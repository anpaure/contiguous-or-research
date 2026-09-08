# Lane F: layered MSW path covers and an exact Catalan-fibre phase switch

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The MSW/Chung--Feller exact factor has a precise layered matching normal
form.  Let

\[
        \mathcal R=\mathcal D_{2m}^{0},\qquad
        B=|\mathcal R|=\operatorname {Cat}_m,
\]

and write

\[
        X_t(u)=f^t(u)\in\mathcal D_{2m}^{t}
        \quad(0\le t\le m),\qquad u\in\mathcal R.
\]

A phase-respecting alternative is completely described by permutations
\(p_t\in\operatorname {Sym}(\mathcal R)\).  It is an exact complementary
path factor precisely when

1. \(p_0=p_m\) (after a row relabelling, both are the identity);
2. every consecutive pair
   \(X_t(p_tu),X_{t+1}(p_{t+1}u)\) is Johnson adjacent; and
3. the aggregate union-colour multiset is

   \[
     \biguplus_{t=0}^{m-1}\biguplus_{u\in\mathcal R}
       \{X_t(p_tu)\cup X_{t+1}(p_{t+1}u)\}
       =\binom{[2m]}{m+1}.
       \tag{0.1}
   \]

Equivalently, in relative matchings

\[
              \sigma_t=p_{t+1}p_t^{-1},
\]

the endpoint condition is the zero-monodromy equation

\[
              \sigma_{m-1}\cdots\sigma_1\sigma_0=1.
              \tag{0.2}
\]

This class is **not rigid**.  There is an exact two-row, two-cut switch,
already visible in semilength two, which preserves all \(X\)-states,
preserves the aggregate \(Y\)-palette, and leaves both endpoints of every
row fixed.  Suspended in an arbitrary aligned Dyck context, it peels one
row away from a \(\operatorname {Cat}_r\)-fold aligned fibre, simultaneously
on its lower intersection target and its upper union target.

Thus the aligned Catalan fibre is not an invariant of exact
MSW/Chung--Feller phase matching.  What is proved here is one-row
dispersion, not a packing theorem that disperses all fibres at once.

## 1. The canonical layered cover

Regard a balanced up/down word of length \(2m\) as its set of up-step
positions, hence as an \(m\)-subset of \([2m]\).  Let
\(\mathcal D_{2m}^{t}\) be the class of balanced paths with exactly \(t\)
flaws.  Chung--Feller gives

\[
       |\mathcal D_{2m}^{t}|=B
       \quad(0\le t\le m),
       \qquad (m+1)B=\binom{2m}{m}.
       \tag{1.1}
\]

The MSW minimum-change map is a bijection

\[
       f:\mathcal D_{2m}^{t}\longrightarrow
                       \mathcal D_{2m}^{t+1}.
       \tag{1.2}
\]

It factors as \(f=h\circ g\), where \(g\) inserts one up-step and \(h\)
deletes one.  For \(u\in\mathcal R\), put

\[
       X_t(u)=f^t(u),\qquad
       Y_t(u)=X_t(u)\cup X_{t+1}(u)=g(X_t(u)).
       \tag{1.3}
\]

The canonical columns are

\[
       X_0(u),X_1(u),\ldots,X_m(u).
       \tag{1.4}
\]

They have the following three exact properties.

* At layer \(t\), the states \(X_t(u)\), \(u\in\mathcal R\), are exactly
  \(\mathcal D_{2m}^{t}\).
* The map \(g\) is a bijection from

  \[
       \mathcal D_{2m}^{0}\sqcup\cdots\sqcup
       \mathcal D_{2m}^{m-1}
       \quad\hbox{onto}\quad \binom{[2m]}{m+1}.
  \]

  Hence all \(Y_t(u)\) are distinct and exhaust the upper layer.
* The endpoint theorem is

  \[
                         X_m(u)=\overline{X_0(u)}.
                         \tag{1.5}
  \]

The usual odd-factor column is obtained by adjoining a new coordinate
\(\infty\) and replacing every colour \(Y_t(u)\) by

\[
             Z_t(u)=\{\infty\}\cup([2m]\setminus Y_t(u)).
             \tag{1.6}
\]

Then

\[
 X_0(u),Z_0(u),X_1(u),Z_1(u),\ldots,Z_{m-1}(u),X_m(u)
 \tag{1.7}
\]

is a \((2m+1)\)-cycle in \(KG(2m+1,m)\), closed by (1.5).

## 2. Exact characterization of alternative phase matchings

The word "phase" below means the flaw layer, not a cyclic rotation of one
already constructed wreath.

### Theorem 2.1 (layer-permutation normal form)

Let \(p_0,\ldots,p_m\) be permutations of \(\mathcal R\), and define

\[
                         X'_t(u)=X_t(p_tu).
                         \tag{2.1}
\]

The rows

\[
                  X'_0(u),X'_1(u),\ldots,X'_m(u)
                  \tag{2.2}
\]

give a phase-respecting exact MSW-type wreath factor if and only if:

\[
 |X'_t(u)\triangle X'_{t+1}(u)|=2
 \quad(u\in\mathcal R,\ 0\le t<m),                 \tag{2.3}
\]

\[
 p_m=p_0,                                             \tag{2.4}
\]

and

\[
 \biguplus_{t,u}\{X'_t(u)\cup X'_{t+1}(u)\}
     =\binom{[2m]}{m+1}.                              \tag{2.5}
\]

Every phase-respecting alternative path cover arises uniquely in this
form, up to one common relabelling of its rows.

#### Proof

Because \(p_t\) is a permutation, the states at layer \(t\) in (2.1)
are exactly \(\mathcal D_{2m}^{t}\).  Over all layers, therefore, every
\(m\)-subset of \([2m]\) occurs once.

Condition (2.3) makes each consecutive pair a Johnson edge, and its union
is an \((m+1)\)-set.  Condition (2.5) says exactly that these union colours
occur once each.  Applying (1.6), their complements with \(\infty\)
therefore own once each all middle vertices containing \(\infty\).

It remains only to check the closing edge.  By (1.5),

\[
 X'_m(u)=X_m(p_mu)=\overline{X_0(p_mu)}.
\]

This is the complement of \(X'_0(u)=X_0(p_0u)\) for every \(u\) if and
only if \(p_m=p_0\), since \(u\mapsto X_0(u)\) is injective.  Hence
(2.3)--(2.5) produce vertex-disjoint cycles (1.7) covering the entire odd
middle layer.

Conversely, in a phase-respecting cover, layer \(t\) uses every member of
\(\mathcal D_{2m}^{t}\) once.  Relative to the canonical indexing this is
a unique permutation \(p_t\).  Johnson legality gives (2.3), exact
ownership of the vertices containing \(\infty\) gives (2.5), and
complementary endpoints give (2.4).  A common relabelling changes all
\(p_t\) on the right by the same permutation and changes no physical row.
\(\square\)

### Corollary 2.2 (relative matchings and monodromy)

After the harmless gauge choice \(p_0=1\), put

\[
                         \sigma_t=p_{t+1}p_t^{-1}.
                         \tag{2.6}
\]

Then \(\sigma_t\) is the matching from canonical row labels at layer
\(t\) to canonical row labels at layer \(t+1\).  The exact conditions are

\[
 X_t(v)\sim_JX_{t+1}(\sigma_tv)                     \tag{2.7}
\]

for every \(t,v\), the aggregate colour equation

\[
 \biguplus_{t,v}
 \{X_t(v)\cup X_{t+1}(\sigma_tv)\}
 =\binom{[2m]}{m+1},                                \tag{2.8}
\]

and the monodromy equation

\[
                    \sigma_{m-1}\cdots\sigma_0=1.   \tag{2.9}
\]

Conversely, (2.7)--(2.9) reconstruct \(p_t\) by
\(p_{t+1}=\sigma_tp_t\).

In particular, a nontrivial change at only one cut is impossible: it has
nontrivial monodromy.  The smallest possible endpoint-preserving change is
a two-cut dipole.  Importantly, (2.8) is an aggregate equation.  Requiring
the old \(Y\)-palette separately at each cut is a strictly stronger and
unnecessary condition.

### Corollary 2.3 (exact slab criterion)

Suppose only layers \(a,\ldots,b\) in a row set \(U\subseteq\mathcal R\)
are changed and the boundary permutations satisfy \(p_a=p_b=1\) on
\(U\).  Then the replacement is exact if and only if all new consecutive
pairs are Johnson edges and

\[
 \biguplus_{t=a}^{b-1}\biguplus_{u\in U}
 \{X_t(p_tu)\cup X_{t+1}(p_{t+1}u)\}
 =
 \biguplus_{t=a}^{b-1}\biguplus_{u\in U}
 \{X_t(u)\cup X_{t+1}(u)\}.                         \tag{2.10}
\]

There is no separate \(X\)-ledger: at every changed layer, \(p_t\) merely
permutes the old states.

## 3. The exact two-cut rectangle

For a list of common spectator coordinates \(R\), abbreviate
\(\{1,2,4\}\cup R\) to \(124R\).  The semilength-two MSW traces are

\[
\begin{array}{c|ccc}
1100&12&14&34\\
1010&13&23&24.
\end{array}                                               \tag{3.1}
\]

Swap the two states in the middle layer.  The two new traces are

\[
                       12,23,34,
             \qquad    13,14,24.                         \tag{3.2}
\]

Every new consecutive pair is Johnson adjacent.  The four old union
colours are

\[
                   124,134,123,234,                       \tag{3.3}
\]

whereas the four new colours are

\[
                   123,234,134,124.                       \tag{3.4}
\]

Thus the aggregate palette is unchanged.

Notice the essential cross-cut cancellation.  At the first cut the old
palette \(\{124,123\}\) becomes \(\{123,134\}\); at the second cut the
old palette \(\{134,234\}\) becomes \(\{234,124\}\).  Neither cut is
colour-preserving by itself, but their signed discrepancies cancel.

In the permutation normal form, the middle-layer permutation is the
transposition \(\tau\) of the two rows, and the boundary permutations are
the identity.  Hence the two relative matchings are

\[
                           \sigma_0=\tau,
                           \qquad\sigma_1=\tau,           \tag{3.5}
\]

whose product is one.  This is the minimal nonzero-monodromy cancellation.

## 4. A scalable exact switch

Fix \(r\ge1\), put \(s=r+1\), and let

\[
 C_r=1100(10)^{r-1},\qquad
 E_r=(10)^{r+1},\qquad
 R=\{5,7,\ldots,2s-1\}.                               \tag{4.1}
\]

The set \(R\) has size \(r-1\).  The MSW flip orders begin

\[
 \pi(C_r)=(4,2,3,1,\ldots),\qquad
 \pi(E_r)=(2,1,4,3,\ldots).                            \tag{4.2}
\]

Indeed both identities follow from the concatenation law

\[
                   \pi(AB)=\pi(A)\mathbin\Vert
                              (|A|+\pi(B))               \tag{4.3}
\]

for Dyck words \(A,B\), together with
\(\pi(1100)=(4,2,3,1)\) and \(\pi(10)=(2,1)\).
Consequently the first three states are

\[
\begin{array}{c|ccc}
C_r&12R&14R&34R\\
E_r&13R&23R&24R.
\end{array}                                               \tag{4.4}
\]

Replace (4.4) by

\[
\begin{array}{c|ccc}
C_r&12R&23R&34R\\
E_r&13R&14R&24R.
\end{array}                                               \tag{4.5}
\]

The common set \(R\) simply adjoins to every state and every colour in
(3.1)--(3.4).  Hence (4.5) satisfies the exact slab criterion (2.10).
All later states and both endpoints of both rows are unchanged.  We have
therefore proved:

### Theorem 4.1 (noncanonical exact phase cover)

For every \(r\ge1\), the canonical MSW factor in semilength \(r+1\)
admits a noncanonical phase-respecting exact factor obtained by changing
two rows at one intermediate layer.  It preserves every \(X\)-state,
preserves every \(Y\)-colour in aggregate, and preserves the complementary
endpoint pairing row by row.

No assertion about a generic discrepancy rounding is used: this is a
literal integral factor trade.

## 5. Suspension in an aligned Dyck context

The switch is not confined to the top-level two words.  Let
\(P\in\mathcal D_{2p}^{0}\) and \(W\in\mathcal D_{2w}^{0}\) be arbitrary
Dyck words, and put

\[
                         m=p+(r+1)+w.                    \tag{5.1}
\]

Consider the two roots

\[
                         PC_rW,qquad PE_rW.             \tag{5.2}
\]

By (4.3), the MSW exchanges of \(P\), then of the displayed central
block, then of \(W\), occur in three consecutive phase slabs.  During the
central slab, all coordinates outside that block form one fixed spectator
set \(K\).  Thus its first three states are exactly the two rows (4.4),
with \(K\) adjoined and all local coordinates shifted by \(2p\).

Swapping their middle states therefore gives the same exact rectangle.
No other row or phase changes.  This proves:

### Theorem 5.1 (context functor)

The switch of Theorem 4.1 embeds in every concatenation-aligned Dyck
context \(P(\cdot)W\).  It preserves the full global \(X\)- and \(Y\)-
ownership equations and the original complementary endpoints.

## 6. The switch disperses an aligned Catalan fibre

Assume now \(r\ge2\).  In the same context define

\[
              \mathcal F_{P,W}
                =\{P\,10v\,W:v\in\mathcal D_{2r}^{0}\}.
                                                               \tag{6.1}
\]

It contains exactly \(\operatorname {Cat}_r\) rows.  Use local coordinates
\(1,\ldots,2r+2\) on the block \(10v\), and inspect the \(r+1\) states
from immediately after the first \(10\)-exchange through the end of that
block.

For every \(v\), the first exchange replaces local coordinate \(1\) by
local coordinate \(2\).  The next \(r\) exchanges flip every coordinate
of the child block \(\{3,\ldots,2r+2\}\) exactly once.  Therefore, before
the switch, every row in (6.1) has

\[
 \bigcap X_t=K\cup\{2\},
 \qquad
 \bigcup X_t=K\cup
       (\{1,\ldots,2r+2\}\setminus\{1\}),             \tag{6.2}
\]

over this slab.  This is the aligned lower/upper Catalan fibre.

The row \(E_r\) is the member corresponding to \(v=(10)^r\).  After the
switch, its first slab state is \(14R\), its second is \(24R\), and all
later states are canonical.  Local coordinate \(4\) occurs in every one
of these states.  Every other coordinate is absent somewhere:

* \(1\) is absent from the second state;
* \(2\) is absent from the first state;
* \(3\) is absent from every new slab state;
* each odd coordinate in \(R\) is deleted later; and
* every even coordinate at least \(6\) is absent before it is inserted.

Likewise, every local coordinate except \(3\) occurs somewhere: coordinate
\(1\) occurs in the new first state, coordinate \(2\) occurs from the
second state onward, coordinate \(4\) occurs throughout, and the remaining
coordinates occur on one side of their unique exchange.  Hence the changed
row has

\[
 \bigcap X'_t=K\cup\{4\},
 \qquad
 \bigcup X'_t=K\cup
       (\{1,\ldots,2r+2\}\setminus\{3\}).             \tag{6.3}
\]

All other rows of \(\mathcal F_{P,W}\) retain (6.2).  We have proved:

### Theorem 6.1 (exact Catalan-fibre dispersion)

For every \(r\ge2\) and every aligned context \(P(\cdot)W\), there is a
noncanonical exact MSW-type path cover which changes the common lower
target of the distinguished row from \(K\cup\{2\}\) to \(K\cup\{4\}\),
and its common upper target from the complement of local \(1\) to the
complement of local \(3\).  The other
\(\operatorname {Cat}_r-1\) rows retain the old two targets.

Thus both aligned multiplicities split as

\[
               \operatorname {Cat}_r
                   \longrightarrow
               (\operatorname {Cat}_r-1)+1.            \tag{6.4}
\]

In particular, exact \(X\)-ownership, aggregate \(Y\)-ownership, and
complementary endpoints do not force Catalan-fibre alignment.

## 7. Exact scope

The proof settles the local existence-versus-rigidity question in the
nonrigid direction.

It also identifies why the switch was easy to miss.

1. Changing the Chung--Feller starting flaw class only chooses another
   transversal of the same canonical columns.  It does not alter any
   phase matching.
2. A single changed relative matching violates endpoint monodromy.
3. The working switch changes two adjacent cuts, and its \(Y\)-ledger
   cancels only after those cuts are aggregated.
4. A substitution confined to a child hole while fixing both of that
   child's complementary boundary states cannot change the intersection
   of the child slab: every exterior coordinate is always present and
   every child coordinate is absent at one boundary.  The construction
   succeeds because it trades at the **parent** level and changes the
   entrance state of the child fibre.

What remains open is quantitative.  The theorem peels one row from one
aligned fibre.  It does not prove that a positive-density collection of
overlapping parent switches can be chosen simultaneously, nor that all
large Catalan fibres can be reduced to sublinear multiplicity while
retaining exact ownership.  Those are packing/interaction questions, not
local rigidity questions.

## 8. Audit verdict

The proof has five independent load-bearing checks.

| Claim | Verdict | Exact check |
|---|---:|---|
| Layered normal form | PASS | Phasewise permutations preserve every \(X\)-layer; (2.5) is exactly ownership of the \(\infty\)-containing vertices; \(p_m=p_0\) is exactly complementary endpoint closure. |
| Two-cut legality | PASS | All four new pairs in (3.2) differ by one deletion and one insertion. |
| Aggregate \(Y\)-ledger | PASS | Both sides are the literal multiset \(\{123,124,134,234\}\); the cancellation is across two cuts, not cutwise. |
| Context suspension | PASS | The MSW concatenation law makes the prefix-complement and suffix state fixed spectators during the local block. |
| Fibre dispersion | PASS | The canonical slab has intersection \(K\cup\{2\}\) and union missing local \(1\); the changed row has intersection \(K\cup\{4\}\) and union missing local \(3\). |

The only scope warning is the one already stated: this is a certified local
nonrigidity theorem and a one-row fibre split.  Calling it a simultaneous
or asymptotically complete dispersion theorem would be unsupported.

## 9. Authoritative local target: rooted middle-levels path factors

The phase-permutation normal form of Section 2 retains the canonical flaw
layers.  For context substitution this restriction is unnecessary.  The
larger and authoritative local object is the path-factor normal form of
Theorem 17.3 in `MATH_AUDIT_PLATEAU_TRUNCATION_20260726.md`.

Let \(J\) have size \(2r\), let \(D\subseteq\binom Jr\) be the affine
Dyck port family, and let \(\mathsf M(J)\) be the bipartite inclusion graph
between \(\binom Jr\) and \(\binom J{r+1}\).  Assume, as holds for an
affine Dyck family, that \(D\) contains exactly one chosen side of each
boundary port pair used by the canonical local factor.

### Theorem 9.1 (port-path factor dictionary)

There is a bijection between the following objects.

1. Exact \(D\)-port-transversal \(C_{2r+1}\)-factors of
   \(KG(J\cup\{\infty\},r)\).
2. Vertex partitions of \(\mathsf M(J)\) into paths

   \[
   P=X_0\subset Y_0\supset X_1\subset\cdots\subset
   Y_{r-1}\supset X_r=J\setminus P,qquad P\in D.       \tag{9.1}
   \]

The odd cycle reconstructed from (9.1) is

\[
 X_0,Z_0,X_1,Z_1,\ldots,Z_{r-1},X_r,qquad
 Z_t=\{\infty\}\cup(J\setminus Y_t).                  \tag{9.2}
\]

#### Proof audit

Every \(X_t\) is an \(r\)-set and every \(Y_t\) is an \((r+1)\)-set.
The containments in (9.1) make \(X_t\) and \(X_{t+1}\) disjoint from
\(Z_t\), while \(X_r=J\setminus X_0\) gives the closing odd-graph edge.
Partition of the \(X\)-shore is exactly ownership of local odd-graph
vertices avoiding \(\infty\).  The map

\[
 Y\longmapsto\{\infty\}\cup(J\setminus Y)             \tag{9.3}
\]

is a bijection from \((r+1)\)-sets of \(J\) to local odd-graph
\(r\)-sets containing \(\infty\), so partition of the \(Y\)-shore is
exactly the other ownership ledger.  Conversely, cutting every
\(D\)-port-transversal odd cycle at \(\infty\) gives (9.1).  These
operations are inverse.  The shore counts agree:

\[
 (r+1)|D|=\binom{2r}{r},\qquad
 r|D|=\binom{2r}{r+1}.                                \tag{9.4}
\]

Thus no hidden completion condition remains beyond the rooted vertex
partition.

Theorem 9.1 strictly contains Section 2: an alternative local factor need
not keep its \(t\)-th states in the canonical flaw class.  The rectangle
of Sections 3--4 happens to lie in both classes.

## 10. Two-order normal form and the child-window projection

Every path (9.1) has length \(2r\), so its \(X\)-projection has \(r\)
Johnson edges from \(P\) to \(J\setminus P\).  Their Johnson distance is
also \(r\).  Hence the projection is geodesic.

### Lemma 10.1 (deletion--insertion orders)

For every rooted path (9.1), there are unique orderings

\[
 (a_1,\ldots,a_r)\text{ of }P,qquad
 (b_1,\ldots,b_r)\text{ of }J\setminus P               \tag{10.1}
\]

such that, with \(A_t=\{a_1,\ldots,a_t\}\) and
\(B_t=\{b_1,\ldots,b_t\}\),

\[
 X_t=(P\setminus A_t)\cup B_t,                         \tag{10.2}
\]

\[
 Y_t=(P\setminus A_t)\cup B_{t+1}
     =X_t\cup X_{t+1}.                                 \tag{10.3}
\]

#### Proof

At step \(t\), let \(a_t\) be the deleted coordinate and \(b_t\) the
inserted coordinate.  A repeated deletion, a repeated insertion, or the
later reversal of an earlier exchange would make the length-\(r\) path
strictly longer than the distance between its complementary endpoints.
Thus the deleted coordinates are precisely \(P\), the inserted coordinates
are precisely \(J\setminus P\), each once.  Induction gives (10.2), and
adjoining the next inserted coordinate gives (10.3). \(\square\)

For an arbitrary consecutive window \(X_i,\ldots,X_{i+q}\), (10.2) gives
the exact flags

\[
 \boxed{
 \begin{aligned}
 \bigcap_{t=i}^{i+q}X_t
   &=(P\setminus A_{i+q})\cup B_i,\\
 \bigcup_{t=i}^{i+q}X_t
   &=(P\setminus A_i)\cup B_{i+q}.
 \end{aligned}}                                           \tag{10.4}
\]

The parent-to-child window is especially simple.

### Corollary 10.2 (first-edge label theorem)

For the \(r\)-state window after the first transition,

\[
                         X_1,X_2,\ldots,X_r,
\]

one has

\[
 \boxed{
       \bigcap_{t=1}^{r}X_t=\{b_1\},\qquad
       \bigcup_{t=1}^{r}X_t=J\setminus\{a_1\}.}       \tag{10.5}
\]

In an ambient aligned context, the fixed exterior present set is adjoined
to both expressions.  Therefore the full rooted depth-\((r-1)\) child
shadow profile depends only on the first directed Johnson edge

\[
                         P\longrightarrow P-a_1+b_1.   \tag{10.6}
\]

This is the main constructive gain from Theorem 17.3: dispersing an
aligned child Catalan fibre is exactly the problem of dispersing the first
deletion--insertion labels \((a_1,b_1)\) among the rooted paths of a
parent \(D\)-port path factor.  The remaining \(r-1\) edges are needed for
exact completion, but they do not alter this particular child target.

## 11. Exact-cover formulation and the rectangle circuit

For \(P\in D\), let \(\Gamma(P)\) be the \((r!)^2\) ordered pairs in
(10.1), equivalently all rooted complement geodesics from \(P\) to
\(J\setminus P\).  For \(\gamma\in\Gamma(P)\), let
\(V_X(\gamma)\) and \(V_Y(\gamma)\) be the states (10.2) and colours
(10.3).

The authoritative construction target is the following integral exact
cover.  Choose \(z_\gamma\in\{0,1\}\) satisfying

\[
 \sum_{\gamma\in\Gamma(P)}z_\gamma=1
                         \qquad(P\in D),             \tag{11.1}
\]

\[
 \sum_{\gamma:X\in V_X(\gamma)}z_\gamma=1
                         \qquad(X\in\tbinom Jr),      \tag{11.2}
\]

\[
 \sum_{\gamma:Y\in V_Y(\gamma)}z_\gamma=1
                         \qquad(Y\in\tbinom J{r+1}).  \tag{11.3}
\]

By Theorem 9.1, its integral points are bijectively the
\(D\)-port-transversal local factors.  Equations (11.1)--(11.3), not the
canonical MSW recurrence, are the exact local construction constraints.

For the uniform rectangle at local scale \(r\ge2\), put

\[
 R=\{5,7,\ldots,2r-1\},
\]

and use the two rooted path prefixes

\[
 12R,14R,34R,qquad 13R,23R,24R.                    \tag{11.4}
\]

Replacing them by

\[
 12R,23R,34R,qquad 13R,14R,24R                     \tag{11.5}
\]

changes two variables positively and two negatively in (11.1)--(11.3).
On the inclusion graph, after common incidences are suppressed, its support
is the single alternating cycle

\[
 12R-124R-24R-234R-34R-134R-13R-123R-12R.           \tag{11.6}
\]

Thus (11.5) is an integral circuit of the exact-cover system.  It retains
the two roots \(12R,13R\in D\) and their complementary endpoints, so it
proves directly in the authoritative normal form:

### Theorem 11.1 (noncanonical port factor)

For every \(r\ge2\), the canonical affine-Dyck-port factor has a
noncanonical \(D\)-port-transversal mate.  For \(r=1\), the local odd
graph is \(C_3\), so the factor is unique.

The first-edge labels on the two changed roots are

\[
\begin{array}{c|c|c}
P&\text{canonical }(a_1,b_1)&\text{switched }(a_1,b_1)\\ \hline
12R&(2,4)&(1,3)\\
13R&(1,2)&(3,4).
\end{array}                                             \tag{11.7}
\]

Equation (10.5) therefore recovers both shadow changes without inspecting
the later path: on the second row the child intersection changes from
\(\{2\}\) to \(\{4\}\), and the child union changes from
\(J\setminus\{1\}\) to \(J\setminus\{3\}\).

The exact remaining local gate is now clean.  Construct a family of
integral solutions to (11.1)--(11.3) whose first-edge labels (10.6), when
the family member is chosen according to the outer context, split every
relevant aligned Catalan fibre to the required phase-capacity scale.  The
rectangle is a nonzero circuit and proves nonrigidity, but a dense
compatible circuit packing or a larger path-factor library is still
needed for quantitative constant-one dispersion.
