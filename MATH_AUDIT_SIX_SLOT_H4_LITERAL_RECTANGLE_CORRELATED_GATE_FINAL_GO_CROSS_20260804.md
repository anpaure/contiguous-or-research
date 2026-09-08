# Final independent GO audit: six-slot `h=4` literal rectangle gate

**Date:** 2026-08-04  
**Theorem SHA-256:** `533f194ed727b2c15d26ca2007131a3bfc22f08f401097f74d021d40cf5dd5cd`  
**Freeze-manifest SHA-256:** `7b4df9d5e48bdaaff70cfb177ccee999d005b1bae177859590f9c54901c42290`  
**Predecessor fail-closed audit:** `ba3e903140a54bdd24ad9c2af1d486030474b01fe6bc1c0f3a09fd0529fd5deb`

**Verdict:** **PASS / FINAL GO for the stated correlated reduction.**
This replay is limited to the three corrections demanded by the predecessor
audit.  All three are exact, and the manifest verifies every bound file.

## 1. Display repair

The theorem now displays the literal rectangle as

\[
0,\quad u,\quad P,\quad P+u.
\]

The malformed predecessor tokens `0,quad u,quad P,quad P+u` are absent.
This is exactly correction 1.

## 2. Gamma-cap arithmetic repair

The frozen self-audit now gives

\[
{1\over20000}+{1129\over25000}-{57\over1400}
={35+31612-28500\over700000}
={3147\over700000}.
\]

The numerator is `3147`.  The predecessor's mixed-denominator numerator
has been removed.  The theorem's constant and far-end margin are unchanged.
This is exactly correction 2.

## 3. Local-interval dependency repair

Section 7 and the freeze manifest now bind both

\[
\texttt{badc46480b85ef794e784ca2f62273aa6258cdf3dcfecbd915553102c6acd6af}
\]

for the corrected local gate theorem and

\[
\texttt{5781c83357c77dd8216ecbb24ab4739e779d0c65751c7f8aecce1ef43b6ae46c}
\]

for its final independent GO audit.  The stale `340570...` theorem is not
in the successor freeze.  The local positivity through `delta_*` is
therefore authenticated proof lineage rather than an omitted premise.
This is exactly correction 3.

## 4. Manifest and scope

The successor manifest verifies all five entries: theorem, corrected
self-audit, correction map, corrected local theorem, and final local GO
audit.  The correction map accurately states that no rectangle identity,
inequality, constant, far-end margin, or KKT equation changed.

The successor still claims only a correlated necessary gate, far-end
positivity, and a finite KKT stratum list.  It does not claim full interior
positivity.  This matches the mathematical scope previously audited.

\[
\boxed{\textbf{FINAL GO}.}
\]
