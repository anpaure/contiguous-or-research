# Pinned aligned rays admit a zero-overlap-debt rank-row transport

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional asymptotic rank-row transportation theorem and
exact consequence for the mandatory two-sided-collar inequalities.  It
does not assign named targets to literal cells, construct a carrier, or
prove a complete lower deck.

## 0. Outcome

Put

\[
 r=\left\lceil {k\over2}\right\rceil,
 \qquad W={k\choose r},
 \qquad
 \Lambda=\sum_{s=1}^{r-1}{k\choose s},
\]

and let `d=d(k)` be least with

\[
                     dW+{d+1\choose2}\ge\Lambda.       \tag{0.1}
\]

Remove any triangular boundary family with rank multiplicities `b_s` and
put

\[
                     n_s={k\choose s}-b_s,
 \qquad             \sum_{s<r}n_s\le dW.             \tag{0.2}
\]

Assume that the boundary family does not contain the displayed terminal
ray targets.  This is automatic after the boundary is fixed away from
those `2(d-1)` named values; the usual triangular boundary has only
`O(d^2)` choices in ranks at most `d`, whereas the ray bank is in the
central lower band once `r>2d`.

The mandatory-collar inequality used below is the cyclic resident-factor
inequality from the cited rotor theorem.  Thus every positive run in
`\mathcal R` is internal and has legal length at least `d+1`.  On an
opened linear carrier, the rank-row transportation conclusion remains
valid, but the exact interpretation of the right side of (0.5) must also
include the separately priced clipped boundary runs.

In one aligned `Ibc/Ica` phase, row `q`, `1<=q<d`, contains two forced
ray cells.  They have the same rank

\[
                         s_q=r-d-1+q.                 \tag{0.3}
\]

For all sufficiently large `k`, all remaining nonboundary targets can be
assigned integrally to the `d` physical length rows, with `W` cells in
each row, so that

1. the two authenticated ray cells in every row `q<d` remain fixed;
2. every remaining singleton is assigned to row one; and
3. every remaining target of rank `s>=2` assigned to row `q` satisfies

   \[
                              2q\le s.                \tag{0.4}
   \]

Consequently, in the mandatory-collar inequality

\[
 \sum_{s=1}^{r-1}(2q-s)_+ n_{s,q}
 \le
 \sum_{R\in\mathcal R}
       \bigl(q-(L(R)-d-1)\bigr)_+,                  \tag{0.5}
\]

where `\mathcal R` is the multiset of maximal positive coordinate runs of
the carrier and `L(R)` is the number of owner vertices in the run,

the left side is zero for every `q>1` and is exactly the number of
nonboundary singleton targets for `q=1`.  Thus the complete family of
aggregate two-sided-collar/run inequalities has no further rank-level
content: it is satisfied as soon as the carrier has one exact minimum
positive run of length `d+1` with the correct label for every singleton
left to the central factor.

This is a genuine positive result for the pinned one-phase face.  It says
that neither the two ray rows nor any higher-rank collar count creates a
scalar obstruction.  The unresolved problem is entirely named and
physical: choose actual cells with `K_(j,q) subseteq S subseteq E_(j,q)`,
make all choices coexist in one occurrence system, and cover every named
target once up to bounded waste.

## 1. The two forced rays in each physical row

The aligned phase has, for `1<=j<d`, the exact target/address pairs

\[
 X_j=J\cup\{x\}\cup P_j,
 \qquad |X_j|=r-d-1+j,
 \qquad |C(X_j)|=j,                                  \tag{1.1}
\]

and

\[
 Y_j=J\cup\{y\}\cup S_j,
 \qquad |Y_j|=r-j-1,
 \qquad |C(Y_j)|=d-j.                                \tag{1.2}
\]

Here `|J|=r-d-2`, `|P_j|=j`, and `|S_j|=d-j`.  Therefore row `q`
contains

\[
                         X_q\quad\hbox{and}\quad Y_{d-q},
\]

and both have rank (0.3).  The aligned-ray theorem proves that these are
two distinct named targets at two distinct literal addresses.

For sufficiently large `k`, `r>=2d`, and hence

\[
                         s_q-2q=r-d-1-q\ge0
                         \qquad(1\le q<d).            \tag{1.3}
\]

Thus the forced rays themselves already lie on the zero-overlap-debt side
of (0.5).

## 2. The Ferrers rank-to-row graph

After deleting the two pins from each row `q<d`, give the rows capacities

\[
 c_q=\begin{cases}
       W-2,&1\le q<d,\\
       W,&q=d.
     \end{cases}                                      \tag{2.1}
\]

Delete the corresponding two named targets of rank `s_q` from the demands
`n_s`, and denote the remaining demands by `n'_s`.  Give a remaining
rank-`s` target the eligible row set

\[
 Q(1)=\{1\},
 \qquad
 Q(s)=\{1,\ldots,\min(d,\lfloor s/2\rfloor)\}
                         \quad(s\ge2).                \tag{2.2}
\]

Every edge in this rank graph obeys (0.4), except the deliberately retained
singleton exception.

The neighbourhoods in (2.2) are nested initial intervals.  Hence the
integer transportation problem is feasible exactly when

\[
 \sum_{s:Q(s)\subseteq[1,t]} n'_s
       \le\sum_{q=1}^t c_q
                         \qquad(1\le t\le d).         \tag{2.3}
\]

For `t<d`, the left side of (2.3) is

\[
                         \sum_{s=1}^{2t+1}n'_s,       \tag{2.4}
\]

while the right side is `t(W-2)`.  At `t=d`, (2.3) is only total
capacity.

## 3. Every Ferrers cut passes

The lower-bound asymptotic gives `d=Theta(sqrt(k))`.  Therefore

\[
 m_k:=2d-1=o(k).
\]

The standard elementary binomial bounds give

\[
 \sum_{s=1}^{m_k}{k\choose s}
 \le (m_k+1)\left({ek\over m_k}\right)^{m_k}
       =\exp(O(\sqrt{k}\log k)),                    \tag{3.1}
\]

whereas

\[
                         W\ge {2^k\over k+1}.         \tag{3.2}
\]

Consequently, for all sufficiently large `k`,

\[
                 \sum_{s=1}^{2d-1}{k\choose s}
                         \le W-2d.                   \tag{3.3}
\]

Fix `1<=t<d`.  Equations (2.4) and (3.3) give

\[
 \sum_{s=1}^{2t+1}n'_s
 \le W-2d
 \le t(W-2)=\sum_{q=1}^t c_q.                       \tag{3.4}
\]

At `t=d`, (0.2) gives

\[
 \sum_s n'_s
 =\sum_s n_s-2(d-1)
 \le dW-2(d-1)
 =\sum_{q=1}^d c_q.                                  \tag{3.5}
\]

Thus every cut (2.3) passes.  Integral max flow in the Ferrers
transportation graph assigns every remaining named target to a row.
Restoring the forced ray cells proves the rank-row transport asserted in
Section 0.

The argument assigns named targets only to **row copies**.  It does not
choose their physical start positions or prove literal aperture
containment.

## 4. Collapse of the aggregate collar inequalities

Let `n_(s,q)` be the resulting row census including the two ray pins.
For every scheduled non-singleton, (0.4) gives

\[
                              (2q-s)_+=0.             \tag{4.1}
\]

Section 1 proves the same statement for both forced targets in every row.
The only exception is `s=q=1`, for which

\[
                              (2q-s)_+=1.             \tag{4.2}
\]

It follows that the left side of (0.5) is

\[
 \sum_s(2q-s)_+n_{s,q}
 =\begin{cases}
      n_1,&q=1,\\
      0,&2\le q\le d.
   \end{cases}                                       \tag{4.3}
\]

For `q=1`, the right side of (0.5) is exactly the number of positive
carrier runs of minimum legal length `d+1`.  A singleton `\{x\}` needs
such a run labelled by the same coordinate `x`.  Hence one labelled
minimum run for every nonboundary singleton makes (0.5) hold at `q=1`;
all other rows then hold automatically.

This proves the claimed collapse.  Notice that it is stronger than merely
showing enough total short-cell capacity: it simultaneously respects the
actual `2(d-1)` ray lengths and eliminates every higher-rank demand for
arrival/departure overlap in the exact collar census.

## 5. Exact scope and the surviving lower theorem

The theorem closes only the **rank-row projection** of the mandatory
two-sided collar.  In particular it does not prove any of the following.

1. A row copy assigned rank `s` has not been assigned a physical cell
   `(j,q)`.  The named target still must satisfy

   \[
                         K_{j,q}\subseteq S\subseteq E_{j,q}.
   \]

2. Separate individually legal pins need not coexist.  Their negative
   coordinate intervals must obey the exact owner and positive-aperture
   cover cuts.
3. The required labelled minimum runs, resident complete Johnson carrier,
   and upper-complete chronology are not constructed here.
4. Rank-row transportation does not chainize the named targets, solve the
   sliding suffix cocycle, or control duplicate values in the fixed-word
   waste identity.
5. No implication to `nu(k)<=B(k)+O(1)` or to exact equality is claimed.

After the fixed-word functional-occurrence collapse and the pinned maximal-
envelope extension theorem, the remaining lower-side statement can now be
phrased without any scalar collar caveat:

> Construct one resident upper-complete carrier with the labelled
> minimum-run transversal and choose one protected occurrence signature
> extending the aligned ray facts whose **named** short-cell map covers all
> but `O(1)` strict-lower targets.

Every aggregate rank capacity and every aggregate mandatory-collar/run
inequality needed by that statement is compatible with the forced one-phase
ray bank.

## 6. Dependencies

- `MATH_THEOREM_INTEGRAL_ROTOR_MANDATORY_COLLAR_AND_MINIMUM_RUN_TRANSVERSAL_20260803.md`
- `MATH_THEOREM_ALIGNED_IBC_ICA_AMBIENT_BIRAIL_AND_POLARIZED_BUNDLES_20260804.md`
- `MATH_THEOREM_SERIAL_ONE_PHASE_FORCED_RAY_TERMINAL_REDUCTION_20260804.md`
- `MATH_THEOREM_FIXED_WORD_FUNCTIONAL_OCCURRENCE_AND_ONE_PHASE_HALL_COLLAPSE_20260804.md`
- `MATH_THEOREM_PINNED_MAXIMAL_ENVELOPE_GLOBAL_EXTENSION_AND_WASTE_IDENTITY_20260804.md`
