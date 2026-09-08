# Independent audit of the promoted `k=11` distance-19 certificate

## Verdict: **PASS**

The promotion in `K11_DISTANCE19_CERTIFICATE_PROMOTION.md` is justified.
The frozen CNF is independently verified UNSAT by `drat-trim`, and the exact
semantic consequence is:

> There is no spanning 461-real-edge subgraph of `J(11,6)` having two
> degree-one vertices and 460 degree-two vertices, complete rank-seven union
> colours, pairwise-distinct rank-five intersection colours, endpoint access
> to the unique omitted rank-five colour, and at most nineteen missing edges
> from the score-549 seed.

Disconnected real cycle components are allowed by the formula.  Therefore the
result applies in particular to connected Hamilton paths satisfying the same
colour and endpoint requirements.  Every such object drops at least twenty
seed edges.  Since both its real-edge set and the seed edge set have size 461,
their symmetric difference has size at least forty.

This is only a radius-19 theorem for the audited central-colour relaxation.  It
does not prove that no qualifying object exists at distance twenty or more,
does not impose factorability or deeper shadows, and does not decide the full
length-465 OR-array problem.

## 1. Independent checker evidence

The complete local checker log is

```text
scratch/certificates/k11_distance19/k11_d19_drat_trim.log
```

with SHA-256

```text
da9fddf68f57aefbdf4e61941c925ee91b086f5d7b116aa43862dd34a32e2bfd
```

After normalizing its carriage-return progress formatting for display only,
its terminal lines are

```text
c parsing input formula with 48357 variables and 167764 clauses
c finished parsing, read 4723026902 bytes from proof file
c detected empty clause; start verification via backward checking
c 122890 of 167764 clauses in core
c 11210313 of 22261486 lemmas in core using 6627849376 resolution steps
c 45488 RAT lemmas in core; 53735029 redundant literals in core lemmas
s VERIFIED
c verification time: 9848.830 seconds
EXIT:0
```

Thus both required terminal conditions are present: the proof checker itself
printed `s VERIFIED`, and the wrapper recorded exit status zero immediately
after it terminated.  This is not merely the producer's `UNSAT` assertion.

The producer log is separately frozen with SHA-256

```text
ae0cd43d8e780c8c682a63fac37f41d242b07ca5fd16e0f6ccca326e44f08be6
```

and contains `s UNSATISFIABLE` and `EXIT:20`, consistently but redundantly.

## 2. Remote proof artifact confirmation

Without rerunning the 9848-second proof check, I connected read-only to the
recorded proof-producing host `157.157.221.29:27423` and independently ran
`stat`/`sha256sum` on the existing artifacts.  The results were

```text
/root/corrected_allinc19_proof.drat  4723026902 bytes
e55401bf90ed645f032f8769db262646ed661519d753aa441b05198b4a30fa78

/root/corrected_allinc19.cnf         5590154 bytes
b2c247d22105cfa963d4e6871e03397c5948a4447d2cedf5e5c7f7f09ccb90ef

/root/k11_d19_drat_trim.log          493 bytes
da9fddf68f57aefbdf4e61941c925ee91b086f5d7b116aa43862dd34a32e2bfd
```

The remotely hashed checker log is therefore byte-identical to the locally
frozen log, and the proof byte count is exactly the count reported by
`drat-trim`.  The proof file itself is not duplicated in the local bundle
because it is 4.72 GB; this is a certificate-archival durability caveat, not a
logical gap in the verified theorem.

## 3. Local bundle hashes and DIMACS inventory

The proof-critical local files independently hash to

```text
b2c247d22105cfa963d4e6871e03397c5948a4447d2cedf5e5c7f7f09ccb90ef  corrected_allinc19.cnf
1548f086a637deda1cfeb325dcaa183900b60dac1ee77d48a7e043e00b0edde2  recombine_paths_sat.cpp
71dfa5b4c33c86dee070b46fb991d9c8a0ef2c9d49a09825fc96d8e8c398552f  k11_allbase_r7full.txt
f7323f583a9d3367b27265248bea157d2a2a686422b2a360b64bbdcff441d477  k11_lower956_upper549.txt
ae0cd43d8e780c8c682a63fac37f41d242b07ca5fd16e0f6ccca326e44f08be6  k11_kissat_d19_proof.frozen.log
da9fddf68f57aefbdf4e61941c925ee91b086f5d7b116aa43862dd34a32e2bfd  k11_d19_drat_trim.log
```

An independent token-level DIMACS parse, not just the header, gives

```text
variables in header       48,357
clauses in header         167,764
parsed clause terminators 167,764
maximum variable          48,357
literal occurrences       990,744
CNF size                  5,590,154 bytes
```

This matches the inventory in the prior source audit and the formula parsed by
the successful proof check.

## 4. Independent input checks

Both input files contain exactly 462 distinct masks, every mask has rank six,
and every consecutive pair is an edge of `J(11,6)`.  Recomputing their colour
statistics gives

```text
k11_allbase_r7full.txt:
    462 vertices, 461 distinct rank-five intersection colours,
    330 distinct rank-seven union colours.

k11_lower956_upper549.txt:
    462 vertices, 461 distinct rank-five intersection colours,
    318 distinct rank-seven union colours (twelve missing).
```

The second file consequently defines a 461-edge seed set `E0`; its edges are
distinct because its 461 lower colours are distinct.

## 5. Exact encoding semantics

The dumped invocation uses mode `allinc19`:

* `all` exposes every one of the 6,930 edges of `J(11,6)`;
* `inc19` sets the near-distance limit to nineteen;
* the finite distance limit disables every seed-relative canonicalization;
* `inc` does not enable ordered connectivity, pair shadows, deeper shadows, or
  coordinate-run clauses; and
* `RECOMBINE_DUMP_ONLY=1` returns immediately after the static DIMACS dump, so
  the later lazy connectivity/refinement loop contributes no hidden clauses.

### Degree profile and disconnected cycles

One dummy vertex is adjacent to all 462 real vertices.  The CNF imposes degree
exactly two on every real vertex and on the dummy.  Hence the augmented graph
has 463 selected edges.  Exactly two are dummy edges, leaving exactly 461 real
edges.  Removing the dummy makes its two distinct real neighbours degree one
and leaves every other real vertex degree two.

No connectivity clauses occur in this unordered dump.  The dummy component
opens into one real path, while any other components may be real cycles.  The
promoted theorem correctly states this relaxation rather than silently calling
every model a Hamilton path.

### Distance is the number of dropped seed edges

For each of the 461 seed edges, the counter receives the literal `-x_e`; it
imposes

```text
|E0 \\ E| <= 19.
```

It does not encode vertex-order edit distance or a number of local moves.
Because the degree equations independently force `|E|=|E0|=461`, if `d` seed
edges are dropped then exactly `d` nonseed edges are added and

```text
|E triangle E0| = 2d.
```

The verified UNSAT result at `d<=19` therefore proves `d>=20` and symmetric
difference at least forty for every qualifying candidate.

### Colour and endpoint clauses

Every real Johnson edge has a rank-five intersection and a rank-seven union.
Pairwise clauses impose at most one selected edge of each rank-five colour.
There are 461 selected real edges and 462 possible rank-five colours, so the
selected lower colours are exactly 461 distinct colours and exactly one is
omitted.  A coverage clause for each of the 330 rank-seven masks enforces full
upper-colour coverage.

For every rank-five target `C`, the endpoint-access clause is

```text
(some selected real edge of lower colour C)
OR (some selected dummy edge at a rank-six vertex containing C).
```

It is automatically satisfied by every present lower colour.  For the unique
omitted colour it requires one of the two degree-one real endpoints to contain
that colour, exactly as claimed.

### The support cap is redundant

The seed misses twelve upper colours.  If at most nineteen seed edges are
dropped, exactly the same number of nonseed edges are selected.  At least
twelve nonseed edges are mandatory to introduce those missing colours, leaving
at most seven extra nonseed edges.  The support encoding charges every nonseed
edge of a seed-present colour and every duplicate use of a seed-missing colour,
then caps the number of activated colour classes at seven.  One activated
class can account for multiple extras, so the number of active classes is at
most the number of extra edges.  The cap therefore removes no model satisfying
the distance and upper-coverage clauses.

The implementation independently computes the safe cap `19-12=7` and rejects
any supplied smaller cap.

## 6. Scope discipline

The verified implication is exactly

```text
at-most-19 dropped seed edges is UNSAT
    => every qualifying candidate drops at least 20 seed edges
    => real-edge symmetric difference from E0 is at least 40.
```

It remains valid despite allowing disconnected cycles, because that makes the
SAT search space larger.  It says nothing about distance twenty or beyond and
does not establish any claim about the unrestricted optimum `nu(11)`.

