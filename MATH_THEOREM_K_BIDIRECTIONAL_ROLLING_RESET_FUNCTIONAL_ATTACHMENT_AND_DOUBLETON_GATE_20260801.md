# Bidirectional rolling reset: exact functional-attachment exchange and the closed-doubleton gate

**Date:** 2026-08-01  
**Lane:** K, protected common rounding  
**Status:** unconditional local theorem and scoped obstruction.  The two
orientations of the rolling reset are all-depth static alternatives and give
two exact functional attachments.  On the closed ring their attachment
overlay is one alternating cycle and their protected predecessor factors
are inverse cycles.  On an opened ring the phase switch transports one
head-owner defect and two parity predecessor defects to the opposite
endpoints.  It is therefore a useful prospective exchange path, but it is
not intrinsically augmenting.  Edgewise phase mixing creates a literal
closed doubleton and repeats an owner.  A useful opened exchange needs an
external owner return and external predecessor linkages with one common
literal turn-triple lift.  Separate projection paths are only necessary.
Connectivity,
voltage, residence outside the packet, arbitrary upper shadows, and the
compiler are not claimed.

## 0. Notation and outcome

Assume \(d\ge2\), and put

\[
                         N=2(d+1)=2n,
\]

and read indices modulo \(N\).  Let \(X_0,\ldots,X_{N-1}\) be the private
coordinates of the two-queue ring and let \(K\) be its fixed core.  The
rank-\(r\) reset roots and their adjacent rank-\(r+1\) owners are

\[
 T_a=K\cup\{X_a,X_{a+1},\ldots,X_{a+n-1}\},                  \tag{0.1}
\]

\[
 U_a=T_a\cup T_{a+1}
    =K\cup\{X_a,X_{a+1},\ldots,X_{a+n}\}.                    \tag{0.2}
\]

There are two complete flag phases on the same roots:

\[
 f_a^{\rightarrow}
   =(T_a;X_a,X_{a+1},\ldots,X_{a+d-2}),                      \tag{0.3}
\]

\[
 f_a^{\leftarrow}
   =(T_a;X_{a+n-1},X_{a+n-2},\ldots,X_{a+2}).                 \tag{0.4}
\]

The forward phase has protected turns

\[
                         T_a\longrightarrow T_{a+1},          \tag{0.5}
\]

and the reverse phase has

\[
                         T_a\longrightarrow T_{a-1}.          \tag{0.6}
\]

Both are literal depth-\(d\) turns.

The exact conclusions are:

1. The two phases have identical root, owner, every-depth suffix-row,
   immediate-lower, and immediate-upper multisets.
2. Their functional attachments are

   \[
       \theta_{\rightarrow}(T_b)=U_{b-1},\qquad
       \theta_{\leftarrow}(T_b)=U_b.                          \tag{0.7}
   \]

   Their overlay is one alternating \(2N\)-edge cycle in the
   head--owner incidence graph.
3. Within the reset roots, the corresponding predecessor sets are

   \[
     P_{\rightarrow}(T_b)\cap\{T_a\}=\{T_{b-1}\},\qquad
     P_{\leftarrow}(T_b)\cap\{T_a\}=\{T_{b+1}\}.              \tag{0.8}
   \]

4. Selecting both directions of one reset edge is exactly the forbidden
   closed-doubleton transposition and repeats owner \(U_a\).  Consequently
   every owner-injective neighbour factor on the closed reset cycle is one
   of the two uniform phases.
5. After deleting one seam, the owner-attachment overlay is one alternating
   path, while the protected predecessor overlay is two alternating parity
   paths.  Switching phase is exact only when the ambient carrier supplies
   one owner return and both predecessor endpoint linkages.  The reset
   itself supplies no positive matching gain.

## 1. Both orientations are all-depth static alternatives

### Theorem 1.1 (bidirectional static transparency)

The tables \(\{f_a^{\rightarrow}\}\) and
\(\{f_a^{\leftarrow}\}\) use the same roots, and for every
\(1\le j<d\) they use the same multiset of rank-\((r-j)\) suffix rows.
They also use the same immediate lower and upper palettes and have the same
residence inventory.

#### Proof

The depth-\(j\) forward suffix at root \(T_a\) is

\[
 K\cup\{X_{a+j},X_{a+j+1},\ldots,X_{a+n-1}\},                \tag{1.1}
\]

a cyclic interval of \(n-j\) private coordinates.  The reverse suffix is

\[
 K\cup\{X_a,X_{a+1},\ldots,X_{a+n-j-1}\},                    \tag{1.2}
\]

also a cyclic interval of length \(n-j\).  As \(a\) runs modulo \(N\),
equations (1.1) and (1.2) run through the same interval family.

Both phases use every root \(T_a\).  Their directed edges are the two
orientations of the same undirected Johnson cycle, so their intersections
and unions are the common sets \(I_a=T_a\cap T_{a+1}\) and \(U_a\).
Finally, reversing the chronology reverses but does not change any cyclic
coordinate-run length. \(\square\)

Thus optional marked suffix occurrences can be transferred phasewise.  The
theorem is static: it does not say that either phase has the same legal
external predecessors as the other.

## 2. Exact functional attachment and predecessor effect

### Theorem 2.1 (closed-ring functional phase exchange)

Equations (0.7) define two bijections from the reset heads to the reset
owners.  The symmetric difference of their attachment columns is the one
alternating cycle

\[
 T_0-U_0-T_1-U_1-\cdots-T_{N-1}-U_{N-1}-T_0.                 \tag{2.1}
\]

In the forward phase, the protected predecessor of head \(T_b\) is
\(T_{b-1}\); in the reverse phase it is \(T_{b+1}\).  Among reset roots
these predecessors are unique, proving (0.8).

#### Proof

The turn entering \(T_b\) from \(T_{b-1}\) has union \(U_{b-1}\), while
the reverse turn entering it from \(T_{b+1}\) has union \(U_b\).  This gives
(0.7) and (2.1).

The rank-\((r+1)\) set \(U_{b-1}\) contains the two adjacent reset roots
\(T_{b-1},T_b\).  Every other reset window omits at least one element of
their union, so no other reset root is a facet of \(U_{b-1}\).  Excluding
the stuttering head leaves only \(T_{b-1}\) as a reset predecessor.
The reverse statement is identical.  Literal legality follows directly
from the shifted queues (0.3)--(0.4). \(\square\)

The last statement is deliberately intersected with the reset bank.
External predecessor sets depend on the ambient selected flags and may
change substantially when the phase is reversed.  No equality of the full
sets \(P_F(a)\) is asserted.

### Corollary 2.2

On the closed ring, toggling all attachment columns from
\(\theta_{\rightarrow}\) to \(\theta_{\leftarrow}\) is one legal
owner-alternating-cycle exchange.  Toggling all protected predecessor edges
reverses one directed reset cycle.  Both phases are exact functional cycle
covers of the packet, but both leave it as a closed component.  Hence the
closed exchange is reset-transparent but gives no Hall augmentation and no
topological merge.

## 3. The owner two-cycle and closed-doubleton hazard

At the edge between \(T_a\) and \(T_{a+1}\), the forward turn deletes
\(X_a\) and adds \(X_{a+n}\).  The reverse turn deletes \(X_{a+n}\) and adds
\(X_a\).  Their common owner base is

\[
                         I_a=T_a\cap T_{a+1}.                  \tag{3.1}
\]

### Theorem 3.1 (phase rigidity under owner injectivity)

The two orientations of one reset edge form the local directed
transposition

\[
                         X_a\longleftrightarrow X_{a+n}.       \tag{3.2}
\]

They both have owner

\[
                         I_a\cup\{X_a,X_{a+n}\}=U_a.          \tag{3.3}
\]

Thus selecting both is exactly a closed doubleton: the unique local
derangement is a two-cycle and repeats its owner.

More generally, let \(\sigma\) be a permutation of the reset roots with

\[
                         \sigma(T_a)\in\{T_{a-1},T_{a+1}\}.   \tag{3.4}
\]

If its selected turns have distinct owners, then \(\sigma\) is either the
uniform forward cycle or the uniform reverse cycle.

#### Proof

Equations (3.2)--(3.3) prove the first statement and identify it with the
closed-doubleton criterion.

For the second, every component of a neighbour permutation on a simple
cycle is either the whole cycle with one uniform orientation or a directed
two-cycle on one edge.  Indeed, if \(T_a\to T_{a+1}\) and the edge is not a
two-cycle, then \(T_{a+1}\) cannot point back to \(T_a\), so it must point
to \(T_{a+2}\).  Iteration forces the forward orientation around the cycle;
the first reversal would itself create a two-cycle with the preceding
forward edge.  The reverse case is symmetric.  Every two-cycle repeats
the corresponding owner by (3.3), so owner injectivity excludes it.
\(\square\)

Accordingly, the bidirectional reset is an **all-at-once alternating
exchange**, not a bank of independently switchable edge bits.  Any proposed
interpolation between phases must either leave a root unmatched or create a
closed doubleton.

## 4. Opening one seam: exact boundary transport

Delete the seam owner edge between \(T_{N-1}\) and \(T_0\).  Put

\[
 \begin{aligned}
 D_{\rightarrow}&=\{(T_{a+1},U_a):0\le a<N-1\},\\
 D_{\leftarrow}&=\{(T_a,U_a):0\le a<N-1\}.
 \end{aligned}                                                \tag{4.1}
\]

These are the internal head--owner attachment matchings.  Similarly put

\[
 \begin{aligned}
 M_{\rightarrow}&=\{T_a^-T_{a+1}^+:0\le a<N-1\},\\
 M_{\leftarrow}&=\{T_{a+1}^-T_a^+:0\le a<N-1\}.
 \end{aligned}                                                \tag{4.2}
\]

### Theorem 4.1 (opened reset exchange signature)

The two attachment matchings in (4.1) use the same owners
\(U_0,\ldots,U_{N-2}\).  Their symmetric difference is one alternating path
with head endpoints \(T_0,T_{N-1}\).

The two predecessor matchings in (4.2) each have size \(N-1\).  Their
symmetric difference is the disjoint union of the parity paths

\[
 T_0^- -T_1^+ -T_2^- -T_3^+ -\cdots- T_{N-1}^+,              \tag{4.3}
\]

and

\[
 T_0^+ -T_1^- -T_2^+ -T_3^- -\cdots- T_{N-1}^-.              \tag{4.4}
\]

Here (4.3) has endpoints \(T_0^-,T_{N-1}^+\), while (4.4) has endpoints
\(T_0^+,T_{N-1}^-\).

#### Proof

In (4.1), owner \(U_a\) is incident with head \(T_{a+1}\) in the forward
matching and head \(T_a\) in the reverse matching.  Chaining these
alternately gives one path through all displayed heads and owners.

For (4.2), alternation changes the root index by two.  Since \(N\) is even,
there are exactly two parity components.  Writing them from their boundary
vertices gives (4.3)--(4.4). \(\square\)

Thus reversing the opened reset transports the attachment defect from one
head endpoint to the other and simultaneously transports two predecessor
boundary defects.  It does not erase them.

## 5. Exact ambient completion criterion

Call a pair of outside turn sets
`(E_out^right,E_out^left)` a **compatible three-return lift** if:

1. each set is a matching of literal tail--head--owner triples jointly
   supported by one consistent flag table extending the corresponding
   reset phase;
2. the two resulting global tables have the same declared static suffix
   resources outside the reset;
3. the head--owner projection of the outside symmetric difference is an
   attachment return closing the attachment path of Theorem 4.1, and its
   tail--head projection consists of returns closing both predecessor paths;
4. every projected attachment edge and predecessor edge selected at a head
   are the projections of the same literal triple.

Both outside matchings avoid internal reset resources except at their
declared endpoints.  Equivalently, unioning `E_out^right` or `E_out^left`
with its internal reset phase gives two three-shore matchings on the same
tail, head, and owner resource sets.

This compatibility clause is load-bearing: arbitrary head--owner and
tail--head alternating paths need not pair to legal triples.

### Theorem 5.1 (reset-transparent functional exchange criterion)

Let a global selected flag table contain one opened rolling-reset phase.
An all-at-once switch to the opposite phase extends to another exact
functional owner attachment and another perfect predecessor matching if
the ambient support supplies a compatible three-return lift whose
projections consist of:

1. an attachment-alternating return path, outside the internal reset
   columns, joining the two head endpoints of the path in Theorem 4.1; and
2. predecessor-alternating return paths which close both parity paths
   (4.3)--(4.4).

Toggling the internal paths together with these returns preserves every
head, owner, tail, and static suffix resource.  Conversely, if the outside
attachment and predecessor matchings are held fixed, the phase switch is
impossible: their unmatched endpoint sets differ exactly by the endpoints
listed in Theorem 4.1.

#### Proof

The symmetric difference of two matchings is a disjoint union of alternating
cycles and alternating paths.  The internal attachment difference is the
one path of Theorem 4.1; adding the first return makes it an alternating
cycle, whose toggle preserves the attachment perfect matching.

The predecessor difference consists of exactly the two paths (4.3)--(4.4).
The two external returns make alternating cycles, and toggling them preserves
the predecessor perfect matching.  Compatibility of the lift says that
these projection toggles select the same literal tail--head--owner triples,
rather than unrelated projection matchings.  Theorem 1.1 preserves all
static flag resources.  The converse follows because, without changing
outside edges, the endpoint degree differences of the three internal paths
remain nonzero.
\(\square\)

### Corollary 5.2 (no intrinsic augmentation)

The two internal phases have equal attachment cardinality and equal
predecessor cardinality.  Therefore toggling only the internal reset edges
cannot increase the cardinality of either selected matching.  Any global
Hall gain must use an ambient return that reaches a previously unmatched
or deficient shore, rather than merely closing the internal alternating
paths.  Equivalently, the reset is a bounded-state **defect transporter**,
not by itself a positive-gain absorber.

The direct one-column completion in either phase uses the omitted seam owner
\(U_{N-1}\): it is the unique rank-\((r+1)\) set containing both endpoint
roots \(T_0,T_{N-1}\).  The forward and reverse completions use its two
alternative endpoint columns.  Either closes the reset ring and recreates
the isolated component.  Hence any topology-useful functional exchange
needs a nontrivial ambient owner return.

At predecessor level, the two direct seam directions are

\[
                         T_{N-1}\to T_0,qquad
                         T_0\to T_{N-1}.                       \tag{5.1}
\]

They are the opposite orientations of one owner \(U_{N-1}\).  Selecting
both in one factor is the closed doubleton of Theorem 3.1; selecting one
merely closes one reset orientation.  Thus direct seam closure does not
give the desired open augmenting exchange.

## 6. Consequence for prospective functional attachment

The rolling reset does supply a useful exact gadget, but its correct state
is larger than a single attachment bit.  It exports

\[
 \boxed{\text{one head--owner alternating endpoint pair}
       +\text{two parity predecessor endpoint pairs}.}       \tag{6.1}
\]

A prospective construction may reserve a common literal lift of those three
returns while choosing the ambient SCD flags and the functional attachment
\(\theta\).  Once the lift is present, Theorem 5.1 gives an exact
reset-transparent exchange; one may then choose the phase whose transported
endpoints meet the desired Dulmage--Mendelsohn shore.

What is not justified is treating the reset orientations as independent
local choices, or inferring a Hall gain from their equal static ledgers.
The exact next theorem is:

> **Rolling-reset return-linkage lemma.**  In the prospectively selected
> zero-boundary flag table, every prepared reset bank has one external
> owner-alternating return and two predecessor returns, one of which reaches
> the current deficient DM shore, and all three are projections of one
> common literal turn-triple trade.

The robust-order portal theorem gives large local turn lists at a bounded
prepared bank, but it does not yet supply these correlated three returns.
Owner two-cycle avoidance and the closed-component exclusion must be imposed
explicitly.

## 7. Scope

Every identity above is uniform for \(d\ge2\) and uses no finite
computation.  The degenerate depth-one case has no protected deletion
coordinate and is intentionally outside the flag-table statement.
The negative statements concern the standard two-queue reset and its
functional-attachment face.  A nonstandard packet may couple the owner and
two predecessor returns internally, and is not ruled out.  No conclusion
about the existence of the global common selector is drawn.

The derivation is bound to the following inputs:

```text
7634f77868a190773bba680a18a709d439a2b16c8b50d773332b824838b1cae1
  MATH_THEOREM_TWO_QUEUE_ROLLING_GUARDED_RESET_20260801.md

c45e01cb8ee2a67e776286db6d51642426158ff85b51e6887daa26fa36f2433a
  MATH_THEOREM_NECKLACE_SELECTOR_ROLLING_RESET_COEXISTENCE_AND_K17_CERTIFICATE_20260801.md

5647ac545ddcafa37e4ada27d3105c00c6f4739eb6956072ac0876b5de4ba9f6
  MATH_THEOREM_K17_RESET_CONDITIONED_THREE_MATROID_AND_FUNCTIONAL_FLOW_GATE_20260801.md

8c3b02920dc3fe0a658d3f36de19cbb943067ee23456978c4f77889015d8c40c
  MATH_THEOREM_K_OVERLAP_CORE_FLOW_AND_ROOT_COLOURED_CIRCULATION_GATE_20260801.md
```
