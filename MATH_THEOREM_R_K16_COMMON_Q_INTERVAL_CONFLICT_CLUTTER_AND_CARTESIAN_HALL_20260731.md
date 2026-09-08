# The c7be common-Q gate: bounded local conflict clutter and Cartesian Hall

Date: 2026-07-31  
Lane: R  
Status: unconditional abstract theorems; exact specialization to the frozen
`c7be...` target order and pinned P/Q schedule.  K16 equality was closed by
a separate construction; this note claims only the reusable compiler theorem.

## 1. Endpoint-independent setup and scope

Let \(P=\{0,\ldots,n-1\}\) be the physical positions.  Let the middle rows
be labelled intervals

\[
 (T_i,I_i),
\]

and put \(D=\max_i|I_i|\).  Define

\[
 E_p=\bigcap_{i:p\in I_i}T_i.                                      \tag{1.1}
\]

We assume that every (E_p) is nonempty and that the maximal envelope word
already realizes every middle row:

\[
 \bigcup_{p\in I_i}E_p=T_i.                                        \tag{1.2}
\]

The physical lower cells form a set \({\cal C}\) of **distinct** intervals
\(C\subseteq P\), each of length at most \(d\).  The compiler case has
\(D=d+1\); c7be has \(d=3,D=4\).  A candidate edge
is a pair \(e=(S,C)\), where \(S\) is a nonempty lower target and capping
\(E_p\) by \(S\) on \(C\), by itself,

1. leaves all physical letters nonempty;
2. leaves every middle row exact; and
3. realizes (S) exactly on (C).

This is precisely the individually feasible incidence used in the pinned
generalized Hall graph.  A lower-perfect matching (M) contains exactly one
edge incident with each lower target and at most one edge incident with each
physical cell.  Its maximal common cap is

\[
 A_p(M)=E_p\cap\bigcap_{(S,C)\in M:\ p\in C}S.                     \tag{1.3}
\]

The empty second intersection in (1.3) is the full coordinate set.  No
endpoint, cyclic, PBBS, or Pascal hypothesis enters Sections 2--7: only the
labelled physical intervals and their envelopes enter.

For the frozen K16 instance, the target order is

```text
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
SHA-256 c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906
```

and the schedule is

\[
X=\{12870,12871,12872\},\qquad Y=\{0,1,6388\}.
\]

The envelope in the residual graph is already capped at position 6389 to
`0x8000`, and the singleton cell is reserved.  Thus the theorems below apply
to the pinned residual graph, not to an uncapped optimistic graph.

## 2. Exact conflict clutter

Only sets of candidate edges having distinct target endpoints and distinct
cell endpoints are relevant; call such a set matching-compatible.

For a middle bit define

\[
 H_{i,b}=\{p\in I_i:b\in E_p\},\qquad b\in T_i,                    \tag{2.1}
\]

and for a candidate edge (e_0=(S_0,C_0)) define

\[
 H_{e_0,b}=\{p\in C_0:b\in E_p\},\qquad b\in S_0.                 \tag{2.2}
\]

Individual feasibility makes all sets in (2.1)--(2.2) nonempty.

Define three families of matching-compatible forbidden sets.

* A **position conflict** at (p) is an inclusion-minimal family (F) of
  edges whose cells contain (p) and for which

  \[
  E_p\cap\bigcap_{(S,C)\in F}S=\varnothing.                       \tag{2.3}
  \]

* A **middle-bit conflict** for ((i,b)) is an inclusion-minimal family
  (F) of edges with (b\notin S) such that

  \[
  H_{i,b}\subseteq\bigcup_{(S,C)\in F}C.                          \tag{2.4}
  \]

* An **assigned-lower-bit conflict** consists of an anchor
  (e_0=(S_0,C_0)), a bit (b\in S_0), and an inclusion-minimal blocker
  family (F), all jointly matching-compatible, such that every edge of
  (F) has (b\notin S) and

  \[
  H_{e_0,b}\subseteq\bigcup_{(S,C)\in F}C.                        \tag{2.5}
  \]

  The forbidden set is \(\{e_0\}\cup F\).

Let \({\mathfrak F}\) be the clutter of all three types.

### Theorem 2.1 (exact conflict-clutter characterization)

A lower-perfect matching (M) has a simultaneous common cap if and only if
it contains no member of \({\mathfrak F}\).  In that case the maximal word
(A(M)) in (1.3) is a realizing word.

#### Proof

If (M) contains a position conflict, (1.3) is empty at its defining
position.  If it contains a middle-bit conflict, every position at which
the named middle bit is available is capped by a selected target omitting
that bit, so the middle row loses it.  If it contains an assigned-lower-bit
conflict, the anchor cell loses the named bit.  Thus all three types are
genuine obstructions.

Conversely, suppose (A(M)) is not a simultaneous realization.  If some
letter is empty, the selected edges covering that position contain an
inclusion-minimal subfamily satisfying (2.3).  Otherwise every letter is
nonempty.  Because (A_p(M)\subseteq E_p), a middle row cannot gain an
extra bit; if it is inexact, choose a missing bit (b).  The selected edges
whose targets omit (b) cover (H_{i,b}), and an inclusion-minimal cover
is (2.4).  Finally, on the cell of a selected anchor (e_0=(S_0,C_0)),
the word is pointwise contained in (S_0), so that cell also cannot gain an
extra bit.  If it is inexact, a missing bit gives (2.5).  These exhaust all
failures.  The maximal-cap theorem then gives the final assertion. \(\square\)

## 3. Exact rank and geometric span bounds

### Theorem 3.1 (general depth-\(d\) local bounds)

When middle rows have length at most \(D\) and distinct physical lower cells
have length at most \(d\), the forbidden sets in Theorem 2.1 have the
following bounds.

| conflict | maximum number of selected edges | maximum physical span of all cells |
|---|---:|---:|
| position | \(\min\{|E_p|,d(d+1)/2\}\) | \(2d-1\) positions |
| middle bit | \(D\) | \(D+2d-2\) positions |
| assigned lower bit | \(d+1\), including the anchor | \(3d-2\) positions |

#### Proof

There are at most

\[
1+2+\cdots+d=\frac{d(d+1)}2                                    \tag{3.1}
\]

distinct intervals of lengths at most \(d\) containing a fixed
position.  In a minimal family satisfying (2.3), for each edge (e) choose
a coordinate (b_e) which survives after deleting (e) but not before.
For (e\ne f), one has (b_e\in S_f) and (b_f\notin S_f), so the
(b_e)'s are distinct.  This also bounds the family by (|E_p|).  Every
length-at-most-\(d\) interval containing \(p\) lies inside
\([p-d+1,p+d-1]\), proving the span \(2d-1\) bound.

In an inclusion-minimal cover of a finite point set, every covering member
has a private point.  Hence the blocker family in (2.4) has size at most
\(|H_{i,b}|\le |I_i|\le D\).  Every length-at-most-\(d\) cell meeting a
middle interval lies inside its \((d-1)\)-position enlargement on both
sides, of size at most \(D+2d-2\).

The same private-point argument bounds the blocker family in (2.5) by
\(|H_{e_0,b}|\le |C_0|\le d\).  Adding the anchor gives \(d+1\).  All
blockers meet \(C_0\), so their union with the anchor lies in the
\((d-1)\)-position enlargement of \(C_0\), of size at most \(3d-2\).
\(\square\)

For the compiler relation \(D=d+1\), every exact no-good has rank at most

\[
R_d=\max\left\{\frac{d(d+1)}2,d+1\right\}                         \tag{3.2}
\]

(with the first term further capped by \(|E_p|\) for position conflicts)
and span at most \(3d-1\).  At \(d=3,D=4\), the position bound six sharpens
the generic coordinate bound eight, and every no-good has rank at most six
and span at most eight.  The last-row rank includes the anchor.

The first independently replayed failure of the deterministic c7be perfect
matching is exactly a rank-two middle-bit conflict: target `0xc000` on
`[1,2)` and target `0x826a` on `[2,4)` are each legal alone, but together
cover all three hosts `[1,2,3]` of bit `0x0100` in middle row 1.  Notice that
the two cells are disjoint.  Therefore an overlap-only conflict model is
already false on the frozen instance.

## 4. Exact integer program and complete bounded-rank CEGAR

Use one variable (x_e) for each candidate incidence.  The following
integer system is exact:

\[
\begin{aligned}
 \sum_{e\ni S}x_e&=1 &&(S\text{ a lower target}),\\
 \sum_{e\ni C}x_e&\le1 &&(C\text{ a physical cell}),\\
 \sum_{e\in F}x_e&\le |F|-1 &&(F\in{\mathfrak F}),\\
 x_e&\in\{0,1\}.                                                    \tag{4.1}
\end{aligned}
\]

### Corollary 4.1

Integral solutions of (4.1) are in bijection with simultaneous common-cap
matchings.  Moreover, integral separation needs only local no-goods with the
rank and span bounds of Theorem 3.1; for c7be these are six and eight.

#### Proof

The first two lines say exactly that the selected edges form a lower-perfect
matching.  The third line says exactly that the matching avoids the clutter
in Theorem 2.1.  For a proposed integral matching, compute (1.3).  An empty
position supplies a minimal (2.3) set; a missing middle bit supplies a
minimal interval cover (2.4); a missing assigned-lower bit supplies (2.5).
Deleting redundant members produces the displayed rank bounds. \(\square\)

If a pin edge is fixed, set its variable to one and contract it from every
conflict set.  A two-edge conflict containing the pin becomes a unary edge
deletion.  The frozen c7be marginal graph has already installed and reserved
the `0x8000` pin before its perfect matching is computed.

## 5. Exact guard/trace lift: all high-arity conflicts become binary

For a fixed matching (M), a **trace decoration** consists of:

1. a bit \(a_p\in E_p\) for every physical position (p);
2. a position \(h_{i,b}\in H_{i,b}\) for every middle requirement
   (b\in T_i); and
3. a position \(h_{e,b}\in H_{e,b}\) for every selected edge
   (e=(S,C)\) and every (b\in S).

A decoration is compatible with (M) if, whenever a selected edge
(f=(R,D)) contains a chosen trace position (p\in D), its target (R)
contains the bit attached to that trace.  This condition is pairwise between
one chosen trace token ((p,b)) and one selected matching edge.

### Theorem 5.1 (binary trace-lift equivalence)

A lower-perfect matching has a simultaneous common cap if and only if it has
a compatible trace decoration.

#### Proof

For a compatible decoration, every (a_p) survives all selected caps, so
every (A_p(M)) is nonempty.  The trace (h_{i,b}) makes (b) survive in
middle row (i), and (h_{e,b}) makes (b) survive in the selected lower
cell of (e).  Hence all three conditions of the maximal-cap theorem hold.

Conversely, given a realizing maximal cap (A(M)), choose
(a_p\in A_p(M)).  For every required middle or lower bit, choose a position
where that bit occurs in (A(M)).  A bit in (A_p(M)) belongs to every
selected target whose cell contains (p), so all chosen traces are
compatible. \(\square\)

Thus higher conflicts are not intrinsically necessary: they can be lifted
to binary trace-versus-edge exclusions.  The price is a coupled choice among
at most \(|E_p|\) position-bit guards, at most \(D\) middle trace positions,
and at most \(d\) lower trace positions.  For c7be these bounds are eight,
four, and three.  This does **not** turn the problem into ordinary matching,
because the trace choices and the matching remain coupled.

## 6. Cartesian Hall: the strongest Hall-only sufficient certificate

For an edge subgraph (H) of the candidate graph define

\[
 K_p(H)=E_p\cap\bigcap_{(S,C)\in H:\ p\in C}S.                    \tag{6.1}
\]

Call (H) **Cartesian** if

\[
\begin{aligned}
K_p(H)&\ne\varnothing &&(p\in P),\\
\bigcup_{p\in I_i}K_p(H)&=T_i &&(i\text{ a middle row}),\\
\bigcup_{p\in C}K_p(H)&=S &&((S,C)\in H).                         \tag{6.2}
\end{aligned}
\]

### Theorem 6.1 (Cartesian-Hall factorization)

There is a simultaneous common-Q compiler if and only if there is a
Cartesian edge subgraph (H) containing a lower-perfect matching.  When
such an (H) is given, ordinary Hall in (H) plus the word (K(H)) is a
complete constructive certificate.

#### Proof

If (H) is Cartesian, (6.2) says that the one physical word (K(H))
realizes every candidate edge in (H) simultaneously and preserves every
middle row.  Choose any lower-perfect matching in (H).

Conversely, if (M) is a simultaneous matching, take (H=M).  Then
(K(H)=A(M)), and the maximal-cap theorem gives (6.2). \(\square\)

As an equivalence, this strong Cartesian formulation permits the tautological
choice (H=M).  It becomes a useful positive route only when (H) is
constructed independently of the final matching.  Also note that a strong
Cartesian (H) cannot put two distinct target labels on one physical cell;
once every target is incident, cell injectivity is automatic and Hall adds no
further global obstruction.  The weaker Cartesian-*guarded* formulation in
`MATH_THEOREM_R_MAXIMAL_COMMON_CAP_INTERVAL_CEGAR_AND_CARTESIAN_HALL_20260731.md`
is the useful Hall factorization: its guards are checked only against
co-selectable edges, and then any perfect matching in the pruned graph works.

At the time of the original audit, the missing statement was:

> **c7be Cartesian-Hall gate.**  Construct a Cartesian subgraph of the
> pinned 26,331-target incidence graph which still has a 26,331-matching.

The full marginal graph has a perfect matching, but the deterministic
matching's rank-two conflict proves it is not safe to infer Cartesianity from
interval geometry alone.  The subsequent exact common-cap model does exhibit
a different compatible matching for c7be; see the updated boundary in
Section 8.

### Theorem 6.2 (endpoint-independent literal compiler theorem)

Assume, for arbitrary \(k,d,D\), all of the following.

1. The middle intervals and envelopes satisfy (1.1)--(1.2), with every
   forced pin already included in the envelopes and candidate graph.
2. Every required lower target is a left vertex of the candidate graph.
3. There is a Cartesian subgraph \(H\) with a lower-perfect matching.
4. For every required upper target \(U\), there is a consecutive block \(J\)
   of middle rows such that

   \[
   \bigcup_{i\in J}I_i\text{ is one physical interval},\qquad
   \bigcup_{i\in J}T_i=U.                                         \tag{6.3}
   \]

Then \(K(H)\), together with any lower-perfect matching in \(H\), is one
literal nonzero word realizing every prescribed lower, middle, and upper
target.

#### Proof

Theorem 6.1 gives every lower and middle target.  For an upper block \(J\),
put \(W=\bigcup_{i\in J}I_i\).  Since \(W\) is a physical interval and every
one of its positions belongs to at least one row in \(J\),

\[
\bigcup_{p\in W}K_p(H)
=\bigcup_{i\in J}\bigcup_{p\in I_i}K_p(H)
=\bigcup_{i\in J}T_i=U.                                           \tag{6.4}
\]

Thus the same literal word realizes the upper target as a contiguous OR.
All letters are nonempty by Cartesianity. \(\square\)

Theorem 6.2 is the reusable all-\(k\) implication.  Carrier chronology and
Pascal/PBBS machinery are needed only to supply hypothesis 4 and a candidate
Cartesian-Hall subgraph; they are not used in the common-cap proof.

## 7. Laminarity, uncrossing, stable matching, and TU do not close the gate

Here is a smallest abstract obstruction within the stated width bounds.
Use coordinates \(a,b,c\), positions \(0,1,2,3\), one middle row
\([0,3]\) labelled \(\{a,b,c\}\), and hence
\(E_p=\{a,b,c\}\) throughout.
Use the nested cells

\[
C_a=[1,1]\subset C_b=[0,1]\subset C_c=[0,2]                     \tag{7.1}
\]

for the singleton lower targets \(\{a\},\{b\},\{c\}\), respectively.
Each candidate is individually feasible: position 3, which is outside every
cell in (7.1), preserves the complete middle row.  The three edges form a
perfect marginal matching.  But any two of them make the common position 1
empty.  Thus even a laminar cell family and a perfect matching need not
admit a common cap.  There is no crossing pair to uncross, and even a unique
or preference-selected marginal matching can fail.

The natural conflict LP is also not integral.  Add three disjoint private
positions \(4,5,6\), and add singleton rows on those positions with labels
\(\{a\},\{b\},\{c\}\), respectively, so that their envelopes are the
named singletons.  Use the corresponding fallback singleton cells
\(D_a,D_b,D_c\).  Give each singleton target its
risky edge in (7.1) and its private fallback edge.  Write (x_a,x_b,x_c)
for the risky choices and (y_a,y_b,y_c) for the fallbacks.  The point

\[
x_a=x_b=x_c=y_a=y_b=y_c=\tfrac12                                \tag{7.2}
\]

satisfies the target equations and all three exact pair-conflict cuts

\[
x_a+x_b\le1,\qquad x_b+x_c\le1,\qquad x_c+x_a\le1.             \tag{7.3}
\]

It is a fractional vertex: the three target equations and the three tight
rows (7.3) determine it uniquely.  The \(3\times3\) conflict submatrix has
determinant two.  The entire cell family remains laminar (nested or
disjoint).  Consequently:

* physical interval incidence does not make (4.1) totally unimodular;
* laminar-cell uncrossing does not remove the obstruction; and
* stable-marriage selection has no applicable automaticity, since there are
  no preferences encoding the collective cap constraints.

As a purely sufficient LP criterion, if the full augmented matrix in (4.1)
is proved totally unimodular (for example by an actual consecutive-ones
ordering of that **augmented** matrix), its relaxation is exact.  The
interval order of the cells alone proves no such ordering, and (7.1)--(7.3)
shows that no theorem of this form can hold for the abstract class.

## 8. Precise c7be boundary

For the authenticated c7be order and pinned schedule, the following are
proved:

1. exact middle ownership and all upper shadows;
2. a literal reserved `0x8000` singleton cap;
3. 26,331 residual targets, 32,229 available cells, and a residual perfect
   marginal matching;
4. exact common-cap feasibility is the rank-at-most-six, span-at-most-eight
   conflict-avoiding matching problem (4.1);
5. equivalently, it is the binary trace-lift problem of Theorem 5.1 or the
   Cartesian-Hall problem of Theorem 6.1; and
6. the subsequent direct model has an integral solution and decodes to
   `answers/k16.word`, length `12873`, SHA-256
   `890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe`.

The exact positive certificate and four independent literal replays are in
`MATH_CERTIFICATE_K16_OPTIMAL_12873_TRUEFF_COMMONCAP_20260731.md`.  Interval
and laminar geometry alone still cannot supply the implication in general.
For a Hall-only all-dimensional finish one needs the Cartesian-guarded
condition of the companion note (or another quantitative sufficient
criterion), not marginal Hall, pairwise cell overlap, stable matching, or an
unproved TU assertion.

## 9. Source audit and corrections to the earlier common-cap note

The finite constants and the displayed rank-two conflict were checked
against:

```text
scratch/r_k16_true_fourfilter_reroot_pin8000_hall_20260731.audit.json
SHA-256 7dc309006db70c84be5e2065f38045863cefe54270d26c300ad03fa05f79dc15

scratch/audit_k16_genuine_fourfilter_endpoint12825_commoncap_independent_20260731.py
SHA-256 f301f2131b04a89311a38fd55baeef231d7f7975d764034f5d3bd85f36ddc593

scratch/k16_genuine_fourfilter_endpoint12825_commoncap_independent_20260731.audit.json
SHA-256 df7718a737414ad8ead8f451b92384cec68663d67b7a35eb21f7b7db7d15b702
payload ead4d63267318347768596942464882c876ce5efb27d185eb35a1d0d4327ab6a
```

Relative to the earlier common-cap CEGAR theorem, the corrections and
strengthenings are:

1. a position no-good has rank at most six in COMP3, not merely the generic
   coordinate bound eight, because there are only six distinct length-at-
   most-three physical cells through one position;
2. every no-good has physical span at most eight;
3. the three cut families form an exact conflict clutter, yielding (4.1);
4. higher conflicts have the exact binary trace lift of Theorem 5.1; and
5. the endpoint-independent all-\(k\) sufficient hypothesis is precisely a
   Cartesian-Hall subgraph plus the upper block condition (6.3).

The c7be fibre is now known feasible by the exact certificate cited in
Section 8.  These corrections still make no uniform PBBS/Pascal or all-(k)
existence assertion.
