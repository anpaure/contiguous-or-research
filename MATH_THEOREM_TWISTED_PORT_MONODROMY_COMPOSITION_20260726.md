# Abstract twisted port ledgers, serial monodromy, and the fixed-exterior obstruction

Date: 2026-07-26

Method: pure mathematics only.

## 0. Authoritative correction and point of the theorem

**Correction.**  The serial monodromy algebra below is valid for abstract
middle-levels path ledgers and for genuinely exterior-moving packets.  A
nonidentity twist is **not** a legal substitution inside one ordinary
fixed-exterior minimum-wreath slab.  Every contiguous segment of a wreath
is geodesic.  If the exterior is fixed and a nominal length-`r` slab starts
at `O union P` and ends at `O union (J\tau(P))`, then

\[
 d_J\bigl(O\cup P,O\cup(J\setminus\tau(P))\bigr)
 =|P\cap\tau(P)|.                                    \tag{0.1}
\]

This equals `r` only when `tau(P)=P`.  Thus the earlier reading
"nonidentity twisted slab + later inverse slab gives a literal wreath"
was false in the standard Section-17 interface.  Theorems 2.1--4.2 below
should be read as composition laws **conditional on a physical
exterior-moving realization**, not as a construction of one.

The usual port-substitution theorem requires every local complement path
to join a Dyck port `P` to its own complement `J\P`.  This is sufficient
for replacing one slab independently, but it is stronger than necessary
when several aligned slabs are replaced jointly.

A local path partition may instead join

\[
                    P\quad\hbox{to}\quad J\setminus\tau(P)
\]

for one permutation `tau` of the port labels.  It still owns every local
`X`-state and every local `Y`-colour exactly once.  Its only defect is that
it permutes the row tails.  Several such defects cancel exactly when their
transported product is the identity.

This identifies how local zero monodromy could be removed by a new
boundary-moving trade.  It does not produce that trade.

## 1. Twisted rooted path partitions

Let `J` have size `2r`, let

\[
                  D\subseteq\binom Jr,
       \qquad D\cap\overline D=\varnothing,
       \qquad \overline D=\{J\setminus P:P\in D\},
\]

and let `tau` be a permutation of `D`.

### Definition 1.1

A **`tau`-twisted `D`-port path factor** is a vertex partition of the
middle-levels inclusion graph on

\[
             \binom Jr\ \sqcup\ \binom J{r+1}
\]

into paths

\[
 P=X_0\subset Y_0\supset X_1\subset\cdots\subset
 Y_{r-1}\supset X_r=J\setminus\tau(P),
 \qquad P\in D.                                      \tag{1.1}
\]

The untwisted port factor is the case `tau=1`.

### Proposition 1.2 (the degree ledger determines a twist)

Suppose a spanning simple subgraph of the middle-levels inclusion graph
has degree one at the vertices of `D union Dbar` and degree two at every
other vertex, has no cycle component, every path has one endpoint in
`D` and one endpoint in `Dbar`, and every path has exactly `2r` edges.
Then it is a `tau`-twisted port path
factor for a unique permutation `tau` of `D`.

#### Proof

There are `|D|` path components.  Each contains one endpoint `P in D`
and one endpoint in `Dbar`, uniquely of the form `J\Q` for `Q in D`.
Define `tau(P)=Q`.  Distinct components have distinct endpoints, so `tau`
is bijective.  The total edge count is `2r|D|`; the distance from an
`r`-set to the complement of any `r`-set is at most `2r`, while every
component is an alternating path with its displayed endpoints.  The
assumed path length makes every component have the form (1.1).
Uniqueness of `tau` is immediate.  \(\square\)

The length hypothesis in the final sentence must not be dropped from an
arbitrary degree factor: a shorter path together with a longer path can
have the same total degree ledger.

### Theorem 1.3 (fixed-exterior geodesic obstruction)

Let the left and right exteriors be `O_L,O_R`, disjoint from the local
`2r`-set `J`, and assume the two boundary states have equal total size.
Put

\[
                         e=|O_L\setminus O_R|.
\]

Then

\[
 d_J\bigl(O_L\cup P,
           O_R\cup(J\setminus Q)\bigr)
                    =e+|P\cap Q|.                    \tag{1.2}
\]

Consequently an `r`-step **geodesic** slab with endpoint label
`Q=tau(P)` can exist only if

\[
                         e=|P\setminus\tau(P)|.        \tag{1.3}
\]

For `O_L=O_R`, equation (1.3) forces `tau(P)=P` for every row.

#### Proof

The elements which must be removed when changing the left state into the
right state are the `e` elements of `O_L\setminus O_R` together with the
elements of `P` which also lie in `Q` (those are absent from `J\setminus
Q`).  The two sets are disjoint, giving (1.2).  A length-`r` Johnson path
is geodesic precisely when this distance is `r`; since
`|P\cap Q|=r-|P\setminus Q|`, this is (1.3). \(\square\)

Every segment of a Johnson geodesic is geodesic.  Hence Theorem 1.3 is a
statewise obstruction, not an artifact of row closure or of a missing
ownership equation.  A physical twisted construction must move the
exterior and prove its complete crossing-collar ledger.

## 2. One twisted slab permutes tails

Consider a bundle of ambient rows indexed by `D`.  Assume an aligned slab
has, after removing a common exterior, canonical left and right boundary
states

\[
                         L_P=O_L\cup P,
       \qquad R_P=O_R\cup(J\setminus P).              \tag{2.1}
\]

The pieces of the old rows strictly to the right of the slab will be
called the **right tails** and denoted `T_P`; thus `T_P` begins at `R_P`.

### Theorem 2.1 (abstract twisted single-slab ledger)

Replace the canonical local paths by a `tau`-twisted path factor.  Join
the new local path starting at `L_P` to the old right tail `T_(tau(P))`.
At the level of the abstract two-shore ownership ledger:

1. every displayed boundary-state join is legal;
2. every listed middle owner inside and outside the slab is still used
   exactly once;
3. every local adjacent-union colour is still used exactly once; and
4. the row bundle emerging from the slab is permuted by `tau`.

#### Proof

The new local path from `P` ends at

\[
                     O_R\cup(J\setminus\tau(P))
                         =R_{\tau(P)},
\]

which is exactly the initial state of `T_(tau(P))`.  This proves boundary
join legality in the abstract trace.  A twisted path factor is still a vertex partition of both
local shores, so adjoining the common exteriors preserves the local
`X`- and `Y`-ownership ledgers.  The tails are merely permuted and hence
preserve every ownership ledger outside the slab.  The last assertion is
the definition of the displayed reconnection. \(\square\)

Thus nonidentity local monodromy is not an ownership-ledger defect.  In a
fixed-exterior minimum-wreath application it is nevertheless prohibited
by Theorem 1.3.  Calling the reassembled trace a literal wreath requires a
separate exterior-moving geodesicity theorem.

## 3. Serial composition

Suppose a row bundle passes successively through aligned slabs
`S_1,...,S_k`.  Between `S_i` and `S_(i+1)` the unchanged ambient pieces
identify the exiting port labels with the entering labels by a bijection

\[
                         alpha_i:D_i\longrightarrow D_{i+1}. \tag{3.1}
\]

Let the replacement in `S_i` have local twist `tau_i in Sym(D_i)`.
Transport all twists to the first label set.  Equivalently, follow one
row label through the actual sequence of `alpha`'s and `tau`'s; call the
resulting permutation `Mon`.

### Theorem 3.1 (abstract serial monodromy cancellation)

The jointly reassembled abstract row ledger has the original label closure
if

\[
                              \boxed{\operatorname{Mon}=1.} \tag{3.2}
\]

In a common labelling, where all `alpha_i=1`, this is

\[
                         \boxed{\tau_k\tau_{k-1}\cdots\tau_1=1.} \tag{3.3}
\]

Every listed middle-owner and adjacent-union ledger is exact before imposing
(3.2); equation (3.2) is used only for the final rowwise closure.

#### Proof

Apply Theorem 2.1 successively.  At each slab the local two-shore ledgers
remain exact, and between slabs whole unchanged row segments are merely
permuted.  Therefore all ownership ledgers remain exact after every
stage.  A row starting with label `P` returns to the old closing tail
labelled `Mon(P)`.  It has its original closing boundary for every `P`
if and only if `Mon=1`.  Under (3.2), every reassembled abstract row
closes with the same total length and boundary label as before.  This
proves the ledger statement.  Literal minimum-wreath realizability
additionally requires Theorem 1.3 at every slab and the complete
moving-exterior collar ledger. \(\square\)

### Corollary 3.2 (inverse-packet principle)

If two physically realized exterior-moving slabs admit twists `tau` and
`tau^{-1}`, then their abstract monodromies cancel.  Exact ambient
installation still requires their geodesicity and crossing-collar ledgers.

This is the abstract consumer for an **equal-length path partition** with a
nonidentity endpoint permutation.  In particular, a genuine three-cycle
twist is not an obstruction if an aligned inverse three-cycle can be
supplied later.

The rank-three degree-factor witness in Proposition 7.2 of
`MATH_ATTACK_S_PORT_PATH_FACTOR_HALL_20260726.md` is not yet such an atom:
its five component lengths are `10,6,6,2,6`, rather than all `6`.  It proves
that degree Hall does not control monodromy, but it cannot be inserted into
a fixed-length ambient wreath bundle.  Equal component length remains an
essential hypothesis.

### Corollary 3.3 (finite-order repetition principle)

If one physically realized exterior-moving packet has monodromy `tau` of
order `d`, then `d` serial aligned copies have zero total abstract
monodromy:

\[
                              \tau^d=1.                \tag{3.4}
\]

Thus an inverse-packet theorem is algebraically unnecessary for
bounded-order twists.  A literal construction still has to realize one
transported label through all copies and satisfy Theorem 1.3.
In particular, a three-cycle atom can be closed by three coherently
oriented copies, and an involutory atom by two.

The word *coherently* is load-bearing.  The coordinate embeddings and
exteriors of the copies must identify the port labels so that the physical
monodromies are the same `tau`; and their lower-shadow carrier vectors must
point in the same desired direction.  Equation (3.4) proves exact row
closure, not favourable carrier alignment.

There is a useful variable-length extension.  Let a twisted slab send
label `P` to `tau(P)` using `ell(P)` local edges, whereas the canonical
slab uses `L` edges on every row.  Call the slab **orbit-length balanced**
when

\[
             \sum_{P\in O}\ell(P)=|O|L
       \qquad\hbox{for every orbit }O\hbox{ of }\tau. \tag{3.4a}
\]

After `d` identical serial copies, where `d` is a multiple of every orbit
length, a row visits every label in its `tau`-orbit equally often.  Hence
(3.4a) restores its total canonical length as well as its label.  The
jointly reassembled ambient rows are therefore literal wreaths, even
though the individual open slabs do not have equal row lengths.

Every alternating incidence-cycle toggle which satisfies the exact
strand-diagram condition (so that it still consists of endpoint paths and
has no detached cycle) is orbit-length balanced: it cuts old paths at
possibly different phases and reattaches the same collection of segments,
so the sum of the new lengths on each induced strand orbit is unchanged.
Thus the finite-order repetition principle applies to strand-admissible
mixed-phase cycles as well as to the same-phase atoms of Theorem 3.4.

### Theorem 3.4 (a same-phase alternating hexagon is a three-cycle atom)

Let an untwisted path factor be written in synchronized form

\[
 X_0^i-Y_0^i-X_1^i-\cdots-Y_{r-1}^i-X_r^i.
\]

Fix one phase `t`.  Suppose three of the selected incidence edges
`X_t^i Y_t^i` have the form

\[
\begin{array}{c|c}
 X_t^1=K\cup\{a\}&Y_t^1=K\cup\{a,b\}\\
 X_t^2=K\cup\{b\}&Y_t^2=K\cup\{b,c\}\\
 X_t^3=K\cup\{c\}&Y_t^3=K\cup\{c,a\},
\end{array}                                             \tag{3.5}
\]

where `|K|=r-1` and `a,b,c` are distinct.  Replace these three edges by

\[
 X_t^2Y_t^1,\qquad X_t^3Y_t^2,\qquad X_t^1Y_t^3.       \tag{3.6}
\]

Then the result is an equal-length twisted path partition with a
three-cycle endpoint permutation.  It uses exactly the same `X`-vertices
and `Y`-vertices as before.

#### Proof

The six vertices in (3.5) form the alternating incidence hexagon

\[
 K a-Kab-K b-Kbc-K c-Kca-K a.
\]

Thus every edge in (3.6) is legal, and toggling the alternating half of
the hexagon preserves all six degrees.  Nothing else in the factor is
changed, so both shore ledgers remain exact.

Cut the three old paths immediately before the displayed incidence edges.
After (3.6), the prefix ending at `Ka` follows the old suffix beginning at
`Y_t^3=Kca`; the prefix ending at `Kb` follows suffix `1`; and the prefix
ending at `Kc` follows suffix `2`.  Hence the three right tails are
cyclically permuted.  All three cuts occur at the same phase, so every new
path has the same number of edges as the old paths.  The induced twist has
order three. \(\square\)

The identical statement holds when the toggled half-edges are the three
`Y_t^iX_{t+1}^i` edges instead.  This is the smallest possible incidence
switch because the middle-levels inclusion graph is `C_4`-free.

Combining Theorem 3.4 with Corollary 3.3 gives a concrete successor to the
failed two-edge-splicing idea: a bank of coherently oriented same-phase
hexagons, repeated in triples of aligned slabs, is automatically exact.
What remains is a positive-density occurrence and carrier-sign theorem.

### Theorem 3.5 (same-phase cycles and the rooted-tree alternative)

Fix one of the incidence matchings at a synchronized cut, for example the
selected edges `X_t^iY_t^i`.  Fix an `(r-1)`-set `K`.  Write every selected
edge whose lower endpoint contains `K` as

\[
             K\cup\{a\}\longrightarrow K\cup\{a,b\},
\]

and draw the directed arc `a->b` on the `r+1` coordinates outside `K`.
No undirected edge is used twice, because a repeated pair `{a,b}` would
repeat the same `Y`-vertex.

Every directed cycle all of whose selected edges occur at the **same path
phase**

\[
                     a_1\to a_2\to\cdots\to a_l\to a_1 \tag{3.7}
\]

gives an alternating incidence cycle of length `2l`.  Toggling it produces
an equal-length twisted path partition whose tail monodromy is an
`l`-cycle.  Consequently `l` coherently aligned copies close exactly.

If exactly one lower endpoint `K+a_*` is absent from the domain of the
global outgoing incidence matching, then the absence of every directed
functional cycle is equivalent to the selected arcs forming a spanning
tree oriented toward `a_*`.

#### Proof

The cycle (3.7) lifts to

\[
 K a_1-Ka_1a_2-Ka_2-\cdots-Ka_la_1-Ka_1.
\]

Toggling its alternating selected half preserves all degrees.  Since all
cuts occur at phase `t`, it cyclically reconnects equal-length prefixes
and suffixes, exactly as in Theorem 3.4.  This proves the first assertion.

For the rooted-tree assertion, now forget the phase restriction and use
the global outgoing incidence matching of the whole path factor.  Suppose
only `a_*` lacks an outgoing arc.  Every other vertex has
outdegree one.  If there is no directed cycle, following outgoing arcs
from any vertex must terminate at `a_*`.  The underlying graph has `r`
distinct edges on `r+1` vertices and is connected, hence is a tree, with
all arcs directed toward its unique sink `a_*`.  Conversely such an
oriented tree has no directed cycle. \(\square\)

For the port problem the omitted lower states have average incidence one
per `K`: if the omitted shore has `C_r` states, then

\[
 C_r r=\binom{2r}{r-1}.
\]

Thus the local obstruction to an **uncoloured outgoing functional-cycle**
bank is exact: most `K`-fibres would have to realize the rooted-tree
alternative.
For twisted routing one must additionally control the phase/strand
colouring.  A future positive theorem may prove that the required carrier
balance forces a positive density of monochromatic or otherwise
strand-admissible short cycles.

The Dyck port family permits a much stronger unconditional count.

### Theorem 3.6 (ballot-forced outgoing functional-cycle bank)

Orient any `D_r`-port path factor from `D_r` to `Dbar_r`.  Take the one
selected outgoing incidence edge from every

\[
              X\in\binom{[2r]}r\setminus\overline{D_r}.
\]

These edges form a perfect matching onto
`binom([2r],r+1)`.  For exactly

\[
 \boxed{
 Z_r={r-1\over r+2}\binom{2r}{r-1}
     ={r(r-1)\over r+2}C_r                         \tag{3.8}
 }
\]

of the `(r-1)`-cores `K`, no extension `K+a` lies in
`overline{D_r}`.  Every one of these `K`-fibres contains a directed cycle
in the outgoing-matching functional graph, of length at least three.

Moreover one can choose at least

\[
 \boxed{
       {Z_r\over r(r+1)}
       ={r-1\over(r+1)(r+2)}C_r
       =\left({1\over r}+O(r^{-2})\right)C_r          \tag{3.9}
 }
\]

pairwise outgoing-matching-edge-disjoint directed cycles.

#### Proof

Every oriented path uses each `Y`-vertex once and gives it a unique
predecessor `X`.  The predecessors are precisely all lower states except
the terminal ports `overline{D_r}`.  Hence the outgoing edges are the
claimed perfect matching.

Encode an `(r-1)`-set `K` by a `0/1` word with `r-1` up-steps and `r+1`
down-steps, and let `h_j` be its prefix height.  An omitted extension
`K+a` belongs to `overline{D_r}` exactly when changing the zero at `a`
to one makes a nonpositive balanced path.  Such an `a` can exist only if
the original deficient path is itself nonpositive: before `a` its heights
are unchanged, and after `a` they are two below the new heights.

Conversely, if the deficient path is nonpositive, take the down-step
immediately after its last visit to height `-1`.  Thereafter its height is
at most `-2`; changing that zero to one raises the suffix by two and gives
a nonpositive balanced path.  Thus `K` has an omitted extension if and
only if its deficient path is nonpositive.

By the reflection principle, the number of nonpositive paths with
`r-1` up-steps and `r+1` down-steps is

\[
 \binom{2r}{r-1}-\binom{2r}{r-2}
 ={3\over r+2}\binom{2r}{r-1}.                      \tag{3.10}
\]

Subtracting from all `binom(2r,r-1)` cores proves (3.8).

For any one of these `Z_r` cores, all `r+1` states `K+a` belong to the
matching domain.  Draw `a->b` when its selected outgoing edge is
`K+a -> K+a+b`.  Every vertex has outdegree one, loops are impossible,
and a directed two-cycle would use the same `Y=K+a+b` twice.  A finite
functional digraph therefore contains a directed cycle of length at least
three.

Choose one such cycle in every eligible core.  A selected matching edge
`X->Y` can occur in certificates for at most the `r` cores obtained by
deleting one element from `X`.  One certificate has at most `r+1` selected
edges.  Greedily selecting a certificate therefore deletes at most
`r(r+1)` certificates, and proves (3.9). \(\square\)

The lower bound (3.9) is a genuine supply theorem for outgoing-cycle
**certificates**, but it must not be compared directly with the global
`W/r^(3/2)` plateau scale.  One aligned size-`r` context carries `C_r`
rows, and its critical Catalan overshoot is a constant fraction of
`C_r`; a bank touching only `Theta(C_r/r)` rows is still a factor `r`
short at that one-context normalization if every touched row contributes
only `O(1)` carrier mass.  Serial finite-order repetition or long-cycle
carriers could change that accounting, but require a separate exact
supply/demand theorem.

There is a sharper full-factor correction.  A functional arc
`a -> b` uses the outgoing edge `K+a -- K+a+b`; the putative other half
`K+a+b -- K+b` may already belong to the incoming matching of the path
factor.  Hence a directed functional cycle is not automatically an
alternating cycle of the full factor.  In the canonical Chung--Feller
geodesic, its lift is full-factor alternating if and only if its selected
states lie on distinct root strands.  Thus every admissible lift is clean,
and folded `C_6` routers do not arise from this outgoing bank.

The exact correction and a positive-density **abstract path-ledger** bank
are proved in
`MATH_THEOREM_BALLOT_FORCED_C8_SUFFIX_ROUTER_BANK_20260726.md`: there are
`Cat_(r-3)` pairwise vertex-disjoint clean suffix `C_8` abstract switches,
affecting

\[
                 4\operatorname {Cat}_{r-3}
                    =(1/16+o(1))\operatorname {Cat}_r
\]

rows and avoiding every initial protected prefix ending before phase
`r-3`.  This is not a fixed-exterior wreath packet.  Its port
displacements are `1,1,1,2`, so not even one common moving exterior can
satisfy the rowwise geodesic equation.  A larger row-dependent
boundary-moving construction with a complete crossing-collar ledger is
required before monodromy repetition or carrier sign can be invoked.

## 4. The remaining signed-carrier gate

Let `Delta_i(q,S;tau_i)` be the depth-`q` load discrepancy produced by
the twisted replacement at slab `S_i`, measured after the row-tail
reconnection of Theorem 2.1.  Exact middle ownership gives

\[
                          \Delta_i(0,\cdot;\tau_i)=0,
\]

but no identity forces

\[
             \Delta_i(q,\cdot;\tau_i)
             +\Delta_j(q,\cdot;\tau_i^{-1})=0          \tag{4.1}
\]

at lower depths.  The two slabs have different exteriors and orientations,
so their shadow discrepancies may cancel, reinforce, or act on disjoint
targets.

Consequently the next exact question is:

> Can one realize `tau` and `tau^{-1}` in two aligned parent-visible
> slabs for which the sum of their row-resolved carrier vectors decreases
> the coherent PCap/hole functional?

A mirror theorem which proves inverse monodromy is only half of this
question.  It must retain the orientation of the desired carrier, rather
than returning the negative carrier as happened in the audited canonical
`H_4` conjugacy hinge.

### Theorem 4.1 (defect--carrier norm separation)

It is useful to allow an open routing packet which is not exact by itself.
Record such a packet by three data:

* its transported row monodromy `tau`;
* its signed `X/Y` ownership defect `epsilon` in the free abelian resource
  module; and
* its signed lower-shadow carrier `delta` in the target module.

Let `g_0,...,g_(d-1)` be physically realized exterior-moving coordinate
charts for `d` serial copies, each satisfying the geodesicity equation
(1.3) and its full crossing-collar ledger.  Transport the port labels
between copies so that, in one common label set, every row monodromy is the
same `tau`.  Suppose also that the copies are orbit-length balanced.  Then
the serial packet is an exact fixed-length ambient replacement if

\[
 \boxed{
       \tau^d=1,
       \qquad \sum_{j=0}^{d-1}g_j\epsilon=0.          \tag{4.2}
 }
\]

Its total lower-shadow action is

\[
 \boxed{
                    \Delta_{\rm total}
                    =\sum_{j=0}^{d-1}g_j\delta.       \tag{4.3}
 }
\]

Consequently the exact algebraic successor target is

\[
 \boxed{
   \sum_jg_j\epsilon=0
   \quad\hbox{but}\quad
   \sum_jg_j\delta\ne0.                              \tag{4.4}
 }
\]

#### Proof

Ownership discrepancies add as signed multisets, after applying the
physical chart of each copy.  Hence the second equation in (4.2) restores
both local resource ledgers.  The first equation restores the row labels;
orbit-length balance restores every row length.  Literal joins are fixed
by the interface-preserving chart assumption, so the resulting rows are
closed exact wreaths.  Lower-shadow histograms are also additive as signed
row/start-resolved carriers, which gives (4.3). \(\square\)

### Corollary 4.2 (finite-group Reynolds criterion)

Let a finite interface group `Gamma` act on both modules and commute with
the transported monodromy.  Installing one conjugate for every
`g in Gamma` is exact whenever `tau^|Gamma|=1` and

\[
                         \sum_{g\in\Gamma}g\epsilon=0. \tag{4.5}
\]

It is productive precisely when the Reynolds sum

\[
                         \sum_{g\in\Gamma}g\delta      \tag{4.6}
\]

has a favourable nonzero projection on the overloaded quota classes.

This separates the two representation-theoretic requirements.  The
nuisance ownership defect must lie in a module with zero invariant
projection, whereas the useful carrier must retain an invariant coarse
component.  A group which averages both modules to zero is useless; so is
a group which leaves a nonzero invariant part of `epsilon`.

The formal rank-three splice audited in
`MATH_AUDIT_D3_PENTAGON_TWIST_MONODROMY_20260726.md` fails (4.4): under
literal repeated copies the physical action on its four-colour defect is
trivial, so its defect norm is three times the original nonzero vector.

## 5. Scope

The authoritative conclusion is narrower than the first draft of this
note.  The ordinary fixed-exterior port-substitution space is **not**
enlarged: Theorem 1.3 forces pointwise zero twist there.  What survives is
an exact algebraic specification for a genuinely new boundary-moving
construction.

It still requires:

* a nonidentity exterior-moving geodesic packet satisfying (1.3) rowwise;
* its complete `X/Y` and crossing-collar ledger;
* a serial or group orbit with zero monodromy and zero ownership-defect
  norm;
* correct orbitwise total row length; and
* a favourable nonzero multidepth carrier norm.

The ballot cycle theorem and the `C_6/C_8` router classification live in
the abstract degree/path-factor category until these physical conditions
are proved.  No literal constant-one construction follows from them yet.
