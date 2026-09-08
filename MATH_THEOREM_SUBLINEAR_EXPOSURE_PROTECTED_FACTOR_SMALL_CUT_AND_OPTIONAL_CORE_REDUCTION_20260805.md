# Sublinear-exposure protected forests: small-cut closure and the exact optional middle core

**Date:** 2026-08-05  
**Method:** pure mathematics; minimal deficient shores, capacitated Hall,
and the sharp partial-shadow theorem; no computation, search, or solver  
**Status:** unconditional small-cut and optional-tail theorem.  Two
`o(r)` exposure bounds force every residual obstruction and its optional
complement to have size `2^(2r-o(r))`.  They do not by themselves exclude
an obstruction in the remaining middle interval.  Excluding that interval
is the exact optional/co-small condition still needed for a spanning
two-factor.

## 0. Setting and outcome

Work on the odd ground set `[2r-1]` with the balanced middle-level
incidence graph

\[
 \mathcal L={ [2r-1]\choose r-1},
 \qquad
 \mathcal U={ [2r-1]\choose r},
 \qquad
 W=|\mathcal L|=|\mathcal U|.                       \tag{0.1}
\]

Let `P` be the incidence lift of a vertex-disjoint owner-path forest.
Thus every used lower colour has protected degree two, every unused lower
colour has protected degree zero, and every owner has protected degree at
most two.  Put

\[
 Z=\{x\in\mathcal L:d_P(x)=2\},
 \qquad X=\mathcal L\setminus Z,                    \tag{0.2}
\]

and give an owner residual capacity

\[
                         c_U=2-d_P(U).               \tag{0.3}
\]

Define the two literal exposure parameters

\[
 \alpha_r=\max_{x\in X}
   |\{U\in\mathcal U:x\subset U,\ d_P(U)>0\}|,       \tag{0.4}
\]

and

\[
 \beta_r=\max_{U\in\mathcal U}|N(U)\cap Z|.        \tag{0.5}
\]

The first is the protected-owner load in one lower owner star.  The second
is the used-facet load in one owner.  Item 5 of
`MATH_THEOREM_THREE_PALETTE_DISJOINT_CATALAN_COLLAR_BANK_20260805.md`
gives

\[
                  \alpha_r,\beta_r=O(r/\log r)=o(r) \tag{0.6}
\]

for its selected collar forest.

For an integer `D>=2`, put

\[
                         K(D)={2D-1\choose D}.        \tag{0.7}
\]

The conclusions are as follows.

### Theorem 0.1 (two-sided obstruction window)

Assume `alpha_r<=r-3` and `beta_r<=r-3`, and define

\[
 D_\alpha=r-\alpha_r-1,
 \qquad
 D_\beta=r-\beta_r-1.                               \tag{0.8}
\]

Every optional bank \(B\subseteq X\) with
\(\Omega_P(Z\cup B)>2|B|\) satisfies

\[
 \boxed{
 |B|\ge K(D_\beta)+1,
 \qquad
 |X\setminus B|\ge K(D_\alpha).}                    \tag{0.9}
\]

Consequently, if `P` does not extend, every positive optional obstruction,
including its canonical minimal DM core `B^-`, lies in the interval

\[
 \boxed{
 K(D_\beta)+1
 \ \le |B|\ \le
 |X|-K(D_\alpha)}.                                  \tag{0.10}
\]

In particular, when `alpha_r,beta_r=o(r)`, both lower bounds in (0.9) are

\[
                         2^{2r-o(r)}.               \tag{0.11}
\]

For the audited collar bank they are more explicitly

\[
                         2^{2r-O(r/\log r)}.        \tag{0.12}
\]

Thus all genuinely small residual shores and the co-small tail of the
optional obstruction are closed.  What remains is a possible middle
optional DM core, not another singleton or polynomial shore.

### Corollary 0.2 (exact sufficient optional condition)

The protected forest extends to a spanning two-factor if an independent
argument proves that no positive optional bank lies in (0.10).
It is enough, for example, to prove either of the following:

1. every positive \(B\) has \(|B|<K(D_\beta)+1\);
2. every positive \(B\) has \(|X\setminus B|<K(D_\alpha)\); or
3. every positive \(B\) obeys a small/co-small localization with cutoff
   smaller than \(\min\{K(D_\alpha),K(D_\beta)+1\}\).

The old cutoff `2^(r+o(r))` is far stronger than required and would close
the gate immediately.  It is not currently proved for the Catalan-scale
collar forest.

No connectedness, upper-`q1` exactness, residence, or literal compiler
claim is made.

## 1. Residual Hall and minimality

For `A subseteq X`, put

\[
 a_U=|N(U)\cap A|,
 \qquad
 \kappa(A)=\sum_{U\in\mathcal U}\min\{c_U,a_U\}.      \tag{1.1}
\]

Because every protected lower vertex has degree two,

\[
 \sum_{U\in\mathcal U}c_U
 =2W-|E(P)|
 =2W-2|Z|
 =2|X|.                                             \tag{1.2}
\]

The capacitated bipartite Hall criterion is

\[
 P\text{ extends to a spanning two-factor}
 \quad\Longleftrightarrow\quad
 \kappa(A)\ge2|A|\quad(A\subseteq X).               \tag{1.3}
\]

Assume a failure exists and choose an inclusion-minimal nonempty failed
shore `A`.  Integrality gives

\[
                         \kappa(A)\le2|A|-1.          \tag{1.4}
\]

Call an owner loose when

\[
                         1\le a_U\le c_U.            \tag{1.5}
\]

### Lemma 1.1 (one loose owner per selected lower vertex)

Every `x in A` lies below at most one loose owner.

#### Proof

Removing `x` decreases `kappa` by exactly the number `q_A(x)` of owners
above `x` satisfying (1.5).  Minimality makes `A-{x}` safe, so

\[
 q_A(x)
  =\kappa(A)-\kappa(A-\{x\})
  \le(2|A|-1)-2(|A|-1)=1.                            \tag{1.6}
\]

\(\square\)

## 2. Sublinear owner exposure closes the small side

Let

\[
 \mathcal F=\{U\in\mathcal U:d_P(U)=0,\ a_U\ge3\}.  \tag{2.1}
\]

### Lemma 2.1 (high-degree balanced partial shadow)

Every `x in A` is contained in at least

\[
                         D_\alpha=r-\alpha_r-1       \tag{2.2}
\]

owners of `mathcal F`, and

\[
                         |\mathcal F|\le|A|-1.       \tag{2.3}
\]

#### Proof

A lower vertex has exactly `r` owner neighbours.  At most `alpha_r` of
them are protected owners.  Every remaining owner has residual capacity
two.  Among those unprotected owners, Lemma 1.1 permits at most one with
`a_U<=2`; every other one has `a_U>=3` and belongs to `mathcal F`.  This
proves (2.2).

Every member of `mathcal F` contributes exactly two to `kappa(A)`.
Therefore

\[
             2|\mathcal F|\le\kappa(A)\le2|A|-1,
\]

and integrality proves (2.3). \(\square\)

### Theorem 2.2 (exact small-shore threshold)

Every failed residual shore has cardinality at least

\[
                         K(D_\alpha)
       ={2D_\alpha-1\choose D_\alpha}.              \tag{2.4}
\]

#### Proof

It is enough to prove the assertion for an inclusion-minimal failed shore
`A`.  Complement the families in `[2r-1]`:

\[
 \mathcal J=\{[2r-1]\setminus x:x\in A\}
             \subseteq{[2r-1]\choose r},            \tag{2.5}
\]

\[
 \mathcal C=\{[2r-1]\setminus U:U\in\mathcal F\}
             \subseteq{[2r-1]\choose r-1}.          \tag{2.6}
\]

Every member of `mathcal J` contains at least `D_alpha` members of
`mathcal C`, by Lemma 2.1, while

\[
                         |\mathcal C|<|\mathcal J|.  \tag{2.7}
\]

The threshold partial-shadow theorem, with side ratio one, gives

\[
                         |\mathcal J|
                          \ge{2D_\alpha-1\choose D_\alpha}.          \tag{2.8}
\]

Since complementation preserves cardinality, this is (2.4).  Any failed
shore contains an inclusion-minimal failed shore, so the same lower bound
holds without minimality. \(\square\)

If `alpha_r=o(r)`, Stirling's formula gives

\[
 \log_2K(D_\alpha)
 =2D_\alpha-\frac12\log_2D_\alpha+O(1)
 =2r-o(r).                                           \tag{2.9}
\]

This replaces the constant `m-21` estimate in the earlier theorem.  It
also removes the old exceptional top-endpoint set and the separate
polynomial Kruskal--Katona range: all protected owners, including both
collar endpoints, are already priced by `alpha_r`.

## 3. Sublinear forced-facet exposure closes the optional tail

For an owner put

\[
 G_U=N(U)\cap X,
 \qquad g_U=|G_U|=r-|N(U)\cap Z|.                   \tag{3.1}
\]

Thus (0.5) gives

\[
                         g_U\ge r-\beta_r.           \tag{3.2}
\]

For `B subseteq X`, let

\[
 b_U(B)=|B\cap G_U|,
\]

and use the exact optional overflow functional

\[
 \Omega_P(Z\cup B)
   =\sum_U\bigl(b_U(B)-(g_U-c_U)\bigr)_+.            \tag{3.3}
\]

The optional-complement identity is

\[
 \kappa(X\setminus B)-2|X\setminus B|
       =2|B|-\Omega_P(Z\cup B).                     \tag{3.4}
\]

Let \(B\subseteq X\) be any positive optional bank, meaning
\(\Omega_P(Z\cup B)>2|B|\).  Define its positive owner family

\[
 \mathcal Q=
 \{U:b_U(B)\ge g_U-c_U+1\}.                         \tag{3.5}
\]

Positivity gives

\[
 \sum_U\bigl(b_U(B)-(g_U-c_U)\bigr)_+>2|B|.
                                                               \tag{3.6}
\]

Every summand is at most `c_U<=2`, so

\[
                         |\mathcal Q|>|B|.           \tag{3.7}
\]

Moreover each `U in mathcal Q` contains at least

\[
 g_U-c_U+1
       \ge(r-\beta_r)-2+1
       =D_\beta                                      \tag{3.8}
\]

members of \(B\).

### Theorem 3.1 (exact optional-core threshold)

Every positive optional bank satisfies

\[
 \boxed{
 |B|\ge {2D_\beta-1\choose D_\beta-1}+1
          =K(D_\beta)+1.}                           \tag{3.9}
\]

#### Proof

Apply the strict-imbalance form of the sharp partial-shadow theorem to
the adjacent-rank families \((B,\mathcal Q)\), using (3.7)--(3.8).  It
gives the first expression in (3.9).  Symmetry of the odd top row gives

\[
 {2D_\beta-1\choose D_\beta-1}
 ={2D_\beta-1\choose D_\beta}=K(D_\beta).
\]

\(\square\)

If `beta_r=o(r)`, the same Stirling calculation as (2.9) gives

\[
                         \log_2|B|\ge2r-o(r).        \tag{3.10}
\]

## 4. Proof of the obstruction window

Take any positive optional bank \(B\).  By Theorem 3.1,

\[
                         |B|\ge K(D_\beta)+1.        \tag{4.1}
\]

Put \(A=X\setminus B\).  Equation (3.4) says that \(A\) is a failed residual
shore.  It contains an inclusion-minimal failed shore, so Theorem 2.2
gives

\[
                         |A|\ge K(D_\alpha).         \tag{4.2}
\]

Since \(A\) and \(B\) partition \(X\), equations (4.1)--(4.2) are exactly
(0.9)--(0.10). \(\square\)

One immediate numerical corollary is worth recording.

### Corollary 4.1 (a sufficient two-tail inequality)

If

\[
                         K(D_\alpha)+K(D_\beta)+1>|X|,               \tag{4.3}
\]

then `P` extends to a spanning two-factor.

This criterion is unconditional but is not implied merely by
`alpha_r,beta_r=o(r)`.

## 5. Why the previous co-small closure does not automatically transfer

The earlier co-selected-reservoir theorem combined the constant exposure
bounds with an independently proved cardinality localization

\[
             \min\{|A|,W-|A|\}=2^{r+o(r)}.           \tag{5.1}
\]

That localization came from the global protected-edge bound
`|E(P)|=O(r2^r)` and the protected Ore near-shadow theorem.  It put one
side of every failed cut far below both partial-shadow thresholds.

For the parity-appropriate Catalan collar bank, the number of collars is

\[
                  b={W\over2r-1}-1,                 \tag{5.2}
\]

and a collar has `s+1` Johnson transitions.  Its incidence lift therefore
has

\[
                  |E(P)|=2b(s+1)=\Theta(W/\sqrt r)  \tag{5.3}
\]

at deadline scale.  Substitution into the old total-edge localization
produces only an upper bound of order `W sqrt(r)`, which is larger than the
entire shore and hence vacuous.

The local estimates `alpha_r,beta_r=O(r/log r)` close both tails by
Sections 2--3, but they do not supply a cardinality localization excluding
the middle interval (0.10).  No theorem currently derives such a
localization from those two marginal loads alone.

Accordingly the exact remaining premise is:

> **Optional middle-core exclusion.**  The selected collar forest has no
> positive optional DM core `B^-` satisfying (0.10).

Any structural proof of this premise completes the spanning-two-factor
extension.  A much stronger but sufficient replacement is the old
`2^(r+o(r))` small/co-small cutoff.  Proving upper-`q1` exactness,
connectedness, or residence is neither needed for this factor-extension
step nor implied by it.

## 6. Application boundary for the audited three-palette bank

The audited bank supplies exactly the hypotheses used above:

1. owner blocks are disjoint and every collar is a simple owner path;
2. lower resources are disjoint, so every used lower vertex has protected
   degree two and the incidence lift is a path forest;
3. Item 5 gives `alpha_r=O(r/log r)`;
4. the same item gives `beta_r=O(r/log r)`.

Therefore Theorem 0.1 applies and closes all optional-core tails outside

\[
 \left[
  2^{2r-O(r/\log r)},
  |X|-2^{2r-O(r/\log r)}
 \right].                                           \tag{6.1}
\]

It does **not** by itself prove that the bank extends.  The exact live row
is the optional middle-core exclusion above.  Even after that row is
proved, the conclusion is only a spanning two-factor containing the
protected collar forest; it says nothing about the number of cycles or
about upper palettes beyond those already protected prospectively.

## 7. Dependencies

- `MATH_THEOREM_COSELECTED_RESERVOIR_SMALL_CUT_CLOSURE_AND_PROTECTED_FACTOR_20260804.md`
- `MATH_THEOREM_OPTIONAL_CO_SMALL_CHARGING_LP_EXACT_FACTOR_EQUIVALENCE_20260804.md`
- `MATH_THEOREM_SHARP_OPTIONAL_THRESHOLD_SHADOW_VIA_PARTIAL_SHADOW_20260804.md`
- `MATH_THEOREM_THREE_PALETTE_DISJOINT_CATALAN_COLLAR_BANK_20260805.md`
