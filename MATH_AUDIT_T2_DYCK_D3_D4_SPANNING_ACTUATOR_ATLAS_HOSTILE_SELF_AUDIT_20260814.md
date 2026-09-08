# Hostile self-audit of the `T2` `D_3/D_4` suffix-actuator atlas

**Date:** 2026-08-14
**Object audited:**
`MATH_THEOREM_T2_DYCK_D3_D4_SPANNING_ACTUATOR_ATLAS_AND_CONTEXT_GATE_20260813.md`
**Status:** **PASS** for the finite `D_3` and `D_4` construction after the
scope corrections below; **OPEN** for an insertion-closed all-semilength
actuator grammar and for a physical common-history/residence lift.  This is a
hostile self-audit, not an independent audit.

## 1. Audit boundary

The audited theorem makes four logically separate claims.

1. Four frozen circuits give a resource-disjoint, q2-safe suffix-tree
   actuator on `D_3` whose simultaneous component action has one output.
2. Every edge of the 47-edge transposition graph on `D_4` has a q2-safe
   alternating circuit, and a selected thirteen-edge label arborescence has
   pairwise disjoint owner/colour resources and one simultaneous component
   output.
3. The minimum circuit lengths are exact in a stated admissible class.
4. The finite constructions do not yet give undilated residence or a Catalan
   recursion closed under left insertion/primitive wrapping.

The audit deliberately does **not** infer a source realization from a factor
circuit, a component hypertree from a suffix-label tree, or an all-`s`
construction from right-tail tensoring.

## 2. Scope correction: the minimum class

The enumeration restricts path vertices to owners of degree two in the
post-`T2` owner--q1 factor.  This is the internal-owner class in which every
toggled row has a well-defined untouched mate and hence an exact selected-q2
current.  It is also the class relevant to the proposed turn-faithful source
lift.

Therefore the certified words “shortest” and “minimum” mean:

> shortest owner-simple and colour-simple q2-safe alternating circuit through
> the two named suffix representatives, with every circuit owner internal in
> the post-`T2` factor, over the stated prefix channels.

They do not compare against circuits using a degree-one endpoint owner.  The
audited theorem now says this at the definition, theorem, and certificate
sites.

## 3. `D_3` replay

The frozen verifier independently rebuilds the canonical factor at `m=9`,
applies all `T2` packets, and checks the four literal circuits.  It certifies:

```text
suffix vertices                 5
selected suffix edges           4 (a tree)
selected lengths                C16,C16,C18,C16
pairwise owner disjoint         yes
pairwise q1-colour disjoint     yes
aggregate q2 support loss       0
base components met             27
simultaneous output components  1
component reduction             26
output shore owner length       893 = 47*19
```

Every individual circuit has arity eight and reduction seven.  The
component--trade incidence graph of the four circuits nevertheless has two
independent hypercycles; the one-output statement is proved by traversal,
not by the sufficient hypertree theorem.

The all-six-prefix strict-shorter audit exhausts every admissible path split
below each frozen incumbent.  It finds exact minima `C16,C16,C18,C16`.
Several channels have a directed-distance bound at the incumbent and hence
no strict-shorter label-simple circuit to enumerate; this is a valid
distance proof, not a missing loop.

## 4. `D_4` minimum atlas and selection replay

The two-channel exhaustive search enumerates from the directed-distance
bound through the first q2-safe length on every suffix edge.  It establishes
the histogram

```text
C14:3  C16:15  C18:11  C20:9  C22:8  C24:1.
```

For the other four `T2` prefix channels, a separate audit exhausts all
admissible circuits strictly below each two-channel incumbent.  It finds no
improvement on any of the 47 edges and reproduces the histogram.  The two
runs together, not either one alone, prove all-six-prefix admissible
minimality.

The main search retains at most 160 witnesses after reaching the first safe
length.  That cap can restrict the subsequent SAT selection, but cannot
change existence or minimality at the reported length: every shorter length
was exhausted before witness retention begins.

The independent frozen-certificate verifier checks the thirteen selected
circuits without trusting the SAT encoding.  It reconstructs every old/new
incidence, internal-owner condition, suffix endpoint occurrence,
owner/colour disjointness, arborescence orientation, q2 current, component
traversal, common intersection, palette current, and residence collar.  Its
global result is:

```text
suffix vertices                 14
selected label edges            13 (a rooted arborescence)
selected lengths                C14:1,C16:6,C18:5,C20:1
base components met             82
simultaneous output components  1
component reduction             81
output shore owner length       2898 = 138*21
aggregate q2 support loss       0
```

The selected suffix arborescence is a tree only in the 14-vertex label
graph.  Individual actuator component supports overlap, and one selected
`C14` circuit meets six base components but reduces the global component
count by only four.  The theorem therefore makes no component-hypertree
claim.  Its simultaneous one-output conclusion is the exact traversal
certificate.

## 5. PR-path obstruction scope

The PR-path CNF is UNSAT for choosing one circuit per edge from the enumerated
shortest internal-owner candidate classes in the two productive prefix
channels, subject to pairwise owner/colour disjointness.  Arc consistency
leaves every domain unchanged, so the incompatibility is genuinely global
within that finite menu.

This does **not** rule out:

* shortest candidates from another prefix channel;
* longer circuits;
* controlled component or incidence overlap;
* a different Catalan spanning-tree recursion.

The theorem now states exactly this limited obstruction.

## 6. Residence and common-history audit

At `D_3`, all four individual circuits have bad upper and lower `2`-collars.
At `D_4`, every selected circuit has at least one bad shore; one circuit has
zero bad lower collars but still has three bad upper collars.  The
simultaneous results are:

```text
             bad upper q2 collars   bad lower q2 collars   min seam gap
D_3                    18                     14                 1/1
D_4                    51                     40                 1/1
```

Hence there is no undilated two-shore residence theorem.  The finite common
intersections are only algebraic feasibility data.  The upper common-core
ranks in the selected `D_4` circuits are `7` or `8`; lower ranks range from
`2` through `6`, and every lower palette has a nonzero loss current.

The common-intersection lift additionally requires occurrence-disjoint,
cut-separated source fragments.  At width `d+3`, the selected q2 ledger is
carried only by a turn-faithful planting with both endpoint mates, or by a
direct joint cut-current audit.  Neither physical planting is in the finite
certificate.  It is therefore correct to call common-history lifting
prospective and residence-dilated.

## 7. Context audit

Right concatenation by a common Dyck tail preserves the MSW insertion and
deletion orders, factor incidences, q2 backups, and finite component action.
It gives a valid tensor family.  Different right tails remain separate
blocks, so this operation alone does not connect the Catalan suffix graph.

The transformations `X -> 10X` and `X -> 1X0` change the MSW prefix phase.
No functorial incidence identity analogous to right concatenation has been
proved for them.  Consequently the `D_3/D_4` atlas is finite evidence, not a
finite template grammar closed under all Catalan context insertions.

## 8. Verdict and exact remaining gate

The finite topology result survives hostile review: the aligned `C16`
matching is not the end of the method, because explicit q2-safe disjoint
actuators span `D_3` and `D_4` and have a one-orbit simultaneous component
action.  The exact remaining gate is the conjunction

\[
 \boxed{\begin{array}{c}
 \text{a finite symbolic actuator set closed under the left/context moves of}\
 \text{a spanning Catalan recursion, with a globally compatible selection;}\\
 \text{an occurrence-disjoint, cut-separated, residence-dilated, two-turn}\
 \text{common-history planting for that selection.}
 \end{array}}
\]

No finite computation reported here proves either line for unbounded `s`.
