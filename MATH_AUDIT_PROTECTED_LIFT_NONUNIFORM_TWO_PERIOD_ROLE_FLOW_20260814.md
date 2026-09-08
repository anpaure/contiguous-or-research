# Audit: protected-lift nonuniform two-period role flow

**Date:** 2026-08-14  
**Verdict:** **PASS.**  The slot-clone decomposition, two-period residue
repair, support/core capacity inequalities, balanced padding argument, and
named-order dual are correct under the theorem's explicit hypotheses.  The
result proves exact ground-point roles only; it does not prove named-order
feasibility or rounding.

**Frozen theorem:**
`MATH_THEOREM_PROTECTED_LIFT_NONUNIFORM_TWO_PERIOD_ROLE_FLOW_AND_NAMED_ORDER_DUAL_GATE_20260814.md`  
**Theorem SHA-256 (H100):**
`1caecb5d9885f8bad88258f9fc1f1df5eee79294a1a0187d0009e95a81a46bb8`

**Verifier:** `verify_protected_lift_nonuniform_two_period_role_flow.py`  
**Verifier SHA-256 (H100):**
`67d7102b2aa1731a570244e300b2bae85dcc933dd0a65987c76cd8b846da3304`

**Frozen H100 output SHA-256:**
`94fa8825e74217f2037a04d059d1d4cb4d7ac32d5061039568acc75cf2c16f12`

## 1. Slot-clone integrality

For equal-period shell tokens, the necessary degree conditions are

\[
 \sum_x\alpha_x=ct,qquad
 \sum_x\beta_x=Nt,qquad
 \alpha_x+\beta_x\le t.
\]

The proof realizes the core and support demands as parallel edges from
`c+N` labelled slots to coordinate vertices, each slot having degree `t`.
Coordinate degree is at most `t`.  Adding dummy slots and edges makes a
balanced `t`-regular bipartite multigraph.  Its `t` perfect matchings each
use distinct coordinates and separate genuine core slots from genuine
support slots.  This is exactly a collection of legal shell pairs with the
prescribed integer degrees.  Parallel edges cause no collision inside one
matching.

Thus no total-unimodularity or unproved hypergraph decomposition is hidden
in the role construction.

## 2. Direction margin and large-support coordinates

With `n=2q+2`, the hypothesis

\[
                         h_i\le2^p/(q+4)
\]

gives every physical support defect

\[
                         u_x=h_i/2\le e/(n+6).
\]

If fewer than `n+2` coordinates had `u_x>=b`, their total support defect
would be strictly below

\[
                         (n+1)e/(n+6)+mb<e,
\]

contradicting `sum u_x=e`.  Hence the heavy supports can be confined to an
`(n+2)`-set `Q` with per-coordinate capacity at least `b`.

The repeated-direction separation `q+4` is used only to imply the displayed
direction-count bound.  The theorem does not assert that a Gray code with
that margin exists outside the separately stated long-run range.

## 3. Heavy-core residues

For `rho_x=r_x mod n`, choosing `b congruent e mod n` makes

\[
                         cb-\sum_x\rho_x
\]

divisible by `n`.  The lower bound on `b` makes it nonnegative.  Keeping
the `n+2` coordinates of `Q` at their small residues leaves
`g=m-(n+2)` coordinates on which to add multiples of `n`.  Their aggregate
increment capacity is at least

\[
                         g(b-2n)/n\ge cb/n,
\]

which dominates the required increment count.  This proves the exact
heavy-core sum `cb` while preserving `0<=v_x<=b` and small `v_x` on `Q`.

The light-core degrees

\[
                         ell_x=(r_x-(n+1)v_x)/n
\]

are integral.  Their sum is `ca`.  Nonnegativity follows from

\[
 r_x\ge e/2-(q-1)e/(n+6)=5e/(n+6)
                         \ge(n+1)b,
\]

and `ell_x<=a` follows from `r_x<=e/2` together with
`(n+1)b<=e/(n+6)`.

## 4. Heavy and light support capacities

On `Q`, the heavy support capacity is at least

\[
 (n+2)(b-n+1)\ge(n+1)b,
\]

so the heavy degrees `s_x` can be selected with
`v_x+s_x<=b` and `s_x<=u_x`.  The remaining light degrees
`w_x=u_x-s_x` are nonnegative and sum to `na`.

The key light capacity identity was replayed algebraically:

\[
 \begin{aligned}
 n(a-ell_x-w_x)
 &=e/2-(q+3)u_x-(n+1)(b-v_x)+ns_x\\
 &\ge e/(n+6)-(n+1)b\ge0.
 \end{aligned}
\]

Therefore both equal-period classes meet all hypotheses of the slot-clone
lemma.  Their weighted core degrees combine as

\[
                         n ell_x+(n+1)v_x=r_x,
\]

and their support degrees combine as `w_x+s_x=u_x`.

## 5. Balanced full-bank padding

The proof chooses macroscopic counts `A,B=Theta(W/q)` with
`nA+(n+1)B=W`.  The balanced residue lemma supplies heavy-core degrees
`V_x=cB/k+O(n)` in the required congruence class, making

\[
                         L_x=(cK-(n+1)V_x)/n
                            =cA/k+O(n)
\]

integral.  Balanced heavy supports `S_x` and `Q_x=K-S_x` have the analogous
degrees.  Since all defect degrees are `O(2^p)` while
`2^p=o(W/k)`, the full degrees dominate the defect degrees coordinatewise.

The strict ambient margins

\[
 k-c-(n+1)=p-q-3>0,qquad k-c-n=p-q-2>0
\]

make the full core-plus-support degree strictly smaller than the token count
by a positive linear fraction.  This dominates the submiddle defect and
gives the residual slot-clone capacities after subtraction.  Adding the
defect and padding shells yields a uniform exact role bank; deleting the
defect bank leaves precisely the protected residual targets.

This padding argument is asymptotic.  No explicit finite threshold is
claimed.

## 6. Named-order characterization

For fixed shells, the sum of the convex hulls of their safe order-incidence
vectors is the exact fractional attainable-load polytope.  The theorem's
inequality against every pair of real owner/lower weights is its support-
function membership criterion, hence is necessary and sufficient by finite-
dimensional separation.

Binary order variables are still required for the integral factor.  The
fractional dual is not a rounding theorem.  Even fractional feasibility is
not proved for the constructed nonuniform shells.  Individual rails are
owner/lower simple and internally biresident, but global upper support,
seam collars, and component fusion remain separate.

## 7. H100 verifier replay

All compilation, execution, and hashing were performed via `ssh h100`.
The verifier returned `PASS` on a synthetic `(p,q)=(15,2)` direction vector
satisfying the theorem's margin.  It materialized the defect bank using
bipartite perfect-matching decomposition:

\[
                         5410\text{ period-6 shells},qquad
                         44\text{ period-7 shells}.
\]

Their total period is `32768`, support defect is `32768`, and weighted-core
defect is `458752=14*32768`.  The frozen shell digest is

`11aa174ba3f28117369d6aff76e38ff1de89e29915f87b58297c29f97f60a48d`.

The replay also checked positive residual padding margins in a complete
period-6/7 bank.  The synthetic direction counts are not claimed to arise
from a named Gray cycle; their role is to test the theorem's deterministic
degree construction once its explicit numerical hypotheses are supplied.

## 8. Scope

The theorem closes the nonuniform core/support Hall gate under the stated
direction margin and proves that the required macroscopic cross-cell bank
is compatible with exact protected point roles.  It does not close:

* safe fractional named-order feasibility;
* integral owner/lower ordering;
* immediate-upper support;
* source-letter chronology; or
* component joining.

