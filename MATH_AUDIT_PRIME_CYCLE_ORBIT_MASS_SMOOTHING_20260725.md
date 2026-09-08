# Audit of prime-cycle orbit-mass smoothing

Date: 2026-07-25

Audited file:
`MATH_THEOREM_PRIME_CYCLE_ORBIT_MASS_SMOOTHING_20260725.md`.

## Verdict

**PASS.**  Theorem 4.2 is correctly normalized.  There is no hidden factor
of `n`, the averaging argument selects one common coordinate cycle for all
depths in the window, and the reduction from odd prime dimensions to all
dimensions is valid.  The note does not claim that relaxed token transport
is already an exact-factor operation; Section 6 states that missing lift
explicitly.

The only issue found was notational: the source initially used `P_sigma`
both for the permutation action and for the cyclic-orbit projection.  It
has now been repaired, using `P_tau` for permutation action and
`Pi_sigma=(1/n)sum_t P_(sigma^t)` for the orbit projection.  No mathematical
formula changed.

## 1. Orbit-floor normalization

For a prime-order coordinate cycle every nontrivial target orbit has size
`n`.  If its total load is `t_O`, then the orbit projection has constant
value `t_O/n` there, and

\[
 \sum_{S\in O}(1-(\Pi_\sigma\mu)(S))_+
 =n(1-t_O/n)_+=(n-t_O)_+.
\]

Thus equation (2.3) counts each orbit floor exactly once; it neither loses
nor gains a factor `n`.

Since `lambda_q>=1`,

\[
 (1-\lambda_q-(\Pi_\sigma f_q)(S))_+
 \le |(\Pi_\sigma f_q)(S)|,
\]

so the `L^1` and Cauchy bounds in (2.4) have the correct direction.

## 2. Projection class average

Exact cyclic loads have total mass zero after centering and constant point
marginals.  Hence `f_q` has no Johnson `U_0` or `U_1` component.

For prime `n`, every exponent `1<=t<n` is invertible modulo `n`; therefore
the power map `sigma -> sigma^t` is a bijection of the conjugacy class of
coordinate `n`-cycles.  The class average is zero on every `U_j`, `j>=2`.
Consequently

\[
 \mathbb E_\sigma\|\Pi_\sigma f_q\|_2^2
 ={1\over n}\|f_q\|_2^2.
\]

This verifies (3.3).  Summing this equality with arbitrary nonnegative
depth weights before choosing `sigma` verifies the simultaneous-cycle
statement (3.5).

## 3. Surplus lemma: exact cancellation of `n`

For an orbit `O`, define

\[
 d_O=\sum_{S\in O}\mu_q(S)-n\lambda_q.
\]

Its hole floor is

\[
 (-d_O-n(\lambda_q-1))_+.
\]

The projected centered function has value `d_O/n` at every one of the
`n` targets in `O`.  Therefore

\[
 \|\Pi_\sigma f_q\|_2^2
 =\sum_O n(d_O/n)^2={1\over n}\sum_Od_O^2,
\]

or equivalently

\[
                         \sum_Od_O^2
                         =n\|\Pi_\sigma f_q\|_2^2.
\]

Applying `(y-a)_+<=y^2/(4a)` with
`a=n(lambda_q-1)` gives

\[
 \mathfrak D_{\sigma,q}
 \le {n\|\Pi_\sigma f_q\|_2^2
       \over4n(\lambda_q-1)}
 ={\|\Pi_\sigma f_q\|_2^2\over4(\lambda_q-1)}.
\]

Thus Lemma 4.1 has exactly the stated normalization.

## 4. One cycle for the whole band

With `Q=ceil(m^(1/4))`, the two nonnegative random variables in (4.11)
satisfy

\[
 \mathbb ET_1\le {C_AQW\over n},
 \qquad
 \mathbb ET_2=O_A(W/Q).
\]

The second estimate follows from

\[
 \lambda_q-1\ge {q^2\over2m},
 \qquad
 {W\over n}\sum_{q>Q}{2m\over q^2}=O(W/Q).
\]

For positive expectations, the normalized sum

\[
 {T_1\over\mathbb ET_1}+{T_2\over\mathbb ET_2}
\]

has expectation two.  Hence one and the same `sigma` has both ratios at
most two.  If an expectation is zero, nonnegativity makes the corresponding
random variable identically zero, so omitting it is legitimate.

For that common cycle,

\[
 \sum_{q\le Q}\mathfrak D_{\sigma,q}
 \le(\sum_{q\le Q}N_q)^{1/2}T_1^{1/2}
 =O(QW/\sqrt n),
\]

and Lemma 4.1 gives

\[
 \sum_{Q<q\le H}\mathfrak D_{\sigma,q}=O(W/Q).
\]

Both are `O(Wm^(-1/4))`.  No depthwise choice of different cycles is used.

## 5. Prime-dimension lift

Let `p=p(k)<=k` be the largest odd prime below `k`.  The prime number
theorem implies `p/k->1`.  Repeated trimmed lifts give

\[
 \nu(k)\le2^{k-p}\nu(p).
\]

The central-binomial asymptotic gives

\[
 {2^{k-p}W(p)\over W(k)}=(1+o(1))\sqrt{k/p}=1+o(1).
\]

Therefore a coefficient-one theorem along odd prime dimensions would imply
the theorem in all dimensions.  This argument does not assert that Theorem
4.2 already proves the prime-dimensional theorem: the row-bundling and
middle-ownership lift remains explicitly open in Section 6.

## 6. Exact scope

What is proved is an `o(W)` **orbit-mass lower floor in the independent
token relaxation**, conditional on the bounded-energy exact factor (4.9).
What is not proved is attainability of that floor by legal wreath-row
switches, preservation of exact middle ownership, or construction of the
factor satisfying (4.9).  The source note states all three omissions.
