# Independent audit: nested Macaulay gate multi-run current

**Date:** 2026-08-04  
**Verdict:** **INDEPENDENT GO.**  The root nesting, least-active indexing,
active-core law, exact protected-current partition, rank-`q` category
counts, scalar slack formula, `T=1` specialization, and full-colex safety
criterion have all been rederived independently.  No theorem-level
correction is required.

This is a pure mathematical audit.  No finite search, computation, or
solver output is used.

## 1. Audited artifacts

| artifact | SHA-256 |
|---|---|
| `MATH_THEOREM_NESTED_MACAULAY_GATE_MULTI_RUN_CURRENT_20260804.md` | `0e63df633f3d89879b05ec076cb0254a5ab74036b5b7ff10d97225f5d236d5de` |
| `MATH_AUDIT_NESTED_MACAULAY_GATE_MULTI_RUN_CURRENT_SELF_20260804.md` | `3c663ef3f40ac94d5687600e3c85558cf0d74390a13331fddeeb2e69a1455f70` |

The self-audit is consistent with the independent derivation below, but
the present file is the independent audit.

## 2. Canonical run order and root nesting

For increasing Macaulay index `j`, the apertures

\[
 \rho_j=c_j-j+1
\]

are nondecreasing, because `c_(j+1)-c_j>=1`.  The theorem indexes maximal
constant-aperture runs in the opposite direction, from the largest
Macaulay indices downward.  Hence

\[
 \rho^{(0)}>\rho^{(1)}>\cdots>\rho^{(T)}.
\]

At the boundary between a lower-index run of aperture `rho_-` ending at
`b` and the next higher-index run of aperture `rho_+`, the common-root
formula gives

\[
 R_-=R_+\mathbin{\dot\cup}
 \{\rho_-+b+1,\ldots,\rho_++b\}.
\]

Thus the gate has size `rho_+-rho_-`.  Consecutive gate intervals lie
between consecutive pivot intervals, so the gates are pairwise disjoint
and avoid every pivot bank.  Induction proves

\[
 R_t=R_0\mathbin{\dot\cup}G_1\mathbin{\dot\cup}\cdots
      \mathbin{\dot\cup}G_t.
\]

Roots therefore grow with `t`.  It follows that the **least** active index
is indeed the uppermost active run.  This orientation is essential and is
correct in the theorem.

The isolated endpoint `c_m=n` is correctly removed before introducing
pivots: its formal pivot is `n+1`, while its complementary lower family is
the complete shore and has zero scalar and protected loss.

## 3. Active-core intersection and fibre size

Fix an active owner and let `t` be its least active index.  Every active
clause in run `t` has core `R_t+x`.

* If at least two pivots of that run are active, their core intersection is
  `R_t`.
* If exactly one pivot `x` is active and no later run is active, the global
  active-core intersection is `R_t+x`.
* If the pivot `x` is unique in run `t` but a later run `u>t` is active,
  then `R_u` contains `R_t` while all gates and pivots are disjoint from
  `x`; hence

  \[
   (R_t\cup\{x\})\cap(R_u\cup\{y\})=R_t.
  \]

These cases are disjoint and exhaustive, proving (1.1).  For a monotone
DNF, deletion of `z in U` leaves a selected facet exactly when at least one
active core omits `z`, equivalently when `z` is outside the intersection
`J_U`.  Thus `a_U=m-|J_U|`.  Condition `|R_T|+1<=m-2` makes every nonzero
fibre at least two, exactly as required by the protected-current argument.

## 4. Exact protected-current partition

At an owner of least active index `t`, the root part of `J_U` is

\[
 R_t=R_0\mathbin{\dot\cup}G_1\mathbin{\dot\cup}\cdots
      \mathbin{\dot\cup}G_t.
\]

Therefore a protected deletion in the root belongs to exactly one of
`xi_0,xi_1,...,xi_t`.  A pivot deletion occurs in `J_U` exactly when one
clause is active globally, in which case it belongs to exactly one
`eta_t`.  The coordinate banks are disjoint, so these currents are
pairwise disjoint; the active-core law makes them exhaustive.  This proves

\[
 \lambda_P(\mathcal D)=\xi_0+\sum_{i=1}^T\xi_i+
                        \sum_{t=0}^T\eta_t.
\]

On a resident owner path, the owners containing a fixed root form one
interval.  Any incidence deleting from that root is one of its at most two
boundary incidences.  Each pivot coordinate likewise has one occurrence
interval and at most two deleting boundary incidences.  The state
restrictions `tau>=i` and unique-clause activity only remove candidates.
Hence (2.2)--(2.4) follow with no missing factor.

For the clause-wise alternative, every coordinate in `J_U` lies in every
active core.  Since each individual clause fibre is at least two, any
protected deletion counted by the union loss is counted by the loss of at
least one active principal-star clause.  This verifies (2.5).

## 5. The `T=1` consistency check

For two runs, write the upper root as `R`, the lower additional gate as
`G`, and the upper and lower pivot banks as `Y,X`.  Then

\[
 (\xi_0,\eta_0,\xi_1,\eta_1)
 =(\xi_R,\eta_Y,\xi_G,\eta_X).
\]

Indeed, `tau>=1` means precisely that the upper run is inactive while the
lower run is active, and a sole active clause in run zero or one is exactly
an upper-only or lower-only unique hit.  This is the frozen strict-jump
four-current identity, so the indexing and shielding laws recover the
`T=1` theorem exactly.

## 6. Disjoint rank-category counts

Let `q` be `m-1` or `m`.  A rank-`q` set has least active run `t` exactly
when it

1. contains `R_t`;
2. avoids `X_0 union ... union X_(t-1)`; and
3. hits `X_t`.

Condition 1 automatically contains every earlier root, so condition 2 is
both necessary and sufficient to make all earlier runs inactive.  Later
activity is irrelevant to the least index.  The banks are disjoint, and
the ground set outside `R_t` has size

\[
 n-|R_t|=m+\rho_t.
\]

After excluding the `H_t` earlier pivots, subtraction of the choices
avoiding `X_t` gives exactly

\[
 |C_t(q)|=
 \binom{m+\rho_t-H_t}{q-|R_t|}
 -\binom{m+\rho_t-H_t-h_t}{q-|R_t|}.
\]

Every active rank-`q` set has one least active index, so the categories are
disjoint and exhaustive.  At `q=m-1,m`, the lower arguments are
`rho_t,rho_t+1`, respectively.  Since all nonzero owner fibres are
two-covered,

\[
 {\sigma(\mathcal D)\over2}
 =\sum_t\bigl(|C_t(m)|-|C_t(m-1)|\bigr),
\]

which is precisely (4.3).

At `T=1`, `C_0(q)` is the whole upper-run family, while `C_1(q)` is the
lower-run family with the upper pivot bank excluded.  Their sum is the
two-run union and is algebraically identical to the frozen
inclusion--exclusion formula.  Thus the scalar formula also passes the
`T=1` recovery test.

## 7. Canonical scalar identity and safety criterion

When all canonical apertures are at least two, every shadow facet of the
initial colex segment is at least two-covered.  Complementation therefore
gives

\[
 {\sigma(A)\over2}=|\partial F|-|F|.
\]

The exact colex shadow formula and the binomial ratio

\[
 |\partial F|=\sum_j\binom{c_j}{j-1},
 \qquad
 \binom{c_j}{j-1}={j\over\rho_j}\binom{c_j}j
\]

prove (4.5).  The full-shore term, if present, contributes zero to this
identity.

For run `t`, `|R_t|=m-rho^(t)-1`, so the root-path trace bound is
`N_(rho^(t)+1)`.  Each clause core has residual rank `rho^(t)`, giving the
principal-clause bound `2N_(rho^(t))`.  Consequently the two global loss
bounds are twice the two alternatives on the right of (4.6).  Since its
left side is half the scalar slack, (4.6) implies `lambda<=sigma` with the
factor of two exactly balanced.

## 8. Scope

The theorem correctly excludes aperture-one runs from the two-covered
multi-run formula and does not assert that criterion (4.6) holds for every
localized profile.  What it proves unconditionally is the complete
multi-jump algebra: nested roots, shielding, exact occurrence current,
linear least-active scalar categories, and the stated sufficient
full-colex inequality.  On precisely that scope, the verdict is
**INDEPENDENT GO**.
