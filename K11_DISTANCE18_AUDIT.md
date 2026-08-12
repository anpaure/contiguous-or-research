# Independent audit of the corrected `k=11` distance-18 certificate

## Verdict

The distance-18 certificate is valid for the precise local theorem below.
The frozen source regenerated the archived CNF byte for byte on a RunPod
different from the proof-producing machine. A second `drat-trim` run ended in
`s VERIFIED` and process exit code zero.

Proof-critical data:

```text
CNF variables       47566
CNF clauses         166186
CNF SHA-256          71c09ac92b9136d5a5eaeee3dbd702b27d51c51e3d871eedf7ec298929f5554f
DRAT SHA-256         5e36fa0a2f47408ce89a732b9993988312052b3dfd21a64fae8aa7996105cd64
source SHA-256       1548f086a637deda1cfeb325dcaa183900b60dac1ee77d48a7e043e00b0edde2
all-vertex input     71dfa5b4c33c86dee070b46fb991d9c8a0ef2c9d49a09825fc96d8e8c398552f
seed path            f7323f583a9d3367b27265248bea157d2a2a686422b2a360b64bbdcff441d477
stored CNF.gz        dc9e9bead8957ac53cdfd4a1ac59d3f6abdc9202dc6d39d4375510831e72db47
stored DRAT.gz       e2728f1c5098cf1044fa9e6d5a15d9395c93cb7698ebfe70d2ccc44ad92e7125
```

## Exact theorem certified

Let `V` be the 462 rank-six subsets of `[11]`, let `J=J(11,6)`, and let
`E_0` be the 461 consecutive edges of `k11_lower956_upper549.txt`. There is
no real-edge set `E subseteq E(J)` satisfying all of:

1. two real vertices have degree one and every other real vertex has degree
   two; disconnected cycle components are allowed;
2. at most eighteen seed edges are absent, `|E_0 setminus E|<=18`;
3. the 461 selected rank-five intersection colours are distinct;
4. every rank-seven union colour occurs; and
5. the unique omitted rank-five colour is contained in one of the two
   degree-one vertices.

The degree equations force `|E|=|E_0|=461`. Therefore every connected
Hamilton-path candidate with these colour properties drops at least nineteen
seed edges and has edge-set symmetric difference at least 38 from the seed.

## Encoding audit

The audited invocation is the no-canonical all-edge mode

```text
RECOMBINE_EXTRA_SUPPORT=6 \
RECOMBINE_DUMP_CNF=corrected_allinc18.cnf \
RECOMBINE_DUMP_ONLY=1 \
recombine_paths_sat_support 11 6 \
    k11_allbase_r7full.txt \
    k11_lower956_upper549.txt \
    allinc18:<SAT-seed>
```

The numeric SAT seed changes phases only and not the dumped clauses. The model
creates the complete 6,930-edge Johnson graph plus one dummy vertex. Exact
degree two in the augmented graph gives 461 real edges and two distinct real
endpoints after deleting the dummy. A sequential counter bounds missing seed
edges by 18. Colour bucket clauses impose distinct lower colours, endpoint
clauses expose the one omitted lower colour, and 330 coverage clauses require
every upper colour.

The support-six strengthening is equisatisfiable with this distance-18 model.
The seed misses twelve upper colours. A candidate at distance at most 18 must
spend at least twelve new edges, one for each missing colour, leaving at most
`18-12=6` new edges supporting already-present upper colours. Hence it uses at
most six such extra colour supports. The selector counter encodes this safe
cap; it is not a heuristic restriction.

Canonicalization is disabled whenever the finite near-distance limit is
present. The CNF fixes no omitted colour, endpoint, orientation, first edge,
or coordinate permutation. The first input supplies the vertex set; the
second supplies only the immutable preferred edge set and solver phases.

## Independent regeneration and proof checks

The independent generator reported

```text
extra_colour_support=6 selectors=330
vertices=462 real_edges=6930 variables=47566
dumped_cnf=regenerated18.cnf clauses=166186
```

The regenerated CNF hash was exactly the archived hash. The producer-side
proof checker and the independent checker both reported the same core:

```text
93160 of 166186 clauses in core
1459271 of 2492985 lemmas in core
769368154 resolution steps
36321 RAT lemmas in core
s VERIFIED
```

The independent run took 2427.502 seconds and ended with `EXIT:0`. Its exact
log is
`scratch/certificates/k11_distance18/independent_dratcheck.log`.

The compressed CNF, proof, frozen source, both inputs, regeneration logs,
solver log, and two verification logs are stored in
`scratch/certificates/k11_distance18/`.

## Scope exclusions

This theorem does not determine `nu(11)`. It excludes distance 18 but not a
more distant central row, and it imposes neither connectivity nor
factorability, lower/longer shadows, or factor labels. It also does not
exclude unrestricted monotone-band or central-forest optima. Its exact content
is a proof-certified radius-18 exclusion around one seed in a relaxation which
already allows disconnected cycle covers.
