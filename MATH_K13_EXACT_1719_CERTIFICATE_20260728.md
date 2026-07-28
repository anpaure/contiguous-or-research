# Exact k=13 certificate: nu(13) = 1719

## Result

There is a nonzero word of length `1719` on subsets of `[13]` whose
contiguous ORs contain every one of the `2^13-1 = 8191` nonempty masks.
Together with the endpoint-blocker lower bound `nu(13) >= B(13) = 1719`,
this proves

\[
\boxed{\nu(13)=1719.}
\]

## Construction route

1. The SAT model
   `scratch/k13_res0_onehole_repair_history16x5.round0.disconnected.json`
   is a `Z_13`-equivariant exact middle 2-factor with two physical cycles of
   lengths `1547` and `169`.  It has depth-3 residence and complete lower and
   upper shadows at every depth `q=1,...,6`.
2. Cut one edge in each physical cycle and join the resulting paths by one
   cross-component Johnson edge.  The enumerator
   `scratch/search_k13_two_cycle_one_seam_paths.py` checks all `6240` cross
   Johnson pairs and both orientations at both cuts (`24960` candidates).
3. `6032` candidates preserve every upper shadow.  Of those, `1092` also
   satisfy the exact linear depth-3 residence equation `D^3 P=T`.
4. Candidate `000` loses only one native lower-q1 colour.  Its complete
   flexible-compiler Hall graph has deficiency zero.
5. The global linear depth-3 compiler assigns the `1719` entries and covers
   the whole lower ideal.  The already-certified carrier windows cover the
   middle and upper ideals.

The chosen seam is

\[
2515\longrightarrow2391,
\]

with component data

```text
component 0 endpoint = 3,  direction = -1
component 1 endpoint = 53, direction = +1
```

## Independent audit

For `scratch/k13_two_cycle_one_seam_path_000.word.txt`:

```text
word length                  1719
nonempty contiguous ORs      8191 / 8191
missing OR masks             0
D^3 word length              1716
distinct D^3 values          1716 = binom(13,7)
D^3 rank histogram           {7: 1716}
row distinct counts          [990, 1491, 1717, 1716]
entry rank histogram         {1:17, 2:196, 3:677, 4:826, 5:2, 6:1}
```

SHA-256:

```text
word
8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0

middle path / cut certificate
baa204bf8208c531cc1905c6cf53a2438db85a0b778231c0e59a631eef4b7973

Hall audit
2a7b7eb4ece4711214dd24f93ad216f8d77dd53c27bd7edda0162b3059f8c137

two-cycle source
2987fe2e3ef6de56c538038688835246e6aafafc5c6a7dd576b3df986ee44ef9
```

## Primary artifacts

- exact word: `scratch/k13_two_cycle_one_seam_path_000.word.txt`
- middle path and cut data: `scratch/k13_two_cycle_one_seam_path_000.json`
- Hall certificate: `scratch/k13_two_cycle_one_seam_path_000.hall.json`
- complete seam census: `scratch/k13_two_cycle_one_seam_paths.json`
- source exact 2-factor:
  `scratch/k13_res0_onehole_repair_history16x5.round0.disconnected.json`
- source full audit:
  `scratch/k13_res0_onehole_repair_history16x5.round0.disconnected.full_audit.json`

## Structural lesson

Hamilton-cycle connectivity was stronger than necessary.  The optimal word
only needs its `D^3` carrier to be a Hamilton **path**.  The two boundary
degrees of freedom created by cutting two exact carrier cycles are precisely
what lets the `W+1` cells in row `d-1` absorb the single lost lower-q1 colour,
while one cross seam retains all upper shadows.  This is the reusable
architecture to test for the remaining depth-3 cases.

## Transferable signature: comparison with the exact k=11 carrier

The quantities which are not forced by counting were extracted from the
cyclic carriers before they were opened into paths.

Both constructions are genuinely cyclic-equivariant:

- the exact `k=11` carrier is one `Z_11` quotient cycle, of nonzero voltage
  `2`;
- the exact `k=13` carrier is a `Z_13` quotient 2-factor with component
  sizes `119` and `13`, of nonzero voltages `8` and `6`.  Its physical
  lifts therefore have lengths `1547` and `169`.

Thus the successful `k=13` relaxation was not to abandon symmetry.  It was
to replace quotient Hamiltonicity by an exact small-component 2-factor and
then perform one shadow-safe cross-component splice.

For the level-`r-1` sequence `X_i=T_{i-1}\cap T_i`, the cyclic run-length
histograms are:

```text
k=11:
  3:143, 4:132, 5:55, 6:44, 7:22, 8:11,
  9:22, 10:11, 11:11, 13:11

k=13:
  3:429, 4:299, 5:208, 6:221, 7:117, 8:130,
  9:104, 10:13, 11:13, 12:104, 13:26,
  14:13, 15:26, 17:13
```

Equivariance makes the per-coordinate histogram identical for every
coordinate.  In both cases the minimum run is exactly the required depth
`3`, not bounded away from it.  The residence condition is therefore active,
but the `k=13` carrier still achieves it with one more unit of mean-run
margin.

The upper-q1 multiplicity histograms are:

```text
k=11:  1^198 2^132
k=13:  1^936 2^273 3^78
```

So `k=11` attains the integrality floor (no multiplicity above two), whereas
`k=13` has 78 triple-covered upper colours.  Its floor-corrected collision
mass is `2*78=156`, yet it still gives an exact optimal OR word.  Consequently
the simple-design/CPCR condition is useful search guidance but is not a
necessary condition for exactness.
