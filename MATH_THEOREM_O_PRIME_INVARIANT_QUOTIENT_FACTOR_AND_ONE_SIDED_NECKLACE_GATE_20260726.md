# Prime cyclic invariant wreath factors: exact voltage normal form, necklace flows, and the nonlinear difference-family gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.  The dense-subsequence transfer theorem in
`MATH_THEOREM_DENSE_SUBSEQUENCE_TRANSFER_FOR_CONSTANT_ONE_20260726.md`
is treated as proved; this report addresses only the invariant prime
construction.

## 0. Outcome

Let

\[
                 p=2m+1\equiv1\pmod4
\tag{0.1}
\]

be prime, let \(\rho:x\mapsto x+1\) act on \(\mathbb F_p\), and put

\[
 W=\binom pm,\qquad T={W\over p}=\operatorname {Cat}_m,
 \qquad \mathcal N_r=\binom{\mathbb F_p}r/\langle\rho\rangle.
\tag{0.2}
\]

Thus \(|\mathcal N_m|=T\), and \(m\) is even.  The exact conclusions are
as follows.

1. A \(\rho\)-invariant exact middle wreath factor is equivalent to a
   spanning voltage two-factor of the quotient odd graph consisting of
   exactly two nonzero-voltage AP loops and

   \[
                       {T-2\over p}
   \tag{0.3}
   \]

   pairwise vertex-disjoint simple \(p\)-cycles of voltage zero.  This is
   both necessary and sufficient.  It is a characterization, not an
   existence theorem.
2. The complete lower-shadow contribution of such a factor is an exact
   necklace difference family.  A free quotient cycle contributes, at
   depth \(q\), the multiplicity vector of its \(p\) every-second
   \((m-q)\)-windows.  An AP loop contributes **one**, not \(p\), to the
   load of its unique AP target necklace: its \(p\) physical intervals
   are the \(p\) different phases of that necklace.  Hence physical lower
   holes satisfy

   \[
        M_q^-=p\,\#\{O\in\mathcal N_{m-q}:k_q(O)=0\}.
   \tag{0.4}
   \]

   Covering all but \(o(T)\) quotient targets through a growing window is
   therefore exactly the physical one-sided \(o(W)\) target.
3. There is no marginal or laminar algebraic Hall obstruction.  For every
   \(H<m\), the layered quotient inclusion graph admits \(T\) integral
   nested deletion paths, one from each middle necklace, for which every
   depth-\(q\) target load is one of

   \[
              c_q=\left\lfloor{W\over N_q}\right\rfloor,
              \qquad c_q+1,
              \qquad N_q=\binom p{m-q}.
   \tag{0.5}
   \]

   In particular every lower necklace is covered at \(q=1\).  The paths
   lift to translation-equivariant literal nested flags.  What is missing
   is their grouping into common rows whose reciprocal odd edges close
   into the cycles in Item 1.
4. The normalized quotient has an exact edge-label model.  If
   \(A_i\) is the zero-sum representative of a quotient vertex and the
   edge label is \(y_i\), then

   \[
       A_{i+1}=T_{y_i}(A_i),\qquad
       T_y(A)=\bigl(\mathbb F_p\setminus(A\cup\{y\})\bigr)-2y,
   \tag{0.6}
   \]

   and a closed free packet has \(\sum_i y_i=0\).  If

   \[
             s_0=0,qquad s_{i+1}=s_i+2y_i,qquad
             z_i=s_i+y_i,
   \tag{0.7}
   \]

   then \((z_i)\) is the omitted-coordinate permutation of the lifted
   wreath.  Consequently all its finite-field power sums are those of
   \(\mathbb F_p\).
5. This gives a sharp no-go for the first algebraic ansatz.  If the
   quotient voltage schedule is affine in the cycle index,

   \[
                              y_i=\alpha i+\beta,
   \tag{0.8}
   \]

   then

   \[
                              z_i=\alpha i^2+2\beta i+\beta.
   \tag{0.9}
   \]

   For \(\alpha\ne0\) this is not injective; for \(\alpha=0\), the only
   permutation case is an AP wreath, which projects to a loop rather than
   a simple free \(p\)-cycle.  Thus no affine-voltage free packet exists.
   Likewise the affine normalizer of \(\langle\rho\rangle\) induces a
   group of order \(p-1\) on necklaces and has no orbit of length \(p\).
   A root-scale AGL-orbit construction cannot supply the free cycles.
6. Extra homogeneous symmetry is sharply obstructed.  A multiplicative
   stabilizer has order at most four.  Reflection symmetry requires
   \(\binom m{m/2}\le(T-2)/p+2\), which fails at \(p=13\); order-four
   symmetry is impossible for \(p\equiv1\pmod8\).  These cuts do not
   obstruct a fully asymmetric translation-only factor.
7. The canonical MSW/Chung--Feller factor does not furnish the missing
   invariant factor.  With the natural identification
   \(\infty=0\), translation followed by recutting at the new infinity
   acts on an omitted-label permutation by the explicit cut transform
   (8.4).  Every canonical MSW permutation starts with an even label,
   whereas the shifted mountain row starts with \(3\) and ends with
   \(1\).  Neither orientation belongs to the MSW catalogue.  Thus there
   is no induced shift action on its Dyck row indices.
8. Almost every row packet is simultaneously necklace-rainbow through
   every mesoscopic window \(H=o(m)\), and the good literal cycle catalogue has
   a fractional middle nearpacking/lower cover with only exponentially
   small exceptions.  Nevertheless its middle cycle hypergraph obeys
   \(\Delta_2\ge2D/(m+1)\), so the atomic growing-rank nibble condition
   \(\Delta_2=o(D/p)\) fails by a factor bounded away from zero.

No explicit nonlinear difference family satisfying the middle partition
and the growing-window lower cover is constructed here.  No positive-
density obstruction against an unrestricted nonlinear zero-voltage factor
is proved either.  The exact surviving object is the common nonlinear
cycle chronology in Sections 4 and 7 below.  In particular, coefficient
one is not claimed.

## 1. The quotient voltage graph

Every nonempty proper subset of \(\mathbb F_p\) has a free translation
orbit.  Hence the quotient of the odd graph

\[
                       O_p=KG(p,m)
\tag{1.1}
\]

by \(\langle\rho\rangle\) has \(T\) vertices.  Each middle necklace has a
unique zero-sum representative:

\[
 \mathcal Z_m=
 \left\{A\in\binom{\mathbb F_p}m:\sum_{x\in A}x=0\right\}.
\tag{1.2}
\]

Indeed translation by \(t\) changes the sum by \(mt\), and

\[
                              m^{-1}=-2\pmod p.
\tag{1.3}
\]

For \(A\in\mathcal Z_m\) and \(y\notin A\), define \(T_y(A)\) by
(0.6).

### Lemma 1.1 (normalized neighbor and voltage)

The \(m+1\) quotient neighbors of \(A\) are precisely the
\(T_y(A)\), \(y\notin A\).  With the convention that the lifted neighbor
is \(T_y(A)+2y\), the oriented edge has voltage \(2y\), and

\[
                              T_{-y}(T_y(A))=A.
\tag{1.4}
\]

#### Proof

The physical odd-graph neighbor obtained by omitting \(y\) is

\[
                         D_y=\mathbb F_p\setminus(A\cup\{y\}).
\tag{1.5}
\]

It has sum \(-y\).  Translating it by \(-2y\) changes its sum by
\(m(-2y)=y\), so its zero-sum representative is \(T_y(A)\), and
\(D_y=T_y(A)+2y\).  Also

\[
 \mathbb F_p\setminus T_y(A)
 =(A\cup\{y\})-2y=(A-2y)\cup\{-y\}.
\tag{1.6}
\]

Deleting \(-y\) and translating by \(2y\) recovers \(A\), proving
(1.4). \(\square\)

For a quotient walk

\[
 A_0\xrightarrow{y_0}A_1\xrightarrow{y_1}\cdots
 \xrightarrow{y_{\ell-1}}A_\ell,
\tag{1.7}
\]

the total voltage is \(2\sum_i y_i\).  A simple quotient \(p\)-cycle
lifts to \(p\) physical \(p\)-cycles exactly when this sum is zero.  A
nonzero-voltage quotient loop lifts to one physical \(p\)-cycle.

### Lemma 1.2 (the loops are exactly AP wreaths)

A quotient loop is a translation-stable arithmetic-progression wreath.
There are exactly \(m=(p-1)/2\) underlying loop rows, indexed by a
nonzero slope modulo sign.

#### Proof

The loop equation is

\[
             \mathbb F_p=A\ \dot\cup\ \{y\}\ \dot\cup\ (A+2y).
\tag{1.8}
\]

Along the cyclic order with step \(2y\), membership in \(A\) alternates
away from the single omitted point.  This uniquely gives every other
point in that AP order.  Reversal replaces \(y\) by \(-y\).  Conversely
an AP wreath has this alternating partition. \(\square\)

## 2. Exact invariant-factor classification

Call a nonfixed row **free**.  Its translation orbit has \(p\) rows.  If
these rows occur in an exact middle factor, their middle supports are
pairwise disjoint.  Therefore the projected quotient walk is simple.  One
physical lift is already closed, so its voltage is zero.  Conversely a
simple zero-voltage quotient \(p\)-cycle lifts to \(p\) disjoint wreath
rows.

### Theorem 2.1 (two loops plus a zero-voltage \(C_p\)-factor)

For prime \(p=2m+1\equiv1\pmod4\), the following are equivalent.

1. There is a \(\rho\)-invariant exact middle wreath factor.
2. In the quotient voltage graph there are two AP loops and
   \((T-2)/p\) pairwise vertex-disjoint simple \(p\)-cycles of voltage
   zero whose vertex sets, together with the two loop vertices, partition
   \(\mathcal N_m\).

#### Proof

Every factor row orbit has size one or \(p\).  The fixed rows are exactly
the AP rows by Lemma 1.2.  If \(f\) is their number, then

\[
                               f\equiv T\pmod p.
\tag{2.1}
\]

Since \(m\) is even,

\[
 T={1\over m+1}\binom{p-1}m
   \equiv2(-1)^m=2\pmod p.
\tag{2.2}
\]

There are only \(m<p\) AP rows, so (2.1) forces \(f=2\).  Every free
orbit gives one simple zero-voltage quotient \(p\)-cycle by the preceding
paragraph.  Exact middle ownership makes their quotient vertex sets and
the two loop vertices a partition.  Counting gives \((T-2)/p\) cycles.

Conversely lift every zero-voltage cycle.  The simple-cycle and
vertex-disjointness hypotheses make all lifted free row orbits mutually
middle-disjoint.  Add the two AP wreaths represented by the loops.  The
quotient partition says that every physical middle set occurs once.
Hence the result is an invariant exact factor. \(\square\)

For \(p=13,m=6\), this asks for two of the six AP loops and ten
zero-voltage \(13\)-cycles on the remaining \(130\) of the
\(T=132\) quotient vertices.  The theorem does not assert that this
finite instance, or the general instance, has a solution.

There is an equivalent successor-selector form which is useful for
testing proposed algebraic formulae.

### Corollary 2.2 (exact selector normal form)

A \(\rho\)-invariant exact factor is equivalent to a choice

\[
                         y(A)\in\mathbb F_p\setminus A
                         \qquad(A\in\mathcal Z_m)
\tag{2.3}
\]

such that

\[
                              \Phi(A)=T_{y(A)}(A)
\tag{2.4}
\]

is a permutation of \(\mathcal Z_m\), has exactly two fixed points, has
every nonfixed cycle of length \(p\), and obeys

\[
                              \sum_{A\in C}y(A)=0
\tag{2.5}
\]

on every nonfixed cycle \(C\).  Its fixed points are the AP vertices

\[
 A_y=y\{4j+3:0\le j<m\},\qquad A_{-y}=A_y,
\tag{2.6}
\]

indexed by \(y\in\mathbb F_p^*/\{\pm1\}\).

#### Proof

Orient every component of the quotient factor and let \(y(A)\) be the
label of its outgoing edge.  The selected successor is a permutation.
Theorem 2.1 gives the cycle lengths and the two fixed AP vertices, while
the voltage of a nonfixed cycle is \(2\sum_Cy(A)\), proving (2.5).
Conversely the cycles of such a permutation give the components required
in Theorem 2.1.  Formula (2.6) satisfies the alternating loop partition
(1.8), and that partition uniquely determines the loop vertex. \(\square\)

## 3. Exact necklace difference-family form

Let \(z=(z_0,\ldots,z_{p-1})\) be the omitted-coordinate permutation of
a lifted wreath.  Put

\[
 J_{i,r}(z)=
 \{z_{i+1},z_{i+3},\ldots,z_{i+2r-1}\},
 \qquad i\in\mathbb F_p.
\tag{3.1}
\]

For \(r=m-q\), these are exactly the lower depth-\(q\) intervals.  For a
free row packet define its quotient multiplicity vector

\[
 a_{z,q}(O)=
 \#\{i\in\mathbb F_p:[J_{i,m-q}(z)]_\rho=O\},
 \qquad O\in\mathcal N_{m-q}.
\tag{3.2}
\]

It has total mass \(p\).  At \(q=0\), a selectable free row orbit has

\[
                         a_{z,0}(O)\in\{0,1\}.
\tag{3.3}
\]

For an AP row of slope \(d\), denote by \(O_{d,q}\) the necklace of its
length-\((m-q)\) AP intervals.

### Lemma 3.1 (the exact AP normalization)

One selected AP loop contributes the vector \(\mathbf1_{O_{d,q}}\) to
the common physical load on quotient target necklaces.

#### Proof

The \(p\) intervals are

\[
 id+\{0,d,\ldots,(m-q-1)d\},\qquad i\in\mathbb F_p.
\tag{3.4}
\]

They are precisely the \(p\) different physical phases of one target
necklace.  Each phase has load one.  Quotient load records this common
phase load, not the raw number \(p\) of positions. \(\square\)

### Theorem 3.2 (difference-family equivalence and lower loads)

Choose two distinct AP slopes \(d_1,d_2\) modulo sign and a set
\(\mathcal P\) of free row-translation orbits.  They form an invariant
exact middle factor if and only if

\[
 \boxed{
   \sum_{z\in\mathcal P}a_{z,0}(O)
   +\mathbf1_{O_{d_1,0}}(O)+\mathbf1_{O_{d_2,0}}(O)=1
   \quad(O\in\mathcal N_m).}
\tag{3.5}
\]

For that factor, the exact common load on a depth-\(q\) lower target
necklace is

\[
 \boxed{
 k_q(O)=
   \sum_{z\in\mathcal P}a_{z,q}(O)
   +\mathbf1_{O_{d_1,q}}(O)+\mathbf1_{O_{d_2,q}}(O).}
\tag{3.6}
\]

Consequently

\[
 \boxed{
 M_q^-=p\,\overline M_q,
 \qquad
 \overline M_q=\#\{O\in\mathcal N_{m-q}:k_q(O)=0\}.}
\tag{3.7}
\]

Since \(\sum_Ok_q(O)=T\), the quotient holes also obey the exact
one-sided repeat ledger

\[
 \boxed{
 \overline M_q
 =\sum_O(k_q(O)-1)_+
  -\bigl(T-|\mathcal N_{m-q}|\bigr).}
\tag{3.8}
\]

Thus repeats are harmless up to the unavoidable surplus
\(T-|\mathcal N_{m-q}|\); only repeat excess beyond it creates holes.

#### Proof

For a free packet, each occurrence of a necklace at a base-row position
is translated through all \(p\) physical phases by the \(p\) lifted rows.
Thus its multiplicity in (3.2) is the load of every physical phase.  At
the middle rank, exact ownership is precisely the pointwise partition
(3.5).  Lemma 3.1 gives the fixed-loop terms.  The same phase argument at
rank \(m-q\) gives (3.6).  Invariance makes the load constant on every
target necklace, proving (3.7).  Finally
\(k=\mathbf1_{\{k>0\}}+(k-1)_+\) pointwise; summing this identity and
using \(\sum_Ok_q(O)=T\) proves (3.8). \(\square\)

Thus the exact growing-window one-sided theorem for this architecture is

\[
 \boxed{
     \sum_{q=1}^{H_m}\overline M_q=o(T),
     \qquad H_m/\sqrt m\longrightarrow\infty,}
\tag{3.9}
\]

for one family satisfying (3.5).  The same selected rows must serve every
\(q\); separate difference families at separate ranks do not compose.

The two AP loops affect at most two quotient target necklaces per depth.
Their total direct contribution across the window in (3.9) is at most \(2H_m\), not
\(2pH_m\).  For every mesoscopic \(H_m=o(T)\) this is negligible.  Their
importance is exact middle congruence, not asymptotic shadow capacity.

The same color can be read directly from the selector data.  For a lifted
free cycle put \(B_i=A_i+s_i\), with \(s_i,z_i\) as in (0.7).  The
odd-graph recurrence gives

\[
                         B_{j+2}=B_j\setminus\{z_{j+1}\}
                                      \cup\{z_j\}.
\tag{3.10}
\]

Consequently its depth-\(q\) lower color at index \(i\) is

\[
 \boxed{
 \chi_q(C,i)=
 \left[
 B_{i-2q}\setminus
 \{z_{i-2q+1},z_{i-2q+3},\ldots,z_{i-1}\}
 \right]_\rho.}
\tag{3.11}
\]

Indeed (3.10) successively deletes the displayed odd omitted labels and
inserts new labels absent from the initial state; precisely the deleted
labels fail to survive the intersection of
\(B_{i-2q},B_{i-2q+2},\ldots,B_i\).  Formula (3.11) is the selector-form
version of the every-second window vector in (3.2).

## 4. Marginal and laminar necklace flows are exactly integral

The difficulty in (3.9) is not a rankwise Hall cut.  This can be shown
without using wreath factors.

Fix \(q\).  Form the bipartite quotient **multigraph** \(\mathcal I_q\)
whose left vertices are \(\mathcal N_m\), whose right vertices are
\(\mathcal N_{m-q}\), and whose edges are translation orbits of literal
flags

\[
                              B\subset A,qquad
                              |B|=m-q,\qquad |A|=m.
\tag{4.1}
\]

Parallel flag orbits are retained.  Freeness of translation on proper
sets makes the degrees

\[
 d_L=\binom mq,qquad
 d_R=\binom{m+q+1}q,qquad
 {d_R\over d_L}={W\over N_q}=:\lambda_q.
\tag{4.2}
\]

### Theorem 4.1 (exact floor-balanced necklace flow)

There is an integral selection of one incident flag at every left vertex
of \(\mathcal I_q\) such that every right vertex is selected exactly
\(c_q\) or \(c_q+1\) times, where \(c_q=\lfloor\lambda_q\rfloor\).
Exactly

\[
                              T-c_q|\mathcal N_{m-q}|
\tag{4.3}
\]

right vertices have load \(c_q+1\).

#### Proof

Give every quotient flag the fractional value \(1/d_L\).  Each left
vertex then sends one unit, and each right vertex receives
\(d_R/d_L=\lambda_q\), which lies in \([c_q,c_q+1]\).

Make the standard flow network with a unit-capacity source arc into every
left vertex, the flag multiedges of capacity one, and a right-to-sink arc
with lower capacity \(c_q\) and upper capacity \(c_q+1\).  The uniform
fractional flow is feasible.  The node--arc incidence matrix is totally
unimodular, so the integral circulation theorem gives an integral flow of
the same value.  Every left vertex emits one selected flag, and every
right load is \(c_q\) or \(c_q+1\).  Summing the right loads gives (4.3).
\(\square\)

At \(q=1\),

\[
                 \lambda_1={m+2\over m}=1+{2\over m},
\tag{4.4}
\]

so Theorem 4.1 covers every lower necklace once or twice, with no hole.
For \(q=\lfloor A\sqrt m\rfloor\), it remains exact with
\(\lambda_q\to e^{A^2}\).

### Lemma 4.2 (local literal realizability)

Every selected flag \(B\subset A\) in (4.1) can occur as the indicated
depth-\(q\) lower trace of a literal wreath segment starting at \(A\).

#### Proof

Use the notation (3.1) with \(i=0\).  Put the elements of \(B\) in the
odd positions

\[
 z_1,z_3,\ldots,z_{2(m-q)-1},
\]

put the elements of \(A\setminus B\) in the remaining \(q\) odd
positions, and put the elements of \(\mathbb F_p\setminus A\) in the
\(m+1\) even positions.  Then \(J_{0,m}(z)=A\) and
\(J_{0,m-q}(z)=B\).  By the every-second intersection identity, these
are respectively the first middle window and its depth-\(q\) lower trace.
This gives a literal row segment; the orders inside the three displayed
classes are arbitrary. \(\square\)

Theorem 4.1 and Lemma 4.2 are deliberately rankwise.  The next theorem
removes the nesting defect, but neither construction gives reciprocal
odd-graph edges or closure after \(p\) steps.  Those remaining conditions
are factor chronology, rather than a hidden necklace-capacity deficit.

In fact the nesting defect can also be removed at the level of deletion
flags.

### Theorem 4.3 (simultaneous floor-balanced quotient deletion paths)

For every \(H<m\), there are \(T\) integral directed paths in the
layered quotient inclusion multigraph

\[
 \mathcal N_m\longrightarrow\mathcal N_{m-1}\longrightarrow\cdots
 \longrightarrow\mathcal N_{m-H},
\tag{4.5}
\]

one beginning at each middle necklace, such that the number
\(\ell_q(O)\) of paths through every \(O\in\mathcal N_{m-q}\) obeys

\[
                 \boxed{\ell_q(O)\in
                   \{\lfloor\lambda_q\rfloor,
                     \lceil\lambda_q\rceil\}}
                 \qquad(0\le q\le H).
\tag{4.6}
\]

Every quotient path lifts to a full translation packet of literal nested
deletion flags.

#### Proof

At layer \(q\), a rank-\((m-q)\) necklace has \(m-q\) outgoing deletion
flag orbits.  A rank-\((m-q-1)\) necklace has \(m+q+2\) incoming flag
orbits.  Give every node at layer \(q\) fractional throughput
\(\lambda_q=T/|\mathcal N_{m-q}|\), split equally over its outgoing
edges.  The incoming throughput at the next layer is

\[
 {m+q+2\over m-q}\lambda_q=\lambda_{q+1},
\tag{4.7}
\]

by the adjacent binomial ratio.  At layer zero \(\lambda_0=1\), so this
is a fractional flow of total value \(T\).

Split every node into an in-node and an out-node.  Give its internal arc
integer lower and upper capacities

\[
                    \lfloor\lambda_q\rfloor,
                    \qquad\lceil\lambda_q\rceil,
\tag{4.8}
\]

and retain the quotient deletion multiedges between consecutive layers.
The displayed fractional flow is feasible.  The directed node--arc
incidence matrix is totally unimodular, so the integral circulation
theorem supplies an integral flow with the same value and bounds.  The
network is layered and acyclic; decompose this integral flow into \(T\)
unit source--sink paths.  The unit source arcs at layer zero make their
starts the \(T\) distinct middle necklaces, and the node bounds give
(4.6).

Finally choose one actual representative of a starting necklace and lift
the quotient flag edges successively.  This gives one nested literal
deletion flag.  Translating it by every element of \(\mathbb F_p\) gives
the full packet; freeness ensures that these are its \(p\) distinct
physical phases.

Explicitly, write the lifted path as
\(B_q=A\setminus\{d_1,\ldots,d_q\}\).  Choose the odd-position order
\(u_1,\ldots,u_m\) of \(A\) so that

\[
                              u_{m-q+1}=d_q
                              \qquad(1\le q\le H),
\tag{4.9}
\]

order the initial elements of \(B_H\) arbitrarily, and put the complement
of \(A\) arbitrarily in the even positions.  Then simultaneously

\[
                         J_{0,m-q}=\{u_1,\ldots,u_{m-q}\}=B_q
                         \qquad(0\le q\le H).
\tag{4.10}
\]

Thus one literal pointed row segment realizes the whole path. \(\square\)

Theorem 4.3 proves exact simultaneous feasibility of every laminar
inclusion/Hall constraint, even through the entire lower half.  It still
does not pair different owner flags into a common cyclic order.  In a
wreath factor the paths starting at the \(p\) middle necklaces of one
selected quotient cycle must be the correlated every-second traces
(3.11), and the same correlations must satisfy reciprocity and zero
voltage.  Total unimodularity of (4.5) does not impose those equations.

## 5. The midpoint permutation invariant

Consider a simple zero-voltage quotient \(p\)-cycle

\[
 A_0\xrightarrow{y_0}A_1\xrightarrow{y_1}\cdots
 \xrightarrow{y_{p-1}}A_0.
\tag{5.1}
\]

Set \(s_i,z_i\) as in (0.7).  Then \(A_i+s_i\) is a closed lifted
odd-graph \(p\)-cycle.  The coordinate omitted by its \(i\)-th edge is
\(z_i=s_i+y_i\).

### Theorem 5.1 (midpoint permutation and moment equations)

The sequence \((z_i)_{i\in\mathbb F_p}\) is a permutation of
\(\mathbb F_p\).  Equivalently,

\[
                       z_i={s_i+s_{i+1}\over2}
\tag{5.2}
\]

are the edge midpoints of the closed phase walk, and

\[
 \sum_i z_i^r=
 \begin{cases}
 0,&1\le r\le p-2,\\
 -1,&r=p-1.
 \end{cases}
\tag{5.3}
\]

In particular

\[
                         \sum_i y_i=0,qquad
                         \sum_i i,y_i=0.
\tag{5.4}
\]

#### Proof

The voltage-zero equation gives \(s_p=s_0\), so the lift closes in
\(p\) edges.  A closed walk of length \(p=2m+1\) in \(KG(p,m)\) has
every omitted coordinate exactly once: if coordinate \(z\) is omitted
\(t_z\) times, its membership toggles on the other \(p-t_z\) edges, so
\(t_z\) is odd; the sum of all \(t_z\) is \(p\), forcing \(t_z=1\).
Thus the \(z_i\) form a permutation.  Formula (5.2) follows from
\(s_{i+1}-s_i=2y_i\), and (5.3) is the standard finite-field power-sum
identity.

Also \(\sum_i y_i=0\) is voltage zero.  Since

\[
 \sum_{i=0}^{p-1}s_i
 =2\sum_{j=0}^{p-1}(p-1-j)y_j
 =-2\sum_j j y_j
\tag{5.5}
\]

after using \(\sum_jy_j=0\), while
\(\sum_i z_i=\sum_i s_i+\sum_i y_i=0\), the second identity in (5.4)
follows. \(\square\)

These equations are necessary for a proposed labelled quotient cycle.
They are not sufficient: the set transitions (0.6), simplicity, and
vertex-disjointness between different cycles remain literal conditions.

### Corollary 5.2 (affine voltage schedules give no free packet)

No simple zero-voltage quotient \(p\)-cycle has an affine edge-label
schedule \(y_i=\alpha i+\beta\).

#### Proof

Summing (0.7) gives

\[
 s_i=\alpha i(i-1)+2\beta i,
 \qquad
 z_i=\alpha i^2+2\beta i+\beta.
\tag{5.6}
\]

If \(\alpha\ne0\), the quadratic has the involutive symmetry

\[
 z_i=z_{-i-2\beta/\alpha},
\tag{5.7}
\]

and is not injective on the odd field.  This contradicts Theorem 5.1.
If \(\alpha=0\), the sequence \((z_i)\) is a permutation only when
\(\beta\ne0\), in which case it is the AP order
\(z_i=2\beta i+\beta\).  Its middle windows all lie in one translation
necklace, so its quotient image is an AP loop, not a simple \(p\)-cycle.
The case \(\beta=0\) is not a permutation. \(\square\)

Thus a free difference-family packet must already use a nonlinear
state-dependent voltage schedule.

There are also exact global moment tests for any proposed selector.  Put

\[
 Q(A)=\sum_{x\in A}x^2,qquad R_3(A)=\sum_{x\in A}x^3.
\tag{5.8}
\]

### Proposition 5.3 (quadratic and cubic selector identities)

For every normalized quotient edge \(A\xrightarrow{y}T_y(A)\),

\[
 \boxed{
 Q(T_y(A))+Q(A)=y^2,}
\tag{5.9}
\]

and

\[
 \boxed{
 R_3(T_y(A))+R_3(A)=6yQ(A)-3y^3.}
\tag{5.10}
\]

Consequently every spanning selector in Corollary 2.2 satisfies

\[
 \boxed{
     \sum_{A\in\mathcal Z_m}y(A)^2=0,
     \qquad
     \sum_Ay(A)^3=2\sum_Ay(A)Q(A).}
\tag{5.11}
\]

#### Proof

Let \(D=\mathbb F_p\setminus(A\cup\{y\})\).  Since
\(\sum_Ax=0\),

\[
 \sum_{d\in D}d=-y,qquad
 \sum_{d\in D}d^2=-Q(A)-y^2,qquad
 \sum_{d\in D}d^3=-R_3(A)-y^3.
\tag{5.12}
\]

Expand the second and third powers of \(d-2y\), sum over the \(m\)
elements of \(D\), and use \(2m=-1\) in \(\mathbb F_p\).  The quadratic
coefficient becomes \(3+4m=1\), giving (5.9); the cubic coefficient
becomes \(-7-8m=-3\), giving (5.10).

Scaling \(A\mapsto cA\) permutes \(\mathcal Z_m\).  Choosing \(c\) with
\(c^2\ne1\), and then with \(c^3\ne1\), shows

\[
                         \sum_AQ(A)=\sum_AR_3(A)=0.
\tag{5.13}
\]

Sum (5.9)--(5.10) over \(A\) and use that \(A\mapsto T_{y(A)}(A)\) is a
permutation.  Equations (5.11) follow. \(\square\)

These identities reject false voltage tables, but their right signs and
zero totals do not contradict an unrestricted translation-only factor.

## 6. The affine-normalizer orbit obstruction

The normalizer of the translation cycle in the full coordinate symmetric
group is

\[
 N_{S_p}(\langle\rho\rangle)=\operatorname {AGL}(1,p).
\tag{6.1}
\]

On translation necklaces, the translation subgroup acts trivially, so the
induced normalizer group is a quotient of \(\mathbb F_p^*\), of order
dividing \(p-1\).

### Theorem 6.1 (no normalizer-orbit free cycles)

No orbit of one affine-normalizer element, and no orbit of the full
induced affine-normalizer group, has size \(p\) on the necklace quotient.
Consequently the free \(p\)-cycles in Theorem 2.1 cannot be obtained as
root-scale AGL orbits.

#### Proof

Every orbit size divides the order of the acting group, which divides
\(p-1\).  It therefore cannot equal the prime \(p\). \(\square\)

This theorem does not forbid using affine images of exponentially many
independently chosen nonlinear base cycles.  It forbids the much stronger
and tempting construction in which one affine group element or one
normalizer orbit supplies the cycle chronology itself.  In particular,
the two AP loops are the only part of the exact factor furnished by a
one-dimensional affine schedule.

The same calculation gives a sharper obstruction to adding multiplicative
symmetry to a translation-invariant construction.  For
\(c\in\mathbb F_p^*\), put \(S_c(A)=cA\).  Directly from (0.6),

\[
                              S_cT_y=T_{cy}S_c.
\tag{6.2}
\]

### Theorem 6.2 (multiplicative stabilizers have order at most four)

If an exact factor from Theorem 2.1 is also invariant under a subgroup
\(H\le\mathbb F_p^*\), then

\[
                     \left|H/(H\cap\{\pm1\})\right|\le2.
\tag{6.3}
\]

Consequently \(H\) is contained in the unique subgroup of order four of
\(\mathbb F_p^*\).  In particular no fully multiplicatively equivariant,
and hence no fully AGL-equivariant, construction exists for \(p\ge13\).

#### Proof

The two selected AP loop slopes form an \(H\)-invariant two-set in
\(\mathbb F_p^*/\{\pm1\}\).  The effective action of
\(H/(H\cap\{\pm1\})\) on slope classes is free: if \(ca=\pm a\), then
\(c=\pm1\).  Its orbit size must therefore divide two, proving (6.3).
Since \(\mathbb F_p^*\) is cyclic, the asserted subgroup conclusion
follows. \(\square\)

Even reflection symmetry has an exact fixed-point cut.  Let

\[
                              R=\binom m{m/2},
                              \qquad K={T-2\over p}.
\tag{6.4}
\]

### Theorem 6.3 (reflection-fixed necklace cut)

If an invariant exact factor is also invariant under
\(A\mapsto-A\), then exactly \(R-2\) of its \(K\) free quotient cycles
are reflection-stable, every such cycle contains exactly one fixed
quotient vertex, and

\[
                              \boxed{R\le K+2.}
\tag{6.5}
\]

The remaining \(K-(R-2)\) free cycles occur in reflection pairs and hence
this difference is even.  For \(p=13,m=6\), one has

\[
                              R=20,qquad K=10,
\tag{6.6}
\]

so no reflection-invariant exact factor exists.

#### Proof

A zero-sum middle set fixed by negation cannot contain \(0\), because its
remaining cardinality would be odd.  It is therefore a union of \(m/2\)
of the \(m\) pairs \(\{x,-x\}\), giving exactly \(R\) fixed quotient
vertices.  Every AP vertex is among them, and the two selected loops cover
two.

If a remaining fixed vertex lies on a selected free cycle, uniqueness of
the selected component forces that cycle to be setwise reflection-stable.
For a stable free cycle, negation sends a lifted wreath to one of its
coordinate translates.  After undoing that translate, a nonidentity
affine reflection preserves the supporting physical \(C_p\).  Its induced
automorphism is a reflection of the odd cycle and fixes exactly one cycle
vertex.  The action is not the identity: the \(p\) middle windows
reconstruct all omitted coordinates, so an affine coordinate map fixing
every cycle vertex is the identity.  Middle transversality then says that
the stable quotient cycle contains exactly one negation-fixed quotient
vertex.

Thus the fixed vertices outside the loops and the stable free cycles are
in bijection.  There are \(R-2\) such cycles, proving (6.5).  Every other
cycle is paired with its reflected image.  Substitution of
\(T=\operatorname {Cat}_6=132\) gives (6.6). \(\square\)

There is also a complete order-four obstruction on half of the remaining
prime subsequence.

### Theorem 6.4 (no \(C_4\)-symmetric factor for \(p\equiv1\pmod8\))

Let \(i^2=-1\) in \(\mathbb F_p\).  If \(p\equiv1\pmod8\), no exact
factor can be invariant under multiplication by \(i\).

#### Proof

Now \(m\equiv0\pmod4\).  Choose any \(m/4\) of the multiplicative
four-orbits

\[
                              \{x,ix,-x,-ix\}
\]

in \(\mathbb F_p^*\).  Their union is an \(m\)-set of sum zero and is a
quotient vertex fixed by multiplication by \(i\).  It is not an AP loop
fixed by \(i\), since the induced action on AP slope classes is free.
Therefore its unique selected free cycle would have to be setwise
\(i\)-stable.

Such stability would make an affine coordinate map with multiplier \(i\)
preserve a lifted wreath.  This affine map has order four, while a simple
odd cycle has automorphism group \(D_{2p}\), which has no element of order
four.  Faithfulness again follows from reconstruction by the middle
windows.  This contradiction proves the theorem. \(\square\)

When \(p\equiv5\pmod8\), an \(i\)-invariant set has cardinality
\(0\) or \(1\pmod4\), while \(m\equiv2\pmod4\), so the fixed-vertex
argument in Theorem 6.4 is absent.  The reflection cut (6.5) remains; it
already rules out the first case \(p=13\).  These theorems do not obstruct
a fully asymmetric translation-only factor.

## 7. The exact grouped one-sided gate

Let \(\mathscr C_0\) be the catalogue of simple zero-voltage quotient
\(p\)-cycles, and let \(\mathscr L\) be the AP loops.  For
\(C\in\mathscr C_0\), write \(v(C)\in\{0,1\}^{\mathcal N_m}\) for its
middle vertex incidence and \(a_{C,q}(O)\) for its lower multiplicity.
For an AP loop \(L\), use its singleton middle and lower incidence.

An exact invariant one-sided solution through depth \(H\) is precisely a
binary vector \((x_C,x_L)\) satisfying

\[
\begin{aligned}
 \sum_Cx_Cv(C)+\sum_Lx_Lv(L)&=\mathbf1_{\mathcal N_m},\\
 \sum_Lx_L&=2,\\
 z_{q,O}+\sum_Cx_Ca_{C,q}(O)
             +\sum_Lx_La_{L,q}(O)&\ge1,\\
 x_C,x_L,z_{q,O}&\in\{0,1\},
\end{aligned}
\tag{7.1}
\]

with objective

\[
                           \sum_{q\le H}\sum_O z_{q,O}.
\tag{7.2}
\]

The desired theorem is that the minimum is \(o(T)\) for some
\(H/\sqrt m\to\infty\).  The same cycle variable occurs in every row of
(7.1).  Even the nested path variables from Theorem 4.3 cannot be
substituted for it.

The local catalogue is in fact exponentially complete throughout every
mesoscopic window \(H=o(m)\).  The exact enumerator is useful because it rules
out packet scarcity as an explanation for the remaining gate.

### Theorem 7.1 (exact translate-collision enumerator)

Let \(I,J\subset\mathbb F_p\) be distinct cyclic position intervals of
the same size \(k\le m\), put \(r=|I\cap J|\), and let \(a\ne0\).  For a
uniform random bijection \(\pi:\mathbb F_p\to\mathbb F_p\),

\[
 \boxed{
 \Pr\bigl(\pi(J)=\pi(I)+a\bigr)
 ={k-r\over k\binom{p-1}k}.}
\tag{7.3}
\]

Consequently the expected number of ordered translation collisions among
the \(p\) rank-\(k\) intervals is exactly

\[
                              {p^2(p-1)\over\binom pk}.
\tag{7.4}
\]

If \(H=o(m)\), the probability that a random row fails
translation-rainbowness at some rank \(m-q\), \(0\le q\le H\), is at
most

\[
             { (H+1)p^2(p-1)\over\binom p{m-H}}
             =e^{-\Omega(m)}.
\tag{7.5}
\]

#### Proof

Put \(b=k-r\).  For a fixed image \(X=\pi(I)\), the equality in (7.3)
requires \(|X\setminus(X+a)|=b\).  Along the single \(a\)-cycle on
\(\mathbb F_p\), this is the number of one-runs of \(X\).  The exact
cyclic-run count is

\[
 {p\over b}\binom{k-1}{b-1}\binom{p-k-1}{b-1}.
\tag{7.6}
\]

For each such \(X\), the four positional regions determined by \(I,J\)
can be bijected to their four forced label regions in

\[
                         r!\,b!^2\,(p-2k+r)!
\tag{7.7}
\]

ways.  Divide the product of (7.6) and (7.7) by \(p!\); elementary
factorial cancellation gives (7.3).

For a cyclic separation \(d\), let \(b(d)=k-|I\cap(I+d)|\).  Since
\(k\le(p-1)/2\),

\[
                              \sum_{d=1}^{p-1}b(d)=k(p-k).
\tag{7.8}
\]

Sum (7.3) over \(p\) starts, the \(p-1\) nonzero translations, and all
separations.  Using
\(\binom{p-1}k=(p-k)\binom pk/p\) gives (7.4).  Markov and a union bound
over \(q\) give (7.5): indeed

\[
 \log\binom p{m-H}=(2\log 2+o(1))m
\]

whenever \(H=o(m)\), whereas the remaining factor in (7.5) is
polynomial in \(m\). \(\square\)

A row counted as good in (7.5) is free, gives a simple zero-voltage
quotient \(p\)-cycle at the middle rank, and has \(p\) distinct attached
necklace colors at every protected lower rank.

There is even a fractional simultaneous cover supported entirely on these
literal good cycles.

### Theorem 7.2 (admissible-catalogue fractional nearcover)

Fix \(H=o(m)\).  There are exceptional sets

\[
                         E_q\subseteq\mathcal N_{m-q}
\]

with

\[
                         \sum_{q=0}^H|E_q|
                         =e^{-\Omega(m)}T,
\tag{7.9}
\]

and one constant nonnegative weight on every row orbit good in Theorem
7.1 such that

* every middle necklace has total packet weight at most one;
* every middle necklace outside \(E_0\) has weight at least
  \(1-e^{-\Omega(m)}\); and
* every lower necklace outside \(E_q\), \(1\le q\le H\), has total
  attached-color weight at least one.

#### Proof

Use geometric cyclic orders modulo rotation and reversal.  Their number is

\[
                              R={(p-1)!\over2}.
\tag{7.10}
\]

Before the bad rows are deleted, the exact quotient occurrence degree at
rank \(m-q\) is

\[
 D_q={R\over|\mathcal N_{m-q}|}
     ={(m-q)!(m+q+1)!\over2},
 \qquad {D_q\over D_0}=\lambda_q.
\tag{7.11}
\]

Let \(\varepsilon=e^{-\Omega(m)}\) be the bad-row fraction from
(7.5), enlarged to include the polynomial AP catalogue, and put
\(\delta=\sqrt\varepsilon\).  At each rank, the sum of all degree deficits
created by deleting bad rows is at most \(\varepsilon D_q\) times the
number of quotient targets.  Markov's inequality therefore leaves an
exceptional set of size at most \(\delta|\mathcal N_{m-q}|\) outside
which the good degree is at least \((1-\delta)D_q\).  This proves (7.9).

Give every good free row orbit weight

\[
                              w={1\over D_0}.
\tag{7.12}
\]

Middle degrees never exceed \(D_0\), and outside \(E_0\) their weighted
load is at least \(1-\delta\).  At depth \(q\ge1\), the load outside
\(E_q\) is at least

\[
                           (1-\delta){D_q\over D_0}
                           =(1-\delta)\lambda_q.
\tag{7.13}
\]

The minimum is at \(q=1\), where
\(\lambda_1=1+2/m\).  Since \(\delta\) is exponentially small, (7.13)
exceeds one for all large \(m\), uniformly through the window. \(\square\)

Thus there is no \(\Omega(T)\) real-linear/Fourier or fractional
configuration-Hall obstruction: the fractional exception is exponentially
small.  Integrality and exact middle ownership are the issue.

There is, however, a sharp obstruction to resolving that integrality by
an atomic growing-rank nibble.

### Theorem 7.3 (intrinsic cycle-codegree obstruction)

Let \(\mathcal H_0\) be the \(p\)-uniform hypergraph on middle necklaces
whose edges are admissible simple zero-voltage quotient \(p\)-cycles.
Let \(v\) have maximum degree \(D_M\).  Then

\[
                         \boxed{
 \Delta_2(\mathcal H_0)\ge{2D_M\over m+1}.}
\tag{7.14}
\]

In particular

\[
             {\Delta_2(\mathcal H_0)\over D_M/p}
             \ge {2p\over m+1}=4-o(1),
\tag{7.15}
\]

so the commonly proposed growing-rank hypothesis
\(\Delta_2=o(D_M/p)\) fails already at the middle layer.

#### Proof

The quotient odd graph gives \(v\) at most \(m+1\) distinct neighbors.
Every selected simple cycle through \(v\) uses two distinct such
neighbors.  Hence

\[
                      \sum_{u\sim v}\operatorname {codeg}(u,v)=2D_M.
\tag{7.16}
\]

One neighbor has codegree at least the average
\(2D_M/(m+1)\), proving (7.14)--(7.15). \(\square\)

If every depth/sign slot is appended to a packet edge, its rank is
\(r=p(H+1)\).  The same middle-neighbor pair gives, relative to the
middle maximum degree,

\[
                         {\Delta_2\over D_M/r}
                         \ge {2r\over m+1}
                         =(4+o(1))(H+1).
\tag{7.17}
\]

To replace \(D_M\) by a global maximum degree in (7.17), one must assume
the intended approximately regular slot expansion; without that
normalization only the displayed \(D_M\)-relative statement is automatic.

Theorem 7.3 closes the generic atomic-cycle nibble criterion, not the
existence of a structured cycle factor.  An ordinary matching which
requires disjointness at every depth also loses the middle fraction
\(1-e^{-A^2}+o(1)\) at \(q=A\sqrt m\); one-sided coverage needs repeated
lower use up to the available mean, not cross-rank disjointness.

Thus the exact remaining positive statement is a nonlinear, capacitated
difference-family resolution of (7.1), or a literal trade system which
rounds Theorem 4.3 into common rows while maintaining Theorem 2.1.

## 8. Canonical MSW equivariance audit

Identify the distinguished MSW coordinate \(\infty\) with \(0\in\mathbb
F_p\), and identify the remaining coordinates with
\(1,2,\ldots,2m\).  Let

\[
                              \rho(t)=t+1\pmod p.
\tag{8.1}
\]

For a Dyck word \(x\) of semilength \(m\), write its MSW flip-position
permutation as

\[
                              \pi(x)=(\pi_1,\ldots,\pi_{2m}).
\tag{8.2}
\]

The omitted-edge word of the corresponding canonical wreath is the
geometric cyclic word

\[
                              \widehat\pi(x)=(\pi(x),0).
\tag{8.3}
\]

Let \(j=j(x)\) be the position of the label \(2m=-1\) in \(\pi(x)\).
After applying \(\rho\), this entry becomes \(0\).  Recut the translated
cyclic word immediately after it so that the new \(0\) is again last.
The resulting permutation of \(\{1,\ldots,2m\}\) is

\[
 \boxed{
 \mathsf S\pi=
 (\pi_{j+1}+1,\ldots,\pi_{2m}+1,
  1,\pi_1+1,\ldots,\pi_{j-1}+1),}
\tag{8.4}
\]

where the entries are reduced modulo \(p\), and empty strings are
omitted.  Formula (8.4) is the exact candidate shift action on the
Chung--Feller row index: invariance would require, for every \(x\), a
Dyck word \(x'\) with

\[
        \mathsf S\pi(x)=\pi(x')
        \quad\hbox{or}\quad
        \mathsf S\pi(x)=\operatorname {rev}\pi(x').
\tag{8.5}
\]

These are the only two possibilities.  Indeed, on a minimum odd cycle
every edge has a distinct omitted coordinate, so its omitted-label word is
intrinsic up to cyclic rotation and reversal.  Putting the unique label
\(0\) last removes rotation; ordinary word reversal is the remaining
choice.  Thus the second alternative in (8.5) accounts exactly for the
fact that a geometric wreath is unoriented.

For a balanced word \(u\), write

\[
                 \mu(u)=\overline{\operatorname {rev}_{\rm word}(u)},
\]

where the bar interchanges its up- and down-steps.  The exact MSW
recursion is

\[
 \pi(1u0v)=
 \bigl(|u|+2,\ |u|+2-\pi(\mu(u)),\
       1,\ |u|+2+\pi(v)\bigr).
\tag{8.6}
\]

Here \(|u|\) is even.

### Lemma 8.1 (MSW first-label parity)

Every canonical MSW flip permutation begins with an even label.

#### Proof

The first entry in (8.6) is \(|u|+2\), which is even. \(\square\)

Let \(x_m=1^m0^m\) be the mountain Dyck word and put
\(\pi^{(m)}=\pi(x_m)\).

### Lemma 8.2 (the mountain prefix)

For every \(m\ge2\),

\[
                             \pi^{(m)}_1=2m,
                             \qquad \pi^{(m)}_2=2.
\tag{8.7}
\]

#### Proof

In (8.6), the first-return decomposition of \(x_m\) has

\[
 u=1^{m-1}0^{m-1},\qquad v=\varnothing,
 \qquad \mu(u)=u.
\]

Therefore

\[
 \pi^{(m)}=
 \bigl(2m,\ 2m-\pi^{(m-1)},\ 1\bigr).
\tag{8.8}
\]

The first identity follows immediately.  The first entry of
\(\pi^{(m-1)}\) is \(2m-2\), so the second entry in (8.8) is \(2\).
\(\square\)

### Theorem 8.3 (canonical MSW is not translation-invariant)

For every \(m\ge2\), the canonical MSW wreath factor on
\(2m+1\) coordinates is not invariant under the natural translation
\(\rho\) in (8.1).  In particular it is not invariant when
\(m\) is even and \(p=2m+1\equiv1\pmod4\) is prime.

#### Proof

For the mountain row, (8.7) says that the label \(2m\) is first, so
\(j=1\) in (8.4).  Hence

\[
                  \mathsf S\pi^{(m)}
                  =(3,\pi^{(m)}_3+1,\ldots,
                        \pi^{(m)}_{2m}+1,1).
\tag{8.9}
\]

Its first entry is \(3\), so Lemma 8.1 rules out
\(\mathsf S\pi^{(m)}=\pi(x')\).  Its last entry is \(1\), so the first
entry of \(\operatorname {rev}(\mathsf S\pi^{(m)})\) is odd; Lemma 8.1
also rules out
\(\mathsf S\pi^{(m)}=\operatorname {rev}\pi(x')\).  Thus the translated
mountain row is absent from the canonical factor in both orientations.
One missing translated row refutes setwise invariance. \(\square\)

The failure occurs before lower-shadow considerations.  Therefore, under
the fixed natural action \(\rho:t\mapsto t+1\), the canonical MSW factor
cannot be projected to the two-loop/free-orbit normal form of Theorem 2.1,
and its known shadow statistics cannot be imported as the necklace loads
of a \(\rho\)-invariant factor.  This does not rule out first conjugating
the MSW factor by an arbitrary ground-set permutation and then testing a
different regular cyclic subgroup.  For the natural prime cyclic action
used throughout this report, a new retiled factor or a noncanonical
equivariant Chung--Feller construction is required.

## 9. Audited boundary

Proved here:

1. the exact two-AP-loop/zero-voltage-cycle characterization;
2. the exact lower-shadow necklace multiplicities, including the unit AP
   normalization;
3. the exact simultaneous integral floor-balanced nested deletion paths
   through every quotient rank;
4. local literal realizability of every assigned nested flag;
5. the midpoint-permutation and power-sum invariants of every free packet;
6. the affine-voltage and affine-normalizer orbit no-go theorems;
7. the multiplicative, reflection, and order-four symmetry cuts;
8. the exact Gaussian-window collision enumerator and fractional good-cycle
   nearcover;
9. the intrinsic atomic-cycle codegree obstruction; and
10. the exact refutation of canonical MSW translation invariance.

Imported standard results are explicitly limited to finite-field power
sums, total unimodularity/integral circulation, and the already proved
dense-subsequence transfer theorem.  None supplies the grouped cycle
selection in (7.1).

Not proved:

1. existence of an invariant exact factor for any unbounded sequence of
   primes \(p\equiv1\pmod4\) (beyond the elementary \(p=5\) case);
2. a nonlinear zero-voltage difference family satisfying (3.5);
3. simultaneous lower necklace near-coverage (3.9); or
4. a positive-density Hall/Fourier obstruction against the unrestricted
   nonlinear catalogue.

The algebraic invariant lane therefore closes two broad explicit ansatzes
but does not close the architecture.  Marginal necklace capacity is
exactly sufficient, and even nested deletion flags balance integrally;
the unresolved content is their reciprocal grouping into common
zero-voltage row cycles.
