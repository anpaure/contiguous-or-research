# Rolling-reset three-return gate: the strict-gammoid 3-circuit and the private-sink repair

**Date:** 2026-08-01  
**Lane:** L, terminal compiler / occurrence-labelled lift  
**Status:** exact direct and fixed-cap obstructions; exact conditional
private-sink/root-slot repair; exact two-matroid criterion on the separated
typed singleton-hazard face.
The statements below concern the compiler/linkage interface exported by the
opened bidirectional rolling reset.  They do not construct the three ambient
returns in a Boolean chronology, and they do not claim a regenerative
compiler.

## 0. Outcome

An opened rolling reset exports three typed endpoint pairs:

1. one head--owner alternating endpoint pair, denoted \(O\); and
2. two predecessor-parity endpoint pairs, denoted \(P_0,P_1\).

There are two logically different linkage problems.

* The **chronology linkages** close those three alternating paths in the
  owner and predecessor matching graphs.
* The **compiler relocations** move every occurrence-labelled compiler cell
  made unavailable by the chosen returns to unused cells of one fixed cap
  state.

Disjoint chronology paths do not imply disjoint compiler relocations.  In
fact, even if all three chronology returns are fixed, mutually
resource-disjoint, and every proper subfamily is compiler-safe, the triple
can fail.  The smallest obstruction is the rank-two 3-circuit

\[
                             U_{2,3}.                         \tag{0.1}
\]

It is realized by one compiler target and three distinct occurrence cells.
Thus neither individual nor pairwise return feasibility supplies the three
returns required by the rolling-reset theorem.

There is nevertheless an exact positive interface.  Let \(D_O,D_0,D_1\)
be the compiler hazard cells of the three returns in one fixed cap
\(\theta\), put \(D=D_O\cup D_0\cup D_1\), and assume installation has
the deletion-only fixed-cap semantics of Section 1.  They coexist with the
compiler precisely when

\[
       D\text{ is independent in }M_\theta^*,                 \tag{0.2}
\]

where \(M_\theta^*\) is the strict gammoid dual to the compiler
transversal matroid.  Equivalently, all hazard cells admit simultaneous
vertex-disjoint alternating relocations to distinct unmatched-cell sinks.
A source-private version, with one disjoint relocation block for each
return, is a transparent sufficient hypothesis.  For an allowed deletion
family \(\mathcal F_B\), the exact robust row is

\[
 r_{M_\theta^*}(D_O\cup D_0\cup D_1\cup F)
       =|D_O\cup D_0\cup D_1\cup F|
       \qquad(F\in\mathcal F_B).                              \tag{0.3}
\]

The abstract Boolean root-slot reserve proves (0.3) only after a literal
trace-guarded root-slot injection has been supplied.  The current collared
pivot has a two-flag physical column, not that universal injection, so it
does not by itself close the three-return gate.

Prospective **selection** is generally a three-matroid/packet problem.  It
reduces to ordinary two-matroid intersection only on the stronger separated
typed-corridor face: the three return types are absorbed into a direct-sum
rank-three gammoid, every triple is aligned-column compatible, and every
candidate has a singleton compiler hazard (or an automatic certified
root-fibre hazard).  Section 3 gives the exact Edmonds rank row on that
face.

There is also an earlier physical obstruction to the most literal direct
closure.  All three endpoint pairs project to the same two reset roots
\(T_0,T_{N-1}\), whose unique common rank-\((r+1)\) owner is
\(U_{N-1}\).  Hence three direct same-neighbour closures have demand three
on an owner resource of capacity one.  The two predecessor directions are
the forbidden closed doubleton.  Any positive construction must therefore
use nontrivial external paths before the compiler condition (0.3) is even
reached.

## 1. The fixed-cap interface

Fix a complete cap/trace state \(\theta\), with compiler graph

\[
                    G_\theta=(\mathcal T,\mathcal C;E_\theta)
\]

and a matching saturating every target in \(\mathcal T\).  Let
\(M_\theta\) be the transversal matroid on the occurrence-labelled cell
set \(\mathcal C\).  A cell set \(D\) can be made unused while retaining
all compiler targets if and only if

\[
                       D\in\mathcal I(M_\theta^*).            \tag{1.1}
\]

This is the dual-transversal identity of the strict-gammoid compiler
theorem.  In elementary Hall form, (1.1) is

\[
 |D\cap N_\theta(A)|
       \le |N_\theta(A)|-|A|
       \qquad(A\subseteq\mathcal T).                          \tag{1.2}
\]

Now fix three external chronology returns

\[
                       R_O,R_0,R_1.                           \tag{1.3}
\]

Assume that they close the owner endpoint pair and the two predecessor
parity endpoint pairs of the opened reset, and that their chronology
resources are mutually disjoint except at the prescribed typed endpoints.
Let \(D_i\subseteq\mathcal C\) be every old compiler cell that must be
made unused when \(R_i\) is installed.  Occurrence labels are retained:
two equal Boolean masks at different positions are different members of
\(\mathcal C\).

For the next theorem impose the **deletion-only fixed-cap interface**:
installing the three returns preserves the target set and every
nonreserved incidence of the one graph \(G_\theta\), introduces no new
mandatory target assignment, and has complete compiler effect exactly the
reservation of \(D_O\cup D_0\cup D_1\).  A physical retiming which changes
other cap incidences is outside this interface.

### Theorem 1.1 (exact compiler condition for fixed returns)

The three fixed chronology returns can be installed while retaining a full
compiler matching in cap \(\theta\) if and only if

\[
       D:=D_O\cup D_0\cup D_1\in\mathcal I(M_\theta^*).       \tag{1.4}
\]

If an additional allowed compiler deletion is \(F\), the corresponding
condition is \(D\cup F\in\mathcal I(M_\theta^*)\).  Hence adaptive
robustness to a family \(\mathcal F_B\) is exactly (0.3).  The cap graph
\(G_\theta\) is fixed, although its surviving target-saturating matching
may depend on \(F\).

#### Proof

The chronology hypothesis closes the three matching differences exported
by the reset and uses no compiler conclusion.  Once those paths are fixed,
their compiler effect is exactly the removal of the occurrence cells in
\(D\) (and, if present, \(F\)).  The dual-transversal identity gives (1.4)
and its robust version. \(\square\)

The theorem deliberately separates chronology and compiler linkages.  The
owner/predecessor alternating paths live in the functional-attachment
graphs.  The strict-gammoid paths live in the alternating digraph of a
compiler matching and terminate at unmatched compiler cells.  Calling both
objects ``returns'' does not identify their resources.

### Proposition 1.2 (strict stutters have the wrong boundary type)

A fixed-neighbour, fixed-owner private stutter has zero endpoint boundary in
both the head--owner attachment matching and the predecessor matching.
Hence any resource-disjoint union of strict stutters has zero chronology
boundary and cannot supply any nonempty subset of the opened reset's one
attachment and two predecessor return obligations.

#### Proof

The two stutter phases have the same incoming predecessor, outgoing
successor, and owner.  Their chronology-matching symmetric differences
therefore contain no external path endpoint.  Boundary is additive under a
resource-disjoint union. \(\square\)

The explicit repeated-owner sidecar of item2552L is exactly such a strict
stutter.  It can protect compiler cells belonging to a return packet, but
its owner/upper/boundary transparency prevents it from being the return.
The weak saturated-pivot rethread changes one internal owner resource, but
its local two-edge rethread has the same external endpoints.  Thus it has a
nonzero owner-resource current, not a reset-return endpoint boundary; it
could only be a segment of a future external return.  It also carries one
lower, one upper, and longer-prefix debt and supplies neither signed
predecessor return.

### Proposition 1.3 (direct same-neighbour closure is impossible)

For the opened reset of length \(N\), the three endpoint pairs are

\[
 (T_0,T_{N-1}),\qquad
 (T_0^-,T_{N-1}^+),\qquad
 (T_0^+,T_{N-1}^-).                                         \tag{1.5}
\]

After forgetting the typed signs, all three are the same adjacent root
pair.  Their only common rank-\((r+1)\) owner is

\[
                  U_{N-1}=T_0\cup T_{N-1}.                  \tag{1.6}
\]

Consequently no three resource-disjoint direct same-neighbour returns can
close (1.5).  The direct owner return closes the omitted attachment seam
and recreates the reset component.  The two direct predecessor returns are
the opposite orientations

\[
                  T_{N-1}\to T_0,\qquad T_0\to T_{N-1},     \tag{1.7}
\]

of the same owner (1.6), so selecting both repeats that owner and is exactly
the closed doubleton.

#### Proof

The endpoint identities are the two alternating parity paths and the
head--owner path in the opened-reset theorem.  Consecutive reset roots have
union \(U_{N-1}\), and a rank-\((r+1)\) owner containing both rank-\(r\)
roots must equal their union, proving uniqueness.  Equations (1.7) and the
closed-doubleton conclusion are the two orientations of that one Johnson
edge. \(\square\)

The strict-gammoid compiler reserve cannot repair this capacity-one owner
conflict: it only certifies that compiler cells can be vacated after
chronology returns have been chosen.  Thus every live architecture needs a
nontrivial external owner-return path and at least one nontrivial signed
predecessor path.  The other predecessor return may be direct only if the
joint aligned-column and resource rows permit it; both cannot be direct.
The next section shows that even admissible chronology paths need an
additional joint compiler certificate.

## 2. The smallest literal obstruction

### Theorem 2.1 (pairwise-safe three-return no-go)

There is a fixed cap and three mutually occurrence-disjoint chronology
returns such that every proper subfamily of returns is compiler-safe, but
the family of all three is not.

#### Construction and proof

Take one compiler target \(t\), three distinct occurrence cells

\[
                            c_O,c_0,c_1,
\]

and all three edges \(tc_i\).  The compiler graph has a full matching.
Its transversal matroid on the cells is \(U_{1,3}\), so its dual safe-
deletion matroid is

\[
                         M_\theta^*=U_{2,3}.                  \tag{2.1}
\]

Give the three external chronology returns disjoint private path resources
and set

\[
                 D_O=\{c_O\},\qquad D_0=\{c_0\},\qquad
                 D_1=\{c_1\}.                               \tag{2.2}
\]

Deleting zero, one, or two of the cells leaves a neighbor for \(t\), so
every proper return subfamily is safe.  Deleting all three isolates \(t\).
The first and only violated compiler cut is

\[
 A=\{t\}:\qquad
 |D\cap N(A)|=3>|N(A)|-|A|=2.                                \tag{2.3}
\]

Thus all chronology paths may coexist while the common compiler cap fails.
\(\square\)

This obstruction is smallest in the strong sense relevant here.  A
minimally ternary obstruction in a matroid is a circuit meeting all three
return hazards.  With one singleton hazard per return it therefore needs
at least three elements, and the restriction to those three elements is
exactly \(U_{2,3}\).  The example uses the minimum possible number of
compiler targets, namely one.

In the alternating-digraph representation, choose the baseline compiler
matching \(tc_O\).  The cells \(c_0,c_1\) are the two unmatched sinks.
Any two of \(c_O,c_0,c_1\) link to the two sinks by disjoint alternating
paths, but all three cannot.  This is the literal sink collision hidden by
three separately successful relocation audits.

## 3. Prospective candidate choice and the three-matroid row

Suppose each of \(O,P_0,P_1\) has a menu of direct, occurrence-labelled
return columns.  On the single-cell-hazard face let \(E\) be the disjoint
union of those menus and let \(\phi:E\to\mathcal C\) send a column to its
compiler hazard cell.  Parallelize equal images and pull
\(M_\theta^*\) back along \(\phi\); call the resulting matroid \(K\).

There are two other constraints.

* \(P\) is the task partition matroid: at most one return is chosen from
  each of the three menus.
* **If** there is a literal directed network with typed source/private sink
  banks whose gammoid independents are exactly the feasible simultaneous
  owner/predecessor return choices, call that gammoid \(L\).

Under this additional gammoid-representation hypothesis, a prospective
three-return choice is exactly a common independent set of size three in

\[
                              P,L,K.                          \tag{3.1}
\]

This is a three-matroid common-set problem, not ordinary matroid
intersection.  In the obstruction of Theorem 2.1 the menus are singletons,
\(P=L=U_{3,3}\), and \(K=U_{2,3}\).  The complete set \(X=E\) is the
first rank obstruction:

\[
                      r_K(X)=2<3.                             \tag{3.2}
\]

### Theorem 3.1 (separated typed two-matroid face)

There is a larger exact two-matroid face than completely automatic
chronology.  For each type
\(i\in\{O,P_0,P_1\}\), suppose a literal typed directed corridor has
entrance set \(E_i\), prescribed endpoint type, and a strict gammoid
\(L_i\).  Require the three corridor interiors to be pairwise physically
resource-disjoint, and require every realized triple to be aligned-column
compatible in one fixed flag table, functional owner attachment,
predecessor matching, and cap.  Put

\[
 L_{\rm ret}=\operatorname{Tr}_1(L_O)
       \oplus\operatorname{Tr}_1(L_{P_0})
       \oplus\operatorname{Tr}_1(L_{P_1}).                    \tag{3.3}
\]

A size-three independent set of \(L_{\rm ret}\) automatically chooses one
return of each type.  On the singleton-hazard face, where each entrance
\(e\) reserves one compiler cell \(c(e)\) and all other compiler incidences
are phase-identical, let \(K\) be the pullback of \(M_\theta^*\) along
\(c\).  Require equal hazard-cell images to be a physical resource conflict,
equivalently require \(c\) to be injective on every feasible return triple;
the parallel classes of \(K\) encode that rule.  Then the three returns
exist in the one fixed cap if and only if

\[
 \boxed{\quad
   \min_{X\subseteq E}
       \bigl(r_{L_{\rm ret}}(X)+r_K(E-X)\bigr)\ge3.
\quad}                                                       \tag{3.4}
\]

#### Proof

Edmonds' matroid-intersection theorem says the maximum size of a set
independent in both \(L_{\rm ret}\) and \(K\) is the left side of (3.4).
The rank of \(L_{\rm ret}\) is at most three, and any size-three
independent set has one entrance in each summand.  The three strict-gammoid
certificates realize the corresponding typed paths; corridor separation
makes their physical resources disjoint.  Aligned-column compatibility
makes their combined chronology toggle literal.  Independence in \(K\)
is exactly safe deletion of the three risk cells, so the fixed-cap compiler
survives.  Conversely any protected typed return triple records three
entrances independent in both matroids. \(\square\)

This is ordinary matroid intersection.  It is an explicit integral face on
which the task-type constraint has already been absorbed into the typed
direct-sum gammoid and the compiler footprint is matroidal.  If chronology
compatibility is completely automatic, one may instead use the task
partition matroid \(P\) in place of \(L_{\rm ret}\).  In the
\(U_{2,3}\) example either form fails at \(X=\varnothing\), where the
compiler rank is two.

The typed-corridor hypothesis cannot be replaced by an unpaired linkage
rank.  With sources \(a,b\), sinks \(A,B\), and only the disjoint arcs

\[
                         a\to B,\qquad b\to A,
\]

the source set links to the sink bank, but the prescribed pairs
\((a,A),(b,B)\) do not link.  The two reset parity returns have prescribed
signs, so a common ambient predecessor network must either retain this
pairing-resolved state or prove that both endpoint bijections are
acceptable.

There is also a smallest genuinely three-matroid warning.  On
\(\{a,b,c,d\}\), take the three rank-two partition matroids whose parallel
pairs are respectively

\[
 \{a,b\}|\{c,d\},\qquad
 \{a,c\}|\{b,d\},\qquad
 \{a,d\}|\{b,c\}.                                          \tag{3.5}
\]

Every pair of these matroids has a common base, but no two-element set is
independent in all three.  All three matroids are transversal and strict
gammoids.  Adding one common coloop turns (3.5) into a rank-three example.
Therefore pairwise owner-linkage, predecessor-linkage, and compiler tests
cannot replace (3.1).

For multi-cell return packets, the preimage of compiler independence under
``take the union of this packet's cells'' need not itself be a matroid.
Then (3.1) is only a relaxation unless the packet family has a separately
proved matroidal representation.  The fixed-choice test (1.4) remains
exact.

Likewise, source privacy by itself does not prove the asserted chronology
gammoid representation.  Typed three-commodity path packing or disjoint
pre-enumerated packet selection can fail matroid exchange.  Without the
literal network representation above, (3.1) is only a relaxation even on
the single-cell compiler face.

## 4. The exact private-sink repair

Fix one target-saturating compiler matching \(M\), and form its alternating
digraph: matched edges are directed cell-to-target, unmatched allowed edges
target-to-cell, and unmatched cells are sinks.

### Theorem 4.1 (joint relocation / private-sink criterion)

For fixed hazard sets \(D_O,D_0,D_1\), condition (1.4) holds if and only if
all cells in their union have vertex-disjoint directed alternating paths to
distinct unmatched-cell sinks.

In particular, it holds if there are pairwise vertex-disjoint alternating
subgraphs \(\Gamma_O,\Gamma_0,\Gamma_1\) such that, for each \(i\), every
cell of \(D_i\) links inside \(\Gamma_i\) to a distinct private sink.

#### Proof

The first assertion is the standard strict-gammoid representation of
\(M_\theta^*\).  The union of the three private linkages in the second
assertion is a joint linkage for all of \(D\). \(\square\)

This hypothesis is stronger than disjointness of the chronology paths and
stronger than disjointness of the hazard cells.  It separates the
**relocation corridors and their sinks**, which is exactly what the
\(U_{2,3}\) obstruction lacks.

### Corollary 4.2 (deletion-robust private blocks)

Suppose a fourth alternating subgraph \(\Gamma_B\) is vertex-disjoint from
the three return blocks.  If every \(F\in\mathcal F_B\) links inside
\(\Gamma_B\) to distinct private sinks and each \(D_i\) links inside
\(\Gamma_i\) as in Theorem 4.1, then (0.3) holds for every
\(F\in\mathcal F_B\).

Thus deletion robustness follows from literal private compiler corridors.
If, in addition, every displayed relocation path has length at most a
common constant \(L\) and all packet guards survive those paths, this gives
a deletion-robust height-\(L\) funnel.  Without the path-length hypothesis,
no constant-height conclusion follows.  Merely knowing that each return
and each \(F\) is separately safe does not suffice.

## 5. Root-slot specialization and the present pivot boundary

The Boolean root-slot theorem gives a useful sufficient implementation of
the preceding condition.  Suppose one cap has a trace-guarded root-slot
lift, \(P_0\) is its already unavailable root bank, the three return
hazards are literally contained in the injected slot fibres over root sets
\(H_O,H_0,H_1\), and every allowed deletion \(F\) is literally contained
in the injected fibres over a root set \(H(F)\).  Any off-slot hazard cells
are required to be disjoint from the fixed residual matching, exactly as in
the trace-guarded root-slot definition.  If

\[
 |P_0\cup H_O\cup H_0\cup H_1\cup H(F)|\le m+1
       \qquad(F\in\mathcal F_B),                              \tag{5.1}
\]

then (0.3) follows in one fixed cap.  A coarser sufficient count is

\[
 |P_0|+|H_O|+|H_0|+|H_1|+
       \max_{F\in\mathcal F_B}|H(F)|\le m+1.                 \tag{5.2}
\]

For a literal one-fixed-matching robust bank, plant \(B+1\)
resource-private corridors of each type over distinct certified fibres,
with every deletable resource incident with at most one copy.  The shared
typed endpoints, cap/root-slot injection, and immutable guards are outside
the deletion family.
If every corridor has hazard width at most \(a\), and \(b_{\rm del}\)
bounds the hazard-root union of **all** allowed deletion cells, the stronger
single-union condition

\[
                  |P_0|+3a(B+1)+b_{\rm del}\le m+1           \tag{5.3}
\]

puts every copy and every allowed deletion in one coindependent reserve.
One compiler matching can then avoid that entire union, while any \(B\)
resource deletions leave a surviving corridor of each type.  The adaptive
\(\forall F\,\exists M_F\) form needs only (5.1) for each actual \(F\).
Neither statement bounds chronology- or compiler-linkage length unless a
uniform path bound is separately exported.  Condition (5.3) proves only the
one-fixed-matching **compiler** row; the separated-corridor and
aligned-column chronology hypotheses of Section 3 remain independently
required.

This is an abstract reserve theorem, not a physical reset construction.
For the saturated collared pivot, the literal pivot port supplies only the
two coatom values

\[
                    s-\rho_1,\qquad s-x_R,                  \tag{5.4}
\]

at its physical cell.  It does not supply every containment neighbor of
the root \(s\), so it is not the trace-guarded root-slot injection required
by (5.1).  The explicit repeated-owner strict-stutter sidecar does provide
the desired two-flag ray and exact all-depth return, but no current theorem
plants three reset-endpoint sidecars together with the external chronology
returns and the private compiler relocation corridors of Theorem 4.1.

Consequently the strict-gammoid reserve can certify a prospectively planted
three-return system, but it does not manufacture that system from the
collared pivot.  The precise remaining positive statement is:

> plant one owner return and two predecessor-parity returns whose
> occurrence hazards satisfy the joint relocation condition (0.3), while
> keeping their chronology paths mutually resource-disjoint in the same
> physical flag table and cap.

## 6. Scope

Theorem 2.1 rules out the inference

\[
 \text{three individually (even pairwise) safe returns}
 \Longrightarrow \text{one simultaneous common-cap return triple}.
\]

It does not rule out a Boolean-specific prospective construction with
private compiler sinks, a genuine root-slot lift, or a dynamic compiler
packet that changes the cap graph rather than deleting old cells.  The
private-sink and root-slot statements are sufficient conditions; their
physical realization at the opened rolling reset remains open.  Compiler
relocation, chronology linkage, arbitrary-width upper guards, residence,
and topology remain distinct rows.

The note uses the following exact inputs:

* `MATH_THEOREM_K_BIDIRECTIONAL_ROLLING_RESET_FUNCTIONAL_ATTACHMENT_AND_DOUBLETON_GATE_20260801.md`;
* `MATH_THEOREM_L_DUAL_GAMMOID_ROOT_SLOT_RESERVE_AND_BOUNDED_DEPTH_RECURSION_20260801.md`;
* `MATH_THEOREM_L_PIVOT_FLAG_RETHREAD_STRICT_STUTTER_SIDECAR_AND_ROOT_SLOT_GATE_20260801.md`.
