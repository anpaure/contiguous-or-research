# Coatom \(q=2\) switches: Johnson--Plucker Markov bases and the exact two-chain Hall gate

Date: 2026-08-01  
Lane: K, occurrence-labelled lower compiler  
Status: exact algebraic/Markov theorem and exact restricted-support criterion;
the required exterior trace-guarded return bank is still open  
Scope: lower-compiler occurrence tables and the mixed coatom packet; no
claim of `B(k)+O(1)`

## 0. Outcome

The \(q=2\) coatom change is literally a Johnson-adjacent \(2\times2\)
switch.  If \(A=S\cup\{a\}\), \(B=S\cup\{b\}\), and two occurrence
columns \(c,e\) support the four indicated assignments, the move is

\[
 E_{A,c}+E_{B,e}\longleftrightarrow E_{A,e}+E_{B,c}.       \tag{0.1}
\]

Its binomial is the (2\times2) minor

\[
                 x_{A,c}x_{B,e}-x_{A,e}x_{B,c}.             \tag{0.2}
\]

Thus it is a Segre minor whose row direction is a Johnson root; this is the
precise sense in which it is a Johnson-square/Plucker switch.  No claim is
made that (0.2) is by itself a Grassmann Plucker relation.

There are three exact conclusions.

1. On a complete occurrence table, the moves (0.1) are a Markov basis as
   soon as the positive-margin target sets induce a connected Johnson graph.
   In general, their Markov classes are classified exactly by the amount of
   each Johnson component placed in each physical column.
2. On an arbitrary allowed-incidence graph, all chordless even-cycle moves
   form the indispensable Markov basis.  All ordinary (2\times2) moves
   suffice exactly when the graph is chordal bipartite.  Johnson-restricted
   squares suffice for every margin vector exactly when, in addition, the
   two target rows of every (4)-cycle are Johnson adjacent.
3. If the exterior return incidences for the two coatom exposure chains are
   nested chainwise, their Hall deficiency is the maximum of only the
   two-prefix cuts (6.2) below.  Such a support is automatically chordal
   bipartite, so every matching transfer decomposes into ordinary squares.
   It decomposes into coatom Johnson squares only under the extra
   Johnson-row condition.

For the presently planted tensor, the exact trace-guarded local return graph
is empty.  Consequently none of the apparent local Plucker rectangles is a
legal physical move, and its local deficiency remains \(2(d-1)\).  The
Markov theorem therefore does not repair the current packet internally.  It
turns the missing theorem into a sharp exterior statement: plant a return
support satisfying the two-prefix inequalities with absolute deficit and,
if square-only routing is required, the Johnson-row condition.

## 1. Occurrence tables and Johnson minors

Fix a uniform target layer

\[
                         {\cal A}=\binom{\Omega}{s}             \tag{1.1}
\]

and a finite set \({\cal C}\) of occurrence-labelled physical cells.  For
nonnegative integer margins \(\alpha=(\alpha_A:A\in{\cal A})\) and
\(\beta=(\beta_c:c\in{\cal C})\), of the same total mass, put

\[
 {\cal F}(\alpha,\beta)=
 \left\{x\in{\mathbb Z}_{\ge0}^{{\cal A}\times{\cal C}}:
       \sum_cx_{A,c}=\alpha_A,
       \ \sum_Ax_{A,c}=\beta_c\right\}.                       \tag{1.2}
\]

Rows \(A,B\) are Johnson adjacent, written \(A\sim_JB\), when
\(|A\mathbin\triangle B|=2\).  For \(A\sim_JB\) and distinct columns
\(c,e\), define

\[
 Q(A,B;c,e)=(\mathbf e_A-\mathbf e_B)
             (\mathbf e_c-\mathbf e_e)^{\mathsf T}.            \tag{1.3}
\]

Adding or subtracting (1.3), when its two negative entries are positive,
is exactly (0.1).  It preserves both margins.  In the matching fibre
\(\alpha_A=1\), \(\beta_c\le1\), it also preserves zero--one entries.

The already-established flag/Plucker lattice theorem identifies these
minors as generators of the relevant integer kernel.  Lattice generation
does not imply connectivity through nonnegative tables.  The next theorem
is the required nonnegative strengthening.

## 2. Exact complete-table Markov theorem

Let

\[
             {\cal A}_+=\{A\in{\cal A}:\alpha_A>0\},          \tag{2.1}
\]

and let \({\cal K}\) be the components of the induced Johnson graph
\(J[{\cal A}_+]\).  For \(K\in{\cal K}\), define the component load of a
table in column \(c\) by

\[
                         \sigma_{K,c}(x)=\sum_{A\in K}x_{A,c}. \tag{2.2}
\]

### Theorem 2.1 (complete-table classes)

Two tables \(x,y\in{\cal F}(\alpha,\beta)\) are connected by legal
nonnegative Johnson-square moves if and only if

\[
                     \sigma_{K,c}(x)=\sigma_{K,c}(y)           \tag{2.3}
\]

for every \(K\in{\cal K}\) and \(c\in{\cal C}\).

In particular, if \(J[{\cal A}_+]\) is connected, the Johnson squares form
a Markov basis of the complete occurrence table.

#### Proof

A Johnson square exchanges two row labels lying in the same component, so
it preserves (2.2).  This proves necessity.

For sufficiency, split column \(c\) into \(\beta_c\) labelled slots.  Realize
each table by placing \(\alpha_A\) individually labelled tokens of type \(A\)
in the slots.  Condition (2.3) permits the slots in each column to be
partitioned into the same component classes for \(x\) and \(y\).

Fix one nonsingleton component \(K\).  Join two of its labelled tokens when
their row types are Johnson adjacent.  This token graph is a blow-up of the
connected graph \(J[K]\), and hence is connected.  Edge transpositions of a
connected graph generate the full symmetric group on its vertices.
Therefore the tokens of \(K\) can be permuted from their placement in \(x\)
to their placement in \(y\) using transpositions of Johnson-adjacent token
types.  A transposition between two different columns is (1.3); a
transposition inside one column changes no table and may be omitted.
Singleton components need no moves because (2.3) fixes their column counts.
Doing this independently for all \(K\) proves sufficiency.  Every
intermediate object is a nonnegative placement, so the proof is a genuine
Markov proof, not only a lattice calculation.  \(\square\)

For the usual compiler row \(\alpha_A=1\) for every target in one uniform
layer, the active Johnson graph is the whole connected Johnson graph.
Hence there is no hidden algebraic invariant on the complete table.

## 3. Restricted supports: the exact toric obstruction

Let \(G=({\cal A},{\cal C};E)\) be the bipartite graph of physically legal,
trace-guarded incidences, and restrict (1.2) to tables supported on \(E\).
For a simple even cycle

\[
 C=A_1c_1A_2c_2\cdots A_tc_tA_1,                              \tag{3.1}
\]

the alternating cycle move adds one alternating edge class and subtracts
the other.  Its degree is \(t\).  Degree two is exactly a rectangle.

### Theorem 3.1 (cycle Markov basis)

The alternating moves on the chordless even cycles of \(G\) connect every
nonempty margin fibre supported on \(G\).  Every chordless-cycle move is
indispensable up to sign.

#### Proof

For two tables \(x,y\) of the same margins, orient each positive copy of
\(x-y\) from the target shore to the cell shore and each negative copy in
the reverse direction.  The resulting directed multigraph is balanced at
every vertex, hence decomposes into directed alternating cycles.  Applying
one such unit cycle subtracts only entries currently positive and strictly
decreases \(\lVert x-y\rVert_1\).  Iteration reaches \(y\).

If a cycle has a chord, the chord splits it into two smaller even cycles.
Execute first the smaller move which **inserts** the chord, and then the move
which removes it.  All other subtracted edges belonged to the original
negative alternating class, so both moves remain nonnegative.  Recursing
reduces every cycle move to chordless ones.

For a chordless cycle, prescribe margin one at each of its vertices and
margin zero outside.  The induced positive-margin graph is exactly the
cycle and the fibre consists of its two alternating perfect matchings.
They can be joined only by the full cycle move.  Thus that move is
indispensable.  \(\square\)

### Corollary 3.2 (ordinary quadrics)

All legal \(2\times2\) moves form a Markov basis for every margin vector if
and only if \(G\) is chordal bipartite, namely \(G\) has no induced cycle of
length at least six.

This is an exact equivalence, not merely a sufficient expansion condition.

### Corollary 3.3 (Johnson quadrics)

Let only those rectangles whose two target rows are Johnson adjacent be
allowed.  They form a Markov basis for every margin vector supported on
\(G\) if and only if both conditions hold:

1. \(G\) is chordal bipartite;
2. in every \(4\)-cycle of \(G\), its two target vertices are Johnson
   adjacent.

#### Proof

Under the two conditions, every indispensable chordless cycle is an
allowed Johnson rectangle.  Conversely, an induced cycle of length at least
six gives the two-point fibre in the proof of Theorem 3.1 and has no
rectangle move.  A \(4\)-cycle with non-Johnson target rows gives the same
two-point fibre, but its sole connecting rectangle is forbidden.  \(\square\)

Thus ordinary chordality is not enough for a *coatom-only* Markov basis.
The row-label condition is load-bearing.

## 4. Literal identification of the coatom square

Use the notation of the mixed coatom packet.  Put

\[
 I=\{\infty,c\},\qquad V_0=I\cup\{b\},\qquad
 V_1=I\cup\{a\}.                                             \tag{4.1}
\]

At depth \(q=2\), with \(h=d-1\), the prefix native column changes between

\[
 \begin{aligned}
 A^-_0&=K\cup I\cup\{b\}\cup\{f_1,\ldots,f_{d-1}\},\\
 A^-_1&=K\cup I\cup\{a\}\cup\{f_1,\ldots,f_{d-1}\},
 \end{aligned}                                                \tag{4.2}
\]

and the suffix native column changes between

\[
 \begin{aligned}
 A^+_0&=K\cup I\cup\{a\}\cup\{f_2,\ldots,f_d\},\\
 A^+_1&=K\cup I\cup\{b\}\cup\{f_2,\ldots,f_d\}.
 \end{aligned}                                                \tag{4.3}
\]

Each pair in (4.2)--(4.3) differs by exchanging \(a,b\), and hence is a
Johnson edge.  If \(c\) is its native physical column and \(e\) an exterior
column carrying the opposite target before the switch and the old target
after the switch, the two phase assignments are exactly the two diagonals
of (0.1).

The same row adjacency holds separately for every \(q\ge2\).  What does
*not* follow is a single cross-depth Johnson table: the targets at different
depths have different ranks.  The Johnson Markov theorem is therefore
rankwise, and a uniform all-depth conclusion requires a compatible exterior
column bank at every depth.

## 5. The exact local obstruction

The maximal-erosion audit in
`MATH_THEOREM_THREAD_D_COATOM_U5_NATIVE_COLUMNS_AND_RETURN_HALL_20260801.md`
proves more than a shortage of columns.  Every local envelope candidate for
the opposite target deletes a complete maximal-erosion occurrence of one
filler coordinate.  Consequently every such cross incidence fails the
middle-row trace guard, monotonically under further caps.

In the toric language, the two diagonal native assignments in
(4.2)--(4.3) exist across the two phases, but the cross variables required
by (0.2) are absent from the literal trace-guarded support.  Hence there is
no legal local Johnson minor.  At \(q=2\) the two native rungs contribute
deficiency two.  Across \(2\le q\le d\), the exact local return graph is
empty and contributes

\[
                         \delta_{\rm loc}=2(d-1).              \tag{5.1}
\]

This is a support-face obstruction, not a failure of the complete-table
Markov basis.  Exterior cells or a nonflat rethread must supply the missing
cross variables.

## 6. Two nested exterior chains

The strongest useful deterministic support condition suggested by the
symbolic erosion formula is the following.  Partition the old obligations
into two ordered chains

\[
                  P_1,\ldots,P_p,qquad S_1,\ldots,S_s,        \tag{6.1}
\]

and suppose their literal trace-guarded exterior neighborhoods satisfy

\[
 N(P_1)\subseteq\cdots\subseteq N(P_p),\qquad
 N(S_1)\subseteq\cdots\subseteq N(S_s).
\]

Put \(N(P_0)=N(S_0)=\varnothing\).

### Theorem 6.1 (exact two-prefix deficiency)

The matching deficiency of this return graph is

\[
 \boxed{
 \delta=
 \max_{0\le i\le p,\ 0\le j\le s}
 \left(i+j-|N(P_i)\cup N(S_j)|\right).}                       \tag{6.2}
\]

In particular, its deficiency is at most the absolute constant \(b\) if
and only if

\[
                 |N(P_i)\cup N(S_j)|\ge i+j-b                \tag{6.3}
\]

for every pair \((i,j)\).  These are the complete cutwise inequalities; no
other subset needs to be checked.

#### Proof

For any subset \(X\), let it contain \(i\) prefix-chain rows and \(j\)
suffix-chain rows.  The largest selected prefix index is at least \(i\), and
the largest selected suffix index is at least \(j\).  Nestedness therefore
gives

\[
                  |N(X)|\ge|N(P_i)\cup N(S_j)|.
\]

The subset consisting of the first \(i\) rows of the first chain and the
first \(j\) rows of the second attains equality.  Taking the maximum Hall
shortfall proves (6.2).  \(\square\)

### Proposition 6.2 (quadratic routing on two chains)

Every bipartite graph whose target shore is the union of two nested-
neighborhood chains is chordal bipartite.  Hence every two matchings with
the same margins in this support are connected by ordinary \(2\times2\)
switches.

#### Proof

An induced cycle of length at least six contains at least three target
vertices, so two lie in the same chain.  Let their neighborhoods be
nested.  The larger one is adjacent to both cycle neighbors of the smaller
one.  In a cycle longer than four, at least one of those edges is a chord.
This contradiction proves chordal bipartiteness, and Corollary 3.2 applies.
\(\square\)

The word **ordinary** in Proposition 6.2 is essential.  If a rectangle has
target rows of different ranks, or nonadjacent rows in the same rank, it is
not a coatom Johnson square.  Corollary 3.3 gives the exact additional test.
Failure of that test identifies a genuine need for a higher or nonlocal
circuit, such as a planted \(C_6\), rather than a failure of Hall itself.

## 7. Bounded compiler deficiency

The preceding statements give a direct, nonasymptotic bridge to the lower
compiler.

### Corollary 7.1 (square-routable core)

Suppose a phase-zero compiler matching is fixed.  Delete a set \(B\) of
target obligations.  Assume that on the remaining rows there is one
co-selectable transition support \(G_{\rm tr}\) such that:

1. the retained phase-zero table and a phase-one literal trace-guarded
   matching both lie in the same margin fibre supported on \(G_{\rm tr}\);
2. \(G_{\rm tr}\) satisfies the two conditions of Corollary 3.3.

Then Johnson-square moves transform the retained phase-zero occurrence
table to a phase-one matching at the occurrence-table level.  Re-inserting
no rows from \(B\) already
proves

\[
                  \operatorname{def}_{\rm Hall}(\text{phase one})
                  \le |B|.                                   \tag{7.1}
\]

For the two-chain face, assumptions 1 and the bound in (7.1) reduce exactly
to (6.3); ordinary square routing is automatic, and only the Johnson-row
test remains.

#### Proof

Theorem 2.1 handles a complete support; Corollary 3.3 handles the stated
restricted support.  Every move preserves row and physical-column margins,
so the final retained table is a matching.  It saturates every target
outside \(B\), giving (7.1) directly.  \(\square\)

This is the promised bounded-defect implication.  It is deliberately not a
claim that Markov connectivity creates a matching: assumption 1, or the
cutwise inequalities (6.3), is indispensable.  Chordal bipartite graphs can
still be Hall deficient.  Moreover, an occurrence-table Markov path is a
literal chronology path only when every rectangle in the path is supplied
by a physical safe coatom actuator with all noncompiler guards.  The toric
theorem alone does not provide those actuators.

## 8. Exact remaining theorem

For the zero-defect coatom tensor, a concrete constant-\(\beta\) recurrence
would follow from either of these equivalent-strength exterior inputs.

* **Cut form:** construct trace-guarded exterior neighborhoods for the two
  erosion chains satisfying (6.3) with an absolute \(b\), together with the
  Johnson-row condition on every rectangle used; or
* **circuit form:** construct a phase-one matching after deleting at most
  \(b\) rows, and decompose its symmetric difference from the phase-zero
  matching into legal Johnson squares plus a bounded number of explicitly
  guarded higher circuits.

Then the compiler contribution to the regenerative additive row is at most
\(b\) (plus whatever separately exported packet-task cell is required).
The current planted maximal-erosion support has \(b=2(d-1)\), not \(O(1)\),
because it has no return edge at all.  Thus the exact Markov theorem closes
the algebra of q2 switches but does not by itself close regeneration.

## 9. Scope audit

1. The complete-table theorem is exact for occurrence-labelled columns and
   arbitrary nonnegative integer margins.
2. The chordal-bipartite equivalence concerns all ordinary rectangles.
   Coatom-only rectangles require Corollary 3.3.
3. Different erosion depths live in different uniform target ranks; no
   cross-depth Johnson connectivity is asserted.
4. Envelope containment is not a legal edge.  Every edge in Sections 5--8
   must pass the middle-row trace, residence, fixed-pin, and common-cap
   guards.
5. Markov connectivity is conditional on a nonempty target fibre.  It does
   not replace Hall or the packet-task deletion-cell row.
6. Therefore this note proves an exact algebraic and cutwise reduction, not
   `nu(k)<=B(k)+O(1)`.
