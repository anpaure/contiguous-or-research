# Gate C: the exact single-root ballot law and the factorial-moment gate

**Status (2026-08-22).**  Every general assertion below is proved.  For a
uniform cyclic block order on `K=2e+1` blocks, the sign word at one fixed
value cut is uniform on an explicit family of `binom(2e,e)` parity-balanced
words.  The proportion of those words which are two-sided ballot is
`O(1/K)`.  Hence the expected number of ballot cuts is bounded uniformly
in `K`.

The remaining high-overlap count is now an exact factorial-moment question.
If the `j`th falling factorial moment is at most exponential in `j` (or
even at most `C^K` when `j=K-R`), then the desired
`exp(O(K+R log K))` count follows immediately.  This multiroot estimate is
not proved here.

Throughout,
\[
                         K=2e+1\ge3.                    \tag{0.1}
\]

## 1. Uniform single-root word

Let `tau in S_K` be a uniform cyclic block order and put
`sigma=tau^{-1}`.  Fix a value `a`.  Translating all positions lets us
normalize `sigma(a)=0`; the relative position sequence
\[
 R(u)=\sigma(a+u)-\sigma(a)\pmod K,
 \qquad1\le u\le2e,                                    \tag{1.1}
\]
is then a uniform permutation of `1,...,2e`.  Define
\[
 w(u)=
 \begin{cases}
 +1,&R(u)\equiv u\pmod2,\\
 -1,&R(u)\not\equiv u\pmod2.
 \end{cases}                                           \tag{1.2}
\]
This is exactly the equal-block sign word at the cut `a`.

Call a word `w in {+1,-1}^{2e}` *parity-balanced* when the number of plus
signs in its odd positions equals the number in its even positions.

### Lemma 1.1 (exact word law)

The word (1.2) is uniform on the parity-balanced words.  Their number is
\[
                         \binom{2e}{e}.                  \tag{1.3}
\]

#### Proof

Suppose a prescribed word has `r` plus signs in its odd positions.  The
odd image residues must occupy those `r` positions and the `e-r` minus
positions of even parity.  Therefore the word is realizable exactly when
it also has `r` plus signs in its even positions.  In that case the odd
images can be assigned in `e!` ways and the even images independently in
`e!` ways.  The multiplicity `(e!)^2` is independent of the word.
Finally Vandermonde gives
\[
 \sum_{r=0}^e\binom er^2=\binom{2e}{e}.                 \tag{1.4}
\]
\(\square\)

The parity-balance condition is equivalently
\[
                         \sum_{u=1}^{2e}(-1)^u w(u)=0.  \tag{1.5}
\]

## 2. A meander plus alternating-local estimate

We use two standard elementary random-walk bounds, and include the joint
one because it supplies the extra square-root saving.

### Lemma 2.1 (one-dimensional meander)

For independent uniform signs `X_1,...,X_m`,
\[
 \Pr\left(\sum_{t=1}^sX_t\ge0\text{ for every }s\le m\right)
 \le {C\over\sqrt{m+1}}.                               \tag{2.1}
\]

This is the classical reflection/cycle-lemma count
`2^{-m} binom(m,floor(m/2))`, up to the harmless parity convention, and
the central-binomial bound proves (2.1).

### Lemma 2.2 (meander with a fixed alternating sum)

Uniformly in the integer `z`,
\[
 \Pr\left(
  \sum_{t=1}^sX_t\ge0\text{ for every }s\le m,
  \ \sum_{t=1}^m(-1)^tX_t=z
 \right)
 \le {C\over m+1}.                                     \tag{2.2}
\]

#### Proof

First let `m=2r`.  Pair consecutive signs and put
\[
 U_j={X_{2j-1}+X_{2j}\over2},\qquad
 V_j={X_{2j}-X_{2j-1}\over2}.                          \tag{2.3}
\]
The vector `(U_j,V_j)` is uniform on
`(1,0),(-1,0),(0,1),(0,-1)`.  The original meander event implies that the
first coordinate is nonnegative at every pair boundary, while the fixed
alternating sum fixes `2 sum_j V_j`.

Let `H` be the number of horizontal vector steps.  Conditional on `H` and
on their locations, the horizontal orientations form a simple walk of
length `H`, and the vertical orientations form an independent simple walk
of length `r-H`.  Lemma 2.1 and the maximum point mass of a simple walk
give the conditional upper bound
\[
 {C\over\sqrt{(H+1)(r-H+1)}}.                           \tag{2.4}
\]
Here `H` is binomial `(r,1/2)`.  On `r/4<=H<=3r/4`, (2.4) is `O(1/r)`;
outside that interval the binomial tail is exponentially small.  Averaging
proves (2.2) for even `m`.  For odd `m`, condition on the final sign and
apply the even case to the first `m-1` signs, changing `z` by one. \(\square\)

## 3. The `O(1/K)` single-cut theorem

Let `N_e` be the number of parity-balanced words whose prefix sums all lie
between zero and their terminal sum:
\[
 0\le\sum_{u=1}^m w(u)\le\sum_{u=1}^{2e}w(u)
 \qquad(1\le m\le2e).                                  \tag{3.1}
\]

### Theorem 3.1 (single-root rarity)

There is an absolute constant `C` such that
\[
 N_e\le {C4^e\over(e+1)^{3/2}},\qquad
 {N_e\over\binom{2e}{e}}\le {C\over e+1}={O(1)\over K}.
                                                               \tag{3.2}
\]

#### Proof

Choose a completely uniform sign word of length `2e` and split it into
two halves.  Condition (3.1) implies that the first half is a meander and
that the reversed second half is also a meander, because every suffix sum
is nonnegative.  Equation (1.5) says that the alternating sums of the two
halves agree up to a fixed sign depending only on `e`.

The halves are independent.  Sum over their common alternating-sum value,
bound the first-half sum by its total meander probability (2.1), and bound
each second-half summand by the maximum joint probability (2.2).  This
gives
\[
 {N_e\over4^e}\le {C\over(e+1)^{1/2}}{C\over e+1}
                  \le {C'\over(e+1)^{3/2}}.             \tag{3.3}
\]
The standard lower central-binomial bound
`binom(2e,e)>=c 4^e/sqrt(e+1)` gives the second assertion. \(\square\)

If `G(tau)` denotes the number of two-sided-ballot value cuts, symmetry
and Lemma 1.1 now give
\[
                         \mathbb E G\le C.              \tag{3.4}
\]

## 4. Exact factorial-moment reduction

For `j>=1`, write
\[
                         (G)_j=G(G-1)\cdots(G-j+1).     \tag{4.1}
\]
Let
\[
 \mathcal B_{K,R}=\{\tau:G(\tau)\ge K-R\}.             \tag{4.2}
\]
With `j=K-R`, Markov's inequality in falling-factorial form gives the
exact implication
\[
 { |\mathcal B_{K,R}|\over K!}
 \le {\mathbb E(G)_j\over j!}.                         \tag{4.3}
\]
Therefore either of the bounds
\[
 \mathbb E(G)_j\le C_0^j
 \quad\text{or merely}\quad
 \mathbb E(G)_{K-R}\le C_0^K                          \tag{4.4}
\]
would imply
\[
 \boxed{|\mathcal B_{K,R}|\le C_0^K K^R,\qquad
        \log|\mathcal B_{K,R}|=O(K+R\log K).}          \tag{4.5}
\]
For the Gate-C scale `K=Theta(b/log b)` and
`R=O(b/log^2 b)`, the last exponent is `o(b)`, which would rule out the
equal-block multiplicity route.

Theorem 3.1 is exactly the `j=1` case.  The multiroot estimate (4.4) is the
remaining theorem; single-root rarity alone does not imply it.

## 5. Finite audit

The companion checker
`scratch/verify_gate_c_single_root_ballot_law_and_moment_gate_20260822.py`
verifies the constant-multiplicity word law through `K=9`, enumerates
`N_e` through `e=10`, and reports all falling-factorial moments through
`K=9`.  Those finite moments are consistent with (4.4), but are labelled
computational evidence rather than proof.
