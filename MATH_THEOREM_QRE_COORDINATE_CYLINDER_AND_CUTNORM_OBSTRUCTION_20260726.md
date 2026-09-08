# QRE at Gaussian depth: the coordinate-cylinder and cut-norm obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let `G_q^-` and `G_q^+` be the maximal lower and upper
allocation-overlap graphs arising from any local rank-matching array,
random or deterministic. Their edges always obey

\[
                         T\subset X\quad(-),
 \qquad                 X\subset U\quad(+).          \tag{0.1}
\]

At

\[
                         q=A\sqrt m+O(1),\qquad A>0, \tag{0.2}
\]

this elementary order relation gives a sharp obstruction to the proposed
spectral and cut-norm proofs of `QRE_A`.

1. Every possible expansion theorem has optimal factor at most

   \[
                          e^{A^2}+o(1).               \tag{0.3}
   \]

   This remains true after arbitrary `o(N_q)` target and `o(W)` owner
   quarantines.
2. Every uniform-marginal fractional inclusion kernel has second singular
   value at least

   \[
                   \sqrt{m-q\over m+q}
                   =1-{A\over\sqrt m}+O(m^{-1}).     \tag{0.4}
   \]

   Hence no constant spectral gap or constant strong `L^2` contraction is
   available.
3. More decisively, inside every safe ordered target/source profile pair
   there are target and owner subfamilies of constant relative density
   with **zero** incidence. Therefore a product-mixing or cut-norm estimate
   of the form proposed in `QRE_A`, uniform over arbitrary subsets inside
   profiles, is false even for the complete ordinary inclusion graph. It
   cannot be repaired by independent local matchings.

This does not refute `QRE_A`: coordinate cylinders have neighborhood ratio
asymptotic to the upper bound (0.3), so they are compatible with every
smaller fixed expansion constant. It does definitively close the
constant-gap spectral and raw product-cut-norm routes. A successful proof
must instead be one-sided and isoperimetric, retaining the monotone
coordinate cylinders rather than trying to mix them away.

## 1. The sharp cylinder upper bound below

Put

\[
 W=\binom{2m}m,
 \qquad
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.                \tag{1.1}
\]

Fix a coordinate `x` and define the lower target cylinder

\[
 \mathcal A_x^-=
 \{T\in\tbinom{[2m]}{m-q}:x\in T\}.                 \tag{1.2}
\]

Every source adjacent to a member of `mathcal A_x^-` contains `x`, by
(0.1). Therefore

\[
 N_{G_q^-}(\mathcal A_x^-)
 \subseteq
 \mathcal B_x^+:=
 \{X\in\tbinom{[2m]}m:x\in X\}.                    \tag{1.3}
\]

The two exact cardinalities are

\[
 |\mathcal A_x^-|={m-q\over2m}N_q,
 \qquad
 |\mathcal B_x^+|={W\over2}.                        \tag{1.4}
\]

Consequently every lower compatibility graph satisfies

\[
 { |N(\mathcal A_x^-)|\over|\mathcal A_x^-|}
 \le {mW\over(m-q)N_q}
 ={W\over N_q}\left(1+{q\over m}+O(q^2/m^2)\right).
                                                               \tag{1.5}
\]

Since

\[
                         {W\over N_q}=e^{A^2+o(1)},  \tag{1.6}
\]

(1.5) proves the lower version of (0.3).

For the upper graph take the complementary cylinder

\[
 \mathcal A_x^+=
 \{U\in\tbinom{[2m]}{m+q}:x\notin U\}.              \tag{1.7}
\]

If `X subset U` and `x notin U`, then `x notin X`. Thus its neighborhood
is contained in the `W/2` middle owners omitting `x`, while

\[
                         |\mathcal A_x^+|
                         ={m-q\over2m}N_q.           \tag{1.8}
\]

The same bound (1.5) follows above.

### Quarantine audit

Let `E_T` and `E_X` be arbitrary deleted target and owner families with

\[
                         |E_T|=o(N_q),\qquad |E_X|=o(W).         \tag{1.9}
\]

For every fixed `x`,

\[
 |\mathcal A_x^\epsilon\setminus E_T|
 ={m-q\over2m}N_q-o(N_q),                            \tag{1.10}
\]

and its surviving neighborhood is still contained in the corresponding
half of the middle layer. Deleting owners can only reduce that
neighborhood. Hence (1.5)--(1.6) remain valid after arbitrary quarantines.
In particular, if `QRE_A` holds with

\[
                         |N(\mathcal A)|
                         \ge(1+\delta_A)|\mathcal A|, \tag{1.11}
\]

then necessarily

\[
                         1+\delta_A\le e^{A^2}+o(1). \tag{1.12}
\]

The Gaussian profile theorem has exactly this leading expansion factor,
so the cylinder obstruction is sharp at the level of constants.

## 2. Universal near-one singular value

Consider any fractional lower inclusion flow which saturates every target
uniformly and has uniform owner load `N_q/W`. After division by its total
mass it defines a coupling `(T,X)` of the uniform measures on

\[
                         \binom{[2m]}{m-q}
 \quad\hbox{and}\quad \binom{[2m]}m,                 \tag{2.1}
\]

supported on `T subset X`.

Fix `x` and put

\[
                         L=\mathbf1_{\{x\in T\}},
 \qquad                 R=\mathbf1_{\{x\in X\}}.    \tag{2.2}
\]

The marginals are

\[
                         \mathbb EL={m-q\over2m}=:p,
 \qquad                 \mathbb ER={1\over2}.       \tag{2.3}
\]

Since `L<=R` pointwise, `LR=L`. Therefore

\[
\begin{aligned}
 \operatorname{Cov}(L,R)&=p-{p\over2}={p\over2},\\
 \operatorname{Var}L&=p(1-p),\\
 \operatorname{Var}R&={1\over4}.
\end{aligned}                                        \tag{2.4}
\]

The correlation is exactly

\[
 \operatorname{Corr}(L,R)
 ={p\over\sqrt{p(1-p)}}
 =\sqrt{m-q\over m+q}.                               \tag{2.5}
\]

Centered and normalized coordinate indicators are legal test vectors for
the conditional expectation operator of the coupling. Hence its second
singular value is at least (2.5), proving (0.4).

For the upper graph use

\[
                         L=\mathbf1_{\{x\notin U\}},
 \qquad                 R=\mathbf1_{\{x\notin X\}}. \tag{2.6}
\]

Again `L<=R`, and the same marginals and calculation apply.

Thus the obstruction is not a defect of one choice of normalization. Any
uniform-marginal fractional kernel supported on the required literal
inclusions has spectral gap at most

\[
                         1-\sqrt{m-q\over m+q}
                         ={A\over\sqrt m}+O(m^{-1}). \tag{2.7}
\]

An expander-mixing argument requiring a constant gap cannot prove
`QRE_A`.

Equivalently, the `chi^2` strong data-processing coefficient is at least

\[
                         {m-q\over m+q}=1-{2A\over\sqrt m}+O(m^{-1}),
                                                               \tag{2.8}
\]

and the relative-entropy contraction coefficient has the same lower bound
under infinitesimal perturbations of the uniform input. Hence a proof based
on a constant strong data-processing contraction is excluded as well. This
does not exclude a one-sided local-LYM entropy argument, which is not a
mixing statement.

## 3. Constant-density zero rectangles inside safe profiles

The stronger obstruction applies directly to the proposed within-profile
cut estimate.

Fix a retained lower ordered profile arc `tau to kappa` in one residual
fibre. In some block `j`, let the target and source `A_j`-half counts be

\[
                         a_j,qquad a'_j=a_j+\alpha_j.             \tag{3.1}
\]

Choose one coordinate `x in A_j` and put

\[
\begin{aligned}
 \mathcal C_T^-&=\{T\in\tau:x\in T\},\\
 \mathcal C_X^-&=\{X\in\kappa:x\notin X\}.
\end{aligned}                                        \tag{3.2}
\]

There is no edge from `mathcal C_T^-` to `mathcal C_X^-`, because every
lower edge is an inclusion. Nevertheless their exact relative densities
inside the two ordered profiles are

\[
 { |\mathcal C_T^-|\over w_T(\tau)}={a_j\over d},
 \qquad
 { |\mathcal C_X^-|\over w_X(\kappa)}=1-{a'_j\over d}.           \tag{3.3}
\]

On the safe two-promotion core,

\[
                         {1\over4}\le{a_j\over d}\le{3\over4},
 \qquad
                         1-{a'_j\over d}\ge{1\over4}-O(d^{-1}). \tag{3.4}
\]

Thus (3.2) is a zero rectangle whose two shores each have constant
relative density. It exists for every matching realization and even in
the complete ordinary inclusion graph.

It also has nonzero, constant-order incidence mass in the compatibility
graph. In the compatible incidence multiset of the fixed profile arc,
simultaneous relabelling of the `d` matching edges is transitive. Since
every target has exactly `a_j` occupied `A_j` coordinates and every source
has exactly `a'_j`, the fraction of arc incidences whose target lies in
`mathcal C_T^-` is exactly `a_j/d`, while the fraction whose source lies
in `mathcal C_X^-` is exactly `1-a'_j/d`. Thus both degree sums appearing
in a degree-normalized mixing formula are positive constant fractions of
the arc mass, although the cross-incidence is zero.

For an upper arc, let the upper target half-count be `u_j` and the source
count be `u'_j=u_j-alpha_j`. Define

\[
\begin{aligned}
 \mathcal C_T^+&=\{U\in\tau:x\notin U\},\\
 \mathcal C_X^+&=\{X\in\kappa:x\in X\}.
\end{aligned}                                        \tag{3.5}
\]

Again there are no edges, now because `X subset U`, while

\[
 { |\mathcal C_T^+|\over w_T(\tau)}=1-{u_j\over d},
 \qquad
 { |\mathcal C_X^+|\over w_X(\kappa)}={u'_j\over d},              \tag{3.6}
\]

and both are at least `1/4-O(1/d)` on the safe core.

The same edge-label symmetry gives the corresponding incident-degree
fractions `1-u_j/d` and `u'_j/d` above.

Consequently no estimate of the form

\[
 e(\mathcal A,\mathcal B)
 =(1+o(1))
 {d(\mathcal A)d(\mathcal B)\over\sum_Xd(X)}         \tag{3.7}
\]

can hold uniformly for arbitrary profile-contained sets: its right side
is positive and of constant normalized order on (3.2) or (3.5), while its
left side is exactly zero. This refutes the sufficient raw cut-norm form
proposed in Section 8 of
`MATH_THEOREM_RANDOM_RANK_MATCHING_ALLOCATION_HALL_PROFILE_20260726.md`.

Independent rank matchings only randomize which additional compatibility
edges survive inside the inclusion relation. They can never fill either
zero rectangle.

## 4. What remains possible

The zero rectangles do not violate one-sided Hall expansion. For example,
the full lower cylinder `mathcal A_x^-` can still use essentially all
middle owners containing `x`, and the ratio of that containing shore to
the cylinder is precisely the upper bound (1.5).

Accordingly the following routes remain logically possible:

1. a local-LYM or compression theorem adapted to the random-rank
   compatibility relation;
2. an entropy proof which preserves monotone coordinate cylinders; or
3. a direct fractional flow with target rows one and owner columns below
   one, without demanding product mixing.

What is ruled out is any proof which first asserts constant-gap spectral
mixing or raw product cut-norm quasirandomness inside profiles. The
coordinate obstruction is exact, survives both signs, survives arbitrary
`o(W)` quarantine, and already occurs before packet axes and chronology
are imposed.

## 5. Audited boundary

Proved:

1. the optimal universal upper bound `e^(A^2)+o(1)` on `QRE_A` expansion;
2. the exact near-one coordinate singular value for every uniform-marginal
   inclusion coupling;
3. constant-density zero rectangles inside every safe ordered profile arc;
   and
4. failure of the proposed arbitrary-subset product cut-norm estimate, for
   both signs and every matching realization.

Not proved or refuted:

1. `QRE_A` with some fixed `0<delta_A<e^(A^2)-1`;
2. a one-sided entropy/compression theorem;
3. a raw injection; or
4. selected-axis and grouped packet chronology.

Thus the raw all-cuts problem remains open, but its spectral/quasirandom
form is now sharply and permanently excluded.
