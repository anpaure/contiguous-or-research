# Simultaneous junta balance on adjacent middle layers

**Date:** 2026-08-05  
**Method:** the deletion coupling between adjacent slices and
hypergeometric concentration; no computation or search  
**Status:** unconditional sampling theorem.  At the odd middle level, two
equal-size samples can be chosen so that every event depending on at most
`t` coordinates has discrepancy at most `H(t/n+epsilon)` simultaneously.
For `t=O(d)`, `d^2=Theta(n)`, and `H=Theta(W/d)`, this is `O(H/d)`, exactly
the available total copy-loss scale.  The theorem closes the balance side
of any prospective `O(d)`-coordinate container proof.  It does not prove
that every physical Hall obstruction has such a container, nor that the
fresh-path packing produces a uniform skeleton sample.

## 1. Adjacent middle slices

Let

\[
                         n=2r-1,
 \qquad
 \mathcal L={ [n]\choose r-1},
 \qquad
 \mathcal R={ [n]\choose r}.
 \tag{1.1}
\]

The two layers have the same size

\[
                         W=|\mathcal L|=|\mathcal R|.       \tag{1.2}
\]

For `J subseteq [n]` and a family `A subseteq 2^J`, write

\[
 \mathcal C_\ell(J,A)
   =\{S\in{[n]\choose \ell}:S\cap J\in A\}.               \tag{1.3}
\]

Thus `C_l(J,A)` is an arbitrary `J`-junta event on the rank-`ell` slice;
no monotonicity or cylinder assumption is imposed.

## 2. Exact deletion coupling

Choose `T` uniformly from `R`, and then choose `x` uniformly from `T`.
Put

\[
                         K=T-\{x\}.                          \tag{2.1}
\]

### Lemma 2.1 (adjacent-slice junta distance)

The set `K` is uniform on `L`.  Moreover, for every `J subseteq [n]`,

\[
 \boxed{
 d_{\rm TV}\bigl(\mathcal L(T\cap J),
                   \mathcal L(K\cap J)\bigr)
                         \le {|J|\over n}.}                 \tag{2.2}
\]

Consequently, for every `A subseteq 2^J`,

\[
 \left|
 { |\mathcal C_r(J,A)|\over W}
 -{ |\mathcal C_{r-1}(J,A)|\over W}
 \right|
                         \le {|J|\over n}.                  \tag{2.3}
\]

#### Proof

For a fixed `K in L`, there are `n-(r-1)=r` possible supersets `T=K+x`.
Every pair `(T,x)` has probability `1/(Wr)`, so `K` is uniform on `L`.

Under this coupling, the two restrictions `T cap J` and `K cap J` differ
only when `x in J`.  Since `T` is uniform and `x` is uniform in `T`, `x`
is uniform on `[n]`.  Hence

\[
                         Pr(x\in J)={|J|\over n}.            \tag{2.4}
\]

The coupling inequality gives (2.2), and the event characterization of
total variation gives (2.3).  \(\square\)

The factor `|J|/n` is sharp in scale.  For example, with `J={z}` and the
event that `z` is present, the two slice probabilities differ by `1/n`.
Thus a one-coordinate Hall cut naturally spends `Theta(H/n)` slots; it
cannot in general be forced to have zero discrepancy.

## 3. Simultaneous empirical balance

Choose independently and uniformly

\[
                         X_-\in{\mathcal L\choose H},
 \qquad
                         X_+\in{\mathcal R\choose H}.       \tag{3.1}
\]

For a layer sign `sigma in {-,+}`, a coordinate set `J`, and a pattern
`P subseteq J`, put

\[
 \widehat\mu_\sigma^J(P)
   ={1\over H}|\{S\in X_\sigma:S\cap J=P\}|,               \tag{3.2}
\]

and let `mu_sigma^J(P)` be the corresponding uniform-slice probability.

### Theorem 3.1 (all-junta balance)

Let `1<=t<=n/2` and `epsilon>0`.  If

\[
 {2H\epsilon^2\over4^t}
   > t\log{en\over t}+t\log2+\log4,                        \tag{3.3}
\]

then there are samples `X_-`, `X_+` as in (3.1) such that, simultaneously
for every `J subseteq [n]` with `|J|<=t` and every `A subseteq 2^J`,

\[
 \boxed{
 \left|
 |X_+\cap\mathcal C_r(J,A)|
 -|X_-\cap\mathcal C_{r-1}(J,A)|
 \right|
             \le H\left({|J|\over n}+\epsilon\right).}     \tag{3.4}
\]

#### Proof

Sampling without replacement satisfies Hoeffding's inequality.  For a
fixed sign, `J`, and pattern `P`,

\[
 Pr\left(
  |\widehat\mu_\sigma^J(P)-\mu_\sigma^J(P)|
       >{\epsilon\over2^t}
 \right)
       \le2\exp\left(-{2H\epsilon^2\over4^t}\right).       \tag{3.5}
\]

There are two signs, at most `(en/t)^t` coordinate sets of size at most
`t` (enlarging a smaller set to size `t` only increases this bound), and
at most `2^t` patterns for each.  Condition (3.3) makes the union bound in
(3.5) strictly smaller than one.  Fix samples for which every pattern
estimate succeeds.

For each `J`, summing the pattern errors gives

\[
 d_{\rm TV}(\widehat\mu_\sigma^J,\mu_\sigma^J)
                         \le {\epsilon\over2}.              \tag{3.6}
\]

Lemma 2.1 and the triangle inequality now give

\[
 d_{\rm TV}(\widehat\mu_+^J,\widehat\mu_-^J)
                         \le {|J|\over n}+\epsilon.         \tag{3.7}
\]

Taking the event `A` in the variational definition of total variation and
multiplying by `H` proves (3.4).  \(\square\)

The proof balances the `2^|J|` pattern cells.  It does **not** union-bound
over the `2^(2^|J|)` different Boolean functions on `J`; once the pattern
measures are close, every such function is controlled at once.

## 4. Central asymptotic consequence

Let `d=d(n)` satisfy

\[
                         d^2=Theta(n),                       \tag{4.1}
\]

and let

\[
                         H=Theta(W/d).                       \tag{4.2}
\]

Fix an absolute `C` and take

\[
                         t=Cd,
 \qquad
                         \epsilon={1\over n}.               \tag{4.3}
\]

Since `log H=Theta(n)` whereas `t=O(sqrt(n))`, the left side of (3.3) is
`exp(Theta(n)-O(sqrt(n)))`, while the right side is `O(sqrt(n) log n)`.
Thus (3.3) holds for all sufficiently large `n`.

Equation (3.4) becomes

\[
 \left|
 |X_+\cap\mathcal C_r(J,A)|
 -|X_-\cap\mathcal C_{r-1}(J,A)|
 \right|
                         \le { (C+o(1))H d\over n}
                         =O(H/d)                             \tag{4.4}
\]

uniformly over **every** junta on at most `Cd` coordinates.

### Corollary 4.1 (junta containers cost only the separator budget)

Suppose every bottom-band Hall obstruction can be replaced by a container
whose membership on both adjacent middle layers is determined by at most
`Cd` coordinates, with replacement error `o(H/d)`.  Then the two middle
samples can be chosen so that all container discrepancies, and hence the
maximum bottom Hall deficiency attributable to such containers, are
`O(H/d)`.

#### Proof

Choose `X_-`, `X_+` from Theorem 3.1.  Apply (4.4) to the container event
and add its replacement error.  \(\square\)

This is deliberately conditional only at the final structural step.  The
new content is that **no additional probabilistic union bound is needed**
once an `O(d)`-coordinate container theorem is available.

## 5. Scope and the remaining physical rows

The theorem proves an existence statement for independent uniform samples
from the two full adjacent layers.  The physical owner construction still
has to establish both of the following.

1. The fresh-path/upper-level process can expose its bottom skeleton bank
   with the same junta-balance property (or can be switched to one of the
   samples supplied here).
2. Every bottom Hall obstruction is approximated, to `o(H/d)` error, by an
   `O(d)`-coordinate container.

The cylinder-moment invariant alone does not imply either row; the
two-component counterexample in

`MATH_THEOREM_BOTTOM_BAND_EMPTY_RECTANGLE_AND_CYLINDER_OBSTRUCTION_20260805.md`

shows why a global cut invariant is necessary.  The present theorem closes
the complementary balance calculation and explains the natural loss scale:
one coordinate costs `Theta(H/n)=Theta(H/d^2)`, while `Theta(d)` protected
coordinates cost `Theta(H/d)` in total.
