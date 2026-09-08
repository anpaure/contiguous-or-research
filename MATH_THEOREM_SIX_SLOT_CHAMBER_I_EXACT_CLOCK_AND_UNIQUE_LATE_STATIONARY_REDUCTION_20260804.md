# Six-slot chamber I: exact clock and unique late-stationary reduction

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction for the actual
chamber-I functional.  It does not replace the true period by the
threshold period.  It proves that, for fixed `(p,a)`, the complete
three-pulse gate has only its two endpoint exits and at most one genuine
interior-minimum exit.  That interior exit is confined to an explicit
late compact strip.  The theorem does not sign the remaining endpoint or
late-stationary gates, and therefore does not by itself close chamber I.

Put

\[
                         A={\sqrt\pi\over2},
\]

and let `K` be the Rayleigh signed-tail kernel.  On chamber I the exact
retained-pulse gate is

\[
\begin{aligned}
 \mathcal G_{\rm I}(p,a,b)={}&\mathcal L_3(p;a,2a)\\
 &+K(b-a)-K(a)+K(b)-K(2a)\\
 &+K(p+b)-K(p+2a),
\end{aligned}
\tag{0.1}
\]

on

\[
 {A\over2}\le p<A,
 \qquad 0\le a\le {p\over3},
 \qquad a\le b\le2a,
 \qquad p+b<A.
\tag{0.2}
\]

All closures below are taken inside the compact set obtained by replacing
the last strict inequality by `p+b<=A`.  Positivity on the strict physical
domain follows from positivity on that closure.

## 1. The actual clock and its two inert displayed generators

Set

\[
                         x=b-a.
\tag{1.1}
\]

Then (0.1) is exactly the Bellman functional of the six-slot table

\[
 \boxed{(0,x,b,p,p+a,p+b,2p).}
\tag{1.2}
\]

Indeed, the chamber inequalities give

\[
 0\le x\le a,
 \qquad b\le2a,
 \qquad p\ge3a.
\tag{1.3}
\]

They verify all internal superadditivity inequalities for (1.2).  The
only non-immediate ones reduce to

\[
 b\ge2x,
 \qquad p\ge2b-a,
 \qquad p\ge a+b,
\tag{1.4}
\]

and these follow respectively from `b<=2a`, `b<=2a`, and `p>=3a`.
Moreover,

\[
                         p+b=p+b,
 \qquad                 2p=p+p,
\tag{1.5}
\]

so the size-five generator is exactly the composition of sizes two and
three, while the size-six generator is exactly two size-three generators.
Both displayed generators are inert in the max-plus recurrence.

The exact clock is

\[
\begin{array}{c|cccccc}
 m&0&1&2&3&4&5\\ \hline
 V_m&0&x&b&p&p+a&p+b,
\end{array}
\tag{1.6}
\]

and, for every `q>=2`,

\[
 V_{3q}=qp,
 \qquad V_{3q+1}=qp+a,
 \qquad V_{3q+2}=qp+2a.
\tag{1.7}
\]

For `q=1`, the first two formulas in (1.7) remain true while the last
eventual value `p+2a` is replaced by the available value `p+b`.  At
capacities one and two, the eventual values `a,2a` are similarly replaced
by `x,b`.  Summing (1.6)--(1.7) gives exactly (0.1).

This records a useful but limited simplification: the clock has only four
non-inert displayed generator types, but all four remain below `A`.
Therefore complete positivity through grid size five cannot simply be
cited; the first threshold crossing still occurs at the inert composite
capacity six.

## 2. A period-retaining lower clock

Write

\[
 (W_0,\ldots,W_5)=(0,x,b,p,p+a,p+b).
\tag{2.1}
\]

Superadditivity and `V_6=2p` give

\[
                         V_{6q+i}\ge2qp+W_i
 \qquad(q\ge0,\ 0\le i<6).
\tag{2.2}
\]

For `q>=1`, both sides lie in `[A,infinity)`, where `K` is increasing.
Consequently

\[
 \boxed{
 \mathcal G_{\rm I}(p,a,b)
 \ge \mathcal R(p,a,b)
 :=\sum_{q\ge0}\sum_{i=0}^{5}K(2qp+W_i).}
\tag{2.3}
\]

Unlike threshold-period descent, (2.3) retains the true composite period
`2p`.  The cyclic gap word of `mathcal R` is

\[
 \boxed{(x,a,p-b,a,x,p-b).}
\tag{2.4}
\]

It is ordered in the sense

\[
                         0\le x\le a\le p-b,
\tag{2.5}
\]

because `p-b>=3a-2a=a`.  Thus (2.3) is a special six-gap train with two
copies of each of three ordered gaps.  It remains proof-safe at the
degenerate boundary where the threshold-period theta lower bound can be
negative.

The six compact head points also have the exact reflection-free pairing

\[
 (0,p+b),\qquad(x,p+a),\qquad(b,p),
\tag{2.6}
\]

so all three pair sums are the same subthreshold value `p+b`.

## 3. The compact kernel has positive third derivative

Put

\[
 c={\pi\over4},
 \qquad h(t)=t e^{-ct^2},
 \qquad D(u)=h(1+u)-h(1-u).
\tag{3.1}
\]

For `0<=u<=1`, direct differentiation gives

\[
                         K'(Au)=2A D(u)
\tag{3.2}
\]

and hence

\[
 K'''(Au)={2\over A}
 \{h''(1+u)-h''(1-u)\}.
\tag{3.3}
\]

### Lemma 3.1

For every

\[
                         0<u<1,
\]

one has

\[
                         \boxed{K'''(Au)>0.}
\tag{3.4}
\]

### Proof

For `0<u<=1/2`, this is exactly the strict increase of

\[
 G(u)=h'(1+u)+h'(1-u)
\]

proved in the compact second-derivative lemma: its proof establishes

\[
 G'(u)=h''(1+u)-h''(1-u)>0.
\]

Now let `1/2<=u<1`.  Since

\[
 h''(t)=2ct(2ct^2-3)e^{-ct^2},
\tag{3.5}
\]

the inequality `pi>8/3` gives

\[
 {3\over2}>\sqrt{6/\pi}.
\]

Thus `h''(1+u)>0`, whereas `0<1-u<=1/2` gives
`h''(1-u)<0`.  The difference in (3.3) is again strictly positive.
This proves (3.4).  \(\square\)

## 4. Exact one-parameter collapse

For fixed `(p,a)`, all dependence of (0.1) on `b` is carried by

\[
                         J_{p,a}(b)
 :=K(b-a)+K(b)+K(p+b).
\tag{4.1}
\]

Let

\[
                         B(p,a)=\min\{2a,A-p\}.
\tag{4.2}
\]

The closed chamber fibre is the interval

\[
                         I_{p,a}=[a,B(p,a)].
\tag{4.3}
\]

When `a>0`, the strict physical domain (0.2) implies `4a<A`.  On the
closed domain the same strict inequality holds whenever the fibre is
nontrivial: `B(p,a)>a` gives `p+a<A`, while `p>=3a`.  The only possible
equality case `4a=A` has `B(p,a)=a` and is already an endpoint-only
fibre.  Hence, on every nontrivial fibre, the first two arguments in
(4.1) lie in `[0,A/2)`, while the third lies in `(0,A]`.  Lemma 3.1
therefore gives

\[
 \boxed{
 J'''_{p,a}(b)
 =K'''(b-a)+K'''(b)+K'''(p+b)>0
 \quad(a<b<B(p,a)),}
\tag{4.4}
\]

with the same strict conclusion at a one-sided endpoint whenever the
fibre is nontrivial.  In particular,

\[
                         J'_{p,a}\ \hbox{is strictly convex.}
\tag{4.5}
\]

Define the stationary expressions

\[
\begin{aligned}
 \Sigma(p,a,b)
  &:=K'(b-a)+K'(b)+K'(p+b),\\
 \Xi(p,a,b)
  &:=K''(b-a)+K''(b)+K''(p+b).
\end{aligned}
\tag{4.6}
\]

### Theorem 4.1 (unique late-stationary reduction)

For every fixed feasible `(p,a)` with `a>0`, the set

\[
 \mathcal S_{p,a}
 :=\{b\in(a,B(p,a)):
       \Sigma(p,a,b)=0,\ \Xi(p,a,b)\ge0\}
\tag{4.7}
\]

has at most one element.  Moreover,

\[
\boxed{
 \min_{b\in I_{p,a}}\mathcal G_{\rm I}(p,a,b)
 =\min\left(
   \mathcal G_{\rm I}(p,a,a),
   \mathcal G_{\rm I}(p,a,B(p,a)),
   \{\mathcal G_{\rm I}(p,a,b):b\in\mathcal S_{p,a}\}
            \right).}
\tag{4.8}
\]

The last set is omitted when empty.

### Proof

The derivative of `mathcal G_I` in `b` is exactly `Sigma`, and its
second derivative is exactly `Xi`; all other terms in (0.1) are fixed.
By (4.5), `Sigma=J'` is strictly convex.  A strictly convex function on
an interval has at most two zeros.  If two zeros exist, only the larger
one can have nonnegative derivative `Xi=Sigma'`; if one zero exists, the
same condition selects it only when it can be a local minimum of
`mathcal G_I`.  Thus (4.7) has at most one element.

Every interior minimizer must satisfy `Sigma=0` and `Xi>=0`.  All other
minimizers are endpoints.  This proves (4.8). \(\square\)

The two endpoint gates in (4.8) are explicit:

\[
\boxed{
\begin{aligned}
 \mathcal E_0(p,a)
 &:=\mathcal G_{\rm I}(p,a,a)\\
 &=\mathcal L_3(p;a,2a)
   +K(0)-K(2a)+K(p+a)-K(p+2a),
\end{aligned}}
\tag{4.9}
\]

and

\[
 \boxed{
 \mathcal G_{\rm I}(p,a,2a)
 =\mathcal L_3(p;a,2a).}
\tag{4.10}
\]

When `B(p,a)=A-p<2a`, the other endpoint is the already isolated
threshold endpoint `b=A-p`.  On the strict face `a<b<2a`, the table

\[
 (0,b-a,b,p,p+a,p+b)
\]

is a feasible five-slot table with endpoint `p+b=A`, and its exact
Bellman functional is precisely `mathcal G_I`; it is therefore positive
by the audited five-slot threshold theorem.  If this endpoint coincides
with `b=a`, it is already the endpoint `mathcal E_0`.  Thus the only
genuinely new upper endpoint is (4.10) on `p+2a<=A`.

## 5. The stationary point is forced into one late strip

Let `theta` be the unique number in `(1/2,1)` satisfying

\[
                         2\operatorname{arctanh}\theta
                         =\pi\theta,
\tag{5.1}
\]

and put

\[
                         \xi=A\theta.
\tag{5.2}
\]

### Lemma 5.1

On the compact branch,

\[
 K'(u)<0\quad(0<u<\xi),
 \qquad
 K'(u)>0\quad(\xi<u\le A).
\tag{5.3}
\]

### Proof

Equation (3.2) shows that a nonzero root of `K'(Au)` is equivalent to

\[
 {1+u\over1-u}=e^{\pi u},
\]

which is (5.1).  The function

\[
 f(u)=2\operatorname{arctanh}u-\pi u
\]

has `f(0)=0`, initially decreases because `f'(0)=2-pi<0`, has strictly
increasing derivative on `(0,1)`, and tends to infinity at one.  Hence it
has exactly one positive root.  Also

\[
 f(1/2)=\log3-\pi/2<0,
\]

so that root lies above `1/2`.  The signs in (5.3) follow directly from
(3.2). \(\square\)

Since

\[
                         0\le b-a\le b\le2a<A/2<\xi,
\]

the first two summands of `Sigma` are nonpositive, and the second is
strictly negative.  Consequently

\[
 \boxed{
 p+b\le\xi
 \quad\Longrightarrow\quad
 \Sigma(p,a,b)<0.}
\tag{5.4}
\]

Every member `b_*` of the stationary set (4.7) therefore satisfies

\[
                         \boxed{\xi<p+b_*<A.}
\tag{5.5}
\]

Thus there is no interior-minimum gate on the entire bulk subregion
`p+B(p,a)<=xi`; there `mathcal G_I` is strictly decreasing in `b`, and
its fibre minimum is the upper endpoint.  Even on the remaining region,
(4.7) leaves at most one late stationary value.

## 6. Degenerate boundary and final residual statement

If `a=0`, then (0.2) forces `b=0`, and all three pulses in (0.1) vanish.
Therefore

\[
 \boxed{
 \mathcal G_{\rm I}(p,0,0)
 =\mathcal L_3(p;0,0)=3C(p)>0,}
\tag{6.1}
\]

by strict all-ceiling positivity.  This includes the boundary near which
the threshold-period theta lower bound can be negative.

Combining (4.8)--(6.1), complete chamber-I positivity has been reduced,
without period loss, to the following three proof-safe exits:

1. the zero-first-gap endpoint `mathcal E_0(p,a)` in (4.9);
2. the pure repeated-gap endpoint `mathcal L_3(p;a,2a)` only on the
   lower-period face `p+2a<=A` (the complementary upper endpoint is the
   already-positive threshold face);
3. at most one late stationary point satisfying simultaneously

   \[
    \Sigma=0,\qquad\Xi\ge0,\qquad\xi<p+b<A.
   \]

No other `b`-minimum, availability pulse, or degenerate boundary remains.

## 7. Scope and dependencies

This is a sharp residual theorem for the actual chamber-I clock, not a
sign proof for the three exits in Section 6.  It does not close chamber I,
the complete `h=3` branch, six-slot positivity, the all-grid Bellman
inequality, or an OR-word upper bound.

| role | file | SHA-256 |
|---|---|---|
| exact chamber-I gate | `MATH_THEOREM_SIX_SLOT_THREE_EFFICIENT_EXACT_THREE_CHAMBER_GATE_20260804.md` | `a3a79b92148b1b4b415c7795473b70f50bd6d0b84f20f6899a3275f62af9b0dd` |
| independent exact-gate audit | `MATH_AUDIT_SIX_SLOT_THREE_EFFICIENT_EXACT_THREE_CHAMBER_GATE_INDEPENDENT_20260804.md` | `d6f89ab80a67b193e9ee6e5d31ccb82f906ec460ded4c382e13b1708c8d44a11` |
| compact `G' > 0` lemma on `0<u<=1/2` | `MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_DELAYED_B_CONCAVITY_AND_PURE_LATTICE_GATE_20260804.md` | `b494371c790ed20f14e29bd4beba67b27aa30f7f5b1447e4ef8da4e74db8ea14` |
| independent compact-lemma audit | `MATH_AUDIT_FIVE_SLOT_THREE_EFFICIENT_DELAYED_B_CONCAVITY_AND_PURE_LATTICE_GATE_INDEPENDENT_20260804.md` | `9eec90787605f06568446c353153503c51570c6dc218597181c09fafa160edaf` |
| five-slot threshold endpoint | `MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_THRESHOLD_ENDPOINT_AND_DELAYED_CROSSING_REDUCTION_20260804.md` | `1e15d736592bce3103786fb965f62fe6f028436c0d35b763b195157a2cf3d0b6` |
| independent threshold audit | `MATH_AUDIT_FIVE_SLOT_THREE_EFFICIENT_THRESHOLD_ENDPOINT_AND_DELAYED_CROSSING_REDUCTION_INDEPENDENT_20260804.md` | `6d07121018046f26f4ab5377e37dd692efffa8389b9d939668e2f1a73ae14425` |
| strict all-ceiling positivity | `MATH_THEOREM_RAYLEIGH_CEILING_DOMINATION_AND_FINITE_MIR_CONE_NOGO_20260804.md` | `18a5d75526774673909d29a26d93710a1d56e9298c51d3a4cebaa8ebcd62baf3` |
| independent ceiling audit | `MATH_AUDIT_RAYLEIGH_CEILING_DOMINATION_AND_FINITE_MIR_CONE_NOGO_20260804.md` | `9f807a2a044469bed61c2943adf51b48f71ce594748cc8d3fb41ceea3394ac39` |
