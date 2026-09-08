# K17 protected LLR release--compensation descent

**Date:** 2026-08-02  
**Status:** exact graph-theoretic descent lemma plus an authenticated K17
strict-Pareto witness; not a chronology, compiler, K17 word, or proof that the
descent reaches deficiency zero.

## Result

The protected `b268` LLR lane has a solver-free one-for-one exchange that
strictly improves both the complete supplier rank and the measured socket
tuple.  From the strict-Pareto deficiency-85 table

```text
selected  0fb9a812e0afd7e9590d6ba690d2c3d7bee3f15a9462e3236b784a17de48b59f
table     ea0e8803b666dd51e4e5b073e50938ca5c508f3c2d7066f04ec2a0bd9f083aa8
sockets   (p0,p1,both,either) = (3102,2259,1843,3518)
supplier  16813/16898, deficiency 85
```

remove protected transfer `32175` and add protected transfer `36629`.  The
four changed rows are respectively

```text
remove 32175  (left,right) = (12586,24210)
add    36629  (left,right) = (13716,13720).
```

The exact materialization has

```text
selected  c490cc49aef575caae9f72d478ff08320f24a3625593f2465f9b94fb7d8ce979
table     3171bf380c3a139313f1304bb1d821810cb7402c20aa99f01ab8ccdc189854f1
sockets   (p0,p1,both,either) = (3102,2260,1844,3518)
supplier  16814/16898, deficiency 84
zero      71
DM shore  98/14
```

Thus `p0` and `either` are preserved, `p1`, `both`, and supplier rank each
increase by one, and all `7,213` authenticated private-ticket rows remain
literal.  This replaces the inferior generic deficiency-84 result whose two
phase socket counts regressed.

The exact H100 freeze is

```text
/home/amodo/or15/work/root_k17_b268_llr_release_oracle_20260802/
  def84_pareto_remove32175_add36629/
```

and the repository package is

```text
scratch/q1_k17_b268_llr_release_theorem_20260802/
```

## Release--compensation lemma

Let `G(T)` be the complete supplier--hard-head bipartite graph of a legal
lower table `T`, and let `M` be a maximum matching.  Let `e=(A,D)` be a
selected LLR transfer and let `T-e` denote the table obtained by restoring its
two source rows.  Let `f=(A',D')` be an unselected protected transfer on two
rows disjoint from every transfer retained after removing `e`.

Assume:

1. undoing `e` makes an isolated hard head `h` adjacent to `A` or `D`;
2. in `G(T-e)` that new incidence begins an `M`-alternating path ending at an
   unmatched supplier, and all matched incidences outside the path survive;
3. the path does not use the other row changed by `e` in an incompatible
   state;
4. adding `f` is matching-transparent for the augmented matching: the old
   right head removed by `f` can be replaced by its new left head (or both are
   unmatched), the matched supplier incidences on `A',D'` survive, and no
   supplier or head collision is introduced.

Then the one-for-one table

```text
T' = T - e + f
```

has a supplier matching of size at least `|M|+1`.  If an exact maximum
matching replay returns `|M|+1`, the supplier deficiency falls by exactly one.

### Proof

By assumptions 1--3, prepend the new edge `h--A` (or `h--D`) to the certified
alternating path and flip every edge along it.  This augments `M`, producing a
matching `M+` of size `|M|+1` in `G(T-e)`.  Assumption 4 transports `M+`
through the compensating addition without losing cardinality.  Hence

```text
matching_rank(G(T')) >= |M|+1.
```

An exact maximum-matching replay certifies equality in the finite instance.
Row disjointness and the transfer identities preserve the complete target
partition and transfer count.  If all four rows avoid the protected ticket
union, those rows remain literal.  This proves the claim.  ∎

## Exact K17 actuator

At the strict-Pareto deficiency-85 checkpoint, undoing edge `32175` has the
following independently replayed geometry:

```text
activated isolated head        12592
creating supplier              12586
alternating escape length      0 (already free)
DM incidence delta             +2
DM heads gaining/losing        2 / 0
restored right-head degree     6
```

The compensating edge `36629` is row-disjoint and common-positive in both
measured phases.  Before the swap its new hard head has three suppliers, all
outside the old DM neighbor shore, and it has zero incidence delta on the old
DM shore.  Full materialization and maximum-matching replay, rather than
those local prices alone, certify the displayed deficiency-84 table.

The same release actuator was still present after the unrelated root descent
from deficiency 92 through deficiency 85.  At deficiency 92 it also gives a
valid solver-free deficiency-91 table.  The generic exact solver independently
found a different swap, `1792 -> 88113`, with the same supplier improvement.
Therefore the improving move is not unique.

## Iterative conditional corollary

Suppose a sequence of legal protected tables has positive supplier deficiency
and, at every stage, contains a release edge and a compensating edge satisfying
the four hypotheses above, with the complete socket/protection rows required
by the application.  Iterating the lemma decreases deficiency by one per
stage.  If the condition persists through every positive deficiency, the
supplier projection reaches deficiency zero.

The current evidence is finite only.  Exact one-for-one searches produced a
supplier chain through deficiency 84, and the release oracle finds six safe
release candidates at the strict-Pareto deficiency-85 checkpoint.  This does
not prove that a release--compensation pair exists after every recomputed DM
shore, nor that the exterior socket, phase coupling, or chronology gates can
be preserved to deficiency zero.

## Scope

The theorem concerns one exact static lower-table projection.  Phase 0 is
literal on `b268`; phase 1 is still only a root-aligned transported owner
marginal.  Residual outer rematching, a common occurrence-labelled state,
opening transport, chronology, residence, arbitrary upper shadows, common
cap, compiler, and a universal K17 word remain unproved.

Key hashes:

```text
b268 literal parent             b268d1248e53d164d87bc83cf69fbd5ebd412451ac9e4a4313408167f1e637dc
protected edge catalogue        30fac2b299c353446024a83fb93525d66e6b6720eacbd1895db68c5544598c89
result projection audit         7f2dc7ae146ae6a706a2399326b293809f7ae62d34a89ac393a2301a357dab05
native phase-0 DNF              031b5b48d62306c140fa666544c7c2f6e1b8bc1a0201f8c46f4cb87ed0e529d8
transported phase-1 DNF         465e3a99d62c104227a7986dba62c30b33c916f121faeeaef1fea5688af58ed8
```
