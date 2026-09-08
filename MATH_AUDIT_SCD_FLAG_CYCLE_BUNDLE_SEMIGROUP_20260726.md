# Exact SCD flags versus whole-cycle bundles: hypergraph, dual, lattice, and the surviving gate

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Fix the exact two-sided nested flags supplied by the SCD--Hoffman theorem.
There is an exact cycle-bundle hypergraph whose matchings are precisely the
ways of grouping those owner-rooted flags into legal isometric cycles.  Its
owner-incidence semigroup is the correct integral object.  The SCD target rows
are redundant: because the SCD assigns every target to a unique middle owner,
covering an owner automatically covers all target tokens on its flag.

The fractional problem has a clean signed LP dual, and every lattice
congruence has a clean complete description through the Smith lattice (or,
equivalently, its character annihilator).  The visible congruences include:

* total and carrier-component divisibility by the cycle length (2h);
* checkerboard balance in every cube carrier;
* divisibility by (h) of every physical coordinate-star total;
* even antipodal contributions to every shallow profile-flow cell; and
* any frame-, packet-, or sector-total divisibility forced by the allowed
  catalogue.

The global total and all coordinate-star congruences can be repaired
simultaneously by deleting fewer than (2h) owners: delete a suitable number
of complementary middle-set pairs.  The previously counted frame/profile
congruences also cost (o(W)).  This does **not** prove that all Smith
congruences are cheap; controlling the full lattice quotient is part of the
remaining theorem.

There is a more immediate structural issue.  Once one successful frame state
is frozen at every owner, its first lower flag fixes its successor.  Higher
flags impose a de Bruijn overlap of length (H-1) on consecutive owners.  The
compatible-cycle hypergraph then degenerates to the good (2h)-orbits of a
functional digraph.  Fractional saturation is integral in that frozen model,
but it covers exactly the vertices already lying on good orbits; there is no
rounding mechanism that creates new ones.

Thus the exact SCD flags solve integral nesting but not cyclic coherence.  The
remaining statement is not ordinary semigroup rounding: one must choose the
successful frame states *jointly* so that their overlap digraph has an
almost-spanning (C_{2h})-factor.  The known determinant-two minor forbids a
blanket TU assertion when several cycle choices are retained.  No approximate
saturation proof is obtained here.

One positive projection survives.  If upper flags, higher depths, and cycle
closure are temporarily forgotten, the depth-one SCD lower targets admit a
collision-free assignment of distinct successor owners by Hall's theorem.
Hence the first obstruction is not simple successor indegree; it is the
simultaneous upper/higher-depth overlap and exact (2h)-cycle closure.

## 1. Flag data and allowed decorated cycles

Let

\[
 \Omega=\binom{[2m]}m,
 \qquad W=|\Omega|.                                                \tag{1.1}
\]

Fix a symmetric-chain decomposition.  For every owner (X), let

\[
 \mathfrak f_X=
 \big((L^-_{X,q})_{q\le r_X},(L^+_{X,q})_{q\le r_X}\big),
 \qquad r_X\le H,                                                  \tag{1.2}
\]

be its exact lower and upper truncated flags.  The SCD property says that,
at every depth and sign, the defined targets (L^pm_{X,q}) are pairwise
distinct as (X) varies and exhaust the corresponding Boolean rank.

Let \(\mathcal S_X\) be the set of successful local states available to
owner (X).  A state records a pair frame, the literal pair directions of
the two flags, and any packet/cell data required by the local construction.
The flag theorem proves \(\mathcal S_X\ne\varnothing\); it does not choose
the states coherently between owners.

An **allowed decorated bundle** is a tuple

\[
 B=(X_0,s_0;X_1,s_1;\ldots;X_{2h-1},s_{2h-1})                    \tag{1.3}
\]

such that:

1. the (X_i)'s are distinct middle owners;
2. (X_0X_1\cdots X_{2h-1}X_0) is an allowed isometric (C_{2h});
3. its transition word is \(\sigma\sigma\) for a permutation of its
   (h) active pair directions;
4. the state (s_i\in\mathcal S_{X_i}) is compatible with the common
   active pair system; and
5. every required forward/backward cycle window at (X_i) equals the
   corresponding target in \(\mathfrak f_{X_i}\).

This definition deliberately absorbs all local geometry into the edge
catalogue.  Let \(\mathscr B\) be the finite set of allowed decorated bundles
and put

\[
 A_{X,B}=\mathbf1_{\{X\in B\}},
 \qquad A\in\{0,1\}^{\Omega\times\mathscr B}.                     \tag{1.4}
\]

Every column has exactly (2h) ones.

### Theorem 1.1 (exact cycle-bundle hypergraph)

The integral solutions of

\[
                         Ax=\mathbf1_\Omega,
 \qquad x\in\mathbb Z_{\ge0}^{\mathscr B}                         \tag{1.5}
\]

are in bijection with exact owner-disjoint (C_{2h})-factors which realize
all fixed SCD flags.

More generally, for (L\subseteq\Omega), the solutions of

\[
                         Ax=\mathbf1_{\Omega\setminus L}           \tag{1.6}
\]

are precisely the compatible cycle packings leaving exactly the owners in
(L).

#### Proof

An owner row in (1.5) makes two selected bundle columns containing the same
owner impossible.  Thus an integral solution selects pairwise owner-disjoint
bundles and covers every owner once.  Conversely, the incidence vector of
such a factor satisfies (1.5).  The same argument proves (1.6). \(\square\)

### Lemma 1.2 (the SCD target rows are redundant)

For every depth and sign there is a (0)-(1) matrix (D_q^\pm), with at
most one nonzero entry in every row and column, such that the target census of
a selected owner vector (b\in\{0,1\}^\Omega) is exactly

\[
                              D_q^\pm b.                            \tag{1.7}
\]

In particular, appending the fixed SCD target rows to (A) neither changes
its integer points nor creates an additional rounding problem.

#### Proof

At fixed (q,\pm), an owner with (r_X\ge q) is assigned exactly one target,
and the SCD assigns every target to exactly one owner.  This incidence is the
partial permutation matrix (D_q^\pm). \(\square\)

If (L) owners are discarded, the aggregate two-sided target loss through
depth (H) is at most

\[
                              2H|L|.                               \tag{1.8}
\]

Therefore (|L|=o(W)) suffices at each fixed depth, but the full summed
constant-one ledger requires the stronger (|L|=o(W/H)).

## 2. Semigroup and exact LP duals

Put

\[
 \mathsf S(A)=A\mathbb Z_{\ge0}^{\mathscr B},
 \qquad
 \mathsf C(A)=A\mathbb R_{\ge0}^{\mathscr B},
 \qquad
 \Lambda(A)=A\mathbb Z^{\mathscr B}.                              \tag{2.1}
\]

The three objects have different roles:

* \(b\in\mathsf C(A)\) is fractional feasibility;
* \(b\in\Lambda(A)\) is the complete collection of linear and congruence
  necessities; and
* \(b\in\mathsf S(A)\) is an actual integral cycle packing.

Neither of the first two implies the third in a nonnormal semigroup.

### Proposition 2.1 (Farkas dual for fractional exact bundling)

For a real right-hand side (b),

\[
 b\in\mathsf C(A)
 \quad\Longleftrightarrow\quad
 \langle y,b\rangle\ge0
 \quad\hbox{for every }y\in\mathbb R^\Omega
 \hbox{ with }A^Ty\ge0.                                          \tag{2.2}
\]

Thus a signed owner weighting is a fractional obstruction precisely when
every allowed cycle has nonnegative total weight but the desired owner vector
has negative total weight.

### Proposition 2.2 (dual of the fractional leave)

Define

\[
 \ell_{\mathbb R}=
 \min\left\{\sum_Xz_X:Ax+z=\mathbf1, x,z\ge0\right\}.            \tag{2.3}
\]

Then

\[
 \boxed{
 \ell_{\mathbb R}=
 \max\left\{
   \sum_Xy_X:
   A^Ty\le0, y_X\le1\ \text{for every }X
 \right\}.}                                                       \tag{2.4}
\]

The variables (y_X) have no lower bound.  Positive mass may be placed on a
bad owner region only if enough negative mass is placed on every allowed
cycle meeting it.

Equivalently, since all columns have size (2h), the maximum fractional
number of covered owners is

\[
 \max\left\{2h\sum_Bx_B:Ax\le\mathbf1, x\ge0\right\}
 =\min\left\{\sum_Xu_X:A^Tu\ge2h\mathbf1, u\ge0\right\}.         \tag{2.5}
\]

#### Proof

Equations (2.2), (2.4), and (2.5) are the standard equality- and
inequality-form LP duals.  In (2.4), (x) has zero cost, giving
(A^Ty\le0), while (z) has unit cost, giving (y_X\le1). \(\square\)

If profile or frame-quota rows are retained, append them to (A).  For a
general decorated matrix \(\widetilde A\) and target vector (b), the exact
fractional (L^1)-error has dual

\[
 \min_{x\ge0}\|b-\widetilde Ax\|_1
 =\max\left\{
   \langle b,y\rangle:
   \widetilde A^Ty\le0, \|y\|_\infty\le1
 \right\}.                                                       \tag{2.6}
\]

This is the precise replacement for an informal Hall or expansion slogan.

## 3. The complete lattice obstruction

Let

\[
 V=\operatorname{span}_{\mathbb Q}\Lambda(A),
 \qquad
 \Lambda^{\rm sat}=V\cap\mathbb Z^\Omega.                         \tag{3.1}
\]

There are two kinds of lattice obstruction.

1. **Rational equalities:** every (z\in\ker(A^T)\cap\mathbb Q^\Omega)
   must satisfy \(\langle z,b\rangle=0\).
2. **Finite congruences:** the class of (b) in the finite group
   \(\Lambda^{\rm sat}/\Lambda(A)\) must vanish.

Equivalently, if the Smith normal form of a full-rank restriction of (A)
has invariant factors (d_1\mid\cdots\mid d_s), then the transformed
coordinates of (b) must be divisible by the corresponding (d_i)'s.

An intrinsic form, not requiring a chosen Smith basis, is

\[
 \Lambda(A)^\perp=
 \left\{
 \theta\in(\mathbb R/\mathbb Z)^\Omega:
 \sum_{X\in B}\theta_X=0\pmod1
 \text{ for every }B\in\mathscr B
 \right\}.                                                       \tag{3.2}
\]

After the rational equalities are imposed,

\[
 b\in\Lambda(A)
 \quad\Longleftrightarrow\quad
 \sum_Xb_X\theta_X=0\pmod1
 \quad\text{for every }\theta\in\Lambda(A)^\perp.               \tag{3.3}
\]

Equations (3.1)--(3.3) are the exact list of **all** congruence
obstructions.  Any shorter coordinate list is only a visible sublist unless
the Smith group has actually been computed.

## 4. Visible equalities and congruences

The following consequences of (3.3) hold in every standard pair-cube
catalogue.

### 4.1 Total and carrier totals

Every column has size (2h), so

\[
                       \sum_Xb_X\equiv0\pmod{2h}.                  \tag{4.1}
\]

More strongly, if bundles never cross a carrier component (K) (a selected
frame, packet, cube sector, or component of the bundle hypergraph), then

\[
                       \sum_{X\in K}b_X\equiv0\pmod{2h}.           \tag{4.2}
\]

### 4.2 Checkerboard equality

Every (C_{2h}) in a cube alternates between its two parity classes and has
exactly (h) vertices in each.  Therefore, in every invariant cube carrier,

\[
 \sum_{X\in K}(-1)^{\operatorname{par}(X)}b_X=0.                  \tag{4.3}
\]

This is a rational equality, not merely a congruence.

### 4.3 Coordinate-star congruences

Fix a physical coordinate (u\).  On one isometric cycle, either (u) is
inactive and occurs in zero or (2h) owners, or its pair direction is active
and it occurs in exactly (h) owners.  Consequently

\[
                    \sum_{X\ni u}b_X\equiv0\pmod h.               \tag{4.4}
\]

This holds globally, independent of how frames and packets are grouped.

### 4.4 Antipodal profile parity

For (q<h), a direction (q)-interval occurs at the two antipodal starts of
the word \(\sigma\sigma\).  The two starts have the same source and target
macroprofiles.  Hence every decorated profile-flow cell has even cycle
contribution:

\[
                         G_{q,k,\ell}\equiv0\pmod2.                \tag{4.5}
\]

Transition-direction rows, if included, are even as well, because every
active direction occurs exactly twice per cycle.

### Lemma 4.1 (cheap simultaneous repair of (4.1) and (4.4))

For the complete middle layer \(\Omega=\binom{[2m]}m\), delete fewer than
(2h) owners so that the surviving total is divisible by (2h) and every
coordinate-star total is divisible by (h).

#### Proof

Every coordinate belongs to exactly

\[
                         \binom{2m-1}{m-1}=W/2                     \tag{4.6}
\]

owners.  Let (r\in\{0,\ldots,h-1\}) be the residue of (W/2) modulo
(h).  Delete (r) distinct complementary pairs \(\{X,X^c\}\).  Every
coordinate occurs exactly once in each complementary pair, so every star
total becomes (W/2-r\), divisible by (h).  The surviving owner count is

\[
                         W-2r=2(W/2-r),                            \tag{4.7}
\]

which is divisible by (2h). \(\square\)

The leave in Lemma 4.1 is genuinely necessary on infinitely many parameters.
If \(h=2^t\), Kummer's theorem gives

\[
 v_2\binom{2m}{m}=s_2(m),                                         \tag{4.8}
\]

where \(s_2(m)\) is the number of ones in the binary expansion of \(m\).
An exact full-layer bundle factor would require \(2h\mid W\), equivalently
\(t+1\le s_2(m)\).  For every power-of-two \(m\), one has \(s_2(m)=1\), so
no exact full-layer factor with \(h\ge2\) can exist.  The complementary-pair
repair removes this entire 2-adic obstruction at cost less than \(2h\).

Carrier residues can be repaired at the counting level by deleting fewer
than (2h) owners per carrier.  If the number of frame/profile carriers is
(W^{o(1)}) and (h=W^{o(1)}), this costs (o(W)).  Likewise the number of
reachable profile-flow cells through Gaussian depth is
\(\exp(0.5494\ldots m+o(m))=o(W)\), so the visible parity repairs cost
(o(W)).

These statements do **not** show that every character in (3.2) has a cheap
repair.  A saturation proof must either compute the Smith group or prove a
bounded local generating theorem for it.

## 5. The determinant-two obstruction, used honestly

The unrestricted owner--cycle incidence matrix contains, for (h\ge3), the
three-cycle minor

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix},
 \qquad \det=-2.                                                   \tag{5.1}
\]

Thus the parent cycle matrix is not totally unimodular.  A flag restriction
deletes columns, so it may remove this particular minor; it cannot justify a
TU assertion either way.  There are two honest possibilities:

* if the three translated cycles remain flag-compatible, (5.1) persists and
  the decorated matrix is non-TU;
* after one state is frozen per owner, the catalogue may collapse to disjoint
  functional orbits and become integral for the opposite reason: it has too
  few columns.

Therefore the determinant-two obstruction is a proof that no automatic
network-matrix argument is available, not a proof that the particular all-one
right-hand side is outside the semigroup.

## 6. Successor and overlap rigidity

Fix one successful state (s_X\in\mathcal S_X) at every owner with a
nonempty lower flag.  Its first literal lower step specifies one selected
coordinate (a_X\in X), its paired mate \(b_X\notin X\), and hence the unique
candidate successor

\[
                         S(X)=X-\{a_X\}+\{b_X\}.                   \tag{6.1}
\]

Let

\[
 w_H(X)=(d_0(X),d_1(X),\ldots,d_{H-1}(X))                         \tag{6.2}
\]

be the ordered unordered-pair directions literalizing its first (H) lower
steps (truncate at (r_X) when necessary).

### Lemma 6.1 (de Bruijn overlap)

If (X,Y) occur consecutively in a compatible directed bundle and both flags
have length at least (H), then

\[
 Y=S(X),
 \qquad
 (d_0(Y),\ldots,d_{H-2}(Y))
 =(d_1(X),\ldots,d_{H-1}(X)).                                    \tag{6.3}
\]

The analogous reversed overlap holds for the upper/backward flags.  Around a
whole bundle the direction labels are periodic with half-period (h), and
the first (h) labels are distinct.

#### Proof

The first lower face is the intersection of (X) with its next owner, so its
literal pair direction forces (6.1).  At the next start, the following
(H-1) transitions are the previous start's transitions two through (H).
Directions are unordered physical pairs, so their labels agree exactly as in
(6.3).  The word of an isometric (C_{2h}) is \(\sigma\sigma\), giving the
last assertion. \(\square\)

### Theorem 6.2 (frozen-state functional reduction on the active core)

Quarantine the owners whose lower SCD flag is empty; by (7.2) they form an
\(o(W)\) set.  Restrict to bundles contained in the remaining active core.
After the states are frozen, every compatible cycle in this restricted
catalogue is a directed orbit of the function \(S\).  The compatible bundles
are exactly those orbits which:

1. have length (2h);
2. satisfy all lower and upper overlaps; and
3. have a direction word \(\sigma\sigma\).

Distinct such orbits are vertex-disjoint.  Hence the frozen owner--bundle
matrix is a submatrix of a partition matrix and is totally unimodular.  Its
maximum fractional and integral packings coincide, and both leave exactly the
owners not lying on good orbits.

#### Proof

Equation (6.1) gives every owner of the active core exactly one candidate
outgoing arc.  Any directed cycle using those arcs is therefore an orbit of
\(S\), and distinct orbits of a function are disjoint.  Lemma 6.1 and the
upper conditions select the good orbits.  Their incidence columns have
disjoint supports. \(\square\)

The equality of the fractional leave can also be read directly in the dual
(2.4).  Let \(R\) be the set of active-core owners lying on no good orbit and
put \(y=\mathbf1_R\).  Every retained bundle is disjoint from \(R\), so
\(A^Ty=0\), while \(\sum_Xy_X=|R|\).  Thus \(y\) is an exact signed-dual
certificate for the unavoidable frozen-state leave.

This theorem is the central warning.  For fixed SCD states there is no
interior cone whose integral points need rounding: either the desired good
orbits were built into the state assignment, or the corresponding owners are
uncoverable even fractionally.

## 7. A positive depth-one projection

The preceding obstruction begins after the first literal step.  At depth one,
if upper constraints, frame exclusions, and cycle closure are temporarily
ignored, all lower SCD targets can be assigned distinct successor owners.

Let \(\mathcal A\subseteq\Omega\) be the owners whose SCD chain reaches rank
(m-1).  The map

\[
 X\longmapsto T_X=L^-_{X,1}                                      \tag{7.1}
\]

is a bijection from \(\mathcal A\) to \(\binom{[2m]}{m-1}\).  In particular,

\[
 |\Omega\setminus\mathcal A|={W\over m+1}=o(W).                  \tag{7.2}
\]

Build a bipartite graph with left side \(\mathcal A\), right side \(\Omega\),
and

\[
 X\sim Y
 \quad\Longleftrightarrow\quad
 T_X\subset Y\text{ and }Y\ne X.                                \tag{7.3}
\]

### Proposition 7.1 (collision-free first successors)

The graph (7.3) has a matching saturating \(\mathcal A\).

#### Proof

A rank-((m-1)) target has (m+1) middle supersets; excluding its own SCD
owner leaves every left vertex with degree exactly (m).  A middle owner
contains (m) rank-((m-1)) targets, so every right degree is at most (m).
For any \(\mathcal Z\subseteq\mathcal A\), all (m|\mathcal Z|) incident
edges end in \(\Gamma(\mathcal Z)\), while each right vertex receives at most
(m) of them.  Hence

\[
                         |\Gamma(\mathcal Z)|\ge|\mathcal Z|.     \tag{7.4}
\]

Hall's theorem proves the claim. \(\square\)

Every matched pair differs by one Johnson swap and can be made a legal pair
direction in some frame.  Proposition 7.1 does not make the partial successor
map closed, does not impose the upper flag, and does not force (2h)-cycles.
It nevertheless proves that the remaining obstruction is more structured
than a first-neighbour collision.

## 8. Exact approximate-saturation target

The integral leave is

\[
 \ell_{\mathbb Z}(A)=
 \min\{|L|:\mathbf1_{\Omega\setminus L}\in\mathsf S(A)\}.        \tag{8.1}
\]

The desired whole-cycle theorem after the SCD construction is

\[
 \boxed{\ell_{\mathbb Z}(A)=o(W/H).}                              \tag{8.2}
\]

If only one depth is charged, (o(W)) is enough.  Equation (8.2) is the
correct simultaneous-depth scale by (1.8).

There are three logically separate gates:

1. **fractional gate:** the dual optimum (2.4) is (o(W/H));
2. **lattice gate:** after a leave of that size, the all-one vector satisfies
   every character in (3.2); and
3. **semigroup gate:** the resulting lattice point lies in
   \(\mathsf S(A)\), despite the determinant-two obstruction.

The SCD--Hoffman theorem proves none of these for the bundle matrix.  The
frozen-state reduction shows why: for an arbitrary successful state choice,
the fractional gate itself can fail by \(\Theta(W)\).

A plausible route would have to choose the states and cycles simultaneously,
prove a fractional perfect matching by (2.2), compute or locally generate the
Smith lattice, and then establish a growing-uniformity matching/absorber
theorem for the resulting hypergraph.  Ordinary Birkhoff, Hoffman, TU, and
depthwise Hall stop before the first of these steps.

## 9. Final boundary

The exact SCD construction should be viewed as a perfect integral solution of
the **path** problem.  Whole-cycle bundling is the following strictly stronger
statement:

> Choose one successful state at each of almost all owners so that their
> length-(H) direction signatures form almost-disjoint de Bruijn overlaps,
> and those overlaps close into isometric (2h)-cycles with word
> \(\sigma\sigma\).

The cycle-bundle hypergraph and its dual/lattice are now exact, the visible
congruences are cheap, and simple first-successor collisions can be removed.
What remains is coherent state selection plus cyclic closure.  No valid
approximate saturation proof is currently known.
