# Recyclable cube catalysts: an anchored exact no-go and an \(o(W)\) temporary-load bypass

Date: 2026-07-27

Method: pure mathematics only. No finite search, computation, solver, or
web input is used.

## 0. Exact outcome

Consider the degree-eight three-placeholder cube relation from
MATH_THEOREM_L_QUARTET_TORIC_MARKOV_OBSTRUCTION_20260726.md. Let

\[
W=\binom{2m}{m},\qquad
N_H=\binom{2m}{m+H},\qquad
M=m+H,\qquad
MN_H=(1+o(1))W,\qquad H=o(M).
\]

All asymptotic statements are along an integer sequence \(m\to\infty\)
with \(H=H(m)\ge2\) satisfying the displayed calibrated plateau
relation. In particular, \(M\ge16H\) eventually whenever that stronger
local hypothesis is invoked.

There are three inequivalent catalyst questions.

1. **Exact extra-column catalyst.** Every isolated cube has an explicit
   catalyst of four additional frame columns. Four physical quartets
   cross the cube and restore that catalyst exactly.
2. **Can that catalyst migrate?** No. Every quartet, every three-top
   conveyor, the six-frame mixed exchange, and every certified
   two-/four-/eight-top moving-hole exchange preserves the top
   multiplicity

   \[
   \mu_U=\sum_{\pi}x_{U,\pi}
   \]

   separately for every top \(U\). Hence the four extra columns are
   anchored to their four original tops and cannot be transported to a
   disjoint cube by the named move library. Installing this local bank
   independently on the dense cube packing costs

   \[
   \left(\frac12-o(1)\right)W
   \]

   retained middle incidences.
   Within one fixed rooted positional atlas, the only punctured versions
   certified for the three-top and six-frame exchanges leave the deleted
   slot at each top unchanged as well. Those fixed-atlas primitives do
   not transport a one-hole token. This statement is not invariant under
   a change of rooting or positional chart.
   For unpunctured three-top conveyors in one fixed chart, a private-edge
   parity ledger shows that restoring every outside catalyst orientation
   bit also restores every focal-star orientation bit. The favorable
   six-frame catalyst is even more rigid for the present purpose: its
   old seven-frame full-deck packet has exactly \(2H\) middle
   collisions; after one common phase deletion at least \(2H-3\)
   remain. It is therefore not a state of the squarefree exact factor.
3. **Temporary target-incidence defects.** If intermediate tables may
   violate target loads and the exception ledger is the cumulative
   \(\ell_1\) target-incidence variation, the same dense cube sector is
   traversable with total cost

   \[
   O(HN_H)=O\!\left(\frac HM W\right)=o(W).
   \]

   This path keeps one literal frame at every top and closes exactly
   after each cube, but it need not preserve the exact middle-owner
   matching at intermediate states. Its charge is target-load symmetric
   difference, not the literal whole-column occurrence charge.

Thus there is an exact invariant/no-go for **transporting an
extra-column catalyst**, but no coefficient-one obstruction in the
weaker temporary-incidence model. The still-open physical gate is
narrower:

> convert the anchored four-column catalyst into a bounded
> one-frame-per-top moving-hole token, route that token through the
> special \(\omega/\omega'\) base states of successive cubes while
> preserving squarefree middle ownership, and restore its complete
> all-depth load.

None of the existing moving-hole reports proves that conversion,
base-state alignment, or restoration theorem. No additive invariant is
proved that rules it out: the quartet characters do not see the cube
endpoint difference, and the normalized determinant-parity quotient
disappears after unrestricted conveyor images are admitted.

## 1. The isolated cube and its exact catalyst

Let \(\epsilon\in\{0,1\}^3\) index the eight cube tops. Choose
transpositions \(s,t\in S_3\) with

\[
\tau=st
\]

the placeholder three-cycle. Write \(x_{\epsilon,g}\) for the frame
variable at corner \(\epsilon\) with placeholder permutation \(g\).
The two isolated cube monomials are

\[
\begin{aligned}
T_0&=
\prod_{|\epsilon|\ {\rm even}}x_{\epsilon,1}
\prod_{|\epsilon|\ {\rm odd}}x_{\epsilon,\tau},\\
T_1&=
\prod_{|\epsilon|\ {\rm even}}x_{\epsilon,\tau}
\prod_{|\epsilon|\ {\rm odd}}x_{\epsilon,1}.
\end{aligned}
\tag{1.1}
\]

Define

\[
C_s=\prod_{|\epsilon|\ {\rm odd}}x_{\epsilon,s}.
\tag{1.2}
\]

It has degree four.

### Theorem 1.1 (four-frame restored catalyst)

There is a four-quartet path

\[
\boxed{T_0C_s\longrightarrow T_1C_s.}
\tag{1.3}
\]

Every intermediate monomial is nonnegative, every move is a literal
physical quartet with the common cube schedule, and the catalyst
\(C_s\) is restored exactly.

#### Proof

The transposition \(s\) acts on two placeholder families. Fixing the
third cube bit gives two disjoint \(s\)-faces. On each face, \(T_0C_s\)
contains the identity frame at the two even vertices and an added
\(s\)-frame at the two odd vertices. Apply the \(s\)-quartet on both
faces. The resulting monomial has

\[
s\text{-frames at every even corner},\qquad
1\text{- and }\tau\text{-frames at every odd corner}.
\tag{1.4}
\]

The transposition \(t\) acts on two families in the \(s\)-frame. Fixing
its untouched bit gives two \(t\)-faces. On each, use the \(s\)-frames
at the even vertices and the original \(\tau=st\) frames at the odd
vertices. The two \(t\)-quartets replace them by \(\tau\) at the even
vertices and \(s\) at the odd vertices. The untouched identity frames
at odd vertices remain. This is exactly \(T_1C_s\). \(\square\)

This gives a sharper saturation certificate than an unspecified common
monomial: four added frame copies and four quartet moves suffice.

## 2. The top-multiplicity invariant

For any nonnegative frame table \(x\), define

\[
\mu(x)=(\mu_U(x))_{U\in\binom{[n]}M},
\qquad
\mu_U(x)=\sum_{\pi\text{ on }U}x_{U,\pi}.
\tag{2.1}
\]

### Theorem 2.1 (all named exchanges preserve \(\mu\))

The vector \(\mu\) is preserved separately at every top by:

1. checkerboard quartets and higher placeholder cubes;
2. fixed-core cycle exchanges;
3. the three-top two-base conveyor;
4. the six-frame mixed-placeholder exchange;
5. the two-top moving-hole transfer; and
6. the squarefree four- and eight-top moving-hole cubes.

#### Proof

Every displayed exchange has the same touched top multiset on its two
shores and replaces exactly one frame column at each touched top by one
frame column on that same top. Summing the frame variables over one
fixed top therefore gives the same number before and after the move.
Composition preserves the equality. \(\square\)

### Corollary 2.2 (an extra-column catalyst cannot traverse)

Suppose a catalyst is represented by extra frame multiplicity above the
one-frame-per-top table. Under any sequence of the moves in Theorem 2.1,
the support and value of that excess top-multiplicity vector are fixed.
In particular, \(C_s\) from (1.2), supported on the four odd tops of one
cube, cannot become the corresponding catalyst on four tops of a
top-disjoint cube.

This is an exact integral invariant. Moving a deleted phase inside one
selected frame does not evade it: a moving-hole exchange changes the
frame state but not the number of selected columns at its top.

### Corollary 2.3 (dense permanent-bank cost)

The dense cube packing has

\[
G=\frac{N_H-o(N_H)}8
\tag{2.2}
\]

top-disjoint gadgets. Installing the explicit four-column catalyst on
every gadget uses \(4G\) extra columns. The exact incidence count depends
on the column convention. For the full frame variables used in Section
1, each added column has \(M\) middle-phase occurrences, hence

\[
4MG=\frac M2\bigl(N_H-o(N_H)\bigr)
=\left(\frac12-o(1)\right)W.
\tag{2.3}
\]

If all cube and catalyst columns are coherently repaired by deleting one
common positional phase, the four-quartet proof of Theorem 1.1 survives
after that common restriction. Each added column then has \(M-1\)
retained occurrences and

\[
4(M-1)G
=\frac{M-1}{2}\bigl(N_H-o(N_H)\bigr)
=\left(\frac12-o(1)\right)W.
\tag{2.3a}
\]

Thus this exact catalyst bank is not an \(o(W)\) permanent-incidence
repair in either convention.

Corollary 2.2 rules out literal support transport of the bank. It does
not rule out a more subtle protocol in which an anchored bank remotely
initiates a long chain of squarefree one-frame moves.

### Theorem 2.4 (fixed-atlas three-/six-frame moves do not move holes)

Fix, at every top under consideration, one rooted positional atlas and
require every composed move to use that fixed identification of its
slots. For a punctured frame table in this atlas, let

\[
\eta_U=\sum_{\pi\text{ selected on }U}e_{s(\pi)}
\tag{2.4}
\]

be the multiset of deleted positional phases at top \(U\). Checkerboard
quartets with a common deleted phase, the protected one-hole version of
the three-top conveyor, and the common-phase-deleted six-frame exchange
preserve \(\eta_U\) separately at every top.

Consequently no sequence using only these punctured fixed-atlas moves
can transport an anomalous slot-hole from one top-disjoint cube to
another.

#### Proof

In each certified punctured statement, the old and new column at a
touched top use the same positional deleted phase. The three-top theorem
requires a common phase whose derivative vanishes in both bases; the
six-frame identity permits an arbitrary common phase deletion; and the
quartet identity permits the same common retained-phase schedule on both
shores. Hence every summand in (2.4) is unchanged top by top. \(\square\)

The genuine two-/four-/eight-top moving-hole theorems deliberately use
different pattern-dependent holes and are outside Theorem 2.4.
Moreover, a positional slot has no canonical identification across two
unrelated rooted templates on the same top. Thus Theorem 2.4 gives no
global invariant for chart-changing compositions. If a hole is instead
identified intrinsically by its deleted physical target or terminal
label, even a common-slot placeholder swap can change that intrinsic
datum.

### Theorem 2.5 (fixed-chart private catalyst ledger)

Fix one \((M-2)\)-core \(D\), one outside apex \(x\), a set
\(\Lambda\) of other outside labels, and one rooted two-slot chart. Put

\[
S_u=D\cup\{x,u\},\qquad C_{uv}=D\cup\{u,v\}
\quad(u,v\in\Lambda).
\tag{2.5}
\]

Record in \(\mathbb F_2\) whether the two chart slots at each top have
been swapped. A three-top conveyor on \(x,u,v\) adds

\[
e_{S_u}+e_{S_v}+e_{C_{uv}}.
\tag{2.6}
\]

For a sequence of such fixed-apex conveyors let \(t_{uv}\) be the parity
with which \(x,u,v\) is used. Then

\[
\Delta C_{uv}=t_{uv},\qquad
\Delta S_u=\sum_{v\in\Lambda\setminus\{u\}}t_{uv}.
\tag{2.7}
\]

Hence

\[
\boxed{\Delta C_{uv}=0\ \forall uv
\quad\Longrightarrow\quad
\Delta S_u=0\ \forall u.}
\tag{2.8}
\]

In particular, a bank of outside orientation bits cannot be restored
while leaving a nonzero accumulated focal-star change in this fixed
chart.

#### Proof

The outside top \(C_{uv}\) belongs to exactly one triangle with the fixed
apex \(x\), so its change is \(t_{uv}\). The star top \(S_u\) belongs
to precisely the triangles \(x,u,v\), which gives the second identity.
If every outside bit is restored, every \(t_{uv}\) vanishes separately,
and therefore so does every star bit. \(\square\)

If the apex is also allowed to vary while the common core \(D\) and
chart remain fixed, every conveyor still toggles the three edges of one
triangle. Let \(r_{uv}\) be the parity with which the pair top
\(D\cup\{u,v\}\) is touched. Consequently the odd touched-edge graph is
Eulerian:

\[
\sum_{v\ne u}r_{uv}=0\pmod2
\qquad\text{for every outside label }u.
\tag{2.9}
\]

Both (2.8) and (2.9) are chart-local. Moving the common core lets a
former catalyst top reappear in a different role and escapes their
hypotheses.

## 3. Quartet characters do not detect the cube endpoints

The top-multiplicity invariant distinguishes catalyst locations, not the
two cube endpoints: \(T_0\) and \(T_1\) both have multiplicity one at
every cube top.

### Proposition 3.1 (cube endpoints defeat every quartet character)

Every homomorphism from the frame exponent group to an abelian group
which vanishes on all quartet vectors takes the same value on \(T_0\)
and \(T_1\).

#### Proof

The exponent difference \(T_1-T_0\) is the integral sum of the four
quartet vectors used after localization in Theorem 1.1. Apply the
homomorphism. \(\square\)

In particular, determinant parity, affine top characters, and every
unordered subset-slot census agree at the two endpoints.

This conclusion concerns additive homomorphisms which vanish on every
quartet vector. It does not exclude invariants of conformal
nonnegative applicability, special-base compatibility, chronology, or
moving-hole admissibility.

### Proposition 3.2 (unrestricted conveyors kill determinant parity)

Let \(D_M\) be the normalized physical quartet wedge lattice from
MATH_THEOREM_L_QUARTET_INTEGER_QUOTIENT_DENSE_MARKOV_NOGO_20260726.md,
so

\[
E_M/D_M\cong(\mathbb F_2)^n.
\]

Assume \(H\ge2\) and \(M\ge8H\), and allow unrestricted relabelling of
every certified three-top pattern, so all patterns used below are
available. Adjoin the normalized parity images of all those conveyors.
Then the enlarged image is all of \(E_M\); its determinant quotient is
zero.

#### Proof

Modulo two, a conveyor on

\[
C+\{x,y\},\quad C+\{x,a\},\quad C+\{a,y\}
\]

has top support

\[
e_{C+xy}+e_{C+xa}+e_{C+ay}.
\tag{3.1}
\]

Fix an \((M-3)\)-set \(D\) and four labels \(1,2,3,4\notin D\). The
four triangle supports obtained by taking cores
\(D+1,D+2,D+3,D+4\) give, on the four basis tops

\[
A=D+123,\quad B=D+124,\quad
C'=D+134,\quad D'=D+234,
\]

the relations

\[
A+B+C'=0,\quad
A+B+D'=0,\quad
A+C'+D'=0,\quad
B+C'+D'=0.
\tag{3.2}
\]

They force \(A=B=C'=D'=0\) over \(\mathbb F_2\). Relabelling kills
every basis top. Thus the conveyor classes span \(E_M/D_M\).
\(\square\)

This is only a lattice statement. A certified conveyor is applicable
only when its three current frames realize the special paired bases
\(\omega,\omega'\). Equation (3.2) does not manufacture those bases or
a nonnegative path.

## 4. What the moving-hole theorems actually transport

The exact all-depth derivative sizes of the audited primitives are:

\[
\begin{array}{c|c|c}
\text{primitive}
&\text{two-sided untagged }\ell_1\text{ action}
&\text{middle status}\\ \hline
\text{two-top moving hole}&6H-4&H-1\text{ repeats}\\
\text{four-top moving hole}&12H-8&\text{squarefree}\\
\text{eight-top moving hole}&24H-16&\text{squarefree}\\
\text{three-top conveyor}&8H(H+1)&\text{squarefree}\\
\text{six-frame mixed exchange}
&16H^2+8H-8&\text{old collar collides}.
\end{array}
\tag{4.1}
\]

Here “action” is derivative support/\(\ell_1\) mass in the protected
rows, not the much larger physical column footprint.

The two-top seam really does exchange its left- and right-hole states
between two adjacent tops, but its \(H-1\) repeated middle owners prevent
its direct insertion into a squarefree factor. The four- and eight-top
moving-hole cubes are squarefree, but require their special long-run
patterns and pattern-dependent hole terminals. The three-top conveyor
requires its special \(\omega,\omega'\) bases. It can act as a literal
bounded-collateral port catalyst, but it does not move or restore a
pre-existing catalyst column. Theorem 4.3 of
MATH_THEOREM_THREE_TOP_CONVEYOR_PORT_CATALYSIS_AND_CORE_REORDERING_20260727.md
proves more precisely that, when \(M\ge16H\), three conveyors through
one far buffer realize any prescribed transposition on one focal frame,
using six distinct companion tops and at most

\[
18(H+\delta-1)
\tag{4.1a}
\]

ordered-port edits at protected depth \(\delta\le H\). Exact middle
squarefreeness is preserved after every step if the seven prescribed
source frames occur, but the six companions finish in their opposite
states. This is a bounded-collateral theorem, not a closed catalyst
route. Equations (2.8)--(2.9) explain why the companions cannot simply
be restored inside one fixed chart; changing common cores escapes those
equations but supplies no restoration theorem.

The six-frame collar descent consumes an existing collision fan;
restoring the original collar restores the collisions and cancels the
gain. Its favorable seven-frame old full-deck shore already has \(2H\)
middle collisions, so it is not an exchange between two states of a
squarefree exact factor.

### Proposition 4.1 (the six-frame catalyst is excluded from the exact fibre)

At the full middle row, the favorable six changed frames together with
their fixed closing catalyst contain exactly \(2H\) unordered colliding
target pairs and no target of multiplicity three. The new seven-frame
packet is pairwise disjoint.

After deleting one common positional phase from every frame, at least

\[
2H-3\ge1
\tag{4.1b}
\]

of the old packet's collision pairs remain, whereas the restricted new
packet stays pairwise disjoint. Hence neither the full nor the
coherently one-phase-repaired favorable old packet can occur inside a
squarefree exact middle-owner factor.

#### Proof

This is Proposition 5.3 of
MATH_THEOREM_SIX_FRAME_MIXED_PLACEHOLDER_RECTANGLE_AND_MINIMALITY_20260726.md
at \(h=H\) for the full decks. Only the fixed closing frame and the two
endpoint frames participate in the \(2H\) collision pairs. One common
phase deletion removes at most one occurrence from each of those three
frames and therefore destroys at most three collision pairs. Restriction
cannot create a collision in the new packet. Since \(H\ge2\), (4.1b)
proves the repaired squarefree exclusion. \(\square\)

This repaired conclusion requires the certified common-phase deletion.
No exclusion is asserted for arbitrary independently chosen holes; that
punctured six-frame identity is not available.

Most importantly, the full/common-hole cube rigidity theorem says:
within a common-base checkerboard cube, restoring a common hole while
preserving the middle load returns to the all-lower-depth load-neutral
class. A serial moving-hole catalyst must therefore carry nontrivial
hole/base monodromy between gadgets or use a new non-common-base
connector.

Consequently none of the existing reports proves a squarefree
one-frame-per-top route

\[
\text{cube catalyst at }G_i
\longrightarrow
\text{cube catalyst at }G_{i+1}
\tag{4.2}
\]

with the outer all-depth defect restored.

### Naive three-top cumulative scale

Using one independent three-top conveyor per dense cube would cost

\[
G\cdot8H(H+1)
=\bigl(1+o(1)\bigr)N_HH(H+1)
=\Theta\!\left(\frac{WH^2}{M}\right).
\tag{4.3}
\]

At the tuned height \(H^2\asymp m\log m\), (4.3) is
\(\Theta(W\log m)\), not \(o(W)\). This is an exact ledger for the naive
independent protocol, not a lower bound against telescoping or recycling.

By contrast, formally summing the derivative actions of \(G\)
top-disjoint catalogue copies of the squarefree eight-top moving-hole
primitive gives

\[
G(24H-16)\le N_H(3H-2)
=O\!\left(\frac HM W\right)=o(W).
\tag{4.4}
\]

Top-disjointness alone does not prove that these copies coexist in one
squarefree exact factor: cross-packet middle-owner conflicts may remain.
Even if that packing gate were supplied, (4.4) would not connect the
isolated cube endpoints: its patterns and unequal holes are different
columns, and no alignment theorem is known.

## 5. A relaxed \(o(W)\) temporary-load bypass

The dense cube obstruction can be chosen with its three placeholder
positions at cyclic positions \(0,2,4\). They lie in three distinct
core gaps, so the within-cube ordered-core isolation proof and the
cross-gadget factorial union bound are unchanged. The three-cycle
\(\tau\) is a product of two transpositions, each of positional distance
two.

### Lemma 5.1 (short transposition incidence bound)

Let \(\pi'\) be obtained from a rooted cyclic frame \(\pi\) by swapping
two positions at cyclic distance \(\delta\). For any proper interval
length and any retained positional phase set,

\[
\|c_{\pi'}-c_\pi\|_1\le4\delta.
\tag{5.1}
\]

The same bound holds after root complementation and in any one
positionally tagged row.

#### Proof

The starts of intervals containing one swapped position form a cyclic
arc, and the corresponding starts for the other position are its shift
by \(\delta\). Their symmetric difference has size at most
\(2\delta\). Only those intervals can change. Each changed occurrence
removes one target basis vector and adds one, contributing at most two
to \(\ell_1\). Phase restriction can only delete changed occurrences,
and complementation permutes target coordinates. \(\square\)

Assume that all eight cube corners use one common retained-phase set and
one common phase-to-row/tag map, as required by the phasewise cube
identity. Let \(R\) count all protected row/tag coordinates in which a
retained phase is recorded. In the standard untagged signed-window
system,

\[
R\le2H+1.
\tag{5.1a}
\]

### Theorem 5.2 (temporary-defect traversal)

In the unrestricted frame catalogue, the two endpoints of every dense
degree-eight cube can be joined by changing its eight tops sequentially,
using the two distance-two transpositions for each top. The path has:

\[
\begin{aligned}
\text{cumulative variation per top}&\le16R,\\
\text{cumulative variation per cube}&\le128R,\\
\text{peak outstanding defect per cube}&\le128R.
\end{aligned}
\tag{5.2}
\]

After the eighth top is completed, every top row and every retained
common phase/length interval row closes exactly by the cube identity.
In particular, this includes the prescribed middle rows, all protected
depth rows, and every tag obtained from the same common positional
schedule. Over the whole dense packing,

\[
\boxed{
\text{total cumulative target-incidence variation}
\le16RN_H.}
\tag{5.3}
\]

If \(R=o(M)\), this is \(o(W)\). In particular, (5.1a) and \(H=o(M)\)
give the desired conclusion in the standard system. Even the sum of
the outstanding defect over all intermediate states is at most

\[
256RN_H,
\tag{5.4}
\]

which is likewise \(o(W)\) when \(R=o(M)\).

#### Proof

Lemma 5.1 with \(\delta=2\) gives cost at most eight in one row for one
transposition, hence at most \(16R\) for the two transpositions realizing
\(\tau\) or \(\tau^{-1}\) at one top. Sum over eight tops for (5.2) and
over all \(N_H-o(N_H)\) covered tops for (5.3).

At most sixteen single-transposition stages occur in one cube, and at
every stage the outstanding defect is bounded by \(128R\). There are
\((N_H-o(N_H))/8\) cubes, giving the safe bound (5.4). The exact
phasewise cube identity makes the outstanding derivative zero at the end
of each cube. Finally, since \(MN_H=(1+o(1))W\),

\[
RN_H=(1+o(1))\frac RM W=o(W)
\]
whenever \(R=o(M)\). In the standard system this follows from
\(R\le2H+1\) and \(H=o(M)\).
\(\square\)

This is a constructive traversal only in the temporary-incidence model;
it is not a sequence of exact toric exchanges. Intermediate tables
retain one literal cyclic frame at every top, but they need not have the
prescribed exact middle load or be squarefree. It is therefore not a
substitute for the missing moving-hole routing theorem inside one exact
factor.

The charge in (5.3) is cumulative \(\ell_1\) symmetric difference of
target-load vectors. It is not automatically the literal
exceptional-column incidence charge used in the permanent-frame
normalization. If every temporarily changed whole column is charged all
\(M\) occurrences, or \(M-1\) in the repaired model, changing
\(N_H-o(N_H)\) tops costs \(\Theta(W)\). Converting (5.3) into literal
recyclable occurrence capacity requires an additional compiler/reuse
lemma.

## 6. Exact boundary

Proved:

1. an explicit degree-four catalyst restored by four quartets;
2. exact top-multiplicity anchoring under the entire named exchange
   library;
3. the linear permanent-incidence cost of installing that catalyst on
   every dense cube;
4. fixed-rooted-atlas slot-hole anchoring for the certified punctured
   three-/six-frame moves;
5. the fixed-chart private-edge and star-parity obstructions to closed
   conveyor catalysts;
6. disappearance of the normalized determinant-parity quotient after
   unrestricted conveyor images are added;
7. the exact action ledgers and composition limitations of the existing
   moving-hole/conveyor theorems; and
8. an \(o(W)\) cumulative target-load-symmetric-difference path through
   all cube relations when temporary target-incidence defects are
   allowed.

Not proved:

1. that an anchored catalyst cannot influence remote cubes without
   moving its excess top support;
2. transport of a slot-hole through changing rooted charts or common
   cores;
3. conversion of the four extra columns into a squarefree
   one-frame-per-top hole token;
4. \(\omega/\omega'\)-compatible routing of such a token through the
   independently chosen cube templates;
5. exact all-depth restoration after that route;
6. conversion of the relaxed \(\ell_1\) load ledger into literal
   recyclable occurrence capacity and a contiguous-OR compiler; and
7. coefficient one.

The dense isolated-cube construction therefore closes neither side of
the remaining exact-factor gate. It does not obstruct the relaxed
\(o(W)\) target-load-symmetric-difference model, while the physically
integral moving-hole route remains a conformal base-compatibility
problem not resolved by any of the audited abelian invariants.
