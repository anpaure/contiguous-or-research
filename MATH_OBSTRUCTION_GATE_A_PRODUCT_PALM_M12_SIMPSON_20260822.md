# Gate A no-go: an adverse product Palm covariance at carrier order twelve

**Date:** 2026-08-22  
**Status:** exact non-punctured product-law counterexample; it rules out an
abstract mixture-of-FKG sign theorem, not a punctured-specific signed-tail
estimate

## 0. Statement

There is a finite simple hypergraph with independently retained targets at
probability $1/2$, an increasing root-degree test $\Psi$, and ordered
twelve-carriers for which

\[
 \operatorname {Cov}_{\rm Palm}(h_\gamma,\Psi)<0,           \tag{0.1}
\]

even though, for every fixed labelled carrier $\gamma$,

\[
 \operatorname {Cov}(h_\gamma,\Psi
          \mid\gamma\text{ retained})\ge0.                 \tag{0.2}
\]

Thus the fixed-carrier Harris/FKG theorem does not survive the
survival-weighted mixture over carrier labels.  The adverse term is exactly
the between-carrier Simpson covariance.

The construction is not a directed-punctured residual.  It is therefore
not evidence against a punctured-specific $m=12$ signed-tail theorem; it
only proves that such a theorem must use punctured geometry.

## 1. Hypergraph and carrier types

Use mutually distinct target vertices

\[
 v,a,b,\quad s_i,t_i,u_i\ (1\le i\le12),\quad
 x_{ij}\ (1\le i\le12,\ 1\le j\le M).
\]

The root-star rows are

\[
 A_i=\{v,a,s_i,t_i\},\qquad B_i=\{v,b,u_i\}
       \qquad(1\le i\le12),                                \tag{1.1}
\]

and the external rows are

\[
 X_{ij}=\{u_i,x_{ij}\}.                                    \tag{1.2}
\]

Retain every target independently with probability $1/2$, and retain a
row precisely when all of its targets are retained.  An ordered
twelve-carrier is an ordered choice of twelve distinct alive rows from the
24-row root star.  Its hazard $h_\gamma$ is the number of alive rows
meeting at least one carrier row.  Put

\[
                         \Psi=\mathbf1_{\{d_v\ge13\}}.      \tag{1.3}
\]

For a carrier label, let $k$ be the number of selected $B$-rows.
There are $12!\binom{12}{k}^2$ ordered labels of type $k$.  The common
factor $12!$ cancels from the Palm law.  The number of distinct forced
targets is

\[
 b_k=1+\mathbf1_{\{k>0\}}+\mathbf1_{\{k<12\}}
          +k+2(12-k),                                      \tag{1.4}
\]

so the unnormalised type weight and its normalising sum are

\[
 w_k=\binom{12}{k}^2 2^{-b_k},\qquad
 Q=\sum_{k=0}^{12}w_k=\frac{125800033}{67108864},qquad
 \pi_k=\frac{w_k}{Q}.                                      \tag{1.5}
\]

## 2. Conditional degree and hazard profiles

Write

\[
 P_k=\Pr(\Psi=1\mid\gamma\text{ retained, type }k),qquad
 \mu_k=\mathbb E[d_v\mid\gamma\text{ retained, type }k].  \tag{2.1}
\]

For $1\le k\le11$, both common targets $a,b$ are forced.  The
unselected root rows consist of $k$ independent $A$-rows, each alive
with probability $1/4$, and $12-k$ independent $B$-rows, each alive
with probability $1/2$.  Hence

\[
 P_k=1-\left(\frac34\right)^k\left(\frac12\right)^{12-k},
 \qquad \mu_k=18-\frac{k}{4}.                              \tag{2.2}
\]

At the endpoints the unused common target is not forced, giving

\[
 P_0=\frac12(1-2^{-12}),\qquad \mu_0=15,                   \tag{2.3}
\]

\[
 P_{12}=\frac12\left(1-\left(\frac34\right)^{12}\right),
 \qquad \mu_{12}=\frac{27}{2}.                             \tag{2.4}
\]

Every alive root-star row meets every carrier row through $v$.  An
external row $X_{ij}$ meets the carrier exactly when $B_i$ was selected;
then $u_i$ is forced and $X_{ij}$ survives with probability $1/2$.
These external survival indicators are independent of $d_v$ and
$\Psi$.  Therefore

\[
 H_k:=\mathbb E[h_\gamma\mid\gamma\text{ retained, type }k]
       =\mu_k+\frac{kM}{2},                                 \tag{2.5}
\]

and the fixed-carrier covariance receives no external contribution.

Since $d_v=12+Y$ for a nonnegative integer $Y$, while
$\Psi=\mathbf1_{\{Y\ge1\}}$, the fixed-carrier covariance is exactly

\[
 C_k:=\operatorname {Cov}(h_\gamma,\Psi\mid\gamma,k)
      =(1-P_k)(\mu_k-12)\ge0.                              \tag{2.6}
\]

This explicitly verifies (0.2), without using FKG as a black box.

## 3. Exact Simpson calculation

The law of total covariance gives

\[
 \operatorname {Cov}_{\rm Palm}(h_\gamma,\Psi)
 =\sum_{k=0}^{12}\pi_kC_k
   +\operatorname {Cov}_{\pi}(H_k,P_k).                    \tag{3.1}
\]

Direct rational collection of (1.5) and (2.2)--(2.6) gives

\[
 \sum_k\pi_kC_k
 =\frac{40946898723}{2061107740672}>0,                     \tag{3.2}
\]

\[
 \operatorname {Cov}_{\pi}(\mu_k,P_k)
 =\frac{201910008730439973}{259287421793093042176}>0,      \tag{3.3}
\]

but

\[
 \boxed{
 \operatorname {Cov}_{\pi}(k,P_k)
 =-\frac{48859110891261717}{16205463862068315136}<0.}      \tag{3.4}
\]

Substituting $H_k=\mu_k+kM/2$ in (3.1) yields the affine exact formula

\[
 \boxed{
 \operatorname {Cov}_{\rm Palm}(h_\gamma,\Psi)
 =\frac{669128902416437229-48859110891261717M}
        {32410927724136630272}.}                            \tag{3.5}
\]

At $M=13$, the numerator is

\[
 33960460830034908>0,
\]

whereas at $M=14$ it is

\[
 -14898650061226809<0.                                    \tag{3.6}
\]

Thus $M=14$ is the first adverse member of this family and proves (0.1).
The negative contribution comes solely from the survival-weighted
between-carrier term: carriers containing more $B$-rows have more
external hazard, but their conditional upper-tail probability is smaller.

## 4. Consequence for Gate A

The product-law identity

\[
 \operatorname {Cov}_{\rm Palm}(h_\gamma,\Psi)
 =\mathbb E_\pi\operatorname {Cov}(h_\gamma,\Psi\mid\gamma)
   +\operatorname {Cov}_\pi(H_\gamma,P_\gamma)              \tag{4.1}
\]

cannot be closed by discarding the second term.  Even at carrier order
twelve, that term can overwhelm all favorable fixed-carrier covariances.
The remaining directed-punctured theorem must therefore control the
specific signed tail-decorated between-carrier cluster, or the whole
unsplit hazard covariance, using the punctured boundary geometry.
