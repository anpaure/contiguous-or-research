# Exact `k=15` certificate from a two-cycle resident factor

Date: 2026-07-29

Status: **proved and independently verified**.

## 1. Exact result

Let `nu(k)` be the minimum length of a nonzero word whose nonempty contiguous
ORs contain every nonempty `k`-bit mask.  The counting lower bound gives

```text
W = binom(15,8) = 6435,
d(15) = 3,
B(15) = W+d = 6438.
```

The retained word

```text
scratch/threadD_k15_exact_6438_owned_20260729.word
```

has length `6438`, SHA-256

```text
a37a9c82e8e57c22a78c349fcce4edb1932dee8dbdde651001cb30ebcf699585,
```

and covers all `32767` nonempty masks.  Its third derivative is exactly the
`6435` rank-eight masks.  Therefore

```text
nu(15)=6438,
N(15)=6439.
```

The second equality follows by adjoining one zero, using the standard zero
separation lemma.

## 2. Frozen carrier and seam

The source factor is

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    from3_markov_s7_merge.best.json
```

with SHA-256

```text
0c11aefbfe3a0661c457b48f0a7a82afacc6d02d4362e23e5d710bb799135555.
```

Its independent factor audit has SHA-256

```text
c5f700aef824b93e257957c313a7395eb3d2512c773e6d434f08934ba93ac6f4.
```

It is a degree-two factor on every rank-eight set, with two physical cycles
of lengths `6390` and `45`.  Every coordinate run has length at least four,
and every lower and upper cyclic shadow is complete at depths `q=1,...,7`.

The winning opening is

```text
states             44 -> 12863
component order    0,1
cuts               22,41
orientations       0,1
cut colours        18553,18033
seam colour        17017
```

The seam is Johnson but deliberately **nonrecycling**: `17017` is neither cut
colour.  The resulting middle chronology has SHA-256

```text
273985a653e9301da84a15cfd7d9c6c2720fe7d48b734910e7052200d585aa7b.
```

It is resident, has no upper hole at any depth under either fixed-width or
arbitrary-width replay, has exactly two lower-q1 holes (`18553,18033`), and
has no lower hole at depths `q=2,...,7`.

This corrects the earlier overrestriction to cut-colour-recycling seams.  An
exact census of all `1290` recycling seams found zero upper-complete
chronologies.  The broader catalogue contains `18000` Johnson endpoint pairs,
of which `3960` are residence-safe; the positive above is arc 4 in the
repo-owned ordering.

## 3. Boundary SDR and compiler

For a depth-three resident path `T`, let `P` be its maximal erosion.  Its six
high boundary cells have ranks

```text
8,7,6 | 6,7,8.
```

The two missing rank-seven cut colours have the exact containment SDR

```text
18553 -> left outer cell,
18033 -> right outer cell.
```

The generalized compiler then has `4945` residual literal targets: all `4943`
rank-one through rank-five targets, plus those two rank-seven targets.  Its
ordinary Hall matching is `4945/4945`.  The exact adjacent-omission model has

```text
assignment variables       200192
constraints                 50011
adjacent omission rows      38628
```

and returns `VERIFIED_OPTIMAL`.  The owned H100 run used one CPU worker and
spent `2.419` seconds in this compiler (`13.391` seconds end to end).

The compiled word has derivative rank histograms

```text
D^0: 1^15 2^105 3^455 4^1365 5^4495 7^3
D^1: 6^6433 7^2 8^2
D^2: 7^6434 8^2
D^3: 8^6435.
```

## 4. Independent verification

The following three routes agree.

1. The H100 compiler constructs the word, checks `D^3 A=T`, and invokes the
   independent literal verifier.
2. `verify_exact_or_word.py` locally enumerates all intervals until their OR
   is full, obtaining `32767/32767` masks and the exact middle row.
3. `threadD_verify_k15_owned_two_cycle_certificate_20260729.py` independently
   reconstructs both opened cycles and the seam from the frozen factor,
   recomputes all lower/fixed-upper/arbitrary-upper shadows, checks the third
   derivative, and directly enumerates the word's interval ORs.

Frozen outputs are

```text
scratch/threadD_k15_exact_6438_owned_broad_endgame_20260729.audit.json
scratch/threadD_k15_exact_6438_owned_independent_verify_20260729.json
scratch/threadD_k15_exact_6438_owned_reconstruction_20260729.audit.json.
```

The reproducibility hashes are

```text
f66d21fd369a2abe62adb6abd1e434ee2b3a39cfa0090e9aff38a02d16c2b139  all-seam enumerator
1fb65f879d8099ddc95ef0b2c12ebaf9ff5c7fa4753ed9676a9a26de7bc31cc9  factor/seam library
647b5a05e9263378c828e39d751792c6f5b2dbd17f8aca64733c893654578fcf  generalized compiler
9d3498964c5b2eb83dcf6e36727e9b0e30cc2e17bac2db7ef057138cef1dd26d  literal verifier
cbd5d09a036aacd7d7c3dbda9a4d73e09fff089350fbfd5b49367097adad34a0  reconstruction verifier
1c064dbd0367d51b4cf79c37854d80698b8f2bba7db9bd7a7312c8f33fa1fb08  H100 endgame audit
50d786c87ff41598e8740ac1e8c9099349197d81c02eb20b2ea7a08df3d69dbf  local literal audit
bac9289dafa0a7f9237e1b7652c152b8b7331cc204e3f69541248f101b268c40  reconstruction audit
```

Reproduction commands (run the first on the H100 CPU with OR-Tools on
`PYTHONPATH`) are:

```text
python3 scratch/threadD_twocycle_one_seam_frontier_20260729.py \
  --output owned_broad_endgame.audit.json \
  --word-dir owned_broad_words --seam-mode all-johnson \
  --shard-index 0 --shard-count 1 --compiler-workers 1 --seed 1961

python3 scratch/verify_exact_or_word.py \
  scratch/threadD_k15_exact_6438_owned_20260729.word \
  --k 15 --require-middle-row

python3 scratch/threadD_verify_k15_owned_two_cycle_certificate_20260729.py \
  --output scratch/threadD_k15_exact_6438_owned_reconstruction_20260729.audit.json
```

No SAT/CP status alone is used as the final certificate: acceptance rests on
the literal word and the independent deterministic replays.

## 5. Generic exact factor-to-word algorithm

Fix `k`, central rank `r`, middle width `W=binom(k,r)`, and lower-bound
depth `d`.  Suppose an exact rank-`r` cycle factor is given.

1. **Cut states.**  For every factor edge and both orientations, form the
   opened component path and retain its endpoint collars.
2. **All-seam census.**  Enumerate every permitted endpoint transition; do
   not restrict the seam colour to a deleted colour.  Directly test the
   seam collar and the erosion identity.  For a factor with `c` components,
   enumerate component-transversal paths of `c-1` seams.
3. **Unrestricted upper replay.**  Reconstruct the complete middle chronology
   `T`.  For every start, process the first arrival of each absent coordinate;
   this enumerates every distinct interval union in `O(kW)` time.  Reject any
   chronology missing an upper target.  Minimum-width witnesses may be used as
   a sufficient eager filter, never as a necessary projected cut.
4. **Maximal erosion and boundary SDR.**  Form

       P_j = intersection of T_i over max(0,j-d) <= i <= min(W-1,j).

   Compute the lower targets absent from the fixed positive derivative rows
   of `P`.  Run the exact containment-capacity matching on every cell able to
   contain a residual target.  In a residence-safe geodesic chronology the
   interior cells have rank `r-d`, so the higher residuals are confined to the
   `2d` boundary cells.
5. **Generalized compiler.**  Match every residual target `S` to one position
   `p` with `S subseteq P_p`, at most one target per position.  Impose the
   coordinatewise adjacent equations

       A_p union A_(p+1) = P_p union P_(p+1).

   Unassigned positions retain `A_p=P_p`.  This is the exact one-core
   compiler `DA=DP`; solve its Hall relaxation and then its coupled integral
   model.
6. **Literal verification.**  Require nonempty letters, length `W+d`, exact
   `D^d A`, and direct coverage of all nonempty masks.

This is a finite exact algorithm for a fixed factor and seam alphabet.  A
negative result must state that scope; a positive literal word is global.

## 6. Minimal abstract lifting lemma

### Lemma (resident factor/compiler lift)

Let `T=(T_0,...,T_(W-1))` be a permutation of all rank-`r` subsets.  Assume:

1. `T` is a Johnson path whose every internal coordinate run has length at
   least `d+1`;
2. every set of rank greater than `r` is the union of a nonempty interval of
   `T`;
3. for the maximal erosion `P` above, there is a nonempty word
   `A=(A_0,...,A_(W+d-1))` such that `DA=DP`; and
4. every nonempty set of rank less than `r` is the union of an interval of
   `A`.

Then `A` is a universal nonzero word of length `W+d`.  If `W+d` is the
counting lower bound, it is optimal.

### Proof

For every `i`, each `P_j` contributing to `(D^dP)_i` is an intersection of a
window containing `T_i`, so `(D^dP)_i subseteq T_i`.  Conversely, a coordinate
of `T_i` lies in a run of length at least `d+1`; one length-`d+1` subwindow of
that run contains `i`, so the coordinate belongs to a contributing `P_j`.
Hence `D^dP=T`.

From `DA=DP`,

```text
D^d A = D^(d-1)(DA) = D^(d-1)(DP) = D^d P = T.
```

Thus every middle target is the OR of `d+1` consecutive letters of `A`.
If an upper target is `T_u union ... union T_v`, then it is exactly

```text
A_u union ... union A_(v+d),
```

so hypothesis 2 lifts every upper target.  Hypothesis 4 supplies every lower
target.  The letters are nonempty, and the length is `W+d`; therefore `A` is
universal and attains the lower bound.  QED.

The all-depth factor theorem is what makes hypotheses 1--2 reachable with few
seams; the boundary SDR and generalized compiler are the exact finite content
of hypotheses 3--4.  Connectivity by itself is unnecessary.

## 7. The minimal uniform lemma for all `k`

Component count alone cannot be the uniform hypothesis.  Even for the solved
two-cycle factor, all `1290` residence-safe seams in the natural
cut-colour-recycling subcatalogue fail upper coverage.  Nor is the boundary
SDR sufficient: it ignores low-rank competition and the adjacent equations.

The exact uniform statement needed by this method is therefore the following.

### Uniform openable-factor lemma `UOF(k)`

Put `r=ceil(k/2)`, `W=binom(k,r)`, and let `d=d(k)` be the lower-bound depth.
There is an exact cycle factor of the rank-`r` owner layer and a transversal
choice of cuts, orientations, and unrestricted physical seams such that the
resulting linear chronology `T` satisfies:

1. `T` is depth-`d` resident (equivalently, its maximal erosion `P` has
   `D^dP=T`);
2. every target of rank greater than `r` is an arbitrary-width interval union
   of `T`; and
3. the exact residual compiler of `P` is integrally feasible: there is a
   nonempty `A` with `DA=DP` covering every lower target.

### Corollary

If `UOF(k)` holds, then `nu(k)=B(k)=W+d`.  If it holds for every `k`, the
conjectured formula holds uniformly.

**Proof.**  Apply the resident factor/compiler lift.  The lower bound supplies
the reverse inequality.  QED.

This is minimal relative to the present pipeline: deleting condition 1 loses
literalization of the middle chronology; deleting condition 2 leaves an upper
mask uncovered; deleting condition 3 leaves a lower mask uncovered.  “Few
components” is a tractability promise for finding the transversal, not a
replacement for any of these three exact conditions.  The remaining general
mathematical problem is to prove `UOF(k)` for a uniform factor family, or to
derive its three clauses from a stronger but genuinely checkable local seam
extension property.
