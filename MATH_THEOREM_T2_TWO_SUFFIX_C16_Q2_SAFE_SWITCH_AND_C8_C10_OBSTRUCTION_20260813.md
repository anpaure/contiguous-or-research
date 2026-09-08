# Two suffix copies admit a q2-safe `C16`, but no `C8` or `C10`

**Date:** 2026-08-13  
**Status:** unconditional explicit tensorable switch theorem, plus an exact
finite shortest-cycle certificate in the 16-coordinate base.  The switches
preserve owners, immediate-upper colours, and q2 support.  They do **not**
yet prove the desired residence concatenation or a favorable socket action.

## 0. Outcome

Apply the exact two-hex `T2` relay to both four-bit Dyck suffixes

```text
                         V0=1100,   V1=1010
```

in the semilength-eight canonical MSW factor.  For each of the six changed
prefix owners `P`, compare the corresponding owners `P V0,P V1`.

There is no local alternating incidence cycle of length `8` or `10`
containing either pair.  If every owner on the circuit is required to be
internal in the open MSW path forest, the exact **incidence-cycle lower
bounds** for the six pairs are

| prefix owner | lower bound |
|---|---:|
| `101010001101` | `22` |
| `100011001101` | `16` |
| `100010001111` | `16` |
| `101011000101` | `20` |
| `101001010101` | `16` |
| `101001001101` | `16` |

Allowing degree-one owner endpoints lowers this table to
`18,14,14,18,14,14`; it still excludes `C8,C10`.  Within the internal-owner
class the bound `16` is sharp for the last two owners.  There are two
explicit, owner-disjoint and colour-disjoint alternating `C16` switches,
one through each of those corresponding suffix pairs.  Either switch, and
both simultaneously, preserve the support of every q2 target represented
before the switch.

Appending an arbitrary Dyck word `W` tensors both `C16`s literally.  Thus,
for every semilength `r>=8` and every `W in D_(r-8)`, the two `T2` packets
with suffixes

```text
                         1100W,   1010W
```

admit the same pair of q2-safe cross-suffix switches.  Different `W` give
disjoint switch supports.

The switches escape the local hexagon obstruction by visiting owners whose
prefix rank drops by one while the four-coordinate suffix rank rises by
one.  They are therefore genuine cross-phase circuits, not constant-prefix
Gray-edge splices.

## 1. Directed exchange graph

Let `F` be an exact incidence factor between rank-`R` owners and
rank-`R+1` colours.  Its directed exchange graph `D(F)` has the owners under
consideration as vertices and an arc

\[
                  A\mathrel{\mathop\longrightarrow^{X}}B        \tag{1.1}
\]

when `A-X` is unselected and `B-X` is selected.  Every simple alternating
incidence cycle projects to a directed owner cycle

\[
       A_0\longrightarrow A_1\longrightarrow\cdots
          \longrightarrow A_(k-1)\longrightarrow A_0             \tag{1.2}
\]

by orienting each inserted incidence from its owner to the owner at which
the same colour was selected.  Conversely, a simple directed owner cycle
is an alternating incidence `C_(2k)` only when its `k` arc labels are
pairwise distinct.  Both explicit cycles below pass that extra test.

Consequently, if an alternating incidence cycle contains vertices `A,B`,
the two arcs of its directed owner projection
between them have lengths at least

\[
                         d_F(A,B),\qquad d_F(B,A),                 \tag{1.3}
\]

and hence

\[
                         |C|\ge2(d_F(A,B)+d_F(B,A)).              \tag{1.4}
\]

For the exact semilength-eight factor after the two `T2` suffix packets,
restrict first to paths whose intermediate owners are internal in the open
MSW forest.  The six directed-distance pairs are

| prefix owner | `d(PV0,PV1)` | `d(PV1,PV0)` |
|---|---:|---:|
| `101010001101` | `4` | `7` |
| `100011001101` | `3` | `5` |
| `100010001111` | `3` | `5` |
| `101011000101` | `4` | `6` |
| `101001010101` | `3` | `5` |
| `101001001101` | `3` | `5` |

This proves the displayed internal-owner lower bounds.  Allowing endpoint
owners gives directed-distance pairs

\[
 (4,5),(3,4),(3,4),(4,5),(3,4),(3,4),               \tag{1.5}
\]

and literal label-simple alternating cycles of respective lengths
`18,14,14,18,14,14`.  Equation `(1.4)` applied to `(1.5)` still excludes
every `C8` and `C10` through a corresponding suffix pair.  Section 5
records the exact verifier for the internal distances and explicit
`C16`s; the unrestricted-distance replay is a separate H100 diagnostic.

## 2. A common `C16` template

Number the sixteen coordinates from zero.  Put

\[
 a=0,\qquad c=10,\qquad x=13,\qquad y=14,\qquad z=15.             \tag{2.1}
\]

There are two instances:

\[
\begin{array}{c|c|c}
 b&H_b&\text{corresponding prefix owner}\\ \hline
 4&\{2,5,7,9,11,12\}&101001010101\\
 6&\{2,5,8,9,11,12\}&101001001101.
\end{array}                                                       \tag{2.2}
\]

For either row of `(2.2)`, the eight owner vertices, after suppressing the
common core `H_b`, are

\[
 ax, xy, by, ay, cy, cz, bc, bx.                            \tag{2.3}
\]

The selected incidence colours removed by the switch are

\[
 abx, axy, bxy, aby, acy, cyz, bcz, bcx,                   \tag{2.4}
\]

and the inserted colours are the one-step cyclic shift

\[
 axy, bxy, aby, acy, cyz, bcz, bcx, abx.                   \tag{2.5}
\]

Every set in `(2.3)--(2.5)` is implicitly united with `H_b`.  Each colour
in `(2.4)` contains its displayed owner in `(2.3)`, while the corresponding
colour in `(2.5)` is the union of that owner and the next owner.  Direct
MSW incidence evaluation gives

\[
 (\text{owner},\text{old colour})\in F,qquad
 (\text{owner},\text{new colour})\notin F                         \tag{2.6}
\]

in all sixteen rows of the two instances.  Hence `(2.3)--(2.5)` are two
literal alternating `C16`s.

The two instances have disjoint owner sets and disjoint colour sets, so
they may be toggled simultaneously.

## 3. Exact q2 support

At every switched owner let `M` be its unchanged other selected colour.
The local q2 change is

\[
                         [M\cup Q^+]-[M\cup Q^-].                 \tag{3.1}
\]

After cancellation, the only negatively charged targets and their complete
old loads in the post-`T2` semilength-eight factor are as follows.

### Instance `b=4`

| target | old load | new load |
|---|---:|---:|
| `1010111101011100` | `5` | `4` |
| `1010111101011010` | `5` | `4` |
| `1010010101111110` | `2` | `1` |
| `0010110101111110` | `2` | `1` |
| `0010110111111001` | `2` | `1` |
| `1010010101011111` | `2` | `1` |

### Instance `b=6`

| target | old load | new load |
|---|---:|---:|
| `1010011111011100` | `3` | `2` |
| `1010011111011010` | `3` | `2` |
| `1010010011111110` | `2` | `1` |
| `0010011011111110` | `2` | `1` |
| `1010011011111001` | `3` | `2` |
| `1010010011011111` | `2` | `1` |

The two negative target lists are disjoint.  Every old support value
therefore remains represented after either switch or both switches.  This
is support monotonicity, not equality of q2 multiplicities: the switches
also create new q2 values.

## 4. Dyck tensor

Let `W` be a Dyck word of semilength `r-8`, on coordinates after the first
sixteen, and adjoin its up-step set `U(W)` to every owner and colour in
Sections 2--3.  The MSW insertion/deletion orders concatenate:

\[
 I(XW)=I(X)\Vert(16+I(W)),\qquad
 D(XW)=D(X)\Vert(16+D(W)).                             \tag{4.1}
\]

Thus every selected base incidence in `(2.6)` remains selected, every
unselected base incidence remains unselected, and both `C16`s tensor
literally.

Every base occurrence witnessing one of the old loads in Section 3 also
tensors by `U(W)`.  A switch deletes only the one displayed tensor copy,
so the load bounds in Section 3 remain valid.  Hence q2 support remains
monotone for every `W`.

If `W\ne W'`, then `U(W)\ne U(W')`; projection onto the coordinates after
sixteen separates every owner and colour.  All tensor copies may therefore
be toggled simultaneously.

### Theorem 4.1 (tensorable cross-suffix switch bank)

For every `r>=8`, applying the two switches `(2.2)--(2.5)` for every
`W in D_(r-8)` preserves the exact owner ledger, preserves the exact
immediate-upper-colour ledger, and loses no previously represented q2
target.

## 5. Exact finite certificate and scope

The standard-library verifier is

```text
scratch/verify_t2_cross_suffix_c16_q2_safe_20260813.py
```

with SHA-256

```text
3b668ef31f46fa05c4fc6ab450a5d7c8225e3d01f408142b46884427daa474ae
```

Its H100 output has SHA-256

```text
57f5e72e435923d26754830486fa35d4298e182e52d4ff2a96a249922c75b9e7
```

The verifier independently builds the canonical semilength-eight MSW
factor, applies the two complete `T2` suffix packets, breadth-first computes
all six internal-owner directed distances, checks all old/new incidences in both explicit
`C16`s, checks pairwise owner/colour disjointness, and recomputes the full
q2 support current.

This theorem does **not** prove that the two corresponding T2 arcs are
joined into one owner chronology.  Indeed, in the tested base factor the
explicit `C16`s change the endpoint pairing through background MSW paths;
the two named owners need not lie in one resulting path component.  A
separate socket/topology and residence analysis is required.  Nor does the
theorem cover arbitrary adjacent Dyck suffixes: it supplies the aligned
pair `1100W/1010W`.

The exact advance is therefore:

\[
 \boxed{
 \text{C8/C10 are locally impossible, and an explicit cross-phase C16 exists,}
 \atop
 \text{is Catalan-tensorable, and is q2-support-safe.}}
\]
