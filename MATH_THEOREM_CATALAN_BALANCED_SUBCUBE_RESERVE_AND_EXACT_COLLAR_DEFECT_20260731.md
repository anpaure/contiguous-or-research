# A balanced subcube reserve and its exact collar defect

Date: 2026-07-31  
Status: exact all-`m` recursive reserve embedding, exact fractional loads,
and exact complement-collar deficit; no integral collar braid

## 0. Verdict

The `p=m^(-1/3)` residual need not be an unstructured random induced
hypergraph.  There is a deterministic balanced reserve of exactly that
scale which automatically excludes every four-resource space barrier:
fix a balanced pattern on `2a` coordinates.  The induced ordered-diamond
hypergraph is literally the full problem at parameter `m-a`.

For

```text
a=(1/6+o(1)) log_2 m,
```

its outer size is `Theta(m^(-1/3)N_m)`.  It has the exact uniform fractional
matching inherited from the smaller Boolean lattice.

Deleting this reserve from the ambient hypergraph has a remarkably local
effect.  Every outer vertex outside a two-coordinate trace collar retains
its full atom star.  A first-collar vertex loses exactly `2m` of its
`m(m+1)` ordered atoms, while a second-collar vertex loses exactly two.
Thus the ambient uniform fractional weighting leaves the respective exact
deficits

```text
2/(m+1),             2/[m(m+1)]
```

and zero deficit elsewhere.  The two collars have only
`a M_(m-a)+binom(a,2)N_(m-a)` vertices on each outer shore.  Thus the global
four-resource capacity problem is reduced to an explicit radius-two trace
braid around an exact recursive core.

This does not yet prove the construction: the fractional collar deficit
must be rerouted integrally while preserving middle capacities and physical
acyclicity.  It replaces an arbitrary logarithmic-degree residual theorem
by a much more structured recursive interface.

## 1. The balanced central subcube

Let the ground set split as

```text
[2m]=C disjoint_union R,       |C|=2a,       |R|=2m',
m'=m-a,
```

and fix one `a`-set `A subset C`.  Define

```text
L_A={A union L': L' in C(R,m'-1)},
X_A={A union X': X' in C(R,m')},
U_A={A union U': U' in C(R,m'+1)}.
```

The two middle roles use separate copies of `X_A`.

### Theorem 1.1 (exact recursive reserve)

The ordered-diamond hypergraph induced by

```text
L_A, U_A, (X_A)_T, (X_A)_H
```

is canonically isomorphic to the full ordered-diamond hypergraph at
parameter `m'` on ground set `R`.

### Proof

Every induced atom has the form

```text
(A+L', A+U', A+T', A+H'),
```

and deleting the common set `A` preserves the identities

```text
L'=T' intersect H',          U'=T' union H'.
```

Conversely every ordered diamond on `R` lifts by adjoining `A` to all four
resources.  The maps are inverse.  `square`

Write

```text
N_j=binom(2j,j-1)=j Cat_j,       M_j=binom(2j,j)=(j+1)Cat_j.
```

The reserve therefore has outer order `N_(m')` and middle-role order
`M_(m')`.

### Proposition 1.2 (complete trace quotient)

For a fixed collar trace `S subset C`, write

```text
j=|S|-a.
```

The numbers of resources with exactly this trace are

```text
ell_j = binom(2m',m'-1-j),
x_j   = binom(2m',m'-j),
u_j   = binom(2m',m'+1-j).                              (1.1)
```

They satisfy `u_j=ell_(-j)` and `x_j=x_(-j)`.

Every atom from lower trace `S` to upper trace `S union Z`, where
`Z subset C-S` and `z=|Z|<=2`, adds exactly `2-z` outside coordinates.
For each fixed lower resource the number of ordered atoms of this trace
type is

```text
2 binom(m'+1+j,2-z),                                     (1.2)
```

and for each fixed upper resource it is

```text
2 binom(m'+1-j-z,2-z).                                   (1.3)
```

The two middle traces are:

```text
z=0: S,S;
z=1: S,S union Z;
z=2: S union {z_1}, S union {z_2}.                       (1.4)
```

### Proof

The outside ranks are forced by the total ranks, giving (1.1).  An atom
adds two coordinates.  Once its `z` collar additions are fixed, choose the
other `2-z` from the `m'+1+j` outside coordinates absent from the lower
set; either ordering of the two added coordinates gives an ordered atom.
This proves (1.2).  Counting deleted outside coordinates from the upper set
gives (1.3).  Formula (1.4) is literal.  `square`

This quotient contains all rank and resource information needed for a
finite collar braid; its number of trace states is `2^(2a)=m^(1/3+o(1))`
at the chosen scale.

## 2. Exact scale and fractional capacity

### Proposition 2.1 (reserve density)

If `a=o(m)`, then

```text
N_(m-a)/N_m
 =4^(-a) sqrt(m/(m-a)) (1+O(a^2/m)).                     (2.1)
```

Consequently `a=(1/6+o(1))log_2 m` gives reserve density
`Theta(m^(-1/3))`.

### Proof

Use `N_j=j Cat_j` and the uniform Catalan ratio

```text
Cat_(m-a)/Cat_m
 =4^(-a)(m/(m-a))^(3/2)(1+O(a^2/m)),
```

which follows directly from the factorial product or Stirling's formula.
Multiplication by `(m-a)/m` gives (2.1).  `square`

### Proposition 2.2 (exact fractional interior)

Give every ordered atom of the reserve weight

```text
w=1/[m'(m'+1)].                                           (2.2)
```

Then every reserve outer resource has load one and every reserve middle
resource in either role has load

```text
m'/(m'+1)<1.                                              (2.3)
```

### Proof

In the parameter-`m'` ordered-diamond hypergraph, every lower or upper
resource has degree `m'(m'+1)`, while every fixed tail or head resource has
degree `m'^2`.  Equations (2.2)--(2.3) follow.  `square`

Thus the reserve lies exactly in the four-resource fractional polytope; the
space barrier from
`MATH_THEOREM_CATALAN_LOG_RESIDUAL_OUTER_HALL_AND_SPACE_BARRIER_20260731.md`
cannot occur inside it.

## 3. Which ambient resources interact with the reserve?

For any ambient set `S`, call `S intersect C` its collar trace.

### Lemma 3.1 (two-coordinate locality)

An outer resource outside the reserve shares an ambient atom with some
reserve resource only in the following cases:

```text
lower trace: A-S         with 1<=|S|<=2;
upper trace: A+Z         with 1<=|Z|<=2.
```

The width-one cases touch a reserve middle resource; the width-two cases
touch a reserve outer resource.  Conversely every displayed collar vertex
has atoms meeting the reserve.

### Proof

An atom adds exactly two coordinates to its lower trace.  To meet a reserve
middle trace `A`, the lower trace must be `A` or `A-{c}`.  To meet a reserve
upper trace `A`, it may additionally be `A-{c,d}`.  Trace `A` itself is the
reserve lower class.  The upper statement is dual.  Adding the one or two
missing collar coordinates, or deleting the one or two extras, proves the
converse.  `square`

Equivalently, in the trace quotient of Proposition 1.2 an atom touches the
reserve if and only if at least one of the following holds:

```text
(i)   S=A;                                      (reserved lower)
(ii)  S union Z=A;                              (reserved upper)
(iii) S=A-{c} and c in Z.                       (reserved middle)
```

Here `|Z|<=2`; overlaps among the three rows are allowed.  This is the
complete crossing-atom catalogue.

There are exactly

```text
a M_(m')                  first-collar vertices,
binom(a,2) N_(m')         second-collar vertices           (3.1)
```

on each outer shore.  At trace distance one the outside part has rank `m'`;
at trace distance two it has rank `m'+1` on the lower shore or `m'-1` on
the upper shore, both counted by `N_(m')`.

## 4. Exact deficit of the uniform complement weighting

Delete every atom touching any reserve resource, and give each remaining
ambient atom the full-system uniform weight

```text
w_m=1/[m(m+1)].                                           (4.1)
```

### Theorem 4.1 (all fractional damage is within radius two)

Every nonreserve outer resource outside the collar of Lemma 3.1 has load
exactly one.  Every first-collar lower or upper resource has load

```text
(m-1)/(m+1)=1-2/(m+1).                                   (4.2)
```

Every second-collar outer resource has load

```text
1-2/[m(m+1)].                                             (4.3)
```

Every nonreserve middle resource has load at most `m/(m+1)`.

### Proof

A noncollar outer resource has no incident atom meeting a reserve resource,
by Lemma 3.1 and its dual, so it retains all `m(m+1)` ordered atoms and has
load one.

Let a lower collar set have trace `A-{c}`.  An incident atom is deleted
exactly when one of its two added coordinates is `c`: then one intermediate
middle set has trace `A`.  There are `m` choices for the other added
coordinate and two orientations, hence exactly `2m` deleted ordered atoms.
Its retained degree is

```text
m(m+1)-2m=m(m-1),
```

which gives (4.2).  For an upper collar set of trace `A+{z}`, the dual count
chooses `z` as one deleted coordinate and any of the other `m` coordinates
as the second, again losing exactly `2m` ordered atoms.

For a lower second-collar trace `A-{c,d}`, the only deleted unordered
diamond adds precisely `{c,d}` and reaches a reserve upper resource.  Its
two orientations are the only lost ordered atoms, giving (4.3).  The upper
second-collar count is dual.

A middle resource had full weighted load `m/(m+1)` and deleting atoms can
only reduce it.  `square`

### Corollary 4.2 (total collar debt)

The exact missing outer mass on each shore is

```text
Delta_collar
 =2a M_(m-a)/(m+1)
  +2 binom(a,2)N_(m-a)/[m(m+1)].                          (4.4)
```

For `a=(1/6+o(1))log_2 m`, this is

```text
Theta(N_m log m/m^(4/3))=Theta(Cat_m log m/m^(1/3)).       (4.5)
```

All nonreserve middle vertices retain slack at least `1/(m+1)` under the
uncorrected weighting.

## 5. An explicit fractional collar completion

The radius-two debt has a uniform three-edge detour.  This proves that the
complement has no fractional space barrier once `a>=3`.

Put `B=C-A` and `n=m'=m-a`.  Start from the uniform weight
`w_0=1/[m(m+1)]` on every ordered atom avoiding the reserve.

### First-collar paths

Choose

```text
d in A,       z in B,       e in A-{d},
X,Y in C(R,n),       |X-Y|=|Y-X|=1,
```

and write `V=X union Y`.  The following is an alternating outer path:

```text
L_0=(A-{d})+X,
U_0=(A-{d}+{z})+V,
L_1=(A-{d,e}+{z})+Y,
U_1=(A+{z})+Y.                                           (5.1)
```

The positive edges are `L_0U_0,L_1U_1`; the negative edge is `L_1U_0`.
All four outer resources and all atoms avoid the reserve.  Give every such
path coefficient

```text
alpha_1=2/[(m+1)a(a-1)n^2].                             (5.2)
```

A fixed first-collar endpoint belongs to exactly `a(a-1)n^2` paths, so its
added load is `2/(m+1)`, exactly its deficit.

### Second-collar paths

Choose

```text
D in C(A,2),       Z in C(B,2),
Y subset X subset R,       |Y|=n-1, |X|=n+1.
```

Then

```text
L_0=(A-D)+X,
U_0=(A-D+Z)+X,
L_1=(A-D+Z)+Y,
U_1=(A+Z)+Y                                             (5.3)
```

is another reserve-avoiding alternating three-edge path.  Give it
coefficient

```text
alpha_2
 =2/[m(m+1) binom(a,2) binom(n+1,2)].                    (5.4)
```

Every second-collar endpoint lies in exactly
`binom(a,2)binom(n+1,2)` such paths, so its added load is precisely
`2/[m(m+1)]`.

For each path, add half its coefficient to each orientation of its two
positive diamonds and subtract half from each orientation of its negative
diamond.

### Theorem 5.1 (fractional complement theorem)

If `a>=3` and `m-a>=1`, the modified weights are nonnegative, cover every
nonreserve lower and upper resource with load exactly one, and give every
nonreserve tail and head resource load at most one.

### Proof

The internal upper and lower vertices of each path occur once positively
and once negatively, so every noncollar outer load is unchanged.  The path
counts above and Theorem 4.1 show that the two collar deficits are filled
exactly.

A fixed negative diamond in (5.1) occurs in exactly `n` paths: after its
outside pair `Y subset V` is fixed, choose which of the `n` elements of `Y`
is omitted by `X`.  Thus each ordered orientation loses `n alpha_1/2`.
This is at most `w_0` exactly when

```text
m <= a(a-1)(m-a),                                        (5.5)
```

which holds for every `a>=3,m-a>=1`.  A negative diamond in (5.3) belongs
to one path, and `alpha_2/2<=w_0` is immediate.  Hence all atom weights are
nonnegative.

It remains to check middle capacities.  Because both orientations receive
the same correction, tail and head loads are identical.  Classify a middle
trace by

```text
(r,e)=(|A-S|,|S-A|).
```

The first family has the following positive per-resource corrections:

```text
(1,0): (n+1)/[(m+1)n],
(1,1): 2/[a(m+1)],
```

and a negative correction on type `(2,1)`.  The second family has positive
correction `2/[a m(m+1)]` on types `(2,1)` and `(1,2)`, and a negative
correction on `(2,2)`.  These values follow by fixing the displayed middle
resource and counting the remaining path parameters.

Before correction, a type `(1,0)` middle resource has lost exactly `m`
of its `m^2` atoms, so its slack is `2/(m+1)`.  A type `(1,1)` resource has
lost the unique swap replacing its extra collar coordinate by its missing
one, so its slack is `1/m`.  Every other nonreserve middle resource has at
least the full-system slack `1/(m+1)`.  Therefore

```text
(n+1)/[(m+1)n] <= 2/(m+1),
2/[a(m+1)]     <= 1/m,
2/[a m(m+1)]   <= 1/(m+1),
```

for `a>=3,n>=1`.  Negative corrections only help.  Every middle load is at
most one, completing the proof.  `square`

### Corollary 5.2 (exact robust fractional capacity)

For every `a>=3`, the disjoint union of

1. the child uniform fractional matching from Proposition 2.2, and
2. the complement weighting from Theorem 5.1

is an outer-perfect fractional ordered-four-transversal of the full
parameter-`m` hypergraph.  It uses no atom crossing the child boundary.

Thus the balanced-subcube reserve verifies the four-resource capacity
hypothesis exactly, rather than probabilistically.

### Theorem 5.3 (the two-coordinate recursion)

There is an even smaller exact fractional recursion.  Take `a=1`, write the
collar as `{c,z}` and reserve trace `{c}`.  Put `n=m-1` and

```text
M=binom(2n,n),       N=binom(2n,n-1),
P=binom(2n,n-2),     R=N-M+P.
```

For `m>=4`, `R>=0`.  On the five allowed trace transitions, prescribe the
following total outer flow:

```text
empty -> empty        P,
empty -> {z}          M-P,
{z}   -> {z}          R,
{z}   -> {c,z}        M-P,
{c,z} -> {c,z}        P.                               (5.6)
```

Distribute each total uniformly over its biregular outside-set incidence
orbit and equally over the two physical orientations.  This is an
outer-perfect fractional matching of the complement.  Its middle load is

```text
1-(n-1)/[n(n+2)]       on traces empty and {c,z},
n/(n+1)                 on trace {z}.                    (5.7)
```

In particular every middle load is below one.

### Proof

The lower trace-class orders are `M,N,P`, while the upper orders are
`P,N,M`.  The row and column sums of (5.6) are therefore exact; the middle
entry is nonnegative because

```text
R/M=(n^2-2n-2)/[(n+1)(n+2)]>=0        (n>=3).
```

Every allowed trace orbit is biregular, so uniform distribution realizes
the displayed aggregate flow on actual outer pairs.  Counting the incident
outside-set extensions of a fixed middle resource gives (5.7).  `square`

Because the outer projection is bipartite, its fractional perfect matching
also implies an integral perfect matching of the two nonreserve outer
palettes.  What does not follow by bipartite integrality is simultaneous
tail/head injectivity or physical acyclicity; those remain the four-resource
rounding gate.

## 6. The exact recursive interface

The balanced subcube reserve separates the construction into three pieces.

1. **Recursive core.**  Solve the exact parameter-`m-a` problem inside the
   reserve.  Its fractional capacity and all local Boolean identities are
   automatic by Theorem 1.1.
2. **Far bulk.**  Outside the reserve and its two-coordinate collar, the
   original uniform fractional solution is unchanged.
3. **Collar braid.**  Reroute the deficit (4.3) through atoms outside the
   reserve, preserving the middle capacity inequalities, then round the
   resulting fractional solution and eliminate physical cycles.

Theorem 5.1 solves the fractional collar interface.  Direct collar-to-collar
atoms pass through a reserve middle resource, and the three-edge paths
(5.1),(5.3) are the explicit detours around it.  This is the same structural
role played by the finite seam braids in the exact certificates.

An exact sufficient theorem is therefore:

> **Balanced-subcube collar theorem.**  For the reserve above, the complement
> ordered-diamond hypergraph has an integral matching covering every
> nonreserve outer resource, using no reserve middle resource, and its
> physical lift can be chosen acyclic jointly with the recursive core.

This statement is now purely integral and topological.  It is strictly more structured than an arbitrary
`D=Theta(log N)` residual theorem: all deficit is explicit, supported on
the two trace collars counted in (3.1), with the two exact values in
Theorem 4.1.  It remains unproved.

### Theorem 6.1 (exact two-coordinate integral collar gate)

Put `n=m-1` and abbreviate

```text
M=binom(2n,n),       N=binom(2n,n-1),
P=binom(2n,n-2),     C=M-P=Cat_(n+1),
R=N-C.
```

Assume the parameter-`n` child ordered-diamond hypergraph has a Catalan
linear matching `F` of `N` atoms.  The following decoration is sufficient
to construct a Catalan linear matching at parameter `n+1`.

1. Choose `Q subset F` with `|Q|=C`; retain the `R` atoms of `F-Q` on the
   central complement trace `{z}`.
2. For every upper endpoint `U` of an atom in `Q`, choose a distinct
   `n`-set `p^-(U) subset U`.  For every lower endpoint `L` of an atom in
   `Q`, choose a distinct `n`-set `p^+(L) supseteq L`.
3. The `P` rank-`n` sets outside `im(p^-)` admit a saturating diamond
   matching onto every rank-`n+2` set.  Dually, every rank-`n-2` set admits
   a saturating diamond matching onto the `P` rank-`n` sets outside
   `im(p^+)`.
4. After assigning physical orientations to all displayed diamonds, their
   rank-`n+1` resources are injective in both roles and the resulting
   directed physical graph is acyclic.

Then the union of the following five sectors is the required complement
matching:

```text
trace empty -> empty:       the first saturating matching;
trace empty -> {z}:         p^-(U) -> U       for U in Q;
trace {z} -> {z}:           F-Q;
trace {z} -> {c,z}:         L -> p^+(L)       for L in Q;
trace {c,z} -> {c,z}:       the dual saturating matching.
```

Together with any child Catalan linear matching on the reserved trace
`{c}`, this gives a Catalan linear matching at parameter `n+1`.

### Proof

The five sector sizes are exactly `P,C,R,C,P`, the integral version of
(5.6).  The two port maps cover precisely the child endpoints removed with
`Q`; all other central endpoints are covered by `F-Q`.  The complementary
port sets have order `P`, so the two saturating matchings cover the two
remaining outer sectors.  Thus every nonreserve lower and upper resource
occurs once.  Hypothesis 4 supplies tail/head injectivity and a path forest.
The reserved child uses middle trace `{c}`, disjoint from the three
complement traces, so adjoining it preserves the four resource conditions.
`square`

Theorem 6.1 identifies the smallest exact collar gate.  Outer counts,
fractional capacity and port cardinalities are already forced and solved.
The inherited-port theorem chooses `p^-=tail` and `p^+=head`; the common-
basis theorem then guarantees a suitable `Q` and both diagonal incidence
matchings.  The remaining statement is one *joint physical* certificate:
realize the two diagonal matchings as anchor-capped side forests whose
contracted seam attachment graph is acyclic.  This is the
alternating-SDR/transparent-gluing condition in two-coordinate normal form.

### Proposition 6.2 (one SCD supplies both diagonal complements)

Fix any symmetric-chain decomposition of `B_(2n)`.  Let `B_*` be the rank-`n`
sets lying on chains whose minimum rank is `n-1` or `n`.  Then

```text
|B_*|=(N-P)+(M-N)=M-P=C.                                (6.1)
```

Every rank-`n+2` set is paired, along its chain, with a distinct rank-`n`
set outside `B_*`.  Dually every rank-`n-2` set is paired with a distinct
rank-`n` set outside `B_*`.  Both pairings are saturating diamond matchings.

### Proof

A chain reaches rank `n+2` exactly when its minimum rank is at most `n-2`.
Such a chain contains one rank-`n` set, giving the first pairing.  Chains
with minimum rank at least `n-1` account for the complementary rank-`n`
sets, whose count is the telescoping value (6.1).  Symmetry of every chain
gives the lower pairing.  `square`

### Corollary 6.3 (common-port-bank form of the gate)

In Theorem 6.1, Hypotheses 2--3 are satisfied if one can choose `Q` and two
bijections

```text
p^-: upper(Q) -> B_*,       p^+: lower(Q) -> B_*
```

with `p^-(U) subset U` and `L subset p^+(L)`.  Thus, after fixing one SCD,
the incidence problem is a common Catalan-size port bank served
simultaneously by the lower and upper endpoints of one `C`-edge subset of
the child factor.  Proposition 6.4 and the later automatic-common-basis
theorem settle that incidence row without fixing the SCD bank in advance.
The remaining condition is that suitable diagonal diamonds admit one
injective acyclic physical realization.

### Proposition 6.4 (exact matroid-intersection criterion)

Let the ground set be the `N` atoms of the child factor `F`.  Define two
transversal matroids on this ground set:

* `M^-`: a set of atoms is independent when their upper endpoints can be
  matched down into distinct members of `B_*`;
* `M^+`: a set is independent when their lower endpoints can be matched up
  into distinct members of `B_*`.

Write their rank functions as `r_-,r_+`.  A common-port set `Q` of order
`C` exists if and only if

```text
min_(S subset F) [r_-(S)+r_+(F-S)] >= C.                  (6.2)
```

### Proof

The two port injections are exactly independence in the two displayed
transversal matroids.  Edmonds' matroid-intersection min--max theorem says
that the maximum common independent-set size is the left side of (6.2).
Each matroid has rank at most `|B_*|=C`, so a common set of size `C` is a
common basis and gives both required bijections.  `square`

The positivity question in (6.2) has since been settled.  The strengthened
Kruskal--Katona chord in
`MATH_THEOREM_CATALAN_TWO_COORDINATE_COMMON_BASIS_AUTOMATIC_20260731.md`
proves the dual-rank density `C/N` on every relevant subset.  Applying it to
the two pullbacks makes the left side of (6.2) at least `C` term by term.
Thus a common basis is automatic for every child Catalan forest (indeed for
every pair of injective tail/head maps).  Compatibility with the physical
side-degree and forest rows remains open.

### Proposition 6.5 (orientation is exactly the linear-forest row)

After the outer diamonds are fixed, let `R` be their undirected physical
Johnson-edge support.  There is an orientation injective in both middle
roles and acyclic if and only if `R` is a linear forest.

### Proof

Tail/head injectivity gives indegree and outdegree at most one, hence
undirected degree at most two.  Acyclicity excludes cycle components, so the
support is a disjoint union of paths.  Conversely orient every path
consistently; each physical vertex then has indegree and outdegree at most
one and no directed or undirected cycle occurs.  `square`

Accordingly the sole part left after (6.2) is choosing physical
representatives of an already guaranteed common basis so that their support,
together with `F-Q`, has maximum degree two and no cycle.  In the sharper
port-inheritance formulation this is exactly two punctured side forests plus
an acyclic contracted attachment graph.  This forest-compatible realization
theorem is still missing.

## 7. Lattice/transferral condition

For any absorber catalogue, let `Gamma` be the integer lattice generated by
the incidence differences

```text
chi(on state)-chi(off state)
```

over all four resource classes.  The exact absorption condition for a
residual defect vector `z` has two parts:

1. `z in Gamma`, subject to the global equality of the two outer totals and
   the allowed `Cat_m` middle slack; and
2. `z` has a representation by mutually resource-disjoint catalogue
   elements inside the available collar/reserve pools.

The first is the lattice/transferral gate; the second is the integral
packing gate.  The independent-boundary theorem enlarges the generating
catalogue but does not, by itself, prove either a bounded-norm lattice basis
or a disjoint representation.  A complete collar theorem must establish
both, not merely the fractional loads in Section 4.

## 8. Exact audit

The standard-library `Fraction` replay

```text
scratch/audit_balanced_subcube_fractional_collar_completion_20260731.py
```

enumerates every ambient ordered atom, deletes the child reserve, applies
every path in (5.1) and (5.3) with the exact rational coefficients, and
checks every outer equality, middle inequality and atom nonnegativity.  It
passes at `(m,a)=(4,3),(5,3),(6,3)`.  The retained output is

```text
scratch/balanced_subcube_fractional_collar_completion_20260731.audit.json.
```

The separate trace/count audit

```text
scratch/audit_balanced_subcube_reserve_collar_20260731.py
```

checks the crossing catalogue and the exact lost-degree histogram through
`m=6,a=2`.

Finally,

```text
scratch/audit_balanced_subcube_two_coordinate_fractional_recursion_20260731.py
```

constructs the orbit weights (5.6) directly on every ambient ordered atom
and verifies the exact outer and middle loads for `m=4,5,6,7`.
