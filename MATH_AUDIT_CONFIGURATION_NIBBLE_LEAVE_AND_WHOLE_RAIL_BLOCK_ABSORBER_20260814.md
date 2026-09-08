# Hostile audit of the configuration leave and whole-rail block absorber reduction

**Date:** 2026-08-14  
**Audited source:**
`MATH_REDUCTION_CONFIGURATION_NIBBLE_LEAVE_SEMIGROUP_AND_WHOLE_RAIL_BLOCK_ABSORBER_20260814.md`  
**Verdict:** **PASS after narrowing the nibble scope.**  The finite
semigroup interface, alternating-incidence cut theorem, point-role and
parity shape, disjoint whole-fibre block absorber, augmented exact-cover
equivalence, and `q=2` coupled-boundary obstruction are exact.  The note
does not claim a near-perfect growing-rank matching theorem.

## 1. Finite completion and the exact cut condition

For a fixed finite legal catalogue, exact completion is tautologically but
usefully the truncated semigroup

\[
 \{Ax:x\in\mathbb Z^\Gamma,\ 0\le x\le m\}.         \tag{1.1}
\]

The real box image is a zonotope.  Its two support values at a row weight
`y` are

\[
 \sum_\gamma m_\gamma\min(0,y\cdot a_\gamma),
 \qquad
 \sum_\gamma m_\gamma\max(0,y\cdot a_\gamma),       \tag{1.2}
\]

so the displayed all-weight inequalities are necessary and sufficient for
fractional membership.  Integer lattice membership and these inequalities
need not imply semigroup membership; scalar legal-period columns `6,7` and
demand one already witness the hole.

Before imposing the pure-rail common-core/window structure, the named
owner/lower containment graph has a spanning simple `2`-factor exactly when

\[
 e(X,L_0\setminus Y)+2|Y|\ge2|X|                   \tag{1.3}
\]

for all owner subsets `X` and lower subsets `Y`.  The max-flow construction
has source-owner and lower-sink capacity two and containment-edge capacity
one; the cut capacity is exactly

\[
 2(|O_0|-|X|)+e(X,L_0\setminus Y)+2|Y|.             \tag{1.4}
\]

Since the shores have equal size, a full flow saturates every owner and
lower capacity.  Integrality gives a simple bipartite `2`-factor.  Its
alternating owner projection is a Johnson cycle factor with distinct lower
colours.  This proves a necessary incidence cut theorem, not pure-rail
sufficiency.

The H100 verifier exhausts all `2^(n^2)` bipartite graphs for `n=1,2,3` and
finds exact agreement between `(1.3)` and brute-force `2`-factor existence.

## 2. Exact role and parity shape

For each period-`N` shell `(C,T)`, the owner and lower point vectors are

\[
 N\mathbf1_C+q\mathbf1_T,
 \qquad
 N\mathbf1_C+(q-1)\mathbf1_T.                      \tag{2.1}
\]

Thus `U=o-ell=1_T` and `K=q ell-(q-1)o=N 1_C` per
rail.  A token-partite leave is therefore exactly the sum of the fixed
roles of its unmatched tokens.  It cannot acquire an unexplained point
defect, although it can have a fatal named-resource defect within those
point totals.

Every closed owner cycle has zero fixed-pair `alpha` boundary.  Since
`eta(e)=1+sum alpha_i(e)`, its charge is its period modulo two.  Hence the
leave charge is also fixed by its unmatched token periods.  A conformal
trade cannot alter it independently.

## 3. Nibble statement and the repaired quotient scope

For an honest `r`-uniform `D`-regular hypergraph, Bonferroni gives

\[
 r(D-1)-{r\choose2}(\Delta _2-1)
 \le|\Gamma(E)|\le r(D-1).                          \tag{3.1}
\]

Independent marking at probability `gamma/(rD)` and retaining isolated
edges therefore covers in expectation

\[
 {\gamma e^{-\gamma}\over r}
 \left(1+O\left(D^{-1}+{r\Delta _2\over D}\right)\right).        \tag{3.2}
\]

Writing `theta=r^2 Delta_2/D`, the collision correction is
`O(theta/r)`.  This is a rigorous one-bite theorem, but covers only
`Theta(1/r)`.

The first draft incorrectly treated the alternating configuration quotient
as an ordinary hypergraph.  The final note repairs this.  On the actual
owner/lower hypergraph, the incident owner-facet codegree gives squared-rank
parameter `Theta(N^2/R)=Theta(1)` centrally.  Contracting the two facets
inside each owner restores an external collision ledger `O(k^(-1))`, but
constituent lower collisions remain real even when complete triples differ.
A configuration/conflict matching theorem is needed before the abstract
one-bite lemma applies at that quotient scale.  No iteration or regenerated
degree trajectory is claimed.

## 4. Exact whole-fibre interface

For pairwise resource-disjoint complementary-fibre gadgets, let `b_i` be
the complete occurrence-labelled residual block.  Their incidence matrix
has at most one `1` in each row.  Therefore it is totally unimodular, and a
leave is absorbable exactly when it is

\[
                         \sum_{i\in I}b_i.           \tag{4.1}
\]

Equivalently every row inside a block has the same zero-one leave value.
The choice of `I` is unique.  The identity is unconditional on owner and
proper interval rows; any additional ticket is explicitly assumed to be
decorated compatibly and disjointly.

Installing every `G_i` shore turns structured cover-down into the single
augmented equation

\[
 A_{\rm bulk}x+\sum_{i\in I}b_i=t-\sum_i g_i.       \tag{4.2}
\]

For selected `i`, replacing `G_i+B_i` by `S_i` changes `g_i+b_i` to the
equal physical vector `s_i`.  This proves both directions of the exact-cover
equivalence.  It also explains why an ordinary arbitrary leave is the wrong
target.

For any two rows `x,y` in one block, `e_x-e_y` annihilates every disjoint
whole-block column.  A partial block is therefore outside even their signed
lattice.  A stronger absorber must have a column nonconstant on an old
block: it must refactor inside a fibre or couple fibres.  Adding another
disjoint whole-fibre switch cannot help.

At the scalar level, an interval of `r_0` consecutive admissible terminal
periods represents every residue modulo a bulk period `r_0`.  This permits
one terminal fibre when ambient room and nonnegative mass permit.  It does
not select the named fibre leave or make its polynomial reserve physically
constant-size.

## 5. Exact `q=2` lower debt

Reconstructing the two published eight-rail near-core banks gives owner
current exactly `e_012`.  Their lower shores are not matchings:

* positive: `50` occurrences, `34` named values, maximum multiplicity `3`;
* negative: `49` occurrences, `35` named values, maximum multiplicity `2`.

After cancellation, the lower current has mass one, support nineteen, and
`l1` norm nineteen.  Its point current and the signed support/core degrees
satisfy the exact role identities.  Therefore the certificate is a valid
simple owner absorber but not an alternating owner/lower absorber.

For a fixed relabelled macro `M_H=(e_H,lambda_H)` over each owner, signed
macro combinations span only the graph `(u,Lambda u)`.  Correcting one
owner against a prescribed lower unit leaves `e_L-lambda_H`, whose minimum
`l1` norm is eighteen.  Any repair needs an owner-zero atom carrying the
opposite lower current.  The audit does not claim that no richer catalogue
contains such an atom.

## 6. H100 verification and scope

All executable checks and hashes were run via SSH on H100.  The interface
verifier checked:

* `2`, `16`, and `512` bipartite graphs at shore sizes `1`, `2`, and `3`;
* all `512` zero-one leaves of a three-block, nine-row toy interface;
* `8,505` terminal-period residues through `q=64`;
* the point-role reconstruction; and
* the complete `q=2` alternating lower current.

The frozen H100 digests are:

| artifact | SHA-256 |
|---|---|
| reduction theorem | `234e22559220ac5de9b19b59e5d2791671c4d15763d4ab8f73cb1830c435e1b9` |
| q=2 verifier | `473ab83f3b43430c6f91bec29d3a69d467929968b55def1628a66091e4ebe73a` |
| q=2 verifier output | `cb29f51ea68a0ee5c40a464cf1fbe2710e77b1ae65b439b213bd05fd5c1e84bb` |
| interface verifier | `de9f3554acbbee1ae461bbb944e5f005cb552a5162babdb6af94ed469a89ce28` |
| interface output | `f5bf728c0644b5f7dd78c736e8b23cffbf2eafb28d5cb9253996cf4a1805e01a` |

The proved result is an exact reduction and structured absorber interface.
The global named-spread reserve-aware matching, an honest growing-rank
configuration theorem, simplicity against all external banks, and
chronology remain open.
