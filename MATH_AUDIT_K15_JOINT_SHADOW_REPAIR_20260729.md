# k=15 joint upper-q1 / lower-q3 repair audit

Date: 2026-07-29

Authoritative inputs:

- `scratch/fixtures/k15_residence_hint_explicit_v1.json`
- `scratch/k15_residence_seed_upper_repair.audit.json`
- `scratch/graded_quotient_pipeline.py`

Reproducer:

```text
python3 scratch/audit_k15_joint_shadow_repair.py
```

Machine-readable output:

- `scratch/k15_joint_shadow_repair.audit.json`
- `scratch/fixtures/k15_joint_q1_q3_scaffold_hint_v1.json`

## Result in one sentence

The minimum 67-change upper-q1 scaffold unexpectedly completes 8 of the 11
missing lower-q3 orbits; exactly two further selector changes complete the
remaining three while preserving all upper-q1 colours, giving a 69-change
joint shadow scaffold.  It is not yet a carrier: degree balance alone forces
at least 40 further changes from that scaffold.

## 1. Unconditional Hamming lower bound

The resident strict carrier misses 67 upper-q1 orbit colours.  An unchanged
lower-orbit choice cannot introduce one of these colours, and one changed
choice introduces at most one colour.  Therefore every exact carrier covering
upper q1 has Hamming distance at least

\[
  R\ge 67
\]

from the resident seed.  This remains the rigorous global lower bound after
adding residence, degree two, connectivity, voltage, and lower-q3 constraints.

The capacitated upper repair realizes this lower bound at the selector level:
67 changes cover all 67 missing upper colours without deleting the last copy
of an old colour.

## 2. Exact q3 support statistics

For each missing rank-5 orbit representative, every possible three-edge
carrier motif was enumerated.  `overlap j` means that exactly `j` of its three
choice IDs occur in the indicated selector.

| target | motifs | seed overlap 2 | scaffold overlap 2 | scaffold overlap 3 | new scaffold choices in any motif |
|---:|---:|---:|---:|---:|---:|
| 157 | 123480 | 282 | 337 | 2 | 11 |
| 285 | 123480 | 295 | 321 | 2 | 8 |
| 651 | 123159 | 244 | 293 | 1 | 8 |
| 661 | 122865 | 277 | 352 | 2 | 5 |
| 665 | 123186 | 307 | 309 | 1 | 7 |
| 837 | 123159 | 286 | 379 | 3 | 8 |
| 1187 | 122869 | 308 | 326 | 2 | 5 |
| 1233 | 123186 | 302 | 310 | 2 | 4 |
| 1349 | 122899 | 275 | 272 | 0 | 4 |
| 1585 | 120150 | 269 | 256 | 0 | 3 |
| 2329 | 122872 | 346 | 346 | 0 | 0 |

Thus a repair chosen using only upper-q1 information already does the
following:

- 41 of its 67 new choices occur in at least one missing-q3 motif;
- 15 new choices occur in a completed q3 witness;
- 14 individually close a motif whose other two choices are retained;
- 8 of 11 missing q3 orbits become covered;
- only `1349`, `1585`, and `2329` remain.

The last line of the table is especially diagnostic: none of the 67 new
choices even lies in a q3 motif for target `2329`.  Its failure is a genuine
blind spot of the q1-only matching, not a near miss in orientation.

## 3. Exact local extension of the fixed scaffold

Around the fixed 67-change scaffold, enumerate every one-choice replacement
that closes a motif with two already selected choices and preserves all
upper-q1 colours.

- There are 357 such q1-safe actions touching a remaining target.
- One action can hit at most two of the three remaining targets.
- Consequently one further action cannot finish the q3 gate.
- There are 829 exact q1-safe two-action pairs that preserve an existing or
  newly completed witness for all 11 q3 targets.

The lexicographically best pair under degree-shortage, number of bad-degree
vertices, and degree L1 is

```text
choice 5380 -> 5389  (lower orbit 1893): completes q3 target 1349
choice 9314 -> 9299  (lower orbit 3275): completes q3 targets 1585 and 2329
```

Both removed upper colours retain another copy.  The resulting selector is at
Hamming distance 69 from the resident seed, covers every upper-q1 orbit, and
has exact q3 witness counts

```text
157:2  285:2  651:1  661:2  665:1  837:3
1187:2  1233:2  1349:1  1585:1  2329:1
```

This proves that, once degree/connectivity/residence are temporarily relaxed,
the q1 and q3 demands are almost perfectly aligned: only 2 changes beyond the
sharp q1 minimum are needed.

## 4. Why the scaffold is only a hint

The 67-change q1 scaffold has quotient degree histogram

```text
degree 0:3, 1:72, 2:283, 3:65, 4:5, 5:1.
```

It has 78 shortage units and 78 excess units.  A same-lower choice replacement
can move at most two incidence units from excess vertices to deficient
vertices, so at least 39 additional replacements are required to reach degree
two from this scaffold.

The 69-change joint scaffold has histogram

```text
degree 0:4, 1:71, 2:283, 3:64, 4:6, 5:1.
```

It has 79 shortage units, hence is at least 40 choice replacements from any
degree-two selector.  These are rigorous scaffold-centred lower bounds.  They
do not add to the global 67 bound relative to the resident carrier, because a
true solution can choose a different set of 67+ changes.

## 5. Compact exact optimization model

The right joint model is already expressible with the quotient catalogue and
does not need the roughly 1.35 million explicit q3 motif clauses.

Use a Boolean `y_a` for every directed quotient arc and `x_c` for every
undirected choice.

1. `AddCircuit` on the 429 central necklace vertices.  This enforces degree
   two and quotient connectivity.
2. Link `x_c` to its two possible directed arcs and select exactly one choice
   for each lower central orbit.
3. Require unit voltage, `gcd(v,15)=1`, so the quotient circuit lifts to one
   physical cycle of length 6435.
4. Use the existing age automaton to forbid deletion at ages 1, 2, or 3;
   equivalently every positive coordinate run has length at least 4.
5. For every upper-q1 orbit `U`, impose
   `OR{x_c : upper_colour(c)=U}`.
6. For each of the 11 rank-5 targets, introduce four central-state variables
   and three directed-arc-index variables.  Each state ranges over the 120
   rank-8 supersets of the target.  Allowed-transition tables plus
   `Element(arc_index,y,1)` enforce one selected three-edge path whose four
   states intersect exactly in the target.
7. Bound or minimize

   \[
     R=429-\sum_{c\in F_{\rm resident}}x_c.
   \]

This is precisely the `AddCircuit + age automaton + upper1 +
shadow-state-path` model in `graded_quotient_pipeline.py`.  It preserves
degree two and residence inside the solver instead of trying to repair them
afterward.

## 6. Recommended bounded searches

No additional heavy job was launched for this audit.  When CPU capacity is
available, use two complementary centres.

### Valid resident-cycle centre

This supplies both choice and directed-arc hints.  Seed all 11 q3 cuts (and
the existing q2/upper cuts) eagerly.

```text
R = 80, 96, 120
```

Use `R=67` separately as the decisive exact-bound feasibility test; if it is
UNSAT, increase through 72 and 80.  The 69-change relaxed construction makes
80 a reasonable first solution-seeking radius while leaving 11 changes for
structural reconciliation.

### Joint q1/q3 selector centre

Use `scratch/fixtures/k15_joint_q1_q3_scaffold_hint_v1.json`.  It has no arc
hint, and the degree count proves

```text
R >= 40
```

around this centre.  Suggested radii are

```text
R = 48, 64, 96.
```

This second centre tells CP-SAT where the two shadow systems meet; the first
centre tells it where the exact circuit and residence live.  A portfolio using
both is better justified than increasing an unstructured global timeout.

## 7. Scope

This audit closes neither lower q2 nor upper depths q>=2, and it does not
produce a k=15 word.  Its contribution is narrower and exact:

1. the live q1/q3 neighbourhood is quantified;
2. the sharp global Hamming lower bound is 67;
3. a 69-change joint shadow scaffold exists;
4. the remaining structural distance of that scaffold is bounded below;
5. the next solver instances and their meaningful radii are now specified.

