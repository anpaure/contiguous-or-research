# The fixed-Dyck-transversal exact-factor fibre: anchored correction, legal moves, and overlay connectivity

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let

\[
 J=[2r],\qquad N=J\sqcup\{\infty\},\qquad
 \mathcal D_r=\{P\in\tbinom Jr:\mathbf 1_P\text{ is Dyck}\}.
 \tag{0.1}
\]

There are two different fibres which must not be conflated.

* A **weak** \(\mathcal D_r\)-transversal factor has exactly one member of
  \(\mathcal D_r\) on every wreath row.
* An **anchored** \(\mathcal D_r\)-transversal factor has, after cutting
  every row at the distinguished coordinate \(\infty\), the complementary
  endpoints \(P,J\setminus P\) for a unique \(P\in\mathcal D_r\).

Anchored implies weak, but the converse is false already for \(r=2\).
The state/adjacent-union criterion with fixed endpoints describes the
anchored fibre, not the whole weak fibre.  This matters for constant one:
only the anchored condition permits row-by-row substitution into a fixed
outer Dyck context.

The principal positive result is an exact connectivity theorem.  Overlay
any two weak transversal exact factors, or any two anchored transversal
exact factors, by ownership of the odd-graph vertices.  Every connected
overlay component may be switched independently.  All intermediate cube
vertices remain in the same respective fibre.  Consequently the graph of
the anchored fibre under connected ownership-component switches is
connected, with distance at most
\(\lfloor\operatorname {Cat}_r/2\rfloor\) nontrivial switches between any
two members after common rows are cancelled.

The oriented Dyck set-system has the exact coordinate automorphism group

\[
 \operatorname {Aut}(\mathcal D_r)
 =\langle(2,3),(4,5),\ldots,(2r-2,2r-1)\rangle
 \cong C_2^{r-1}.
\]

Its coordinate-component moves are legal and anchored, but preserve exact
row-orbit and target-orbit masses. Equations (4B.7)--(4B.8) give the
resulting sharp integer and PSD obstruction floors. No macroscopic lower
bound for the canonical orbit floor is proved, so this is a test rather
than a separation theorem.

Anchoring still leaves a large local move space. The canonical
\((2\,3)\)-comparison has
\((1/12+o(1))\operatorname {Cat}_r\) independently switchable anchored
components, and a positive-density subfamily has only \(O(\log r)\) rows
per component. Endpoint anchoring therefore does not isolate MSW.

It follows that **no invariant preserved by arbitrary legal
interaction-component switches can separate the canonical MSW factor from
all shadow-dispersing anchored factors**.  This is unconditional as an
invariant statement: if such a target factor exists, it lies in the same
component.  Moreover the known anchored octahedral rectangle is already a
single legal move from MSW and has nonzero rooted child-shadow action in a
parent context.

For the narrower generator consisting only of two-row one-phase switches,
there is a genuine invariant.  Every nontrivial such switch is forced to
be the four-coordinate octahedral rectangle, and it preserves, root by
root, the matching between deleted and inserted coordinates along the
complementary Johnson geodesic.  This invariant proves rigidity of that
small move class, but it cannot be the requested shadow-separating
invariant, because the octahedral rectangle itself changes a rooted child
shadow while preserving the invariant.

The remaining coefficient-one gate is therefore quantitative rather than
topological: construct an anchored target with sufficiently dispersed
shadows, or exhibit bounded-support component moves leading to one with a
monotone cap-tail estimate.  The connectivity proof does not construct the
unknown target and gives no bound on component support.

Finally, the certified \(r=4\) nonlocal Haar trade admits an explicit
coordinate conjugation into the fixed **weak**
\(\mathcal D_4\)-transversal fibre. It preserves the first shadow and
changes the second. Its unique Dyck roots are often internal, however, so
this certificate does not lie in the corrected anchored fibre under the
verified embedding.

## 1. Cutting a wreath at infinity

Write

\[
 \mathcal L=\binom Jr,\qquad
 \mathcal U=\binom J{r+1},\qquad
 B=|\mathcal D_r|=\operatorname {Cat}_r.
 \tag{1.1}
\]

Cut a minimum odd cycle in \(KG(N,r)\) at the unique edge whose two
endpoints avoid \(\infty\) and lie on opposite sides of \(\infty\) in its
cyclic order.  Its vertices can be written

\[
 X_0,Z_0,X_1,Z_1,\ldots,Z_{r-1},X_r,
 \tag{1.2}
\]

where

\[
 X_t\in\mathcal L,\qquad
 |X_t\triangle X_{t+1}|=2,\qquad
 X_r=J\setminus X_0,
 \tag{1.3}
\]

and

\[
 Y_t=X_t\cup X_{t+1}\in\mathcal U,
 \qquad
 Z_t=\{\infty\}\cup(J\setminus Y_t).
 \tag{1.4}
\]

Conversely, (1.3)--(1.4) reconstruct the odd cycle, including its closing
edge \(X_rX_0\).

Because a Johnson path from an \(r\)-set to its complement has distance
\(r\), every path in (1.3) is a geodesic.  Thus there are unique orders

\[
 a_1,\ldots,a_r\text{ of }X_0,
 \qquad
 b_1,\ldots,b_r\text{ of }J\setminus X_0
 \tag{1.5}
\]

such that

\[
 X_t=X_0\setminus\{a_1,\ldots,a_t\}
            \cup\{b_1,\ldots,b_t\}.
 \tag{1.6}
\]

No deleted coordinate is reinserted and no inserted coordinate is later
deleted.

### Definition 1.1 (weak and anchored fibres)

An exact wreath factor \(F\) is **weakly \(\mathcal D_r\)-transversal** if
every row contains exactly one state in \(\mathcal D_r\).

It is **anchored \(\mathcal D_r\)-transversal** if its rows can be indexed
by \(P\in\mathcal D_r\) so that their infinity-cut traces satisfy

\[
 X_0(P)=P,\qquad X_r(P)=J\setminus P.
 \tag{1.7}
\]

Since a nonempty Dyck word begins with \(1\), while its complement begins
with \(0\), \(\mathcal D_r\cap\{J\setminus P:P\in\mathcal D_r\}=\varnothing\).
Hence the orientation in (1.7) is unambiguous.

## 2. The corrected fibre theorem

### Theorem 2.1 (exact weak-transversal trace model)

For every \(r\ge1\), weakly \(\mathcal D_r\)-transversal exact factors are
equivalent to families

\[
 \bigl(X_0(P),\ldots,X_r(P);h(P)\bigr),
 \qquad P\in\mathcal D_r,\quad 0\le h(P)\le r,
 \tag{2.1}
\]

satisfying all of the following:

1. \(X_t(P)\in\mathcal L\), consecutive states are Johnson adjacent, and
   \(X_r(P)=J\setminus X_0(P)\);
2. \(X_{h(P)}(P)=P\);
3. the state ledger is exact,
   \[
   \biguplus_{P\in\mathcal D_r}\biguplus_{t=0}^r
        \{X_t(P)\}=\mathcal L;
   \tag{2.2}
   \]
4. the adjacent-union ledger is exact,
   \[
   \biguplus_{P\in\mathcal D_r}\biguplus_{t=0}^{r-1}
        \{X_t(P)\cup X_{t+1}(P)\}=\mathcal U.
   \tag{2.3}
   \]

The anchored fibre is precisely the subfamily for which every trace can
be oriented with

\[
 h(P)=0,qquad X_0(P)=P,qquad X_r(P)=J\setminus P.
 \tag{2.4}
\]

#### Proof

Cut every row of a weak transversal factor at \(\infty\), and index it by
its unique Dyck state \(P\).  Equations (1.2)--(1.4) give Conditions 1--2.
Exact ownership of the vertices avoiding \(\infty\) gives (2.2).
Complementation in \(J\), followed by adjoining \(\infty\), is a bijection

\[
 \mathcal U\longrightarrow
 \{Z\in\tbinom Nr:\infty\in Z\},
 \qquad Y\longmapsto\{\infty\}\cup(J\setminus Y),
 \tag{2.5}
\]

so exact ownership of the vertices containing \(\infty\) is exactly
(2.3).

Conversely Conditions 1, 3, and 4 reconstruct, by (1.4), disjoint odd
cycles covering every vertex of \(KG(N,r)\) once.  Condition 2 places all
\(B\) distinct Dyck states into the \(B\) rows.  The state ledger prevents
any repeated Dyck state, so each row contains exactly its displayed one.
This is weak transversality.  Finally, a row is anchored exactly when its
displayed Dyck state is an infinity-cut endpoint; orienting that endpoint
first gives (2.4). \(\square\)

Thus a fixed-root state/union-ledger theorem is an **anchored** theorem.
It is not an if-and-only-if theorem for weak transversality.

### Proposition 2.2 (the distinction is real at \(r=2\))

Let \(J=[4]\) and \(\mathcal D_2=\{12,13\}\).  The two traces

\[
 14,12,23,
 \qquad
 13,34,24
 \tag{2.6}
\]

form a weakly \(\mathcal D_2\)-transversal exact factor, but not an anchored
one.

#### Proof

The six displayed states are all members of \(\binom{[4]}2\), once each.
Their adjacent unions are

\[
 124,123,134,234,
 \tag{2.7}
\]

which are all members of \(\binom{[4]}3\), once each.  The endpoints in
each row are complementary.  Theorem 2.1 therefore gives an exact factor.
The first row contains the unique Dyck state \(12\), and the second the
unique Dyck state \(13\), so it is weakly transversal.  But \(12\) is
internal in its row; its infinity-cut complementary endpoint \(34\) is
not the other endpoint of that row.  Hence no orientation makes that row
anchored at \(12\). \(\square\)

This example cannot be inserted row by row into a canonical size-two hole
whose prescribed boundary states are \(12,34\).

### Theorem 2.3 (corrected context-substitution interface)

An exact local factor can replace the canonical traces in an aligned
size-\(r\) hole by the direct rowwise substitution of the plateau
architecture if it is anchored \(\mathcal D_r\)-transversal. Conversely,
anchoring is necessary for that direct substitution with the prescribed
row boundaries \(P,J\setminus P\).

#### Proof

For an anchored factor, orient the row indexed by \(P\) as

\[
 P=X_0(P),X_1(P),\ldots,X_r(P)=J\setminus P.
 \tag{2.8}
\]

After adjoining the fixed exterior coordinates of the hole, (2.8) has
exactly the two canonical boundary states. The state ledger (2.2)
preserves every local middle owner, and the union ledger (2.3), through
the bijection (2.5), preserves every owner containing the interface
coordinate \(\infty\). Hence the replacement is a literal exact ambient
factor.

Conversely, a direct rowwise replacement of the canonical row labelled
\(P\) must enter and leave through \(P\) and \(J\setminus P\).
These must therefore be the two endpoints of one infinity-free trace,
which is precisely anchoring. A weak transversal whose unique \(P\) is
internal, as in Proposition 2.2, does not meet this interface. \(\square\)

This corrects the scope of the transversal context-substitution theorem:
unique Dyck incidence somewhere on a row is not enough.

### Proposition 2.4 (the anchored \(r=2\) fibre)

The anchored \(\mathcal D_2\)-transversal fibre has exactly two factors:

\[
\begin{array}{c|cc}
&\text{row rooted at }12&\text{row rooted at }13\\ \hline
F^-&12,14,34&13,23,24\\
F^+&12,23,34&13,14,24.
\end{array}
\tag{2.9}
\]

They are joined by the one-phase octahedral rectangle.

#### Proof

The internal state of the path \(12\to34\) must be a common Johnson
neighbour of its endpoints. The possibilities are \(13,14,23,24\), but
\(13,24\) are the prescribed endpoints of the other rooted path and
cannot be reused. Thus it is \(14\) or \(23\), and exact state ownership
forces the other path to use the remaining choice. In either case the
four adjacent unions are \(123,124,134,234\), once each. These are exactly
the two rows of (2.9), and swapping their internal states exchanges them.
\(\square\)

## 3. Exact phasewise moves in the anchored fibre

Fix an anchored factor and write its traces as in (2.4).

### Theorem 3.1 (slab replacement criterion)

Choose rows \(Q\subseteq\mathcal D_r\) and a phase slab
\(a\le t\le b\).  Keep the two boundary states fixed row by row and replace
the internal states by \(X'_t(P)\).  The replacement is another anchored
exact factor if and only if

1. every new consecutive pair is Johnson adjacent;
2. the multiset of states removed from the slab equals the multiset
   inserted;
3. the multiset of adjacent unions removed from the slab equals the
   multiset inserted.

If

\[
 X'_t(P)=X_t(f_t(P)),
 \tag{3.1}
\]

where every \(f_t\) is a permutation of \(Q\) and the boundary
permutations are the identity, Condition 2 is automatic.  Condition 3 is
still indispensable and is required only after aggregation over the
whole slab, not separately at every phase.

#### Proof

The fixed boundary states glue the new traces to the unchanged portions
and preserve (2.4).  Condition 1 gives paths.  Conditions 2--3 are exactly
the two ledger discrepancies in (2.2)--(2.3).  Theorem 2.1 proves
sufficiency and necessity.  Under (3.1), the state multiset at every phase
is merely permuted. \(\square\)

There is a useful concrete version for phasewise alternating cycles.

### Corollary 3.2 (two-cut block-permutation move)

Let \(0\le a<b\le r\), with \(b\ge a+2\), let \(Q\) be a set of rows,
and let \(\pi\in\operatorname {Sym}(Q)\).  Define

\[
 X'_t(P)=
 \begin{cases}
 X_t(\pi P),&P\in Q, a<t<b,\\
 X_t(P),&\text{otherwise}.
 \end{cases}
 \tag{3.2}
\]

Then (3.2) is a legal anchored move if and only if all entry and exit
pairs

\[
 X_a(P)\sim_J X_{a+1}(\pi P),qquad
 X_{b-1}(\pi P)\sim_J X_b(P)
 \tag{3.3}
\]

are legal and

\[
\begin{aligned}
 \biguplus_{P\in Q}
 \{&X_a(P)\cup X_{a+1}(\pi P),
     X_{b-1}(\pi P)\cup X_b(P)\}\\
 &={}
 \biguplus_{P\in Q}\{Y_a(P),Y_{b-1}(P)\}.
\end{aligned}
\tag{3.4}
\]

All internal transitions of the moved block are old transitions of row
\(\pi P\), so their union colours are only permuted.  Thus (3.3)--(3.4)
are the complete boundary test.  Taking \(\pi\) to be a cycle gives a
literal phasewise alternating-cycle move.  Taking \(b=a+2\) and \(\pi\)
to be a transposition gives a two-row one-phase move.

## 4. Classification of every elementary two-row move

For an \((r-2)\)-set \(C\) and distinct elements \(i,j\notin C\), write
\(Cij=C\cup\{i,j\}\).

### Lemma 4.1 (common neighbours at Johnson distance two)

If

\[
 L=Cab,qquad R=Ccd,qquad |C|=r-2,
 \tag{4.1}
\]

with \(a,b,c,d\) distinct, then the common Johnson neighbours of \(L,R\)
are exactly

\[
 Cac,\quad Cad,\quad Cbc,\quad Cbd.
 \tag{4.2}
\]

#### Proof

A common neighbour has intersection size \(r-1\) with both \(L\) and
\(R\).  It must therefore contain all of \(C\), one of \(a,b\), and one
of \(c,d\).  These four choices work, and no other choice has the required
two intersection sizes. \(\square\)

### Theorem 4.2 (octahedral normal form)

Consider a nonidentity two-row one-phase swap in an anchored exact factor:

\[
 L,A,R,qquad L',B,R'
 \quad\longmapsto\quad
 L,B,R,qquad L',A,R'.
 \tag{4.3}
\]

Assume the four new adjacencies are Johnson edges and the four affected
adjacent-union colours have the same multiset before and after.  Then,
after relabelling four coordinates and possibly reversing the second row,
there is a common \((r-2)\)-set \(C\) for which

\[
\begin{array}{c|ccc}
\text{old row 1}&Cab&Cac&Ccd\\
\text{old row 2}&Cad&Cbd&Cbc
\end{array}
\quad\longmapsto\quad
\begin{array}{c|ccc}
\text{new row 1}&Cab&Cbd&Ccd\\
\text{new row 2}&Cad&Cac&Cbc.
\end{array}
\tag{4.4}
\]

The old and new adjacent-union multisets are both

\[
 \{Cabc,Cabd,Cacd,Cbcd\}.
 \tag{4.5}
\]

Thus every elementary move is precisely an affine copy of the
four-coordinate octahedral rectangle.

#### Proof

Because the first row is a subpath of a complementary length-\(r\)
geodesic, its two consecutive exchanges use distinct deleted and inserted
coordinates.  Hence \(d_J(L,R)=2\).  Write

\[
 L=Cab,qquad R=Ccd,qquad A=Cac
 \tag{4.6}
\]

after relabelling.  Cross legality says that \(B\) is another common
neighbour of \(L,R\).  By Lemma 4.1 it is one of
\(Cad,Cbc,Cbd\).

Suppose first that \(B=Cad\).  The first row's two old union colours are
\(Cabc,Cacd\), while its new colours are \(Cabd,Cacd\).  Thus it removes
\(Cabc\) and inserts \(Cabd\).

Now \(A=Q c\) and \(B=Q d\), where \(Q=C\cup\{a\}\).  A common Johnson
neighbour \(S\) of these adjacent sets is of exactly one of the forms

\[
 S=Qe\quad(e\notin Q\cup\{c,d\}),
 \qquad
 S=(Q\setminus\{q\})\cup\{c,d\}\quad(q\in Q).
 \tag{4.7}
\]

In the second form, \(S\cup A=S\cup B\).  In the first form, changing
the middle state from \(B\) to \(A\) changes the union colour from
\(Qde\) to \(Qce\).  Equality of the aggregate four-colour multisets
therefore requires exactly one second-row boundary of the first type with
\(e=b\), in order to replace \(Cabd\) by \(Cabc\).  But that boundary
state is \(Qb=Cab=L\), already used in the first row.  This contradicts
the exact state ledger.  Hence \(B\ne Cad\).  The symmetric argument at
the other side gives \(B\ne Cbc\).

Therefore \(B=Cbd\), opposite \(A\) in (4.2).  Cross legality on the
second row says that \(L',R'\) are common neighbours of the opposite sets
\(A,B\).  Lemma 4.1 again gives the four possibilities

\[
 Cab,Cad,Cbc,Ccd.
 \tag{4.8}
\]

Exact state ownership excludes \(Cab=L\) and \(Ccd=R\), so the two
distinct boundary states are \(Cad,Cbc\), in one of the two orders.  This
is (4.4).  Direct union gives (4.5). \(\square\)

### Definition 4.3 (rootwise exchange matching)

For an anchored row rooted at \(P\), write its geodesic as in (1.5)--(1.6)
and define

\[
 \phi_F(P):P\longrightarrow J\setminus P,
 \qquad \phi_F(P)(a_t)=b_t.
 \tag{4.9}
\]

This is independent of the order in which the \(r\) exchange pairs are
performed.

### Corollary 4.4 (elementary-rectangle invariant)

Every two-row one-phase switch preserves \(\phi_F(P)\) for each affected
root \(P\).  Hence

\[
 \Phi(F)=\bigl(\phi_F(P)\bigr)_{P\in\mathcal D_r}
 \tag{4.10}
\]

is invariant under every sequence of elementary rectangle switches.

#### Proof

In the first row of (4.4), the old two exchanges are

\[
 b\mapsto c,qquad a\mapsto d,
 \tag{4.11}
\]

while the new row performs the same two exchange pairs in the reverse
order.  The same statement holds in the second row.  All other exchanges
are unchanged. \(\square\)

The tuple \(\Phi\) is a real obstruction to connectivity of the narrow
rectangle graph whenever two fibre members with different tuples are
present.  It is not an obstruction to shadow action: reordering exchange
pairs changes interval intersections even though their matching is fixed.

## 4A. Exact coordinate automorphisms of the Dyck transversal

Coordinate relabelling supplies another natural, but very small,
reconfiguration class.  Its group can be determined without a catalogue.
For \(1\le i\le2r\), put

\[
 a_i=|\{P\in\mathcal D_r:i\in P\}|.
 \tag{4A.1}
\]

### Theorem 4A.1 (Dyck set-system automorphism group)

For every \(r\ge1\),

\[
 \operatorname {Aut}(\mathcal D_r)
 =\left\langle(2,3),(4,5),\ldots,(2r-2,2r-1)\right\rangle
 \cong C_2^{\,r-1}.
 \tag{4A.2}
\]

For \(1\le j\le r-1\), the exact frequency identities are

\[
 a_{2j}=a_{2j+1},
 \qquad
 a_{2j}-a_{2j+2}
   =\operatorname {Cat}_j\operatorname {Cat}_{r-j-1}.
 \tag{4A.3}
\]

#### Proof

Immediately before position \(2j\), a Dyck path has odd nonnegative
height, hence height at least one.  Interchanging the steps at positions
\(2j,2j+1\) therefore preserves nonnegativity: the only nontrivial change
is between \(10\) and \(01\), and the latter first lowers a height which
is at least one.  Thus each transposition in (4A.2) preserves
\(\mathcal D_r\), proving the first identity in (4A.3).

Use that identity to write

\[
 a_{2j}-a_{2j+2}=a_{2j+1}-a_{2j+2}.
 \tag{4A.4}
\]

Swap the adjacent steps at positions \(2j+1,2j+2\).  Paths having local
pattern \(10\) pair with paths having pattern \(01\), except when the
height after \(2j\) steps is zero; in that case \(01\) is forbidden.  An
unpaired path is exactly a Dyck prefix of semilength \(j\), followed by
\(10\), followed by a Dyck suffix of semilength \(r-j-1\).  Their number
is the product in (4A.3).

The frequency classes are consequently

\[
 \{1\},\{2,3\},\{4,5\},\ldots,
 \{2r-2,2r-1\},\{2r\},
 \tag{4A.5}
\]

and their frequencies are strictly decreasing.  Here \(a_1=\operatorname
{Cat}_r>a_2\) for \(r\ge2\), since the paths beginning \(10\) are counted
by \(\operatorname {Cat}_{r-1}>0\), and \(a_{2r}=0\); all intermediate
strict inequalities are (4A.3).  Every set-system automorphism preserves
coordinate frequencies, so it fixes the singleton classes and can only
interchange the two coordinates in each displayed pair.  The first
paragraph shows that all these interchanges, independently, are genuine
automorphisms.  The case \(r=1\) has an empty generating list and is
trivial. \(\square\)

Thus coordinate automorphisms alone cannot supply a large Catalan
reconfiguration group.  This is independent of the much stronger
ownership-component connectivity proved next.

## 4B. Legal coordinate-component moves and their exact orbit floor

Put

\[
 \Gamma_r=\operatorname {Aut}(\mathcal D_r)
 =\langle(2,3),(4,5),\ldots,(2r-2,2r-1)\rangle,
 \tag{4B.1}
\]

acting on \(J\) and fixing \(\infty\). For an anchored factor \(F\) and
\(g\in\Gamma_r\), make a graph on the **source rows** of \(F\) by joining
the owner of \(T\) to the owner of \(gT\), for every odd-graph vertex
\(T\). Equivalently one may use both the \(X\)-tokens and \(Y\)-tokens in
the cut model.

### Theorem 4B.1 (oriented-Dyck coordinate-component switch)

If \(K\) is a union of components of this source graph, then

\[
 F'=(F\setminus K)\cup gK
 \tag{4B.2}
\]

is an anchored \(\mathcal D_r\)-transversal exact factor.

#### Proof

Let \(\mathcal V(K)\) be the set of odd-graph vertices owned by rows of
\(K\). Component closure says that \(T\in\mathcal V(K)\) if and only if
\(gT\in\mathcal V(K)\). Hence \(g\mathcal V(K)=\mathcal V(K)\), so the
rows \(gK\) partition exactly the vertex set formerly partitioned by
\(K\). Rows outside \(K\) are unchanged, proving exact factorhood.

If a row of \(K\) has endpoints \(P,J\setminus P\), its image has endpoints
\(gP,J\setminus gP\). Since \(g\mathcal D_r=\mathcal D_r\), the image row
is anchored. Exact ownership then gives one anchored row for every Dyck
root. \(\square\)

These are intrinsic heat-bath moves: unlike Theorem 5.1 below, their
comparison factor is the prescribed coordinate image \(gF\).

They have a genuine invariant. Let \(\mathcal T_q\) be any target set on
which \(\Gamma_r\) acts, and suppose each row \(C\) has an additive,
coordinate-equivariant contribution \(v_q(C)\in\mathbb Z_{\ge0}^{\mathcal
T_q}\). This includes every fixed-depth lower-shadow histogram. Put

\[
 \mu_q(F)=\sum_{C\in F}v_q(C).
 \tag{4B.3}
\]

### Theorem 4B.2 (coordinate-orbit census and exact integer floor)

Along every sequence of moves (4B.2), the following quantities are
invariant:

\[
 \#\{C\in F:C\in\mathcal O\}
 \quad\text{for each }\Gamma_r\text{-orbit of rows }\mathcal O,
 \tag{4B.4}
\]

and

\[
 M_O(F):=\sum_{T\in O}\mu_q(F;T)
 \quad\text{for each }\Gamma_r\text{-orbit }O\subseteq\mathcal T_q.
 \tag{4B.5}
\]

Consequently, let \(a=|O|\), write

\[
 M_O=at+u,\qquad 0\le u<a,
 \tag{4B.6}
\]

and fix an integer floor \(c\). Every reachable integral load vector
satisfies

\[
\begin{aligned}
 \sum_{T\in O}(\mu_q(T)-c)(\mu_q(T)-c-1)
 \ge \Phi_{a,c}(M_O)
 :={}&(a-u)(t-c)(t-c-1)\\
 &+u(t+1-c)(t-c).
\end{aligned}
 \tag{4B.7}
\]

For a real mean \(\lambda\), it also satisfies

\[
 \sum_{T\in\mathcal T_q}(\mu_q(T)-\lambda)^2
 \ge
 \sum_{O\in\mathcal T_q/\Gamma_r}
 \frac{(M_O-\lambda|O|)^2}{|O|}.
 \tag{4B.8}
\]

#### Proof

In (4B.2), every removed row \(C\) is replaced by \(gC\), which lies in
the same \(\Gamma_r\)-orbit. This proves (4B.4). Equivariance gives
\(v_q(gC;gT)=v_q(C;T)\), so summing over a target orbit proves (4B.5).

The integer function \(x\mapsto(x-c)(x-c-1)\) has constant positive
second difference. Among \(a\) integers of sum \(M_O\), its sum is
therefore minimized when the entries differ by at most one, namely at
\(a-u\) copies of \(t\) and \(u\) copies of \(t+1\). This is (4B.7).
Equation (4B.8) is orthogonal projection onto the subspace of
\(\Gamma_r\)-orbit-constant vectors. \(\square\)

Thus (4B.7) is an exact obstruction test for the oriented-Dyck
coordinate-component class. If its canonical value is of order \(W\) on
a required depth window, this entire move class is incapable of
coefficient-one shadow dispersion. That canonical orbit floor has not
been evaluated here, so no such separation is claimed. General
comparison-component moves from Section 5 do not preserve (4B.4)--(4B.5)
and can escape this obstruction.

The coordinate reversal \(\iota(i)=2r+1-i\) maps
\(\mathcal D_r\) to its complementary anti-Dyck endpoint family and
therefore also preserves **anchored** admissibility after reversing each
row orientation. If reversal-component moves are admitted, one must
replace \(\Gamma_r\) in the orbit floor by
\(\langle\Gamma_r,\iota\rangle\). No larger anchored coordinate symmetry
group is asserted.

## 4C. A positive-density anchored cube at the canonical factor

The exact MSW component decomposition proved in
MSW_TRANSPOSITION_COMPONENTS.md and
CATALAN_SEAM_ABSORPTION_OBSTRUCTION.md for

\[
 \tau=(2,3)\in\Gamma_r
 \tag{4C.1}
\]

therefore lies wholly inside the anchored fibre. Its components are
indexed by

\[
 0\le j\le r-2,\qquad R\in\mathcal D_{r-j-2};
 \tag{4C.2}
\]

for fixed \((j,R)\), the number of rows on either shore is

\[
 s_j=\operatorname {Cat}_j+\operatorname {Cat}_{j+1}.
 \tag{4C.3}
\]

Thus the anchored support face between \(F_{\rm MSW}\) and
\(\tau F_{\rm MSW}\) is a Boolean cube of dimension

\[
 \sum_{j=0}^{r-2}\operatorname {Cat}_{r-j-2}
 =\sum_{k=0}^{r-2}\operatorname {Cat}_k
 =\left(\frac1{12}+o(1)\right)\operatorname {Cat}_r.
 \tag{4C.4}
\]

In particular, the \(j=0\) layer consists of

\[
 \operatorname {Cat}_{r-2}
 =\left(\frac1{16}+O(r^{-1})\right)\operatorname {Cat}_r
 \tag{4C.5}
\]

independent two-row rectangles rooted at

\[
 1100R,\qquad1010R,\qquad R\in\mathcal D_{r-2}.
 \tag{4C.6}
\]

Their first-lower-shadow effects are disjoint elementary four-target
squares. Hence endpoint anchoring neither isolates MSW nor freezes its
first shadow.

There is also a bounded-degree positive-density truncation. If
\(J=J(r)\to\infty\) slowly and only components with \(j\le J\) are used,
then the number of cube coordinates remains

\[
 \left(\frac1{12}+o(1)\right)\operatorname {Cat}_r,
 \tag{4C.7}
\]

the number of rows appearing on either shore is

\[
 \left(\frac38+o(1)\right)\operatorname {Cat}_r,
 \tag{4C.8}
\]

and the largest component has
\(\operatorname {Cat}_J+\operatorname {Cat}_{J+1}\) rows. Choosing

\[
 J=\lfloor\log_4\log r\rfloor
 \tag{4C.9}
\]

makes this \(O(\log r)\). Thus a positive proportion of canonical rows
already admits logarithmic-support anchored switches.

This does not prove shadow dispersion. In the fixed comparison face the
top component has

\[
 \operatorname {Cat}_{r-2}+\operatorname {Cat}_{r-1}
 =\left(\frac5{16}+o(1)\right)\operatorname {Cat}_r
 \tag{4C.10}
\]

rows per shore, so every path confined to that face from
\(F_{\rm MSW}\) to \(\tau F_{\rm MSW}\) must flip a component of that
size. An excursion through other anchored factors may avoid it.

## 5. Ownership-component connectivity of the full fibre

Let \(F,G\) be two exact wreath factors on \(N\).  Their **ownership
overlay** \(\Gamma(F,G)\) is the bipartite multigraph whose left vertices
are rows of \(F\), whose right vertices are rows of \(G\), and which has,
for every \(S\in\binom Nr\), one edge labelled \(S\) joining the unique
row of \(F\) containing \(S\) to the unique row of \(G\) containing
\(S\).

Equivalently, in the cut-trace model put in one edge for every state token
\(X\in\mathcal L\), and one edge for every adjacent-union token
\(Y\in\mathcal U\), the latter joining the owners of
\(\{\infty\}\cup(J\setminus Y)\).  Thus the overlay sees both exact
ledgers simultaneously; omitting the \(Y\)-edges would not certify an
exact odd-graph factor.

Every overlay vertex has degree \((r+1)+r=2r+1\).

### Theorem 5.1 (component cube inside the weak and anchored fibres)

Let \(F,G\) both belong to the weak \(\mathcal D_r\)-transversal fibre, or
both belong to the anchored \(\mathcal D_r\)-transversal fibre.  Let
\(K_1,\ldots,K_c\) be the connected components of \(\Gamma(F,G)\), after
discarding components on which the two sides are the same row.  For every
\(I\subseteq[c]\), select the complete \(G\)-side of \(K_i\) when
\(i\in I\), the complete \(F\)-side when \(i\notin I\), and keep every
common row.  Call the resulting row family \(F_I\).  Then:

1. every \(F_I\) is a literal integral exact wreath factor;
2. in the weak case, every \(F_I\) is weakly
   \(\mathcal D_r\)-transversal;
3. in the anchored case, every \(F_I\) is anchored
   \(\mathcal D_r\)-transversal;
4. changing one coordinate of \(I\) is one connected
   ownership-component switch;
5. \(F_\varnothing=F\), \(F_{[c]}=G\), and
   \(c\le\lfloor B/2\rfloor\);
6. these are all exact factors whose rows are contained in the row support
   \(F\cup G\).

Consequently both the weak and anchored fibres are connected under legal
connected ownership-component switches.

#### Proof

Fix one overlay component \(K\), with \(u\) left rows and \(v\) right
rows.  Counting its labelled edges from its two shores gives

\[
 (2r+1)u=|E(K)|=(2r+1)v,
 \tag{5.1}
\]

so \(u=v\).  More strongly, the union of the odd-graph vertices owned by
the left rows of \(K\) equals the union owned by its right rows: an edge
label \(S\) lies in \(K\) from either owner simultaneously.  Either shore
therefore partitions the same set of vertices.  Independent shore choices
over the components partition all of \(\binom Nr\) once and consist of
complete wreath rows.  This proves exact integral factorhood.

In the weak case, every selected row is a row of \(F\) or \(G\), hence
contains exactly one Dyck state.  Exact ownership prevents repetitions,
so weak transversality is retained.  Moreover the state-token edge
labelled \(P\) joins the unique \(F\)-row containing \(P\) to the unique
\(G\)-row containing \(P\).  Thus the Dyck-root blocks on the two shores
of every component agree in the weak case as well.

Now assume the factors anchored.  For each \(P\in\mathcal D_r\), let
\(F_P,G_P\) be their rows with infinity-cut endpoints
\(P,J\setminus P\).  The overlay edge labelled \(P\) joins \(F_P\) to
\(G_P\).  Hence these two rows lie in the same component.  In each
component the sets of root labels on the two shores are therefore equal.
Choosing either complete shore selects exactly one row with endpoints
\(P,J\setminus P\) for every root label belonging to that component.
This proves anchoring of every cube vertex.

If two cube vertices differ only at \(K_i\), their overlay restricted to
the rows which change is the original connected graph \(K_i\); all rows
outside are common.  Thus this is exactly one connected component switch.

To classify every support-contained hybrid, first cancel common rows.  For
a row \(u\) of \(F\) and a row \(v\) of \(G\), let
\(x_u,y_v\in\{0,1\}\) record whether that row is selected.  Exact ownership
of the token labelling an overlay edge \(uv\) is precisely

\[
                         x_u+y_v=1.                       \tag{5.3}
\]

Along a connected component, (5.3) forces all left indicators to have one
common value and every right indicator to have its complement.  Thus an
exact support-contained hybrid chooses exactly one complete shore of every
component.

Finally, a component containing one left root also contains one right
root.  Its two rows would own exactly the same \(2r+1\) odd-graph
vertices.  A minimum odd cycle is induced: a chord would split it into
two cycles, one of which is an odd cycle shorter than the odd girth
\(2r+1\).  Hence the common vertex set determines the same wreath row,
contrary to cancellation.  Every remaining component contains at least
two roots.  Their root blocks are disjoint, so
\(c\le\lfloor B/2\rfloor\).  The endpoint statements are immediate.
\(\square\)

### Corollary 5.2 (root-block context substitution)

In the anchored case, every component \(K_i\) carries the same root block

\[
 \mathcal R_i=\{P:F_P\in K_i\}
             =\{P:G_P\in K_i\}
 \tag{5.2}
\]

on its two shores.  Therefore the switch can be installed inside a fixed
outer hole without changing any row's two prescribed boundary states.
Every intermediate cube vertex is a legal exact context substitute.

### Corollary 5.3 (no interaction-component invariant)

Let \(I\) be any quantity on the anchored fibre which is unchanged by a
connected ownership-component switch.  Then \(I\) is constant on the
entire anchored fibre.

In particular, for any nonempty class \(\mathscr S\) of anchored factors
defined by a shadow-dispersion condition, \(I\) cannot separate the
canonical MSW factor from every member of \(\mathscr S\).

#### Proof

Join MSW to any \(G\in\mathscr S\) by the component path in Theorem 5.1
and telescope invariance along the path. \(\square\)

This conclusion includes nonlinear, modular, homological, and rowwise
statistics.  They may obstruct a smaller prescribed generator set, but
not the full legal comparison-component move class.

## 6. The canonical rectangle already crosses a shadow boundary

For completeness, the shadow-active anchored move can be written without
any existence assumption.  Let \(s\ge2\), put

\[
 R=\{5,7,\ldots,2s-1\},
 \tag{6.1}
\]

and use the two canonical Dyck roots

\[
 1100(10)^{s-2},qquad (10)^s.
 \tag{6.2}
\]

Their first three MSW states are

\[
\begin{array}{c|ccc}
1100(10)^{s-2}&12R&14R&34R\\
(10)^s&13R&23R&24R.
\end{array}
\tag{6.3}
\]

Swap \(14R\) and \(23R\).  Theorem 4.2 proves that this is an anchored
exact-factor move; its four union colours are

\[
 123R,124R,134R,234R.
 \tag{6.4}
\]

When this size-\(s\) factor is installed as a parent of its aligned
right-child hole of size \(s-1\), inspect the child window consisting of
phases \(1,\ldots,s\) in the row \((10)^s\).  Before the switch its states
successively exchange each odd coordinate for the following even one, so

\[
 \bigcap_{t=1}^{s}X_t((10)^s)=\{2\}.
 \tag{6.5}
\]

After the switch, phase one is \(14R\), while phases two through \(s\)
are unchanged.  Coordinate \(4\) belongs to all these states; coordinate
\(2\) is absent at phase one, coordinate \(1\) is absent from phase two,
every later odd coordinate is eventually deleted, and every even
coordinate at least six is absent at phase one.  Hence

\[
 \bigcap_{t=1}^{s}X'_t((10)^s)=\{4\}.
 \tag{6.6}
\]

Thus a rooted child target really moves.  At the same time Corollary 4.4
says that the rowwise exchange matching is unchanged.  Therefore neither
the exchange-matching invariant nor any invariant preserved by the
rectangle move can separate MSW from all factors with nonzero rooted
shadow action.

The move is also one ownership-component switch.  Outside the two affected
rows the old and new factors have identical rows.  On the affected rows,
the changed state and infinity-state incidences form the connected
octahedral alternating component.  Hence Corollary 5.3 applies directly,
without passing through a long path.

## 6A. The nonlocal \(r=4\) Haar edge lies in the weak fibre after conjugation

The known four-for-four Haar trade gives a second, genuinely nonlocal
legal move, but only in the weak fibre under the currently verified
embedding.

Let \(\infty=9\). For a listed cyclic order
\(q=(q_0,\ldots,q_8)\), put

\[
 \widehat q=(q_0,q_2,q_4,q_6,q_8,q_1,q_3,q_5,q_7),
 \tag{6A.1}
\]

rotate it to \((9,x_0,\ldots,x_7)\), and take the five finite states

\[
 X_j=\{x_j,x_{j+1},x_{j+2},x_{j+3}\},
 \qquad0\le j\le4.
 \tag{6A.2}
\]

For the standard coordinate order,

\[
\begin{aligned}
\mathcal D_4=\{&
1234,1235,1236,1237,1245,1246,1247,1256,1257,\\
&1345,1346,1347,1356,1357\}.
\end{aligned}
\tag{6A.3}
\]

The ten rows common to the two certified factors and the two four-row
trade shores have the following intersections with \(\mathcal D_4\):

\[
\begin{array}{c|c@{\qquad}c|c}
C_1&\varnothing&C_2&1345\\
C_3&\varnothing&C_4&\varnothing\\
C_5&\varnothing&C_6&\varnothing\\
C_7&\{1356,1256\}&C_8&\{1237,1347\}\\
C_9&1245&C_{10}&\{1357,1257,1247\}\\ \hline
N_1,P_1&1346&N_2,P_2&1246\\
N_3,P_3&1236&N_4,P_4&\{1235,1234\}.
\end{array}
\tag{6A.4}
\]

This is a direct hand check from (6A.1)--(6A.3). On either shore there
are five zero rows, five unique rows, and four multiple rows. Thus the
printed factors are not transversal for the printed standard
\(\mathcal D_4\).

There is nevertheless an exact factor-only conjugation which puts both
sides in the fixed weak fibre. Order the eight finite coordinates as

\[
 \sigma=(6,8,1,2,4,3,5,7).
 \tag{6A.5}
\]

The corresponding Dyck family is

\[
 \mathcal D^*=
 \left\{S\in\tbinom{[8]}4:
 6\in S,\ 7\notin S,\ 
 S\cap\{8,1\}\ne\varnothing,\ 
 \{3,5\}\nsubseteq S
 \right\}.
 \tag{6A.6}
\]

Indeed the Dyck prefix conditions in the order (6A.5) say that the first
coordinate \(6\) is selected, the last \(7\) is not, at least two of
\(\{6,8,1\}\) are selected, and at least three of
\(\{6,8,1,2,4\}\) are selected; with total size four this is exactly
(6A.6).

Each common row now contains the following unique
\(\mathcal D^*\)-root, at the displayed phase:

\[
\begin{array}{c|cccccccccc}
\text{row}&C_1&C_2&C_3&C_4&C_5&C_6&C_7&C_8&C_9&C_{10}\\ \hline
\text{root}&1368&2368&1456&1568&1268&1468&1256&4568&2568&2468\\
\text{phase}&0&3&2&1&0&0&1&4&2&4.
\end{array}
\tag{6A.7}
\]

On the affected shores the unique roots agree row by row:

\[
\begin{array}{c|cccc}
\text{row pair}&1&2&3&4\\ \hline
\text{root}&1346&1246&1236&3468\\
\text{\(N\)-phase}&0&0&0&3\\
\text{\(P\)-phase}&3&4&4&1.
\end{array}
\tag{6A.8}
\]

Let \(\rho=\sigma^{-1}\), fixing \(9\); explicitly,

\[
\begin{array}{c|ccccccccc}
x&1&2&3&4&5&6&7&8&9\\ \hline
\rho(x)&3&4&6&5&7&1&8&2&9.
\end{array}
\tag{6A.9}
\]

Then both conjugated exact factors are weakly standard-\(\mathcal D_4\)
transversal. Their fourteen unique roots are exactly all the sets in
(6A.3), and the four-for-four replacement is a root-preserving connected
component switch. If \(w\) is its signed row effect, then

\[
 B_4(\rho w)=B_3(\rho w)=0,
 \tag{6A.10}
\]

whereas

\[
 B_2(\rho w)=
 -e_{36}+e_{46}+e_{35}-e_{45}
 +e_{37}-e_{47}-e_{39}+e_{49}\ne0.
 \tag{6A.11}
\]

The final transposition is the conjugate \((3\,4)\) of the original
\((1\,2)\). Thus the weak fixed-transversal fibre contains a literal
nonlocal edge which preserves the first shadow and changes the second.

This does not yet give a context substitute. Several roots in
(6A.7)--(6A.8) are internal. For example \(C_2\) has unique root
\(2368=X_3\), while its finite complement \(1457\) is absent from that
row. Hence the two Haar factors are not anchored under this embedding.
Whether a different factor-only conjugation makes both sides anchored is
not proved here.

## 7. Exact constant-one boundary

The following statements are proved.

1. The fixed-root state/adjacent-union fibre is the anchored fibre.  Weak
   transversality alone is insufficient for recursive substitution.
2. Phasewise alternating-cycle and block-permutation moves have the exact
   boundary test (3.3)--(3.4).
3. Every legal nontrivial two-row one-phase move is the octahedral
   rectangle (4.4).
4. Elementary rectangles preserve the full rootwise exchange-matching
   tuple \(\Phi\).
5. Arbitrary ownership-component switches connect every pair of anchored
   factors through at most
   \(\lfloor\operatorname {Cat}_r/2\rfloor\) nontrivial switches, with
   every intermediate factor literal, integral, and anchored.
6. Therefore no invariant under that broad legal move class can obstruct
   a shadow-dispersing anchored factor.
7. A single explicit anchored rectangle already changes one rooted child
   target while preserving both exact ownership ledgers.
8. The oriented coordinate stabilizer is exactly \(C_2^{r-1}\), with
   frequency gaps
   \[
   a_{2j}-a_{2j+2}
   =\operatorname {Cat}_j\operatorname {Cat}_{r-j-1}.
   \]
9. Pure stabilizer-component moves preserve row-orbit and shadow-target
   orbit masses and obey the exact floor (4B.7).
10. The canonical \((2\,3)\) face contains
    \((1/12+o(1))\operatorname {Cat}_r\) anchored switch coordinates,
    including a positive-density \(O(\log r)\)-support subfamily.
11. After an explicit conjugation, the \(r=4\) nonlocal Haar trade is a
    root-preserving edge of the weak fixed-\(\mathcal D_4\) fibre and has
    \(B_4w=B_3w=0\), \(B_2w\ne0\).

The following are not proved.

1. The overlay-connectivity theorem does not construct a quantitatively
   shadow-dispersing endpoint factor: it uses that factor as the comparison
   shore.
2. A connected overlay component can contain a Catalan number of rows.
   No bounded-support, logarithmic-length, or monotone-energy path follows.
3. The explicit rectangle changes only a sparse set of rooted shadows.  No
   \(o(W)\) cap-tail or leave estimate follows from one move.
4. The exchange-matching tuple is not asserted to classify rectangle
   components, and it is not invariant under arbitrary block or ownership
   component switches.
5. The canonical orbit-floor lower bound in (4B.7)--(4B.8) has not been
   shown to be macroscopic on the coefficient-one window.
6. The verified \(r=4\) Haar embedding is weak but not anchored; no
   anchored conjugation of both sides is proved.
7. No anchored factor is constructed with
   \(\operatorname {PCap}_H=o(W)\), nor is a common legal phase lift or
   literal lower-shadow cover obtained.

Accordingly, the invariant branch of the assigned lane is closed for the
full interaction-component move class.  The surviving coefficient-one
problem is constructive: find an anchored comparison factor with the
required multidepth shadow dispersion and control the size or energy of
the overlay components used to reach it.

At one local scale the connectivity path changes each root block at most
once, so its total row degree is at most

\[
 \operatorname {Cat}_r
 =\frac{1}{2r+1}\binom{2r+1}{r}.
 \tag{7.1}
\]

This is \(o\!\left(\binom{2r+1}{r}\right)\); integrality and endpoint
anchoring themselves therefore impose no coefficient-one-scale toll.
The unresolved issue is whether such locally cheap moves can be chosen
coherently over all recursive parent holes while producing the required
global multidepth dispersion.
