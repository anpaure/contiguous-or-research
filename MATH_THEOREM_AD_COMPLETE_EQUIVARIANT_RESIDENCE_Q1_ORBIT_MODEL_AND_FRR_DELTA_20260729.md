# Complete fixed-orbit residence-four and both-`q1` model at `K=16`

Date: 2026-07-29  
Lane: AD  
Status: exact integral formulation, exact row census, and exact FRR
source-relative compression proved.  No solver or search was run.

## 0. Verdict

The complete fixed-label `C_15` edge-orbit catalogue already contains all
chronology needed for residence and both `q1` palettes.  No successor,
component-voltage, width, or motif-selector variable is needed.

Under the strict finite-cycle convention for one-sided positive residence,
the exact `K=16` model is

```text
binary edge-orbit variables                         27,456
weighted degree-two equations                          858
lower-q1 cover rows                                    764
upper-q1 cover rows                                    764
positive-residence rows                          9,103,956
total indexed rows                               9,106,342
auxiliary / width-selector variables                       0
```

The residence rows should normally be separated lazily.  Every actual
short nonconstant run gives a labelled quotient-walk no-good with at most
four orbit literals; a constant-one triangle gives one with at most three.
The eager count above is exact before possible equality of projected row
supports, but no irredundancy claim is made.

There are four exceptional `q1` target orbits: two lower targets containing
`z` and two upper targets avoiding `z`.  Each has five literal colours.  A
selected provider edge orbit contributes physical load three to every
literal colour in such an orbit.  Its Boolean cover clause nevertheless has
coefficient one.

For the separated, frozen-small-component FRR collar-rethread subclass, the
raw canonical subcatalogue has exactly `11,928` free `BB` edge bits.  This is
affinely isomorphic to the current `426 + 426*27 = 11,928` joint `x/y`
model, so the raw catalogue is not smaller.  Eliminating the derived cut bit
and the old/default edge bit in every free upper block gives an exact
source-relative delta model with `426*27 = 11,502` Boolean edit bits.  This
is a saving of 426 bits, not a new WLOG reduction of unrestricted FRR.

## 1. The complete fixed-label factor catalogue

Let

\[
 K=16,\qquad r=8,\qquad n=15,\qquad
 W=\binom{16}{8}=12870,\qquad N=W/n=858.
\tag{1.1}
\]

Let `rho` rotate the fifteen old coordinates and fix the coordinate `z`.
The action on middle vertices is free.  Indeed, a middle vertex contains
either eight old coordinates or seven old coordinates, while every
nontrivial coordinate cycle of a subgroup of `C_15` has length `3`, `5`, or
`15`; neither seven nor eight is divisible by three or five.

The action on undirected physical Johnson edges is also free.  A
nonidentity rotation cannot fix either endpoint.  If it stabilized an
unordered edge by exchanging the endpoints, its induced permutation on the
two endpoints would have order two, impossible for an element of the odd
group `C_15`.  Hence every edge orbit contains exactly fifteen physical
edges.

Fix one representative of each middle orbit.  Let `mathcal E` be the set of
undirected physical edge orbits and use one bit `y_e` for each
`e in mathcal E`.  The exact census is

\[
 |\mathcal E|=12012\;AA+3432\;AB+12012\;BB=27456.
\tag{1.2}
\]

For quotient owner `v`, let `m_v(e)` be `0` or `1` for an ordinary quotient
edge incidence and `2` for a quotient loop at `v`.  Then

\[
              \sum_{e\in\mathcal E}m_v(e)y_e=2
              \qquad(v=1,\ldots,858)                 \tag{1.3}
\]

is equivalent, in both directions, to a literal `rho`-invariant spanning
two-factor of `J(16,8)`.  The loop coefficient two is essential.

No directed successor variables are needed for the present properties.  A
literal undirected two-factor already determines each cyclic chronology up
to reversal, and `q1` coverage and residence are reversal-invariant.  If an
explicit equivariant orientation is desired, orient one cycle in each
`C_15`-orbit of physical cycles and transport the orientation.  A cycle
stabilizer has odd order and therefore cannot reverse an orientation.  The
result projects to an arbitrary quotient successor permutation with its
actual phase increments.  Thus zero, nonunit, and unit component voltages
all remain present in (1.3); none is selected or excluded by an auxiliary
voltage field.

The earlier even-`r` catalogue theorem proves that every member of
`mathcal E` occurs in some equivariant factor.  Consequently 27,456 is the
smallest direct fixed-label edge-orbit support catalogue at `K=16`.
This does not claim information-theoretic minimality among implicit binary
encodings or after quotienting by one coherent global coordinate normalizer.

## 2. Exact both-`q1` rows and stabilizer coefficients

For an edge orbit `e`, let `L(e)` be the rotation orbit of the intersection
of either physical edge in `e`, and let `U(e)` be the rotation orbit of its
union.  For a target orbit `O`, put

\[
 h_O=|\operatorname{Stab}_{C_{15}}(T)|=15/|O|
 \qquad(T\in O).                                      \tag{2.1}
\]

### Theorem 2.1 (exact literal load)

For every literal target `T in O`, its load in the lifted factor is

\[
 \lambda_L(T)=h_O\sum_{e:L(e)=O}y_e,
 \qquad
 \lambda_U(T)=h_O\sum_{e:U(e)=O}y_e.                 \tag{2.2}
\]

Therefore complete literal lower and upper `q1` coverage is exactly

\[
 \sum_{e:L(e)=O}y_e\ge1,
 \qquad
 \sum_{e:U(e)=O}y_e\ge1                              \tag{2.3}
\]

for every lower and upper target orbit, respectively.

#### Proof

The map from the fifteen physical edges of a fixed edge orbit to their
intersection targets is the equivariant orbit map `C_15 -> O`.  Every
fibre has size `15/|O|=h_O`.  Selecting `e` therefore contributes exactly
`h_O` distinct physical providers to every literal target in `O`.  Summing
over selected edge orbits proves the lower identity.  Union is identical.
The common load is positive exactly when at least one provider-orbit bit is
selected, proving (2.3).  No component traversal enters the proof.  QED.

The exact `K=16` target census is

| palette | target orbits | provider orbit bits per row |
|:--|--:|:--|
| lower, no `z` (old rank 7) | 429 | `28 AA + 8 AB = 36` |
| lower, with `z` (old rank 6), generic | 333 | `36 BB` |
| lower, with `z`, exceptional | 2 | `12 BB` |
| upper, no `z` (old rank 9), generic | 333 | `36 AA` |
| upper, no `z`, exceptional | 2 | `12 AA` |
| upper, with `z` (old rank 8) | 429 | `28 BB + 8 AB = 36` |

Old ranks seven and eight are free and give 429 orbits each.  Burnside at
old rank six gives

\[
 \frac{\binom{15}{6}+2\binom52}{15}=335,             \tag{2.4}
\]

namely 333 size-fifteen orbits and two size-five orbits.  Complementation
gives the same census at old rank nine.  Thus each palette has
`429+335=764` rows.

For a generic target orbit, `h_O=1` and there are 36 provider orbit bits.
For each of the four exceptional size-five orbits,

\[
 h_O=3,\qquad |P(O)|=12,
 \qquad \lambda(T)=3\sum_{e\in P(O)}y_e.             \tag{2.5}
\]

The support clause in (2.3) remains coefficient one.  The coefficient
three must be restored in every physical-load, excess, or exact-rainbow
ledger.  The total number of positive `q1` row incidences is

\[
 2\bigl(429\cdot36+333\cdot36+2\cdot12\bigr)=54912.  \tag{2.6}
\]

## 3. Exact strict residence-four rows

This section uses the strict finite-cycle positive convention: a factor
component whose trace is constantly one in coordinate `a` is one finite
positive run of the component's length.  Thus a constant-one triangle is
forbidden.

For a physical coordinate `a`, put

\[
 \mathcal U_a=\{X\in\tbinom{[16]}8:a\in X\},
 \qquad H_a=J(16,8)[\mathcal U_a].                    \tag{3.1}
\]

For `S subseteq mathcal U_a`, let `delta_a(S)` be the set of shore edges
of `H_a` with exactly one endpoint in `S`.

### Theorem 3.1 (strict shore-boundary characterization)

Let `F` be a spanning simple two-factor.  Every cyclic positive `a`-run has
length at least four if and only if

\[
                 |F\cap\delta_a(S)|\ge1              \tag{3.2}
\]

for every nonempty `H_a`-connected set `S` with `|S|<=3`.

#### Proof

The components of `F[mathcal U_a]` are precisely the bounded positive runs
(path components) and the constant-one factor components (cycle
components).  A forbidden run is therefore a path or cycle component `P`
of size one, two, or three.  Taking `S=V(P)` violates (3.2).

Conversely, if (3.2) fails, no selected shore edge joins `S` to its shore
complement.  Every component of `F[mathcal U_a]` meeting `S` is consequently
contained in `S`; at least one exists and has size at most three.  It is a
forbidden run.  If a disconnected `S` violated the row, one of its
`H_a`-components would already violate it because boundary counts are
nonnegative and additive.  Hence connected sets suffice.  QED.

For an edge orbit `e`, write `E(e)` for its fifteen physical edges and set

\[
 d_e(a,S)=|E(e)\cap\delta_a(S)|.                      \tag{3.3}
\]

Since `y_e=1` selects all of `E(e)`, (3.2) projects exactly to

\[
                  \sum_e d_e(a,S)y_e\ge1.             \tag{3.4}
\]

For Boolean variables and right-hand side one, this is equivalently the
support clause

\[
                  \bigvee_{e:d_e(a,S)>0}y_e.          \tag{3.5}
\]

The integer coefficient must not be discarded in a fractional or physical
load identity; a quotient-loop orbit can meet one physical owner twice.
One representative of every rotation orbit of pairs `(a,S)` gives all and
only the strict residence rows.

## 4. Labelled quotient-walk CEGAR is exactly equivalent

Fix section representatives `U_i`.  Write a directed labelled quotient dart
as `(i,j,p)` when its physical lift sends
`rho^s U_i` to `rho^(s+p) U_j`.  A compatible labelled walk has phase sums

\[
 P_0=0,\qquad P_t=\sum_{h<t}p_h,
 \qquad X_t=\rho^{s+P_t}U_{i_t}.                      \tag{4.1}
\]

Let `ell in {1,2,3}`.  A bracket walk is a physically simple sequence
`X_0,...,X_(ell+1)` with trace

\[
                         0,1^\ell,0                  \tag{4.2}
\]

in some coordinate.  Let `supp(P)` be the set of distinct undirected
edge-orbit IDs used by the physical edges of this walk.  Repeated orbit IDs
are included only once.  The exact no-good is

\[
          \sum_{e\in\operatorname{supp}(P)}y_e
          \le |\operatorname{supp}(P)|-1.             \tag{4.3}
\]

For the strict convention, also add (4.3) for every constant-one physical
triangle, using its three physical edges.  Every row has at most four orbit
literals.

### Theorem 4.1 (lift/project equivalence)

On the weighted degree-two face, the static rows (3.4), all walk rows (4.3)
including the constant-triangle rows, and literal strict positive residence
four have exactly the same integral solutions.

#### Proof

A short nonconstant run together with its two bordering factor edges is a
walk (4.1)--(4.2), all of whose orbit variables are selected, so it violates
(4.3).  A constant short component in a simple two-factor can only be a
triangle and violates the corresponding triangle row.

Conversely, selecting every orbit ID in `supp(P)` selects every displayed
physical edge, including different physical edges belonging to a repeated
orbit.  At each internal physical vertex the two walk edges saturate degree
two, so the factor must traverse the displayed bracket and contains the
short run.  Selecting every edge of a constant-one physical triangle
saturates all three vertices and forces that triangle component.  This
proves exactness of the walk family.  Theorem 3.1 proves exactness of the
static family.  QED.

The phase recurrence (4.1) uses the actual edge labels.  It makes no
assumption on the sum of phases around a quotient component, so zero and
nonunit voltages cannot evade the cuts.  An integral lazy separator may
lift the selected 858 orbit edges to the 12,870-edge physical factor,
traverse its cycles, and scan all coordinate traces in `O(KW)` time.  Every
emitted conflict has at most four literals.  This is exact CEGAR, not a
claim about solver runtime.

## 5. Exact `K=16` residence row census

For one fixed coordinate,

\[
 H_a\cong J(15,7),\qquad |V(H_a)|=6435,
 \qquad \deg(H_a)=56,
 \qquad |E(H_a)|=180180.                              \tag{5.1}
\]

The number of Johnson triangles is

\[
 T=\binom{15}{6}\binom93+\binom{15}{8}\binom83
  =780780.                                             \tag{5.2}
\]

Counting centred wedges, where a nontriangle connected triple has one
centre and a triangle has three, gives

\[
 C_3=6435\binom{56}{2}-2T=8348340.                    \tag{5.3}
\]

Thus a fixed shore has

\[
 R_*=6435+180180+8348340=8534955                     \tag{5.4}
\]

connected sets of sizes one, two, and three.

For the fifteen old coordinate labels, the action on labelled pairs
`(a,S)` is free, so all old coordinates together contribute exactly
`R_* = 8,534,955` quotient row orbits.

The top coordinate `z` is fixed, so Burnside is required.  Singleton and
edge actions are free, giving 429 and 12,012 orbits.  A connected triple can
be fixed nontrivially only by `rho^5` or `rho^10`.  For either rotation, the
old coordinates split into five triples.  A rank-seven mask is adjacent to
its translate exactly when one coordinate triple contributes one point and
two of the other four triples are full.  There are

\[
                     5\cdot3\cdot\binom42=90         \tag{5.5}
\]

such masks, forming 30 invariant Johnson triangles.  Hence the number of
top-coordinate connected-triple orbits is

\[
                    \frac{8348340+30+30}{15}=556560, \tag{5.6}
\]

and the top contributes

\[
                    429+12012+556560=569001.          \tag{5.7}
\]

Therefore the exact symmetry-reduced index count is

\[
                  R_{\rm res}=8534955+569001
                              =\boxed{9103956}.        \tag{5.8}
\]

Adding the 858 factor equations and 1,528 `q1` rows proves the
`9,106,342` total in Section 0.  Distinct indexed rows may project to the
same Boolean support, so this is not an irredundancy theorem.

If constant-coordinate components are declared vacuously safe (the
bordered-run convention), the same index family is used with the exact row

\[
 |F\cap C_a(S)|\le |F\cap\delta_a(S)|,                \tag{5.9}
\]

where `C_a(S)` is the set of coordinate-crossing edges from `S`.  The
integer coefficients in this row cannot be replaced by supports.  If both
positive runs and zero gaps must have length at least four, repeat the
strict rows on the negative shore.  The exact residence-row count then is
`18,207,912`, and the complete factor-plus-both-`q1` row count is
`18,210,298`.

## 6. FRR as a canonical `BB` subcatalogue

Write a `BB` middle owner as `X+z`, with `X` an old rank-seven set.  Every
`BB` Johnson edge has the unique form

\[
 (U-\{a\})+z\;--\;(U-\{b\})+z,
 \qquad U\in\binom{[15]}8,\quad\{a,b\}\in\binom U2. \tag{6.1}
\]

Thus each of the 429 upper-colour orbits is one block of 28 edge-orbit
choices, accounting for all `429*28=12,012` `BB` variables.

In the saved FRR source, the large component uses 426 upper blocks and the
45-cycle uses three.  The independent-rail construction fixes every `AA`
bit, every `AB` bit, and all 84 bits in the three small-component blocks.
The free direct subcatalogue therefore has

\[
                         426\cdot28=11928             \tag{6.2}
\]

bits.

For block `q`, let `p_0(q)` be its old/default pair.  The present joint model
has one cut bit `x_q` and 27 nonold choice bits `y_(q,p)`, with

\[
                \sum_{p\ne p_0(q)}y_{q,p}=x_q.         \tag{6.3}
\]

If `z_(q,p)` denotes the canonical edge bit, then

\[
 z_{q,p_0}=1-x_q,
 \qquad z_{q,p}=y_{q,p}\quad(p\ne p_0)                \tag{6.4}
\]

is an affine bijection.  Hence the direct 11,928-bit catalogue and the joint
11,928-bit `x/y` model are exactly the same one-hot object.

### Theorem 6.1 (exact delta elimination)

Use only the 11,502 nonold edit bits and impose

\[
                 \sum_{p\ne p_0(q)}y_{q,p}\le1
                 \qquad(q=1,\ldots,426).              \tag{6.5}
\]

Decode

\[
 h_q=\sum_{p\ne p_0(q)}y_{q,p},\qquad
 z_{q,p_0}=1-h_q,qquad z_{q,p}=y_{q,p}.               \tag{6.6}
\]

For every rank-seven owner orbit `V`, impose the signed degree equation

\[
 \sum_{q,p\ne p_0}
 \bigl(m_V(e_{q,p})-m_V(e_q^0)\bigr)y_{q,p}=0,         \tag{6.7}
\]

with loop coefficient two.  For a lower target orbit `O`, let `c_O=1`
generically and `c_O=3` on either exceptional orbit.  If `ell_O^0` is its
old physical load, impose

\[
 \ell_O^0+c_O\sum_{q,p\ne p_0}
 \bigl(1_{L(e_{q,p})=O}-1_{L(e_q^0)=O}\bigr)y_{q,p}
 \ge1.                                                  \tag{6.8}
\]

Equations (6.5)--(6.8) are projection-bijective to the factor and both-`q1`
part of the joint model.  Upper `q1` is automatic because every upper block
selects exactly one old or new edge.  The proof is substitution of (6.6)
in the canonical degree and load rows; conversely define `x_q=h_q` to
recover (6.3)--(6.4).

The 1,425 old length-three runs project to 95 closed collar orbits.  Their
necessary hit rows are

\[
 \sum_{q\in C}\sum_{p\ne p_0(q)}y_{q,p}\ge1
 \qquad(C\in\mathcal C_0).                            \tag{6.9}
\]

The current separated subclass additionally forbids two changed blocks at
cyclic distance one, two, or three.  There are exactly `3*426=1,278` such
rows.  Before lazy residence cuts, the exact installed semantic-family
count is

| family | rows |
|:--|--:|
| at most one nonold choice | 426 |
| weighted owner degree | 429 |
| lower-orbit coverage | 335 |
| old-collar hits | 95 |
| optional separated-cut rows | 1,278 |
| **separated total** | **2,563** |

Without the optional separation restriction, but retaining the necessary
collar hits, the base has 1,285 rows.  These are installed-family counts;
some signed rows can become tautological after substituting the frozen
small component.

Every FRR short physical run still projects to the labelled walk row (4.3).
After the source-relative substitution, the corresponding absence clause is

\[
 \sum_{e_q^0\in P}\sum_{p\ne p_0(q)}y_{q,p}
 +\sum_{e_{q,p}\in P}(1-y_{q,p})\ge1.                 \tag{6.10}
\]

It uses the actual phase labels and therefore remains exact for arbitrary
emergent component voltages.  No width selector is introduced.

Consequently the answer to the compactness question is exact:

* the raw fixed-label subcatalogue is **not** smaller than the joint model;
  both have 11,928 primary bits and are affinely isomorphic;
* the source-relative delta chart is smaller, with 11,502 bits, because the
  cut and old/default channels are derived rather than selected; and
* no claim is made that 11,502 is an information-theoretically minimum SAT
  encoding.  A binary-coded 28-way state would require an exact decoder for
  degree, lower colour, and residence and has no proved smaller total
  formulation.

## 7. Exact proved boundary

Proved WLOG for the complete equivariant carrier model:

* the full 27,456 fixed-label physical edge-orbit catalogue;
* weighted degree two, including quotient-loop coefficient two;
* all lower and upper `q1` support rows with exact stabilizer loads;
* strict one-sided residence through the static rows or exact labelled-walk
  CEGAR; and
* arbitrary factor topology and arbitrary component voltages.

Not imposed and not claimed:

* connectivity, unit voltage, or a prescribed successor permutation;
* any bounded-width shadow catalogue;
* opening/splicing or common-compiler Hall;
* deeper shadows; or
* a literal contiguous-OR word.

For FRR, freezing the 45-cycle and imposing four-separated cuts are
sufficient-subclass restrictions, not WLOG consequences of `FRR(7,4)`.
The 11,502-bit theorem is exact only for the corresponding source-relative
edit chart (or for the unseparated frozen-small chart after deleting the
1,278 optional rows).  It is not an unrestricted FRR existence theorem and
does not assert feasibility.

## 8. Independent audit trail

The decisive layers were proved and audited separately in:

```text
MATH_THEOREM_AD_FIXED_ORBIT_RESIDENCE_QUOTIENT_WALK_CUTS_20260729.md
MATH_AUDIT_AD_FIXED_ORBIT_RESIDENCE_QUOTIENT_WALK_CUTS_20260729.md
MATH_THEOREM_AD_K16_CANONICAL_ORBIT_BOTH_Q1_ROWS_20260729.md
MATH_AUDIT_AD_FRR_COLLAR_RETHREAD_CANONICAL_CATALOGUE_20260729.md
```

The independent checks covered the strict-cycle correction, repeated
edge-orbit IDs in a walk, the `rho^5/rho^10` Burnside correction, quotient
loops, exceptional physical coefficient three, the `11,928 <-> 11,928`
affine FRR channel, and the `11,502` delta substitution.  No web access,
solver, remote job, exhaustive enumeration, or sustained local computation
was used.
