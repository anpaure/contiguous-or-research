# Rank-twisted macroblocks: literal factor twirl and the weighted Hall kernel

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Result

The complete-atlas compatibility formulas for the rank-twisted macroblock
tiling count potential source owners.  They do not by themselves account
for the facts that

* the \(2^q\) compatible orientations of a chosen set of \(q\) empty axes
  are the vertices of one physical \(q\)-face, rather than \(2^q\)
  independently selectable literal targets; and
* one valid context factor, with one packet-wide physical direction
  conjugation, chooses only its actual consecutive-window faces.

This note inserts both constraints exactly.

Let \(C\cong Q_S\) be one rank-twisted product orientation cell.  Choose
an \(n\)-subset of its physical axes, where

\[
                         q\le H\le n/4-1,
\]

freeze the other axes in all spectator orientations, and install the valid
two-sided trace-injective context factor in every resulting \(Q_n\)-fibre.
As in the owner tiling, retain exactly the product cells with \(S\ge n\);
cells of smaller dimension form the owner leave.  Residual ground
coordinates are frozen and must agree between source and target.
Average uniformly over all \(n\)-subsets and all cube-automorphism
conjugates of the factor.  Then every physical lower \(q\)-face of \(C\),
and every physical upper \(q\)-face of \(C\), is selected with exactly the
same probability

\[
 \boxed{\tau_{S,q}={2^q\over\binom Sq}.}                 \tag{0.1}
\]

This is an actual factor statement, not potential reachability.  One
conjugate is used on the whole spectator family and remains a valid exact
factor simultaneously at every protected depth.

Consequently the exact twirled lower load of a physical target \(T\) is

\[
 \boxed{
 \Lambda_q^-(T)
 =\sum_{\substack{\mathbf a\ge0\\\sum_j a_j=q}}
   \mathbf1_{\{q+\sum_j s_j(\mathbf a,T)\ge n\}}
   {2^q\prod_j\binom{z_j(\mathbf a,T)}{a_j}
    \over
    \binom{q+\sum_j s_j(\mathbf a,T)}q}.}               \tag{0.2}
\]

Here \(t_j=|T\cap B_j|\), statuses are evaluated in the matching
\(M_{j,t_j+a_j}\), and \(z_j,s_j\) are respectively its empty- and
single-edge counts on \(T\cap B_j\).  The exact upper formula is

\[
 \boxed{
 \Lambda_q^+(U)
 =\sum_{\substack{\mathbf a\ge0\\\sum_j a_j=q}}
   \mathbf1_{\{q+\sum_j s_j(\mathbf a,U)\ge n\}}
   {2^q\prod_j\binom{v_j(\mathbf a,U)}{a_j}
    \over
    \binom{q+\sum_j s_j(\mathbf a,U)}q},}               \tag{0.3}
\]

where statuses are evaluated in \(M_{j,u_j-a_j}\) and \(v_j\) is the
number of full edges.

The denominator in (0.2)--(0.3) is essential.  It is the exact number of
\(q\)-supports available at a compatible source cell of dimension

\[
                         S=q+\sum_js_j.                 \tag{0.4}
\]

Equivalently,

\[
 \Lambda_q^-(T)
 =\sum_{\substack{X\sim T\\X\text{ retained}}}
   {1\over\binom{S(X)}q},                              \tag{0.5}
\]

where the sum is over compatible source owners belonging to retained
cells, and \(S(X)\) is the dimension of the intrinsic rank-twisted product
cell containing \(X\).
The \(2^q\) source orientations on one chosen face turn (0.5) into (0.2)
exactly; they are not independent factor options.

For the complete retained cell family,

\[
 \boxed{
 \sum_T\Lambda_q^-(T)=G,
 \qquad
 \sum_U\Lambda_q^+(U)=G,}                             \tag{0.6}
\]

where \(G\) is the retained owner mass.  Thus the literal factor/order
layer introduces no fractional loss and no sign bias.  It converts the
old potential kernel into the source-normalized weighted kernel
(0.2)--(0.3).

In particular, at Gaussian depth \(q=A\sqrt m+O(1)\), the exponentially
small owner leave gives

\[
 {1\over N_q}\sum_T\Lambda_q^-(T)
 ={1\over N_q}\sum_U\Lambda_q^+(U)
 ={G\over N_q}=e^{A^2+o(1)}.                            \tag{0.7}
\]

Thus the valid consecutive-window library retains the full constant
Gaussian first-moment slack.  Any surviving negative result must be a
nontrivial target-family or integral option cut; it cannot be a loss of
total literal factor capacity.

What remains is not another marginal calculation.  To obtain one actual
owner factor, one must choose one common active set and one common
conjugate in every product cell.  The minimum remaining hypothesis is a
multiple-choice integral cover/rounding theorem for these cell options.
Neither \(\Lambda_q^\pm(T)\ge1\) nor small aggregate fractional deficit by
itself supplies that rounding.

## 1. Cube-face census

The number of unoriented physical \(q\)-faces of \(Q_S\) is

\[
                         \binom Sq2^{S-q}.             \tag{1.1}
\]

Fix one valid context factor \(F\) on \(Q_n\).  At a protected signed
depth \(q\), it has one trace occurrence per owner.  Literal trace
injectivity says that its signed image consists of exactly

\[
                         2^n                              \tag{1.2}
\]

distinct physical \(q\)-faces.  The cube automorphism group

\[
                         \Gamma_n=\mathbb F_2^n\rtimes S_n \tag{1.3}
\]

acts transitively on the \(\binom nq2^{n-q}\) physical \(q\)-faces.
Double counting pairs \((g,Q)\), where \(g\in\Gamma_n\) and
\(Q\in gF_q^\epsilon\), gives the following exact lemma.

### Lemma 1.1 (factor-conjugate incidence)

For either sign and every physical \(q\)-face \(Q\subset Q_n\),

\[
 {\#\{g\in\Gamma_n:Q\in gF_q^\epsilon\}\over|\Gamma_n|}
 ={2^n\over\binom nq2^{n-q}}
 ={2^q\over\binom nq}.                                 \tag{1.4}
\]

The same conjugate is a legal exact factor at every protected depth; (1.4)
is a simultaneous family of marginal identities, not a depth-dependent
choice of factors.

## 2. Spectator-safe active-axis twirl

Fix a physical \(q\)-face \(Q\) of \(Q_S\), and let \(D\) be its set of
\(q\) varying axes.  A uniform \(n\)-subset \(A\) of the \(S\) axes
contains \(D\) with probability

\[
 {\binom{S-q}{n-q}\over\binom Sn}
 ={\binom nq\over\binom Sq}.                           \tag{2.1}
\]

Conditional on \(D\subseteq A\), the fixed orientations outside \(A\)
place \(Q\) in one unique spectator fibre.  Lemma 1.1 then gives the
conditional factor probability \(2^q/\binom nq\).  Multiplying with
(2.1) proves (0.1).

There is no between-fibre collision hidden here.  Every target retains one
endpoint on each inactive split axis and therefore recovers the spectator
orientation.  The same active set and the same conjugate are installed in
all fibres, exactly as required by the audited variable-cell compiler.

The paired lower and upper faces associated with one abstract cube face
also have probability (0.1): an occurrence empties its \(q\) support axes
on the lower shore and fills the same axes on the upper shore.  In
particular, the marginal twirl is identical for the two signs.

## 3. Derivation of the lower kernel

Fix a lower target \(T\).  Write

\[
                         T_j=T\cap B_j,qquad t_j=|T_j|. \tag{3.1}
\]

Suppose the face uses \(a_j\) axes in block \(j\), where
\(\sum_ja_j=q\).  The source local rank is \(k_j=t_j+a_j\), so statuses
must be evaluated in \(M_{j,k_j}\).  If that matching has
\((z_j,s_j,v_j)\) statuses on \(T_j\), choose the \(a_j\) face axes from
its \(z_j\) empty edges.  There are

\[
                         \binom{z_j}{a_j}             \tag{3.2}
\]

choices of the physical axes.  Once those axes are chosen, all their
\(2^{a_j}\) source orientations lie in one and the same orientation cell;
they do not give different physical faces.

In that source cell, the selected empty edges become single, while the
original \(s_j\) single edges remain single.  Hence its dimension is

\[
                         S=\sum_j(s_j+a_j)
                          =q+\sum_js_j.               \tag{3.3}
\]

The retained construction installs an \(n\)-direction compiler in this
cell if and only if \(S\ge n\); cells with \(S<n\) belong to the owner
leave and contribute zero.  For a retained candidate cell-face, Theorem
(0.1) contributes \(2^q/\binom Sq\).  Multiplying the axis choices (3.2)
over blocks, inserting \(\mathbf1_{\{S\ge n\}}\), and summing over
allocations proves (0.2).

Alternatively, each chosen face contains \(2^q\) compatible source
owners.  Every such source has the same cell dimension \(S\), so summing
\(1/\binom Sq\) over its vertices gives exactly
\(2^q/\binom Sq\).  This proves the equivalent formula (0.5).

## 4. Upper kernel and the two-sign invariant

For an upper target \(U\), put \(u_j=|U\cap B_j|\).  If \(a_j\) axes are
used in block \(j\), the source rank is \(u_j-a_j\), so statuses are
evaluated in \(M_{j,u_j-a_j}\).  Choose the support axes from the
\(v_j\) full edges of \(U_j\).  In the source they become single, giving
the same dimension formula (3.3).  The proof of Section 3 then gives
(0.3).

There is also an exact coarse invariant worth recording.  In every
macroblock write

\[
 \delta_j(S)=|S\cap A_j|-|S\cap C_j|.                  \tag{4.1}
\]

For the paired lower and upper targets of one occurrence, every used axis
adds one \(A_j\)-endpoint and one \(C_j\)-endpoint.  Therefore

\[
                         \delta_j(U)=\delta_j(T)       \tag{4.2}
\]

for every block.  This does not yield a count obstruction.  For each
fixed imbalance vector \(\boldsymbol\delta\), complementing a target and
then swapping the two halves of every macroblock preserves
\(\boldsymbol\delta\) and interchanges global ranks \(m-q\) and \(m+q\).
Consequently the lower and upper target counts in every fixed imbalance
vector are exactly equal.  Any two-sign obstruction must be finer than
(4.2).

## 5. Conservation of total literal mass

Fix a product cell \(C\cong Q_S\).  Every active-set/conjugate option is
an exact owner factor on \(C\), and at either signed depth its literal
image has exactly \(|C|=2^S\) targets.  Averaging options does not change
that total.  Summing over the owner-disjoint retained cells proves (0.6).

The same identity follows directly from (0.5):

\[
\begin{aligned}
 \sum_T\Lambda_q^-(T)
 &=\sum_{X\text{ retained}}
   {\#\{\text{legal }q\text{-subsets of the }S(X)
                    \text{ split axes}\}\over\binom{S(X)}q}\\
 &=\sum_{X\text{ retained}}1=G.                         \tag{5.1}
\end{aligned}
\]

The upper identity is identical.

## 6. Exact fixed-profile contribution

For a fixed allocation \(\mathbf a\) and fixed exact status data, every
target in that fibre has the same twirled contribution

\[
 \boxed{
 \lambda(\mathbf a;\mathbf z,\mathbf s)
 =\mathbf1_{\{q+\sum_js_j\ge n\}}
  {2^q\prod_j\binom{z_j}{a_j}
   \over\binom{q+\sum_js_j}q}}                       \tag{6.1}
\]

on the lower shore, with \(z_j\) replaced by \(v_j\) above.  This is the
literal successor to the unnormalized source/target ratio

\[
 2^q\prod_j{\binom{z_j}{a_j}\over\binom{s_j+a_j}{a_j}}. \tag{6.2}
\]

Equation (6.2) compares the cardinalities of one target fibre and one
source-owner fibre.  Equation (6.1) additionally divides by the complete
\(q\)-support capacity of each source cell and is therefore the quantity
seen by an actual packet-wide factor twirl.  Neither expression may be
summed over allocations without controlling overlaps of the resulting
source cells.

## 7. Exact remaining integral statement

For a retained product cell \(C\), let \(\mathcal O(C)\) be its finite
set of legal options \((A,g)\), consisting of an admissible active-axis
set and one cube conjugate of the valid common context factor.  Every
option is one exact owner factor on \(C\) simultaneously through all
protected depths.

The literal completion problem is to choose

\[
                         o_C\in\mathcal O(C)          \tag{7.1}
\]

for every retained cell so that, simultaneously for both signs and every
\(q\le H\), the union of the selected target images has only \(o(W)\)
holes in aggregate.  This is a multiple-choice set-packing/cover problem:
all \(2^S\) starts in one cell are coupled by the one option \(o_C\).

The twirl gives one exact fractional point of this option polytope.  A
necessary marginal test for that particular point is

\[
 \sum_{q\le H,\epsilon}\sum_T
       (1-\Lambda_q^\epsilon(T))_+=o(W),              \tag{7.2}
\]

but even (7.2) would not round (7.1): target coverage is a nonlinear union
condition, and independent option choices at constant mean load leave a
Poisson-scale fraction of holes.  Conversely, failure of (7.2) refutes
the uniform twirl but not every nonuniform correlated choice.

Nor may the twirl be installed inside one cell by silently assigning all
active sets to binary selector fibres.  Such a batching freezes its
selector directions, and every literal target decodes the one relevant
selector row.  The resulting fixed-cylinder indicator must then be
inserted in (0.2)--(0.3).  The present theorem instead averages genuinely
mutually exclusive whole-cell options; it proves an exact fractional point
of (7.1), not an internal selector implementation of that point.

Thus the exact proved boundary is:

1. owner tiling and local literal compilation are exact;
2. all active-axis and packet-order restrictions disappear under the
   exact twirl (0.1);
3. the surviving fractional status kernel is precisely (0.2)--(0.3); and
4. the minimum unresolved theorem is a nonuniform, correlated integral
   choice from the cell option sets (7.1), not potential source Hall.

The subsequent construction
MATH_THEOREM_TRANSVERSAL_AXIS_SELECTOR_AND_COMPILER_HALL_GATE_20260726.md
integralizes the **direction-support marginal** without a parallel
localized carrier.  It partitions a typical \(Q_S\) as a product of
direction-spread edge matchings and batches one affine compiler conjugate
per resulting packet.  Its actual signed occurrences satisfy
\[
 \nu_q(D\subseteq E)\le(1+o(1))
        (|E|/(S-o(S)))^q.
\]
This removes the localized-\(E\) cut and preserves the Gaussian profile
Hall expansion.  It does not integralize the literal target loads in
(7.1); arbitrary block-labelled configuration weights remain open.
