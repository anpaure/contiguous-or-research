# K17 exact radius-one matching escape and the post-supplier occurrence gate

**Date:** 2026-08-02  
**Status:** proof-complete finite reduction and independent audit through the
accepted deficiency-`80` checkpoint.  This is a theorem about the declared
protected `b268` transfer face and its generalized supplier projection.  It
is not a common occurrence-labelled state, chronology, compiler, or `k=17`
word.

## 1. Declared transfer face

Let `E` be the `11,893` common-marginal-positive protected transfers in the
authenticated `b268` catalogue.  Each transfer has one `LR` host row and one
`LMR` donor row.  A selected transfer set is therefore a matching in the
bipartite row graph.  The complete common face has matching rank `464`.

The current construction uses a seed matching `M` of size

\[
                         m=438.
\]

For nonnegative integers `p,q`, define its bounded exchange face

\[
 {cal R}_{p,q}(M)=
 \{M'\subseteq E:M'\text{ is a matching},
       |M\setminus M'|\le p,
       |M'\setminus M|\le q\}.                 \tag{1.1}
\]

The authoritative controller additionally imposes `|M'| >= 438` and uses
`p=q=1`.

## 2. Exact radius-one matching characterization

For an unselected edge `f in E-M`, put

\[
 C_M(f)=\{e\in M:e\text{ shares a row endpoint with }f\}. \tag{2.1}
\]

Because `M` is a matching, `|C_M(f)|` is `0`, `1`, or `2`.

### Theorem 2.1 (complete radius-one escape list)

The matchings in

\[
 {cal R}_{1,1}(M)\cap\{M':|M'|\ge m\}             \tag{2.2}
\]

are exactly:

1. `M` itself;
2. `M+f` for every `f` with \(C_M(f)=\varnothing\);
3. `M-e+f`, where either
   * `C_M(f)={e}`, so the dropped edge is forced, or
   * \(C_M(f)=\varnothing\), in which case any `e in M` may be dropped.

No edge with `|C_M(f)|=2` can enter this face.

#### Proof

Write

\[
 d=|M\setminus M'|,\qquad a=|M'\setminus M|.
\]

The radius gives `d,a <= 1`, while `|M'|=m-d+a >= m` gives `a>=d`.
Thus `(d,a)` is one of `(0,0)`, `(0,1)`, or `(1,1)`.

In the add-only case, the new edge must be disjoint from every edge of `M`,
which is exactly \(C_M(f)=\varnothing\).  In the swap case, `f` must be disjoint from
`M-e`, which is equivalent to `C_M(f) subseteq {e}`.  This gives the two
subcases above and excludes `|C_M(f)|=2`.  Conversely, every listed set is a
matching of the required radius and cardinality.  \(\square\)

This theorem supplies a solver-free enumeration of the *matching* escape
face.  The hard part is evaluating the nonlinear supplier and socket rows on
each materialized table.

## 3. Exact activated supplier-Hall separator

For a selected transfer matching `S`, let `T(S)` be its literal materialized
table, and let `G(S)` be the complete generalized `6/9/4` supplier graph.  Its
hard-head shore has size

\[
                         H=16,898.
\]

Define

\[
 \delta(S)=H-\nu(G(S))
          =\max_{X\subseteq H}\bigl(|X|-|N_{G(S)}(X)|\bigr). \tag{3.1}
\]

A Hall shore extracted from one incumbent is mode-labelled: if an endpoint
row is transferred, the head occurrence and supplier occurrence use that
specific edge-labelled row state.  For such a shore `X`, let `a_h(z)` be the
exact activity of head occurrence `h` under transfer selector `z`, and let
`n_(X,u)(z)` say that supplier identity `u` has at least one compatible
active occurrence into an active member of `X`.  Both predicates are exact
bidirectional Boolean DNFs over row modes.

### Theorem 3.1 (globally valid activated Hall row)

Every table with supplier deficiency at most `k` satisfies

\[
 \boxed{
   \sum_{h\in X}a_h(z)-\sum_u n_{X,u}(z)\le k.
 }                                                        \tag{3.2}
\]

#### Proof

Under a fixed selector `z`, the active members of the mode-labelled set form
an ordinary hard-head subset `X(z)`.  The first sum is `|X(z)|`.  Because
`n_(X,u)` is an exact OR over all compatible active occurrence pairs, the
second sum is exactly `|N(X(z))|`, counting each supplier identity once.
Equation (3.2) is therefore the Hall inequality

\[
                 |X(z)|-|N(X(z))|\le k,
\]

which holds for every head subset if and only if the graph deficiency is at
most `k`.  \(\square\)

At an incumbent with deficiency greater than `k`, its maximum alternating
shore violates (3.2).  Hence the row removes that incumbent but no feasible
one.

### Theorem 3.2 (finite exact radius-Benders oracle)

Fix `M,p,q,k` and a transfer-cardinality floor.  Repeatedly:

1. solve the exact row-matching and radius master with all accumulated rows
   (3.2);
2. materialize every SAT selector and rebuild `G(S)` from definition;
3. accept if `delta(S)<=k`; otherwise add the maximum-shore row (3.2).

With exact SAT decisions and no iteration limit, this process returns SAT if
and only if the declared radius face contains a table of deficiency at most
`k`.  If the final master is UNSAT, a DRAT-verified proof certifies that no
such table exists in that face.

#### Proof

Every added cut is necessary by Theorem 3.1, so no feasible selector is ever
removed.  Every failed selector is removed by its own violated cut.  The
radius face is finite, so either a feasible selector is encountered or all
selectors are removed and the master becomes UNSAT.  \(\square\)

The bounded-exchange implementation is

```text
17c587bb39afca212a5f4afcfc530d748f1e136007efdf58a656fecba8939bf0
  /home/amodo/or15/work/root_k17_b268_llr_radius_20260802/src/
    solve_k17_llr_supplier_benders_radius_20260802.cpp
1122929a8d6b36e05bbefcbd452cdcc102bdf9e2e9fa0d8c4143adda71533c44
  /home/amodo/or15/work/root_k17_b268_llr_radius_20260802/solve_radius
```

The source uses independent at-most-one-drop and at-most-one-add sequential
counters, in addition to the transfer matching and cardinality floor.

## 4. What the socket controller does and does not certify

The radius Benders master optimizes the supplier projection.  The controller
then rematerializes the winning table, prices all `7,395` short roles in the
native phase 0 and transported opening phase 1, and computes

\[
 (P_0,P_1,P_\cap,P_\cup).
\]

Its strict mode accepts only coordinatewise nondecreasing tuples.  Its floor
mode accepts only

\[
 P_0,P_1,P_\cap,P_\cup\ge1748.                        \tag{4.1}
\]

This post-pricing check is not a Benders constraint.  Therefore:

* an accepted step is a literal positive witness for both supplier and its
  reported socket policy;
* `STOP_SOCKET_REGRESSION` or `STOP_SOCKET_FLOOR` rejects the particular SAT
  candidate returned by the supplier master;
* such a stop does **not** prove that every other radius-one supplier escape
  violates the socket policy.

An exact combined no-go would require putting the complete socket DNFs and
the desired tuple bounds inside the finite master, or exhaustively evaluating
the candidate list of Theorem 2.1.

Likewise, a timeout, signal, or non-verdict exit is `UNKNOWN`, never UNSAT.

## 5. Independently audited floor chain through deficiency 80

The accepted floor chain is

```text
def   supplier       P0    P1   both  either   one-for-one exchange
83    16815/16898    3100  2257  1841  3516    -12615 +72987
82    16816/16898    3100  2258  1841  3517    -15440 +93220
81    16817/16898    3100  2259  1842  3517    -32175 +72738
80    16818/16898    3100  2259  1842  3517    -32928 +81210
```

The terminal exact hashes are

```text
f9885b6b47ff65f726db35ef63b0beaffb17a0f89ec032a1deef263c60828d8c
  def80 selected transfers
b77e15e6ec68c52c50d9a3ac1e51b19d05fe0064e498d48a0763e7e25eb586ce
  def80 materialized table
e65933dae1b7140291f7f2e1c4e454b268bc0c1d2cd18d2ff71b152747d2121c
  def80 supplier projection
```

A fresh build of the current materializer/evaluator independently replayed
that selected set at iteration zero and reproduced all three hashes, supplier
rank `16818`, and shore `91/11`.

The independent static ledger auditor additionally checked every accepted
row `83` through `80` for:

* ledger, selected, table, and projection hashes;
* exactly one removed and one added transfer;
* `438` row-disjoint transfers and `876` distinct endpoint rows;
* exact equality between the changed table rows and those endpoints;
* disjointness from all `7,213` protected physical rows;
* full two-phase DNF recount and the four reported socket coordinates;
* every compressed CNF/model/pricer trace against its hash in
  `PRECOMPRESSION.sha256` by streaming decompression.

```text
d38167413fe52306b484804da3561edde5e146b9f0190e0465d2501712077d22
  scratch/audit_k17_b268_radius_chain_ledger_20260802.sh
18f5f5c3f1cef4db84e6217e29ccfdb3c7f6f7497e80240775614835a12d61c5
  floor_chain_through80.audit.txt
7889657625baa7b45636f0379cd14e5f2e0fd8e31a8a8840d34e3e14b98af44e
  def80_independent_replay.summary.txt
```

The first attempt from deficiency `80` to target `79` ended with process
status `143`; that run remains `UNKNOWN` and supplies no UNSAT claim.  A
separately restarted controller subsequently accepted a deficiency-`79`
table, but it lies beyond the independent checkpoint audit in this note.

## 6. What supplier deficiency zero would prove

If this declared face reaches `delta=0`, it proves exactly that the
materialized row-pair supplier projection has a perfect matching on all
`16,898` hard heads, while retaining the protected ticket rows and the stated
two marginal-positive transfer catalogue.

It would **not** yet prove a common occurrence-labelled state.  At the
deficiency-`80` checkpoint, the complete marginal socket counts are only

\[
                    (3100,2259,1842,3517)
\]

out of `7,395` short roles.  Thus even supplier perfection would leave the
literal ticket/state problem substantial rather than formal.

## 7. Exact next gate after projected supplier perfection

The next proof-safe object must select all of the following on one common
materialized table.

### 7.1 Residual outer/common-basis matching

Rebuild the complete active outer containment graph for the final table and
choose one outer matching/common basis extending the protected `1,748`-ticket
bank and its `3,495` forced movable endpoint assignments.  Static receiver
allocation is weighted matroid intersection, or equivalently the specialized
matching flow.  It does not select occurrence witnesses.

### 7.2 One ticket per literal short role

For every remaining fixed/free short role, choose one occurrence-labelled
ticket whose complete DNF agrees on

* table row state;
* selected outer edges;
* predecessor and successor hosts and flags;
* bottom-token and physical-address resources.

The protected `1,748` tickets and all chosen residual tickets must coexist.
Marginal positivity is only an OR over possible tickets and cannot replace
these exact-one resource rows.

### 7.3 One common contracted state cover

Choose one flag per long role and complete the unused incoming and outgoing
long ports by direct transitions.  After ticket choices are fixed, this is a
bipartite Hall flow; before they are fixed, it is a typed hypermatching and
is not generally totally unimodular.

### 7.4 Selected-parent supplier matching

Every supplier occurrence must be activated by both its complete
table/outer/state DNF and its selected parent primitive.  The projected
row-pair supplier edge is insufficient.  The exact selected-state Hall rows
must then saturate all `16,898` hard heads.  If both owner phases are required,
their occurrence records must share the same underlying table, outer
matching, addresses, and compatible flags; two independent phase witnesses
do not compose.

### 7.5 Topology

The preceding rows give a contracted cycle cover.  One-cycle connectivity
still needs subtour joining or an equivalent topological certificate.

### Theorem 7.1 (exact decomposition of the next gate)

For a fixed final transfer table and a complete cloned occurrence catalogue,
feasibility of the rows in Sections 7.1--7.4 is equivalent to a target-exact
contracted common-state cycle cover extending the protected bank and having a
perfect selected-parent supplier matching.

#### Proof

The outer/common-basis degrees choose the literal containing-root allocation.
The ticket exact-one and resource rows choose one realizable occurrence for
every short role.  Contracting each selected long--short--long ticket leaves
one incoming and one outgoing port at every long state; the direct-transition
Hall flow fills exactly the unused ports.  Finally, selected-parent
activation constructs the literal supplier graph, and Hall's theorem is
equivalent to its perfect matching.  Conversely, reading these choices from
any such labelled cover satisfies every displayed family.  \(\square\)

This gate is naturally solved by branch plus matching-flow/Benders
separation.  The static common-basis polytope remains integral, but appending
literal socket implications already contains a determinant-`2` submatrix, so
ordinary matching integrality does not survive automatically.

## 8. Scope after the next gate

Even a successful common-state cycle cover would still leave one-cycle
joining, carrier transport for the second phase, physical chronology,
residence, arbitrary-width upper shadows, common cap, lower compiler, and the
literal word.  Supplier deficiency zero is therefore an important projection
milestone, not the solution of `k=17`.
