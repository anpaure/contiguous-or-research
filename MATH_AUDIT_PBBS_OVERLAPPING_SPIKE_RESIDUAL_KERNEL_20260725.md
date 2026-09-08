# PBBS overlapping intervals plus owner-fixed spikes: exact current frame and residual kernel

Date: 2026-07-25

Method: pure mathematics only.  No computation, search, solver, or
long-running job is used.

## 0. Verdict

Put

\[
 n=2m+1,
 \qquad W=\binom{2m+1}{m},
 \qquad H=\lceil L\sqrt m\rceil,
 \qquad B=\operatorname{Cat}_m=\frac{W}{2m+1},
\]

with fixed \(L>0\).  Assume the recursively conjugate PBBS transition
seed has been made \(H\)-physical under the residence hypothesis

\[
 \rho_H=o\!\left(
 \frac{\binom{2m-1}{m-1}}{H\log m}
 \right).
\tag{0.1}
\]

This note audits the proposed union of three mechanisms:

1. PBBS maximal physical intervals in one adjacent block;
2. the joined overlap of the odd and even adjacent-block layers; and
3. terminal owner-fixed upper or lower spikes.

There is a genuine positive advance.  The PBBS interval construction is
legal simultaneously for **all** adjacent blocks, not only for a disjoint
parity layer.  At each upper depth its target graph is a disjoint union of
directed paths.  If a path has base loads

\[
 x_0\ge x_1\ge\cdots\ge x_s,
 \qquad d_i=x_i-x_{i+1},
\]

and a packet corner moves \(\ell_i\) occurrences across its \(i\)-th
edge, where \(0\le\ell_i\le d_i\), then the exact doubled floor-energy
drop is

\[
 \boxed{
 \mathscr D_{\rm path}(\ell)
 =2\sum_{i=0}^{s-1}\ell_i(d_i-\ell_i)
  +2\sum_{i=0}^{s-2}\ell_i\ell_{i+1}\ge0.}
\tag{0.2}
\]

The first sum is the within-block physical-interval charge and the second
is precisely the joined odd/even charge.  Thus **every** overlapping PBBS
corner is floor-energy nonincreasing at every upper depth; all lower loads
are fixed.  The total packet and run counts remain

\[
 \boxed{
 r_{\rm all}=o(W/H),
 \qquad J(M_\varepsilon)\le J_0+2r_{\rm all}=o(W/H).}
\tag{0.3}
\]

The interval null space is exact:

\[
 \boxed{
 \mathscr D_{\rm path}(\ell)=0
 \Longleftrightarrow
 \ell_i\in\{0,d_i\}\ \text{for every }i,
 \quad
 \ell_i\ell_{i+1}=0\ \text{for every }i.}
\tag{0.4}
\]

Thus a flat interval corner consists of complete coherent swaps on a
matching of nonadjacent positive-capacity path edges.  Partial transport
or two consecutive nonzero transports is strictly decreasing.

The current-endpoint spike law in
`MATH_ATTACK_PBBS_INTERVAL_SPIKE_CURRENT_ENDPOINT_FRAME_20260725.md`
also passes audit with its stated normalization.  At one rank, an
owner-fixed occurrence switch is a directed target edge \(e:u\to v\),
with column \(d_e={\bf e}_v-{\bf e}_u\).  For any selected edge set
\(F\),

\[
 \boxed{
 Q(x+z_F)-Q(x)
 =\sum_{e\in F}2(x_v-x_u+1)
  +2\sum_{\{e,f\}\subseteq F}\langle d_e,d_f\rangle,}
\tag{0.5}
\]

where

\[
 \langle d_e,d_f\rangle
 =\mathbf1_{\{\operatorname{tail}e=\operatorname{tail}f\}}
  +\mathbf1_{\{\operatorname{head}e=\operatorname{head}f\}}
 \ge0.
\tag{0.6}
\]

Consequently the one-rank spike target-graph local-minimum cone is

\[
 \boxed{
 Q(x+z_F)\ge Q(x)\text{ for every }F
 \Longleftrightarrow
 x_v\ge x_u-1\text{ for every allowed spike edge }u\to v.}
\tag{0.7}
\]

A selected spike set **inside this cone** is exactly energy-flat iff every
selected edge is tight, \(x_v=x_u-1\), and its edges have pairwise
distinct tails and pairwise distinct heads.

For the full weighted flag chain, put

\[
 a_e=2\sum_{p:\,d_{e,p}\ne0}w_p^+
       \bigl(x_p(v_{e,p})-x_p(u_{e,p})+1\bigr).
\tag{0.7a}
\]

Then (0.5) holds with its first summand replaced by
\(\sum_{e\in F}a_e\), and

\[
 \langle d_e,d_f\rangle_w
 =\sum_p w_p^+
 \left(
  \mathbf1_{\{u_{e,p}=u_{f,p}\}}
  +\mathbf1_{\{v_{e,p}=v_{f,p}\}}
 \right)\ge0.
\tag{0.7b}
\]

Thus the stacked spike local-minimum cone is exactly \(a_e\ge0\) for
every admissible occurrence arc.  Inside that cone, a selected set is
flat iff \(a_e=0\) for every selected arc and all its distinct selected
columns are pairwise orthogonal.  Equation (0.7) is precisely its
one-rank specialization.

Equations (0.4) and (0.7a)--(0.7b) characterize the exact residual
zero cone of the combined floor-corrected quadratic mechanism.  For a
sequential interval-then-spike menu there is one necessary orbit
qualification: the stacked inequalities \(a_e\ge0\) must hold after
every zero-drop interval corner satisfying (0.4).  This condition is also
sufficient, because every interval corner is nonincreasing and every
spike cross-Gram is nonnegative.  The cone is nontrivial.  Its canonical
diffuse element at one rank is a load-two target with two occurrence
edges leading to distinct load-one image targets.  Switching one
occurrence is flat; switching both raises doubled floor energy by two.  If
such fibres are isolated from the adjacent target paths, neither the
interval charge nor the joined charge sees them.

This gives a rigorous **rank-projected** no-go to deriving a charged-frame
inequality from the three quadratic identities alone.  At upper depth
two there are integral fixed-mass profiles with

\[
 \mathcal Q_2=\Theta(W),
 \qquad
 \mathscr D_{{\rm interval},2}=0,
 \qquad
 \sup_F[Q_2(x)-Q_2(x+z_F)]=0,
\tag{0.8}
\]

while their abstract physical packet incidence uses only
\(O(W/m)=o(W/H)\) long runs and their displayed depth-one predecessors are all
distinct.  Since

\[
 H\operatorname{Cat}_m
 =\left(\frac L2+o(1)\right)\frac{W}{\sqrt m}=o(W),
\tag{0.9}
\]

no rank-two projected inequality of the form

\[
 \text{interval charge}_2+\text{joined charge}_2
 +\text{spike descent}_2
 \ge\gamma_L\bigl(\mathcal Q_2-C_LH\operatorname{Cat}_m\bigr)
\tag{0.10}
\]

is a formal consequence of those three mechanisms.

The construction in Section 6 is an exact integral rank-two load and
one-step nested-incidence, low-packet counterexample to the **projected
quadratic implication**.  It is not asserted to extend to a complete
weighted flag chain, nor to be the flag profile of the canonical PBBS
transition factor.  Accordingly it does not refute the physical PBBS
charged-frame lemma.  It identifies its next exact form:

> **PBBS diffuse-plateau exclusion (open).**  In every current
> \(H\)-physical PBBS endpoint with
> \(\mathcal Q\gg_LH\operatorname{Cat}_m\), all but
> \(O_L(H\operatorname{Cat}_m)\) floor excess must either cross a
> nontrivial adjacent path edge as in (0.2), or admit an owner-fixed spike
> occurrence arc with negative stacked marginal \(a_e<0\), with the productive occurrences
> packable into \(o(W/H)\) physical blocks.

This is strictly sharper than the previous renewable-frame statement: it
names the exact residual cone that PBBS chronology must exclude.  No
constant-one conclusion is claimed.

## 1. Recursively conjugate PBBS notation

Let \(P_1,\ldots,P_m\) be the fixed ordered coordinate pairs, with one
unpaired coordinate.  Let \(\theta_j\) exchange \(P_j,P_{j+1}\)
coordinatewise.  Starting from one PBBS transition factor
\(\mathcal F_1\) on \([n]\setminus P_1\), put

\[
 \mathcal F_{j+1}=\theta_j\mathcal F_j.
\tag{1.1}
\]

For a lower root \(S\) in phase \(j\), write \(f_j(S)\) for its
designated middle owner.  Exact PBBS transition ownership gives:

\[
 S\subset f_j(S),
 \qquad f_j(S)\cap P_j=\varnothing,
\tag{1.2}
\]

and \(f_j\) is injective.  For

\[
 \mathcal E_j=\left\{S:
 S\cap P_h\ne\varnothing\ (h<j),
 \quad S\cap(P_j\cup P_{j+1})=\varnothing\right\},
\tag{1.3}
\]

the two candidate owners satisfy

\[
 f_{j+1}(S)=\theta_jf_j(S).
\tag{1.4}
\]

Every PBBS lower flag is contained in \(S\).  Every upper flag contains
\(S\), avoids the current source pair, and therefore has the same first
avoided category as its source phase.

## 2. Full overlapping PBBS legality and the run ledger

### Theorem 2.1 (all adjacent PBBS packet families form one cube)

For every \(j<m\), split the occurrences of \(\mathcal E_j\) in the
\(H\)-physical phase-\(j\) paths into maximal physical intervals.  On
every interval choose either all phase-\(j\) tokens or all conjugate
phase-\((j+1)\) tokens.  These choices may be made simultaneously for all
\(j=1,\ldots,m-1\), including neighboring blocks.  Every corner is
lower-saturating and middle-injective.

### Proof

The carriers \(\mathcal E_j\) are pairwise disjoint: if \(j<k\), a root
in \(\mathcal E_j\) avoids \(P_j\), whereas a root in
\(\mathcal E_k\) meets it.  Hence every lower target receives exactly one
token.

Within one block, a mixed owner equality

\[
 f_j(S)=f_{j+1}(T)=\theta_jf_j(T)
\]

has a common owner avoiding both exchanged pairs.  It is fixed by
\(\theta_j\), so injectivity of \(f_j\) gives \(S=T\), and a corner
never chooses both candidates at one root.

For roots in blocks \(j<k\) with \(k\ge j+2\), the earlier owner avoids
one of \(P_j,P_{j+1}\), while the later root, and hence its owner, meets
both.  Equality is impossible.

It remains to compare neighboring blocks.  A root
\(T\in\mathcal E_{j+1}\) meets \(P_j\), so it cannot share an owner with
the phase-\(j\) candidate over \(S\in\mathcal E_j\).  Two
phase-\((j+1)\) candidates are separated by injectivity.  In the last
case, suppose

\[
 f_{j+1}(S)=f_{j+2}(T)
 =\theta_{j+1}f_{j+1}(T).
\]

The common owner avoids \(P_{j+1}\cup P_{j+2}\), hence is fixed by
\(\theta_{j+1}\).  Injectivity gives \(S=T\), contradicting the
disjointness of the carriers.

An old candidate coexists with every unchanged background token in the
base endpoint.  Its new candidate coexists with that same background in
the coherent endpoint obtained by swapping only positions \(j,j+1\).
Thus no changed owner collides with the unchanged background.  This
exhausts all owner pairs.  \(\square\)

Let \(r_{\rm odd}\) and \(r_{\rm even}\) be the packet counts in the two
parity layers.  The PBBS compatibility theorem and (0.1) give

\[
 r_{\rm odd}=o(W/H),
 \qquad r_{\rm even}=o(W/H).
\]

Their union has

\[
 r_{\rm all}\le r_{\rm odd}+r_{\rm even}=o(W/H).
\tag{2.1}
\]

Switching one packet clears one old physical interval and fills one
conjugate interval.  Sequentially applying these operations raises the
selected-run count by at most two per packet, even when one PBBS factor
participates in both neighboring blocks.  This proves (0.3).  The literal
endpoint initialization and collar toll is

\[
 O\bigl(H(J_0+r_{\rm all})\bigr)=o(W).
\tag{2.2}
\]

## 3. Exact signed-path descent

Fix one upper depth \(q\le H\).  A nonfixed phase-\(j\) upper target
\(U\) has first avoided category \(j\), and

\[
 V=\theta_jU
\]

has category \(j+1\).  Draw the directed edge \(U\to V\).  A target has
at most one incident edge from the preceding block and at most one edge to
the following block.  Category strictly increases along every edge.
Consequently the target graph is a disjoint union of directed paths.

Let \(x_U,x_V\) be the current base loads and let \(d_{UV}\) be the total
number of occurrences moved from \(U\) to \(V\) by the complete coherent
block swap.  That coherent endpoint is the \(\theta_j\)-permutation of
the base load on the union of categories \(j,j+1\).  Hence

\[
 x_U-d_{UV}=x_V,
 \qquad x_V+d_{UV}=x_U,
\]

so

\[
 \boxed{d_{UV}=x_U-x_V\ge0.}
\tag{3.1}
\]

On one directed path label the vertices \(0,1,\ldots,s\).  Put

\[
 d_i=x_i-x_{i+1}.
\]

A packet corner moves some number \(\ell_i\) of the \(d_i\) occurrences
on edge \(i\), with

\[
 0\le\ell_i\le d_i.
\tag{3.2}
\]

The new loads are

\[
 y_0=x_0-\ell_0,
\]

\[
 y_i=x_i+\ell_{i-1}-\ell_i\quad(1\le i<s),
\]

\[
 y_s=x_s+\ell_{s-1}.
\tag{3.3}
\]

With \(\ell_{-1}=\ell_s=0\), direct expansion gives

\[
 \begin{aligned}
 \|y\|_2^2-\|x\|_2^2
 &=-2\sum_i d_i\ell_i
   +\sum_{i=0}^s(\ell_{i-1}-\ell_i)^2\\
 &=-2\sum_i\ell_i(d_i-\ell_i)
   -2\sum_i\ell_i\ell_{i+1}.
 \end{aligned}
\tag{3.4}
\]

Every corner has the same total load at this rank, so the linear and floor
baseline terms in doubled factorial-floor energy cancel.  Negating (3.4)
proves (0.2).  Summing paths, depths, and arbitrary nonnegative weights
proves deterministic floor monotonicity.

Every term on the right of (0.2) is nonnegative.  It vanishes iff

\[
 \ell_i(d_i-\ell_i)=0
 \quad\text{and}\quad
 \ell_i\ell_{i+1}=0
\]

for every \(i\).  This is exactly (0.4).

All lower flag loads are fixed because each lower flag lies in the
pointwise fixed root.  At the first upper rank, the PBBS seed has
\(o(W)\) doubled floor excess.  Equation (0.2) shows that every full
overlapping corner still has \(o(W)\) first-shadow collision excess.  Its
hole excess is also \(o(W)\), because

\[
 \#\text{holes}
 =K-T+\sum_U(x_U-1)_+,
 \qquad
 \sum_U(x_U-1)_+\le\sum_U\binom{x_U}{2}.
\tag{3.5}
\]

Thus the joined atlas introduces no first-shadow repair debt.

## 4. Audit and kernel of the current spike law

First fix one rank and one actual source phase with omitted pair \(A\).
Every selected owner-fixed upper spike has old target \(u_e\) avoiding
\(A\) and image target \(v_e\) meeting \(A\).  Put

\[
 d_e={\bf e}_{v_e}-{\bf e}_{u_e}.
\]

For two distinct selected occurrences, old/image cross equalities are
impossible.  Therefore

\[
 \langle d_e,d_f\rangle
 =\mathbf1_{\{u_e=u_f\}}+
  \mathbf1_{\{v_e=v_f\}}\ge0,
\]

which is (0.6).

For one edge, fixed-mass doubled floor energy changes by

\[
 2\langle x,d_e\rangle+\|d_e\|_2^2
 =2(x(v_e)-x(u_e)+1).
\tag{4.1}
\]

Expanding a sum of columns proves (0.5).

If every edge obeys \(x(v_e)\ge x(u_e)-1\), each singleton term in
(0.5) and every cross term is nonnegative, so no subset descends.
Conversely, if one edge has \(x(v_e)\le x(u_e)-2\), its singleton switch
strictly descends.  This proves (0.7).

Inside the local-minimum cone (0.7), equality in (0.5) requires every
selected singleton term and every selected cross term to vanish.  Thus
all selected edges must satisfy \(x(v_e)=x(u_e)-1\), and no two may share
a tail or a head.  This proves the exact one-rank spike kernel statement.

Now retain the whole weighted upper flag chain.  Regard \(d_e\) as the
stacked innovation and define

\[
 D=\sum_e\sum_{p:\,d_{e,p}\ne0}w_p^+
 \bigl(x_p(u_{e,p})-1-x_p(v_{e,p})\bigr),
\tag{4.1a}
\]

\[
 G=2\sum_{e<f}\langle d_e,d_f\rangle_w.
\tag{4.1b}
\]

The cross inner product is (0.7b), hence nonnegative.  Applying the
one-rank expansion and summing ranks proves that a stacked state admits no
descending deterministic spike subset iff every individual occurrence
arc has nonnegative marginal \(a_e\) from (0.7a).  Within that cone a
selected subset is flat iff every selected \(a_e=0\) and every selected
pair has weighted inner product zero.

For completeness, if all chosen occurrences are switched independently
with common probability \(s\), then

\[
 \boxed{
 \mathbb E_sQ-Q=s^2G-2sD.}
\tag{4.2}
\]

This agrees exactly with the current-endpoint source report.  Its optimal
guaranteed descent is

\[
 \Psi(D,G)=
 \begin{cases}
 0,&D\le0,\\
 D^2/G,&0<D<G,\\
 2D-G,&D\ge G>0,\\
 2D,&G=0<D.
 \end{cases}
\tag{4.3}
\]

The lower owner-fixed spike has the same target-graph law in the lower
direct summand.  In the upper-rank projection used below the lower weights
are zero, so lower spikes cannot change that projected obstruction.

## 5. The exact sequential hybrid inequality

Let \(M_0\) be the current \(H\)-physical PBBS seed.  Choose an arbitrary
full overlapping interval corner \(I\), and let

\[
 \mathscr D_{\rm int}(I)
 =\sum_{q\le H}w_q^+
   \sum_{\text{target paths at }q}
      \mathscr D_{\rm path}(\ell).
\tag{5.1}
\]

Then

\[
 \mathcal Q_w(M_I)
 =\mathcal Q_w(M_0)-\mathscr D_{\rm int}(I).
\tag{5.2}
\]

At the actual current endpoint \(M_I\), choose an owner-fixed spike
family inside one actual source phase, recompute \(D_I,G_I\), and use the
optimal bias (4.3).  Some literal final corner satisfies

\[
 \boxed{
 \mathcal Q_w(M')
 \le\mathcal Q_w(M_0)
   -\mathscr D_{\rm int}(I)-\Psi(D_I,G_I).}
\tag{5.3}
\]

If the spike family contains \(N\) occurrences, its central incidences
remain fixed and it adds at most \(2N\) selected runs.  Hence

\[
 \boxed{
 J(M')\le J_0+2r_{\rm all}+2N.}
\tag{5.4}
\]

For complete fibres of multiplicity at least \(K_0\), with collision
count \(C_{K_0}\),

\[
 N\le\frac{2C_{K_0}}{K_0-1},
 \qquad
 \Delta J_{\rm spike}\le\frac{4C_{K_0}}{K_0-1}.
\tag{5.5}
\]

Equations (5.3)--(5.5) are the strongest unconditional current-endpoint
hybrid theorem supplied by the three audited charts.

Define the current one-round hybrid charge

\[
 \mathfrak F(M_0)=
 \sup_{\substack{I\text{ overlapping packet corner}\\
                  \mathscr S\text{ post-}I\text{ spike family}\\
                  2r_{\rm all}+2|\mathscr S|=o(W/H)}}
 \left[\mathscr D_{\rm int}(I)
       +\Psi(D_{I,\mathscr S},G_{I,\mathscr S})\right].
\tag{5.6}
\]

A constant current frame would be

\[
 \boxed{
 \mathfrak F(M)
 \ge\gamma_L
 \bigl(\mathcal Q_w(M)-C_LH\operatorname{Cat}_m\bigr)}
\tag{5.7}
\]

for every current physical PBBS endpoint, with fixed
\(\gamma_L,C_L>0\).  The chart identities prove (5.3), but they do not
prove (5.7).

There is also a structural reason not to put interval and spike bits into
one unexamined simultaneous Gram cube: cross products between an interval
column and a spike column have no fixed sign.  Sequential composition in
(5.3), with \(D,G\) recomputed at \(M_I\), is the exact safe statement.

### Theorem 5.1 (exact one-round residual zero cone)

Call \(M\) null for the interval-then-spike menu if

\[
 \mathcal Q_w(M_{I,F})\ge\mathcal Q_w(M)
\tag{5.8}
\]

for every legal full overlapping interval corner \(I\) and every
deterministic owner-fixed spike subset \(F\) admissible at the resulting
endpoint \(M_I\).  Then (5.8) holds if and only if both of the following
conditions hold:

1. at every positive-weight rank, every path flow induced by every legal
   interval corner satisfies (0.4);
2. for every such interval endpoint \(M_I\), every admissible stacked
   spike occurrence arc satisfies \(a_e(M_I)\ge0\).

Indeed, set \(F=\varnothing\).  Interval monotonicity gives
\(\mathcal Q_w(M_I)\le\mathcal Q_w(M)\), while (5.8) gives the reverse
inequality.  Hence every interval corner is flat, and the sum of the
nonnegative path terms forces (0.4) at every positive-weight rank.  Now
take \(F=\{e\}\).  Since \(M_I\) has the same energy as \(M\), (5.8)
forces \(a_e(M_I)\ge0\).  Conversely, condition 1 makes the interval
step flat, while condition 2 and the nonnegative spike cross-Grams make
every post-interval spike subset nondecreasing.  This proves the
equivalence.

For an arbitrarily repeated state-adaptive menu, the exact criterion is
the same pair of conditions at every state in the directed closure under
zero-energy interval and spike moves.  This is an orbit qualification,
not an additional analytic inequality.

## 6. Canonical diffuse plateau in the residual kernel

We now construct an exact integral **rank-two projected** profile in the
intersection of the interval and spike kernels.  It is a counterexample
to the rankwise implication

\[
 \text{chart algebra}+\text{floor arithmetic}
 \Longrightarrow\text{a positive charged frame}.
\]

It is not a complete physical PBBS factor.

At upper depth \(q=2\), the autonomous token mass and target count agree:

\[
 T=\binom{2m+1}{m-1}
  =\binom{2m+1}{m+2}=K_2.
\tag{6.1}
\]

Thus the exact floor is the all-one vector.  Fix the first two priority
pairs \(P_1,P_2\), and let

\[
 \mathcal Z=
 \{U\in\tbinom{[2m+1]}{m+2}:U\cap(P_1\cup P_2)=\varnothing\}.
\tag{6.2}
\]

Every \(U\in\mathcal Z\) has first-avoided category one and is fixed by
the coordinatewise exchange of \(P_1\) and \(P_2\).  Hence it is an
isolated vertex of the complete all-adjacent target-path graph: block one
fixes it, and blocks \(j\ge2\) do not act on category one.

For a completely explicit nested occurrence family, choose four distinct
coordinates

\[
 B_1=\{b_1,b_2\},\qquad B_2=\{b_3,b_4\}
\]

outside \(P_1\cup P_2\), put \(B=B_1\cup B_2\), and define

\[
 \mathcal U=
 \{B\cup C:C\in\tbinom{[2m+1]\setminus(P_1\cup P_2\cup B)}{m-2}\}.
\tag{6.3}
\]

Its exact size is

\[
 F_m=|\mathcal U|=\binom{2m-7}{m-2}=\Theta(W).
\tag{6.4}
\]

Set \(R=\lfloor F_m/2\rfloor\).  Choose \(R\) targets from
\(\mathcal U\) as overloads and \(R\) further targets from
\(\mathcal Z\) as holes.  This is possible for all sufficiently large
\(m\), since \(|\mathcal Z|=\binom{2m-3}{m+2}\) and
\(2R\le F_m<|\mathcal Z|\).  Put

\[
 x(U)=2\quad(U\text{ overloaded}),\qquad
 x(Z)=0\quad(Z\text{ a hole}),
\]

and give every other rank-two target load one.  The mass is exactly
\(K_2=T\), and the doubled factorial-floor excess is

\[
 \boxed{Q_2(x)=2R=\Theta(W).}
\tag{6.5}
\]

Indeed, for floor one,

\[
 Q_2(x)=\sum_U(x(U)-1)(x(U)-2),
\]

so only the \(R\) holes contribute, two each.

Give every overloaded target \(U=B\cup C\) two labelled phase-one
occurrences.  Their middle owners and nested upper chains are

\[
 Y_1=C\cup\{b_1,b_2\},
 \quad Y_1\subset C\cup\{b_1,b_2,b_3\}\subset U,
\]

\[
 Y_2=C\cup\{b_1,b_4\},
 \quad Y_2\subset C\cup\{b_1,b_2,b_4\}\subset U.
\tag{6.6}
\]

These chains are genuine two-step Johnson chains.  For the first use the
successive states

\[
 C\cup\{b_1,b_2\},
 \quad C\cup\{b_1,b_3\},
 \quad C\cup\{b_3,b_4\},
\]

and for the second use

\[
 C\cup\{b_1,b_4\},
 \quad C\cup\{b_2,b_4\},
 \quad C\cup\{b_2,b_3\}.
\]

Their lower roots are respectively \(C\cup\{b_1\}\) and
\(C\cup\{b_4\}\).  Hence all displayed lower roots and all displayed
middle owners are distinct.  The two depth-one predecessors are
\(U\setminus\{b_4\}\) and \(U\setminus\{b_3\}\); the special-coordinate
patterns in (6.3) show that all \(2R\) displayed predecessors are
globally distinct.  Thus the rank-two overloads force no first-upper
collision.

An owner-fixed spike of either displayed occurrence can be distinguished
at depth one or two.  At rank two its image replaces one entering
coordinate by one marker from the omitted pair \(P_1\).  Every such image
therefore meets \(P_1\), whereas every overload and every hole avoids
\(P_1\).  Hence every possible image has current load one.  In particular,
every allowed arc out of a load-two target is tight:

\[
 x(v)=1=x(u)-1.
\tag{6.7}
\]

Every arc out of a load-one target is automatically nonnegative because
all loads are nonnegative.  Thus (0.7) holds for **every current**
rank-two spike arc, not just for one preselected marker.  No choice of
subset or marker in this current-endpoint spike menu descends.  For the
two occurrences of one overload, switching one is flat and switching
both costs two whenever their images are distinct; image coincidences can
only add a nonnegative Gram term.  The claim does not include a newly
recentered spike menu after taking such a flat singleton.

All overload and hole vertices are isolated from the all-adjacent target
paths.  Every other vertex has load one, so every target-path capacity
\(d_i=x_i-x_{i+1}\) is zero.  Therefore

\[
 \boxed{
 \mathscr D_{{\rm interval},2}=0,
 \qquad
 \sup_F\bigl[Q_2(x)-Q_2(x+z_F)\bigr]=0.}
\tag{6.8}
\]

At the packet-incidence bookkeeping level, the \(2R=\Theta(W)\)
displayed labelled occurrences can be grouped into

\[
 O(R/m)=O(W/m)=o(W/H)
\tag{6.9}
\]

long blocks of length \(\Theta(m)\).  Since

\[
 H\operatorname{Cat}_m
 =\left(\frac L2+o(1)\right)\frac W{\sqrt m},
\]

equation (6.5) gives

\[
 \frac{Q_2(x)}{H\operatorname{Cat}_m}=\Theta_L(\sqrt m)\longrightarrow\infty.
\tag{6.10}
\]

The qualification ``packet-incidence bookkeeping level'' is essential.
Grouping labels into long blocks does not prove that the prescribed
chains (6.6) occur consecutively in one canonical PBBS transition factor,
nor does the rank-two shield prove the stacked inequalities (0.7a) at all
higher ranks.  The construction is therefore an exact coordinate-level
no-go for the projected quadratic implication, not a physical full-window
PBBS counterexample.

## 7. Exact remaining PBBS statement

The combined chart zero cone has two pieces:

1. complete, pairwise nonadjacent coherent interval swaps, from (0.4);
2. nonnegative stacked spike marginals \(a_e\ge0\), with tight one-rank
   edges \(x_v=x_u-1\) and diffuse load-two stars as the smallest
   collision-bearing example, from (0.7)--(0.7b).

The canonical obstruction is not high multiplicity.  Its old fibres have
load two, so activating them occurrence by occurrence is both
nondecreasing and linear in physical pieces.  High-multiplicity spike
packing does not touch it.

Accordingly, the exact next positive theorem is the PBBS
diffuse-plateau exclusion stated in Section 0.  Equivalently, prove that
the physical PBBS chronology cannot support more than
\(O_L(H\operatorname{Cat}_m)\) floor excess on target-path-isolated
load-two fibres for which every admissible owner-fixed occurrence chain
has \(a_e\ge0\), uniformly throughout the zero-drop interval orbit.  Any
stronger state-adaptive theorem may instead show that a new coherent
recentering exposes a positive path edge for a fixed fraction of these
fibres, but its cumulative packet ledger must remain \(o(W/H)\).

Until one of those statements is proved, overlapping joined charts and
owner-fixed spikes do not establish a current-endpoint charged frame or
constant one.
