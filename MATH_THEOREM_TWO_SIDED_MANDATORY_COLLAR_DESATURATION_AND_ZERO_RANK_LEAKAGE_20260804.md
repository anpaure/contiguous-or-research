# Two-sided mandatory-collar desaturation and zero rank leakage

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional fixed-carrier theorem.  It removes the
`R_A` term from the lower-deck waste identity on any sufficiently long
resident simple Johnson owner path, without changing the owner path or its
Euler connectivity.  It does not control duplicate lower values.

## 0. Outcome

Let

\[
 T_0,T_1,\ldots,T_{W-1}\in { [k]\choose r},
 \qquad
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\},              \tag{0.1}
\]

be a simple rank-`r` Johnson path.  Assume every internal positive
coordinate run has length at least `d+1` (boundary-clipped runs are
allowed), the maximal envelopes below realize the owners, `d<r`, and
`W>2d`.  Then it has a nonempty
depth-`d` antecedent

\[
                     T_i=\bigcup_{p=i}^{i+d}A_p       \tag{0.2}
\]

with the exact two-sided boundary collars

\[
 A_p=\{\alpha_p\}\quad(0\le p<d),
 \qquad
 A_p=\{\beta_{p-d-1}\}\quad(W\le p<W+d).           \tag{0.3}
\]

Every physical interval of length at most `d` then has rank strictly less
than `r`.  Hence

\[
                              \boxed{R_A=0}.          \tag{0.4}
\]

The two boundary chains are literal and forced:

\[
 \bigcup_{p=0}^{q-1}A_p
      =\{\alpha_0,\ldots,\alpha_{q-1}\},             \tag{0.5}
\]

\[
 \bigcup_{p=W+d-q}^{W+d-1}A_p
      =\{\beta_{W-q-1},\ldots,\beta_{W-2}\}
      \qquad(1\le q\le d).                           \tag{0.6}
\]

Both have rank `q`.  Thus the linear opening pays the mandatory
one-sided collars exactly rather than treating them as an unpriced
boundary sidecar.

If the owner path is obtained by opening one connected owner-coloured
Euler cycle, (0.3) leaves the owner order unchanged.  The result is the
same single rooted Euler trail, with no added reset arc and no connectivity
charge.

Finally, the construction commutes with any already validated finite pin
halo whose affected owner windows are disjoint from the first and last `d`
owner windows.  In particular, after choosing the opening away from an
authenticated one-phase `Ibc/Ica` halo, the forced rays and (0.3) coexist.

Consequently the pinned waste target on this face reduces exactly from

\[
                  D_A^\Pi+Q_A^\Pi+R_A^\Pi
                         \le \sigma+C
\]

to

\[
                  \boxed{D_A\le\sigma+C},            \tag{0.7}
\]

because exact distinct lower pins merely reclassify the unpinned duplicate
term: `D_A^Pi+Q_A^Pi=D_A`, while `R_A^Pi=R_A=0`.

## 1. Linear maximal envelopes

Use source positions `0,1,...,W+d-1` and owner windows

\[
                              I_i=[i,i+d].             \tag{1.1}
\]

Put

\[
                 E_p=\bigcap_{i:\,p\in I_i}T_i.      \tag{1.2}
\]

The stated maximal-envelope hypothesis gives `E_p` nonempty and

\[
                              T_i=\bigcup_{p=i}^{i+d}E_p. \tag{1.3}
\]

Define `A` from `E` by (0.3), leaving

\[
                         A_p=E_p\qquad(d\le p<W).     \tag{1.4}
\]

The only issue is whether the two collar replacements can erase an owner
coordinate.  The next two lemmas settle the two ends separately.

## 2. The left collar preserves every owner

### Lemma 2.1

Replacing `E_p` by `\{alpha_p\}` for `0<=p<d` preserves (1.3).

### Proof

Only owners `T_i` with `0<=i<d` meet the modified block.  Fix
`x in T_i`.

Consider the maximal positive run of `x` containing this occurrence in
`T_i`.  If that run does not meet the left boundary, it begins at an owner
`a` with `1<=a<=i`.  Its maximal-envelope support begins at `a+d`.
If the run ends internally at owner `b`, residence gives `a+d<=b`; if it
reaches the right boundary, its envelope support continues to the end of
the source word.  Hence

\[
                     h=\max(i,a+d)                   \tag{2.1a}
\]

lies in both `[i,i+d]` and that envelope support.  Since `a>=1`, we have
`h>=d+1`; moreover `h<=i+d<2d<W`, so it is unmodified and supplies `x`.

Suppose instead that the run containing `T_i` meets the left boundary.  If
it reaches `T_d`, then it contains every owner `T_0,...,T_d`.  Therefore

\[
                            x\in E_d,                 \tag{2.1}
\]

and the unmodified source position `d` supplies it to every such owner
window containing `T_i`.

Otherwise let `b<d` be the transition at which this boundary-positive run
ends.  Then `x=alpha_b`; since `i<=b<=i+d`, the retained mandatory letter
`A_b={alpha_b}` lies in the source window of `T_i` and supplies `x`.  In
either case `x` remains in the union of the source window of `T_i`.  No
extraneous coordinate can be introduced, because `alpha_p in E_p`.  Hence
every affected owner is preserved.
\(\square\)

The last assertion can also be read directly from residence: for `p<d`,
the coordinate departing at transition `p` was already present in every
owner whose window contains source position `p`.

## 3. The right collar preserves every owner

### Lemma 3.1

Replacing `E_p` by `\{beta_(p-d-1)\}` for `W<=p<W+d`
preserves (1.3).

### Proof

Only owners `T_i` with `W-d<=i<W` meet the modified block.  Fix
`x in T_i`.

Consider the maximal positive run `[a,b]` of `x` containing this
occurrence in `T_i`.  If the run ends before the right boundary, residence
gives `a+d<=b`, and its maximal-envelope support is `[a+d,b]`.  Therefore

\[
                     h=\min(b,i+d)                   \tag{3.1a}
\]

lies in that support and in `[i,i+d]`.  If `b<=i+d`, then `h=b<W`; if
`b>i+d`, then `h=i+d<b<W`, again `h<W`.
Thus this supplier is outside the modified suffix block.

Suppose instead that the run containing `T_i` reaches the right boundary.
If it begins no later than `T_(W-d-1)`, then it contains every owner from
`T_(W-d-1)` to `T_(W-1)`.  Thus

\[
                            x\in E_{W-1},             \tag{3.1}
\]

and the unmodified source position `W-1` supplies it.

Otherwise this right-boundary run begins at an owner `a>W-d-1`, so its
entry transition `u=a-1` satisfies

\[
                         W-d-1\le u\le W-2.           \tag{3.2}
\]

Then `x=beta_u`, and source position `p=u+d+1=a+d` lies in
`[W,W+d-1]`.  Since `a<=i<=W-1` and `a>W-d-1`, we also have
`i<=a+d<=i+d`; hence this position lies in the source window of `T_i`,
and its retained mandatory letter supplies `x`.  Again no extraneous
coordinate is introduced because `beta_u in E_(u+d+1)`.  Hence every
affected owner is preserved.  \(\square\)

Because `W>2d`, no owner window meets both collar blocks.  Lemmas 2.1 and
3.1 therefore apply simultaneously and prove (0.2).

## 4. Exact localization and removal of rank-`r` leakage

For a `q`-cell

\[
                         C_{j,q}=[j,j+q-1],           \tag{4.1}
\]

the owner windows containing it have indices

\[
 \max(0,j+q-1-d)\le i\le\min(j,W-1).                \tag{4.2}
\]

When `1<=q<=d`, this interval of owner indices has size one if and only if

\[
                         j=0
 \quad\hbox{or}\quad
                         j+q-1=W+d-1.                \tag{4.3}
\]

Every other short cell is contained in two consecutive owner windows.
Those two owners are distinct rank-`r` Johnson neighbours, so their
intersection has rank `r-1`.  The cell value is contained in that
intersection and is therefore strict-lower.

The two exceptional cells in (4.3) are respectively the length-`q`
prefix and suffix.  Equations (0.3) give their values (0.5)--(0.6).
Consecutive departure labels are distinct over a block of at most `d`
transitions, as are consecutive arrival labels: a repeated label would
create a positive run shorter than `d+1`.  Their ranks are therefore
exactly `q<r`.  This proves (0.4).

The same argument gives a useful carrier-independent localization:

\[
 R_A=
 |\{q:\operatorname{OR}(A_0,\ldots,A_{q-1})=T_0\}|
 +|\{q:\operatorname{OR}(A_{W+d-q},\ldots,A_{W+d-1})=T_{W-1}\}|.
                                                               \tag{4.4}
\]

Thus rank leakage was never an interior rounding obstruction; it is purely
a two-sided opening-collar choice.

## 5. Coexistence with a protected pin halo

Let `Pi` be an exact pin bank already extended by the maximal-envelope halo
theorem, and let `H(Pi)` be its complete affected-owner source halo.  Assume
no owner window meeting `H(Pi)` is among

\[
                  T_0,\ldots,T_{d-1},
                  T_{W-d},\ldots,T_{W-1}.            \tag{5.1}
\]

Start with the globally extended pinned antecedent.  Outside `H(Pi)` it
equals the unpinned maximal envelope.  Apply the two replacements (0.3).
The proofs of Lemmas 2.1 and 3.1 take place entirely in the owner windows
listed in (5.1), so no pin cell or pin-affected owner changes.  The forced
facts remain exact and every owner remains realized.

If the carrier is cyclic and the pin halo has `O(d)` consecutive extent,
an opening satisfying (5.1) exists whenever its complement contains a
gap of at least `2d+1`.  This last gap condition is an explicit planting
hypothesis; the theorem does not infer it merely from the size of the pin
set.

## 6. Euler and waste accounting

The construction changes only the antecedent letters, not the owner row.
Hence a Hamilton owner cycle opened at one edge remains one Hamilton owner
path.  In the state-circulation language, deleting the opening edge turns
one connected Euler circuit into one rooted Euler trail; the collar
replacement introduces neither another component nor a reset arc.

For exact distinct strict-lower pins, the fixed-word reclassification
identity gives

\[
                     D_A^\Pi+Q_A^\Pi=D_A,
 \qquad             R_A^\Pi=R_A.                    \tag{6.1}
\]

Together with (0.4), the pinned waste identity becomes

\[
                             M_A^\Pi=D_A-\sigma.      \tag{6.2}
\]

Therefore the complete remaining scalar gate on this face is precisely
(0.7).  The theorem has paid the mandatory two-sided collar and Euler
connectivity exactly.  It does **not** bound `D_A`: named lower-value
collisions, integral one-copy owner/target coupling, and protected global
planting remain open.

## 7. Dependencies and scope exclusions

Dependencies:

- `MATH_THEOREM_PINNED_MAXIMAL_ENVELOPE_GLOBAL_EXTENSION_AND_WASTE_IDENTITY_20260804.md`;
- `MATH_THEOREM_INTEGRAL_ROTOR_MANDATORY_COLLAR_AND_MINIMUM_RUN_TRANSVERSAL_20260803.md`;
- `MATH_COROLLARY_LITERAL_LOWER_DECK_WASTE_AS_L1_DISCREPANCY_20260804.md`.

This theorem does not prove:

- `D_A<=sigma+O(1)`;
- an integral endpoint-triangular chain partition;
- a one-copy coloured rotor or Hamilton owner carrier;
- upper completeness, protected reservoir planting, or regeneration; or
- that an arbitrary prescribed opening is far from the pin halo.

It proves that none of those remaining rows needs to pay an additional
rank-`r` short-cell leakage or Euler-reset charge.
