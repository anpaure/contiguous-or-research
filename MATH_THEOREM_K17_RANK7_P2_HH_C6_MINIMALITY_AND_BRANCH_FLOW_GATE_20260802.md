# K17 rank-seven P2/H crossing: C6 minimality and exact branch--flow gate

**Date:** 2026-08-02  
**Status:** proof-complete structural obstruction and exact conditional
min--max theorem.  The P2-only face is inherited from the canonical root
no-go and is not rerun here.  A concrete three-row C6 is now independently
authenticated with common-phase sockets, the private `1748`-ticket bank, its
outer matching, and the raw-warm47 full supplier matching.  This is one
positive local column, not a packing or global chronology.

## 1. Rebase after the P2-only no-go

The canonical result

```text
MATH_THEOREM_ROOT_K17_P2_ONLY_RETHREAD_CONTAINMENT_NOGO_20260802.md
```

proves that permuting the `3899` P2 bottoms among the fixed P2 roots cannot
repair the frozen common-phase socket zeros.  The present note starts after
that theorem.

For a current P2 row and a current long H row write

\[
                  (S,R)+(B,M,U),                             \tag{1.1}
\]

where `S` is the P2 bottom and `M` is the H middle target.  Every current H
middle in the declared bank has rank seven.

The smallest two-row P2/H bottom swap is

\[
       (S,R)+(B,M,U)\longmapsto(B,R)+(S,M,U).                 \tag{1.2}
\]

It requires

\[
                         B\subsetneq R,\qquad S\subsetneq M. \tag{1.3}
\]

## 2. The two-row P2/H donor graph is still deficient

Let `Z_phi` be the phase-`phi` P2 global-zero set, and let
`Z_U=Z_0 union Z_1`.  The frozen census gives

\[
 |Z_0|=1412,\quad |Z_1|=1413,\quad |Z_U|=1641.              \tag{2.1}
\]

Among these, the rank-seven counts are

\[
 |Z_0^{(7)}|=581,qquad |Z_1^{(7)}|=582,qquad
 |Z_U^{(7)}|=623.                                            \tag{2.2}
\]

Build the structural bottom-swap graph whose left shore is a declared zero
P2 row and whose right shore is a common currently-long H row, with an edge
when (1.3) holds.

### Theorem 2.1 (rank-seven bottom-swap isolation)

Every rank-seven left vertex is isolated.  Consequently the phase-specific
and common-phase bottom-swap deficiencies satisfy

\[
                  \delta_0\ge581,qquad
                  \delta_1\ge582,qquad
                  \delta_{01}\ge623.                        \tag{2.3}
\]

For the common-phase graph on all `1641` union-zero roles,

\[
                         \nu\le1641-623=1018.                 \tag{2.4}
\]

#### Proof

Both `S` and every H middle `M` have rank seven.  The strict containment
`S subsetneq M` in (1.3) is therefore impossible.  These vertices have no
structural edge, before any socket, state, supplier, or protected-bank test.
Hall's theorem gives (2.3)--(2.4). \(\square\)

The local audit row is frozen at

```text
scratch/k17_immutable_p2_role_kernel_20260802/
  rank7_p2_h_donor_cut.audit.tsv
```

It records `PASS_K17_RANK7_P2_H_DONOR_CUT`, the four rank histograms, and
the smallest common witness `9515,46864,46865`.

Thus the two-row prefix swap (1.2) can help lower-rank labels but cannot be
the rank-seven escape promised by the P2-only theorem.

## 3. Why a C6 is the first rank-seven crossing

Let `J` be the bipartite incidence graph between rank-seven targets and
rank-eight roots, with an edge for strict containment.

### Lemma 3.1 (no C4)

The graph `J` contains no four-cycle.

#### Proof

If two distinct rank-seven sets `A,B` lie below one rank-eight set, then
`|A union B|=8` and that rank-eight set is uniquely `A union B`.  Hence the
same two rank-seven sets cannot have two distinct common rank-eight
supersets.  That is exactly the exclusion of a C4. \(\square\)

### Corollary 3.2 (support-minimal crossing)

A nontrivial root-preserving reassignment of rank-seven targets cannot be a
two-row transposition.  Its incidence support has length at least six.
One support-six mixed architecture uses one P2 role and two H roles:

\[
\begin{split}
 &(S_0,R_0)+(B_1,S_1,R_1)+(B_2,S_2,R_2)\\
 &\qquad\longmapsto
 (S_1,R_0)+(B_1,S_2,R_1)+(B_2,S_0,R_2).             \tag{3.1}
\end{split}
\]

Its exact containment rows are

\[
 S_1\subsetneq R_0,\quad S_2\subsetneq R_1,\quad
 S_0\subsetneq R_2,\quad B_1\subsetneq S_2,\quad
 B_2\subsetneq S_0.                                  \tag{3.2}
\]

When (3.2) holds, (3.1) preserves every target exactly once, every root and
owner, and the row-length histogram.  It moves the old P2 rank-seven target
`S_0` into an H middle position and replaces it by `S_1`.  Lemma 3.1 proves
only the support-six lower bound.  It neither proves that a relevant C6
exists nor excludes another type distribution, such as two P2 roles and one
H role.

## 4. Authenticated support-six column

The root-authenticated column uses rows `(P2,H1,H2)=(16269,16267,16271)`:

```text
old  81416-81417 ; 73216-81409-81413 ; 81408-81412-81420
new  81409-81417 ; 73216-81412-81413 ; 81408-81416-81420
```

The new P2 role has the exact common-phase census

```text
phase 0: 3899 hyperarcs, witness (q,a,b)=(8,2,2)
phase 1: 3584 hyperarcs, witness (q,a,b)=(7,0,0)
```

The producer and independent outputs are

```text
scratch/k17_fixed_p2_role_moving_escape_20260802/
  rank7_p2_hh_suffix_c6.producer.audit.txt
  rank7_p2_hh_suffix_c6.independent.audit.txt
```

They replay exact target/root/owner/histogram preservation, literal
five-cell witnesses in both phases, all `1748` protected tickets, and the
complete outer matching (`16898` H plus `1748` F receivers).  The separate
supplier/private audit

```text
scratch/k17_immutable_p2_role_kernel_20260802/
  rank7_suffix_c6_supplier_private.audit.tsv
```

retains the raw-warm47 matching at `16898/16898` and all protected tickets.
Thus the support-six lower bound is sharp on this declared local face.

The canonical finite theorem and H100 bindings are in

```text
MATH_THEOREM_K17_IMMUTABLE_P2_ROLE_MOVING_PREFIX_AND_SUFFIX_CIRCUITS_20260802.md
```

This positive column still does not certify simultaneous state cover,
chronological serialization, residence, upper/source closure, the compiler,
or a word.

## 5. Exact C6 packing as branch--flow

Let `K` be the `623` rank-seven union-zero P2 roles and `H` the admissible
currently-long H roles after excluding every protected private endpoint
host (or, more generally, after attaching a literal replay condition to any
protected host retained).  Let `widehat C` be the complete set of
occurrence-labelled C6 columns, with maps `i(c),h_1(c),h_2(c)`.  Its row
shadow is

\[
 \mathcal C=\bigl\{(i(c),h_1(c),h_2(c)):
                    c\in\widehat{\mathcal C}\bigr\}
       \subseteq K\times H\times H.                          \tag{5.1}
\]

Every underlying column satisfies:

1. the five containments (3.2);
2. distinct physical rows and preservation of the exact target deck;
3. an exact common-phase five-cell socket for the new P2 row;
4. literal legality of both rebuilt H long modes; and
5. every declared protected endpoint/token exclusion.

Parallel occurrence columns with the same row triple remain distinct in
`widehat C`; (5.1) forgets them only for the row-disjoint flow below.

### Exact catalogue construction

The structural enumeration need not scan any H-row pairs.  In fact it has
at most seven row-shadow candidates per rank-seven P2 role.

### Lemma 5.0 (one deleted element determines the C6)

Fix `i in K` with current edge `S_0 subset R_0`, and write

\[
                         R_0=S_0\mathbin{\dot\cup}\{b\}.
\]

Every alternating rank-seven/rank-eight C6 through this edge is uniquely
determined by an element `a in S_0`.  Put

\[
 C=S_0-\{a\},\qquad S_1=C+\{b\}.
\]

The exact target partition gives at most one current row with middle `S_1`;
require that it be an H row `h_1`, and write

\[
 R_1=S_1+\{c\}.
\]

Then necessarily

\[
 S_2=C+\{c\},\qquad R_2=C+\{a,c\}.                 \tag{5.0}
\]

Consequently `h_2`, if it exists, is the unique current H row with middle
`S_2` and root `R_2`.

#### Proof

The second rank-seven neighbor of `R_0` must be `R_0-\{a\}` for a unique
`a in S_0`, giving `S_1`.  Exact target use makes its physical row unique.
The roots `R_0,R_1` are distinct, so `a,b,c` are distinct outside `C`.
Any second rank-seven neighbor of `R_1=C+\{b,c\}` is obtained by deleting
one element.  Deleting `c` returns `S_1`.  Deleting `x in C` gives a set
whose union with `S_0=C+\{a\}` has rank nine.  Only deleting `b` gives
`S_2=C+\{c\}`, whose union with `S_0` has rank eight.  A rank-eight root
containing both must therefore be their union `C+\{a,c\}`.  Exact target use
again makes the row unique. \(\square\)

Thus for each `i in K` the exact structural loop is:

1. enumerate the seven choices `a in S_0` and form the forced labels in
   (5.0);
2. look up the two unique physical H rows and require their recorded roots
   to equal `R_1,R_2`;
3. test the two lower containments in (3.2), physical-row distinctness, and
   the protected-host/token exclusions;
4. materialize both rebuilt H modes and run the exact common-phase
   five-cell oracle for the new P2 role, excluding endpoint modes destroyed
   by either changed H row; and
5. retain every occurrence witness and its complete endpoint/token/history
   footprint under one column ID.

The rank-seven/rank-eight containment index has bounded local degree, so the
structural part is output-sensitive in the number of C6 candidates.  The
five-cell test may be streamed on demand and memoized by the fully labelled
new P2 role and forbidden-mode set.  Boolean existence alone is insufficient
for the later common-state packing.

### Exact fixed-table row-shadow census

A separate literal enumerator applied Lemma 5.0 to all `623` rank-seven
union-zero P2 roles.  Before any five-cell socket test it found

| filter | columns | covered P2 roles |
|---|---:|---:|
| forced rank-incidence closure | 364 | 290 |
| both rebuilt H bottoms remain legal | 180 | 168 |
| additionally avoid every protected H short and all `3496` protected endpoint hosts | 118 | 116 |

No role has more than three structural columns.  The authenticated column
on row `16269` appears in this final set.  The audit files and SHA-256 values
are

```text
scratch/audit_k17_rank7_c6_structural_unique_closure_20260802.cpp
  7da1f9ab6e6b0013eac30fde0370bcb36361ed9b95effe2faadcc199209dd979
scratch/k17_rank7_p2_hh_c6_audit_20260802/structural_candidates.tsv
  cb93bfc7b785eff4e9d6d01bc6ec6f46e3e2025879b3b1abeff85ba9757fefe0
scratch/k17_rank7_p2_hh_c6_audit_20260802/structural.audit.json
  77d3ada0ea96b95044830c216d62e4826a16c027212563773cf048975d608e48
```

Therefore a single row-disjoint packing of P2--H--H C6 columns from this
**fixed table and protected bank** cannot cover all `623` roles: already
`507` roles have no protected row-clean structural column.  This is not a
serial-C6 no-go.  One accepted C6 changes two H middles and hence the next
catalogue; richer P2/P2/H architectures or other support sizes are also
outside this census.

Selecting disjoint C6 columns is a three-way hypermatching problem.  It is
not, in general, a second matroid or an ordinary bipartite matching.

Fix an injective first-H assignment

\[
                         \mu:K\hookrightarrow H.              \tag{5.2}
\]

Build the bipartite graph `Gamma_mu` with left shore `K`, right shore
`H minus mu(K)`, and edge `i h` exactly when

\[
                         (i,\mu(i),h)\in\mathcal C.            \tag{5.3}
\]

### Theorem 5.1 (one-H branch, one-flow completion)

The branch `mu` extends to pairwise row-disjoint C6 columns covering all of
`K` if and only if `Gamma_mu` has a matching saturating `K`.  Equivalently,

\[
                     |N_{\Gamma_\mu}(X)|\ge |X|
                     \qquad(X\subseteq K).                    \tag{5.4}
\]

The exact branch deficiency is

\[
 |K|-\nu(\Gamma_\mu)
   =\max_{X\subseteq K}\bigl(|X|-|N_{\Gamma_\mu}(X)|\bigr), \tag{5.5}
\]

and one maximum flow/minimum cut returns either a completion or a
maximum-deficiency Hall shore.

#### Proof

Injectivity of `mu` fixes distinct first H rows.  Deleting `mu(K)` from the
right shore forbids a second H row from colliding with any first H row.
A matching saturating `K` chooses distinct second H rows, and (5.3) makes
each resulting triple a legal C6 column.  Conversely every disjoint C6
packing with first coordinate `mu` projects to such a matching.  Hall's
theorem gives (5.4)--(5.5). \(\square\)

A deficient shore certifies failure of the fixed branch `mu`.  The always
safe Benders no-good is therefore

\[
                  \sum_{i\in K} y_{i,\mu(i)}\le |K|-1.       \tag{5.6}
\]

Here `y_(i,h)` is the first-H branch variable.  Retaining only the first-H
choices on the deficient shore `X` is not generally enough: changing a
first-H choice outside `X` can free a physical H role which becomes a new
second-H neighbor of `X`.

There is nevertheless an exact localized cut.  For the incumbent branch
\(\bar\mu\), put

\[
 A_X=\bigcup_{i\in X}
       \{h:(i,\bar\mu(i),h)\in\mathcal C\},
 \qquad o_h=\sum_{j\in K}y_{j,h}.                         \tag{5.7}
\]

Every integral C6 packing satisfies

\[
 \sum_{h\in A_X}(1-o_h)
 +|X|\sum_{i\in X}(1-y_{i,\bar\mu(i)})
 \ge |X|.                                                   \tag{5.8}
\]

If all first-H choices on `X` remain fixed, their second H rows must be
`|X|` distinct unoccupied members of `A_X`.  If any such first choice
changes, the second term safely disables the row.  At the incumbent, the
first term equals
\( |N_{\Gamma_{\bar\mu}}(X)|<|X| \), so (5.8) separates it.
If \(\mathcal C\) was filtered by assumed history, phase, outer-placement, or
protected-resource literals, (5.8) and (5.6) must be guarded by those
assumptions or by an independently verified smaller core.

Arbitrary three-dimensional matching is a special case of (5.1).  Thus
there is no general Edmonds two-matroid min--max that eliminates the first-H
branch.  A private, laminar, or functional C6 atlas could create a Rado face,
but no such rank theorem is presently authenticated.

Theorem 5.1 is exact for disjoint **row geometry**.  Row-disjoint columns can
still share socket endpoint hosts/tokens, or a socket endpoint of one column
can be an H row rebuilt by another column.  Full occurrence compatibility
therefore requires each column's labelled footprint plus cross-column
branching, or a privacy/functional theorem which makes row-disjointness
sufficient.

## 6. The downstream inner lifting rows

The C6 flow is only the geometric rethread selector.  A promoted endpoint
must still use the same occurrence-labelled choices in all of the following
rows.

1. Rebuild every changed H state and the new P2 five-cell ticket in both
   required phases.
2. Preserve or replay the protected `1748`-ticket bank and its forced outer
   placements.
3. Rebuild the hard supplier graph and require rank `16898`; a deficient
   supplier shore is a separate exact Hall/Benders cut.
4. Choose one shared state per physical long role and complete the residual
   long--long arcs by the state-expanded Hall/min-cut oracle.
5. Replay reset balance, the component profile, and any required physical
   serialization of the simultaneous C6 columns.

Separate positive matchings for C6 geometry, suppliers, and residual direct
arcs are insufficient if they use incompatible ticket occurrences.  Exact
activation must retain the common column/ticket variables, or the inner
flows must be conditioned on the full materialized choice.

## 7. What is newly resolved

The P2/H rebase now has a sharp trichotomy:

- P2-only permutation is already canonically closed;
- two-row P2/H bottom swaps cannot touch any of the `623` rank-seven
  union-zero roles;
- support six is sharp: the authenticated P2--H--H column realizes it, and
  after fixing the first H coordinate of a proposed packing the rest has an
  exact Hall min--max and one-flow oracle.

What remains is the complete protected occurrence-labelled C6 catalogue,
row-disjoint packing for the `623` rank-seven roles, and then a common
supplier-rank replay and the state/protected-bank/chronology gates in
Section 6.  The single authenticated column proves nonemptiness, not the
required packing rank.
