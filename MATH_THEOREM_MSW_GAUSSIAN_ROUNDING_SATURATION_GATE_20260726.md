# Gaussian-window rounding: saturation removes the depth factor, but laminarity alone cannot

Date: 2026-07-26

## 0. Outcome

The factor `|Q|` in the unconditional trade-cube rounding bound can be
removed in one precise regime: **critical saturation**.  If the initial
fixed-cut obstruction at almost every protected depth is within aggregate
`o(W)` of the maximum four units per switch, then every fractional
product state with `o(W)` mean `PCap` is close to the all-on corner.  The
all-on exact factor then also has `o(W)` `PCap`, with no dependence on the
number of depths.

This gives a rigorous Gaussian-window rounding theorem conditional only on
an aggregate critical-capacity identity.  It also shows what must replace a
generic Beck--Fiala or square-function argument: near the current Catalan
cutoff, a successful construction has to use essentially every available
four-arm switch.

The presently certified parent family does **not** establish the required
aggregate identity.  Its capacity ratio differs from the critical value
by `Theta(1/r)` at each depth, and summing that error through a Gaussian
window is much larger than `W`.  Moreover an abstract direct sum of the
four-arm triangle gadget can be arranged along nested flags and has
integrality gap linear in the number of depths.  Thus bounded support,
conflict degree four, and nested chains alone cannot improve the depth
factor.  A literal MSW improvement must use an additional statewise fact
about the canonical overloaded sets and the variable prefix arms.

---

## 1. Setup

Let `E` be an exact Boolean cube of `M` switches.  No additivity is
assumed.  For each protected depth `q`, write

\[
              \mu_q^x\qquad(x\in\{0,1\}^{E})             \tag{1.1}
\]

for the integral load vector.  Toggling one bit in any current state
removes at most four target occurrences and inserts at most four.  Put

\[
 K_q(y)=\sum_S(y(S)-b_q)_+,qquad
 \phi_q(y)=(K_q(y)-c_q)_+.                               \tag{1.2}
\]

For the row-power application, `b_q=p` and `c_q=W-N_q`.

Let the zero state be the canonical seed and put

\[
 \Omega_q=\{S:\mu_q^0(S)>b_q\},qquad
 D_q=K_q(\mu_q^0)-c_q.                                  \tag{1.3}
\]

The fixed overloaded-set functional is

\[
                  L_q(y)=\sum_{S\in\Omega_q}(y(S)-b_q).
                                                                    \tag{1.4}
\]

It satisfies `L_q(mu_q^0)=K_q(mu_q^0)`.  Since one toggle removes at
most four occurrences, in every state

\[
                  L_q(\mu_q^{x+e})
                  \ge L_q(\mu_q^x)-4.                   \tag{1.5}
\]

No assertion about the signs of the four collateral arms is used.

---

## 2. The saturation rounding theorem

Choose independent switch bits with arbitrary probabilities `x_e`, and
write

\[
 \bar\mu_q=\mathbb E\mu_q^X,qquad
 s=\sum_ex_e.                                           \tag{2.1}
\]

Thus `M-s` is the expected number of off bits.  Let `1` denote the all-on
state.

### Theorem 2.1 (all-on saturation rounding)

Assume numbers `delta_q>=0` satisfy

\[
                         D_q\ge4M-\delta_q               \tag{2.2}
\]

for every `q` in a depth set `Q`.  Then

\[
\boxed{
 4|Q|(M-s)
 \le \sum_{q\in Q}\phi_q(\bar\mu_q)
      +\sum_{q\in Q}\delta_q,}                          \tag{2.3}
\]

and the all-on exact factor satisfies

\[
\boxed{
 \sum_{q\in Q}\phi_q(\mu_q^{\mathbf1})
 \le
 2\sum_{q\in Q}\phi_q(\bar\mu_q)
 +\sum_{q\in Q}\delta_q.}                              \tag{2.4}
\]

Consequently, for a Gaussian-size or arbitrarily larger window,

\[
 \sum_q\phi_q(\bar\mu_q)=o(W),qquad
 \sum_q\delta_q=o(W)                                   \tag{2.5}
\]

imply an integral exact factor with aggregate `o(W)` cap obstruction.

#### Proof

Transform the zero state to an outcome `X` by toggling its selected bits
in any order.  Iterating (1.5) gives

\[
                  L_q(\mu_q^X)
                  \ge K_q(\mu_q^0)-4|X|.                \tag{2.6}
\]

Take expectations.  Since `L_q` is linear,

\[
                  L_q(\bar\mu_q)-c_q
                  \ge D_q-4s.                           \tag{2.7}
\]

For every real load vector,

\[
                  \phi_q(y)
                  \ge L_q(y)-c_q,                       \tag{2.8}
\]

because `K_q(y)` is the maximum over all target weights in `[0,1]`, and
the outer positive part is at least its argument.  Equations
(2.2), (2.7), and (2.8) give

\[
                  \phi_q(\bar\mu_q)
                  \ge4(M-s)-\delta_q.                   \tag{2.9}
\]

Sum to obtain (2.3).

Now couple `X` to the all-on state by toggling its off bits.  Two load
vectors of equal total mass which differ by one physical toggle have
`ell_1` distance at most eight.  Hence their cap tails, and therefore
their outer positive parts, differ upward by at most four.  Iteration and
expectation give

\[
 \phi_q(\mu_q^{\mathbf1})
 \le \mathbb E\phi_q(\mu_q^X)+4(M-s).                   \tag{2.10}
\]

For the desired comparison with the mean rather than the expected convex
value, apply the same equal-mass inequality directly to

\[
 \mu_q^{\mathbf1}-\bar\mu_q
 =\mathbb E(\mu_q^{\mathbf1}-\mu_q^X).
\]

The expected transport has positive mass at most `4(M-s)`, so

\[
 \phi_q(\mu_q^{\mathbf1})
 \le\phi_q(\bar\mu_q)+4(M-s).                            \tag{2.11}
\]

Sum (2.11) and substitute (2.3), proving (2.4).  \(\square\)

The proof is statewise and works for the full nonlinear cube.  It uses
neither total unimodularity nor independent target effects.

### Weighted form

For weights `w_q>=0`, assume

\[
                         D_q\ge4M-\delta_q
\]

on the support of the weights.  The same proof gives

\[
 \sum_qw_q\phi_q(\mu_q^{\mathbf1})
 \le2\sum_qw_q\phi_q(\bar\mu_q)
       +\sum_qw_q\delta_q.                              \tag{2.12}
\]

Thus the theorem applies directly to Gaussian quota weights whenever the
weighted criticality error is `o(W)`.

---

## 3. What the certified Catalan constants give

For the fixed-scale parent family,

\[
 d=\operatorname {Cat}_r,qquad
 M=H_{m,r+1}\operatorname {Cat}_{r-1},                  \tag{3.1}
\]

and

\[
 \rho_{m,r}:={M\over H_{m,r}d}
 ={(m-r)(r+1)\over
   4(2(m-r)-1)(2r-1)}
 ={1\over16}+\Theta(r^{-1}+r/m).                        \tag{3.2}
\]

At the critical formal value `d=4p`, the certified plateau tail is

\[
 H_{m,r}(d/2-p)={1\over4}H_{m,r}d,                      \tag{3.3}
\]

whereas the nominal four-arm capacity is

\[
                         4M=4\rho_{m,r}H_{m,r}d.         \tag{3.4}
\]

Because `rho_(m,r)>1/16`, the known lower bound is short of `4M` by

\[
                         \Theta(M/r+Mr/m)                \tag{3.5}
\]

per depth, even before subtracting `c_q=W-N_q`.  Across a window of
order `sqrt(m)`, the sum of (3.5) is not `o(W)` when
`r=Theta(log p)`.

This does not disprove critical saturation: (3.3) is only one certified
part of the canonical tail, and additional parent orientations could tune
the capacity.  It proves that Theorem 2.1 cannot be invoked from the
currently recorded constants alone.  The exact next scalar audit is

\[
 \boxed{
 \sum_{q\in Q}
  \left(4M-[K_q(\mu_q^0)-c_q]\right)_+=o(W).}            \tag{3.6}
\]

If (3.6) holds and a fractional product mean has `o(W)` aggregate `PCap`,
then Gaussian-window integrality is finished by Theorem 2.1.

---

## 4. Why a generic square-function theorem cannot suffice

There is an abstract nested four-arm family with integrality gap linear in
the number of depths.  Start with the three-column triangle gadget:
at each depth its fractional optimum is `3/2`, while every integral state
has value at least `2`.  For each resource and each private endpoint,
replace that endpoint at depth `q` by the `q`-th member of a nested target
chain.  The same three switch variables are used at all depths.  Every
column is still a ganged four-arm column, the switch family is additive
and conflict-free, and each of its arms is a nested flag.  Nevertheless

\[
 \min_{X\in\{0,1\}^3}\sum_{q\le H}K_q(X)
 -\min_{x\in[0,1]^3}\sum_{q\le H}K_q(x)
 ={H\over2}.                                             \tag{4.1}
\]

Taking disjoint direct sums gives gap `Theta(MH)`.

The chains can be realized as chains of sets, and each four-arm column can
be padded by reverse Johnson swaps so that it has zero total mass and zero
point margins.  Thus the following properties, even together, do not
imply sublinear-in-`H` rounding:

* four positive and four negative units per column;
* additive or conflict-free switches;
* nested support flags across depth;
* zero total and coordinate point margins.

This is an obstruction to a theorem based only on laminarity, vector
Efron--Stein, or Beck--Fiala column norms.  It is **not** asserted to be a
literal positive-density minor of the MSW matrix.  Proving such a literal
minor would require the unresolved cross-context collision geometry of
the variable prefix targets.

Hence a successful MSW Gaussian theorem must use one of two genuinely
seed-specific inputs:

1. the saturation identity (3.6), which forces a near-corner solution and
   bypasses discrepancy; or
2. a structural exclusion of persistent odd-cycle gadgets in the prefix
   collision matrix, substantially stronger than nestedness.

