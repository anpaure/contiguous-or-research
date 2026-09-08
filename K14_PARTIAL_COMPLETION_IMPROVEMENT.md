# The 260-mask `k=14` completion problem

## 1. Certified input and current construction

The partial word `k14_pinnable_factor_missing260.txt` has length 3434 and
misses exactly 260 nonzero masks:

* 238 masks of rank 9;
* 22 masks of rank 10.

The existing program `partial_completion_forest.cpp` constructs a standalone
completion of length 243.  It uses all 238 rank-9 masks literally, three
low-rank auxiliary entries, and two literal rank-10 entries.  Exhaustive suffix
OR verification of the concatenated length-3677 word succeeds.

`k14_completion_243_witnesses.txt` is a direct standalone certificate.  It
contains one record

```
target rank one_based_left one_based_right recomputed_or
```

for each of the 260 targets.  Its shortest-witness distribution is

| target rank | witness length | count |
|---:|---:|---:|
| 9 | 1 | 238 |
| 10 | 1 | 2 |
| 10 | 2 | 20 |

Among the 22 missing rank-10 masks, fourteen contain at least two of the
missing rank-9 masks and are covered by adjacent literal rank-9 entries in a
linear forest.  Seven contain exactly one missing rank-9 mask:

| rank-10 target | unique contained rank-9 target | missing bit(s) |
|---:|---:|---:|
| 7676 | 7420 | 256 |
| 8015 | 8014 | 1 |
| 13287 | 13283 | 4 |
| 13439 | 13423 | 16 |
| 13757 | 13725 | 32 |
| 14285 | 6093 | 8192 |
| 15334 | 15302 | 32 |

The remaining target

\[
V=15346
\]

contains **no** missing rank-9 mask.  Call these eight masks the hard upper
family \(\mathcal H\).

The current three auxiliaries are

\[
288,\quad 8196,\quad 48.
\]

They cover six of the seven uniquely based targets in pairs; 8015 and 15346
are then written literally.  Hence the length is

\[
238+3+2=243.
\]

## 2. Exact standalone optimum

### Theorem 1 (endpoint-defect bound)

Every standalone word covering the 238 missing rank-9 masks and the eight hard
rank-10 masks has length at least 243.  Consequently the existing 243-term
completion is globally shortest as a standalone completion of this 260-mask
family.

### Proof

Let the word have length \(n\), and choose one witness interval \(I_S\) for
each of the \(M=238\) missing rank-9 masks \(S\).  Distinct rank-9 masks are
incomparable.  Therefore no two chosen intervals contain one another: interval
containment would imply containment of their OR masks.  It follows that the
238 left endpoints are distinct and the 238 right endpoints are distinct.
There are exactly \(n-M\) positions unused as rank-9 left endpoints and
exactly \(n-M\) positions unused as rank-9 right endpoints.  These are
side-specific slots; a physical position may count once on each side.

Choose one witness interval \(J_T\) for each of the eight hard rank-10 masks
\(T\in\mathcal H\).  These eight masks are also incomparable, so their left
endpoints are mutually distinct and their right endpoints are mutually
distinct.

We need one elementary endpoint-sharing fact.  Suppose \(J_T\) and \(I_S\)
have the same left endpoint.  Equal right endpoints are impossible because
one physical interval has only one OR.  If \(J_T\) ended first, then
\(J_T\subset I_S\), which would imply the impossible containment
\(T\subseteq S\) from a rank-10 set into a rank-9 set.  Hence
\(I_S\subset J_T\), and therefore \(S\subset T\).  The same argument, with
the order reversed, applies when the two intervals have the same right
endpoint: again \(I_S\subset J_T\) and \(S\subset T\).

The target 15346 contains no missing rank-9 mask, so neither endpoint of its
witness can be shared with a selected rank-9 witness.  Each of the other seven
hard targets contains exactly one missing rank-9 mask \(S_T\).  Its two
endpoints cannot both be shared.  Indeed, sharing on both sides would force
both shared rank-9 witnesses to represent \(S_T\); there is only one selected
interval \(I_{S_T}\), and sharing both endpoints with it would make
\(J_T=I_{S_T}\), although one physical interval cannot have both a rank-9 and
a rank-10 OR.

Thus the eight hard witnesses have sixteen side-endpoints, of which at most
seven can be shared with selected rank-9 endpoints.  At least

\[
16-7=9
\]

must use omitted rank-9 side-endpoint slots.  But there are only
\(2(n-M)\) such slots.  The hard upper left endpoints are distinct, and
separately their right endpoints are distinct, so no side-specific omitted
slot is counted twice.  We obtain

\[
9\le2(n-238),
\]

and hence \(n\ge243\).  (If \(n<238\), the rank-9 antichain alone is already
impossible.)  The certified 243-term word attains the bound. \(\square\)

### General two-layer endpoint-defect lemma

The argument has a reusable form.  Let \(\mathcal A\) be an antichain of
\(M\) lower-rank targets and \(\mathcal B\) an antichain of higher-rank
targets.  For \(T\in\mathcal B\), put

\[
c(T)=|\{S\in\mathcal A:S\subset T\}|.
\]

Then every standalone word covering both families satisfies

\[
2(n-M)\;\ge\;
\sum_{T\in\mathcal B}\max\{0,2-c(T)\}.
\]

To see this, the selected \(\mathcal A\)-witnesses occupy \(M\) distinct
left slots and \(M\) distinct right slots.  Each shared same-side endpoint of
a \(T\)-witness identifies a contained lower target.  If both endpoints are
shared, they must identify two distinct lower targets; identifying the same
selected lower witness twice would make the physical intervals identical.
Thus a \(T\)-witness shares at most \(\min\{2,c(T)\}\) of its endpoints and
requires at least \(\max\{0,2-c(T)\}\) omitted side-slots.  Distinct witnesses
in \(\mathcal B\) cannot reuse a left slot or reuse a right slot.

For the complete 22-mask missing rank-10 family here, fourteen targets have
\(c(T)\ge2\), seven have \(c(T)=1\), and 15346 has \(c(T)=0\).  The defect sum
is therefore

\[
14\cdot0+7\cdot1+1\cdot2=9,
\]

which is exactly the preceding \(n\ge238+\lceil9/2\rceil=243\) bound.

### Scope

This theorem is exact for a **standalone** completion word.  It does not rule
out appending only 242 new entries to the old factor if some missing targets
are represented by intervals crossing the old/new seam.  It is therefore not
a new lower bound on a full universal `k=14` array.

## 3. Secondary run-capacity structure

The endpoint-defect proof above settles the standalone question.  The next two
lemmas are retained because they describe why the existing forest gadget is
rigid and may be useful in a future cross-seam repair.

### Theorem 2 (literal-lower optimum)

Let \(W\) be a standalone word covering the 238 missing rank-9 masks and the
eight hard upper masks.  If every one of the 238 rank-9 masks occurs literally
as an entry of \(W\), then

\[
|W|\ge 243.
\]

Thus the existing 243-term completion is shortest in the entire class that
literalizes every missing rank-9 mask.  In particular, every possible
242-term completion must represent at least one rank-9 target by a genuinely
non-singleton interval.

### Proof

Assume for contradiction that \(|W|\le242\).  Mark one literal occurrence of
each of the 238 distinct rank-9 targets.  Call the remaining positions
*extra*.  Their number is

\[
t\le 242-238=4.
\]

The extra positions split into \(q\le t\) maximal consecutive runs.  We assign
one witness of every target in \(\mathcal H\) to one such run.

First consider the target \(V=15346\).  Its witness cannot contain a marked
position: a marked position is a missing rank-9 set \(S\), and containment of
that position would imply \(S\subset V\), whereas no missing rank-9 target is
contained in \(V\).  Hence the witness for \(V\) lies wholly inside one extra
run.

Now consider one of the other seven targets \(T\).  It contains exactly one
marked mask, namely its displayed rank-9 base \(S_T\).  Consequently a witness
for \(T\) contains at most one marked position.  If it contains none, it lies
inside one extra run.  If it contains the marked occurrence of \(S_T\), trim
the witness as follows.  Since \(T\setminus S_T\) is one bit, retain the
marked entry and an occurrence of that missing bit on one side of it, deleting
the other side.  Every retained entry is a subset of \(T\), so the trimmed
interval still has union exactly \(T\).  It consists of the marked base and a
prefix or suffix of one adjacent extra run.  Assign it to that run.

Fix an extra run of length \(s\), and adjoin its marked neighbor on each side
when present.  Every assigned witness is either internal to the run, or uses
one adjacent marked endpoint.  No assigned witness uses both marked endpoints.
The assigned masks all have rank 10 and are distinct, so their intervals form
a noncontaining family.  In particular their left endpoints are distinct.
There are at most \(s+1\) possible left endpoints: the left marked endpoint
and the \(s\) extra positions.  Therefore this run receives at most \(s+1\)
hard targets.

Summing over all runs gives

\[
8=|\mathcal H|\le \sum_R(|R|+1)=t+q.
\]

Since \(t\le4\) and \(q\le t\), equality is possible only when
\(t=q=4\): there are four singleton extra runs and every run receives two hard
targets.

But the singleton run receiving \(V\) has its sole entry equal to \(V\).
Any boundary witness assigned to the same run contains that entry, hence its
union contains \(V\).  A distinct rank-10 target cannot strictly contain the
rank-10 set \(V\).  Thus this run receives only \(V\), not two targets.  The
total capacity is at most seven, a contradiction.  Therefore \(|W|\ge243\).
\(\square\)

### Consequence inside the literal-lower class

The theorem rules out all approaches that merely:

* reorder the 238 rank-9 literals;
* change the three current auxiliaries;
* repack the seven uniquely based upper masks into different auxiliary pairs;
* replace either literal upper mask while retaining all rank-9 literals.

A hypothetical counterexample to the endpoint theorem would have needed
overlap of incomparable witnesses.  If a rank-9 target \(Q\) were not literal,
its witness and the witness for 15346 would have to cross or occupy distinct
extra runs; neither could contain the other because \(Q\not\subset15346\).

### Theorem 3 (one nonliteral rank-9 target is still insufficient)

In fact, every 242-term completion must have **at least two** missing rank-9
targets which do not occur as literal entries.

#### Proof

Suppose exactly one missing rank-9 target \(Q\) is not literal.  Mark one
literal occurrence of each of the other 237 rank-9 targets.  There are at most

\[
t=242-237=5
\]

unmarked positions, again split into \(q\) maximal runs.

The selected witness for \(Q\) lies wholly in one unmarked run and has length
at least two.  It cannot contain a marked rank-9 entry, since that entry would
be a distinct rank-9 subset of \(Q\).  In particular \(q\le4\).

We use a small saturation observation.  A run of \(s\) unmarked positions can
receive at most \(s+1\) witnesses from the hard rank-10 family, exactly as in
Theorem 2.  If it receives \(s+1\), then its two marked neighbors must both
exist, and the witness intervals are forced to be all the adjacent pairs

\[
[0,1],[1,2],\ldots,[s,s+1].
\]

Indeed, the \(s+1\) left endpoints and the \(s+1\) right endpoints must all be
distinct; in increasing order the only possible matching is right endpoint
\(i+1\) for left endpoint \(i\).

The run containing the non-singleton witness for \(Q\) cannot saturate this
bound.  That witness contains some adjacent pair of unmarked positions, and
the OR of that adjacent pair is a subset of the rank-9 set \(Q\), hence has
rank at most 9.  But saturation would use that same physical pair as a witness
for a rank-10 hard target.  Therefore the \(Q\)-run receives at most \(s\)
hard targets.

Consequently the total hard-target capacity is at most

\[
t+q-1\le 8.
\]

The only way this can equal eight is \(t=5,q=4\).  Then the \(Q\)-run has
length two and the other three runs are singletons.  The target 15346 cannot
be represented inside the \(Q\)-run, because every internal interval there is
contained in the selected rank-9 witness \(Q\).  It must therefore occupy one
of the singleton runs.  The sole entry of that run is then 15346 itself, and,
as in Theorem 2, no distinct rank-10 boundary target can use the same run.
That run has capacity one rather than two.  The total is at most seven, a
contradiction.

Thus a 242-term completion requires at least two genuinely nonliteral rank-9
targets. \(\square\)

This independently shows that a 242-term counterexample could not have lived
in either of the first two literal-defect regimes.

## 4. Exact search reduction and computational cross-check

### Scope warning

Theorems 1--3 concern a **standalone** word which, by itself, covers all
260 missing masks.  They are not lower bounds on an arbitrary suffix appended
to the existing length-3434 factor: a target witness crossing the old/new
seam need not satisfy this standalone marked-run decomposition.  In
particular, none of these theorems is a new lower bound on the length of a full
universal `k=14` array.

Let \(M=238\) and suppose a completion has length \(M+4=242\).  Select one
witness interval for every missing rank-9 mask.  The standard nonnesting-band
argument gives:

\[
\text{every selected rank-9 witness has length at most }5.
\]

Moreover, every physical interval of length at least five contains one of
those selected rank-9 witnesses.  Since 15346 contains no missing rank-9
target, its witness has length at most four.

There is a stronger target-sensitive form.  If a rank-10 target \(T\)
contains exactly \(c(T)\) of the 238 missing rank-9 masks, then every witness
for \(T\) has length at most

\[
4+c(T).
\]

Indeed, a physical interval \(J=[a,b]\) of length \(\ell\ge5\) contains the
selected rank-9 witness \(I_i\subseteq[i,i+4]\) for every
\(i=a,a+1,\ldots,b-4\).  These are \(\ell-4\) distinct missing rank-9 masks,
and all must be subsets of \(U(J)=T\).  Hence \(\ell-4\le c(T)\).  In the
present instance \(c(T)\le4\), so no required upper witness is longer than
eight.

The endpoint arithmetic has no hidden boundary exception.  Since
\(b\le n=M+4\), an interval of length at least five has \(a\le M\), while
\(b-4\le M\).  Thus every index in \([a,b-4]\) is a valid selected-witness
index in \([1,M]\), including when \(J\) touches either end of the word.

These two facts give a substantially smaller exact SAT formulation than a raw
all-interval search:

* 242 by 14 entry-bit variables;
* shared exact OR variables for every physical interval;
* rank-9 selectors only for intervals of lengths 1 through 5;
* each rank-10 target \(T\) only for intervals of lengths 1 through
  \(4+c(T)\), at most 8 here;
* distinct selected left and right endpoints within each rank.

The source is `scratch/k14_partial_completion_interval_sat.cpp`.  It is an
exact formulation of the standalone 260-mask completion problem; it imposes
no literal-lower, fixed-forest, fixed-order, or fixed-window assumption.

The exact length-242 searches were stopped after Theorem 1 made them
mathematically redundant.  No SAT/UNSAT solver result is used in the proof.

## 5. Verification and artifacts

Any returned 242-term word must be checked independently in two ways:

1. enumerate every one of its \(242\cdot243/2=29,403\) intervals and confirm
   that all 260 target masks occur;
2. append it to `k14_pinnable_factor_missing260.txt` and run the independent
   distinct-suffix-OR verifier over all 16,383 nonzero 14-bit masks.

The existing 243-term word passes both checks.  Its standalone witness file is
`k14_completion_243_witnesses.txt`; the full concatenated word is
`k14_completed_best.txt`.  The exact standalone optimum is therefore 243.

SHA-256 values:

| artifact | SHA-256 |
|---|---|
| `k14_pinnable_factor_missing260.txt` | `4c71a5e59985ff8d78a4ae80845defd21cebfe240c16ad4604b57e9b9cb999ad` |
| `k14_missing_260.txt` | `152e7e9d951e96c0600875d674f78333b634622e4c34262f44de51053fbd64ab` |
| `k14_completion_best.txt` | `06f4b5a06f411a896df9d471b4e2f60d97eea537b4c81710f5e1c62117d68b19` |
| `k14_completion_243_witnesses.txt` | `63a5f7a51e7e873db394e92cfd606c027405971598377fa96a838a9c0ac58590` |
| `k14_completed_best.txt` | `d5fc5c13685ca0e2eb182de0d245e93368453d0aaeaf6e2f5cfdff219a59c83c` |
