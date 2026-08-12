# Two-sided depth-one pseudofactors and the complement-fusion obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, or web input
is used.

## 0. Outcome

Put

\[
 \Omega=[2m],\qquad
 \mathcal M=\binom\Omega m,\qquad
 W=|\mathcal M|,
\]

and

\[
 \mathcal L=\binom\Omega{m-1},\qquad
 \mathcal U=\binom\Omega{m+1},\qquad
 N=|\mathcal L|=|\mathcal U|=W-K,
 \quad K={W\over m+1}=\operatorname {Cat}_m.
 \tag{0.1}
\]

For a Johnson edge \(e=XY\), write

\[
 \ell(e)=X\cap Y,\qquad u(e)=X\cup Y.
 \tag{0.2}
\]

The following unconditional asymptotic depth-one object is available on both
central grounds `2m` and `2m+1`:

> There is a spanning Johnson linear forest \(F_m\) with
> \(e(F_m)=W-o(W)\), whose lower colours \(\ell(e)\) are pairwise distinct
> and whose upper colours \(u(e)\) are pairwise distinct.

Consequently both adjacent colour layers have only \(o(W)\) holes, and the
forest has \(o(W)\) path components.  Cyclically concatenating the paths
gives a permutation of every middle owner with only \(o(W)\) non-Johnson
seams.  This is a genuine two-sided depth-one **pseudocycle**, but it is not
a Johnson cycle.

A sufficient remaining gate for this pseudofactor route is
endpoint-compatible Hamiltonization: after deleting only \(o(W)\) further
forest edges, a subcollection of the resulting paths covering \(W-o(W)\)
owners must admit Johnson connector edges whose component quotient is one
cycle.  Requiring all paths to be retained is a stronger sufficient gate,
not an equivalent reformulation of the almost-spanning target.  Neither the
fixed-girth matching theorem nor the Gregor--Mička--Mütze central-level
cycle theorem supplies even the weaker assertion.

There is also a sharp no-gain result for the most immediate proposed repair.
On even ground, complementing a lower-rainbow one-sided core makes it
upper-rainbow.  Any cycle which retains all but \(o(W)\) edges of both cores
can exist only if the two cores already have a common two-sided-rainbow
subgraph of size \(W-o(W)\).  Reversal changes no edge set.  Thus sparse
complement/reversal splicing cannot manufacture the missing opposite rainbow;
it presupposes it.

This note does not construct the requested single cycle and does not claim
constant one.

## 1. The unconditional two-sided pseudofactor

We record the already audited fixed-uniformity construction because its exact
interface is the starting point for the single-cycle question.

Make a four-partite, four-uniform hypergraph \(\mathcal H_m\) with parts

\[
 \mathcal L,\qquad \mathcal U,\qquad
 \mathcal M^0,\qquad \mathcal M^1,
 \tag{1.1}
\]

where \(\mathcal M^0,\mathcal M^1\) are two labelled copies of the middle
layer.  For every flag

\[
 S\in\mathcal L,qquad U\in\mathcal U,qquad S\subset U,
 \tag{1.2}
\]

write \(U\setminus S=\{a,b\}\),
\(X=S\cup\{a\}\), and \(Y=S\cup\{b\}\).  Insert the four hyperedges

\[
 \{S,U,X^i,Y^j\},\qquad i,j\in\{0,1\}.
 \tag{1.3}
\]

A matching in \(\mathcal H_m\) projects to a simple Johnson graph of maximum
degree at most two, with both edge-colour maps injective.  Indeed, the two
clones impose middle degree at most two, while the \(\mathcal L\)- and
\(\mathcal U\)-vertices impose the two rainbow conditions.

The exact degrees are

\[
 d(S)=d(U)=2m(m+1),qquad d(X^i)=2m^2,
 \tag{1.4}
\]

and the maximum pair codegree is \(2m\).  Thus

\[
 {\delta(\mathcal H_m)\over\Delta(\mathcal H_m)}
 ={m\over m+1}=1-o(1),
 \qquad
 \Delta_2(\mathcal H_m)=o(\Delta(\mathcal H_m)).
 \tag{1.5}
\]

For fixed \(L\), declare a forbidden configuration to be a submatching whose
projected Johnson edges form a cycle of length at most \(L\).  If
\(D=2m(m+1)\), a fixed lifted edge lies in

\[
 O_L(D^{i-2})
 \tag{1.6}
\]

forbidden \(i\)-cycles, and a prescribed \(j\)-edge submatching extends to
at most

\[
 O_L(D^{i-j-1})
 \tag{1.7}
\]

of them.  These estimates follow by choosing a projected continuation walk;
the last edge is forced, and clone choices contribute only an \(L\)-dependent
constant.  The published Delcourt--Postle small-codegree conflict-free
matching theorem, in the fixed-uniformity form audited in
`ASYMPTOTIC_MATCHING.md`, therefore gives, for every fixed \(L\), a matching
of size \(N-o_L(W)\) whose projection has girth greater than \(L\).  This is
an explicit external black box; (1.4)--(1.7) are the hypotheses verified
here.

Delete one edge from every projected cycle.  At most \(W/(L+1)\) edges are
deleted.  Taking first \(m\to\infty\) for fixed \(L\), and then using the
standard diagonal choice \(L=L(m)\to\infty\), proves the following.

### Theorem 1.1 (two-sided rainbow linear pseudofactor)

There is a spanning linear forest \(F_m\subseteq J(2m,m)\) such that

\[
 e(F_m)=W-o(W),\qquad c(F_m)=W-e(F_m)=o(W),
 \tag{1.8}
\]

and both maps

\[
 e\longmapsto\ell(e),\qquad e\longmapsto u(e)
 \tag{1.9}
\]

are injective on \(E(F_m)\).  It consequently misses only \(o(W)\) members
of each of \(\mathcal L\) and \(\mathcal U\).

The proof above is the depth-one specialization of the audited construction
in `ASYMPTOTIC_MATCHING.md`.  Its use here is exact: fixed-uniformity
matching is used only before the diagonal passage.

### Corollary 1.2 (odd-ground version)

The conclusion of Theorem 1.1 also holds in `J(2m+1,m)`.  If

\[
 W^+=\binom{2m+1}{m},\qquad
 N^- =\binom{2m+1}{m-1}=\frac{m}{m+2}W^+,
\]

then there is a spanning linear forest with `W^+-o(W^+)` edges whose
intersection and union colours are both injective.  It misses `o(W^+)`
targets on each shore and has `o(W^+)` components.

#### Proof

Use the same cloned four-graph.  Its exact degrees are now

\[
\begin{array}{c|c}
\text{vertex class}&\text{degree}\\ \hline
\binom{[2m+1]}{m-1}&2(m+1)(m+2),\\
\binom{[2m+1]}{m+1}&2m(m+1),\\
\text{each middle clone}&2m(m+1).
\end{array}                                           \tag{1.10}
\]

The maximum pair codegree is `2(m+1)`, and the Johnson degree is
`m(m+1)`.  Hence the degree ratio tends to one, the pair-codegree ratio
tends to zero, and the conflict counts (1.6)--(1.7) are unchanged up to
absolute factors.  Moreover

\[
 \frac{|E(\mathcal H_m)|}{2(m+1)(m+2)}=N^-=W^+-O(W^+/m). \tag{1.11}
\]

The same fixed-girth conflict-free matching theorem therefore supplies
`N^--o(W^+)=W^+-o(W^+)` projected edges.  Delete one edge from every
remaining cycle and take the same diagonal limit.  Since both target shores
have size `W^+-o(W^+)` or `W^+`, the two missing counts are `o(W^+)`.
Finally a spanning forest on `W^+` vertices with `W^+-o(W^+)` edges has
`o(W^+)` components. `\square`

## 2. Exact seam ledger

Orient every nontrivial component of \(F_m\) arbitrarily.  Regard an isolated
owner as a path of length zero.  List the oriented paths in any cyclic order
and concatenate their vertex lists.

### Corollary 2.1 (cyclic owner pseudocycle)

There is a cyclic permutation

\[
 X_0,X_1,\ldots,X_{W-1}
 \tag{2.1}
\]

of all middle owners with a distinguished family of \(W-o(W)\) consecutive
pairs which are Johnson edges and on which the lower and upper colours are
both injective and miss only \(o(W)\) targets.  The remaining \(o(W)\)
seams are unrestricted; a seam which happens to be a Johnson edge is not
asserted to carry a fresh colour.

More exactly, the number of unlicensed seams is at most

\[
 c(F_m)=o(W).
 \tag{2.2}
\]

#### Proof

Every forest edge is one consecutive pair in (2.1).  Exactly one seam is
inserted after each component, including the cyclic closing seam.  Hence
there are \(c(F_m)\) seams.  Some may accidentally be Johnson edges, so this
is an upper bound.  The internal colours retain the injectivity and coverage
of Theorem 1.1. \(\square\)

The distinction is essential.  A Johnson cycle requires every seam in
(2.1) to be a Johnson edge.  An arbitrary pair of middle sets may have
Johnson distance as large as \(m\); replacing each seam by a shortest
geodesic can cost as much as \(m c(F_m)\).  The diagonal theorem proves only
\(c(F_m)=o(W)\), not \(c(F_m)=o(W/m)\).  Therefore geodesic insertion is not
an audited \(o(W)\) repair.

## 3. The exact endpoint completion gate

Let \(F\) be any spanning linear forest on \(\mathcal M\).  Give each
nontrivial path its two endpoints as ports, and give an isolated owner two
formal ports at the same owner.  Form the port graph \(A(F)\): two ports are
adjacent when their underlying middle owners are distinct and Johnson
adjacent.  A port matching is called **physically simple** when it never
selects the same underlying Johnson edge twice.

### Proposition 3.1 (endpoint-cycle criterion)

The forest \(F\) extends, without deleting a forest edge, to a Hamilton cycle
of \(J(2m,m)\) if and only if \(A(F)\) contains a physically simple perfect
matching \(M\) such that, after every path component of \(F\) is contracted
to one vertex, the matching edges form one connected \(2\)-regular
multigraph.  When \(F\) has one component, this permits the single quotient
loop obtained by joining the two distinct endpoints of that path.

#### Proof

In a Hamilton extension, every path endpoint needs exactly one new incident
edge, so the added edges give a perfect matching of the ports.  Contracting
the retained paths leaves the component quotient of the Hamilton cycle,
which is one cycle.

Conversely, expand every contracted vertex of such a quotient through its
oriented path.  Port matching gives degree two at every owner and the
one-cycle quotient gives connectedness.  Thus the expansion is a Hamilton
cycle. \(\square\)

If \(d\) forest edges are deleted first, the number of path components and
port pairs rises by exactly \(d\).  Consequently the exact asymptotic gate is:

> Find \(F'_m\subseteq F_m\) with
> \(|E(F_m)\setminus E(F'_m)|=o(W)\) such that the port graph of \(F'_m\)
> has a connected perfect matching as in Proposition 3.1.

The cloned-hypergraph construction controls projected short cycles, but it
places no condition on this port graph.  High girth is not endpoint
connectability.

## 4. Complementation and reversal do not supply the gate

For \(X\in\mathcal M\), put \(cX=\Omega\setminus X\), and for a Johnson edge
\(e=XY\), put \(ce=(cX)(cY)\).  Then

\[
 \ell(ce)=\Omega\setminus u(e),
 \qquad
 u(ce)=\Omega\setminus\ell(e).
 \tag{4.1}
\]

Thus if a graph \(P\) is lower-rainbow, \(cP\) is upper-rainbow.

The following elementary inequality is the precise audit of the proposed
fusion.

### Theorem 4.1 (complement-fusion no-gain theorem)

Let \(P\) be any Johnson graph with \(N\) edges, and let \(cP\) be its
complement.  Let \(C\) be any simple Johnson cycle, of any length at most
\(W\).  If

\[
 |E(C)\cap E(P)|\ge N-a,
 \qquad
 |E(C)\cap E(cP)|\ge N-b,
 \tag{4.2}
\]

then

\[
 \boxed{
 |E(C)\cap E(P)\cap E(cP)|
 \ge W-2K-a-b.}
 \tag{4.3}
\]

In particular, if \(a+b=o(W)\), then \(P\cap cP\) already contains
\(W-o(W)\) edges.  If \(P\) is lower-rainbow, this common subgraph is
two-sided-rainbow.

#### Proof

Inside the set \(E(C)\), inclusion--exclusion gives

\[
\begin{aligned}
 |C\cap P\cap cP|
 &\ge |C\cap P|+|C\cap cP|-|C|\\
 &\ge 2N-a-b-W\\
 &=W-2K-a-b.
\end{aligned}
 \tag{4.4}
\]

If \(P\) is lower-rainbow, the common edges have distinct lower colours.
They lie in \(cP\), whose upper colours are distinct by (4.1). \(\square\)

Reversal of a cycle changes its orientation but not its edge set, so it does
not weaken (4.3).  A coordinate permutation merely replaces \(cP\) by a
conjugate; the identical inclusion--exclusion bound applies to that fixed
conjugate.

The theorem does not say that a new construction using mostly new edges is
impossible.  It says that **sparse splicing which purports to retain both
one-sided cores is circular**: their common \(W-o(W)\) core must already have
the desired simultaneous rainbow property.

## 5. Audit of the published central-level route

Gregor--Mička--Mütze Corollary 2, applied to two adjacent levels, gives a
lower-saturating projected Johnson cycle.  Dually it gives an
upper-saturating projected cycle.  These are separate objects.

On odd ground \([2m+1]\), put

\[
 W_o=\binom{2m+1}{m},\qquad
 N^-=\binom{2m+1}{m-1},\qquad
 D_o=W_o-N^-=\frac{2W_o}{m+2}.                       \tag{5.0}
\]

A middle-level Hamilton cycle projects to a Hamilton cycle on all \(m\)-sets
whose union colours are every \((m+1)\)-set exactly once.  The theorem does
not bound collisions among its intersection colours.  Complementation swaps
the two cube ranks; it does not turn this into a second cycle on the same
rank-\(m\) owner class with the missing lower ledger.

For the two-level lower-saturating GMM core, write

\[
 R_i\subset X_i\supset R_{i+1},\qquad
 X_i=R_i\cup R_{i+1}.                                \tag{5.1a}
\]

Its unproved upper map is exactly

\[
 X_{i-1}\cup X_i=R_{i-1}\cup R_i\cup R_{i+1}.        \tag{5.1b}
\]

If \(c_+\) is the collision excess of (5.1b), then on odd ground the
number of missing upper targets is

\[
                            D_o+c_+.                  \tag{5.1c}
\]

Thus the GMM core solves the requested asymptotic two-sided problem exactly
when one can choose it with \(c_+=o(W_o)\).  Corollary 2 contains no such
second-window assertion.

There is a full-owner version using three consecutive levels.  A saturating
cycle there alternates all \(W_o\) middle owners \(X_i\) with \(W_o\) distinct
outer vertices \(Y_i\), each of rank \(m-1\) or \(m+1\).  Projecting away
the \(Y_i\)'s gives a Hamilton Johnson cycle.  Let \(Z_i\) be the opposite
colour of the edge \(X_iX_{i+1}\): if \(Y_i\) is its intersection, then
\(Z_i\) is its union, and conversely.  With

\[
 \mathcal O=\binom{[2m+1]}{m-1}\dot\cup
             \binom{[2m+1]}{m+1},
\]

the exact total two-sided missing count is

\[
 \boxed{M^-+M^+=N^--|\operatorname{supp}(Z)\setminus Y|.} \tag{5.1d}
\]

Indeed, \(|\mathcal O|=N^-+W_o\), \(|Y|=W_o\), and the present target support is
exactly \(Y\cup\operatorname{supp}(Z)\).  Thus three-level saturation gives
the requested Hamilton owner cycle, but the desired shadow conclusion is
equivalent to the new opposite-colour estimate

\[
             |\operatorname{supp}(Z)\setminus Y|=N^--o(W_o). \tag{5.1e}
\]

Again Corollary 2 contains no estimate of this quantity.

On even ground, complementation does stay inside the middle owner layer, but
Theorem 4.1 applies.  In the standard two-copy quotient of an odd-dimensional
middle-level Hamilton cycle, the upper and lower contracted forests
\(F_+,F_-\) each have \(N\) edges.  Any proposed cycle retaining
\(N-o(W)\) edges from each must likewise retain

\[
 |F_+\cap F_-|\ge 2N-W-o(W)=W-o(W).
 \tag{5.1}
\]

Complement invariance gives only \(F_-=cF_+\), not the edgewise overlap
(5.1).  Hence the published symmetry is duality, not simultaneous
two-sided colour perfection.

### The explicit GJM lexical projection has linear opposite-colour waste

The description of the GJM lexical forest and the fact that the published
six-cycle joins leave that lower forest unchanged are imported published
inputs, independently checked in
`MATH_OBSTRUCTION_THREE_LEVEL_OPPOSITE_COLOR_AND_GJM_LINEAR_COLLISIONS_20260726.md`
and `GJM_FOUR_LEVEL_AUDIT.md`.  The collision injection below is internal.

The direct Gregor--Jäger--Mütze--Sawada--Wille middle-four-level lexical
construction is not a candidate for repairing (5.1b) sparsely.  Suppress
its rank-\((m-1)\) vertices.  The resulting lower-colour-perfect linear
forest is indexed by the binary words \(x\) of length \(2m+1\) and weight
\(m-1\).  Its upper colour \(\psi(x)\) is obtained by changing the last
two down-steps of \(x\) in the lexical row scan into up-steps.

### Theorem 5.1 (linear lexical collision family)

The duplicate upper-colour excess of this forest satisfies

\[
 \delta_m\ge\binom{2m-1}{m-2}
       =\left(\frac14-o(1)\right)W_o.                \tag{5.2}
\]

Consequently any owner-cycle projection retaining all but \(s\) of its
lower-forest edges still has upper collision excess at least
\(\delta_m-s\).  Achieving \(o(W_o)\) upper holes requires

\[
                         s\ge(1/4-o(1))W_o.           \tag{5.3}
\]

#### Proof

Choose an arbitrary word \(y\) of length \(2m-1\) and weight \(m-2\).
Write

\[
                         y=A0B                       \tag{5.4}
\]

at the zero step at which its lattice path first reaches its global
minimum.  Form

\[
                         x=A010B,\qquad x'=A001B.     \tag{5.5}
\]

In \(x\), the first and third displayed zeros are the final two down-steps
in the lexical row scan.  In \(x'\), they are the first and second displayed
zeros.  The first-global-minimum choice excludes a later lower row or an
earlier competitor on the same row.  Hence

\[
                         \psi(x)=A111B=\psi(x').     \tag{5.6}
\]

The pairs are disjoint as \(y\) varies: the intrinsic two selected lexical
steps determine whether the local block is \(010\) or \(001\), and deleting
the last two positions of that block recovers \(y\).  There are
\(\binom{2m-1}{m-2}\) choices of \(y\), so every pair lowers the image size
by at least one.  Finally

\[
 \frac{\binom{2m-1}{m-2}}{\binom{2m+1}{m}}
       =\frac{m-1}{2(2m+1)}=\frac14+O(m^{-1}).        \tag{5.7}
\]

Deleting one forest edge reduces duplicate excess by at most one; adding
connector edges cannot remove a duplicate among retained edges.  This proves
(5.3). \(\square\)

The six-cycle joins used in the published GJM Hamiltonicity proof lie in
the upper two levels and leave this lower lexical forest unchanged.  Hence
Theorem 5.1 is a no-go for the direct published projection, not merely for
one orientation of it.  It does not rule out a new three-level saturating
cycle with \(c_+=o(W)\).

There is an independent exact obstruction: when
\(m=2^t-1\), the Catalan number \(K\) is odd, and no exact two-sided-rainbow
cycle factor of length \(N\) exists.  The complete flag-lift and deficiency
proof is in
`MATH_THEOREM_Q1_DIAMOND_LIFT_AND_CATALAN_PARITY_OBSTRUCTION_20260726.md`.
That obstruction costs only a bounded number of colour omissions and does
not refute the \(o(W)\)-defect target.

## 6. Exact proved/conditional boundary

In this section \(W\) denotes the relevant middle-layer size on the ground
under discussion.  The following are unconditional.

1. On both central grounds \(2m\) and \(2m+1\), there is a
   two-sided-rainbow Johnson linear forest with \(W-o(W)\) edges and
   \(o(W)\) components.
2. Hence there is a cyclic permutation of all middle owners with \(o(W)\)
   unrestricted seams, while a distinguished legal set of \(W-o(W)\)
   internal transitions has both depth-one shadow defects \(o(W)\).
3. A three-level GMM saturating cycle does give a Hamilton owner cycle, but
   its total defect is exactly (5.1d); the opposite-colour estimate (5.1e)
   is additional.
4. Exact simultaneous colour matchings have no marginal Hall obstruction;
   their middle lift and connectivity are the issue.
5. Sparse complement/reversal fusion cannot create simultaneous
   rainbowness unless a \(W-o(W)\) simultaneous core was already present.
6. The direct GJM lexical projection has \((1/4-o(1))W\) opposite-colour
   collision excess and needs a linear rerouting.
7. The strongest exact version fails in infinitely many even dimensions by
   Catalan parity.

The desired almost-spanning conclusion is the first statement below.  The
second is a sufficient gate for the particular pseudofactor route, but is
strictly stronger unless one also proves an absorption theorem for discarded
owners.

* Construct directly a Johnson cycle on \(W-o(W)\) middle owners whose two
  colour supports have size \(N-o(W)\).
* Prove endpoint-cycle completion, after \(o(W)\) deletions and after
  discarding path components of total owner mass \(o(W)\), for one of the
  two-sided pseudofactors in Theorem 1.1.  Retaining every component would
  give a full Hamilton cycle and is stronger still.

No currently audited rate gives \(o(W/m)\) path components, so replacing
each seam by an arbitrary length-\(m\) Johnson geodesic is not a proof.
No statement in the published central-level cycle theorem supplies the
endpoint matching in Proposition 3.1.

## 7. Adversarial audit

* Theorem 1.1 uses a fixed-uniformity conflict-free matching theorem.  The
  diagonal passage proves only unparameterized \(o(W)\); it must not be
  upgraded to \(o(W/m)\).
* Corollary 2.1 is deliberately called a pseudocycle.  Its seams can be
  non-Johnson pairs and therefore it is not the object requested in the
  question.
* Proposition 3.1 is an equivalence for retaining all edges of a specified
  forest.  It does not assert that its port graph has the required matching.
* Theorem 4.1 obstructs retention-based complement fusion only.  A cycle
  built from mostly new edges lies outside its hypothesis.
* Catalan parity refutes exact zero-defect factors on an infinite subsequence,
  but permits \(o(W)\) defects.  It is not an asymptotic no-go.

Accordingly the requested two-sided single Johnson cycle remains open; the
new structural closure is that neither ordinary high-girth pseudofactor
output nor complement/reversal splicing supplies the missing connectivity.
