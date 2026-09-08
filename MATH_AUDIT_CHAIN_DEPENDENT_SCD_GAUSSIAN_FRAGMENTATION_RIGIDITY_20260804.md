# Independent audit: chain-dependent SCD Gaussian fragmentation rigidity

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_CHAIN_DEPENDENT_SCD_GAUSSIAN_FRAGMENTATION_RIGIDITY_20260804.md`  
**Verdict:** PASS, with the scope stated in Section 6 of the theorem.  This
is an asymptotic necessity and obstruction theorem, not an existence
theorem for the Rayleigh fragmentation or the literal cross-SCD matching.

## 1. Exact SCD censuses

An SCD of `B_(2r)` has `H_b=C_b-C_(b-1)` chains beginning at rank `b`.
The augmented residual length is `t-b`; deleting the empty set alters only
the unique `b=0` chain by one cell.  A collar chain beginning at `t+u`
has exactly capacity `u`, and the endpoint triangle supplies one further
capacity-`u` socket.  These facts give (1.1)--(1.2) exactly up to the
declared one-cell puncture.

The cumulative sums telescope:

\[
 \sum_{b\le B}H_b=C_B,
 \qquad
 \sum_{u\ge q}H_{t+u}=W-C_{t+q-1}.
\]

Thus the two tails used in (1.7) and (1.10) are correct.

## 2. Gaussian scaling and moments

The local central-binomial ratio at distance `z sqrt(r)` is
`exp(-z^2)`, not `exp(-2z^2)`; this agrees with the convention
`C_s=binom(2r,s)`.  Differentiating the two limiting tails gives exactly

\[
 2(A+x)e^{-(A+x)^2},qquad
 2(A-y)e^{-(A-y)^2}.
\]

Both moment calculations were redone.  The source moment is
`int_A^infty exp(-z^2) dz`; the socket moment is
`A-int_0^A exp(-z^2) dz`.  They agree precisely because
`A=sqrt(pi)/2=int_0^infty exp(-z^2) dz`.  This is also consistent with the
exact scalar ledger.

## 3. Rigidity proof

The threshold cuts give stochastic tail domination of every subsequential
chunk limit by `mu` away from zero.  Minimality of `d` gives
`0<=sigma_r<W+d`, hence the normalized first-moment gap tends to zero.
The layer-cake identity converts equality of first moments into equality
of all positive tails.  The `q=1` cut then rules out an extra atom at zero.
No unjustified interchange of an infinite sum is used: all chunk measures
have uniformly bounded mass and compact support, while the source-tail
tightness is Gaussian.

The same argument tolerates an `o(W)` maximum additive threshold error.
Therefore a different weak limit forces a linear violation along a
subsequence, as claimed.

## 4. Minimum and balanced rules

For one length `L`, the minimum number of pieces is `ceil(L/d)`.  Summing
its tail representation over the SCD start census yields

\[
 \sum_{m\ge1}e^{-\pi m^2/4}
\]

after normalization.  The geometric estimate beginning at `m=2` is valid
because `(m+1)^2-m^2>=5` there.  The displayed elementary exponential
bounds give the strict separation from `1-e^(-pi/4)` with room to spare.
Hence the obstruction is independent of all cut positions.

For balanced pieces, the `m=1` source rows alone give a top-tail density
linear in `epsilon`; the socket tail is quadratic in `epsilon`.  Extra
contributions from `m>=2` can only strengthen the violation.  The stated
top-threshold no-go is therefore valid.

## 5. Literal matching waste

Every used socket contributes capacity minus chunk length, and every unused
socket contributes its whole capacity.  Summing gives total socket
capacity minus total residual demand, exactly `sigma_r`.  Markov's
inequality at scale `epsilon sqrt(r)` yields `O(W/sqrt(r))=o(W)` exceptional
sockets.  The joint-limit diagonal statement follows.

## 6. Scope audit

The theorem proves none of the following:

* existence of a fragmentation of `nu` into `mu`;
* an integral discrete cutting with bounded rather than linear defect;
* literal containment Hall for a fixed or correlated SCD pair;
* extension of selected socket roots to a full SCD;
* upper palettes, residence, chronology, topology, or common-cap routing.

It correctly proves that all of those constructions, if coefficient-one,
must sit on the unique zero-waste Gaussian fragmentation face.  The odd
statement is asymptotic only; parity corrections are explicitly not
claimed exact.
