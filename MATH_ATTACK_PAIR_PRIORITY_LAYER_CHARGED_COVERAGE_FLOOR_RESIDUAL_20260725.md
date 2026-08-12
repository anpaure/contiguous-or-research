# Pair-priority layers: exact charged coverage after the factorial floor

Date: 2026-07-25

Method: pure mathematics only.  No computation, search, solver, or
long-running job is used.

## 0. Outcome

Let

\[
 n=2m+1,
 \qquad W=\binom{2m+1}{m},
 \qquad T=\binom{2m+1}{m-1}=\frac{m}{m+2}W,
\]

and let \(M_0\) be the first-avoided matching associated with the ordered
disjoint pairs \(P_1,\ldots ,P_m\).  Use recursively conjugate exact local
factors

\[
 F_{j+1}=\theta_jF_j,
\]

where \(\theta_j\) exchanges \(P_j\) and \(P_{j+1}\) coordinatewise.
The simultaneous legality and additive descent theorem for either disjoint
parity layer is proved in
`MATH_ATTACK_PAIR_PRIORITY_DISJOINT_LAYER_SIMULTANEOUS_LEGALITY_20260725.md`.
The purpose of this note is to compare its activated duplicate census with
the *floor-corrected* upper energy, without discarding the collisions fixed
by the layer.

At upper depth \(q\), let \(x_{q,U}\) be the load of target \(U\), and let
\(a_{j,q,U}\) be the number of its occurrences which are genuinely movable
by the adjacent block \((j,j+1)\).  Precisely, when the first-avoided
category of a loaded \(U\) is \(j<m\), put

\[
 a_{j,q,U}=
 \begin{cases}
 |\{\text{occurrences over }S:\ S\cap P_{j+1}=\varnothing\}|,
      &U\cap P_{j+1}\ne\varnothing,\\
 0,&U\cap P_{j+1}=\varnothing,
 \end{cases}
\tag{0.1}
\]

and put \(a_{m,q,U}=0\).  For a parity layer \(\Lambda\), replace
\(a_{j,q,U}\) by zero when \(j\notin\Lambda\).  Then its activated census
is

\[
 \mathcal C_{\Lambda,q}
 =\sum_{U:\,\kappa(U)=j\in\Lambda}\binom{a_{j,q,U}}2.
\tag{0.2}
\]

Every loaded target avoids the phase pair of its token, so its
first-avoided category \(\kappa(U)\) is defined.  Unloaded targets contribute
zero to every displayed census and may be omitted from the sums.

Define the complementary, literally uncharged collision census

\[
 \mathcal I_{\Lambda,q}
 =\sum_U\left\{\binom{x_{q,U}}2-
       \mathbf 1_{\{\kappa(U)\in\Lambda\}}
       \binom{a_{\kappa(U),q,U}}2\right\}.
\tag{0.3}
\]

The braces in (0.3) are nonnegative collision-pair counts.  They count
exactly the following cases: an inactive category, the final category
\(m\), a target avoiding the proposed partner pair, or a pair of
occurrences at least one of whose lower windows already meets the partner
pair.

Let \(p_q^{\min}\) be the exact integral factorial floor for mass \(T\) on
the \(K_q=\binom{2m+1}{m+q}\) upper targets, and let

\[
 \Phi_q=\sum_U\binom{x_{q,U}}2-p_q^{\min}
\]

be the half-floor excess.  Then the sharp charged-coverage identity is

\[
 \boxed{
 \mathcal C_{\Lambda,q}
 =\Phi_q-\bigl(\mathcal I_{\Lambda,q}-p_q^{\min}\bigr).}
\tag{0.4}
\]

Thus it is the **invariant surplus above the global arithmetic floor**, not
the raw invariant census, which obstructs descent.  With arbitrary
nonnegative finite weights \(w_q\), (0.4) remains exact after summation.
In particular, if

\[
 \mathfrak S_{\rm all}
 =\sum_{q=1}^Hw_q
   \bigl(\mathcal I_{{\rm all},q}-p_q^{\min}\bigr),
 \qquad
 \Phi_w=\sum_{q=1}^Hw_q\Phi_q,
\tag{0.5}
\]

then the better parity layer satisfies

\[
 \boxed{
 \max\{\mathcal C_{\rm odd},\mathcal C_{\rm even}\}
 \ge \frac12\bigl(\Phi_w-\mathfrak S_{\rm all}\bigr).}
\tag{0.6}
\]

This is the sharpest possible statement in terms of fixed collisions and
the exact floor: the right side is exactly one half of the complete
activated census before taking the maximum.

There is an absolute first-rank obstruction.  For every choice of exact
local factors,

\[
 \boxed{
 \mathcal C_{{\rm all},1}=0,
 \qquad
 \mathfrak S_{{\rm all},1}=\Phi_1,
 \qquad
 \Phi_1\ge \frac{W}{2m+1}=\operatorname{Cat}_m.}
\tag{0.7}
\]

Hence no positive comparison
\(\mathcal C_{\rm all}\ge\gamma\Phi_w\) can hold for arbitrary rank
weights, or even for the weight supported at \(q=1\).  This is a genuine
exact-factor obstruction, not an abstract load-vector example.  It does
not by itself obstruct constant one, because
\(\operatorname{Cat}_m=O(H\operatorname{Cat}_m)\); it says that a successful
iteration must either absorb the entire first-rank energy into the allowed
baseline or use a genuinely overlapping/joined atlas which is not a
disjoint interval layer.

At \(H=L\sqrt m\), one parity layer uses

\[
 r_\Lambda=O\!\left(\frac{W\log ^2m}{m}\right)
\]

interval bits, adds at most \(2r_\Lambda\) selected-row runs and at most
\(4r_\Lambda\) raw run endpoints, and therefore has \(H\)-weighted
boundary cost \(o(W)\).  Combining (0.6) with the exact layer descent gives
an integral corner whose doubled floor energy drops by at least

\[
 \frac12(\Phi_w-\mathfrak S_{\rm all})
\]

for those \(4r_\Lambda\) endpoints.  Consequently an active excess of
order \(W\) yields descent of order \(m/\log ^2m\) per permitted endpoint.

The exact missing theorem for contraction is now isolated: after removing
an allowed \(O_L(H\operatorname{Cat}_m)\) baseline, prove a uniform
\(\gamma>0\) for which

\[
 \mathfrak S_{\rm all}
 \le (1-\gamma)\Phi_w+O_L(H\operatorname{Cat}_m).
\tag{0.8}
\]

Under (0.8), one parity layer contracts the doubled floor energy by the
factor \(1-\gamma/4\), up to the stated baseline.  With a legal reset or an
overlapping-layer iteration, \(O_\gamma(\log m)\) rounds would leave
\(O_L(H\operatorname{Cat}_m)\) energy and would add only

\[
 O_\gamma\!\left(\frac{W\log ^3m}{m}\right)=o(W/H)
\]

run endpoints.  Neither (0.8) nor the reset is proved here.

## 1. Exact floors

For each \(1\le q\le H\), set

\[
 K_q=\binom{2m+1}{m+q}.
\]

Write, with no asymptotic replacement,

\[
 T=c_qK_q+\delta_q,
 \qquad 0\le\delta_q<K_q.
\tag{1.1}
\]

The minimum of the collision sum over all integral load vectors of mass
\(T\) on \(K_q\) targets is

\[
 \boxed{
 p_q^{\min}
 =(K_q-\delta_q)\binom{c_q}{2}
   +\delta_q\binom{c_q+1}{2}.}
\tag{1.2}
\]

Indeed, moving one unit from a coordinate at least two larger than another
strictly decreases the collision sum, so every minimizer has coordinates
\(c_q,c_q+1\); their counts are forced by (1.1).  Therefore

\[
 \Phi_q=\sum_U\binom{x_{q,U}}2-p_q^{\min}\ge0.
\tag{1.3}
\]

The doubled floor energy used by the interval-descent theorem is

\[
 \mathcal Q_w^+=2\Phi_w,
 \qquad
 \Phi_w=\sum_{q=1}^Hw_q\Phi_q.
\tag{1.4}
\]

At \(q=1\),

\[
 K_1=\binom{2m+1}{m+1}=W>T,
 \qquad c_1=0,
 \qquad p_1^{\min}=0.
\tag{1.5}
\]

Thus no quotient by a nonexistent positive first-rank floor parameter is
used anywhere below.

## 2. Which collision pairs one adjacent block moves

Every loaded upper target has a unique first-avoided category.  If an
occurrence over lower endpoint \(S\) has category \(j\), then

\[
 S\cap P_h\ne\varnothing\quad(h<j),
 \qquad S\cap P_j=\varnothing.
\tag{2.1}
\]

It belongs to the changed carrier for block \((j,j+1)\) exactly when it
also avoids \(P_{j+1}\).  Its upper target moves nontrivially exactly when
that target meets \(P_{j+1}\).  This proves (0.1).

Fix a target \(U\) of active category \(j\), and abbreviate

\[
 x=x_{q,U},\qquad a=a_{j,q,U},\qquad b=x-a.
\]

The collision pairs at \(U\) split, with no overlap, into the two movable
occurrences and all remaining pairs:

\[
 \boxed{
 \binom{x}{2}
 =\binom a2+ab+\binom b2.}
\tag{2.2}
\]

The first term is exactly the positive joined-Gram census of the interval
chart.  The other two terms are exactly the pairs having at least one fixed
occurrence.  If the category is not in the layer, if \(j=m\), or if
\(U\cap P_{j+1}=\varnothing\), the whole quantity \(\binom x2\) is fixed.
Summing (2.2) over active targets and adding those wholly fixed targets
proves

\[
 \boxed{
 \sum_U\binom{x_{q,U}}2
 =\mathcal C_{\Lambda,q}+\mathcal I_{\Lambda,q}.}
\tag{2.3}
\]

Subtracting (1.2) from (2.3) proves (0.4).  Notice that
\(\mathcal I_{\Lambda,q}-p_q^{\min}\) is signed.  Raw fixed collisions
below the global floor do not obstruct descent; the movable census must
then supply the missing floor mass before any excess remains.  Equivalently,

\[
 \mathcal C_{\Lambda,q}
 \ge \Phi_q-
 \bigl(\mathcal I_{\Lambda,q}-p_q^{\min}\bigr)_+,
\tag{2.4}
\]

but the equality (0.4) is sharper than (2.4).

## 3. Odd/even charged coverage

Put

\[
 \Lambda_{\rm odd}=\{j<m:j\text{ odd}\},
 \qquad
 \Lambda_{\rm even}=\{j<m:j\text{ even}\}.
\]

A movable collision pair has one unique category \(j<m\), so it belongs
to exactly one of these layers.  Therefore, for every depth and after
arbitrary nonnegative weighting,

\[
 \mathcal C_{\rm odd}+\mathcal C_{\rm even}
 =\mathcal C_{\rm all}.
\tag{3.1}
\]

Apply (0.4) with every index \(j<m\) active.  This gives

\[
 \mathcal C_{\rm all}=\Phi_w-\mathfrak S_{\rm all}.
\tag{3.2}
\]

Taking the larger member of (3.1) proves (0.6).  The simultaneous layer
theorem then supplies a literal integral interval corner \(M'\) with

\[
 \boxed{
 \mathcal Q_w^+(M')
 \le \mathcal Q_w^+(M_0)
   -\frac12(\Phi_w-\mathfrak S_{\rm all}).}
\tag{3.3}
\]

The factor \(1/2\) in (3.3) is only parity pigeonholing.  The factor
between a duplicate census and the half-energy convention is already
accounted for by using the doubled energy \(\mathcal Q_w^+=2\Phi_w\).

Suppose, conditionally, that (0.8) holds with error \(E_m\).  Equations
(3.2)--(3.3) yield

\[
 \mathcal Q_w^+(M')
 \le \left(1-\frac\gamma4\right)\mathcal Q_w^+(M_0)
       +\frac{E_m}{2}.
\tag{3.4}
\]

This is the exact one-layer contraction supplied by a charged-coverage
bound; there is no hidden floor error.

## 4. The first-upper-rank kernel is exact and nonempty

The exact-factor collar argument in the simultaneous-legality theorem
shows that

\[
 a_{j,1,U}\le1
\]

for every \(j,U\).  Indeed, two depth-one occurrences of the same
\((m+1)\)-set have disjoint two-point collars.  Here is the needed
adjacency check.  If two such collars shared \(c\), then
\(X=U\setminus\{c\}\) would be one of the two adjacent rank-\(m\) windows
of both occurrences.  Exactness places \(X\) at one unique physical
row-start.  There are precisely two token starts in that row for which
\(X\) is one of the two depth-one middle facets.  If the occurrences were
distinct, they would be those two consecutive starts.  Their upper flags
would then be two distinct proper cyclic \((m+1)\)-windows of the same row,
contrary to their both being \(U\).  Thus distinct occurrences have
disjoint collars.  Two changed occurrences avoiding the same partner pair,
while their common upper target meets that pair, would have a common collar
point.  This is impossible.  Hence

\[
 \mathcal C_{{\rm all},1}=0.
\tag{4.1}
\]

By (1.5) and (2.3),

\[
 \mathfrak S_{{\rm all},1}
 =\mathcal I_{{\rm all},1}
 =\sum_U\binom{x_{1,U}}2
 =\Phi_1.
\tag{4.2}
\]

It remains to prove that this exact kernel is nonempty for every exact
factor.  The first priority phase uses every lower target in
\([n]\setminus P_1\).  Its number of token occurrences is

\[
 A_m=\binom{2m-1}{m-1}.
\tag{4.3}
\]

All its first upper flags lie in the same \((2m-1)\)-point universe, where
the number of possible \((m+1)\)-targets is

\[
 K_m^{\rm loc}=\binom{2m-1}{m+1}
              =\binom{2m-1}{m-2}
              =\frac{m-1}{m+1}A_m.
\tag{4.4}
\]

For \(m\ge3\), distributing \(A_m\) integral occurrences among these
targets creates at least \(A_m-K_m^{\rm loc}\) collision pairs.  This is
the exact arithmetic minimum (for \(m=3\), every target has load two at
the minimum; for \(m>3\), the minimum loads are one and two).  Therefore

\[
 \begin{aligned}
 \Phi_1
 &\ge A_m-K_m^{\rm loc}
   =\frac{2A_m}{m+1}\\
 &=\frac{W}{2m+1}
   =\operatorname{Cat}_m.
 \end{aligned}
\tag{4.5}
\]

Other priority phases can only add collision pairs at this rank, because
the global first-rank floor is zero.  This proves all assertions in (0.7).
In particular, taking \(w_1>0\) and \(w_q=0\) for \(q>1\) disproves every
positive universal bound of \(\mathcal C_{\rm all}\) by \(\Phi_w\).

## 5. Exact endpoint accounting at \(H=L\sqrt m\)

Let

\[
 A_m=\binom{2m-1}{m-1},
 \qquad
 R_m=\frac{A_m}{2m-1}=\operatorname{Cat}_{m-1},
 \qquad
 t=\lceil20\log m\rceil.
\]

For either parity layer, the number of maximal physical carrier intervals
obeys

\[
 r_\Lambda
 \le R_mt(t+1)+4C\sqrt m\,A_m(3/4)^t
 =O\!\left(\frac{W\log ^2m}{m}\right),
\tag{5.1}
\]

where \(C\) is the absolute constant in the category-tail estimate.  The
exact ratios are

\[
 \frac{A_m}{W}=\frac{m+1}{2(2m+1)},
 \qquad
 \frac{R_m}{W}=\frac{m+1}{2(2m-1)(2m+1)}.
\tag{5.2}
\]

One interval choice adds at most two selected-row runs, equivalently at
most four raw run endpoints.  Thus the corner in (3.3) has

\[
 \Delta J\le2r_\Lambda,
 \qquad
 \partial_{\rm new}\le4r_\Lambda.
\tag{5.3}
\]

If \(\Phi_w>\mathfrak S_{\rm all}\), its certified descent per allowed raw
endpoint is at least

\[
 \boxed{
 \frac{\Phi_w-\mathfrak S_{\rm all}}{8r_\Lambda}.}
\tag{5.4}
\]

For fixed \(L\) and \(H=\lceil L\sqrt m\rceil\),

\[
 H r_\Lambda
 =O_L\!\left(\frac{W\log ^2m}{\sqrt m}\right)=o(W).
\tag{5.5}
\]

If the active excess \(\Phi_w-\mathfrak S_{\rm all}\) is
\(\Omega_L(W)\), then (5.4) is
\(\Omega_L(m/\log ^2m)\), much larger than \(H\).

Under the conditional contraction (3.4), starting from \(O_L(W)\) energy,
\(O_\gamma(\log m)\) legal rounds suffice to reach the fixed-point scale
\(O_\gamma(E_m)\).  Their cumulative endpoint catalog has size

\[
 O_\gamma\!\left(\frac{W\log ^3m}{m}\right),
\]

and multiplying by \(H=L\sqrt m\) gives

\[
 O_{L,\gamma}\!\left(\frac{W\log ^3m}{\sqrt m}\right)=o(W).
\tag{5.6}
\]

This last paragraph is conditional twice: (0.8) must remain valid at each
state, and successive parity updates must be made legal by an overlapping
owner theorem or a reset to a coherent first-avoided base.

## 6. Proved boundary

The simultaneous interval theorem plus the present calculation proves:

1. exact legality for every disjoint odd or even layer;
2. exact additive doubled-floor descent by its activated census;
3. the floor-corrected coverage identity (0.4), including all fixed
   collision pairs and every arithmetic floor;
4. the best-parity bound (0.6);
5. the exact endpoint ratio (5.4) and Gaussian-window budget (5.5);
6. the universal first-rank kernel and lower bound (0.7).

The surviving structural statement is not an unspecified Gram inequality.
It is precisely the invariant-surplus estimate (0.8), with the first-rank
kernel either absorbed into its allowed \(O_L(H\operatorname{Cat}_m)\)
term or attacked by a joined overlapping chart.  Without such an estimate,
the disjoint-layer atlas has no universal contraction: at \(q=1\) this is
already rigorously false for every exact local factor.

No constant-one conclusion is claimed.
