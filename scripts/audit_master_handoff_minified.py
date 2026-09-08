#!/usr/bin/env python3
"""Mechanical contract for the compact self-contained master handoff.

This checks structure, literal finite certificates, and common corruption
patterns. It complements rather than replaces a proof audit.
"""

from __future__ import annotations

import hashlib
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "MASTER_HANDOFF.md")
text = TARGET.read_text()
raw = TARGET.read_bytes()
errors: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def section(start: str, end: str) -> str:
    require(text.count(start) == 1, f"section start is not unique: {start}")
    require(text.count(end) == 1, f"section end is not unique: {end}")
    if text.count(start) != 1 or text.count(end) != 1:
        return ""
    i = text.index(start)
    j = text.index(end, i)
    return text[i:j]


# Size and byte hygiene.
require(len(raw) <= 339_968, f"handoff exceeds 332 KiB: {len(raw)} bytes")
bad_controls = [(i, b) for i, b in enumerate(raw) if b < 32 and b not in (10,)]
require(not bad_controls, f"control bytes present: {bad_controls[:8]}")
require(b"\r" not in raw and b"\t" not in raw, "CR or tab characters present")
require(text.endswith("\n"), "file must end with one newline")


# Required architecture/status statements.
required = [
    "Set `B(0)=0`.",
    r"\boxed{\nu(k)\le(c_4+o(1))W(k),\qquad c_4<1.27.}",
    "## Appendix A.5: Four-block cross-split full-cube bound [I]",
    "## Appendix A.6: Centered terminal-rectangle ledger barrier [I]",
    "Bridge and floor errors contribute",
    "The support split changes with the tuple.",
    "The bound concerns designated paired rectangles and their bridge cost.",
    "four-block full-cube upper bound | [I]",
    "grouped cylinders/three-block precursor | [I]",
    "centered terminal-rectangle floor | [I]",
    "There is an overlap-sensitive top-bit splice.",
    r"24313=B(17)\le\nu(17)\le25745",
    "**Reversed boundary splice [I]+[W].**",
    r"d\le n-W(k)",
    "The historically decisive breakthrough for each closed dimension was:",
    "the sole permitted self-containment exception [W]",
    "### 2.3 Cyclic finite certificates and safe erasure [I]",
    r"\boxed{\mu(7)=35=W(7).}",
    r"\boxed{\mu(5)=12}",
    "assert (n,q)==(246730,242)",
    "59,118,199,219,236,285,355,365,398,433,438,472",
    "There are three logically separate compiler branches:",
    "### 3.4 High OR-derivative compiler [I]/[C]",
    "### 3.5 Deterministic truncated-bridge band compiler [I]",
    r"\boxed{W(2b)\le\nu_h(2b)\le W(2b)+(2h+3)W(b-1)W(b)",
    r"F(c)=\sqrt2\,\operatorname {erf}(\sqrt2c)",
    "### 3.5A Exact coverage and fixed-split completion barriers [I]",
    r"\eta_0=e^{-1/\pi}-\operatorname {erfc}(1/\sqrt\pi)",
    r"P(c)={2\over\pi}\mathbb E(X_cY_c)",
    r"N\ge W(b)(2^b-2)=(\sqrt2-o(1))W(2b)",
    "maximal alternating half-supported",
    "These results constrain only appends to (3.12)",
    "This excludes only that independent-residual model.",
    "### 3.6 Architecture-free adjacent shadows and a GK-block obstruction [I]/[C]",
    r"\boxed{h_-\le2t,\qquad h_+\le2t.}",
    r"N\ge(9/8-o(1))W",
    "### 3.7 Union recoding and cumulative difference cycles [I]",
    r"|\mathcal U_s(B)\setminus\mathcal U_s(A)|",
    r"\sum_i\delta_i=M\operatorname {Cat}_r",
    r"{1\over h(S)}\sum_{j=1}^s\binom{g_j-1}{r-s+1}",
    "any fixed number of these blocks",
    "not automatically an",
    "### 3.8 Cyclic normalization and exact-width rigidity [I]",
    r"W(k)\le\mu(k)\le\nu(k)\le\mu(k)+(k-2)_+",
    r"\boxed{\nu(k)=(1+o(1))W(k)\iff\mu(k)=(1+o(1))W(k).}",
    r"\mu(17)=24310\Longrightarrow\nu(17)\le24325",
    "### 3.9 Sublinear-dimension cylinder completion [I]/[C]",
    "### 3.10 Facet-forest repair and exact envelope deficiency [I]/[C]",
    "### 3.11 Prescribed Catalan matching extension [I]/[C]",
    "### 3.12 Quantitative inherited-symmetry breaking [I]",
    "Ordinary regularity alone would not prove it.",
    r"\Delta_C=h_6+\beta_C",
    r"\det H={41\over61740}\ne0",
    r"\det A_{\mathcal W}/\det A=-893/128125\ne0",
    "These are adjacency bounds, not extra-letter costs.",
    r"\boxed{\nu(k+t)\le2^t\{m+(k-2)_+\}+h\{\nu(t)+1\}.}",
    "equivalent existence",
    "not an almost-cover construction",
    "## Appendix C.5a: Average-conflict descent and bounded arrival test [I]/[C]",
    r"\boxed{\Delta_C^2\le qZ\bar C",
    r"\kappa<1-6\alpha",
    "The child is evaluated before discarding it for a new cap violation.",
    "## I.7 Density-hole selectors after dimension extension [C]/[O]",
    "No near-width density-almost-cover family is constructed",
    "### 4.4 Gates A and B already imply coefficient one [C]",
    "## Appendix A.4: A short far-rank repair [I]",
    r"Gate \(C_{\rm F}\)",
    "a DCC construction itself are [O]",
    "the missing output remains the compatible all-depth positive cover stated",
    "The exact missing stopped-law input is [O]:",
    r"\kappa<2-20\alpha",
    "## Appendix C.12: Signed sixth-moment collision forcing",
    "## Appendix C.12a: Deterministic post-purge stability",
    "## H.14 Uniform all-depth conditioning of the sixteen-atom bank [I]",
    "## H.15A Exact \\(j=2\\) six-vertex rooted-core determinant [I]",
    "## I.3A The all-pairing coherent-tour orbit [I]",
    "## I.3 All-band pairing catalogues",
    "## I.4 Cyclic derivative of internal collisions",
    "## I.5 Quadratic-moment balanced code",
    "## I.1A Phase-packet banks and the separate-block gate",
    r"### Gate \(C_{\rm Q}\) [O]",
    r"\boxed{{\Delta_2\over D_{\rm pkt}}",
    "cross-join cleanliness are unnecessary.",
    "Archived GK/Dyck branch (status only; not a premise)",
    "stopped pre-purge scalar sum (C.12a.24) and removed-edge sum (C.12a.25)",
    "No packet-boundary repair or common symmetric-chain factor is needed.",
    "deterministic central band | [I]",
    "append/fixed-split barriers | [I]",
    "union-preserving recoding | [I]",
    "cumulative difference cycles | [I]",
    "cyclic normalization/rigidity | [I]",
    "cylinder completion/almost-cover equivalence | [I]/[C]",
    "average-conflict descent/bounded test | [I]/[C]",
    "density-hole selectors | [C]/[O]",
    "cyclic finite certificates/safe erasure | [I]",
    "bordered top-bit splice | [I]+[W]",
    "adjacent shadows/GK chronology | [I]/[C]",
    "full coefficient one | [O] | no assembled construction",
]
for needle in required:
    require(needle in text, f"required statement missing: {needle}")

for forbidden in [
    "MATH_THEOREM_",
    "MATH_REDUCTION_",
    "MATH_AUDIT_",
    "scratch/",
    "answers/k17_upper25746.word",
    "cited implementation",
    "G.17",
    "phase atom",
    "conditional only on persistence",
    "conditional on persistence of the displayed maximum-degree cap",
    "twenty-two factorial blocker terms",
    r"| Gate \(C_{\rm P}\) | [O] |",
    r"M_b:=2b^3+8b^2-16b",
    "\\n\\n",
]:
    require(forbidden not in text, f"forbidden residue present: {forbidden}")

# The only named external mathematical files are the sixteen allowed words.
paths = set(re.findall(r"(?<![A-Za-z0-9_./-])([A-Za-z0-9_./-]+\.(?:md|py|cpp|word|gz))", text))
allowed_paths = {f"answers/k{k:02d}.word" for k in range(1, 17)}
require(paths <= allowed_paths, f"unexpected file references: {sorted(paths - allowed_paths)}")


# Markdown/TeX mechanical balance.
require(text.count("~~~") % 2 == 0, "unbalanced tilde code fences")
require(text.count("```") % 2 == 0, "unbalanced backtick code fences")
lines = text.splitlines()
require(sum(line.strip() == r"\[" for line in lines) ==
        sum(line.strip() == r"\]" for line in lines),
        "unbalanced display-math delimiters")
for env in ["aligned", "array", "cases", "gathered", "split"]:
    require(text.count(rf"\begin{{{env}}}") == text.count(rf"\end{{{env}}}"),
            f"unbalanced TeX environment: {env}")
lone_slashes = [i for i, line in enumerate(lines, 1)
                if line.rstrip().endswith("\\") and not line.rstrip().endswith("\\\\")]
require(not lone_slashes, f"lone terminal TeX backslashes on lines {lone_slashes[:12]}")

tags = re.findall(r"\\tag\{([^}]+)\}", text)
duplicates = [tag for tag, count in Counter(tags).items() if count > 1]
require(not duplicates, f"duplicate equation tags: {duplicates[:12]}")


# Exact finite-history table preservation.
history = section(
    "The historically decisive breakthrough for each closed dimension was:",
    "This table is historical provenance",
)
history_hash = hashlib.sha256(history.encode()).hexdigest()
require(
    history_hash == "8c4c093b2e8c3430df22bd8b193de1d827ab0692e00eebbba5e43bd8529ace0b",
    f"finite breakthrough table changed: {history_hash}",
)
history_rows = re.findall(r"^\|\s*(\d+)\s*\|\s*(\d+)\s*\|", history, re.M)
require([int(k) for k, _ in history_rows] == list(range(17)),
        "breakthrough table must contain exactly k=0,...,16 in order")


# Literal [W] certificates: hashes, lengths, and mathematical verification.
expected = {
    1: (1, "4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865"),
    2: (2, "f251ddc12234e0da8d3b778bd0f7463fb477f16f47757f5617dc8b4ff4d4f14a"),
    3: (4, "aafa934d13be209cc39a9b5cb0b140af652fc0eebd127c42c6c982422964a790"),
    4: (7, "efe145ebc697686a2e3bf53a36362b5025835f2eb0ba16a1a0e64e2abd4ec1ca"),
    5: (12, "72195450d0361b37fbf58442203014eff475b3f59222c907fab99743106eee06"),
    6: (21, "7d30e058f98e6c09d65515e3f3971ae8bd7637f711670fa06a8a1dc536852d6d"),
    7: (37, "dda4b06c2e35bda3ea8a876a90807172adee166567d84b587ef5ae68cae9bec7"),
    8: (72, "df6d76b468bd816fd014d9b6f5259ba60e5f1ea06e4c4313901fe6155c8780eb"),
    9: (128, "c7e8cbfbe1a3531ffae4c9a01bd4b3b51dad0856b38486bacc56dbcaa73e3221"),
    10: (254, "24b6fc4f4c054e46ef54553ca37eded126150542d51a61256a837d666e0c74fd"),
    11: (465, "746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850"),
    12: (926, "6d598c62f5925d1d2dfce8279eea82069318bd93ff66d0b204c639cf06297851"),
    13: (1719, "8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0"),
    14: (3434, "7d94117099bbb46402e8f4edda718dae7eb10e2e5e34e9b588e08a198b43db17"),
    15: (6438, "f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b"),
    16: (12873, "890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe"),
}
for k, (expected_length, expected_hash) in expected.items():
    path = ROOT / f"answers/k{k:02d}.word"
    require(path.is_file(), f"word missing: {path.relative_to(ROOT)}")
    if not path.is_file():
        continue
    body = path.read_bytes()
    require(hashlib.sha256(body).hexdigest() == expected_hash,
            f"word hash mismatch at k={k}")
    masks = [int(value) for value in body.split()]
    require(len(masks) == expected_length, f"word length mismatch at k={k}")
    require(all(0 < value < (1 << k) for value in masks),
            f"out-of-range mask at k={k}")
    ending: set[int] = set()
    seen: set[int] = set()
    for value in masks:
        ending = {value} | {prior | value for prior in ending}
        seen |= ending
    require(seen == set(range(1, 1 << k)), f"word is not universal at k={k}")
    row = rf"| {k} | {expected_length} | {expected_hash} |"
    require(row in text, f"word table row missing or changed at k={k}")

# The bordered splice records that the literal k=16 certificate has no border.
k16 = [int(value) for value in (ROOT / "answers/k16.word").read_bytes().split()]
prefix = [0] * len(k16)
for i in range(1, len(k16)):
    j = prefix[i - 1]
    while j and k16[i] != k16[j]:
        j = prefix[j - 1]
    if k16[i] == k16[j]:
        j += 1
    prefix[i] = j
require(prefix[-1] == 0, f"k=16 certificate has border {prefix[-1]}")

# Reconstruct k=17 from the allowed k=16 body, not a new external premise.
appendix_b = section(
    "# Appendix B: The sole self-containment exception",
    "# Appendix C: Complete proofs for the direct punctured route",
)
verifiers = re.findall(r"~~~python\n(.*?)\n~~~", appendix_b, re.S)
splices = re.findall(r"```python\n(.*?)\n```", appendix_b, re.S)
require(len(verifiers) == len(splices) == 1, "Appendix B must contain the verifier and splice replay")
if len(verifiers) == len(splices) == 1:
    try:
        scope = {"X": k16}
        exec(compile(verifiers[0], "<embedded word verifier>", "exec"), scope)
        exec(compile(splices[0], "<embedded k17 splice>", "exec"), scope)
        payload = (" ".join(map(str, scope["Y"])) + "\n").encode()
        require(
            hashlib.sha256(payload).hexdigest()
            == "ef69969f6f72bc85173c9ccb413b7c111a398e725b956f2a91cbe5decbabca38",
            "reconstructed k=17 word hash mismatch",
        )
    except Exception as exc:
        errors.append(f"embedded k17 splice failed: {type(exc).__name__}: {exc}")

# Execute the compact exhaustive finite-cycle verifier embedded in the master.
cyclic = section(
    "### 2.3 Cyclic finite certificates and safe erasure [I]",
    "## 3. Exact compiler facts and the asymptotic reduction",
)
blocks = re.findall(r"```python\n(.*?)\n```", cyclic, re.S)
require(len(blocks) == 1, "section 2.3 must contain one Python verifier")
if len(blocks) == 1:
    try:
        exec(compile(blocks[0], "<embedded cyclic verifier>", "exec"), {})
    except Exception as exc:
        errors.append(f"embedded cyclic verifier failed: {type(exc).__name__}: {exc}")


# Verify the small prescribed-extension certificate, not a matching search.
catalan = section(
    "### 3.11 Prescribed Catalan matching extension [I]/[C]",
    "### 3.12 Quantitative inherited-symmetry breaking [I]",
)
blocks = re.findall(r"```python\n(.*?)\n```", catalan, re.S)
require(len(blocks) == 1, "section 3.11 must contain one rational orbit check")
if len(blocks) == 1:
    try:
        exec(compile(blocks[0], "<embedded Catalan inverse block>", "exec"), {})
    except Exception as exc:
        errors.append(f"Catalan inverse block failed: {type(exc).__name__}: {exc}")

# Execute the full rational certificate, including its integration error.
four_block = section(
    "## Appendix A.5: Four-block cross-split full-cube bound [I]",
    "## Appendix A.6: Centered terminal-rectangle ledger barrier [I]",
)
blocks = re.findall(r"```python\n(.*?)\n```", four_block, re.S)
require(len(blocks) == 1, "Appendix A.5 must contain one rational verifier")
if len(blocks) == 1:
    try:
        exec(compile(blocks[0], "<embedded four-block verifier>", "exec"), {})
    except Exception as exc:
        errors.append(f"embedded four-block verifier failed: {type(exc).__name__}: {exc}")


if errors:
    print(f"FAIL: {TARGET} ({len(errors)} errors)")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print(
    f"PASS: {TARGET} | {len(raw)} bytes | {len(tags)} unique tags | "
    "16 hashes and universality certificates verified | rational c4 < 1.27 verified"
)
