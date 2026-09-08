# K17 complement-dual age-local `D` switches: exact collars and the minimal residence-improving `C6`

Date: 2026-08-01  
Lane: A  
Status: exact local theorem, complete support-`1,2,3` catalogue on the
authenticated factor, and independently replayed positive switch.  The
result improves the raw flat depth-three residence ledger; it does not
supply an occurrence-age decoration, deeper shadows, or a compiler.

## 1. Outcome

Let `C` be complementation between the quotient rank-eight and rank-nine
shores, let `D` be an incidence perfect matching, and put

\[
                       A=CD,\qquad H=CD^{-1}C,
                       \qquad B=H^{-1}D=A^2.          \tag{1.1}
\]

The authenticated input is

```text
/dev/shm/root_k17_complement_dual_deep17931_20260801/best.tsv
SHA256 a3f9eac037ae66a460349b12d578a31222afe1a7d168da641e77967a44ddbab3
```

It replays as a palette-complete complement-dual factor with

\[
              A\text{-cycle lengths }[1429,1],
              \qquad c(B)=2,
              \qquad c(B_{\rm physical})=2.          \tag{1.2}
\]

Its two physical owner cycles have lengths `24293` and `17`.  The long
cycle has positive-run histogram below four

\[
                         2^{1190}3^{3128};             \tag{1.3}
\]

the 17-cycle is residence-clean.  Thus the raw flat depth-three ledger is

\[
 R_{<4}=4318,qquad
 \mathcal D=\sum_{L<4}(4-L)=5508.                    \tag{1.4}
\]

The complete alternating-`D` circuit catalogue on one, two, and three
selected rows has the following exact counts.

| changed `D` rows | raw circuits | dual-collision-free | both palettes complete | two physical components | residence-improving |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 | 0 |
| 2 | 19 | 18 | 3 | 0 | 0 |
| 3 | 627 | 389 | 11 | 2 | 4 |

The sole one-row move merely interchanges the complementary selected
incidences `3825` and `3829` at owner `425`; the unoriented factor support
is unchanged.  It is therefore support-inert.

There is exactly one two-component-preserving, palette-safe `C6` which
also improves residence without changing the `[1429,1]` component profile:

```text
owner 75:   edge  681 ->  678     facet 163 -> 194
owner 265:  edge 2385 -> 2391     facet 194 -> 449
owner 219:  edge 1975 -> 1971     facet 449 -> 163
```

It changes the run ledger to

\[
            2^{1156}3^{3145},\qquad
            R_{<4}=4301,qquad \mathcal D=5457.       \tag{1.5}
\]

Hence it removes 17 physical short runs, comprising one `Z_17` orbit, and
lowers deficit by 51:

\[
                         \Delta R_{<4}=-17,
                         \qquad \Delta\mathcal D=-51. \tag{1.6}
\]

This proves a sharp scoped statement: among all complement-dual
alternating `D` circuits changing at most three selected rows, support
three is the minimum for simultaneously preserving both immediate
palettes, preserving the two-physical-component profile, and strictly
improving the raw flat residence ledger.

The natural `C6` through the singleton owner does **not** pass.  There is
exactly one such circuit.  It changes tails `(230,430,425)` to incidence
edges `(2074,3874,3832)`, replaces `[1429,1]` by `[1167,263]`, and retains
two physical components, but it loses the three rank-ten orbits

\[
                         0x1e6f,\qquad0x1f1f,
                         \qquad0x3d37,                \tag{1.7}
\]

with the complementary three rank-seven losses.  It also worsens

\[
                    R_{<4}:4318\longrightarrow4352,
                    \qquad
                    \mathcal D:5508\longrightarrow5559.          \tag{1.8}
\]

Thus the support-three singleton-removal shell is exactly closed on this
factor.  It is not a global obstruction to a longer `D` circuit.

The next two paired-dual singleton shells are also exact:

| shell | raw circuits | dual-collision-free | `A` Hamilton | palette-safe `A` Hamilton |
|---:|---:|---:|---:|---:|
| `C8` (four `D` rows) | 9 | 5 | 3 | 0 |
| `C10` (five `D` rows) | 41 | 19 | 0 | 0 |

All three Hamilton `C8` candidates have two physical parity components,
but the best still misses five rank-ten targets.  `C10` cannot Hamiltonize
`A` by parity.  Thus no strict paired-dual singleton circuit through
`C10` reaches the palette-complete `[715,715]` target.

The independently authenticated longer catalogue first reaches the target
at `C12` up to one complementary palette hole: candidate 72 has Hamilton
`A`, quotient factor lengths `[715,715]`, upper hole `0x03e4f`, and lower
hole `0x00d87`.  Its exact second-repair interface is recorded in
`MATH_THEOREM_A_K17_CANDIDATE1911_SECOND_CIRCUIT_AGE_SERVICE_GATE_20260801.md`.

## 2. Exact palette and chronology collars

Let `X={x_1,...,x_t}` be the tails of an alternating assignment circuit.
After cyclic indexing, the old and new `A` arcs are

\[
 x_i\longmapsto A(x_i)
       \quad\rightsquigarrow\quad
 x_i\longmapsto A(x_{i+1}).                         \tag{2.1}
\]

Equivalently `A'=A sigma`, where `sigma=(x_1 ... x_t)` on `X` and fixes
the other owners.  Every displayed new incidence must exist with its
chosen phase, the selected `D` edges must still be a perfect matching, and
no selected edge may meet the complement of another selected edge.

Define two collars

\[
                    P=X\cup A(X),
                    \qquad Q=X\cup A^{-1}(X).        \tag{2.2}
\]

### Theorem 2.1 (two-collar locality)

1. Only turn colours centered in `P` can change.
2. `B'=A'^2` differs from `B=A^2` only on successor tails in `Q`.
3. `B'(Q)=B(Q)` as sets.

#### Proof

An outgoing `A` arc changes only at a tail in `X`.  An incoming arc changes
only at one of the permuted old heads `A(X)`.  Since a turn uses one
incoming and one outgoing arc, its centre lies in `P`.

For `z` outside `X union A^{-1}(X)`, both `A'(z)=A(z)` and
`A'(A'(z))=A(A(z))`, proving the second statement.  Both `B` and `B'` are
permutations and agree off `Q`, so their images of the complementary set
agree; hence their images of `Q` agree as well.  \(\square\)

Let `mu_T` be the old rank-ten occurrence load, and let `loss_T(P)` and
`gain_T(P)` be the old and new occurrences among the changed centres.

### Corollary 2.2 (exact immediate-palette test)

The switched complement-dual factor preserves both immediate palettes if
and only if

\[
              \mu_T-\operatorname{loss}_T(P)
                    +\operatorname{gain}_T(P)\ge1
                    \qquad\text{for every rank-ten }T.             \tag{2.3}
\]

#### Proof

Theorem 2.1 lists every changed rank-ten occurrence.  Complement duality
continues to hold after a `D` switch, so the rank-seven load vector is the
complement of the rank-ten load vector with the same multiplicities.
Thus (2.3) is necessary and sufficient for both shores.  \(\square\)

For the authenticated input the common load histogram is

\[
                         1^{878}2^{247}3^{18}4^1.    \tag{2.4}
\]

The positive `C6` changes ten quotient loads on each shore, all of which
remain positive, and leaves (2.4) unchanged.

## 3. Local topology and voltage

Cut the old `A` arcs at the tails in `X`.  For every cut head
`y in A(X)`, follow the unchanged old `A` fragment until the next cut tail;
call that tail `r(y)`.  Let `g:X->A(X)` be the new head assignment in
(2.1).

### Theorem 3.1 (fragment permutation)

The new `A` components which meet the switch are exactly the cycles of

\[
                              r\circ g:X\longrightarrow X.        \tag{3.1}
\]

Their voltages are obtained by summing the precomputed fragment voltages
and the corresponding new arc voltages around those cycles.

#### Proof

Starting at a cut tail, first take its new arc to the cut head `g(x)` and
then traverse the unchanged fragment to `r(g(x))`.  These are precisely
the transitions of (3.1).  Every changed component alternates such a new
arc with one unchanged fragment, and no other component is touched.  The
voltage statement follows by additivity.  \(\square\)

This is an `O(t)` topology and voltage replay after fragment preprocessing;
it does not require reconstructing all 1,430 quotient owners.

There is a useful parity consequence for the singleton shell.  A `t`-row
circuit changes the sign of `A` by `(-1)^(t-1)`.  Starting from two
`A`-cycles, a `C6` (`t=3`) cannot make `A` Hamilton.  It can, however,
replace `[1429,1]` by two nontrivial odd cycles while keeping `c(A^2)=2`,
as the unique singleton `C6` does in (1.7).  An `A`-Hamiltonizing circuit
after the absent singleton `C4` must have at least four rows (`C8`).

## 4. Exact occurrence-age lift of a local circuit

An occurrence-age state at an owner `u` is

\[
 S_u=(T_u;C_{u,0},C_{u,1},C_{u,2},C_{u,3}),
                         \qquad C_{u,3}=\{\alpha_u\}.              \tag{4.1}
\]

For a phase-labelled Johnson transition `u->v`, let
`R_{uv}^delta(S_u,S_v)=1` precisely when

\[
\begin{aligned}
 T_u-T_v&=C_{u,3},\\
 C_{v,j+1}&\subseteq C_{u,j}\quad(0\le j\le2),\\
 C_{v,0}&=\{\beta\}\mathbin{\dot\cup}
          \bigcup_{j=0}^{2}(C_{u,j}-C_{v,j+1}),
             \qquad \{\beta\}=T_v-T_u .                         \tag{4.2}
\end{aligned}

This is the literal survivor/refresh relation.  It is stronger than a
run-length test.

### Theorem 4.1 (exact local age test)

For a fixed cyclic-equivariant state assignment, only the phase-labelled
`B` seams with tails in `Q` from (2.2) need to be rescored.  The switch is
compatible with the fixed assignment if and only if every new seam has
`R=1`.

For variable states, cut the old factor at `Q`.  Let each unchanged
fragment carry the Boolean transfer matrix obtained by multiplying its
relations `R`.  The switched factor admits an age decoration if and only
if every new component has nonzero Boolean trace of the cyclic product of
its fragment matrices and new-seam matrices.

Tropical products give the exact minimum number of illegal transitions.
Replacing Boolean entries by monomials in the nine age types gives an
exact coefficient test for the prescribed global type multiplicities.

#### Proof

By Theorem 2.1 every old `B` transition outside `Q` is unchanged.  For
fixed states, (4.2) is necessary and sufficient on each new seam.  For
variable states, matrix multiplication existentially sums over the common
state at every internal endpoint, while the trace identifies the initial
and final state on a component.  The tropical and graded versions are the
same finite-state path composition over different semirings.  \(\square\)

The input `best.tsv` contains only

```text
owner  pick_edge  dual_edge  facet
```

and no occurrence-age states.  Therefore the positive switch in Section 1
cannot yet be called age-compatible in the sense of (4.2).  It is a proved
raw-residence improvement and supplies a six-tail transfer-matrix collar
for the next exact state calculation.

## 5. Why the positive-run ledger is exact

Let `(T_i)` be any cyclic Johnson owner component.  For a coordinate `z`,
its **positive runs** are the cyclic runs of indices for which `z in T_i`.

### Theorem 5.1 (flat depth-three residence criterion)

There exist nonempty source cells `(S_i)` such that

\[
                         T_i=S_{i-3}\cup S_{i-2}
                                  \cup S_{i-1}\cup S_i            \tag{5.1}
\]

for every `i` if and only if every positive coordinate run in `(T_i)` has
length at least four.

#### Proof

If (5.1) holds, every occurrence of `z` in one source cell makes `z`
present in four consecutive owners.  Overlapping such intervals may merge,
but no positive owner run can have length below four.

Conversely suppose every positive run has length at least four and put

\[
                         S_i=T_i\cap T_{i+1}
                                  \cap T_{i+2}\cap T_{i+3}.        \tag{5.2}
\]

For a binary cyclic trace, dilation of the four-step erosion (5.2)
recovers the trace exactly when every positive run has length at least
four.  Hence (5.1) follows coordinatewise.  At the Johnson step into
`T_i`, the unique entering coordinate begins a run of length at least four
and therefore belongs to `S_i`; so every `S_i` is nonempty.  \(\square\)

Thus `R_<4` is the exact count of flat-residence obstructions, while
`mathcal D` in (1.4) is a useful severity potential.  This criterion does
not impose the exact age-type multiplicities or lower common-cap matching.
Zero-run counts are diagnostic only and are not required by Theorem 5.1.

## 6. Complete finite audit

The exact O3 catalogue is

```text
scratch/threadA_k17_complement_dual_age_local_repair_20260801/
  catalogue_k17_complement_dual_age_local_dswitches_20260801.cpp
  SHA256 9eebcdeb51c3cec2e761cd71e19fe817e5ded0626a0c3a1840832ceac5fc826d

  dswitch_catalogue.audit.json
  SHA256 99f0b06c31f949005430be4e7cf8732d4aefefe929a56a4df7ca26bda3e953ca

  dswitch_catalogue.tsv
  SHA256 a768dce9ef218e3ae5dd448de4ed0d3cc84cbda5983fa633d240361aecbbb16f

  best_age_improving_dswitch.tsv
  SHA256 bff9739f830fff21ab48201d4193f5b1eb805da9b2553caa914a4b83d25661d8
```

The source enumerates every parallel one-row substitution and every
connected directed alternating assignment circuit on two or three distinct
rows.  It additionally enumerates the complete singleton-rooted four- and
five-row shells.  Each candidate is then replayed from the named incidence
matching, with fail-closed tests for perfectness, dual collision, both
immediate palettes, `A` and `A^2` topology, physical phase lift, and every
positive coordinate run.  Since there is only one parallel one-row
substitution, the support-below-three minimality statement is also valid
for a disconnected matching change.

An independent implementation replays the base and the positive switch:

```text
scratch/threadA_k17_complement_dual_age_local_replay_20260801/
  independent.audit.json
  SHA256 a9575f196bd68a456f0cd3c329c99b7f66e9bc3c078a4d6cfc01a1cbf1553bc8

  switch75_265_219.audit.json
  SHA256 7e180f3b5c1a5a13206916f98ce9f727d0d1085b2ece62a49aaf54f768ea4ec5
```

The independent replay also checks the four-deletion-spine diagnostic,
which improves from `5474` to `5440`.  This is consistent with, but not
identical to, the positive-run potential.

## 7. Non-dual splice boundary

The exact non-dual age filter is proved separately in

```text
MATH_THEOREM_A_K17_COMPLEMENT_DUAL_CROSS_RECTANGLE_AGE_FILTER_20260801.md
```

For the fixed `D`, all `1429` pairs consisting of one `H` edge from each
component have been checked, and none has both crossed incidences.  Thus
the fixed-`D` two-edge non-dual rectangle is geometrically impossible
before palette, voltage, or age tests.  The frozen audit is

```text
scratch/threadA_k17_complement_dual_age_local_replay_20260801/
  twofactor_splice_catalogue.audit.json
SHA256 17f1852bedb86abc176a4013d2c5823e97c120a5019e064ff0e2fda582ee7815
```

Moreover, an alternating pure-`H` circuit meeting the component profile
`[1429,1]` can join the components only when the number of changed `H`
edges is even.  Hence `C6` cannot join them; after the empty `C4` shell,
`C8` is the first topology-capable pure-`H` shell.  This does not exclude a
mixed `D/H` circuit.

## 8. Exact remaining gate

The local geometry is no longer the obstruction to raw residence
improvement: the switch in (1.5) is an exact positive atom.  The remaining
occurrence-age gate is to attach the certified age-state menus and exact
type quotas to the `Q`-fragment transfer matrices of Theorem 4.1.  A pass
would certify an age-compatible `C6`; a failure would be a scoped
six-tail state obstruction, not a no-go for larger circuits.

Even such a pass would leave thousands of residence defects, the ranks
eleven and above, the common-cap compiler, and final connected topology.
No `nu(17)=B(17)` claim is made.
