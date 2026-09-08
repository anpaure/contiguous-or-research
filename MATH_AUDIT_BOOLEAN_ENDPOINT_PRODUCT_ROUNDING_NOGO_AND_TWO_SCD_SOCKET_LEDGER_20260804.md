# Independent audit: Boolean product-rounding no-go and two-SCD socket ledger

**Date:** 2026-08-04  
**Status:** independent line-by-line mathematical audit; PASS with the scope
limitations stated below.  No computation or solver result is used.

Audited theorem:

`MATH_THEOREM_BOOLEAN_ENDPOINT_PRODUCT_ROUNDING_NOGO_AND_TWO_SCD_SOCKET_LEDGER_20260804.md`.

## 1. Product-rounding probability

At rank `r-1`, slot `j` selects any fixed named target with probability
`x_j=p_j/a`.  The fractional rank transportation gives

\[
 0\le x_j\le1/a,\qquad\sum_jx_j=1.
\]

For independent slots the miss probability is `prod_j(1-x_j)`.  Moving
mass between two nonextreme coordinates toward an endpoint decreases the
product while preserving the sum.  The minimizing vector consequently has
`a` entries `1/a`, so the miss probability is at least
`(1-1/a)^a>=1/4`.  Summation gives `E Z>=a/4`.

Changing one slot changes the number of empty rank-`r-1` targets by at most
one.  McDiarmid with deviation `a/8` gives exactly

\[
 \Pr(Z<a/8)\le e^{-a^2/(32n)}.
\]

Because `a/W` tends to one and `n/W` tends to one, the exponent is
`-Omega(W)`.  One slot can newly cover at most one hole in this rank, so
`a/8` holes require at least `a/8` altered slots.  The theorem correctly
rules out product sampling plus `o(W)`-slot alteration, not arbitrary
dependent rounding or rare product outcomes.

## 2. Collar attachment equivalence

The collar SCD covers every target in ranks `m-d,...,m-1` exactly once.
The residual SCD covers every target below rank `m-d` exactly once.  A
residual chunk can be prepended to a nonempty collar exactly when its top
is contained in the collar bottom; the load inequality is exact.  Empty
and boundary sockets impose only their scalar capacity at the static level.
Therefore a collar-preserving exact partition is precisely a matching
saturating the residual chunks.  Hall's condition is both necessary and
sufficient within this face.

## 3. Exact capacity identity

For each lower SCD length `L`,

\[
 (d-L)_+-(L-d)_+=d-L.
\]

Summing over the `W` chains gives `K-E=dW-Lambda`; adding boundary capacity
`binom(d+1,2)` gives the exact vacancy `sigma`.  The deletion of the empty
set is already included in the definition `L(C)=|C cap mathcal L|`, so no
off-by-one remains in this identity.

## 4. Socket and chunk census

SCD chains with lower length below `d` start strictly above rank `m-d`.
Their count telescopes to

\[
                         W-{2m\choose m-d}.
\]

For the augmented lower segment including the empty set, the number of
`d`-chunks below the collar is

\[
                         \sum_{q\ge1}{2m\choose m-qd-1}.
\]

Deleting the unique empty set changes this number by at most one, which is
the stated `O(1)`.  The local central-binomial limit with
`d^2/m -> pi/4` gives the two asserted limits.  Gaussian domination
justifies summing over `q`.  The displayed geometric tail proves the strict
numerical gap without relying on a decimal coincidence.

## 5. Scope

The theorem does not prove the typed Hall inequalities.  In particular,
raw socket count and total capacity do not imply a matching because socket
capacities and Boolean containment neighborhoods are correlated.  Empty
and boundary sockets are unanchored in this static theorem.  No distinct
owner, left-endpoint, countdown, upper, residence, topology, or common-cap
claim is made.

Within those boundaries, the theorem and all displayed identities PASS.

