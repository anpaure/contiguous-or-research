# Upper-complete K16 two-reversal carrier: exact static compiler no-go

**Date:** 2026-07-31  
**Status:** two independent exact audits; fixed maximizing schedule is dead

## 1. Result

The frozen target order is

```text
scratch/k16_facet_augmented_uppercomplete_capacity27597_targets_20260731.word
SHA-256 63aababe9d5cbaeec4ce68a1ec32edc02d249caf3750bb20f6bc87c1ca1eac43
```

It is obtained from the P9/P9 area candidate by reversing, in order,

```text
[5567..11365], then [11..11268].
```

Literal replay gives:

```text
rank-eight targets distinct       12870 / 12870
rank-nine colours distinct        11440 / 11440
missing upper masks, ranks 9..16       0
```

The complete three-hole DP has an envelope-realizable maximizing schedule

```text
start holes       {5722,10950,10951}
deadline holes    {10,12,13}
selected area     27588
omitted-start credit  9
capacity upper bound 27597 > 26332.
```

The scalar capacity gate therefore passes.  Nevertheless, the exact static
compiler graph at this schedule has

```text
proper-prefix cells        27597
exact candidate incidences 293968
zero-candidate targets      1478
maximum matching           24328 / 26332
Hall deficiency             2004
DM shore                 4029 / 2025.
```

Most decisively, the required top singleton

```text
0x8000
```

is one of the zero-candidate targets.  Hence no common-Q assignment and no
literal compiler can realize this fixed schedule.

This retires the maximizing P/Q schedule, not the target order under every
other three-hole schedule and not the wider facet/reversal family.

## 2. Exact individual-provider theorem

Let (I_i=[s_i,e_i]) be the fixed middle intervals, (T_i) their targets,
and

\[
 E_p=\bigcap_{i:p\in I_i}T_i                         \tag{2.1}
\]

their maximal envelopes.  For a proper-prefix cell (J), define its allowed
mask

\[
 A_J=\bigcup_{p\in J}E_p.                            \tag{2.2}
\]

For every scheduled row-bit pair ((i,x)) with (x\in T_i), its host set is

\[
 H(i,x)=\{p\in I_i:x\in E_p\}.                       \tag{2.3}
\]

Define the mandatory mask of (J) by

\[
 M_J=\{x:\text{some }(i,x)\text{ has }H(i,x)\subseteq J\}. \tag{2.4}
\]

### Theorem 2.1

A lower target (S) can be assigned individually to cell (J), while all
other physical positions remain at their maximal envelopes, if and only if

\[
 M_J\subseteq S\subseteq A_J                         \tag{2.5}
\]

and

\[
 E_p\cap S\ne\varnothing\quad(p\in J).               \tag{2.6}
\]

### Proof

Capping positions in (J) to (E_p\cap S) makes their union exactly (S)
if and only if (2.5)'s upper inclusion holds and every bit of (S) has a
host; the latter is exactly (S\subseteq A_J).  Condition (2.6) is precisely
nonzeroness of every capped physical letter.  A scheduled bit is erased if
and only if all its hosts lie in (J) and that bit is absent from (S),
which is excluded exactly by (M_J\subseteq S).  These conditions are thus
necessary and sufficient.  \(\square\)

The audit enumerates every nonempty subset of each (A_J) and applies
(2.5)--(2.6) literally.  The `1,478` zero-degree targets are therefore a
sound no-host certificate, not a heuristic candidate screen.

## 3. Complete cell family and conservative treatment of hole starts

At every selected middle start (s_i), the possible lower prefix cells have
lengths

\[
 1,\ldots,e_i-s_i.
\]

Their number is the selected area `27,588`.  Each of the three omitted starts
is granted all three possible lower-prefix lengths, adding nine cells.  This
is an outer relaxation: any actual equality word can use no more.  Therefore
a no-host or Hall obstruction in the resulting `27,597`-cell graph is valid
for the fixed schedule even if an omitted start later becomes a flat, jump,
or stall.

The envelope replay itself passes exactly:

```text
zero envelope cells     0
failed middle rows      0
chain breaks            0
envelope ranks          4^3 5^5705 6^5230 7^2 8^1933
span histogram          0^1931 1^1 2^5227 3^5711.
```

Thus the obstruction is genuinely the lower compiler, not failure to realize
the middle rows.

## 4. Zero-host and Hall certificates

The zero-target rank profile is

```text
rank 1:    1
rank 6:   27
rank 7: 1450
total:  1478.
```

The unique zero singleton is `0x8000`.  The 27 zero rank-six targets are

```text
0663 098b 0a9a 0aaa 1196 12aa 16a1 1866 216a
2532 28a3 28aa 28ca 2991 29a1 2b42 3119 446a
4564 46a8 4ca8 50aa 5216 528a 528c 5324 6a12.
```

Hopcroft--Karp on the complete graph returns `24,328`; the alternating DM
shore has `4,029` targets and `2,025` neighboring cells, proving deficiency
`2,004`.  The zero singleton alone already proves no-go, while the DM shore
gives the exact maximum-matching obstruction.

## 5. Upper and common-Q scope

The target order covers every upper mask as a consecutive carrier interval.
The maximizing middle intervals have no chain breaks, so every such carrier
interval is a literal physical interval whenever the scheduled middle rows
are realized.  No extra upper pin remains.

Ordinarily a Hall PASS would still be weaker than common-Q: overlapping
chosen cells must be capped simultaneously and all middle and lower pins
replayed.  Here Hall already fails, so no common-Q solve is needed or
authorized by this artifact.

The independent C++ diagnostic also caps one deterministic maximum matching;
as expected for a deficient graph it reports many failures.  Those common-Q
counts are not used in the no-go proof.

## 6. Scope

Proved impossible:

* this exact target SHA;
* the maximizing schedule with the stated start/deadline holes; and
* every compiler assignment inside its exact maximal envelopes, even after
  granting all nine possible cells at the omitted starts.

Not excluded:

* another envelope-realizable three-hole schedule for the same target order;
* another pair of reversals or another facet-augmenting trail pair; or
* a different carrier chronology.

## 7. Reproducible artifacts

Primary Python audit:

```text
scratch/audit_r_k16_uppercomplete27588_static_hall_20260731.py
scratch/r_k16_uppercomplete27588_static_hall_20260731.audit.json
scratch/r_k16_uppercomplete27588_static_hall_20260731.matching.tsv
```

Independent C++ audit:

```text
scratch/audit_r_k16_facet_uppercomplete_max_envelope_hall_20260731.cpp
```

The implementations independently agree on all decisive figures:

```text
cells 27597; incidences 293968; zero targets 1478;
matching 24328; deficiency 2004; DM shore 4029/2025.
```
