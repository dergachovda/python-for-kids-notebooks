#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

from release_manager import LESSONS_DIR, ReleaseManager


def print_status(manager, state):
    total = len(manager.chapters)
    practice_count = len(state["unlocked_practice"])
    solution_count = len(state["unlocked_solutions"])

    print("\n== Current Progress ==")
    print(f"Practice unlocked: {practice_count}/{total}")
    print(f"Solutions unlocked: {solution_count}/{total}")

    if practice_count:
        print("\nUnlocked practice chapters:")
        for slug in state["unlocked_practice"]:
            print(f"- {slug}")
    else:
        print("\nUnlocked practice chapters: none")

    if solution_count:
        print("\nUnlocked solution chapters:")
        for slug in state["unlocked_solutions"]:
            print(f"- {slug}")
    else:
        print("\nUnlocked solution chapters: none")

    next_practice = manager.next_practice_slug(state)
    next_solution = manager.next_solution_slug(state)

    print("\nNext available unlocks:")
    print(f"- Practice: {next_practice or 'none'}")
    print(f"- Solution: {next_solution or 'none'}")

    print(f"\nStudent content location: {LESSONS_DIR}")


def do_unlock_practice(manager, state, dry_run=False):
    slug = manager.next_practice_slug(state)
    if not slug:
        print("All practice chapters are already unlocked.")
        return False

    if dry_run:
        print(f"[Dry-run] Would unlock practice: {slug}")
        return False

    manager.unlock_next_practice(state)
    manager.save_state(state)
    print(f"Unlocked practice: {slug}")
    return True


def do_unlock_solution(manager, state, dry_run=False):
    slug = manager.next_solution_slug(state)
    if not slug:
        print("No solution chapter is available to unlock.")
        return False

    if dry_run:
        print(f"[Dry-run] Would unlock solutions for: {slug}")
        return False

    manager.unlock_next_solution(state)
    manager.save_state(state)
    print(f"Unlocked solutions for: {slug}")
    return True


def do_reset(manager, state):
    _ = state
    confirmation = input("Type YES to reset progress and clean lessons output: ").strip()
    if confirmation != "YES":
        print("Reset cancelled.")
        return

    new_state = manager._default_state()
    manager.reset_lessons_output()
    manager.save_state(new_state)
    manager.sync_unlocked_content(new_state)
    print("Progress reset complete. Initial chapter practice has been restored.")


def interactive_menu(manager):
    state = manager.load_state()
    manager.sync_unlocked_content(state)

    while True:
        print("\n=== Python for Kids Release Menu ===")
        print("1) Show status")
        print("2) Unlock next chapter practice")
        print("3) Unlock next chapter solutions")
        print("4) Dry-run unlock preview")
        print("5) Reset progress and clean lessons")
        print("6) Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            print_status(manager, state)
        elif choice == "2":
            changed = do_unlock_practice(manager, state)
            if changed:
                state = manager.load_state()
        elif choice == "3":
            changed = do_unlock_solution(manager, state)
            if changed:
                state = manager.load_state()
        elif choice == "4":
            do_unlock_practice(manager, state, dry_run=True)
            do_unlock_solution(manager, state, dry_run=True)
        elif choice == "5":
            do_reset(manager, state)
            state = manager.load_state()
        elif choice == "6":
            print("Bye. Keep learning.")
            return
        else:
            print("Unknown option. Please choose 1-6.")


def main():
    parser = argparse.ArgumentParser(description="Interactive chapter disclosure manager")
    parser.add_argument(
        "command",
        nargs="?",
        default="menu",
        choices=["menu", "status", "unlock-practice", "unlock-solution", "dry-run", "reset"],
        help="Command to run",
    )
    args = parser.parse_args()

    try:
        manager = ReleaseManager()
    except FileNotFoundError as exc:
        print(f"Setup error: {exc}")
        print("Make sure you are running this from the project root directory.")
        sys.exit(1)

    state = manager.load_state()
    manager.sync_unlocked_content(state)

    if args.command == "menu":
        interactive_menu(manager)
        return

    if args.command == "status":
        print_status(manager, state)
        return

    if args.command == "unlock-practice":
        do_unlock_practice(manager, state)
        return

    if args.command == "unlock-solution":
        do_unlock_solution(manager, state)
        return

    if args.command == "dry-run":
        do_unlock_practice(manager, state, dry_run=True)
        do_unlock_solution(manager, state, dry_run=True)
        return

    if args.command == "reset":
        do_reset(manager, state)
        return

    print("Unsupported command.")
    sys.exit(1)


if __name__ == "__main__":
    main()
