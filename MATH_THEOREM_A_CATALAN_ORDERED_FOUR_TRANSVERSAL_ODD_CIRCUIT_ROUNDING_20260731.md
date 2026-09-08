# Ordered Catalan four-transversals: projection cuts, mixed circuits, and rounding

Date: 2026-07-31  
Lane: A, global quotient matching / integral correlation  
Status: unconditional fractional theorem, a support-minimal cut outside the
original matching/cap-two/graphic relaxation, unconditional mixed-resource
odd-circuit cuts, and conditional integral rounding theorems.  A general
integral ordered four-transversal is not proved.

## 0. Verdict

Put

\[
 \mathcal L=\binom{\Omega}{m-1},\qquad
 \mathcal X=\binom{\Omega}{m},\qquad
 \mathcal U=\binom{\Omega}{m+1},\qquad |\Omega|=2m,
\]

and

\[
 K=\operatorname{Cat}_m,\qquad
 N=|\mathcal L|=|\mathcal U|=mK,\qquad
 M=|\mathcal X|=(m+1)K,
\]

\[
 d=\binom{m+1}{2}.
\]

The exact reductions in
`MATH_THEOREM_CATALAN_LINEAR_MATCHING_EXACT_REDUCTIONS_20260731.md`
show that the Catalan linear matching gate is an ordered
four-transversal with an acyclic middle trace.  The conclusions of this
note are:

1. The fully **oriented** relaxation is fractionally feasible.  One may
   orient every Johnson edge so that the constant diamond weight \(1/d\)
   satisfies the lower, upper, tail, head, cap-two, and every graphic row.
   Thus the orientation split does not create a fractional obstruction.
2. Already at \(m=2\), the original **unoriented** relaxation misses the
   support-minimal reciprocal-completion cut

   \[
                              x_{ij}+x_{ji}\le1.             \tag{0.1}
   \]

   An explicit fractional point satisfies perfect matching, every middle
   cap-two row, and every graphic inequality while giving the left side
   value \(4/3\).  On any four active coordinates in any dimension, the
   same circuit yields a valid escape inequality.
3. In the local oriented resource-conflict relaxation, the first
   support-minimal non-Helly clique has three physical atoms.  For every
   \(m\ge2\) there is a mixed
   lower--upper--tail conflict triangle
   \(\{\alpha,\beta,\gamma\}\) for which

   \[
                         z_\alpha+z_\beta+z_\gamma\le1.       \tag{0.2}
   \]

   The half-vector on those three atoms satisfies all corresponding
   resource, cap-two, and graphic rows.  Inequality (0.2) is the smallest
   possible **oriented mixed-resource** Chvatal--Gomory cut: it is obtained
   by adding three pair-conflict rows and rounding \(3/2\) down to one.
4. More generally, every strong odd resource circuit gives its odd-cycle
   stable-set inequality.  These are genuine integral-correlation rows,
   not additional shadow-capacity estimates.
5. There is an exact positive rounding theorem.  If a candidate atom
   catalogue has bipartite resource-conflict graph, supports a fractional
   lower/upper perfect matching under all four resource capacities, and all
   of its directed atoms increase one common potential on \(\mathcal X\),
   then it contains an integral acyclic ordered four-transversal.
6. Inside the one-middle-levels-cycle subclass, the missing coupling between
   the two turn SDRs is exactly the cyclic-interval discrepancy system

   \[
    \left|\#(\hbox{selected A positions in }I)
          -\#(\hbox{selected B positions in }I)\right|\le1             \tag{0.3}
   \]

   for every cyclic interval \(I\).  Equivalently, after fixing the upper
   SDR, the cyclic gaps must have a perfect matching to the lower colours.
   Once this gap-Hall condition chooses actual lower occurrences, the
   residual cross matching is forced; only the explicitly known binary-
   trace cycle face remains to be excluded.  Separate surjectivity of the
   two turn words is not enough.
7. A standard incidence-hexagon switch preserves a carried decoration
   exactly when its two selected local colour multisets and its three
   fragment-boundary types are transparent.  If the old gap-colour graph
   is a forest, the switched gap graph remains a forest exactly when the
   changed-edge attachment multigraph is graphic; the carried perfect
   matching is then unique and leaf-peelable.  This gives a precise
   “alternating SDR plus transparent gluing tree” induction target.

Consequently the global quotient perfect-matching theorem has removed the
palette Hall gate, but matching plus cap-two plus graphic inequalities do
not encode even the reciprocal completion circuit, and four separate
oriented resource shores miss non-Helly odd circuits.  The sharp constructive
target is now a fractionally perfect, monotone catalogue whose mixed
resource conflict graph can be rounded—bipartite support is one sufficient
form.  This does not prove Catalan linear matching in every dimension.

## 1. The oriented atom system

An oriented diamond atom is

\[
             \alpha=(L;a,b),qquad
 L\in\mathcal L,\quad a,b\in\Omega\setminus L,\quad a\ne b.             \tag{1.1}
\]

It has four resources

\[
\begin{aligned}
 \lambda(\alpha)&=L,\\
 \upsilon(\alpha)&=L\cup\{a,b\},\\
 \tau(\alpha)&=L\cup\{a\},\\
 \eta(\alpha)&=L\cup\{b\},
\end{aligned}                                                           \tag{1.2}
\]

and directed physical trace

\[
                         \tau(\alpha)\longrightarrow\eta(\alpha).       \tag{1.3}
\]

The two orientations \((L;a,b)\) and \((L;b,a)\) are alternatives for
the same unoriented diamond.

With a variable \(z_\alpha\), the ordered resource relaxation is

\[
\begin{aligned}
 \sum_{\lambda(\alpha)=L}z_\alpha&=1 &&(L\in\mathcal L),\\
 \sum_{\upsilon(\alpha)=U}z_\alpha&=1 &&(U\in\mathcal U),\\
 \sum_{\tau(\alpha)=X}z_\alpha&\le1 &&(X\in\mathcal X),\\
 \sum_{\eta(\alpha)=X}z_\alpha&\le1 &&(X\in\mathcal X),\\
 \sum_{\tau(\alpha),\eta(\alpha)\in S}z_\alpha&\le |S|-1
       &&(\varnothing\ne S\subseteq\mathcal X),\\
 z_\alpha&\ge0.
\end{aligned}                                                           \tag{1.4}
\]

In the first two rows both orientations of one diamond are included.  An
integral point of (1.4) is precisely an acyclic ordered four-transversal.

### Lemma 1.1 (balanced orientation)

Every finite graph has an orientation satisfying

\[
                 |\deg^+(v)-\deg^-(v)|\le1                         \tag{1.5}
\]

at every vertex.

#### Proof

Adjoin one new vertex and join it once to every odd-degree old vertex.
The number of odd-degree vertices is even, so every degree in the augmented
graph is even.  Orient an Euler tour in every nontrivial component and then
delete the added edges and vertex.  An old vertex loses at most one directed
edge, proving (1.5). \(\square\)

### Theorem 1.2 (ordered uniform fractional feasibility)

Orient the Johnson graph \(J(2m,m)\) as in Lemma 1.1.  For every diamond,
retain its orientation induced by the corresponding Johnson edge and give
that oriented atom weight

\[
                              z_\alpha={1\over d};                    \tag{1.6}
\]

give the reverse atom weight zero.  Then (1.4) holds.  The total unused
tail capacity and total unused head capacity are both exactly \(K\).

#### Proof

Every lower and every upper colour has \(d\) incident diamonds, so the
first two rows have load one.  The Johnson degree is \(m^2\).  By (1.5),

\[
 \deg^+(X),\deg^-(X)\le\left\lceil{m^2\over2}\right\rceil
                         \le {m(m+1)\over2}=d.                       \tag{1.7}
\]

Thus both directed middle loads are at most one.  Forgetting orientation,
(1.6) is exactly the uniform diamond point.  For \(|S|=s\le m+1\),

\[
 |E_J(S)|\le\binom s2\le d(s-1),
\]

while for \(s\ge m+1\),

\[
 |E_J(S)|\le {m^2s\over2}\le d(s-1).
\]

Division by \(d\) proves every graphic row.  Finally the total selected
tail load is the total atom weight \(N\), against \(M=N+K\) tail slots;
the same holds for heads. \(\square\)

Theorem 1.2 strengthens the unordered fractional theorem: even four
separate resource shores and directed orientation retain linear slack.
The obstruction is integral correlation.

There is also a fully symmetric ordered point.  Give **both** orientations
of every diamond weight \(1/(2d)\).  Each lower and upper row again has
load one, while every tail and every head has load

\[
                         {m^2\over2d}={m\over m+1}<1.     \tag{1.8}
\]

After forgetting orientation its projection is the same uniform diamond
point, so all graphic rows hold.

### Proposition 1.3 (orbit-barycentre test)

If one integral ordered four-transversal exists, the average of its
coordinate-permutation orbit under \(S_{2m}\) is the fully symmetric point
\(1/(2d)\) on every ordered atom.

#### Proof

The coordinate group is transitive on ordered atoms.  Every integral
solution has \(N\) atoms, whereas the complete ordered catalogue has
\(2dN\) atoms.  Every orbit coordinate therefore has average
\(N/(2dN)=1/(2d)\). \(\square\)

Consequently no coordinate-invariant linear inequality can separate the
fully symmetric point if the desired theorem is true.  Valid cuts must
control correlations during rounding; they need not expose a symmetric
capacity deficit.

## 2. The first exact projection and mixed-resource cuts

The orientation variables are not needed to see the first gap in the
original relaxation.  At \(m=2\), write

\[
 \Omega=\{0,1,2,3\},\qquad
 L_i=\{i\},\qquad U_j=\Omega\setminus\{j\},
\]

and denote the diamond \((L_i,U_j)\), defined for \(i\ne j\), by
\(e_{ij}\).  A perfect diamond matching is a derangement of four letters.

### Theorem 2.1 (support-minimal reciprocal-completion cut)

Every Catalan linear perfect matching at \(m=2\) satisfies

\[
                              x_{ij}+x_{ji}\le1
                              \qquad(i\ne j).             \tag{R1}
\]

Inequality (R1) is not implied by the lower/upper perfect-matching rows,
all middle cap-two rows, and all graphic inequalities.  No strict valid
one-column **upper/rank** inequality is missing from that relaxation.

#### Proof

If a derangement contains both \(i\mapsto j\) and \(j\mapsto i\), then
the two remaining letters must also be transposed.  Up to relabelling this
is \((01)(23)\).  Its four lifted Johnson edges are

\[
 02{-}03,\qquad12{-}13,\qquad02{-}12,\qquad03{-}13,
\]

which form the physical four-cycle

\[
                         02-03-13-12-02.               \tag{R2}
\]

Thus no linear forest contains both reciprocal diamonds, proving (R1).

Let \(P_{\rm dt}\) be this double-transposition matching and let \(u\) put weight
\(1/3\) on every edge of the twelve-edge crown graph \(B_2\).  Set

\[
                         x={1\over2}\chi^{P_{\rm dt}}+{1\over2}u. \tag{R3}
\]

Both summands satisfy the perfect-matching equalities.  The cycle vertices
have \(P_{\rm dt}\)-degree two and the uniform middle load is \(4/3\), so their
mixed load is \(5/3\); the other two middle vertices have mixed load
\(2/3\).  Hence every cap-two row holds.

The only graphic row violated by \(\chi^{P_{\rm dt}}\) is the row on the four
vertices of (R2).  The Johnson graph induced there is that same four-cycle,
so (R3) gives internal weight

\[
                         {1\over2}4+{1\over2}{4\over3}
                         ={8\over3}<3.                 \tag{R4}
\]

Every other graphic row holds for both summands and hence for their
average.  But

\[
                         x_{01}+x_{10}={4\over3}>1.     \tag{R5}
\]

Finally, every single diamond occurs in a four-cycle derangement, and the
representative \((0123)\) lifts to two two-edge paths and two isolates.
Coordinate relabelling handles every diamond.  Thus every one-column upper
bound \(x_e\le1\) is attained by a valid forest; two columns are support-
minimal. \(\square\)

The reciprocal circuit has a dimension-uniform escape form.  Partition

\[
             \Omega=C\sqcup A\sqcup R,\qquad
             |C|=|R|=m-2,\qquad |A|=4,                 \tag{R6}
\]

and put

\[
             L_i=C\cup\{i\},\qquad
             U_j=C\cup(A\setminus\{j\})
             \qquad(i,j\in A).                         \tag{R7}
\]

Let

\[
 \eta_C(x)=
 \sum_{i\in A}\ \sum_{\substack{U\supset L_i\\
                    U\notin\{U_j:j\in A\}}}x_{L_i,U}. \tag{R8}
\]

### Corollary 2.2 (four-coordinate escape cut)

For every integral Catalan linear perfect matching and distinct
\(i,j\in A\),

\[
                   x_{L_i,U_j}+x_{L_j,U_i}
                   \le1+\eta_C(x).                     \tag{R9}
\]

#### Proof

If \(\eta_C(x)\ge1\), (R9) follows from the two individual upper bounds.
If \(\eta_C(x)=0\), all four active lower colours are matched into the
four active upper colours and hence bijectively.  A reciprocal pair forces
the remaining two active colours to form the other reciprocal pair.  After
deleting the common core \(C\), the four lifted edges are exactly (R2), a
forbidden cycle. \(\square\)

At \(m=2\), there is no exterior escape and (R9) is exactly (R1).  For
\(m>2\), (R9) is proved valid, but no claim is made here that it is
independent of the entire original relaxation.

### The first oriented mixed-resource circuit

Two atoms conflict when they have a common resource of the same type in
(1.2).  Tail equality and head equality are different resource types; a
middle set may legally be the head of one selected atom and the tail of
another.

Fix \(L\in\mathcal L\), choose \(\ell\in L\), and choose distinct

\[
                         p,q,r\in\Omega\setminus L.                   \tag{2.1}
\]

This is possible for every \(m\ge2\).  Put

\[
\begin{aligned}
 \alpha&=(L;p,r),\\
 \beta&=(L;q,p),\\
 L'&=(L\setminus\{\ell\})\cup\{p\},\\
 \gamma&=(L';\ell,q).
\end{aligned}                                                        \tag{2.2}
\]

Their three pairwise conflicts are of three different kinds:

\[
\begin{aligned}
 \lambda(\alpha)=\lambda(\beta)&=L,\\
 \upsilon(\beta)=\upsilon(\gamma)&=L\cup\{p,q\},\\
 \tau(\gamma)=\tau(\alpha)&=L\cup\{p\}.             \tag{2.3}
\end{aligned}
\]

No one resource is common to all three.  Their heads are respectively

\[
 L+r,\qquad L+p,\qquad (L\setminus\{\ell\})+p+q,        \tag{2.4}
\]

and all remaining like-typed resources are distinct.

### Theorem 2.3 (mixed triangle cut)

Every integral ordered four-transversal satisfies

\[
                         z_\alpha+z_\beta+z_\gamma\le1.              \tag{2.5}
\]

The inequality is not implied by the corresponding unrounded resource,
middle-capacity, and graphic rows on these three columns.

#### Proof

The three equalities in (2.3) give

\[
 z_\alpha+z_\beta\le1,\qquad
 z_\beta+z_\gamma\le1,\qquad
 z_\gamma+z_\alpha\le1.                              \tag{2.6}
\]

Adding gives \(2(z_\alpha+z_\beta+z_\gamma)\le3\).  For integral
variables, rounding the right side down proves (2.5).

On the other hand, put all three variables equal to \(1/2\).  Every row
in (2.6) has load one and every other four-resource row has load at most
one half.  The three physical Johnson edges form a star with centre
\(L+p\).  Its centre load is \(3/2<2\), every leaf load is \(1/2\), and
every induced-support graphic inequality holds because the support itself
is a tree.  Hence the unrounded local rows admit this half-vector. \(\square\)

Within the resource-conflict graph, a non-Helly clique or odd circuit with
fewer than three vertices is already one resource edge.  Thus (2.5) is
support-minimal among **non-Helly resource-conflict** cuts.  The reciprocal
completion cut (R1) is a different two-column phenomenon: its two columns
share no same-type resource, and their incompatibility is forced only after
global completion.  This does not assert that (2.5) extends to a separating
face of the full oriented LP or that it alone rounds the global polytope.

### Proposition 2.4 (strong odd resource circuits)

Let \(t\ge1\), and let \(\alpha_0,\ldots,\alpha_{2t}\) be pairwise-distinct
atoms, cyclically indexed.  Suppose
that for every \(i\) there is a resource row \(R_i\) containing
\(\alpha_i,\alpha_{i+1}\), and that the chosen rows are distinct and
contain no third circuit atom.  Then every integral four-transversal obeys

\[
                         \sum_{i=0}^{2t}z_{\alpha_i}\le t.            \tag{2.7}
\]

#### Proof

Sum the \(2t+1\) pair rows
\(z_{\alpha_i}+z_{\alpha_{i+1}}\le1\).  Every variable occurs twice, so
\(2\sum_i z_{\alpha_i}\le2t+1\).  Integral rounding gives (2.7).
\(\square\)

Theorem 2.3 is the case \(t=1\).  These are stable-set odd-cycle rows in
the occurrence-labelled resource-conflict graph.  They are invisible if
the four resources are audited only one shore at a time.

## 3. A positive integral rounding theorem

For a candidate atom catalogue \(\mathcal C\subseteq\mathcal A_m\), let
\(G_{\mathcal C}\) be its **resource-conflict graph**: its vertices are
the atoms of \(\mathcal C\), and two vertices are adjacent exactly when
their atoms share a lower, upper, tail, or head resource.

### Theorem 3.1 (bipartite-conflict monotone rounding)

Assume all of the following.

1. The graph \(G_{\mathcal C}\) is bipartite.
2. There is a fractional vector \(x\in[0,1]^{\mathcal C}\) such that

   \[
   \sum_{\lambda(\alpha)=L}x_\alpha=1,qquad
   \sum_{\upsilon(\alpha)=U}x_\alpha=1,                \tag{3.1}
   \]

   for every \(L\in\mathcal L,U\in\mathcal U\), while every tail and
   head resource has load at most one.
3. There is a function \(\varphi:\mathcal X\to\mathbb R\) such that

   \[
                    \varphi(\tau(\alpha))
                       <\varphi(\eta(\alpha))
                    \qquad(\alpha\in\mathcal C).       \tag{3.2}
   \]

Then \(\mathcal C\) contains an integral acyclic ordered
four-transversal.

#### Proof

In a bipartite graph the edge--vertex incidence matrix is totally
unimodular: multiply the columns in one vertex class by \(-1\), turning
each edge row into a row with one \(+1\) and one \(-1\), the transpose of
a directed incidence matrix.  Hence

\[
 0\le y_\alpha\le1,qquad
 y_\alpha+y_\beta\le1\quad(\alpha\beta\in E(G_{\mathcal C}))          \tag{3.3}
\]

is the integral stable-set polytope of \(G_{\mathcal C}\).

The vector \(x\) is feasible in (3.3), because every conflict is witnessed
by one resource-capacity row.  Its total weight is \(N\), by summing the
lower equalities.  Every stable set has size at most \(N\), since it uses
at most one atom over each of the \(N\) lower resources.  Integrality of
(3.3) therefore gives a stable set \(S\) of size exactly \(N\).

The atoms of \(S\) have distinct lower resources, so size \(N\) makes
them cover every lower resource.  They also have distinct upper resources,
and there are exactly \(N\) of those, so they cover every upper resource.
Tail and head resources are separately injective.  Thus \(S\) is an
ordered four-transversal.  Finally (3.2) strictly increases along every
selected directed arc, excluding a directed cycle. \(\square\)

The theorem is a real rounding statement: it starts from a fractional
global quotient matching and returns an integral physical path forest.
Its hypotheses are stronger than the desired conclusion.  The full Boolean
catalogue is not bipartite, by Theorem 2.3.  The remaining constructive
problem is to find a sufficiently rich monotone subcatalogue after resolving
the mixed odd circuits, not to prove more scalar capacity.

There is a second exact rounding form that needs only two parent matchings.
Let \(P_0,P_1\) be perfect matchings of the lower--upper diamond graph, and
fix a total order \(\prec\) on \(\mathcal X\).  Orient every physical edge
in \(P_0\cup P_1\) from its smaller to its larger endpoint.  The symmetric
difference \(P_0\triangle P_1\) is a union of alternating even cycles
\(C_1,\ldots,C_t\).  A Boolean variable \(w_i\) chooses one of the two
matching parities on \(C_i\); common edges are forced.

For every two candidate atoms \(e,f\) having a common tail or a common
head, add the clause

\[
                              \neg s_e\vee\neg s_f,       \tag{3.4}
\]

where \(s_e\) is the literal selecting the parity containing \(e\).
After simplifying forced literals, these clauses form a 2-CNF
\(\Phi(P_0,P_1,\prec)\).

### Theorem 3.2 (two-parent alternating-cycle rounding)

The formula \(\Phi(P_0,P_1,\prec)\) is satisfiable if and only if the
alternating-cycle hull of \(P_0,P_1\) contains a perfect diamond matching
with injective tail and head maps under the \(\prec\)-orientation.  Every
such matching is a Catalan linear matching.

#### Proof

Choosing one parity on every symmetric-difference cycle, together with the
common edges, always gives a perfect lower--upper matching.  Clauses (3.4)
are exactly the tail/head injectivity constraints, proving the equivalence.
Every chosen arc strictly increases under \(\prec\), so the directed graph
has no cycle.  With indegree and outdegree at most one, an undirected cycle
would necessarily be directed consistently, a contradiction.  Hence the
physical lift is a linear forest. \(\square\)

This reduces a concrete two-parent rounding attempt to implication-graph
reachability.  It does not assert that every solution belongs to a
two-parent hull.  The companion note
`THREAD_A_ORDERED_FOUR_TRANSVERSAL_OCTAGON_CUT_20260731.md` proves that
simple half-integral tail--head cycles of lengths four and six always
round, while the explicit Johnson octagon

\[
 123,124,246,245,125,126,146,134,123
\]

has its two parities killed on opposite outer shores.  Its eight-atom rank
cut has right side three.  The trap suspends to every \(m\ge3\) by adjoining
a common \((m-3)\)-set to all eight vertices and leaving another disjoint
\((m-3)\)-set unused.  This is the first trap in the simple half-integral
tail--head cycle subclass.  It is not asserted to be a symmetric-difference
cycle of the two lower--upper parent matchings in Theorem 3.2.  The
reciprocal and non-Helly cuts of Section 2 have smaller support outside that
restricted cycle class.

## 4. The exact extra cut on one middle-levels cycle

Now restrict to the sufficient architecture of
`MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md`.
Write

\[
             \widehat\Omega=\Omega_0\sqcup\{\infty\},
             \qquad |\Omega_0|=2m-1,
\]

and, locally in this section,

\[
 Q=\binom{2m-1}{m-1},\qquad
 P=\binom{2m-1}{m-2},\qquad
 K=Q-P=\operatorname{Cat}_m.                           \tag{4.0}
\]

and fix a middle-levels Hamilton cycle on \(\Omega_0\)

\[
 A_0,B_0,A_1,B_1,\ldots,A_{Q-1},B_{Q-1},A_0.            \tag{4.1}
\]

Let \(p_i\in\{0,1\}\) mark the \(A_i\)-position chosen for an upper turn,
and let \(q_j\in\{0,1\}\) mark the \(B_j\)-position chosen for a lower
turn.  The two independent SDR rows are

\[
 \sum_{i:u_i=U}p_i=1\quad(U\in\tbinom{\Omega_0}{m+1}),
 \qquad
 \sum_{j:\ell_j=L}q_j=1\quad(L\in\tbinom{\Omega_0}{m-2}). \tag{4.2}
\]

For a cyclic interval \(I\) of the \(2Q\) positions, define

\[
 D(I)=\sum_{A_i\in I}p_i-\sum_{B_j\in I}q_j.             \tag{4.3}
\]

### Theorem 4.1 (cyclic interval characterization of the common SDR)

Assume the two totals in (4.2) are equal.  The selected turn occurrences
alternate in rail type around (4.1) if and only if

\[
                            -1\le D(I)\le1              \tag{4.4}
\]

for every cyclic interval \(I\).

#### Proof

If selected occurrences alternate, their restriction to any cyclic
interval is a contiguous subsequence of an alternating cyclic sequence.
Such a subsequence has rail-count discrepancy at most one.

Conversely, if the selected cyclic sequence is not alternating, two
consecutive selected occurrences in that sequence have the same rail type.
Take the cyclic interval beginning at the first and ending at the second,
with no selected occurrence strictly between them.  Its discrepancy is
\(+2\) or \(-2\), contradicting (4.4). \(\square\)

Thus (4.4) is the exact missing coupling between the two turn-surjection
systems.  When (4.2) and (4.4) hold, deleting the marked positions leaves
even paths and their cross matching is unique.  No residual matching choice
remains.

The whole fixed-cycle correlation problem is itself one ordinary
bipartite matching.  Form the augmented graph \(\mathcal G_C\) with shores

\[
 \bigl(\{A_i\}\sqcup\tbinom{\Omega_0}{m-2}\bigr)
 \quad\text{and}\quad
 \bigl(\{B_i\}\sqcup\tbinom{\Omega_0}{m+1}\bigr),       \tag{4.5}
\]

and edges

\[
 A_i u_i,\qquad \ell_i B_i,\qquad A_iB_{i-1},\qquad A_iB_i.            \tag{4.6}
\]

### Theorem 4.2 (fixed-cycle integral trace rounding)

Perfect matchings of \(\mathcal G_C\) are in bijection with simultaneous
upper and lower turn bijections whose chosen occurrences alternate around
the cycle.  Consequently, any fractional perfect matching of
\(\mathcal G_C\) rounds integrally; no further representative-rounding
lemma is needed on this fixed cycle.

#### Proof

In a perfect matching every upper-colour vertex is matched to one of its
occurrence vertices \(A_i\), and every lower-colour vertex to one of its
occurrence vertices \(B_j\).  The remaining position vertices must be
matched by the two types of cycle edges in (4.6).  Such a residual matching
exists exactly when every residual path between chosen turns has even
order, equivalently when chosen turn types alternate.  Conversely,
alternating turn bijections leave even paths, each with its unique perfect
matching.  This is the claimed bijection.  Fractional-to-integral rounding
is the ordinary integrality of bipartite perfect matching. \(\square\)

Every Hall cut of this augmented graph has an exact colour-level
compression.  For \(S\subseteq\mathbb Z_Q\), considered as \(A\)-positions,
put

\[
 \Gamma(S)=\{B_{i-1},B_i:i\in S\},\qquad
 U(S)=\{u_i:i\in S\},                                  \tag{4.7}
\]

and for a lower colour \(L\) put

\[
 O_L=\{B_j:\ell_j=L\},\qquad
 \lambda(S)=|\{L:O_L\subseteq\Gamma(S)\}|.             \tag{4.8}
\]

### Corollary 4.3 (component-Hall cuts)

The graph \(\mathcal G_C\) has a perfect matching if and only if

\[
                  |U(S)|+|\Gamma(S)|-\lambda(S)\ge|S|   \tag{4.9}
\]

for every \(S\subseteq\mathbb Z_Q\).  If \(S\) is nonempty and proper
with \(c(S)\) cyclic components, this is

\[
                         \lambda(S)-|U(S)|\le c(S).      \tag{4.10}
\]

#### Proof

An arbitrary set on the left shore of \(\mathcal G_C\) is \(S\sqcup D\),
where \(D\) is a set of lower colours.  Its neighbourhood has size

\[
                  |U(S)|+|\Gamma(S)\cup O(D)|.          \tag{4.11}
\]

The occurrence classes \(O_L\) are disjoint.  For fixed \(S\), adding
\(L\) to \(D\) changes \(|\Gamma(S)\cup O(D)|-|D|\) by
\(|O_L\setminus\Gamma(S)|-1\), which is negative exactly for the
\(\lambda(S)\) trapped classes and never becomes negative again.
Minimizing over \(D\) therefore gives
\(|\Gamma(S)|-\lambda(S)\).  Hall is exactly (4.9).  Finally every proper
cyclic component of \(S\) contributes one more neighbouring \(B\)-position
than \(A\)-positions, so \(|\Gamma(S)|=|S|+c(S)\), giving (4.10).
\(\square\)

There is an exact Hall separator that avoids guessing both shores at once.
Fix an upper transversal \(I=\{i_0,\ldots,i_{P-1}\}\), cyclically ordered,
and let

\[
                  G_t=[i_t,i_{t+1})_{\mathbb Z_Q}       \tag{4.12}
\]

be the set of intervening \(B\)-positions.  Form the bipartite graph
\(\Gamma_I\) whose left shore is the \(P\) gaps, whose right shore is the
\(P\) lower turn colours, and where

\[
 G_t\sim L
 \quad\Longleftrightarrow\quad
 \ell_j=L\text{ for some }j\in G_t.                    \tag{4.13}
\]

### Theorem 4.4 (fixed-upper gap-Hall equivalence)

The upper transversal \(I\) extends to alternating bijective lower
representatives if and only if \(\Gamma_I\) has a perfect matching.
Equivalently,

\[
 \left|\left\{\ell_j:
       j\in\bigcup_{G\in\mathcal S}G\right\}\right|
       \ge |\mathcal S|                                 \tag{4.14}
\]

for every family \(\mathcal S\) of \(I\)-gaps.

#### Proof

Between consecutive selected \(A\)-positions an alternating selection has
exactly one selected \(B\)-position.  Bijectivity makes the corresponding
lower colours distinct, so they define a perfect matching of \(\Gamma_I\).
Conversely, choose in every matched gap one occurrence of its matched lower
colour.  There is then exactly one lower mark in every upper gap and every
lower colour is used once, which is precisely alternation.  Formula (4.14)
is Hall's theorem. \(\square\)

This gives the exact fixed-upper min--max gate

\[
 \exists\ I\text{ that is an upper SDR and satisfies (4.14)}.           \tag{4.15}
\]

It is strictly stronger than the existence of separate SDRs.  Indeed, if
\(i,i+1,i+2\) are three upper occurrences forced by globally unique upper
turn colours, alternation forces the two intervening lower positions
\(i,i+1\).  If \(\ell_i=\ell_{i+1}\), then the two singleton gaps have
only one lower neighbour, violating (4.14).

The authenticated \({\rm ML}(7)\) Hamilton cycle in
`MATH_THEOREM_CATALAN_ALTERNATING_TURN_SDR_HALL_AND_M4_COUNTEREXAMPLE_20260731.md`
has both turn words surjective but has exactly this obstruction:

\[
 u_9=115,qquad u_{10}=121,qquad u_{11}=124
\]

are globally unique, while

\[
                         \ell_9=\ell_{10}=96.           \tag{4.16}
\]

All \(12{,}288\) upper SDRs fail; the best gap matching has size
\(20<21\).  By contrast, every audited \({\rm ML}(5)\) Hamilton cycle is
decorable.  Therefore a recursive middle-levels construction must preserve
gap-Hall/interlacing, not merely the two turn surjections.

The negative \({\rm ML}(7)\) cycle is not a no-go for this architecture:
one standard incidence-hexagon toggle repairs it.  The local transfer rule
is exact.  Let \(H\in\binom{\Omega_0}{m-2}\) and choose distinct
\(a,b,c\notin H\).  The six sets

\[
 H+a,\ H+b,\ H+c,
 \qquad H+a+b,\ H+b+c,\ H+c+a                         \tag{4.17}
\]

form an incidence hexagon with alternating matchings

\[
\begin{aligned}
 M_0&=\{(H+a,H+a+b),(H+b,H+b+c),(H+c,H+c+a)\},\\
 M_1&=\{(H+a,H+c+a),(H+b,H+a+b),(H+c,H+b+c)\}.
\end{aligned}                                         \tag{4.18}
\]

Suppose this is a valid factor switch:

\[
 C\cap E(Z)=M_0,
 \qquad C'=(C-M_0)\cup M_1
\]

is again a cycle or two-factor, where \(Z\) is the displayed incidence
hexagon.  Deleting \(M_0\) leaves at most three retained path fragments.
Here a decoration of a two-factor means globally exact selected palettes on
both shores together with alternating selected shore types on every factor
cycle.

### Theorem 4.5 (transparent-hexagon transfer)

Fix one decoration \(D=(D_A,D_B)\) of \(C\).  The same selected vertex
sets decorate \(C'\) if and only if:

1. separately on the two shores, the multisets of turn colours contributed
   by selected vertices among the six hexagon vertices are the same before
   and after the toggle; and
2. on each new factor cycle, after orienting the retained fragments in their
   new cyclic order, the last selected shore type on every fragment whose
   selected subsequence is nonempty is opposite the first selected shore
   type on the next such fragment.

#### Proof

Only neighbour pairs at the six hexagon vertices change.  All selected turn
colours outside the hexagon are fixed, so global bijectivity is preserved
exactly when the two local selected colour multisets are preserved.
Alternation inside every retained fragment is unchanged, even when the
fragment is reversed.  Its only possible failures after reconnection are at
the new seams, and Condition 2 is exactly their exclusion. \(\square\)

For a Hamilton-to-Hamilton toggle, if a trace breaker—an unmarked run of
length at least four or an even marked run—lies away from the six ports, the
same toggle preserves forest topology.  For a two-factor one needs such a
breaker on every component whose lift is claimed to be a forest.  More
generally one may carry the exact one-bit state “outside the unique bad
trace face” separately on each relevant component.

There is also an exact transfer rule for the newly observed unique-gap-
matching invariant.  Label a gap occurrence by its unoriented retained
interval, equivalently by the unordered pair of selected upper-turn
occurrences at its ends, distinguishing the two cyclic arcs if the endpoint
pair alone is ambiguous.  This label survives reversal of a retained
fragment.  Thus only the seam-crossing gap occurrences are replaced.  Let
\(\Gamma\) and \(\Gamma'\) be the old and new gap--lower-colour graphs and,
using these occurrence labels, put

\[
 E_0=E(\Gamma)\cap E(\Gamma'),\qquad
 A=E(\Gamma')\setminus E(\Gamma),                       \tag{4.19}
\]

View \(E_0\) on the vertex set \(V'=V(\Gamma')\); in particular every new
gap occurrence starts as an isolated vertex, while old-only gap occurrences
are discarded.  Contract every connected component of \((V',E_0)\).  Let
\(\mathcal K\) be the resulting component set, and let \(A[\mathcal W]\)
denote new edges whose two contracted endpoints lie in
\(\mathcal W\subseteq\mathcal K\).  Loops and parallel edges retain their
usual multiplicity.

### Theorem 4.6 (transparent gap-forest transfer)

Assume \(\Gamma\) is a forest and the fixed decoration survives the switch
by Theorem 4.5.  Then \(\Gamma'\) is a forest if and only if

\[
                    |A[\mathcal W]|\le|\mathcal W|-1
       \qquad(\varnothing\ne\mathcal W\subseteq\mathcal K).            \tag{4.20}
\]

Whenever (4.20) holds, \(\Gamma'\) has a unique perfect matching and is
leaf-peelable.

#### Proof

The common graph \((V',E_0)\) consists of a subforest of \(\Gamma\), together
with isolated new gap vertices, and is therefore a forest.  Moreover
\(\Gamma'=(V',E_0\cup A)\).  Adding the new edges creates a cycle exactly
when, after contracting the components of \((V',E_0)\), a new edge becomes
a loop or the new-edge multigraph contains a cycle.  The full graphic system
for that contracted multigraph is precisely (4.20), proving the first
assertion.

The transparent fixed decoration chooses one lower colour in every new gap
and every lower colour once, so it supplies a perfect matching of
\(\Gamma'\).  A forest has at most one perfect matching, because the
symmetric difference of two distinct perfect matchings is a union of even
cycles.  Finally a nonempty forest with a perfect matching has a leaf; its
incident matching edge is forced.  Removing that matched pair and iterating
gives leaf peeling. \(\square\)

Thus the extra local row beyond transparency is not another Hall family:
it is the contracted graphic row (4.20) on the changed gap-colour edges.
The observed \(m=2,3,4\) gap forests satisfy it, but no all-\(m\) claim is
made.

For the explicit negative cycle above, take the hexagon

\[
 H=33,\qquad(a,b,c)=(3,4,6),                           \tag{4.21}
\]

which, with \(M_0,M_1\) interchanged relative to (4.18), replaces edges

\[
 (41,105),(49,57),(97,113)
 \quad\text{by}\quad
 (41,57),(49,113),(97,105).                           \tag{4.22}
\]

The resulting authenticated positive Hamilton cycle is decorable and its
mark trace has a zero-run of length six.  Its diamond lift is therefore a
spanning \(\operatorname{Cat}_4=14\)-path forest.  The finite census has 31
alternating hexagons around this repaired positive cycle, 16 Hamilton
outputs, 10 decorable outputs, and only 6 outputs sharing a decoration with
that positive input.  Thus transparency is real but not automatic.

### Corollary 4.7 (transparent gluing-tree implication)

Suppose a recursive middle-levels factor starts with a **componentwise
decoration**: the selected upper and lower turn palettes are globally exact,
and the selected shore types alternate on every initial factor cycle.
Suppose it admits a component-merging tree of valid incidence-hexagon
toggles.  If every toggle is transparent for the currently carried
decoration and one protected trace breaker survives every toggle into the
final Hamilton trace, then the final Hamilton cycle is decorable and its
diamond lift is a spanning \(\operatorname{Cat}_m\)-path forest.  If the
initial gap graph is a forest and every toggle also passes (4.20), every
intermediate and final gap graph has a unique, leaf-peelable perfect
matching.

#### Proof

Induct along the gluing tree using Theorem 4.5.  It preserves both palettes
and alternating representatives; the breaker excludes the sole cycle face.
When assumed, Theorem 4.6 propagates the gap-forest invariant.  The final
decorated-cycle equivalence gives the exact diamond matching and path
forest. \(\square\)

This is the correct recursive target: a joint alternating SDR together with
a transparent gluing tree.  Neither an arbitrary frozen SDR nor an arbitrary
published gluing tree is sufficient.

The physical topology then has only the exact binary-trace exception.  If
the cyclic mark word is

\[
             1^{a_1}0^{b_1}\cdots1^{a_s}0^{b_s},        \tag{4.23}
\]

it contains one physical cycle exactly when every \(b_t=2\) and every
\(a_t\) is odd.  Hence a decorated-cycle solution is a forest iff at least
one zero-run has length at least four or at least one marked run has even
length.  This is a final trace no-good, not a new palette row.

Two exact consequences make this topology face small.  On the bad face the
\(2K\) unmarked positions form \(K\) runs of length two, hence there are
\(K\) marked runs, all of odd length.  Their total marked length is \(2P\),
which is even.  Therefore:

### Corollary 4.8 (odd Catalan automatic forest)

If \(K=\operatorname{Cat}_m\) is odd, every decoration supplied by
Theorem 4.2 is already a linear forest.

When \(K\) is even, one explicit escape is also an ordinary matching test.
If \(\mathcal G_C\) has a perfect matching containing both residual cycle
edges \(A_iB_i\) and \(A_{i+1}B_{i+1}\), then four consecutive positions
are unmarked, so a zero-run has length at least four and the lift is a
forest.  Equivalently, delete those four position vertices and ask for a
perfect matching of the remaining balanced bipartite graph.

Theorems 4.1--4.4 apply only after fixing one middle-levels Hamilton cycle
and its turn occurrence lists.  An arbitrary Catalan linear matching need
not be middle-levels-resolvable; the explicit \(m=3\) counterexample in the
companion trace-decoration note forbids that overclaim.

## 5. Relation to the three-primary quotient lane

The global quotient perfect-matching theorem remains the correct first
step when \(3\mid(2m-1)\): it automatically services the shortened Catalan
banks.  The period-three filters therefore do not create a residual Kneser
Hall problem.  What the quotient matching does **not** supply is the
integral correlation between its four resources and its physical trace.

At the clean subgroup scale, the ordered atom system, mixed-resource cuts,
and rounding theorems apply to occurrence-labelled quotient atoms, with
parallel voltage/endpoint options kept distinct.  A quotient solution still
requires a private endpoint
cycle whose total voltage generates the clean cyclic group.  The common-cap
compiler may subsequently break the quotient symmetry.

The support-minimal proved projection row is (R1); its dimension-uniform
escape form is (R9).  At orientation level the first non-Helly row is
(2.5), and the first positive unrestricted-support rounding target is
Theorem 3.1.  Neither gives the all-\(m\) construction.
The precise unproved lemma is:

> Find, for every \(m\), either an integral acyclic ordered
> four-transversal directly, or a subcatalogue satisfying Theorem 3.1.
> In the middle-levels-resolvable subclass, it is enough to choose one
> upper SDR satisfying the exact gap-Hall rows (4.14), equivalently solve
> both turn SDRs together with the interval rows (4.4), and avoid the single
> trace cycle face (4.23).  A recursive sufficient route is to preserve
> these data through a transparent hexagon gluing tree as in Corollary 4.7,
> imposing the exact contracted gap-graphic row (4.20) at every switch.

No bound from the retracted `GK_PROJECTION_COUNTS` / `GK_TWO` linear-
subforest estimate is used here.  In particular, this note makes no
\(W/2\)-retention claim.
