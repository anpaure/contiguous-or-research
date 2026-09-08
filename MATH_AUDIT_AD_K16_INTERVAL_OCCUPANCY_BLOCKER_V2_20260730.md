# Adversarial audit: K16 interval-occupancy/blocker v2

Date: 2026-07-30  
Lane: AD independent audit  
Status: mathematical encoding **PASS**; emitted-map ledgers **PASS**;
positive decoding **sound**; frozen-provenance fail-closedness **needs two
repairs**; no solver was run

## 1. Frozen files and scope

The audited sources are

```text
MATH_THEOREM_AD_K16_INTERVAL_OCCUPANCY_BLOCKER_COMPRESSION_20260730.md
SHA-256 7ffa70336bec21ea2ecd9c6af5625e5dedb30ab6fd152c5d8dd5746e54390509

scratch/build_ad_k16_12873_occupancy_blocker_cnf_20260730.py
SHA-256 71345c82e64a4d9fff1d24f6d14fe154dd8348eaa0fcda73de205480ef5fe063

scratch/decode_verify_ad_k16_12873_occupancy_blocker_cnf_20260730.py
SHA-256 2626ef26421cfa349548030692c69a8a5e2d56b0e54851915c02270f6aedbaad
```

This audit inspected the theorem, emitter, decoder, and four retained map
files.  It did not run SAT/CP-SAT, emit another CNF, or claim a profile
verdict.

## 2. One-block and one-run semantics: PASS

For a target \(T\), the global occupancy ALO gives at least one occupied
cell.  Every occupied cell in block \(j\) forces \(g_{T,j}\), while the
three pairwise block-control AMO clauses forbid occupancy in two blocks.
Consequently exactly one block contains the support.  The occupied block's
control is true and the other controls are false; no control ALO is needed.

Inside a width-\(w\) block, put

\[
 s_0=a_0,\qquad s_i=\neg a_{i-1}\wedge a_i\quad(1\le i<w).
\]

The emitter clause for starts \(i<j\), \(j\ge i+2\), is exactly
\(\neg s_i\vee\neg s_j\).  Two distinct runs have start indices separated
by at least two.  Conversely, adjacent start events are logically
inconsistent, so omitting their clauses loses nothing.  Thus the support is
one nonempty run in one block.

The number of run-start rows is

\[
                         \binom{w-1}{2}.
\]

This gives

\[
\begin{array}{c|c}
(4,9,4)&57(3+28+3)=1938,\\
(5,8,4)&57(6+21+3)=1710,\\
(5,9,3)&57(6+28+1)=1995.
\end{array}
\]

In particular the width-three contribution in the last profile is one,
and the current theorem/emitter use the corrected value.

## 3. Endpoint signatures: PASS

For \(I=[f,\ell]\), the signature uses positive occupancy at its endpoint
or endpoints and negative occupancy at each existing immediate exterior
neighbor.  Under the one-run theorem:

* the actual support interval makes its signature true;
* a strict subinterval fails an exterior-neighbor literal;
* a strict superinterval fails an endpoint literal; and
* an interval in an inactive block fails an endpoint literal.

The singleton case correctly omits the duplicated endpoint.  Full-block,
left-boundary, and right-boundary intervals correctly omit only nonexistent
exterior neighbors.  Lines 267--283 of the emitter form the literal
disjunction \(\neg\Sigma_I\) and append the relevant durable literals, so
exactly the actual support's rows activate.

## 4. Blocker and durable equivalence: PASS

For every occupied target/cell pair, the emitter forces a blocker for every
coordinate omitted by the target.  Therefore a false blocker certifies that
all active targets contain that coordinate.  The 17 common-coordinate rows
make every active-target intersection nonzero; an unused cell may set all
blockers false.

For the unique support interval of \(T\), each coordinate in
\(T\setminus b_T(I_T)\) receives a point with a false blocker.  Hence it
belongs to the active-target intersection at that point.  Assigning every
used cell its active-target intersection and an unused cell the frozen live
sentinel `0x0001` is exactly the canonical construction in the imported
chart-intersection theorem.  Overstated blocker bits can only strengthen the
formula and cannot create a false positive.

Conversely, any literal feasible chart selection supplies one-run
occupancies, the occupied block control, and the minimal blocker assignment.
Thus the theorem and emitter are iff-exact, not a Hall or marginal
relaxation.

## 5. Exact variables and clauses: PASS

The variable partition is

\[
 57\cdot17=969\text{ occupancies},\qquad
 57\cdot3=171\text{ block controls},\qquad
 17\cdot16=272\text{ blockers},
\]

for 1,412 variables.  The common rows are

\[
 57+969+171+7616+17,
\]

where

\[
 7616=17\sum_{T\in R}(16-|T|)=17\cdot448.
\]

Adding the profile run rows and the audited maximal-context durable rows
gives

\[
\begin{array}{c|c}
(4,9,4)&57+969+171+1938+7616+28292+17=39060,\\
(5,8,4)&57+969+171+1710+7616+26442+17=36982,\\
(5,9,3)&57+969+171+1995+7616+28695+17=39520.
\end{array}
\]

The four retained maps replay as follows:

| map | byte SHA-256 | charts | durable | clauses |
|---|---|---:|---:|---:|
| `4_9_4_anchor6436` | `8672d9248aee5ffe5bd9e33d822696f228afbeb0488f1203628a0c98c765e932` | 3705 | 28292 | 39077 |
| `4_9_4_anchorany` | `42d2cec5de6bc739ba4a5fb7260f245c9111f0bef2f1e5e133e062526ad885d7` | 3705 | 28292 | 39196 |
| `5_8_4_anchorany` | `f4fbcac08aa283196650aec8fa688e834b53e37922a5274ed17c032d75af15c0` | 3477 | 26442 | 37118 |
| `5_9_3_anchorany` | `5604115173b4ae3a86fce6017add266b2bff2463fc7684865ad39122fa89b70e` | 3762 | 28695 | 39656 |

For each map, independent lightweight replay verified its stable payload,
the exact variable partition `1..969`, `970..1140`, `1141..1412`, unique
chart keys, consecutive chart flats, and the displayed durable sum.  The
fixed branch adds 17 unit clauses; each anchor-any map adds
\(\binom{17}{2}=136\) clauses.  No local CNF bytes or solver transcript were
present in this audit, so no CNF-byte or solver verdict is inferred from the
maps.

## 6. Anchor modes: PASS

In any literal witness of \(H=\mathtt{8000}\), every nonzero variable cell
is a submask of the singleton-bit target and is therefore exactly \(H\).
Choosing any one such cell as a singleton witness is safe.  More explicitly,
start from the feasible physical word, retain every other chosen witness,
and replace only the chosen \(H\)-chart by that singleton.  Removing the old
extra \(H\)-occupancies relaxes active intersections and blockers; it cannot
destroy another target's durable point.  Hence singleton-anchor branching
is WLOG.

Pairwise AMO on the 17 \(H\)-occupancies plus their existing ALO gives the
complete anchor-any model.  Seventeen signed unit clauses give an exact
fixed-position singleton.  The union of the 17 fixed branches is the
anchor-any model's feasible set.

## 7. Decoder: positive-sound, but not provenance-fail-closed

The decoder's mathematical positive path is sound:

1. it requires a complete, noncontradictory SAT assignment;
2. it checks every DIMACS clause under that assignment;
3. it independently checks one occupied block and one consecutive interval
   for every target;
4. it reconstructs canonical active-target intersections;
5. it verifies every selected maximal-context chart exactly; and
6. most decisively, it performs a fresh start-by-start literal OR replay of
   the final 12,873-letter word and rejects any hole.

Therefore every ordinary `PASS_LITERAL_UNIVERSAL` execution certifies an
actual universal word, even independently of the compact-model proof.

Two operational defects prevent calling the current bundle fully
fail-closed for frozen provenance.

### Finding 7.1 (map authenticity is self-asserted)

At decoder lines 149--160, the map is checked only against a payload hash
stored inside that same mutable map, the answer hash, the emitter hash
string stored in the map, and the CNF hash stored in the map.  The decoder
does **not** pin or reconstruct:

* the core source/audit hashes and payload;
* the chart and occupancy theorem hashes;
* the canonical profile/delete/block/position tuple;
* the exact 57-target list;
* the variable-row partition and uniqueness;
* the exhaustive chart ledger, bases, flats, and required bits; or
* the expected profile/anchor dimensions.

It also accepts no operator-supplied frozen map/CNF/payload hashes.  Thus a
different self-consistent map/CNF pair can pass the provenance checks after
rewriting its own payload fields.  Final literal replay still prevents a
false **word** certificate, but the resulting audit would not prove that
the word came from the named frozen occupancy instance or anchor branch.

Required repair: either reconstruct the full map from the pinned answer,
core, profile, and theorem sources, or require externally frozen map, CNF,
and payload hashes and additionally validate all canonical structural
fields.  At minimum the hard-coded constants already present in the emitter
must be checked against the corresponding metadata rows.

### Finding 7.2 (output aliases are not rejected)

Emitter lines 143--146 reject existing output files but do not reject
`--cnf` and `--map` resolving to the same new path.  In that case the map
atomically replaces the just-written CNF.

Decoder lines 142--143 likewise do not reject `--candidate` and `--audit`
resolving to the same new path.  The audit JSON then replaces the verified
candidate word while the decoder prints success.

These are artifact-integrity failures, not Boolean-encoding errors.  Both
programs should compare resolved output paths before writing, as the older
fixed-gap emitters/decoders already do.

Additional structural checks are advisable even after hash pinning: reject
duplicate target rows and duplicate chart keys, require exact variable
ranges, require `positions` to equal the flattened canonical blocks, allow
only the three named profiles and three named anchor modes, and require
exact anchor-mode clause counts.

## 8. Verdict and exact boundary

The one-run encoding, endpoint signatures, blockers, durable rows, corrected
`(5,9,3)` arithmetic, and singleton-anchor completeness all pass.  The
1,412-variable theorem and emitter are exact.

The decoder is positive-sound because its final literal replay is decisive,
but the present hash/payload checks do not authenticate the map as the
output of the frozen emitter, and output aliases are not rejected.  No SAT
artifact should be canonically promoted under a profile/anchor provenance
claim until those two fail-closed defects are repaired or the exact
map/CNF hashes are independently frozen and checked outside the decoder.

No SAT or UNSAT conclusion follows from this audit.
