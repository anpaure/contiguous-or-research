# K17 `C10` packets after the controlled-debt/residence rebase

Date: 2026-07-31  
Status: exact solver-free factor-local replay for packets `3836`, `919`, and
their two-packet endpoint; no linear chronology, directed Pascal contraction,
compiler, four-transversal, or K17 equality claim

## 0. Verdict

The two frozen common-exterior `C10` packets have materially different
interfaces once the item2183--2184 state is imposed.

* Packet `919` is a genuine factor-local Pareto packet.  It gains two missing
  rank-seven lower turns, raises augmented occurrence rank by three, reduces
  factor components from eleven to nine, loses no cyclic consecutive flag at
  any rank, removes two cyclic run-three occurrences, and reduces the short-run
  support from `7115` to `7111` owners.
* Packet `3836` gains four missing rank-seven turns and raises occurrence rank
  by four, but it is not an all-depth accepting endpoint.  It loses the lower
  rank-five target `0x08491` and the upper rank-eleven target `0x1b47d`.
  Those are two named live debts, not a scalar caveat.
* Applying both packets gives the same endpoint in either order.  The exact
  occurrence rank is `39631`, but the two named `3836` debts remain.  Packet
  `919` does **not** discharge them.

Both closed packets are algebraically the wrong input type for Pascal
contraction.  Deleting their five old edges leaves five physical paths; the
new matching closes these as two cycles, one a single-path self-closure and
one a four-path cycle.  Thus a boundary-deficient use needs at least two
omissions and four live physical ports even before an orientation and its
directed reachability relation are supplied.  The two-packet endpoint leaves
ten core paths and four contraction cycles, hence needs at least four such
omissions on this literal matching face.

This is the precise sense in which `919` is a useful controlled-debt packet
and `3836` is only useful with explicit deeper-witness reserves.

## 1. Independent replay and scope

The script

```text
scratch/threadD_audit_k17_packet_residence_deepflags_20260731.py
```

reads the frozen eleven-cycle factor and the two packet JSON files, rebuilds
every factor edge, and recomputes from scratch:

1. degree two, Johnson legality, components and component provenance;
2. every cyclic coordinate run of length one, two or three;
3. every cyclic consecutive intersection and union palette, by rank;
4. the five-path or ten-path deleted-edge physical core; and
5. the old/new matchings on its exposed endpoints.

It imports neither the packet catalogue builder nor an occurrence matcher.
For occurrence ranks it cites the already proof-carrying independent packet
audit and four-packet macro audit, which contain equal-size matchings and
Kőnig covers.

The source regression is literal:

\[
 (N_1,N_2,N_3)=(0,2025,1221),\qquad
 |\operatorname {supp}(R_2\cup R_3)|=7115,
\]

the rank-eight and rank-ten palettes are exact, and the arbitrary-upper hole
count is `1838`, split as

\[
                 1496\ (r=11),\quad329\ (r=12),\quad13\ (r=13).
\]

The replay uses cyclic factor intervals only.  It does not choose component
cuts, orientations or an order, and therefore does not infer a staircase
deadline or compiler chronology.

## 2. Exact packet ledger

Put

\[
                         \Phi_3=2N_2+N_3.
\]

This is an exact cyclic short-run statistic, not the final deadline loss.
The complete local ledger is

| state | components | lower-`r7` holes | occurrence deficiency | `(N1,N2,N3)` | short support | `Phi3` |
|---|---:|---:|---:|---:|---:|---:|
| source | 11 | 3826 | 4134 | `(0,2025,1221)` | 7115 | 5271 |
| `3836` | 9 | 3822 | 4130 | `(0,2023,1223)` | 7115 | 5269 |
| `919` | 9 | 3824 | 4131 | `(0,2025,1219)` | 7111 | 5269 |
| `3836+919` | 10 | 3820 | 4127 | `(0,2023,1221)` | 7111 | 5267 |

Two cautions are visible already.  First, topology is not additive: each
singleton packet changes `11 -> 9`, while their edge-disjoint union has ten
components.  Second, both singleton packets improve `Phi3` by two, but only
`919` reduces the number and owner support of short occurrences.  Neither is
close to residence: the endpoint still has `3244` cyclic short runs.

### 2.1 Packet `3836`

The packet cuts exactly four old short-run collars and creates exactly four:

\[
  (N_2,N_3): (2025,1221)\longmapsto(2023,1223).
\]

It gains eleven cyclic flag targets in total, including its four advertised
rank-seven turns, but loses exactly

```text
lower rank 5: 0x08491
upper rank11: 0x1b47d
```

At upper rank eleven it gains `0x1b17d`, so the *number* of upper holes stays
`1838`; this equality of counts must not be mistaken for witness preservation.

### 2.2 Packet `919`

The packet cuts three old short-run collars (one run two and two run threes)
and creates one run-two collar.  Hence

\[
  (N_2,N_3): (2025,1221)\longmapsto(2025,1219),
\]

and four owners leave the short-run support.

More strongly, its cyclic flag delta is inclusion-monotone.  It gains

```text
rank 5:  0x02826
rank 6:  0x02a0e 0x02aa4
rank 7:  0x02aac 0x0a8aa
rank11:  0x0aaef 0x12baf
rank12:  0x0aeef
```

and loses nothing.  Thus arbitrary-upper holes fall from `1838` to `1835`
while lower ranks five, six and seven all improve.  This statement is about
factor-cycle interval support; it still does not select private occurrences
or a compiler word.

## 3. The two orders and their surviving debt

The physical packet supports are edge-disjoint, so both orders have the same
factor endpoint.  Exact proof-carrying occurrence ranks and rank-seven holes
are

\[
\begin{array}{c|ccc|ccc}
\text{order}&\multicolumn{3}{c|}{\rho}&\multicolumn{3}{c}{h_7}\\
919,3836&39624&39627&39631&3826&3824&3820\\
3836,919&39624&39628&39631&3826&3822&3820.
\end{array}
\]

Hence both orders are monotone in lower support and occurrence rank.  The
endpoint correlation excess is

\[
                         4127-3820=307.
\]

The full cyclic flag replay, however, gives the endpoint losses

```text
0x08491 at rank 5,  0x1b47d at rank 11.
```

They are precisely the two `3836` debts.  Packet `919` adds further witnesses
but no witness for either debt.  Therefore neither order is an all-depth
accepting packet.  Only the displayed order `3836 -> 919` has its second-step
common-core linkage signature frozen in the four-packet audit; the reverse
order has exact prefix and endpoint ranks, but no reverse-transition linkage
signature is inferred.

## 4. Physical boundary and Pascal reachability

For each singleton packet, deleting the five old edges leaves five paths.
After contracting those paths, the new five-edge matching has cycle type

\[
                             1+4.
\]

For `3836`, the self-closed path has order `335`; for `919` it has order
`2097`.  The other four paths close into the second cycle.  This directly
explains the touched topology `4 cycles -> 2 cycles`.

The closed state cannot be a scalar Pascal contraction atom.  If an arc
`T -> H` lies on an intact directed cycle, the complementary directed path
is an `H -> T` path.  Thus the item2184 contraction test fails until every
cycle is opened.  On the literal new-matching face the singleton interface
must omit at least two edges, leaving two physical paths and four live ports.
It must then export their orientations and the exact reachability relation;
the undirected endpoint pairing alone is insufficient.

Packet `919` exposes a useful boundary trade-off.  Its self-closing new seam

```text
(10911,11166): lower 0x02a9e, upper 0x02b9f (upper load one)
```

is the only new seam on the small contraction cycle.  On the four-path cycle,
the seams

```text
(10927,10942): upper load two
(11151,11182): upper load two
```

can be omitted without making an upper-`q1` hole, but neither hits the one
new short-run collar.  Omitting

```text
(10671,43438)
```

does hit that run-two collar, but its upper colour `0x0a9af` has load one.
Thus even on this tiny face, residence service and upper-`q1` boundary debt
are different coordinates.  Every omitted Johnson edge also loses its unique
rank-eight colour and therefore creates one lower-`q1` recycle obligation.

For the two-packet endpoint, deleting all ten old packet edges leaves ten
paths.  The new matching closes them into four cycles of path-node orders

\[
                     1,\quad1,\quad3,\quad5.
\]

Accordingly its literal boundary-deficient matching face needs at least four
omissions and eight live ports.  This nonadditive `4`-cycle state, rather than
the two singleton component counts, is the state which a compound recursive
macro must carry.

## 5. Exact rethread interface

Let `P` be one of these switch packets and `R` an interior rethread.  A sound
composition certificate must export and replay all of the following.

1. **Named flag debt.**  Every lost target at every rank, with a retained or
   recreated occurrence.  For `3836`, the initial debt is exactly
   `{0x08491,0x1b47d}`; for `919` it is empty.
2. **Occurrence linkage.**  Recompute the common graph after deleting all
   changed augmented bundles and certify the final Hall row by a matching,
   cover, and labelled augmenting linkage.  Linkage ranks are not additive
   across packets.
3. **Physical boundary.**  Export the open path endpoints, their orientations,
   and the transitive reachability relation.  Reject every filling arc
   `T -> H` for which `H` reaches `T`.
4. **Residence collars.**  Export the exact changed short-run collars and the
   capped initial/terminal positive-run lengths of all seventeen coordinates
   on every live path.  Recompute new cross-seam runs.  A scalar `Phi3` decrease
   is only a prefilter.
5. **Palette and compiler rows.**  Preserve/recycle the unique rank-eight
   colours of all cuts, retain the required upper colours, and then replay
   the lower envelope/common-cap compiler.  The old occurrence rail is not a
   full ordered four-transversal.

This interface is bounded by the live paths and named debts, not by the total
length of their interiors.  It is therefore compatible with the new
controlled-debt architecture.  What remains unproved is an interior rethread
which discharges the thousands of K17 residence collars while maintaining
these exact states.

## 6. Artifacts

```text
scratch/threadD_audit_k17_packet_residence_deepflags_20260731.py
scratch/threadD_k17_packets_3836_919_residence_deepflags_20260731.audit.json
scratch/threadD_k17_packets_3836_919_residence_deepflags_20260731.run.stdout
scratch/threadD_k17_packets_3836_919_residence_deepflags_20260731.run.stderr
```

The final run used `7.70` seconds wall time and `122,552,320` bytes peak RSS
on the local lightweight audit.  No SAT, exhaustive switch generation, or
H100 job was run.
