# Audit of Claude's latest ledger, construction note, and `cword.py`

Date: 2026-07-29

Audited upstream files:

```text
/Users/amir.nuriyev/Downloads/opusproblem/work/LEDGER.md
/Users/amir.nuriyev/Downloads/opusproblem/work/GENERAL_CONSTRUCTION.md
/Users/amir.nuriyev/Downloads/opusproblem/work/cword.py
/Users/amir.nuriyev/Downloads/opusproblem/work/movecover.py
```

This is a proof-scope audit, not a search transcript.  No heavy local solve
was run.

## 1. Claims that are mathematically sound

### 1.1 Single-trace strict-spiral normal form

For a connected strict unit-voltage spiral, one cyclic binary trace `c`
determines the whole carrier by

\[
 T_i=\{t:c_{i-tN}=1\}.
\]

Multiplying coordinate labels by a unit gauges any unit voltage to one.
The following eager conditions are exact within this strict-spiral class:

1. class sum `r` in every residue modulo `N` gives `|T_i|=r`;
2. one run start and one run end in each residue class gives exactly one
   insertion and one deletion at every physical seam;
3. minimum cyclic positive-run length `d+1` is residence; and
4. pairwise rotation-inequivalent columns are exactly the Hamilton/one-copy
   condition.

The first three imply Johnson adjacency and the correct q1 rank.  They do
not imply middle-orbit or q1-colour distinctness; `cword.py` correctly audits
and cuts those lazily.

The start/end-permutation plus length/gap composition parametrization is a
valid rewriting of the same normal form.  The remaining q2 and upper
conditions really are constraints on those permutations and lengths.

### 1.2 Published undecorated base

The Merino--Micka--Mutze projection supplies the undecorated strict spiral
with perfect first lower rainbow for every odd `k` and unit voltage.  It does
not supply residence, q2, or upper decoration.  The ledger states this
distinction correctly.

### 1.3 Positive-output soundness of `cword.py`

The exact eager constraints and the two persistent collision cuts are sound:

* `diffcut` requires two collided middle columns to differ somewhere;
* `q1diffcut` requires two collided intersection columns to differ somewhere.

The cover selectors are capped at 150 and are therefore a sufficient
strengthening, not an exact cover encoding.  The driver correctly treats an
UNSAT result containing such cover rows as inconclusive and drops those
rows.  A literal `PASS` is sound because the physical audit recomputes every
gate without using the selector bookkeeping.

An UNSAT result after **all** capped covers are removed is a nonexistence
certificate only for this strict run-transversal `c`-space, not for arbitrary
factors or arbitrary optimal words.

### 1.4 Finite positive calibrations

The work directory retains a `k=9` cyclic-gate PASS and an independently
checkable length-128 word.  These are useful calibrations of the strict
spiral architecture.  They do not prove the all-`k` decoration statement.

## 2. Claims that are conditional or overstated

### 2.1 A compiler model is not a universal feasibility theorem

The sentence

```text
Given ANY gate-passing k=15 carrier [sandwich2] emits the 6438 word
```

is not proved by the cited evidence.  `sandwich2.py` is an exact SAT
formulation and has positive `k=11,13` calibrations.  That proves its model
and those instances, not feasibility for every decorated carrier.  Likewise
`construct.py` uses backtracking; it is not an unconditional polynomial-time
constructor.

The one-core theorem is explicitly conditional on Hall.  The universal
bit-level compiler may use lower-row hosting beyond the one-core face, but no
theorem in the upstream note proves that its SAT instance is always
satisfiable from residence+q2+upper decoration alone.  Therefore the safe
implication is

\[
 \text{decorated carrier} + \text{compiler/Hall PASS}
 \Longrightarrow \text{word},
\]

not decorated carrier alone.

This also resolves an internal tension in `GENERAL_CONSTRUCTION.md`: it says
terminal q3 is entirely compiler-side, but later observes that rank-`h`
targets force q3-envelope surjectivity on the special one-core face.  In the
larger bit-level model q3 may be repaired by other rows, but that is an exact
instance question until a general feasibility theorem is proved.

### 2.2 The all-odd decorated spiral remains conjectural

The two-permutation design is a valuable exact target, not its own existence
proof.  Random-probe statistics, the k7 census, and the k9/k11 examples are
evidence only.  The odd general construction and the even two-layer braid
remain open.

### 2.3 The latest `k=15` strict-spiral lane has no PASS

The ledger reports improved first-round miss counts and several active
search configurations, but the live folder contains no new `k=15` PASS,
compiled word, or independently replayed upper-bound improvement.  The
actionable output is its smaller exact search coordinate system, not a new
answer.

## 3. Code-level qualifications

1. `cword.py` calls `solver.Solve(m)` twice in succession in window-LNS.
   This merely wastes the first solve; it should be deleted.
2. `--runbound` assumes a seed/anchor but the CLI does not fail early when
   it is omitted.
3. The duplicated `m.Minimize(sum(diffs))` call is harmless but redundant.
4. Upper cover templates inspect only a few widths and only the 150 cheapest
   selectors.  Positive candidates remain sound; negative conclusions do
   not.
5. `movecover.py`'s upper-delta window is not proof-safe.  It sets
   `REACH=max(number of rank changes in a closure)+2`, whereas an upper union
   may stall for arbitrarily many carrier steps between rank changes.  A
   changed column can therefore alter witnesses whose starts lie farther
   back than `REACH`.  Its final full `CWord.audit` protects positive output,
   but the claimed exact `OPTIMUM=0` move-family no-go is not certified by
   that delta model.  The k9 positive calibration cannot validate a negative
   IP conclusion.

The last issue is the main new defect found in this audit.

## 4. Stale statements

The upstream ledger still gives `nu(15)<=6459`.  The retained rigorous bound
in the main repository is

\[
 6438\le\nu(15)\le6458.
\]

More importantly, the main repository has now gone beyond the ledger's
carrier status.  The independently audited factor

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    u2u3l3_s801.engine.json
```

has cyclic minimum run four, exact middle/lower q1, complete lower q2/q3,
and complete upper coverage at every rank.  It has nine physical components.
Thus the live bottleneck is no longer finding simultaneous decorations in an
arbitrary factor; it is opening/splicing those nine components and passing
the exact compiler.  The strict connected-spiral conjecture remains useful
for the general theorem, but it is no longer the shortest finite route to
`k=15`.

## 5. Actionable conclusions

1. Keep `cword.py` as the compact lane for the all-odd strict-spiral
   conjecture; do not infer global nonexistence from its negative searches.
2. Fix the duplicate LNS solve and replace `movecover` upper deltas by literal
   interval-witness recomputation before retaining any negative certificate.
3. Do not spend the immediate `k=15` budget on the stale 47/95 strict seed.
   The nine-cycle all-shadow factor is strictly closer.
4. Solve its exact special-cell seam Hall problem, residence collars, and
   witness-survival condition as stated in
   `K15_NINE_CYCLE_ALL_SHADOW_FACTOR_OPENING_SEAM_THEOREM_20260729.md`, then
   run the exact compiler and full OR verifier.
