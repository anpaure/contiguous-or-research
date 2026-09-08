# Common-basis representatives: private alternating circuits and the exact graphic alteration gate

Date: 2026-07-31  
Status: exact exchange reduction and a quantitative sufficient alteration
theorem.  This does **not** prove that the Boolean punctured-side incidence
graphs satisfy the required circuit-supply hypothesis.

## 0. Verdict

The uniform-marginal common-basis theorem closes selection of the deleted
child bank `Q`; it does not by itself control the nonlinear physical defects
of the two diagonal representatives.  Nevertheless, once one exports a
bank of private matching-alternating circuits, the remaining physical
selection **on that private face** has an exact partition--graphic
two-matroid form rather than a new four-resource matching problem.

The rigorous conclusions are as follows.

1. For a fixed common basis `Q`, every change of either saturating diagonal
   matching is a disjoint union of alternating circuits.  After contracting
   the matching edges, these are precisely directed cycles in an explicit
   exchange digraph.  A selected representative is immutable exactly when
   its contracted vertex lies on no directed cycle.
2. A circuit passes the physical row exactly when its added physical edges
   obey the degree caps and form a forest after contraction of the graph
   left by its removed edges.  This test simultaneously sees side cycles and
   cycles in the final attachment graph `Gamma_Q`.
3. Suppose local circuits have private incidence and physical sockets, and
   after their common off-state deletion every option contributes one
   possible link between components of a fixed forest.  Then one can repair
   every defect in a set `I` if and only if

   ```text
   r_gr(union_(i in J) L_i) >= |J|       for every J subset I,       (0.1)
   ```

   where `L_i` is the link bank for defect `i`.  This is Rado's theorem for
   the graphic matroid.  It is a finite, cutwise, proof-producing criterion.
4. More generally, if

   ```text
   r_gr(union_(i in J) L_i) >= alpha |J| - beta                    (0.2)
   ```

   for every `J`, one alteration round repairs at least
   `alpha|I|-beta` defects.  Under regeneration of the same hypothesis,

   ```text
   V_(t+1) <= (1-alpha)V_t + beta.                                 (0.3)
   ```

   Thus bounded live boundary/debt follows from a genuine rank-expanding
   private circuit bank; bounded support or scalar switch abundance does not
   suffice.
5. There are two sharp architecture-level obstructions.  Fixed matching
   edges can already force an anchor overload or a cycle.  Also an exchange
   component may be one directed cycle of arbitrary length, so no C6 move
   exists although one long circuit repairs the state.

The independent-boundary absorber supplies the right *local* ingredient in
the balanced diamond graph: prescribed boundary diamonds may be joined by
an alternating path.  To invoke the theorem below for the punctured
off-centre side graphs one must still prove disjoint off-state installation,
node-private ports, and the corresponding off-centre corridor realization.
That transfer is not automatic from the existing absorber theorem.

## 1. The representative exchange digraph

Let `B=(L,R;E)` be a balanced bipartite graph and let `M` be a perfect
matching.  Contract each edge of `M` to a vertex.  For every nonmatching
edge joining the left endpoint of matched edge `e_i` to the right endpoint
of matched edge `e_j`, put the directed arc

```text
                         i -> j.                                  (1.1)
```

Call the resulting directed multigraph `D_M`.

### Lemma 1.1 (exact circuit dictionary)

Directed simple cycles of `D_M` are in bijection with simple
`M`-alternating cycles of `B`.  Toggling the latter gives another perfect
matching.  If `M'` is any other perfect matching, `M triangle M'` is a
vertex-disjoint union of such alternating cycles.

Consequently:

* every perfect matching is reachable from `M` by alternating-circuit
  toggles;
* a matching edge `e_i` can be **omitted** by some alternative perfect
  matching if and only if vertex `i` lies on a directed cycle of `D_M`; and
* a C6 toggle is exactly a directed triangle of `D_M`.

#### Proof

Along an alternating cycle, a nonmatching edge goes from the left endpoint
of one matched edge to the right endpoint of the next.  Contracting the
matched edges therefore gives (1.1) around a directed cycle.  Expansion is
the inverse operation.  The symmetric difference of two perfect matchings
has degree zero or two at every bipartite vertex and hence is a disjoint
union of alternating even cycles.  The last two assertions follow
immediately. `square`

For a forbidden set `Z` of matched edges, an alternating circuit through
`e_i` and avoiding `Z` exists precisely when `i` lies in a nontrivial
strongly connected component of `D_M-Z` (a loop is treated separately).
Thus the first circuit-supply audit is an SCC computation, not a count of
all incidence hexagons.

The two punctured diagonal matchings are independent after `Q` is fixed.
Apply this construction to each shore.  A product move is a collection of
vertex-disjoint directed cycles in the two exchange digraphs.

Explicitly, a directed cycle

```text
                         i_1 -> i_2 -> ... -> i_t -> i_1             (1.2)
```

removes the representatives `(l_(i_j),r_(i_j))` and inserts
`(l_(i_j),r_(i_(j+1)))`, with cyclic indices.  Thus every physical audit of
a C6 or a long circuit is obtained from the signed endpoint-degree vector

```text
delta_C(v)=sum_(e added) 1_(v in phi(e))
          -sum_(e removed)1_(v in phi(e)).                         (1.3)
```

### Lemma 1.2 (two absorbers make one literal long circuit)

Work in the balanced Boolean diamond graph to which the
independent-boundary absorber theorem applies.  Let `A_1,A_2` be two
absorbers with the same outer endpoint pair `(L,U)`, internally
outer-vertex-disjoint.  Write their off/on matchings as
`(M_1^-,M_1^+)` and `(M_2^-,M_2^+)`.  Then

```text
M_old=M_1^+ union M_2^-,       M_new=M_1^- union M_2^+             (1.4)
```

cover exactly the same outer vertices, each once.  Their symmetric
difference is one matching-alternating circuit, obtained by joining the two
internally disjoint alternating `L`--`U` paths.  Each path has at most
`2m+1` edges, so the circuit has at most `4m+2` edges.

If, in addition, the two absorber supports are cross-disjoint in every
physical middle role, then (1.4) is a literal resource-disjoint
representative switch.  Each path separately permits arbitrary prescribed
boundary diamonds under the endpoint-distance hypothesis.  That fact does
**not** assert that two such prescribed paths can simultaneously be chosen
internally or physically disjoint; disjoint two-path packing remains an
extra hypothesis here.

#### Proof

For each absorber, `M_i^-` covers all its internal outer vertices and
neither endpoint, whereas `M_i^+` covers the same internal vertices and
both `L,U`.  Hence both sides of (1.4) cover every internal vertex and cover
`L,U` exactly once.  On each absorber support the symmetric difference is
its full alternating endpoint path.  The two paths share only their
endpoints, so their union is an alternating cycle.  The length and physical
claims are exactly those of the independent-boundary theorem plus the
stated cross-disjointness. `square`

This lemma upgrades the local augmentor into the correct matching-preserving
move.  It still does not pack many such pairs: cross-corridor physical
disjointness and off-state installation are precisely the global private
bank hypotheses in Section 3.  Also, the currently proved absorber is
balanced; applying the construction to the punctured off-centre side graph
requires a separate embedding or analogue.

The required analogue does hold in the **full** off-centre diamond graph.
The puncture may still delete its internal lower vertices, so this does not
yet close the side theorem.

### Theorem 1.3 (off-centre independent-boundary absorber)

Let `r>=4`, let `Omega` have order `2r`, and let

```text
L in C(Omega,r),       U in C(Omega,r+2),
s=|L-U|>=3.                                                       (1.5)
```

Prescribe arbitrary boundary incidences

```text
Y_0=L+{p,q},          X_*=U-{rho,tau}.                             (1.6)
```

Then the full incidence graph between ranks `r` and `r+2` contains an
alternating `L`--`U` path with first upper vertex `Y_0` and last lower
vertex `X_*`.  Its off state covers every internal outer vertex and neither
endpoint; its on state covers the same vertices together with `L,U`.  In
each state all lifted rank-`r+1` physical vertices are distinct.  The path
has at most `2r+3` edges.  The case `r=4` is vacuous because
`|Omega-U|=r-2=2`, so (1.5) cannot hold; the first nonempty case is `r=5`.

#### Proof

Choose distinct

```text
a_0,a_1,a_* in L-U
```

and name the prescribed start pair so that `p` is used first and `q`
second.  Put

```text
X_0=L,             X_1=L-a_0+p,             X_(d+1)=X_*.
```

Let `A=X_1-X_*`, `B=X_*-X_1`, and `d=|A|=|B|`.  The set `A` contains
`(L-U)-{a_0}`, so `d>=2` and contains `a_1,a_*`.  Choose
`b_1 in B-{q}`.  Order

```text
A=(a_1,...,a_d) with a_d=a_*,
B=(b_1,...,b_d),
```

and take the monotone Johnson geodesic

```text
X_(i+1)=X_i-a_i+b_i                    (1<=i<=d).       (1.7)
```

For `1<=i<=d` put `Z_i=X_i+b_i`.  Choose a filler
`c_i notin Z_i` subject to

```text
c_i != a_(i-1),
c_i != b_(i+1)                 when i<d,               (1.8)
```

where `a_0` has its already declared meaning.  There are

```text
|Omega-Z_i|=r-1>=3
```

choices and at most two forbidden values, so this is possible.  Define

```text
V_0=Y_0,             V_i=Z_i+c_i       (1<=i<=d).      (1.9)
```

Now use the alternating path

```text
L=X_0,V_0,X_1,V_1,...,X_d,V_d,X_(d+1)=X_*,U.          (1.10)
```

The two matchings are

```text
M^-={X_(i+1)V_i:0<=i<=d},
M^+={X_iV_i:0<=i<=d} union {X_*U}.                    (1.11)
```

They have the asserted outer coverage.  It remains to check physical
collisions.  For an internal transition `i>=1`, the common physical vertex
is `Z_i`; the other one is

```text
C_i=X_i+c_i       in M^+,
D_i=X_(i+1)+c_i   in M^-.                             (1.12)
```

Along a monotone Johnson geodesic, a rank-`r+1` set containing `X_i` can
coincide with a transition union only at an adjacent transition.  The
first exclusion in (1.8) prevents `C_i=Z_(i-1)` (with
`Z_0=L+p=X_1+a_0`), and the second prevents `D_i=Z_(i+1)`.  Nonadjacent
lower bases differ in at least two coordinates, while adjacent auxiliary
vertices cannot agree because their common transition union already
contains the exchanged coordinate.  Hence the internal physical vertices
are distinct in each state.

The start on-state vertices are `L+p,L+q`, and the start off-state vertices
are `L+p,X_1+q`.  The choice `b_1!=q`, the fact `b_1!=a_0`, and the first
exclusion in (1.8) separate these from the first internal transition.  All
later internal bases contain `b_1`, whereas no start physical vertex does,
so there are no later start collisions.

Finally, every transition union `Z_i` and every `C_i` contains the last
unswapped element `a_*=a_d` until the last exchange, and `Z_d=X_*+a_*`.
Since `a_* notin U`, none can equal either final on-state physical vertex
`X_*+rho,X_*+tau`.  The two final vertices are distinct.  The same
monotone-base argument proves the upper vertices `V_i` distinct; `V_0`
cannot equal `V_1` because `{a_0,q}` cannot equal `{b_1,c_1}`, every later
`V_i` contains `b_1` while `V_0` does not, and no `V_i` equals `U` because
it contains `a_*` or still misses an element of `X_*`.

Thus (1.11) is collision-free in both states.  Since `d<=r`, (1.10) has
`2d+3<=2r+3` edges. `square`

Theorem 1.3 removes the rank-offset issue for large parameters.  To use it
inside a punctured diagonal graph one must additionally keep every lower
geodesic vertex `X_i` in the surviving domain and pack two corridors with
cross-disjoint physical resources.  Those are global reserve conditions,
not consequences of (1.5).

## 2. The exact physical test for one or many circuits

Let `phi:E -> binom(V,2)` send a containment incidence to its lifted
physical Johnson edge.  In the Boolean diamond graph this map is injective:
the physical intersection and union recover the incidence endpoints.

Let `H_0` contain all physical edges not changed by the diagonal matching,
including the retained child forest and the seam edges.  For a matching
`M`, put

```text
                         H(M)=H_0 union phi(M).                    (2.1)
```

Give each physical vertex a cap `b(v)`: it is one at a seam anchor and two
at an ordinary side vertex.  For a family `C` of pairwise
incidence-disjoint alternating circuits write

```text
R_C = phi(M intersect union C),
A_C = phi((union C) - M),
H_C = H(M) - R_C + A_C.                                           (2.2)
```

### Lemma 2.1 (degree and topology certificate)

Assume `H(M)-R_C` is a forest.  Then `H_C` is a capped linear forest if and
only if

```text
d_(H(M)-R_C)(v)+d_(A_C)(v) <= b(v)       for every v,              (2.3)
```

and, after contracting every component of `H(M)-R_C`, the multigraph
formed by `A_C` is loopless and acyclic.  Parallel pairs count as a
two-cycle.

The same statement remains valid when the vertices contracted in (2.2)
include the retained child and both side forests.  In that form the last
test is exactly the `Gamma_Q` forest condition.

#### Proof

Equation (2.3) is the definition of the physical caps.  Adding an edge to a
forest creates a cycle exactly when its endpoints already lie in the same
component, or when it closes a cycle among previously contracted
components.  Applying this one edge at a time gives the loopless-forest
criterion.  A capped acyclic graph with cap at most two is a linear forest.
`square`

There is no pairwise-local substitute for the last row in general: three
individually and pairwise harmless component links may together form a
triangle.  A conflict *graph* is therefore sound only after a private-port
or graphic-matroid reduction such as the next theorem.

### Theorem 2.2 (exact fixed-`Q` circuit characterization)

Fix `Q` and initial saturating matchings on both shores.  A physically
acceptable pair of saturating matchings exists if and only if there are
vertex-disjoint directed-cycle families in the two exchange digraphs such
that their combined removal/addition sets satisfy (2.3) and the contracted
loopless-forest test of Lemma 2.1.

#### Proof

Toggling such cycle families preserves both saturating matchings by Lemma
1.1, and Lemma 2.1 gives physical acceptability.  Conversely, compare the
initial pair with any acceptable pair.  Their two symmetric differences
are vertex-disjoint alternating-cycle families.  The graph left after
removing the old-only physical edges is a subgraph of the acceptable final
graph, hence is a forest.  Lemma 2.1 therefore applies and certifies exactly
the displayed rows. `square`

Thus long alternating circuits are a complete move language at fixed `Q`.
The difficulty is not reachability; it is finding a cycle packing whose
physical images pass the degree and graphic rows.

## 3. Private unit-link circuit atlases

Fix a representative state and an integer set `I` of defect tokens.  A
token may be one unit of anchor overload, one unit of ordinary degree
overload, or one chosen edge of a cycle-breaking basis.  A **private
unit-link atlas** is first put in the following quarantined normal form.

The current physical graph is a fixed forest `F_0` together with
pairwise-private off fragments `R_i`, one for every `i in I`.  Each `R_i`
is attached to at most one component of `F_0`, interacts with no other
`R_j`, and carries exactly token `i`.  Thus leaving `R_i` in place retains
that local defect but contributes no link between two components of
`F_0`.  Deleting all `R_i` leaves exactly `F_0`.

The atlas then consists of the following data.

1. For every `i in I`, a nonempty family `S_i` of alternating circuits in
   one of the two representative exchange digraphs.  Every option in
   `S_i` has the same matching off state whose physical image is `R_i`;
   it may have a different on state.
2. The off-state matching packets are installed in pairwise disjoint
   incidence corridors.  Options belonging to distinct tokens use
   disjoint private outer vertices and distinct physical attachment ports.
   Hence any one option per token may be toggled simultaneously at the
   matching and degree rows.
3. For every `C in S_i`, all on-state physical edges internal to its
   private corridor form a forest, obey all local caps, repair token `i`,
   and, after their internal vertices are suppressed, have exactly one
   nonlocal effect: a link

   ```text
                       ell(C) in K^(2),                            (3.1)
   ```

between components of `F_0`, where `K^(2)` denotes unordered pairs with
repetition; equal endpoints record a loop.  No option creates another
defect token.
   If token `i` is not selected in a partial alteration, its old fragment
   `R_i` remains; by quarantine it cannot interact with the selected
   component links.

Here `K` is the component set of `F_0`.  Let

```text
                         L_i={ell(C):C in S_i}.                     (3.2)
```

Multiple circuits giving the same link are harmless; only the link set
matters after privacy has been certified.

The privacy assumption is precisely what the independent-boundary
absorber is designed to supply: one first assigns distinct boundary
diamonds/ports and then realizes the intervening alternating paths.  The
existing theorem gives the second step for balanced endpoints at distance
at least three.  It does not by itself give the first step or its
off-centre punctured-side analogue.

### Theorem 3.1 (private-circuit Rado theorem)

There is a simultaneous circuit choice `C_i in S_i` for every `i in I`
whose toggled physical graph is a capped linear forest if and only if

```text
r_gr(union_(i in J) L_i) >= |J|       for every J subseteq I.      (3.3)
```

Here `r_gr` is rank in the graphic matroid on the component multigraph
`K`; loops have rank zero and parallel links have rank one.

Equivalently, if `kappa_J` is the number of connected components of the
graph `(K, union_(i in J)L_i)`, including isolated vertices, then

```text
                         |K|-kappa_J >= |J|.                       (3.4)
```

#### Proof

By atlas privacy, choosing a circuit is equivalent at all matching,
degree, and local-forest rows to choosing its link.  The total physical
graph is a forest exactly when the selected links are independent in the
graphic matroid, by Lemma 2.1.  Thus the remaining problem is to choose one
element of every set `L_i` so that the chosen elements are independent.
Rado's independent-transversal theorem gives exactly (3.3).  Formula
(3.4) is the graphic rank formula. `square`

This is a proof-producing finite criterion.  A violating family `J`
certifies the precise component bottleneck; a passing instance produces
the circuit list by a graphic-matroid transversal algorithm.

### Theorem 3.2 (quantitative partial alteration)

The maximum number of distinct defect tokens simultaneously repairable by
a private unit-link atlas equals

```text
 min_(J subseteq I) ( |I-J| + r_gr(union_(i in J)L_i) ).           (3.5)
```

In particular, if constants `alpha in [0,1]` and `beta>=0` satisfy

```text
r_gr(union_(i in J)L_i) >= alpha|J|-beta
                                      for every J subseteq I,      (3.6)
```

then at least `alpha|I|-beta` tokens can be repaired simultaneously.

#### Proof

Formula (3.5) is the deficient form of Rado's theorem (equivalently,
adjoin dummy freely independent elements and apply Theorem 3.1).  Using
(3.6), every term in (3.5) is at least

```text
|I-J|+alpha|J|-beta
 = |I|-(1-alpha)|J|-beta
 >= alpha|I|-beta.
```

`square`

### Corollary 3.3 (regenerative contraction)

Let `V_t` be the number of live defect tokens after round `t`.  Suppose
that whenever `V_t>0`, the current state exports a new private unit-link
atlas satisfying (3.6) with the same `alpha,beta`, and that repaired tokens
are not recreated.  Then

```text
V_(t+1) <= (1-alpha)V_t+beta,                         (3.7)
V_t <= (1-alpha)^t V_0 + beta/alpha                  (3.8)
```

for `alpha>0`.  If the sharper rank bound is

```text
r_gr(union_(i in J)L_i) >= alpha(|J|-beta),           (3.9)
```

then `V_t <= (1-alpha)^tV_0+beta`.

This is the exact kind of bounded-defect regenerative invariant needed by
an additive-constant recursion.  The substantive all-`n` gate is now a
rank-expanding private circuit supply theorem, not a scalar estimate for
the number of available switches.

### Corollary 3.4 (fixed-backbone pressure criterion)

Suppose all candidate links lie in one prescribed forest `T` on the
component set of `F_0`.  If every nonexceptional defect has at least
`lambda` candidate links and every edge of `T` belongs to the lists of at
most `mu` nonexceptional defects, then

```text
r_gr(union_(i in J)L_i)=|union_(i in J)L_i|
                       >= (lambda/mu)|J|              (3.10)
```

for every set `J` of nonexceptional defects.  Hence:

* if `lambda>=mu`, every nonexceptional defect can be repaired at once;
* in general one round repairs at least
  `min(1,lambda/mu)|I|-beta` defects when at most `beta` defects are
  exceptional; and
* regeneration gives (3.7) with
  `alpha=min(1,lambda/mu)`.

#### Proof

Every subset of the edge set of `T` is graphically independent, proving
the equality in (3.10).  Count token--link incidences over `J`.  There are
at least `lambda|J|`, while each link is counted at most `mu` times, so the
union has at least `lambda|J|/mu` members.  Apply Theorem 3.2 and charge the
exceptional tokens to `beta`. `square`

This criterion is deliberately stronger than generic expansion, but its
hypotheses are local and auditable.  It identifies a concrete all-`n`
target: route the independent-boundary corridors to a fixed component-tree
bank, with list size exceeding link pressure.  Once this is achieved,
cycle elimination is automatic rather than a later alteration.

### Proposition 3.5 (private-support capacity)

Let each punctured shore contain `P=binom(2n,n-2)` matching edges.  In a
two-shore private atlas the disjoint off packets satisfy

```text
                         sum_(i in I)|R_i| <= 2P.                   (3.11)
```

Consequently, if every repair circuit uses at least `s` old matching
edges, then

```text
                         |I| <= 2P/s.                              (3.12)
```

Since `P=Theta(N)`, a private bank repairing `Theta(N)` separate defect
tokens must have bounded average off support.  Generic
`Theta(n)`-length absorber pairs can service only `O(N/n)=O(Cat_n)` tokens.

#### Proof

The off packets are pairwise incidence-disjoint subsets of the two current
perfect matchings, which together have `2P` edges.  This proves (3.11), and
(3.12) follows by summation.  Finally `N/n=Cat_n` and `P=Theta(N)`.
`square`

Thus the independent-boundary absorber is automatically a Catalan-scale
final augmentor when used at generic distance.  Bulk suppression of a
central-layer number of side overloads requires C6/constant-support atoms,
or circuits which repair many defect tokens at once.

## 4. What uniform common-basis marginals do and do not buy

At child parameter `n`, put

```text
N=binom(2n,n-1),       K=Cat_n=N/n,
C=Cat_(n+1),           C/N=2(2n+1)/(n(n+2)) < 4/n.   (4.1)
```

The common-basis theorem gives a distribution with
`Pr(q in Q)=C/N` for every child edge `q`.  Therefore, for every
nonnegative **precomputed additive** risk `w(q)`, some common basis obeys

```text
w(Q) <= (C/N) w(F).                                  (4.2)
```

### Corollary 4.1 (additive exceptional-bank reduction)

Suppose the private-circuit construction is robust under the later choice
of both diagonal representatives, except at child atoms charged by a
precomputed cost `w`, and `w(F)=O(N)`.  Then one may choose the synchronized
common basis so that the total exceptional charge is `O(K)`.

#### Proof

Use (4.2) and `C/N<4/n`, while `N/n=K`. `square`

The word **precomputed** is essential.  Physical overloads such as

```text
binom(d_G(v),3),       (d_G(v)-2)_+,       beta(G)                  (4.3)
```

are nonlinear functions of the eventual representative matching.  Exact
one-element marginals for `Q` give no bound on their expectation and no
negative dependence.  Nor does (4.2) show that the two saturating
representative matchings can be selected from private circuit-rich faces.
Thus the uniform-marginal theorem can pay an `O(K)` *exceptional atlas*
once robustness is proved; it cannot manufacture that atlas.

It does, however, preserve almost all of any precomputed **sublinear
corridor bank**.  This is the strongest direct use of the balanced
distribution.

### Theorem 4.2 (common-basis puncture survival)

For each prospective defect token `i in I`, let `P_i` be a nonempty finite
family of precomputed side-corridor candidates.  For `P in P_i`, let
`R(P) subseteq F` be the child atoms whose membership in `Q` would puncture
that corridor: on the minus shore these are atoms whose tails are required
lower vertices, and on the plus shore atoms whose heads are required lower
vertices.  A candidate may combine both shores by taking the union of the
two risk sets.  Put

```text
ell_i = (1/|P_i|) sum_(P in P_i)|R(P)|,
alpha = C/N.                                                       (4.4)
```

There is a synchronized common basis `Q` for which, if `b_i` is the
fraction of candidates in `P_i` punctured by `Q`, then

```text
                         sum_(i in I)b_i <= alpha sum_(i in I)ell_i. (4.5)
```

Consequently, if every `ell_i<=L`, then for every `theta>0`, all but at
most

```text
                         (alpha L/theta)|I|                         (4.6)
```

tokens retain at least a `(1-theta)` fraction of their candidate
corridors.  In particular, when `L=o(n)`, taking
`theta=sqrt(alpha L)` leaves all but `o(|I|)` tokens with a
`1-o(1)` fraction of their lists.

#### Proof

Define the additive child-atom cost

```text
w(q)=sum_(i in I) |{P in P_i:q in R(P)}|/|P_i|.                    (4.7)
```

Choose `Q` using (4.2).  Then

```text
w(Q) <= alpha w(F)=alpha sum_i ell_i.                              (4.8)
```

Every punctured candidate contains at least one selected risk atom, so a
union bound inside each list gives `b_i` at most its contribution to
`w(Q)`.  Summing proves (4.5).  Markov's inequality on the deterministic
numbers `b_i` proves (4.6).  Finally `alpha<4/n`, so `alpha L=o(1)` when
`L=o(n)`. `square`

Theorem 4.2 is correlation-free: exact one-atom marginals suffice because
puncture risk is union-bounded into an additive cost.  It says that a
sublinear-length private corridor atlas survives synchronization almost
intact.  It says nothing about cross-corridor middle-resource conflicts,
off-state installation, or the graphic ranks of the surviving links.
For generic length-`Theta(n)` corridors the right side of (4.5) may be a
constant multiple of `|I|`, so the theorem deliberately makes no survival
claim at that scale.

### Corollary 4.3 (sublinear private-tree alteration)

Assume a precomputed **`Q`-robust** private atlas has the following
deterministic form.

1. Every defect token has `s_0` distinct candidate links in one fixed,
   `Q`-independent component forest `T`, with **one designated corridor
   candidate per link**.  Thus puncture survival is measured on distinct
   links, not on a multiset of several corridors realizing one link.  For
   every common basis under consideration, each surviving designated
   candidate contracts to its declared edge of `T`.
2. Every edge of `T` occurs in at most
   `mu<=(1-epsilon)s_0` token lists, for a fixed `epsilon>0`.
3. Every link is realized by a corridor candidate, and the average puncture
   risk (4.4) of every token is at most `L=o(n)`.
4. The privacy, common-off-state, local cap, no-new-defect, and component-
   contraction hypotheses of Section 3 hold for every surviving candidate
   after every allowed puncture.

Then some synchronized common basis leaves a simultaneous circuit repair
for all but at most

```text
                         (2 alpha L/epsilon)|I|=o(|I|)              (4.9)
```

defect tokens.  Equivalently one alteration round has

```text
                         V' <= (2 alpha L/epsilon)V=o(V).           (4.10)
```

If initially `V=O(N)` and `L=O(1)`, this sharpens to

```text
                         V'=O(N/n)=O(Cat_n).                        (4.11)
```

#### Proof

Apply Theorem 4.2 with `theta=epsilon/2`.  Apart from the number in (4.9),
every token retains at least `(1-epsilon/2)s_0>mu` distinct links.  Puncture
deletion cannot increase the pressure of any tree edge.  Corollary 3.4
therefore gives a simultaneous graphic-independent representative for all
remaining tokens.  Since `alpha<4/n` and `L=o(n)`, the coefficient in
(4.10) tends to zero.  When `V=O(N)` and `L=O(1)`, the same estimate is
`O(N/n)=O(Cat_n)`, proving (4.11). `square`

Corollary 4.3 is a rigorous asymptotic alteration theorem under explicit
pseudorandom hypotheses.  Its unproved Boolean content is sharply exposed:
construct a `Q`-robust node-private, common-off-state, fixed-tree corridor
bank of sublinear risk length with a constant list-pressure gap.  In
particular, the components of `F-Q` normally depend on `Q`; treating their
link tree as precomputed without a robustness proof would invalidate this
corollary.  Neither the common-basis theorem nor the independent-boundary
path theorem alone gives that bank.

## 5. Sharp exchange obstructions

### Proposition 5.1 (fixed representative core)

Let

```text
                         Fix(B)=intersection{M':M' perfect in B}.  (5.1)
```

Every alternating-circuit sequence preserves `Fix(B)`.  Consequently no
capped-forest representative exists if either

```text
d_(H_0 union phi(Fix(B)))(v)>b(v)       for some v,                 (5.2)
```

or `H_0 union phi(Fix(B))` already contains a cycle.

#### Proof

By Lemma 1.1 an edge changes membership only on an alternating cycle.
Edges in (5.1) lie on none.  Conditions (5.2) and cyclicity are hereditary
under adding more physical edges. `square`

This obstruction is invisible to part sizes, average degree, a fractional
matching, and the common-basis marginals.  In the exchange digraph it is
the union of vertices lying on no directed cycle.

### Proposition 5.2 (bounded C6 moves are incomplete)

For every `ell>=4` there is a balanced bipartite graph with exactly two
perfect matchings whose symmetric difference is one alternating
`2ell`-cycle.  Relative to either matching, `D_M` is one directed
`ell`-cycle.  It has no directed triangle and hence no C6 move, although
the unique long alternating circuit changes the matching.

One may assign the physical labels so that the first matching violates an
anchor cap while the second does not.  Therefore no theorem using only C6
repairs can hold at the abstract representative level.

#### Proof

Take the bipartite cycle `C_(2ell)`.  Its two alternating edge shores are
its only perfect matchings.  Contracting either shore gives a directed
`ell`-cycle.  Assign two edges of the first matching physical images
incident with one cap-one anchor and assign the second-shore images to
distinct private vertices. `square`

This is an architecture-level obstruction, not a claim that a particular
Boolean side incidence graph has no additional chords.  For the Boolean
theorem it says that one must prove either long-circuit supply or enough
chords to triangulate every required exchange.

## 6. Exact remaining Boolean theorem

The following statement would complete the physical row left by the
automatic common-basis theorem.

> **Boolean private-circuit expansion.**  One can choose a synchronized
> common basis `Q` and its two saturating diagonal matchings so that, after
> charging `O(K)` precomputed exceptional atoms, all physical degree,
> anchor, and cycle defects admit node-private alternating-circuit banks.
> Their unit-link sets satisfy (3.9) with constants `alpha>0` and
> `beta=O(K)` (or, for an exact theorem, (3.3)), and the off-state corridors
> are simultaneously installed.

The independent-boundary absorber handles the local boundary-to-boundary
path after its off state and ports are supplied.  The missing proof is the
global correlation: robust circuit SCCs, private port assignment, and the
graphic rank inequality.  A raw count of C6 atoms, a uniform fractional
matching, or uniform one-edge marginals does not imply any of these.

The theorem above is nonetheless a genuine simplification.  On the
private face, simultaneous side linearity and `Gamma_Q` acyclicity reduce
to one ordinary graphic Rado inequality, and quantitative rank expansion
gives the desired contraction recurrence with exact constants.
