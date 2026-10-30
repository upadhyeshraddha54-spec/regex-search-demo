
"""Regex search demo: grep-style matching and sed-style replacement."""
import re

PATTERNS = {
    "1": ("Error word", r"(?i)\berror\b", "WARNING"),
    "2": ("Repeated words", r"\b(\w+)\s+\1\b", "[REPEATED WORD]"),
    "3": ("TODO marker", r"\bTODO\b", "DONE"),
    "4": (".txt filename", r"^[\w-]+\.txt$", "file.md"),
    "5": ("Repeated spaces", r" {2,}", " "),
}


def main():
    print("Regex Search Demo")

    for key, (name, _, _) in PATTERNS.items():
        print(f"  {key}. {name}")

    choice = input("Choose pattern (1-5): ").strip()

    if choice not in PATTERNS:
        print("Invalid choice.")
        return

    name, pattern, replacement = PATTERNS[choice]
    text = input("Enter text: ")

    regex = re.compile(pattern)
    matches = [m.group(0) for m in regex.finditer(text)]

    if matches:
        print("Valid - match found.")
        print("Matches:", matches)
        print("sed-style replacement:", regex.sub(replacement, text))
    else:
        print("Invalid - no match found.")


if __name__ == "__main__":
    main()
