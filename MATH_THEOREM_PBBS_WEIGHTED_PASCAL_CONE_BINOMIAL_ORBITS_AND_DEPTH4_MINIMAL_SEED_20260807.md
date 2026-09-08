# The Pascal distance transfer has an exact binomial invariant cone; the minimal depth-four seed is not the Pascal pair

**Date:** 2026-08-07  
**Status:** unconditional weighted-state theorem, unconditional exact
depth-four invariant cone, and exact limitation.  The result supplies the
correct weighted replacement for false standalone pair positivity.  It
does not prove $FC_D$ at any previously unresolved depth.

## 1. Individual distance states and the transfer operator

For an integer distance $s$, define the complete signed-tail state

\[
 G_s^{R,D}(u)
 =\Gamma^{(2R,R+s,R+s-D)}(u).
 \tag{1.1}
\]

The state is allowed to be formal when a shifted owner rank is off the
physical middle line.  Applying Pascal twice gives

\[
 \boxed{
 G_s^{R,D}=G_{s+1}^{R-1,D}
             +2G_s^{R-1,D}+G_{s-1}^{R-1,D}.}
 \tag{1.2}
\]

Let $w=(w_s)_{s\in\mathbb Z}$ be a finite, even, nonnegative weight
profile.  For a closed covering price $\psi$, put

\[
 \mathcal M_{R,D}(w;\psi)
 =\sum_{s\in\mathbb Z}w_s
   \sum_{u\ge1}G_s^{R,D}(u)
       \bigl(\psi(u)-\psi(u-1)\bigr).
 \tag{1.3}
\]

Thus $w_0$ is the central-state weight and, for $s>0$, the common value
$w_s=w_{-s}$ is the coefficient of the symmetric pair at distance $s$.
Define

\[
                         (Tw)_s=w_{s-1}+2w_s+w_{s+1}.
 \tag{1.4}
\]

### Theorem 1.1 (weighted invariance)

For every finite even profile $w$ and every closed price $\psi$,

\[
 \boxed{
 \mathcal M_{R,D}(w;\psi)
 =\mathcal M_{R-1,D}(Tw;\psi).}
 \tag{1.5}
\]

#### Proof

Multiply (1.2) by $w_s$ and sum over $s$.  The coefficient of
$G_t^{R-1,D}$ is $w_{t-1}+2w_t+w_{t+1}=(Tw)_t$.  Pairing with the price
increments proves (1.5). \(\square\)

## 2. Laurent solution and the forced binomial weights

Associate to $w$ the Laurent polynomial

\[
                         W(z)=\sum_sw_sz^s.
 \tag{2.1}
\]

Then

\[
                         T:W(z)\longmapsto
                         (z+2+z^{-1})W(z).
 \tag{2.2}
\]

Starting from one middle state, $W_0(z)=1$, the unique finite-support
orbit is

\[
 W_N(z)=(z+2+z^{-1})^N
       =z^{-N}(1+z)^{2N},
 \tag{2.3}
\]

so

\[
 \boxed{
 b_s^{(N)}={2N\choose N+s}.}
 \tag{2.4}
\]

In particular the first two-step descent has central weight two and
distance-one pair weight one.  Repeated Pascal expansion, equivalently
Vandermonde's identity, gives the stronger state identity

\[
 \boxed{
 \sum_{s=-N}^{N}{2N\choose N+s}G_s^{R,D}
 =\Gamma^{(2(R+N),R+N,R+N-D)}.}
 \tag{2.5}
\]

Indeed, a child of owner rank $R+s$ uses $N-s$ of the $2N$ removed
coordinates, and
${2N\choose N-s}={2N\choose N+s}$.  The birth rank descends by the
same amount, from $R+N-D$ to $R+s-D$.

The conic hull of the profiles $b^{(N)}$ is therefore transfer-invariant:

\[
                         Tb^{(N)}=b^{(N+1)}.
 \tag{2.6}
\]

For every price, its aggregate margin is exactly the margin of the
undecomposed higher-dimensional middle state.  Thus whenever that parent
has $FC_D$, every fan-ray margin on the binomial aggregate is
nonnegative.

This is the unique finite-support exact representation of a repeatedly
descended middle state: (2.2) fixes every coefficient.  Formal geometric
eigenprofiles also exist,

\[
 w_s=z^s+z^{-s}\quad(z>0),
 \qquad Tw=(2+z+z^{-1})w,
 \tag{2.7}
\]

but they have infinite support.  No nonzero finite-support eigenprofile
exists, because $T$ creates a nonzero coefficient one step beyond each
extreme support point.  For finite physical states, the binomial orbit,
not a geometric eigenvector, is the canonical solution.

## 3. The general price-positive weight cone

Let $\Psi_D=\{\psi_1,\ldots,\psi_m\}$ be the extreme rays of the
fixed-depth min-plus fan.  Define

\[
 \mathcal W_{R,D}
 =\left\{w\ge0:\ w_s=w_{-s},
 \mathcal M_{R,D}(w;\psi_i)\ge0
 \text{ for }1\le i\le m\right\}.
 \tag{3.1}
\]

At every fixed $D$ this is a rational polyhedral cone: the min-plus fan
is finite, and each displayed condition is linear in $w$.  Theorem 1.1
gives the exact invariant-cone relation

\[
 \boxed{
                         T\mathcal W_{R,D}
                         \subseteq\mathcal W_{R-1,D}.}
 \tag{3.2}
\]

This is not a definition-only tautology about individual pairs.  A weight
profile may combine negative pair margins with positive central margins;
(1.5) preserves the aggregate exactly.  It is the smallest natural
polyhedral state space visible to all price rays simultaneously.

The binomial profiles are distinguished elements of this cone whenever
their undecomposed parents have $FC_D$, by (2.5).  Conversely, (2.5)
shows the limitation: binomial weighting alone cannot prove an unknown
parent inequality, because its aggregate inequality is exactly that
parent inequality.

## 4. Exact minimal support-one seed at depth four

Use the actual depth-four state with $R=24$, so its central state is
$(k,r,t)=(48,24,20)$.  Let

\[
 c_i=\mathcal M_{24,4}(\delta_0;\psi_i)=M_{48}(\psi_i),
 \tag{4.1}
\]

and let $p_i$ be the margin of the distance-one symmetric pair.  The
two-step decomposition of the actual parent $(50,25,21)$ gives

\[
                         p_i=M_{50}(\psi_i)-2M_{48}(\psi_i).
 \tag{4.2}
\]

Every $c_i$ is positive.  Among the thirteen depth-four fan rays, only
$p_3,p_5,p_8,p_9$ are negative.  Therefore a support-one profile

\[
 w_0=\alpha,
 \qquad w_1=w_{-1}=1,
 \qquad w_s=0\quad(|s|\ge2)
 \tag{4.3}
\]

lies in $\mathcal W_{24,4}$ if and only if

\[
 \alpha\ge
 \max_{i\in\{3,5,8,9\}}{-p_i\over c_i}.
 \tag{4.4}
\]

The four exact candidate ratios are

\[
\begin{array}{c|c|c}
i&-p_i/c_i&\text{decimal guide}\\ \hline
3&93372827081/1092355086432&0.08548\\
5&570294445018/4264498187717&0.13373\\
8&2855680888673/4376728218623&0.65247\\
9&65359876165/440252087683&0.14846
\end{array}
 \tag{4.5}
\]

Direct cross-multiplication shows that ray 8 is the maximum.  Hence the
exact minimal central subsidy is

\[
 \boxed{
 \rho_*={2855680888673\over4376728218623}.}
 \tag{4.6}
\]

Equivalently, the entire support-one section of the price-positive cone is

\[
 \boxed{
 \mathcal W_{24,4}\cap\{w_s=0:|s|\ge2\}
 =\operatorname{cone}\{\delta_0,w^*\},}
 \tag{4.7}
\]

where $w^*_0=\rho_*$ and $w^*_{1}=w^*_{-1}=1$.  The linear volume ray
is tight at $w^*$; every other depth-four ray is nonnegative.  The exact
Pascal profile $(w_0,w_1)=(2,1)$ lies well inside this cone, but it is not
the minimal price-positive weighting.

There is a symbolic reason for the binding ray.  For the linear volume
price, let $V_{2r,D}$ be the complete middle-state margin in dimension
$2r$.  With

\[
 W_c={2r-2\choose r-1},
 \tag{4.8}
\]

the central-child and distance-one-pair volume margins are exactly

\[
\begin{aligned}
 V_{2r-2,D}
   &=(D+\tfrac12)W_c-2^{2r-3}+1,\\
 P^{\rm vol}_{r,D}
   &=V_{2r,D}-2V_{2r-2,D}\\
   &=(2D+1){r-1\over r}W_c-4^{r-1}-1.
\end{aligned}
 \tag{4.9}
\]

Thus every support-one positive cone at these parameters necessarily has

\[
 \alpha\ge
 \rho^{\rm vol}_{r,D}:=
 \max\left(0,{-P^{\rm vol}_{r,D}\over V_{2r-2,D}}\right).
 \tag{4.10}
\]

Formula (4.9) follows from

\[
 \sum_{j=1}^{r-1}{2r\choose j}
 =2^{2r-1}-{1\over2}{2r\choose r}-1
 \tag{4.11}
\]

and
${2r\choose r}/{2r-2\choose r-1}=4-2/r$.
The complete fan calculations through depth four show that this necessary
volume bound is also sufficient at the last even row of each nontrivial
depth block:

\[
\begin{array}{c|c|c|c}
D&2r&\rho^{\rm vol}_{r,D}&\text{binding fan ray}\\ \hline
2&14&137/263&L\\
3&30&6340337/6190373&L\\
4&50&2855680888673/4376728218623&L
\end{array}
 \tag{4.12}
\]

For all earlier even parent/child pairs within those same depth blocks,
the complete paired margins are already nonnegative, so the minimum is
$\alpha=0$.  This finite theorem suggests a concrete all-depth target:
prove that the volume lower bound (4.10) controls every other min-plus fan
ray.  It is not asserted here beyond $D\le4$.

## 5. Symbolic orbit of the minimal seed

The smallest transfer-invariant cone generated by the complete
support-one section has two explicit rays at descent time $n$:

\[
                         T^n\delta_0=b^{(n)},
 \qquad T^nw^*=w^{*,(n)}.
 \tag{5.1}
\]

Their second Laurent polynomial is

\[
 W_n^*(z)=z^{-n}(1+z)^{2n}
             (\rho_*+z+z^{-1}),
 \tag{5.2}
\]

and hence

\[
 \boxed{
 w_s^{*,(n)}=
 \rho_*{2n\choose n+s}
 +{2n\choose n+s-1}
 +{2n\choose n+s+1}.}
 \tag{5.3}
\]

All coefficients are nonnegative and symmetric.  More importantly,
Theorem 1.1 gives, for every one of the thirteen depth-four rays,

\[
 \boxed{
 \mathcal M_{24-n,4}(w^{*,(n)};\psi_i)
 =\mathcal M_{24,4}(w^*;\psi_i)\ge0.}
 \tag{5.4}
\]

Thus

\[
 \mathcal C_n=
 \operatorname{cone}\{b^{(n)},w^{*,(n)}\}
 \subseteq\mathcal W_{24-n,4},
 \qquad T\mathcal C_n=\mathcal C_{n+1}.
 \tag{5.5}
\]

This is an exact, nontrivial weighted invariant cone.  It permits the
outer pair to have negative margins and carries precisely the necessary
central subsidy.  For $0\le n\le9$, every shifted owner and birth rank in
its support remains physical; beyond that range the algebraic identity
continues with the usual formal-state convention.

## 6. Exact conclusion

There are two different notions of minimality, and conflating them hides
the real induction gate.

1. Exact repeated decomposition of one middle parent uniquely forces the
   binomial weights ${2N\choose N+s}$.
2. Price positivity needs less central mass.  At the first actual
   depth-four test, the exact minimum is the volume-bound ratio $\rho_*$,
   and its binomial convolution orbit gives the smaller invariant cone
   (5.5).

The construction generalizes mechanically at every fixed depth: classify
the finite min-plus fan, form the rational cone (3.1), extract its small
support extreme seeds, and propagate them symbolically by (2.2).  What is
not yet proved is a dimension-uniform description of those seed cones as
$D$ grows, or an invariant showing that every new actual middle state
enters them without first verifying its own fan-ray margins.  That is the
remaining noncircular all-depth problem.
