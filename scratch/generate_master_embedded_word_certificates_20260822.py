#!/usr/bin/env python3
"""Emit a self-contained fixed-width base-36 certificate appendix.

The generated text contains all word data for k=1,...,16 and an executable
exact suffix-OR verifier.  It reads repository files only while generating;
the emitted appendix has no file dependency.
"""

from pathlib import Path
import textwrap


ROOT = Path(__file__).resolve().parents[1]
DIGITS = "0123456789abcdefghijklmnopqrstuvwxyz"
EXPECTED = {
    1: 1,
    2: 2,
    3: 4,
    4: 7,
    5: 12,
    6: 21,
    7: 37,
    8: 72,
    9: 128,
    10: 254,
    11: 465,
    12: 926,
    13: 1719,
    14: 3434,
    15: 6438,
    16: 12873,
}


def base36(value: int, width: int) -> str:
    out = ""
    while value:
        out = DIGITS[value % 36] + out
        value //= 36
    return (out or "0").rjust(width, "0")


def exact_check(k: int, word: list[int]) -> None:
    assert all(0 < x < (1 << k) for x in word)
    ending: set[int] = set()
    seen: set[int] = set()
    for x in word:
        ending = {x} | {y | x for y in ending}
        seen |= ending
    assert seen == set(range(1, 1 << k))


records: list[tuple[int, int, int, str]] = []
for k, expected_length in EXPECTED.items():
    word_path = ROOT / "answers" / f"k{k:02d}.word"
    word = [int(token) for token in word_path.read_text().split()]
    assert len(word) == expected_length
    exact_check(k, word)
    width = 1
    while 36**width < 2**k:
        width += 1
    payload = "".join(base36(x, width) for x in word)
    assert len(payload) == width * expected_length
    records.append((k, expected_length, width, payload))

print("<details>")
print("<summary>Embedded exact finite word certificates (expand)</summary>")
print()
print("```python")
print("# Base-36 digits have values 0,...,35 in the displayed order.")
print("DIGITS = '0123456789abcdefghijklmnopqrstuvwxyz'")
print("CERTIFICATES = {")
for k, length, width, payload in records:
    print(f"    {k}: ({length}, {width}, r'''" )
    print(textwrap.fill(payload, width=100))
    print("'''),")
print("}")
print()
print("def decode_and_check(k, n, width, payload):")
print("    s = ''.join(payload.split())")
print("    assert len(s) == n * width")
print("    value = {c: i for i, c in enumerate(DIGITS)}")
print("    def decode(token):")
print("        x = 0")
print("        for c in token:")
print("            x = 36*x + value[c]")
print("        return x")
print("    word = [decode(s[i:i+width]) for i in range(0, len(s), width)]")
print("    assert len(word) == n and all(0 < x < (1 << k) for x in word)")
print("    ending, seen = set(), set()")
print("    for x in word:")
print("        ending = {x} | {y | x for y in ending}")
print("        seen |= ending")
print("    assert seen == set(range(1, 1 << k))")
print()
print("for k, (n, width, payload) in CERTIFICATES.items():")
print("    decode_and_check(k, n, width, payload)")
print("print('embedded certificates k=1,...,16: PASS')")
print("```")
print()
print("</details>")
