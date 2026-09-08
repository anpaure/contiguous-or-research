# Fixed-shell safe-order degrees, the complete-orbit fractional factor, and a rank-one no-go

**Date:** 2026-08-14  
**Status:** unconditional exact enumeration and fractional theorem.  Every
short pure-rail shell retains almost all cyclic orders after the protected
transversal lift is forbidden.  The unrestricted complete orbit has an
exact owner/lower fractional perfect matching with all pair codegrees
explicit.  However exact point roles do not imply even fractional named
coverage for a fixed shell bank, and the ordering dual cannot uncross to
rank-one point weights.  Integral ordering remains open.

## 0. One shell

Put

\[
 k=2p+1,qquad R=p+1,qquad c=R-q,qquad
 \mathcal O={ [k]\choose R},qquad
 \mathcal L={ [k]\choose {R-1}}.                     \tag{0.1}
\]

Fix a shell

\[
                         (C,T),qquad
 |C|=c,quad |T|=N,quad C\cap T=\varnothing,quad N>2q. \tag{0.2}
\]

Let `Omega(T)` be the `(N-1)!` oriented cyclic orders of `T`, modulo
rotation.  An order `sigma` contributes

\[
 E^+(\sigma)=\{C\cup I_i^q(\sigma):i\in\mathbb Z_N\}, \tag{0.3}
\]

\[
 E^-(\sigma)=\{C\cup I_i^{q-1}(\sigma):i\in\mathbb Z_N\}. \tag{0.4}
\]

Every set in these two decks is distinct.

## 1. Exact fixed-shell degrees and codegrees

For a petal \(Q\subseteq T\), \(|Q|=q\), put \(A=C\cup Q\).  For
\(S\subseteq T\), \(|S|=q-1\), put \(L=C\cup S\).

### Theorem 1.1 (one-vertex degrees)

In the order hypergraph of this one token,

\[
 \deg(A)=q!(N-q)!,                                    \tag{1.1}
\]

\[
 \deg(L)=(q-1)!(N-q+1)!,                             \tag{1.2}
\]

and the token has degree `(N-1)!`.  Ineligible owners or lower sets have
degree zero.

#### Proof

Double-count order/window pairs.  Across all `(N-1)!` cyclic orders there
are `N` windows of a given width.  Symmetry among the corresponding subsets
gives

\[
 {(N-1)!N\over {N\choose q}}=q!(N-q)!
\]

and its `(q-1)` analogue. \(\square\)

For two distinct `q`-petals with intersection size `q-delta`, define

\[
 \gamma_q(\delta)=
 \begin{cases}
 2(q-\delta)!(\delta!)^2(N-q-\delta)!,&1\le\delta<q,\\
 (N-2q+1)(q!)^2(N-2q)!,&\delta=q.
 \end{cases}                                         \tag{1.3}
\]

For two distinct `(q-1)`-petals with intersection size `q-1-delta`, define

\[
 \gamma_{q-1}(\delta)=
 \begin{cases}
 2(q-1-\delta)!(\delta!)^2(N-q+1-\delta)!,
                       &1\le\delta<q-1,\\
 (N-2q+3)((q-1)!)^2(N-2q+2)!,&\delta=q-1.
 \end{cases}                                         \tag{1.4}
\]

For a `q`-petal `Q` and a `(q-1)`-petal `S`, put \(j=|Q\cap S|\) and

\[
 a_j=\begin{cases}N-2q+2,&j=0,\\2,&1\le j\le q-1,
 \end{cases}                                         \tag{1.5}
\]

\[
 \kappa(j)=a_jj!(q-j)!(q-1-j)!(N-2q+1+j)!.          \tag{1.6}
\]

### Theorem 1.2 (all pair codegrees)

The owner--owner, lower--lower, and owner--lower codegrees inside one shell
are respectively

\[
 \boxed{\gamma_q(\delta),\qquad
        \gamma_{q-1}(\delta),\qquad
        \kappa(j).}                                   \tag{1.7}
\]

In particular, if `L subset A`, then

\[
                         \deg(A,L)=2(q-1)!(N-q)!,      \tag{1.8}
\]

and therefore

\[
                         {\deg(A,L)\over\deg(A)}={2\over q}.     \tag{1.9}
\]

#### Proof

Fix labelled positions on a cycle.  Two equal-length arcs with overlap
`q-delta` have two relative placements when `delta<q`; disjoint arcs have
`N-2q+1` placements.  Assign labels independently to the overlap, two
differences, and exterior.  This gives `(1.3)`; `(1.4)` is identical with
width `q-1`.

A `q`-arc and `(q-1)`-arc with overlap `j>0` have two relative placements;
if disjoint they have `N-2q+2`.  The same four-region assignment gives
`(1.6)`.  At `j=q-1`, equation `(1.8)` follows. \(\square\)

These formulas show why token partiteness does not remove the large local
owner--facet correlation: conditional on an owner window, each of its
`q` petal facets is an endpoint facet with probability `2/q`.

## 2. Every fixed shell has many protected-safe orders

Let `Z` be the `2^p` transversal lower shore and `Y` the owner shore of
the transversal lift.  Call an order safe when

\[
                         E^+(\sigma)\cap Y=\varnothing,
 \qquad                  E^-(\sigma)\cap Z=\varnothing.          \tag{2.1}
\]

For the fixed shell, let `f^+` and `f^-` be the numbers of eligible
protected owners and lower sets.

### Lemma 2.1 (uniform protected eligibility bounds)

For every shell,

\[
                         f^-\le2^{q-1},               \tag{2.2}
\]

\[
                         f^+\le(2c+q-1)2^{q-2}.       \tag{2.3}
\]

#### Proof

If `C` is contained in a transversal, it fixes one endpoint in each of `c`
different pairs.  The remaining `p-c=q-1` pairs have at most two choices
each, proving `(2.2)`.

If `C` is contained in a lifted owner, it omits `z` and has at most one
double pair.  With one double pair, at most `q` missing singleton pairs give
`2^q` completions.  With no double pair, the unique final double can be one
of the `c` occupied pairs, leaving `q-1` binary singleton choices, or one of
the `q-1` empty pairs, leaving `q-2` binary choices.  The latter total is

\[
 c2^{q-1}+(q-1)2^{q-2}=(2c+q-1)2^{q-2},              \tag{2.4}
\]

which also dominates `2^q` in the stated central range.  Extra restrictions
from `T` can only reduce the count. \(\square\)

### Theorem 2.2 (safe-token degree)

Every fixed shell has at least

\[
 \boxed{
 |\Omega^{\rm safe}(C,T)|
 \ge(N-1)!(1-\varepsilon_{p,q,N}),}                   \tag{2.5}
\]

where

\[
 \varepsilon_{p,q,N}=
 (2c+q-1)2^{q-2}{N\over{N\choose q}}
 +2^{q-1}{N\over{N\choose {q-1}}}.                   \tag{2.6}
\]

For `N in {2q+2,2q+3}` and central `p=Theta(q^2)`,

\[
                         \varepsilon_{p,q,N}
 =O(pq^{3/2}2^{-q})=e^{-\Omega(q)}.                  \tag{2.7}
\]

Thus every token in the nonuniform protected role construction has a
nonempty safe order set for all sufficiently large central parameters.

#### Proof

One eligible protected owner occurs in a uniform cyclic order with
probability `N/binom(N,q)`; one eligible protected lower set has probability
`N/binom(N,q-1)`.  Apply the union bound and Lemma 2.1.  The central estimate
uses the usual central-binomial asymptotics. \(\square\)

Safety is therefore not the first fractional obstruction.  Named eligibility
and simultaneous load are.

## 3. The unrestricted complete-orbit fractional factor

Now let `H_N` contain every parameterized ordered shell `(C,T,sigma)` of
period `N`, with one hyperedge consisting of its `N` owners and `N` lower
sets.  Tokens are not included in this complete orbit.

### Theorem 3.1 (exact degree and fractional factor)

The two shores have the same common degree

\[
 \boxed{
 D_N={R!(R-1)!\over c!(R-1-N+q)!}.}                   \tag{3.1}

\]

Weight `1/D_N` on every parameterized rail.  This is an exact fractional
perfect matching on \(\mathcal O\mathbin{\dot\cup}\mathcal L\).

#### Proof

For an owner `A`, choose `C subset A` in `binom(R,c)` ways, choose the
other `N-q` support points outside `A`, and use `(1.1)`:

\[
 \deg(A)={R\choose c}{R-1\choose {N-q}}q!(N-q)!=D_N. \tag{3.2}
\]

For a lower set, the analogous count is

\[
 {R-1\choose c}{R\choose {N-q+1}}
 (q-1)!(N-q+1)!=D_N.                                 \tag{3.3}
\]

Uniform reciprocal degree therefore gives every vertex load one. \(\square\)

### Theorem 3.2 (complete-orbit codegrees)

For owners `A,B` with \(|A\cap B|=R-\delta\),

\[
 {\deg(A,B)\over D_N}=
 \begin{cases}
 \displaystyle {2\over {R\choose\delta}{R-1\choose\delta}},
                   &1\le\delta<q,\\[2mm]
 \displaystyle {N-2q+1\over {R\choose q}{R-1\choose q}},
                   &\delta=q,\\[2mm]
 0,&\delta>q.
 \end{cases}                                         \tag{3.4}
\]

For lower sets `L,M` with \(|L\cap M|=R-1-\delta\),

\[
 {\deg(L,M)\over D_N}=
 \begin{cases}
 \displaystyle {2\over {R-1\choose\delta}{R\choose\delta}},
                   &1\le\delta<q-1,\\[2mm]
 \displaystyle {N-2q+3\over {R-1\choose {q-1}}{R\choose {q-1}}},
                   &\delta=q-1,\\[2mm]
 0,&\delta>q-1.
 \end{cases}                                         \tag{3.5}
\]

For an owner `A` and lower set `L`, put

\[
                         j=|A\cap L|-c.               \tag{3.6}
\]

When `0<=j<=q-1`,

\[
 \boxed{
 \deg(A,L)=
 {c+j\choose c}
 {c+j\choose {N-2q+1+j}}
 \kappa(j),}                                         \tag{3.7}
\]

and the codegree is zero otherwise.  In particular, for every incidence
`L subset A`,

\[
                         \deg(A,L)={2D_N\over R}.      \tag{3.8}
\]

#### Proof

The same interval-position count as Theorem 1.2, followed by choosing the
common core and the unused support points, gives all three formulas.  For
`(3.7)`, \(|A\cap L|=c+j\), the exterior of \(A\cup L\) also has size `c+j`,
and the support needs `N-2q+1+j` points there. \(\square\)

This is an exact fractional theorem, not a protected or fixed-shell result.
After removing `Y,Z` and freezing the nonuniform shell bank, neither the
degrees nor the uniform fractional weights remain exact.

## 4. Point roles do not imply named fractional coverage

The cyclic orbit-block role construction chooses a regular `k`-cycle
`tau` and, from one base shell, all `k` translates

\[
                         (\tau^rC,\tau^rT),qquad r\in\mathbb Z_k. \tag{4.1}
\]

Every such block has perfectly uniform point roles, independently of the
base shell.

### Theorem 4.1 (rank-one dual obstruction)

Repeat only one base orbit block for each of the two periods
`2q+2,2q+3`, with multiplicities giving total period `W`.  The resulting
shell multiset satisfies all exact owner and lower point-role equations.
Yet the number of named owners eligible in any shell is at most

\[
 k\left({2q+2\choose q}+{2q+3\choose q}ight),       \tag{4.2}

\]

and the analogous lower bound uses `(q-1)` in place of `q`.  In the central
regime these quantities are `exp(O(q))=o(W)`.  Hence almost every owner and
lower set has degree zero in the fixed-shell order hypergraph, so no
fractional named-order factor exists.

Consequently the support-function dual for fixed-shell ordering cannot be
uncrossed to weights which are additive over ground points.

#### Proof

One shell has exactly `binom(N,q)` eligible owners and `binom(N,q-1)`
eligible lower sets; repetition creates no new eligible named vertices.
The `k` translates give `(4.2)`.  Exact point roles follow from cyclic-orbit
regularity.

For any point-additive weights, the load of one shell is independent of its
cyclic order and is determined by the already exact point-role equations.
Such dual tests all pass.  Give weight one instead to a named owner outside
the eligibility union and zero elsewhere.  The target side of the
fractional dual is one while every shell maximum is zero.  This is a strict
higher-order separating weight. \(\square\)

Thus the positive role theorem must be supplemented by a named-eligibility
spread condition before fractional order selection can even be posed
robustly.

## 5. Why there is no Birkhoff shortcut

For `q=2`, the owner petals of one shell are exactly the edges of a
Hamilton cycle on `T`, while the lower petal deck is all singleton points of
`T`, independent of order.  The convex hull of the owner projections is
therefore the symmetric travelling-salesperson polytope, not a bipartite
matching polytope.  Subtour inequalities are genuine facets.

For larger `q`, every order choice still carries its underlying Hamilton
cycle on the toggle labels, so token partiteness selects one TSP vertex per
token; it does not turn the order polytope into a Birkhoff polytope.  A
Latin or permutation-matrix formulation without cyclic-connectivity rows is
therefore incomplete.

## 6. The alternating-incidence configuration quotient

One may try to remove the large incident owner--facet codegree by treating
the complete alternating rail

\[
 L_{i-1},A_i,L_i\qquad(i\in\mathbb Z_N)               \tag{6.1}
\]

as one internal configuration.  This is legitimate bookkeeping: every
owner occurrence carries its two incident lower occurrences, so those
pairs need not be tested as external hypergraph codegrees.

The remaining normalized pair codegrees in the complete orbit are given by
`(3.4)--(3.7)` after excluding `L subset A`.  Their maximum is

\[
 \boxed{
 \max\left\{
 {2\over R(R-1)},
 \max_{0\le j\le q-2}{\deg(A,L)_j\over D_N}
 \right\}.}                                           \tag{6.2}
\]

For central `R~k/2`, `q=o(R)`, and `N=2q+O(1)`, the largest nonincident
mixed term occurs at `j=q-2` and is

\[
                         {4\over R(R-1)^2}=O(k^{-3}),              \tag{6.3}
\]

while the same-shore distance-one terms are exactly

\[
                         {2\over R(R-1)}=Theta(k^{-2}). \tag{6.4}
\]

Hence the configuration quotient restores the owner-only normalized
codegree scale `Theta(k^(-2))`.  With configuration rank `Theta(N)`, its
squared-rank collision parameter is

\[
                         O(N^2/k^2)=O(k^{-1})          \tag{6.5}

\]

in the central regime.

This is a useful method reduction, but not an application of an existing
`A`-perfect matching theorem.  The available Delcourt--Postle hypotheses
are stated for bounded edge rank fixed independently of the degree limit,
whereas here `N=Theta(sqrt k)` grows.  Moreover, a configuration matching
still has to cover every owner and every lower occurrence once; moving the
two incident facets inside the configuration does not by itself supply the
required partite degree surplus or an absorber for the residual named leave.

### Theorem 6.1 (exact quotient verdict)

After contracting the two incident owner--facet relations inside each rail
configuration:

1. every remaining complete-orbit normalized pair codegree is `O(k^(-2))`;
2. the growing-rank collision parameter tends to zero centrally; but
3. no presently quoted fixed-rank Delcourt--Postle `A`-perfect theorem
   applies uniformly to this growing-rank configuration hypergraph.

Thus the large `2/R` codegree is a quotient artefact, not the final method
obstruction.  The remaining rigorous gate is a **growing-rank**
configuration-matching theorem plus protected fixed-bank degree spread.

#### Proof

Same-shore codegrees follow directly from `(3.4)--(3.5)` and are maximized
at distance one.  For a nonincident mixed pair write `j=q-s`, `s>=2`.
Equations `(3.1),(3.7)` simplify to

\[
 {\deg(A,L)\over D_N}
 ={2s!(s-1)!(R-s)!^2\over R!(R-1)!}.                  \tag{6.6}
\]

Successive terms have ratio `s(s+1)/(R-s)^2<1` in the stated range, so
`s=2` is maximal and gives `(6.3)`; the disjoint case is smaller as well.
Equations `(6.4)--(6.5)` follow.  The quantifier mismatch with a fixed-rank
theorem is literal and no diagonal extension is inferred.
\(\square\)

## 7. The dual max-order problem is already TSP-hard

Take `q=2`.  Lower petals are singleton toggle points, so arbitrary lower
weights contribute a constant independent of order.  Give an arbitrary
weight `w_{uv}` to owner `C+{u,v}`.  Maximizing the owner/lower weight of a
cyclic order becomes

\[
                         \max_\sigma\sum_iw_{x_ix_{i+1}},         \tag{7.1}

\]

the maximum-weight Hamilton cycle problem on the complete graph with edge
weights `w`.  Deciding whether `(7.1)` reaches a specified threshold is
NP-complete, already for `0/1` weights by the Hamilton-cycle problem.

### Corollary 7.1

The support-function maximization in the exact fractional dual cannot, for
arbitrary named weights, be reduced in polynomial time to point weights,
pairwise independent assignments, or a Birkhoff matching, unless `P=NP`.
The cyclic subtour constraints are computationally and polyhedrally real.

This complexity statement concerns arbitrary dual weights.  It does not
preclude a structural uncrossing for the special weights arising from a
future proof of the protected fractional inequalities.

## 8. Exact scope and next gate

The theorem establishes, separately:

1. exact fixed-shell unsafed degrees and every pair codegree;
2. a uniform exponentially small bound on the fraction of orders forbidden
   by the protected lift;
3. an exact unrestricted complete-orbit fractional owner/lower factor;
4. a sharp example showing exact point roles do not imply named fractional
   feasibility; and
5. a TSP-polytope obstruction to a naive Birkhoff/Latin rounding.

It does not prove safe fractional feasibility for the nonuniform shell bank
from the protected role theorem.  The precise next condition is named
eligibility spread plus the full support-function inequalities; after that,
integral rounding must retain the cyclic subtour structure and the forced
owner--facet correlations.
