# The odd-block Gaussian Hall cut for every fixed-partition `B_4` atlas

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Corrected verdict

The frame-diffusion theorem in
`MATH_THEOREM_HASHED_THREE_SEED_B4_FRAME_DIFFUSION_20260726.md` is correct
as a perfect-matching-label statement, but it does **not** remove the full
Gaussian Hall obstruction.

All three relabelled `B_4` seeds still exchange coordinates inside one
fixed partition into four-blocks.  This preserves a coarser two-sided
channel.  For a target `T`, let

\[
 J(T)=\{i:|T\cap B_i|\in\{1,3\}\},                   \tag{0.1}
\]

and let

\[
 K(T)=|\{i\in J(T):|T\cap B_i|=3\}|.                \tag{0.2}
\]

Every physical depth-`q` window in every fixed-partition `B_4` packet,
regardless of its seed labels, satisfies

\[
 J(L)=J(U),\qquad K(U)=K(L)+q,                        \tag{0.3}
\]

where `L` and `U` are its lower intersection and upper union.

Fix the exact restrictions outside `J`, put `s=|J|`, and let `k=K(L)`.
The two literal target sides of this channel have exact sizes

\[
 \boxed{
 L_{s,k}=4^s\binom sk,
 \qquad
 U_{s,k,q}=4^s\binom{s}{k+q}.}                       \tag{0.4}
\]

This is independent of which of the three cyclic seeds is used in each
block.  If `p_\gamma` selected starts lie in a channel `\gamma`, the two
shadow supports in that channel have sizes at most

\[
                         \min(p_\gamma,L_\gamma),
 \qquad
                         \min(p_\gamma,U_\gamma).    \tag{0.5}
\]

Consequently, for any common lower/upper depth-`q` selection of total
occurrence mass `P_q`,

\[
 \boxed{
 M_q^-+M_q^+
 \ge
 \left[
   \sum_\gamma\max(L_\gamma,U_\gamma)-P_q
 \right]_+.}                                         \tag{0.6}
\]

The sum in (0.6) has a positive Gaussian excess.  If

\[
                         q=x\sqrt m+o(\sqrt m),
 \qquad x>0.                                         \tag{0.7}
\]

then

\[
 \sum_\gamma\max(L_\gamma,U_\gamma)
 \ge
 \bigl(2\Phi(x)+o(1)\bigr)N_q.                      \tag{0.8}
\]

where

\[
                         N_q=\binom{2m}{m-q}
 =(e^{-x^2}+o(1))W.                                  \tag{0.9}
\]

Therefore:

1. For the radius-balanced selection proposed in the `B_4` note,

   \[
                           P_q=N_q+o(W).              \tag{0.10}
   \]
   \]

   one has, for every fixed `x>0`,

   \[
   \boxed{
   M_q^-+M_q^+
   \ge
   \bigl(e^{-x^2}(2\Phi(x)-1)-o(1)\bigr)W.}          \tag{0.11}
   \]
   \]

2. Even if all `W-o(W)` middle starts are used at depth `q`,

   \[
   \boxed{
   M_q^-+M_q^+
   \ge
   \bigl(2e^{-x^2}\Phi(x)-1-o(1)\bigr)_+W.}          \tag{0.12}
   \]
   \]

   The coefficient is positive for every sufficiently small fixed
   `x>0`.

Thus the hashed ternary seed atlas remains coefficient-one impossible in
its present fixed-block form.  Randomizing, balancing, or causally hashing
the three local matching labels does not affect (0.3)--(0.4).

Any successful repair must use physical transitions which change the
four-block rank data: for example, coordinate exchanges between distinct
blocks, a phase-dependent recoupling of the block partition, or a larger
packet move whose lower and upper shadows do not retain one common odd-set
channel.  Merely choosing a different one-factor of `K_4` inside each
fixed block cannot work.

## 1. The exact coarse channel

Let `B_1,\ldots,B_b` be the moving four-blocks.  All remaining
coordinates, including any ternary-hash anchor, are allowed but are frozen
inside an individual packet.

Consider a physical depth-`q` window

\[
                         X_0,X_1,\ldots,X_q.          \tag{1.1}
\]

The recursive Hamming order used in the `B_4` construction touches `q`
different local blocks when `q\le r`.  In every touched block, all middle
states have local rank two and one local coordinate is exchanged.  Hence
the lower intersection has local rank one and the upper union has local
rank three.  Every untouched block has the same restriction in all
`X_j`, so its lower and upper restrictions are identical.

It follows immediately that the lower and upper targets have the same set
of odd-rank blocks.  Every touched block contributes rank one below and
rank three above; every untouched rank-three block remains rank three on
both sides.  This proves (0.3).

To make the channel literal, fix:

1. the common odd-block set `J`;
2. the exact subset in every block outside `J`;
3. the exact restriction on the anchor and leftover coordinates; and
4. the lower number `k` of rank-three blocks in `J`.

Call the resulting datum `\gamma`.  Its lower total-rank equation
determines `k`; the corresponding upper datum has `k+q` rank-three
blocks.  We use the convention `\binom sk=0` outside `0\le k\le s`.

### Lemma 1.1 (exact side sizes)

If `s=|J|`, then

\[
 |\mathcal L_\gamma|=4^s\binom sk,
 \qquad
 |\mathcal U_\gamma|=4^s\binom{s}{k+q}.             \tag{1.2}
\]

#### Proof

Choose the `k` lower rank-three blocks inside `J`; every other block of
`J` has rank one.  A four-block has four singleton subsets and four
triple subsets, so after the rank choice there are exactly `4^s` literal
targets.  The upper count is identical with `k+q` in place of `k`.
All restrictions outside `J` were fixed.  \(\square\)

The three seed matchings

\[
 12\mid34,\qquad13\mid24,\qquad14\mid23.             \tag{1.3}
\]

only change which rank-two edge produces a given singleton/triple pair.
They never change the side sizes or the channel relation.

## 2. The exact max-side Hall inequality

Let `p_\gamma` be the number of selected depth-`q` starts whose paired
lower/upper shadows lie in channel `\gamma`.  Since every start produces
one lower and one upper occurrence,

\[
                         \sum_\gamma p_\gamma=P_q.   \tag{2.1}
\]

No injectivity assumption is needed.  The number of distinct covered
lower targets in `\gamma` is at most

\[
                         \min(p_\gamma,L_\gamma),    \tag{2.2}
\]

and the upper support is at most `\min(p_\gamma,U_\gamma)`.  Therefore

\[
\begin{aligned}
 M_q^-+M_q^+
 &\ge
 \sum_\gamma
 \left((L_\gamma-p_\gamma)_+
      +(U_\gamma-p_\gamma)_+\right)\\
 &\ge
 \sum_\gamma\bigl(\max(L_\gamma,U_\gamma)-p_\gamma\bigr).
\end{aligned}                                        \tag{2.3}
\]

Using (2.1) and nonnegativity gives (0.6).

Both target layers have size `N_q`, so

\[
 \sum_\gamma L_\gamma
 =\sum_\gamma U_\gamma=N_q.                         \tag{2.4}
\]

Consequently

\[
 \sum_\gamma\max(L_\gamma,U_\gamma)
 =N_q+{1\over2}\sum_\gamma|L_\gamma-U_\gamma|.      \tag{2.5}
\]

Thus the excess is exactly the total-variation distance between the two
coarse channel laws, multiplied by `N_q`.

## 3. A scalar projection of the channel law

It is enough to retain only the number of rank-three moving blocks.  Let
`T^-` be uniform in the lower layer `\binom{[2m]}{m-q}` and put

\[
 K_-=|\{i:|T^-\cap B_i|=3\}|.                        \tag{3.1}
\]

Let `T^+` be uniform in the upper layer and define the adjusted statistic

\[
                         K_+=|\{i:|T^+\cap B_i|=3\}|-q.            \tag{3.2}
\]

Equation (0.3) says that paired occurrences have the same adjusted
statistic.  Projection cannot increase total variation, hence

\[
 {1\over2N_q}\sum_\gamma|L_\gamma-U_\gamma|
 \ge
 \left\|\mathcal L(K_-)-\mathcal L(K_+)\right\|_{\rm TV}.          \tag{3.3}
\]

Complement `T^+`.  Its complement is uniform in the lower layer, and a
rank-three block of `T^+` is a rank-one block of the complement.  Thus if

\[
 L_-=|\{i:|T^-\cap B_i|=1\}|.                        \tag{3.4}
\]

then

\[
                         K_+\overset d=L_--q.         \tag{3.5}
\]

We therefore compare `K_-` and `L_--q` under one lower-layer law.

## 4. Gaussian asymptotics of the projected cut

Assume the number of anchor and leftover coordinates is `o(m)`, as in the
hashed construction with `r=o(m)`.  Then

\[
                         b={m\over2}+o(m).            \tag{4.1}
\]

Put

\[
 p_m={m-q\over2m}
 ={1\over2}-{x\over2\sqrt m}+o(m^{-1/2}).            \tag{4.2}
\]

Under independent Bernoulli-`p_m` coordinates, one moving block has size
`R\sim\operatorname {Bin}(4,p_m)`.  Write

\[
 Y_3=\mathbf1_{\{R=3\}},
 \qquad
 Y_1=\mathbf1_{\{R=1\}}.                             \tag{4.3}
\]

Conditioning the independent model on total size `m-q` gives the uniform
lower layer exactly.

At `p=1/2`,

\[
\begin{aligned}
 \mathbb EY_3&=\mathbb EY_1={1\over4},\\
 \operatorname {Var}(Y_3)&=\operatorname {Var}(Y_1)={3\over16},\\
 \operatorname {Var}(R)&=1,\\
 \operatorname {Cov}(Y_3,R)&={1\over4},\\
 \operatorname {Cov}(Y_1,R)&=-{1\over4}.
\end{aligned}                                        \tag{4.4}
\]

Therefore the conditional variance per moving block is

\[
 {3\over16}-{(1/4)^2\over1}={1\over8}.               \tag{4.5}
\]

With `b=m/2+o(m)`, both conditional variances are

\[
                         {m\over16}+o(m).             \tag{4.6}
\]

The one-block probabilities satisfy

\[
\begin{aligned}
 4p^3(1-p)&={1\over4}+(p-1/2)+O((p-1/2)^2),\\
 4p(1-p)^3&={1\over4}-(p-1/2)+O((p-1/2)^2).
\end{aligned}                                        \tag{4.7}
\]

Consequently

\[
\begin{aligned}
 \mathbb E K_-&={b\over4}-{x\sqrt m\over4}+o(\sqrt m),\\
 \mathbb E(L_--q)&={b\over4}-{3x\sqrt m\over4}+o(\sqrt m).
\end{aligned}                                        \tag{4.8}
\]

### Lemma 4.1 (conditional central limit)

Under the uniform lower-layer law,

\[
 {K_--\mathbb EK_-\over\sqrt m/4}
 \Longrightarrow N(0,1),
 \qquad
 {L_--q-\mathbb E(L_--q)\over\sqrt m/4}
 \Longrightarrow N(0,1).                            \tag{4.9}
\]

#### Proof

For `K_-`, use the two-variable block polynomial

\[
 F_3(z,u)=(1+z)^4+4(u-1)z^3.                        \tag{4.10}
\]

For `L_-`, use

\[
 F_1(z,u)=(1+z)^4+4(u-1)z.                          \tag{4.11}
\]

Multiply over the `b` moving blocks and by `(1+z)^{o(m)}` for the anchor
and remainder.  Exponentially tilt `z` so that its Bernoulli parameter is
`p_m`; then the coefficient `[z^{m-q}]` conditions the sum of the block
sizes at its mean.  Expanding the logarithm of `F_j` for

\[
                         u=e^{it/\sqrt m}.            \tag{4.12}
\]

and applying Fourier inversion in the size coordinate gives a Gaussian
characteristic function.  The Schur complement of the size variance is
exactly (4.5), while all third cumulants contribute `O(m^{-1/2})`
uniformly for bounded `t`.  The coordinates outside the moving blocks are
`o(m)`; they are included in the conditioned size coordinate and change
the leading Schur-complement variance only by `o(m)`.  This proves
(4.9).  \(\square\)

Let `a_m` be the midpoint of the two means in (4.8).  Their separation is

\[
                         {x\sqrt m\over2}+o(\sqrt m).               \tag{4.13}
\]

which is `2x+o(1)` conditional standard deviations.  Lemma 4.1 gives

\[
\begin{aligned}
 \Pr(K_-\ge a_m)&\longrightarrow\Phi(x),\\
 \Pr(L_--q\ge a_m)&\longrightarrow\Phi(-x).
\end{aligned}                                        \tag{4.14}
\]

Hence

\[
 \left\|\mathcal L(K_-)-\mathcal L(L_--q)\right\|_{\rm TV}
 \ge2\Phi(x)-1-o(1).                                \tag{4.15}
\]

Combine (3.3) and (4.15) with (2.5).  This proves (0.8), and substitution
of the two possible values of `P_q` proves (0.11)--(0.12).

Finally,

\[
 {d\over dx}\left(2e^{-x^2}\Phi(x)-1\right)\bigg|_{x=0}
 =2\phi(0)>0.                                        \tag{4.16}
\]

Thus the full-mass coefficient in (0.12) is positive on a nonempty
interval `0<x<x_0`, without requiring a numerical value of `x_0`.

## 5. Consequence for the three-seed construction

The anchor hash proves the genuine estimate

\[
 I_{P,q}^\pm\le(3^{-q}+e^{-\Omega(r)})W.             \tag{5.1}
\]

for every fixed coordinate matching `P`.  The present theorem does not
retract that estimate.  It shows that perfect-matching labels are too fine
to see the surviving obstruction.

All three seeds preserve local block size along their middle cycles.
Therefore every hashed packet, every recursive Hamming cycle, every
context-dependent seed vector, and every nested start selection still
obeys the same odd-block channel (0.3).  The radius-balanced construction
is ruled out quantitatively by (0.11).

The minimal structural repair must make (0.3) false on positive Gaussian
occurrence mass.  It must include at least one of:

1. swaps whose removed and inserted coordinates lie in different
   four-blocks;
2. owner- or phase-dependent recouplings of the coordinate block
   partition; or
3. larger exact packet trades which move occurrences between different
   odd-block sets `J`.

A further randomization among the three one-factors of `K_4` inside the
same block partition cannot change a single term in (0.4), and hence
cannot repair the cut.
