# Native--laminar Shadow--Braid compiler, interval TU, and the first exact obstructions

Date: 2026-07-28

Status: proved exact fixed-braid compiler theorem, proved guarded package-Hall
corollary, and proved minimal obstructions.  This note does not construct the
middle braid or the lower-target injection required by the full induction.

## 0. Result and scope

The common-compiler gate has a useful exact positive solution.

The decisive distinction is not simply between laminar and crossing physical
intervals.  It is between two kinds of pins relative to the **final global
erosion controller**.

1. A controller-trace pin has label equal to the union of the controller
   states on its physical interval.  Such a pin is negative-inert.  Arbitrarily
   many trace pins may cross; the maximal erosion realizes all of them at
   once.
2. Every other pin is exceptional.  Exceptional pins delete controller
   occurrences.  If their intervals form a laminar, inclusion-monotone
   forest, their complete simultaneous effect is described by a tree atom
   condition, the exact controller port/gap condition, trace survival, and a
   point-core condition.

This yields an exact hybrid native--laminar Shadow--Braid compiler theorem.
It is stronger than a sectorwise compiler statement: it produces one literal
nonzero word on the final physical line.

There are two complementary integrality conclusions.

* For fixed labels, each coordinate-support problem is an interval hitting
  LP and is totally unimodular, even when the physical intervals cross.
  In fact feasibility is simpler than LP duality: the maximal allowed support
  is already integral.
* If exceptional pin packages are placed into short separated controller
  collars and each package passes the local atom/port/core tests, ordinary
  package Hall is sufficient for one common compiler.

Neither conclusion selects the full SB3 lower-target injection in an
unrestricted Pascal or diamond atlas.  The raw triangular atlas is interval
but not laminar.  The theorem closes SB4 for every fixed braid and pin
assignment satisfying its hypotheses; SB0--SB3 remain separate.

## 1. Exact controller-restricted common-pin kernel

Let (X) be a finite coordinate set and let

\[
 T=(T_0,\ldots,T_{W-1}),\qquad T_i\in {X\choose r},
\tag{1.1}
\]

be a depth-(d) resident Johnson chronology.  Put

\[
 L=W+d,
 \qquad V=\{0,1,\ldots,L-1\},
\tag{1.2}
\]

and define its maximal erosion controller

\[
 P_p=
 \bigcap_{\substack{0\le i<W\\i\le p\le i+d}}T_i
 \qquad(0\le p<L).
\tag{1.3}
\]

The empty intersection convention is never needed in (1.3).  Residence is
equivalent to

\[
 T_i=\bigcup_{p=i}^{i+d}P_p
 \qquad(0\le i<W).
\tag{1.4}
\]

Let

\[
 \Pi_0=\{(I_c,S_c):c\in C\}
\tag{1.5}
\]

be any finite family of extra exact pins, where every (I_c\subseteq V) is
a nonempty integer interval and (S_c\subseteq X).  We seek a nonzero word

\[
 A=(A_0,\ldots,A_{L-1})
\tag{1.6}
\]

such that

\[
 \bigcup_{p=i}^{i+d}A_p=T_i
 \quad(0\le i<W),
 \qquad
 \bigcup_{p\in I_c}A_p=S_c
 \quad(c\in C).
\tag{1.7}
\]

For each physical position define the controller-restricted label core

\[
 K_p=P_p\cap\bigcap_{c:p\in I_c}S_c,
\tag{1.8}
\]

where the intersection over no extra pins is (X).  For (x\in X), put

\[
 K_x=\{p\in V:x\in K_p\}.
\tag{1.9}
\]

### Theorem 1.1 (exact interval--controller compiler)

A nonzero word satisfying (1.7) exists if and only if all three conditions
below hold:

\[
 K_x\cap[i,i+d]\ne\varnothing
 \qquad(0\le i<W,\ x\in T_i),
\tag{1.10}
\]

\[
 K_x\cap I_c\ne\varnothing
 \qquad(c\in C,\ x\in S_c),
\tag{1.11}
\]

and

\[
 K_p\ne\varnothing
 \qquad(p\in V).
\tag{1.12}
\]

When they hold, the coordinatewise maximal compiler is

\[
 \boxed{A_p=K_p\qquad(p\in V).}
\tag{1.13}
\]

Every other compiler (B) satisfies (B_p\subseteq K_p) for every (p).

#### Proof

The central equalities in (1.7) force (B_p\subseteq P_p).  Indeed, if
(x\notin P_p), some central interval containing (p) has label omitting
(x).  Likewise, the pin (I_c\mapsto S_c) forces
(B_p\subseteq S_c) whenever (p\in I_c).  Hence every compiler is
contained in (1.8).

If (x\in T_i), its positive central occurrence must lie in
([i,i+d]\cap K_x), which proves (1.10).  The same argument for an extra
pin proves (1.11).  Nonzero source letters give (1.12).

Conversely, take (1.13).  Since (K_p\subseteq P_p), no coordinate outside
(T_i) occurs in the central interval ([i,i+d]).  Condition (1.10)
inserts every coordinate of (T_i), so its OR is exactly (T_i).
Similarly, (1.8) excludes every coordinate outside (S_c) from (I_c),
while (1.11) supplies every coordinate in (S_c).  Thus every extra pin is
exact.  Condition (1.12) makes the word literal and nonzero.  \(\square\)

### Relation to the exact (Q_x) criterion

The unrestricted common-pin allowed set is

\[
 Q_x=V\setminus\bigcup_{c:x\notin S_c}I_c.
\tag{1.14}
\]

The central pins restrict this to the controller support:

\[
 K_x=\{p:x\in P_p\}\cap Q_x.
\tag{1.15}
\]

Thus Theorem 1.1 is exactly the common-(Q_x) theorem after the central
row has been compressed to its maximal erosion.  No independent row
matching is being substituted for the common word.

## 2. Native trace pins and exceptional pins

For every physical interval (I\subseteq V), define its controller trace

\[
 \tau_P(I)=\bigcup_{p\in I}P_p.
\tag{2.1}
\]

### Definition 2.1 (native and exceptional pins)

A pin ((I,S)) is **native** if

\[
 S=\tau_P(I).
\tag{2.2}
\]

Every other pin is **exceptional**.

Fix a partition

\[
 \Pi_0=\mathcal N\sqcup\mathcal E
\tag{2.3}
\]

in which every member of (mathcal N) is native.  For (x\in X), put

\[
 B_x=
 \bigcup_{(I,S)\in\mathcal E:\ x\notin S}I,
 \qquad
 \widehat H_x=\{p:x\in P_p\}\setminus B_x.
\tag{2.4}
\]

### Lemma 2.2 (native pins are negative-inert)

If ((I,S)\in\mathcal N), then its negative requirements remove no point
from any controller support.  Precisely, for (x\notin S),

\[
 I\cap\{p:x\in P_p\}=\varnothing.
\tag{2.5}
\]

#### Proof

If (p\in I) and (x\in P_p), then
(x\in\tau_P(I)=S), contrary to (x\notin S).  \(\square\)

### Theorem 2.3 (exact native--exceptional compiler)

For an arbitrary exceptional family (mathcal E), one nonzero word
realizes the central row and every pin in (mathcal N\sqcup\mathcal E) if
and only if

\[
 \widehat H_x\cap[i,i+d]\ne\varnothing
 \qquad(i,\ x\in T_i),
\tag{2.6}
\]

\[
 \widehat H_x\cap I\ne\varnothing
 \qquad((I,S)\in\mathcal N\sqcup\mathcal E,\ x\in S),
\tag{2.7}
\]

and

\[
 \{x:p\in\widehat H_x\}\ne\varnothing
 \qquad(p\in V).
\tag{2.8}
\]

The canonical compiler is

\[
 \boxed{
 A_p=\{x:p\in\widehat H_x\}.
 }
\tag{2.9}
\]

#### Proof

By Lemma 2.2, native pins introduce no negative deletion beyond the
controller.  The exceptional negative requirements give exactly the sets
(B_x) in (2.4).  Hence (widehat H_x) is the maximal allowed support of
coordinate (x).  Conditions (2.6), (2.7), and (2.8) are respectively the
central positive hits, all extra positive hits, and physical nonzeroness in
Theorem 1.1.  \(\square\)

### Corollary 2.4 (all-native compiler)

If (mathcal E=\varnothing), the word (A=P) realizes the central row and
every native pin simultaneously, regardless of how their intervals cross.

#### Proof

There are no deletions, so (widehat H_x=\{p:x\in P_p\}).  Equation
(1.4) gives the central pins and (2.2) gives every extra pin.  \(\square\)

This corollary is the first substantive gain.  Crossing of canonical flag
intervals is not itself a common-compiler obstruction.  Only a pin whose
label differs from its trace can shrink the maximal word.

## 3. Exact laminar compression of the exceptional family

Assume from now on that the distinct intervals occurring in
(mathcal E) form a laminar family: two of them are disjoint or one
contains the other.  Pins on the same physical interval must have the same
label; otherwise no word can realize them, so identical copies are merged.

Write an exceptional pin simply as (I\mapsto S_I).  Exact feasibility
forces label monotonicity,

\[
 J\subsetneq I\quad\Longrightarrow\quad S_J\subseteq S_I,
\tag{3.1}
\]

because the OR on a subinterval is contained in the OR on its parent.  We
therefore impose (3.1).

For (p\in V), let (delta(p)) be the unique inclusion-minimal
exceptional interval containing (p).  If no exceptional interval contains
(p), use a formal root with label

\[
 S_{\delta(p)}=X.
\tag{3.2}
\]

Since the intervals through (p) form a chain and their labels are nested,
the maximal compatible word is

\[
 \boxed{A_p=P_p\cap S_{\delta(p)}.}
\tag{3.3}
\]

For an exceptional node (I), let (operatorname{ch}(I)) be its maximal
proper exceptional subintervals and define its physical atom

\[
 \operatorname{At}(I)
 =I\setminus\bigcup_{C\in\operatorname{ch}(I)}C.
\tag{3.4}
\]

### Lemma 3.1 (exact laminar atom criterion)

The maximal word (3.3) realizes every exceptional pin exactly if and only
if, for every exceptional node (I),

\[
 \boxed{
 S_I\setminus
 \bigcup_{C\in\operatorname{ch}(I)}S_C
 \ \subseteq\ 
 \bigcup_{p\in\operatorname{At}(I)}P_p.
 }
\tag{3.5}
\]

#### Proof

For (p\in I), the deepest exceptional label at (p) is contained in
(S_I).  Hence (A_p\subseteq S_I), so an exceptional pin can fail only
by losing a positive coordinate.

Proceed upward from the leaves of the laminar forest.  Fix (x\in S_I).
If (x\in S_C) for some child (C), then the inductive realization of the
child pin supplies (x) inside (C\subseteq I).  If (x) lies in no child
label, every point in a child interval forbids (x); it can occur in (I)
only on (operatorname{At}(I)), and it occurs there precisely when
(x\in P_p) at some atom point.  This is exactly (3.5).

Conversely, the same dichotomy shows that every (x\in S_I) occurs either
in a child or in the atom.  Thus the OR on (I) is (S_I).  \(\square\)

The atom condition is not a scalar capacity inequality.  It retains the
coordinate label and the exact physical laminar node at which that
coordinate stops descending.

### 3.1 Exact controller loss condition

For a coordinate (x), let

\[
 Z_x=\{p:x\in P_p\text{ and }x\notin S_{\delta(p)}\}
\tag{3.6}
\]

be the deleted part of its controller support.  Equivalently, (Z_x) is
the union, intersected with the controller support, of the first laminar
descendants whose labels omit (x).  These first-drop intervals are
pairwise disjoint.  Touching first-drop intervals must nevertheless be
coalesced before measuring a deleted component.

Let (R=[u,v]) be a maximal (x)-run in the controller (P).

### Lemma 3.2 (deleted-component form of the port/gap theorem)

The maximal support (R\setminus Z_x) realizes the corresponding carrier
run exactly if and only if

1. (u\notin Z_x) whenever (u>0);
2. (v\notin Z_x) whenever (v<L-1); and
3. every connected component of (Z_x\cap R) has at most (d) physical
   positions.

These clauses include all one-sided boundary cases.

#### Proof

For an internal controller run, the erosion port theorem forces both
endpoints and requires consecutive surviving positions to have distance at
most (d+1).  A deleted component of cardinality (s), lying between two
surviving positions, creates a gap (s+1); the gap condition is therefore
equivalent to (s\le d).

If (u=0), the left carrier run meets the physical boundary and its first
selected controller position may be as late as (d).  This is equivalent
to allowing an initial deleted component of size at most (d).  Its right
endpoint remains forced unless the controller run also reaches the right
physical boundary.  The right-boundary statement is dual.  If the run spans
both boundaries, its initial and terminal deleted components are each
allowed size at most (d), exactly as asserted.  \(\square\)

In particular, it is not enough to bound each bad pin interval separately.
Two disjoint but adjacent bad intervals form one larger deleted component.

### 3.2 Trace survival and point cores

For a native pin (c=(I,S)), equation (3.3) realizes it if and only if

\[
 \tau_A(I)=\tau_P(I),
\tag{3.7}
\]

or equivalently

\[
 I\cap\{p:x\in A_p\}\ne\varnothing
 \qquad(x\in\tau_P(I)).
\tag{3.8}
\]

A useful explicit certificate is to choose, for every native incidence
((c,x)), a protected position

\[
 a(c,x)\in I\cap\{p:x\in P_p\}
\tag{3.9}
\]

such that every exceptional interval containing (a(c,x)) has a label
containing (x).  Then (3.8) holds.  One may take the first or last
controller occurrence in (I); in the flat controller interior these are
incoming or outgoing ports unless they lie on the boundary of (I).

Physical nonzeroness is exactly the point-core condition

\[
 \boxed{P_p\cap S_{\delta(p)}\ne\varnothing
 \qquad(p\in V).}
\tag{3.10}
\]

### Theorem 3.3 (hybrid native--laminar Shadow--Braid compiler)

Let (T) be a fixed resident Johnson chronology, let (P) be its final
global erosion controller, let (mathcal N) be any family of native trace
pins, and let (mathcal E) be a laminar exceptional family satisfying
(3.1).  Then a common nonzero compiler exists if and only if all four
conditions hold:

1. the atom condition (3.5) holds at every exceptional node;
2. every native trace satisfies (3.7), equivalently (3.8);
3. every controller run satisfies the port/deleted-component conditions of
   Lemma 3.2; and
4. every physical position satisfies the point-core condition (3.10).

When these conditions hold, the single literal compiler is (3.3), has
length exactly (W+d), and realizes all pins simultaneously.

#### Proof

Nested labels make (3.3) the coordinatewise maximal word compatible with
all central and exceptional negative requirements.  Lemma 3.1 is exactly
the positive part of every exceptional pin.  Conditions (3.7)--(3.8) are
exactly the positive parts of all native pins, which are negative-inert by
Lemma 2.2.  Lemma 3.2 is equivalent to the central equality
(D^dA=T).  Finally, (3.10) is literal nonzeroness.  Apply Theorem 2.3.
\(\square\)

Thus Theorem 3.3 pays the common-compiler gate under its stated structural
hypotheses.  It does not return separate words for separate sectors.

## 4. A guarded short-collar theorem and package Hall

The exact run test admits a simple structural sufficient condition.

Let (R_1,\ldots,R_s) be the maximal roots of the exceptional laminar
forest.  Call them **guarded short collars** when

\[
 |R_j|\le d
 \qquad(1\le j\le s),
\tag{4.1}
\]

and, after ordering the roots from left to right, at least one physical
position outside every exceptional root lies strictly between consecutive
roots.

### Theorem 4.1 (guarded short-collar compiler)

Assume:

1. the exceptional roots are guarded short collars;
2. the exceptional labels are nested and satisfy the atom condition (3.5);
3. no exceptional pin omitting (x) contains a forced endpoint of a maximal
   (x)-run of (P);
4. every native incidence has a protected position (3.9); and
5. every point core (3.10) is nonempty.

Then (3.3) is one common nonzero compiler for the central row and all native
and exceptional pins.

#### Proof

Fix (x).  Every connected deleted component lies inside one exceptional
root.  Indeed, two different roots have an untouched separator; if one
maximal (x)-run meets both roots, (x) is present at every intervening
controller position and survives at that separator.  By (4.1), every
deleted component has size at most (d).  Hypothesis 3 preserves every
forced internal endpoint.  Lemma 3.2 therefore gives the central equality.

The atom condition realizes exceptional pins, the protected positions
realize native pins, and the point-core condition gives a nonzero word.
Theorem 3.3 finishes the proof.  \(\square\)

### Corollary 4.2 (thick traces survive automatically)

Suppose the controller run condition of Lemma 3.2 holds.  If a native
incidence ((I,x)) contains (d+1) consecutive physical positions of one
maximal (x)-run in (P), then (x) survives somewhere in (I).

#### Proof

Erasing all (d+1) positions would create a connected deleted component of
size at least (d+1), contradicting Lemma 3.2.  \(\square\)

The threshold is sharp: a deleted component of exactly (d) positions
creates a permitted gap of exactly (d+1).  Hence only thin native
incidences require explicit protected anchors once the run condition is
known.

### Corollary 4.3 (guarded package Hall)

Fix a family of physical slots (mathcal B), each an interval of at most
(d) positions, with an unused separator between consecutive slots.  Fix
the controller (P), all native pins, one protected position for every
native incidence, and all forced controller endpoints.

Let (mathcal G) be a family of exceptional laminar pin packages.  Join
(g\in\mathcal G) to (b\in\mathcal B) when the prescribed transplant of
the whole package (g) into (b)

1. has nested labels and satisfies the atom condition;
2. kills none of the fixed protected native positions or forced controller
   endpoints; and
3. leaves every point core inside (b) nonempty.

Assume (P_p\ne\varnothing) outside all slots.  If

\[
 |N(\mathcal G')|\ge |\mathcal G'|
 \qquad(\mathcal G'\subseteq\mathcal G),
\tag{4.2}
\]

then all packages can be installed simultaneously in one common compiler.

#### Proof

Hall's theorem gives a matching assigning distinct slots to all packages.
The transplanted package roots are short and separated.  Every local edge
certificate supplies the atom, port, protected-trace, and point-core
conditions in its slot; outside the slots there is no exceptional deletion.
The union therefore satisfies Theorem 4.1.  \(\square\)

This is a genuine Hall theorem for the common compiler.  Its right vertices
are disjoint physical package slots, not separate sectorwise copies of the
same positions.  The short-collar and guard hypotheses are substantive and
cannot be suppressed; Section 7 gives exact failures.

## 5. The interval LP and its exact dual

Laminarity is unnecessary for the coordinatewise support LP.  Return to an
arbitrary fixed pin system and its maximal allowed sets (K_x) from (1.9).
For each coordinate define the demand intervals

\[
 \mathcal D_x=
 \{[i,i+d]:x\in T_i\}
 \ \cup\ 
 \{I_c:x\in S_c\}.
\tag{5.1}
\]

The positive requirements on coordinate (x) are precisely that its chosen
support hit every member of (mathcal D_x).

Order (K_x=\{p_1<\cdots<p_t\}) physically, and let

\[
 M_x(J,j)=\mathbf 1_{\{p_j\in J\}}
 \qquad(J\in\mathcal D_x,\ 1\le j\le t).
\tag{5.2}
\]

### Theorem 5.1 (coordinate interval TU and min--max)

The matrix (M_x) is totally unimodular.  Consequently, provided every
demand interval meets (K_x),

\[
 \tau_x=min\left\{
 \sum_{p\in K_x}z_p:
 \sum_{p\in J\cap K_x}z_p\ge1\ (J\in\mathcal D_x),
 \ z_p\ge0
 \right\}
\tag{5.3}
\]

has a (0)-(1) optimum and

\[
 \boxed{
 \tau_x=max\bigl\{|\mathcal Q|:
 \mathcal Q\subseteq\mathcal D_x,\
 (J\cap K_x)_{J\in\mathcal Q}
 \text{ are pairwise disjoint}\bigr\}.
 }
\tag{5.4}
\]

Here disjointness is measured on the allowed positions (K_x); two physical
intervals may intersect only at forbidden positions.

#### Proof

In the induced physical order (p_1<\cdots<p_t), every row of (M_x) has
consecutive ones.  Equivalently, every column of (M_x^{\mathsf T}) has
consecutive ones.  Apply the Ghouila--Houri criterion to
(M_x^{\mathsf T}): for any selected set of its point rows, order those
rows physically and give them alternating signs.  The selected rows lying
in any interval form a consecutive subsequence, whose alternating signed
sum is (0), (1), or (-1).  Thus (M_x^{\mathsf T}), and hence (M_x),
is totally unimodular.

The covering LP (5.3) therefore has an integral optimum.  Its dual is

\[
 \max\left\{
 \sum_{J\in\mathcal D_x}y_J:
 \sum_{J\ni p}y_J\le1\ (p\in K_x),
 \ y_J\ge0
 \right\}.
\tag{5.5}
\]

Total unimodularity gives an integral dual optimum.  An integral feasible
dual is exactly a family of demands whose allowed-position traces are
pairwise disjoint, proving (5.4).  \(\square\)

### Corollary 5.2 (what TU does and does not prove)

For fixed pin labels, fractional feasibility of every coordinate support is
equivalent to integral feasibility.  More strongly, mere feasibility holds
if and only if

\[
 J\cap K_x\ne\varnothing
 \qquad(x\in X,\ J\in\mathcal D_x),
\tag{5.6}
\]

because the maximal integral support (K_x) then hits every demand.

This does not remove the point-core condition (K_p\ne\varnothing), and it
does not choose pin labels or target-to-cell assignments.  Changing an
assigned label changes many sets (K_x) simultaneously, so ordinary Hall
in the one-target projection is not the dual of that nonlinear choice.

Thus the legitimate roles are:

* interval TU sparsifies or budgets coordinate witnesses after the labels
  are fixed;
* guarded package Hall chooses among genuinely disjoint common physical
  slots;
* the common maximal-core theorem remains the authoritative feasibility
  test.

## 6. Calibration on canonical Pascal and diamond flags

For (0\le q\le d) and every valid start (i), the exact controller trace
identities are

\[
 \bigcap_{h=0}^{q}T_{i+h}
 =\bigcup_{p=i+q}^{i+d}P_p
 =\tau_P([i+q,i+d]),
\tag{6.1}
\]

and

\[
 \bigcup_{h=0}^{q}T_{i+h}
 =\bigcup_{p=i}^{i+d+q}P_p
 =\tau_P([i,i+d+q]).
\tag{6.2}
\]

Therefore every canonical lower or upper flag of the **final resident
chronology**, pinned on the physical interval displayed in (6.1) or (6.2),
is native.  The maximal erosion (P) realizes the complete canonical flag
tower simultaneously.  No laminarity is required for this conclusion.

The physical family is nevertheless not laminar.  For fixed (q<d), two
adjacent lower cells are

\[
 [i+q,i+d],
 \qquad
 [i+q+1,i+d+1],
\tag{6.3}
\]

which overlap and neither contains the other.  The central windows
([i,i+d]) and ([i+1,i+d+1]) already give the same crossing.  For a fixed
start (i), by contrast, the lower flag intervals form a nested chain, as
do the upper flag intervals.

Consequently the correct Pascal/diamond verdict is:

1. a same-start canonical flag package is laminar;
2. the full all-start triangular family is consecutive-ones but not
   laminar;
3. crossings among pins that remain final-controller traces are harmless;
4. a transported sector pin, seam pin, endpoint pin, fallback pin, or
   displaced target pin is exceptional whenever its label differs from the
   trace of the **final global** controller on its physical interval; and
5. only this exceptional family needs Theorems 3.3 or 4.1.

A label that is native for a sector-local controller need not be native
after the sectors are braided.  Mixed collars must always be recomputed
against the final global (P).  Pascal identities alone do not prove that
the resulting exceptional labels are laminar or nested.

## 7. Exact obstructions and sharpness

### 7.1 Smallest consecutive-ones obstruction to common nonzeroness

Take physical positions (V=\{0,1,2\}), coordinates (X=\{a,b\}), and
two pins

\[
 [0,1]\longmapsto\{a\},
 \qquad
 [1,2]\longmapsto\{b\}.
\tag{7.1}
\]

Then

\[
 Q_a=\{0\},
 \qquad
 Q_b=\{2\}.
\tag{7.2}
\]

Both positive requirements are hit, and the (2\times3) physical incidence
matrix

\[
 \begin{pmatrix}
 1&1&0\\
 0&1&1
 \end{pmatrix}
\tag{7.3}
\]

is consecutive-ones and totally unimodular.  Nevertheless position (1)
has empty common label core, so no nonzero word realizes both pins.

This template is minimal in the numbers of pins and positions among
crossing interval examples.  One pin with a nonempty label never forces an
empty position in its own interval; with at most two physical positions,
two intersecting nonempty intervals are nested or equal, not crossing.

Thus interval TU and all coordinate positive hits do not imply CP3.

### 7.2 Inclusion-minimal laminar split-cover obstruction

The atom condition remains necessary even when central residence and
physical nonzeroness survive.

Take (d=2), a coordinate (x), and distinct coordinates (y_j).  On a
long enough index interval define the resident rank-four Johnson path

\[
 T_i=\{x,y_i,y_{i+1},y_{i+2}\}.
\tag{7.4}
\]

Every nonboundary (y_j)-run has length (3=d+1), and (x) spans the
chronology, so the path is depth-two resident.  At every fully interior
controller index,

\[
 P_j=T_{j-2}\cap T_{j-1}\cap T_j=\{x,y_j\}.
\tag{7.5}
\]

Fix two consecutive fully interior indices (u+1,u+2).  Use the native
parent trace pin

\[
 I=[u+1,u+2]
 \longmapsto
 \{x,y_{u+1},y_{u+2}\},
\tag{7.6}
\]

and the two exceptional singleton children

\[
 \{u+1\}\longmapsto\{y_{u+1}\},
 \qquad
 \{u+2\}\longmapsto\{y_{u+2}\}.
\tag{7.7}
\]

The family is laminar and the labels are inclusion-monotone.  The maximal
word deletes (x) at (u+1,u+2) but keeps (x) at (u) and (u+3).
The surviving gap is

\[
 (u+3)-u=3=d+1,
\tag{7.8}
\]

so the exact central port/gap condition still holds.  Both singleton
letters are nonempty.  Yet the parent interval loses its positive
coordinate (x).  Its atom is empty and

\[
 x\in S_I\setminus
 (S_{\{u+1\}}\cup S_{\{u+2\}}),
\tag{7.9}
\]

which is precisely the failure of (3.5).

Removing any one of the three pins eliminates the failure.  Hence this is
an inclusion-minimal distinct-cell laminar split-cover obstruction.  It
also proves the sharpness of the (d+1) thick-trace threshold: a native
trace supported on only (d) consecutive controller positions can be
erased while central residence survives.

### 7.3 Adjacent short roots cannot be checked independently

The unused separator in Theorem 4.1 is substantive.  Here is a complete
depth-one resident Johnson example.

Let

\[
 \begin{aligned}
 T_0&=\{a,c,f,g\},\\
 T_1&=\{b,c,f,g\},\\
 T_2&=\{b,c,e,f\}.
 \end{aligned}
\tag{7.10}
\]

This is a Johnson path.  Every internal coordinate run has length at least
(2=d+1), so it is depth-one resident.  Its maximal erosion is

\[
 \begin{aligned}
 P_0&=\{a,c,f,g\},\\
 P_1&=\{c,f,g\},\\
 P_2&=\{b,c,f\},\\
 P_3&=\{b,c,e,f\}.
 \end{aligned}
\tag{7.11}
\]

Place the two disjoint singleton pins

\[
 \{1\}\longmapsto\{f,g\},
 \qquad
 \{2\}\longmapsto\{b,f\}.
\tag{7.12}
\]

Each pin separately admits a common central compiler.  Explicitly, for the
first pin one may take

\[
 (A_0,A_1,A_2,A_3)
 =(
 \{a,c\},\{f,g\},\{b,c\},\{e,f\}),
\tag{7.13}
\]

and for the second one may take

\[
 (A_0,A_1,A_2,A_3)
 =(
 \{a\},\{c,f,g\},\{b,f\},\{c,e\}).
\tag{7.14}
\]

With both pins imposed, coordinate (c) is deleted at positions (1) and
(2), so the central interval ([1,2]) has no (c).  Equivalently, the
two adjacent roots form a deleted component of size (2>d=1).

The pin intervals are disjoint and therefore laminar, each root has length
(d), and each one-pin target--cell compatibility test passes.  What fails
is exactly the separator/coupled-run condition.  Thus independent local
Hall edges cannot be composed across adjacent collars without retaining
the controller state.

## 8. Consequence for Shadow--Braid induction

Fix a decorated Johnson Shadow--Braid satisfying SB0--SB3, and compute its
maximal erosion controller from the final braided chronology.  Partition
its SB4 pins into final-controller trace pins and exceptional pins.

If the exceptional pins satisfy Theorem 3.3, then the word (3.3) proves SB4.
If instead they are chosen by a guarded package matching satisfying
Corollary 4.3, that matching proves SB4.  In either case the fixed-braid
Shadow--Braid theorem then gives the literal length-(W+d) word; at the
exact monotone deadline this is the claimed length (B(k)).

The proved implication is therefore

\[
 \boxed{
 \text{SB0--SB3}
 +\text{ native--laminar compiler certificate}
 \ \Longrightarrow\ \text{one exact Shadow--Braid word}.}
\tag{8.1}
\]

The following are not proved here.

1. The complete Pascal or diamond lower ideal admits an injective assignment
   whose exceptional pins are laminar or fit enough guarded slots.
2. Sector-local native labels remain native through every mixed final
   collar.
3. SB2 upper occurrences survive the cuts and reconnections.
4. An arbitrary target--cell Hall matching satisfies the common compiler.
5. The all-(k) or asymptotic coefficient-one conjecture.

The remaining constructive question is now precise: choose the braid and
SB3 injection so that every off-trace pin either becomes a final-controller
trace or enters a laminar/guarded exceptional package.  A bare
consecutive-ones matrix, sectorwise Hall matching, or pairwise collar audit
does not imply this.

## 9. Independent audit ledger

The decisive implications were checked independently in three forms.

1. **Maximality audit.**  Every feasible letter is contained in
   (P_p\cap\bigcap_{I\ni p}S_I); enlarging to this core cannot create a
   forbidden coordinate.  Therefore failure of a positive hit or point
   core at the maximal word is terminal.
2. **Laminar audit.**  At a point, containing exceptional intervals form a
   chain.  The deepest label is their intersection.  Induction on the
   laminar forest gives exactly (3.5); no coordinate is charged to two
   incomparable children.
3. **Run audit.**  Deleted intervals are coalesced after intersection with
   one maximal controller run.  A component of (s) deleted sites creates
   a surviving gap (s+1), including the one-sided prefix/suffix cases.
   This verifies the constant (d), not (d+1), in Lemma 3.2.

The examples in Section 7 independently isolate the three conditions which
could otherwise be conflated: CP3 point cores, laminar atom survival, and
cross-package controller gaps.
