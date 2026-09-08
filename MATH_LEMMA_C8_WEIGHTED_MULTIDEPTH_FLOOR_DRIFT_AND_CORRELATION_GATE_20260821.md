# Exact weighted multidepth floor drift of the dimension-free `C_8`

**Date:** 2026-08-21  
**Status:** unconditional per-switch and aggregate drift identities; the
availability-correlation inequality needed for a global bound remains open

## 1. Floor potential

Put

\[
 b=2r+1,\qquad A=\binom br,
 \qquad N_q=\binom b{r-q},
 \qquad c_q=\left\lfloor{A\over N_q}\right\rfloor.          \tag{1.1}
\]

For an exact middle wreath factor `F`, let `mu_q(T)` be the multiplicity of
the cyclic rank-`(r-q)` target `T`.  Define

\[
 Q_q(F)=\sum_T(\mu_q(T)-c_q)(\mu_q(T)-c_q-1),                \tag{1.2}
\]

and, for `1<=H<=r-2`,

\[
             {\cal Q}_H(F)=\sum_{q=1}^H{Q_q(F)\over c_q}.   \tag{1.3}
\]

Every summand in (1.2) is nonnegative at integral load.  This is the
unhalved floor potential; it is not the duplicate-support mass
`sum_T(mu_q(T)-1)_+`.

If `h_q` is the number of missing depth-`q` targets, then each missing
target contributes

\[
 {(-c_q)(-c_q-1)\over c_q}=c_q+1\ge2
\]

to (1.3).  Hence the exact support consequence is

\[
                 \boxed{\quad 2\sum_{q=1}^Hh_q(F)
                                \le {\cal Q}_H(F).\quad}     \tag{1.4}
\]

In particular an `O(HA/r)` floor bound gives aggregate hole count
`O(HA/r)=o(A)` whenever `H=o(r)`.

## 2. Exact drift of one physical switch

Orient one legal dimension-free two-row `C_8` from its current pair to its
alternate pair.  At depth `q`, let `D_q` be its donor targets and `R_q`
its recipient targets.  The exact all-depth footprint theorem gives

\[
 p_q:=|D_q|=|R_q|=
 \begin{cases}
 2,&q=1,\\
 4,&2\le q\le r-2.
 \end{cases}                                                \tag{2.1}
\]

All targets on either side are distinct at these depths.

### Theorem 2.1 (per-switch floor drift)

For every legal oriented switch `s`,

\[
 \boxed{
 \Delta_s{\cal Q}_H
 =2\sum_{q=1}^H{1\over c_q}
 \left(
    \sum_{T\in R_q}\mu_q(T)
   -\sum_{T\in D_q}\mu_q(T)+p_q
 \right).}                                                 \tag{2.2}
\]

Thus a switch is improving for the weighted multidepth objective exactly
when the weighted donor-load advantage exceeds the footprint floor
`sum_q p_q/c_q`.

#### Proof

Put `f_c(x)=(x-c)(x-c-1)`.  A donor loses one occurrence and a recipient
gains one, so

\[
 f_c(x-1)-f_c(x)=2(c+1-x),\qquad
 f_c(z+1)-f_c(z)=2(z-c).                                    \tag{2.3}
\]

Sum (2.3) over the `p_q` donors and recipients.  Since their numbers are
equal, the `c_q` terms cancel and leave

\[
 \Delta_sQ_q
 =2\left(\sum_{R_q}\mu_q-\sum_{D_q}\mu_q+p_q\right).       \tag{2.4}
\]

Divide by `c_q` and sum through depth `H`. `square`

At `q=1`, formula (2.4) is twice the familiar convex-energy drift
`z+w-x-y+2`.  At every deeper active rank, the corresponding floor is
four rather than two.

## 3. Aggregate legal-move identity

Let `S(F)` be the bank of currently legal oriented `C_8` switches.  For a
depth-`q` target `T`, put

\[
 d^-_{q,T}=|\{s\in S(F):T\in D_q(s)\}|,
 \quad
 d^+_{q,T}=|\{s\in S(F):T\in R_q(s)\}|,
 \quad
 \eta_{q,T}=d^-_{q,T}-d^+_{q,T}.                            \tag{3.1}
\]

Also write

\[
                         P_H=\sum_{q=1}^H{p_q\over c_q}.    \tag{3.2}
\]

### Corollary 3.1 (exact multidepth drift sum)

\[
 \boxed{
 \sum_{s\in S(F)}\Delta_s{\cal Q}_H
 =2\left(
 P_H|S(F)|-
 \sum_{q=1}^H{1\over c_q}\sum_T\mu_q(T)\eta_{q,T}
 \right).}                                                 \tag{3.3}
\]

#### Proof

Sum (2.2) over the legal bank and collect the coefficient of each target.
Recipients contribute `d^+` and donors contribute `-d^-`, giving (3.3).
`square`

In particular every one-step local minimum obeys the **upper** correlation
inequality

\[
 \sum_{q=1}^H{1\over c_q}\sum_T\mu_q(T)\eta_{q,T}
 \le P_H|S(F)|.                                             \tag{3.4}
\]

The direction in (3.4) matters: high-load targets must correlate with
donor rather than recipient incidence in order to force an improving move.

## 4. The precise quantitative gate

An availability theorem of the following form would close the desired
local-minimum estimate:

\[
 \sum_{q=1}^H{1\over c_q}\sum_T\mu_q(T)\eta_{q,T}
 \ge P_H|S(F)|+\gamma{\cal Q}_H(F)-C{HA\over r},             \tag{4.1}
\]

with absolute `gamma>0,C`.  Combining (4.1) with (3.4) gives

\[
                         {\cal Q}_H(F)\le {C\over\gamma}{HA\over r}.
                                                                    \tag{4.2}
\]

Equation (4.1), or an augmenting-path replacement that is allowed to use
zero-drift switches before a negative one, is the exact remaining theorem.
Neither the abstract Boolean-square lattice nor the count of canonical
marked-gap switches implies (4.1): it depends on the squares physically
present in the evolving factor.

For comparison, define the first-shadow duplicate mass

\[
 D_1(F)=\sum_T(\mu_1(T)-1)_+
       =A-N_1+h_1(F)={2A\over r+2}+h_1(F).                   \tag{4.3}
\]

A q1-only capacity compiler needs `D_1=o(A)`, while an `H`-collar charged
by purging repeated first-shadow occurrences needs
`H D_1/A=o(1)`.  These are support requirements, not the quadratic floor
potential (1.3).  Equation (1.4) gives

\[
 D_1(F)\le {2A\over r+2}+{{\cal Q}_H(F)\over2},             \tag{4.4}
\]

but an `O(HA/r)` floor bound does not by itself imply the purge condition
at Gaussian `H`.  Its direct conclusion is instead the aggregate all-depth
hole bound in (1.4).  The two compiler routes must not be conflated.

## 5. Exact finite audit and its limit

The audit script

```text
scratch/audit_c8_weighted_multidepth_floor_drift_20260821.py
```

checks (2.2) literally on every legal edge of the complete canonical C8
components for `r=3,4`.  For `r=4`, the component has 3,014 factors.  Its
one-step local minima satisfy

\[
 \max {\cal Q}_1=14<0.445{A\over r},\qquad
 \max {\cal Q}_2={94\over3}<0.498{2A\over r}.               \tag{5.1}
\]

The global minima are `2` and `52/3`, respectively.  The exact active
footprints are `(2)` at `H=1` and `(2,4)` at `H=2`.

Randomized strictly-descending searches for `r=5,6,7` also terminate at
finite local minima, but their ratios to `HA/r` increase across these small
cases.  They are therefore recorded only as a warning: (5.1) is not
promoted to a uniform asymptotic constant.  Proving (4.1) requires a
structural Catalan/availability argument or neutral augmenting paths, not
extrapolation from bounded ranks.

## 6. Scope

The proved content is the exact floor drift (2.2), its legal-bank sum
(3.3), and the reduction (4.1)--(4.2).  This note does not prove (4.1), an
`O(HA/r)` local-minimum theorem, a C8-reachable low-energy factor, or
simultaneous upper/lower collar compilation.
