# Obstructions to two canonical all-parameter MSW port selectors

**Date:** 2026-08-14  
**Status:** exact finite and infinite-pattern obstructions. These results do
not obstruct the full coalesced separated-port CSP; its
\((m,d)=(10,3)\) instance is feasible.

## 0. Outcome

Two tempting consequences of the highest-valley four-packet theorem are
false.

1. Sending a child through its leftmost highest valley does **not** make
   `child -> (parent, packet type)` injective. The resulting parent can have
   more than four children, and choosing the least direct common cut creates
   parent-side port collisions.
2. The standard Proskurowski--Ruskey transposition Hamilton path does **not**
   lie in the equality-only same-forced graph once \(d\ge2\), already at the
   first threshold \(m=3d+1\). The later full common-history relaxation repairs
   some of these transitions but still does not contain the standard PR path.
3. Grouping every inverse child of a parent by the four packet types does
   **not** repair the first failure. Frequently there is no single parent
   start compatible with all children in one type; even when each type has a
   universal start, the type sets need not admit a separated transversal.

Thus an all-parameter theorem needs a genuinely global edge/port selector or
a richer recursive path, not one canonical residue gap per packet type.

## 1. Deterministic highest-valley selector

Fix the following rule at \(m\ge3d+1\): choose the leftmost highest valley,
use the packet prescribed by the four residue cases, use `001` at the
exception \((L,Q,O)=(d,d,d-1)\), and otherwise choose the least direct common
cut. At the exceptional triple choose the least crossed common-cut pair.

Every chosen edge individually has a common depth-\(d\) forced history and
strictly increases area. The hoped-for global properties nevertheless fail:

| \((m,d)\) | max multiplicity of `(parent,type)` | max children | max distinct used ports | collision rows |
|---:|---:|---:|---:|---:|
| \((4,1)\) | 1 | 3 | 4 | 4 |
| \((7,2)\) | 2 | 6 | 5 | 130 |
| \((10,3)\) | 3 | 7 | 6 | 4,763 |
| \((11,3)\) | 4 | 9 | 6 | 14,786 |
| \((13,4)\) | 4 | 9 | 7 | 203,290 |

The smallest noninjective fibre in this audit occurs at \((m,d)=(7,2)\):

```text
parent  = 11111100010000
packet  = 001
child 1 = 11111100000100   with (L,Q,O)=(4,0,1)
child 2 = 11111001010000   with (L,Q,O)=(1,0,4)
```

Both children choose the displayed parent by a highest-valley `001` move.
They are distinct, disproving injectivity into `(parent, packet type)`.

Even at \((4,1)\), where that injectivity happens to hold, least-cut ports
fail. At the mountain `11110000`, the three child incidences use parent starts
\(0,4,1\); starts \(0\) and \(1\) have cyclic distance one, below
\(d+1=2\).

## 2. No universal parent start per inverse packet type

For a parent row \(v\), orientation \(\epsilon\), and packet type \(t\), let
\(C_t(v)\) be all children obtained by an inverse highest-valley packet of
type \(t\). For \(u\in C_t(v)\), put

\[
 A_{v,t}(u)=\{b:\text{some child start }a\text{ satisfies }
 \Sigma_{u,\epsilon}(a)=\Sigma_{v,\epsilon}(b)\}.
\]

The proposed universal parent-port class is

\[
 U_{v,t}=\bigcap_{u\in C_t(v)}A_{v,t}(u).
\]

Exact H100 enumeration gives the following identical counts in each global
orientation:

| \((m,d)\) | nonempty `(parent,type)` fibres | empty \(U_{v,t}\) | max fibre | parents with types | parents failing some \(U_{v,t}\) | parents with a separated universal-type transversal |
|---:|---:|---:|---:|---:|---:|---:|
| \((7,2)\) | 852 | 399 | 3 | 411 | 271 | 107 |
| \((10,3)\) | 32,974 | 9,522 | 5 | 16,024 | 7,810 | 8,214 |
| \((13,4)\) | 1,445,041 | 244,543 | 6 | 707,831 | 203,600 | 501,664 |

At \((7,2)\), another 33 parents have all nonempty universal-type sets but
no choice of one element from each set whose distinct elements have cyclic
distance at least three. At \((13,4)\), 2,567 parents have this second
failure. There is no such second failure at \((10,3)\).

The typewise empty-intersection counts are:

| \((m,d)\) | `01` | `001` | `011` | `0011` |
|---:|---:|---:|---:|---:|
| \((7,2)\) | 248 | 69 | 69 | 13 |
| \((10,3)\) | 5,334 | 2,089 | 2,089 | 10 |
| \((13,4)\) | 166,250 | 39,130 | 39,130 | 33 |

An early explicit failure is the \((7,2)\) parent
`11111100100000`. Its two inverse `01` children are
`11111100010000` and `11111010100000`, and their admissible parent-start sets
are disjoint in either fixed global orientation.

This obstruction is deliberately stronger than failure of the least-cut
rule: it exhausts **all** parent starts and allows the child start to vary.

## 3. Standard PR path obstruction

Let \(P_m\) be the standard Proskurowski--Ruskey path defined by

\[
\begin{aligned}
\operatorname{flip}(w)&=1^{k-1}01w_{k+1:},\\
\operatorname{insert}(w)&=1^{k+1}00w_{k+1:},
\end{aligned}
\]

where \(k\) is the initial ascent length, and by the usual reversed-branch
Catalan recursion. The audit used precisely this recursion rather than an
arbitrary Gray ordering.

At \((m,d)=(4,1)\), all 13 transitions are same-forced. A dynamic program
also chooses the two incident port witnesses at every internal path row so
that they coincide or have cyclic distance at least two.

At the next threshold, the path itself fails before packing. For every
\(d\ge2\), put \(m=3d+1\) and consider the consecutive PR words

\[
 x_d=1^{3d}0^d1,0^{2d+1},
 \qquad
 y_d=1^{3d}0^{d+1}1,0^{2d}.
\]

They differ by one adjacent `10 -> 01` transposition. Direct reconstruction
of the MSW tight orders and forced signatures finds no cuts \(a,b\) and no
endpoint orientations \(\epsilon,delta\) satisfying

\[
 \Sigma_{x_d,\epsilon}(a)=\Sigma_{y_d,\delta}(b).
\]

The targeted H100 replay verifies zero oriented common-history options for
every \(2\le d\le10\). The first three instances are:

```text
d=2: 11111100100000 -> 11111100010000
d=3: 11111111100010000000 -> 11111111100001000000
d=4: 11111111111100001000000000 -> 11111111111100000100000000
```

Full path enumeration gives 109 missing same-forced transitions among 428
at \((7,2)\), and 4,314 among 16,795 at \((10,3)\). The displayed family is
the first missing transition in each standard PR path.

The zero-option family is presently a verified exact pattern through
\(d=10\), not yet a symbolic all-\(d\) proof. It already refutes the proposed
all-parameter use of the standard PR path inside the equality-only subgraph.

Under the exact full compatibility criterion

\[
 F^u_j\cup F^v_j\subseteq P^u_j\cap P^v_j,
\]

the earlier first transitions can recover, but the standard path still fails.
At \((7,2)\), 8 of 428 PR transitions have no full common-history option; the
first is

```text
11111011000000 -> 11111001000010.
```

At \((10,3)\), 2,020 of 16,795 transitions have no full option; the first is

```text
11111111100001000000 -> 11111111100000100000.
```

At \((4,1)\), all 13 transitions remain feasible, and a dynamic program can
choose distinct incident starts at every internal row with cyclic distance at
least two. Simply exchanging both recursive branches is not a valid repair:
the resulting order ceases to be a transposition path by \(m=7\).

## 4. Exact remaining gate

The finite \((10,3)\) CSP proves that the obstructions above are selector
failures, not nonexistence of a coalesced arborescence. A more faithful
formulation has one option per child consisting of

\[
 (\text{parent},\text{child orientation/start},
   \text{parent orientation/start}),
\]

with global orientation consistency and a conflict graph on distinct used
starts of each row. This is a coupled list-selection problem with
coalescence, not an ordinary matching into four packet bins. Any Hall-type
proof must retain the endpoint coupling and the cyclic conflict graph; raw
expansion into `(parent,start)` classes alone is only a relaxation.

## 5. Reproducibility

All enumeration, compilation, execution, and hashing used SSH on H100. The
audit sources are:

- `scratch/audit_msw_deterministic_highest_valley_parent_ports_20260814.cpp`;
- `scratch/audit_msw_parent_packet_universal_ports_20260814.cpp`;
- `scratch/audit_msw_pr_path_common_ports_20260814.py`; and
- `scratch/audit_msw_pr_first_transition_obstruction_20260814.py`.
- `scratch/audit_msw_pr_path_general_common_separated_20260814.py`.

These scripts reconstruct MSW tight orders from the \(g/h\) recursion and
compare literal unordered endpoint rails. No signed lattice identity is used
as a positive decomposition.

Frozen H100 SHA-256 digests:

| artifact | SHA-256 |
|---|---|
| deterministic selector source | `1f8896b5d699cc59e69a9747bf0cea4ac37b3cbb8f7ba6938a9e58ecd244f5dc` |
| universal packet-port source | `c2498cebce4ec29f38580188f0bc36fd0189855e4bce5327c6073d44c5133925` |
| PR path source | `81c5929f90271145eb25945a9fec774f9ba5fe2603d541d7ade7b492de67a76a` |
| targeted PR family source | `d133918b71aaca7a62f1c77002c610164ff39568ecaed1df69aa0103df163b86` |
| deterministic outputs \((4,1),(7,2),(10,3)\) | `adda1dc0a97c260621167874202a4b7921c7b474c3db5ef3f9800171c0047521`, `7f5f6d708efc95d5abf247b5b86b3ed23ade5dc924cbd927c410d05f6355cfb5`, `62f9dd709094f9344ed894175609c6cfb31092c34d9a8f8cb01627c1f8f9b0d6` |
| universal packet-port outputs \((7,2),(10,3),(13,4)\) | `718ca8b7bd642d70200c15f26b40b90986bcab72ebfcca7566a52cb296cbe56c`, `4a9fb80b245406940e6103629c8da29aab27d2ad8eb7ad7d4804ad6cd10fa980`, `6650c8af8ffb5444e0d7be6a08fb25b062e5014403ee6fb591407f528763a0fc` |
| PR all-orientation outputs \((4,1),(7,2),(10,3)\) | `9cdd9197b4bd239cee6be11724baffea14f129507900531dc23cb0e335a534b3`, `7ae868c6558df2566995b868ba923c3e170816e027da4d1ad4f005398c014968`, `5295ea52fd0570166c24c9e9762b2afd4adb59420923fd15b4bb0fc3469a144b` |
| targeted PR family output, \(2\le d\le10\) | `1263adf69a7ad05686763af729dc11680c137c8a22264483c0b47f45227e337a` |
