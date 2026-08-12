# Dense-subsequence transfer for the coefficient-one theorem

Date: 2026-07-26

## 0. Statement

Let

\[
  W(k)=\binom{k}{\lfloor k/2\rfloor}
\]

and let \(\nu(k)\) be the minimum length in the contiguous-OR problem.
Assume the standard trimmed lift

\[
  \nu(k+1)\le 2\nu(k).                                      \tag{0.1}
\]

Suppose there is an increasing sequence \(k_1<k_2<\cdots\) such that

\[
  k_{j+1}-k_j=o(k_j)                                         \tag{0.2}
\]

and

\[
  \nu(k_j)\le(1+o(1))W(k_j).                                \tag{0.3}
\]

Then

\[
  \boxed{\nu(k)=(1+o(1))W(k)}                               \tag{0.4}
\]

for all integers \(k\).

Consequently it is enough to prove coefficient one along any
multiplicatively dense arithmetic subsequence. In particular, a proof
for the dimensions naturally associated with primes in one fixed
reduced residue class, such as \(p\equiv1\pmod4\), transfers to all
dimensions, because consecutive primes in that progression have ratio
tending to one.

This removes the final-dimension objection to a construction that exists
only for the arithmetically admissible invariant cases
\(n=2m+1\equiv1\pmod4\).

## 1. Uniform central-binomial ratio

The central-binomial asymptotic, uniformly in parity, is

\[
  W(k)=2^k\sqrt{\frac{2}{\pi k}}\left(1+O(k^{-1})\right).     \tag{1.1}
\]

Hence, uniformly for \(0\le d=o(k)\),

\[
 \frac{2^dW(k)}{W(k+d)}
   =\sqrt{\frac{k+d}{k}}\,(1+o(1))
   =1+o(1).                                                   \tag{1.2}
\]

The parity of \(k\) and \(k+d\) changes only the relative
\(1+O(k^{-1})\) term in (1.1).

## 2. Proof of the transfer theorem

Given a large \(k\), choose \(j\) with

\[
                       k_j\le k<k_{j+1}
\]

and put \(d=k-k_j\). By (0.2), \(d=o(k_j)\). Iterating (0.1) gives

\[
  \nu(k)\le2^d\nu(k_j)
          \le(1+o(1))2^dW(k_j).
\]

Apply (1.2):

\[
  \nu(k)\le(1+o(1))W(k).
\]

The Sperner lower bound \(\nu(k)\ge W(k)\) gives (0.4). \(\square\)

## 3. Prime-progression corollary

Let \(p_j\) be the primes in a fixed reduced residue class modulo a
fixed integer \(a\). The prime number theorem in arithmetic
progressions implies

\[
                         \frac{p_{j+1}}{p_j}\longrightarrow1. \tag{3.1}
\]

Indeed, for every fixed \(\varepsilon>0\), the interval
\([x,(1+\varepsilon)x]\) contains a prime in that residue class for all
sufficiently large \(x\); then let \(\varepsilon\downarrow0\) along a
diagonal sequence. Thus any affine dimension parameter
\(k_j=p_j+O(1)\) satisfies (0.2).

For the translation-invariant wreath lane, the arithmetic audit gives:

* if \(n=2m+1\) is prime and \(n\equiv1\pmod4\), full
  \(\mathbb Z_n\)-invariance is arithmetically possible and requires
  exactly two fixed arithmetic-progression wreaths;
* if \(n\equiv3\pmod4\), it is impossible by the Catalan congruence.

Therefore a coefficient-one construction for all sufficiently large
primes \(n\equiv1\pmod4\) would be asymptotically sufficient; no
separate construction for the other congruence class is needed.

## 4. Scope

This theorem supplies only the endgame interpolation. It does not
construct the invariant factor or prove its quotient-shadow coverage.
Those are the exact remaining algebraic tasks in that lane.
