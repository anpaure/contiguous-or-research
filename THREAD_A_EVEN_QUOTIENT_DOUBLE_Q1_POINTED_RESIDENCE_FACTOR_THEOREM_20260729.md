# Even quotient carriers: uniform double-q1 factor and exact pointed residence

Date: 2026-07-29

Status: unconditional theorem for the direct `C_(k-1)` quotient factor;
exact residence correction and scope theorem.  No finite search is used.
The result proves a uniform degree-two factor with both q1 decks and pointed
top residence.  It does not prove a connected unit-voltage chronology or
all-coordinate residence.

## 0. Result

Let `K=2r=2m+2` be even, put

\[
 n=K-1=2m+1,
 \qquad \Omega=\mathbb Z_n,
\]

and distinguish `z notin Omega`.  The middle layer of `Omega union {z}`
has two shores

\[
 \mathcal A=\binom{\Omega}{m+1},
 \qquad
 \mathcal B=\{\{z\}\cup X:X\in\binom{\Omega}{m}\}.    \tag{0.1}
\]

The following statements are proved below.

1. For every even `K>=4`, there is a `C_n`-invariant spanning simple
   degree-two factor of `J(K,r)` which covers every lower-q1 and every
   upper-q1 target.
2. Its two palettes of smaller multiplicity are exact, and its other two
   palettes have the common PBBS load profile `1,2,3`.
3. The factor is strictly resident for the distinguished point `z` and its
   complement through every run threshold `D<=n`.  In particular it is
   pointed resident at the deadline depth, since `D=d(K)+1<=r<=n`.
4. On an arbitrary voltage quotient factor, residence is exactly a local
   insertion-return condition.  The eager `k=16` cross-boundary rows are
   exact on mixed-shore components, but a monochromatic quotient component
   also requires its lifted voltage length to be at least `D`.
5. Full old-coordinate residence remains separate.  Within the constructed
   complementary pair it is equivalent to simultaneous one-run and zero-run
   residence of the odd PBBS rail.  The canonical `K=16` rail fails that
   condition.

Thus the uniform **double-q1 plus pointed-residence factor theorem is true**.
The stronger double-q1 plus all-coordinate-residence theorem is not proved;
its implication from the pointed theorem is false.

## 1. Four q1 palettes and complementation

For a middle edge `e={X,Y}`, write

\[
 \partial_-(e)=X\cap Y,
 \qquad
 \partial_+(e)=X\cup Y.                               \tag{1.1}
\]

An AA edge has both endpoints in `mathcal A`, a BB edge has both endpoints
in `mathcal B`, and an AB edge crosses the shores.  Their possible colours
are:

| edge | lower q1 | upper q1 |
|---|---|---|
| AA | rank `m`, no `z` | rank `m+2`, no `z` |
| BB | `{z}` plus old rank `m-1` | `{z}` plus old rank `m+1` |
| AB | old rank `m` | `{z}` plus old rank `m+1` |

The two hard palettes are therefore lower-with-`z`, supplied only by BB,
and upper-without-`z`, supplied only by AA.

For `X subseteq Omega`, write `bar X=Omega setminus X`.

### Lemma 1.1 (complement-paired shore factor)

Let `G` be a spanning two-factor of `J(n,m)`, and let `bar G` be
the factor on `binom(Omega,m+1)` obtained by complementing both endpoints
of every edge.  Place `G` on the B shore by adjoining `z`, and place
`bar G` on the A shore.  Their disjoint union `H(G)` has both q1 decks
complete if and only if

\[
 \{X\cap Y:XY\in E(G)\}=\binom{\Omega}{m-1}           \tag{1.2}
\]

and

\[
 \{X\cup Y:XY\in E(G)\}=\binom{\Omega}{m+1}.         \tag{1.3}
\]

Multiplicities are paired occurrence by occurrence:

\[
 \begin{aligned}
 \partial_-(\{z\}\cup X,\{z\}\cup Y)
   &=\{z\}\cup(X\cap Y),\\
 \partial_+(\{z\}\cup X,\{z\}\cup Y)
   &=\{z\}\cup(X\cup Y),\\
 \partial_-(\bar X,\bar Y)&=\overline{X\cup Y},\\
 \partial_+(\bar X,\bar Y)&=\overline{X\cap Y}.
 \end{aligned}                                       \tag{1.4}
\]

#### Proof

Equations (1.4) are De Morgan's laws.  The four target families in the
table are pairwise the images of the two families in (1.2)--(1.3), so those
two support conditions are sufficient.  Conversely, within the split factor
`H(G)`, BB is the only source of either `z`-containing palette: its lower
deck forces (1.2), and its upper deck forces (1.3).  QED.

### Lemma 1.2 (residence under shore complementation)

Let `D>=1`.  On every B component of `H(G)`, the `z` trace is constant one;
on every A component it is constant zero.  Under the strict convention that
a constant cyclic trace is one run of the component length, `H(G)` is
top-bi-`D`-resident if and only if every component of `G` has length at
least `D`.

For an old coordinate `x`, its trace on a paired A component is the bitwise
complement of its trace on the B component.  Hence `H(G)` is fully
old-coordinate `D`-resident if and only if every coordinate trace of `G`
has both all one-runs and all zero-runs of length at least `D`, with constant
traces interpreted by component length.

#### Proof

The first assertion follows from the shore definitions.  The second follows
from

\[
 \mathbf1_{\{x\in\bar X\}}=1-\mathbf1_{\{x\in X\}}.   \tag{1.5}
\]

QED.

## 2. Uniform PBBS construction

Let `f` be the canonical cyclic-parenthesis/PBBS permutation of
`binom(Omega,m)`.  We use the following audited PBBS facts.

1. `f` commutes with rotation of `Omega`.
2. The centered edges

   \[
    E_X=\{f^{-1}(X),f(X)\}
    \qquad(X\in\binom{\Omega}{m})                     \tag{2.1}
   \]

   form a simple spanning two-factor `G_PBBS`.
3. The intersections

   \[
    \theta(X)=f^{-1}(X)\cap f(X)                      \tag{2.2}
   \]

   cover every old rank-`(m-1)` set, each with load between one and three.
4. Every orbit of `f` has length divisible by `n`.

Facts 2--4 are the symbolic conclusions audited in
`MATH_AUDIT_PBBS_FIRST_SHADOW_THEOREM_20260726.md`; the orbit-divisibility
input there is explicitly inherited from
`PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md`, not from equivariance alone.

Both PBBS neighbours of `X` are disjoint from `X`.  Since (2.2) has rank
`m-1`, their union has rank `m+1`; it is contained in the rank-`(m+1)` set
`bar X`.  Therefore

\[
 f^{-1}(X)\cup f(X)=\bar X.                            \tag{2.3}
\]

In particular, the union colours in (2.1) enumerate every old
rank-`(m+1)` set exactly once.

### Theorem 2.1 (uniform double-q1, pointed-resident factor)

For every even `K=2m+2>=4`, let

\[
 F_B=\bigl\{\{\{z\}\cup f^{-1}(X),
                   \{z\}\cup f(X)\}:X\in\binom{\Omega}{m}\bigr\},
                                                               \tag{2.4}
\]

let `F_A` be its old-coordinate complement on `mathcal A`, and put

\[
                         F=F_A\mathbin{\dot\cup}F_B.   \tag{2.5}
\]

Then:

1. `F` is a `C_n`-invariant spanning simple degree-two factor of
   `J(K,m+1)`;
2. both q1 decks are complete;
3. for `R in binom(Omega,m-1)` and `U in binom(Omega,m+1)`,

   \[
   \begin{aligned}
    \lambda_-(\{z\}\cup R)
       &=\lambda_+(\bar R)
        =|\{X:\theta(X)=R\}|\in\{1,2,3\},\\
    \lambda_+(\{z\}\cup U)
       &=\lambda_-(\bar U)=1;
   \end{aligned}                                      \tag{2.6}
   \]

4. every physical component has length at least `n`, and `F` is strictly
   top-bi-`D`-resident for every `D<=n`.

#### Proof

For `m=1`, take `f` to be the cyclic permutation of the three singletons of
`Z_3`.  The centered factor is a triangle: its intersections give the empty
old set with load three, and its unions give each old two-set once.  Its
complement is the other middle-layer triangle.  Thus all claims, including
component length `n=3`, hold directly.  Assume henceforth `m>=2`, where the
audited PBBS facts above apply.

The PBBS factor theorem gives the degree-two and simplicity assertions on
the B shore; complementation gives them on the A shore.  The shores are
disjoint, so (2.5) is spanning and degree two.  Rotation equivariance of
`f` proves `C_n` invariance.

Equations (2.2)--(2.3), Lemma 1.1, and the PBBS load bound give (2.6) and
both q1 decks.

Let an `f`-cycle have length `ell*n`.  The centered factor has monodromy
`f^2`, so its cycles have length

\[
 \frac{\ell n}{\gcd(2,\ell n)}
  =\frac{\ell n}{\gcd(2,\ell)},                       \tag{2.7}
\]

because `n` is odd.  This is a positive multiple of `n`.  Lemma 1.2 now
proves strict top bi-residence through `D=n`.  QED.

### Corollary 2.2 (exact direct quotient factor)

The factor `F` descends to an integral degree-two factor of
`J(K,m+1)/C_n`.  Quotient loops count twice in the degree equation.

#### Proof

Rotation is free on old ranks `m` and `m+1`: a nontrivial stabilizer would
partition `Omega` into equal orbits of a length dividing `n`, and an
invariant subset size would be divisible by that length, contrary to

\[
 \gcd(n,m)=\gcd(n,m+1)=1.                              \tag{2.8}
\]

The edge action is also free.  An odd-order rotation stabilizing an
unordered two-set of vertices cannot interchange them, so it fixes each;
vertex freeness then makes it the identity.  Thus every physical edge orbit
has size `n`, and quotienting the invariant degree-two equations is exact.
A quotient loop represents an edge joining two rotated copies of one vertex
orbit and contributes degree two.  QED.

### Corollary 2.3 (deadline pointed residence)

Let `d(K)` be the monotone-deadline depth and set `D=d(K)+1`.  Then the
factor in Theorem 2.1 is top-bi-`D`-resident.

#### Proof

There are `m` nonempty ranks strictly below the middle rank, and each has
size at most the middle width `W=binom(K,m+1)`.  Hence the deadline
inequality already holds at `d=m`, so

\[
 d(K)\le m,
 \qquad D\le m+1\le2m+1=n.                            \tag{2.9}
\]

Apply Theorem 2.1.  QED.

The theorem solves the direct quotient **factor** gate.  It does not give
one `(c,t)` word: that normal form describes a single coprime-voltage cyclic
chronology, whereas (2.5) is a shore-separated factor with generally many
components.

## 3. Exact pointed residence on a voltage quotient

The preceding construction has constant top traces.  We now give the exact
criterion for an arbitrary selected quotient factor.

Let `C` be an oriented quotient cycle of length `ell`.  Choose a developed
lift

\[
 X_{i+\ell}=\rho^vX_i,
 \qquad
 X_{i+1}=X_i-\{a_i\}+\{b_i\},                         \tag{3.1}
\]

where `v in Z_n` is the cycle voltage.  Extend `a_i,b_i` by the same
rotation rule.  Put

\[
 o=\operatorname{ord}_{\mathbb Z_n}(v)
   =\frac n{\gcd(n,v)},
 \qquad L=\ell o.                                     \tag{3.2}
\]

The quotient cycle lifts to `gcd(n,v)` physical cycles, each of length `L`.

### Theorem 3.1 (insertion-return criterion)

For every quotient transition occurrence `i`, define

\[
 g_i=\min\{s\ge1:a_{i+s}=b_i\}.                       \tag{3.3}
\]

Then `g_i` is exactly the length of the physical positive run begun by the
insertion at transition `i`.  It is independent of the phase of the lift.
Consequently positive `D`-residence on all nonconstant traces is equivalent
to either of

\[
 g_i\ge D\quad\hbox{for every }i,                     \tag{3.4}
\]

\[
 b_i\in\bigcap_{s=1}^{D}X_{i+s}\quad\hbox{for every }i.\tag{3.5}
\]

Bi-residence additionally requires

\[
 a_i\notin\bigcup_{s=1}^{D}X_{i+s}\quad\hbox{for every }i.\tag{3.6}
\]

Under the strict cyclic convention, a constant-one trace must also have
physical length `L>=D` for positive residence.  For bi-residence the same
length condition applies to either constant symbol.

#### Proof

The coordinate `b_i` is absent from `X_i`, is inserted into `X_(i+1)`, and
remains present until the first transition which deletes it.  Closure after
`L` transitions guarantees such a deletion and proves that the run is

\[
 X_{i+1},X_{i+2},\ldots,X_{i+g_i}.                    \tag{3.7}
\]

This proves (3.3)--(3.5).  Replacing the developed lift by another phase
rotates both the states and the transition labels, leaving the gap of the
corresponding rotated insertion unchanged.  This is phase independence of
the orbit test, not an identification of differently named old coordinates.

After deletion of `a_i`, condition (3.6) says that the coordinate is absent
from the next `D` states, which is exactly the zero-run condition.  Constant
traces have no insertion or deletion event, so (3.4)--(3.6) do not see them;
the run of the constant symbol is the whole physical component of length
`L`.  QED.

Rotating `b_i` to a distinguished old point turns (3.5) into a literal
pointed-vertex test.  Thus only one radius-`D` successor audit per quotient
transition is needed; it represents all developed rotations of that
insertion.

### Corollary 3.2 (top-shore path criterion)

Delete every selected AB edge of a physical degree-two factor.  Each
component induced on the B shore is either

1. a path, whose number of vertices is exactly one finite positive `z`-run;
   or
2. a cycle, which is a factor component with constant-one `z` trace.

Hence top `D`-residence is equivalent to every B path having at least `D`
vertices, together with the same bound on each all-B cycle under the strict
convention.  Top bi-residence applies the identical test to the A shore.

#### Proof

At a B vertex, deleting cross edges leaves rail degree two, one, or zero
according as its selected cross degree is zero, one, or two.  The resulting
maximum-degree-two components are paths and cycles.  Path endpoints are
exactly shore-change vertices, so traversing the original factor identifies
the path with one maximal B run.  An isolated B vertex of cross degree two
is a one-vertex path whose single vertex represents both run boundaries.
A B cycle has no cross edge and is a whole factor component.  QED.

On a mixed quotient cycle, the physical shore word is the cyclic quotient
shore word repeated `o` times.  Its nonconstant run lengths are therefore
the quotient run lengths.  For arbitrary `D`, the exact local encoding is to
forbid every selected cross--rail--cross path with fewer than `D` shore
vertices.

### Corollary 3.3 (monochromatic voltage clause)

If a monochromatic B quotient component has quotient length `ell` and
voltage `v`, strict positive-top residence requires and is implied by

\[
                 \frac{\ell n}{\gcd(n,v)}\ge D.        \tag{3.8}
\]

For strict top bi-residence, the same condition is required on a
monochromatic component of either shore.

Thus the `k=16` eager cross-degree/product rows are exact for mixed
components but not by themselves for arbitrary quotient factors.

At `n=15`, let

\[
 X=\{0,1,2,5,6,7,10,11\}.
\]

Then `X+5` is obtained from `X` by deleting `2` and inserting `12`.  The AA
edge `{X,X+5}` is a quotient loop of voltage five.  It consumes quotient
degree two and lifts to five physical triangles.  All cross-boundary eager
variables vanish, yet its constant zero top trace has length three.  Its
full complement is a BB loop with constant-one top trace of length three.
This is an exact counterexample to the unqualified eager-residence claim;
(3.8) is the missing condition.

## 4. Necessary capacity bounds

Put

\[
 P=\binom nm,
 \qquad H=\binom n{m-1}.                               \tag{4.1}
\]

### Proposition 4.1 (physical cross-run capacity)

Let a spanning even-middle two-factor have `2R` cross-shore edges.  Then it
has `R` finite runs on each shore and

\[
 e_{AA}=e_{BB}=P-R.                                    \tag{4.2}
\]

If both q1 decks are complete, then

\[
 R\le P-H=\frac{2P}{m+2}.                             \tag{4.3}
\]

If it is top-bi-`D`-resident, then also

\[
                         R\le\frac PD.                \tag{4.4}
\]

#### Proof

Summing degree two over either shore gives

\[
 2P=2e_{AA}+2R=2e_{BB}+2R,
\]

which proves (4.2).  Lower-with-`z` has `H` targets and can use only BB;
upper-without-`z` has `H` targets and can use only AA.  Thus both same-shore
edge counts are at least `H`, proving (4.3).  Finally, the `R` B runs are
vertex-disjoint and each has at least `D` vertices, so `RD<=P`.  QED.

For the quotient form, let

\[
 M=P/n=\operatorname{Cat}_m
\]

be the number of vertex orbits on each shore, and let `Q` be the number of
`C_n` orbits of old rank-`(m-1)` targets.

### Corollary 4.2 (quotient capacity)

If `a,b,c` are the numbers of selected AA, BB, and AB edge orbits in an
invariant quotient factor, then

\[
 2a+c=2M=2b+c,
 \qquad
 a=b=M-c/2.                                            \tag{4.5}
\]

Double-q1 completeness and top bi-`D`-residence imply respectively

\[
 c\le2(M-Q),
 \qquad
 c\le\frac{2M}{D}.                                    \tag{4.6}
\]

At `K=16`, `M=429`, `Q=335`, so `c/2<=94`.  In a single `(c,t)`
chronology the number of cross edge orbits is `2h`, where `h` is the number
of one-runs of the word `t`; this recovers exactly `h<=94` from the
normal-form note.

#### Proof

Equation (4.5) is the quotient shore-degree sum; it also makes `c` even.
Each same-shore edge orbit has only one hard colour orbit, so `a,b>=Q`.
The residence bound follows by partitioning the `M` quotient vertices of
one shore among its `c/2` mixed runs and any monochromatic components.  QED.

### Proposition 4.3 (old-coordinate residence rate obstruction)

Let `G` be any spanning two-factor on `binom(Omega,m)`.  If every positive
coordinate run has length at least `D`, then

\[
                              D\le m.                  \tag{4.7}
\]

#### Proof

Orient every component.  There are `P` transitions and hence `P` insertion
events in total.  For a fixed coordinate `x`, the total membership mass is

\[
 \binom{n-1}{m-1}=\frac{mP}{n}.                        \tag{4.8}
\]

Every insertion starts a positive run of at least `D` states, so `x` is
inserted at most `mP/(nD)` times.  Summing over all `n` coordinates gives

\[
 P\le n\frac{mP}{nD},
\]

which is (4.7).  Constant positive components consume membership mass but
create no insertion, so they only strengthen the inequality.  QED.

This obstruction already rules out a fully resident version at thresholds
`D>m`; it does not obstruct the `K=16` target `D=4,m=7`.

## 5. A conditional top-mixing square

The factor in Theorem 2.1 is shore-separated.  There is nevertheless an
exact **physical-factor** q1-preserving square whenever two PBBS hard
colours have reserve.  This subsection does not claim that rotating the
square orbitwise preserves its run lengths or its exceptional-orbit loads.

Put `g=f^2`, let

\[
 I_X=X\cap g(X),
\]

and index the B rail edge by `{X,g(X)}`.  Remove that edge and the A rail
edge complementary to `{f(X),f^3(X)}`.  Add the cross edges

\[
 (\{z\}\cup X)\ --\ \overline{f(X)},
 \qquad
 (\{z\}\cup g(X))\ --\ \overline{f^3(X)}.             \tag{5.1}
\]

They are legal Johnson edges because consecutive PBBS states are disjoint.

### Proposition 5.1 (conditional mixed-component switch)

The switch (5.1) restores every deleted easy q1 colour.  Its only possible
q1 losses are

\[
 \{z\}\cup I_X,
 \qquad
 \overline{I_{f(X)}}.                                  \tag{5.2}
\]

Therefore it preserves both complete q1 decks if

\[
 |\{Y:I_Y=I_X\}|\ge2,
 \qquad
 |\{Y:I_Y=I_{f(X)}\}|\ge2.                            \tag{5.3}
\]

It merges the selected A and B cycles into one mixed cycle, whose two shore
runs have the full old cycle lengths and are therefore at least `n`.

#### Proof

The first cross edge has lower colour `X` and upper colour
`{z} union bar(f(X))`; the second has lower colour `g(X)` and upper colour
`{z} union bar(f^3(X))`.  The deleted B upper colour is
`{z} union bar(f(X))`, while the deleted A lower colour is `g(X)`; these are
restored.  Cross edges cannot supply a lower-with-`z` or upper-without-`z`
hard colour, so the only deleted hard colours are exactly (5.2).  Condition
(5.3) leaves another PBBS occurrence of each.

Removing one edge from each of two disjoint cycles gives two paths, and the
two cross edges join them into one cycle.  Each path contains every vertex
of its old cycle, so Theorem 2.1 supplies the run-length bound.  QED.

Condition (5.3) is not proved uniformly.  Proposition 5.1 is therefore a
conditional physical top-mixing theorem, not part of the unconditional
existence claim.  A `C_n`-equivariant version must apply the complete
rotation orbit of (5.1); short target orbits can then lose several physical
occurrences at once, and repeated cuts of one component can shorten the top
blocks.  It must also verify that the two new cross edges occupy distinct
edge orbits with the required four endpoint incidences, and that at least one
retained edge orbit still covers each deleted hard-colour orbit.  Those
orbit-load, degree, and chronology checks remain separate.

## 6. Exact boundary of the theorem

The algebraic `(c,t)` normal form in
`MATH_EVEN_EQUIVARIANT_CT_NORMAL_FORM_20260729.md` is sound: its class sums,
transversality, two necklace bijections, residence identities, and `k=16`
bound `h<=94` all pass.  It parametrizes a single unit-voltage equivariant
chronology.  The split factor of Theorem 2.1 belongs to the larger direct
quotient factor model, not generally to that normal form.

The uniform theorem proves:

* exact middle ownership and degree two;
* `C_(K-1)` equivariance;
* all four q1 palettes;
* strict residence of the top coordinate and its complement; and
* an exact quotient realization with loops correctly weighted.

It does not prove:

* connectedness or coprime unit voltage;
* a single `(c,t)` chronology;
* all-coordinate residence;
* deeper shadow support after a mixed fusion;
* a safe linear opening or arbitrary-width upper completeness; or
* feasibility of the final unrestricted compiler.

For the canonical `K=16` PBBS shore, there are `90` positive runs of length
two and `855` of length three.  Thus its complementary split factor is not
fully `D=4` resident.  The independently repaired resident B shore has a
complement with `1125` short runs (`360` of length two and `765` of length
three).  The first census is recorded in
`MATH_K16_Q1_COMPILER_CAPACITY_AND_PBBS_PIVOT_20260729.md`; the second is in
`MATH_AUDIT_K16_CT_RECONCILIATION_AND_QUOTIENT_FACTOR_20260729.md`.  These
facts refute the implication

\[
 \text{double-q1 + pointed residence}
 \Longrightarrow
 \text{all-coordinate residence},                    \tag{6.1}
\]

but do not refute existence of another fully resident double-q1 factor.
That is the smallest remaining factor-level theorem.

## 7. Boundary check against the connected k16 Hamilton artifact

The retained artifact

```text
scratch/k16_connected_q1_lower2_hamilton_20260729.json
```

has file SHA-256

```text
16fc3739b8b4df5bed71c44b2f2e148f4839753cab6b9ea308e78d17ee9c32d8.
```

Its audit block reports:

\[
 \begin{array}{c|c}
 \text{selected quotient edge orbits}&858\\
 (AA,AB,BB)&(376,106,376)\\
 \text{physical components}&1\\
 \text{physical component length}&12870\\
 \text{upper-q1 quotient holes}&0\\
 \text{lower-q1 quotient holes}&2\\
 \text{q2 quotient holes}&89\\
 \text{arbitrary-upper quotient holes}&129.
 \end{array}                                           \tag{7.1}
\]

The parallel swap replaces edge orbit `13230` by the parallel orbit `13232`.
The two have the same quotient endpoints, so the quotient degree-two cycle
is unchanged while its total voltage becomes coprime to 15; the developed
lift changes from three cycles of length 4290 to one cycle of length 12870.
Thus connectivity/Hamiltonicity is genuinely closed for this selected
factor.  The artifact is also upper-q1 perfect.

The phrase **lower2** must retain its quotient meaning.  It denotes two
missing lower-colour orbits, not two missing physical colours.  This matters
to the compiler.

### Lemma 7.1 (invariant q1 holes cannot use two boundary channels)

Let `K=2m+2>=6`, let a `C_(2m+1)`-invariant Johnson Hamilton cycle on the
middle layer be opened to a linear path `T`, and suppose a word `A` satisfies
`D^dA=T` and covers every lower-q1 target.  Then the original cyclic carrier
must already have complete lower-q1 support.

#### Proof

The missing lower-q1 family of the cyclic carrier is rotation invariant.
A lower target omitting `z` has an old `m`-subset, while one containing `z`
has an old `(m-1)`-subset.  Since `m>=2`, neither old subset is empty or all
of `Z_(2m+1)`.  Its rotation orbit is therefore a nontrivial divisor of the
odd number `2m+1`, and has size at least three.

Opening the Hamilton cycle deletes an edge and cannot create an internal q1
colour.  Hence any nonempty cyclic hole orbit leaves at least three q1
targets absent from the internal transition deck of `T`.  But the
unrestricted q1 two-channel theorem says that an antecedent `D^dA=T` can
realize at most one such missing rank-`(r-1)` target on its prefix chain and
at most one on its suffix chain.  Thus at most two are possible, a
contradiction.  QED.

### Corollary 7.2 (the retained Hamilton is not COMP3-feasible)

The two missing quotient lower-q1 orbits in (7.1) have representatives
`33371` and `38053` and respective orbit sizes `15` and `5`.  They therefore
contain exactly twenty physical targets.  Hence no opening of this fixed
Hamilton cycle admits a lower-complete `COMP_3` antecedent.  Moreover, exact
enumeration of all `2*12870=25740` directed openings gives minimum endpoint
SDR deficiency `19`; this stronger finite statement is recorded in
`scratch/threadD_k16_connected_q1_lower2_hamilton_comp3.audit.json`.

The artifact is correctly labelled `PARTIAL_Q1_PHYSICAL_HAMILTON`.  Its
proved content is precisely:

\[
 \boxed{\text{physical Hamilton + upper-q1 perfect + two lower quotient holes}}.
                                                               \tag{7.2}
\]

It is not compiler-eligible: the two quotient holes are twenty literal q1
holes, whereas the two global boundary channels cannot repair them.  For
this exact carrier the remaining ledgers are already explicit:

* residence fails, with short-run histogram
  `1^375 2^1635 3^1410`;
* q2 has 89 quotient holes;
* arbitrary upper coverage has 129 quotient holes; and
* `COMP_3` is impossible already at lower q1 by Corollary 7.2.

Thus the parallel-voltage swap closes connectivity only.  A successor
carrier must preserve the Hamilton/unit-voltage achievement while reducing
the lower-q1 quotient holes from two to zero, and then address residence,
q2, arbitrary upper coverage, and the remaining compiler constraints.

## 8. Exact fixed-quotient parallel-phase residence no-go

The same retained Hamilton has a second, logically independent obstruction.
It cannot be made fully `D=4` resident by retaining its quotient cyclic order
and merely replacing selected quotient edges by parallel edge orbits.  The
reason is local and survives arbitrary changes of the total voltage.

Let a cyclic group `G` permute a coordinate set and act freely on the
vertices and edges of a `G`-invariant set-labelled graph, so membership
traces are transported equivariantly.  Let

\[
 v_0v_1\cdots v_{s-1}v_0                              \tag{8.1}
\]

be a loopless cycle in the quotient multigraph.  For each quotient
adjacency `v_i v_(i+1)`, let `E_i` be the set of physical edge orbits above
that unordered pair.  A *parallel reassignment* keeps (8.1) and replaces
the selected member of `E_i` by another member of `E_i`; it may change the
total voltage and hence the number of developed components.

Suppose a developed lift contains a marked coordinate trace

\[
 0,\underbrace{1,\ldots,1}_{r},0,
 \qquad 1\le r<D,                                      \tag{8.2}
\]

along `r+1` consecutive physical edges above quotient adjacencies
`i,i+1,...,i+r`.  Call this witness *parallel-rigid* if

\[
 |E_i|=|E_{i+1}|=\cdots=|E_{i+r}|=1.                  \tag{8.3}
\]

### Lemma 8.1 (frozen-segment lemma)

Every parallel reassignment of the fixed quotient cycle (8.1) retains a
`G`-translate of every parallel-rigid witness (8.2).  In particular, if
(8.2) is a complete positive run, the reassigned developed factor still has
a positive run of length `r<D` and is not `D`-resident.

#### Proof

Fix a lift of `v_i`.  Because the action is free and the quotient cycle is
loopless, a physical edge orbit above `v_jv_(j+1)` is a `G`-equivariant
perfect matching between the two vertex fibres.  Hence a prescribed lift of
`v_j` has a unique continuation through that edge orbit.  Under (8.3), the
entire lifted segment above `v_i,...,v_(i+r+1)` is therefore forced once its
first vertex is chosen.

A parallel reassignment before the segment can change which lift of `v_i`
is reached, but freeness says that this new lift is `g` times the old one for
a unique `g in G`.  Equivariance then forces every vertex of the new local
segment to be the same `g`-translate of the corresponding old vertex.
Reassignments after the segment do not affect it.  Thus the marked
coordinate in (8.2) is transported by `g` and again has trace `0,1^r,0`.
This is a complete positive run of the same length.  The argument does not
use the total voltage or connectedness of the developed lift.  QED.

The loopless hypothesis is only a convenient way to avoid choosing an
orientation through a quotient loop.  It holds for the retained Hamilton
quotient cycle.  The conclusion also holds for an oriented loop occurrence
once its signed lift is included in the fixed local data.

### Corollary 8.2 (three thousand immutable `k=16` residence defects)

For the quotient cycle in

```text
scratch/k16_connected_q1_lower2_hamilton_20260729.json
```

there are `43` selected quotient adjacencies having at least one parallel
choice and `50` alternative edge orbits above them.  Its short positive-run
census and parallel-rigid subcensus are

\[
\begin{array}{c|rrr|r}
 r&1&2&3&\text{total}\\ \hline
 \text{all short runs}&375&1635&1410&3420\\
 \text{parallel-rigid}&360&1455&1185&3000.
\end{array}                                             \tag{8.4}
\]

Equivalently, the rigid rows in (8.4) comprise respectively `24`, `97`, and
`79` `C_15`-orbits of witnesses, for `200` quotient witnesses in all.
Therefore **every** choice of parallel representatives on this fixed
quotient Hamilton cycle retains at least `3000` positive runs of length less
than four.  No phase or voltage choice in this class can make the factor
fully `D=4` resident.

#### Certificate and audit scope

The exact audit is

```text
scratch/audit_k16_fixed_qcycle_parallel_residence_no_go_20260729.py
```

with SHA-256

```text
14c02bbbcaf1e3762777cf4ef512f4a3e23caaee8e852416339a877539b25029.
```

It pins the carrier SHA in Section 7 and also pins the sorted selected-orbit
list by SHA-256

```text
02078ab691a57372de7a540417ce7005ac0fb52265a3a05d728518a23bc3131d.
```

The script reconstructs the complete catalogue of `27456` physical edge
orbits, groups them by unordered quotient endpoint pair, reconstructs the
unique physical Hamilton cycle, and tests the entering, internal, and
exiting edges of every short run against the complete parallel catalogue.
Thus (8.4) is an exact fixed-cycle certificate, not a sample or a
single-phase check.

This no-go does **not** obstruct a new quotient cycle, a switch that changes
one of the 858 quotient adjacencies, or a non-equivariant physical surgery.
It says precisely that the attractive remaining freedom after fixing this
quotient Hamilton cycle--parallel edge choice, phase, and total
voltage--is insufficient for residence.  Together with Corollary 7.2 it
gives two independent reasons that the promoted carrier is not the final
even-`k` compiler carrier:

\[
 \boxed{
 \begin{array}{c}
 \text{fixed quotient order + parallel choices}
   \Longrightarrow \text{at least 3000 short runs},\\
 \text{two fixed lower-q1 hole orbits}
   \Longrightarrow \mathrm{COMP}_3\text{ infeasible}.
 \end{array}}
                                                               \tag{8.5}
\]

Consequently, within the equivariant quotient-carrier route, the smallest
surviving construction problem must change the quotient adjacency cycle
itself while preserving physical Hamiltonicity and upper-q1 completeness,
and must simultaneously obtain lower-q1 completeness and full residence.
Deeper q2, arbitrary-upper, and compiler conditions remain later gates.

## 9. A different `k=16` quotient cycle closes double-q1 plus pointed residence

Section 8 is deliberately tied to one SHA-pinned quotient order.  It does
not apply to the later certificate

```text
scratch/k16_qfactor_q1_topresident_hamilton_20260729.json
```

whose SHA-256 is

```text
f76ab4e5c30c3269da87788c275777a3b40deea96f4fbf892cd5c6027280a7a5.
```

The catalogue replay and the separately implemented replay are

```text
scratch/k16_qfactor_q1_topresident_hamilton_20260729.audit.json
scratch/k16_qfactor_q1_topresident_hamilton_20260729.independent.audit.json
```

with respective SHA-256 values

```text
f51c1cba8d540fda4cf148b68b7bbc71a3c04407f4182cfba641fa255bce1624
577328d33dde398f584e5cd0a49278edb39b7be9866bded5a0c55de366792c1a.
```

They report

\[
 \begin{array}{c|c}
 \text{lower/upper q1 quotient support}&764/764\\
 \text{quotient components}&1\\
 \text{physical components}&1\\
 \text{physical cycle length}&12870\\
 \text{minimum top-one/top-zero run}&4/4.
 \end{array}                                           \tag{9.1}
\]

Thus, at `K=16`, physical Hamiltonicity, both complete q1 decks, and pointed
top-bi-residence are simultaneously attainable.  This is stronger than the
uniform split-factor conclusion at this one dimension and removes the two
lower-q1 hole orbits of Section 7 by changing the quotient adjacency cycle.
Among the two Hamilton artifacts discussed here, this q1-perfect,
top-bi-resident cycle is the only compiler-eligible carrier.  Here
*compiler-eligible* means that it clears the carrier-side q1 and pointed
residence prerequisites for an exact compiler audit; it does not mean that
`COMP_3` has already been solved.

It does not solve full residence.  The other-coordinate short-run census is

\[
 1^{330}2^{1620}3^{1440},                              \tag{9.2}
\]

for `3390` violations.  Nor do the q1/top-residence audits certify q2,
arbitrary upper coverage, or `COMP_3`.  Consequently the exact surviving
`k=16` factor gate is now full-coordinate residence on a double-q1
Hamilton quotient cycle; the deeper and compiler ledgers remain separate.
No dimension-uniform connected/resident theorem follows from this finite
certificate.

## 10. Exact residence--q1 coupling on the compiler-eligible Hamilton cycle

The carrier of Section 9 cannot be repaired by first deleting old edges to
destroy its residence defects while preserving its current q1 providers.
Residence and q1 reconstruction must be solved in one global rethread.

Let `F` be the selected set of `858` quotient edge orbits in the Section 9
carrier.  For a selected edge `e`, write `c_-(e)` and `c_+(e)` for its lower
and upper q1 colours, and put

\[
 P_\epsilon(c)=\{e\in F:c_\epsilon(e)=c\},
 \qquad \epsilon\in\{-,+\}.                           \tag{10.1}
\]

The `3390` physical short positive runs split into `226` free `C_15`-orbits.
For one representative run of length `r<4`, retain the entering edge, its
internal run edges, and the exiting edge.  Their quotient edge-orbit set is
a *residence motif*.  Thus the motif-size histogram is

\[
 2^{22}3^{108}4^{96},
 \qquad 22+108+96=226.                                \tag{10.2}
\]

Let $\mathcal M$ be this family of motifs.  For a deletion set
$D\subseteq F$, define

\[
 h_\epsilon(D)=
 \#\{c:P_\epsilon(c)\ne\varnothing,
          P_\epsilon(c)\subseteq D\}.                 \tag{10.3}
\]

Thus $h_\epsilon(D)$ counts q1 quotient palette rows whose last *old*
provider is deleted.  It does not count providers that a simultaneous
rethread may add.

### Lemma 10.1 (every resident rethread hits every old motif)

Let `F'` be any `C_15`-invariant spanning degree-two factor selected from the
same complete edge-orbit catalogue, with no positive coordinate run shorter
than four, and set

\[
 D=F\setminus F'.                                     \tag{10.4}
\]

Then $D$ meets every $M\in\mathcal M$.

#### Proof

Suppose all edge orbits of one motif survive in `F'`.  In every developed
copy, its internal run vertices retain their two old incident edges, while
the two boundary edges still enter and leave through vertices omitting the
marked coordinate.  Degree two therefore forces the same local path

\[
 0,1^r,0,
 \qquad r<4.
\]

Edges changed outside the motif cannot alter this local trace.  Hence `F'`
still has a forbidden short run, a contradiction.  QED.

### Theorem 10.2 (palette-safe deletion no-go and certified optimum)

There is no $D\subseteq F$ such that

\[
 D\cap M\ne\varnothing\quad(M\in\mathcal M),
 \qquad h_-(D)=h_+(D)=0.                              \tag{10.5}
\]

More strongly, the retained exact finite optimization reports the
lexicographic optimum

\[
 \min_{D:\,D\cap M\ne\varnothing\ (M\in\mathcal M)}
       \bigl(h_-(D)+h_+(D),\ |D|\bigr)
   =(180,148).                                         \tag{10.6}
\]

One retained optimum has

\[
 h_-(D)=88,
 \qquad h_+(D)=92,
 \qquad |D|=148.                                      \tag{10.7}
\]

#### Proof of the zero-hole obstruction

An edge may belong to a zero-hole deletion set only if both its lower and
upper colours have another selected provider.  Exactly `36` selected edge
orbits have this property.  Of the `226` motifs, `186` contain none of these
edges.  A canonical locked motif is

\[
 \{1091,1406\}.                                       \tag{10.8}
\]

Edge `1091` is the unique selected provider of its upper colour and edge
`1406` is the unique selected provider of a different upper colour.  Hitting
(10.8) therefore creates an upper q1 hole.  This proves (10.5) directly.

For (10.6), the finite model has one Boolean deletion variable for each of
the `858` selected edge orbits, one hitting inequality for each of the `226`
motifs, and the exact indicators (10.3) for all `764+764` q1 palette rows.
It minimizes

\[
 1000\bigl(h_-(D)+h_+(D)\bigr)+|D|.                  \tag{10.9}
\]

Because `|D|<=858<1000`, this is exactly the lexicographic objective in
(10.6).  The retained optimum has objective `180148`, and the solver's best
bound is also `180148`; direct replay verifies every motif hit and the counts
(10.7).  This establishes (10.6) under the retained exact-solver
certificate.  The zero-hole statement itself was proved independently by
the locked motif (10.8).  QED.

The residence-only interval certificate separately gives a minimum motif
transversal of `147` edge orbits.  Thus one extra deletion is necessary to
attain the least possible old-palette damage, but even that best damage is
linear on the quotient scale.

### Corollary 10.3 (joint global rethread is mandatory)

Unconditionally, every fully resident and q1-complete equivariant rethread
must delete the whole old provider bank of at least one q1 colour and add a
new provider for it.  Under the certified optimum (10.6), its deleted old
set $F\setminus F'$ causes at least `180` lower-plus-upper q1 palette rows to
lose their last old provider.  These rows must be restored by edges of
$F'\setminus F$.  Since one new edge orbit supplies at most one lower and
one upper q1 row,

\[
 |F'\setminus F|\ge90.                                \tag{10.10}
\]

This does not rule out a resident double-q1 factor.  It rules out the staged
architecture

\[
 \text{palette-preserving residence deletions}
 \quad\longrightarrow\quad
 \text{later local completion}.                       \tag{10.11}
\]

The next search or construction must choose old deletions and new providers
simultaneously, while also enforcing degree two, connectivity/unit voltage,
absence of newly created short runs, and the later shadow/compiler rows.

The exact artifacts are

```text
scratch/k16_residence_motif_palette_safe_hitting_20260729.json
scratch/k16_residence_motif_minholes_hitting_20260729.json
scratch/k16_qfactor_q1_topresident_hamilton_20260729.motif_structure.audit.json
scratch/solve_k16_residence_motif_palette_safe_hitting_20260729.py
```

with respective SHA-256 values

```text
9c451d60839ba1085c64a37807d041c4fe2d0062ecc4285faded33f24e803780
7afddc14dfbd0daa825c6a19045e7d95c9e9bb745165bfb1145a2df76a354827
e76dbb6a8e5417c13ded8990f787a67c461912ba5931bd0093059a3e4330e9a8
0d87153ebba4577add71c376aeca94a181cb449483dc582550fd68db72be838d.
```

The optimization deliberately omits replacement edges, degree constraints,
connectivity, voltage, and newly created motifs.  Those omissions make
(10.6) a necessary old-edge damage bound for every equivariant rethread in
the complete quotient catalogue, not a sufficient construction and not a
global nonexistence certificate.  The two optimization JSONs record trusted
CP-SAT `INFEASIBLE`/`OPTIMAL` outcomes but do not contain a standalone UNSAT
core or proof log.  The primal `(88,92,148)` witness is independently
replayable; the lower bound `180148` relies on the recorded exact solver
bound.  By contrast, the locked-motif no-go and the residence-only
transversal value `147` have direct combinatorial certificates.

## 11. Coloured interval cuts, two-shore factors, and the fixed-cross no-go

The general reconstruction theorem is isolated in

```text
THREAD_A_COLOURED_INTERVAL_CUT_TWO_SHORE_FFACTOR_LEMMA_20260729.md
THREAD_A_TWO_SHORE_COLOURED_FFACTOR_LAMINAR_HALL_20260729.md.
```

If the residence motifs are cyclic intervals with an uncovered cycle point,
then after restricting allowed cut edges to `AA union BB` their nonempty
traces remain intervals.  Consequently

\[
 \tau_{AA\cup BB}=\nu_{AA\cup BB}.                    \tag{11.1}
\]

An all-same-shore minimum cut exists exactly when every motif has a
same-shore edge and the restricted-trace packing number equals the
unrestricted packing number.  At `k=16`,

\[
 \tau=\nu=\tau_{AA\cup BB}=147,                       \tag{11.2}
\]

and one certified minimum cut has sector split `(87,0,60)`.

Once a cross bank and a same-shore cut are fixed, immediate q1 and degree
completion split exactly into independent coloured `b`-factor problems on
the two shores.  Minimal-change demands are `b_sigma=d_(T_sigma)`;
from-scratch shore demands are `b_sigma=2-d_C`.  A palette bank followed by
Tutte's exact residual factor test is necessary and sufficient.  On a
genuine bipartite residual scaffold, the exact capacitated Hall cuts are

\[
 b'(X)-b'(Y)\le e(X,R\setminus Y),                    \tag{11.3}
\]

and the companion laminar Rado--Hall theorem supplies an automatically
extendible paired lower/upper provider bank.  Artificial in/out cloning of
the nonbipartite catalogue does not justify (11.3); its odd-set constraints
remain Tutte constraints.

Endpoint palette accessibility must already be imposed while choosing the
cut.  The canonical `(87,0,60)` cut has four lost lower colours and five lost
upper colours with no same-shore provider on exposed endpoints.  More
strongly, the joint radius-`147` model varies the cut over the complete
`476`-edge union of the `147` packed motifs, freezes all `80` `AB` edge
orbits, allows all `23218` off-seed nonloop same-shore seams, and enforces
degree two plus both q1 palettes.  It is `INFEASIBLE`.

Thus the exact fixed-cross conclusion is

\[
 \boxed{\text{every radius-147 rethread must alter the cross pattern;}
        \quad\text{otherwise radius}>147.}             \tag{11.4}
\]

The interval and factor theorems remain dimension-uniform.  The numerical
no-go is confined to this `k=16` loopless quotient-seam face.  Once a viable
joint cross/cut bank is found, connectivity, voltage, and newly created
boundary motifs are the remaining recoupling checks.  The nine
endpoint-accessibility failures are directly replayable; the global
`INFEASIBLE` status is a trusted exact CP-SAT record without a standalone
proof log.
