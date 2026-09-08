# Critical interval rigidity at the exact lower-bound length

Date: 2026-09-08.

Status: proved necessary structure. This is not an attaining construction or
a proof that nu(k)=B(k). The finite audit below was executed only on h100.

## 1. Statement

Put

\[
r=\lceil k/2\rceil,\qquad W=\binom kr,\qquad
\Lambda=\sum_{s=1}^{r-1}\binom ks,
\]

and let d be least with

\[
\Lambda\le dW+\binom{d+1}{2}.
\]

Write n=W+d=B(k) and

\[
\sigma=dW+\binom{d+1}{2}-\Lambda.
\]

For a nonzero universal word A of length n, call a physical interval
**critical** if its OR has rank at least r but every proper subinterval has
OR rank below r. Let p be the number of critical intervals.

Then

\[
\boxed{
 W\le p,\qquad
 \binom{p+1}{2}-\binom{W+1}{2}\le\sigma.
}
\tag{1}
\]

In particular:

* For every k>=1, p is either W or W+1.
* If sigma<W+1, then p=W. Every critical interval has rank exactly r,
  every r-set labels exactly one critical interval, and that critical
  interval is contained in **every** witness for its label.
* The exceptional case p=W+1 is possible by this count only when
  sigma>=W+1. It has exactly one excess critical interval: either one
  critical interval has rank above r, or one r-set labels two critical
  intervals. All other critical labels are distinct r-sets.

The word "possible" in the last item means not excluded by (1). No example
at length B(k) with p=W+1 is supplied.

This rigidity holds with positive arithmetic slack. It does not force all
middle witnesses to have a common physical length or a flat derivative row.

## 2. Proof of the critical interval bound

Any interval with OR rank at least r contains an inclusion-minimal such
interval, since there are finitely many subintervals. In particular, a
witness for an r-set T contains a critical interval J. Its OR is both a
subset of T and of rank at least r, so its OR is exactly T. Thus every
r-set labels some critical interval and p>=W.

Distinct critical intervals cannot contain each other. Their left endpoints
are therefore distinct, their right endpoints are distinct, and ordering
the left endpoints orders the right endpoints strictly. Write them as

\[
J_i=[a_i,b_i],\qquad 1\le i\le p,
\]

in that order, and put q=n-p. Endpoint room gives

\[
i\le a_i\le b_i\le i+q.
\tag{2}
\]

Every physical interval of length at least q+1 contains a critical interval:
if its left endpoint is a, then a<=p and (2) puts J_a inside it. Hence every
interval with rank below r has length at most q. The number of intervals
of length at most q is

\[
N_q(n)=qn-\binom q2
      =\binom{n+1}{2}-\binom{p+1}{2}.
\]

All Lambda lower targets must appear among them. Consequently

\[
\Lambda\le \binom{n+1}{2}-\binom{p+1}{2}.
\tag{3}
\]

Subtract (3) from

\[
\Lambda+\sigma
=\binom{n+1}{2}-\binom{W+1}{2}
\]

to obtain (1).

For d>=1, minimality of d gives

\[
0\le\sigma\le W+d-1.
\tag{4}
\]

Also d<=r-1: each of the r-1 binomial coefficients in Lambda is at most W.
Since W>=r, we have d<=W-1. If p>=W+2, the left side of (1) is at least
2W+3, whereas (4) is at most 2W-2. This is impossible. If d=0, then
n=W and p<=n immediately gives p=W. Thus p<=W+1 in all cases.

If p>=W+1, (1) requires sigma>=W+1. Therefore sigma<W+1 implies p=W.
We already showed that all W r-sets occur among the p critical labels; with
exactly W intervals there can be neither a repeated label nor a higher-rank
label. The same counting proves the stated alternatives when p=W+1.

Finally, any witness for T contains a critical interval labeled T. When
p=W, there is exactly one such interval J_T, so every witness contains J_T.
This proves all the claims. QED.

## 3. Exact shape of every middle-target witness family

Assume p=W. Fix an r-set T, write its unique critical interval as
J_T=[a_T,b_T], and let [ell_T,u_T] be the maximal contiguous block of
positions containing J_T on which every letter is a subset of T.

Then the complete family of interval witnesses for T is exactly

\[
\boxed{
 \{[a,b]:\ell_T\le a\le a_T,\quad b_T\le b\le u_T\}.
}
\tag{5}
\]

Indeed, every witness contains J_T by Section 2 and consists only of
letters contained in T, so it lies in [ell_T,u_T]. Conversely, any interval
in (5) contains J_T and has no coordinate outside T, so its OR is T.

Thus a middle target appears at consecutive right endpoints b_T,...,u_T
and at consecutive left endpoints ell_T,...,a_T. Distinct r-sets cannot
occur at the same right endpoint, because suffix ORs form an inclusion
chain; the corresponding assertion at a fixed left endpoint is identical.
The middle target visible at the right endpoint therefore never disappears
and later returns. The same is true in the reversed word.

This gives a lossless restriction on any exact construction in the regime
sigma<W+1. It rules out distinct physical copies of the same minimal middle
witness, while allowing arbitrary increasing start/deadline schedules.

## 4. A companion bound on total middle multiplicity

For any word of length W+d covering all W rank-r targets, even without the
critical-uniqueness hypothesis, let l_T be the number of left endpoints
used by witnesses for T and e_T the number of right endpoints used by them.
Each is positive. A physical endpoint can serve only one target at rank r,
so

\[
\sum_T l_T\le W+d,\qquad \sum_T e_T\le W+d.
\]

Writing x_T=l_T-1 and y_T=e_T-1, we get sum x_T<=d and sum y_T<=d. The
number m_T of witnesses for T is at most l_T e_T. Therefore the total
number of rank-r physical intervals satisfies

\[
\boxed{
\sum_T m_T\le W+2d+d^2.
}
\tag{6}
\]

Here sum x_T y_T<= (sum x_T)(sum y_T)<=d^2. Under critical uniqueness,
(5) additionally says m_T=l_T e_T exactly. Thus only O(k) physical
middle-target occurrences beyond the W indispensable occurrences are
possible at length B(k), since d=Theta(sqrt(k)). This counts all physical
intervals, not merely one chosen middle witness per target.

## 5. Consequences at k=17

The master handoff gives

\[
r=9,\quad W=24310,\quad d=3,\quad \Lambda=65535,
\quad \sigma=7401.
\]

Since 7401<24311, any hypothetical 24313-letter universal word has exactly
24310 critical intervals. Their labels are all 9-sets, each once. Each
9-set has one minimal physical witness, every other witness for it contains
that one, and the right-endpoint middle sequence has no return to an
earlier target. Equation (6) limits the total number of rank-nine physical
intervals to W+15=24325.

This does not construct the missing 24313-letter word. It supplies exact
necessary constraints for such a construction, without assuming flatness,
grading, Johnson adjacency, or cyclic symmetry.

## 6. Relation to the earlier notes

The input is the elementary antichain/interval-length argument in
MASTER_HANDOFF.md Section 2 and in
MONOTONE_DEADLINE_LOWER_BOUND_AND_EQUALITY_AUDIT_20260727.md. The same
arithmetic breakpoint sigma<W+1 already appears as the shortest raw-cell
threshold in THREAD_H_SHORTEST_BULK_SKELETON_AND_K15_RESIDUAL_CERTIFICATE_20260728.md.
Neither the scalar lower bound nor that arithmetic breakpoint is new.

The new application here counts the **entire** antichain of minimal
rank-reaching intervals rather than a selected family of W middle
witnesses. It yields at most one excess critical interval in every exact
word, unique minimal middle witnesses in the usual slack regime, the
complete rectangle description (5), and the resulting no-return
restriction. The endpoint multiplicity estimate (6) is a separate elementary
count. No claim is made that these facts alone supply an exchange axiom or
the missing all-k construction.

The positive-slack counterexample to central flattening remains compatible
with all of these facts. The maximal-envelope and arbitrary-start staircase
criteria still impose additional pin and run constraints; this note does
not bypass them.

## 7. Bounded literal verification

The source script is

    scratch/verify_exact_b_critical_intervals_20260908.py

It was copied, together with answers/k01.word through answers/k16.word, to

    h100:/tmp/exact-b-critical-20260908.LZSLZL/

and run there with Python 3. It was not executed on the Mac. The script
maintains a monotone rank-threshold window to enumerate every critical
interval, checks (1), verifies that all critical labels are distinct r-sets,
and independently checks that no middle target returns after a missing
right endpoint. Every stored exact word from k=1 through k=16 passed.

Selected output:

| k | W | d | sigma | critical intervals | actual lower-rank cells |
|---:|---:|---:|---:|---:|---:|
| 4 | 6 | 1 | 3 | 6 | 4 |
| 9 | 126 | 2 | 0 | 126 | 255 |
| 11 | 462 | 3 | 369 | 462 | 1392 |
| 15 | 6435 | 3 | 2928 | 6435 | 19307 |
| 16 | 12870 | 3 | 12284 | 12870 | 32225 |

The finite checks validate these consequences on the stored witnesses.
Sections 2--4 prove the general statements. No k=17 equality witness or
all-dimensional equality theorem follows from the finite checks.
