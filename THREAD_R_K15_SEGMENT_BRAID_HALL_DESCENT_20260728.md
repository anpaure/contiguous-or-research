# The \(k=15\) three-cut segment Shadow--Braid and exact Hall descent

Date: 2026-07-28

Status: exact general segment-braid theorem, exact audit of the named
\(\operatorname{RF}(471,2327,5456)\) move, and an exact Hall-current descent
criterion.  The move is a genuine nonlocal realization of one clean
flag-graph \(C_6\), preserves depth-three residence and the complete lower
and upper support profiles through depth seven, and lowers the unpeeled
Hall deficiency from \(29\) to \(28\).  This note audits that first step.
Subsequent exact work found three further three-cut braids reaching Hall
\(25\), then exhausted the same one-move catalogue at Hall \(25\); see
`MATH_K15_THREE_CUT_SEGMENT_BRAID_DESCENT_20260728.md`.  Nothing here
proves a route from Hall \(25\) to zero, preserves the old peeled
reservations at their absolute addresses, or solves the simultaneous
one-word lower compiler.

No web search or solver run was used in this audit.  The global counts
\(12{,}013\) resident and \(9{,}243\) upper-safe moves are taken as supplied
input: the present source and JSON do not contain a self-contained census
log.  The named move, all seam/shadow/residence claims, the materialized
path, the Hall number, and the critical-shore exchange were independently
checked from the stored path.

## 0. Verdict

The three-cut braid is the first verified mechanism in this lane which
simultaneously has all of the following properties.

1. It is integral inside one middle chronology: it permutes the \(6435\)
   rank-eight owners and remains a vertex-simple Johnson path.
2. Only three unordered middle edges change.  The named move's old and new
   boundary matchings form a clean alternating \(C_6\).
3. The three rank-seven lower seam colours are fixed pointwise and the three
   rank-nine upper seam colours are cyclically permuted.  Hence both
   adjacent shadow **multisets** are exactly preserved.
4. Every expected-rank lower and upper support through depth seven is
   preserved, and depth-three residence remains exact.
5. The exact lower-target candidate graph gains twelve edges and its
   matching number increases from \(16354\) to \(16355\).

The Hall mechanism is not a new incidence for target \(6308\).  The maximal
controller still has no letter \(6308\), the rank-five canonical missing set
still contains \(6308\), and the Hall degree of target \(6308\) remains
\(14\).  Instead, one physical depth-two cell in the old critical shore is
replaced by two independently usable cells after the braid.

There is an exact descent theorem for an individual braid, stated in
Section 6.  What remains unproved is the expansion statement needed for
iteration: every reachable positive-deficiency state must admit a
residence- and support-safe braid satisfying the all-shore Hall-current
inequality.  Move abundance at the initial state does not imply this.

## 1. The exact three-cut segment-braid theorem

Let

\[
                         T=(T_0,\ldots,T_{W-1})
\]

be a vertex-simple path in \(J(n,r)\), and choose

\[
                         1\le a<u\le v<W-1.
\]

Write

\[
\begin{aligned}
 A&=T_0\cdots T_{a-1},&
 B&=T_a\cdots T_{u-1},\\
 C&=T_u\cdots T_v,&
 D&=T_{v+1}\cdots T_{W-1},
\end{aligned}
\tag{1.1}
\]

and put

\[
 x=T_{a-1},\quad b_0=T_a,\quad b_1=T_{u-1},\quad
 c_0=T_u,\quad c_1=T_v,\quad d=T_{v+1}.
\tag{1.2}
\]

For \(\epsilon_B,\epsilon_C\in\{F,R\}\), form

\[
                  T^\tau=A\,C^{\epsilon_C}\,B^{\epsilon_B}\,D,
\tag{1.3}
\]

where \(R\) means reversal.  The native convention names a move by the
orientation of \(C\), followed by the orientation of \(B\).

### Theorem 1.1 (necessary and sufficient endpoint tests)

The sequence (1.3) is a Johnson path if and only if the three displayed
new interfaces in its row are Johnson edges:

\[
\begin{array}{c|ccc}
\text{type}&A|C&C|B&B|D\\ \hline
FF&x\sim c_0&c_1\sim b_0&b_1\sim d\\
RF&x\sim c_1&c_0\sim b_0&b_1\sim d\\
FR&x\sim c_0&c_1\sim b_1&b_0\sim d\\
RR&x\sim c_1&c_0\sim b_1&b_0\sim d.
\end{array}
\tag{1.4}
\]

When these tests hold, \(T^\tau\) contains exactly the same middle owners,
with exactly the same multiplicities, as \(T\).  In particular, a Hamilton
path remains a Hamilton path and the middle deck is exact.

For \(FF,RF,FR\), the old cut positions are

\[
                         a,\quad u,\quad v+1,
\tag{1.5}
\]

and the new seam positions are

\[
                         a,\quad a+v-u+1,\quad v+1.
\tag{1.6}
\]

Only the three corresponding unordered Johnson edges change.  In the \(RR\)
case, \(c_0b_1\) is the old \(B|C\) edge reversed, so only the two exterior
edges change.

#### Proof

Every internal edge of \(A,B,C,D\) is inherited.  Reversal does not affect
adjacency because the Johnson graph is undirected.  Thus the only possible
failures are exactly the interfaces in (1.4), proving necessity and
sufficiency.  Equation (1.3) is a permutation of the four retained vertex
lists, so it preserves the deck.  The cut and seam positions follow from
the segment lengths.  Finally,

\[
                 A\,\overleftarrow C\,\overleftarrow B\,D
                 =A\,\overleftarrow{BC}\,D,
\]

which explains the two-cut \(RR\) exception.  \(\square\)

This is a seam-local theorem for unordered middle edges.  Ordered
chronology is not local: reversing an internal transition replaces
\((\alpha,\beta)\) by \((\beta,\alpha)\), and thousands of absolute
physical addresses can move.

## 2. Exact shadow and residence ledgers

For an unordered Johnson edge \(e=XY\), put

\[
                         L(e)=X\cap Y,\qquad U(e)=X\cup Y.
\]

Let

\[
 E_{\rm old}=\{xb_0,b_1c_0,c_1d\},
\tag{2.1}
\]

and let \(E_{\rm new}\) be the three interfaces from the relevant row of
(1.4).

### Proposition 2.1 (adjacent-shadow current)

The complete signed adjacent currents, including multiplicity, are

\[
 \Delta^-_1=
 \sum_{e\in E_{\rm new}}\mathbf e_{L(e)}
 -\sum_{e\in E_{\rm old}}\mathbf e_{L(e)},
\tag{2.2}
\]

\[
 \Delta^+_1=
 \sum_{e\in E_{\rm new}}\mathbf e_{U(e)}
 -\sum_{e\in E_{\rm old}}\mathbf e_{U(e)}.
\tag{2.3}
\]

The braid preserves both adjacent shadow multisets if and only if

\[
                         \Delta^-_1=\Delta^+_1=0.
\tag{2.4}
\]

#### Proof

Every internal edge of a retained segment has one old/new mate, possibly
with reversed orientation.  Intersection and union ignore orientation, so
all internal contributions cancel.  Equations (2.2)--(2.3) are the
remaining boundary terms.  \(\square\)

For \(q\ge1\), define the exact intersection and union loads

\[
 \mu^\cap_{q,Z}(T)=
 \#\left\{i:\bigcap_{j=0}^{q}T_{i+j}=Z\right\},
\qquad
 \mu^\cup_{q,Z}(T)=
 \#\left\{i:\bigcup_{j=0}^{q}T_{i+j}=Z\right\}.
\tag{2.5}
\]

Let \({\cal O}_q\) be the set of old \(q\)-window starts crossing at least
one old cut, and let \({\cal N}_q\) be its new-seam analogue.  A window
crossing several seams occurs once in these sets.

### Theorem 2.2 (all-depth seam ledger)

For every mask \(Z\),

\[
\begin{aligned}
 \mu^\cap_{q,Z}(T^\tau)-\mu^\cap_{q,Z}(T)
 &=
 \sum_{i\in{\cal N}_q}
 {\bf1}\!\left[\bigcap_{j=0}^{q}T^\tau_{i+j}=Z\right]\\
 &\quad-
 \sum_{i\in{\cal O}_q}
 {\bf1}\!\left[\bigcap_{j=0}^{q}T_{i+j}=Z\right],
\end{aligned}
\tag{2.6}
\]

and the same identity holds with intersections replaced by unions.

If the four retained segments are longer than \(q\), and the relevant cuts
and endpoints are \(q\)-separated, then

\[
                 |{\cal O}_q|=|{\cal N}_q|=3q
\tag{2.7}
\]

for \(FF,RF,FR\).  The set formula (2.6) remains valid without separation.

#### Proof

A window wholly inside one retained segment has a unique translated or
reflected mate.  Intersection and union are invariant under reversal.
Exactly the crossing windows remain.  Under the separation hypothesis, one
cut belongs to exactly \(q\) \(q\)-edge windows and the three families are
disjoint.  \(\square\)

Thus exact multiset preservation is the equality of every load in (2.6),
whereas support preservation requires only

\[
          \mu^{\cap/\cup}_{q,Z}(T)+\Delta^{\cap/\cup}_{q,Z}\ge1
\tag{2.8}
\]

for each required target.  These claims must not be conflated.

### Proposition 2.3 (residence under oriented segment transport)

Assume \(T\) has no internally bounded positive-coordinate run of at most
\(h\) vertices.  Write the new transitions as

\[
                     T^\tau_{i+1}=T^\tau_i-\alpha'_i+\beta'_i.
\]

Then \(T^\tau\) is \(h\)-resident if and only if

\[
                         \beta'_i\ne\alpha'_j
\tag{2.9}
\]

for every \(i<j\), \(j-i\le h\), whose transition interval meets the new
seam set.

#### Proof

A run wholly inside a translated segment is unchanged.  A run wholly inside
a reversed segment has the same length with its endpoints interchanged.
Thus a new forbidden run must cross a new seam.  Such a positive run starts
when \(\beta'_i\) is inserted and ends when the same coordinate is
\(\alpha'_j\), giving (2.9).  \(\square\)

This positive-run condition is weaker than full \(G_h\) trace-rainbow.
For a linear path, runs meeting a global endpoint are exempt; cyclic paths
require cyclic indexing.

The seam-retention argument also gives

\[
                         |\nu_h(T^\tau)-\nu_h(T)|\le3
\tag{2.10}
\]

for \(FF,RF,FR\), and at most two for \(RR\).  Indeed, every packed interval
not wholly in a retained interior contains a distinct deleted or inserted
seam edge.

## 3. The named \(\operatorname{RF}(471,2327,5456)\) certificate

For the frozen \(k=15\) path,

\[
                         W=6435,
\]

take

\[
                         (a,u,v)=(471,2327,5456).
\]

The segment lengths are

\[
                         471,\quad1856,\quad3130,\quad978,
\tag{3.1}
\]

and the materialized move is

\[
                         A\,B\,C\,D
                         \longmapsto
                         A\,\overleftarrow C\,B\,D.
\tag{3.2}
\]

Equivalently,

\[
 T'_{471\ldots3600}=T_{5456\ldots2327},\qquad
 T'_{3601\ldots5456}=T_{471\ldots2326}.
\tag{3.3}
\]

The JSON path satisfies (3.3) at all \(6435\) positions, retains all
distinct rank-eight owners, and every one of its \(6434\) transitions is a
Johnson edge.

The six cut endpoints are

\[
 (x,b_0,b_1,c_0,c_1,d)
 =(7277,6381,6319,7341,6255,7215).
\tag{3.4}
\]

The exact seam table is

\[
\begin{array}{c|c|c|c|c}
 &\text{old edge}&(L,U)&\text{new edge}&(L,U)\\ \hline
1&xb_0&(6253,7405)&xc_1&(6253,7279)\\
2&b_1c_0&(6317,7343)&c_0b_0&(6317,7405)\\
3&c_1d&(6191,7279)&b_1d&(6191,7343).
\end{array}
\tag{3.5}
\]

Consequently the lower colours are fixed pointwise and the upper colours
undergo the cycle

\[
              (7405,7343,7279)\longmapsto(7279,7405,7343).
\tag{3.6}
\]

Both adjacent shadow multisets are therefore exactly preserved.

### Proposition 3.1 (the boundary switch is one clean flag \(C_6\))

Put

\[
 K=\{0,2,3,5,11,12\}\quad(\text{mask }6189),
\]

\[
                         (a_0,a_1,a_2)=(6,7,1),\qquad c=10.
\tag{3.7}
\]

The lower rows are

\[
 R_0=K+6=6253,\qquad
 R_1=K+7=6317,\qquad
 R_2=K+1=6191,
\tag{3.8}
\]

and the upper columns are

\[
\begin{aligned}
 U_0&=K+\{6,7,10\}=7405,\\
 U_1&=K+\{7,1,10\}=7343,\\
 U_2&=K+\{1,6,10\}=7279.
\end{aligned}
\tag{3.9}
\]

The old boundary matching is \(R_iU_i\); the new one is

\[
                         R_0U_2,\qquad R_1U_0,\qquad R_2U_1.
\tag{3.10}
\]

Hence (3.2) is the exact nonlocal realization of the clean \(C_6\) from
the earlier flag-table theorem.

This identifies what the local two-state blocks lacked.  The reversed
3130-owner segment supplies an exterior-moving collar, so the other two
clean-C6 seams really occur in the frozen factor.  The earlier companion-
edge obstruction remains valid for fixed-address atomic blocks; (3.2)
escapes its hypothesis by transporting whole retained segments.

### Proposition 3.2 (exact residence)

The new seam positions are

\[
                         471,\quad3601,\quad5457.
\]

Every retained interior is old or coherently reversed.  Direct inspection
of the three depth-three collars gives no equality
\(\beta'_i=\alpha'_{i+t}\) for \(1\le t\le3\).  Equivalently, the whole
path has zero forbidden internal runs, with minimum positive-run length
four.  Thus (3.2) is depth-three resident.

The native residence predicate proves only positive-run residence, not the
stronger pairwise-rainbow condition.

## 4. Exact all-depth and maximal-controller audit

All four segments in (3.1) have length greater than seven.  Therefore the
ledger at depth \(q\le7\) contains exactly \(3q\) old and \(3q\) new
crossing windows.

The following table records expected-rank support and the number of masks
whose multiplicity changes.  A zero in the last column means multiset
equality; equality of support alone is weaker.

\[
\begin{array}{c|c|c|c|c}
q&
\text{upper support }|\binom{[15]}{8+q}|&
\#\text{ changed upper multiplicities}&
\text{lower support}/\text{holes at rank }8-q&
\#\text{ changed lower multiplicities}\\ \hline
1&5005&0&6431/4&0\\
2&3003&0&4984/21&4\\
3&1365&5&2999/4&8\\
4&455&2&1364/1&10\\
5&105&2&455/0&6\\
6&15&1&105/0&3\\
7&1&0&15/0&0.
\end{array}
\tag{4.1}
\]

Every upper support is complete.  Every lower missing set is unchanged.
The nonempty lower missing sets are

\[
\begin{aligned}
q=1:\quad&
\{5801,7267,8877,13620\},\\
q=2:\quad&
\{311,685,1103,1581,2420,2575,2676,3651,4213,4877,7504,8869,\\
&\qquad9524,13616,17683,17738,18272,18970,19568,21641,29776\},\\
q=3:\quad&
\{6308,6928,7681,16399\},\\
q=4:\quad&
\{16646\}.
\end{aligned}
\tag{4.2}
\]

Depths \(5,6,7\) have no lower holes.  In particular, the braid preserves
the complete all-depth support profile but does not fill the canonical
rank-five hole \(6308\).

For audit precision, the nonzero expected-rank multiplicity changes at the
first deeper levels are

\[
\begin{array}{c|l}
\text{upper }q=3&
7919:-1,\ 8047:-1,\ 8111:+1,\ 15983:+1,\ 16109:-1\\
\text{lower }q=2&
4205:+1,\ 4269:-1,\ 6245:-1,\ 6309:+1\\
\text{lower }q=3&
109:+1,\ 173:-1,\ 4197:-1,\ 4201:+1,\ 4261:+1,\ 4265:-1,\
6241:-1,\ 6305:+1.
\end{array}
\tag{4.3}
\]

Thus “all upper layers survive” means last-witness support, not multiset
equality beyond \(q=2\).  The native source checks the upper support through
seven and lower \(q=1\) only; the deeper lower assertions in (4.1)--(4.3)
come from the direct named-path audit.

Define the maximal depth-three erosion word

\[
 P'_p=
 \bigcap_{i=\max(0,p-3)}^{\min(p,6434)}T'_i,
 \qquad0\le p\le6437.
\tag{4.4}
\]

Then

\[
 \#\{|P'_p|=5,6,7,8\}=(6432,2,2,2),
\tag{4.5}
\]

every \(P'_p\) is nonempty, the controller chronology has the required
Johnson/inclusion steps, and

\[
                         \bigcup_{p=i}^{i+3}P'_p=T'_i
                         \qquad(0\le i<6435).
\tag{4.6}
\]

Thus \(P'\) is one literal common word with \(D^3P'=T'\).  This certifies
the middle ownership and the upper tower.  It does not make \(P'\) a
universal lower word; the lower Hall/compiler selection remains separate.

## 5. The bounded Hall interface

Let the compiler depth be \(d\), and let a physical lower cell in row
\(r\in\{0,\ldots,d-1\}\) start at source position \(p\).  Its exact target
neighbourhood is determined by the middle owners in

\[
                         [p-2d,\ p+r+d].
\tag{5.1}
\]

Indeed, the maximal letter \(P_p\) uses owners in \([p-d,p]\).  An owner
whose carrier subset can enter the cell starts in \([p-d,p+r]\), and its
full carrier test uses owners from \(d\) positions before through \(d\)
positions after that start.

Consequently, under canonical translation/reflection, every cell whose
dependency interval (5.1) lies in one retained segment has an old/new mate
with the same target neighbourhood.  Near one cut, row \(r\) has at most

\[
                         3d+r
\tag{5.2}
\]

affected starts.  If \(t\) old cuts are replaced by \(t\) new seams, the
uncancelled old-plus-new right-profile mass is at most

\[
 2t\sum_{r=0}^{d-1}(3d+r)
 =t(7d^2-d).
\tag{5.3}
\]

For \(d=t=3\), this upper bound is \(180\).  In the named braid, cancellation
leaves exactly \(37\) lost and \(37\) gained right-neighbourhood instances.
Thus a global segment reorder induces a bounded seam-profile exchange in
the unlabelled Hall graph.

This locality is canonical, not absolute.  The RF move reverses 3130 owners
and moves another 1856.  Named old physical cells and the 1489 peeled
reservations are globally reindexed or reflected.  Any theorem retaining
those occurrences must transport and re-audit them; “only three seams
change” is false for fixed numerical addresses.

## 6. Exact Hall-current and matching descent theorems

Let \(G=(L,R,E)\) be a finite bipartite target/cell graph.  For
\(X\subseteq L\), define

\[
 \delta_G(X)=|X|-|N_G(X)|,\qquad
 h(G)=\max_{X\subseteq L}\delta_G(X)=|L|-\nu(G).
\tag{6.1}
\]

For a braid \(b\), canonically transport the unchanged right cells and
write \(G_b\) for the new graph.  Define

\[
 J_b(X)=|N_{G_b}(X)|-|N_G(X)|,
\qquad
 \sigma_G(X)=h(G)-\delta_G(X)\ge0.
\tag{6.2}
\]

### Theorem 6.1 (exact all-shore descent formula)

Put

\[
                         \mu_b=
 \min_{X\subseteq L}\bigl(\sigma_G(X)+J_b(X)\bigr).
\tag{6.3}
\]

Then

\[
                         \boxed{h(G_b)=h(G)-\mu_b.}
\tag{6.4}
\]

In particular, \(b\) lowers Hall deficiency by at least one if and only if

\[
 J_b(X)\ge1-\sigma_G(X)
 =\delta_G(X)-h(G)+1
 \qquad\text{for every }X\subseteq L.
\tag{6.5}
\]

Every old critical shore needs current at least one.  This is necessary but
not sufficient by itself: a shore of slack \(s\) may lose at most \(s-1\)
neighbours.

#### Proof

For every shore,

\[
 \delta_{G_b}(X)=\delta_G(X)-J_b(X)
 =h(G)-\bigl(\sigma_G(X)+J_b(X)\bigr).
\]

Taking the maximum over \(X\) gives (6.4); the integer condition
\(\mu_b\ge1\) is exactly (6.5).  \(\square\)

There is an equivalent profile form.  Let

\[
 p_G(U)=\#\{c\in R:\Gamma_G(c)=U\},
\qquad
 \Delta_b(U)=p_{G_b}(U)-p_G(U).
\tag{6.6}
\]

Then

\[
 J_b(X)=
 \sum_{U\subseteq L}\Delta_b(U)\,
 {\bf1}[U\cap X\ne\varnothing].
\tag{6.7}
\]

This is the exact floor-covariance/Shadow--Braid current of the segment
exchange.  It accounts for dependencies; the changed cells are not
independent signs.

### Theorem 6.2 (augmenting-path certificate)

Fix a maximum matching \(M\) of \(G\), let

\[
                         M_0=M\cap E(G_b),
\qquad r=|M|-|M_0|.
\tag{6.8}
\]

Then \(h(G_b)\le h(G)-1\) if and only if \(G_b\) contains \(r+1\)
pairwise vertex-disjoint \(M_0\)-augmenting paths.

#### Proof

The matching \(M_0\) has size \(\nu(G)-r\).  Simultaneous augmentation along
\(r+1\) disjoint paths gives a matching of size \(\nu(G)+1\).  Conversely,
the symmetric difference of \(M_0\) with any matching of size at least
\(\nu(G)+1\) has at least \(r+1\) vertex-disjoint components which are
augmenting paths for \(M_0\).  \(\square\)

For \(r=0\), this is one ordinary augmenting path.  A matching witness or
the path family is a self-contained positive certificate; a scalar matching
number alone is not.

## 7. The exact Hall-\(28\) exchange

For the unpeeled lower-target graph,

\[
\begin{array}{c|c|c}
 &\text{old}&\text{RF braid}\\ \hline
\text{targets}&16383&16383\\
\text{cells}&19311&19311\\
\text{candidate edges}&133534&133546\\
\text{maximum matching}&16354&16355\\
\text{deficiency}&29&28\\
\text{zero-candidate targets}&7&7.
\end{array}
\tag{7.1}
\]

The common zero set is

\[
             \{2575,5801,13616,13620,17738,21641,29776\}.
\tag{7.2}
\]

Target degrees change by \(-1\) for 79 targets, by \(+1\) for 83 targets,
and by \(+2\) for four targets; all other \(16217\) target degrees are
unchanged.  Thus the twelve-edge net gain is highly correlated.

Let \(S_0\) be the old canonical Dulmage--Mendelsohn shore.  Then

\[
                         |S_0|=1524,\qquad
                         |N_G(S_0)|=1495,
\tag{7.3}
\]

while

\[
                         |N_{G_b}(S_0)|=1496.
\tag{7.4}
\]

Hence

\[
                         J_b(S_0)=1.
\tag{7.5}
\]

Inside this shore, four old affected cells are replaced by five new affected
cells.  The decisive old depth-two cell at start 472 has full neighbourhood

\[
 \{6276,6277,6308,6309,6340,6341,6372,6373\}.
\tag{7.6}
\]

Its intersection with \(S_0\) is

\[
                         \{6308,6309,6372,6373\}.
\]

After the braid, the depth-one cell at start 3602 has neighbourhood

\[
 \{6148,6149,6180,6181,6276,6277,6308,6309\},
\tag{7.7}
\]

and the depth-two cell at the same start has neighbourhood

\[
 \{6212,6213,6244,6245,6340,6341,6372,6373\}.
\tag{7.8}
\]

Their intersections with \(S_0\) are the disjoint pairs

\[
                         \{6308,6309\},\qquad\{6372,6373\}.
\tag{7.9}
\]

Thus one four-target contention cell splits into two independent right
vertices.  The individual degrees of targets

\[
                         6308,6309,6372,6373
\]

remain respectively

\[
                         14,\quad4,\quad6,\quad1.
\tag{7.10}
\]

The improvement is a correlation/capacity gain, not an incidence-count
gain for these targets.

After the split, the new canonical DM shore has

\[
                         |S_1|=1489,\qquad |N_{G_b}(S_1)|=1461,
\tag{7.11}
\]

so its defect is \(28\).  This same shore already had defect \(28\) in the
old graph.  The braid removes the top defect-29 obstruction and exposes a
pre-existing next layer; it does not yet alter that layer.

The move is particularly unrelated to the previous singleton-\(6308\)
route:

\[
 \#\{p:P_p=6308\}=0=\#\{p:P'_p=6308\},
\tag{7.12}
\]

target \(6308\) has Hall degree \(14\) on both sides, and \(6308\) remains
one of the four missing canonical rank-five masks in (4.2).

On the old peeled 35-target residual interface, every raw target degree is
unchanged except target \(449\), which decreases from \(75\) to \(74\).
Therefore the Hall improvement is not a new UNIT pin or address in that
fixed 35-versus-6 architecture.  The reservations and their cell IDs have
been globally rethreaded and must be recomputed.

### Proposition 7.1 (explicit augmentation mechanism)

Under canonical profile transport, pair the \(19274\) old/new right cells
having identical full neighbourhoods.  Of the old matching edges incident
with the 37 lost-profile cells, 31 are used.  All 31 displaced targets have
distinct one-edge recovery matches among the new cells.  After those
repairs, the remaining augmentation is the alternating path

\[
 7844\longrightarrow c_{18305}\longleftarrow6820
 \longrightarrow c_{10947}\longleftarrow6308
 \longrightarrow c_{10040}.
\tag{7.13}
\]

The three right neighbourhoods are

\[
\begin{aligned}
 \Gamma(c_{18305})&=\{6788,6820,7812,7844\},\\
 \Gamma(c_{10947})&=\{4132,4260,4644,4772,6180,6308,6692,6820\},\\
 \Gamma(c_{10040})&=\{6148,6149,6180,6181,6276,6277,6308,6309\}.
\end{aligned}
\tag{7.14}
\]

The first two cells are transported copies of old cells \(15175\) and
\(7817\); the last has no old neighbourhood-profile counterpart.  Hence the
newly covered target is \(7844\), while \(6308\) is an already matched relay.
This is the concrete matching explanation of (7.1).

For audit completeness, the 31 direct recovery pairs
\(\text{target}\mapsto\text{new cell}\) are

\[
\begin{gathered}
12\mapsto694,\ 134\mapsto568,\ 175\mapsto11894,\ 197\mapsto3604,\ 
207\mapsto6912,\ 239\mapsto13348,\\
431\mapsto18330,\ 463\mapsto13349,\ 935\mapsto18329,\ 
2089\mapsto471,\ 2217\mapsto773,\\
3177\mapsto6908,\ 3241\mapsto8803,\ 3689\mapsto13344,\ 
3753\mapsto16474,\ 4143\mapsto11895,\\
4197\mapsto833,\ 4207\mapsto13347,\ 4269\mapsto7912,\ 
4325\mapsto10041,\ 6191\mapsto18332,\\
6241\mapsto6909,\ 6249\mapsto9242,\ 6253\mapsto13346,\ 
6313\mapsto8647,\ 6373\mapsto16477,\\
7273\mapsto13345,\ 7337\mapsto16475,\ 16613\mapsto8244,\ 
16615\mapsto16479,\ 20709\mapsto16478.
\end{gathered}
\tag{7.15}
\]

The current JSON stores the materialized path, move, and summary Hall
report, but no \(16355\)-edge matching, min-cut, or DM certificate.  The
numbers and augmentation above were independently recomputed and are valid;
the JSON alone is not yet a self-contained Hall certificate.

## 8. What would constitute a descent theorem

Every endpoint-valid segment braid is invertible.  The inverse of the named
move is

\[
                         \operatorname{FR}(471,3601,5456),
\tag{8.1}
\]

which takes the Hall-28 path back to the Hall-29 path.  Therefore the
admissible exchange graph is undirected whenever admissibility is tested at
both endpoints.  A downhill edge has an uphill inverse.  No argument using
only the number of resident/support-safe braids can orient all moves by a
strict Lyapunov function.

A positive-deficiency state is a strict braid-local minimum exactly when
for every admissible braid \(b\) there is some shore \(X_b\) with

\[
                         J_b(X_b)\le-\sigma_G(X_b),
\tag{8.2}
\]

equivalently \(\mu_b\le0\), equivalently the augmenting-path family of
Theorem 6.2 fails.  A local minimum need not be a component minimum because
a plateau or uphill escape may exist.  If the minimum deficiency on an
entire exchange component is positive, Hall zero is unreachable in that
component.

The supplied census numbers prove abundant resident and upper-support-safe
moves at the **initial** path.  Subsequent exact enumeration found the chain

\[
29\longrightarrow28\longrightarrow27\longrightarrow26\longrightarrow25
\]

and proved that Hall \(25\) is a strict one-move local minimum for the full
resident, upper-safe `FF/RF/FR/RR` three-cut catalogue.  Thus the formerly
missing \(28\to27\) step is no longer open, but the unrestricted expansion
statement is false for this move class.  Escaping Hall \(25\) requires at
least one of: four or more independently movable segments, a compound route
with a non-improving intermediate, a compensated deck-changing circuit, or
simultaneous carrier/pin motion.  The all-shore criterion (6.5) remains the
exact test for every proposed larger braid.

Even Hall zero would remain the SDR gate.  The exact finite word still needs
one simultaneous selection of all lower occurrences inside a common
physical word \(A\) with \(D^3A=T\), together with the transported 1489
reservations, trace-two/owner conditions, and endpoint deadlines.  The
present move certifies the middle/upper word \(P'\), not that final lower
selection.

## 9. Artifact provenance and precise scope

The audited files are

- scratch/k15_segment_braid_hall28.json
- scratch/search_k15_segment_braid_native.cpp

The JSON SHA-256 is

\[
\mathtt{a11aaa927367dc70cf57e4e550c1b7d0a81e480c2c3801a45381795851c4c283}.
\tag{9.1}
\]

The native source changed concurrently during this audit, so no source hash
is declared authoritative here.  The named-path calculations use the JSON
and are unaffected.

The source predicate preserves_upper checks expected-rank support, not deep
multiset equality.  Its lower_holes predicate checks \(q=1\) only.  Its
resident predicate checks short positive runs, not full trace-rainbow.  The
source prints improving moves but does not itself write the JSON.  A
canonical final artifact should add the census manifest and a
self-contained matching/min-cut or augmenting-path certificate.
