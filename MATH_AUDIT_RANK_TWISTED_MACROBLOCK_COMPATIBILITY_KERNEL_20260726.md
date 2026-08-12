# Audit of the rank-twisted macroblock tiling and its exact compatibility kernel

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

The owner-side theorem in
`MATH_THEOREM_RANK_TWISTED_MACROBLOCK_PACKET_TILING_20260726.md` is correct.
The local status cells partition every rank layer, their products partition
the middle owners, and the number of owners in cells of dimension below
\(r=o(m)\) is at most

\[
                         2^{m+o(m)}.                 \tag{0.1}
\]

Every selected axis joins the two halves of one macroblock, so the final
packets have \(s(P)=r\) cross-half axes.  To use the previously audited
quartet Hall toll literally, the halves must be chosen as unions of the old
quartets; taking \(d\) to be a multiple of four supplies this harmless
alignment.  Without it, “cross-half” need not mean “crosses the fixed old
quartet partition.”

The target theorem is not yet determined by the construction as written.
The instruction “choose a deterministic \(r\)-subset of the flexible axes”
does not specify that subset, and the compiler permits an arbitrary
direction bijection.  Different rules give different consecutive-window
compatibility graphs.  Hence there is no single exact Hall ratio for the
selected tiling until the axis-selection and compiler-label rules are part
of the data.

There is, however, an exact universal compatibility kernel for the full
rank-twisted status atlas.  If a lower target has local trace \(T_j\) of
rank \(t_j\), and \(a_j\) of the \(q\) additions are assigned to block
\(j\), put

\[
                         k_j=t_j+a_j.                \tag{0.2}
\]

In the matching \(M_{j,k_j}\), let \(z_j(\mathbf a,T)\) be the number of
edges having both endpoints outside \(T_j\).  Then the exact number of
compatible source owners for this allocation is

\[
 \boxed{
 D_T(\mathbf a)
 =\prod_j2^{a_j}\binom{z_j(\mathbf a,T)}{a_j},
 \qquad \sum_ja_j=q.}                               \tag{0.3}
\]

Different allocation vectors give different source local-rank vectors and
hence disjoint source sets for a fixed target.  Thus the full relaxed
target degree is

\[
 \boxed{
 D^-(T)=
 \sum_{\substack{\mathbf a\ge0\\\sum_ja_j=q}}
 \prod_j2^{a_j}\binom{z_j(\mathbf a,T)}{a_j}.}       \tag{0.4}
\]

For a fixed allocation and a fixed status profile, the exact local
source/target ratio is

\[
 \boxed{
 R(\mathbf a;\mathbf z,\mathbf s)
 =2^q\prod_j
   {\binom{z_j}{a_j}\over\binom{s_j+a_j}{a_j}},}    \tag{0.5}
\]

where \(s_j\) is the number of single-status matching edges in the target.
This is the corrected profile ratio for the rank-twisted atlas.  It is a
conditional fibre ratio, not yet a Hall cut, because one target may use many
different allocations and hence many different matchings
\(M_{t_j+a_j}\).

The complete potential compatibility graph has the exact total edge count

\[
 \boxed{
 E_q=2^q\binom mq\binom{2m-2q}{m-q}}                \tag{0.6}
\]

when \(d\mid m\) and there is no residual block.  Thus it has abundant
global first-moment capacity; its target-average degree is \(W/N_q\) times
its source-average degree.  Formula (0.6) neither proves Hall nor refutes
it.  The remaining theorem is an allocation-mixing/axis-selection theorem,
not another potential-reachability count.

## 1. Owner partition audit

Fix one block \(B=A\dot\cup C\), \(|A|=|C|=d\).  At local rank \(k\), a
perfect matching \(M_k\) partitions the \(2d\) coordinates into \(d\)
pairs.  A \(k\)-set gives each pair status zero, one, or two.  Fixing all
zero/two statuses and leaving every single status free is a physical cube:
each free move exchanges the two endpoints of one matching edge and
preserves rank \(k\).

The status vector of a set is unique, so these cells partition the local
rank layer.  The use of a different matching at another rank is legal
because a cube move never changes local rank.  Products of the local cells
therefore partition the global middle layer.

For the cyclic twist

\[
 M_k=\{a_i c_{i+k\pmod d}:i\in\mathbb Z_d\},        \tag{1.1}
\]

all shifts occur.  Although ranks zero and \(2d\) have no flexible state,
the shift zero also occurs at rank \(d\), and every nonzero shift occurs at
a rank having flexible states.  Hence the physical union of available
local axes is indeed \(K_{d,d}\).

## 2. Leave audit

Fix a local-rank vector \(\mathbf k=(k_1,\ldots,k_b)\).  It freezes one
matching in each macroblock.  Relative to this now fixed collection of
\(db=m+O(d)\) pairs, a uniform unconditioned subset makes each pair flexible
with probability \(1/2\), independently.  Therefore

\[
                         S\sim\operatorname{Bin}(db,1/2).       \tag{2.1}
\]

For \(r=o(m)\),

\[
 \Pr(S<r)
 \le2^{-db}\sum_{i<r}\binom{db}{i}
 =2^{-m+o(m)}.                                      \tag{2.2}
\]

The number of rank vectors is

\[
 (2d+1)^b
 =\exp\!\left(O\!\left({m\log d\over d}\right)\right)
 =2^{o(m)}.                                         \tag{2.3}
\]

For a fixed vector, the subsets actually inducing it form a subfamily of
the sample space in (2.1), so the union bound used in the source note is
valid despite the dependence of \(M_k\) on \(k\).  The residual
\(O(d)\)-coordinate factor is \(2^{o(m)}\).  This proves (0.1), and rank
conditioning can only reduce the leave.

## 3. Exact local compatibility

Fix a lower target trace \(T\subseteq B\), with \(|T|=t\), and suppose
\(a\) additions are assigned to this block.  The source local rank is

\[
                         k=t+a,
\]

so compatibility is tested in \(M_k\), not in \(M_t\).  Let its statuses
on \(T\) be

\[
                         (z,s,v),
\]

the numbers of empty, single, and double edges.  Then

\[
 z+s+v=d,\qquad s+2v=t.                            \tag{3.1}
\]

To obtain a source, choose \(a\) empty edges and put one endpoint of each
into the source.  The orientations give

\[
                         2^a\binom za               \tag{3.2}
\]

sources.  In the source those chosen edges change from empty to single, so
its status profile is

\[
                         (z-a,s+a,v).                \tag{3.3}
\]

Conversely, deleting the selected endpoint on each of \(a\) specified
single edges of a source with profile (3.3) recovers one target.  Thus the
local compatibility graph between these two exact status classes is
biregular with degrees

\[
                         2^a\binom za,\qquad
                         \binom{s+a}a.               \tag{3.4}
\]

The ratio of the class cardinalities is therefore

\[
                         2^a{\binom za\over\binom{s+a}a}.        \tag{3.5}
\]

Multiplying (3.5) over blocks proves (0.5); summing the target-side degrees
over allocations proves (0.3)--(0.4).

The upper kernel is the rank-reversed analogue but should be written
separately because the twist depends on source rank.  If an upper target
\(U\) has local rank \(u\) and receives \(a\) union additions in this
block, then its source rank is

\[
                         k=u-a,
\]

and statuses are taken in \(M_{u-a}\).  Choose \(a\) double edges of the
upper target and retain one endpoint of each in the source.  If the upper
status profile is \((z,s,v)\), the exact target degree and source degree are

\[
                         2^a\binom va,\qquad
                         \binom{s+a}a,               \tag{3.6}
\]

and the local upper source/target ratio is

\[
 \boxed{
                         2^a{\binom va\over\binom{s+a}a}.}      \tag{3.7}
\]

Thus the two signs use the same denominator but sample opposite status
tails and different rank-twisted matchings.

For the cyclic matching, if

\[
 I=\{i:a_i\in T\},\qquad J=\{j:c_j\in T\},
\]

then the empty-edge count has the useful exact form

\[
 z_k(T)=d-|I|-|J|+|I\cap(J-k)|
       =d-t+|I\cap(J-k)|.                           \tag{3.8}
\]

The twist therefore hashes the allocation \(a\) into the cyclic
cross-correlation of the two target halves at shift \(k=t+a\).

## 4. Exact global source enumerator

For a source owner \(X\), let \(S(X)\) be the total number of flexible
matching edges in its rank-twisted product cell.  The number of relaxed
return-free \(q\)-faces ending at \(X\) is

\[
                         \binom{S(X)}q.              \tag{4.1}
\]

Assume for clarity that \(d\mid m\), so \(db=m\) and there is no residual
block.  For one macroblock, although the matching depends on the local
rank, the number of rank-\(k\) sets with a given number of single statuses
is the same for every perfect matching.  Hence the exact bivariate
inventory is

\[
 \sum_{X\subseteq[2m]}x^{|X|}y^{S(X)}
 =(1+2xy+x^2)^m.                                    \tag{4.2}
\]

Differentiate \(q\) times in \(y\), set \(y=1\), extract \([x^m]\), and
divide by \(q!\).  This gives

\[
\begin{aligned}
 \sum_{X\in\binom{[2m]}m}\binom{S(X)}q
 &=[x^m](2x)^q\binom mq(1+x)^{2m-2q}\\
 &=2^q\binom mq\binom{2m-2q}{m-q},                 \tag{4.3}
\end{aligned}
\]

which is (0.6).  Double counting compatibility pairs also gives

\[
                         \sum_TD^-(T)=E_q.           \tag{4.4}
\]

Therefore the exact mean target degree divided by the exact mean source
degree is

\[
                         {W\over N_q}=e^{A^2+o(1)}. \tag{4.5}
\]

The full relaxed catalogue has a constant global source surplus at
Gaussian depth.  Any negative conclusion must use a genuine profile cut or
failure of the selected-axis/compiler subgraph, not total path supply.

## 5. A dangerous but non-Hall fibre calculation

In the dominant allocation regime, almost all of the \(q\) additions occupy
distinct macroblocks because

\[
                         {q\over b}=O(d/\sqrt m)=o(1).           \tag{5.1}
\]

For a roughly uniform allocation the number of repeated-block collisions
is of order \(q^2/b=\Theta_A(d)\), which is not zero but is \(o(q)\).

For one such block \(a=1\), and (3.5) becomes

\[
                         {2z\over s+1}.             \tag{5.2}
\]

At the exactly balanced central status \(z=d/4\), \(s=d/2\), this equals

\[
                         1-{2\over d}+O(d^{-2}).     \tag{5.3}
\]

Thus a single fixed allocation/status fibre can have ratio as small as

\[
                         \exp(-\Theta(q/d)),         \tag{5.4}
\]

which tends to zero for \(d=\Theta(\log m)\) and
\(q=A\sqrt m\).

This is **not** a Hall deficit.  The same target can choose among many
allocation vectors, and changing \(a_j\) changes both the source local-rank
vector and the matching \(M_{t_j+a_j}\).  The union of those source fibres
is exactly what (0.4) counts.  Treating one term of (0.4) as the entire
neighbourhood would repeat the potential-versus-capacity error of the old
quartet lane in the opposite direction.

The calculation does identify the burden on a positive proof: allocation
mixing must recover an \(\exp(\Theta(q/d))\) finite-block loss while keeping
one common owner and compiler assignment.

## 6. Why the selected tiling has no determined Hall ratio yet

Inside a product cell of dimension \(S\), the theorem selects an unspecified
deterministic \(r\)-subset \(R(C)\) of its flexible axes.  The relaxed
compatibility formulas (0.3)--(0.6) use all \(S\) axes.  After selection,
they must be replaced by

\[
 D^-_{R}(T)
 =\#\{X:\text{the required empty edges lie in }R(C_X)\}.        \tag{6.1}
\]

This number can change radically with \(R\).  For example, a lexicographic
rule may concentrate selected axes in early macroblocks, whereas a
block-balanced rule can spread them over \(r\) different macroblocks.
Both satisfy the owner theorem.

Even after \(R\) is fixed, the cell-factor-blind compiler allows a bijection
between the physical axes and its abstract directions.  Actual consecutive
windows use only the \(q\)-subsets and basepoints exposed by that bijection,
not every face counted in (6.1).

Hence the following data are necessary before an exact selected-tiling Hall
ratio exists:

1. an equivariant rule \(C\mapsto R(C)\) selecting the \(r\) axes;
2. a rule distributing those axes among macroblocks;
3. the physical-to-abstract direction bijection in every packet; and
4. the actual consecutive-window basepoint map of the compiler.

The owner theorem proves that any such choices preserve the near-tiling.  It
does not prove that one choice has balanced target capacity.

## 7. The exact next Hall problem

A useful positive formulation is now explicit.  Choose a block-balanced,
rank-equivariant axis selector \(R\) and a direction labeling.  For every
target family \(\mathcal A\subseteq\binom{[2m]}{m-q}\), define its actual
neighbourhood by the consecutive-window kernel induced by those choices.
The missing theorem is

\[
                         |N_R(\mathcal A)|
 \ge|\mathcal A|-o(W)                               \tag{7.1}
\]

simultaneously for both signs and all protected depths, together with a
rounding which uses every source owner once.

At profile level, the first necessary calculation is to sum (0.5) over all
allocations leading into the same source family, controlling overlaps
rather than adding their cardinalities.  Equivalently, one needs an
allocation-flow theorem on the macroblock ranks whose local arc weights are

\[
                         2^a{\binom za\over\binom{s+a}a}.        \tag{7.2}
\]

The cyclic twist enters only through the correlation formula (3.8).  A
proof must show that these shifted correlations average sufficiently across
the selected blocks; potential reachability or the first moment (0.6) is
not enough.

## 8. Audited boundary

Verified:

1. the rank-twisted local and global owner partitions;
2. the leave \(2^{m+o(m)}\);
3. maximal cross-half axis density \(s(P)=r\);
4. the cyclic frame union \(K_{d,d}\);
5. the exact compatibility kernel (0.3)--(0.5); and
6. the exact global potential edge count (0.6).

Not verified, because it is not yet specified or proved:

1. an exact Gaussian Hall ratio for the selected \(Q_r\) tiling;
2. a selector/compiler choice satisfying all profile cuts;
3. simultaneous lower and upper floor balance; or
4. the implication to coefficient one.

The construction decisively solves the owner gate and the dense physical
crossing toll.  The surviving lane is a block-balanced allocation and
consecutive-window scheduling theorem for the exact kernel above, not
another bounded cross-axis round.
