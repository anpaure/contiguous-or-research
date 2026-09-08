# Independent audit of the exact fixed-prefix `k=14`, `q=241` append encoding

## Verdict: **PASS**

I audited the frozen source

```text
scratch/k14_append241_exact.cpp
SHA-256 b4b7b586766906bf0727adeb587cccb98cb57b9783e9e3059498bce292fab964
```

as an encoding of the following decision problem:

> Does the designated 3,434-entry `k=14` prefix admit a 241-entry
> nonzero append whose combined word covers every nonzero 14-bit mask?

For the designated prefix `k14_pinnable_factor_missing260.txt` and its exact
missing family `k14_missing_260.txt`, the disjunction of the 52 generated
branches is **sound and complete**.  More precisely, each branch is SAT iff
there is an append together with one exact witness for every missing target
having that branch's selected rank-nine crossing pattern and endpoint profile;
the 52 branches cover every possible 241-entry completion.

The phase-selection additions in the frozen version affect only CaDiCaL's
preferred polarities.  They add no logical restriction.

This audit does **not** say that a branch is SAT or UNSAT.  A SAT result must
still yield and verify an explicit append.  A global UNSAT conclusion requires
all 52 branches to be refuted, with independently checked proof certificates
if a proof-producing result is claimed.

## 1. Input binding and the exact residual problem

The source independently recomputes all masks covered by the supplied prefix
and requires the target vector to equal, in increasing mask order, the exact
missing family.  It then requires precisely 238 rank-nine and 22 rank-ten
targets.  Therefore no already-covered mask needs a new witness, and every
modeled target does need one.  Appending entries cannot destroy any old
witness.

Every target is absent from the prefix.  Consequently any new witness ends in
the appended word.  It has exactly one of two forms:

1. an append-only interval `[l,r]`; or
2. an old/new crossing interval consisting of the fixed old suffix beginning
   at old position `s`, followed by appended positions `[0,r]`.

The source represents exactly these two forms.  For every target it enumerates
**all** old starts whose fixed suffix OR is a subset of the target.  There is no
old-start truncation in the target encoding.

The entry variables are unrestricted 14-bit masks except for a nonzero clause.
This is the intended nonzero problem.  Even if zero entries were initially
allowed, this restriction would preserve existence at length 241: delete all
zeros from a completing append, then pad its end with arbitrary nonzero masks
to restore length 241.  Deletion preserves every old or crossing nonzero OR
witness, and end padding does not destroy coverage.

## 2. Exact interval variables

For each target `S` and appended position `p`, the encoding uses:

- `left[p]`: `p` is at or to the right of the selected appended left endpoint;
- `right[p]`: `p` is at or to the left of the selected right endpoint;
- `inside[p]`: both predicates hold;
- `new_start[p]`: the append-only witness starts at `p`;
- `end[p]`: the witness ends at `p`;
- one selector for each compatible old start; and
- `cross`, equivalent to the OR of the old-start selectors.

The clauses make `left` a `0...01...1` threshold, with `left[240]=1`.
When `cross=1`, `left[0]=1`, so the whole appended prefix through the selected
right endpoint is included.  When `cross=0`, exactly one `new_start` marks the
`0`-to-`1` transition of `left`.

Likewise, `right` is a nonempty `1...10...0` threshold with `right[0]=1`, and
exactly one `end` marks its final `1`.  The three clauses for `inside[p]` give

```text
inside[p] <-> left[p] AND right[p].
```

The disjunction of the `inside` variables rules out a left endpoint after the
right endpoint.  Hence every target selects exactly one nonempty contiguous
appended portion, plus exactly one compatible fixed old suffix iff it crosses
the seam.

The sequential `at_most_one` implementation is correct, including the
two-variable boundary case.  Applying it separately to all same-rank starts
and ends is safe: two distinct equal-rank target intervals sharing a left or
right endpoint would be nested, so their OR masks would be comparable; equal
cardinality would then force the targets to be equal.  Old and new starts are
different physical domains and are correctly handled separately.

## 3. Exact OR clauses

For a bit absent from target `S`, every selected appended position is forced
not to contain it.  Every eligible fixed old suffix was prefiltered to be a
subset of `S`, so an absent bit cannot enter from the old side either.

For a bit present in `S`, one support literal is required.  A support is either

- the selected old suffix selector, when that suffix contains the bit; or
- a `hit` implying both `inside[p]` and that appended entry's bit variable.

Thus every required bit actually occurs in the selected physical interval,
and no forbidden bit occurs there.  The `hit` variables need only imply, not be
equivalent to, `inside AND entry`: the support disjunction proves existence,
and leaving additional true interval bits unmarked cannot weaken exactness.

It follows that every satisfying assignment supplies an actual interval OR
equal to each missing target.  Conversely, any chosen exact physical witness
sets the threshold, selector, endpoint, and suitable hit variables so as to
satisfy these clauses.

## 4. Exhaustive crossing-pattern inventory

The independently audited old suffix chain leaves four old starts compatible
with missing rank-nine masks, with compatibility counts

```text
12411: 1,  12409: 1,  12393: 7,  12329: 18.
```

The first two support the same sole target `12923`.  Therefore a selected
equal-rank witness family uses at most three old starts.

Order selected crossing witnesses by increasing old start.  Their old suffixes
form a decreasing inclusion chain `C_1 superset ... superset C_x`; nonnesting
forces their appended right endpoints, and hence appended prefix ORs, to be
increasing.  If target `S_i` is assigned to `C_i`, the smallest possible
cumulative appended requirement satisfies

```text
P_i = P_(i-1) OR (S_i without C_i).
```

Such a nested prefix chain exists exactly while `P_i` remains a subset of
`S_i`.  This is precisely the recursion at source lines 103--129.  It is both
necessary and sufficient: when the test passes, `C_i OR P_i = S_i` at every
step.  The final CNF still enforces the actual prefix ORs, so the enumerator is
allowed to be an overapproximation with respect to endpoint timing but cannot
admit a false SAT model.

The resulting raw counts are exactly:

```text
x=1: 27 patterns
x=2: 27 patterns
x=3:  6 patterns
```

For `x=1`, 18 patterns consume old position 3434 and 9 do not.  For `x=2`,
23 consume position 3434 and 4 do not.  Every `x=3` pattern consumes it.  These
figures follow directly from the independently verified pair table

```text
0, 2, 9, 2, 6, 8
```

and the six verified triples.  They also explain the source's `h` value:

- if old position 3434 remains free, hard targets `13439` and `13757` have two
  distinct usable old-start resources, so `h=2`;
- if it is consumed by a rank-nine witness, only the `13439` resource remains,
  so `h=1`.

The always-available earlier old start for `13439` is not compatible with a
missing rank-nine target, so no other selected rank-nine start reduces `h`.

## 5. Why exactly 52 profile branches are exhaustive

The 238 selected rank-nine witnesses have 238 distinct new right endpoints in
241 appended positions, leaving three lower-free new right endpoints.  Let
`f` be the number of the seven unique-base hard rank-ten targets whose selected
right endpoint is lower-free.  The exceptional target `15346` contains no
missing rank-nine target and must itself consume a lower-free right endpoint;
hence `f<=2`.

Every one of the other `7-f` hard targets shares its right endpoint with its
unique contained missing rank-nine target.  It cannot share that lower
witness's left endpoint as well, because then the two physical intervals would
be identical.  The exceptional target also needs a lower-free left endpoint.
Thus at least `8-f` hard witnesses need lower-free left endpoints.

If `x` rank-nine witnesses start old, the number of lower-free new starts is
`3+x`, and the usable old hard-start capacity is `h`.  Therefore every actual
completion obeys

```text
8 - f <= 3 + x + h.
```

Together with the exact old-start geometry, this gives precisely the source's
profiles:

| `x` | allowed `(f,h)` |
|---:|---|
| 1 | only `(2,2)` |
| 2 | `(2,1)`, `(2,2)`, or `(1,2)` |
| 3 | `(1,1)` or `(2,1)` |

The pattern split then gives

```text
x=1:  9 h=2 patterns * 1 f-value  =  9 branches
x=2: 23 h=1 patterns * 1 f-value
     +4 h=2 patterns * 2 f-values = 31 branches
x=3:  6 h=1 patterns * 2 f-values = 12 branches
                                          --------
                                             52 total
```

The standard endpoint-capacity proof rules out `x=0`, while the old-start
matching bound gives `x<=3`.  Hence no possible suffix lies outside these 52
branches.

The CNF definition of `used9[p]` is exactly the OR of rank-nine endpoint flags.
For each unique-base hard target, `free` is exactly the statement that its
unique selected endpoint has `used9=0`.  The direct subset cardinality clauses
correctly enforce exactly `f` of the seven free flags.  The exceptional target
is explicitly forbidden from ending at a used rank-nine endpoint.  These
clauses encode the declared `f` profile exactly.  The hard-start resource
argument is used only to discard impossible profiles; remaining physical
left-endpoint conflicts are still enforced by the general rank-ten start
uniqueness clauses.

## 6. Safe rank-nine endpoint and length cuts

Sort the 238 selected rank-nine intervals by increasing left endpoint.  Their
right endpoints occur in the same order.  If the selected right endpoints are

```text
r_0 < r_1 < ... < r_237
```

inside zero-based positions `0,...,240`, then `r_i<=i+3`.

The `x` old-start witnesses are the first `x` intervals in left-endpoint order.
The source fixes the `i`-th selected crossing target's endpoint to at most
`i+3`, exactly matching this inequality, and forces crossing endpoints into
the same order.

For an append-only rank-nine witness, let it be the zero-based `s`-th new left
endpoint.  Its physical start is at least `s`, while its overall rank-nine
order is `x+s`, so its right endpoint is at most `x+s+3`.  Its appended length
is therefore at most `x+4`.  Forbidding two `inside` positions at distance
`x+4` is exactly the contiguous-interval encoding of this length bound.

No rank-ten length cutoff is imposed.  All crossing rank-ten starts compatible
with their targets remain available.  Thus these reductions remove no valid
completion.

## 7. Soundness and completeness summary

### Soundness

From any satisfying assignment, read the 241 nonzero entry masks.  Each target
has one genuine append-only or old/new physical interval whose exact OR is that
target.  The old prefix already covers every other nonzero mask.  Therefore
the concatenated word is universal.  The source additionally recomputes full
coverage before writing a SAT output, providing a defense-in-depth check.

### Completeness

Given any completing 241-entry nonzero append, choose one witness for each
missing target.  Equal-rank nonnesting gives distinct, consistently ordered
endpoints.  The endpoint argument yields `1<=x<=3`; its old-start assignments
appear in one of the `27,27,6` pattern lists; and its hard endpoint choices give
one of the valid `f,h` profiles.  The safe endpoint and length inequalities
hold.  Setting entry bits, thresholds, old selectors, endpoints, free flags,
and one hit per required bit satisfies that branch's CNF.

Therefore the OR over all 52 formulas is equivalent to existence of a
241-entry completion for the designated fixed prefix.

## 8. Non-fatal scope and provenance caveats

1. The source is an **exact designated-prefix solver**, not a general solver
   for every arbitrary 3,434-entry prefix with 260 omissions.  It recomputes
   the exact omission family and checks the `27,27,6` inventory, but the eight
   hard-target identities and the interpretation of `h` are hardcoded rather
   than rederived and asserted from arbitrary input.  They have already been
   independently verified for the designated prefix.  Supplying a different
   prefix that coincidentally passes the coarse counts is outside this audit's
   guarantee.  A prefix SHA check or runtime verification of all hard-target
   containment/resource facts would make that scope self-enforcing.

2. The seed file is used only for phase selection.  Requiring its entries to
   be nonzero and truncating it to 241 values changes search behavior, not the
   formula's solution set.

3. `required_prefix` is used to enumerate and report crossing patterns but is
   not separately fixed in the CNF.  This is intentional: the exact OR clauses
   already impose the actual prefix states, and omitting redundant equalities
   cannot create an invalid SAT append.

No soundness or completeness defect was found.
