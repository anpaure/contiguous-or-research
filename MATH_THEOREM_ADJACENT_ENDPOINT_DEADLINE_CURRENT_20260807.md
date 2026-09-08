# Adjacent endpoint deadline current: every surviving packet must move a rank bank of size \(d\)

**Date:** 2026-08-07  
**Method:** exact shared-suffix submodularity and the endpoint-interval lemma  
**Status:** theorem.  Independently audited in two pure-math lanes; the
only correction was to state the required \(d\ge2\) scope explicitly.

## 1. Arbitrary endpoint profiles

Let

\[
 Z_{i,j}=A_{i-j+1}\cup\cdots\cup A_i,
 \qquad 1\le j\le d.
\]

Assume \(d\ge2\).  No fullness or saturated-chain assumption is made.  For two adjacent
endpoints put

\[
 a_j=|Z_{i,j}|,
 \qquad b_j=|Z_{i+1,j}|.
\]

Use

\[
 s=m-2d,
 \qquad t=m-d.
\]

Define the deviations of the three relevant cells from the full two-rail
profile by

\[
 \alpha=a_d-(t-1),\qquad
 \beta=b_d-(t-1),\qquad
 \gamma=(t-2)-a_{d-1}.                              \tag{1.1}
\]

Here \(\alpha\) and \(\beta\) are top-rank excesses, whereas positive
\(\gamma\) is a collapse of the shared depth-\((d-1)\) suffix.  These
numbers need not be nonnegative individually.

## 2. Exact current inequality

### Theorem 2.1

In a universal word of exact length \(W+d\), every adjacent endpoint pair
satisfies

\[
 \boxed{\alpha+\beta+\gamma\ge d.}                  \tag{2.1}
\]

#### Proof

Put

\[
 X=Z_{i,d},\qquad Y=Z_{i+1,d},\qquad H=Z_{i,d-1}.
\]

The shared \(d-1\) source letters give \(H\subseteq X\cap Y\), so

\[
 |X\cup Y|\le a_d+b_d-a_{d-1}.                       \tag{2.2}
\]

The union \(X\cup Y\) is the union of the \(d+1\) consecutive source
letters from \(i-d+1\) through \(i+1\).  At length \(W+d\), the
architecture-free endpoint-interval lemma requires every such interval to
have rank at least \(m\).  Hence

\[
 m\le a_d+b_d-a_{d-1}.
\]

Substituting

\[
 a_d=t-1+\alpha,\qquad b_d=t-1+\beta,
 \qquad a_{d-1}=t-2-\gamma,
\]

the right side is \(t+\alpha+\beta+\gamma\).

Since \(m=t+d\), inequality (2.1) follows. \(\square\)

The inequality is sharp at the level of ranks: equality means that the
shared suffix accounts for all of \(X\cap Y\) and that the \((d+1)\)-cell
span is itself a rank-\(m\) owner.

## 3. Fixed-additive guarded form

At length \(W+d+C\), place the same adjacent pair inside a containing
interval of length \(d+C+1\).  Let \(G\) be the union of the \(C\) outside
guard letters in that extension, and put

\[
                         \zeta=|G\setminus(X\cup Y)|.
\]

Then

\[
 \boxed{\alpha+\beta+\gamma+\zeta\ge d.}             \tag{3.1}
\]

The proof is identical: the containing interval has rank at least \(m\),
while

\[
 |X\cup Y\cup G|
 \le a_d+b_d-a_{d-1}+\zeta.
\]

For two full endpoints, \(\alpha=\beta=\gamma=0\), so the guard bank must
contribute at least \(d\) fresh coordinates.  If the guard contribution is
\(o(d)\), then the endpoint profiles themselves must carry
\(d-o(d)\) units of rank current.

## 4. Consequences for a replacement packet

The fixed-additive full-endpoint density theorem proves that a positive
density of complete two-rail packets is impossible.  The present theorem
identifies the minimum local change needed by any adjacent replacement:

\[
 \boxed{\text{top excess} + \text{shared-suffix collapse}
        + \text{fresh guard rank}\ \ge d.}
\]

Therefore no bounded-rank perturbation of the full packet can work.  A
surviving positive-density interface must do at least one of the following
on a deadline scale:

1. raise one or both depth-\(d\) endpoint ranks by \(\Omega(d)\);
2. collapse the shared depth-\((d-1)\) suffix by \(\Omega(d)\);
3. import an \(\Omega(d)\)-fresh guard bank; or
4. distribute these three currents with total at least \(d\).

This is a rank-current condition only.  It does not prove that a profile
meeting (2.1) or (3.1) has the named lower targets, residence, upper deck,
or compiler compatibility required by a universal word.
