# Endpoint-transport `fixed_5`: exact DM decomposition and protected upper-pin gate

Date: 2026-07-31

This note concerns only

```text
scratch/k16_fourfilter_def4_endpoint_transport_fixed_5_targets_20260731.word
SHA-256 9142910f9009deb4a012d2ad3828ea39753c9f8438592f18cd036e65891f939b.
```

It is a complete permutation of the rank-eight layer, is q1-complete, and has
exactly two arbitrary-upper debts:

\[
                 U_0=\mathtt{3ceb}\quad(|U_0|=10),
        \qquad    U_1=\mathtt{a9fe}\quad(|U_1|=11).
\]

## 1. The displayed schedule

The maximum-area schedule under audit is

\[
 X=\{12870,12871,12872\},\qquad
 Y=\{0,1,8589\}.
\]

It has selected area 30,023, exact physical lower-cell count 30,029, and
therefore scalar right excess

\[
                   30029-26332=3697.
\]

Every middle row replays exactly and every maximal envelope is nonempty.

## 2. Exact Hall and DM decomposition

The complete individual-pin incidence graph has

\[
 |L|=26332,qquad |R|=30029,qquad |E|=358122.
\]

Hopcroft--Karp gives

\[
                         \nu=26327,
             \qquad |L|-\nu=5.
\]

The zero-host targets are exactly

\[
 \mathtt{29cc},\qquad \mathtt{38c6},\qquad
 \mathtt{8000},\qquad \mathtt{898d}.
\]

The forward alternating shore is `30/25`; its ordinary bipartite connected
components are

\[
             26/25,quad 1/0,quad 1/0,quad 1/0,quad 1/0.
\]

The four isolated components are the four zero hosts.  The `26/25` packet is

```text
0169 016b 017b 01e9 01eb 0369 03e9 0569 056b 0769
0969 096b 0979 09e9 0b69 0d69 11e9 1969
8169 816b 8179 81e9 8369 8569 8969 9169
```

and has common intersection

\[
                   \bigcap_{S\in C}S=\mathtt{0169}.
\]

Every one of its 26 targets is exposable: after deleting any chosen target,
the remaining 25 targets match to the same 25 old packet cells.  This was
checked by 26 independent restricted bipartite matchings.

The backward alternating shore is `13458/17160`, of surplus 3702.  The
balanced part is `12844/12844`.  Hence

\[
                   3702-5=3697,
\]

exactly the global scalar right excess.  As in the earlier return candidate,
raw cell surplus and useful Hall supply live in different DM regions; here the
deficit has fortunately collapsed to five elementary components.

## 3. Component-port theorem

Let the five forward components be \((L_i,R_i)\), with
\(|L_i|=|R_i|+1\).  Their old right shores are pairwise disjoint.

### Theorem 3.1 (necessary component Hall inequalities)

For any repaired incidence graph on the same lower-target universe and every
set \(I\) of old deficient components,

\[
 \left|N'(\mathop{\bigcup}_{i\in I}L_i)
       \setminus \mathop{\bigcup}_{i\in I}R_i\right|
       \ge |I|
\]

is necessary for a perfect lower matching.

In particular, all five components together need at least five distinct cells
outside the old 25-cell forward shore.  Each isolated zero target needs a new
incidence.

#### Proof

The old union has

\[
 \left|\mathop{\bigcup}_{i\in I}R_i\right|
 =\sum_{i\in I}(|L_i|-1)
 =\left|\mathop{\bigcup}_{i\in I}L_i\right|-|I|.
\]

Even if every old right cell remains a neighbour, Hall's inequality for the
left union requires at least \(|I|\) further distinct neighbours.  Deleting
old incidences can only strengthen this requirement.  \(\square\)

### Theorem 3.2 (exact protected direct-exit normal form)

The following conditions suffice to repair the lower matching.

1. Retain a 25-edge matching from the `26/25` packet minus any chosen packet
   target to the old 25 packet cells.
2. Choose five distinct currently unmatched physical cells.
3. Add one incidence from the exposed packet target and one from each of the
   four zero targets to those five cells.

Then the repaired graph has a perfect matching on all 26,332 lower targets.

#### Proof

The old global matching remains unchanged outside the forward components.
The retained packet matching saturates its 25 non-exit targets.  The five new
edges match the five exits to previously unmatched, pairwise distinct cells.
No two operations share a left or right vertex.  \(\square\)

There are 3702 currently unmatched cells, but their mere number is irrelevant:
a geometric rethread must create the five required incidences while protecting
the internal packet matching.

## 4. Interaction with the two upper debts

Suppose a physical interval \(J\) realizes an upper target \(U\).  Every
letter in \(J\) is a subset of \(U\).  Consequently, every lower compiler cell
whose full interval is contained in \(J\) can host only lower targets contained
in \(U\).  A lower target containing a bit outside \(U\) must use a cell which
crosses a boundary of \(J\), or a cell changed elsewhere.

For the `26/25` packet:

\[
 \mathtt{0169}\setminus\mathtt{3ceb}=\mathtt{0100},
 \qquad
 \mathtt{0169}\setminus\mathtt{a9fe}=\mathtt{0001}.
\]

Thus no packet target is interior-eligible for either upper provider.

For the four isolated components:

| target | outside `3ceb` | outside `a9fe` |
|---:|---:|---:|
| `29cc` | `0104` | `0000` |
| `38c6` | `0004` | `1000` |
| `8000` | `8000` | `0000` |
| `898d` | `8104` | `0001` |

It follows that:

- a local `3ceb` provider cannot supply an interior port for any of the five
  deficient components; all five exits must be boundary-straddling or supplied
  elsewhere;
- a local `a9fe` provider may supply interior ports only for `29cc` and `8000`;
  the packet, `38c6`, and `898d` still require at least three boundary or
  external ports.

Choosing an exit target with minimum outside demand in each component gives
the exact boundary signature

```text
             packet   29cc   38c6   8000   898d
3ceb:          0100    0104   0004   8000   8104
a9fe:          0001    0000   1000   0000   0001
```

Here `0000` means that an interior provider cell is not excluded by
containment; it is not by itself an incidence certificate.

At depth three, an internal interval has at most

\[
  2\sum_{\ell=2}^{3}(\ell-1)=6
\]

distinct length-at-most-three intervals crossing its two boundaries.  This is
only an upper bound: the literal proper-prefix schedule may expose fewer.
Hence a purely local `3ceb` repair has the near-saturated port signature
`5 of at most 6`, before protecting q1, middle replay, or the old 25 packet
cells.

Moreover, any upper interval which wholly contains one of those 25 protected
cell intervals destroys that cell's packet incidence, because every packet
target contains the omitted common-core bit.  Such a loss must be replaced
before the five exits can yield a perfect matching.

## 5. Exact upper-pin audit

For the displayed maximum-area schedule, the exact capped-envelope criterion
gives no legal physical pin for either `3ceb` or `a9fe`.

The stronger independently frozen audit ranges over every monotone depth-three
schedule with three omitted starts and deadlines for this fixed target order.
Its optima are:

| upper pin | longest facet run | best physical pin | best area | optimistic capacity |
|---:|---:|---:|---:|---:|
| `3ceb` | 2 | `[12872,12872]` | 25740 | 25749 |
| `a9fe` | 4 | `[6096,6101]` | 25743 | 25752 |

Both capacities are below 26,332.  Therefore the fixed target order cannot be
completed by merely choosing another P/Q schedule and capping a provider.  A
viable continuation must rethread the target order, create both upper
occurrences, and satisfy the five-component port criterion in the new
incidence graph.

This is a target-order/architecture statement, not a global K16 no-go.

## 6. Frozen artifacts

```text
scratch/audit_k16_endpoint_transport_fixed5_dm_protected_pins_20260731.py
SHA-256 29ea14fcbb5cfce5e4231030633470a73dd9b8ca7d6c6caacc61281f742bcb70

scratch/k16_endpoint_transport_fixed5_dm_protected_pins_20260731.audit.json
SHA-256 e4be9c659627a934fa2d7911206140ac59205866ed427a25c8a038c9db672a38
payload SHA-256 5f8186fbe22d0f7485756a764b2cdf0c68269960fa080606588edf276def39fd

scratch/k16_endpoint_transport_upper_pin_capacity_20260731.audit.json
SHA-256 5bd0ce5372b70219cce2aeff1bdf0f5ee8d7e4e0dde7b3ee7962f15c8322b1dc
payload SHA-256 0d0e8a50ae51818f76c7366ae613f5c89276edac895da7d8a76714ee5295c0b0
```
