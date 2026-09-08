# The exact cut-colour recycling gate is a matroidal provider transversal

Date: 2026-08-01  
Lane: immediate lower palette in the cyclic four-sector child  
Status: exact conditional min--max theorem and unconditional frozen
candidate-graph bound.  This does not construct the required four-sector
provider atlas or a terminal common-cap matching.

## 0. Outcome

Let a `q1`-rainbow spanning two-factor have `c>=2` components.  Cut one edge
in each component, orient and order the resulting paths, and write their
distinct cut colours as

\[
                       \Delta=\{q_1,\ldots,q_c\}.
\]

The first and last colours are special: `q_1` is contained in the global
left owner and `q_c` in the global right owner.  The two repeated endpoint
cap banks therefore contain distinct candidate cells for them.  For
`d>=2`, the fresh-`q1` coatom transporter exposes one controlled alternative
cell at each end; its local choice capacity is

\[
                         b_L=b_R=1.                 \tag{0.1}
\]

This sharpens the boundary estimate in the first rainbow-sidecar note.  If
`eta` interior cut colours remain unrecycled, then for every `d>=1`

\[
                         \boxed{\delta_{\rm top}\le\eta}.    \tag{0.2}
\]

No hypothesis `d>=eta+2` is needed at the frozen candidate-graph level.
Reserve one left candidate cell for `q_1` and one right candidate cell for
`q_c`; every other possible hole is one of the `eta` interior colours.
Turning the two transporter alternatives into net compiler assignments is
a separate exchange gate because each fixed cell also has a displaced old
target.

The remaining recycling problem has an exact min--max on the physically
private/common-boundary face.  Let `P` be a bank of certified colour-pure
sidecar providers and let `M` be the matroid of provider sets which can be
installed together without changing the common topology.  For the interior
bank

\[
                        \Delta^\circ=\{q_2,\ldots,q_{c-1}\},
\]

join a colour `q` to a provider `p` when `p` can install `q`.  Then the
minimum possible interior debt is exactly

\[
 \boxed{
   \eta_M
    =\max_{X\subseteq\Delta^\circ}
          \bigl(|X|-r_M(N(X))\bigr).}               \tag{0.3}
\]

Thus `eta_M<=C` is equivalent to the cut inequalities

\[
                  r_M(N(X))\ge |X|-C
                  \quad(X\subseteq\Delta^\circ).    \tag{0.4}
\]

For source-private seam slots, `M` is a partition matroid and (0.3) is an
ordinary capacitated Hall/max-flow deficiency.  An alternating augmenting
path lowers `eta_M` by one; a closed alternating circuit merely reroutes the
same number of colours.  This is the exact occurrence-routing target.

The theorem deliberately does not infer (0.4) from raw packet abundance.
If options use crossing shared resources, their compatibility need not be a
matroid and the reduction is no longer sound.

## 1. The endpoint charge is exactly two capacity-one banks

Let

\[
                 P_1\Vert P_2\Vert\cdots\Vert P_c
\]

be a legal splice of the opened factor components.  The edge cut from
component `i` has colour `q_i`; let the new seams have arbitrary colours.
By the exact cut/seam ledger, every natural `q1` hole belongs to

\[
             \Delta\setminus\operatorname{supp}\{\text{new seams}\}.
                                                               \tag{1.1}
\]

Put

\[
 \eta=\left|\{q_2,\ldots,q_{c-1}\}
         \setminus\operatorname{supp}\{\text{new seams}\}\right|.
                                                               \tag{1.2}
\]

### Theorem 1.1 (dimension-free frozen endpoint-cap bound)

For every `d>=1`, the candidate deficiency of the frozen top-shadow gate
satisfies

\[
                           \delta_{\rm top}\le\eta.           \tag{1.3}
\]

If `d>=2` and disjoint fresh-`q1` endpoint coatom transporters are planted
at the two ends, their complete paired `q>=2` endpoint chains are transported
simultaneously and each exposes the desired outer `q1` alternative in one
fixed cell.  These become net physical q1 assignments only if the two
displaced alternatives have reserved redundant witnesses or lie on a
certified matching exchange in the same terminal cap state.

#### Proof

If `q_1` remains a hole, it is contained in the first owner of `P_1`.
Assign it to one of the `d` repeated left caps.  If `q_c` remains a hole,
assign it to one of the `d` repeated right caps.  These are distinct
physical cells even when `d=1`, so the two assignments coexist.  Every
other hole in (1.1) is one of the `eta` interior colours.  Starting with the
two displayed assignments and adding `eta` target vertices can increase
the unmatched count of a bipartite matching by at most `eta`.  This proves
(1.3).

The fresh endpoint transporter has exactly one differing length-`d` cell;
hence its local alternative bank has capacity one.  Its reverse gives the
disjoint right bank.  The literal prefix calculation in the endpoint-chain
theorem shows that the two gadgets also transport the paired deeper chains.
It does not, by itself, rehost the old target displaced from either cell;
that is precisely the additional matching-exchange hypothesis above.
\(\square\)

The local capacity statement is sharp.  One transporter has one physical
length-`d` address and cannot expose two distinct missing `q1` targets.  The
two gadgets together expose two alternatives, not `2d`: the other repeated
endpoint caps belong to the ambient compiler.  Exposure is weaker than a
net capacity-two matching until the two displaced targets are closed.

### Corollary 1.2 (the strongest unconditional scalar statement)

For an arbitrary legal splice, `eta<=c-2` and hence

\[
                          \delta_{\rm top}\le c-2.            \tag{1.4}
\]

No dimension-uniform `O(1)` bound follows unless the number of unrecycled
interior colours, rather than merely the number of physical seam choices,
is controlled.

## 2. A physically sound provider interface

The min--max theorem needs more than a list of abstract colour labels.
Fix the opened fragments, their external order skeleton, and an off/default
state for every connector collar.  A **colour-pure provider** `p` consists
of a certified local replacement with the following properties.

1. It has the same two external owners and the same declared topology as
   its off state.
2. Relative to the common retained `q1` deck, it installs one declared cut
   colour `q(p)` and deletes no other cut-bank occurrence.
3. It preserves the required U1--U4 rows and all literal protected guards.
4. Its physical resource set is recorded, including its connector slot.

One provider atom denotes one literal labelled alternative.  If one
geometric collar has a menu of possible exported colours, represent its
different labelled alternatives by different provider atoms in the same
rank-one slot block.  Let `P` be the resulting finite provider bank.  A
family `I subseteq P` is
**compatible** when all its providers can be turned on simultaneously (or
serially through their common off states) while retaining the common
external chronology.  Assume that the compatible families are the
independent sets of a matroid

\[
                              M=(P,\mathcal I).               \tag{2.1}
\]

The main proved face is source-private/laminar.  Each ordinary Johnson seam
has capacity one because it carries one rank-`r-1` intersection colour.
Alternatives for one seam slot therefore form a rank-one block.  Nested
private resource banks give further laminar capacity rows.  These rows form
a laminar matroid.  A partition into private seam slots is the special case

\[
                 r_M(A)=\sum_{s}\min\{1,|A\cap P_s|\}.       \tag{2.2}
\]

The scalar slot ledger is exact.  A linear `c`-fragment splice has `c-1`
connector slots of capacity one and only `c-2` interior cut-colour demands,
so one connector may remain in its off/default state.  A cyclic splice has
`c` connector slots and `c` cut-colour demands, with no spare slot.  The two
endpoint transporter cells are compiler providers, not additional Johnson
connector slots.

The hypothesis is substantive.  The smallest exchange failure already has
three provider atoms with `(slot,resource)` pairs

\[
                         (s_1,r_1),\quad(s_1,r_2),\quad(s_2,r_1). \tag{2.3}
\]

Under capacity one on every slot and resource, the singleton containing the
first atom and the two-set containing the other atoms are both compatible,
but neither atom of the two-set can augment the singleton.  Hence crossing
slot and resource partitions do not define a matroid.  With labelled colour
rows this is the first three-dimensional-matching obstruction.  Raw
alternatives may not be inserted into (2.1) without proving the stated
laminar/private compatibility interface.

## 3. Exact Rado deficiency

Build the bipartite eligibility graph

\[
                 G=(\Delta^\circ,P;E),
 \qquad q\sim p\Longleftrightarrow q(p)=q.                   \tag{3.1}
\]

Equivalently, before expanding a labelled menu into atoms, this relation
says that the corresponding geometric provider can install `q`.

A **provider transversal** of `S subseteq Delta^circ` is a matching of `S`
to a provider set independent in `M`.

### Theorem 3.1 (matroidal cut-colour min--max)

The maximum number `mu_M` of simultaneously recycled interior cut colours
is

\[
 \mu_M=min_{X\subseteq\Delta^\circ}
       \left(|\Delta^\circ\setminus X|+r_M(N(X))\right).     \tag{3.2}
\]

Consequently

\[
 |\Delta^\circ|-\mu_M
 =\max_{X\subseteq\Delta^\circ}
       \left(|X|-r_M(N(X))\right)=\eta_M.                   \tag{3.3}
\]

Installing a maximum transversal and leaving every unused slot in its off
state gives a legal splice with

\[
                            \delta_{\rm top}\le\eta_M.       \tag{3.4}
\]

#### Proof

Formula (3.2) is the matroidal transversal theorem.  For completeness, the
upper bound is immediate: at most `|Delta^circ-X|` selected colours lie
outside `X`, while the providers selected for colours in `X` form an
independent subset of `N(X)` and hence have size at most `r_M(N(X))`.
Equality follows from the standard matroid-intersection augmenting-path
proof applied to the transversal matroid induced on `P` by (3.1) and `M`.
Subtracting (3.2) from `|Delta^circ|` gives (3.3).

The providers in a maximum transversal coexist by (2.1), and colour purity
means that their distinct installed cut colours cannot delete one another.
Thus at most `eta_M` interior cut colours remain missing.  Apply
Theorem 1.1.  \(\square\)

### Corollary 3.2 (exact bounded-recycling criterion)

For an absolute integer `C>=0`, the provider bank leaves at most `C`
interior cut colours unrecycled if and only if

\[
                  r_M(N(X))\ge |X|-C
                  \quad\text{for every }X\subseteq\Delta^\circ. \tag{3.5}
\]

This is the weakest exact availability theorem on the matroidal provider
face.  In particular, a regenerative `O(1)` top-shadow theorem is obtained
once (3.5) is proved with an absolute `C` at every same-parity lift.

## 4. Ordinary flow and alternating occurrence routing

Suppose the providers are private by connector slot and every slot has
capacity one.  Collapse all alternatives in one slot to a right vertex
`s`; put `q~s` when that slot has a certified option installing `q`.  Then

\[
 \eta_*=\max_{X\subseteq\Delta^\circ}
              (|X|-|N(X)|)                                \tag{4.1}
\]

is the ordinary Hall deficiency.  Equivalently, create a unit-capacity
network

\[
   \text{source}\longrightarrow\Delta^\circ
       \longrightarrow S\longrightarrow\text{sink}.        \tag{4.2}
\]

Its maximum flow is `|Delta^circ|-eta_*`.  For a partition of slot groups
with capacities `b_s`, replace the last arc capacity by `b_s`; the cut
formula becomes

\[
 \eta_*=\max_X\left(|X|-\sum_s
                   \min\{b_s,\ |N(X)\cap P_s|\}\right).     \tag{4.3}
\]

Starting from a selected matching, an alternating path from an uncovered
cut colour to an unused slot raises the flow by one and decreases `eta_*`
by one.  An alternating cycle changes the physical occurrence routing but
preserves its cardinality.  When every slot has a common off state, a cycle
can be serialized by first turning its selected providers off and then
turning the alternate providers on; the declared U1--U4 and boundary guards
are preserved throughout by the provider definition.

The no-augmenting-path certificate is literal.  If `R` is the set of
colours reachable from the unmatched colours in the alternating graph,
then its reachable slots form a tight cut and

\[
                          |R|-|N(R)|=\eta_*                 \tag{4.4}
\]

after taking the union of the deficient alternating components.  Thus a
failed occurrence router produces the exact violating colour bank, not
only a scalar failure count.

### Corollary 4.1 (degree/load test)

On the private-slot face, let `D>=1`, suppose all but at most `C` interior
colours have at least `D` eligible slots, and every slot is eligible for at
most `D` of those nonexceptional colours.  Then

\[
                              \eta_*\le C.                  \tag{4.5}
\]

Indeed, double-counting the eligibility edges from any set `X` of
nonexceptional colours gives `D|X|<=D|N(X)|`; Hall saturates all
nonexceptional colours.

This is the useful bounded-load target for a regenerative atlas.  A large
raw menu without the per-slot load bound gives no such conclusion.

## 5. Endpoint providers and the two exact targets

The endpoint gadgets may be folded into the same rank formula.  Add provider
banks `P_L,P_R`, each of rank one, and take

\[
                M^+=M\oplus U_{1,P_L}\oplus U_{1,P_R}.      \tag{5.1}
\]

Only after a planted transporter and its displaced target have been closed
into one net provider may one join `q_1` to `P_L` and `q_c` to `P_R`.
More endpoint-contained colours may be joined only after an analogous
literal net provider is certified.  Under that hypothesis, applying
Theorem 3.1 to all of `Delta` gives the exact combined
sidecar-plus-endpoint deficiency

\[
 \eta^+=\max_{X\subseteq\Delta}
             (|X|-r_{M^+}(N(X))).                           \tag{5.2}
\]

This formulation makes the capacities in (0.1) explicit and prevents the
same endpoint cell from paying two cut colours.

There are two different terminal goals.

1. **Bounded compiler top shadow.**  Equations (3.4) or (5.2) suffice.
   Repeated seam colours are harmless except insofar as they leave a cut
   colour uncovered.
2. **A `q1`-injective cyclic child.**  Endpoint cells do not count as cycle
   edges.  Use `c` cyclic connector slots and no endpoint providers.  If

   \[
                r_M(N(X))\ge|X|\qquad(X\subseteq\Delta),     \tag{5.3}
   \]

   then a transversal assigns every cut colour to a distinct cyclic seam.
   Colour purity and the retained rainbow interiors make the entire child
   cycle `q1`-rainbow.

For a linear `B1` path, choose a prospective closing colour `q_*` contained
in both global endpoints and match `Delta-{q_*}` to the `c-1` seam slots.
The same rank inequalities on that deleted left bank are necessary and
sufficient.  The endpoint edge of colour `q_*` then closes the path.

The fresh endpoint transporters solve neither (5.3) nor the existence of a
common endpoint colour `q_*`.  Before displaced-target closure they only
expose the two local alternatives.  After such closure, they supply the
capacity-two endpoint assignment represented in (5.1).

## 6. Exact remaining obstruction

The result separates three claims which must not be conflated.

* The two outer cut colours have distinct frozen candidate cells
  unconditionally.  Planted endpoint collars expose one controlled
  alternative per end, but net physical ownership still needs
  displaced-target closure.
* Once a colour-pure private/laminar provider atlas is given, bounded
  recycling is exactly the rank row (3.5), and cyclic injectivity is exactly
  (5.3).
* The current four-sector construction has not yet supplied such an atlas
  with the required ranks.  In particular, options whose external owners
  differ do not share a connector slot, and crossing owner/slot/compiler
  conflicts cannot be silently compressed into `M`.

Accordingly the weakest new same-parity statement which would close this
lane is:

> **Bounded cut-colour router.**  After forming the child rainbow factor,
> expose a common-boundary colour-pure provider bank whose compatibility is
> matroidal and which satisfies (3.5) with an absolute `C`.

The stronger zero-defect statement replaces (3.5) by (5.3) on the cyclic
bank.  Residence, deeper shadows, and the common-cap compiler remain
separate gates.

## 7. Replay

Run

```text
python3 scratch/audit_o1_q1_cut_colour_recycling_rado_gate_20260801.py
```

The replay exhausts the endpoint-class inequality through six interior
holes and checks the partition-matroid form of (3.2)--(3.3) on every small
eligibility graph in its declared range.
