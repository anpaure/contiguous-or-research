# Independent audit: `K11_Q369_MEET_RIGIDITY_NEXT.md`

## Verdict

The exact `k=11` core is valuable and mostly correct:

* **Theorem 1: PASS.**  The exact-meet interpretation is impossible.  The
  hypotheses of Theorem 1 itself force at least 438 distinct rank-four `D3`
  values; adding the twelve-cell reservoir rank caps raises this to 456.
* **Theorem 2: PASS**, with one harmless range typo in its proof and a small
  omission in the list of non-forced seam cells.
* **Theorem 3: PASS.**  The `323/330` `D3`-coverage law and its seven-host
  inventory are correct.
* **Corollary 3.1: PARTIAL FAIL.**  The current snapshot correctly repairs
  the earlier unconditional “460 exact `D2`” wording to the `459/460` defect
  case split.  But the theorems still do not force a two-cut Hamilton cycle
  of `ML_11` or the required crosswise endpoint facets.
* **Sections 5 and 8 overstate necessity.**  Their middle-levels cycle is a
  useful stronger construction ansatz, not the exact remaining object for
  every q369 word.  Refuting that subclass would not refute the full q369
  schedule.
* **Section 9 is not proved by the preceding arguments.**  It invokes an
  even `k=14` analogue inside an odd-dimensional discussion and asserts a
  general one-defect/D3 law without the required inventory proof.  It should
  be moved from “proved” to “conjectural/generalization target.”

No issue found here refutes the q369 branch or changes `nu(11)`.

Audited source snapshot:

```text
ee305730bf4ef710650bf13a04bafe92b594a5cdcd8bc7b4eaae41d679a76291
K11_Q369_MEET_RIGIDITY_NEXT.md
```

The source file was not edited during this audit.

## 1. Mechanical inventory audit

Using one-based positions, the central cells are

```text
T_i=[i,i+2], i=1..369,
Q_i=[i,i+3], i=370..462.
```

Direct enumeration reproduces all counts in Sections 1 and 6:

```text
short cells                         1392
short central cells                  369
noncentral short cells              1023
D2 cores                              461
D3 cores                              460
late D4 cores                          90
all nontrivial meet cores            1011
reservoir                               12
rank-five maximal pool                463
certifiable bulk D2 slots             460
boundary rank-five slots                3
forced rank-four hosts                458
fixed unforced rank-four hosts           6
plus the unique defect host              1
```

The reservoir is exactly

```text
A1, B1, A2; T370, B371, A372;
A463, A464, A465, B463, B464, T463.
```

The 460 bulk `D2` slots are

```text
B2..B369, T371..T462,
```

and the three boundary slots are

```text
B1, T370, T463.
```

The 458 forced rank-four hosts are `A3..A369` and `B372..B462`, mapping
bijectively to `D3` windows

```text
p in [1,367] union [370,460].
```

The executable enumeration printed:

```text
PASS short=1392 central_short=369 meet=1011 reservoir=12
PASS rank5_pool=463 bulk_D2_slots=460 boundary_slots=3
PASS forced_rank4_hosts=458 fixed_unforced=6 plus defect=1 D3_windows=458
```

## 2. Theorem 1

The proof is correct.  Pairwise distinctness of all 1011 meet values makes
`D3(p)` a strict subset of `D2(p)`.  Since two distinct rank-six sets have
intersection rank at most five, every rank-five meet value is a `D2` value.

Without reservoir rank caps, at least `462-12=450` of the 461 `D2` values
have rank five, leaving at most eleven bad positions.  A bad `D2(q)` affects
only adjacent `D3` windows `q-1,q`; therefore at least

```text
460 - 2*11 = 438
```

`D3` values have rank exactly four.  Pairwise distinctness contradicts the
330 available four-sets.

With the explicit reservoir assignment, only `B1,T370,T463` can carry rank
five.  Thus at least 459 `D2` values have rank five, at most two are bad, and

```text
460 - 2*2 = 456 > 330.
```

Two presentational corrections are needed:

1. Theorem 1 alone proves 438; 456 requires Remark 1.1's reservoir caps.
2. The opening calls the forced rank-four objects “depth-two
   intersections.”  They are the depth-three intersections `D3` under the
   document's own notation.

These corrections do not affect the contradiction.

## 3. Theorem 2

### Saturation and defect

Part (a) is exact.  Every interval of length at least four starts at
`a<=462` and contains `[a,a+3]`, which contains the selected `I_a`.
Consequently its OR has rank at least six.  All 1023 lower masks therefore
use the 1023 noncentral short cells.  They are a bijection, so physical strict
containment gives strict containment of their values.

Part (b)'s maximal pool is correct: `B1..B369,T370..T463`, 463 cells for 462
rank-five masks, hence one defect.  Boundary arguments for singleton and late
pair ranks are also correct.

### Exact meets

Part (c) correctly certifies

```text
D2(p)=B_(p+1), p=1..368, when that slot is nondefective;
D2(p)=T_(p+1), p=370..461, when that slot is nondefective.
```

The seam `p=369` has core `B370` of rank at most four and is correctly left
uncontrolled.

Part (d)'s exact `D3` identities are valid.  The proof contains the phrase
“Late pair `B_j`, `372<=j<=463`”; the valid forced range is `372<=j<=462`,
as both the theorem statement and the following parenthetical correctly say.
`B463` is an unforced reservoir host.  Also, `A372` is capped at rank three
but, like `A370,A371`, has no forced meet equality; mentioning it would make
the seam inventory clearer.

Warning 2.1 is correct: a rank-three late singleton need not equal `D4` if
the two adjacent `D3` set intersections coincide.

## 4. Theorem 3

The host inventory is exhaustive.  There are six fixed unforced cells

```text
A1, A2, B370, B371, B463, B464
```

and the unique defective rank-five slot can be a seventh rank-four host.
Every other rank-four value must occur on a forced host and hence equal the
corresponding `D3`.  Therefore at least

```text
330 - 7 = 323
```

distinct rank-four masks occur among the 458 stated `D3` windows.

A bulk defect touches at most two of these windows.  All other windows have
two distinct exact rank-five flanks inside one rank-six set, so their `D3`
has rank exactly four.  Thus the “all but at most two” assertion is correct.

## 5. Corollary 3.1: the corrected count does not imply the cycle

The current source correctly uses the following case split.  Let `delta=1`
when the unique defect lies in a bulk slot

```text
B2..B369 or T371..T462,
```

and `delta=0` when it lies in `B1,T370,T463`.  What is actually proved is

```text
certified exact D2 colours = 460-delta,
boundary rank-five values = 2+delta,
total                         462.
```

Thus:

* boundary defect: 460 exact `D2` colours and two boundary rank-five values;
* bulk defect: 459 exact `D2` colours and three boundary rank-five values.

At a bulk defect the corresponding central transition may or may not still
be Johnson-adjacent; its set intersection is simply not certified by the
physical core and need not be a new colour.  Hence the two displayed blocks
are not unconditionally two Johnson paths.

Even in the boundary-defect case, the two remaining boundary rank-five masks
are only known to be facets of individual endpoints (`B1 subset C1`,
`T370 subset C370`, `T463 subset C462`, according to which two survive).
Nothing proves that two of them join the four path endpoints crosswise, and
there is no physically forced facet at `C369`.  Therefore Theorem 8.1's
cut-cycle converse cannot be invoked.

The safe conclusion is:

> The row has 459 or 460 distinct certified rainbow Johnson transitions,
> split between the two prescribed blocks, with a free seam and at most one
> additional uncertified internal transition.

Thus the repaired `459/460` wording should be retained, but calling the result
“precisely a two-arc facet-rainbow decomposition” remains unsupported.

## 6. Consequences for Sections 5 and 8

Condition (ii) in Section 5 must use the `459/460` case split above.  The
Hamilton-cycle Open Lemma in Section 8 remains a useful **stronger sufficient
construction target**, but it is not the exact remaining lemma for the q369
branch.  In particular, proving that every factorable two-arc facet-rainbow
cycle misses more than seven `D3` colours would refute that subclass, not a
q369 schedule having a bulk defect or lacking crosswise endpoint facets.

Condition (v) is also stronger than what universality immediately forces.
Every upper-rank witness whose right endpoint is a central right endpoint is
a consecutive central-row union by the exact join-hull theorem.  In this
schedule the central right endpoints are

```text
3..371 and 373..465;
```

endpoint 372 is missing.  Upper masks may therefore additionally occur as
suffix ORs ending at 372.  Those suffix values form an inclusion chain, so
at most one per rank (at most five across ranks 7 through 11) can escape the
consecutive-union family.  Demanding all 562 upper masks as row unions is a
clean sufficient condition, but the note has not proved it necessary.

## 7. Section 9 generalization

Section 9 should not be listed wholesale as proved.  Its exact-meet
over-production calculation is salvageable, but its corrected-word structure
is not established.

For an odd upper-middle canonical schedule satisfying the reservoir theorem's
hypotheses and `d>=2`, the exact-meet argument does extend: at most
`d(d+1)` rank-`r-1` masks lie in the reservoir, so at most

```text
(M-1) - (C(k,r-1)-d(d+1))
```

`D2` positions are bad, and the adjacent-good count stated in Section 9
follows.  This reproduces 114 for `k=9` and 438 for `k=11`; separate even
arithmetic gives 2562 for the proposed `k=14` analogue.  The required
schedule range and reservoir hypotheses should be stated explicitly, and
finite “every k” claims should be checked rather than inferred from the
asymptotic comparison.

By contrast, the corrected actual-word argument uses several facts that are
not established there for general `k`:

1. equality of the two middle-layer sizes in odd dimension;
2. the precise single-switch maximal-cell pool and its one-defect count;
3. a complete general reservoir rank-cap inventory;
4. the number and location of forced `D3` hosts;
5. the endpoint/facet geometry of the resulting components.

The paragraph starts with odd `k=2m+1` but then cites the even case `k=14`
without separately proving the even corrected-value inventory.  Its `2562>2002`
arithmetic is internally consistent with the proposed exact-meet count
(`3430-2*(3431-2997)=2562`), but this arithmetic does not establish the
claimed general value ladder or corrected-host theorem.

The asymptotic intuition is plausible: at an upper odd middle rank the gap
between `binom(k,r-1)` and `binom(k,r-2)` is of order `M/k`, which is
exponentially large relative to an `O(d^2)` reservoir.  (The two binomial
layers themselves have ratio tending to one, so the source's `much greater`
symbol should refer to their difference versus the reservoir, not their
ratio.)  But the note has not proved the claimed general one-defect theorem,
the `binom(k,r-2)-O(d^2)` corrected-value coverage law, or closure under a
cut-middle-level cycle.  Those parts belong under “conjectural / next
theorem”; only the properly qualified exact-meet over-production argument is
ready for the proved ledger.

## Recommended corrected status

Retain as proved:

1. the exact-meet impossibility at `k=11` (`438>330`, or `456>330` with
   reservoir caps);
2. Theorem 2's q369 saturation/value ladder;
3. Theorem 3's `323/330` `D3` law.

Downgrade or rewrite:

1. Corollary 3.1: retain its repaired `459/460` count, but downgrade the
   cut-cycle conclusion to “at most one uncertified internal transition”;
2. Sections 5 and 8 from an equivalent reduction to a stronger constructive
   ansatz;
3. retain Section 9's exact-meet count only with its schedule hypotheses;
   move its one-defect, corrected D3-law, and cut-cycle claims to conjectural
   generalization pending separate proofs.
