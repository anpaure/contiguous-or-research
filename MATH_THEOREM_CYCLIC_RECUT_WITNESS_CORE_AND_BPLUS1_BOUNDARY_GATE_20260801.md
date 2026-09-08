# Cyclic recutting is controlled by witness-interior cores, and one surplus only opens the boundary

Date: 2026-08-01  
Lane: cyclic linearization / flat coefficient-one carrier / `B+C` recut gate  
Status: exact cyclic-witness theorem, exact flat-window count, and finite
`B+1` calibration.  This is a pure-rotation obstruction, not an owner-rethread
obstruction.

## 0. Outcome

For a target `S` in a cyclic set word, intersect the interior-edge sets of
all cyclic intervals whose OR is `S`.  A cut destroys `S` exactly when the
cut edge lies in this intersection.

Consequently, if a length-`W+d` word carries `W` distinct flat owners and the
owner at start `s` has the unique eligible length-`d+1` cyclic witness

\[
                              [s,s+d],\qquad 1\le s\le W,     \tag{0.1}
\]

then every internal edge lies inside the unique witness of some owner.  No
internal pure recut retains the complete coefficient-one owner row.  The
only safe cut is the original outer boundary.

At length

\[
                              L=W+d+C,                         \tag{0.2}
\]

the exact number of original flat windows which avoid a cut after `a`
positions is

\[
 N(a)=\max(0,a-d)+\max(0,L-d-a)
     =\max(0,a-d)+\max(0,W+C-a).                              \tag{0.3}
\]

If `C<d`, the necessary condition `N(a)>=W` forces

\[
                              a\le C\quad\hbox{or}\quad a\ge L-C. \tag{0.4}
\]

Thus `C=0` permits no internal safe recut.  For `C=1<d`, the only
nontrivial candidates are the two boundary-adjacent cuts `a=1` and
`a=L-1`.  They are not automatically safe: the first requires the unused
flat start to be the first start, and the second requires it to be the last.
With only one unused start, at most one of the two can work.

This calibrates the `B+1` possibility sharply.  One surplus can move the
outer boundary across one unused extreme window; it does not create an
arbitrary internal rotation.  A new owner chronology, alternate witnesses,
or a nonflat rethread can escape because it changes the witness system.

## 1. The cyclic witness core

Let

\[
                          C=(C_0,\ldots,C_{L-1})               \tag{1.1}
\]

be a cyclic word of nonempty sets.  Its cyclic edges are indexed by their
left endpoint: edge `e` joins `C_e` to `C_(e+1 mod L)`.

An oriented cyclic interval `I` is a consecutive vertex arc.  Its interior
`int(I)` is the set of edges traversed between its first and last vertices.
A singleton has empty interior.  A full-cycle interval may be rooted at any
vertex; these `L` rooted witnesses have different omitted boundary edges, as
they should.

For a target `S` occurring in the cyclic interval deck, let

\[
 \mathcal W_C(S)=\{I:\operatorname{OR}_C(I)=S\},\qquad
 \mathfrak b_C(S)=\bigcap_{I\in\mathcal W_C(S)}\operatorname{int}(I). \tag{1.2}
\]

Call `b_C(S)` the witness-interior core of `S`.

### Theorem 1.1 (exact cyclic recut criterion)

Cut the cycle at edge `e` and read the remaining path as a linear word.
Then

\[
 \boxed{
 S\text{ survives as a linear interval OR}
 \quad\Longleftrightarrow\quad
 e\notin\mathfrak b_C(S).}                                  \tag{1.3}
\]

For a target family `T`, the cut preserves every target if and only if

\[
                         e\notin\bigcup_{S\in\mathcal T}
                                           \mathfrak b_C(S). \tag{1.4}
\]

#### Proof

A cyclic interval is a contiguous interval after cutting at `e` precisely
when it does not traverse `e` internally.  Therefore `S` survives precisely
when at least one witness `I` has `e notin int(I)`.  This is equivalent to
`e` not belonging to the intersection of all witness interiors.  Intersect
the survival conditions over the target family to obtain (1.4). \(\square\)

If `S` has one cyclic witness `I`, then

\[
                              \mathfrak b_C(S)=\operatorname{int}(I). \tag{1.5}
\]

Multiple witnesses can make the core smaller or empty.  This is why
coefficient-one or another literal uniqueness hypothesis is essential.

## 2. Exact-`B` flat carrier obstruction

Let a linear word have length `W+d`, and close its two ends only for the
purpose of considering recuts.  Suppose it has distinct rank-`r` owners
`O_1,...,O_W`, where `O_s` has the unique eligible cyclic length-`d+1`
witness

\[
                              I_s=[s,s+d].                     \tag{2.1}
\]

Here *eligible* may mean all length-`d+1` cyclic intervals, or a more
restricted authenticated flat row.  If uniqueness is asserted only in that
row, the conclusion concerns preservation of that row; target-level absence
requires uniqueness among all cyclic witnesses of the target.

### Theorem 2.1 (no internal coefficient-one recut)

Every internal edge of the length-`W+d` line is blocked by one of the unique
owner witnesses (2.1).  Hence no nonidentity pure rotation retains the full
flat coefficient-one owner row.  The original outer boundary is the only
safe linearization cut.

#### Proof

Index an internal edge by the number `a` of positions on its left, so
`1<=a<=W+d-1`.  Take

\[
                              s=\max(1,a-d+1).                 \tag{2.2}
\]

Then `1<=s<=W` and `s<=a<=s+d-1`, so edge `a` lies in the interior of
`I_s`.  Since `I_s` is the unique eligible witness of `O_s`, cutting there
loses that owner occurrence.  None of the intervals (2.1) crosses the
original outer boundary, so that boundary is safe. \(\square\)

This is stronger than a dimension count: it names a blocking owner at every
internal edge.

## 3. The exact `B+C` count

Now let `L=W+d+C`.  There are

\[
                              L-d=W+C                           \tag{3.1}

nonwrapping length-`d+1` windows in the original linearization.  Suppose the
`W` distinct owners have unique eligible cyclic witnesses among these
windows.  Their starts are therefore `W` distinct elements of
`{1,...,W+C}`.

Cut after `a` positions, `0<=a<=L`.  A surviving original flat window lies
entirely in the left segment of length `a` or in the right segment of length
`L-a`.

### Theorem 3.1 (cut capacity)

The number of original flat windows avoiding the cut is exactly (0.3).  A
pure recut which retains all `W` uniquely witnessed owners must satisfy

\[
                              N(a)\ge W.                        \tag{3.2}
\]

If `0<=C<d`, condition (3.2) implies (0.4).

#### Proof

A line segment of length `m` contains `max(0,m-d)` windows of length
`d+1`.  Applying this to the two sides of the cut proves (0.3).

If `a<=d`, the first term is zero, and `N(a)>=W` gives `a<=C`.  If
`a>=W+C`, the second term is zero, and `N(a)>=W` gives
`a>=W+d=L-C`.  In the remaining region both terms are positive and

\[
                              N(a)=W+C-d<W                       \tag{3.3}
\]

because `C<d`.  This proves (0.4). \(\square\)

### Corollary 3.2 (`B+1` boundary gate)

Assume `d>=2` and `C=1`.  There are `W+1` possible original flat starts and
exactly one is unused.

* The cut `a=1` is safe exactly when start `1` is unused.
* The cut `a=L-1` is safe exactly when start `W+1` is unused.
* No other internal cut is safe under the uniqueness hypothesis.

Thus at most one nontrivial recut exists, and it merely moves the outer
boundary across the unique extreme slack window.  If the unused start is
internal, no internal recut survives.

When `d=1`, `C=1` is not below `d`, so the boundary conclusion does not
apply.  When `C>=d`, the middle value `W+C-d` in (3.3) is at least `W`; the
count alone then gives no recut obstruction.

## 4. What “survival” means

There are three nested statements which must not be conflated.

1. **Target support.**  Theorem 1.1 uses every cyclic witness of every
   length.  It decides whether the set value remains anywhere in the linear
   interval deck.
2. **Flat owner-row support.**  Theorems 2.1 and 3.1 use eligible
   length-`d+1` witnesses.  An alternate witness of another length may save
   the OR target while failing to save the flat derivative row.
3. **Selected occurrence transport.**  If one named witness is to remain the
   same physical occurrence, its own interior blocks the cut even when the
   target has an alternate occurrence elsewhere.

The phrase “unique owner” in the recut obstruction must therefore mean a
unique eligible witness, not merely a distinct owner value in the original
row.

## 5. `B+1` calibration

The audit performs three independent calibrations.

### 5.1 Saved optimal words

For each saved answer `k=3,...,16`, the replay checks whether its first
`W` length-`d+1` windows form a flat coefficient-one middle row, counts all
cyclic flat witnesses, and tests every cut after legal duplicate-letter
splits `X -> X,X`.  All split positions are tested through `k=10`; the first,
middle and last positions are tested for the longer words.

The saved words for `k=3,6,...,15` are flat; `k=4,5,16` are not flat at the
original cut in this specific representation, but their duplicate-letter
expansions are still tested as calibration outside Theorem 3.1's premise.
Among the flat words:

* `k=3,10,11,12,13,14,15` have unique cyclic flat witnesses before the
  split;
* `k=6,7,8,9` have extra cyclic owner occurrences, so Theorem 2.1's
  uniqueness hypothesis is absent;
* `k=6` already has a nonidentity owner-preserving shift at exact length;
* for every flat saved word, duplicating the first or last source letter
  exhibits the expected boundary-adjacent `B+1` recut;
* for the unique-witness cases with `d>=2`, a tested middle duplication does
  not give a complete flat owner row after any cut; and
* the nonflat saved `k=4` word has one successful duplicate site and two
  owner-complete recuts.  Here `d=C=1`, so the hypothesis `C<d` is false and
  this is not an exception to Corollary 3.2.  No tested duplicate works for
  the saved `k=5` word or the three sampled sites of the saved `k=16` word.

The output records whether each expanded word remains coefficient one and
whether cyclic uniqueness survives; the mere presence of all owner values
is not silently promoted to either stronger property.

The three saved `k=16` upper words of lengths `12874,12875,12876` are also
tested separately at the inherited depth `d=3`.  None has a cyclic cut whose
flat row contains all `12870` middle owners; these records are calibration,
not a claim that every `k=16` `B+1` construction fails.

### 5.2 Rotating-hole split

For every `2<=d<=32`, split the actual rotating-hole host letter as

\[
                   A_d^-=\{\epsilon\}\cup\tau
                       \longmapsto \{\epsilon\},\tau.        \tag{5.1}
\]

Every reference target and the new task survive at the original cut.  The
transported owner witnesses cover every internal edge of the expanded word:
`d+1` owners use length `d+2`, and the remaining two use length `d+1`.
Exhaustive recutting finds:

\[
 \begin{aligned}
 &\text{cuts preserving the complete reference support plus task}=\{0\},\\
 &\text{cuts carrying all owners in one flat length-`d+1` row}=\varnothing.
                                                               \tag{5.2}
 \end{aligned}
\]

Thus the `+1` split is a valid nonflat OR repair, but it supplies no hidden
flat lost/gained-window permutation.

### 5.3 Conditional mixed-coatom two-ray split

The local split

\[
 (A+f_1)\cup(B+f_d)\longmapsto A+f_1,\ B+f_d               \tag{5.3}

creates both canonical rays.  For every `3<=d<=24`, cutting between the two
new pieces preserves both ray banks, but fails to preserve the old local
interval support.  The original cut is the only cut preserving the old
support and both new rays simultaneously.

This is a local trace calibration, not a complete coefficient-one carrier;
the canonical packet also lacks the actual dominating source envelope
required by (5.3).

## 6. Exact scope and escape routes

The theorem forbids only **pure recutting of a fixed cyclic word with a fixed
eligible witness system**.  It does not forbid:

* changing source letters or their cyclic order;
* replacing the flat owner row by variable-length transported witnesses;
* constructing alternate witnesses which shrink the cores (1.2);
* inserting a collar and rethreading the owner chronology;
* regenerating a fresh `W+d+C` source after the cut; or
* using `C>=d`, where the elementary count ceases to obstruct interior cuts.

In particular, an owner rethread can escape by moving the unique witnesses
so that the proposed cut lies outside their interiors.  Nothing here proves
that such a rethread is impossible.

## 7. Audit

Run

```text
python3 scratch/audit_cyclic_recut_witness_core_and_bplus1_20260801.py
```

The dependency-free replay checks:

* Theorem 1.1 on all `3,276` cyclic words of lengths `2,...,7` over the
  nonempty two-bit alphabet, comprising `60,837` target/cut tests;
* formula (0.3) and implication (0.4) over `104,520` parameter/cut tests,
  plus `9,460` exact missing-extreme `B+1` tests;
* the saved-answer calibration through `k=16`;
* the rotating-hole split through `d=32`; and
* the conditional coatom split through `d=24`.

It reports

```text
PASS_CYCLIC_RECUT_WITNESS_CORE_AND_BPLUS1_BOUNDARY_GATE
```

with hashes

```text
audit script SHA-256:
8d6f292e44f695f20f326ee64353fe10210874edc7eabc85360cdf07ce13e7c3

audit JSON SHA-256:
147aaa64eb602d56c21e8d4196e5d0518f2cf5925cbaf82d5e4ac972d3a9794c

canonical payload SHA-256:
7f6087231df99361afa2894169dc80c803812e2bf6d20f1b1882ec930a4321d1
```

Dependencies:

* `MATH_THEOREM_H1_SPLIT_LETTER_RAY_ABSORPTION_AND_ONE_COLUMN_CRITERION_20260801.md`;
* `MATH_THEOREM_NONFLAT_SPLIT_LETTER_TWO_COATOM_RAYS_AND_NATIVE_HOST_GATE_20260801.md`; and
* `scratch/audit_h1_flat_carrier_cyclic_recut_20260801.py`.
