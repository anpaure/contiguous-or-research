# General upper support for the explicit PBBS short-sector path

Date: 2026-09-08. Author: Codex subagent `exact_b_induction`.

Status: algebraic preservation theorem for the first two proper upper
ranks and the coatom rank, plus a bounded complete-upper audit at r=3,...,8.
Preservation of every intermediate upper rank in every dimension remains
unproved. No mathematical programs ran locally.

Subsequent result on the same date: the intermediate-rank gap is now closed
by the pure height argument in
`scratch/PBBS_GLOBAL_CORRIDOR_HEIGHT_AND_SHORT_SECTOR_FULL_UPPER_PRESERVATION_20260908.md`.
The open-status language below records the state when this first-ranks note
was written; its detailed q1/q2 proofs and bounded data remain in use.

## 1. Construction and precise claims

Use the explicit path in
`scratch/PBBS_ALL_R_SHORT_RUN_SECTOR_JOHNSON_PATH_20260908.md`, replacing
the r−2 bad canonical cycles by its one path and retaining every other
canonical component intact. Put n=2r+1 and g=f².

For every r>=3 this mixed path/cycle family retains:

* every rank-(r+2) target;
* every rank-(r+3) target; and
* every rank-(2r) target.

These claims concern actual consecutive unions of complementary owners.
The two first ranks and the coatom rank exhaust the proper upper ranks
when r=3 or r=4, so complete upper preservation follows in those two cases.
For larger r, the bounded audit in Section 6 checks all proper upper ranks
through r=8, but the general intermediate-rank assertion remains open.

## 2. Notation for the deleted immediate-upper colors

We work with lower rank-r owners: their adjacent intersection K corresponds
to the immediate-upper target K^c in the rank-(r+1) complement row.
Let rho be a one-position spatial rotation and use the explicit forms

\[
\begin{aligned}
 A_b&=\operatorname{evens}[0,2b]\cup\operatorname{odds}[2b+1,2r-3],\\
 B_b=fA_b&=\operatorname{odds}[1,2b-1]
       \cup\operatorname{evens}[2b+2,2r-2]\cup\{2r-1\},\\
 C_b=f^2A_b&=(A_b\setminus\{2b+1\})\cup\{2r\}.
\end{aligned}                                             \tag{2.1}
\]

Here 0<=b<=r−3, all labels are modulo n, and f³=rho on the defect-one
class. Write M=r−2. The block order is 1,...,M−1,0; block b>0 is cut
before g^(2n−b)A_b, while block zero is cut before A_0.

The last lower owner of a block b>0 is f^(t_b)A_b, where

\[
                         t_b=4n-2b-2.                      \tag{2.2}
\]

Reducing t_b modulo three and removing a common rotation, the three
possible deleted adjacent-intersection colors are

\[
\begin{array}{c|c}
\text{phase}&\text{deleted color}\\\hline
0&A_b\setminus\{2b+1\},\\
1&B_b\setminus\{2r-1\},\\
2&C_b\setminus\{0\}.
\end{array}                                               \tag{2.3}
\]

The identities follow by intersecting respectively
`A_b,C_b`, `B_b,rho A_b`, and `C_b,rho B_b` using (2.1).

## 3. Every deleted immediate-upper target is recovered

### Phase zero

The next block exists: the final nonzero block b=r−3 has t_b congruent to
two, so cannot be in this case. The new seam joins equal-time versions
of A_b and A_(b+1), whose intersection is

\[
              A_b\cap A_{b+1}=A_b\setminus\{2b+1\}.
\]

Thus the new seam recreates exactly the deleted color, with the common
spatial rotation restored.

### Phase one

Write t_b=3j+1. If b>=2, the preceding seam has f-time t_b+2=3j+3. Its
intersection is rho^(j+1) of `A_(b-1) intersect A_b`. The identity

\[
 A_{b-1}\cap A_b=A_b\setminus\{2b\},\qquad
 \rho(A_b\setminus\{2b\})=B_b\setminus\{2r-1\}
\]

shows that it recreates the deleted color.

If b=1, that preceding seam is not present because block zero is last.
Instead the color is supplied by the old q1 edge in component zero at
rho^(j+1) of `A_0 -> C_0`: indeed

\[
                  A_1\setminus\{2\}=A_0\setminus\{1\}.
\]

This occurrence survives the cut in block zero. To see this without a
phase assumption, its color is an independent (r−1)-set with one cyclic
zero gap of length two and one of length three; all other gaps have
length one. The color removed by the block-zero cut, computed below,
instead has one zero gap of length four and all others of length one.
They cannot be equal under rotation.

### Phase two: explicit untouched backup

Let

\[
 K_b=C_b\setminus\{0\}
   =\operatorname{evens}[2,2b]
      \cup\operatorname{odds}[2b+3,2r-3]\cup\{2r\}.
\]

For b>=2, the rooted state

\[
                    (b-1,M-b,1,1)                         \tag{3.1}
\]

is exactly `K_b union {2b+1}`. Applying f² in the explicit coordinate
formula gives `(1,b-1,M-b,2r-1)`, which is exactly `K_b union {1}`.
Hence these two states form a literal canonical q1 edge of color K_b.
All three coordinates of its triple are positive. Its component is
therefore outside the boundary-triple bad sector and is left intact.

For b=1 and r>=5, use instead the literal edge

\[
 K_1\cup\{2r-2\}\longrightarrow K_1\cup\{4\},             \tag{3.2}
\]

whose starting rooted state is `(r-4,1,1,4)`. Its f² successor is
`(1,r-4,1,1)`. Again every triple coordinate is positive, so this is
an untouched interior component. Both (3.1) and (3.2) are verified by
expanding `D(x,y,z)=(10)^x1(10)^(y+1)0(10)^z`; no existence of another
occurrence is inferred merely from a count.

The exceptional case r=4,b=1 has

\[
                              K_1=\{2,5,8\}.
\]

This color has spatial period three. Its component has length 27 and
f³=rho, so the q1 edge and its rotations by three and six positions
are three distinct occurrences of the same color within that component.
Opening the component once removes only one edge; another occurrence
survives. At r=3 there is no nonzero block to consider.

Common spatial rotations of these backup edges handle the omitted rho^j
in every phase-two case.

### Block zero

The deleted edge `g^(-1)A_0 -> A_0` has color

\[
                         K_0=\operatorname{odds}[1,2r-3].
\]

The all-unit soliton component supplies the literal edge

\[
                K_0\cup\{2r\}\longrightarrow K_0\cup\{2r-1\}.
\]

Its g action is a two-position rotation, which gives the displayed
successor directly. This height-one component is not in the bad sector
and remains intact.

All old q1 occurrences not crossing the chosen cuts remain literal
adjacencies. The cases above therefore prove preservation of every q1
color in the complete canonical factor, and consequently every upper
target of rank r+2 after complementation.

## 4. Every next-upper-rank target has a high component backup

Let S have rank r−2, so S^c has upper rank r+3. The explicit five-block
q2 construction in
`MATH_ATTACK_Y12_DIRECT_ALL_DEPTH_PBBS_DYCK_GATE_20260725.md`, Section 4,
and in
`MATH_THEOREM_PBBS_MAX_HEIGHT_Q1_SECTION_IS_Q2_COMPLETE_20260805.md`,
Section 3, supplies a canonical middle state A with

\[
                      g^{-1}A\cap A\cap gA=S.
\]

The height assertion needed here is part of that actual construction.
Decompose S at its five unmatched zeros into Dyck blocks D_i. Since
|S|=r−2>=1, their maximum height H is at least one. The construction
fills the unmatched zero before a tallest block and the down-step after
its rightmost maximum. Its rooted central primitive has height exactly
H+2, while the exterior primitives have height at most H. Thus A has
height at least three.

PBBS preserves rooted Dyck height. Every modified bad-sector component
has height two. Therefore the three-state witness lies in an untouched
component. Complementation proves that every upper target of rank r+3
survives, without imposing any condition on the new bad-sector seams.

This argument is specifically q2. It does not assert the unproved
height bound for the general global-maximum corridor construction.

## 5. Coatom targets also survive

The height-r single-soliton component is untouched for r>=3. Its lower
owners are all cyclic contiguous r-sets, with g shifting them one position
backwards. Intersecting r successive such owners gives any prescribed
singleton after rotation. Hence its complementary owner intervals realize
every coatom target of rank 2r, and all these witnesses survive.

## 6. Complete bounded audit and the remaining higher-rank claim

The fixed formula was checked against the complete canonical factors for
r=3,...,8, stopping at the first failure if one occurred. There was no
failure. Every mathematical execution was on h100, capped at 90 CPU
seconds, 110 wall seconds, and 2 GiB memory. No alternative ordering or
port selection was searched.

| r | n | bad owners | proper upper targets retained | targets with no outside bad-sector supplier |
|---:|---:|---:|---:|---:|
| 3 | 7 | 21 | 28 | 7 |
| 4 | 9 | 54 | 129 | 21 |
| 5 | 11 | 99 | 561 | 33 |
| 6 | 13 | 156 | 2379 | 52 |
| 7 | 15 | 225 | 9948 | 75 |
| 8 | 17 | 306 | 41225 | 102 |

All targets in the last column have rank r+2. Their complementary zero
gap pattern is `(3,2,1,...,1)`, except at r=4 where the three spacing-three
sets with pattern `(2,2,2)` also occur. This complete supplier classification
is presently a bounded observation, not a claimed all-r theorem.

Artifacts:

```text
scratch/audit_pbbs_all_r_short_sector_upper_20260908.py
scratch/pbbs_all_r_short_sector_upper_audit_20260908.json
```

The JSON contains the exact special target sets and a literal path witness
for every one of them. The remote directory is
`/home/amodo/exact-b-all-r-short-sector-upper-20260908/`.

The remaining general assertion is preservation of the intermediate
proper upper ranks r+4 through 2r−1. One prospective route is to prove
that their global-maximum-corridor witnesses can be chosen in components
of height at least three. The existing corridor theorem gives support,
but its required height property has not been established here.
