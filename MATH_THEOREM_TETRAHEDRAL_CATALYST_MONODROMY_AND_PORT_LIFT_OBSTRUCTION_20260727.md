# Tetrahedral catalyst monodromy exists abstractly but has no canonical one-frame conveyor lift

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, or web
input is used.

Inputs:

- MATH_THEOREM_THREE_TOP_TWO_BASE_PROMOTION_CONVEYOR_20260726.md;
- MATH_THEOREM_MAXIMAL_PLACEHOLDER_CELL_ORDERED_CORE_INVARIANT_20260726.md;
- MATH_THEOREM_THREE_TOP_CONVEYOR_ORDERED_CORE_CATALYST_AUDIT_20260727.md;
- MATH_THEOREM_COMMON_CORE_BOUNDARY_SWAP_MARGINAL_ESCAPE_20260727.md.

## 0. Outcome

Let \(C\) have size \(M-3\), let

\[
                         V=\{0,1,2,3\},
\tag{0.1}
\]

and put

\[
 S=C\cup V,\qquad U_i=S\setminus\{i\}\quad(i\in V).
\tag{0.2}
\]

The four rank-\(M\) tops \(U_0,U_1,U_2,U_3\) form the smallest
Johnson tetrahedron on which the common \((M-2)\)-core can change. Face
\(F_l\) has common core \(C\cup\{l\}\) and touches the three tops
\(U_i\), \(i\ne l\).

There are two exact conclusions.

1. In the owner/permutation relaxation, the tetrahedron contains a
   recyclable catalyst. If \(g_l\) is the simultaneous placeholder
   transposition on face \(F_l\), then

   \[
      w=(g_1g_2g_1g_2g_0)^2
   \tag{0.3}
   \]

   is the identity on \(U_1,U_2,U_3\) and a nontrivial \(3\)-cycle on
   \(U_0\). Its integral frame ledger telescopes to one positive and one
   negative frame column on \(U_0\), with zero endpoint ledger on every
   other top. In fact the four face permutations generate the full
   product \(S_3^4\). Consequently no nonzero mod-two or integral
   ordered-core invariant survives in the abstract tetrahedral
   permutation system.

2. Word (0.3) is not a legal sequence of the canonical two-base
   conveyors in a one-frame transversal. More strongly, for \(H\ge3\),
   no word supported on one tetrahedron can restore three top frames and
   change the fourth if every face step is an audited canonical
   \((\omega,\omega')\) conveyor. The obstruction is a port invariant.
   The order on the permanent core \(C\) never changes. Three active
   face types force the same pair of \(C\)-orders to serve as canonical
   companions. That pair uniquely determines its two placeholder gaps.
   Every subsequent legal face therefore fixes the same third port, so
   the face type cannot change.

Thus the fixed-core star parity does not extend as an abstract
changing-core invariant: the explicit monodromy (0.3) destroys it at
the integral permutation level. Nevertheless the smallest literal
tetrahedral lift is impossible for the canonical conveyor. A recyclable
coefficient-one catalyst must use either an auxiliary top/order row, a
noncanonical multi-port companion, or a larger Johnson carrier on which
the companion port pair itself can move.

For the boundary-swap application, this distinction is decisive. A
neutral occurrence router, if it existed, could conjugate the exact
phase-\(2\) swap and leave precisely \(e_Y-e_X\) at the middle with
only \(O(H)\) signed-trace collateral. The abstract word (0.3) does not
provide such a router: it permutes labels but neither transports the
retained-path boundary nor has a literal trace-neutral conveyor lift.

## 1. The Johnson tetrahedron and its face reflections

For \(i\ne l\), the top \(U_i\) contains the three labels
\(V\setminus\{i\}\). The face \(F_l\) regards \(l\) as part of its
common core and swaps the other two labels. Let

\[
 s_{i,l}=\text{the transposition of }V\setminus\{i,l\}
 \quad\text{on }U_i,
\tag{1.1}
\]

and put \(s_{l,l}=1\). The relaxed face generator is

\[
                         g_l=(s_{0,l},s_{1,l},s_{2,l},s_{3,l})
                         \in S_3^4.
\tag{1.2}
\]

Equivalently, on the three labels of \(U_i\), the reflection
\(s_{i,l}\) fixes \(l\) and swaps the other two. This definition records
exactly the label permutation made by a plus-to-minus frame change. It
forgets only the requirement that the three source frames on one face
must be a coherent \(\omega,\omega',\omega'\) packet.

At the support-parity level the incidence matrix of the four faces
against the four tops is

\[
                         A=J_4-I_4.
\tag{1.3}
\]

Its eigenvalues over \(\mathbb Z\) are \(3,-1,-1,-1\), so

\[
                         \det A=-3.
\tag{1.4}
\]

In particular \(A\) is invertible over \(\mathbb F_2\). Hence a face
multiset which restores the swap parity at all four tops uses every
face evenly. This is the complete mod-two audit. It does not control
even permutations, and that missing information is decisive below.

## 2. A pure-top tetrahedral monodromy

For the top \(U_i\), write \(r_i\) for either orientation of the
\(3\)-cycle on \(V\setminus\{i\}\). The orientation will be fixed by the
calculation and is otherwise irrelevant.

Put

\[
                         c_{12}=g_1g_2g_1g_2.
\tag{2.1}
\]

On \(U_1\), the generator \(g_1\) is the identity, so \(c_{12}=1\).
The same holds on \(U_2\). On each of \(U_0,U_3\), the two generators
are distinct transpositions, and therefore

\[
 c_{12}|_{U_0}=r_0^{\pm1},\qquad
 c_{12}|_{U_3}=r_3^{\pm1}.
\tag{2.2}
\]

The signs can be chosen consistently, but are not needed: a
transposition conjugates every \(3\)-cycle to its inverse.

### Theorem 2.1 (ten-step pure-top word)

The word

\[
                         w=(c_{12}g_0)^2
                          =(g_1g_2g_1g_2g_0)^2
\tag{2.3}
\]

satisfies

\[
 w|_{U_1}=w|_{U_2}=w|_{U_3}=1,
 \qquad
 w|_{U_0}=r_0^{\pm1}\ne1.
\tag{2.4}
\]

#### Proof

On \(U_0\), \(g_0=1\), so \(w=c_{12}^2\), a nontrivial \(3\)-cycle.
On \(U_1\) and \(U_2\), \(c_{12}=1\), while \(g_0\) is a
transposition; hence \(w=g_0^2=1\). On \(U_3\), \(c_{12}\) is a
\(3\)-cycle and \(g_0\) a transposition. Their product is a
transposition, so its square is the identity. \(\square\)

The face counts in (2.3) are

\[
 \#F_0=2,\qquad \#F_1=4,\qquad \#F_2=4,\qquad \#F_3=0.
\tag{2.5}
\]

Thus every face is used evenly. The entire mod-two ledger is zero, yet
the integral endpoint permutation at \(U_0\) is nonzero.

## 3. The full telescoping frame ledger

Choose a reference cyclic frame \(P_i\) on each \(U_i\). For a prefix
\(v\) of a word in the \(g_l\), let \(P_i^v\) be the frame obtained by
applying the induced label permutation on \(U_i\). If

\[
                         v=g_{l_1}\cdots g_{l_t},
\tag{3.1}
\]

define its relaxed integral frame ledger by

\[
 \mathcal Z(v)=
 \sum_{a=1}^{t}\ \sum_{i\ne l_a}
 \left(
 e_{P_i^{g_{l_1}\cdots g_{l_a}}}
 -e_{P_i^{g_{l_1}\cdots g_{l_{a-1}}}}
 \right).
\tag{3.2}
\]

At each fixed top the summands telescope, giving

\[
 \mathcal Z(v)=
 \sum_{i=0}^{3}\left(e_{P_i^v}-e_{P_i}\right).
\tag{3.3}
\]

Applying Theorem 2.1 yields the exact endpoint ledger

\[
 \boxed{
  \mathcal Z(w)=e_{P_0^{r_0^{\pm1}}}-e_{P_0}.}
\tag{3.4}
\]

There are no duplicate owners at the endpoints: the negative shore has
one frame on \(U_0\), the positive shore has one frame on \(U_0\), and
the other three endpoint ledgers vanish. Every intermediate top also
has only one current frame. Thus (3.4) is exactly the coefficient-one
ledger one would want from a recyclable catalyst.

The qualification is that (3.2) treats each face as an available
simultaneous transposition on its current three frames. A canonical
conveyor is available only when those frames form the required coherent
two-base source packet. Section 5 proves that this lift condition fails.

## 4. There is no abstract permutation invariant left

Let

\[
                         G=\langle g_0,g_1,g_2,g_3\rangle\le S_3^4.
\tag{4.1}
\]

### Theorem 4.1 (full tetrahedral permutation image)

One has

\[
                         \boxed{G=S_3^4.}
\tag{4.2}
\]

#### Proof

The sign vector of \(g_l\) is the \(l\)-th column of \(A=J_4-I_4\).
Since \(A\) is invertible over \(\mathbb F_2\), the sign image of \(G\)
is all of \((\mathbb Z/2)^4\).

Theorem 2.1 supplies a pure \(3\)-cycle in coordinate \(0\).
Permuting the four labels supplies a pure \(3\)-cycle in every
coordinate. Therefore

\[
                         A_3^4\le G.
\tag{4.3}
\]

Given any element of \(S_3^4\), first realize its four signs by the
surjective sign map. The residual element lies in \(A_3^4\), already
contained in \(G\). This proves (4.2). \(\square\)

Consequently an invariant ruling out catalyst motion cannot depend only
on top support, transposition parity, or the final permutations of the
three variable labels. It must use the physical cyclic-frame ports or
the all-depth collar structure.

## 5. The canonical companion-port invariant

We now restore the actual two-base condition. Throughout this section
assume \(H\ge3\), and use the marked inner and outer arms of the
canonical bases \(\omega,\omega'\).

Every tetrahedral face move swaps only labels in \(V\). Hence, for each
top \(U_i\), the induced rooted cyclic order

\[
                         \kappa_i=\operatorname{ord}_C(P_i)
\tag{5.1}
\]

is invariant along any proposed walk.

On one canonical conveyor face, one top uses the \(\omega\)-base and
the other two use the same \(\omega'\)-base. After restriction from the
common core \(C\cup\{l\}\) to \(C\), let these two orders be

\[
                         P_l=\omega|_C,
                         \qquad Q_l=\omega'|_C.
\tag{5.2}
\]

They are distinct. Indeed, the companion switch moves four inner arms
of length \(H-1\), and deletion of the one label \(l\) leaves at least
three nonempty moved arm blocks.

### Lemma 5.1 (static two-colour condition)

If face \(F_l\) occurs in a literal walk, then among

\[
                         \{\kappa_i:i\ne l\}
\tag{5.3}
\]

two entries are equal to \(Q_l\) and the remaining entry is equal to
\(P_l\), with \(P_l\ne Q_l\).

If at least three different face types occur, all occurring faces use
one common unordered pair of core orders \(\{P,Q\}\).

#### Proof

The first assertion is the direct/path definition of the two-base
conveyor, followed by restriction to the permanent core \(C\).

For the second, take any three occurring faces. Their three
three-subsets of the four fixed values \(\kappa_0,\ldots,\kappa_3\)
must each have type \(2+1\), never \(3\) and never \(1+1+1\). If three
of the \(\kappa_i\) were pairwise distinct, one of those triples would
have type \(1+1+1\). If all relevant values were equal, one would have
type \(3\). Hence the four values use exactly two orders, in a
\(2+2\) split or in a \(3+1\) split whose singleton is omitted by the
unused fourth face. Every occurring triple consequently uses the same
unordered pair \(\{P,Q\}\). \(\square\)

We need one exact property of the canonical arm braid.

### Lemma 5.2 (canonical companion gaps are unique)

Fix two distinct rooted cyclic orders \(P,Q\) on the labelled set
\(C\). Suppose they are obtained by restricting a canonical
\((\omega,\omega')\) pair after deletion of at most one ordinary label.
Then the unordered pair of placeholder gaps is determined by \((P,Q)\).

#### Proof

Passing from \(\omega\) to \(\omega'\) interchanges the two positive
inner arms and interchanges the two negative inner arms. The four arms
are consecutive labelled blocks of length \(H-1\), situated on the two
sides of the two placeholder gaps. The four outer arms, each of length
\(H\), separate these inner blocks from every other possible gap.

After deletion of at most one label and under \(H\ge3\), every
placeholder collar still contains a nonempty moved block on both sides,
and the two collars remain separated by unchanged outer-arm paths. In
the pair \((P,Q)\), take the maximal directed labelled intervals whose
internal adjacencies occur in both orders but whose endpoint adjacencies
differ. The four moved inner arms are exactly the four intervals of
length at most \(H-1\) adjacent to two common gap locations; the outer
arms certify that no third gap has this property. Pairing the two
positive and the two negative intervals recovers the two gap locations,
up to exchanging them. Hence a second canonical representation of the
same labelled pair \((P,Q)\) uses the same unordered placeholder gaps.
\(\square\)

The marked outer arms are essential in this statement. Lemma 5.2 makes
no claim for an unmarked, freely reassociated multi-port template; such
a template is precisely one possible escape from the theorem.

### Theorem 5.3 (no literal tetrahedral catalyst)

No sequence of canonical two-base conveyors supported on the four faces
of one Johnson tetrahedron can restore three top frames and leave a
nonidentity frame on the fourth in a one-frame transversal.

#### Proof

First, a word isolating one top must use at least three face types. With
one face type, every touched top undergoes the same number of
transpositions. With two face types, the two tops not omitted by either
face carry isomorphic two-reflection actions, with common kernel
\(\langle g_a^2,g_b^2,(g_ag_b)^3\rangle\). The projections on the tops
omitted by \(a\) and \(b\) record, respectively, the parity of \(g_b\)
and \(g_a\). If the target is one of the two common-action tops,
identity on the other common-action top forces identity on the target.
If the target is an omitted top, identity on both common-action tops and
on the other omitted top forces both generator parities even, hence
identity on the target. Thus two face types cannot isolate a top.

By Lemma 5.1, three active face types use one fixed companion pair
\(\{P,Q\}\). By Lemma 5.2, this pair has one fixed unordered pair of
placeholder gaps, say \(\{A,B\}\), at every occurrence.

Inspect any top shared by two active faces. It contains exactly three
labels of \(V\). At an occurrence of one face, its common-core label
occupies the third, nonplaceholder port \(R\), while the other two
labels occupy \(A,B\). The move swaps the occupants of \(A,B\) and
fixes the occupant of \(R\). Every later face using the same companion
pair again has placeholders \(A,B\), so it also fixes the occupant of
\(R\). Therefore the label at \(R\), and hence the face type whose
common core it can represent, never changes.

Only that one face type can occur on the shared top. This contradicts
the existence of three active face types. Hence no isolated-top word
has a literal canonical lift. \(\square\)

The argument is owner-level and precedes all interval projection. Phase
deletion, nested tags, complementation, and the exact upper/lower
derivative identities cannot remove the obstruction.

## 6. Audit of the proposed ten-step word

The exact failure of (2.3) occurs already in its first commutator.
In the permutation relaxation the prefix

\[
                         g_1g_2g_1
\tag{6.1}
\]

is well defined. In a literal common-port realization, the first
\(g_1\) fixes label \(1\) at the third port and swaps the other two
ports. The following \(g_2\) must use a different label as its
common-core port. It changes the position of label \(1\) on exactly two
of the three tops of face \(F_1\), leaving the third unchanged. Thus the
three source frames required for the second \(g_1\) no longer share the
same companion ports. The second \(g_1\) is not applicable.

Equivalently, (3.4) is a valid telescoping identity in the unrestricted
permutation path groupoid, but its ten summands cannot simultaneously be
chosen from the canonical conveyor source monomials. No duplicate-owner
problem appears at the endpoints; the failure is earlier and sharper:
the middle source monomial does not exist.

## 7. Boundary-swap conjugation and the exact router gate

We now state the concrete reason for seeking a recyclable catalyst.
For a retained tight path with injective word

\[
                         a=(a_1,\ldots,a_{d+H-1}),
\tag{7.1}
\]

write

\[
 J_j(a)=\{a_j,\ldots,a_{j+H-1}\},
 \qquad X_j=U\setminus J_j(a).
\tag{7.2}
\]

The boundary-swap theorem interchanges \(a_1,a_2\). It fixes every
middle occurrence except phase \(2\), where it makes the literal unit
transfer

\[
                         e_Y-e_X,
 \qquad X=X_2(a),\quad Y=X_2((1\ 2)a).
\tag{7.3}
\]

At every other protected signed depth, at most two interval targets
change. Across both signs and all \(q\le H\), its complete trace
derivative therefore has support at most \(4H+O(1)\).

### Definition 7.1 (neutral phase-\(2\) router)

A neutral router for a chosen middle occurrence \((P,j)\) is a
coefficient-one path of frame tables \(R_j\) with the following
properties.

1. It sends the selected occurrence to phase \(2\) of one target row.
2. It preserves the literal target carried by that occurrence.
3. Every companion top has one current frame throughout and returns to
   its initial frame under \(R_j^{-1}\).
4. The aggregate full signed trace derivative of both the forward route
   and its applicable post-swap inverse is zero at every protected
   depth.
5. The post-swap inverse carries the changed literal occurrence back to
   the original owner slot without relabelling its set.

The inverse is required as a path on the post-swap state, not merely as
a formal negative integer combination.

### Proposition 7.2 (neutral-router conjugation principle)

Assume a neutral router exists for a selected occurrence carrying
\(X\), and assume the routed target row admits the phase-\(2\) boundary
swap from \(X\) to a prescribed Johnson neighbor \(Y\). Then

\[
                         R_j^{-1}\,B_{12}\,R_j
\tag{7.4}
\]

is a recyclable coefficient-one catalyst loop with the following exact
ledger:

1. every companion frame is restored;
2. the middle derivative is exactly \(e_Y-e_X\);
3. every top retains one frame at every time; and
4. the total collateral over all nonmiddle protected signed traces is
   at most \(4H+O(1)\).

#### Proof

The router and its inverse have zero aggregate signed trace derivative,
and they are mutually applicable on the two sides of the central swap.
Thus their companion ledgers cancel occurrence by occurrence. At the
middle, the only noncancelled event is (7.3), giving \(e_Y-e_X\).
At a fixed deletion length, a swap of the first two word positions can
affect only intervals containing exactly one of those positions, of
which there are at most two. There are \(2H+O(1)\) protected signed
depths, proving the collateral bound. \(\square\)

The proposition separates two issues that must not be conflated.
Theorem 2.2 of the boundary-swap note proves that every oriented Johnson
edge \(X\to Y\) has some phase-\(2\) realization. It does not prove
that a currently selected occurrence of \(X\) can be transported to
that realization while preserving all other owners. Definition 7.1 is
exactly that missing state-dependent assertion.

### Theorem 7.3 (one tetrahedron cannot be the neutral router)

The canonical four-top tetrahedron of Sections 1--6 cannot realize the
router in Definition 7.1 for any nontrivial change of target phase.

#### Proof

Before the central boundary swap, a nontrivial router must change the
target top's port or retained-path state while returning every companion
top. Deleting the phase marks leaves a nonidentity target frame state
unless the router was already trivial on the selected occurrence. Such
a pure-target canonical conveyor path is excluded by Theorem 5.3.

If deletion of the phase marks makes the target frame identical, then
the proposed motion is purely a change of retained phase origin. But
every canonical tetrahedral face uses the same fixed companion gaps
recovered in Lemma 5.2; it swaps their two occupants and never moves the
third port or the path boundary. It therefore cannot send phase
\(j\ne2\) to phase \(2\). \(\square\)

The abstract identity (3.4) does not contradict Theorem 7.3. It gives a
pure permutation of three labels at one top in the unrestricted path
groupoid. It contains no retained-phase transport, and Section 6 shows
that its intermediate face source monomial is not a legal canonical
packet.

Thus the concrete next lemma is stronger than a pure-top permutation
word: one needs a multi-port, flag-preserving associator whose neutral
part transports a marked occurrence to the left path boundary, whose
central step is (7.3), and whose inverse returns every auxiliary frame.
Once such a router is proved, the vertical price of a unit middle repair
is already audited as \(O(H)\), with no additional catalyst toll.

## 8. Exact boundary

Proved:

1. the full mod-two tetrahedral face/top incidence matrix and its
   determinant;
2. the ten-step word (2.3), restoring three top permutations and leaving
   a nonzero \(3\)-cycle on the fourth;
3. its exact telescoping integral frame ledger with coefficient-one
   endpoints;
4. the equality of the abstract face group with \(S_3^4\), ruling out
   every support/permutation-only invariant;
5. the static permanent-core two-colour condition for literal
   conveyors;
6. uniqueness of the canonical companion port pair; and
7. impossibility of a literal recyclable catalyst on one Johnson
   tetrahedron;
8. the neutral-router conjugation principle for the boundary swap, with
   exact middle derivative \(e_Y-e_X\) and \(O(H)\) trace collateral;
   and
9. impossibility of obtaining that router from one canonical
   tetrahedron.

Not proved:

1. a multi-port companion pair in which the placeholder gaps themselves
   can move while the all-depth derivative remains exact;
2. a lift of the abstract monodromy using an auxiliary fifth top or a
   second permanent-core order row;
3. a star-parity invariant for all larger changing-core carriers;
4. a neutral all-depth occurrence router sending an arbitrary current
   middle occurrence to phase \(2\); and
5. coefficient one globally.

The smallest abstract carrier is therefore sufficient, but the smallest
canonical physical carrier is not. The next exact target is no longer a
parity lemma. It is a ported associator: a finite auxiliary-row packet
which realizes the pure-top word (2.3) while changing the canonical
companion gap pair between successive face types and returning every
auxiliary owner exactly once. For the boundary-swap application it must
also transport the retained phase flag, so that conjugation by the
associator leaves only (7.3) and its audited \(O(H)\) trace collar.
