# The rainbow sidecar and fresh-q1 transporter are compatible but do not compose to cyclic injectivity

Date: 2026-08-01  
Lane: strict scope audit of handoff items 2368ROOT and 2369TSR  
Status: exact interface theorem, two literal small counterexamples, and a
conditional bounded-`eta_*` occurrence-routing lemma.  No residence,
upper-support, compiler, or `B(k)+O(1)` conclusion is claimed.

## 0. Verdict

There are three different objects which must not be identified.

1. A `B1` path closes to a q1-rainbow **parent cycle**.
2. A diamond-ready parent cycle, together with an upper-union occurrence
   transversal and the cap-two factor, gives a q1-rainbow **child
   two-factor** by the direct four-sector formula.
3. A cyclic component-neutral macro braid is a further physical
   Hamiltonization.  Its slot counts are exact, but its occurrence-labelled
   q1 injectivity is an additional condition.

The fresh-q1 endpoint transporter acts on a fourth object: prefix or suffix
**compiler cells** of two antecedents with the same depth-`d` owner carrier.
It can carry an endpoint-contained missing q1 target, but it does not change
the natural edge intersections of either the parent or child factor.
Consequently items 2368ROOT and 2369TSR are locally compatible, but their
composition does **not** prove cyclic four-sector q1 injectivity.

## 1. Exact local compatibility of the endpoint definitions

Let `E` be a rank-`R` endpoint owner and let `Q` be one of its rank-`R-1`
facets.  Suppose

\[
                         R-1\ge d+3                         \tag{1.1}
\]

and there is at least one coordinate outside `E`.  Write `b` for the unique
element of `E-Q`.  Choose distinct elements of `Q` and name them

\[
 \infty,c,a,\xi,f_1,\ldots,f_{d-1},                       \tag{1.2}
\]

put all remaining elements of `Q` in `K`, and choose `f_0` outside `E`.
Then the fresh-q1 transporter of item 2368ROOT has

\[
 T_0=K\cup\{\infty,a,b,c\}
          \cup\{f_1,\ldots,f_{d-1},\xi\}=E               \tag{1.3}
\]

and its `a`-alternative at prefix length `d` is exactly

\[
 K\cup\{\infty,c,a,\xi,f_1,\ldots,f_{d-1}\}=Q.           \tag{1.4}
\]

Thus every endpoint-contained q1 colour admits the advertised local
coordinate relabelling in the stable rank range.  Use the construction
forward at the left endpoint and reversed at the right endpoint.

Two scope qualifications are essential.

* The fresh filler `xi` in (1.2) is a role name; it must not silently be
  identified with either Pascal tag `x,y` unless the desired facet itself
  contains that tag.
* The two endpoint gadgets need disjoint **physical cell/occurrence banks**.
  Their coordinate supports need not, and for overlapping outer cut colours
  generally cannot, be disjoint.

Only actually unrecycled outer holes should be assigned.  If the splice has
one component, or if a seam already reinstalls one outer cut colour, adding
two copies would duplicate a target.  Moreover, changing the length-`d`
cell from one alternative to the other displaces its former q1 target.
Complete q1 coverage therefore still needs that displaced target to have
another provider, a reserved unused cell, or a coexistent matching exchange.
This is exactly the q1/common-cap Hall qualification already stated in
item 2368ROOT.

## 2. `B1` alone does not supply the direct four-sector hypotheses

The published ML(7) Hamilton cycle in
`MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`
admits the legal incidence-hex toggle

\[
 H=\{2,3\},\qquad(a,b,c)=(0,1,5),                           \tag{2.1}
\]

which removes

\[
 (13,15),(14,46),(44,45)                                   \tag{2.2}
\]

and adds

\[
 (14,15),(44,46),(13,45).                                  \tag{2.3}
\]

The result is again a 70-vertex middle-levels Hamilton cycle.  Its rank-four
projection is a Hamilton cycle in `J(7,4)` whose 35 rank-three edge
intersections are all distinct.  Hence opening any edge gives a literal B1
path.  Nevertheless its adjacent rank-five unions occupy only 20 of the 21
targets; the sole missing union is

\[
                              0x3e.                         \tag{2.4}
\]

Therefore B1 closure does not imply the upper-union occurrence transversal
in the definition of a diamond-ready parent.  This does not contradict the
direct four-sector factor theorem: once the occurrence transversal and
cap-two factor are separately supplied, the four signature palettes

\[
        Z+xy,\qquad C+x,\qquad C+y,\qquad T                \tag{2.5}
\]

partition the complete child q1 palette and the direct child two-factor is
automatically q1-injective.

## 3. A simple cyclic-path bank is not automatically rainbow

There is a second independent failure at the first possible old rank.  On
seven old coordinates, take the complete rank-five `U` deck and identify it
with complements of the rank-two deck.  The complement sequence

```text
56 46 45 04 05 06 01 02 03 34 14 24 25 15 35 13 12 16 26 23 36
```

is a Hamilton path of `J(7,2)`, so the corresponding rank-five owners form
one simple Johnson path through the entire `U` deck.  Its 20 internal edges
have only 15 distinct rank-four intersections.  The five colours

```text
0x0f 0x33 0x39 0x4e 0x55
```

each occur twice.  In particular even `c=1` and simple owner topology do not
make the internal untagged bank rainbow.  This is a counterexample to an
automatic-injectivity inference from the component-neutral slot ledger, not
a complete four-sector macro counterexample.

## 4. Exact occurrence-routing lemma by transparent two-switches

Let `F` be a q1-rainbow spanning two-factor in `J(k,r)`.  A **transparent
cross-switch** consists of two factor edges

\[
 e=uv,\qquad f=xy                                             \tag{4.1}
\]

in different components and one of the two cross pairings `P`, such that
both edges of `P` are Johnson and

\[
       \{\!\{\chi(g):g\in P\}\!\}
       =\{\!\{\chi(e),\chi(f)\}\!\}.                       \tag{4.2}
\]

Replacing `e,f` by `P` merges the two cycles and preserves every q1 colour
with multiplicity one.

### Theorem 4.1 (resource-disjoint transparent forest)

Suppose a family of transparent cross-switches has pairwise vertex-disjoint
source edges, and its graph on the original components of `F` is a forest.
Applying all switches, in any order, gives a q1-rainbow two-factor with

\[
       c(F)-|\mathcal S|                                      \tag{4.3}
\]

components.  In particular a spanning tree gives a q1-rainbow Hamilton
cycle.

#### Proof

Deleting one edge from each of two distinct cycles and inserting a cross
pairing gives one cycle.  Equation (4.2) preserves the two deleted colours
exactly.  Vertex-disjoint source edges make the switches commute.  Before a
forest edge is processed, its two endpoint components cannot already be
joined by the other processed forest edges; otherwise those edges plus the
unprocessed edge would form a cycle in the component graph.  Thus every
switch lowers the component count by one and (4.3) follows.  \(\square\)

### Corollary 4.2 (an exact bounded-`eta_*` two-component target)

It is enough to find a resource-disjoint transparent forest of rank at
least `c(F)-2`.  The resulting factor has at most two q1-rainbow components.
If there are two, connectivity of `J(k,r)` supplies a Johnson edge between
the two vertex sets.  Cut one incident factor edge in each cycle and use
that cross edge as the seam.  The result is a spanning path with no interior
factor component and therefore

\[
                           \eta_*=0,
       \qquad \delta_{\rm top}=0\quad(d\ge2).                \tag{4.4}
\]

Its only possible natural holes are the two outer cut colours.  The endpoint
transporter of Section 1 supplies a local physical alternative for each
hole, subject to the displaced-target/common-cap qualification there.

More generally, if a transparent forest leaves `h` components and those
components possess a legal ordered one-cut splice, then simply because
there are only `h-2` interior cuts,

\[
                     \eta_*\le\max(0,h-2).                  \tag{4.5}
\]

This is the exact bounded cut-colour recycling theorem.  The ordered-splice
hypothesis cannot be replaced by connectivity of the component quotient
when `h>2`: an internal component must expose its two cross-seam endpoints
as the endpoints of one opened factor edge.

## 5. Relation to the unrestricted incidence reset

The transparent-forest theorem is a sufficient route **inside a restricted
physical edge catalogue**.  At the unrestricted owner/q1 level it is not
necessary.  The independently frozen incidence-reset theorem
`MATH_THEOREM_O1_FOUR_SECTOR_Q1_ALTERNATING_CIRCUIT_RESET_20260801.md`
lifts every q1-rainbow Johnson two-factor to a spanning two-factor of the
Middle Levels incidence graph, chooses a Middle Levels Hamilton target
through a protected source edge, and toggles the closed alternating
circuits in their symmetric difference.  This proves a q1-rainbow Hamilton
cycle, hence `eta_*=0`, without a private transparent-switch tree.

Accordingly plain cyclic q1 injectivity is closed once the direct
four-sector q1 factor exists.  The remaining correlated theorem is to find
the incidence circuits inside the subcatalogue which also preserves U1--U4
and admits the terminal common-cap state.  The fresh-q1 transporter handles
one endpoint compiler-cell alternative after such routing; it is not an
edge of either circuit graph and does not by itself protect the displaced
q1 target.  Upper-union support, residence, protected packet placement, and
the common-cap matching must still coexist with the selected circuits.

## 6. Replay

Run

```text
python3 scratch/audit_q1_sidecar_transporter_scope_20260801.py
```

which writes

```text
scratch/q1_sidecar_transporter_scope_20260801.audit.json
```

and verifies (2.1)--(2.4) and the complete one-path `U`-deck witness of
Section 3.
