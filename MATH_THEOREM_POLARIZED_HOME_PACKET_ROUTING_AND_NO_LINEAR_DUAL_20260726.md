# Polarized home-packet routing: exact capacitated system and the no-linear-dual barrier

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web
input is used.

## 0. Verdict

Let

\[
 \mathcal V
 =\mathop{\dot\bigcup}_{q\le H,\epsilon\in\{-,+\}}
       \mathcal T_q^\epsilon
\tag{0.1}
\]

be the typed all-depth target universe.  After every shared frame,
selector, and overlapping slab variable has either been frozen or placed
inside a common master choice group, let \(\mathcal G\) be an
owner-disjoint family of legal compound groups.  One option
\(\omega\in\Omega_g\) chooses the complete packet/frame/slab/compiler
state of group \(g\), simultaneously through every protected depth and
both signs.  Write

\[
                         I_{g,\omega}\subseteq\mathcal V
\tag{0.2}
\]

for its typed literal image.

For product distributions \(x_g\in\Delta(\Omega_g)\), define

\[
 p_g(v)=\sum_{\omega\in\Omega_g}
     x_{g,\omega}{\bf1}_{\{v\in I_{g,\omega}\}}.
\tag{0.3}
\]

The exact near-deterministic home functional is

\[
 \boxed{
 D_{\rm home}(x)
 =\sum_{v\in\mathcal V}
       \left(1-\max_{g\in\mathcal G}p_g(v)\right).}
\tag{0.4}
\]

### Polarized routing theorem

If

\[
                         D_{\rm home}(x)=o(W),
\tag{0.5}
\]

then one integral common all-depth legal state has

\[
                         \mathfrak H=\mathfrak X=o(W).
\tag{0.6}
\]

The rounding loses at most \(D_{\rm home}(x)\) targets and uses every
physical owner capacity once.  Thus (0.4)--(0.5) are a rigorous
capacitated version of “all but \(o(N_q)\) targets receive score
\(1-o(1)\) from one home packet/frame.”  The aggregate \(o(W)\) rate in
(0.5), rather than an unquantified depthwise \(o(N_q)\), is what the
constant-one transfer consumes.

The presently proved rank-twisted frames and cross-parent
\(Q_{R+1}\)-slabs do not construct (0.5).  They prove that home packets
can cross parent boundaries and give the exact literal derivative of one
trade, but they provide neither a positive-density compatible slab
packing nor an all-depth bundle assignment satisfying (0.4).

There is also no possible negative certificate of the requested form
using the exact linear cross-profile/configuration dual.  Under the
audited normalized-conjugacy premise, there is a legal fractional point
with total load at least one at every retained typed target.  Therefore,
for every \(y\ge0\),

\[
 \boxed{
 \sum_{v\in\mathcal V}y_v
 \le\sum_{g\in\mathcal G}\max_{\omega\in\Omega_g}
          \sum_{v\in I_{g,\omega}}y_v.}
\tag{0.7}
\]

Consequently no single nonnegative dual \(y\) can prove that every
integral routing leaves \(\Omega(W)\) holes.  If such an integral
obstruction exists, it is an integrality-gap or higher-order bundle
obstruction, invisible to the linear dual.

This distinction is real.  A tensorable two-group option system has
exact mean-one fractional coverage and satisfies (0.7) for every \(y\),
but every integral state misses one quarter of its targets.  No embedding
of that alternating minor into the full physical rank-twisted/slab atlas
is currently proved.  Hence neither a polarized physical construction nor
a physical \(\Omega(W)\) no-go follows from the audited inputs.

The exact surviving theorem is now sharply isolated: prove (0.5), or
prove a literal positive-density alternating/bundle obstruction in the
actual compound slab-option catalogue.  Common-order syndrome,
within-packet injectivity, and quadratic CPCR are not involved.

## 1. Legal compound groups and common source capacity

A choice group must contain every variable which cannot be selected
independently.  In particular:

1. overlapping slabs belong to one master group unless an
   owner-disjoint slab packing has first been fixed;
2. a rank matching or frame conjugacy shared by several packets belongs
   to their common group; and
3. one option records the same compiler label at all depths and both
   signs.

After this grouping, distinct groups have disjoint middle-owner sets.
Choosing one option in every group is therefore an exact factor of the
same retained owner set, with no duplicated source capacity.

The source-profile projection makes this explicit.  For a fixed typed
depth \(c=(q,\epsilon)\), ordered target profile \(\tau\), and middle
source profile \(\kappa\), let

\[
 n_{g,\omega}^{c}(\tau,\kappa)
\tag{1.1}
\]

be the number of \(\kappa\)-owners in group \(g\) whose option-\(\omega\)
literal target has profile \(\tau\).  Put

\[
 c_{\tau\kappa}^{c}(x)
 ={1\over|\kappa|}
   \sum_{g,\omega}x_{g,\omega}
             n_{g,\omega}^{c}(\tau,\kappa).
\tag{1.2}
\]

Every owner emits exactly one typed target at depth \(c\), so

\[
\begin{aligned}
 \sum_\tau c_{\tau\kappa}^{c}(x)
 &={1\over|\kappa|}
   \sum_{g,\omega}x_{g,\omega}
      \#\{\kappa\text{-owners in }g\}\\
 &\le1.
\end{aligned}
\tag{1.3}
\]

Thus the common source-profile constraint is automatic in the physical
grouped formulation.  Different depths reuse the same owner as different
required shadows, which is intentional; the same option \(\omega\)
couples those shadows.

If one works one level earlier with profile ratios
\(R_{\tau\kappa}\), (1.2) is precisely a physical refinement of the
coefficients \(c_{\tau\kappa}\) in the exact cross-profile dual.  Not
every abstract feasible \(c\) has such a refinement: packet supports,
compiler labels, and slab consistency are the additional constraints.

## 2. Exact polarized capacitated assignment

The maximum in (0.4) can be written as a home assignment.  Introduce

\[
 h_{v,g}\in\{0,1\},\qquad e_v\in\{0,1\},
\tag{2.1}
\]

with

\[
                         e_v+\sum_gh_{v,g}=1.
\tag{2.2}
\]

Here \(e_v=1\) quarantines \(v\), while \(h_{v,g}=1\) declares \(g\)
its home group.  The exact aggregate home defect is

\[
 D(x,h,e)
 =\sum_ve_v+sum_{v,g}h_{v,g}(1-p_g(v)).            \tag{2.3}
\]

Minimizing (2.3) over \((h,e)\) gives (0.4), because every target chooses
a group maximizing \(p_g(v)\); explicit quarantine is unnecessary unless
one wants to record exceptional targets separately.

Equivalently, for a prescribed accuracy \(\delta_m\to0\) and reserve
\(E_m=o(W)\), the strong threshold form is

\[
\begin{aligned}
 &x_{g,\omega}\ge0,qquad
   \sum_\omega x_{g,\omega}=1,\tag{2.4}\\
 &e_v+\sum_gh_{v,g}=1,qquad
   \sum_ve_v\le E_m,\tag{2.5}\\
 &p_g(v)\ge1-\delta_m
       \quad\text{whenever }h_{v,g}=1.             \tag{2.6}
\end{aligned}
\]

If

\[
                         E_m+\delta_m|\mathcal V|=o(W),
\tag{2.7}
\]

then (2.4)--(2.6) imply (0.5).  The weighted form (2.3) is sharper: it
allows target-dependent errors and requires only their sum to be
\(o(W)\).

The variables \(h\) make the feasible set nonconvex.  Dropping their
integrality and replacing (2.6) by the summed condition
\(\sum_gp_g(v)\ge1\) returns the diffuse fractional cover and loses the
home property.

## 3. Lossless all-depth rounding of a polarized point

### Theorem 3.1 (home-bundle rounding)

For every product point \(x\), there is one option
\(\omega_g^\ast\in\Omega_g\) for every group such that the resulting
integral all-depth state misses at most

\[
                         D_{\rm home}(x)
\tag{3.1}
\]

typed targets.

#### Proof

Assign every target \(v\) to a home group \(g(v)\) attaining
\(\max_gp_g(v)\), and put

\[
                         B_g=\{v:g(v)=g\}.
\tag{3.2}
\]

The bundles \(B_g\) are pairwise disjoint.  If group \(g\) samples
\(\omega\) from \(x_g\), the expected number of its assigned homes which
are absent is

\[
\begin{aligned}
 \mathbb E_{x_g}|B_g\setminus I_{g,\omega}|
 &=\sum_{v\in B_g}(1-p_g(v)).
\end{aligned}
\tag{3.3}
\]

Choose one option \(\omega_g^\ast\) whose missing count is no larger
than this expectation.  Sum (3.3) over groups.  Since the assigned
bundles are disjoint, every target present in its chosen home option is
globally covered.  The total missed count is at most

\[
 \sum_g\sum_{v\in B_g}(1-p_g(v))
 =D_{\rm home}(x).
\]

Every \(I_{g,\omega}\) is the complete typed image of one legal option,
so the same chosen option serves all depths and signs. \(\square\)

The theorem proves more than generic conditional expectation for the
product-uncovered functional: it rounds each declared home bundle
separately and charges the linear home defect.  It is valid only after
all shared variables have been grouped correctly as in Section 1.

### Corollary 3.2 (near-deterministic threshold form)

Any solution of (2.4)--(2.7) rounds to one legal state with
\(o(W)\) total missing shadows and hence \(o(W)\) repeat excess.

## 4. The exact linear dual and why it cannot obstruct polarization

For the ordinary fractional cover with reserve \(E\), separation gives

\[
 \sum_g\max_{\omega}
       \sum_{v\in I_{g,\omega}}y_v+\rho_E(y)
 \ge\sum_vy_v
 \qquad(y\ge0).
\tag{4.1}
\]

This is the packet-option refinement of the exact cross-profile dual

\[
 \sum_Ty_T
 \le\sum_\kappa\max_\tau
       \sum_{T\in\tau}y_TR_{\tau\kappa}(T).
\tag{4.2}
\]

The normalized conjugacy construction supplies distributions
\(x^{\rm orb}\) with

\[
                         \ell(v):=sum_gp_g^{\rm orb}(v)\ge1
\tag{4.3}
\]

on every retained typed target, under the audited premise.  Hence, for
every \(y\ge0\),

\[
\begin{aligned}
 \sum_vy_v
 &\le\sum_vy_v\ell(v)\\
 &=\sum_{g,\omega}x_{g,\omega}^{\rm orb}
       \sum_{v\in I_{g,\omega}}y_v\\
 &\le\sum_g\max_\omega
       \sum_{v\in I_{g,\omega}}y_v.
\end{aligned}
\tag{4.4}

This proves (0.7) with \(E=0\).

### Theorem 4.1 (no single linear dual witness)

As long as (4.3) is a convex combination of **legal common all-depth
options**, there is no nonnegative target weight \(y\) violating (4.1)
or its profile projection (4.2).  In particular, no single \(y\) from
the exact cross-profile dual can prove that every integral home routing
has \(\Omega(W)\) holes.

The theorem does not assert that an integral home routing exists.  It
asserts that any negative theorem must detect the integrality gap between
diffuse fractional cover and one-option-per-group coverage.  Such a
certificate necessarily uses option intersections, alternating minors,
or another nonlinear/higher-order invariant.

If the claimed orbit average exists only at the abstract
source-profile-ratio level and has not been refined to legal packet
options, then (4.3) is not available for (4.1).  In that case the exact
remaining task is precisely to prove or disprove this refinement; one
must not silently identify the two convex hulls.

## 5. Exact abstract integrality obstruction

The failure of a single dual witness is not merely logical.  Let the
target set be \(\{1,2,3,4\}\).  Give group \(A\) the options

\[
                         \{1,2\},\qquad\{3,4\},
\tag{5.1}
\]

and group \(B\) the options

\[
                         \{1,3\},\qquad\{2,4\}.
\tag{5.2}
\]

Choosing every option with probability \(1/2\) gives every target total
fractional load one, so (4.1) holds for every \(y\).  But every integral
row/column choice has union size three and leaves exactly one target
uncovered.  Tensoring \(n\) disjoint copies gives

\[
                         \mathfrak H={1\over4}|\mathcal V|
\tag{5.3}
\]

for every integral state while the fractional dual remains feasible.

This system is already owner-group disjoint and has injective option
images.  It can be decorated by state-independent private targets at
all other depths, so its obstruction is compatible with one common
all-depth option bit.  It is not a proved subcatalogue of the physical
diverse-order compiler.  Therefore it refutes any abstract theorem
deducing polarized routing from (4.1), but not the physical constant-one
conjecture.

In bundle language, the obstruction is failure of exchange: the
hereditary families

\[
 \mathcal F_g=\{B:B\subseteq I_{g,\omega}
                      \text{ for some }\omega\}
\tag{5.4}
\]

are unions of power sets, not matroids.  Ordinary Hall ranks become
sufficient only after a genuine matroidal/polymatroidal exchange theorem
for the compound physical option families.

## 6. What cross-parent slabs do and do not provide

One legal \(Q_{R+1}\)-slab trade replaces two old packet images by two
new ones while preserving exactly \(2^{R+1}\) owners.  At one signed
depth, with \(s=2^R\), it changes the literal image by a balanced vector
\(\Delta\) satisfying

\[
 \|\Delta\|_1\le4s,qquad
 \sum_T(\Delta(T))_+le2s.
\tag{6.1}
\]

Against a fixed background, one slab can therefore fill at most \(2s\)
holes.  Repairing a linear deficit \(D=\Theta(W)\) requires at least

\[
                         {D\over2s}=\Omega(W/2^R)
\tag{6.2}
\]

changed slabs.  Since the complete owner set contains only
\(\Theta(W/2^R)\) owner-disjoint slab units at this scale, every positive
construction must use cross-parent trades on a positive fraction of the
available owner mass.

The slab theorem proves local reachability of the two resolutions and
the exact derivative (6.1).  It does not prove:

1. a positive-density owner-disjoint packing of compatible slabs;
2. a choice of slab resolutions whose new target images form disjoint or
   near-home bundles;
3. an exchange axiom for the resulting compound bundle families; or
4. a common all-depth solution of (0.4).

Thus sparse absorption cannot solve the polarized problem.  A dense
cross-parent recoupling is necessary, but the currently proved slabs are
compatible with both a positive construction and an alternating
integrality obstruction.

## 7. The exact physical alternatives

The current inputs prove neither side of the requested physical
dichotomy.

### Positive alternative

Construct an owner-disjoint compound catalogue and distributions \(x_g\)
such that

\[
 \boxed{
 \sum_{v\in\mathcal V}
       \left(1-max_gp_g(v)\right)=o(W).}
\tag{7.1}
\]

Theorem 3.1 then gives one integral common all-depth state with the exact
constant-one L1 conclusion.

### Negative alternative

Embed, on \(\Omega(W)\) typed targets, a literal alternating minor or
another non-matroidal bundle obstruction which survives every allowed
rank-frame change and every owner-preserving compound slab trade.  This
would prove a linear integral hole lower bound.  It cannot be certified
by one nonnegative \(y\) satisfying the linear dual, because Theorem 4.1
closes that dual whenever the normalized conjugacy point refines to legal
options.

No invariant in the present slab theorem preserves the earlier
fixed-profile or frozen-parent cuts: one legal trade crosses those parent
boundaries, and a dense family of trades has exactly the scale needed to
repair a linear cut.  Conversely, reachability alone supplies no bundle
exchange theorem.

## 8. Certified boundary

Proved here:

1. the exact common-source, all-depth polarized capacitated system;
2. lossless rounding of every aggregate home point (0.5);
3. the impossibility of a single linear dual obstruction under legal
   normalized conjugacy;
4. a tensorable abstract integral obstruction invisible to every such
   dual; and
5. the positive-density slab toll required by any moving-frame repair.

Not proved:

1. (7.1) for the rank-twisted/slab compiler catalogue;
2. a literal alternating minor invariant under the full slab semigroup;
3. a physical \(\Omega(W)\) missing-shadow lower bound; or
4. coefficient one.

The near-deterministic escape has therefore been reduced to one exact
object: a common all-depth home-bundle assignment in the compound
packet-option catalogue.  It is an integral exchange problem, not a
profile-capacity, annealed-marginal, common-order, or within-packet
problem.
