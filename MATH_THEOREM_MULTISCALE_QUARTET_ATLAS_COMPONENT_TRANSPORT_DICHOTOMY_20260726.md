# Multiscale quartet atlases: exact component--transport dichotomy

Date: 2026-07-26

Method: pure mathematics only.  The local consecutive-trace compiler is
assumed exact, as permitted.  No probabilistic marginal product is used.

## 0. Verdict

Alternating quartet partitions at dyadic scales can generate a
fractional scale catalogue with constant crossing capacity across every
positive-density coordinate cut.  They cannot turn that catalogue into a
component-adaptive moving-frame factor while retaining subexponential
common-owner components.

The obstruction is exact and precedes the trace compiler.

Assume first that the \(2m\) physical coordinates are indexed by

\[
                         V=\mathbb F_2^\ell,\qquad |V|=2m.       \tag{0.1}
\]

For every nonzero \(v\in V\), let

\[
                         M_v=\{\{x,x+v\}:x\in V\}/2             \tag{0.2}
\]

be the translation perfect matching.  Let \(S\subseteq V\setminus\{0\}\)
be the set of scales/directions admitted by the atlas and put

\[
                         U=\langle S\rangle.                    \tag{0.3}
\]

The union graph of the matching atlas is the Cayley graph
\(\operatorname {Cay}(V,S)\).  Its coordinate components are exactly the
cosets of \(U\).  By the exclusion-process occupancy theorem, its
common-owner components on the middle layer are exactly

\[
 \boxed{
 \mathcal U_{\boldsymbol\kappa}
 =\left\{X\in\tbinom Vm:
       |X\cap(c+U)|=\kappa_c\quad(c\in V/U)\right\}.} \tag{0.4}
\]

The local three-shore associator does not alter (0.4).  On every affine
two-flat

\[
                         x+\langle v,w\rangle,                  \tag{0.5}
\]

its three shores are the translation matchings in directions
\(v,w,v+w\); the reservoir lift turns the six rank-two owners into the
24-owner associator without changing the coordinate union graph.

There are now only two cases.

1. If \(U\ne V\), choose \(0\ne a\in U^\perp\).  The half-density
   coordinate set
   \[
                         R_a=\{x:a\cdot x=0\}                    \tag{0.6}
   \]
   is crossed by no edge of any admitted matching.  Every atlas move
   preserves \(|X\cap R_a|\).  Thus a positive-density projection survives
   exactly.

2. If \(U=V\), the union graph is connected.  Equation (0.4) has only the
   middle layer itself:
   \[
                         \mathcal U_{(m)}=\binom Vm.             \tag{0.7}
   \]
   Hence an exact cell-recoupling selector has one global common-owner
   component.  It cannot choose different matching shores on different
   owner regions.  After it chooses one global perfect matching \(M\),
   take \(R_M\) to be the union of any half of the edges of \(M\).  Then
   \(|R_M|=|V|/2\) and no selected matching direction crosses
   \(R_M\mid(V\setminus R_M)\).

This proves the sharp dichotomy

\[
\boxed{
\begin{array}{c}
\text{all half-density linear projections are movable}\\
\Longrightarrow U=V\\
\Longrightarrow\text{one common-owner component of size }
                 \binom{2m}m\\
\Longrightarrow\text{one globally selected matching, which itself has a
zero-crossing half cut.}
\end{array}}                                         \tag{0.8}
\]

There is also a scale-free component-size obstruction.  For *every*
nonempty perfect-matching atlas and a uniformly random middle owner \(X\),

\[
 \boxed{
 |\mathcal U(X)|\ge2^{m/3}}                          \tag{0.9}
\]

with probability \(1-o(1)\).  Indeed, one fixed matching cell contained
in \(\mathcal U(X)\) already has that size.  Therefore no perfect-matching
status-cell atlas can have \(2^{o(m)}\) common-owner components on
\((1-o(1))\binom{2m}m\) owners.

On the positive geometric side, one may choose
\(|S|=O(\ell)\) so that \(\operatorname {Cay}(V,S)\) has a constant
spectral gap.  Then, for every
\(\eta\le |R|/|V|\le1-\eta\),

\[
 {1\over|S|}\sum_{v\in S}
 {e_{M_v}(R,V\setminus R)\over |V|/2}
 \ge c_\eta>0.                                      \tag{0.10}
\]

Consequently a uniformly mixed scale catalogue has the edge capacity
needed for \(\Omega_\eta(q)\) cut transport in a Gaussian \(q\)-window.
Turning that fractional capacity into one literal cycle factor still
requires the directions from different matchings to be assembled into
disjoint physical pairs.  Equation (0.8) says what happens to the
status-cell recoupling route: the expanding scale family is connected and
admits no nontrivial componentwise matching selector.

Thus the requested three properties

\[
\begin{array}{l}
\text{(i) exact common-owner recoupling,}\\
\text{(ii) }2^{o(m)}\text{ components on almost all owners,}\\
\text{(iii) }\Omega(q)\text{ transport across every positive-density cut}
\end{array}
\]

are mutually incompatible in the moving-perfect-matching/24-owner
associator model.

The two-sign occurrence-capacity Hall theorem is therefore not obtained.
The surviving invariant is the coset occupancy vector in (0.4); eliminating
all of its positive-density projections forces the global component
(0.7).  In that connected case the globally selected matching is subject
to the exact fixed-frame Gaussian Hall cut, so both signs have
\(\Omega(W)\) deficiency.  A positive construction must leave the
status-cell recoupling model--for example by using exterior-moving
components whose owner overlap is not generated by matching-edge exclusion
moves.

## 1. Alternating quartet shores are translation matchings

Fix independent \(v,w\in V\).  On every affine two-flat (0.5), the three
perfect matchings are

\[
\begin{aligned}
 &\{\{y,y+v\}:y\in x+\langle v,w\rangle\}/2,\\
 &\{\{y,y+w\}:y\in x+\langle v,w\rangle\}/2,\\
 &\{\{y,y+v+w\}:y\in x+\langle v,w\rangle\}/2.
                                                               \tag{1.1}
\end{aligned}
\]

They are precisely the three shores of the quartet associator.  Adding
the four-state reservoir square replaces every six-owner rank-two
associator by one 24-owner equal-dimensional component.  It changes
neither the special-coordinate edges in (1.1) nor their connected union.
Reservoir pairs may be kept inside the same \(U\)-cosets.  If reservoirs
are instead reused across cosets, they only add union-graph edges, enlarge
\(U\), and strengthen the connectedness side of the dichotomy.

Accordingly, allowing associators between scale directions in \(S\)
enlarges the union graph by directions in their linear span and never
beyond \(U=\langle S\rangle\).

## 2. Exact common-owner components

### Theorem 2.1 (Cayley occupancy classification)

For the atlas generated by \(S\), two middle owners \(X,Y\) lie in one
cell-overlap component if and only if

\[
 |X\cap(c+U)|=|Y\cap(c+U)|
 \qquad\text{for every }c\in V/U.                   \tag{2.1}
\]

#### Proof

Every matching edge has both endpoints in one \(U\)-coset.  Orientation
flips on split matching edges therefore preserve every count in (2.1).

Conversely, the Cayley graph on each coset \(c+U\) is connected because
\(S\) spans \(U\).  The simple exclusion graph on the \(k\)-subsets of a
connected graph is connected: along a spanning tree, move particles from
the leaves toward a fixed canonical \(k\)-set.  Every elementary particle
move is an orientation flip on an edge belonging to one admitted matching.
Apply this independently in every coset. \(\square\)

Theorem 2.1 is unchanged if the transitions among the matchings are
implemented only through the 24-owner three-shore associator: its three
local shores generate exactly the same exclusion edges on every
two-flat.

### Corollary 2.2 (exact selectors)

For every admissible occupancy vector
\(\boldsymbol\kappa=(\kappa_c)_{c\in V/U}\), one may choose one matching
\(M_{\boldsymbol\kappa}\) and factor all of its status cells inside
\(\mathcal U_{\boldsymbol\kappa}\).  These choices give an exact middle
factor if and only if they are constant on every set (0.4).

If \(U=V\), this is one global choice.

## 3. Dyadic hierarchy

Take a basis \(e_1,\ldots,e_\ell\) of \(V\), and let

\[
                         U_k=\langle e_1,\ldots,e_k\rangle.      \tag{3.1}
\]

Activating quartet recouplings through the first \(k\) dyadic scales gives
coordinate components equal to the \(2^{\ell-k}\) cosets of \(U_k\),
each of size \(2^k\).  The owner components are

\[
 \left\{X:|X\cap(c+U_k)|=\kappa_c
                    \quad(c\in V/U_k)\right\}.       \tag{3.2}
\]

Activating scale \(k+1\) merges the two child cosets in every
\(U_{k+1}\)-coset.  On the owner side it forgets the two child occupancies
and retains only their sum.  This is exactly the component merger induced
by the three-shore quartet associator.

If the hierarchy stops at \(k<\ell\), choose
\(0\ne a\in U_k^\perp\).  The projection \(R_a\) in (0.6) is a union of
whole dyadic coordinate components and no active direction crosses it.
If the hierarchy reaches \(k=\ell\), all coordinate and owner components
merge.  Thus no stopping scale supplies both nontrivial component
adaptivity and transport across every dyadic half cut.

The same conclusion holds for a non-laminar collection of scales: replace
\(U_k\) by their linear span.

## 4. Typical owner components are necessarily exponential

Fix any admitted matching \(M\).  For a middle owner \(X\), let

\[
 s_M(X)=\#\{e\in M:|X\cap e|=1\}                    \tag{4.1}
\]

be its number of split matching edges.  Its \(M\)-status cell has

\[
                         |C_M(X)|=2^{s_M(X)}.        \tag{4.2}
\]

Every matching cell is contained in the atlas component
\(\mathcal U(X)\), so

\[
                         |\mathcal U(X)|\ge2^{s_M(X)}.           \tag{4.3}
\]

For uniform \(X\in\binom Vm\),

\[
 \mathbb E s_M(X)={m^2\over2m-1}={m\over2}+O(1),
 \qquad
 \operatorname {Var}s_M(X)=O(m).                    \tag{4.4}
\]

Chebyshev gives

\[
 \Pr\{s_M(X)<m/3\}=O(1/m)=o(1).                     \tag{4.5}
\]

Equations (4.3)--(4.5) prove (0.9).

This argument uses only one matching in the atlas.  Adding scales can
only merge status cells and enlarge their common-owner components.

## 5. A cut-diffuse multiscale family exists

The preceding obstruction is not a failure of multiscale geometry.  It
is a compatibility failure between that geometry and componentwise exact
recoupling.

Choose \(L=C\ell\) vectors \(v_1,\ldots,v_L\) independently and uniformly
from \(V\).  With probability \(1-o(1)\) they are nonzero and distinct;
we restrict to that event.  For a fixed nonzero linear functional \(a\),
the bits

\[
                         a\cdot v_1,\ldots,a\cdot v_L             \tag{5.1}
\]

are independent fair bits.  Chernoff gives

\[
 \Pr\left\{\left|
 {1\over L}\#\{i:a\cdot v_i=1\}-{1\over2}\right|>{1\over4}
 \right\}\le2e^{-L/24}.                              \tag{5.2}
\]

For sufficiently large absolute \(C\), a union bound over the
\(2^\ell-1\) nonzero \(a\)'s gives a deterministic set \(S\) such that

\[
 {1\over4}\le {1\over L}\#\{v\in S:a\cdot v=1\}
 \le {3\over4}                                      \tag{5.3}
\]

for every nonzero \(a\).  In particular \(S\) spans \(V\).

The normalized adjacency eigenvalue belonging to character
\(\chi_a(x)=(-1)^{a\cdot x}\) is

\[
 \lambda_a={1\over L}\sum_{v\in S}(-1)^{a\cdot v}.  \tag{5.4}
\]

Equation (5.3) gives \(|\lambda_a|\le1/2\) for every nonconstant
character.  Hence the Cayley multigraph has spectral gap at least \(1/2\).
The expander-mixing identity, or the elementary variance decomposition in
the character basis, gives

\[
 {1\over L}\sum_{v\in S}
 e_{M_v}(R,V\setminus R)
 \ge {1\over2}\rho(1-\rho)|V|,                      \tag{5.5}
\]

up to the harmless convention of counting each matching edge once, where
\(\rho=|R|/|V|\).  Thus (0.10) holds uniformly for
\(\rho\in[\eta,1-\eta]\).

For one doubled-permutation word on \(h\) physical directions, a direction
occurrence belongs to exactly \(q\) cyclic \(q\)-windows.  Hence, if a
literal factor could assemble disjoint directions whose empirical
scale/cut incidence realizes the catalogue average in (5.5), its exact
occurrence average of cut-crossing directions would be
\(\Omega_\eta(q)\).  Equation (5.5) is therefore the required geometric
capacity statement, not a claim that the status-cell selector has already
compiled those overlapping matchings into one factor.

But (5.3) implies \(U=V\), so Theorem 2.1 turns the entire middle layer
into one owner component.  The scale mixture cannot be selected
independently on smaller owner regions by status-cell recoupling.  A
single globally selected \(M_v\), or any single hybrid perfect matching,
again has the zero-crossing cut obtained by taking a union of half of its
matching edges.

## 6. Exact projection invariant and the Hall boundary

When \(U\ne V\), the occupancy vector

\[
                         \pi_U(X)=
 (|X\cap(c+U)|)_{c\in V/U}                          \tag{6.1}
\]

is invariant under every owner edge, every matching-status cell, every
three-shore associator, and every tensor or recursive composition which
uses only directions in \(U\).

For \(a\in U^\perp\setminus\{0\}\), the coarser coordinate count

\[
                         |X\cap R_a|                \tag{6.2}
\]

is a positive-density projection of (6.1), and no physical direction
crosses its coordinate cut.

This is the surviving statewise projection invariant requested in the
problem.  It blocks the proposed assertion that every Gaussian window
moves \(\Omega(q)\) coordinates across every positive-density cut.

It does not, by itself, prove a physical target Hall deficit after an
arbitrary exact trace compiler: lower intersections and upper unions can
change their counts inside each side of the cut.  Hence it would be
incorrect to claim the two-sign Hall inequalities fail solely from
(6.2).

When \(U=V\), the projection invariant disappears, but exact recoupling
has only the global component (0.7).  The selected status-cell factor is
based on one global perfect matching \(M\), and the union \(R_M\) of half
its edges is a statewise half-density zero-crossing projection.  Thus the
proposed \(\Omega(q)\)-across-every-cut property fails even after
connectedness has removed the fixed linear projections.

There is also an exact occurrence-capacity Hall cut in this connected
case.  Classify middle owners and signed targets by their status relative
to \(M\).  The relevant fibre counts are

\[
\begin{aligned}
 V_f&={m!\over f!^2(m-2f)!}\,2^{m-2f},\\
 T_{f,q}&={m!\over f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.
                                                               \tag{6.3}
\end{aligned}
\]

Every \(M\)-internal factor has at most \(V_f\) occurrences available for
the \(T_{f,q}\) targets of type \(f\).  Hence either sign misses at least

\[
 \boxed{
 D_{m,q}=\sum_f(T_{f,q}-V_f)_+.}                    \tag{6.4}
\]

At \(q=A\sqrt m+o(\sqrt m)\), the hypergeometric local central limit
calculation gives

\[
 {D_{m,q}\over W}\longrightarrow
 e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0.                   \tag{6.5}
\]

All consecutive directions of a status-cell factor are edges of its
globally selected \(M\), so the local trace compiler remains inside this
cut.  Thus the connected multiscale atlas violates both lower and upper
occurrence-capacity Hall inequalities by \(\Theta_A(W)\).

For \(U\ne V\), the occupancy invariant (6.1) and the zero-crossing linear
cut (6.2) survive.  A zero-crossing owner cut alone is not automatically
a physical target deficiency after intersections and unions are taken
inside its two sides, so no stronger Hall claim is made in that case.
The projection invariant already disproves the transport hypothesis
required by the proposed hierarchical Hall proof.

Accordingly the exact conclusion is a no-go for the requested
*simultaneous* component and transport properties, not a proof that every
possible exterior-moving factor fails Hall.  The remaining escape must
use components whose owner-overlap relation is not the exclusion process
of a fixed family of perfect matchings.
