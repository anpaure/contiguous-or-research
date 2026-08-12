# Three-tag vertical parity: exact local crown and the fixed-base obstruction

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, or web input is used.

## 0. Verdict

There is a literal local saturated-chain realization of the canonical
three-tag binary parity obstruction in the **contracted vertical-option
system**.

Each tag has two arrival-diamond options.  For every pair of tags, equal
bits share one protected target, while unequal bits do not.  Thus an
integral collision-free choice would be a proper two-colouring of a
triangle and is impossible.  Giving the two options at every tag weight
(1/2) gives load exactly one on each of the six shared targets.  Every
one-bit diamond extends locally to a full commuting adjacent-switch cube,
and uniform cube measure retains the same (1/2,1/2) marginal.

This does **not** yet give an actual capacity-one protected-strip
multicover.  In the explicit realization, the three pairs of base chains
share three fixed source-prefix targets.  Each such target is present in
both options of two tags, so its load is two.

The fixed-base collision is unavoidable if complete source-prefix
incidence is counted.  More generally, whenever two arrival diamonds
realize both collision clauses of a binary pair constraint, their
saturated base chains coincide at at least one relevant rank.  The common
base target is fixed rather than optional.

Consequently:

\[
 \boxed{
 \begin{minipage}{0.84\linewidth}
 The three-tag parity gadget exists exactly after vertical-column
 contraction, but it cannot have all complete-incidence target loads at
 most one.  A protected-priority realization must hide every forced common
 base (and the analogous fixed endpoint prefixes).  Whether this can be
 done simultaneously with global return-free completion, all spectator
 cube faces, and no other cross-tag collision remains open.
 \end{minipage}}
\tag{0.1}
\]

Thus the local saturated-chain step is proved.  The gap is not Boolean
cube closure itself; it is the passage from the contracted option columns
to the full claimed path supports.

## 1. The binary parity table

Let the three tags be (A,B,C), with bits

\[
 x_A,x_B,x_C\in\{0,1\}.
\]

For each pair (ij\in\{AB,BC,CA\}), introduce two targets

\[
 T_{ij}^0,T_{ij}^1.
\]

Option (b) of tag (i) and option (b) of tag (j) both claim
(T_{ij}^b).  No unequal pair claims a common parity target.  A
collision-free integral choice would therefore require

\[
 x_A\ne x_B,\qquad x_B\ne x_C,\qquad x_C\ne x_A,
\tag{1.1}
\]

which is impossible.

Under the uniform rational choice

\[
 x_i(0)=x_i(1)=\frac12,
\tag{1.2}

every (T_{ij}^b) has load

\[
 \frac12+\frac12=1.
\tag{1.3}

This is the smallest contradictory implication cycle with exact unit
target loads.

## 2. Exact saturated-chain realization of the option columns

Fix a rank (k), a (k)-set (K), one label (t\in K), and five labels

\[
 p,q,s,a,b
\]

outside (K), all distinct.  Here (a,b) will be the two arrival labels;
(s\ne q) is a private upper increment.  Define three saturated
three-rank base-chain fragments by

\[
 \begin{array}{c|ccc}
 &k&k+1&k+2\\ \hline
 {\cal C}_A&K&K+q&K+p+q\\
 {\cal C}_B&K&K+p&K+p+s\\
 {\cal C}_C&K-t+p&K+p&K+p+q.
 \end{array}
\tag{2.1}

Every consecutive inclusion in (2.1) adds one element.  For
(\epsilon\in\{0,1\}), put

\[
 y_0=a,\qquad y_1=b,
\tag{2.2}

and define the corresponding vertical option targets by

\[
 V_i^\epsilon(\ell)
 =C^i_{\ell-1}+y_\epsilon,
 \qquad \ell=k+1,k+2,k+3.
\tag{2.3}

### Theorem 2.1 (local vertical parity crown)

Among the eighteen targets in (2.3), the only cross-tag equalities are

\[
 \boxed{
 \begin{aligned}
 V_A^\epsilon(k+1)=V_B^\epsilon(k+1)&=K+y_\epsilon,\\
 V_B^\epsilon(k+2)=V_C^\epsilon(k+2)&=K+p+y_\epsilon,\\
 V_C^\epsilon(k+3)=V_A^\epsilon(k+3)&=K+p+q+y_\epsilon,
 \end{aligned}}
\tag{2.4}

for (\epsilon=0,1).  Hence these three arrival diamonds realize the
parity table of Section 1 exactly.

#### Proof

The three displayed equalities are immediate from (2.1).  At rank (k),
the (C)-base (K-t+p) differs from (K).  At rank (k+1), the
(A)-base (K+q) differs from the common (B,C)-base (K+p).  At rank
(k+2), the (B)-base (K+p+s) differs from the common (A,C)-base
(K+p+q).  Thus there are no further same-option equalities.

Every base avoids (a,b).  A target with arrival (a) contains (a) and
not (b), while a target with arrival (b) contains (b) and not (a).
Therefore opposite options cannot coincide.  Targets at different ranks
have different cardinalities.  This exhausts all possibilities.
\(\square\)

The incidence graph of the six option rails is two disjoint triangles,
one for each (\epsilon).  The base chains route each triangle through
three different ranks, so no order-cycle contradiction occurs inside the
Boolean poset.

### Corollary 2.2 (literal one-diamond realization)

Assume the interval of controlled base ranks contains
(k,k+1,k+2).  Each fragment in (2.1) extends to a saturated chain

\[
 C_{m-Q-1}\subset C_{m-Q}\subset\cdots\subset C_{m+Q}
\]

avoiding (a,b).  With (a,b) placed in the residual block, the ordered
state construction for an arrival diamond realizes the two option columns

\[
 \bigl(C_{\ell-1}+a\bigr)_\ell,
 \qquad
 \bigl(C_{\ell-1}+b\bigr)_\ell.
\tag{2.5}

#### Proof

Extend downward by deleting unused elements and upward by adjoining unused
elements.  Only (O(Q)) labels are required, while (Q=o(m)).  For the
resulting full chain, take its first increment as the first departure,
the remaining increments as the ordered collar, and put (a,b) in the
residual block.  The complete arrival-diamond formula gives (2.5).
\(\square\)

The three carriers can be made distinct by adding different filler labels.
This proves literal local reachability of each of the six path templates.

## 3. Full local cube closure

Fix the distinguished adjacent arrival switch in each of the three
carriers.  Choose any collection of further disjoint adjacent phase pairs
away from its two updates.  Their transpositions commute, so every bit
vector is a legal zero-winding bounded-displacement trajectory.

The distinguished switch changes only its own intermediate phase column.
All spectator bits agree at that phase.  Consequently, under the uniform
measure on the full local (d)-cube,

\[
 \Pr(C_i^0)=\Pr(C_i^1)=\frac12,
\tag{3.1}

and every fixed phase column has mass one.  Equations (2.4) therefore keep
the exact loads (1.3) after full local cube closure.

Under (s=4) dynamic quarantine, the proved cube-boundary theorem retains
almost every fixed-radius face around almost every raw vertex.  Thus the
eight products of the three distinguished one-faces survive whenever the
three chosen faces are intact.  The theorem does not preserve an entire
(d=\Theta(m)) ambient cube, nor does it show that owner/priority
conditioning selects typical intact faces.

## 4. The fixed-base obstruction

The construction in Section 2 has fixed source-prefix collisions

\[
 C_A(k)=C_B(k)=K,
\tag{4.1}

\[
 C_B(k+1)=C_C(k+1)=K+p,
\tag{4.2}

\[
 C_C(k+2)=C_A(k+2)=K+p+q.
\tag{4.3}

These targets belong to the common source state of the corresponding
arrival diamonds.  They occur in both options and hence have tag mass one.
If complete source-prefix incidence is capacity constrained, each target
in (4.1)--(4.3) has total load two.

This is forced by a general two-tag lemma.

### Theorem 4.1 (two clauses force a common base)

Let

\[
 (A_r)_r,\qquad(B_r)_r
\]

be saturated chains, and let (a_0,a_1) be distinct labels absent from
every (A_r), while (b_0,b_1) are distinct labels absent from every
(B_r).  Suppose that for a permutation
(\sigma\in S_2) there are ranks (r,s) such that

\[
 A_r+a_0=B_r+b_{\sigma(0)},
\tag{4.4}

\[
 A_s+a_1=B_s+b_{\sigma(1)}.
\tag{4.5}

Then (A_u=B_u) for at least one of (u=r,s).

#### Proof

If (r=s), intersect the two equalities.  Since the two arrival labels are
absent and distinct,

\[
 (A_r+a_0)\cap(A_r+a_1)=A_r,
\]

while the intersection of the right sides is (B_r).  Hence (A_r=B_r).

Assume (r<s).  If (a_0=b_{\sigma(0)}), equation (4.4) immediately
gives (A_r=B_r).  Otherwise (4.4) implies

\[
 a_0\in B_r,
\]

and nestedness gives (a_0\in B_s).  But (a_0) is absent from (A_s),
and (a_1\ne a_0), so the left side of (4.5) omits (a_0), whereas its
right side contains (a_0).  This is impossible.  The case (s<r) is
the same argument with the two option labels interchanged.  Thus one of
the two common-base conclusions is unavoidable. \(\square\)

### Corollary 4.2 (no complete-incidence unit-load parity gadget)

Suppose each tag has total mass one on its two arrival-diamond options and
all common source-prefix targets are included among the capacity-one
resources.  If two tags realize the two collision targets of any binary
pair constraint, some fixed source target has load at least two.

Hence the three-tag parity table cannot be an all-target-load-one rational
point for complete arrival-diamond incidence.  The obstruction occurs
already on one tag pair; the contradictory triangle is not needed for this
negative conclusion.

## 5. What priority hiding would have to prove

The protected-column system does not necessarily claim every source
prefix.  Theorem 4.1 therefore leaves one possible escape: every forced
common base must be unclaimed by at least one of its two tags.

The local construction can place (4.1)--(4.3) strictly away from the
middle rank, where owners are mandatory.  One may then assign a large
radius to the distinguished intermediate phase and a smaller radius to
its source and endpoint phases.  This makes priority hiding locally
plausible.  It is not yet a global embedding theorem, for four reasons.

1. The common two-step endpoint also exposes fixed prefix chains.  Their
   cross-tag coincidences must be hidden together with the source bases.
2. The prescribed high- and low-radius phases must fit the exact global
   priority histogram in every carrier.
3. After adding the (d-1) spectator switches, every fixed and optional
   column in all three full cubes must avoid every unintended cross-tag
   protected equality.
4. The three local ordered states must extend to complete zero-winding,
   return-free carrier trajectories with those avoidance properties.

The existing coordinate-transitivity and cube-survival theorems prove
abundance before these simultaneous conditions are imposed.  They do not
prove the required conditioned extension count or face diffusion.

An exact positive embedding theorem would therefore have to construct
three carrier cubes for which

\[
 \mu(S)\le1
\tag{5.1}

for every claimed target (S), with equality on the six parity targets,
while all forced bases from Theorem 4.1 are absent from the claimed fixed
columns.  No current strip or cube theorem supplies this.

## 6. Exact status

Proved:

1. the contracted six-column parity table with unit rational target loads;
2. literal realization of its columns by three saturated arrival-diamond
   fragments;
3. local extension of each bit to a full commuting adjacent-switch cube;
4. the universal fixed-base theorem for every two-clause vertical pair;
5. impossibility when complete source-prefix incidence is capacity
   constrained.

Open:

1. simultaneous priority hiding of all forced source and endpoint bases;
2. a three-carrier return-free extension with no unintended protected
   collisions;
3. preservation of the required faces under the actual conditioned
   dynamic history.

Accordingly, the (s=4) cubes do not yet yield an actual parity
counterexample to protected rounding, but the only remaining escape from
the exact local obstruction is explicit: priority must remove the common
base shadows before the full path supports are compared.

## 7. Degree-(D) abstract cube audit and quantifier correction

The contracted obstruction has an exact degree normalization.  Let

\[
 D=2^d
\]

and put one full cube (Q_d) above each vertex of an odd cycle (C_n).
For every cycle edge (ij) and (b\in\{0,1\}), introduce one target
(T_{ij}^b), claimed by precisely the (b)-halfcubes at its two
endpoints.  Thus

\[
 d(U_i)=D,
 \qquad
 d(T_{ij}^b)=\frac D2+\frac D2=D.
\tag{7.1}
\]

Giving every cube vertex weight (1/D) gives load exactly one on every
tag and every displayed parity target.  Private targets used to distinguish
the remaining switch coordinates need only have load at most one; they are
not automatically saturated.  Two candidates on distinct tags meet in at
most one displayed target.  Hence their common protected family has width
at most one, the four-antichain quarantine graph is empty, and no vertex,
edge, or rectangle of the stipulated cubes is removed by that quarantine.

An integral matching which covered all (n) tags would assign one bit to
each cycle vertex and would have to alternate the bits on every cycle
edge.  This is impossible for odd (n).  Conversely, after omitting one
tag, the remaining path can be alternately labelled.  Therefore the exact
conclusion is

\[
 \boxed{\text{maximum integral tag coverage}=n-1.}
\tag{7.2}
\]

This should not be called an integral target cover: it is a maximum
matching, measured by the number of covered tag resources.

The degree-(D) model is an exact counterexample only to an implication
whose hypotheses are the contracted incidence data, full formal cube
closure, and four-antichain survival.  It is not a complete-incidence
arrival-diamond embedding.  By Theorem 4.1, every cycle edge that realizes
both parity targets also forces a fixed common base.  In a full
degree-(D) cube that base receives (D) occurrences from each endpoint,
so it has degree (2D) and uniform load two unless priority hides it.

Finally, the dynamic quarantine ledger at (s=4) is normalized as follows:

\[
 \xi_4=m^{-5+o(1)},\qquad \eta=m^{-4},
\]

and hence

\[
 E_{\rm tag}\le {W\xi_4\over\eta}
 =Wm^{-1+o(1)},
\tag{7.3}
\]

\[
 E_{\rm target}\le {WK\xi_4\over g\eta}
 \le W(2Q+1)m^{-1+o(1)}
 =Wm^{-1/2+o(1)}.
\tag{7.4}
\]

The quantifiers in (7.3)--(7.4) are

\[
 \text{for every admissible selected history }\mathcal S,
 \quad
 \text{there is an }\mathcal S\text{-dependent exceptional ledger}.
\tag{7.5}
\]

They do not produce one exceptional ledger which works simultaneously for
all possible histories.  In the abstract odd-cycle model itself the
four-antichain quarantine graph is empty, so its quarantine exceptional
ledger is actually zero; the unresolved conditioning issue concerns a
literal physical embedding.
