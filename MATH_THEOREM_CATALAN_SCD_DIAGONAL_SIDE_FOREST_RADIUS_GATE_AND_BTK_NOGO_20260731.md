# SCD diagonal side forests: the radius gate and the canonical BTK obstruction

Date: 2026-07-31  
Status: exact side-graph reduction, an all-`n` no-go for the canonical BTK
diagonal ansatz, and finite comparison with the positive `n=3,4` collar
fixtures; arbitrary SCDs and the punctured-side theorem remain open

## 0. Verdict

Once the synchronized set `Q` is supplied by
`MATH_THEOREM_CATALAN_TWO_COORDINATE_COMMON_BASIS_AUTOMATIC_20260731.md`,
an SCD diagonal gives a very structured candidate for either punctured
side matching.  Its physical conditions have an exact local form.

For every SCD chain of radius at least two, join the on-chain intermediate
vertex of its central two-step interval to the off-chain corner.  If
`mu(Y)` is the number of off corners equal to `Y`, then

\[
 d(Y)=\mathbf1_{\rho(Y)\ge2}+\mu(Y).                 \tag{0.1}
\]

Thus maximum degree two and the seam-anchor cap are respectively

\[
 \mu(Y)\le2-\mathbf1_{\rho(Y)\ge2},\qquad
 \mu(Y)\le1-\mathbf1_{\rho(Y)\ge2}\quad(Y\text{ an anchor}). \tag{0.2}
\]

Under (0.2), cycles are exactly cycles of the functional chain map which
sends a long chain to the chain containing its off corner.  In particular,
strict decrease of chain radius proves acyclicity.

This separates the issue sharply: radius laminarity handles topology, but
not degree or anchor capacity.  The canonical Greene--Kleitman/BTK SCD is
the minimal counterexample.

* Every canonical off corner lies on a chain of radius exactly one less,
  so both side graphs are acyclic.
* At `n=3`, each side graph has degree histogram
  `0^5 1^8 2^2`.  Only `13` of the `15` side vertices are anchor-safe,
  while `C=Cat_4=14` anchors are forced.  No anchor set can pass.
* For every `n>=4`, the explicit rank-`n+1` vertex

  \[
       v_n=\{0,1,2,4,6,\ldots,2n-2\}                 \tag{0.3}
  \]

  has side degree `n-1>=3`.  Moreover all its incident lower resources
  lie below `v_n` and all incident upper resources lie above `v_n`, so any
  re-pairing confined to that collision star still uses `v_n`.  A local
  laminar uncrossing cannot repair it.

Therefore the canonical BTK diagonal and every coordinate relabelling of
it fail the anchor-capped side-forest gate for every `n>=3`.  This is **not**
a no-go for a noncanonical SCD, a rethreaded diagonal matching, or the
unrestricted two-coordinate recursion.

The frozen positive `n=3,4` side forests are genuinely outside this ansatz:
none of the `90` and `2520` coordinate-permuted canonical BTK middle banks,
respectively, even fit one inherited tail bank after arbitrary child-path
reorientation.  Their positivity is therefore consistent with the
canonical obstruction.

## 1. The punctured side matching

Fix a core ground set of order `2n`.  Write

\[
 \mathcal X=\binom{[2n]}n,\quad
 P=\binom{2n}{n-2},\quad
 C=\binom{2n}n-P=\operatorname{Cat}_{n+1}.           \tag{1.1}
\]

For the upper side, a prescribed \(P\)-set \(D\subseteq\mathcal X\) must be
matched bijectively to all rank-`n+2` resources.  A selected incidence

\[
                         X\subset U,qquad |U-X|=2   \tag{1.2}
\]

lifts to the Johnson edge on the two rank-`n+1` intermediates in the
interval `[X,U]`.  Thus a side matching is exactly a selection of `P`
length-two Boolean intervals with distinct bottoms and tops.  Its physical
graph is their intermediate-edge graph.

The lower side is complementary: match every rank-`n-2` resource to a
prescribed `P`-set of rank `n`, and take the two rank-`n-1` intermediates.
Everything below has a literal lower-side dual.

Given inherited ports from `Q`, the upper-side domain is

\[
 D^-=\mathcal X\setminus\{t_q:q\in Q\},              \tag{1.3}
\]

and its seam anchors are \(B^-=\{U_q:q\in Q\}\).  Incidence feasibility of an
appropriate `Q` is automatic, but neither the physical representative nor
an SCD realizing the particular domain (1.3) is automatic.

## 2. The SCD diagonal

Let `S` be an SCD of the Boolean lattice `B_(2n)`.  If a chain begins at
rank `n-r`, call `r` its radius.  A radius-`r` chain is symmetric and ends
at rank `n+r`.

For every chain `A` of radius at least two, write its central upper segment

\[
                  X_A<Y_A<U_A,qquad
 |X_A|=n, |Y_A|=n+1, |U_A|=n+2,                   \tag{2.1}
\]

and put

\[
                  H_A=X_A\cup(U_A-Y_A).             \tag{2.2}
\]

The SCD upper diagonal selects the diamond `(X_A,U_A)` and physical edge
`Y_A H_A`.  There are exactly `P` radius-at-least-two chains, because each
contains one rank-`n-2` member.  Their `X_A` are distinct, and their `U_A`
enumerate the complete rank-`n+2` layer.  Hence they are a saturating side
matching with domain

\[
 D_S=\{X_A:\rho(A)\ge2\}.                            \tag{2.3}
\]

The lower diagonal uses the central lower segment of the same long chains.

## 3. Exact degree, anchor and cycle criteria

Every rank-`n+1` vertex `Y` belongs to a unique SCD chain, of radius at
least one.  It is an on-chain endpoint of a selected diagonal edge exactly
when its chain has radius at least two.  Define

\[
 \mu(Y)=|\{A:\rho(A)\ge2,\ H_A=Y\}|.                 \tag{3.1}
\]

### Theorem 3.1 (SCD side-forest criterion)

For a fixed SCD diagonal:

1. the physical degree is exactly (0.1);
2. maximum degree at most two is equivalent to the first inequality in
   (0.2);
3. an anchor set `B` respects the one-unit seam cap exactly when the second
   inequality in (0.2) holds for every `Y in B`; and
4. after the degree row holds, the side graph is acyclic exactly when the
   directed map

   \[
        A\longmapsto \text{the SCD chain containing }H_A             \tag{3.2}
   \]

   has no cycle entirely among radius-at-least-two chains.

#### Proof

The on-chain vertices `Y_A` are distinct, since they belong to distinct
SCD chains.  Their contribution to `d(Y)` is therefore the indicator in
(0.1), while every equality `H_A=Y` contributes one further incidence.
This proves the first three statements.

Orient every selected side edge from `Y_A` to `H_A`.  Every vertex has
outdegree at most one and indegree `mu(Y)`.  In an undirected cycle all
vertices have degree two.  Such a component cannot contain a vertex of
outdegree zero and indegree two, because it would then require a vertex of
outdegree two to balance the orientations.  Hence every cycle has one
incoming and one outgoing edge at each vertex and is exactly a directed
cycle of (3.2).  The converse is immediate. \(\square\)

### Corollary 3.2 (radius-laminar acyclicity)

If every selected chain `A` satisfies

\[
       \rho(\text{chain containing }H_A)<\rho(A),     \tag{3.3}
\]

then the SCD side graph is acyclic.

This is the valid laminar theorem.  It proves only the cycle row; (0.2)
must still be checked separately.

## 4. Canonical BTK: perfect radius flow, failed capacity

Use the standard bracket SCD, scanning coordinates from `0` to `2n-1`,
pairing an unmatched zero with a later one.  A radius-`r` chain has
`2r` free coordinates.  At its central member the first `r` free
coordinates are one and the last `r` are zero.  Its next two steps turn
the next two free zeros into ones.

### Lemma 4.1 (exact BTK radius drop)

For every radius-`r>=2` BTK chain, the upper off corner `H_A` belongs to a
BTK chain of radius exactly `r-1`.  The same holds dually on the lower
side.

#### Proof

Let the next two free coordinates be `f_(r+1)<f_(r+2)`.  The off corner
sets `f_(r+2)=1` while leaving `f_(r+1)=0`.  These two coordinates become a
new bracket pair.  All old bracket pairs are unchanged, so precisely two
free coordinates disappear.  The new chain has `2r-2` free coordinates
and radius `r-1`.  Complementation gives the lower statement. \(\square\)

Thus the canonical side graph is always acyclic.  Its degree obstruction
is nevertheless uniform.

### Theorem 4.2 (canonical collision star)

For every `n>=3`, the vertex `v_n` in (0.3) is incident with the following
`n-1` distinct canonical upper-diagonal edges:

* for each even `k in {4,6,...,2n-2}`, the chain with central bottom
  `v_n-{k}` adds `k-1` and then `k`, giving an off-corner incidence at
  `v_n`; and
* the chain with central bottom `v_n-{2}` adds `2` and then `2n-1`, giving
  the unique on-chain incidence at `v_n`.

In particular its degree is at least `n-1`, so the canonical diagonal
violates maximum degree two for every `n>=4`.

#### Proof

Apply the bracket rule directly to the displayed bit pattern.  For
`k>=4` even, deleting `k` leaves `k-1,k` as the next two free zeros, in
that order.  The opposite intermediate restores `k` and is `v_n`.  After
deleting `2`, the next two free zeros are `2,2n-1`, so `v_n` is the
on-chain intermediate.  These `n-1` chains are distinct. \(\square\)

The obstruction is immune to a star-local uncrossing.  Every selected
bottom in this star is a subset of `v_n`, and every selected top contains
`v_n`.  Therefore every cross-pairing of the same bottoms and tops remains
a valid length-two Boolean interval through `v_n`.  At least one resource
must be exported outside the star.

At `n=3`, Theorem 4.2 gives only degree two.  A direct 15-vertex check gives

\[
              d^0=5,\qquad d^1=8,\qquad d^2=2.       \tag{4.1}
\]

The seam requires `C=14` anchors, but only `5+8=13` vertices have side
degree at most one.  Thus the anchor cap fails for every anchor set.  We
have proved:

### Corollary 4.3 (canonical BTK side no-go)

For every `n>=3`, neither the canonical BTK SCD diagonal nor any coordinate
permutation of it is an anchor-capped punctured side forest.

This corollary is about the canonical SCD diagonal only.  It does not
restrict other side matchings.

## 5. Alignment with the inherited `Q`

Even an SCD satisfying Theorem 3.1 must realize the domain imposed by `Q`.
Let

\[
 B_S=\mathcal X-D_S                                      \tag{5.1}
\]

be its short-chain central bank.  Equations (1.3) and (2.3) show that an
upper SCD diagonal using inherited tails requires exactly

\[
                         \{t_q:q\in Q\}=B_S.          \tag{5.2}
\]

There is a dual head equality on the lower side.  Automatic existence of
some common basis `Q` does not imply (5.2) for a prescribed SCD bank.

For a child path forest with freely reversible components, a bank `B_S`
is contained in some tail image if and only if

1. every isolated child vertex lies outside `B_S`; and
2. no nontrivial child path has both endpoints in `B_S`.

Indeed, the missing tail on each nontrivial oriented path is its terminal
endpoint, which may be chosen at either end; an isolated vertex is always
missing.

The exact coordinate-orbit audit applies this criterion to the frozen
positive fixtures.

| child `n` | distinct permuted BTK banks | fixture `D^-` hits | fixture `D^+` hits | banks feasible after any path reversals |
|---:|---:|---:|---:|---:|
| 3 | 90 | 0 | 0 | 0 |
| 4 | 2520 | 0 | 0 | 0 |

Thus those positive side forests do not secretly come from a relabelled
canonical diagonal.  This is an orbit statement, not an enumeration of all
SCDs.

## 6. Consequence for a surviving SCD strategy

The weakest exact SCD target is now explicit.  One must choose, jointly
with the automatic common basis `Q`, one SCD per side (or a more general
diagonal matching) such that:

1. its long-chain central bank is the punctured domain imposed by `Q`;
2. its off-corner load obeys (0.2), including the actual seam anchors;
3. its chain map has no directed cycle, for example by (3.3); and
4. after both side forests and `F-Q` are contracted, the complete seam
   attachment graph is still a forest.

The canonical radius law supplies item 3 but fails items 1--2.  The
degree-three star proves that a theorem based only on laminar chain radii
or a permutation of colliding partners cannot establish item 2.  A viable
construction needs a noncanonical chain bank, a resource-exporting
uncrossing, or a side matching not tied to one SCD.

## 7. Exact audit and scope

The independent standard-library audit is

```text
scratch/audit_catalan_scd_diagonal_side_forest_gate_20260731.py
scratch/catalan_scd_diagonal_side_forest_gate_m2_m8_20260731.audit.json
```

It verifies the canonical BTK upper and lower diagonals through `n=8`,
including every degree, cycle and radius transition.  It also checks every
canonical two-factor product split through `n=6`; these finite products
have the same recorded degree histograms and exact radius drop.  Finally it
exhausts the coordinate-permuted middle-bank orbits for the `n=3,4`
fixtures.

The proof above promotes only the exact fixed-SCD criterion, BTK radius
drop, collision star, and canonical all-`n` no-go.  The product-split rows
and arbitrary-path-bank comparisons are finite audits.  No arbitrary-SCD
obstruction, all-`n` side-forest construction, full two-coordinate collar,
residence, deeper-shadow, compiler, or new `nu(k)=B(k)` result is claimed.
