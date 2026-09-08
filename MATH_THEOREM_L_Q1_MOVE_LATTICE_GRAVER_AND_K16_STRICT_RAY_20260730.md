# The q1-neutral move lattice: alternating components, augmented Graver packets, and the K16 strict short-cycle ray

Date: 2026-07-30

Status: general algebraic theorem plus a hash-pinned finite certificate for the
repaired asymmetric `k=16` factor.  The certificate closes the authenticated
deep-safe, gainful `C3/C4/C5` catalogue even fractionally.  It does not close
catalogues containing deep-unsafe, non-gainful, overlapping, or longer atoms.

## 1. Three different objects

Let \(V\) be the middle layer and split a directed copy of it into tails
\(V^-\) and heads \(V^+\).  A successor permutation is a perfect matching
in the allowed bipartite graph \(G\subseteq V^-\times V^+\).  Let \(B\) be
its tail--head incidence matrix.  Let \(Q\) send an allowed directed Johnson edge
to its two literal q1 colours, one lower and one upper.

Fix a source matching \(M_0\).  An alternating component \(c\) is oriented
positive on new matching edges and negative on \(M_0\)-edges, so

\[
Bc=0,\qquad d(c):=Qc.
\tag{1.1}
\]

There are three notions which must not be identified.

1. A **degree circuit** is an alternating cycle of the matching matrix \(B\).
2. A **q1 circuit packet** is a nonempty, coordinate-minimal nonnegative
   integer relation among the signed columns \(d(c)\).
3. An **executable factor exchange** is a squarefree edge vector which, when
   added to the source, is still a simple Johnson two-factor and passes every
   chronological constraint.

The first is a local matching object.  The second is a Graver/Hilbert object
in generator-coordinate space.  The third additionally requires positivity,
simplicity, and literal chronology.

## 2. Exact alternating decomposition

### Theorem 2.1 (matching decomposition and the q1 packet lattice)

Let \(M_0,M_1\) be perfect matchings of the same allowed bipartite graph.
Then

\[
z={\bf1}_{M_1}-{\bf1}_{M_0}
\tag{2.1}
\]

is squarefree and its nonzero support is a disjoint union of even alternating
cycles \(c_1,\ldots,c_t\).  Every subfamily of these cycles is again an
executable perfect-matching exchange.  Moreover,

\[
Q{\bf1}_{M_1}=Q{\bf1}_{M_0}
\quad\Longleftrightarrow\quad
\sum_{j=1}^t d(c_j)=0.
\tag{2.2}
\]

If a nonempty subfamily \(S\) is inclusion-minimal subject to
\(\sum_{j\in S}d(c_j)=0\), its indicator \({\bf1}_S\) is a positive Graver
element of the signature matrix

\[
D=(d(c_1)\ \cdots\ d(c_t)).
\tag{2.3}
\]

Conversely, a binary positive Graver element of \(D\) is an
inclusion-minimal exact-q1-neutral subfamily.

#### Proof

Every vertex of the symmetric difference \(M_0\triangle M_1\) has degree
zero or two, with old and new edges alternating.  This proves the cycle
decomposition and the perfect-matching claim.  Applying \(Q\) gives (2.2).

For the last assertion, a conformal integer subvector of a zero-one vector is
again zero-one.  Thus a conformal decomposition of \({\bf1}_S\) in
\(\ker_{\mathbb Z}D\) is exactly a partition off of a nonempty proper
zero-sum subfamily.  Minimality is therefore equivalent to Graver
indecomposability in the positive orthant.  \(\square\)

This theorem is exact for the directed matching.  To obtain a simple
undirected two-factor, one must also exclude a reciprocal pair of arcs that
would use the same undirected edge twice.  Residence and deeper shadows are
not properties of the matching matrix and require separate checks.

## 3. The token-flow quotient and where network integrality stops

On the pure \(B\)-rail of the repaired asymmetric factor, every upper q1
colour occurs exactly once.  Pair each deleted \(BB\) edge with its new edge
and draw the old-upper-token to new-upper-token arrow.  If \(N\) is the
vertex--arc incidence matrix of this token digraph and \(A\) records all token
arcs belonging to each port-cycle generator, then

\[
D_{U_z}=NA.
\tag{3.1}
\]

### Proposition 3.1 (flow characterization)

A pure-\(B\) packet is upper-q1 neutral if and only if its aggregate token
arcs form an Eulerian directed multigraph.  With individual token arcs as
variables, the nonnegative primitive relations are exactly directed simple
cycles.

#### Proof

The signed load at a token is indegree minus outdegree.  Hence neutrality is
zero divergence.  Every nonzero integral circulation decomposes into directed
cycles, and a coordinate-minimal nonnegative circulation is one simple
directed cycle.  \(\square\)

The port-cycle variables are grouped columns of \(A\): one may not normally
take only one token arrow from a port cycle.  Lower-q1 signatures and deep
collars couple the groups further.  Therefore the actual matrix is of the
form

\[
\begin{pmatrix}NA\\D_{\rm lower}\\D_{\rm deep}\end{pmatrix},
\tag{3.2}
\]

and need not be a network matrix or totally unimodular.  Smith normal form
of (3.2) correctly gives the integer kernel and its congruence quotient, but
does not impose nonnegativity, coefficient one, conflict-freeness, or
chronology.  The relevant finite test set is its positive Graver/Hilbert
basis, followed by executability.

In particular, the real circuit support bound `rank+1` is not a binary move
bound.  Clearing denominators of a small real dependence may require a
coefficient greater than one on a generator whose physical collar can be
used only once.

## 4. A protected-load augmented Graver theorem

The next statement explains exactly what is gained by admitting individually
unsafe or non-gainful atoms.

Let \(p_1,\ldots,p_n\) be base-relative atoms.  Assume that every compatible
selection \(x\in\{0,1\}^n\) has additive protected-load change \(Cx\), and
that compatibility is hereditary under taking a sub-selection.  Let
\(s\ge0\) be the source slack above the required load one.  Thus \(x\) is
protected-safe precisely when

\[
s+Cx\ge0.
\tag{4.1}
\]

Some rows may be declared exact-neutral, in which case \(Cx=0\) is required
on those rows.  Let \(g\in\mathbb Z^n\) be any additive gain functional.

### Theorem 4.1 (safe augmented-Graver extraction)

If a compatible binary selection \(x\) satisfies (4.1), is exact on the
declared neutral rows, and has \(g^Tx>0\), then it contains a nonempty
sub-selection \(y\le x\) such that

1. \(y\) is compatible and protected-safe;
2. \(Cy=0\) on every declared exact-neutral row;
3. \(g^Ty>0\); and
4. \((y,Cy)\) is a gain-positive Graver element of

   \[
   \widehat C=(C\ -I).
   \tag{4.2}
   \]

Thus the selected subpacket itself is an augmented-Graver element, not just
a packet containing one algebraically.

#### Proof

The vector

\[
\widehat x=(x,Cx)
\tag{4.3}
\]

lies in \(\ker_{\mathbb Z}\widehat C\).  Decompose it conformally into
Graver elements \(\widehat y_j=(y_j,Cy_j)\).  Since the first block \(x\)
is binary and nonnegative, each \(y_j\) is a nonempty binary sub-selection
and their supports partition that of \(x\).  Hereditary compatibility makes
each \(y_j\) executable at the base matching level.

Fix a protected row.  If \((Cx)_r\ge0\), conformality gives
\((Cy_j)_r\ge0\).  If \((Cx)_r<0\), it gives

\[
0\ge (Cy_j)_r\ge (Cx)_r\ge-s_r.
\tag{4.4}
\]

Thus every \(y_j\) satisfies (4.1).  If \((Cx)_r=0\) on an exact row,
conformality forces \((Cy_j)_r=0\).  Finally
\(g^Tx=\sum_jg^Ty_j>0\), so some summand has positive gain.  Choose it.
\(\square\)

The additivity hypothesis is decisive.  Separated frozen collars satisfy it.
Overlapping or sequential collars whose shadows must be recomputed do not;
their whole literal compound must first be exported as one new atom.
Likewise, a nonlinear distinct-hole objective must be represented by exact
load/service variables before applying Theorem 4.1.

## 5. Peeling is a strict Gordan certificate

Let \(D\in\mathbb Z^{R\times n}\) be signed columns on source-tight rows.
Start with \(I_0=[n]\).  In round \(r\), choose rows \(W_r\) such that

\[
D_{wi}\le0\qquad(w\in W_r,\ i\in I_{r-1}),
\tag{5.1}
\]

and delete every column assigned to a row on which it is strictly negative.
Let the survivors be \(I_r\).

### Theorem 5.1 (peeling-to-Gordan)

If finitely many rounds leave \(I_R=\varnothing\), then

\[
Dx\ge0,\quad x\ge0
\tag{5.2}
\]

has only the zero solution.  Moreover nonnegative weights on the rows
\(W_1\cup\cdots\cup W_R\) can be chosen so that

\[
\alpha^TD_i<0\qquad(i=1,\ldots,n).
\tag{5.3}
\]

#### Proof

For (5.2), take a nonzero \(x\ge0\) and let \(r\) be the earliest deletion
round of a column in its positive support.  At the beginning of round \(r\),
every column in that support is alive.  The assigned witness row is
nonpositive on all of them and strictly negative on one with positive
coefficient.  Hence that coordinate of \(Dx\) is negative.

For (5.3), sum the chosen witness rows within each round.  The round-\(r\)
sum is nonpositive on all round-\(r\) survivors and strictly negative on
every column killed in that round.  Give earlier-round sums successively
large positive weights, working backwards.  Finiteness and integrality make
all inequalities strict.  This is also Gordan's alternative.  \(\square\)

## 6. Exact K16 certificate

The source is

`scratch/k16_asymmetric_triangle_orbit_repair_20260729.json`,

SHA-256

`6044bd63b7281c358c6c33399ccf2dd15143f783535cb6fe6b85a797c04affdc`.

It is the literal triangle-orbit repair with lower-q2 holes (45) and
upper-q3/arbitrary-rank-11 holes (63), reduced from (78).

The authenticated catalogue

`scratch/k16_asymmetric_signed_compound_cycle_catalogue_20260730.json`

has SHA-256

`23984ea67f6d9275efa0de337c85a58bd23ff0bb6763af5de01a30f1d3305817`

and consists of all (1263) exported individually deep-safe, gainful
separated port cycles of lengths three through five:

\[
95+180+988=1263.
\tag{6.1}
\]

The frozen peeling certificate kills (1235) columns and then (28).  Pick
the stored witness of each killed column.  Their distinct row sets have

\[
|W_1|=732=312_{\rm lower}+420_{\rm upper},\qquad
|W_2|=28=14_{\rm lower}+14_{\rm upper},
\tag{6.2}
\]

and \(W_1\cap W_2=\varnothing\).  Every one is a source-load-one q1 row.
The exact exported columns satisfy

\[
\boxed{\alpha=2{\bf1}_{W_1}+{\bf1}_{W_2},\qquad
       \alpha^TD_i\le-1\quad(1\le i\le1263).}
\tag{6.3}

The coefficient two is exact and sufficient: a first-round-killed column
has \(W_1\)-value at most \(-1\), while its positive \(W_2\)-mass is at
most one.  A second-round column has nonpositive \(W_1\)-value and
\(W_2\)-value at most \(-1\).

The complete value histogram is

\[
\begin{array}{c|rrrrrrr}
\alpha^TD_i&-10&-6&-5&-4&-3&-2&-1\\ \hline
\#i&3&111&24&366&16&698&45.
\end{array}
\tag{6.4}
\]

Consequently, for every nonzero real vector \(x\ge0\),

\[
\alpha^TDx<0.
\tag{6.5}
\]

But q1 safety on the tight rows would give \(Dx\ge0\), hence
\(\alpha^TDx\ge0\).  Thus the catalogue contains no nonzero fractional,
integer, or binary q1-safe compound.  Conflict, cut-separation, and deep rows
are not used in this last contradiction.

The fail-closed lightweight replay is

`scratch/audit_k16_short_cycle_peeling_gordan_20260730.py`.

It hash-pins the source, catalogue, and peeling audit and checks every one of
the (1263) inequalities (6.3).  It performs no cycle enumeration or solve.

## 7. What the present negatives imply about minimum support

The supplied single-cycle census reports no q1-safe, selected-deep-safe
positive port cycle through length seven.  Its resource record does not
byte-pin the executed binary to the retained frozen C++ source, so this
exhaustive minimum-length conclusion is scoped to the supplied census.  The
length-eight census has fifteen such cycles, one free rotation orbit.  They
are q1-coverage-safe but not exact-q1 neutral: each spends four
source-load-two rows.  Applying the complete orbit gives the independently
audited \(108\to93\) repair.

The exact consequences are:

1. Within the supplied census, a successful selected-ledger-safe **single**
   port-cycle atom has length at least eight, and equality is attained by the
   frozen C8 orbit.
2. No compound of any cardinality drawn only from the authenticated
   deep-safe, gainful \(C3/C4/C5\) catalogue can work, even fractionally.
3. Any successful compound of cycles of length at most seven must contain at
   least two atoms and at least one atom outside that catalogue: a length-six
   or length-seven atom, an individually deep-unsafe atom, an individually
   non-gainful atom, a close/interacting collar, or an atom scored by a
   broader arbitrary-width service ledger.
4. For a base-relative compatible family of disjoint port cycles, each cycle
   has at least two cuts, so the physical cut floor supplied by these facts is
   only four.  If one atom is from the \(C3/C4/C5\) catalogue, the floor is
   five.  Overlapping stateful moves require recomputation as one atom and are
   outside this cut count.

No larger support floor follows formally.  Two abstract atoms can have
signatures \(d\) and \(-d\), deep effects \(-h\) and \(h\), and gains one and
zero.  Neither is a safe positive singleton, while their pair is neutral,
deep-safe, and gainful.  This two-atom model satisfies all of the stated
single-atom negatives.  Therefore a claimed support-six, support-eight, or
macroscopic lower bound needs the actual columns of the unsafe/non-gainful
catalogue, not Smith rank or the existing short safe catalogue.

## 8. The exact gate for an enlarged catalogue

Let \(I\) be the old 1263 columns and \(J\) newly exported unsafe,
non-gainful, or longer columns.  Every q1-safe selection obeys the dual budget

\[
\sum_{j\in J}[\alpha^TD_j]_+x_j
\ge
\sum_{i\in I}(-\alpha^TD_i)x_i
+\sum_{j\in J}[-\alpha^TD_j]_+x_j.
\tag{8.1}
\]

In particular, a selection using any old column must use a new column of
strictly positive \(\alpha\)-score.  A new column of score zero or negative
cannot by itself unlock the old cone.  Equation (8.1) is the cheapest exact
filter for the next export.

After this dual filter, form the full protected signature matrix \(C\), not
only q1, and seek binary positive augmented-Graver elements of
\((C\ -I)\).  Each surviving algebraic element must then pass:

1. coefficient-one use of each physical collar;
2. disjoint deleted edges and distinct legal added edges;
3. no reciprocal-arc collapse in the undirected factor;
4. exact degree and successor permutation;
5. additive collar separation, or a fresh literal replay when collars
   overlap; and
6. residence and arbitrary-width shadow replay.

This is the precise algebra/geometry boundary.  Alternating cycles generate
the matching fibre, and Graver packets generate its q1/protected-load
subfibre, but neither statement alone compiles a chronological Johnson
two-factor.

## 9. Proved boundary

The strict ray (6.3) puts the entire authenticated C3/C4/C5 gainful
selected-deep-safe cone on the wrong side of one tight-q1 hyperplane.  The
complete C8 orbit has score zero on this ray and escapes on its boundary
face; it does not contradict the strict inequality, whose column set stops
at C5.  The exact owner-plus-q1 circuit minimum and the all-depth analysis on
the resulting factor are proved separately in
`MATH_THEOREM_L_K16_EXACT_Q1_LATTICE_AND_ALL_DEPTH_C9_TRAP_20260730.md`.
