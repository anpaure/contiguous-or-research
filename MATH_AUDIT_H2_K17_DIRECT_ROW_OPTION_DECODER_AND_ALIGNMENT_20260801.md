# K17 direct rooted-row option decoder and alignment audit

Date: 2026-08-01  
Lane: H2 independent audit  
Status: exact decoder/interface theorem; no optimizer verdict

## 1. Object and exact static rows

Let `R` be the 1,430 cyclic representatives of the rank-eight subsets of
`Z_17`.  A direct row solution assigns to every `r in R` a type and an ordered
partition

```text
r = C0(r) disjoint-union C1(r) disjoint-union C2(r).
```

The fail-closed decoder

```text
scratch/audit_h2_k17_rooted_flag_direct_row_solution_20260801.py
SHA256 979e8d4a64a8da901ff10861e63074c6e31c098f13ca7047608972b485164749
```

accepts either a complete certificate or an option-id selection together with
the materialized option table.  It independently checks the root partition,
the nine exact type masses, and multiplicity one for every necklace in each
suffix ledger of ranks two through eight.  In option mode it also checks the
literal option/root binding; a solver's option id is never trusted without
replaying its masks.

## 2. Gauge convention and the owner-pair theorem

For a mask `x`, the decoder defines

```text
canonical(x) = (rep,s)  iff  rot_left(rep,s)=x,
```

with `rep` the numerically least rotation.  This sign convention is replayed
at every use.

Fix a rank-nine owner representative `O`.  Its nine rank-eight incidences are
written in the `O` gauge.  For two distinct incident roots let the old root
omit `x`, with aligned classes `A0,A1,A2`, and let the next root omit `y`, with
aligned classes `B0,B1,B2`.

**Owner-pair theorem.**  There is a literal incoming age-compatible turn
through this ordered pair if and only if

```text
y in A2,       B2 subset A1,       B1 subset A0.                 (2.1)
```

The apparently missing fourth condition `x in B0` follows from (2.1): `x` is
outside the old root, hence outside `A0 union A1`; the two inclusions exclude
it from `B1 union B2`, while `x != y` puts it in the next root.  The full
equality

```text
B0 = {x} union (A0-B1) union (A1-B2) union (A2-{y})               (2.2)
```

then follows because both sides partition `O`.  Thus the compact three-test
condition used by the column materializer is exact, not a relaxation.

The decoder verifies this theorem twice for every selected table: it computes
(2.1) in the owner gauge, separately enumerates all physical turns in the
source-root gauge, and requires the resulting 1,430-bit owner-live vectors to
agree.  It also requires that this vector equal the owners containing a state
of nonzero literal indegree.

## 3. Literal turn recurrence

For source packet `p` in its canonical root gauge, choose an entering absent
coordinate `beta`, then a leaving coordinate `x` of
`O=p union {beta}`.  If

```text
target_physical = O-{x} = rot_left(q,delta),
```

then the target attachment in the canonical `q` gauge is

```text
b = x-delta (mod 17).                                             (3.1)
```

Put `Dj=rot_left(Cj(q),delta)` and `D3={x}`.  The literal turn is legal exactly
when

```text
D1 subset C0(p),  D2 subset C1(p),  D3 subset C2(p),
D0 = {beta} union (C0(p)-D1) union (C1(p)-D2) union (C2(p)-D3).    (3.2)
```

Each legal packet turn induces exactly eight state arcs: the old attachment
may be any absent coordinate other than `beta`.  The decoder asserts this
factor of eight.  This catches the common errors of rotating by `-delta`,
using `x+delta` in (3.1), or forgetting that the entering incidence and the
selected old attachment must be distinct.

## 4. Four logically different gates

The following must not be conflated.

1. **Owner support:** every owner has some ordered pair satisfying (2.1).
   Different owners may demand mutually inconsistent root incidences.
2. **Packet-support matching:** the projected directed packet graph has a
   perfect bipartite matching.  This projection forgets the selected owner
   attachment.
3. **Root-owner state transversal:** choose exactly one of the nine states of
   each root and exactly one state at each owner.  Even restricting to states
   with some global incoming and outgoing arc gives only a necessary
   bipartite matching test; the witnessing neighbours need not themselves be
   selected.
4. **Fixed-transversal transition matching:** after a literal root-owner
   transversal is supplied, restrict the state arcs to the selected states.
   A perfect bipartite matching in this induced graph is equivalent to a
   directed cycle cover on those states.  A supplied cover is accepted only
   through literal fields `(source root, source attachment, entering, target
   root, target attachment, delta)` and is replayed from (3.2).

Connectivity and primitive voltage are still later tests.  The decoder reports
cycle voltages only for a supplied literal cover.

## 5. Frozen regression fixtures

The authenticated baseline (`ad9e15...`) independently replays as

```text
raw turns / state arcs                  912 / 7,296
packet support matching                530
owner zero-out / zero-in               12 / 782
root-owner in-live matching            528
root-owner out-live matching           669
root-owner both-live matching          259.
```

Audit JSON:

```text
scratch/h2_k17_rooted_flag_direct_row_baseline_20260801.audit.json
SHA256 286849119e78fcd6ccd4f781615f8ce76f9eb4c6359f075b6aabf4e13993dcfa
payload 2f85389a6bde9cf28db64527ae948b8f98a7085293f100bc76c02db8bc9a4079
```

The alternate certificate `28401` (`e973061f...`) independently replays as

```text
raw turns / state arcs                  961 / 7,688
packet support matching                557
owner zero-out / zero-in                7 / 703
root-owner in-live matching            555
root-owner out-live matching           691
root-owner both-live matching          295.
```

Audit JSON:

```text
scratch/h2_k17_rooted_flag_direct_row_28401_20260801.audit.json
SHA256 8a29d10d3a3ec5e9488ae62f4a915f386e995b4800ab9a800a08d619ada240cd
payload 0f95dfc59331a89f5ce453ae95cab19d33d3e11dbcd51a5e051e186b1083ee64
```

The first five alternate metrics agree with the independently frozen portfolio
audit.  The three root-owner live-state matching values are new necessary-gate
diagnostics; none is a global optimum statement over other row tables.

The independently supplied `shuffle201` certificate (`d44b6061...`) also has
the exact type and rank-two-through-eight suffix ledgers.  Its literal geometry
is

```text
raw turns / state arcs                  970 / 7,760
packet support matching                556
packet zero-out / zero-in              723 / 826
owner zero-out / zero-in                 3 / 708
root-owner in-live matching            571
root-owner out-live matching           707
root-owner both-live matching          287.
```

Audit JSON:

```text
scratch/h2_k17_rooted_flag_direct_row_shuffle201_20260801.audit.json
SHA256 a503c6e4092493f9cad37d1485e3572a594cd65e9691f8cf25985370bac9a714
payload e33cc85de1b5958e17f9f5714850fc5f33b7eddc6ee4024212d945aafac1662a
```

This is a genuinely complementary basin, not a dominance improvement over
`28401`: it has nine more raw turns, sixteen fewer zero-out packets, four fewer
zero-out owners, and larger separate in-live/out-live root-owner matchings,
but packet matching is smaller by one, owner zero-in is larger by five, and
the both-live root-owner matching is smaller by eight.

The reverse support-two candidate is a literal certificate in the same exact
eight-column schema, with 1,430 data rows and SHA
`e28a8ee5825564baf0d75720d8f3c1a53a911e9c53956aff49ed2460fd08c8dd`.
It passes every static ledger and gives

```text
raw turns / state arcs                1,855 / 14,840
packet support matching                954
packet zero-out / zero-in              234 / 445
owner zero-out / zero-in                 0 / 351
root-owner in-live matching            890
root-owner out-live matching         1,196
root-owner both-live matching          718.
```

Audit JSON:

```text
scratch/h2_k17_rooted_flag_direct_row_shuffle201_reverse_20260801.audit.json
SHA256 c87add18cfe9da003fa63e222946bf71366e81fdcd7ccf35d34cb3539c0399fe
payload 3d707f964e2ca4aadf6e02b5db6e4b32bd8fc3e91180bc9546196fa95ef522a5
```

It strictly improves the three earlier fixtures in every displayed
transition/live diagnostic, but it still fails complete incoming-owner support
and therefore is only a strong optimizer basin.

Two subsequent common-first factors are independently replayed with explicit
alternating-reachability Hall witnesses.  Round two (`4e7a5fa3...`) has packet
matching 1,156 and common/both-live matching 1,099; its canonical witnesses
have `(tail,head,deficiency)=(566,292,274)` and `(365,34,331)`.  Round three
(`4213de9d...`) improves these to packet matching 1,166 and common matching
1,132, with witnesses `(579,315,264)` and `(319,21,298)`.  The decoder asserts
that each displayed head is exactly the neighbourhood of its displayed tail.
Round three covers 678 of the 782 baseline-dead owners and leaves 104.

```text
scratch/h2_k17_rooted_flag_direct_row_commonfirst_round2_560d_20260801.audit.json
SHA256 ef238db53e22258b2d935ebe2d1ec69ec082fc80549045e69634950eb2fc3c1d

scratch/h2_k17_rooted_flag_direct_row_commonfirst_round3_4e7_20260801.audit.json
SHA256 c30c473c53ec613beb14e493c787df901bc454a85b66877b4ff5129292631314
```

## 6. Exact scope

This audit supplies the independent decoder required for any future direct-row
SAT/PB candidate.  It does not solve the direct option model.  In particular,
zero owner-support defect is not promoted to a rooted factor, and no K17
construction, upper-shadow, physical opening, source, or compiler claim is
made.
