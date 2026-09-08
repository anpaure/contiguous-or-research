# Fixed additive slack does not change the two-SCD Gaussian fragmentation

**Date:** 2026-08-04  
**Status:** unconditional asymptotic corollary for every fixed additive
charge.  It does not construct the required chain fragmentation, prove the
configuration-price inequalities, or prove literal cross-SCD containment.

## 0. Result

Let `k=2r`, let `d=d(2r)` be the coefficient-one depth, and fix an integer
`C>=0` independent of `r`.  Put

\[
 h=d+C,
 \qquad t_C=r-h,
 \qquad A={\sqrt\pi\over2}.                         \tag{0.1}
\]

Use one SCD above `t_C` as the collar and cut the chains of a second SCD
below `t_C` into chunks of length at most `h`.  If the chunks pass all
anonymous socket-capacity threshold cuts, then their scaled empirical
measure converges to

\[
 \boxed{
 d\mu(y)=2(A-y)e^{-(A-y)^2}\,dy,
 \qquad 0<y<A.}                                     \tag{0.2}
\]

This is exactly the same measure forced at charge zero.  Consequently:

1. every fixed-`C` minimum-number-of-chunks rule fails by `Omega(W)`;
2. every successful rule still needs a positive-density bank of additional
   cuts; and
3. every literal matching is asymptotically capacity-diagonal.

Thus a constant additive charge can repair only the `W`-scale
configuration/residue and occurrence-correlation layer.  It cannot buy a
different leading `W sqrt(r)`-scale chain geometry.

## 1. Shifted row and socket measures

Write

\[
 C_s={2r\choose s},\qquad W=C_r,
 \qquad H_b=C_b-C_{b-1}.                            \tag{1.1}
\]

The residual bank contains only the nonempty ranks \(1,\ldots,t_C-1\).
Hence a chain beginning at rank \(b<t_C\) has residual length

\[
 L_b=t_C-b-\mathbf 1_{\{b=0\}}.                    \tag{1.2}
\]

The correction at \(b=0\) removes the empty set. It has mass \(1/W\) and
does not affect any Gaussian limit, but it is needed for the exact vacancy
identity in Section 3. Define

\[
 \nu_{r,C}={1\over W}\sum_{b=0}^{t_C-1}H_b
       \delta_{L_b/\sqrt r}.                        \tag{1.3}
\]

The collar supplies `H_(t_C+u)` owner sockets of capacity `u`, and the
endpoint triangle supplies one additional socket of each capacity
`1,...,h`.  Define

\[
 \mu_{r,C}={1\over W}\sum_{u=1}^{h}(H_{t_C+u}+1)
       \delta_{u/\sqrt r}.                          \tag{1.4}
\]

### Lemma 1.1 (fixed shifts disappear in Gaussian scaling)

For every fixed `C`,

\[
 \nu_{r,C}\Longrightarrow
 2(A+x)e^{-(A+x)^2}\,dx\quad(x>0),                 \tag{1.5}
\]

and

\[
 \mu_{r,C}\Longrightarrow\mu.                     \tag{1.6}
\]

#### Proof

The coefficient-one depth satisfies

\[
 {d\over\sqrt r}\longrightarrow A.
\]

Therefore `(d+C)/sqrt(r)->A`.  For fixed `x>=0`, telescoping the SCD start
counts gives

\[
 \nu_{r,C}([x,\infty))
 ={C_{t_C-\lceil x\sqrt r\rceil}\over W}+o(1)
 \longrightarrow e^{-(A+x)^2}.                    \tag{1.7}
\]

For `0<y<A`, the socket tail similarly satisfies

\[
 \mu_{r,C}([y,A+o(1)])
 ={W-C_{t_C+\lceil y\sqrt r\rceil-1}\over W}+o(1)
 \longrightarrow1-e^{-(A-y)^2}.                   \tag{1.8}
\]

The \(h=O(\sqrt r)\) boundary atoms have total mass \(o(1)\). Differentiating
the two limiting tails proves (1.5)--(1.6). Gaussian tail domination gives
tightness.  \(\square\)

## 2. The extra capacity is second order

Let

\[
 \sigma_0=dW+{d+1\choose2}-\Lambda,
 \qquad 0\le\sigma_0<W+d,                          \tag{2.1}
\]

where the upper bound follows from the minimality of `d`.  At depth
`h=d+C`, the exact scalar vacancy is

\[
 \begin{aligned}
 \sigma_C
 &=hW+{h+1\choose2}-\Lambda\\
 &=\sigma_0+CW+Cd+{C(C+1)\over2}.                  \tag{2.2}
 \end{aligned}
\]

Hence, for fixed `C`,

\[
                         \sigma_C=O(W),
 \qquad {\sigma_C\over W\sqrt r}\longrightarrow0. \tag{2.3}
\]

The job and socket first moments at the scaled normalization therefore
still agree in the limit.

## 3. Fixed-charge rigidity theorem

For a declared cutting, let

\[
 \eta_{r,C}={1\over W}\sum_F
       \delta_{|F|/\sqrt r}.                        \tag{3.1}
\]

### Theorem 3.1

Suppose there is one sequence \(\epsilon_r\to0\) such that, simultaneously
for every integer \(1\le q\le h\),

\[
 \#\{F:|F|\ge q\}
 \le \#\{\text{sockets of capacity at least }q\}
      +\epsilon_rW.                                \tag{3.2}
\]

Then

\[
                         \eta_{r,C}\Longrightarrow\mu.           \tag{3.3}
\]

#### Proof

The threshold at \(q=\lceil y\sqrt r\rceil\), together with (1.8), gives
every subsequential limit \(\eta\) the tail domination

\[
                         \eta([y,A])\le\mu([y,A])
 \qquad(y>0).                                       \tag{3.4}
\]

The chunks partition all residual targets, so

\[
 \sum_F|F|=\sum_{s=1}^{t_C-1}C_s.
\]

Discrete summation by parts gives total socket capacity

\[
 \sum_{u=1}^{h}u(H_{t_C+u}+1)
 =hW-\sum_{s=t_C}^{r-1}C_s+{h+1\choose2}.
\]

The difference is exactly \(\sigma_C\); the rank-zero correction in (1.2)
is what makes the identity exact. Equations (1.6) and (2.3) give

\[
                         \int x\,d\eta(x)=\int y\,d\mu(y).        \tag{3.5}
\]

Integrating (3.4) over \(y\) and using (3.5), the nonnegative tail difference
has integral zero. Tail continuity at non-atoms, followed by one-sided
approximation, gives equality of every positive tail. The \(q=1\) threshold
and (1.6) forbid an additional atom at zero. Thus \(\eta=\mu\); uniqueness
of every subsequential limit proves (3.3). The uniform \(\epsilon_rW\)
error disappears after normalization.
\(\square\)

### Corollary 3.2 (minimum-piece rules still fail)

The minimum possible number of pieces in a residual row of length `L` is
`ceil(L/h)`.  Since `h/sqrt(r)->A`, its limiting total chunk count is

\[
 p_{\min}=\sum_{m\ge1}e^{-\pi m^2/4}<0.501.          \tag{3.6}
\]

But Theorem 3.1 forces

\[
 \mu((0,A))=1-e^{-\pi/4}>0.544.                    \tag{3.7}
\]

Therefore every minimum-piece rule violates some threshold by
`Omega(W)`, for every fixed `C`.

### Corollary 3.3 (fixed-charge capacity diagonality)

In any literal attachment, write `u_F` for the capacity receiving chunk
`F`.  Count the whole capacity of every unused socket as waste.  Then

\[
 \sum_F(u_F-|F|)+\sum_{R\ \mathrm{unused}}u_R=\sigma_C=O(W).    \tag{3.8}
\]

For every fixed `epsilon>0`, at most

\[
 {\sigma_C\over\epsilon\sqrt r}=o(W)                \tag{3.9}
\]

sockets are unused at capacity at least `epsilon sqrt(r)` or have matched
slack at least `epsilon sqrt(r)`.  Thus every macroscopic joint limit is
supported on the diagonal and has both marginals equal to `mu`.

## 4. Exact frontier for `B+O(1)`

For the two-SCD route, fixed additive slack does not weaken the leading
fragmentation theorem.  A proof of `nu(k)<=B(k)+O(1)` through this route
still needs:

1. a positive-density, chain-dependent composition realizing `mu`;
2. all nonconcave finite configuration-price inequalities and an integral
   pattern selection;
3. literal containment Hall for a jointly chosen residual/collar SCD pair;
4. countdown/source-word serialization; and
5. co-instantiation with residence, upper witnesses, seam, and common cap.

The constant charge is available only for the second-order discrepancy of
those steps.  No item above is asserted here.
