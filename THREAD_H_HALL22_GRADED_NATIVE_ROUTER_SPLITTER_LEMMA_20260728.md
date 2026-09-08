# Hall-22 graded native router/splitter lemma

Date: 2026-07-28

Status: unconditional grading, matching, Boolean-router, and final-controller
implication theorems; exact H23-to-H22 instance; orbit hitting remains
unproved.

## 1. Strongest correct conclusion

The native router/splitter mechanism has three logically separate parts.

1. A Boolean packet reassociation can be certified matching-rank neutral.
2. A local refinement of a unit DM circuit can add one matching rank while a
   right-disjoint exterior matching survives.
3. One final controller gives a literal common-Q conclusion only for the pins
   simultaneously certified against that controller.

For the frozen H23-to-H22 compound, parts 1 and 2 prove the global rank change

\[
16360\longrightarrow16360\longrightarrow16361.                 \tag{1.1}
\]

Part 3 proves one final-controller injection of 985 pins on the old
1007-target critical shore.  It does not prove that an arbitrary global
16361-edge matching is realized by one word.

For future Hall-22 descent, the exact missing assertion is not the implication
below but orbit hitting: a protected neutral route must reach a physically
graded splitter endpoint while retaining or regenerating the exterior and the
complete final common-Q ledger.

## 2. Native grading

Let

\[
T_0,T_1,\ldots,T_{W-1}\in\binom{[k]}r
\]

be a Johnson path,

\[
T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.                           \tag{2.1}
\]

Assume depth-d residence: every internal positive coordinate run in T has
length at least d+1.  Equivalently, whenever both sides are defined,

\[
\beta_i\ne\alpha_{i+t}\qquad(1\le t\le d).                      \tag{2.2}
\]

Define the clipped maximal erosion

\[
P_j=\bigcap_{i=\max(0,j-d)}^{\min(j,W-1)}T_i,
\qquad 0\le j<W+d.                                               \tag{2.3}
\]

An index \(j\) is fully interior when \(d\le j\le W-1\).  An edge
\(j\longrightarrow j+1\) is fully interior when \(d\le j\le W-2\).  The
distinction at the right endpoint matters: \(P_{W-1}\) still has full rank,
but the next controller state is already clipped.

### Theorem 2.1 (controller and native-trace grading)

For every fully interior vertex \(j\),

\[
|P_j|=r-d,                                                       \tag{2.4}
\]

and the flat interior of \(P\) is a Johnson path.  More precisely, for every
fully interior edge \(j\longrightarrow j+1\),

\[
P_j\setminus P_{j+1}=\{\alpha_j\},
\qquad
P_{j+1}\setminus P_j=\{\beta_{j-d}\}.                          \tag{2.5}
\]

Moreover, if 0\le s<d and every index in [p,p+s] is fully interior, then

\[
\boxed{
\left|\bigcup_{h=0}^{s}P_{p+h}\right|=r-d+s.}                  \tag{2.6}
\]

#### Proof

Across the d transitions from T_{j-d} to T_j, the deleted coordinates

\[
\alpha_{j-d},\ldots,\alpha_{j-1}                                \tag{2.7}
\]

are distinct.  Indeed, if \alpha_u=\alpha_v with u<v<u+d, then after its
deletion at u the coordinate must be reinserted at some transition q with
u<q<v.  Thus \beta_q=\alpha_v and 1\le v-q\le d, contradicting
(2.2).  The same argument shows that every coordinate in (2.7) was already
present in T_{j-d}: if \alpha_v were inserted inside the window, its
insertion-to-deletion gap would be at most d.

No coordinate inserted after T_{j-d} belongs to the intersection (2.3), and
every coordinate in (2.7) is absent from at least one state.  Hence

\[
P_j=T_{j-d}\setminus
\{\alpha_{j-d},\ldots,\alpha_{j-1}\},                            \tag{2.8}
\]

which proves (2.4).

The run ending with deletion \alpha_j contains
T_{j-d},\ldots,T_j by residence, so \alpha_j\in P_j and
\alpha_j\notin P_{j+1}.  Conversely, \beta_{j-d} is absent from
T_{j-d}, then is present throughout T_{j-d+1},\ldots,T_{j+1} by
residence.  Sliding the intersection window therefore gives (2.5).

For (2.6), each controller transition from P_{p+h} to P_{p+h+1} adds

\[
b_h=\beta_{p+h-d}.                                               \tag{2.9}
\]

The coordinate b_h is absent from T_{p+h-d}, one of the states occurring in
the intersection defining P_p, so b_h\notin P_p.  The b_h are pairwise
distinct: if b_t=b_h for t<h<d, then b_t is still present immediately before
the later insertion by (2.2), contradicting the Johnson requirement that
\beta_{p+h-d}\notin T_{p+h-d}.  Consequently

\[
\bigcup_{q=0}^{s}P_{p+q}
=P_p\cup\{b_0,\ldots,b_{s-1}\},                                 \tag{2.10}
\]

and (2.4) gives (2.6).  \(\square\)

Boundary controller positions are clipped and need not obey (2.4)--(2.6).

### Corollary 2.2 (physical cell bound and equality)

Suppose a physical word A satisfies D^d A=T.  Then A_j\subseteq P_j.  Hence
for a fully interior depth-s cell I=[p,p+s], 0\le s<d,

\[
\left|\bigcup_{j\in I}A_j\right|\le r-d+s.                     \tag{2.11}
\]

If equality holds, its target is necessarily the native trace

\[
\tau_P(I)=\bigcup_{j\in I}P_j.                                  \tag{2.12}
\]

#### Proof

Every A_j is contained in every middle target whose length-(d+1) window
contains j, hence in their intersection P_j.  Union containment and Theorem
2.1 give (2.11).  Under equality, the physical union is a subset of
\tau_P(I) with the same cardinality, so the two sets coincide.  \(\square\)

### Corollary 2.3 (the k=15 grading)

At \(k=15,r=8,d=3\), fully interior native traces have exactly the ranks

\[
\begin{array}{c|ccc}
\text{cell depth }s&0&1&2\\ \hline
|\tau_P(I)|&5&6&7.
\end{array}                                                       \tag{2.13}
\]

Therefore, among fully interior cells, a rank-six target has a native cell
only at depth one, and a rank-seven target has a native cell only at depth
two.  A rank-six target may occur nonnatively in a depth-two cell, but that
is not a native ear.  Clipped boundary cells are outside this grading claim
and must be checked against the protected endpoint collars.

## 3. The discarded depth-zero portal

On the frozen six-zero Hall-22 carrier, exact reconstruction gives

\[
\begin{array}{c|c|c|c|c}
\text{cell}&\text{depth}&\text{start}&\text{native trace}&\text{rank}\\ \hline
5617&0&5617&2574&5\\
17342&2&4467&2607&7.
\end{array}                                                       \tag{3.1}
\]

Here

\[
2575=2574\cup\{1\}                                              \tag{3.2}
\]

in one-based coordinate notation, so 2575 has rank six.  Cell 5617 is fully
interior.  By Corollary 2.2 it cannot realize 2575 in any depth-three
resident protected endpoint.  In the frozen graph its envelope is literally
2574, so the incidence 2575--5617 is absent.

Nor can a clipped depth-zero cell realize 2575 on this protected carrier.
Every left clipped controller state is contained in \(T_0=9901\), and every
right clipped state is contained in \(T_{W-1}=7779\), whereas

\[
\operatorname{mask}(2575\setminus9901)=2050\ne0,
\qquad
\operatorname{mask}(2575\setminus7779)=12\ne0.                \tag{3.3}
\]

Thus the projected alternating path

\[
2607-17342-2575-5617                                             \tag{3.4}
\]

is not a physical compiler portal.  It is discarded completely.

There is also a fixed-carrier monotonicity witness: middle target T_{5616}
omits coordinate 1, while physical position 5617 belongs to its four-letter
window.  Adding coordinate 1 at that position contaminates T_{5616}; an OR
cannot be repaired by deleting the coordinate elsewhere.

The controller incidence identity reinforces, but does not weaken, this
no-go.  For an exact middle deck at d=3,

\[
p_x=\binom{14}{7}-3i_x,                                         \tag{3.5}
\]

where p_x is the number of x-incidences in P and i_x is the number of
internal x-runs in T.  Between two exact resident deck orderings,

\[
\Delta p_x\equiv0\pmod3.                                       \tag{3.6}
\]

Also every fully interior controller state has rank five, so every local bit
gain forces a same-state bit loss.  Replacing 2574 by 2574\cup\{1\} violates
the state rank before (3.6) is even considered; deleting another required bit
keeps rank five but no longer realizes 2575.  No companion edit rescues a
depth-zero native 2575 trace at cell 5617.

## 4. Exact common-Q and native extension

Fix one final controller P and selected pins

\[
\Phi=\{(I_c,S_c)\}_c.
\]

Put

\[
K_p(\Phi)=P_p\cap\bigcap_{c:p\in I_c}S_c.                        \tag{4.1}
\]

### Lemma 4.1 (exact final-controller criterion)

There is one nonempty word A with A_p\subseteq P_p realizing every central
target and every selected pin if and only if:

1. K_p(\Phi)\ne\varnothing for every position p;
2. every coordinate of every central target occurs in some K_p in its
   central window;
3. every coordinate of every S_c occurs in some K_p with p\in I_c.

When these conditions hold, A_p=K_p(\Phi) is a simultaneous realizing word.

#### Proof

Every feasible A_p must lie in P_p and in every selected pin target whose
interval contains p, hence A_p\subseteq K_p.  This proves necessity of the
three nonemptiness/hit conditions.  Conversely choose A_p=K_p.  Containment
in P prevents excess coordinates in central windows, and containment in S_c
prevents excess coordinates in selected cells.  Conditions 2 and 3 supply
all required coordinates, while condition 1 makes every letter nonempty.
\(\square\)

### Lemma 4.2 (native extension is exact)

Let \Phi satisfy Lemma 4.1.  Add pins

\[
(J_a,R_a),\qquad R_a=\tau_P(J_a).                               \tag{4.2}
\]

Then the sets K_p do not change.  The enlarged family is common-Q feasible
if and only if

\[
J_a\cap\{p:x\in K_p(\Phi)\}\ne\varnothing
\quad(a,\ x\in R_a).                                             \tag{4.3}
\]

If every old pin is also native under P, then K_p=P_p and (4.3) is automatic.

#### Proof

For p\in J_a, P_p\subseteq\tau_P(J_a)=R_a.  Since K_p\subseteq P_p,
intersecting K_p with R_a changes nothing.  Thus all old constraints and
point nonemptiness are unchanged, and only the positive hits of the new pins
remain; these are exactly (4.3).  In the all-native case, every pin
intersection contains P_p, so K_p=P_p, and the definition of a native trace
gives every required hit.  \(\square\)

Equivalently, in the all-native incidence graph every native-eligible cell
has one native target.  It has right degree one, so a target family has a
native injection exactly when every target has at least one distinct-trace
preimage.  A clipped trace outside the compiler's target ranks contributes
no incidence.  Pins on overlapping intervals cause no conflict: the same
word \(P\) realizes all of them.

## 5. Unit-circuit refinement

Let D=(X,Y) be a unit transversal circuit:

\[
|X|=|Y|+1,
\qquad
X\setminus\{x\}\text{ matches bijectively to }Y
\quad(x\in X).                                                    \tag{5.1}
\]

### Lemma 5.1 (exact binary refinement criterion)

Replace y\in Y by two cells y_0,y_1.  The refined component saturates X if
and only if there are distinct

\[
x_i\in N(y_i)\cap X\quad(i=0,1)                                 \tag{5.2}
\]

such that X\setminus\{x_0,x_1\} matches to Y\setminus\{y\}.

#### Proof

A perfect refined matching uses both new cells because the two sides now
have equal size.  Delete their two matching edges to obtain the stated
residual matching.  Conversely append the two edges to that residual
matching.  \(\square\)

### Theorem 5.2 (every genuine shore partition perfects)

For every nonempty partition

\[
N_D(y)=A\mathbin{\dot\cup}B,                                    \tag{5.3}
\]

replacing y by children with shores A,B saturates X.

#### Proof

Delete y and let M be the transversal matroid on X represented by
Y\setminus\{y\}.  It has rank |X|-2: for any x, match X\setminus\{x\}
onto Y and delete the edge using y.  Therefore M^* has rank two, and a pair
\{u,v\} is a basis of M^* exactly when X\setminus\{u,v\} matches to
Y\setminus\{y\}.

For every x\in X, a matching of X\setminus\{x\} onto Y matches y to some
z\in N_D(y), so \{x,z\} is a basis of M^*.  Hence M^* has no loops, and
N_D(y) contains a basis.  If no pair a\in A,b\in B were a basis, every
cross-pair would be dependent.  In a loopless rank-two matroid, two distinct
dependent elements are parallel.  Fixing one element on each side and using
transitivity of parallelism would put A\cup B=N_D(y) in one parallel class,
contradicting that N_D(y) contains a basis.  A cross-basis \{a,b\} and its
residual matching satisfy Lemma 5.1.  \(\square\)

This closes the abstract polarization problem for all 15 nonloop Hall-22
components.  It does not produce a physical braid or a final common-Q word.

### Corollary 5.3 (graded nested 2/1 native ear)

At \(k=15,d=3\), let

\[
C=\{R,R^+\},\qquad R\subset R^+,\quad |R|=6,\quad |R^+|=7.  \tag{5.4}
\]

Suppose a fully interior depth-two cell \(c^+\) is available for \(R^+\)
and is also adjacent to \(R\).  If a distinct unused fully interior depth-one
cell \(c^-\) has native trace \(R\), then \(C\) is
perfectly matchable by

\[
c^-\mapsto R,qquad c^+\mapsto R^+.                             \tag{5.5}
\]

Both pins are native under the same final controller when \(c^+\) has native
trace \(R^+\).  The depth assignments in (5.5) are forced within the fully
interior all-native architecture by Corollary 2.3.

For the six-zero circuit \{2575,2607\}, cell 17342 is the required depth-two
native 2607 cell and is also adjacent to 2575.  A valid native augmentation
of the stipulated all-native flat-interior form must therefore find a
distinct depth-one cell \(c\) with

\[
\tau_P(c)=2575.                                                  \tag{5.6}
\]

Relative to the exceptional matching \(17342\mapsto2575\), this gives the valid
augmenting path

\[
2607-17342-2575-c,                                               \tag{5.7}
\]

which flips to the two native assignments in (5.5).  In the common-Q ledger,
the exceptional nonnative pin is removed before the two native pins are
inserted; the resulting shore family is all-native under \(P\).  Existence of
\(c\) is not proved.

## 6. Boolean packet rotation

Let a unit circuit have common right core \(Z\) and two packet cells whose
component-restricted old shores are

\[
U\cup V,qquad W,qquad V\ne\varnothing.                        \tag{6.1}
\]

Replace them by

\[
V,qquad U\cup W.                                                \tag{6.2}
\]

### Lemma 6.1 (automatic unpointed rank neutrality)

The reassociation (6.1)--(6.2) preserves the component matching rank.

#### Proof

Choose r\in V and match every target except r to all old right cells.  Let
the U\cup V cell use a and the W cell use b; retain every core edge.  If
a\in V, the new V cell can still use a and the new U\cup W cell can use b.
If a\in U\setminus V, use the new V cell on r and the new U\cup W cell on a;
b becomes the exposed target.  In either case all right cells remain
saturated, and their unchanged number is an upper bound on rank.  \(\square\)

For a prescribed root r, let

\[
\mathcal B_Z=
\{D\in\tbinom X3:X\setminus D\text{ matches to }Z\}.            \tag{6.3}
\]

The root is exposable in an orientation exactly when the two packet shores
contain distinct a,b with \{r,a,b\}\in\mathcal B_Z.  Thus scalar rank
neutrality does not imply preservation of a pointed root or even of the
unit-circuit property.  A fresh DM audit is required after a router.

## 7. Native router/splitter composition theorem

### Theorem 7.1

Let G_0,G_1,G_2 be compiler graphs on the same global target universe L.
Put

\[
\nu(G_0)=|L|-h=N.                                                \tag{7.1}
\]

Assume:

1. G_0\to G_1 is a protected neutral router: deck, Johnson legality,
   residence, the ordered middle endpoints and clipped endpoint collars,
   and every declared shadow support hold, and
   \nu(G_1)=N.  Lemma 6.1 may certify its local Boolean packet.
2. At G_1 a remote unit component C has an internal matching of size |C|-1,
   and G_2 contains a size-|C| matching on C after a refinement satisfying
   Lemma 5.1.
3. A matching of size N-(|C|-1) outside C survives or is rerouted onto cells
   disjoint from the perfected C matching.
4. G_2 retains a Hall shore of gap h-1.

Then

\[
\nu(G_1)=N,qquad\nu(G_2)=N+1,qquad h(G_2)=h-1.                 \tag{7.2}
\]

#### Proof

The exterior matching and the perfected component matching are disjoint and
have total size

\[
N-(|C|-1)+|C|=N+1.                                              \tag{7.3}
\]

Thus \nu(G_2)\ge N+1.  The gap-(h-1) shore gives
\nu(G_2)\le |L|-(h-1)=N+1.  Equality follows.  \(\square\)

The literal conclusion is separate.  Let S be a designated critical target
shore.  If one final controller P supplies a target/cell-injective pin family
on S consisting of a retained common-Q base plus native ears satisfying
Lemma 4.2, then that one final word realizes the enlarged S-matching.  If all
pins are native under P, the condition is automatic.  This does not make the
exterior matching in hypothesis 3 common-Q.

Only when the union of all shore pins and all exterior pins jointly passes
Lemma 4.1 against the same final \(P\) may the graph-rank conclusion and the
critical-shore literal conclusion be merged into one global literal matching
theorem.  Edgewise feasibility is insufficient because several pins may
jointly shrink one \(K_p\).

## 8. Exact finite instantiation and Hall-22 specialization

For the H23 neutral router, inside the 161/160 component rooted at 24610 put

\[
\begin{aligned}
U&=24610+\mathcal P(\{1,64\}),\\
V&=(24610+4096+\mathcal P(\{1,64\}))\setminus\{24610+4096\},\\
W&=\{u+4:u\in U\}.
\end{aligned}                                                    \tag{8.1}
\]

The restricted bank changes

\[
\{U\cup V,W\}\longrightarrow\{V,U\cup W\}.                   \tag{8.2}
\]

All additions in (8.1) are disjoint-bit additions, and all displayed shores
are restricted to the named DM component.  Lemma 6.1 proves local rank
neutrality.  The second braid makes no restricted change there and remotely
refines \{4877,4909\}.  Its final native cells have depths one and two and
traces 4877 and 4909, respectively, exactly as required by (2.13).

The global rank claim uses the following audited disjoint decompositions,
not merely the local packet calculation.  In the neutral step, a 160-edge
matching inside the 161/160 component is disjoint from a 16200-edge exterior
matching, and a retained gap-23 shore caps the rank.  In the splitter step,
the perfected two-edge matching on the 2/1 component is disjoint from a
16359-edge exterior matching, and a retained gap-22 shore caps the rank.
Thus the global ranks are exactly (1.1).  Separately, the final controller
realizes 985 native pins on the old 1007-target shore.

### 8.1 Standard Hall-22 carrier

At the standard frozen Hall-22 endpoint
`scratch/k15_segment_braid_hall22.json`, the canonical DM shore has size
1005/983 and is the disjoint union of 22 unit circuits:

\[
\begin{array}{c|l}
169/168&1920\\
161/160&960,8217,24610\\
160/159&449,8218\\
5/4&4213,7504\\
3/2&1103,18970\\
2/1&2420,2676,9524,17683,19568\\
1/0&2575,5801,13616,13620,17738,21641,29776.
\end{array}                                                       \tag{8.3}
\]

The 983 right cells have distinct native traces equal to every component
minus its intersection root, and the one H22 controller realizes all 983
simultaneously.  Among fully interior native ears, the nine nonloop rank-six
roots are grade-compatible only with depth one.  The six nonloop rank-four
roots cannot be added by a native ear at any interior compiler depth; they
require a nonnative common-Q rebase.  Fully interior rank-seven zero targets
require depth-two native creators.  Boundary ears require a separate
endpoint-collar check.

For a shore-local H22-to-H21 native descent it is therefore sufficient to
regenerate the 983-target native atlas and add one unused, grade-compatible
native target without collision, leaving a fixed-shore gap 21.  For the
global rank 16362 one additionally needs a disjoint exterior matching of

\[
16361-983=15378                                                  \tag{8.4}
\]

edges.  For a global common-Q theorem, those 15378 exterior pins must also
pass Lemma 4.1 jointly with the shore pins under the same final controller.

### 8.2 Six-zero Hall-22 carrier and the stipulated nested ear

The separate carrier `scratch/k15_segment_braid_hall22_zero6.json` has
canonical shore 1006/984.  Its component

\[
\{2575,2607\}/\{17342\}                                       \tag{8.5}
\]

has the exceptional common-Q assignment \(17342\mapsto2575\), with the other
983 shore pins native.  It also has the canonical all-native 984-pin basis,
which instead assigns \(17342\mapsto2607\) and exposes 2575.  Cell 17342 is
fully interior at depth two and has native trace 2607.  If a protected route
creates a distinct unused fully interior depth-one cell \(c\) with native
trace 2575, while regenerating the other 983 native shore pins and retaining
\(17342\mapsto2607\) under that same final controller, it extends the
canonical basis directly.  Equivalently, relative to the exceptional basis,
the alternating path (5.7) replaces the exceptional pin by

\[
c\mapsto2575,qquad 17342\mapsto2607.                           \tag{8.6}
\]

The resulting 985 shore pins are all native under one final controller.
For global rank 16362 this six-zero branch needs a disjoint exterior matching
of

\[
16361-984=15377                                                  \tag{8.7}
\]

edges, not 15378.  Equivalently, relative to the selected 2/1 component,
Theorem 7.1 needs a 16360-edge matching outside it: 983 other shore edges
plus these 15377 exterior edges.  A gap-21 shore must still cap the rank, and
a global literal theorem still requires the exterior pins and the 985 shore
pins jointly to satisfy Lemma 4.1.

## 9. Proved implication versus unproved orbit hitting

Theorems 2.1, 4.2, 5.2, 6.1, and 7.1 are implications with complete proofs.
They do not produce a route.

For the stipulated all-native flat-interior six-zero lane, the exact
remaining one-step Hall-22 gate is:

> Find one protected neutral route to a final state which regenerates the
> 983 other native shore pins, creates a free depth-one native 2575 cell,
> retains a depth-two native 2607 cell, retains or reroutes a 15377-edge
> exterior matching, retains a gap-21 shore, and makes the full exterior plus
> shore pin family pass the one-controller criterion of Lemma 4.1.  The
> ordered middle endpoints remain \(T'_0=9901,T'_{W-1}=7779\), equivalently
> the clipped endpoint collars remain protected.

The depth-zero cell 5617 is excluded permanently.  The frozen clipped
endpoint traces also exclude 2575 by (3.3), so the requested native ear must
be depth one while 2607 remains depth two.  No native 2575 cell currently
exists in the frozen six-zero carrier; the route must create one.

This is the smallest gate within the required all-native flat-interior
architecture.  It does not prove that every conceivable nonnative common-Q
rebase is impossible; those rebases are outside the lane fixed here.

No such H22-to-H21 endpoint is proved.  Nor is there a closed decorated
router chart reaching every remaining circuit, and strict conjugacy cannot
be universal because the component incidence types differ.  Hereditary
iteration requires the orbit-hitting property again after every discharge.

## 10. Audit artifacts

The exact finite claims use only frozen lightweight audits:

* scratch/k15_segment_braid_hall23.json;
* scratch/k15_segment_braid_hall23_portal.json;
* scratch/k15_segment_braid_hall22.json;
* scratch/k15_segment_braid_hall22_zero6.json;
* scratch/audit_k15_h22_router_splitter_structure.py;
* scratch/audit_k15_h22_router_splitter_common_q.py;
* scratch/k15_h22_router_splitter_common_q_certificate.json;
* scratch/threadD_h22_graded_split_mincut_base_audit.json;
* scratch/audit_k15_h25_native_dm_pins.py.

No local exhaustive search was run for this theorem.
