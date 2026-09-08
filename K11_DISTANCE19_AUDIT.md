# Independent audit of the corrected `k=11` distance-19 certificate

> **Post-audit promotion.**  The pending independent check described below
> subsequently completed with `s VERIFIED` and `EXIT:0`.  The checker log,
> proof hash, and promoted theorem are frozen in
> `K11_DISTANCE19_CERTIFICATE_PROMOTION.md`.  The remainder of this file is
> the contemporaneous pre-verification source/encoding audit.

## Status: proof verification pending

The archived source and inputs independently regenerate the producer CNF byte
for byte, and the proof-producing Kissat run ended with

```text
s UNSATISFIABLE
EXIT:20
```

Those facts do **not** yet certify UNSAT.  At the time of this report, an
independent `drat-trim` process was still reading the 4.4-GiB proof; its log
had not yet printed `s VERIFIED` and the wrapper had not yet recorded exit
code zero.  Accordingly, the distance-19 theorem below is a precisely stated
**pending theorem**, not a result that may yet be cited as proved.

Promotion requires all of the following against the exact CNF hash recorded
below:

1. the independent checker prints `s VERIFIED`;
2. the checker process exits with code `0`;
3. its complete log, the proof hash, and the exact proof artifact are frozen;
4. the log and proof are added to the local certificate bundle.

Until then the already certified radius is distance 18, as documented in
`K11_DISTANCE18_AUDIT.md`.

## Frozen and independently reproduced data

The current local bundle is

```text
scratch/certificates/k11_distance19/
```

Its proof-critical hashes are

```text
CNF SHA-256          b2c247d22105cfa963d4e6871e03397c5948a4447d2cedf5e5c7f7f09ccb90ef
source SHA-256       1548f086a637deda1cfeb325dcaa183900b60dac1ee77d48a7e043e00b0edde2
all-vertex input     71dfa5b4c33c86dee070b46fb991d9c8a0ef2c9d49a09825fc96d8e8c398552f
seed path            f7323f583a9d3367b27265248bea157d2a2a686422b2a360b64bbdcff441d477
producer-log SHA-256 ae0cd43d8e780c8c682a63fac37f41d242b07ca5fd16e0f6ccca326e44f08be6
```

The CNF header and an independent DIMACS parse give

```text
variables            48,357
clauses              167,764
parsed clauses       167,764
maximum variable     48,357
literal occurrences  990,744
CNF size             5,590,154 bytes
```

The producer proof currently exists remotely with size

```text
4,723,026,902 bytes.
```

Its SHA-256 is deliberately marked pending rather than inferred from its
filename or producer log.  The proof itself is not yet present in the local
bundle.

On a RunPod different from the proof-producing machine, the frozen source and
two inputs produced

```text
extra_colour_support=7 selectors=330
vertices=462 real_edges=6930 variables=48357
dumped_cnf=regen19_independent.cnf clauses=167764
```

and the regenerated CNF had exactly the archived hash

```text
b2c247d22105cfa963d4e6871e03397c5948a4447d2cedf5e5c7f7f09ccb90ef.
```

This proves byte-identical independent regeneration.  It does not replace
proof checking.

## Exact theorem that the pending proof would certify

Let `V` be the 462 rank-six subsets of `[11]`, let `J=J(11,6)`, and let `E_0`
be the 461 consecutive real edges of
`k11_lower956_upper549.txt`.  If the independent DRAT check succeeds, it will
certify that there is no real-edge set `E subseteq E(J)` satisfying all of:

1. two real vertices have degree one and every other real vertex has degree
   two; disconnected cycle components are explicitly allowed;
2. at most nineteen seed edges are absent,
   `|E_0 setminus E|<=19`;
3. all 461 selected rank-five intersection colours are distinct;
4. every one of the 330 rank-seven union colours occurs; and
5. the unique omitted rank-five colour is contained in at least one of the
   two degree-one endpoint vertices.

The degree equations force `|E|=|E_0|=461`.  Therefore a verified proof would
imply that every connected Hamilton-path candidate satisfying these same
colour and endpoint conditions drops at least twenty seed edges and has
real-edge-set symmetric difference at least 40 from `E_0`.

The disconnected relaxation is important: the pending statement excludes
all qualifying degree-two covers in this radius, not only connected paths.

## Independent input audit

Both one-line inputs contain 462 distinct rank-six masks.  Their independently
recomputed path statistics are

```text
k11_allbase_r7full.txt:
    462 Johnson-adjacent vertices, 461 lower colours, 330 upper colours

k11_lower956_upper549.txt:
    462 Johnson-adjacent vertices, 461 lower colours, 318 upper colours
```

Thus the preferred seed misses exactly twelve rank-seven colours.  In the
audited all-edge mode the first input supplies the complete vertex set; the
last input supplies `E_0` and phase preferences.  The complete Johnson graph
is generated independently of the input edges.

## Encoding audit

The exact dump-only invocation is

```bash
RECOMBINE_EXTRA_SUPPORT=7 \
RECOMBINE_DUMP_CNF=corrected_allinc19.cnf \
RECOMBINE_DUMP_ONLY=1 \
./recombine_paths_sat_audit 11 6 \
    k11_allbase_r7full.txt \
    k11_lower956_upper549.txt \
    allinc19
```

The optional numeric SAT seed changes phases only and cannot change the
dumped clauses.

### Complete graph and degree equations

The `all` prefix exposes all 6,930 edges of `J(11,6)`.  The generator adds one
dummy vertex adjacent to all 462 real vertices.  Every real vertex and the
dummy have degree exactly two in the augmented selected graph.  Removing the
dummy leaves exactly two distinct degree-one real vertices, with all other
real vertices of degree two, and exactly 461 selected real edges.  No
connectivity clauses are present in this dump-only, unordered formula, so
disconnected real cycles are genuinely allowed.

### Corrected distance bound and absence of canonicalization

For every one of the 461 preferred edges, a literal records that it was
dropped.  A sequential counter imposes at most 19 drops.  Because a finite
near-distance limit is active, the source disables the otherwise WLOG bit,
endpoint, orientation, omitted-colour, and first-edge canonicalization.  This
is the corrected formulation: no symmetry tied to the seed is silently
assumed inside its Hamming ball.

### Lower rainbow, upper completeness, and endpoint access

For every rank-five colour, pairwise clauses permit at most one selected real
edge of that colour.  Since there are 461 selected real edges and 462 possible
rank-five colours, exactly one lower colour is omitted.  One coverage clause
for each rank-seven colour requires all 330 upper colours.

For each possible omitted rank-five target `C`, the formula requires either a
selected real edge of colour `C` or a selected dummy edge incident with a
rank-six vertex containing `C`.  Since exactly one lower colour is absent,
this says precisely that the omitted colour is available at an endpoint.

### Why `RECOMBINE_EXTRA_SUPPORT=7` is exact

The preferred seed misses twelve upper colours.  If `d<=19` seed edges are
dropped, the fixed real-edge count means exactly `d` nonseed edges are added.
At least twelve of them are required to introduce the twelve missing upper
colours.  At most

```text
d-12 <= 7
```

additional nonseed edges remain.  The support variables charge any nonseed
edge of a seed-present upper colour, and charge a seed-missing colour if it is
used more than once.  Hence at most seven support colours can be active.  The
cap is a redundant consequence of the distance and upper-coverage clauses,
not a heuristic restriction.  The implementation independently computes the
minimum safe cap `19-12=7` and refuses any smaller supplied value.

As an arithmetic cross-check against the certified distance-18 formula,
raising the two sequential-counter widths from 18/6 to 19/7 adds

```text
461+330 = 791 variables
2*(461-1)+2*(330-1) = 1,578 clauses,
```

which takes `47,566/166,186` exactly to the observed
`48,357/167,764` inventory.

## Current proof evidence

The proof-producing Kissat wrapper returned

```text
s UNSATISFIABLE
EXIT:20
```

against the exact CNF hash above.  This is strong producer evidence but is not
an independently checkable theorem by itself.

The independent command is of the form

```bash
/root/drat-trim/drat-trim \
    corrected_allinc19.cnf \
    corrected_allinc19_proof.drat \
    > k11_d19_drat_trim.log 2>&1
echo EXIT:$? >> k11_d19_drat_trim.log
```

At the audit snapshot, that process was alive and using one CPU, while
`k11_d19_drat_trim.log` was still empty.  Therefore neither required terminal
condition—`s VERIFIED` and `EXIT:0`—was yet present.

## Scope exclusions

Even after successful proof verification, this theorem would remain local to
the fixed-row central-graph search around one seed.  It would **not**:

* determine `nu(11)` or rule out a length-465 unrestricted array;
* rule out a qualifying central row at distance 20 or more;
* impose or certify connectivity, delay-three factorability, rank-three/four/
  eight/nine deeper shadows, lower factor labels, or full interval-OR
  coverage; or
* constrain the globally unrestricted monotone-band/central-forest formula.

Its exact content, once independently verified, would be a radius-19
exclusion around `k11_lower956_upper549.txt` in a relaxation that already
allows disconnected degree-two covers while enforcing lower-rainbow,
rank-seven completeness, and omitted-colour endpoint access.
