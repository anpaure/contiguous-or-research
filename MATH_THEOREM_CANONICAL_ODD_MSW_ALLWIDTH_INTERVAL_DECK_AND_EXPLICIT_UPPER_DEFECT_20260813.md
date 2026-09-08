# The canonical odd MSW long-aperture factor has an explicit exponential immediate-upper defect

**Date:** 2026-08-13  
**Status:** unconditional all-width reduction and explicit infinite-family
obstruction; exact finite census through `m=11`  
**Scope:** the canonical published M\"utze--Standke--Wiechert factor, not
every possible minimum-odd-cycle factor

## 1. The all-width deck is one cyclic-interval system

Put

\[
 \Omega=[2m]\sqcup\{\infty\},\qquad n=2m+1,       \tag{1.1}
\]

and let `F_m` be the canonical MSW factor into `Cat_m` minimum cycles of
`KG(2m+1,m)`.  Reconstruct from each Dyck root `w` its cyclic omitted-label
order

\[
 \sigma_w=(z_0,\ldots,z_{2m}).                    \tag{1.2}
\]

Every component's rank-`m` vertices are all cyclic `m`-intervals in this
order, and their complements are all cyclic `(m+1)`-intervals.  We use the
latter as the long-aperture rank-`R=m+1` owner component.

Let `q=d+1 <= m` be the flat erosion length and put

\[
 A_i=I_i^{m-q+2}(\sigma_w).                       \tag{1.3}
\]

Then the union of `ell` consecutive source letters is

\[
 \bigcup_{j=0}^{\ell-1}A_{i+j}
 =I_i^t(\sigma_w),
 \qquad t=m-q+\ell+1,                             \tag{1.4}
\]

as long as `t<n`.  At `t=n` it is the full ground.

### Lemma 1.1 (exact witness criterion)

For every proper rank `t`, a named target `T in binom(Omega,t)` is
witnessed by the canonical long-aperture source if and only if `T` is a
cyclic `t`-interval in at least one order `sigma_w`.

Moreover,

\[
 T=I_i^t(\sigma_w)
 \quad\Longleftrightarrow\quad
 \Omega\setminus T=I_{i+t}^{n-t}(\sigma_w).       \tag{1.5}
\]

Hence the covered rank-`t` and rank-`(n-t)` families are complements of
one another and have the same defect.

### Proof

Equation (1.4) is the union formula for overlapping cyclic intervals.
Every proper source interval occurs at one of the `n` starts of its
component, proving the criterion.  Equation (1.5) is the complementary arc
of a cyclic order. \(\square\)

There are

\[
 n\operatorname{Cat}_m
 =\binom{2m+1}{m}
 =:W_m                                               \tag{1.6}
\]

pointed interval occurrences at every proper rank.  Therefore the average
multiplicity at rank `t` is

\[
 \lambda_t=\frac{W_m}{\binom nt}.                  \tag{1.7}
\]

For the upper rank

\[
 t=m+1+j,\qquad1\le j\le m-1,                     \tag{1.8}
\]

complementation reduces coverage to rank `m-j`, and

\[
 \lambda_{m+1+j}
 =\frac{W_m}{\binom n{m-j}}
 =\prod_{s=0}^{j-1}\frac{m+2+s}{m-s}.             \tag{1.9}
\]

In particular the immediate-upper row `j=1` has only

\[
 \lambda_{m+2}=\frac{m+2}{m}=1+\frac2m             \tag{1.10}
\]

average load.  Thus it is a nearly tight interval-cover problem, not a row
with constant scalar slack.

## 2. Exact solved rows

The MSW factor itself gives

\[
 \mathcal C_m=\binom\Omega m,qquad
 \mathcal C_{m+1}=\binom\Omega{m+1},               \tag{2.1}
\]

where `C_t` denotes the family covered by cyclic `t`-intervals.  The first
identity is the minimum-odd-cycle factor; the second follows by
complementation.  In the owner convention, rank `m+1` is the exact owner
row and rank `m` is the exact immediate-lower row.

At the full width every endpoint gives the same target `Omega`; named
coverage is counted once per component rather than once per endpoint.

No MSW theorem asserts

\[
 \mathcal C_{m-1}=\binom\Omega{m-1},               \tag{2.2}
\]

and (2.2) is in fact false for the canonical factor.

## 3. An explicit missing family at the immediate-upper rank

Write a subset of `[2m]` as an up/down word, with `1` denoting membership.
Put

\[
 T_0=(1100)^2 1111.                                \tag{3.1}
\]

For `m>=6` and every Dyck word `V` of semilength `m-6`, define

\[
 T_V=T_0V\subseteq[2m].                            \tag{3.2}
\]

The word `T_V` has `m+2` ones.

### Theorem 3.1 (canonical immediate-upper defect)

No `T_V` is a cyclic `(m+2)`-interval in any canonical MSW order.
Consequently

\[
 \left|\binom\Omega{m+2}\setminus\mathcal C_{m+2}\right|
 \ge\operatorname{Cat}_{m-6}.                    \tag{3.3}
\]

Equivalently, the rank-`(m-1)` complements

\[
 S_V=\{\infty\}\cup([2m]\setminus T_V)           \tag{3.4}
\]

are absent from the lower interval deck.

### Proof

Cut a canonical odd MSW order at `infinity`.  The rank-`(m-1)` intervals
containing `infinity` are exactly

\[
 \{\infty\}\cup([2m]\setminus\Gamma(x)),          \tag{3.5}
\]

where `Gamma(x)` is the union of the two selected upper facets incident
with one internal state of the canonical complementary-geodesic factor.
This is the exact three-sector decomposition of the canonical odd wreath
first shadow.

The canonical `Gamma` inverse criterion says that a rank-`(m+2)` word `T`
has a preimage if and only if it has two up-step positions `p<q` satisfying
the four height, clean-corridor, and ordinal conditions.  The proved
Dyck-suffix obstruction shows that `T_0V` has no such pair for every Dyck
suffix `V`; see
`MATH_OBSTRUCTION_CANONICAL_MSW_Q2_SURJECTIVITY_INFINITE_FAMILY_20260805.md`,
Theorem 4.1.  Hence `T_V` is not a `Gamma` value.  By (3.5), `S_V` is not
an odd-wreath interval.  Complementation (1.5) then says that `T_V` is not
an `(m+2)`-interval either.

There are `Cat_(m-6)` Dyck suffixes and they give distinct words, proving
(3.3). \(\square\)

Since

\[
 W_m=(2m+1)\operatorname{Cat}_m,                  \tag{3.6}
\]

the proved relative defect obeys

\[
 \frac{\operatorname{Cat}_{m-6}}{W_m}
 \sim\frac{1}{2\cdot4^6m}
 =\frac1{8192m}.                                   \tag{3.7}
\]

Thus the theorem gives an unconditional `Omega(W_m/m)` missing family.
The exact census below is much larger and suggests a positive limiting
fraction, but no such limit is claimed here.

## 4. Exact finite all-width census

The program `msw_shadow_test.cpp` reconstructs the canonical `g,h` maps,
the omitted-label order (1.2), and every cyclic interval independently.
The immediate-upper defect, equivalently the rank-`(m-1)` defect, is

\[
\begin{array}{c|r|r|c}
m&\binom{2m+1}{m-1}&\text{missing}&\text{fraction}\\ \hline
4&84&4&0.047619\\
5&330&32&0.096970\\
6&1287&176&0.136752\\
7&5005&837&0.167233\\
8&19448&3709&0.190713\\
9&75582&15811&0.209190\\
10&293930&65860&0.224067\\
11&1144066&270337&0.236295
\end{array}                                        \tag{4.1}
\]

At `m=11`, complementation converts the complete lower-depth census into
the following upper census:

\[
\begin{array}{c|rrrrrrrrr}
\text{upper rank}&13&14&15&16&17&18&19&20&21\\ \hline
\text{missing}&270337&286787&197038&100863&38991&11086&2168&249&0.
\end{array}                                        \tag{4.2}
\]

Here the owner rank is `12`; ranks `12` and below are omitted from the
upper table, and ranks `22,23` are also complete.  These are exact finite
integer censuses, not evidence for a proved asymptotic formula.

## 5. No bounded local or exterior repair of the canonical chronology

### Lemma 5.1 (cyclic window stability)

Change `s` adjacency transitions in a collection of cyclic orders.  At
interval length `ell`, at most `ell s` old starts and at most `ell s` new
starts contain a changed transition.  Hence at most `ell s` previously
missing named targets can be introduced.

### Proof

A fixed directed transition belongs to at most `ell` cyclic intervals of
length `ell`.  Union-bound over the changed transitions. \(\square\)

Applying the lemma with `ell=m+2` and Theorem 3.1 shows that any repair of
the canonical factor which works by changing only chronology transitions
must change at least

\[
 \frac{\operatorname{Cat}_{m-6}}{m+2}             \tag{5.1}
\]

transitions.  In particular:

* no bounded packet bank whose packets change `O(1)` transitions can fix
  the row;
* no bounded number of exterior insertions, cuts, or splices can fix it,
  because each changes only `O(1)` local transitions; and
* no polynomial-size local repair bank can fix the explicit missing family.

The same conclusion follows in the source chronology: a bounded exterior
edit changes only `O(q)` windows of source width `q+1`, whereas (3.3) is
exponential in `m`.

This does **not** rule out a globally different minimum-cycle factor or a
Catalan-scale coherent rethreading.  It proves that the canonical MSW
factor is an exact owner/immediate-lower skeleton whose upper completion is
global, not a bounded postprocessing problem.

## 6. Consequence for the long-aperture route

The canonical odd MSW route gives, unconditionally:

\[
 \boxed{\text{exact owners} + \text{exact immediate lowers}
 + \text{flat biresidence}.}                       \tag{6.1}
\]

It does not give all-width upper coverage.  The first failed row is already
the immediate upper rank, with the explicit family (3.2).  Therefore the
remaining alternatives are sharply:

1. replace the canonical factor by a globally upper-aware wreath factor;
2. perform a Catalan-scale rethread selected simultaneously with the upper
   witnesses; or
3. abandon this exact skeleton and use a different global carrier.

Treating the missing upper row as a bounded exceptional bank is impossible
within the canonical chronology.
