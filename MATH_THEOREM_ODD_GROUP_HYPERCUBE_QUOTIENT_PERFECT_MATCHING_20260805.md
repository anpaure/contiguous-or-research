# Odd-group hypercube quotients have perfect matchings

## 1. Statement

Let a finite group \(G\) of odd order act on the coordinate set
\([t]=\{1,\ldots,t\}\), where \(t\ge 1\).  Let \(G\) act on the vertices
of the hypercube \(Q_t\) by permuting coordinates.  Write
\(Q_t/G\) for the simple orbit graph: its vertices are the \(G\)-orbits
of subsets of \([t]\), and two distinct orbits are adjacent when they
contain representatives whose symmetric difference has size one.

### Theorem 1 (odd-group quotient matching)

The bipartite graph \(Q_t/G\) has a perfect matching.

In particular, this holds when \(G\) is any odd-order cyclic group.

The result is stronger than parity balance.  It gives Hall's conclusion
without requiring a canonical root in a periodic necklace fibre.

## 2. Exterior-algebra proof

Let \(V=\mathbb R^t\) with its orthonormal coordinate basis
\(e_1,\ldots,e_t\), and let

\[
  \Lambda V=\Lambda^{\mathrm{ev}}V\oplus\Lambda^{\mathrm{odd}}V.
\]

For a subset \(S=\{i_1<\cdots<i_s\}\), write

\[
  e_S=e_{i_1}\wedge\cdots\wedge e_{i_s}.
\]

The coordinate action of \(G\) induces its natural orthogonal action on
\(\Lambda V\).

### Lemma 2.1 (one invariant line per set orbit)

For every \(G\)-orbit \({\cal O}\) of subsets, the signed permutation
module

\[
  E_{\cal O}=\operatorname{span}\{e_S:S\in{\cal O}\}
\]

has a one-dimensional invariant subspace.

#### Proof

Fix \(S\in{\cal O}\).  If \(g\in G_S\) stabilizes \(S\) setwise, then

\[
  g e_S=\operatorname{sgn}(g|_S)e_S.
\]

The map \(g\mapsto\operatorname{sgn}(g|_S)\) is a homomorphism from the
odd-order group \(G_S\) to \(\{\pm1\}\), so it is trivial.  Thus the
stabilizer acts trivially on \(e_S\).  Inducing this trivial stabilizer
representation to the orbit gives a signed orbit sum spanning exactly
one invariant line.  Distinct set orbits have disjoint basis support.
\(\square\)

Consequently,

\[
 \dim (\Lambda^{\mathrm{ev}}V)^G
   =\#\{\text{even set orbits}\},
 \qquad
 \dim (\Lambda^{\mathrm{odd}}V)^G
   =\#\{\text{odd set orbits}\}.
 \tag{2.1}
\]

Put

\[
  v=e_1+\cdots+e_t.
\]

Let \(\varepsilon_v\) denote exterior multiplication by \(v\), let
\(\iota_v\) denote contraction by \(v\), and set

\[
  C_v=\varepsilon_v+\iota_v.
\]

The Clifford relations give

\[
  C_v^2
  =\varepsilon_v\iota_v+\iota_v\varepsilon_v
  =\langle v,v\rangle I
  =tI.
  \tag{2.2}
\]

Thus \(C_v\) is invertible.  It reverses exterior parity.  Moreover,
\(v\) is fixed by every coordinate permutation, so \(C_v\) commutes
with \(G\).  Hence it restricts to an isomorphism

\[
  C_v:(\Lambda^{\mathrm{ev}}V)^G
     \longrightarrow(\Lambda^{\mathrm{odd}}V)^G.
  \tag{2.3}
\]

Choose the orbit-indexed invariant bases supplied by Lemma 2.1.  In
these bases, a matrix entry of (2.3) can be nonzero only if the
corresponding even and odd set orbits contain sets differing in one
coordinate: both \(\varepsilon_v\) and \(\iota_v\) toggle exactly one
coordinate.  Therefore every nonzero matrix entry is supported on an
edge of \(Q_t/G\).

The matrix in (2.3) is square and nonsingular.  A nonzero term in its
determinant selects one nonzero entry in every row and every column.
The corresponding quotient edges form a perfect matching.  This proves
Theorem 1. \(\square\)

## 3. Exact application to periodic zero-skeleton fibres

Consider an odd cyclic composition length \(q\).  Fix:

1. a cyclic zero pattern with exactly \(j\) zeros;
2. the positive-run decomposition between those zeros;
3. in every run, the standard adjacent pairs (pairs \((1,2),(3,4),\ldots\)
   in an even run, and an unpaired first coordinate followed by pairs
   \((2,3),(4,5),\ldots\) in an odd run);
4. the sum of each adjacent pair and its local two-state key; and
5. all unpaired positive coordinates.

For one adjacent positive pair \((a,b)\), put

\[
  u=a-1,\qquad w=b-1.
\]

Fix its sum \(n=u+w\), and put \(z=\lfloor u/2\rfloor\).  The states
with this sum split exactly into the two-state keys

\[
  (u,w)=(2z,n-2z)
  \quad\hbox{and}\quad
  (2z+1,n-2z-1),
  \tag{3.1}
\]

for \(2z<n\).  When \(n\) is even, the sole state not in one of these
two-state keys is

\[
  (u,w)=(n,0);
  \tag{3.2}
\]

this is the quiet singleton key.  Thus the keys partition every
possible allocation of the fixed pair sum.  Toggling a two-state phase
transfers one unit between the two
adjacent coordinates.  Both coordinates stay positive, so this is a
legal edge of the adjacent-unit-transfer composition graph and it does
not change the zero pattern.

Let \(t\) be the number of nonsingleton pair keys.  The stabilizer
\(H\le C_q\) of all the fixed skeleton/key data permutes these \(t\)
active pairs.  Since \(q\) is odd, \(|H|\) is odd.  Necklace states in
this fixed fibre are exactly

\[
  \{0,1\}^t/H.
  \tag{3.3}
\]

Under this identification, a one-bit quotient edge is exactly one legal
adjacent chip transfer (3.1).  Theorem 1 therefore gives:

### Corollary 3.1 (periodic first-nonquiet matching)

Every fixed skeleton/key fibre with \(t\ge1\) is perfectly matched by
legal adjacent chip transfers, even when the zero skeleton is periodic
and has no distinguished cyclic root.

If \(t=0\), the fibre is a singleton.  These and only these singleton
fibres are the all-quiet residual states that must be passed to the
next-zero receiver construction.

Thus periodic zero patterns introduce no additional matching defect.

The conclusion is conditional only on the stated fibre decomposition:
one must verify in the ambient adjacent-necklace construction that the
chosen skeleton, pair sums/keys, and unpaired coordinates really are
invariants of the proposed local phase moves.  It does not by itself
match different skeleton/key fibres.

## 4. Protected sockets: the strongest automatic extension

Arbitrary prescribed-edge extension is false.  For example,

\[
  Q_3/C_3\cong P_4.
\]

Its perfect matching is unique, so the middle edge belongs to no perfect
matching.  Therefore Theorem 1 cannot be used to demand an arbitrary
protected radial edge inside a phase fibre.

The proof does, however, identify a protected subgraph.  Normalize the
orbit invariant vectors from Lemma 2.1 to obtain orthonormal bases.  Let
\(A\) be the matrix of \(C_v\) from even invariants to odd invariants.
Self-adjointness of \(C_v\), together with \(C_v^2=tI\), gives

\[
  A^{-1}=t^{-1}A^{\mathsf T}.
  \tag{4.1}
\]

Call a quotient edge **Clifford-active** when its corresponding entry
of \(A\) is nonzero.

### Corollary 4.1 (every Clifford-active edge is extendable)

Every Clifford-active edge belongs to a perfect matching of \(Q_t/G\).
Equivalently, if its endpoints are \(x,y\), then

\[
  (Q_t/G)-\{x,y\}
\]

has a perfect matching.

#### Proof

If \(A_{y,x}\ne0\), then (4.1) says that the complementary cofactor of
that entry is nonzero.  A nonzero determinant term of the complementary
minor gives the desired matching after \(x,y\) are deleted; adjoining
\(xy\) gives a full perfect matching containing the edge. \(\square\)

An easy sufficient condition for activity is uniqueness: if all literal
one-bit edges between the two set orbits form one \(G\)-orbit, then the
quotient edge is Clifford-active.  Indeed, equivariance makes every
translated literal edge contribute the same signed scalar in the two
invariant orbit vectors, so cancellation is impossible.  Cancellation
can occur when two or more literal edge orbits project to the same
quotient edge.  In \(Q_3/C_3\), this is exactly what happens at the
unextendable middle edge.

There is nevertheless an exact two-boundary statement.

### Corollary 4.2 (one prescribed socket, one free companion)

Let \(R=Q_t/G\), with \(|G|\) odd and \(t\ge1\).  For every prescribed
vertex \(x\in V(R)\), there is a vertex \(y\) of opposite parity such
that

\[
  R-\{x,y\}
\]

has a perfect matching.

#### Proof

Take any perfect matching of \(R\), and let \(y\) be the mate of \(x\).
Delete their matching edge. \(\square\)

This is the correct radial-socket interpretation.  If an incoming radial
edge consumes the prescribed receiver \(x\), the fibre can match every
other vertex except one freely chosen companion \(y\).  That companion
is the outgoing radial socket.  Hence a single monomer can be transported
through a sequence of periodic phase fibres without branching or
accumulating.

It is not automatic that a separately prescribed outgoing socket can be
used.  Such a claim requires a stronger extendability theorem or an
explicit boundary construction in the ambient necklace graph.

## 5. Scope

What is now unconditional:

- odd cyclic symmetry never obstructs perfect matching inside a full
  phase-cube fibre;
- all nonquiet phase fibres can be saturated by legal adjacent transfers;
- one prescribed receiver can always be converted into one outgoing
  companion socket, so radial monomer count need not grow.

What remains outside this theorem:

- matching the all-quiet singleton fibres into the \((j+1)\)-zero core;
- proving injectivity of those receiver edges across different fibres;
- arranging protected shell-splice edges such as the radial square
  \(AB/CD\) when their endpoints are prescribed in advance; and
- consolidating multiple radial monomer paths into the globally allowed
  socket budget.
