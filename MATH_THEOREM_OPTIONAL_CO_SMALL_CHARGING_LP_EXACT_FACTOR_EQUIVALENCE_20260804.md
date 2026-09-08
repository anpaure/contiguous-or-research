# Optional co-small charging is exactly the residual two-factor problem

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves that the
proposed generalized owner-to-facet charging LP is not a weaker way to
close the optional co-small cuts: it is exactly the fractional residual
two-factor polytope, and hence, by bipartite integrality, is feasible if
and only if the protected path bank already extends to a spanning
two-factor.  Equivalently, the optional gap-saturation functional is the
complete residual Hall dual after complementation.  The theorem also
gives the canonical extremal optional banks and their exact local closure
conditions.

No computation, search, or solver result is used.

## 0. Setup

Let

\[
 \mathcal L=\binom{[2m-1]}{m-1},
 \qquad
 \mathcal U=\binom{[2m-1]}m,
\]

and let `P` be the incidence lift of a family of simple owner paths.  Thus
every protected lower colour has protected degree two and every other
lower vertex has protected degree zero.  Put

\[
 Z=\{x\in\mathcal L:d_P(x)=2\},
 \qquad X=\mathcal L\setminus Z.
\tag{0.1}
\]

For an owner `U`, write

\[
 G_U=N(U)\cap X,
 \qquad g_U=|G_U|,
 \qquad c_U=2-d_P(U).
\tag{0.2}
\]

Every protected edge has its lower endpoint in `Z`, and

\[
 |E(P)|=2|Z|.
\tag{0.3}
\]

Since the two middle-level shores have equal size,

\[
 \boxed{\sum_{U\in\mathcal U}c_U=2|X|.}
\tag{0.4}
\]

For `B subseteq X`, put

\[
 b_U(B)=|B\cap G_U|,
\]

and retain the exact optional unpaid-load functional

\[
 \Omega_P(Z\cup B)
 =\sum_U\left[
 c_U\mathbf1_{\{b_U=g_U\}}
 +\mathbf1_{\{c_U=2\}}
  \mathbf1_{\{b_U=g_U-1\}}
 \right].
\tag{0.5}
\]

The second indicator is interpreted as zero when `g_U-1<0`.

## 1. A single convex formula for the unpaid load

### Lemma 1.1 (gap-overflow form)

For every optional bank `B`,

\[
 \boxed{
 \Omega_P(Z\cup B)
 =\sum_{U\in\mathcal U}
   \bigl(b_U(B)-(g_U-c_U)\bigr)_+.}
\tag{1.1}
\]

This identity remains valid even when the forced-bank base condition
fails.

#### Proof

There are only three possible capacities.

* If `c_U=0`, both sides vanish.
* If `c_U=1`, the positive part is one exactly when `b_U=g_U`.
* If `c_U=2`, the positive part is one at `b_U=g_U-1`, two at
  `b_U=g_U`, and zero below those two occupancies.

These are exactly the two terms in (0.5). \(\square\)

Thus the optional obstruction is a sum of convex threshold-overflow
functions.  In particular it is supermodular as a function of `B`.

## 2. Complementation gives the complete residual Hall dual

Delete the protected edges and give every owner residual capacity `c_U`.
Only the lower vertices in `X` have positive residual demand, and each of
them has demand two.  For `A subseteq X`, let

\[
 \kappa_P(A)=
 \sum_U\min\{c_U,|A\cap G_U|\}
\tag{2.1}
\]

be its residual-capacity supply.

### Theorem 2.1 (exact optional-complement identity)

For every `B subseteq X`, with `A=X setminus B`,

\[
 \boxed{
 \kappa_P(X\setminus B)-2|X\setminus B|
 =2|B|-\Omega_P(Z\cup B).}
\tag{2.2}
\]

Consequently the full residual two-factor deficiency is

\[
 \boxed{
 \delta(P)
 =\max_{B\subseteq X}
   \bigl(\Omega_P(Z\cup B)-2|B|\bigr).}
\tag{2.3}
\]

In particular,

\[
 \boxed{
 \Omega_P(Z\cup B)\le2|B|\quad\hbox{for every }B\subseteq X}
\tag{2.4}
\]

holds if and only if `P` extends to a spanning two-factor.

#### Proof

At owner `U`, the complement `A=X setminus B` occupies `g_U-b_U`
optional residual incidences.  Hence the capacity lost relative to the
full owner capacity is

\[
 c_U-\min\{c_U,g_U-b_U\}
 =\bigl(b_U-(g_U-c_U)\bigr)_+.
\]

Summing, using Lemma 1.1 and (0.4), gives

\[
 \begin{aligned}
 \kappa_P(A)-2|A|
 &=\sum_Uc_U-\Omega_P(Z\cup B)-2(|X|-|B|)\\
 &=2|B|-\Omega_P(Z\cup B),
 \end{aligned}
\]

which is (2.2).

A lower vertex in `Z` has residual demand zero.  Removing such a vertex
from any Hall shore cannot decrease its deficiency.  Thus the maximum
residual Hall deficiency may be taken over `A subseteq X`.  Complementing
`A` inside `X` and applying (2.2) proves (2.3).  The capacitated bipartite
Hall theorem now gives (2.4). \(\square\)

This shows that the phrase "optional co-small inequality for every `B`"
already asks for the complete extension theorem.  It is not an
independent local subproblem once the quantifier ranges over all optional
banks.

## 3. The proposed generalized charging LP

Consider nonnegative variables

\[
 w_{U,x}\qquad(x\in G_U)
\]

subject to

\[
 \sum_{U\supset x}w_{U,x}\le2
 \qquad(x\in X),
\tag{3.1}
\]

\[
 \sum_{x\in G_U}w_{U,x}\ge c_U
 \qquad(U\in\mathcal U),
\tag{3.2}
\]

and, for every unprotected owner `U` and every `y in G_U`,

\[
 \sum_{x\in G_U\setminus\{y\}}w_{U,x}\ge1.
\tag{3.3}
\]

Condition (3.2) pays a completely filled optional gap; (3.3) pays an
unprotected gap missing one facet; and (3.1) caps the charge received by
one optional lower vertex.

### Theorem 3.1 (charging-LP equivalence and circularity)

The following are equivalent.

1. The charging system (3.1)--(3.3) is feasible.
2. The residual incidence graph has a fractional `b`-matching with lower
   degrees two and owner degrees `c_U`, with unit edge capacities.
3. The residual incidence graph has an integral such `b`-matching.
4. The protected path bank `P` extends to a spanning two-factor.
5. Every optional bank satisfies (2.4).

Therefore the generalized charging LP is exactly the residual
two-factor polytope.  Its feasibility cannot serve as a noncircular proof
of the optional co-small gate.

#### Proof

Sum (3.1) over `x` and (3.2) over `U`.  Equation (0.4) gives

\[
 2|X|
 \ge\sum_{Ux}w_{U,x}
 \ge\sum_Uc_U
 =2|X|.
\]

Every inequality is therefore tight.  In particular,

\[
 \sum_{U\supset x}w_{U,x}=2,
 \qquad
 \sum_{x\in G_U}w_{U,x}=c_U.
\tag{3.4}
\]

If `c_U<=1`, its row equality already gives `w_{U,x}<=1`.  If
`c_U=2`, (3.3) and (3.4) give

\[
 w_{U,y}
 =2-\sum_{x\ne y}w_{U,x}
 \le1.
\]

Thus `w` is precisely the fractional `b`-matching in item 2.

Conversely, a fractional residual `b`-matching satisfies (3.1)--(3.2).
At a capacity-two owner its unit edge bounds imply

\[
 \sum_{x\ne y}w_{U,x}=2-w_{U,y}\ge1,
\]

so (3.3) also holds.  This proves `1 iff 2`.

The bipartite `b`-matching polytope with integral vertex demands,
capacities, and unit edge bounds is integral, proving `2 iff 3`.  Adding
the integral residual matching to `P` gives exactly a spanning
two-factor, proving `3 iff 4`.  Finally Theorem 2.1 and capacitated Hall
give `4 iff 5`. \(\square\)

### Corollary 3.2 (the harmonic weights are one rigid interior ansatz)

The harmonic choice

\[
 w_{U,x}={c_U\over g_U}
\tag{3.5}
\]

is one special row-uniform point of the polytope in Theorem 3.1.  Its
column equations are exactly `Gamma_P(x)=2`.  Failure of pointwise
harmonic balance does not obstruct a residual factor; it only obstructs
this row-uniform ansatz.  Any successful nonuniform redistribution,
however, is already a fractional factor and rounds integrally.

## 4. Canonical optional obstruction banks

Define

\[
 \Psi_P(B)=\Omega_P(Z\cup B)-2|B|.
\tag{4.1}
\]

By Lemma 1.1, `Psi_P` is supermodular.  Let

\[
 \mathfrak B=
 \operatorname*{argmax}_{B\subseteq X}\Psi_P(B).
\]

### Theorem 4.1 (optional DM lattice)

The family `mathfrak B` is closed under union and intersection.  Hence it
has unique inclusion-minimal and inclusion-maximal members

\[
 B^-=\bigcap_{B\in\mathfrak B}B,
 \qquad
 B^+=\bigcup_{B\in\mathfrak B}B.
\tag{4.2}
\]

They are the complements in `X` of the maximal and minimal residual DM
shores respectively.

For `B subseteq X`, put

\[
 q_B^-(x)=
 |\{U\supset x:b_U(B)\ge g_U-c_U+1\}|,
 \qquad x\in B,
\tag{4.3}
\]

and

\[
 q_B^+(y)=
 |\{U\supset y:b_U(B)\ge g_U-c_U\}|,
 \qquad y\notin B.
\tag{4.4}
\]

If the maximum deficiency is positive, then

\[
 \boxed{q_{B^-}^-(x)\ge3\qquad(x\in B^-),}
\tag{4.5}
\]

and

\[
 \boxed{q_{B^+}^+(y)\le1\qquad(y\in X\setminus B^+).}
\tag{4.6}
\]

Thus every member of the minimal optional obstruction bank participates
in at least three already-overflowing owner gaps, while every excluded
vertex of the maximal bank can trigger at most one threshold-ready gap.

#### Proof

For a convex cardinality function, summing over owner rows proves
supermodularity of (4.1).  If `B_1,B_2` are both maximizers, then

\[
 \Psi(B_1\cap B_2)+\Psi(B_1\cup B_2)
 \ge2\max\Psi.
\]

Neither term exceeds the maximum, so both are maximizers.  This proves
the lattice assertion.  The complement correspondence follows directly
from (2.2).

Removing `x in B` changes the objective by

\[
 \Psi(B)-\Psi(B\setminus\{x\})=q_B^-(x)-2,
\tag{4.7}
\]

because an owner overflow drops by one exactly when its old occupancy is
at least `g_U-c_U+1`.  No proper subset obtained by deleting an element
from `B^-` is a maximizer, so (4.7) is strictly positive, proving (4.5).

Similarly,

\[
 \Psi(B\cup\{y\})-\Psi(B)=q_B^+(y)-2.
\tag{4.8}
\]

Maximality of `B^+` makes (4.8) strictly negative, proving (4.6).
\(\square\)

The corresponding nonempty block conditions are exact: for every
`D subseteq B^-`,

\[
 \sum_U\left[
  (b_U-(g_U-c_U))_+
  -(b_U-|D\cap G_U|-(g_U-c_U))_+
 \right]>2|D|,
\tag{4.9}
\]

and for every nonempty `E subseteq X setminus B^+`,

\[
 \sum_U\left[
  (b_U+|E\cap G_U|-(g_U-c_U))_+
  -(b_U-(g_U-c_U))_+
 \right]<2|E|.
\tag{4.10}
\]

They are simply the optional-complement forms of strict irreducibility of
the two canonical DM shores.

## 5. Exact implication for the proof programme

The generalized charging proposal settles the optional bank only if it
constructs the residual factor itself.  The total-mass equality (0.4)
leaves no disposable fractional slack: every owner row and every lower
column is forced tight, while the near-full constraints are exactly the
unit incidence bounds.

Accordingly, a noncircular co-small argument must use information absent
from (3.1)--(3.3), for example:

1. the **localized size restriction** on `B`, rather than all optional
   banks;
2. structural impossibility of the canonical threshold conditions
   (4.5)--(4.6) inside the constant-spread path reservoir;
3. correlations between full/almost-full owner gaps which prevent them
   from coexisting in one small `B`; or
4. a direct construction of the residual factor, in which case the
   co-small gate and every other Hall gate close simultaneously.

In particular, replacing the harmonic weights by arbitrary ownerwise
weights does not weaken the theorem to be proved.  The precise remaining
co-small target is to rule out a **localized** positive maximizer of
`Psi_P`, not to solve the unrestricted charging LP.

## 6. Dependencies

| role | file | SHA-256 |
|---|---|---|
| residual-capacity Hall and DM theorem | `MATH_THEOREM_PROTECTED_ORE_RESIDUAL_CAPACITY_DM_UNCROSSING_20260804.md` | `fd528c5cb0fa2c50af611271ee3ef1f0bbbcc1849cee7226335ebb88c8dd2bf2` |
| exact optional gap functional and harmonic ansatz | `MATH_THEOREM_CO_SMALL_FORCED_Q1_HARMONIC_GAP_CERTIFICATE_20260804.md` | `4a5d0993d7c3e2eb54198c2b6278670649308f7aeb3dd1de046b18742db0a85a` |
| base-safe forced q1 construction | `MATH_THEOREM_CO_SMALL_BASE_SAFE_Q1_FORBIDDANCE_20260804.md` | `c17615960cf7a9ff551125d72b69849b97181b41e1cd234d8a3b58820d7faf7a` |
