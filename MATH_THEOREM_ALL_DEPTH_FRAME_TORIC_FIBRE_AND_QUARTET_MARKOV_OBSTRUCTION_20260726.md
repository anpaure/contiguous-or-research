# The all-depth common-frame toric fibre: cycle moves, quartet saturation, and a degree-six Markov obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or
external theorem is used.

## 0. Outcome

This note treats the audited all-depth quartet exchanges as candidate
Markov moves.

Let \(\mathcal E\) be the set of legal rooted common-permutation frame
columns.  A column records

1. its top \(U\);
2. one labelled cyclic order on \(U\);
3. one common deleted phase and nested phase-to-depth schedule; and
4. every resulting physical lower and upper target incidence.

Let \(\mathsf A\) be the integer matrix whose rows are the top rows and
all scheduled physical target rows.  For an integral load vector \(b\),
the exact frame-table fibre is

\[
 \mathcal F_b=
 \{x\in\mathbb Z_{\ge0}^{\mathcal E}:\mathsf A x=b\}.
\tag{0.1}
\]

The checkerboard quartets are degree-four binomials in the toric ideal
\(I_{\mathsf A}\).  The main conclusions are as follows.

1.  Fix an \((M-2)\)-set \(C\), a positional word on
    \(C\cup\{A,B\}\), and an outside label set \(Z\).  The two orders on
    each top \(C\cup\{u,v\}\) identify a frame table with a tournament
    on \(Z\).  Its complete all-depth load vector depends only on the
    tournament score sequence.  Thus every fixed-score tournament fibre
    embeds in one literal physical-load fibre.

2.  Reversing any directed label cycle is an exact literal all-depth
    frame move.  A cycle of length \(r\) gives a degree-\(r\) toric
    binomial.  Triangles are the indispensable primitive moves in this
    sector and connect every tournament fibre with fixed scores.

3.  Checkerboard quartets are exactly directed \(4\)-cycle reversals.
    Over \(\mathbb Z\), their lattice has index two in the full cycle
    lattice.  The quotient is only the already audited odd-cycle parity.
    Thus, after parity is neutralized, there is no further *lattice*
    obstruction in this sector.

4.  Nevertheless quartets are not a Markov basis, even after parity is
    neutralized.  On six labels, take two directed triangles and orient
    every cross edge from the first triangle to the second.  Reverse
    both triangles.  The two tournaments have the same score sequence
    and hence identical physical loads at every phase and every depth.
    Their difference has degree six and lies in the integer quartet
    lattice.  Every affine mod-two top character evaluates to zero on
    it.

    But neither tournament contains a directed \(4\)-cycle.  Therefore
    no checkerboard quartet is applicable at either endpoint: both are
    isolated vertices of the quartet move graph.

5.  Algebraically, the degree-six binomial lies in the saturation of
    the quartet ideal by the frame variables, but not in the quartet
    ideal itself.  The obstruction is nonnegative/Markov, not another
    parity or real-span defect.

The degree-six double triangle is the smallest parity-neutral
obstruction beyond a quartet in this cycle sector.  Hence checkerboard
quartets do not generate the exact integer fibre.  Any Markov basis must
contain odd-cycle moves, or parity-neutral compounds which can traverse
the corresponding triangle blocks without requiring a pre-existing
directed \(4\)-cycle.

The result is an exact no-go for quartets as a universal Markov basis.
It does not yet prove that the degree-six obstruction persists in the
particular global fibre having one frame at every top; moves through
additional occupied tops may provide detours there.

## 1. The exact integer configuration

Let

\[
 \mathcal U=\binom{[n]}M.
\tag{1.1}
\]

For each top \(U\), let \(\mathcal C(U)\) be the selected legal
common-permutation columns.  A column \(e\in\mathcal C(U)\) contains a
rooted cyclic order, its retained phase set, and one nested tag schedule.
For every scheduled signed depth \(q\) and physical target \(S\), put

\[
 a_{S,q,e}=
 \#\{\text{retained phase occurrences of }S
       \text{ in column }e\text{ at signed depth }q\}.
\tag{1.2}
\]

The top rows are

\[
 a_{U,e}=\mathbf1\{e\in\mathcal C(U)\}.
\tag{1.3}
\]

The matrix \(\mathsf A\) consists of (1.2)--(1.3).  Thus (0.1) is the
literal nonnegative integer fibre with fixed top multiplicities and
fixed all-depth target loads.  The physical one-frame problem is the
special case

\[
                         b_U=1\qquad(U\in\mathcal U),
\tag{1.4}
\]

but a Markov basis for \(\mathsf A\) must connect every nonempty fibre,
including fibres with some \(b_U=0\).

For a move \(z\in\ker_{\mathbb Z}\mathsf A\), write

\[
                         z=z^+-z^-,
\qquad z^+,z^-\in\mathbb Z_{\ge0}^{\mathcal E},
\tag{1.5}
\]

with disjoint supports.  Its binomial is

\[
                         X^{z^+}-X^{z^-}.
\tag{1.6}
\]

A set \(\mathcal M\subseteq\ker_{\mathbb Z}\mathsf A\) is a Markov
basis precisely when, for every \(b\), the graph on \(\mathcal F_b\)
obtained by the applicable moves in \(\pm\mathcal M\) is connected.

The checkerboard quartet from the audited exchange theorem has four
columns on each side and is therefore a degree-four move.

## 2. The fixed-core tournament sector

Fix

\[
                         C\in\binom{[n]}{M-2}
\tag{2.1}
\]

and a cyclic positional word

\[
                         \omega
 \quad\text{on}\quad C\cup\{A,B\}.
\tag{2.2}
\]

Fix also one common retained phase set and one common nested tag
schedule.  Let \(Z\subseteq[n]\setminus C\).  For distinct
\(u,v\in Z\), put

\[
                         U_{uv}=C\cup\{u,v\}.
\tag{2.3}
\]

There are two frame columns under consideration on this top:

\[
\begin{aligned}
 e_{u\to v}&:\quad A\mapsto u,\quad B\mapsto v,\\
 e_{v\to u}&:\quad A\mapsto v,\quad B\mapsto u,
\end{aligned}
\tag{2.4}
\]

with every label of \(C\) left at its common position.

Impose the top margins

\[
 x_{u\to v}+x_{v\to u}=1
 \qquad(\{u,v\}\in\tbinom Z2).
\tag{2.5}
\]

An integral table in this sector is therefore a tournament \(T\) on
\(Z\): orient \(u\to v\) exactly when \(x_{u\to v}=1\).

Write

\[
                         d_T(u)=|\{v:u\to v\text{ in }T\}|
\tag{2.6}
\]

for its score sequence.

### Theorem 2.1 (all-depth loads factor through scores)

The aggregate interval-load vector of the frame table associated with
\(T\) depends only on

\[
                         (d_T(u))_{u\in Z}.
\tag{2.7}
\]

If the rows are refined by positional phase, then any retained
positional interval containing \(A\) but not \(B\) determines (2.7).
Consequently the phase-refined sector fibre is exactly a tournament
score fibre.  Without phase refinement, every fixed-score tournament
fibre is still contained in one physical-load fibre.

#### Proof

Fix one retained phase and interval length, and let \(K\subseteq C\) be
the core labels in that positional interval.

If the interval contains neither placeholder, every top contributes
the same target \(K\).  If it contains both, the top
\(\{u,v\}\) contributes \(K\cup\{u,v\}\), independently of its
orientation.

If the interval contains \(A\) but not \(B\), the oriented top
\(u\to v\) contributes

\[
                         K\cup\{u\}.
\tag{2.8}
\]

Thus the multiplicity of \(K\cup\{u\}\), after summing over all pair
tops, is \(d_T(u)\).  If the interval contains \(B\) but not \(A\), it
is the indegree

\[
                         |Z|-1-d_T(u).
\tag{2.9}
\]

This proves factorization through the scores at every phase and length,
and hence after aggregation.  In the phase-refined table, a retained
interval containing exactly \(A\) recovers every \(d_T(u)\) from
(2.8). \(\square\)

The condition in the last paragraph can always be enforced by placing
the placeholders farther apart than the largest controlled window and
retaining one appropriate phase.  It is automatic if all proper
interval lengths are included.

The root-form promotion middle targets are complements of positional
intervals with a common phase shift.  Complementation is a coordinate
permutation, so Theorem 2.1 applies without alteration to the literal
middle, lower, and upper ledgers.

## 3. All directed cycles are physical toric moves

Let

\[
                         z_0,z_1,\ldots,z_{r-1}\in Z
\tag{3.1}
\]

be distinct, with subscripts modulo \(r\).  Consider the two frame
tables on the \(r\) pair tops \(U_{z_i z_{i+1}}\):

\[
\begin{aligned}
 T^\to&:\quad z_i\to z_{i+1}\quad(0\le i<r),\\
 T^\leftarrow&:\quad z_{i+1}\to z_i\quad(0\le i<r).
\end{aligned}
\tag{3.2}
\]

All other pair tops, if present, are identical on the two sides.

### Theorem 3.1 (phasewise cycle exchange)

For every \(r\ge3\), the replacement

\[
                         T^\to\longleftrightarrow T^\leftarrow
\tag{3.3}
\]

is an exact degree-\(r\) move in \(\ker_{\mathbb Z}\mathsf A\).  It
preserves every phasewise interval load, every common deleted phase, and
every common nested tag schedule.

#### Proof

Fix a positional interval and its core set \(K\).  If it contains zero
or two placeholders, the two sides agree top by top.

If it contains only \(A\), the two aggregate contributions are

\[
 \sum_{i=0}^{r-1}e_{K\cup\{z_i\}},
 \qquad
 \sum_{i=0}^{r-1}e_{K\cup\{z_{i+1}\}},
\tag{3.4}
\]

which are equal after cyclic reindexing.  The only-\(B\) case is the
same identity in the opposite direction.  The statement follows
phase by phase, and hence after every common deletion and nested
weighting. \(\square\)

For \(r=3\), this is a triangle reversal.  For \(r=4\), after writing
the cycle bipartition as

\[
                         a_0,b_0,a_1,b_1,
\tag{3.5}
\]

it is exactly the audited checkerboard quartet.

### Theorem 3.2 (triangle Markov theorem for each score subfibre)

Triangle reversals connect every two tournaments on \(Z\) having the
same score sequence.  Hence the degree-three cycle binomials form a
Markov basis for every fixed-score subfibre, and for the phase-refined
fixed-core tournament configuration.

#### Proof

Let \(T,T'\) have the same scores.  Direct every edge on which they
differ according to its orientation in \(T\).  At every vertex the
number of outgoing difference edges equals the number of incoming
difference edges, because the scores agree.  The directed difference
graph is therefore Eulerian and decomposes into directed cycles.

Reversing one such cycle preserves every score and removes all of its
edges from the difference graph.  It remains to decompose a directed
cycle reversal into applicable triangle reversals.

Let

\[
                         v_1\to v_2\to\cdots\to v_r\to v_1
\tag{3.6}
\]

be a directed cycle with \(r\ge4\).  Inspect the chord \(v_1v_3\).
If \(v_3\to v_1\), first reverse the directed triangle

\[
                         v_1\to v_2\to v_3\to v_1
\tag{3.7}
\]

and then reverse the resulting directed \((r-1)\)-cycle

\[
                         v_1\to v_3\to v_4\to\cdots\to v_r\to v_1.
\tag{3.8}
\]

The chord is flipped twice and every edge of (3.6) once.  If instead
\(v_1\to v_3\), perform (3.8) first.  Its reversal creates the directed
triangle (3.7); reverse that triangle second.  Again the chord is
flipped twice and precisely the original cycle is reversed.

Induction on \(r\) proves the decomposition.  Repeating over the
Eulerian cycle decomposition connects \(T\) to \(T'\). \(\square\)

The three-vertex fibre containing the two orientations of a directed
triangle has exactly two states.  Therefore the cubic triangle move is
indispensable in this sector.

## 4. What quartets generate over \(\mathbb Z\)

Choose an arbitrary reference orientation of the edges of \(K_Z\).  Let

\[
 \partial:\mathbb Z^{E(K_Z)}\longrightarrow\mathbb Z^Z
\tag{4.1}
\]

be its signed vertex-edge incidence matrix.  The difference of two
tournaments with the same scores is an element of the integral cycle
lattice

\[
                         \mathcal L_{\rm cyc}=\ker_{\mathbb Z}\partial.
\tag{4.2}
\]

Let \(\mathcal L_4\) be the lattice generated by the signed incidence
vectors of simple \(4\)-cycles.

### Theorem 4.1 (quartet lattice has index two)

For \(|Z|\ge4\),

\[
 \boxed{
 \mathcal L_4=
 \left\{
 z\in\mathcal L_{\rm cyc}:
 \sum_{e\in E(K_Z)}z_e\equiv0\pmod2
 \right\}.}
\tag{4.3}
\]

Consequently

\[
                         \mathcal L_{\rm cyc}/\mathcal L_4
                         \cong\mathbb Z/2\mathbb Z.
\tag{4.4}
\]

There is no additional integral lattice invariant in the fixed-core
sector after this parity is neutralized.

#### Proof

The parity in (4.3) is independent of the arbitrary reference
orientation.  Every \(4\)-cycle has four nonzero coefficients and hence
lies in its kernel.

Fix a vertex \(0\in Z\).  Orient the relevant edges consistently and
write the triangle cycle vectors as

\[
                         \tau_{ij}=e_{0i}+e_{ij}-e_{0j}
\qquad(i,j\in Z\setminus\{0\})
\tag{4.5}
\]

generate \(\mathcal L_{\rm cyc}\): subtract the appropriate
\(\tau_{ij}\) to clear every edge not incident with \(0\), after which
the zero-divergence condition clears the remaining star edges.

For distinct \(i,j,k\), suitable orientations of the three
\(4\)-cycles on \(\{0,i,j,k\}\) give

\[
 \tau_{ij}+\tau_{jk},\qquad
 -\tau_{ij}+\tau_{ik},\qquad
 \tau_{ik}-\tau_{jk}
 \quad\in\mathcal L_4.
\tag{4.6}
\]

Combining the three displayed vectors gives
\(2\tau_{ij}\in\mathcal L_4\), and similarly for every star triangle.
The line graph on the pairs \(\{i,j\}\) is connected, so (4.6) also
identifies all star-triangle classes up to sign modulo
\(\mathcal L_4\).  Since each class has order at most two, all of them
are the same order-two class.  Therefore every combination of the
\(\tau_{ij}\)'s whose coefficient sum is even belongs to
\(\mathcal L_4\).

Modulo two, every triangle has odd edge sum, so the parity of a cycle
equals the coefficient sum in any star-triangle expansion.  This proves
(4.3).  A triangle represents the nonzero quotient class, proving
(4.4). \(\square\)

The theorem distinguishes two questions:

* **lattice generation:** after the one parity class is fixed, quartet
  vectors generate every integer kernel direction;
* **Markov generation:** the required quartet summands may need frame
  variables absent from the current nonnegative table.

The second statement does not follow from the first.

## 5. A parity-neutral degree-six Markov obstruction

Take six outside labels

\[
 A_0=\{a_0,a_1,a_2\},
 \qquad
 B_0=\{b_0,b_1,b_2\}.
\tag{5.1}
\]

Define a tournament \(T\) on their union by

\[
\begin{aligned}
 a_0&\to a_1\to a_2\to a_0,\\
 b_0&\to b_1\to b_2\to b_0,\\
 a_i&\to b_j\qquad(0\le i,j\le2).
\end{aligned}
\tag{5.2}
\]

Let \(T'\) reverse the two internal triangles and leave all nine cross
edges unchanged.

### Theorem 5.1 (double-triangle obstruction)

The frame tables associated with \(T\) and \(T'\) satisfy all of the
following.

1. They lie in the same exact all-depth fibre \(\mathcal F_b\).
2. Their difference is a degree-six integer kernel vector in
   \(\mathcal L_4\).
3. Every affine mod-two top character from the earlier parity audit has
   the same value on the two tables.
4. Neither table admits an applicable checkerboard quartet.

Consequently checkerboard quartets do not connect \(\mathcal F_b\) and
do not form a Markov basis.

#### Proof

Every \(a_i\) has score \(4\): one win in its internal triangle and
three cross wins.  Every \(b_j\) has score \(1\).  Reversing a directed
triangle preserves the score one at each of its vertices.  Hence \(T\)
and \(T'\) have the same scores, and Theorem 2.1 proves Item 1.
Equivalently, apply the exact triangle identity of Theorem 3.1 twice.

The difference reverses six pair tops.  It is the sum of two triangle
cycle vectors and therefore has even edge parity.  Theorem 4.1 puts it
in \(\mathcal L_4\), proving Item 2.

For Item 3, let

\[
                         w(U)=\alpha_0+\sum_{x\in U}\alpha_x
                         \pmod2
\tag{5.3}
\]

be any affine top character.  The six changed tops are the three pair
tops internal to \(A_0\) and the three internal to \(B_0\).  Their total
character is zero: the constant term occurs six times; every
\(c\in C\) occurs six times; and every \(a_i,b_j\) occurs twice.

Finally, every directed cycle of \(T\) lies inside one of the two
three-vertex blocks.  Indeed all cross edges point from \(A_0\) to
\(B_0\), so a directed walk which enters \(B_0\) cannot return to
\(A_0\).  Neither block contains four vertices.  Thus \(T\) has no
directed \(4\)-cycle.  The same argument applies to \(T'\).

By (3.5), an applicable checkerboard quartet is exactly a directed
\(4\)-cycle reversal.  Hence both tables are isolated in the quartet
move graph, proving Item 4 and the theorem. \(\square\)

### Corollary 5.2 (quartet ideal is not saturated)

Let \(I_4\) be the binomial ideal generated by the checkerboard quartet
binomials in this sector, and let

\[
                         \mathfrak m=\prod_e X_e
\tag{5.4}
\]

be the product of all frame variables.  The double-triangle binomial
\(B_6\) satisfies

\[
                         B_6\notin I_4,
\qquad
                         B_6\in I_4:\mathfrak m^\infty.
\tag{5.5}
\]

#### Proof

If \(B_6\in I_4\), the standard monomial-fibre interpretation of a
binomial move ideal would give a path between its two monomials using
applicable quartet binomials.  Theorem 5.1 says both endpoints are
quartet-isolated, so \(B_6\notin I_4\).

Its exponent difference lies in the lattice generated by quartets by
Theorem 5.1(2).  Clearing the negative parts of an integer quartet
decomposition by a sufficiently large common monomial multiplier puts
that multiplier times \(B_6\) in \(I_4\).  This is exactly membership
in the saturation. \(\square\)

This is an integral positivity obstruction.  The real span and the
integer lattice both contain the double-triangle direction; only the
nonnegative fibre fails to realize the required chord intermediates.

## 6. Minimality and literal promotion validity

Within the fixed-core cycle sector:

* degree \(3\) gives the indispensable triangle, but it carries the odd
  parity class;
* degree \(4\) is the checkerboard move itself;
* degree \(5\) again carries odd cycle parity; and
* degree \(6\) is therefore the smallest possible parity-neutral degree
  beyond a quartet.

Theorem 5.1 realizes that minimum.

Every column used above is an actual labelled cyclic frame.  The cycle
identity is phasewise and therefore survives:

1. a common deleted phase;
2. arbitrary common phase weights;
3. the complete nested lower and upper tag schedule; and
4. root-form complementation at the middle layer.

For the mechanical atlas, place \(A,B\) in two positions with the same
mechanical bit and choose the six outside labels from that same shore.
Then every column in the construction respects the common mechanical
binary word.  Thus the degree-six obstruction is present in the
mechanical subatlas whenever that shore has at least six available
labels.

To view the construction as a fibre of the full matrix \(\mathsf A\),
take top margin one on the fifteen tops

\[
                         C\cup\{u,v\},
 \qquad \{u,v\}\in\binom{A_0\cup B_0}2,
\tag{6.1}
\]

and top margin zero elsewhere.  A quartet involving any other top is
inapplicable.  Among the fifteen occupied tops, applicable quartets are
exactly directed \(4\)-cycles, of which Theorem 5.1 supplies none.
Hence this is a genuine integer fibre of the full column matrix, not
only a formal relation in a projected score table.

## 7. Exact Markov-basis verdict

The audited checkerboard exchanges pass every linear load test but fail
the exact integer connectivity test.

Proved here:

1. the exact toric fibre of common-permutation frame tables with fixed
   top and all-depth physical loads;
2. a fixed-core tournament realization of that fibre;
3. an all-depth physical cycle exchange at every degree \(r\ge3\);
4. a triangle Markov theorem for the tournament sector;
5. the exact index-two quartet sublattice over \(\mathbb Z\);
6. a parity-neutral degree-six pair in that sublattice whose endpoints
   are both quartet-isolated;
7. the corresponding nonsaturation of the quartet binomial ideal; and
8. literal compatibility with one-hole, nested-tag, root-complement,
   and mechanical-support conventions.

Not proved:

1. a Markov basis for the full global one-frame-at-every-top fibre;
2. that triangle or degree-six moves can be packed with bounded
   congestion across the critical root stars;
3. an energy descent toward balanced target loads; or
4. coefficient one.

The smallest missing primitive is already visible: the quartet atlas
must be enlarged by odd-cycle moves, or by degree-six compounds capable
of crossing a pair of triangle blocks without requiring an available
directed \(4\)-cycle.  Merely knowing that quartets span the parity-even
integer kernel is insufficient.
