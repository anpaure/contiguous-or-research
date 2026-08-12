# Boolean aligned colours, terminal five-colour flow, and the sparse-\(C_{10}\) parity gate

Date: 2026-07-31

Status: exact affine-alignment characterization; exact whole-colour
co-omission and capacity-cut ledgers; an all-large-\(n\), actual-Boolean
protected induced-face counterexample with near-ceiling classes and the
correct bridge divisibility; exact five-colour terminal-boundary and
directed-release theorems; an exact projected algebraic generation identity
and a conformal non-generation theorem for sparse \(C_{10}\) switches; and an
exact delete--contract--add theorem
for breaking the physical cycles of a correlated exact cover.  The
positive-density assertion for a specially chosen colouring of the full
dense host remains open.

## 0. Result and scope

Fix one admissible common basis \(Q\) and its four-uniform Boolean
capacity-slot host \({\cal H}_Q\).  The strongest literal interpretation of
an aligned Delcourt--Postle colour is false for a simple reason: every colour
leave contains a forced positive slot baseline.  After removing that
baseline, alignment is exactly extendibility to a \(P\)-atom matching,
together with one contracted graphic row.  It is not a consequence of class
size.

There are four further conclusions.

1. For every sufficiently large \(n\) and every fixed \(Q\), an actual
   vertex-induced Boolean subhost has an optimal four-colouring in which all
   four classes have deficiency \(n=o(P_*)\), satisfy the necessary
   \(n\mid\delta\) bridge congruence, and have no residual candidate atom at
   all.  Arbitrary recolouring inside that protected face cannot gain.  This
   refutes every hereditary or purely local positive-density theorem, but not
   a global theorem using exterior atoms of the full \({\cal H}_Q\).
2. A support-preserving five-colour refactorization changes the target leave
   only on resources of packet degree at most four.  A five-regular packet is
   an incidence-kernel move and cannot align a bad leave.  The affine
   \(25\)-atom alternate factorization is of this useless saturated type and
   also has no direct Boolean lift: its \(K_{5,5}\) lower--upper projection
   collapses onto one owner and needs at least thirteen colours.
3. The sparse Boolean \(5\leftrightarrow5\) switch is the correct kind of
   low-degree slot rerouter, but its outer permutation is a \(5\)-cycle and
   hence even.  Every sequence of these \(C_{10}\) switches preserves
   matching sign.  A literal capacity-safe Boolean square changes the sign.
   Thus sparse \(C_{10}\)'s do not connect the protected-face exchange
   graph, so no universal connectivity theorem is possible.  Algebraically
   this is not a binary cycle-space obstruction: for
   \(n\ge9\), every full-host Boolean square is the projected signed
   difference of two sparse \(C_{10}\)'s.  Conformal legal switching and
   projected lattice generation are therefore genuinely different.
4. A bare sparse \(C_{10}\) is not an all-resource move: it migrates one
   slot from each \(P_i\) to \(Q_i\).  For a slot-closed packet family, the
   exact forest test is that the deleted edges hit every old physical cycle
   and the added edges are independent after contracting the retained
   forest.  With a fixed coherent tail/head orientation and the at-most-one-
   reset invariant, directed closed \(C_6\) and \(C_{10}\) kernel moves
   absorb unwanted cycles only in blocks of two and four.  If reorientation
   is allowed, the sharper test is an alternating port-path condition: every
   killed cycle must be routed to an invariant path endpoint.

Whole residual paths are joint three-sector objects.  Even a completed side
colour is path-aligned only after the other two sector forests, their
orientations, the path-dependent endpoint bank, and one socket Hall matching
are supplied.  No unary positive-density statement can bypass those rows.

## 1. Host notation and the forced affine baseline

Use

\[
 N={2n\choose n-1},\qquad P={2n\choose n-2},\qquad
 C=\operatorname {Cat}_{n+1},\qquad K=\operatorname {Cat}_n .
\tag{1.1}
\]

The resource shores of \({\cal H}_Q\) have sizes

\[
                 P,\qquad P,\qquad 2N-C.             \tag{1.2}
\]

An atom contains one punctured rank-\(n\) lower colour, one rank-\((n+2)\)
upper colour, and one labelled slot at each of its two rank-\((n+1)\)
physical owners.  Let \(A_Q\) be the resource-by-atom incidence matrix.

The excess slot count is

\[
 \sigma=(2N-C)-2P=C-2K={2P\over n}>0.                \tag{1.3}
\]

For a colour matching \(M\), put

\[
 t=P-|M|,\qquad r_M={\bf1}-A_Q{\bf1}_M.              \tag{1.4}
\]

Its leave has shore signature

\[
                         (t,t,2t+\sigma).             \tag{1.5}
\]

Every union of \(t\) candidate atoms has signature \((t,t,2t)\).
Consequently no literal full-host colour leave is a union of candidates.
This holds for every \(Q\), every colouring, and every \(n\).

### Theorem 1.1 (exact affine candidate alignment)

The following are equivalent.

1. \(M\) extends, while retaining every atom of \(M\), to a \(P\)-atom
   matching of \({\cal H}_Q\).
2. There are a slot set \(B_0\subseteq\operatorname {supp}r_M\) of order
   \(\sigma\) and \(z\in{\mathbb Z}_{\ge0}^{E({\cal H}_Q)}\) such that

   \[
                    r_M-{\bf1}_{B_0}=A_Qz.            \tag{1.6}
   \]

When these statements hold, \(z\) is automatically the incidence vector of
a \(t\)-edge host matching disjoint from \(M\).

#### Proof

An exact extension \(T=M\dot\cup Z\) leaves \(\sigma\) slots unused and no
outer resource unused.  Taking these slots as \(B_0\) and the added atoms as
\(z\) gives (1.6).

Conversely, the left side of (1.6) is zero-one.  Since \(A_Q\) is zero-one
and \(z\) is a nonnegative integer vector, no coefficient of \(z\) exceeds
one and no two selected columns meet in a resource.  Its support is contained
in the leave of \(M\), so it is disjoint from \(M\).  Counting the lower
shore in (1.6) gives \(|z|=t\).  Therefore \(M\cup\operatorname {supp}z\)
is a \(P\)-atom matching.  \(\square\)

If a fixed scaffold \(F_{\rm fix}\cup\phi(M)\) is already a forest, the
extension in Theorem 1.1 is a physical forest exactly when the edges
\(\phi(\operatorname {supp}z)\) are loopless and independent in the graphic
matroid after contracting that scaffold.

The baseline is not merely an arbitrary set of the right cardinality after
a terminal state is prescribed.  For a final forest \(F\), its ownerwise
baseline multiplicity is

\[
                 b_F(x)=c_Q(x)-d_F(x).               \tag{1.7}
\]

Slot labels at one owner are interchangeable, so (1.7) is also sufficient
for the labelled baseline.  A path-dependent endpoint or no-empty state
therefore fixes the histogram of \(B_0\), not just \(|B_0|\).

## 2. What the entire colouring would have to control

Let \(M_1,\ldots,M_k\) be the complete proper conflict-free colouring and
let

\[
 C(v)=\{i:v\in V(M_i)\}.
\tag{2.1}
\]

Properness gives \(|C(v)|=d(v)\).  Let

\[
 {\cal F}_i=\{e\in E({\cal H}_Q):V(e)\subseteq
                  V({\cal H}_Q)\setminus V(M_i)\}
\tag{2.2}
\]

be the free candidate host for colour \(i\).

### Proposition 2.1 (four-resource co-omission ledger)

\[
 \boxed{\quad
 \sum_i|{\cal F}_i|
   =\sum_{e\in E({\cal H}_Q)}
      \left(k-\left|\bigcup_{v\in e}C(v)\right|\right).
 \quad}                                                \tag{2.3}
\]

Moreover \(M_i\) is affinely candidate-aligned exactly when

\[
                  \nu({\cal F}_i)=P-|M_i|,             \tag{2.4}
\]

with the contracted graphic and prescribed-baseline rows added when a
physical terminal state is required.

#### Proof

An atom \(e\) is free for colour \(i\) exactly when
\(i\notin\bigcup_{v\in e}C(v)\).  Counting such pairs \((i,e)\) proves
(2.3).  A matching of \(P-|M_i|\) free atoms completes \(M_i\) to order
\(P\), and every extension supplies such a matching.  This proves (2.4).
\(\square\)

Thus the one-resource omission law and the pair-of-colours support ledger
from item 2300A do not control the required statistic.  Equation (2.3)
depends on candidate-specific triple and quadruple intersections.  For a
whole residual path it depends on \(O(n)\)-fold co-omission.

There is also an exact capacity-cut average.  Fix an upper-target family
\(W\) and a slot bank \(S(W)\) which contains both physical corners of every
surviving candidate incident with \(W\), after any protected forced-row
propagation.  Put

\[
 h_i(W)=|W\setminus V(M_i)|,\qquad
 u_i(W)=|S(W)\setminus V(M_i)|,
\tag{2.5}
\]

where the second expression refers only to slot resources.  Every retaining
completion of \(M_i\) satisfies

\[
                         2h_i(W)\le u_i(W).           \tag{2.6}
\]

Across the whole colouring,

\[
\boxed{
\begin{aligned}
 \sum_i(2h_i(W)-u_i(W))
  ={}&2\left(k|W|-\sum_{V\in W}d(V)\right)\\
    &-\left(k|S(W)|-\sum_{s\in S(W)}d(s)\right).
\end{aligned}}                                        \tag{2.7}
\]

The proof is the one-resource omission identity summed over \(W\) and
\(S(W)\).  It controls a signed average for each cut, not simultaneous
nonpositivity of every cut in one colour.

## 3. A near-perfect protected Boolean face with zero aligned colours

This section gives a dimension-growing obstruction inside the actual
Boolean host.

Fix four coordinates

\[
             X=\{x_0,x_1,x_2,x_3\},\qquad
             Y=[2n]\setminus X,
\tag{3.1}
\]

and \(K_0\in{Y\choose n-1}\).  Define

\[
 D_{K_0,i}=K_0+x_i,\qquad
 V_{K_0,j}=K_0+(X\setminus\{x_j\}).                  \tag{3.2}
\]

Then

\[
 D_{K,i}\subset V_{K',j}
 \quad\Longleftrightarrow\quad K=K'\text{ and }i\ne j.
\tag{3.3}
\]

For fixed \(K\), the twelve outer incidences form the crown
\(K_{4,4}\) minus its diagonal.  Its six physical owners are
\(K+\{x_i,x_j\}\), \(i<j\).  Retain one available slot at each owner.

Colour the crown by the following four oriented triangular faces:

\[
\begin{array}{c|c}
0&1\to2\to3\to1\\
1&0\to3\to2\to0\\
2&0\to1\to3\to0\\
3&0\to2\to1\to0 .
\end{array}                                           \tag{3.4}
\]

The twelve directed off-diagonal pairs occur exactly once.  In each colour,
the three diamonds use all six owners once, so the colour is a physical
matching and omits exactly the nonedge

\[
                         D_{K,c},V_{K,c}.             \tag{3.5}
\]

Add many disjoint filler blocks.  For a distinct \(K\in{Y\choose n-1}\),
put

\[
 D_K=K+x_0,\qquad V_K=K+x_0+x_1+x_2,                 \tag{3.6}
\]

with owners \(K+x_0+x_1\) and \(K+x_0+x_2\).  When \(D_K\) survives the
puncture and both owners are ordinary, retain both slots at both owners.
The resulting block has four slot lifts of its unique outer pair; put one
lift in each colour.

Let

\[
                       t_0={2n-4\choose n-1}.         \tag{3.7}
\]

At most \(C\) values of \(K\) are killed by the punctured lower bank.  The
two owner images in (3.6) are disjoint, so the anchor bank kills at most
another \(C\) values in total.  Hence there are at least

\[
                         t_0-2C=\Theta(P)             \tag{3.8}
\]

good filler indices, since \(t_0/P\to1/16\) and \(C/P\sim4/n\).
There are also enough crown indices for every sufficiently large \(n\).

Choose \(r=n\) crown blocks and \(T=\Theta(P)\) good filler blocks, all with
different \(K\)'s, and take the vertex-induced subhost on their displayed
outer and slot resources.

### Theorem 3.1 (congruence-correct protected-face obstruction)

The induced host has equal outer-shore order

\[
                           P_*=T+4n,                 \tag{3.9}
\]

and an optimal proper conflict-free four-colouring in which every class has

\[
                   |M_c|=T+3n=P_*-n=P_*-o(P_*).      \tag{3.10}
\]

Every class is a physical linear forest and its deficiency \(n\) satisfies
the necessary residual-path congruence \(n\mid\delta\).  Nevertheless

\[
                    E({\cal H}_{\rm ind}[L_c])=\varnothing
                    \qquad(c=0,1,2,3),               \tag{3.11}
\]

and

\[
                    \nu({\cal H}_{\rm ind})=T+3n.    \tag{3.12}
\]

Thus no recolouring using only this protected induced face, with five
colours or with arbitrarily many colours, can align or enlarge any class.

#### Proof

Different \(K\)-blocks have no cross containment by (3.3), and their owner
sets are disjoint.  Each filler contributes one atom to every colour and
has matching number one.  Each crown contributes the three atoms in (3.4);
their physical edges form a matching on its six owners.  Hence (3.9)--(3.10)
and conflict freedom hold.

The outer holes of colour \(c\) are the \(n\) pairs in (3.5); filler blocks
also contribute the forced unused-slot baseline.  A same-\(K\) pair is a
noncontainment pair, and distinct \(K\)'s have no containment by (3.3),
proving (3.11).  Six selected crown slots bound a crown matching by
three, while (3.4) attains three.  Summing this with the filler bound proves
(3.12).  \(\square\)

This is not a colouring of the complete dense \({\cal H}_Q\).  Exterior
atoms can connect a displayed lower hole to an upper resource outside the
protected face.  The theorem refutes a hereditary/local aligned-colour
theorem, not a global favourable-\(Q\) theorem.

## 4. One consumptive recolouring is an all-or-none terminal question

Let \(Z\subseteq M\) be protected and let \({\cal T}_Z\) be the family of
all \(P\)-atom physical-forest matchings in the fixed host and scaffold
which contain \(Z\) and satisfy every prescribed endpoint, socket, and
compiler guard.

### Theorem 4.1 (one-shot collapse)

There is one consumptive multicolour packet which changes \(M\) to an
aligned terminal while preserving \(Z\) if and only if

\[
                         {\cal T}_Z\ne\varnothing.    \tag{4.1}
\]

#### Proof

Take \(T\in{\cal T}_Z\) and \(S=T\setminus M\).  Every atom of
\(M\setminus T\) has a lower resource which is covered by a unique different
atom of \(T\), hence by an atom of \(S\).  Conversely an atom of \(M\cap T\)
meets no atom of \(S\).  Therefore

\[
                         N_M(S)=M\setminus T.         \tag{4.2}
\]

The simultaneous packet \(M-N_M(S)+S\) is exactly \(T\) and keeps \(Z\).
The reverse implication is tautological from the terminal state.  \(\square\)

Thus, with no support bound and no donor-colour transparency, the starting
Delcourt--Postle colour is irrelevant.  For \(Z=\varnothing\), either every
colour is consumptively repairable or none is.  A positive-density theorem
has content only when it limits the changed support or preserves the other
colours and the prefix guards.

There is an exact counting cost for strong protection.  Let \({\cal T}\)
be any family of allowed guarded terminals.  Suppose every considered class
has size at least \(P-h\), and a repair retains all but at most \(b\) atoms
of that class.  If \(I\) is the set of repairable colours and
\(P-h-b>0\), then

\[
 |I|\le |{\cal T}|
       \left\lfloor{P\over P-h-b}\right\rfloor .      \tag{4.3}
\]

Indeed, assign to every \(i\in I\) one terminal \(T_i\).  For a fixed
terminal \(T\), the sets \(T\cap M_i\) are disjoint over \(i\), because the
colour classes are edge-disjoint, and each assigned intersection has order
at least \(P-h-b\).  This proves (4.3).  In particular, when
\(h+b=o(P)\), positive density among \(k=\Theta(n^2)\) colours requires
\(\Omega(k)\) allowed physical terminals in the chosen endpoint/socket
state.  One canonical terminal cannot do this.

## 5. Exact terminal-boundary theorem for five colours

Let \(U\) be one atom support with two proper five-colourings
\(\phi,\psi:U\to{\mathbb Z}_5\).  Put

\[
 M_c=\phi^{-1}(c),\qquad N_c=\psi^{-1}(c),\qquad
 b=A_Q({\bf1}_{N_0}-{\bf1}_{M_0}).                  \tag{5.1}
\]

### Theorem 5.1 (five-colour boundary lives on terminals)

Let

\[
                        T(U)=\{v:d_U(v)\le4\}.        \tag{5.2}
\]

Then

\[
                         \operatorname {supp}b\subseteq T(U).    \tag{5.3}
\]

If \(g=|N_0|-|M_0|\), then

\[
 \sum_{D\in{\cal D}}b_D=g,\qquad
 \sum_{V\in{\cal V}}b_V=g,\qquad
 \sum_{s\in{\cal S}}b_s=2g.                         \tag{5.4}
\]

In particular, if every used resource has \(U\)-degree five, then

\[
                         b=0,\qquad g=0.              \tag{5.5}
\]

The refactorization may change physical topology, but it cannot change the
target resource leave or its candidate-semigroup membership.

#### Proof

Properness gives \(d_U(v)\le5\).  At a resource of degree five, each proper
five-colouring uses all five colours exactly once, so colour zero occurs
once before and after.  This proves (5.3).  Each Boolean atom has one lower,
one upper, and two slot resources; summing (5.1) over the three types gives
(5.4).  Equation (5.5) follows.  \(\square\)

For a target leave \(r_{M_0}\), the new target is affinely aligned exactly
when, for its prescribed baseline,

\[
            r_{M_0}-b-{\bf1}_{B_0}=A_Qz,\qquad z\ge0,             \tag{5.6}
\]

together with the contracted graphic and endpoint/socket rows.  Therefore
a useful gain-one five-colour packet must expose net terminal boundary
\((1,1,2)\); a saturated alternate factorization cannot do so.

If \(U\) is only part of five global colour classes, properness of \(\psi\)
on \(U\) is not enough.  Every new colour must avoid frozen same-colour atoms
outside \(U\), and every affected class must still avoid the Delcourt--
Postle configuration hypergraph.  Equivalently, the packet must be
colour-closed or carry an explicit transparent boundary.

## 6. Why the affine five-colour opening has no direct Boolean use

Suppose two lower families
\({\cal A}\subseteq{[2n]\choose n}\) and
\({\cal B}\subseteq{[2n]\choose n+2}\), each of order at least two, satisfy
\(A\subset B\) for every \(A\in{\cal A},B\in{\cal B}\).  Put

\[
                  H=\bigcup_{A\in{\cal A}}A
                   =\bigcap_{B\in{\cal B}}B.          \tag{6.1}
\]

The first union has order at least \(n+1\), the second intersection at most
\(n+1\), so \(|H|=n+1\).  Every \(A\) is \(H-a_A\), every \(B\) is
\(H+b_B\), and every diamond \((A,B)\) uses the owner \(H\).

### Corollary 6.1 (quantitative biclique collapse)

If \(|{\cal A}|=|{\cal B}|=5\), a colour matching contains at most
\(c_Q(H)\le2\) of the \(25\) diamonds.  Hence every proper colouring of
one occurrence from each pair needs at least

\[
                    \left\lceil{25\over c_Q(H)}\right\rceil
                    \ge13                                      \tag{6.2}
\]

colours; if \(H\) is an anchor it needs \(25\).

The affine refactorization \(N_b=\{e_{x,c}:c=x+b\}\) has a complete
\(K_{5,5}\) projection on any injective lower/upper realization.  It
therefore has no direct five-colour Boolean capacity-slot embedding.
Independently, its abstract support is five-regular, so Theorem 5.1 says
that it is a zero-boundary kernel move even before attempting the lift.

## 7. Sparse \(C_{10}\) switches: useful rerouters, incomplete generators

Use the construction in
\[
\text{\rm MATH\_THEOREM\_CATALAN\_SPARSE\_FIVE\_CYCLE\_PHYSICAL\_SWITCH\_20260731.md}.
\]
Its old and new phases have the same five lower and five upper resources.
With the notation there, the old owners are \(H_i,P_i\) and the new owners
are \(H_i,Q_i\).  Choosing the same labelled \(H_i\)-slot in both phases
gives the exact target boundary

\[
 b_{\cal D}=b_{\cal V}=0,\qquad
 b_{\cal S}=\sum_{i\in{\mathbb Z}_5}
       ({\bf e}_{\xi_{Q_i}}-{\bf e}_{\xi_{P_i}}),    \tag{7.1}
\]

Thus the switch is a genuine five-unit slot transporter.  It has gain zero
and cannot fill an outer leave by itself.  Its role is to clear a
slot-dependency cut or rethread the physical forest before a nonzero-boundary
actuator is used.

There is a universal generation obstruction.

### Theorem 7.1 (outer-sign obstruction)

Fix orders on equal lower and upper outer banks.  Toggling an alternating
\(2\ell\)-cycle changes the sign of the matching permutation by

\[
                             (-1)^{\ell-1}.           \tag{7.2}
\]

Consequently every sparse \(C_{10}\) switch preserves matching sign, and
every sequence of such switches stays in one sign class.

#### Proof

On the \(\ell\) lower vertices of the alternating circuit, the new
assignment is obtained from the old one by one \(\ell\)-cycle.  Its sign is
\((-1)^{\ell-1}\).  For \(\ell=5\) this is \(+1\).  \(\square\)

Both sign classes occur in literal capacity-safe Boolean faces.  Choose an
ordinary rank-\((n+1)\) owner \(H\), distinct \(a,b\in H\), and distinct
\(c,d\notin H\).  The two lower sets

\[
                         H-a,\quad H-b
\]

and upper sets

\[
                         H+c,\quad H+d
\]

form a containment square.  Give the two atoms in either phase the two
different slots at \(H\).  The other four owners are distinct.  Both phases
are physical two-edge paths, while the square toggle is a transposition and
changes matching sign.  Disjoint filler blocks suspend this to arbitrarily
large protected balanced faces.

Therefore the \(C_{10}\)-only exchange graph is disconnected on these
protected balanced faces, and no universal \(C_{10}\)-connectivity theorem
is possible.  This does not assert that both square phases extend to
perfect matchings of every complete fixed-\(Q\) host.
The full \(3\leftrightarrow3\) suspended-hex phase is also a \(3\)-cycle
on its outer matching and hence preserves this sign.  Its planted
\(2\to3\) use leaves the fixed-cardinality matching face and must be
evaluated by the separate boundary ledger.
This sign argument concerns legal matching moves.  The next result shows
that it is not a binary cycle-space obstruction.

### Theorem 7.2 (every Boolean square is a projected difference of two
sparse \(C_{10}\)'s)

For \(n\ge9\), every four-cycle of the full unpunctured rank-\(n\) / rank-
\((n+2)\) inclusion graph belongs both to the projected integral lattice
and to the projected binary span of the sparse \(C_{10}\) phase
differences, where the projection retains only the lower and upper outer
resources.

#### Proof

Write the lower vertices of the square as

\[
                 D_0=S+a,\qquad D_1=S+b,
\tag{7.3}
\]

and its upper vertices as

\[
                 V_z=S+a+b+z,\qquad
                 V_{z'}=S+a+b+z',                  \tag{7.4}
\]

where \(|S|=n-1\).  Choose \(c\in S\), put \(B=S-c\), and use the active
cyclic order

\[
                         (a,c,b,a_3,a_4).            \tag{7.5}
\]

Keep four spectators \(z_1,\ldots,z_4\) fixed.  Form one sparse
\(C_{10}\) with \(z_0=z\) and another with \(z_0=z'\).  Their four
nonzero-index old/new pairs agree.  At index zero their signed phase
differences are respectively

\[
 ({\bf e}_{D_1V_z}-{\bf e}_{D_0V_z}),\qquad
 ({\bf e}_{D_1V_{z'}}-{\bf e}_{D_0V_{z'}}).
\]

Subtracting gives the oriented square; reducing modulo two gives its four
outer edges.  The six auxiliary points \(a_3,a_4,z_1,\ldots,z_4\) can be chosen
disjointly precisely in the asserted range.  \(\square\)

For a fixed punctured host, the three auxiliary lower colours at indices
two, three and four must also survive \(Q\).  Theorem 7.2 therefore gives a
full-host outer-projection identity, not a four-resource kernel and not a
protected fixed-\(Q\) legal sequence.  Its literal-slot boundary need not
vanish.
Indeed the two signed \(C_{10}\)'s need not be simultaneously conformal to
one current matching.  Full outer-projection binary generation is reduced
past the rectangle subspace to the residual Johnson odd-cycle/pentagon
quotient; no spanning theorem for that quotient is claimed here.

### Proposition 7.3 (the bare owner and endpoint boundary)

Let \(F\) contain the old physical edges, and compute every component count
on one fixed spanning owner universe,

\[
                      O=\{H_iP_i:i\in{\mathbb Z}_5\},
\]

put \(F_0=F-O\), and let

\[
                      I=\{H_iQ_i:i\in{\mathbb Z}_5\}.
\]

The bare switch has the pointwise degree change

\[
 d_{F'}(H_i)=d_F(H_i),\qquad
 d_{F'}(P_i)=d_F(P_i)-1,\qquad
 d_{F'}(Q_i)=d_F(Q_i)+1.                            \tag{7.6}
\]

In particular it does not preserve the owner baseline or a fixed endpoint
bank.  If \(e_1(G)\) denotes the number of degree-one vertices, then under
the legality bounds \(d_F(P_i)\in\{1,2\}\) and
\(d_F(Q_i)\in\{0,1\}\),

\[
\begin{aligned}
 e_1(F')-e_1(F)=\sum_i\big(&
 {\bf1}_{d_F(P_i)-1=1}-{\bf1}_{d_F(P_i)=1}\\
 &+{\bf1}_{d_F(Q_i)+1=1}-{\bf1}_{d_F(Q_i)=1}\big). \tag{7.7}
\end{aligned}
\]

Let \(r_{\rm gr}(I/F_0)=c(F_0)-c(F_0+I)\) be the graphic rank gained by
the new edges after contracting the components of \(F_0\).  Then

\[
 c(F')-c(F)=c(F_0)-c(F)-r_{\rm gr}(I/F_0).          \tag{7.8}
\]

These identities follow directly by deleting and adding the displayed
edges.  They show why no fixed five-cycle component formula is valid until
a companion collar closes the \(P_i\to Q_i\) boundary.

### Theorem 7.4 (exact baseline and cycle-breaking criterion)

Let \(F\) be any current physical carrier and let a jointly legal packet
family, private only from the frozen exterior, delete an edge set
\(O\subseteq F\) and add an equal-sized edge set \(I\).  Assume every lower
and upper outer resource is preserved.  Let \(b_F\) be the zero-one
indicator of the unused literal slots.  If \(\xi_{P_i},\xi_{Q_i}\) are the
actual chosen slot labels, let the total sparse-packet displacement be

\[
              d=\sum_{\gamma}y_\gamma d_\gamma,\qquad
 d_\gamma=\sum_i
    ({\bf e}_{\xi_{Q_i}}-{\bf e}_{\xi_{P_i}}).       \tag{7.9}
\]

The replacement is slot-feasible exactly when

\[
                              b_F-d\in\{0,1\}^{\cal S}.          \tag{7.9a}
\]

It preserves the unused baseline pointwise exactly when \(d=0\).
Subject to (7.9a) and the packet conflict rows, the new carrier

\[
                         F'=(F-O)\cup I              \tag{7.10}
\]

is a forest if and only if

1. \(O\) meets every cycle of \(F\), equivalently \(F-O\) is a forest; and
2. \(I\) is independent in the graphic matroid contracted by \(F-O\).

#### Proof

The old and new sparse phases already have equal outer incidence, while
(7.1) gives \(b_{F'}=b_F-d\) on slots.  Put \(K=F-O\).  For the cyclomatic
number \(\beta(G)=|E(G)|-r_{\rm gr}(E(G))\), graphic contraction gives

\[
       \beta(F')=\beta(K)+|I|-r_{\rm gr}(I/K).       \tag{7.11}
\]

Both terms on the right are nonnegative.  They vanish exactly under the two
displayed conditions.  \(\square\)

An exact \(P\)-cover in the full host still has the \(\sigma\) unused slots
from (1.3).  A single bare sparse \(C_{10}\) is capacity-legal exactly when
its five \(Q_i\)-slots are unused and its five \(P_i\)-slots are occupied;
it transports those five baseline units from \(Q\) to \(P\).  It is
impossible only on the face where the unused baseline is frozen pointwise
(equivalently, after that baseline has been deleted from the balanced
host).  On this fixed-baseline face a compound must satisfy \(d=0\).  If
the \(\xi_P(\gamma)\cup\xi_Q(\gamma)\) literal-slot banks of the available
oriented packets are pairwise disjoint, this equation has only the zero
nonnegative solution.  A useful fixed-baseline rerouter bank must overlap
in a deliberately Eulerian slot circulation.  The full
\(3\leftrightarrow3\) suspended-hex phase has zero slot boundary and
therefore cannot cancel a nonzero \(C_{10}\) displacement.

For a max-degree-two carrier, the first row merely says that at least one
old edge is deleted from every pure cycle.  The second says that, after the
resulting path fragments are contracted, the new quotient edges are
loopless and form a forest.  This is a necessary-and-sufficient physical
test, not an average expansion condition.

There is a useful dual obstruction.  If a slot potential \(w\) satisfies

\[
 \langle w,d_\gamma\rangle\ge0
 \quad\hbox{for every currently usable packet }\gamma,         \tag{7.12}
\]

and the inequality is strict for every packet whose old phase meets one
fixed physical cycle \(C\), then every nonnegative fixed-baseline family
with \(d=0\) avoids \(C\).  Hence \(C\) survives.  This is a genuine directed
owner-boundary obstruction even when the unpunctured packet vectors span a
large binary cycle space.

### Theorem 7.5 (directed closed-port cut-and-join)

Augment every physical path by its prescribed socket/reset edge and orient
the resulting components.  Consider a degree-vector-preserving packet which
avoids the reset edges and respects the fixed tail/head bipartition.  Cut
its \(r\) old arcs, label the exposed directed strands, and let \(\alpha\)
be the exterior return permutation.  If the new local phase reconnects
them by \(\tau\), then

\[
                  c_{\rm new}-c_{\rm old}
                     =c(\alpha\tau)-c(\alpha).       \tag{7.13}
\]

If \(r=\ell\) and \(\tau\) is one \(\ell\)-cycle, then

\[
 |c(\alpha\tau)-c(\alpha)|\le \ell-1,\qquad
 c(\alpha\tau)-c(\alpha)\equiv \ell-1\pmod2.        \tag{7.14}
\]

#### Proof

Starting at one cut, traverse its new local arc and then the exterior until
the next cut.  The resulting permutation of cut labels is
\(\alpha\tau\), so its cycles are exactly the new augmented components
meeting the packet.  Equation (7.13) follows.  The bound in (7.14) follows
by inserting an \(\ell\)-cycle, and its parity follows from

\[
                    \operatorname {sgn}\pi=(-1)^{r-c(\pi)}.
\]

\(\square\)

When the five marks of a closed \(C_{10}\) lie in five distinct augmented
components, \(\alpha\) is the identity and the switch merges them into one,
decreasing the component count by four.  The analogous closed \(C_6\)
merges three distinct components and decreases it by two.

Consequently suppose a correlated exact cover has \(K\ge1\) reset-bearing
path components and \(h\) additional pure physical cycles.  Require before
and after every move that each augmented component contain at most one
reset, require every absorption move to avoid merging two reset-bearing
components, and require the terminal state to have exactly one reset in
every augmented component.  If every allowed post-cover packet is an
orientation-coherent closed \(C_6\) or closed \(C_{10}\) kernel switch
preserving this directed reset state, then

\[
                              h\equiv0\pmod2          \tag{7.15}
\]

is necessary for eliminating every pure cycle.  It is sharp at the abstract
component level: partition an even \(h\) into blocks of two and four; for a
two-block use one private closed \(C_6\) meeting the two cycles and one
reset-bearing component, and for a four-block use one private closed
\(C_{10}\) meeting the four cycles and one reset-bearing component.  If
each support is available, slot-closed, socket-neutral, and quotient-
graphic legal, successive switches absorb every block into a component
which retains its unique reset.  Deleting the artificial resets leaves a
forest with the original endpoint bank.

The literal sparse \(C_{10}\) of Proposition 7.3 is not yet such a closed
packet.  Here a closed \(C_{10}\) means that its entire companion owner
collar is topology-neutral and the resulting relative port permutation is
still one \(5\)-cycle.  Slot closure alone is insufficient: a collar may
cut and reconnect extra strands and destroy (7.14).  An even-half-length
sparse switch such as a directed closed \(C_{12}\) changes component parity
by (7.14), but no protected closed-\(C_{12}\) supply theorem is presently
known.

The directed hypothesis is essential.  If the physical packet may reverse
exterior fragments and the carrier is reoriented only after switching,
component parity alone is not invariant.  The exact undirected criterion is
the following.

### Theorem 7.6 (port-pairing form and one-cycle absorption)

Assume the hypotheses of Theorem 7.4, assume \(F\) and \(F'\) have maximum
degree at most two, and impose the fixed-baseline equation \(d=0\), so the
labelled physical degree vector and endpoint multiset are unchanged.  Put
\(K=F-O\).  At every removed edge keep its two labelled half-edge ports.
Pair two ports when they lie at the ends of one retained path component of
\(K\); call this partial matching \(\rho\).  The new edges \(I\) give a
perfect matching \(\mu\) of all ports.
Then

\[
 F' \hbox{ is a forest}
 \quad\Longleftrightarrow\quad
 K\hbox{ is a forest and }\rho\cup\mu
 \hbox{ has no alternating cycle}.                  \tag{7.16}
\]

Indeed, suppressing every retained path of \(K\) turns \(F'\) exactly into
\(\rho\cup\mu\); its alternating paths correspond to physical paths and its
alternating cycles to physical cycles.

If every affected retained component contains two ports and no invariant
degree-one endpoint, then \(\rho\) is perfect.  Hence \(\rho\cup\mu\) is
two-regular and no such exact-resource move can produce a forest.  Every
cycle-breaking bank must reach at least one path-endpoint component.

More sharply, suppose an \(\ell\)-edge exact kernel packet removes one edge
of one physical cycle and \(\ell-1\) edges of one physical path, no other
cycle survives, and all resource rows are exact.  The packet produces one
affected physical path exactly when \(\rho\cup\mu\) is connected.  In that
case it has \(2\ell\) vertices and \(2\ell-1\) edges, so it is an
alternating path; unaffected path components remain separate.
For a planted suspended hex, the two exact terminal phases are

\[
                  O\dot\cup\{t\}\quad\longleftrightarrow\quad N,
 \qquad |O\dot\cup\{t\}|=|N|=3,                    \tag{7.17}
\]

and have identical four-resource incidence.  Thus, only on this
count-neutral terminal face, the planted absorber becomes a genuine closed
\(C_6\) topology bit after the target atom \(t\) is installed.  The gain
activation \(O\to N\) itself is not degree-vector preserving and lies
outside Theorem 7.6.  The terminal \(3\leftrightarrow3\) bit can realize
the one-cycle absorption motif if
its port matching passes (7.16), its terminal orientation can be chosen
coherently, and all recursive/common-cap guards survive.  None of those
three conclusions follows merely from the existence of the planted hex.

### Corollary 7.7 (what remains after the JMS no-go)

The direct Joos--Mubayi--Smith tripartite exact-cover route is already
excluded by the fixed-\(Q\) exponent contradiction in

\[
\text{\rm MATH\_THEOREM\_CATALAN\_JMS\_TRIPARTITE\_C6\_MACRO\_EXPONENT\_NOGO\_20260731.md}.
\]

Even counterfactually granting such an exact outer cover with planted
hexes, sparse-cycle existence alone would not finish the physical row.  One
must still exhibit a packet choice satisfying either baseline feasibility
(7.9a) or the fixed-baseline slot kernel \(d=0\), the cycle-hitting and
contracted-graphic rows of Theorem 7.4, and either the
directed parity condition (7.15) or the endpoint-reaching port condition
(7.16), together with coherent final orientation.  Thus the surviving
target is correlated planting plus endpoint recursion/common-cap and a
closed cycle-routing bank, not another application of the global JMS black
box.

## 8. Exact directed release and the \(C_{10}\)+absorber interface

Take two literal occurrence-labelled capacity-slot matchings \(R,B\).
Form their outer symmetric difference in the occurrence-labelled
multigraph: atoms with the same pair \((D,V)\) but different slot lifts are
parallel and form a two-cycle rather than being projected away.  Freeze
exact common atoms and contract every remaining alternating component.
Let \({\cal Z}\) be the component set.
For \(S\subseteq{\cal Z}\), choose the \(B\)-phase on \(S\) and the
\(R\)-phase elsewhere.  Draw an arc

\[
                         Z\longrightarrow Z'          \tag{8.1}
\]

whenever a \(B\)-atom in \(Z\) and an \(R\)-atom in \(Z'\) use the same
labelled slot.

### Theorem 8.1 (phase closure and terminal leave)

The phase hybrid is a slot matching if and only if \(S\) is out-closed in
the dependency digraph.  Its outer leave is

\[
 L_{\rm common}\ \dot\cup\
 \bigdotcup_{Z\in S}T_R(Z)\ \dot\cup\
 \bigdotcup_{Z\notin S}T_B(Z),                       \tag{8.2}
\]

where \(T_R(Z)\) and \(T_B(Z)\) are the phase-exclusive outer terminals.

#### Proof

Whole alternating components in the occurrence-labelled outer multigraph
make every hybrid an outer matching.  Since \(R\) and \(B\) are themselves
slot matchings, the only possible slot failure is a cross-phase collision.
Choosing \(B\) at \(Z\) forces \(B\) at every \(Z'\) reached by such a
shared slot, which is exactly out-closure.  Common outer resources are
covered in either phase.  A resource appearing only in phase \(R\) is a
hole precisely when phase \(B\) is chosen, and conversely, proving (8.2).
\(\square\)

With forced \(B\)-components \(I\) and forced \(R\)-components \(O\), after
deleting a set \(J\) of dependency arcs there is a phase containing \(I\)
and avoiding \(O\) if and only if the residual digraph has no directed
\(I\)-to-\(O\) path.  If every arc has one independent private release
packet, the minimum packet number is the directed \(I\)-\(O\) min cut.

For sparse \(C_{10}\) packets, write \(P(\gamma)\) for the five old slots
vacated and \(Q(\gamma)\) for the five new slots occupied.  A private
packet family is a legal release bank when

1. every required collision slot belongs to the union of the selected
   \(P(\gamma)\)'s;
2. every selected \(Q(\gamma)\) is free, or is freed by the same closed
   packet family;
3. no new dependency arc is created;
4. after deleting the old physical edges, the new edges are independent in
   the contracted graphic matroid; and
5. the packet is transparent for the other four colours, the
   Delcourt--Postle configurations, and the endpoint/socket state.

These are exact finite rows.  Under the stronger unit-effective condition
that every packet has one designated collision slot and all other boundary
slots are private, ordinary Hall on collision-to-packet menus selects a
simultaneous family satisfying the slot-release rows 1--3.  Rows 4--5 still
require a joint graphic/configuration test unless their independence has
been included explicitly in the private-menu hypothesis.

After release, planted \(2\to3\) actuators may absorb an edge-aligned leave
provided their nonzero boundaries sum to that leave, their supports are
private, and their packet blockers satisfy the self-breaking/circuit-
deadline conditions.  Sparse \(C_{10}\)'s contribute no outer boundary, so
the actuators, not the rerouters, must supply every missing lower and upper
resource.

Matching sign remains a separate row.  Closing every nonzero-boundary
actuator against its reserved target gives it a parity signature in
\({\mathbb Z}_2\).  Since all \(C_{10}\)'s have signature zero, the selected
actuator signatures must sum to the required terminal sign; otherwise no
composition reaches the desired factor.  No odd-sign actuator bank is
proved here.

There is also a permanent-arc obstruction.  An arc witnessed at a
capacity-one owner is immutable whenever both incident outer pairs are
pointwise protected: the pair \((D,V)\) fixes its two physical owners and
capacity one fixes the slot.  In the authenticated \(n=3\) locked-\(C_6\)
fixture, the two cross-arcs are witnessed by

\[
\begin{array}{c|c|c}
\text{slot}&B\text{-pair}&R\text{-pair}\\ \hline
30&(28,31)&(26,62)\\
27&(26,59)&(19,31).
\end{array}                                           \tag{8.3}
\]

Protecting these four pairs leaves only the two constant phases.  A
path-dependent endpoint bank fixes global endpoints, not all four internal
cap pairs, so this is a scoped protected-pair obstruction rather than a
no-go for the pointed-\(C_5\) bank.

## 9. Whole-path alignment is a three-sector Hall property

Assume all hypotheses of the cited socket theorem: the three sector forests
have the same component order, their internal palettes and endpoint-deficit
ledgers are exact, and \(\kappa\) is a bijection.  Write their oriented
components as

\[
 T_i:A_i^0\to A_i^1,\qquad
 M_j:X_j^0\to X_j^1,\qquad
 B_k:L_k^0\to L_k^1.
\tag{9.1}
\]

Let the path-dependent complement pairing satisfy

\[
                    L_{\kappa(i)}^1=\Omega\setminus A_i^0.       \tag{9.2}
\]

The completed side records concatenate into residual complement geodesics
if and only if the socket graph

\[
 i\sim j
 \quad\Longleftrightarrow\quad
 X_j^0\subset A_i^1
 \ \hbox{ and }\
 L_{\kappa(i)}^0\subset X_j^1                         \tag{9.3}
\]

has a perfect matching.  Equivalently,

\[
                         |N(S)|\ge|S|                 \tag{9.4}
\]

for every top-component set \(S\).  This is Theorem 8.1 of
\[
\text{\rm MATH\_THEOREM\_K\_CATALAN\_ANTIPODAL\_FILLER\_LOWER\_CIRCUITS\_PORT\_PARITY\_AND\_RECURSION\_OBSTRUCTIONS\_20260731.md}.
\]

Therefore an aligned-colour density can only be defined relative to a
joint state consisting of three sector records, orientations, compatible
\(E,Q\), an endpoint bank, and the socket matching.  The canonical
parameter-three Dyck endpoint bank has no AGCF, while the \(72\) viable
banks are exactly the pointed five-cycle banks.  This is why a fixed
canonical endpoint state cannot be inserted after the colour selection.

## 10. Exact remaining theorem

The unrestricted positive-density statement is refuted in three precise
senses:

1. literal raw leaves have the nonzero affine baseline \(\sigma\);
2. every-\(Q\) normalized completion is false by the authenticated
   parameter-three \(8>7\) capacity cut; and
3. hereditary/local normalized completion is false by Theorem 3.1, even
   with near-ceiling classes and \(n\mid\delta\).

The full dense, bank-flexible large-\(n\) statement remains open.  Its
minimum useful form is:

> Choose one compatible path-dependent endpoint/common-basis state and a
> full-host conflict-free colouring such that a positive density of
> three-sector colour records have (i) enough four-resource/pathwise
> co-omission to satisfy (1.6), (ii) the contracted graphic row,
> (iii) the socket Hall row, and (iv) a terminal-bearing sparse packet bank
> whose directed release cuts are complete.  The selected topology packets
> must additionally satisfy the allowed baseline migration (or form an
> Eulerian slot circulation when the baseline is fixed), hit every physical
> cycle, and pass the contracted-graphic/alternating-port test (7.16).

Equivalently, one may bypass density and prove one protected global
many-colour recolouring with those rows.  The Delcourt--Postle class-size
and one-resource ledgers prove none of the required higher-order
co-omission, terminal-flow, sign, or socket correlations.

## 11. Adversarial audit

1. The induced-face obstruction is a literal Boolean subhost but not the
   complete \({\cal H}_Q\); exterior rescue is explicitly left open.
2. The affine baseline is removed before candidate-semigroup claims.
3. The five-colour boundary theorem concerns the complete packet support.
   A packet embedded in global colours needs colour-closure and
   configuration transparency.
4. The \(K_{5,5}\) theorem rules out only the direct affine embedding, not
   sparse five-colour or status-migrating packets.
5. Matching-sign invariance obstructs legal \(C_{10}\) exchange
   connectivity.  Theorem 7.2 explicitly shows why it is not an
   \({\mathbb F}_2\)-cycle-space non-generation proof; its identity is a
   full-host outer-projection identity and need not survive a fixed
   puncture.
6. Internal acyclicity of either sparse phase does not imply acyclicity
   beside a retained forest; the contracted graphic row is retained.
7. The \(2\to3\) absorbers are invoked only conditionally after a literal
   fixed-host realization and the parity/guard rows.  AGCF paths are not
   silently identified with side atoms.
8. A bare sparse \(C_{10}\) is never called all-resource-neutral.
   Baseline feasibility (7.9a), or \(d=0\) on a fixed-baseline face, is
   required.
9. The component-parity claim in Theorem 7.5 is scoped to fixed directed
   tail/head and reset data.  When exterior fragments may be reversed, the
   exact criterion is Theorem 7.6, not parity.
10. Joos--Mubayi--Smith is cited only for its proved exponent no-go in this
    host.  The post-cover cycle statements are counterfactual sufficient and
    obstruction theorems for a different correlated cover construction.
