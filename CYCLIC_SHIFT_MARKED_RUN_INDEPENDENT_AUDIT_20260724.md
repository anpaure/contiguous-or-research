# Independent audit: cyclic shift, marked excursions, and corridor Hall cuts

Date: 2026-07-24

## Verdict

The forced deletion law, the common-prefix excursion identity, the fixed
Gaussian-window equivalence, the truncated bound `K_H <= 2 R_H`, the
diagonal upper bound, and the target-side corridor deficiency in
`CYCLIC_SHIFT_MARKED_RUN_REDUCTION_20260724.md` are correct.

There are four useful sharpenings.

1. The truncation argument gives the stronger formula

   \[
   K_H\le R_H+B_H\le2R_H,
   \]

   where `B_H` is the number of nontrivial permutation blocks completed by
   depth `H`.
2. Moved deletion sites admit an exact inter-mark run formula, and prefix
   crossings admit a sharper displacement-area bound.  The latter can save
   a factor `H` over the diagonal union bound.
3. The target-side Hall cut has a complementary owner-side cut.  The two
   cut families are jointly necessary and sufficient for a corridor-supported
   balanced assignment at one fixed rank.
4. A cyclic shift has crossing multiplicity one, but it does **not** lie in
   the symmetric containment corridor of radius one.  Symmetric radius one
   forces a product of disjoint adjacent transpositions, hence only singleton
   excursions.  The radius-two zig-zag cycle in the main note is sharp.

## 1. Exact excursion and moved-site formulas

For one owner, write

\[
 d_t=a_{\rho(t)},\qquad \rho\in S_m,
\]

and put

\[
 \kappa(q)=|\rho([q])\setminus[q]|
 =\#\{t\le q:\rho(t)>q\}.
\]

Then

\[
 P_q\ne\Gamma_q\quad\Longleftrightarrow\quad\kappa(q)>0.
\]

Let `z_1<...<z_k` be the moved positions of `rho`, and set
`z_(k+1)=m+1`.  At an unmoved position both prefix sets acquire the same new
element, so their equality status cannot change.  Consequently, with

\[
 \beta_j={\bf1}\{\rho([z_j])\ne[z_j]\},
\]

the exact truncated owner cost is

\[
 \boxed{
 \sum_{q=1}^{H}\frac{{\bf1}\{P_q\ne\Gamma_q\}}{c_q}
 =\sum_{j:z_j\le H}\beta_j
   \sum_{q=z_j}^{\min\{H,z_{j+1}-1\}}\frac1{c_q}.}
 \tag{1.1}
\]

This is the precise marked-site/run identity.

There is also the crossing coarea identity

\[
 \sum_{q=1}^{H}\frac{\kappa(q)}{c_q}
 =\sum_{t:\rho(t)>t}
   \sum_{q=t}^{\min\{H,\rho(t)-1\}}\frac1{c_q}.
 \tag{1.2}
\]

Since `1_{kappa>0}<=kappa`, (1.2) is a displacement-area upper bound on
the true synchronization loss.  It is substantially sharper than charging
every moved deletion site through every later depth.

For example, for the cyclic shift `rho(t)=t+1` modulo `m`, one has
`kappa(q)=1` at every proper depth.  Formula (1.2) is exact and has order
`H`, whereas the diagonal union bound has order `H^2`.

## 2. Truncation in the site bound

Consider a nontrivial indecomposable permutation block of length `l`.
If its right endpoint is at most `H`, it contributes at most `l` moved
positions and exactly `l-1` bad prefix states.  If it crosses `H`, and its
left cut is `r`, it contributes at most `H-r` moved positions through `H`
and exactly `H-r` bad prefix states through `H`.

Therefore

\[
 \boxed{K_H\le R_H+B_H\le2R_H,}\tag{2.1}
\]

where every completed nontrivial block counted by `B_H` contributes at
least one bad prefix state.  This proves the truncation case without an
implicit appeal to the untruncated final return.

## 3. Two different notions of corridor width

The cyclic shift has

\[
 \kappa(q)=1\qquad(1\le q<m),
\]

so it has one open crossing token at every cut.  However,

\[
 \rho([q])=\{2,3,\ldots,q+1\}
\]

does not contain `[q-1]`.  Thus it is not in the symmetric rank corridor

\[
 [q-D]\subseteq\rho([q])\subseteq[q+D]
 \tag{3.1}
\]

with `D=1`.

In fact symmetric radius one is completely rigid.

### Lemma 3.1 (radius-one flags are isolated adjacent toggles)

For a permutation `rho`, the following are equivalent:

1. `[q-1] subset rho([q]) subset [q+1]` for every `q`;
2. `|rho(t)-t|<=1` for every `t`;
3. `rho` is a product of disjoint adjacent transpositions and fixed points.

Hence every common-prefix excursion has length exactly one.  If

\[
 T=\{q:\rho([q])\ne[q]\},
\]

then `T` is an independent set in the path `1,...,m-1`, and

\[
 \rho=\prod_{q\in T}(q\ q+1).
\]

#### Proof

The upper inclusion at `q=t` gives `rho(t)<=t+1`.  The lower inclusion at
`q=j+1` gives `rho^{-1}(j)<=j+1`, hence `rho(t)>=t-1`.  A permutation of a
line with bandwidth one consists exactly of disjoint adjacent
transpositions and fixed points.  The remaining assertions follow
immediately.  QED.

For an owner `X`, the two radius-one depth-`q` states are

\[
 \Gamma_q(X)=\Gamma_{q+1}(X)\cup\{a_{q+1}(X)\}
\]

and its sibling

\[
 \widetilde\Gamma_q(X)
 =\Gamma_{q+1}(X)\cup\{a_q(X)\}.
\]

Thus a simultaneous radius-one resolver is exactly a selection of
nonadjacent depth toggles for every owner.  This is a concrete
conflict-free orientation problem.  Radius two is qualitatively different:
the zig-zag successor permutation from the main note has bandwidth two and
one excursion of length `m-1`.  In fact its crossing multiplicity is also
exactly one at every proper cut: the set `[q]` is one cyclic interval in the
zig-zag order, so exactly one directed cycle edge leaves it.  Thus symmetric
radius two plus one open crossing token still does not force a return.

The full product-of-transpositions characterization uses the corridor at
all proper depths.  If it is imposed only through `q<=H<m`, bad depths below
`H` are still isolated, but the state at `H` may be the opening of a block
that closes after the truncation.  A truncated application must either also
control the next cut or allow this one terminal exception per owner.

## 4. Exact one-rank corridor Hall criterion

Fix `q,D` and form the bipartite corridor graph between owners `U` and
rank-`m-q` targets `V`.  An edge means

\[
 \Gamma_{q+D}(X)\subseteq S\subseteq\Gamma_{q-D}(X).
\]

A corridor-supported balanced assignment is a subgraph in which every
owner has degree one and every target has degree in `[c_q,c_q+1]`.

By the integral lower-bounded-flow theorem, such an assignment exists if
and only if both of the following hold:

\[
 \boxed{c_q|A|\le |N(A)|\quad(A\subseteq V),}\tag{4.1}
\]

\[
 \boxed{|B|\le(c_q+1)|N(B)|\quad(B\subseteq U).}\tag{4.2}
\]

The first is the target lower-quota Hall condition already present in the
main note.  The second is the owner/upper-capacity condition.  Accordingly,
the number of noncorridor assignments is at least each of

\[
 \max_{A\subseteq V}(c_q|A|-|N(A)|)_+,
 \qquad
 \max_{B\subseteq U}(|B|-(c_q+1)|N(B)|)_+.
 \tag{4.3}
\]

These cut families are sharp at one rank.  They do not impose nesting across
ranks and, for `D>=2`, do not bound common-prefix return time.

### Adjacent-toggle specialization

For `D=1`, every owner has exactly two sibling states, so it is an edge of a
multigraph `G_q` on the targets.  Choosing the state is orienting that edge
toward its selected endpoint.  The two Hall families reduce to the standard
orientation criterion

\[
 \boxed{e_{G_q}(A)\le(c_q+1)|A|,\qquad
        i_{G_q}(A)\ge c_q|A|\quad(A\subseteq V),}
 \tag{4.4}
\]

where `e_G(A)` is the number of edges internal to `A` and `i_G(A)` is the
number of edges incident with `A`, each edge counted once.  Parallel edges
are harmless; a coincident sibling is a forced loop and may be subtracted as
a fixed preload.

Rankwise orientations satisfying (4.4) still have to obey the cross-depth
condition that one owner cannot toggle at adjacent depths.  This is exactly
the remaining path-independent-set coupling in the radius-one model.

## 5. Correct status

The marked-excursion formalism is exact.  Counts of shift violations,
crossing multiplicity, or rankwise corridor feasibility alone do not bound
return time.  A viable proof can use either:

* weighted displacement area (1.2);
* symmetric radius-one toggles with their cross-depth independent-set
  constraint; or
* radius at least two together with a separate return-time mechanism.

Any statement calling the cyclic shift a symmetric `D=1` corridor example
must be corrected; it is `D=1` only in crossing-multiplicity width.
