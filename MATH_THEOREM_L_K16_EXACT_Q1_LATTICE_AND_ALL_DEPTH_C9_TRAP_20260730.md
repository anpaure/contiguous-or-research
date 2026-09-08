# The exact q1 move lattice after the K16 length-eight orbit repair

Date: 2026-07-30

Status: proved algebraic theorem and hash-pinned finite certificates.  The
minimum support in the exact owner-degree plus q1 lattice is determined.  The
complete saved length-nine shallow-safe catalogue is rejected by literal
all-depth replay.  No global no-go is claimed for arbitrary compound or
nonlocal exchanges.

## 1. Executive statement

Let $F_\triangle$ be the triangle-orbit-repaired factor and let $F_8$ be
the factor obtained by the complete orbit of fifteen length-eight rethreads:

```text
F_triangle  scratch/k16_asymmetric_triangle_orbit_repair_20260729.json
SHA-256     6044bd63b7281c358c6c33399ccf2dd15143f783535cb6fe6b85a797c04affdc

F_8         scratch/k16_asymmetric_len8_orbit_repair_20260730.json
SHA-256     6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204
```

The following statements are proved.

1. The q1 matrix is the incidence matrix of the rank-$(7,9)$ Boolean
   inclusion graph.  Its nonzero Smith factors are all one.  Thus q1 alone
   has no torsion obstruction.
2. After middle-owner degree is imposed, every nonzero lattice circuit has
   at least six physical edge columns.  This is sharp: an inverse repaired
   triangle has three cuts and six signed edges.  Hence the exact circuit
   minimum is

   \[
   \boxed{\text{three cuts, or six signed physical edges}.}
   \]
3. All fifteen inverse triangles survive at $F_8$.  They split a primitive
   $\mathbb Z^{15}$ direct summand of the formal degree-plus-q1 lattice.
   Each single inverse is resident and leaves every lower-rank hole set
   unchanged, but reopens one arbitrary rank-eleven target.  These minimum
   circuits are genuine exact-q1 circuits and genuine all-depth anti-descent
   directions.
4. The fifteen inverse length-eight moves are not exact-q1 circuits.  Their
   q1 signatures have disjoint row supports, rank fifteen, Smith factors
   $1^{15}$, and zero integer kernel.  No nonempty combination of them is
   exact-q1 neutral.
5. On $F_8$, the first saved positive port cycles passing q1 and the
   selected lower-q2/upper-q3 ledger have length nine.  There are thirty,
   arranged as two labelled copies of fifteen signatures.  Their
   nonnegative exact-q1 kernel is zero.  More decisively, literal replay of
   every one gives

   \[
   \Delta H_{U,10}=2,\qquad
   \Delta H_{L,5}=1,\qquad
   \Delta H_{U,11}=-1,
   \]

   and therefore increases the complete compiler deficit by two.
6. The maximum compatible saved length-nine packet has seven atoms.  It
   appears to gain seven in the selected ledger, but its literal all-depth
   deficit changes from $93$ to $107$, a loss of fourteen.

The exact remaining algebra is not the q1 Smith kernel.  It is the
witness-extended path/automaton fibre for every fixed lower flag and every
arbitrary-width upper union.

## 2. The literal all-depth objective

For a factor $F$, let $H^-_s(F)$ be the number of missing lower targets
of rank $s<8$ in the forced fixed-length flag tower.  Let $H^+_s(F)$ be
the number of rank-$s>8$ targets which are not the union of any nonempty
contiguous interval of a component of $F$.  Define

\[
 \mathcal H(F)=\sum_{s<8}H^-_s(F)+\sum_{s>8}H^+_s(F).
\tag{2.1}
\]

This is the relevant hole count for the literal lower-flag/arbitrary-upper
compiler.  A hole in a prescribed fixed upper width is not counted if the
same target is realized by a different interval width.

The independently audited state $F_8$ has

\[
 H^-_6(F_8)=45,\qquad H^+_{11}(F_8)=48,
\tag{2.2}
\]

and every other term in (2.1) is zero.  Hence

\[
 \boxed{\mathcal H(F_8)=93.}
\tag{2.3}
\]

There are also fifteen fixed-width upper-q4 holes, but all fifteen rank-12
targets have arbitrary-width witnesses.  They therefore do not enter
$\mathcal H$.

The full length-eight orbit uses 120 pairwise distinct cuts and changes the
previous objective $45+63=108$ to $45+48=93$.  It retains minimum
positive run four.

## 3. The q1 inclusion graph and its Smith form

Let $J=J(16,8)$.  Put

\[
 \mathcal L={ [16]\choose 7},\qquad
 \mathcal U={ [16]\choose 9},
\]

and let $\Lambda$ be the bipartite graph on
$\mathcal L\sqcup\mathcal U$ with edge $LU$ when $L\subset U$.
Every physical Johnson edge $e=\{X,Y\}$ corresponds bijectively to

\[
 \phi(e)=(X\cap Y,X\cup Y)\in E(\Lambda).
\tag{3.1}
\]

Let $Q$ be the unsigned vertex-edge incidence matrix of $\Lambda$, and
let $P$ be the middle-vertex incidence matrix of $J$.  Thus $Qz=0$
means exact equality of both q1 load vectors, while $Pz=0$ means exact
middle-owner degree balance.  The formal exact lattice is

\[
 \mathcal K=\ker_{\mathbb Z}\!\begin{pmatrix}P\\Q\end{pmatrix}.
\tag{3.2}
\]

### Theorem 3.1 (q1 Smith saturation)

The matrix $Q$ has

\[
 22880\text{ rows},\qquad 411840\text{ columns},\qquad
 \operatorname{rank}Q=22879,
\tag{3.3}
\]

and all its nonzero Smith invariant factors equal one.  Consequently

\[
 \operatorname{rank}\ker_{\mathbb Z}Q=388961.
\tag{3.4}
\]

#### Proof

Multiplying every $\mathcal U$-row by $-1$ turns $Q$ into the oriented
incidence matrix of $\Lambda$.  The graph $\Lambda$ is connected: two
7-sets differing by one exchange lie below a common 9-set, the Johnson graph
on 7-sets is connected, and every 9-set has a 7-subset.  An oriented
incidence matrix of a connected graph has rank $|V|-1$, and a spanning-tree
minor has determinant $\pm1$.  This proves (3.3) and the Smith assertion.
Finally,

\[
 |V(\Lambda)|=2{16\choose7}=22880,qquad
 |E(\Lambda)|={16\choose7}{9\choose2}=411840,
\]

which gives (3.4).  \(\square\)

This theorem is only about $Q$.  It does not assert a Smith form for the
owner-augmented matrix in (3.2), nor does it impose coefficient-one use,
matching feasibility, residence, or deeper shadows.

## 4. Owner degree kills every q1 rectangle

### Theorem 4.1 (exact circuit girth)

Every nonzero element of $\mathcal K$ has edge support at least six.  At
the factors $F_\triangle$ and $F_8$, equality is attained by a literal
factor exchange with three deleted and three added edges.  Such a six-edge
witness is a primitive Graver circuit.

#### Proof

The support of a nonzero $Q$-circulation has minimum degree at least two in
the simple bipartite graph $\Lambda$, and hence contains an even cycle.
There is no support below four.  A five-edge circulation is also impossible:
a 4-cycle already uses all four edges of its $K_{2,2}$, while an additional
edge creates a support-degree-one vertex unless it belongs to another cycle;
the next bipartite cycle has six edges.

It remains to exclude support four.  A four-edge $Q$-circuit is a rectangle

\[
 (L_1,U_1),(L_2,U_2)\quad\longleftrightarrow\quad
 (L_1,U_2),(L_2,U_1),
\tag{4.1}
\]

with $L_1\ne L_2$ and $U_1\ne U_2$.  All four inclusions imply

\[
 L_1\cup L_2\subseteq U_1\cap U_2.
\]

The left side has size at least eight and the right side at most eight, so
both equal one 8-set $K$.  Write

\[
 L_1=C\cup\{a\},\quad L_2=C\cup\{b\},\quad
 U_1=K\cup\{x\},\quad U_2=K\cup\{y\},
\tag{4.2}
\]

where $|C|=6$ and $a,b,x,y$ are distinct.  The two old physical edges
have middle-endpoint multiset

\[
 \{K,K,C+a+x,C+b+y\},
\]

whereas the two crossed physical edges have multiset

\[
 \{K,K,C+a+y,C+b+x\}.
\]

The four displayed residual 8-sets are pairwise distinct.  Therefore the
owner boundary is nonzero, so (4.1) is not in $\ker P$.

The frozen inverse of the repaired triangle with transition order

\[
 (6708,9581,7768)
\tag{4.3}
\]

has three deleted and three added Johnson edges, has zero owner boundary,
and its q1 columns form a primitive six-cycle of $\Lambda$.  Hence the
lower bound is attained.  A conformal proper subrelation would have support
below six, which was just excluded, so the witness is Graver primitive.
\(\square\)

The theorem concerns the formal physical degree-plus-q1 lattice.  The
displayed witness also preserves the stronger directed successor matching;
this extra fact is part of the finite replay.

## 5. The two orbit blocks at $F_8$

### Theorem 5.1 (primitive inverse-triangle summand)

At $F_8$, all fifteen inverse triangles survive.  Their 90 edge columns
and 90 middle vertices are pairwise disjoint, and they are disjoint from the
240-vertex support of the length-eight surgery.  If their signed vectors are
$g_0,\ldots,g_{14}$, then

\[
 \bigoplus_{j=0}^{14}\mathbb Z g_j\cong\mathbb Z^{15}
\tag{5.1}
\]

is a primitive direct summand of $\mathcal K$.

#### Proof

Every $g_j$ is the rotation of (4.3), so Theorem 4.1 and literal replay put
it in $\mathcal K$.  Choose one restored edge $p_j$ private to $g_j$.
The coordinate map

\[
 \rho:\mathcal K\longrightarrow\mathbb Z^{15},\qquad
 \rho(z)=(z_{p_0},\ldots,z_{p_{14}})
\]

sends $g_j$ to the $j$-th standard basis vector.  It is therefore a
retraction onto their span, proving both splitting and primitivity.
\(\square\)

Every binary subset of these disjoint moves remains a physical
degree-and-q1 factor.  This does not assert that an arbitrary subset is
all-depth safe.  For each single move, however, equivariant literal replay
proves:

* exact q1 load equality;
* minimum positive run four;
* no change to any lower-rank hole set;
* one newly missing arbitrary rank-11 target (39911 for (4.3)); and
* one fewer fixed-width q4 hole, which does not compensate the missing
  arbitrary-width rank-11 target.

Thus every one of these fifteen minimum exact-q1 circuits increases
$\mathcal H$ by one.

### Theorem 5.2 (the inverse-C8 block is transverse)

Let $h_0,\ldots,h_{14}$ be the fifteen inverse length-eight moves at
$F_8$.  Every $Qh_j$ has eight nonzero unit rows, the fifteen row supports
are pairwise disjoint, and

\[
 \operatorname{rank}_{\mathbb Z}(Qh_0\ \cdots\ Qh_{14})=15.
\tag{5.2}
\]

The nonzero Smith factors of this 15-column block are $1^{15}$, and

\[
 \ker_{\mathbb Z}(Qh_0\ \cdots\ Qh_{14})=0.
\tag{5.3}
\]

#### Proof

Each column has a private unit q1 row, and the frozen replay verifies the
claimed disjoint supports.  The private-row minor is the identity matrix,
which proves (5.2), the Smith statement, and (5.3).  \(\square\)

The sector grading of every inverse C8 is

\[
 (-1,+1,+1,-1)
\tag{5.4}
\]

on $(L_{\bar z},L_z,U_{\bar z},U_z)$.  These moves are q1-coverage-safe by
using the surplus created by the forward orbit, but they are not exact-q1
neutral.  Each single inverse keeps all lower ranks and residence, and
reopens one arbitrary rank-11 target (48373 for the representative).

## 6. Finite generator certificates before and after $F_8$

The finite negatives have different bases and must not be merged.

### 6.1 The triangle source $F_\triangle$

The exact individual classification of all 2,023 reciprocal C2 switches is

\[
\begin{array}{c|rrrrrr}
(q1\text{-safe},\,\text{selected-deep-safe},\,\text{gainful})
 &(0,0,0)&(0,0,1)&(0,1,0)&(0,1,1)&(1,0,0)&(1,1,0)\\ \hline
\#&1140&90&643&75&15&60.
\end{array}
\tag{6.0}
\]

The exported C2--C5 catalogue contains only the 75 individually q1-unsafe,
selected-deep-safe, gainful C2 columns together with the 1,263 C3--C5
columns.  Peeling eliminates all 1,338 exported columns.  Therefore that
exported cone contains no nonzero q1-safe packet.  It does **not** follow
that an arbitrary packet from all 2,023 C2 switches is impossible: the
omitted nongainful or selected-deep-unsafe C2 columns may act as catalysts.

For the 1,263 individually gainful, selected-deep-safe C3--C5 columns, the
strict Gordan ray from the companion theorem is

\[
 \alpha=2\mathbf1_{W_1}+\mathbf1_{W_2},\qquad
 \alpha^TD_i\le-1\quad(1\le i\le1263),
\tag{6.1}
\]

with $|W_1|=732$ and $|W_2|=28$.  Hence even a fractional nonzero packet
from that catalogue violates a tight q1 row.  These are finite-catalogue
statements, not global Markov-basis theorems.

The supplied length-seven census reports that no positive, q1-safe,
selected-deep-safe separated port cycle exists through length seven.  Its
resource record does not byte-pin the executed binary to the retained frozen
C++ source, so this exhaustive minimum-length conclusion is scoped to that
supplied census.  The length-eight orbit is the first recorded such
source-relative safe positive atom, but Theorem 5.2 explains why it is not
an exact-q1 lattice circuit: it spends q1 surplus.

### 6.2 The new source $F_8$

Here “selected deep” means only the four signed families

\[
 \{\text{lower q1},\text{upper q1},\text{lower q2},\text{upper q3}\}.
\tag{6.2}

It does not mean the complete lower tower or arbitrary-width upper coverage.

Within valid positive-residence seams and pairwise cut-separated directed
port cycles containing a current-hole provider, the frozen census gives:

| length | q1-safe | q1-safe and selected-deep-safe |
|---:|---:|---:|
| 3 | 0 | 0 |
| 4 | 0 | 0 |
| 5 | 0 | 0 |
| 6 | 0 | 0 |
| 7 | 0 | 0 |
| 8 | 45 | 0 |
| 9 | 60 | 30 |

Every one of the thirty saved length-nine rows gains exactly one current
upper-q3 target.  They are two labelled copies of fifteen distinct q1
signatures.  At each rotation the two columns are equal.  The fifteen
distinct columns have pairwise-disjoint lower supports and pairwise-disjoint
upper supports; each has one $+1$ and one $-1$ on each shore, and every
negative row has source load two.  Consequently their signature matrix has
rank fifteen and Smith factors $1^{15}$.  Its integer kernel is the
saturated lattice generated by the fifteen differences between the two
labelled copies, while its nonnegative kernel is zero.  In particular:

\[
 \boxed{\text{no nonempty subset of the thirty C9 atoms is exact-q1 neutral}.}
\tag{6.3}

The census is complete for the q1-safe provider class.  Because q1 prefix
pruning was used, its q1-unsafe classification counts are not a complete
census of all unsafe cycles.  Also, the census JSON and resource record do
not byte-pin the executed binary to the subsequently modified C++ source;
the exhaustiveness claim is therefore scoped to the supplied frozen census.

## 7. Complete replay rejects every saved C9 atom

### Theorem 7.1 (atomwise all-depth trap)

Every one of the thirty saved q1/selected-deep-safe C9 atoms has the same
complete count profile:

\[
\begin{array}{c|ccccc|c}
 &H^-_6&H^-_5&H^+_{10}&H^+_{11}&\text{other }H^\pm_s&\mathcal H\\ \hline
F_8&45&0&0&48&0&93\\
F_8+C9&45&1&2&47&0&95.
\end{array}
\tag{7.1}
\]

Every atom retains minimum positive run four.  Thus the apparent unit gain
in upper q3 is accompanied by three newly missing compiler targets, and

\[
 \boxed{\Delta\mathcal H=+2.}
\tag{7.2}

#### Proof

The frozen all-objective audit independently materializes every saved cycle,
recomputes every fixed lower rank and every arbitrary-width upper union, and
obtains (7.1) for all thirty rows.  This is a literal finite replay, not an
inference from the selected four-family ledger.  \(\square\)

### Theorem 7.2 (the seven-atom shallow false descent)

The cut-conflict graph of the thirty saved C9 atoms consists of two labelled
copies over $\mathbb Z_{15}$, with within-copy forbidden differences
$\{4,11\}$ and cross-copy forbidden differences $\{0,4,11\}$.  Its
maximum compatible packet has size seven.  A certified maximum packet has

\[
 \Delta(H^-_6+H^+_{11})=-7
\tag{7.3}

but

\[
 \Delta H^+_{10}=14,\qquad
 \Delta H^-_5=7,\qquad
 \Delta H^+_{11}=-7.
\tag{7.4}

Therefore

\[
 \boxed{\mathcal H:93\longmapsto107,\qquad\Delta\mathcal H=+14.}
\tag{7.5}

The packet remains q1-complete and resident, but is not exact-q1 neutral:
on each q1 shore its signed delta has fourteen rows, seven $+1$ and seven
$-1$, with every loss changing load $2\to1$.

#### Proof

Multiplication by four identifies the shift-conflict graph with $C_{15}$,
so its independence number is $\lfloor15/2\rfloor=7$.  The materialized
seven-cycle witness attains the bound.  Its complete physical replay gives
(7.4), while the separate q1 signature replay gives the final assertion.
Equation (7.5) follows.  \(\square\)

This is the decisive normalization correction.  The selected ledger sees
only the last term of (7.4).  The complete compiler sees all three.

## 8. Exact all-depth witness lift

The omitted upper-q2 row happens to agree with arbitrary rank-10 failure for
the C9 witnesses above.  It cannot replace arbitrary-width upper coverage in
general: $F_8$ itself has fifteen fixed-q4 holes and zero arbitrary
rank-12 holes.

Let $\mathcal A$ be the allowed directed Johnson arcs on the middle layer,
and let $x_e\in\{0,1\}$ be a successor permutation.  Put
$W={16\choose8}=12870$.

For a lower target $L$ of rank $8-q$, let $\mathcal P^-_L$ be the set
of directed paths of exactly $q$ arcs whose $q+1$ middle vertices have
intersection $L$.  For an upper target $U$, including $U=[16]$, let
$\mathcal P^+_U$ be the set of directed paths of at most $W-1$ arcs whose
middle vertices have union $U$.

### Theorem 8.1 (simultaneous path lift)

The successor factor has the complete lower flag tower and all
arbitrary-width upper targets if and only if there are binary variables
$y_{T,P}$ satisfying, for every target $T$,

\[
 \sum_{P\in\mathcal P_T}y_{T,P}\ge1,
 \qquad
 y_{T,P}\le x_e\quad(e\in P).
\tag{8.1}

Here $\mathcal P_T=\mathcal P^-_T$ for a lower target and
$\mathcal P_T=\mathcal P^+_T$ for an upper target.

#### Proof

If $y_{T,P}=1$, all arcs of $P$ are selected, so $P$ is a literal
contiguous witness for $T$.  Conversely, choose one actual witness path
for each covered target and set its $y$-variable to one.  An upper
interval never needs to traverse a component twice; hence length at most
$W-1$ is sufficient.  \(\square\)

For an incomplete factor, introduce one binary hole variable $h_T$ and
replace the first inequality in (8.1) by

\[
 h_T+\sum_{P\in\mathcal P_T}y_{T,P}\ge1.
\tag{8.1a}
\]

Minimizing $\sum_T h_T$ gives exactly $\mathcal H$: a covered target can
set $h_T=0$ by choosing a witness, while an uncovered target forces
$h_T=1$.  If exact q1 load equality rather than q1 coverage is required,
retain the separate equality $Qx=b_{q1}$ in this lifted system.

### Theorem 8.2 (upper accumulated-union cut dual)

For a fixed upper target $U$, including the full ground set, form the
automaton with states

\[
 (v,S),\qquad v\subseteq U,\quad v\subseteq S\subseteq U,\quad |v|=8.
\]

Its starts are $(v,v)$, its accepting states have $S=U$, and a physical
arc $e=(v,w)$ with $w\subseteq U$ induces

\[
 (v,S)\longrightarrow(w,S\cup w).
\tag{8.2}

For any state cut $K$ containing all starts and no accepting state, let
$c_e(K)$ be the number of copies of physical arc $e$ directed from
$K$ to its complement.  Then $U$ is covered if and only if the integral
successor vector satisfies every cut row

\[
 \boxed{\sum_{e\in\mathcal A}c_e(K)x_e\ge1.}
\tag{8.3}

#### Proof

An accepting path crosses every start/accept cut, proving necessity.  If no
accepting path exists, let $K$ be the states reachable from all starts
using selected arcs.  No selected transition leaves $K$, so the left side
of (8.3) is zero.  This proves sufficiency.  \(\square\)

A minimum cut separates (8.3) in time polynomial in the explicitly expanded
automaton.  This is not claimed polynomial in a compressed parameter $k$.
A layered accumulated-intersection automaton gives the analogous fixed
lower rows.

After slacks are introduced, (8.1)--(8.1a) form an integer lifted fibre and
objective.  Standard conformal Graver decomposition applies in that lifted
space.  Projection to the edge-only matrix $Q$, or even to fixed
short-shadow columns, does not
preserve the conclusion: an arbitrary-width upper witness may traverse
several collars, and its creation or destruction is not additive in
separately exported port-cycle columns.  A compound must either be replayed
literally or represented together with its witness variables.

## 9. Exact boundary

What is closed:

* the q1-only Smith quotient has no torsion;
* the exact owner-plus-q1 circuit minimum is six edges/three cuts;
* a primitive fifteen-dimensional minimum-circuit summand survives at
  $F_8$, but its single generators are all-depth anti-descent;
* the inverse-C8 orbit and the saved positive C9 catalogue contain no
  nonempty exact-q1-neutral subset;
* no saved C9 atom, nor its maximum compatible seven-packet, is a complete
  objective descent.

What remains open:

* a compound mixing other deep-unsafe, nongainful, longer, or overlapping
  generators may cancel both q1 and all-depth debts;
* the present certificates do not enumerate all support-six circuits of
  $\mathcal K$, so they do not prove every minimum circuit anti-productive;
* arbitrary-width witness effects are nonadditive outside the lifted path
  fibre; and
* no all-depth-safe productive exact-q1 circuit, and no complete K16
  compiler, is proved here.

Thus the next exact search object is a negative-$\mathcal H$ or
hole-filling Graver move in the simultaneous degree/q1/path-witness lift,
not a further Smith computation of the q1 projection.

## 10. Frozen certificates

```text
scratch/audit_k16_len8_factor_inverse_orbit_lattice_20260730.py
SHA-256 e213718176cde9b56410e2f4a3d54a12c38fc72cfae5a53c7d43845b401c3075

scratch/k16_len8_factor_inverse_orbit_lattice_20260730.audit.json
SHA-256 a9d5f141f23ab9c51e500e06cab52bca2757ec979c3405ea15bb3c9e126e4f77

scratch/audit_k16_len8_source_c9_q1_signature_kernel_20260730.py
SHA-256 de1ce0bc11d2b7bfb71f2c8db87e151fd793578fae96478f99b32df722024d21

scratch/k16_len8_source_c9_q1_signature_kernel_20260730.audit.json
SHA-256 95f4aa440eb75238cc945ec95230c5fb17ecad578d62b4ef9f40aa6c2018f5de

scratch/k16_asymmetric_len8_orbit_source_long_cycles_3_9_20260730.audit.json
SHA-256 b55983f3de8816c4457fec92d713b26ebc833304e6f19cde548e7ffee95d122f

scratch/audit_k16_long_cycle_full_objective_20260730.py
SHA-256 9f6913445e6793a10b29942e8802a12972586e2e5571aa6c2aedcd682fbf9485

scratch/solve_k16_asymmetric_compound_cycle_packing_20260730.py
SHA-256 8d7761b9f37d74b27499e3c38e347abbc628505ac06bc7e92a87f61dbb199ea6

scratch/k16_asymmetric_len8_orbit_source_len9_full_objective_20260730.audit.json
SHA-256 ce024402a264ff994b5b6583702e7553dd9a53703fbfeed835f2c2695662af72

scratch/k16_asymmetric_len8_then_len9_maxpacking_repair_20260730.packing.audit.json
SHA-256 849c32f148bbbe1bbc4b7475bf788747603616a0a1e0c502b50b481caca33fdb

scratch/k16_asymmetric_len8_then_len9_maxpacking_repair_20260730.json
SHA-256 81118d55bc16a7b80ae5f95355a0d4a81cdc841dad6fe839cb16501c38b36473

scratch/k16_asymmetric_len8_then_len9_maxpacking_repair_20260730.audit.json
SHA-256 5ea654e46119b11f2f9e451841adfd034a2e9ba1873b8addf467f1fe66e860f4
```

The general alternating-component, protected-load augmented-Graver, and
strict-ray proofs used above are in
`MATH_THEOREM_L_Q1_MOVE_LATTICE_GRAVER_AND_K16_STRICT_RAY_20260730.md`.
