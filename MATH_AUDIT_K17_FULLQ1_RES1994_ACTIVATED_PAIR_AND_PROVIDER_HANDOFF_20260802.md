# K17 full-q1 residence-1994 activated pair and provider-handoff audit

## 1. Canonical frozen root

The present canonical checkpoint is

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
    checkpoint_fullq1_escape_res1994/model
```

with bindings

```text
model                 127f97f02d238215367a1d5291853e0dd7ecb6d2d227cfcfed1c365e68d5ebcd
passive audit         9673e703985640504c41b95953cc96134be2a481639312ca59f553deaaab2343
independent audit     6bae984f36d2d72ca65af39e2e8438ef488404f21d8446e487c034037783e148
provenance summary    bc160c262b23f9977902fe02ddf4ea5bdc9d0f7b4c4135c51d2cbc8d2352081f
MANIFEST.sha256 file  0dc6f0fbba8b9d8e509811b329e02bd35ec6493d1b82c92cf28969bc26aef714
```

Both licensed openings have all 19,448 rank-ten targets, residence 1,994,
and upper-hole vector

```text
(h10,h11,h12,h13,h14,h15,h16,h17) = (0,1520,271,4,0,0,0,0).
```

Thus `D=1795`.  The ordinary non-D provider projection is separately complete
at `19412/19412`.  A transient expanded checkpoint manifest existed during an
in-place refresh, but is not the present canonical binding; no present-tense
claim below relies on it.

The frozen global map, incidence map, accumulated bank, and full formula have
SHAs `d90eda6666629aad49a52247b07068d24d3e8da265f587dae55e864dca223d63`,
`80980012d7b1449c8ce3932e77ee7e5e47f5d6eb6f18d219687358cbd024355a`,
`e64219c98e4191bbef8e6ba32567cec6286c777755782030fd9cca13669971fc`,
and `5304cac329238115b57f0e01a1c488d4b5327c6cf502805007d716760d58fb19`,
respectively.

## 2. A strict negative pair at the frozen root

Let `F` be the canonical root.  The sampled state-relative actuator found the
following ordered packet.

```text
A: C6
   core   7946
   labels (4,14,7)
   roots  (7962,24330,8074)
   remove (11156,42258,11437)
   add    (11158,42261,11433)

B: star-C8
   core   5914
   labels (11,14,15,13)
   roots  (7962,22298,38682,14106)
   remove (11158,37889,68776,22443)
   add    (11157,37887,68777,22445)
```

The faces share rank-eight root `7962`.  More strongly, `A` installs incidence
edge `11158` and `B` consumes it.  Therefore `B` is not an alternating/root-
applicable primitive at `F`; it is regenerated only in state `A(F)`.  The
shared edge cancels in the net signed rewrite, so the two faces form a closed
12-edge Eulerian symmetric-difference packet.

The exact opened profiles are

| state | orientation histories | residence | upper `(h10,h11,h12,h13)` | deep |
|---|---:|---:|---:|---:|
| `F` | `(1267,727)` / `(1268,726)` | 1994 | `(0,1520,271,4)` | 1795 |
| `A(F)` | `(1268,726)` / `(1269,725)` | 1994 | `(0,1520,271,4)` | 1795 |
| `B(A(F))` | `(1268,725)` / `(1267,726)` | 1993 | `(0,1521,271,4)` | 1796 |

Hence `A` is neutral in `(R,D)`, while the pair has exact scalar cost

```text
21779*(1993-1994) + (1796-1795) = -21778.
```

This is a minimal negative accepting path: it has two physical faces, its
first prefix is non-descending, and its second schema has no root arc.

## 3. Independent replay of the pair

The search artifacts are

```text
search source          ef43457a3d18fd04de9a319b783f38a9d894043c18a45d10e3170a7b218ae592
search audit           e081853a125821c406804f6f6062fd2ddd328e928d9863b0365792b0bfd19d72
packet                 415240ce187d0e2caadcbb3d5c7f43ce92914a19d08352444c579664d59b7538
terminal primary model a9f0d53bdee43fc5db770ecac57781899c4d0f4fbed3b83ca0ac8b6af00008dd
```

An independent formula materializer reconstructed both prefixes from `F` and
reported exactly one root-applicable constituent.  Its audit SHA is

```text
b7b8f48a1029b38cf77753bdaaee2fbb3eba5bda32756d14e562a137616e15b3.
```

The independently materialized models have SHAs

```text
A(F)       a73b5fe36e4bd7944c275ffefed5181d502370e9d08ef059c834f39b9fa8142b
B(A(F))    a9f0d53bdee43fc5db770ecac57781899c4d0f4fbed3b83ca0ac8b6af00008dd.
```

For each prefix, the independent single-model auditor replayed exact degrees,
the protected boundary, all 16,261 accumulated rows, all 19,412 ordinary q1
targets, one connected augmented h1 lollipop, and both opened chronologies.
Their audit SHAs are
`934dbf0d9ff2b908d9b783c10bf1999eb02a1ca82df434db1edd4891119bc4d7`
and
`eb54a9bd5a06e32878d8c9c3f7415c9ab97e5199848c653e7c8f4e3947ca6874`.
Each deterministic y+p
extension also satisfies all 7,163,170 clauses of `round4.cnf`; the complete-
DIMACS replay audit SHA is
`777306ca8ae7cb641d9dc98522b8fa797d9088679764d593d007e169b4e0c224`
for each prefix.

## 4. A second compound mechanism: nonlinear provider handoff

An earlier internal seed-13 prefix contains a different true pair.  At its
pre-neutral base, residence/deep are `(1999,1796)`.

```text
A': C6 core 24136, labels (5,7,15), roots (24168,24264,56904)
B': C6 core 7880,  labels (0,2,14), roots (7881,7884,24264)
```

`A'` is legal and neutral in residence, reaching `(1999,1795)`.  `B'` alone
is incidence-applicable and connected, but loses one ordinary and one opened
rank-ten target.  It violates exactly zero-based accumulated row `12668`
(one-based row `12669`).  The missing target is mask `24300`: `B'` destroys
its last provider

```text
p262698: root 7884, owners 7916 and 24268,
```

whereas the ordered pair creates the replacement

```text
p387503: root 24264, owners 24268 and 24296.
```

Both providers have union `24300`.  Thus `A';B'` closes the same 45-literal
q1/Hall row by a deterministic p-channel handoff and reaches `(1997,1793)`.
The exact guard-repair audit and failed-row ledger have SHAs

```text
8e8d9ae90384c3f04c59a47c9e3ff8afca10b911232053ab0c046f600c67ea20
c5aa9f3688829c92bdeb2d68161c5509fd5934263568a64e922a25103b040565.
```

This example proves why boolean q1 coverage is not a sufficient lifted state:
the exact provider loads and regenerated p channel determine legality.

## 5. Exact theorem extracted from the two witnesses

Let the materialized state graph contain only hard-legal states and regenerate
its physical face arcs after every prefix.  Give an arc the telescoping cost
`S(F')-S(F)`, where `S=21779 R+D` on the hard `h10=0` face.

A negative two-face packet exists whenever there are a legal arc
`F --A--> G` and a regenerated arc `G --B--> H` such that

```text
S(G)-S(F) >= 0,
S(H)-S(F) < 0,
```

even if `B` has no root arc or its root proposal violates a resource row.
The first frozen-root witness realizes the missing-root-arc case.  The
provider-handoff witness realizes the resource-illegal-root-proposal case.
Both are ordinary paths in the exact lifted graph, so Bellman-Ford detects
their negative root-to-accepting cost; a static primitive catalogue cannot.

For repeated descent, one must additionally prove a uniform renewal statement
over the full endpoint state, including provider loads, clauses, protected
edges, topology/opening tickets, and any batch masks.  The observed repeated
bridge/quench chain and these two exact packets are positive finite evidence,
not a uniform expansion theorem or a weighted-bisimulation quotient proof.

## 6. Scope

The new terminal candidate has residence 1,993, not zero.  Deep holes remain
positive.  `outer_pass` remains false.  No source antecedent, lower compiler,
resident factor, universal word, or value claim is made.
