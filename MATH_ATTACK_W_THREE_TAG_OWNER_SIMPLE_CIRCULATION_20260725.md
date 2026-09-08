# Minimal owner-simple tag circulations for the truncated rotor

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, computation,
or solver input is used.

## 0. Verdict

Throughout, \(m,H,Q\) are positive integers with \(Q\ge1\).  Put

\[
 n=2Q,\qquad a_0=m-Q,\qquad M=m+H.
\]

The one-update triangle of Sections 2--3 assumes

\[
 m\ge Q+2,\qquad H\ge Q+2.
\]

The full \(M\)-state cyclic continuation assumes the slightly stronger
condition \(m\ge Q+3\).

The owner duplication in the two-route funnel is repaired exactly by three
tags.  No fourth tag is needed.

Under these hypotheses there is a literal three-path circulation with the
following properties.

1. Its two alternatives use the two incidence matchings of a tag triangle,
   \[
   (a\to ab,\ b\to bc,\ c\to ca)
   \quad\hbox{and}\quad
   (b\to ab,\ c\to bc,\ a\to ca).
   \]
2. The two orientations assigned to any one edge reach the same ordered
   quotient state after one rotor update.  All connector trajectories can
   therefore be chosen literally identical and cancel state by state.
3. If the three collar orders have the same first-\(Q\) set, the complete
   middle-owner multiset is identical in the two alternatives.
4. The remaining full hard-flag difference is the source circulation
   \[
   \Delta_h=
   d_{ab}(P_h(z_{ab}))+d_{bc}(P_h(z_{bc}))
             +d_{ca}(P_h(z_{ca})).
   \]
   Taking \(z_{ab}=z_{bc}=z\) and \(z_{ca}=z^*\) reduces this to one
   four-corner trade between \(z\) and \(z^*\).  One adjacent collar swap
   leaves exactly one marked rank rectangle and nothing at any other rank.
5. Each edge state admits a tag-avoiding cyclic continuation.  Choosing
   three positive continuation lengths with sum \(M-3\) gives exactly
   \(M\) designated quotient states in either alternative.  At every
   controlled hard rank all \(M\) flags are distinct.  The exact literal
   length of the three standalone words is
   \[
   \boxed{M+6Q+3.}
   \]

Thus the local connector, integrality, owner-duplication, and
internal-collision gates are all solved simultaneously.  In the calibrated
regime \(Q=o(M)\), the displayed reset toll is also \(o(M)\), so the local
packet has coefficient one.

There is also an exact \(L\)-triangle version for every positive integer
\(L\).  Under

\[
 m\ge Q+3,\qquad
 3L\le H-Q+1,\qquad
 M\ge6L,
\]

it gives \(L\) independently choosable owner-preserving orientations,
still with exactly \(M\) designated states, and exact literal length

\[
 \boxed{M+3L(2Q+1).}
\]

Consequently it is coefficient-one locally whenever

\[
 LQ=o(M).
\]

For a half-reversal collar pair, flipping all \(L\) orientations has exact
total square metric

\[
 2L\left\lfloor\frac{Q^2}{4}\right\rfloor.
\]

This does **not** prove the constant-one theorem.  The construction gives a
complete local positive packet and a literal word collection, but it does
not prove that one such prescribed packet can be installed in every member
of a fixed global exact wreath factor, that packets chosen in different
carriers have globally disjoint hard flags, or that the correlated
half-reversal directions satisfy the required weighted frame/descent
inequality.  Initialization-transient flags are also outside the signed
designated-state ledger.

## 1. Quotient notation and the exact scope of the ledger

Fix a carrier \(U\) of size \(M\).  A radius-\(Q\) quotient state is

\[
 \omega=(A;z_1,\ldots,z_n;B),
\]

where

\[
 |A|=a_0=m-Q,\qquad |B|=H-Q,
\]

and the displayed blocks partition \(U\).  Its hard flag at index \(h\) is

\[
 F_h(\omega)=A\cup P_h(z),
 \qquad
 P_h(z)=\{z_1,\ldots,z_h\},
 \qquad 0\le h\le n.
\tag{1.1}
\]

Thus \(|F_h|=a_0+h\), and \(F_Q\) is the middle owner.

One rotor update chooses \(x\in A\) and \(y\in B\) and sends

\[
 (A;z_1,\ldots,z_n;B)
 \longmapsto
 (A-x+y;\ x,z_1,\ldots,z_{n-1};\ B-y+z_n).
\tag{1.2}
\]

For a multiset \(\mathcal P\) of designated quotient states, write

\[
 I_h(\mathcal P)=\sum_{\omega\in\mathcal P}e_{F_h(\omega)}.
\tag{1.3}
\]

All identities below concern the complete incidences of these designated
states.  Under the already audited quotient-to-literal lift, a quotient
path having \(s\) designated states compiles into a literal word of length

\[
 s+(n+1)=s+2Q+1.
\tag{1.4}
\]

The extra \(n+1\) letters initialize the first quotient window.  Their
incidental OR witnesses are genuine positive witnesses, but they are not
terms of (1.3).  They are counted exactly in every literal-length formula
below.

## 2. The unoriented-edge collapse after one update

Assume throughout this section that

\[
 m\ge Q+2,\qquad H\ge Q+2.
\tag{2.0}
\]

Partition the carrier as

\[
 U=K\mathbin{\dot\cup}Z\mathbin{\dot\cup}R
       \mathbin{\dot\cup}T,
 \qquad T=\{a,b,c\},
\tag{2.1}
\]

where

\[
 |K|=m-Q-1,\qquad |Z|=2Q,\qquad |R|=H-Q-2.
\tag{2.2}
\]

For each edge

\[
 e\in\{ab,bc,ca\},
\]

fix an order

\[
 z_e=(z_{e,1},\ldots,z_{e,n})
\]

of \(Z\).  If \(e=\{v,w\}\), define the source state

\[
 \omega_{v,e}=
 (K+v;\ z_{e,1},\ldots,z_{e,n};\ R+(T-\{v\})).
\tag{2.3}
\]

Choose once and for all \(x\in K\).  From \(\omega_{v,e}\), make one
rotor update with core choice \(x\) and tail choice \(w\).

### Lemma 2.1 (edge collapse)

The resulting state is

\[
 \boxed{
 \eta_e(z_e)=
 \left(
 K-x+e;\
 x,z_{e,1},\ldots,z_{e,n-1};\
 R+(T-e)+z_{e,n}
 \right).}
\tag{2.4}
\]

It depends on the unordered edge \(e\) and its collar order, but not on
which endpoint of \(e\) was the source tag.

#### Proof

The core exchange is

\[
 K+v-x+w=K-x+\{v,w\}=K-x+e.
\]

The old tail is \(R+(T-\{v\})\).  Removing \(w\) and receiving the last
collar label gives

\[
 R+(T-\{v,w\})+z_{e,n}=R+(T-e)+z_{e,n}.
\]

The collar update is exactly the middle block in (2.4).  Every displayed
choice is legal. \(\square\)

An immediate consequence is stronger than equality of projected loads.
For fixed \(e,z_e\), the routes starting from \(v\) and \(w\) can use the
same choices after their first update and hence have literally identical
ordered connector states.

## 3. The exact triangle circulation

Use the two incidence matchings

\[
 \mathcal M_+
 =\{a\to ab,\ b\to bc,\ c\to ca\},
\tag{3.1}
\]

and

\[
 \mathcal M_-
 =\{b\to ab,\ c\to bc,\ a\to ca\}.
\tag{3.2}
\]

For each edge, use the same continuation from \(\eta_e(z_e)\) in the two
systems.  Let \(\mathcal P_+\) and \(\mathcal P_-\) denote the complete
designated-state multisets, including their three sources.

For tags \(u,v\) and a set \(P\subseteq Z\), put

\[
 d_{uv}(P)=e_{K+u+P}-e_{K+v+P}.
\tag{3.3}
\]

### Theorem 3.1 (statewise cancellation and full flag ledger)

For every \(0\le h\le2Q\),

\[
 \boxed{
 \begin{aligned}
 \Delta_h
 &: =I_h(\mathcal P_+)-I_h(\mathcal P_-)\\
 &=d_{ab}(P_h(z_{ab}))
   +d_{bc}(P_h(z_{bc}))
   +d_{ca}(P_h(z_{ca})).
 \end{aligned}}
\tag{3.4}
\]

Every designated connector state cancels edge by edge and state by state.
At every rank, \(\Delta_h\) has total mass zero and singleton margin zero.

#### Proof

For an edge \(e=\{v,w\}\), Lemma 2.1 makes the first positive poststate
and first negative poststate equal to the same ordered state \(\eta_e\).
Their chosen continuations are identical.  Thus every non-source state
cancels literally.

The three positive sources have flags

\[
 K+a+P_h(z_{ab}),\quad
 K+b+P_h(z_{bc}),\quad
 K+c+P_h(z_{ca}),
\]

whereas the negative sources have flags

\[
 K+b+P_h(z_{ab}),\quad
 K+c+P_h(z_{bc}),\quad
 K+a+P_h(z_{ca}).
\]

Subtracting gives (3.4).

Each summand in (3.4) has total mass zero and singleton margin respectively

\[
 e_a-e_b,\qquad e_b-e_c,\qquad e_c-e_a.
\]

Their sum is zero. \(\square\)

### Corollary 3.2 (exact middle-owner criterion)

The two source-owner multisets are equal if and only if

\[
 \boxed{
 P_Q(z_{ab})=P_Q(z_{bc})=P_Q(z_{ca}).}
\tag{3.5}
\]

When (3.5) holds, writing the common set as \(P\), the source owners in
either system are exactly

\[
 K+P+a,\qquad K+P+b,\qquad K+P+c.
\tag{3.6}
\]

The connector-owner multisets are equal without any additional condition,
because they agree edgewise as ordered states.  Consequently the complete
middle-owner multisets of \(\mathcal P_+\) and \(\mathcal P_-\) are equal.

#### Proof

Sufficiency follows from (3.6).  Conversely, intersection with the tag set
\(T\) identifies the unique owner containing singleton tag \(a\), then the
unique owners containing \(b\) and \(c\).  Equality therefore forces

\[
 P_Q(z_{ab})=P_Q(z_{ca}),\quad
 P_Q(z_{bc})=P_Q(z_{ab}),\quad
 P_Q(z_{ca})=P_Q(z_{bc}).
\]

This is (3.5). \(\square\)

The criterion is multiset-level, not merely the vector equation
\(\Delta_Q=0\).

If every route is stopped at its first poststate, either alternative has
six designated states.  Their tag intersections are the three singletons
and the three triangle edges, so all six hard flags are distinct at every
rank.  By (1.4), the exact standalone literal length of this minimal
one-update circulation is

\[
 3(2+2Q+1)=6Q+9.
\tag{3.7}
\]

## 4. Tag-free cyclic continuation and exact owner simplicity

The one-update triangle already cancels its connectors, but coefficient-one
packing also needs to use the remaining state budget without creating an
owner collision.  The following cyclic continuation supplies exactly that.

Delete all three tags from \(\eta_e\).  On

\[
 V=U-T,
 \qquad |V|=M'=M-3,
\]

the remaining quotient state is

\[
 \eta'_e=(L';q_1,\ldots,q_{2Q};R'),
\tag{4.1}
\]

where

\[
 L'=K-x,
 \qquad
 (q_1,\ldots,q_{2Q})
 =(x,z_{e,1},\ldots,z_{e,n-1}),
 \qquad
 R'=R+z_{e,n}.
\tag{4.2}
\]

Put

\[
 m'=m-2,\qquad H'=H-1.
\tag{4.3}
\]

Then

\[
 |L'|=m'-Q,qquad |R'|=H'-Q,qquad M'=m'+H'.
\tag{4.4}
\]

Thus (4.1) is exactly a radius-\(Q\) rotor state on \(V\).

### Lemma 4.1 (every quotient state lies on a phase-simple cyclic rotor)

Assume

\[
 m'-Q\ge1,qquad H'-Q\ge1.
\tag{4.5}
\]

There is a cyclic rotor of period \(M'\) through \(\eta'_e\) such that, at
every hard index \(0\le h\le2Q\), its \(M'\) phase flags are all distinct.

#### Proof

Choose a cyclic departure order

\[
 d_0,d_1,\ldots,d_{M'-1}
\]

as follows:

\[
 \begin{array}{ll}
 d_0,\ldots,d_{Q-1}
   &=q_Q,q_{Q-1},\ldots,q_1,\\[2mm]
 d_Q,\ldots,d_{m'-1}
   &=\text{an arbitrary order of }L',\\[2mm]
 d_{m'},\ldots,d_{M'-Q-1}
   &=\text{an arbitrary order of }R',\\[2mm]
 d_{M'-Q},\ldots,d_{M'-1}
   &=q_{2Q},q_{2Q-1},\ldots,q_{Q+1}.
 \end{array}
\tag{4.6}
\]

All subscripts below are read modulo \(M'\).  At phase \(t\), take the
core, ordered collar, and tail to be

\[
 A'_t=\{d_{t+Q},\ldots,d_{t+m'-1}\},
\tag{4.7}
\]

\[
 (d_{t+Q-1},d_{t+Q-2},\ldots,d_{t-Q}),
\tag{4.8}
\]

and the remaining labels, respectively.  At \(t=0\), (4.6) turns
(4.7)--(4.8) into exactly (4.1).

The update \(t\to t+1\) removes \(d_{t+Q}\) from the core, inserts
\(d_{t+m'}\) from the tail, prepends the removed core label to the collar,
and drops \(d_{t-Q}\) from the collar into the tail.  Hence it is precisely
the legal recurrence (1.2).

At hard index \(h\), the flag is the cyclic interval

\[
 \boxed{
 F'_h(t)=\{d_{t+Q-h},d_{t+Q-h+1},\ldots,d_{t+m'-1}\},}
\tag{4.9}
\]

of length

\[
 k_h=m'-Q+h.
\tag{4.10}
\]

Condition (4.5) gives

\[
 1\le k_h\le M'-1
 \qquad(0\le h\le2Q).
\tag{4.11}
\]

A fixed-length proper cyclic interval in a cycle of distinct labels cannot
equal a nontrivial cyclic translate of itself.  Equivalently, its circular
indicator word consists of one nonempty block of ones and one nonempty
block of zeros and has no nontrivial rotational period.  Thus the \(M'\)
sets in (4.9) are distinct. \(\square\)

Reinsert the fixed edge \(e\) into every core and the third tag \(T-e\)
into every tail.  No tag is ever selected.  This lifts the cyclic rotor to
a continuation from \(\eta_e\), and its full hard flags are

\[
 e\cup F'_h(t).
\tag{4.12}
\]

### Theorem 4.2 (full owner-simple triangle packet)

Assume

\[
 m\ge Q+3,qquad H\ge Q+2.
\tag{4.13}
\]

For each edge \(e\in\{ab,bc,ca\}\), choose a positive integer \(\ell_e\)
of consecutive phases from its lifted cyclic rotor, beginning with
\(\eta_e\), such that

\[
 \ell_{ab}+\ell_{bc}+\ell_{ca}=M-3.
\tag{4.14}
\]

Use the same edge prefix in the positive and negative alternatives.  Then:

1. each alternative has exactly
   \[
   3+\sum_e\ell_e=M
   \tag{4.15}
   \]
   designated quotient states;
2. at every \(0\le h\le2Q\), their \(M\) hard flags are pairwise distinct;
3. if (3.5) holds, the two alternatives have the same squarefree
   middle-owner incidence vector;
4. the complete signed hard-flag ledger remains exactly (3.4);
5. the three standalone literal words have exact total length
   \[
   \boxed{M+3(2Q+1)=M+6Q+3.}
   \tag{4.16}
   \]

#### Proof

Equation (4.15) counts the three source states and the chosen edge phases.

At any fixed hard rank, a source flag meets \(T\) in one of the three
singletons \(a,b,c\).  A connector flag meets \(T\) in one of the three
edge pairs \(ab,bc,ca\).  Hence sources are mutually distinct, no source
equals a connector flag, and connectors on different edge paths are
distinct.  On one edge path, Lemma 4.1 gives distinct flags at distinct
phases.  This proves assertion 2, including the middle rank.

Assertions 3 and 4 follow from Corollary 3.2 and edgewise state
cancellation.  If the edge path has \(1+\ell_e\) designated states when
its source is included, (1.4) gives literal length

\[
 1+\ell_e+2Q+1.
\]

Summing over the three edges and using (4.14) gives (4.16). \(\square\)

In particular, the designated factorial pair-collision count within one
packet is exactly zero at every controlled rank.  This assertion does not
include initialization-transient flags or flags belonging to other
carriers.

## 5. Isolated rectangles and long-block square metric

Take

\[
 z_{ab}=z_{bc}=z,
 \qquad
 z_{ca}=z^*.
\tag{5.1}
\]

Then (3.4) telescopes in the tag coordinate:

\[
 \boxed{
 \Delta_h=d_{ac}(P_h(z))-d_{ac}(P_h(z^*)).}
\tag{5.2}
\]

### Theorem 5.1 (one exact marked rectangle)

Suppose \(z^*\) is obtained from \(z\) by swapping adjacent collar labels
\(u,v\) in positions \(r,r+1\), where

\[
 1\le r\le2Q-1,qquad r\ne Q.
\tag{5.3}
\]

Then (3.5) holds,

\[
 \Delta_h=0\qquad(h\ne r),
\tag{5.4}
\]

and, with \(G=P_{r-1}(z)=P_{r-1}(z^*)\),

\[
 \boxed{
 \Delta_r=
 e_{K+G+a+u}+e_{K+G+c+v}
 -e_{K+G+c+u}-e_{K+G+a+v}.}
\tag{5.5}
\]

Thus all connector traces cancel, the complete middle-owner multiset is
preserved, and exactly one elementary octahedral rectangle survives at the
marked hard rank.

#### Proof

An adjacent swap changes a prefix set only when the prefix cut separates
the two exchanged positions, namely at \(h=r\).  Since \(r\ne Q\), both
labels lie on the same side of the middle cut and the first-\(Q\) set is
unchanged.  Substitution in (5.2) gives (5.4)--(5.5). \(\square\)

For arbitrary orders \(z,z^*\) with the same collar-label set, put

\[
 d_h=|P_h(z)\setminus P_h(z^*)|
     =\frac12|P_h(z)\mathbin\triangle P_h(z^*)|.
\tag{5.6}
\]

Let \(d_\square\) be unit-octahedral distance at the fixed hard rank, and
let \(\Gamma_2\) be the pair-incidence shadow.

### Lemma 5.2 (exact square metric)

For every \(h\),

\[
 \boxed{
 d_\square(\Delta_h)=d_h,
 \qquad
 \|\Gamma_2\Delta_h\|_1=4d_h.}
\tag{5.7}
\]

#### Proof

A Johnson geodesic replacing the \(d_h\) elements of
\(P_h(z)-P_h(z^*)\) one at a time telescopes (5.2) into \(d_h\) elementary
rectangles, giving the upper bound.

All pair coordinates not meeting \(\{a,c\}\) cancel in (5.2).  For each
label in the symmetric difference of the two prefixes, exactly the two
pair coordinates joining it to \(a\) and \(c\) survive, both with absolute
coefficient one.  There are \(2d_h\) such labels, so the norm is \(4d_h\).
One unit octahedron has pair-shadow norm four.  The triangle inequality
therefore gives the matching lower bound. \(\square\)

Now let \(z^*\) reverse positions \(1,\ldots,Q\) internally and reverse
positions \(Q+1,\ldots,2Q\) internally.  Then

\[
 P_Q(z)=P_Q(z^*),
\tag{5.8}
\]

and

\[
 d_h=
 \begin{cases}
 \min(h,Q-h),&0\le h\le Q,\\
 \min(h-Q,2Q-h),&Q\le h\le2Q.
 \end{cases}
\tag{5.9}
\]

Since

\[
 \sum_{h=0}^{Q}\min(h,Q-h)
 =\left\lfloor\frac{Q^2}{4}\right\rfloor,
\tag{5.10}
\]

Lemma 5.2 yields

\[
 \boxed{
 \sum_{h=0}^{2Q}d_\square(\Delta_h)
 =2\left\lfloor\frac{Q^2}{4}\right\rfloor,}
\tag{5.11}
\]

and

\[
 \boxed{
 \sum_{h=0}^{2Q}\|\Gamma_2\Delta_h\|_1
 =8\left\lfloor\frac{Q^2}{4}\right\rfloor.}
\tag{5.12}
\]

This is an exact \(\Theta(Q^2)\) long-block incidence movement carried by
three literal paths with only \(6Q+3\) initialization letters beyond the
\(M\) designated-state budget.

## 6. Why three tags are minimal in the simple post-edge model

The minimality statement needs a precise scope.  It is not an absolute
claim against every conceivable two-tag route carrying additional
persistent non-tag signatures.

Let the left vertices be source tags \(s\in T\), and let the right vertices
be simple post-update tag pairs \(e\in\binom T2\).  A route beginning with
source tag \(s\) and inserting tag \(t\) is the incidence edge

\[
 s\sim\{s,t\}.
\tag{6.1}
\]

In the **simple-post-edge matching model**, an admissible route system is
required to use at most one route at each source-tag vertex and at most one
route at each simple post-edge vertex; equivalently, it is a matching in
this bipartite incidence graph.  The tag intersections then certify owner
simplicity: a source owner has tag intersection \(\{s\}\), and every
tag-avoiding connector owner has tag intersection \(e\).  Owner-simplicity
by itself would not imply the matching condition if different non-tag
signatures were allowed at the same tag vertex.

### Theorem 6.1 (model-relative minimality)

Suppose two nonidentical tag-static route systems

1. are matchings in the simple tag--post-edge incidence graph and are
   owner-simple;
2. cover the same source tag vertices;
3. cover the same simple post-edge vertices; and
4. cancel their connector trajectories statewise at each post-edge vertex.

Then their symmetric difference contains at least a six-cycle.  In
particular, at least three tags and three routes per alternative are needed.
The triangle construction of Section 3 attains equality.

#### Proof

The two systems are matchings with the same covered left and right
vertices.  Their symmetric difference is therefore a disjoint union of
alternating even cycles.

A four-cycle in the incidence graph would require two distinct right
vertices adjacent to the same two left tags \(s,t\).  But the unique simple
two-subset adjacent to both is \(\{s,t\}\).  Hence no four-cycle exists.
The shortest possible alternating cycle has length six, and it is exactly

\[
 a-ab-b-bc-c-ca-a.
\]

Its two alternating matchings are (3.1)--(3.2). \(\square\)

### Proposition 6.2 (the actual two-tag parallel-edge escape collides)

One can formally create a four-cycle with two tags \(a,b\) by treating
the same tag pair equipped with two collar orders \(z,z^*\) as two coloured
right vertices.  Its first post-update middle owner is

\[
 \boxed{
 \operatorname{Own}(\eta_{ab}(z))
 =K+a+b+P_{Q-1}(z),}
\tag{6.2}
\]

independently of the buffer \(x\).

If \(z,z^*\) differ by the static adjacent row swap at positions
\(r,r+1\) with

\[
 r\le Q-2,
\tag{6.3}
\]

then

\[
 P_{Q-1}(z)=P_{Q-1}(z^*).
\tag{6.4}
\]

The two coloured poststates therefore have the same middle owner already
after their first updates.  The parallel-edge four-cycle is not
owner-simple.

#### Proof

At \(\eta_{ab}(z)\), the core is \(K-x+a+b\), while the first \(Q\)
collar labels are \(x\) together with \(P_{Q-1}(z)\).  Their union is
(6.2).  Under (6.3), both swapped positions lie in the first \(Q-1\)
positions, proving (6.4). \(\square\)

The same duplicate conclusion holds whenever the swap does not cross the
\((Q-1)\)-prefix cut.  The exceptional cut \(r=Q-1\), or an extra
persistent separator outside the tag pair, is not ruled out by Proposition
6.2.  Such a separator enlarges the effective right-signature space and is
precisely outside the simple-post-edge minimality theorem.

## 7. Four tags and general even cycles

The triangle is minimal, but a four-cycle gives the best small-cycle
amortization for isolated rectangles.

Let

\[
 T=\{t_0,t_1,\ldots,t_{k-1}\},
 \qquad k=2s\ge4,
\]

and let

\[
 e_i=\{t_i,t_{i+1}\}
\]

with indices modulo \(k\).  Replace (2.2) by

\[
 |K|=m-Q-1,qquad |Z|=2Q,qquad
 |R|=H-Q-k+1.
\tag{7.1}
\]

The forward alternative sends \(t_i\) to edge \(e_i\); the reverse
alternative sends \(t_{i+1}\) to the same edge.  Lemma 2.1 applies
unchanged.  If edge \(e_i\) has collar order \(z_i\), the full source ledger
is

\[
 \boxed{
 \Delta_h=\sum_{i=0}^{k-1}
 \left(
 e_{K+t_i+P_h(z_i)}
 -e_{K+t_{i+1}+P_h(z_i)}
 \right).}
\tag{7.2}
\]

All connector states cancel edgewise.

Assign

\[
 z_i=
 \begin{cases}
 z,&i\text{ even},\\
 z^*,&i\text{ odd}.
 \end{cases}
\tag{7.3}
\]

Using the zero sum of all tag edges at a fixed prefix set, (7.2) becomes

\[
 \boxed{
 \Delta_h=
 \sum_{i\ {\rm even}}
 \left[
 d_{t_i t_{i+1}}(P_h(z))
 -d_{t_i t_{i+1}}(P_h(z^*))
 \right].}
\tag{7.4}
\]

The even tag edges are pairwise disjoint.  Therefore one adjacent collar
swap with (r\ne Q) gives exactly \(s=k/2\) support-disjoint marked
rectangles and preserves the complete middle-owner multiset.  More
generally, the middle multiset is preserved whenever

\[
 P_Q(z)=P_Q(z^*).
\]

A
four-cycle gives two rectangles with four routes per alternative, or two
routes per rectangle.  A half reversal gives exact aggregate square metric

\[
 2s\left\lfloor\frac{Q^2}{4}\right\rfloor
\tag{7.5}
\]

and pair-shadow norm

\[
 8s\left\lfloor\frac{Q^2}{4}\right\rfloor.
\tag{7.6}
\]

There is also a full \(M\)-state version.  After deleting all \(k\) tags
from an edge state, the effective parameters are

\[
 m'=m-2,qquad H'=H-k+2,qquad M'=M-k.
\tag{7.7}
\]

If

\[
 m\ge Q+3,qquad k\le H-Q+1,qquad M\ge2k,
\tag{7.8}
\]

choose positive integer edge-arc lengths summing to \(M-k\).  The \(k\) sources
and these arcs give exactly \(M\) designated states, all hard-rank flags
are distinct, and the exact literal length is

\[
 \boxed{M+k(2Q+1).}
\tag{7.9}
\]

For only the source and one poststate on each route, the corresponding
standalone length is

\[
 k(2Q+3).
\tag{7.10}
\]

The exact length ratio is

\[
 1+\frac{k(2Q+1)}M.
\]

Thus this even-cycle packet has coefficient one exactly when
\(kQ=o(M)\).  In particular, a fixed four-cycle is coefficient-one locally
when \(Q=o(M)\).  Feasibility of the tag blocks alone does not imply a
negligible initialization toll.

## 8. An independent \(L\)-triangle packet cube

The most useful packable form uses disjoint triangles rather than one long
cycle, because their orientations can be chosen independently.

Let

\[
 T=\mathbin{\dot\bigcup}_{g=1}^L
 \{a_g,b_g,c_g\},
 \qquad |T|=3L,
\tag{8.1}
\]

and partition

\[
 U=K\mathbin{\dot\cup}Z\mathbin{\dot\cup}R
       \mathbin{\dot\cup}T
\tag{8.2}
\]

with

\[
 |K|=m-Q-1,qquad |Z|=2Q,qquad
 |R|=H-Q-3L+1.
\tag{8.3}
\]

For each of the \(3L\) triangle edges, perform the first update of Lemma
2.1.  Deleting all tags leaves effective parameters

\[
 \boxed{
 m'=m-2,\qquad H'=H-3L+2,\qquad M'=M-3L.}
\tag{8.4}
\]

Indeed, the tag-free core has size \(m-Q-2=m'-Q\), and the tag-free tail
has size

\[
 H-Q-3L+2=H'-Q.
\tag{8.5}
\]

### Theorem 8.1 (coefficient-one local triangle cube)

Assume

\[
 \boxed{
 m\ge Q+3,qquad
 3L\le H-Q+1,qquad
 M\ge6L.}
\tag{8.6}
\]

For each triangle edge \(e\), choose a positive integer cyclic-arc length
\(\ell_e\) such that

\[
 \sum_e\ell_e=M-3L.
\tag{8.7}
\]

For every bit vector \(\varepsilon\in\{0,1\}^L\), independently choose the
forward or reverse triangle matching in component \(g\), and use the same
edge arcs for every bit vector.  Then:

1. every \(\varepsilon\) gives a positive integral system of exactly \(M\)
   designated quotient states;
2. at every controlled hard rank, these \(M\) flags are pairwise distinct;
3. if the three first-\(Q\) collar sets agree within each triangle, every
   bit vector has exactly the same squarefree middle-owner incidence;
4. all connector states are independent of \(\varepsilon\);
5. the \(L\) route orientations are independently choosable; if every
   component direction is nonzero, disjoint tag triples make the signed
   directions linearly independent; under a nontrivial adjacent-swap
   specialization, their four-corner supports are pairwise disjoint;
6. every bit vector has exact standalone literal length
   \[
   \boxed{M+3L(2Q+1).}
   \tag{8.8}
   \]

#### Proof

The first two inequalities in (8.6) make every cyclic hard interval
nonempty and proper, by (8.4)--(8.5).  The last inequality is exactly

\[
 M-3L\ge3L,
\]

which is necessary and sufficient for the positive composition (8.7).

There are \(3L\) source states and \(M-3L\) edge-arc states.  This proves
the state count.  Source flags have distinct singleton intersections with
\(T\).  Connector paths have distinct edge-pair intersections with \(T\),
and Lemma 4.1 separates phases within one edge path.  Hence all flags are
distinct.

Corollary 3.2 applies independently in each triangle.  Lemma 2.1 makes all
edge arcs bit-independent.  Whenever the component directions are nonzero,
their disjoint tag supports prove linear independence; in the adjacent-swap
case the four-corner supports themselves are disjoint.  Finally, the \(3L\)
paths contribute \(3L(2Q+1)\) initialization letters beyond their total of
\(M\) designated states. \(\square\)

For half-reversal collars in every triangle, support disjointness in the
tag coordinates and Lemma 5.2 give the exact totals

\[
 \boxed{
 \sum_h d_\square(\Delta_h^{\rm all})
 =2L\left\lfloor\frac{Q^2}{4}\right\rfloor,}
\tag{8.9}
\]

and

\[
 \boxed{
 \sum_h\|\Gamma_2\Delta_h^{\rm all}\|_1
 =8L\left\lfloor\frac{Q^2}{4}\right\rfloor.}
\tag{8.10}
\]

Here the totals refer to flipping all \(L\) bits; flipping a subset gives
the corresponding additive sub-total.

## 9. Coefficient-scale packing ledger

The exact local length ratio in Theorem 8.1 is

\[
 \boxed{
 \frac{\operatorname{len}}M
 =1+\frac{3L(2Q+1)}M.}
\tag{9.1}
\]

Therefore

\[
 \operatorname{len}=M+o(M)
 \quad\Longleftrightarrow\quad
 LQ=o(M).
\tag{9.2}
\]

Suppose a calibrated global architecture supplies

\[
 N_H=(1+o(1))\frac WM
\tag{9.3}
\]

carrier packets to which Theorem 8.1 can be applied.  Then the literal
length would be

\[
 \begin{aligned}
 N_H\bigl(M+3L(2Q+1)\bigr)
 &=(1+o(1))W
   +O\!\left(\frac{WLQ}{M}\right).
 \end{aligned}
\tag{9.4}
\]

Thus \(LQ=o(M)\) is exactly the coefficient-one reset condition for this
separately initialized route family.

There is a nontrivial regime with both negligible overhead and large
correlated square capacity.  Assume here that \(Q\to\infty\), as in the
calibrated regime, and let \(\omega=\omega(m)\) satisfy

\[
 1\ll\omega\ll \frac MQ,
\tag{9.5}
\]

and take

\[
 L=\left\lfloor\frac{M}{Q\omega}\right\rfloor,
\tag{9.6}
\]

provided the tag-capacity inequality in (8.6) holds.  Then the extra
literal length per carrier is

\[
 (6+o(1))\frac M\omega=o(M),
\tag{9.7}

\]

while the half-reversal square metric per carrier is

\[
 (1+o(1))\frac{MQ}{2\omega}.
\tag{9.8}
\]

Across (9.3), this is

\[
 (1+o(1))\frac{WQ}{2\omega}.
\tag{9.9}
\]

In the calibrated scale

\[
 H\asymp\sqrt{m\log m},
 \qquad
 Q\asymp\sqrt{m\log\log m},
 \qquad M\asymp m,
\tag{9.10}
\]

the tag-capacity condition is compatible with (9.5)--(9.6).  Choosing
\(\omega=o(Q)\) makes (9.9) larger than linear in \(W\), while the literal
overhead remains \(o(W)\).

This large number is a **metric capacity**, not a proved correction
theorem.  Each half-reversal bit ties together its entire multirank train.
The exact number of independently choosable signs is only

\[
 L N_H=(1+o(1))\frac{WL}{M}.
\tag{9.11}
\]

For the choice (9.6), this is \((1+o(1))W/(Q\omega)\).  No theorem here
shows that these correlated directions frame every diffuse weighted excess
mode.

There is also a sharp limitation for isolated rectangles in this route
packaging.  Every independent triangle bit requires three separately
initialized paths.  Hence coefficient one forces

\[
 L=o(M/Q).
\tag{9.12}
\]

If each bit is specialized to one isolated adjacent-swap rectangle, only
\(o(M/Q)\) independent isolated directions occur per carrier.  Products of
\(p=O(Q)\) disjoint row swaps can display \(O(LQ)=o(M)\) support-disjoint
rectangles, but those \(p\) rectangles share one sign within a triangle.
Obtaining \(\Theta(M)\) independently addressable static rectangles by
this separately initialized family would incur a positive linear toll.
Long-block interpolation avoids the square-metric loss, but not the
correlation issue.

## 10. Exact proved boundary

### Proved

1. Three tags suffice for exact statewise connector cancellation with a
   surviving marked rectangle.
2. The complete designated hard-flag ledger is (3.4), including every
   controlled rank.
3. Equality of the middle-owner multiset is exactly characterized by
   (3.5).
4. Tag-free cyclic continuations give exactly \(M\) designated states and
   zero internal designated collision at every controlled rank.
5. The exact three-path literal cost is \(M+6Q+3\).
6. Three tags are minimal in the tag-static simple-post-edge matching
   category.  The natural two-tag coloured escape collides for the actual
   internal static cuts covered by Proposition 6.2.
7. A four-cycle carries two disjoint rectangles, and an even \(k\)-cycle
   carries \(k/2\).
8. The \(L\)-triangle cube gives \(L\) independently choosable
   exact-owner-preserving orientations at literal length
   \(M+3L(2Q+1)\).  Nontrivial adjacent-swap specializations give \(L\)
   linearly independent directions.
9. Half reversal gives exact total square metric
   \(2L\lfloor Q^2/4\rfloor\).

### Not proved

1. The packet's squarefree owner set is not proved to coincide with a
   prescribed packet of one already fixed exact wreath factor.  If one
   alternative is support-feasibly installed in such a factor, every bit
   choice is an exact middle-owner-preserving replacement; the installation
   statement itself remains open.
2. No global selection theorem makes the designated flags of different
   carriers disjoint or bounds their cross-carrier factorial collision
   excess.
3. The initialization-transient flags are not part of (3.4).  Their number
   is exactly the displayed \(o(M)\) overhead in the coefficient-one
   regime, but no factorial-collision estimate for their labels is asserted.
4. No weighted curvature/frame inequality turns the half-reversal metric
   capacity into guaranteed negative energy against every residual load.
5. The model-relative minimality theorem does not exclude a two-tag circuit
   with an additional persistent non-tag separator or the exceptional
   \((Q-1)\)-prefix cut.
6. The three or \(3L\) literal paths are not fused into one quotient
   component.  They are separate standalone words whose initialization
   costs have already been charged exactly.

## 11. Independent audit of the decisive steps

Three independent proof audits were requested.

The first recomputed the edge state (2.4), removed all tags, and obtained
exactly

\[
 (m',H',M')=(m-2,H-1,M-3)
\]

for one triangle and

\[
 (m',H',M')=(m-2,H-3L+2,M-3L)
\]

for \(L\) triangles.  It independently checked the cyclic phase formula
(4.9), the proper-interval inequalities, all state counts, and the literal
lengths \(M+6Q+3\) and \(M+3L(2Q+1)\).  It also identified the necessary
positive-arc condition \(M\ge6L\) and the separate asymptotic requirement
\(LQ=o(M)\).

The second audit recast the circulation as two matchings in the tag--edge
incidence graph.  Under the explicitly stated matching-model hypothesis,
it verified that this graph has no four-cycle and that the triangle is its
shortest alternating cycle.  It also recomputed the post-first middle owner
(6.2), confirming the buffer-independent two-tag collision and the exact
limitation of that obstruction to cuts for which the \((Q-1)\)-prefix is
unchanged.

The third audit adversarially checked the complete report.  It confirmed
all rotor recurrences, parameter reductions, cyclic phase formulas,
owner/flag distinctness claims, rectangle signs, square metrics, and exact
lengths.  It caught and caused the following scope corrections now present
in the statements: the finite hypotheses before Section 2; the explicit
matching assumption in Theorem 6.1; the condition \(kQ=o(M)\) for growing
even cycles; the nonzero-direction hypothesis for linear independence; and
the condition \(Q\to\infty\) for the asymptotic constants in
(9.7)--(9.9).

Finally, the sign and constant ledger was checked directly:

\[
 d_{ab}+d_{bc}+d_{ca}=0
\]

when the three bases agree;

\[
 d_{ab}(P)+d_{bc}(P)=d_{ac}(P);
\]

one adjacent swap changes exactly one prefix cut; and

\[
 2\sum_{h=0}^{Q}\min(h,Q-h)
 =2\left\lfloor\frac{Q^2}{4}\right\rfloor.
\]

The decisive conclusion survives these audits: the three-tag circulation
is an integral, literal, owner-simple, middle-preserving local packet with
exactly cancelled connectors and a nonzero marked rectangle.  The remaining
coefficient-one gate is global packet installation/selection and a
target-specific frame inequality, not local connector or owner positivity.
