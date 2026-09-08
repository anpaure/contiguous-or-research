# Coatom \(q=2\) Plücker switches: exact transport Markov basis and compiler-pressure criterion

Date: 2026-08-01  
Lane: K, additive-constant lower compiler  
Status: unconditional algebraic/flow theorem and exact conditional physical
lift. The canonical planted tensor does not satisfy the required guarded
return hypothesis, so no unconditional \(B(k)+O(1)\) theorem is claimed.

## 0. Result

At depth \(q=2\), the canonical mixed coatom tensor acts on its four exposed
lower targets by the Johnson-square switch

\[
 (X,P)+(Y,S)\longleftrightarrow (Y,P)+(X,S).                 \tag{0.1}
\]

Here

\[
\begin{aligned}
 X&=K\cup\{\infty,b,c\},&
 Y&=K\cup\{\infty,a,c\},\\
 P&=\{f_1,\ldots,f_{d-1}\},&
 S&=\{f_2,\ldots,f_d\}.
\end{aligned}                                                \tag{0.2}
\]

Thus its signed occurrence table is the rectangle, or Plücker-type,
binomial

\[
 e_{XP}+e_{YS}-e_{YP}-e_{XS}.                                \tag{0.3}
\]

The four masks form a Johnson square: changing \(X\) to \(Y\) exchanges
\(a,b\), and changing \(P\) to \(S\) exchanges \(f_1,f_d\).

There are three exact conclusions.

1. On a complete occurrence-by-profile transportation fibre, switches
   (0.3) are a nonnegative Markov basis.
2. If trace-guarded common-cap incidences have block-complete,
   source-private anchors, their minimum lower-compiler deficiency is the
   explicit quotient pressure

   \[
   b=\max_{J}\bigl(\ell(J)-u(N(J))\bigr)_+.                  \tag{0.4}
   \]

   Thus the cut inequalities \(\ell(J)\le u(N(J))+b_0\) imply
   deficiency at most \(b_0\). For two disjoint nested exposure chains the
   pressure is the sum of two one-dimensional prefix pressures. Pressure at
   most one on each chain gives the concrete bound two; one nonprivate hard
   packet task raises it by at most one.
3. Neither (0.1) nor fixed margins imply common-cap Hall. Exact trace guards
   create structural zeros. In the presently planted tensor, the local
   guarded return graph is empty, so its pressure is \(2(d-1)\), not
   \(O(1)\). A supported \(C_6\) also shows that legal square moves need not
   connect a guarded fibre even when a perfect matching exists.

The missing all-\(k\) row is precise: plant a trace-guarded exterior anchor
graph with absolute quotient pressure and a square-complete (or, more
generally, even-circuit-complete) physical lift.

## 1. The exact \(q=2\) square

For the canonical mixed-screen schedule, the old-only lower targets at
depth \(q\) are

\[
\begin{aligned}
 A_q^0&=K\cup\{\infty,b,c\}\cup
              \{f_1,\ldots,f_{d+1-q}\},\\
 B_q^0&=K\cup\{\infty,a,c\}\cup
              \{f_q,\ldots,f_d\},
\end{aligned}                                                \tag{1.1}
\]

and the new phase exchanges \(a,b\) between the two filler profiles. At
\(q=2\), (1.1) is the diagonal pair \((X,P),(Y,S)\), while the new pair is
the opposite diagonal \((Y,P),(X,S)\). This proves (0.1)--(0.3).

The adjective *Plücker* is used in the bipartite/Segre sense: (0.3) is a
\(2\times2\) minor. It is not a claim that the full three-term
Grassmann--Plücker relation is available physically.

For \(q>2\), the two filler profiles differ in \(q-1\) labels. Hence the
depth-\(q\) exchange is not itself one Johnson square. Deriving the whole
nested chain from \(q=2\) moves requires several occurrence-labelled
squares and separate proofs of all their physical guards.

## 2. Exact Markov theorem for the unguarded transport fibre

Let \(R,C\) be finite and let \(r\in\mathbb Z_{\ge0}^R\),
\(c\in\mathbb Z_{\ge0}^C\) have equal total. Put

\[
 \mathcal F(r,c)=\left\{x\in\mathbb Z_{\ge0}^{R\times C}:
 \sum_jx_{ij}=r_i,\quad \sum_ix_{ij}=c_j\right\}.             \tag{2.1}
\]

For distinct \(i,i'\in R\) and \(j,j'\in C\), a rectangle move is

\[
 Q(i,i';j,j')=e_{ij}+e_{i'j'}-e_{ij'}-e_{i'j}.               \tag{2.2}
\]

### Theorem 2.1 (nonnegative rectangle Markov basis)

Any two tables in \(\mathcal F(r,c)\) are connected by rectangle moves for
which every intermediate table is nonnegative.

#### Proof

For \(x,y\in\mathcal F(r,c)\), orient every positive unit of \(x-y\) from
\(R\) to \(C\), and every negative unit from \(C\) to \(R\). Equal margins
make the directed bipartite multigraph Eulerian. Decompose it into directed
even cycles. Subtract one unit on the positive edges and add one unit on the
negative edges of one cycle. This is sign-compatible and decreases
\(\|x-y\|_1\).

It remains to split a cycle of length \(2s\) into rectangles. Write its
positive edges as

\[
 (i_1,j_1),(i_2,j_2),\ldots,(i_s,j_s)
\]

and its negative edges as

\[
 (i_2,j_1),(i_3,j_2),\ldots,(i_1,j_s).
\]

Use successively the rectangles on rows \(i_1,i_t\) and columns
\(j_{t-1},j_t\), for \(t=2,\ldots,s\). The first move creates the
temporary edge \((i_1,j_2)\); each later move consumes the preceding
temporary edge and creates the next. Every subtraction is from an original
positive edge or the just-created temporary edge, so all tables remain
nonnegative. Iteration reaches \(y\). \(\square\)

At the lattice level,

\[
 \ker_{\mathbb Z}(\text{row and column margins})
 =A_{|R|-1}\otimes A_{|C|-1},                                \tag{2.3}
\]

generated by \((e_i-e_{i'})\otimes(e_j-e_{j'})\). Formula (0.3) is one
generator.

### Supported fibres

For structural-zero support \(G\subseteq R\times C\), the integer kernel is
generated sign-compatibly by signed simple even cycles of \(G\). Hence all
supported alternating cycles form a Markov basis. Supported rectangles
suffice whenever every even cycle admits a conformal decomposition into
supported \(4\)-cycles; chordal-bipartite support is sufficient.

This qualification is necessary. If \(G=C_6\), its two alternating perfect
matchings have equal margins, but \(G\) contains no rectangle. They are
disconnected under \(q=2\) switches, so a length-six physical atom is
genuinely necessary.

## 3. Source-private quotient pressure

Partition the soft lower targets and occurrence-labelled cells as

\[
 L=\dot\bigcup_{j\in J}L_j,\quad |L_j|=\ell_j,\qquad
 C=\dot\bigcup_{i\in I}C_i,\quad |C_i|=u_i.                  \tag{3.1}
\]

Let \(G\subseteq J\times I\). Assume:

**Source-private block condition.** The cells in (3.1) are pairwise
distinct source-fixed anchors. If \(ji\in G\), every target of \(L_j\) has
a trace-guarded common-cap incidence to every cell of \(C_i\). All claimed
edges coexist in one physical bank; phase intersection, middle replay,
residence, fixed pins, and reserved-cell guards have already been imposed.

This may be weakened to explicit injective anchor maps inside used blocks,
but marginal cardinalities alone are not a substitute.

For \(J'\subseteq J\), write

\[
 \ell(J')=\sum_{j\in J'}\ell_j,\qquad
 u(N(J'))=\sum_{i\in N_G(J')}u_i.                             \tag{3.2}
\]

### Theorem 3.1 (exact quotient deficiency)

In the supplied block-complete subgraph, the minimum number of soft targets
left unmatched is

\[
 \boxed{\delta(G;\ell,u)=
 \max_{J'\subseteq J}\bigl(\ell(J')-u(N(J'))\bigr)_+.}        \tag{3.3}
\]

Additional literal compiler edges can only reduce this number.

#### Proof

Hall's deficiency formula maximizes over arbitrary \(X\subseteq L\). If
\(X\) meets precisely the blocks \(J_X\), its neighborhood is the union of
the complete cell blocks \(N_G(J_X)\), whereas
\(|X|\le\ell(J_X)\). For fixed \(J_X\), take all targets in those blocks.
This gives (3.3). \(\square\)

Equivalently, (3.3) is an integral transportation min-cut. No
fractional-to-integral gap occurs.

### Corollary 3.2 (bounded pressure)

If, for an absolute \(b_0\),

\[
 \ell(J')\le u(N(J'))+b_0
 \quad\text{for every }J'\subseteq J,                         \tag{3.4}
\]

then all but at most \(b_0\) soft targets have distinct literal common-cap
cells. If the block bank is the entire graph, the bound is exact.

If \(h\) hard packet tasks have distinct private cells outside \(C\), they
are saturated and (3.4) is unchanged. If instead a fixed matching of those
tasks consumes \(h\) cells of \(C\), delete those cells first. Every quotient
cut loses at most \(h\) capacity, so soft deficiency is at most

\[
                              b_0+h.                           \tag{3.5}
\]

The hard-task matching hypothesis is essential. An isolated hard task is
infeasible; it cannot be paid by appending a soft lower target.

## 4. Two nested chains and an explicit constant

For one chain, index target blocks \(L_1,\ldots,L_s\) so that

\[
 N(L_1)\subseteq N(L_2)\subseteq\cdots\subseteq N(L_s).       \tag{4.1}
\]

Put

\[
 D_t=\sum_{j\le t}|L_j|,\qquad C_t=|N(L_t)|.                 \tag{4.2}
\]

### Lemma 4.1 (serial/Ferrers matching)

The exact deficiency is

\[
 b_{\rm ch}=\max_{1\le t\le s}(D_t-C_t)_+.                   \tag{4.3}
\]

It is attained constructively by processing classes from the smallest
neighborhood outward and using an unused eligible anchor.

#### Proof

For a nonempty collection of classes with largest index \(t\), its
neighborhood is \(N(L_t)\). Adding omitted earlier classes can only increase
the Hall deficit. Hence the extremal cuts are the prefixes
\(\{1,\ldots,t\}\), giving (4.3). The same prefix inequalities prove the
greedy construction by induction. \(\square\)

If the prefix and suffix exposure chains use disjoint cell banks, then

\[
                            \delta=b_-+b_+.                    \tag{4.4}
\]

Cross-bank incidences can only improve this bound. Therefore:

* pressure at most one on each chain gives soft deficiency at most \(2\);
* one hard packet task on a disjoint private anchor leaves the bound \(2\);
* if that task instead consumes one eligible chain anchor, the bound is
  at most \(3\).

These are concrete candidate values of the regenerative additive term
\(\beta\). More generally, if

\[
 b_-(\kappa)+b_+(\kappa)\le\rho\kappa+\beta_0,                \tag{4.5}
\]

then

\[
 \kappa'\le\rho\kappa+\beta_0+h.                             \tag{4.6}
\]

The \(O(1)\) conclusion requires absolute pressure bounds, not merely many
unguarded candidate cells per target.

## 5. Alternating ladders and the extra endpoint operation

The symmetric difference of an incumbent matching and the transportation
matching from Theorem 3.1 is a union of alternating cycles and paths. A
cycle changes no endpoint deficit. A path ends at a free private anchor or
at one of the unmatched soft targets counted by (3.3).

There is an important algebraic distinction. A rectangle move preserves
both margins and therefore cannot by itself change the number of matched
real targets. An augmenting path also needs one endpoint insertion/deletion,
or equivalently a declared dummy target carried by the free anchor. Thus a
closed Plücker Markov theorem never manufactures the endpoint resource
needed for Hall augmentation.

### Theorem 5.1 (physical square-plus-endpoint lift)

Suppose:

1. the source-private block condition holds;
2. every closed rectangle used in the discrepancy-cycle decomposition
   lifts to a safe coatom \(q=2\) switch preserving all noncompiler rows;
3. every open alternating path has a literal free endpoint operation (or a
   physical dummy-anchor state), and its successive vacancy slides are
   legal; and
4. all switches, slides, and anchor incidences are evaluated in one literal
   phase-common guarded bank.

Then any initial table with the prescribed margins can be rethreaded by
physical \(q=2\) switches to a compiler assignment with deficiency (3.3),
plus the hard-task surcharge (3.5).

#### Proof

Theorem 3.1 constructs an integral endpoint matching. Compare its occurrence
table with the incumbent table. Theorem 2.1 expresses every closed
discrepancy circuit as rectangles, which are physical by hypothesis 2.
For an open component, start at its declared free endpoint and slide the
vacancy along the alternating path; hypothesis 3 is exactly the physical
authorization for these non-margin-preserving endpoint steps. Hypothesis 4
makes the complete sequence co-selectable. The path endpoints left open are
exactly those counted by (3.3). \(\square\)

If the supported square graph is not Markov-complete, the theorem remains
true after adding all required longer physical alternating circuits. It is
false if only unguarded margins are checked.

## 6. Sharp failure on the current planted tensor

The symbolic maximal-erosion calculation supplies two native target columns
at every \(2\le q\le d\), and at \(q=2\) they are exactly the two diagonals
of (0.1). After a phase switch, the new targets consume those native
columns; the old targets need exterior return cells.

The trace-guard audit in
MATH_THEOREM_THREAD_D_COATOM_U5_NATIVE_COLUMNS_AND_RETURN_HALL_20260801.md
proves that every apparently eligible local return cell deletes a complete
maximal-erosion occurrence of one filler coordinate. Further caps cannot
restore it. Hence

\[
 E(\mathcal R_{\rm loc})=\varnothing,\qquad
 \delta_{\rm ret,loc}=2(d-1).                                \tag{6.1}
\]

Every deep target is a singleton quotient cut of pressure one. The doubled
\(q=1\) hinge is a closed alternating cycle, so it supplies no free endpoint.

Thus the \(q=2\) Plücker switch is a complete algebraic move on a complete
transport fibre, but the current planted maximal-erosion realization has no
local good-support edge on which that algebra can repair common-cap Hall.
An exterior bank, a nonflat rethread creating filler occurrences, or a
larger guarded circuit is necessary.

## 7. Minimal all-\(k\) construction row

A sufficient recursive export is finite and cutwise.

1. Partition exposed occurrence-labelled lower targets into the two nested
   chains and \(O(1)\) exceptional blocks.
2. Export source-fixed, pairwise distinct exterior cells whose fully guarded
   quotient graph has \(b_-+b_+=O(1)\).
3. Give every hard task a private cell, or charge its consumed anchor by the
   explicit \(+h\) in (3.5).
4. Prove the physical square atlas is Markov-complete; if it contains an
   induced \(C_{2s}\) without conformal square decomposition, include that
   \(2s\)-circuit as an atom.
5. Regenerate the same anchor/pressure state in the child.

Pressure zero gives exact compiler Hall. Pressure at most two with a private
U5 cell gives \(\beta=2\); pressure at most two with U5 consuming a chain
cell gives \(\beta=3\). Neither constant currently applies to the canonical
local tensor because of (6.1), and the serialized packet-to-cell list is
empty.

## 8. Scope audit

The following implications are not asserted.

* Palette/margin equality does not imply trace-guarded common-cap Hall.
* Algebraic kernel generation does not imply safe physical realization of
  every generator, and closed generators do not supply a free Hall endpoint.
* A guarded perfect matching does not imply square-only reachability;
  \(C_6\) is the smallest obstruction.
* Nested unguarded candidate sets do not imply a Ferrers guarded graph. In
  the current local tensor, all local return edges are removed by the
  middle-row trace guard.
* A soft deficiency bound cannot pay an isolated hard packet task.

Dependencies:

* MATH_AUDIT_MIXED_SCREEN_LOWER_DAMAGE_OPTIMALITY_20260801.md;
* MATH_THEOREM_THREAD_D_COATOM_U5_NATIVE_COLUMNS_AND_RETURN_HALL_20260801.md;
* MATH_THEOREM_THREAD_D_COATOM_TENSOR_COMPILER_PREFIX_AUGMENTED_HALL_GATE_20260801.md;
* MATH_THEOREM_COATOM_SCREEN_TENSOR_RESIDENT_ECO_PACKET_20260801.md; and
* MATH_THEOREM_INDEPENDENT_UNUSED_BASIS_FRONTIER_MATCHING_AND_MOBILITY_20260731.md.
