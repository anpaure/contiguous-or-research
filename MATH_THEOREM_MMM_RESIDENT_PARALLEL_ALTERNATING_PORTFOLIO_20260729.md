# MMM parallel and alternating switches on the resident `k=15` factor

Date: 2026-07-29

Status: exact composition theorems, independent selector-175 audit, complete
enumeration of the published switches that are immediately alternating at the
resident endpoint (the baseline-enabled family), and a reproducible finite
overlay-circuit normal form.  The
finite conclusions preserve exact middle ownership and the lower first-shadow
deck.  They do **not** produce a carrier with complete lower `q2`, complete
upper shadows, or a common literal compiler word.

Unless explicitly called physical, every numerical "hole" count below is a
count of rotation-orbit representatives.  Literal physical support weights a
representative by the size of its rotation orbit.

## 0. Verdict

Let `F_res` be the residence-perfect strict quotient factor stored in

```text
scratch/fixtures/k15_residence_hint_explicit_v1.json
```

and let `Mbar_15` be the phase-labelled bipartite necklace multigraph on its
`429+429=858` central vertices.

1. A family of parallel-label switches on one fixed oriented quotient cycle
   has an exact additive voltage/prefix cocycle.  Its physical coordinate
   trace, when the terminal voltage is a unit, is one explicit columnwise
   affine shear.  Distinct menus commute;
   fixed-depth shadow interactions have finite chronological range, while
   unrestricted upper intervals remain global.

2. Selector 175 is independently verified:

   ```text
   (1807,7,12) -> (1807,11,12).
   ```

   It changes voltage `1 -> 8`, preserves the 6,435 middle owners and the
   complete lower-`q1` deck, remains residence-clean, preserves the lower-`q2`
   hole set and lower-`q2` pair-collision energy, and improves exact all-width
   upper holes `95 -> 94`.  Its upper native-rank deficit also falls by 180
   physical units.  It is not lower-`q2` load-neutral and creates the new
   lower-`q3` hole `1159`.

3. Of all 131 labelled published MMM gluing `C6` packets, exactly two are
   alternating at `F_res`.  Together with the five resident parallel digons,
   they form the complete seven-atom, 128-state **baseline-enabled**
   resident-local published cube.
   All 128 toggles retain quotient degree two; 54 lift to one physical cycle.
   Exactly two states are simultaneously one physical cycle, residence-clean,
   and lower-`q2` support-neutral: the baseline and selector 175 alone.  Thus
   selector 175 is the unique nontrivial best collision-neutral portfolio in
   this resident-local published family.

4. Overlaying `F_res` with the frozen published MMM shift-one factor gives one
   ordinary connected red/blue support, not a Boolean cube of ordinary
   components.  Pairing red and blue incidences lexicographically decomposes
   it into ten edge-disjoint alternating circuits of lengths

   ```text
   468, 374, 190, 116, 42, 34, 6, 6, 6, 4.
   ```

   The analogous 34 potential-arborescence overlays give circuit dimensions
   six through ten and exactly 10,624 raw states.  Together with the 1,024
   states of the published overlay, the 35 actual MMM endpoints yield 11,648
   raw circuit-cube states before deduplication.  This is a sound bounded
   portfolio for terminal physical audit, but it depends on the chosen
   incidence pairing and is not the full alternating-circuit space.

5. Selector 175 is not a quotient `C6`.  It is a parallel quotient digon; its
   relative voltage seven lifts to one alternating physical 30-cycle.  The
   physical `C6` is the distinct MMM gluing-pair generator.

## 1. Quotient model and ledgers preserved automatically

Put

\[
 k=15,\qquad m=7,\qquad r=8,\qquad
 N=\operatorname{Cat}_7=429,\qquad W=kN=6435.
\]

The bipartite quotient multigraph `Mbar_15` has upper vertices equal to the
rotation orbits of rank-eight sets and lower vertices equal to the rotation
orbits of rank-seven sets.  Its edges are **labelled inclusion-edge orbits**;
parallel labels are retained.

A spanning quotient 2-factor `F` has degree two at every upper and lower
necklace.  At each lower necklace its two incidences contract to one coloured
Johnson edge between upper necklaces, possibly a quotient loop when those
upper necklaces coincide.  The two physical upper neighbors are nevertheless
distinct.  Therefore every such factor has:

* exact quotient middle degree two; and
* one selected contracted edge over every lower necklace.

After a physical lift which visits every central orbit once, these become
exact middle ownership and a perfect physical lower-`q1` deck.  They are raw
degree ledgers.  Residence, lower `q2`, upper shadows, connectivity, voltage,
and the literal compiler remain additional gates.

## 2. Exact multi-parallel-switch shear

Fix one oriented unlabelled quotient Hamilton cycle.  Enumerate its upper
necklaces as `U_j`, `j in Z_N`.  Choose representatives and let the oriented
edge-label voltages be `alpha_j in Z_k`.  Set

\[
 s_0=0,\qquad s_{j+1}=s_j+\alpha_j,
 \qquad v=\sum_{j=0}^{N-1}\alpha_j.                 \tag{2.1}
\]

The corresponding physical upper table is

\[
 T_{j+tN}=\rho^{s_j+tv}U_j,
 \qquad j\in\mathbb Z_N,\quad t\in\mathbb Z_k.     \tag{2.2}
\]

Assume first that `v` is a unit.  At distinct quotient incidences `p`, replace
the baseline parallel label by another label.  Let its signed oriented voltage
change be `delta_p`, and let `x_p` record whether that replacement is used.
With an origin fixed at quotient column zero, define

\[
 D_0(x)=0,\qquad
 D_j(x)=\sum_{p\in[0,j)}x_p\delta_p,
 \qquad
 \Delta(x)=\sum_p x_p\delta_p.                     \tag{2.3}
\]

Extend `D` by

\[
 D_{j+N}=D_j+\Delta.                                 \tag{2.4}
\]

### Theorem 2.1 (multi-switch voltage and affine shear)

For every terminal label assignment, the phase prefixes and voltage are
exactly

\[
 s'_j=s_j+D_j,\qquad v'=v+\Delta.                    \tag{2.5}
\]

If the terminal voltage `v'=v+Delta` is also a unit and

\[
 h_j(t)={\bf1}_{\{0\in\rho^{s_j+tv}U_j\}},
\]

then the terminal physical coordinate-zero trace satisfies

\[
 \boxed{
 h'_j(t)=h_j\left(at+b_j\right),\qquad
 a=(v+\Delta)v^{-1},\quad b_j=D_jv^{-1}
 }                                                     \tag{2.6}
\]

in `Z_k`.  For arbitrary `v'`, the lift has `gcd(v',k)` components.  It is one
physical Hamilton cycle if and only if

\[
 \gcd(v+\Delta,k)=1.                                  \tag{2.7}
\]

#### Proof

Only the selected edge labels change.  Before column `j`, their accumulated
change is `D_j`, and over a full quotient lap it is `Delta`; this proves
(2.5).  When `v'` is a unit, consequently

\[
 T'_{j+tN}=\rho^{s_j+D_j+t(v+\Delta)}U_j.             \tag{2.8}
\]

On the other hand,

\[
 h_j(at+b_j)
 ={\mathbf1}_{\{0\in
   \rho^{s_j+(at+b_j)v}U_j\}}.
\]

The exponent after `s_j` is

\[
 (at+b_j)v=t(v+\Delta)+D_j,
\]

which proves (2.6).  The unlabelled quotient order is unchanged.  Its lift
has `gcd(v',k)` components, so it is one cycle exactly under (2.7).  \(\square\)

If `v'` is not a unit, formula (2.8) with `t in Z_k` is still an exact
`k`-lap parametrization of one lifted walk, but it repeats a component and
omits other sheet cosets.  It must not be called the full physical owner
table or trace.

### Corollary 2.2 (composition and commutativity)

For disjoint menus, the `D` and `Delta` currents add.  Thus the terminal
labelled factor is independent of switch order.  More explicitly, if packet
one has `(D_1,Delta_1)` and packet two has `(D_2,Delta_2)`, their sequential
affine factors are

\[
 a_1={v+\Delta_1\over v},\quad b_{1,j}={D_{1,j}\over v},
\]

and

\[
 a_2={v+\Delta_1+\Delta_2\over v+\Delta_1},\quad
 b_{2,j}={D_{2,j}\over v+\Delta_1}.
\]

Hence

\[
 a_1a_2={v+\Delta_1+\Delta_2\over v},
 \qquad
 a_1b_{2,j}+b_{1,j}={D_{1,j}+D_{2,j}\over v}.        \tag{2.9}
\]

Reversing the packets gives the same terminal shear.  The apparent
noncommutativity of arbitrary affine maps comes from changing normalization
between steps, not from the physical label switches.

The displayed **sequentially normalized** formulas require
`v+Delta_1` to be a unit; the reverse-order display similarly requires
`v+Delta_2` to be a unit.  Raw label substitution and addition of `D,Delta`
remain valid even when an intermediate lift is disconnected.  The direct
baseline-to-terminal physical formula (2.6) remains valid whenever the
**terminal** voltage is a unit, regardless of disconnected intermediates.
Thus terminal commutativity does not
assert that every chosen sequential route stays inside physical Hamilton
cycles.

Within one parallel bundle, labels form a pair-groupoid:

\[
 \delta(e,g)=\delta(e,f)+\delta(f,g),\qquad
 \delta(f,e)=-\delta(e,f).                            \tag{2.10}
\]

Two alternatives in one bundle are therefore a one-hot menu, not independent
bits.  At `k=15` every exposed resident menu is binary.

## 3. Exact fixed-depth signatures and residence range

Put

\[
 P_j=\rho^{s_j}U_j,
 \qquad P_{j+N}=\rho^vP_j.
\]

For a `q`-edge window starting at `j`, remove the irrelevant common rotation
`rho^{D_j}`.  Its exact terminal lower and upper targets are

\[
 I_{j,q}(x)=
 \bigcap_{h=0}^{q}
 \rho^{D_{j+h}-D_j}P_{j+h},                           \tag{3.1}
\]

and

\[
 O_{j,q}(x)=
 \bigcup_{h=0}^{q}
 \rho^{D_{j+h}-D_j}P_{j+h}.                           \tag{3.2}
\]

### Theorem 3.1 (chronological locality)

At fixed depth `q`, a quotient-window term changes only if its `q` consecutive
seams contain a switched seam.  Therefore `s` switches affect at most `qs`
quotient-window occurrences, before overlaps are removed.  A mixed Möbius
interaction among switches vanishes unless all participating seams occur in
one `q`-edge window.  In particular, switches at cyclic separation at least
`q` have additive depth-`q` signed load signatures.

#### Proof

If no switch lies among the seams from `j` through `j+q-1`, then

\[
 D_{j+h}-D_j=0\quad(0\le h\le q),
\]

so (3.1)--(3.2) equal their baseline values.  A fixed seam belongs to exactly
`q` cyclic `q`-edge windows.  The mixed-derivative statement follows because
a term depending on none of one selected variable has zero discrete
derivative in that variable.  \(\square\)

At upper depth one, a parallel replacement

\[
 (L,a,b)\longrightarrow(L,a',b),
 \qquad [L+a]=[L+a'],                                  \tag{3.3}
\]

has exact quotient signature

\[
 e_{[L\cup\{a',b\}]}-e_{[L\cup\{a,b\}]}.            \tag{3.4}
\]

Its lower-`q1` signature is zero.

For residence, orient every Johnson edge as

\[
 T_{i+1}=T_i-\{a_i\}+\{b_i\}.
\]

Minimum positive run length at least `d+1` is equivalent to

\[
 b_i\ne a_{i+t}\qquad(1\le t\le d)                  \tag{3.5}
\]

at every cyclic index `i`.  Thus residence clauses have chronological range
`d`.  Individually residence-safe parallel switches whose quotient seams are
more than `d` apart compose safely; overlapping residence collars require a
joint check.  Cyclic wrap collars are included.

There is no bounded-collar theorem for unrestricted upper intervals.  The
affine shear rethreads long quotient-lap blocks, creating globally different
suffix-prefix unions.  They must be audited on the terminal physical order.

### Theorem 3.2 (exact upper native-rank potential)

For any cyclic Johnson component `T` and `q>=1`, put

\[
 E_q^+(T)=\sum_i\left((r+q)-
       \left|\bigcup_{h=0}^{q}T_{i+h}\right|\right).  \tag{3.6}
\]

If `R_x^-(s)` is the number of cyclic zero-runs of coordinate `x` having
length `s`, then for `q` no larger than the component length,

\[
 E_q^+(T)=\sum_x\sum_s(q-s)^+R_x^-(s).               \tag{3.7}
\]

For `q` exceeding a component length, (3.6) remains the definition and exact
direct count, but (3.7) needs a winding correction and is not asserted here.
For a multifactor, sum (3.6) over its physical cyclic components.  For a
unit-voltage strict spiral all coordinate traces are translates of one scalar
trace `c`; in the range `q<=W` relevant here,

\[
 E_q^+=k\sum_s(q-s)^+R_c^-(s).                       \tag{3.8}
\]

This is an exact capacity deficit before target collisions are considered.
The overlay enumerator computes the physical vector

\[
 (E_1^+,\ldots,E_{k-r}^+)
\]

directly for every state, and uses its sum as a cheap lexicographic potential
only after exact middle/lower ownership, physical connectivity, residence,
and the declared lower-`q2` constraints.  Exact upper support is still audited
on every residence-clean Hamilton state with nonworsening lower-`q2` hole
count; the potential never replaces that audit.

For the resident factor the depth-one-through-seven vector is

\[
 (0,1065,2940,5325,8205,11610,15450),                \tag{3.9}
\]

of total `44595`.  Selector 175 changes it by

\[
 (0,-15,-30,-45,-45,-30,-15),                       \tag{3.10}
\]

so its total becomes `44415`, an exact improvement of 180 physical units.

## 4. Collision algebra

For any fixed shadow family and rotation orbit `[Y]`, let
`ell_[Y]` be the common load of each physical target in that orbit, and put

\[
 C_{\rm orb}(\ell)=\sum_{[Y]}\binom{\ell_{[Y]}}{2}.   \tag{4.1}
\]

If a switch portfolio has signed per-target load vector `sigma`, then

\[
 C_{\rm orb}(\ell+\sigma)-C_{\rm orb}(\ell)
 =\langle\ell,\sigma\rangle
  +{1\over2}\left(\|\sigma\|_2^2-
                  \sum_{[Y]}\sigma_{[Y]}\right).
                                                               \tag{4.2}
\]

For literal physical counts, give `[Y]` weight

\[
 w_Y=|[Y]|.
\]

Every fixed-window signature conserves **weighted** mass after including a
cemetery coordinate for invalid ranks.  On the valid targets alone, write

\[
 M(\sigma)=\sum_{[Y]}w_Y\sigma_{[Y]}.                 \tag{4.3}
\]

The exact physical collision is

\[
 C_{\rm phys}(\ell)
 =\sum_{[Y]}w_Y\binom{\ell_{[Y]}}2,                  \tag{4.4}
\]

and therefore

\[
 \Delta C_{\rm phys}
 =\langle\ell,\sigma\rangle_w
  +{1\over2}\left(\|\sigma\|_{2,w}^2-M(\sigma)\right).
                                                               \tag{4.5}
\]

This always-valid formula simplifies to

\[
 \Delta C_{\rm phys}
 =\langle\ell,\sigma\rangle_w
  +{1\over2}\|\sigma\|_{2,w}^2                      \tag{4.6}
\]

when valid-rank occurrence mass is itself conserved.  That hypothesis holds
for upper `q1` and for the residence-clean lower windows used in the neutral
portfolio.  Merely adding a cemetery state would instead define an augmented
collision energy; it does not justify (4.6) for the literal valid-target
energy when valid mass changes.

For additive signatures `sigma=sum sigma_i`, this gives

\[
 \Delta C_{\rm phys}
 =\sum_i\Delta C_{{\rm phys},i}
  +\sum_{i<j}\langle\sigma_i,\sigma_j\rangle_w.      \tag{4.7}
\]

Thus chronological separation removes local mixed shadow terms but does not
remove global same-colour Gram interference.

Three notions must remain distinct:

* **support-neutral:** `1_(ell+sigma>0)=1_(ell>0)`;
* **collision-neutral:** the specified `C_orb` or `C_phys` is unchanged; and
* **load-neutral:** `sigma=0`.

Neither of the first two implies the third.

This matters outside the two central levels: at `k=15`, ranks six, five, and
nine can have short rotation orbits.  The finite portfolio audit therefore
records both unweighted orbit collision and the weighted physical collision,
and calls a terminal lower-`q2` collision-neutral only when both deltas vanish.

For unrestricted upper intervals of one spanning physical Hamilton cycle,
count only strict prefix-union increments.
Every start contributes exactly `k-r` increments before reaching the full
set, so total increment mass is fixed.  These increments have exactly the
same support as all nontrivial contiguous upper unions.  Therefore upper
hole minimization is equivalent, up to a fixed additive constant, to
minimizing

\[
 E_{\rm upper}=\sum_U(\mu_U-1)_+.                     \tag{4.8}
\]

Here `U` ranges over literal physical targets.  Orbit-level hole scoring is
obtained only after grouping by rotation and applying the corresponding
short-orbit weights.

This identity does not make the loads local; it only gives an exact global
objective.

## 5. Alternating overlay cubes

Let `F` and `G` be spanning quotient 2-factors in the labelled multigraph.
Cancel common labelled edges.  Colour `F minus G` red and `G minus F` blue.
At every upper and lower quotient vertex,

\[
 d_R(v)=d_B(v),                                       \tag{5.1}
\]

because both factors have degree two.

Choose at every vertex a bijection between its red and blue incidences.
Following these paired incidences decomposes the exclusive edges into
edge-disjoint closed alternating circuits

\[
 C_1,\ldots,C_c.                                      \tag{5.2}
\]

### Theorem 5.1 (paired-circuit Boolean cube)

For every `x in {0,1}^c`, define

\[
 F(x)=F\mathbin\triangle
      \bigtriangleup_{i:x_i=1}C_i.                   \tag{5.3}
\]

Then `F(x)` has degree two at every upper and lower quotient vertex.  The
toggles commute exactly, every state preserves the middle and lower-`q1`
owner ledgers, `F(0)=F`, and `F(1)=G`.

#### Proof

At every visit of a circuit to a quotient vertex, the chosen local pairing
contains one red and one blue incidence.  Toggling the circuit replaces one
by the other and preserves local degree.  The circuits are edge-disjoint,
even when they share a degree-four support vertex, so every subset performs
these replacements independently.  Symmetric difference of their fixed edge
sets is order-independent.  Equation (5.1) also holds on the lower shore, so
the one-owner-per-lower-necklace ledger is retained.  \(\square\)

This is a raw degree-two cube.  Connectivity, terminal orientation, voltage,
residence, and shadows must be recomputed.  A gluing toggle may reverse the
terminal traversal through retained incidences, so its voltage is not a
fixed additive charge.  The additive theorem of Section 2 applies only to
parallel substitutions on one fixed unlabelled oriented quotient cycle.
For an unoriented terminal component the intrinsic voltage datum is the pair
`{v,-v}`; the script also records one raw value from its deterministic
traversal solely for reproduction.

The decomposition also depends on the incidence pairings at vertices of
exclusive degree four.  One chosen pairing gives a sound cube; it does not
enumerate all hybrid 2-factors in `F union G`.

## 6. Independent selector-175 audit

The exact switch is

\[
 (1807,7,12)\longrightarrow(1807,11,12).              \tag{6.1}
\]

It removes the rotations of the Johnson edge `(1935,5903)` and adds the
rotations of `(3855,5903)`.  Parallelism holds because

\[
 \operatorname{canon}(1807+2^7)
 =\operatorname{canon}(1807+2^{11})=1935.             \tag{6.2}
\]

The exact physical audit is:

| gate | resident | selector 175 |
|---|---:|---:|
| quotient/physical voltage | 1 | 8 |
| middle vertices | 6,435 distinct | 6,435 distinct |
| lower `q1` colours | 6,435 distinct | 6,435 distinct |
| residence defects | 0 | 0 |
| lower `q2` holes | 47 | 47 |
| lower `q3` holes | 11 | 12 |
| all-width upper holes | 95 | 94 |

The exact quotient-load signatures, obtained by dividing physical orbit
loads by 15, are

\[
 \Delta U_1=-e_{3887}+e_{1951},
 \qquad 4\to3,\quad0\to1,                             \tag{6.3}
\]

\[
 \Delta L_2=-e_{1671}+e_{1295},
 \qquad 2\to1,\quad1\to2,                             \tag{6.4}
\]

and

\[
 \Delta L_3=e_{271}-e_{647}+e_{901}-e_{1159},
 \qquad 1\to2,\ 3\to2,\ 3\to4,\ 1\to0.             \tag{6.5}
\]

The unweighted orbit pair-collision changes are respectively

\[
 -3,\qquad0,\qquad+2.                                 \tag{6.6}
\]

All changed representatives have full orbit size 15, so the corresponding
literal physical pair-collision changes are

\[
 -45,\qquad0,\qquad+30.                               \tag{6.7}
\]

Thus selector 175:

* fills upper representative `1951` and loses no upper support;
* has the identical lower-`q2` hole set and load histogram;
* is lower-`q2` collision-neutral but not load-neutral; and
* creates lower-`q3` hole `1159`.

With the frozen deterministic quotient origin, orientation, and
representatives, the coordinate-zero trace shear is uniquely

\[
 h'_j(t)=h_j(8t+b_j),\qquad b=0^{381}7^{48}.           \tag{6.8}
\]

Its trace Hamming distance is 3,092; 406 run starts and 406 run ends are
replaced.  Residence validity is preserved, not the run-length profile.

Finally, the switch's quotient symmetric difference consists of two parallel
labelled incidences, hence is a digon.  If two parallel perfect matchings on
one `k`-fibre differ by voltage `delta`, their union has

\[
 g=\gcd(k,\delta)
\]

alternating components, each of length `2k/g`.  Here `k=15`, `delta=7`, so
the lift is one alternating 30-cycle.  It is not an MMM gluing `C6`.

## 7. Complete baseline-enabled resident-local published switch census

The independent MMM extractor lists 131 labelled gluing pairs at `m=7`.
Exactly two of their six-edge circuits alternate immediately against `F_res`.

The first is label 19:

```text
x = 11011100001010
y = 10111100001010
old = (1893,14), (1957,6), (3659,8)
new = (1893,7),  (1957,14), (3659,7)
```

Its physical lift has three cycles of upper lengths

```text
2145, 2145, 2145
```

and 60 residence defects.  It retains 47 lower-`q2` holes, 11 lower-`q3`
holes, and 95 upper holes when intervals are confined to its components.

The second is label 129:

```text
x = 11001010101100
y = 10101010101100
old = (3411,3), (3413,1), (3417,2)
new = (3411,2), (3413,3), (3417,1)
```

Its physical upper-cycle lengths are

```text
1760, 1760, 1760, 1155
```

and it has 60 residence defects, 48 lower-`q2` holes, 11 lower-`q3` holes,
and 94 componentwise upper holes.

The resident factor also exposes precisely five binary parallel menus at
selector indices

```text
0, 175, 316, 380, 384.
```

The two `C6` circuits and five digons are edge-disjoint.  Their fixed circuit
sets therefore commute under symmetric difference.  Complete enumeration of
the resulting `2^7=128` states gives:

* 128 quotient degree-two factors;
* 54 one-cycle physical lifts; and
* exactly two one-cycle, residence-clean, lower-`q2`-support-neutral states.

Those two states are the baseline and selector 175 alone.  The latter has bit
signature

```text
atom order: G19,G129,P0,P175,P316,P380,P384
bits:       0001000
```

and is the unique nontrivial optimum in this exact baseline-enabled
resident-local published portfolio.  It is not all-depth neutral because of
(6.5).  This census does not exclude a published `C6` which becomes
alternating only after some other, non-baseline toggle.

## 8. Resident versus global MMM overlay census

For the frozen published shift-one MMM factor, the expanded labelled factors
share 235 of 858 inclusion-edge orbits.  Their exclusive support contains
623 red and 623 blue edges and is one ordinary connected component on 825
vertices:

\[
 412\text{ lower},\qquad413\text{ upper}.             \tag{8.1}
\]

Its total exclusive-degree histogram is

\[
 2^{404}4^{421}.                                       \tag{8.2}
\]

Lexicographic red/blue incidence pairing gives ten alternating circuits of
lengths

\[
 468,374,190,116,42,34,6,6,6,4.                       \tag{8.3}
\]

Thus ordinary connectedness does not make the overlay indivisible; the
chosen paired decomposition gives a 1,024-state raw cube.

For the all-first potential-decreasing arborescence and all 33 one-option
changes, all 34 resident overlays again have one ordinary connected support.
Their common-edge counts range from 140 to 148.  The lexicographic circuit
dimensions have histogram

\[
 6^2,\quad7^6,\quad8^{16},\quad9^9,\quad10^1.          \tag{8.4}
\]

Consequently these 34 cubes contain

\[
 2(2^6)+6(2^7)+16(2^8)+9(2^9)+2^{10}=10624            \tag{8.5}
\]

raw states.  Including (8.3) gives exactly 11,648 raw terminal states before
deduplication.

The search artifact additionally includes selector 175 as an explicit
one-digon, two-state calibration.  Thus a full artifact run has 36 endpoint
occurrences and 11,650 raw states, while the actual 35 MMM-overlay endpoints
still contribute exactly 11,648.  The calibration's two factors duplicate
the resident and selector states already audited in Section 7; its role is to
verify the common lift, collision, upper-support, and rank-deficit code.

The exact neutral slice is defined statewise by all of:

1. one physical Hamilton cycle (hence unit component voltage);
2. zero physical residence defects;
3. the exact resident lower-`q2` missing set;
4. zero change in unweighted orbit lower-`q2` collision; and
5. zero change in short-orbit-weighted physical lower-`q2` collision.

Within that slice, the primary lexicographic score is

\[
 \left(\sum_{q=1}^{7}E_q^+,
       H_{\rm upper},
       H^-_3,
       C^-_{3,\rm phys}\right).                       \tag{8.6}
\]

Separately, to avoid hiding a nonneutral `q2`/upper trade, the script performs
the exact all-width upper audit on every one-cycle, residence-clean state with
at most 47 lower-`q2` hole orbits.  It records exact gained/lost `q2` and upper
supports and the Pareto frontier in

\[
 (H^-_2,\ \sum_qE_q^+,\ H_{\rm upper}).              \tag{8.7}
\]

This broader table is diagnostic only; it does not weaken the neutral-slice
requirements.

### 8.1 Exact terminal enumeration

The full 36-endpoint artifact completed without truncation.  Its exact census
is

```text
endpoint occurrences                         36
raw paired-cube states                    11,650
distinct labelled quotient factors         9,264
collision-neutral state occurrences            37
distinct collision-neutral factors              2
distinct upper-audit-eligible factors            2
```

The 37 neutral occurrences consist of 36 copies of the resident factor (the
zero state in every endpoint cube) and one copy of selector 175.  Hence the
two distinct neutral factors are exactly

| factor | factor SHA-256 | score `(sum E_q^+,H_upper,H^-_3,C^-_{3,phys})` |
|---|---|---|
| resident | `2bcf875a3e02195aac886a6ea2fdfec137afd404ee394b17be8f185e4fa05175` | `(44595,95,11,5655)` |
| selector 175 | `77bedcc2f9be611935de13539bc670b86947f0b7fbfdc1869156a01ef3081b24` | `(44415,94,12,5685)` |

Thus selector 175 is the unique lexicographic optimum in the exact neutral
slice.  It is also the unique nonresident neutral factor and the unique
Pareto factor for (8.7), with vector

\[
 (H^-_2,\sum_qE_q^+,H_{\rm upper})=(47,44415,94).
\]

Its terminal checks reproduce the independent local audit: one physical
cycle of length 6,435, intrinsic voltage pair `{7,8}`, zero residence
defects, the exact resident lower-`q2` missing set and zero lower-`q2`
orbit/physical collision change, upper support gain `{1951}` with no loss,
and deficit change

\[
 (0,-15,-30,-45,-45,-30,-15).
\]

The price is exact: the lower-`q3` missing count is `12`, target `1159` is
lost, and the lower-`q3` orbit/physical collision changes are `+2/+30`.
Accordingly the portfolio contains no collision-neutral upper improvement
whose lower-`q3` missing count and physical collision are both nonworsening.
It also contains no state at all with zero lower-`q2` holes and no eligible
state with zero upper holes.

This portfolio is complete for the displayed lexicographic pairings, not for
all red/blue pairings and not for alternating circuits using edges outside
the selected resident--MMM overlays.

## 9. Audit artifacts and reproducibility

The lightweight resident-local audit is

```text
scratch/audit_k15_mmm_resident_switch_portfolio_20260729.py
scratch/k15_mmm_resident_switch_portfolio_20260729.audit.json
```

It freezes the sparse upper-`q1`, lower-`q2`, and lower-`q3` signed load
vectors, short-orbit-aware physical and orbit collision deltas, and exact
all-width support gains/losses for every baseline-enabled atom.  Their
SHA-256 hashes are

```text
script
c838d4998f06a6d1fdda104d753ff63113bde2b7b4c980c2d7f127b552a40b7c

audit JSON
5af9de5d374e4d9cd6983f1925ba8a96568787a43ecc270efbd9f37fee95fd25
```

The bounded global overlay enumerator is

```text
scratch/search_k15_mmm_overlay_circuit_cube_20260729.py
```

Post-audit script SHA-256:

```text
65b311f1e3c3b5629164ceddce000ec533955c34dd527c569862ff4537a5f529
```

Its complete output is

```text
scratch/k15_mmm_overlay_circuit_cube_20260729.audit.json
```

with byte size `39,001,956` and SHA-256

```text
1d780b778bac390f01a1764696de34042641e651102fbcaa6bdf56fd76f0a731
```

It lifts arbitrary quotient factors directly in the bipartite graph, so
hybrid lower vertices that contract to a Johnson self-loop are not silently
discarded.  Every terminal is checked for quotient degree two, physical
component structure and component voltage, unique middle ownership,
lower-`q1` ownership, physical residence, lower `q2/q3` support and both
orbit/physical collision, and the exact upper native-rank deficit vector.
All-width upper support is checked for every residence-clean Hamilton state
whose lower-`q2` hole count is nonworsening; the exact collision-neutral slice
is retained separately.

Frozen input hashes:

```text
pipeline
a364a0e48e1f35dc9610436adf3e841f16290b883f12308de04dfce728fa8fda

MMM extractor
f54d3840221857e02be4c82574704ee3e4a4884ae213c0728c30ba8010fafe67

resident fixture
4482c3d448b3e314f89cc0c6e3f04a950e12a9e97ceb680da0478a00f2f4ee10

frozen published shift-one payload
0f42e4ba0ac0ec63e7f5edc8f1c3966208080b0fa58ebf7ea9552f84865a4e19
```

Selector-175 physical cycle hashes are

```text
resident
b6c231aa269791db4a5457f5dc32d25f0017495418d17984236357ae6f9e0bda

switched
bd7405a3f641ca2701fcbf9bcba1270aa83422f6db03f45313c169dad2cb7356
```

One provenance caveat is exact: rerunning the earlier selector script emits
a detailed JSON whose byte hash differs from the manually condensed frozen
summary JSON.  All overlapping mathematical quantities agree.  The new
resident-local artifact above is generated directly by its named script.  The
overlay script and full output hashes above were independently recomputed
after copying the completed remote artifact.  Re-parsing all endpoint states
reproduces 11,650 occurrences, 9,264 distinct factor hashes, 37 neutral
occurrences, two distinct neutral hashes, the circuit-count histogram (8.4),
and the lexicographic key `(44415,94,12,5685)`.

## 10. Sharp remaining boundary

This note proves the algebra needed to compose the published parallel and
alternating moves, and it closes the immediately available resident-local
published cube.  It does not prove any of the following:

1. that every useful alternating circuit occurs in one resident--MMM overlay;
2. that the lexicographic pairing is optimal among the exponentially many
   pairings at degree-four overlay vertices;
3. that a collision-neutral upper improvement can also avoid the lower-`q3`
   debt;
4. that a terminal factor has complete lower `q2` or complete upper support;
5. that any quotient carrier has a compatible cut, exact common compiler, or
   literal contiguous-OR word.

The next exact mathematical object is the pairing-dependent interference
hypergraph of Section 5: identify a different pairing, or a circuit using an
edge outside the 35 MMM overlays (plus the selector calibration), whose
terminal is unit-voltage, residence-clean, lower-`q2` collision-neutral,
upper-support improving, and lower-`q3` nonworsening.  No conclusion about
the full alternating-circuit space follows from failure of one finite paired
portfolio.
