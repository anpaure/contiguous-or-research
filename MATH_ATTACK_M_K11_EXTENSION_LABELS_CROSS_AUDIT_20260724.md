# Cross-audit of the \(K_{11}\) extension-label and rank-seven reduction

Date: 2026-07-24

## 1. Verdict

**PASS on every requested claim.**

I independently audited
MATH_ATTACK_M_K11_EXTENSION_LABELS_20260724.md against the following frozen
mathematical sources:

* K11_ZERO_MARGIN_WINDOW_ATTACK_20260724.md and its independent audit;
* K11_THREE_LAYER_WIDTH_ALIGNMENT.md and its audit;
* K11_FOREST_ADJACENT_SHADOW_REDUCTION.md and both mathematical audits.

The following statements are correct.

1. For every coordinate \(x\),
   \[
   e_x^{\rm ext}=43-R_x^{(3)}-\mathbf1_{\{x\in H\}}.
   \]
2. The inclusion-exclusion hierarchy for every
   \(X\subseteq[11]\), \(1\le |X|\le5\), has the signs and endpoint/seam
   correction stated in the report. Its exact external complement is
   displayed in Section 3 below.
3. The alternating cover projects to a spanning directed linear forest in
   the stated five-in-neighbor digraph \(D_M\), and the converse lift is
   exact.
4. At least \(319\) of the \(330\) rank-seven colors occur in the particular
   projected six-set forest, not merely in a separate endpoint-shadow
   family.
5. The rank-seven duplicate excess satisfies
   \[
   126\le\Delta_7\le137.
   \]
6. Every coordinate has positive repeated-color incidence at least \(72\)
   and lies in at least \(15\) distinct repeated rank-seven colors.

No endpoint, singleton, direction, seam, or off-by-one correction is needed.

One terminology convention should remain explicit: “width at most four”
means endpoint span \(r-\ell\le4\), the frozen convention
\(\text{width}=\text{length}-1\). Such an interval may contain five array
entries. Read this way, the literal-hull statement is correct.

No computation, finite enumeration, or web source was used in this audit.

## 2. Frozen premises actually needed

The proof uses only the following frozen facts.

### F1. Ordered perfect middle-level matching

There are ordered selected witnesses
\[
I_0,\ldots,I_{461},\qquad J_0,\ldots,J_{461}
\]
whose colors \(S_j,U_j\) enumerate all five-sets and all six-sets and obey
\[
S_j\subset U_j.
\]
Thus
\[
M(S_j)=U_j
\]
is a perfect inclusion matching. If
\[
P(U)=M^{-1}(U),\qquad a(U)=U\setminus P(U),
\]
then every coordinate is the label \(a(U)\) exactly
\[
\binom{10}{5}-\binom{10}{4}=42
\tag{2.1}
\]
times.

### F2. The six-block forest

The nonempty rank-five offset blocks number \(c\), with
\[
1\le c\le6.
\]
Deleting the \(c-1\) transitions between them leaves \(c\) alternating
paths. The projected five-set forest has \(462-c\) edges with distinct
six-set union colors.

Appending the unused matching color at each root makes each alternating
component contain the same number of five-sets and six-sets. Consequently
the six-set projection spans all \(462\) six-sets and also has
\[
462-c
\tag{2.2}
\]
edges.

### F3. Rank-seven endpoint losses

Select one witness for every rank-seven target. For either endpoint color,
the rank-six endpoint set occupies \(462\) of the \(465\) positions.
Rank-seven selected endpoints are distinct. Therefore at most three
rank-seven targets fail to share that endpoint with the rank-six row:
\[
0\le e_L,e_R\le3.
\tag{2.3}
\]

At a shared endpoint, the selected rank-six interval is a proper facet
interval of the rank-seven witness. This is forced by interval containment
and the unequal ranks.

### F4. Central seam matching

For the central word \(A_0,\ldots,A_{m-1}\), let
\[
C_i=A_i\cup A_{i+1}\cup A_{i+2},\qquad
T_i=A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3}.
\]
There is one exceptional triple \(H=C_s\). The ordinary triples and all
four-windows have equal cardinality \(m-3\), and the matching is
\[
C_i\mapsto T_i\quad(i<s),\qquad
C_i\mapsto T_{i-1}\quad(i>s).
\tag{2.4}
\]

These four inputs suffice for every requested conclusion.

## 3. Long-run external degrees and their joint subset form

### Theorem 3.1 (one-coordinate formula)

Let \(R_x^{(3)}\) be the number of maximal \(x\)-zero-runs in the central
\(A\)-word having length at least three, and put
\[
h_x=\mathbf1_{\{x\in H\}}.
\]
If \(t_x\) is the number of central matching edges labelled \(x\), then
\[
\boxed{t_x=R_x^{(3)}-1+h_x.}
\tag{3.1}
\]
Hence
\[
\boxed{
e_x^{\rm ext}
=42-t_x
=43-R_x^{(3)}-h_x.
}
\tag{3.2}
\]

#### Proof

Let \(N_{\ell,x}\) count length-\(\ell\) windows whose OR contains \(x\).
In a maximal zero-run of length \(r\), the numbers of all-zero length-three
and length-four windows are
\[
\max(r-2,0),\qquad\max(r-3,0).
\]
The second is one smaller exactly when \(r\ge3\). There is also one fewer
length-four window globally. Therefore
\[
N_{4,x}-N_{3,x}=R_x^{(3)}-1.
\tag{3.3}
\]

The central source family contains all length-three colors except \(H\);
the target family contains all length-four colors. Thus its target-minus-
source point incidence is
\[
N_{4,x}-\bigl(N_{3,x}-h_x\bigr)
=R_x^{(3)}-1+h_x.
\]
Along an inclusion matching, this incidence difference counts precisely
the edges that add \(x\), proving (3.1). Equation (2.1) then gives (3.2).
\(\square\)

This proof is valid for internal and boundary seams. Bijectively, if
\(x\notin H\), the unique long zero-run containing all three seam positions
is the sole long run that supplies no central label. If \(x\in H\), no such
run exists and every long run supplies one label.

The sums also check:
\[
\sum_xt_x=m-3,\qquad
\sum_xe_x^{\rm ext}=465-m.
\tag{3.4}
\]

### Theorem 3.2 (joint subset formula)

For nonempty \(X\subseteq[11]\), \(|X|=r\le5\), define
\[
\Delta_X
=\#\{T:X\subseteq T\}
-\#\{C:X\subseteq C\}
\]
on the central target and source families. For nonempty \(Y\subseteq X\),
let \(R_Y^{(3)}\) count maximal runs of at least three consecutive entries
all disjoint from \(Y\). Then
\[
\boxed{
\Delta_X
=-1+\mathbf1_{\{X\subseteq H\}}
+\sum_{\varnothing\ne Y\subseteq X}
(-1)^{|Y|+1}R_Y^{(3)}.
}
\tag{3.5}
\]
Moreover,
\[
\boxed{0\le\Delta_X\le D_r,}
\qquad
D_r:=
\binom{11-r}{6-r}-\binom{11-r}{5-r},
\tag{3.6}
\]
where
\[
\boxed{(D_1,D_2,D_3,D_4,D_5)=(42,42,28,14,5).}
\tag{3.7}
\]

The exact joint external degree, implicit in the audited report, is
\[
\boxed{
e_X^{\rm ext}
=D_r-\Delta_X
=D_r+1-\mathbf1_{\{X\subseteq H\}}
-\sum_{\varnothing\ne Y\subseteq X}
(-1)^{|Y|+1}R_Y^{(3)}.
}
\tag{3.8}
\]

#### Proof

For a window \(W\), inclusion-exclusion gives
\[
\mathbf1_{\{X\subseteq\operatorname{OR}(W)\}}
=\sum_{Y\subseteq X}(-1)^{|Y|}
\mathbf1_{\{\operatorname{OR}(W)\cap Y=\varnothing\}}.
\tag{3.9}
\]
Subtract the length-three sum from the length-four sum. The empty term
contributes \(-1\). For nonempty \(Y\), each \(Y\)-zero-run of length at
least three decreases the all-\(Y\)-zero window count by one; after
multiplication by \((-1)^{|Y|}\), its contribution is
\((-1)^{|Y|+1}R_Y^{(3)}\). Omitting \(H\) from the source family adds the
indicator in (3.5).

Because each central source is included in its matched target,
\(\Delta_X\) counts central matching edges that newly complete containment
of \(X\), so it is nonnegative. Over the full matching, the corresponding
count is exactly \(D_r\). The central matching edges are a subset, giving
(3.6). The remaining full-matching edges are external, proving (3.8).
\(\square\)

For \(r=1\), equation (3.8) is exactly (3.2). Thus the joint formula is a
genuine extension-degree theorem, not merely an alternating-sum identity.

## 4. The directed six-set forest

### Theorem 4.1 (six-set projection)

Orient one alternating component as
\[
P_0,U_0,P_1,U_1,\ldots,P_r,U_r,
\qquad M(P_i)=U_i.
\tag{4.1}
\]
Then
\[
U_{i-1}\cap U_i=P_i\quad(1\le i\le r).
\tag{4.2}
\]
Consequently the \(U\)-vertices form a path in \(J(11,6)\). Over all
components they form a spanning linear forest \(G_6\) with \(c\) components
and \(462-c\) edges.

#### Proof

Both \(U_{i-1}\) and \(U_i\) contain \(P_i\). They are distinct because the
matching is bijective, so two six-sets containing the same five-set have
intersection exactly that five-set. Every six-set occurs once as some
\(M(P)\), including the final unused root color of each component. Hence
the projection spans all six-sets. \(\square\)

The last sentence is essential: omitting the root colors would give the
wrong vertex, edge, and point counts. A singleton component becomes the
two-vertex alternating path \(P_0,U_0\) and one isolated vertex of \(G_6\);
all formulas remain valid.

### Theorem 4.2 (matching-digraph equivalence)

For \(U\in\binom{[11]}6\), put
\[
P(U)=M^{-1}(U)=U\setminus\{a(U)\}.
\]
Define \(D_M\) on the six-sets by the five incoming arcs
\[
\boxed{
U-\{a(U)\}+\{z\}\longrightarrow U
\qquad(z\notin U).
}
\tag{4.3}
\]
The six-set projection of every alternating cover is a spanning directed
linear forest in \(D_M\). Conversely, every spanning directed linear forest
in \(D_M\) lifts, with the fixed \(M\), to an alternating cover of all
\(462+462\) middle-level vertices.

#### Proof

In (4.1), the predecessor \(U_{i-1}\) and destination \(U_i\) share
\(P(U_i)\). Therefore
\[
U_{i-1}
=P(U_i)\cup\{z\}
=U_i-\{a(U_i)\}+\{z\}
\]
for the unique \(z\in U_{i-1}\setminus U_i\), and \(z\notin U_i\). This is
an arc of \(D_M\).

Conversely, on an arc \(U'\to U\), equation (4.3) gives
\[
P(U)\subset U'\cap U.
\]
Insert \(P(U)\) between \(U'\) and \(U\), and insert \(P(U)\) before every
directed start \(U\). Each six-set is used once because the directed forest
spans; each five-set is used once because \(M\) is bijective. Degree at most
one and acyclicity give alternating paths, with an isolated directed
six-vertex lifting to the one-matching-edge path \(P(U),U\). \(\square\)

There are \(5\cdot462=2310\) candidate arcs. For each coordinate, the
candidate gain and loss margins are both \(210\):
\[
42\cdot5=210,\qquad \binom{10}{6}=210.
\]
This balance is exact but supplies no contradiction.

## 5. Alignment of crossed rank-seven spans with \(G_6\)

This is the delicate step behind \(319\).

### Lemma 5.1 (crossed spans)

At least
\[
p\ge330-e_L-e_R\ge324
\tag{5.1}
\]
rank-seven selected witnesses share both a left endpoint and a right
endpoint with selected rank-six witnesses.

For such a target \(Q\), let its witness be \(K_Q\), and let
\(J_{a_Q}\), \(J_{b_Q}\) be the common-left and common-right rank-six
witnesses. Then
\[
a_Q<b_Q,\qquad
1\le b_Q-a_Q\le6.
\tag{5.2}
\]
Every selected \(J_j\), \(a_Q\le j\le b_Q\), lies inside \(K_Q\), so every
\(U_j\) is a distinct six-facet of \(Q\). Therefore every gap
\[
j\in\{a_Q,\ldots,b_Q-1\}
\tag{5.3}
\]
has set-union color \(Q\).

The gap sets (5.3) of distinct crossed targets are disjoint.

#### Proof

There are \(330-e_L\) left-good and \(330-e_R\) right-good targets inside a
330-target family, proving (5.1).

At a common left endpoint, the six-witness is a proper prefix of \(K_Q\);
at a common right endpoint, it is a proper suffix. Strict common endpoint
order gives \(a_Q<b_Q\). Every intermediate selected six-witness has left
endpoint no earlier than \(K_Q\)'s left endpoint and right endpoint no later
than its right endpoint, so it is physically contained in \(K_Q\). Its
color is a six-subset of \(Q\). There are only seven such facets, proving
the upper bound in (5.2).

If a gap \(j\) belonged to crossed targets \(Q,Q'\), then both
\(U_j,U_{j+1}\) would be distinct facets of both targets. Their union is a
seven-set, so
\[
Q=U_j\cup U_{j+1}=Q'.
\]
\(\square\)

### Lemma 5.2 (literal hull at a noncut gap)

If \(j\) is not a rank-five state cut, then \(J_j,J_{j+1}\) share the
intervening selected five-witness physically. Their union is one literal
interval, and
\[
\operatorname{OR}(J_j\cup J_{j+1})=U_j\cup U_{j+1}.
\tag{5.4}
\]
Its endpoint width is at most four.

#### Proof

In a left-oriented rank-five block, \(I_{j+1}\) lies in both \(J_j\) and
\(J_{j+1}\). In a right-oriented block, \(I_j\) lies in both. Hence the two
six-witness intervals overlap and their union is a contiguous interval.

The ordered endpoint slack places each endpoint of \(J_j\) within offsets
\(\{0,1,2,3\}\) of \(j\), and likewise for \(J_{j+1}\). The outer hull
therefore has offset state among
\[
02,\ 03,\ 04,\ 14,\ 24,
\]
all of endpoint width at most four. \(\square\)

### Theorem 5.3 (the \(319/330\) support bound)

Let
\[
t_Q=\#\{E\in E(G_6):\text{the endpoint union of }E\text{ is }Q\},
\qquad
z=\#\{Q:t_Q>0\}.
\]
Then
\[
\boxed{
z\ge331-c-e_L-e_R\ge319.
}
\tag{5.5}
\]
Equivalently, at most
\[
\boxed{
M_7:=330-z\le c-1+e_L+e_R\le11
}
\tag{5.6}
\]
rank-seven colors are missing.

Every color counted by \(z\) has a literal witness of endpoint width at most
four.

#### Proof

Before the \(c-1\) state cuts, every crossed target has the nonempty,
disjoint gap set from Lemma 5.1. A crossed color can fail to occur in
\(G_6\) only if every gap in its span is a state cut. Since different
crossed colors have disjoint gap sets, assign to each lost crossed color
one of its cuts; this assignment is injective. Thus at most \(c-1\)
crossed colors disappear:
\[
z\ge p-(c-1)\ge331-c-e_L-e_R.
\]
The minimum occurs at \(c=6,e_L=e_R=3\), giving \(319\). Lemma 5.2 supplies
the literal width-four witness for every surviving crossed color.
\(\square\)

The proof loses \(c-1\), not \(c\), because the global order has exactly
\(c-1\) inter-block gaps. This is the main off-by-one audited here.

## 6. Duplicate range

### Lemma 6.1 (fixed-color capacity)

For every seven-set \(Q\),
\[
\boxed{t_Q\le6.}
\tag{6.1}
\]

#### Proof

The endpoints of a \(Q\)-colored \(G_6\)-edge are two of the seven
six-facets of \(Q\). The \(Q\)-colored edges form a subgraph of the linear
forest \(G_6\) on those seven vertices, hence have at most six edges.
\(\square\)

### Theorem 6.2 (exact duplicate ledger)

Define
\[
\Delta_7:=\sum_Q(t_Q-1)_+.
\]
Then
\[
\boxed{
\Delta_7
=(462-c)-z
=132-c+M_7.
}
\tag{6.2}
\]
Consequently,
\[
\boxed{126\le\Delta_7\le137.}
\tag{6.3}
\]
At least \(26\) rank-seven colors repeat.

#### Proof

The forest has \(462-c\) edges. Removing one primary occurrence of each of
its \(z\) colors gives (6.2). Since \(z\le330\),
\[
\Delta_7\ge462-c-330=132-c\ge126.
\]
Using (5.6),
\[
\Delta_7
\le132-c+(c-1+e_L+e_R)
=131+e_L+e_R
\le137.
\]
By Lemma 6.1, one repeated color contributes at most five excess
occurrences, so at least
\[
\left\lceil\frac{126}{5}\right\rceil=26
\]
colors repeat. \(\square\)

## 7. Coordinate repeat lower bounds

Orient the \(c\) six-set paths from their initial to their final vertex. Let

* \(\pi_x\) count paths whose initial matching label is \(x\);
* \(\mu_x\) count final six-sets containing \(x\);
* \(M_x\) count missing rank-seven colors containing \(x\).

Then
\[
0\le\pi_x,\mu_x\le c.
\tag{7.1}
\]

### Theorem 7.1 (exact rank-seven point degree)

If
\[
q_x^{(7)}:=\sum_{Q\ni x}t_Q,
\]
then
\[
\boxed{q_x^{(7)}=294-\pi_x-\mu_x.}
\tag{7.2}
\]
In particular,
\[
\boxed{294-2c\le q_x^{(7)}\le294.}
\tag{7.3}
\]

#### Proof

Every matching label occurs \(42\) times. Along the six-set paths, a label
is a \(0\to1\) gain unless it is the initial matching label. Thus the number
of gains of \(x\) is \(42-\pi_x\).

An \(x\)-zero-run ends before such a gain or at a final six-set omitting
\(x\). Hence the number of zero-runs is
\[
Z_x^{(6)}=(42-\pi_x)+(c-\mu_x)
=42+c-\pi_x-\mu_x.
\tag{7.4}
\]
Exactly \(210\) of the \(462\) six-sets omit \(x\). Each zero-run of \(r\)
vertices contains \(r-1\) edges whose two endpoints omit \(x\). Therefore
\[
\#\{\text{edges whose hull omits }x\}=210-Z_x^{(6)}.
\]
Subtracting from the \(462-c\) edges gives (7.2). \(\square\)

### Theorem 7.2 (positive repeat incidence)

For every coordinate \(x\),
\[
\boxed{
\sum_{Q\ni x}(t_Q-1)_+
=84-\pi_x-\mu_x+M_x.
}
\tag{7.5}
\]
Consequently,
\[
\boxed{
\sum_{Q\ni x}(t_Q-1)_+\ge72,
}
\tag{7.6}
\]
and \(x\) belongs to at least
\[
\boxed{15}
\tag{7.7}
\]
distinct repeated rank-seven colors.

#### Proof

There are \(210\) seven-sets containing \(x\). Thus
\[
\sum_{Q\ni x}(t_Q-1)
=q_x^{(7)}-210
=84-\pi_x-\mu_x.
\]
Each missing color contributes \(-1\) to this signed sum and zero to the
positive sum, proving (7.5). Since \(\pi_x,\mu_x\le c\le6\) and \(M_x\ge0\),
the right side is at least \(84-12=72\).

By Lemma 6.1, a repeated color contributes at most
\[
t_Q-1\le5
\]
to (7.5). Hence at least
\[
\left\lceil\frac{72}{5}\right\rceil=15
\]
distinct repeated colors containing \(x\) are required. \(\square\)

The global point check is
\[
\sum_xq_x^{(7)}
=11\cdot294-\sum_x\pi_x-\sum_x\mu_x
=3234-7c
=7(462-c),
\]
exactly seven incidences per forest edge.

## 8. Adversarial checks

1. **Final root colors.** They are vertices of \(G_6\), although their
   matching edges were unused as five-forest colors. Excluding them would
   invalidate Sections 4 and 7.
2. **Singleton components.** They lift as \(P_0,U_0\) and project to one
   isolated six-set. They contribute to both endpoint ledgers but no hull
   edge; all formulas still hold.
3. **Cuts.** There are \(c-1\) state-cut gaps, not \(c\). Each lost crossed
   color consumes a distinct cut because crossed gap spans are disjoint.
4. **Endpoint exceptions.** The support loss is \(e_L+e_R\), not an
   additional six after already using \(p\ge330-e_L-e_R\).
5. **Literal hulls.** Set union alone is insufficient for a literal
   interval. At noncut gaps the intervening rank-five witness makes
   \(J_j,J_{j+1}\) overlap physically; this is why (5.4) is valid.
6. **Width convention.** State \(04\) has width four and length five.
7. **Multiplicity versus support.** The \(319\) theorem is a support
   statement; the remaining \(462-c-z\) edges are duplicate occurrences.
8. **Positive versus signed repeat sums.** Missing colors contribute
   \(-1\) to the signed sum. The \(+M_x\) in (7.5) is indispensable.
9. **Coordinate endpoint corrections.** The crude lower bound \(72\) uses
   both possible losses \(\pi_x\le c\) and \(\mu_x\le c\); they cannot be
   silently merged.
10. **Abstract converse scope.** A directed forest in \(D_M\) lifts to an
    abstract alternating cover, but need not respect physical endpoint
    order, offset blocks, or the central word. The source report states
    this limitation correctly.

## 9. Final ledger

| Claim audited | Verdict |
|---|---|
| \(e_x^{\rm ext}=43-R_x^{(3)}-\mathbf1_{x\in H}\) | pass |
| Joint subset hierarchy and bounds \(42,42,28,14,5\) | pass |
| Exact external joint degree (3.8) | pass; implicit in source |
| Directed six-set forest and converse lift | pass |
| \(z\ge319\), hence \(M_7\le11\) | pass |
| \(126\le\Delta_7\le137\) | pass |
| At least \(26\) repeated rank-seven colors globally | pass |
| Positive repeated incidence at least \(72\) per coordinate | pass |
| At least \(15\) distinct repeated colors through each coordinate | pass |
| Endpoint, singleton, cut, and parity corrections | pass |

The audited report's requested core is mathematically sound. Its unresolved
step remains exactly as stated there: incompatibility of the directed
forest with the simultaneous physical endpoint, central-run, and literal
interval constraints is not proved.
