"""Run with python3 tests/check_scripts.py; tests the documented shell function."""

from pathlib import Path
import re
import subprocess
import tempfile


contract = Path(__file__).resolve().parents[1] / "references/output-contract.md"
shell = re.search(r"```sh\n(.*?)\n```", contract.read_text(), re.S).group(1)


def check(*paths):
    return subprocess.run(
        ["sh", "-ec", shell + '\ncheck_scripts "$@"', "check_scripts", *map(str, paths)],
        capture_output=True,
        text=True,
    ).returncode


with tempfile.TemporaryDirectory(prefix="briefcast-check-") as directory:
    primary = Path(directory) / "brief.primary.md"
    secondary = Path(directory) / "brief.secondary.md"
    primary.write_text("今天我们聊聊科学。\n\n这是第二段。\n")
    assert check(primary) == 0, "primary-only output should pass"
    assert check(primary, secondary) == 2, "missing enabled language should fail"
    secondary.write_text("Today we talk about science.\n")
    assert check(primary, secondary) == 0, "bilingual output should pass"
    assert check() == 2, "no scripts is an execution error"

    invalid = [
        "", " \n\t", "# Heading", "  # Heading", "- Story", "1. Story", "2) Story",
        "This is *important*.", "This is **important**.", "This is _important_.",
        "This is __important__.", "Use `Agent`.", "A finding.[^1]", "A finding.[1]",
        "Read [more](https://example.com/story).", "Visit https://example.com/story.",
        "Visit www.example.com.", "![image](image.png)", "> Quote", "| A | B |",
        "---", "_ _ _", "~~Deleted~~",
    ]
    for body in invalid:
        primary.write_text(body + "\n")
        assert check(primary) == 1, f"missed non-speakable text: {body!r}"

    primary.write_text("Good primary script.\n")
    secondary.write_text("A finding.[^1]\n")
    assert check(primary) == 0, "disabled leftover secondary must be ignored"
    assert check(primary, secondary) == 1, "enabled secondary must be checked"

print("Script checks passed (primary-only, bilingual, errors, empty and formatted drafts).")
