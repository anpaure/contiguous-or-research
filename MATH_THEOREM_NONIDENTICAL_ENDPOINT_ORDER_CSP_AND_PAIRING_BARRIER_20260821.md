# Nonidentical endpoint orders: exact phase CSP, a mesoscopic no-go, and cheap partial seams

**Status (2026-08-21).**  Every assertion below is proved.  Conditional on
the local tight-cycle factors used by the clustered two-block route, the two
endpoint sources of one fixed split profile admit an exact finite CSP:
there is one variable in `Z_b` for every physical order-pair atom, and every
labelled target is one disjunction of cyclic-interval membership literals.
This reduction keeps arbitrary cross-rank interval multiplicities and hence
does not assume that the two factor banks share orders.

The reduction gives four sharp conclusions.

1. Arbitrarily correlating the factor conjugations does not rescue
   **independent** phase origins.  Conditional on every choice of the four
   factor banks, their expected missed fraction has an explicit positive
   lower bound; it is `1/4-o(1)` on the complementary diagonal.
2. The unrestricted deterministic endpoint CSP itself has a zero-coordinate
   row/column obstruction.  At every mesoscopic offset
   `q~c sqrt(b)`, the endpoint sources miss `Omega_c(W_b)` targets in
   aggregate over the split profiles, for every choice of factors,
   conjugations, and phase origins.  The clustered interior phases have only
   `O(qW_b/b)=o(W_b)` occurrences there, so the complete one-copy clustered
   product-factor bank still has a linear deficit at that rank.
3. Replacing literal common orders by arbitrary nonidentical orders inside
   one-to-one two-atom blocks does not evade the factor-bank cardinality
   barrier.  At a profile whose two bank sizes have a nonunit limiting
   ratio, every such blockwise coupling misses a positive fraction of that
   profile.  The old `b^(1/4)` aggregate barrier therefore applies to all
   one-to-one block couplings, not only literal bank intersections.
4. Nonidentity itself is not expensive.  Swapping one adjacent pair in a
   cyclic order preserves exactly `b-2` interval coordinates at every
   nontrivial rank.  Two atoms whose two local orders differ by `o(b)`
   adjacent swaps can be phase-aligned to cover `(1-o(1))b^2` targets in
   their one block.

Full interval-coordinate isomorphisms are rigid: after all label
conjugations have been fixed, they are only simultaneous dihedral
identifications of the same underlying cycles.  Thus the surviving physical
mechanism is neither a renamed literal intersection, a one-to-one pairing,
nor a many-to-many reassignment of the same one-copy clustered endpoint
atoms.  It must leave that strict route, for example by changing the type
schedule or factor/atom geometry, or by rerouting a linear fraction of the
existing atoms.  An `o(W_b)` seam repair cannot suffice.  No coefficient-one
construction is claimed here.

## 1. Fixed-profile endpoint coordinates

Let `b` be an odd prime and let `A,B` be disjoint `b`-sets.  Fix

\[
 1\le q,\qquad t=s-q,
 \qquad q\le L\le \min(t,b-s).                       \tag{1.1}
\]

The choice `L=q` keeps the ordinary fixed-`q` endpoint phases.  The choice
`L=H` keeps only origins whose next entire `H` type steps are constant, as
in the band-constant endpoint theorem.  Put

\[
 C_j={b\choose j},\qquad f_j={C_j\over b},           \tag{1.2}
\]

and define the two retained phase counts

\[
 a_0=b-s-L+1,\qquad a_1=t-L+1.                      \tag{1.3}
\]

Thus

\[
 a_0+a_1=b-q-2L+2.                                  \tag{1.4}
\]

A rank-`(b+q)` target in split profile `s` is identified with

\[
 (X,Y),\qquad X=V\cap A,\quad
 Y=B\setminus(V\cap B),\quad |X|=s,\quad |Y|=t.     \tag{1.5}
\]

The profile size is

\[
 P_{q,s}=C_sC_t.                                     \tag{1.6}
\]

For an oriented cyclic order `alpha`, with coordinates in `Z_b`, write

\[
 I_\alpha(i,k)=
 \{\alpha_i,\alpha_{i+1},\ldots,\alpha_{i+k-1}\}.   \tag{1.7}
\]

Take independently conjugated tight-cycle factors

\[
\mathcal F_s^A,\ \mathcal F_s^B,
\ \mathcal F_t^A,\ \mathcal F_t^B.                \tag{1.8}
\]

Each rank-`k` factor has `f_k` orders, and the map
`(alpha,i) -> I_alpha(i,k)` is a bijection from
`F_k times Z_b` to the rank-`k` layer.
On the `B` side we index an atom by the rank of the **complement** of its
middle `B` interval.  Thus `F_s^B`, for example, supplies the physical
rank-`(b-s)` middle deck by complementing its rank-`s` intervals.  This is
the standard complementary-factor representation and explains why all four
banks in (1.8) are indexed by `s` or `t`.

For `X` and `Y`, let their direct owners be

\[
 o_s^A(X)=(\alpha,x),\qquad o_t^B(Y)=(\delta,y),     \tag{1.9}
\]

and define the two cross-deck occurrence sets

\[
 D_0(Y)=
 \{(\beta,v):\beta\in\mathcal F_s^B,
                 I_\beta(v,t)=Y\},                  \tag{1.10}
\]

\[
 D_1(X)=
 \{(\gamma,u):\gamma\in\mathcal F_t^A,
                 I_\gamma(u,s)=X\}.                 \tag{1.11}
\]

These are multisets only across different orders: a proper interval set
occurs at most once in one cyclic order.  Write

\[
 d_0(Y)=|D_0(Y)|,\qquad d_1(X)=|D_1(X)|.             \tag{1.12}
\]

The endpoint-`0` atom `(alpha,beta)` has payload `s`, schedule
`A^sB^(b-s)`, and uses the phases whose next `L` types are all `B`.
The endpoint-`1` atom `(gamma,delta)` has payload `t`, schedule
`A^tB^(b-t)`, and uses the phases whose next `L` types are all `A`.
Rotating the second stream of an atom gives one effective relative-origin
variable

\[
 \theta^0_{\alpha\beta},\theta^1_{\gamma\delta}
 \in\mathbb Z_b.                                    \tag{1.13}
\]

Define the two fixed diagonal masks

\[
 J_0=\{p+q-s:s\le p\le b-L\}\pmod b,               \tag{1.14}
\]

\[
 J_1=\{p-t:0\le p\le t-L\}\pmod b.                \tag{1.15}
\]

They are cyclic intervals of sizes `a_0,a_1`.

### Theorem 1.1 (exact endpoint order-pair CSP)

For arbitrary choices of the four factor banks and of every variable in
(1.13), the labelled target `(X,Y)` is covered by the retained endpoint
sources if and only if the following clause is true:

\[
 \boxed{
 \begin{aligned}
 &\bigvee_{(\beta,v)\in D_0(Y)}
   \bigl[x+v-\theta^0_{\alpha\beta}\in J_0\bigr]\\
 &\qquad\vee
 \bigvee_{(\gamma,u)\in D_1(X)}
   \bigl[u+y-\theta^1_{\gamma\delta}\in J_1\bigr],
 \end{aligned}}                                      \tag{1.16}
\]

where `(alpha,x)=o_s^A(X)` and `(delta,y)=o_t^B(Y)`.
Consequently, with the four banks fixed, the optimum physical endpoint
coverage of this fixed profile over all relative origins is exactly
`P_(q,s)` minus the minimum number of unsatisfied clauses in the
`Z_b`-valued CSP (1.16).

#### Proof

Index a window start by `kb+p`, where `0<=p<b`.  In the payload-`s`
atom, the `A` interval of the upper target starts at

\[
 ks+\min(p,s),                                       \tag{1.17}
\]

while the complementary rank-`t` interval in the rotated `B` order starts
at

\[
 k(b-s)+\max(0,p-s)+b-s+q+\theta^0_{\alpha\beta}.   \tag{1.18}
\]

The sum of these coordinates is
`p+q-s+theta^0_(alpha beta)` modulo `b`.  The next `L` types are all `B`
exactly for

\[
 p=s,s+1,\ldots,b-L.                                \tag{1.19}
\]

As `k` runs through `Z_b`, the two interval coordinates run through all
`b` points of that sum diagonal, because `s` is nonzero modulo the prime
`b`.  Hence the payload-`s` atom covers `(X,Y)` exactly when `X` has its
direct coordinate `(alpha,x)`, `Y` has a cross occurrence `(beta,v)`, and
the first family of literals in (1.16) holds.

For the payload-`t` atom, the upper rank-`s` interval in `A` starts at

\[
 kt+\min(p,t),                                       \tag{1.20}
\]

and the complementary rank-`t` interval in the rotated `B` order starts at

\[
 k(b-t)+\max(0,p-t)+b-t+\theta^1_{\gamma\delta}.    \tag{1.21}
\]

Their sum is `p-t+theta^1_(gamma delta)` modulo `b`.  The next `L` types
are all `A` exactly for `p=0,...,t-L`.  Again `k` traverses the whole
diagonal.  This gives the second family of literals.  The direct factor
decks make the owners in (1.9) unique, so the two families list every
physical endpoint occurrence and no nonphysical one.  This proves (1.16)
and the optimization statement.  \(\square\)

The total cross-deck multiplicities are fixed although their distributions
depend on the factors:

\[
 \sum_Yd_0(Y)=bf_s=C_s,
 \qquad
 \sum_Xd_1(X)=bf_t=C_t.                             \tag{1.22}
\]

Thus the average degrees on the two target coordinates are reciprocal:

\[
 {1\over C_t}\sum_Yd_0(Y)=R,qquad
 {1\over C_s}\sum_Xd_1(X)=R^{-1},qquad
 R={C_s\over C_t}.                                  \tag{1.23}
\]

This reciprocal pair, together with the atom variables shared by many
clauses, is the exact nonidentical-order gate.

## 2. Independent origins still miss a positive fraction

The factor banks and all their conjugations may be chosen and correlated
arbitrarily in this section.  Conditional on those choices, make all
variables in (1.13) mutually independent and uniform in `Z_b`.

### Theorem 2.1 (factor-uniform independent-origin barrier)

The exact expected missed fraction of the fixed profile is

\[
 \begin{aligned}
 {\mathbb E Z_{q,s}\over P_{q,s}}
 &=\left[{1\over C_t}\sum_Y
       \left(1-{a_0\over b}\right)^{d_0(Y)}\right]
   \left[{1\over C_s}\sum_X
       \left(1-{a_1\over b}\right)^{d_1(X)}\right]             \tag{2.1}\\
 &\ge
 \boxed{
 \left(1-{a_0\over b}\right)^R
 \left(1-{a_1\over b}\right)^{1/R}.}                         \tag{2.2}
 \end{aligned}
\]

The lower bound holds for every deterministic choice of the factors and
their conjugations.

#### Proof

For one target `(X,Y)`, the first disjunction in (1.16) uses exactly
`d_0(Y)` distinct payload-`s` atom variables.  The second uses exactly
`d_1(X)` distinct payload-`t` atom variables.  The two payload banks are
disjoint.  A uniform variable satisfies its interval literal with
probability `a_i/b`, so independence gives

\[
 \Pr((X,Y)\text{ is missed})=
 \left(1-{a_0\over b}\right)^{d_0(Y)}
 \left(1-{a_1\over b}\right)^{d_1(X)}.             \tag{2.3}
\]

Average first over `X` and then over `Y` to obtain (2.1).  For `0<c<1`,
the function `d -> c^d` is convex.  Jensen's inequality and (1.23) give
(2.2).  \(\square\)

For the complementary profile

\[
 s={b+q\over2},\qquad t={b-q\over2},                \tag{2.4}
\]

we have `R=1`.  If `q,L=o(b)`, both `a_0/b` and `a_1/b` are
`1/2-o(1)`, so (2.2) becomes

\[
 {\mathbb E Z_{q,s}\over P_{q,s}}\ge {1\over4}-o(1). \tag{2.5}
\]

More generally, write

\[
 s={b+q\over2}+x.                                   \tag{2.6}
\]

If `q=c sqrt(b)+o(sqrt(b))`, `x=d sqrt(b)+o(sqrt(b))`, and `L=o(b)`,
the central binomial expansion gives

\[
 R=\exp(-4cd+o(1)).                                 \tag{2.7}
\]

Hence (2.2) has the positive limit lower bound

\[
 2^{-\{e^{-4cd}+e^{4cd}\}}.                         \tag{2.8}
\]

Correlating conjugations alone therefore cannot solve the endpoint gate.
The phase variables themselves must be deliberately anti-aligned across
the two payload banks.  Theorem 2.1 is an expectation theorem; it does not
exclude a successful deterministic CSP assignment.

### Theorem 2.2 (deterministic zero-coordinate row/column obstruction)

Put

\[
 p_0={a_0\over b},\qquad p_1={a_1\over b}.           \tag{2.9}
\]

For every deterministic choice of the four factor banks, all conjugations,
and all phase origins, the unrestricted CSP (1.16) has missed fraction

\[
 \boxed{
 {Z_{q,s}\over P_{q,s}}\ge
 \begin{cases}
 (1-R^{-1})(1-p_0R)_+,&R\ge1,\\[3pt]
 (1-R)(1-p_1/R)_+,&R\le1.
 \end{cases}}                                        \tag{2.10}
\]

Equivalently, the exact integer lower bounds before normalization are

\[
 Z_{q,s}\ge
 \begin{cases}
 (C_s-C_t)(C_t-a_0f_s)_+,&C_s\ge C_t,\\[3pt]
 (C_t-C_s)(C_s-a_1f_t)_+,&C_s\le C_t.
 \end{cases}                                         \tag{2.11}
\]

#### Proof

Suppose first that `C_s>=C_t`.  The cross-deck family
`F_t^A` contains exactly

\[
 bf_t=C_t                                               \tag{2.12}
\]

rank-`s` interval occurrences in total.  Consequently at most `C_t` of the
`C_s` sets `X` have `d_1(X)>0`; at least `C_s-C_t` rows have
`d_1(X)=0`.

Fix one such row `X`, with direct owner `(alpha,x)` in `F_s^A`.  The second
disjunction in (1.16) is empty.  For one `beta in F_s^B`, the single
variable `theta^0_(alpha beta)` can satisfy the first literal at at most
`a_0` of the `b` rank-`t` interval coordinates of `beta`, because `J_0`
has size `a_0`.  There are `f_s` choices of `beta`.  Hence, regardless of
all collisions and origin choices, the endpoint-`0` bank covers at most

\[
 a_0f_s                                                \tag{2.13}
\]

of the `C_t` targets in this row.  Every one of the at least `C_s-C_t`
zero rows therefore misses at least `(C_t-a_0f_s)_+` targets.  This proves
the first line of (2.11).

If `C_s<=C_t`, interchange the two endpoint banks.  There are at least
`C_t-C_s` columns `Y` with `d_0(Y)=0`, and the endpoint-`1` atoms with
fixed direct owner `delta` cover at most `a_1f_t` targets in one such
column.  This proves the second line of (2.11).  Dividing by `C_sC_t` and
using `R=C_s/C_t` gives (2.10).  \(\square\)

The obstruction is zero on the complementary diagonal `R=1`, as it must be.
It is positive on a whole punctured neighborhood of that diagonal.  Define

\[
 g(R)=
 \begin{cases}
 (1-R)\left(1-{1\over2R}\right)_+,&0<R\le1,\\[5pt]
 (1-R^{-1})\left(1-{R\over2}\right)_+,&R\ge1.
 \end{cases}                                         \tag{2.14}
\]

Thus `g(R)>0` exactly for `1/2<R<2` with `R!=1`.

### Corollary 2.3 (linear mesoscopic no-go for the one-copy clustered bank)

Let

\[
 {q\over\sqrt b}\longrightarrow c\in(0,\infty),
 \qquad q\le L=o(b).                                 \tag{2.15}
\]

For every choice of the tight-cycle factor banks, conjugations, and origins,
the endpoint sources alone miss

\[
 \boxed{
 \sum_s Z_{q,s}\ge(\Gamma_c+o(1))W_b,}              \tag{2.16}
\]

where

\[
 \Gamma_c={2e^{-c^2}\over\sqrt\pi}
 \int_{-\infty}^{\infty}e^{-4u^2}
        g(e^{-4cu})\,\mathrm du>0.                   \tag{2.17}
\]

In particular this holds for the strongest endpoint choice `L=q`.  At that
choice, all interior clustered phase types together have only

\[
 {2(q-1)\over b}W_b+e^{-\Omega(b)}W_b=o(W_b)         \tag{2.18}
\]

occurrences.  Therefore even after all interior phases are restored, the
complete one-copy clustered product-factor bank misses

\[
 \boxed{(\Gamma_c-o(1))W_b}                          \tag{2.19}
\]

rank-`(b+q)` targets.

#### Proof

Write `s=(b+q)/2+x` and `x=d sqrt(b)`.  Uniformly for bounded `d`, the
central binomial estimates give

\[
 R=e^{-4cd+o(1)},\qquad
 {P_{q,s}\over W_b}
 ={2+o(1)\over\sqrt{\pi b}}
   e^{-c^2-4d^2}.                                    \tag{2.20}
\]

Also `p_0,p_1->1/2` uniformly on this range by (2.15).  Theorem 2.2 and a
mesh-`1/sqrt(b)` Riemann sum therefore give (2.16)--(2.17).  The integrand
is nonnegative and is strictly positive, for example, whenever
`0<|4cd|<log 2`; hence `Gamma_c>0`.

It remains to count the phases omitted from the endpoint CSP.  For every
central payload rank `r` and every `1<=z<=q-1`, the clustered word
`A^rB^(b-r)` has exactly two phases at which the next `q` types contain
`z` letters of type `A`.  The rank-`r` atom bank contains `C_r^2/b^2`
atoms, and one phase in one atom contains `b` counter points.  Hence all
interior types have at most

\[
 \sum_r\sum_{z=1}^{q-1}{2C_r^2\over b}
 \le {2(q-1)\over b}\sum_rC_r^2
 ={2(q-1)\over b}W_b                                \tag{2.21}
\]

occurrences.  Payload ranks outside the central quarter have total middle
mass `e^{-Omega(b)}W_b` and can be charged in full.  Each additional
occurrence covers at most one endpoint hole, so subtracting (2.18) from
(2.16) proves (2.19).  \(\square\)

Corollary 2.3 is scoped to the one-copy clustered product-factor route:
one physical atom for every pair of factor orders, with the nested type word
`A^rB^(b-r)`.  It does not obstruct a different factor/atom geometry,
linear duplication of the middle bank, or a linear-scale rerouting of
existing occurrences.  Directly appending a linear duplicate bank would of
course forfeit coefficient one.  The corollary does show that the separate
endpoint-token matchings cannot be lifted to this physical order bank with
only `o(W_b)` repairs.

## 3. Arbitrary one-to-one nonidentical blocks retain the cardinality barrier

Let

\[
 \mathcal A_s=\mathcal F_s^A\times\mathcal F_s^B,
 \qquad
 \mathcal A_t=\mathcal F_t^A\times\mathcal F_t^B                 \tag{3.1}
\]

be the two physical atom banks.  Their sizes are `f_s^2` and `f_t^2`.
Call a construction a **one-to-one two-atom block coupling** if it chooses
a matching between subsets of `A_s` and `A_t`, uses no atom in two blocks,
and obtains all of its fixed-profile endpoint targets from the two atoms in
its chosen blocks.  Inside a block the two cyclic-order pairs may be
completely nonidentical, their labels and coordinates may be correlated
arbitrarily, and their origins and retained occurrences may be chosen
adversarially.

### Theorem 3.1 (nonidentical one-to-one pairing barrier)

Every one-to-one two-atom block coupling covers at most

\[
 \boxed{
 \left(1-{q+2L-2\over b}\right)
 \min(C_s,C_t)^2}                                    \tag{3.2}
\]

distinct targets in the profile.  Consequently its missed fraction obeys

\[
 \boxed{
 {Z_{q,s}\over P_{q,s}}
 \ge
 1-\left(1-{q+2L-2\over b}\right)e^{-|\log R|}.}     \tag{3.3}
\]

#### Proof

One payload-`s` atom has exactly `a_0b` retained endpoint occurrences and
one payload-`t` atom has exactly `a_1b`.  Hence one paired block has at most

\[
 (a_0+a_1)b=(b-q-2L+2)b                              \tag{3.4}
\]

distinct covered targets, regardless of how its order coordinates are
identified.  The number of blocks is at most

\[
 \min(f_s^2,f_t^2)={\min(C_s,C_t)^2\over b^2}.       \tag{3.5}
\]

Multiplying (3.4) and (3.5) proves (3.2).  Finally

\[
 {\min(C_s,C_t)^2\over C_sC_t}
 ={\min(C_s,C_t)\over\max(C_s,C_t)}=e^{-|\log R|},   \tag{3.6}
\]

which proves (3.3).  \(\square\)

For the scaling in (2.6)--(2.7), with `c d != 0` and `L=o(b)`, this gives

\[
 {Z_{q,s}\over P_{q,s}}
 \ge 1-e^{-4|cd|}+o(1).                              \tag{3.7}
\]

Thus even ideal nonidentical coordinate maps inside one-to-one blocks cannot
have `o(P_(q,s))` misses on a genuinely off-complementary central profile.

The aggregate consequence is exactly the old cardinality obstruction but
with a strictly larger scope.  The corresponding full formal sum of the
weaker pointwise term in (3.3) is

\[
 L_{b,q}=\sum_{s=q}^b
 \left(C_sC_{s-q}-\min(C_s,C_{s-q})^2\right).         \tag{3.8}
\]

If `m=floor((b-q)/2)`, Vandermonde, symmetry, and unimodality give

\[
 L_{b,q}={2b\choose b+q}-A_{b,q},                    \tag{3.9}
\]

where

\[
 A_{b,q}=\begin{cases}
 2\displaystyle\sum_{j=0}^{m}{b\choose j}^2,
       &b-q\text{ odd},\\[5pt]
 2\displaystyle\sum_{j=0}^{m-1}{b\choose j}^2+{b\choose m}^2,
       &b-q\text{ even}.
 \end{cases}                                         \tag{3.10}
\]

Deleting profiles outside the central quarter changes this by only
`exp(-Omega(b))W_b` for `q=O(sqrt(b))`.  When `q<=L=o(b)`, every
central-quarter profile satisfies (1.1) for all sufficiently large `b`.
Thus the actual central-profile miss of a one-to-one block route is at least
`L_(b,q)-exp(-Omega(b))W_b`.  The hypergeometric central limit theorem
therefore gives, when `q/sqrt(b)->c>0`,

\[
 {L_{b,q}\over W_b}\longrightarrow
 e^{-c^2}-\operatorname{erfc}(c)>0.                  \tag{3.11}
\]

Uniformly for `q=o(sqrt(b))`,

\[
 {L_{b,q}\over W_b}
 ={2q\over\sqrt{\pi b}}+
 O\left({q^2\over b}+{1\over\sqrt b}\right).       \tag{3.12}
\]

Thus for `1<<Q<<sqrt(b)`, every one-to-one two-atom block route has
aggregate miss at least

\[
 \left({1+o(1)\over\sqrt\pi}\right)
 {Q^2\over\sqrt b}W_b.                               \tag{3.13}
\]

The proof of (3.9)--(3.13) is the same elementary calculation visible in
the displays: `C_s>=C_(s-q)` precisely on one side of `(b+q)/2`, reflection
turns the minimum-square sum into (3.10), and the probability weights
`C_j^2/W_b` are hypergeometric with variance `b^2/[4(2b-1)]`.

Theorem 3.1 does not apply to the full CSP (1.16), which uses every atom in
the larger bank without assigning it a unique mate.  That many-to-many
one-sided-surplus use is exactly the surviving possibility.

## 4. Full interval-coordinate isomorphisms are dihedral

The next statement is deterministic and does not use factor existence.

### Theorem 4.1 (cyclic interval-deck rigidity)

Let `b>=5` be odd, let `2<=k<=b-2`, and let `alpha,gamma` be cyclic orders
of the same labelled `b`-set.  Suppose a bijection `pi:Z_b->Z_b` satisfies

\[
 I_\alpha(i,k)=I_\gamma(\pi(i),k)
 \quad\text{for every }i\in\mathbb Z_b.              \tag{4.1}
\]

Then `alpha` and `gamma` have the same underlying undirected Hamilton cycle.
After choosing coordinate origins,

\[
 \pi(i)=\varepsilon i+c,qquad
 \varepsilon\in\{1,-1\}.                            \tag{4.2}
\]

In particular a full labelled interval-coordinate isomorphism is only a
rotation or reversal of the same cyclic order.

#### Proof

Complementing every `k`-interval reduces the problem to

\[
 m=\min(k,b-k)\le {b-1\over2},\qquad m\ge2.          \tag{4.3}
\]

From the unordered deck of all `m`-intervals, define `N(x,y)` to be the
number of deck members containing both labels `x,y`.  If their cyclic
distance is `d`, then

\[
 N(x,y)=\max(0,m-d)+\max(0,m-(b-d)).                 \tag{4.4}
\]

Because `m<b/2`, this equals `m-1` precisely when `x,y` are adjacent in
the cycle.  Thus the interval deck reconstructs every undirected cycle edge.
Equation (4.1) says the two decks agree, so the two cycles have the same edge
set.  An undirected cycle has only its two traversal orientations, up to
rotation.  Since all proper interval sets in one cycle are distinct, their
coordinate bijection is the corresponding affine map (4.2).  \(\square\)

There is also a two-sided phase consequence.  Suppose coordinate maps on
the `A` and `B` orders preserve all sum diagonals, in the sense that
`pi_A(i)+pi_B(j)` depends only on `i+j`.  By (4.2), write their signs as
`epsilon_A,epsilon_B`.  Replacing `(i,j)` by `(i+1,j-1)` shows

\[
 \varepsilon_A=\varepsilon_B.                       \tag{4.5}
\]

Hence a full two-sided interval-coordinate isomorphism compatible with the
phase diagonals is a simultaneous rotation, or a simultaneous reversal, of
the same two underlying cycles.  After reversals are identified in the
usual unoriented cycle convention, this is literal common-order alignment.

This rigidity theorem concerns a **full same-target coordinate
identification**.  It does not rule out partial coordinate overlap or the
many-to-many CSP.

## 5. Adjacent swaps give cheap genuinely nonidentical seams

### Lemma 5.1 (exact adjacent-swap overlap)

Let `gamma` be obtained from `alpha` by swapping two cyclically adjacent
positions.  For every `2<=k<=b-2`,

\[
 \left|
 \{I_\alpha(i,k):i\in\mathbb Z_b\}
 \cap
 \{I_\gamma(i,k):i\in\mathbb Z_b\}
 \right|=b-2.                                        \tag{5.1}
\]

Moreover the `b-2` common sets occur at the same coordinates.

#### Proof

A length-`k` coordinate window changes under the swap exactly when it
contains one of the two exchanged labels but not the other.  Exactly two
cyclic windows have this property.  All other `b-2` coordinate sets are
unchanged.  Put the exchanged positions at `0,1`.  The two changed old sets
use respectively the predecessor positions
`b-k+1,...,b-1` and the successor positions `2,...,k`; replacing the one
exchanged label cannot turn either new set into the other old set because
the former position set contains `b-1` and the latter does not.  Nor can a
changed set equal an unchanged one, since that would duplicate a set inside
one proper interval deck.  Hence there are exactly `b-2` common sets.
\(\square\)

A sequence of `d` adjacent swaps therefore changes at most `2d` coordinate
windows at any fixed nontrivial rank.

### Theorem 5.2 (partial nonidentical two-atom seam)

Consider one payload-`s` atom `(alpha,beta)` and one payload-`t` atom
`(gamma,delta)`.  Suppose `gamma` is obtained from `alpha` by `d_A`
adjacent swaps and `delta` from `beta` by `d_B` adjacent swaps.  There are
relative origins for the two atoms whose retained endpoint targets have a
labelled-distinct union of size at least

\[
 \boxed{
 \bigl[a_0+a_1-2d_A-2d_B\bigr]_+\,b.}              \tag{5.2}
\]

In particular, if `q+L+d_A+d_B=o(b)`, the two genuinely nonidentical atoms
cover `(1-o(1))b^2` distinct targets in their coordinate block.

#### Proof

By the preceding lemma and a union bound over the swaps, at least
`b-2d_A` rank-`s` coordinates agree between `alpha,gamma`, and at least
`b-2d_B` rank-`t` coordinates agree between `beta,delta`.

The masks `J_0,J_1` are cyclic intervals and their total size is at most
`b` by (1.4).  Translate them by the two freely chosen relative origins so
that they are disjoint.  On the full coordinate torus, their sum diagonals
then contain exactly

\[
 (a_0+a_1)b                                           \tag{5.3}
\]

points.  Restrict to the common rank-`s` rows and common rank-`t` columns.
Deleting the exceptional rows and columns removes at most

\[
 (2d_A+2d_B)b                                        \tag{5.4}
\]

points.  On every remaining point, both orders assign the same labelled
pair `(X,Y)`, and the disjoint masks ensure that at most one endpoint atom
claims it.  Direct interval coordinates are injective, so all retained
targets are distinct.  Subtracting (5.4) from (5.3) proves (5.2).
\(\square\)

Theorem 5.2 proves that replacing literal equality by controlled partial
interval overlap is locally meaningful.  Theorem 3.1 proves at the same
time that pairing such excellent blocks one-to-one cannot handle unequal
factor-bank sizes.  Theorem 2.2 further proves that even distributing the
coordinates many-to-many within the same one-copy endpoint bank leaves a
linear mesoscopic deficit.  Cheap local seams can therefore help only after
the global atom/factor geometry is changed or a linear external repair
mechanism is supplied.

## 6. Exact remaining gate and audit

The note separates the fixed-profile problem into five levels.

1. The unrestricted endpoint order problem is exactly the cyclic-interval
   CSP (1.16).
2. That full CSP has the deterministic zero-coordinate lower bound (2.10),
   which becomes `Omega_c(W_b)` at one mesoscopic offset; the clustered
   interior palette is too small to repair it (Corollary 2.3).
3. Full orderwise coordinate isomorphisms add nothing beyond dihedral common
   orders (Theorem 4.1).
4. Partial nonidentical seams can be almost perfect inside one atom block
   (Theorem 5.2).
5. Any one-to-one assembly of those blocks retains the same bank-size loss
   as literal common-order overlap (Theorem 3.1).

Thus the one-copy clustered product-factor route cannot be the missing
coefficient-one lift, even with optimally correlated nonidentical orders and
origins.  A surviving construction must change the type schedule or the
global factor/atom geometry, or reroute a linear fraction of the existing
atoms without paying linear extra length.  Separate token matchings do not
provide any of these.

The H100 audit
`scratch/audit_nonidentical_endpoint_order_csp_20260821.py` performs the
following finite checks.

- For five `(b,q,s,L)` cases with `b=5,7`, including independently
  conjugated neighboring-rank factors, it directly enumerates every product
  word and verifies equality with the CSP coverage set (1.16).
- In three asymmetric `b=7` cases it checks the zero cross-coordinate counts,
  the exact row/column capacities used in (2.11), and the resulting
  deterministic lower bound against direct physical coverage.
- For every cyclic order with a fixed first label at `b=5,7` and every
  `2<=k<=b-2`, it verifies deck rigidity and the exact `b-2` adjacent-swap
  overlap.
- At `b=7,11` it constructs the two nonidentical atoms in Theorem 5.2,
  chooses disjoint phase masks, and checks the certified labelled target
  subset against direct word enumeration.
- It exhaustively checks the two-sided sign condition (4.5) for
  `b=5,7,11`.

These computations audit the indexing and finite identities.  The proofs
above are independent of them.
