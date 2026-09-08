# Cyclic quotient port voltage, three-primary filters and interlaced spirals

Date: 2026-07-31  
Lane: R, Hamilton-compatible port matching  
Status: unconditional free-cyclic transition theorem, exact clean-\(H\)
sector and paired-filter criteria, unconditional global quotient-matching
and physical block-splice theorems, and exact applications to the
authenticated \(m=4\) and K16 fixtures.  In the Catalan specialization the
cyclic order is the clean order
\(h=(2m-1)/3^{v_3(2m-1)}\), not necessarily \(2m-1\).  The filter-extension
Hall gate is closed by choosing the global quotient matching first.  No
all-\(m\) forest-admissible matching or protected private-socket closure
theorem is claimed.  Protected shadows, residence and the common-cap
compiler remain literal additional hypotheses.

## 0. Verdict

Inside a free cyclically equivariant fixed-fragment fibre, quotienting does
collapse the complete physical balanced-fragment subtour family to two
conditions:

\[
 \boxed{\text{one quotient transition cycle}
 \quad\hbox{and}\quad
 \gcd(n,V)=1,}                                        \tag{0.1}
\]

where \(V\) is the total voltage of that quotient cycle in
\(\mathbb Z_n\).

More generally, if the quotient transition permutation has cycles \(C\)
with voltages \(V_C\), then the exact number of physical factor components
is

\[
                         \sum_C\gcd(n,V_C).            \tag{0.2}
\]

Thus (0.1) accounts for every physical subtour, including subtours which
are not unions of full group orbits.

The hypotheses are essential.  The cyclic action must be free on
occurrence-labelled fragment and port states, the selected port matching
must be invariant, and the quotient records must give a genuine
one-in/one-out transition system.  Stabilizers, coarsened repeated
occurrences or a noninvariant matching invalidate the simple gcd formula.

For a Catalan problem put

\[
 q=2m-1,\qquad s=3^{v_3(q)},\qquad h=q/s,\qquad
 H=\langle s\rangle\cong\mathbb Z_h.                 \tag{0.3}
\]

MATH_THEOREM_CATALAN_THREE_PRIMARY_QUOTIENT_REDUCTION_20260731.md
proves that \(H\) is the maximal uniformly available clean rotation group:
it acts freely on all three relevant ranks and \(h\mid\operatorname{Cat}_m\).
When \(3\mid q\), full \(\mathbb Z_q\)-invariant exact lower rainbowness is
impossible because the outer layers have short orbits.  For the maximal
clean Catalan specialization of (0.1), therefore, take \(n=h\); smaller
subgroups of \(H\) remain possible but give less compression.  If an
explicit residual-template partition into \(s\) sectors has been supplied,
one unit-voltage quotient cycle must pass through all of its
occurrence-labelled sector states.  Separate unit-voltage cycles in those
\(s\) sectors give exactly \(s\) physical components.  Such a sector
partition is extra structure; it does not follow from mere
\(H\)-invariance of an arbitrary selected forest.

For the frozen \(m=4\) fixture there are two compatible quotient views.

1. The fourteen retained paths form two free \(\mathbb Z_7\)-orbits.
   Their canonical closure quotients to a two-state cycle of voltage
   \(2\pmod7\), so it lifts to one fourteen-fragment cycle.
2. The underlying 56-state seam cycle quotients to an eight-state cycle of
   the same voltage.  The forced repair orbit and either of the two kernel
   orbits equivariantly subdivide two quotient arcs, producing a ten-state
   quotient cycle.  Both choices still have voltage \(2\pmod7\), and hence
   both lift to one physical 70-state Hamilton cycle.

Consequently the binary kernel choice in
MATH_THEOREM_CATALAN_M4_Z7_QUOTIENT_REPAIR_CORE_20260731.md is
**connectivity-neutral**.  It is not a binary voltage tuner: both choices
subdivide an already unit-voltage cycle without changing its monodromy.

The repair-core quotient alone does not prove this.  It is a three-shore
matching object with two disconnected quotient tokens and has no physical
Hamilton voltage until its triples are embedded into the actual
fragment/seam transition system.

The authenticated K16 carrier exhibits the complementary architecture.
Four closed strict \(\mathbb Z_{15}\)-spirals each have clean
\(\mathbb Z_5\)-voltage \(4\), but every spiral already interlaces all three
residual sectors.  Four phase-specific openings and three singleton Johnson
seams then form a physical Hamilton path; they destroy \(H\)-equivariance,
and the missing fourth wrap is non-Johnson.  Thus voltage certifies the
closed blocks, while physical palette-safe splicing certifies the final
linear chronology.

## 1. Free cyclic voltage covers

Let

\[
                         \Gamma=\mathbb Z_n=\langle\rho\rangle.   \tag{1.1}
\]

Assume \(\Gamma\) acts freely on occurrence-labelled marked and unmarked
ports, on their retained fragments and on admissible seam occurrences.
Assume it preserves:

1. the two port shores;
2. the fixed fragment pairing \(P\);
3. the Boolean containment graph \(G\); and
4. all selected guard labels.

Let \(M\) be a \(\Gamma\)-invariant perfect matching of \(G\), and put

\[
                              F=P\cup M.               \tag{1.2}
\]

The graph \(F\) is a physical degree-two factor.  Its quotient

\[
                              \overline F=F/\Gamma     \tag{1.3}
\]

is a two-regular occurrence multigraph.  Loops and parallel quotient edges
are retained.

Choose one physical representative \(\widetilde v\) of every quotient
vertex \(\bar v\).  For an oriented quotient edge
\(\bar e:\bar u\to\bar v\), define its voltage
\(\delta(\bar e)\in\mathbb Z_n\) by requiring the lifted edge from
\(\widetilde u\) to end at

\[
                         \rho^{\delta(\bar e)}\widetilde v.       \tag{1.4}
\]

Changing representatives by
\(\widetilde v\mapsto\rho^{r_v}\widetilde v\) changes

\[
              \delta(\bar e)\mapsto
              \delta(\bar e)+r_u-r_v.                \tag{1.5}
\]

Hence the sum of edge voltages around a closed quotient walk is gauge
invariant, up to sign when its orientation is reversed.

## 2. Exact component formula

### Theorem 2.1 (free cyclic port-lift theorem)

Write the quotient factor as the disjoint union of cycles

\[
                     \overline F=C_1\sqcup\cdots\sqcup C_\ell.  \tag{2.1}
\]

For an orientation of \(C_i\), put

\[
                         V_i=\sum_{\bar e\in C_i}\delta(\bar e)
                         \pmod n.                    \tag{2.2}
\]

Then the physical lift of \(C_i\) has exactly

\[
                         \gcd(n,V_i)                  \tag{2.3}
\]

components, each of quotient-cover length

\[
                    |C_i|\,\frac{n}{\gcd(n,V_i)}.     \tag{2.4}
\]

Here \(\gcd(n,0)=n\).  Consequently

\[
                         c(F)=\sum_{i=1}^\ell\gcd(n,V_i).         \tag{2.5}
\]

In particular,

\[
 F\text{ is one physical cycle}
 \quad\Longleftrightarrow\quad
 \ell=1\text{ and }\gcd(n,V_1)=1.                     \tag{2.6}
\]

#### Proof

Choose a starting phase \(g\in\mathbb Z_n\) over one vertex of \(C_i\).
One traversal of the quotient cycle returns to the same quotient vertex in
phase

\[
                              g+V_i.                  \tag{2.7}
\]

The physical lifts of \(C_i\) are therefore indexed by the orbits of the
translation \(g\mapsto g+V_i\).  Those orbits are the cosets of the cyclic
subgroup \(\langle V_i\rangle\).  Their number is \(\gcd(n,V_i)\), and
their common size is \(n/\gcd(n,V_i)\).  Multiplying by the quotient-cycle
length gives (2.4).  Summing over the disjoint quotient cycles gives (2.5)
and (2.6). \(\square\)

For prime \(n=p\), the voltage condition in (2.6) is simply

\[
                              V_1\ne0\pmod p.          \tag{2.8}
\]

For composite \(n\), nonzero voltage is not sufficient.

## 3. Collapse of the balanced-fragment subtour family

Recall the exact physical subtour characterization from
MATH_THEOREM_R_CATALAN_PORT_HAMILTON_MATCHING_AND_PROTECTED_EAR_ROUTER_20260731.md:
a port perfect matching is connected if and only if every proper balanced
fragment-block cut contains at least two selected seams.

### Corollary 3.1 (exact quotient compression)

Under the hypotheses of Section 1, the complete physical balanced-block
subtour family holds if and only if (0.1) holds.

#### Proof

If the quotient has several cycles, their physical lifts are disjoint
factor components.  If it has one cycle with voltage \(V\), Theorem 2.1
gives \(\gcd(n,V)\) physical components.  Every physical factor component
contains equally many marked and unmarked fragments, so each proper
component union gives a zero balanced-block cut.

Conversely, a zero balanced-block cut is a union of physical components.
Thus absence of all such cuts is exactly physical connectedness, which is
(0.1) by Theorem 2.1. \(\square\)

The reduction is not merely a test of invariant subtours.  When \(V\) is
nonprimitive, the individual cosets of \(\langle V\rangle\) are generally
noninvariant under the whole group, but they are exactly the missing
physical subtour witnesses.

## 4. Transition-system form

The theorem can be stated without first constructing the full physical
matching.

Let \({\cal S}\) index oriented marked-fragment orbits.  A selected quotient
record

\[
                         (x,y,z;a,b)                  \tag{4.1}
\]

means that, for every phase \(g\),

\[
 A_{x,g}\longrightarrow B_{y,g+a}
             \longrightarrow A_{z,g+a+b}.            \tag{4.2}
\]

The first arrow is a marked-exit to unmarked-entry seam, and the second is
the unmarked-exit to next-marked-entry seam.  Assume the selected records
use every marked source orbit, every unmarked orbit and every marked target
orbit once.  Then

\[
                         \theta(x)=z                  \tag{4.3}
\]

is a permutation of \({\cal S}\), and the combined transition voltage is

\[
                         \Delta_x=a+b\pmod n.         \tag{4.4}
\]

Here the entry and exit representatives on each retained fragment are gauged
so that fixed fragment traversal has voltage zero.  With another gauge, its
two fragment-traversal voltages must be added to \(a+b\); all closed-cycle
voltage sums are unchanged.

For every cycle \(C\) of \(\theta\), put

\[
                         V_C=\sum_{x\in C}\Delta_x.   \tag{4.5}
\]

### Theorem 4.1 (cyclic saturating transition system)

Under free occurrence-labelled equivariance, assume additionally that the
development is injective on selected physical seam occurrences, selected
seams are disjoint from retained internal edges, and the development has
physical degree two at every middle vertex.  Then the physical factor
developed from (4.1) has

\[
                         \sum_{C\in{\cal C}(\theta)}
                                  \gcd(n,V_C)          \tag{4.6}
\]

components.  It is one cycle if and only if \(\theta\) is one cycle and
its voltage (4.5) is coprime to \(n\).

#### Proof

The saturation hypotheses make (4.2) a perfect port matching after
development.  Combining the two seams and the two fixed fragment traversals
gives the map

\[
                         (x,g)\longmapsto
                         (\theta(x),g+\Delta_x).       \tag{4.7}
\]

Apply Theorem 2.1 to every permutation cycle of \(\theta\). \(\square\)

### Theorem 4.2 (protected cyclic transition-system theorem)

In addition to Theorem 4.1, assume:

1. every developed seam in (4.2) is a literal simple Boolean-containment
   edge, the developed seam occurrences are pairwise physically distinct,
   and none duplicates a retained internal edge;
2. the endpoint-complement conditions EC1--EC3 hold occurrencewise,
   including pairwise-distinct marked lower colours;
3. each unmarked endpoint occurrence is used once, retaining its prescribed
   immediate-upper colour;
4. every selected deeper witness either avoids every changed seam or has an
   explicitly supplied literal replacement in the final developed order;
5. the exact product of all developed fragment and seam residence states is
   accepting, including physical cyclic closure; and
6. the opening and common-cap compiler, if required, are verified on that
   same physical chronology.

If \(\theta\) is one cycle and its voltage is coprime to \(n\), the
developed object is one literal protected physical cycle.  It has the exact
lower-q1 palette, the fixed complete immediate-upper multiplicity vector,
and precisely the deeper-shadow and residence guarantees supplied in
items 4--5.

#### Proof

Theorem 4.1 gives one physical cycle.  EC1--EC3 and port saturation give
the exact lower palette.  At an unmarked occurrence \(b\), every cross seam
has upper colour \(z+U(b)\); using each occurrence once fixes the entire
immediate-upper multiset.  Items 4--6 are literal guard and compiler
hypotheses and therefore survive development. \(\square\)

This theorem gives a direct cut-selection target: construct one safe
saturating quotient transition system whose transition permutation is
cyclic and whose total voltage is a unit.

## 5. Quotient splices and binary voltage choices

### Proposition 5.1 (component-transversal orbit splice)

Let \(C_1,\ldots,C_r\) be all cycles of a protected quotient transition
system.  Delete one closing edge \(e_i\) of voltage
\(\epsilon_i\) from each \(C_i\).  The remaining directed quotient path has
voltage

\[
                              R_i=V_i-\epsilon_i.      \tag{5.1}
\]

Suppose protected compatible quotient seams \(f_i\) of voltage \(\beta_i\)
connect the terminal port of the opened \(C_i\) to the initial port of
\(C_{i+1}\), cyclically.  Replacing all \(e_i\) by all \(f_i\) gives one
quotient cycle of voltage

\[
                V_{\rm new}
                 =\sum_i R_i+\sum_i\beta_i
                 =\sum_iV_i+\sum_i(\beta_i-\epsilon_i).           \tag{5.2}
\]

Its physical lift is Hamiltonian exactly when

\[
                              \gcd(n,V_{\rm new})=1.   \tag{5.3}
\]

#### Proof

Deleting one edge opens each quotient cycle into a path.  The new seams
concatenate those paths into one quotient cycle.  Voltage is additive along
the concatenation, giving (5.2), and Theorem 2.1 gives (5.3). \(\square\)

If only a proper subfamily of quotient cycles is opened, the same formula
describes the newly merged component, but untouched quotient cycles remain;
no whole-factor Hamilton conclusion then follows.

In the Boolean rank-gap-one port graph, every new seam from an unmarked
endpoint owner \(U_i\) to a marked label \(L_{i+1}\) additionally requires

\[
                              L_{i+1}\subset U_i.       \tag{5.4}
\]

Together with the old \(L_i\subset U_i\), distinct labels force
\(U_i=L_i\cup L_{i+1}\).  Thus a quotient splice is a literal
voltage-labelled Johnson necklace.

### Corollary 5.2 (prime binary tuner)

Let \(n=p\) be prime.  Suppose two protected invariant choices both give
one quotient cycle and have distinct voltages \(V_0\ne V_1\).  At least one
choice has a physical Hamilton lift.

#### Proof

At most one of two distinct residues modulo \(p\) is zero, and every nonzero
residue is a unit. \(\square\)

For composite \(n\), distinct voltages do not suffice: \(2\) and \(3\)
modulo \(6\) are distinct and both are nonunits.

### Lemma 5.3 (equivariant subdivision invariance)

Replace one quotient edge of voltage \(\delta\) by a directed two-edge path
of voltages \(\delta_1,\delta_2\), where

\[
                              \delta_1+\delta_2=\delta.             \tag{5.5}
\]

This equivariant subdivision changes neither quotient component count nor
total cycle voltage, and hence changes no physical component count.

#### Proof

The quotient cycle is only subdivided, and its voltage sum replaces one
summand by two summands with the same total.  Apply Theorem 2.1. \(\square\)

## 6. The canonical m=4 path quotient

Identify

\[
                         [8]=\mathbb Z_7\sqcup\{\infty\},          \tag{6.1}
\]

and let \(\rho\) add one on \(\mathbb Z_7\) while fixing \(\infty\).
The fourteen oriented retained paths in the canonical certificate form two
free path orbits.  With phases \(g=0,\ldots,6\), their frozen path indices
are

\[
\begin{aligned}
 S_g&=(0,2,5,13,11,9,6)_g,\\
 L_g&=(1,4,12,10,8,3,7)_g.                           \tag{6.2}
\end{aligned}
\]

The letters \(S,L\) refer to the length-three and length-seven path orbits.
Rotation preserves the recorded path orientations.

The canonical path cycle is

\[
\begin{split}
 S_0,L_0,S_2,L_2,S_4,L_4,S_6,L_6,\\
 S_1,L_1,S_3,L_3,S_5,L_5,S_0.                       \tag{6.3}
\end{split}
\]

Equivalently its quotient transitions are

\[
                         S_g\longmapsto L_g,\qquad
                         L_g\longmapsto S_{g+2}.       \tag{6.4}
\]

The quotient is one two-state cycle and its voltage is

\[
                              0+2=2\pmod7.             \tag{6.5}
\]

Since \(\gcd(7,2)=1\), Theorem 4.1 proves that (6.3) is one physical
fourteen-fragment cycle.  Expanding the paths gives all seventy rank-four
middle states once.

The second rooted closure in the census is also equivariant, with

\[
                         S_g\longmapsto L_{g-1},\qquad
                         L_g\longmapsto S_{g+2};       \tag{6.6}
\]

its voltage is \(-1+2=1\pmod7\).  This second closure is not the alternate
kernel matching \({\cal E}\sqcup{\cal K}_1\) inside the canonical repair
core.

## 7. Expanded seam quotient and the two kernel choices

Use the gauge in which a mask \(x\) is written
\(\rho^g\bar x\) relative to the displayed representative.  The canonical
56-state seam cycle has eight free state orbits and quotient order

\[
 135\longrightarrow15\longrightarrow23\longrightarrow43
 \longrightarrow27\longrightarrow147\longrightarrow141
 \longrightarrow139\longrightarrow135.              \tag{7.1}
\]

The representatives encode

\[
\begin{array}{c|c}
135&\{0,1,2,\infty\}\\
15&\{0,1,2,3\}\\
23&\{0,1,2,4\}\\
43&\{0,1,3,5\}\\
27&\{0,1,3,4\}\\
147&\{0,1,4,\infty\}\\
141&\{0,2,3,\infty\}\\
139&\{0,1,3,\infty\}.
\end{array}                                           \tag{7.2}
\]

The edge-voltage vector along (7.1) is

\[
                         (6,0,1,4,0,4,2,6),           \tag{7.3}
\]

whose sum is

\[
                              23\equiv2\pmod7.         \tag{7.4}
\]

The forced orbit \({\cal E}\) inserts the state orbit represented by
\(29=\{0,2,3,4\}\) into the quotient edge \(15\to23\), splitting its
voltage \(0\) as \(0+0\).

For the two residual kernel matchings, the expanded quotient cycles are:

\[
\begin{array}{c|l|l}
\text{choice}&\text{quotient state order}&\text{edge voltages}\\ \hline
{\cal E}\sqcup{\cal K}_0&
135,15,29,23,43,27,147,141,139,149&
(6,0,0,1,4,0,4,2,6,0)\\
{\cal E}\sqcup{\cal K}_1&
135,15,29,23,43,27,147,141,149,139&
(6,0,0,1,4,0,4,3,6,6).
\end{array}                                           \tag{7.5}
\]

Both rows close back to \(135\).  In the first row the orbit represented by
\(149=\{0,2,4,\infty\}\) subdivides \(139\to135\).  In the second it
subdivides \(141\to139\).  Direct summation gives

\[
                         V({\cal E}\sqcup{\cal K}_0)
                         =V({\cal E}\sqcup{\cal K}_1)
                         =2\pmod7.                    \tag{7.6}
\]

Thus both choices satisfy the one-cycle and primitive-voltage conditions.
Each quotient cycle has ten free state orbits, so each lift is one physical
cycle of length

\[
                              10\cdot7=70.             \tag{7.7}
\]

The repair-core matching theorem supplies every omitted, base and outgoing
colour once for either choice.  The literal candidate rows also give
distinct incoming colours and retain the audited lower/upper profiles
\(1^{42}2^{14}\).  Therefore both are genuine uniformly-outgoing physical
repairs of the canonical seam transition.

### Corollary 7.1 (kernel connectivity neutrality)

The choice \({\cal K}_0\) versus \({\cal K}_1\) does not change physical
component count in the canonical \(m=4\) fixture.

#### Proof

Equation (7.5) shows that each choice is an equivariant subdivision of the
same quotient seam cycle, and (7.6) gives the same primitive voltage.
Apply Lemma 5.3 and Theorem 2.1. \(\square\)

This conclusion is stronger and more precise than applying the prime binary
tuner: the two voltages are equal, not distinct.

## 8. What the three-orbit core does and does not encode

The complete repair core has the quotient anatomy

\[
 \{\text{one forced edge orbit}\}
 \quad\sqcup\quad
 \{\text{two parallel kernel edge orbits}\}.          \tag{8.1}
\]

This is a quotient of a three-partite matching problem on omitted, base and
outgoing colours.  It proves that exactly two repair matchings exist.  It
does not contain:

1. the retained-fragment involution \(P\);
2. the cyclic order of the seam transition;
3. a source/target orientation for a physical factor; or
4. the accumulated transition voltage.

Accordingly, the step-one and step-three heptagons formed by
\(D\triangle Z\) are palette geometry, not by themselves physical factor
voltages.  Equations (6.3)--(7.6) become available only after the frozen
physical transition data are supplied.

This distinction also prevents a common misidentification.  The census's
second rooted closure has voltage \(1\), but it is not
\({\cal E}\sqcup{\cal K}_1\).  It uses a different seam orbit represented
by \((29,22,21)\), retains the \({\cal K}_0\) choice and has a different
28-edge complete repair core.

## 9. Sharp scope failures

### 9.1 Nonfree actions

Let \(\Gamma=\mathbb Z_6\), let \(H=\langle3\rangle\), and take physical
phases in \(\Gamma/H\).  The transition

\[
                              [g]\longmapsto[g+2]      \tag{9.1}
\]

is one physical three-cycle, although \(\gcd(6,2)=2\).  The correct
transitivity condition is

\[
                              \langle H,2\rangle=\Gamma.           \tag{9.2}
\]

Thus stabilizers must be included; Theorem 2.1 deliberately assumes
freeness.

### 9.2 Coarsened repeated occurrences

Two different quotient occurrence states may carry the same Boolean label.
They must not be identified.  For example, two same-label quotient loops
over \(\mathbb Z_5\), each of voltage one, lift to two physical five-cycles,
not one.  Occurrence splitting is part of the theorem's hypotheses.

### 9.3 Several quotient cycles

Two quotient loops over \(\mathbb Z_5\), each of voltage one, still lift to
two physical cycles.  Their voltages collectively generate the group, but
voltage cannot join distinct quotient components.

### 9.4 Noninvariant selections

If cuts, endpoints or matching edges are chosen phase by phase rather than
as complete \(\Gamma\)-orbits, there is no quotient cover with one voltage
per edge orbit.  The physical port degree and balanced-subtour rows must
then be retained.

### 9.5 Guard projection

Quotient guard rows are exact only when both the selected witness catalogue
and the chosen transition are invariant.  A target with a short orbit or a
phase-specific last witness requires its physical occurrence rows.  Voltage
controls topology only; it does not average away shadow or residence
obligations.

## 10. Three-primary clean-group specialization and sector braid

Retain the notation (0.3).  One phase step in \(\mathbb Z_h\) means
physical rotation by \(s\) finite coordinates.  A voltage originally
written in a full-\(\mathbb Z_q\) gauge must not merely be reduced modulo
\(h\); the \(H\)-orbit representatives and their coset labels must first be
chosen.

### Theorem 10.1 (clean-H transition criterion)

Let \(H\cong\mathbb Z_h\) act freely on the occurrence-labelled Catalan
fragments and ports, and let an \(H\)-invariant saturating degree-two
transition system have quotient occurrence states \({\cal Q}\).  Its
one-in/one-out transition is a permutation \(\tau\) of \({\cal Q}\), and it
has the skew-product form

\[
                         T(x,g)=(\tau(x),g+\delta_x),
                         \qquad x\in{\cal Q},\ g\in\mathbb Z_h.   \tag{10.1}
\]

Then

\[
 c(F)=\sum_{C\in{\cal C}(\tau)}
             \gcd\left(h,\sum_{x\in C}\delta_x\right).            \tag{10.2}
\]

In particular, all physical balanced-fragment subtour rows hold if and only
if \(\tau\) is one occurrence-level cycle and

\[
                         \gcd\left(h,\sum_{x\in{\cal Q}}\delta_x\right)=1.
                                                               \tag{10.3}
\]

When \(h=1\), condition (10.3) is vacuous and all topology lies in the
occurrence-level one-cycle condition.

#### Proof

This is Theorem 4.1 with \(n=h\).  Rank-vertex freeness and the divisibility
needed to form the Catalan quotient are supplied by the three-primary
theorem.  Freeness of the chosen occurrence fragments and ports remains the
explicit hypothesis here; for an invariant path forest it also follows from
Lemma 10.2 below. \(\square\)

### Lemma 10.2 (path-component freeness is automatic)

Let a finite group of odd order act freely on the vertices of an invariant
linear forest.  Then it acts freely on the occurrence-labelled path
components of that forest.  In particular, every component orbit of an
\(H\)-invariant Catalan path forest has size \(h\), so its quotient path
lifts to exactly \(h\) physical paths.

#### Proof

If a group element stabilizes one path component setwise, its restriction
is an automorphism of a finite path.  The automorphism group of a path has
order at most two.  The stabilizer has odd order, so its image in that
automorphism group is trivial.  It therefore fixes every vertex of the
path, and vertex freeness forces the element to be the identity. \(\square\)

The occurrence qualifier is decisive.  The quotient states may retain a
residual label in \(\mathbb Z_q/H\cong\mathbb Z_s\), but an arbitrary merely
\(H\)-invariant forest need not come with a canonical sector template.
Whenever sectors are used below, their partition is an explicit hypothesis,
not a consequence of \(H\)-invariance alone.

### Theorem 10.3 (uniform-sector return-map criterion)

Assume an explicit partition into nonempty parts

\[
                         {\cal Q}=\bigsqcup_{a\in S}{\cal Q}_a             \tag{10.4}
\]

and suppose that the occurrence permutation satisfies

\[
                         \tau({\cal Q}_a)={\cal Q}_{\pi(a)}               \tag{10.5}
\]

for a permutation \(\pi\) of \(S\).  For a cycle
\(A=(a_0,\ldots,a_{d-1})\) of \(\pi\), define its return permutation

\[
                         R_A=\tau^d\big|_{{\cal Q}_{a_0}}.                 \tag{10.6}
\]

For a cycle \(D=(x_0,\ldots,x_{e-1})\) of \(R_A\), put

\[
 V_{A,D}=\sum_{i=0}^{e-1}\sum_{j=0}^{d-1}
                  \delta_{\tau^j(x_i)}\pmod h.                            \tag{10.7}
\]

Then the exact number of physical components is

\[
 c(F)=\sum_{A\in{\cal C}(\pi)}
             \sum_{D\in{\cal C}(R_A)}\gcd(h,V_{A,D}).                    \tag{10.8}
\]

Consequently the physical factor is one cycle if and only if \(\pi\) is one
cycle, its return permutation \(R_A\) is one cycle, and the corresponding
voltage \(V_{A,D}\) is a unit modulo \(h\).

#### Proof

Every cycle \(D\) of \(R_A\) develops into exactly one cycle of \(\tau\):
between successive states of \(D\), traverse the \(d\) sectors in the order
prescribed by \(A\).  This is a bijection between pairs \((A,D)\) and cycles
of \(\tau\), and (10.7) is exactly the voltage of the associated
\(\tau\)-cycle.  Apply (10.2). \(\square\)

The sector permutation alone is therefore not a topology certificate unless
each sector has already been compressed to one macro state.  Condition
(10.5) also forces sector sizes to be equal along every cycle of \(\pi\).

### Theorem 10.4 (protected contiguous-sector braid)

Assume an explicit partition

\[
                         {\cal Q}=\bigsqcup_{a\in\mathbb Z_s}{\cal Q}_a
                                                               \tag{10.9}
\]

of the complete quotient-component set of an \(H\)-invariant spanning path
forest into \(s\) nonempty sectors.  In each sector choose one protected
directed Hamilton path \(R_a\) through all states of \({\cal Q}_a\).  Write
its initial and terminal states as \(\iota_a,\omega_a\), and its
\(H\)-voltage as \(r_a\).

Let \(\pi\) be one \(s\)-cycle on the sector labels.  Suppose that for every
\(a\) there is one literal protected \(H\)-orbit of Boolean containment
seams

\[
                         \omega_a\longrightarrow\iota_{\pi(a)}  \tag{10.10}
\]

of voltage \(b_a\).  Assume that the internal transitions of all \(R_a\),
together with these seam orbits, use every occurrence-labelled port on both
shores exactly once---including every unmarked occurrence fixing the
immediate-upper multiplicity---and preserve the exact lower-colour ledger.
Then the quotient is one cycle of voltage

\[
                              V=\sum_{a\in\mathbb Z_s}(r_a+b_a)
                              \pmod h.                \tag{10.11}
\]

If

\[
                              \gcd(h,V)=1,             \tag{10.12}
\]

its \(H\)-lift is one physical Hamilton cycle.  Under the guard hypotheses
of Theorem 4.2 it is a protected Hamilton-compatible port matching.

#### Proof

The sector paths are disjoint and cover every quotient occurrence.  The
\(s\) bridges (10.10) concatenate them according to the one-cycle
permutation \(\pi\), so the result is one quotient cycle.  Voltage adds
along the concatenation, giving (10.11).  Theorems 10.1 and 4.2 give the
physical and protected conclusions. \(\square\)

For \(s>1\), exactly \(s\) intersector bridges are used in this contiguous
cyclic architecture, the minimum for closing \(s\) nonempty sector paths
into one cycle.  At \(s=1\), (10.10) is the single closing seam.  The scalar
count is not sufficient: the bridges must form one sector permutation, use
occurrence-compatible endpoints and satisfy the common physical palette and
guard ledgers.

### Proposition 10.5 (sector connectivity alone is insufficient)

Let \(s=3\), and put two occurrence states \(a_i,b_i\) in sector \(i\).
Let

\[
             \tau=(a_0\,a_1\,a_2)(b_0\,b_1\,b_2),     \tag{10.13}
\]

giving both quotient cycles unit \(H\)-voltage.  The aggregated sector graph
is a directed three-cycle and is strongly connected, but the physical lift
has at least two components.

#### Proof

The transition permutation has two occurrence-level cycles.  Apply
(10.2). \(\square\)

Outside Theorem 10.4's contiguous-block hypotheses, connectedness of the
aggregated sector graph is insufficient and no sector permutation need
exist; the exact condition is that \(\tau\) itself be one occurrence cycle.
If every transition follows a fixed sector cycle \(\pi\), then Theorem 10.3
says that \(\tau\) is one cycle exactly when the induced \(s\)-step return
permutation on one sector is one cycle.

When \(3\mid q\), Theorem 2 of the three-primary reduction forces symmetry
breaking somewhere in the complete selection.  If the complete
\(H\)-invariant lower-rainbow edge selection---internal paths and bridges
together---were also invariant under the physical residual rotation, it
would be fully \(\mathbb Z_q\)-invariant and hence impossible.  The bridge
subfamily itself may nevertheless be a full residual orbit when the
internal paths or repair choices already break residual symmetry.  For a
general merely \(H\)-invariant forest, the residual action need not preserve
the selected catalogue at all.

### Proposition 10.6 (three-primary provider triples)

Assume \(3\mid q\), and let \({\cal O}\) be a full-rotation orbit of an
outer colour whose stabilizer has order exactly three.  Then \({\cal O}\)
splits into \(s/3\) free \(H\)-orbits.  If \({\cal E}\) is one free
\(\mathbb Z_q\)-orbit of candidate edges whose colour map is onto
\({\cal O}\), then \({\cal E}\) splits into \(s\) free \(H\)-edge orbits,
and exactly three of them lie over each \(H\)-colour orbit in \({\cal O}\).
An \(H\)-invariant exact lower-rainbow selection confined to \({\cal E}\)
must choose one provider from every such triple.

#### Proof

The colour orbit has size \(q/3=h(s/3)\), whereas the free edge orbit has
size \(q=hs\).  Both actions of \(H\) are free, so their numbers of
\(H\)-orbits are respectively \(s/3\) and \(s\).  The equivariant colour
map restricts to a bijection from each \(H\)-edge orbit onto one
\(H\)-colour orbit.  Its total fibre size is three, proving the claim.
Exact rainbowness selects one, rather than zero or three, provider orbits
over each colour orbit. \(\square\)

Proposition 10.6 describes the local ternary provider fibres, but it is no
longer an existential instruction to prescribe those providers and then
extend them.  Theorem 11.3 below chooses a perfect matching of the complete
quotient diamond graph first; its restriction automatically chooses all
exceptional providers.  The surviving all-\(m\) target is therefore to
choose that global quotient matching so that its induced middle graph is a
linear forest, and then to close its occurrence-labelled endpoints by one
protected unit-voltage transition.  The asymmetric provider phases are
outputs of this choice, not prior constraints on it.

## 11. Period-three paired-necklace transition system

Assume now

\[
 q=6a+3,\qquad m=3a+2,\qquad
 {\cal N}_a=\binom{\mathbb Z_{2a+1}}a/\mathbb Z_{2a+1},\qquad
 |{\cal N}_a|=\operatorname{Cat}_a.                  \tag{11.1}
\]

The period-three filter theorem identifies two complementary exceptional
colour banks indexed by \({\cal N}_a\).  At the clean \(H\)-scale, one full
exceptional colour orbit splits into \(s/3\) free \(H\)-colour orbits.
Thus the lower and upper exceptional demand rows are

\[
 {\cal X}^-={\cal N}_a\times\mathbb Z_{s/3},qquad
 {\cal X}^+={\cal N}_a\times\mathbb Z_{s/3},          \tag{11.2}
\]

and each bank has \((s/3)\operatorname{Cat}_a\) rows.  Complementation gives
an index pairing between \({\cal X}^-\) and \({\cal X}^+\), but no common
Johnson provider: an exceptional lower colour contains \(\infty\), whereas
an exceptional upper colour avoids it, so no edge can service both.

Fixing one free full-rotation provider orbit over one exceptional necklace,
Proposition 10.6 identifies the three clean-\(H\) provider orbits above a row
\((\nu,c)\).  An \(H\)-invariant section of that fixed provider orbit is
therefore a phase function

\[
 \phi^\pm_\nu:\mathbb Z_{s/3}\longrightarrow\mathbb Z_3.          \tag{11.3}
\]

After compatible gauges, the three provider indices above
\(c\in\mathbb Z_{s/3}\) are
\[
                         c,\quad c+s/3,\quad c+2s/3\pmod s,
\]
and \(\phi^\pm_\nu(c)\) chooses one of them.
Hence one fixed full provider orbit has exactly
\[
                         3^{s/3}
\]
\(H\)-invariant sections.  The residual \(\mathbb Z_s\)-action on these
phase words is free, so they form exactly \(3^{s/3}/s\) residual cyclic
orbits.  Without \(H\)-invariance there are instead \(3^{q/3}\) arbitrary
physical sections.  For freeness, any nontrivial subgroup of the cyclic
3-group \(\mathbb Z_s\) contains its order-three subgroup; invariance under
that subgroup would make a transversal a union of three-point fibres,
contradicting its choice of exactly one point per fibre.

Only when \(v_3(q)=1\), so \(s=3\), is (11.3) one scalar choice among three
phases.  With several contributing full edge orbits, each row instead has
the union of their ternary provider lists.

Theorem 3 of the period-three filter note supplies a genuine positive input
when \(v_3(q)=1\): it constructs exactly
\(2\operatorname{Cat}_a\) clean-\(H\) provider orbits, pairs complementary
lower and upper necklace indices, and makes all of their middle endpoints
distinct.  In the terminology below this supplies the two provider
occurrences required in item 1 for every \(p\), at the provider/middle
matching level.  It does not order them into macro paths, insert the
ordinary quotient records, saturate all remaining ports, or prove topology,
guards or voltage.

There is also an exact global congruence toll.  The exceptional-bank lower
bound is \(2\operatorname{Cat}_a\) partial full-rotation edge orbits, but if
\(3\nmid\operatorname{Cat}_a\), every complete two-sided-rainbow edge set
has at least
\[
                         2\operatorname{Cat}_a+1                 \tag{11.4a}
\]
partial full-rotation edge orbits.  At least one extra orbit has both colour
orbits nonexceptional.  Thus the paired exceptional provider bank cannot by
itself be the complete transition defect bank in this case.

Indeed, put \(C=\operatorname{Cat}_a\),
\(E=(q/3)C\), and \(R=\binom{2m}{m-1}\).  The nonexceptional lower colours
are a union of free \(q\)-orbits, so \(q\mid R-E\).  If exactly \(2C\)
partial edge orbits existed, equality in the exceptional-bank bound would
put exactly \(2E\) selected edges in them and all remaining selected edge
orbits would be full, giving \(q\mid R-2E\).  Subtraction yields
\(q\mid E\), equivalently \(3\mid C\), a contradiction.  If every partial
orbit met an exceptional colour orbit, the same count would apply, proving
the nonexceptional assertion.

### Theorem 11.1 (two-bank paired-necklace transition)

Put

\[
                         {\cal P}={\cal N}_a\times\mathbb Z_{s/3}.          \tag{11.4}
\]

For every \(p\in{\cal P}\), suppose there are protected directed quotient
macro paths \(L_p\) and \(U_p\).  The first contains one selected provider
for the lower row \((-,p)\), and the second contains one distinct selected
provider for the complementary upper row \((+,p)\).  The macros may absorb
specified ordinary quotient records; collectively they are disjoint,
partition the complete quotient state set of the spanning path forest,
saturate their internal occurrence ports, and leave one entry and one exit
each.  Write their internal \(H\)-voltages as \(\ell_p,u_p\).

Suppose protected seam orbits give bijections
\(\alpha,\beta\in\operatorname{Sym}({\cal P})\) through

\[
\begin{aligned}
 \operatorname{exit}(L_p)&\longrightarrow
        \operatorname{entry}(U_{\alpha(p)}) &&\text{with voltage }a_p,\\
 \operatorname{exit}(U_j)&\longrightarrow
        \operatorname{entry}(L_{\beta(j)}) &&\text{with voltage }b_j.
\end{aligned}                                                     \tag{11.5}
\]

Assume that internal transitions and seams jointly use every physical
occurrence port exactly once, are pairwise physically distinct and avoid
retained internal edges, satisfy both exact adjacent palette ledgers, and
pass the selected deeper-witness and residence guards.  Define

\[
 \theta=\beta\circ\alpha,\qquad
 \Delta_p=\ell_p+a_p+u_{\alpha(p)}+b_{\alpha(p)}\pmod h.            \tag{11.6}
\]

For a cycle \(D\) of \(\theta\), put
\(V_D=\sum_{p\in D}\Delta_p\pmod h\).

Then the exact physical component count is

\[
                         c(F)=\sum_{D\in{\cal C}(\theta)}
                                      \gcd(h,V_D).                  \tag{11.7}
\]

In particular, the result is one protected physical Hamilton cycle if and
only if

\[
             \theta\text{ is one cycle}
             \quad\text{and}\quad \gcd(h,V_D)=1.                  \tag{11.8}
\]

#### Proof

Start at the entry of \(L_p\), traverse \(L_p\), the first seam,
\(U_{\alpha(p)}\), and the second seam.  Equation (11.5) becomes the skew
permutation

\[
                         (p,g)\longmapsto
                         (\theta(p),g+\Delta_p).
\]

Theorem 10.1 gives (11.7)--(11.8), and the joint literal guard hypotheses
give the protected conclusion. \(\square\)

The complementary necklace pairing does not force
\(\alpha=\beta=\operatorname{id}\), nor does it construct either macro
family.  Theorem 3 of the period-three note supplies one disjoint seed edge
inside every \(L_p,U_p\) only when \(s=3\); all macro extensions and both
port bijections remain additional hypotheses.

### Proposition 11.2 (physical linear two-bank transition)

Retain only the two-bank indexing of Theorem 11.1, but now let every
\(L_p,U_p\) be an already-connected **physical** macro path, and let the
seams below be single physical edges rather than developed \(H\)-orbits.
Assume these \(2|{\cal P}|\) macros are pairwise vertex-disjoint and their
vertex sets partition the complete physical carrier state set.  Let
\(\alpha:{\cal P}\to{\cal P}\) be a complete \(L\)-to-\(U\) seam
bijection.  Choose \(j_{\rm end},p_{\rm start}\in{\cal P}\), and let
\[
 \beta:{\cal P}\setminus\{j_{\rm end}\}
       \longrightarrow{\cal P}\setminus\{p_{\rm start}\}           \tag{11.9}
\]
be a bijection of the remaining \(U\)-exits to \(L\)-entries.  Put
\[
 p_{\rm end}=\alpha^{-1}(j_{\rm end}),\qquad
 \theta(p)=\beta(\alpha(p))\quad(p\ne p_{\rm end}).                \tag{11.10}
\]
Assume the \(\alpha\)-seams use every \(L\)-exit and every \(U\)-entry
exactly once, the \(\beta\)-seams use exactly all remaining \(U\)-exits and
\(L\)-entries, and all seams are distinct and avoid macro interiors.  Under
the corresponding physical simplicity and guard hypotheses, the
\(2|{\cal P}|\)
macros form one directed physical path if and only if \(\theta\) is one
directed Hamilton path on \({\cal P}\), from \(p_{\rm start}\) to
\(p_{\rm end}\).  The number of cross-macro seams is exactly
\[
                         |{\cal P}|+(|{\cal P}|-1)
                         =2|{\cal P}|-1.              \tag{11.11}
\]

#### Proof

Starting at \(L_p\), the complete seam family first enters
\(U_{\alpha(p)}\).  Unless \(p=p_{\rm end}\), the partial seam family then
enters \(L_{\beta(\alpha(p))}=L_{\theta(p)}\).  Thus contraction of each
\(L_p,U_p\) macro gives precisely the partial successor \(\theta\).  Its
being one Hamilton path is necessary and sufficient for the uncontracted
alternating macro path.  The seam count is immediate. \(\square\)

This is the exact symmetry-broken linear analogue of Theorem 11.1.  It has
no global voltage condition because its inputs are already-connected
physical macros and the final
\(U_{j_{\rm end}}\)-to-\(L_{p_{\rm start}}\) closure is absent.  If instead
the same partial system is developed from \(H\)-quotient macros using full
seam orbits, it generally gives \(h\) physical paths, not one; an additional
phase braid is then required.  A legal physical closing seam closes the
displayed physical path into a cycle.

Theorems 11.1--11.2 are useful structured architectures, but the exceptional
providers should not be prescribed before solving the global palette
matching.  The following theorem removes that extension quantifier.

### Theorem 11.3 (global quotient matching gives extendable filters)

Let
\[
 {\cal L}=\binom{\Omega}{m-1},\qquad
 {\cal U}=\binom{\Omega}{m+1},
\]
and let \({\cal B}_m\) be the bipartite diamond graph
\[
                         L\sim U\quad\Longleftrightarrow\quad L\subset U.
                                                                    \tag{11.12}
\]
Both shores have size \(\binom{2m}{m-1}\), and every vertex has degree
\[
                         \Delta=\binom{m+1}{2}.                       \tag{11.13}
\]
Let the clean group \(H\cong\mathbb Z_h\) act freely on both shores.
Then the quotient multigraph \({\cal B}_m/H\) is balanced and
\(\Delta\)-regular, has a perfect matching \(\overline M\), and its orbit
lift \(M\) is an \(H\)-invariant physical perfect matching of
\({\cal B}_m\).

Consequently every predetermined \(H\)-stable vertex bank, including both
period-three exceptional banks, is serviced by restricting this already
global matching \(M\) to the edges incident with the bank.  This does not
extend prescribed provider edges or phases; the providers are chosen as the
restriction of \(M\).

#### Proof

Freeness implies that an edge orbit incident with a quotient vertex contains
exactly one edge at every physical vertex in that vertex orbit.  Two
different physical incidences at one vertex cannot lie in the same edge
orbit, since that would give a nonidentity stabilizer of the vertex.
Therefore every quotient vertex has degree \(\Delta\), with parallel orbit
edges retained.  For every quotient left set \(X\),
\[
                         \Delta|X|\le\Delta|N(X)|,
\]
so Hall gives \(\overline M\).  Lifting every selected quotient edge to its
full \(H\)-orbit covers every physical shore vertex once. \(\square\)

When \(q=6a+3\), the exceptional restriction contains exactly
\[
                         2\frac{s}{3}\operatorname{Cat}_a          \tag{11.14}
\]
clean-\(H\) edge orbits; for \(s=3\), this is
\(2\operatorname{Cat}_a\).  Indeed one exceptional full-rotation colour
orbit has size \(q/3=(s/3)h\), hence splits into \(s/3\) clean quotient
vertices; there are \(\operatorname{Cat}_a\) such full orbits on each typed
shore.  No selected edge can meet an exceptional vertex on both shores, so
the two counts add.

The lower and upper exceptional restrictions are disjoint.  Within each
typed opposite shore their used colours are distinct, because they are
endpoints of different matching edges.  Equality between a lower-family
and an upper-family label after the auxiliary complement identification is
possible and is not excluded.  All physical rank-\(m\) middle endpoints of
the filters are nevertheless pairwise distinct.  Two different exceptional
lower colours differ by at least two complete order-three cosets, so they
cannot both lie in one rank-\(m\) set; the upper assertion is complementary,
and lower-filter middle endpoints contain \(\infty\) whereas upper-filter
endpoints do not.

This distinctness is internal to the filter restriction.  A selected
nonexceptional diamond can still use one of those middle vertices; excluding
such branching is part of the degree constraints in Theorem 11.4, not part
of Theorem 11.3.

For \(s=3\), each selected exceptional \(H\)-edge orbit occupies exactly one
third of one free full-rotation edge orbit.  This makes the
**exceptional-bank contribution** locally sharp.  It does not say that the
whole matching has only \(2\operatorname{Cat}_a\) partial full-rotation
orbits: when \(3\nmid\operatorname{Cat}_a\), the global congruence above
forces at least one additional nonexceptional partial orbit.

### Theorem 11.4 (exact global matching-to-forest/socket gate)

Put \(K=\operatorname{Cat}_m\),
\[
 N_m=\binom{2m}{m}=(m+1)K,\qquad
 R_m=\binom{2m}{m-1}=mK.                               \tag{11.15}
\]
For a quotient perfect matching \(\overline M\) from Theorem 11.3, lift it
to \(M\).  Assume additionally that \(H\) has odd order and acts freely on
the rank-\(m\) middle vertices.  (Both properties hold for the clean
Catalan group.)  Every matched diamond \(L\subset U\), with
\(U\setminus L=\{x,y\}\), canonically gives the Johnson edge
\[
                         (L\cup\{x\})(L\cup\{y\}).                  \tag{11.16}
\]
Let \(J(M)\) be the resulting developed \(H\)-invariant middle graph and
\(\overline J(\overline M)=J(M)/H\) its occurrence multigraph.

1. \(J(M)\) has exactly \(R_m\) edges on all \(N_m\) middle vertices and
   uses every lower and every upper colour exactly once.
2. \(J(M)\) is a spanning linear forest if and only if
   \(\overline J(\overline M)\) is acyclic as a multigraph and has maximum
   degree at most two.  Equivalently, it has no quotient loop,
   \[
      |E(\overline J[S])|\le |S|-1
      \quad(\varnothing\ne S\subseteq V(\overline J)),
   \]
   and every quotient middle vertex has degree at most two.
3. Under item 2, the quotient forest has exactly \(K/h\) path components,
   and its lift has exactly \(K\) physical path components.  Endpoints are
   counted as deficit occurrences: a vertex of degree \(d\) contributes
   \(2-d\) ports, so an isolated vertex contributes two.  Thus there are
   exactly \(2K/h\) quotient endpoint occurrences and \(2K\) physical
   endpoint occurrences.
4. Orient those quotient path occurrences and choose literal, physically
   injective \(H\)-orbit closure seams using every endpoint occurrence once.
   If the resulting occurrence successor \(\tau\) is one cycle and its
   total internal-plus-seam voltage is a unit modulo \(h\), then its
   development is one physical Hamilton cycle.  The closure contains exactly
   \(K/h\) quotient seam orbits and \(K\) physical seams.  Conversely these
   two conditions are necessary inside that invariant closure fibre.

#### Proof

The diamond matching gives one edge for every lower and upper colour,
proving item 1 and the counts (11.15).  A cover of a quotient multigraph
which contains a loop, parallel-edge cycle or ordinary cycle contains a
physical cycle; conversely the lift of a quotient forest is a disjoint
union of forests because every tree voltage can be gauged to zero.  The
odd-order middle action has no edge inversion, so this is an ordinary
regular multigraph cover rather than a quotient half-edge.
Physical degrees equal quotient occurrence degrees.  This proves item 2.
Euler's formula gives
\[
 \frac{N_m}{h}-\frac{R_m}{h}=\frac Kh
\]
quotient components.  Lemma 10.2 makes their \(H\)-action free, giving
item 3; the port count is the degree-deficit identity
\(\sum_v(2-d(v))=2|V|-2|E|\).  Pairing all ports gives the stated seam
count.  Item 4 is Theorems 4.2 and 10.1 applied to the
occurrence-labelled path ports. \(\square\)

The forest condition is not a consequence of regular quotient Hall.  At
\(m=5\) one has \(q=9,s=9,h=1\), so the clean quotient is the physical
diamond graph.  In the standard BTK two-rank perfect matching, put
\[
                         E_5=\{0,2,4,6,8\},\qquad
                         L_j=E_5\setminus\{2j\}.
\]
The matched upper set adds \(\{0,9\}\) when \(j=0\), and adds
\(\{2j-1,2j\}\) when \(1\le j\le4\).  Each of the five induced Johnson
edges is incident with \(E_5\), so \(\deg_{J(M)}(E_5)=5\).  This is an
explicit matching-first counterexample to any claim that (11.13) alone
forces item 2.

The **closure-socket** condition in item 4 says that closure seams must use
occurrence-labelled endpoint ports injectively, be pairwise physically
distinct, avoid retained internal edges and degree-two internal path
vertices, and pass the literal palette, deeper-shadow and residence ledgers.
Here injectivity concerns port and seam occurrences: the two ports of an
isolated path vertex are distinct occurrences at the same physical vertex.
The exceptional filters are already internal edges of \(J(M)\); they need
no separate **extension** sockets.  If the protected construction intends
to replace, decorate or route those filter edges through packets, then each
such packet needs its own occurrence-labelled private socket, with all
endpoint, phase, voltage, collar, host and witness resources capacity-one.
Pairwise-distinct filter middle endpoints do not imply these stronger socket
conditions.  Thus filter-extension Hall is retired, while packet/socket
compatibility is not.

The matching theorem itself guarantees only the two adjacent palettes.
If the conclusion is called protected, the chosen internal forest
\(J(M)\), as well as its closure seams, must explicitly retain the selected
deeper-witness bank and residence corridors.

Since \(J(M)\) already uses every outer colour exactly once, closure seams
cannot create adjacent-palette holes; they only add multiplicity.  The
extremal cap-two profile
\[
                         1^{R_m-K}2^K
\]
on both shores is obtained exactly when the \(K/h\) quotient closure seams
have pairwise distinct lower-colour orbits and pairwise distinct
upper-colour orbits.  Any stronger outgoing-sign, contiguous-block or
compiler compatibility remains occurrence-level and is not implied by
regular quotient Hall.

### Proposition 11.5 (generic symmetry-broken forest splice)

Let \(F\) be any physical spanning linear forest with \(K\) components,
with its \(2K\) endpoint ports counted by degree deficit.  Let \(S\) be
\(K-1\) distinct new edges, each joining two endpoint-port occurrences, so
that every port is used at most once and no edge of \(S\) repeats an edge of
\(F\).  Contract every component of \(F\).  Then \(F\cup S\) is one
Hamilton path if and only if the contracted seam graph is one path and its
two unused ports are the two ends.  If \(F=J(M)\), the exact adjacent-colour
multisets are
\[
 \chi_\pm(F\cup S)={\bf 1}_{\mathcal C_\pm}
                  +\sum_{e\in S}{\bf e}_{c_\pm(e)},               \tag{11.17}
\]
where \(c_-(e)\) and \(c_+(e)\) are its intersection and union colours.
In particular, pairwise distinct seam colours on each typed shore give
\[
                         1^{R_m-K+1}2^{K-1}.                       \tag{11.18}
\]
All seams must still be literal Johnson edges and pass the deeper-shadow,
residence, boundary and compiler ledgers.

#### Proof

After contraction, every component-vertex has degree at most two.  The
uncontracted graph is connected and acyclic with two unused ports exactly
when the contracted graph is a path; expansion of its contracted vertices
then gives a spanning path.  Equation (11.17) is the disjoint edge ledger,
and (11.18) follows from distinctness. \(\square\)

If \(h>1\), a single physical Hamilton path cannot itself be
\(H\)-invariant: the automorphism group of a finite path has order at most
two, whereas \(H\) has odd order and acts freely on its vertices.  Hence a
linear output from the clean quotient generally has to break symmetry, as
the K16 chronology does.

Thus the residual Kneser/phase Hall problem is retired.  The exact remaining
existence theorem is to choose \(\overline M\) **inside the global quotient
perfect-matching fibre** so that item 2 holds and its path endpoints admit
the protected socket closure in item 4.  For a symmetry-broken linear
output, use Proposition 11.5 (or its structured specializations,
Proposition 11.2 and Theorem 12.2) and perform the full physical
guard/compiler replay.

The compiler is deliberately outside the equivariant theorem.  It may be
chosen only after the physical carrier and may break \(H\)-symmetry; the
authenticated K16 compiler shows that requiring equivariance here would be
a false additional restriction.

## 12. Interlaced strict-spiral blocks and palette-safe linear splicing

The contiguous-sector architecture of Theorem 10.4 is not the only useful
one.  A strict full-rotation spiral interlaces every residual sector inside
one physical block.

### Theorem 12.1 (clean voltage of a strict spiral)

Let \(R\) generate a free \(\mathbb Z_q\)-action, write \(q=sh\), and put
\(H=\langle R^s\rangle\cong\mathbb Z_h\).  Let
\[
 P=(p_0,\ldots,p_{n-1})
\]
be one base sheet, and let \(\gcd(\eta,q)=1\).  Suppose the literal
concatenation
\[
 C=\operatorname{Sp}(P,\eta)
   =P\Vert R^\eta P\Vert\cdots\Vert R^{(q-1)\eta}P      \tag{12.1}
\]
with its sheet joins and final wrap is a simple physical cycle.  Then its
\(H\)-quotient is one cycle on \(sn\) quotient vertices, its clean
\(H\)-voltage is
\[
                              \eta\pmod h,              \tag{12.2}
\]
and its \(H\)-lift is the one physical cycle \(C\).

#### Proof

Modulo \(H\), retain the \(s\) consecutive sheet representatives
\(P,R^\eta P,\ldots,R^{(s-1)\eta}P\).  Traversing them returns to the first
quotient sheet at
\[
                         R^{\eta s}P=(R^s)^\eta P,
\]
so the quotient voltage is \(\eta\bmod h\).  Since
\(\gcd(\eta,q)=1\), also \(\gcd(\eta,h)=1\); Theorem 2.1 gives one physical
lift.
\(\square\)

Thus a strict spiral is not a sector-separated port packet.  Its quotient
cycle itself traverses all \(s\) residual sheet classes before acquiring
the clean voltage (12.2).

### Corollary 12.1A (equivariant block-return criterion)

Let \({\cal B}\) index strict blocks in an \(H\)-invariant transition
system.  Suppose every transition follows one residual-sector cycle, and
after one complete sector tour the block index has return permutation
\(\sigma\).  Let \(w_b\in\mathbb Z_h\) be the voltage of that tour from
block \(b\) to block \(\sigma(b)\).  Then
\[
 c(F)=\sum_{D\in{\cal C}(\sigma)}
          \gcd\!\left(h,\sum_{b\in D}w_b\right).
\]
Hence the equivariant block braid is Hamiltonian exactly when \(\sigma\) is
one cycle and its total return voltage is a unit.  Call the connectors
**phase-aligned with zero defect** when deleted and inserted boundary
voltages agree and the complete sector-tour voltage from every block is
exactly the strict-spiral voltage \(\eta\), so \(w_b=\eta\).
In this co-oriented zero-defect case, a single \(t\)-block return cycle is
connected exactly when
\[
                         \gcd(h,t\eta)=1,
\]
equivalently \(\gcd(h,t)=1\).

#### Proof

This is Theorem 10.3 after compressing every within-sector subpath and
identifying \(\sigma\) as the sector-tour return map. \(\square\)

This corollary applies only while connectors are selected as full
\(H\)-orbits.  Phase-specific physical openings and singleton seams destroy
that equivariance and must be handled by Theorem 12.2 instead.

### Theorem 12.2 (physical block-path splice)

Let \(C_1,\ldots,C_t\) be vertex-disjoint simple physical cycles, not
necessarily jointly invariant under any group.  Choose and orient one edge
\[
                         d_i=(z_i,x_i)\in E(C_i)
\]
as the closing edge of \(C_i\), and delete all \(d_i\).  Let
\(\sigma\) be an ordering of \([t]\).  If the \(t-1\) pairs
\[
                         f_j=(z_{\sigma(j)},x_{\sigma(j+1)}),
                         \qquad 1\le j<t,              \tag{12.3}
\]
are pairwise distinct literal Johnson edges, then
\[
 \left(\bigsqcup_{i=1}^t(C_i-d_i)\right)
       \sqcup\{f_1,\ldots,f_{t-1}\}                    \tag{12.4}
\]
is one simple physical Hamilton path on the union of the block vertices.
Conversely, suppose a splice deletes exactly one edge \(d_i\) from each
block, retains \(C_i-d_i\) as one connected path, adds only cross-block
edges, and produces one path.  It uses at least \(t-1\) cross-block edges;
at equality its contracted block graph is a tree, and coherent degree at
most two makes that tree a path.

#### Proof

Deleting \(d_i\) opens \(C_i\) into the directed path from \(x_i\) to
\(z_i\).  The seams (12.3) concatenate those paths in the order
\(\sigma\), proving (12.4).  Contracting the \(t\) nonempty block paths
shows that any connected splice needs at least \(t-1\) cross-block edges.
At equality the contraction is a tree; the final path-degree condition
forces maximum degree two and hence a path. \(\square\)

The additional cyclic seam is neither needed nor allowed unless it is itself
a literal Johnson edge.  If it exists, adding it closes (12.4) into a cycle.
If it is non-Johnson, the correct output is the linear path.

### Proposition 12.3 (exact palette-safe connector ledger)

For a Johnson edge \(e=XY\), put
\[
                         \ell(e)=X\cap Y,\qquad u(e)=X\cup Y.
\]
Assume now that every edge of every \(C_i\), as well as every inserted
seam, is a Johnson edge.  Let \(\chi_\ell(E)\) and \(\chi_u(E)\) denote the
occurrence multisets of lower and upper colours of an edge set \(E\).  In
Theorem 12.2, with
\(E_0=\bigsqcup_iE(C_i)\), \(D=\{d_1,\ldots,d_t\}\), and
\(S=\{f_1,\ldots,f_{t-1}\}\), the final path has exactly
\[
\begin{aligned}
 \chi_\ell(E_{\rm fin})
   &=\chi_\ell(E_0)-\sum_{d\in D}{\bf e}_{\ell(d)}
                      +\sum_{f\in S}{\bf e}_{\ell(f)},\\
 \chi_u(E_{\rm fin})
   &=\chi_u(E_0)-\sum_{d\in D}{\bf e}_{u(d)}
                      +\sum_{f\in S}{\bf e}_{u(f)}.    \tag{12.5}
\end{aligned}
\]
Equivalently, if \(\mu_\ell,\mu_u\) are the background loads and
\(d^\pm_z,j^\pm_z\) are the numbers of deleted and inserted incidences of
colour \(z\), adjacent-palette coverage is preserved exactly when
\[
                         \mu_\pm(z)-d^\pm_z+j^\pm_z\ge1             \tag{12.6}
\]
for every required lower or upper colour \(z\).  For prescribed exact
adjacent-palette multisets \(\Lambda_\ell,\Lambda_u\), replace (12.6) by
equality of the two right sides in (12.5) with
\(\Lambda_\ell,\Lambda_u\).  Deeper shadows, residence and the common-cap
compiler remain additional occurrence-level guards.

#### Proof

The final edge set is exactly \((E_0\setminus D)\sqcup S\); applying the
intersection and union colour maps gives (12.5). \(\square\)

### Corollary 12.4 (A/B lift seam count)

If an odd parent has \(c\) cyclic components and a two-rail lift turns each
parent component into one \(A\)-block and one \(B\)-block, then the even
child has \(t=2c\) block cycles.  Any block-interior-preserving linear splice
needs at least
\[
                              2c-1                         \tag{12.7}
\]
cross-block seams, and a palette-safe directed block path with exactly that
many seams is sufficient.

This is a connector-count identity, not a connector-existence theorem.

### 12.5 Exact K16 reconciliation

The authenticated K16 carrier in
MATH_THEOREM_K16_THREE_PRIMARY_SPIRAL_BRAID_ANATOMY_20260731.md has
\[
 q=15,\qquad s=3,\qquad h=5,\qquad
 a_{\rm Cat}=2,\qquad \eta=4.
\]
It consists of four co-oriented strict spirals with base lengths
\[
                         426,\quad426,\quad3,\quad3.   \tag{12.8}
\]
By Theorem 12.1 each closed block has one clean-\(\mathbb Z_5\) quotient
cycle of voltage \(4\in\mathbb Z_5^\times\).  Every block contains all
three residual sectors in sheet order
\[
                         0,1,2,0,1,2,\ldots,
\]
so it is not an instance of the sector-separated paths in Theorem 10.4.

More explicitly, the clean quotient states of block \(i\) are
\((i,c,r)\), where \(c\in\mathbb Z_3\) and \(0\le r<n_i\).  Within a
sector subpath \(r\) advances normally; the three sheet-boundary transitions
have clean voltages \(0,0,4\).  Compressing each sector subpath gives sector
permutation \((0\,1\,2)\), but the three-step return map is the identity on
the four block indices in this compressed macro system.  On raw quotient
states the corresponding return takes \(3n_i\) edge transitions.  Theorem
10.3 therefore gives
\[
                         4\gcd(5,4)=4
\]
closed physical components, exactly as in the literal factor.

The final chronology deletes one physical closure edge from each block and
uses exactly three physical Johnson seams.  These four deletions and three
insertions are phase-specific rather than complete \(H\)-orbits, so the
final linear path is not governed by an invariant voltage cover.  Its
connectedness follows directly from Theorem 12.2, while its adjacent
palettes obey (12.5)--(12.6).  The three-seam bank is coverage-safe, not
palette-multiset-neutral.  The unused fourth wrap
\(0xf30c\to0xc3ca\) has symmetric difference six, rank-five intersection
\(0xc308\), and rank-eleven union \(0xf3ce\); it is not a Johnson edge and
supplies no adjacent q1 transition.

It is exactly Proposition 11.2 with
\[
\begin{array}{c|cc}
p&L_p&U_p\\ \hline
\mathrm{large}&B_{\rm large}&A_{\rm large}\\
\mathrm{small}&A_{\rm small}&B_{\rm small},
\end{array}
\qquad
\alpha=\operatorname{id},\qquad
\beta(\mathrm{large})=\mathrm{small},\qquad
p_{\rm start}=\mathrm{large},\qquad
p_{\rm end}=j_{\rm end}=\mathrm{small}.                \tag{12.9}
\]
The missing \(\beta(\mathrm{small})=\mathrm{large}\) edge is precisely the
non-Johnson wrap.  These \(L/U\) labels describe alternating physical block
roles; they are not a canonical identification with the lower/upper
period-three necklace providers.

The blocks are the \(A/B\) lifts of \(c=2\) parent components, giving the
literal identity
\[
                         c=2\longmapsto2c=4
                         \longmapsto2c-1=3\text{ seams}.           \tag{12.10}
\]
The four phase defects do not correspond one-for-one to the four shortened
outer-colour orbits.  Accordingly, the period-three provider theorem should
guide palette-safe opening choices but does not canonically label the four
spiral blocks.  The exact scalable target exposed by K16 is:

1. construct a bounded collection of protected strict spiral blocks;
2. orient and open them so their contracted palette-safe connector graph
   contains a directed Hamilton path; and
3. verify (12.5), deeper witnesses, residence and common-cap compilation on
   the resulting physical order.

Sector-separated ports are only one sufficient architecture.  The K16
certificate instead proves the viability of palette-safe connectors between
sector-interlaced blocks.  Its decoded common-cap compiler is strongly
non-\(H\)-invariant, so the compiler must be solved after the physical braid;
equivariant compilation is not a valid general hypothesis.

## 13. General sufficient quotient target

The reusable theorem exposed by the \(m=4\) fixture is:

> **Protected cyclic Catalan transition lemma.**  Put
> \(q=2m-1\), \(s=3^{v_3(q)}\), \(h=q/s\), and use the free clean group
> \(H\cong\mathbb Z_h\).  Choose \(H\)-orbits of retained marked and
> unmarked fragments, occurrence-labelled endpoint ports and invariant safe
> seam records so that:
>
> 1. the orbit developments satisfy EC1--EC3 exactly;
> 2. the quotient records saturate every source, intermediate and target
>    fragment orbit once;
> 3. their full sector-labelled quotient transition permutation is one
>    occurrence cycle;
> 4. the total quotient voltage generates \(\mathbb Z_h\);
> 5. all physical seam occurrences are simple, pairwise distinct and
>    disjoint from retained internal edges; and
> 6. one invariant literal witness/corridor bank survives, or every final
>    physical witness and residence state is replayed.

Theorems 4.1--4.2 prove that these hypotheses give one protected physical
cycle with exact adjacent palettes.  A protected quotient splice satisfying
(5.2)--(5.3) gives the corresponding constructive repair when the initial
quotient has several cycles.

Theorem 11.3 now supplies the adjacent-palette part without prescribing
filters.  A completely checkable matching-first certificate consists of
binary quotient-diamond variables \(x_e\) satisfying
\[
 \sum_{e\ni L}x_e=1,qquad \sum_{e\ni U}x_e=1                 \tag{13.1}
\]
at every lower and upper quotient vertex, together with the induced-middle
conditions
\[
 \deg_x(v)\le2,qquad
 \sum_{e:\,j(e)\subseteq S}x_e\le |S|-1
       \quad(\varnothing\ne S\subseteq V(\overline J)).       \tag{13.2}
\]
Here \(j(e)\) is the quotient Johnson edge induced by the diamond edge
\(e\), loops and parallel edges retain their multigraph meanings, and
\(S\) is a set of quotient middle occurrences.  Equations (13.1) are the
global quotient perfect matching; (13.2) is necessary and sufficient for
its lift to be the \(K\)-path linear forest of Theorem 11.4.  The remaining
socket variables must saturate the \(2K/h\) quotient endpoint occurrences,
form one occurrence transition cycle, have unit total \(H\)-voltage, and
pass the literal guard ledgers.  This is the exact surviving all-\(m\)
existence problem.  It is not a residual extension problem for a fixed
exceptional filter.

These are the `(QM),(D),(G)` core rows of
`MATH_REDUCTION_GLOBAL_QUOTIENT_MATCHING_PHYSICAL_FOREST_SOCKET_VOLTAGE_20260731.md`.
Its `(D+)` and `(BW0)--(BW3)` rows are the stronger, explicitly conditional
nontrivial block-wedge face; its socket refinements require an exhaustive
orbit-complete resource catalogue.

The canonical \(m=4\) object satisfies the resulting transition theorem
with \(q=h=7\), \(s=1\), and voltage \(2\).  When \(s>1\), Theorem 10.4
gives a precise sufficient contiguous-sector braid, and Theorem 11.1 gives
an optional paired-necklace macro architecture.  Neither architecture is a
necessary partition of a matching-first solution: the globally chosen
filters are internal edges of \(J(M)\), and a valid socket braid may
interlace residual sectors.

The K16 optimum lies in the complementary linear architecture of
Theorem 12.2: clean voltage certifies each closed spiral block, after which
phase-specific palette-safe representatives open and concatenate the blocks.
No global unit-voltage condition applies to that final path without a
literal closing Johnson seam.  Its compiler is a subsequent asymmetric
choice and supplies no evidence that the common-cap assignment can be made
\(H\)-invariant in general.
