# K16 period-three subgroup branch audit

Date: 2026-07-30

This note independently checks the finite subgroup split used by the
source-independent one-block two-rail K16 carrier model.  It is scoped to the
exact quotient model with binary rail order, one `A` block, one `B` block,
and the two installed lower rows

```text
q2: 37449 = {top} union H,
q3:  4681 = H,
H = 3 Z_15 = {0,3,6,9,12}.
```

It uses no source carrier, edit radius, seam repair assumption, or solver
outcome.

## 1. The q2 cluster

Fix the physical target `H union {top}`.  Every state in a three-state q2
provider is on shore `A`.  After removing the target, its three states are
two-subsets of the ten-point complement `C=Z_15\H`.  A simple Johnson path
with empty three-way intersection has the unique form

```text
P0={a,u},  P1={a,v},  P2={v,w}.
```

Consequently the number before quotient-node distinctness is

```text
binom(10,2) * 2 * 8 * 8 = 5760.
```

The stabilizer of `H` is the five-element rotation subgroup `3 Z_15`.
Its action on two-subsets of `C` is free, since a nonempty invariant subset
of an orbit of order five cannot have size two.  The exact finite pair-orbit
enumeration in
`scratch/audit_k16_subgroup_shadow_geometry_20260730.py` removes 1160 paths
whose quotient nodes repeat:

```text
repeat 02 only  560
repeat 12 only  280
repeat 01 only  280
repeat all       40
```

Thus `4600/5=920` quotient provider paths remain.  There are
`binom(10,2)/5=9` exceptional A-necklace nodes containing a rotation of `H`.
Every provider visits three of these nodes, and every option increment is
zero modulo three.  Its middle node is therefore exactly one of

```text
378, 380, 381, 383, 384, 395, 396, 405, 406.
```

These nine middle classes partition the **q2 provider witnesses**.  Four
classes have 80 witnesses and five have 120.

## 2. The q3 shore patterns

Every state in a four-state provider for `H` contains `H`.  An A state adds
`top` and two points of `C`; a B state adds three points of `C`.  The same
free stabilizer argument gives nine exceptional A nodes and
`binom(10,3)/5=24` exceptional B nodes.  All three option increments in a
provider are zero modulo three.

Binary rail order makes each shore one path of length 429 and supplies only
the two end seams.  A path of three options cannot traverse both blocks, so
its four-letter shore word changes shore at most once.  `AAAA` is impossible:
four A states have `top` in their intersection, whereas the target `H` does
not.  Hence the seven possible patterns are exactly

```text
AAAB, AABB, ABBB, BAAA, BBAA, BBBA, BBBB.
```

The exact provider counts are respectively

```text
7360, 7504, 6640, 7360, 7504, 6640, 42720,
```

which sum to 85728.  The remaining 2736 paths in the unrestricted 88464-path
catalogue have two or more shore changes and are false under binary rail
order.  Thus the seven classes partition the **q3 provider witnesses**.

There are two endpoint couplings.  For an `AAAB` provider, the intersection of
the first three A states contains `H union {top}`.  It contains no further old
coordinate: such a coordinate lies in the third A state and survives the
following A-to-B transition, contradicting that the four-state intersection
is exactly `H`.  Therefore its first two options form a q2 provider, with the
same middle node.

By the reverse argument, in a `BAAA` provider the last three A states also
intersect in exactly `H union {top}`: every old coordinate in the first A
state was already present in the preceding B state.  Thus its last two
options form a q2 provider.  The current branch generator exploits only the
AAAB prefix coupling because its q3 Tseitin factorization is keyed by the
first two options.  Filtering BAAA by the middle of its q2 **suffix** is an
additional exact strengthening available to a future generator; it is not
needed for completeness of the frozen portfolio.

## 3. Factored-row size check

The frozen unbranched preinstallation ledger is arithmetically exact.  The
q2 DNF has 920 two-option conjunctions, hence 920 auxiliaries and
`3*920+1=2761` clauses.  The q3 row has 85728 paths grouped into 11720
two-option prefixes.  Of those prefixes, 920 are the already installed q2
providers, leaving 10800 new prefix variables and 11720 q3 witness variables:

```text
q3 new variables = 10800 + 11720 = 22520,
all new provider variables = 920 + 22520 = 23440.
```

New-prefix equivalences cost `3*10800=32400` clauses.  The factored q3
witnesses cost `2*11720+85728`, and the row OR costs one, giving

```text
32400 + 2*11720 + 85728 + 1 = 141569 q3 clauses.
```

Together with q2 this is 144330 provider clauses.  The nine redundant cluster
witnesses add 9 variables and 19 clauses, reproducing exactly 344200 total
variables and 3925421 total clauses from the audited **unbranched positive-row**
formula.  The later compact disjoint AAAB encoding is smaller and is recorded
in `THREAD_D_K16_AAAB_TERMINAL_POSITION_AND_Q1_HALL_AUDIT_20260730.md`.

## 4. Exact 63-case coverage and the disjointness correction

For selected-option literals `x_e`, define the exact path sets

```text
P_m = {(e0,e1) in P2 : target(e0)=(A,m)},
Q_p = {(e0,e1,e2) in P3 : shoreword(e0,e1,e2)=p}.
```

Then `E_m` is the DNF

```text
OR_(path in P_m) AND_(e in path) x_e,
```

and `Q_p` is defined analogously.  The implemented non-AAAB branch installs
the two exact rows `E_m` and `Q_p`.  In an AAAB branch it replaces `Q_AAAB`
by the subrow with `target(e0)=(A,m)`; the prefix lemma proves that this is
still complete.  The extra fixed-middle cluster clauses merely expose the
implied exceptional incoming/outgoing options to unit propagation.  They do
not replace either exact provider DNF, and they fix a quotient-node identity,
not an absolute binary rail position.

Every carrier satisfying both installed rows belongs to at least one of the
`9*7=63` branches:

* for a non-AAAB q3 witness, choose its pattern and any q2-witness middle;
* for an AAAB q3 witness, choose the middle of its own q2 prefix.

This proves **exhaustiveness** of the portfolio.  The original positive-only
63 SAT formulas are not, in general, disjoint as sets of carriers: a carrier can contain q2
providers at several exceptional middles or q3 providers of several shore
patterns.  What is disjoint is the classification of an already distinguished
provider witness.  If a formally disjoint case partition is needed, order the
63 predicates `B_1,...,B_63` and replace them by

```text
D_i = B_i and not B_1 and ... and not B_(i-1).
```

or introduce an exactly-one distinguished-witness selector.  The executable
portfolio now implements the former canonical first-witness tie-break; see
`THREAD_D_K16_Q23_DISJOINT_AAAB_PORTFOLIO_20260730.md`.  The overlap statement
here remains the audit of the superseded positive-only formulas.

## 5. Why AAAB is the smallest family

After fixing the AAAB middle, only 640 paths remain in an 80-prefix class and
960 in a 120-prefix class.  They are eight third-edge extensions of each q2
prefix.  The factored CNF reuses each q2 prefix variable and needs one q3
witness per prefix, not one variable per three-edge path.  Including the
single fixed-middle propagation witness, the nine AAAB branches add only

```text
161 or 241 variables; 1045 or 1565 clauses.
```

Every other pattern adds at least 2065 variables and 11845 clauses; the exact
ranges in the frozen portfolio ledger agree with these inequalities.  Thus
AAAB-first is justified by exact encoded size of the **current prefix-factored
portfolio**, not merely raw path count.  It is not an intrinsic asymmetry of
the shadow geometry: BAAA has the suffix coupling proved above, which the
current encoder leaves unused.

## 6. Scope and caveats

1. The 63-case theorem depends essentially on binary rail order.  Without it,
   the audited catalogue also contains `AABA`, `ABAA`, and `ABBA` providers,
   so the seven-pattern split is incomplete.
2. The node indices are necklace indices in the fixed quotient gauge.  The
   canonical target labels already represent all physical rotations; no
   physical copy of the subgroup is lost by fixing `H`.
3. Reversal exchanges some shore patterns, but residence/history orientation
   need not respect that involution.  The seven patterns must not be quotient
   identified without a separate proof.
4. These two rows cover only the singular subgroup q2/q3 target orbits.  A
   SAT branch must still enter the complete deep CEGAR, physical replay,
   COMP3, and literal 65535-mask verifier.

Frozen evidence:

```text
scratch/k16_subgroup_shadow_geometry_20260730.audit.json
  d4887f9bdd15a479c965448ad208d250d87279be9891d30c6cdf92b2c5ac1f4a
scratch/k16_joint_q23_preinstall_size_20260730.audit.json
  7b585784ac2cde11d8dc40f1c67041b0ae14ccb123e49fa93a5c81fdd3a4c024
scratch/k16_subgroup_cluster_portfolio_20260730.audit.json
  d763a3dcb059a6f573aae6e55b568c703a5ac92dabb58079d8671b5cc427f71d
```
