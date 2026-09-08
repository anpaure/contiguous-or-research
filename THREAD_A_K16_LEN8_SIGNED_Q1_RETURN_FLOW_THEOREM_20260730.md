# The k=16 length-eight source: exact signed-q1 return flow and arbitrary-union endpoint model

## 1. Scope and authenticated base state

This note works from the audited factor

\[
F_8={\tt scratch/k16\_asymmetric\_len8\_orbit\_repair\_20260730.json},
\]

whose SHA256 is

\[
\texttt{6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204}.
\]

The independent replay audit is

\[
\texttt{scratch/k16\_asymmetric\_len8\_orbit\_repair\_20260730.audit.json},
\]

with SHA256

\[
\texttt{3e9c62c66d85ff6a8c242897a80dc2841eaf4fca9e908f50b8f1f5b697576e87}.
\]

The audited endpoint has 12,870 middle owners, 29 components, positive residence at least four, complete lower and upper q1 palettes, 45 lower-q2 holes, and 48 arbitrary-upper rank-11 holes. Thus its canonical deep objective is 93. The fixed-width q4 audit has 15 holes, but the arbitrary rank-12 union audit has none; consequently those 15 fixed-width holes are not part of the canonical 93-objective.

The remaining nonzero canonical target orbits are

\[
\begin{array}{c|c}
\text{shore} & \text{orbit representatives}\\ \hline
\text{lower q2} & 33337,33609,34069,\\
\text{arbitrary upper rank 11} & 36343,36599,39791,46811.
\end{array}
\]

The last upper orbit has size three; the other six displayed orbits have size fifteen. The previously missing upper orbits represented by 39911 and 40623 have been repaired and hence must be treated as protected survivor rows, not as unsatisfied demand rows.

The purpose of this note is to give an exact finite endpoint model in which:

1. a service move may temporarily lose q1 or deep witnesses;
2. non-gainful moves may serve as return moves;
3. the completed rethread is q1-safe or q1-deck-neutral;
4. lower fixed-depth and arbitrary-upper witnesses are checked in the final chronology, rather than by adding per-move gain scores.

No claim of existence of a 92-defect endpoint is made here.

## 2. The tail-head assignment graph

Let

\[
V=\binom{[16]}8,
\qquad n=|V|=12870.
\]

Orient every component of the base factor \(F_8\). Index its directed transitions by the tails: for each \(i\in I\), write

\[
e_i=(v_i,w_i),
\]

where \(v_i\) is the tail and \(w_i\) is its base successor. Both \(i\mapsto v_i\) and \(i\mapsto w_i\) are bijections from \(I\) to \(V\).

Define the permitted tail-head graph

\[
\mathcal G=\{(i,j): |v_i\triangle w_j|=2\}.
\]

A binary array \(x=(x_{ij})_{(i,j)\in\mathcal G}\) is a head assignment if

\[
\sum_{j:(i,j)\in\mathcal G}x_{ij}=1\quad(i\in I),
\tag{2.1}
\]

and

\[
\sum_{i:(i,j)\in\mathcal G}x_{ij}=1\quad(j\in I).
\tag{2.2}
\]

It selects the successor \(v_i\mapsto w_j\) whenever \(x_{ij}=1\). Let \(x^0\) be the identity assignment \(x^0_{ii}=1\), and put \(z=x-x^0\).

For an ordered Johnson edge \((X,Y)\), let

\[
y_{XY}=\sum_{i:v_i=X}\sum_{j:w_j=Y}x_{ij}.
\]

Since both indexing maps are bijections, this sum has at most one term.

To exclude a doubled undirected edge, impose

\[
y_{XY}+y_{YX}\le 1
\qquad(\{X,Y\}\in E(J(16,8))).
\tag{2.3}
\]

### Lemma 2.1 (exact assignment decoder)

The binary solutions of (2.1)--(2.3) are in bijection with oriented simple spanning 2-factors of \(J(16,8)\).

#### Proof

Equation (2.1) gives every vertex one successor, and (2.2) gives every vertex one predecessor. Hence the selected directed graph is a disjoint union of directed cycles spanning \(V\). Membership in \(\mathcal G\) makes every selected transition a Johnson edge. Johnson adjacency excludes loops, and (2.3) excludes a directed 2-cycle represented twice by the same undirected edge. Forgetting orientations gives a simple spanning 2-factor.

Conversely, orient every component of a simple spanning 2-factor. For the unique successor \(Y\) of \(v_i\), there is a unique \(j\) with \(w_j=Y\); set \(x_{ij}=1\). The predecessor and successor conditions give (2.1)--(2.2), while simplicity gives (2.3). ∎

### Lemma 2.2 (alternating-cycle decomposition)

For every binary head assignment \(x\), the support of \(x\triangle x^0\) is a disjoint union of even alternating cycles in the bipartite graph with left vertices \(I_{\rm tail}\), right vertices \(I_{\rm head}\), identity edges \((i,i)\), and permitted edges \((i,j)\in\mathcal G\).

Equivalently, every endpoint rethread is a sum of head-permutation port cycles. No individual summand is required to preserve q1 or any deeper shadow.

#### Proof

Both \(x\) and \(x^0\) are perfect matchings of the tail-head bipartite graph. Every vertex in their symmetric difference has degree zero or two, with the two edge types alternating. ∎

This elementary decomposition is the algebraic reason that temporary damage is legitimate: only the sum of all chosen alternating cycles is the physical endpoint.

## 3. Exact positive-residence constraints

For a directed Johnson edge \(X\to Y\), define

\[
\iota(X,Y)=Y\setminus X,
\qquad
\delta(X,Y)=X\setminus Y.
\]

For every directed Johnson walk

\[
X_0\to X_1\to\cdots\to X_{r+1},
\qquad 1\le r\le 3,
\]

such that

\[
\iota(X_0,X_1)=\delta(X_r,X_{r+1}),
\tag{3.1}
\]

impose the no-good inequality

\[
\sum_{a=0}^{r} y_{X_aX_{a+1}}\le r.
\tag{3.2}
\]

### Lemma 3.1 (exact cyclic residence-four form)

For a binary head assignment, (3.2) for all walks satisfying (3.1) is equivalent to positive residence at least four, including across component rootings.

#### Proof

If all \(r+1\) transitions in such a walk are selected, the coordinate inserted on the first transition is deleted on the last after exactly \(r\le3\) intervening positive states, producing a forbidden residence. Thus positive residence at least four implies every inequality.

Conversely, a residence violation chooses the transition on which a coordinate enters and the first transition, at cyclic distance at most four, on which it leaves. The intervening selected transitions form a walk satisfying (3.1), and every term in (3.2) equals one, contradicting (3.2). The argument is cyclic and therefore does not depend on an artificial linear rooting. ∎

This formulation is deliberately endpoint-based. Intermediate alternating-cycle summands may violate residence; the final selected transition system may not.

## 4. Signed q1 inventory and return equations

For an ordered Johnson edge \(a=(X,Y)\), let

\[
L(a)=X\cap Y,
\qquad U(a)=X\cup Y
\]

be its lower and upper q1 colours. Let \(\mathcal C_1^-\) and \(\mathcal C_1^+\) be the complete lower and upper q1 colour sets.

For an off-diagonal assignment arc \(a=(i,j)\), define its signed q1 column relative to the removed base edge \(e_i=(v_i,w_i)\) by

\[
Q_{C,a}=
\begin{cases}
\mathbf1\{L(v_i,w_j)=C\}-\mathbf1\{L(v_i,w_i)=C\},&C\in\mathcal C_1^-,\\
\mathbf1\{U(v_i,w_j)=C\}-\mathbf1\{U(v_i,w_i)=C\},&C\in\mathcal C_1^+.
\end{cases}
\tag{4.1}
\]

The same definition, with a zero column, may be used for identity arcs. Let

\[
s_C=m_C(F_8)-1
\tag{4.2}
\]

be the base multiplicity above the mandatory one copy of colour \(C\).

### Lemma 4.1 (exact signed-q1 endpoint criterion)

The endpoint encoded by \(x\) has both q1 palettes complete if and only if

\[
Qz\ge -s
\tag{4.3}
\]

coordinatewise. It has exactly the same q1 multiplicity vectors as \(F_8\) if and only if

\[
Qz=0.
\tag{4.4}
\]

#### Proof

For each colour \(C\), (4.1) telescopes over the changed tails and gives

\[
m_C(F_x)=m_C(F_8)+(Qz)_C=1+s_C+(Qz)_C.
\]

Completeness is precisely nonnegativity after subtracting the mandatory one copy, yielding (4.3); equality of decks is precisely (4.4). ∎

The full length-eight orbit creates a mixed-shore source. Its audited directed edge counts are

\[
A\to A:6420,\quad A\to B:15,\quad B\to A:15,\quad B\to B:6420.
\]

In particular, a B-only unique-token permutation normal form is not the correct global model at this source. The signed two-shore matrix \(Q\) is.

### Proposition 4.2 (service skeleton plus signed return)

Let \(P\) be the tail-head incidence matrix whose column for an off-diagonal assignment arc \((i,j)\) is

\[
P_{ij}=\mathbf e_j-\mathbf e_i.
\tag{4.5}
\]

Let \(p\) and \(r\) be disjoint binary selections of off-diagonal assignment arcs, with the combined selection using every tail and every head at most once. Let \(p\) be fixed as the partial service selection. A compatible return selection \(r\) closes it to a head assignment, after inserting the unused identity arcs, if and only if

\[
P r=-Pp,
\tag{4.6}
\]

together with the unused row/column capacities and the binary conflict constraints. The closed endpoint is q1-safe if and only if

\[
Qr\ge -s-Qp,
\tag{4.7}
\]

and is q1-deck-neutral if and only if

\[
Qr=-Qp.
\tag{4.8}
\]

#### Proof

The vector \(P(p+r)\) records head demand minus tail supply. It vanishes exactly when the selected nonidentity arcs can be completed by the complementary identity arcs to a permutation of heads; the capacity bounds prevent a tail or head from being used twice. Equations (4.7)--(4.8) are Lemma 4.1 applied to the sum of service and return columns. ∎

There is also a useful colour-graph interpretation of (4.8). Project every changed edge simultaneously to the arrow from its old lower colour to its new lower colour and to the arrow from its old upper colour to its new upper colour. Equation (4.8) says that both projected directed multigraphs are Eulerian. Thus a q1 debt created by a service path must either be closed by a return path or, under (4.7), terminate at an audited surplus token.

For \(F_8\), the q1 surplus is not hypothetical. On the lower no-z shore and the upper with-z shore there are respectively fifteen colours of multiplicity two; all remaining colours on those two shores have multiplicity one. These are finite endpoint reservoirs, not permission to ignore signed restoration.

## 5. Exact lower and arbitrary-upper chronology witnesses

Per-move gain vectors cannot enforce the deep target. The endpoint chronology must be materialized.

### 5.1 Lower fixed-depth witnesses

Fix a lower target \(R\) of the required rank. Let \(\Pi_R^-\) be the set of all directed middle-level walks

\[
\pi=(X_0,X_1,\ldots,X_q)
\]

of the required depth such that

\[
\bigcap_{a=0}^{q}X_a=R.
\tag{5.1}
\]

Require the \(q+1\) owners \(X_0,\ldots,X_q\) to be pairwise distinct. This matches the literal audit convention that a component shorter than \(q+1\) supplies no fixed-q window.

Introduce nonnegative path variables \(f^-_{R,\pi}\) and a binary coverage variable \(c_R^-\). Impose

\[
0\le f^-_{R,\pi}\le y_{X_aX_{a+1}}
\quad(0\le a<q),
\tag{5.2}
\]

and

\[
\sum_{\pi\in\Pi_R^-}f^-_{R,\pi}\ge c_R^-.
\tag{5.3}
\]

Because \(y\) is binary, \(c_R^-=1\) is feasible exactly when the endpoint contains an actual contiguous witness for \(R\).

### 5.2 Arbitrary-upper accumulated-union automata

Fix a strict upper target \(T\) of rank between nine and sixteen. Define a product digraph \(\mathcal A_T\) with states

\[
(X,S),\qquad X\in V,\quad X\subseteq S\subseteq T.
\]

It has an active transition

\[
(X,S)\longrightarrow(Y,S\cup Y)
\tag{5.4}
\]

only when \(y_{XY}=1\) and \(Y\subseteq T\). Add a supersource \(\sigma_T\) with an arc to every \((X,X)\), and add an arc from every accepting state \((X,T)\) to a supersink \(\tau_T\). Let \(c_T^+\) be binary. Impose ordinary flow conservation at every product state, net outflow \(c_T^+\) at \(\sigma_T\), net inflow \(c_T^+\) at \(\tau_T\), nonnegativity, and an upper bound \(y_{XY}\) on every copy of (5.4). Source and sink arcs have capacity one.

### Lemma 5.1 (exact arbitrary-upper automaton)

The constraint \(c_T^+=1\) is feasible if and only if some cyclic contiguous interval of the endpoint factor has union exactly \(T\).

#### Proof

An endpoint interval \(X_0,X_1,\ldots,X_q\) contained in \(T\) lifts to the product path

\[
(X_0,X_0),(X_1,X_0\cup X_1),\ldots,
(X_q,X_0\cup\cdots\cup X_q).
\]

It reaches an accepting state exactly when the union is \(T\).

Conversely, decompose any positive source-to-accepting flow into directed paths and cycles. One positive source-to-accepting path remains. Projecting it onto its first coordinate gives selected consecutive successor edges, and its second coordinate is, by (5.4), exactly the accumulated union. At acceptance that union is \(T\). If the projected path repeats an owner, determinism of the selected successor means that it has traversed a whole factor component. By the last distinct owner it has already accumulated the union of that component; further laps add nothing. Therefore, whenever the later state accepts, the state at the last distinct owner is already accepting. Hence every accepting path has an accepting prefix with no repeated owner, exactly as in the literal finite-interval audit. ∎

The automaton, rather than a fixed q3 test, is the required safety object. In particular it detects the rank-10 and lower-q3 casualties exhibited by the audited length-nine packets.

## 6. Exact signed alternating-return repair theorem

For the canonical k=16 audit, define the target universe explicitly by

\[
\mathcal T^-=\bigsqcup_{q=2}^{8}\binom{[16]}{8-q},
\qquad
\mathcal T^+=\bigsqcup_{r=10}^{16}\binom{[16]}r.
\tag{6.1}
\]

A lower target in the q-th summand is tested on exactly \(q+1\) consecutive owners by (5.1). Every upper target is tested over intervals of arbitrary cyclic width by Section 5.2. Together with the separately imposed rank-7/rank-9 q1 palettes, this is exactly the complete fixed-lower/arbitrary-upper objective used by the authenticated audit. Put

\[
\mathcal T=\mathcal T^-\sqcup\mathcal T^+,
\qquad
B_8=\sum_{T\in\mathcal T}c_T(F_8)=|\mathcal T|-93.
\tag{6.2}
\]

### Theorem 6.1 (SAAR-93: exact endpoint equivalence)

The following are equivalent.

1. There exists a simple spanning 2-factor \(F\) of \(J(16,8)\) obtained by reassigning the heads of \(F_8\), with positive residence at least four, complete lower and upper q1 palettes, and strictly smaller canonical deep defect than 93.

2. There are binary assignment variables \(x\), binary coverage variables \(c_T\), and lower-path and upper-automaton flow variables satisfying:

   (a) the assignment and simplicity constraints (2.1)--(2.3);

   (b) every residence inequality (3.2);

   (c) the signed q1 inequalities (4.3);

   (d) the lower witness constraints (5.2)--(5.3);

   (e) the upper accumulated-union automaton constraints of Section 5.2;

   (f) the strict endpoint objective

   \[
   \sum_{T\in\mathcal T}c_T\ge B_8+1.
   \tag{6.3}
   \]

The same equivalence holds with either of the following stronger endpoints:

* q1-deck neutrality, on replacing (4.3) by (4.4);
* monotone deep repair, on requiring \(c_T=1\) for every target covered by \(F_8\) and

  \[
  \sum_{T:c_T(F_8)=0}c_T\ge1;
  \tag{6.4}
  \]

* full repair, on requiring \(c_T=1\) for every \(T\in\mathcal T\).

#### Proof

Assume first that the variables exist. By Lemma 2.1, \(x\) decodes to a simple spanning 2-factor \(F\). Lemma 3.1 gives positive residence at least four. Lemma 4.1 gives both complete q1 palettes. Equations (5.2)--(5.3) and Lemma 5.1 show that every target with \(c_T=1\) has a literal contiguous witness in \(F\). Hence (6.3) says that \(F\) covers at least one more canonical target than \(F_8\), so its defect is at most 92. The three strengthened conclusions follow from their corresponding extra constraints.

Conversely, orient the components of a factor \(F\) satisfying item 1. Lemma 2.1 constructs its binary head assignment. Positive residence gives (3.2) by Lemma 3.1, and q1 completeness gives (4.3) by Lemma 4.1. For each covered lower target, choose one literal witness path and put unit flow on it. For each covered upper target, lift one literal union interval to the product automaton as in Lemma 5.1. Set all other coverage variables to zero. Since the defect is smaller than 93, (6.3) holds. The same construction proves the converse assertions for the strengthened variants. ∎

### Corollary 6.2 (constructive service-return form)

Fix any partial service skeleton \(p\), including a skeleton that directly creates a witness for one of the seven remaining target orbits. It extends to a valid strict descent endpoint if and only if there is a return selection \(r\) such that:

\[
Pr=-Pp,
\qquad
Qr\ge-s-Qp,
\tag{6.5}
\]

the combined selection obeys assignment capacities, simplicity, and residence, and its decoded endpoint satisfies the witness systems and (6.3). For exact q1 deck neutrality the second condition in (6.5) is replaced by \(Qr=-Qp\).

Thus the repair problem is an alternating-return circulation with a nonlinear-looking chronology condition that has nevertheless been linearized by path and automaton flows. It is not a packing of individually safe positive cycles.

## 7. Orbit quotient and the exact seven-row demand

The base factor and its defect families are invariant under the free \(\mathbb Z_{15}\)-rotation on coordinates \(0,\ldots,14\), fixing coordinate 15. An orbit-symmetric endpoint is obtained by adding

\[
x_{\rho i,\rho j}=x_{ij}
\tag{7.1}
\]

for every rotation \(\rho\), together with orbit-equivariant copies of the witness flows. Under (7.1), the assignment, residence, q1, witness, and endpoint-objective constraints descend without approximation to a finite quotient mixed-integer flow model. Assignment and coverage variables remain binary; an orbit with nontrivial stabilizer may require an averaged, hence fractional, equivariant witness flow. The seven unsatisfied orbit rows are exactly those listed in Section 1; the repaired 39911 and 40623 rows occur only as survivor constraints in the monotone model.

This quotient statement is exact but is not a claim that an optimal endpoint must be rotation-invariant. Dropping (7.1) gives the unrestricted physical model of Theorem 6.1.

The old nine-orbit provider table from the pre-length-eight source cannot be transplanted as an exact column catalogue. On the authenticated length-eight source, the separated three-collar catalogue contains 211,604 nonold seams and 5,425 provider seams. The unrestricted graph \(\mathcal G\) of Section 2 is larger: it contains all \(12870\cdot63=810810\) nonidentity Johnson tail-head arcs. Every service and return column, whether unrestricted or collar-prefiltered, must be regenerated relative to this source because both q1 signs and accumulated-union histories are state-relative.

## 8. Consequences of the authenticated short-cycle census

The source-relative audit gives the following exact boundary for restricted port-cycle repairs.

1. There is no q1-safe positive port cycle of length three through seven.

2. At length eight there are 45 q1-safe cycles, but every one fails the simultaneous lower-q2/upper-q3 safety test.

3. At length nine there are 30 candidates, forming two \(\mathbb Z_{15}\)-orbits, that are q1/lower-q2/upper-q3-safe and gain one rank-11 target.

4. Each such length-nine representative nevertheless creates two rank-10 holes and one lower-q3 hole. Its full canonical objective therefore worsens by two. A maximum compatible packing of seven of the new-source length-nine packets leaves lower-q2 defect 45, upper-q2 defect 14, lower-q3 defect 7, and upper-q3 defect 41.

### Proposition 8.1 (first possible monotone restricted repair form)

Within the audited single-cycle catalogue through length nine, no column by itself satisfies the monotone-deep system of Theorem 6.1. Consequently any monotone repair supported on audited cycles of length at most nine must use at least two alternating cycles with compensating signed deep histories. Otherwise a monotone single-cycle repair requires a new alternating cycle of length at least ten. Moreover, every one of the thirty audited q1/lower-q2/upper-q3-safe length-nine candidates fails even the weaker strict net-descent objective.

#### Proof

Lengths three through seven fail before the full endpoint test. Every length-eight candidate fails a protected deep row and hence cannot be monotone. Of the sixty q1-safe length-nine candidates, thirty fail a selected protected row and hence cannot be monotone; the other thirty have negative net full-objective gain by item 4. Hence no single audited cycle satisfies the monotone system, and none of the thirty fixed-deep-safe length-nine candidates satisfies strict net descent. Lemma 2.2 leaves only a compound sum of cycles for a monotone repair, unless a longer alternating component is used. The stated censuses do not rule out a nonmonotone net-positive length-eight candidate or one of the thirty fixed-deep-unsafe length-nine candidates, and no such stronger inference is used here. ∎

This proposition is intentionally scoped. It does not say that a compound repair of total small support is impossible. Indeed, Theorem 6.1 is designed precisely to permit one constituent to lose a survivor while another restores it, or one non-gainful constituent to close q1 and residence debt.

## 9. Relation to the separated port-permutation master

The assignment equations in

\[
\texttt{MATH\_THEOREM\_K16\_SEPARATED\_PORT\_PERMUTATION\_MASTER\_20260730.md}
\]

and (2.1)--(2.2) above have the same tail-head assignment form. Their column sets are not equal. The separated master restricts at the outset to its 211,604 source-relative collar-valid nonold seams, whereas the unrestricted graph \(\mathcal G\) contains all 810,810 nonidentity Johnson tail-head arcs. Thus the separated assignment polytope is a column-restricted face of the unrestricted one, before its additional cut-separation rows are imposed.

The separated master adds the sufficient restrictions that the nonfixed source indices are pairwise at cyclic distance greater than three and that each new seam passes its source-relative three-collar test. Under those restrictions, every q1, q2, or q3 window crosses at most one seam. Its occurrence-level formula

\[
\mu'_t(S)=\mu_t(S)-D_C(t,S)+
\sum_{(i,j)}x_{ij}A_{ij}(t,S)
\tag{9.1}
\]

is therefore exact. The unrestricted model in this note does not assume separation: it replaces local collar sufficiency by all exact residence no-goods (3.2), and replaces fail-closed deep CEGAR by the endpoint path and accumulated-union flows of Section 5.

### Theorem 9.1 (exact comparison of the two masters)

Let \(x\) be a binary assignment on the length-eight source.

1. If its cut set is three-separated and all its nonold seams are three-collar-safe, then the residence constraints (3.2) hold. For q1 through q3, the fixed-width lower and upper coverage constraints are equivalent to the occurrence-load inequalities obtained from (9.1). On the upper shore, these are the fixed-length restrictions of the accumulated-union automata, not the full arbitrary-width condition.

2. If, in addition, \(x\) satisfies the simplicity rows (2.3) and literal replay accepts every fixed lower depth and every arbitrary-width upper union, then \(x\) satisfies the corresponding SAAR-93 endpoint constraints. In particular, a separated-master assignment with strict canonical gain and a complete replay PASS has defect at most 92.

3. Conversely, a SAAR-93 solution whose cuts are three-separated and whose seams pass the three-collar catalogue is feasible for the separated master's q-at-most-three core only if it also covers every fixed upper q2/q3 row imposed there. Under that additional hypothesis, its exact Section 5 witnesses make every subsequent complete-objective CEGAR query accept.

Thus a separated-master assignment that survives complete literal replay is a three-separated, locally certifiable submodel of Theorem 6.1. The converse need not hold: arbitrary upper coverage at rank \(8+q\) may use an interval longer than \(q+1\) and therefore need not satisfy the master's fixed-q upper row. Separation is sufficient but not necessary for the exact residence and chronology constraints.

#### Proof

The separated residence assertion is Theorem 3.1 of the separated master. Its unique-crossing-window theorem proves (9.1) occurrence by occurrence. A fixed-depth target is covered exactly when its resulting occurrence load is positive, which is exactly the feasibility condition for the corresponding fixed-length path witness variables. This proves item 1. Lemma 5.1 identifies literal arbitrary-union replay with the upper automata, proving item 2. For item 3, the extra fixed-upper hypothesis supplies precisely the rows not implied by arbitrary-width coverage; all remaining implications then read in reverse. ∎

### 9.1 A constructive quota-first Hall guarantee

Fix a three-separated cut set \(C\). Then every port permutation fixes \(I\setminus C\) and permutes \(C\). Let \(H_C\) be a bipartite graph from a tail copy of \(C\) to a head copy of \(C\), containing only nonidentity, Johnson-legal, collar-safe seams. To avoid hiding the physical two-cycle condition inside Hall, suppose first that the chosen support \(H_C^\circ\subseteq H_C\) is conflict-free in both senses: no arc in \(H_C^\circ\) is the reverse of an unchanged source edge indexed by \(I\setminus C\), and no two arcs in \(H_C^\circ\) realize opposite orientations of the same undirected Johnson edge.

For every required q-at-most-three occurrence row \(t\), define the demand after the fixed destructions

\[
b_t=\max\{0,1-\mu_t(F_8)+D_C(t)\},
\tag{9.2}
\]

and let \(g_t(i,j)=A_{ij}(t)\) be the nonnegative number of new occurrences contributed by seam \((i,j)\).

### Proposition 9.2 (witness-bank plus residual Hall)

Suppose there is a partial matching \(K\subseteq H_C^\circ\) such that

\[
\sum_{a\in K}g_t(a)\ge b_t
\qquad\text{for every required row }t,
\tag{9.3}
\]

and the graph obtained from \(H_C^\circ\) by deleting the tail and head vertices used by \(K\) satisfies Hall's condition. Then \(K\) extends to a separated port permutation that is simple, positive-resident to depth four, and complete on every imposed q1, q2, and q3 row.

#### Proof

Hall gives a matching of all residual tail vertices to all residual head vertices. Together with \(K\), it is a perfect matching of the two copies of \(C\), hence a port permutation fixing the complement of \(C\). The support is conflict-free, so the resulting physical 2-factor is simple. Three-separation and collar safety give residence by Theorem 9.1. Once \(C\) is fixed, all destructions in (9.2) are fixed and every completion column contributes a nonnegative number of occurrences. Thus the bank \(K\) already meets every demand, and the residual matching cannot undo (9.3). Equation (9.1) proves all asserted cover rows. ∎

This is a genuine integral guarantee. It is stronger than necessary because one may instead handle physical two-cycle conflicts in the completion itself, but it cleanly separates the quota-first witness choice from an ordinary Hall completion.

### 9.2 The exact fractional dual and its limitation

After fixing a partial service bank \(K\), let \(L\) and \(R\) be the unused tail and head vertices, let \(E_K\subseteq H_C^\circ\) be the residual globally conflict-free allowed seam set, and put

\[
d_t=\max\left\{0,b_t-\sum_{a\in K}g_t(a)\right\}.
\tag{9.4}
\]

The fractional return problem is

\[
\begin{aligned}
&\sum_{j:(i,j)\in E_K}r_{ij}=1 &&(i\in L),\\
&\sum_{i:(i,j)\in E_K}r_{ij}=1 &&(j\in R),\\
&\sum_{(i,j)\in E_K}g_t(i,j)r_{ij}\ge d_t &&(t),\\
&r_{ij}\ge0.
\end{aligned}
\tag{9.5}
\]

### Proposition 9.3 (Farkas obstruction for a fixed separated return problem)

System (9.5) is infeasible if and only if there are free tail and head potentials \(\alpha_i,\beta_j\) and nonnegative quota potentials \(\lambda_t\) such that

\[
\alpha_i+\beta_j+
\sum_t\lambda_tg_t(i,j)\le0
\qquad((i,j)\in E_K),
\tag{9.6}
\]

while

\[
\sum_{i\in L}\alpha_i+
\sum_{j\in R}\beta_j+
\sum_t\lambda_td_t>0.
\tag{9.7}
\]

#### Proof

This is Farkas' alternative applied to the two families of equality rows and the nonnegative covering rows in (9.5). Directly, any feasible \(r\) makes the left side of (9.7) at most

\[
\sum_{(i,j)}r_{ij}
\left(\alpha_i+\beta_j+\sum_t\lambda_tg_t(i,j)\right)\le0,
\]

contradicting (9.7). The converse is the separating-hyperplane half of Farkas' lemma. ∎

With no quota rows, this dual is the usual Hall obstruction and fractional feasibility already has an integral perfect matching. With colour or shadow quotas, that integrality implication is false in general. On an abstract \(K_{2,2}\), colour the two diagonal edges with one mandatory colour and the two off-diagonal edges with a second mandatory colour. The half-on-every-edge point satisfies both colour demands, while either integral perfect matching uses only one colour. Thus:

* a certificate (9.6)--(9.7) is a rigorous no-go even for integral repair;
* absence of such a certificate is only fractional feasibility, not an integral guarantee;
* Proposition 9.2 supplies one checkable integral sufficient condition;
* a checked SAT/ILP UNSAT proof may certify the full separated integer model, but its scope remains the three-separated class;
* a CEGAR clause blocking one replay-failing permutation is sound, but is not by itself a structural dual obstruction.

The arbitrary-upper automata in Theorem 6.1 can be appended to the common assignment kernel to obtain a one-shot exact finite model. The separated master instead trades model size for fail-closed replay and CEGAR. Neither choice licenses fixed-q3 scores as a proxy for arbitrary upper coverage.

## 10. What has and has not been proved

Proved here:

* an unrestricted exact head-assignment representation of every rethreaded spanning 2-factor relative to the length-eight source;
* an exact finite family of cyclic residence-four inequalities;
* exact signed q1 safety and q1-deck-neutral return equations;
* exact lower fixed-depth witness flows and arbitrary-upper accumulated-union automata;
* an if-and-only-if finite model for strict, monotone, or complete repair of the authenticated 93-defect endpoint;
* the resulting necessity of a compound compensated repair for monotone descent within the audited length-at-most-nine port-cycle universe, and the separate strict-descent no-go for the thirty fully replayed fixed-deep-safe length-nine candidates.

Not proved:

* feasibility of SAAR-93 with objective at most 92;
* existence of a compound alternating return using the seven remaining service orbits;
* connectivity of a repaired 2-factor, or compatibility with the final word compiler after a repaired endpoint is found.

The smallest remaining mathematical/finite gate is therefore precise:

> Find a service-return circulation satisfying (6.5), the residence inequalities, and the lower/upper history flows, with (6.3); or produce a dual certificate for this exact endpoint model (or for a clearly stated support/orbit restriction of it).

A fixed-q3 gain score, a nine-row marginal provider table, or a packing of individually protected cycles is not a certificate for this gate.
