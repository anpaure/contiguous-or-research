# A compact Horn reachability encoding for the `k=17` residence master

Date: 2026-08-02

Status: exact positive-residence encoding and exact catalogue census.  It does
not encode quotient connectivity, nonzero voltage, deep upper shadows, or the
source/compiler.

## 1. Boundary states rather than insertion identities

Work on the exact facet/owner face of the marker-58 quotient catalogue.  Let
`u` be a rank-nine owner representative and let `x in u`.  There are

\[
             1430\cdot9=12870                           \tag{1.1}
\]

owner-coordinate states.

Introduce three Boolean layers:

* `B(u,x)`: a selected edge incident with `u` deletes `x`; equivalently this
  occurrence is an endpoint of the positive `x`-run;
* `R1(u,x)`: along the selected orientation, a `B` state occurs one retained
  edge before `(u,x)`;
* `R2(u,x)`: a `B` state occurs two retained edges before `(u,x)`.

Only implications into these variables are required.  They are witness
variables, not exact definitions.

For a nonloop quotient edge `e` between owner frames `u` and `v`, let its
forward dart have voltage `delta`, delete `a` in the `u` frame, and insert
`b` in the `v` frame.  Every retained coordinate

\[
 x\in u-\{a\}
\]

is represented in the target frame by

\[
                         y=x-\delta\pmod {17}.           \tag{1.2}

Let `p_e` be the primary edge variable and `d_e` one of its two directed-dart
variables.

## 2. The Horn module

### Endpoint witnesses

For both endpoints of every nonloop edge, add

\[
                         \neg p_e\vee B(u,a).            \tag{2.1}

For a protected fixed edge, (2.1) is the unit `B(u,a)`.  No reverse
implication is needed.

### Two-step propagation

For every directed dart and every one of its eight retained coordinates add

\[
 \begin{aligned}
  &\neg d_e\vee\neg B(u,x)\vee R1(v,y),\\
  &\neg d_e\vee\neg R1(u,x)\vee R2(v,y).
 \end{aligned}                                          \tag{2.2}

### Accepting rows

For every owner-coordinate state add

\[
       \neg B(u,x)\vee\neg R1(u,x),\qquad
       \neg B(u,x)\vee\neg R2(u,x).                    \tag{2.3}

Retain the existing primary/dart equivalence and the incoming/outgoing
orientation rows.  Undirected degree two then makes every selected component
a coherently directed cycle.

## 3. Exactness and propagation

### Theorem 3.1

On the exact lower-facet and owner-degree-two face, the Horn module
(2.1)--(2.3) is satisfiable for a selected oriented factor if and only if
every nonconstant positive coordinate run has length at least four.

#### Proof

A length-one positive run is already impossible: its entering and leaving
edges have the same lower facet.

Suppose a run has length two.  Its first owner is a boundary state, so (2.1)
forces `B`; the selected retained dart forces `R1` at the second boundary by
(2.2), contradicting (2.3).  For a length-three run, the two retained darts
force `R1` at the middle owner and `R2` at the final boundary, again
contradicting (2.3).

Conversely, assume every positive run has length at least four.  Set `B`
exactly at its two boundary owners.  Set `R1` at the selected successor of
each `B` state and `R2` at the next selected successor.  A run of length at
least four has neither marker on its terminal boundary, so (2.3) holds.
Constant-one component traces have no boundary state and are legal.  All
implications hold by construction. `square`

### Corollary 3.2 (unit propagation)

Once the darts of a bad directed segment are selected, unit propagation
alone derives the conflict.  More strongly, after a boundary and one or two
retained darts are selected, propagation installs `R1` or `R2`; (2.3) then
sets the possible terminal `B` false, and (2.1) prunes every boundary edge
which would close the short run.

Thus the encoding detects impossible partial **directed** turns.  It does not
unit-refute a bad segment while both coherent orientations remain unresolved:
the two directions are a genuine Boolean symmetry.  The sound primary clause
from the orientation-free segment theorem should be learned lazily when an
incumbent exposes such a segment.

## 4. Exact marker-58 size

The active catalogue has:

```text
owner orbits                 1,430
nonloop undirected rows     35,937
directed darts              71,874
retained labels per dart         8
```

Therefore the residence state has

\[
              3\cdot12870=38610                         \tag{4.1}

\]

variables, and the residence-only clause counts are

\[
\begin{array}{lr}
\text{endpoint witnesses} & 2\cdot35937=71874,\\
\text{two Horn reach layers}&2\cdot71874\cdot8=1149984,\\
\text{accepting conflicts}&2\cdot12870=25740.
\end{array}                                               \tag{4.2}

Hence

\[
                 \boxed{1247598}                         \tag{4.3}

\]

residence clauses suffice.

The existing primary/dart channel and coherent-orientation rows contribute
71,874 dart variables and 146,152 clauses.  Relative to the round-one base,
the complete replacement master therefore has

\[
\begin{array}{c|r|r}
 &\text{added variables}&\text{added clauses}\\ \hline
\text{current one-hot history}&144804&3465094\\
\text{Horn reachability v3}&110484&1393750.
\end{array}                                               \tag{4.4}

\]

Using the authenticated round-one base `(204167,439463)`, the final v3 census
would be

\[
                  \boxed{314651\text{ variables},
                          1833213\text{ clauses}}.        \tag{4.5}

\]

This saves 34,320 state variables and 2,071,344 appended clauses.  The
residence-state variables alone fall from 72,930 to 38,610.

The saving comes from two facts absent in the generic history automaton:

1. a recent insertion which has not yet been deleted must be one of the nine
   coordinates of the current owner; and
2. only reachability from a run boundary is needed, not the identity and
   exact age of all three previous insertions.

## 5. Primary propagation and the exact tradeoff

There is also a completely orientation-free version using only the endpoint
variables `B`.

For every retained undirected edge `uv` and retained coordinate `x`, add

\[
                 \neg p_{uv}\vee\neg B(u,x)\vee\neg B(v,x).  \tag{5.1}

\]

This excludes every length-two run.  For every two-edge retained path
`u-v-w`, add

\[
 \neg p_{uv}\vee\neg p_{vw}\vee\neg B(u,x)\vee\neg B(w,x).  \tag{5.2}

\]

This excludes length three.  The endpoint witnesses plus (5.1)--(5.2) are
exact and unit-refute a bad segment as soon as its **primary** edges are set,
without choosing an orientation.

The exact catalogue counts, after discarding edge pairs which already collide
in one facet row, are

```text
endpoint witness clauses              71,874
length-two retained-edge clauses      287,496
length-three centred-path clauses  12,808,054
total                              13,167,424
```

This is dramatically smaller than the 532-million minimal primary-segment
family, because `B` summarizes all possible boundary edges.  It is still
more than nine times the Horn v3 module and more than three times the current
whole directed-history suffix.  It is therefore a useful maximal-propagation
option, not the preferred default.

The practical exact architecture is:

1. use Horn v3 for compact directed propagation;
2. replay every incumbent literally; and
3. learn the at-most-four-primary orientation-free clause for each exposed
   bad segment.

This combination is complete, compact at initialization, and increasingly
strong in precisely the basins the solver actually visits.

## 6. General depth and the limit of the improvement

For residence floor `d+1`, use layers

\[
                     B,R1,\ldots,R_{d-1}.               \tag{6.1}

\]

Each selected retained dart propagates one layer.  The exact variable and
reach-clause scales are

\[
             \Theta(nrd),\qquad
             \Theta(Mr d),                              \tag{6.2}

\]

where `n` is the number of owner orbits and `M` the edge-orbit catalogue.
At central rank `r=Theta(k)` and `M=Theta(nk^2)`, the clause scale is
`Theta(ndk^3)`, the same asymptotic order as a coordinate-explicit one-hot
history transport.  The improvement is a large exact constant and the
removal of one-hot rows, not a new asymptotic exponent.

Eliminating the reach states projects the formulation back to the path
clauses of Section 5 and ultimately to the 532-million primary family.  This
is an explicit size-versus-propagation tradeoff.  No general CNF extension-
complexity lower bound is claimed.

## 7. Audit

The independent catalogue/replay source is

```text
scratch/audit_k17_orientation_free_reachability_residence_v3_20260802.cpp
SHA256 4a04309f44f1ae856ec2eeba8fc8029b9db93fe7dcf9524c97b49c35b6724490
```

It reconstructs the quotient geometry and coordinate transport, verifies the
35,945-row catalogue census, orients the authenticated floor-3,502 factor,
and obtains exactly

```text
length-two run orbits  114
length-three run orbits 92
```

matching `1938/17` and `1564/17` from the independent literal replay.  This
control verifies the Horn reach semantics; it is not a verdict on the free
v3 master.

The retained H100 audit output has SHA256
`dc05c8b0ce7e02dac30e3bbe2c5a77d8fc62869a4a880add561947f81c429d52`
under
`/home/amodo/or15/work/root_k17_orientation_free_residence_v3_20260802`.

## 8. Frozen CNF build

The fail-closed builder

```text
scratch/build_k17_compact_horn_residence_v3_20260802.cpp
```

was run against the authenticated round-one base, map and witness.  After the
exact v3 body it appends the independently promoted canonical union of 562
primary blockers as redundant propagation and the global-reversal WLOG unit
`204168`.  Connectivity and nonzero voltage are not asserted in the CNF and
remain decoder/CEGAR gates.

The built artifact, before any solver launch, is

```text
/home/amodo/or15/work/root_k17_compact_horn_v3_20260802/
marker58_compact_horn_v3.cnf
marker58_compact_horn_v3.map.tsv
```

with frozen header and hashes

```text
p cnf 314651 1833776
CNF SHA256 cff3acda560916bdb846fb2f7026c0e4c514de54da4672f48d18f24ce02c103c
map SHA256 b623e15e60006dcf1ad4cbd817f7d595b691e9d622359a7886620e5f632ead38
builder SHA256 d758eb6458495a42dda2c34a3540ebf29db244d012b0b244e66b81f21895ae58
```

The 563 final rows beyond the exact core are not used in the equivalence
proof: 562 are already implied residence blockers and one fixes the reversal
symmetry.

Independent V2 stream replay subsequently passed without correction.  It
regenerated the 439,463-clause base prefix, every one of the 1,393,750 exact
core clauses, the sorted 562-bank, the WLOG row, and all 110,484 map rows.  Its
synthetic control rejects runs of lengths two and three and accepts lengths
four through eight; its independent floor-3,502 replay obtains the same
`114/92` quotient run-orbit counts.  The audit is frozen at

```text
/home/amodo/or15/work/qa_k17_compact_horn_v3_stream_replay_20260802_quotientaudit
audit JSON SHA256 fff169578e0a1cf8c0a05f07013f85272914acab8143d012a089e87bb89766bb
source SHA256     381e321d1979dd68f5f1d277ca486d6bee144684feacd931cdb0d1075ba58266
```

The artifact is therefore eligible for a solver run.  None had been launched
at the time of this promotion.
