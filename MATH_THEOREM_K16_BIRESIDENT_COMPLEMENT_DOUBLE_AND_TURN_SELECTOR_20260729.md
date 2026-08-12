# The unrestricted `K=16` carrier: excess identities, complement doubling, and the exact turn-selector gate

Date: 2026-07-29  
Status: proved reductions and identities.  No `K=16` carrier is claimed.

## 0. Executive conclusion

There is no first-moment obstruction to a depth-four resident, double-`q1`
factor of `J(16,8)`.  In fact, for every coordinate which is nonconstant on
every factor component, double-`q1` coverage forces mean positive-run length
at least `9/2`.  Monochromatic components must be checked separately.  The
obstruction seen in the finite PBBS cores is therefore one of **run
arrangement/component geometry**, not total boundary supply.

There are two exact sufficient reductions of the unrestricted even problem
to objects on the odd ground set.  The weaker one uses two independent
rails.  The already certified positive-resident rank-eight `k=15` factor can
be retained unchanged; it is enough to find a positive-resident,
double-`q1` factor on rank seven.  No complement symmetry or zero-run
condition is needed for this independent second rail.

A stronger one-factor reduction is complement doubling.  Let `S=[15]`.  It
is enough to find a spanning 2-factor `G` of `J(S,7)` such that

1. every rank-six intersection colour occurs;
2. every rank-eight union colour occurs (and hence occurs exactly once);
3. every positive and every zero coordinate run has length at least four;
4. every component has length at least four.

Then `G`, on the shore containing the new coordinate, together with its
set-complement on the opposite shore, is the required factor of `J(16,8)`.

Moreover `G` is encoded by one map

\[
 p:\binom{[15]}8\longrightarrow\binom{[15]}2,
 \qquad p(U)\subset U.
\]

The degree equations, lower-rainbow condition, and residence condition are
stated exactly in Section 4.  This gives a clean symmetric missing lemma:

> **Resident turn-rainbow lemma at `(15,7,4)`.**  There is such a map `p`
> whose induced middle-levels 2-factor is turn-surjective and whose projected
> coordinate words have all one-runs and zero-runs of length at least four.

It is stronger than necessary.  The weakest source-relative target obtained
from the known `k=15` carrier is the facet-rail repair lemma in Section 4A.
Both are sufficient theorems for `K=16`, not necessary conditions on an
arbitrary factor of `J(16,8)`: they restrict to no-cross subclasses.  Inside
their stated subclasses the reductions are exact.

## 1. The even double-`q1` excess identity

Put

\[
 \mathcal M=\binom{[2m]}m,
 \quad W=|\mathcal M|,
 \quad N=\binom{2m}{m-1}=\binom{2m}{m+1},
 \quad C=W-N=\frac{W}{m+1}.
\]

Let `F` be a spanning 2-factor of `J(2m,m)`.  For an edge `e=XY`, write

\[
 c^-(e)=X\cap Y,
 \qquad c^+(e)=X\cup Y.
\]

Let `ell_R` and `u_U` be the loads of the lower and upper colours.  Assume
both palettes are covered, so

\[
 \delta_R=\ell_R-1\ge0,
 \qquad \epsilon_U=u_U-1\ge0.
\]

For a coordinate `x`, let `2b_x` be the number of selected edges crossing
the cut

\[
 \{X:x\in X\}\mid\{X:x\notin X\}.
\]

Thus `b_x` is the number of nonconstant positive runs of `x` (equivalently,
the number of nonconstant zero runs), aggregated over the factor cycles.

### Theorem 1.1 (boundary equals excess degree)

For every `x in [2m]`,

\[
 \boxed{
 \sum_{R\ni x}\delta_R=C-b_x,
 \qquad
 \sum_{U\ni x}\epsilon_U=b_x.}
 \tag{1.1}
\]

Consequently

\[
 0\le b_x\le C,
 \qquad
 \sum_x b_x=W.
 \tag{1.2}
\]

#### Proof

Exactly `W/2` middle vertices contain `x`.  If `I_x` is the number of
selected edges with both endpoints containing `x`, degree two gives

\[
 W=2I_x+2b_x,
 \qquad I_x=W/2-b_x.
\]

An edge has lower colour containing `x` exactly when both endpoints contain
`x`, whereas it has upper colour containing `x` when at least one endpoint
contains `x`.  Therefore

\[
 \sum_{R\ni x}\ell_R=W/2-b_x,
 \qquad
 \sum_{U\ni x}u_U=W/2+b_x.
\]

The baseline palette counts are

\[
 \binom{2m-1}{m-2}=W/2-C,
 \qquad
 \binom{2m-1}{m}=W/2.
\]

Subtracting them proves (1.1).  Nonnegativity proves the pointwise bounds.
Finally every selected Johnson edge crosses exactly two coordinate cuts, so
`sum_x 2b_x=2W`.  QED.

### Corollary 1.2 (the `K=16` supply margin)

At `m=8`,

\[
 W=12870,
 \qquad C=1430,
 \qquad b_x\le1430.
\]

There are `W/2=6435` middle vertices containing a fixed coordinate.  If that
coordinate is nonconstant on every factor component (in particular, if the
factor is connected), its positive runs therefore have mean length at least

\[
 \frac{W/2}{C}=\frac{m+1}{2}=\frac92.
 \tag{1.3}
\]

Monochromatic components must be checked separately; a monochromatic
triangle, for example, would violate depth four without contributing a cut
boundary.  In the connected case the required minimum four is below the
forced global mean.  Short runs can then persist only because the run mass
is unevenly distributed.

Equation (1.1) also identifies the excess designs.  The upper excess is a
rank-`m+1` multihypergraph of `C` blocks and degree sequence `(b_x)`; the
lower excess is a rank-`m-1` multihypergraph of `C` blocks and degree sequence
`(C-b_x)`.  In the simple complementary case, choosing a family `D` of `C`
upper blocks and the complements of those blocks below satisfies the moment
law automatically.

## 2. The odd upper-rainbow Catalan law

Let `n=2r+1` and let `G` be a spanning 2-factor of `J(n,r)`.  The number of
edges of `G`, the number of rank-`r` vertices, and the number of rank-`r+1`
upper colours are all

\[
 W_o=\binom{2r+1}r.
\]

Hence upper-colour coverage is automatically upper-colour **perfection**.

Let

\[
 C_r=\frac1{r+1}\binom{2r}r
\]

be the Catalan number.

### Theorem 2.1 (forced boundary count)

If every upper colour occurs, then every upper colour occurs exactly once
and, for every coordinate `x`,

\[
 \boxed{b_x=C_r.}
 \tag{2.1}
\]

The `x=1` shore has `r C_r` vertices and the `x=0` shore has `(r+1)C_r`
vertices.  If no factor component is monochromatic in `x`, its positive
runs therefore have mean `r` and its zero runs have mean `r+1`.

#### Proof

The first claim follows from equality of the number of edges and upper
colours.  A fixed coordinate belongs to

\[
 \binom{2r}{r-1}=rC_r
\]

rank-`r` vertices and to

\[
 \binom{2r}r=(r+1)C_r
\]

upper colours.  As in Theorem 1.1, the number of selected upper-coloured
edges containing `x` is `rC_r+b_x`.  Equating it to `(r+1)C_r` proves
(2.1).  QED.

For the odd factor needed below, `r=7`.  Thus each coordinate has exactly
`C_7=429` boundary pairs, `3003` positive vertices and `3432` zero vertices:
the forced means are exactly seven and eight.  Depth four again has ample
global margin.

## 3. Complement doubling

Let `S=[2m-1]` and add a new coordinate `z`.  Let `G` be a spanning 2-factor
of `J(S,m-1)`.  Make two copies of every vertex `X`:

\[
 B_X=X+z,
 \qquad A_X=S\setminus X.
\]

Both have size `m`, and the `A` and `B` families partition
`binom(S+z,m)`.  For every edge `XY` of `G`, select both edges

\[
 B_XB_Y,
 \qquad A_XA_Y.
 \tag{3.1}
\]

Call the resulting factor `D_z(G)`.

### Theorem 3.1 (complement-doubling lemma)

`D_z(G)` is a spanning 2-factor of `J(2m,m)`.  If `G` covers every
rank-`m-2` intersection and every rank-`m` union, then `D_z(G)` covers every
rank-`m-1` intersection and every rank-`m+1` union.

For an old coordinate `x in S`, the trace of `x` on the `B` copy is the
trace of `x` on `G`, while its trace on the `A` copy is the binary complement
of that trace.  The trace of `z` is constant one on every `B` component and
constant zero on every `A` component.  Consequently, if

* every one-run and zero-run of every old coordinate on `G` has length at
  least `s`, and
* every component of `G` has length at least `s`,

then every positive coordinate run of `D_z(G)` has length at least `s`.
The same hypotheses also give two-sided residence in the natural convention
where constant component traces are runs of the component length.

#### Proof

Adjacency and degree two are preserved by adjoining `z` and by complementing
inside `S`.  For an edge `XY` of `G`,

\[
\begin{array}{c|c|c}
 &\text{intersection}&\text{union}\\ \hline
B_XB_Y&(X\cap Y)+z&(X\cup Y)+z\\
A_XA_Y&S\setminus(X\cup Y)&S\setminus(X\cap Y).
\end{array}
\]

Thus the two old palettes of `G`, with and without complementation and `z`,
give all four even palettes.  The trace assertions are immediate from the
definitions.  QED.

### Corollary 3.2 (the exact `K=16` sufficient object)

A double-`q1`, bi-resident factor of `J(15,7)` with minimum run and component
length four produces a double-`q1`, resident factor of `J(16,8)`.

Conversely, every no-cross factor of `J(16,8)` which is invariant under the
involution

\[
 X+z\longleftrightarrow [15]\setminus X
\]

arises in this way.  Thus the reduction is exact in the complement-doubled
subclass.

### Theorem 3.3 (independent-rail lemma)

Let `A` be any spanning 2-factor of `J(S,m)` and `B` any spanning 2-factor
of `J(S,m-1)`.  On the two shores of `binom(S+z,m)`, select

\[
 A\quad\text{and}\quad B+z.                         \tag{3.2}
\]

This is a spanning 2-factor of `J(2m,m)`.  It covers both even `q1`
palettes if `A` and `B` each cover their own lower and upper `q1` palettes.
If both have positive coordinate runs of length at least `s`, and every
component of `B` has length at least `s`, then (3.2) has positive residence
at least `s`.

#### Proof

The shores partition the middle layer and each old Johnson edge remains a
Johnson edge after adjoining `z`.  Edges of `A` supply precisely the lower
and upper colours avoiding `z`; edges of `B+z` supply precisely those
containing `z`.  Old-coordinate traces are unchanged on both shores.  The
new coordinate is absent on `A` and constantly present on each `B`
component.  QED.

For `K=16`, the certified `k=15` rank-eight factor supplies `A`: it is
positive-resident at depth four and has complete lower and upper shadows.
Therefore the unrestricted factor problem needs only a positive-resident,
double-`q1` rank-seven factor `B`.  Requiring `B` to be the complement of
`A`, or requiring one factor to be bi-resident, is optional extra symmetry.

## 4. One-map turn-selector normal form

Continue with `n=2r+1`.  For every upper set

\[
 U\in\binom{[n]}{r+1},
\]

choose a pair `p(U) in binom(U,2)`.  It defines the Johnson edge

\[
 e_U=\{U\setminus\{a\},U\setminus\{b\}\},
 \qquad p(U)=\{a,b\}.
 \tag{4.1}

### Theorem 4.1 (turn-selector equivalence)

The edges `(e_U)` form a spanning 2-factor of `J(2r+1,r)` if and only if

\[
 \boxed{
 \#\{x\notin X:x\in p(X+x)\}=2
 \quad\text{for every }X\in\binom{[n]}r.}
 \tag{4.2}
\]

Their upper colours are then perfect automatically.  Their lower colours
are complete if and only if

\[
 \boxed{
 \forall R\in\binom{[n]}{r-1}\quad
 \exists\{a,b\}\subset[n]\setminus R:
 p(R+a+b)=\{a,b\}.}
 \tag{4.3}
\]

Equivalently, select in the middle-levels incidence graph between ranks `r`
and `r+1` the two incidences

\[
 U\setminus\{a\}\ --\ U,
 \qquad U\setminus\{b\}\ --\ U.
\]

Equation (4.2) says this is a 2-factor.  Condition (4.3) says that every
rank-`r-1` set occurs as the colour of a turn through an upper vertex.

#### Proof

At an upper vertex `U`, (4.1) selects exactly the two displayed middle
facets.  At a middle vertex `X`, a selected edge is incident precisely when
it comes from `U=X+x` and the omitted element `x` belongs to `p(U)`.  This
proves (4.2).  The intersection of the two endpoints of `e_U` is
`U\setminus p(U)`, proving (4.3).  QED.

Residence is now an exact property of the cycles generated by (4.1): read
the indicator of every coordinate on their rank-`r` vertices and forbid
cyclic words `0 1^j 0` and `1 0^j 1` for `1<=j<s`.  No phase variable or
even-shore chronology remains.

For `K=16`, use `(n,r,s)=(15,7,4)`.  There are 6,435 values `p(U)`, each with
28 possible pairs; equations (4.2) have one row per 7-set and (4.3) one row
per 6-set.  This is the unrestricted odd factor, not the prime-only quotient
or a fixed spiral.

## 4A. The facet derivative of the known `k=15` factor

There is a still smaller source-relative target.  Let `T=(T_i)` be a cyclic
factor on rank `r+1` of `[2r+1]`, and suppose its consecutive intersections

\[
 X_i=T_i\cap T_{i+1}                               \tag{4.4}
\]

enumerate every rank-`r` set exactly once.

### Theorem 4A.1 (turn derivative)

The `X_i` form a spanning 2-factor of `J(2r+1,r)`.  Its upper colours are
exactly the middle states `T_i`, once each.  Its lower colours are

\[
 X_i\cap X_{i+1}=T_i\cap T_{i+1}\cap T_{i+2}.      \tag{4.5}
\]

Consequently, if the depth-two lower shadow of `T` is complete, then `X` is
double-`q1` complete.  For every coordinate nonconstant on a source
component, a positive run of length `ell` in `T` becomes a positive run of
length `ell-1` in `X`.

#### Proof

Both `X_i` and `X_(i+1)` are distinct rank-`r` facets of `T_(i+1)`, so they
are Johnson adjacent and their union is `T_(i+1)`.  Their intersection is
(4.5).  On binary traces, (4.4) is adjacent AND: `ell` consecutive one
states give `ell-1` consecutive one edges.  QED.

There is an all-depth strengthening.  For every `q>=0`,

\[
 \bigcap_{j=0}^{q}X_{i+j}
   =\bigcap_{j=0}^{q+1}T_{i+j}.                       \tag{4.5a}
\]

If every positive run of `T` has length at least two, then for every
`q>=1`,

\[
 \bigcup_{j=0}^{q}X_{i+j}
   =\bigcup_{j=1}^{q}T_{i+j}.                         \tag{4.5b}
\]

Equation (4.5a) is immediate from \(X_j=T_j\cap T_{j+1}\).  For (4.5b),
each left-hand term lies in one of the interior `T` states.  Conversely, an
occurrence of a coordinate in an interior state belongs to the preceding
adjacent intersection, or, if it has just entered, to the following one
because its run has length at least two.  Thus a complete all-depth source
factor `T` has a complete all-depth turn derivative `X`: lower depth `q` of
`X` is lower depth `q+1` of `T`, while upper depth `q` of `X` is upper depth
`q-1` of `T`.

Apply this theorem to the audited `6390+45` cyclic source behind the optimal
`k=15` word.  The resulting rank-seven factor already has perfect upper
`q1`, complete lower `q1`, and complete shadows at every depth.  A direct
physical replay covers every subset of `[15]` in ranks zero through fifteen.
Its only positive-residence defects are

\[
 1425\text{ runs of length }3,                    \tag{4.6}
\]

all inherited from the source's 1,425 runs of length four on its large
component.  The 45-cycle contributes none.

Each bad run gives a four-edge closed collar.  The 1,425 physical collars
form 95 coordinate-rotation orbits on `Z_426`.  Their exact transversal
numbers are

\[
 \boxed{900\text{ physical edges}=60\text{ quotient edge orbits}.} \tag{4.7}
\]

This is the corrected facet-rail value independently audited in
`MATH_THEOREM_K_K15_TO_K16_LIFT5_FACET_Q2_AND_DENSE_B_BUDGET_20260729.md`;
it must not be confused with the complement-rail value `1230=82*15`.

The closed-collar argument is independent of how the replacement is found:
every resident spanning factor on the same rank-seven deck must delete at
least 900 edges of `B_0`.  Since both factors have 6,435 edges, it must add
at least 900 as well.  Hence every such repair has

\[
                 |E(B_0)\mathbin\triangle E(B')|\ge1800.       \tag{4.7a}
\]

Thus no bounded/local descent can prove `FRR(7,4)`; the first possible
repair is macroscopic, changing at least fourteen percent of the factor.

Thus the weakest explicit source-relative missing theorem is:

> **Facet-rail repair lemma `FRR(7,4)`.**  The factor `(X_i)` can be
> rethreaded, while retaining perfect upper colours and complete lower
> colours, so that every positive coordinate run has length at least four
> and every component has length at least four.

By Theorem 3.3, `FRR(7,4)` plus the unchanged rank-eight source factor gives
the requested resident, double-`q1` factor of `J(16,8)`.  This is strictly
weaker than `RTR(7,4)`: zero-runs of the repaired rank-seven factor are
irrelevant when the two even shores are chosen independently.

## 4B. The smallest sufficient source-relative trade theorem

Let `B_0` be the facet factor in Section 4A.  Its edges are indexed by their
perfect upper colours: write `e_U` for the unique selected edge with union
`U`.  Cut a set `H` of these edges.  Apart from an already-safe uncut cycle,
the retained graph is a family of paths.  At every path endpoint `v` and
coordinate `x`, let

\[
 \tau_x(v)\in\{1,2,3,4\}
\]

be the length, capped at four, of the terminal constant run seen inward from
that endpoint.

Call two endpoints `v,w` residence-compatible when they are Johnson
adjacent and, for every coordinate `x`,

\[
\begin{cases}
 \tau_x(v)+\tau_x(w)\ge4,&1_{x\in v}=1_{x\in w},\\
 \tau_x(v)\ge4\text{ and }\tau_x(w)\ge4,
     &1_{x\in v}\ne1_{x\in w}.
\end{cases}                                             \tag{4.8}
\]

### Theorem 4B.1 (rainbow collar rethreading)

Assume:

1. `H` meets the closed collar of every length-three run of `B_0`;
2. every retained path has at least four vertices;
3. there is a perfect matching `M` of all exposed endpoints such that every
   matched pair is residence-compatible;
4. the union colours of the edges in `M` are exactly the cut colours
   `{U:e_U in H}`, once each; and
5. the retained lower-colour occurrences together with the intersections
   of the edges in `M` cover every rank-six set.

Then

\[
                   (B_0-H)\cup M                         \tag{4.9}
\]

is a spanning double-`q1`, positive-depth-four 2-factor of `J(15,7)`.
Hence it completes the unrestricted `K=16` factor through Theorem 3.3.

#### Proof

A perfect matching of the exposed endpoints restores degree two.  Conditions
4 and 5 restore the two q1 palettes.  Every completed run internal to a
retained path is an old run whose collar was not wholly retained, so it has
length at least four.  A new run crossing one seam satisfies (4.8).  A new
run crossing two or more seams contains an entire intermediate path on which
the coordinate is constant; that path has length at least four by condition
2.  Thus every new run is safe.  QED.

This is a genuine reduction to a finite **rainbow endpoint matching**, not a
generic expansion claim.  There are `2|H|` endpoint vertices and `|H|`
distinct required upper colours.  A candidate matching edge is retained
only if it has the prescribed union colour, passes (4.8), and does not make
the lower-cover inequalities impossible.  Choosing one edge of every colour
while matching every endpoint is a three-index matching problem; ordinary
bipartite Hall alone is not sufficient.

The same gate has an exact signed-circulation form in the turn-selector
variables.  If `p_0(U)` is the old pair and `p(U)` the new pair, freezing
`p=p_0` off `H`, degree preservation is

\[
 \sum_{U\in H}\left(
   {\bf1}_{U-a_U}+{\bf1}_{U-b_U}
  -{\bf1}_{U-a_U^0}-{\bf1}_{U-b_U^0}\right)=0
 \quad\text{in }\mathbb Z^{\binom{[15]}7}.          \tag{4.10}
\]

The lower rows are

\[
 \ell_0(R)-\#\{U\in H:U\setminus p_0(U)=R\}
 +\#\{U\in H:U\setminus p(U)=R\}\ge1.             \tag{4.11}
\]

Every integral solution of (4.10) is an alternating-circuit packet in the
middle-levels incidence graph.  Equations (4.10)--(4.11), together with the
finite trace clauses, are therefore the exact quotient/flow formulation of
`FRR(7,4)`.

There is also a sharp q1 price at the minimum collar scale.  Among
`Z_15`-equivariant large-component cut sets of exactly `b` edge orbits which
hit all 95 collars, the minimum number of cut edge orbits carrying globally
load-one lower colours is

\[
\begin{array}{c|ccccc}
b&60&61&62&63&64\\ \hline
\text{forced unique lower-colour orbits}&12&11&10&9&8,
\end{array}                                             \tag{4.12}
\]

and it remains eight for `64<=b<=90`.  Thus an exact minimum 60-orbit
rethread must restore at least twelve distinct lower-colour orbits (180
physical colours), even before multiplicity-two/three colours whose every
provider is cut are charged.  The deterministic width-three cyclic DP and
witnesses are

```text
scratch/audit_k15_facet_rail_q1_rethread_frontier_20260729.py
scratch/k15_facet_rail_q1_rethread_frontier_20260729.audit.json
```

with SHA-256 values

```text
9cb5cf2418060d7750c448ae404643310e16c127c42400e51955f3695a053256  script
c80d81000f0da3ffa9d028f263ce374dd1d0e1a2a98af79c32e44e551fa8d4c0  output
```

Equation (4.12) is a necessary source-relative frontier, not a proof that
the endpoint matching in Theorem 4B.1 exists.

## 4C. Exact composite-equivariant quotient

The cyclic action of `Z_15` is free on ranks seven and eight: a nontrivial
stabilizer has orbit size three or five, so an invariant set has size a
multiple of three or five, never seven or eight.  Therefore an equivariant
turn selector is determined by

\[
 6435/15=429
\]

upper-orbit choices, each with `binom(8,2)=28` possible pairs.  Its exact
quotient system consists of

* 429 weighted degree-two rows on rank-seven orbits;
* 335 positive lower-cover rows on rank-six orbits (including the two
  size-five exceptional orbits); and
* the finite short-trace clauses of lengths at most five in the physical
  voltage lift.

No primality assumption is involved.  Rotation carries the trace of
coordinate `x` to the trace of coordinate `x+1`, so it is sufficient and
necessary to audit coordinate zero on every physical lifted component.
Every forbidden depth-four run projects to a labelled quotient walk of at
most four selected Johnson edges, and conversely every such lifted labelled
walk is a physical forbidden motif.  Thus residence is an exact bounded-path
constraint on the 429-vertex quotient factor, not an asymptotic condition;
monochromatic lifted components additionally require the explicit
voltage-length check.

This quotient is useful computationally and conceptually, but it is still
the integral turn-selector problem.  Freeness removes duplicate variables;
it does not make the degree/turn matrix totally unimodular or prove the
rainbow endpoint matching of Theorem 4B.1.

## 5. What is and is not a standard polynomial problem

Dropping the turn colours, (4.2) is an ordinary bipartite 2-factor problem
and is integral.  The turn colour at `U`, however, depends on the **pair** of
selected incidences at `U`.  Thus (4.3) is quadratic in the ordinary
middle-levels edge variables.

Equivalently, regard each possible pair `p(U)` as one coloured edge between
two rank-`r` facets.  One must choose

* exactly one edge of each upper colour `U`,
* degree exactly two at every middle vertex, and
* at least one edge of every lower turn colour `R`.

This is a doubly-rainbow 2-factor.  The ordinary b-matching theorem handles
the first two incidence degrees only after forgetting the pairing; ordinary
matroid parity handles paired elements under one matroid, not these two
simultaneous degree systems plus lower-colour covering.  Therefore no
standard matroid-parity theorem presently closes (4.2)--(4.3).

Two useful endpoints are already known:

* an MSW wreath factor has perfect upper colours and runs/gaps exactly
  `r/(r+1)`, but its lower turn map has holes;
* the centred PBBS factor has complete lower and upper turn support, but its
  coordinate run distribution has short gaps/runs.

The missing operation must combine MSW's run arrangement with PBBS's turn
surjectivity.

## 6. Exact missing lemma and the role of the finite core

### Resident turn-rainbow lemma (`RTR(r,s)`)

There is a map `p` satisfying (4.2) and (4.3) such that every induced factor
component has length at least `s` and every coordinate trace on every
component has all positive and zero runs of length at least `s`.

`RTR(7,4)` implies the desired unrestricted `K=16` carrier by Theorem 3.1.
More generally, `RTR(m-1,d(2m)+1)` supplies the complement-doubled even
carrier needed by the coefficient-one construction whenever the downstream
compiler accepts that carrier.

The symmetric difference of two solutions of (4.2), viewed in the
middle-levels incidence graph, is an Eulerian bipartite graph and decomposes
into alternating even circuits.  Hence a proof by transformation can be
stated entirely as:

> starting from the PBBS turn-surjective 2-factor, choose a family of
> alternating circuits which preserves (4.3) and eliminates every forbidden
> short trace.

The solver-free motif-390 certificate and the radius-three catalogue no-go
show that the required family need not contain a local improving circuit.
They do **not** obstruct `RTR(7,4)`: they concern one fixed overlay and a
finite local edge catalogue.  Their mathematical message is that the
alternating-circuit lemma must be global, or must construct `p` directly,
rather than descend one short run at a time.

The exact open alternatives are now sharply separated:

1. prove the weaker source-relative `FRR(7,4)`;
2. prove `RTR(7,4)` (or its all-`r` form) by a direct selector construction;
3. prove a global alternating-circuit smoothing theorem preserving the turn
   cover;
4. find a genuine dual obstruction to (4.2)--(4.3) plus residence.  The
   identities in Sections 1--2 rule out any obstruction based only on first
   moments or total run capacity.
