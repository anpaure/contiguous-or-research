# Half-integral hypercircuits and exact residual-slot absorption

Date: 2026-08-01  
Lane: Thread D / prospective `M0` / bounded-defect rounding  
Status: exact support-circuit characterization, exact conditional absorber,
and a smallest literal Boolean one-slot obstruction.  No all-dimensional
rounding or `B+O(1)` claim is made.

## 0. Verdict

There are two logically separate steps in a proposed odd-circuit rounding.

1. A half-integral point can be rounded *inside its support* after omitting a
   set of upper colours.  The exact support obstruction is not an ordinary
   matching odd cycle.  It is an XOR/NAND system: the `R,L,T` equality rows
   form a parity graph, while the head rows give NAND clauses.  A minimal
   parity obstruction is a chordless odd **hypercircuit** whose vertices are
   half-integral diamond or residual-matching columns.
2. An omitted colour can be put back using one residual predecessor edge and
   one unused head exactly when these three objects form a literal oriented
   Boolean diamond.  For several omitted colours the exact absorber is again
   a common independent set in colour, residual-slot, head, and contracted
   graphic matroids.

Thus the `C=Cat_m` unused slots do not by themselves prove absorption.  If
`k` colours are first omitted, there are actually `C+k` residual predecessor
slots and `C+k` unused heads, so scalar capacity is never the issue.  The
missing assertion is the structured three-/four-resource matching.

This distinction is already sharp at `m=3`.  There is a literal prospective
`M0` partial state with one missing upper colour, a perfect residual incidence
matching, and six residual slots, but no compatible one-slot insertion.  A
two-colour alternating chain repairs it.  Hence even the smallest Boolean
case requires compound rather than independent slot absorption.

There is also an independently audited `m=3` half-integral **vertex** whose
fractional circuit consists of eight diamond columns and no fractional
residual `y` column.  Its four circuit colours have restricted integral
matching number only two.  Thus neither half-integrality nor global Catalan
slack permits one to charge each fractional circuit to a residual slot in its
own support.  The slot theorem below intentionally starts only *after* an
integral partial state and its literal residual matching have been produced.

The tight-pivot bank is safe under every theorem below: integral protected
columns are frozen before the half-integral support is formed, and a residual
slot insertion uses only resources unused by the protected state.

## 1. The prospective system

Use the notation

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal O={ [2m-1]\choose m},\qquad
 \mathcal U={ [2m-1]\choose m+1},
\]

and

\[
 W=|\mathcal L|=|\mathcal O|,\qquad
 U=|\mathcal U|,\qquad C=W-U=\operatorname {Cat}_m.
\]

An oriented diamond is

\[
 d=(R;L,T,V),\qquad T\cap V=L,\quad T\cup V=R.       \tag{1.1}
\]

The exact prospective system has diamond variables `x_d` and residual
incidence variables `y_(L,T)`, with

\[
\begin{aligned}
 \sum_{d:R(d)=R}x_d&=1,\tag{1.2a}\\
 \sum_{d:L(d)=L}x_d+\sum_{T\supset L}y_{L,T}&=1,\tag{1.2b}\\
 \sum_{d:T(d)=T}x_d+\sum_{L\subset T}y_{L,T}&=1,\tag{1.2c}\\
 \sum_{d:V(d)=V}x_d&\le1.\tag{1.2d}
\end{aligned}
\]

Integral solutions of (1.2) are exactly the oriented-diamond selections with
the residual Hall completion described in the prospective-`M0` theorem.

## 2. Exact half-integral support system

This section is conditional, not an extreme-point classification.  Exact
`m=3` audits exhibit a vertex of the unrestricted prospective system with
denominator `11`, and a vertex on a face fixing a two-arc predecessor path
with denominator `4`.  Thus a global proof cannot decompose all vertices
into half-integral odd circuits.  The point of this section is to state the
exact rounding and absorption law on the half-integral face, where an
odd-circuit argument is meaningful.  The dependency-clean extreme-point
statement is recorded in
`MATH_THEOREM_THREAD_D_PROSPECTIVE_DIAMOND_EXTREME_DENOMINATORS_20260801.md`.

Let `w=(x,y)` be a feasible point of (1.2) whose coordinates lie in
`{0,1/2,1}`.  Freeze all columns of value one and remove their already
satisfied rows.  Let `S` be the remaining half-integral columns.

Every residual `R,L,T` equality row is incident with exactly two columns of
`S`.  Join those two columns by an edge labelled by that resource.  Call the
resulting multigraph `K_=`.  If a head row has two half-integral diamond
columns, join them by a **head-conflict edge**; head rows with zero or one
half-integral column require no edge.

### Theorem 2.1 (XOR/NAND characterization)

There is an integral solution supported on the frozen columns and `S` if and
only if there are bits `epsilon_s` (`s in S`) satisfying

\[
 \epsilon_s\mathbin\oplus\epsilon_t=1
       \quad(st\in E(K_=)),                              \tag{2.1}
\]

and

\[
 \epsilon_s+\epsilon_t\le1
       \quad(st\text{ a head-conflict edge}).            \tag{2.2}
\]

Equivalently, every component of `K_=` must be bipartite; after replacing
each bipartite component by its one phase bit, the head-conflict edges form a
2-SAT instance in those phase bits.

#### Proof

Every equality row has residual right side one and two columns of value
`1/2`, so an integral support choice must select exactly one of them.  This
is (2.1).  A head row is only a capacity row, so two supported columns may
not both be selected; this is exactly (2.2).  These are all rows of (1.2).

The XOR equations are soluble on a connected component precisely when it is
bipartite, and then all column bits are determined by one global phase.  On
substitution, each NAND inequality is a 2-CNF clause in one or two component
phase bits.  The converse reconstruction is immediate.  \(\square\)

### Corollary 2.2 (the actual odd circuit)

An edge-minimal obstruction in the equality rows is a chordless odd cycle of
`K_=`.  Its vertices are columns of the four-resource system and its edges
are alternately shared `R,L,T` rows.  It is therefore a hypercircuit of the
oriented-diamond matrix, not necessarily an alternating cycle in the
tail--head bipartite graph.

Head conflicts can obstruct a bipartite equality support by rejecting both
of its phases.  Consequently “all extreme points are independent odd
cycles” would still be insufficient even under an additional
half-integrality theorem.

## 3. Exact support defect

For a set `D` of half-integral upper rows, **open** `R in D` by replacing its
XOR equation, whose endpoint columns are `s_R,t_R`, by

\[
                      \epsilon_{s_R}=\epsilon_{t_R}=0.  \tag{3.1}
\]

All other `R,L,T` equations and all head conflicts remain literal.  Define

\[
 \kappa(w)=\min\{|D|:\text{the opened XOR/NAND system is feasible}\}, \tag{3.2}
\]

with value infinity if no upper-row opening suffices.  Protected upper rows
are forbidden from `D`.

### Theorem 3.1 (exact support-contained colour defect)

`kappa(w)` is exactly the minimum number of upper colours omitted by an
integral partial solution using only the support of `w` and retaining every
protected integral column.

If `k=kappa(w)<infinity`, the partial solution contains `U-k` diamonds,
`C+k` residual incidence edges, and has `C+k` unused heads.

#### Proof

For an unopened colour, its two half columns must contain exactly one chosen
column.  Omitting the colour means choosing neither, exactly (3.1).
Theorem 2.1 handles every other row, proving the first assertion.

The `L` and `T` equalities partition the `W` predecessor resources between
diamond and residual columns.  Therefore `U-k` selected diamonds leave
`W-(U-k)=C+k` residual edges.  Head injectivity uses `U-k` of the `W` heads,
leaving the same number `C+k`.  \(\square\)

### Lemma 3.2 (clean odd-circuit cost one)

Suppose one component of `K_=` is unicyclic, its unique cycle is odd, and an
upper-row edge `R` lies on that cycle.  Delete that edge.  If the phase with
both endpoints of the deleted edge equal to zero satisfies all incident head
conflicts, then that component has exact colour defect one.

#### Proof

Deleting an edge from an odd cycle leaves an even-length path between its
endpoints.  They therefore lie in the same bipartition class.  Set that
class to zero and alternate over the component.  Every remaining equality
is satisfied and `R` is omitted.  Head cleanliness is precisely (2.2).
The original odd cycle rules out defect zero.  \(\square\)

An odd equality circuit containing no openable upper edge is not repaired by
this lemma.  Nor does the lemma suppress contradictory head clauses.  Those
are exact reasons a general extreme-point theorem must track hypercircuits,
not just their number.

### Proposition 3.3 (an extreme `m=3` circuit already has matching defect two)

The following eight genuine diamonds, each with weight `1/2`, form the
fractional circuit block of a vertex of (1.2):

\[
\begin{array}{c|c|c|c}
R&L&T&V\\ \hline
1234&14&124&134\\
1234&12&123&124\\
1235&13&123&135\\
1235&15&135&125\\
1245&12&124&125\\
1245&14&145&124\\
1345&15&145&135\\
1345&13&135&134.
\end{array}                                             \tag{3.3}
\]

Every displayed `R,L,T,V` resource has total load one.  The compatibility
graph in which two columns are adjacent when they have distinct values in
all four roles is the three-cube `Q_3`; nevertheless its maximum clique, and
hence the maximum integral four-role matching contained in (3.3), has size
two.  The four fractional colours therefore have restricted matching defect
two.

Adding the integral diamond `(2345;23,234,235)` and the five integral
residual pairs

\[
25\to125,quad34\to134,quad35\to235,quad
24\to245,quad45\to345                            \tag{3.4}
\]

gives a feasible full point of (1.2).  Its fourteen positive columns have
rank fourteen against active equality/head rows, so the point is a vertex.
In particular, the fractional block (3.3) contains no residual `y` mass at
all.

#### Consequence

Lemma 3.2 is a genuinely conditional clean-circuit lemma, not a
classification of extreme points.  The circuit (3.3) cannot be rounded by
assigning one locally supported residual slot to each odd parity feature.
Any bounded-defect proof must either introduce off-support predecessor
columns, perform a compound multi-colour move, or choose a better fractional
point prospectively.

## 4. One residual-slot absorber

Let `(X,Y)` be an integral partial state which omits a colour `R`, where `Y`
is its residual perfect incidence matching.  Put

\[
 H_0=\mathcal O-V(X).                                  \tag{4.1}
\]

For `y=(L,T) in Y` and `V in H_0`, call `(y,V)` an `R`-slot when

\[
                         T\cap V=L,\qquad T\cup V=R.    \tag{4.2}
\]

### Lemma 4.1 (literal one-slot insertion)

The operation

\[
        X'=X\cup\{(R;L,T,V)\},\qquad Y'=Y-\{(L,T)\}    \tag{4.3}
\]

is an integral prospective-`M0` state filling `R` if and only if `(y,V)` is
an `R`-slot.  It changes no previously selected diamond and hence preserves
the tight-pivot bank literally.

If the rooted arcs of `X` form a forest, (4.3) preserves the forest exactly
when `T` and `V` lie in distinct components of that forest.

#### Proof

Removing `y` and inserting the diamond uses the same lower and tail
resources, so every `L,T` equality remains exact.  The missing upper row is
filled once, and `V in H_0` preserves the head capacity.  The Boolean
identities (4.2) are exactly the oriented-diamond identities.  These
conditions are also plainly necessary if no other column changes.

After contracting every component of the old forest, the new rooted arc is
`T->V`.  It is graphic-independent exactly when its endpoints are distinct
contracted vertices.  \(\square\)

Thus a clean odd circuit satisfying Lemma 3.2 is completely absorbed at
zero final defect whenever its omitted colour has a safe slot (4.2).

### Lemma 4.2 (slot transposition and alternating chains)

Let `e=(R;L_e,T_e,V_e)` be an unprotected selected diamond, let
`y=(L,T) in Y`, and let `V` be an unused head such that
`d=(R;L,T,V)` is a diamond.  Then

\[
\begin{aligned}
 X'&=X-\{e\}+\{d\},\\
 Y'&=Y-\{(L,T)\}+\{(L_e,T_e)\}                         \tag{4.4}
\end{aligned}
\]

is an exact prospective state with the same colour set.  It consumes the
slot `(L,T;V)` and releases `(L_e,T_e;V_e)`.  Conversely, every one-colour
change of representative which leaves all other columns fixed has this
form.

If the old rooted arcs are a forest, the new rooted arcs are a forest iff
`T` and `V` lie in distinct components after deleting `T_e->V_e`.

#### Proof

The exchanged predecessor edges use exactly the same two lower resources
and the same two tail resources before and after (4.4).  The old and new
diamonds have the same upper colour, while the head exchange consumes one
unused head and releases the old one.  This proves every partition row and
also necessity.  The graphic statement is the fundamental-cycle test after
the old arc is deleted.  \(\square\)

Iterating (4.4) gives the precise alternating-chain model: a current slot
reroutes one selected colour and the released predecessor/head pair becomes
the next slot.  The chain terminates by applying Lemma 4.1 to an omitted
colour.  Such a chain is protected exactly when none of its rerouted
diamonds belongs to the tight-pivot bank.

## 5. Several defects and the exact absorber rank

Let `D` be the omitted colour set of a partial state `(X,Y)`.  Form the
absorber ground set

\[
 \mathcal A_D=\{(R,y,V):R\in D,\ y=(L,T)\in Y,\ V\in H_0,
                 \ (R;L,T,V)\text{ is a diamond}\}.     \tag{5.1}
\]

On `A_D` take the partition matroids by `R`, by `y`, and by `V`, and the
graphic matroid of the arcs `T->V` after contracting the rooted forest of
`X`.  Write `nu_D(X,Y)` for their common-independence number.

### Theorem 5.1 (exact compound absorber)

All omitted colours are absorbed without changing `X` if and only if

\[
                         \nu_D(X,Y)=|D|.                \tag{5.2}
\]

More generally, the exact number left unabsorbed by this fixed partial state
is

\[
                         |D|-\nu_D(X,Y).                \tag{5.3}
\]

For a half-integral point `w`, the best defect obtainable by support rounding
followed by residual-slot absorption is therefore

\[
 \delta_{\rm slot}(w)=
 \min_{D,\epsilon}\bigl(|D|-\nu_D(X_\epsilon,Y_\epsilon)\bigr),       \tag{5.4}
\]

where `(D,epsilon)` ranges over feasible opened systems in Section 3.

#### Proof

A set of absorbers must use every missing colour at most once, distinct
residual matching edges, and distinct heads.  These are the first three
matroids.  The selected new rooted arcs must remain acyclic after the old
forest is contracted, which is exactly the fourth.  Applying Lemma 4.1 to
the common independent set gives the forward construction.  Every
fixed-`X` absorption has precisely these four properties, proving necessity
and (5.3).  Minimizing over support roundings gives (5.4).  \(\square\)

Equation (5.2), not `C>=|D|`, is the exact gate.  It is again a four-matroid
common-independence problem; no ordinary Hall formula is being asserted.

For completeness, let `Gamma_P(X,Y)` be the state graph generated by the
protected slot transpositions (4.4), and define

\[
 r_P(X,Y;D)=\min\{q:\text{some state at distance }q
                   \text{ has }\nu_D=|D|\}.             \tag{5.5}
\]

Then the exact compound service cost, counting the `|D|` final insertions and
the rerouted existing representatives, is

\[
                         |D|+r_P(X,Y;D).                 \tag{5.6}
\]

This is an exact state-space characterization rather than a claimed
polynomial min--max theorem.  Proposition 6.1 below has `|D|=1`, initial
absorber rank zero, `r_P=1`, and hence compound service cost two.

## 6. Why the number of Catalan slots is insufficient

For one colour `R`, define its literal slot row

\[
 N_R(X,Y)=\{(L,T)\in Y:T\subset R,
       \ R-(T-L)\in H_0\}.                             \tag{6.1}
\]

The induced head is unique.  Lemma 4.1 says one-slot absorption is possible
exactly when `N_R` contains a graphically safe member.  The cardinalities
`|Y|=|H_0|=C+1` give no lower bound on (6.1).

There is a dimension-uniform local blocker.  Let

\[
 R=\{a_0,\ldots,a_m\},\qquad x\notin R,
\]

with cyclic subscripts, and select the `m+1` diamonds

\[
\begin{aligned}
 T_i&=R-\{a_i\},\\
 L_i&=R-\{a_i,a_{i+1}\},\\
 V_i&=L_i\cup\{x\},\\
 R_i&=(R-\{a_i\})\cup\{x\}.                         \tag{6.2}
\end{aligned}
\]

Their `R_i,L_i,T_i,V_i` values are separately injective, so all four local
partition rows are legal.  But the `T_i` consume every middle facet of `R`.
Consequently no residual predecessor edge can have tail `T subset R`, and
`N_R` is empty.  This is a local obstruction only; (6.2) is not claimed to
extend to a full state for every `m`.

At `m=3`, however, it *does* extend to a literal residual perfect matching,
giving the smallest exact Boolean certificate.

### Proposition 6.1 (smallest one-slot obstruction, service radius two)

On `[5]`, omit `R=1234` and select

\[
\begin{array}{c|c|c|c}
\text{colour}&L&T&V\\ \hline
2345&34&234&345\\
1345&14&134&145\\
1245&12&124&125\\
1235&23&123&235.
\end{array}                                             \tag{6.3}

The residual predecessor matching may be

\[
 13\!\to135,quad15\!\to125,quad24\!\to245,quad
 25\!\to235,quad35\!\to345,quad45\!\to145.         \tag{6.4}

All four facets `123,124,134,234` of the missing colour are already selected
as tails, so (6.1) is empty.  Hence service radius one is impossible.

Nevertheless the two-colour chain

\[
 (2345;34,234,345)\longmapsto(2345;24,245,234),         \tag{6.5}
\]

followed by

\[
                  (1234;34,234,134)                    \tag{6.6}

is legal.  The final residual matching is (6.4) with `24->245` removed, and
all five upper colours and all `L,T,V` resources are injective.  Thus the
minimum number of colour representatives serviced by a compound chain is
exactly two.

#### Proof

Every intersection and union in (6.3), (6.5), and (6.6) is displayed
literally.  The six pairs in (6.4) use exactly the lower and tail vertices
not used in (6.3).  The absence of a tail facet proves the lower bound.

After (6.5), the old predecessor pair `34->234` becomes residual and the
pair `24->245` is consumed.  Its new head `234` was unused.  Equation (6.6)
then consumes `34->234` and uses the unused head `134`.  Direct inspection
gives distinct selected lower vertices `24,34,14,12,23`, distinct tails
`245,234,134,124,123`, and distinct heads `234,134,145,125,235`.
\(\square\)

This proposition does not contradict the `329` positive full matchings at
`m=3`: it proves that a particular partial rounding cannot be finished by an
independent one-slot move, while a compound reroute reaches a full matching.

## 7. Cycle breaking versus half-integral absorption

If one starts from a full colour/tail/head matching rather than a fractional
point, its rooted arcs form paths and directed cycles.  Removing one cycle
edge opens a colour and produces one extra residual predecessor slot only if
the removed diamond's predecessor edge is returned to `Y`.  Re-inserting the
colour through a different slot is exactly Lemma 4.1.  It reduces the cycle
count precisely when the new tail and head lie in distinct components after
the old edge is removed.

The displayed fixed-`M0`, `m=3` audit has two cyclic full matchings and ten
cycle edges.  Every one of those ten edges has a graphically safe one-slot
reroute.  This is positive finite evidence, not a theorem: Proposition 6.1
shows that prospective partial states already require a compound chain.

## 8. Precise surviving bounded-defect gate

A `B+O(1)` theorem would follow from the following two additional statements
for a suitable half-integral (or otherwise bounded-denominator) prospective
point retaining the tight pivot:

1. its support defect `kappa(w)` is bounded; and
2. the corresponding absorber rank satisfies

\[
                 \kappa(w)-\nu_D(X,Y)=O(1),             \tag{8.1}
\]

including the contracted graphic row.

Neither follows from the number `C` of unused slots.  The first is a parity
plus head-holonomy assertion about fractional extreme components; the second
is a compound Boolean-diamond routing assertion.  Proposition 6.1 identifies
the first necessary compound primitive: a two-colour alternating chain.

## 9. Exact audit

The finite claims in Sections 6--7 are independently replayed by

* `scratch/audit_threadD_m3_residual_slot_absorbers_20260801.py`;
* `scratch/threadD_m3_residual_slot_absorbers_20260801.audit.json`.

The extreme circuit in Proposition 3.3 is replayed by

* `scratch/audit_threadD_boolean_parity_circuit_cslot_nogo_20260801.py`;
* `scratch/audit_threadD_boolean_parity_circuit_cslot_nogo_20260801.audit.json`.

The non-half-integral scope warning in Section 2 is replayed by

* `scratch/audit_threadD_oriented_diamond_vertex_denominators_20260801.py`;
* `scratch/threadD_oriented_diamond_denominator11_vertex_20260801.audit.json`;
* `scratch/audit_threadD_protected_face_vertex_denominators_20260801.py`;
* `scratch/threadD_protected_path_denominator4_vertex_20260801.audit.json`.

The symbolic results in Sections 2--5 use no finite computation.
