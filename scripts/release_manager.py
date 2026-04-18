#!/usr/bin/env python3
import json
import shutil
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT_DIR / ".content"
LESSONS_DIR = ROOT_DIR / "lessons"
STATE_DIR = ROOT_DIR / ".state"
STATE_FILE = STATE_DIR / "progress.json"
MANIFEST_FILE = CONTENT_DIR / "manifest.json"


class ReleaseManager:
    def __init__(self):
        self.manifest = self._load_manifest()
        self.chapters = self.manifest["chapters"]
        self.chapter_slugs = [chapter["slug"] for chapter in self.chapters]
        self.initial_unlock = self.manifest.get("initial_unlock", {})

    def _load_manifest(self):
        if not MANIFEST_FILE.exists():
            raise FileNotFoundError(f"Missing manifest file: {MANIFEST_FILE}")

        with MANIFEST_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _default_state(self):
        return {
            "unlocked_practice": list(self.initial_unlock.get("practice", [])),
            "unlocked_solutions": list(self.initial_unlock.get("solutions", [])),
        }

    def load_state(self):
        if not STATE_FILE.exists():
            return self._default_state()

        with STATE_FILE.open("r", encoding="utf-8") as f:
            state = json.load(f)

        state.setdefault("unlocked_practice", [])
        state.setdefault("unlocked_solutions", [])

        # Keep only chapters that exist in manifest.
        state["unlocked_practice"] = [
            slug for slug in state["unlocked_practice"] if slug in self.chapter_slugs
        ]
        state["unlocked_solutions"] = [
            slug for slug in state["unlocked_solutions"] if slug in self.chapter_slugs
        ]
        return state

    def save_state(self, state):
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        with STATE_FILE.open("w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)
            f.write("\n")

    def chapter_by_slug(self, slug):
        for chapter in self.chapters:
            if chapter["slug"] == slug:
                return chapter
        raise KeyError(f"Unknown chapter slug: {slug}")

    def copy_files(self, slug, file_list):
        source_dir = CONTENT_DIR / slug
        target_dir = LESSONS_DIR / slug
        target_dir.mkdir(parents=True, exist_ok=True)

        for relative in file_list:
            src = source_dir / relative
            dst = target_dir / relative
            if not src.exists():
                raise FileNotFoundError(f"Missing source file for chapter '{slug}': {src}")
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    def sync_unlocked_content(self, state):
        LESSONS_DIR.mkdir(parents=True, exist_ok=True)

        for slug in state["unlocked_practice"]:
            chapter = self.chapter_by_slug(slug)
            self.copy_files(slug, chapter.get("practice_files", []))

        for slug in state["unlocked_solutions"]:
            chapter = self.chapter_by_slug(slug)
            self.copy_files(slug, chapter.get("solution_files", []))

    def next_practice_slug(self, state):
        unlocked = set(state["unlocked_practice"])
        for chapter in self.chapters:
            if chapter["slug"] not in unlocked:
                return chapter["slug"]
        return None

    def next_solution_slug(self, state):
        unlocked_practice = set(state["unlocked_practice"])
        unlocked_solutions = set(state["unlocked_solutions"])

        for chapter in self.chapters:
            slug = chapter["slug"]
            if slug not in unlocked_practice:
                continue
            if slug in unlocked_solutions:
                continue
            if chapter.get("solution_files"):
                return slug
        return None

    def unlock_next_practice(self, state):
        slug = self.next_practice_slug(state)
        if not slug:
            return None

        if slug not in state["unlocked_practice"]:
            state["unlocked_practice"].append(slug)
        chapter = self.chapter_by_slug(slug)
        self.copy_files(slug, chapter.get("practice_files", []))
        return slug

    def unlock_next_solution(self, state):
        slug = self.next_solution_slug(state)
        if not slug:
            return None

        if slug not in state["unlocked_solutions"]:
            state["unlocked_solutions"].append(slug)
        chapter = self.chapter_by_slug(slug)
        self.copy_files(slug, chapter.get("solution_files", []))
        return slug

    def chapter_title(self, slug):
        chapter = self.chapter_by_slug(slug)
        return chapter.get("title", slug)

    def reset_lessons_output(self):
        if LESSONS_DIR.exists():
            shutil.rmtree(LESSONS_DIR)
        LESSONS_DIR.mkdir(parents=True, exist_ok=True)
        (LESSONS_DIR / ".gitkeep").touch()
