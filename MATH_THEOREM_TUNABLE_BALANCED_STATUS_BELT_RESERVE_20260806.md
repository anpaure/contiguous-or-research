# A tunable balanced status belt is an exact recursive owner/root reserve

## Status

A single balanced coordinate vortex has size `Theta(W 4^{-a})`.  Taking
all complementary vortices on one `2a`-coordinate block produces a much
larger and more flexible reserve: the central status class has density
`Theta(a^{-1/2})`.  Thickening it by any fixed number of status layers
still has that density and contains every owner/root resource whose packet
degree changes when packets meeting the central bank are removed.

This note proves that the thickened belt has an unconditional simple
spanning owner/root `2`-factor.  Its scale is tunable: for any
`a->infinity` with `a=o(sqrt r)`, it is `o(W)`, while the intrinsic deadline
still differs from the ambient deadline by at most one.  Thus a future
cover-down theorem may choose the reserve scale after its quantitative
leave bound is known.

The belt symmetry also closes the immediate-upper row fractionally.  There
is an explicit status-dependent distribution on coloured diamonds which
has root load one, owner load two, and raw upper load at least one on every
upper status fibre; orbitwise thinning is exact.  Integral coloured
rounding and source-ring grouping remain open.

The theorem is central only.  Proper lower-chain tickets of a packet can
move by

\[
                         \Theta(\min\{a,D\})
\]

status levels.  In the tunable regime `a=o(sqrt r)` and
`D=Theta(sqrt r)`, this is `Theta(a)`, not `Theta(D)`.  It is nevertheless
unbounded, so their complete decorated reserve is not confined to any
fixed-width belt.

## 1. The balanced bank and its belt

Put

\[
 n=2r-1,
 \qquad W=\binom{2r-1}{r}.                              \tag{1.1}
\]

Fix a coordinate block `S subset [n]` of size `2a`, let `C=[n]-S`, and
put

\[
                         g=r-a,
 \qquad |C|=2g-1.                                       \tag{1.2}
\]

For a fixed integer `p>=0`, define the owner and root belts

\[
 \begin{aligned}
 \mathcal O_p(S)
   &=\{X\in\tbinom{[n]}r: ||X\cap S|-a|\le p\},\\
 \mathcal Q_p(S)
   &=\{Y\in\tbinom{[n]}{r-1}: ||Y\cap S|-a|\le p\}.
 \end{aligned}                                          \tag{1.3}
\]

At `p=0`, these are the disjoint union, over all
`A in binom(S,a)`, of the balanced vortex shores with fixed-present set
`A` and fixed-absent set `S-A`.

## 2. Exact size

### Proposition 2.1 (belt density)

For fixed `p` and `a->infinity`, `a=o(r)`,

\[
 \boxed{
 { |\mathcal O_p(S)|\over W}
  =\Theta_p(a^{-1/2}),
 \qquad
 { |\mathcal Q_p(S)|\over W}
  =\Theta_p(a^{-1/2}).}                                  \tag{2.1}
\]

More exactly,

\[
 |\mathcal O_p(S)|
   =\sum_{j=-p}^p
      \binom{2a}{a+j}\binom{2g-1}{g-j},                 \tag{2.2}
\]

and

\[
 |\mathcal Q_p(S)|
   =\sum_{j=-p}^p
      \binom{2a}{a+j}\binom{2g-1}{g-1-j}.               \tag{2.3}
\]

#### Proof

Choose the intersection with `S` and then the neutral coordinates,
giving (2.2)--(2.3).  For every fixed `j`, Stirling's formula gives

\[
 \binom{2a}{a+j}=\Theta(4^a/\sqrt a),
 \qquad
 \binom{2g-1}{g-j}=\Theta(4^g/\sqrt g),                 \tag{2.4}
\]

uniformly over `|j|<=p`; the analogous root estimate is identical.
Since `W=Theta(4^{a+g}/sqrt(a+g))` and `a=o(r)`, each summand has ratio
`Theta(a^{-1/2})`, proving (2.1). \(\square\)

Thus `a` may tend to infinity arbitrarily slowly, giving an `o(W)` reserve
which can be much larger than the critical `W/sqrt r` single vortex.

## 3. Exact product model

Let

\[
 R_{a,p}=\mathcal B_{2a}[a-p,a+p]                       \tag{3.1}
\]

be the rank-selected Boolean band, regraded so that its ranks are
`0,...,2p`.  It is rank-symmetric, normal, and has a log-concave rank
sequence.  The full belt poset is

\[
 \boxed{R_{a,p}\times\mathcal B_{2g-1}.}                \tag{3.2}
\]

Its two central product ranks correspond exactly to the set-ranks `r-1`
and `r` in (1.3).

### Theorem 3.1 (simple spanning 2-factor in the belt)

For every fixed `p`, if

\[
                         g\ge4p(p+1),\qquad g-p\ge2,     \tag{3.3}
\]

then the incidence graph between `mathcal Q_p(S)` and `mathcal O_p(S)`
contains a simple spanning `2`-factor, equivalently two edge-disjoint
perfect matchings.

#### Proof

The proof of the symmetric-halo two-factor theorem uses only the following
properties of its boundary factor `R`: rank symmetry, normality,
log-concavity, rank `2p`, and monotonicity of its rank numbers up to `p`.
The Boolean band `R_(a,p)` has all of them.

For completeness, route the cumulative imbalance between consecutive
boundary ranks through normalized flows of `R_(a,p)`.  The neutral-edge
weight is at most `1/(g-p)`, and the boundary-edge weight is at most

\[
                         {2p(p+1)\over g}.                \tag{3.4}
\]

This gives a fractional perfect matching with maximum edge weight

\[
 \gamma\le
 \max\left\{{1\over g-p},{2p(p+1)\over g}\right\}.     \tag{3.5}
\]

Under (3.3), doubling the flow keeps every edge weight at most one and
gives degree two at every vertex.  The bipartite capacitated
`b`-matching polytope is integral, so it has a simple integral spanning
`2`-factor. \(\square\)

At `p=0`, each fixed `A=X cap S` is a separate middle-levels graph on
`C`, and the Middle Levels Theorem gives a Hamilton cycle in every fibre.
For `p>0`, Theorem 3.1 also uses cross-status incidence edges and need not
respect that fibre decomposition.

The transfer from the rectangular-halo proof can be made completely
explicit here.  Index a status fibre by

\[
                         j=|X\cap S|-a\in[-p,p].          \tag{3.6}
\]

For a root of status `j`, the neutral rank is `g-1-j`.  Thus it has
`g+j` neutral upward edges and, when `j<p`, `a-j` status-changing upward
edges.  Let `t=j+p` be the corresponding rank of `R_(a,p)`, let `L_t,U_t`
be the lower/upper central fibre sizes, and put

\[
 F_t=\sum_{i=0}^t(L_i-U_i),\qquad
 \eta_j={F_t\over L_t}.                                  \tag{3.7}
\]

Then

\[
 0\le\eta_j\le {2p(p+1)\over g},                         \tag{3.8}
\]

and the fractional matching of Theorem 3.1 assigns

\[
 {1-\eta_j\over g+j}                                     \tag{3.9}
\]

to every neutral upward edge at status `j`, and

\[
 {\eta_j\over a-j}                                       \tag{3.10}
\]

to every status-changing edge.  At `j=p`, interpret (3.10) as zero.
These formulas follow because every consecutive pair of ranks in the
Boolean band is biregular, so its normalized flow is uniform.  They also
give a direct line-by-line verification of (3.4), without importing any
additional hypothesis from the rectangular halo.

## 3.1 The status symmetry closes the fractional upper-colour row

The belt has one advantage over a fixed directed `A`-present, `B`-absent
halo: its stabilizer is transitive on every status fibre.  This turns the
upper-coloured fractional problem into a scalar recurrence.

Put

\[
                         \sigma_j=2\eta_j.                \tag{3.11}
\]

Under (3.3), `0<=sigma_j<=1`.  At a root `Q` of status `j`, choose an
unordered pair of owner neighbours as follows:

* with total weight `1-sigma_j`, choose two neutral additions uniformly;
* with total weight `sigma_j`, choose one neutral and one status-coordinate
  addition uniformly.

There are no two-status-coordinate pairs.  Explicitly, every neutral pair
has weight

\[
                {1-\sigma_j\over\binom{g+j}2},            \tag{3.12}
\]

and every mixed pair has weight

\[
                {\sigma_j\over(g+j)(a-j)}.                \tag{3.13}
\]

Again (3.13) is zero at `j=p`.

### Theorem 3.2 (fractional upper-decorated belt factor)

The diamond weights (3.12)--(3.13) have the following properties.

1. Every root has diamond load one.
2. Every owner has incidence load two.
3. Every rank-`(r+1)` upper target whose status lies in `[-p,p]` has raw
   load

   \[
    \boxed{
    \lambda_j=
      {(g+1-j)(g+3j)\over(g-1+j)(g+j)}.}                  \tag{3.14}
   \]

4. If `g>=2p(p+1)`, then `lambda_j>=1` for every
   `-p<=j<=p`; hence typewise marking gives every such upper target marked
   load exactly one.

#### Proof

The root equation is immediate.  A neutral owner edge at status `j` is
selected with marginal

\[
 {2-\sigma_j\over g+j},                                  \tag{3.15}
\]

and a status-changing edge with marginal

\[
 {\sigma_j\over a-j}.                                    \tag{3.16}
\]

These are exactly twice (3.9)--(3.10), so Theorem 3.1's fractional flow
gives owner load two.  Equivalently, the scalar identity is

\[
 (g-j){2-\sigma_j\over g+j}
 +(a+j){\sigma_{j-1}\over a-j+1}=2,                      \tag{3.17}
\]

where `sigma_(-p-1)=0` and `sigma_p=0`.

An upper target of status `j` is produced either by a neutral pair at a
root of status `j`, or by a mixed pair at a root of status `j-1`.
Transitivity inside each status fibre and elementary binomial ratios give

\[
 \begin{aligned}
 \lambda_j
  ={}&{(g-j)(g+1-j)\over(g+j)(g-1+j)}(1-\sigma_j)\\
   &+{a+j\over a-j+1}{g+1-j\over g-1+j}\sigma_{j-1}.
                                                               \tag{3.18}
 \end{aligned}
\]

Substitute (3.17).  The dependence on `a,p,sigma` cancels, leaving (3.14).
Finally,

\[
 \lambda_j-1=
 {2(g+2j-2j^2)\over(g-1+j)(g+j)}.                        \tag{3.19}
\]

The numerator is nonnegative on `[-p,p]` once
`g>=2p(p+1)`.  Constant thinning in each status orbit then gives exact
marked upper load. \(\square\)

Thus the belt formulation really is easier on the immediate-upper row:
it has an explicit full fractional diamond factor, rather than only an
aggregate scalar surplus.  This remains a fractional statement.  The
local determinant-two diamond minor is still present, so integral coloured
rounding does not follow from bipartite `b`-matching integrality.

## 3.2 Fixed-uniform nibble consequence

The preceding fractional point is sufficiently spread to round
approximately **with the upper colours present**.  This is another benefit
of passing from long source packets to the status-symmetric diamond belt.

### Theorem 3.3 (upper-decorated belt cover up to `o(1)`)

Fix `p` and let `g->infinity`.  There is a partial simple owner/root
`2`-factor in the belt which covers

\[
 (1-o(1))|\mathcal Q_p(S)|
\]

roots and the same proportion of the two owner-capacity slots, and whose
upper colours include all but an `o(1)` proportion of the upper targets in
statuses `[-p,p]`.

#### Proof

Split every owner into two labelled capacity copies.  For every unordered
diamond of weight `z`, use its two orientations, each with weight `z/2`,
assigning its two owners to the two different capacity copies.

If the diamond's upper status is `j`, split each oriented copy into:

* a **marked** copy of weight `z/(2lambda_j)`, containing the root, the two
  owner slots, and the upper target;
* an **unmarked** copy of the remaining weight, containing the root and the
  two owner slots but no constrained upper resource.

One may pad every unmarked copy by a private dummy vertex.  Theorem 3.2
then says that the resulting fixed-uniform hypergraph has fractional load
one at every root, every owner slot, and every constrained upper target.

Its maximum single-edge weight is `O_p(g^{-2})`.  Indeed a neutral pair has
weight at most `1/binom(g-p,2)`, while a mixed pair has weight at most

\[
 {4p(p+1)/g\over(g-p)(a-p+1)}=O_p(g^{-2}).                \tag{3.20}
\]

The maximum weighted pair load is `O_p(g^{-1})`:

* a root--owner pair is one owner-edge marginal from (3.15)--(3.16);
* a root--upper or owner--owner pair determines at most a bounded number
  of diamonds and has load `O_p(g^{-2})`;
* an owner--upper pair lies in at most `r` diamonds, each of weight
  `O_p(g^{-2})`;
* private dummies create no cross-edge codegree.

Thus all weighted codegrees tend to zero.  The standard fixed-uniform
fractional-matching nibble (equivalently, rational blow-up followed by the
Rödl nibble) gives a matching missing only `o(1)` of every unit-load
required vertex class.  Forgetting the private dummies gives the claimed
partial simple `2`-factor and upper coverage. \(\square\)

Theorem 3.3 is still not an exact coloured factor.  Its value is that the
integral belt obstruction has been reduced to an `o(|mathcal O_p|)`
structured leave in a **four-uniform** local problem.  The growing
`Theta(D)` packet uniformity no longer enters the immediate-upper rounding.
Source-ring grouping and proper lower tickets must be restored after this
diamond-level rounding.

## 4. Exact central exposure of a packet crossing the bank

Consider a two-hole packet with top `H`.  Its owners are `H-e` with
`|e|=2`, its immediate roots are `H-T` with `|T|=3`, and its immediate
uppers are `H-z`.

### Proposition 4.1 (fixed-width belt contains every central casualty)

If such a packet contains an owner or root in the central bank
`mathcal O_0(S) union mathcal Q_0(S)`, then every owner of the packet lies
in `mathcal O_3(S)`, every immediate root lies in `mathcal Q_3(S)`, and
every immediate upper has status

\[
                         ||U\cap S|-a|\le3.              \tag{4.1}
\]

Consequently, deleting all packets which meet the central bank leaves the
degree of every owner/root resource outside the radius-three belt literally
unchanged.

#### Proof

Write

\[
                         h_S=|H\cap S|-a.                 \tag{4.2}
\]

An owner, root, and upper status is respectively

\[
 h_S-u_2,\qquad h_S-u_3,\qquad h_S-u_1,                  \tag{4.3}
\]

where `0<=u_i<=i`.  If a central owner occurs, then `h_S in[0,2]`; hence
all owner, root, and upper statuses lie respectively in
`[-2,2],[-3,2],[-1,2]`.  If a central root occurs, then
`h_S in[0,3]`; the corresponding ranges are
`[-2,3],[-3,3],[-1,3]`.  Their union is contained in the radius-three
belt, proving the assertion and its degree contrapositive. \(\square\)

The constant three is deliberately uniform over the owner/root comparison.
Sharper row-dependent radii are possible but unnecessary here.

### Proposition 4.2 (fixed-width belts cannot contain the lower tickets)

Let

\[
                 1\le t\le\min\{a,D-1\}.                 \tag{4.4}
\]

There is an all-high `D+2` packet containing a central-bank owner and a
proper width-one ticket of status `-t`.  Consequently, if `a->infinity`, no
fixed `p` contains all proper tickets of packets meeting the central bank.

#### Proof

Choose the packet common core `K` so that

\[
                         |K\cap S|=a-t.                   \tag{4.5}
\]

Among the `D+2` private labels choose exactly `t` labels in `S`.  Cyclically
order them so that one length-`D` owner window contains all `t`, while one
of its other phases is a neutral private label.  This is possible because
`t<=D-1`: besides the `t` status labels there are at least three neutral
private labels, two for the omitted phases and one for the displayed
width-one phase.

The selected owner has `S`-intersection size `(a-t)+t=a`, so it is in the
central bank.  The displayed width-one union has `S`-intersection
`a-t`, hence status `-t`. \(\square\)

Proposition 4.2 is sharp at the scale relevant here.  The status belt makes
the owner/root and immediate-upper rows one-dimensional, but it does not
compress the arbitrary-depth lower compiler into a bounded status window.

## 5. Tunable recursive phase

If `a=o(sqrt r)` and `g=r-a`, the odd-deadline stability theorem gives,
under its explicit finite inequality,

\[
                         d(2r-1)-d(2g-1)\in\{0,1\}.      \tag{5.1}
\]

The phase-adaptive antipodal theorem gives every already-selected halo
diamond a local literal lift in either of the two values in (5.1), with no
additional source position.  This is a local vocabulary theorem, not a
joint selection theorem for all diamonds.  Consequently choosing
`a->infinity` slowly creates no *local scalar* recursive toll; integral
co-selection of the lifted rings remains part of the coloured packet gate.

Combining Theorem 3.1 with the exact C6 loose-tree splice gives the following
proof-safe reduction:

> Cover all central resources outside the balanced belt by decorated
> packets; realize the belt by a phase-appropriate decorated `2`-factor;
> plant a serially sealed loose tree of C6 ports across all resulting
> components; and protect or reroute every nonlocal lower/upper ticket.

The uncoloured owner/root rows, the fractional immediate-upper row, and the
zero-length local splice are now unconditional.  The remaining difficulty
is integral coloured rounding, compatible source-ring grouping, and the
protected nonlocal-ticket cover-down.  The reserve scale itself is no
longer fixed in advance.
