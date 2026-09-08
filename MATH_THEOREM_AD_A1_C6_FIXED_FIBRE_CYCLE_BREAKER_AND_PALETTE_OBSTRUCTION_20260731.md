# The `a=1` fixed-fibre cycle breaker and the asymmetric-`C6` palette obstruction

Date: 2026-07-31  
Status: exact obstruction to the literal minimum asymmetric `C6`; exact
necessary-and-sufficient fixed-common-basis cycle-breaking criterion;
audited for ambient `m=3,4,5,6`; no all-`m` directed-triangle supply theorem

## 0. Verdict

The minimum asymmetric `C6` from
`MATH_THEOREM_AD_MINIMAL_ASYMMETRIC_C6_TIGHT_TRANSFER_20260731.md` is **not**
a universal local actuator for the two-coordinate recursion of Theorem 6.1
in `MATH_THEOREM_CATALAN_BALANCED_SUBCUBE_RESERVE_AND_EXACT_COLLAR_DEFECT_20260731.md`.
It fails before the physical forest row.

The tight-enumeration packet deletes occurrences

```text
(9,15), (17,51), (9,57)
```

and adds

```text
(3,27), (9,45), (17,57).
```

Two deleted atoms have the same lower palette vertex `9`.  Hence the old
half cannot be a subset of any outer-perfect side matching.  Reversing the
packet makes the terminal half invalid; complementation moves the duplicate
to the upper shore.  Coordinate relabelling and fixed-coordinate suspension
preserve the equality pattern.

The correct local actuator is a different object: an alternating `C6` in
the **outer incidence matching**, equivalently a directed triangle in the
exchange digraph of one punctured side matching.  Such a packet preserves
the common basis and both puncture maps exactly.  It breaks the remaining
physical cycles precisely when its full-support contraction is loopless and
acyclic and its signed attachment equations are consistent.

## 1. The fixed `a=1` fibre

Use the notation of Theorem 6.1.  The parent parameter is `m=n+1`; on the
`2n` core coordinates put

\[
 M=\binom{2n}{n},\quad N=\binom{2n}{n-1},\quad
 P=\binom{2n}{n-2},\quad K=M-N=\operatorname {Cat}_n,
\]

\[
                    C=M-P,\qquad R=P-K.               \tag{1.1}
\]

Fix the selected child set `Q` and port maps `p^-,p^+` of Theorem 6.1.
In the SCD-aligned sharpening, this means fixing the common deep-flag
basis `E` together with its two singleton-port bijections; `Q` is the
union of `E` with the already forced shallow child bank.  These data fix
the omitted rank-`n` port bank on each side.  The two diagonal sectors are
then
punctured outer-perfect matchings:

* the `empty -> empty` sector matches its selected rank-`n` palette to
  every rank-`n+2` palette vertex;
* the `{c,z} -> {c,z}` sector matches every rank-`n-2` palette vertex to
  its selected rank-`n` palette.

The later theorem
`MATH_THEOREM_CATALAN_TWO_COORDINATE_COMMON_BASIS_AUTOMATIC_20260731.md`
proves that an appropriate synchronized basis exists for every child
forest when `n>=4`; a selected finite `n=3` interface is separately
realized.
Nothing below reopens that incidence result.  The issue here is whether the
**physical representatives** of the resulting punctured side matchings can
be locally exchanged without losing their palettes, degree caps,
contracted acyclicity or inherited endpoint roles.

No other sector uses either unpunctured outer trace.  Therefore a local
edit which keeps `Q,p^-,p^+` fixed must be an alternating-cycle exchange
inside the relevant side matching.  Even if the puncture image is allowed
to change, the unpunctured shore must still have zero palette flux.

## 2. Dimension-uniform obstruction to the literal packet

Desuspend the common coordinate of the six physical owners and then adjoin
an arbitrary fixed suspension set `H`.  Name five distinct active
coordinates `a,b,r,c,d`, all outside `H`.  In cyclic order the physical
ports are

\[
\begin{array}{lll}
X_0=H+a+r,&X_1=H+b+r,&X_2=H+r+d,\\
X_3=H+r+c,&X_4=H+c+d,&X_5=H+a+c.
\end{array}                                           \tag{2.1}
\]

The old half is `X_0X_1,X_2X_3,X_4X_5`; the new half is
`X_1X_2,X_3X_4,X_5X_0`.  Their lower labels are respectively

\[
             H+r,\ H+r,\ H+c
       \quad\longrightarrow\quad
             H+r,\ H+c,\ H+a,                       \tag{2.2}
\]

and their upper labels are

\[
\begin{array}{c}
 H+a+b+r,\ H+r+c+d,\ H+a+c+d\\[1mm]
 \longrightarrow\\[-1mm]
 H+b+r+d,\ H+r+c+d,\ H+a+r+c.
\end{array}                                           \tag{2.3}
\]

Thus the exact palette flux is

\[
 \partial_L={\bf e}_{H+a}-{\bf e}_{H+r}\ne0,          \tag{2.4}
\]

\[
 \partial_U={\bf e}_{H+a+r+c}+{\bf e}_{H+b+r+d}
             -{\bf e}_{H+a+b+r}-{\bf e}_{H+a+c+d}\ne0. \tag{2.5}
\]

### Theorem 2.1 (literal actuator no-go)

No coordinate relabelling, fixed-coordinate suspension, reversal or
complement of the minimum asymmetric `C6` is a palette-preserving exchange
inside either punctured side matching of an `a=1` fibre, for any fixed
choice of `Q,p^-,p^+` (and hence for any fixed aligned common basis `E`).

#### Proof

An outer matching contains at most one atom incident with any lower or
upper palette vertex.  Equation (2.2) gives a repeated old lower vertex, so
the old half cannot occur in the lower side matching.  Reversal places the
same repetition in the proposed terminal matching.  Complementation swaps
lower and complementary upper labels, moving rather than removing the
collision.

Relabelling and adjoining `H` are injective maps on every palette layer and
therefore preserve all equalities and inequalities in (2.2)--(2.5).
Moreover (2.5) is nonzero on the unpunctured shore.  Thus moving the
puncture while leaving this three-edge packet as an isolated side exchange
cannot compensate it.  A simultaneous compensating edit outside the packet
is a different, global operation and is not excluded.  \(\square\)

For audit only, one may attach three abstract old/new membership bits to
the packet.  There are `20` pairs of such bit patterns having equal old and
new cardinality, and none changes the already computed endpoint flux
(2.4)--(2.5).  This is **not** a model of a global common-basis exchange:
diagonal side atoms are not child atoms in `Q`.  It merely confirms that
reclassifying the three local records cannot cure their endpoint collision.
A compensating packet elsewhere or a global child-factor/common-basis
rethread is not covered by this local statement.

This explains the difference from the positive tight-enumeration setting.
A Hamilton support may use a lower colour more than once; a selected
Catalan matching cannot.

## 3. Exact replacement: directed-triangle exchange

Let

\[
                       D=\{(L_i,U_i):i\in I\}          \tag{3.1}
\]

be either fixed punctured side matching.  Define its exchange digraph
`K_D` on `I` by

\[
                 i\longrightarrow j
       \quad\Longleftrightarrow\quad L_i\subset U_j.  \tag{3.2}
\]

### Theorem 3.1 (strict three-atom exchange)

A strict three-atom exchange preserving exactly the lower and upper
palettes of `D` exists on pairwise distinct indices `i,j,k` if and only if,
after a cyclic ordering of them,

\[
                         i\to j\to k\to i             \tag{3.3}
\]

is a directed triangle of `K_D`.  The switch is

\[
\begin{array}{c}
(L_i,U_i),(L_j,U_j),(L_k,U_k)\\
\longrightarrow\\
(L_i,U_j),(L_j,U_k),(L_k,U_i).
\end{array}                                           \tag{3.4}
\]

It preserves the punctured palette, the selected child set `Q`, the aligned
common basis `E` when that sharpening is used, and the maps `p^-,p^+`
literally.

#### Proof

Any palette-preserving exchange keeps the same three lower and three upper
vertices and only permutes their partners.  If all three atoms change, the
permutation has no fixed point and is therefore one of the two 3-cycles.
The three new diamonds exist exactly when their containments give (3.3).
Conversely (3.3) makes all three new pairs valid, and (3.4) visibly retains
each palette vertex once.  Since the puncture sets themselves do not
change, neither do `Q,p^-,p^+`.  \(\square\)

The six incidence edges in (3.4) form an alternating Boolean-incidence
`C6`.  This is not the physical six-port packet of Section 2.

### Corollary 3.2 (nearest palette-neutral local replacements)

On five active coordinates, write `02` for the owner set `{0,2}` and so
on.  Among all oriented strict palette-neutral alternating `C6` packets in
the complete owner graph `J(5,2)`, define

\[
 d((A,B),(A_0,B_0))
 =\frac{|A\mathbin\triangle A_0|+|B\mathbin\triangle B_0|}{2},       \tag{3.5}
\]

where `(A_0,B_0)` is the desuspended asymmetric packet.  There are exactly
`40` such oriented packets, with distance histogram

```text
d=3: 2,     d=4: 2,     d=5: 14,     d=6: 22.
```

The two minimizers are

```text
{02-04, 03-34, 23-24} -> {02-24, 03-04, 23-34},
{12-14, 13-34, 23-24} -> {12-24, 13-14, 23-34}.          (3.6)
```

They are in one oriented `S_5` orbit.  Each old and new half has the same
three distinct lower labels and the same three distinct upper labels, so
each is precisely a directed-triangle exchange of Theorem 3.1.  Common
suspension transports it to every higher lower-side layer, and complement
transports it to the dual diagonal side.

#### Finite proof and scope

There are only ten rank-two owners.  Enumerate each six-owner subset, every
Johnson perfect matching on it, and every ordered pair of disjoint
matchings whose union is one alternating cycle; retain the pairs having
equal lower and upper palette multisets.  This gives the `40` rows and the
displayed complete distance histogram.  Direct intersection/union replay
gives (3.6), and coordinate permutations put the two rows in one orbit.

This is a local supply catalogue, not an extension theorem.  A row is
usable for a fixed recursion only if its old triple occurs in the supplied
punctured matching and the full-support tests of Section 4 pass.  No such
occurrence is asserted for an arbitrary common basis, SCD or the frozen
`m=3` Hamilton carrier.

## 4. Exact forest-compatible common-basis gate

Let `S` be the complete undirected physical support after the common basis,
both side matchings, the central sector, cross flags, recursive core and all
fixed attachments have been installed.  For one directed-triangle switch,
or for a family of pairwise index-disjoint triangles, let `A` be the old
physical edges and `B` the new physical edges, and put

\[
                              T=S-A.                  \tag{4.1}
\]

### Theorem 4.1 (fixed-fibre cycle breaker)

The switched support `(S-A)+B` is a linear forest if and only if all three
conditions hold:

1. `T` is a linear forest;
2. `deg_T(v)+deg_B(v)<=2` for every physical owner `v`;
3. after contracting every component of `T`, the multigraph formed by `B`
   is loopless and acyclic.

Together with a directed triangle on each edited side, these conditions are
necessary and sufficient for preserving every outer row of Theorem 6.1 and
its undirected physical forest row while keeping the common basis fixed.
Overlapping triangles must instead be applied sequentially in the updated
matching, or treated as one global palette-preserving partner permutation;
their set-theoretic union is not covered by this formulation.

#### Proof

Outer exactness and the fixed port data follow from Theorem 3.1.  If the
terminal support is a linear forest, its subgraph `T` is a linear forest,
the degree inequalities are necessary, and a loop or cycle after
contraction would expand through the unique paths of `T` to a terminal
cycle.

Conversely conditions 1--2 give maximum degree at most two.  Any terminal
cycle contracts to a loop or cycle in the component multigraph, forbidden
by condition 3.  Hence the terminal support is a linear forest.  \(\square\)

### Proposition 4.2 (signed tail/head ledger)

Assume some edges or attachments already have prescribed directions.  For
every nontrivial path component `P` of `T`, choose a reference orientation,
let `x_P in F_2` record whether it is reversed, and label its two endpoints
by `0,1` in the reference direction.  For an isolated component incident
with `d=1` or `2` edges of `B`, give those incidences abstract endpoint
slots as follows: for `d=1`, choose either slot `0` or `1`; for `d=2`,
choose a bijection of the two incidences with the two slots.  Introduce the
same reversal bit after this choice.  A new edge joining slot `i` of `P` to
slot `j` of `Q` preserves one-in/one-out chronology exactly when

\[
                   x_P\mathbin\oplus x_Q=1\oplus i\oplus j. \tag{4.2}
\]

First require that the prescribed arrows internal to each nontrivial
component agree with one of its two orientations; they then pin the
corresponding variables.  Prescribed roles at an isolated owner constrain
its slot assignment and reversal bit.  The tail/head ledger extends if and
only if there is a choice of all isolated-component slots for which this
affine system is consistent.

#### Proof

A nontrivial path has only its two global orientations.  An isolate has two
abstract chronology slots: when it receives two joins they must occupy
opposite slots, and when it receives one join either slot may be used.
Equation (4.2) says exactly that the slots joined by every new edge receive
opposite head/tail roles.  Satisfying all join equations, slot choices and
pins orients every terminal path consistently; conversely every valid
terminal orientation supplies those slots and values `x_P`.
\(\square\)

For the literal six-port physical `C6`, only two of the eight assignments
of head/tail roles to its three old edges preserve all six old port-role
labels when the new edges are installed.  Thus it also fails to be
universal for that frozen six-port signature, independently of its palette
obstruction.  This `2/8` count is not a census of arbitrary external
attachment ledgers; those are governed by Proposition 4.2.

### Corollary 4.3 (cycle-rank bound)

One three-edge switch can finish only if

\[
                              \beta(S)\le3,            \tag{4.3}
\]

where `beta` is the cyclomatic number.  One switch on each side requires
`beta(S)<=6`.  If `S` has maximum degree at most two, `A` must meet every
cyclic component; after those cuts, Theorem 4.1 decides exactly whether
`B` recreates a cycle.

#### Proof

Deleting one edge lowers cyclomatic number by at most one.  Condition 1 of
Theorem 4.1 therefore requires `beta(S)<=|A|`.  In a degree-two
pseudoforest, a cyclic component remains cyclic unless at least one of its
edges is deleted.  \(\square\)

Theorems 3.1--4.1 are the requested forest-compatible common-basis gate.
They are exact for a supplied packet, but they do not prove that every
common basis or every cycle contains a suitable directed triangle.

## 5. Targeted audit for `m=3,4,5,6`

The scalar collar and literal-packet rows are:

\[
\begin{array}{c|c|r|r|r|r|r|r}
m&n&M&N&P&K&C&R\\ \hline
3&2&6&4&1&2&5&-1\\
4&3&20&15&6&5&14&1\\
5&4&70&56&28&14&42&14\\
6&5&252&210&120&42&132&78
\end{array}                                           \tag{5.1}
\]

At `m=3`, `R=P-K=-1`, so the `a=1` integral collar gate is already
scalar-impossible.  At `m=4`, the first valid collar instance, the
desuspended packet embeds in the rank-`n-1=2` side layer but its old half
has only two distinct lower palette labels.  Fixed suspensions give the
same `2/3` collision at `m=5,6`.  On the complement-dual side the old half
has only two distinct upper labels.  In every embedded row the unpunctured
palette flux is nonzero.

The two rows (3.6) are the nearest valid zero-flux replacements at `m=4`;
their common suspensions remain valid local partial matchings at `m=5,6`.
This does not say that the fixed diagonal matching selected by a given
common basis contains either old triple.

Nor does the literal-packet no-go contradict the known complete finite
recursions at child parameters `n=3,4`: those fixtures choose different
side representatives and need not contain this packet.

The frozen tail/head test has exactly two compatible signatures among the
eight orientations of the three old physical edges.  These counts are
unchanged by suspension.  The independent audit also exhausts the `20`
equal-cardinality pairs of abstract three-bit local membership signatures
at each of `m=4,5,6`; none changes either palette delta.  As stressed in
Section 2, this diagnostic is not a global `Q`/common-basis exchange.

This audit is deliberately local.  It verifies the scalar ledger and every
equality, palette flux and role signature of the authenticated packet; the
proof of Theorem 2.1 covers all coordinate relabellings and suspensions.  It
does not enumerate common bases, SCDs or global factors.

## 6. Scope and surviving theorem

What is closed:

* the exact minimum asymmetric `C6`, its reverse, complement and every
  suspension cannot act inside a fixed punctured side matching;
* changing only the local puncture/membership record, without a second
  compensating physical edit, cannot absorb its nonzero unpunctured flux;
* the exact replacement packet is a directed triangle in `K_D` satisfying
  the contraction and signed-orientation tests;
* at the first valid collar size there are exactly two closest labelled
  zero-flux replacements, one up to coordinate relabelling;
* one such packet cannot remove more than three independent cycles.

What remains open:

* directed-triangle supply inside side representatives compatible with an
  automatically available recursive common basis;
* choosing one or more triangles so the full contraction is acyclic;
* joint availability on both sides with a consistent signed attachment
  system; and
* all downstream residence, deep-shadow and compiler rows.

Accordingly the asymmetric tight-enumeration `C6` is a useful common-core
Hall repair, but not a side-matching actuator.  The recursion needs an
incidence-alternating, zero-flux `C6` selected jointly with the common basis.

## 7. Reproducible audit

Primary targeted audit:

* `scratch/audit_ad_a1_c6_common_basis_gate_m3_m6_20260731.py`,
  SHA-256 `66e3b726111eb3fba72cc738192d9f7b149e2eaa8f803e2fee5a816ddc26163a`;
* `scratch/ad_a1_c6_common_basis_gate_m3_m6_20260731.audit.json`,
  SHA-256 `68647ba0a931ccd5c48799b98bc430902baafa18395ab61cded453cb9acdc12d`,
  payload `372c567c50c4dd713580dd68a26ea9c01f5716e4cbdd0f1109627774d8878da8`.

Independent replay from the original six bitmask edges:

* `scratch/verify_ad_a1_c6_common_basis_gate_m3_m6_20260731.py`,
  SHA-256 `910470fa92102463e939f8c7ef3e6a99e6d476e9c0dd81d3471b788b7d11dc8a`;
* `scratch/ad_a1_c6_common_basis_gate_m3_m6_20260731.independent.audit.json`,
  SHA-256 `1d423b7977f34e26bb108377dcdd92c22985b36a636a1d59b51871260e53d214`,
  payload `b236b62c26c75e505ca507e2442f8c16186f057cbd9f52c8ed95841673a684b4`.

Both audits check (5.1), the raw and suspended palette signatures, the
complement-dual obstruction and the exact `2/8` tail/head count.  They do
not claim a global factor census.

Nearest zero-flux replacement catalogue:

* `scratch/audit_ad_a1_c6_palette_neutral_replacements_20260731.py`,
  SHA-256 `16831cb3675959002a4f5f2afb5452cdb915db51a078c29945c9c47f5e53ff56`;
* `scratch/ad_a1_c6_palette_neutral_replacements_20260731.audit.json`,
  SHA-256 `db586363f0cb5725c1292c6fc019d644cb6aafe991f0d5bbc769533966c226a8`,
  payload `ec173c0e646be365a7bb5d8b201c3ca0ef63ed65221568715c48349736465f23`.
* `scratch/verify_ad_a1_c6_palette_neutral_replacements_20260731.py`,
  SHA-256 `13d668285b09978c921b33c845f5eadc29077b7e93e74b7755e0090f4193a297`;
* `scratch/ad_a1_c6_palette_neutral_replacements_20260731.independent.audit.json`,
  SHA-256 `ac47787a1d9712a121b3553b2148f208acbbad9b2ff7d8ba15f4fb47e58a6dc2`,
  payload `238a745176f8e4fa8e7704e534abd81605154ba15c05e2348102b175eb9f698d`.

The producer enumerates six-owner Johnson matchings; the independent replay
generates the same count and distance frontier from symbolic incidence
triangles.  This is a complete ten-owner local enumeration, not a search
over SCDs, common bases or physical factors.
