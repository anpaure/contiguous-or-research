# Lane W: PBBS bridge-one residence theorem and a separated-star nonlocal braid

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Exact verdict

This note attacks the weakest full-flag gate \((CP_A)\) directly. It
combines the bridge-one classification from
`ROTOR_MULTI_FRAME_PACKET_RESOLUTION_20260725.md` with the corrected
sandwich and QCF ledgers in
`MATH_ATTACK_W_PBBS_NORMALIZED_PORT_CROSSING_OBSTRUCTION_20260725.md` and
`PBBS_MULTI_CUT_DOMINANCE_CLUSTER_20260725.md`.

The main advance is an exact dynamic characterization which is stronger
than a port-counting statement.

> **Bridge-one residence theorem.** A finite directed Johnson path has a
> full radius-\(H\) bridge-one lift if and only if no coordinate which is
> inserted on the path is removed again within the next \(H\) edges.
> Endpoint queues can be completed whenever
> \[
>    H+1\le r,\qquad H\le n-r,
> \]
> for rank-\(r\) owners in \([n]\).

Thus bridge-one paths forbid short **positive** residence, but they do not
forbid a short absence: a singleton promotion absorbs a reinsertion from
the upper cache. In particular, the upper flag of a promoted state is not
in general the union of the preceding PBBS owners. Any argument which
treats every bridge-one arc as a natural two-sided rotor arc is false.

The theorem gives an exact nonlocal seam signature. Around a proposed
splice, list the last \(H\) insertion labels on the left, the splice
insertion/removal labels, and the first \(H\) removal labels on the right.
The splice is legal exactly when no equal insertion/removal pair at edge
distance at most \(H\) crosses the splice. This is a triangular,
mixed-sign port condition; equality of a normalized endpoint port is
neither necessary nor sufficient.

There is a genuine nonlocal positive class. Suppose a collection of PBBS
path pieces has one common endpoint facet \(F\), their terminal owners are
\(F+b_i\), their initial owners are \(F+a_i\), and, throughout every
radius-\(H\) boundary collar,

* all left-collar insertion labels and all \(a_i\)'s lie in an alphabet
  \(A\);
* all right-collar removal labels and all \(b_i\)'s lie in a disjoint
  alphabet \(B\).

Then **every** tail can be joined to **every** head. Pairwise owner-disjoint
pieces concatenate in an arbitrary order into one bridge-one path, of
exact literal length

\[
   \boxed{M+2H}
\]

for \(M\) owners. Compiling the pieces separately would cost
\(M+2Ht\) for \(t\) pieces. This is an exact \(2H(t-1)\) nonlocal
contraction. The class is PBBS-natural: on a rainbow fixed-core parity
row, the omitted labels split into pairwise disjoint \(a\)- and
\(b\)-alphabets, and each transition inserts an \(a\)-label and removes a
\(b\)-label. The extra common-facet/shadow-twin hypothesis is essential
for the cross edge to be a Johnson edge.

The positive class does not by itself prove \((CP_A)\). Three exact
obstructions remain.

1. A nonlocal join must be an actual Johnson edge; coarse normalized
   singleton ports do not ensure this.
2. The lower full flag on a bridge-one path is forced by the next \(H\)
   removals. If \(J\) PBBS edges are cut and whole pieces are reordered,
   only \(qJ\) depth-\(q\) lower occurrences can change. Consequently a
   balanced depth-\(q\) load is possible only if the original PBBS load is
   within \(2qJ\) in \(\ell^1\) of the balanced load polytope.
3. Promotions alone cannot form a covering transversal with few paths.
   If \(D_H\) distinct top flags occur in a path forest with \(p\)
   components, at least \(D_H-p\) arcs are genuine rotor arcs. For a
   covering transversal \(D_H\ge\binom{2m}{m-H}\), which is
   \(\Theta_A(W)\) for \(H=A\sqrt m\).

There is also a PBBS residence-hitting obstruction. Let \(\nu_H\) be the
maximum number of edge-disjoint positive PBBS residence intervals of
length at most \(H\). If a bridge-one path forest has \(p\) paths and
uses \(c\) non-PBBS chords, then

\[
   \boxed{c\ge \nu_H-p.}
\]

At upper depth \(q\), at most \(W-N_q\) arcs can be flag-preserving in
any covering transversal. Hence at least

\[
   \boxed{\nu_H-p-(W-N_q)}
\]

of the non-PBBS chords must genuinely change the depth-\(q\) upper flag
(when the right side is positive). At \(q=1\),
\(W-N_1=W/(m+1)\). Thus a critical \(\Theta(W/H)\) residence family
cannot be repaired by first-cache, entry-neutral promotions.

Finally, the exact baseline-relative combination is as follows. If the
owners are partitioned into bridge-braided pieces and owner-disjoint
sandwich atoms, if the braided part has \(p\) paths, if the sandwich
excess is \(E_{\rm sand}\), and if the original PBBS crossing windows are
repaired by cut clusters of spans \(S_j\), then the constructed literal
word has length at most

\[
 \boxed{
 W+2Hp+E_{\rm sand}
   +\sum_j(7H+3S_j-3).}
\]

Here the corrected all-phase fixed-fibre ledger may be inserted verbatim:

\[
 E_{\rm sand}
 =\sum_q\bigl(N\bar R_q+(q-1)c_q\bigr),
\]

provided the charged atom owner segments are disjoint and the sandwich
charts are substituted for, rather than appended to, those owner
baselines. No baseline is counted twice. Therefore this route proves a
coefficient-one block compiler for the nontrivial separated-star class
whenever all three displayed excess terms are \(o(W)\). The present note
does **not** prove that the full canonical PBBS factor admits such a
decomposition, nor that its forced lower flag loads are balanced.

## 1. Full states and the exact queue recurrence

Let \(1\le H\le\min(r,n-r)\). A full radius-\(H\) useful state is an
ordered partition

\[
 \omega=(L;z_1,\ldots,z_{2H};R),
 \qquad |L|=r-H,\quad |R|=n-r-H.                 \tag{1.1}
\]

Its middle owner is

\[
 X(\omega)=L\cup\{z_1,\ldots,z_H\}.             \tag{1.2}
\]

Write the two singleton queues as

\[
 \alpha(\omega)=(z_H,z_{H-1},\ldots,z_1),
 \qquad
 \beta(\omega)=(z_{H+1},\ldots,z_{2H}).          \tag{1.3}
\]

Thus \(\alpha_1\) is the first lower deletion and \(\beta_1\) is the
first upper addition.

### Lemma 1.1 (exact bridge-one queue law)

Let \(\omega\to\omega'\) be a bridge-one arc between distinct owners.
Then there are \(x\in L\) and \(b\notin X\) such that

\[
 X'=X-\alpha_1+b,                                \tag{1.4}
\]

and

\[
 \boxed{\alpha'=(\alpha_2,\ldots,\alpha_H,x).}   \tag{1.5}
\]

For the upper cache exactly one of the following holds.

1. If \(b\notin\{\beta_1,\ldots,\beta_H\}\), then \(b\in R\) and
   the arc is a rotor shift:
   \[
      \boxed{\beta'=(\alpha_1,\beta_1,\ldots,\beta_{H-1}).} \tag{1.6}
   \]
2. If \(b=\beta_s\), then the arc is the position-\(s\) singleton
   promotion:
   \[
      \boxed{
      \beta'=(\alpha_1,\beta_1,\ldots,
             \widehat{\beta_s},\ldots,\beta_H).} \tag{1.7}
   \]

In both cases

\[
 L'=L-x+b.                                        \tag{1.8}
\]

#### Proof

Proposition 4.3 of the multi-frame report gives, in \(z\)-coordinates,

\[
 (z'_1,\ldots,z'_{2H})
 =
 \begin{cases}
  (x,z_1,\ldots,z_{2H-1}),&b\in R,\\
  (x,z_1,\ldots,z_{H+s-1},z_{H+s+1},\ldots,z_{2H}),
       &b=z_{H+s}.
 \end{cases}                                     \tag{1.9}
\]

Reversing the first \(H\) singleton positions gives (1.5), and reading
positions \(H+1,\ldots,2H\) gives (1.6)--(1.7). Equation (1.2)
then gives (1.4); the displayed lower block gives (1.8). \(\square\)

The law (1.5) is independent of whether the arc is a rotor or a
promotion. This is the source of the residence theorem.

## 2. Bridge-one paths are exactly long-positive-residence paths

Let

\[
 X_0,X_1,\ldots,X_{s-1}\in\binom{[n]}r           \tag{2.1}
\]

be a directed Johnson path, with

\[
 X_{i+1}=X_i-r_i+a_i
 \qquad(0\le i<s-1).                             \tag{2.2}
\]

A positive residence starts when \(a_i\) is inserted. If its next
removal is at edge \(j>i\), its length is \(j-i\).

### Theorem 2.1 (exact finite bridge-one residence theorem)

Assume

\[
 H+1\le r,
 \qquad H\le n-r.                                \tag{2.3}
\]

The path (2.1) admits one full radius-\(H\) state at every owner such
that every path edge is bridge-one if and only if

\[
 \boxed{
 a_i\ne r_j
 \quad\text{whenever}\quad 0<j-i\le H.}         \tag{2.4}
\]

Equivalently, every positive residence whose insertion and next removal
both occur on the path has length at least \(H+1\).

#### Proof: necessity

Suppose a lift exists. Iterating (1.5) along consecutive arcs gives

\[
 \alpha(X_i)=(r_i,r_{i+1},\ldots,r_{i+H-1})      \tag{2.5}
\]

whenever all displayed edges lie on the path. The next appended queue
element is \(r_{i+H}\in L_i\). Hence
\(r_i,\ldots,r_{i+H}\) are distinct and all belong to \(X_i\). But
\(a_i\notin X_i\), so (2.4) follows.

#### Proof: sufficiency in the interior

Condition (2.4) implies that all actual future removals

\[
 r_i,r_{i+1},\ldots,r_{i+H-1}                   \tag{2.6}
\]

which exist on the path are distinct and lie in \(X_i\). If a future
removal label were absent from \(X_i\), it would have to be inserted after
time \(i\) and removed within \(H\) steps. If two future removals were
equal, the coordinate would have to be reinserted between them and again
removed within \(H\) steps. Both contradict (2.4).

Away from the terminal collar, define

\[
 \alpha_i=(r_i,r_{i+1},\ldots,r_{i+H-1}),
 \qquad L_i=X_i\setminus\{r_i,\ldots,r_{i+H-1}\}. \tag{2.7}
\]

Then

\[
 \alpha_{i+1}=(\alpha_{i,2},\ldots,\alpha_{i,H},r_{i+H}),
 \qquad
 L_{i+1}=L_i-r_{i+H}+a_i.                        \tag{2.8}
\]

Choose any ordered \(H\)-subset of \([n]\setminus X_0\) as \(\beta_0\),
and put all remaining coordinates into \(R_0\). At edge \(i\), take
\(x=r_{i+H}\). If \(a_i\in R_i\), apply the rotor update (1.6); if
\(a_i=\beta_{i,s}\), apply the promotion (1.7). These cases are
exhaustive. Equations (1.5), (1.8), and (2.8) give the prescribed owner
and lower queue inductively.

#### Proof: terminal completion

Extend the actual removal list by formal labels

\[
 c_0,c_1,\ldots,c_{H-1}                           \tag{2.9}
\]

at edge indices \(s-1,s,\ldots,s+H-2\). For \(0\le d<H\), put

\[
 C_d=
 \bigcap_{i=\max(0,s-1+d-H)}^{s-1}X_i.           \tag{2.9a}
\]

The sets \(C_d\) are nested increasingly, and the displayed owner
interval has at most \(H-d\) transitions. Therefore

\[
 |C_d|\ge r-H+d\ge d+1.                          \tag{2.9b}
\]

Choose greedily distinct \(c_d\in C_d\). A formal label \(c_d\) occurs
in the lower queue, or as the appended \(x\), only at actual owners whose
indices lie in the intersection defining \(C_d\), so it is present there.
It cannot equal an actual removal in the same queue window: after such an
actual removal it is absent at the next owner, which also lies in that
intersection. The \(c_d\)'s are mutually distinct by construction.

Use this extended removal list in (2.7)--(2.8). No dummy owner or dummy
word position is emitted; the \(c_d\)'s only fill the terminal lower
queues. The initial upper queue exists because \(H\le n-r\), and its
recursion is required only on actual edges. This completes the lift and
proves sufficiency. \(\square\)

### Corollary 2.2 (exact literal length)

If the path has \(s\) owners, the useful-prefix word of its bridge-one
lift has exact length

\[
 \boxed{s+2H.}                                    \tag{2.10}
\]

#### Proof

Initialize the first state by its nonempty lower block followed by its
\(2H\) singleton blocks, using \(2H+1\) letters. Every bridge-one update
appends one new lower block. There are \(s-1\) updates. The MTF suffix
identities expose every selected lower and upper flag literally.
\(\square\)

### Lemma 2.3 (which natural PBBS windows a lift preserves)

For every owner having \(q\) following path edges, the selected lower
flag is forced and equals

\[
 \boxed{
 L_q(\omega_i)
 =X_i\setminus\{r_i,\ldots,r_{i+q-1}\}
 =\bigcap_{h=0}^qX_{i+h}.}                       \tag{2.11}
\]

For an owner having \(q\) preceding path edges, if the actual union of
those owners is floor-correct,

\[
 \left|\bigcup_{h=0}^qX_{i-h}\right|=r+q,        \tag{2.12}
\]

then

\[
 \boxed{U_q(\omega_i)=\bigcup_{h=0}^qX_{i-h}.}   \tag{2.13}
\]

Without (2.12), equation (2.13) need not hold.

#### Proof

Equation (2.11) follows from (2.5). Every next removal is an original
coordinate of \(X_i\), while every insertion starts outside \(X_i\).

For (2.13), floor correctness means that the \(q\) most recent removal
labels are distinct and none has been reinserted by time \(i\). Each is
prepended to \(\beta\) by (1.6) or (1.7); because none is reinserted,
none is deleted by a promotion. Hence the first \(q\) cache entries are
precisely those removals in reverse time order. Adjoining them to \(X_i\)
gives the chronological union. If one is reinserted, promotion deletes it
from the cache and the equality can fail. \(\square\)

## 3. The exact nonlocal seam signature

Take the last \(H\) transitions of a left piece, a proposed cross edge,
and the first \(H\) transitions of a right piece. Index them by

\[
 -H,-H+1,\ldots,-1,0,1,\ldots,H,                \tag{3.1}
\]

where edge \(0\) is the splice, and write edge \(u\) as removal \(r_u\),
insertion \(a_u\). Assume each old piece separately satisfies (2.4).

### Theorem 3.1 (weighted age/departure seam test)

The concatenated path satisfies the bridge-one residence condition if and
only if

\[
 \boxed{
 a_s\ne r_t
 \quad\text{for every}\quad
 -H\le s<t\le H,\quad s\le0\le t,
 \quad t-s\le H.}                                \tag{3.2}
\]

Equivalently: the splice removal was not inserted in the preceding
\(H\) edges; the splice insertion is not removed in the following
\(H\) edges; and a label inserted \(u\) edges before the splice and
removed \(v\) edges after it is forbidden exactly when \(u+v\le H\).

#### Proof

Every positive run newly created by concatenation has its insertion on or
before the splice and its removal on or after it. Its residence length is
the edge-index difference \(t-s\). All other insertion/removal pairs lie
inside one old piece. Theorem 2.1 proves the equivalence. \(\square\)

Thus the exact port is an ordered, age-weighted collision signature. A
coarse normalized label tuple which forgets the owner facet cannot certify
that the cross edge is a Johnson edge; an unweighted set intersection
cannot certify \(t-s>H\).

## 4. A separated-star PBBS braid

The seam test has a simple PBBS-realizable sufficient pattern. Let
\(A,B,F\subseteq[n]\) satisfy

\[
 A\cap B=\varnothing,
 \qquad |F|=r-1,
 \qquad F\cap(A\cup B)=\varnothing.              \tag{4.1}
\]

For \(1\le i\le t\), let \(P_i\) be a directed Johnson path piece with
initial and terminal owners

\[
 Y_i=F\cup\{a_i\},\quad a_i\in A,
 \qquad
 X_i=F\cup\{b_i\},\quad b_i\in B.               \tag{4.2}
\]

Assume:

* every positive residence internal to \(P_i\) has length at least
  \(H+1\);
* every insertion label on the last \(H\) edges of \(P_i\) belongs to
  \(A\);
* every removal label on the first \(H\) edges of \(P_i\) belongs to
  \(B\).

If a piece has fewer than \(H\) edges, use all of its edges in the
corresponding condition.

### Theorem 4.1 (separated-star nonlocal braid)

For every ordered pair \((i,j)\), the edge

\[
 X_i=F+b_i\longrightarrow F+a_j=Y_j              \tag{4.3}
\]

is a nonlazy Johnson edge and is legal in the seam test (3.2).
Consequently, for every permutation \(i_1,\ldots,i_t\),

\[
 P_{i_1},P_{i_2},\ldots,P_{i_t}                  \tag{4.4}
\]

concatenate into one bridge-one Johnson walk. If their owner sets are
pairwise disjoint and have total size \(M\), this walk is a path and the
resulting literal useful-prefix word has exact length

\[
 \boxed{M+2H.}                                    \tag{4.5}
\]

#### Proof

Equation (4.3) removes \(b_i\in B\) and inserts \(a_j\in A\), so it is
a nonlazy Johnson edge.

Consider any positive residence of length at most \(H\) in a
concatenation. If it lies inside one old piece, it is excluded by
hypothesis. Otherwise it crosses at least one new seam. Its insertion is
either a seam insertion, or lies within the last \(H\) edges of the piece
containing it; in either case its label lies in \(A\). Its removal is
either a seam removal, or lies within the first \(H\) edges of the piece
containing it; in either case its label lies in \(B\). This remains true
even if a short piece allows the residence to cross several seams. The
equality of the two labels would contradict \(A\cap B=\varnothing\).

Thus every concatenation is long-positive-residence. Theorem 2.1 gives
its bridge-one lift, and Corollary 2.2 gives (4.5). \(\square\)

### PBBS specialization

On a rainbow fixed-core PBBS parity row, write the distinct omitted labels
as

\[
 A=\{a_0,a_1,\ldots\},
 \qquad B=\{b_0,b_1,\ldots\}.                    \tag{4.6}
\]

The audited PBBS recurrence on that row removes a \(b\)-label and inserts
an \(a\)-label. Thus every boundary collar wholly inside the rainbow row
has exactly the separated insertion/removal property in Theorem 4.1. If
several such physical pieces are shadow twins with the same endpoint
facet \(F\), they form a separated-star braid.

This is a genuine PBBS nonlocal family, not an arbitrary Johnson example:
the two alphabets are the two PBBS omitted-label parities and their
disjointness is the rainbow hypothesis. What is not proved is a canonical
PBBS decomposition in which all but \(o(W/H)\) pieces lie in large
shadow-twin groups of this form.

### 4.1 The full two-core atlas is not itself the braid

The preceding positive theorem needs cross-atlas shadow twins. The closed
two-core atlas from one rainbow packet has an exact opposite property.

Let

\[
 \Gamma=(\gamma_0,\ldots,\gamma_{2s})
\]

be a cyclic list of \(2s+1\) distinct labels, and let \(V_i\) be its
cyclic \(s\)-window beginning at \(i\). Let \(K,K'\) be disjoint
\((r-s)\)-sets, disjoint also from \(\Gamma\), and put

\[
 \mathcal A(K,K';\Gamma)
 =\{K\cup V_i: i\in\mathbb Z_{2s+1}\}
  \cup
  \{K'\cup V_i: i\in\mathbb Z_{2s+1}\}.          \tag{4.7}
\]

This is the full two-core window atlas; the physical rainbow packet uses
two particular length-\(s\) arcs of it.

### Proposition 4.2 (exact induced atlas graph)

If

\[
 s\le r-2,                                       \tag{4.8}
\]

then the Johnson graph induced by (4.7) is exactly

\[
 \boxed{C_{2s+1}\ \dot\cup\ C_{2s+1}.}          \tag{4.9}
\]

#### Proof

For two cyclic \(s\)-windows, let \(d\in\{0,1,\ldots,s\}\) be the
smaller circular distance between their starts. Since the ambient circle
has length \(2s+1\), their intersection has size \(s-d\). Hence two
distinct windows overlap in \(s-1\) labels exactly when their starts are
cyclic neighbors. Adding the same core proves that each core class induces
one \(C_{2s+1}\).

Across the two core classes, an intersection has size at most \(s\),
because \(K,K'\), and \(\Gamma\) are pairwise disjoint. Johnson adjacency
of rank-\(r\) owners requires intersection size \(r-1\), and
\(s\le r-2\) excludes it. \(\square\)

### Proposition 4.3 (atlas-confined bridge toll)

Assume (4.8) and \(H\ge s\). Every bridge-one path whose vertices and
arcs are confined to one cycle in (4.9) has at most \(s\) edges and
\(s+1\) owners. Consequently a bridge-one path cover of the full atlas
has at least four paths. For \(g\) owner-disjoint atlases, any
atlas-confined bridge compiler has

\[
 p\ge4g,
 \qquad
 M=2g(2s+1),
 \qquad
 L-M=2Hp\ge8Hg.                                  \tag{4.10}
\]

In particular,

\[
 \frac{L-M}{M}
 \ge\frac{4H}{2s+1}
 \ge\frac{4s}{2s+1}.                             \tag{4.11}
\]

#### Proof

A simple path in an induced cycle follows consecutive cycle edges in one
orientation. In the forward orientation, edge \(i\) inserts
\(\gamma_{i+s}\), and edge \(i+s\) removes the same label. Thus any
subpath with \(s+1\) edges contains a positive residence of length
\(s\le H\), forbidden by Theorem 2.1. The reverse orientation has the
same property. Hence one path has at most \(s+1\) vertices.

Covering \(2s+1\) cycle vertices therefore needs at least
\(\lceil(2s+1)/(s+1)\rceil=2\) paths. There are two components, so four
paths are necessary. Corollary 2.2 gives the remaining identities.
\(\square\)

Thus merely staying inside the two-core atlas has a constant relative
initialization toll when \(H\ge s\). A successful Gaussian braid must use
cross-atlas or cross-core Johnson chords of the kind isolated in Theorem
4.1; the circular two-core internal chart alone is not a \((CP_A)\) path
cover.

For the actual \(2s+2\)-owner rainbow packet, the two physical parity
rows are the two length-\(s\) atlas arcs

\[
 K+V_0,\ldots,K+V_s
 \quad\text{and}\quad
 K'+V_{s+1},\ldots,K'+V_{2s},K'+V_0.             \tag{4.12}
\]

Under (4.8) there is no cross-core Johnson edge, so an atlas-confined
compiler of one physical packet needs at least two paths and pays at least
\(4H\) initialization letters. This lower bound is attained by the two
displayed row paths. For \(g\) packets compiled independently, the
relative initialization excess is at least

\[
 \frac{4Hg}{(2s+2)g}=\frac{2H}{s+1},             \tag{4.13}
\]

which is bounded away from zero when \(s\le H\) and \(s\to\infty\).
Thus even the physical packet rows must be fused across packet atlases at
the Gaussian scale.

## 5. Exact residence-hitting obstruction inside the canonical PBBS factor

Let \(P\) be the directed projected PBBS 2-factor on \(W\) owners. If a
coordinate is inserted on PBBS edge \(e_i\) and next removed on edge
\(e_j\), where

\[
 1\le j-i\le H,                                  \tag{5.0}
\]

put

\[
 I(i,j)=\{e_i,e_{i+1},\ldots,e_j\}.              \tag{5.0a}
\]

Thus the positive residence length is \(j-i\le H\), while its closed
edge interval contains \(j-i+1\le H+1\) edges. Let \(\mathcal I_H\) be
this family of closed intervals, and let

\[
 \nu_H=\max\{|\mathcal A|:\mathcal A\subseteq\mathcal I_H
                    \text{ is edge-disjoint}\}.             \tag{5.1}
\]

Let \(\mathcal F\) be any bridge-one path forest on one full state at
each of the same \(W\) owners. Write \(p\) for its number of paths and
\(c\) for the number of its arcs which are not arcs of \(P\).

### Theorem 5.1 (PBBS residence-hitting inequality)

\[
 \boxed{p+c\ge\nu_H,
 \qquad c\ge\nu_H-p.}                            \tag{5.2}
\]

#### Proof

The forest has \(W-p\) arcs, of which \(c\) are non-PBBS. Hence it
retains exactly \(W-p-c\) PBBS arcs, and the omitted PBBS edge set has
size

\[
 W-(W-p-c)=p+c.                                  \tag{5.3}
\]

If every edge of one interval \(I\in\mathcal I_H\) were retained, the
indegree/outdegree-one condition would force those edges to occur
consecutively on one forest path. That path would contain the short
positive residence represented by \(I\), contradicting Theorem 2.1.
Thus the omitted PBBS edges hit every member of \(\mathcal I_H\). Any
hitting set has at least \(\nu_H\) edges because it must choose a
different edge from each member of an edge-disjoint subfamily. Combine
with (5.3). \(\square\)

This theorem is not a lower bound on \(\nu_H\). It says exactly what a
future PBBS return-packing theorem would force on every \((CP_A)\) braid.

## 6. Top-fibre and promotion budgets

Now specialize to the symmetric middle layer of \([2m]\):

\[
 W=\binom{2m}{m},
 \qquad N_q=\binom{2m}{m-q}.                     \tag{6.1}
\]

For a full state, put

\[
 T(\omega)=X(\omega)\cup\{\beta_1,\ldots,\beta_H\}; \tag{6.2}
\]

this is its top rank-\((m+H)\) flag.

### Lemma 6.1 (top flags force rotor arcs)

Suppose a bridge-one path forest has \(p\) paths and its selected top
flags assume \(D_H\) distinct values. If \(R\) is the number of rotor
arcs, then

\[
 \boxed{R\ge D_H-p.}                             \tag{6.3}
\]

In particular, a covering prefix transversal has \(D_H=N_H\) and
satisfies

\[
 \boxed{R\ge N_H-p.}                             \tag{6.4}
\]

#### Proof

A singleton promotion preserves the full top set: it moves
\(x\in L\) into the singleton list and moves the promoted \(\beta_s\)
into the owner, so (6.2) is unchanged. A rotor arc replaces the final top
singleton by a coordinate from \(R\), and therefore changes the top set.

For each top value \(U\), let \(t_U\) be its number of occurrences and
\(c_U\) the number of path blocks formed by those occurrences. There are
exactly \(t_U-c_U\) promotion arcs inside that fibre. Hence

\[
 R=(W-p)-\sum_U(t_U-c_U)=\sum_Uc_U-p.             \tag{6.5}
\]

Every occupied top value has \(c_U\ge1\), proving (6.3). A covering
transversal uses every one of the \(N_H\) possible top values, so
\(D_H=N_H\). \(\square\)

For \(H=A\sqrt m+o(\sqrt m)\),

\[
 \frac{N_H}{W}
 =\prod_{i=0}^{H-1}\frac{m-i}{m+i+1}
 \longrightarrow e^{-A^2}.                      \tag{6.6}
\]

Thus \((CP_A)\) with \(p=o(W/H)\) necessarily uses
\(\Theta_A(W)\) rotor arcs. A braid made almost entirely of
top-preserving promotions cannot work.

### Lemma 6.2 (which promotions preserve an upper flag)

For \(1\le q\le H\), a position-\(s\) promotion preserves the depth-
\(q\) upper flag if and only if \(s\le q\). Every rotor arc changes it.

#### Proof

Before the update,

\[
 U_q=X\cup\{\beta_1,\ldots,\beta_q\}.            \tag{6.7}
\]

Under a position-\(s\) promotion, the new owner is
\(X-\alpha_1+\beta_s\), and the new cache is (1.7). If \(s\le q\),
the promoted \(\beta_s\) moves into the owner, \(\alpha_1\) moves into
the cache, and the same set (6.7) results. If \(s>q\), the new upper flag
replaces \(\beta_q\) by \(\beta_s\). Under a rotor arc, it replaces
\(\beta_q\) by the newly inserted coordinate from \(R\). \(\square\)

### Theorem 6.3 (upper-flag preservation budget)

Let \(E_{\le q}\) be the number of position-\(s\) promotions with
\(s\le q\) in a bridge-one path forest, let \(D_q\) be the number of
distinct selected depth-\(q\) upper flags, and let \(C_q\) be the total
number of maximal same-\(U_q\) blocks across all paths. Then

\[
 \boxed{E_{\le q}=W-C_q,}
 \qquad
 \boxed{\#\{U_q\text{-changing arcs}\}=C_q-p.}   \tag{6.7a}
\]

Consequently

\[
 \boxed{E_{\le q}\le W-D_q.}                    \tag{6.8}
\]

For a covering transversal, \(D_q=N_q\) and

\[
 \boxed{E_{\le q}\le W-N_q.}                    \tag{6.9}
\]

Combining with Theorem 5.1, at least

\[
 \boxed{
 \bigl(\nu_H-p-(W-N_q)\bigr)_+}                 \tag{6.10}
\]

non-PBBS chords must be rotors or promotions deeper than cache position
\(q\), hence must change the depth-\(q\) upper flag.

#### Proof

By Lemma 6.2, the \(U_q\)-preserving arcs are exactly the promotions at
positions \(s\le q\). A maximal same-value block of \(t\) vertices has
exactly \(t-1\) such arcs. Summing over all blocks gives
\(E_{\le q}=W-C_q\); subtracting from the \(W-p\) total arcs gives the
second identity in (6.7a). Since every occupied target value contributes
at least one block, \(C_q\ge D_q\), proving (6.8). A covering transversal
uses every one of the \(N_q\) possible values, giving (6.9).

Theorem 5.1 gives at least \(\nu_H-p\) non-PBBS chords. At most
\(W-N_q\) arcs in the entire forest can preserve the depth-\(q\) upper
flag. Subtraction proves (6.10). \(\square\)

At depth one,

\[
 W-N_1
 =\binom{2m}{m}-\binom{2m}{m-1}
 =\frac{W}{m+1}.                                 \tag{6.11}
\]

Therefore a PBBS family with \(\nu_H\asymp W/H\),
\(H\asymp\sqrt m\), forces \(\Omega(W/H)\) genuinely
shallow-upper-recoding chords whenever \(p=o(W/H)\). First-cache
promotion is quantitatively insufficient.

## 7. Lower balance is not free after a path cover is chosen

Let the original PBBS cycles be cut at \(J\) edges into whole
chronological pieces, and form a new path forest by permuting only those
pieces. On each piece retain the PBBS owner order. Let
\(\mu_q^{\rm old}(T)\) be the multiplicity of a rank-\((r-q)\) target
as a floor-correct chronological depth-\(q\) lower flag in the old PBBS
cycles, and let \(\mu_q^{\rm new}(T)\) be the selected lower-flag load in
the bridge lift.

### Proposition 7.1 (exact lower-load edit radius)

For every \(q\le H\),

\[
 \boxed{
 \sum_T|\mu_q^{\rm new}(T)-\mu_q^{\rm old}(T)|
 \le2qJ.}                                        \tag{7.1}
\]

#### Proof

Let \(A_q\) be the set of owners whose old \(q\)-edge forward window
meets a cut. Every projected PBBS component has more than \(q\) edges in
the range under consideration, so one cut belongs to exactly \(q\) such
windows and

\[
 |A_q|\le qJ.                                    \tag{7.1a}
\]

If an owner is not in \(A_q\), all \(q\) old PBBS edges remain
consecutive in one new path. Lemma 2.3 forces the same rank-\((r-q)\)
lower flag there, and in particular shows that the old window is
floor-correct. If an owner lies in \(A_q\), its new load contribution is
one basis vector, while its old floor-correct contribution is either one
basis vector or zero. The per-owner \(\ell^1\) change is therefore at
most \(2\), including terminal collars filled by the construction in
Theorem 2.1. Sum over (7.1a). \(\square\)

Let \(\mathcal B_q\) be the set of integer balanced load vectors of total
mass \(W\), with every coordinate equal to

\[
 \left\lfloor\frac{W}{N_q}\right\rfloor
 \quad\text{or}\quad
 \left\lceil\frac{W}{N_q}\right\rceil.          \tag{7.2}
\]

### Corollary 7.2 (necessary balance condition)

If the reordered bridge lift is balanced at depth \(q\), then

\[
 \boxed{
 \operatorname {dist}_{\ell^1}
   (\mu_q^{\rm old},\mathcal B_q)\le2qJ.}         \tag{7.3}
\]

This is not presently a numerical PBBS obstruction: no lower bound of the
required scale is known for the left side. It does prove that balanced
flags cannot be chosen independently after a low-cut piece order has been
fixed. The lower queues are forced. There is no analogous natural-union
formula for every upper flag because promotions are legal; the exact upper
restriction is Theorem 6.3.

## 8. Corrected sandwich/QCF composition and all baseline charges

Partition the \(W\) physical owners into two disjoint classes.

1. **Bridge class.** Its owners are partitioned into Johnson pieces and
   rejoined into \(p\) paths satisfying the seam test (3.2). Let its
   owner count be \(M_{\rm br}\).
2. **Sandwich class.** Its owners lie in pairwise owner-disjoint typed
   fixed-fibre atoms. The substituted sandwich words have total exact
   length
   \[
      M_{\rm sand}+E_{\rm sand},
      \qquad M_{\rm br}+M_{\rm sand}=W.           \tag{8.1}
   \]

Assume the atoms' assigned targets are all internal targets proved by
their sandwich charts. Every original PBBS target through depth \(H\)
which crosses an interface not covered by one of those charts is assigned
to a cluster of physical cuts. If cluster \(j\) has span \(S_j\), assume

\[
 3H+S_j\le r.                                    \tag{8.2}
\]

The corrected dominance/QCF compiler supplies an auxiliary word of length
at most \(7H+3S_j-3\) for that cluster.

### Theorem 8.1 (baseline-relative bridge--sandwich--QCF compiler)

Under the preceding hypotheses there is one nonzero literal contiguous-OR
word covering every middle owner, every target assigned internally to a
bridge piece or sandwich atom, and every declared floor-correct lower and
upper PBBS crossing target through depth \(H\), of total length at most

\[
 \boxed{
 L\le W+2Hp+E_{\rm sand}
       +\sum_j(7H+3S_j-3).}                      \tag{8.3}
\]

#### Proof

The bridge pieces give a literal word of length

\[
 M_{\rm br}+2Hp                                  \tag{8.4}
\]

by Theorem 2.1 and Corollary 2.2. Lemma 2.3 covers every floor-correct
chronological target whose whole owner window remains inside one retained
piece. The sandwich words cost
\(M_{\rm sand}+E_{\rm sand}\) and, by hypothesis, cover their own
owners and assigned targets. The cluster charts restore all declared
crossing targets. Concatenate these already literal words. Equation (8.1)
gives (8.3), and no owner is charged in both baselines. \(\square\)

For the all-phase fixed-fibre sandwich family of the normalized-port
report, the exact excess may be inserted as

\[
 \boxed{
 E_{\rm sand}
 =\sum_q\bigl(N\bar R_q+(q-1)c_q\bigr).}          \tag{8.5}
\]

This substitution is valid only when the owner segments charged to the
different depths are pairwise disjoint globally, and when the same
sandwich word covers the owners whose baseline it replaces. Merely
appending the charts to a separate \(W\)-owner word would add
\(M_{\rm sand}\) a second time and is invalid for coefficient one.

### Corollary 8.2 (nontrivial sufficient class)

Suppose, for \(H=\lceil A\sqrt m\rceil\), the canonical PBBS factor has
a decomposition satisfying Theorem 8.1 such that

\[
 Hp=o_A(W),
 \qquad E_{\rm sand}=o_A(W),
 \qquad \sum_j(H+S_j)=o_A(W).                    \tag{8.6}
\]

Then its complete correct PBBS central band through depth \(H\) has a
literal word of length \(W+o_A(W)\). In particular this holds for a
factor whose residual bridge pieces fall into \(o_A(W/H)\)
separated-star groups and whose sandwich/QCF terms obey (8.6).

This is a real positive factor class. It is not an unconditional theorem
about the canonical PBBS factor: abundance of separated-star shadow twins,
the clustered-span estimate, and balanced/covering lower loads remain
unproved.

## 9. Audit corrections and precise implication scope

1. **Upper chronology.** Promotions make
   \(U_q(\omega_i)=\bigcup_{h=0}^qX_{i-h}\) false in general. This note
   uses it only under the floor-correctness hypothesis (2.12), where it is
   proved in Lemma 2.3.

2. **Finite endpoints.** The sufficiency direction of Theorem 2.1 uses
   the explicit terminal completion (2.9); it does not silently assume a
   bi-infinite path. The exact rank conditions are (2.3).

3. **Identity arcs.** A path cover of distinct middle owners uses no
   identity arc. If occurrence-labelled repeated owners are allowed,
   identity arcs preserve every flag and must be added to the preserving
   side of the budgets in Section 6.

4. **PBBS versus Johnson.** The residence theorem and seam test are
   Johnson statements. The separated-star specialization is PBBS-specific
   only because the PBBS rainbow parity row supplies the disjoint
   insertion/removal alphabets. No claim is made that all canonical PBBS
   pieces share the required endpoint facet.

5. **Hitting versus packing.** Theorem 5.1 uses only
   \(\tau_H\ge\nu_H\). It proves no upper or lower estimate on the actual
   PBBS value \(\nu_H\).

6. **Balanced flags.** Theorem 4.1 selects one integral full flag per
   owner, but it does not prove the simultaneous floor/ceiling load balance
   of Theorem 4.8 in the multi-frame report. Corollary 7.2 is the exact
   necessary lower-load condition which a balance proof must meet.

7. **QCF charge.** The term \(7H+3S_j-3\) is an auxiliary cluster word,
   while the sandwich baseline in (8.5) is substituted. These two kinds
   of charge are not interchanged or counted twice. Paying the one-cut
   \(4H-1\) chart independently at \(\Theta(W/H)\) seams would still cost
   \(\Theta(W)\).

8. **Exact-factor scope.** All PBBS owners, pieces, and substituted atoms
   remain inside one exact factor. Every output described in Section 8 is
   a literal word. No complement is treated as an OR witness and no
   fractional common-owner synchronization is used.

9. **Independent audit corrections.** Two independent audits found and
   corrected three boundary issues before finalization: the finite lift
   needs \(H<r\), the terminal fillers require the nested intersections
   (2.9a) rather than an arbitrary ordering from one terminal
   intersection, and a residence of length \(H\) occupies \(H+1\)
   closed PBBS edges as stated in (5.0a). The audit also supplied the
   terminal-collar-safe proof of (7.1). The seam test, separated-star
   alphabet argument, rotor count, and promotion budget survived
   unchanged.

## 10. Final boundary

The coarse normalized-port obstruction is not the end of the lane. There
is an exact nonlocal braid mechanism: separated PBBS insertion/removal
alphabets over a common endpoint facet fuse arbitrarily many pieces for one
\(2H\) initialization. The exact general seam condition is (3.2).

The mechanism also reveals why the full theorem is difficult. A
coefficient-one \((CP_A)\) solution must simultaneously:

1. hit every short positive PBBS residence by a path end or a non-PBBS
   chord;
2. use \(\Theta_A(W)\) genuine rotor arcs to traverse the top target
   fibres;
3. use many shallow-upper-changing chords if the PBBS short-return packing
   is critical;
4. satisfy the forced lower-load balance inequalities (7.3); and
5. realize its endpoint joins as actual Johnson edges, not merely equal
   normalized singleton ports.

The exact proved positive class is Theorem 4.1 together with the
baseline-relative compiler Theorem 8.1. The exact unresolved PBBS input is
the existence of enough compatible separated/star-shadow endpoint groups,
or a different nonlocal family satisfying the weighted seam test, with

\[
 Hp+E_{\rm sand}+\sum_j(H+S_j)=o_A(W)
\]

and with covering (preferably balanced) forced lower flags. No
coefficient-one conclusion is claimed here.
