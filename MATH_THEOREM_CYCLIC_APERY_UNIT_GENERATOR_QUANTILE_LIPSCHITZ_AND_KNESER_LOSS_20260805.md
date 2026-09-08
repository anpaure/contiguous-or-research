# Cyclic Apéry profiles: unit-generator normalization, quantile Lipschitzness, and exact Kneser loss

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional reduction.  Every nonzero cyclic Apéry profile
reduces, with a stronger target inequality, to a true-period profile whose
distinguished generator has cost one.  Its increasing defect quantiles are
automatically one-Lipschitz.  Failure of their full subadditivity is possible
only through a proper Kneser stabilizer, and the size of that stabilizer is
bounded explicitly by the physical initial interval already present in the
two sublevel balls.  This does not by itself prove the cyclic variance
conjecture.

## 1. Setup and the scale-sharp target

Let

\[
 e:\mathbb Z/g\mathbb Z\longrightarrow[0,\infty),\qquad e(0)=0,
\]

be subadditive:

\[
 e(x+y)\le e(x)+e(y).
\tag{1.1}
\]

Write

\[
 c=e(1),\qquad \mu={1\over g}\sum_xe(x).
\]

The scale-sharp form of the Apéry variance conjecture is

\[
 \boxed{\operatorname {Var}(e)\le {\mu(\mu+c)\over3}.}
\tag{1.2}
\]

Since the physical normalization has `c<=1`, (1.2) is stronger than the
previous target `Var(e)<=mu(mu+1)/3`.

### Lemma 1.1 (unit-generator normalization)

If `c=0`, then `e` vanishes identically.  If `c>0`, put `f=e/c`.  Then

\[
 f(1)=1,\qquad f(j)\le j\quad(0\le j<g),
\tag{1.3}
\]

and proving

\[
 \operatorname {Var}(f)\le {\bar f(\bar f+1)\over3}
\tag{1.4}
\]

proves (1.2).

#### Proof

Repeated use of (1.1) gives `e(j)<=j e(1)`.  Thus `c=0` forces every
value to be zero.  For `c>0`, division by `c` preserves subadditivity and
gives (1.3).  Multiplying (1.4) by `c^2` gives

\[
 \operatorname {Var}(e)
 \le {c^2\bar f(\bar f+1)\over3}
 ={\mu(\mu+c)\over3}.
\]

\(\square\)

## 2. The zero subgroup and true period

Put

\[
 H_0=\{x:e(x)=0\}.
\]

### Lemma 2.1

`H_0` is a subgroup, and `e` is constant on every `H_0`-coset.  Hence it
descends to a subadditive profile on `G/H_0` with the same value
distribution.  In particular one may assume, without changing the mean or
variance, that

\[
 \boxed{e(x)=0\iff x=0.}
\tag{2.1}
\]

#### Proof

Closure under addition follows from nonnegativity and (1.1).  If `h` has
finite order and `e(h)=0`, then

\[
 0\le e(-h)=e((\operatorname {ord}(h)-1)h)
 \le(\operatorname {ord}(h)-1)e(h)=0,
\]

so `H_0` is a subgroup.  For `h in H_0`,

\[
 e(x+h)\le e(x)+e(h)=e(x)
\]

and, using `-h in H_0`, the reverse inequality follows.  The quotient
statement is immediate.  Each quotient value is repeated exactly `|H_0|`
times upstairs, so its mean and variance are unchanged. \(\square\)

## 3. One-Lipschitz sorted quantiles

For `t>=0`, let

\[
 B_t=\{x:e(x)\le t\}.
\]

Under the unit normalization `e(1)=1`, equation (1.3) gives

\[
 \{0,1,\ldots,\lfloor t\rfloor\}\subseteq B_t.
\tag{3.1}
\]

Let

\[
 0=q_0\le q_1\le\cdots\le q_{g-1}
\]

be the values of `e` in increasing order, with multiplicity.

### Lemma 3.1 (cyclic interval growth)

For every nonempty `A subseteq Z/gZ` and integer `j>=0`,

\[
 |A+\{0,1,\ldots,j\}|\ge\min\{g,|A|+j\}.
\tag{3.2}
\]

#### Proof

It is enough to add the generator `1` one step at a time.  If a proper
subset `C` satisfied `C+1=C`, then invariance under the generator would
give `C=Z/gZ`.  Hence every proper `C` obeys
`|C union (C+1)|>=|C|+1`.  Iteration proves (3.2). \(\square\)

### Theorem 3.2 (quantile Lipschitzness)

For all `i,j>=0` with `i+j<g`,

\[
 \boxed{q_{i+j}\le q_i+j.}
\tag{3.3}
\]

In particular

\[
 \boxed{0\le q_{i+1}-q_i\le1.}
\tag{3.4}
\]

#### Proof

Subadditivity gives

\[
 B_{q_i}+B_j\subseteq B_{q_i+j}.
\]

By (3.1), `B_j` contains `{0,...,j}`.  Since `B_(q_i)` has at least
`i+1` elements, Lemma 3.1 shows that `B_(q_i+j)` has at least `i+j+1`
elements.  This is exactly (3.3).  Monotonicity supplies the lower half
of (3.4). \(\square\)

Quantile Lipschitzness is strictly stronger than the old pointwise bound
`q_i<=i`, but it is not alone sufficient for the variance inequality; the
remaining information is the additive growth of two arbitrary sublevel
balls.

## 4. Exact Kneser loss and its physical aperture

Subadditivity gives

\[
 B_s+B_t\subseteq B_{s+t}.
\tag{4.1}
\]

Fix quantile indices `i,j`, and let

\[
 H=\operatorname {Stab}(B_{q_i}+B_{q_j}).
\]

Write `h=|H|` and `m=g/h` for its index.

### Theorem 4.1 (quantitative Kneser quantile alternative)

If `B_(q_i)+B_(q_j)` is the whole group, then

\[
 q_{g-1}\le q_i+q_j.
\tag{4.2}
\]

Otherwise

\[
 \boxed{q_{i+j+1-h}\le q_i+q_j}
\tag{4.3}
\]

whenever the displayed index is nonnegative, and its stabilizer index
satisfies

\[
 \boxed{
 m>\lfloor q_i\rfloor+\lfloor q_j\rfloor+1,
 \qquad
 h<{g\over \lfloor q_i\rfloor+\lfloor q_j\rfloor+1}.}
\tag{4.4}
\]

For the aperiodic case `h=1`, (4.3) is the full quantile subadditivity

\[
 q_{i+j}\le q_i+q_j.
\tag{4.5}
\]

#### Proof

Kneser's theorem gives

\[
 |B_{q_i}+B_{q_j}|
 \ge |B_{q_i}|+|B_{q_j}|-|H|
 \ge i+j+2-h.
\]

Together with (4.1), this proves (4.2)--(4.3).

By (3.1), the sumset contains the consecutive residues

\[
 0,1,\ldots,\lfloor q_i\rfloor+\lfloor q_j\rfloor.
\tag{4.6}
\]

An `H`-periodic subset of the cyclic group is a union of the `m` residue
classes modulo `m`.  If it contains `m` consecutive residues, it contains
every `H`-coset and is the whole group.  In the proper case, (4.6) must
therefore contain fewer than `m` residues.  This gives the first inequality
in (4.4), and `h=g/m` gives the second.  Setting `h=1` in (4.3) gives
(4.5). \(\square\)

## 5. Consequence for the composite-period frontier

The prime-period proof used (4.5) for every pair and then a sharp prefix
majorization argument.  Theorem 4.1 shows exactly what changes in a
composite period:

* every failed quantile sum pays an index loss of `h-1`;
* that loss comes from a genuine proper subgroup;
* and a large physical threshold forces the subgroup to be small through
  (4.4).

Thus no arbitrary quantile jump survives.  A remaining counterprofile must
repeatedly correlate low-threshold balls with proper subgroups whose indices
exceed their physical initial-interval apertures.  The unresolved theorem is
to amortize the losses `h-1` in (4.3), or to factor the corresponding coset
profiles and apply the already-proved product-coset variance closure.

This note does not claim that this amortization has been completed.

## 6. Dependencies

1. Kneser's theorem for finite abelian groups;
2. `MATH_THEOREM_RAYLEIGH_GENERAL_APERY_PHASE_MOMENTS_AND_VARIANCE_GATE_20260805.md`;
3. `MATH_THEOREM_RAYLEIGH_PRIME_PERIOD_APERY_VARIANCE_AND_FORMAL_POSITIVITY_20260805.md`;
4. `MATH_COROLLARY_RAYLEIGH_APERY_VARIANCE_PRODUCT_COSET_CLOSURE_20260805.md`.
