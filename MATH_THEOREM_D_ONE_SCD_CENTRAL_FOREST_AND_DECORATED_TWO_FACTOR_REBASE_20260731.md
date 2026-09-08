# One-SCD central forests, endpoint rerooting, and the decorated-2-factor rebase

Date: 2026-07-31  
Status: exact central equivalences and product interface; one positive
`B_4 -> B_6` lift and one sharply scoped next-step obstruction; no all-`m`
construction and no full-word theorem are claimed

## 0. Verdict

There are now two distinct sufficient routes to Catalan Linear Matching.

1. **One-SCD route.**  Freeze the nonmiddle skeleton of one symmetric-chain
   decomposition of `B_(2m)`.  Its central flags define a graph `J` on the
   middle layer.  The exact target is that `J` be a linear forest.  The
   initially proposed condition that the native opposite-corner map `g` be
   injective and acyclic is a convenient endpoint-rooted normal form, but it
   is not necessary for a fixed SCD: two native arcs may meet legally at a
   radius-zero singleton.  Every linear central graph can, however, be
   rerooted with the entire nonmiddle skeleton fixed so that `g` becomes
   injective and acyclic.

2. **Decorated-2-factor route.**  A spanning 2-factor of `ML(2m-1)` with
   globally exact selected turn palettes, componentwise alternating shore
   marks, and cycle-rank-zero trace on every component already supplies the
   perfect diamond matching and the `Cat_m`-path forest.  A marked component
   must contain an unselected occurrence; a wholly marked component contributes
   two rail cycles and is forbidden.  Hamiltonicity and component merging are
   not part of this minimal existential target.

These are different parametrized subclasses of the same central conclusion.
Neither parametrization is presently known to contain the other.  In
particular, the binary trace conditions of the second route must not be
inserted into the SCD criterion, and an arbitrary one-SCD forest is not known
to have a Middle-Levels 2-factor support.

The ordinary chainwise `B_(2m) x B_2` product has a complete normalized
interface.  Its product graph `Lambda(S)` can be written explicitly, and a
central rerooting exists if and only if `Lambda(S)` is a path forest.  This
gives a genuine noncanonical `B_4 -> B_6` step.  It does not iterate on the
resulting displayed `B_6` state: an unavoidable `2,1,2,1` radius pattern
creates a degree-three vertex at the next product.  A different `B_6`
skeleton or a nonlocal resolver remains open.

The corrected `ML(7)` incidence-hex theorem is consistent with this
hierarchy.  It proves a positive finite repair and an exact transparent
transfer rule, but transparency and a gluing tree belong to a stronger
recursive certificate, not to the minimal decorated-2-factor statement.

Everything below concerns the central Catalan matching only.  Residence,
deeper shadows, sockets/voltage, and the integral compiler remain separate.

## 1. The central graph of one SCD

Put

\[
 W=\binom{2m}{m},\qquad
 N=\binom{2m}{m-1}=m\operatorname {Cat}_m,\qquad
 K=\operatorname {Cat}_m=\frac{W}{m+1}.
\tag{1.1}
\]

Let `S` be an SCD of `B_(2m)`.  Every one of its `W` chains has one
rank-`m` member.  Exactly `N` chains have positive radius and exactly `K`
are rank-`m` singleton chains.  Write

\[
 \mathcal A=\{\hbox{middle members of positive-radius chains}\},
 \qquad
 \mathcal E=\{\hbox{singleton middle members}\}.
\tag{1.2}
\]

For `X in A`, its central flag is

\[
 R_X\subset X\subset U_X,
 \qquad |R_X|=m-1,\qquad |U_X|=m+1.
\tag{1.3}
\]

There are unique distinct coordinates `alpha_X,beta_X` with

\[
 X=R_X+\alpha_X,\qquad
 U_X=X+\beta_X.
\tag{1.4}
\]

The opposite middle corner and the undirected central edge are

\[
 g(X)=R_X+\beta_X=X-\alpha_X+\beta_X,
 \qquad e_X=\{X,g(X)\}.
\tag{1.5}
\]

Every rank-`m-1` set and every rank-`m+1` set occurs in exactly one
positive-radius chain.  Hence

\[
 X\longmapsto R_X,qquad X\longmapsto U_X
\tag{1.6}
\]

are bijections onto their respective ranks.  The `N` pairs `(R_X,U_X)`
are therefore a perfect matching of the Boolean diamond graph.

Let `J_S` be the graph on all `W` middle sets with the `N` edges `e_X`.
The edges are loopless and distinct.  A reverse pair
`g(X)=Y,g(Y)=X` would give the same lower intersection and upper union to
two SCD chains, contrary to (1.6).

More invariantly, delete the rank-`m` members from the SCD and retain the
`N` flags `R subset U`.  This is the **nonmiddle skeleton** `Sigma`.  Its
central graph `J_Sigma` has the edge joining the two rank-`m` sets between
each flag.  It does not depend on which corner is later installed in that
chain.

Because a completion orients every edge out of a distinct chosen middle
member, every component of `J_Sigma` has at most one cycle.  Thus it is a
pseudoforest.  Since it has `W` vertices and `W-K` edges, it has exactly
`K` tree components; it may additionally have unicyclic components.

## 2. Native ordered four-transversals and the exact fixed-SCD correction

### Theorem 2.1 (native owner orientation)

For the owner `R_X`, order the two new coordinates as

\[
 (a_{R_X},b_{R_X})=(\alpha_X,\beta_X).
\tag{2.1}
\]

Then

\[
 L_{R_X}=R_X,\quad U_{R_X}=U_X,\quad
 T_{R_X}=X,\quad H_{R_X}=g(X).
\tag{2.2}
\]

This owner-fixed family is an ordered four-transversal whose directed
physical graph is a forest if and only if

\[
                  g\text{ is injective and has no periodic orbit}.
\tag{2.3}
\]

Under (2.3), the physical graph is the disjoint union of exactly `K`
directed paths, with isolates allowed.

#### Proof

The lower and upper maps in (2.2) are bijective by (1.6), and the tail map
is injective because the SCD uses each middle set once.  The only remaining
transversal condition is injectivity of the head map, which is exactly
injectivity of `g`.  A directed cycle is exactly a periodic orbit of `g`.
The graph then has indegree and outdegree at most one and is acyclic, hence
is a path forest.  Its component count is

\[
                  W-N=K.
\tag{2.4}
\]

This proves the claim.  \(\square\)

The injectivity in Theorem 2.1 is a condition on the **native ordering**,
not on the underlying diamond matching.

### Theorem 2.2 (exact fixed-SCD path criterion)

For a middle set `Y`, put

\[
                         d^-(Y)=|g^{-1}(Y)|.
\tag{2.5}
\]

The undirected central graph `J_S` is a linear forest if and only if

\[
 \begin{array}{ll}
 d^-(Y)\le1,&Y\in\mathcal A,\\
 d^-(Y)\le2,&Y\in\mathcal E,
 \end{array}
 \qquad\text{and}\qquad
 g\text{ has no periodic orbit}.
\tag{2.6}
\]

When (2.6) holds, `J_S` has exactly `K` path components.

#### Proof

The absence of reverse pairs gives the exact degree identity

\[
             \deg_{J_S}(Y)=\mathbf1_{\mathcal A}(Y)+d^-(Y).
\tag{2.7}
\]

Thus the first two conditions of (2.6) are exactly maximum degree at most
two.  If an undirected cycle has `s` vertices, its `s` distinct edges must
have `s` distinct owners among those same vertices, because every owner
supplies only one edge.  Hence every cycle vertex owns its outgoing cycle
edge and the cycle is a directed periodic orbit.  The converse is immediate.
Finally, an acyclic graph with `W` vertices and `W-K` edges has `K`
components.  \(\square\)

The extra allowance `d^-(Y)=2` on `E` is real: two paths may meet at a
radius-zero singleton and make one undirected path with the arrows pointing
toward its internal vertex.

## 3. Endpoint-reroot normalization

### Theorem 3.1 (fixed-skeleton normalization)

Let `Sigma` be a completable nonmiddle SCD skeleton.  The following are
equivalent.

1. `J_Sigma` is a disjoint union of paths.
2. `Sigma` has a completion whose native `g` is injective and acyclic.

Moreover, the completion in 2 can be obtained from any completion of
`Sigma` under item 1 by changing only rank-`m` members.

#### Proof

The implication `2 -> 1` is Theorem 2.1.  Conversely, orient each
nontrivial path of `J_Sigma` toward either endpoint.  For every flag

\[
                         R\subset U,
\tag{3.1}
\]

its edge is `{R+a,R+b}`.  Replace the rank-`m` member of that nontrivial
chain by the oriented tail of this edge.  Both possible members are between
the same `R` and `U`, so the chain remains saturated and symmetric and all
of its nonmiddle members are unchanged.

The oriented tails are exactly all middle vertices except one terminal per
path.  Use those `K` omitted terminals as the singleton chains.  The chains
therefore still partition rank `m`, and every other rank was untouched.
The new head map is the chosen path orientation, so it is injective and
acyclic.  \(\square\)

Thus the exact one-SCD target is completion-independent:

\[
 \boxed{\quad J_\Sigma\text{ is a }\operatorname {Cat}_m\text{-path forest}.
        \quad}
\tag{3.2}
\]

Native injectivity merely says that the singleton root chosen in each path
is an endpoint.  An internal singleton root produces the legal two-incoming
configuration of Theorem 2.2.

### Corollary 3.2 (endpoint divergence)

In an injective-acyclic normalization, let `B` be the set of path beginnings
and `E` the singleton terminal set.  For coordinate `i`, put

\[
 b_i=|\{B\in\mathcal B:i\in B\}|,
 \qquad e_i=|\{E\in\mathcal E:i\in E\}|.
\tag{3.3}
\]

Let `A_i` and `D_i` count physical arcs inserting and deleting coordinate
`i`.  Then

\[
 A_i+D_i=K,\qquad A_i-D_i=e_i-b_i,
\tag{3.4}
\]

and hence

\[
 A_i=\frac{K+e_i-b_i}{2},\qquad
 D_i=\frac{K-e_i+b_i}{2}.
\tag{3.5}
\]

Indeed the first identity is the forced diamond marginal

\[
 \binom{2m-1}{m}-\binom{2m-1}{m-2}=K,
\tag{3.6}
\]

and the second telescopes membership from all tails
`M-E` to all heads `M-B`.  This explains why the paired-SCD parity
obstruction does not apply: a paired cycle factor has `B=E`, whereas a path
forest may export the parity discrepancy through different endpoint banks.

## 4. The smallest exact examples

Write subsets of `[4]` as digit strings.  The SCD

\[
\begin{aligned}
 &\varnothing<1<12<123<1234,\\
 &2<23<234,\qquad3<34<134,\qquad4<14<124,\\
 &13,\qquad24
\end{aligned}
\tag{4.1}
\]

has

\[
 g(12)=g(34)=13,qquad g(23)=g(14)=24.
\tag{4.2}
\]

Its native head map is not injective, but its central graph is

\[
             12-13-34\qquad\dot\cup\qquad23-24-14,
\tag{4.3}
\]

so it already gives the required two-path physical lift.

Theorem 3.1 normalizes (4.1) to

\[
\begin{aligned}
 &\varnothing<1<12<123<1234,\\
 &2<23<234,\qquad3<13<134,\qquad4<24<124,\\
 &14,\qquad34,
\end{aligned}
\tag{4.4}
\]

with directed paths

\[
                     12\to13\to34,
 \qquad              23\to24\to14.
\tag{4.5}
\]

There is also a short classification at `m=2`.  Identify a lower singleton
`i` with the upper triple omitting `pi(i)`.  Containment says
`pi(i) != i`, so the outer flags are indexed by derangements in `S_4`.
A derangement of type `(2,2)` gives one `C_4` and two isolates; a 4-cycle
gives two `P_3`'s.  Consequently the six good central skeletons are one
coordinate-conjugacy class.

## 5. Exact `B_(2m) x B_2` product interface

Let a parent chain be

\[
 C=(c_0<c_1<\cdots<c_{2d}),
 \qquad |c_i|=m-d+i.
\tag{5.1}
\]

For `1<=i<=2d-1`, define its alternate same-rank corner

\[
                 \widehat c_i
 =c_{i-1}\cup(c_{i+1}\setminus c_i).
\tag{5.2}
\]

Add new coordinates `a,b`.  In a given parent-chain box choose phase
`p in {a,b}` and let `q` be the other coordinate.  The underlying central
graph contributed by the standard boundary-peeling product has the
following edges; tags denote union with the displayed new coordinates.

\[
\begin{array}{c|l}
d\ge2
 &c_{d+1}-\widehat c_{d+1},\\
 &c_d+p-(\widehat c_d+p),\quad
  c_d+q-(\widehat c_d+q),\\
 &c_{d-1}+ab-(\widehat c_{d-1}+ab);\\[1mm]
d=1
 &c_2-(c_1+p),\\
 &c_1+p-(c_0+ab),\quad
  c_1+q-(\widehat c_1+q);\\[1mm]
d=0
 &c_0+a-(c_0+b).
\end{array}
\tag{5.3}
\]

Let `Lambda_p(S)` be the union of (5.3) over the parent chains, allowing
the phase to be chosen chainwise.

### Theorem 5.1 (normalized product criterion)

The standard product nonmiddle skeleton has a completion with injective,
acyclic central map if and only if

\[
                         \Lambda_p(\mathscr S)
                 \text{ is a linear forest}.
\tag{5.4}
\]

#### Proof

Writing the four boundary-peeling child chains in each rectangle and taking
their central flags gives exactly (5.3).  This graph is independent of the
choice of central owners in the child completion.  Necessity follows from
Theorem 2.1, and sufficiency is precisely the fixed-skeleton rerooting of
Theorem 3.1.  \(\square\)

Theorem 5.1 is the strongest noncircular induction lemma obtained here: it
reduces the product step to an explicit degree-and-cycle test before any
middle roots are chosen.

### Proposition 5.2 (raw-owner product no-go)

The inherited raw owner orientation of the standard product is never both
injective and acyclic for `m>=2`, even with a separate `a/b` phase in every
parent-chain box.

#### Proof

Let `P` be the rank-`m-1` members `c_(d-1)` of chains of radius at least two,
and let `E` be the lower endpoints of radius-one chains.  They partition the
parent rank `m-1`.  For `Z=c_(d-1) in P`, let `h(Z)` be the other rank-`m-1`
corner between

\[
                         c_{d-2}<Z<c_d.
\tag{5.5}
\]

The raw child heads on the `ab` rail are `h(P)+ab`, together with every
`E+ab`; the latter family is phase-independent.  Raw injectivity would force
`h` injective and `h(P)` disjoint from `E`, hence `h(P)=P`.  The associated
child arcs then permute the nonempty set `P+ab` and contain a directed cycle.
At `m=2`, `P` is a singleton and injectivity already fails because
`h(Z)!=Z`.  \(\square\)

This proposition is not a skeleton no-go: rerooting can remove a native head
collision when (5.4) holds.

### Proposition 5.3 (local product branch)

Suppose a parent central edge owned by a chain of radius at least two ends,
in the chosen orientation, at the center `X` of a radius-one chain.  Then
`Lambda_p(S)` has degree at least three, independently of the phase choices.

#### Proof

The deep edge has a copy on both one-coordinate rails.  On the phase rail
chosen by the radius-one box, (5.3) gives the two boundary edges through
`X+p`.  The copied deep edge is a third, distinct edge incident with the
same vertex.  \(\square\)

Thus the central path property is not functorial under the standard product.

### Proposition 5.4 (a genuine positive `B_4 -> B_6` step)

Use the endpoint-rerooted `B_4` SCD

\[
\begin{aligned}
 &\varnothing<1<13<134<1234,\\
 &3<23<123,\qquad4<34<234,\qquad2<24<124,\\
 &14,\qquad12.
\end{aligned}
\tag{5.6}
\]

Its directed paths are

\[
                    23\to13\to14,
 \qquad             34\to24\to12.
\tag{5.7}
\]

For the standard product with new coordinates `5,6`, take common phase
`p=5` and `q=6` in every parent-chain box.  Then (5.3) is the following
five-path graph:

\[
\begin{array}{l}
 134-123-235-356-156,\\
 135-145-146-136-236,\\
 234-345-456,\\
 346-246-126-125,\\
 124-245-256.
\end{array}
\tag{5.8}
\]

It has all twenty rank-three vertices, fifteen edges, maximum degree two,
and no cycle.  Theorem 3.1 therefore gives an explicit SCD of `B_6` with
injective acyclic `g` and five physical paths.

This is not an all-dimension recursion.  In the second path of (5.8), the
inherited edge-radius sequence is

\[
                             2,1,2,1.
\tag{5.9}
\]

Either orientation of this path contains a transition `d>=2 -> 1`.
Proposition 5.3 therefore forces a degree-three vertex in the next standard
product.

This obstruction is classification-level for the standard recursion, not a
label accident.  Every good `B_4` skeleton is one of the six conjugate
4-cycle derangements from Section 4 and consists of two `P_3`'s.  Its unique
radius-two edge lies beside a radius-one edge on one path.  A successful
`B_4 -> B_6` product must orient that path in radius order `1,2`; the reverse
order already triggers Proposition 5.3.  The product of the forced `1,2`
piece contains, up to relabelling, the five-vertex subpath

\[
 (v_1+p)-(s+p)-(s+q)-(v_1+q)-(v_0+q),
\tag{5.10}
\]

whose owner-radius sequence is `2,1,2,1`.  Hence **every** successful
standard `B_4 -> B_6` normalization fails under the next standard `B_2`
product, for every endpoint rerooting and every chainwise phase choice.
The standard boundary-peeling recursion with central rerooting can reach
`B_6` but cannot reach `B_8`.

The scope remains important: a different `B_6` SCD, a mixed/mirrored local
resolver, or a cross-parent/nonlocal product surgery is not excluded.

More generally, label every edge of a parent central path by the radius of
its owning nontrivial chain.  A necessary condition for one standard
product step is that the path admit an orientation in which all radius-one
edges form an initial segment.  Otherwise some consecutive pattern
`d>=2,1` invokes Proposition 5.3.  This condition is not sufficient: the
outer rank-turn graphs and cycles elsewhere in `Lambda_p(S)` remain to be
checked by Theorem 5.1.

## 6. What the older SCD obstructions do and do not say

1. The equal-radius product path

   \[
                         Z_0\to Z_1\to\cdots\to Z_{2r}
   \tag{6.1}
   \]

   ending at a singleton is positive for the present route.  It obstructs a
   paired SCD only because a paired construction requires a permutation.

2. Paired-SCD Catalan parity, quartet flux, common-box cycles, cross-box
   mass, and component residues all assume closed/permutation behavior and
   do not refute (3.2).

3. The canonical BTK/GK SCD has acyclic native `g`, but its central lift is
   physically branched.  The alternating middle set

   \[
                         E_m=\{0,2,\ldots,2m-2\}
   \tag{6.2}
   \]

   has degree `m`; hence BTK fails (2.6) for every `m>=3`.  At `m=3` the
   first obstruction consists of two `K_(1,3)` components.  This closes the
   fixed-priority route, not all SCDs.

4. A genuinely relevant Pascal obstruction remains: retaining two complete
   parent Catalan linear matchings in the two one-coordinate sectors forces
   `Cat_m` cross edges.  The induced two-rail excess is

   \[
                 \operatorname {Cat}_m-2\operatorname {Cat}_{m-1}\ge0,
   \tag{6.3}
   \]

   so a cycle is forced.  Any viable recursion must release parent edges and
   carry boundary reachability.  After adding a candidate arc `T -> H`, the
   exact acyclicity test is that the residual core is acyclic and contains
   no path `H leadsto T`.

   The exact `k=15 -> k=16` word now supplies a literal escape from this
   architecture, not a counterexample to the obstruction.  Only the plain
   rail is a complete parent traversal.  The marked rail deletes 49 parent
   states and inserts 49 lower edge facets, so the hypotheses of the
   two-full-parent count are absent.  Section 9 records the exact operator.

Consequently no existing no-go rules out a genuinely noncanonical,
boundary-deficient one-SCD recursion.  What is closed is the canonical
fixed-priority family, the scalar two-full-copy recursion, and the repeated
standard product on the explicit state (5.8).

## 7. Independent audit of the decorated-2-factor reduction

Put `Omega=[2m-1]`.  Let a component of a spanning 2-factor of
`ML(2m-1)` be

\[
 A_0,B_0,A_1,B_1,\ldots,A_{q-1},B_{q-1},A_0,
 \qquad A_i\subset B_i\supset A_{i+1}.
\tag{7.1}
\]

Its lower and upper turn colours are

\[
 \ell_i=A_i\cap A_{i+1},qquad
 u_i=B_{i-1}\cup B_i.
\tag{7.2}
\]

Choose `A`- and `B`-occurrences over all components so that the selected
`u_i` enumerate `binom(Omega,m+1)` once and the selected `ell_i` enumerate
`binom(Omega,m-2)` once.  On each marked component require consecutive
selected occurrences to have opposite shore types.  The unselected
occurrences then have a residual perfect matching: it is unique on a marked
component and has the two alternating phases on an unmarked component.

### Theorem 7.1 (exact supported factor criterion)

Within the diamond catalogue supported by the turns and cross edges of the
fixed 2-factor, the preceding palette, alternation, and residual-phase rows
are necessary and sufficient for a perfect diamond matching.

Its physical lift is a forest if and only if every component has cycle rank
zero.  For the cyclic binary mark word `w` of a component of order `2q`, the
cycle rank is

\[
\beta(w)=
\begin{cases}
0,&w=0^{2q},\\
2,&w=1^{2q},\\
1,&0<|w|_1<2q,\ \,
   \text{every positive zero-run has length }2
   \text{ and every one-run is odd},\\
0,&\text{otherwise}.
\end{cases}
\tag{7.3}
\]

If every `beta(w)=0`, the lift is a spanning forest with exactly `Cat_m`
path components.

#### Proof

The special lower colours containing the added coordinate can only be
served by selected lower turns, and the special upper colours avoiding it
can only be served by selected upper turns.  This forces the two global
bijections.  All remaining occurrences must be matched by factor cross
edges.  Deleting the selected occurrences leaves even paths exactly when
the selected shore types alternate; those paths have unique matchings.
An unmarked even cycle has its two residual phases.  This proves the
supported matching equivalence.

The physical rank-`m` vertices are precisely the `A`-vertices with the added
coordinate and the `B`-vertices without it, so distinct factor components
lift on disjoint vertex sets.  The binary-trace calculation on one component
gives (7.3).  In particular, a wholly marked component gives two rail
cycles; treating its absent zero-runs vacuously is invalid.  When all cycle
ranks vanish, the perfect diamond matching has `W-K` edges on `W` vertices,
so the forest has exactly `K` components.  \(\square\)

This confirms all load-bearing hypotheses in
`MATH_THEOREM_CATALAN_DECORATED_TWO_FACTOR_MINIMAL_TRACE_TARGET_20260731.md`,
including its corrected wholly-marked exclusion.

### Theorem 7.2 (factor connectivity is existentially free)

Any two spanning 2-factors of the same Middle Levels graph differ by a
finite family of alternating closed trails.  Toggling those trails one at a
time preserves degree two.  Hence, from any starting factor, an
alternating-circuit packet reaches an accepting decorated factor if and only
if some accepting decorated factor exists.

#### Proof

Colour the two differences red and blue.  At every vertex their degrees
agree.  Pair unlike half-edges and follow the pairings to obtain edge-disjoint
closed alternating trails.  Each toggle removes and inserts equally many
edges at every visited vertex.  \(\square\)

This theorem is existential.  It gives no bound on the packet and preserves
no residence, shadow, socket, or compiler state along the way.

## 8. The corrected hierarchy and the exact remaining targets

The central implications are

\[
\begin{array}{c}
\text{joint-SDR transparent Hamilton gluing tree}\\
\Downarrow\\
\text{forest-decorated Hamilton cycle}\\
\Downarrow\\
\text{forest-decorated spanning 2-factor}\\
\Downarrow\\
\text{Catalan Linear Matching}.
\end{array}
\tag{8.1}
\]

Only the last implication is the minimal factor-level route.  None of the
reverse implications is known.

The positive `ML(7)` theorem verifies the stronger local transfer rule for
one standard incidence-hex toggle:

* the selected local turn-colour multisets must agree separately on the two
  shores; and
* the retained-fragment boundary mark types must alternate after
  reconnection.

Its exact census has 31 alternating hexes, 16 Hamilton outputs, 10 decorable
outputs, and 6 outputs sharing a forest decoration with the input.  Thus it
both repairs the first gap-Hall counterexample and proves that transparent
preservation is strictly stronger than terminal decorability.  Separate
upper and lower rainbow surjectivity is not enough.

There are therefore two honest all-dimension targets.

### Direct minimal target `D2F_m`

Construct any spanning Middle Levels 2-factor with the two global occurrence
bijections, componentwise shore alternation, no wholly marked component, and
`beta(w)=0` on every component.  No component merge is requested.

The companion exact reduction
`MATH_THEOREM_CATALAN_D2F_FACTOR_FLOW_AND_RELATIONAL_ROOT_20260731.md`
turns this into two concrete interfaces.

* For a proposed perfect diamond matching `M`, form its forced Middle Levels
  support `Theta(M)` from the two factor edges at every same-rail turn and
  the literal factor edge at every cross diamond.  It is factor-resolvable
  exactly when `deg_Theta(v)<=2` and the residual demands

  \[
                       2-\deg_\Theta(v)
  \tag{8.2}
  \]

  are met by a capacity-one bipartite `b`-flow.  Thus direct D2F is
  equivalent to a perfect diamond matching whose physical lift is a forest
  and whose forced support passes this integral flow.  There are no subtour
  or Hamilton rows.

* On a fixed 2-factor, choose one upper-turn occurrence for every upper
  colour.  The exact remaining row is one occurrence-labelled perfect
  matching between the resulting cyclic gaps and the lower turn colours,
  followed by the component trace test (7.3).  Separate turn surjections do
  not imply this gap matching.

### Stronger relational induction target

Propagate the **joint** relation of realizable upper occurrences, lower
occurrences, residual phases, and trace-boundary states under the recursive
factor operations, using natural join and existential projection.  The root
is accepting only when the two palettes are bijective and every closed
component has cycle rank zero.  A fixed transparent decoration and gluing
tree is one sufficient point of this relation, not the whole relation.

This relational composition is now an exact theorem: store boundary factor
degrees, augmented matching degrees, and for every open trace fragment its
two boundary bits, capped zero-run data, one-run parity, homogeneous
`all-zero/all-one/mixed` type, and breaker bit.  Natural join glues literal
fragments, each forgotten vertex must close at its exact degree, and every
sealed component is tested once by (7.3).  The empty-boundary root accepts
if and only if D2F holds for the assembled factor.  What remains open is
nonemptiness with uniformly controlled boundary state, not correctness of
the recurrence.

For the one-SCD route, the corresponding smallest invariant is the
nonmiddle skeleton together with the requirement that `J_Sigma` be a path
forest; for the standard `B_2` lift this is exactly (5.4).  An ordered
four-transversal without radius-compatible half-chain extensions does not
construct such an SCD.

No theorem here proves `D2F_m`, the one-SCD path-skeleton statement, or the
stronger accepting-root relation for all `m`.  Even if one of them is proved,
the full equality `nu(k)=B(k)` still requires the downstream residence,
all-depth shadow, and compiler theorems.

## 9. The shifted-chunk facet operator: the nonflat even-lift target

The exact optimal `k=16` certificate supplies a concrete downstream
odd-to-even operator.  This operator is at the filtered depth-three carrier
level; it is not a cellwise substitution in the source word.

Put

\[
 T=D^3A^{15},\qquad |T|=6435,
\tag{9.1}
\]

where `T` consists of two lower-rainbow Johnson cycles

\[
 C_L=T[0:6390],\qquad C_S=T[6390:6435]
\tag{9.2}
\]

of lengths `6390` and `45`.  In `D^3A16`, the new-coordinate trace is

\[
                         1^{6390}0^{6435}1^{45}.
\tag{9.3}
\]

After filtering by the new coordinate and deleting it from marked states,
the plain subsequence is the four shifted parent chunks

\[
 T[5112:6390]\Vert T[0:5112]\Vert
 T[6426:6435]\Vert T[6390:6426].
\tag{9.4}
\]

The marked subsequence keeps

\[
                         T[5113:6390]\Vert T[0:5109]
\tag{9.5}
\]

and then inserts 49 rank-seven facets.  Equivalently, define the released
parent vertices

\[
 R_V=T[5109:5113]\mathbin{\dot\cup}C_S
\tag{9.6}
\]

and the facet packet

\[
\begin{aligned}
 R_E={}&\{T_i\cap T_{i+1}:5108\le i\le5111\}\\
      &\mathbin{\dot\cup}
        \{X_i\cap X_{i+1}:X_i\in C_S\},
\end{aligned}
\tag{9.7}
\]

where the second family is cyclic.  Then `|R_V|=|R_E|=4+45=49`, the
members of `R_E` are globally distinct, and the marked child deck is

\[
 \{z\cup T_i:T_i\notin R_V\}
 \mathbin{\dot\cup}
 \{z\cup E:E\in R_E\}.
\tag{9.8}
\]

Its rank profile is

\[
 6386\text{ marked rank-nine states}
 \quad\dot\cup\quad
 49\text{ marked rank-eight states},
\tag{9.9}
\]

while the plain deck is all 6435 parent rank-eight states.  Thus the child
is neither a flat marked copy, a complete lower-facet Pascal copy, nor a
strict complement rail.

### Lemma 9.1 (facet-packet substitution)

Let a family consist of vertex-disjoint rank-`r` Johnson cycles and rooted
Johnson paths.  Assume that all lower edge colours over all selected pieces
are distinct.  Replace every cycle vertex by its cyclic incoming edge facet,
and replace every nonroot path vertex by the facet of its incoming edge.
Then:

1. a cycle with `s` vertices becomes a rank-`r-1` Johnson cycle with `s`
   facet vertices;
2. a rooted path with `t` edges contributes `t` rank-`r-1` facet vertices,
   forming a path with `t-1` edges, and replaces exactly its `t` nonroot
   slots;
3. all inserted facets are distinct; and
4. matching every facet to the successor endpoint of its parent edge gives
   a canonical containment bijection from inserted facets to released
   vertices.

#### Proof

Two consecutive facets are distinct codimension-one subsets of their common
rank-`r` middle vertex, so they differ by one exchange.  This proves Johnson
adjacency, including the wraparound pair on a cycle.  Slot counts are the
edge counts stated above.  Global distinctness is a hypothesis, and every
incoming facet is contained in its successor, proving the last assertion.
\(\square\)

The substitution also conjugates all internal interval morphology.  With
incoming facets `E_i=V_(i-1) cap V_i`, for every `1<=a<=b<=t`,

\[
 \bigcap_{i=a}^{b}E_i
   =\bigcap_{j=a-1}^{b}V_j,
\tag{9.10}
\]

and, when `a<b`,

\[
 \bigcup_{i=a}^{b}E_i
   =\bigcup_{j=a}^{b-1}V_j.
\tag{9.11}
\]

The intersection identity is associativity.  For the union identity,
`E_i` and `E_(i+1)` are distinct codimension-one subsets of `V_i`, so their
union is `V_i`; union over consecutive pairs proves (9.11).  The same
identities hold cyclically and commute with adjoining the new top bit.
Thus complete-cycle packets have exact internal intersection conjugacy at
all widths and union conjugacy for blocks of at least two facets.  Singleton
states deliberately change rank.  Packet boundaries and external splices
still need separate interval accounting.

For each old coordinate, the facet trace is the one-step erosion

\[
                       e_i=v_{i-1}\wedge v_i.
\tag{9.12}
\]

Accordingly a nonconstant positive run may shorten by one.  Slot and
interval preservation therefore do not by themselves prove residence.

Dually, if the upper edge colours

\[
                       U_i=V_{i-1}\cup V_i
\tag{9.13}
\]

are distinct, then

\[
 \bigcup_{i=a}^{b}U_i=\bigcup_{j=a-1}^{b}V_j,
\qquad
 \bigcap_{i=a}^{b}U_i=\bigcap_{j=a}^{b-1}V_j\quad(a<b).
\tag{9.14}
\]

Thus a two-sided-rainbow component transports both interval morphologies
internally.  Distinct lower colours alone does not imply the upper premise.

The `k=16` packet is Lemma 9.1 applied to the complete 45-cycle and the
rooted four-edge path

\[
 T_{5108}\to T_{5109}\to T_{5110}\to T_{5111}\to T_{5112}.
\tag{9.15}
\]

### Corollary 9.2 (one-exit-test selector law)

Align slot `i` either with the parent state `V_i` or with the top-marked
incoming facet `z+E_i`.  Inside a constant parent run or facet run, adjacency
is Johnson.  At a `parent -> facet` boundary,

\[
                         E_i\subset V_{i-1},
\tag{9.16}
\]

so replacing the one old coordinate by `z` gives an automatic Johnson
entrance.  At a `facet -> parent` boundary one would need
`E_i subset V_(i+1)`, which is not automatic.  Hence every proper facet run
exports exactly one nonautomatic exit test/port, whereas a whole facet cycle
exports none.  The exit may pass in a particular catalogue.

This is a topology statement about the aligned selector.  Arbitrary chunk
rotations still require their literal endpoint test.  The selector compares
same-rank states `V_i` and `z+E_i`; it is not the filtered marked subsequence
(9.8), which also contains `z+V_i`.  This corollary therefore does not
certify the literal `k=16` seams.

### Corollary 9.3 (automatic facet bank from a central forest)

Any Catalan linear matching path forest has globally distinct lower edge
colours: they are precisely its complete lower diamond palette.  On each
oriented physical path, those colours therefore form the facet path of
Lemma 9.1.  Choosing one root per component gives a canonical slot-preserving
lowered bank for every nonroot vertex.  Its upper edge colours are likewise
the complete upper diamond palette, so the dual identities (9.14) also hold.
Thus every accepted one-SCD forest or corrected D2F lift is intrinsically
two-sided facet-ready; a chosen D2F residual phase still changes the physical
path order and must be exported.

This corollary links the central one-SCD/D2F target to the finite even-lift
anatomy.  It does **not** select which paths or subpaths should be lowered,
order their chunks, or prove that the mixed deck is a derivative of a word.

### Exact surviving recurrence gate

A uniform even lift should carry the following correlated state.

1. A parent Johnson component bank with globally distinct lower colours,
   together with chosen cycle components and rooted path collars.
2. The released vertex set and the facet packet, including their canonical
   containment matching and all cross-piece collision checks.
3. Rotations, cuts, and exterior endpoint types for both the complete plain
   traversal and the boundary-deficient marked traversal.
4. A literal proof that the mixed-rank chronology is `D^d` of an exact-length
   child word and satisfies residence and every accumulated-union shadow.
5. The common-cap/compiler matching after facet insertion.

This is a delete-first, boundary-deficient packet.  Residual physical arcs
must still pass acyclicity and the exact `H`-to-`T` reachability exclusion;
the 49-slot containment matching alone proves none of the downstream rows.
The 45-facet Johnson cycle is a carrier chronology component, not a permitted
cycle in the final Catalan physical forest.

Consequently the correct even target is **shifted traversal plus selected
cycle/path facet substitution**, not flat doubling.  The exact `k=16`
certificate proves this target nonempty once; it does not supply a uniform
choice theorem.

## 10. Source map

The exact ingredients audited here are:

* `MATH_THEOREM_SCD_DIAMOND_GRAPH_AND_STRIP_COMPATIBILITY_20260726.md`;
* `MATH_THEOREM_PAIRED_SCD_PRODUCT_AND_SKELETON_COMPLETION_AUDIT_20260726.md`;
* `MATH_ATTACK_D_FIFTH_WAVE_MULTIFRAME_SCD_SURGERY_20260725.md`;
* `MATH_THEOREM_CATALAN_LINEAR_MATCHING_EXACT_REDUCTIONS_20260731.md`;
* `MATH_THEOREM_CATALAN_ABSTRACT_COLOUR_FOREST_AND_PHYSICAL_LIFT_GATE_20260731.md`;
* `MATH_THEOREM_CATALAN_PASCAL_SECTOR_DETERMINANT_AND_TWO_COPY_NOGO_20260731.md`;
* `MATH_THEOREM_CATALAN_DECORATED_TWO_FACTOR_MINIMAL_TRACE_TARGET_20260731.md`;
* `MATH_THEOREM_CATALAN_D2F_FACTOR_FLOW_AND_RELATIONAL_ROOT_20260731.md`;
* `MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`;
* `MATH_THEOREM_K16_SHIFTED_CHUNK_FACET_SUBSTITUTION_ANATOMY_20260731.md`.
