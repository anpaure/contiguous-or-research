# Chain-aligned scalar--Hall does not imply an exact common cap

Date: 2026-07-31  
Status: solver-free exact counterexample and exhaustive tiny-class audit  
Scope: the staircase/common-cap interface; no claim about a particular
PBBS carrier or about global nonexistence

## 1. Exact semantics used

Let the physical positions be a line.  A middle target `T_i` is assigned a
physical interval `I_i`, and its maximal envelope is

\[
 E_p=\bigcap_{i:p\in I_i}T_i,
\]

with an empty intersection interpreted as the whole coordinate universe.
The complete lower-cell atlas consists of the nonempty physical intervals
which contain no whole `I_i`.  After fixed pins have been intersected into
the envelope, retain a target--cell incidence exactly when installing that
one additional cap leaves every position nonempty, preserves every middle
row and fixed pin, and realizes the proposed lower target on its cell.

For an injective assignment `M`, its maximal common cap is

\[
 A_p(M)=\Gamma_p\cap
        \bigcap_{S:p\in M(S)}S.                         \tag{1.1}
\]

The assignment is realizable if and only if `A(M)` is nonempty at every
position, has OR `T_i` on every middle interval, and has OR `S` on every
selected lower cell.  This is the fixed-assignment maximal-cap equivalence;
there is no alternative word which can repair a failed equation in `A(M)`.

## 2. Absolute two-position obstruction

Use three coordinates `o,a,x`, two positions, and the single middle row

\[
 I=[0,1],\qquad T=\{o,a,x\}.
\]

This is a chain-aligned staircase (there is only one row), and its legal
maximal envelope is `E_0=E_1=T`.  Its complete lower-cell atlas is exactly

\[
 C_0=[0,0],\qquad C_1=[1,1].
\]

Require the two lower targets

\[
 S_0=\{o\},\qquad S_1=\{o,x\}.                         \tag{2.1}
\]

Every target--cell incidence is individually exact.  Capping either one
singleton by either target realizes that target, while the other position
retains `T` and therefore preserves the middle row.  Thus the exact
individually-sound marginal graph is `K_{2,2}`.  It satisfies Hall, and its
scalar capacity equals its target count: `2=2`.

### Theorem 2.1

No target-saturating matching in this graph has an exact common cap.

#### Proof

Every perfect matching uses both singleton cells.  Formula (1.1) makes the
two letters `S_0` and `S_1`, in one order or the other.  Their union is
`{o,x}`, so the middle row loses `a`.  Both positions remain nonempty and
both lower cells remain exact; the failed middle bit is the only defect.
By maximality (1.1), no smaller word can restore it.  ∎

The two physical cells are disjoint, hence laminar.  Therefore neither
interval geometry, cell laminarity, chain-aligned deadlines, a permanent
owner `o`, scalar capacity, nor marginal Hall supplies the missing lift.

### Minimality

Within the canonical one-full-span-row class, at least two targets and two
cells are necessary: with one target, individual soundness already is the
simultaneous condition, while Hall cannot match two targets to one cell.
With two positions the complete atlas is forced to be the two singleton
cells.  On a two-coordinate universe the only two distinct nonempty proper
targets are the complementary singletons, whose union preserves the full
middle row.  A three-coordinate universe is therefore necessary, and the
example above is minimal in positions, targets, cells, and coordinates among
permanent-owner examples of this form.

The independent census checks every universe of size at most three and
every one- or two-position member of this class.  Its first unrestricted
failure is the coordinate-renamed pair `{1},{2}` at three coordinates; its
first permanent-owner failure is `{1},{1,2}`.  There is no failure with at
most two coordinates or at most one position.

## 3. Forced Johnson-staircase obstruction

The preceding core is absolutely minimal but its marginal graph is
`K_{2,2}` and its sole middle row is the full coordinate universe.  The
following slightly larger core has the geometry relevant to a carrier: two
distinct same-rank Johnson neighbours, a nontrivial overlapping staircase,
the complete physical atlas, and a **unique forced** marginal matching.

Use coordinates `o,a,u,v`, rank-three rows

\[
 T_0=\{o,a,u\},\qquad T_1=\{o,a,v\},
\]

and schedule

\[
 I_0=[0,1],\qquad I_1=[1,2].                            \tag{3.1}
\]

The starts and deadlines are strictly increasing, their union is an
interval, and the maximal envelope is

\[
 (E_0,E_1,E_2)=(\{o,a,u\},\{o,a\},\{o,a,v\}).          \tag{3.2}
\]

Both rows are exact in (3.2).  The complete lower-cell atlas consists of
the three singleton cells, so its scalar capacity is three.  Require

\[
 S_0=\{o,u\},\qquad S_1=\{o\}.                          \tag{3.3}
\]

Exact one-edge replay gives the complete marginal graph

\[
 N(S_0)=\{[0,0]\},\qquad N(S_1)=\{[1,1]\}.             \tag{3.4}
\]

Indeed `S_0` needs the private coordinate `u`, which exists only at position
zero.  Putting `S_1` at position zero would delete the sole `u` provider of
`T_0`; putting it at position two would delete the sole `v` provider of
`T_1`.  Position one is individually safe because each uncapped endpoint
still carries its complete row.

### Theorem 3.1

The system (3.1)--(3.4) has scalar surplus one and a unique marginal perfect
matching, but it has no exact common cap.

#### Proof

The forced assignment caps (3.2) to

\[
 (\{o,u\},\{o\},\{o,a,v\}).                            \tag{3.5}
\]

Every position is nonempty and both selected singleton cells are exact.
The second middle row remains `{o,a,v}`, and the union of all three positions
is still the full rank-four upper target `{o,a,u,v}`.  But the first middle
row has value `{o,u}` and has lost exactly `a`.  Maximality of (3.5) makes
the failure final.  ∎

This is minimal for the stated Johnson-singleton structure.  Two distinct
length-two staircase rows require at least three positions.  To cap their
overlap nontrivially while retaining a permanent owner `o` and deleting a
second shared bit `a`, their intersection must have size at least two, hence
the row rank is at least three.  A distinct same-rank Johnson neighbour then
needs the two private coordinates `u,v`, hence at least four coordinates.
Two targets are already the minimum possible simultaneous conflict.

Compared with Theorem 2.1, this core spends one extra position and one extra
coordinate to remove every possible matching choice: marginal Hall is not
merely compatible with a bad matching; its **only** matching is bad.  It is
therefore the sharper local obstruction for a carrier-level theorem.

## 4. Lift containing every lower target for `k=r=3`

The two-target core can be embedded without omitting the other lower
targets.  Use six positions, the same middle row `[0,1]` labelled by the
three-coordinate universe, and the uncapped maximal envelope equal to the
whole universe at every position.  Fix the other four nonempty proper
subsets as legal singleton pins:

\[
 \{a\}\mapsto[2,2],\quad
 \{x\}\mapsto[3,3],\quad
 \{o,a\}\mapsto[4,4],\quad
 \{a,x\}\mapsto[5,5].                                 \tag{4.1}
\]

After exact residualization the envelope is

\[
 (\{o,a,x\},\{o,a,x\},\{a\},\{x\},\{o,a\},\{a,x\}). \tag{4.2}
\]

The complete atlas has 16 cells: `[0,0]` and all 15 nonempty intervals in
the tail `[1,5]`.  Hence total scalar capacity is `16` for six targets; after
the four pinned cells are reserved, residual scalar capacity is `12` for two
targets.

Rebuilding the complete individually-sound residual graph from (4.2) gives
exactly

\[
 N(\{o\})=N(\{o,x\})=\{[0,0],[1,1]\}.                 \tag{4.3}
\]

For example, the apparent tail cells `[3,4]`, `[4,5]`, and `[3,5]` could
locally union to `{o,x}`, but they delete the private `a` provider of one of
the fixed pins in (4.1), so exact one-edge replay correctly excludes them.
Equation (4.3) is therefore the complete rebuilt residual graph, not a
hand-selected subgraph.

Hall holds in (4.3), but every residual perfect matching is the obstruction
of Theorem 2.1 and loses `a` from the middle row.  Thus **all six** nonempty
proper subsets of the three-coordinate universe are present—four fixed and
two residual—yet no exact common cap exists.

This schedule is also a legitimate tail-start `P/Q` staircase: with one
selected start and five omitted starts, take the sole owner interval to be
`[0,1]`.  The large arbitrary-start tail supplies 15 cells, but those scalar
particles do not repair the protected-trace conflict.  This is precisely why
an arbitrary-start counting threshold cannot replace common-cap guards.

## 5. Consequence and sharp boundary

Any zero-defect compiler theorem must add data that sees surviving physical
traces.  Valid examples are:

1. a guarded subgraph which still satisfies Hall;
2. the exact conflict-clutter inequalities;
3. an actually proved total-unimodularity statement for the **augmented**
   matching-plus-trace matrix; or
4. a carrier-specific canonical greedy invariant that ensures every required
   middle and assigned-lower bit retains a provider.

Laminarity of the cells alone is strictly too weak: Theorem 2.1 already uses
disjoint singleton cells.  The positive `k=16` common-cap certificate is
consistent with this obstruction because it selects a different matching
whose maximal cap passes every trace equation; it does not establish an
automatic marginal-Hall lift.

## 6. Frozen audit

```text
scratch/audit_commoncap_chain_aligned_minimal_counterexample_20260731.py
SHA-256 ffb44523c28a27baeecc6dc6e0d00c0eba64dc1a2fd3e21976d35ca1ce8177df

scratch/commoncap_chain_aligned_minimal_counterexample_20260731.audit.json
SHA-256 f3ccc762072f68974eb5025b4d77a8d7be8adb56278fc5abfc48d7fb8a8b32b0
payload  f47bfdb1e734e5cda7ff2cbbff8d06080719b7c5d4a6fff9ab159b6edd80e3d7
```

The audit enumerates the complete physical atlases, every individually exact
incidence, every residual injection, and the literal maximal-cap replay.  It
uses no optimizer or SAT solver.
