# A common-endpoint fiber contains a linear-distance central deck code

**Status (2026-08-21).**  The theorem below is proved.  It strengthens the
common-transformation bundle: after imposing central chordlessness, its
branch entropy cannot be concentrated in retained decks differing at only
`o(n)` targets.  After deleting the branch-independent final checkpoint, a
fixed-endpoint microblock contains an exponentially large code whose
rank-`m` decks have linear replacement distance.  This supplies real local
mobility, but does not by itself orient that mobility toward a given global
residual or Hall cycle.

## 1. An induced-path ball bound

Let `G` be a graph on `V` vertices with maximum degree `Delta>=1`, and let
`P` be an induced path on `ell>=2` vertices.  For another induced `ell`-vertex
path `P'`, define its replacement distance from `P` by

\[
 d(P,P')=|V(P')\setminus V(P)|
        =|V(P)\setminus V(P')|.                       \tag{1.1}
\]

### Lemma 1.1 (induced-path replacement ball)

The number of induced `ell`-vertex path decks `P'` satisfying
`d(P,P')<=r` is at most

\[
 (r+1)V(8\ell^2\Delta)^{r+1}.                         \tag{1.2}
\]

The same bound holds if paths are regarded as unordered vertex decks.

#### Proof

It is enough to count ordered paths, which only overcounts unordered decks.
Fix `j=d(P,P')<=r`, and write `X=V(P) cap V(P')`.  In the order of `P'`,
the maximal consecutive runs consisting of vertices of `X` are separated
by new vertices.  There are at most `j+1` such runs.

Every run is an oriented interval of `P`: two consecutive old vertices in
`P'` are adjacent in `G`, and the induced graph on `V(P)` has only the
edges of `P`.  An ordered list of at most `j+1` oriented intervals is
therefore overcounted by `(2ell^2)^(j+1)`.  The lengths and locations of the
new-vertex gaps are overcounted by `4^(j+1)`.

After those choices, if the first path vertex is new it has at most `V`
choices; every later new vertex has at most `Delta` choices from its
predecessor.  Ignoring the additional requirement that it connect to the
next old interval gives at most `V Delta^j` choices.  Hence the number at
distance exactly `j` is at most

\[
 V(8\ell^2\Delta)^{j+1}.
\]

Summation over `0<=j<=r` gives (1.2).  \(\square\)

## 2. Application to the tail-MTF common-endpoint bundle

Work in the actual palette regime

\[
 n=2m+1,\qquad W={n\choose m},\qquad
 H=\lceil\sqrt{n\log n}\rceil,
\]

\[
 K=\{m-H,\ldots,m+1+H\},\qquad
 f=m+H+2,\qquad d=n-f+1=m-H.
\]

Let `ell=ceil(Cn)` for fixed `C>1`, put `a=ell-1`, and use the
strengthened common-transformation family `G_ell` whose traces are
`K`-simple and whose rank-`m` traces are chordless.  Fix one seed state and
delete the final,
branch-independent checkpoint target.  The remaining ordered trace has
`a` vertices.  Because `a>=m+1`, trace reconstruction determines the first
`a` branch letters from it; there are at most `d` choices for the deleted
final branch letter.  Chordlessness makes the unordered retained deck
determine its order up to reversal.  Consequently the family realizes at
least

\[
 { |\mathcal G_\ell|\over2d}
 \ge \exp\bigl((C-1)n\log n-O(n)\bigr)                \tag{2.1}
\]

distinct unordered retained central decks.

### Theorem 2.1 (linear-distance deck code)

For every fixed `C>1` there is a constant `c_C>0` and a subfamily
`C_ell subseteq G_ell` such that

1. all its words have the same complete endpoint transformation;
2. every word is legal, band-simple, and centrally chordless;
3. any two distinct retained rank-`m` decks in the subfamily have replacement
   distance at least `c_C n`; and
4. the subfamily still has

   \[
   \log|\mathcal C_\ell|=\Omega_C(n\log n).           \tag{2.2}
   \]

The same conclusion holds for `ell=Theta(n log n)`, with distance
`Omega(ell)` and logarithmic family size `Omega(n(log n)^2)`.

#### Proof

Apply Lemma 1.1 with path length `a` to `J(n,m)`, where

\[
 V=W=\exp(O(n)),
 \qquad
 \Delta=m(m+1)=O(n^2).                               \tag{2.3}
\]

For `a=Theta(n)` and `r=alpha n`, (1.2) gives

\[
 \log B_r
 \le O(n)+(4\alpha+o(1))n\log n,                  \tag{2.4}
\]

because `log(a^2 Delta)=(4+o(1))log n`.  Choose, for
example, any fixed `alpha<(C-1)/8`.  Greedily select one deck and discard
its radius-`r` ball.  For every selected deck, choose one arbitrary word of
`G_ell` realizing it, and let `C_ell` be this representative-word family.
There is exactly one representative per selected deck, so
(2.1)--(2.4) leave

\[
 \log|\mathcal C_\ell|
 \ge (C-1-4\alpha-o(1))n\log n-O(n)
 =\Omega_C(n\log n).                                 \tag{2.5}
\]

The selected decks have pairwise distance greater than `r`, proving the
first assertion with `c_C=alpha`.

If `ell=L_n n log n` with `L_n` bounded above and below by positive
constants, then `a=(L_n+o(1))n log n`, the common-fiber entropy is

\[
 (L_n+o(1))n(\log n)^2,
\]

and, for `r=alpha a`, the ball logarithm is at most

\[
 (4\alpha L_n+o(1))n(\log n)^2.
\]

Any fixed `alpha<1/8` therefore leaves an exponentially large greedy code,
uniformly over this range of `L_n`.  \(\square\)

## 3. Scope

The theorem proves `Theta(n)` (or `Theta(ell)`) potential retained-target
mobility per checkpoint microblock.  Across `Theta(W/ell)` microblocks this is the
linear aggregate mobility scale required to repair a `Theta(W)` defect.
It removes the earlier entropy-only concern that every common-endpoint
branch might differ in merely `O(log n)` central targets.

It does not prove directional mobility.  A reached residual family may
avoid every deck in the code, as the dictator-star obstruction shows, and
the replacement sets supplied by two far decks need not be the targets
needed by an alternating augmentation.  The remaining positive theorem
must couple this linear-distance code to reachable-residual expansion or
to a global exchange argument.
