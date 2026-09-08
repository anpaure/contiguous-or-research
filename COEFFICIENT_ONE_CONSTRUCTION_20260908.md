# What the coefficient-one manuscript constructs

2026-09-08. Companion to `COEFFICIENT_ONE_PROOF_20260908.md`.

The manuscript's original cutoff-and-packing PBBS recipe, underlying its
logarithmic analysis, is documented in Sections 1 and 2. An executable
implementation of that original recipe has not been delivered here.
The later height-adaptive PBBS recipe in Section 3 has a deterministic
implementation producing a verified 24,957-letter word at k=17; an exact
binary-forest repair reduces that to 24,947. The current best supplied
literal word has 24,658 letters and is independently verified, while its
rewrite/search regeneration procedure was not supplied. These construction
and verification scopes are distinct. The general proofs have internal
AI-agent reviews, not independent external review or formal verification;
the finite words have exact exhaustive coverage certificates.

## 1. Earlier cutoff-and-packing recipe in odd dimension

Given n=2r+1, try every positive integer H with 2H<=r+1. Fix a
lexicographic order to resolve arbitrary choices.

1. Enumerate the rank-r states of the canonical parenthesis-matching
   PBBS permutation. Take their complements and traverse by two steps,
   obtaining rank-(r+1) owner cycles X_i. The map and conventions are in
   `PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`, Sections 1, 8, and 9,
   and `PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md`.

2. List positive coordinate runs of at most H owners. Their repair
   intervals include the insertion edge, internal edges, and removal
   edge. On each cycle with such intervals, choose an edge in one
   interval and cut there. Hit the remaining line intervals by the
   greedy right-endpoint algorithm. This uses at most twice the maximum
   number of disjoint repair intervals on that active cycle.

3. On each resulting path X_0,...,X_(v-1), extend X constantly beyond
   both endpoints. Output the v+H nonempty subset letters

       D_i = intersection_(j=0)^H X_tilde_(i+j),  -H<=i<=v-1.

   On a cycle needing no cuts, output the cyclic version and repeat
   its first 2H letters. This is the endpoint-capped erosion construction
   in Section 22 of the residence note.

4. At each cut use the ORIGINAL cyclic owners to form

       P_(s,t) = intersection_(i=-s)^(t-1) X_i,  1<=s,t<=H.

   Record the capped positive extents (u_x,v_x) of each coordinate
   present on both sides. Join their Pareto-minimal points by the
   east-before-south unit path from (1,H) to (H,1), and emit P_(s,t)
   at its 2H-1 vertices. Then emit X_(-H),...,X_(H-1). These two words
   restore crossing lower and upper targets. Section 24 and
   `MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md` give the
   formulas and proof.

5. Append the product symmetric-chain tail word. On two r-coordinate
   halves, take standard symmetric-chain decompositions. For each
   chain pair C,D with minimum ranks a+b<=r-H, concatenate C's reversed
   increment word and D's forward increment word. Lift this tail word
   to 2r+1 coordinates by the rule below. The complete recipe is in
   `MATH_THEOREM_O_PRODUCT_SCD_TAIL_MIXED_CYCLE_INTERFACE_20260726.md`,
   Sections 1 and 2.

6. Concatenate all blocks and retain the shortest output among the
   finitely many H candidates. Each witness stays inside its block.

For small dimensions with no admissible H, use a direct complete word,
for example listing all nonempty subsets. No running-time claim is made.

Trying every H avoids needing the nonexplicit thresholds in the
asymptotic proof: the shortest candidate is no longer than the one chosen
by its slow diagonal. This is a finite selection rule, not a rate estimate.

## 2. Even dimensions

For a complete word Q_1,...,Q_N on the preceding odd dimension, add a
new coordinate z and output

    Q_1,...,Q_N, {z}, Q_1 union {z},...,Q_(N-1) union {z}.

This has 2N letters. Old witnesses remain in the first copy. Witnesses
with z use the last block or an old suffix followed by {z}.

## 3. The actual construction at k=17

The current verified finite bounds are

    24,313 <= nu(17) <= 24,658.

The user-supplied `answers/k17_upper24658.word` has exactly 24,658 nonzero
letters and covers all 131,071 nonempty targets. Its SHA-256 is

    24f7f831b7446e942cc0927472296b2d20069f694b8bbad6374e65cc07b6f7fb.

The independent checker `scripts/verify_k17_upper24658.py` enumerated all
suffix ORs and then rechecked one ordinary, nonwrapping interval witness
for every target using a separate segment-tree range-OR calculation.
Its PASS report and all 131,071 witnesses are saved in
`witnesses/k17_upper24658/literal24658_verification.json` and
`witnesses/k17_upper24658/literal24658_target_witnesses.json`.

The endpoint lower bound remains 24,313, leaving a gap of 345. The word is
not claimed optimal. Its supplied literal body is verified; the user's
rewrite/search regeneration procedure was not supplied or independently
verified. This record does not attribute that unavailable procedure to
the independently implemented recipes below.

The preceding supplied `answers/k17_upper24715.word` remains unchanged,
with SHA-256

    3e7da8c69f8d32ca73750e12b8746fc483f9d56a441ad94f1d3a2e9b4c11b2fe.

It too is a verified universal word, with its literal report and all
target witnesses in `witnesses/k17_upper24715/`. Its regeneration
procedure was not supplied. The newer word improves its length by 47.

### Implemented height-adaptive construction and its forest repair

The implemented height-adaptive construction outputs
`answers/k17_upper24957.word`. It has exactly 24,957 nonzero letters,
covers all 131,071 nonempty targets, and has SHA-256

    dc7c7af32feb73c91fd14e00c6a046de6d753af4d2fc632f71960dcdbdd820db.

Its finite deterministic recipe is:

1. Enumerate the canonical rank-eight lower-owner cycles under f^2. Open
   each at its least integer mask, keep the forward orientation, and order
   the cycles by those initial masks. There are 146 cycles; their invariant
   Dyck heights h sum to 519.
2. Complement to rank-nine owners X_i. On each cycle form the nonempty
   source period D_i=intersection_(j=0)^h X_(i+j), with cyclic indices.
3. Emit each period followed by its first h letters and concatenate in
   the fixed order. This gives 24,829 letters. Exact enumeration finds
   128 missing targets: 65 of rank ten, 49 of rank eleven, and 14 of rank
   twelve.
4. Append all 128 missing masks as individual letters in increasing order.
   Every old interval witness is retained, and each missing target obtains
   its own length-one witness. The result has length 24,957.

No alternative cut, component ordering, or selected repair search was used.
Repeating the first 2h-1 letters at step 3 instead produces a directly
verified universal word of length 25,202, without a missing-target repair.
The generator is
`scratch/verify_k17_height_adaptive_fixed_construction_20260908.py`.
The complete proof, canonical component data, three literal words, and
all target witnesses are recorded in
`scratch/K17_HEIGHT_ADAPTIVE_25202_AND_REPAIRED24957_EXACT_CERTIFICATE_20260908.md`
and `scratch/k17_height_adaptive_20260908/`.

The separate literal checker `scripts/verify_k17_upper24957.py` enumerates
all suffix ORs and rechecks every target witness using a segment-tree
range-OR calculation. Its report and all 131,071 ordinary, nonwrapping
witnesses are saved in
`witnesses/k17_upper24957/literal24957_verification.json` and
`witnesses/k17_upper24957/literal24957_target_witnesses.json`.

The 24,957-word is independently constructed and verified. The user's
reported 24,969-word with 140 holes was not supplied and is not claimed
verified: opening cuts and component order can change the holes covered
by intervals crossing blocks. The fixed convention above yielded 128.

The 24,957-word saved 417 letters relative to the 25,374-word and 788
relative to the 25,745-word. It is retained unchanged for provenance.

A subsequent exact binary-forest construction keeps its 24,829-letter
prefix unchanged and replaces the 128-letter repair by 118 letters. Among
the 128 holes there are exactly 56 strict pair-union decompositions and
only ten possible parent targets. Ten simultaneously compatible pairs
attain all ten parents. Their depth-first leaf word covers every hole;
118 is therefore optimal within this fixed-hole binary-forest model.
This is not an optimality claim for unrestricted repairs or universal words.

The resulting universal word has length 24,947 and SHA-256

    a358c7d539ea8af286c61a45f621b7d9bc1227c292829ea3bb981acd1f975389.

It and all 131,071 independently replayed target witnesses are retained in
`scratch/k17_height_adaptive_20260908/binary_forest_repair/`, with full word
`k17_height_forest24947.word`. The exact model, ten pairs, optimality proof,
and bounded optimization/verification record are in
`scratch/K17_HEIGHT_ADAPTIVE24947_OPTIMAL_BINARY_FOREST_REPAIR_20260908.md`.
Both this intermediate construction and the original 24,957-word remain
separate from the supplied best 24,658-word.

### Earlier verified words and construction provenance

The retained user-supplied `answers/k17_upper25374.word` has exactly 25,374 nonzero
letters and realizes all 131,071 nonempty targets. Its SHA-256 is

    16951cef9e2efff841c6bbf9cc72f2061f35650dda850714fcceee7a7bb43208.

The independent checker `scripts/verify_k17_upper25374.py` enumerated all
suffix ORs and then rechecked a literal ordinary, nonwrapping interval
witness for every target with a separate segment-tree range-OR calculation.
Its PASS report and all 131,071 witnesses are saved in
`witnesses/k17_upper25374/literal25374_verification.json` and
`witnesses/k17_upper25374/literal25374_target_witnesses.json`.

This is verification of the supplied literal word. It does not verify the
construction search's intermediate or Hall-count claims, establish that
25,374 is optimal, or implement the coefficient-one PBBS recipe above.

The earlier `answers/k17_upper25745.word` is retained unchanged as a
25,745-letter construction with its own source-only proof. Its saved
independent exhaustive verification reports all 131,071 nonempty targets
covered, zero missing. It is an earlier boundary splice, not an output
of the new coefficient-one PBBS analysis.

Using `answers/k16.word` as the Python list X, its exact recipe is

```python
Y = X[1:][::-1] + [65536, 50122, 33642] + [x | 65536 for x in X[3:]]
```

Each integer encodes a subset; bit j represents coordinate j+1. Targets
are bitwise ORs of nonempty contiguous, nonwrapping intervals. The
generator and source-only proof are in
`scripts/k17_boundary_splice_20260906_b7e41_audit.py`.

The earlier review package includes the source k=16 word, the 25,745-letter
word, its generator, independent verifier, and saved verification in its
`finite_construction` directory. The later 25,374-, 24,957-, 24,947-,
24,715-, and 24,668-letter words and their verification are recorded separately at the
paths above.
The older `answers/k17_upper25746.word` is also retained unchanged for
provenance.

At r=8, the earlier uniform-cutoff PBBS ledger has four admissible H choices. Even dropping
its nonnegative packing term, the right-hand sides are 97,786; 94,374;
81,106; and 62,910. Thus that ledger cannot certify a better k=17 word.
These figures do NOT lower-bound all words or constrain the different
height-adaptive construction above. See `scratch/PBBS_K17_FINITE_COMPILER_LEDGER_20260908.md`
for the exact remote calculation and its scope.

## 4. Comparison with the user's new coefficient 1.15325

The user's endpoint-partition argument claims
nu(k)<=(1.15325+o(1))W(k). This is the same full-cube leading coefficient
as our proposed nu(k)=(1+o(1))W(k). If the coefficient-one proof is
correct, it is asymptotically stronger and optimal in its leading
coefficient. It does not imply exact equality nu(k)=W(k), or replace a
verified finite word at k=17.

The new 1.15325 argument has not been independently audited here.
The supplied labels for its proof and verifier contained no accessible
paths or URLs; no claim is made to have run that external verifier.
