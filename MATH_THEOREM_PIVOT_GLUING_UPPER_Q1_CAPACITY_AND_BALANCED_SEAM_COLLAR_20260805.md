# Pivot gluing: the exact upper-q1 capacity correction and a balanced seam collar

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional counting obstruction, unconditional local collar,
and an exact reduction of the owner/q1 part of the complementary-factor
problem.  The result corrects the overly strong requirement that all upper
targets be witnessed internally by the complementary trace components.
That requirement is impossible for a Catalan-scale bank of positive-length
pivot bridges.  The correct object is a jointly decorated factor: almost all
bridge and seam transitions must themselves carry new upper-q1 colours.
The theorem does not construct the remaining punctured ordered
four-transversal, a resident literal trace factor, or the higher upper deck.

## 1. General transition accounting

Fix a ground set of size `k`, owner rank `r`, and put

\[
             W={k\choose r},\qquad U={k\choose r+1}.
\tag{1.1}
\]

Suppose `c` nonempty ordered owner components are glued in a line by
`b=c-1` pairwise owner-disjoint bridges.  Each bridge has `s` owner windows.
Assume that component owners and bridge owners partition the rank-`r` layer.
Then the component owner set has size

\[
                         W-bs.                         \tag{1.2}
\]

Consequently the numbers of adjacent-owner transitions are

\[
\begin{aligned}
 E_{\rm comp}&=W-bs-c,\\
 E_{\rm collar}&=b(s-1)+2b=b(s+1),\\
 E_{\rm total}&=W-1.
\end{aligned}                                          \tag{1.3}
\]

Here `E_collar` includes the `s-1` internal transitions of each bridge and
its two seams.  Every rank-`r+1` interval witness contains at least two
consecutive owner windows.  Hence one adjacent-owner transition can witness
at most one upper-q1 target.

### Theorem 1.1 (upper-q1 capacity identity)

If all `U` upper-q1 targets are covered, the collar transitions must supply
at least

\[
        D_U:=U-E_{\rm comp}=U-W+bs+c                 \tag{1.4}
\]

distinct upper-q1 colours.  Call a transition **upper-q1 waste** when its
union either has rank above `r+1`, or repeats an upper-q1 colour already
assigned to another transition.  The total upper-q1 waste is at least

\[
                         R_U:=W-1-U.                  \tag{1.5}
\]

If every upper-q1 target occurs, the waste is exactly `R_U`; it is the sum
of the number of above-q1 transitions and the upper-q1 multiplicity excess.
In particular, it consists entirely of repeated q1 occurrences exactly
when every transition union has rank `r+1`.  Independently of this split,

\[
                    E_{\rm collar}-D_U=R_U.           \tag{1.6}
\]

#### Proof

There are only `E_comp` internal component adjacencies, so they witness at
most that many distinct rank-`r+1` targets.  This gives (1.4).  A path on
all `W` owners has `W-1` transitions, and at most `U` of them can be first
providers of distinct upper-q1 targets.  This proves (1.5).  If all targets
occur, exactly `U` transitions are chosen as first providers, giving the
stated exact waste decomposition.  Finally,
using `b=c-1`,

\[
\begin{aligned}
 E_{\rm collar}-D_U
 &=b(s+1)-(U-W+bs+c)\\
 &=b-c+W-U=W-1-U.
\end{aligned}
\]

This is (1.6).  \(\square\)

### Corollary 1.2 (internal upper completeness is impossible here)

If `D_U>0`, the complementary components cannot be internally upper-q1
complete, and therefore cannot be internally complete for the whole strict
upper ideal.

For the even middle layer `k=2r`, put

\[
                 C={W\over r+1},\qquad c=C.
\tag{1.7}
\]

Then `U=W-C`, and

\[
                  D_U=bs=s(C-1),\qquad R_U=C-1=b.    \tag{1.8}
\]

Thus every one of the `b` positive-length collars must supply on average
exactly `s` new upper-q1 colours, and the entire finished path has room for
only one repeat per collar.

For the odd middle layer `k=2r-1`, with the standard component count

\[
                  c={W\over2r-1},                    \tag{1.9}
\]

we have

\[
\begin{aligned}
 U&={r-1\over r+1}W,\\
 D_U&=s(c-1)+c-{2W\over r+1},\\
 R_U&={2W\over r+1}-1.                               \tag{1.10}
\end{aligned}

At the deadline scale `s=Theta(sqrt r)`, (1.10) again has `D_U>0` for all
sufficiently large `r`.

#### Proof

Substitute the displayed binomial ratios into (1.4)--(1.5).  In the even
case,

\[
 U-E_{\rm comp}=(W-C)-(W-bs-C)=bs.
\]

For odd `k`, `U/W=(r-1)/(r+1)`, which gives (1.10).  Since
`s(c-1)` is asymptotic to `sW/(2r)` whereas `2W/(r+1)=Theta(W/r)`, the
first term dominates at `s=Theta(sqrt r)`.  \(\square\)

The consequence is structural: an assumption that every upper target has
an interval lying wholly inside one complementary component cannot be the
load-bearing gluing hypothesis for a Catalan-scale positive-length pivot
bank.  The bridges and seams are not merely topology.  They carry an
asymptotically forced part of the upper palette.

## 2. A balanced literal seam collar for one pivot

Let `h>=2`, put `s=h+1`, and assume `r-h>=1`.  Choose pairwise disjoint

\[
 Q,\quad \lambda_1,\ldots,\lambda_h,\quad
       \rho_1,\ldots,\rho_h,qquad |Q|=r-h.           \tag{2.1}
\]

The pivot owners are

\[
 M_j=Q\cup\{\lambda_{j+1},\ldots,\lambda_h\}
       \cup\{\rho_1,\ldots,\rho_j\},
       \qquad0\le j\le h.                            \tag{2.2}
\]

Fix `q in Q`.  Write

\[
 L=\{\lambda_1,\ldots,\lambda_h\},\qquad
 R=\{\rho_1,\ldots,\rho_h\}.                         \tag{2.3}
\]

Define the endpoint owners

\[
 P=(Q\setminus\{q\})\cup L\cup\{\rho_1\},
 \qquad
 N=(Q\setminus\{q\})\cup R\cup\{\lambda_1\}.       \tag{2.4}
\]

These are literal trace-compatible endpoints.  Immediately before the
pivot, the order-`h` source state is

\[
       (\{\lambda_1\},\ldots,\{\lambda_h\}),          \tag{2.5}
\]

and it may be preceded by the nonempty letter
`(Q\setminus{q}) union {rho_1}`, whose owner is `P`.  Immediately after the
pivot, the state is

\[
       (\{\rho_1\},\ldots,\{\rho_h\}),                \tag{2.6}
\]

and the next nonempty letter `(Q\setminus{q}) union {lambda_1}` creates
owner `N`.

### Theorem 2.1 (one-repeat balanced pivot collar)

The owners `P,M_0,...,M_h,N` are all distinct.  Every consecutive pair is
a Johnson edge.  The `h` internal bridge upper colours are

\[
 U_j=M_{j-1}\cup M_j
 =Q\cup\{\lambda_j,\ldots,\lambda_h\}
       \cup\{\rho_1,\ldots,\rho_j\},
       \qquad1\le j\le h.                            \tag{2.7}
\]

The seam colours satisfy

\[
                  P\cup M_0=U_1,                    \tag{2.8}
\]

and

\[
                  M_h\cup N=Q\cup R\cup\{\lambda_1\}=:U_*.
\tag{2.9}
\]

The values `U_1,...,U_h,U_*` are pairwise distinct.  Hence the `h+2=s+1`
collar transitions supply exactly `s=h+1` distinct upper-q1 targets and
have exactly one repeat, namely the second occurrence of `U_1`.

Moreover all `h+2` lower-q1 colours of the collar are pairwise distinct:

\[
\begin{aligned}
 P\cap M_0&=(Q\setminus\{q\})\cup L,\\
 M_{j-1}\cap M_j
 &=Q\cup\{\lambda_{j+1},\ldots,\lambda_h\}
       \cup\{\rho_1,\ldots,\rho_{j-1}\},\\
 M_h\cap N&=(Q\setminus\{q\})\cup R.
\end{aligned}                                        \tag{2.10}
\]

#### Proof

All displayed owners have rank `r`.  The endpoint `P` contains the whole
lambda rail and misses `q`, whereas each pivot owner contains `q`; similarly
`N` contains the whole rho rail and misses `q`.  Thus neither endpoint is a
pivot owner.  They are distinct because `L` and `R` are disjoint and
`h>=2`.  Equations (2.7)--(2.9) follow by direct union.

The rho-prefix length recovers `j` in (2.7), so the `U_j` are distinct.
The only internal colour containing all of `R` is
`U_h=Q union R union {lambda_h}`.  Since `lambda_1 != lambda_h`, `U_*` is
new.  Equation (2.8) gives the unique declared repeat.

For lower colours, the two seam values omit `q`, while every internal value
contains `q`, so no seam value collides with an internal one.  The internal
values are distinguished by their rho-prefix lengths.  The two seam values
are distinct because one contains `L` and the other contains `R`.  This
proves (2.10) and the theorem.  \(\square\)

### Corollary 2.2 (the even collar ledger is locally sharp)

In the even case of (1.8), a family of `b=C-1` balanced collars has exactly
the required local multiplicity pattern: `bs` new upper-q1 occurrences and
`b` repeats.  Consequently **no further upper-q1 collision is affordable**.
The `bs` target values supplied by different collars must be globally
distinct, and every internal component transition must supply a different
target in the complementary upper palette.

This is only a local construction.  Owner-disjointness of the pivots does
not imply cross-collar disjointness of the values in (2.7)--(2.9).

### Theorem 2.3 (spread bank with the endpoint owners already protected)

Assume the sparse-marking Turan spread theorem for simple uniform regular
hypergraphs.  For every sufficiently large middle dimension, there is a
parity-appropriate Catalan number of balanced collars from Theorem 2.1 such
that all bridge owners **and both endpoint owners** are pairwise distinct.
The complete protected owner union still removes only `O(r^(-1/2))` of
every containment star rooted at rank at most `r-h-1`, and it may avoid any
independently prescribed `o(W/h)` owner bank.

#### Proof

Make a hypergraph on the rank-`r` owner layer.  Its hyperedges are the
distinct sets

\[
                    \{P,M_0,\ldots,M_h,N\}            \tag{2.11}
\]

over all labelled choices (2.1) and all `q in Q`.  Theorem 2.1 says that
every edge has exactly

\[
                         t=h+3=s+2                   \tag{2.12}
\]

vertices.  The family is nonempty and invariant under all coordinate
permutations.  Since the symmetric group is transitive on rank-`r` owners,
the simple hypergraph obtained after deduplicating (2.11) is regular.

Apply the general sparse-marking Turan theorem with uniformity `t`.  The
same test sets `mathcal O(S)` have minimum size
`binom(k-r+h+1,h+1)`, so replacing `s` by `s+2` does not change the
asymptotic spread hypothesis.  Also

\[
       {t^2\over r}\longrightarrow{\pi\over4}.        \tag{2.13}
\]

Thus `gamma=5`, followed by a sufficiently small fixed epsilon, gives more
than `W/(r+1)` collared edges in the even case because `5/6>pi/4`.  In the
odd case the required coefficient is only `pi/8`.  Take an arbitrary
submatching of the exact required size.  The forbidden-bank and star-spread
conclusions are inherited from the same theorem.  \(\square\)

Theorem 2.3 closes endpoint-owner collisions at the prospective bank stage.
It does not close upper-colour collisions: upper targets are not vertices
of the owner hypergraph (2.11).

## 2.4 An unconditional owner-and-upper disjoint Catalan bank

There is a second construction which closes the upper-colour collision row,
but does not by itself give the low-star spread of Theorem 2.3.  We first
record the harmless generalization of Theorem 2.1 which it uses.

In (2.4), the deleted core labels at the two ends may be different:
`q_- ,q_+ in Q`.  Also replace `lambda_1` at the right seam by any

\[
                    z\notin M_h,qquad z\ne\lambda_h. \tag{2.14}
\]

Thus

\[
\begin{aligned}
 P&=(Q\setminus\{q_-\})\cup L\cup\{\rho_1\},\\
 N&=(Q\setminus\{q_+\})\cup R\cup\{z\}.
\end{aligned}                                        \tag{2.15}
\]

The same proof gives the one repeated left colour `U_1` and the new right
colour

\[
                         U_*=M_h\cup\{z\}.            \tag{2.16}
\]

Indeed the only internal colour containing all of `R` is
`M_h union {lambda_h}`.  The seam intersections omit `q_-` and `q_+`,
respectively, while every internal intersection contains all of `Q`.

### Theorem 2.4 (simultaneously owner- and upper-disjoint balanced bank)

Let `k` be either `2r` or `2r-1`, let `h>=2`, `s=h+1`, and assume

\[
                         r\ge4s+8.                    \tag{2.17}
\]

Then there are at least `c-1` balanced collars, where

\[
 c=\begin{cases}
       W/(r+1),&k=2r,\\
       W/(2r-1),&k=2r-1.
    \end{cases}                                      \tag{2.18}
\]

balanced collars (2.2), (2.15) such that

1. all `s+2` owner resources `P,M_0,...,M_h,N` are pairwise distinct
   across all collars; and
2. all `s` new upper-q1 resources `U_1,...,U_h,U_*` are pairwise distinct
   across all collars.

Thus the exact parity-appropriate Catalan bridge count has an unconditional
prospectively complete owner/endpoint/upper-q1 resource packing.

#### Proof

First let `k=2r` and use the bipartite containment graph

\[
 G:\quad { [2r]\choose r}\longleftrightarrow
              { [2r]\choose r+1}.                    \tag{2.19}
\]

Its two shore degrees are `r` and `r+1`, and it has `Wr` edges.  We build
the collars greedily.  After `t` collars, delete their used owner and upper
vertices.  Since one collar uses `s+2` owners and `s` uppers, the residual
graph `G_t` has at least

\[
 |E(G_t)|\ge Wr-t\bigl((s+2)r+s(r+1)\bigr).           \tag{2.20}
\]

For

\[
             t<{W\over r+1},                         \tag{2.21}
\]

this is strictly larger than

\[
                         W(r-2s-2).                   \tag{2.22}
\]

The two shores together have fewer than `2W` vertices.  Hence `G_t` has
average degree greater than `r-2s-2`, and therefore contains a nonempty
subgraph `H_t` of minimum degree greater than

\[
                         {r-2s-2\over2}\ge s+3.       \tag{2.23}
\]

The standard last inequality uses (2.17); the subgraph follows by
repeatedly deleting vertices of degree below half the average.

It remains to find one balanced collar inside `H_t`.  Start at any owner
`M_0`.  Inductively, after

\[
 M_{j-1}=(M_0\setminus\{\lambda_1,\ldots,\lambda_{j-1}\})
             \cup\{\rho_1,\ldots,\rho_{j-1}\},       \tag{2.24}
\]

choose an available upper neighbour

\[
                         U_j=M_{j-1}\cup\{\rho_j\}   \tag{2.25}
\]

with `rho_j notin M_0`.  At most `j-1` upper neighbours add one of the
already deleted original labels, whereas `deg_H(M_(j-1))>s`; hence this is
possible and the `rho_j` are automatically fresh.

At `U_1`, choose two different available owner facets

\[
                   P=U_1\setminus\{q_-\},\qquad
                   M_1=U_1\setminus\{\lambda_1\},    \tag{2.26}
\]

with `q_-,lambda_1 in M_0`.  Only the facet deleting `rho_1` is
ineligible, and the minimum degree is at least three.  Protect `q_-` from
all later deletions.  At step `j>=2`, at most `j` available-facet labels
are inserted rho labels and at most one is `q_-`; since the degree is
greater than `s>=j+1`, choose a fresh

\[
           \lambda_j\in M_0\setminus
              \{q_-,\lambda_1,\ldots,\lambda_{j-1}\} \tag{2.27}
\]

whose facet `M_j=U_j\setminus{lambda_j}` remains in `H_t`.  This constructs
the induced Johnson geodesic through `M_h`, with

\[
 Q=M_0\setminus\{\lambda_1,\ldots,\lambda_h\}.        \tag{2.28}
\]


Choose an available upper neighbour

\[
                         U_*=M_h\cup\{z\}             \tag{2.29}
\]

with `z != lambda_h`; only one neighbour is forbidden.  At `U_*`, at most
the `h` rho labels and `z` fail to belong to `Q`.  Since
`deg_H(U_*)>s=h+1`, there is an available facet

\[
                         N=U_*\setminus\{q_+\},
                         \qquad q_+\in Q.             \tag{2.30}
\]

Equations (2.24)--(2.30) give precisely the generalized balanced collar.
All of its vertices lie in the residual graph, so they avoid every earlier
collar.  Its internal distinctness is Theorem 2.1 and (2.14)--(2.16).

The construction continues for every integer
`t<W/(r+1)-1`, proving the even assertion.

For `k=2r-1`, the owner and upper shore degrees are `r-1` and `r+1`,
and the initial edge count is `W(r-1)`.  Before
`t<W/(2r-1)` collars have been chosen, the residual edge count is greater
than

\[
 W(r-1)-{W\over2r-1}
       \bigl((s+2)(r-1)+s(r+1)\bigr)
 >W(r-s-3).                                          \tag{2.31}
\]

The two shores again have fewer than `2W` vertices, so a nonempty residual
subgraph has minimum degree greater than `(r-s-3)/2>s` under (2.17).
The identical greedy construction (2.24)--(2.30) therefore supplies the
next collar.  Iterating gives `W/(2r-1)-1` collars.  \(\square\)

### Scope split

Theorems 2.3 and 2.4 close complementary marginals:

* Theorem 2.3 gives the exact owner/endpoint bank with simultaneous low-star
  spread, conditional only on the general sparse-Turan theorem.
* Theorem 2.4 gives the exact owner/endpoint/upper-q1 bank unconditionally.

Their intersection is not automatic.  A simultaneous
owner/upper-disjoint **and** low-star-spread bank remains the precise bank
selection target for the later named lower construction.

## 3. Exact punctured ordered-four-transversal reduction

The preceding count identifies the weakest owner/q1 statement sufficient
for the even gluing architecture.

Fix `b=C-1` pairwise owner-disjoint pivot bridges and choose one balanced
collar (2.4) for each.  Let `R` be their `bs` bridge owners and let
`mathcal U_B` be the set of their `bs` **new** upper-q1 colours, counting
`U_1` only once per collar.  Suppose:

1. the endpoint owners are outside `R` and are pairwise distinct;
2. `|mathcal U_B|=bs` (cross-collar upper disjointness); and
3. no endpoint owner is prescribed both as an initial and terminal endpoint
   in an incompatible way.

Put

\[
                  V_0={ [k]\choose r}\setminus R,
 \qquad
                  \mathcal U_0={ [k]\choose r+1}
                                      \setminus\mathcal U_B.  \tag{3.1}
\]

Then

\[
 |V_0|=W-bs,qquad |\mathcal U_0|=W-C-bs=|V_0|-C.     \tag{3.2}

### Theorem 3.1 (exact complement owner/q1 target)

The owner/q1 part of the even complementary-factor problem is exactly the
following punctured ordered-four-transversal problem:

> Find a spanning linear forest `F` on `V_0` with exactly `C` path
> components, having the prescribed oriented endpoint bank, such that the
> map
> \[
>                         xy\longmapsto x\cup y       \tag{3.3}
> \]
> is a bijection from `E(F)` to `mathcal U_0`.

If such `F` exists, orient its paths according to the endpoint bank and
insert the balanced collars between the paired path ends.  The resulting
owner path uses every rank-`r` owner once and every rank-`r+1` target at
least once, with total multiplicity excess exactly `C-1`.

Conversely, any gluing of these fixed balanced collars which covers every
upper-q1 target and has no multiplicity excess beyond the forced `C-1`
restricts on `V_0` to a forest satisfying (3.3).

#### Proof

Equation (3.2) shows that a `C`-component spanning forest on `V_0` has
exactly `|mathcal U_0|` edges.  If (3.3) is bijective, the component edges
cover `mathcal U_0`, while Corollary 2.2 covers `mathcal U_B` and spends
exactly one repeat per collar.  The endpoint conditions make the gluing a
single path.  This proves the forward direction.

Conversely, Theorem 1.1 and (1.8) leave no spare upper occurrence: the
collars already spend every allowed repeat and the component forest has
exactly `|mathcal U_0|` edges.  Hence its edge-union map must be injective
and must hit every remaining target.  \(\square\)

Theorem 3.1 is a standard-looking **rainbow prescribed-end linear-forest**
problem, but it is not an ordinary bipartite perfect matching.  Besides the
upper-colour partition constraint, it simultaneously imposes tail and head
capacity one and graphic acyclicity.  In the unpunctured case this is the
ordered-four-transversal/Catalan Linear Matching gate.  Thus the protected
complement problem already contains that unresolved integral correlation
before residence, literal lower flags, or higher upper witnesses are added.

## 4. Correct weakest full complement statement

For `B(k)+O(1)`, the useful target is therefore not an internally
upper-complete complement.  It is the following joint statement.

### Protected punctured trace-factor statement `PPTF(C_0)`

For all sufficiently large dimensions there are:

1. a parity-appropriate owner-disjoint pivot bank;
2. literal seam collars whose complete upper-q1 multiplicity excess is at
   most the unavoidable value plus `C_0`;
3. a literal resident trace factor on the complementary owners, with the
   prescribed seam states;
4. joint component-and-collar interval witnesses for every upper target,
   not merely internal component witnesses; and
5. a target-once lower flag system with terminal deficiency at most `C_0`.

Together with the exact pivot gluing and terminal literal repair theorems,
`PPTF(C_0)` implies

\[
                         \nu(k)\le B(k)+O(C_0+1).      \tag{4.1}
\]

The owner-side spread theorem is valuable input to item 5 because it
retains almost all low containment hosts.  It does not by itself imply item
2 or the punctured ordered-four-transversal in item 3: its test family
contains low owner stars, whereas upper-q1 collisions live on the facet
cliques of rank-`r+1` sets.

## 5. Exact frontier

This note proves three facts needed before attacking the complementary
factor:

1. a Catalan-scale positive-length bridge bank cannot be treated as pure
   topology; internal upper completeness of the complement is impossible;
2. each pivot has an explicit literal collar with the sharp even-case
   service pattern `s` new upper colours plus one repeat; and
3. after globally disjoint collar service is supplied, the remaining
   owner/q1 problem is exactly one punctured prescribed-end
   ordered-four-transversal.

What remains open is correspondingly sharper:

* select the spread pivot bank with globally disjoint balanced-collar upper
  palettes;
* solve the punctured ordered-four-transversal with those endpoints;
* lift its paths to compatible order-`h` literal traces carrying residence
  and named lower flags; and
* certify the higher, arbitrary-width upper deck jointly across components
  and collars.

No unconditional `B(k)+O(1)` or all-dimensional exact formula is claimed.
