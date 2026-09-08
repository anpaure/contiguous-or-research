# Protected incidence transport: the parity obstruction, a neutral hexagon, and a parity absorber

Date: 2026-07-31.

Status: **partially superseded**.  The neutral-hexagon classification,
cut-disjoint witness theorem, residence conditions, and clean-component
merger calculations remain valid.  The length-only component-parity theorem
and every conclusion depending on it are withdrawn.

## Correction notice (2026-07-31)

Theorem 2.2, Corollaries 2.3--2.4, the parity inference in Theorem 3.1, and
the parity-dependent parts of Sections 6--8 are false.  A literal rainbow
two-rail factor at `m=2` has an alternating incidence C8 which preserves the
complete lower and immediate-upper multiplicity vectors and maps two factor
cycles to two factor cycles.  Thus component parity is not determined by
circuit half-length.  The error is in Lemma 2.1: the sign ratio of two
labelled matchings is not determined solely by the lengths of the cycles in
their superposition.

The correct universal topology theorem is occurrence-labelled.  Delete the
old circuit half, let `P` pair boundary ports along retained strands, and let
`R,B` be the old and new circuit pairings.  The affected component counts are
exactly `c(P union R)` and `c(P union B)`; there is no length-only parity
shortcut.  Clean `ell`-component switches still merge `ell -> 1`, so the
clean common-exterior C8 theorem remains valid.

The correction and explicit counterexample are proved in
`MATH_THEOREM_R_CATALAN_TWO_RAIL_PORT_MATCHING_AND_C8_CONNECTIVITY_OBSTRUCTION_20260731.md`.

## 0. Original conclusions, with withdrawn clauses marked

Let (I(2m+1,m)) be the inclusion graph between the two middle levels.  A
balanced two-extension factor is a simple spanning 2-factor of this bipartite
graph.  Items 2, 3 and 6 in the original list below are withdrawn by the
correction notice; the other items retain their stated scopes.

1. Any two factors are connected by compound alternating-circuit toggles.
2. **Withdrawn.**  A toggle on a simple alternating circuit of length
   (2\ell) was claimed to change the
   parity of the number of factor components by

   \[
                 \ell-1\pmod 2.                         \tag{0.1}
   \]

   In particular, every incidence-hexagon toggle has (\ell=3) and
   preserves component parity.
3. **Withdrawn as a parity inference.**  The hexagon move graph was claimed
   to be not connected, even inside the
   immediate-upper-surjective fibre.  An explicit counterexample already
   occurs in (I(5,2)).
4. A hexagon is exactly immediate-upper-multiset-neutral when its three
   untouched exterior owners use one common exterior coordinate.
5. Such a neutral hexagon is a literal zero-defect three-tail splice whenever
   chosen deeper witnesses avoid its deleted transitions and the exact
   residence automata accept the three new seams.
6. **Withdrawn as a parity-based conclusion.**  A protected
   parity-changing absorber, followed by a loose
   spanning tree of protected neutral hexagons, gives a monotone
   component-collapsing route to one component with zero shadow or residence
   defect.

The final parity conclusion of the original section is withdrawn.  Exact
connectivity must instead be computed from the retained occurrence-strand
pairing and the old/new circuit pairings.

## 1. The exact fibre

Put

\[
  {\cal C}=\binom{[2m+1]}m,\qquad
  {\cal V}=\binom{[2m+1]}{m+1},
\]

and let (I=I(2m+1,m)) have bipartition
({\cal C}\sqcup{\cal V}), with (C\sim V) when (C\subset V).
A **balanced factor** is a simple edge set (F\subseteq E(I)) satisfying

\[
        d_F(C)=d_F(V)=2
        \quad(C\in{\cal C},\ V\in{\cal V}).             \tag{1.1}
\]

If the selected neighbours of (C) are (C+a) and (C+b), contraction of
the row (C) gives the physical Johnson edge

\[
             (C+a)(C+b),                                \tag{1.2}
\]

whose lower colour is (C) and whose immediate-upper colour is

\[
             \sigma_F(C)=C+a+b.                         \tag{1.3}
\]

Hence (1.1) is exactly the lower-rainbow degree-two fibre, and immediate
upper completeness is the condition

\[
       \#\{C:\sigma_F(C)=U\}\ge1
       \quad\left(U\in\binom{[2m+1]}{m+2}\right).       \tag{1.4}
\]

If (F,G) are balanced factors, every vertex has equal red and blue degree
in (F\setminus G) and (G\setminus F).  Pairing red and blue half-edges at
each vertex decomposes (F\triangle G) into alternating circuits.  Toggling
these circuits one at a time proves unrestricted connectivity of the degree
fibre.  No hexagon or protection assertion is used in this argument.

## 2. The component-parity law

We first record the matching parity identity used in the proof.

### Lemma 2.1 (three matching parity)

Let (P,R,B) be perfect matchings on the same (2\ell) labelled points.
For two matchings (A,D), let (c(A,D)) be the number of alternating cycles
of (A\cup D), counting a common doubled edge as one cycle.  Then

\[
 (-1)^{\ell-c(P,B)}
   =(-1)^{\ell-c(P,R)}(-1)^{\ell-c(R,B)}.                \tag{2.1}
\]

#### Proof

Give a perfect matching its usual Pfaffian sign relative to one fixed order
of the (2\ell) points.  Superimposing (A) and (D), a component with
(2s) vertices contributes ((-1)^{s-1}) to the ratio of their signs.
Multiplying over components gives

\[
          \operatorname {sgn}(A)/\operatorname {sgn}(D)
             =(-1)^{\ell-c(A,D)}.
\]

The product of the ratios (P/R) and (R/B) is (P/B), proving (2.1).
This argument is independent of the chosen reference order. \(\square\)

### Theorem 2.2 (alternating-circuit component parity)

Let (F') be obtained from a 2-factor (F) by toggling a simple
(F)-alternating circuit of length (2\ell).  Then

\[
             c(F')-c(F)\equiv \ell-1\pmod2.             \tag{2.2}
\]

#### Proof

Let (R) be the (\ell) old factor edges and (B) the (\ell) new edges
on the alternating circuit.  In (F-R), every circuit vertex has degree one
and every other affected vertex has degree two.  Its noncyclic components
are therefore paths pairing the (2\ell) circuit vertices.  Contract those
paths to a perfect matching (P).  Unaffected factor cycles contribute
equally to (c(F)) and (c(F')), while the affected cycle counts are

\[
                    c(P,R)\quad\hbox{and}\quad c(P,B).
\]

The union (R\cup B) is one alternating (2\ell)-cycle, so
(c(R,B)=1).  Lemma 2.1 now gives

\[
   c(P,B)-c(P,R)\equiv \ell-c(R,B)=\ell-1\pmod2,
\]

which is (2.2). \(\square\)

### Corollary 2.3 (hexagon parity obstruction)

Every legal incidence-hexagon toggle preserves (c(F)\pmod2).  Therefore
every sequence of legal hexagon toggles preserves component parity, even if
all intermediate upper-shadow and residence constraints are discarded.

#### Proof

An incidence hexagon has length six, so (\ell=3) in Theorem 2.2. \(\square\)

More generally, a parity-changing primitive circuit must have even
half-length.  Consecutive Boolean levels have no 4-cycles, so a protected
parity absorber must use an alternating circuit of length at least eight.
The lower bound eight is structural; the first available circuit in a
particular factor may be longer.

### Corollary 2.4 (fixed-opening fragment covers)

Let a fragment-braid degree cover consist of one path and some cycles, with
fixed external endpoints, and close the path by one fixed dummy incidence
pair.  Any sequence of incidence-hexagon toggles which avoids that dummy and
keeps the endpoints fixed preserves the parity of the number of path-plus-
cycle components.  Hence an even-component cover cannot become one path by
such a C6-only sequence.

#### Proof

Adding the same dummy edge at every stage turns the cover into a spanning
2-factor without changing its number of components.  Every permitted toggle
is a hexagon toggle of that closed factor, so Corollary 2.3 applies. \(\square\)

Endpoint-changing or dummy-changing switches fall outside this corollary;
after closing them with different edges, the parity comparison acquires the
corresponding compound boundary exchange.

## 3. A balanced-surjective counterexample in (I(5,2))

Write a two-set as `12` and a three-set as `123`.  The following is one
Hamilton factor of (I(5,2)):

\[
\begin{split}
H={}&12-123-13-134-34-345-35-135-15-125\\
   &{}-25-235-23-234-24-245-45-145-14-124-12.
                                                               \tag{3.1}
\end{split}
\]

The following factor has two components:

\[
\begin{split}
E_1={}&12-123-13-135-35-345-45-245-24-124-12,\\
E_2={}&14-145-15-125-25-235-23-234-34-134-14,\\
E={}&E_1\cup E_2.                                      \tag{3.2}
\end{split}
\]

Every two-set and every three-set appears once in (3.1), and also once in
(3.2).  Thus both are balanced factors.  They are also immediate-upper
surjective.  In (H), the rank-four colours, listed at the two-set rows in
their cyclic order, are

\[
  1234,1234,1345,1345,1235,1235,2345,2345,1245,1245.
                                                               \tag{3.3}
\]

In (E_1) they are

\[
                1234,1235,1345,2345,1245,
\]

and in (E_2) they are

\[
                1345,1245,1235,2345,1234.              \tag{3.4}
\]

Hence each of the five upper targets has load exactly two in both factors.
Nevertheless (c(H)=1) and (c(E)=2).  Corollary 2.3 proves:

### Theorem 3.1 (nonnegative hexagon connectivity is false)

The legal incidence-hexagon move graph is disconnected even after
restricting to balanced factors which cover every immediate-upper target.

The obstruction is not unrestricted alternating-circuit connectivity.  In
fact (H\triangle E) is the single alternating 12-cycle

\[
  13-134-14-124-24-234-34-345-45-145-15-135-13.        \tag{3.5}
\]

Toggling (3.5) carries (H) to (E), and both endpoints have exactly the
same upper-load multiset.  Here (\ell=6), so (2.2) correctly predicts the
parity change.  The binary cycle-space decomposition of (3.5) into
hexagons therefore cannot be ordered as legal currently-alternating
hexagon toggles.  This is a literal counterexample to replacing algebraic
hexagon generation by monotone hexagon generation.

## 4. Classification of immediate-upper-neutral hexagons

Let (S\in\binom{[n]}{q-1}), and let (a,b,c\notin S) be distinct.  Put

\[
 C_a=S+a,\quad C_b=S+b,\quad C_c=S+c,
\]

and

\[
 T_{ab}=S+a+b,\quad T_{bc}=S+b+c,\quad T_{ca}=S+c+a.
\]

Suppose a factor contains the cyclic half

\[
       C_aT_{ab},\qquad C_bT_{bc},\qquad C_cT_{ca},     \tag{4.1}
\]

and not the opposite half.  Write the other selected owner in the three
rows as

\[
 O_a=S+a+x_a,\quad O_b=S+b+x_b,\quad O_c=S+c+x_c.       \tag{4.2}
\]

Legality and simplicity imply

\[
             x_a,x_b,x_c\notin S\cup\{a,b,c\}.         \tag{4.3}
\]

Toggle (4.1) to (C_aT_{ca},C_bT_{ab},C_cT_{bc}).

### Theorem 4.1 (common-exterior classification)

The multiset of the three immediate-upper colours is unchanged by the
hexagon toggle if and only if

\[
                         x_a=x_b=x_c.                  \tag{4.4}
\]

#### Proof

After removing the common core (S), the old upper colours are

\[
         abx_a,\qquad bcx_b,\qquad cax_c,              \tag{4.5}
\]

and the new colours are

\[
         acx_a,\qquad abx_b,\qquad bcx_c.              \tag{4.6}
\]

By (4.3), every set in (4.5)--(4.6) contains exactly two members of
(\{a,b,c\}).  Therefore the old set with pair (ab) can equal only the
new set with pair (ab), forcing (x_a=x_b).  The pairs (bc) and (ca)
similarly force (x_b=x_c) and (x_c=x_a).  Conversely, when all three
exterior coordinates equal (x), (4.5) and (4.6) are the same three sets
in cyclically permuted order. \(\square\)

Call a hexagon satisfying (4.4) a **common-exterior neutral hexagon**.  It
preserves the lower rainbow, every owner degree, and the complete
immediate-upper multiplicity vector, not merely upper surjectivity.

If its three deleted physical edges lie on three distinct factor cycles,
the toggle joins the three opened paths into one cycle and changes the
component count by (-2).  This is the primitive monotone merging move
available after the parity has been corrected.

## 5. Exact protection and residence locality

Contract the colour rows of a balanced factor (F), obtaining its physical
Johnson 2-factor (G_F).  For every required deeper upper target (Z), fix
one witnessing cyclic interval (W_Z) of (G_F).  Let (R) be the set of
physical edges deleted by one alternating switch.

### Lemma 5.1 (fixed-span protection)

If

\[
                         E(W_Z)\cap R=\varnothing       \tag{5.1}
\]

for every selected witness (W_Z), then all those witnesses remain literal
contiguous intervals after the switch.

#### Proof

Deleting (R) cuts (G_F) into retained path fragments.  Condition (5.1)
places every (W_Z) wholly in one retained fragment.  The switch changes
only the order and orientation in which fragments are joined; it does not
change adjacency inside a fragment. \(\square\)

Residence has an equally exact local formulation.  Let \({\cal B}\) be a
finite collection of forbidden binary words which is closed under reversal,
for example

\[
             {\cal B}_h=\{01^t0:1\le t<h\},          \tag{5.2}
\]

for minimum positive-run length (h).  For every coordinate (x), label a
physical owner by (1) when it contains (x) and by (0) otherwise.

### Lemma 5.2 (exact seam-DFA criterion)

Assume every cyclic coordinate word of \(G_F\) avoids \({\cal B}\).  After
cutting the switched edges into retained fragments, the new factor avoids
\({\cal B}\) if and only if the coordinate words of those fragments in
their actual new orientations, concatenated around every new cyclic
component **including its closing seam**, are accepted by the finite
forbidden-word automaton for \({\cal B}\).

Every newly created forbidden occurrence crosses a new seam.  If every
retained fragment has length at least

\[
                   L_{\cal B}-1,
  \qquad L_{\cal B}=\max_{w\in{\cal B}}|w|,             \tag{5.3}
\]

then a forbidden occurrence crosses at most one new seam, so the full
criterion reduces to the two (L_{\cal B}-1) collars at each seam.  Without
(5.3), multi-seam chains through short fragments must be composed; pairwise
seam tests are not sufficient.

#### Proof

Because \({\cal B}\) is reversal-closed, every word wholly inside a retained
fragment, in either allowed orientation, occurred before the switch up to
reversal and is safe.  Thus a new forbidden word must cross at least one
seam, and exact cyclic automaton composition is necessary and sufficient.
A word of length at most \(L_{\cal B}\) cannot cross two seams when the
intervening fragment has length at least \(L_{\cal B}-1\). \(\square\)

For a forbidden language which is not reversal-closed, the same criterion
is valid only after separately checking that every retained fragment is
internally accepted in its chosen orientation.  Without this check,
reversal can create an internal forbidden word which crosses no seam.

The last assertion explains the observed `010/0110` endpoint failure:
`0|1|0` and `0|11|0` can cross two seams through one- and two-letter
fragments although both individual seam pairs pass.

### Theorem 5.3 (zero-defect neutral-hexagon switch)

Let (F) be a balanced factor with complete immediate-upper multiplicity
vector, selected deeper witness intervals (W_Z), and residence language
({\cal B}).  Let (H) be a currently alternating common-exterior neutral
hexagon.  Suppose:

1. every selected deeper witness satisfies (5.1); and
2. the exact post-toggle fragment composition passes Lemma 5.2 for every
   coordinate.

Then toggling (H) preserves, with zero defect,

* every owner degree and every lower colour;
* the entire immediate-upper multiplicity vector;
* every selected deeper target; and
* the residence condition.

If the old hexagon edges lie on three distinct cycles, the toggle also
reduces the component count by exactly two.

#### Proof

Degree and lower-colour preservation is the alternating-hexagon identity.
Theorem 4.1 preserves the immediate-upper multiset.  Lemmas 5.1 and 5.2 give
the deeper and residence conclusions.  Cutting one edge from each of three
cycles gives three paths; the opposite cyclic half joins them into one
cycle, proving the last assertion. \(\square\)

This is a true plateau move: all protected defect counts remain zero while
the topology changes.

## 6. The parity-absorber plus loose-tree theorem

A **protected parity absorber** is a currently alternating circuit \(A\)
of even half-length which satisfies the net upper-multiplicity, fixed-span,
and residence conditions of Section 5 and whose exact net topological
effect is

\[
                         c(F\triangle A)=c(F)-1.       \tag{6.0}
\]

Equivalently in the clean two-component case, it replaces exactly two
affected components by one and does not split any other component.  It need
not be a hexagon;
Theorem 2.2 says that it cannot be generated by a legal hexagon sequence
having the same endpoints.

### Theorem 6.1 (protected monotone Hamiltonization)

Let (F) be a protected balanced factor with (c) components.

* If (c) is even, assume there is a protected parity absorber whose toggle
  gives a protected factor (F_0) with (c_0=c-1) components.
* If (c) is odd, put (F_0=F) and (c_0=c).
* Assume there are ((c_0-1)/2) successively legal switches
  (H_1,\ldots,H_{(c_0-1)/2}), each a zero-defect neutral hexagon in the
  current factor, and each having its three old physical edges on three
  distinct current components.

Then these switches produce one protected Hamilton component.  At every
intermediate factor all lower colours, all immediate-upper multiplicities,
all selected deeper witnesses, and residence remain valid, while the
component count strictly decreases.

#### Proof

The optional absorber changes (c) to the odd number (c_0) and preserves
all protected data by definition.  Each application of Theorem 5.3 changes
the component count by (-2) and preserves the same data.  After
((c_0-1)/2) applications the count is one. \(\square\)

A convenient static sufficient form is a loose spanning tree in the
3-uniform hypergraph whose vertices are the current factor components and
whose hyperedges are protected neutral hexagons with pairwise-disjoint
**extended supports**.  The extended support consists of the six hexagon
incidences together with the three exterior-owner incidences in (4.2).
Equivalently, no earlier toggle may change any later hexagon's three exterior
owners.  Order the loose-tree edges so that the first contains three old
components and every later edge contains one already joined component and
two new components.  Exact sequential residence-DFA acceptance remains a
separate hypothesis unless the switch collars are separated enough for
Lemma 5.2 to make them independent.  Disjointness of only the six cycle
edges is insufficient: two hexagons may share a lower row, and the first
toggle can then destroy common-exterior neutrality of the second.

Theorem 6.1 is parity-sharp for this monotone C6 architecture: without a
parity-changing step its conclusion is impossible for even \(c\).

## 7. Correction to the guard-intersection nerve

For a paired guard (K), let

\[
 {\cal F}(K)=\{F:F\text{ is balanced and }K\subseteq F\}.
\]

Each nonempty ({\cal F}(K)) is connected by guard-disjoint compound
alternating circuits: decompose the symmetric difference of two members.
If ({\cal F}(K\cup K')\ne\varnothing), the two fibres intersect.  Therefore
connectivity of the guard-intersection graph is a valid **sufficient**
condition for connectivity of the union of its fibres.

The converse is false.  Use (H,E) from Section 3.  Let (K_H) be the
paired physical guard at row `13` with owners `123,134`, and (K_E) the
paired guard at the same row with owners `123,135`.  Both fibres are
nonempty, but

\[
                  {\cal F}(K_H\cup K_E)=\varnothing,    \tag{7.1}
\]

because their union has degree three at row `13`.  Nevertheless the single
alternating circuit (3.5) carries \(H\in{\cal F}(K_H)\) to
\(E\in{\cal F}(K_E)\).  Thus disconnected components of the
guard-intersection nerve need not be disconnected components of the full
protected switch space, even for a two-state catalogue.

### Proposition 7.1 (correct nerve statement)

The guard-intersection nerve certifies routes obtained by moving inside one
guard fibre and passing between fibres at a common protected factor.  Under
the additional **transition-refinement** hypothesis

> the endpoints of every allowed protected circuit toggle lie together in
> at least one catalogue guard fibre,

every protected route induces a path in the nerve.  For the nerve to
classify protected connected components in both directions one must also
assume: the catalogue covers every protected state under discussion; the
protected part of each guard fibre is connected by allowed protected
circuits; and every asserted intersection contains a factor satisfying the
common protected predicate, not merely the balanced degree equations.

Without transition refinement one must add a transition edge
\(K\leadsto K'\) whenever an allowed net-protected circuit has one endpoint
in \({\cal F}(K)\) and the other in \({\cal F}(K')\).  The resulting
transition nerve, with the same catalogue-coverage and protected-
connectivity checks, not the intersection nerve alone, records protected
connectivity.

#### Proof

Sufficiency of an intersection edge follows only when the intersection
factor and the within-fibre routes carry the declared common predicate.
Under transition refinement, every edge of an arbitrary protected route is
contained in one catalogue fibre, so consecutive route edges give a chain
of intersecting fibres.  Catalogue coverage and protected within-fibre
connectivity give the converse construction.  The counterexample above
shows why transition refinement cannot be omitted. \(\square\)

## 8. PBBS and the fragment-braid CSP

PBBS supplies a balanced factor with selected all-depth witnesses.  It does
not automatically supply the protected switch bank of Theorem 6.1.  In
particular:

* a chosen witness may use a would-be deleted edge;
* a common-exterior neutral hexagon may fail to be currently alternating;
* the product residence automaton may reject a multi-seam chain even when
  every endpoint pair is Johnson and pairwise safe; and
* an even PBBS component count forces a longer parity-changing absorber.

For example, in the currently authenticated \(k=17\) certificate the
canonical PBBS factor has 146 components.  A
hexagon-only route can never turn it into one component.  The later
21-component endpoint has already crossed the parity class, so some
parity-changing compound transport is necessarily present in its history.

The exact fragment-braid search object suggested by the theorem is:

1. one parity-absorber variable when the current component count is even;
2. a bank of common-exterior alternating hexagons;
3. occurrence-labelled witness-span exclusions or explicit replacement
   ladders for every deeper target;
4. the complete coordinate-DFA summary, including chains through short
   fragments; and
5. a loose-tree/component-flow constraint on the selected switches.

Only after this carrier endpoint exists do the boundary-hole and common-cap
compiler constraints enter.  One sharp **sufficient carrier theorem** is
therefore the following; it is neither necessary nor a compiler theorem.

> **PBBS protected absorber-bank lemma (open).**  One can select an
> all-depth PBBS witness bank, a protected parity absorber when needed, and
> a loose spanning tree of common-exterior neutral hexagons such that all
> selected witness spans survive and every residence automaton accepts.

Theorem 6.1 shows that this lemma would give monotone zero-defect protected
Hamiltonization.  Sections 2--3 show that deleting the parity absorber from
this C6-based architecture makes it false for even component count.  Other
net-protected compound architectures may exist.  Nothing here proves the
remaining common-cap compiler theorem or the existence of the absorber
bank.

## 9. Audit boundary

Every theorem above is hand-derived.  No finite search, SAT solve, or web
source is used.  The (I(5,2)) factors are written out literally, so their
degree and upper-load claims can be checked from (3.1)--(3.4).  The note does
not claim:

* that hexagons connect one component-parity class;
* that common-exterior hexagons preserve deeper shadows without the fixed-
  span condition;
* that pairwise residence collars replace the full DFA in the presence of
  short fragments;
* that the PBBS protected absorber-bank lemma holds; or
* that protected Hamiltonization alone supplies a length-(B(k)) compiler.
