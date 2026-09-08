# Interior rethreads, gain--Brauer transfer, and the first residence actuator census

Date: 2026-07-31  
Status: exact local transfer theorem; exact scoped m=5 C4/C6/C8/C10
census; one nonprivate residence-improving braid; no all-m actuator theorem

## 0. Verdict

The synchronized repaired m=5 Catalan forest has a stronger positive final
state than its immediate-turn certificate suggests. One colour-injective
42-connector closure covers the complete upper-union and lower-intersection
flag tower, and 46 cuts preserve that tower. However its 42 intact paths
contain 31 internal coordinate patterns 0-11-0. At depth \(d=2\) these are
residence defects, and no path permutation, reversal, or endpoint socket
choice can remove them.

The exact physical continuation is therefore an interior rethread. Its local
state is not just two endpoint masks. A proof-safe collar must carry:

1. its occurrence-labelled gain--Brauer pairing and gains;
2. separate lower/upper palette ledgers, including connector colours;
3. affected all-depth witness debt, equivalently internal witness sets and
   prefix/suffix union/intersection profiles;
4. the coordinate run automaton needed by residence;
5. directed boundary reachability; and
6. every visible private/literal resource capacity.

Equality of this complete signature makes a rethread exterior-transparent.
If the pairing or gain changes, the exact transition must instead be stacked
with the exterior and the one-cycle/primitive-voltage root test repeated.

There is a sharp finite result on the first actuator class. Exhaust all
palette-exact cyclic reassignments of two through five selected diamond
edges, keep the 42 connector edges fixed, and require unchanged endpoint
degrees, a 42-path forest, and one Hamilton closure. Among the resulting
C4/C6/C8/C10 rows:

* exactly four retain the old path pairing;
* exactly two of those retain at least one all-depth cut; and
* none improves the depth-two residence score.

A nonprivate C6 braid does improve it. It replaces

~~~text
(206,236) (214,220) (230,244)
~~~

by

~~~text
(206,220) (214,244) (230,236).
~~~

It preserves both forest palettes, the fixed colour-injective connectors,
one Hamilton cycle, and 47 all-depth cuts. Its best all-depth opening has
58 internal length-two and 13 internal length-one runs, versus 61+13 for
the source. Its path-pairing transition is two reciprocal 3-cycles, so it
is a three-path braid, not a private actuator. At this base \(h=1\), hence
its voltage is vacuous.

Finally, the 31 defect collars have exact old-edge transversal number 29.
Every resident final linear word must omit at least 29 old forest
adjacencies.  One of them may be omitted only by the final opening cut, so an
unrestricted rethread must delete at least 28 old forest edges; the bound is
29 when the opening is a connector or otherwise lies outside the defect
edge union.  Thus the displayed C6 is a genuine improving actuator, but it
cannot finish the compiler-ready rethread.

## 1. The exact m=5 boundary

Let \(F\) be the authenticated 252-vertex, 210-edge, 42-path forest in
\(J(10,5)\), and let \(C\) be the authenticated set of 42 connector edges.
The forest realizes every rank-four intersection and every rank-six union
once. The connector colours are injective separately on both shores, so the
closed cap-two profile is \(1^{168}2^{42}\) on each shore.

The cycle \(F\cup C\) covers every rank-\((5+q)\) union and rank-\((5-q)\)
intersection for \(q=1,\ldots,5\). Exactly 46 of its 252 cuts retain the
complete tower; 39 of those cuts lie in \(C\), leaving all 42 forest paths
intact.

Inside the path bodies are exactly 31 positive coordinate runs of length
two bounded by zeroes. They lie on 18 paths and have coordinate
multiplicities

\[
                         (5,5,2,3,3,3,3,3,3,1).       \tag{1.1}
\]

For \(D^2A=T\), every internal positive run of \(T\) must have length at
least three. Reversal preserves a bounded run and concatenation changes
only path-boundary runs. Therefore no intact-path opening is resident.
This is a no-go only for the fixed 42 path bodies, not for another Catalan
forest or an interior rethread.

## 2. Exact collar signature

Fix a rethread collar \(R\). Every occurrence which an exterior operation
may touch is exposed on a named boundary \(B\); every other shared literal
resource is placed in a visible ledger. A collar signature is

\[
 \Sigma_R=(P_R,\lambda_R,\mathcal Z_R,\mathcal P_R,\mathcal W_R,
           \mathcal R_R,\rho_R).                     \tag{2.1}
\]

Here:

* \(P_R\) pairs boundary occurrences joined by internal path fragments;
* \(\lambda_R\) is the antisymmetric gain on every oriented pair;
* \(\mathcal Z_R\) records every sealed cycle and its voltage;
* \(\mathcal P_R\) is the two-shore palette/connector-colour ledger;
* \(\mathcal W_R\) is the all-depth witness boundary state;
* \(\mathcal R_R\) contains both coordinate-run and directed-reachability
  states; and
* \(\rho_R\) records visible private edges, colours, ports and capacities.

The gain data use one common gauge on \(B\). A proper sealed cycle is
rejecting before the root. At the root there must be exactly one occurrence
cycle and its voltage must be primitive.

## 3. Physical and palette transfer

For a Johnson edge \(e=xy\) put

\[
                    \ell(e)=x\cap y,\qquad u(e)=x\cup y. \tag{3.1}
\]

### Lemma 3.1 (exact local palette row)

Suppose a rethread deletes forest edges \(E^-\), inserts \(E^+\), and leaves
every exterior forest edge fixed. It preserves the exact Catalan diamond
palettes if and only if

\[
 \{\!\{\ell(e):e\in E^-\}\!\}=\{\!\{\ell(e):e\in E^+\}\!\},\qquad
 \{\!\{u(e):e\in E^-\}\!\}=\{\!\{u(e):e\in E^+\}\!\}. \tag{3.2}
\]

If connector edges also change, their new lower labels must be mutually
distinct and avoid every unchanged connector lower label; the analogous
upper condition is independent and also required. These conditions are
equivalent to preserving the cap-two connector profile because the forest
already realizes every immediate colour exactly once.

#### Proof

Every unchanged forest edge realizes the same two labels before and after.
Since each target label has old multiplicity one, the residual deficits are
exactly the two multisets on the left of (3.2). The connector assertion is
the same multiplicity calculation with allowed final multiplicity two.
\(\square\)

Physical validity is separate: every inserted edge must be Johnson, the
new spanning graph must have maximum degree two and no cycle, and the
declared connector union must pass its degree and one-component tests.
Palette balance alone proves none of these.

## 4. All-depth witness transfer

Fix an opening word and a depth \(q\). Let \(A_q^-\) be the old
width-\((q+1)\) windows meeting a deleted adjacency or a changed collar
boundary, and define \(A_q^+\) analogously after the rethread. Windows
outside these sets are literal unchanged witnesses.

For an upper or lower target \(t\), let \(\mathcal O_q^-(t)\) be its old
witness windows. Define the residual debt

\[
 {\cal D}_q=\{t:\mathcal O_q^-(t)\subseteq A_q^-\}.    \tag{4.1}
\]

### Theorem 4.1 (exact affected-witness criterion)

The rethread preserves every old depth-\(q\) target if and only if every
\(t\in{\cal D}_q\) is realized by a new window in \(A_q^+\). It preserves
the full flag tower if and only if this holds separately for unions and
intersections at every required \(q\).

#### Proof

A target outside \({\cal D}_q\) has an old witness outside \(A_q^-\), hence
that witness survives literally. A target in \({\cal D}_q\) loses all old
witnesses and survives exactly when a new affected window realizes it.
\(\square\)

For composition, one sufficient exact representation of \(\mathcal W_R\)
stores all internal target labels plus boundary-port-indexed prefix and
suffix OR/AND profiles of every available length \(1,\ldots,q\), together
with capped fragment length/availability. Every window crossing a collar
boundary is one available suffix joined to one available prefix.  This is a
proof-safe representation, not a claim of minimality. Vertex-disjoint
collars are not automatically independent: an old target may have all its
witnesses split among them.

## 5. Residence and directed reachability

For depth \(d\), the coordinate-run state stores every internal short
positive run, the prefix/suffix bit and run length capped at \(d+1\), and an
all-one/whole-fragment flag with capped fragment length.  The flag records
whether the two terminal positive runs are the same run.  Concatenation
merges only the exposed terminal runs, using that identity flag.  This is the
exact finite run automaton for the residence test; prefix/suffix lengths
without the whole-fragment flag are not sufficient.

There is an independent directed row. For an ordered atom
\(q=(L,U,T,H)\), first delete residual atoms which reuse \(L,U,T,H\) in
their respective lower-palette, upper-palette, tail and head roles. Let
\(J\) already satisfy every remaining palette and head/tail-injectivity row.
Then \(J\) extends by \(q:T\to H\) if and only if:

1. \(J\) is acyclic; and
2. \(J\) contains no directed path \(H\leadsto T\).

Thus \(\mathcal R_R\) must also retain the reachability relation among
exposed directed ports. Atoms with tail \(H\) or head \(T\) are not deleted
merely for that reason; they may be part of the forbidden path.

The condition is necessary and sufficient because adding \(T\to H\)
creates a directed cycle exactly when \(H\leadsto T\) was already present.
This is the two-terminal contraction law of the Pascal determinant theorem.

## 6. Gain--Brauer action of an interior rethread

Let the old and new collar pairings on the same named boundary be
\(P^-,P^+\). In one gauge their relative routing element is

\[
                              T_R=P^+P^-.             \tag{6.1}
\]

If the boundary changes, use gain--Brauer stacking rather than (6.1).
For a fixed exterior connector involution \(M\), the new root topology and
voltage are extracted from \(MP^+\). No local palette or witness condition
can replace this calculation.

For a two-terminal private segment replacement \(Q^-\to Q^+\) with the
same root-oriented endpoints, put

\[
                  \delta=g(Q^+)-g(Q^-)\pmod h.        \tag{6.2}
\]

The underlying boundary pairing is unchanged and the root voltage changes
by the root-oriented signed occurrence of \(\delta\) on the root cycle;
reverse traversal contributes \(-\delta\). Hence:

* a voltage-neutral actuator has \(\delta=0\);
* for inherited voltage \(v\), a chosen defect is primitive-safe exactly
  when \(\gcd(v+\delta,h)=1\); and
* jointly independently selectable private menus with root-oriented defect
  sumset \(S\) work for every inherited voltage exactly when
  \(S+U_h=\mathbb Z_h\).

If \(P^+P^-\) has nontrivial permutation part, the actuator is not private
in the path-pairing coordinate even when the old connector set still closes
one cycle.

### Theorem 6.1 (exact exported actuator criterion)

Assume no hidden reopening: every resource which an exterior continuation
may touch is either named on the boundary or represented in \(\Sigma_R\).
A collar replacement is a proof-safe exported transition exactly when it:

1. is a valid Johnson linear-forest replacement;
2. satisfies the two exact palette ledgers and connector-colour capacities;
3. discharges every current affected all-depth witness debt and exports the
   exact witness boundary state \(\mathcal W_R\);
4. exports its exact coordinate-run and directed-reachability boundary
   states \(\mathcal R_R\);
5. exports its exact gain--Brauer pairing/gain transition and sealed-cycle
   ledger \(\mathcal Z_R\); and
6. satisfies and exports every visible private/literal resource row.

For a specified exterior, the replacement is accepted exactly when stacking
these exported states gives an accepting run/reachability state, no proper
sealed cycle, one root occurrence cycle of primitive voltage, and all final
resource rows. If the
old and new complete signatures are equal, the replacement is
exterior-transparent. If only item 5 changes, the one-cycle and
primitive-voltage tests cannot be omitted.

#### Proof

Items 1--4 are Lemma 3.1, Theorem 4.1, the run automaton and the exact
reachability contraction law. Items 5--6 are precisely the complete
gain--Brauer/resource boundary signature. Each final predicate depends only
on the corresponding exported state, so associative stacking is necessary
and sufficient for the specified exterior. Equal signatures are therefore
interchangeable under every declared exterior. If a transition is exposed
instead, stacking computes the exact new root.
\(\square\)

Neutrality on the complete signature is sufficient for universal
independent exterior transparency. Disjoint physical vertices alone do not
separate all-depth witnesses or directed reachability. Nonneutral disjoint
transitions may still compose for a specified exterior, but their exported
states must be stacked jointly (or conservatively treated as one atomic
controlled-debt macro).

## 7. A 29-edge residence hitting theorem

Every internal 0-11-0 defect on path vertices \(v_0v_1v_2v_3\) is forced
by its three old adjacencies

\[
                 v_0v_1,\quad v_1v_2,\quad v_2v_3.   \tag{7.1}
\]

If all three remain adjacencies of the final linear word--that is, they
survive the rethread and none is the opening cut--the four vertices remain
consecutive, possibly reversed, and the same coordinate defect remains.
Thus every resident final word must omit at least one edge from each
three-edge set (7.1).

### Theorem 7.1 (exact source-adjacency hitting number)

For the authenticated 42 paths, the 31 defect sets (7.1) are distinct,
lie on 18 paths, and their old-edge transversal number is

\[
                                  \tau=29.            \tag{7.2}
\]

Consequently every resident final linear word obtained from this source
omits at least 29 old forest adjacencies.  At most one such omission can be
the final opening cut.  Hence at least 28 old forest edges must be deleted by
the rethread itself; at least 29 must be deleted when the opening cut is not
an old edge belonging to a defect collar.

#### Proof

On each path the defect sets are intervals of three consecutive edge
indices. Stabbing intervals by repeatedly selecting the right endpoint of
the earliest-ending unstabbed interval is optimal. Applying this
independently on the 18 disjoint path lines gives 29 selected edges. The
audit also exhausts every smaller subset of the participating edge indices
on each path, independently reproducing the same per-path minima. Their
sum is 29. \(\square\)

This is a lower bound on old adjacencies absent from the final word, not on
the number of abstract macro stages: one stage may replace many edges, and
one absence may be supplied by the final cut. It proves no existence of a
28- or 29-edge repair.

## 8. Exact minimal actuator census

A size-\(s\) connected palette cycle chooses selected diamonds
\((L_i,U_i)\), \(i\in\mathbb Z_s\), and replaces them by
\((L_i,U_{i+1})\). This is a \(C_{2s}\) alternating cycle in the diamond
incidence graph. The audit exhausts \(s=2,3,4,5\), then requires:

* the same physical endpoint-degree multiset;
* no collision with an unchanged forest edge;
* a spanning 42-path forest;
* the original 42 connectors unchanged; and
* one Hamilton connector closure.

The exact row counts are:

| size | palette cycles | same endpoint multiset | fixed-connector Hamilton | all-depth | same path pairing | pairing-private + all-depth | pairing-private residence improver |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 171 | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | 969 | 74 | 34 | 19 | 3 | 1 | 0 |
| 4 | 8,367 | 13 | 8 | 5 | 1 | 1 | 0 |
| 5 | 95,544 | 130 | 44 | 23 | 0 | 0 | 0 |

Thus there is no pairing-private, all-depth, short-run-score-improving
actuator among the single connected C4/C6/C8/C10 fixed-connector cycles.
Disconnected unions such as C4+C4 are outside the census. Equality of the full
signature from Theorem 6.1 is stronger than pairing privacy, so in particular
there is no fully-signature-private, all-depth, short-run-score-improving
actuator in this class. The positive rows were not
promoted merely from matching endpoint degrees: every accepted row also
passes the literal forest and fixed-connector Hamilton tests.

The best nonprivate row is the C6 displayed in Section 0. Its source best
all-depth opening has short-run histogram \(1^{13}2^{61}\); the output has
\(1^{13}2^{58}\). Its path-pairing transition \(P^+P^-\) has cycle type
\(3^2\), explicitly

~~~text
((9,0) (11,1) (12,0))
((9,1) (12,1) (11,0)).
~~~

The fixed connectors nevertheless close the rethreaded forest to one
cycle. This is a positive three-path actuator and an exact demonstration
that path-pairing change, rather than palette or all-depth loss, is the
first missing private resource. It is not residence-complete and supplies
no nontrivial-voltage evidence because \(h=1\).

## 9. Why boundary reachability is algebraically necessary

The Pascal determinant split rules out the scalar two-full-parent product.
Let \(K'=\operatorname{Cat}_{m-1}\), \(M'=mK'\),
\(N'=(m-1)K'\), and \(K=\operatorname{Cat}_m\). Two complete canonical
parent copies force \(K\) cross edges between their middle rails, so the
induced graph has

\[
 |V|=2M',\qquad |E|=2N'+K,\qquad
 |E|-|V|=K-2K'=\frac{2(m-2)}{m+1}K'\ge0.            \tag{9.1}
\]

It therefore contains a cycle. This excludes wholesale preservation of
the two canonical complete parents, not every Pascal braid. Exact atom
contraction also requires the no-\(H\leadsto T\) state from Section 5.
Boundary-deficient rails and reachability are consequently necessary for
this recursion architecture, not optional solver metadata.

## 10. Uniform target and scope

The proof-safe central target is:

> a controlled-debt packet of bounded-port circuits, followed by an ordered
> fixed-decoration transparent leaf-peelable gluing list, and then an
> interior rethread satisfying Theorem 6.1 and residence.

The packet cardinality may grow with the defect structure. What a finite
recursive interface must bound is the live named boundary and exposed
linkage debt at each composition cut, while sealed history is forgotten.
That bounded-live-interface property is a required all-m hypothesis; it
does not follow merely because each circuit has bounded arity. At m=5 only
the finite debt staircase and common-core linkage are known, and its
augmenting paths may be global.

This note proves neither a private residence actuator beyond the scoped
C10 census nor an all-m interior-rethread theorem.  Item 2188 now supplies a
separate residence-clean `m=5` forest obtained by a much larger interior
rethread (119 changed matching partners).  The finite frontier has therefore
moved to the socket interface.  The separate two-dead-socket theorem now
proves that no endpoint-only chronology of those 42 fixed path bodies can be
resident: both ports of one component have pair-safe degree zero.  The next
actuator must change at least that component's interior/socket trace while
carrying its all-depth witness, gain--Brauer and compiler states explicitly.

## 11. Reproduction

Run

~~~text
python3 scratch/audit_catalan_m5_interior_rethread_actuator_20260731.py
~~~

The audit authenticates the forest/connector projection, independently
replays the 31 defect collars and \(\tau=29\), exhausts every palette cycle
of sizes two through five, replays all-depth support at every output cut,
checks the fixed connector closure, computes path-pairing transitions, and
counts all internal length-one/two residence defects.

The source projection SHA-256 is
d8ad508994409547516e0c3c07452eb17585465e0edb8511558d4ccaac4b7ad3.
