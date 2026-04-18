# python-for-kids-notebooks

Interactive Jupyter notebooks for learning Python based on *Python for Kids* by Jason R. Briggs.

Original book page: [Python for Kids, 2nd Edition](https://nostarch.com/python-kids-2nd-edition)

This repository now uses a guided release workflow so students do not see all chapters immediately.

## Who is this for?

- Kids who are new to coding
- Absolute beginners
- Parents and teachers who want a structured path

## Learning goals

- Learn Python chapter-by-chapter
- Practice first, then reveal solutions
- Keep momentum with small, clear steps

## Guided Learning Release

Content is stored in a hidden author source folder and copied into a student-facing folder as chapters are unlocked.

- Author source: `.content/`
- Student workspace: `lessons/`
- Local progress state: `.state/progress.json`

### Unlock model

Each chapter has two unlock stages:

1. Practice stage: `theory.md` + `exercises.ipynb`
1. Solution stage: `solutions.ipynb`

This helps students focus on trying tasks before seeing answers.

## Quick Start

Recommended Python version: 3.14+

1. Initialize the workspace automatically:

```bash
# Windows
init.bat

# Bash (Git Bash, Linux, macOS)
./init.sh
```

1. Optional: manual setup (if you do not use init scripts):

1. Create a Python virtual environment:

```bash
python -m venv .venv
```

1. Activate the environment:

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Git Bash)
source .venv/Scripts/activate

# Linux/macOS
source .venv/bin/activate
```

1. Install dependencies:

```bash
pip install -r requirements.txt
```

1. Start interactive release menu:

```bash
# Windows
run.bat

# Bash (Git Bash, Linux, macOS)
./run.sh
```

1. Open notebooks from the `lessons/` folder.

## Script Commands

You can use interactive menu mode or direct commands.

```bash
# Show status
python scripts/release.py status

# Unlock next chapter practice
python scripts/release.py unlock-practice

# Unlock next chapter solutions
python scripts/release.py unlock-solution

# Preview what would unlock next
python scripts/release.py dry-run

# Reset progress and clean generated lessons output
python scripts/release.py reset
```

## Repository Structure

```text
python-for-kids-notebooks/
|
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- run.bat
|-- run.sh
|
|-- scripts/
|   |-- release.py
|   `-- release_manager.py
|
|-- .content/
|   |-- manifest.json
|   |-- chapter-01-getting-started/
|   |-- chapter-02-variables-and-input/
|   |-- chapter-03-conditionals/
|   |-- chapter-04-loops/
|   |-- chapter-05-lists/
|   |-- chapter-06-dictionaries-and-tuples/
|   |-- chapter-07-functions/
|   |-- chapter-08-files-and-errors/
|   |-- chapter-09-modules-and-project-structure/
|   |-- chapter-10-classes-and-objects/
|   |-- chapter-11-turtle-graphics/
|   |-- chapter-12-mini-projects/
|   `-- bonus-mini-project/
|
|-- lessons/
|   `-- .gitkeep
|
`-- assets/
    `-- images/
```

## Implemented Chapters

- Chapter 1: Getting Started
- Chapter 2: Variables and Input
- Chapter 3: Conditionals
- Chapter 4: Loops
- Chapter 5: Lists
- Chapter 6: Dictionaries and Tuples
- Chapter 7: Functions
- Chapter 8: Files and Errors
- Chapter 9: Modules and Project Structure
- Chapter 10: Classes and Objects
- Chapter 11: Turtle Graphics
- Chapter 12: Mini Projects
- Bonus: Guess the Number

All chapters include `theory.md`, `exercises.ipynb`, and `solutions.ipynb` (bonus has project notebook).

## Notes

- This is a guided workflow, not hard content security.
- Progress is local and ignored by git.
- The repository content remains original companion material and does not reproduce book text.

## Contributing

Contributions are welcome.

1. Fork the repository
1. Create a branch
1. Improve content or scripts
1. Open a pull request
