# Corrected full-cube suffix dual and the preceding-scale quotient

Date: 2026-07-26

## 0. Outcome

The suffix-star dual obstruction must be applied to the **full** compatible
two-scale cube, not to a cardinality-tuned `L`-bit restriction.

Put

\[
 d=\operatorname {Cat}_r,qquad t={d\over p},qquad
 B=M_r+M_{r+1}-E_r,                                    \tag{0.1}
\]

where

\[
 M_r=H_{m,r+1}\operatorname {Cat}_{r-1},\qquad
 M_{r+1}=H_{m,r+2}\operatorname {Cat}_r,\qquad
 E_r=H_{m,r+2}\operatorname {Cat}_{r-1}.               \tag{0.2}
\]

Every bit still has one hereditary suffix arm which is neutral on the
canonical overloaded-set dual.  Hence its isolated fixed-cut drain is at
most three.  But a product law may use all `B` legal bits.  The corrected
fixed-cut residual is therefore

\[
 D_r-3B,qquad
 D_r=H_{m,r}d\left({1\over2}-{1\over t}\right),         \tag{0.3}
\]

not `D_r-3L`.

Define the exact threshold

\[
 \boxed{
 t_c(m,r)=
 \left(
  {1\over2}-{3B\over H_{m,r}d}
 \right)^{-1}.}                                        \tag{0.4}
\]

Then

\[
                         t_c(m,r)={64\over11}+O(r^{-1}+r/m).             \tag{0.5}
\]

The exact fixed-cut residual is positive if and only if `t>t_c(m,r)`.
After the two-boundary remainder is restored, the multidepth theorem is
quantitatively obstructive whenever

\[
 D_r-3B\gg {W\over r^3}+\max_{q\in I}(W-N_q),          \tag{0.6}
\]

and gives an `Omega(W)` obstruction on `J=Theta(r^(3/2))` depths whenever
`D_r-3B=Theta(H_(m,r)d)`.  In particular this holds whenever
`t>=64/11+epsilon` for a fixed `epsilon>0`.
For `t<=t_c(m,r)`, this witness is nonpositive after the extra legal bits
are admitted; no no-go follows.  When `t-t_c=o(1)` is positive, the
residual must still beat the explicit errors in (0.6).

The preceding scale `r-1` changes the picture exactly where requested.
Write

\[
 c=\operatorname {Cat}_{r-1},qquad
 u=\operatorname {Cat}_{r-2},                           \tag{0.7}
\]

and

\[
 R_r={d\over c}={2(2r-1)\over r+1},qquad
 R_{r-1}={c\over u}={2(2r-3)\over r}.                  \tag{0.8}
\]

For one isolated parent packet, its distinguished arm starts at loads
`(c,u)` and, after `k` packet switches, has loads `(c-k,u+k)`.  All `u`
switches would give one full unit of cap relief if and only if

\[
 \boxed{
 \tau_-(r):={R_rR_{r-1}\over R_{r-1}-1}
 \le t\le
 \tau_+(r):={R_rR_{r-1}\over2}.}                       \tag{0.9}
\]

The endpoints satisfy

\[
                         \tau_-(r)={16\over3}+O(r^{-1}),qquad
                         \tau_+(r)=8+O(r^{-1}).          \tag{0.10}
\]

Thus `4<tau_-(r)<t_c(m,r)<tau_+(r)` for all sufficiently large `r`
in the asymptotic range `r=o(m)`.

Thus throughout

\[
                         {16\over3}+o(1)<t
                         \le {64\over11}+o(1),          \tag{0.11}
\]

an isolated preceding packet has a full fourth arm.  This does **not**
sum over parents.  At scale `r-1` there is a matching of

\[
 K_a=(2a-3)\operatorname {Cat}_{a-2}
     ={a\over2(2a-1)}H_{m,r},\qquad a=m-r,              \tag{0.12}
\]

pairs of distinct parent contexts which induce the same ordered suffix
arc at every serviced depth.  Hence `(1/2+o(1))H_(m,r)` parent packets
already lie in nontrivial suffix fibres.  For one paired fibre the
canonical destination load is at least `2u`; because

\[
                         2u<p<4u                       \tag{0.13}
\]

throughout the range under discussion, the two packets cannot both be
credited with `u` independent units of fourth-arm relief.  If the fibre
has no other incident suffix arcs and its exact loads are `(2c,2u)`, its
entire distinguished capacity is only `p-2u`.

The correct object is therefore the contracted directed suffix graph.
At each fixed depth its optimum is an integral convex-cost flow; across
depths the same packet variables are synchronized, and the stacked
matrix is not a network matrix.  The preceding scale supplies a genuine
candidate fourth arm only if this synchronized suffix-flow optimum
survives together with the other three arms.  The isolated Catalan
straddle alone does not prove that.

The resulting uniform `t`-dichotomy is:

1. `t>t_c(m,r)`: the full `(r,r+1)` fixed-cut residual is positive;
   when the gap beats (0.6) it is a genuine multidepth obstruction, and
   every fixed margin `t>=64/11+epsilon` gives `Omega(W)`;
2. `tau_-(r)<=t<=t_c(m,r)`: that obstruction fails and an isolated
   `r-1` packet has a full fourth arm, but positive-density suffix-fibre
   collisions prevent packetwise summation;
3. `4<=t<tau_-(r)`: the isolated preceding arm is source-limited, and
   pooling inside a suffix fibre can either help the source or saturate
   the destination.  The same contracted-flow gate remains.

No bounded menu is declared closed in regimes 2 or 3.

---

## 1. Corrected full-cube multidepth dual

Let

\[
                         \Omega_q=\{S:\mu_q^0(S)>p\},qquad
                         \alpha_q=\mathbf1_{\Omega_q}.  \tag{1.1}
\]

For every retained scale-`r` or scale-`r+1` switch and every common depth
`q>=r+1`, the hereditary marked suffix arm has both endpoints in
`Omega_q`.  Its coefficient against `alpha_q` is zero.  The other three
arms decrease the fixed potential by at most three:

\[
                         \langle\alpha_q,a_{q,e}\rangle\ge-3.           \tag{1.2}
\]

For the full nonadditive cube, a depth-`q` target can fail to be additive
only when switches occur at both boundary phases of its window.  The
exact two-bit Boolean expansion of one such target is

\[
 \mathbf e_{T_{11}}-\mathbf e_{T_{10}}
 -\mathbf e_{T_{01}}+\mathbf e_{T_{00}},               \tag{1.3}
\]

whose pairing with `alpha_q` has absolute value at most two.  The
two-hole Catalan count for the full compatible catalogue gives, uniformly
for `r+1<=q<=m/2`,

\[
 \#\{\hbox{double-boundary depth-}q\hbox{ windows}\}
 \le {C W\over r^3}.                                   \tag{1.4}
\]

This is statewise: interior switches do not change the intersection once
the two neighboring boundary states are fixed.  Hence it also holds after
averaging an arbitrary law on the full cube.  Since there are `B` bits,
`E|x|<=B`, and cap tail is the support function of the target-weight
cube, every such mean obeys

\[
\boxed{
 \left(K_{q,p}(\bar\mu_q)-(W-N_q)\right)_+
 \ge
 \left[D_r-(W-N_q)-3B-{C W\over r^3}\right]_+.}       \tag{1.5}
\]

Here the plateau lower bound `K_(q,p)(mu^0)>=D_r` is used at every depth.
Summing (1.5) over any interval `I` is the corrected full-cube
multidepth theorem.

In particular, take `I={r+1,...,r+J}` with
`J=floor(r^(3/2))`, in a range where
`max_(q in I)(W-N_q)=o(H_(m,r)d)`.  If
`D_r-3B=Theta(H_(m,r)d)`, then the sum in (1.5) is

\[
                 \Omega(JH_{m,r}d)=\Omega(W).          \tag{1.6}
\]

More generally, (0.6) makes the lower bound positive, but it is only of
order `J(D_r-3B)` and need not be `Omega(W)` when `t-t_c=o(1)`.

### Exact threshold calculation

Put `a=m-r`.  The two-scale count gives

\[
 \rho_{m,r}:={M_r\over H_{m,r}d}
 ={a(r+1)\over4(2a-1)(2r-1)},                          \tag{1.7}
\]

and

\[
 {B\over M_r}
 =1+{3(a-1)(r-1)\over2(2a-3)(r+1)}.                   \tag{1.8}
\]

Therefore

\[
 {B\over H_{m,r}d}
 ={7\over64}+O(r^{-1}+r/m).                            \tag{1.9}
\]

Substitution in (0.4) proves (0.5).  Equivalently,

\[
 {D_r-3B\over H_{m,r}d}
 ={1\over2}-{1\over t}
  -3\rho_{m,r}{B\over M_r}.                            \tag{1.10}
\]

The leading fixed-cut residual is positive exactly when
`t>t_c(m,r)`.  A fixed positive margin above `64/11` makes it a fixed
positive fraction of `H_(m,r)d`; an `o(1)` excess over the threshold must
still be compared with the explicit errors in (1.5).

More precisely,

\[
 D_r-3B
 =H_{m,r}d\left({1\over t_c(m,r)}-{1\over t}\right)
 ={H_{m,r}d\,(t-t_c(m,r))\over t\,t_c(m,r)}.           \tag{1.11}
\]

Since `H_(m,r)d=Theta(W/r^(3/2))`, the two-boundary term alone creates a
transition layer `t-t_c=O(r^(-3/2))`.  The plateau correction
`W-N_q` may widen that layer according to the chosen depth interval.

---

## 2. Exact cap gain of the preceding-scale arm

Consider one scale-`r-1` parent packet.  It contains exactly

\[
                         u=\operatorname {Cat}_{r-2}    \tag{2.1}
\]

elementary switches.  Before cross-parent target identifications, its
distinguished hereditary arm has the isolated two-bin occurrence ledger

\[
                         (c,u)=
  (\operatorname {Cat}_{r-1},\operatorname {Cat}_{r-2}).               \tag{2.2}
\]

In the full admissible range `4<=t<16`, one has `c>p`; in the middle
range of interest one also has `u<p`.  After choosing `k` of the `u`
switches, the two loads become

\[
                              (c-k,u+k).                 \tag{2.3}
\]

The exact cap-tail gain on this arm is

\[
\begin{aligned}
 G_{r-1}(k)={}&(c-p)_++(u-p)_+\\
 &-(c-k-p)_+-(u+k-p)_+.                                \tag{2.4}
\end{aligned}
\]

When `c>p>u`, this simplifies to

\[
 \boxed{
 G_{r-1}(k)=\min\{k,c-p\}-\bigl(k-(p-u)\bigr)_+.}      \tag{2.5}
\]

Equivalently, the next switch has marginal gain `+1` when source relief
is still active and destination cost has not begun, `0` when both are
active or both inactive, and `-1` when only destination cost is active.
The last case is why the three-way minimum would be incorrect.

Consequently every elementary switch contributes one full unit on the
distinguished arm for all `0<=k<=u` exactly when

\[
                         u\le c-p,qquad 2u\le p.        \tag{2.6}
\]

Using `d=tp`, `c=d/R_r`, and `u=d/(R_rR_(r-1))`, the two inequalities in
(2.6) are precisely

\[
                         t\ge\tau_-(r),qquad
                         t\le\tau_+(r),                 \tag{2.7}
\]

with the exact thresholds in (0.9).

For all sufficiently large `r` on the range needed here,
`t<=t_c(m,r)<tau_+(r)`, so the destination has room for the entire
packet.  Therefore the full-packet gain has the exact two-piece form

\[
 \boxed{
 G_{r-1}(u)=
 \begin{cases}
  c-p,&4\le t<\tau_-(r),\\
  u,&\tau_-(r)\le t\le t_c(m,r).
 \end{cases}}                                          \tag{2.8}
\]

This is the exact **isolated-packet** calculation.  The ordered suffix arc
persists at larger serviced depths, but different parent contexts can
coalesce onto that same physical arc.  Therefore (2.8) may not be summed
over packets before the suffix fibres are contracted.

---

## 3. Full preceding-scale suffix quotient

Apply the adjacent-scale compatibility theorem to scales `r-1` and `r`.
Delete the scale-`r` endpoint of every conflict.  Then all
`M_(r-1)` preceding-scale switches remain, together with

\[
                         M_r-E_{r-1},qquad
 E_{r-1}=H_{m,r+1}\operatorname {Cat}_{r-2}.            \tag{3.1}
\]

Fix a depth `q`.  Let `V_q` be the physical target set and let
`mu_q^0(v)` be the canonical load.  Each scale-`r-1` parent context `C`
contributes `u` parallel distinguished arcs

\[
                         s_{C,q}\longrightarrow t_{C,q}.              \tag{3.2}
\]

If `x_C in [0,u]` units of that packet are selected, its distinguished
contribution is

\[
 A_qx=\sum_Cx_C(\mathbf e_{t_{C,q}}-
                       \mathbf e_{s_{C,q}}).            \tag{3.3}
\]

Define its exact fixed-depth capacity by

\[
 \boxed{
 \Phi_q:=K_{q,p}(\mu_q^0)-
  \min_{0\le x_C\le u}K_{q,p}(\mu_q^0+A_qx).}         \tag{3.4}
\]

Linearize the positive parts by variables `z_v`:

\[
 \min\sum_{v\in V_q}z_v,\qquad
 z_v\ge \mu_q^0(v)+(A_qx)_v-p,\quad z_v\ge0,\quad
 0\le x_C\le u.                                       \tag{3.5}
\]

The matrix `A_q` is a directed incidence matrix.  In inequality form the
only nontrivial block is `[A_q|-I]`; it is totally unimodular, and
adjoining the bound rows for `x` preserves total unimodularity.  Hence
(3.5) is equivalently a capacitated min-cost flow and has an integral
optimum when `p,u,mu_q^0` are integral.  This is a genuine fixed-depth
integrality statement; no generic hypergraph rounding is needed for the
distinguished suffix arms alone.

It does not solve the required problem.  A physical packet choice uses
the same `x_C` at every depth and simultaneously activates the other
three arms.  Stacking the matrices `A_q` repeats a column in several
different incidence graphs, so the stacked matrix is not itself a
directed incidence matrix.  The exact synchronized suffix functional is

\[
 \Phi_I:=\max_{0\le x_C\le u}
 \sum_{q\in I}w_q
 \left[K_{q,p}(\mu_q^0)-K_{q,p}(\mu_q^0+A_qx)\right]. \tag{3.6}
\]

The common variable `x_C`, followed by the three omitted arms, is the
surviving non-network coupling.

### 3.1 Positive-density ordered-arc collisions

Put `a=m-r`.  The marked-gap construction gives a matching of

\[
 K_a=(2a-3)\operatorname {Cat}_{a-2}
     ={a\over2(2a-1)}H_{m,r}.                           \tag{3.7}
\]

pairs of distinct scale-`r-1` parent contexts.  The two contexts in a
pair have the same suffix core and the same local labels `beta,gamma`.
They therefore give the same **ordered** arc (3.2), not merely one common
unoriented target, at every serviced depth.

The canonical occurrence injections from the two contexts are disjoint.
Thus their common source and destination have loads at least `2c` and
`2u`, respectively.  In the range `4<=t<=t_c(m,r)`,

\[
                         2u<p<4u.                       \tag{3.8}
\]

The left inequality follows from `t<tau_+(r)`; the right follows from
`t>=4>R_rR_(r-1)/4`.  Hence the two packets cannot both be assigned their
isolated value `u`: before `2u` units can enter the common destination,
that destination crosses the cap.

For the model component consisting of exactly this ordered arc, with
exact loads `(2c,2u)` and no other incident arc, (3.5) gives

\[
 \boxed{\Gamma_2=p-2u.}                                \tag{3.9}
\]

Indeed

\[
 2c-p\ge2u
 \quad\Longleftrightarrow\quad
 t\ge {R_rR_{r-1}\over2(R_{r-1}-1)}
      ={\tau_-(r)\over2},                               \tag{3.10}
\]

and `4>tau_-(r)/2` for all sufficiently large `r`.  Thus the source has
room to lose all `2u` occurrences, while the
destination has only `p-2u` units of slack.  For an isolated ordered
fibre of multiplicity `j` with exact loads `(jc,ju)`, the corresponding
formula is

\[
 \boxed{
 \Gamma_j=\min\{ju,(jc-p)_+,(p-ju)_+\}.}               \tag{3.11}
\]

In particular every fibre with `ju>=p` has zero direct distinguished
capacity.  Other incident arcs can relay mass through the vertex, so
(3.9)--(3.11) are not a global upper bound for (3.6).  Conversely,
coalescence of several matched pairs may make the destination overloaded
already at the zero state, so the matching does not give a positive lower
bound either.  It proves exactly that `H_(m,r)G_(r-1)(u)` is not a legal
full-catalogue ledger.

### 3.2 Scalar count after the correction

Even if the distinguished preceding arms are credited with zero, the
optimistic three-arm ceiling of the compatible `(r-1,r)` pair is

\[
 \mathsf S_3=3M_{r-1}+3(M_r-E_{r-1}),                  \tag{3.12}
\]

and

\[
 {\mathsf S_3\over H_{m,r}d}
 ={3\over R_rR_{r-1}}
  +3\rho_{m,r}\left(1-{1\over R_{r-1}}\right)
 ={21\over64}+O(r^{-1}+r/m).                           \tag{3.13}
\]

For `t<=64/11+o(1)`, the normalized plateau demand is at most
`21/64+o(1)`.  Thus this raw three-arm total count does not obstruct the
lower regimes, with or without the preceding fourth arm.  What remains
is directional: prove that the synchronized suffix flow (3.6) and the
other three arms jointly drain the overloaded targets, or exhibit a
weighted potential against that joint system.

---

## 4. Uniform decision table

Let all thresholds retain their exact finite-`r,m` definitions.

### Regime A: `t>t_c(m,r)` with margin

If

\[
 D_r-3B\gg {W\over r^3}+\max_{q\in I}(W-N_q),         \tag{4.1}
\]

then the full `(r,r+1)` cube has a positive dual obstruction (1.5).  It
is `Omega(W)` on `J=Theta(r^(3/2))` depths when the residual is a fixed
fraction of `H_(m,r)d`; this includes every fixed-margin range
`t>=64/11+epsilon`.

### Regime B: `tau_-(r)<=t<=t_c(m,r)`

The old full-cube witness is nonpositive.  An isolated preceding packet
has the full gain (2.8), but the positive-density ordered-arc collisions
in Section 3.1 forbid summing that gain packetwise.  Each fixed depth is
an integral suffix flow; the live theorem is synchronized multidepth
four-arm dispersion for (3.6).

### Regime C: `4<=t<tau_-(r)`

The isolated preceding arm is source-limited according to (2.5), but
pooling in a suffix fibre can increase source surplus while simultaneously
destroying destination slack.  The full `(r,r+1)` fixed-cut witness is
nonpositive because `tau_-(r)<t_c(m,r)` for large `r`.  The same exact
quotient problem (3.6), coupled to the other three arms, remains.

This is the exact uniform boundary supplied by the current catalogues.
Only the part of Regime A satisfying (4.1) is closed negatively; the
explicit transition layer above `t_c(m,r)` is not.

---

## 5. Precise surviving routing gate

Let `mathcal E` be the retained compatible `(r-1,r)` bits and let `nu`
be a product law on their exact Boolean cube.  For a state `X`, write

\[
 x_C(X)=\sum_{e\ {\rm in\ parent}\ C}X_e.
\]

At depth `q` decompose the exact histogram as

\[
 \mu_q^X=\mu_q^0+A_qx(X)+L_qX+\mathcal R_q(X),         \tag{5.1}
\]

where `A_qx` is the contracted distinguished suffix contribution,
`L_qX` is the sum of the other three isolated arms, and
`mathcal R_q` is the exact double-boundary remainder.  The remaining
fractional theorem is precisely

\[
\boxed{
 \inf_\nu\;
 \sum_{q\le Q}w_q
 \left[
  K_{q,p}\!\left(
   \mu_q^0+A_q\mathbf E_\nu x+
   L_q\mathbf E_\nu X+
   \mathbf E_\nu\mathcal R_q(X)
  \right)
  -(W-N_q)
 \right]_+
 =o(W).}                                               \tag{5.2}
\]

The infimum is over one common product law `nu`, not independent
optimizers at different depths.  Equation (3.5) proves integrality only
after deleting
`L_q`, `mathcal R_q`, and all but one depth.  Thus it cannot be pasted
into (5.2).  Conversely, the full-cube suffix cut proves that (5.2) is
impossible in Regime A but supplies no separating dual in Regimes B or C.

This is the precise surviving gate: a synchronized, collision-contracted
four-arm dispersion theorem for the compatible `(r-1,r)` cube.  A proof
must exploit the actual common suffix graph and the variable prefix arms;
a tuned-subcube lower bound or a packetwise Catalan straddle is
insufficient.
