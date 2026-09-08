# Hand Hall attack on the 924-port physical forest

> **Closure addendum (2026-07-25).**  The corrected family
> \(\mathcal H'=(\mathcal H_{\rm old}-127(10))+347(10)\) has now been
> audited through all A--E internal-deletion rows.  Four formerly omitted E
> incidences raise the E total from 82 to 86.  The class maxima are
> \(8,5,8,10\), and there is an explicit matching saturating all 32
> certified holes with distinct tail wreaths.  See
> `K11_CORRECTED_TAIL_TRANSVERSAL_AND_COUPLED_GATE_20260725.md`.  Thus the
> backward-tail Hall stage is closed; head survival, simultaneous upper
> repair, common ports, and acyclicity remain.

Date: 2026-07-25

## 1. Outcome

There is an orientation issue in the proposed lower-colour repair count.
For the actual 924-port graph, every genuinely missing cyclic four-colour,
not merely thirty of them, has seven backward-safe witnesses in seven
different tail wreaths.  This statement is independent of the particular
list of missing colours.

The resulting hole--tail incidence graph is left 7-regular.  Consequently,
if its maximum tail-wreath degree is at most 11, then it has a matching of
size at least 21.  This is exactly the number of distinct lower holes that
must be repaired when no old lower colour is extinguished.

However, the displayed recursive order table and the displayed list of 32
holes in `K11_CANONICAL_CYCLIC4_SUPPORT_CLASSIFICATION_20260725.md` are
inconsistent.  A class-E row makes the claimed hole

\[
 \{1,2,7,10\}
\]

a literal cyclic four-window.  Hence the requested right-degree audit cannot
soundly be performed on the advertised 32-set family until either the class
table or the hole list is corrected.  A complete hand check of classes C and
D finds no such error there.

The exact two-ledger inequalities also force at least

\[
 6+L_B+L_Y
\]

of the 36 seams to create an initially missing colour on both sides.  The
two colours at every such seam are disjoint four-sets.

## 2. Orientation-complete seven-witness lemma

Let \(F\) be any exact wreath factor on eleven coordinates, and let
\(\mathcal H_4\) be the family of four-sets absent from its cyclic
four-window support.

### Theorem 2.1

For every \(C\in\mathcal H_4\) and every
\(\beta\in[11]\setminus C\), there is a backward-safe off-factor splice
incidence whose new lower colour is \(C\).  The seven choices of \(\beta\)
belong to seven different tail wreaths.

#### Proof

Put

\[
 W=C\cup\{\beta\}.
\]

Exactness gives a unique tail wreath containing the rank-five vertex \(W\).
Write its cyclic order on this five-window as

\[
 W=(w_0,w_1,w_2,w_3,w_4).
\]

The coordinate \(\beta\) cannot be \(w_0\) or \(w_4\).  Otherwise deleting
that endpoint would make \(C\) one of the old cyclic four-windows, contrary
to \(C\in\mathcal H_4\).  Thus

\[
 \operatorname{pos}_W(\beta)\in\{1,2,3\}.
\tag{2.1}
\]

If the position is 1 or 2, let \(t_+\) be the coordinate immediately after
\(W\) in the tail order and use the forward path ending at

\[
 U_+=W\cup\{t_+\}.
\]

The orientation audit says precisely that deletion of \(w_1\) or \(w_2\)
is backward-safe.  Its last source is \(L=W\), its cross source is

\[
 H'=U_+-\beta=C\cup\{t_+\},
\]

and therefore

\[
 B^*=L\cap H'=C.
\tag{2.2}
\]

If the position is 2 or 3, let \(t_-\) be the coordinate immediately before
\(W\), take \(U_-=W\cup\{t_-\}\), and traverse the tail wreath in reverse.
Relative to the notation of the orientation audit, \(W\) is then the last
source and its positions 2 and 3 are the reverse-safe omissions \(q_3,q_4\).
Again the cross source is \(C\cup\{t_-\}\), and (2.2) follows.

In either construction \(\beta\) is internal, so the cross source is neither
of the two on-factor facets of \(U_\pm\).  It is consequently owned by a
different wreath, as required for a splice.

It remains to prove distinctness of the seven tail wreaths.  Suppose
\(C\cup\{\beta\}\) and \(C\cup\{\gamma\}\), with \(\beta\ne\gamma\),
were five-windows in one cyclic order.  Their intersection has size four.
Two distinct length-five windows on an eleven-cycle have intersection four
only when they are consecutive.  Their intersection is then itself a
cyclic length-four window, namely \(C\), a contradiction.  Thus the seven
owners are distinct. \(\square\)

### Consequence 2.2

The two colours singled out in (6.2) of the support-classification note can
be exceptional only for its fixed forward convention.  They cannot be
exceptional in the orientation-complete 924-port graph if they are genuine
holes.  A position-3 omission is supplied by the reverse construction
above.

The theorem is only a backward-tail statement.  The head can still be
double-blocked, and different selected incidences still have to use one
common port per wreath.

### Proposition 2.3 (the seven-letter hole digraph)

Fix a genuine hole \(C\), put \(X=[11]\setminus C\), and write
\(W_x=C\cup\{x\}\) for \(x\in X\).  The two rank-six targets adjacent to
\(W_x\) in its owner wreath have the form

\[
 C\cup\{x,e_-(x)\},\qquad C\cup\{x,e_+(x)\},
\]

where \(e_-(x),e_+(x)\in X\setminus\{x\}\) are the coordinates immediately
before and after the five-window \(W_x\).  Direct the two pairs from \(x\)
to \(e_-(x),e_+(x)\).  This produces an oriented simple graph on the seven
letters of \(X\), with outdegree exactly two at every vertex and 14 directed
edges in total.

If \(s(x)\in\{1,2,3\}\) is the position of \(x\) in its owner window, the
backward-safe repair arcs for \(C\) are exactly

\[
 \begin{array}{c|c}
 s(x)&\text{safe outarcs}\\ \hline
 1&x\to e_+(x)\\
 2&x\to e_-(x),\ x\to e_+(x)\\
 3&x\to e_-(x).
 \end{array}
\tag{2.3}
\]

For a safe arc \(x\to t\), the head source is \(W_t=C\cup\{t\}\).  If
\(s(t)=2\), that arc cannot be double-blocked at the head.  If \(s(t)=1\),
it is double-blocked exactly when the protected coordinate \(c\in C\) is
the last coordinate of the ordered window \(W_t\); if \(s(t)=3\), it is
double-blocked exactly when \(c\) is the first coordinate of \(W_t\).

#### Proof

The two extensions of \(W_x\) along its owner cycle give the two displayed
targets.  A reciprocal pair \(x\to t\) and \(t\to x\) would assign the same
rank-six set \(C\cup\{x,t\}\) to two different wreaths.  The owners are
different by Theorem 2.1, and exact rank-six ownership forbids this.  Hence
the directed graph is simple and has seven times two edges.

The safe-arc table is the forward/reverse position calculation in the proof
of Theorem 2.1.  At the head, \(t\) is internal in \(W_t\) because \(C\) is
missing.  Corollary 5.2 of the physical gate leaves only the double-block
patterns

\[
 (\operatorname{pos}(c),\operatorname{pos}(t))=(4,1),(0,3),
\]

which gives the last assertion. \(\square\)

This seven-vertex digraph is a smaller exact object on which the remaining
head-survival question can be attacked.  In particular, every safe repair
arc entering a position-2 vertex survives automatically; an all-blocked
hole must avoid that possibility and must align every other safe inarc with
one prescribed endpoint coordinate of its head window.

### Corollary 2.4 (middle-position survival bound)

Let

\[
 m_C=|\{x\in X:s(x)=2\}|.
\]

Then \(C\) has at least

\[
 \boxed{\max\{0,5m_C-21\}}
\tag{2.4}
\]

fully physical repair arcs, before any global port choices are imposed.
These arcs use at least

\[
 \boxed{\left\lceil\max\{0,5m_C-21\}/2\right\rceil}
\tag{2.5}
\]

different tail wreaths.  In particular, a hole whose seven backward-safe
witnesses are all head-blocked must have \(m_C\le4\).

#### Proof

The table (2.3) contains exactly \(7+m_C\) safe arcs.  Every vertex of the
full hole digraph has indegree at most four: its two outedges occupy two of
its six unordered pairs, reciprocal arcs are forbidden, and only the other
four pairs can point into it.  Hence at most \(4(7-m_C)\) safe arcs can end
outside the \(m_C\) middle-position vertices.  At least

\[
 (7+m_C)-4(7-m_C)=5m_C-21
\]

safe arcs enter a middle-position vertex, and Proposition 2.3 says that all
of them pass a head orientation.  One tail letter supplies at most two of
the safe arcs, giving (2.5). \(\square\)

## 3. The exact Hall threshold

Define a bipartite graph \(R\) with left side \(\mathcal H_4\) and right
side the 42 wreaths.  Join \(C\) to the owner of
\(C\cup\{\beta\}\) for each \(\beta\notin C\).  Theorem 2.1 proves

\[
 d_R(C)=7
 \quad(C\in\mathcal H_4).
\tag{3.1}
\]

If \(|\mathcal H_4|=32\), then

\[
 |E(R)|=224.
\tag{3.2}
\]

Let

\[
 \Delta=\max_{Q\text{ a wreath}}d_R(Q).
\]

### Proposition 3.1

The matching number satisfies

\[
 \boxed{\displaystyle
 \nu(R)\ge
 \left\lceil\frac{224}{\max\{7,\Delta\}}\right\rceil.}
\tag{3.3}
\]

In particular,

\[
 \Delta\le11\quad\Longrightarrow\quad \nu(R)\ge21.
\tag{3.4}
\]

#### Proof

By Konig's theorem, let \(K\) be a vertex cover of size \(\nu(R)\).  Each
left vertex of \(K\) covers at most seven edges and each right vertex covers
at most \(\Delta\) edges.  Hence

\[
 224=|E(R)|\le\max\{7,\Delta\}|K|.
\]

This gives (3.3).  If \(\Delta\le11\), a cover of size 20 meets at most 220
edges, proving (3.4). \(\square\)

The uniform cap 11 is sufficient but not necessary.  If the 42 right
degrees in decreasing order are

\[
 d_1\ge d_2\ge\cdots\ge d_{42},
\]

then the sharper degree-sequence condition

\[
 \boxed{
 7(20-r)+\sum_{j=1}^r d_j<224
 \quad(0\le r\le20)}
\tag{3.5}
\]

also forces \(\nu(R)\ge21\).  Indeed, a putative 20-vertex cover using
\(r\) right vertices and \(20-r\) left vertices meets at most the left side
of (3.5).  This criterion remains available if a small number of the A/B/E
rows exceed 11.

Thus the finite hand calculation that matters is not the earlier
30-colour witness table.  It is the maximum, over the 42 displayed cyclic
orders, of the number of genuine holes among the 33 internal deletions

\[
 \{w_i,w_{i+1},w_{i+2},w_{i+3},w_{i+4}\}-w_{i+j},
 \qquad j=1,2,3.
\tag{3.6}
\]

The bound 11 would close the backward-tail Hall count exactly.  It would not
yet remove head double-blocks or prove the port forest.

## 4. Exact coupled-ledger inequalities

For either ledger \(Z\in\{B,Y\}\), the initial support is 298 and the final
support identity is

\[
 \sigma_Z^{\rm fin}=298-L_Z+G_Z.
\]

Therefore a support of at least 319 is equivalent to

\[
 \boxed{G_Z-L_Z\ge21.}
\tag{4.1}
\]

There are only 32 initially missing colours, so

\[
 G_Z\le32,
 \qquad
 \boxed{L_Z\le11.}
\tag{4.2}
\]

Let \(E_B\) be the selected seams whose new lower colour was initially
missing, and define \(E_Y\) analogously.  Repetitions can only increase
these occurrence counts, so

\[
 |E_B|\ge G_B\ge21+L_B,
 \qquad
 |E_Y|\ge G_Y\ge21+L_Y.
\]

Since there are 36 seams,

\[
 \boxed{
 |E_B\cap E_Y|
 \ge |E_B|+|E_Y|-36
 \ge 6+L_B+L_Y.}
\tag{4.3}

For a seam with tail six-set \(U\), cross omission \(\beta\), protected
tail endpoint \(t\), complement \(D=[11]\setminus U\), and first head
insertion \(\alpha\),

\[
 B^*=U\setminus\{t,\beta\},
 \qquad
 Y^*=D\setminus\{\alpha\}.
\]

Consequently

\[
 B^*\cap Y^*=\varnothing,
\]

and more exactly

\[
 [11]=B^*\mathbin{\dot\cup}Y^*
       \mathbin{\dot\cup}\{t,\beta,\alpha\}.
\tag{4.4}

Thus every candidate forest must contain at least six simultaneous repairs
even when neither old ledger loses a colour, and every such repair pairs two
disjoint holes.  Each old-colour extinction raises the required number in
(4.3) by one.

## 5. Inconsistency in the advertised hole classification

Take the displayed \(T_4\) row

\[
 R_4\mid I_4=4217\mid6538.
\]

The displayed class-E formula is

\[
 R=(10-I_4,1),
 \qquad I=(10,10-R_4).
\]

Componentwise subtraction gives

\[
 R=(4,5,7,2,1),
 \qquad I=(10,6,8,9,3),
\]

and hence

\[
 \pi=(0,4,5,7,2,1,10,6,8,9,3).
\tag{5.1}
\]

Positions 3 through 6 of (5.1) form the cyclic four-window

\[
 (7,2,1,10),
\]

so \(\{1,2,7,10\}\) is supported.  But it is listed as absent in (4.1)
of the classification note.  At least one of the following is therefore
wrong:

1. the \(T_4\) row;
2. the class-E formula or its componentwise convention;
3. the 32-hole list.

In fact the first two items agree with the displayed recursion.  For the
class-E case one has \(r=4\), hence \(h=10\) and empty \(q\).  Equation
(1.1) gives

\[
 R=(10-I(\operatorname{rc}(p)),1),\qquad
 I=(10,10-R(\operatorname{rc}(p))).
\]

As \(p\) ranges over all semilength-four Dyck words,
\(\operatorname{rc}(p)\) also ranges over all of them.  Thus the displayed
row \(4217\mid6538\) must occur in class E and forces (5.1).  Subject to the
recursive definition stated in the classification note, it is therefore the
hole list (and possibly the claimed total derived from it), rather than the
class-E formula, that needs correction.

Until this is reconciled, the proposed 32-vertex Hall graph and any exact
right-degree number computed from that list are not certified objects.

## 6. Independent class-C and class-D audit

The four class-C rows and five class-D rows were expanded directly from the
displayed formulas.  Their cyclic four-window supports are as follows; `10`
is written in full and each four-set is written by concatenating its sorted
entries with commas suppressed where unambiguous.

```text
C1: 0124 1247 1279 1679 5679 3569 3568 35810 03810 04810 02410
C2: 0124 1248 1278 1678 5678 3567 35610 35910 03910 04910 0249
C3: 0123 1237 1379 1679 4679 4569 4568 45810 05810 02810 02310
C4: 0123 1238 1378 1678 4678 4567 45610 45910 05910 02910 0239

D1: 0246 1246 1249 1289 1789 5789 3578 35710 03510 03610 04610
D2: 0236 1236 1239 1389 1789 4789 4578 45710 04510 05610 02610
D3: 0245 1245 1259 1289 1689 6789 3678 36710 03710 03410 04510
D4: 0235 1235 1359 1589 1489 4689 4678 46710 06710 02710 02310
D5: 0234 1234 1349 1389 1689 5689 5678 56710 05710 02710 02410
```

None is in either displayed list (3.1) or (4.1).  The class-C rows also
follow directly from the two \(T_2\) rows in the \(r=2\) recursion, and the
class-D rows follow from all five displayed \(T_3\) rows in the \(r=3\)
recursion.  No correction to the C or D row formulas is indicated by this
hand audit.  The inconsistency lies in the A/B/E portion or in the claimed
complement list.

## 7. Conditional C/D right-degree audit for the corrected family

For this section only, adopt the provisional correction

\[
 \mathcal H'_4=
 \bigl(\mathcal H^{\rm old}_4\setminus\{\{1,2,7,10\}\}\bigr)
 \cup\{\{3,4,7,10\}\}.
\tag{7.1}
\]

This is conditional until the class-A/B/E and global-support audits confirm
that (7.1) is the genuine 32-hole family.

For a cyclic order \(z=(z_0,\ldots,z_{10})\), define the three internal
deletion templates, with indices modulo 11, by

\[
 \begin{aligned}
 \Delta_1(i)&=\{z_i,z_{i+2},z_{i+3},z_{i+4}\},\\
 \Delta_2(i)&=\{z_i,z_{i+1},z_{i+3},z_{i+4}\},\\
 \Delta_3(i)&=\{z_i,z_{i+1},z_{i+2},z_{i+4}\}.
 \end{aligned}
\tag{7.2}
\]

Thus \(\Delta_j(i)\) deletes position \(j\) from the length-five window
starting at \(i\).  Substitution of the nine displayed C/D rows in (7.2)
gives the following complete table.  In the order column and hole entries,
`A` denotes the coordinate 10.

| row | cyclic order \(z\) | \(\Delta_1\cap\mathcal H'_4\) | \(\Delta_2\cap\mathcal H'_4\) | \(\Delta_3\cap\mathcal H'_4\) | degree |
|---|---|---|---|---|---:|
| C1 | `0421796538A` | `1479` | `0147, 1269` | `0247` | 4 |
| C2 | `042187653A9` | `1478` | -- | -- | 1 |
| C3 | `0231796458A` | `1469, 025A` | `1369, 0258` | `0237, 1479, 258A` | 7 |
| C4 | `023187645A9` | -- | `025A` | `1478, 259A` | 3 |
| D1 | `0642198753A` | `1269` | `1469` | -- | 2 |
| D2 | `0623198745A` | `1369, 1478, 0256` | `1269, 1479, 047A` | `2369, 025A` | 8 |
| D3 | `0452198673A` | `047A` | `1459, 2589, 0347, 025A` | `1269, 347A` | 7 |
| D4 | `0235198467A` | `047A, 0237` | `1469` | `1459, 267A, 025A` | 6 |
| D5 | `0243198657A` | `025A, 0247` | `0257, 247A` | `1369, 257A, 047A` | 7 |

Here each displayed entry occurs for one of the eleven cyclic starting
indices, and direct inspection of the other template values gives no member
of (7.1).  For example, the degree-eight row D2 decomposes exactly as

\[
 \begin{array}{c|l}
 \Delta_1&1369,1478,0256\\
 \Delta_2&1269,1479,047(10)\\
 \Delta_3&2369,025(10).
 \end{array}
\]

The entries within a row are distinct, as they must be for a genuine hole:
two different five-supersets of the same hole in one wreath would make that
hole a cyclic four-window by the argument of Theorem 2.1.

Consequently the four C rows contribute

\[
 4+1+7+3=15
\]

hole--tail incidences, the five D rows contribute

\[
 2+8+7+6+7=30,
\]

and the exact conditional maximum on classes C and D is

\[
 \boxed{\Delta_{C\cup D}=8,}
\tag{7.3}
\]

attained only by D2 among these nine rows.  Thus every C/D row lies safely
below the degree-11 Hall threshold.  The global Hall conclusion still
depends on the remaining 33 A/B/E rows and on confirmation of (7.1).

## 8. Exact status of the forest attack

What is proved without enumeration is:

* every true hole has seven backward-safe witnesses in seven distinct tail
  groups;
* the Hall threshold is the sharp finite cap \(\Delta\le11\);
* support 319 forces (4.1)--(4.3), including at least six disjoint-hole
  double repairs;
* the supplied support data are internally inconsistent, while classes C
  and D pass a complete hand check;
* conditional on the provisional family (7.1), the nine C/D tail degrees
  have exact maximum eight.

What is not proved is:

* confirmation of the corrected hole list and the A/B/E tail-wreath maximum
  degree;
* survival of 21 Hall witnesses after the head double-block filter;
* compatibility with one common port per wreath, indegree constraints, and
  acyclicity;
* the physical rainbow forest itself.

The immediate prerequisite is therefore a corrected, internally consistent
cyclic-four support classification.  Only then can the exact degree-11 Hall
test be completed.
