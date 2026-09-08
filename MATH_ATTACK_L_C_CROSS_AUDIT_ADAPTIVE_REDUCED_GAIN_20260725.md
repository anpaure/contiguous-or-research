# Lane L: cross-audit of the all-transposition C package and an exact adaptive reduced-gain dichotomy

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver,
computer algebra, or numerical experiment is used.

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
t=\frac Wn=\operatorname{Cat}_m,\qquad
H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed.  At depth \(q\), put

\[
r_q=m-q,\qquad N_q=\binom n{r_q},\qquad
\lambda_q=\frac W{N_q}=c_q+\theta_q,
\qquad c_q=\lfloor\lambda_q\rfloor,
\]

and retain the unhalved integer-floor potential

\[
\mathcal Q_A(F)=\sum_{q=1}^H\frac{Q_q(F)}{c_q},
\qquad
Q_q(F)=\sum_{|S|=r_q}
(\mu_q(S)-c_q)(\mu_q(S)-c_q-1).
\tag{0.1}
\]

Write

\[
f_q=\mu_q-\lambda_q\mathbf1,
\qquad
\beta_q=N_q\theta_q(1-\theta_q),
\qquad
B_A=\sum_{q\le H}\frac{\beta_q}{c_q}.
\tag{0.2}
\]

Let

\[
Q_0=\lfloor m^{1/8}\rfloor,
\qquad
\mathcal S_2(F)=
\sum_{q\le Q_0}\frac{\|P_{q,2}f_q\|_2^2}{c_q},
\qquad
\mathcal Q_A^{\rm red}=\mathcal Q_A-\mathcal S_2.
\tag{0.3}
\]

The three C reports have the following audited status.

1.  The giant-shield theorem is valid for genuine exact factors, provided
    local minimality means every subset of the freshly recomputed ownership
    components, and every transposition sum is over unordered coordinate
    transpositions.  It is a conditional structural theorem, not a
    construction of an all-transposition local minimum.

2.  The aggregate-reversal identity, its coefficient \(2(n-1)\), the
    equality classification, and the \(1/9\) and \(1/18\) rigidity constants
    are correct.  Its coefficient-two wall is a no-go for the aggregate
    ledger alone, not for an additional genuine chronology theorem.

3.  The Gram-chronology construction is valid as a decorated
    chronology-free system.  Its middle projection and every middle child
    are genuine exact factors, but its attached lower profiles are not the
    literal cyclic lower intervals of those factors.  It therefore does not
    refute the literal adaptive reduced-gain gate.

This report proves a new exact reduced-objective synthesis.  Define the
centered reduced mass

\[
\boxed{
\mathcal E_A^{\rm red}(F)
:=B_A+\mathcal Q_A^{\rm red}(F).}
\tag{0.4}
\]

For an unordered transposition \(\tau\), let \(s_\tau(F)\) be the largest
number of old-shore rows in one genuine ownership component of
\(F/(\tau F)\), and put

\[
k_s(F)=\#\{\tau:s_\tau(F)>s\},
\qquad
T_n=\binom n2.
\tag{0.5}
\]

Let

\[
D_{m,H}=\sum_{q=1}^H
\frac{(m-q)(m+q+1)-2}{c_q}.
\tag{0.6}
\]

For all sufficiently large \(m=m(A)\), so that
\(Q_0<H\le m-2\), and every integer \(s\ge0\), let

\[
G_\tau^{\rm red}(F)=
\max_I\bigl[
\mathcal Q_A^{\rm red}(F)-
\mathcal Q_A^{\rm red}(F^{\tau,I})
\bigr],
\qquad
G^{\rm red}(F)=\max_\tau G_\tau^{\rm red}(F),
\tag{0.7}
\]

where \(I\) ranges over all subsets of the freshly recomputed genuine
\(\tau\)-components, including the empty subset.  Then, whenever
\(k_s<T_n\),

\[
\boxed{
G^{\rm red}(F)\ge
\max\left\{0,
\frac{(n-1-k_s)\mathcal E_A^{\rm red}(F)
-\frac{s}{2}WD_{m,H}}
{T_n-k_s}
\right\}.}
\tag{0.8}
\]

This remains literally inside one exact factor fibre.  It uses one common
signing at every depth, and every child is a literal exact factor.  No
comparison error is present: shallow-\(E_2\) deletion is absorbed into a
permutation-equivariant positive semidefinite seminorm.

There is a second, sometimes stronger, inequality which explicitly uses the
verified same-row pair-run chronology.  Put

\[
\mathcal E_A(F)=B_A+\mathcal Q_A(F),
\qquad
\delta_m=\Gamma_AQ_0^4\frac tn,
\qquad
\Gamma_A=81e^{2(A+3)^2}.
\tag{0.9}
\]

Then

\[
\boxed{
G^{\rm red}(F)\ge
\max\left\{0,
\frac{(n-1-k_s)\mathcal E_A(F)-\frac{s}{2}WD_{m,H}}
{T_n-k_s}
-\delta_m
\right\}.}
\tag{0.10}
\]

Consequently, if \(g\ge0\), \(G^{\rm red}(F)\le g\), and
\(\mathcal E_A^{\rm red}(F)>g\), then every integer \(s\ge0\) obeys

\[
\boxed{
k_s(F)\ge
\left\lceil
\frac{(n-1)\mathcal E_A^{\rm red}(F)
-\frac{s}{2}WD_{m,H}-T_ng}
{\mathcal E_A^{\rm red}(F)-g}
\right\rceil.}
\tag{0.11}
\]

Thus the adaptive gate is reduced to a literal dichotomy: either the desired
reduced cut exists, or many freshly recomputed overlays contain giant
components.

More sharply, Theorem 6.1 uses the exact integer hinge chronology inside
every component, of arbitrary size.  With

\[
\rho_q(k)=\left\lfloor\frac{kq}{q+1}\right\rfloor
\]

and the chronological capacity \(\mathfrak C_\tau\) defined in (6.7), it
proves the unconditional constructive descent

\[
G^{\rm red}(F)\ge
\max\left\{0,
\frac{4(n-1)\mathcal E_A^{\rm red}(F)
-\sum_\tau\mathfrak C_\tau(F)}{4T_n}
\right\}.
\]

This replaces the component Cauchy coefficient \(k\) by the exact integral
coefficient \(k-\lceil k/(q+1)\rceil\), while retaining literal whole-row
signings and the full floor baseline.

Applied to the audited high-energy MSW cell from the previous Lane L report,
this becomes exponential.  For every fixed target constant \(D_A>0\), every
prescribed transposition \(\tau_0\), and all sufficiently large \(m\), there
is a genuine exact factor \(G_m\) such that either

\[
G^{\rm red}(G_m)>D_A\frac{Ht}{n},
\tag{0.12}
\]

or at least \(\lceil3(n-1)/4\rceil\) transpositions have a component larger
than

\[
s_m=\left\lfloor
\frac{(n-1)\underline E_m}{4WD_{m,H}}
\right\rfloor,
\qquad
\underline E_m=\frac{t4^H}{2048M_AH^4},
\qquad
M_A=\left\lceil e^{2(A+1)(A+2)}\right\rceil.
\tag{0.13}
\]

Moreover

\[
\boxed{
s_m\sim
\frac{4^H}{8192M_AI_AH^4m^{5/2}}
=\exp((A\log4+o_A(1))\sqrt m),
\quad
I_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}.}
\tag{0.14}
\]

At least \(\lceil(n+3)/4\rceil\) of these giant colours are nonnative to
the MSW matching.

The growing-harmonic fixed-\(A\) theorem in Section 11 strengthens this:
for every \(0<\gamma<\log4\), failure of the same adaptive gain forces

\[
\left(\frac{3\gamma A}{4}+o_{A,\gamma}(1)\right)
\frac{m^{3/2}}{\log(108m)}
\]

effective nonnative shield colours at an exponential threshold.  Conversely,
Section 12 proves a genuine fixed-colour no-go: a prescribed giant component,
and even a connected literal overlay with all common-row tails present, can
be flat at this high reduced energy.  Thus only a cross-transposition
no-recycling theorem can finish constant one.

This report does not prove that final exclusion.  Section 8 identifies the
exact common-row chronology absent from the decorated C ledger, while
Theorem 11.1 gives the constructive reduced descent whenever the required
superlinear active-shield family is absent.

## 1. Cross-audit: giant-shield report

The source is *MATH_ATTACK_C_ALL_TAU_GIANT_SHIELD_OBSTRUCTION_20260725.md*.

### 1.1 Valid normalizations

The identities

\[
\mathcal E_H=B_H+\mathcal Q_H
=\sum_{q\le H}\frac{\|f_q\|_2^2}{c_q}
\]

and

\[
\sum_{\tau}\mathscr R_{\tau,H}=2WD_{m,H}
\]

are exact.  One Johnson boundary edge contributes two coordinates to
\(\|w_C-\tau w_C\|_2^2\).  The \(E_2\) Johnson eigenvalue is
\(2(n-1)\), while the unordered-transposition displacement identity adds a
second factor two.  Hence

\[
\sum_\tau A_{\tau,H}\ge4(n-1)\mathcal E_H
\]

has the correct coefficient.

The Cauchy bound for components of at most \(s\) old rows,

\[
\sum_{\tau\in\mathcal T}V_{\tau,H}
\le2sWD_{m,H},
\]

is also exact.  The floor/factorial conversion

\[
\mathcal Q_H
=\sum_q(c_q+1)
\frac{\Phi_q}{\binom{c_q+1}{2}}
\]

and the constants in the AB7 insertion, native subtraction, and
\(D_{m,H}\sim I_Am^{5/2}\) are valid.

### 1.2 Required quantifier repairs

All transposition sums mean the \(T_n=\binom n2\) unordered coordinate
transpositions.  The report's stated all-cut local gate means

\[
\forall\tau\ \forall I:\quad
\mathcal Q_H(F^{\tau,I})\ge\mathcal Q_H(F),
\]

for every component subset, not merely for singleton flips.  With that
meaning the proof is valid.  The basic giant-shield inequality itself needs
only singleton nondecrease, because summing the singleton cut inequalities
already gives \(A_\tau\le V_\tau\); the equality classification and
quantitative cut rigidity in the aggregate report use full-subset locality.

The theorem is conditional: if an AB7-cell corner is local in every fresh
transposition cell, then linear-many fresh overlays have exponential-size
components.  It neither constructs such a corner nor excludes the required
giant components.  Components belonging to different transpositions are
distinct overlay objects and need not be row-disjoint.

The theorem concerns the full floor potential.  It does not, by itself,
prove a statement about \(\mathcal Q_A^{\rm red}\).

### 1.3 Omitted genuine-row lemma

The exact-factor claims require the following physical fact.  If
\(\tau=(ab)\) and \(C\) is one wreath row, some owned middle window contains
both or neither of \(a,b\).  Otherwise all \(n\) middle windows contain
exactly one, whereas their total \(a,b\)-incidence is \(2m=n-1\).  Thus an
owned root is fixed by \(\tau\), so the old row \(C\) and new row
\(\tau C\) lie in the same overlay component.  Consequently every component
is \(\tau\)-invariant, its new shore is \(\tau\) of its old shore, and a
complete-shore switch is a literal integral exact factor.

This missing proof is repairable and will be used below.

## 2. Cross-audit: aggregate-reversal report

The source is *MATH_ATTACK_C_ALL_TAU_AGGREGATE_REVERSAL_20260725.md*.

Fix positive weights \(a_q\).  The report defines

\[
\mathcal E_a=\sum_qa_qQ_q,
\]

which is a floor excess, not the centered norm.  With that convention, its
identity

\[
X_a-2(n-1)\mathcal E_a
=\frac12\sum_\tau(V_{\tau,a}-A_{\tau,a})
\tag{2.1}
\]

is exactly normalized.  Indeed,

\[
\|f_q\|_2^2=Q_q+\beta_q,
\]

the component norm counts both coordinates of a moved target pair, and the
Johnson edge sum counts that unordered pair once.  The higher surplus

\[
\sum_{j\ge3}(j-2)(n-j-1)\|f_{q,j}\|_2^2
\]

has the correct coefficient.

For one cell, the exact legal-cut formula is

\[
\mathcal E_a(F^I)-\mathcal E_a(F)
=-\langle d_I,d_{I^c}\rangle_a.
\tag{2.2}
\]

There is no missing factor: the anti-invariant profile is one half of
\(\sum_K\varepsilon_Kd_K\).  The equality classification by pairwise
orthogonal off-diagonal Gram entries is valid.  The quadratic-chaos lemma
gives

\[
V_{\tau,a}-A_{\tau,a}
\ge\frac19
\left(\sum_{K<L}\langle d_K,d_L\rangle_a^2\right)^{1/2},
\]

and hence the aggregate \(1/18\) remainder.  Both constants are correct.

The factorial weight is exactly \(a_q=1/[c_q(c_q+1)]\).  Locality for
that weighting is not implied by locality for \(1/c_q\), and the report
correctly keeps them separate.

The necessary repairs are:

1. local means every subset in every freshly recomputed cell;
2. the component anti-invariance uses the genuine-row lemma in Section 1.3;
3. the quoted slow \(U_2\) rate \(2/n\) is in the quarter-energy
   normalization; the raw averaged squared displacement is \(8/n\);
4. a coefficient-two upper bound is noncoercive only within the aggregate
   identity alone; a new chronology inequality may add information; and
5. all constants in a proposed strict upper estimate must be uniform in
   \(m\) and \(F\) after \(A\) is fixed.

The aggregate reversal extends to the reduced seminorm in Section 5; this
extension is not stated in the C report.

## 3. Cross-audit: Gram-chronology no-go report

The source is *MATH_ATTACK_C_ALL_TAU_GRAM_CHRONOLOGY_NOGO_20260725.md*.

The chiral statistic, its Johnson \(12\)-Lipschitz bound, the active-block
second moment, reflection balance, and the construction of an integral
Johnson \(1\)-Lipschitz load are valid.  Along the prime subsequence
\(n=2m+1\), the exact depth-one quantities are

\[
\lambda_1=\frac{m+2}{m},\qquad c_1=1,
\qquad W-N_1=\frac{2N_1}{m},
\]

and the constructed load satisfies

\[
Q_1=2|\mathcal H_-|+2(W-N_1),
\qquad
\liminf_{\substack{m\to\infty\\2m+1\ \mathrm{prime}}}
\frac{Q_1}{W}\ge\frac14.
\]

At every \(2\le q\le H\), the cyclic-orbit decoration has exact mass and
point margins and has \(Q_q=0\).  The row count and the coefficient
\(1/(2A)\) in its final ratio are correct.

The following wording corrections are necessary.

1. Depthwise nondecrease is equivalent to the depthwise inequalities

   \[
   -\langle d_{I,q},d_{I^c,q}\rangle_2\ge0.
   \]

   The single weighted Gram inequality is equivalent only to nondecrease of
   the weighted total.  The construction proves the stronger depthwise
   assertion.

2. The old pair difference in the pair-energy calculation is the aggregate

   \[
   z_p=\mu_q(S)-\mu_q(\tau S)=\sum_Kz_{K,p},
   \]

   not one component difference.

3. Every liminf is along the prime subsequence.

4. The all-transposition quantifier agrees with the literal gate, but the
   domain does not.  A switched child is a genuine exact *middle* factor;
   its lower energy in this construction is the energy of artificial
   attached orbit profiles, not of that child's cyclic lower intervals.

Accordingly, the report is a valid chronology-free no-go.  It is not an
exact-factor-fibre counterexample, it does not refute the reduced gate, and
its \(\Omega(W)\) energy is not proved to survive shallow-\(E_2\) deletion.

## 4. The reduced harmonic seminorm

For each depth use the ordinary Johnson decomposition

\[
f_q=\sum_{j\ge2}P_{q,j}f_q.
\]

The degrees \(0,1\) vanish because an exact factor has exact total and point
margins.  Define the permutation-equivariant positive semidefinite form

\[
\langle g,h\rangle_T
=\sum_{q\le H}\frac1{c_q}
\left(
\langle g_q,h_q\rangle_2
-\mathbf1_{\{q\le Q_0\}}
\langle P_{q,2}g_q,P_{q,2}h_q\rangle_2
\right).
\tag{4.1}
\]

On exact-factor discrepancies and component effects, whose degrees \(0,1\)
vanish, its multiplier is \(1/c_q\) on every \(j\ge2\), except that it is
zero on \(j=2,q\le Q_0\).  (Formula (4.1) also assigns \(1/c_q\) to
degrees \(0,1\) on arbitrary vectors, but those sectors never occur here.)
Hence

\[
\boxed{
\|f(F)\|_T^2
=B_A+\mathcal Q_A^{\rm red}(F)
=\mathcal E_A^{\rm red}(F).}
\tag{4.2}
\]

Fix an unordered transposition \(\tau\), and use its genuine components
from Section 1.3.  If \(d_K\) is the old-shore minus new-shore lower
histogram, set

\[
A_\tau^T=\left\|\sum_Kd_K\right\|_T^2,
\qquad
V_\tau^T=\sum_K\|d_K\|_T^2.
\tag{4.3}
\]

The cell midpoint is \(\tau\)-invariant and each \(d_K\) is
\(\tau\)-anti-invariant.  Therefore a component signing \(\varepsilon\)
has

\[
\mathcal Q_A^{\rm red}(F_\varepsilon)
=C_{\tau,F}+\frac14
\left\|\sum_K\varepsilon_Kd_K\right\|_T^2-B_A,
\tag{4.4}
\]

where \(C_{\tau,F}\) is independent of the signing.  In particular,

\[
\mathcal Q_A^{\rm red}(F^I)-\mathcal Q_A^{\rm red}(F)
=-\langle d_I,d_{I^c}\rangle_T,
\tag{4.5}
\]

and averaging independent signs gives

\[
\boxed{
G_\tau^{\rm red}(F)\ge
\frac14(A_\tau^T-V_\tau^T).}
\tag{4.6}
\]

This is a seminorm, not a strictly positive norm, but every identity remains
valid.  The signs are common across all depths and are the signs of literal
whole-row components.

There is also a sharp deterministic PSD cut refinement.  If the cell has
\(h\ge2\) components, put

\[
c_h=\frac{\lfloor h^2/4\rfloor}{h(h-1)}.
\]

For a uniformly chosen component subset of size \(a\), each unordered
component pair is separated with probability
\(2a(h-a)/[h(h-1)]\).  Taking \(a=\lfloor h/2\rfloor\) gives

\[
\boxed{
G_\tau^{\rm red}(F)
\ge c_h(A_\tau^T-V_\tau^T)_+.}
\tag{4.6a}
\]

For \(h=1\), \(A_\tau^T=V_\tau^T\) and the cell is flat.  The constant
\(c_h\) is sharp from the data \((A_\tau^T,V_\tau^T,h)\), as witnessed by
a positive semidefinite Gram matrix with constant diagonal and constant
off-diagonal entry.  Thus energy alone cannot improve (4.6a); genuine row
structure must force retained off-diagonal coherence.

The aggregate reversal also survives verbatim.  If

\[
\mathsf S_T=
\sum_{q,j}b_{q,j}
[j(n-j+1)-2(n-1)]\|P_{q,j}f_q\|_2^2,
\]

where \(b_{q,j}\) is the multiplier of (4.1), and

\[
\mathbf V_T=\frac12\sum_\tau V_\tau^T,
\qquad
X_T=\mathbf V_T-2(n-1)B_A-\mathsf S_T,
\]

then

\[
\boxed{
X_T-2(n-1)\mathcal Q_A^{\rm red}(F)
=\frac12\sum_\tau(V_\tau^T-A_\tau^T).}
\tag{4.7}
\]

Thus all-transposition reduced locality again reverses the aggregate gate;
the shallow deletion does not bypass the coefficient-two wall.

## 5. Spectral heat and literal cyclic-row capacity

Because the form \(T\) commutes with every coordinate permutation, the
unordered-transposition identity and the Johnson eigenvalues give

\[
\begin{aligned}
\sum_\tau A_\tau^T
&=2\sum_{q,j}b_{q,j}j(n-j+1)
\|P_{q,j}f_q\|_2^2\\
&\ge4(n-1)\|f\|_T^2.
\end{aligned}
\]

Therefore

\[
\boxed{
\sum_\tau A_\tau^T
\ge4(n-1)\mathcal E_A^{\rm red}(F).}
\tag{5.1}
\]

Also, for each \(\tau\), orthogonality gives

\[
\boxed{A_\tau^T\le4\mathcal E_A^{\rm red}(F).}
\tag{5.2}
\]

The variance capacity is where literal same-row geometry first enters.
For a physical wreath row \(C\), let \(w_{C,q}\) be the indicator of its
\(n\) genuine cyclic rank-\(r_q\) intervals.  Those intervals induce
exactly \(n\) edges of \(J(n,r_q)\).  Since the Johnson degree is

\[
d_q=r_q(n-r_q)=(m-q)(m+q+1),
\]

their edge boundary has size \(n(d_q-2)\).  Each boundary edge is generated
by a unique unordered coordinate transposition and contributes two
coordinates.  Hence

\[
\boxed{
\sum_\tau\|w_{C,q}-\tau w_{C,q}\|_2^2
=2n(d_q-2).}
\tag{5.3}
\]

This is false for arbitrary point-regular attached profiles; it uses the
consecutive intervals of the same physical row.

Since \(\|g\|_T\le\|g\|_H\), where

\[
\|g\|_H^2=\sum_{q\le H}\frac{\|g_q\|_2^2}{c_q},
\]

Cauchy--Schwarz and (5.3) show that, for any family \(\mathcal U\) of
transpositions all of whose components have at most \(s\) old rows,

\[
\boxed{
\sum_{\tau\in\mathcal U}V_\tau^T
\le2sWD_{m,H}.}
\tag{5.4}
\]

No row is detached from its other depths in this argument: \(d_K\) is the
common whole-row effect.  The estimate does, however, discard the possible
cross-depth cancellation by dominating \(T\) with the full rankwise norm.

## 6. Proof of the adaptive reduced-gain inequality

Let \(\mathcal L_s=\{\tau:s_\tau(F)>s\}\), so
\(|\mathcal L_s|=k_s\).  By (5.1)--(5.2),

\[
\sum_{\tau\notin\mathcal L_s}A_\tau^T
\ge4(n-1-k_s)\mathcal E_A^{\rm red}(F).
\tag{6.1}
\]

Sum (4.6) over the \(T_n-k_s\) small-component colours, and apply (5.4):

\[
\sum_{\tau\notin\mathcal L_s}G_\tau^{\rm red}(F)
\ge
(n-1-k_s)\mathcal E_A^{\rm red}(F)
-\frac{s}{2}WD_{m,H}.
\tag{6.2}
\]

The largest term is at least the average.  The empty signing gives gain
zero.  This proves (0.8).

If \(G^{\rm red}\le g\), the left side of (6.2) is at most
\((T_n-k_s)g\).  Rearranging gives

\[
k_s(\mathcal E_A^{\rm red}-g)
\ge
(n-1)\mathcal E_A^{\rm red}
-\frac{s}{2}WD_{m,H}-T_ng.
\]

When \(\mathcal E_A^{\rm red}>g\), integrality of \(k_s\) proves (0.11).
If the displayed lower bound exceeds \(T_n\), the hypothesis
\(G^{\rm red}\le g\) is impossible.

At an all-transposition reduced local minimum with
\(\mathcal E_A^{\rm red}(F)>0\), take \(g=0\).  For every integer
\(s\ge0\),

\[
\boxed{
k_s(F)\ge
\left\lceil n-1-
\frac{sWD_{m,H}}{2\mathcal E_A^{\rm red}(F)}
\right\rceil.}
\tag{6.3}
\]

This is the reduced-potential analogue of the C giant-shield theorem, with
no shallow-sector error.

### 6.1 Exact chronology-floor capacity and size-free descent

The component Cauchy factor can be improved for every literal component,
without imposing a size cutoff.  Fix \(\tau,q\), let \(K\) have \(k\)
old-shore rows, and define

\[
R_{\tau,K,q}=
\sum_{C\in L_K}\|w_{C,q}-\tau w_{C,q}\|_2^2,
\qquad
\rho_q(k)=\left\lfloor\frac{kq}{q+1}\right\rfloor
=k-\left\lceil\frac{k}{q+1}\right\rceil.
\tag{6.4}
\]

### Theorem 6.1 (integer chronology improvement)

For every genuine component,

\[
\boxed{
\|d_{K,q}\|_2^2
\le\rho_q(k)R_{\tau,K,q}.}
\tag{6.5}
\]

#### Proof

Fix a rank-\(r_q\) target \(S\), put \(T=\tau S\), and write

\[
a_C=g_C(S),\qquad b_C=g_C(T)
\qquad(C\in L_K).
\]

Here \(0\le a_C,b_C\le q+1\), and the literal hinge identity gives

\[
w_{C,q}(S)=\mathbf1_{\{a_C=q+1\}},
\qquad
w_{C,q}(T)=\mathbf1_{\{b_C=q+1\}}.
\]

Let \(U_K\) be the common middle-root union partitioned by either shore of
the component.  Because \(U_K\) is \(\tau\)-invariant,

\[
\sum_Ca_C=\sum_Cb_C.
\tag{6.6}
\]

Let \(x\) and \(y\) be the numbers of top entries \(q+1\) in the two
lists.  If \(x>y\), equality of the sums gives

\[
x(q+1)\le y(q+1)+(k-y)q=kq+y,
\]

and therefore

\[
(x-y)(q+1)\le q(k-y)\le kq.
\]

Interchanging the lists handles \(y>x\).  Thus

\[
|d_{K,q}(S)|=|x-y|\le\rho_q(k).
\]

Since \(d^2\le\rho_q(k)|d|\), while the row differences take values only
in \(\{0,\pm1\}\),

\[
\begin{aligned}
\|d_{K,q}\|_2^2
&\le\rho_q(k)\sum_S|d_{K,q}(S)|\\
&\le\rho_q(k)
\sum_{C\in L_K}\sum_S
|w_{C,q}(S)-\tau w_{C,q}(S)|\\
&=\rho_q(k)R_{\tau,K,q}.
\end{aligned}
\]

This proves (6.5). \(\square\)

The integer improvement is strict: \(\rho_q(1)=0\), and for
\(2\le k\le q+1\), \(\rho_q(k)=k-1\).  In particular, every literal
size-two component has coefficient one, rather than the Cauchy coefficient
two.

Define the fully chronological component capacity

\[
\boxed{
\mathfrak C_\tau(F)=
\sum_{q\le H}\frac1{c_q}
\sum_{K}\rho_q(|L_K|)R_{\tau,K,q}.}
\tag{6.7}
\]

Since the reduced \(T\)-seminorm is dominated by the full weighted norm,
(6.5) gives

\[
V_\tau^T\le\mathfrak C_\tau(F).
\]

Combining this with (4.6) and (5.1), with no component-size hypothesis,
proves the constructive formula

\[
\boxed{
G^{\rm red}(F)\ge
\max\left\{0,
\frac{4(n-1)\mathcal E_A^{\rm red}(F)
-\sum_\tau\mathfrak C_\tau(F)}{4T_n}
\right\}.}
\tag{6.8}
\]

Thus the adaptive target follows constructively whenever

\[
\sum_\tau\mathfrak C_\tau(F)
<4(n-1)\mathcal E_A^{\rm red}(F)
-4T_nD_A\frac{Ht}{n}.
\tag{6.9}
\]

Conversely, every all-transposition reduced local minimum obeys the exact
chronological restitution inequality

\[
\boxed{
\sum_\tau\mathfrak C_\tau(F)
\ge4(n-1)\mathcal E_A^{\rm red}(F).}
\tag{6.10}
\]

If every component has at most an integer \(s\) rows, monotonicity of
\(\rho_q\) and
the physical row identity (5.3) sharpen the old capacity to

\[
\boxed{
\sum_\tau\mathfrak C_\tau(F)
\le2W\sum_{q\le H}
\frac{\rho_q(s)[(m-q)(m+q+1)-2]}{c_q}.}
\tag{6.11}
\]

Theorem 6.1 is the exact gain supplied by one-target same-row chronology.
For connected components \(k=t\), however,
\(\rho_q(t)=t-\lceil t/(q+1)\rceil\) is still of order \(t\).  Hence
(6.8) is a genuine fixed-\(A\) descent theorem but does not by itself close
the giant/connected case.

## 7. The second inequality from genuine pair-run chronology

For a coordinate pair \(e\), let \(d_C(e)\le m\) be its cyclic distance in
the physical row \(C\), and put

\[
s_C(e)=m-d_C(e).
\]

This is the number of middle windows of \(C\) containing \(e\).  Exact
middle ownership gives the same-row identity

\[
\boxed{
\sum_{C\in F}s_C(e)
=\binom{n-2}{m-2}=\frac{m-1}{2}t.}
\tag{7.1}
\]

Define

\[
H_e^{(q)}=\sum_C(q-s_C(e))_+.
\]

The chord inequality

\[
(q-s)_+\le q\left(1-\frac{s}{m-1}\right)
\]

and (7.1) give

\[
0\le H_e^{(q)}\le\frac{qt}{2}.
\tag{7.2}
\]

The exact pair-star inversion then yields, for every exact factor \(G\),
every transposition \(\tau\), and \(q\le H\),

\[
\boxed{
\|P_{q,2}(f_q(G)-\tau f_q(G))\|_2^2
\le
\frac{2q^2(q+1)t^2}{\alpha_q},
\qquad
\alpha_q=\binom{n-4}{m-q-2}.}
\tag{7.3}
\]

This is genuine common-row chronology: all depths use the same integers
\(s_C(e)\), not independently chosen pair marginals.

Every component-signing child is another exact factor.  On one cell, the
change of the shallow \(E_2\) norm is one quarter of the difference of two
complete-factor transposition residuals.  Equations (7.3) and
\(W/\alpha_q\le\Gamma_A\), together with \(c_q\ge1\) and
\(\sum_{q\le Q_0}q^2(q+1)\le Q_0^4\) for \(Q_0\ge2\), therefore give

\[
\boxed{
|\mathcal S_2(F)-\mathcal S_2(F^{\tau,I})|
\le\delta_m
=\Gamma_AQ_0^4\frac tn.}
\tag{7.4}
\]

Apply the full-norm version of (4.6) and then subtract the error (7.4):

\[
G_\tau^{\rm red}(F)
\ge\frac14(A_\tau-V_\tau)-\delta_m.
\]

The full spectral and row-capacity estimates are

\[
\sum_\tau A_\tau\ge4(n-1)\mathcal E_A(F),
\qquad
\sum_{\tau\notin\mathcal L_s}V_\tau\le2sWD_{m,H}.
\]

Average over the small-component transpositions.  This proves (0.10).

The direct seminorm estimate (0.8) and chronology comparison (0.10) are
both exact.  Neither uniformly dominates the other: (0.8) has no error,
while (0.10) uses the larger full centered mass.

## 8. An exact common-row tail representation still unused by the C ledgers

The preceding proof uses two genuine consequences of physical rows:

1. the rankwise cyclic Johnson boundary (5.3); and
2. the common pair-run statistic (7.1)--(7.3).

There is a stronger exact cross-depth identity.  Fix a nonempty coordinate
set \(X\), \(|X|=j\), and a physical row \(C\).  Let

\[
g_C(X)=\#\{\text{middle }m\text{-windows of }C\text{ containing }X\}.
\]

For a rank histogram \(h\), write
\(D_Xh=\sum_{S\supseteq X}h(S)\), and let \(w_{C,0}\) denote the
middle-window indicator.  For every integer \(0\le q\le m-j\), the number
of rank-\((m-q)\) cyclic intervals of the same row containing \(X\) is

\[
\boxed{D_Xw_{C,q}=(g_C(X)-q)_+.}
\tag{8.1}
\]

Consequently, for a genuine \(\tau\)-component \(K\), let \(L_K\) denote
its old-shore row set.  Then

\[
\boxed{
D_Xd_{K,q}
=\sum_{C\in L_K}
\bigl[(g_C(X)-q)_+-(g_C(\tau X)-q)_+\bigr].}
\tag{8.2}
\]

In particular, if \(u_{K,X}(q)=D_Xd_{K,q}\), then for
\(1\le q\le m-j-1\),

\[
\Delta^2u_{K,X}(q)
=\#\{C\in L_K:g_C(X)=q\}
-\#\{C\in L_K:g_C(\tau X)=q\},
\tag{8.3}
\]

where \(\Delta^2u(q)=u(q-1)-2u(q)+u(q+1)\).  Hence

\[
\boxed{
\sum_{q=1}^{m-j-1}|\Delta^2u_{K,X}(q)|\le2|L_K|.}
\tag{8.4}
\]

For use only inside the Gaussian objective window, the sum in (8.4) may be
truncated at \(\min\{H,m-j-1\}\).  The endpoint values come from the same
physical row profiles at depths outside the objective window; no artificial
extension is being made.

Equations (8.1)--(8.4) use the same owner rows and the same run lengths at
every depth.  They fail for the independently attached orbit decorations in
the Gram no-go report.  That report therefore shows precisely why replacing
(8.2) by rankwise mass, point margins, pair-total preservation, or abstract
Gram positivity cannot finish the proof.

There is, however, an exact limitation even on (8.2)--(8.4) when they are
used one cylinder at a time.

### Theorem 8.1 (sharp one-cylinder chronology bound and no-go)

Let \(K\) be a genuine \(\tau\)-component with \(k=|L_K|\) old rows, fix
nonempty \(X\), \(|X|=j\), and put \(D=m-j+1\).  For \(C\in L_K\), set

\[
a_C=g_C(X),\qquad b_C=g_C(\tau X).
\]

The middle-root union of a component is \(\tau\)-invariant.  Since either
shore partitions that union,

\[
\sum_Ca_C
=\#\{M\in U_K:X\subseteq M\}
=\#\{M\in U_K:\tau X\subseteq M\}
=\sum_Cb_C.
\tag{8.5}
\]

Extend \(u(q)=D_Xd_{K,q}\) by the hinge formula to \(0\le q\le D\).
Then

\[
\boxed{
|u(q)|\le\frac{kq(D-q)}D.}
\tag{8.6}
\]

Consequently,

\[
\boxed{
\sum_{q=1}^{D-1}u(q)^2
\le\frac{k^2}{30}\left(D^3-D^{-1}\right).}
\tag{8.7}
\]

#### Proof

Let \(M=\sum_Ca_C=\sum_Cb_C\) and
\(\phi_q(x)=(x-q)_+\).  For \(0\le x\le D\), convexity and the endpoint
chord give

\[
\phi_q(x)\le\frac{D-q}{D}x.
\]

On the other hand,

\[
\sum_C\phi_q(b_C)\ge\max\{0,M-kq\}.
\]

Thus

\[
u(q)\le\frac{D-q}{D}M-\max\{0,M-kq\}.
\]

Maximizing the right side over \(0\le M\le kD\) gives
\(kq(D-q)/D\); interchange \(a,b\) for the lower bound.  Finally,

\[
\sum_{q=1}^{D-1}q^2(D-q)^2=\frac{D^5-D}{30},
\]

which proves (8.7). \(\square\)

The quadratic dependence on \(k\) cannot be improved from these scalar
data.  If \(k,D\) are even, take the \(a\)-multiset to consist of \(k/2\)
zeroes and \(k/2\) copies of \(D\), and take every \(b_C=D/2\).  The totals
in (8.5) agree, all data are integral, and

\[
u(q)=
\begin{cases}
kq/2,&q\le D/2,\\
k(D-q)/2,&q\ge D/2.
\end{cases}
\]

Hence equality holds in (8.6) at \(q=D/2\), while

\[
\sum_{q=1}^{D-1}u(q)^2
=\frac{k^2(D^3+2D)}{48}.
\tag{8.8}
\]

This extremizer belongs to the complete scalar hinge/endpoint/second-
difference constraint class, including (8.4), but is not asserted to be
simultaneously realizable by literal rows.  Therefore no component-variance
bound linear in \(k\) can follow one \(X\) at a time from (8.2)--(8.5).
Any size-free replacement for Cauchy must exploit simultaneous compatibility
among different \(X\) in the same cyclic rows, together with cross-
transposition component structure.

The present adaptive inequalities do not yet exploit (8.2) strongly enough:
(5.4) discards its cross-depth correlation, and (7.4) retains only its
degree-two projection.  Growing Johnson degrees and giant or connected
overlays remain uncontrolled.

## 9. A literal Johnson-Lipschitz fork

The decorated Gram construction suggests a precise genuine-factor test.

### Theorem 9.1 (literal realization would refute the reduced gate)

Fix \(A>0\) and \(\eta>0\).  Suppose that for infinitely many \(m\) there
is a literal exact wreath factor \(F_m\) such that

\[
Q_1(F_m)\ge\eta W,
\tag{9.1}
\]

its genuine depth-one load is Johnson \(1\)-Lipschitz,

\[
|\mu_1(S)-\mu_1(T)|\le1
\qquad(ST\in E(J(n,m-1))),
\tag{9.2}
\]

and either

\[
Q_q(F_m)=0\quad(2\le q\le H),
\tag{9.3}
\]

or, more generally, every genuine \(\mu_q\), \(q\le H\), is Johnson
\(1\)-Lipschitz.  Then

\[
\boxed{
\mathcal Q_A^{\rm red}(F_m)\ge\eta W-o_A(W),
\qquad
G^{\rm red}(F_m)
\le\delta_m
\le\frac{\Gamma_A}{A}\frac{Ht}{n}.}
\tag{9.4}
\]

Consequently, for every \(D_A>\Gamma_A/A\) and every fixed \(K_A\), these
factors violate the proposed implication

\[
\mathcal Q_A^{\rm red}>K_AHt
\quad\Longrightarrow\quad
G^{\rm red}>D_AHt/n
\]

for all sufficiently large members of the sequence.

#### Proof

For a moved pair \(\{S,\tau S\}\), a complete component signing preserves
the pair total.  Under (9.2), the two initial integral loads are the balanced
pair for that total, so no signing can lower their depth-one floor energy.
If (9.3) holds, every deeper initial floor energy is already zero, while
every child's floor energy is nonnegative.  Under the more general
alternative, the same balanced-pair argument applies separately at every
depth.  Thus every genuine component signing satisfies

\[
\mathcal Q_A(F^{\tau,I})\ge\mathcal Q_A(F).
\]

The universal same-row pair chronology bound gives

\[
\mathcal S_2(F)
\le\frac{\Gamma_A}{2}Q_0^4t=o_A(W).
\]

Together with (9.1) and nonnegativity of all \(Q_q\), this proves the first
part of (9.4).  For every signing,

\[
\begin{aligned}
\mathcal Q_A^{\rm red}(F)-
\mathcal Q_A^{\rm red}(F^{\tau,I})
&=\mathcal Q_A(F)-\mathcal Q_A(F^{\tau,I})\\
&\quad-
[\mathcal S_2(F)-\mathcal S_2(F^{\tau,I})]\\
&\le\delta_m
\end{aligned}
\]

by (7.4).  Finally, \(Q_0^4\le\sqrt m\le H/A\), giving the last bound in
(9.4).  Since \(Ht=(A/2+o_A(1))W/\sqrt m=o(W)\), every fixed high-energy
premise is eventually satisfied. \(\square\)

Theorem 9.1 is conditional, but its logical force is exact.  The decorated C
report realizes every displayed property except that its lower profiles are
not the cyclic intervals of the owning rows.  Therefore a proof of the
adaptive gate must use the literal common-row tail representation to exclude
this realization; Gram cuts, point margins, parity, and middle exactness do
not suffice.

The following unconditional theorem supplies new literal constraints on any
such realization.

### Theorem 9.2 (exact chronological tail packets)

Let \(\mu=\mu_1\) be the genuine first-shadow load of an exact factor and
assume it is Johnson \(1\)-Lipschitz.  Put

\[
V_1=\binom{[n]}{m-1},\qquad
L_a=\{S\in V_1:\mu(S)\le a\},\qquad
T_b=\{S\in V_1:\mu(S)\ge b\},
\]

\[
M_b=\sum_{S\in T_b}\mu(S),
\qquad
\partial_{q-1}L_a=
\{X\in\tbinom{[n]}{m-q}:X\subset S
\text{ for some }S\in L_a\}.
\]

Then, for every integer \(a\ge0\) and \(2\le q\le H\),

\[
\boxed{
\sum_{X\in\partial_{q-1}L_a}\mu_q(X)
\le
\sum_{\substack{S\in V_1\\1\le\mu(S)\le a+q-1}}\mu(S)
=W-M_{a+q}.}
\tag{9.5}
\]

#### Proof

Count triples \((C,X,S)\) in which \(X\) is a genuine rank-\((m-q)\)
interval of row \(C\), \(X\in\partial_{q-1}L_a\), and \(S\) is a genuine
rank-\((m-1)\) interval of the same row containing \(X\).  Every occurrence
\((C,X)\) has exactly \(q\) such superintervals.  Choose
\(S_0\in L_a\) containing \(X\).  Since \(S,S_0\) both contain \(X\),

\[
d_J(S,S_0)\le q-1.
\]

Lipschitzness and the occurrence of \(S\) give

\[
1\le\mu(S)\le a+q-1.
\]

Conversely, one occurrence \((C,S)\) contains exactly \(q\) genuine
rank-\((m-q)\) intervals.  Count from the two sides and cancel \(q\).
This cancellation uses the same physical row and is unavailable for the
decorated profiles. \(\square\)

Suppose additionally that \(Q_q=0\).  Put

\[
\zeta_q=W-c_qN_q,
\qquad
\mathcal U_q=\{X:\mu_q(X)=c_q+1\}.
\]

Then \(\mu_q=c_q+\mathbf1_{\mathcal U_q}\),
\(|\mathcal U_q|=\zeta_q\), and (9.5) becomes

\[
\boxed{
c_q|\partial_{q-1}L_a|
+|\mathcal U_q\cap\partial_{q-1}L_a|
\le W-M_{a+q}.}
\tag{9.6}
\]

The normalized Boolean-shadow inequality

\[
\frac{|\partial_{q-1}L_a|}{N_q}
\ge\frac{|L_a|}{N_1}
\]

therefore gives the floor-sensitive packet

\[
\boxed{
M_{a+q}+|\mathcal U_q\cap\partial_{q-1}L_a|
\le
\zeta_q+\frac{c_qN_q}{N_1}|T_{a+1}|.}
\tag{9.7}
\]

For \(q=2\) and sufficiently large \(m\),

\[
c_2=1,\qquad
\kappa=\frac{N_2}{N_1}=\frac{m-1}{m+3},
\qquad
\zeta_1=W-N_1=\frac{2N_1}{m}.
\]

Writing

\[
v_h=|\{S:\mu(S)=h\}|,
\qquad
E_{a+2}=\sum_{h\ge a+2}(h-1)v_h,
\]

equation (9.6) and normalized shadow give

\[
\boxed{
E_{a+2}+|\mathcal U_2\cap\partial_1L_a|
\le
v_{a+1}+\zeta_1+\frac4{m+3}|L_a|.}
\tag{9.8}
\]

Indeed,

\[
\sum_{1\le h\le a+1}hv_h-|L_a|
=\zeta_1+v_{a+1}-E_{a+2},
\qquad
1-\kappa=\frac4{m+3}.
\]

There is also a pointwise zero packet.  Put

\[
Z=\{S:\mu(S)=0\},\qquad
V_{=1}=\{S:\mu(S)=1\},\qquad
u_2(S)=|\{X\in\mathcal U_2:X\subset S\}|.
\]

If \(Q_2=0\), then every \(S\in Z\) satisfies

\[
\boxed{
|\Gamma_J(S)\cap V_{=1}|
\ge2(m-1+u_2(S)).}
\tag{9.9}
\]

To prove this, note that

\[
R_2(S):=
\sum_{\substack{X\subset S\\|X|=m-2}}\mu_2(X)
=m-1+u_2(S).
\]

One physical row cannot contain two distinct rank-\((m-2)\) intervals
inside \(S\): their union would be the rank-\((m-1)\) interval \(S\),
contrary to \(\mu(S)=0\).  Hence these occurrences belong to distinct rows.
Each has two same-row rank-\((m-1)\) superintervals, both distinct from
\(S\), and Lipschitzness forces both loads to equal one.  No endpoint can
repeat, proving (9.9).

Counting these packets over all zero sets gives

\[
\boxed{
(m-1)|Z|+\sum_{S\in Z}u_2(S)
\le(m+1)|V_{=1}|.}
\tag{9.10}
\]

Indeed, a load-one target has one physical row occurrence and two
rank-\((m-2)\) subintervals.  For either subinterval, at most \(m+1\) of
its other rank-\((m-1)\) supersets can be zero, because the two physical
endpoints are nonzero.

Finally, there is a dual run-tail identity.  For \(S\in V_1\), let
\(\ell_C(S)\) be the longest cyclic run of coordinates of \(S\) in row
\(C\), and put \(\delta_C(S)=m-1-\ell_C(S)\).  Uniformly for
\(0\le q\le H+1\),

\[
\boxed{
R_q(S):=
\sum_{\substack{X\subset S\\|X|=m-q}}\mu_q(X)
=\sum_C(q-\delta_C(S))_+.}
\tag{9.11}
\]

At most one run has length \(m-q\), since \(2(m-q)>m-1\).  This proves
(9.11), and discrete differences give

\[
\boxed{
R_{q+1}(S)-2R_q(S)+R_{q-1}(S)
=\#\{C:\delta_C(S)=q\}}
\qquad(1\le q\le H).
\tag{9.12}
\]

When \(Q_q=0\), the same quantity is exactly

\[
\boxed{
R_q(S)=
c_q\binom{m-1}{q-1}
+|\mathcal U_q\cap\tbinom{S}{m-q}|.}
\tag{9.13}
\]

The packets (9.5)--(9.13) are genuine same-row restrictions absent from the
decorated obstruction.  They do not yet exclude (9.1): at the scalar limiting
level, proportions \(p_0=p_1=p_2=1/3\) satisfy the resulting \(q=2\)
inequalities while retaining positive floor energy.  The unresolved step is
simultaneous compatibility of these packets across different \(S\) and all
depths.

## 10. Application to the high exact MSW cell

The audited previous Lane L report proves that, for every prescribed
\(\tau_0\), there is a literal exact factor \(G_m\) satisfying

\[
\mathcal Q_A^{\rm red}(G_m)
\ge
\frac{t4^H}{1024M_AH^4}
-\frac{\Gamma_A}{2A}Ht.
\tag{10.1}
\]

For all sufficiently large \(m\), (10.1) is at least \(\underline E_m\)
from (0.13).  Since \(B_A\ge0\),

\[
\mathcal E_A^{\rm red}(G_m)\ge\underline E_m.
\tag{10.2}
\]

Fix \(D_A>0\), put \(g_A=D_AHt/n\), and suppose the desired adaptive gain
fails at \(G_m\):

\[
G^{\rm red}(G_m)\le g_A.
\tag{10.3}
\]

Because \(4^H\) dominates every power of \(m\), eventually

\[
T_ng_A\le\frac{n-1}{8}\underline E_m,
\qquad
\mathcal E_A^{\rm red}(G_m)>g_A.
\tag{10.4}
\]

The definition of \(s_m\) gives

\[
\frac{s_m}{2}WD_{m,H}
\le\frac{n-1}{8}\underline E_m.
\tag{10.5}
\]

Insert (10.2)--(10.5) into (0.11).  The numerator is at least
\(3(n-1)\mathcal E_A^{\rm red}(G_m)/4\), while its denominator is at most
\(\mathcal E_A^{\rm red}(G_m)\).  Hence

\[
\boxed{k_{s_m}(G_m)\ge\left\lceil\frac{3(n-1)}4\right\rceil.}
\tag{10.6}
\]

After conjugating with the prescribed cell if necessary, its native MSW
transposition matching is

\[
\mathcal N_m=
\{(2u+2\ \ 2u+3):0\le u\le m-2\},
\qquad |\mathcal N_m|=m-1=\frac{n-3}{2}.
\]

Subtracting all of these colours from (10.6) leaves at least

\[
\boxed{\left\lceil\frac{n+3}{4}\right\rceil}
\tag{10.7}
\]

nonnative giant colours.

The large components counted for different transpositions are distinct as
overlay-component objects; no row-disjointness across colours is asserted.

The floor-sensitive asymptotic

\[
D_{m,H}\sim I_Am^{5/2}
\]

and \(t=W/n\) give (0.14).  Thus the alternative to the adaptive gain is
not a bounded-packet phenomenon: it requires linear-many genuinely fresh
overlays with exponentially large components.

## 11. Growing-harmonic amplification: a fixed-\(A\) constructive descent theorem

The coefficient \(4(n-1)\) in (5.1) uses only the lowest retained harmonic.
Genuine same-row chronology gives a stronger statement after uniformly
removing all low growing degrees.

Fix

\[
0<\gamma<\log4,
\qquad
J=\left\lfloor\frac{\gamma H}{\log(108m)}\right\rfloor,
\qquad
\Lambda=(J+1)(n-J).
\tag{11.1}
\]

Put

\[
\mathcal H_J(F)=
\sum_{q\le H}\sum_{j>J}
\frac{\|P_{q,j}f_q\|_2^2}{c_q},
\qquad
U_{m,\gamma}=\frac{tH^3}{n}e^{\gamma H}.
\tag{11.2}
\]

Let \(\mathcal L_J^T(F)=\mathcal E_A^{\rm red}(F)-\mathcal H_J(F)\).
Explicitly, this is the mass in \(2\le j\le J\) with the shallow sector
\((q\le Q_0,j=2)\) omitted.  It is nonnegative and is bounded by the
larger full low band in (11.3).

The exact run-cap envelope from the same physical rows gives, uniformly for
every exact factor,

\[
\sum_{q\le H}\sum_{2\le j\le J}
\frac{\|P_{q,j}f_q\|_2^2}{c_q}
\le U_{m,\gamma}.
\tag{11.3}
\]

For completeness, the input is the literal row identity

\[
D_Xf_q=\ell_{q,j}-\sum_C\min\{q,g_C(X)\},
\]

followed by its exact run-cap interval and the rank-\(r_q\) inclusion
singular value \(\binom{n-2j}{m-q-j}\).  It gives

\[
\frac1{c_q}\|P_{q,j}f_q\|_2^2
\le\frac{q^2t}{2n}(108m)^j.
\]

Summing \(q\le H,j\le J\) proves (11.3).  Thus (11.3) is genuine
same-row chronology, not an arbitrary harmonic truncation assumption.

For a transposition \(\tau\), define the high-degree cell quantities

\[
A_\tau^{>J}=
\sum_{q\le H}\sum_{j>J}\frac1{c_q}
\left\|\sum_KP_{q,j}d_{K,q}\right\|_2^2,
\]

\[
V_\tau^{>J}=
\sum_K\sum_{q\le H}\sum_{j>J}
\frac{\|P_{q,j}d_{K,q}\|_2^2}{c_q},
\tag{11.4}
\]

and recall the physical row capacity

\[
\mathscr R_{\tau,H}(F)=
\sum_{q\le H}\frac1{c_q}
\sum_{C\in F}\|w_{C,q}-\tau w_{C,q}\|_2^2.
\]

Let

\[
k_s^{\rm eff}(F)=
\#\{\tau:V_\tau^{>J}>s\mathscr R_{\tau,H}(F)\}.
\]

Since a component-size bound \(s_\tau\le s\) implies the opposite
inequality by Cauchy--Schwarz,

\[
k_s(F)\ge k_s^{\rm eff}(F).
\]

### Theorem 11.1 (growing-harmonic adaptive reduced descent)

For every fixed \(A>0\), \(0<\gamma<\log4\), all sufficiently large
\(m\), every exact factor \(F\), every integer \(s\ge0\), and
\(k=k_s^{\rm eff}(F)<T_n\),

\[
\boxed{
G^{\rm red}(F)\ge
\max\left\{0,
\frac{(\Lambda/2-k)\mathcal H_J(F)
-\frac{s}{2}WD_{m,H}}
{T_n-k}
-U_{m,\gamma}
\right\}.}
\tag{11.5}
\]

Consequently, if \(g\ge0\), \(G^{\rm red}(F)\le g\), and
\(\mathcal H_J(F)>U_{m,\gamma}+g\), then

\[
\boxed{
k_s^{\rm eff}(F)\ge
\left\lceil
\frac{\frac\Lambda2\mathcal H_J(F)
-\frac{s}{2}WD_{m,H}-T_n(U_{m,\gamma}+g)}
{\mathcal H_J(F)-U_{m,\gamma}-g}
\right\rceil.}
\tag{11.6}
\]

#### Proof

The high-degree Johnson eigenvalues give

\[
\sum_\tau A_\tau^{>J}
\ge2\Lambda\mathcal H_J(F),
\qquad
A_\tau^{>J}\le4\mathcal H_J(F).
\tag{11.7}
\]

For a colour outside the effective shield set,

\[
V_\tau^{>J}\le s\mathscr R_{\tau,H}(F).
\]

The retained low-degree part \(\mathcal L_J^T\) is nonnegative and, by
(11.3), is at most \(U_{m,\gamma}\) at every literal child.  The maximum
gain is at least the fair-sign expected gain.  Averaging the common
component signs in this cell therefore gives

\[
G_\tau^{\rm red}(F)
\ge\frac14(A_\tau^{>J}-V_\tau^{>J})-U_{m,\gamma}.
\tag{11.8}
\]

After removing the \(k\) effective colours from (11.7), summing (11.8), and
using \(\sum_\tau\mathscr R_{\tau,H}=2WD_{m,H}\), we obtain

\[
\sum_{\tau\notin\mathcal B_s^{\rm eff}}G_\tau^{\rm red}
\ge
(\Lambda/2-k)\mathcal H_J
-\frac{s}{2}WD_{m,H}
-(T_n-k)U_{m,\gamma}.
\]

The maximum is at least the average, and the empty cut has gain zero.  This
proves (11.5).  Under \(G^{\rm red}\le g\), compare the last display with
\((T_n-k)g\) and rearrange.  Since the denominator is positive, integrality
of \(k\) proves (11.6).  When \(k=T_n\), (11.6) remains true directly
(and is vacuous for descent), because \(\Lambda/2<T_n\). \(\square\)

The theorem is constructive at the exact fixed-\(A\) level: whenever the
right side of (11.5) is positive, one of the finitely many freshly computed
transposition cells contains a literal complete-component signing with at
least that reduced gain.  No fractional or separately chosen depthwise signs
occur.

For the high exact MSW factor of Section 10, let

\[
E_m^*=\frac{t4^H}{2048M_AH^4},
\qquad
s_m^*=\left\lfloor
\frac{\Lambda E_m^*}{4WD_{m,H}}
\right\rfloor.
\tag{11.9}
\]

If \(L_m=t4^H/(1024M_AH^4)=2E_m^*\), then the full centered mass is at
least \(L_m\), while (11.3) bounds its degrees \(2\le j\le J\) by
\(U_{m,\gamma}=o(E_m^*)\).  Hence

\[
\mathcal H_J(G_m)
\ge L_m-U_{m,\gamma}
\ge E_m^*
\]

for all sufficiently large \(m\).  If
\(G^{\rm red}(G_m)\le D_AHt/n\), (11.6) yields

\[
\varepsilon_m=
\frac{T_n(U_{m,\gamma}+D_AHt/n)}{E_m^*}
\longrightarrow0
\]

and

\[
\boxed{
k_{s_m^*}^{\rm eff}(G_m)
\ge
\left\lceil\frac{3\Lambda}{8}-\varepsilon_m\right\rceil.}
\tag{11.10}
\]

Here

\[
\boxed{
s_m^*\sim
\frac{\gamma4^H}
{8192M_AI_AH^3m^{5/2}\log(108m)},
\qquad
k_{s_m^*}^{\rm eff}
\ge
\left(\frac{3\gamma A}{4}+o_{A,\gamma}(1)\right)
\frac{m^{3/2}}{\log(108m)}.}
\tag{11.11}
\]

Thus failure of constructive reduced descent on the high literal factor
requires not merely linear-many giant overlays, but a superlinear family of
fresh nonnative colours whose growing-harmonic component variance exceeds an
exponential multiple of their entire physical row-displacement capacity.
Indeed, subtracting all \(m-1\) native colours changes the asymptotic in
(11.11) only by a lower-order term.  Connected overlays remain compatible
with this conclusion.

## 12. Fixed-colour giant and connected no-go with literal chronology

The giant alternative cannot be closed one colour at a time, even if the
entire common-row tail representation is imposed.

### Theorem 12.1 (a giant literal component need not yield descent)

Let \(\tau_0=(2\ 3)\), and let \(\mathscr X_m\) be the full intrinsic MSW
\(\tau_0\)-cell.  Every vertex \(F\in\mathscr X_m\) satisfies

\[
\boxed{
\mathcal E_A^{\rm red}(F)
\ge
\frac{t4^H}{1024M_AH^4}
-\frac{\Gamma_A}{2}Q_0^4t
\ge E_m^*}
\tag{12.1}
\]

for all sufficiently large \(m\).  The first inequality combines the
private-pair full-floor lower bound, valid at every cell vertex, with the
universal same-row shallow \(E_2\) mass bound.

The exact \(\tau_0\)-hierarchy has one top component with old-shore size

\[
\boxed{
s_m^{\rm top}
=\operatorname{Cat}_{m-2}+\operatorname{Cat}_{m-1},
\qquad
\frac{s_m^{\rm top}}t
=\frac{(m+1)(5m-6)}{4(2m-1)(2m-3)}
>\frac5{16}.}
\tag{12.2}
\]

Choose \(F_m^*\) minimizing \(\mathcal Q_A^{\rm red}\) on the finite cell.
Component persistence makes every complete \(\tau_0\)-component signing
another vertex of the same cell.  Therefore

\[
\boxed{
G_{\tau_0}^{\rm red}(F_m^*)=0,
\qquad
\mathcal E_A^{\rm red}(F_m^*)\ge E_m^*,}
\tag{12.3}
\]

although its overlay contains the component (12.2).  Every row is literal,
and this top-component effect satisfies, for every \(X,q\),

\[
D_Xd_{K,q}
=\sum_{C\in L_K}
[(g_C(X)-q)_+-(g_C(\tau_0X)-q)_+].
\tag{12.4}
\]

Thus size, \(\tau\)-invariant middle support, and the full one-component
same-row run-tail data do not force a productive cut at a prescribed colour.

### Theorem 12.2 (a connected literal overlay can be flat at high energy)

Let \(F_m^0\) be the canonical MSW vertex (hence a vertex of
\(\mathscr X_m\)) and \(\sigma=(1\ 2)\).  The proved MSW path-owner
connectivity theorem says that its
owner-row quotient is connected for every \(m\).  Each old row is also
joined to its \(\sigma\)-image by a \(\sigma\)-fixed middle root, so this
quotient connectivity lifts to one connected bipartite ownership overlay:
an owner-quotient edge \(x y\) is a middle root giving the bipartite edge
from old \(x\) to new \(\sigma y\), while the fixed-root edge joins old
\(x\) to new \(\sigma x\).  Quotient paths therefore connect all old rows,
and every new row attaches.
Hence the cell has only the two antipodal factors \(F_m^0\) and
\(\sigma F_m^0\).  Permutation invariance of the reduced seminorm gives

\[
\boxed{
G_\sigma^{\rm red}(F_m^0)=0,
\qquad
\mathcal E_A^{\rm red}(F_m^0)\ge E_m^*.}
\tag{12.5}
\]

The unique component has all \(t\) old-shore rows.  By conjugation, for
every transposition prescribed in advance there is a high literal exact
factor with a connected, flat overlay for that colour.

Theorems 12.1--12.2 do not refute the adaptive gate: a different
transposition may be productive at the same factor.  They prove that the
last theorem must be genuinely cross-transposition.  No implication from
these one-colour data to a productive cut in the same cell can close
constant one; any successful use of a selected giant component, its
connectedness, or its literal common-\(q\) run tails must compare genuinely
different transpositions.

## 13. Exact proved and conditional boundary

### Proved

1. The three C reports have the corrected audit verdicts in Sections 1--3.
2. Aggregate reversal extends exactly to the shallow-\(E_2\)-deleted
   objective, with the complete integer-floor baseline retained.
3. The adaptive reduced-gain lower bounds (0.8) and (0.10) hold for every
   exact factor, every fixed \(A>0\), and all sufficiently large \(m\).
4. The integer chronology improvement (6.5) and arbitrary-component
   constructive descent formula (6.8) are exact; they replace component
   Cauchy by \(\rho_q(k)=k-\lceil k/(q+1)\rceil\).
5. Failure of a gain bound \(g\) forces the exact giant-shield lower bound
   (0.11).
6. The literal Johnson-Lipschitz fork, Theorem 9.1, proves that a genuine
   realization of the decorated ideal would refute the reduced gate; hence
   excluding it is a necessary chronology theorem.
7. The chronological tail packets (9.5)--(9.13) are exact necessary
   conditions for that literal realization.
8. The growing-harmonic fixed-\(A\) descent theorem (11.5) is exact.  On the
   high genuine MSW cell, failure of the target \(D_AHt/n\) forces the
   superlinear active-shield family (11.10)--(11.11).
9. The common-row component chronology (8.1)--(8.4), and its sharp scalar
   limitations in Theorem 8.1, are exact and absent from the decorated Gram
   obstruction.

### Not proved

1. Giant or connected fresh overlays are not excluded.
2. No high-energy exact factor local for every transposition is constructed.
3. The decorated Gram construction is not a literal lower-shadow factor and
   supplies no counterexample to the reduced gate.
4. Equations (8.1)--(8.4) have not yet been converted into a positive Gram
   cut for a giant component.
5. No active-row no-recycling theorem excludes the superlinear shield family
   in (11.10).
6. The packet inequalities in Theorem 9.2 do not yet contradict a positive-
   energy \(0/1/2\) load distribution.

The surviving theorem is therefore a **chronological giant-shield
exclusion**: use the common run-tail representation (8.2), together with
middle ownership-component connectedness, to show that the active giant
alternative in (11.6) cannot persist whenever
\(\mathcal Q_A^{\rm red}>K_AHt\).  Proving that statement would supply the
adaptive transposition and complete the reduced local-minimum gate.  An
equivalent obstruction branch is to rule out simultaneous realization of
the Lipschitz tail packets (9.5)--(9.13) at positive-density floor energy.
No claim of \(LM_A\) or of constant one is made here.
