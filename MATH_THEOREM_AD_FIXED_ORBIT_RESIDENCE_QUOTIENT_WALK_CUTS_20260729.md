# Exact residence-four cuts on the fixed even edge-orbit catalogue

Date: 2026-07-29  
Lane: AD, fixed-orbit residence projection  
Status: proved integral formulation and exact symmetry census; no solver run.

## 0. Result and convention

Put

\[
 K=2r,\qquad n=K-1=2r-1,
\]

let `rho` rotate the `n` old coordinates and fix `z`, and let
`E_K` be the undirected physical edge-orbit catalogue of
`MATH_THEOREM_AD_CANONICAL_SECTION_COMPONENT_CATALOGUE_20260729.md`.
For `e in E_K`, write `E(e)` for its orbit of `n` physical Johnson edges
and let `y_e` be its selection bit.  The weighted quotient degree equations
decode `y` to a literal `rho`-invariant spanning simple two-factor `F_y`.

This note uses the **strict finite-cycle positive-residence convention**:
for every coordinate, each maximal cyclic one-run has at least four
vertices; a constant-one trace on a component of length `L` is one run of
length `L`.  Thus a constant-one triangle is forbidden.  Constant-zero
traces are irrelevant to one-sided positive residence.  Section 6 records
the bordered and two-sided variants explicitly.

The exact conclusion is:

1. residence at least four adds **no variables** to the `27,456`-variable
   `K=16` undirected catalogue;
2. it has an exact static quotient projection with `9,103,956` indexed
   clauses, or an exact lazy formulation by labelled quotient-walk no-goods
   of width at most four;
3. zero, nonunit, and unit component voltages, and arbitrary successor
   permutations, are all included.  In particular a short monochromatic
   physical lift is caught without a component-voltage selector;
4. combined with the already proved both-`q1` orbit rows, the complete
   factor + both-`q1` + positive-residence integer model has

   ```text
   binary variables                                  27,456
   weighted degree-two equations                        858
   lower-q1 cover rows                                  764
   upper-q1 cover rows                                  764
   strict positive-residence rows                 9,103,956
   total indexed rows                             9,106,342
   residence auxiliary variables                           0
   ```

The eager residence family is mathematically exact but unattractive for
SAT.  The lazy walk separator keeps the base at `2,386` rows and emits only
actual violated clauses.  No connectivity, opening, FRR collar, or literal
compiler conclusion is part of this theorem.

## 1. Physical strict residence as a shore-boundary condition

Fix a physical coordinate `a`.  Put

\[
 U_a=\{X\in\tbinom{[K]}r:a\in X\},\qquad H_a=J(K,r)[U_a].
\tag{1.1}
\]

For `S subseteq U_a`, let `delta_a(S)` be the set of physical Johnson
edges of `H_a` with exactly one endpoint in `S`.

### Theorem 1.1 (strict residence cut)

Let `F` be a spanning simple two-factor of `J(K,r)`.  The coordinate `a`
has every cyclic positive run of length at least four, under the strict
finite-cycle convention, if and only if

\[
             |F\cap\delta_a(S)|\ge1                 \tag{1.2}
\]

for every nonempty `H_a`-connected set `S` with `|S|<=3`.

#### Proof

The graph `F[U_a]` is a disjoint union of paths and cycles.  Its path
components are exactly the positive runs on mixed factor components.  A
factor component contained in `U_a` is a cycle component of `F[U_a]` and,
under the strict convention, is one constant positive run.  Hence residence
fails exactly when `F[U_a]` has a path or cycle component `P` with
`1<=|P|<=3`.  Taking `S=V(P)` gives a connected set with no selected
`H_a`-edge leaving it, so (1.2) fails.

Conversely, suppose (1.2) fails for nonempty `S`.  No selected edge of
`F[U_a]` joins `S` to `U_a\S`.  Therefore every component of `F[U_a]`
which meets `S` is contained in `S`; at least one such component exists and
has at most three vertices.  It is a forbidden positive run.  If a
disconnected `S` violated (1.2), its `H_a`-components would split the
nonnegative boundary count additively, and one connected component would
already violate it.  Thus connected sets suffice.  QED.

All three support sizes are necessary in the physical formulation: a run
of length `j=1,2,3` violates its size-`j` row while each nonempty proper
subpath has selected shore boundary.

## 2. Exact projection to the fixed orbit bits

For `e in E_K`, define the nonnegative integer

\[
 d_e(a,S)=|E(e)\cap\delta_a(S)|.                    \tag{2.1}
\]

Because selecting `y_e` selects all physical edges in `E(e)`, (1.2)
projects exactly to

\[
       \boxed{\ \sum_{e\in E_K}d_e(a,S)y_e\ge1\ }. \tag{2.2}
\]

For Boolean `y`, (2.2) is just the clause

\[
       \bigvee_{e:\ d_e(a,S)>0} y_e.                \tag{2.3}
\]

No coefficient-one assumption about physical incidences is being made:
a quotient-loop orbit can contribute two boundary edges at one physical
owner, and one edge orbit can meet the boundary at several vertices of
`S`.  In general

\[
                     0\le d_e(a,S)\le2|S|\le6.       \tag{2.4}
\]

The coefficient magnitude disappears only because the strict row has
right-hand side one and `y_e` is Boolean.  It must not be discarded in a
physical load ledger or in the bordered inequality of Section 6.

### Theorem 2.1 (orbit-projected completeness)

Let `y` satisfy the exact weighted degree-two equations of the canonical
catalogue.  Then `F_y` has strict positive residence at least four in every
coordinate if and only if (2.2), equivalently (2.3), holds for one
representative of every `rho`-orbit of pairs `(a,S)` occurring in
Theorem 1.1.

#### Proof

For every physical `a,S`, the left side of (2.2) is exactly
`|F_y cap delta_a(S)|`; Theorem 1.1 gives the equivalence before taking the
quotient.  Rotation sends `(a,S)` to `(rho a,rho S)`, fixes each selected
edge orbit as a set, and preserves (2.1).  Thus all rows in one rotation
orbit have the same left side, so one representative is necessary and
sufficient.  QED.

This proof contains no component-length or voltage hypothesis.  For
example, a selected quotient loop of order three may lift to physical
triangles.  If such a triangle is constant one in coordinate `a`, take its
three vertices for `S`; every selected edge is internal, so (2.2) has left
side zero.  Thus the usual monochromatic-cycle correction is already
present in the fixed physical-orbit rows.

## 3. Labelled quotient-walk form

Fix section representatives `U_i`, `i in [N]`, so every physical middle
state has the unique address `rho^s U_i`.  A labelled bracket walk of run
length `ell in {1,2,3}` is a cyclically simple physical sequence

\[
 X_0,X_1,\ldots,X_{\ell+1},\qquad
 X_t=\rho^{s_t}U_{i_t},                              \tag{3.1}
\]

with consecutive Johnson adjacency and a coordinate `a` such that

\[
 a\notin X_0\cup X_{\ell+1},\qquad
 a\in X_t\quad(1\le t\le\ell).                       \tag{3.2}
\]

Here **cyclically simple** means that all displayed edges and all displayed
vertices are distinct, except that `X_0=X_(ell+1)` is allowed when the
sequence is the complete simple cycle surrounding the run.  Put

\[
 e_t=[(i_t,i_{t+1},s_{t+1}-s_t)],\qquad
 \operatorname{supp}(P)=\{e_0,\ldots,e_\ell\},       \tag{3.3}
\]

where brackets forget dart orientation and repeated orbit IDs are retained
only once.  The exact walk no-good is

\[
 \boxed{\ \sum_{e\in\operatorname{supp}(P)}y_e
              \le |\operatorname{supp}(P)|-1\ }.     \tag{3.4}
\]

It has at most four literals.  For strict residence add the analogous
support no-good for every physical triangle all three of whose vertices
contain `a`; this is the constant-one case and has at most three literals.

### Theorem 3.1 (physical motif / quotient-walk equivalence)

On the weighted degree-two face, the following three systems have the same
integral feasible vectors `y`:

1. strict positive residence at least four in the literal lift;
2. all static projected rows (2.2);
3. all bracket-walk no-goods (3.4), together with the constant-one triangle
   no-goods.

#### Proof

Every short nonconstant physical run supplies (3.1)--(3.2), and every edge
orbit in its support is selected, so it violates (3.4).  A short constant
positive component in a simple two-factor can only be a triangle and
violates its triangle no-good.

Conversely, suppose all support variables of a bracket walk are selected.
Every displayed physical edge is then present because selection is by full
edge orbit.  At each internal state the two walk edges saturate physical
degree two, so the factor traverses the displayed positive states from the
absent entry state to the absent exit state.  This is a positive run of
length `ell<=3`.  If the walk closes, it is the corresponding complete
factor cycle.  Selecting every edge of an all-one triangle similarly forces
that triangle component.  Hence every violated no-good is a literal
residence failure.  The equivalence with (2.2) is Theorem 2.1.  QED.

The data `(i_t,s_t)` are a finite labelled quotient walk, not a bounded
component template.  Simultaneously adding one phase to all `s_t` and
rotating `a` gives the same rotation orbit of physical motifs.  For an old
coordinate one may canonically rotate it to coordinate zero; for `a=z`,
take one canonical phase translate of the address sequence.  This is an
exact projection even for zero or nonunit component voltage.

For general `K=2r`, a crude but rigorous bound on the number of indexed
nonconstant walk orbits is

\[
 N r^3\sum_{j=0}^{2}\bigl(r(r-1)\bigr)^j.             \tag{3.5}
\]

Indeed choose the absent start state modulo rotation, the inserted
coordinate, the entry deletion, each coordinate-retaining internal
Johnson transition, and the exit insertion.  This count includes
self-intersecting candidates and reversal/support duplicates, so it is an
upper bound rather than an exact deduplicated census.  At `K=16` it is

\[
 858\cdot512(1+56+56^2)=1,402,672,128.                \tag{3.6}
\]

The static rows of Section 4 are therefore the much smaller eager
aggregation; the width-four walk rows are preferable as lazy conflict cuts.

## 4. Exact `K=16` static row census

For any fixed physical coordinate, the positive shore is

\[
                       H_a\cong J(15,7).
\]

It has

\[
 |V|=\binom{15}{7}=6435,\qquad
 \Delta=7\cdot8=56,\qquad
 |E|=180180.                                          \tag{4.1}
\]

Its number of triangles is

\[
 T=\binom{15}{6}\binom93+\binom{15}{8}\binom83
   =780780.                                           \tag{4.2}
\]

There are `6435 binom(56,2)` centred wedges.  A nontriangle connected
triple is counted once and a triangle three times, so the number of distinct
connected triples is

\[
 6435\binom{56}{2}-2T=8,348,340.                      \tag{4.3}
\]

Thus one fixed coordinate has exactly

\[
 R_*=6435+180180+8,348,340=8,534,955                 \tag{4.4}
\]

indexed rows before possible equality of coefficient vectors.

### Old-coordinate rows

Rotation is regular on the fifteen old coordinate labels.  Consequently
the action on labelled pairs `(a,S)` with old `a` is free.  All old
coordinates together therefore give exactly `R_*` row orbits; equivalently
fix `a=0` and retain every connected `S` of size at most three.  Hence

\[
                     R_{\rm old}=8,534,955.            \tag{4.5}
\]

### Top-coordinate rows

For `a=z`, Burnside must be used because `z` is fixed.  Vertex and edge
actions are free, giving `6435/15=429` singleton orbits and
`180180/15=12012` edge orbits.

A connected triple can be fixed by a nonidentity rotation only for the two
elements `rho^5,rho^10` of order three.  Rotation by five partitions the
old coordinates into five 3-cycles.  A rank-seven set `X` is adjacent to
`rho^5X` exactly when one coordinate 3-cycle is partially occupied and the
other four are full or empty.  Its size is seven only when the partial
cycle contributes one point and exactly two other cycles are full.  Thus
there are

\[
                  5\cdot3\cdot\binom42=90             \tag{4.6}
\]

such vertices, forming `90/3=30` invariant triangles.  The same count
holds for `rho^10`; every other nonidentity element fixes no three-set of
vertices.  Burnside gives

\[
 R_{z,3}=\frac{8,348,340+30+30}{15}=556,560.          \tag{4.7}
\]

Therefore

\[
 R_z=429+12012+556560=569001.                         \tag{4.8}
\]

Combining (4.5) and (4.8), the exact indexed quotient-row count is

\[
 \boxed{R_{\rm res}=8,534,955+569,001=9,103,956.}     \tag{4.9}
\]

This is an exact count of the symmetry-reduced index family.  Distinct
indices can in principle yield the same Boolean support after edge-orbit
projection; no unsupported claim of irredundancy after that final
deduplication is made.  Every clause has width at most `164`: a connected
nontriangle triple has at most `3*56-2*2=164` physical shore-boundary
edges, while a triangle has `162`.  Hence a coarse rigorous eager bound is

\[
              9,103,956\cdot164=1,493,048,784         \tag{4.10}
\]

positive clause incidences before orbit-ID deduplication.  This confirms
that exact lazy separation is the appropriate SAT realization.

For reference, the number of indexed constant-one triangle motif orbits is

\[
 780780+\frac{780780+30+30}{15}=832836,               \tag{4.11}
\]

where the first term is the old-coordinate family and the second is the top
family.  These motifs are already included in the triple rows of (4.9).

## 5. Exact lazy decoder and separator

At an integral candidate `y` satisfying weighted degree two:

1. expand each of the `N` selected edge orbits through its `n` rotations;
2. traverse the resulting physical cycles;
3. scan the traces of one old-coordinate representative and of `z` for
   positive runs of lengths one, two, or three (scanning all `K`
   coordinates is equivalent but redundant);
4. for a nonconstant bad run emit (3.4); for a constant-one triangle emit
   its triangle support no-good.

The selected quotient multigraph has exactly `N` selected edge orbits even
when it contains quotient loops: summing the `N` degree-two equations gives
`2N`, and every selected undirected quotient edge, including a loop,
contributes two.  Its physical expansion therefore has exactly `nN=W`
selected edges.  Rotation transitivity on the old coordinates proves that
these two traces, across all rotated physical components, detect every old-
coordinate and top defect.  The direct all-coordinate separator runs in

\[
                         O(KW)                         \tag{5.1}
\]

time and `O(W)` memory; the symmetry-reduced two-coordinate separator runs
in `O(W)` time after the same `O(W)` physical decode.  Every emitted clause
has at most four negative literals.  Finiteness of the physical catalogue
and Theorem 3.1 prove that
iterating these cuts is an exact CEGAR scheme: a candidate is accepted if
and only if its literal lift is resident, and termination after finitely
many distinct cuts is guaranteed.  This is a mathematical exactness claim,
not a solver-performance claim.

## 6. Convention variants

### 6.1 Bordered-run convention

If a component constant in coordinate `a` is declared vacuously safe, let
`C_a(S)` be the physical coordinate-crossing edges from `S` to the negative
shore.  Exact bordered residence is

\[
 |F\cap C_a(S)|\le |F\cap\delta_a(S)|                \tag{6.1}
\]

for every connected `S subseteq U_a`, `1<=|S|<=3`.  Its quotient row is

\[
 \sum_e |E(e)\cap C_a(S)|y_e
 \le
 \sum_e d_e(a,S)y_e.                                 \tag{6.2}
\]

Unlike (2.2), the integer coefficients in (6.2) cannot be replaced merely
by their supports.  Equivalently, on the degree-two face one may use the
standard internal-plus-crossing row.  Bracket-walk cuts (3.4) without the
constant-triangle family give this convention exactly.

### 6.2 Two-sided residence

To require both one- and zero-runs to have length at least four, repeat
Theorem 2.1 on the negative shore for every coordinate.  Complementation
commutes with `rho` and identifies the positive and negative row censuses,
so the exact indexed count is

\[
                         2R_{\rm res}=18,207,912.      \tag{6.3}
\]

This doubling is necessary for genuine bi-residence; positive residence
alone does not control short zero-runs.

## 7. Combination with both `q1` and proved boundary

`MATH_THEOREM_AD_K16_CANONICAL_ORBIT_BOTH_Q1_ROWS_20260729.md` proves that
both literal `q1` palettes add exactly `764+764` support rows to the same
`27,456` variables.  Its two exceptional lower-with-`z` target orbits and
their upper complements have orbit size five and stabilizer coefficient
three:

\[
             \lambda(T)=3\sum_{e\in P(O)}y_e.         \tag{7.1}
\]

Thus their Boolean cover clauses still have coefficient one, but physical
loads do not.  Residence projection neither removes nor duplicates this
coefficient; the two ledgers share only the orbit variables.

Consequently the table in Section 0 is a complete integral model for
arbitrary equivariant factors satisfying both `q1` palettes and strict
positive residence four.  What is proved WLOG is only:

* the fixed physical edge-orbit catalogue;
* weighted degree two;
* the exact `q1` orbit-support rows with their physical stabilizer loads;
* the static or lazy residence systems above.

Not proved WLOG, and not imposed, are one quotient component, unit voltage,
a fixed successor order, a bounded shadow-width list, a fixed set of
residence motifs from one seed, or any FRR collar-rethread template.  The
new result is an exact carrier-level formulation, not a literal compiler or
splice theorem.

## 8. Audit checklist

The decisive points were checked independently within the proof as follows.

1. **Strict-cycle correction.**  Boundary-bracket motifs alone miss an
   all-one triangle; (1.2) and the explicit triangle no-good include it.
2. **Voltage scope.**  Rows are written on physical edge orbits, so a
   quotient component of any voltage is expanded literally; no periodic
   infinite-word convention is used.
3. **Loop coefficients.**  A quotient loop can meet one physical owner
   twice, hence (2.4); only the Boolean RHS-one clause forgets magnitude.
4. **Burnside correction.**  The top-coordinate triple family has sixty
   nonidentity fixed incidences, giving `556,560`, not
   `8,348,340/15`.
5. **Exceptional `q1` scope.**  Size-five target orbits have load
   coefficient three even though their cover rows are ordinary support
   clauses.
6. **Minimality wording.**  Residence adds the minimum possible number of
   auxiliary variables, namely zero.  No claim is made that the
   `9,103,956` projected row supports are irredundant after deduplication.
