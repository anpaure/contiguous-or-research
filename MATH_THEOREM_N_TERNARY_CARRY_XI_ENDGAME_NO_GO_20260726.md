# The ternary-carry factor in the collision-to-\(\nu\) endgame: exact ledger and a logarithmic-depth no-go

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\left\lfloor\frac m4\right\rfloor .
 \tag{0.1}
\]

Let \(g\ge3\), let \(t\) be a power of two with

\[
 g\le t\le \frac{3B}{64},
 \qquad h=2t,
 \tag{0.2}
\]

and install the phase-dense ternary-carry factor on every canonical
first-\(t\)-eligible macrocell.  Write \(u\) for its middle leave and

\[
 G=W-u.
 \tag{0.3}
\]

The exact factor data from the carry construction are

\[
 |\mathcal M|=24^t,qquad
 \ell_{\mathrm{car}}=2h3^t=4t3^t,qquad
 p_{\mathrm{car}}=\frac{G}{2h3^t}.
 \tag{0.4}
\]

The factor is cyclically \(t\)-geodesic.  Therefore the factor-blind
finite-delay compiler and product-SCD tail give the exact finite inequality

\[
 \boxed{
 \nu(2m+1)
 \le
 W+\frac{(g-1)G}{h3^t}
 +\mathcal A_{m,g}
 +\Xi^{\mathrm{car}}_{m,g}
 +2L_m(m-g).}
 \tag{0.5}
\]

Here \(\mathcal A_{m,g}\) is the same exact leave-capacity term as in
`MATH_THEOREM_TENSOR_PACKET_COLLISION_TO_NU_ENDGAME_20260726.md`, and
\(\Xi^{\mathrm{car}}_{m,g}\) is defined exactly in Section 3 below.  If

\[
 \frac uW\le
 \min\left\{
 \frac2{m+2},
 \frac{3m}{(2m+1)(m+2)}
 \right\},
 \tag{0.6}
\]

then

\[
 \boxed{\mathcal A_{m,g}=u.}
 \tag{0.7}
\]

The leave bound

\[
 \frac uW\le
 2(m+1)\exp\!\left(-\frac{3B}{256}\right)
 \tag{0.8}
\]

makes (0.6) automatic for all sufficiently large \(m\).

The attempted composition with tensor-packet internal injectivity is,
however, invalid.  That injectivity theorem concerns the recursive
trace-rainbow successor.  The ternary-carry factor uses parallel
common-order Hamming factors and is a sparse changed-edge perturbation of
them.  For either sign and every \(1\le q<h\), if \(K_q^\pm\) is the
number of distinct physical targets hit by all \(G\) good starts, then

\[
 \boxed{
 K_q^\pm\le G\eta_{h,q},\qquad
 \eta_{h,q}:=
 \frac h{2^q}
 +\frac{3q(1-3^{-t})}{4h}.}
 \tag{0.9}
\]

Consequently, at

\[
 q_*:=\left\lceil2\log_2h\right\rceil,
 \tag{0.10}
\]

the signed map of one macrocell has image \(o(24^t)\); in particular it
is not internally injective.  If \(q_*\le g-2\), then the exact
baseline-corrected excess satisfies

\[
 \boxed{
 \Xi^{\mathrm{car}}_{m,g}
 \ge
 N_{q_*}^-+N_{q_*}^+-2G\eta_{h,q_*},}
 \tag{0.11}
\]

where

\[
 N_q^-:=\binom{2m+1}{m-q},\qquad
 N_q^+:=\binom{2m+1}{m+q}.
 \tag{0.12}
\]

In the constant-one regime

\[
 g=\lceil a\sqrt m\rceil,qquad
 t=2^{\lceil\log_2g\rceil}
 \tag{0.13}
\]

for fixed \(a>0\), one has \(q_*\le g-2\),
\(\eta_{h,q_*}=o(1)\), and

\[
 N_{q_*}^-=W-o(W),\qquad N_{q_*}^+=W-o(W).
 \tag{0.14}
\]

Therefore

\[
 \boxed{
 \Xi^{\mathrm{car}}_{m,g}\ge(2-o(1))W.}
 \tag{0.15}
\]

Thus the current phase-dense ternary carry does not satisfy the collision
gate \(\Xi=o(W)\).  Its failure occurs already inside individual
macrocells, before any cross-macrocell collision is counted.  The word
"cross-packet" must therefore be removed from \(\Xi^{\mathrm{car}}\) for this
factor.

This does not disprove coefficient one.  It closes only the proposed
composition of the present carry successor with the collision-to-\(\nu\)
endgame.  The smallest surviving replacement is a carry fusion built on
the recursive trace-rainbow factors with a common legal port coordinate;
that compatibility theorem is unproved.

## 1. Canonical macrocells and the exact carry state count

In each labelled eight-block put

\[
 \mathcal V=
 \left\{
 X\cup Y:
 X\in\binom{\{a,b,c,d\}}2,
 \quad Y\in\{uw,ux,vw,vx\}
 \right\}.
 \tag{1.1}
\]

Thus \(|\mathcal V|=24\), and every member has size four.  A middle
owner is eligible in a block when its restriction belongs to \(\mathcal
V\).  For every owner with at least \(t\) eligible blocks, vary its first
\(t\) eligible blocks through \(\mathcal V\) and freeze the exterior.
The first-\(t\) rule is stable under this variation, so the good owners
partition into owner-disjoint macrocells

\[
 \mathcal M\cong\mathcal V^t,qquad |\mathcal M|=24^t.
 \tag{1.2}
\]

The finite leave estimate is (0.8).  It uses only \(t\le3B/64\), not
\(t=o(m)\).

The carry normal form on one macrocell has state set

\[
 \mathbb Z_2^t\times\mathbb Z_3^t\times K\times\mathbb Z_{2h},
 \qquad
 |K|=\frac{2^h}{2h}.
 \tag{1.3}
\]

Indeed,

\[
 2^t3^t\frac{2^h}{2h}(2h)
 =2^t3^t2^{2t}=24^t.
 \tag{1.4}
\]

The binary orbit label and syndrome \((b,k)\) remain fixed.  After one
\(2h=4t\)-step phase lap, the ternary word \(z\in\mathbb Z_3^t\) is
incremented by one modulo \(3^t\).  Hence every fixed \((b,k)\) gives
one component of length

\[
 2h3^t,
 \tag{1.5}
\]

and one macrocell has

\[
 2^t|K|=\frac{8^t}{4t}
 \tag{1.6}
\]

components.  Equations (1.2), (1.5), and (1.6) agree exactly.

The transition-block word is

\[
 1,2,\ldots,t
 \tag{1.7}
\]

repeated four times in every phase lap and then repeated through the
ternary odometer.  Every cyclic window of at most \(t\) transitions
therefore touches distinct eight-blocks.  The deleted coordinates are
distinct, as are the inserted coordinates, so for \(q\le t\)

\[
 \left|\bigcap_{j=0}^qF^j(x)\right|=m-q,
 \qquad
 \left|\bigcup_{j=0}^qF^j(x)\right|=m+q.
 \tag{1.8}
\]

This proves the precise geodesicity needed below.  It does not prove
shadow injectivity.

## 2. Exact compiler, collar, leave, and tail ledger

The eight-blocks occupy \(8B\) coordinates.  Since

\[
 n-8B=2(m\bmod4)+1\in\{1,3,5,7\},
 \tag{2.1}
\]

fix a residual coordinate \(z\).  It is frozen on every macrocell and
therefore on every carry cycle.  Split the good owners into masses

\[
 G_0+G_1=G,
 \tag{2.2}
\]

according as they omit or contain \(z\).

Use the factor-blind product-SCD tail with parameter \(m-g\).  Its odd
trimmed lift has length \(2L_m(m-g)\) and leaves Stage A responsible for

\[
 \begin{array}{c|c}
 \text{resource}&\text{target set}\\ \hline
 (-,q),\ 1\le q\le g-2&\binom{[n]}{m-q}\\[1mm]
 (+,q),\ 1\le q\le g-1&\binom{[n]}{m+q}\\[1mm]
 (-,\partial)&
 \{T:|T|=m-g+1,\ z\notin T\}\\[1mm]
 (+,\partial)&
 \{T:|T|=m+g,\ z\in T\}.
 \end{array}
 \tag{2.3}
\]

The two boundary sets have common size

\[
 Q_g=\binom{2m}{m-g+1}.
 \tag{2.4}
\]

The full-collar occurrence-capacity shortage is therefore

\[
 \boxed{
 \begin{aligned}
 \mathcal A_{m,g}:={}&
 \sum_{q=1}^{g-2}(N_q^--G)_+
 +\sum_{q=1}^{g-1}(N_q^+-G)_+\\
 &+(Q_g-G_0)_+
 +(Q_g-G_1)_+.
 \end{aligned}}
 \tag{2.4a}
\]

On a \(z\)-free carry cycle use delay and copied-prefix lengths

\[
 d_0=g-1,qquad \sigma_0=g-1;
 \tag{2.5}
\]

on a \(z\)-containing cycle use

\[
 d_1=g-2,qquad \sigma_1=g.
 \tag{2.6}
\]

Every defining delay window has at most \(g\le t\) transitions, so
(1.7) proves delay safety, including across the cyclic seam.  The
finite-delay identities then expose every resource in (2.3).  Both cycle
types cost exactly

\[
 d_\alpha+\sigma_\alpha=2g-2
 \tag{2.7}
\]

extra letters.  Since the global cycle count is (0.4), the full collar is

\[
 \boxed{
 (2g-2)p_{\mathrm{car}}
 =\frac{(g-1)G}{h3^t}.}
 \tag{2.8}
\]

There is no hidden factor of two.  In particular, when \(t\) is the
least power of two at least \(g\),

\[
 2g\le h<4g,
 \qquad
 \frac{(g-1)G}{h3^t}=o(W).
 \tag{2.9}
\]

Appending every omitted middle owner once changes the middle baseline
from \(G\) to \(W\).  The exact occurrence-capacity shortage is the same
\(\mathcal A_{m,g}\) as in the general endgame theorem.  Under (0.6),
the only surviving shortage is the upper rank \(m+1\), whose size is
\(W\) but whose good occurrence mass is \(G\).  It contributes exactly
\(u\), proving (0.7).  Indeed, every other full layer in (2.4a) has
size at most

\[
 \binom{2m+1}{m-1}
 =W\frac m{m+2}.
 \tag{2.10}
\]

For the two \(z\)-fibres before deletion,

\[
 W_0=\binom{2m}{m},\qquad
 W_1=\binom{2m}{m-1},
 \qquad G_\alpha=W_\alpha-u_\alpha,
 \quad 0\le u_\alpha\le u.
 \tag{2.11}
\]

Since \(g\ge3\), the smallest boundary gap is on the \(W_1\) side at
\(g=3\), and it is exactly

\[
 W_1-\binom{2m}{m-2}
 =\frac{3m}{(2m+1)(m+2)}\,W.
 \tag{2.12}
\]

This proves that (0.6) kills every positive part except \(N_1^+-G=u\).
The boundary condition in (0.6) is therefore needed to ensure
\(G_0,G_1\ge Q_g\); the weaker inequality \(u/W<2/(m+2)\) alone is not
sufficient for that finite simplification.

The finite-delay word, the omitted-owner singletons, the missing-target
singletons, and the product tail are separate literal blocks.  Every
witness lies wholly inside one such block.  Thus there is no additional
Stage-A/tail seam term, and (0.5) follows once the exact missing-target
count is written as in Section 3.

## 3. Exact physical multiplicity formula for \(\Xi^{\mathrm{car}}_{m,g}\)

For a good start \(x\), define the physical signed traces

\[
 \tau_q^-(x)=\bigcap_{j=0}^qF^j(x),
 \qquad
 \tau_q^+(x)=\bigcup_{j=0}^qF^j(x).
 \tag{3.1}
\]

For an interior resource let

\[
 n_q^\epsilon(T)
 =\#\{x\text{ good}:\tau_q^\epsilon(x)=T\},
 \tag{3.2}
\]

and put

\[
 K_q^\epsilon
 =\#\{T:n_q^\epsilon(T)>0\}.
 \tag{3.3}
\]

There are exactly \(G\) occurrences at every full signed depth.  Hence

\[
 C_q^\epsilon
 :=\sum_T(n_q^\epsilon(T)-1)_+
 =G-K_q^\epsilon.
 \tag{3.4}
\]

The baseline-corrected duplicate excess is

\[
 X_q^\epsilon
 :=C_q^\epsilon-(G-N_q^\epsilon)_+.
 \tag{3.5}
\]

Combining (3.4)--(3.5) gives the exact identity

\[
 \boxed{
 X_q^\epsilon
 =\min\{G,N_q^\epsilon\}-K_q^\epsilon.}
 \tag{3.6}
\]

No injectivity hypothesis is used in (3.6).

At the lower boundary count only starts in the \(z\)-free fibre; at the
upper boundary count only starts in the \(z\)-containing fibre.  If
\(K_\partial^-\) and \(K_\partial^+\) are the resulting distinct-target
counts, then exactly

\[
 X_\partial^-
 =\min\{G_0,Q_g\}-K_\partial^-,
 \qquad
 X_\partial^+
 =\min\{G_1,Q_g\}-K_\partial^+.
 \tag{3.7}
\]

Therefore the sharp tail-resolved carry excess is

\[
 \boxed{
 \begin{aligned}
 \Xi^{\mathrm{car}}_{m,g}
 ={}&\sum_{q=1}^{g-2}
 \bigl(\min\{G,N_q^-\}-K_q^-\bigr)\\
 &+\sum_{q=1}^{g-1}
 \bigl(\min\{G,N_q^+\}-K_q^+\bigr)\\
 &+\min\{G_0,Q_g\}-K_\partial^-\\
 &+\min\{G_1,Q_g\}-K_\partial^+.
 \end{aligned}}
 \tag{3.8}
\]

Equation (3.8) is the requested exact expression.  It includes all floor
baselines and both odd-dimensional boundary fibres.

For the recursive trace-rainbow packet factor, each macrocell contributes
at most one occurrence to a fixed target, so (3.4) is entirely
cross-macrocell.  That conclusion is false here.  To see the precise
decomposition, write \(n_{\mathcal M,q}^\epsilon(T)\) for the contribution
of macrocell \(\mathcal M\), and let

\[
 s_q^\epsilon(T)
 =\#\{\mathcal M:n_{\mathcal M,q}^\epsilon(T)>0\}.
 \tag{3.9}
\]

Then, target by target,

\[
 (n_q^\epsilon(T)-1)_+
 =\sum_{\mathcal M}
   (n_{\mathcal M,q}^\epsilon(T)-1)_+
 +(s_q^\epsilon(T)-1)_+.
 \tag{3.10}
\]

Thus \(C_q^\epsilon\) is the sum of an intra-macrocell duplicate mass and
a cross-macrocell support duplicate mass.  Section 4 shows that the first
summand alone is linear.

## 4. Common-order support and changed-edge stability

Fix one macrocell \(\mathcal M\).  Let \(F_0\) be the static all-new
reference successor.  It partitions \(\mathcal M\) into \(6^t\)
physical \(Q_h\)-cells.  In every cell the direction word is one common
cyclic order of the \(h\) directions, repeated twice.

### Lemma 4.1 (common-order signed image bound)

For either sign and \(1\le q<h\),

\[
 \left|\operatorname{im}	au_{q,F_0}^\epsilon\right|
 \le6^t h2^{h-q}
 =24^t\frac h{2^q}.
 \tag{4.1}
\]

#### Proof

In one \(Q_h\)-cell, a length-\(q\) window uses a cyclic interval of
\(q\) directions in the common order.  There are at most \(h\) such
direction sets.  After fixing one, the \(h-q\) untouched directions have
\(2^{h-q}\) outside orientations.  The affine face determines both its
physical lower intersection and its physical upper union.  Thus one cell
hits at most \(h2^{h-q}\) targets of either sign.  Summing over the
\(6^t\) cells proves (4.1); physical coincidences between cells can only
decrease the image. \(\square\)

### Lemma 4.2 (changed outgoing edges create at most \(qe\) targets)

Let \(F,F_0\) be permutations of the same finite owner set, and put

\[
 D=\{x:F(x)\ne F_0(x)\},\qquad e=|D|.
 \tag{4.2}
\]

Then for every \(q\ge1\) and either sign,

\[
 \left|\operatorname{im}\tau_{q,F}^\epsilon\right|
 \le
 \left|\operatorname{im}\tau_{q,F_0}^\epsilon\right|+qe.
 \tag{4.3}
\]

#### Proof

A length-\(q\) \(F\)-window can differ from its \(F_0\)-window only if
one of its first \(q\) edge tails belongs to \(D\).  For a prescribed
\(y\in D\) and lag \(j\in\{0,\ldots,q-1\}\), the only possible start is
\(F^{-j}(y)\).  Hence at most \(qe\) starts are affected.  Every
unaffected start has the same complete state window, and hence the same
physical signed target, under \(F\) and \(F_0\).  Each affected start can
add at most one target. \(\square\)

## 5. Exact use of the base-three carry

For fixed syndrome, order the active ports as

\[
 i_1,\ldots,i_t.
 \tag{5.1}
\]

At port \(i_s\), the opposite-shore matching is selected when the
previously updated ternary digits are all zero.  Over a complete ternary
orbit this event has frequency

\[
 3^{-(s-1)}.
 \tag{5.2}
\]

There is one relevant port time per digit in a \(2h\)-step phase lap.
Consequently the exact changed-tail density relative to the static
reference is

\[
 \frac1{2h}\sum_{s=1}^t3^{-(s-1)}
 =\frac{3(1-3^{-t})}{4h}.
 \tag{5.3}
\]

Thus

\[
 e_{\mathcal M}
 =\frac{3(1-3^{-t})}{4h}|\mathcal M|.
 \tag{5.4}
\]

This is where the base-three carry enters the collision audit.  Its
spectral state space is exponentially large, but its physical changed-edge
density is only \(\Theta(1/h)\).

Apply Lemmas 4.1 and 4.2 with (5.4).  For either sign,

\[
 \left|\operatorname{im}\tau_{q,F}^{\epsilon}(\mathcal M)\right|
 \le
 |\mathcal M|
 \left(
 \frac h{2^q}
 +\frac{3q(1-3^{-t})}{4h}
 \right)
 =|\mathcal M|\eta_{h,q}.
 \tag{5.5}
\]

The canonical macrocell partition is owner-disjoint and has total mass
\(G\).  Summing (5.5) over all macrocells gives

\[
 K_q^\epsilon
 \le
 \sum_{\mathcal M}
 \left|\operatorname{im}\tau_{q,F}^{\epsilon}(\mathcal M)\right|
 \le G\eta_{h,q},
 \tag{5.6}
\]

which is (0.9).  Cross-macrocell coincidences only make this upper bound
smaller.

The same proof survives a different legal whole-macrocell block
permutation or affine phase conjugate in every macrocell: conjugate the
static reference simultaneously.  Both the common-order image bound and
the changed-tail count are unchanged.  Correlating these choices between
macrocells cannot improve (5.6), because it holds pointwise for every
integral choice.

## 6. The logarithmic-depth obstruction

Take \(q_*\) as in (0.10).  Then

\[
 \frac h{2^{q_*}}\le\frac1h,
 \qquad
 \frac{3q_*(1-3^{-t})}{4h}
 =O\!\left(\frac{\log h}{h}\right),
 \tag{6.1}
\]

and hence

\[
 \eta_{h,q_*}=o(1).
 \tag{6.2}
\]

In particular, (5.5) maps the \(24^t\) starts of one macrocell to only
\(o(24^t)\) distinct targets.  This proves directly that the carry factor
does not have packet-wide signed shadow injectivity at \(q_*\).

For odd dimension the exact layer ratios are

\[
 \boxed{
 \frac{N_q^-}{W}
 =\prod_{j=0}^{q-1}\frac{m-j}{m+j+2},
 \qquad
 \frac{N_q^+}{W}
 =\prod_{j=0}^{q-1}\frac{m+1-j}{m+1+j}.}
 \tag{6.3}
\]

The second product has first factor one.  Uniformly for
\(q=o(\sqrt m)\), both products are \(1-o(1)\).  More explicitly,

\[
 \log\frac{N_q^-}{W}
 =-\frac{q(q+1)}m+O\!\left(\frac{q^3}{m^2}\right),
 \tag{6.4}
\]

while

\[
 \log\frac{N_q^+}{W}
 =-\frac{q(q-1)}m
 +O\!\left(\frac{q^2}{m^2}+\frac{q^4}{m^3}\right).
 \tag{6.5}
\]

Here \(t\le3B/64=O(m)\), so \(q_*=O(\log m)=o(\sqrt m)\).
Equations (6.3)--(6.5) prove (0.14).

For every \(q\ge1\),

\[
 N_q^-\le N_1^-=W\frac m{m+2},
 \tag{6.6}
\]

and for every \(q\ge2\),

\[
 N_q^+\le N_2^+=W\frac m{m+2}.
 \tag{6.7}
\]

Thus, if

\[
 \frac uW<\frac2{m+2},
 \tag{6.8}
\]

then \(G>N_q^\pm\) for both signs whenever \(q\ge2\).  At \(q_*\),
equation (3.6) therefore simplifies exactly to

\[
 X_{q_*}^\pm=N_{q_*}^\pm-K_{q_*}^\pm.
 \tag{6.9}
\]

If \(q_*\le g-2\), both terms in (6.9) occur among the strict interior
resources of (3.8).  Combining (5.6) and (6.9) gives the finite bound

\[
 \Xi^{\mathrm{car}}_{m,g}
 \ge
 X_{q_*}^-+X_{q_*}^+
 \ge
 N_{q_*}^-+N_{q_*}^+-2G\eta_{h,q_*},
 \tag{6.10}
\]

which proves (0.11).

For (0.13), one has

\[
 g\le t<2g,qquad 2g\le h<4g.
 \tag{6.11}
\]

Therefore \(q_*=O(\log m)<g-2\) for all sufficiently large \(m\).
Equations (0.14), (6.2), and (6.10) prove (0.15).

The obstruction is stronger than a cross-packet collision lower bound.
Indeed, if \(K_{\mathcal M,q}^\epsilon\) is the image size in one
macrocell, its internal duplicate mass is

\[
 |\mathcal M|-K_{\mathcal M,q}^\epsilon.
 \tag{6.12}
\]

Summing (5.5) gives

\[
 C_{q_*}^{\epsilon,\mathrm{internal}}
 \ge G(1-\eta_{h,q_*})=G-o(W).
 \tag{6.13}
\]

Thus the proposed internal-injectivity premise fails by a linear margin.

## 7. Off-by-one, floor, leave, and parity audit

1. **Signed ranks.**  A physical depth-\(q\) lower trace has rank
   \(m-q\), and a physical depth-\(q\) upper trace has rank \(m+q\).
   Odd complementation would pair lower depth \(q\) with upper depth
   \(q+1\), so no complement symmetry is used.  Both signs are proved
   separately.

2. **Interior ranges.**  The product tail leaves lower depths through
   \(g-2\) and upper depths through \(g-1\), plus the two asymmetric
   boundary fibres in (2.3).  Since \(q_*\le g-2\), both obstructing
   layers are strict interior resources.  Neither \(z\)-boundary can
   absorb them.

3. **Actual occurrence floor.**  The floor subtraction is
   \((G-N_q^\epsilon)_+\), determined by the actual good occurrence mass
   \(G\), not by \(W\).  Equation (3.6) is exact in both regimes
   \(G\le N\) and \(G>N\).

4. **Boundary floors.**  The boundary occurrence masses are \(G_0\) and
   \(G_1\), not \(G\).  This is why (3.7) uses
   \(\min\{G_\alpha,Q_g\}\).  Condition (0.6), rather than only
   (6.8), is the audited finite condition for \(\mathcal A_{m,g}=u\).

5. **Cycle and collar factors.**  The cycle length is \(2h3^t\), not
   \(h3^t\).  The number of cycles is \(G/(2h3^t)\).  Multiplication by
   the exact \(2g-2\) collar per cycle gives
   \((g-1)G/(h3^t)\); the two factors of two cancel.

6. **Residual coordinate.**  Reports normalized on a \(2m\)-coordinate
   slice transfer to the present odd setting by retaining the residual
   coordinate as frozen exterior data.  The macrocell support proof is
   fibrewise.  Summing the \(z\)-free and \(z\)-containing fibres gives
   the global mass \(G\), while the physical target counts remain the
   odd quantities (0.12).

7. **Even transfer.**  The established trimmed lift remains exactly

   \[
   \nu(2m+2)\le2\nu(2m+1),
   \qquad
   \binom{2m+2}{m+1}=2W.
   \tag{7.1}
   \]

   It is lossless once an odd coefficient-one bound is known.  It cannot
   repair the failed odd Stage-A collision gate.

8. **Pair energy versus duplicate mass.**  No quadratic pair-energy
   substitution is made.  Equations (3.4)--(3.8) use the raw integer
   duplicate mass \(\sum_T(n(T)-1)_+\), so loads three and above are
   counted correctly.

9. **Cutting cycles cannot enlarge support.**  Partial collars may remove
   some starts, but they cannot add a target outside the full image in
   (5.6).  Hence the logarithmic-depth Hall deficit persists for every
   subset of the carry windows.  The displayed full collar is the clean
   exact composition, not a claim that every cut-dependent finite ledger
   is numerically identical.

## 8. Exact proved boundary and surviving replacement

The following statements are proved.

* The phase-dense carry gives an exact integral middle factor with
  exponentially long literal \(t\)-geodesic cycles.
* Its exact tail-aligned collar is exponentially small as in (2.8).
* Its exact collision-to-\(\nu\) inequality is (0.5), with the complete
  physical floor ledger (3.8).
* The carry successor is not shadow-injective within a macrocell.
* At one logarithmic depth its two physical signed images each have size
  \(o(W)\), while each target layer has size \((1-o(1))W\).
* Consequently its exact baseline-corrected physical excess is at least
  \((2-o(1))W\).

The following is not proved and is the precise remaining escape from this
no-go.

> **Trace-rainbow carry compatibility — UNPROVED.**  On every
> \(\mathcal V^t\) macrocell, construct a legal adjacent-port fusion of
> independently refreshed recursive trace-rainbow \(Q_h\)-factors such
> that the port coordinate is common on each switched owner fibre, all
> cycles have \(o(W/g)\) total component count globally, and the resulting
> physical signed maps have baseline-corrected aggregate excess \(o(W)\)
> through \(q\le g\).

The present base-three carry cannot be inserted into this statement by
assertion: its common phase and syndrome coordinates come from the
parallel common-order factor, while independent recursive refreshing
changes precisely those coordinates.  A new port-compatibility theorem is
required.

## 9. Independent decisive-step audit

The decisive inequality was audited independently in two ways.

1. **Image audit.**  In one static \(Q_h\)-cell, there are at most \(h\)
   cyclic \(q\)-direction intervals and \(2^{h-q}\) outside
   orientations.  Multiplication by \(6^t\), using
   \(6^t2^h=24^t\), gives exactly the first term in (5.5).

2. **Perturbation audit.**  A changed outgoing edge has exactly one
   possible predecessor start at each of the \(q\) lags.  Hence the
   coefficient in Lemma 4.2 is \(q\), not \(2q\).  The geometric series
   in (5.3) is \(\frac32(1-3^{-t})\), and division by the full phase
   length \(2h\) gives \(3(1-3^{-t})/(4h)\).

3. **Odd-floor audit.**  At \(q_*\ge2\), (6.6)--(6.8) give
   \(G>N_{q_*}^\pm\), so no hidden minimum remains:

   \[
   X_{q_*}^\pm=N_{q_*}^\pm-K_{q_*}^\pm.
   \]

   Both terms occur in (3.8).  This independently recovers (6.10).

No constant-one conclusion is claimed.
