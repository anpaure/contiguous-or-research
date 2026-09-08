# Audit of the projection-coded odd-APH handoff

**Date:** 2026-08-07  
**Audited file:**
`MATH_THEOREM_ODD_APH_PROJECTION_CODED_ATOM_ORDER_HANDOFF_20260807.md`  
**Audited SHA-256:**
`6d2d8df5bfd139d05fa2412a69e070d32039cf36a9490c929ac155214dae696d`  
**Method:** literal full-state comparison; no computation or search  
**Verdict:** **FAIL / DO NOT CITE AS APH.**  The persistent `Q_q` repair
corrects the earlier erased-atom defect, but the displayed `r=0` code-writing
route and the displayed `r=0` delimiter-crossing route contain the same full
strict state.  The proposed delimiter head tag is trivial in this row and
does not separate the two occurrences.

## 1. Exact repeated full state

Take the clean `BBBB` branch.  Its first `BB` is changed to the fixed cart
`H|H`, and its second `BB` is the code pair.  Thus the local physical order
is

\[
                         H|H|BB.                    \tag{1.1}
\]

Choose any admissible raw source collar of order class `r=0`; for example
`A|B`.  The atom record is `Q_0` in the `BBBB` branch.  Both `Q_0` and the
raw collar remain literal throughout code writing and cart prepositioning.

For `r=0`, equations (2.6)--(2.7) prescribe the loop-free code route

\[
 BB=2020\longrightarrow2011\longrightarrow1111
       \longrightarrow0211\longrightarrow0121=C_0. \tag{1.2}
\]

At its middle strict state the complete displayed work factor is

\[
                         H|H|11|11.                 \tag{1.3}
\]

At the endpoint, `C_0=P_0|D_0=01|21`.  In the `BBBB` branch the moving
pilot is already on the right-going cart tail and the stationary delimiter
is the next crossed block.  Equation (3.2) prescribes

\[
 P_0|D_0=0121\longrightarrow1021\longrightarrow1111
       \longrightarrow2011\longrightarrow2101=D_0|P_0. \tag{1.4}
\]

The two head blocks are unchanged during this tail-clean phase.  Hence the
strict state `1111` in (1.4) again gives exactly (1.3), at the same four
physical blocks.

All exterior coordinates agree at the two visits:

* `Q_0` is unchanged;
* the raw source collar has not yet been replaced by `Phi(K)`;
* no task ticket has been written;
* the `BBBB` branch has no private gap;
* the cart and code supports are precisely the four blocks in (1.1).

The additional delimiter-crossing tag does not help.  Table (2.3) sets

\[
                            S_0=H,
\]

so the instruction `H -> S_0` makes no graph move and leaves both cart
heads equal to those in the code-writing occurrence.  Therefore (1.3) is
one graph vertex visited at two different macro phases.

In fact the same two routes also share `2011`, so the full state
`H|H|20|11` is repeated as well.  Either intersection alone is fatal.

This disproves the full-state conclusion of Lemma 3.1, the visit-separation
conclusion of Lemma 4.1, Lemma 6.1's record schedule as an occurrence
decoder, and Theorem 7.1.

## 2. The delimiter projections have a second unresolved alias

Even away from (1.3), Lemma 2.1 overstates what one delimiter projection
decodes.  The three ordinary and selected-`M` delimiter lists are

\[
 (D_0,D_1,D_2)=(21,12,10),\qquad
 (\bar D_0,\bar D_1,\bar D_2)=(12,21,01).             \tag{2.1}
\]

Each list separately is injective, but their union is not:

\[
                       \bar D_0=D_1=12,
        \qquad        \bar D_1=D_0=21.               \tag{2.2}
\]

This matters in exactly the phase in which the pilot projection is not
literal.  The displayed tail-clean paths have the literal intersections

\[
\begin{aligned}
 P_0|M &: 0111\to1011\to1101,\\
 P_1|B &: 1020\to1011\to1002\to0102\to0111
          \to0201\to1101\to2001\to2010,             \tag{2.3}
\end{aligned}
\]

and

\[
\begin{aligned}
 P_1|M &:1011\to1002\to0102\to0111\to0201
          \to1101\to1110,\\
 P_0|B &:0120\to1020\to1110\to2010\to2001.         \tag{2.4}
\end{aligned}
\]

Thus a selected-`M`, order-0 occurrence and a raw-`B`, order-1 occurrence
can have both the same active projection and the same stationary delimiter
projection; the symmetric order-1/order-0 ambiguity occurs at `1110`.
The semantic assertion "this is a barred delimiter" is not a literal bit.
It is precisely the `B/M` branch that the delimiter was meant to encode.

Equations (2.2)--(2.4) do not by themselves assert that every surrounding
collar schedule realizes a global collision.  They do prove that the stated
local decoder is circular: `bar D_r` alone does not recover both `r` and
the selected-`M` branch.  A repaired theorem must either give a disjoint
union code, retain a separate literal phase bit, or prove and cite a global
collar invariant which separates these aliases at every strict state.

## 3. Audit of the six requested rows

### 3.1 Translated code-path intersections: fail

Every displayed arrow in (1.2) is a legal unit transfer, and the route is
simple in its four-coordinate projection.  That does not make its
translations disjoint from later local routes.  Equations (1.2)--(1.4)
give an exact translated full-state intersection.  Loop erasure inside the
code route cannot delete it: `1111` occurs only once in (1.2).

### 3.2 Both-code-active delimiter crossing: fail in row zero

For rows one and two, the three distinct values

\[
                         S_1=M,\qquad S_2=B
\]

do separate their shared `1111` delimiter projection from an untagged
`H|H` code-writing state.  In row zero, `S_0=H` supplies no phase change,
and (1.3) is repeated.  The three values do encode `r` *conditional on
already knowing that the delimiter-crossing phase is active*; they do not
establish that phase globally.

### 3.3 Extreme first-out reinterpretation: locally coherent, not a repair

The endpoint change

\[
 (P_0,D_0)=(01,21)\to(10,21)\to(10,12)=(P_1,D_1)
\]

is a valid two-edge fixed-mass path.  At a macro checkpoint, an extreme
literal collar plus the first-out record can reinterpret effective row one
as logical order zero.  The extra `H -> M` tag also separates the three
explicit intersections of the `P_1|M` path with the base `P_0` paths when
`D_1` has been changed to `\bar D_1=D_0`.

This does not address (1.3), which occurs earlier during cart
prepositioning, before the first-out reinterpretation is installed.
Moreover the proof must specify the ordering of the delimiter and head-tag
writes so that no untagged join is exposed.  The current text gives a
plausible local record, not an independent proof of global occurrence
disjointness.

### 3.4 `Phi(K)` visit separation: the literal endpoint table passes

For every listed nonextreme raw collar, `Phi(K) != K`.  Within a fixed
mass fibre the order class is retained by the literal `P_r,D_r` pair while
the collar path is active; across fibres, total collar mass differs.  The
seven displayed `Phi` paths are simple.  In the zero-task mass-four rows,

\[
 \Phi(A|C)=R_0,\quad \Phi(B|B)=R_1,\quad
 \Phi(C|A)=R_2,
\]

and each `R_r` is nonraw, so it differs from the setup collar.

Consequently this table is a valid setup/first-out phase record at the
macro level.  It cannot prove Lemma 4.1 after the exact earlier repetition
(1.3), and it does not supply the missing union-code bit in Section 2.

### 3.5 Eight-coordinate regeneration: local connectivity only

The endpoint mass identity in (5.3) is inherited correctly, and the
capacity-two fixed-mass graph on eight coordinates is connected whenever
its total mass is nonextreme.  The odd pilot and a head put these endpoints
strictly between total masses zero and sixteen.  Hence a simple local path
between the stated endpoints exists.

What is not proved is that an arbitrary such simple path avoids all strict
states of the immediately preceding return crossing, the next outward
crossing, or a translated regeneration path.  The returned outside head,
task ticket, `Q_q`, and `D_r` identify the intended endpoints *after the
regeneration phase is known*; they do not themselves prove that this phase
is recoverable from a strict full state.  A proof-safe completion needs an
explicit path bank plus cross-phase disjointness, or an additional literal
phase tag held through the whole eight-coordinate interior.

### 3.6 Reverse private-gap teardown: conditionally separated

Retaining `Q_q` until the exact raw motif returns repairs the previous
information-erasure error.  The forward setup holds a raw collar
`K in {A,B,C}^2`, whereas reverse work teardown holds

\[
 R_0=H|H,\qquad R_1=H|M,\qquad R_2=M|H.              \tag{3.1}
\]

No `R_r` is a raw collar, so this literal collar separates a reverse
private-gap state from its forward counterpart.  At the late register
handoff, the restored raw motif retains `q` and `R_r` retains `r`; changing
one record only while the other is literal is valid copy-before-erase.

Thus the *data-retention* part of Section 6 is sound conditional on the
clean setup decoder.  It does not repair the earlier repeated graph vertex,
and the claim that the entire reverse concatenation is occurrence-simple
still inherits the unresolved cross-path audit of the chosen work paths.

## 4. Proof-safe frontier and minimum repair target

The following parts survive this audit:

1. the arithmetic mass-four code table and injectivity of each of the
   `P`, `D`, and `bar D` lists separately;
2. legality and individual simplicity of the displayed four-coordinate
   tail-clean paths;
3. the nonextreme/extreme first-visit macro records;
4. local existence of the eight-coordinate regeneration paths; and
5. the copy-before-erase order of the final `(q,r)` handoff.

They do not compose into APH because the complete walk already repeats
(1.3).  The minimum next theorem must jointly select:

* a code-writing path bank and delimiter-crossing path bank with no
  translated intersection under the actual fixed cart;
* a phase tag nontrivial also in order row zero; and
* a literal union code separating `D_r` from `bar D_s`, or a proved global
  invariant replacing it.

The eight-coordinate regeneration bank then still needs its own
cross-phase audit.  Until those rows are supplied, the authoritative odd
frontier remains `ACT4`; the projection-coded candidate is not an odd APH
theorem.

## 5. The first collision has a literal path-bank repair

The repeated `1111` state is not forced by the mass-four layer.  The
following hand-selected routes are legal, simple, avoid `H|H=0202`, and
meet their corresponding delimiter-crossing row only at the intended code
endpoint:

\[
\begin{array}{c|l}
 &\multicolumn{1}{c}{r=0,\ C_0=0121}\\ \hline
BB&2020\to1120\to0220\to0211\to0121,\\
AC&0022\to0112\to0121,\\
CA&2200\to2110\to1210\to1120\to0220\to0211\to0121;
\end{array}                                             \tag{5.1}
\]

\[
\begin{array}{c|l}
 &\multicolumn{1}{c}{r=1,\ C_1=1012}\\ \hline
BB&2020\to1120\to0220\to0211\to0121\to0112\to1012,\\
AC&0022\to0112\to1012,\\
CA&2200\to2110\to2020\to1120\to0220\to0211
      \to0121\to0112\to1012;
\end{array}                                             \tag{5.2}
\]

\[
\begin{array}{c|l}
 &\multicolumn{1}{c}{r=2,\ C_2=2110}\\ \hline
BB&2020\to2110,\\
AC&0022\to0112\to0121\to0211\to0220\to1120
      \to2020\to2110,\\
CA&2200\to2110.
\end{array}                                             \tag{5.3}
\]

For comparison, the forbidden post-initial sets of the three displayed
delimiter rows (including their final macro vertex) are respectively

\[
\begin{aligned}
F_0&=\{1021,1111,2011,2101\},\\
F_1&=\{1102,1111,1201,1210\},\\
F_2&=\{2101,2011,2002,1102,1111,1021\}.
\end{aligned}                                           \tag{5.4}
\]

Direct inspection of (5.1)--(5.3) gives no occurrence of `F_r` in row
`r`.  Their final vertex is the intended initial delimiter-crossing vertex
`C_r`; that join is not a repetition.  Therefore replacing (2.6)--(2.7)
by this source-and-order-indexed path bank repairs the exact collision of
Section 1, including its reverse-teardown copy.

This is only a local correction.  It does not repair the union-code alias
(2.2)--(2.4), nor does it supply cross-phase disjointness for the unspecified
eight-coordinate regeneration paths.  A revised APH theorem would have to
incorporate (5.1)--(5.3) and close those two remaining rows jointly.
