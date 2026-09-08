# Protected matchings in odd-group hypercube quotients: the minor criterion

**Date:** 2026-08-05  
**Method:** Clifford duality and Jacobi's complementary-minor identity; no
computation  
**Status:** unconditional.  It strengthens the odd-group quotient matching
theorem from existence of one perfect matching to an exact criterion under
which a prescribed finite socket matching extends.

## 0. Outcome

Let an odd-order group `G` permute the `t` coordinates of the hypercube,
and let `R=Q_t/G`.  The Clifford proof of the perfect-matching theorem
produces a square matrix `A`, from even subset-orbits to odd subset-orbits,
such that

\[
                 A^{-1}=t^{-1}A^{\mathsf T}.          \tag{0.1}
\]

Every nonzero entry of `A` is an edge of `R`.  Call these edges
**Clifford-active**.

If `U` is a set of `s` even orbit vertices and `V` is a set of `s` odd
orbit vertices, then

\[
 \boxed{
 \det A[U,V]\ne0
 \quad\Longrightarrow\quad
 R-(U\cup V)\text{ has a perfect matching}.}        \tag{0.2}
\]

Consequently, any prescribed matching from `U` to `V` extends to a perfect
matching of `R` whenever its endpoint minor `A[U,V]` is nonsingular.  The
prescribed edges need only be quotient edges; they need not be the
determinant term witnessing the minor.

For two prescribed Clifford-active edges `u_1v_1,u_2v_2`, it is enough
that at least one cross entry `A_(u_1,v_2),A_(u_2,v_1)` vanish.  More
generally, a triangular active socket pattern always extends.

This is the protected-edge statement needed by radial shell induction.  It
does not assert that every quotient edge is Clifford-active, or that every
arbitrary prescribed matching has a nonsingular endpoint minor.

## 1. The Clifford block

Put `V=R^t` with its orthonormal coordinate basis and let

\[
 C=\varepsilon_v+\iota_v,
 \qquad v=e_1+\cdots+e_t.
\]

The Clifford relations give

\[
                         C^2=tI,                     \tag{1.1}
\]

and `C` is self-adjoint.  Since `v` is fixed by every coordinate
permutation, `C` commutes with `G` and restricts to the invariant exterior
algebra.

Because `G` has odd order, the stabilizer of every subset acts with positive
exterior sign on its wedge line.  Hence the invariant even and odd spaces
have orthonormal bases indexed respectively by the even and odd `G`-orbits
of subsets.  In those bases write

\[
 C\bigm|_{(\Lambda V)^G}
   =\begin{pmatrix}0&A^{\mathsf T}\\ A&0\end{pmatrix}. \tag{1.2}
\]

Equation (1.1) gives

\[
 A^{\mathsf T}A=tI,
 \qquad AA^{\mathsf T}=tI.                           \tag{1.3}
\]

In particular `A` is square and (0.1) holds.  A matrix entry can be nonzero
only when its two subset-orbits contain representatives differing in one
coordinate.  Thus the support graph of `A` is a spanning subgraph of
`R`.

## 2. Complementary minors

### Theorem 2.1 (protected-minor extension)

Let `U` index `s` rows of `A` and let `V` index `s` columns.  Then

\[
 \det A[U^c,V^c]
   =\pm \det(A)\,t^{-s}\det A[U,V].                  \tag{2.1}
\]

Therefore `det A[U,V]` is nonzero if and only if the complementary
determinant `det A[U^c,V^c]` is nonzero.  Either condition implies that
the active support graph, and hence the full quotient graph, after deleting
`U union V` has a perfect matching.

If, in addition, `M` is any prescribed matching from `U` to `V` in `R`,
then `M` is contained in a perfect matching of `R`.

#### Proof

Jacobi's complementary-minor identity gives

\[
 \det A[U^c,V^c]
 =\pm\det(A)\det(A^{-1})[V,U].                       \tag{2.2}
\]

By (0.1),

\[
 \det(A^{-1})[V,U]
   =t^{-s}\det A^{\mathsf T}[V,U]
   =t^{-s}\det A[U,V],                              \tag{2.3}
\]

which proves (2.1).

If the right side is nonzero, the determinant expansion of the
complementary minor contains a nonzero permutation term.  Its entries form
a perfect matching between the remaining row and column vertices, all in
the active support graph.  Conversely, existence of a support-perfect
matching alone need not force a nonzero determinant because different
matching terms can cancel.  Accordingly, the implication used below is the
proof-safe direction

\[
 \det A[U,V]\ne0
 \Longrightarrow
 R-(U\cup V)\text{ has a perfect matching}.          \tag{2.4}
\]

Adjoin the prescribed, vertex-disjoint edges of `M` to that complementary
matching.  This gives a perfect matching of `R` containing `M`.  \(\square\)

### Corollary 2.2 (one protected active edge)

Every Clifford-active edge belongs to a perfect matching of `R`.

#### Proof

Take `s=1`.  Its endpoint minor is its nonzero matrix entry.  Apply
Theorem 2.1.  \(\square\)

### Corollary 2.3 (two sockets)

Suppose `u_1v_1,u_2v_2` are disjoint Clifford-active edges.  If

\[
 A_{u_1v_2}=0
 \quad\hbox{or}\quad
 A_{u_2v_1}=0,                                      \tag{2.5}
\]

then both prescribed edges lie in one perfect matching of `R`.

#### Proof

The endpoint minor has determinant

\[
 A_{u_1v_1}A_{u_2v_2}-A_{u_1v_2}A_{u_2v_1}.
\]

The first product is nonzero and (2.5) kills the second.  Apply Theorem
2.1.  \(\square\)

### Corollary 2.4 (triangular protected bank)

Let `u_iv_i`, `1<=i<=s`, be a prescribed matching of Clifford-active
edges.  If the rows and columns may be ordered so that `A[U,V]` is
triangular, then the whole prescribed matching extends to a perfect
matching of `R`.

#### Proof

The diagonal is nonzero, so the triangular minor has nonzero determinant.
\(\square\)

### Corollary 2.5 (unique induced socket matching)

Let `M` be a prescribed Clifford-active matching from `U` to `V`.  If `M`
is the unique perfect matching of the active bipartite graph induced on
`U union V`, then `M` extends to a perfect matching of `R`.

#### Proof

The determinant expansion of `A[U,V]` has exactly one support-nonzero
permutation term, namely `M`.  Its product is nonzero, so the minor cannot
cancel.  Apply Theorem 2.1.  \(\square\)

This is often easier to check than signs or numerical coefficients: an
induced alternating cycle is the only possible source of a second matching
term.

## 3. Recognizing active orbit edges

An edge of the simple quotient may collect several literal cube-edge
orbits, and their exterior signs can in principle cancel.  The following
safe criterion is enough for the necklace application.

### Lemma 3.1 (unique literal edge orbit is active)

Let `O_e,O_o` be an even and an odd subset-orbit.  If the literal cube
edges between them form one `G`-orbit, then the corresponding entry of `A`
is nonzero.

#### Proof

Choose one incident pair `S,T`.  Exterior multiplication or contraction
has coefficient `+1` or `-1` on the oriented wedge pair.  Equivariance of
`C` transports this coefficient, including the coherent orbit-basis signs,
to every translate of the pair.  Since the edge set is one transitive
orbit, all contributions to the orbit-to-orbit coefficient have the same
nonzero sign.  They cannot cancel.  \(\square\)

Thus a protected bank whose endpoint incidence matrix is triangular and
whose selected diagonal edges each have a unique literal toggle orbit is
automatically extendable.

## 4. Radial-shell consequence and exact remaining check

In a periodic zero-skeleton/key fibre of an odd-slot adjacent-necklace
shell, the active allocation phases form `Q_t/H` with `|H|` odd, and a
one-bit edge is a literal adjacent chip transfer.  Theorem 2.1 therefore
gives the following exact reusable rule.

> A prescribed family of phase-toggle sockets is harmless whenever its
> small Clifford endpoint minor is nonsingular.

For the two radial shell sockets, it suffices in general to verify any one of:

1. they lie in distinct phase fibres;
2. in their common fibre, both selected toggle orbits are unique and one
   cross incidence is absent; or
3. their explicit `2x2` Clifford minor is nonzero.

This removes the need for arbitrary edge-extendability, which is false
already for `Q_3/C_3=P_4`.  What remains is a finite symbolic check of the
radial socket fibres and the injection of all-quiet singleton fibres into
the next zero stratum.  No global matching search is involved.

For the universal radial square this symbolic check is explicit.  Write

\[
 A=[0,1^{q-2},s-q+2],\qquad
 B=[0,1^{q-3},2,s-q+1],                             \tag{4.1}
\]

with `s>=q+2`.  The unique-zero skeleton has trivial rotational stabilizer,
and `AB` toggles its final positive pair

\[
                         (1,L)\longleftrightarrow(2,L-1),
 \qquad L=s-q+2.                                    \tag{4.2}
\]

This is one literal toggle orbit.  Lemma 3.1 and Corollary 2.2 therefore
show that `AB` lies in a perfect matching of its entire phase fibre.  It
costs no exported socket.

The other radial edge

\[
 C=[0^{q-1},s],\qquad D=[0^{q-2},1,s-1]             \tag{4.3}
\]

is not a phase edge: it changes the number of zeros.  The `D` endpoint has
one two-coordinate positive run `(1,s-1)` and, in the nonterminal range,
lies in a `t=1` active phase fibre.  Deleting `D` from that fibre and
restricting any perfect matching leaves exactly its opposite-parity mate as
one exported socket.  Thus the protected radial square has the sharp local
state

\[
                 \boxed{AB\text{ costs zero; }CD\text{ starts one
                 radial monomer}.}                  \tag{4.4}
\]

The remaining shell theorem is therefore not a two-edge protection
problem.  It is the one-monomer transport problem through the all-quiet
receiver chain, followed by its terminal absorption.

## 5. Scope

Proved:

1. exact Clifford duality (0.1);
2. the complementary-minor extension implication for every protected
   socket bank;
3. automatic extension of one active edge, two cross-separated active
   edges, or any triangular active bank; and
4. a unique-literal-orbit criterion for activity.

Not proved:

1. that every quotient edge is active;
2. all-quiet receiver transport/absorption in every zero codimension;
3. the complete protected adjacent-necklace shell theorem; or
4. any universal-word upper bound.
