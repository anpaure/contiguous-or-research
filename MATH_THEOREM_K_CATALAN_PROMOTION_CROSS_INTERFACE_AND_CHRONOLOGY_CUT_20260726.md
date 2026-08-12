# Catalan-to-promotion cross-interface: a component-colour obstruction and an all-depth chronology cut

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used. The component census from
`MATH_THEOREM_K_CATALAN_C8_COMPONENTS_VERSUS_SUPERPOLYNOMIAL_CORRELATION_SCALE_20260726.md`
is taken as audited input and is not recomputed.

## 0. Result

Put

\[
 V=[2m],\qquad M=m+H,\qquad
 W=\binom{2m}{m},\qquad
 N=\binom{2m}{m-H},\qquad
 R=\binom mH,
\tag{0.1}
\]

where

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 \frac{H^2}{m}=\log m+o(1),
\tag{0.2}
\]

and assume the packing-side calibration

\[
 (M-1)N\le W,\qquad MN=(1+o(1))W.
\tag{0.3}
\]

Let

\[
 C_m=\frac{W}{m+1}.
\tag{0.4}
\]

Then \(N=(1+o(1))C_m\).  The audited MSW overlay components on one
shore have side sizes

\[
 s_j=C_j+C_{j+1},\qquad 0\le j\le m-2,
\tag{0.5}
\]

with multiplicity \(C_{m-j-2}\).  If

\[
 j_*:=\min\{j:s_j\ge R\},
\tag{0.6}
\]

then the components with \(j\ge j_*\) contain

\[
 \left(\frac58+o(1)\right)C_m
\tag{0.7}
\]

rows, while the unique top component contains

\[
 \left(\frac5{16}+o(1)\right)C_m
\tag{0.8}
\]

rows.

This note proves four interface statements.

### A. Arbitrary relabelling cannot make the MSW components star-wide

Choose all but \(o(N)\) promotion roots and all but \(o(C_m)\) Catalan
rows and transfer the MSW component partition by an arbitrary bijection
between those subsets; treat the remaining roots as exceptional.  For fixed
\(0<\eta<3/8\), let \(\mathcal G_\eta\) be the middle targets \(D\) for
which some transferred component \(B\) satisfies

\[
 |B\cap\mathcal R(D)|\ge(1-\eta)R,
 \qquad
 \mathcal R(D)=\binom D{m-H}.
\tag{0.9}
\]

Then

\[
 \boxed{
 \frac{|\mathcal G_\eta|}{W}
 \le \frac{5/8+o(1)}{1-\eta}.}
\tag{0.10}
\]

If only the unique top component is used, \(5/8\) in (0.10) improves to
\(5/16\).  In particular, as \(\eta\downarrow0\), at least
\((3/8-o(1))W\) middle targets fail the almost-monochromatic-star
condition for the full unmerged hierarchy, and at least
\((11/16-o(1))W\) fail it for the top component alone.

Thus no map which keeps the individual MSW components as its promotion
dependency blocks can supply the targetwise block condition required by
the promotion block-factor theorem.  This statement is independent of
how the Catalan roots are relabelled as promotion roots.

### B. The literal owner-coloured interface has a stronger statewise defect

On one shore of an anchored Catalan factor, each component \(\lambda\)
contains \(s_\lambda\) rows and hence exactly

\[
 w_\lambda=(m+1)s_\lambda
\tag{0.11}
\]

primary middle owners.  Let \(E_\lambda\) be this owner block and define
\(\kappa(D)=\lambda\) when \(D\in E_\lambda\).  Colour each promotion
root \(A\) by one component \(b(A)\), write

\[
 n_\lambda=|b^{-1}(\lambda)|,
 \qquad
 g_D(b)=|\{A\subset D:b(A)=\kappa(D)\}|,
\tag{0.12}
\]

and define the root-star colour error

\[
 \operatorname{Err}(b)
 =\sum_{D\in\binom Vm}\bigl(R-g_D(b)\bigr).
\tag{0.13}
\]

Suppose the repaired decks respect component owner capacity up to total
\(o(W)\) leakage: there are \(e_\lambda\ge0\) such that

\[
 (M-1)n_\lambda\le w_\lambda+e_\lambda,
 \qquad
 \sum_\lambda e_\lambda=o(W).
\tag{0.14}
\]

Then

\[
 \boxed{
 \operatorname{Err}(b)
 \ge\left(\frac9{32}-o(1)\right)WR.}
\tag{0.15}
\]

More precisely, for \((3/8-o(1))W\) targets,

\[
 \boxed{g_D(b)\le\left(\frac14+o(1)\right)R.}
\tag{0.16}
\]

Consequently the capacity-constrained deletion-decoding problem exposed
by the mechanical clone-Hall atlas has a positive constant defect at the
root-star level.  A successful interface must abandon a
single MSW component colour on a positive-density sector, or fuse the
small components into new root-scale dependency blocks.  Quantitatively,
any asymptotically star-wide fusion must absorb at least
\((3/8-o(1))N\) roots from components originally below the scale \(R\).

### C. The phasewise lift exists, but exact component control becomes global

There is nevertheless an exact positive phasewise lift: the mechanical
clone-Hall matching, composed with the Catalan primary-owner bijection,
injects \(W-o(W)\) promotion phase clones into distinct literal Catalan
owner occurrences.  Every matched edge has a genuine one-phase
restriction certificate.

More strongly, for every incidence \(A\subset D\), the unique primary
owner row of \(D\), restricted to \(A^c\), is a literal promotion frame
in which \(D\setminus A\) is an \(H\)-window.  Both overlay shores give
such a witness, and both witnesses lie in the ownership component of
\(D\).  Thus every target-star is exactly component-monochromatic at
the **edge-witness** level.

This does not give one frame or one component colour per promotion root.
The bipartite inclusion graph on roots \(A\) and middle targets \(D\),
with edges \(A\subset D\), is connected.  Consequently, if one demanded

\[
 b(A)=\kappa(D)\qquad\text{for every }A\subset D,
\tag{0.17a}
\]

then both \(b\) and the target component colour \(\kappa\) would have to
be constant.  Exact all-incidence component control therefore collapses
to one global fused dependency block.  The quantitative \(9/32\) theorem
is the positive-density approximate form of this obstruction when owner
capacities are retained.

The same-owner nested continuation is even thinner.  For one primary
target \(D\), exactly \(\binom{m-d}{H-d}\) of its \(R\) compatible
roots inherit the full oriented radius-\(d\) flag from that same owner
row, a fraction

\[
 \frac{(H)_d}{(m)_d}.
\tag{0.17b}
\]

Even granting both component shores gives at most twice this density.
At \(d=1\) it is at most \(2H/m=o(1)\).  Thus the exact middle-star
witness does not extend to nested ambient provenance on almost every
root; a positive construction must change provenance between depths.

### D. One-row chronology is rigid; the aggregate Hall cut is conditional

If one ambient row restricts to a promotion order and certifies \(L\) of
its middle phases as cyclic ambient windows, then

\[
 L\le H+1,
\tag{0.17}
\]

those phases form one interval, and its numbers of complete flags which
survive to radius at least \(d\) are exactly

\[
 (L-d)_+.
\tag{0.18}
\]

For a bank which is simple with respect to **all cyclic \(m\)-windows**,
the total inherited radius-\(d\) capacity is therefore at most

\[
 C_d\le MN\left(1-\frac d{H+1}\right).
\tag{0.19}
\]

Under this additional hypothesis, the retained-chain demand
\(N_d=\binom{2m}{m-d}\) gives the conditional whole-shore Hall
deficiency

\[
 \boxed{
 \Delta_d\ge
 \left[N_d-MN\left(1-\frac d{H+1}\right)\right]_+.}
\tag{0.20}
\]

With

\[
 q_0=\lceil m^{1/4}\rceil,
 \qquad
 D_0=\left\lfloor\frac{m}{4(H+1)}\right\rfloor,
\tag{0.21}
\]

one has, uniformly for \(q_0\le d\le D_0\),

\[
 \boxed{\Delta_d\ge\frac{Wd}{2(H+1)},}
\tag{0.22}
\]

and hence

\[
 \boxed{
 \sum_{d=q_0}^{D_0}\Delta_d
 \ge\left(\frac1{64}+o(1)\right)\frac{Wm^2}{H^3}
 =\Omega\!\left(\frac{W\sqrt m}{(\log m)^{3/2}}\right)
 =\omega(W).}
\tag{0.23}
\]

The hypothesis preceding (0.19) is not automatic for one selected
infinity-cut MSW shore or \(C_8\) factor state.  Such a bank is simple
for its oriented primary owners, but as unoriented cyclic
\(m\)-windows every nonport target has two witnesses: its primary-owner
row and the row primarily owning its complement.  The unconditional
cyclic multiplicity-two estimate for one selected state is only

\[
 C_d\le2MN\left(1-\frac d{H+1}\right),
\tag{0.24}
\]

which is vacuous in the shallow range (0.21).  Hence (0.20)--(0.23) are
a rigorous cut for a cyclic-window-simple inheritance, not a no-go for
the actual complement-paired Catalan bank.

The exact live escape is now narrow: coordinate the primary row with its
complement-owner mate, or use a genuinely noncellular multirow braid.
Either route must also escape the unconditional component-colour
obstruction in Sections 1--2 and satisfy the lag-\(H\) chronology
identities.  No such braid is constructed here.

## 1. The arbitrary-transfer star-mass inequality

Let \(\mathscr P\) be the partition of nonexceptional promotion roots
induced by the partial bijection in Section 0, adjoining the \(o(N)\)
exceptional roots arbitrarily.  For a threshold \(T\), write

\[
 L_T=\bigcup_{B\in\mathscr P:|B|\ge T}B.
\tag{1.1}
\]

Changing the threshold \(R\) to \((1-\eta)R\), for any fixed
\(0<\eta<3/8\), changes the Catalan cutoff by only \(O(1)\) levels.
Every one of those boundary levels has normalized root mass \(o(1)\),
because \(j_*\to\infty\), \(j_*=o(m)\), and

\[
 \frac{s_jC_{m-j-2}}{C_m}
 =(1+o(1))s_j4^{-j-2}=O(j^{-3/2}).
\tag{1.2}
\]

The audited mass theorem therefore gives

\[
 \frac{|L_{(1-\eta)R}|}{N}=\frac58+o(1).
\tag{1.3}
\]

Every promotion root lies in exactly

\[
 Q=\binom{m+H}{H}
\tag{1.4}
\]

middle root-stars, while every middle target has \(R\) roots.  Thus

\[
 NQ=WR
\tag{1.5}
\]

and, for every \(L\subseteq\binom V{m-H}\),

\[
 \sum_{D\in\binom Vm}|L\cap\mathcal R(D)|=|L|Q.
\tag{1.6}
\]

If \(D\in\mathcal G_\eta\), its witnessing block has total size at least
\((1-\eta)R\), and hence is contained in \(L_{(1-\eta)R}\).  Therefore

\[
 |\mathcal G_\eta|(1-\eta)R
 \le |L_{(1-\eta)R}|Q.
\tag{1.7}
\]

Divide by (1.5) to obtain (0.10).  Replacing \(L_T\) by the unique top
component and using (0.8) proves the top-component version.

As a probabilistic corollary, suppose the transferred blocks are sampled
independently and every promotion root has the uniform cyclic-frame
marginal.  For \(D\notin\mathcal G_\eta\), the targetwise block theorem
has

\[
 \alpha_D=p\max_B|B\cap\mathcal R(D)|
 \le(1-\eta)Rp=(1-\eta)(1+o(1)),
\tag{1.8}
\]

where \(p=M/\binom MH\).  For all large \(m\), its miss probability is
at least \(\exp(-4/\eta)\).  Consequently the expected middle-hole count
is at least

\[
 \left(
  1-\frac{5/8}{1-\eta}-o(1)
 \right)e^{-4/\eta}W
 =\Omega_\eta(W).
\tag{1.9}
\]

This corollary concerns a component-product law.  Equations
(0.10) and (1.7), by contrast, are deterministic incidence statements
about every transfer of the component partition.

## 2. Proof of the capacity-constrained colour defect

The primary owners of one anchored exact-factor shore partition all
\(W=(m+1)C_m\) middle targets.  A component with \(s_\lambda\) rows
therefore has the exact owner-block size (0.11).

The levels \(j<j_*\) contain \((3/8+o(1))C_m\) rows.  The one boundary
level \(j_*-1\) has \(o(C_m)\) rows by (1.2).  Call a component
**deep-small** if its level is at most \(j_*-2\).  Deep-small components
therefore own

\[
 \left(\frac38-o(1)\right)W
\tag{2.1}
\]

middle targets.  Since \(s_j\) is increasing and

\[
 \frac{s_{j-1}}{s_j}\longrightarrow\frac14,
\tag{2.2}
\]

uniformly at \(j=j_*-1\to\infty\), minimality of \(j_*\) gives

\[
 \max_{\lambda\text{ deep-small}}s_\lambda
 \le\left(\frac14+o(1)\right)R.
\tag{2.3}
\]

Put

\[
 a_\lambda=\frac{e_\lambda}{M-1}.
\tag{2.4}
\]

Then

\[
 \sum_\lambda a_\lambda=o(N),
\tag{2.5}
\]

because \(W/(M-1)=(1+o(1))N\).  Moreover \(H>2\) and (0.14) imply

\[
 n_\lambda
 \le\frac{m+1}{M-1}s_\lambda+a_\lambda
 \le s_\lambda+a_\lambda.
\tag{2.6}
\]

Choose \(\delta_m\downarrow0\) slowly enough that

\[
 \sum_\lambda a_\lambda=o(\delta_mN).
\tag{2.7}
\]

The number of deep-small colours with \(a_\lambda>\delta_mR\) is
\(o(N/R)\).  Each owns at most

\[
 (m+1)\left(\frac14+o(1)\right)R
\tag{2.8}
\]

targets, so all exceptional deep-small colours together own \(o(W)\)
targets.  For every remaining \(D\in E_\lambda\), equations
(0.12), (2.3), and (2.6) give

\[
 g_D(b)\le n_\lambda
 \le\left(\frac14+o(1)\right)R.
\tag{2.9}
\]

Together with (2.1), this proves (0.16).  Summing the corresponding
defects proves

\[
 \operatorname{Err}(b)
 \ge
 \left(\frac38-o(1)\right)W
 \left(\frac34-o(1)\right)R,
\tag{2.10}
\]

which is (0.15).

There is also a useful fusion consequence independent of the owner
colour names.  If a new macroblock partition makes all but \(o(W)\)
stars \((1-\eta)\)-contained in one macroblock, then (1.6) forces the
union of macroblocks of size at least \((1-\eta)R\) to contain at least
\((1-\eta-o(1))N\) roots.  The original large MSW components contain
only \((5/8+o(1))N\).  Hence at least

\[
 \left(\frac38-\eta-o(1)\right)N
\tag{2.11}
\]

roots from originally small components must be absorbed into new
root-scale blocks.  Diagonalizing \(\eta\downarrow0\) gives the claim in
Section 0.

## 3. The positive phasewise Catalan lift

The mechanical clone-Hall theorem gives an integral matching covering
\(W-o(W)\) middle phase clones.  An anchored Catalan exact factor has one
primary occurrence for every middle target, so its primary-owner map is
a bijection onto \(\binom Vm\).  Composing the inverse of that bijection
with the clone matching gives an injection

\[
 \{\text{\(W-o(W)\) matched promotion phase clones}\}
 \hookrightarrow
 \{\text{distinct Catalan primary occurrences}\}.
\tag{3.1}
\]

This lift is literal at one phase.  If clone \((A,i)\) is matched to
\(D\supset A\), put \(J=D\setminus A\).  Let \(D\) be an ambient
length-\(m\) interval of its unique owner row \(\pi\).  Deleting the
labels of \(A\) from \(\pi\) leaves the labels of \(J\) consecutive in
\(\pi|_{A^c}\).  Thus \(J\) is a genuine length-\(H\) window in the
promotion top.

The same argument does not require the mechanical matching.  For every
incidence \(A\subset D\), apply it to the primary row owning \(D\) on
either shore of the MSW overlay.  Both rows belong to the same ownership
component, because an ownership edge joins the two occurrences of
\(D\).  Hence the full abstract provider star of \(D\) has literal
one-phase witnesses of one component colour.

This proves an exact phase certificate, not a ring certificate.  The
owner rows of two matched phases of the same root may be unrelated.
The remainder of this section gives exact obstructions to grouping these
certificates while retaining their component colours or ambient
provenance.

The natural choice of keeping the same owner row at the nested depths
already has a sharp statewise obstruction.

### Theorem 3.1 (exact same-owner nested-provenance loss)

Fix a primary owner row of \(D\), rotated as

\[
 \pi=(d_1,\ldots,d_m,e_1,\ldots,e_m),
 \qquad
 D=\{d_1,\ldots,d_m\},\quad D^c=\{e_1,\ldots,e_m\}.
\tag{3.2}
\]

For \(A\in\binom D{m-H}\), put \(J=D\setminus A\), list \(J\) in
the \(d\)-order as \(j_1,\ldots,j_H\), and set \(U=A^c\).  Then

\[
 \pi|_U=(j_1,\ldots,j_H,e_1,\ldots,e_m).
\tag{3.3}
\]

For \(0\le d\le H\), the complete oriented promotion flag through
radius \(d\), based at the middle owner \(D^c\), remains a family of
ambient intervals of this same row if and only if

\[
 T_d:=\{d_{m-d+1},\ldots,d_m\}\subseteq J.
\tag{3.4}
\]

Consequently the exact number and density of compatible roots with
same-owner provenance are

\[
 \boxed{
 |\mathcal G_\pi(D,d)|
 =\binom{m-d}{H-d},\qquad
 \frac{|\mathcal G_\pi(D,d)|}{R}
 =\frac{(H)_d}{(m)_d}.}
\tag{3.5}
\]

For the fixed orientations of the two component shores, let their
forced boundary \(d\)-blocks be \(T_d^0,T_d^1\), and put
\(u=|T_d^0\cup T_d^1|\).  Even granting targetwise use of either shore,
the exact union size is, with infeasible binomial coefficients read as
zero,

\[
 2\binom{m-d}{H-d}-\binom{m-u}{m-H}
 \le2\binom{m-d}{H-d}.
\tag{3.6}
\]

In particular, at depth one the two-shore star density is at most

\[
 \boxed{\frac{2H}{m}=o(1).}
\tag{3.7}
\]

If reversal is independently granted on both shores, the crude ceiling
is \(4H/m=o(1)\).

#### Proof

In (3.3), take the centered owner phase whose middle interval is
\(\{e_1,\ldots,e_m\}=D^c\).  Its rank-\((m-r)\) lower member is
\(\{e_{r+1},\ldots,e_m\}\), so it is automatically an ambient interval.
Its rank-\((m+r)\) upper member is

\[
 \{j_{H-r+1},\ldots,j_H\}\cup D^c.
\]

This is the corresponding ambient interval of \(\pi\) for every
\(r\le d\) exactly when the terminal \(r\)-block of \(J\) is the
terminal \(r\)-block of \(D\), which is (3.4).  Force those \(d\)
labels into \(J\), then choose its remaining
\(H-d\) labels freely from the other \(m-d\) elements of \(D\); this
proves (3.5).  Inclusion--exclusion for the two forced boundary blocks
gives (3.6), and \(d=1\) gives (3.7). \(\square\)

Thus the restricted order from the owner-star lift is always a literal
promotion frame, but for a \(1-o(1)\) fraction of each target star its
nested flags cease to be intervals of either ambient owner row already
at depth one.  This does not obstruct a braid which changes provenance
between depths.

There is an exact reason that the edge colours cannot simply be promoted
to root colours.  Let \(\mathcal I\) be the bipartite graph with root
shore \(\binom V{m-H}\), target shore \(\binom Vm\), and
\(A\sim D\) when \(A\subset D\).

### Lemma 3.2 (the root--target incidence graph is connected)

The graph \(\mathcal I\) is connected.

#### Proof

The Johnson graph on the root shore is connected.  If adjacent roots
\(A,A'\) differ by one coordinate, then

\[
 |A\cup A'|=m-H+1\le m.
\tag{3.8}
\]

Extend \(A\cup A'\) to an \(m\)-set \(D\).  Then
\(A-D-A'\) is a path in \(\mathcal I\).  Thus all roots lie in one
component.  Every middle target contains roots, so its vertices join
that same component. \(\square\)

If a root colour \(b(A)\) were required to equal the owner-component
colour \(\kappa(D)\) on every incidence, Lemma 3.2 propagates equality
through all of \(\mathcal I\).  Hence all roots and all targets would
have one colour.  Since the MSW ownership partition has many components,
exact all-incidence compatibility is impossible unless those components
are fused into one global dependency block.  The capacity-constrained
estimate (0.15) quantifies how badly an unmerged approximate colouring
must fail.

## 4. One ambient row has a staircase of inherited flag depths

Fix a promotion top \(U\), \(|U|=M\), and an oriented cyclic order

\[
 \sigma=(u_0,u_1,\ldots,u_{M-1})
\tag{4.1}
\]

on it.  Let \(\pi\) be an ambient cyclic order on \(V\) with
\(\pi|_U=\sigma\).  Write \(g_i\) for the gap after \(u_i\), and let

\[
 B(\pi,U)=\{i:g_i\text{ contains at least one label of }V\setminus U}.
\tag{4.2}
\]

For a phase \(a\in\mathbb Z_M\), let
\(I_\sigma(a,s)=\{u_a,\ldots,u_{a+s-1}\}\).  The actual centered
PBBS/promotion chronology through radius \(d\) has lower and upper
members

\[
 X_a^-(d)=I_\sigma(a+d,m-d),\qquad
 X_a^+(d)=I_\sigma(a-d,m+d).
\tag{4.3}
\]

The whole centered flag through radius \(d\) is ambient-consecutive if
and only if

\[
 B(\pi,U)\subseteq
 Q_a(d):=\{a+m-1,\ldots,a-d-1\},
\tag{4.4}
\]

where \(Q_a(d)\) is a cyclic interval of \(H-d+1\) gaps.  Indeed, once
the middle interval \(I_\sigma(a,m)\) is ambient-consecutive, every
lower member \(X_a^-(r)\) is automatic: it only removes endpoint labels
and internal gaps.  The upper member \(X_a^+(r)\) additionally exposes
the \(r\) gaps immediately before the middle start.  Requiring all
upper members through radius \(d\) therefore shrinks \(Q_a(0)\) by
exactly those \(d\) gaps, giving (4.4).  Taking complements converts
these centered owner intervals into the literal lower and upper
promotion flags of the target \(A\cup(U\setminus I_\sigma(a,m))\).

At \(d=0\), the phases certified by \(\pi\) are the length-\((H+1)\)
gap intervals containing \(B(\pi,U)\).  If nonempty, they form one
cyclic block.  If the minimal cyclic hull of \(B(\pi,U)\) has length
\(s\), the block length is

\[
 L=H-s+2\le H+1.
\tag{4.5}
\]

As the containing interval moves through this block, its slack before
the minimal hull is

\[
 L-1,L-2,\ldots,0.
\tag{4.6}
\]

Shrinking from \(Q_a(0)\) to \(Q_a(d)\) consumes exactly \(d\) units of
that slack.  Therefore the maximum inherited radii are precisely
\(L-1,L-2,\ldots,0\), proving (0.17)--(0.18).

## 5. Cyclic-window multiplicity gives the grouped Hall cut

Suppose first that the ambient witness bank is simple for all cyclic
\(m\)-windows: no \(m\)-set is a cyclic \(m\)-window of two distinct
rows.  If two rows restrict to the same \(\sigma\) at the same top,
their certified phase blocks are then disjoint, because an overlapping
phase would make the same middle target a cyclic \(m\)-window of both
rows.

Let their nonempty block lengths be \(L_1,\ldots,L_t\).  Then

\[
 \sum_{j=1}^tL_j\le M.
\tag{5.1}
\]

At radius \(d\), their capacity is

\[
 \sum_{j=1}^t(L_j-d)_+
 \le\sum_{j=1}^tL_j\left(1-\frac d{H+1}\right)
 \le M\left(1-\frac d{H+1}\right).
\tag{5.2}
\]

Summing over the \(N\) promotion roots proves (0.19).

The retained SCD tag census has \(N_e-N_{e+1}\) chains of exact tag
\(e<H\) and \(N\) chains of tag \(H\).  Hence the number of complete
flags which must reach radius \(d\) is exactly

\[
 \sum_{e=d}^{H-1}(N_e-N_{e+1})+N=N_d.
\tag{5.3}
\]

Taking the entire demand shore in Hall's inequality now gives (0.20).

For the quantitative form, the exact product

\[
 \frac{N_d}{W}
 =\prod_{j=0}^{d-1}\frac{m-j}{m+j+1}
\tag{5.4}
\]

and \(1-\prod_j(1-x_j)\le\sum_jx_j\) give

\[
 \frac{N_d}{W}\ge1-\frac{d^2}{m}.
\tag{5.5}
\]

Also, (0.3) implies

\[
 MN\le W\left(1+\frac1{M-1}\right).
\tag{5.6}
\]

Thus

\[
 \Delta_d\ge W\left(
  \frac d{H+1}-\frac{d^2}{m}-\frac1{M-1}
 \right).
\tag{5.7}
\]

For \(q_0\le d\le D_0\), both of the last two terms are at most
\(d/[4(H+1)]\) for all sufficiently large \(m\).  This proves (0.22).
Summing \(d\) from \(q_0=o(D_0)\) to \(D_0\) proves (0.23).

The range \(d\le D_0=o(\sqrt m)\) lies inside the range in which the
mechanical atlas separately supplies near-perfect clone matchings.
Hence the defect is genuinely caused by common provenance and nested
chronology, not by a failure of the ungrouped clone capacities.

More generally, suppose every \(m\)-set is a cyclic \(m\)-window of at
most \(\mu\) rows of the witness bank.  At a fixed top and phase, at most
\(\mu\) certified blocks overlap, so

\[
 \sum_jL_j\le\mu M.
\tag{5.8}
\]

The same proof gives only

\[
 C_d\le\mu MN\left(1-\frac d{H+1}\right).
\tag{5.9}
\]

One selected infinity-cut MSW factor shore is primary-owner-simple but
has \(\mu=2\) as a cyclic-window bank away from its ports: a target occurs
in its primary-owner row and cyclically in the row primarily owning its
complement.  Thus (5.9), not (0.19), is the unconditional consequence
of exact-factor membership.  With \(\mu=2\), the right side is
asymptotic to \(2W\) throughout the shallow range (0.21), so the Hall
deficiency obtained above vanishes.  This is the precise point at which
the direct chronology no-go stops.

## 6. Implication for the extensive \(C_8\) bank

The component-colour constant (0.15) uses the MSW hierarchy spectrum and
is not asserted for the extensive \(C_8\) cube spectrum.  Two rigorous
obstructions nevertheless apply to the direct \(C_8\) interface.

First, for the fixed-slot transported action, one component contributes
at most

\[
 2m\,2^H=o(R)
\tag{6.1}
\]

direct providers to any promotion root-star.  Thus independently sampled
fixed-slot components retain the audited \((e^{-1}-o(1))W\) expected-hole
floor.

Second, the one-row staircase theorem applies to every \(C_8\) row.
However, exact primary ownership does not make the full cyclic-window
bank simple.  Therefore the aggregate Hall defect (0.20)--(0.23) applies
to a \(C_8\) selection only after a separate cyclic-window-simple
witness theorem.  For one selected \(C_8\) factor state, the standard
complement occurrence gives the same multiplicity-two caveat as in
Section 5, so no such theorem is presently available.  A union of
several alternative factor states can have larger cyclic multiplicity.

The only unclosed \(C_8\) option is the same nonlocal one left by MSW:
select pieces from many rows and factors, rethread them into one cyclic
order per promotion root, and prove exact owner cancellation across the
resulting cross-row seams.  Since one ambient row certifies at most
\(H+1\) middle phases, a fully inherited repaired ring would require at
least

\[
 \left\lceil\frac{M-1}{H+1}\right\rceil
 =\Omega(m/H)
\tag{6.2}
\]

row pieces.  Their one-row depth profiles are constrained by the exact
staircase (0.18), but the complement-owner mate can in principle fill
the aggregate shallow deficit.  Coordinating those mates while retaining
one cyclic order per promotion root is part of the open braid.

There is still a sharp obstruction to the standard cut-and-quarantine
implementation on the unique top MSW component.  Its primary target
block has exact size

\[
 w_{\rm top}
 =(m+1)(C_{m-2}+C_{m-1})
 =\left(\frac5{16}+o(1)\right)W.
\tag{6.3}
\]

Since one inherited ambient row supplies at most \(H+1\) phases, covering
this block by cut-only inherited pieces needs at least

\[
 \frac{w_{\rm top}}{H+1}
 =\left(\frac5{16}+o(1)\right)\frac WH
\tag{6.4}
\]

pieces.  If every piece is separately protected by the standard
two-sided \(2H\) chronology collar, the collar toll is at least

\[
 2H\,\frac{w_{\rm top}}{H+1}
 =\left(\frac58-o(1)\right)W.
\tag{6.5}
\]

Thus a cut-only append/quarantine compiler is linearly expensive.  This
does not charge a nonlocal splice which shares one boundary across many
pieces or uses the complement-owner mate to continue chronology.

## 7. Exact surviving braid interface

A positive construction which escapes the theorems above must provide,
for every promotion root \(A\), one cyclic labelling

\[
 (x_{A,0},x_{A,1},\ldots,x_{A,M-1})
\tag{7.1}
\]

of \(A^c\), with one repaired phase deleted, such that

\[
 J_{A,i}=\{x_{A,i},\ldots,x_{A,i+H-1}\}
\tag{7.2}
\]

obeys the literal rotor identities

\[
 |J_{A,i}\cap J_{A,i+1}|=H-1,
 \qquad
 J_{A,i+1}\setminus J_{A,i}
 =J_{A,i+H}\setminus J_{A,i+H+1},
\tag{7.3}
\]

with the deletion labels exhausting \(A^c\).  Once (7.1) is fixed, all
lower and upper entrance intervals are forced; they cannot be chosen by
separate clone matchings.

In addition, the construction must do all of the following.

1. It must merge the original Catalan component controls on at least the
   positive-density sector quantified in (2.11), or use a target-dependent
   control which is not a root-component colouring at all.
2. It must satisfy the lag-\(H\) identities while coordinating primary
   rows with complement-owner mates, or change ambient provenance inside
   flags.  A cut-only implementation pays the linear collar toll (6.5);
   a viable braid must share or eliminate those boundaries so that the
   actual physical seam and component charge remains \(o(W)\).
3. It must choose the middle and entrance clones jointly.  At owner
   phase \(a\), if \(J_a\) is the omitted \(H\)-set and \(C_a\) is the
   complement of the rank-\((m-q)\) entrance, every common order obeys
   \(J_a\subseteq C_a\).  The separate clone-Hall theorems do not impose
   this containment; the top-harmonic containment cut constructs
   near-perfect separate matchings at edit distance \(W-o(W)\) from one
   another.  That result obstructs arbitrary post hoc coupling, not a
   jointly designed nested matching.

No known MSW component switch, extensive fixed-slot \(C_8\) switch, or
mechanical phase matching supplies all three requirements.  Conversely, the
present results do not prove an invariant against a braid satisfying
them.  The precise proved boundary is therefore:

\[
 \boxed{
 \begin{gathered}
 \text{the phasewise Catalan--clone-Hall interface exists;}\\
 \text{the unmerged component-colour interface is impossible;}\\
 \text{the natural same-owner nested continuation has density }o(1)\text{;}\\
 \text{a cyclic-window-simple common-row chronology lift is impossible,}\\
 \text{but the actual complement-paired bank is not cyclic-window-simple;}\\
 \text{a positive-density, provenance-changing, lag-\(H\) multirow braid
 remains open.}
 \end{gathered}}
\tag{7.4}
\]

## 8. Implication boundary

Proved here:

1. the arbitrary-transfer \(5/8\) star-mass obstruction (0.10);
2. the capacity-constrained MSW owner-colour defect with constant
   \(9/32\), (0.15)--(0.16);
3. the exact positive phasewise Catalan lift of the mechanical clone
   matching;
4. the exact same-owner nested-provenance density
   \((H)_d/(m)_d\), including the two-shore \(2H/m\) depth-one ceiling;
5. the exact inherited-depth staircase \((L-d)_+\);
6. the conditional cyclic-window-simple grouped Hall deficiency (0.20);
7. the uniform shallow estimate and aggregate constant \(1/64\),
   (0.22)--(0.23), under that hypothesis;
8. the exact cyclic multiplicity-two correction (0.24); and
9. the linear standard-collar toll (6.5) for cut-only top-component
   inheritance.

Not proved here:

1. a physical lower bound of one seam per owner--depth crossing;
2. impossibility of coordinating the primary row with its
   complement-owner mate;
3. impossibility of changing ambient provenance inside a flag;
4. impossibility of a globally selected mixture of alternative exact
   factors whose final row pieces are rethreaded noncellularly;
5. a construction of that braid; or
6. the coefficient-one theorem.

The new obstruction is therefore sharp in scope: component size is not
the issue, and ungrouped Hall is not the issue.  The unmerged interface
fails at positive-density component colouring.  Common nested chronology
also fails for a cyclic-window-simple bank, but the factor's exact
complement-owner duplication prevents promoting that conditional cut to
an unconditional MSW/\(C_8\) no-go.
