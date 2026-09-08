# The rank-plateau obstruction to the proposed `k=17` alternating prefix

Date: 2026-07-31  
Status: proved source-independent no-go for the saturated pair/four-window
prefix architecture; exact count-preserving replacement model stated, but
not solved.

**Independent scope correction.**  The current one-pivot two-zone proposal
uses `7399` internal prefix **triple** owners plus two seam triples, not
`7398` internal four-window owners plus three seam windows.  Consequently
the theorem below remains valid for its stated pair/four-window architecture
and its `3699` displacement bound, but it does **not** disprove the current
mixed-width alternating prefix.  On the live face, consecutive distinct
rank-nine triples make every intervening four-window have rank ten.  See
`MATH_AUDIT_K17_TWO_ZONE_PREFIX_AND_LONG_RANK_SCOPE_20260731.md`.

## 0. Verdict

The alternating prefix requested in the two-zone proposal cannot exist.
This is not a failure of the particular `2537`-block inventory, a weak Hall
bound, or an unlucky separator order.  It is already impossible in the
literal path of adjacent-union colours.

For a prefix of length `7401`, the proposal asks for

* all `7400` adjacent-pair unions to be distinct rank-eight masks; and
* all `7398` internal four-window unions, together with three seam-crossing
  four-windows, to be the `7401` complementary rank-nine masks.

The first condition forces every two consecutive internal four-window
owners to be equal whenever both have rank nine.  Hence all `7398` internal
owners coincide.  Even granting three arbitrary seam owners, the prefix
can supply at most four distinct rank-nine masks, not `7401`.

More quantitatively, any length-`7401` architecture with pairwise-distinct
rank-nine four-windows can place distinct rank-eight targets in at most
`3701` adjacent-pair positions.  Thus repairing the architecture without
changing the four-window row requires moving at least

\[
                         7400-3701=3699
\]

rank-eight targets away from adjacent-pair cells.

No finite search is needed or justified for the stated gate.

## 1. The exact trace projection

Let

\[
                     P=(p_0,p_1,\ldots,p_{7400})
\]

be any literal set word.  Define its adjacent-pair colours and internal
four-window owners by

\[
 E_j=p_j\cup p_{j+1},\qquad 0\le j\le7399,             \tag{1.1}
\]

and

\[
 F_i=p_i\cup p_{i+1}\cup p_{i+2}\cup p_{i+3},
       \qquad 0\le i\le7397.                            \tag{1.2}
\]

This is the smallest exact graph model of the proposed prefix: the literal
word is a path whose edge labels are the \(E_j\), while the proposed owner
label on a four-letter interval—equivalently, an interval of three path
edges—is \(F_i\).

The full block/separator formulation projects to (1.1)--(1.2).  Indeed,
orient every two-letter low block and regard it as a fixed internal edge.
For a port carrying a low letter \(A\), a rank-seven separator \(B\), and a
rank-eight colour \(V\), the exact incidence flags are

\[
 \mathcal F=\{(A,B,V): |A\setminus B|=1,\ V=A\cup B\}. \tag{1.3}
\]

Equivalently, \(A\subseteq V\), \(V=B\cup\{x\}\), and \(x\in A\).
A proposed solution selects two flags at every separator, uses all but two
block-port occurrences, uses every required rank-eight colour once, and,
after adjoining the fixed block edges, forms one alternating spanning path.
Consecutive selected flags determine the four-window labels (1.2).

Thus any feasible point of any more detailed flag, matching, flow,
hypergraph, or SAT model must first satisfy the path projection
(1.1)--(1.2).  The obstruction below is therefore a valid dual certificate
for every such formulation.

## 2. Rank-plateau lemma

### Lemma 2.1 (two central edges freeze adjacent owners)

Let \(q_i,\ldots,q_{i+4}\) be sets, put

\[
 E_{i+1}=q_{i+1}\cup q_{i+2},\qquad
 E_{i+2}=q_{i+2}\cup q_{i+3},
\]

and put

\[
 F_i=\bigcup_{j=i}^{i+3}q_j,qquad
 F_{i+1}=\bigcup_{j=i+1}^{i+4}q_j.
\]

For any integer \(r\ge0\), if

\[
 |E_{i+1}|=|E_{i+2}|=r,\quad E_{i+1}\ne E_{i+2},\quad
 |F_i|=|F_{i+1}|=r+1,                                 \tag{2.1}
\]

then

\[
 F_i=F_{i+1}=E_{i+1}\cup E_{i+2}.                     \tag{2.2}
\]

#### Proof

Both \(F_i\) and \(F_{i+1}\) contain

\[
 E_{i+1}\cup E_{i+2}
   =q_{i+1}\cup q_{i+2}\cup q_{i+3}.                  \tag{2.3}
\]

The union of two distinct \(r\)-sets has size at least \(r+1\).  By
(2.1), the set in (2.3) is contained in each of two \((r+1)\)-sets.
Consequently it has size exactly \(r+1\) and equals both.  This proves
(2.2).  \(\square\)

The proof uses only literal containment and cardinality.  In particular it
is independent of block types, separator ranks, cyclic symmetry, and the
tail.

## 3. Exact no-go for the advertised prefix

### Theorem 3.1 (saturated pair/four-window incompatibility)

There is no length-`7401` word \(P\) for which

1. \(E_0,\ldots,E_{7399}\) are pairwise-distinct rank-eight sets; and
2. \(F_0,\ldots,F_{7397}\) are pairwise-distinct rank-nine sets.

In fact, under condition 1, if all the \(F_i\) merely have rank nine, then

\[
                         F_0=F_1=\cdots=F_{7397}.       \tag{3.1}
\]

#### Proof

Apply Lemma 2.1 with \(r=8\) for every
\(0\le i\le7396\).  The two central pair colours \(E_{i+1}\) and
\(E_{i+2}\) are distinct rank-eight sets, while \(F_i,F_{i+1}\) are
rank-nine sets.  Therefore \(F_i=F_{i+1}\).  Chaining these equalities gives
(3.1), contradicting pairwise distinctness.  \(\square\)

### Corollary 3.2 (the advertised two-zone four-window deficiency)

In the two-zone ledger, the tail has `16909` internal rank-nine
four-windows, so the prefix and its seam are required to supply the other

\[
                         24310-16909=7401
\]

rank-nine masks.  Under the proposed `7400`-colour adjacent-pair rainbow,
the internal prefix supplies at most one distinct rank-nine owner.  The
three seam-crossing starts can supply at most three more.  Therefore the
advertised four-window owner row has support at most four and therefore
four-window owner deficiency at least

\[
                         7401-4=7397.                  \tag{3.2}
\]

This refutes the alternating-prefix gate in item `2322K17` of the handoff.
The corrected tail-ear packing and long-rank facet-run questions from that
item remain separately scoped; neither can repair (3.2) while this fixed
prefix/tail ledger is retained.

## 4. Integral packing dual and minimum displacement

The obstruction has a useful scalar dual that applies to redesigned
prefixes as well.

Let \(x_j\in\{0,1\}\) indicate that adjacent-pair position \(j\) is assigned
a rank-eight target, with all assigned rank-eight targets distinct.  Suppose
the internal four-window owners are pairwise-distinct rank-nine sets.  For
every \(0\le i\le7396\), Lemma 2.1 gives the valid inequality

\[
                         x_{i+1}+x_{i+2}\le1.           \tag{4.1}
\]

The variables \(x_1,\ldots,x_{7398}\) therefore form an independent set in
a path on `7398` vertices.  Summing the disjoint inequalities with
\(i=0,2,\ldots,7396\) gives

\[
                  \sum_{j=1}^{7398}x_j\le3699.         \tag{4.2}
\]

The two exterior pair positions \(0,7399\) do not occur together as the two
central edges of adjacent internal four-windows, so they contribute at most
two further assignments.  Hence

\[
                  \sum_{j=0}^{7399}x_j\le3701.         \tag{4.3}
\]

The bound is the exact independence number of this projected path system.
It follows that the current saturated demand of `7400` rank-eight pair
cells exceeds the projected capacity by at least `3699`.

This is stronger than a failed Hall cut in the `2537`-block incidence
hypergraph: it remains valid after arbitrary block replacement, arbitrary
separator choice, and arbitrary ordering.

## 5. A count-preserving replacement trace model

The no-go is specific to assigning the complementary rank-nine palette to
**four**-letter prefix windows while every adjacent pair is rank eight.  A
count-preserving alternative at the trace level is to use triple windows.
A length-`7401` prefix has `7399` internal triple starts and exactly two
triple starts crossing its seam with the tail, for a total of `7401`.

Retain (1.1) and define

\[
 H_i=p_i\cup p_{i+1}\cup p_{i+2}=E_i\cup E_{i+1},
       \qquad 0\le i\le7398.                           \tag{5.1}
\]

If \(E_i,E_{i+1}\) are distinct rank-eight sets, then \(H_i\) has rank nine
exactly when \(E_i,E_{i+1}\) are adjacent in \(J(17,8)\).  Thus the corrected
trace problem is:

* order the `7400` residual rank-eight colours as a Hamilton path in
  \(J(17,8)\);
* make its `7399` internal edge colours \(E_i\cup E_{i+1}\), together with
  two seam colours, the complementary rank-nine palette; and
* factor that trace into the prescribed physical low blocks and rank-seven
  separators.

At a separator occurrence \(p_{i+1}\) of rank seven, physicality forces

\[
                         p_{i+1}=E_i\cap E_{i+1}.       \tag{5.2}
\]

At a low occurrence it requires the corresponding literal letter to lie in
the intersection and both adjacent literal unions to equal the prescribed
\(E\)-colours.  These factorization rows are additional to the trace path.

### Theorem 5.1 (exact graphic-Rado relaxation)

Fix a residual rank-eight vertex set \(\mathcal R_8\) of size `7400`, reserve
two rank-nine colours for the two seam triples, and let \(\mathcal R_9^\circ\)
be the remaining `7399` internal rank-nine colours.  For
\(H\in\mathcal R_9^\circ\), let

\[
 \mathcal E_H=\{UV:U,V\in\mathcal R_8,\ U\ne V,\ U\cup V=H\}. \tag{5.3}
\]

There is a rainbow spanning tree choosing one edge from every
\(\mathcal E_H\) if and only if, for every
\(\mathcal A\subseteq\mathcal R_9^\circ\),

\[
 r_{\rm gr}\!\left(\bigcup_{H\in\mathcal A}\mathcal E_H\right)
       \ge |\mathcal A|.                               \tag{5.4}
\]

Equivalently, writing \(N(\mathcal A)\) for the incident rank-eight vertices
and \(c(\mathcal A)\) for the number of components of the candidate graph
on those vertices,

\[
                         |N(\mathcal A)|-c(\mathcal A)
                              \ge|\mathcal A|.          \tag{5.5}
\]

#### Proof

Apply Rado's independent-transversal theorem to the graphic matroid on the
candidate Johnson edges and the family
\((\mathcal E_H)_{H\in\mathcal R_9^\circ}\).  The graphic rank of an edge
set is the number of its incident vertices minus the number of its
nonempty components, giving (5.5).  A successful transversal has `7399`
independent edges on an ambient set of `7400` vertices, hence is a spanning
tree.  \(\square\)

The tree criterion does **not** imply a Hamilton path.  The exact path
strengthening is the binary system

\[
 \sum_{e\in\mathcal E_H}x_e=1
       \quad(H\in\mathcal R_9^\circ),                  \tag{5.6}
\]

\[
 \sum_{e\ni U}x_e=2-s_U,qquad
 s_U\in\{0,1\},\qquad\sum_U s_U=2,                    \tag{5.7}
\]

and

\[
 \sum_{e\subseteq S}x_e\le |S|-1
       \quad(\varnothing\ne S\subsetneq\mathcal R_8).\tag{5.8}
\]

A star shows sharply why (5.4) alone cannot supply (5.7).  Even a solution
of (5.6)--(5.8) must still pass the occurrence-labelled block/separator
factorization, the two seam colours, residence, all deeper shadows, and the
common-cap compiler.  Theorem 5.1 is therefore an exact corrected trace
reduction, not a `k=17` construction.

## 6. Scope and independent audit

The no-go proves:

* no choice of the `680/972/676/209` low-block inventory can solve the
  stated saturated pair/four-window prefix;
* no separator Hall theorem, path ordering, or heavy exact search can solve
  it; and
* any repair on the same length-`7401` prefix that retains pairwise-distinct
  internal rank-nine four-window owners must displace at least `3699` of the
  distinct rank-eight pair assignments.

It does **not** disprove:

* the triple-window trace architecture of Section 5;
* an architecture with non-rank-eight reset pair cells;
* a longer word or a different rank allocation; or
* a nonflat compiler that realizes the rank-nine complement elsewhere.

The decisive set-theoretic step was independently derived twice.  The
companion audit script verifies the normalized facet identity and the exact
`3699/3701` path-capacity arithmetic without using any proposed inventory or
solver artifact.
