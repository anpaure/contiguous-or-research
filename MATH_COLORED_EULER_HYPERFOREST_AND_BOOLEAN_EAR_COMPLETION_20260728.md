# Hyperforest cuts, the degree-two obstruction, and Boolean ear completions

Date: 2026-07-28

Status: unconditional theorem package.  The chronological cuts from
`MATH_COLORED_EULER_AND_LINEAR_DEBRUIJN_CHRONOLOGY_GATE_20260728.md` are
identified exactly with the hypergraphic-matroid relaxation.  That
relaxation does not impose the degree-two/Hamilton-path condition.  On the
positive side, an explicit incidence-cycle ear construction gives one
connected coloured chronology for a large, exactly characterized cone of
coupled hypersimplex excess designs.  It does not synchronize three or more
rows and does not by itself solve the frozen `k=15` chronology.

## 0. Outcome

Let

\[
 {\cal A}=\binom{[k]}s,\qquad
 {\cal R}=\binom{[k]}{s-1}.
\]

There are three distinct levels of the adjacent-row problem.

1.  The inequalities

    \[
      c({\cal C})\le m(N({\cal C}))-1
      \qquad(\varnothing\ne{\cal C}\subseteq{\cal R})                 \tag{0.1}
    \]

    are exactly the hyperforest inequalities.  When their totals are
    `n-1` colours on `n` occurrence clones, they certify a hypergraphic
    spanning tree.
2.  A chronology is not an arbitrary hypertree.  It is a **typed Berge
    Hamilton path**.  In the unit-load case this is exactly the demand that
    the hypertree admit a shrinking of maximum degree two.  A four-vertex
    Boolean star satisfies every inequality (0.1) with equality and still
    has no chronology.
3.  The obstruction is nevertheless avoidable for a broad family of
    designs.  Every cyclic incidence ear

    \[
      Q+p_0p_1, Q+p_1p_2,\ldots,Q+p_{\ell-1}p_0                 \tag{0.2}
    \]

    can be inserted into a lower-complete Johnson path.  Triangle ears
    admit an exact coordinate-marginal characterization.  If `a` ears are
    to be inserted and `u,l` are their desired upper and lower point-degree
    increments, put

    \[
      \delta=u-l,qquad g={2l-u\over3}.                            \tag{0.3}
    \]

    They are realizable whenever these are nonnegative integral vectors,

    \[
      \sum_x\delta_x=3a,\quad
      \sum_xg_x=(s-2)a,\quad
      \delta_x+g_x\le a\quad(x\in[k]).                            \tag{0.4}
    \]

    The proof is one bipartite edge-colouring.  Thus this part of the
    simultaneous hypersimplex lift is not a search problem.

The remaining adjacent-rank issue is sharply localized: choose a
lower-complete base Hamilton path whose colour point degrees put the
desired residual vectors inside the cone (0.3)--(0.4).  The all-depth issue
remains the requirement that the ears at successive ranks arise from one
common chronology.

## 1. The exact typed-hypergraph formulation

Let `m_A,c_R` be nonnegative integers with

\[
 n:=\sum_{A\in{\cal A}}m_A,\qquad
 \sum_{R\in{\cal R}}c_R=n-1.                                    \tag{1.1}
\]

Make `m_A` distinguishable clones of every `A`, and write

\[
 V_m=\{(A,j):A\in{\cal A},\ 1\le j\le m_A\}.                    \tag{1.2}
\]

For every one of the `c_R` copies of colour `R`, make a hyperedge

\[
 H_R=\{(A,j)\in V_m:R\subset A\}.                               \tag{1.3}
\]

A **typed Berge Hamilton path** is an alternating ordering

\[
 v_0,E_1,v_1,E_2,\ldots,E_{n-1},v_{n-1}                         \tag{1.4}
\]

using every clone and every hyperedge copy exactly once, such that
`v_(i-1),v_i in E_i` and the two clones have different underlying
`s`-set types.

### Theorem 1.1 (chronology equals a typed Berge Hamilton path)

There is a Johnson walk with vertex-type multiplicities `m` and
intersection-colour multiplicities `c` if and only if the clone
hypergraph (1.2)--(1.3) has a typed Berge Hamilton path.

#### Proof

Given a Johnson walk, distinguish repeated occurrences of each vertex type
arbitrarily.  Between consecutive occurrences insert a fresh copy of their
intersection colour.  This is (1.4), and Johnson adjacency says that the
two types are different.

Conversely, erase clone indices and hyperedge-copy indices from (1.4).
The two types adjacent to a copy of `R` are distinct `s`-extensions of
`R`; hence their intersection is exactly `R`.  The resulting type word is
the required Johnson walk.  \(\square\)

This is the occurrence-level version of the coloured-Euler theorem.  It
makes clear why an untyped connectivity argument cannot be the final step.

## 2. Chronological cuts are exactly the hyperforest relaxation

For \(C\subseteq{\cal R}\), put

\[
 c(C)=\sum_{R\in C}c_R,qquad
 m(N(C))=\sum_{A:\,R\subset A\text{ for some }R\in C}m_A.       \tag{2.1}
\]

Recall the hypergraphic-matroid shrinking theorem: a family `F` of
hyperedges can be shrunk, one hyperedge to one ordinary edge joining two of
its vertices, so that the resulting graph is a forest if and only if

\[
 |F'|\le |\bigcup F'|-1
 \qquad(\varnothing\ne F'\subseteq F).                           \tag{2.2}
\]

### Theorem 2.1 (exact hyperforest equivalence)

For the clone hypergraph (1.2)--(1.3), condition (2.2) is equivalent to

\[
 \boxed{c(C)\le m(N(C))-1
 \quad(\varnothing\ne C\subseteq{\cal R}).}                     \tag{2.3}
\]

Under (1.1), these inequalities say exactly that all colour copies form a
basis of the hypergraphic matroid, and hence can be shrunk to a spanning
tree on the `n` clones.

#### Proof

For a nonempty subfamily `F'`, let `C` be the set of colour types appearing
in it.  Its vertex union has size exactly `m(N(C))`, while

\[
 |F'|\le\sum_{R\in C}c_R=c(C).
\]

Thus (2.3) implies (2.2).  Conversely take `F'` to contain all copies of
every colour in `C`; then (2.2) is (2.3).

There are `n-1` hyperedges and `n` clones.  A forest shrinking therefore
has `n-1` edges on `n` vertices and is a spanning tree.  \(\square\)

Thus the cut (3.1) in the preceding coloured-Euler note is not merely
analogous to a hyperforest cut: it is exactly one.  Hypergraphic-matroid or
polymatroid intersection can settle this relaxation, but not the next one.

## 3. The missing condition is degree two, not connectivity

When every positive type has unit load, a typed Berge Hamilton path is a
shrinking of the hypergraphic basis to a spanning tree of maximum degree at
most two.  Such a tree is a Hamilton path.  Maximum degree two is not a
matroidal condition.

### Proposition 3.1 (Boolean star obstruction)

Assume `s>=3` and `k>=s+3`.  There are unit vertex loads and unit colour
loads in the two consecutive Boolean layers which satisfy every
hyperforest inequality (2.3) with equality on their support but admit no
chronology.

#### Proof

Choose

\[
 A_0=\{a_1,\ldots,a_s\},qquad
 R_i=A_0\setminus\{a_i\}\quad(i=1,2,3),                          \tag{3.1}
\]

and distinct `x_1,x_2,x_3 outside A_0`.  Put

\[
 A_i=R_i\cup\{x_i\}\quad(i=1,2,3).                              \tag{3.2}
\]

Give load one to `A_0,A_1,A_2,A_3`, load zero to all other `s`-sets, and
one copy to each `R_1,R_2,R_3`.  Inside the positive support, the
neighbourhood of `R_i` is exactly `{A_0,A_i}`.  A family of `t` colours
therefore has `t+1` neighbours, so (2.3) holds with equality.

Every shrinking is nevertheless the three-edge star centred at `A_0`.
It has degree three and cannot be a path.  Equivalently, deleting `A_0`
from the clone incidence graph leaves three components, whereas deleting
one vertex from a Hamilton path can leave at most two.  \(\square\)

More generally, the clone incidence graph `G(m,c)` obeys the necessary
toughness inequalities

\[
 \operatorname{cc}(G(m,c)-Z)\le |Z|+1                            \tag{3.3}
\]

for every set of occurrence clones `Z` whenever a chronology exists.
They detect degree-two bottlenecks which (2.3) cannot see.  They are still
not sufficient in general: the residual problem contains Hamilton path as
a special case.

## 4. Lower-complete base paths

Put

\[
 N_s=\binom ks,qquad N_{s-1}=\binom k{s-1}.                     \tag{4.1}
\]

Assume \(N_s>N_{s-1}\), equivalently \(s<(k+1)/2\).  The tight-enumeration
theorem for two consecutive Boolean levels projects to a Hamilton cycle of
\(J(k,s)\) whose intersection colours cover all of \({\cal R}\).  Since the
cycle has \(N_s\) edges but only \(N_{s-1}\) colours, some colour is repeated.
Cut an edge carrying a repeated colour.

### Lemma 4.1 (lower-complete Hamilton base)

If `s<(k+1)/2`, there is a Hamilton path

\[
 P_0=(A_0,A_1,\ldots,A_{N_s-1})                                 \tag{4.2}
\]

through \({\cal A}\) whose \(N_s-1\) adjacent intersections cover every
member of \({\cal R}\).

If \(N_s=N_{s-1}\), the same projection gives a Hamilton path missing exactly
one lower colour; this is the unavoidable one-boundary flag.

The next construction preserves the endpoints of `P_0`.

### Theorem 4.2 (saturating-cycle orientation theorem)

Suppose an alternating saturating cycle between the two ranks is written

\[
 R_0,B_0,R_1,B_1,\ldots,R_{M-1},B_{M-1},R_0,                   \tag{4.3}
\]

where \(M=N_{s-1}\), the \(R_i\) enumerate \({\cal R}\), the \(B_i\)
are distinct members of \({\cal A}\), and

\[
                         R_i,R_{i+1}\subset B_i.                \tag{4.4}
\]

Let

\[
 {\cal L}={\cal A}\setminus\{B_0,\ldots,B_{M-1}\},\qquad
 D=|{\cal L}|=N_s-N_{s-1}.                                     \tag{4.5}
\]

For every map

\[
 \phi:{\cal L}\longrightarrow[k],\qquad \phi(X)\in X,           \tag{4.6}
\]

there is a Hamilton cycle of \(J(k,s)\) with complete lower-colour
support and lower load

\[
 c_R=1+\#\{X\in{\cal L}:X\setminus\{\phi(X)\}=R\}.               \tag{4.7}
\]

If \(d_x=\sum_{R\ni x}(c_R-1)\) is the point-degree vector of the
lower excess and

\[
 q_x=\#\{X\in{\cal L}:\phi(X)=x\},
\]

then exactly

\[
                         d_x=\deg_{\cal L}(x)-q_x.               \tag{4.8}
\]

#### Proof

For each \(R_i\), form a block beginning at \(B_{i-1}\), followed in any
order by all \(X\in{\cal L}\) with
\(X\setminus\{\phi(X)\}=R_i\), and ending at \(B_i\).  Every member of
this block is an \(s\)-extension of \(R_i\), so consecutive distinct
members are Johnson-adjacent with intersection exactly \(R_i\).
Concatenating the cyclic blocks identifies their common boundary vertices
and uses every member of \({\cal A}\) once.  The block has one more edge
than assigned internal vertices, proving (4.7).  Each assigned \(X\)
contributes to the excess degree at every coordinate of \(X\) except its
deleted coordinate \(\phi(X)\), which proves (4.8).  \(\square\)

Thus the point-marginal choice inside this construction is one ordinary
flow, not a Hamilton problem.

### Corollary 4.3 (exact deletion-quota flow)

Fix a desired lower-excess point-degree vector
\(d\in{\mathbb Z}_{\ge0}^k\) of total \((s-1)D\), and put

\[
                         q_x=\deg_{\cal L}(x)-d_x.               \tag{4.9}
\]

There is a map (4.6), and hence one lower-complete Hamilton cycle with
excess point degrees \(d\), if and only if \(q_x\ge0\),
\(\sum_xq_x=D\), and for every \(Y\subseteq[k]\),

\[
 \boxed{\quad
 q(Y)\le
 |\{X\in{\cal L}:X\cap Y\ne\varnothing\}|.
 \quad}                                                         \tag{4.10}
\]

Equivalently, the complementary inequalities are

\[
 q(Y)\ge|\{X\in{\cal L}:X\subseteq Y\}|
 \qquad(Y\subseteq[k]).                                         \tag{4.11}
\]

#### Proof

Use the bipartite graph joining \(X\in{\cal L}\) to its coordinates.
Every left vertex has demand one and coordinate \(x\) has demand \(q_x\).
The capacitated Hall theorem gives (4.10) and integrality.  Replacing \(Y\)
by its complement and using \(\sum_xq_x=D\) gives (4.11).  Theorem 4.2
then supplies the chronology.  \(\square\)

For later use, the unused-family degree has a direct run interpretation.
If \(b_x\) is the number of cyclic \(x\)-runs in the lower word
\((R_i)\), then

\[
 \deg_{\cal L}(x)
 =\binom{k-1}{s-1}-\binom{k-1}{s-2}-b_x.                         \tag{4.12}
\]

Indeed, among the boundary sets \(B_i=R_i\cup R_{i+1}\), coordinate \(x\)
occurs on every internal edge of an \(x\)-run and on its two boundary
edges, for a total of
\(\binom{k-1}{s-2}+b_x\).

## 5. Incidence-cycle ears

Choose

\[
 Q\in\binom{[k]}{s-2},qquad
 P=\{p_0,\ldots,p_{\ell-1}\}\subseteq[k]\setminus Q,qquad
 \ell\ge3,                                                       \tag{5.1}
\]

with the displayed cyclic order on `P`.  Define

\[
 A_i=Q\cup\{p_i,p_{i+1}\},qquad
 R_i=Q\cup\{p_{i+1}\},                                         \tag{5.2}
\]

with indices modulo `ell`.  Then

\[
 A_0,R_0,A_1,R_1,\ldots,A_{\ell-1},R_{\ell-1},A_0              \tag{5.3}
\]

is a simple alternating cycle in the inclusion graph of ranks `s-1,s`.

At the occurrence of `A_0` in (4.2), traverse (5.3) once and then continue
along the old path.  On the Johnson projection this replaces `A_0` by

\[
 A_0,A_1,\ldots,A_{\ell-1},A_0                                  \tag{5.4}
\]

and therefore adds exactly `ell` upper occurrences and `ell` lower-colour
occurrences.  Multiple ears, including ears with the same anchor, can be
nested at that occurrence.

### Theorem 5.1 (Boolean ear completion)

Let `P_0` be the lower-complete path of Lemma 4.1.  For any finite family
of pairs `(Q_j,P_j)` as in (5.1), inserting their incidence cycles produces
one connected Johnson chronology.  Its added upper multiset and lower
colour multiset are

\[
 {\cal U}_{\rm ear}
 =\biguplus_j\{Q_j\cup\{p_{j,i},p_{j,i+1}\}:i\in\mathbb Z_{\ell_j}\},
                                                                    \tag{5.5}
\]

\[
 {\cal L}_{\rm ear}
 =\biguplus_j\{Q_j\cup\{p_{j,i}\}:i\in\mathbb Z_{\ell_j}\}.       \tag{5.6}
\]

It has the same two endpoints as `P_0`, and remains hole-free on both
consecutive layers.

For every coordinate `x`, one ear of length `ell` contributes

\[
 \deg_{\cal U}(x)=\ell\,\mathbf1_{x\in Q}+2\,\mathbf1_{x\in P},
 \qquad
 \deg_{\cal L}(x)=\ell\,\mathbf1_{x\in Q}+\mathbf1_{x\in P}.      \tag{5.7}
\]

#### Proof

Distinct consecutive sets in (5.4) meet in the stated `R_i`, including
the closing pair.  The second copy of `A_0` then uses the untouched old
successor edge.  Hence the resulting word is one Johnson path, and the
multisets added are exactly (5.5)--(5.6).  The base path already covers
both layers, so insertions cannot create a hole.  Formula (5.7) follows by
counting: a core coordinate is in all `ell` sets on both shores, whereas a
member of `P` occurs twice above and once below.  \(\square\)

### Corollary 5.2 (all sufficiently large lengths)

If `k-s+2>=5`, then for every `t=0` or `t>=3` there is a lower-complete
Johnson walk with exactly `N_s+t` upper occurrences and `N_s+t-1` lower
occurrences.  If `k-s+2=4`, the same holds for

\[
 t\in\langle3,4\rangle=\{0,3,4,6,7,8,\ldots\}.                  \tag{5.8}
\]

#### Proof

An ear may have any length between three and `k-s+2`.  Lengths three,
four, and five generate every integer at least three; lengths three and
four generate the semigroup in (5.8).  \(\square\)

Thus, once only total multiplicity and coverage are specified, adjacent
Boolean chronology has no asymptotic obstruction.  The obstruction lies
in prescribed marginals or in synchronizing several ranks.

## 6. Exact coupled hypersimplex theorem for triangle ears

The following elementary decomposition is the main positive theorem.

### Lemma 6.1 (two-colour hypersimplex coupling)

Let `a,p,q,k` be nonnegative integers.  For vectors
\(\delta,g\in{\mathbb Z}_{\ge0}^k\), there exist labelled pairs

\[
 (P_j,Q_j)\quad(1\le j\le a),qquad
 |P_j|=p,\quad |Q_j|=q,\quad P_j\cap Q_j=\varnothing,             \tag{6.1}
\]

with point-degree vectors `delta` and `g`, respectively, if and only if

\[
 \sum_x\delta_x=pa,qquad
 \sum_xg_x=qa,qquad
 \delta_x+g_x\le a\quad(x\in[k]).                               \tag{6.2}
\]

#### Proof

Necessity is immediate.  For sufficiency, make `p` red socket vertices and
`q` blue socket vertices.  Distribute `delta_x` parallel red edges from
coordinate `x` among the red sockets so that every red socket has degree
`a`; this is possible because the total is `pa`.  Do the same with the
`g_x` blue edges.  The resulting bipartite multigraph has degree `a` at
every socket and degree `delta_x+g_x<=a` at coordinate `x`.

By Konig's line-colouring theorem it has a proper edge-colouring with `a`
colours.  Every colour occurs exactly once at every socket, because each
socket has degree `a`.  For colour `j`, let `P_j` be the coordinates on
its red edges and `Q_j` those on its blue edges.  Properness makes all these
coordinates distinct, proving (6.1).  \(\square\)

This is a simultaneous integer decomposition of two uniform-matroid base
polytopes with a per-packet disjointness constraint.  It is stronger than
performing the two hypersimplex decompositions separately.

### Theorem 6.2 (coordinate criterion for triangle-ear chronology)

Fix \(a\ge0\), and let \(u,l\in{\mathbb Z}_{\ge0}^k\) be desired point-degree increments
on the rank-`s` and rank-`s-1` shores of `3a` added occurrences.  Put

\[
 \delta=u-l,qquad g={2l-u\over3}.                               \tag{6.3}
\]

If `delta,g` are nonnegative integral vectors satisfying

\[
 \sum_x\delta_x=3a,qquad
 \sum_xg_x=(s-2)a,qquad
 \delta_x+g_x\le a\quad(x\in[k]),                              \tag{6.4}
\]

then there is an explicit family of `a` triangle ears whose added upper
and lower point-degree vectors are exactly `u` and `l`.  Inserting them in
`P_0` gives one connected lower-complete chronology with those marginals.

Conversely every family of `a` triangle ears satisfies (6.3)--(6.4).

#### Proof

Apply Lemma 6.1 with `p=3,q=s-2` to obtain disjoint triples `P_j` and cores
`Q_j` having degree vectors `delta,g`.  Give each triple either cyclic
orientation.  By (5.7), the resulting ear family has lower point degrees

\[
 \delta+3g=l
\]

and upper point degrees

\[
 2\delta+3g=u.
\]

Theorem 5.1 inserts all ears into one chronology.  The converse follows
from the same two identities and the disjointness of every `(P_j,Q_j)`.
\(\square\)

This is a genuine positive lift theorem: on the cone (6.3)--(6.4), the
hypersimplex designs, the hyperforest cuts, the degree-two requirement, and
connectivity are all solved simultaneously.

### Corollary 6.3 (mixed-ear residue correction)

Let \(u,l\) be the desired point-degree increments for \(t\) added
occurrences.  First choose any finite family of exceptional ears
\((Q_j,P_j)\) of lengths \(\ell_j\ge4\), and let \(u^E,l^E\) be their
contributions from (5.7).  If

\[
 t-\sum_j\ell_j=3a\ge0                                           \tag{6.5}
\]

and the residual vectors

\[
 u'=u-u^E,\qquad l'=l-l^E                                      \tag{6.6}
\]

satisfy Theorem 6.2 with \(a\) triangle ears, then the exceptional ears
together with those triangle ears realize \(u,l\) in one chronology.

For divisibility, the useful identity is

\[
 2l^E-u^E=\sum_j\ell_j\,\mathbf1_{Q_j}.                         \tag{6.7}
\]

Thus exceptional core sets alone control the coordinate residues of
\(2l-u\) modulo three; the cyclic sets \(P_j\) may then be selected
disjointly from their cores while using the wide nonnegativity slack.

#### Proof

Subtract the exceptional contributions and apply Theorem 6.2 to
\(u',l'\).  Inserting all ears in the same lower-complete base path is
legal by Theorem 5.1.  Formula (6.7) is (5.7) with
\(2(\ell\mathbf1_Q+\mathbf1_P)
-(\ell\mathbf1_Q+2\mathbf1_P)=\ell\mathbf1_Q\).  \(\square\)

### Corollary 6.4 (cyclically balanced bulk)

Suppose a cyclic coordinate permutation has a full orbit on a disjoint
pair `(|P|,|Q|)=(3,s-2)`.  Insert the `k` translated triangle ears.  They
add `3k` occurrences, and every coordinate receives exactly

\[
 \Delta\deg_{\cal U}=3s,qquad
 \Delta\deg_{\cal L}=3(s-1).                   \tag{6.8}
\]

Repeating `b` full orbits gives a perfectly point-regular chronology bulk
of size `3bk`.  For prime `k`, every nontrivial coordinate orbit is full.

#### Proof

Across all translates, a coordinate belongs to three translated triples
and to `s-2` translated cores.  Substitute in (5.7).  \(\square\)

Hence a large nearly regular excess can be installed in a single
chronology, leaving only `O(k)` occurrences outside full cyclic ear orbits.

## 7. `k=15` calibration: the residual scalar target

This section is a calibration, not an existence proof.  For the frozen
Hall-29 `k=15` carrier, the separately completed rank-six and rank-five
excess point degrees from the hypersimplex note are

\[
 u=(568,570,574,572,574,568,572,572,574,572,568,572,569,569,574),
                                                                    \tag{7.1}
\]

\[
 \gamma_3=(1138,1141,1147,1144,1147,1138,1144,1144,1147,1145,
            1138,1145,1140,1140,1147).                            \tag{7.2}
\]

There are `a=1428/3=476` triangle ears available after a Hamilton base on
all `binom(15,6)=5005` rank-six sets.  Let `h_x` be the point degree of the
`5004` rank-five colours on that base path.  The lower ear increment is

\[
 l_x=\binom{14}{4}+\gamma_{3,x}-h_x
     =1001+\gamma_{3,x}-h_x.                                    \tag{7.3}
\]

Theorem 6.2 reduces ear completion to fifteen scalar conditions on `h`:

\[
 \delta_x=h_x+u_x-1001-\gamma_{3,x}\ge0,                         \tag{7.4}
\]

\[
 g_x={2(1001+\gamma_{3,x}-h_x)-u_x\over3}\in\mathbb Z_{\ge0},   \tag{7.5}
\]

\[
 \delta_x+g_x\le476,qquad
 \sum_xh_x=5\cdot5004=25020.                                   \tag{7.6}
\]

These scalar constraints have enormous room.  One explicit admissible
vector is

\[
 h=(1666,1665,1669,1667,1669,1669,1667,1667,1669,1668,
       1669,1668,1669,1669,1669).                                \tag{7.7}
\]

For it, the values of `delta_x+g_x` lie between `221` and `223`, less than
half the cap `476`.

Therefore the frozen adjacent pair would be solved by the following much
smaller object:

> a lower-complete Hamilton path through the rank-six layer whose
> rank-five intersection-colour point-degree vector is (7.7).

No existence of that base path is asserted here.  The reduction is useful
because it replaces the full pair of rankwise excess designs and their
coloured-Euler flow by one balanced 15-coordinate statistic of a standard
lower-complete Hamilton path.  A projected-flow or SAT computation may
calibrate this finite statement, but it is not used in the proof above.

### 7.1 Mixed ears reduce the target to perfect point balance

Corollary 6.3 improves (7.7).  Take instead

\[
                         h_x=1668\qquad(x\in[15]).                \tag{7.8}
\]

This has the required sum \(15\cdot1668=25020\).  With (7.1)--(7.3),
the residue vector of \(2l-u\) modulo three is

\[
 (2,0,2,1,2,2,1,1,2,0,2,0,2,2,2).                              \tag{7.9}
\]

Choose two length-four and two length-five ears with cores

\[
\begin{aligned}
 Q_1&=\{1,3,13,14\},&Q_2&=\{6,7,13,14\},\\
 Q_3&=\{0,1,2,4\},&Q_4&=\{5,8,10,12\},
\end{aligned}                                                    \tag{7.10}
\]

and cyclic sets, respectively,

\[
\begin{aligned}
 P_1&=\{0,2,4,5\},&P_2&=\{0,1,2,3\},\\
 P_3&=\{3,5,6,7,8\},&P_4&=\{0,1,2,3,4\}.
\end{aligned}                                                    \tag{7.11}
\]

Every \(P_i\) is disjoint from \(Q_i\).  The weighted core sum

\[
 4\mathbf1_{Q_1}+4\mathbf1_{Q_2}
 +5\mathbf1_{Q_3}+5\mathbf1_{Q_4}                              \tag{7.12}
\]

has residue (7.9) modulo three.  After removing these 18 occurrences,
there remain \(1410=3\cdot470\) occurrences for triangle ears.  Their
vectors in Theorem 6.2 are

\[
 \delta=(94,94,91,92,92,95,94,94,93,94,97,94,96,96,94),        \tag{7.13}
\]

\[
 g=(123,123,127,126,127,123,126,126,127,128,123,128,124,123,126).
                                                                    \tag{7.14}
\]

They have sums \(1410=3\cdot470\) and \(1880=4\cdot470\), and

\[
                    217\le\delta_x+g_x\le222<470.               \tag{7.15}
\]

Hence Lemma 6.1 constructs the remaining 470 disjoint
triple/core packets, and Theorem 5.1 inserts all 474 ears in one path.
Consequently the frozen rank-six/rank-five marginal pair would be solved
by the especially symmetric base theorem:

> There is a lower-complete Hamilton path through
> \(\binom{[15]}6\) whose 5004 rank-five intersection colours have point
> degree exactly 1668 at every coordinate.

Again this balanced-base theorem is not proved here.  It is, however,
strictly cleaner than prescribing (7.7), and its target is invariant under
the full coordinate group.

### 7.2 The balanced base is one saturating-cycle flow

Theorem 4.2 reduces the remaining balanced-base theorem further.  Take any
saturating cycle (4.3) between ranks five and six, let \({\cal L}\) be its
2002 unused six-sets, and let \(b_x\) be the cyclic run counts of coordinate
\(x\) in its rank-five word.  Formula (4.12) becomes

\[
                         \deg_{\cal L}(x)=1001-b_x.              \tag{7.16}
\]

Choose a five-set \(R_*\).  To make the Hamilton-cycle lower-excess degree

\[
                         d_x=667+\mathbf1_{x\in R_*},            \tag{7.17}
\]

the deletion quotas in Corollary 4.3 are exactly

\[
                         q_x=334-b_x-\mathbf1_{x\in R_*}.        \tag{7.18}
\]

They automatically sum to 2002, because every edge of the rank-five
Hamilton cycle creates one new coordinate run and hence
\(\sum_xb_x=3003\).

Consequently, if \(q_x\ge0\) and the Hall inequalities

\[
 q(Y)\le|\{X\in{\cal L}:X\cap Y\ne\varnothing\}|
 \qquad(Y\subseteq[15])                                         \tag{7.19}
\]

hold, Theorem 4.2 constructs a lower-complete Hamilton cycle through all
six-sets whose lower-colour point degrees are

\[
                         1668+\mathbf1_{R_*}.                    \tag{7.20}
\]

The colour \(R_*\) occurs on that cycle.  Cutting one of its occurrences
therefore gives the perfectly balanced base path (7.8), after which the
mixed-ear construction closes the frozen rank-six/rank-five marginal pair.

This is an exact sufficient theorem, not a claim that an arbitrary or the
canonical GMM saturating cycle satisfies (7.18)--(7.19).  It reduces that
finite search to:

1. compute the 15 run counts and the 2002-set unused family of one
   saturating cycle;
2. try the 3003 possible \(R_*\); and
3. run one bipartite max flow.

No coloured-Euler subtour constraints remain after this test, because the
block chronology is constructed explicitly.

### 7.3 Balanced saturating runs make every deletion Hall cut automatic

The preceding flow has a purely local sufficient hypothesis.  Suppose the
rank-five word of the saturating cycle has perfectly balanced coordinate
run counts:

\[
 b_x\in\{200,201\},\qquad
 |\{x:b_x=201\}|=3.                                             \tag{7.21}
\]

This is the only possible floor/ceiling balance because
\(\sum_xb_x=3003\).  For any five-set \(R_*\), (7.18) then gives

\[
                         132\le q_x\le134.                       \tag{7.22}
\]

### Theorem 7.1 (balanced-run Hall theorem for ranks five and six)

Under (7.21), the deletion quotas (7.18) satisfy every Hall inequality
(7.19), for every choice of \(R_*\).  Consequently the saturating-cycle
orientation theorem constructs the perfectly balanced base path (7.8).

#### Proof

Use the equivalent contained-set inequalities (4.11):

\[
 q(Y)\ge |\{X\in{\cal L}:X\subseteq Y\}|.                        \tag{7.23}
\]

Put \(t=|Y|\).  If \(t\le5\), the right side is zero.  For
\(6\le t\le12\), (7.22) and the trivial complete-layer bound give

\[
 q(Y)\ge132t\ge\binom t6
 \ge|\{X\in{\cal L}:X\subseteq Y\}|;                             \tag{7.24}
\]

the seven numerical comparisons at \(t=6,\ldots,12\) are respectively

\[
 792\ge1,\ 924\ge7,\ 1056\ge28,\ 1188\ge84,\ 1320\ge210,\
 1452\ge462,\ 1584\ge924.
\]

If \(t=13\), then

\[
 q(Y)\ge2002-2\cdot134=1734>\binom{13}6=1716.                   \tag{7.25}
\]

If \(t=14\), let \(x\) be the excluded coordinate.  From
\(\deg_{\cal L}(x)=d_x+q_x\ge667+132=799\),

\[
 |\{X\in{\cal L}:X\subseteq Y\}|
 =2002-\deg_{\cal L}(x)\le1203,                                 \tag{7.26}
\]

whereas \(q(Y)=2002-q_x\ge1868\).  For \(t=15\), both sides of
(7.23) equal 2002.  These cases exhaust all \(Y\).  Corollary 4.3,
Theorem 4.2, and the cut at colour \(R_*\) now give (7.8).  \(\square\)

Combining Theorem 7.1 with the mixed-ear calculation proves the following
conditional statement with no hidden flow or integrality clause:

> If there exists a saturating cycle between ranks five and six of
> \(B_{15}\) whose rank-five coordinate run counts are floor/ceiling
> balanced, then the frozen Hall-29 rank-six/rank-five marginal pair has
> one common lower-complete chronology.

The literature theorem supplies a saturating cycle, but does not state
(7.21).  The remaining object is therefore a transition-balanced
saturating cycle.  This is substantially narrower than a prescribed
coloured Hamilton cycle.

## 8. Consequences for the general route

1. **Do not ask matroid intersection to produce the chronology.**  It can
   certify the hyperforest basis (2.3), but the star in Proposition 3.1
   shows that degree two is an independent obstruction.
2. **Choose the excess designs from chronology-realizable atoms.**  The
   triangle-ear cone (6.3)--(6.4) is an explicit such family, and its
   simultaneous decomposition is polynomial-time constructive.
3. **Separate bulk from boundary.**  Corollary 6.4 installs a regular bulk
   in packets of `3k`; only an `O(k)` remainder needs exceptional ears or a
   boundary collar.
4. **The next positive theorem is balanced-base Hamiltonicity.**  It is
   enough to construct a lower-complete Hamilton path whose coordinate
   colour degrees lie in the broad residue intervals forced by (6.3)--(6.4).
   This is much weaker than prescribing every colour multiplicity.
5. **All-depth synchronization is still real.**  Ears chosen independently
   at consecutive ranks need not be projections of one safe middle word.
   The common decorated de Bruijn flow remains the final compatibility
   condition.
