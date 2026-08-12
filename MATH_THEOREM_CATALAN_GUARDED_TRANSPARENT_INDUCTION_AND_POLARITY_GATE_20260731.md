# Guarded transparent induction and the first connector-polarity obstruction

Date: 2026-07-31  
Status: exact all-dimension composition theorem on an explicit private
ownership face; exact common-basis avoidance corollary; solver-free finite
counterexample to matching-first gluing; the joint side-realization/supply
lemma remains open

## 0. Verdict

The verified `ML(11)` reset proves that all rows required by the Catalan
construction can coexist on one nontrivial finite object: turn palettes,
gap--Hall interlacing, physical topology, residence, every deep shadow, and
the lower compiler.  The transparent-hexagon, automatic-common-basis and
topology-decoupling theorems identify how such objects could recurse.

There is now an exact proof-sufficient induction invariant.  Besides the
usual decorated factor boundary, it carries:

1. a leaf-peelable occurrence-gap forest and its matching;
2. an oriented physical socket forest with its endpoint pairing;
3. capped coordinate-run boundary records for residence;
4. an explicit privately owned witness for every protected deep-shadow
   target; and
5. an explicit privately owned compiler SDR.

If every internal join is transparent and its new gap edges, physical
connector, shadow witnesses and compiler cells are node-private, these five
rows compose by induction.  This is proved below.

What remains is existence of the required correlated joins.  In particular,
one may not first choose an arbitrary perfect augmented matching and then
connect its path forest.  The first matching decoded from the exact `k=11`
reset already gives a solver-free counterexample: eleven of its 132 paths
are **orientation-polarity traps**.  For one explicit path, one orientation
admits entrances but no exits under even the weak minimum-run-three guard,
while the reverse admits exits but no entrances.  No residence-preserving
cyclic concatenation of that fixed forest exists.

Thus the missing uniform theorem is not another Hall inequality.  It is one
joint integral statement choosing the common basis, physical side forests,
path orientations/connectors and downstream ownership tables together.

## 1. The guarded private-tree state

Fix a required coordinate one-run threshold `h>=1` and a rooted binary
gluing tree.  A state at a node `x` consists of the following literal data.

### 1.1 Decorated factor and gap matching

The physical middle-levels factor inside `x` has globally named selected
turn occurrences.  They own disjoint exact lower and upper palette banks and
alternate by shore on every marked component.  Its occurrence-labelled
gap--colour graph is a forest with its displayed perfect matching.

At the boundary store the selected/unselected bits, the exact current owner
colours, first and last selected shore types on each exposed fragment, and
the connectivity partition and exposed mate relation of the gap forest.
This is the exact transparent-collar state of the leaf-peelable transfer
theorem.

### 1.2 Physical socket forest

After orienting its finalized path components, the node exposes a directed
linear forest.  Store every literal endpoint occurrence, the pairing of
endpoints joined by retained internal paths, the remaining degree demands,
its used private-resource owners and, in a clean quotient, the gain of every
oriented path.  A one-chain tree-contiguous socket record is a useful special
case, not part of the general invariant.

### 1.3 Residence record

For every coordinate `a`, record:

```text
first bit, last bit,
length of the first run capped at h,
length of the last run capped at h,
whether every completed internal one-run has length at least h.
```

The record is taken on the oriented physical chain.  A closed root is
accepted only when the wrap seam passes the same test.

### 1.4 Deep-shadow ownership

Let `S_x` be a named bank of required targets.  For every target in `S_x`,
store one explicit consecutive window entirely contained in the chronology
already finalized below `x`, together with its intersection or union value.
Banks owned by distinct nodes are disjoint.  A child-internal witness is
never allowed to cross a future cut.

This is deliberately stronger than support-only coverage: it records a
provider which later joins cannot delete.

### 1.5 Compiler ownership

Let `C_x` be a named bank of lower targets.  Store an injection from `C_x`
to literal short-interval/envelope cells finalized below `x`, with every
assigned cell containing its target legally.  Target banks and cell banks
owned by distinct nodes are disjoint.  Equivalently, store an actual partial
SDR rather than only its Hall inequalities.

At the root the shadow banks must partition every required lower and upper
shadow target, and the compiler banks must partition the complete lower
target family.

## 2. Exact composition theorem

Call an internal binary join `x=(y,z)` **guardedly private and
transparent** when all of the following hold.

1. The local turn-colour multisets before and after agree separately on the
   two shores, and the retained-fragment endpoint types alternate after
   reconnection.
2. Its new gap attachment is a tree meeting the retained gap core in at
   most one component; its private gap vertices/colours are disjoint from
   every other node's bank, and its displayed matching extends the two child
   matchings.
3. The node-private legal connectors join child path endpoints, use no
   retained forest edge or resource owned elsewhere, and their attachment
   graph on the child paths is a forest.  They therefore merge paths but
   never seal a nonterminal cycle.
4. The residence records compose legally: whenever the seam separates two
   unequal bits, every one-run completed at that seam has length at least
   `h`; equal one-runs are merged and capped at `h`.
5. Every new shadow target owned by `x` has its displayed window inside the
   two child collars plus the new seam.  It is distinct from all descendant
   target banks.
6. Every new compiler target owned by `x` is assigned to a new private
   collar cell, disjoint from all descendant cells and all other assignments
   at `x`.

### Theorem 2.1 (guarded private-tree composition)

Suppose every leaf carries an accepted state of Section 1 and every internal
node is guardedly private and transparent.  Then every node carries an
accepted state of Section 1.  If the root banks are complete, the root has:

* exact alternating turn representatives and hence gap--Hall interlacing;
* a leaf-peelable occurrence-gap graph;
* one physical linear forest; after a supplied legal endpoint completion,
  one cycle or the declared number of linear carrier pieces (and primitive
  voltage when required);
* coordinate residence at least `h`;
* all declared deep intersection/union shadows; and
* a compiler SDR for every declared lower target.

#### Proof

Induct up the rooted tree.  Turn-palette equality and the endpoint-type test
are exactly the transparent-polygon theorem, so the selected occurrences
remain one joint alternating decoration.  The retained gap core is a forest;
contracting it turns the new private attachment into a tree meeting the old
core once.  Expanding the contraction therefore gives another forest.  The
union of the child matchings and the displayed private matching is perfect,
so the gap forest remains leaf-peelable.

The two child physical forests are vertex-disjoint.  Contract every child
path.  Condition 3 says that the new connector graph is a forest, so its
expansion is again a linear forest and contains no sealed subtour.  Private
resource ownership preserves every literal capacity.  At the root one may
either retain its path pieces and charge the deliberate seams to the
compiler budget, or supply a legal endpoint completion.  In the latter case
the ordinary occurrence-cycle and gain tests are necessary and sufficient
in a clean quotient.

Every coordinate run wholly inside a child is already legal.  At the new
seam, equal one-runs merge and can only lengthen; unequal bits complete at
most the suffix one-run of the left child and the prefix one-run of the right
child.  Condition 4 checks exactly these runs.  The capped prefix/suffix
record is therefore sufficient and associative.

A descendant shadow witness lies wholly inside a finalized child chronology,
so the join changes none of its vertices or adjacencies.  New node-owned
witnesses are checked literally.  Disjoint union of the target banks proves
the shadow assertion.  The compiler argument is identical: old assigned
cells survive, new cells are legal, and private target/cell ownership makes
the union of the child injections and the node injection an injection.

All assertions follow at the root when its banks are complete. `square`

This theorem is dimension-uniform, but it is conditional.  Its point is to
make the downstream rows genuinely compositional rather than silently infer
them from central palettes.

## 3. What the automatic common basis additionally buys

Use the constants of the automatic-common-basis theorem:

\[
 N=\binom{2n}{n-1},\qquad C=\operatorname{Cat}_{n+1}.
\]

Its balanced common-basis distribution has marginal

\[
 {C\over N}={2(2n+1)\over n(n+2)}.                 \tag{3.1}
\]

### Lemma 3.1 (protected-edge avoidance)

For every forbidden child-edge set `R` satisfying

\[
 |R|<{N\over C}={n(n+2)\over2(2n+1)},              \tag{3.2}
\]

there is a synchronized common basis `Q` with `Q cap R` empty.

#### Proof

Under the balanced distribution,

\[
             E|Q\cap R|={C\over N}|R|<1.
\]

The random variable is a nonnegative integer.  Hence some common basis has
value zero. `square`

More generally, every nonnegative additive boundary-risk function has a
common basis whose cost is no larger than its uniform-density average.
Thus a bounded protected collar is eventually avoidable by the incidence
choice.  This does not choose physical diagonal representatives, prove
node privacy, or protect an unbounded provider/compiler bank.

After `Q` is fixed, the topology-decoupling theorem removes the global cycle
condition: it suffices to realize one Catalan-size anchor pairing on the
left shore and its greedy acyclic completion on the right, with no
anchor-free side components.  Hence incidence and abstract global topology
are not the missing rows of Theorem 2.1.

## 4. A solver-free obstruction to matching-first gluing

Decode the perfect augmented matching in

```text
scratch/ml11_guarded_full_reset_20260731.audit.json
```

into its 132 paths on the 924 rank-six masks of `[12]`.  Consider the path

```text
P = 119,63,159,2203,2266.                            (4.1)
```

For every other path and both of its orientations, enumerate a directed
Johnson connector into or out of `P`.  Call a seam weakly residence-safe
when every boundary-crossing coordinate word of length three or four avoids

```text
010, 0110.                                           (4.2)
```

This is necessary for cyclic coordinate one-runs to have length at least
three, and hence necessary for every stronger residence threshold.

### Theorem 4.1 (orientation-polarity trap)

In the forward orientation of (4.1), there are exactly two weakly safe
incoming seams and no weakly safe outgoing seam.  In the reverse
orientation, there are exactly two weakly safe outgoing seams and no weakly
safe incoming seam.  Consequently the fixed 132-path forest admits no
cyclic orientation/concatenation by literal Johnson connectors with even
minimum coordinate one-run three.

#### Proof

The two other relevant unoriented paths are

```text
629,630,694
371,1379,1351,1477,3524,3462.
```

With paths sorted by `(length,lexicographic word)`, their oriented state
indices are `44,45` and `148,149`; the two states of (4.1) are `100,101`.
Exact seam replay gives

```text
45 -> 100,   149 -> 100,
101 -> 44,   101 -> 148,
```

and no other weakly safe seam incident with states `100,101` in the needed
direction.  A cyclic concatenation must orient `P` once and use that same
oriented state for one incoming and one outgoing seam.  Neither state has
both, a contradiction. `square`

The standard-library audit finds eleven such polarity paths, not just
(4.1).  The proof uses no optimizer or SAT status.  Pairwise seam safety is
only a necessary test, so omitting longer multi-seam windows cannot create a
false obstruction.

### Corollary 4.2 (six-chain floor)

Every weakly residence-safe concatenation of the fixed 132 paths into a
linear path cover has at least six output paths.

#### Proof

Each of the eleven polarity paths can occur only as an endpoint path of an
output chain: neither orientation has both a safe entrance and a safe exit.
One output chain has only two ends.  Therefore at least
`ceil(11/2)=6` chains are required. `square`

This theorem is sharply scoped.  It does not rule out another perfect
augmented matching, splitting/rethreading these paths, or choosing matching
and connectors jointly.  It rules out exactly the tempting implication

```text
fully guarded carrier + arbitrary perfect matching
    => residence-safe post-hoc one-chain connection.
```

## 5. The exact remaining lemma

The four authoritative ingredients now leave one correlated construction
statement.

> **Joint guarded side-realization lemma.**  For every accepted child state
> and every two-coordinate recursion step, choose simultaneously:
>
> 1. one automatic synchronized common basis `Q`;
> 2. its two saturating diagonal representatives as punctured side forests,
>    realizing the prescribed anchor pairings of topology decoupling;
> 3. a transparent/private connector forest with an explicitly budgeted
>    number of terminal carrier pieces; and
> 4. the residence, deep-shadow-provider and compiler-SDR ownership tables
>    of Theorem 2.1,
>
> so that the resulting parent state is accepted.

The common basis exists unconditionally, and the global pairing can be
chosen abstractly.  What is not proved is a **single integral realization**
of those choices together with the provider/compiler tables.  Theorem 4.1
shows that sequentially choosing them is false already at the first fully
guarded base.

The `ML(11)` reset supplies a positive leaf state for this relation: all
logical guard rows coexist.  It is not extension-surjective, because its
first decoded forest has the polarity obstruction.  A uniform proof must
either establish the joint guarded side-realization lemma, or enlarge the
state so a bounded reset can rethread polarity paths before they are sealed.

## 6. Audit and scope

Run

```text
python3 scratch/audit_ml11_full_reset_forest_orientation_polarity_20260731.py
```

and compare its stdout with

```text
scratch/ml11_full_reset_forest_orientation_polarity_20260731.audit.json.
```

The audit reconstructs the 132 paths from the frozen physical edge list,
checks every path and connector literally, enumerates both orientations of
every component, and reports all eleven polarity traps.  The all-dimension
composition and avoidance statements are mathematical proofs; the finite
obstruction is exhaustive only for this one decoded forest.  No all-`k`
existence or nonexistence conclusion is asserted.
