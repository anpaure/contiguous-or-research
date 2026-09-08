# Strict balanced expansion under coherent orientation and the exact four-sector gate

Date: 2026-07-31  
Status: exact all-parameter reformulations and one inherited-sector
preservation theorem; complete finite orientation audits at parameters three
and four; the all-parameter integral preservation theorem remains open.

## 0. Verdict

Strict balanced expansion (SBE) is not a property of an undirected Catalan
forest alone.  It depends on which endpoint of every path is declared final.
That dependence has an exact form.

For either strict occurrence shore, a family of outer colours with middle
neighbourhood `S` obeys SBE exactly when

\[
 n\kappa+(4n+2)|S\cap Z|\ \ge\ n\delta+2|S|,                 \tag{0.1}
\]

where `Z` is the chosen terminal bank,

\[
 \delta=\sum_{v\in S}(2-d_F(v))
\]

is the number of path-end incidences in `S`, and `kappa` is the unused
occurrence capacity of `S`.  Choosing the two ends of every nontrivial path
with weight one half turns (0.1) into

\[
 \boxed{\quad n\kappa+(n+1)\delta\ge2|S|.\quad}              \tag{0.2}
\]

The half-endpoint point passes both shores on every authenticated chained
forest at parameters `n=3,4,5,6,7`.  It is nevertheless not integrally
roundable in general: on the authenticated parameter-three seed no coherent
orientation passes even one shore.  Two explicit co-singleton cuts force
opposite orientations of the same path.  Thus a generic generalized-
polymatroid or Frank-orientation argument cannot close preservation.

The first strict lift repairs the gap.  The authenticated parameter-four
output has `475` both-SBE orientations among its `2^10=1024` distinct
coherent orientations.  A second, independently produced lift from a
both-SBE parameter-three parent has `356/1024` both-SBE orientations.

At the recursive level, one of the four outer sectors on each shore is an
isomorphic copy of the parent SBE graph, with weaker next-parameter weights;
that sector is preserved unconditionally.  The remaining obstruction is
exactly three cross-sector overlap charges.  The stored parameter-four bad
orientation passes SBE on every proper collection of sectors but fails when
all four are enabled.  Hence sectorwise, pairwise, and even three-sector
preservation are insufficient; the missing statement is genuinely one
four-sector integral-correlation theorem.

## 1. Exact occurrence-slack identity

Use the notation of
`MATH_THEOREM_CATALAN_STRICT_BALANCED_EXPANSION_COMMON_BASIS_20260731.md`:

\[
 M=\binom{2n}{n},\quad N=\binom{2n}{n-1},\quad
 P=\binom{2n}{n-2},\quad C=M-P,\quad R=N-C.             \tag{1.1}
\]

Fix either strict occurrence graph.  Let `mathcal U` be an outer family and
put `S=N(mathcal U)`.  For `v in S`, let `a_v` be the number of occurrence
edges from `mathcal U` to `v`, retaining occurrence multiplicity.  The exact
degree law gives

\[
 c_v:=d_G(v)=n-d_F(v).
\]

Define

\[
 \kappa=\sum_{v\in S}(c_v-a_v),\qquad
 \delta=\sum_{v\in S}(2-d_F(v)).                       \tag{1.2}
\]

Every outer vertex has `n+2` occurrences, so

\[
 (n+2)|\mathcal U|
 =\sum_{v\in S}a_v
 =(n-2)|S|+\delta-\kappa.                              \tag{1.3}
\]

For a coherent orientation, let `Z` be the endpoint omitted from the
oriented endpoint image: heads on the upper shore, tails on the lower shore.
The SBE capacity of `S` is

\[
 y_Z(S)={R\over N}|S|+{C\over N}|S\cap Z|.             \tag{1.4}
\]

The parameter identities give

\[
 {C\over N}={4n+2\over n(n+2)},\qquad
 {R\over N}={n^2-2n-2\over n(n+2)}.                   \tag{1.5}
\]

Substituting (1.3) into (1.4) yields the exact identity

\[
 y_Z(S)-|\mathcal U|
 ={n\kappa+(4n+2)|S\cap Z|-n\delta-2|S|
    \over n(n+2)}.                                    \tag{1.6}
\]

This proves (0.1).

### Corollary 1.1 (half-endpoint point)

Give each endpoint of a nontrivial path terminal weight one half and each
isolated vertex terminal weight one.  The expected terminal order in `S` is
exactly `delta/2`.  Hence its SBE slack is

\[
 {n\kappa+(n+1)\delta-2|S|\over n(n+2)},              \tag{1.7}
\]

proving (0.2).

Equivalently, the fractional primal load is

\[
 \bar y(v)=1-{C\over2N}d_F(v),                         \tag{1.8}
\]

and the complementary dual load is `C d_F(v)/(2N)`.  Thus the half point
puts equal dual mass on the two incidences of every child edge.

### Corollary 1.2 (orientation-independent sufficient condition)

Let `chi_F(S)` count nontrivial paths having exactly one endpoint in `S`.
The least possible terminal count in `S`, over all coherent orientations,
is

\[
 \min_Z|S\cap Z|={\delta-\chi_F(S)\over2}.             \tag{1.9}
\]

Consequently every coherent orientation is SBE on the shore if and only if

\[
 \boxed{\quad
 n\kappa+(n+1)\delta\ge2|S|+(2n+1)\chi_F(S)
 \quad}                                                \tag{1.10}
\]

for every outer family.  This stronger robust-SBE condition is useful but
is not asserted for every Catalan forest.

## 2. Exact endpoint-orientation cut system

For a middle family `S`, define its outer closure

\[
 \mathcal O^\pm(S)=\{w:N_{G^\pm}(w)\subseteq S\},
 \qquad
 \Phi^\pm(S)=N|\mathcal O^\pm(S)|-R|S|.               \tag{2.1}
\]

It is enough to test outer families of the form `mathcal O(S)`: once `S`
is fixed, including every available outer vertex only increases the left
side without changing the neighbourhood.  Therefore a coherent orientation
with head set `H` and tail set `T` is both-SBE exactly when

\[
 C|H\cap S|\ge\Phi^-(S),\qquad
 C|T\cap S|\ge\Phi^+(S)                               \tag{2.2}
\]

for every `S subseteq X`.

The function `Phi` is supermodular.  Indeed,

\[
 \mathcal O(S\cap T)=\mathcal O(S)\cap\mathcal O(T),
 \qquad
 \mathcal O(S\cup T)\supseteq\mathcal O(S)\cup\mathcal O(T),
\]

and `-|S|` is modular.

Let `E` be the nontrivial path endpoints and `I` the isolated vertices.
Eliminating all non-endpoint coordinates gives

\[
 \Psi^\pm(A)=
 \max_{S:\,S\cap E=A}
 \bigl(\Phi^\pm(S)-C|I\cap S|\bigr),\qquad A\subseteq E.       \tag{2.3}
\]

Partial maximization preserves supermodularity, so each `Psi` is
supermodular.  The integral orientation constraints, however, are

\[
 |H\cap A|\ge p^-(A),\qquad |T\cap A|\ge p^+(A),
 \qquad
 p^\pm(A)=\max\left\{0,\left\lceil{\Psi^\pm(A)\over C}\right\rceil\right\}.
                                                               \tag{2.4}
\]

The ceiling in (2.4) need not preserve crossing supermodularity.  Even one
shore is therefore not automatically an instance of Frank's integral
orientation theorem, and coupling the head and tail systems adds a third
partition-base constraint.

## 3. The parameter-three rounding obstruction

The authenticated parameter-three seed has three nontrivial endpoint pairs

\[
 (19,49),\qquad(13,28),\qquad(37,41),                         \tag{3.1}
\]

and isolated vertices `26,38`.  Index the six displayed endpoints in the
displayed order.  On the upper shore the two endpoint sets

\[
 A_1=E\setminus\{28\},\qquad A_2=E\setminus\{13\}             \tag{3.2}
\]

both have demand three.  Since exactly three heads are chosen, the first
constraint says that `28` is not a head and the second says that `13` is
not a head.  They are the two ends of one path, a contradiction.  The lower
shore has the identical obstruction on the pair `(19,49)`.

The raw endpoint demands `p` have `96` violations of supermodularity on
each shore.  Nevertheless the half-endpoint point satisfies every raw
weighted inequality exactly.  This is a literal fractional/integral gap,
not a missing application of a standard orientation theorem.

Exhausting all `2^3=8` distinct coherent orientations confirms that neither
shore is SBE.  This also explains why the original stored orientation had
scaled violations `(11,4)`: changing orientation cannot repair that seed.

## 4. Regeneration under a suitable first lift

The authenticated strict output at parameter four has ten nontrivial paths
and four isolates.  Exhausting its `2^10=1024` distinct orientations gives

\[
 \begin{array}{c|r}
 \text{property}&\text{orientations}\\ \hline
 \text{upper SBE}&569\\
 \text{lower SBE}&786\\
 \text{both SBE}&475.
 \end{array}                                                \tag{4.1}
\]

The stored orientation was upper-deficient by fourteen, but reversing one
nontrivial path makes both violations zero.

Independently, the complete parameter-three census contains a both-SBE
parent with a literal strict physical extension.  Reconstructing its
parameter-four child gives `356/1024` both-SBE orientations.  Thus suitable
SBE-to-SBE preservation is realized in two unrelated first-step fixtures;
the failure of the original parameter-three orientation is not inherited.

For the stored chain, exact min-cut replay of the half-endpoint point gives
zero violation on both shores at every parameter `3,4,5,6,7`.  The stored
orientations themselves are both-SBE at `n=5,6,7`.

## 5. Four-sector transformation

Consider one strict lift from parameter `n` to `n+1`, with new coordinates
`c,z`.  Split both the next outer shore and the next middle shore according
to their intersection with `{c,z}`, encoded by `0,1,2,3`.

For the upper occurrence graph, the possible middle sectors reached from
each outer sector are

\[
 0\to\{0\},\qquad
 1\to\{1\},\qquad
 2\to\{0,2\},\qquad
 3\to\{1,2,3\}.                                      \tag{5.1}
\]

For the lower graph they are

\[
 0\to\{0,1,2\},\qquad
 1\to\{1\},\qquad
 2\to\{2,3\},\qquad
 3\to\{3\}.                                         \tag{5.2}
\]

These relations follow directly from the five edge families: the isolated
`c`-rail, the punctured `z`-rail, the two pure sides, and the two seam
families.  In particular every middle sector has at most two source
sectors.  The three source-overlap links are

\[
 \begin{array}{c|c}
 \text{upper}&(0,2),(1,3),(2,3)\\
 \text{lower}&(0,1),(0,2),(2,3).
 \end{array}                                           \tag{5.3}
\]

Let `S_ij(mathcal U_i)` be the middle-sector-`j` neighbourhood generated by
outer family `mathcal U_i`, and let `y'` be the next SBE capacity.  Define
the separate sector slack

\[
 \sigma_i=y'\!\left(\bigcup_jS_{ij}\right)-|\mathcal U_i|.
                                                               \tag{5.4}
\]

Because there are no triple feeders, inclusion-exclusion is exact:

\[
 y'\!\left(N\left(\bigcup_i\mathcal U_i\right)\right)
 -\sum_i|\mathcal U_i|
 =\sum_i\sigma_i-
   \sum_{(a,b)\in L}y'(S_{aj}\cap S_{bj}),             \tag{5.5}
\]

where each link `(a,b)` uses its unique shared middle sector `j`, and `L`
is the appropriate three-edge set in (5.3).

Thus next-stage SBE is exactly a four-sector overlap budget: the individual
sector slacks must pay the three duplicated-neighbour capacities.

### Theorem 5.1 (the inherited `c` sector preserves SBE)

On both shores, sector `1` is an isomorphic copy of the parent's strict
occurrence graph.  For example on the upper shore,

\[
 N_{G'^{-}}(c+A)=c+N_{G^-}(A).                         \tag{5.6}
\]

The extra occurrence obtained by deleting `c` is precisely the chosen side
representative and duplicates an already present simple neighbour.  The
lower statement is its deletion dual.

Write `alpha_n=R_n/N_n` and `beta_n=1-alpha_n`.  Direct calculation gives

\[
 \beta_n-\beta_{n+1}
 ={2(2n^2+4n+3)\over n(n+1)(n+2)(n+3)}>0.             \tag{5.7}
\]

Hence `alpha_(n+1)>alpha_n`.  If the isolated `c`-rail is oriented as its
SBE parent, then for every parent neighbourhood with `m` vertices and `z`
terminals,

\[
 \alpha_{n+1}(m-z)+z\ge\alpha_n(m-z)+z.               \tag{5.8}
\]

Parent SBE therefore proves SBE on the copied sector without any condition
on `Q` or either side representative.

### Proposition 5.2 (proper-sector checks do not preserve SBE)

For the stored parameter-four bad orientation, exact min-cut separation
passes on every nonempty proper subset of the four outer sectors—each
single sector, every pair, and every triple.  Enabling all four sectors
produces the scaled upper violation fourteen, with outer-sector counts

\[
                         (1,1,6,10).                  \tag{5.9}
\]

Thus no theorem checking the four sectors separately, pairwise, or only
three at a time can prove preservation.  The three overlap charges in
(5.5) must be controlled jointly.

## 6. Correct preservation target

The common-basis distribution supplied by parent SBE gives exact uniform
marginals for `Q`.  It can average any additive edge risk, but the overlap
charges in (5.5) and the endpoint rounding constraints (2.2) are not
additive.  The exact remaining statement is therefore:

> **Balanced four-sector DERF orientation theorem.**  From an SBE structural
> parent, choose one strict common basis, both representative systems, the
> physical graphic completion, and coherent orientations of the resulting
> paths so that the three overlap charges in (5.5) are paid on both shores.

Theorem 5.1 removes one sector on both shores.  Equations (1.6), (2.2), and
(5.5) are exact polynomial checking criteria for every fixed integral
choice.  What remains is integral correlation of the three controllable
sectors; it is not another one-shore Hall theorem.

The finite evidence supports existence, but no all-parameter proof is
claimed here.

## 7. Independent replay

The finite assertions in Sections 3--5 are replayed by

```text
scratch/audit_catalan_sbe_orientation_sector_gate_20260731.py
scratch/catalan_sbe_orientation_sector_gate_20260731.audit.json
```

At freeze time their SHA-256 hashes are respectively

```text
0e0e69cf25a394ed6aed83c15fa7b31f516828ba68283ce230783be82c7cda2a
71239ba961afc3974d57ab650170abf80c98b6ca87bfe37d811312a923f6ca98
```

and the JSON canonical payload hash is

```text
b7eb615710f19bcb30e74bdf2c03204b2c51a1c68e4ebc4d9b434c73e9eb55af
```

The replay reconstructs both occurrence graphs, checks the half-endpoint
min-cuts at `n=3,...,7`, exhausts the distinct orientations at `n=3,4`,
reconstructs the independent census child, verifies the two raw endpoint
demand functions and their rounded failures, tests all fifteen nonempty
sector collections, and verifies the copied-parent adjacency identity on
both shores in every stored lift.
