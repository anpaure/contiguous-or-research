# Independent-style audit: complete pair-slice parity and leakage theorem

**Date:** 2026-08-05  
**Audited file:**
`MATH_THEOREM_COMPLETE_PAIR_SLICE_TARGET_EXACT_PARITY_AND_LINEAR_LEAKAGE_NOGO_20260805.md`  
**Method:** pure mathematics; no computation, search, or solver  
**Verdict:** **GO**, with the full triangular middle-layer application
explicitly outside scope.

## 1. Literal semantics

For

\[
 X_i=K\cup\{i\},
 \qquad
 T_{ij}=K\cup\{i,j\},
\]

the depth-one trace `X_i -> X_j` has owner

\[
 X_i\cup X_j=T_{ij}
\]

and proper suffix target `X_j`.  Thus marked and unmarked copies have the
same literal state boundary and owner while differing only in whether the
head occurrence is charged to the named target bank.  The theorem's model
is a genuine Boolean trace slice.

## 2. Fractional ledger

For one unordered owner, the total marked mass is

\[
 {2\over n-1}
\]

and the total unmarked mass is

\[
 2{n-3\over2(n-1)}={n-3\over n-1}.
\]

Their sum is one.  In either direction the combined mass is

\[
 {1\over n-1}+{n-3\over2(n-1)}={1\over2}.
\]

Hence every state receives and emits `(n-1)/2`, while every target receives
`n-1` marked incoming copies of weight `1/(n-1)`.  The support is the
complete bidirected graph and is connected.  All four fractional rows are
therefore exact.

## 3. Separate integral owner/target projection

A directed Hamilton cycle uses `n` distinct pair owners and has every state
as head once.  Mark those arcs and orient every other owner arbitrarily and
unmarked.  This proves exact owner and target integrality without making any
state-balance claim.

## 4. Even-order parity and repair cost

Any one-copy owner selection is an orientation of `K_n`.  At vertex `i`,

\[
 b_i=2\operatorname{out}(i)-(n-1).
\]

For even `n`, every `b_i` is odd.  Since `sum_i b_i=0`, the total positive
imbalance is at least `n/2`.  A directed trail has one positive boundary
unit, and one added arc can reduce positive imbalance by at most one.  The
claimed lower bounds `n/2`, `n/2`, and `n/2-1` for trail decomposition,
circuit repair, and open-trail repair follow.

Orientation reversal changes the two endpoint imbalances by `plus/minus 2`,
so parity is invariant under every internal exchange.  Deleting one owner
edge toggles only two vertex parities, proving the `(n-2)/2` deletion floor.

Inside a larger chronology, every slice vertex begins with odd internal
degree.  Balance requires an odd number of external incidences at each of
the `n` vertices.  One external arc contributes at most two such incidences,
giving the exact linear leakage bounds.  Loops contribute two incidences at
one vertex and therefore do not weaken the parity argument.

## 5. Odd-order sharpness

For odd `n`, the cyclic tournament has equal indegree and outdegree
`(n-1)/2`.  Its step-one arcs form a directed Hamilton cycle; marking them
uses every target once.  The same cycle makes the entire selected support
connected.  Euler's theorem then gives one component.  Thus the obstruction
is genuinely parity-sharp.

## 6. Polyhedral consequence and scope

For even `n`, the combined polytope has an integral right-hand side and the
fractional point above, but no integral stationary point.  With owner sums
equal to one it is bounded.  Therefore its constraint matrix cannot be
totally unimodular.

The result rules out a black-box implication from exact marginals, regular
connected support, or separate factorization to bounded-defect Euler
rounding.  It does not show that the full triangular Boolean instance
contains an isolated even pair slice: cross-core arcs may provide the
linear leakage.  Accordingly it does not refute the desired all-`k`
integral rotor theorem or imply any bound on `nu(k)`.
