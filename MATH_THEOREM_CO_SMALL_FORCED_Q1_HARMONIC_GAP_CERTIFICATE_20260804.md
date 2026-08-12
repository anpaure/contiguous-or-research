# Co-small forced-q1 harmonic gap certificate

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  For an incidence-lift
protected bank, it gives a sharp fractional charging certificate which
closes every co-small Ore cut whose complement contains the forced
protected lower bank.  The certificate has exact mean two; consequently a
uniform pointwise proof requires perfect harmonic balance, not merely
average spread.

No computation, search, or solver result is used.

## 0. Forced and optional complement banks

Use the notation of the residual-capacity DM theorem.  Assume `P` is the
incidence lift of simple owner paths, and put

\[
 Z=\{x\in\mathcal L:d_P(x)=2\}.
\tag{0.1}
\]

Then

\[
 2|Z|=|E(P)|.
\tag{0.2}
\]

Every complement of a minimal co-small deficient shore has the form

\[
 C=Z\mathbin{\dot\cup}B.
\tag{0.3}
\]

For an owner `U`, define

\[
 z_U=|N(U)\cap Z|,
 \qquad
 g_U=m-z_U,
 \qquad
 b_U=|N(U)\cap B|,
 \qquad
 c_U=2-d_P(U).
\tag{0.4}
\]

Thus `g_U` is the number of owner facets not already forced into the
complement, and `0<=b_U<=g_U`.

The exact unpaid near-clique load is

\[
 \Omega_P(Z\cup B)
 =\sum_U\left[
 c_U\mathbf1_{\{b_U=g_U\}}
 +\mathbf1_{\{d_P(U)=0\}}
  \mathbf1_{\{b_U=g_U-1\}}
 \right].
\tag{0.5}
\]

The complementary cut is safe exactly when

\[
 \Omega_P(Z\cup B)\le2|B|.
\tag{0.6}
\]

## 1. The forced-bank base condition

At `B=emptyset`, the unpaid load is

\[
 \boxed{
 \Omega_P(Z)
 =\sum_{U:g_U=0}c_U
  +|\{U:g_U=1,\ d_P(U)=0\}|.}
\tag{1.1}
\]

Hence the base forced bank is safe if and only if

\[
 \boxed{
 g_U=0\Longrightarrow d_P(U)=2,
 \qquad
 g_U=1\Longrightarrow d_P(U)\ge1.}
\tag{1.2}
\]

This is necessary for any all-`B` charging certificate, because the right
side of (0.6) vanishes at `B=emptyset`.

## 2. Harmonic gap load

Assume (1.2).  For every optional lower vertex `x notin Z`, define

\[
 \boxed{
 \Gamma_P(x)
 =\sum_{U\supset x}{c_U\over g_U}.}
\tag{2.1}
\]

Every denominator in this sum is positive because `x` itself is a facet
outside `Z`.

### Theorem 2.1 (harmonic charging certificate)

For every optional bank `B subseteq mathcal L setminus Z`, one has

\[
 \boxed{
 \Omega_P(Z\cup B)
 \le\sum_{x\in B}\Gamma_P(x).}
\tag{2.2}
\]

Consequently, if

\[
 \boxed{\Gamma_P(x)\le2\qquad(x\notin Z),}
\tag{2.3}
\]

then every co-small cut whose complement contains `Z` is safe.

#### Proof

Fix an owner.

If `b_U=g_U`, its unpaid contribution is `c_U`, while charging every one
of its `b_U` optional facets by `c_U/g_U` pays exactly `c_U`.

Suppose instead that `d_P(U)=0` and `b_U=g_U-1`.  Its unpaid contribution
is one.  Condition (1.2) excludes `g_U=1`, so `g_U>=2`; hence

\[
 {c_U\over g_U}b_U
 ={2(g_U-1)\over g_U}\ge1.
\]

All other owner contributions vanish.  Summing these owner-wise charges
and reversing the incidence sum proves (2.2).  Equation (2.3) then gives

\[
 \Omega_P(Z\cup B)
 \le2|B|,
\]

which is (0.6). \(\square\)

## 3. Exact mean-two law

### Theorem 3.1 (harmonic balance identity)

Under the base condition (1.2),

\[
 \boxed{
 \sum_{x\notin Z}\Gamma_P(x)=2|\mathcal L\setminus Z|.}
\tag{3.1}
\]

Thus the average harmonic gap load is exactly two.  In particular, the
pointwise certificate (2.3) holds if and only if

\[
 \boxed{\Gamma_P(x)=2\qquad(x\notin Z).}
\tag{3.2}
\]

#### Proof

Reverse the order of summation in (2.1).  An owner with `g_U>0`
contributes

\[
 g_U{c_U\over g_U}=c_U.
\]

When `g_U=0`, condition (1.2) gives `c_U=0`.  Therefore

\[
 \sum_{x\notin Z}\Gamma_P(x)
 =\sum_Uc_U
 =2|\mathcal U|-|E(P)|.
\]

The two shores have the same size and (0.2) gives

\[
 2|\mathcal U|-|E(P)|
 =2(|\mathcal L|-|Z|).
\]

This proves (3.1).  A family of numbers with average two is everywhere at
most two exactly when every number equals two, proving (3.2).
\(\square\)

## 4. Exact frontier

The theorem turns the co-small closure problem into two concrete design
conditions on the protected q1 bank:

1. no residual-capacity owner is already full, and no unprotected owner
   is already almost full, in the forced bank `Z`;
2. the reciprocal forced gaps balance to the exact value two at every
   optional lower vertex.

The second condition is sharp: average spread, even exact average two,
cannot imply it.  A nonuniform protected reservoir necessarily has some
`Gamma_P(x)>2`, and Theorem 2.1 alone cannot close optional banks
concentrated on those vertices.  One then needs either a different
fractional allocation of near-clique units or a structural theorem showing
that no DM complement can concentrate in the positive-harmonic region.

## 5. Dependency

| role | file | SHA-256 |
|---|---|---|
| residual-capacity DM and exact co-small gap form | `MATH_THEOREM_PROTECTED_ORE_RESIDUAL_CAPACITY_DM_UNCROSSING_20260804.md` | `fd528c5cb0fa2c50af611271ee3ef1f0bbbcc1849cee7226335ebb88c8dd2bf2` |

