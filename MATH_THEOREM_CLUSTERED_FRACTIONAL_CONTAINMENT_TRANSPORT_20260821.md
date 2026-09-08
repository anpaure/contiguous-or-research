# Exact fractional containment transport for clustered product profiles

**Status (2026-08-21).**  Every assertion below is proved.  The formal
clustered profile capacities admit an exact labelled fractional transport on
the Boolean containment graph.  At each upper offset `q`, the transport has
value

\[
 \sum_s\min(P_{q,s},T_{q,s}),
\]

so its aggregate target deficit is `O(W_b b^(-1/4))=o(W_b)`.  Ordinary
bipartite-flow integrality then gives, separately at each `q`, an integral
containment matching of at least the same size.

This is a relaxation, not the coefficient-one construction.  The integral
matching may choose extensions that cannot be realized simultaneously by one
set of tight-cycle factors, clustered phases, and cyclic orders.  Matchings
obtained separately at different `q` need not form nested extension chains.
The theorem identifies the remaining obstruction as **coinstantiation of the
order geometry**, not fractional labelled transport or Boolean containment.

## 1. Source and target profiles

Let `A,B` be disjoint `b`-sets, with `b` an odd prime.  Let

\[
 W_b={2b\choose b},\qquad
 H/\sqrt b\longrightarrow\infty,\qquad H=o(b^{2/3}),
\]

and let

\[
 I=\{H+2,\ldots,b-H-2\}.
\]

Conditional complementary-rank tight-cycle factors partition the middle
targets of split `r` for every `r in I`; there are

\[
 {b\choose r}^2                                      \tag{1.1}
\]

such middle targets.  The theorem below only uses these source sets and the
clustered phase counts, so it is also a statement about the corresponding
formal containment relaxation.

Fix `1<=q<=H`.  For a payload rank `r`, let `n_(r,q,z)` be the number of base
phases at which the next `q` symbols of `A^rB^(b-r)` contain exactly `z`
`A`-symbols.  Since `q<=r,b-r`,

\[
 n_{r,q,z}=
 \begin{cases}
  b-r-q+1,&z=0,\\
  2,&1\le z\le q-1,\\
  r-q+1,&z=q,
 \end{cases}
 \qquad
 \sum_{z=0}^q n_{r,q,z}=b.                            \tag{1.2}
\]

An upper target `V` at rank `b+q` has split

\[
 s=|V\cap A|,
 \qquad
 P_{q,s}={b\choose s}{b\choose s-q}.                 \tag{1.3}
\]

On a central admissible profile, its formal occurrence capacity is

\[
 T_{q,s}
 ={1\over b}\sum_{\substack{r\in I\\0\le s-r\le q}}
 n_{r,q,s-r}{b\choose r}^2.                          \tag{1.4}
\]

This is the same capacity as the explicit three-term clustered formula.
Outside a fixed central interval, set `T_(q,s)=0` and charge the exponentially
small target mass in full.

## 2. A symmetric fractional flow

Let `L_q` consist of every middle `b`-set `U` whose split
`r=|U cap A|` lies in `I`, and let `R_q` consist of the rank-`(b+q)` targets.
Join `U` to `V` when `U subset V`.  All vertices have unit matching capacity.

For `U` of split `r` and an integer `z`, the number of containment neighbours
`V` with split `r+z` is

\[
 D_{r,q,z}={b-r\choose z}{r\choose q-z}.              \tag{2.1}
\]

For a central profile `s`, put

\[
 \rho_{q,s}=
 \begin{cases}
  \min(1,P_{q,s}/T_{q,s}),&T_{q,s}>0,\\
  0,&T_{q,s}=0.
 \end{cases}                                          \tag{2.2}
\]

If `U subset V`, write `r=|U cap A|`, `s=|V cap A|`, and `z=s-r`.
Define

\[
 f_q(U,V)=
 \rho_{q,s}{n_{r,q,z}\over bD_{r,q,z}}               \tag{2.3}
\]

when `r in I` and `0<=z<=q`, and put `f_q(U,V)=0`
otherwise.

### Theorem 2.1 (exact fractional profile transport)

The weights `f_q` form a feasible fractional matching.  Every target `V` in
profile `s` receives exactly

\[
 \sum_U f_q(U,V)=\min\left(1,{T_{q,s}\over P_{q,s}}\right), \tag{2.4}
\]

and the total flow into that profile is exactly

\[
 \min(P_{q,s},T_{q,s}).                               \tag{2.5}
\]

#### Proof

For a fixed source `U` of split `r`, summing (2.3) over all neighbours with a
fixed `z` gives `rho_(q,r+z)n_(r,q,z)/b`.  Hence its total outgoing load is at
most

\[
 {1\over b}\sum_{z=0}^q n_{r,q,z}=1.                 \tag{2.6}
\]

Now fix a target `V` of split `s`.  For `r` and `z=s-r`, the number of
split-`r` sources contained in `V` is

\[
 {s\choose r}{b+q-s\choose b-r}.                     \tag{2.7}
\]

The two elementary choose-in-either-order identities give

\[
 {{s\choose r}{b+q-s\choose b-r}\over
  {b-r\choose z}{r\choose q-z}}
 ={ {b\choose r}^2\over
    {b\choose s}{b\choose s-q}}
 ={ {b\choose r}^2\over P_{q,s}}.                    \tag{2.8}
\]

Therefore (2.3), summed over all contributing `r`, gives

\[
 \sum_U f_q(U,V)
 =\rho_{q,s}{T_{q,s}\over P_{q,s}}
 =\min\left(1,{T_{q,s}\over P_{q,s}}\right).         \tag{2.9}
\]

This is at most one, proving the target constraints.  Multiplication by the
`P_(q,s)` targets in the profile proves (2.5).  \(\square\)

The flow also has a direct symmetrization interpretation.  Give a source
`U` a uniform clustered base phase, so the chance of `z` additions from `A`
is `n_(r,q,z)/b`; conditional on `z`, choose the `z` new `A`-letters and the
`q-z` new `B`-letters uniformly.  Equation (2.3) is this containment kernel,
with the harmless rankwise real-claim thinning `rho_(q,s)`.  It is the
transitive orbit-average relaxation obtained when labels may be symmetrized
at the token level, not one fixed order bank.

## 3. Integral containment matching and aggregate deficit

### Theorem 3.1

For every fixed `q`, the containment graph has an integral matching of size
at least

\[
 \sum_s\min(P_{q,s},T_{q,s}).                         \tag{3.1}
\]

Consequently one can choose distinct middle sources and distinct upper
targets at every `q` separately with aggregate upper-band target deficit

\[
 \sum_{q=1}^H\left[{2b\choose b+q}-|\mathcal M_q|\right]
 =O(W_b b^{-1/4})=o(W_b).                             \tag{3.2}
\]

#### Proof

Theorem 2.1 is a feasible point of the ordinary bipartite matching polytope.
That polytope is integral: equivalently, replace every vertex by a unit
capacity arc and apply integral max flow.  Thus a maximum integral matching
has cardinality at least the fractional value (3.1).

The uncovered target count at rank `q` is at most

\[
 \sum_s[P_{q,s}-T_{q,s}]_+.
\]

The pooled clustered profile-capacity theorem sums this quantity over
`1<=q<=H` to `O(W_b b^(-1/4))`, including the fully charged tail profiles.
This proves (3.2).  \(\square\)

The integral matching in Theorem 3.1 does **not** retain the phase-class
amounts `n_(r,q,z)` from the fractional witness.  Integrality applies after
all containment edges are placed in one graph; it may select individually
possible edges which require incompatible local order conjugations.  This is
why Theorem 3.1 is a relaxation rather than a product-word construction.

## 4. A joint fractional chain across all offsets

There is no cross-`q` obstruction at the fractional containment level either.
For a source `U` of split `r`, choose one base phase `p` uniformly in
`Z_b`.  Let `z_q` be the number of `A` phases among the next `q` clustered
phases.  Independently choose uniform random orderings of `A\setminus U` and
`B\setminus U`, and define

\[
 V_q=U\cup\{\hbox{first }z_q\hbox{ letters of }A\setminus U\}
       \cup\{\hbox{first }q-z_q\hbox{ letters of }B\setminus U\}. \tag{4.1}
\]

Then

\[
 U=V_0\subset V_1\subset\cdots\subset V_H,           \tag{4.2}
\]

and the marginal law at every `q`, after assigning real-claim weight
`rho_(q,|V_q cap A|)`, is exactly the flow (2.3).  Thus all the fractional
profile transports have marginals carried by one nested containment-chain
law.

The assertion follows because `z_(q+1)-z_q` is the next type bit, while the
first `z_q` and first `q-z_q` entries of the two fixed random complement
orders are nested.  Conditional on `z_q=z`, those prefixes are uniform
subsets of the required sizes, giving (2.3).

The unthinned chain `(V_q)` is a single probability law.  Multiplication by
the profile-dependent `rho_(q,s)` is rankwise fractional claim bookkeeping;
no claim is made that the thinned marginals form a probability law on chains
which are real at every rank, or that their separate integral matchings are
one simultaneous integral chain family.

## 5. Exact remaining coinstantiation gate

Three relaxations are now separately exact up to `o(W_b)`:

1. pooled scalar split-profile capacity;
2. integral Ferrers balancing of all counter-origin phase diagonals; and
3. labelled fractional containment transport, even on nested chains, plus
   an integral containment matching at each offset separately.

They do not automatically compose.  A physical product atom fixes, for every
middle source, one extension chain coming from two cyclic orders.  Sources in
the same tight cycle share that order, the same atom must serve all offsets,
and compatible order coordinates are needed across neighboring payload
ranks.  The missing theorem must round the joint fractional chain while
respecting those factor-cycle blocks and the Ferrers origins, or directly
construct a simultaneous multirank factor coupling with the same effect.

In particular, ordinary bipartite total unimodularity is exhausted by
Theorem 3.1.  The surviving constraint is the intersection with global
order-bank realizability, not another one-profile Hall inequality.
