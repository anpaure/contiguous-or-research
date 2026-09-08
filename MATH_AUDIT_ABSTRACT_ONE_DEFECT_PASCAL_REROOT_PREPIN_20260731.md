# Audit of the one-defect Pascal lift, endpoint reroot, and prepin principles

Date: 2026-07-31  
Status: the set-layer lift and cut-spectrum statements are valid after the
qualifications below; the strongest interpretation of “freeze a prepin” is
false for a multi-cell pin.

## 1. One-defect Pascal lift

Let `X` have size `2r-1`, let `z` be a new coordinate, and define the
inclusive-OR derivative of a word `w=(w_0,...,w_{m-1})` by

\[
D^j(w)_i=\bigvee_{t=0}^{j}w_{i+t},qquad 0\le i<m-j.
\]

Put

\[
N=\binom{2r-1}{r}=\binom{2r-1}{r-1}.
\]

Assume:

1. `D^h(w)` has length `N` and is a permutation of all rank-`r` subsets of
   `X`;
2. `D^(h-1)(w)` consequently has length `N+1`; and
3. for one index `e` in `{0,...,N}`, deleting its entry leaves a permutation
   of all rank-`r-1` subsets of `X`.

Write `Q=D^h(w)` and `P=D^(h-1)(w)`.  Then

\[
T=\operatorname{rev}(z\vee P[0:e])\;\Vert\;Q\;\Vert\;
  \operatorname{rev}(z\vee P[e+1:N+1])                 \tag{1.1}
\]

is a permutation of the complete rank-`r` layer on `X union {z}`.

### Proof

The three block sizes are

\[
e,quad N,quad N-e,
\]

so (1.1) has length `2N`.  The middle block is exactly the rank-`r` sets not
containing `z`.  The two outer blocks together are exactly `z` joined to all
rank-`r-1` sets of `X`, hence exactly the rank-`r` sets containing `z`.
These two classes are disjoint, and

\[
2N=\binom{2r-1}{r}+\binom{2r-1}{r-1}=\binom{2r}{r}.
\]

Thus every rank-`r` set occurs once.  Reversal is irrelevant to this
set-layer conclusion.  □

The phrase “one exceptional entry” must mean deletion of one indexed
occurrence, not merely deletion of one distinct value.  It is harmless if
the exceptional occurrence itself has rank `r-1`, provided the remaining
indexed sequence is the asserted permutation.

### Chain qualification

The hypotheses above do **not** imply that `T` is a Johnson path.  Inside a
marked outer block, consecutive colours are automatically

\[
(z\vee P_i)\vee(z\vee P_{i-1})=z\vee Q_{i-1},
\]

whenever neither `P` entry is the deleted exception.  The two exterior-to-
middle seams are also Johnson when present, because `P_0 subset Q_0` and
`P_N subset Q_{N-1}`.

But inside `Q`, adjacency has union

\[
Q_i\vee Q_{i+1}=D^{h+1}(w)_i,
\]

whose rank is not controlled by the stated assumptions.  A Johnson-chain
claim therefore needs the additional condition

\[
|D^{h+1}(w)_i|=r+1\quad(0\le i<N-1).
\]

Nor do the hypotheses imply q1 completeness: for an interior exception,
the marked internal colours `z|Q_(e-1)` and `z|Q_e` are precisely the two
natural colours skipped by splitting `P`.  Further filter or seam conditions
must supply them.

## 2. Endpoint reroot and exact cut spectra

Let a linear target word be split into three nonempty consecutive blocks

\[
T=A\Vert B\Vert C,
\]

and let

\[
T'=\operatorname{rev}(A)\Vert B\Vert\operatorname{rev}(C). \tag{2.1}
\]

As unordered adjacent pairs, every internal edge of each block is preserved.
Exactly the two cut pairs are replaced:

\[
(A_{-1},B_0)\mapsto(A_0,B_0),
\qquad
(B_{-1},C_0)\mapsto(B_{-1},C_{-1}).                    \tag{2.2}
\]

Thus at most two q1 edge occurrences change.  “Exactly two q1 colours” is
too strong: an old or new union may have rank other than `r+1`, the old and
new colours may coincide, or a colour may have another occurrence elsewhere.
Also, (2.2) concerns undirected OR colours; every directed internal edge in
a reversed block changes orientation.

For a cut after position `c`, define its linear cut spectrum

\[
\Sigma_T(c)=
\left\{
 \bigvee T[i..j]:0\le i\le c<j<|T|
\right\}.                                                \tag{2.3}
\]

Equivalently it is the pairwise OR of the suffix-OR ray of `T[0..c]` and the
prefix-OR ray of `T[c+1..]`.  Let `I` be the union of all interval-OR spectra
internal to `A`, `B`, and `C`.  Reversal preserves each internal spectrum, so

\[
\operatorname{Cov}(T)=I\cup\Sigma_T(c_1)\cup\Sigma_T(c_2),
\]

\[
\operatorname{Cov}(T')=I\cup\Sigma_{T'}(c'_1)
                         \cup\Sigma_{T'}(c'_2).           \tag{2.4}
\]

Intervals spanning all three blocks are included in both relevant cut
spectra; they must not be omitted by using only spectra local to two adjacent
blocks.

Consequently the following ray test is exact.  Put

\[
\Sigma_{old}=\Sigma_T(c_1)\cup\Sigma_T(c_2),\qquad
\Sigma_{new}=\Sigma_{T'}(c'_1)\cup\Sigma_{T'}(c'_2).
\]

Then

\[
\Sigma_{old}\subseteq I\cup\Sigma_{new}                 \tag{2.5}
\]

is exactly the no-loss condition.  If the old word covers every desired
upper mask except a set `H`, then (2.5) together with

\[
H\subseteq I\cup\Sigma_{new}                             \tag{2.6}
\]

implies upper completeness of `T'`.  The gained masks are exactly

\[
(I\cup\Sigma_{new})\setminus(I\cup\Sigma_{old}).
\]

### Linear and physical-chain qualifications

There is no cyclic endpoint seam in (2.3).  The OR of the two global
endpoints is not a witness unless the construction is explicitly cyclic.
Treating it as a third cut can create a false upper witness.

Likewise, target-order upper completeness does not automatically give a
physical-word witness.  If middle target `i` occupies `[s_i,d_i]`, a
consecutive block of target rows has a contiguous physical union only under
the chain condition

\[
s_{i+1}\le d_i+1.
\]

Without it, an abstract interval witness may cross a physical gap.  Endpoint
rerooting also changes occurrence positions and therefore need not preserve
P/Q capacity or any directed chronology invariant.

## 3. What can be frozen before common-cap matching

Let `E_p` be a maximal envelope for protected middle rows.  Fix a finite
family of preassigned pins `(S_alpha,C_alpha)` and define their joint cap

\[
\bar E_p=E_p\cap
 \bigcap_{\alpha:p\in C_\alpha}S_\alpha.                 \tag{3.1}
\]

Assume (3.1) is nonempty and exactly replays every middle row and every
prepin.  The prepin assignments and their cell identities may then be fixed
before the residual matching.  For a residual injection `M`, put

\[
A_p(M)=\bar E_p\cap
 \bigcap_{S:p\in M(S)}S.                                 \tag{3.2}
\]

There is a simultaneous extension exactly when (3.2) is nonempty and
exactly replays:

1. every middle row;
2. every frozen prepin row; and
3. every residual assigned lower row.

The proof is the same maximal-cap monotonicity used in Section 1: every
realization lies pointwise below (3.2), and (3.2) itself is the maximal
candidate.  In the residual graph one must remove the reserved cell
identities and recompute/filter incidences against `bar(E)`, including the
bits needed to preserve every frozen prepin row.

### Counterexample to forgetting a multi-cell prepin

It is not enough to verify a prepin once and then drop its equality from
later replay.  Take three physical positions with

\[
E_1=E_2=\{a,b\},\qquad E_3=\{b\}.
\]

The middle row on `[1,3]` has target `{a,b}`.  Freeze a prepin `{a,b}` on
`[1,2]`; it is initially exact.  Now assign residual target `{a}` to
`[1,2]`.  The final maximal cap is

\[
A_1=A_2=\{a\},\qquad A_3=\{b\}.
\]

All letters are nonempty, the middle row remains exact, and the residual pin
is exact, but the frozen prepin has fallen from `{a,b}` to `{a}`.  Therefore
a general multi-cell prepin remains a protected row throughout matching.

For a one-cell singleton prepin, the equality *is* automatic: every nonempty
future cap of that position is the same singleton.  This is why reserving a
literal `0x8000` singleton can be fully frozen after all residual incidences
that make its position empty are removed.

## 4. Verdict

1. The one-defect Pascal formula is correct as a complete-layer permutation,
   with derivative lengths `N` and `N+1` and indexed deletion made explicit.
2. The endpoint reroot statement is correct for two disjoint linear endpoint
   blocks when phrased as “at most two undirected adjacency occurrences” and
   when the cut spectra include intervals spanning both cuts.
3. A finite prepin cap can be frozen as part of the base envelope and fixed
   assignment, but its row equality cannot generally be forgotten.  It must
   remain protected unless an immunity condition, such as a one-cell
   singleton, makes future replay automatic.

