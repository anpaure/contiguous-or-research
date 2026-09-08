# Home-packet assignments and the exact diverse-compiler realizability gate

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

The transversal-axis selector theorem removes the localized-carrier
obstruction and is compatible with the diverse-order compiler.  It also
gives a useful exact fact: within one rank-twisted product cell, literal
faces recover their unique transversal packet.  Hence compiler images
from different packets of that cell are disjoint.

These facts do **not** prove the requested home-packet theorem.  There
are two distinct Hall problems.

1. The selected-axis candidate graph asks only whether a target is a
   physical face of a packet.
2. The configuration graph asks whether one common affine conjugate of
   the diverse compiler contains the entire bundle assigned to that
   packet, simultaneously over all depths and both signs.

Ordinary weighted Hall in the first graph does not imply Hall in the
second.  The exact local obstruction is finite and explicit.  If
\(\tau=(q,\epsilon,T)\) is a target token and \(P\) is a compatible
packet, define

\[
 {\cal G}_P(\tau)
 =\{g\in\Gamma_R:T\in I_{P,g,q}^{\epsilon}\}.        \tag{0.1}
\]

A bundle \(B\) assigned to \(P\) is realizable by one compiler if and
only if

\[
                         \boxed{
 \bigcap_{\tau\in B}{\cal G}_P(\tau)\ne\varnothing.} \tag{0.2}
\]

This condition is absent from a target-to-packet \(b\)-matching.

It is highly restrictive.  At one signed depth, let

\[
 V_{R,q}=\binom Rq2^{R-q}                           \tag{0.3}
\]

be the number of physical \(q\)-faces of \(Q_R\).  One compiler image has
\(2^R\) faces, and there are at most
\(|\Gamma_R|=2^RR!\) affine images.  Therefore the number of realizable
\(k\)-face bundles is at most

\[
                         |\Gamma_R|\binom{2^R}{k}.  \tag{0.4}
\]

For \(k=o(2^R)\) with

\[
 k\gg {R\log R\over q\log(R/q)},                    \tag{0.5}
\]

an asymptotically vanishing fraction of all \(k\)-bundles is realizable.
At Gaussian depth this threshold is only
\(O(R\log R/(\sqrt m\log(R/\sqrt m)))\), whereas a home cover assigns
about \(2^R/\lambda_q\) targets to a typical packet.  Thus an arbitrary
outer Hall assignment is overwhelmingly outside the compiler orbit.

The correct bipartite object already has packet-option labels
\((P,g)\) on its right shore.  Its exact fractional near-cover condition
is the configuration inequality

\[
 \sum_P\max_g\sum_\tau y_\tau a_{P,g,\tau}
       +\rho_E(y)
 \ge\sum_\tau y_\tau
 \qquad(y\ge0),                                     \tag{0.6}
\]

where \(E=o(W)\) is the allowed reserve and \(\rho_E(y)\) is the sum of
the \(E\) largest target weights.  The transversal theorem proves (0.6)
only for its safe profile/cylinder weight classes, not for arbitrary
literal \(y\).

Finally, even a home cover does not by itself verify the
column-square/floor-energy requirement: all non-home occurrences of the
selected compiler images remain and may concentrate their forced surplus.
Exact floor balancing is the stronger signed quota-configuration dual in
Section 6.

Thus the requested construction is not currently proved.  The exact
block is not owner packing, support dispersion, or within-packet
injectivity.  It is the finite bundle constraint (0.2), inserted into the
arbitrary-weight configuration Hall inequality (0.6), followed by its
integral signed-quota rounding.

## 1. What the transversal selector proves

Fix a dimension-typical rank-twisted product cell

\[
                         C\cong Q_S,\qquad S=\Theta(m).           \tag{1.1}
\]

Partition its axes into \(R\) groups and take the Cartesian product of
one direction-spread matching edge from every group.  The resulting
transversal \(Q_R\)'s partition \(C\) exactly.  Every packet uses one
axis from every group, while the support distribution is
asymptotically the product of the uniform group distributions.

For every physical axis carrier \(E\subseteq C\), the fraction of
depth-\(q\) occurrences supported wholly in \(E\) is at most

\[
 (1+o(1))
 \left({|E\cap P_C|\over|P_C|}\right)^q.            \tag{1.2}
\]

At \(q=A\sqrt m\), a carrier of size \(O(R)=o(m)\) therefore captures
only \(o(1)\) of the occurrences.  This correctly eliminates the old
localized-axis counterexample.

There is also exact packet recovery.  In every group, a packet matching
edge is determined by either the edge itself or either endpoint.  A
physical face consequently recovers the matching edge in every group and
hence its unique packet.  Therefore:

### Lemma 1.1 (within-cell configuration disjointness)

For any choice of trace-injective compiler conjugate in every
transversal packet, the signed depth-\(q\) target images of distinct
packets in one product cell are disjoint.

This removes within-cell cross-packet repeats.  It does not separate
targets emitted by different product cells.

The selector theorem further proves weighted Hall expansion for weights
constant on its safe empirical half-rank/carrier profiles.  Its own
configuration dual explicitly leaves arbitrary block-labelled target
weights open.  Anti-localization and profile Hall therefore cannot be
substituted for (0.6).

## 2. The correct packet-option incidence graph

Let

\[
 {\cal U}=\{(q,\epsilon,T):1\le q\le H,\ 
       \epsilon\in\{-,+\},\ T\in{\cal T}_{q}^{\epsilon}\}        \tag{2.1}
\]

be the protected target-token set.  A packet \(P\) has option group

\[
                         {\cal O}_P=\{(P,g):g\in\Gamma_R\}.       \tag{2.2}
\]

For \(u=(q,\epsilon,T)\), put

\[
 a_{P,g,u}
 ={\bf1}\{T\in I_{P,g,q}^{\epsilon}\}.              \tag{2.3}
\]

Literal trace injectivity says that, at one sign and depth,

\[
                         \sum_Ta_{P,g,(q,\epsilon,T)}=2^R.       \tag{2.4}
\]

The option must be chosen packetwise:

\[
 x_{P,g}\in\{0,1\},\qquad
                         \sum_gx_{P,g}=1.            \tag{2.5}
\]

A target is covered when

\[
                         \sum_{P,g}a_{P,g,u}x_{P,g}\ge1.         \tag{2.6}
\]

If a set of options satisfying (2.5)--(2.6) is known, every covered
target may be assigned to one selected incident option.  This gives a
home-packet/home-label assignment.  Conversely, such a home assignment
with one label per packet gives (2.5)--(2.6).  Thus the configuration
graph, not the candidate packet graph, is the exact home graph.

For a fractional reserve \(E\), introduce

\[
 {\cal Z}_E=\{z\in[0,1]^{\cal U}:\sum_uz_u\le E\},
 \qquad
 \rho_E(y)=\max_{z\in{\cal Z}_E}\sum_uy_uz_u.        \tag{2.7}
\]

Here \(\rho_E(y)\) is the sum of the \(E\) largest weights, with a
fractional last term if necessary.  Separation of the product of packet
simplices from the covering orthant proves:

### Theorem 2.1 (exact fractional configuration Hall)

There are \(x_{P,g}\ge0\), \(\sum_gx_{P,g}=1\), and
\(z\in{\cal Z}_E\) satisfying

\[
                         \sum_{P,g}a_{P,g,u}x_{P,g}+z_u\ge1
                                                               \tag{2.8}
\]

for every token \(u\) if and only if, for every \(y\ge0\),

\[
 \boxed{
 \sum_P\max_g\sum_uy_ua_{P,g,u}+\rho_E(y)
 \ge\sum_uy_u.}                                      \tag{2.9}
\]

#### Proof

The load vectors of fractional packet choices form a compact convex set.
Adding \({\cal Z}_E\) and the nonnegative orthant gives another convex set.
If it does not contain the all-one vector, separation supplies a
nonnegative normal \(y\).  The support function of the product of packet
simplices is

\[
                         \sum_P\max_g\sum_uy_ua_{P,g,u},
\]

and the support function of \({\cal Z}_E\) is \(\rho_E(y)\).  This proves
necessity and sufficiency.  \(\square\)

The transversal selector's profile inequalities test (2.9) on a small
class of \(y\).  They do not establish it for arbitrary literal weights.
Even if (2.9) were proved, its integral rounding with the grouped
constraints (2.5) would remain.

## 3. Why target-to-packet Hall does not lift

Erase \(g\) from the right vertices and join a target to a packet whenever
it is some physical face of that packet.  A capacitated Hall theorem in
this larger graph can assign a bundle \(B_P\) of targets to every packet.
For this assignment to lift, however, one needs one option \(g_P\) with

\[
                         a_{P,g_P,u}=1
                         \quad\text{for every }u\in B_P.          \tag{3.1}
\]

Equivalently, define the allowed-conjugate set

\[
                         {\cal G}_P(u)=\{g:a_{P,g,u}=1\}.         \tag{3.2}
\]

Then (3.1) is exactly

\[
                         \bigcap_{u\in B_P}{\cal G}_P(u)
                         \ne\varnothing.             \tag{3.3}
\]

Ordinary Hall controls only the separate nonemptiness of the sets in
(3.2).  It supplies no finite-intersection property.

This is not a negligible issue.  At one Gaussian depth, the average
number of home targets per packet required to cover the layer is

\[
 {N_q\over G/2^R}
 ={N_q\over G}\,2^R
 =(e^{-A^2}+o(1))2^R.                               \tag{3.4}
\]

Thus the local bundle is a positive-density subset of one compiler image,
not a bounded collection of independently satisfiable faces.

## 4. Exact finite local compiler constraint

Identify a packet with the abstract cube \(Q_R\).  A physical signed
target token restricts to a signed face

\[
                         f=(q,\epsilon,J,\eta),      \tag{4.1}
\]

where \(J\subseteq[R]\), \(|J|=q\), is the varied-axis set and
\(\eta\in Q_{[R]\setminus J}\) records the fixed outside orientations.
The sign remembers whether the physical target empties or fills the
axes in \(J\).

Let

\[
 {\mathfrak F}_{q,\epsilon}
 =\{f_{q,\epsilon}(x):x\in Q_R\}                    \tag{4.2}
\]

be the signed face image of the base diverse compiler.  It has \(2^R\)
members.  For a bundle \(B\) of signed faces, (3.3) is equivalent to

\[
 \boxed{
 \exists\,g=(\sigma,a)\in S_R\ltimes Q_R
 \quad\text{such that}\quad
 g^{-1}(B_{q,\epsilon})\subseteq{\mathfrak F}_{q,\epsilon}
 \quad\text{for every }(q,\epsilon).}
                                                               \tag{4.3}
\]

More plainly, one affine cube map must carry every face in \(B\) into
the corresponding base compiler catalogue.  The same map is used at all
depths and both signs.

This condition has a concrete finite invariant.  For two faces
\(f=(J,\eta)\) and \(f'=(J',\eta')\) of the same dimension, their orbit
under cube automorphisms is determined by

\[
 \omega(f,f')
 =\left(
 |J\cap J'|,
 |\{i\notin J\cup J':\eta_i\ne\eta'_i\}|
 \right).                                           \tag{4.4}
\]

The first coordinate records common varied axes.  On axes fixed in both
faces, translation complements both bits and hence preserves their
difference; coordinate permutation preserves only its Hamming weight.
All other coordinate categories are determined by \(R,q\), and the two
numbers in (4.4) are also sufficient to construct an automorphism.

Consequently a necessary pairwise condition for (4.3) is:

\[
 \omega(f,f')\text{ occurs among a pair of faces in }
 {\mathfrak F}_{q,\epsilon}
 \quad\text{for every }f,f'\in B.                  \tag{4.5}
\]

For faces of different dimensions, retain both support sizes in addition
to the same intersection and fixed-bit difference data.  Across signs,
retain the sign labels as well.

For three or more faces, pair data need not suffice.  The complete
invariant is still finite.  At every coordinate record:

1. which faces vary on that coordinate; and
2. the vector of their fixed bits on the faces which do not vary,
   modulo simultaneous complementation of all those fixed bits.

An affine translation chooses the complementation independently at each
coordinate, and a coordinate permutation merely permutes the resulting
column types.  Hence the multiset of these column types is the complete
affine invariant of the ordered face bundle.  A bundle is realizable
exactly when it can be matched to an equally labelled subbundle of the
base compiler catalogue with the same column-type multiset.

This is the requested exact finite local compiler constraint.

## 5. Quantitative scarcity of realizable bundles

The local constraint cannot be omitted on the grounds that the affine
catalogue is large.

At one sign and depth, the full physical face universe has size

\[
                         V_{R,q}=\binom Rq2^{R-q}.   \tag{5.1}
\]

Every conjugate compiler image has \(K=2^R\) faces.  The number of
conjugates is at most

\[
                         |\Gamma_R|=2^RR!.           \tag{5.2}
\]

Therefore:

### Lemma 5.1 (bundle-orbit bound)

The number of \(k\)-subsets of physical \(q\)-faces which are contained
in at least one affine compiler image is at most

\[
                         |\Gamma_R|\binom Kk.        \tag{5.3}
\]

Consequently the fraction of all \(k\)-bundles which are realizable is
at most

\[
 {|\Gamma_R|\binom Kk\over\binom{V_{R,q}}k}.        \tag{5.4}
\]

#### Proof

For each \(g\in\Gamma_R\), choose the bundle from the \(K\)-set
\(g{\mathfrak F}_{q,\epsilon}\).  Summing over \(g\) may count one bundle
several times, so it is an upper bound.  Division by the total number of
\(k\)-subsets gives (5.4).  \(\square\)

For \(k=o(K)\),

\[
 {\binom Kk\over\binom{V_{R,q}}k}
 \le
 \left({K\over V_{R,q}-k+1}\right)^k
 =\left((1+o(1)){2^q\over\binom Rq}\right)^k.        \tag{5.5}
\]

Also

\[
 \log|\Gamma_R|=O(R\log R),\qquad
 \log{\binom Rq\over2^q}
 =\Theta(q\log(R/q))                                \tag{5.6}
\]

when \(q=o(R)\).  Thus (5.4) tends to zero whenever

\[
                         k\gg
 {R\log R\over q\log(R/q)}.                         \tag{5.7}
\]

This calculation was for \(k=o(K)\).  The required dense-bundle scale is
even more strongly excluded from a uniform bundle model.  If
\(k=\alpha K\), \(0<\alpha<1\) fixed, then

\[
 \binom Kk\le2^K,\qquad
 \binom{V_{R,q}}k\ge\left({V_{R,q}\over k}\right)^k,
                                                               \tag{5.8}
\]

and hence

\[
 {|\Gamma_R|\binom Kk\over\binom{V_{R,q}}k}
 \le
 \exp\!\left[-\Omega_\alpha\!\left(
 K\log{\binom Rq\over2^q}\right)\right].             \tag{5.9}
\]

At \(q=A\sqrt m\), \(R\asymp\sqrt{mH}\), the threshold (5.7) is
subexponential and tiny compared with the required bundle size
\((e^{-A^2}+o(1))2^R\) in (3.4), while (5.9) shows that a uniformly
chosen bundle at that required density is unrealizable with
doubly-exponentially high probability.

Lemma 5.1 does not prove that a specially constructed global assignment
cannot choose realizable bundles.  It proves that realizability cannot be
deduced from an arbitrary outer Hall assignment: almost every bundle
allowed by that Hall graph violates the exact local compiler constraint.

## 6. Home coverage is weaker than floor balancing

Suppose, optimistically, that one integral option \(g_P\) has been chosen
per packet and all but \(o(W)\) target tokens have been assigned to
incident selected options.  This proves a small zero class, but it does
not control the full load vector

\[
                         L_{q,\epsilon}(T)
 =\sum_Pa_{P,g_P,(q,\epsilon,T)}.                   \tag{6.1}
\]

At one depth and sign,

\[
                         \sum_TL_{q,\epsilon}(T)=G.  \tag{6.2}
\]

Write

\[
 {G\over N_q}=c_q+\alpha_q,\qquad
 c_q=\left\lfloor{G\over N_q}\right\rfloor.         \tag{6.3}
\]

The floor energy is

\[
 Q_{q,\epsilon}(L)
 =\sum_T(L_{q,\epsilon}(T)-c_q)
        (L_{q,\epsilon}(T)-c_q-1).                  \tag{6.4}
\]

It vanishes exactly when every load is \(c_q\) or \(c_q+1\).  A home
assignment controls only whether \(L(T)\ge1\).  The remaining
\(G-N_q\) occurrences can still concentrate on a small set of targets
and make (6.4) of order \(W\) or larger.

The correct convex quota set \({\cal B}_{q,\epsilon}\) consists of the
translations of the hypersimplex with \(R_q=G-c_qN_q\) coordinates at
\(c_q+1\) and the rest at \(c_q\).  Let

\[
 {\cal B}=\prod_{q\le H,\epsilon}{\cal B}_{q,\epsilon}.          \tag{6.5}
\]

The convex load set of packet options is

\[
 {\cal C}
 =\left\{
 \sum_{P,g}x_{P,g}a_{P,g}:
 x_{P,g}\ge0,\ \sum_gx_{P,g}=1
 \right\}.                                           \tag{6.6}
\]

Separation gives the exact fractional floor-feasibility condition:

\[
 \boxed{
 \sum_P\min_g\langle y,a_{P,g}\rangle
 \le h_{\cal B}(y)
 \quad\text{for every real protected target array }y.}         \tag{6.7}
\]

The minimum appears because a separating hyperplane would have
\(\inf_{z\in{\cal C}}\langle y,z\rangle>
\sup_{b\in{\cal B}}\langle y,b\rangle\).
All depths and signs occur inside the same minimum because one \(g\) is
used packetwide.

For one layer,

\[
 h_{{\cal B}_{q,\epsilon}}(y)
 =c_q\sum_Ty_T+\sum_{\text{\(R_q\) largest }y_T}y_T.             \tag{6.8}
\]

Condition (6.7) is precisely the weighted configuration inequality left
open in the transversal-axis theorem.  The Latin column-square condition
is a sufficient integral averaging mechanism for approaching the same
floor polytope, but neither a home cover nor profile Hall verifies it.

## 7. Final obstruction statement

### Theorem 7.1 (home-packet lifting gate)

The dispersed transversal-axis selector and the diverse-order compiler
prove exact owner factorhood, anti-localization, within-packet
injectivity, and within-cell target disjointness.  They do not imply an
all-target home assignment or the joint floor-energy conclusion.

An all-but-\(E\) fractional home assignment exists exactly when the
packet-option incidence system satisfies (2.9).  Any integral home
assignment must additionally choose one option in every packet group.
An assignment first constructed in the larger target-to-packet graph
lifts if and only if every packet bundle satisfies the finite
intersection condition (3.3), equivalently the affine bundle invariant
of Section 4.  Almost every bundle beyond the threshold (5.7) fails this
condition.

Even a successful home cover does not imply the desired column-square
or floor-energy bound.  Joint floor balancing over all depths and signs
requires the stronger configuration inequality (6.7), followed by
integral grouped rounding.

Therefore the exact unresolved finite local constraint is:

\[
 \boxed{
 \exists\,g_P\in\Gamma_R\quad
 B_{P,q,\epsilon}\subseteq I_{P,g_P,q}^{\epsilon}
 \quad\text{for every }q\le H,\ \epsilon\in\{-,+\}.
 }                                                   \tag{7.1}
\]

understood through the nonempty intersection (3.3).  No theorem currently
shows that the transversal selected-axis Hall assignment can be chosen
inside these compiler-realizable bundles.

The subsequent note
\(\texttt{MATH\_THEOREM\_COMPILER\_COLUMN\_TYPES\_AND\_BUNDLE\_HYPERGRAPH\_GATE\_20260726.md}\)
classifies these bundles by their complete column-type multiset and gives
the exact pair-type degree/codegree kernel of the resulting colored
hypergraph.
