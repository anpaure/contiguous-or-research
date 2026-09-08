# The three-direction pair-frame tensor: exact cubical partitions and the common-order window obstruction

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let

\[
 A=\{a,b,c,d\},\qquad
 \mathcal R=\{uw,ux,vw,vx\},
\]

and

\[
 \mathcal V=\{X\cup Y:X\in\tbinom A2,\ Y\in\mathcal R\}.
\tag{0.1}
\]

The observed local decomposition is exact.  The graph on the special
two-sets is the octahedral graph \(J(4,2)\), and every perfect matching of
that graph, multiplied by the reservoir square \(Q_2\), partitions
\(\mathcal V\) into three induced \(Q_3\)'s.  There are exactly eight such
partitions.  Two disjoint special matchings give a genuine
three-\(Q_3\)-versus-three-\(Q_3\) associator whose cell-ownership graph is
a \(6\)-cycle.

Tensoring \(r\) blocks gives exactly

\[
                         3^r\text{ disjoint }Q_{3r}\text{ cells}
\tag{0.2}
\]

on the common support \(\mathcal V^r\), of total size \(24^r\).

This vertex/cell theorem does **not** remove the fine consecutive-window
obstruction for the linear-translate Hamming resolution.  In one product
cell, consider the fine depth-\(q\) direction profiles which choose one of
the three local directions in each of \(q\) distinct blocks.  Their exact
number is

\[
                         N_{r,q}=3^q\binom rq.             \tag{0.3}
\]

A common-order isometric-cycle layer exposes at most \(h\) of them, where
\(h\) is the active cube dimension.  Consequently a library of \(K\)
common-order layers leaves at least the fraction

\[
             \boxed{\left(1-\frac{Kh}{3^q\binom rq}\right)_+}       \tag{0.4}
\]

of any sectorwise uniform fine-profile quota unsupported.  In particular,
even granting all \(h/2\) classes of one resolvable edge decomposition
leaves at least

\[
             \boxed{\left(1-\frac{h^2}{2\,3^q\binom rq}\right)_+}. \tag{0.5}
\]

There is a stronger labelled owner-lock theorem, proved in Section 9.
Allow an arbitrary vertex-disjoint mosaic of the tensor support by literal
product \(Q_{3r}\) cells, and then choose an arbitrary Hamming direction
order and phase separately in every cell.  For the explicit target family

\[
                 |\mathcal T_{r,q}|=\binom rq16^q24^{r-q},          \tag{0.5a}
\]

the reachable fraction is at most

\[
 \boxed{
       \rho_{r,q}=\left(\frac34\right)^q
                     \frac{r-q+1}{\binom rq}.}                     \tag{0.5b}
\]

The key is that every compatible labelled target has a unique carrier
product cell.  Hence even state-adaptive raw associator mosaics cannot pool
the exponentially many cell orders.  A switch among \(K\) whole-cycle
parent catalogues reaches at most \(K\rho_{r,q}\), and therefore needs

\[
 K\ge(1-o(1))\left(\frac43\right)^q
                  \frac{\binom rq}{r-q+1}                           \tag{0.5c}
\]

to cover almost all of this fine family.

The direct cell \(Q_{3r}\) cannot itself be partitioned into full-dimensional
isometric \(C_{6r}\)'s: \(6r\nmid2^{3r}\).  This arithmetic defect is
repairable, for example by one global spectator when
\(3r+1=4^t\), or by one spectator per block when \(r\) is a power of two.
After either repair, \(h\le4r\), so (0.4)--(0.5) remain exponentially
sharp.

For \(q=A\sqrt m+O(1)\) and \(q=o(r)\), the number of independent order
layers required even at the unlabelled direction level satisfies

\[
 \log K\ge
 q\log\frac{3er}{q}
   -O\!\left(\frac{q^2}{r}+\log r\right).               \tag{0.6}
\]

Thus boundedly many local shores, polynomially many conjugates, and even
one complete Hamming edge resolution miss a \(1-o(1)\) fraction of the
fine profiles.  Three directions improve the local cubical dimension;
they do not replace the exponentially large order atlas.

There is one important boundary.  The full tensor library contains
exponentially many *alternative* product partitions.  When \(q=o(r)\), its
cardinality is numerically large enough to pass (0.6).  But all those
partitions cover the same middle vertices; using them simultaneously
duplicates ownership.  Therefore the exact remaining escape is an
owner-disjoint, state-adaptive selector which chooses exponentially many
orders across different physical cells while retaining one occurrence of
each middle owner and balancing labelled affine faces.  The local
three-\(Q_3\) partition by itself proves no such selector.

## 1. The local graph is \(J(4,2)\square Q_2\)

Join two members of \(\mathcal V\) when one is obtained from the other by
exchanging the selected endpoint of one coordinate pair.  On the first
four coordinates, two special sets \(X,X'\in\binom A2\) are adjacent
exactly when \(|X\cap X'|=1\).  This is the Johnson graph \(J(4,2)\).
Its three nonedges are the complementary pairs

\[
             ab\mid cd,\qquad ac\mid bd,\qquad ad\mid bc.          \tag{1.1}
\]

Thus \(J(4,2)=K_{2,2,2}\), the octahedral graph.  The reservoir
orientations form the square

\[
                         uw, vw, vx, ux,                           \tag{1.2}
\]

and the induced graph on \(\mathcal V\) is

\[
                         J(4,2)\square Q_2.                           \tag{1.3}
\]

Let \(M\) be a perfect matching of \(J(4,2)\).  For each
\(e=\{X,X'\}\in M\), the eight vertices

\[
                         e\times\mathcal R                           \tag{1.4}
\]

induce \(Q_1\square Q_2=Q_3\).  The three matching edges have disjoint
endpoints and exhaust the six special states, so the three cubes (1.4)
partition all \(24\) members of \(\mathcal V\).

This is a vertex partition, not an edge decomposition of the full local
graph.  The three cubes contain all \(24\) reservoir edges, but only the
\(12\) special edges above the chosen matching; the full product graph has
\(72\) edges.

## 2. All eight partitions and the exact alternative overlap

Put

\[
 P_0=(ab,cd),\qquad P_1=(ac,bd),\qquad P_2=(ad,bc),                 \tag{2.1}
\]

and label the two vertices in each \(P_i\) by bits.  Every perfect
matching of \(K_{2,2,2}\) has one edge between each pair of parts.
After choosing its \(P_0P_1\) edge, there are two ways to join the four
remaining vertices.  Hence there are

\[
                         2\cdot2\cdot2=8                              \tag{2.2}
\]

perfect matchings, and therefore eight local three-\(Q_3\) partitions.

Two explicit disjoint matchings are

\[
 M_0=\{ab\!-!ac,\ ad\!-!bd,\ bc\!-!cd\},                       \tag{2.3}
\]

\[
 M_1=\{ab\!-!ad,\ ac\!-!bc,\ bd\!-!cd\}.                       \tag{2.4}
\]

The cell-incidence edges, labelled by their common special state, are

\[
\begin{array}{lll}
 (ab-ac)(ab-ad)&[ab],& (ab-ac)(ac-bc)\ [ac],\\
 (ad-bd)(ab-ad)&[ad],& (ad-bd)(bd-cd)\ [bd],\\
 (bc-cd)(ac-bc)&[bc],& (bc-cd)(bd-cd)\ [cd].
\end{array}                                                         \tag{2.5}
\]

They form a \(6\)-cycle.  Each incidence in (2.5) represents the four
common reservoir orientations, namely a full \(Q_2\).  Thus (2.3)--(2.4)
are two exact partitions of the same \(24\)-set support, and their
ownership overlap is connected.

More generally, two distinct perfect matchings either share one edge or
are disjoint.  In the first case the overlap has one identical \(Q_3\)
component and one four-cell alternating component.  In the second case
the union of the matchings is a \(6\)-cycle, giving the connected overlap
above.  For each matching, three of the other seven matchings share one
edge and four are disjoint: each of its three edges belongs to exactly two
of the eight perfect matchings.  Hence the eight partitions have exactly
\(8\cdot4/2=16\) unordered connected associator pairs and
\(8\cdot3/2=12\) unordered shared-cell pairs.  By symmetry, exactly two
matchings omit each one of the four possible singleton intersection
labels.

### Proposition 2.1 (exact tensor overlap components)

Let two product partitions use the same local matching in \(r-s\) blocks
and disjoint local matchings in the remaining \(s\) blocks.  Their raw
product-cell ownership overlap has exactly

\[
                         3^{r-s}                                    \tag{2.6}
\]

connected components.  In particular, if all \(r\) blocks are changed,
the overlap is connected and the component switch has only its two whole
tensor shores.

#### Proof

For two disjoint local matchings, label their three cells so that the
cell-incidence matrix is

\[
                         B=J_3-I_3.                                 \tag{2.7}
\]

Indeed, the incidence graph is the \(6\)-cycle
\(K_{3,3}\setminus M_3\).  Moreover

\[
                         BB^{\mathsf T}=J_3+I_3,                    \tag{2.8}
\]

whose entries are all positive.  For \(s\) changed blocks, the
biadjacency matrix is a tensor product of \(s\) matrices of the form
\(B\), and its two-step left-to-left matrix is a tensor product of
strictly positive matrices (2.8).  Hence that changed-block overlap is
connected.

An unchanged block contributes the identity incidence matrix \(I_3\), so
its common cell label cannot change along an overlap path.  The
\(r-s\) unchanged labels give \(3^{r-s}\) sectors, and the preceding
argument makes each sector connected.  This proves (2.6). \(\square\)

Thus a one-block associator switch inside an \(r\)-block tensor has
\(3^{r-1}\) independently selectable raw components, indexed by the
other cell labels.  Selecting shores separately in those components
produces a hybrid product-cell tiling.  Proposition 2.1 also shows why
switching every block at once gives no such independence.

## 3. What the local directions delete

Fix a cell \(\{X,X'\}\times Q_2\) and a vertex \(X\cup Y\) in it.  Its
three cube directions are:

1. the special exchange \(X\leftrightarrow X'\);
2. the reservoir exchange \(u\leftrightarrow v\);
3. the reservoir exchange \(w\leftrightarrow x\).

On a lower edge, the special exchange deletes the unique point of
\(X\setminus X'\); it cannot delete the fixed point in \(X\cap X'\).
The two reservoir directions delete the two selected reservoir points.
Consequently one chosen \(Q_3\) cell exposes exactly three of the four
possible one-coordinate deletions from each of its vertices.

For a prescribed set of \(q\) distinct blocks, one fixed product cell
therefore exposes at most \(3^q\) of the \(4^q\) coordinate-deletion
patterns.  A bounded library of \(B\) product partitions exposes at most
the fraction

\[
                         \min\{1,B(3/4)^q\}.                         \tag{3.1}
\]

At \(q=A\sqrt m+O(1)\), (3.1) tends to zero exponentially for every
fixed \(B\).  This loss occurs before imposing consecutiveness.

Two associator shores do not universally expose both special deletions.
There is a useful exact parity explanation.  Identify a vertex of
\(J(4,2)\) with an edge of \(K_4\).  If two disjoint perfect matchings
form their alternating \(6\)-cycle, call a \(K_4\)-edge bad when its two
cycle neighbours meet it at the same endpoint.  At a bad special state,
the two shores delete the same selected special point.

Let \(B\subseteq E(K_4)\) be the set of bad edges.  The good edges, read
around the alternating cycle, form a closed trail using each good edge
once.  Hence every vertex has even degree in \(K_4-B\).  Since every
degree in \(K_4\) is three, every vertex has odd degree in \(B\).  In
particular

\[
                         |B|\ge2.                                   \tag{3.2}
\]

Thus at least two of the six special states, hence at least eight of the
twenty-four local owners, see no new lower-deletion direction under a
two-shore connected associator.

This local defect can be removed by a larger local atlas.  The four
matchings

\[
\begin{aligned}
 &\{ab-ac,\ ad-bd,\ bc-cd\},\\
 &\{ab-bd,\ cd-ad,\ ac-bc\},\\
 &\{cd-ac,\ ab-ad,\ bd-bc\},\\
 &\{cd-bd,\ ab-bc,\ ac-ad\}
\end{aligned}                                                       \tag{3.3}
\]

are pairwise edge-disjoint and partition the twelve edges of
\(J(4,2)\).  Any three of them expose three of the four special neighbours
at every special state.  Of the four neighbours of a two-set \(X\), two
delete each one of the two points of \(X\).  Hence any three matchings in
(3.3) expose both possible special deletions at every owner.  This proves
that (3.1) is a one-partition or bounded-global-library obstruction, not a
local state-space invariant.

## 4. Tensoring the cell partitions

Choose one perfect matching \(M_i\) in each of \(r\) disjoint local
blocks.  Choosing one of its three matching edges in every block gives
\(3^r\) product cells.  Each is

\[
                Q_3\square\cdots\square Q_3=Q_{3r},                 \tag{4.1}
\]

has \(2^{3r}=8^r\) vertices, and the cells partition

\[
                         |\mathcal V^r|=24^r=3^r8^r.                \tag{4.2}
\]

Replacing any \(M_i\) by an alternative perfect matching gives another
partition of exactly the same vertex support.  It does not add a fourth
direction to a cell of the chosen partition, and it does not give a second
occurrence of a vertex unless one actually superposes two alternative
partitions.

There is also an unavoidable arithmetic mismatch in the direct tensor.
A vertex partition of \(Q_{3r}\) into full-dimensional isometric
\(C_{6r}\)'s would contain

\[
                         \frac{2^{3r}}{6r}                           \tag{4.3}
\]

cycles.  This is never an integer because its denominator has a factor
three.  Equivalently, a full-dimensional \(C_{2h}\)-resolution of \(Q_h\)
requires \(h\) to be a power of two, whereas \(h=3r\) never is.

The mismatch is not a deep obstruction.  If

\[
                         r=\frac{4^t-1}{3},                          \tag{4.4}
\]

one global spectator direction makes \(h=3r+1=4^t\), a power of two.
Alternatively, one spectator in every block gives cells \(Q_{4r}\), and
\(h=4r\) is a power of two whenever \(r\) is.  These repairs preserve the
three original local directions and have \(h\le4r\).

## 5. Exact fine-profile count

In a fixed product cell, label its three local directions in block \(i\)
by

\[
                         (i,1),(i,2),(i,3).                          \tag{5.1}
\]

For \(1\le q\le r\), let \(\mathscr D_{r,q}\) be the family of direction
sets which choose one label in each of \(q\) distinct blocks:

\[
 \mathscr D_{r,q}=
 \left\{\{(i,\alpha_i):i\in J\}:
 J\in\tbinom{[r]}q,\ \alpha_i\in[3]\right\}.                       \tag{5.2}
\]

The parametrization in (5.2) is unique, so

\[
                         |\mathscr D_{r,q}|=3^q\binom rq.           \tag{5.3}
\]

These are only a subfamily of the \(\binom{3r}{q}\) possible direction
sets.  They are precisely the fine refinement of the coarse profiles that
touch \(q\) blocks once each.

## 6. Common-order interval theorem

Every isometric \(C_{2h}\) in \(Q_h\) has transition word

\[
                         \sigma\sigma                               \tag{6.1}
\]

for a cyclic order \(\sigma\) of the \(h\) directions.  For
\(1\le q<h\), its consecutive \(q\)-direction sets are exactly the
\(h\) cyclic \(q\)-intervals of \(\sigma\); the second half merely repeats
them.

Call a cycle layer common-order if all of its components use the same
\(\sigma\), up to cyclic phase and reversal.  The linear-kernel translate
resolution has exactly this property.

### Theorem 6.1 (fine-profile support bound)

Let \(K\) common-order layers be placed on one tensor sector, in an active
cube of dimension \(h\ge3r\) obtained by adjoining spectators if needed.
Then their union supports at most \(Kh\) members of
\(\mathscr D_{r,q}\).  If a desired sectorwise measure has total mass
\(S\) and assigns mass \(S/N_{r,q}\) to every fine profile, the unsupported
desired mass is at least

\[
                 S\left(1-\frac{Kh}{N_{r,q}}\right)_+.              \tag{6.2}
\]

#### Proof

One cyclic order has exactly \(h\) cyclic \(q\)-intervals, so it supports
at most \(h\) members of the subfamily \(\mathscr D_{r,q}\).  The union
of \(K\) orders therefore supports at most \(Kh\) profiles.  Every one of
the remaining \(N_{r,q}-Kh\) profiles has desired mass
\(S/N_{r,q}\) and receives zero.  Summing those deficits proves (6.2).
\(\square\)

A resolvable edge decomposition of \(Q_h\) has \(h/2\) resolution
classes.  Even if one grants a different direction order to every class,
Theorem 6.1 with \(K=h/2\) gives (0.5).  In the explicit linear-translate
construction the classes actually share one direction order, so the
stronger \(K=1\) bound applies.  Notice also that using all \(h/2\)
classes repeats every vertex \(h/2\) times; it is already more generous
than a coefficient-one vertex-factor selection.

For the spectator repairs in Section 4, \(h\le4r\).  Hence one layer
misses at least

\[
                  \left(1-\frac{4r}{3^q\binom rq}\right)_+,       \tag{6.3}
\]

and a whole edge resolution misses at least

\[
                  \left(1-\frac{8r^2}{3^q\binom rq}\right)_+.      \tag{6.4}
\]

Both tend to one exponentially fast on the Gaussian window.

## 7. Exact asymptotic accounting

For \(q=o(r)\), Stirling's formula and the falling-factorial expansion give

\[
 \log\binom rq
 =q\log\frac rq+q
   +O\!\left(\frac{q^2}{r}+\log(q+1)\right).                        \tag{7.1}
\]

Combining (5.3) and (7.1),

\[
 \log N_{r,q}
 =q\log\frac{3er}{q}
   +O\!\left(\frac{q^2}{r}+\log(q+1)\right).                        \tag{7.2}
\]

Thus Theorem 6.1 forces

\[
 \log K
 \ge q\log\frac{3er}{q}
   -\log h
   -O\!\left(\frac{q^2}{r}+\log(q+1)\right)                        \tag{7.3}
\]

whenever the unsupported fraction is to tend to zero.  Since \(h\le4r\),
this is (0.6).

At

\[
                         q=A\sqrt m+O(1),\qquad q=o(r),              \tag{7.4}
\]

equation (7.3) becomes

\[
 \log K
 \ge A\sqrt m\log\frac{3er}{A\sqrt m}
   -O_A\!\left(\frac mr+\log m\right).                             \tag{7.5}
\]

In particular, if \(K=m^{O(1)}\), the supported fraction in (6.2) is

\[
 \exp\left\{-A\sqrt m\log\frac{3er}{A\sqrt m}
       +O_A\!\left(\frac mr+\log m\right)\right\}=o(1).            \tag{7.6}
\]

If instead \(q/r\to\alpha\in(0,1]\), the entropy form is

\[
 \log N_{r,q}
 =r\bigl(H(\alpha)+\alpha\log3\bigr)+O(\log r),                   \tag{7.7}
\]

so the required library is still exponential in \(r=\Theta(\sqrt m)\).
The factor \(3^q\) means that even at \(q=r\), where there is only one
coarse block set, there remain \(3^r\) fine profiles.

## 8. Sharp boundary and next exact statement

The theorem rules out the following direct inference:

\[
 \text{three local cube directions}
 \quad\Longrightarrow\quad
 \text{fine Gaussian consecutive-window balance}.                 \tag{8.1}
\]

A cell partition says where vertices live.  Consecutive-window balance
asks for an exponentially large catalogue of ordered direction intervals.
Equations (6.2)--(7.5) quantify the missing catalogue exactly.

The result does not rule out a genuinely state-adaptive tensor atlas.
Indeed, three independently selectable local partitions already give
\(3^r\) formal tensor corners, and for \(q=o(r)\)

\[
 q\log(r/q)=o(r),                                                   \tag{8.2}
\]

so \(3^r\) is numerically larger than the lower bound in (7.3).  The
counting obstruction therefore ends precisely here.  Those corners are
alternative partitions of the same \(24^r\) owners, not disjoint source
copies.  A coefficient-one use of their order catalogue requires a new
theorem with all of the following simultaneous conclusions:

1. every middle owner is assigned to exactly one selected product cell and
   one cycle;
2. the selected cell orders collectively realize the required fine
   \(q\)-profiles;
3. the resulting affine lower and upper faces, not merely their direction
   labels, meet the floor/ceiling quotas;
4. the assignment uses no replicated ownership and has the required small
   row-run boundary.

That owner-disjoint ordered-face selector is the exact constructive lemma
left after the local \(Q_3\) theorem.  Neither the existence of eight
local partitions nor their formal tensor product proves it.

## 9. Stronger owner lock for arbitrary hybrid product-cell tilings

The preceding common-order count can be strengthened in the actual
labelled tensor sector.  The strengthening also closes a possible loophole
in Section 8: choosing different local matchings in different cells does
not help as long as the cells remain literal products of the local
\(Q_3\)'s.

Call a **hybrid product-cell tiling** any vertex partition of
\(\mathcal V^r\) into cells

\[
             C=\prod_{i=1}^r(e_i(C)\times Q_{2,i}),                 \tag{9.1}
\]

where each \(e_i(C)\) is an arbitrary edge of \(J(4,2)\).  There is no
requirement that the edges \(e_i(C)\), as \(C\) varies, come from one
fixed perfect matching in block \(i\).  Since every cell has \(8^r\)
vertices, every such tiling has exactly

\[
                         24^r/8^r=3^r                               \tag{9.2}
\]

cells.

For \(1\le q\le r\), define a labelled lower-target family
\(\mathcal T_{r,q}\).  Choose \(I\in\binom{[r]}q\).  In a touched block
\(i\in I\), choose

\[
 T_i=\{z_i\}\cup Y_i,qquad
 z_i\in\{a_i,b_i,c_i,d_i\},\quad Y_i\in\mathcal R_i,                \tag{9.3}
\]

giving sixteen choices.  In an untouched block choose any
\(T_i\in\mathcal V_i\), giving twenty-four choices.  Thus

\[
                 |\mathcal T_{r,q}|=\binom rq16^q24^{r-q}.          \tag{9.4}
\]

### Theorem 9.1 (hybrid-cell owner lock)

Fix an arbitrary hybrid product-cell tiling.  Assign an arbitrary cyclic
direction order and an arbitrary linear-translate resolution phase to
each cell, independently between cells.  Then at most

\[
                         3^r(r-q+1)4^q8^{r-q}                       \tag{9.5}
\]

members of \(\mathcal T_{r,q}\) can be lower faces of consecutive
length-\(q\) windows.  Consequently their reachable fraction is at most

\[
 \boxed{
       \left(\frac34\right)^q
       \frac{r-q+1}{\binom rq}.}                                   \tag{9.6}
\]

The same bound holds after adjoining any spectator axes.

#### Proof

The local cardinality of a depth window decreases by the number of local
cube axes used.  A target in (9.3) has local size three in blocks of
\(I\) and local size four elsewhere.  Hence a carrying window must use
exactly one axis in every block of \(I\), no axis outside \(I\), and no
spectator axis.  A reservoir axis leaves two special coordinates and one
reservoir coordinate, whereas (9.3) has one special and two reservoir
coordinates.  Thus every used axis is the special axis of its local
\(Q_3\).

Such a target has at most one carrier cell.  Indeed, in an untouched
block any carrier cell must contain the prescribed special two-set.  In a
touched block its special edge must have intersection label \(z_i\).
Any two edges of \(J(4,2)\) with the same singleton intersection
\(z_i\) share a special two-set: they are two edges of the triangle on
the three two-sets containing \(z_i\).  Therefore two putative carrier
product cells share a local vertex in every block, and hence share a
middle vertex globally.  This contradicts vertex-disjointness of the
tiling.

Now fix one cell.  Its cyclic order contains \(r\) special axes and at
least \(2r\) nonspecial reservoir axes.  If the cyclic runs of special
axes have lengths \(\ell_1,\ldots,\ell_t\), the number of all-special
length-\(q\) intervals is

\[
               \sum_j(\ell_j-q+1)_+\le r-q+1.                       \tag{9.7}
\]

For a fixed supported touched set \(I\), a target carried by this cell
has four choices of reservoir orientation in every touched block and
eight choices of cell vertex in every untouched block.  Hence there are
at most

\[
                         4^q8^{r-q}                                 \tag{9.8}
\]

such targets.  Carrier uniqueness makes the counts from distinct cells
disjoint.  Multiplying (9.7)--(9.8) by the \(3^r\) cells proves (9.5).
Dividing by (9.4) gives

\[
 \frac{3^r(r-q+1)4^q8^{r-q}}
      {\binom rq16^q24^{r-q}}
 =\left(\frac34\right)^q\frac{r-q+1}{\binom rq},
\]

which is (9.6).  Spectator directions cannot occur in a window with the
fixed local rank profile (9.3), so adjoining them changes nothing.
\(\square\)

### Corollary 9.2 (exact corner multiplicity threshold)

Even if \(K\) different hybrid tilings are supplied, each with arbitrary
cellwise orders and phases, covering a \((1-\epsilon)\)-fraction of
\(\mathcal T_{r,q}\) requires

\[
 \boxed{
 K\ge(1-\epsilon)
       \left(\frac43\right)^q
       \frac{\binom rq}{r-q+1}.}                                   \tag{9.9}
\]

For \(q=o(r)\),

\[
 \log K\ge
 q\log\frac rq+\bigl(1+\log(4/3)\bigr)q
 -O\!\left(\frac{q^2}{r}+\log r\right).                           \tag{9.10}
\]

At \(q=A\sqrt m+O(1)\), this is exponential in \(\sqrt m\) when
\(r=\Theta(\sqrt m)\), and is
\(\exp((1+o(1))q\log(r/q))\) when \(q=o(r)\).

Theorem 9.1 is a sharper boundary than the abstract direction count: it
already permits a different order in every one of the \(3^r\) cells and
every componentwise mosaic which is still a vertex-disjoint tiling by the
product boxes (9.1), including the raw children quantified in Proposition
2.1.  It does **not** cover a post-Hamming component child whose selected
long cycles no longer regroup into product boxes.  A surviving bypass must
therefore use such a genuinely non-box cycle mixture whose fine target has
several physical carrier cells, or route the target from a different
middle macrosector.  Merely selecting raw local associator components
cannot do so.

There is nevertheless a complete bound for an ordinary two-shore
post-Hamming component switch.

### Proposition 9.3 (whole-cycle switches inherit the parent catalogue)

Let \(F_1,\ldots,F_K\) be long-cycle factors, each obtained from an
admissible product-box tiling with arbitrary cellwise orders and phases.
Suppose a child \(F_*\) is formed by selecting whole cycles from the union
of these parent factors; in particular this includes every ordinary
ownership-component switch between two factors.  Then

\[
 \operatorname{Reach}_q(F_*)cap\mathcal T_{r,q}
 \subseteq
 \bigcup_{j=1}^K
   \bigl(\operatorname{Reach}_q(F_j)\cap\mathcal T_{r,q}\bigr).      \tag{9.11}
\]

Consequently the reachable fraction of \(F_*\) is at most

\[
 K\left(\frac34\right)^q
       \frac{r-q+1}{\binom rq}.                                    \tag{9.12}
\]

For a pairwise associator switch, \(K=2\).

#### Proof

Every cycle of \(F_*\) is literally a cycle of one of the parents.  Every
consecutive window internal to that cycle, including its physical lower
target, is therefore a window of the same parent.  This proves (9.11).
Apply Theorem 9.1 to each parent and use the union bound to obtain (9.12).
\(\square\)

Thus refinement of the cycle-ownership overlap may destroy the box
grouping, but it gives no new window words.  To escape (9.12), a procedure
must either use exponentially many genuinely different parent catalogues,
as quantified by (9.9), or splice/recombine cycles so that new windows cross
new seams.  The latter is no longer an associator component selection and
requires its own exact seam and recurrence-gap audit.
