# PBBS intervals and owner-fixed spikes: an exact current-endpoint frame law

Date: 2026-07-25

Method: pure mathematics only.  No computation, search, solver, or
long-running job is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad W=\binom{2m+1}{m},
 \qquad H=\lceil L\sqrt m\rceil
\]

with fixed \(L>0\).  Assume the recursively conjugate PBBS seed has been
made \(H\)-physical under the residence hypothesis in
`PBBS_SEEDED_INTERVAL_DESCENT_COMPATIBILITY_20260725.md`.  This note
composes its disjoint long-interval layers with the audited upper
owner-fixed spike cubes and resolves the spike endpoint-orientation term
exactly.

The main new identity is the following.  Start at the **current** matching
\(M\), choose \(N\) owner-fixed spike occurrences in one actual source
phase, and let every occurrence be switched independently with common
probability \(s\in[0,1]\).  For each active signed-depth flag, write
\(u_i\) for its current old target and \(v_i\) for its spike image.  If
\(x(\cdot)\) is the current load, define

\[
 \boxed{
 D=\sum_{p}w_p^+
   \sum_{i:\,d_{i,p}\ne0}
       \bigl(x_p(u_{i,p})-1-x_p(v_{i,p})\bigr).}
\tag{0.1}
\]

Let

\[
 G=\left\|\sum_i d_i\right\|_w^2-
   \sum_i\|d_i\|_w^2\ge0
\tag{0.2}
\]

be the exact spike Gram gap.  Then the doubled factorial-floor energy has
the **current-endpoint** law

\[
 \boxed{
 \mathbb E_s\mathcal Q_w(M_s)-\mathcal Q_w(M)
 =s^2G-2sD.}
\tag{0.3}
\]

Here and throughout, \(\mathcal Q_w\) is the autonomous selected-token
flag ledger, or that ledger plus a completion literally common to every
spike corner.  Choice-dependent singleton initialization collars are not
silently included in the Haar identity.  They use \(O(HN)\) literal
positions and are tracked separately below; fitting them into a fixed
\(O(H\operatorname{Cat}_m)\) reserve requires \(N=O(\operatorname{Cat}_m)\).

There is no coherent-endpoint remainder hidden in (0.3).  Optimizing \(s\)
gives a literal integral corner with descent at least

\[
 \boxed{
 \Psi(D,G)=
 \begin{cases}
 0,&D\le0,\\[2mm]
 D^2/G,&0<D<G,\\[2mm]
 2D-G,&D\ge G>0,\\[2mm]
 2D,&G=0<D.
 \end{cases}}
\tag{0.4}
\]

Thus this common-bias independent rounding is current-descending exactly
when its weighted old collision degree exceeds its weighted current image
load.  Repeated spike images do not enter this sign test; their positive
image-image Gram cancels their coherent endpoint collision increment.

The same averaging proves a run-efficient form.  If \(D>0\), some corner
obeys

\[
 \boxed{
 \frac{\mathcal Q_w(M)-\mathcal Q_w(M')}
      {\text{new selected-row runs}}
 \ge \frac{D}{2N},}
\tag{0.5}
\]

with the convention that a zero denominator is omitted.  The corresponding
bound per raw run endpoint is \(D/(4N)\).

For complete collision fibres of multiplicity at least \(K\), let

\[
 C_K=\sum_{U:\,\mu_U\ge K}\binom{\mu_U}{2},
 \qquad N_K=\sum_{U:\,\mu_U\ge K}\mu_U.
\]

Then

\[
 \boxed{
 N_K\le\frac{2C_K}{K-1},
 \qquad
 \Delta J\le\frac{4C_K}{K-1}.}
\tag{0.6}
\]

At the distinguished depth \(q\), their contribution to the positive part
of (0.1) is exactly \(2w_q^+C_K\).  If the complete all-depth orientation
surplus satisfies

\[
 D\ge\eta w_q^+C_K,
\tag{0.7}
\]

then (0.5)--(0.6) give descent per new run at least

\[
 \boxed{\frac{\eta w_q^+}{4}(K-1).}
\tag{0.8}
\]

Consequently \(K/H\to\infty\) makes such spikes super-\(H\)-efficient and,
when \(C_K=O(W)\), gives \(o(W/H)\) new runs and \(o(W)\) literal context.

The composition with PBBS is exact.  The all-adjacent legality/path theorem
in Section 8 permits one full packet corner \(I\), with exact path descent
\(\mathscr D_{\rm int}(I)\) and
\(r_{\rm all}\le r_{\rm odd}+r_{\rm even}=o(W/H)\).  Then apply a
\(q\ge2\) owner-fixed spike cube at that resulting current endpoint.
Some integral final corner satisfies

\[
 \boxed{
 \mathcal Q_{\ge2}(M')
 \le \mathcal Q_{\ge2}(M_0)
   -\mathscr D_{\rm int}(I)-\Psi(D,G),}
\tag{0.9}
\]

and

\[
 \boxed{
 J(M')\le J_0+2r_{\rm all}+2N.}
\tag{0.10}
\]

Every interval corner preserves or improves the PBBS first upper shadow,
and every helper spike based at \(q\ge2\) fixes that shadow pointwise.
Hence (0.9) retains

\[
 O(W\log m/m)=o(H\operatorname{Cat}_m)
\tag{0.11}
\]

first-shadow defect.

At \(q=1\), (0.3) strengthens the audited marker sink.  For complete
fibres, distinct marker images, collision count \(C\), and total current
image load \(B\),

\[
 G=2C,
 \qquad D=2C-B.
\]

Thus the optimized current-descent criterion is

\[
 \boxed{B<2C,}
\tag{0.12}
\]

improving the fair-bit sufficient condition \(B<3C/2\).

This is a decisive current-endpoint lemma, but not yet the requested full
charged frame.  The exact missing inequality is now

\[
 \sup_{\substack{I\text{ full adjacent packet corner}\\
                   \mathscr S\text{ post-}I\text{ spikes}\\
                   2r_{\rm all}+2|\mathscr S|=o(W/H)}}
 \left(
  \mathscr D_{\rm int}(I)
  +\Psi(D_{I,\mathscr S},G_{I,\mathscr S})
 \right)
 \ge
 \gamma_L\bigl(
   \mathcal Q_{\ge2}-C_LH\operatorname{Cat}_m
 \bigr).
\tag{0.13}
\]

Neither PBBS marginal balance nor the present spike theorem proves
(0.13).  Two exact obstructions remain: a diffuse multiplicity-
\(O(H)\) sector cannot be touched by owner-fixed leaves in \(o(W/H)\)
blocks, and a spike family with \(D\le0\) has no descent under **any**
common biased independent rounding.  Section 8 strengthens this to arbitrary
product biases when every individual shield surplus is nonpositive.  Long intervals must charge the first
sector, while a new image-load routing or joined-frame theorem must rule
out the second.  No constant-one conclusion is claimed.

Section 8 identifies the residual null cone exactly.  Interval nullity is
packet monochromaticity on every positive target-path edge together with
the requirement that positive edges form a path matching.  Owner-spike
cube nullity is the pointwise shield inequality

\[
 \sum_pw_p^+
 \bigl(x_p(u_{i,p})-1-x_p(v_{i,p})\bigr)\le0
\]

on every admissible weighted occurrence arc.  In the rank-two projection,
where the integral floor is the all-one vector, these conditions admit a canonical
\(\Theta(W)\)-dimensional double/hole family of energy \(\Theta(W)\) and
direct escape cost \(\Omega(W/H)\).  This is an exact target-graph
obstruction to a rankwise frame.  Lifting it through all depths inside one
physical PBBS factor, or proving that no such lift exists, is the surviving
chronology fork.

## 1. Exact floor normalization

At upper depth \(p\), let \(K_p\) be the number of targets and let every
corner have the same integral mass \(T_p\).  Write

\[
 T_p=c_pK_p+\delta_p,
 \qquad0\le\delta_p<K_p.
\]

The doubled factorial-floor excess is

\[
 Q_p(x)=\sum_Z(x_Z-c_p)(x_Z-c_p-1).
\tag{1.1}
\]

On a fixed-mass fibre, the difference between \(Q_p(x)\) and
\(\sum_Zx_Z^2\) is constant.  Therefore every calculation below may be
made with squared loads and is automatically floor-corrected.  No
divisibility and no positive first-rank floor quotient is assumed.

The statement remains exact after adding any flag profile which is common
to all corners.  A corner-dependent physical initialization profile is a
different object; only its \(O(HN)\) literal size, not its quadratic energy,
is asserted here.

All lower flags of an upper owner-fixed spike are fixed.  We therefore
stack only the changed upper ranks with arbitrary finite nonnegative
weights \(w_p^+\).

## 2. Current-endpoint collision-pair decomposition

Fix one actual source phase with omitted pair \(A\).  Select \(N\) current
tokens in that phase.  Each token may have its own distinguished depth
\(q_i\ge1\).  Use the audited helper construction: if \(b_i\) enters at
depth \(q_i\), choose

\[
 z_i\notin U_H(e_i)\cup A,
 \qquad B_i=\{b_i,z_i\},
\]

and exchange \(A\) with \(B_i\).  Give every auxiliary row its factor-copy
label, or fix one canonical conjugacy whenever a leaf pair repeats.

The selected lower--owner incidence is fixed pointwise.  At every changed
upper rank, the old target \(u_{i,p}\) avoids \(A\), while the image
\(v_{i,p}\) meets \(A\).  Hence the old and image target families are
disjoint.

For a fixed rank \(p\), let

\[
 r^-_{p,u}=|\{i:u_{i,p}=u\}|,
 \qquad
 r^+_{p,v}=|\{i:v_{i,p}=v\}|.
\tag{2.1}
\]

Only indices with nonzero innovation are included.  Put

\[
 \alpha_{p,u}=x_p(u)-r^-_{p,u},
 \qquad
 \beta_{p,v}=x_p(v).
\tag{2.2}
\]

Thus \(\alpha\) is the old load not selected for removal, while \(\beta\)
is the current external load at an image target.  Define

\[
 \begin{aligned}
 C^-&=\sum_pw_p^+\sum_u\binom{r^-_{p,u}}2,&
 E^-&=\sum_pw_p^+\sum_u\alpha_{p,u}r^-_{p,u},\\
 C^+&=\sum_pw_p^+\sum_v\binom{r^+_{p,v}}2,&
 E^+&=\sum_pw_p^+\sum_v\beta_{p,v}r^+_{p,v}.
 \end{aligned}
\tag{2.3}
\]

The collision pairs removed by the coherent all-spike endpoint are
\(E^-+C^-\); those inserted are \(E^++C^+\).  Therefore its exact
doubled-floor drift is

\[
 \boxed{\Delta=2(E^++C^+-E^--C^-).}
\tag{2.4}
\]

The old/image cross equalities are impossible.  Hence the exact joined
Gram is

\[
 \boxed{G=2(C^-+C^+)\ge0.}
\tag{2.5}
\]

Finally set

\[
 \boxed{D=E^-+2C^--E^+.}
\tag{2.6}
\]

Equations (2.4)--(2.6) give

\[
 \boxed{\Delta=G-2D.}
\tag{2.7}
\]

The occurrence form of (2.6) is exactly (0.1), because for a target with
selected multiplicity \(r\) and total load \(x=\alpha+r\),

\[
 r(x-1)=\alpha r+r(r-1)
       =\alpha r+2\binom r2.
\tag{2.8}
\]

Thus selected--selected old collision pairs have coefficient two in
\(D\), selected--unselected pairs have coefficient one, untouched pairs
have coefficient zero, and every unit of current image load has coefficient
minus one.  This is the exact collision-pair frame decomposition at the
current endpoint.

## 3. Biased Haar optimization

Let \(\xi_i\) be independent Bernoulli variables with common mean \(s\).
The random profile is

\[
 f_s=f+\sum_i\xi_i d_i.
\]

The exact endpoint/Haar identity gives

\[
 \mathbb E_s\mathcal Q_w(f_s)-\mathcal Q_w(f)
 =s\Delta-s(1-s)G.
\tag{3.1}
\]

Substitute (2.7) to obtain (0.3):

\[
 s\Delta-s(1-s)G=s^2G-2sD.
\]

The right side is a convex quadratic in \(s\).  Its minimum on \([0,1]\)
is attained at \(s=0\) when \(D\le0\), at \(s=D/G\) when
\(0<D<G\), and at \(s=1\) when \(D\ge G\).  This proves (0.4).
For \(G=0\), the drift is \(-2sD\), proving the last case.

Because the expectation is an average over literal legal corners, some
integral corner realizes at least the descent (0.4).

There is also an exact energy-per-run extraction.  Let \(R(\xi)\) be the
number of switched occurrences.  Then

\[
 \mathbb ER=sN.
\]

If every corner with \(R>0\) had

\[
 \frac{\mathcal Q_w(M)-\mathcal Q_w(M_\xi)}{R}
 <\frac{\Psi(D,G)}{sN},
\]

averaging would contradict the definition of \(\Psi\).  Hence one corner
has descent per switched occurrence at least \(\Psi/(sN)\).  For the
optimizing \(s\), this is \(D/N\) when \(0<D<G\), and at least \(D/N\)
when \(D\ge G\).  Switching one occurrence adds at most two selected-row
runs and four raw endpoints.  This proves (0.5).

This optimization strictly strengthens fair rounding.  Fair bits give
current descent only when \(D>G/4\), whereas an
optimized bias gives descent for every \(D>0\).

## 4. Complete fibres and the orientation charge

Fix a distinguished depth \(q\), one source phase, and a family of complete
source-phase collision subfibres \(G_U\) with multiplicities
\(\mu_U\ge K\).  Select every occurrence of that source phase in these
subfibres.  Other source phases, if present after an earlier mixed interval
corner, are left in the external old load and only improve the old-degree
side of the orientation balance.  At depth \(q\),

\[
 C_q^-=w_q^+C_K.
\]

Define the remaining old-degree bonus and complete image-load charge by

\[
 R_K^{\rm old}
 =\sum_{p=q}^Hw_p^+
   \sum_i\bigl(x_p(u_{i,p})-1\bigr)-2w_q^+C_K,
\tag{4.1}
\]

\[
 B_K^{\ge q}
 =\sum_{p=q}^Hw_p^+
   \sum_i x_p(v_{i,p}).
\tag{4.2}
\]

The helper spike fixes every earlier upper flag.  Equation (0.1) becomes

\[
 \boxed{
 D=2w_q^+C_K+R_K^{\rm old}-B_K^{\ge q}.}
\tag{4.3}
\]

Here \(R_K^{\rm old}\ge0\): at depth \(q\), the selected--selected degree
is exactly \(2C_K\), and every selected--unselected old collision is an
additional nonnegative term; all deeper old degrees are also nonnegative.

Thus the exact current-orientation condition is

\[
 \boxed{
 B_K^{\ge q}<2w_q^+C_K+R_K^{\rm old}.}
\tag{4.4}
\]

No image-image multiplicity occurs in (4.4).  Such multiplicity enlarges
both the endpoint drift and the Gram by the same amount.

The elementary inequality

\[
 \binom\mu2\ge\frac{\mu(K-1)}2
 \qquad(\mu\ge K)
\]

gives (0.6).  If (0.7) holds, (0.5) and (0.6) yield

\[
 \frac{\text{descent}}{\text{new runs}}
 \ge\frac{D}{2N_K}
 \ge\frac{\eta w_q^+C_K}{4C_K/(K-1)}
 =\frac{\eta w_q^+}{4}(K-1),
\]

which proves (0.8).

For \(K=H g_m\) with \(g_m\to\infty\) and \(C_K=O(W)\),

\[
 \Delta J=O\!\left(\frac{W}{Hg_m}\right)=o(W/H),
 \qquad
 O(HN_K)=O(W/g_m)=o(W).
\tag{4.5}
\]

If one insists that spike contexts themselves fit the sharper fixed
Catalan reservoir \(O(H\operatorname{Cat}_m)=O(HW/m)\), then

\[
 N_K=O(\operatorname{Cat}_m)
\tag{4.6}
\]

is required.  For a reservoir \(C_K=\Theta(W)\), (0.6) guarantees (4.6)
only at the stronger threshold \(K=\Omega(m)\).  Thus the mesoscopic range

\[
 H\ll K\ll m
\]

is coefficient-one cheap but is not automatically chargeable to one fixed
\(O(H\operatorname{Cat}_m)\) context reserve.  This distinction is exact.

### 4.1 A two-marker image-load bound

There is a nontrivial bound on the distinguished-rank part of the image
charge.  It does not close the all-depth frame, but it converts the raw
endpoint orientation into collision quantities at two adjacent ranks.

For a selected occurrence at depth \(q\), put

\[
 R_i=U_{q-1}(e_i),
 \qquad U_q(e_i)=R_i\cup\{b_i\}.
\]

Write the omitted source pair as \(A=\{a_1,a_2\}\).  The two possible
canonical marker choices give the two distinguished-rank images

\[
 V_{R_i,h}=R_i\cup\{a_h\},
 \qquad h=1,2.
\tag{4.7}
\]

Under the labelled-fresh-copy convention, choose for each occurrence the
marker with smaller current image load.  If

\[
 r_R=|\{i:R_i=R\}|,
 \qquad y_{R,h}=x_q(V_{R,h}),
\]

then its distinguished-rank image charge is

\[
 B_q=\sum_Rr_R\min\{y_{R,1},y_{R,2}\}.
\tag{4.8}
\]

The targets \(V_{R,h}\) are pairwise distinct as \((R,h)\) varies: every
old \(R\) avoids \(A\), so deleting the unique member of \(A\) recovers
both \(R\) and \(h\).  Put

\[
 C_{q-1}^{\rm pred}=\sum_R\binom{r_R}{2},
\]

\[
 P_q(\mathcal V)=\sum_{R,h}\binom{y_{R,h}}2,
 \qquad
 M_q(\mathcal V)=\sum_{R,h}y_{R,h}.
\]

For nonnegative integers \(r,y\),

\[
 ry\le\binom r2+\binom y2+\frac{r+y}{2},
\tag{4.9}
\]

because the right side minus the left side is \((r-y)^2/2\).  Using
\(\min(y_1,y_2)\le(y_1+y_2)/2\) and summing (4.9) gives the exact bound

\[
 \boxed{
 B_q\le
 C_{q-1}^{\rm pred}
 +\frac12P_q(\mathcal V)
 +\frac12N
 +\frac14M_q(\mathcal V).}
\tag{4.10}
\]

Moreover,

\[
 C_{q-1}^{\rm pred}
 \le\sum_R\binom{x_{q-1}(R)}2,
 \qquad
 P_q(\mathcal V)\le\sum_V\binom{x_q(V)}2,
 \qquad
 M_q(\mathcal V)\le T.
\tag{4.11}
\]

If the selected distinguished-rank source subfibres have collision count
\(C_K\), their old degree at that rank is at least \(2C_K\).  Therefore

\[
 \boxed{
 D_q\ge
 2w_q^+C_K-w_q^+\left(
 C_{q-1}^{\rm pred}+\frac12P_q(\mathcal V)
 +\frac12N+\frac14M_q(\mathcal V)
 \right).}
\tag{4.12}
\]

Thus a large depth-\(q\) spike can be shielded at its distinguished rank
only by predecessor collisions, collisions already present on its two
marker image sectors, or linear flag mass.  This is a genuine vertical
charge, but it is not yet (0.13): the same marker controls all higher
images, whose loads occur in \(B_K^{\ge q}\), and (4.10) does not bound
that tail.

## 5. The improved first-shadow sink

At \(q=1\), use the fixed-marker construction from the audit.  At a
coherent first-avoided endpoint, or whenever the selected fibres are
globally complete, they have no unselected old load, and their image
targets are distinct.  With

\[
 C=\sum_U\binom{\mu_U}{2},
 \qquad
 B=\sum_i x_1(v_i),
\]

we have

\[
 C^-=C,
 \qquad C^+=0,
 \qquad E^-=0,
 \qquad E^+=B.
\]

Therefore

\[
 G=2C,
 \qquad D=2C-B,
\tag{5.1}
\]

and (0.12) follows.  If \(0<2C-B<2C\), the exact guaranteed descent is

\[
 \boxed{
 \frac{(2C-B)^2}{2C}.}
\tag{5.2}
\]

The fair-bit identity in the audit gives descent only when
\(B<3C/2\).  The interval \(3C/2\le B<2C\) is a genuine gain from biased
optimization.

If labelled fresh copies allow the lower-loaded one of the two markers to
be chosen occurrence by occurrence, then at \(q=1\) the predecessors are
the distinct middle owners.  Equation (4.8) has \(r_R=1\), and the two
candidate-image families are disjoint.  Consequently

\[
 B\le\frac12M_1(\mathcal V)\le\frac T2.
\tag{5.3}
\]

Thus every complete first-shadow reservoir with \(C>T/4\) is
unconditionally current-descending under this fresh-copy convention.  In
the stricter one-factor-per-leaf model the marker cannot be reoriented
independently on repeated leaves, so (5.3) is not asserted there.

For the PBBS composition, no first-shadow spike is needed: its seed defect
is already

\[
 O(W\log m/m)=o(H\operatorname{Cat}_m),
\]

because \(H\operatorname{Cat}_m\asymp_LW/\sqrt m\).  We retain (5.1)--(5.2)
as a current-endpoint fallback.

## 6. Sequential PBBS compatibility

Let \(M_0\) be the \(H\)-physical recursively conjugate PBBS seed.  Choose
one full all-adjacent packet corner \(I\).  The legality and signed-path
theorem in Section 8 gives a literal corner \(M_I\) with

\[
 \mathcal Q_{\ge2}(M_I)
 \le\mathcal Q_{\ge2}(M_0)
   -\mathscr D_{\rm int}(I),
 \qquad
 J(M_I)\le J_0+2r_{\rm all},
\tag{6.1}
\]

where \(r_{\rm all}\le r_{\rm odd}+r_{\rm even}=o(W/H)\).

Its lower ledger is exact and its first upper shadow is no worse than that
of \(M_0\).

Now group any chosen current tokens of \(M_I\) by their **actual** source
phase.  Apply the owner-fixed theorem to one group.  Its central
lower--owner incidences are unchanged, so it cannot invalidate the interval
corner's lower saturation or middle injectivity.  When its distinguished
depths satisfy \(q_i\ge2\), every first upper flag is also fixed.  Applying
Section 3 at the current endpoint \(M_I\) proves (0.9)--(0.10).

Auxiliary conjugate rows are treated as labelled fresh physical sources,
as permitted in the audited spike theorem.  They therefore do not impose a
triangle-holonomy relation on the recursively conjugate PBBS path.  If a
formal model instead permits only one globally preattached factor for each
omitted pair, this fresh-copy convention is unavailable and the known
star/path holonomy is an additional obstruction; the present composition
theorem is explicitly not asserting that stronger fixed-factor statement.

Different source phases need not be put in one Gram cube.  They may be
tested sequentially at their then-current endpoints, recomputing \(D\) each
time.  Every accepted step with \(D>0\) decreases the exact energy.  This
observation gives a legal greedy schedule, but by itself gives neither a
lower bound on the sum of its decreases nor a no-reuse run bound.

## 7. Why the full frame does not yet follow

At a current target, color occurrence vertices selected or unselected.
Its collision pairs decompose exactly as

\[
 \binom{x}{2}
 =\binom r2+r(x-r)+\binom{x-r}{2}.
\tag{7.1}
\]

The spike orientation budget counts the first class twice, the second once,
and the third not at all; it then subtracts the current image loads.  This
is (2.6).  The long interval layer separately counts only equal-target
pairs lying in different active physical packets.  Therefore every
collision pair is now assigned to one of three explicit ledgers:

1. interval within-edge and joined adjacent-path charge;
2. spike old-degree charge, reduced by image-load orientation;
3. an untouched diffuse/invariant remainder.

The exact arithmetic floor is subtracted only from their total.  To prove
(0.13), one must show that the third ledger, together with every nonpositive
orientation balance \(D\), has floor surplus only
\(O_L(H\operatorname{Cat}_m)\).

The existing hypotheses do not give this.  There are two quantitative
reasons.

First, if \(D\le0\), (0.3) is nonnegative for every \(s\in[0,1]\).  Thus
no common biased independent rounding of this exact spike cube descends
from the current endpoint.  This closes the biased-orientation shortcut;
one needs a new image routing, a nonproduct signing, or a joined chart.

Second, the helper spike has a sparse fixed-leaf carrier.  Along an
\(H\)-physical transition run, the coordinates entering in any \(H\)
consecutive transitions are distinct; otherwise the union of the
corresponding \(H+1\) states would have size less than \(m+H\).  For a
fixed helper leaf \(B=\{b,z\}\), the distinguished entering coordinate
must be one of these two coordinates.  Hence a consecutive carrier block
has length at most two when \(H\ge3\), and in all cases at most \(H\).
Therefore moving \(M\) diffuse occurrences at depth \(q\) needs at least

\[
 \frac{M}{H}
\tag{7.2}
\]

alternate leaf-row blocks.  For \(q\le H\), touching \(\Theta(W)\)
bounded-multiplicity occurrences costs \(\Omega(W/H)\) blocks, whereas the
coefficient-one ledger requires \(o(W/H)\).  Owner-fixed singleton/fixed-
leaf spikes cannot replace the missing diffuse fusion theorem.

These are rigorous obstructions to two specific completion mechanisms, not
counterexamples to the combined PBBS architecture.  The current exact
boundary is (0.13): prove it by showing that long intervals cover the
diffuse sector and that the surviving spike image-load balances have
positive aggregate \(D\), or construct a physical PBBS endpoint violating
that statement.  Neither is done here.

## 8. Exact residual null cone and its canonical diffuse wall

The two chart families admit a precise null-space description on the
current occurrence/target graph.  It is useful to state it because it
shows that the residual is not known to be low-dimensional.

### 8.1 The occurrence collision graph

At depth \(p\), make one vertex for every current flag occurrence and join
two vertices when they have the same target.  Thus a target of load \(t\)
gives a clique \(K_t\), and the number of graph edges is the raw collision
sum.

For adjacent block \(j\), retain only vertices whose occurrences are
movable by that block and whose common target moves nontrivially.  Color
such vertices by their maximal physical carrier packet.  The PBBS
within-edge interval charge on this target is

\[
 \sum_{I<J}k_I k_J,
\tag{8.1}
\]

The recursively conjugate PBBS family in fact permits all adjacent blocks
simultaneously.  The neighboring-block owner cases are separated by phase
injectivity: a block-\(j\) phase-\((j+1)\) candidate and a block-
\((j+1)\) phase-\((j+2)\) candidate can coincide only if their common
owner avoids both exchanged pairs, in which case conjugacy and injectivity
force their disjoint lower roots to be equal.  Thus the all-adjacent target
graph is a union of directed category-increasing paths.

The complete owner/background and run audit appears in
`MATH_AUDIT_PBBS_OVERLAPPING_SPIKE_RESIDUAL_KERNEL_20260725.md`; the
argument above is the only new neighboring-block case beyond disjoint-layer
legality.

On one such path write the base loads as

\[
 x_0\ge x_1\ge\cdots\ge x_s,
 \qquad d_i=x_i-x_{i+1}.
\]

The coherent block swap moves exactly \(d_i\) occurrences across edge
\(i\).  If a packet corner moves \(0\le\ell_i\le d_i\), direct expansion
of the squared loads gives the exact doubled-floor drop

\[
 \boxed{
 \mathscr D_{\rm path}(\ell)
 =2\sum_i\ell_i(d_i-\ell_i)
  +2\sum_i\ell_i\ell_{i+1}.}
\tag{8.1a}
\]

Every term is nonnegative.  A particular interval corner is flat exactly
when

\[
 \ell_i\in\{0,d_i\}\quad\text{for every }i,
 \qquad
 \ell_i\ell_{i+1}=0\quad\text{for every }i.
\tag{8.1b}
\]

where \(k_I\) is the number of its vertices of packet color \(I\).
Consequently:

\[
 \boxed{
 \begin{aligned}
 &\text{no corner of the full adjacent interval cube descends}\\
 &\quad\iff\quad
 \text{every positive-capacity edge is carried by one packet, and}\\
 &\hspace{34mm}
 \text{the positive-capacity edges form a matching on every target path.}
 \end{aligned}}
\tag{8.2}
\]

Indeed, two packets on one positive edge permit a proper
\(0<\ell_i<d_i\), while two consecutive positive edges may both be
switched coherently and activate the second sum in (8.1a).  Conversely,
the two displayed conditions force every corner to satisfy (8.1b).
Occurrences outside every adjacent carrier, targets fixed by the adjacent
exchange, and isolated final-category targets are automatically in this
interval-null sector.

### 8.2 The owner-spike shield graph

For one source phase, give every admissible owner-fixed realization of
occurrence \(i\) a directed arc from its old flag chain to its image flag
chain.  Give that arc the current degree surplus

\[
 \delta_i
 =\sum_{p:\,d_{i,p}\ne0}w_p^+
   \bigl(x_p(u_{i,p})-1-x_p(v_{i,p})\bigr).
\tag{8.3}
\]

The first term is the weighted degree of occurrence \(i\) in the old
collision graph.  The last term is the weighted number of current
occurrences shielding its image targets.  Equation (0.1) says

\[
 D_{\mathscr S}=\sum_{i\in\mathscr S}\delta_i.
\tag{8.4}
\]

There is an exact strengthening of the common-bias nullity.  Give the
spike bits arbitrary independent probabilities \(s_i\).  The one-bit
marginal is \(-2\delta_i\), and the audited within-phase cross-Grams are
nonnegative.  Hence

\[
 \mathbb E(Q'-Q)
 =-2\sum_i s_i\delta_i
   +2\sum_{i<k}s_is_k\langle d_i,d_k\rangle_w.
\tag{8.5}
\]

It follows that

\[
 \boxed{
 \begin{aligned}
 &\delta_i\le0\text{ for every admissible spike arc }i\\
 &\quad\iff\\
 &\text{no literal corner of any owner-fixed spike cube in this source}\\
 &\qquad\text{phase descends from the current endpoint.}
 \end{aligned}}
\tag{8.6}
\]

The reverse implication uses a deterministic singleton: if
\(\delta_i>0\), then switching only \(i\) changes the doubled energy by
\(-2\delta_i<0\).  If all \(\delta_i\le0\), the deterministic specialization
of (8.5) is nonnegative for every subset because every cross-Gram is
nonnegative.  Thus (8.6) is an exact null cone, not only a sufficient
shield condition.

Combining (8.2) and (8.6), the residual null cone of the present menu
at one fixed endpoint consists precisely of:

1. packet-monochromatic positive path edges, with those edges forming a
   matching in every target path;
2. owner-spike arcs dominated by at least as much current image load as old
   collision degree; and
3. the arithmetic factorial-floor wall, which must be quotiented before
   any excess is claimed.

For the **sequential** interval-then-spike menu, one extra orbit
quantifier is necessary.  When (8.2) holds, every permitted flat corner is
a collection of complete coherent swaps on nonadjacent target-path edges.
Let \(\mathscr O_{\rm int}(M)\) be the finite set of endpoints obtained
from these zero-charge matching swaps.  Then

\[
 \boxed{
 M\text{ is null for one full interval cube followed by one spike step}
 \iff
 \delta_i(M')\le0
 \text{ for every }M'\in\mathscr O_{\rm int}(M)
 \text{ and every admissible arc }i.}
\tag{8.6a}
\]

Indeed, a positive arc after a flat packet choice gives a descending
singleton.  Conversely, (8.2) makes the interval step flat and (8.6)
makes every subsequent within-phase spike corner nondecreasing.  For a
renewed sequence which rebuilds interval packets after a mixed endpoint,
the same statement uses the iterated orbit closure; controlling that larger
closure is exactly the renewal problem, not a consequence of one-round
compatibility.

The PBBS first-shadow theorem puts the \(p=1\) part of this cone inside
\(o(H\operatorname{Cat}_m)\).  No analogous dimension bound is known for
\(p\ge2\).

The arithmetic wall is visible directly in (8.3).  At a rank with floor
loads \(c,c+1\), an arc from a \((c+1)\)-loaded target to a \(c\)-loaded
target has

\[
 (c+1)-1-c=0.
\]

It transports a collision without crossing below the integral floor.  A
strict current descent requires an arc which actually connects an overload
to a load below this adjacent floor wall, or a multi-occurrence joined
effect not represented by independent owner spikes.

### 8.3 A canonical rank-two floor-wall family

At depth two there is an especially transparent obstruction.  Here

\[
 K_2=\binom{2m+1}{m+2}
    =\binom{2m+1}{m-1}=T,
\]

so the exact arithmetic floor is the all-one load vector.  Choose \(R\)
targets \(U_1,\ldots,U_R\) and \(R\) targets
\(Z_1,\ldots,Z_R\), and set

\[
 x(U_r)=2,
 \qquad x(Z_r)=0,
 \qquad x(V)=1\quad\text{otherwise}.
\tag{8.7}
\]

The mass is still \(T\), while the doubled floor excess is exactly

\[
 \boxed{Q_2(x)=2R.}
\tag{8.8}
\]

Indeed, in \(Q_2=\sum_V(x_V-1)(x_V-2)\), an overloaded coordinate
contributes zero and its compensating hole contributes two.

Use the first omitted pair \(P_1\), and choose every \(U_r\) and every
hole \(Z_r\) to avoid both \(P_1,P_2\).  Such targets are fixed pointwise
by the only possible outgoing adjacent exchange, and category one has no
incoming edge.  Their number is

\[
 F_2=\binom{2m-3}{m+2},
 \qquad
 \frac{F_2}{K_2}\longrightarrow\frac1{16}.
\tag{8.8a}
\]

Thus they are genuinely isolated vertices of the full adjacent path graph,
not merely declared isolated in an arbitrary graph.

Attach two source-\(P_1\) occurrence vertices to every \(U_r\).  An upper
owner spike can change the rank-two target only when its distinguished
depth is one or two.  Each choice has two markers, so one occurrence has
at most four rank-two marker images and one load-two gadget has at most
eight.  At the incidence level, choose the two depth-one predecessors
\(U_r\setminus\{b_{r,1}\}\) and
\(U_r\setminus\{b_{r,2}\}\) globally distinct.  Since
\(R\le F_2/3\), this choice follows greedily: after \(t\) gadgets, the
\(2t\) used predecessors have at most \(2t(m-4)\) incidences with future
\(U\)'s, so fewer than \(2t\) candidates have at most one unused
predecessor; together with the \(t\) already used candidates this leaves a
new choice while \(3t<F_2\).  Thus the wall does not force any
first-shadow duplicate.  Every
rank-two marker image has exactly one coordinate of \(P_1\) and avoids
\(P_2\); that image sector has size

\[
 2\binom{2m-3}{m+1}=\Theta(K_2).
\tag{8.8b}
\]

This image sector is disjoint from both the overload and hole sectors,
whether or not different occurrences have repeated images.  Repeated
images only add a nonnegative spike cross-Gram.  Choose disjoint overloads
and holes inside the family (8.8a), taking

\[
 R=\left\lfloor\frac{F_2}{3}\right\rfloor.
\tag{8.8c}
\]

Every target outside the overload/hole family has load one.  Therefore all
incoming and outgoing path neighbors of a marker image also have load one,
so their path capacities are zero.  The interval-flat orbit cannot move a
hole onto a marker image.

Every available rank-two image of an overloaded occurrence has load at
least one.  Since its old load is two,

\[
 \delta_{i,2}=2-1-x_2(v_i)\le0.
\tag{8.9}
\]

Equations (8.2), (8.6a), and (8.9) make (8.7) a null configuration for the
rank-two projection of the full adjacent interval/product-spike menu,
despite its energy (8.8).  Moving one
occurrence from load two to an image of load one merely transports the
collision; it does not fill a hole.

At the packet-incidence level, the \(2R\) displayed old occurrences may be
placed in abstract source packets of length \(\Theta(m)\), using

\[
 O(R/m)=O(W/m)=o(W/H)
\tag{8.9a}
\]

packets at \(H=L\sqrt m\).  This is a low-packet incidence assignment, not
an assertion that the canonical PBBS factor realizes the prescribed
nested flags.

The choices \(e_{U_r}-e_{Z_r}\) contain \(\Theta(K_2)=\Theta(W)\)
independent directions.  Thus the canonical target-graph null family is
linear-dimensional, not \(o(W)\)-dimensional.  Escaping it by direct
owner-fixed leaf pieces must touch \(\Theta(W)\) diffuse occurrences, and
the carrier bound (7.2) costs \(\Omega(W/H)\) alternate blocks rather than
\(o(W/H)\).

Using (8.8a)--(8.8c) and \(K_2=T=(m/(m+2))W\),

\[
 \frac{Q_2(x)}{H\operatorname{Cat}_m}
 =\left(\frac{1}{12L}+o_L(1)\right)\sqrt m\longrightarrow\infty.
\tag{8.10}
\]

So the projected wall is genuinely above the permitted Catalan scale.

This is a rigorous obstruction in the exact rank-two occurrence/target
projection with the exact floor and the exact projected menus above.  It is
**not** yet a full-window counterexample made from one physical PBBS factor:
simultaneously realizing \(\Theta(W)\) such path-isolated double/hole
gadgets with nested higher PBBS flags whose tail shield
inequalities also hold is not proved.  The chronology fork is therefore
exact:

* prove that physical PBBS incidence excludes or fuses this
  \(\Theta(W)\)-dimensional floor wall; or
* realize it in one PBBS seed, which would refute the desired current-frame
  inequality (0.13).

Absent that genuinely physical theorem, the combined chart menu does not
have a proved \(o(W)\)-dimensional or Catalan-cheap residual.

No coefficient-one conclusion is claimed.
