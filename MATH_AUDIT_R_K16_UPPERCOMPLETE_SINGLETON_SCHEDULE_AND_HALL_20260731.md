# Upper-complete K16 facet rethread: singleton schedule and exact Hall gates

**Date:** 2026-07-31  
**Status:** exact fixed-schedule no-go results; fixed target order remains open

## 1. Frozen carrier

The target order is

```text
scratch/k16_facet_augmented_uppercomplete_capacity27597_targets_20260731.word
SHA-256 63aababe9d5cbaeec4ce68a1ec32edc02d249caf3750bb20f6bc87c1ca1eac43
```

It is obtained from the P9/P9 target order by the two inclusive block
reversals

```text
[5567..11365], then [11..11268].
```

Direct replay proves:

```text
distinct rank-eight targets                 12870 / 12870
distinct adjacent rank-nine colours         11440 / 11440
missing carrier-interval targets, ranks 9..16           0
adjacent union ranks                   9^12863 10^4 11^2.
```

Thus the former `0xef79` upper debt is gone.  The remaining obstruction is
entirely on the physical lower compiler side.

## 2. Exact individual lower-pin criterion

Fix a monotone P/Q schedule with middle rows

\[
  (I_i,T_i),\qquad I_i=[s_i,e_i],\quad |T_i|=8,
\]

and maximal envelopes

\[
 E_p=\bigcap_{i:p\in I_i}T_i.
\]

For an interval `J`, put

\[
 U_J=\bigcup_{p\in J}E_p
\]

and, for each row-bit incidence `(i,b)`, put

\[
 H(i,b)=\{p\in I_i:b\in E_p\}.
\]

The mandatory mask of `J` is

\[
 M_J=\{b:\text{some }(i,b)\text{ has }H(i,b)\subseteq J\}.
\]

### Lemma 2.1 (individual capped pin)

A lower target `S` can be realized on `J`, while preserving every middle row
and leaving every other position maximal, if and only if

\[
 M_J\subseteq S\subseteq U_J
 \quad\text{and}\quad
 E_p\cap S\ne\varnothing\quad(p\in J).              \tag{2.1}
\]

### Proof

Every physical letter lies inside its maximal envelope.  Hence an interval
with OR `S` forces every letter on `J` into `E_p cap S`, proving the upper
inclusion and nonzeroness in (2.1).  If all hosts of a scheduled row-bit lie
in `J`, that bit must belong to `S`, proving the mandatory inclusion.

Conversely set the letters on `J` equal to `E_p cap S` and leave all other
letters equal to `E_p`.  The resulting OR on `J` is exactly `S`; every cell
is nonzero; and a scheduled row-bit can disappear only when all of its hosts
lie in `J` and it is omitted by `S`, which (2.1) forbids.  QED.

Consequently, an exact lower compiler induces an injection from the 26,332
lower targets to individually legal proper-prefix cells.  Ordinary Hall is
therefore necessary before the stronger simultaneous capped-envelope or
common-Q equations are imposed.

## 3. The unconstrained area-maximizing schedule is dead

The complete three-hole envelope DP gives

```text
start holes       {5722,10950,10951}
deadline holes    {10,12,13}
depths             0^1931 1^1 2^5227 3^5711
selected area      27588
omitted-start credit upper bound 9
total scalar capacity upper bound 27597.
```

The maximal envelopes are nonzero and replay every middle row.  Granting
all nine possible length-one/two/three prefixes at the omitted starts gives
an outer graph with

```text
right cells                 27597
individual incidences      293968
zero-degree lower targets    1478 = 1^1 6^27 7^1450
maximum matching            24328 / 26332
Hall deficiency              2004
alternating Hall shore       4029 / 2025.
```

The unique zero-degree singleton is `0x8000`.  Since the graph already
grants every omitted start its maximum possible three cells, this is an
exact no-go for the displayed schedule.  Simultaneous common-Q constraints
cannot repair a deficient outer graph.

## 4. Correct complete singleton-capped P/Q theorem

The singleton no-host is **not** schedule-independent.  An earlier transient
calculation reporting maximum singleton-compatible area `21878` was false
and must not be used.

On the maximizing schedule, `10,478` optimistic proper-prefix cells have the
top bit in every physical envelope position.  Every one nevertheless has a
mandatory bit outside `0x8000`; the minimum outside-mandatory rank is one,
attained by `1,176` cells.  Thus the exact local socket condition is

\[
  0x8000\subseteq E_p\quad\text{and}\quad
  M_{\{p\}}\subseteq0x8000.                         \tag{4.0}
\]

The first schedule fails the second clause everywhere.  Moving the first
start hole four places left creates precisely such a socket at position
5717, demonstrating directly that this no-host is a P/Q endpoint condition,
not an invariant of the target order.

### Lemma 4.1 (singleton reduction)

If a nonempty physical interval has OR `0x8000`, every letter in that
interval equals `0x8000`.  Hence every universal word contains a physical
cell equal to `0x8000`.

### Lemma 4.2 (maximal capped envelope)

For a fixed P/Q schedule and position `p`, a middle-realizing word with
`A_p=0x8000` exists if and only if the word

\[
 C_p=0x8000,\qquad C_j=E_j\ (j\ne p)                \tag{4.1}
\]

is nonzero and replays every middle row.

### Proof

Necessity follows because any feasible word is coordinatewise contained in
the word (4.1), while both are contained in every prescribed middle target.
If the smaller word supplies every target bit, so does (4.1).  Sufficiency is
immediate because (4.1) itself is a word.  QED.

Augmenting the exact P/Q queue DP by one Boolean state recording whether the
singleton cap has been used is therefore complete.  Independent
implementations agree on the exact optimum:

```text
maximum selected area       27584
capacity upper bound        27593
start holes                 {5718,10950,10951}
deadline holes              {10,12,13}
singleton cell              position 5717
middle replay failures      0.
```

The uncapped envelope at position 5717 is `0xa045`; replacing it by
`0x8000` preserves all four covering middle rows.  Thus the target order
survives singleton capacity, with scalar slack `27593-26332=1261`.

## 5. The best singleton-compatible schedule also fails Hall

Reserve the proper-prefix cell `(5717,1)` for `0x8000`.  Recompute maximal
carriers after that cap, remove the reserved cell, and grant all nine
omitted-start prefixes to the remaining 26,331 lower targets.  The complete
graph has

```text
total right cells, including reserved       27593
available right cells                        27592
remaining target-to-cell incidences         293943
remaining zero-degree targets                 1478 = 6^27 7^1451
maximum matching                             24328 / 26331
Hall deficiency                               2003
alternating Hall shore                        4027 / 2024.
```

Only one optimistic omitted-start cell lies in the Hall neighbor shore.
Therefore this singleton-compatible maximizing schedule is also
compiler-dead before common-Q.

## 6. Exact boundary

Proved:

1. the two-reversal carrier is squarefree in the middle and complete at q1
   and every upper depth;
2. its unconstrained area-maximizing schedule is lower-Hall impossible;
3. the complete singleton-capped schedule DP has optimum `27584`, not
   `21878`; and
4. that optimum singleton-compatible schedule is lower-Hall impossible.

Not proved:

1. no lower-area P/Q schedule of the same target order has a full lower
   matching;
2. any Hall-perfect schedule has a simultaneous capped-envelope/common-Q
   realization; or
3. the wider colour-preserving alternating-path/reversal mechanism is dead.

The exact remaining fixed-order problem is therefore a **schedule-plus-Hall
problem**: range over every envelope-realizable P/Q schedule with selected
area at least `26323`, screen its complete graph (2.1), and impose common-Q
only after a perfect matching appears.  The carrier mechanism remains live,
but neither of its two natural highest-area schedules compiles.

## 7. Reproducible artifacts

Static maximizing-schedule Hall:

```text
scratch/audit_r_k16_uppercomplete_capacity27597_hall_20260731.py
scratch/r_k16_uppercomplete_capacity27597_hall_20260731.audit.json
```

Independent singleton-capped P/Q DP:

```text
scratch/audit_r_k16_uppercomplete_singleton_capped_dp_20260731.py
  SHA-256 1419cc3e909331811d3c8d20a09b2ded6b8370c8f53f757d7db8cbe370532938
scratch/r_k16_uppercomplete_singleton_capped_dp_20260731.audit.json
  SHA-256 6c53c68afb38522f549d7f05d28979f6a61e397349e81288b8724b9e62ca5274
  payload SHA-256 fbeb768e3ad00c7be7a19b8f2dd48d268254df01b591bf4edddb0911d8e0f8d5
```

Primary independently patched singleton DP:

```text
scratch/audit_r_k16_facet_uppercomplete_singleton_capacity_dp_20260731.py
  SHA-256 7cca0e185f4830b51468f99ebf4a0afedd36d0fdb461d04c269e950c8589a14b
scratch/k16_facet_uppercomplete_singleton_capacity_dp_20260731.audit.json
  SHA-256 91f112e0505d5f4339e0029c028be78feacbbae112119d9f34c0d5d1984e552e
  payload SHA-256 39ec4de6f815317d5e96140eb5dd7e2e167e850992b5179ae52e339981ae9aa1
```

Singleton-compatible schedule Hall:

```text
scratch/audit_r_k16_uppercomplete_singleton_schedule_hall_20260731.py
  SHA-256 87072865611e1921c0c466d895d1765e15e9ecda4e831c3bf14ee83eef96baf5
scratch/r_k16_uppercomplete_singleton_schedule_hall_20260731.audit.json
  SHA-256 381349abdc048e803ff6d3dd1e49dbae048aea016639b3181a3eaea8f3a4afeb
  payload SHA-256 e56e594ef374a42a162f1067ad6d9fb51f68e5d399af0dc9fde20441f65212c9
```
