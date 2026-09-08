# Algebraic rigidity of shift-compatible symmetric-chain projections

## 1. Outcome

This note tests two of the most direct algebraic realizations of the
shift-compatible SCD target from Sections 9--12 of
`PARTIAL_BLOCK_MULTISCALE.md`.

The target is a middle projection

\[
 f(X)=X-\{r_0(X)\}+\{u_0(X)\}
\]

which preserves the radius class and whose flags shift according to

\[
 r_i(fX)=r_{i+1}(X),\qquad
 u_i(fX)=u_{i+1}(X).                                  \tag{1.1}
\]

Two natural algebraic shortcuts are impossible.

1. On an orientation cube, an affine permutation which sends almost every
   vertex to a Hamming neighbour must in fact send every vertex to a
   neighbour, and then all its cycles have length at most four.
2. On the Boolean middle layer, an orbit of one fixed coordinate
   permutation can be a long Johnson orbit only on an exponentially small
   family.  More quantitatively, covering a positive fraction of the
   typical-radius centres by such orbits needs exponentially many distinct
   coordinate permutations.

These are geometry theorems, not capacity estimates.  They rule out a
single affine successor in each pair-orientation cube, a bounded or
polynomial collection of cyclic coordinate actions, and any analogous
subexponential template family.  They do **not** rule out the actual wreath
program: that program is allowed exponentially many coordinate orders and
a nonlinear, state-dependent successor rule.

The checker `scratch/verify_shift_scd_algebra.cpp` exhausts all affine
permutations through dimension four and all coordinate permutations through
eight points.

## 2. Shift recurrence forces long locally geodesic cycles

Let a radius-`d` chain centred at an `m`-set `X` have ordered labels

\[
 r_0(X),\ldots,r_{d-1}(X)\in X,
 \qquad
 u_0(X),\ldots,u_{d-1}(X)\notin X.                  \tag{2.1}
\]

All removal labels are distinct, all addition labels are distinct, and the
two lists are disjoint.  Under (1.1), induction gives

\[
 f^j(X)=X-\{r_0,\ldots,r_{j-1}\}
          +\{u_0,\ldots,u_{j-1}\}
 \qquad(0\le j\le d).                               \tag{2.2}
\]

### Lemma 2.1 (period lower bound)

If `X` has radius `d>0` and belongs to an `f`-cycle of length `p`, then

\[
                              p>d.                   \tag{2.3}
\]

#### Proof

If `p<=d`, equation (2.2) gives

\[
 f^p(X)=X-\{r_0,\ldots,r_{p-1}\}
          +\{u_0,\ldots,u_{p-1}\}\ne X,
\]

because the displayed removal and addition sets are disjoint and nonempty.
This contradicts `f^p(X)=X`.  QED.

For the `2m`-cube, the number of radius-`d` chains is

\[
 V_d=\binom{2m}{m-d}-\binom{2m}{m-d-1}.             \tag{2.4}
\]

Consequently, for any fixed `0<a<b`,

\[
 \sum_{a\sqrt m\le d\le b\sqrt m}V_d
 =\binom{2m}{m-\lceil a\sqrt m\rceil}
  -\binom{2m}{m-\lfloor b\sqrt m\rfloor-1}
 =\Theta(W).                                         \tag{2.5}
\]

Thus a shift-compatible SCD needs cycles of length `Theta(sqrt(m))` on a
positive fraction of all middle centres.  This is the scale against which
the algebraic actions below must be tested.

## 3. Affine-neighbour rigidity on an orientation cube

Write the orientation cube as `Q_s=F_2^s`, with Hamming neighbours differing
by one standard unit vector.  Let

\[
                              F(x)=Ax+b              \tag{3.1}
\]

be an affine permutation, and put

\[
 M=A+I,\qquad r=\operatorname {rank}M.               \tag{3.2}
\]

The displacement map is

\[
                              F(x)+x=Mx+b.            \tag{3.3}
\]

### Lemma 3.1 (unit vectors in an affine flat)

An affine subspace of `F_2^s` of dimension `r` contains at most `r+1`
standard unit vectors.

#### Proof

Any `t` distinct unit vectors are affinely independent up to dimension
`t-1`: after choosing one of them as origin, the `t-1` differences
`e_i+e_{i_0}` are linearly independent.  Hence an `r`-flat contains at most
`r+1` of them.  QED.

### Theorem 3.2 (affine-neighbour bound)

The fraction of vertices `x` for which `F(x)` is a Hamming neighbour of
`x` is at most

\[
                         \boxed{\frac{r+1}{2^r}}.     \tag{3.4}
\]

If this fraction is greater than `3/4`, then `r<=1`.  If it is
`1-o(1)` along a sequence of dimensions, it is eventually exactly one, and
every cycle of `F` has length at most four.

#### Proof

The affine map (3.3) is uniform on the `r`-flat

\[
                         b+\operatorname {im}M;
\]

every point of that flat has `2^(s-r)` preimages.  Lemma 3.1 therefore gives
(3.4).  For `r>=2`, `(r+1)/2^r<=3/4`.  For `r=0` or `1`, the neighbour
fraction belongs to a finite set; if it tends to one, the displacement flat
must consist entirely of unit vectors.

It remains to classify this last case.  If `r=0`, then `A=I` and `b=e_i`,
so `F` is an involutory translation.

If `r=1`, write

\[
 M=u\varphi
\]

for a nonzero linear functional `varphi`.  The two displacement values must
be distinct unit vectors, say

\[
 b=e_i,\qquad b+u=e_j,qquad u=e_i+e_j.              \tag{3.5}
\]

The rank-one determinant identity and invertibility of `A=I+u\varphi`
give

\[
                         \varphi(u)=0.               \tag{3.6}
\]

Hence `A^2=I` and

\[
 F^2(x)=x+u\varphi(b).                               \tag{3.7}
\]

If `varphi(b)=0`, then `F^2=I`; if `varphi(b)=1`, then `F^2` is translation
by `u` and `F^4=I`.  Thus every cycle has length at most four.  QED.

### Corollary 3.3 (no affine orientation-cube solution)

No affine permutation of a growing orientation cube can be the middle
projection of a shift-compatible SCD on all but `o(2^s)` centres of
unbounded radius.  In particular, assigning one affine successor map to a
typical fixed-pair stratum cannot extend the depth-one construction in
`FIXED_PAIR_RESIDUAL_SCD.md` to depth `H->infinity`.

Indeed, the projected move must be a Hamming-neighbour move on
`1-o(1)` of the stratum.  Theorem 3.2 then bounds every orbit by four, while
Lemma 2.1 requires orbit length greater than the assigned radius.

The statement is deliberately about one global affine map on a stratum.  A
piecewise-affine or fully nonlinear cube cycle is not covered by it.

## 4. Fixed coordinate actions: an exact orbit count

Let `g` be a permutation of an `n`-point ground set.  Write its coordinate
cycles as

\[
                         C_1,\ldots,C_c,qquad |C_i|=\ell_i. \tag{4.1}
\]

For `L>=2`, define

\[
 \mathcal A_g(L)=\{X\subseteq[n]:
     |X\mathbin\triangle gX|=2,
     |\operatorname {Orb}_g(X)|\ge L\}.              \tag{4.2}
\]

### Theorem 4.1 (two-transition orbit formula)

For every coordinate permutation `g`,

\[
 \boxed{
 |\mathcal A_g(L)|
  =2^{c-1}\sum_{i:\ell_i\ge L}\ell_i(\ell_i-1).
 }                                                     \tag{4.3}
\]

In particular,

\[
                         |\mathcal A_g(L)|
 \le n^2 2^{n-L}.                                     \tag{4.4}
\]

Both formulas count subsets of all ranks, so (4.4) also bounds the middle
rank.

#### Proof

On one coordinate cycle of `g`, the contribution to
`|X triangle gX|` is the number of binary transitions in the cyclic
incidence word of `X`.  This number is even.  Total distance two therefore
means:

* exactly one coordinate cycle is nonconstant;
* on that active cycle the ones form one nonempty proper cyclic interval;
* every other coordinate cycle is constantly zero or constantly one.

On a cycle of length `ell_i`, there are exactly
`ell_i(ell_i-1)` nonempty proper cyclic intervals.  The other `c-1` cycles
may be chosen independently, giving the summand in (4.3).

A nonempty proper cyclic interval has trivial stabilizer under rotation, so
the `g`-orbit of the resulting set has length exactly `ell_i`.  This proves
the cutoff in (4.3).

For a term with `ell_i>=L`, the number of other coordinate cycles is at
most `n-ell_i`, and hence

\[
 2^{c-1}\ell_i(\ell_i-1)
 \le 2^{n-\ell_i}\ell_i^2.
\]

Summing and using `sum_i ell_i^2<=n^2` gives (4.4).  QED.

The formula exhibits the exact algebraic tradeoff.  Many fixed points or
short coordinate cycles create many Johnson neighbours, but only in short
orbits.  A long coordinate cycle creates a long Johnson orbit, but requiring
one interval on that cycle loses an exponential factor.

Examples:

* for one `n`-cycle, (4.3) gives `n(n-1)` eligible subsets;
* for a product of `n/2` transpositions, it gives
  `n 2^(n/2-1)` eligible subsets, all in orbits of length two.

## 5. A group-template lower bound

Suppose a proposed construction partitions some middle centres into cyclic
bundles, and every bundle is an orbit of one coordinate permutation from a
template family `G_n`.  If all bundles under consideration have length at
least `L`, Theorem 4.1 and a union bound give

\[
 \#\{\text{covered middle centres}\}
 \le |G_n|n^2 2^{n-L}.                               \tag{5.1}
\]

Since

\[
 W_n=\binom n{\lfloor n/2\rfloor}
     =\Theta(2^n/\sqrt n),                           \tag{5.2}
\]

a positive-density cover requires

\[
                         \boxed{
 |G_n|=\Omega\!\left(\frac{2^L}{n^{5/2}}\right).}    \tag{5.3}
\]

### Corollary 5.1 (no small cyclic-action model)

Take `n=2m`.  A positive fraction of the forced SCD radii lie between
`sqrt(m)` and `2sqrt(m)` by (2.5).  Lemma 2.1 and (5.3) imply that any
coordinate-action orbit model for those centres needs

\[
                         2^{\Omega(\sqrt m)}          \tag{5.4}
\]

distinct coordinate permutations.  In particular, no bounded,
polynomial-size, or more generally `exp(o(sqrt(m)))` family of cyclic
generators can produce a near shift-compatible SCD.

This strictly generalizes the fixed-rotation obstruction in
`CYCLIC_INTERVAL_LIFT_INITIALIZATION_AUDIT.md`: it applies to arbitrary
cycle types and makes the orbit-length tradeoff explicit.

The quantifier in this corollary matters.  It applies when each bundle is a
literal orbit of one fixed coordinate permutation.  A factor made from
`Theta(W/m)` unrelated cyclic orders has far more than the minimum number
of templates in (5.4), so the theorem does not obstruct it.

## 6. Consequences for the construction search

The following routes are now excluded.

1. **One affine successor per orientation cube.**  Near-spanning adjacency
   collapses the affine order to at most four.
2. **One global cyclic coordinate action.**  Its long Johnson orbits cover
   an exponentially negligible part of the middle layer.
3. **A small library of cyclic/affine templates.**  At the typical SCD
   radius it needs at least `2^(Omega(sqrt(m)))` different generators.
4. **A straightforward group-equivariant SCD with one generator per
   radius.**  There are only `O(m)` radii, far below (5.4).

What remains viable is precisely the less rigid architecture already
suggested by the audited work:

* exponentially many wreath orders, selected by a global resolution;
* a state-dependent, nonlinear successor inside orientation cubes;
* superposition of many fixed-pair resolutions rather than one affine
  tiling; or
* a genuinely integral Baranyai-style design which couples its different
  coordinate orders across all depths.

The algebraic lesson is therefore negative but sharp.  Symmetry can still
index or balance the construction, but the actual successor cannot be one
small group action.  A successful construction must break symmetry at the
level of individual wreaths while restoring it statistically or through a
large exact design.

## 7. Adversarial scope audit

There are two quantifier transitions in the results above, and both are
worth making explicit.

### Near-affine adjacency really becomes exact adjacency

For a fixed affine map, the neighbour fraction is not an arbitrary real
number.  If `r=rank(A+I)`, it is

\[
 \frac{|(b+\operatorname {im}(A+I))\cap\{e_1,\ldots,e_s\}|}{2^r}.
                                                               \tag{7.1}
\]

The bound `(r+1)/2^r` is at most `3/4` for every `r>=2`.  Hence a sequence
with neighbour fraction `1-o(1)` has `r<=1` eventually.  For `r<=1`, the
possible fractions are discrete (`0,1/2,1`, with repetitions removed in
dimension one), so convergence to one forces the fraction to equal one for
all sufficiently large dimensions.  Only then is the order-at-most-four
classification invoked.  No pointwise conclusion is being inferred from an
average without this discrete rank step.

### The coordinate count uses full literal orbits

Formula (4.3) counts sets for which one **fixed** coordinate permutation
`g` supplies both the Johnson move and the complete cyclic bundle.  The
orbit cutoff is exact because a one-run binary word on the unique active
coordinate cycle has trivial rotational stabilizer.  The union bound (5.1)
therefore applies to a construction which first chooses `g` from a template
family and then uses a full `g`-orbit.

It does not apply when the generator changes with the state, when a cycle is
assembled from edges belonging to different group elements, or when the
successor is nonlinear.  In particular it does **not** exclude:

* a state-dependent pair-flip wreath;
* a nonlinear circuit code in an orientation cube;
* an exponentially large family of unrelated cyclic orders; or
* a Baranyai-style resolution whose individual blocks have unrelated
  generators.

Those are precisely the live cases.  The obstruction says they cannot be
compressed into one affine action or a small cyclic template library; it
does not claim that the live cases fail.

## 8. The remaining algebraic target

The smallest honest positive successor is a **large-template resolution
theorem**:

> Select `W-o(W)` middle centres into locally geodesic cyclic bundles drawn
> from at least `2^(Omega(sqrt(m)))` coordinate orders, and assign the forced
> SCD radii so that every depth-`q` lower and upper flag, for
> `q<=H=sqrt(m) omega(1)`, has total defect `o(W)`.

The exact MSW factor in odd dimension supplies enough distinct wreaths but
not the vertical flags; the residual-SCD construction supplies exact
vertical pairings but not a coherent nonlinear successor.  Theorems 3.2 and
4.1 show that neither side can be made coherent by replacing this missing
coupling with a single affine or cyclic action.
