# Independent audit of the corrected `k=11` distance-17 certificate

## Verdict

The distance-17 certificate is valid for the precise local theorem below.
The frozen source regenerated the archived CNF byte for byte on a RunPod
different from the proof-producing machine, and an independent
`drat-trim` run ended in `s VERIFIED`.

Proof-critical data:

```text
CNF variables       46775
CNF clauses         164608
CNF SHA-256          36137b8b08608c6cb4f8ef7d8ea463f4f09981b715c47a53da769b60df73f978
DRAT SHA-256         ef1ee4a0be77098ff639c683c8717979283a4c3769ebe2b07681ca47853cdf07
source SHA-256       1548f086a637deda1cfeb325dcaa183900b60dac1ee77d48a7e043e00b0edde2
all-vertex input     71dfa5b4c33c86dee070b46fb991d9c8a0ef2c9d49a09825fc96d8e8c398552f
seed path            f7323f583a9d3367b27265248bea157d2a2a686422b2a360b64bbdcff441d477
```

## Exact theorem certified

Let `V` be the 462 rank-six subsets of `[11]`, let `J=J(11,6)`, and let
`E_0` be the 461 consecutive edges of `k11_lower956_upper549.txt`.
There is no real-edge set `E subseteq E(J)` satisfying all of:

1. two real vertices have degree one and every other real vertex has degree
   two; disconnected cycle components are allowed;
2. at most seventeen seed edges are absent, `|E_0 setminus E|<=17`;
3. the 461 selected rank-five intersection colours are distinct;
4. every rank-seven union colour occurs; and
5. the unique omitted rank-five colour is contained in one of the two
   degree-one vertices.

The degree equations force `|E|=|E_0|=461`.  Therefore every connected
Hamilton-path candidate with these colour properties drops at least
eighteen seed edges and has edge-set symmetric difference at least 36 from
the seed.

## Encoding audit

The audited invocation is the no-canonical all-edge mode

```text
RECOMBINE_EXTRA_SUPPORT=5
recombine_paths_sat_support 11 6 \
    k11_allbase_r7full.txt \
    k11_lower956_upper549.txt \
    allinc17:91717
```

with CNF dump-only mode enabled.  It creates the complete 6,930-edge
Johnson graph plus one dummy vertex.  Exact degree two in the augmented
graph gives 461 real edges and two distinct real endpoints after deleting
the dummy.  A sequential counter bounds missing seed edges by 17.  Colour
bucket clauses impose distinct lower colours, endpoint clauses expose the
one omitted lower colour, and 330 coverage clauses require every upper
colour.

The support-five strengthening is equisatisfiable with this distance-17
model.  The seed misses twelve upper colours.  A candidate with `d<=17`
new edges spends at least twelve on one baseline edge for each missing
colour, leaving at most `d-12<=5` extra upper-colour supports.  The selector
counter encodes exactly those extras; it is not a heuristic restriction.

Canonicalization is disabled whenever a finite near-distance limit is
present.  The CNF fixes no omitted colour, endpoint, orientation, first
edge, or coordinate permutation.  The first input supplies the vertex set;
the second supplies only the immutable preferred edge set and solver phases.

## Independent regeneration and proof check

On the independent machine, the frozen source reported

```text
extra_colour_support=5 selectors=330
vertices=462 real_edges=6930 variables=46775
dumped clauses=164608
```

The regenerated CNF hash was exactly the archived hash.  The independent
proof checker reported

```text
161581684 resolution steps
s VERIFIED
verification time: 498.291 seconds
```

The compressed CNF, proof, frozen source, both inputs, regeneration log,
and independent verification log are stored in
`scratch/certificates/k11_distance17/`.

## Scope exclusions

This theorem does not determine `nu(11)`.  It does not exclude distance 18
or a distant central row, and it imposes neither connectivity nor
factorability, lower/longer shadows, or factor labels.  It also does not
exclude unrestricted monotone-band or central-forest optima.  Its exact
content is a proof-certified radius-17 exclusion around one seed in a
relaxation which already allows disconnected cycle covers.
