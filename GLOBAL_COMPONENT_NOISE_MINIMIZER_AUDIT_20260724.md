# Audit of the global component-noise minimizer reduction

Date: 2026-07-24

Audited source: `GLOBAL_COMPONENT_NOISE_MINIMIZER_RAW_20260724.md`.

The saved source compresses and renumbers the main-thread displays as
\((1)\)--\((9)\).  The reconstruction below labels the full submitted chain
\((18)\)--\((29)\), as requested.

## Verdict

**MATERIAL CORRECTION REQUIRED.**

The following parts of the proposal are exact after their missing
hypotheses and definitions are supplied:

1. the universal integer variance floor \(V_q^{\min}\);
2. the identity \(V_q-V_q^{\min}=Q_q\) and the inequality
   \(2O_q\le Q_q\) for the standard balanced overload \(O_q\);
3. exact factor preservation under complete ownership-component side
   choices;
4. the fair switching expectation, including its factor \(1/4\);
5. the averaged inequality forced by global minimality.

The decisive spectral step is not sharp enough in the raw note.  The bound

\[
\sum_\tau\|f-\tau f\|_2^2\ge 2n\|f-\bar f\mathbf1\|_2^2
\]

is valid for an arbitrary rank-slice function when unordered coordinate
transpositions are counted once.  It is not the exact applicable bound for
an exact-factor histogram.  Exact factors have fixed point margins, so their
centered depth histograms contain neither Johnson degree \(0\) nor degree
\(1\).  The applicable sharp spectral factor is therefore

\[
\boxed{
\sum_\tau\|f_q-\tau f_q\|_2^2
\ge 4(n-1)\|f_q\|_2^2.}
\]

Consequently the raw final criterion

\[
R_H\le 2n\sum_{q\le H}\frac{V_q^{\min}}{c_q}+o(nW)
\]

is formally sufficient if one deliberately uses the weaker generic gap,
but it is asymptotically impossible in every fixed nontrivial Gaussian
window \(H=\lceil A\sqrt m\rceil\).  The spectrally compatible repaired
sufficient criterion is

\[
\boxed{
R_H\le 4(n-1)\sum_{q\le H}\frac{V_q^{\min}}{c_q}+o(nW).}
\tag{29*}
\]

Even \((29*)\) is unproved.  It is a new minimizer-only sufficient gate, not an
equivalent formulation of RFEN, the positive-cut lemma, or the stationary
class gate.

The raw wildcard degree-counting objection also does not survive as stated.
Degree double counting is compatible with the natural marker construction;
what fails is only the use of fictitious marker-only completion edges as if
they were physical wreaths.

## 1. Standalone hypotheses and notation

Assume

\[
n=2m+1,\qquad m\ge2,\qquad W=\binom nm,
\qquad N_q=\binom n{m-q}.
\]

For the fixed Gaussian window one has

\[
1\le q\le H_A:=\lceil A\sqrt m\rceil\le m-2
\]

for all sufficiently large \(m\).  The same finite calculations apply to
any admissible \(H\le m-2\).  The terminal rank \(m-q=1\), if included, has
identically constant exact-factor histogram and can simply be discarded.

Every norm below is the unnormalized counting \(\ell_2\)-norm.  Every sum
over transpositions is over the \(\binom n2\) **unordered** coordinate
transpositions, each counted once.

An exact factor \(F\) contains

\[
|F|=\frac Wn=\operatorname{Cat}_m
\]

unoriented wreaths.  For \(r=m-q\), let \(\mu_q(F,S)\) count the wreaths of
\(F\) in which the \(r\)-set \(S\) is a cyclic interval.  Then

\[
\sum_{S\in\binom{[n]}r}\mu_q(F,S)=W.
\]

Write

\[
a_q:=\frac W{N_q}=c_q+\theta_q,
\qquad c_q=\lfloor a_q\rfloor,
\qquad 0\le\theta_q<1,
\tag{18}
\]

and

\[
t_q:=W-c_qN_q=N_q\theta_q\in\{0,1,\ldots,N_q-1\}.
\tag{19}
\]

The raw source uses \(O_q\) without defining it.  The only definition under
which its stated inequality is the standard audited one is

\[
\begin{aligned}
D_q^-&:=\sum_S(c_q-\mu_q(S))_+,\\
D_q^+&:=\sum_S(\mu_q(S)-c_q-1)_+,\\
O_q&:=\max\{D_q^-,D_q^+\}.
\end{aligned}
\tag{20}
\]

In particular, \(O_q\) is not the naive quantity
\(\sum_S(\mu_q(S)-c_q)_+\), which is positive even on a perfectly balanced
\(c_q/c_q+1\) profile.

Equivalently, \(O_q\) is the minimum half-\(\ell_1\) distance from
\(\mu_q\) to a balanced quota vector having exactly \(t_q\) entries
\(c_q+1\) and all other entries \(c_q\).  To see this, put the high quotas
on the \(t_q\) largest loads and let \(h\) be the number of loads exceeding
\(c_q\).  The mass identity is

\[
t_q=h+D_q^+-D_q^-.
\]

If \(h\ge t_q\), the minimum half-distance is
\(D_q^++h-t_q=D_q^-\).  If \(h\le t_q\), it is \(D_q^+\).
Thus the minimum is \(\max\{D_q^-,D_q^+\}\).

## 2. The integer floor \(V_q^{\min}\) and \(2O_q\)

Define

\[
V_q(F):=\sum_S(\mu_q(F,S)-a_q)^2.
\tag{21}
\]

### Proposition 2.1 (universal integer variance floor)

Among all nonnegative integer vectors \(z=(z_S)_{S\in\binom{[n]}r}\) with
\(\sum_Sz_S=W\), the minimum of

\[
\sum_S(z_S-a_q)^2
\]

is attained precisely by vectors with \(N_q-t_q\) coordinates equal to
\(c_q\) and \(t_q\) coordinates equal to \(c_q+1\).  Hence

\[
\begin{aligned}
V_q^{\min}
&=(N_q-t_q)\theta_q^2+t_q(1-\theta_q)^2\\
&=N_q\theta_q(1-\theta_q).
\end{aligned}
\tag{22}
\]

#### Proof

If two integer coordinates satisfy \(z_T-z_S\ge2\), replace them by
\(z_S+1,z_T-1\).  The change in the sum of squares about \(a_q\) is

\[
(z_S+1-a_q)^2+(z_T-1-a_q)^2
-(z_S-a_q)^2-(z_T-a_q)^2
=-2(z_T-z_S-1)<0.
\]

Iteration terminates only when every two coordinates differ by at most one.
The fixed total then forces the displayed numbers of \(c_q\)'s and
\(c_q+1\)'s.  Substituting \(t_q=N_q\theta_q\) gives the second equality in
(22).  Conversely such a vector admits no improving transfer.  ∎

This is an unconstrained integer-mass floor.  It is a lower bound for every
exact-factor histogram; the proposition does not say that every balanced
floor vector is realizable by an exact factor.

Put \(d_S=\mu_q(S)-c_q\).  Since

\[
\sum_Sd_S=t_q=N_q\theta_q,
\]

direct expansion gives the exact identity

\[
\boxed{
V_q(F)-V_q^{\min}
=\sum_Sd_S(d_S-1)
=:Q_q(F).}
\tag{23}
\]

For every integer \(d\),

\[
d(d-1)\ge2\bigl((-d)_++(d-1)_+\bigr).
\]

Therefore the proposal's overload inequality is valid, and in fact the
slightly stronger statement is

\[
\boxed{
V_q(F)-V_q^{\min}=Q_q(F)
\ge2(D_q^-+D_q^+)\ge2O_q(F).}
\tag{24}
\]

Thus the raw objective

\[
\Phi_H(F):=\sum_{q\le H}\frac{V_q(F)-V_q^{\min}}{c_q}
\tag{25}
\]

is exactly the previously audited **full** floor energy
\(\mathcal Q_H(F)=2\Psi_H(F)\), not the half-normalized energy
\(\Psi_H\).

## 3. Exact ownership-component switching

Fix an unordered coordinate transposition \(\tau\).  For \(m\ge2\), the
previously audited disjointness lemma gives

\[
F\cap\tau F=\varnothing.
\]

For completeness, if a wreath \(C\in F\) were also \(\tau D\) for
\(D\in F\), one of the two open cyclic arcs between the transposed labels
has at least \(m\) vertices, so \(D\) has an \(m\)-interval avoiding both
labels.  That interval is fixed by \(\tau\) and is also an interval of
\(\tau D\).
Exactness would force \(C=D\).  But the stabilizer of an unoriented odd
\(n\)-cycle contains no single transposition when \(n\ge5\), a
contradiction.

Form the bipartite ownership multigraph with left vertices \(F\), right
vertices \(\tau F\), and one edge labelled by each middle \(m\)-set, joining
its unique owners on the two sides.  Every wreath owns exactly \(n\) middle
sets, so this graph is \(n\)-regular on both sides.  In each connected
component \(C\), degree counting gives the same number \(s_C\) of wreaths on
the left and right.

Every middle-set edge of \(C\) has one endpoint on each complete side.
Selecting either the whole left side or the whole right side therefore
covers every middle set of \(C\) exactly once.  Independent complete-side
choices across components give an integral exact factor.  Partial side
choices within a component are not licensed by this argument.

Let \(u_{q,C}\) and \(w_{q,C}\) be the depth-\(q\) histograms of the left and
right **sides**, respectively.  They are not histograms of the union of both
sides.  Then

\[
\sum_Cu_{q,C}=\mu_q(F),
\qquad
\sum_Cw_{q,C}=\mu_q(\tau F)=\tau\mu_q(F).
\]

The fixed \(m\)-interval used in the disjointness proof gives, for every
left wreath \(D\), an ownership edge \(D\!-\!\tau D\).  Hence \(\tau\)
stabilizes every ownership component setwise and exchanges its two sides.
Consequently \(w_{q,C}=\tau u_{q,C}\) after consistent component indexing.

## 4. Fair switching expectation and the minimizer inequality

Let independent Rademacher signs \(\varepsilon_C\) encode the complete-side
choices and put

\[
b_{q,C}:=\frac{u_{q,C}+w_{q,C}}2,
\qquad
d_{q,C}:=u_{q,C}-w_{q,C}.
\]

The switched histogram is

\[
\mu_q(F')
=\sum_C\left(b_{q,C}+\frac{\varepsilon_C}{2}d_{q,C}\right).
\]

Since the signs are independent, centered, and have variance one, all cross
terms vanish.  Thus

\[
\boxed{
\mathbb EV_q(F')
=\left\|\frac{\mu_q(F)+\tau\mu_q(F)}2-a_q\mathbf1\right\|_2^2
+\frac14\sum_C\|u_{q,C}-w_{q,C}\|_2^2.}
\tag{26}
\]

For the original factor, set

\[
h_q:=\frac{\mu_q+\tau\mu_q}{2}-a_q\mathbf1,
\qquad
g_q:=\mu_q-\tau\mu_q.
\]

Here \(h_q\) is \(\tau\)-invariant and \(g_q\) is \(\tau\)-anti-invariant, so
they are orthogonal.  Since \(\mu_q-a_q\mathbf1=h_q+g_q/2\),

\[
\boxed{
V_q(F)=\left\|\frac{\mu_q(F)+\tau\mu_q(F)}2-a_q\mathbf1\right\|_2^2
+\frac14\|\mu_q(F)-\tau\mu_q(F)\|_2^2.}
\tag{27}
\]

Now choose, for the same window \(H\), a global minimizer \(F=F_{m,H}\) of
\(\Phi_H\) over the finite exact-factor space.  Every complete-side child is
an exact factor, hence pointwise

\[
\Phi_H(F')\ge\Phi_H(F).
\]

Take the fair expectation, use (26)--(27), and cancel the factor-independent
\(V_q^{\min}\).  For every transposition \(\tau\),

\[
\boxed{
\sum_{q\le H}\frac{\|\mu_q(F)-\tau\mu_q(F)\|_2^2}{c_q}
\le
\sum_{C\in\mathcal C_\tau(F)}\sum_{q\le H}
\frac{\|u_{q,C}-w_{q,C}\|_2^2}{c_q}.}
\tag{28}
\]

The sign and all factors in (26)--(28) are correct.

Two scope points matter.

1. \(F_{m,H}\) must minimize the same \(H\)-window objective used in
   \(R_H\).  A noise bound at an arbitrary factor cannot be inserted into
   (28).
2. Global minimality is stronger than needed for (28).  It suffices that
   \(F\) have no negative **fair averaged** drift in any \(\tau\)-cell.
   Conversely, (28) is not equivalent to deterministic cut-locality: one
   decreasing correlated signing can coexist with a nonnegative fair
   average.

## 5. Exact Johnson factor in the all-transposition sum

Let \(r=m-q\le m\), let

\[
f_q:=\mu_q-a_q\mathbf1,
\qquad V_q=\|f_q\|_2^2,
\]

and let \(L_{J(n,r)}\) be the combinatorial Johnson Laplacian.  Each Johnson
edge \(S\sim T\) is generated by a unique coordinate transposition.  For
that transposition, the counting norm sums the squared difference once from
each endpoint.  Hence the exact identity is

\[
\sum_{\tau}\|f-\tau f\|_2^2
=2\sum_{\{S,T\}\in E(J(n,r))}(f(S)-f(T))^2
=2\langle f,L_{J(n,r)}f\rangle.
\]

The Johnson Laplacian eigenvalue on degree \(j\) is

\[
\lambda_j=j(n-j+1),
\qquad 0\le j\le r.
\]

Thus the raw generic statement

\[
\sum_\tau\|f-\tau f\|_2^2
\ge2n\|f-\bar f\mathbf1\|_2^2
\]

is valid and sharp on Johnson degree \(1\).  Ordered pairs \((a,b)\) would
count every transposition twice and double this constant.

The exact-factor profile has additional structure.  Each wreath has exactly
\(r\) cyclic \(r\)-intervals through a fixed coordinate \(x\), so

\[
\sum_{S\ni x}\mu_q(F,S)
=r|F|=\frac{rW}{n}.
\]

The constant profile has the same point margin:

\[
a_q\binom{n-1}{r-1}
=\frac W{N_q}\frac r nN_q
=\frac{rW}{n}.
\]

Therefore every point-star sum of \(f_q\) is zero.  The point-incidence map
is nonzero exactly on Johnson degrees \(0\) and \(1\), so

\[
f_q\in\bigoplus_{j\ge2}E_j.
\]

Consequently the exact applicable identity and bound are

\[
\boxed{
\begin{aligned}
\sum_\tau\|f_q-\tau f_q\|_2^2
&=2\sum_{j\ge2}j(n-j+1)\|f_q^{(j)}\|_2^2\\
&\ge4(n-1)\|f_q\|_2^2.
\end{aligned}}
\tag{29a}
\]

The factor \(4(n-1)\) is sharp on the \(E_2\) subspace of the
point-incidence kernel.  This is a representation-theoretic sharpness
statement; it does not assert that an exact-factor histogram attains
equality.
Every individual component difference \(u_{q,C}-w_{q,C}\) also has zero
total and zero point margins, because the two component sides contain the
same number of wreaths.  This harmonic fact does not, by itself, upper-bound
the component-noise norm.

## 6. Aggregate ledger and the corrected \(R_H\) criterion

Define

\[
\begin{aligned}
B_H&:=\sum_{q\le H}\frac{V_q^{\min}}{c_q},\\
S_H&:=\sum_{q\le H}\frac{V_q}{c_q}=B_H+\Phi_H(F),\\
D_H&:=\sum_\tau\sum_{q\le H}
\frac{\|\mu_q-\tau\mu_q\|_2^2}{c_q},\\
R_H&:=\sum_\tau\sum_{C\in\mathcal C_\tau(F)}\sum_{q\le H}
\frac{\|u_{q,C}-w_{q,C}\|_2^2}{c_q},\\
P_H&:=\sum_{q\le H}\frac{O_q(F)}{c_q}.
\end{aligned}
\]

Summing (28) gives \(D_H\le R_H\).  Equation (29a) gives

\[
R_H\ge D_H\ge4(n-1)S_H
=4(n-1)(B_H+\Phi_H(F)).
\tag{29b}
\]

Combining (24) with (29b) yields the sharpened overload estimate

\[
\boxed{
P_H
\le\frac{\Phi_H(F)}2
\le\frac{R_H}{8(n-1)}-\frac{B_H}{2}.}
\tag{29c}
\]

If one instead uses only the generic \(2n\) gap, one obtains the raw bound

\[
P_H\le\frac{R_H}{4n}-\frac{B_H}{2}.
\]

That raw inequality is valid but deliberately weak.  Plugging in the raw
criterion

\[
R_H\le2nB_H+o(nW)
\tag{29}
\]

would formally give \(P_H=o(W)\).  The problem is that the raw (29) is
incompatible with the stronger unavoidable lower bound (29b) on the
intended window.

### 6.1 The raw criterion is impossible on a fixed Gaussian window

Uniformly for \(q\le A\sqrt m\),

\[
a_q=\frac{W}{N_q}
=\exp\left(\frac{q(q+1)}m+O_A(m^{-1/2})\right).
\]

For \(q=x\sqrt m+O(1)\), this tends to \(e^{x^2}\).  Define

\[
g(y):=
\frac{\{y\}(1-\{y\})}{y\lfloor y\rfloor},
\]

with value \(0\) at the positive integers.  The apparent jumps of the floor
are killed by the numerator, so \(g\) is continuous on every compact
subinterval of \([1,\infty)\).  Since

\[
\frac{V_q^{\min}}{c_qW}
=\frac{\theta_q(1-\theta_q)}{c_qa_q}
=g(a_q),
\]

the Riemann sum gives, for \(H_A=\lceil A\sqrt m\rceil\),

\[
\boxed{
\frac{B_{H_A}}{W\sqrt m}
\longrightarrow
\kappa_A:=\int_0^A
\frac{\{e^{x^2}\}(1-\{e^{x^2}\})}
{e^{x^2}\lfloor e^{x^2}\rfloor}\,dx>0.}
\tag{29d}
\]

The integral is positive for every fixed \(A>0\), because its integrand is
positive except at the discrete points where \(e^{x^2}\) is an integer.

But (29b) and the raw (29) together would imply

\[
(4(n-1)-2n)B_H=(2n-4)B_H\le o(nW).
\]

By (29d), the left side is
\(\Theta_A(nW\sqrt m)\), a contradiction.  Thus the literal raw condition
is not merely stronger than necessary: it is asymptotically infeasible for
the stated fixed Gaussian window.  For an arbitrary much shorter sequence
of windows it at least forces \(B_H=o(W)\); the Gaussian-window conclusion
is the scope relevant to fixed-window MWB.

### 6.2 Spectrally compatible repaired criterion

The natural factor-specific replacement is

\[
\boxed{
R_{H_A}(F_{m,A})
\le4(n-1)B_{H_A}+o_A(nW),}
\tag{29*}
\]

where, for every \(m\), \(F_{m,A}\) is a global minimizer of the same
\(H_A\)-window objective.  Equation (29c) then gives

\[
P_{H_A}=o_A(W).
\]

In fact it gives the stronger conclusion

\[
\Phi_{H_A}(F_{m,A})=o_A(W).
\]

No estimate in the raw note proves \((29*)\).

### 6.3 Exact meaning of \((29*)\) at a global minimizer

At a global minimizer all three terms in

\[
\boxed{
\begin{aligned}
R_H-4(n-1)B_H
={}&(R_H-D_H)\\
&+\bigl(D_H-4(n-1)S_H\bigr)\\
&+4(n-1)\Phi_H(F)
\end{aligned}}
\tag{29e}
\]

are nonnegative.  More explicitly,

\[
R_H-D_H
=4\sum_\tau
\bigl(\mathbb E_{\varepsilon}\Phi_H(F_{\tau,\varepsilon})
-\Phi_H(F)\bigr)\ge0,
\]

and

\[
D_H-4(n-1)S_H
=2\sum_{q\le H}\frac1{c_q}
\sum_{j\ge3}
\bigl(j(n-j+1)-2(n-1)\bigr)\|f_q^{(j)}\|_2^2\ge0.
\]

Therefore \((29*)\) is equivalent, at the selected global minimizer, to the
simultaneous conditions

\[
\Phi_H(F)=o(W),
\]

\[
R_H-D_H=o(nW),
\]

and

\[
D_H-4(n-1)S_H=o(nW).
\]

It demands not only a low-energy minimizer, but also negligible aggregate
fair-switch drift and negligible Johnson spectral excess above degree \(2\).
It is therefore strictly stronger than the conclusion
“the global minimum is \(o(W)\)” as an analytic condition, although no
strict separation has been constructed inside the exact-factor system.

## 7. Relation to the previously audited gates

The literal raw (29) is infeasible on the relevant window, so it is not
a meaningful reformulation of any previous gate.  The comparison below is
with the repaired condition \((29*)\).

| Gate | Quantity and quantifier | Precise relation to \((29*)\) |
|---|---|---|
| Minimizer-only annealed RFEN | Propagated rankwise restitution along an \(O(n)\)-step iid-uniform word frozen before component signs and then averaged over that word, with ownership components recomputed at successive states | No proved implication either way. RFEN can exploit suffix filtering of large early noise; \((29*)\) controls the unpropagated one-step sum over every transposition at one state. Conversely, \((29*)\) proves the desired low minimizer directly but does not establish the RFEN remainder inequality for a word. The original deterministic-word FEN is a separate sufficient hypothesis. |
| Positive-cut/local-minimum lemma \(LM_A\) | Every high-energy factor has a decreasing correlated component signing; equivalently every cut-local minimum is low | No proved implication either way. A global minimizer is automatically cut-local, but \(LM_A\) supplies no upper bound on its fair noise \(R_H\). Condition \((29*)\) says nothing about nonglobal cut-local minima and therefore does not imply \(LM_A\). |
| Stationary-class gate \(SCOV_A\) | Some heat communicating class has low uniform stationary mean/covariance energy | No proved implication either way. Condition \((29*)\) gives one low global minimizer and one-step near-zero drift, not a low mean over its entire class. A low class mean gives a low state but no sharp component-noise bound at that state. |

Thus \((29*)\) is **merely another sufficient condition** for one good exact
factor.  It is not known to be stronger than, weaker than, or equivalent to
RFEN, \(LM_A\), or \(SCOV_A\) under their actual quantifiers.  At a global
minimizer its exact equivalence is the three-term near-equality statement
(29e), not any of those earlier gates.

Conditionally, if \((29*)\) holds for every fixed \(A\), then

\[
\sum_{q\le H_A}\frac{O_q(F_{m,A})}{c_q}=o_A(W).
\]

The previously audited diagonalization then gives MWB.  This last transfer
is imported; neither the raw note nor this audit proves \((29*)\), RFEN,
\(LM_A\), \(SCOV_A\), or MWB.

## 8. Audit of the crude component-size bound

Let \(s_{\tau,C}\) be the number of wreaths on either side of a
\(\tau\)-ownership component.  For every proper nonempty target rank,

\[
\|u_{q,C}\|_1=ns_{\tau,C},
\qquad
\|u_{q,C}\|_\infty\le s_{\tau,C},
\]

because every wreath contributes \(n\) cyclic intervals at that rank and a
fixed proper target occurs at most once in a wreath.  The same bounds hold
for \(w_{q,C}\).  Nonnegativity gives

\[
\begin{aligned}
\|u_{q,C}-w_{q,C}\|_2^2
&=\|u_{q,C}\|_2^2+\|w_{q,C}\|_2^2
-2\langle u_{q,C},w_{q,C}\rangle\\
&\le2n s_{\tau,C}^2.
\end{aligned}
\]

With

\[
\Lambda_H:=\sum_{q\le H}\frac1{c_q},
\]

one obtains the valid crude estimate

\[
\boxed{
R_H\le2n\Lambda_H
\sum_\tau\sum_Cs_{\tau,C}^2.}
\tag{30}
\]

For every \(\tau\),

\[
\sum_Cs_{\tau,C}=|F|=\frac Wn.
\]

Without a maximum-component-size estimate,

\[
\sum_Cs_{\tau,C}^2\le\left(\frac Wn\right)^2,
\]

and therefore

\[
\boxed{
R_H\le(n-1)W^2\Lambda_H.}
\tag{31}
\]

If one knows only that every component has \(s_{\tau,C}\le K\), then

\[
\sum_Cs_{\tau,C}^2\le K\frac Wn
\]

and

\[
\boxed{
R_H\le K n(n-1)W\Lambda_H.}
\tag{32}
\]

For a fixed Gaussian window,

\[
\Lambda_{H_A}=\Theta_A(\sqrt m),
\qquad
4(n-1)B_{H_A}=\Theta_A(nW\sqrt m).
\]

The unrestricted bound (31) loses a factor of order \(W\).  Even the
extreme estimate \(K=1\) in (32) loses a factor of order \(n\), and it gives
no \(o(nW)\) control on the excess above the baseline.  If there are exactly
\(k\) positive-size components and their total side size is \(B_0=W/n\), then

\[
\sum_Cs_C^2\le(B_0-k+1)^2+(k-1).
\]

Thus component count does give a formal bound, but it is not usefully small
unless \(k\) is close to \(B_0\), equivalently unless a giant component is
excluded or the size distribution is controlled.  The raw statement that
crude component estimates are much too large is therefore correct, with
(30)--(32) giving the principal losses.

## 9. Wildcard-marker degree counting

The final raw sentence does not define its marker vertices, candidate
edges, weights, or matching constraints.  Taken literally, its assertion
about equal average weighted degrees is not a valid obstruction.

For any incidence hypergraph in which each hyperedge contains one marker
and \(n\) middle-set vertices, double counting gives

\[
\sum_{y\in Y}\deg(y)=|\mathcal E|,
\qquad
\sum_{S\in X}\deg(S)=n|\mathcal E|.
\]

Thus the **total** degrees are in ratio \(1:n\).  The average degrees are
equal exactly when

\[
|X|=n|Y|.
\]

The natural exact-factor counts satisfy this condition:

\[
|X|=W,
\qquad
|Y|=\frac Wn.
\]

Indeed, let \(\mathscr W\) be the full set of wreath supports and suppose,
by transitivity, that every middle set lies in exactly \(d\) wreaths.  Since
every wreath contains \(n\) middle sets,

\[
n|\mathscr W|=Wd,
\qquad
|\mathscr W|=\frac{Wd}{n}.
\]

Create one hyperedge for every pair \((y,C)\in Y\times\mathscr W\),
consisting of marker \(y\) together with the \(n\) middle sets of wreath
\(C\).  Then

\[
\deg(y)=|\mathscr W|=\frac{Wd}{n}
\]

for every marker, while

\[
\deg(S)=d|Y|=\frac{Wd}{n}
\]

for every middle set.  The two vertex classes therefore have exactly equal
average degrees without any completion edges.  A perfect hypermatching
covers \(W/n\) markers and all \(W\) middle sets; after deleting the markers,
its selected wreaths are exactly an exact factor.  Conversely, assigning
the wreaths of any exact factor bijectively to the markers gives such a
perfect hypermatching.

What survives from the raw objection is narrower.  Markers create no
physical slack: a dummy edge covering only an unmatched marker is not a
wreath and cannot be used as a legal completion edge.  Hence a near-perfect
nibble cannot be finished by fictitious marker-only edges.  That is a
completion/absorption objection, not a degree-counting obstruction to the
natural exact perfect-matching formulation, and it does not rule out
weighted, \(b\)-matching, or structurally restricted marker constructions.

## Final audited status

The exact switching and minimizer algebra survives, but the submitted
spectral constant changes the conclusion qualitatively:

\[
\boxed{
\text{raw }2nB_H\text{ criterion: valid as a formal implication but
Gaussian-window infeasible};
}
\]

\[
\boxed{
\text{correct factor-specific sufficient gate: }
R_H\le4(n-1)B_H+o(nW).
}
\]

The corrected gate remains unproved and is not equivalent to RFEN,
positive-cut, or stationary selection.  Its exact content at a global
minimizer is simultaneous control of the floor energy, aggregate fair heat
drift, and spectral mass above Johnson degree \(2\).
