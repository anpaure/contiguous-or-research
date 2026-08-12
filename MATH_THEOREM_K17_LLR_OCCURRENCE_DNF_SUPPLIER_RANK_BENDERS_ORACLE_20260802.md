# K17 LLR occurrence-DNF selector and the exact supplier-rank Benders oracle

**Date:** 2026-08-02  
**Status:** proof-complete finite formulation and exact cut separation theorem.
The `4,803/470/1,012` LLR transfer census and its materialized table are bound
only at their warm47 structural/common-positive scope.  They fail the literal
common-parent preflight against the protected `b268...` materialization;
row-ID disjointness alone does not put them in one table.  No selected-state
factor, chronology, residence, upper, compiler, or word claim is made.

## 0. Exact input and verdict

Let the authenticated protected phase contain

* `1,748` fixed H-short rows with one selected occurrence ticket each;
* `3,496` pairwise distinct directed endpoint hosts;
* `3,495` fixed movable token placements and one fixed soft endpoint; and
* a residual square bottom-placement matching on `15,151` real tokens and
  `15,151` receiver slots.

After contracting this bank there are exactly

\[
        3,899+1,748=5,647                                      \tag{0.1}
\]

unprotected short roles and `16,915` long roles.  Choosing all short
tickets consumes `7,395` predecessor and `7,395` successor ports, leaving
exactly

\[
                     16,915-7,395=9,520                         \tag{0.2}
\]

long--long transitions.

The corrected full-private LLR transfer census currently reports

```text
common-positive transfer edges                         4,803
maximum common-only transfer matching                    470
maximum protected-structural transfer matching       1,012/1,018
```

and a warm47-based materialized `470` table is being repriced.  Here
`full-private` means the declared row-disjoint/protected-resource screen on
the transfer columns.  It does not mean that the warm47 table contains the
literal protected tickets and token placements of the independently
materialized `b268...` table.  These numbers supersede the older
`private496` calibration, but they do not imply a common static
materialization, a simultaneous occurrence-state selection, or a
supplier-perfect completion.

The exact remaining finite problem is not one TU flow.  It is, however, an
exact branch--Benders problem with four polynomial matching separators and
one explicit occurrence-hypermatching master.  Most importantly, the LLR
transfer choice can be optimized against the **exact selected-parent
supplier rank**, rather than against a marginal supplier score.

### Theorem 0.1 (literal common-parent contract)

Let `Pi` be the finite set of prospective parent materializations and let
`b_p` select exactly one `p in Pi`.  A branch is semantically admissible only
when all of the following objects are literal descendants of that same `p`:

1. the complete labelled table and both transported owner phases;
2. every fixed private-ticket incidence value, host/token placement, flag,
   and outer/common-basis presentation edge;
3. every LLR transfer column and its edge-labelled `MR`/`LLR` modes; and
4. every supplier-head occurrence and compatibility record used by a Hall
   or rank cut.

Equivalently, every selected object `v` carries one parent guard

\[
                         v\le b_{p(v)},\qquad
                         \sum_{p\in\Pi}b_p=1,             \tag{0.3}
\]

and every AND/OR activation in Sections 2--5 contains that same parent
literal.  A matching shore separated on parent `p` is installed as the
implication

\[
                  b_p=1\quad\Longrightarrow\quad
                  \text{Hall/rank cut on the exact `p` activations}.       \tag{0.4}
\]

Together with exact one-hot state selection and bidirectional within-parent
AND/OR activations, this common-parent contract is fail-closed sufficient for
the Benders cuts to be valid across parent branches.  It is also necessary
unless an explicit incidence-preserving common-materialization/equivalence
theorem transports every listed object.  It is a semantic precondition, not
a feasibility certificate: after it holds, the structural, occurrence,
long-state, and supplier oracles must still pass.

#### Proof

Under (0.3), every active incidence is a literal fact about one table, so its
exact signed-parent AND and neighborhood OR have the meaning used in Hall's
theorem.  Therefore (0.4) is valid on its branch.  Conversely, if a ticket,
transfer mode, table row, or supplier record comes from a different parent,
the purported edge need not exist in any single materialization.  Its
neighborhood OR can then count a stale edge, and the resulting Hall cut is
neither a valid cut for the first parent nor for the second.  Hence no mixed-
parent Benders row is proof-safe.  \(\square\)

For the current data this gate rejects before supplier optimization.  The
warm47-derived 470 table differs from the authenticated `b268...` private
parent on `16,034` rows; `6,479` of the `7,213` protected row IDs and `7,437`
protected occurrences have different literal values.  Thus the `7,213`-row
screen proves only warm47 row-footprint avoidance.  It does **not** prove
survival of the `b268...` tickets or placements.

## 1. The declared LLR transfer grammar

Start with one labelled compressed-normal table `T` and let `D` be its `LMR`
rows and `J` its direct `LR` rows.  An admissible transfer column

\[
                 e=(d,j),\qquad d=(\ell,m,r),\quad j=(u,q),       \tag{1.1}
\]

satisfies `ell subset u` and replaces

\[
       (\ell,m,r)+(u,q)\longmapsto(m,r)+(\ell,u,q).               \tag{1.2}
\]

Let `z_e` select columns.  The exact row-disjointness constraints are

\[
 \sum_{e\ni d}z_e\le1\quad(d\in D),\qquad
 \sum_{e\ni j}z_e\le1\quad(j\in J).                              \tag{1.3}
\]

Every selected column preserves the five named targets, the two roots and
owners, and the multiset of row lengths.  If the compressed table itself is
prospective, `z_e` additionally implies the three representing matching
edges which define (1.1).  Every protected ticket and token occurrence
implies its representation edges in that **same** table `T`.  Completion of
all unpinned representation edges is then tested by the augmented
common-basis matching oracle of Section 5.  A warm47 transfer column and a
`b268...` protected ticket cannot be combined merely because their row IDs
are disjoint: their pinned presentation edges must coexist in one residual
matching.

For a baseline short row `j`, a donor row `d`, and every untouched short
row `w`, their final short indicators are

\[
 a_j=1-\sum_{e\ni j}z_e,\qquad
 a_d=\sum_{e\ni d}z_e,\qquad a_w=1.                              \tag{1.4}
\]

Thus every transfer deactivates one old `LR` short and activates one new
`MR` short.  The number of unprotected shorts stays `5,647`.  The LLR row
created at `j` is a long row whose state catalogue is indexed by the whole
column `e`, not merely by its root `q`.

Equations (1.3)--(1.4) are exact only for this declared two-row transfer
grammar.  They are not a parametrization of every possible `LLR` table.

## 2. Literal occurrence master

For every active unprotected short role `w` and transported phase `phi`,
let `G_w^phi` be its completely regenerated occurrence catalogue after
contracting the protected bank.
For a transferred donor this is the new `MR` catalogue; for a retained old
short it is the retained direct catalogue.  Let `G_e^long` be the complete
four-flag/state catalogue of the new `LLR` long row created by `e`.

A ticket `g` carries its complete signed parent conjunction `A_g`:

* the common base-table/materialization selector and the relevant transfer
  literal `z_e` or `1-z_e`;
* its common-basis representation edges;
* its residual bottom-token placements;
* its predecessor and successor hosts and directed ports;
* its long flags, short address, and physical occurrence resources; and
* every selected-parent supplier record created by that occurrence.

Use binary `lambda_g^phi` and impose only the exact upper AND implications

\[
             \lambda_g^\phi\le \ell\quad(\ell\in A_g^\phi),       \tag{2.1}
\]

together with the role exact-one rows

\[
 \sum_{g\in G_w^\phi}\lambda_g^\phi=a_w,
 \qquad
 \sum_{g\in G_{e,\phi}^{long}}\lambda_{g}^{long,\phi}=z_e.       \tag{2.2}
\]

Because the right sides of (2.2) are binary, (2.1)--(2.2) select a genuine
active conjunction in every required phase; reverse AND implications are
unnecessary unless all currently active occurrences are to be counted.
The structural row and declared common state (including shared flag fields)
are common to the phases.  The selected physical occurrence may differ by
phase unless the catalogue explicitly declares a common occurrence; silently
identifying the two occurrence variables is a stronger, unjustified row.

The `1,748` protected ticket variables, their `3,496` directed host-port
uses, `3,495` movable token placements, one soft endpoint, and selected
flags are fixed to one only on a table branch whose common structural
presentation contains their pinned edges.  Every remaining resource `c`
has its literal
capacity row

\[
        \sum_{g:c\in P(g)}\lambda_g\le 1-b_c,                       \tag{2.3}
\]

where `b_c` is the protected use.  A host may use its opposite directed
port if allowed, but it retains its unique protected long flag.

This is the exact occurrence layer.  Replacing `A_g` by a union or minimum
score on a row, root, or transfer edge is only a relaxation.

## 3. A universal selectable-matching Hall oracle

The matching recourse layers below are instances of one lemma.

Let `G=(A,B,E)` be bipartite.  At a master point `xi`, let `r_a(xi)` be the
binary demand of `a`, and let `p_e(xi)` be the **bidirectional** activation
of edge `e`, expressed as the OR of its selected complete parent DNFs.  Edge
activation already includes the availability of both endpoints.  For a
set `X subset A` and `b in B`, introduce on demand

\[
 n^X_b=\bigvee\{p_{ab}:a\in X,ab\in E\}.                           \tag{3.1}
\]

### Lemma 3.1 (availability-aware Hall separation)

There is a matching saturating every demanded left vertex if and only if

\[
             \boxed{\sum_{b\in B}n^X_b\ge
                    \sum_{a\in X}r_a}\qquad(X\subseteq A).         \tag{3.2}
\]

At an integral master point, one maximum matching plus alternating
reachability either constructs the matching or returns a violated `X`.
After that `X` is installed, (3.1) must be encoded as an exact OR of the
complete signed parent activations.  Then (3.2) is globally valid, not a
fixed-table no-good.

#### Proof

At a fixed integral point, the right side is the number of demanded
vertices in `X` and the left side is exactly the cardinality of their
active neighborhood.  Hall's theorem proves equivalence.  Exact OR
linearization makes the same inequality valid under every later master
assignment.  QED.

If edge availability is encoded only in the forward direction, a stale
edge may remain counted after its selected parent disappears.  Such a cut
is unsound.

## 4. Exact supplier-rank optimization

Let `H_0` be the universe of hard heads, let `d_h` be the selected active-head
bit, put `K=sum_h d_h` (equal to `16,898` on the current face), and let `U`
be the physical supplier identities.  A supplier occurrence
`sigma=(h,u,g)` is active if
and only if its selected parent ticket or long--long edge `g`, its state,
and every signed placement literal are active.  Let `p_sigma` be this exact
AND and, for a separated set `X subset H_0`, put

\[
 n^X_u=\bigvee\{p_{(h,u,g)}:h\in X\}.                             \tag{4.1}
\]

### Theorem 4.1 (exact selected-parent rank epigraph)

For every fixed master assignment, the maximum supplier matching rank is

\[
 \boxed{
 r_{sup}=\min_{X\subseteq H_0}
       \left( K-\sum_{h\in X}d_h+\sum_{u\in U}n^X_u\right).}       \tag{4.2}
\]

Consequently an integer variable `Theta` equals the optimized supplier
rank when it is maximized subject to the lazy cuts

\[
 \boxed{
 \Theta\le K-\sum_{h\in X}d_h+\sum_{u\in U}n^X_u}
 \qquad(X\subseteq H_0).                                          \tag{4.3}
\]

Projection-perfect supplier Hall on the current face is exactly
`Theta=K=16,898`, equivalently

\[
                    \sum_u n^X_u\ge\sum_{h\in X}d_h.              \tag{4.4}
\]

#### Proof

Apply the deficiency form of the bipartite matching theorem to the active
shore `H_*={h:d_h=1}`.  It gives

\[
 K-r_{sup}=\max_{X\subseteq H_*}(|X|-|N(X)|).
\]

Adding inactive vertices to `X` changes neither its active cardinality nor
its active neighborhood, so the minimum may be written over `H_0` with
`sum_(h in X)d_h`.  Equation (4.1) makes
`sum_u n^X_u=|N(X)|`; rearrangement gives (4.2).
Maximizing `Theta` under all its epigraph cuts gives equality.  QED.

This is the requested exact mechanism for optimizing the LLR transfer
choice against supplier rank.  At a candidate `z`, tickets, flags, bottom
placements, and long-edge selection, compute a maximum supplier matching.
Its Dulmage--Mendelsohn shore returns `X`; add (4.3), whose exact parent ORs
price the transfer choices which can really add distinct supplier
identities to that shore.  No additive per-transfer supplier score is used.

If a supplier occurrence is merely possible under some unselected ticket,
it is absent from (4.1).  Likewise, multiple occurrence records with the
same physical supplier contribute one unit, not their multiplicity.

## 5. The matching recourses

The common-basis presentation and the protected-bottom presentation below
are not two independent copies of the lower target allocation.  On the
current fixed-owner/root face, the bottom matching *is* the low-witness
part of the structural table and its selected placements must be identified
with the corresponding common-basis witness literals.  One may use either
the restricted bottom presentation or the general augmented presentation,
but not accept two incompatible completions.  On a root-changing face the
general augmented presentation replaces the restricted one, with all
protected token placements embedded as fixed presentation edges.

### 5.1 Common-basis representation

Use the augmented perfect-matching presentation with shores

\[
     L\dot\cup M\dot\cup\Delta\quad\hbox{and}\quad M\dot\cup R,
     \qquad |\Delta|=2,533.                                     \tag{5.1}
\]

Every selected ticket and transfer fixes a finite partial matching
footprint in this presentation.  Reject endpoint collisions immediately;
delete the used endpoints and call one residual perfect-matching oracle.
By Lemma 3.1, a failed residual matching returns an exact presentation-Hall
cut whose edge activations are linked to the same selected footprints.
The returned perfect matching is the literal pair of common-basis
representatives, not merely a receiver basis.

This is also the exact **common-materialization gate** between the warm47
LLR family and the protected `b268...` bank.  If their union of fixed
footprints is not a partial matching, or its residual presentation fails
Hall, that branch is closed.  A transfer graph computed on warm47 may be
used directly only with warm47 tickets; on the protected branch its columns
must be regenerated prospectively or revalidated by this oracle.

For an `LLR` transfer, this oracle is applied to the **pre-transfer**
compressed carrier: the selected transfer fixes the three carrier witness
edges in (1.1), while (1.2) gives the final physical table.  This cleanly
separates the common-basis carrier certificate from the final noncompressed
LLR table.

### 5.2 Residual protected-bottom matching (restricted structural face)

After fixing the `3,495` protected movable token placements, solve the
`15,151` by `15,151` residual containment matching.  Ticket parents may
prescribe additional token placements.  Delete their endpoints and apply
Lemma 3.1.  A failed matching returns a globally valid bottom-placement
Hall cut, not a no-good for one residual completion.  Its chosen placement
edge is the same literal used by every occurrence DNF and by the structural
matching witness; there is no second independently chosen copy.

### 5.3 Residual long-state flow

Once all `7,395` short tickets are selected, their ports are removed.  The
remaining `9,520` outgoing and `9,520` incoming long ports must be matched
in the exact compatible long--long graph.  Every long arc has an exact
parent DNF in the chosen bottom modes and flags.  Lemma 3.1 gives its exact
availability-aware Hall family.  If supplier edges are carried by a
long--long arc, promote that arc as a sparse master column; its supplier
record is active only when the arc is selected.

This produces a cycle factor.  One chronology still requires separate
subtour/merge constraints.

### 5.4 Supplier matching

Use Theorem 4.1, not a marginal screen.  Supplier perfectness can be imposed
as feasibility through (4.4), or optimized lexicographically through
`Theta` and (4.3).

## 6. Exact Benders algorithm

The following algorithm is finite and proof-safe on the completely listed
catalogues.

1. **Master.** Select one common base-table/materialization branch, LLR
   transfer columns `z` valid on that branch, occurrence tickets `lambda`,
   bottom placements required by those tickets, common flags,
   sparse promoted long--long arcs, and the exact supplier-parent
   activations.  Fix the full private bank.  Maximize lexicographically
   `Theta`, then the number/weight of accepted LLR transfers, then any
   declared secondary ticket objective.
2. **Immediate rows.** Enforce (1.3)--(2.3), all exact-one role rows, all
   protected units, signed DNFs, and named resource capacities.
3. **Structural oracle.** First verify that every protected-ticket and LLR
   parent footprint belongs to one common materialization.  On the
   fixed-owner/root face, complete the residual protected-bottom matching
   and replay the fixed upper witness;
   on a root-changing face, complete the general augmented common-basis
   presentation with the same protected placement literals.  On failure
   add its Hall shore (3.2).  Never accept two inconsistent low witnesses.
4. **Long oracle.** Complete the `9,520` residual long transitions.  Promote
   the chosen long columns, or on failure add its availability-aware Hall
   shore (3.2).
5. **Supplier oracle.** Compute the exact selected-parent supplier matching.
   If its rank is below `Theta`, add the DM optimality cut (4.3); for final
   feasibility require `Theta=16,898`.
6. Repeat until all literal matchings replay simultaneously.

The catalogues are finite, so branching plus cut generation terminates.
This is not a polynomial-time claim: the occurrence exact-cover layer
contains 3-dimensional matching, and the natural combined matrix already
has determinant-two minors.

### Corollary 6.1 (proof-safe cut certificate)

An UNSAT or optimum claim is proof-safe if its bundle contains

* the bound input/catalogue hashes;
* every selected-parent AND/OR definition used by a cut;
* every separated shore and its literal active-neighbor list;
* independent maximum-matching replay for each oracle; and
* a final literal reconstruction of all selected tickets, matching
  representatives, protected resources, long edges, and supplier edges.

A receiver-only common-basis cut, a marginal DNF zero, or a fixed-table
supplier shore does not meet this standard unless its complete parent
guards are included.

## 7. Exact scope and next executable row

This theorem sharply reduces the global `5,647`-role selector to a sparse
occurrence master plus four exact matching separators.  It closes the
algorithmic question of how to optimize LLR choices against supplier rank:
use (4.3), with selected-parent ORs generated from the DM shore.

It does not decide the current K17 instance.  The warm47-derived 470 table is
now bound and marginally repriced, but the common-parent audit rejects its
combination with the protected `b268...` bank.  On that warm47 table the
complete union projection has supplier rank `16,872/16,898`, deficiency
`26`, `23` zero heads, and a maximum-deficiency shore of `36` heads with
`10` supplier identities.  These are exact warm47 projection facts, not a
literal protected-bank or selected-state graph.  The complete regenerated
ticket and long-transition catalogues have not been replayed.  The first
exact finite run should therefore:

1. choose one literal parent and bind its table, transported phases, ticket
   incidences, transfer modes, and supplier records under Theorem 0.1;
2. either regenerate the transfer graph on the protected `b268...` parent,
   regenerate a complete private bank on the warm47-derived table, or prove
   through one prospective common materialization that all of those literal
   descendants coexist;
3. only then regenerate all active `5,647` role DNFs and new LLR long states
   and contract the exact protected `1,748/3,496/3,495` object;
4. build selected-parent supplier records, not union records; and
5. run the lexicographic `Theta` Benders loop above.

Until that bundle passes, `470` is a structural/common-positive transfer
certificate, not a global socket or supplier certificate.
