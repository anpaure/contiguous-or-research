# Meet-value rigidity for the canonical `q=369` schedule

## 0. Answer to the central question

> Can the 1011 automatic bulk meet cells and twelve localized reservoir
> cells be organized together with an upper-complete mixed-run rank-6
> braid?

**No, in the exact-meet reading; yes remains possible, but only in a
corrected reading with a new forced coverage law.**

Precisely:

1. **Theorem 1 (over-production obstruction).**  Requirement 2 as stated
   — the 1011 nontrivial feasible consecutive **intersections** realized
   as 1011 distinct lower masks — is unsatisfiable for every rank-6
   permutation.  At least 438 consecutive triple intersections are then
   forced to be **distinct masks of rank exactly four** (456 if the
   reservoir rank caps of requirement 4 are added), but only
   `C(11,4)=330` rank-four masks exist.  This
   kills the maximal-factor/sparse-repair route of
   `SINGLE_SWITCH_MAXIMAL_SHADOW_THEOREM.md`, Corollary 3.3 and
   Theorem 3.6, at `k=11`, and likewise at `k=9` (114>84) and `k=14`
   (2562>2002), and at every central rank (Section 9).
2. **Theorem 2 (corrected value rigidity).**  In any actual universal
   465-entry word whose selected rank-6 witnesses follow the `q369`
   schedule, short-cell saturation is forced, and the cell **values** obey
   an exactness ladder: rank-5 cells are exact adjacent intersections,
   rank-4 cells are exact triple intersections, rank-3 late singletons are
   exact quadruple intersections.  Deep cells may carry **proper subsets**
   of their intersections; that freedom is what Theorem 1 removes from the
   exact-meet route and what the true `k=9` optimum uses.
3. **Theorem 3 (D3-coverage law).**  The corrected necessary condition on
   the central row is new: the consecutive triple intersections
   `C_p ∩ C_{p+1} ∩ C_{p+2}` must cover at least **323 of the 330**
   rank-four masks.  The row is forced to be a cut middle-levels object
   (two facet-rainbow Johnson arcs of 369 and 93 vertices with a free
   seam), recovering exactly the `ML_11` cut-cycle geometry of
   `K11_PORTAL_EMBEDDING_MATH_NEXT.md`, Section 8, now **derived as
   necessary** rather than proposed.

The remaining open lemma is stated exactly in Section 8.  Nothing here
changes `nu(11)`: length-465 words remain possible in the corrected
reading, and the `q369_schedule` SAT branch (which imposes only the
schedule, not exact meets) is unaffected.

## 1. Setting and conventions

`k=11`, `r=6`, `M=462`, `d=3`, `L=1023`, `sigma=369`, `n=465`.  Selected
central witnesses

    I_i=[i,i+2] (1<=i<=369),   I_i=[i,i+3] (370<=i<=462),

with distinct rank-6 values `C_i`.  Write `A_j` for entries,
`B_j=OR[j,j+1]`, `T_j=OR[j,j+2]`, and for the set intersections

    D2(p)=C_p∩C_{p+1}            (1<=p<=461),
    D3(p)=C_p∩C_{p+1}∩C_{p+2}    (1<=p<=460),
    D4(p)=C_p∩...∩C_{p+3}        (370<=p<=459).

The 1011 nontrivial meet cores are, as physical cells:

    early p=1..369:  pair [p+1,p+2]=B-cell,  singleton [p+2];
    late  p=370..461: triple [p+1,p+3]=T-cell;
    late  p=370..460: pair [p+2,p+3];
    late  p=370..459: singleton [p+3].

Counts: `369+369+92+91+90=1011`.  The twelve excluded short cells are
exactly the audited reservoir:

    A_1,B_1,A_2;  T_370,B_371,A_372;
    A_463,A_464,A_465,B_463,B_464,T_463.

All of this matches `SINGLE_SWITCH_MAXIMAL_SHADOW_INDEPENDENT_AUDIT.md`,
Section 8, cell for cell.

## 2. Theorem 1: the exact-meet reading over-produces rank four

> **Theorem 1.**  There is no choice of 462 distinct rank-6 masks
> `C_1,...,C_462` for which the 1011 nontrivial feasible consecutive
> intersections `D2(1..461), D3(1..460), D4(370..459)` are pairwise
> distinct masks covering all but twelve of the 1023 lower masks.
> Hence requirement 2 of the q369 target, read as a statement about the
> set intersections (equivalently, about the maximal factor's meet-cell
> values, by Theorem 2.1 of the maximal-shadow theorem), is
> unsatisfiable.  No mixed-run, upper, reservoir, or pin condition is
> needed for the refutation.

**Proof.**  Assume such a row.  All 1011 intersection values are distinct
by hypothesis.

*Step 1 (rank-5 masks live only at depth two).*  `D3(p) ⊆ D2(p)` always;
distinctness makes the containment strict, so `|D3(p)| ≤ 4`, and likewise
`|D4(p)| ≤ 3`.  A rank-5 mask among the 1011 values is therefore a
`D2(p)`.  There are 462 rank-5 masks and at most twelve missing masks in
total, so at least `462-12=450` of the 461 depth-two intersections have
rank exactly five.  Call the other positions *bad*: at most 11.

*Step 2 (two adjacent rank-5 meets force an exact rank-4 triple meet).*
Fix `p` with `|D2(p)|=|D2(p+1)|=5`.  Both are subsets of the rank-6 set
`C_{p+1}`, and they are distinct (distinct cell values).  Two distinct
5-subsets of a 6-set intersect in exactly 4 elements.  Since

    D3(p)=C_p∩C_{p+1}∩C_{p+2}=D2(p)∩D2(p+1),

we get `|D3(p)|=4` exactly.

*Step 3 (pigeonhole).*  Each bad position `q` destroys at most the two
windows `p=q-1,q`.  Hence at least `460-2·11=438` positions `p` have
`|D3(p)|=4`.  These 438 values are pairwise distinct rank-4 masks.  But
`C(11,4)=330<438`.  Contradiction.  ∎

**Remark 1.1 (refinement via reservoir rank caps).**  If requirement 4 is
also imposed, the twelve missing masks sit on the reservoir.  Strict
containments determined by the schedule alone cap the reservoir ranks:

    A_1⊊B_1⊊C_1, A_2⊊D2(1);  T_370⊊C_370, B_371⊊D2(370), A_372⊊D3(370);
    T_463⊊C_462, B_463⊊D2(461), B_464⊊T_463, A_463⊊D3(460),
    A_464⊊B_463, A_465⊊B_464.

Only `B_1, T_370, T_463` can have rank five.  So at most 3 missing masks
have rank five, at least 459 of the D2 cells are rank five, and the
forced count rises to `460-2·2=456` distinct rank-4 masks.  The deficit
against 330 is at least 126.

**Remark 1.2 (scope against the maximal factor).**  For the maximal
factor of any factorable q369 row, every bulk meet-cell value equals the
set intersection (audited Theorem 2.1), and a sparse repair confined to
`Omega` cannot change any bulk meet core (all are disjoint from
`Omega`).  Theorem 1 therefore refutes requirement 2 *as stated* — the
distinct-1011-meets reading — for every central row, before reservoir,
pins, or upper coverage are examined.  If distinctness is dropped and
only coverage is demanded of the maximal factor, the audited deficit
`>=(d-1)^2=4` of Proposition 3.4 still applies; Theorem 1 does not claim
to worsen that coverage-only bound, but it moves the live architecture
away from exact meets entirely (Section 3).

**Meet-core inventory used above and below** (exact, from the schedule):
depth-2 cores exist for `p=1..461` (461 cells), depth-3 cores for
`p=1..460` (singletons `[p+2]` for `p<=369`, pairs `[p+2,p+3]` for
`p>=370`), depth-4 cores for `p=370..459` (singletons `[p+3]`, 90
cells); `461+460+90=1011`.  The two seam depth-3 cores are the
singletons `A_370` (block `368..370`) and `A_371` (block `369..371`).

## 3. Theorem 2: what an actual q369 word is forced to do

Now let `A_1,...,A_465` be **any** universal nonzero word whose selected
rank-6 witnesses follow the q369 schedule (the exact semantics of the
`q369_schedule` SAT branch).  No saturation or distinctness is assumed;
it is derived.

> **Theorem 2 (forced saturation and value ladder).**
> (a) *Saturation.*  The 1023 non-central short cells carry pairwise
> distinct lower masks and cover all 1023 lower masks (a bijection).
> (b) *One defect.*  Rank-5 values occur only on the 463 slots
> `B_1,...,B_369, T_370,...,T_463`; exactly one slot has rank at most 4.
> (c) *Exact depth-two meets.*  For `1<=p<=368` with `|B_{p+1}|=5`:
> `B_{p+1}=C_p∩C_{p+1}` and `|C_p∩C_{p+1}|=5`.  For `370<=p<=461` with
> `|T_{p+1}|=5`: `T_{p+1}=C_p∩C_{p+1}`, rank 5.  Hence the central row
> consists of two Johnson arcs (`C_1..C_369` and `C_370..C_462`) with at
> most one non-Johnson transition inside them, located at the defect;
> the seam transition `C_369→C_370` is unconstrained at depth two.
> (d) *Forced rank-4 identities.*  If `3<=j<=369`, both flanking pairs
> `B_{j-1},B_j` nondefective, and `|A_j|=4`, then `A_j=D3(j-2)`.  If
> `372<=j<=462`, both flanking triples `T_{j-1},T_j` nondefective, and
> `|B_j|=4`, then `B_j=D3(j-2)`.  Late singletons `A_j` (`373<=j<=462`)
> satisfy `A_j ⊆ D4(j-3)` and have rank at most 3; the seam cells
> `B_370` (rank ≤4) and `A_370,A_371` (rank ≤3) are unforced.

**Proof.**  (a) A window of length `>=4` starting at `a<=462` contains
`[a,a+3] ⊇ I_a`, so its OR contains `C_a` and has rank at least 6.
Windows of length `>=4` start at `a<=462`.  Hence every one of the 1023
lower masks occurs as the value of a short cell (length `<=3`) that is
not one of the 369 shortened central cells (those have rank-6 values
`C_1..C_369`) and not one of the 93 central quadruples (rank 6, and not
short anyway).  There are exactly `1392-369=1023` non-central short
cells.  Pigeonhole forces a bijection; in particular all non-central
short values are lower masks and pairwise distinct, and physical
containment between two short cells forces strict set containment of
their values.

(b) *No rank-5 singleton:* any `A_j` lies in a pair cell; pairs are
never central, so the pair value is a lower mask strictly containing
`A_j`, giving `|A_j|<=4`.  *No rank-5 late pair:* for `j=370`,
`B_370 ⊊ T_370`; for `371<=j<=464`, `B_j=[j,j+1] ⊊ T_{j-1}=[j-1,j+1]`,
which is a non-central triple (start `j-1>=370`) existing since
`j+1<=465`.  In both cases the containing triple carries a lower value,
so `|B_j|<=4`.  *Early pairs and non-central triples are the slots:*
`B_1..B_369` (369 cells) and `T_370..T_463` (94 cells), total 463.  All
462 rank-5 masks occur, each on a slot; distinctness leaves exactly
`463-462=1` defective slot of rank at most 4 (and at least 2, since
every pair strictly contains a singleton and every triple a pair).

(c) For `p<=368`, `B_{p+1}` is physically `[p+1,p+2] ⊆ I_p∩I_{p+1}`,
so `B_{p+1} ⊆ C_p∩C_{p+1}`.  The `C_i` are distinct rank-6 masks
(selected witnesses of distinct targets), so `|C_p∩C_{p+1}|<=5`.  If
`|B_{p+1}|=5`, containment of a 5-set in a set of size at most 5 forces
equality.  Late case identical with `T_{p+1}=[p+1,p+3] ⊆ I_p∩I_{p+1}`.
The seam: `D2(369)=C_369∩C_370` has physical core `[370,371]=B_370`,
whose value has rank at most 4 by (b); only the containment
`B_370 ⊆ D2(369)` survives, so no equality is forced there.

(d) Early singleton `A_j`, `3<=j<=369`: `A_j ⊆ B_{j-1}∩B_j`.  When both
pairs are nondefective, they are (by (c)) two distinct 5-subsets of the
6-set `C_{j-1}`, so their intersection is exactly
`D2(j-2)∩D2(j-1)=D3(j-2)`, of rank exactly 4.  If `|A_j|=4`, equality.
If a flanking pair is the defect (rank `<=4`), then `A_j ⊊ B` gives
`|A_j|<=3` and `A_j` is not a rank-4 host at all.  Late pair `B_j`,
`372<=j<=462`: `B_j ⊆ T_{j-1}∩T_j`; nondefective flanking triples are
exact meets `D2(j-2),D2(j-1)`, two distinct 5-subsets of `C_{j-1}`,
intersection `D3(j-2)` rank 4; equality when `|B_j|=4`; a defective
flank forces `|B_j|<=3`.  (The bound `j<=462` is exactly what makes
`T_j=D2(j-1)` use an existing `C_j`; `B_463` has no second exact flank
and is handled as an unforced host below.)  Late singleton `A_j`,
`373<=j<=462`:
`A_j ⊆ T_{j-2}∩T_{j-1}∩T_j ⊆ D2(j-3)∩D2(j-2)∩D2(j-1)=D4(j-3)`, and
`|A_j|<=3` follows already from strict containment in the late pair
`B_j` of rank at most 4.  ∎

**Warning 2.1 (no depth-4 equality).**  `|A_j|=3` does **not** force
`A_j=D4(j-3)`: if the two consecutive triple intersections coincide,
`D3(j-3)=D3(j-2)`, then `|D4(j-3)|=4` and a rank-3 `A_j` is a proper
subset.  Coincidence of consecutive `D3` values is not excluded by
saturation — the `D3(p)` are set intersections, not cell values, so
distinctness never applies to them.  This is the depth-4 analogue of the
nonbacktracking lift condition of `K11_PORTAL_EMBEDDING_MATH_NEXT.md`,
Lemma 2.1: `D3(p)≠D3(p+1)` holds iff the Johnson path does not remove
and re-add the same element across the two transitions.  Only under that
extra nonbacktracking hypothesis at window `j-3` does `|D4(j-3)|=3` and
`|A_j|=3` force `A_j=D4(j-3)`.  Theorem 3 below is arranged so that it
never uses any depth-4 equality.

Theorem 2 recovers the one-defect theorem of `PORTAL_RIGIDITY_K11_NEXT`
with **weaker hypotheses** (universality plus the schedule, instead of
assumed short-band saturation), and shows the actual word escapes
Theorem 1 in exactly one way: deep cells may carry proper subsets of
their meets.  The `k=9` optimum already behaves this way, which is why
`nu(9)=B(9)` is consistent with Theorem 1's `k=9` analogue (114>84).

## 4. Theorem 3: the forced D3-coverage law

Cells able to carry a rank-4 value in a q369 word, by Theorem 2.  The
rank caps used below all come from single strict containments in
saturated cells and are exhaustive:

* every late singleton `A_373..A_462` and the seam/terminal singletons
  `A_370,A_371,A_372,A_463,A_464,A_465` are strictly inside a cell of
  rank at most 4 (`B_370`, `B_371`, `B_463`, `B_464`, or a late pair),
  hence have rank at most 3 — **never** rank-4 hosts;
* early singletons `A_3..A_369` (367 cells) and late pairs
  `B_372..B_462` (91 cells) are **forced bulk hosts**: rank 4 with
  nondefective flanks forces value `=D3(j-2)` (Theorem 2(d)); a
  defective flank caps them at rank 3;
* **unforced hosts**, exactly seven:
  1. `A_1` (reservoir; cap 4 via `A_1⊊B_1`),
  2. `A_2` (reservoir; cap 4 via `A_2⊊B_2`),
  3. `B_370` (the seam depth-2 core; cap 4 by Theorem 2(b), value only
     constrained by `B_370⊆D2(369)`),
  4. `B_371` (reservoir; cap 4 via `B_371⊊T_371`),
  5. `B_463` (reservoir; cap 4 via `B_463⊊T_462`),
  6. `B_464` (reservoir; cap 4 via `B_464⊊T_463`),
  7. the unique rank-5 defect slot (Theorem 2(b)), if its rank is 4.

  The reservoir slots `B_1, T_370, T_463` carry rank-5 masks unless one
  of them *is* the defect, which is case 7.

> **Theorem 3 (D3-coverage law).**  In every universal 465-entry word
> with the q369 schedule, at least `330-7=323` of the 330 rank-four
> masks occur among the consecutive triple intersections
> `{D3(p): p in [1,367] ∪ [370,460]}` of the central row.  Moreover all
> but at most two of those 458 windows satisfy `|D3(p)|=4` exactly, and
> the windows carrying the 323 masks are pairwise distinct cells with
> distinct values.

**Proof.**  Each of the 330 rank-4 masks occupies exactly one
non-central short cell (Theorem 2(a)).  By the inventory that cell is
one of the seven unforced hosts or a forced bulk host; at most 7 masks
use unforced hosts, so at least 323 sit on forced bulk hosts.  A forced
bulk host with a defective flank has rank at most 3 and hosts nothing,
so each of the 323 masks equals `D3(j-2)` for its host `j`
(Theorem 2(d)).  Host windows: early `j=3..369` gives `p=j-2=1..367`;
late `j=372..462` gives `p=370..460`.  (The seam windows `p=368,369`
never appear: their would-be hosts are the singletons `A_370,A_371`,
which are capped at rank 3.)  Distinct masks on distinct cells is
saturation; distinct host cells give distinct windows `p`.  For the
exactness claim: at most one slot among the 463 is defective
(Theorem 2(b)); every window `p` whose two flanking slots are
nondefective has `|D3(p)|=4` by Step 2 of Theorem 1 (two distinct exact
5-subsets of the 6-set `C_{p+1}` meet in exactly 4).  One defective slot
lies in at most two windows.  ∎

**Consistency check.**  `458=367+91` candidate windows, at least 323
required distinct rank-4 values among them — comfortably below the 330
available, and above `330-7`.  Had the unforced-host count been 65 or
more, Theorem 3 would be vacuous; the actual count is 7.

**Corollary 3.1 (forced cut-middle-levels geometry).**  The 463 rank-5
slots split as 460 depth-2 core slots (`B_{p+1}`, `p∈[1,368]`;
`T_{p+1}`, `p∈[370,461]`) plus the 3 reservoir slots `B_1,T_370,T_463`,
which are cores of no window.  In any such word `D2(p)` has rank
exactly 5 for every core window outside at most one defective
transition; hence `C_1..C_369` and `C_370..C_462` are Johnson paths
(one transition may fail if the defect is a core slot), and either
`459` exact `D2` values `+3` reservoir rank-5 masks (core defect) or
`460+2` (reservoir defect) exhaust all 462 rank-5 masks.  This is precisely a two-arc facet-rainbow decomposition — the
cut middle-levels object of `K11_PORTAL_EMBEDDING_MATH_NEXT.md`,
Theorem 8.1, with a free (un-pinned) seam — now derived as *necessary*
from universality plus the schedule alone.  The new content beyond
Theorem 8.1 is the second-order law: the *rank-4 shadow*
`p ↦ D3(p)` of the cycle must be 323/330-surjective.

## 5. Answering the central question, in both readings

**Exact-meet reading: no.**  Theorem 1: the 1011 meets cannot be 1011
distinct masks.  The organized object named in the question — bulk meets
carrying the meets as values, reservoir carrying the twelve leftovers —
does not exist for any braid, however upper-complete.  Requirement 2
must be abandoned as written.

**Corrected reading: reduced, not resolved.**  Conditions (i)–(v) below
are *necessary* for a universal q369 word (Theorems 2–3 plus the audited
run criterion).  They are **not** claimed sufficient: because Theorem 1
forces deep cells to carry proper subsets of their meets, the word is
not the maximal factor, and the automatic pin survival of the
maximal-shadow theorem no longer applies to depth-3/4 cells.
Sufficiency requires additionally (vi): the full value assignment passes
the exact coordinatewise interval-stabbing test — for every coordinate
`x`, the legal set left by all cells whose value omits `x` must still
meet every cell whose value contains `x`.  That test is now global on
the deep cells, not localized to `Omega`.

  (i) mixed-run factorability (runs `>=3` early / `>=4` late, audited
      Theorem 4.1 criterion);
  (ii) two facet-rainbow Johnson arcs `C_1..C_369`, `C_370..C_462` with
      at most one defective transition, their 460 exact `D2` values plus
      at most 3 reservoir rank-5 values (on `B_1,T_370,T_463`)
      exhausting the 462 rank-5 masks with one defect slot;
  (iii) the D3-coverage law: `>=323` distinct rank-4 masks among the 458
      window intersections `D3(p)`, `p∈[1,367]∪[370,460]`, the missing
      `<=7` placed injectively on the seven unforced hosts subject to
      their containments (`A_1⊆C_1`-side chains, `B_370⊆D2(369)`, etc.);
  (iv) ranks 1–3 (`11+55+165=231` masks) assigned to the remaining short
      cells respecting strict containment — depth-3/4 cores, defect
      neighbours, and reservoir remainders; and
  (v) upper completeness: consecutive unions of the `C_i` covering all
      `562` masks of ranks 7–11 (by Theorem 2.1(3) of the maximal-shadow
      theorem this is row-intrinsic: every factor realizes exactly the
      consecutive-union family).

Condition (iii) is the genuinely new gate.  It is a *strong* second-order
constraint on the middle-levels cycle: a random or generic Johnson path
repeats D3 values freely, while (iii) demands near-perfect injectivity
of the triple-meet shadow on 458 windows (at most `458-323=135` slack
repetitions/misses, but with all 330 values needed up to 7 exceptions).

## 6. Explicit k=11 arithmetic ledger

    slots for rank 5:      369 early pairs + 94 late triples = 463
    rank-5 masks:          462     -> exactly 1 defect slot
    forced-exact D2:       460 of 461 windows (D2(369) exempt: its core
                           B_370 is capped at rank <=4)
    rank-4 hosts:          367 early singletons + 91 late pairs forced;
                           7 unforced (A_1,A_2,B_370,B_371,B_463,B_464,
                           defect slot)
    D3 windows hosting:    458 = [1,367] ∪ [370,460]
    D3-coverage law:       >=323 of C(11,4)=330
    rank<=3 masks:         231 on remaining cells: 90 depth-4 cores
                           (A_373..A_462), seam/terminal singletons
                           A_370,A_371,A_372,A_463,A_464,A_465, early
                           singletons A_3..A_369 not hosting rank 4,
                           defect-flank cells, and reservoir leftovers
    meet-core total:       461+460+90=1011 physical cells (cells, not
                           necessarily 1011 distinct values — Theorem 1)
    reservoir:             12 cells, ranks capped as in Section 2
    upper masks:           sum_{s=7..11} C(11,s)=562 targets from
                           consecutive unions of the C_i

## 7. Adversarial self-audit

* **Theorem 1, Step 1** uses only strict containment of nested distinct
  cells — needs the *hypothesis* of 1011 distinct values, granted.  The
  count `450=462-12` allows all twelve missing masks to be rank 5;
  Remark 1.1 sharpens with reservoir caps but Theorem 1 does not need
  it.  **Step 2** is the 5-subsets-of-a-6-set identity; `D2(p)≠D2(p+1)`
  because they are distinct cell values (both are among the 1011 by the
  inventory: `D2` cores exist for all `p=1..461`).  Seam: `p=369` has
  core `B_370`, included, so no window is exempt in Theorem 1 —
  exemptions only matter in Theorem 2 where `D2(369)` has no rank-5
  slot.  **Step 3**: each bad position kills windows `p-1,p` only.
  Verified: `460-2·11=438>330`.
* **Theorem 2(a)** pigeonhole: needs every lower mask on a *non-central*
  short cell.  A lower mask could sit on a shortened central cell?  No —
  those cells' values are `C_1..C_369`, rank 6.  Could two non-central
  short cells share a value with some lower mask missing?  No — count is
  exactly 1023=1023, so injectivity and surjectivity are equivalent and
  both forced.  Windows of length `>=4` starting at `a>=463` do not
  exist (`465-4+1=462`).  ✓
* **Theorem 2(b)** boundary cases: `B_465` does not exist (pairs end at
  464).  `T_464,T_465` do not exist (triples end at 463).  The 94 late
  triples are `T_370..T_463`.  ✓  Minimum defect rank 2 (pair) / 3
  (triple) noted but unused.
* **Theorem 2(c)** uses distinctness of `C_p,C_{p+1}` — they are
  witnesses of distinct rank-6 targets.  The seam is correctly exempt.
* **Theorem 2(d)** flank logic: early host `A_j` needs `B_{j-1},B_j`
  exact, i.e. slots `B_{j-1},B_j` nondefective — both exist for
  `3<=j<=369`.  Late host `B_j` needs `T_{j-1},T_j` exact — exist for
  `372<=j<=462`.  At `j=463`: `T_463` is reservoir/slot but `T_463`'s
  exactness would need window `p=462`... `D2(462)` does not exist
  (central row ends at 462), so `B_463` is correctly *not* a forced
  host; it is unforced host 5.  ✓  **Warning 2.1** documents the
  depth-4 non-forcing; nothing downstream uses depth-4 equality.
* **Theorem 3** host exhaustiveness: every short non-central cell is
  (early singleton | early pair | seam-zone cell | late pair | late
  singleton | late triple | terminal cell).  Rank-4 candidates: early
  singletons (forced), early pairs only as *the defect* (case 7), late
  triples only as the defect (case 7), late pairs `B_372..B_462`
  (forced), `B_370,B_371,B_463,B_464,A_1,A_2` (unforced 1–6), all other
  singletons capped `<=3`.  `A_372⊊B_372`? `[372,372]⊂[372,373]`, and
  `B_372` has rank `<=4`, so `A_372` capped at 3.  ✓  Exactly 7.
* **Defect double-counting**: if the defect slot has rank 4 it *is*
  unforced host 7; if rank 2–3 it hosts nothing and only kills `<=2`
  windows.  Both cases respected.
* **Corollary 3.1**: "Johnson paths" requires exact rank-5 D2 at every
  core transition except `<=1` defective; the seam `p=369` is not a core
  window (its core `B_370` is rank-capped), matching Theorem 2(c).
  Facet-rainbow: exact D2 values are distinct because they are cell
  values.  Slot arithmetic: `368+92=460` core slots `+3` reservoir
  slots `=463`; both defect placements give `462` rank-5 masks.  ✓
  Note the corollary does not claim the two facets of `B_1`-type slots
  attach as in Theorem 8.1; it claims the arc/facet *counts* and
  distinctness, which is what the reduction uses.
* **Section 5(vi)** honesty: sufficiency is open; no conditional
  construction is presented as a solution.

## 8. The precise remaining lemma

> **Open Lemma (D3-surjective factorable cut cycle).**  Construct (or
> refute) a Hamilton cycle of `ML_11` with two cut vertices, giving arcs
> of 369 and 93 rank-6 vertices ordered as `C_1..C_369, C_370..C_462`,
> such that:
> 1. the mixed-run criterion holds (internal coordinate runs `>=3`
>    before index 370, `>=4` after);
> 2. the triple-meet shadow `{D3(p)}` over the 458 hosting windows
>    covers at least 323 rank-4 masks (equivalently: at most 7 rank-4
>    masks are D3-missing, and those admit an injective assignment to
>    the seven unforced hosts compatible with their containment chains);
> 3. ranks 1–3 admit a saturated assignment to the remaining cells; and
> 4. the consecutive unions cover all 562 upper masks;
> 5. the resulting full value table passes the coordinatewise
>    interval-stabbing test.
>
> A refutation of clause 2 alone — e.g. a proof that every factorable
> two-arc facet-rainbow row misses more than 7 rank-4 masks in its D3
> shadow — would refute the entire q369 schedule (branch-locally: the
> `q369_schedule` SAT branch would be UNSAT), leaving `nu(11)=465` to
> other monotone-band schedules.

The quantitative heart is clause 2.  Note `458-330=128` windows *must*
repeat or waste D3 values even in the best case; the law does not demand
injectivity, only near-surjectivity — this is a covering design
condition on the middle-levels cycle, new to this reduction.

## 9. General-k extension

For odd `k=2m+1`, `r=m+1`, `d`, `sigma` canonical: the same proofs give
(a) forced short-band saturation from universality plus the schedule,
(b) a one-defect theorem, (c) exact depth-2 meets away from defect and
seam, (d) the over-production theorem — with `bad<=(M-1)-(C(k,r-1)-d(d+1))`,
at least `(M-2)-2·bad` distinct exact depth-3 meets are forced versus
`C(k,r-2)` available; since `M ≈ C(k,r-1) ≫ C(k,r-2)` at central ranks,
the exact-meet reading dies for **every** such `k` (`k=9`: 114>84;
`k=11`: 438>330 without reservoir caps, 456>330 with; `k=14`:
2562>2002), and (e) the
corrected D3-coverage law: at least `C(k,r-2)-O(d^2)` rank-(r-2) masks
must appear among consecutive triple meets, with the `O(d^2)` unforced
hosts confined to the seam and terminal zones.  The general open lemma
is the same covering-design condition on a cut middle-levels cycle; the
`k=9` optimum is a existence proof for its `k=9` instance, and its
D3-shadow statistics are the natural first object to compute for
recursive (Pascal-fusion) constructions.

## 10. Ledger

**Proved here.**
1. Theorem 1: exact-meet requirement 2 is unsatisfiable (456>330);
   with reservoir caps, deficit `>=126`.  Analogues at `k=9,14`.
2. Theorem 2: forced saturation, one-defect, exact-D2, forced rank-4
   identities, depth-4 warning, for every universal q369 word.
3. Theorem 3: the D3-coverage law `>=323/330` with the exact 7-element
   unforced-host inventory.
4. Corollary 3.1: necessity of the two-arc facet-rainbow (cut
   middle-levels) geometry.
5. Section 6 arithmetic; window/flank bookkeeping verified by script.

**Conjectural / open.**
1. Existence of a cycle satisfying the Open Lemma (all five clauses).
2. Sufficiency of (i)–(v) alone — false as stated without (vi); the
   right sufficiency theorem for non-maximal deep values is open.
3. Any claim about other monotone-band schedules at `k=11`.

**Not touched.**  `nu(11)` bounds; the running SAT portfolios; shared
solver files; the handoff.
