# Universal component catalogue, witness-width boundary, and literal splice

Date: 2026-07-29  
Status: solver-free exact theorem synthesis.  No SAT run, factor-existence
search, or compiler-feasibility claim.

## 0. Answer

Let

\[
 K=2r,\qquad n=K-1=2r-1,\qquad
 W=\binom K r,\qquad N=W/n,
\]

and let `rho` rotate the `n` old coordinates and fix the top coordinate.
There are three logically different catalogues.

1. **Factor catalogue.**  After fixing one representative of each free
   middle-owner orbit, the complete undirected catalogue is the set
   `E_K` of rotation orbits of physical Johnson edges.  It has exactly

   \[
                         |E_K|=Nr^2/2.                 \tag{0.1}
   \]

   Selecting weighted quotient degree two at every owner is necessary and
   sufficient for an arbitrary rotation-invariant spanning simple
   two-factor.  If `r` is even, every member of `E_K` occurs in some such
   factor; hence this is the unique inclusion-minimal fixed physical
   edge-orbit catalogue under the fixed coordinate labels.  At `K=16`, it
   has exactly `27,456` variables and `858` weighted degree rows.  No
   component partition or voltage list is selected.

2. **Witness-width catalogue.**  This is separate from factor
   representation.  Every minimal proper depth-`q` upper or lower shadow
   witness has width

   \[
      q+1\le w\le B_{r,q},\qquad
      B_{r,1}=2,\qquad
      B_{r,q}=\binom{r+q-2}{q-2}+2\quad(q\ge2).          \tag{0.2}
   \]

   Therefore the consecutive list

   \[
        H_{\rm safe}(r)=
        \{2,3,\ldots,\binom{2r-3}{r-3}+2\}             \tag{0.3}
   \]

   is unconditionally WLOG for detecting every *occurring nonempty proper*
   shadow in every simple factor.  Its endpoint is `(1/8+o(1))W`; at
   `K=16` it is `2,...,1289`.  Thus the current six widths are a sufficient
   subclass, not an all-factor theorem.  Sharp simple Johnson cycles attain
   the endpoint, and at depth three every individual width `4,...,r+3` is
   uniquely necessary locally.  Extension of those prescribed cycles to
   spanning `rho`-equivariant factors is not proved, so the smallest
   witness-width list for that narrower class remains open.

3. **Opening/splice catalogue.**  Every physical lift cycle can be decoded,
   independently reversed and cut once.  Literal one-cut splicability is
   equivalent to ordering the resulting component endpoint records so that
   consecutive tail/head sets are Johnson adjacent.  It has either a sparse
   directed seam catalogue of at most `Wr^2` variables, or a selector-free
   width-`W` shared-record Waksman encoding of size

   \[
                  O((K+\log W)W\log W).                 \tag{0.4}
   \]

   Neither form enumerates component orders by voltage.  The post-splice
   literal shadow ledger is exact, but cyclic quotient coverage does not by
   itself survive the cuts.  The common compiler remains a separate exact
   condition.

Thus arbitrary successor permutations and voltages have a compact complete
factor catalogue.  What fails is promoting a small fixed shadow-width list,
bounded component templates, or cyclic coverage to a WLOG literal-completion
theorem from gauge and the local factor laws alone.  For spanning
`rho`-equivariant factors the minimum complete width list is left explicit as
an open narrower question below.

## 1. The smallest fixed physical factor catalogue

Fix representatives `U_i`, `i in [N]`, of the middle-owner rotation
orbits.  The action is free because a nontrivial rotation orbit length
dividing `2r-1` cannot divide either old rank `r` or `r-1`.

Define the directed dart set

\[
 A_K=\{(i,j,p):U_i\sim\rho^pU_j,\ p\in\mathbb Z_n\}.    \tag{1.1}
\]

Reversal sends `(i,j,p)` to `(j,i,-p)`.  It has no fixed point: a fixed
dart would have `i=j` and `2p=0`, hence `p=0` because `n` is odd, contrary
to strict Johnson adjacency.  Put

\[
                         E_K=A_K/(a\sim\bar a).          \tag{1.2}
\]

For `e in E_K`, let `m_i(e)` be zero, one, or two according as its quotient
edge is not incident with owner `i`, is a nonloop incident with `i`, or is a
loop at `i`.

### Theorem 1.1 (exact undirected component catalogue)

The `rho`-invariant spanning simple two-factors of `J(K,r)` are in bijection
with `y in {0,1}^{E_K}` satisfying

\[
                    \sum_{e\in E_K}m_i(e)y_e=2
                    \qquad(i\in[N]).                    \tag{1.3}
\]

Moreover

\[
                    |A_K|=Nr^2,\qquad |E_K|=Nr^2/2.     \tag{1.4}
\]

#### Proof

The action on physical Johnson edges is free.  A rotation fixing an
unordered edge either fixes both endpoints, contradicting vertex freeness,
or swaps them, which would give an element of order two in an odd-order
group.

Every selected nonloop orbit contributes one incident edge at each lift of
each endpoint owner.  A quotient loop represented by
`U_i -- rho^p U_i` contributes the two neighbours with phases `+p` and
`-p`; they are distinct because `p!=0` and `n` is odd.  Thus (1.3) is
exactly physical degree two.  Conversely every invariant factor is a union
of full free edge orbits and satisfies these quotient degrees.

Each fixed physical rank-`r` owner has Johnson degree
`r(K-r)=r^2`.  Freeness and the fixed section give one unique dart for each
neighbour.  Summing over the `N` tails and quotienting by fixed-point-free
reversal proves (1.4).  QED.

### Theorem 1.2 (global minimality for even `r`)

If `r` is even, `E_K` decomposes into `r^2/2` supports satisfying (1.3).
Consequently every edge orbit occurs in some equivariant factor, and no
proper subset of `E_K` contains every factor.

#### Proof

The quotient edge multigraph is `r^2=2k` regular, counting a loop twice.
Orient an Euler tour in every connected component.  Every quotient vertex
then has indegree and outdegree `k`; a loop contributes one to each.  Split
each vertex into a left tail and right head.  The oriented edges form a
`k`-regular bipartite multigraph, which decomposes by repeated Hall matching
into `k` perfect matchings.  Each matching selects one incoming and one
outgoing edge at every owner and hence satisfies weighted degree two.
The matchings partition `E_K`, so every edge orbit belongs to a factor.
QED.

For odd `r`, (1.3) remains a complete fixed catalogue, but global
inclusion-minimality is exactly the union of supports of its feasible
solutions.  Equality with all of `E_K` is not asserted.

Here “gauge-fixed” means that the free choice of one representative in each
owner orbit has been removed by the canonical section.  A single global
coordinate multiplier is an additional coherent symmetry of the *whole*
factor.  Theorem 1.2 does not claim that `27,456` remains minimal after
quotienting complete feasible factors by that global symmetry; selecting one
edge representative from each global orbit independently would be unsound
because the multiplier cannot vary by component or edge.

At `K=16`, `r=8`, `N=858`; hence the globally minimal catalogue has
`27,456` edge variables and `858` rows, including `28` quotient loops with
coefficient two.  The loop number is imported from the independently
replayed quotient census in
`MATH_AUDIT_K16_CT_RECONCILIATION_AND_QUOTIENT_FACTOR_20260729.md`.

## 2. Oriented successor and compact SAT forms

If chronology is needed, orient every decoded physical cycle
equivariantly.  Equivalently choose `x in {0,1}^{A_K}` with one outgoing and
one incoming dart per owner and

\[
                         x_a+x_{\bar a}\le1.             \tag{2.1}
\]

The unique selected outgoing dart gives

\[
             F(i,s)=(\sigma(i),s+p_i).                  \tag{2.2}
\]

This is the arbitrary-successor/arbitrary-voltage normal form.  For a
`sigma`-cycle `C`,

\[
 v_C=\sum_{i\in C}p_i\pmod n,\qquad
 g_C=\gcd(n,v_C),\qquad
 L_C=|C|n/g_C.                                           \tag{2.3}
\]

It lifts to `g_C` physical cycles of length `L_C`.  Changing section adds a
coboundary to the `p_i` and preserves `v_C`; no component-voltage selector
is involved.

When `r` is even, the oriented dart support is globally irredundant as well:
every underlying edge orbit extends by Theorem 1.2, and either dart direction
is obtained by orienting the physical-cycle orbit containing that edge in
the prescribed direction before equivariant transport.  Thus all `Nr^2`
darts occur among oriented factors, even though the undirected base is the
smaller representation.

There are two exact SAT bases.

* The sparse form has `Nr^2` dart bits, `2N` exact-one rows, and reverse-pair
  rows.  At `K=16` this is `54,912` dart bits.
* The implicit form uses one width-`N` Waksman successor and `N` bounded
  phase residues.  With the current two-sided switch count `S(N)`, a
  conservative pre-comparator variable bound is

  \[
      S(N)+2(2K+b)S(N)+Nb+2nbN,
      \qquad b=\lceil\log_2n\rceil.                     \tag{2.4}
  \]

  At `K=16`, `S(858)=8078` and (2.4) is `696,086`.

The sparse base is smaller at `K=16`; the Waksman base is useful when many
state, root, phase, and window fields must follow the same symbolic
successor.  Any topology-oblivious router realizing all `N!` permutations
needs at least `ceil(log_2(N!))` controls, so `O(N log N)` controls are
asymptotically optimal for that promise.  This is not a lower bound on the
unknown number of locally legal factor permutations.

Component length and voltage may be decoded after selection.  If solver
predicates need them, root/order/phase-potential fields routed through the
same controls record `(ell_C,v_C)` in polynomial size.  Prescribing one
partition, bounding all component lengths, or requiring all voltages one is
a sufficient subclass, not gauge normalization.

## 3. Why bounded component templates are not WLOG

Section gauge preserves `sigma`, and global coordinate relabelling only
conjugates it.  Hence both preserve the quotient cycle-length multiset.
Any catalogue partitioning the owner slots into fixed blocks of size at
most `B` excludes every factor having a quotient cycle longer than `B`.

The retained `K=16` equivariant physical Hamilton factor has one quotient
cycle of length `N=858`; therefore every such block catalogue with
`B<858` is a strict subclass.  Explicitly listing all possible labelled
one-component orders would require `(N-1)!` directed cyclic templates
before phases.  The symbolic successor network is the compact replacement
for that enumeration.

This does not conflict with the local catalogue `E_K`: fixed edge-orbit
templates plus the global degree rows encode arbitrarily long components
implicitly.

## 4. Complete proper-shadow width bound

Let `A_0,...,A_(w-1)` be a one-pass interval of distinct consecutive states
in a simple Johnson component.

### Theorem 4.1 (minimal witness width)

If this interval is endpoint-minimal with upper union `T`, `|T|=r+q`, or
lower intersection `L`, `|L|=r-q`, then (0.2) holds.

#### Proof

For an upper witness put `D_i=T\setminus A_i`.  These are distinct
`q`-subsets of the `(r+q)`-set `T`, consecutive ones are Johnson neighbours,
and

\[
                    \bigcap_iD_i=\varnothing.           \tag{4.1}
\]

Each step introduces at most one new union coordinate, giving `w>=q+1`.
Minimality after deleting the last or first state gives tokens

\[
 x\in\bigcap_{i=0}^{w-2}D_i,\qquad
 y\in\bigcap_{i=1}^{w-1}D_i.                            \tag{4.2}
\]

They are distinct by (4.1).  Every internal `D_i` contains both, and there
are only `binom(r+q-2,q-2)` distinct `q`-subsets with that property.  Thus
`w-2` is at most this number.  At `q=1`, two distinct singleton deletion
sets already have empty intersection, so `w=2`.

For a lower witness put `D_i=A_i\setminus L`.  These are distinct
`q`-subsets of the `(r+q)`-set `[2r]\setminus L`, and the same proof applies.
QED.

Every witness contains an endpoint-minimal subinterval.  Hence the widths

\[
 H_q(r)=\{q+1,\ldots,B_{r,q}\}                           \tag{4.3}
\]

are WLOG for detecting every occurring proper depth-`q` shadow.  Their union
over `1<=q<=r-1` is exactly (0.3).  The full target `[2r]` is automatic after
the components are spliced into a path through every middle owner: the union
of the whole path is `[2r]`.  It need not consume a pre-splice cyclic width.
At every listed width the one-pass activity bit still suppresses components
shorter than that width; periodically repeating a short cycle is never a
literal witness.

At `K=16` the depth endpoints are

\[
                 2,\ 3,\ 11,\ 47,\ 167,\ 497,\ 1289.   \tag{4.4}
\]

Thus the common safe list has `1288` widths and `858*1288=1,105,104`
quotient start--width objects before target routing.  It is exact and
selector-free, but no longer the fixed-width near-linear regime.

### Theorem 4.2 (sharp local width obstruction)

For every `2<=q<=r-1`, a simple Johnson cycle has a rank-`r+q` target whose
only cyclic witnessing interval has width `B_(r,q)`; the lower dual also
holds.  For `r>=4`, at depth three every individual width
`4,...,r+3` is uniquely necessary for some simple Johnson cycle.

#### Proof sketch with the exact construction

Write `T={x,y} dotcup Omega`, `|Omega|=r+q-2`.  List all `(q-2)`-subsets
`E_1,...,E_s` of `Omega` in fixed-weight Gray order and define deletion sets

\[
 D_0=\{x\}\cup E_1\cup\{a\},\quad
 D_i=\{x,y\}\cup E_i,\quad
 D_{s+1}=\{y\}\cup E_s\cup\{b\},                       \tag{4.5}
\]

where `a notin E_1`, `b notin E_s`.  Consecutive sets share `q-1`
coordinates.  Every proper prefix has durable token `x`, every proper suffix
has durable token `y`, and the complete intersection is empty.  Therefore
`A_i=T\setminus D_i` has the unique union witness of width
`s+2=B_(r,q)`.  Close the path through states containing an outside
coordinate; those states contaminate every other possible union interval.
Complementing the construction gives the lower dual.

The required Gray order follows by the reflected recursion
`G(R,k)=G(R-1,k); rev(G(R-1,k-1))+{R}`.  Its two blocks partition the
`k`-subsets, and the induction endpoints differ by one exchange, so every
join is a Johnson edge.

For a prescribed depth-three width `h`, take `s=h-2`, choose distinct
`u_1,...,u_s` in an `(r+1)`-set (so `2<=s<=r+1`), and use the triples

\[
 D_0=\{x,u_1,u_2\},\quad D_i=\{x,y,u_i\},\quad
 D_{s+1}=\{y,u_s,u_{s-1}\};                            \tag{4.6}
\]

the same durable-token argument and outside-coordinate closure apply.
QED.

The sharp cycles are not proved extendible as prescribed components of a
spanning `rho`-equivariant factor.  Therefore (0.3) is an unconditional safe
upper catalogue, while endpoint minimality for the narrower equivariant
spanning class remains open.  What is proved is that gauge, rerooting, and
reversal cannot justify a dimension-independent bounded list from the local
component laws.  In particular the current widths `{2,3,4,6,9,13}` remain
sufficient-only.

## 5. Exact factor-level surgery

Let selected darts `a=(i,j,p)` and `b=(k,l,q)` be replaced by legal darts
`a'=(i,l,p')`, `b'=(k,j,q')`, without selecting a reverse pair.  The
one-in/one-out rows are preserved, so another factor results.  If the old
darts lie on distinct quotient cycles of voltages `v_1,v_2`, the cycles
merge with voltage

\[
                 v'=v_1+v_2-p-q+p'+q'\pmod n.           \tag{5.1}
\]

The joined quotient component has one physical lift exactly when `v'` is a
unit.  If the darts lie on one quotient cycle, the usual two path sums plus
`p',q'` give the two split voltages.  This is factor-level alternating
surgery; it is not yet a literal opening of all physical lift cycles.

Only starts in

\[
              \bigcup_{t=0}^{w-2}\sigma^{-t}(D)         \tag{5.2}
\]

can have their raw width-`w` word changed when the successors/phases change
at `d=|D|` tails.  Hence at most `d(w-1)` quotient occurrences change.
If a changed physical component becomes shorter than the audited width,
its one-pass activity may change at every start; this is the exact exception
to the locality bound.

## 6. Physical decoder and one-cut literal splice

Let a quotient cycle be

\[
 C=(i_0,\ldots,i_{\ell-1}),\qquad
 P_j=\sum_{t<j}p_{i_t},\qquad v=P_\ell.
\]

Put `g=gcd(n,v)` and `m=n/g`.  For every coset representative `h` of the
subgroup generated by `v`, one physical cycle is

\[
 \Gamma_{C,h}=
 \bigl((i_j,h+qv+P_j):0\le q<m,\ 0\le j<\ell\bigr),     \tag{6.1}
\]

in lexicographic `q,j` order.  These `g` cycles are disjoint, have length
`m ell`, and exhaust the lift.

Reverse each physical cycle independently if desired, cut one directed
edge `e_Gamma -> H(e_Gamma)`, and write its opened path from
`H(e_Gamma)` to `e_Gamma`.

### Theorem 6.1 (decode/open/splice equivalence)

A linear Johnson ordering of all `W` middle states obtained by opening the
factor once in every physical component is equivalent to:

1. one orientation and one cut per physical cycle;
2. one ordering of those cycles; and
3. a Johnson adjacency from each opened path tail to the next path head.

The concatenation of the opened paths is the decoded ordering.

#### Proof

Removing one edge from a simple cycle gives a path, with its two possible
orders.  The cycles partition all physical middle states.  Their
concatenation is a Johnson path exactly when every consecutive endpoint pair
is adjacent.  Conversely any one-cut concatenation uniquely recovers these
data after choosing the first component.  QED.

### Theorem 6.2 (two exact compact splice catalogues)

After the factor is fixed, literal one-cut splicability has either of the
following exact formulations.

* **Sparse seams.**  Choose one root/cut per physical cycle.  Use a variable
  only for a directed Johnson adjacency from a cut tail to another component
  head.  There are at most

  \[
                              Wr^2                       \tag{6.2}
  \]

  candidates.  Indegree/outdegree at most one, `c-1` selected seams for `c`
  components, and a strict component-order potential are equivalent to one
  directed Hamilton path through the components.

* **Shared records.**  Attach to each physical root the inseparable record
  `(active, root address, cut-tail address, head set, tail set)`, pad with
  inactive state records, and route all `W` records through one Waksman
  network.  Force active records to a prefix and require consecutive active
  tail/head sets to be Johnson adjacent.  If

  \[
             q_R=1+2\lceil\log_2W\rceil+2K,             \tag{6.3}
  \]

  this uses `S(W)` controls, at most `2q_R S(W)` record mux variables, and
  `O(KW)` guarded adjacency comparators.  Inverse-routing each next-root
  record and passing it to the cut tail recovers the actual global successor
  without seam selectors; the unique last-active record routes `bottom`, and
  fields on inactive outputs are ignored.  The total ordering scale is
  (0.4).

Both formulations contain every independent lift orientation, cut, and
component order, regardless of quotient voltage.  The sparse formulation is
often smaller at `K=16`; the record formulation is the topology-oblivious
selector-free alternative.  Neither is claimed circuit-minimal.

## 7. Exact cut/seam shadow ledger

Fix `1<=w<=W` and suppose every physical component has length at least `w`.
Let `mu_w^pm(S)` be the cyclic multiplicity of literal label `S` in
the old factor, `L_(e,w)^pm(S)` the occurrences destroyed by cut `e`, and
`G_(a,w)^pm(S)` the occurrences created across seam `a`, for lower
intersections or upper unions respectively.

### Theorem 7.1 (old minus cuts plus seams)

For the spliced linear middle word `T`,

\[
 m_{T,w}^\pm(S)=\mu_w^\pm(S)
       -\sum_eL_{e,w}^\pm(S)+\sum_aG_{a,w}^\pm(S).       \tag{7.1}
\]

Every cut destroys exactly `w-1` occurrences and every seam creates exactly
`w-1`; with `c` components,

\[
 \sum_Sm_{T,w}^\pm(S)
 =W-c(w-1)+(c-1)(w-1)=W-w+1.                            \tag{7.2}
\]

#### Proof

For `w=1`, all cut-loss and seam-gain families are empty and the identity is
immediate.  Assume `w>=2` below.

A cyclic width-`w` occurrence survives exactly when its `w-1` transition
edges avoid the selected cut.  A seam supplies one interval for every split
`1,...,w-1`.  Under the length hypothesis, a width-`w` interval cannot cross
two seams, so internal survivors and seam intervals partition the literal
windows.  QED.

Multiplicity is essential: deleting one provider does not create a hole if
another survives or a seam recreates it.  Summing by rotation orbit is not
enough after arbitrary physical cuts.

If a component is shorter than `w`, periodically repeating it is invalid and
(7.1) must not be used seam-by-seam.  Instead construct the partial global
successor `G` of the assembled Hamilton path and declare a start active
exactly when `G^j x` exists for `0<=j<w`.  Successive guarded payload passes
then give the exact `W-w+1` literal windows.  For a fixed declared width set,
their physical target cover remains polynomial and selector-free, but it is
not quotient-orbit coverage any longer.

## 8. Compiler composition and the final boundary

Let `T` be the decoded Johnson path.  A satisfying exact compiler antecedent
`A` with `D^dA=T`, literal nonempty letters, and every required target
occurrence yields a literal contiguous-OR word.  If one additionally imposes
the one-core condition `DA=DP` for the maximal erosion `P`, the known
core-Hall inequalities are necessary and sufficient inside that
architecture.  Failure of one-core Hall is not a lower bound against the
unrestricted compiler.

The following are WLOG:

1. the canonical physical edge catalogue (1.3);
2. arbitrary successor permutation and dart phases after orientation;
3. decoding component length and voltage rather than selecting a type tuple;
4. independent physical-cycle orientations and one-cut splice data;
5. the safe proper-shadow widths (0.3), if all occurring shadows are to be
   detected by an explicit width list.

The following remain sufficient-only or open:

1. prescribed components, bounded component length, or all voltages one;
2. the six-width `K=16` shadow catalogue as an all-factor statement;
3. endpoint sharpness of (0.3) inside spanning equivariant factors;
4. quotient-orbit coverage after non-equivariant physical cuts;
5. residence-safe splice existence and exact unrestricted compiler
   feasibility.

The decisive answer is therefore two-tiered.  The universal factor
catalogue is fixed, exact, and at `K=16` globally minimal under fixed labels.
No dimension-independent bounded width is WLOG for unrestricted simple
component chronologies, and no such conclusion follows from gauge/local laws
for the spanning equivariant subclass.  The exact unconditional safe list
for that subclass grows to order `W`; whether a smaller list is complete
there remains open.  Literal decoding still requires cut-aware physical
coverage and the common compiler.
