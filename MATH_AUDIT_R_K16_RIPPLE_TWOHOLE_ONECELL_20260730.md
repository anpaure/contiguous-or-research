# Independent audit of the corrected K16 ripple two-hole seed

## 1. Artifact reconciliation and verdict

There are two different length-12,874 files, differing at exactly one
zero-based position.

| file | SHA-256 | cell 6440 | exact missing set |
|---|---|---:|---|
| `scratch/k16_ripple_insert12874_onehole.word` | `5ac147eca512b7e398c7217f1796836f454a304274c6e54fda7050fc9b4f66db` | `0xa069` | `{0x287d}` |
| `scratch/k16_12874_twohole_partial.word` | `a62cb41fc97127edbac362afa0447cf6a45d795f327ec7f2a3652f7c12873181` | `0x2069` | `{0xa879,0xa87d}` |

Thus the historically named `onehole` file is, at the time of this audit,
still literally a one-hole word.  The second row is the intended corrected
two-hole seed.  Every theorem below concerns that SHA-pinned second row.

An independent suffix-OR recurrence recomputed all 65,535 nonempty targets;
the two missing decimal masks are exactly 43,129 and 43,133.

## 2. Relation to the authenticated basin and retained upper bound

Let `P=scratch/k16_12873_repaired_partial.word`, SHA-256
`0a70a67eced48a82883a698c6fd25688a27c52faf19e3fa11bbbd9a78581bea6`.
The corrected seed is reconstructed exactly by making the following six
zero-based replacements in `P`, then inserting `0x0864` at gap 12,870:

| old position in `P` | old | new |
|---:|---:|---:|
| 6440 | `0xa069` | `0x2069` |
| 6441 | `0x806d` | `0x006d` |
| 6497 | `0x886a` | `0x8862` |
| 12870 | `0x8c62` | `0x8c63` |
| 12871 | `0x8c61` | `0xcc61` |
| 12872 | `0xcc41` | `0xce41` |

The currently retained upper certificate is instead
`P || (0x0200,0x287d)`, SHA-256
`d4690a0d11f1d8e69765ec988d9fbcbac63d354ebd6ab07aa8081b577a9ac0c9`.
The two constructions therefore share the authenticated basin but use
different boundary repairs.

## 3. Exact witness exchange

Put

\[
h_0=0xa879,\qquad h_1=0xa87d=h_0\lor0x0004.
\]

Both `P` and the SHA-`5ac1...` one-hole word have exactly one witness for
each high target:

\[
h_0:[6439,6440],\qquad h_1:[6439,6441].
\]

Clearing bit 15 at cell 6440 from `0xa069` to `0x2069` destroys precisely
those unique high witnesses.  In the corrected two-hole word their projected
windows are

\[
0x2879:[6439,6439],[6439,6440],\qquad
0x287d:[6439,6441].
\]

In particular, the old low hole `0x287d` is now filled uniquely, while the
two high targets become the exact holes.  This is a literal balanced exchange,
not a one-hole seed.

For completeness, the following is the complete census of downward
Hamming-distance-one near witnesses in the corrected seed.  Bits are numbered
from zero at the least significant bit; each entry lists every witness of
`h_i` with that one bit deleted.

| target | deleted bit | deficient mask | all intervals |
|---|---:|---:|---|
| `0xa879` | 0 | `0xa878` | `[9621,9622]` |
| | 3 | `0xa871` | `[6603,6604]` |
| | 4 | `0xa869` | `[9957,9958]` |
| | 5 | `0xa859` | `[11271,11272]` |
| | 6 | `0xa839` | `[7651,7652]`, `[12360,12361]` |
| | 11 | `0xa079` | `[12369,12370]` |
| | 13 | `0x8879` | `[8153,8154]` |
| | 15 | `0x2879` | `[6439,6439]`, `[6439,6440]` |
| `0xa87d` | 0 | `0xa87c` | `[9621,9623]` |
| | 2 | `0xa879` | none (the other hole) |
| | 3 | `0xa875` | `[6992,6994]` |
| | 4 | `0xa86d` | `[0,2]`, `[0,3]` |
| | 5 | `0xa85d` | `[11271,11273]` |
| | 6 | `0xa83d` | `[12360,12362]` |
| | 11 | `0xa07d` | `[12369,12371]` |
| | 13 | `0x887d` | `[8153,8155]` |
| | 15 | `0x287d` | `[6439,6441]` |

## 4. Exact one-cell surgery criterion

The audit uses the following necessary-and-sufficient finite criterion, so it
does not confuse hitting the two holes with preserving all old targets.

For insertion at gap `g`, let `L_g` be zero together with all ORs of suffixes
ending immediately left of the gap, and let `R_g` be zero together with all
ORs of prefixes starting immediately right of it.  Put

\[
C_g=\{\ell\lor r:\ell\in L_g, r\in R_g\}.
\]

Let `E_g` be the set of old targets every one of whose witnesses crosses the
gap.  Inserting a nonzero cell `v` gives a universal word if and only if

\[
\forall t\in\{h_0,h_1\}\cup E_g\quad
\exists c\in C_g: c\lor v=t. \tag{I}
\]

Indeed, exactly the crossing old intervals are lost, and exactly the labels
`c OR v` are gained.  Since every new witness of both holes contains `v`, it
is necessary that `v` be a nonzero submask of
`h_0 AND h_1 = h_0`; this leaves 255 values.

For replacement at position `p`, define `L_p,R_p` using the cells strictly to
the left and right, and let `E_p` be the targets all of whose witnesses use
cell `p`.  Replacing the cell by `v` is universal if and only if the analogous
condition

\[
\forall t\in\{h_0,h_1\}\cup E_p\quad
\exists c\in C_p: c\lor v=t 
\tag{R}
\]

holds.  The checker computes `E_g,E_p` from exact interval multiplicities.
Equations (I) and (R) are the complete one-cell constraints.

## 5. Complete census

Ignoring endangered old targets, insertion has 5,730 `(gap,v)` rows over 520
gaps that can hit both holes.  Their canonical row digest is
`5761bb1d682b6076404f93997c97acd9ff11332a639d0e175aa79fb91c52b17e`.
After imposing (I), exactly one row remains:

\[
(g,v)=(0,0xa879).
\]

Thus prepending `0xa879` gives a universal length-12,875 word.  In that word
the complete new witness lists are

\[
h_0:[0,0],\qquad
h_1:[0,1],[0,2],[0,3],[0,4].
\]

Its canonical space-separated serialization would have SHA-256
`74d9aa13a6b9dae664ccbaa744a16efa724acbafee2ed44afc5462a03c5bc441`.
It is an alternative certificate of the existing upper bound, not an
improvement.  In particular, the append gap has no candidate; the successful
insertion is uniquely the prepend row.

For replacement, 4,192 `(p,v)` rows over 515 positions hit both holes in the
relaxation.  Their canonical row digest is
`e15c9e388367672ad99bb570a2a2cc1181fc4961e9ccf25c6431e6e14cbc42f0`.
After imposing (R), **no row remains**.  Therefore no one-cell replacement of
this exact corrected seed is universal: this entire radius-one replacement
neighborhood cannot improve the upper bound to 12,874.

This is scoped to the SHA-`a62c...` seed.  It does not exclude two or more
coordinated replacements, nor a different length-12,874 basin.

## 6. Reproducer

The independent fail-closed checker is
`scratch/audit_r_k16_ripple_twohole_onecell_20260730.py`.  It also asserts the
complete near-witness table and directly replays the unique prepended word.
