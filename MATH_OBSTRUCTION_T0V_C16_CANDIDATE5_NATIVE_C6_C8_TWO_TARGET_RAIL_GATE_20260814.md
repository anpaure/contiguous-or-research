# The candidate-5 two-target rail has no native `C6/C8` one- or two-cycle zero-current closure

**Date:** 2026-08-14
**Status:** unconditional for the literal `m=9` candidate-5 factor, the
complete rank-correct five-owner adjacent-window rail census, the complete
target-relevant native `C6/C8` single-cycle atlases, and commuting
owner-and-colour-disjoint pairs from those atlases.  Overlapping sequential
cycles, longer native cycles, and a cut-open marked collar are not
classified.

## 0. Result

Retain binary `C16` candidate 5 from the frozen thirteen-root scaffold.  At
the first singleton fibre `V=110100`, its two lost upper-`q3` values are

```text
A = 100011010111110111,
B = 100010011111110111.                              (0.1)
```

They have rank twelve, their intersection has rank eleven, and they differ
by one Johnson exchange.  A five-owner rank-nine Johnson rail can create
both as consecutive four-owner unions.  The complete literal census has

```text
721710 simple rails,

missing current-factor incidences:
3:    404
4:   8406
5:  61536
6: 202132
7: 296940
8: 152292.                                          (0.2)
```

Every rail has five distinct owners and four distinct upper colours.  None
of the `404` three-missing rails closes as a native alternating `C6`, and
none of the `8810` rails missing at most four incidences completes to a
native alternating `C8`.

The stronger atlas calculation is independent of this particular rail
parametrization.  From `1936` exhaustive target start arcs in the current
factor it finds

```text
native target-relevant C6 cycles:   382  (A:6,  B:5,  both:0),
native target-relevant C8 cycles:  1495  (A:22, B:25, both:0). (0.3)
```

Finally, index every cycle by its complete typed-current signature through
`q2`.  There are exactly zero inverse-signature pairs in each menu

```text
C6+C6, C6+C8, C8+C8.                                (0.4)
```

Thus no commuting owner-and-colour-disjoint pair from these complete
target-relevant banks can both have zero typed current through `q2` and
repair `(0.1)`; the typed-current gate already fails before common binary
phase, topology, or residence is tested.

The sharp continuation is a nonnative marked collar around the open rail,
or an overlapping/longer native construction.  It must be keyed by the
injective `c0(V)` data, not only by the collapsed target `G2(V)`.

## 1. Rank-correct adjacent-window normal form

Let owner rank be `R`, let `H=A intersect B` have rank `R+2`, and write
`A=H+a`, `B=H+b`.  Choose distinct `h1,h2,h3,h4` in `H` and put

```text
O1 = H-{h1,h2},
O2 = H-{h2,h3},
O3 = H-{h3,h4},
O0 = O1-u+a,
O4 = O3-v+b,                                        (1.1)
```

where `u in O1`, `v in O3` and the five owners are distinct.  Consecutive
omission pairs in `(1.1)` meet in one coordinate, so `O1,O2,O3` form a
Johnson path.  Their union is all of `H`, because the three omission pairs
have empty common intersection.  Therefore

```text
O0 union O1 union O2 union O3 = A,
O1 union O2 union O3 union O4 = B.                  (1.2)
```

At `(0.1)`, `R=9`.  One literal witness is

```text
O0  000001000111110111
O1  000000010111110111
O2  000010000111110111
O3  100000000111110111
O4  000000001111110111.
```

Its four upper colours are

```text
000001010111110111
000010010111110111
100010000111110111
100000001111110111.
```

They are pairwise distinct.  This also shows why the tempting
same-upper-colour obstruction is inapplicable: omitting one common
coordinate from the middle union would prevent an endpoint from restoring
that coordinate and adding `a` or `b` in a single exchange.

Every consecutive-window rail has this complement-of-two-subsets normal
form.  Enumerating the omission chain and the two endpoint exchanges gives
the total and histogram in `(0.2)`.

## 2. Native single-cycle obstruction

For every colour of the current factor, record its two selected owner
mates.  A missing rail incidence specifies one new mate.  Three missing
incidences can be the new matching of a closed `C6` only if one can select
the old mates with the same owner set and the six toggled incidences form
one connected alternating cycle.  All `404` possibilities fail this exact
test.

For a `C8`, four missing incidences are tested directly.  When only three
are missing, the search also enumerates the fourth old/new owner exchange,
then independently rechecks the selected mates, degree two at every
support vertex, and connectedness.  No completion exists.

The exhaustive atlas then removes dependence on a chosen open rail.  A
new provider of `A` or `B` must contain a new incidence whose colour is a
subset of that target.  Enumerating every possible such start arc and
extending it to every simple alternating `C6` or `C8`, with support
deduplication, yields `(0.3)`.  Direct full upper-`q3` replay confirms that
no single cycle creates both values.

## 3. Exact two-cycle inverse-signature obstruction

For each cycle `C`, compute the exact occurrence current

```text
J(C) = (owner, upper-q1, lower-q1, upper-q2, lower-q2).  (3.1)
```

For owner-and-colour-disjoint simultaneous cycles, these currents add
without cross terms.  Consequently zero typed current is equivalent to
`J(C2)=-J(C1)`.  Hashing the complete target-relevant banks by `(3.1)` and
looking up the inverse signature gives zero candidate pairs in all three
menus `(0.4)`.  This is stronger than finding no final repair: no such pair
even reaches the target or phase tests.

Target relevance is complete for the stated two-cycle question.  Any new
`A/B` provider uses at least one newly inserted incidence contained in the
corresponding target.  If only one cycle had such an incidence, the other
could not change the target-local provider graph; the first cycle would
then create both values alone, contrary to `(0.3)`.  Hence both members of
any repairing pair occur in the enumerated banks.

The owner-and-colour-disjoint hypothesis is essential.  It makes the
cycles commuting conformal substitutions and makes `(3.1)` additive.
Overlapping sequential switches may have cross terms and are outside the
no-go.

## 4. Minimal marked-collar reduction

The open rail itself is positive: installing its four edges creates both
targets.  However every literal rail is missing at least three factor
incidences, and no minimum three-incidence set is the new side of a closed
native `C6`.  Thus a minimum-size realization must expose at least one
boundary mismatch instead of closing internally.  A proof-safe marked
collar must:

1. install a rank-correct five-owner rail selected from `(1.1)`;
2. expose and reconnect the unmatched old/new owner or colour darts;
3. cancel the complete typed current `(3.1)`, including cross terms at the
   reconnection;
4. preserve a common binary phase with the candidate-5 scaffold;
5. have a certified contractible component action; and
6. choose its omission chain and endpoint exchanges injectively from
   `c0(V)` so different suffix copies have disjoint resources.

The native no-go does not prove that such a cut-open collar exists.  It
does prove that merely closing the rail with one native `C6/C8`, or with
two commuting resource-disjoint cycles of those sizes, cannot supply it.

## 5. Scope

This note closes the requested smallest native `C6/C8` suffix-side menu at
the first bad candidate-5 fibre.  It does not classify:

* overlapping or sequential switches;
* a single native cycle of length at least ten;
* three or more native cycles;
* the marked cut-open collar in Section 4; or
* cross-suffix common-history/residence coinstantiation.

Those are deliberately left as the all-`k` q3 boundary; no broader q3
atlas is opened here.
