# Lane L: bounded-debt incidence-circuit fusion for NRFC

Date: 2026-08-01  
Status: exact conditional all-parameter theorem, sharp abstract obstruction,
and independently replayed finite `k=17` calibration.  This note does not
prove NRFC, an all-`k` connector supply theorem, or a compiler theorem.

## 0. Outcome

The exact zero-defect fusion target can be weakened without losing a useful
inductive statement.

Suppose an occurrence-labelled factor is already exact on its named palettes
but has several components.  If serial-safe incidence circuits merge those
components and their **statewise literal palette changes** form a component
coboundary

```text
Delta(C_1,...,C_s -> E)
       = pi(E)-pi(C_1)-...-pi(C_s)+epsilon,
```

then all internal component terms cancel over the merge tree.  The terminal
palette debt depends only on the root-minus-leaf boundary and the sum of the
exceptional errors.  In particular it is `O(1)` independently of the number
of components whenever those two quantities are `O(1)`.

There is a chronological alternative.  If circuit payloads are port
coboundaries and the selected sequence splits into only `O(1)` compatible
port chains, then only the `O(1)` chain endpoints survive.  This gives the
same bounded-debt conclusion.

Both qualifications are necessary.  Even resource-disjoint component merges
that each lose only one new palette colour can accumulate `c-1` holes while
joining `c` components.  A bare endpoint-potential formula does not prevent
this on a star: the star has `c-1` incompatible one-edge port chains.

The finite `k=17` assignment circuits are a clean calibration, not an
all-`k` proof.  A strict-dual `D`-assignment `C6` is palette-complete
(zero-debt, but with nonzero signed payload) and does not fuse the two
physical components.  A `C12` makes the auxiliary permutation `A` Hamilton
but leaves the physical `A^2` factor split and has one q1 hole on each shore.
A non-dual `C16` makes the physical factor one cycle and leaves exactly two
lower-q1 holes and no upper-q1 hole.  Thus bounded debt, rather than exact
zero, is the correct first connector target.

## 1. Literal palette ledger

Let the protected palettes be finite, pairwise-disjoint sets

```text
P = disjoint_union_(a in I) P_a.
```

The index `a` may encode shore, rank, or another named target class.  For a
literal factor state `F`, let

```text
mu_F(p) = number of selected occurrences carrying target p.
```

All loads are nonnegative integers.  Define the missing-colour debt on one
palette and in total by

```text
h_a(F) = sum_(p in P_a) (1-mu_F(p))_+,
h(F)   = sum_a h_a(F).                                  (1.1)
```

For a signed vector `v`, write `v_-=(-v)_+` coordinatewise.

Because the loads are integral and nonnegative, `(1-mu)_+` is the indicator
that the colour is absent.  Thus support debt and `l_1` debt coincide.

Consider a serialized sequence of legal incidence-circuit moves

```text
F_0 --e_1--> F_1 --e_2--> ... --e_q--> F_q.
```

Its **statewise** signed payload is

```text
Delta_j = mu_(F_j)-mu_(F_(j-1)) in Z^P.              (1.2)
```

This definition is important when circuits overlap.  A delta computed against
the original factor may not be added after an earlier circuit has changed one
of the same turns.

### Lemma 1.1 (exact terminal debt row)

For every serialized legal sequence,

```text
mu_(F_q) = mu_(F_0)+sum_j Delta_j.                   (1.3)
```

If `F_0` covers every palette colour, then

```text
h(F_q) <= ||(sum_j Delta_j)_-||_1,                  (1.4)
```

and the same inequality holds separately on every `P_a`.  If
`mu_(F_0)=1` pointwise, as in an exact named-target deck, then (1.4) is an
equality.  If each move preserves the total number of palette occurrences,
the missing and excess masses of an initially exact deck are equal.

#### Proof

Equation (1.3) telescopes definition (1.2).  Since `mu_(F_0)(p)>=1`, a final
zero at `p` requires

```text
sum_j Delta_j(p) <= -1.
```

Summing the negative parts proves (1.4).  When every initial load is one,
the final deficit vector is exactly `(-sum_j Delta_j)_+`.  Conservation of
total load equates its positive and negative masses.  QED.

Equivalently, terminal debt at most `H` is the exact linear slack condition

```text
mu_(F_0)(p)+sum_j Delta_j(p)+b_p >= 1  for every p,
b_p>=0,  sum_p b_p<=H.                               (1.5)
```

For an integral terminal factor the minimum of `sum b_p` in (1.5) is (1.1).

## 2. Component-coboundary fusion

A circuit move is called **serial-safe** for the present statement when all
of the following are checked in the current state:

1. every deleted incidence is still selected and every added incidence is
   live;
2. matching degrees, one-copy owner constraints, pins, and declared resource
   capacities remain valid;
3. the move replaces declared current components
   `C_1,...,C_s`, `s>=2`, by one component `E`, creates no undeclared split,
   and leaves all other components unchanged;
4. its palette payload is recomputed literally as in (1.2).

Conditions concerning residence, upper shadows, or a compiler may be added
as hard guards, but they are not implied by this definition.

### Theorem 2.1 (bounded-root merge-tree lemma)

Assume `F_0` covers every protected palette colour, and let `L` be its set
of components.  Suppose a serial-safe sequence builds a merge forest from
those leaves.  Assign every component state that
appears a signed palette vector `pi(C) in Z^P`.  For move `j`, which replaces
the current child components `A_j` by `E_j`, assume the exact statewise row

```text
Delta_j = pi(E_j)-sum_(C in A_j) pi(C)+epsilon_j.    (2.1)
```

If `R` is the set of terminal roots, then

```text
sum_j Delta_j
 = sum_(E in R) pi(E)-sum_(C in L) pi(C)+sum_j epsilon_j.   (2.2)
```

Consequently, writing

```text
B = sum_(E in R) pi(E)-sum_(C in L) pi(C),
Eps = sum_j epsilon_j,
```

one has the exact protected-palette bound

```text
h(F_q) <= ||(B+Eps)_-||_1
        <= ||B_-||_1+||Eps_-||_1.                  (2.3)
```

The statement is componentwise in the palettes `P_a`.  In particular, if
the sequence has one root, `||B_-||_1<=rho`, and at most `b` moves have
nonzero error with `||(epsilon_j)_-||_1<=beta`, then

```text
h(F_q) <= rho+b beta.                               (2.4)
```

Thus `rho,b,beta=O(1)` gives bounded terminal debt even when the number of
initial components and the number of exact merge moves grow.

#### Proof

Sum (2.1) over the merge forest.  Every nonleaf, nonroot component appears
once with coefficient `+1`, when it is created, and once with coefficient
`-1`, when it is consumed.  Those terms cancel.  The leaves appear only
negatively and the roots only positively, proving (2.2).  Apply Lemma 1.1
and subadditivity of the negative part to obtain (2.3)--(2.4).  QED.

The theorem also handles one long circuit that merges several components:
such a move decreases the component count by `|A_j|-1`.  The output is
connected precisely when the merge forest has one root.  No assumption that
exactly `|L|-1` circuits are used is needed.

### Corollary 2.2 (bounded-debt connected NRFC reduction)

Assume a literal occurrence-labelled NRFC factor has already been built,
including one-copy owners, the age-cell recurrence, and an exact named
nested-target deck, but its successor permutation has several components.
If a guarded incidence-circuit catalogue contains a serial-safe one-root
merge forest satisfying (2.1) and (2.4), and every changed transition is
replayed against the literal age cells, then the output is a connected
owner-simple factor with at most `rho+b beta` missing named targets.

This is a reduction, not an NRFC existence theorem.  The hypothesis must
include the literal recurrence

```text
C_(tau(u),i+1)=C_(u,i)-B_(tau(u))
```

on every changed transition.  Matching or rank counts alone do not supply
it.  Upper/deep witnesses, residence, and common-cap compatibility remain
separate unless included among the guarded resources.

## 3. Chronological compatible-port version

Sometimes a component potential is too strong, but the connectors have a
literal input/output port state.  Let `S` be the port-state set and
`phi:S->Z^P`.  Suppose

```text
Delta_j = phi(t_j)-phi(s_j)+epsilon_j.              (3.1)
```

Partition the selected chronological sequence into `K` maximal compatible
chains, where consecutive circuits in one chain obey `t_j=s_(j+1)`.

### Theorem 3.1 (bounded-chain endpoint lemma)

Put

```text
rho = max_(x,y in S) ||(phi(y)-phi(x))_-||_1.
```

Also put

```text
d(v)=#{j:t_j=v}-#{j:s_j=v},
Div=sum_(v in S)|d(v)|.
```

Then

```text
h(F_q) <= K rho+||(sum_j epsilon_j)_-||_1.          (3.2)
```

More generally, if `||phi(v)||_1<=P`, then

```text
h(F_q) <= P Div+||(sum_j epsilon_j)_-||_1.          (3.3)
```

Every closed compatible chain contributes zero boundary term.  If merely
`||phi(s)||_1<=P`, there are at most `J` incompatible consecutive seams,
and at most `b` errors of `l_1` norm at most `beta`, then `K<=J+1` and

```text
h(F_q) <= 2(J+1)P+b beta.                           (3.4)
```

#### Proof

Inside each compatible chain, all intermediate `phi` terms in (3.1)
cancel.  Only one end-minus-start vector remains.  This proves (3.2).
Without choosing a chain decomposition, the complete potential boundary is

```text
sum_(v in S) d(v)phi(v),
```

whose `l_1` norm is at most `P Div`; this proves (3.3).  Finally
`Div<=2K<=2(J+1)` for the maximal-chain decomposition, and the residual
triangle inequality proves (3.4).  QED.

Thus endpoint coboundaries give bounded debt only with bounded boundary
divergence: a bounded number of compatible chains, closed chains, or an
equivalent cancellation certificate.  This is weaker than Theorem 2.1 on a
branching merge tree.

### Proposition 3.2 (exact port-potential audit)

On a fixed directed port multigraph with edge labels `Delta_e in Z^P`, an
exact representation

```text
Delta_e=phi(head(e))-phi(tail(e))                    (3.5)
```

exists on each weak component if and only if the signed sum of the labels
around every undirected closed walk is zero, using `-Delta_e` when an edge is
traversed backwards.

#### Proof

Necessity is telescoping.  For sufficiency, fix a root, define `phi(v)` as
the signed label sum along any root-to-`v` walk, and use the closed-walk
condition to prove path independence.  QED.

Thus a proposed zero-error port catalogue has a finite exact circuit audit.
Allowing `O(1)` exceptional payloads means deleting or charging an explicit
`O(1)` residual edge set before applying this test; bounded error on every
edge is not enough.

## 4. Sharp obstruction to per-circuit reasoning

### Proposition 4.1 (unit local debt can accumulate linearly)

For every `c>=2` there is an abstract serial-safe spanning merge tree on
`c` components and an initially exact palette such that every merge has
negative payload mass one, while the connected terminal factor has `c-1`
missing colours.

#### Construction

Take palette

```text
P={q,t_1,...,t_(c-1)}
```

with initial load one on every colour.  Use a star of component merges, one
resource-private merge for each leaf, with payload

```text
Delta_i = 1_q-1_(t_i).                              (4.1)
```

Every move preserves total load and has one negative ticket.  After all
`c-1` merges the factor is connected, `q` has load `c`, and every `t_i` is
missing.  Hence the terminal debt is `c-1`.

This example even has a bounded endpoint-potential representation.  Orient
each star edge from leaf `i` to the centre, put

```text
phi(centre)=0,  phi(leaf_i)=1_(t_i)-1_q,
```

and, explicitly,

```text
Delta_i=phi(head)-phi(tail)
       =phi(centre)-phi(leaf_i)=1_q-1_(t_i).
```

The failure is that the chronological
sequence has `c-1` incompatible one-edge chains.  Equivalently, its boundary
divergence is unbounded.  The merge-tree row (2.1) can represent the example
only with a root-minus-leaf boundary whose negative mass is `c-1`, so
Theorem 2.1 detects rather than hides the obstruction.  QED.

Therefore none of the following implies bounded terminal debt:

* every incidence circuit has `O(1)` support;
* every circuit individually loses at most `O(1)` colours;
* the selected circuits are resource-disjoint;
* their component edges form a spanning tree;
* every payload is an endpoint coboundary with bounded endpoint vectors.

One additionally needs the component cocycle of Theorem 2.1, only `O(1)`
compatible chronological chains as in Theorem 3.1, or another explicit
bounded-cancellation invariant.

### Proposition 4.2 (zero standalone debt is not compositional)

For every `m>=3` there is an abstract transition system satisfying the
serial-safe topology/resource axioms, with `m` resource-private merges, such that
each merge, when tested alone against the common baseline, leaves every
palette colour covered, but applying all `m` merges leaves `m` holes.

#### Construction

Give each target `t_i`, indices modulo `m`, two distinct baseline provider
occurrences, and give a reservoir colour `q` one provider.  Move `e_i`
deletes one provider of each of `t_i,t_(i+1)` and creates two additional
occurrences of `q`:

```text
Delta_i=2 1_q-1_(t_i)-1_(t_(i+1)).                  (4.2)
```

Choose all deleted provider occurrences and all incidence resources
distinct, take `m+1` initial components, and let the moves be the `m` edges
of any fixed spanning tree.  One move
leaves the two affected targets at load one, so its standalone coverage debt
is zero.  Across all moves, each `t_i` loses both providers and is absent;
the terminal debt is `m`.  Total palette-occurrence mass is conserved in
every move.  QED.

This is why “palette-safe C6” is not itself a compositional label.  Its full
signed load change and the identities of its surviving providers must be
retained, unless disjoint affected-colour closures or a context-independent
cocycle has been proved.  Proposition 4.2 is a logical counterexample to an
inference from standalone coverage tests; it does not claim that this exact
load pattern is a Boolean incidence-circuit family.

## 5. Exact finite `k=17` calibration

The frozen complement-dual seed has SHA

```text
a3f9eac037ae66a460349b12d578a31222afe1a7d168da641e77967a44ddbab3.
```

Its selected matchings have two physical factor components and complete
immediate rank-10/rank-7 quotient-q1 palettes.  The following statements are
literal replay results.

### 5.1 Incidence `C6`: zero debt, zero fusion

The strict-dual three-row assignment circuit uses owners

```text
75,265,219
```

and changes incidences

```text
681->678, 2385->2391, 1975->1971.
```

Both immediate palettes remain complete, with common load histogram

```text
1^878 2^247 3^18 4^1.
```

But the factor still has physical components of sizes `24293` and `17`.
This is a palette-complete, nonzero-signed-payload residence-improving
rethread, not a connector.

Frozen sources:

* `scratch/threadA_k17_complement_dual_age_local_repair_20260801/`
  `best_age_improving_dswitch.tsv`, SHA
  `bff9739f830fff21ab48201d4193f5b1eb805da9b2553caa914a4b83d25661d8`;
* `scratch/threadA_k17_complement_dual_age_local_replay_20260801/`
  `switch75_265_219.audit.json`, SHA
  `7e180f3b5c1a5a13206916f98ce9f727d0d1085b2ece62a49aaf54f768ea4ec5`;
* `MATH_THEOREM_A_K17_COMPLEMENT_DUAL_AGE_LOCAL_DSWITCH_CATALOGUE_20260801.md`,
  SHA `c36aee8ff5a6bd4a42dd458841a0f88408eb55b55f5e166c8a9eb2f257eb20af`.

### 5.2 Incidence `C12`: auxiliary Hamiltonicity, two palette holes

The strict-dual length-six assignment circuit, candidate `72`, makes `A`
one quotient `1430`-cycle of voltage `15`.  Its physical factor is still
the square `A^2`: two quotient `715`-cycles, each of voltage `15`, lifting
to two physical `12155`-cycles.  The exact immediate debts are

```text
rank 10: {0x03e4f},
rank  7: {0x00d87}.                                  (5.1)
```

Thus “one q1 hole” here means one missing quotient orbit on each shore, not
one total hole and not a connected physical factor.

### 5.3 Incidence `C16`: physical fusion with debt two

The non-dual length-eight `H` assignment circuit, candidate `1911`, keeps
`D,H` edge-disjoint perfect matchings.  Their union is one quotient
`1430`-cycle of voltage `9`, hence one physical `24310`-cycle.  Rank-10 q1
is complete.  Rank-7 q1 has exactly

```text
{0x00e0f,0x01547}.                                  (5.2)
```

This is a literal finite instance of connected fusion with terminal debt
`H=2`.

The independent TSV-only replay is

```text
scratch/k17_dual_splice_dev5_independent_20260801/
  independent_replay.audit.json
SHA 3edce35e7429b89255029b4a3c0fbc7bf78a6f24b4261cc20ebf50884152a437.
```

It reconstructs the `Z17` incidence atlas, all selected incidences in all
17 phases, both matching degrees, quotient and physical topology, voltages,
and immediate q1 loads.  The bound factor files have SHAs

```text
C12 f1d21146512662a54ad0c3811b8a4c901e738c6e3e7c2f42e835017c662134c0,
C16 c082621d6444dc2283675882557d0240babb989f2d31847eb198fbe8b4612587.
```

The finite rows are alternative single-circuit outputs from one seed, not
a serialized `C6+C12+C16` packet.  The exact catalogue scope is assignment
cycles through the singleton up to bipartite length `16`.  It does not
certify q2, deeper shadows, C12/C16 residence, common cap, compiler
feasibility, or an all-`k` cocycle.

## 6. The exact remaining all-parameter connector theorem

The useful weakened NRFC target is now precise.

1. Build a literal exact named-owner/nested-flag factor, possibly with many
   components.
2. Prospectively select a guarded incidence-circuit merge forest.
3. Prove either the component-potential law (2.1) with bounded root boundary,
   or a chronological realization with only `O(1)` unmatched port chains.
4. Keep only `O(1)` exceptional palette errors, or prove their signed sum is
   bounded.
5. Repair the resulting `O(1)` named-target debt with a source-private
   absorber.

Steps 2--4 are the **bounded-debt circuit-fusion gate**.  They are strictly
weaker than demanding every circuit be palette-transparent, but stronger
than a spanning circuit tree with bounded local support.  The finite C16
row proves that this relaxation is nonvacuous.  It does not yet provide the
all-parameter circuit catalogue or its root potential.

There is a prior topology cut which no payload identity can repair.  The
merge hypergraph must be connected on the **actual** current components,
including any tight age-word fibres.  If a fibre has no outgoing live
circuit, as in the buffered all-two fixed-decomposition obstruction, then no
merge tree exists and Theorems 2.1 and 3.1 are inapplicable.  Bounded debt is
a conclusion after literal component-spanning supply, not a substitute for
that supply.
