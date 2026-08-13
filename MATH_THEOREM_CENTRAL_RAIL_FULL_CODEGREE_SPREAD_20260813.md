# Full codegree spread of the central resident rail hypergraph

**Date:** 2026-08-13  
**Status:** unconditional full-codegree upper bound and quantitative spread
theorem.  In the target regime its Gould--Kelly-type spread parameter is
`Omega(sqrt(k))`.  This is a geometric input to a matching theorem, not by
itself a diagonal growing-uniformity matching theorem.

## 1. Setup

Put

\[
 q=d+1,\qquad c=R-q,\qquad r=2q+1,
\]

and let `H_cent` be the parameterized hypergraph on the rank-`R` owners.
An edge is a core `C`, a toggle set `T` of size `r`, and a directed cyclic
order of `T` modulo rotation; its vertices are

\[
 C\cup I_i^q\qquad(i\in\mathbb Z_r).                \tag{1.1}
\]

Parallel directed orientations are retained.  Let `D_j` denote the
maximum number of parameterized edges containing a prescribed set of `j`
distinct owners.  Thus `D_1=D` is the exact vertex degree.

For two owners at Johnson distance `t`, the exact pair formula is

\[
 {\lambda_t\over D}
 ={2(t!)^2\over(R)_t(k-R)_t}\qquad(1\le t\le q),     \tag{1.2}
\]

and the codegree is zero for `t>q`.

## 2. A metric fact for cyclic windows

### Lemma 2.1

Let `j` distinct starts be chosen on the cycle `Z_r`.  Some pair has
cyclic distance at least

\[
 s_j=\left\lceil{j-1\over2}\right\rceil.             \tag{2.1}
\]

#### Proof

Fix any chosen start.  The ball of cyclic radius `s_j-1` around it has at
most

\[
 1+2(s_j-1)\le j-1
\]

positions.  It cannot contain all `j` chosen starts.  A chosen start
outside the ball gives the required pair.  `square`

For central `q`-windows on a `(2q+1)`-cycle, the Johnson distance between
the windows at starts `a,b` is exactly their cyclic distance

\[
 \min\{|a-b|,r-|a-b|\}\in\{0,1,\ldots,q\}.          \tag{2.2}
\]

Adjoining the common core does not change that distance.

## 3. Full codegree bound

### Theorem 3.1

For every `2<=j<=r`, put `s=s_j`.  Then

\[
 \boxed{
 D_j\le \max_{s\le t\le q}\lambda_t.}              \tag{3.1}
\]

If the pair codegrees decrease with distance, as they do whenever

\[
 (t+1)^2<(R-t)(k-R-t)\qquad(s\le t<q),              \tag{3.2}
\]

then

\[
 \boxed{
 {D_j\over D}
 \le {2(s!)^2\over(R)_s(k-R)_s},
 \qquad s=\left\lceil{j-1\over2}\right\rceil.}      \tag{3.3}
\]

#### Proof

Take `j` owners contained in a common central edge.  Remove its common
core and identify the resulting petals with their `j` distinct cyclic
`q`-windows.  Lemma 2.1 supplies two of those windows whose cyclic, hence
Johnson, distance is some `t>=s`.  Every parameterized edge containing
all `j` owners also contains this fixed pair.  Its number is therefore at
most `lambda_t`, proving (3.1).  Formula (3.2) and the exact ratio

\[
 {\lambda_{t+1}\over\lambda_t}
 ={(t+1)^2\over(R-t)(k-R-t)}
\]

then give (3.3).  `square`

No factor `binom(j,2)` is needed: after fixing the owner family, one
distance-large pair from any one containing edge is a fixed pair of named
owners, and every other containing edge must still contain it.

## 4. Quantitative spread parameter

Define

\[
 B_{\rm cent}=
 \min\left\{
   \sqrt{D/D_2},
   \min_{4\le j\le r}(D/D_j)^{1/(j-1)}
 \right\}.                                          \tag{4.1}
\]

This is the full-codegree scale that appears, up to conventions, in
modern higher-codegree nibble theorems.

### Corollary 4.1

Let

\[
 a=\min\{R,k-R\},\qquad q\le a/4.
\]

Then, for an absolute constant `c_0>0`,

\[
 \boxed{B_{\rm cent}\ge c_0,{a\over q}.}            \tag{4.2}
\]

In particular, if `R,k-R=Theta(k)` and `q=Theta(sqrt(k))`, then

\[
 \boxed{B_{\rm cent}=\Omega(\sqrt k).}               \tag{4.3}
\]

#### Proof

For `1<=s<=q`,

\[
 (R)_s(k-R)_s\ge(a-q)^{2s},\qquad s!\le s^s.        \tag{4.4}
\]

Hence (3.3) gives

\[
 {D_j\over D}\le
 2\left({s\over a-q}\right)^{2s}.                  \tag{4.5}
\]

If `j=2s+1`, taking the `1/(j-1)=1/(2s)` root yields at least

\[
 2^{-1/(2s)}{a-q\over s}.
\]

If `j=2s`, the exponent is `1/(2s-1)` and gives a no smaller bound up to
an absolute constant because `(a-q)/s>=3`.  The minimum over `s<=q` is
therefore `Omega((a-q)/q)=Omega(a/q)`.  Finally,

\[
 \sqrt{D/D_2}=\sqrt{R(k-R)/2}\ge a/\sqrt2,
\]

which is not the smaller term.  This proves (4.2)--(4.3).  `square`

## 5. Exact terminal tail

The estimate above is deliberately an upper bound, not a claim that every
`D_j` is attained by consecutive windows.  At the terminal end one has an
exact flat tail:

\[
 \boxed{D_{r-1}=D_r=2.}                              \tag{5.1}
\]

To see this, `r-1` owners from one support recover the core as their
intersection.  In the resulting petal family, the `q` labels of the
missing window have incidence degree `q-1`, and the other `q+1` toggle
labels have degree `q`; hence the toggle set and missing window are
recovered.  The adjacency graph on the full family, joining windows with
intersection `q-1`, is a cycle, whose two directions give exactly the two
directed orders modulo rotation.  The full support likewise has those two
orientations.

This tail explains why a Vu hierarchy based on consecutive ratios cannot
simply be extended through `j=r`: the last ratio is one.  The global
spread parameter (4.1), however, remains large because it compares every
`D_j` directly to `D`.

## 6. Matching-theorem boundary

Corollary 4.1 establishes the precise higher-codegree geometry that the
pair-only audit left open.  Formally, a theorem with a leave of order

\[
 O\bigl(|V|B_{\rm cent}^{-1+o(1)}\bigr)
\]

would give an `o(|V|)` owner leave here.  The presently cited
Gould--Kelly and Vu formulations, however, fix the uniformity before the
degree limit or contain constants/hierarchies not controlled when

\[
 r=2q+1=\Theta(\sqrt k).
\]

Therefore (4.3) is a material positive input, but it is not being used as
an illicit diagonal black box.  A proof still needs either:

1. a matching theorem uniform for this growing `r` and the exact spread
   (3.3); or
2. a direct random-greedy/absorbing argument exploiting the cyclic-window
   structure.

