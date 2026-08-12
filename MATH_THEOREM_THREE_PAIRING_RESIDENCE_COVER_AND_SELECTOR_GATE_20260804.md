# Three-pairing residence cover and the exact selector gate

**Date:** 2026-08-04
**Status:** unconditional probabilistic cover theorem, exact integral
selector formulation, and an exact obstruction to deriving a spanning
factor from owner coverage alone.  This note does **not** claim a spanning
resident factor, palette coverage, or a compiler.

## 1. Singleton pairs of one fixed owner

Let `T` be a fixed `r`-subset of `[2r]`, and let `P` be a uniformly random
perfect pairing of `[2r]`.  Write

\[
 X_P(T)=\#\{e\in P:|e\cap T|=1\}.
\]

Thus `X_P(T)` is the dimension of the pair cell containing `T`.  Necessarily

\[
                 X_P(T)\equiv r\pmod 2.                         \tag{1.1}
\]

### Lemma 1.1 (exact law)

For `0<=m<=r` with `m congruent to r modulo 2`,

\[
 \Pr(X_P(T)=m)
 = {\binom rm^2m!\,((r-m)-1)!!^2\over(2r-1)!!}
 = {2^m(r!)^3\over
    m!\,((r-m)/2)!^2(2r)!}.                                    \tag{1.2}
\]

For consecutive admissible values,

\[
 {\Pr(X_P(T)=m+2)\over\Pr(X_P(T)=m)}
 ={(r-m)^2\over(m+1)(m+2)}.                                   \tag{1.3}
\]

#### Proof

Choose the `m` endpoints of cross-pairs on each shore, pair them by a
bijection, and pair the remaining `r-m` points internally on each shore.
This gives the first expression in (1.2).  Substitution of

\[
 (2a-1)!!={(2a)!\over2^aa!}
\]

gives the second.  Taking the quotient at `m+2` gives (1.3). \(\square\)

Put `epsilon=r mod 2`.  Standard central-binomial bounds give

\[
 \Pr(X_P(T)=\epsilon)
 \le 4(r+1)^{3/2}2^{-r}.                                      \tag{1.4}
\]

Indeed, for even `r`,

\[
 \Pr(X_P(T)=0)
 ={\binom r{r/2}\over\binom{2r}r}
 \le2\sqrt r\,2^{-r}.                                       \tag{1.5}
\]

For odd `r`, the exact relation

\[
 \Pr_r(X_P(T)=1)
 ={r^2\over2r-1}\Pr_{r-1}(X_P(T)=0)                           \tag{1.6}
\]

implies (1.4).

### Lemma 1.2 (explicit lower-tail bound)

For every integer `1<=M<=r`,

\[
 p_{r,M}:=\Pr(X_P(T)<M)
 \le 4(r+1)^{3/2}(M+1)r^M2^{-r}.                              \tag{1.7}
\]

#### Proof

Iterating (1.3), for every admissible `m`,

\[
 {\Pr(X_P(T)=m)\over\Pr(X_P(T)=\epsilon)}
 \le {r^{m-\epsilon}\over m!}\le r^M
 \qquad(m<M).
\]

There are at most `M+1` summands.  Apply (1.4). \(\square\)

In particular, whenever `M=o(r/log r)`,

\[
 p_{r,M}
 =\exp\{- (\log2)r+O(M\log r+\log r)\}.                       \tag{1.8}
\]

## 2. Three pairings cover every owner

Call `T` **good in P** when `X_P(T)>=M`.

### Theorem 2.1 (three-pairing cover)

If

\[
 64(r+1)^{9/2}(M+1)^3r^{3M}2^{-r}<1,                          \tag{2.1}
\]

then there are three perfect pairings `P_1,P_2,P_3` of `[2r]` such that
every `r`-set is good in at least one of them.

Consequently, if

\[
 M=L+\lceil3\log_2r\rceil,
 \qquad L=O(\sqrt r),                                         \tag{2.2}
\]

then such three pairings exist for every sufficiently large `r`.

#### Proof

Choose the three pairings independently.  For a fixed owner `T`, the
probability that it is bad in all three frames is `p_{r,M}^3`.  A union
bound over the at most `4^r` middle owners and (1.7) gives

\[
 \Pr(\text{some owner is bad in all three frames})
 \le
 64(r+1)^{9/2}(M+1)^3r^{3M}2^{-r}.                             \tag{2.3}
\]

Under (2.1) this is less than one.  Under (2.2), the base-two logarithm
of the right side is

\[
       -r+3M\log_2r+O(\log r)
       =-r+O(\sqrt r\log r),                                  \tag{2.4}
\]

which tends to minus infinity. \(\square\)

The probabilistic argument gives an ordered triple; repetition is harmless.
For large `r` it can also be made a triple of distinct pairings, since the
collision probability of three independent samples is at most
`3/(2r-1)!!`, while (2.3) tends to zero.

### Theorem 2.2 (the general redundancy law)

Fix integers `q>=h>=1`, and put

\[
                         s=q-h+1.                              \tag{2.5}
\]

If `s>=3` and `M=o(r/log r)`, then for all sufficiently large `r` there are
`q` pairings such that every owner is good in at least `h` frames.

More explicitly, the probability that independent random frames fail has
the bound

\[
 \binom{2r}{r}\,2^q p_{r,M}^{s}
 \le
 2^q\bigl(4(r+1)^{3/2}(M+1)r^M\bigr)^s2^{(2-s)r}.              \tag{2.6}
\]

#### Proof

An owner is good in fewer than `h` frames only if it is bad in at least
`s=q-h+1` frames.  Its probability is at most

\[
 \sum_{j=s}^q\binom qj p_{r,M}^j\le2^q p_{r,M}^s.
\]

Union bound over the middle layer and use (1.7).  When `s>=3`, the linear
term `(2-s)r` dominates the `o(r)` correction. \(\square\)

Thus three frames give one good choice everywhere, and four frames give
at least two good choices everywhere.  The latter redundancy still does
not solve the integral selector; Section 5 gives an exact obstruction.

## 3. Consequence for local residence

Fix `M` as in (2.2).  In every good cell of every pairing, install a cyclic
cube Gray code with same-bit transition separation at least

\[
             m-3\log_2m\ge L.                                 \tag{3.1}
\]

Under the pair-cell embedding, this is an `L`-resident Johnson Hamilton
cycle on that cell.  For frame `i`, the good cells therefore form a partial
`L`-resident cycle factor `F_i` on a domain `G_i`.  Theorem 2.1 says

\[
                         G_1\cup G_2\cup G_3=\binom{[2r]}r.    \tag{3.2}
\]

This is an exact owner cover, not an almost-cover.  It is not yet a
spanning cycle factor because the partial factors overlap.

## 4. The weakest exact edge selector

Let `V=binom([2r],r)`, and let `H` be the simple union of all undirected
edges of the good-cell factors.  Make a symmetric bipartite occurrence
graph `B^{+-}` with shores `V_L,V_R`: for every edge `vw` of `H`, include
both arcs `v_Lw_R` and `w_Lv_R`.

### Proposition 4.1 (exact resident selector equivalence)

There is a spanning simple `L`-resident 2-factor in `H` if and only if
`B^{+-}` has a perfect matching whose induced permutation `sigma` satisfies

\[
 \partial(e_v)\cap\partial(e_{\sigma^j(v)})=\varnothing
 \quad\text{for every }v\in V, 1\le j<L,                     \tag{4.1}
\]

where `e_v=(v,sigma(v))` and

\[
                 \partial(e_v)=v\mathbin\triangle\sigma(v).
\]

#### Proof

Orient every cycle of a resident 2-factor.  Its successor arcs give a
perfect matching of `B^{+-}`, and residence is exactly (4.1).

Conversely, a perfect matching defines a permutation `sigma` of `V` whose
arcs all lie in `H`.  Condition (4.1) excludes a directed two-cycle when
`L>=2`, because its two transition supports are equal.  Thus every
permutation orbit is a simple cycle of length at least three.  The same
condition says exactly that two transitions less than `L` edges apart on
an orbit use disjoint physical coordinates.  Hence the projected cycle
cover is a simple `L`-resident 2-factor. \(\square\)

Without (4.1), Hall in `B^{+-}` gives only a directed permutation cover;
it may contain an antiparallel two-cycle and it need not be resident.

There is a useful narrower topological selector.  Orient every cycle of
every `F_i`, let `s_i:G_i->G_i` be its successor permutation, and define
`B^to` by the arcs

\[
             v_Ls_i(v)_R\qquad(v\in G_i).                     \tag{4.2}
\]

Then `B^to` has a perfect matching exactly when

\[
 \left|\bigcup_{i=1}^3s_i(X\cap G_i)\right|\ge|X|             \tag{4.3}
\]

for every `X subseteq V`.  This is ordinary Hall.  A matching gives a
directed spanning permutation cover using only the chosen orientations;
it becomes a resident simple 2-factor precisely when its orbits also
satisfy (4.1).

Thus the weakest exact integral object is a **collar-compatible perfect
matching** in `B^{+-}`.  Ordinary matching integrality settles the degree
row but not the orbit-collar row.

There is one seam-free specialization.  Let `C` range over all good cells
in all frames.  Selecting whole cell cycles gives a spanning resident
factor if and only if

\[
 x_C\in\{0,1\},\qquad
 \sum_{C\ni v}x_C=1\quad(v\in V).                              \tag{4.4}
\]

has a solution.  This is an exact-cover problem on three partitions.  It
is sufficient, and it is necessary if residence is to be inherited only
from uncut cell cycles, with no cross-frame collar theorem.

## 5. What the cover theorem does and does not imply

### Proposition 5.1 (a positive regular-multiplicity selector)

If every owner belongs to exactly `a>=1` of the domains `G_i`, then `B^to` is
`a`-regular as a bipartite multigraph.  It therefore has a perfect matching;
indeed its edge set decomposes into `a` perfect matchings.

#### Proof

Each active frame contributes one outgoing and one incoming successor arc
at every owner in its domain.  Hence both copies of every owner have degree
`a`.  Hall follows by counting edges from a left set into its neighbourhood,
or equivalently from the standard decomposition of a regular bipartite
multigraph. \(\square\)

This proves a directed permutation cover only.  A selected matching may
contain a two-cycle or mix frames too rapidly to satisfy (4.1).

### Proposition 5.2 (all perfect pairings close ordinary successor Hall)

Assume `M<=r`, and take the family of **all** perfect pairings of `[2r]`.
In every good cell of every pairing, choose and orient one of the resident
cube cycles from Section 3.  The resulting successor-occurrence bipartite
multigraph `B_all^to` is regular and has a perfect matching.  Hence it has
a directed spanning permutation cover.

#### Proof

For an owner `T`, let `a(T)` be the number of perfect pairings `P` for which
`X_P(T)>=M`.  The symmetric group on `[2r]` acts transitively on the middle
owners and bijects the perfect pairings, while preserving `X_P(T)`.  Thus
`a(T)=a` is independent of `T`.  Also `a>0`: a perfect matching between
`T` and its complement has `X_P(T)=r>=M`.

Every good frame containing `T` contributes exactly one oriented successor
occurrence from `T` and exactly one oriented predecessor occurrence into
`T`.  Therefore both copies of every owner have degree `a` in
`B_all^to`, counting parallel occurrence arcs separately.  A regular
bipartite multigraph has a perfect matching.  \(\square\)

This does not prove a resident simple 2-factor.  The selected matching may
change frames from one edge to the next, violate the collar condition
(4.1), or choose the two orientations of one Johnson edge as an
antiparallel two-cycle.

### Proposition 5.3 (owner cover, even with redundancy two, is insufficient)

There are four partial oriented cycle factors whose domains cover every
vertex at least twice, but whose union has no spanning cycle factor.

#### Proof

Take vertices `a,b,c,d,e`.  Let two frames be copies of the triangle

\[
                         a-b-c-a,
\]

and let the other two be copies of

\[
                         a-d-e-a.
\]

Every vertex belongs to at least two frame domains.  Ignoring duplicate
physical edges, the union is two triangles sharing only `a`.

Any spanning 2-factor would have to use the entire `a-d-e-a` triangle to
give `d,e` degree two, and the entire `a-b-c-a` triangle to give `b,c`
degree two.  Then `a` has degree four, a contradiction.  In the oriented
selector, the same failure is the Hall set consisting of the two vertices
whose forced successors are both `a`. \(\square\)

Therefore Theorem 2.2 with `(q,h)=(4,2)` still does not supply the selector.
The obstruction is not lack of local choices; it is collision of those
choices at the common occurrence.

## 6. Exact remaining residence theorem

The probabilistic geometry now supplies finitely many global frames with
no uncovered owner.  What remains is one of the following genuinely
integral statements:

1. prove Hall (4.3) and the orbit-collar constraints (4.1) for a jointly
   chosen set of good-cell Gray cycles;
2. solve the seam-free exact cover (4.4); or
3. plant run-transparent cross-frame switches and prove a collared
   `f`-factor theorem in their occurrence lift.

The three-pairing theorem removes the low-cell **owner-supply** obstruction.
Using all perfect pairings additionally removes ordinary successor Hall by
Proposition 5.2.  It still does not remove the collar-compatible occurrence
selector, and the five-vertex example shows that no argument using only the
multiplicities

\[
                 \#\{i:v\in G_i\}
\]

can do so.
