# Exact factor heat-bath identity

## 1. Interaction-component resampling

Let `F` be any exact middle wreath factor on `n=2m+1` coordinates and let
`tau` be a coordinate transposition.  Form the bipartite interaction
multigraph between `F` and `tau F`, with one edge for every middle mask.
For a connected component `K`, write

\[
             L_K=K\cap F,\qquad R_K=K\cap\tau F.
\]

The two order families `L_K,R_K` cover exactly the same middle masks.  Hence
choosing independently, for every component, either `L_K` or `R_K` always
gives another exact middle factor.  Call this one **heat-bath step**.

For rank `r`, put

\[
 c_r(F)=B_r{\bf1}_F,
 \qquad
 \Delta_{K,r}=B_r({\bf1}_{R_K}-{\bf1}_{L_K}).          \tag{1.1}
\]

## 2. Exact mean and covariance

### Theorem 1 (factor heat-bath identity)

If `G` is obtained by choosing every component side by an independent fair
coin, then

\[
 \boxed{
   \mathbb E[c_r(G)\mid F,\tau]
       ={c_r(F)+\tau c_r(F)\over2}.}                  \tag{2.1}
\]

Moreover,

\[
 \boxed{
 \operatorname {Cov}(c_r(G)\mid F,\tau)
       ={1\over4}\sum_K
          \Delta_{K,r}\Delta_{K,r}^{\mathsf T}.}      \tag{2.2}
\]

For two ranks `r,s`, the cross-covariance is

\[
 \operatorname {Cov}(c_r(G),c_s(G)\mid F,\tau)
       ={1\over4}\sum_K
          \Delta_{K,r}\Delta_{K,s}^{\mathsf T}.       \tag{2.3}
\]

#### Proof

Write `epsilon_K` for independent uniform signs, with `+1` selecting `R_K`.
Then

\[
 c_r(G)=\frac12\sum_K
   \bigl(B_r{\bf1}_{L_K}+B_r{\bf1}_{R_K}\bigr)
   +\frac12\sum_K\epsilon_K\Delta_{K,r}.              \tag{2.4}
\]

The left component sides partition `F`, and the right sides partition
`tau F`.  Equivariance gives

\[
                 B_r{\bf1}_{\tau F}=\tau c_r(F).
\]

Taking expectations in (2.4) proves (2.1).  Independence and
`E epsilon_K epsilon_J=1_(K=J)` give (2.2), and the identical calculation at
two ranks gives (2.3).  QED.

Thus component resampling is not merely an abstract exact-factor move.  Its
mean performs one coordinate-transposition averaging step on every vertical
rank simultaneously, while its entire rounding error is the explicit sum of
component effect covariances.

## 3. Exact quadratic-energy ledger

Let

\[
                    f_r=c_r(F)-\mu_r{\bf1},
 \qquad \mu_r={\binom nm\over\binom nr}.
\]

Since the constant vector is fixed by `tau`, Theorem 1 gives

\[
\begin{aligned}
 \mathbb E\|c_r(G)-\mu_r{\bf1}\|_2^2
  ={}&\left\|{f_r+\tau f_r\over2}\right\|_2^2
       +{1\over4}\sum_K\|\Delta_{K,r}\|_2^2\\
  ={}&\|f_r\|_2^2
       -{1\over4}\|f_r-\tau f_r\|_2^2
       +{1\over4}\sum_K\|\Delta_{K,r}\|_2^2.        \tag{3.1}
\end{aligned}
\]

The first negative term is the exact Johnson/random-transposition smoothing
gain.  The final positive term is the integrality noise.  If the interaction
graph is one giant component, its effect vector is the whole difference and
the two terms cancel: the heat bath merely chooses `F` or `tau F`.  Fine
component fragmentation is exactly what can make the rounding noise smaller
than the continuous smoothing gain.

For several ranks with weights `w_r>=0`, summing (3.1) gives the identical
multirank ledger

\[
 \Delta\mathcal E
 =-{1\over4}\sum_r w_r\|f_r-\tau f_r\|_2^2
   +{1\over4}\sum_K\sum_r w_r\|\Delta_{K,r}\|_2^2.  \tag{3.2}
\]

This is an exact quantitative form of the component-frame requirement.

## 4. Exact missing-event formula inside one cube

Fix a target mask `S`.  For a component `K`, let `a_K(S)` and `b_K(S)` be
its occurrence counts on `L_K` and `R_K`.  If some component has both counts
positive, then `S` occurs after every switch choice.  Otherwise let

\[
 d_S=\#\{K:\text{exactly one of }a_K(S),b_K(S)
                    \text{ is positive}\}.
\]

If no component has both counts positive, independent fair resampling gives

\[
 \boxed{
        \Pr(S\text{ is missing from }G\mid F,\tau)=2^{-d_S}.}
                                                               \tag{4.1}
\]

Indeed, every one-sided component forces one independent coin value for the
target to be absent, while components with two zero counts impose no
condition.  This formula is valid with arbitrary positive occurrence
multiplicities; only their zero/nonzero status matters.

For a family of targets `A`, conditional expectation gives

\[
 \mathbb E\,\#\{S\in A:S\text{ missing}\}
 =\sum_{S\in A:\,a_K(S)b_K(S)=0\ \forall K}2^{-d_S}.  \tag{4.2}
\]

Hence a deterministic cube vertex has no more missing targets than the
right side.  The remaining combinatorial task is now transparent: prove
that the contextual MSW component charts give large flexibility `d_S` for
all but `o(W)` central-band targets, using several prefix-free transposition
families to handle targets invariant under any one transposition.

## 5. Limitation of one transposition

If `tau S=S` (the target contains both exchanged coordinates or neither),
then `c_r(tau F)_S=c_r(F)_S`.  A one-transposition cube may still rearrange
which component contains an occurrence, but its two total endpoint counts
agree, and a missing target remains missing on both sides of the entire
trade.  In particular, no theorem based on one fixed transposition alone can
repair targets absent from both `F` and `tau F`.

For a central-rank target and a uniform coordinate pair, the invariant event
has probability asymptotic to `1/2`.  A complete proof therefore needs
several coordinate pairs, or the recursive contextual charts at different
Dyck boundaries.  This is the precise role of multirank absorption/stability;
it is not removable by analyzing the root `(2 3)` cube more sharply.

