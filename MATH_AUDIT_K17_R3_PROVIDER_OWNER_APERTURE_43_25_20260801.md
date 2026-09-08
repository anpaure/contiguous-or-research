# The fixed-`r3` provider obstruction is a `43 -> 25` owner aperture

## Status and scope

This note gives an exact finite theorem for the corrected one-facing
provider atlas of the current `k=17` rich-157, fixed-`r3` chronology.  It
uses the fixed J1/J2/J3 owner reservations and cut assignments.

It is a **provider-only** theorem.  The provider witnesses here have not
yet been intersected with every variable L3 socket candidate, so this is
not a unified socket/provider certificate and is not a proof of
`nu(17)=24313`.

The corrected endpoint convention is essential: a left-finish witness
requires only its seam-facing right boundary cut, and a right-start
witness requires only its seam-facing left boundary cut.  The far end may
continue into the residual native path.

The nineteen targets declared internal before the provider solve are

```text
68223,71133,71383,71595,72681,72947,73078,73585,75006,
78071,79517,80358,81734,83446,85595,85775,88251,69609,69624
```

The fixed macro cuts are

```text
forced:
1436:2,1436:3,1209:3,1209:6,
151:1,294:1,294:4,
2:3,2:4,672:7,672:9

forbidden:
1209:4,1209:5,
294:2,294:3,
672:8
```

Only one of these fixed assignments is present in the reduced provider
cut-variable universe, but retaining it changes the base CNF by one unit
clause.  All certified thresholds below use that corrected CNF.

## 1. Exact provider threshold

There are 348 externally assigned provider target groups after the
nineteen declarations above.  A provider occurrence reserves physical
owner positions and imposes required/forbidden cut literals.  At most one
occurrence is selected for each non-internal target; reserved owner
positions have capacity one.

### Theorem 1.1

Exactly eighteen further targets must be declared internal in this
provider model.

### Certification

* budget 17 is UNSAT;
* budget 18 is SAT;
* the budget-17 Kissat proof was replayed by `drat-trim` with status
  `VERIFIED`;
* the budget-18 model was replayed independently against every DIMACS
  clause with zero assignment conflicts, zero unsatisfied clauses, and
  zero unknown clauses.

There is an optimal bank avoiding the L3-socket-dead target `73592`:

```text
29053,29886,30332,47709,49659,53208,68571,73145,79796,
80238,80880,82937,83323,85880,85972,86000,86207,91326
```

## 2. A 43-target core carries the whole obstruction

The budget-17 proof exposes the following 43-target subsystem:

```text
7550,8046,8110,17855,23742,26616,29053,29886,30332,
31190,31356,36091,39357,43199,46255,47421,47709,48492,
49659,53208,64325,68571,72542,73145,73592,75701,77238,
78206,79796,80238,80880,81181,81321,82937,83323,85370,
85880,85972,86000,86207,90874,91326,91763
```

Rebuilding the provider problem on these 43 targets alone gives:

* 424 provider witness rows;
* budget 17 UNSAT, with an independently verified DRAT proof;
* budget 18 SAT, with an independently replayed model.

Thus the remaining 305 target groups are irrelevant to the lower bound:
all eighteen necessary internalizations can be confined to this core.

## 3. Human-scale owner-aperture certificate

Let `R(w)` be the reserved-owner footprint of a provider witness `w`.
The following set `P` of 25 physical owner positions meets every one of
the 424 core witness footprints:

```text
28:5,108:4,219:0,300:0,381:4,410:3,434:2,651:5,794:1,
846:3,1091:7,1130:1,1143:5,1146:3,1178:0,1259:0,
1268:4,1307:2,1329:0,1330:0,1598:3,1793:0,2006:1,
2347:6,2558:0
```

All 25 positions lie on different native components.

### Theorem 3.1 (owner-aperture lower bound)

At most 25 of the 43 core targets can be supplied by mutually compatible
provider witnesses.  Hence at least

\[
43-25=18
\]

core targets must be internal.

### Proof

For every core witness `w`, the literal audit gives

\[
R(w)\cap P\ne\varnothing.                 \tag{3.1}
\]

Choose one position of `R(w) intersection P` for each selected witness.  Two
selected witnesses cannot choose the same position because physical owner
positions have capacity one.  Therefore the selected witnesses inject
into `P`, and there are at most 25 of them.  Since the core has 43 target
groups, at least 18 are internal.  The budget-18 model proves sharpness.
\(\square\)

The cover audit is especially tight:

* 384 of the 424 witness rows meet `P` in exactly one position;
* the remaining 40 meet it in exactly two;
* 34 targets can meet only one member of `P` over their entire witness
  menu, eight can meet two, and one can meet three.

A separate hitting-set census proves that 24 owner positions do not cover
all 424 witness footprints, while the displayed 25 do.  This minimum-cover
fact is not needed for Theorem 3.1, but confirms that the aperture
certificate is itself sharp.

## 4. Rank, orbit, and facet anatomy

The core is not a missed cyclic orbit:

* all 43 targets have rank 10;
* all 43 lie in distinct `Z_17` rotation orbits;
* the optimal eighteen-target bank above also has eighteen distinct
  rotation orbits.

Nor is it one dense Johnson facet cluster.  At Johnson distance one
(symmetric difference two), the core has only 14 edges.  Its nontrivial
connected components have vertex sizes

```text
3,3,2,2,2,6,2,2
```

and the remaining targets are isolated at that distance.

The core is instead strongly localized in the opened physical chronology.
Across its 43 rank-10 masks the coordinate degrees are

```text
19,22,27,34,36,35,27,25,31,20,26,27,25,23,21,10,22
```

against mean `430/17 = 25.29`.  This phase imbalance, together with the
25-component aperture, identifies the obstruction as physical provider
funnelling rather than necklace arithmetic.

The omitted banks are biased toward low-menu targets: the 18-target
socket-safe bank has median four provider witnesses, versus median twelve
over the complete provider target family.  Nevertheless it includes
targets with 22 and 30 witnesses, so raw candidate degree alone does not
explain the obstruction; the shared aperture does.

## 5. Provider packing, aperture covers, and the exact min--max

The useful general invariant suggested by this audit is not merely raw
candidate count.

Perform every certified native shared-range fusion first, treating the
fused object as one packet.  Let `E` then be the set of one-capacity
physical owner tokens.  For each target `x` in a
target family `C`, let `W_x` be its menu of provider packets, and let

\[
 R(w)\subseteq E
\]

be the nonempty owner footprint of packet `w`.  Define the actual provider
rank

\[
 \rho(C)=\max\{|I|:\ I\subseteq C\text{ has a jointly compatible
 provider }w_x\in W_x\ (x\in I)\}.          \tag{5.1}
\]

Compatibility includes disjoint owner footprints and every other literal
condition, such as common cut assignments.  Consequently the exact number
of targets of `C` that must be internal is

\[
 \iota(C)=|C|-\rho(C).                       \tag{5.2}
\]

This equality is a definition, not yet a tractable min--max.  Owner
apertures give a useful certified relaxation.

### Definition 5.1 (owner-aperture cover)

An owner set \(P\subseteq E\) covers `C` when

\[
 R(w)\cap P\ne\varnothing
 \qquad(x\in C,\ w\in W_x).                 \tag{5.3}
\]

Let

\[
 \tau(C)=\min\{|P|:\ P\text{ covers }C\}.   \tag{5.4}
\]

This is the transversal number of the hypergraph whose edges are all
provider footprints.  Any compatible packet family is a matching in that
hypergraph.  Hence the standard packing--cover inequality gives

\[
 \rho(C)\le \tau(C),
 \qquad
 \iota(C)\ge |C|-\tau(C).                   \tag{5.5}
\]

The second inequality is useful when \(\tau(C)<|C|\); it need not be sharp
for an arbitrary packet hypergraph.

### A sharper transversal-matroid relaxation

Fix a cover `P`.  Form a bipartite graph `G_P` with shores `C` and `P`,
joining `x` to `p` when some packet in `W_x` contains `p` in its owner
footprint.  Any jointly compatible provider family maps injectively to a
matching in `G_P`: choose, for each selected packet, one member of its
nonempty intersection with `P`.  Disjoint packet footprints make the
chosen members distinct.

Let `r_P(C)` be the matching rank of `G_P`.  It is the rank of the
transversal matroid induced on `C`, and

\[
 \rho(C)\le r_P(C)\le |P|.                  \tag{5.6}
\]

Hall's theorem gives the exact min--max

\[
 r_P(C)
 =\min_{X\subseteq C}\bigl(|C\setminus X|+|N_P(X)|\bigr), \tag{5.7}
\]

or equivalently

\[
 |C|-r_P(C)
 =\max_{X\subseteq C}\bigl(|X|-|N_P(X)|\bigr).             \tag{5.8}
\]

Thus every aperture cover `P` supplies the rigorous lower bound

\[
 \iota(C)\ge |C|-r_P(C).                    \tag{5.9}
\]

For singleton packet footprints with no additional incompatibilities,
this is the exact provider min--max.  For general multi-owner packets it
is an upper relaxation of provider rank unless a compatible packet packing
attains it.

### The finite core has packing--cover equality

For the displayed 25-position set `P`, the literal audit verifies (5.3),
and a 25-edge matching exists in `G_P`.  The separate owner-cover census
gives

\[
 \tau(C)=25:
\]

cover budget 24 is DRAT-verified UNSAT, while the displayed budget-25
cover is SAT and independently replayed.  The corrected fixed-cut provider
model also supplies 25 core targets.  Therefore this finite core satisfies

\[
 \rho(C)=r_P(C)=\tau(C)=25,
 \qquad
 \iota(C)=43-25=18.                         \tag{5.10}
\]

The packing--cover equality in (5.10) is an audited fact about this finite
core, not a claimed theorem for arbitrary provider packet systems.

## 6. Dimension-uniform expansion sufficient for bounded sockets

The global q1 problem is conditional, not an exact-one provider problem
on a preselected target list.  A chosen cut may destroy an old q1 witness
of colour `t`.  Its correct clause has the form

\[
 z_e\Longrightarrow
 \left(i_t\ \lor\!\bigvee_{w\in W_t} y_w\right),           \tag{6.1}
\]

where `i_t` means that `t` is delivered internally and `y_w` selects a
literal provider packet.  The packet variable implies all of its owner,
orientation, required-cut, forbidden-cut, and residence conditions.

For a feasible host/cut state `z`, let `C(z)` be the activated colours and
let `rho_z` be provider rank after restricting every menu to packets
compatible with `z`.

### Proposition 6.1 (all-cut provider expansion)

Assume that an absolute constant `K` satisfies

\[
 \rho_z(C(z))\ge |C(z)|-K                 \tag{6.2}
\]

for every feasible state `z`, and that the construction exports `K`
literal internal sockets capable of serving the residual colours.  Then
all global q1 clauses can be satisfied with at most `K` internal targets.

### Proof

For the chosen state `z`, select a compatible provider family of size at
least `|C(z)|-K` and assign the remaining at most `K` colours to the
internal sockets.  This satisfies every implication (6.1).  The statement
is uniform because the same `K` works for every feasible `z`.
\(\square\)

Condition (6.2) is the exact sufficient rank statement.  A more
checkable Hall formulation is available when the protected host
singletonizes its provider packets, or otherwise proves that the packet
system is a transversal matroid: then it suffices that

\[
 |N_z(X)|\ge |X|-K
 \qquad(X\subseteq C(z)).                    \tag{6.3}
\]

Without such an integrality/realization theorem, a large neighbourhood or
a large aperture cover alone does not imply a compatible packet packing.

### Reconciliation with the protected-host theorem

A dimension-uniform protected host sufficient for `B(k)+O(1)` should now
export the following q1 interface:

1. every admissible cut pattern determines its activated family `C(z)`;
2. structural-zero colours are either forbidden from activation or have
   named internal sockets;
3. the surviving provider packet system satisfies (6.2), or satisfies
   (6.3) in a proved transversalizable packet class;
4. the at most `K` residual targets are routed through the protected pivot
   or other bounded internal packet bank;
5. the same bounded interface regenerates in the next Pascal child.

Together with the already separate residence, arbitrary-width upper deck,
topology, and lower-compiler gates, this gives the bounded q1 sidecar
needed by a regenerative protected-host theorem.

The fixed-`r3` chronology fails this desired expansion sharply: the
activated 43-target core has rank only 25.  That does not refute the
programme; it says that the host, cut pattern, or internal macro bank must
be reselected jointly.  A pivot or native macro helps not only by
delivering a missing colour, but by opening an owner aperture outside the
current bottleneck set.

The global cap-32 export made for the next selector covers 16,708 of the
19,448 rank-10 colours and has 2,740 structural zeros relative to the
current pre-atlas seam source.  Those zeros are exact for that source
atlas.  The cap of 32 is only a search sparsification for the nonzero
menus; a proof of (6.2) must use the full menus or justify a sparse
rank-preserving certificate.

## 7. Reproducible artifacts

The compact proof package is under
`scratch/k17_r3_provider_owner_aperture_20260801/`.

Key SHA-256 values:

```text
core target list
1a23d353d7b7a39ddcfd226b07127057d2bfe05d4187c4ad8f4f5abeb4a64e2d

43-target budget-17 CNF / DRAT / replay
e915d1f4b4af1348685497ef0ecba3960848030b0b493369ad0db4f645222a6f
d69f303912c5e56e02e65e6f22df7f440d2fc060e5ea2fa805ea5140170826f0
491f880666ae09a77dba5ff2c4838d6f19d0bba5a254872404580ab23484516a

43-target budget-18 CNF / model / independent replay
204fd61d9140015c975e1fb23a1f8e51319d080b853ec35adbe453b3808850ae
62adc4db87624fc6efcd399c53fc799136205c449089fd1ce6db8177b07b7f07
9e3525f1c6e966aa9b66ff4ddef8a063819cac8003d0a20a427b0cd4c09f8f82

owner-cover budget-24 CNF / DRAT / replay
6d2badf0ec35893ee70ff416a47f3f93bd0762b42541540dad62c0ee13e09454
8548f9f2f483c89d03fd200344c3dafc92fd139273df2349fe670ddd76e82a14
09da4f3f91179ea0da43d765cec41285b162d191eccd96dbc4436eaea12ce9c5

owner-cover budget-25 CNF / model / independent replay / literal audit
5e796dd1b8a5722dcaadbdd399ad6ab185e96d85c61a8668bdaa412c59b43db4
7a12f99e7b450bc40fe325d43e233a59dac8a33ff1cb9412b5548c6a11d189d9
c7cd341434385283d5656ae9e4036c61b8b5c78ccd2651cb3dcd8006ad9b5edc
a6c997d7b3bf9a90870c3f476100814a5409299cf73526dc500210b9be715c65

25-edge transversal matching certificate
d66836774e9ae027f62e611e5d574cbd4907a9ce0533b1cd192ebd7c9bf5dd93
```

The full corrected fixed-cut artifacts remain on the H100 CPU host under
`/dev/shm/k17_r3_provider_unified_fixedcuts_ladder/`.
