# Terminal PBP certificates and ported Pascal composition

Date: 2026-07-30  
Lane: R  
Status: pure mathematics plus exact use of already authenticated finite
certificates.  The smallest nontrivial odd-to-even Pascal terminal-PBP
descendant in the requested `k=11,13,15` lineage is proved, Pascal boundary
composition and cumulative phase credit are proved, and an exact
serial/parallel induction theorem is proved under explicit port hypotheses.
No positive plateau PBP and no unconditional all-`k` recurrence are claimed.

## 0. Main result and corrected boundary

There are two different notions.

1. A **terminal PBP** is one completed child chronology together with one
   literal common source `Q`, a casualty matching, and complete upper replay.
   Its compiler may have been solved afresh.
2. A **ported PBP** additionally exports occurrence-labelled protected
   providers, their complete dependency collars, a boundary common-`Q`
   fibre, and upper seam sockets which survive the next Pascal lift.

The authenticated `11->12` and `13->14` six-piece constructions are terminal
PBPs.  Their inherited facet states are depth-drop constructions:

\[
    D=3,\qquad d=2,\qquad a=1,qquad f=0,
\]

so their phase credit is

\[
    f+(D-d)=1=a.                                    \tag{0.1}
\]

They do not cross a net flat and do not prove the plateau case.  Their child
compilers were solved afresh, so they also do not certify a nonempty
parent-to-child protected pin map or hereditary facet transparency.

The `k=15` optimum supplies a different nontrivial terminal socket: its
two-component non-Pascal splice repairs a genuine nested upper casualty
pair and assigns two lower casualties to the global boundaries under one
exact compiler.  It is not an odd-even Pascal morphism.

This note proves the exact composition law which would turn such terminal
objects into an induction: Pascal orders add, boundary facets contribute a
bounded and explicitly labelled bridge block, actual horizon requirements
compose, and lower matchings compose exactly when their local source fibres
have one common member, transported occurrences remain injective, and the
global casualty graph passes Hall.  Phase losses themselves need not add
when deadline origins reset.  The missing all-`k` hypothesis is existence of
the exported ported structure, not another terminal word.

## 1. Terminal and ported PBP

Let `T=(T_i)` be a middle chronology with actual horizons `rho_i`, and put

\[
    W_i=[i,i+\rho_i],
    \qquad
    E_p=\bigcap_{i:p\in W_i}T_i.                    \tag{1.1}
\]

A **common source** is a family

\[
    \varnothing\ne Q_p\subseteq E_p,
    \qquad
    T_i=\bigcup_{p\in W_i}Q_p.                     \tag{1.2}
\]

For a physical source interval `C`, write

\[
    \lambda_Q(C)=\bigcup_{p\in C}Q_p.              \tag{1.3}
\]

### Definition 1.1 (terminal PBP)

A child construction is a terminal phase-balanced protected braid if:

1. its Pascal pieces satisfy their phase-credit inequalities and all
   claimed transported exact-envelope cells have protected collars;
2. one common source (1.2) exists;
3. a protected lower matching together with a matching from every remaining
   strict lower target into unallocated physical intervals `C` satisfying
   `lambda_Q(C)=target` covers the strict lower ideal;
4. the chronology has exact middle ownership and literal residence, and
   every upper target has a retained internal or explicitly replayed seam
   interval;
5. every endpoint, terminal, and fixed-tag singleton obligation is literal.

The protected matching may be empty.  Taking it empty makes every lower
target a casualty; this is legitimate for a terminal certificate but carries
no compiler information into the next rank.

### Definition 1.2 (ported PBP)

A terminal PBP is **ported** if it also exports:

1. an occurrence-labelled protected lower matching, with every full
   dependency collar and every fixed-tag hit;
2. the actual horizons, first/last source collars, and left/right base-state
   collars sufficient to construct every declared next-order Pascal bridge;
   a bridge uses both future sides and cannot in general be exported by one
   side alone;
3. hereditary facet transparency and fixed-tag hits on every
   descendant-selected restriction in the declared output port class;
4. a nonempty boundary fibre of common sources `Q` which keep all exported
   occurrences exact;
5. occurrence-labelled internal and seam upper witnesses, with the complete
   base collars required after the next Pascal transform;
6. a declaration of every exported cell not protected for the next lift as
   a next-stage casualty.

This is a mathematical interface, not extra decoration.  Section 8 gives a
three-position example in which two separately feasible terminal compilers
have no common source and therefore cannot compose.

## 2. The first odd-to-even Pascal terminal-PBP descendant in the lineage

Write `PBP_drop(r,d)` for a terminal `PBP(r,d)` whose inherited facet
pieces use order `a=1` from parent protection depth `D=d+1` with phase loss
`f=0`; any inserted boundary states still require separate literal replay.

The smallest nontrivial odd-to-even Pascal terminal-PBP descendant among the
authenticated `k=11,13,15` parent lineage is the `11->12` depth-drop braid.
(`5->6` is a smaller six-piece certificate, but lies outside the parent
lineage specified in the task.)  This qualifier is essential: under
Definition 1.1, each authenticated universal odd word is already a terminal
PBP with empty protected matching and a fresh compiler, but is not itself an
odd-to-even Pascal braid.

Put `z=2^11=0x800`.  The two middle sectors each have 462 states.  The exact
six-piece data are

\[
\begin{array}{c|c}
\text{A cuts}&66,459\\
\text{B-ear start and length}&409,3\\
\text{oriented order}&
 A_1^R,B_1^F,A_2^R,B_2^R,A_3^F,B_3^R\\
\text{piece lengths}&67,409,393,3,2,50.
\end{array}                                           \tag{2.1}
\]

The five seams, written as `left -> right : intersection, union`, are

```text
  95 -> 2079 :   31, 2143
2219 ->  235 :  171, 2283
1381 -> 2405 :  357, 3429
2095 ->  175 :   47, 2223
 159 -> 2203 :  155, 2207.
```

Every seam is Johnson and exchanges `z` with one old coordinate.

### Theorem 2.1 (exact `PBP_drop(6,2)` certificate)

The chronology (2.1), together with the retained word

```text
scratch/k12_intersection_sixpiece_hallpass_001.word
```

is a terminal `PBP(6,2)`.  More precisely:

1. it contains all `binom(12,6)=924` middle owners exactly once and is
   linearly depth-two resident;
2. every inherited order-one `B` state has phase credit by (0.1); the one
   inserted endpoint-completion state `B_0` is an explicitly audited
   boundary state rather than transported facet data;
3. every upper target is covered by a literal middle interval;
4. one nonzero 926-letter source `Q` satisfies `D^2Q=T` and covers all
   
   \[
       \sum_{j=1}^{5}{12\choose j}=1585
   \]
   strict lower targets;
5. its distinguished ear has middle positions `869,870,871`, and
   
   \[
       Q_{871}=\{z\}=0x800;
   \]
6. the literal source covers all 4095 nonempty masks, and its length is
   
   \[
       924+2=B(12)=926.
   \]

#### Proof

Exact reconstruction of the six oriented pieces gives the 924 distinct
rank-six states and the five displayed Johnson seams.  The retained
residence replay has zero structural failure, including every seam; checking
piece-interior runs alone would not suffice.

The targets absent from individual piece interiors at upper depth one are

\[
    0x89f,\quad0x8af,\quad0xd65.                    \tag{2.2}
\]

They are recreated respectively by the literal seam windows

```text
start 873: (0x09f,0x89b)                    -> 0x89f
start 871: (0x82f,0x0af)                    -> 0x8af
start 868: (0x565,0x965)                    -> 0xd65.
```

At upper depth two the only interior casualties are

\[
    0x8bf,\qquad0xd6d,                              \tag{2.3}
\]

with witnesses

```text
start 871: (0x82f,0x0af,0x09f)              -> 0x8bf
start 872: (0x0af,0x09f,0x89b)              -> 0x8bf
start 868: (0x565,0x965,0x92d)              -> 0xd6d.
```

Every upper target of depth at least three already has an internal witness.
Thus (2.2)--(2.3) are the complete upper-seam replay, not a q1 proxy.

The final middle chronology itself still has the two fixed-width lower-q1
holes `0x525,0x964` and the fixed-width lower-q2 hole `0x524`.  Hence its
lower clause is nonvacuous.  The
retained source is nonzero, reconstructs every middle row, and its exact
compiler replay covers all 1585 strict lower masks.  Choosing the first
literal witness interval of each target gives a matching: two distinct
target labels cannot have the same interval union.  This is precisely the
casualty matching of Definition 1.1 with `M_prot` taken empty and **every**
lower target freshly matched.
The same replay gives the literal singleton at position 871 and all 4095
targets.  The deadline lower bound proves optimality.  \(\square\)

The authenticated files are

```text
f57f775c55c9ae156aeb124fa0016dd835c0efd1c472897e93bc6ea5abfc45d6
  scratch/k12_intersection_sixpiece_hallpass_001.json
6d3777dd2ea66c6ff5706d7354133e2132b3fadd4bdf6b986f20bbf61b53e617
  scratch/k12_intersection_sixpiece_hallpass_001.compile.json
28c6d581bc5912b6ad369cb0ae60d164fb5a8391c48655ad581eb2a3deb2e506
  scratch/k12_intersection_sixpiece_hallpass_001.verify.json
a29517e67dd3c9db5f773f5332b3e3e44197cfe79d3d8014ea0770c9bedeb482
  scratch/k12_intersection_sixpiece_hallpass_001.word.
```

### Corollary 2.2 (the second drop calibration)

The authenticated `13->14` six-piece braid is another terminal PBP.  Its
inherited facet states have `D=3,d=2,a=1,f=0`; its single inserted
endpoint-completion state `B_1715` is separately audited.  Its cuts, ear
and order are

\[
 (418,1445),\qquad 966,\qquad
 A_1^F,B_2^R,A_3^F,B_1^F,A_2^R,B_3^F.              \tag{2.4}
\]

Its upper seam replay consists exactly of q1 targets

\[
 0x29ce,\quad0x352e,\quad0x3b64
\]

and q2 target `0x29de`; every higher upper target is internal.  Its literal
top singleton is `Q_421=0x2000`, and its 3434-letter source covers all 16383
nonempty masks.  The hashes are

```text
d67bb4176b49c0b7be4d0ac6f232cf59e4b0247999dbb5b1f06aeb50c62bbc7d
  scratch/k14_intersection_sixpiece_hallpass_004a.json
c4afb1dee3193d5ed37d21eae316ee67c3544329af2495163ce4be6bad549537
  scratch/k14_intersection_sixpiece_hallpass_004a.compile.json
6b5d06a9c8e65b713e80f97c00e1738d8e179df4882f94b73b91884644c9d202
  scratch/k14_intersection_sixpiece_hallpass_004a.verify_generic.json
7d94117099bbb46402e8f4edda718dae7eb10e2e5e34e9b588e08a198b43db17
  scratch/k14_intersection_sixpiece_hallpass_004a.word.
```

Again the compiler is terminal/fresh.  Neither Corollary 2.2 nor Theorem 2.1
exports a nonempty protected parent compiler matching.

## 3. What the odd `k=11,13,15` certificates supply

The exact boundary routers form a useful progression.

| parent | component operation | strict lower interface casualties | proper upper interface casualties | status |
|---|---|---|---|---|
| `k=11` | open one component | q1 `155`, q2 `154` | none | boundary pins, common compiler |
| `k=13` | two cuts, one seam | q1 `2135,2387`, q2 `2323` | none | boundary/seam pins, common compiler |
| `k=15` | two cuts, one seam | q1 `18553,18033` | `20089 subset 28537` | boundary pins plus literal upper seam grid, common compiler |

For `k=15`, the seam union `19065 union 18041` is `20089`, and the
four-state middle window at indices `6387,...,6390` has union `28537`.
The two lower casualties are the literal source boundaries

\[
    Q_0=18553,\qquad Q_{6437}=18033.                \tag{3.1}
\]

Thus `k=15` is the first retained member of this three-parent list which
tests a nonempty higher upper casualty chain.  Its exact word proves a
terminal PBP socket at fixed rank, but the seam is non-Pascal and its
`COMP_3` was solved afresh.  It is not a ported `15->16` morphism.

These assertions are independently authenticated in
`MATH_AUDIT_AD_K15_CERTIFICATE_AND_C_COMPONENT_BOUNDARY_HALL_20260729.md`
and its pinned factor/compiler/word artifacts for `k=15`.  The `k=11,13`
rows are authenticated in
`MATH_THEOREM_K_RELATIVE_PPR_ROUTER_ATLAS_AND_PASCAL_REGENERATION_GATE_20260730.md`
and the raw-word carrier audits cited there.  They do not follow from the
`k=12,14` files listed in Section 2.

## 4. Pascal associativity and its exact boundary block

Let

\[
 P^{(a)}_{Z_a}(V)_i
   =Z_a\cup\bigcap_{v=0}^{a}V_{i+v},                \tag{4.1}
\]

where the fixed tags used at different stages are disjoint.

### Theorem 4.1 (Pascal associativity)

For all nonnegative `a,b` for which the windows exist,

\[
\boxed{
 P^{(b)}_{Z_b}\bigl(P^{(a)}_{Z_a}(V)\bigr)
   =P^{(a+b)}_{Z_a\cup Z_b}(V).}                    \tag{4.2}
\]

#### Proof

The old-coordinate core at index `i` is

\[
 \bigcap_{u=0}^{b}\bigcap_{v=0}^{a}V_{i+u+v}
 =\bigcap_{w=0}^{a+b}V_{i+w},                       \tag{4.3}
\]

because every `w=0,...,a+b` has a representation `u+v=w`.  Both fixed tags
occur in every transformed state.  \(\square\)

Now cut a base sequence between `V_c` and `V_(c+1)`, with at least `a`
states on each side.

### Theorem 4.2 (exact Pascal boundary bridge)

The order-`a` facet of the uncut concatenation decomposes as

\[
 P^{(a)}(V_L|V_R)
 =P^{(a)}(V_L)\ | B_1|\cdots|B_a\ | P^{(a)}(V_R), \tag{4.4}
\]

where the exactly `a` bridge states are

\[
\boxed{
 B_h=Z_a\cup
     \bigcap_{v=c-a+h}^{c+h}V_v,
 \qquad1\le h\le a.}                                \tag{4.5}
\]

If every crossing subwalk

\[
 V_{c-a+h},V_{c-a+h+1},\ldots,V_{c+h}
 \quad(1\le h\le a)                                  \tag{4.6}
\]

is geodesic, every `B_h` has the required rank.  For the complete bridge
sequence also to have strict Johnson transitions, the corresponding
`a+1`-transition collars must be protected.  Nested orders `a,b` give the
same `a+b` bridge states as the direct order-`a+b` facet only when the second
facet is applied to the **complete** first-stage sequence, including all its
bridges.

#### Proof

The order-`a` windows lying wholly on the left or right give the two outer
terms in (4.4).  A crossing window can start at exactly

\[
    c-a+1,c-a+2,\ldots,c,
\]

which gives (4.5).  There are no other starts.  Geodesicity removes exactly
`a` old coordinates.  The final assertion follows by applying (4.2) to the
whole uncut sequence; both iterated and direct constructions enumerate the
same crossing windows.  \(\square\)

Ignoring (4.5) is a genuine composition error.  An upper child window of
depth `q` crossing this interface depends on the base collar of

\[
    a+q                                             \tag{4.7}
\]

transitions.  Separate side certificates which do not export that collar
cannot imply upper-seam replay.

## 5. Cumulative phase credit and internal upper transport

For a chain of Pascal orders `a_1,...,a_m`, put

\[
    A_j=\sum_{h=1}^{j}a_h,
    \qquad
    Z^{(j)}=\bigcup_{h=1}^{j}Z_{a_h}.                \tag{5.1}
\]

Repeated application of the Pascal envelope identity together with
associativity (Theorems 3.1 of the preceding flat-phase note and 4.1 here)
gives

\[
\begin{aligned}
 E_q^{(j)}(p)&=Z^{(j)}\cup E_{q+A_j}^V(p+A_j),\\
 U_q^{(j)}(p,\ell)&=Z^{(j)}\cup
                    U_{q+A_j}^V(p+A_j,\ell).
                                                               \tag{5.2}
\end{aligned}
\]

For a fixed exposed stage below, abbreviate `A=A_j` and
`Z^(A)=Z^(j)`.

The complete base dependency collar of the displayed child cell is

\[
    [p-q,\ p+A_j+\ell-1].                            \tag{5.3}
\]

### Theorem 5.1 (cumulative phase credit)

If the base atlas is protected and supplies its selected flags through depth
`D`, then an exposed stage `j`, with deadline `d_j`, actual phase loss `f_j`,
and horizon `q_j=d_j-f_j`, is depth-valid under the universal implication
from depth `D` if and only if

\[
\boxed{q_j+A_j\le D.}                                \tag{5.4}
\]

If its immediate parent has residual protected depth

\[
    D_{j-1}=D-A_{j-1},
\]

then (5.4) is the one-step condition

\[
\boxed{f_j+(D_{j-1}-d_j)\ge a_j.}                    \tag{5.5}
\]

Every exposed prefix must satisfy (5.4).  If only the final nested facet is
used, only the final inequality is required.  Actual horizons compose; raw
flat counts need not.  A particular atlas with extra protection beyond its
declared depth can succeed when (5.4) fails; that does not contradict the
universal statement.

#### Proof

Equation (5.2) requests base flag depth `q_j+A_j`; it is available through
depth `D` exactly when (5.4) holds.  The same inequality compares the
shortest transformed positive run, of length `D+1-A_j`, with the required
length `q_j+1`.  Substituting `q_j=d_j-f_j` and
`D_(j-1)=D-A_(j-1)` gives (5.5).  Sharpness follows from a base run of exact
length `D+1`.  \(\square\)

There is also an exact internal upper formula.  On a protected/no-return base
collar through all `A+q` transitions

\[
    V_{i+1}=V_i-\alpha_i+\beta_i,
\]

one has

\[
\begin{aligned}
 P_i^{(A)}&=Z^{(A)}\cup
  \left(V_i\setminus\{\alpha_i,\ldots,\alpha_{i+A-1}\}\right),\\
 P_{i+1}^{(A)}&=P_i^{(A)}-\alpha_{i+A}+\beta_i,
                                                               \tag{5.6}
\end{aligned}
\]

and hence

\[
\boxed{
 \bigcup_{v=0}^{q}P_{i+v}^{(A)}
  =Z^{(A)}\cup
   \left(V_i\setminus\{\alpha_i,\ldots,\alpha_{i+A-1}\}\right)
   \cup\{\beta_i,\ldots,\beta_{i+q-1}\}.}           \tag{5.7}
\]

Thus protected internal upper witnesses compose through nested Pascal
facets.  Moving the intact event block across a phase wall changes lower
compiler horizons but not the internal middle sequence or the labels in
(5.7).  Reversal uses the correspondingly reversed indices.  New seams still
require the `A+q` collar audit (4.7).

## 6. Literal transparency and common-source amalgamation

Suppose the base owners are realized at depth `D` by source letters `R_p`.
The exact total-order old-core condition for a selected order-`A` provider is

\[
\boxed{
 \bigcap_{u=0}^{A}V_{i+u}
   =\bigcup_{p=i+A}^{i+D}R_p.}                       \tag{6.1}
\]

It must hold on every selected physical restriction, and every selected
child interval must hit all coordinates of the total fixed tag `Z^(A)`.
Stagewise facet transparency and stagewise tag hits imply (6.1) by induction
provided all starts are aligned and every stagewise equality and tag hit is
imposed again on every later descendant-selected restriction.  A tag hit on
a larger interval can disappear after restriction.  The total condition may
hold even when an unused intermediate presentation is not transparent.

Even transparent local modules do not compose unless their source choices
amalgamate.

### Lemma 6.1 (source amalgamation)

Let local modules prescribe source assignments on domains `S_j`.  If their
assignments agree on every overlap, define `Q_p` by the common value there
and by the unique local value elsewhere.  Assume

\[
    \bigcup_j S_j=\mathcal S,                         \tag{6.2}
\]

the entire global source-position set.  Assume each local assignment already
satisfies every owner equation wholly certified by its module, and that every
central window is either wholly certified by some module or belongs to the
explicitly enumerated cross-interface class.  If every window in the latter
class satisfies (1.2), then `Q` is a global common source.  Conversely, every
global common source restricts to agreeing local assignments.

#### Proof

Agreement makes `Q` well-defined.  The stated local and cross-interface
equations exhaust the central windows.  The converse is restriction.
\(\square\)

One may replace fixed assignments by local source fibres on possibly
different domains.  The exact condition is that their natural join on
overlaps, together with all cross-interface owner equations, is nonempty.
Separate local nonemptiness does not suffice.

## 7. Exact serial, parallel, and Pascal induction laws

### Theorem 7.1 (serial socket gluing)

Let guarded modules `B_1,...,B_s` be concatenated in a fixed order.  Retain
only protected target-cell edges whose full dependency collars lie in their
module guards.  Suppose:

1. every Pascal piece satisfies its certified phase-credit inequality, and
   every retained transported provider or upper witness keeps its complete
   dependency collar after all cuts, reversals, and gluings;
2. the owner pieces concatenate through legal seams and one global actual
   horizon map, and the resulting middle chronology contains every required
   middle owner exactly once;
3. the local source fibres have one common member `Q`, including every
   cross-interface owner equation;
4. retained protected target labels are distinct, the selected
   occurrence-labelled physical interval cells are distinct (they may overlap
   in source positions), and every selected edge remains exact under `Q`;
5. putting
   
   \[
   \mathcal T_{cas}=\mathcal T_{req}\setminus
                     \operatorname{dom}M_{prot},
   \qquad
   \mathcal C_{free}=\mathcal C_{phys}\setminus
                     \operatorname{im}M_{prot},       \tag{7.1}
   \]
   the graph
   
   \[
       T\sim C\quad\Longleftrightarrow\quad
       \lambda_Q(C)=T                               \tag{7.2}
   \]
   has a matching saturating `T_cas`;
6. the retained internal upper witnesses and the exhaustive literal
   noninternal-window catalogue—including every window through a Pascal
   bridge state (4.5) and every multi-interface window—together cover every
   upper target;
7. every interface passes residence, endpoint, terminal, and fixed-tag
   singleton checks.

Then the serial composite satisfies terminal PBP.

Relative to the frozen module interiors, clauses 3, 5, and 6 are necessary
as well as sufficient among completions required to be terminal PBPs with
upper targets witnessed by middle-chronology intervals, provided the local
source fibres are the full fibres allowed by the frozen constraints,
`C_phys` contains every allowed unallocated interval, and the
internal/noninternal upper catalogues are exhaustive.

#### Proof

Clauses 1--3 give one phase-valid reconstructed middle chronology.  The
protected and casualty matchings in clauses 4--5 cover the strict lower ideal
using one source.  Clauses 6--7 give every upper target and every physical boundary
obligation.  These three ideals exhaust the nonempty Boolean lattice.

For necessity, restrict any completing terminal-PBP source to the module
domains.  Every unprotected lower target has an actual unallocated witnessing
interval, giving (7.2).  Under the stated upper-by-middle requirement, every
upper target without a retained internal witness must occur in the exhaustive
noninternal window catalogue.  The fullness hypotheses prevent an omitted
local fibre, cell, or witness from evading the conclusion.  This necessity
claim does not apply to an arbitrary universal source whose upper masks are
allowed to arise by an unrelated mechanism.  \(\square\)

For more than two modules, clause 6 is global.  It may be checked
associatively by recomputing the complete suffix/prefix traces of each
partial composite.  Independent one-seam checks are sufficient only when
every casualty has been assigned to a one-seam grid; a witness spanning a
short intermediate module is otherwise a genuine multi-seam interval.

### Theorem 7.2 (parallel gluing)

Modules on the same chronology compose without new seam conditions if they
use one common `Q`, have disjoint target domains and disjoint selected
physical cells, and all selected edges remain exact under `Q`.  Their
matchings and internal upper witness sets then unite.  If their free cell
banks overlap, the exact replacement is one global Hall condition, not the
conjunction of their local Hall conditions.

#### Proof

Under the disjointness hypotheses the union of the local matchings is a
matching and every edge remains exact.  No physical chronology changes, so
there is no new upper or residence condition.  Overlapping free banks can
compete for cells, which is exactly the global Hall obstruction.  \(\square\)

### Theorem 7.3 (ported Pascal induction)

Let a child be assembled from ported parent modules by copy/facet orders
`a_j`, phase losses `f_j`, and serial/parallel gluings.  Cumulative orders
`A_j` are computed separately on each root-to-leaf nested Pascal ancestry
chain; orders of serial or parallel sibling pieces are not added.  Suppose:

1. the transformed pieces, canonical bridges, and any explicit replacement
   states form the exact child middle deck, and every exposed Pascal prefix
   on every ancestry chain satisfies the cumulative phase condition (5.4);
   every transition inside an explicit replacement block and at its boundary
   is a legal Johnson transition;
2. every transported literal provider satisfies total or stagewise facet
   transparency and all fixed-tag hits, and its entire transported dependency
   collar survives every child cut, reversal, bridge insertion, and gluing;
3. the Pascal bridges (4.5) are retained as the corresponding middle states;
   if a braid replaces or omits one, exact middle ownership is restored
   separately, every lower target/provider edge depending on that bridge is
   reclassified into the casualty ledger, and every dependent upper window
   is reclassified into the interface ledger;
4. occurrence-labelled transported images are injective on both shores:
   selected target labels are distinct after choosing one representative
   for each repeated label, their physical child intervals are distinct, and
   every selected transported edge remains exact under the common `Q` in
   condition 5;
5. all local source fibres and interface owner equations have one common
   member `Q`;
6. with `T_cas` and `C_free` defined by (7.1) after every transformation and
   allocation, the global casualty graph (7.2) has a matching saturating
   `T_cas` under `Q`;
7. the global internal/bridge/seam upper catalogue is complete and every
   physical interface passes residence and boundary replay, including legal
   endpoints, the terminal suffix, and every fixed-tag/top-singleton
   obligation.

Then the child is a terminal PBP.  If its output atlas, boundary fibre,
protected matching, and upper witnesses are separately verified and exported
as in every clause of Definition 1.2, it is ported and may be used as a parent
in the next application.  Therefore ported PBP morphisms are closed under a
Pascal odd-even composition only when compatibility includes a verified
Definition 1.2 output port whose declared type belongs to the next morphism's
input class.

#### Proof

Theorems 4.1--4.2 identify every interior and boundary state after all
Pascal transforms.  Condition 1 supplies the exact middle deck.  Theorem 5.1
gives phase availability, while (5.7) transports the protected internal
upper witnesses.  Conditions 2--4, including the full transported-collar
condition, give the transported protected lower
matching.  Conditions 5--6 and Theorem 7.1 complete the lower compiler under
one source.  Condition 7 completes the upper ideal and physical replay.
Only the additional verified export restores every clause of Definition 1.2;
when it does, induction is valid.  \(\square\)

On a depth drop, `D=d+1,a=1,f=0`, as in Theorem 2.1 and Corollary 2.2.  On a
plateau, `D=d,a=1`, so each inherited facet piece needs `f>=1`; the
lower target of every designated provider that is flat-shifted, truncated,
or cut enters the lower casualty bank.  Altered bridge middle owners are
handled by condition 3, and their dependent upper windows by condition 7.
The theorem does not assert that the required bank exists.

## 8. Sharp failure of compiler composition

Separate local Hall passes and distinct selected cells do not imply a common
compiler.

### Proposition 8.1

Let three physical source positions have maximal envelopes `{1,2}`, and let
their sole central owner be

\[
    T=\{1,2\},\qquad W=[0,2].                       \tag{8.1}
\]

Module A asks that cell `[0,0]` realize target `{1}`.  It is feasible with

\[
    (Q_0,Q_1,Q_2)=(\{1\},\{2\},\{2\}).             \tag{8.2}
\]

Module B asks that the distinct cell `[0,1]` realize target `{2}`.  It is
feasible with

\[
    (Q_0,Q_1,Q_2)=(\{2\},\{2\},\{1\}).             \tag{8.3}
\]

Both reconstruct (8.1), but no source satisfies both module requests.

#### Proof

Module A forces `Q_0={1}`.  Exactness of Module B forces
`Q_0 union Q_1={2}`, contradicting the first equality.  \(\square\)

Thus even identical middle ownership, separate compiler feasibility,
distinct targets, and distinct physical cells do not compose.  The common
source fibre in Theorem 7.1 is indispensable.  The other irreducible
interface failures are missing tag hits, collisions of transported
occurrences, omitted Pascal bridge states, and upper sockets lacking the
base collar (4.7).

## 9. Exact all-`k` implication and the remaining lemma

### Corollary 9.1

Assume one initial deadline-tight ported odd carrier, and assume every
subsequent odd-even step admits a ported Pascal PBP morphism satisfying
Theorem 7.3, while every
even-to-odd step admits a separately specified ported transition theorem.
Require in each case that the typed output socket belongs to the next
morphism's declared input class, and that the child has the exact middle deck
and deadline-tight number of source positions.  Then induction produces a
literal universal word of deadline length at every step; the monotone
deadline lower bound makes each such word optimal.

This is a theorem, but its existence hypothesis is not presently known.
The authenticated finite lineage proves only:

- `11->12` and `13->14`: terminal depth-drop PBPs with fresh compilers;
- `k=15`: a terminal non-Pascal two-component socket with a fresh compiler;
- carrier 3 at `15->16`: the exact one-flat `19+1+2` shifted Hall ledger,
  not a completed casualty bank or common source.

The exact smallest missing positive statement is therefore:

> **Ported plateau extension lemma (UNPROVED).**  For one explicit recursive
> PBBS/Pascal carrier family, every plateau step admits a one-flat
> order-one braid satisfying Theorem 7.3 and exports a nonempty protected
> matching, declared-depth transparent provider atlas, compatible boundary
> source fibre, and complete upper socket belonging to the same recursive
> port class required at the next step.

Proving only a terminal child compiler is enough for that one rank but does
not prove the next induction step.  Proving only phase balance, scalar Hall,
or upper seam replay is weaker still.

## 10. Audit boundary

The general proofs use no finite search.  The finite assertions in Section 2
and Corollary 2.2 import the already frozen exact reconstructions, compiler
outputs, and independent literal word replays listed there.

The following stronger claims are explicitly rejected:

1. no retained certificate has `t>0` phase-shift PBP;
2. a fresh terminal compiler is not a functorial compiler transport;
3. separate local common-source fibres need not intersect;
4. pairwise seam checks do not cover an unassigned multi-seam upper target;
5. Pascal side transforms without the bridge states (4.5) do not compose;
6. rank/tag ledgers do not imply occurrence-labelled injectivity.
