# The shielded p9958 seven-debt service plus two arbitrary returns is impossible

**Date:** 2026-07-30  
**Lane:** D, exact finite K16 interval-OR transport  
**Status:** complete scoped no-go, independently audited

## 1. Verdict

Start with the authenticated reorganized-H1 chronology of length `12,873`.
Keep the following four edits literal:

1. at `p6440`, replace `0x806d` by one of all sixteen audited gate values;
2. at `p9958`, apply the unique minimum shielded joint-service row
   `0x2a01 -> 0x806d`;
3. choose two distinct further positions outside `{6440,9958}`; and
4. at each return position, choose an arbitrary changed nonzero 16-bit value.

There is no universal word in this complete fibre.

The proof does not add source-relative one-cell columns.  It retains the
exact interaction of the two arbitrary return values through

\[
  A_r(x)+B_s(y)+C_{rs}(x\mathbin\lor y),
\]

even when a return lies inside the old gate/service shield.  The complete
raw quantifier has

\[
  16\binom{12871}{2}(65534)^2
  =5{,}691{,}335{,}370{,}473{,}712{,}960
\]

literal assignments.  A proved support theorem reduces the position pairs
to `41,856`, and an exact maximum-envelope MITM decides every remaining
arbitrary-value kernel.

This is the high-debt fallback explicitly left open in handoff item 1989-D.
It does not prove `nu(16)>12873`; the bracket remains

\[
  12873\leq \nu(16)\leq12874.
\]

## 2. Frozen base

The source is

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
```

and has sole hole `0x2c6d`.  The gate alphabet is

```text
0440 0441 0444 0445 0448 0449 044c 044d
0460 0461 0464 0465 0468 0469 046c 046d.
```

For every gate, the simultaneous service edit at `p9958` leaves exactly the
same seven unit holes

\[
 D=\{\mathtt{aa65},\mathtt{aa69},\mathtt{aac5},\mathtt{aacd},
       \mathtt{aae5},\mathtt{ab69},\mathtt{eb69}\}.
\]

Their meet is `0xaa41`.  The sixteen complete signed base profiles are
distinct, despite their common positive residual.  The full joint atlas has
202 rows, of which 199 are shielded; `p9958` is the unique shielded row with
only seven exported holes.

## 3. Complete position-support theorem

For a return position `t` and value `z`, let

\[
  P_t(z)\subseteq[7]
\]

be the exact set of debts in `D` acquired by the one-cell replacement at
`t`.  Values with empty profile remain quantified; they are not deleted from
the final MITM.

For an unordered position pair `r<s`, let `b_rs` be the OR of the unchanged
open bridge.  Define two pair families:

* `J` consists of pairs for which `b_rs` is a submask of at least one debt in
  `D`.  These are precisely the pairs at which a genuinely joint
  debt-labelled witness can occur.
* `A` consists of pairs for which some exact one-cell profiles satisfy
  `P_r(x) union P_s(y)=[7]`.

### Lemma 3.1 (necessary support)

Every two-return completion has its position pair in `J union A`.

**Proof.**  Outside `J`, the fixed bridge contains a bit outside every debt
in `D`, so no interval labelled by a debt can contain both return cells.
The debt witnesses then split into intervals through `r` alone and through
`s` alone.  Their exact truncated profiles equal the unrestricted one-cell
profiles, and all seven debts require a profile union `[7]`; hence the pair
lies in `A`.  This argument permits either return to have empty individual
profile when the other covers all debts.  Conversely, pairs in `J` are kept
without any additive-profile requirement.  Thus no joint-only or
compensation-only completion is pruned.  QED.

The independent catalogue proves the following exact census:

```text
eligible return positions                         12,871
all unordered return-position pairs           82,824,885
J, bridge-compatible pairs                         15,044
A, additive-profile pairs                          26,833
J intersect A                                          21
J union A                                           41,856
class J only / A only / both              15,023 / 26,812 / 21
```

The bridge-compatible distance histogram is

```text
1:12868  2:1699  3:361  4:97  5:18  6:1.
```

There are 39 exact nonzero one-cell profile masks.  The histogram of the
largest number of debts attainable at a position is

```text
1:10202  2:2545  3:120  4:1  5:1  6:1  7:1.
```

The four exceptional positions are `3518,3519,3520,3521`, with maxima
`4,5,7,6`.  Since `3+3<7`, every additive pair meets this four-position set;
this makes the `A` construction complete without scanning 82.8 million
pairs.  Its incidences at the four positions are `3,1096,12870,12870`.

The explicit 41,856-row catalogue has digest

```text
76c6e4839f51805ca836d51e7696474f76b5df2e707799fcb01187b4eaf845ea.
```

## 4. Exact two-return kernel

Fix one gate/service base and a retained pair `r<s`.  Partition every
interval into four disjoint classes: it avoids both return cells, meets only
`r`, meets only `s`, or meets both.  For every target `T`, exact occurrence
multiplicity after the two replacements is

\[
 m'_{T}(x,y)=m^{00}_{T}+A_{r,T}(x)+B_{s,T}(y)
                       +C_{rs,T}(x\lor y).                 \tag{4.1}
\]

Here `C` contains the complete fixed bridge OR.  Formula (4.1) is an
identity, not an additive approximation.

Let

\[
 K_{rs}=D\cup\{T:m^{00}_{T}=0\}.
\]

Every target outside `K_rs` has an interval avoiding both returns and is
automatically preserved.  Thus the full 65,535-target problem is equivalent
to covering `K_rs` in (4.1).

For each interval class and target, remove the edited letters and call the
remaining fixed OR `c`.  A literal value `v` completes that context exactly
when

\[
 c\subseteq T,\qquad v\subseteq T,\qquad T\setminus c\subseteq v.
\]

Consequently a context family is represented without loss by the
inclusion-minimal missing masks `T minus c`.  For the both-cell class the
same statement holds with `v=x union y`.  No multiplicity is needed after
the avoiding class is zero: one surviving context suffices.  All
multiplicities are nevertheless used when constructing `K_rs`.

## 5. Exact value reduction

### Lemma 5.1 (first-value quotient)

It is exhaustive to test every changed nonzero `x` which is a submask of
some target in `K_rs`, plus one legal representative outside that union.

**Proof.**  If `x` is not a submask of a critical target `T`, it can occur in
neither an `r`-only nor a both-cell `T` witness.  All such outside values
therefore have the same behaviour on every target in `K_rs`.  Values inside
the union are retained literally, then grouped only when their complete
`A`-coverage and all residual `C` missing-mask antichains agree.  QED.

### Lemma 5.2 (maximum envelope)

Fix a first value `x`, and let `E` be the critical targets not covered by an
`r`-only interval.  Put

\[
  U=\bigcap_{T\in E}T.
\]

If `E` is empty, any legal changed nonzero second value works.  Otherwise:

* if `U=0`, the kernel is impossible;
* if `U` differs from the incumbent at `s`, testing only `y=U` is complete;
* if `U` equals the incumbent, testing its nonzero coatoms is complete.

**Proof.**  Any `s`-only or both-cell witness for every `T in E` requires
`y subseteq T`, hence `y subseteq U`.  Within this common down-set, both
conditions

\[
 B_{s,T}(y)>0,qquad C_{rs,T}(x\lor y)>0
\]

are upward closed in `y`.  Therefore a feasible changed value extends to
`U`, unless `U` is the forbidden incumbent; in that case it extends to one
of the nonzero coatoms of `U`.  QED.

The implementation uses dynamic requirement vectors; there is no unsafe
64-target assumption.  The observed maximum was 38.

## 6. Complete result

The exact run reports:

```text
gate states                                      16
supported position pairs per gate            41,856
exact raw kernels                             669,696
distinct complete kernels                     41,967
exact cache hits                              627,729
first-value representatives             2,641,181,504
complete first profiles                   396,104,508
second envelopes tested                  348,359,189
zero deficit intersections                48,016,535
empty deficits                                     0
maximum critical-set size                         38
maximum first-value candidates                 12,443
universal candidates                                0
ordered kernel digest                  541e6c21f57effcd
```

The status is

```text
PASS_EXHAUSTED_NO_COMPLETION.
```

The production run used one H100 CPU, a unique `/home` directory, a 2 GiB
address-space cap, and no `/dev/shm` storage:

```text
wall time             93.72 s
maximum RSS           50,176 KiB
swap                   0
exit                   0
```

No candidate word was emitted, so there is no positive requiring literal
replay.  The engine would reject any kernel-positive unless a complete
literal occurrence recount covered all 65,535 nonempty masks.

## 7. Independent audit and provenance

The support stage and value stage are separate artifacts.

```text
scratch/audit_threadD_k16_p6440_j7_pair_support_catalogue_independent_20260730.py
SHA-256 2907a9a73aa5ca798856e20caeccf59189e4fe239244fccdfbe855d8762d441e

scratch/threadD_k16_p6440_j7_pair_support_catalogue_independent_20260730.audit.json
SHA-256 31ac36866d209da6cb3b92b9f19cfdad94644d4ae92c4708d7f750f3b0b852a5

scratch/threadD_k16_p9958_j7_pair_support_20260730.tsv
SHA-256 42e10fd3312f80a715b465d35a983379953de0f1341bc29927471bed863b8678

scratch/search_threadD_k16_p9958_j7_two_return_exact_mitm_20260730.cpp
SHA-256 85e3c3f33155904e7f6cecf7b7be58c0fd9fc6ae0b3f75465180ca7972a184b2

scratch/threadD_k16_p9958_j7_tworeturn_exact_20260730/j7.audit.json
SHA-256 b39134cb14e4fc0db69053293f2a29aabcac86f0456a61f81394a642de51d403

scratch/audit_threadD_k16_p9958_j7_two_return_exact_mitm_20260730.py
SHA-256 73f6aeacbc88d35d29f913020385b85ed89d84204b2c197184791190a419d9b0

scratch/threadD_k16_p9958_j7_tworeturn_exact_20260730/j7.independent.audit.json
SHA-256 8b973e15d46182ccec8b4c15dc55377ac0d1b46de3272d3b606e775d3cc0d3cc
```

The independent checker re-authenticates the source and 41,856-row support
catalogue, reproduces its binary digest and class histogram, and checks all
sixteen 41,856-pair exhaustion ledgers.  Its status is

```text
PASS_INDEPENDENT_EXHAUSTION_LEDGER_REPLAY.
```

The capped production directory is

```text
/home/amodo/or15/work/threadD_k16_p9958_j7_tworeturn_exact_20260730.
```

## 8. Exact scope boundary

The result is disjoint from the named active campaigns in the following
precise sense.

* It has four genuine edited sites, so it is outside the H1-local
  support-at-most-three/radius-three face.
* `p9958` is outside the frozen 13-cell support and collar594.  The mandatory
  `p6440` gate overlaps those regions, so no stronger position-disjointness
  claim is made.
* Thread A's H2/R19 face fixes `(p6440,p9958)` at
  `(0x806d,0x2a01)`; this fibre changes both to a gate value and `0x806d`,
  respectively, and starts from the reorganized-H1 basin.
* A return may lie inside `(6440,9958)` and destroy the original FULL shield.
  This is why the exact `C_rs(x OR y)` term is retained for every pair.

The theorem does not cover a return overwriting either fixed edit,
coincident or trivial returns, three or more returns, another one of the 201
joint-service rows, another portal/basin, arbitrary rethreads, or
unrestricted K16.  The next literal service alternatives are therefore a
different high-debt joint row or a third return around this seven-debt row;
neither follows from the present no-go.
