# The exact fused configuration hypergraph and a linear-scale literal carrier cut

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

This note does two things.

First, it gives the smallest exact hypergraph formulation of the
all-depth, two-sign home problem.  Its matching objective is precisely
the missing-shadow objective, not CPCR.  A hyperedge consists of one
fused packet group together with an arbitrary bundle contained in one
complete legal state of that group.  A matching saturating all target
tokens is equivalent to one common legal atlas state covering every
target; a matching missing \(o(W)\) target vertices is equivalent to the
constant-one target.

Second, it gives a literal physical Hall cut against the conclusions of
the patched linear-scale theorem **without** an additional
projection-free hypothesis.  There is a legal choice

\[
 {m\over512}<R\le {m\over256},\qquad
 d=4\left\lceil {5\over2}\log _2m\right\rceil ,
\]

with all active axes contained in a fixed carrier \(E\) of size \(m/2\),
such that:

* the owner leave is \(e^{-\Omega(m)}W\);
* every packet has the diverse-order \(C_{2R}\)-factor;
* every \(q\le H=o(m)\) window is geodesic and packet-trace injective;
* every retained parent cell is a literal rainbow;
* signs are fused by complementation; but
* at every fixed \(q=A\sqrt m+O(1)\), \(A>0\), the lower configuration
  hypergraph has an explicit target cut of deficiency
  \(\Omega_A(W)\).

No choice of compiler conjugates, no correlation between different
packets, and no compound home assignment can cross this cut, because
every physical move fixes the exterior \(E^c\).

This is not a counterexample to an atlas which is required to move
coordinates across every positive-density projection.  It is a
counterexample to deriving the unrestricted configuration Hall theorem
from linear \(R\), logarithmic blocks, parent-cell rainbows, and fused
signs alone.  The missing positive input is therefore an explicit
projection-free all-cuts theorem at the level of complete compiler
states.

## 1. Fused choice groups and target tokens

Let \(\mathfrak G\) be the set of atomic fused choice groups.  A group
\(g\) contains a packet \(P\), its complementary packet \(P^c\), and the
requirement that their compiler labels are conjugate so that

\[
                         P_{\rm succ}(X^c)=P_{\rm succ}(X)^c.
                                                               \tag{1.1}
\]

Let \(\Omega_g\) be the complete finite menu of legal states of \(g\).
It includes the packet axes, any allowed cross-parent recoupling internal
to the group, the compiler conjugate, and the common orientation data.

The protected target-token set is

\[
 {\cal U}
 =\{(q,\varepsilon,T):
       1\le q\le H,\ \varepsilon\in\{-,+\},\
       T\in\tbinom{[2m]}{m+\varepsilon q}\}.          \tag{1.2}
\]

Here \(m+\varepsilon q\) means \(m-q\) for the lower sign and \(m+q\)
for the upper sign.  For \(\omega\in\Omega_g\), let

\[
                         J_g^\omega\subseteq{\cal U}            \tag{1.3}
\]

be the set of target tokens covered by that complete state.  Multiplicity
inside one group is discarded in (1.3), because the missing-shadow
objective asks only whether a token is covered.

## 2. The smallest exact home-bundle hypergraph

Define a hypergraph \({\cal K}\) on

\[
                         V({\cal K})=\mathfrak G\dot\cup{\cal U}.
                                                               \tag{2.1}
\]

For every \(g\in\mathfrak G\), every \(\omega\in\Omega_g\), and every
bundle \(B\subseteq J_g^\omega\), put in the hyperedge

\[
                         e(g,\omega,B)=\{g\}\dot\cup B.          \tag{2.2}
\]

The empty bundle is allowed.

### Theorem 2.1 (exact home matching equivalence)

For \(E\ge0\), the following are equivalent.

1. There is one state \(\omega_g\in\Omega_g\) for every fused group such
   that at most \(E\) target tokens are uncovered:

   \[
        \left|{\cal U}\setminus\bigcup_gJ_g^{\omega_g}\right|
        \le E.                                                   \tag{2.3}
   \]

2. The hypergraph \({\cal K}\) has a matching which saturates every group
   vertex and all but at most \(E\) target vertices.

#### Proof

Assume (2.3).  Assign every covered target token to one selected group
which covers it.  Let \(B_g\) be the bundle assigned to \(g\).  The
bundles are pairwise disjoint and \(B_g\subseteq J_g^{\omega_g}\), so
the edges \(e(g,\omega_g,B_g)\) form the desired matching.

Conversely, a matching saturating every group chooses one edge
\(e(g,\omega_g,B_g)\) for that group.  Its target bundles are disjoint
and every saturated target belongs to the selected state
\(J_g^{\omega_g}\).  Hence the selected states cover every saturated
target, proving (2.3). \(\square\)

The bundle coordinate in (2.2) is essential.  If one used only the edge
\(\{g\}\cup J_g^\omega\), ordinary hypergraph matching would forbid
overlap between two selected state images.  Such overlaps are legal and,
when \(G>N_q\), partly forced.  The bundles remember only the home
assignment and impose no false no-overlap condition on nonhome
occurrences.

## 3. Missing shadows are not CPCR

For selected states \(\boldsymbol\omega=(\omega_g)_g\), let

\[
 C_t(\boldsymbol\omega)
 =\#\{g:t\in J_g^{\omega_g}\}.                       \tag{3.1}
\]

Let \(\ell_t(\boldsymbol\omega)\) be the actual packet-occurrence load;
inside one fused group it may count the same token twice.  The two loads
have the same zero set:

\[
                         C_t=0\quad\Longleftrightarrow\quad\ell_t=0.
                                                               \tag{3.1a}
\]

The authoritative objective represented by Theorem 2.1 is

\[
\boxed{
 {\mathfrak H}(\boldsymbol\omega)
 =\sum_{t\in{\cal U}}(1-\ell_t(\boldsymbol\omega))_+
 =\left|{\cal U}\setminus\bigcup_gJ_g^{\omega_g}\right|.}
                                                               \tag{3.2}
\]

It ignores every multiplicity above one.

CPCR instead penalizes, at each colour \(c=(q,\varepsilon)\), the
quadratic floor excess

\[
 \Phi_c
 =\sum_T(\ell_c(T)-a_c)(\ell_c(T)-a_c-1),\qquad
 a_c=\left\lfloor{G\over N_q}\right\rfloor.           \tag{3.3}
\]

CPCR implies a small missing hinge, but the converse is false.  For
example, loads

\[
                         (K,1,1,\ldots,1),\qquad K\to\infty,
\]

have zero missing mass and arbitrarily large quadratic excess.  Thus a
perfect matching in \({\cal K}\) proves exactly what constant one needs;
it does not assert CPCR.

## 4. Exact configuration Hall and augmenting forms

The fractional reserve-\(E\) relaxation of Theorem 2.1 is feasible if
and only if, for every nonnegative target weight \(y\),

\[
\boxed{
 \sum_{g\in\mathfrak G}
       \max_{\omega\in\Omega_g}\sum_{t\in J_g^\omega}y_t
 +\rho_E(y)
 \ge\sum_{t\in{\cal U}}y_t,}                         \tag{4.1}
\]

where \(\rho_E(y)\) is the sum of the \(E\) largest weights.  This is the
support-function separation theorem for the product of the group
simplices.  It is necessary for the integral matching in \({\cal K}\),
but it is not sufficient without an integral decomposition theorem for
the bundle hypergraph.

There is also an exact, fully integral exchange formula.  Fix a selected
state vector and a set \(S\subseteq\mathfrak G\) of groups to be changed.
Remove their current images and put

\[
\begin{aligned}
 Z_S&={\cal U}\setminus
       \bigcup_{g\notin S}J_g^{\omega_g},\\
 U_S^0&=\bigcup_{g\in S}J_g^{\omega_g},\\
 U_S^1&=\bigcup_{g\in S}J_g^{\omega'_g}.
\end{aligned}                                                   \tag{4.2}
\]

Then

\[
\boxed{
 \Delta_S{\mathfrak H}
 =|Z_S\cap U_S^0|-|Z_S\cap U_S^1|.}                \tag{4.3}
\]

Thus an augmenting configuration is exactly a group set \(S\) and new
states covering more of the common zero set than the old states.  Formula
(4.3) contains intersections of every order.  Pair codegrees, CPCR
derivatives, and bounded-order alternating paths do not determine it.

## 5. A legal linear carrier atlas

Let \(E\subseteq[2m]\) be a union of complete rank-twisted macroblocks
with

\[
                         e:=|E|={m\over2}+O(d).                  \tag{5.1}
\]

Choose the largest admissible

\[
                         R=8\cdot2^r\le {m\over256}.             \tag{5.2}
\]

Then

\[
                         {m\over512}<R\le {m\over256},           \tag{5.3}
\]

so \(R=\Theta(m)\), and \(H\le R/4-1\) eventually whenever \(H=o(m)\).

There are

\[
                         n_E={e\over2}={m\over4}+O(d)
                                                               \tag{5.4}
\]

adaptive matching pairs inside \(E\).  By the exact aggregate enumerator,
their actual split count under the unconditioned Boolean-cube law is

\[
                         S_E\sim\operatorname{Bin}(n_E,1/2).
                                                               \tag{5.5}
\]

Since \(16R\le m/16\), while
\(\mathbb ES_E=m/8+O(d)\), Hoeffding gives

\[
                         \Pr(S_E<16R)\le e^{-m/32+o(m)}.         \tag{5.6}
\]

Conditioning on the middle rank costs only \(O(\sqrt m)\), so the middle
owners without \(16R\) split axes in \(E\) have size
\(e^{-\Omega(m)}W\).

On every remaining product cell, take the first \(16R\) flexible axes
inside \(E\), divide them into \(R\) groups of sixteen, and use the exact
complement-equivariant \(Q_{16}\) matching product.  Install the
linear-scale diverse-order compiler in every resulting \(Q_R\)-packet.
All conclusions of the patched local theorem remain literal:

* exact owner packetization outside the exponential leave;
* cycles \(C_{2R}\) of length \(\Theta(m)\);
* trace injectivity through every \(q\le H\);
* exact parent-cell rainbows;
* exact laminar depth flags; and
* complement-fused signs.

But every active physical exchange is contained in \(E\).  Therefore

\[
                         X\cap E^c=P^i(X)\cap E^c               \tag{5.7}
\]

for every owner, every time \(i\), and every compiler or correlated atlas
state.

## 6. The exterior-fibre Hall cut

Fix

\[
                         q=A\sqrt m+O(1),\qquad A>0.             \tag{6.1}
\]

For \(Y\subseteq E^c\), define the middle-owner and lower-target fibres

\[
\begin{aligned}
 {\cal O}_Y&=\{X\in\tbinom{[2m]}m:X\cap E^c=Y\},\\
 {\cal T}_Y&=\{T\in\tbinom{[2m]}{m-q}:T\cap E^c=Y\}.
\end{aligned}                                                   \tag{6.2}
\]

Put \(t=m-q-|Y|\).  Ignoring the harmless \(O(d)=o(\sqrt m)\)
rounding in (5.1), so that \(e=m/2\), their exact cardinalities are

\[
                         |{\cal T}_Y|=\binom et,\qquad
                         |{\cal O}_Y|=\binom e{t+q}.             \tag{6.3}
\]

By (5.7), every lower target emitted in \({\cal T}_Y\) must come from an
owner in \({\cal O}_Y\).  Each retained owner emits one lower target at
this depth.  Hence every legal correlated configuration covers at most

\[
                         |{\cal O}_Y|                           \tag{6.4}
\]

distinct targets of \({\cal T}_Y\).

Write

\[
                         t={e\over2}-{q\over4}+x
\]

and restrict to the band

\[
                         |x|\le {q\over8}.                       \tag{6.5}
\]

Uniformly in this band, the central binomial expansion gives

\[
\begin{aligned}
 \log { |{\cal O}_Y|\over|{\cal T}_Y|}
 &=
 \log{\binom e{e/2+3q/4+x}
              \over
              \binom e{e/2-q/4+x}}\\
 &=-{2\over e}
   \left[\left({3q\over4}+x\right)^2
         -\left(-{q\over4}+x\right)^2\right]+o(1)\\
 &=-{2\over e}\left({q^2\over2}+2qx\right)+o(1)
 \le-{q^2\over2e}+o(1)\\
 &=-A^2+o(1).                                      \tag{6.6}
\end{aligned}
\]

The \(O(d)\) error in (5.1) changes (6.6) by \(o(1)\).

For a uniformly random lower target, \(t=|T\cap E|\) is hypergeometric
with mean

\[
                         {e(m-q)\over2m}
                         ={e\over2}-{q\over4}+o(\sqrt m)
\]

and variance \(\Theta(m)\).  The local central limit theorem therefore
gives a constant \(c_A>0\) such that the union \({\cal B}_q\) of the
fibres in (6.5) satisfies

\[
                         |{\cal B}_q|\ge(c_A-o(1))N_q.           \tag{6.7}
\]

Summing (6.4)--(6.6) over those disjoint fibres proves:

### Theorem 6.1 (literal linear-scale carrier cut)

For every legal joint compiler state of the atlas in Section 5,

\[
\boxed{
 \#\{\text{covered targets in }{\cal B}_q\}
 \le(e^{-A^2}+o(1))|{\cal B}_q|.}                  \tag{6.8}
\]

Consequently

\[
\boxed{
 {\mathfrak H}_q^-
 \ge(c_A-o(1))(1-e^{-A^2})N_q
 =\Omega_A(W).}                                     \tag{6.9}
\]

Equivalently, the indicator weight \(y={\bf1}_{{\cal B}_q}\) violates
the reserve-\(o(W)\) configuration Hall inequality (4.1).  This is a
literal physical target cut, not a profile-labelled or formal-envelope
counterexample.

Complementation gives the corresponding upper empty-carrier cut for the
same fused states.

## 7. Scope of the no-go

The carrier atlas is dispersed over \(\Theta(m/\log m)\) growing
macroblocks inside \(E\), has \(R=\Theta(m)\), and satisfies every local
owner and trace conclusion of the patched theorem.  Nevertheless it
freezes the positive-density projection \(E^c\).

Therefore:

1. linear packet rank does not imply physical all-cuts dispersion;
2. the aggregate block enumerator does not prevent a literal Hall cut;
3. parent-cell rainbows do not compare different exterior fibres; and
4. arbitrary correlation of compiler states cannot repair an invariant
   which holds statewise.

Theorem 6.1 does not rule out a different atlas whose frame union moves
coordinates across every positive-density cut.  For such an atlas, the
smallest exact remaining theorem is a near-perfect matching in the
bundle hypergraph \({\cal K}\), equivalently an integral strengthening of
(4.1).  Any positive proof must use a projection-free property of the
complete state images, not merely pair codegrees or the cell-dimension
enumerator.

## 8. Projection-free successor

MATH_THEOREM_PROJECTION_FREE_MOVING_FRAME_UNION_DUAL_AND_LITERAL_CUT_20260726.md
derives the exact home-bundle configuration dual and the concave-closure
dual for prescribed moving-frame marginals. For a two-frame overlay with
whole-component options \(J_K^0,J_K^1\), it proves the literal formula

\[
 \mathbb E\mathfrak H
 =\sum_{t:c_t=0}2^{-d_t},
\]

where \(c_t\) records a component covering \(t\) on both sides and \(d_t\)
counts component orbits covering it on exactly one side.

The successor also supplies a different physical cut which survives
coordinate projection-freeness in the canonical pair-status component
model. A connected coordinate union has one global owner component, so
every integral state selects one fixed pair frame and has
\((\delta_A-o(1))W\) holes at \(q=A\sqrt m\). The all-ones weight on that
target layer gives the same positive configuration-dual deficit. The full
coordinate orbit balances raw occurrence multiplicities, but not literal
support indicators. Thus projection-free coordinate motion alone does
not close even the fractional whole-union gate in this component model.
