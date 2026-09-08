# Corrected triangular pull-clock theorem

Date: 2026-08-01  
Status: proof of the stationary fractional marked-trace gate for the
left-filled optimal Ferrers boundary.  This does not perform integral
one-owner rounding, component fusion, or upper-carrier construction.

## 1. Statement

Let

\[
 r=\lceil k/2\rceil,\qquad W=\binom{k}{r},\qquad
 d=\min\left\{t:tW+\binom{t+1}{2}\ge
                    \sum_{s=1}^{r-1}\binom{k}{s}\right\}.
\]

Let `b_s` be the column multiplicities obtained by filling the triangular
Ferrers boundary from left to right, and set

\[
 q_s=\frac{\binom{k}{s}-b_s}{W}\qquad(1\le s<r).
\]

Then the residual vector `q` has a stationary literal marked-trace
circulation of depth `d`.  In the notation of the research handoff,

\[
                         \boxed{q\in ST_{k,r,d}}.
\]

The submitted pull-clock argument had the correct construction but not a
valid sign chain: its displayed inequalities (14), (16), (18), (19), (27),
and (28) point in the wrong direction.  The corrected inequalities below
prove the desired nonnegativity and packing bound.

## 2. Pull tiles and the telescoping decomposition

Put

\[
 c=r-d-1,
 \qquad A_t=q_{c-t+1}\ (1\le t\le c),
 \qquad P=\sum_{t=1}^c A_t,
\]

and

\[
 G_j=1-q_{c+j}\ (1\le j\le d),
 \qquad H=\sum_{j=1}^dG_j.
\]

The scalar boundary identity is

\[
                         H-P=d-\sum_{s=1}^{r-1}q_s\ge0.       \tag{2.1}
\]

Assume first that `H>0`, and define

\[
 w_j=G_j/H,\qquad w_{d+1}=w_{d+2}=0,
 \qquad \Delta_j=w_j-w_{j+1}.
\]

A pull block of type `(delta,j)` is represented by the staircase

\[
 S_{\delta,j}=\{(t,q):1\le t\le\delta,
                         1\le q\le j-\delta+t\}.
\]

Its row sums are the newly supplied low ranks and its column sums are the
net high-rank deficits (including the high-band values to which longer
windows fall).  Define

\[
 x_{\delta,j}=A_\delta\Delta_j-A_{\delta+1}\Delta_{j+1},
 \qquad A_{c+1}=0.                                      \tag{2.2}
\]

For every cell `(t,q)`, two telescoping sums give

\[
 \sum_{\delta=t}^{c}\sum_{j=q+\delta-t}^{d}x_{\delta,j}
       =A_tw_q.                                         \tag{2.3}
\]

Thus, once `x` is nonnegative, the product coupling `A_t w_q` is exactly a
nonnegative combination of literal pull staircases.

## 3. Correct nonnegativity inequalities

For all sufficiently large `k`, `c>d`; this follows from the established
explicit `d=O(sqrt(k))`/Wallis bound.  Hence the Ferrers correction is below
the high band.  The finitely many remaining values are handled in Section 5.

Set

\[
                         \rho=\frac{k-c+1}{c}>1.        \tag{3.1}
\]

### 3.1 The low sequence

The left-filled Ferrers columns satisfy

\[
 b_1\ge b_2\ge\cdots\ge b_d\ge0,
 \qquad b_s=0\quad(s>d).
\]

Write `N_s=binom(k,s)`.  Since `N_s>=N_(s-1)` below the middle layer,

\[
 \frac{N_s-b_s}{N_{s-1}-b_{s-1}}
       \ge \frac{N_s}{N_{s-1}}.                         \tag{3.2}
\]

Indeed, cross multiplication reduces (3.2) to

\[
                         N_sb_{s-1}\ge N_{s-1}b_s.
\]

The binomial ratio `(k-s+1)/s` is decreasing in `s`, not increasing.
Therefore, for `s<=c`,

\[
 \frac{q_s}{q_{s-1}}
   \ge \frac{k-s+1}{s}
   \ge \frac{k-c+1}{c}=\rho.                            \tag{3.3}
\]

After reversing the indices, this is

\[
                         \frac{A_\delta}{A_{\delta+1}}\ge\rho. \tag{3.4}
\]

### 3.2 The high differences

Put `p_s=binom(k,s)/W` and `D_s=p_(s+1)-p_s`.  Above the corrected boundary,

\[
                         \Delta_j=D_{c+j}/H.
\]

Whenever `D_s>0`, direct substitution gives

\[
 \frac{D_{s+1}}{D_s}
 =\frac{(k-s)(k-2s-3)}{(s+2)(k-2s-1)}
 <\frac{k-s}{s+1}.                                     \tag{3.5}
\]

For `s>=c`, the last expression is strictly below `rho`.  At a zero terminal
difference the conclusion is automatic.  Hence

\[
                         \frac{\Delta_{j+1}}{\Delta_j}\le\rho. \tag{3.6}
\]

Combining (3.4) and (3.6) gives

\[
 A_\delta\Delta_j\ge A_{\delta+1}\Delta_{j+1},
\]

so every coefficient in (2.2) is nonnegative.

## 4. Correct block-resource bound

Let

\[
                         C=\sum_{\delta,j}(j+1)x_{\delta,j}.
\]

Summing (2.2) first in `j` and then in `delta` gives exactly

\[
 C=A_1+Pw_1+(P-A_1)(w_1-w_2).                           \tag{4.1}
\]

Write

\[
 \alpha=p_c=A_1,\qquad \beta=p_{c+1},\qquad\gamma=p_{c+2}.
\]

Since `H>=P`,

\[
 Pw_1\le G_1=1-\beta,
 \qquad w_1-w_2=\frac{\gamma-\beta}{H}.                \tag{4.2}
\]

The corrected geometric consequence of (3.4) is

\[
 P-\alpha\le\frac{\alpha}{\rho-1},
 \qquad \frac{P-\alpha}{P}\le\frac1\rho,
 \qquad \frac{P-\alpha}{H}\le\frac1\rho.             \tag{4.3}
\]

Equation (3.5), at `s=c`, gives the other corrected inequality

\[
                         \frac{\gamma-\beta}{\beta-\alpha}\le\rho. \tag{4.4}
\]

Substituting (4.2)--(4.4) into (4.1),

\[
 \begin{aligned}
 C
 &\le \alpha+(1-\beta)
       +\frac{P-\alpha}{H}(\gamma-\beta)\\
 &\le \alpha+(1-\beta)+(\beta-\alpha)=1.
 \end{aligned}                                         \tag{4.5}
\]

This is the required pull-block packing inequality.

If `H=0`, there is no low demand by (2.1), and the all-high clock suffices.

## 5. Finite boundary range

The only dimensions in which the asymptotic separation `c>d` needs no
appeal are finite.  Direct exact-rational substitution for `k<=14` gives:

```text
k=1..5  trivial all-high case
k=6     C=1/2
k=7     C=2/5
k=8     C=1/5
k=9     C=2/3
k=10    C=2665/7308
k=11    C=62/273
k=12    C=9/17
k=13    C=41/120
k=14    C=2583/3718
```

Every exact coefficient `x_(delta,j)` is nonnegative in those cases.  From
`k=15` onward the separated-band argument above applies.

## 6. Literal stationary realization

Clear denominators in the rational coefficients `x_(delta,j)`.  On a cyclic
timeline, concatenate the required number of blocks of each type, placing one
high separator after every block; fill unused positions with high slots.
Equation (4.5) guarantees that they fit.

Let `T=C disjoint-union F`, with `|C|=c` and `|F|=d+1`, and cycle the private
labels of `F` with period `d+1`.  A high letter is `C union {f_t}`.  In a
block of type `(delta,j)`, omit a fixed `delta`-subset of `C` for its `j`
low positions.  No low run has length more than `d`, so every `d+1` window
contains a high slot and all private labels; its union is exactly `T`.

Every proper window has precisely the rank profile computed by the
staircase ledger.  Symmetrize over owners, core choices, private-label orders,
block placements, and omitted core subsets.  The resulting literal
circulation has a rank profile `v_s>=q_s`.  Retain a `q_s/v_s` fraction of the
rank-`s` marked occurrences.  Proper suffix unions inside one trace are
strictly nested, so this thinning remains a legal marked chain.

Full coordinate symmetry makes every rank-`s` target equiprobable.  A fixed
rank-`s` target lies in `binom(k-s,r-s)` owners, and

\[
 \frac{\binom{k-s}{r-s}}{\binom{r}{s}}q_s
   =\frac{Wq_s}{\binom{k}{s}}
   =1-\frac{b_s}{\binom{k}{s}}.
\]

The Ferrers boundary supplies the complementary load.  Flow is balanced at
every literal trace state, proving the theorem.

## 7. What remains

This theorem removes the fractional stationary chronology separator.  The
circulation may repeat an owner many times and may have many components.  It
does not yet provide:

* exactly one trace for each rank-`r` owner;
* exactly one occurrence of every named residual target;
* one rooted Euler component with bounded sidecar;
* complete upper interval-union coverage and global residence in that same
  integral chronology.

The next lower-side statement is therefore an integral coloured rotor-fusion
theorem, not another fractional feasibility inequality.

## 8. Audits

All C++ compilation and numerical work ran on H100.

* exact finite audit source:
  `scratch/audit_pull_clock_small_exact_20260801.cpp`, SHA-256
  `7c844dd9f12ad0d744aa54f457bff0cc3dd22ec8ed6d05a1e383d1b45fafc3f2`;
* exact finite output:
  `scratch/audit_pull_clock_small_exact_20260801.out`, SHA-256
  `c9469eda90d8c37f0045416c34f40b62bd48f154c450f539ad6e0e5dcbae0fd0`;
* high-precision stress-audit source:
  `scratch/audit_pull_clock_staircase_inequalities_20260801.cpp`, SHA-256
  `e9cefa784cdfaf9a0bd9cb6d9c6ad90a94def70545024ae39518f4aeb99805ac`;
* stress output through `k=10000`:
  `scratch/audit_pull_clock_staircase_inequalities_20260801.out`, SHA-256
  `6e5a9cb0b5bb6ef14089b125a55974e50c525d6d1fb03082b248c41f62fb5c62`.

