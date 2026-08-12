# The resident q-port fusion is depth one; recursion needs a guarded socket tree

**Date:** 2026-08-01  
**Lane:** H3, protected upper-exact host / monotone component fusion  
**Status:** exact obstruction and exact conditional hierarchy theorem.  The
literal `H_2 -> H_3` resident-rail packet is an unconditional one-round
fusion, but it is not self-nesting.  A recursive use of the underlying
q-gon requires new named-socket, cut-witness and terminal-compiler data.

## 0. Outcome

The authoritative packet in
`MATH_THEOREM_QPORT_RESIDENT_RAIL_ROLE_CONVERTER_20260801.md` has

\[
                       \ell=2d+2                                      \tag{0.1}
\]

roots and atoms on each of its `q` small `H_2` cycles.  The fusion
`H_2 -> H_3` replaces those `q` cycles by one cycle of length `q ell`.
Because every small rail plus its direct seam is already a closed component
of a q1 factor, the large output cycle cannot be an input component of a
second literal copy of the same packet.  Thus a bank of the frozen packets
has fusion depth one.

For the reset arity

\[
                            q=2(d+1)=\ell,                            \tag{0.2}
\]

one selected packet state has exactly

\[
                         q\ell=q^2=4(d+1)^2                            \tag{0.3}
\]

root positions and atoms.  Its two-phase atom catalogue has

\[
 q(\ell-1)+2q=q(q+1)=2(d+1)(2d+3)                                    \tag{0.4}
\]

atoms: `q(ell-1)` common rail atoms and the `q+q` alternative direct
atoms.  All selected states use the same `q^2` resources in each of the
lower, upper, tail and head classes (the tail and head palettes are the
same `q^2` physical root positions).

Even if a generalized version could be nested on arbitrary larger cycles,
fixed arity leaves the exact congruence

\[
 c_{\rm final}\equiv c_{\rm initial}\pmod {q-1}.                       \tag{0.5}
\]

With unlimited applicable fusions the least positive residue is

\[
 c_* =1+((c_{\rm initial}-1)\bmod(q-1)).                              \tag{0.6}
\]

For (0.2), the worst residue is `q-1=2d+1`.  Hence the reset arity alone
cannot guarantee a number of components bounded independently of `d`.

The weakest recursive replacement is an occurrence-labelled guarded socket
tree.  Every child must export a parent-ready oriented atom; every internal
node must have a literal balanced q-gon on distinct current components;
every cut-crossing upper loss must have a surviving internal or ambient
witness; and the chosen terminal state must have a lower compiler.  No
pre/post or phase-common compiler intersection is required in the
reversal-quotient induction.

## 1. The frozen packet cannot consume its output

Let `F` be a directed q1 factor, so every root has indegree and outdegree at
most one.  In `H_2`, port `i` consists of the direct atom

\[
                         A_i\longrightarrow B_i                         \tag{1.1}
\]

and the resident return rail from `B_i` to `A_i`.  Together they are a
directed cycle on exactly `ell` roots.

### Theorem 1.1 (depth-one theorem)

If a q1 factor contains the full old state `H_2` of a literal resident
q-port packet, then each of its `q` displayed `ell`-cycles is an entire
factor component.  After the switch to `H_3`, their union is one component
of length `q ell`.  No later literal packet with the same `(q,d)` can use
that output component as one of its `H_2` input components.

Consequently every sequence consisting only of literal copies of the
frozen packet acts on pairwise disjoint sets of original small components.
It has nesting depth at most one.

#### Proof

Every root of a displayed rail-plus-seam cycle already has one incoming and
one outgoing selected atom.  The degree-one condition forbids any factor
atom from leaving or entering it, so it is a whole component.

The q-gon switch changes no root and joins the `q` components into one
cycle, hence the output has `q ell` roots.  A component of the old state of
another frozen packet has exactly `ell` roots.  Since `q>=3`, the large
output cannot equal such a component.  Nor can a proper subset of a simple
cycle support another selected closed cycle: all of its vertices already
use their unique predecessor and successor on the large cycle.  Thus a
later frozen packet cannot meet the output.  \(\square\)

### Corollary 1.2 (best possible one-round reduction)

Suppose optimistically that `c` initial components are standard small port
cycles and can be grouped into as many disjoint literal packets as possible.
Writing

\[
                              c=sq+r,\qquad0\le r<q,                    \tag{1.2}
\]

one round leaves at least

\[
                              s+r=\lfloor c/q\rfloor+(c\bmod q)        \tag{1.3}
\]

components.  Theorem 1.1 prevents a second round on the `s` fused outputs.
Thus the literal resident bank does not replace a many-level Catalan
connector tree.

## 2. Component arithmetic remains after any generalization

The following does not use the special rails.

### Proposition 2.1 (fixed-arity residue)

Every forward q-gon fusion on `q` distinct cycles changes the component
count by `-(q-1)`.  Therefore any sequence of such fusions satisfies (0.5).
If an applicable fusion is available whenever at least `q` components
remain, repeated fusion terminates at (0.6).

#### Proof

Each move replaces `q` components by one.  Repeated subtraction of `q-1`
from `c_initial-1` proves both assertions.  \(\square\)

For `q=2(d+1)`, (0.6) is only an `O(d)` conclusion.  A bounded cleanup can
still use only fusion directions, but it needs another arity.  For example,
regenerating `q=3` packets leave at most two components; `q=3` together with
`q=4` has decrement monoid generated by `2,3` and can reach one component
from every count except the isolated count two.  This is an additional
packet-supply theorem, not a consequence of the reset-arity bank.

For a uniform q-ary merge forest with `c` leaves and `r` roots, the number
of internal fusions is necessarily

\[
                         I={c-r\over q-1},\qquad qI={q(c-r)\over q-1}    \tag{2.1}
\]

where `qI` is the number of child-to-parent socket incidences.  At reset
arity a formal reservation of one full standard packet at every internal
node would charge

\[
 {4(d+1)^2(c-r)\over2d+1}                                             \tag{2.2}
\]

selected-state atom incidences, or

\[
 {2(d+1)(2d+3)(c-r)\over2d+1}                                        \tag{2.3}
\]

two-phase catalogue incidences.  Equations (2.2)--(2.3) are only a formal
budget: Theorem 1.1 says that vertex-disjoint full standard packets cannot
be arranged as a nested hierarchy.  A genuine hierarchy must reuse the
child root blocks and reserve only compatible sockets and their guards.

## 3. The exact prospective replacement

Let `M_0` be an exact four-resource directed factor whose physical
components are cycles.  A **guarded socket forest** consists of a rooted
forest `T` and, for each internal node `v`, the following data.

1. Its children are cycle components present after all descendant switches.
   Their root sets are disjoint.
2. Each child has a named current atom

   \[
                         e_{v,i}=A_{v,i}\to B_{v,i}.                    \tag{3.1}
   \]

   The `q_v` named atoms form the old phase of one literal q-gon, and its
   new phase has the same complete lower, upper, tail and head palettes.
3. The named atoms lie on `q_v` distinct current components.  The new port
   permutation is one `q_v`-cycle.
4. The switched component is depth-`d` resident.  If `v` is not a forest
   root, it exports a named, correctly oriented parent socket which is not
   deleted before the parent switch.
5. Every required upper target whose selected witness is destroyed at this
   step has either a new internal witness or an occurrence-labelled ambient
   reserve ticket.  Tickets used simultaneously are one-copy compatible,
   and a ticket is either outside every later modified block or is
   recertified at the next step.
6. Packets at incomparable nodes which are applied in parallel have
   disjoint current typed resources.  Serial packets may reuse a resource
   only through an explicitly named output-to-input socket.
7. The final oriented state has the required occurrence-labelled lower
   compiler matching.  If the induction insists that every intermediate
   state be admissible, replace this by a compiler matching at every state.

Condition 5 can be written without prose.  Freeze a step and let `r_v(T)`
be the number of still-unpaid required copies of target `T` after counting
surviving and new internal witnesses.  Let `C_v(T)` be the resource-private
ambient tickets for `T` which survive the rest of the schedule.  Then the
necessary and sufficient reserve condition is

\[
 |N(\mathcal A)|\ge\sum_{T\in\mathcal A}r_v(T)                         \tag{3.2}
\]

for every target family `A`.  Without resource privacy, (3.2) is only the
matching marginal and must be replaced by the actual Rado/conflict rank
condition.

### Theorem 3.1 (guarded postorder fusion)

Given a guarded socket forest, applying its packets in postorder produces
an exact factor with one cycle for each root of `T`.  It preserves the
complete immediate palettes and depth-`d` residence, and it loses no
required upper target.  If condition 7 holds, the terminal state also has
the required lower compiler.

For uniform arity `q`, its component count is

\[
                              c_{\rm final}=c_{\rm initial}-I(q-1).     \tag{3.3}
\]

#### Proof

At an internal node, all descendants have already become the stated child
cycles.  Conditions 2--3 and the q-gon topology theorem make the switch a
legal four-resource replacement and fuse exactly those cycles.  Condition
6 prevents interference with incomparable nodes.  Condition 4 proves
residence and supplies the socket required by the parent.  Condition 5 and
Hall's theorem transport the target certificate.  Induction over the
postorder proves all assertions, while summing the component decrement
gives (3.3).  Condition 7 is already stated on the resulting occurrence
graph.  \(\square\)

Conversely, every successful serial fusion schedule which is required to
remain upper-exact after every move induces such a merge forest from the
successive coarsenings of the component partition.  Its actual old atoms
are the named sockets, and its actual target and compiler certificates
supply conditions 5 and 7.  Thus Theorem 3.1 is the weakest exact
prospective condition for **state-by-state upper-exact** fusion; the missing
content is a theorem constructing that occurrence-labelled data from an
upper-exact factor.  If only the terminal state must be upper-exact,
condition 5 may be replaced by one final witness ledger, allowing temporary
debts; that weaker mode has no monotone intermediate-state conclusion.

## 4. Sharp failures of component-only packet supply

### Proposition 4.1 (laminar component necessity)

The vertex sets of all components produced by a fusion sequence form a
laminar family.  In particular, two proposed merge blocks which overlap
but neither contains the other cannot both occur as components in one
schedule.

#### Proof

Every fusion replaces several blocks of the current component partition by
their union.  Component partitions therefore only coarsen.  Two blocks
which occur at different times are disjoint or one contains the other.
\(\square\)

Component laminarity is not sufficient because component labels forget the
literal socket occurrence.

### Proposition 4.2 (shared-socket loose-tree obstruction)

Fix `q>=3`.  Take `2q-1` cycle components

\[
 C_0,C_1,\ldots,C_{q-1},D_1,\ldots,D_{q-1}.                         \tag{4.1}
\]

Suppose packet `P` uses one old atom `e` on `C_0` and one old atom on each
`C_i`, while packet `Q` uses the same literal atom `e` and one old atom on
each `D_i`.  Assume both q-gon replacements are individually legal and
there are no other packets.

The two component footprints are q-edges meeting in one vertex, hence form
a loose hypertree.  Component arithmetic predicts that two fusions would
send `2q-1` cycles to one.  Nevertheless no two-step fusion sequence
exists.

#### Proof

The old and new direct phases of a q-gon are disjoint when `q>=3`.
Whichever packet is toggled first deletes `e` and does not reinstall it.
The other packet's literal old phase is therefore absent.  The process
stops after one move, with `q` components.  \(\square\)

If the two packets use distinct surviving sockets on `C_0`, the first
merged component may feed the second packet.  Thus Proposition 4.2 is
sharp: component overlap alone is not the obstruction; occurrence-level
socket consumption is.

The same point appears as **port depletion**.  A fusion consumes all `q`
named old sockets.  Although `H_3` creates `q` new direct atoms, the local
q-port theorem does not prove that one of them, together with sockets from
`q-1` sibling outputs, is a parent-ready guarded q-gon.  Socket regeneration
is a new compatibility theorem.

## 5. Relative phase, upper exterior and compiler scope

A parent packet requires oriented named sockets, not unoriented component
labels.  If `q` child components carry phase vector

\[
                         \epsilon\in\mathbb F_2^q,                       \tag{5.1}
\]

global reversal identifies only `epsilon` and `epsilon+1`.  The other
`q-1` relative phase bits remain.  Thus a guarded socket forest must export
a compatible sibling orientation at each parent; global reversal cannot
repair a mixed vector component by component.

The internal upper monotonicity

\[
                         \operatorname{Deck}(H_2)
                          \subseteq\operatorname{Deck}(H_3)              \tag{5.2}
\]

is retained exactly for the frozen rail cycles.  It pays no old internal
root-interval target in that closed packet.  It does not prove any of the
following for a generalized parent socket on a larger cycle:

* survival of intervals crossing the chosen parent cut;
* survival of prefix/suffix windows after the terminal linear opening;
* graded multiplicity or derivative/source occurrence transport; or
* survival of an arbitrary frozen exterior witness assignment.

Those are precisely the demands `r_v(T)` in (3.2).  An ambient
duplicate/reflection bank may pay them, but it must be named occurrence by
occurrence.  There is no safe-cut conclusion here.

Finally, the global-reversal quotient removes an obsolete requirement: one
does **not** need a compiler in the intersection of two globally reversed
phase graphs.  It suffices to construct a compiler for the selected
terminal orientation and reflect it with the whole state.  The nonlinear
fusion `H_2 -> H_3` is not itself a reversal, so its post-fusion compiler is
not supplied by the pre-fusion matching; terminal existence remains an
explicit condition.  Named parent sockets and the cut ledger are likewise
not reversal gauges.

## 6. H3 verdict

The monotone q-port theorem removes a one-round topology row but does not
yet remove the Catalan connector hierarchy.  There are three independent
reasons:

1. the literal resident packet has depth one;
2. the fixed reset arity leaves as many as `2d+1` components; and
3. a generalized recursion needs occurrence-labelled regenerated sockets,
   sibling phase compatibility, and explicit cut/exterior target tickets.

The exact positive target is Theorem 3.1 with a mixed-arity regenerative
socket forest, preferably bulk arity `2(d+1)` followed by a regenerating
`q=3,4` cleanup.  Those two arities reach one from every count at least
three except when the process is actually stranded at two; that last case
still needs a separate two-component sidecar.  The lower compiler is
terminal and orientation-specific in the reversal quotient; arbitrary
exterior witnesses remain an explicit Hall/Rado ledger.
