# K16 ghost-conditioned deadline rematching for the Lane L DM exits

Date: 2026-07-31  
Status: **PASS scoped antecedent gate; PASS focused total-two no-go.**  
No unrestricted K16 lower bound and no no-go for two additional edits is
claimed.

## 1. Exact lineage statement

The two authenticated length-12,873 one-hole words are

```text
scratch/k16_upper12874_best_delete.word
  SHA a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649
scratch/k16_vv_th495_deletep1_onehole_20260731.word
  SHA e4a7ad4ed3041fd8e1fa7e6c1805a2315a2cf5dc811f5897e7b3a29e7c348676.
```

In both, the intervals

```text
[11726,11728] and [12826,12828]
```

first-deliver `0xc279` at distinct deadlines.  Therefore any **cumulative
physical transformation** which changes no cell in either triple retains two
first-middle deliveries of `0xc279`, has ghost extra `G>=1`, and cannot be a
universal equality word, because

\[
 26332\le (3-G)(12873+G)
\]

already fails at `G=1`.

This is a theorem about transformations from those two antecedents.  It is
not a theorem that the last incremental move of every construction must touch
one of the historical triples.  In particular, the authenticated
pass33/35/46/55 Hall carriers are a distinct, already ghost-free lineage.
The independently reconstructed pass33 word has `G=0`, no middle hole, and
literal providers

```text
2c6d at [3783,3786],   c679 at [12826,12829].
```

Ghost accounting must therefore be attached to the cumulative lineage, not
blindly to the final DM-exit delta.

## 2. Six unrestricted escape sites, five unique-bit sites

The exact incumbent unique contributions to `0xc279` are:

| fibre | position | unique mask |
|---|---:|---:|
| both | 11726 | `0010` |
| both | 11727 | `4000` |
| delete-p1 | 11728 | `0268` |
| V/V | 11728 | `0008` |
| both | 12826 | `0040` |
| both | 12827 | `0000` |
| both | 12828 | `0008` |

Thus the nonzero unique-bit set is

```text
{11726,11727,11728,12826,12828}.
```

That five-site set is a complete gate only for target-contained edits which
do not preempt the old deadline.  It is not an unrestricted substitution
gate: although `12827` contributes no unique incumbent bit, a replacement
there containing a bit outside `0xc279` can still make the old delivery jump.
For arbitrary macros the exact safe gate is full first-outcome replay on all
six positions, or the sufficient antecedent obstruction that the support is
disjoint from both entire triples.

Lane L's complete support-at-most-six deck is

```text
6603..6611 union 12710..12722.
```

Its intersection with all six ghost positions is empty.  Consequently all
84,001,148 formal occurrence permutations in that four-carrier census would
leave the inherited ghost untouched if applied with the same positional
support to either fixed one-hole antecedent.  This coordinate fact does not
reject the actual Hall carriers, which are already `G=0`.

## 3. Exact released-deadline test

For a physical word `X`, form the sparse bipartite graph `D(X)` whose left
vertices are the 12,870 rank-eight masks and whose right vertices are
physical deadlines.  Put `T--d` when some start first reaches rank eight at
deadline `d` with OR exactly `T`.  Every rank-eight interval is represented:
once a start has reached rank eight, extending it cannot change to another
rank-eight label.

The exact unfrozen test that a released deadline can host `H=0x2c6d` is

\[
 \mu_H(D)=1+\max_{d\in N(H)}
       \nu\bigl(D-\{H,d\}\bigr).                       \tag{3.1}
\]

It succeeds at equality only if `mu_H(D)=12870`, together with literal full
coverage and the required first-delivery inventory.  Merely finding one new
`H` interval is not enough.  Equation (3.1) is recomputed by a fresh full
Hopcroft--Karp matching; no incumbent mate is frozen.

This deadline graph is separate from the 26,332-target lower compatibility
graph used in the Hall-24 DM calculation.  Both `0x2c6d` and `0xc279` have
rank eight and are not lower-graph vertices.  For genuinely lower provider
requirements `Q`, the corresponding unfrozen forced-residual test is

\[
 \mu_Q(G)=\max_f\left(|Q|+
 \nu(G-Q-f(Q))\right),                                 \tag{3.2}
\]

where the maximum is over injective choices of an available cell for every
required target.  The Lane L specialization forcing `4e70--J` and
`8000--J31761` is

\[
 2+\nu\left(G-\{4e70,8000\}-\{J,J31761\}\right)\ge26309.
\]

The literal/deadline test (3.1) and lower rematch (3.2) are separate mandatory
conjuncts; neither can be substituted for the other.

## 4. Focused `p12826` total-two branch

At `p12826`, exactly sixteen normalized values collapse the inherited
`0xc279` ghost while preserving every other middle label.  In either fibre,
every such one-edit word has literal holes

```text
{2c6d,c679}
```

and deadline matching rank 12,869.  There is no `2c6d` edge, so (3.1) is
zero at this stage.

With only one further substitution available, two disjoint one-target sites
are impossible: the remaining site must be a same-site common provider for
both holes.  The exact common-provider intersection contains eight
assignments, all at `p6437`:

```text
0408 0409 0428 0429 0448 0449 0468 0469.
```

Their two unique new witnesses are distinct intervals sharing that edited
cell:

```text
2c6d at [6437,6439],   c679 at [6434,6437].
```

All `16*8=128` macros were fully replayed in each fibre.  Every one loses

```text
2879 287d a879 a87d c879 e879.
```

The rank-eight losses are `287d,a879,c879`.  A fresh whole deadline matching
has rank 12,867 even when the new `2c6d--6439` edge is forced.  It also has
two duplicate labels,

```text
c479 at deadlines 6437,9720;
ac69 at deadlines 6438,10926.
```

Thus the focused total-two branch is exactly negative.  Its failure is not a
frozen-mate artefact: `2c6d` is successfully rematched, but three other
rank-eight targets and two new deadline injections fail.

## 5. What the wider two-edit catalogues do and do not prove

The complete total-two substitution balls around the original one-hole words
are already negative under the standard exact dichotomy:

| fibre | sequential first providers | exact second work | joint supports | joint value pairs |
|---|---:|---:|---:|---:|
| delete-p1 | 27,064 | 646,720 assignments | 13,235 | 102,404,745 |
| V/V | 26,438 | 247,044 candidate sites | 13,177 | 100,771,016 |

The sequential branch orients an edit which alone supplies the original
hole; the genuinely joint branch covers a final hole witness containing both
edited sites.  Both use exact private-target/literal replay and contain no
completion.

These catalogues include `p12826` plus one more edit.  They do **not by
themselves** decide `p12826` followed by two additional edits.  The published structural counts
`144` and `77,202` are only Cartesian support products (`6*24` and
`6*(12873-6)`); they are not value-level pair censuses, matching results, or
no-go theorems.  The distributed two-additional-provider branch and the
19-cell CNFs are outside this note's finite replay.

## 6. Existing support-at-most-three ghost surgery

For the delete-p1/collar594 primary word, the six-position surgery audit
exhausts all

```text
C(6,1)+C(6,2)+C(6,3)=41
```

supports through the target-intersection closure normalization.  None has a
ghost-free complete middle solution.  Its one-cell layer also directly
replays all `6*65534=393204` nontrivial substitutions.  This is complete only
for supports contained in the two displayed triples of that primary word; the
V/V support-at-most-three table was not independently enumerated.  It does not
exclude a ghost cell interacting with remote provider cells.

## 7. Frozen artifacts

Primary focused rematch:

```text
scratch/audit_laneL_k16_ghost_conditioned_deadline_rematch_20260731.py
  SHA e296d9a1ea0085cb3f8ff649d21aed0b8290392794d95e39a6dd252d21c29c49
scratch/laneL_k16_ghost_conditioned_deadline_rematch_20260731.audit.json
  SHA 13768799f4d9199576e8bdb64e3b641084eb93e885d16d39a22f64458262a7c1
  payload eb6e71362a93040a04a0de04fd423ad757ddb0d03b94b1eb2f057e00de818a18
```

Independent lineage/forced-residual audit:

```text
scratch/audit_k16_c279_dm_lineage_acceptance_20260731.py
  SHA 53e758636583b223c77bd52cc4717d16cd03eee068f157698ca4f42376967128
scratch/k16_c279_dm_lineage_acceptance_20260731.audit.json
  SHA 2d598cdcd38feb8ee0c6b646becce1d2b78bee1e740e5d056a8e710d35ec9930
  payload f86b3642138256c1220d4dd6c7ff4a8e4cf52484f48ba4864bb480c8107d2b93
```

The primary run is a light deterministic replay (about nine seconds locally)
and uses no H100, SAT solver, or frozen matching.

## 8. Scope boundary

The antecedent theorem is exact for the two named one-hole words and any
cumulative macro disjoint from both fixed triples.  The focused finite no-go
is exact for the sixteen `p12826` values followed by one arbitrary common
provider cell.  It does not cover two additional cells after `p12826`, a
different one-hole word, support seven or larger in the Hall-24 closure, or a
physical embedding between the one-hole fibres and the distinct exact229
Hall carriers.
