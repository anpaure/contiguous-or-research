# Rectangular rearrangement orbits are a subtractive Euclidean algorithm

**Date:** 2026-08-05  
**Method:** pure mathematics; no search or solver  
**Status:** unconditional exact no-go in the natural measurable extension
of the anchored-component operator.  A zero-area positive-prefix,
negative-tail kernel can retain that sign order for arbitrarily many
iterates and then land on a nonzero sign-reversed fixed point.  Hence no
finite collection of initial one-crossing or origin-slack checks can imply
orbit convergence.  The example is piecewise constant and is not a
counterexample to the specific continuous Rayleigh orbit.

## 1. The family

Fix `b,L>0`.  For `r>0`, define, up to immaterial endpoint values,

\[
 F_r(t)=br\,\mathbf1_{[0,L]}(t)
       -b\,\mathbf1_{(L,(1+r)L]}(t).              \tag{1.1}
\]

Its positive and negative masses are both `brL`, so

\[
 \int F_r=0.                                      \tag{1.2}
\]

For every depth `0<s<b`, the negative superlevel set is the single
interval `(L,(1+r)L]`, of length `rL`.  Therefore its anchored component
profile is

\[
 C_{F_r}(t)=b\,\mathbf1_{[0,rL]}(t).              \tag{1.3}
\]

The layer-cake proof of the rearrangement inequality applies verbatim to
these measurable step kernels.

## 2. Exact orbit

### Theorem 2.1

If `r>1`, then

\[
 \boxed{\mathcal RF_r=F_{r-1}.}                   \tag{2.1}
\]

If `r=1`, then

\[
 \boxed{\mathcal RF_1=0.}                         \tag{2.2}
\]

If `0<r<1`, then

\[
 \mathcal RF_r
 =-b(1-r)\mathbf1_{[0,rL]}
  +br\mathbf1_{(rL,L]},                           \tag{2.3}
\]

and the kernel on the right of (2.3) is a nonzero fixed point of
`mathcal R`.

### Proof

Subtract (1.3) from the positive part of (1.1).  When `r>1`, the profile
`C_{F_r}` covers `[0,L]` and continues to `rL`; hence

\[
 \mathcal RF_r
 =b(r-1)\mathbf1_{[0,L]}
  -b\mathbf1_{(L,rL]},
\]

which is exactly `F_(r-1)`.  At `r=1` the two equal rectangles cancel.

When `0<r<1`, the profile ends at `rL<L`, giving (2.3).  Its negative
part is a constant nonincreasing initial block and its positive part is
disjoint and lies immediately afterward.  Rearranging the negative block
does nothing, so another application of `mathcal R` leaves (2.3)
unchanged. `square`

### Corollary 2.2

Write `r=m+theta`, where `m=floor(r)` and `0<=theta<1`.

* If `theta=0`, the orbit reaches zero after exactly `m` transforms.
* If `theta>0`, the first `m` transforms successively replace `r` by
  `r-1`, and the next transform lands on the nonzero fixed point (2.3)
  with parameter `theta`.

Thus

\[
 \boxed{
 \|\mathcal R^nF_r\|_1\to0
 \quad\Longleftrightarrow\quad r\in\mathbb N.}
 \tag{2.4}
\]

## 3. Consequences for proposed Rayleigh invariants

For any prescribed integer `N`, choose `r in (N,N+1)`.  Then the first
`N` orbit points are nonzero positive-prefix/negative-tail kernels with
one negative superlevel component at every active depth and with strict
positive origin value.  Nevertheless the orbit subsequently becomes a
nonzero sign-reversed fixed point.

In particular, none of the following data, taken for only finitely many
initial iterates, proves convergence:

1. one sign crossing;
2. one negative component per superlevel;
3. strict origin slack `H_n(0)>0`; or
4. exact `L1` dissipation at those finitely many steps.

The signed first moment is negative throughout the positive-prefix phase
and becomes strictly positive exactly on the terminal fixed face.  This
shows why the all-iterate nonpositive-moment barrier is a substantive
invariant rather than a restatement of finitely many shape checks.

The theorem does **not** refute the Rayleigh rearrangement-orbit lemma.
The Rayleigh kernel is smooth, has Gaussian tails, and carries special
differential relations absent from (1.1).  It does refute any proof that
uses only the generic component rearrangement algebra plus finitely many
initial sign/count checks.

