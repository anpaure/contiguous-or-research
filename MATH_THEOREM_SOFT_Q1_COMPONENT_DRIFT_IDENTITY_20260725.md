# Exact soft depth-one drift on ownership-component switches

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

After the augmented-orbit stalling audit, lower traces should be a soft
objective rather than hard vertices of one giant matching edge.  This
note gives the exact one-step laws for that surviving model.

Let \(F,G\) be exact middle wreath factors and let \({\cal K}\) be the
connected components of their middle-ownership overlay.  For a
rank-\((m-1)\) target \(R\), write

\[
 a_K(R)=\hbox{load from the \(F\)-side of component \(K\)},
 \qquad
 b_K(R)=\hbox{load from the \(G\)-side}.
 \tag{0.1}
\]

Switching one component \(K\) changes the hole count by exactly

\[
 \boxed{
 H_1(F_K)-H_1(F)=D_K-R_K,}
 \tag{0.2}
\]

where

\[
 R_K=\#\{R:\mu_F(R)=0,\ b_K(R)>0\}
 \tag{0.3}
\]

is its repair count, and

\[
 D_K=\#\{R:\mu_F(R)=a_K(R)>0,\ b_K(R)=0\}
 \tag{0.4}
\]

is its damage count.  Thus a deterministic improving move exists if
the total repair incidence over a component menu exceeds the total
single-component-fragility incidence.

For independent fair choices of all component sides, a target which is
positive on both sides of one component is always safe.  Every other
target with positive support on \(d\) one-sided components is missing
with probability exactly \(2^{-d}\).

When \(G=\tau F\) for a coordinate transposition \(\tau\), the expected
hole drift has the exact orbit decomposition

\[
 \boxed{
 \mathbb EH_1(F_\varepsilon)-H_1(F)
 =-\sum_{\text{exclusive \(\tau\)-pairs }P}
       (1-2^{1-s_P})
 +\sum_{R\in{\cal C}}2^{-d_R}.}
 \tag{0.5}
\]

Here \(s_P\) is the number of one-sided components supporting either
member of an exclusive hole/covered target pair, and \({\cal C}\) is
the family of targets covered by both endpoint factors but not safe in
any one component.  Thus:

* exclusive load split among at least two components gives genuine
  negative drift;
* covered-on-both-sides but component-separated load gives the exact
  leakage;
* all \(\tau\)-fixed covered depth-one targets are automatically safe.

Equation (0.5) is the sharp soft-hole substitute for quadratic heat.
It can improve holes even when floor-collision energy increases, but it
also exposes the missing theorem: a fresh overlay must supply
macroscopic multi-component repair while keeping nonrobust leakage
smaller.

The contextual size-two atlas inside the canonical MSW construction has
only \(O(\operatorname{Cat}_m)=o(W)\) total first-shadow action, and the
proved \(3/8\)-mass suffix tail of the fixed \((2\ 3)\)-component cube has
rankwise diameter \(O(W/\sqrt m)=o(W)\).  These facts rule out the most
direct private/local repair and that large tail separately.  They do **not**
bound the action of the complete fixed \((2\ 3)\) hierarchy: the remaining
large-atom head has only an \(O(W)\) triangle bound at present.  Thus both a
productive cut in the complete canonical cube and a genuinely fresh
nonlocal overlay remain live possibilities for partial descent.  A separate
fixed-target localization now proves that every corner of the complete
fixed cube retains \((1/32-o(1))W\) holes, so this one fibre cannot by itself
reach the \(o(W)\) first-shadow target; see
`MATH_THEOREM_MSW_23_FIXED_HOLE_FLOOR_20260725.md`.

## 1. One complete component

Let

\[
 \mu_F(R)=\sum_{K\in{\cal K}}a_K(R).
 \tag{1.1}
\]

After switching component \(K\),

\[
 \mu_{F_K}(R)=\mu_F(R)-a_K(R)+b_K(R).
 \tag{1.2}
\]

### Theorem 1.1 (single-component hole gradient)

Equations (0.2)--(0.4) hold.

#### Proof

An old hole has \(\mu_F(R)=0\), and hence \(a_K(R)=0\) for every
component.  It is repaired by switching \(K\) exactly when
\(b_K(R)>0\).  This gives (0.3).

A previously covered target becomes a hole exactly when the right side
of (1.2) is zero.  All three terms are nonnegative except the displayed
subtraction, so this happens exactly when

\[
 \mu_F(R)=a_K(R)>0,\qquad b_K(R)=0.
 \tag{1.3}
\]

This gives (0.4), and no other target changes hole status. \(\square\)

Summing (0.2) over components yields

\[
 \sum_K\bigl(H_1(F_K)-H_1(F)\bigr)=D_*-R_*,
 \tag{1.4}
\]

where

\[
 R_*=\sum_{R:\mu_F(R)=0}
      \#\{K:b_K(R)>0\},
 \tag{1.5}
\]

and

\[
 D_*=\#\left\{
 R:\begin{array}{l}
 \mu_F(R)>0,\text{ all its \(F\)-occurrences lie in one component }K,\\
 \text{and }b_K(R)=0
 \end{array}\right\}.
 \tag{1.6}
\]

Therefore

\[
 \boxed{R_*>D_*\quad\Longrightarrow\quad
 \text{some single legal component switch decreases }H_1.}
 \tag{1.7}
\]

This is an exact local-search criterion.  It has no quadratic baseline
or integrality error.

For a transposition overlay it simplifies further.  Retain the
exclusive moved pairs \(P\) and their component-support sizes \(s_P\)
from Section 4.  Define

\[
 D_{\rm common}
 =\#\left\{
 R:\begin{array}{l}
 R\text{ is covered by both }F\text{ and }\tau F,\\
 \text{all \(F\)-occurrences of }R\text{ lie in one component }K,\\
 b_K(R)=0
 \end{array}\right\}.
 \tag{1.8}
\]

### Theorem 1.2 (exact transposition aggregate gradient)

\[
 \boxed{
 R_*-D_*
 =\sum_{P:\,s_P\ge2}s_P-D_{\rm common}.}
 \tag{1.9}
\]

Consequently

\[
 \boxed{
 \sum_{P:\,s_P\ge2}s_P>D_{\rm common}
 \quad\Longrightarrow\quad
 \text{some single component switch decreases }H_1.}
 \tag{1.10}
\]

#### Proof

Every \(F\)-hole which is also a \(\tau F\)-hole contributes zero to
\(R_*\).  For an exclusive pair, let \(R\) be its member which is a hole
of \(F\).  Its \(\tau F\)-support occupies \(s_P\) components, so it
contributes \(s_P\) to \(R_*\).  Hence

\[
 R_*=\sum_Ps_P.
 \tag{1.11}
\]

The other member \(\tau R\) is covered by \(F\) and absent from
\(\tau F\).  By involutive symmetry its \(F\)-support also occupies
\(s_P\) components.  It contributes to \(D_*\) exactly when
\(s_P=1\).  The remaining contributions to \(D_*\) are precisely the
covered-on-both targets in (1.8).  Therefore

\[
 D_*=\#\{P:s_P=1\}+D_{\rm common}.
 \tag{1.12}
\]

Subtract (1.12) from (1.11); the \(s_P=1\) terms cancel, proving
(1.9).  Equation (1.10) follows from (1.7). \(\square\)

This local criterion is different from fair-cube drift.  A split pair
with \(s_P\) components contributes \(s_P\) units to the aggregate
single-move repair surplus, whereas its fair-cube gain is only
\(1-2^{1-s_P}\).  Conversely, \(D_{\rm common}\) charges a target by one
even when its fair-cube leakage \(2^{-d_R}\) is tiny.  Neither criterion
uniformly dominates the other.

The collision ledger gives the useful lower bound

\[
 \boxed{
 R_*-D_*
 \ge2(A_\tau^{(2)}-\Xi_\tau)-D_{\rm common}.}
 \tag{1.13}
\]

Indeed at most \(\Xi_\tau\) productive load-at-least-two exclusive
targets can have \(s_P=1\), and every remaining one has \(s_P\ge2\).
Thus the verifiable sufficient condition

\[
 \boxed{
 D_{\rm common}<2(A_\tau^{(2)}-\Xi_\tau)}
 \tag{1.14}
\]

forces a deterministic improving component.

If the surplus in (1.9) is \(G>0\) and the overlay has \(k\) components,
then some component satisfies

\[
 \boxed{H_1(F_K)-H_1(F)\le-{G\over k}\le-{G\over B},
 \qquad B=W/n.}
 \tag{1.15}
\]

The first inequality is averaging; the second uses \(k\le B\), since
every component contains at least one wreath row on each side.  Thus a
surplus \(G=\gamma W/m\) guarantees a component with constant-order
improvement at least \(\gamma n/m=(2+o(1))\gamma\).  A full fair-cube
choice can realize \(\Theta(W/m)\) improvement at once under Theorem
6A.1; the local greedy version distributes the same aggregate gradient
over its components.

## 2. Exact floor-energy gradient

The same switch has a closed quadratic formula at every depth.  Let

\[
 \phi_c(t)=(t-c)(t-c-1),
 \qquad
 Q_q(F)=\sum_R\phi_{c_q}(\mu_F(R)).
 \tag{2.1}
\]

Put

\[
 \delta_K(R)=b_K(R)-a_K(R).
 \tag{2.2}
\]

Then

\[
 \boxed{
 Q_q(F_K)-Q_q(F)
 =\sum_R\left[
   (2\mu_F(R)-2c_q-1)\delta_K(R)+\delta_K(R)^2
 \right].}
 \tag{2.3}
\]

Indeed, this is the identity

\[
 \phi_c(t+d)-\phi_c(t)=(2t-2c-1)d+d^2.
 \tag{2.4}
\]

At depth one, \(c_1=1\) and

\[
 Q_1(F)
 =2H_1(F)+\sum_{\mu_F(R)\ge3}
   (\mu_F(R)-1)(\mu_F(R)-2).
 \tag{2.5}
\]

Thus decreasing holes and decreasing floor energy are different
objectives.  A switch may repair holes while concentrating the displaced
mass at load three.  Since the literal soft-trace transfer only needs
few holes, (0.2) is the more direct first-shadow drift.

## 3. A fair full component cube

Choose the \(F\)- or \(G\)-side of every component independently with
probability \(1/2\), producing the exact factor \(F_\varepsilon\).

Call target \(R\) **two-sided safe** if some component \(K\) has

\[
 a_K(R)>0\quad\hbox{and}\quad b_K(R)>0.
 \tag{3.1}
\]

If it is not safe, define

\[
 I_R=\{K:a_K(R)+b_K(R)>0\},\qquad d_R=|I_R|.
 \tag{3.2}
\]

### Theorem 3.1 (one-child hole probability)

For every target \(R\),

\[
 \boxed{
 \Pr(R\text{ is a hole of }F_\varepsilon)=
 \begin{cases}
 0,&R\text{ is two-sided safe},\\
 2^{-d_R},&R\text{ is not safe}.
 \end{cases}}
 \tag{3.3}
\]

The convention \(2^0=1\) covers a target absent from both endpoint
factors.

#### Proof

If (3.1) holds, either side of that component supplies \(R\).  Otherwise
each active component has exactly one owning side.  The child misses
\(R\) precisely when it chooses the nonowning side in every one of the
\(d_R\) active components, an event of probability \(2^{-d_R}\).
\(\square\)

Consequently

\[
 \boxed{
 \mathbb EH_1(F_\varepsilon)
 =\sum_{R\text{ not safe}}2^{-d_R}.}
 \tag{3.4}
\]

This is the exact soft-hole heat identity.  Unlike the quadratic heat
identity, it ignores multiplicity within one component and records only
support across component sides.

## 4. Involutive relabeling

Assume now \(G=\tau F\), where \(\tau\) is a coordinate transposition.
The target set splits into \(\tau\)-fixed targets and moved pairs.
Moreover

\[
 H_1(G)=H_1(F).
 \tag{4.1}
\]

Partition the targets into:

* \({\cal I}\): holes in both \(F\) and \(G\);
* exclusive moved pairs \(P=\{R,\tau R\}\), one member a hole of \(F\)
  and the other a hole of \(G\);
* \({\cal C}\): individual targets covered by both \(F\) and \(G\),
  but not two-sided safe;
* safe targets.

For an exclusive pair, let \(s_P\) be the number of active one-sided
components of either member.  The involution maps the two support
systems bijectively, so the two numbers agree.

### Theorem 4.1 (exact transposition hole drift)

Equation (0.5) holds.

#### Proof

A target in \({\cal I}\) has \(d_R=0\) and contributes one both to
\(H_1(F)\) and to the expectation.  An exclusive pair contributes one
hole to \(F\), whereas Theorem 3.1 gives expected contribution

\[
 2\cdot2^{-s_P}=2^{1-s_P}.
 \tag{4.2}
\]

A target in \({\cal C}\) contributes zero to \(H_1(F)\) and
\(2^{-d_R}\) to the expectation.  Safe targets contribute zero to
both.  Summing proves (0.5). \(\square\)

Thus a sufficient one-step escape condition is

\[
 \boxed{
 \sum_P(1-2^{1-s_P})
 >\sum_{R\in{\cal C}}2^{-d_R}.}
 \tag{4.3}
\]

If the difference in (4.3) is at least \(\gamma W\), some integral
corner of the component cube has at least \(\gamma W\) fewer holes than
\(F\).

The negative term has a useful collision lower bound.  Let

\[
 A_\tau^{(2)}
 =\#\{R:\mu_F(R)=0,\ \mu_F(\tau R)\ge2\},
 \tag{4.4}
\]

and define the component coalescence energy on the covered sides of
these exclusive pairs by

\[
 \Xi_\tau
 =\sum_{R:\mu_F(R)=0}
   \sum_K\binom{b_K(R)}2.
 \tag{4.5}
\]

Also put

\[
 \Lambda_\tau=\sum_{R\in\mathcal C}2^{-d_R}.
 \tag{4.6}
\]

### Corollary 4.2 (duplicate splitting versus leakage)

\[
 \boxed{
 \mathbb EH_1(F_\varepsilon)-H_1(F)
 \le-{1\over2}(A_\tau^{(2)}-\Xi_\tau)+\Lambda_\tau.}
 \tag{4.7}
\]

Hence

\[
 \boxed{
 A_\tau^{(2)}>\Xi_\tau+2\Lambda_\tau
 \quad\Longrightarrow\quad
 \text{some integral child has fewer holes}.}
 \tag{4.8}
\]

#### Proof

An exclusive pair whose covered member has load at least two has
\(s_P\ge2\), and hence gain

\[
 1-2^{1-s_P}\ge1/2,
 \tag{4.9}
\]

unless all its covered occurrences coalesce in one component.  Every
such coalesced failure contributes at least one to
\(\sum_K\binom{b_K(R)}2\).  Therefore at least
\(A_\tau^{(2)}-\Xi_\tau\) exclusive pairs contribute at least one half
to the negative term of (0.5).  The positive term is exactly
\(\Lambda_\tau\).  This proves (4.7)--(4.8). \(\square\)

The quantity \(\Xi_\tau\) is the precise soft-target component
pair-square.  Bounding it asks whether two occurrences of one lower
target are forced into the same ownership component.  The
neighborhood/three-link and affine label-dispersal estimates are
relevant here without making the lower target a hard resource.

## 4B. Exact biased component heat

Choose the \(G=\tau F\) side of every component independently with a
common probability \(p\in[0,1]\).  For a target which is not two-sided
safe, put

\[
 \ell_R=\#\{K:a_K(R)>0\},\qquad
 r_R=\#\{K:b_K(R)>0\}.
 \tag{4B.1}
\]

It is a hole exactly when all \(\ell_R\) left-owning components choose
right and all \(r_R\) right-owning components choose left.  Therefore

\[
 \boxed{\Pr_p(R\text{ is a hole})=p^{\ell_R}(1-p)^{r_R}.}
 \tag{4B.2}
\]

Under the transposition involution, exclusive targets occur in pairs
with profiles \((0,s_P)\) and \((s_P,0)\).  Nonfixed common unsafe
targets occur in pairs with profiles \((\ell,r)\) and \((r,\ell)\).
Fixed covered targets are safe by Corollary 5.2.  Hence the complete
biased objective is

\[
 \boxed{
 H_1(p)=|{\cal I}|
 +\sum_{P\text{ exclusive}}
   \bigl[p^{s_P}+(1-p)^{s_P}\bigr]
 +\sum_{U\text{ common unsafe}}
   \bigl[p^{\ell_U}(1-p)^{r_U}
        +p^{r_U}(1-p)^{\ell_U}\bigr],}
 \tag{4B.3}
\]

where one representative is taken from every transposition orbit in
the final sum.  This is exact for every \(p\), and every outcome is an
integral exact factor.

There is a convenient one-variable form.  Put

\[
 x=p(1-p)\in[0,1/4]
 \tag{4B.4}
\]

and define

\[
 E_0(x)=2,\qquad E_1(x)=1,\qquad
 E_s(x)=E_{s-1}(x)-xE_{s-2}(x).
 \tag{4B.5}
\]

Then

\[
 E_s(x)=p^s+(1-p)^s.
 \tag{4B.6}
\]

Choosing \(\ell_U\le r_U\), equation (4B.3) becomes

\[
 \boxed{
 H_1(p)-H_1(0)
 =\sum_P(E_{s_P}(x)-1)
 +\sum_Ux^{\ell_U}E_{r_U-\ell_U}(x).}
 \tag{4B.7}
\]

Thus a biased improving child exists if and only if the polynomial on
the right of (4B.7) is negative at some \(x\in(0,1/4]\).  This is an
exact finite criterion, not a moment bound.

Differentiating at \(p=0\) gives

\[
 \boxed{
 H_1'(0)
 =-\sum_{P:s_P\ge2}s_P+D_{\rm common}.}
 \tag{4B.8}
\]

This recovers Theorem 1.2: negative derivative is exactly positive
aggregate single-component repair surplus.

Endpoint symmetry alone does not force a useful \(p\).  One exclusive
pair with \(s=2\) and one common unsafe orbit with
\((\ell,r)=(1,1)\) has

\[
 H_1(p)-|{\cal I}|
 =[p^2+(1-p)^2]+2p(1-p)=1
 \tag{4B.9}
\]

for every \(p\).  Adding another \((1,1)\) common orbit makes every
interior \(p\) strictly worse.  These are exact support profiles (not
claimed here to arise from cyclic wreaths), and they refute a generic
convexity/endpoint-averaging theorem.

Conversely, the full polynomial is strictly stronger than its
derivative.  Since

\[
 E_5(x)=1-5x+5x^2,
 \tag{4B.10}
\]

one exclusive pair with \(s=5\), together with five common unsafe
orbits of profile \((1,3)\), has zero derivative at the endpoint but

\[
 H_1(p)-H_1(0)
 =(E_5(x)-1)+5xE_2(x)=-5x^2<0
 \tag{4B.11}
\]

for every interior \(p\).  There are also profiles with positive
endpoint derivative but improvement near \(p=1/2\): one \(s=2\)
exclusive pair and three \((1,10)\) common orbits have

\[
 H_1'(0)=1>0,
 \qquad
 H_1(1/2)-H_1(0)
 =-{1\over2}+{3\over1024}<0.
 \tag{4B.12}
\]

Therefore the best biased theorem is genuinely the polynomial
criterion (4B.7).  The local gradient and the fair point \(p=1/2\) are
two different sufficient tests; neither subsumes the other in abstract
support data.

There is nevertheless an exact averaging criterion which uses the
whole interval of biases.

### Theorem 4B.2 (uniform-bias beta criterion)

If

\[
 \boxed{
 \sum_{P\text{ exclusive}}
   \left(1-{2\over s_P+1}\right)
 >
 \sum_{U\text{ common unsafe}}
   {2\ell_U!r_U!\over(\ell_U+r_U+1)!},}
 \tag{4B.13}
\]

then there is a bias \(p\in(0,1)\) for which
\(H_1(p)<H_1(0)\), and consequently some integral component-cube child
has fewer holes than \(F\).

More quantitatively, the difference between the two sides of (4B.13)
is a lower bound on the improvement for some \(p\) in expectation.

#### Proof

Integrating (4B.3) over \(p\in[0,1]\) gives

\[
 \int_0^1[p^s+(1-p)^s],dp={2\over s+1},
 \tag{4B.14}
\]

and the beta integral gives

\[
\begin{aligned}
 &\int_0^1
 [p^\ell(1-p)^r+p^r(1-p)^\ell],dp\\
 &\hspace{30mm}
 =2B(\ell+1,r+1)
 ={2\ell!r!\over(\ell+r+1)!}.
\end{aligned}
 \tag{4B.15}
\]

Targets in \(\mathcal I\) contribute one both to the endpoint and to
the integral.  Thus (4B.13) says exactly that

\[
 \int_0^1H_1(p)\,dp<H_1(0).
 \tag{4B.16}
\]

Some \(p\) has \(H_1(p)<H_1(0)\), and some integral child is no worse
than its expectation. \(\square\)

The constants are sharp for the simplest counterprofile.  One
exclusive \(s=2\) pair has averaged gain \(1-2/3=1/3\), while one
common \((1,1)\) orbit has averaged leakage
\(2/(3!)=1/3\); equation (4B.9) is indeed constant for every bias.

If a common unsafe orbit has total support
\(d=\ell+r\), then

\[
 {2\ell!r!\over(d+1)!}
 ={2\over(d+1)\binom d\ell}
 \le {2\over d(d+1)},
 \tag{4B.16a}
\]

with equality at \(\ell=1\) or \(r=1\).  Consequently, if at most
\(\varepsilon T\) of \(T\) productive load-at-least-two exclusive
pairs have \(s=1\), every common unsafe orbit has support at least
\(d_0\), and there are \(C\) such orbits, the uniform-bias criterion is
implied by

\[
 \boxed{
 {1-\varepsilon\over3}T
 >{2C\over d_0(d_0+1)}.}
 \tag{4B.16b}
\]

The beta criterion can be substantially weaker than the derivative
test when common damage has large support: a \((1,r)\) orbit costs only

\[
 {2\over(r+1)(r+2)}
 \tag{4B.17}
\]

under uniform bias, rather than one unit in \(D_{\rm common}\).  It is
different from the fair test, which gives exponentially smaller leakage
for very large \(r\).  Taking the best of (4B.7), (4B.8), the fair point,
and (4B.13) is therefore genuinely useful.

All formulas sum across depths with one common bias.  In particular,
for weights \(w_q\ge0\), if

\[
 \boxed{
 \sum_qw_q\sum_{P\in{\cal P}_q}
   \left(1-{2\over s_{P,q}+1}\right)
 >
 \sum_qw_q\sum_{U\in{\cal U}_q}
   {2\ell_{U,q}!r_{U,q}!\over
    (\ell_{U,q}+r_{U,q}+1)!},}
 \tag{4B.18}
\]

then some single \(p\) and some integral child decrease the weighted
multidepth hole potential \(\sum_qw_qH_q\).  This follows by integrating
the weighted sum of (4B.3); no separate sign choice is made at different
depths.

## 5. Fixed targets are automatically safe at depth one

For a depth-one target \(R\), define its endpoint set

\[
 E_F(R)=\{x\notin R:
 R\cup\{x\}\text{ has }R\text{ as an endpoint facet in its owning
 wreath of }F\}.
 \tag{5.1}
\]

Each cyclic occurrence of \(R\) has two distinct middle extensions, and
each middle set has a unique owning wreath.  Therefore

\[
 \boxed{|E_F(R)|=2\mu_F(R).}
 \tag{5.2}
\]

### Lemma 5.1 (endpoint-overlap safety)

If

\[
 E_F(R)\cap E_G(R)\ne\varnothing,
 \tag{5.3}
\]

then \(R\) is two-sided safe in the \(F/G\) overlay.

#### Proof

For \(x\) in the intersection, the unique left and right wreaths
displaying \(R\) both own the middle set \(R\cup\{x\}\).  Hence those
two wreaths are joined by an overlay edge and lie in the same component.
Both sides of that component contain \(R\). \(\square\)

### Corollary 5.2 (transposition-fixed targets are safe)

If \(\tau R=R\) and \(\mu_F(R)>0\), then \(R\) is two-sided safe in the
\(F/(\tau F)\) overlay.

#### Proof

Equation (5.1) gives

\[
 E_{\tau F}(R)=\tau E_F(R).
 \tag{5.4}
\]

The set \(E_F(R)\) has size at least two by (5.2).  Every subset of size
at least two intersects its image under a transposition: a transposition
moves only its two exchanged points, and every other point is fixed.
Thus (5.3) holds. \(\square\)

It follows that the leakage family \({\cal C}\) in (0.5) contains only
targets moved by \(\tau\).  The exact fixed-target fraction at rank
\(r=m-1\) is

\[
 {\binom{n-2}{r-2}+\binom{n-2}{r}\over\binom nr}
 ={r(r-1)+(n-r)(n-r-1)\over n(n-1)}
 ={2m^2+4\over(2m+1)(2m)}
 ={1\over2}+O(1/m).
 \tag{5.5}
\]

Thus endpoint-overlap safety removes asymptotically half the ambient
rank-\((m-1)\) targets from the leakage problem, exactly and without a
moment estimate.

There is also an unconditional supply of exclusive hole/covered pairs
for at least one transposition.

### Proposition 5.3 (Johnson boundary supplies a productive transposition)

Let \({\cal Z}\subseteq\binom{[n]}r\) be the hole family of an exact
factor at any rank, put \(h=|{\cal Z}|\) and
\(N=\binom nr\), and define

\[
 A_\tau=|{\cal Z}\setminus\tau{\cal Z}|.
 \tag{5.6}
\]

Then

\[
 \boxed{
 \sum_{\tau\text{ transposition}}A_\tau
 =|\partial_{J(n,r)}{\cal Z}|
 \ge n h(1-h/N).}
 \tag{5.7}
\]

Consequently some transposition satisfies

\[
 \boxed{
 A_\tau\ge {2h(1-h/N)\over n-1}.}
 \tag{5.8}
\]

#### Proof

Every Johnson edge \(\{R,R-x+y\}\) is generated by the unique
coordinate transposition \((x\ y)\).  It crosses the cut
\((\mathcal Z,\mathcal Z^c)\) exactly when its endpoint in
\(\mathcal Z\) is counted by \(A_{(x\ y)}\).  This proves the equality
in (5.7).

The unnormalized Laplacian spectral gap of \(J(n,r)\) is \(n\).
Applying its Poincare inequality to the indicator of \(\mathcal Z\)
gives

\[
 |\partial_J\mathcal Z|
 \ge n\sum_R
  (\mathbf1_{\mathcal Z}(R)-h/N)^2
 =nh(1-h/N).
 \tag{5.9}
\]

Divide by \(\binom n2\) to obtain (5.8). \(\square\)

At depth one with \(h=\Theta(W)\), (5.8) is
\(\Theta(W/m)\).  Thus \(\Theta(n)\) adaptively recomputed
transposition rounds have the correct aggregate opportunity scale for
positive-density escape.  What remains is to convert these exclusive
pairs into the negative term of (0.5): their covered loads must occupy
at least two components often enough, and the leakage term must be
smaller.

For \(G=\tau F\), \(A_\tau\) is exactly the number of exclusive moved
pairs in Theorem 4.1: if \(R\in\mathcal Z\) but
\(\tau R\notin\mathcal Z\), then \(R\) is a hole only on the \(F\)-side
and \(\tau R\) is the paired hole only on the \(G\)-side.

The same averaging chooses one transposition simultaneously for every
controlled depth.

### Theorem 5.4 (weighted multidepth opportunity)

For depths \(q\in Q\), let

\[
 {\cal Z}_q\subseteq\binom{[n]}{r_q},\qquad
 h_q=|{\cal Z}_q|,\qquad N_q=\binom n{r_q},
 \tag{5.10}
\]

and put

\[
 A_{\tau,q}=|{\cal Z}_q\setminus\tau{\cal Z}_q|.
 \tag{5.11}
\]

For arbitrary weights \(w_q\ge0\), some coordinate transposition
\(\tau\) satisfies

\[
 \boxed{
 \sum_{q\in Q}w_qA_{\tau,q}
 \ge {2\over n-1}
      \sum_{q\in Q}w_qh_q(1-h_q/N_q).}
 \tag{5.12}
\]

#### Proof

Apply (5.7) at each rank, multiply by \(w_q\), and sum:

\[
 \sum_\tau\sum_qw_qA_{\tau,q}
 \ge n\sum_qw_qh_q(1-h_q/N_q).
 \tag{5.13}
\]

Divide by \(\binom n2\).  At least one summand on the left is at least
the average, proving (5.12). \(\square\)

For the balanced-overload weighting, one may take \(w_q=1/c_q\); for
literal separate hole repair, take \(w_q=1\).  Theorem 5.4 is therefore
the exact simultaneous opportunity theorem needed by either ledger.

To state its conversion gate, define at every depth the exclusive-pair
component support \(s_{P,q}\), and let \(D_{{\rm common},q}\) be the
analogue of (1.8).  For the weighted hole potential

\[
 {\cal H}_w(F)=\sum_{q\in Q}w_qH_q(F),
 \tag{5.14}
\]

Theorem 1.2 summed over depths gives the exact identity

\[
 \boxed{
 \sum_K\bigl({\cal H}_w(F_K)-{\cal H}_w(F)\bigr)
 =-\sum_qw_q\left[
   \sum_{P:s_{P,q}\ge2}s_{P,q}-D_{{\rm common},q}
 \right].}
 \tag{5.15}
\]

Hence one deterministic component improves the common multidepth
potential whenever

\[
 \boxed{
 \sum_qw_q\sum_{P:s_{P,q}\ge2}s_{P,q}
 >\sum_qw_qD_{{\rm common},q}.}
 \tag{5.16}
\]

The fair-cube analogue is

\[
 \boxed{
 \sum_qw_q\sum_P(1-2^{1-s_{P,q}})
 >\sum_qw_q\Lambda_{\tau,q}.}
 \tag{5.17}
\]

Theorem 5.4 supplies the weighted number of exclusive pairs, but not
(5.16) or (5.17): singleton support cancels, while common-target leakage
must be controlled.  The exact remaining **multidepth conversion
theorem** is to find, for the productive transposition in (5.12), enough
component splitting of the exclusive mass and sufficiently little
weighted common damage to make one of (5.16)--(5.17) hold with a fixed
fraction of the right side of (5.12).

At depth one, a general relabeling supplies the stronger
hole-to-duplicate count at the desired \(W/m\) scale.

### Proposition 5.5 (general-permutation duplicate opportunity)

Let \({\cal Z}=\{R:\mu_F(R)=0\}\), \(h=|\mathcal Z|\), and

\[
 {\cal D}_2=\{R:\mu_F(R)\ge2\},\qquad d_2=|\mathcal D_2|.
 \tag{5.18}
\]

Then

\[
 \boxed{d_2\ge {2(h+W-N_1)\over m}.}
 \tag{5.19}
\]

Consequently some coordinate permutation \(\sigma\in S_n\) satisfies

\[
 \boxed{
 T_\sigma
 :=|\{R\in\mathcal Z:\sigma^{-1}R\in\mathcal D_2\}|
 \ge {2h(h+W-N_1)\over mN_1}.}
 \tag{5.20}
\]

In particular, if \(h\ge\delta W\), then

\[
 \boxed{T_\sigma\ge {2\delta^2W\over m}.}
 \tag{5.21}
\]

#### Proof

The exact total duplicate excess is

\[
 \sum_R(\mu_F(R)-1)_+
 =W-(N_1-h)=h+W-N_1.
 \tag{5.22}
\]

By the endpoint identity (5.2),

\[
 \mu_F(R)\le{m+2\over2},
 \tag{5.23}
\]

and hence every member of \(\mathcal D_2\) contributes at most \(m/2\)
to (5.22).  This proves (5.19).

For a uniform coordinate permutation \(\sigma\), the image of every
fixed rank-\((m-1)\) target is uniform on that rank.  Therefore

\[
 \mathbb E_\sigma T_\sigma={hd_2\over N_1}.
 \tag{5.24}
\]

Use (5.19) and choose a permutation attaining at least the average.
If \(h\ge\delta W\), then \(h+W-N_1\ge\delta W\) and
\(N_1\le W\), giving (5.21). \(\square\)

This proves the \(\Theta(W/m)\) **opportunity** used in Section 6A.
It does not prove that the \(F/(\sigma F)\) overlay has enough
components.  A general permutation overlay may be connected, in which
case all duplicate occurrences coalesce and no partial switch exists.

There is nevertheless an exact conditional conversion.  Let
\(\Xi_{\rm rep}\) be the internal collision energy restricted to the
\(T_\sigma\) repaired-hole targets, and let \(D_*\) be (1.6) for the
general \(F/(\sigma F)\) overlay.  Then

\[
 \boxed{
 R_*-D_*
 \ge2(T_\sigma-\Xi_{\rm rep})-D_*.}
 \tag{5.25}
\]

Thus \(\Xi_{\rm rep}\le\varepsilon T_\sigma\) and
\(D_*\le\delta T_\sigma\), with
\(2(1-\varepsilon) >\delta\), force a deterministic improving
component.  The missing general-permutation theorem is precisely this
fragmentation-versus-damage estimate.

## 6. Relation to the neighborhood/three-link method

The Bonferroni neighborhood theorem controls how often a soft-target
action profile can be highly atypical when legal moves are sampled from
a diffuse catalogue.  In the present notation it can be used to bound

* the distribution of \(R_K\), the old-hole repair support of a move;
* the distribution of \(D_K\), its single-component-fragility damage;
* intersections among the target supports of different proposed moves.

Its raw diagonal pair-square term controls repeated target action, and
its remaining weighted triple kernel is the first obstruction to
showing \(R_*>D_*\) for a move catalogue.

The coalescence term in Corollary 4.2 has an exact row-overlap form.
Let \({\cal I}_1(P)\) be the set of depth-one intervals displayed by a
wreath row \(P\), and let \({\cal R}_K\) be the rows on the covered side
of component \(K\).  Since a cyclic row displays a given target at most
once,

\[
 \boxed{
 \sum_R\binom{b_K(R)}2
 =\sum_{\{P,Q\}\subseteq{\cal R}_K}
   |{\cal I}_1(P)\cap{\cal I}_1(Q)|.}
 \tag{6.1}
\]

Define the full internal overlap energy

\[
 \widehat\Xi_\tau
 =\sum_K\sum_{\{P,Q\}\subseteq{\cal R}_K}
   |{\cal I}_1(P)\cap{\cal I}_1(Q)|.
 \tag{6.2}
\]

Hence

\[
 \boxed{
 \Xi_\tau\le\widehat\Xi_\tau.}
 \tag{6.2a}
\]

The leakage term has a complementary cross-component overlap bound.  Put

\[
 \Omega_\tau
 =\sum_{K\ne L}
   \sum_{P\in{\cal L}_K,\ Q\in{\cal R}_L}
   |{\cal I}_1(P)\cap{\cal I}_1(Q)|,
 \tag{6.3}
\]

where \({\cal L}_K\) and \({\cal R}_K\) are the two row sides of
component \(K\).  A target in \({\cal C}\) has at least one left and one
right occurrence, and all such occurrences lie in different components.
Therefore it contributes at least one to \(\Omega_\tau\).  Since
\(d_R\ge2\),

\[
 \boxed{\Lambda_\tau\le{1\over4}|{\cal C}|
                    \le{1\over4}\Omega_\tau.}
 \tag{6.4}
\]

In load-vector notation these two overlap energies are

\[
 \boxed{
 \widehat\Xi_\tau
 ={1\over2}\sum_K
   \bigl(\|b_K\|_2^2-\|b_K\|_1\bigr),}
 \tag{6.4a}
\]

and

\[
 \boxed{
 \Omega_\tau
 =\langle\mu_F,\mu_{\tau F}\rangle
  -\sum_K\langle a_K,b_K\rangle.}
 \tag{6.4b}
\]

Indeed, (6.4a) is
\(\binom t2=(t^2-t)/2\) summed over target loads in a component.
For (6.4b), expand the global cross inner product as
\(\sum_{K,L}\langle a_K,b_L\rangle\) and remove its diagonal
\(K=L\).  Thus the leakage is precisely global first-shadow
correlation not coalesced inside ownership components.

Combining (4.7), (6.2a), and (6.4), a sufficient purely row-overlap
condition for a fair improving child is

\[
 \boxed{A_\tau^{(2)}>\widehat\Xi_\tau+{1\over2}\Omega_\tau.}
 \tag{6.5}
\]

This convenient sufficient condition must not be mistaken for a new
way around the quadratic heat gap.  There is an exact identity showing
that the crude majorants collapse back to that gap.

Let

\[
 P_F=\sum_R\binom{\mu_F(R)}2,\qquad
 P_G=\sum_R\binom{\mu_G(R)}2,
 \tag{6.6}
\]

let \(\widehat\Xi_F,\widehat\Xi_G\) be the two internal component
collision energies, and put

\[
 A=\|\mu_F-\mu_G\|_2^2,\qquad
 V=\sum_K\|a_K-b_K\|_2^2.
 \tag{6.7}
\]

### Proposition 6.1 (overlap--heat identity)

\[
 \boxed{
 \Omega
 =(P_F-\widehat\Xi_F)+(P_G-\widehat\Xi_G)
 +{V-A\over2}.}
 \tag{6.8}
\]

#### Proof

Since every endpoint factor has total depth-one mass \(W\),

\[
 \|\mu_F\|_2^2=W+2P_F,\qquad
 \|\mu_G\|_2^2=W+2P_G.
 \tag{6.9}
\]

Therefore

\[
 \langle\mu_F,\mu_G\rangle
 =W+P_F+P_G-A/2.
 \tag{6.10}
\]

On the other hand,

\[
 V=2W+2\widehat\Xi_F+2\widehat\Xi_G
   -2\sum_K\langle a_K,b_K\rangle,
 \tag{6.11}
\]

so

\[
 \sum_K\langle a_K,b_K\rangle
 =W+\widehat\Xi_F+\widehat\Xi_G-V/2.
 \tag{6.12}
\]

Subtract (6.12) from (6.10) and use (6.4b). \(\square\)

For \(G=\tau F\), symmetry gives

\[
 P_F=P_G=P,\qquad
 \widehat\Xi_F=\widehat\Xi_G=\widehat\Xi,
 \tag{6.13}
\]

and hence (6.5) becomes

\[
 \boxed{A_\tau^{(2)}>P+{V-A\over4}.}
 \tag{6.14}
\]

Since \(A_\tau^{(2)}\le H_1(F)\) and
\(P\ge W-N_1+H_1(F)\), (6.14) requires a compensating positive
quadratic heat gap \(A-V\).  Thus the crude overlap bounds do not evade
the known first-shadow heat obstruction.

The real advantage of the hole identity is more delicate: retain the
exact restricted coalescence \(\Xi_\tau\) and the exact exponentially
weighted leakage \(\Lambda_\tau=\sum2^{-d_R}\).  Replacing them by
\(\widehat\Xi\) and \(\Omega/4\) throws away precisely the nonlinear
support information which distinguishes holes from collision energy.

## 6A. A sharp quantitative \(W/m\) descent bridge

The following gives exact constants for converting a supplied family of
productive hole-to-duplicate pairs into a genuine improving factor.

### Theorem 6A.1 (productive splitting with controlled leakage)

Let \(T=A_\tau^{(2)}\), and assume

\[
 \Xi_\tau\le\varepsilon T,
 \qquad
 \Lambda_\tau\le\lambda T
 \tag{6A.1}
\]

for some \(0\le\varepsilon\le1\) and \(\lambda\ge0\).  Then some
integral component-cube child satisfies

\[
 \boxed{
 H_1(F_\varepsilon)
 \le H_1(F)-\left({1-\varepsilon\over2}-\lambda\right)T.}
 \tag{6A.2}
\]

In particular, a strict improvement is forced whenever

\[
 \boxed{\lambda<{1-\varepsilon\over2}.}
 \tag{6A.3}
\]

#### Proof

Corollary 4.2 gives

\[
 \mathbb EH_1(F_\varepsilon)-H_1(F)
 \le-{1\over2}(T-\Xi_\tau)+\Lambda_\tau.
 \tag{6A.4}
\]

Insert (6A.1).  Some integral child is no worse than the expectation,
which proves (6A.2)--(6A.3). \(\square\)

The factor \(1/2\) is sharp from support data alone: a productive load
two split over exactly two components has expected gain exactly one
half.  The leakage coefficient is also exact because
\(\Lambda_\tau\) is the literal expected number of new holes.

There is a verifiable row-overlap version.  For a leakage target \(R\),
let

\[
 \ell_R=\#\{K:a_K(R)>0\},\qquad
 r_R=\#\{K:b_K(R)>0\}.
 \tag{6A.5}
\]

Then \(d_R=\ell_R+r_R\), and its contribution to
\(\Omega_\tau\) is at least \(\ell_Rr_R\).  If every leakage target
satisfies \(d_R\ge d_0\ge2\), then

\[
 {2^{-d_R}\over\ell_Rr_R}
 \le {2^{-d_0}\over d_0-1}.
 \tag{6A.6}
\]

Indeed, for fixed \(d_R\), the product \(\ell_Rr_R\) is minimized at
\((1,d_R-1)\), and \(2^{-d}/(d-1)\) decreases in \(d\).  Summing gives

\[
 \boxed{
 \Lambda_\tau
 \le\gamma_{d_0}\Omega_\tau,
 \qquad
 \gamma_{d_0}={2^{-d_0}\over d_0-1}.}
 \tag{6A.7}
\]

### Corollary 6A.2 (component-support/row-overlap criterion)

If

\[
 T\ge {\alpha W\over m},\qquad
 \Xi_\tau\le\varepsilon T,
 \qquad d_R\ge d_0\ (R\in\mathcal C),
 \qquad\Omega_\tau\le\beta T,
 \tag{6A.8}
\]

then some integral child has

\[
 \boxed{
 H_1(F_\varepsilon)
 \le H_1(F)-\left[
 {1-\varepsilon\over2}
 -{2^{-d_0}\over d_0-1}\beta
 \right]{\alpha W\over m}.}
 \tag{6A.9}
\]

Thus a strict \(\Theta(W/m)\) improvement follows under the sharp
numerical condition

\[
 \boxed{
 \beta<2^{d_0-1}(d_0-1)(1-\varepsilon).}
 \tag{6A.10}
\]

For the weakest support information \(d_0=2\), this reads

\[
 \Omega_\tau<2(1-\varepsilon)T.
 \tag{6A.11}
\]

Here is a literal component-size specialization.  Let
\(B=W/n\) be the number of wreath rows in one factor.  Suppose every
covered-side component has at most \(s_{\max}\) rows and every two
distinct rows in one such component satisfy

\[
 |{\cal I}_1(P)\cap{\cal I}_1(Q)|\le\lambda_{\rm int}.
 \tag{6A.12}
\]

Then (6.2) gives

\[
\begin{aligned}
 \Xi_\tau
 &\le\widehat\Xi_\tau
 \le\lambda_{\rm int}\sum_K\binom{|{\cal R}_K|}2\\
 &\le {\lambda_{\rm int}(s_{\max}-1)B\over2}.
\end{aligned}
 \tag{6A.13}
\]

If \(T\ge\alpha W/m\), define

\[
 \varepsilon_0
 ={\lambda_{\rm int}(s_{\max}-1)m\over2\alpha n}.
 \tag{6A.14}
\]

### Corollary 6A.3 (bounded components with trace overlap)

Under (6A.12), if every leakage target spans at least \(d_0\)
components and \(\Omega_\tau\le\beta T\), then some child improves by
at least

\[
 \boxed{
 \left[{1-\varepsilon_0\over2}
 -{2^{-d_0}\over d_0-1}\beta\right]T,}
 \tag{6A.15}
\]

provided the bracket is positive.

The constants show why component size alone is insufficient.  If
\(\lambda_{\rm int}=\Theta(n)\), as for some locally swapped cyclic
orders, then \(\varepsilon_0\) is macroscopic or larger even for
bounded \(s_{\max}\).  A useful theorem needs both bounded component
size and \(O(1)\)-scale (or suitably averaged) internal trace overlap.

If instead every leakage target spans \(d_0\asymp\log_2m\) components,
then \(\gamma_{d_0}=O(1/(m\log m))\), so even
\(\Omega_\tau=O(W)\) costs only \(O(W/(m\log m))\), smaller than the
forced \(T=\Theta(W/m)\) scale.

Finally, suppose the hypotheses persist adaptively with

\[
 T\ge{\alpha H_1(F)\over m}
 \tag{6A.16}
\]

and with a fixed positive bracket \(\gamma\) in (6A.9).  Repeatedly
choosing the guaranteed integral child gives

\[
 H_1(F_s)
 \le H_1(F_0)\left(1-{\alpha\gamma\over m}\right)^s.
 \tag{6A.17}
\]

Hence \(O(m)\) recomputed rounds reduce a positive-density MSW defect by
a fixed factor, and \(O(m\log m)\) rounds reduce it to \(o(W)\).  This is
a statement about mathematical reconfiguration steps, not final word
length; every intermediate state is one exact factor.

The remaining theorem is now quantitative and local to the soft model:
prove (6A.8), or the sharper exact conditions (6A.1), for a productive
transposition supplied by the Johnson boundary.

This is precisely an internal weighted overlap energy of ownership
components.  A component-size bound by itself does not make (6.2)
small: two cyclic orders related by a local adjacent swap can share
\(\Theta(n)\) length-\((m-1)\) intervals.  One additionally needs a
high-overlap quarantine or the weighted three-link/affine-dispersal
bound to show that such row pairs carry only \(o(W)\) total component
mass.

But neighborhood regularity alone cannot prove (4.3).  That inequality
is a signed component-containment statement: it asks for duplicate
covered mass to split across components while common covered mass is
coalesced inside components.  The exact soft stochastic gate is now

\[
 \boxed{
 \text{construct a fresh overlay with }
 \sum_P(1-2^{1-s_P})-\sum_{R\in{\cal C}}2^{-d_R}=\Omega(W),}
 \tag{6.15}
\]

or, for adaptive single-component descent, prove \(R_*>D_*\).

The first expression is global fair-cube drift; the second is local
greedy drift.  Both are literal statements about integral exact factors.

## 7. Consequence for the MSW starting factor

The canonical MSW factor has

\[
 H_1(F_m^{\rm MSW})\ge(1/16-o(1))W.
 \tag{7.1}
\]

For its canonical fixed transposition, two proper submenus are proved
shallow-inert:

\[
 \text{contextual size-two atlas action}
 =O(\operatorname{Cat}_m)=o(W),
 \tag{7.2}
\]

and the \(3/8\)-mass suffix tail has depth-one diameter

\[
 O(W/\sqrt m)=o(W).
 \tag{7.3}
\]

Neither statement applies to the complete component menu.  The available
all-component estimate

\[
 \|\Delta_{j,R}^{(1)}\|_1
 \le(4j+10)(\operatorname{Cat}_j+\operatorname{Cat}_{j+1})
 \tag{7.4}
\]

sums only to a coefficient-scale upper bound because of the large-atom
endpoint.  Consequently it is **not proved** that the negative term in
(0.5) is \(o(W)\) for the full canonical cube.  Its exact sign remains the
support-profile problem in (4.3), or equivalently the local criterion
\(R_*>D_*\).

Independently of this unknown sign, the marked-gap fixed-target theorem
gives the complete-cube floor

\[
 \boxed{
 H_1(F_I)\ge
 (m-3)\operatorname{Cat}_{m-2}-{2W\over m+2}
 =\left({1\over32}-o(1)\right)W}
 \tag{7.5}
\]

for every component choice \(I\).  Therefore a productive canonical cut,
if it exists, can only be a partial preprocessing step before changing the
bridge or recomputing the ownership decomposition.

The already proved row-distance escape from the full relabelled MSW
orbit changes \(\Theta(\operatorname{Cat}_m)=o(W)\) wreath packets and
does not by itself imply depth-one hole escape.  To reduce (7.1), one
needs either

1. a productive cut in the complete canonical \((2\ 3)\)-cube;
2. \(\Theta(W)\) total productive first-shadow action accumulated over a
   sequence of recomputed overlays; or
3. one genuinely nonlocal overlay satisfying (6.15).

No such all-\(m\) construction is proved here.  The advance is the exact
soft objective and the precise repair-versus-leakage inequality which a
positive-density MSW escape must satisfy.

The full-cube scope correction is detailed in
`MATH_AUDIT_FULL_CANONICAL_23_CUBE_Q1_20260725.md`.
