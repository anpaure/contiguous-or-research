# Full-rotation necklace factors and the exact `m=6,8` cycle finishes

Date: 2026-08-01  
Status: exact quotient reduction and finite certificates for `2 <= m <= 8`;
the `m=6` cyclic factor is converted exactly to a Catalan linear forest.
No all-`m` existence claim is made.

## 0. Verdict

The proposed direct application of the Joos--Mubayi--Smith `P`-perfect
matching theorem does **not** prove an asymptotic ordered four-transversal.
In the Boolean host its degree parameter is `d=Theta(m^2)` while the
ambient vertex set has logarithm `Theta(m)`.  The theorem requires

\[
 |P\cup Q|\le \exp(d^{\varepsilon^3}),
\]

and its allowed fixed `epsilon` is sufficiently small (in particular below
`1/6` in the four-uniform application).  Therefore

\[
 d^{\varepsilon^3}=m^{2\varepsilon^3+o(1)}=o(m),
\]

so the ambient-size hypothesis fails.  Replacing the completion resources
by private copies does not change this row.  This is the same first failure
recorded in
`MATH_AUDIT_AD_JOOS_MUBAYI_SMITH_TRIPARTITE_COVERDOWN_SCOPE_20260731.md`.

There is nevertheless a new positive route.  Let the full coordinate
rotation `C_(2m)` act on the Boolean layers.  The exact four-resource
factor problem has a small orbit formulation.  A dependency-free exact
search in that formulation gives invariant cap-two factors for every

\[
                         2\le m\le8.                 \tag{0.1}
\]

The factors at `m=2,4,5,7` are already linear forests.  The factor at `m=6`
has twelve physical four-cycles.  It contains twenty-four exact old phases
of the square-collared ternary-hex actuator.  Toggling all twenty-four
phases simultaneously:

* preserves every lower and upper colour exactly;
* preserves physical maximum degree two;
* preserves full `C_12` rotation invariance; and
* removes all twelve cycles.

Thus the final `m=6` object is an explicit invariant Catalan linear forest
with exactly `Cat_6=132` path components.

At `m=8`, a `C_16`-invariant exact cap-two factor is found in `33` seconds.
It has `Cat_8=1430` path components and exactly one residual physical
`32`-cycle.  The cycle is free, projects to a quotient two-cycle, and has
coprime voltage.  It contains no old phase of the six-edge square-collar
actuator.  Nevertheless, an exhaustive short matching-exchange census finds
sixteen exact three-diamond switches, one rotation orbit, each of which
opens the cycle and two endpoint-bearing paths and reconnects them as a
forest.  Thus `m=8` also has an explicit exact Catalan linear forest.

This is finite evidence, but it identifies a much smaller all-dimensional
target: a weighted necklace-orbit selector, followed only when needed by a
rotation-closed square-collar toggle bank.

## 1. Exact orbit-selector reduction

Put

\[
 \mathcal L={\binom{[2m]}{m-1}},\qquad
 \mathcal M={\binom{[2m]}m},\qquad
 \mathcal U={\binom{[2m]}{m+1}}.
\]

For a diamond `e=(L,U)`, where `U-L={a,b}`, write

\[
             \psi(e)=\{L+a,L+b\}\in E(J(2m,m)).       \tag{1.1}
\]

Let `G=C_(2m)` act by coordinate rotation and write bars for orbits.  An
edge orbit `alpha=G e` is **outer-simple** if the two projections

\[
       \alpha\longrightarrow \bar L,\qquad
       \alpha\longrightarrow \bar U                 \tag{1.2}
\]

are bijections.  Thus selecting `alpha` covers every literal lower set in
`bar L` once and every literal upper set in `bar U` once.

For `X in mathcal M`, define the literal endpoint load

\[
 q_\alpha(X)=
 \#\{e'\in\alpha:X\in\psi(e')\}.                     \tag{1.3}
\]

### Theorem 1.1 (outer-simple orbit selector)

Let `A` be the outer-simple diamond orbits.  A binary vector
`(x_alpha:alpha in A)` develops to a `G`-invariant exact lower/upper
matching with physical maximum degree at most two if and only if

\[
 \sum_{\alpha:\bar L(\alpha)=\lambda}x_\alpha=1
       \quad(\lambda\in\mathcal L/G),                 \tag{1.4}
\]

\[
 \sum_{\alpha:\bar U(\alpha)=\upsilon}x_\alpha=1
       \quad(\upsilon\in\mathcal U/G),               \tag{1.5}
\]

and

\[
                \sum_\alpha q_\alpha(X)x_\alpha\le2
                       \quad(X\in\mathcal M).         \tag{1.6}
\]

Every component of the developed graph can then be oriented consistently,
giving injective tail and head maps.  Directed cycles are the only possible
remaining obstruction to a linear forest.

#### Proof

Outer simplicity makes (1.4) and (1.5) exactly the two literal palette
equalities.  Equation (1.3) is the contribution of one selected orbit to a
literal middle degree, so (1.6) is exactly maximum degree two.  Conversely,
any invariant factor which is a union of outer-simple orbits has a unique
selector satisfying these rows.  A graph of maximum degree two is a union
of paths and cycles, and coherent orientation of every component gives
indegree and outdegree at most one. `square`

This is an exact quotient reduction, not an LP relaxation.  It retains the
stabilizer weights in (1.3).  In particular, a middle necklace of orbit
size `s` can receive load `(2m)/s` from one full edge orbit; quotient degree
one is not the same as literal degree one.

### Corollary 1.2 (fixed-support Hall criterion)

Suppose a rotation-invariant physical graph `R` of maximum degree two is
already supplied and every edge orbit of `R` is outer-simple.  Form the
bipartite occurrence graph whose shores are the lower and upper necklaces
and whose edges are the edge orbits of `R`.  Then `R` contains an invariant
exact four-resource factor if and only if this occurrence graph has a
perfect matching, equivalently

\[
                  |N(S)|\ge |S|
            \qquad(S\subseteq\mathcal L/G).           \tag{1.7}
\]

This is ordinary Hall because the physical cap has been paid by `R` and
outer-simple development has unit necklace margins.  If non-simple orbits
are admitted, (1.7) is replaced by the corresponding integral weighted
`b`-matching rows.

## 2. The full-lattice Greene--Kleitman baseline

There is a useful non-equivariant baseline which separates topology from
physical degree.  In the ordinary Greene--Kleitman SCD of `B_(2m)`, every
chain meeting rank `m-1` has a central triple

\[
                         L\lessdot T\lessdot U.       \tag{2.1}
\]

Let `H` be the other middle vertex of `[L,U]`, and select `TH`.

### Proposition 2.1 (exact GK branching forest)

The selected edges use every lower and every upper colour exactly once.
Their orientation `T -> H` is acyclic, and the underlying graph is a
spanning forest with exactly `Cat_m` components.  Its maximum degree is
exactly `m`, so it is not a Catalan **linear** forest for `m>=3`.

#### Proof

The SCD central triples enumerate the rank-`m-1` and rank-`m+1` layers,
giving the two outer palettes.  In the standard bracketing description let
`a<b` be the first two free zero positions.  Then

\[
                         T=L+a,\qquad H=L+b.          \tag{2.2}
\]

The potential `omega(X)=sum_(i in X)i` strictly increases by `b-a` on
every directed edge, proving acyclicity.  There are `|L|` edges on `|M|`
vertices, so the number of forest components is

\[
                         |\mathcal M|-|\mathcal L|
                         =\operatorname {Cat}_m.      \tag{2.3}
\]

Finally the alternating word `X_*=(01)^m` is a singleton GK chain and is
the alternate head of the `m` words obtained by replacing one `01` block
by `00`.  Hence its degree is `m`.  The general fibre formula in
`MATH_THEOREM_CATALAN_FIXED_SCD_CENTRAL_MAP_AND_BTK_NOGO_20260731.md`
shows no larger fibre. `square`

Thus GK already pays exact outer palettes and acyclicity.  The entire
central difficulty is the integral rethread which lowers one branching
fibre from degree `m` to degree two without losing either palette.  The
full-rotation selector below does exactly that in the audited dimensions.

For reference, the central asymptotic ratio is

\[
 {2^{2m}\over\binom{2m}m}=\sqrt{\pi m}\,(1+o(1))
                         =2d(2m)+O(1),                \tag{2.4}
\]

not its reciprocal.

## 3. Relation to the necklace symmetric-chain theorem

Dhand proved that the binary necklace poset

\[
                        B_n/C_n
\]

has a symmetric-chain decomposition; see Vivek Dhand, *Symmetric Chain
Decomposition of Necklace Posets*, EJC 19 (2012), P26,
<https://doi.org/10.37236/1178>.

For even `m`, rotation is free on ranks `m-1` and `m+1`, so the central
length-two pieces of a necklace SCD give an outer-simple bijection between
the lower and upper necklaces.  They also nominate one on-chain middle
necklace and one alternate middle necklace.

There is an important stabilizer qualification.  If the nominated middle
necklace has literal orbit size `s<2m`, developing one outer-simple diamond
orbit hits each of its middle vertices `(2m)/s` times.  Thus a quotient SCD
does **not** by itself prove middle injection.  The exact remaining row is

\[
       \text{on-chain stabilizer load}
       +\text{alternate-head stabilizer load}\le2.     \tag{3.1}
\]

The orbit selector in Theorem 1.1 is precisely a rethreaded central
necklace matching with (3.1) enforced literally.  A uniform proof can now
reason at necklace scale, but it must retain these weights.

## 4. Exact finite census

The deterministic audit gives:

| `m` | `|L|` | lower necklaces | orbit candidates | exact solve | path components | cycle profile |
|---:|---:|---:|---:|:---|---:|:---|
| 2 | 4 | 1 | 2 | DFS, 2 nodes | 2 | none |
| 3 | 15 | 3 | 9 | DFS, 4 nodes | 5 | `2 x C6` |
| 4 | 56 | 7 | 66 | DFS, 8 nodes | 14 | none |
| 5 | 210 | 22 | 289 | DFS, 1,597 nodes | 42 | none |
| 6 | 792 | 66 | 1,366 | DFS, 304 nodes | 132 | `12 x C4` |
| 7 | 3,003 | 217 | 5,889 | Kissat, 1.4 s | 429 | none |
| 8 | 11,440 | 715 | 25,716 | Kissat, 33 s | 1,430 | `1 x C32` |

The path count in every row is forced by Euler:

\[
 |\mathcal M|-|\mathcal L|=\operatorname {Cat}_m.     \tag{4.1}
\]

Cycles add components but do not change the number of path components.

The physical cycle orbits are also explicit.

* At `m=3`, the two six-cycles form one rotation orbit.  The quotient is a
  two-cycle and its voltage has gcd `2` with `6`; it is not primitive.
* At `m=6`, the twelve four-cycles form one rotation orbit.  The quotient
  is a four-cycle of voltage zero, so its lift has all twelve components.
* At `m=8`, the unique thirty-two-cycle is itself rotation-invariant.  All
  its vertices have free `C_16` orbits, it projects to a quotient two-cycle,
  and its voltage has gcd one with `16`.

At `m=7` no voltage row remains because the selected graph is already a
`Cat_7=429`-path forest.  Thus the raw cyclic selector does not hide a coprime-voltage Hamilton
closure.  At `m=4,5` no voltage row remains because the selected physical
graph is already a forest.

## 5. Exact `m=6` square-collar finish

The `m=6` cap factor contains twenty-four indexed old phases of the
square-collar actuator in
`MATH_THEOREM_BOOLEAN_HEX_SQUARE_COLLAR_CYCLE_ACTUATOR_20260801.md`.
For each embedding, the three toggled old edges

\[
                         AB,\quad CD,\quad EF          \tag{5.1}
\]

and the three new edges

\[
                         AF,\quad CB,\quad ED          \tag{5.2}
\]

have identical lower- and upper-colour multisets.  The unchanged collar is

\[
                         FX,\quad XY,\quad YE.         \tag{5.3}
\]

In the selected factor the twenty-four old toggle triples are pairwise
edge-disjoint, and the twenty-four new triples are pairwise edge-disjoint.
The unchanged collars are allowed to overlap: only the zero-current
toggle triples are removed and inserted.  Applying all twenty-four toggles
therefore changes `72` old edges into `72` new edges.

### Theorem 5.1 (finite invariant collar closure)

The simultaneous toggle produces a `C_12`-invariant spanning linear forest
on the rank-six layer with:

\[
                    792\text{ edges},\qquad
                    924\text{ vertices},\qquad
                    132\text{ path components}.       \tag{5.4}
\]

Its lower intersections are all rank-five sets exactly once, and its upper
unions are all rank-seven sets exactly once.

#### Proof

The audit independently checks the palette identity for every one of the
twenty-four toggles and again for their union.  It checks that the final
edge set has the same cardinality, is closed under coordinate rotation,
and has maximum degree two.  Direct component traversal finds no cycle and
exactly `132` path components.  The two palette counters are the complete
rank-five and rank-seven layers.  Orient every path to obtain the ordered
tail/head injection. `square`

This is a finite exact use of the square collar on a globally chosen
factor, not the still-open claim that an arbitrary factor supplies such a
bank.

### Theorem 5.2 (finite `m=8` endpoint-bearing `C6` closure)

The frozen `m=8` factor has exactly one physical cycle, of length `32`.
There is a three-diamond alternating matching exchange which converts it to
a spanning linear forest with

\[
 11440\text{ edges},\qquad 12870\text{ vertices},\qquad
 1430=\operatorname {Cat}_8\text{ path components}.          \tag{5.5}
\]

One literal exchange uses lower masks

\[
                         8677,\quad10637,\quad43397.          \tag{5.6}
\]

It removes the physical edges

\[
 \{10669,10701\},\quad
 \{10725,41445\},\quad
 \{43405,43461\},                                      \tag{5.7}
\]

and inserts

\[
 \{8685,10725\},\quad
 \{10701,43405\},\quad
 \{43429,43461\}.                                     \tag{5.8}
\]

The first removed edge lies on the `32`-cycle; the other two lie in distinct
path components of sizes `11` and `62`.  Thus this is literally an
endpoint-bearing path-bank exchange: open the cycle and the two paths, then
reconnect the three pieces without a cycle.

#### Proof and exact motif census

Write the three selected diamonds as `(L_i,U_i)`.  Replacing them by

\[
                       (L_1,U_2),(L_2,U_3),(L_3,U_1)          \tag{5.9}
\]

preserves the lower and upper palettes identically.  The audit develops the
six diamonds into literal Johnson edges, checks maximum middle degree two,
and traverses every component of the changed graph.

The exhaustive census through the unique cycle is:

* all `32` alternating two-diamond (`C4`) exchanges fail the literal
  degree-two row;
* there are `720` directed three-diamond (`C6`) exchanges;
* `704` fail the literal degree row;
* the remaining `16` all produce a cycle-free `1430`-path forest.

The sixteen winners form one full `C_16` rotation orbit.  Every winner
removes exactly one edge of the `32`-cycle and one edge from each of two
distinct path components.  The first final physical edge-set SHA-256 is

```text
33c3aaa9b001f848e571cf00247e11f0f4bba2db92c80f89df0b8e7b5882fe13
```

This proves (5.5).  `square`

## 6. What is and is not proved

The finite results prove that full cyclic symmetry is compatible with the
central theorem much farther than the standard SCD examples suggest.  It
also shows that nonprimitive quotient cycle voltage can be repaired by a
rotation-closed zero-current actuator bank.

It does **not** prove:

1. that the orbit-selector system (1.4)--(1.6) is feasible for every `m`;
2. that a necklace SCD can always be rethreaded to satisfy (3.1);
3. that every residual cycle orbit has either a square-collar bank or an
   endpoint-bearing alternating exchange bank; or
4. any residence, deeper-shadow, or common-cap compiler row needed for the
   full OR-word theorem.

The clean next lemma is now:

> **Necklace-SCD weighted rethreading.**  Choose the central diamonds of a
> binary-necklace SCD, allowing alternating orbit switches, so every lower
> and upper necklace is used once and every literal middle load is at most
> two; moreover every resulting cycle orbit is either absent or supplied
> with a palette-neutral exchange which opens it against a path bank.

That statement would prove the exact central Catalan linear matching for
all `m`.  Guarding its toggles is then a separate RSB step.

## 7. Mechanical audit

Run

```text
python3 scratch/audit_catalan_full_rotation_cap_factors_20260801.py
```

It writes

```text
scratch/catalan_full_rotation_cap_factors_20260801.audit.json
```

and checks every literal atom, orbit projection, lower/upper palette,
middle degree, component, cycle orbit, actuator palette identity, and the
simultaneous `m=6` forest finish.

The compact `m=7` certificate is

```text
scratch/catalan_full_rotation_cap_factor_m7_20260801.audit.json
```

and is rebuilt without the SAT model by

```text
python3 scratch/audit_catalan_full_rotation_cap_certificate_20260801.py \
  scratch/catalan_full_rotation_cap_factor_m7_20260801.audit.json
```

The replay regenerates all `5,889` orbit candidates, develops the selected
`217` orbits, and checks all `3,003` lower colours, all `3,003` upper
colours, all `3,432` middle degrees, rotation invariance, and the complete
component traversal.  Its physical edge-set SHA-256 is
`c4479c257f6f880f553d8d5da6ae55da7bcb5225c32c5ef3e7a575f31fa20a5a`.

The compact `m=8` certificate is

```text
scratch/catalan_full_rotation_cap_factor_m8_20260801.audit.json
```

and is replayed by the same command with that path substituted.  It
regenerates all `25,716` orbit candidates, develops the selected `715`
orbits, and checks all `11,440` lower colours, all `11,440` upper colours,
all `12,870` middle degrees, rotation invariance, and the complete component
profile.  Its physical edge-set SHA-256 is
`76d2222791d3df336e65ebd9df51632f289542da86127818583dee115bbe72b5`.

The complete `m=8` short-exchange census is replayed by

```text
python3 scratch/audit_catalan_m8_cycle_exchange_census_20260801.py
```

and writes

```text
scratch/catalan_m8_cycle_exchange_census_20260801.audit.json
```

It enumerates all literal alternating matching cycles of lengths two and
three which touch the unique physical cycle, checks degree and topology for
every exchange, and verifies the rotation orbit and exact outer palettes of
the winner bank.  Its payload SHA-256 is
`e95c64bd32bb965642424716f52323629e34afd31b66d1d87c97efda74398587`.

Frozen audit identifiers:

```text
script SHA-256  caf3b172798f4015f01418228251bbed14be72630c110f5157321b044b9b4cda
JSON SHA-256    6a1486fccd04ade04ef645a536ed03edbbe3d1c6ac3d6cd3d6144c3399416ca5
payload SHA-256 2eea5972fea80e935005d0cbd97a9e92d29045154d7b3b12e2f0ab9ca4e44faa
```

Additional compact/exchange artifacts:

```text
generator SHA-256        e23457c895f37a4c001b7eb421eec3ef97a0af74d2ad4320618d75193d04caa6
decoder SHA-256          d9c4228cfbf5acf0ad974cf6272420958816e3205882e65732b99d2a4643baa9
compact replay SHA-256   ed45f030d971e6c62de79ff4e71f4074f61c5d45143e48e485b8f49a8fee864e
m=7 certificate SHA-256  e00e89a7aab011606b9427ff2f33e3d9acef0f8ce4662d440207625e70df763f
m=8 certificate SHA-256  694a048dc49474eb4444e244e5896860aa96d98dd06a507de6f0b741b8a52576
m=8 exchange script SHA   37bc266b756491998c95534ecd1bb56cf31f305d8f1aaf777f8aa76e90012e15
m=8 exchange JSON SHA     8bb3b7e39212edef0532b1d72296faff833b2ed22cf57a19aae017f33c67f433
```
