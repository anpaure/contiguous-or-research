# Multidepth marked-gap obstruction to weighted-cover minimax

Date: 2026-07-25

Method: pure mathematics only.  No web search, computation, finite search,
solver, or long-running job is used.

## 0. Result

Let

\[
 n=2m+1,\qquad W=\binom nm,\qquad B=W/n=\operatorname{Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil .
\]

Throughout, \(A>0\) is fixed and \(m\) is sufficiently large that
\(H\le m-1\).

The proposed estimate

\[
 O_q(F_m^{\rm MSW})=O_A(qB)
\]

for the canonical MSW exact factor is false, and its possible aggregate
consequence \(\sum_{q\le H}O_q=O_A(W)\) is false as well.  The already
audited marked-gap collisions at depth one persist, at the same pointed
slots, through every lower depth.  If

\[
 P_q(F):=\sum_{S\in\binom{[n]}{m-q}}
              \left\lfloor\frac{\ell_q^F(S)}2\right\rfloor,
\]

then

\[
 P_q(F_m^{\rm MSW})
 \ge K_m:=(2m-3)\operatorname{Cat}_{m-2}
 \qquad(1\le q\le m-1).
\]

Consequently, for every

\[
 0<a<\sqrt{\log(16/15)},
\]

uniformly for \(1\le q\le a\sqrt m\),

\[
 \boxed{
 O_q(F_m^{\rm MSW})
 \ge\bigl(e^{-a^2}-15/16-o(1)\bigr)W.}
\]

Thus, for every fixed \(A>0\),

\[
 \boxed{
 \sum_{q=1}^{\lceil A\sqrt m\rceil}
 O_q(F_m^{\rm MSW})=\Omega_A(HW).}
\]

The same conclusion holds in a positive-density row neighbourhood of every
coordinate relabelling of the MSW factor.  More exactly, if \(F=F_m\) is at
row distance \(b_m=\beta_m B\) from such a relabelling, then on the same range

\[
 \boxed{
 \frac{O_q(F)}W
 \ge e^{-a^2}-\frac{15}{16}-\frac{\beta_m}2-o(1).}
\]

Hence the lower bound is uniformly positive whenever, for some fixed
\(\eta>0\),

\[
 \limsup_{m\to\infty}\beta_m
 \le2(e^{-a^2}-15/16)-\eta.
\]

Every monotone-release completion of a factor in this fixed-margin basin
has tail area \(\Omega_{A,a,\eta}(HW)\), and its weighted common-owner
overload incidence has the same lower bound on the early subwindow.  In particular it cannot prove
\(\mathrm{MR}_A=o(W)\), and the canonical MSW factor cannot supply the
stronger \(O_A(W)\) spill estimate sought for constant-one extraction.

Finally, the coordinate-orbit barycentre of the canonical factor has
perfectly uniform fractional loads at every depth.  For the explicitly
defined balanced-overload relaxation in Section 6, the preceding theorem
gives an \(\Omega_A(HW)\) integrality gap inside the convex hull of that
orbit.  Thus coordinate averaging inside the MSW orbit cannot prove the
\(o(W)\) monotone-release or \(O_A(W)\) aggregate-spill estimates.  This
does not by itself decide A's density-weighted extraction inequality,
whose positive shoulder term may also be of order \(HW\).

This is a no-go theorem for the \(o(W)\) monotone-release and
\(O_A(W)\)-spill implementations on the canonical orbit and its local
basin, not a counterexample to density-weighted extraction or to the
existence of a factor satisfying the constant-one inequality.

## 1. Persistence of the audited marked-gap certificates

The insertion--erasure theorem in
`MATH_ATTACK_I_MARKED_GAP_COLLISION_INDEPENDENT_AUDIT_20260725.md`
constructs, for every

\[
 R\in\mathcal D_{m-2}
 \quad\hbox{and every one of its }2m-3\hbox{ gaps},
\]

two canonical MSW rows.  Their marked depth-one occurrences are distinct
over all certificates and have one common rank-\((m-1)\) target.  Thus the
number of disjoint occurrence pairs is

\[
 K_m=(2m-3)\operatorname{Cat}_{m-2}.
\tag{1.1}
\]

The audit proves slightly more ordering information than equality of the
depth-one sets.  After cyclically rotating the omitted-label orders to the
marked cut, they have the form

\[
 q(R^{(i)})=(\pi_i,t_0,t_1,\ldots,t_{2m-4}),
\tag{1.2}
\]

with the same ordered outside word for \(i=0,1\).  Multiplication of cyclic
positions by two converts (1.2) into the ordinary contiguous-interval
orders.  Writing \(\pi_i=(\pi_{i,0},\ldots,\pi_{i,3})\), the resulting
ordinary row is, exactly,

\[
 (\pi_{i,0},\pi_{i,2},
   t_0,t_2,\ldots,t_{2m-4},
   \pi_{i,1},\pi_{i,3},
   t_1,t_3,\ldots,t_{2m-5}).
\tag{1.3}
\]

Indeed, multiplication by two first visits the even positions
\(0,2,4,\ldots,2m\) and then, after reduction modulo \(2m+1\), the odd
positions \(1,3,5,\ldots,2m-1\).  Thus in both rows it produces the same
ordered block

\[
 \mathsf E=(t_0,t_2,\ldots,t_{2m-4}),
 \qquad |\mathsf E|=m-1,
\tag{1.4}
\]

at the marked slot.  This is the ordered form of the audited depth-one
target.

### Lemma 1.1 -- multidepth persistence

Every marked-gap certificate in (1.1) gives a common same-start target at
every depth \(1\le q\le m-1\), namely

\[
 \operatorname{pre}_{m-q}\mathsf E.
\tag{1.5}
\]

The two pointed occurrences in every pair, and all pointed occurrences
belonging to different certificate pairs, remain distinct.

#### Proof

The canonical same-start depth-\(q\) target is the first \(m-q\) entries of
the ordered depth-one block (1.4), namely the exact set

\[
 S_{R,g,q}=\{t_0,t_2,\ldots,t_{2(m-q-1)}\}.
\tag{1.6}
\]

This proves (1.5).  The pointed physical
start is unchanged when the interval is shortened.  Distinctness at depth
one was proved in the marked-gap audit by recovering the inserted gap and
root from the root and pointed cut.  Hence the same marked starts remain
distinct at every depth. \(\square\)

### Corollary 1.2 -- pair-mass lower bound

For the canonical MSW factor,

\[
 \boxed{P_q(F_m^{\rm MSW})\ge K_m
 \qquad(1\le q\le m-1).}
\tag{1.7}
\]

#### Proof

A target fibre of load \(t\) contains at most \(\lfloor t/2\rfloor\)
pairwise occurrence-disjoint collision pairs.  Sum this bound over target
fibres and use Lemma 1.1. \(\square\)

## 2. Exact conversion from pair mass to balanced overload

At depth \(q\), write

\[
 N_q=\binom n{m-q},\qquad
 W=c_qN_q+\rho_q,\qquad0\le\rho_q<N_q.
\tag{2.1}
\]

### Lemma 2.1 -- pair-functional overload inequality

If \(c_q=1\), then every exact factor satisfies

\[
 \boxed{O_q(F)\ge P_q(F)-\rho_q.}
\tag{2.2}
\]

#### Proof

Let \(b_q\) be a balanced quota attaining \(O_q(F)\).  It has \(\rho_q\)
entries equal to two and all other entries equal to one, so

\[
 \sum_S\left\lfloor\frac{b_q(S)}2\right\rfloor=\rho_q.
\tag{2.3}
\]

For nonnegative integers \(x,y\),

\[
 \left\lfloor\frac x2\right\rfloor
 \le
 \left\lfloor\frac y2\right\rfloor+(x-y)_+.
\tag{2.4}
\]

Apply (2.4) with \(x=\ell_q(S)\), \(y=b_q(S)\), sum in \(S\), and use
the definition of the optimized balanced overload.  Equations
(2.3)--(2.4) give (2.2). \(\square\)

For the canonical factor, (1.5) and (2.2) give the exact finite estimate

\[
 \boxed{O_q(F_m^{\rm MSW})\ge K_m-\rho_q
 \qquad(c_q=1).}
\tag{2.5}
\]

Now

\[
 \frac{K_m}{W}
 =\frac{m(m+1)}{4(2m-1)(2m+1)}
 =\frac1{16}+o(1).
\tag{2.6}
\]

Uniformly for \(q=O(\sqrt m)\),

\[
 \lambda_q:=\frac W{N_q}
 =\exp\left(\frac{q(q+1)}m+O(m^{-1/2})\right).
\tag{2.7}
\]

If \(q\le a\sqrt m\) and
\(a<\sqrt{\log(16/15)}<\sqrt{\log2}\), then \(c_q=1\) and

\[
 \frac{\rho_q}{W}=1-\frac1{\lambda_q}
 \le1-e^{-a^2}+o(1).
\tag{2.8}
\]

Substitution of (2.6)--(2.8) into (2.5) proves

\[
 O_q(F_m^{\rm MSW})
 \ge\bigl(e^{-a^2}-15/16-o(1)\bigr)W.
\tag{2.9}
\]

For fixed \(A>0\), choose once and for all

\[
 0<a<\min\{A,\sqrt{\log(16/15)}\}.
\]

There are \((a/A+o(1))H\) depths in (2.9), proving
\(\sum_{q\le H}O_q=\Omega_A(HW)\).

## 3. Positive-density row stability

Let \(F'\) be an exact factor at row distance

\[
 b=|F'\triangle F_m^{\rm MSW}|/2
\tag{3.1}
\]

from the canonical factor, with every shared row carrying its inherited
canonical orientation.  The marked-gap audit proves that one canonical
row participates in at most \(m-1\) certificates.  Removing \(b\) rows
therefore leaves at least

\[
 K_m-(m-1)b
\tag{3.2}
\]

certificate pairs whose two rows still belong to \(F'\).  By Lemma 1.1,
the same retained pairs persist at every depth.  Hence

\[
 P_q(F')\ge K_m-(m-1)b.
\tag{3.3}
\]

Combining (2.2), (2.7), and (3.3), and writing \(b=\beta_m B\), yields

\[
 \boxed{
 \frac{O_q(F')}W
 \ge e^{-a^2}-\frac{15}{16}-\frac{\beta_m}2-o(1)
 \qquad(q\le a\sqrt m).}
\tag{3.4}
\]

Indeed,

\[
 \frac{(m-1)b}{W}=\frac{m-1}{2m+1}\,\beta_m
 =\frac{\beta_m}2+o(1).
\]

Coordinate relabelling preserves all load histograms and transports every
certificate, so (3.4) holds around every relabelled MSW factor.

## 4. Consequences for common-owner covers and monotone release

Fix one common integral balanced quota flow \(b_q\).  Every packet-feasible
monotone release profile satisfies the survival inequality, and hence

\[
 |E_q|\ge D_q^b(F)\ge O_q(F),
\tag{4.1}
\]

where \(D_q^b\) is the fixed-common-quota overload and \(O_q\) is the
independently optimized balanced overload.  Likewise its weighted
overload-fibre incidence satisfies

\[
 J_q^\uparrow(F,b;E_q)\ge D_q^b(F)\ge O_q(F).
\tag{4.2}
\]

There is a stronger exact tail-area consequence already from the first
transition.  For a factor at row distance \(b\) from MSW, (2.2)--(3.3) at
\(q=1\) give

\[
 |E_1|\ge O_1(F)
 \ge [K_m-(m-1)b-\rho_1]_+.
\tag{4.3}
\]

Since the release sets are monotone,

\[
 \boxed{
 \mathsf R_A(F,\mathbf b,\mathbf E)
 \ge [K_m-(m-1)b-\rho_1]_+
       \sum_{q=1}^H\frac1{c_q}.}
\tag{4.4}
\]

In particular, if \(b=\beta_m B\) and, for some fixed \(\eta>0\),
\(\limsup_m\beta_m\le1/8-\eta\), then, with
\(C_A=\max_{q\le H}c_q=O_A(1)\),

\[
 \mathsf R_A(F,\mathbf b,\mathbf E)
 \ge
 \left(\frac1{16}-\frac{\beta_m}2-o(1)\right)
 \frac{HW}{C_A}
 =\Omega_{A,\eta}(HW).
\tag{4.5}
\]

Thus the monotone-release obstruction holds uniformly on every closed
sub-basin \(\beta\le1/8-\eta\) of the sharp audited open MSW row basin; it
does not depend on summing the multidepth collision bound.  Equation (4.3)
uses \(c_1=1\), which holds for \(m\ge3\).

On the early subwindow of Sections 2--3, \(c_q=1\).  If the row-distance
parameters satisfy

\[
 \limsup_m\beta_m
 \le2(e^{-a^2}-15/16)-\eta
\]

for some fixed \(\eta>0\), then every such factor obeys

\[
 \sum_{q=1}^H\frac{|E_q|}{c_q}
 \ge\sum_{q\le a\sqrt m}O_q(F)
 =\Omega_{A,a,\eta}(HW),
\tag{4.6}
\]

and

\[
 \sum_{q\le a\sqrt m}J_q^\uparrow(F,b;E_q)
 =\Omega_{A,a,\eta}(HW).
\tag{4.7}
\]

Thus the exact monotone-release theorem does not rescue the canonical MSW
factor or this local basin.  In fact, for the tail-area statement alone,
the audited depth-one hole bound already forces a linear \(E_1\), which
then persists by monotonicity.  The multidepth theorem is stronger because
it also obstructs the unlabelled aggregate spill and the depth-weighted
common-owner incidence.

For the density-weighted extraction theorem, (4.2) gives the exact
necessary contribution

\[
 \sum_{a\in\mathcal A}\alpha_aJ_{\tau(a)}^\uparrow
 \ge
 \sum_{q\le a\sqrt m}
 (\alpha_{-q}+\alpha_{q+1})O_q(F)
\tag{4.8}
\]

whenever both signed slots are used.  Formula (4.8) is a lower bound, not a
claim that it exceeds the available shoulder supply for every prescribed
family: that depends on the actual densities \(\alpha_a\).

## 5. What weighted common ownership proves unconditionally

Fix one exact factor \(F\) and one load vector \(b=(b_q)_{q\le H}\)
belonging to a common integral balanced nested resolution.  Let

\[
 D_q^b(F)=\sum_S(\ell_q(S)-b_q(S))_+,
 \qquad
 \Delta_A=\max_{q,S}b_q(S)=O_A(1).
\tag{5.1}
\]

Set \(D_0^b(F)=0\) and \(J_0(F,b;E)=0\) for every owner set \(E\).  Since every balanced vector uses
\(u_q=c_q+\mathbf1_{\{\rho_q>0\}}\), the same constant is
\(\Delta_A=\max_{q\le H}u_q\).

For nonnegative depth weights \(\omega_q\), define

\[
 \jmath_\omega(F;b)
 =\min_E\sum_{q=1}^H\omega_qJ_q(F,b;E),
\tag{5.2}
\]

where the minimum is over one owner set \(E\) satisfying every survival
and directed crossing inequality through depth \(H\).  Equivalently, the
canonical paths outside \(E\) extend to one common integral resolution
with load vector \(b\).

### Theorem 5.1 -- exact weighted-cover comparison

For every such \((F,b)\) and every nonnegative \(\omega\),

\[
\boxed{
 \sum_{q=1}^H\omega_qD_q^b(F)
 \le\jmath_\omega(F;b)
 \le(\Delta_A+1)
       \sum_{q=1}^H\omega_qD_q^b(F).}
\tag{5.3}
\]

#### Proof

The lower bound is the survival inequality, summed only over overloaded
fibres:

\[
 J_q(F,b;E)
 =\sum_{\ell_q(S)>b_q(S)}a_q^E(S)
 \ge\sum_S(\ell_q(S)-b_q(S))_+
 =D_q^b(F).
\]

For the upper bound take \(E=V_0\), the set of all middle owners.  This is
feasible because the assumed common resolution with load vector \(b\) can
be used after every canonical path is released.  If
\(d_S=\ell_q(S)-b_q(S)\ge1\), then

\[
 \ell_q(S)=d_S+b_q(S)
 \le(\Delta_A+1)d_S.
\]

Consequently

\[
 J_q(F,b;V_0)
 =\sum_{\ell_q(S)>b_q(S)}\ell_q(S)
 \le(\Delta_A+1)D_q^b(F).
\]

Multiply by \(\omega_q\) and sum. \(\square\)

Thus arbitrary directed crossing packets add at most a fixed-(A)
multiplicative factor to the weighted overload-fibre incidence objective.
This is a genuine common-owner cover theorem: the same integral owner set
and the same common quota flow are used at every depth.  It deliberately
does not bound the cardinality or monotone-release tail area of that cover.

### Theorem 5.2 -- fixed-window owner-alignment fusion

Let the signed families \((\mathcal T_a)_{a\in\mathcal A}\) satisfy the
hypotheses of A's density-weighted common-owner extraction theorem, and
write

\[
 \alpha_a=\frac{|\mathcal T_a|}{N_{\tau(a)}},
 \qquad
 \omega_q=\sum_{a:\,\tau(a)=q}\alpha_a
 \quad(1\le q\le H).
\tag{5.4}
\]

For every exact factor \(F\) and every common integral balanced nested
resolution \(b\), there exist one integral owner set \(E\), the constant
monotone profile \(E_q=E\) for \(q\ge1\), one coordinate relabelling, and
one capped and parent-pruned literal occurrence graph such that its target
degree is at most \(\Delta_A\) and its edge count satisfies

\[
\boxed{
 L\ge
 W\sum_{a\in\mathcal A}\alpha_a
 -\jmath_\omega(F;b)-P_{\mathcal A}^{\#}
 \ge
 W\sum_{a\in\mathcal A}\alpha_a
 -(\Delta_A+1)\sum_{q=1}^H\omega_qD_q^b(F)
 -P_{\mathcal A}^{\#}.}
\tag{5.5}
\]

All occurrences in (5.5) are intervals in the globally relabelled rows
\(\sigma F\), with every cyclic order unchanged; the transported versions
of the same owners and the same nested quota flow certify every depth.

#### Proof

Choose an owner set attaining the finite minimum in (5.2), and put
\(E_0=\varnothing\), \(E_q=E\) for \(q\ge1\).  By the definition of the
feasible sets in (5.2), this is a packet-compatible common release
certificate.  At depth zero the exact middle ownership has no overloaded
fibre.  Therefore A's incidence form of the extraction theorem gives one
joint relabelling and pruned literal graph with

\[
 \begin{aligned}
 L
 &\ge \sum_{a\in\mathcal A}
       \alpha_a\bigl(W-J_{\tau(a)}(F,b;E)\bigr)
       -P_{\mathcal A}^{\#}\\
 &=W\sum_{a\in\mathcal A}\alpha_a
   -\jmath_\omega(F;b)-P_{\mathcal A}^{\#}.
 \end{aligned}
\]

The target-degree cap and literal parent pruning are conclusions of that
theorem.  Apply the upper bound in (5.3) for the second inequality in
(5.5). \(\square\)

Theorem 5.2 is an unconditional fixed-\(A\) alignment/cover statement, not
an assertion that its displayed lower bound has a positive fixed margin.
Indeed A's direct deficit form gives the sharper estimate

\[
 L\ge W\sum_a\alpha_a-\sum_{q=1}^H\omega_qD_q^b(F)
       -P_{\mathcal A}^{\#}.
\tag{5.6}
\]

Thus inserting the common-owner cover does not improve the numerical
factor-selection inequality; its gain is the explicit simultaneous
integral owner certificate.

### Theorem 5.3 -- pointed extraction cannot bootstrap the cover objective

The operations in the audited pointed-extraction theorem do not change
\(D_q^b(F)\), \(\jmath_\omega(F;b)\), any fixed feasible incidence
\(J_q(F,b;E)\), or the monotone-release tail area.

#### Proof

A coordinate relabelling \(\sigma\) transports

\[
 \ell_q^{\sigma F}(\sigma S)=\ell_q^F(S),
 \quad b_q^\sigma(\sigma S)=b_q(S),
 \quad a_q^{\sigma E}(\sigma S)=a_q^E(S).
\]

It bijects every survival packet, every directed crossing packet, and every
feasible common owner set.  Hence all four scalar quantities are invariant.
The subsequent cap, parent pruning, and cloned Hall matching only designate
or select existing literal occurrences; they alter none of \(F,b,E\) or
their canonical flags.  They therefore alter none of the four quantities.
\(\square\)

The density-weighted extraction theorem may consume the certificate in
Theorems 5.1--5.2, but it cannot create a better factor, common quota flow, or
cover.  Therefore factor selection cannot be deduced merely by applying
the extraction operations to an arbitrary input factor.  This is not a
failure theorem for extraction: its positive shoulder term can still
dominate the invariant cover cost for a particular factor.

## 6. Exact orbit-convexification obstruction

Assume that \(m\) is sufficiently large that \(H\le m-1\), and let
\(\mathscr O_m\) be the coordinate-relabelling orbit of the canonical MSW
exact factor.  Every member of \(\mathscr O_m\) has the same load
histograms, so Section 2 gives

\[
 \sum_{q\le H}O_q(F)=\Omega_A(HW)
 \qquad(F\in\mathscr O_m).
\tag{6.1}
\]

For a fractional factor point \(x\in\operatorname{conv}(\mathscr O_m)\),
let \(\ell_q^x\) be its linear depth-\(q\) load vector, and define

\[
 \Phi_A(x)=
 \min_{\substack{c_q\le z_q(S)\le c_q+1\\
                  \sum_Sz_q(S)=W\ (1\le q\le H)}}
 \sum_{q=1}^H\sum_S(\ell_q^x(S)-z_q(S))_+.
\tag{6.2}
\]

At an integral orbit vertex \(F\), the relaxation in (6.2) has an integral
optimum.  Indeed, write \(z_q(S)=c_q+x_S\).  Because
\(\ell_q^F(S)\) is integral, a unit of \(x_S\) has unit benefit precisely
when \(\ell_q^F(S)\ge c_q+1\), and zero benefit otherwise.  Since the
available budget \(\rho_q=W-c_qN_q\) is integral, assigning it greedily
has a \(0/1\) optimum.  Hence

\[
 \Phi_A(F)=\sum_{q=1}^H O_q(F)=\Omega_A(HW)
 \qquad(F\in\mathscr O_m).
\tag{6.3}
\]

On the other hand, the uniform orbit average \(\bar x\) has
\(\ell_q^{\bar x}=\lambda_q\mathbf1\).  Taking
\(z_q=\lambda_q\mathbf1\) in (6.2) gives

\[
 \Phi_A(\bar x)=0.
\tag{6.4}
\]

There are no additional \(0/1\) points in
\(\operatorname{conv}(\mathscr O_m)\).  Indeed, if a coordinate of a
convex combination of \(0/1\) orbit vectors equals zero or one, every
positive-weight constituent has that same coordinate.  Hence a fully
\(0/1\) convex combination equals one of its constituents.  Equations
(6.3)--(6.4) therefore give an \(\Omega_A(HW)\) gap for the explicitly
defined balanced-overload relaxation between the orbit barycentre and
every integral point of the orbit polytope.

This rules out using coordinate averaging inside the MSW orbit to obtain
\(o(W)\) monotone-release or \(O_A(W)\) aggregate spill.  It does not rule
out arbitrary LP/minimax methods, and it does not decide A's
density-weighted extraction inequality without comparing its actual
shoulder coefficient against the weighted incidence cost.

## 7. Adversarial audit and exact boundary

1. The multidepth extension uses the **ordered** common block (1.3), not
   merely equality of its underlying depth-one set.  Multiplication by two
   preserves the outside parity order, so the same-start prefixes are
   literal cyclic intervals.
2. Certificate distinctness is occurrence-level, not target-level.  This
   is exactly what is needed for the bound by
   \(\sum_S\lfloor\ell_q(S)/2\rfloor\).
3. The overload conversion is restricted to the unit-floor subwindow.
   Here \(c_1=1\) for \(m\ge3\); no false pair-baseline formula is used
   after \(c_q\ge2\).
4. A removed row can destroy at most \(m-1\) original marked-gap
   certificates, and every shared row retains its canonical orientation.
   New rows are not credited with any collision, so (3.3) is a safe
   one-sided bound.
5. The orbit barycentre is fractional.  No integral factor is inferred by
   Jensen's inequality.
6. The theorem rules out the canonical orbit and a positive-density basin.
   Here “rules out” means only for the \(o(W)\) monotone-release and
   \(O_A(W)\) spill routes.  It does not compare the incidence constant
   with A's shoulder-supply constant, does not lower-bound the global
   minimum over all exact factors, and therefore does not disprove
   density-weighted extraction, \(\mathrm{MR}_A\), fixed-window overload,
   or the constant-one conjecture.
7. The upper bound in Theorem 5.1 uses the all-owner cover.  It is a bound
   for weighted overload incidence, not for owner cardinality or release
   tail area; those latter quantities are linear for this cover.

The remaining positive problem is exact: either prove that A's weighted
shoulder supply dominates the invariant common-owner incidence for some
factor (possibly even an MSW-orbit factor), or construct a factor with a
smaller incidence profile.  The crossing-cover theorem and coordinate
averaging alone do not perform either comparison or selection.
