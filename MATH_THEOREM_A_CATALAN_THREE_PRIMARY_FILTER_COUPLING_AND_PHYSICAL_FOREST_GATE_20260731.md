# Three-primary global matching, physical filter packets, and the exact forest gate

Date: 2026-07-31  
Lane: A, general Catalan sector-braid theorem  
Status: exact global-first quotient-matching theorem, exact
symmetry-breaking lower bound, two audited optional filter normal forms,
and an exact physical-forest/unit-voltage equivalence.  The global physical
selection is not proved.

## 0. Verdict

Let

\[
 q=2m-1,\qquad
 K=\operatorname{Cat}_m,\qquad
 N=mK,\qquad M=(m+1)K,\qquad
 s=3^{v_3(q)},\qquad h=q/s,\qquad
 G=\mathbb Z_q,\qquad H=\langle s\rangle\cong\mathbb Z_h .
\]

When \(3\mid q\), write

\[
 m=3a+2,\qquad q=6a+3,\qquad
 \kappa=\operatorname{Cat}_a,\qquad r=s/3.
\]

The exact conclusions are as follows.  All statements involving
\(a,\kappa,r\) below are under the additional hypothesis \(3\mid q\).

1. There are \(\kappa\) shortened full-\(G\) colour orbits on each outer
   shore.  Each splits into \(r\) \(H\)-orbits.
2. Every \(H\)-equivariant two-sided exact transversal uses exactly
   \(\kappa r\) lower-short/free-upper and \(\kappa r\)
   free-lower/upper-short edge orbits, and no short/short edge.
3. Its distance from residual-\(\mathbb Z_s\)-invariance is at least

   \[
          2\kappa r+r\,{\mathbf 1}_{3\nmid\kappa}.        \tag{0.1}
   \]

   It has at least

   \[
          2\kappa+{\mathbf 1}_{3\nmid\kappa}             \tag{0.2}
   \]

   partial full-\(G\) edge orbits.  These are occurrence-orbit counts, not
   physical seam counts.
4. The complete lower--upper diamond graph modulo \(H\) is balanced and
   regular.  Choosing a quotient perfect matching first therefore gives an
   unconditional global exact outer-colour matching.  Its restriction to
   the exceptional banks is already globally extendable, uses distinct
   opposite colours, and has pairwise-distinct physical middle endpoints.
   Prescribed-filter Hall is not the existential gate.
5. Two different optional normal forms are available through the whole
   \(3\)-primary tower:

   * an antipodal, setwise-complement two-edge bank using exactly
     \(2\kappa\) partial full-\(G\) edge orbits; and
   * a physical inclusion-flag \(P_4\) packet bank, with a native omitted
     socket whose replacement is topology- and voltage-neutral.

   They are not the same bank.  Neither is forced on a global matching.
6. The exact remaining carrier gate is to choose **among global quotient
   perfect matchings** one whose Johnson lift is a spanning linear forest
   with \(K/h\) paths, then choose pairwise-private endpoint connectors
   forming one quotient cycle whose total \(H\)-voltage generates \(H\).
   With literal directed-repair/collar rows included, the displayed system
   in Section 5 is necessary and sufficient.

Thus the shortened palettes and their marginal extension are solved.  The
unproved statement is a common global matching--graphic--endpoint-cycle
selection.  No K17 statement and no all-\(m\) existence claim is made.

## 1. The exact exceptional and normal orbit ledger

Put

\[
 {\cal L}=\binom{\mathbb Z_q\sqcup\{\infty\}}{m-1},
 \qquad
 {\cal U}=\binom{\mathbb Z_q\sqcup\{\infty\}}{m+1},
 \qquad
 N=|{\cal L}|=|{\cal U}| .
\]

Let \(J\le G\) be the unique subgroup of order three, and put
\(\pi:G\to G/J\).  The period-three theorem gives the shortened colours

\[
 L_A=\{\infty\}\cup\pi^{-1}(A),
 \quad A\in\binom{G/J}{a},                               \tag{1.1}
\]

and

\[
 U_B=\pi^{-1}(B),
 \quad B\in\binom{G/J}{a+1}.                             \tag{1.2}
\]

Every such colour has stabilizer exactly \(J\).  The action on the
\(a\)-subsets of \(G/J\cong\mathbb Z_{2a+1}\) is free, so the number of
short full-\(G\) orbits on either shore is

\[
 \frac1{2a+1}\binom{2a+1}{a}
   =\operatorname{Cat}_a=\kappa.                         \tag{1.3}
\]

Every short full orbit has \(q/3\) physical colours and decomposes into
\(r=s/3\) \(H\)-orbits.  If \(F\) is the number of free full-\(G\) colour
orbits on either shore, the exact quotient count is

\[
                   \frac Nh=sF+\kappa r.                 \tag{1.4}
\]

For a Johnson edge \(e=XY\), write

\[
 \ell(e)=X\cap Y,\qquad u(e)=X\cup Y .
\]

### Lemma 1.1 (forced short/free type ledger)

No Johnson edge has both \(\ell(e)\) and \(u(e)\) shortened.  Consequently
every \(H\)-equivariant common transversal has quotient edge-type counts

\[
\begin{array}{c|cccc}
\text{type}&SS&SF&FS&FF\\ \hline
\text{count}&0&\kappa r&\kappa r&N/h-2\kappa r .
\end{array}                                              \tag{1.5}
\]

Here the first letter refers to the lower shore.

#### Proof

A shortened lower colour contains \(\infty\), whereas a shortened upper
colour avoids it.  Since \(\ell(e)\subset u(e)\), they cannot occur on one
edge.  Every shortened outer \(H\)-orbit must nevertheless be met exactly
once.  There are \(\kappa r\) on each shore, proving (1.5). \(\square\)

## 2. Exact ternary filters and the minimum symmetry breaking

Let \(S=G/H\cong\mathbb Z_s\), and let \(K_3=JH/H\le S\).  A shortened
colour orbit in the \(H\)-quotient is \(S/K_3\cong\mathbb Z_r\), while
every full-\(G\) Johnson-edge orbit becomes a regular \(S\)-orbit.

For one shortened colour orbit \(\alpha\), index candidate regular provider
orbits by \(c\).  After choosing origins, their colour maps have the form

\[
 S\longrightarrow S/K_3,\qquad z\longmapsto z+\eta_c+K_3 .
\]

With binary variables \(x_{c,z}\), exact coverage of the shortened row is
therefore

\[
 \boxed{\quad
 \sum_c\ \sum_{k\in K_3}x_{c,j-\eta_c+k}=1
 \qquad(j\in S/K_3).\quad}                              \tag{2.1}
\]

For a normal colour orbit the corresponding map is bijective and its row
is

\[
                   \sum_c x_{c,j-\eta_c}=1
                   \qquad(j\in S).                       \tag{2.2}
\]

Equation (2.1) is the exact orbit-imbalance ledger.  Making each
\(x_{c,\cdot}\) constant would make its left side divisible by three, so
residual \(S\)-equivariance is impossible.

For a selected quotient-edge set \(T\subseteq E(B_m)/H\), and for every
full-\(G\) edge orbit
\({\cal O}\), put

\[
 z_{\cal O}=|T\cap({\cal O}/H)|,
 \qquad
 d_S(T)=\sum_{\cal O}\min\{z_{\cal O},s-z_{\cal O}\}.     \tag{2.3}
\]

This is the quotient-Hamming distance from the nearest union of complete
residual \(S\)-orbits, measured orbit by orbit.  The corresponding physical
distance is \(h\,d_S(T)\).

### Theorem 2.1 (global symmetry-breaking lower bound)

Every \(H\)-equivariant exact two-sided common transversal satisfies

\[
 d_S(T)\ge
       2\kappa r+r\,{\mathbf 1}_{3\nmid\kappa},           \tag{2.4}
\]

and uses at least

\[
       2\kappa+{\mathbf 1}_{3\nmid\kappa}                \tag{2.5}
\]

partial full-\(G\) edge orbits.

The first \(2\kappa r\) units and first \(2\kappa\) partial orbits are
forced by the shortened banks.  The possible extra term is forced on a
free/free orbit and is independent of the exceptional construction.

#### Proof

An edge orbit incident with one fixed shortened full colour orbit projects
three-to-one onto its \(r\) shortened \(H\)-vertices.  Matching capacity
therefore gives \(z_{\cal O}\le r<s/2\).  Hence its contribution to
\(d_S\) is exactly \(z_{\cal O}\).  Summing over both disjoint shortened
banks and using (1.5) gives exactly \(2\kappa r\).

The selected free/free count is

\[
 \frac Nh-2\kappa r=sF-\kappa r.                         \tag{2.6}
\]

Full residual edge orbits contribute multiples of \(s=3r\).  On the
circle \(\mathbb Z_s\), the triangle inequality gives

\[
 \sum_{\substack{{\cal O}\\\mathrm{free/free}}}
      \min\{z_{\cal O},s-z_{\cal O}\}
 \ge \operatorname{dist}_{\mathbb Z_s}(-\kappa r,0).
\]

The last distance is zero if \(3\mid\kappa\), and \(r\) otherwise.  This
proves (2.4).  Each shortened full colour orbit requires a distinct partial
edge orbit, and the lower and upper collections are disjoint by Lemma 1.1.
If \(3\nmid\kappa\), (2.6) is not divisible by \(s\), so at least one
free/free edge orbit is partial.  This proves (2.5). \(\square\)

The numerical bounds are sharp in the orbit-occupancy relaxation: use
\(r\) selected cells in every shortened carrier orbit and, when required,
one free/free partial orbit of size \(r\) or \(2r\).  This is not an
attainment claim for the physical incidence or forest constraints.

For one provider orbit used alone above one shortened orbit, an exact
selector is a section \(\sigma:\mathbb Z_r\to\mathbb Z_s\).  Writing

\[
 \sigma(j+1)-\sigma(j)=1+r\varepsilon_j,
 \qquad \varepsilon_j\in\mathbb Z_3,
\]

and summing around \(\mathbb Z_r\) gives

\[
                       \sum_j\varepsilon_j=-1\pmod3.     \tag{2.7}
\]

Thus every orbitwise selector has a phase slip.  If several provider types
are used, either their type changes somewhere or the same monodromy
argument applies.  Hence there is at least one provider/phase break for
each of the \(2\kappa\) shortened full colour orbits.  This is an
orbit-labelled break count; several breaks may occur at one physical seam.

## 3. Complement-paired phase words through the full \(3\)-primary tower

The \(v_3(q)=1\) construction in the period-three theorem uses the Chinese
remainder product \(G\cong\mathbb Z_{2a+1}\times\mathbb Z_3\).  The product
is not needed.

### Theorem 3.1 (all-depth paired exceptional filter bank)

Assume \(a\ge1\).  For every \(v_3(q)\), and independently for every
shortened Catalan necklace, choose an arbitrary phase word of length
\(r=s/3\).  There is an \(H\)-equivariant set \(P_{\rm exc}\) of Johnson
edges with all the following properties.

1. Every shortened lower colour and every shortened upper colour occurs
   exactly once.
2. All nonshortened opposite colours of these edges are separately
   distinct.  Thus \(P_{\rm exc}\) is a partial matching in the
   lower--upper diamond graph.
3. All middle endpoints of all selected Johnson edges are distinct.
4. The upper-filter bank is the setwise complement of the lower-filter
   bank.
5. Exactly \(2\kappa\) full-\(G\) edge orbits are partial.  In each one,
   \(r\) of its \(s\) \(H\)-edge orbits are selected.

#### Construction

Put \(Q=G/J\cong\mathbb Z_{2a+1}\).  From every translation orbit in
\(\binom Qa\), choose one representative \(A\), put \(B=Q\setminus A\),
and choose distinct \(b,c\in B\).  Choose lifts

\[
                         x\in\pi^{-1}(b),\qquad
                         y\in\pi^{-1}(c).
\]

Define

\[
\begin{aligned}
 L_A&=\{\infty\}\cup\pi^{-1}(A),\\
 U_B&=\pi^{-1}(B),\\
 e_A^-&=\{L_A\cup\{x\},L_A\cup\{y\}\},\\
 e_A^+&=\{U_B\setminus\{x\},U_B\setminus\{y\}\}.
\end{aligned}                                            \tag{3.1}
\]

The edges \(e_A^+\) and \(e_A^-\) are setwise complements.

Let \(\Gamma\subset G\) be a transversal of \(G/HJ\); thus
\(|\Gamma|=r\).  A phase word is a choice \(\theta_A(\gamma)\in J\) for
every \(\gamma\in\Gamma\).  Select the \(H\)-orbits

\[
 H\bigl(\gamma+\theta_A(\gamma)\bigr)e_A^-,
 \qquad
 H\bigl(\gamma+\theta_A(\gamma)\bigr)e_A^+
 \quad(\gamma\in\Gamma),                                \tag{3.2}
\]

for every necklace representative \(A\).

#### Proof

Translation by \(J\) fixes \(L_A\) and \(U_B\), but changes the phases of
the two distinguished points.  Since \(\Gamma\) represents \(G/HJ\), the
first family in (3.2), developed by \(H\), covers every translation of
\(L_A\) exactly once.  The complementary family does the same for \(U_B\).
Varying the \(\kappa\) primitive necklace representatives covers both
shortened banks.

The free upper colour of \(e_A^-\) is

\[
             L_A\cup\{x,y\}.                             \tag{3.3}
\]

It has exactly the \(a\) full \(J\)-cosets \(A\), together with two
distinguished points in two different outside cosets.  Thus it recovers the
translated decorated necklace and the unordered distinguished pair
\(\{x,y\}\).  Freeness of the necklace translation action then separates
the quotient translate, while the literal points separate the \(J\)-phase.
Its translates are all distinct, including across different necklaces and
phase-word positions.  The free lower colour of \(e_A^+\) is its complement,
so those colours are distinct as well.

An endpoint of \(e_A^-\) contains \(\infty\), has the \(a\) full cosets
\(A\), and one distinguished outside point.  It therefore recovers its
necklace, translate, phase and choice of \(x\) or \(y\).  All lower-filter
middle endpoints are distinct.  The upper-filter endpoints are their
distinct complements and avoid \(\infty\), proving Item 3.

For fixed \(A\), both banks lie in one full-\(G\) edge orbit apiece.
Equation (3.2) chooses exactly one of the three \(H\)-edge orbits over
each shortened \(H\)-colour orbit, hence \(r\) of \(s\).  Different
necklaces and the two shores give distinct full edge orbits. \(\square\)

For \(a=0\), use the direct \(m=2\) filter pair in Section 6.  Theorem 3.1
is local-sharpness of the exceptional bank.  If \(3\nmid\kappa\), Theorem
2.1 proves that every complete transversal extending it must break at
least one additional free/free orbit.

## 4. Global-first existence and the optional fixed-bank Hall face

Let \(B_m\) be the bipartite Boolean-diamond graph on
\({\cal L}\sqcup{\cal U}\), with \(L\sim U\) when \(L\subset U\).  Its
degree is

\[
                         D=\binom{m+1}{2}.               \tag{4.1}
\]

The action of \(H\) is free on its vertices and edges.  Write
\(\bar B_m=B_m/H\).

### Lemma 4.1 (unrestricted filter-only existence)

The quotient \(\bar B_m\) is a \(D\)-regular balanced bipartite
multigraph.  Consequently it has a perfect matching, and its lift is an
\(H\)-equivariant exact common outer-colour transversal containing every
shortened row.

#### Proof

Fix a physical representative \(L\).  Two different incident physical
edges at \(L\) cannot lie in one \(H\)-edge orbit: an element identifying
them would fix \(L\), contrary to shore freeness.  Thus the quotient degree
is still \(D\), on both shores.  For any left quotient set \(X\),
edge-counting gives \(D|X|\le D|N(X)|\), so Hall applies.  Lifting a
quotient perfect matching is exact by \(H\)-freeness. \(\square\)

This is the main existential palette theorem: choose the global quotient
matching first and take its restriction to the exceptional banks.  That
restriction is extendable by construction.  It also has distinct opposite
colours and pairwise-distinct middle endpoints by the coset-symmetric-
difference argument in
`MATH_THEOREM_CATALAN_FILTERS_FROM_GLOBAL_QUOTIENT_MATCHING_20260731.md`.

The next theorem is needed only if one insists on the separately prescribed
antipodal bank \(P_{\rm exc}\) from Theorem 3.1.  It is not the remaining
existential gate.

### Theorem 4.2 (prescribed phase-bank Hall equivalence)

Fix all necklace choices, \(b,c\), and phase words in Theorem 3.1.  Let
\(\bar P_{\rm exc}\) be the resulting quotient partial matching, and let
\(R_L,R_U\) be its used lower and upper vertices.  The following are
equivalent.

1. \(\bar P_{\rm exc}\) extends to a perfect matching of \(\bar B_m\).
2. The residual graph

   \[
        \bar B_m[({\cal L}/H)\setminus R_L,\,
                 ({\cal U}/H)\setminus R_U]              \tag{4.2}
   \]

   has a perfect matching.
3. For every
   \(X\subseteq({\cal L}/H)\setminus R_L\),

   \[
        |N_{\bar B_m}(X)\setminus R_U|\ge |X|.            \tag{4.3}
   \]

#### Proof

The prescribed edges already match \(R_L\) bijectively to \(R_U\).
Every further edge must lie in (4.2), and a perfect matching there supplies
all remaining vertices.  This proves \(1\Longleftrightarrow2\); Hall gives
\(2\Longleftrightarrow3\). \(\square\)

For that optional fixed-bank face, (4.3) is an exact separation oracle on
the phase words.
With \(R_L\) fixed, repairing a failed \(X\) requires releasing at least one
currently prescribed upper vertex of \(N_{\bar B_m}(X)\cap R_U\).  If both
shores' phase choices may change, the exact no-good is the disjunction that
either some vertex of the present \(X\) becomes prescribed on the lower
shore, or some presently prescribed upper neighbour is released.  Separate
Hall checks on the shortened shores do not imply (4.3).

## 5. The exact physical forest and unit-voltage completion theorem

An outer-colour perfect matching is a set of Boolean diamonds.  Its unique
Johnson lift need not be a path forest.  The next theorem states the whole
remaining carrier gate without imposing residual symmetry on the compiler.

Let \({\cal A}\) be an occurrence-labelled \(H\)-orbit catalogue.  Every
atom records:

* its lower and upper quotient colours;
* its physical middle-edge orbit and gain;
* every directed-repair host, omitted-facet, orientation, and collar
  resource it consumes; and
* its legal endpoint connector options.

Let \(x_a\in\{0,1\}\) select forest atoms and let \(y_c\in\{0,1\}\)
select occurrence-labelled connector orbits.  For every literal resource
row \(\rho\), fix coefficients \(w_{\rho a},w_{\rho c}\), a right side
\(b_\rho\), and its required relation
\(\bowtie_\rho\in\{=,\le,\ge\}\).  These are occurrence equations, not
marginal orbit counts.

### Theorem 5.1 (coupled quotient sector-braid equivalence)

The catalogue has an \(H\)-equivariant exact directed-repair path forest
with all shortened filters, together with a connected physical closure, if
and only if there are forest variables \(x\) and closure variables \(y\)
satisfying all conditions below.

1. Every directed host/token/orientation/collar row satisfies

   \[
     \sum_a w_{\rho a}x_a+
     \sum_c w_{\rho c}y_c\ \bowtie_\rho\ b_\rho.        \tag{5.0}
   \]
2. Every lower and upper quotient-colour row has load one.  On shortened
   rows this is exactly (2.1).
3. Forest and connector alternatives jointly satisfy every physical
   occurrence at-most-one row.
4. Every quotient middle vertex has selected forest degree at most two.
   With the recorded atom orientations, selected forest indegree and
   outdegree are each at most one.
5. For every nonempty quotient middle-vertex set \(W\),

   \[
       \sum_{a:\,\bar e(a)\subseteq W}x_a\le |W|-1.       \tag{5.1}
   \]

6. Give every selected path an ordered negative and positive endpoint stub
   (two stubs at the same vertex for a trivial path).  The selected
   connector orbits are pairwise physically distinct and disjoint from the
   forest, touch no internal path vertex, consume every positive stub once
   as a tail and every negative stub once as a head, and obey every proper
   directed subtour cut.  Thus path contraction gives one directed cycle.
7. If the oriented quotient paths have gains \(r_i\) and their following
   connectors have gains \(\delta_i\), the total gauge-invariant voltage

   \[
                            v=\sum_i(r_i+\delta_i)\in H
   \]

   generates \(H\).  After identifying \(H\cong\mathbb Z_h\), this is
   equivalent to

   \[
                             \gcd(v,h)=1.                 \tag{5.2}
   \]

#### Proof

Necessity is literal.  The outer rows give an exact common transversal,
and the resource rows make it a directed-repair selection in the given
catalogue.  A physical path forest has degree at most two and is graphic,
giving (5.1).  Contracting its components gives the stated one-cycle
conditions.  Connected lift forces its closed voltage to generate \(H\).

Conversely, the colour equations select exactly \(N/h\) quotient middle
edges.  The quotient has \(M/h\) middle vertices, where

\[
                     M/h-N/h=K/h .
\]

Conditions 4 and 5 therefore make the selected graph a spanning linear
forest with exactly \(K/h\) path components, including possible trivial
paths.  Every quotient tree gauges to voltage zero and lifts to \(h\)
disjoint physical paths, so the physical lift has exactly \(K\) paths.
The explicit endpoint rows in Condition 6 join the quotient paths into one
directed quotient cycle without reusing a physical occurrence.
Condition 7 makes its lift connected.  The restored physical graph is
connected and two-regular, hence one Hamilton cycle, with every literal
resource and outer palette exact. \(\square\)

Here outer-palette exactness belongs to the distinguished forest selected
by \(x\).  Connector edges selected by \(y\) may repeat those colours; they
are topology resources, not additional members of the common transversal.

The \(S\)-phase slips and \(H\)-voltage lie in different Chinese-remainder
coordinates:

\[
                       G\cong H\times S.                  \tag{5.3}
\]

Changing one of the three phases inside a fixed provider orbit has zero
direct \(H\)-coordinate for a fixed topology and gain record.  It can still
change which endpoints and closure voltages are admissible.  Conversely,
the forced multiplicities \(r=s/3\) are units modulo \(h\), so the scalar
multiplicity congruence alone imposes no divisor on \(v\).
The exact voltage gate is therefore

\[
   \operatorname{Gen}(H):=\{v\in H:\langle v\rangle=H\},
\]

and

\[
   \{v:\ v\text{ occurs in an admissible one-cycle closure}\}
       \cap\operatorname{Gen}(H)\ne\varnothing,           \tag{5.4}
\]

not a consequence of filter Hall.

## 6. Two sharp obstructions to collapsing the gates

### 6.1 Marginal filter Hall does not imply directed-resource matching

On three shores \(\{0,1\}\), take the four atoms

\[
 (0,0,0),\quad(0,1,1),\quad(1,0,1),\quad(1,1,0).         \tag{6.1}
\]

Every vertex has degree two, every pair projection is \(K_{2,2}\), and
weight \(1/2\) on each atom is a fractional perfect matching.  There is no
integral perfect matching: a second atom disjoint from the first would be
its bitwise complement, which has odd parity and is absent.  Thus the
three-shore resource rows in Theorem 5.1 cannot be replaced by separate
pairwise Hall conditions.

### 6.2 The sharp \(m=2\) filter pair cannot be a physical forest

Let

\[
 \Omega=\{\infty,0,1,2\},\qquad m=2 .
\]

Up to rotation, the sharp complementary exceptional pair is

\[
\begin{aligned}
 e^-&=\{\infty0,\infty1\},
 &(\ell,u)&=(\infty,\infty01),\\
 e^+&=\{12,02\},
 &(\ell,u)&=(2,012).
\end{aligned}                                           \tag{6.2}
\]

The only unused lower colours are \(0,1\), and the only unused upper
colours are \(\infty02,\infty12\).  Hence the unique colour-perfect
extension adds

\[
 \{\infty0,02\},\qquad \{\infty1,12\}.                  \tag{6.3}
\]

The four lifted Johnson edges form the cycle

\[
 \infty0-\infty1-12-02-\infty0,                         \tag{6.4}
\]

while the middle vertices \(\infty2\) and \(01\) are isolated.  Thus
(5.1) fails on those four cycle vertices.  The fixed sharp filter bank is
colour-extendible but not physical-forest-extendible at \(m=2\).

This is only a fixed-bank obstruction, not a global \(m=2\) obstruction.
For example the global-first diamonds can lift to the two spanning paths

\[
 \infty0-\infty1-12,
 \qquad
 01-02-\infty2,
\]

which close by \(12-01\) and \(\infty2-\infty0\) to a Hamilton six-cycle.
The fixed example proves only that exact exceptional filters plus residual
colour Hall do not force the physical sector braid.

## 7. Reconciliation with the K16 optimum

At \(m=8\),

\[
 (q,h,s,a,\kappa,r)=(15,5,3,2,2,1).
\]

The orbit ledger forces four shortened filter rows and the global
congruence forces at least five partial full-rotation edge orbits in any
\(H\)-equivariant distinguished exact common transversal.  This is an
orbit theorem, not a
claim about the changed edges of the authenticated optimum.

The exact K16 anatomy in
'MATH_THEOREM_K16_THREE_PRIMARY_SPIRAL_BRAID_ANATOMY_20260731.md'
shows:

* the carrier consists of four co-oriented strict \(\mathbb Z_{15}\)
  spirals of base lengths \(426,426,3,3\);
* all three residual sectors are interlaced inside every spiral;
* the four deficient carrier edge orbits do not correspond one-for-one to
  the four shortened outer-colour orbits;
* among the changed outer colours only one lower colour is shortened and
  no upper colour is shortened; and
* the final common-cap compiler is strongly non-\(H\)-invariant.

If applied to K16, Theorems 3.1--5.1 would concern a separately selected
distinguished common-transversal forest inside a carrier, not the visible
connector defect list.  The authenticated anatomy does not certify such an
\(H\)-equivariant forest or a unit-voltage quotient closure: its fourth wrap
is not a Johnson edge, and the optimum is a three-seam Hamilton path.  It
does prove that a general construction may use symmetry to organize its
carrier and then spend that symmetry in an asymmetric integral compiler.
Requiring the final word or compiler to remain \(H\)-equivariant would
exclude the known optimum.

## 8. Smallest remaining lemma after the global-first rebase

For every \(m\), choose a quotient perfect matching \(\bar F\) of the
complete clean-\(H\) diamond graph such that its Johnson lift obeys the
middle degree and graphic rows and the directed occurrence rows in
Theorem 5.1.  Then choose private endpoint connectors satisfying the stub,
subtour, and generator-voltage conditions of Items 6--7.

The prescribed Hall test (4.3) is only the optional face obtained by
insisting on the antipodal bank of Theorem 3.1.  It is not part of the
minimal global-first hypothesis.  The P4/native-socket packet bank in
`MATH_THEOREM_CATALAN_PERIOD3_FILTER_PACKET_AND_NEUTRAL_CONNECTOR_20260731.md`
is another stronger sufficient face, not an equivalent normal form.

The newer exact reductions sharpen the forest part further.  A global
matching with a linear lift is exactly an acyclic ordered four-transversal,
and its natural matching/cap-two/graphic LP is fractionally feasible.  The
first proved missing correlation cuts and positive rounding criteria are in
`MATH_THEOREM_A_CATALAN_ORDERED_FOUR_TRANSVERSAL_ODD_CIRCUIT_ROUNDING_20260731.md`.
Thus the unresolved input is integral correlation inside the global
matching space, followed by the endpoint-voltage closure—not marginal
palette Hall.

An asymmetric common-cap compiler is a subsequent gate on the fixed final
chronology and must not be folded into \(H\)-equivariance.
