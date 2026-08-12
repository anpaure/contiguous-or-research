# Lane K: a growing common-core crown cannot support a nontrivial coordinated long cycle

Date: 2026-07-26

Method: pure mathematics only. No enumeration, solver, script, or web input is used.

## 0. Outcome

Work in the two-perfect-matching/middle-levels path-factor normal form on

\[
 \mathcal X=\binom{[2r]}r,
 \qquad
 \mathcal Y=\binom{[2r]}{r+1}.
\]

This report closes a natural genuinely growing alternating-cycle architecture.
At one phase, take a common \((r-2)\)-set \(K\) and pairwise disjoint
two-blocks

\[
 E_1,\ldots,E_k\subseteq[2r]\setminus K,
 \qquad |E_i|=2,
 \qquad
 B_i=K\cup E_i.                                      \tag{0.1}
\]

The number of rows may grow linearly:

\[
 k\le \left\lfloor\frac{r+2}{2}\right\rfloor.       \tag{0.2}
\]

Permute the middle states by an arbitrary \(\pi\in\operatorname{Sym}(k)\),
leaving the two neighbouring phases and every other state fixed. Assume all
new Johnson adjacencies are legal. Then the complete adjacent-union ledger is
preserved if and only if

\[
                         \boxed{\pi^2=\mathrm{id}.}     \tag{0.3}
\]

Thus every legal move in this architecture is a disjoint product of fixed
rows and two-row octahedral rectangles. In particular, no permutation cycle
of length at least three, even one whose length tends to infinity with \(r\),
can be coordinated in the two incidence matchings while preserving the
\(Y\)-saturation ledger. The obstruction occurs before acyclicity or endpoint
monodromy can fail.

Consequently this architecture cannot furnish the requested growing cycle
which transports a middle segment through different peak-erased Motzkin owner
classes. Any owner transfer that survives here has support two and is already
an elementary rectangle effect.

The proof does **not** exclude long cycles whose active two-blocks overlap,
multi-phase systems whose two boundary discrepancies cancel across different
color palettes, or moves which leave the common-core crown normal form.

## 1. Anchored path-factor setup

Let an anchored path factor contain distinct rooted paths, indexed here by
\(i\in[k]\). Around one fixed internal phase write their three-state slabs as

\[
                         A_i,\ B_i,\ C_i.              \tag{1.1}
\]

Thus \(A_i\sim_JB_i\sim_JC_i\). Because the complete path is a length-\(r\)
geodesic between complementary endpoints, two consecutive exchanges cannot
undo one another, and hence

\[
                         d_J(A_i,C_i)=2.                \tag{1.2}
\]

Assume (0.1), with the \(E_i\) pairwise disjoint. For a permutation \(\pi\),
make the proposed replacement

\[
 A_i,B_i,C_i
 \quad\longmapsto\quad
 A_i,B'_i,C_i,
 \qquad B'_i=K\cup E_{\pi(i)}.                         \tag{1.3}
\]

All other states in every row are unchanged. The \(X\)-ledger is automatic:
the middle states have merely been permuted. The rooted endpoints are
unchanged row by row, so the complement endpoint monodromy is the identity.
If all four adjacencies in each changed row are Johnson edges, every new row
still has length \(r\) between endpoints at distance \(r\); it is therefore a
geodesic. Thus the new union of the two incidence matchings is acyclic with
the same fixed \(\mathcal D_r\)-ports once and only once the \(Y\)-ledger is
also exact.

The issue is therefore precisely the two changed adjacent-union colors per
row.

## 2. Local cross-pair rigidity

### Lemma 2.1 (opposite cross-pairs)

Let \(E_i=\{a,b\}\) and \(E_j=\{c,d\}\) be disjoint. The common Johnson
neighbours of

\[
 K\cup E_i,\qquad K\cup E_j
\]

are exactly

\[
 Kac,\quad Kad,\quad Kbc,\quad Kbd.                   \tag{2.1}
\]

If two such common neighbours are the outer states of a two-edge geodesic,
then they are an opposite pair in (2.1): after interchanging \(c,d\) if
necessary, they are

\[
                         Kac,\qquad Kbd.                \tag{2.2}
\]

#### Proof

A common neighbour must retain all \(r-2\) elements of \(K\), one element of
\(E_i\), and one element of \(E_j\), giving (2.1). Two cross-pairs sharing an
active coordinate have Johnson distance one. Two opposite cross-pairs have
Johnson distance two. Equation (1.2) therefore forces the latter case.
\(\square\)

Apply the lemma with \(j=\pi(i)\). For every moved row, the unordered pair of
old colors is independent of which opposite orientation occurs:

\[
 \boxed{
 \{A_i\cup B_i,\ B_i\cup C_i\}
 =\{K\cup E_i\cup\{x\}:x\in E_{\pi(i)}\}.}           \tag{2.3}
\]

Likewise the new pair is

\[
 \boxed{
 \{A_i\cup B'_i,\ B'_i\cup C_i\}
 =\{K\cup E_{\pi(i)}\cup\{x\}:x\in E_i\}.}         \tag{2.4}
\]

Thus the old colors have the type

\[
       \text{double block }i\ \longrightarrow\
       \text{singleton block }\pi(i),                 \tag{2.5}
\]

whereas the new colors have the reverse type.

Equivalently, on the affected color palette define the integral projection

\[
 \Psi_K\bigl(e_{K\cup E_i\cup\{x\}}\bigr)=e_{ij}
 \quad\text{when }x\in E_j.                           \tag{2.6}
\]

Pairwise disjointness makes \(\Psi_K\) well defined. Equations (2.3)--(2.4)
become

\[
 \Psi_K(Y_{\rm old})=2\sum_i e_{i,\pi(i)},
 \qquad
 \Psi_K(Y_{\rm new})=2\sum_i e_{\pi(i),i}.            \tag{2.7}
\]

Thus the crown has an exact directed-arc ledger: a legal switch must make
the permutation digraph invariant under reversal.

## 3. The exact involution theorem

### Theorem 3.1 (common-core crown rigidity)

Under the hypotheses of Section 1, the multiset of all affected
adjacent-union colors is unchanged by (1.3) if and only if

\[
                             \pi^2=\mathrm{id}.         \tag{3.1}
\]

#### Proof

Because the blocks \(E_1,\ldots,E_k\) are pairwise disjoint, any active
three-set of the form

\[
                         E_i\cup\{x\},\qquad x\in E_j,
                         \quad i\ne j,                  \tag{3.2}
\]

uniquely determines its doubled block \(E_i\), its singleton block \(E_j\),
and the singleton coordinate \(x\). Indeed it contains all two coordinates
of exactly one block from the displayed block family.

Fix distinct \(i,j\). By (2.3), the old ledger contains the two colors of
ordered type \((i,j)\) exactly when \(\pi(i)=j\). By (2.4), the new ledger
contains the two colors of ordered type \((i,j)\) exactly when

\[
                         \pi(j)=i.                      \tag{3.3}
\]

Equality of the two color multisets is consequently equivalent to

\[
             \pi(i)=j\quad\Longleftrightarrow\quad\pi(j)=i
             \qquad(i\ne j).                           \tag{3.4}
\]

For a permutation, (3.4) says that every nonfixed orbit has length two,
which is exactly \(\pi^2=\mathrm{id}\).

Conversely, if \(\pi\) is an involution, then every transposition
\(i\leftrightarrow j\) contributes the two old palettes

\[
 \{K\cup E_i\cup x:x\in E_j\},\qquad
 \{K\cup E_j\cup x:x\in E_i\},                       \tag{3.5}
\]

and the new ledger simply interchanges them. Fixed points make no change.
Hence the full \(Y\)-multiset is preserved. \(\square\)

### Corollary 3.2 (no growing permutation cycle)

If \(\pi\) contains a cycle of length \(s\ge3\), then the replacement
(1.3) fails exact \(Y\)-saturation. This remains true when

\[
                         s=s(r)\longrightarrow\infty.  \tag{3.6}
\]

No completion outside the selected rows can repair the discrepancy while
all outside rows remain fixed, because their old and new color contributions
cancel identically.

There is a useful necessary condition even after pairwise disjointness is
dropped.

### Proposition 3.3 (cross-block necessity for any long crown cycle)

Keep the common core \(K\), but now let the distinct two-blocks \(E_i\) be
allowed to overlap. Suppose

\[
 \pi=(1\ 2\ \cdots\ k),\qquad k\ge3,                 \tag{3.7}
\]

and cross legality holds, so

\[
                         E_i\cap E_{i+1}=\varnothing  \tag{3.8}
\]

cyclically. If the \(Y\)-ledger is exact, then for every \(i\) the active
block family contains a block \(E_j\) of the form

\[
                         E_j=\{e,x\},
 \qquad e\in E_i,quad x\in E_{i+1}.                 \tag{3.9}
\]

Thus every disjoint consecutive pair in the permutation cycle must be
bridged by a third active block meeting both. In particular the pairwise
disjoint crown is impossible for every \(k\ge3\).

#### Proof

Because \(k\ge3\), the distinct two-sets \(E_{i-1}\) and \(E_{i+1}\) are
not equal. Choose

\[
                         x\in E_{i+1}\setminus E_{i-1}. \tag{3.10}
\]

The old ledger contains the color

\[
                         T=K\cup E_i\cup\{x\}.         \tag{3.11}
\]

An equal new color from some row \(h\) has the form

\[
                         T=K\cup E_{h+1}\cup\{y\},
                         \qquad y\in E_h.              \tag{3.12}
\]

If \(E_{h+1}=E_i\), distinctness gives \(h+1=i\), so \(h=i-1\), and
(3.12) would force \(y=x\in E_{i-1}\), contrary to (3.10). Hence
\(E_{h+1}\ne E_i\). It is a two-subset of the three-set
\(E_i\cup\{x\}\), so it contains \(x\) and one element \(e\in E_i\).
Taking \(j=h+1\) proves (3.9). \(\square\)

Proposition 3.3 identifies the first possible escape from Theorem 3.1:
long cycles require a collision-rich active-block family closed under
cross-blocks. Merely abandoning private collars without supplying these
bridges cannot work.

### Proposition 3.4 (sharpness: the pentagonal collision)

The cross-block condition is genuinely realizable. On five distinct active
coordinates \(a,b,c,d,e\), put

\[
 E_1=ab,qquad E_2=cd,qquad E_3=be,qquad
 E_4=ac,qquad E_5=de.                                \tag{3.13}
\]

Consecutive blocks in the cyclic order \(E_1,E_2,E_3,E_4,E_5\) are
disjoint. Moreover the five-cycle permutation has zero total color
discrepancy.

#### Proof

Suppress the common core \(K\). The old ten colors are

\[
 abc,abd,bcd,cde,abe,bce,acd,ace,ade,bde,             \tag{3.14}
\]

while the new ten colors, grouped in the reverse doubled/singleton types,
are

\[
 acd,bcd,bce,bde,abc,ace,ade,cde,abd,abe.             \tag{3.15}
\]

These are the same set. \(\square\)

This is the common-core shadow of the rooted five-row pentagon. It shows
that Theorem 3.1 cannot be extended from disjoint blocks to arbitrary
overlapping blocks.

There are arbitrarily long **ledger** cycles obtained by gluing these
pentagons, but they do not supply a new irreducible mechanism. For disjoint
two-blocks \(E,F\), define the signed color discrepancy

\[
 \partial(E,F)
 =\sum_{x\in F}e_{K\cup E\cup\{x\}}
  -\sum_{x\in E}e_{K\cup F\cup\{x\}}.                \tag{3.16}
\]

It is antisymmetric. Given a directed disjointness edge

\[
 U=ab\longrightarrow V=cd,                            \tag{3.17}
\]

and a fresh coordinate \(z\), the pentagon

\[
 U\to V\to bz\to ac\to dz\to U                     \tag{3.18}
\]

has zero \(\partial\)-sum by Proposition 3.4. Hence, inside any zero-sum
cycle containing \(U\to V\), one may replace that edge by

\[
 U\to dz\to ac\to bz\to V.                           \tag{3.19}
\]

The cycle length increases by three and its \(\partial\)-sum remains zero.
Iterating with fresh coordinates gives zero-label cycles of lengths

\[
                         5,8,11,14,\ldots.             \tag{3.20}
\]

Every such identity is, by construction, an integral sum of bounded
pentagon identities. It therefore does not by itself give a new
peak-erased-owner move. In addition, (3.20) certifies only the boundary
color ledger: a literal anchored factor still requires collision-free outer
states and completion to fixed \(\mathcal D_r\)-ports at every intermediate
stage. Thus pentagonal ear gluing is an exact explanation of why long
zero-label equations alone are insufficient.

## 4. Matching interpretation and octahedral decomposition

### Proposition 4.1 (every surviving orbit is one rectangle)

Suppose \(\pi\) interchanges \(i,j\). Then the two changed rows form an
affine four-coordinate octahedral rectangle. In particular, their changes in
the two perfect incidence matchings are the standard coordinated pair of
alternating six-cycles.

#### Proof

Write

\[
 E_i=\{a,b\},\qquad E_j=\{c,d\}.
\]

By Lemma 2.1, the two outer states in row \(i\) are one opposite pair among

\[
                         Kac,Kad,Kbc,Kbd.               \tag{4.1}
\]

The second row has the same two possible middle states and must also use an
opposite pair of common neighbours. Exact \(X\)-ownership forbids it from
reusing either outer state of the first row. Hence it uses the other opposite
pair. After relabelling \(c,d\), the two old slabs are

\[
 \begin{array}{c|ccc}
 i&Kac&Kab&Kbd\\
 j&Kad&Kcd&Kbc,
 \end{array}                                           \tag{4.2}
\]

and the new slabs are

\[
 \begin{array}{c|ccc}
 i&Kac&Kcd&Kbd\\
 j&Kad&Kab&Kbc.
 \end{array}                                           \tag{4.3}
\]

The four colors on either side are

\[
                         Kabc,Kabd,Kacd,Kbcd.           \tag{4.4}
\]

This is precisely the octahedral rectangle. Splitting every alternating
path edge into its \(\mathcal X-\mathcal Y\) incidence edges gives the usual
two coordinated alternating six-cycles, one in each perfect matching.
\(\square\)

### Corollary 4.2 (complete classification of the crown architecture)

Every legal common-core crown move is a disjoint product of octahedral
two-row moves. There is no irreducible alternating-cycle component involving
three or more rows.

The result is stronger than a parity obstruction: it identifies the complete
integral fibre of this architecture.

## 5. Multiple crowns with private palettes

The same argument survives an arbitrary number of simultaneous crowns.
Suppose crown \(\alpha\) has core \(K_\alpha\), pair blocks
\(E_{\alpha,i}\), and permutation \(\pi_\alpha\). Assume their possible
affected color palettes

\[
 \mathcal P_\alpha=
 \{K_\alpha\cup E_{\alpha,i}\cup\{x\}:
       i\ne j,\ x\in E_{\alpha,j}\}                   \tag{5.1}
\]

are pairwise disjoint over \(\alpha\). This is the exact private-collar
condition; no geometric separation beyond (5.1) is needed.

### Corollary 5.1 (private-palette multi-crown no-go)

The simultaneous replacement preserves the global \(Y\)-ledger if and only
if every

\[
                         \pi_\alpha^2=\mathrm{id}.      \tag{5.2}
\]

#### Proof

Project the global color identity onto the disjoint coordinate block
\(\mathbb Z^{\mathcal P_\alpha}\) and apply Theorem 3.1 separately to every
crown. \(\square\)

Thus independent collars cannot hide a growing cycle by aggregate
cancellation. Any escape must deliberately share boundary colors between
different crowns or between different phase cuts.

## 6. Implication for the peak-erased Motzkin gate

Let \(\nu(P)\) denote the peak-erased Motzkin normal form of a Dyck root
\(P\). A proposed crown cycle

\[
 P_1\longrightarrow P_2\longrightarrow\cdots
 \longrightarrow P_s\longrightarrow P_1              \tag{6.1}
\]

can be arranged so that the displayed owners meet several \(\nu\)-classes,
but Theorem 3.1 shows that its middle-levels realization cannot preserve the
adjacent-union ledger when \(s\ge3\). Exact \(X\)-saturation and identity
endpoint monodromy do not help: both were automatic before the failure was
detected.

When the ledger is exact, every owner-routing orbit has size at most two and
Proposition 4.1 reduces it to a bounded rectangle. Therefore this architecture
does not provide the requested genuinely growing mechanism for changing the
peak-erased owner class. It only returns to the already known bounded
two-row menu.

This conclusion is deliberately narrower than an invariant of the full
anchored fibre. An individual surviving rectangle might exchange data between
two owner labels in a setting where such a rectangle exists. The theorem says
that no **long crown cycle** supplies any additional freedom beyond those
two-row moves.

## 7. Audit and exact boundary

The proof uses all of the following hypotheses.

1. **One changed phase.** Only the middle states \(B_i\) are permuted.
2. **Common core.** Every changed middle state is \(K\cup E_i\) for the same
   \((r-2)\)-set \(K\).
3. **Pairwise-disjoint blocks.** The \(E_i\) form a matching. This is what
   makes the doubled/singleton color type unique.
4. **Literal geodesics.** Both old and proposed slabs belong to complementary
   length-\(r\) paths. This forces opposite cross-pairs in Lemma 2.1.
5. **No outside changes.** Outside rows cancel from the ledger comparison.

Under these hypotheses there is no omitted completion issue:

* the \(X\)-ledger is preserved by permutation;
* the roots and complementary endpoints are fixed pointwise;
* legal adjacency plus unchanged length gives geodesic, hence acyclic, rows;
* Theorem 3.1 is exactly the remaining \(Y\)-saturation condition; and
* Proposition 4.1 identifies every integral solution.

The theorem does not address any of the following possible escapes.

* Active blocks which overlap outside the common core. Then a color may admit
  more than one doubled-block interpretation.
* A slab of two or more changed phases whose entry and exit color
  discrepancies cancel one another.
* Several crowns with deliberately overlapping palettes.
* A fully non-phase-monotone alternating-cycle system in the two matchings.

These are the precise places where a successful long-cycle construction must
leave the crown architecture. In particular, merely increasing the number of
pairwise-disjoint rows from bounded size to \(\Theta(r)\) cannot cross the
peak-erased Motzkin gate.

## 8. Independent audit

An independent proof audit confirmed the directed-type argument and checked
the two possible hidden points.

First, for a moved row the four common neighbours of \(K\cup E_i\) and
\(K\cup E_{\pi(i)}\) form a square. The geodesic identity
\(d_J(A_i,C_i)=2\) forces opposite corners. Independently, if adjacent
corners were used, the two new incident \(Y\)-colors would coincide, already
contradicting exact \(Y\)-ownership.

Second, no extra cycle can appear in the union of the two matchings after an
involutive legal switch: every displayed row still advances through the same
strict phase order, the phasewise \(X\)-states remain a permutation, and the
root/complement endpoints remain fixed. Thus the proof has not silently
replaced the nonlinear path condition by the two linear ledgers.
