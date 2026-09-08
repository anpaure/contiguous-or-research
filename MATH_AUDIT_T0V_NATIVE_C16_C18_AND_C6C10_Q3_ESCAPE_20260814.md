# Hostile audit of the native `C16/C18` and paired `C6+C10` `q3` escape

**Date:** 2026-08-14
**Verdict:** **PASS**, with the scope restrictions stated in Sections 5
and 6 of the source note.  The `C16` thirteen-root topology/common-phase
scaffold and every finite-menu obstruction are certified.  A resident
suffix-local two-target backup and a descended thirteen-role port theorem
are not claimed.

**Audited source:**
`MATH_OBSTRUCTION_T0V_NATIVE_C16_BINARY_THIRTEEN_ROOT_SCAFFOLD_HAS_A_DOUBLE_G2_SINGLETON_LOSS_20260814.md`

## 1. Enumeration audit

The parallel long-cycle enumerator starts from every directed canonical
owner arc that can occur in a four-owner provider of `W3`.  It extends to
a simple alternating owner/colour cycle and assigns each resulting support
to the lexicographically first relevant arc in that support.  Hence worker
chunks are disjoint and their counter sum has no cross-worker duplicate.
Any single cycle that raises the zero load of `W3` must toggle at least one
arc of a prospective `W3` provider, so the target-relevant restriction is
complete for the stated single-cycle question.

The certified single-cycle counts are:

```text
             target relevant   owner disjoint   raw W3   typed q2   base q3
C16                 701756            625801      90956          8         6
C18                5192016           4581993     673253         25        15.
```

The paired enumerator uses the complete native `C6` catalogue and the
complete target-relevant `C10` catalogue, tests every owner-disjoint cross
pair, and computes the combined `q3` deck before filtering.  It therefore
does not assume that either member creates `W3` alone.  The exact scoped
counts are `1393933`, `196055`, `66256`, and `5` for owner-disjoint pairs,
`W3` creators, old-`q3`-support preservers, and all-typed-support
preservers.  This does **not** enumerate pairs in which the `C10` member
contains no target-relevant arc; the source correctly labels this as the
target-relevant `C6+C10` menu.

## 2. Circuit, typed-current, and phase audit

For every displayed survivor, the replay reconstructs the alternating
cycle support, checks that the fixed `C8`, fixed `C6`, and new circuit
owner banks are pairwise disjoint, and applies the packet by symmetric
difference.  It then checks every old occurrence-deck value in

```text
owner, lower q1, upper q1, lower q2, upper q2, upper q3
```

against the new deck.  Thus "support safe" means literal positive
multiplicity, not merely zero total current.  The phase solver builds the
union of old and new owner adjacency at every colour and tests
bipartiteness on every component.

Exactly two of the six `C16` survivors have a common binary phase.  Exactly
eight of the fifteen `C18` survivors do.  All five typed-safe `C6+C10`
pairs do.  No residence claim is inferred from bipartiteness alone.

## 3. Component-action audit

The replay constructs the lifted MSW factor and traces both projected rank
shores.  The shore histograms agree.  For either binary `C16`, the base
histogram is `13^119+169`; tracing the new length-169 component gives the
thirteen roots and relative sign vector in the source.  Since all toggled
coordinates are in the twelve-bit prefix, different Dyck suffixes give
disjoint copies.  This proves, rather than extrapolates,

```text
components = Cat_m - 12 Cat_(m-6).
```

The same suffix-copy argument turns the three possible `C6+C10` base
histograms into `Cat_m-11 Cat_(m-6)`, and the two binary `C18` histogram
types into `Cat_m-13 Cat_(m-6)`.  These are favorable contractible actions;
zero topology cost was not imposed.

## 4. Seam and casualty audit

The current convention is `new-old`.  At suffix semilength two, filtering
the exact upper-`q3` current by suffix weight four isolates the two-colour
boundary.  For binary `C16` candidate 5 it is exactly

```text
+000011110111[G] -100011010111[G]
+000010111111[G] -100010011111[G].
```

Grouping suffixes by `G2(V)` reproduces coefficient `|F_G|` on every row.
At `V=110100`, `G=110111` is a singleton fibre and both negative values
have multiplicity `1 -> 0`.  The full replays find `0,0,0,2,4`
upper-`q3` casualties at `m=6,7,8,9,10`, and no casualty in any typed deck
through `q2`.

The independent `C18` replay checks all fifteen survivors.  Every binary
candidate still loses `100011010111[110111]`; six have two casualties and
two have three.  The independent paired replay checks all five `C6+C10`
survivors; each has exactly two casualties at `m=9`, one at that same
prefix.  Therefore neither the longer single cycle nor the first positive
target-relevant paired menu removes the singleton gate.

## 5. Adjacent-window reduction audit

For candidate 5 the two negative prefixes differ by one exchange.  The
rank-correct normal form has owner rank `R` and `|H|=R+2`.  Its middle
owners omit `{h1,h2}`, `{h2,h3}`, and `{h3,h4}`.  Consecutive omissions
meet in one element, so consecutive owners are Johnson-adjacent; the
triple intersection of the omissions is empty, so the three owners union
to all of `H`.  The endpoints exchange one element for `a` and `b`, giving
the required first and last four-owner unions `H+a` and `H+b`.  The two
internal upper colours omit `h2` and `h3`, respectively, so they are
distinct; the endpoint colours contain `a` or `b`.  The displayed literal
rank-nine witness has four distinct colours and unions to the two
rank-twelve targets under direct replay.
Five owners are necessary inside this consecutive four-window model
because two distinct length-four windows offset by one have a five-position
union.  This validates the open-rail reduction only.  Alternating closure,
zero typed current through `q2`, common phase, and physical collar
residence remain the live gate.

## 6. Exact scope and remaining gate

The audit binds:

* complete target-relevant single-cycle atlases through `C18`;
* complete `C6/C8` paired menus and the target-relevant `C6+C10` menu;
* exact binary phase, component action, and typed-current data for the
  displayed `C16` packets; and
* the finite `m<=10` provider/casualty replay stated in the source.

It does not bind arbitrary longer paired/triple menus, a suffix-local rail
closure, a common-history lift, or a physical thirteen-port selection.
The sharp remaining gate is a candidate-5, `c0(V)`-keyed closure of the
five-owner adjacent-window rail that creates both singleton targets while
having zero typed current through `q2` and a phase-compatible contractible
component action.

## 7. H100 provenance

All searches, replays, and hashes were run on host `arboghast` through
`ssh h100`.  The Mac was used only to read/edit files and perform Git
operations.

Binding SHA-256 values:

```text
2c7d536c7aa85a9760e5aa8489b6720770fe1d9bf8dd0848401f3febceab254b  source note

8d839947322f47d5df82949218423a8cdf9cfc2c6f316d10d73e538a53b0460a  long-cycle parallel search
089951fc8c02305bc3dd7cbde7929d7d0fc26efbaf0c3be9ae51d0eb62f8f6a7  C16 atlas output
ec5f4d41090bb9f9f840747181e1d97980680a9205ba8a43a391a3b8cdf85169  C18 atlas output

5872156ababe2ccebcc32360f68e6f9cc8d296e4e7e5eef12d719f43cfbbf87d  paired-menu search
b95217bc42c2929a1eadd1da8f37990919645a2fec14a6643238da6fd212bedf  C6+C6 output
95d137e78ae8d2f3c29d595c6ac2034240e1c55979ec1d92c108193fa11cb34f  C6+C8 output
f333a4010200e1f01304d5bb84decbd22f14fd45b1fc7dccd9b530209ca3e731  C8+C8 output
52182c6b1ca328c021c9afc9c67d267d64b0cbca25f09d1361db513b04c6e71f  C6+C10 output

7c0b2723043976669666ae22c560d054e8cd5907d4e4a02f7bc53af171a73817  C16 atlas diagnostic
7f9f37f4de3e29530ef782516a14bd23856b086ffe868f5282d50a8285cfd9bc  C16 diagnostic output
1a09ad0aff5d05dff8099f27201e92713cf2069212d8a5a66f827e63d3f95dd4  C16 tensor replay
e0d1b0e228d55e79e6019bd556c56006757523d1da8f6d4983b8ab43fba8fc71  C16 tensor output
52056a61da64a95d34d29c040cf943ae942d8d54c01b0de21d41be4a2e213c0a  C18 hostile replay
cfc479eb706ae0e66efcdd36249396ded0ba68e68ef62d2815efdf28218e3d6e  C18 hostile output
d1c491fd583758e7a6af0bdb90603b74b63ee67d35f3c1184333c65c255464f2  C6+C10 hostile replay
10dde6f712438d6347760d7bc80ddd2bc31155f5ac15f9ff477bfdc11a5828d8  C6+C10 hostile output
```
