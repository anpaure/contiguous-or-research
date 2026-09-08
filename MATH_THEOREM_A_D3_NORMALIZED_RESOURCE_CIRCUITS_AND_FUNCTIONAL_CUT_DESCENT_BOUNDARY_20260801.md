# Normalized depth-three resource circuits and the functional Hall-cut boundary

**Date:** 2026-08-01  
**Status:** exact algebraic reduction, exact cut min--max, a protected
two-sum sufficient theorem, and exact smallest-dimensional obstructions.
No all-\(m\) descent theorem is claimed.

## 0. Verdict

For the all-high depth-three row, a literal option is exactly a normalized
pair

\[
 f=(S,z),\qquad |S|=m-2,\quad 0,z\notin S,\quad z\ne0.       \tag{0.1}
\]

Its two nonroot resources are

\[
 T(f)=[S],\qquad P(f)=[S\cup\{0\}].                         \tag{0.2}
\]

Consequently a three-root replacement is resource zero precisely when its
new \(T\)-multiset and new \(P\)-multiset separately equal the old ones. It
is primitive precisely when no one of its three row deltas is zero. With
occurrences labelled, every such circuit is therefore a pair of
permutations of three old \(T\)- and \(P\)-resources, subject only to three
literal root-admissibility tests.

After fixing a functional root-to-owner attachment, chronology is the
punctured-containment graph

\[
 i\longrightarrow j
 \iff z_i\in Z_\vartheta(f_j),\quad
 S_i=H_j-\{\beta\}\text{ for some }\beta\in H_j-\{\gamma_j\}. \tag{0.3}
\]

For every fixed head-root set \(Y\), a circuit changes its Hall deficiency
by exactly

\[
 |A_Y|-|L_Y|,                                                \tag{0.4}
\]

where \(A_Y\) and \(L_Y\) are the added and lost **distinct tail-root
neighbours**. Positive value in (0.4) is necessary on every old
maximum-deficiency cut for a matching increase; positivity on only one
chosen cut is not sufficient.

Two boundaries are essential.

1. A general nine-type K17 row \((t,C_0,C_1,C_2)\) has a single
   \((S,z)\)-normalization only for \(t=(m-2,1,1)\). The authenticated
   support-three serial gains use type migration and therefore do not by
   themselves prove the pure all-high theorem below.
2. The unqualified statement “positive deficiency always admits a
   primitive cut-positive three-root circuit” is false already at \(m=2\):
   the functional graph is empty and every option delta is zero.

The first nondegenerate failure is at \(m=3\): a binary protected face has
one genuine primitive, \(z\)-deck-preserving three-trade, but the head
refresh labels and tail bottoms lie in disjoint coordinate sets, so the
functional graph is empty both before and after. The exact positive
replacement is Theorem 4.3: an external puncture must have a protected
distinct-root two-sum completion in the resource-delta system.

Thus the genuine large-\(m\) target is a **critical three-trade
accessibility theorem** for the literal root-coloured option system,
together with the all-cut inequalities of Section 4.

## 1. Literal row to \((S,z)\) exactly

Write the cyclic ground set additively as \(\mathbb Z_n\), \(n=2m+1\), and
write \(A-c=\{a-c:a\in A\}\). An all-high literal row is

\[
 C_0\subset C_0\mathbin{\dot\cup} C_1
       \subset C_0\mathbin{\dot\cup} C_1\mathbin{\dot\cup} C_2=Q, \tag{1.1}
\]

with

\[
 |C_0|=m-2,\qquad C_1=\{b\},\qquad C_2=\{a\}.          \tag{1.2}
\]

Descending from \(Q\), the first deleted coordinate is \(a\), and the
second is \(b\). Normalize the second deletion to zero and put

\[
 S=C_0-b,\qquad z=a-b.                                      \tag{1.3}
\]

Then (1.1) becomes

\[
 S\cup\{0,z\}\supset S\cup\{0\}\supset S,             \tag{1.4}
\]

with deletion word \((z,0)\). Conversely, translating (1.4) so that its
root is the prescribed representative \(Q\) recovers (1.1). On a free
cyclic root orbit this translation is unique. Thus (1.3) is a bijection
between literal all-high row options at rooted necklace orbits and the
normalized options (0.1) satisfying

\[
 [S\cup\{0,z\}]=[Q].                                        \tag{1.5}
\]

The row resource vector, with its fixed root and fixed all-high type
suppressed, is

\[
 r(S,z)=e_{[S]}+e_{[S\cup\{0\}]}.                           \tag{1.6}
\]

Indeed translation does not change either necklace label. Relative to an
incumbent \(f^0=(S^0,z^0)\) at the same root,

\[
 \partial(S,z)
 =e_{[S]}+e_{[S\cup\{0\}]}
  -e_{[S^0]}-e_{[S^0\cup\{0\}]}.                            \tag{1.7}
\]

Notice that \(z\) enters (1.7) only through root admissibility (1.5).
Distinct literal options can therefore have zero delta. Such an option is
a unary resource circuit, not a primitive member of a support-three packet.

### Proposition 1.1 (sharp scope of the normalization)

A general block row \((t,C_0,C_1,C_2)\) is represented by one normalized
depth-three pair \((S,z)\) if and only if

\[
 (|C_0|,|C_1|,|C_2|)=(m-2,1,1).                            \tag{1.8}
\]

#### Proof

A pair \((S,z)\) records exactly two ordered singleton deletions from a
rank-\(m\) root. Hence both difference blocks in (1.1) must be singletons,
and the bottom has rank \(m-2\), proving necessity. Formula (1.3) proves
sufficiency. \(\square\)

For K17, (1.8) is type \((6,1,1)\). Rows of any of the other eight types
require a block-deletion state and cannot be imported into the present
normal form without adding further data.

## 2. Complete primitive support-three normal form

Fix three distinct rooted orbits \(R_1,R_2,R_3\). Let

\[
 f_i=(S_i,z_i),\qquad f'_i=(S'_i,z'_i)                       \tag{2.1}
\]

be the old and new literal options at \(R_i\). Abbreviate

\[
 t_i=[S_i],\quad p_i=[S_i\cup\{0\}],\qquad
 t'_i=[S'_i],\quad p'_i=[S'_i\cup\{0\}].                    \tag{2.2}
\]

### Theorem 2.1 (two-deck and permutation characterization)

The three-root replacement preserves the complete all-high resource ledger
if and only if

\[
 \{t'_1,t'_2,t'_3\}_{\rm multi}=\{t_1,t_2,t_3\}_{\rm multi},
 \qquad
 \{p'_1,p'_2,p'_3\}_{\rm multi}=\{p_1,p_2,p_3\}_{\rm multi}. \tag{2.3}
\]

Equivalently, after occurrence-labelling repeated resource values, there
are permutations \(\sigma,\tau\in S_3\) such that

\[
 t'_i=t_{\sigma(i)},\qquad p'_i=p_{\tau(i)}.                 \tag{2.4}
\]

The circuit is primitive if and only if

\[
 (t'_i,p'_i)\ne(t_i,p_i)\qquad(i=1,2,3).                    \tag{2.5}
\]

#### Proof

The rank-\((m-2)\) and rank-\((m-1)\) resource coordinates in (1.7) are
disjoint. Their total signed change vanishes exactly when the two multiset
equalities (2.3) hold. Matching equal occurrences gives (2.4), and (2.4)
implies (2.3). A single row delta in (1.7) is zero exactly when its two
resource labels are unchanged. For three zero-sum deltas, absence of a
zero singleton is equivalent to minimality: if a proper pair summed to
zero, the remaining singleton would also be zero. This proves (2.5).
\(\square\)

Literal root feasibility can be kept separate from resource balance. Put

\[
 \Omega_R(t,p)=\{(S,z):[S]=t,\ [S\cup\{0\}]=p,\
                         [S\cup\{0,z\}]=R\}.                 \tag{2.6}
\]

### Corollary 2.2 (root-coloured three-trade test)

A pair \((\sigma,\tau)\) from (2.4) gives a literal primitive circuit on
\(R_1,R_2,R_3\) if and only if one can choose

\[
 f'_i\in\Omega_{R_i}(t_{\sigma(i)},p_{\tau(i)})
 \qquad(i=1,2,3)                                            \tag{2.7}
\]

so that (2.5) holds. Thus the pure \(d=3\) support-three basis is exactly
the catalogue of root-coloured three-edge trades between the two resource
decks. There is no additional signed-lattice condition.

This exposes the first structural obstruction to descent: a deficient table
may have no root-coloured three-trade (2.7), even though the uncoloured two
resource decks balance perfectly.

### Proposition 2.3 (the fixed-alignment third deck)

If a physical alignment \(\zeta\), and hence the individual \(z\)-block
sizes, is frozen, and every contemplated replacement remains literally
compatible with its prescribed head alignment, the correct additional
balance signature is

\[
 \widehat r(S,z)=e_{[S]}+e_{[S\cup\{0\}]}+e_z.              \tag{2.8}
\]

A three-root circuit preserves this fixed-alignment face if and only if
(2.3) holds and, additionally,

\[
 \{z'_1,z'_2,z'_3\}_{\rm multi}
   =\{z_1,z_2,z_3\}_{\rm multi}.                            \tag{2.9}
\]

Equivalently, (2.4) is supplemented by a third occurrence permutation
\(\rho\in S_3\), \(z'_i=z_{\rho(i)}\). Primitivity for the augmented
signature means

\[
 (t'_i,p'_i,z'_i)\ne(t_i,p_i,z_i)\quad(i=1,2,3).            \tag{2.10}
\]

#### Proof

The three coordinate banks in (2.8) are disjoint, so zero total delta is
equivalent to equality of their three occurrence multisets. The same
three-vector zero-sum argument as in Theorem 2.1 proves (2.10).
\(\square\)

Thus a static two-deck circuit which violates (2.9) is not a circuit in a
frozen block decomposition. It is usable only if the alignment/attachment
is simultaneously reselected and its flux cuts are recomputed.

## 3. Functional punctured-containment graph

For \(f=(S,z)\), its head-normalized signature is

\[
 \Gamma(f)=(H,\gamma),\qquad
 H=(S-z)\cup\{-z\},\qquad \gamma=-z.                        \tag{3.1}
\]

Fix a quotient root-to-owner containment bijection \(\vartheta\). For a
selected head row \(f_j\), let \(Z_\vartheta(f_j)\) be its allowed physical
owner-alignment labels. Index both shores by rooted rows. The functional
predecessor graph \(B_\vartheta(F)\) has the exact edge predicate

\[
 i\longrightarrow j
 \iff
 \begin{cases}
 z_i\in Z_\vartheta(f_j),\\
 S_i\subset H_j,\\
 |H_j-S_i|=1,\\
 \gamma_j\in S_i.
 \end{cases}                                                \tag{3.2}
\]

Equivalently, \(S_i=H_j-\{\beta\}\) for one
\(\beta\in H_j-\{\gamma_j\}\). If one alignment
\(\zeta(j)\in Z_\vartheta(f_j)\) has already been selected, the first row
of (3.2) becomes \(z_i=\zeta(j)\), and the graph splits into the usual
punctured-containment blocks.

#### Proof of (3.2)

The exact predecessor formula for a head \((H_j,\gamma_j)\) and external
owner label \(z_i\) is

\[
 (H_j-\{\beta\},z_i),\qquad\beta\in H_j-\{\gamma_j\}.
\]

Identifying this predecessor with \(f_i=(S_i,z_i)\) gives (3.2), and every
row satisfying (3.2) gives that literal predecessor. \(\square\)

In contrast with the common both-live projection used in the finite K17
lineage, (3.2) is a direct bipartite predicate: after changing a root set
\(I\), an edge with both endpoint roots outside \(I\) cannot change. There
is no extra liveness halo at this functional level.

## 4. Exact cut impact and the descent condition

For a set \(Y\) of head roots define

\[
 N_F(Y)=\{i:\text{(3.2) holds for some }j\in Y\}.             \tag{4.1}
\]

After a literal resource circuit \(F\mapsto F'\), put

\[
 A_Y=N_{F'}(Y)-N_F(Y),\qquad
 L_Y=N_F(Y)-N_{F'}(Y),\qquad
 \kappa_C(Y)=|A_Y|-|L_Y|.                                  \tag{4.2}
\]

These are sets of distinct tail-root neighbours, not edge occurrences,
alignments, or resource labels.

### Theorem 4.1 (functional fixed-cut and all-cut formula)

For every \(Y\),

\[
 |Y|-|N_{F'}(Y)|
 =\bigl(|Y|-|N_F(Y)|\bigr)-\kappa_C(Y).                     \tag{4.3}
\]

Let

\[
 D=\max_Y\bigl(|Y|-|N_F(Y)|\bigr),\qquad |V|=N.             \tag{4.4}
\]

Then, for every integer \(a\ge0\),

\[
 \nu(B_\vartheta(F'))\ge N-D+a                              \tag{4.5}
\]

if and only if

\[
 \boxed{\quad
 \kappa_C(Y)\ge |Y|-|N_F(Y)|-D+a
 \quad\text{for every }Y\subseteq V.
 \quad}                                                      \tag{4.6}
\]

#### Proof

Equation (4.3) is the disjoint added/lost-neighbour identity. Hall's
deficiency formula gives

\[
 \nu(B_\vartheta(F'))
 =N-\max_Y\{\,|Y|-|N_F(Y)|-\kappa_C(Y)\,\},
\]

which is equivalent to (4.6). \(\square\)

In particular, a one-unit matching increase requires

\[
 \kappa_C(Y)\ge1
 \quad\text{on every old deficiency-\(D\) cut},             \tag{4.7}
\]

and the corresponding nonloss inequalities on all near-critical cuts.
Thus \(|A_Y|>|L_Y|\) for one canonical DM shore is a proof-safe necessary
filter, not a serial-descent theorem.

### Lemma 4.2 (protected completion criterion)

Let \(C\) be a literal primitive circuit of Corollary 2.2 and let \(Y\) be
a fixed Hall shore. Suppose:

1. some \(u\notin N_F(Y)\) satisfies \(u\in N_{F'}(Y)\); and
2. every \(v\in N_F(Y)\) retains at least one predecessor edge into \(Y\)
   under (3.2).

Then \(A_Y\ne\varnothing\), \(L_Y=\varnothing\), and

\[
 \kappa_C(Y)\ge1.                                           \tag{4.8}
\]

The hypotheses are literal set-containment tests in (3.2). They give a
usable sufficient target: create one external punctured facet, and complete
its two-deck delta on two further roots without destroying the last old
witness of any old neighbour.

The next form isolates the algebraic hypothesis missing from ordinary
punctured-containment expansion. A substitution is called **allowed** here
only if it is root-admissible and retains the fixed functional attachment
\(\vartheta\). If a headwise alignment \(\zeta\) is frozen, its new head
option must also satisfy
\(\zeta(r)\in Z_\vartheta(f'_r)\). Use the augmented delta from (2.8) in
that case, and the two-deck delta from (1.7) otherwise.

### Theorem 4.3 (external puncture plus protected two-sum)

Fix a Hall shore \(Y\), put \(K=N_F(Y)\), and suppose an allowed
substitution \(a\) at a root

\[
                         r_0\notin K\cup Y                 \tag{4.9}
\]

installs a punctured predecessor of some head in \(Y\). Thus \(r_0\) is a
new neighbour of \(Y\). Let its resource delta be \(\delta_a\). Suppose
two further allowed substitutions \(b,c\), at roots \(r_1,r_2\), satisfy:

1. \(r_0,r_1,r_2\) are pairwise distinct and all lie outside \(K\cup Y\);
2. the two-deck projection of each of
   \(\delta_a,\delta_b,\delta_c\) is nonzero; and
3.

\[
                  \delta_a+\delta_b+\delta_c=0.             \tag{4.10}
\]

Then the three substitutions form a primitive static resource-zero circuit
(and, when augmented deltas are used, a circuit on the frozen-alignment
face), and

\[
                  N_F(Y)\cup\{r_0\}\subseteq N_{F'}(Y),
                  \qquad \kappa_C(Y)\ge1.                  \tag{4.11}
\]

For a fixed anchor \(a\), condition (4.10) is necessary and sufficient for
an anchor-containing completion whose other two roots belong to the
protected exterior \(V-(K\cup Y\cup\{r_0\})\), subject to the stated
nonzero-projection condition. Equivalently,

\[
 -\delta_a\in
 \left\{\delta_b+\delta_c:
  r_b,r_c\text{ distinct protected exterior roots},\
  \overline\delta_b,\overline\delta_c\ne0\right\},          \tag{4.12}
\]

where \(\overline\delta\) denotes the two-deck projection.

#### Proof

Equation (4.10) and nonvanishing of all three two-deck projections give a
primitive static circuit by Theorem 2.1. With augmented deltas, (4.10) also
preserves the \(z\)-deck by Proposition 2.3. Only an endpoint root of an
edge in the functional predicate (3.2) can change that edge. The three
changed roots lie outside \(K\cup Y\), so no old edge from a root in \(K\)
to a head in \(Y\) changes. The anchor adds the declared edge from \(r_0\)
into \(Y\), proving (4.11). Necessity and sufficiency of (4.12) are just
(4.10), with the distinct-root, compatibility, and protected-support
restrictions retained. \(\square\)

There is a transparent sufficient pattern for (4.10). Suppose the old
two-deck signatures at three protected exterior roots are

\[
 (P_0,T_0),\qquad(P_1,T_1),\qquad(P_2,T_2),                \tag{4.13}
\]

and allowed literal options exist with new signatures

\[
 (P_1,T_2),\qquad(P_2,T_0),\qquad(P_0,T_1).                \tag{4.14}
\]

If the first option is the external puncture and all three row deltas are
nonzero, (4.14) is a primitive cut-positive circuit. On a fixed-alignment
face, also require each changed head option to retain its prescribed
alignment and require the three new \(z\)-occurrences to be a permutation
of the old ones. Indeed (4.14) separately permutes both old resource decks;
this is the smallest literal **Latin cross** realizing the protected
two-sum condition.

### Lemma 4.4 (raw external-puncture count)

Choose one allowed functional label \(z(y)\in Z_\vartheta(y)\) for every
\(y=(H_y,\gamma_y)\in Y\). Call each literal option

\[
                    (H_y-\{\beta\},z(y)),
             \qquad \beta\in H_y-\{\gamma_y\},              \tag{4.15}
\]

an accessible puncture when its root menu contains it. Let
\({\cal A}(Y)\) be the resulting multiset of puncture incidences, and
suppose at most \(\Delta\) of its incidences lie at any one root. If

\[
                    |{\cal A}(Y)|>\Delta(|K|+|Y|),          \tag{4.16}
\]

then \(Y\) has an accessible puncture rooted outside \(K\cup Y\).

#### Proof

If every accessible puncture were rooted in \(K\cup Y\), the root
multiplicity bound would give at most
\(\Delta|K\cup Y|\le\Delta(|K|+|Y|)\) incidences, contrary to (4.16).
\(\square\)

In the complete punctured host, a fixed allowed label supplies exactly
\(m-2\) incidences per head (the full alignment catalogue may supply more).
Thus, for \(m\ge3\) and \(\Delta>0\), the bound
\(\Delta\le(m-2)/2\) forces (4.16) on every nonempty deficient shore:

\[
 (m-2)|Y|\ge2\Delta|Y|>
                    \Delta(|K|+|Y|).                        \tag{4.17}
\]

This only produces the anchor. It gives no reason for its delta to satisfy
the protected two-sum condition (4.12), which is exactly where ordinary
punctured Hall expansion stops.

## 5. The unqualified descent statement is false

### Proposition 5.1 (smallest-dimensional exception)

At \(m=2\), \(n=5\), the functional depth-three graph has positive
deficiency but admits no primitive resource-zero support-three circuit.

#### Proof

Here \(|S|=m-2=0\), so every normalized option is

\[
 (\varnothing,z).
\]

All of them have the same two resources

\[
 T=[\varnothing],\qquad P=[\{0\}],
\]

and hence every literal option delta is zero. No primitive circuit exists.

Moreover (3.1) gives \(H=\{-z\}\) and \(\gamma=-z\). The punctured
predecessor set is indexed by

\[
 \beta\in H-\{\gamma\}=\varnothing,
\]

so the functional graph has no edges. Its two root-necklace vertices have
matching zero and positive deficiency. \(\square\)

This is the first admissible value of \(m\) for a depth-three flag, so it is
the smallest-dimensional exception. Any dimension-uniform descent theorem
must at least assume \(m\ge3\), and even then it must rule out the genuine
structural obstruction visible in (2.7): absence of an admissible
root-coloured three-trade through the critical punctured-facet boundary.

### Proposition 5.2 (smallest nondegenerate three-trade exception)

At \(m=3,n=7\), a protected three-root residual table can have a unique
primitive resource-zero support-three circuit while both its old and new
functional graphs are empty.

Take the three distinct rooted necklaces

\[
 Q_{12}=\{0,1,2\},\qquad
 Q_{23}=\{0,2,3\},\qquad
 Q_{31}=\{0,1,3\}.                                      \tag{5.1}
\]

Their cyclic gap words are `115`, `214`, and `124`, no two cyclic rotations
of one another. The three rank-two resources below are likewise distinct
necklace orbits, with circular distances `1`, `2`, and `3`. Equip the roots
with the incumbent and alternative normalized options

\[
\begin{array}{c|cc}
Q_{12}&(\{1\},2)&(\{2\},1)\\
Q_{23}&(\{2\},3)&(\{3\},2)\\
Q_{31}&(\{3\},1)&(\{1\},3).
\end{array}                                                \tag{5.2}
\]

For definiteness, a legal residual functional attachment is

\[
\begin{aligned}
 Q_{12}&\longmapsto[\{0,1,2,3\}],\\
 Q_{23}&\longmapsto[\{0,2,3,4\}],\\
 Q_{31}&\longmapsto[\{0,1,3,5\}].
\end{aligned}                                               \tag{5.2a}
\]

The three owner necklaces are distinct and the displayed representatives
contain their respective roots. The argument below in fact makes the graph
empty for every legal functional attachment.

Simultaneously taking the second column has deltas

\[
\begin{aligned}
v_1&=e_{[\{0,2\}]}-e_{[\{0,1\}]},\\
v_2&=e_{[\{0,3\}]}-e_{[\{0,2\}]},\\
v_3&=e_{[\{0,1\}]}-e_{[\{0,3\}]}.
\end{aligned}                                               \tag{5.3}
\]

All three singleton \(T\)-resources have the same necklace label. Hence
(5.3) is the complete delta, its sum is zero, and its three terms are
nonzero. The circuit is primitive. Its old and new \(z\)-multisets are
both \(\{1,2,3\}\), so it also preserves the augmented \(z\)-deck algebra
(2.8). A genuinely frozen headwise alignment additionally needs the
per-option compatibility stated in Proposition 2.3; it is not inferred
from the multiset identity alone.

Because the menus are binary, every replacement packet is a subset sum of
the three vectors in (5.3). No nonempty proper subset sums to zero, so the
simultaneous three-row replacement is the unique nonempty resource-zero
packet on this residual face.

For every option in (5.2), however, \(S\subseteq\{1,2,3\}\) while
\(\gamma=-z\in\{4,5,6\}\). The necessary punctured-containment condition
\(\gamma_j\in S_i\) in (3.2) therefore fails for every ordered pair, before
and after the circuit, independently of the owner attachment. Both
functional graphs are empty, every nonempty shore is deficient, and every
cut impact is zero. In particular, each singleton head shore is a minimal
Hall-deficient shore of deficiency one, so the failure is not caused by
taking a large or nonminimal Hall set.

### Corollary 5.3 (refresh--bottom separation)

Let \({\cal M}\) be any protected residual family of normalized menus. If

\[
             \gamma(g)\notin S(f)
       \qquad\text{for every }f,g\in\bigcup_R{\cal M}_R,     \tag{5.4}
\]

then every selected functional predecessor graph on this menu family is
empty, for every legal functional attachment. Consequently every
resource-zero circuit contained in the family has zero cut impact on every
shore, irrespective of its support or primitivity.

#### Proof

Condition (5.4) negates the necessary row
\(\gamma_j\in S_i\) of the exact edge predicate (3.2) for every possible
ordered pair. Hence no selection has an edge. \(\square\)

This is minimal among nondegenerate examples: \(m=3\) is the first
dimension with at least three root necklaces and with positive punctured
degree \(m-2\). Its scope is a protected residual/binary-menu face. It does
not refute a theorem for the uncontracted complete-option host, but it shows
that resource-zero primitivity alone supplies no cut descent.

## 6. Exact remaining theorem target

The pure all-high static gate would follow from the following statement
(together with serial recomputation of the functional attachment):

> **Critical three-trade accessibility.** For every \(m\ge3\), every
> resource-exact selected normalized table \(F\), and every functional
> attachment \(\vartheta\) with \(D>0\), there is a literal primitive
> three-root trade satisfying (2.7) and all the inequalities (4.6) with
> \(a=1\), where every uncontracted root may use its complete literal cell
> \(\Omega_R\).

The complete-cell quantifier is essential: Proposition 5.2 refutes the
same statement on protected residual menus. On such a residual face, the
proof-safe replacement is the explicit hypothesis (4.12), or a stronger
uniform theorem implying it for every critical external puncture.

A weaker assertion giving only positive (0.4) on one selected critical cut
does not imply matching descent. A still weaker assertion omitting (2.7)
is only an uncoloured two-deck switch and need not be physically assignable
to the three roots.

The hundreds of K17 gains in the authenticated serial census support the
plausibility of a rich exchange principle in the **nine-type** system, but
they prove neither critical three-trade accessibility in the pure
\((S,z)\) fibre nor the all-cut condition. The exact next mathematical
question is therefore whether the root-coloured cells (2.6) have enough
exchange to force Lemma 4.2 simultaneously on every maximum-deficiency cut,
or whether an \(m\ge3\) three-trade-free critical boundary exists.
