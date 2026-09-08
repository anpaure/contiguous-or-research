# Row-label composition of the four-shore \(Q_4\) cube

Date: 2026-07-26

Method: pure mathematics only. No finite search, computation, solver, or
web input is used.

Source audited and extended:
\(MATH\_THEOREM\_Q4\_FOUR\_SHORE\_FIXED\_POINT\_FREE\_TWIST\_CUBE\_20260726.md\).

## 0. Verdict

The two shore generators

\[
                         A=(a\ c),\qquad B=(b\ d),
 \qquad a<b<c<d,                                      \tag{0.1}
\]

can be selected row by row, but their component bits are not a Cartesian
four-bit cube on the cycle labels.  Put

\[
 \delta=e_a+e_c,\qquad \gamma=e_b+e_d.                \tag{0.2}
\]

The row-label theorem below is a theorem for a proper four-coordinate
subsystem of a growing \(Q_h\), with \(h\ge8\).  It is not a claim that
the bare \(Q_4\) has twelve component states.  In the bare cube,

\[
                         \delta+\gamma=\mathbf1.      \tag{0.2a}
\]

Antipodal roots represent the same oriented cycle, so consistency forces
both selector fields to be constant.  Exactly the four global shores
\(I,A,B,AB\) survive there.

On every affine row-label plane
\(Q=k+\langle\delta,\gamma\rangle\), an \(A\)-field has two
\(\delta\)-pair values and a \(B\)-field has two \(\gamma\)-pair values.
There are sixteen formal states.  Exactly twelve are owner-legal.

In coordinates \(k+x\delta+y\gamma\), write

\[
 \alpha(x,y)=U(y),\qquad \beta(x,y)=V(x).             \tag{0.3}
\]

The unique phase at which the prefix cuts both active direction pairs has
row-label map

\[
                         (x,y)\longmapsto
                 (x+U(y),\,y+V(x)).                  \tag{0.4}
\]

It is a permutation if and only if

\[
 \boxed{
 (U(0)+U(1))(V(0)+V(1))=0.}                          \tag{0.5}
\]

Thus one field may vary transversely, or both may be constant, but both
may not vary transversely on the same label plane.  The four illegal
states identify both diagonal pairs at the middle prefix, giving two
double-covered and two omitted phase owners.  This is an exact physical
ownership failure.

Every one of the twelve legal states has a literal sequential
realization on the same four-cycle-label owner packet.  If \(U\) is
constant, install the \(A\)-shore first and then the \(\gamma\)-pair
\(B\)-components.  If \(V\) is constant, install \(B\) first and then the
\(\delta\)-pair \(A\)-components.  Condition (0.5) says that at least one
of these two orders is available.  Thus the twelve states are genuine
owner trades, not merely Latin end states.

For clarity, the twelve-state count begins only after the quartet is
embedded properly in a larger syndrome factor, where
\(\mathbf1\notin\langle\delta,\gamma\rangle\).  In \(Q_4\), translation
by \(\mathbf1=\delta+\gamma\) sends \((x,y)\) to
\((x+1,y+1)\).  Requiring the same shore on the two antipodal roots makes
\(U(y+1)=U(y)\) and \(V(x+1)=V(x)\), hence both are constant and the
twelve states collapse to four.

The twelve legal states give

\[
 \boxed{12^{\,N/4}}                                  \tag{0.6}
\]

distinct exact row fields for one coordinate quartet on a syndrome label
space of size \(N=|K_0|\).  Their information is
\((N/4)\log_2 12\), namely \(0.89624\ldots\) bits per syndrome cycle.
Their local changed-edge counts on the four rows of one label plane are

\[
\begin{array}{c|ccccc}
\text{changed directed edges}&0&8&16&24&32\\ \hline
\text{number of legal states}&1&4&2&4&1.
\end{array}                                           \tag{0.7}
\]

In particular the opposite \(AB\)-state changes all eight occurrences of
the four active direction positions in each long row; uniform choice from
the twelve legal states changes half of those active occurrences on
average.

Disjoint phase-slab quartets compose.  For \(t\) coordinate quartets with
disjoint supports and disjoint prefix slabs, the exact number of factor
states is

\[
                         12^{\,tN/4}.                \tag{0.8}
\]

Their maximum and uniform-state mean changed-edge densities are,
respectively,

\[
                         {4t\over h},\qquad {2t\over h}.           \tag{0.8a}
\]

Thus a hypothetical full-coordinate atlas with \(t=h/4\) would have
\[
 12^{\,2^h/32}\ \text{states},\qquad
 \text{maximum action }1,\qquad
 \text{uniform mean action }{1\over2}.              \tag{0.8b}
\]
This conditional full cover is not supplied by the standard syndrome
presentation.

The standard parity-alternating syndrome presentation does not guarantee
two repeated-column pairs in every consecutive four-coordinate block.
What it does guarantee is one equal-column class consisting of all even
positions.  For \(h=2^s\ge8\), take

\[
 (a_j,b_j,c_j,d_j)
  =(8j,\,8j+2,\,8j+4,\,8j+6),
 \qquad 0\le j<h/8.                                  \tag{0.9}
\]

This gives \(t=h/8\) literal disjoint-slab four-shore layers and

\[
 \boxed{
 \#\mathcal F
   =12^{\,2^h/64},\qquad
 \log_2\#\mathcal F
   ={\log_2 12\over64}\,2^h.}                        \tag{0.10}
\]

Full activation changes exactly one half of all directed successor edges;
uniform legal plane states change one quarter on average.

The fixed-point-free opposite shore removes only the fixed-coordinate
part of the old obstruction, and only on coordinates covered by the
quartets.  It does not remove either of the following.

1. A globally fixed shore in one translation-syndrome factor still has
   the syndrome-kernel collision subgroup, independently of whether its
   coordinate permutation has fixed points.
2. Arbitrary row-dependent \(A/B\) choices preserve the fixed wire
   partition \(\{\{a,c\},\{b,d\}\}\).  Hence a completed \(d\)-support has
   at most \(2^d\) images, and aligned trace codes have distinct proportion
   at most \(2h/2^d\).  Gaussian-depth collision therefore remains total.

Moreover, the fixed-point-free same-owner relation itself survives only
on the four constant charts.  It is not inherited by the twelve-state
high-entropy menu.

For the guaranteed atlas (0.9), all odd directions are fixed, so a cyclic
\(d\)-interval has at most \(\lceil d/2\rceil\) active wire entries.  The
sharper bound is

\[
 \boxed{\text{distinct aligned-trace proportion}
 \le 2h\,2^{-\lfloor d/2\rfloor}.}                  \tag{0.11}
\]

Thus the four-shore cube improves the exact local alphabet and eliminates
the local half-fixed defect at its opposite corner, but a fixed-wire
composition still cannot supply the completed-support entropy required at
Gaussian depth.  A transverse frame-changing associator remains necessary.

## 1. Exact row-label model

Let \(h\ge8\).  Let \(P\) be the rooted syndrome-transversal cycle in
\(Q_h\), let \(K_0\) be its cycle-label space, and suppose the four coordinate columns
in (0.1) satisfy

\[
                         \Psi(e_a)=\Psi(e_c),\qquad
                         \Psi(e_b)=\Psi(e_d).         \tag{1.1}
\]

Assume
\(\mathbf1\notin\langle\delta,\gamma\rangle\), as is automatic when these
four active coordinates are a proper subset of the ambient coordinates.
Then \(\delta,\gamma\in K_0\), after choosing the phase complement to
vanish on their span.  Let

\[
 \alpha:K_0\longrightarrow\mathbb F_2,\qquad
 \beta:K_0\longrightarrow\mathbb F_2                 \tag{1.2}
\]

satisfy the literal pair-component conditions

\[
 \alpha(k+\delta)=\alpha(k),\qquad
 \beta(k+\gamma)=\beta(k).                           \tag{1.3}
\]

Put

\[
 \sigma_k=A^{\alpha(k)}B^{\beta(k)},\qquad
 C_k=\sigma_kP+k.                                    \tag{1.4}
\]

Every \(C_k\) is individually an isometric \(C_{2h}\), because its
direction word is a coordinate permutation repeated twice.  Exact
individual rows are not enough: their phase owners must also partition
the cube.

For a first-half prefix \(p_i\), define

\[
 T_i(k)=k+\sigma_kp_i+p_i.                           \tag{1.5}
\]

The family \(\{C_k:k\in K_0\}\) is an exact factor if and only if every
\(T_i\) is a permutation of \(K_0\).

Although the bare \(Q_4\) four-shore cube has only a common phase modulo
four, the present proper-block embedding has a full common phase.  Choose
\(\eta:K\to\mathbb F_2\) with
\(\eta(\mathbf1)=1\) and
\(\eta(\langle\delta,\gamma\rangle)=0\).  Every displacement in (1.5)
lies in this kernel, so

\[
 c(p_i+\ell)=i+h\eta(\ell)\pmod {2h}                 \tag{1.5a}
\]

is cyclic on every exact row field in the twelve-state family.  Thus the
growing embedding repairs the local \(\mathbb Z_8\)-phase failure without
altering the middle-prefix ownership condition.

The distinction is load-bearing.  Common phase modulo four together with
the common complement port does not by itself satisfy the standard
common-phase suspension lemma, whose tail fibres distinguish the two
antipodal occurrences of a phase.  Any direct suspension of the bare four
shores therefore needs a separately written doubled completion.  Formula
(1.5a), not the bare modulo-four colouring, is what licenses suspension
for the proper growing embedding considered here.

The possible displacement patterns, ignoring frozen coordinates between
\(a,b,c,d\), are

\[
\begin{array}{c|c}
\text{prefix position}&\sigma_kp_i+p_i\\ \hline
i\le a&0\\
a<i\le b&\alpha(k)\delta\\
b<i\le c&\alpha(k)\delta+\beta(k)\gamma\\
c<i\le d&\beta(k)\gamma\\
d<i&0.
\end{array}                                           \tag{1.6}
\]

The one-active intervals are legal by (1.3): they fix or exchange each
corresponding label pair.  Only the overlapping middle interval imposes a
new equation.

## 2. Twelve-state theorem

Fix a coset \(Q=k+\langle\delta,\gamma\rangle\), and identify it with
\(\mathbb F_2^2\).  Pair constancy (1.3) has exactly the form (0.3), where
each of \(U,V\) is one of the four Boolean functions on one bit.
Equation (1.6) gives the middle map (0.4).

Two points on the same horizontal line cannot collide: their first output
coordinates differ.  Two points on the same vertical line cannot collide:
their second output coordinates differ.  The only possible collisions are
the diagonals.  Direct subtraction gives

\[
\begin{aligned}
 F(0,0)=F(1,1)
 &\iff U(0)+U(1)=V(0)+V(1)=1,\\
 F(1,0)=F(0,1)
 &\iff U(0)+U(1)=V(0)+V(1)=1.                    \tag{2.1}
\end{aligned}
\]

Hence both diagonal collisions occur together, exactly in the case
excluded by (0.5).  In every other case all four images are distinct.
The antipodal half has the same displacement equation.  This proves
necessity and sufficiency for the literal exact owner factor.

There are eight legal states with \(U\) constant and \(V\) arbitrary.
There are four further legal states with \(U\) nonconstant and \(V\)
constant.  Thus the count is twelve.  Choices on distinct cosets of
\(\langle\delta,\gamma\rangle\) are independent, proving (0.6).
They give distinct rooted factors because phase zero fixes the row root
\(k\), while the pair \((\alpha(k),\beta(k))\) uniquely determines the
Klein shore of that row.

There is also an explicit literal installation.  If \(U\) is constant,
the \(A\)-choice is constant on the whole label plane.  After it is
installed, the current row field is \(\gamma\)-invariant, so the two
\(\gamma\)-pair \(B\)-components may be selected according to the
arbitrary function \(V\).  If \(V\) is constant, reverse the roles:
install \(B\) first and then select the two \(\delta\)-pair
\(A\)-components according to \(U\).  These are precisely the two
branches in (0.5).

Different label planes have disjoint unions of base cycles.  One may
therefore choose the installation order independently on each plane.
Every intermediate packet state and the final global union are exact
owner factors.

### 2.1 Reconciliation with the nonlinear complete-mapping theorem

This extra twelve-state condition does not contradict Theorem 4.1 of the
source report.  In that theorem one fixes a single cube owner \(x\).
Its base outgoing direction lies either in the \(A\)-wire or in the
\(B\)-wire.  The one-step column map therefore sees only \(\alpha\), or
only \(\beta\), and the separate pair invariances suffice.

Here one chooses a complete cyclic shore for each syndrome-cycle label.
At the middle prefix the path has crossed one endpoint of both wires, so
the accumulated owner displacement sees \(\alpha\) and \(\beta\)
simultaneously.  Exactness is then the four-point Latin condition (0.5).
Thus a nonlinear parity-complete one-step map does not by itself license
an arbitrary product of the two complete-cycle braid fields.

### 2.2 No nonconstant chart has a same-owner \(AB\)-opposite

Let \((U,V)\) and \((U',V')\) be two legal charts on the same label
plane.  Suppose their outgoing physical directions satisfy

\[
 d'(z)=AB\,d(z)
 \qquad\text{for every physical owner }z.             \tag{2.2}
\]

Then both \(U,V\) are constant, and the second chart is their pointwise
complement.

Before the \(a\)-edge no active pair has been cut, so both factors assign
the same row label to a physical owner.  Since the \(a\)-direction is
\(A\)-controlled, (2.2) forces

\[
                         U'(y)=1+U(y).                \tag{2.3}
\]

Immediately before the \(b\)-edge, the prefix has cut the \(A\)-pair but
not the \(B\)-pair.  The two phase maps differ by \((1,0)\), so their row
labels at one physical owner differ by \(\delta\).  Equality of the
required \(B\)-directions gives

\[
                         V'(x+1)=1+V(x).              \tag{2.4}
\]

Immediately before the \(d\)-edge, only the \(B\)-pair is cut.  Applying
the same argument from the other side gives

\[
                         V'(x)=1+V(x).                \tag{2.5}
\]

Equations (2.4)--(2.5) force \(V(x+1)=V(x)\), so \(V\) and \(V'\) are
constant complements.  At the middle boundary before the \(c\)-edge,
the two row labels then differ in the \(y\)-coordinate.  Equality of the
required \(A\)-directions, together with (2.3), forces
\(U(y+1)=U(y)\).  Thus \(U,U'\) are also constant complements.

Conversely, constant complementary charts are two global Klein shores,
for which the same-owner \(AB\) relation is the source theorem.  Therefore
the fixed-point-free opposite is available on the four constant charts
only.  The high-entropy twelve-state factor menu has no nonconstant
same-owner fixed-point-free partner within the four-shore ansatz.

## 3. Exact action distribution

Let

\[
 u=U(0)+U(1),\qquad v=V(0)+V(1)                    \tag{3.1}
\]

as ordinary integer sums, so \(u,v\in\{0,1,2\}\).  Among the four labels
of \(Q\), exactly \(2u\) use the \(A\)-twist and exactly \(2v\) use the
\(B\)-twist.  One twist interchanges two direction positions in each
half of a row and therefore changes four directed successor edges.
Consequently

\[
                         E_Q=8(u+v).                 \tag{3.2}
\]

The legal \((u,v)\) multiplicities are

\[
\begin{array}{c|ccccccccc}
(u,v)&(0,0)&(0,1)&(0,2)&(1,0)&(1,2)&
       (2,0)&(2,1)&(2,2)\\ \hline
\text{multiplicity}&1&2&1&2&2&1&2&1.
\end{array}                                           \tag{3.3}
\]

Collecting equal values of \(u+v\) gives (0.7).  The set of twelve states
is symmetric under complementing either shore bit after interchanging the
corresponding constant/nonconstant chart, and direct summation gives

\[
 \mathbb E u=\mathbb E v=1,\qquad
 \mathbb E E_Q=16.                                   \tag{3.4}
\]

The maximum \(E_Q=32\) is the constant \(AB\)-state.

## 4. Composition on disjoint slabs

Take \(t\) coordinate quadruples

\[
                         a_j<b_j<c_j<d_j             \tag{4.1}
\]

whose coordinate supports and closed prefix spans are pairwise disjoint.
Assume both equal-column equations (1.1) in every quadruple.  For block
\(j\), choose independently one of the twelve legal charts on every
coset of

\[
 H_j=\langle e_{a_j}+e_{c_j},\,
                  e_{b_j}+e_{d_j}\rangle.            \tag{4.2}
\]

At a given phase, at most one block has a nonzero prefix displacement.
Its phase map is either a one-pair exchange or the legal four-point map
(0.4).  Hence all phase maps are permutations, so all block choices
compose into one exact isometric factor.  Coordinate supports are
disjoint, so the final row shore records every block chart injectively.
This proves (0.8).

For the standard parity-alternating syndrome map,
\(\Psi(e_{2q})\) is independent of \(q\).  The quadruples (0.9) therefore
satisfy (1.1).  Their prefix spans lie in the disjoint coordinate slabs
\([8j,8j+6]\).  With

\[
 N={2^h\over2h},\qquad t={h\over8},                 \tag{4.3}
\]

formula (0.8) becomes (0.10).

In one block, the maximum changes eight directed edges per row and the
uniform legal mean changes four.  Multiplying by \(t=h/8\) gives,
respectively, \(h\) and \(h/2\) changed edges per \(2h\)-edge row.  This
proves the exact densities \(1/2\) and \(1/4\).

For general \(t\), the same calculation gives \(8t\) and \(4t\)
changed edges per row, proving (0.8a).  If a separate syndrome
presentation and phase-slab atlas achieves \(t=h/4\), this specializes to
(0.8b).

There is a useful embedding caveat.  Four consecutive directions with
columns paired as \((a,c)\) and \((b,d)\) have zero total syndrome.  If
they formed a proper consecutive block of a longer syndrome-transversal
order, the prefix syndrome would repeat at the end of that block.  Hence a
growing factor cannot simply be tiled by isolated consecutive copies of
the bare \(Q_4\) table.  Frozen intervening directions, as in (0.9), or a
different nonlocal carrier are necessary.

## 5. What fixed-point-free does and does not remove

Let \(S=AB\).  On one active quartet, \(S\) has no fixed coordinate.
Therefore any lower bound which used the two fixed directions of the
one-bit \(B\)-shore is invalid for the opposite pair \((I,S)\) on that
quartet.  If a future atlas covers every ambient coordinate by such
wires, its global opposite permutation can be fixed-point-free.

This does not remove the fixed-global-shore syndrome kernel.  If one
chooses the same \(S\) on every syndrome cycle, then translation by
\(k\in K_0\) still leaves its consecutive direction support unchanged.
For a completed support \(J\), every

\[
 e\in E\cap K\cap\mathbb F_2^J                   \tag{5.1}
\]

gives the usual aligned trace collision

\[
                         p'=p+e,\qquad y'=y+Se.      \tag{5.2}
\]

The dimension lower bound

\[
 \dim(E\cap K\cap\mathbb F_2^J)
                  \ge |J|-\log_2h-1                 \tag{5.3}
\]

does not mention fixed points of \(S\).  Thus the constant \(AB\)-shore
does not evade it.

Nonconstant legal row fields can destroy the translation identity used in
(5.2), so (5.1) must not be claimed as an invariant of all twelve-state
factors.  The surviving universal obstruction is instead the wire frame.
Every allowed shore preserves each pair \(\{a,c\}\), \(\{b,d\}\).
For any completed \(d\)-support \(J\),

\[
 \#\{\sigma J:\sigma\text{ is an allowed row shore}\}
                         \le2^d.                     \tag{5.4}
\]

There are at most \(h\) cyclic base intervals.  Appending the two outside
bit strings to an aligned paired trace gives at most

\[
                         h\,2^d\,2^{2(h-d)}           \tag{5.5}
\]

codes on \(2^{2h-1}\) even-context starts.  Therefore the distinct-code
proportion is at most

\[
                         {2h\over2^d}.                \tag{5.6}
\]

This tends to zero whenever \(d-\log_2h\to\infty\).

In the guaranteed atlas (0.9), only even positions belong to active
wires; every odd direction is fixed by every row shore.  A consecutive
base interval of length \(d\) contains at most \(\lceil d/2\rceil\)
active positions.  Replacing \(2^d\) in (5.5) by
\(2^{\lceil d/2\rceil}\) gives (0.11).

Thus:

* local fixed-coordinate invisibility is removed at the \(AB\) corner;
* only the four constant charts have a same-owner fixed-point-free
  opposite;
* a globally fixed shore still has the full syndrome-kernel collision;
* row-dependent legal shores may break that particular kernel;
* every fixed-frame \(A/B\) composition retains the completed-support
  entropy obstruction; and
* the standard guaranteed embedding still fixes half the ambient
  directions and satisfies the sharper half-rate trace ceiling.

## 6. Exact implication boundary

Proved:

* the complete twelve-state row-label classification for one four-shore
  quartet;
* exact owner failure, with two collisions and two omissions, in the four
  excluded states;
* \(12^{N/4}\) exact states and the full action distribution for one
  quartet;
* a literal disjoint-slab composition theorem and the standard guaranteed
  count \(12^{2^h/64}\);
* maximum changed-edge density \(1/2\) and uniform legal mean \(1/4\) in
  that guaranteed atlas; and
* the exact separation between the removed fixed-coordinate obstruction
  and the surviving syndrome-kernel/fixed-wire trace obstructions.

Not proved:

* a full-coordinate quartet atlas in the standard syndrome presentation;
* a transverse layer which changes the wire frame;
* a Beneš network with rate-one completed-support entropy;
* equality or small discrepancy of protected lower/upper collars; or
* coefficient one.

The first remaining physical object is a common-owner associator which
changes the wire pairing between successive four-shore layers while
retaining the row-label Latin equations.  More shores inside the same
fixed Klein frame cannot remove (5.4).
