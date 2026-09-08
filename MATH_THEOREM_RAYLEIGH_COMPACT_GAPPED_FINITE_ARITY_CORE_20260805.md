# Rayleigh residual reduces to a compact, gapped, finite-arity core

**Date:** 2026-08-05  
**Method:** pure mathematics; no search or solver  
**Status:** unconditional exact reduction.  The Gaussian tail can be
removed while preserving the strict two-to-three count window.  One
bottom-quantile primary socket per remaining job then leaves a compact
equal-work pair whose socket and job supports are both bounded away from
zero and whose socket/job count ratio lies strictly between one and two.
Hence every exact completion has a uniform finite arity bound.  Existence
of that final compact completion is not proved here.

## 1. Input pair and its strict count margins

After the first Rayleigh equal-level subtraction and cancellation of the
one-piece overlap, write the separated residual as

\[
 \nu_2(dy)=g_2(y){\bf1}_{(0,b)}dy,
 \qquad
 \mu_2(dx)=f_2(x){\bf1}_{(b,\infty)}dx.
\]

It has equal first moments.  Put

\[
 S=\nu_2(0,b),\qquad J=\mu_2(b,\infty).
\]

The exact count-window theorem proves

\[
 \Delta_2:=S-2J>0,
 \qquad
 \Delta_3:=3J-S>0.                               \tag{1.1}
\]

The job density has a Gaussian tail, while the socket density has positive
terminal lower limit at `b`.  Therefore the equal-split tail theorem
applies with `C=b`.

## 2. Remove a sufficiently remote tail

For `n>=2`, put

\[
 I_n=((n-1)b,nb).
\]

The tail theorem assigns every job `x in I_n` exactly `n+1` equal
sockets of size `x/(n+1)<b`.  For an integer cutoff `N`, define the job
and socket occurrence counts removed by all bands `n>=N`:

\[
 H_J(N)=\sum_{n\ge N}\mu_2(I_n),
 \qquad
 H_S(N)=\sum_{n\ge N}(n+1)\mu_2(I_n).             \tag{2.1}
\]

### Lemma 2.1 (vanishing count load)

As `N` tends to infinity,

\[
 H_J(N)\longrightarrow0,
 \qquad
 H_S(N)\longrightarrow0.                         \tag{2.2}
\]

### Proof

The transformed job density satisfies

\[
 f_2(x)\le C(1+x)e^{-x^2}
\]

for all sufficiently large `x`.  On `I_n`, one has `x>(n-1)b`, so

\[
 (n+1)\mu_2(I_n)
 \le C_1(n+1)^3e^{-C_2(n-1)^2}
\]

for fixed positive constants `C_1,C_2`.  The right side is summable.
Its tails tend to zero, proving the second limit; the first is weaker.
`square`

Choose `N>=3` sufficiently large that both

1. the pointwise equal-split socket demand of all bands `n>=N` is a
   submeasure of `nu_2`, as supplied by the tail theorem; and
2.

   \[
   H_S(N)-2H_J(N)<\Delta_2.                       \tag{2.3}
   \]

Remove those explicit job configurations and their socket marginal.  Let
the remaining compact pair be `(mu_c,nu_c)`, and put

\[
 J_c=J-H_J(N),\qquad S_c=S-H_S(N).
\]

It still has equal first moments and

\[
 \operatorname {supp}\mu_c\subseteq[b,(N-1)b],
 \qquad
 \operatorname {supp}\nu_c\subseteq[0,b].        \tag{2.4}
\]

Moreover,

\[
\begin{aligned}
 S_c-2J_c
 &=\Delta_2-\bigl(H_S(N)-2H_J(N)\bigr)>0,\\
 3J_c-S_c
 &=\Delta_3+\bigl(H_S(N)-3H_J(N)\bigr)>0.         \tag{2.5}
\end{aligned}

The final inequality uses `n+1>=4` on every removed band, so

\[
 H_S(N)-3H_J(N)
 =\sum_{n\ge N}(n-2)\mu_2(I_n)\ge0.
\]

Thus the compact remainder retains the exact window

\[
 \boxed{2J_c<S_c<3J_c.}                           \tag{2.6}
\]

## 3. A bottom-quantile primary socket

The measure `nu_c` is atomless.  Since `S_c>2J_c`, its bottom cumulative
mass reaches `J_c` at some cutoff

\[
 0<q<b.
\]

Choose a bottom submeasure `kappa` of mass `J_c`, supported in `(0,q]`,
and put

\[
 \lambda=\nu_c-\kappa.
\]

Then `lambda` is supported in `[q,b]` and has mass `S_c-J_c`.

Couple `kappa` arbitrarily to `mu_c`, and replace each coupled pair
`(x,y)` by the remainder

\[
 z=x-y.
\]

Let `gamma` be the remainder-job measure.  The bottom-quantile reduction
gives

\[
 \int z\,d\gamma(z)=\int y\,d\lambda(y),          \tag{3.1}
\]

and every completion of `(gamma,lambda)` lifts by reattaching the primary
socket `y`.  Its supports satisfy

\[
 \operatorname {supp}\gamma
 \subseteq[b-q,(N-1)b],
 \qquad
 \operatorname {supp}\lambda\subseteq[q,b].      \tag{3.2}

Both lower endpoints are strictly positive.  Its count window is

\[
 \gamma(0,\infty)=J_c,
 \qquad
 \lambda(0,\infty)=S_c-J_c,
\]

so (2.6) becomes

\[
 \boxed{
 J_c<\lambda(0,\infty)<2J_c.}                    \tag{3.3}
\]

## 4. Uniform finite arity

### Theorem 4.1 (compact gapped core)

The original Rayleigh continuum coagulation reduces exactly to the pair
`(gamma,lambda)` of Section 3.  This terminal pair has equal work,
compact support bounded away from zero, and socket/job count ratio strictly
between one and two.

In every exact coagulation of this pair, every configuration has at most

\[
 \boxed{
 R=\left\lfloor{(N-1)b\over q}\right\rfloor}      \tag{4.1}
\]

socket occurrences.

### Proof

All preceding operations are exact configuration kernels and have exact
lifting maps, so only the arity assertion remains.  Every socket in a
terminal configuration has size at least `q`, every remainder job has size
at most `(N-1)b`, and configuration sums are exact.  A configuration with
`r` sockets therefore satisfies

\[
 rq\le z\le(N-1)b,

\]

which gives `r<=R`.  `square`

Thus the residual is no longer an unbounded-tail or vanishing-socket
problem.  Its exact dual has only the finite arity list

\[
 1,2,\ldots,R.
\]

The count row says only that its average arity lies in `(1,2)`; it does
not exclude a positive mass of arity at least three balanced by one-socket
configurations.  Proving feasibility of this finite-arity compact
configuration hypergraph remains necessary.

## 5. Scope

This theorem does not prove the final compact configuration inequalities.
In particular, compact support, positive lower support, equal work, and
the count window do not imply configuration feasibility for arbitrary
measures.  The gain is an exact normalization:

\[
 \boxed{
 \text{unbounded Gaussian pair}
 \longrightarrow
 \text{compact pair with }0<q\le y\le b,
 \ 0<b-q\le z\le(N-1)b,
 \ 1<{\#\text{sockets}\over\#\text{jobs}}<2.
 }
\]

## 6. Frozen dependencies

1. `MATH_THEOREM_RAYLEIGH_ONE_SHOT_NORMALIZATION_GAUSSIAN_TAIL_AND_COMPACT_REMAINDER_20260805.md`.
2. `MATH_THEOREM_RAYLEIGH_UNIFORM_LAYER_PACKET_TRANSPORT_AND_EQUAL_SPLIT_GATE_20260805.md`.
3. `MATH_THEOREM_BOTTOM_QUANTILE_GAPPED_PRIMARY_SOCKET_REDUCTION_20260805.md`,
   SHA at use
   `8e794543a946e8202b31d4861b84f357d114171a2700e86ee23441599a3e15e9`.
4. `MATH_THEOREM_RAYLEIGH_FIRST_TRANSFORM_EXACT_TWO_THREE_COUNT_WINDOW_20260805.md`,
   SHA at use
   `1931d629efdcf12c2ec0167a004ead83e547050d44bc23464252dc0a1e062a10`.

