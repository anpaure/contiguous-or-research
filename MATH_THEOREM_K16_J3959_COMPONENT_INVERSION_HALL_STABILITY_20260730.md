# K16 j3959 component inversions, Hall stability, and the c5960 near-identity obstruction

Date: 2026-07-30  
Status: **PASS, solver-free and source-relative**

## 1. Frozen scope

Fix the authenticated `rank1_j3959` length-12,873 source and collar 5960.
Deleting the collar's 19 occurrence-labelled rows leaves nine maximal source
atoms

```text
I0=[0,3751)       I1=[3754,3900)   I2=[3905,3959)
I3=[3960,4620)    I4=[4622,7553)   I5=[7554,10344)
I6=[10345,10391)  I7=[10396,12367) I8=[12368,12873).
```

`I4` contains the first flat and `I8` contains the final two flats.  The
fixed search normal form places the forward collar after the one-flat atom
and before the two-flat atom.  Components may otherwise be reconnected and
oriented as stated below; component values and boundaries remain frozen.

The authenticated c5960 leaf decodes uniquely as

```text
I4F,I1F,C,I6R,I5R,I7R,I0F,I2F,I3F,I8R,
```

whose atom permutation has 15 inversions.  Its complete lower matching is
25,905/26,332, hence deficiency 427.  The exact alternating decomposition is

```text
298 isolated zero-degree components
+ one 3789-left / 3666-right component of deficiency 123
+ six further nontrivial deficiency-one components
= total deficiency 427.
```

Thus `298+123` is not the complete decomposition.

## 2. Scalar source-order and orientation gate

Let the three flat starts of any length-`n` chronology be
`f1<f2<f3`.  The forced depth at row `i` is three minus the number of flat
starts strictly before `i`.  Therefore the number of proper-prefix physical
cells is exactly

\[
\begin{aligned}
K
 &=3n-\sum_{j=1}^{3}(n-1-f_j)\\
 &=f_1+f_2+f_3+3.
\end{aligned}
\]

A matching of deficiency at most 25 needs at least
`26332-25=26307` physical cells.  Consequently every such chronology obeys

\[
f_1+f_2+f_3\ge 26304. \tag{1}
\]

For this component system, let `s4,s8` be the resulting starts of `I4,I8`.
The oriented internal flat offsets are

```text
a4(F)=1811, a4(R)=1118,
b8(F)=501+503=1004, b8(R)=0+2=2.
```

Hence (1) becomes the exact order/orientation gate

\[
s_4+2s_8+a_4(o_4)+b_8(o_8)\ge26304. \tag{2}
\]

The source flat starts `6433,12869,12871` give capacity 32,176.  In c5960
they move to `1811,12368,12370`, giving capacity 26,552: moving `I4` to the
front costs 4,622 cells and reversing `I8` costs another 1,002.  The resulting
flat sum 26,549 satisfies (1), so scalar capacity alone cannot reject c5960.

## 3. Exact provider transport

Provider preservation is stricter than literal row preservation.  The exact
profile of a physical cell depends on a two-stage closure:

1. every target row incoming to an envelope position of the cell;
2. every target row incoming to every envelope position of those carrier
   rows.

This `profile_dependency_rows` closure can extend six rows to the left and
three rows to the right.  A three-row left halo is therefore unsound.

Under the occurrence map from the source to c5960:

```text
retained source rows                         12854
rows whose forced depth changes              5114
sum of absolute depth changes                 5617

source proper-prefix cells                   32176
source gap/cross cells                           65
source internal cells                        32111
internal cells deleted or phase-illegal       5607
directed-legal inherited cells               26504
inherited cells preserving exact provider set 7660
legal inherited cells whose provider set changes 18844
```

All 7,660 exactly preserved provider sets lie in forward `I4`; no internal
cell of any other c5960 atom preserves its complete source provider set under
the occurrence map.

## 4. Two necessary Hall cuts

### 4.1 The terminal `Z288` cut

Among c5960's 298 zero-degree targets is a fixed set `Z288` of 288 targets
whose complete source neighborhood consists of 305 distinct cells internal
to `I8`: 304 length-two cells and one length-one cell.

For any chronology of global deficiency at most 25,

\[
|N(Z288)|\ge 288-25=263. \tag{3}
\]

In the fixed depth-two collar normal form, `I8R` places its two flats at
offsets zero and two and has only four proper-prefix cells in the entire
505-row atom.  Thus an `I8R@2` chronology satisfying (3) needs at least

\[
263-4=259 \tag{4}
\]

distinct `Z288` hosts outside `I8`.  c5960 supplies none.

The independently frozen `Z298` state theorem strengthens this conditional
gate.  Its exact dependency-closed catalogue finds no deep `Z298` provider
in `I0,...,I7` or the phase-two collar, and no deep provider in `I8R@2`.
Charging every non-deep exception to seams gives at most 253 cells.  With
`C_ext` additional right vertices from a wider move,

\[
\delta_{\rm Hall}\ge45-C_{\rm ext}.
\]

Therefore a class promising `delta_Hall <= 25+C_ext` forces `I8F` whenever
`C_ext<=9`.  This does **not** force forward orientation at entry phase three:
`I8R@3` is an authenticated escape state.

### 4.2 The giant-component cut

Let `X` be the fixed 3,789-target left side of c5960's giant alternating
component.  Every chronology of global deficiency at most 25 must satisfy

\[
|N(X)|\ge3789-25=3764. \tag{5}
\]

The source has 3,885 neighbors of `X`, so a reconnection may suffer net loss
at most 121.  c5960 occurrence transport loses 2,719 such source neighbors
and gains 2,500, a net loss of 219.  Its 3,666 neighbors therefore miss (5)
by exactly 98.

Equations (3)--(5) are target-specific necessary gates; they are much cheaper
than rebuilding the complete 26,332-target matching and remain sound under
source losses.

## 5. Dependency-closed near-identity family

Define the forward, phase-preserving family by

```text
permutation of I0,I1,I2,I3;
I4F;
permutation of C,I5,I6,I7;
I8F.
```

For every source cell, retain it only when both its physical positions and
its complete `profile_dependency_rows` closure lie in one atom.  Forward
orientation and unchanged entry phase then preserve its envelope, mandatory
mask, and complete provider set in every member of the family.

The exact common graph contains 31,955 cells and has matching 26,230.  Hence
every exact member has

\[
\delta_{\rm Hall}\le26332-26230=102. \tag{6}
\]

Relative to the source matching 26,329, at most 99 matching units are lost.
This is an `O(1)` seam-dependency loss bound, independent of the long atom
interiors.  The same common core already gives `X` 3,851 neighbors, exceeding
the giant gate (5) by 87.

The earlier 31,979-cell/matching-26,235 bound obtained from a three-left,
three-right halo is retired as unsound; (6) is the dependency-closed bound.

## 6. Exact closure through Hamming distance one

The maximal-envelope recurrence was replayed directly, with no SAT/CP solver.
The following complete faces contain no exact middle chronology:

| face | tested | exact survivors |
|---|---:|---:|
| all-forward phase-preserving face | 576 | 0 |
| exactly one atom reversal, including `I4` or `I8` | 5,184 | 0 |
| exactly one zero-flat atom phase crossing | 6,048 | 0 |

The phase-crossing census includes left-to-middle, middle-to-left, and moves
from either class to the post-`I8` phase-zero class.  Thus, in this explicit
metric, the smallest undecided c5960 topology requires at least two atom
reversals/phase crossings.  This is the precise open subcase; no claim is made
that every distance-two topology survives.

## 7. Authentication

Primary inversion/stability replay:

```text
scratch/audit_k16_c5960_inversion_stability_20260730.py
  SHA256 69864fb4c1cc287ba3ef4098ac7b8b8e722eee8d0a69df437679f18dbad5c9e3

scratch/root_k16_collar_c5960_20260730/inversion_stability.audit.json
  SHA256 24d9a7ee2419e342e95eae09af1da0f1e1c4c8e613a17b7220775be45135cd14
  payload b9b54e6073cd5d6f62dca2986472bb463a2aa8985478d6dc942c4f1cab703bca
```

Independent full-provider decomposition:

```text
scratch/audit_k16_c5960_provider_components_20260730.py
  SHA256 95188fab992c224b4c40147fdf5c2b47121f1fe2ea975b5d578912c2c4d26fe5

scratch/root_k16_collar_c5960_20260730/provider_components.audit.json
  SHA256 acde1fbcf20090dbecb0f633e920611133056fe4128c83b92f3b58cfa4bf82d0
  payload 08891162c18db1beca2d3a02be8143ce94a6cb91d0fd327a9747feeeda58c760
```

Coordinated dependency-closed `Z298` theorem:

```text
MATH_THEOREM_K16_J3959_Z298_TAIL_STATE_20260730.md
  SHA256 8881c2edcb423a6a949a6a446e8f89f88cf0eeb70cc5f3d5d429b26a6214687d

scratch/audit_k16_j3959_z298_internal_state_20260730.py
  SHA256 fd5ff0f15cc8112e35d22cf627754170e7512987f86dd135b5511d9e3d15da4f

scratch/k16_j3959_z298_internal_state_20260730.audit.json
  SHA256 141feff6372a420334a7b5311a56c60217075f13dbdd29c0e0a2f4974acf9935
  payload 3f37abcb2bcc1cc20fe8a58c29feca49ba15c9d5e198a15bad20f603ac8ab28d
```

Frozen primary inputs and exact geometry dependencies:

```text
rank1_j3959.targets                    edc3a3770f90140259f5e1d82c055bac634f49973aeaaff8cb06e42b18c581ee
candidate.targets                      c94fced40186400703799f62edd561b0eb2e16018efad0f63df300b6834c0cf3
local_collars.tsv                      d57e379c10b4932307296e056b68107b49dffe9953c3ecc913444b466cb8d5be
generalized compiler                   69aaa746b9b947b61b4da6af811d21d929c22e776e0926736fc7bc730fc6382d
COMP3 postprocessor                    27299d722bc78b4bf14f62ceb50d210e9e762f6b71f2270bd8b4c5ff1ba55bb0
```

## 8. Scope warning

This theorem concerns only the authenticated `rank1_j3959` source, collar
5960, its nine maximal occurrence-labelled complement atoms, and the stated
signed reconnection normal forms.  It does not cover split atoms, changed
values, other collars or parents, or unrestricted K16 equality.  In
particular, neither the c5960 no-go nor the distance-one closure is a global
K16 lower bound.
