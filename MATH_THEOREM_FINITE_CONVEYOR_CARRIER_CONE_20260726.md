# Finite-order conveyors against the eight Catalan endpoint classes

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

At a fatal child scale put

\[
 r=s-1,\qquad
 \theta={\operatorname {Cat}_{s-1}\over p},\qquad
                         4\le\theta<16.
\tag{0.1}
\]

The canonical \(D_s\) parent has boundary loads

\[
 w_j=\operatorname {Cat}_{j-1}\operatorname {Cat}_{s-j},
 \qquad
 {w_j\over p}={\theta\over\Theta_j(s)},\qquad
 \Theta_j(s)={\operatorname {Cat}_{s-1}\over w_j}.
\tag{0.2}
\]

Only four classes at either end can exceed \(p\) somewhere in (0.1).  Thus
the risk set is finite:

\[
 \mathcal E=\{L_1,L_2,L_3,L_4,R_1,R_2,R_3,R_4\}.
\tag{0.3}
\]

For every certified conveyor type \(a\), its authoritative signed carrier
column is

\[
 \boxed{
 c_a=Q_a\sum_{t=0}^{d_a-1}\Phi_{a,t}\tau_a^t\delta_a.}
\tag{0.4}
\]

Here \(\tau_a\) is its endpoint twist, \(d_a\) its order,
\(\delta_a\) one stage's row-resolved carrier, \(\Phi_{a,t}\) the literal
stage chart, and \(Q_a\) the quotient performing every physical carrier
identification.  For a clean covariant conveyor,

\[
                         c_a=\Phi_aN_{\tau_a}\delta_a,
 \qquad N_\tau=1+\tau+\cdots+\tau^{d-1}.
\tag{0.5}
\]

If \(x_ap\) conveyors of type \(a\) are used, with
\(0\le x_a\le\rho_a\), their normalized aggregate is

\[
                         d(x)=\sum_ax_ac_a.
\tag{0.6}
\]

Let \(b_\xi(\theta)\) be the normalized old load at physical carrier
\(\xi\).  The exact new-minus-old cap derivative is

\[
 \mathscr H_\theta(d)=
 \sum_\xi\left[(b_\xi(\theta)+d_\xi-1)_+
                    -(b_\xi(\theta)-1)_+\right].
\tag{0.7}
\]

Hence a fixed density assignment lowers every cap tail uniformly if and
only if

\[
 \boxed{\mathscr H_\theta(d(x))<0
                   \quad(4\le\theta<16).}
\tag{0.8}
\]

For PCap itself, if

\[
 Z_\theta={K_p(\mu^F)-(W-N_q)\over p},
\]

the exact condition is

\[
 \boxed{
 (Z_\theta+\mathscr H_\theta(d(x)))_+<(Z_\theta)_+.}
\tag{0.9}
\]

For the raw cap tail the test is finite: it is enough to check \(4,16\), the Catalan
thresholds \(\Theta_j(s)\) in the interval, and the finitely many new
hinge crossings

\[
 \theta=\Theta_j(s)(1-d_{L_j}),\qquad
 \theta=\Theta_j(s)(1-d_{R_j})
\tag{0.10}
\]

which lie in \([4,16]\).  Between these values the hinge is affine.

The literally minimal infinitesimal carrier condition is

\[
 \boxed{
 \operatorname {cone}\{c_a:\rho_a>0\}\cap\mathcal P_s
                         \ne\varnothing,}
\tag{0.11}
\]

where \(\mathcal P_s\) is the finite descent cone defined in Section 3.
A robust sufficient version requires a positive combination which is
nonpositive on all eight risk cells and deposits all positive mass into
universal slack carriers.

Clean and folded routers contribute as follows.

* Clean \(C_6\): \(d_a=3\), and only the invariant part of
  \(\delta_a\) survives \(1+\tau+\tau^2\).
* Clean \(C_8\): \(d_a=4\), and only the invariant part survives the
  four-term norm.  Odd endpoint parity does not imply useful carrier sign.
* Folded \(C_6\): a transposition router has \(d_a=2\), so only the
  pair-symmetric part survives \(1+\tau\), after which \(Q_a\) may still
  identify source and destination.
* The known two-strand octahedral \(C_8\) is endpoint-inert.  Its column
  is \(Q_a\delta_a\); it can be useful without repetition, but a symmetric
  fold can make that column zero.

Thus the new cycle framework succeeds only if its actual post-fold
orbit-norm columns positively span a descent direction.  Group generation
alone is irrelevant to (0.11).

## 1. The eight-source Catalan skeleton

Put

\[
 \alpha_j(s)={w_j\over\operatorname {Cat}_{s-1}}
             ={1\over\Theta_j(s)}.
\tag{1.1}
\]

Then

\[
 b_{L_j}(\theta)=b_{R_j}(\theta)=\theta\alpha_j(s).
\tag{1.2}
\]

For fixed \(j\),

\[
 \alpha_j(s)\longrightarrow
 \operatorname {Cat}_{j-1}4^{-(j-1)}.
\tag{1.3}
\]

The limiting coefficients are

\[
                         1,\quad{1\over4},\quad{1\over8},
                         \quad{5\over64},\quad{14\over256},\ldots.
\tag{1.4}
\]

Here \(L_j\) means distance \(j\) from the left end, while \(R_j\) means
the symmetric class with actual index \(s+1-j\).  The fifth class from
either end has worst limiting load \(16(14/256)=7/8<1\).  Consequently
classes whose distance from both ends is at least five are universal
reservoirs for all large \(s\), as are fresh carrier labels with baseline
zero.

The exact normalized overload of one endpoint class is

\[
 e_j(\theta)=\left({\theta\over\Theta_j(s)}-1\right)_+.
\tag{1.5}
\]

Its supremal demand as \(\theta\uparrow16\) is

\[
 e_j^{\max}(s)=\left({16\over\Theta_j(s)}-1\right)_+.
\tag{1.6}
\]

For \(j=1,2,3,4\), this tends to

\[
                         \left(15,3,1,{1\over4}\right).
\tag{1.7}
\]

Thus clearing both ends uniformly can require as much as

\[
                         2\left(15+3+1+{1\over4}\right)p
                         ={77\over2}p
\tag{1.8}
\]

units of transport.  This is a density requirement, not an asymptotic
impossibility: \(\operatorname {Cat}_s<64p\) and the reservoir palette
grows with \(s\).

## 2. Exact finite signed-assignment theorem

Let \(\mathcal C=\mathcal E\sqcup\mathcal U\) contain every physical
carrier used by the proposed atlas.  No collar coordinate may be omitted
unless its coefficient is literally zero.  Let \(c_a\in\mathbb Z^\mathcal
C\) be the complete column (0.4), and suppose \(\rho_ap\) disjoint
conveyors of that type are available.

### Theorem 2.1 (finite carrier assignment)

For fixed \(s\), the following are equivalent.

1. Some densities \(0\le x_a\le\rho_a\) give cap-tail descent for every
   \(\theta\in[4,16)\).
2. The aggregate \(d(x)\) satisfies (0.8).
3. It satisfies (0.8) at the finite breakpoint set consisting of
   \(4,16\), the old thresholds in the interval, and all new crossings
   (0.10) in the interval.

With active PCap floors, replace (0.8) by (0.9).  The same finite
breakpoint conclusion holds when the normalized old floor slack
\(Z_\theta\) is itself given piecewise affinely.  Without such a
description, (0.9) remains the exact test but must be checked with the
actual depthwise floor values.

#### Proof

Every Catalan carrier load is affine in \(\theta\), and every fresh
carrier load is constant.  On an interval containing no old or new hinge
crossing, every term in (0.7) is affine.  Its maximum occurs at an
endpoint.  This proves the equivalence.  The outer positive part in
(0.9) adds only its own finite set of zero crossings. \(\square\)

This is the exact finite-dimensional theorem.  Once a hinge cell is fixed,
its constraints are linear in the densities \(x_a\).

## 3. Minimal and robust positive cones

Away from a threshold, the one-sided derivative at the canonical state is

\[
 L_\theta(d)=
 \sum_{e\in\mathcal E:\ b_e(\theta)>1}d_e.
\tag{3.1}
\]

At an exact threshold,

\[
 L_\theta(d)=
 \sum_{b_e(\theta)>1}d_e+
 \sum_{b_e(\theta)=1}(d_e)_+.
\tag{3.2}
\]

Define the exact infinitesimal descent cone

\[
 \boxed{
 \mathcal P_s=\{d:L_\theta(d)<0
   \text{ for every critical }\theta\in[4,16]\}.}
\tag{3.3}
\]

Write \(D_j=d_{L_j}+d_{R_j}\).  Away from exact threshold faces, the
essential cumulative inequalities are

\[
 \boxed{
 D_1+D_2<0,\qquad
 D_1+D_2+D_3<0,\qquad
 D_1+D_2+D_3+D_4<0.}
\tag{3.4}
\]

For finite \(s\), use the classes already active at \(\theta=4\) in the
first sum and apply the positive-part correction (3.2) at an exact
threshold.  Equation (0.11) is therefore a finite cone-intersection test.

For a sign-safe finite-density direction, choose a reservoir family
\(\mathcal U\) satisfying

\[
 \sigma_u:=1-\sup_{4\le\theta<16}b_u(\theta)>0.
\tag{3.5}
\]

Define

\[
\begin{aligned}
 \mathcal D_s=\{d:\;&\sum_\xi d_\xi=0,\quad
 d_e\le0\ (e\in\mathcal E),\\
 &d_\xi>0\Longrightarrow\xi\in\mathcal U,\quad
 d_{L_1}+d_{R_1}<0\}.
\end{aligned}
\tag{3.6}
\]

If \(d\in\mathcal D_s\) and

\[
                         d_u\le\sigma_u\qquad(u\in\mathcal U),
\tag{3.7}
\]

then no destination reaches cap, no risk class gains load, and the two
always-overloaded endpoint classes give strict uniform descent.
Consequently

\[
 \operatorname {cone}\{c_a:\rho_a>0\}\cap\mathcal D_s\ne\varnothing
\tag{3.8}
\]

is a robust sufficient cone condition.

## 4. Densities for complete uniform clearance

Assume the available columns are sign-safe:

\[
 c_{a,e}\le0\quad(e\in\mathcal E),\qquad
 c_{a,\xi}>0\Longrightarrow\xi\in\mathcal U.
\tag{4.1}
\]

The worst-case finite transportation inequalities are

\[
 \boxed{
 -\sum_ax_ac_{a,L_j}\ge e_j^{\max}(s),\qquad
 -\sum_ax_ac_{a,R_j}\ge e_j^{\max}(s)
                         \quad(1\le j\le4),}
\tag{4.2}
\]

\[
 \boxed{
 \sum_ax_a(c_{a,u})_+\le\sigma_u
                         \quad(u\in\mathcal U),\qquad
 0\le x_a\le\rho_a.}
\tag{4.3}
\]

They are sufficient uniformly over \([4,16)\), and necessary for full
clearance within a sign-safe atlas using exactly these reservoirs.

For a Catalan reservoir at distance \(j\ge5\) from its nearer end,

\[
 \sigma_{L_j}=\sigma_{R_j}
                         =1-{16\over\Theta_j(s)}.
\tag{4.4}
\]

Fresh cells have \(\sigma=1\).  At \(j=5\), (4.4) tends to \(1/8\).

If \(S_ap\) synchronized alternating-cycle stages of type \(a\) are
available, finite-order closure consumes \(d_a\) stages per conveyor, so

\[
                         \rho_a\le {S_a\over d_ap}.
\tag{4.5}
\]

The stage costs are \(3\) for clean \(C_6\), \(4\) for clean \(C_8\),
\(2\) for a folded-\(C_6\) transposition conveyor, and \(1\) for an
endpoint-inert folded \(C_8\).

## 5. Clean cycle possibilities

### 5.1 Clean \(C_6\)

A clean coherent \(C_6\) acts on three distinct strands by a \(3\)-cycle.
Three switch-stable serial stages restore endpoint labels.  Under
covariant charts,

\[
 c_6=(1+\tau+\tau^2)\delta=3\Pi_{\rm inv}\delta.
\tag{5.1}
\]

Therefore \(c_6\ne0\) exactly when \(\delta\) has nonzero
\(\tau\)-invariant projection.  In particular,

\[
                         \delta=e_{\tau x}-e_x
 \quad\Longrightarrow\quad c_6=0.
\tag{5.2}
\]

A clean \(C_6\) which only cycles a carrier token among its three strands
is cap-inert after closure.  It must instead drain an invariant source
class into a separately transported invariant reservoir class.

### 5.2 Clean \(C_8\)

A clean coherent \(C_8\) acts by a \(4\)-cycle and needs four serial
stages.  Its covariant column is

\[
 c_8=(1+\tau+\tau^2+\tau^3)\delta=4\Pi_{\rm inv}\delta.
\tag{5.3}
\]

Again every nontrivial Fourier mode cancels.  The odd permutation is
useful for monodromy correction but says nothing about carrier sign.
Distinct strands prevent a folding collision before the norm; outer
carrier maps can still collide and belong in (0.4).

## 6. Folded cycle possibilities

### 6.1 Folded \(C_6\)

A legal folded \(C_6\) can induce a transposition.  Two coherent stages
give

\[
 c_{6,\rm fold}=Q(1+\tau)\delta=2Q\Pi_{\rm inv}\delta.
\tag{6.1}
\]

The antisymmetric part cancels.  A nonzero symmetric part can still be
killed when \(Q\) identifies its negative source with its positive
destination.  Thus transposition power does not imply a useful carrier
column.

### 6.2 Folded \(C_8\)

The known two-strand octahedral \(C_8\) is endpoint-inert, so it has no
serial monodromy cost.  Its column is

\[
                         c_{8,\rm oct}=Q\delta.
\tag{6.2}
\]

It can lie in the descent cone directly, but the geometry supplies no
sign.  If opposite arms or the two old strands share a carrier, \(Q\)
may cancel the useful direction.  Other folded \(C_8\)'s must be treated
using their actual strand permutation and the general formula (0.4);
cycle length alone determines neither order nor carrier sign.

## 7. Separation form of the minimal condition

Let \(\mathscr C_{6,8}\) be the actual columns of the growing clean/folded
atlas after serial closure, carrier transport, and folding.  The minimal
small-density gate is

\[
 \boxed{
                         \operatorname {cone}(\mathscr C_{6,8})
                         \cap\mathcal P_s\ne\varnothing.}
\tag{7.1}
\]

If it fails, finite-dimensional cone separation supplies a functional
\(\lambda\) with

\[
 \lambda(c)\ge0\quad(c\in\mathscr C_{6,8}),\qquad
 \lambda(d)<0\quad(d\in\mathcal P_s).
\tag{7.2}
\]

No number of additional copies of the same router types can then produce
uniform first-order descent.  A new physical carrier column outside the
separated cone is required.

For full clearance one needs the stronger density system
(4.2)--(4.3).  For PCap rather than raw cap-tail descent, the active-floor
condition (0.9) is additionally necessary.

## 8. Exact scope

The Catalan part is now finite: eight risk classes, finitely many
thresholds, and a finite carrier LP.  The remaining unproved assertion is
geometric—a positive-density, switch-stable \(C_6/C_8\) atlas whose
post-fold orbit-norm columns satisfy (7.1), preferably (3.8) and the
transportation inequalities (4.2)--(4.3).

Group generation is insufficient.  Clean \(C_6\)'s may generate an
alternating group, a clean \(C_8\) may break parity, and folded
\(C_6\)'s may generate transpositions while every carrier norm remains
zero or lies outside the descent cone.  Constant one requires monodromy
closure and a positive carrier cone in the same physical atlas.
