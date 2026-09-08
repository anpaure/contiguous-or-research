# Gate B: the exact `j=2` local scale and the five-vertex replacement bank

**Date:** 2026-08-22

**Status.**  This note certifies a quantitative obstruction to transferring
the sixteen-atom zero-avoidance profile by the currently available absolute
remainder estimate.  It does not disprove a relative harmonic remainder
theorem.  It proves three exact facts.

1. At harmonic level `j=2`, two decisive rows of the sixteen-atom shore
   matrix have closed rational formulas for every `r>=6`.  Their determinant
   is positive and asymptotic to `6/r^8`; the corresponding two-row least
   singular value is asymptotic to

   \[
        {9\over2\sqrt2}\,{D_M\over r^5}.                 \tag{0.1}
   \]

2. Consequently the known pointwise remote bound `O(D_M/r^2)` is not a
   relative perturbation estimate on the certified local singular scale.
   A Weyl/principal-angle transfer based only on those two bounds loses at
   least three powers of `r`.  A matrix-valued harmonic polymer estimate is
   genuinely additional.

3. The next boundary layer is still finite.  For every `r>=9`, all blocker
   sets covering the two event roots and using at most five incident cuts
   comprise exactly `212` inclusion--exclusion terms on `104` vertex sets.
   The `88` new five-vertex sets have the exact topology census in Section 4.

The all-module `W_2` theorem and the exact full-exposure-to-zero-avoidance
quotient remain valid.  The open scalar is still the polynomial lower bound
for the full zero-avoidance affine residual.  The result here says that the
sixteen four-vertex atoms plus an absolute columnwise error cannot close it.

## 1. Objects and normalization

Put

\[
 b=2r+1,\qquad k=r-2,\qquad \ell=r+3,
 \qquad D_M=2r\,r!(r+1)! .                              \tag{1.1}
\]

After multiplication of boundary cuts by `-2 modulo b`, the central
boundary graph is the punctured graph

\[
        \operatorname {Cay}(\mathbb Z_b,\{\pm1,\pm3\}),       \tag{1.2}
\]

and the two event roots are `0,5`.  The sixteen four-vertex sets and their
twenty-two blocker terms are those of the preceding local-atom theorem:
ten induced matchings contribute their matching codegree, while each of six
induced three-edge paths contributes endpoint-matching codegree minus
full-path codegree.

Let `L_(s,2)(t)` be the resulting punctured signed boundary profile on root
shore `s in {r,r-1}`.  No extra-pair denominator occurs at `j=2`.  Define

\[
 a_r={L_{r,2}(0)\over D_M},\quad
 b_r={L_{r-1,2}(0)\over D_M},\quad
 c_r={L_{r,2}(\ell)\over D_M},\quad
 d_r={L_{r-1,2}(\ell)\over D_M}.                    \tag{1.3}
\]

## 2. A root-subset-free exact Venn formula

The following calculation explains why the formulas in Section 3 are
identities rather than interpolation.

Fix an ordered blocker tuple `J=(T_1,...,T_m)`, with `m=2` or `3`.  Its
Boolean cells are indexed by `eta in {0,1}^m`; write `C_eta` for the label
cell and `c_eta=|C_eta|`.  Let the four boundary labels in order be
`p_+,p_-,q_+,q_-`, and let `eta(x)` be the cell containing `x`.  If a
positional root interval has `u_eta` points in the positional blocker cell
corresponding to `eta`, put

\[
 \mathcal H_J(u)=
 [\prod_\eta z_\eta^{u_\eta}]
 (z_{\eta(p_+)}-z_{\eta(p_-)})
 (z_{\eta(q_+)}-z_{\eta(q_-)})
 \prod_\eta(1+z_\eta)^{c_\eta-m_\eta},             \tag{2.1}
\]

where `m_eta` is the number of the four boundary labels in `C_eta`.
This is exactly the signed sum of

\[
 (\mathbf1_{p_+\in S}-\mathbf1_{p_-\in S})
 (\mathbf1_{q_+\in S}-\mathbf1_{q_-\in S})          \tag{2.2}
\]

over label roots `S` with the prescribed cell counts.  Indeed the weighted
choice polynomial for the first boundary pair is
`z_(eta(p_+))-z_(eta(p_-))`, and similarly for the second pair; every
unmarked label contributes `1+z_eta`.

Let `N_(s,J)(u)` count retained positional tuples consisting of a rank-`s`
root interval and blocker intervals of the ranks in `J`, with blocker-cell
sizes `c_eta` and root-inside counts `u_eta`.  Cellwise bijection counting
then gives the exact contribution of `J`:

\[
 \boxed{
 \Omega_{s,J}=
 \sum_u N_{s,J}(u)\,\mathcal H_J(u)
       \prod_\eta u_\eta!\,(c_\eta-u_\eta)! .}       \tag{2.3}
\]

To prove (2.3), fix the positional intervals.  A compatible word is an
independent bijection on every root-refined Boolean cell, giving the
factorial product.  Summing the signed label-root choices gives (2.1).
Conversely every compatible word and retained root start occurs once.

There are only twenty-two `J`'s, at most eight Boolean cells, and at most
`b^4` positional tuples.  Applying (2.3), inserting the puncture, and
collecting factorial ratios gives the four rational functions below.
This derivation is also implemented by the authenticated exact evaluator;
it never enumerates the `binom(b,s)` root subsets.

## 3. Exact rational rows and determinant

For every integer `r>=6`, direct simplification of (2.3) gives

\[
 a_r=-{25r^6-338r^5+1820r^4-5571r^3+8838r^2-5512r+1008
 \over
 r^3(r-4)(r-3)(r-2)^2(r-1)^2(r+1)},                 \tag{3.1}
\]

\[
 b_r=-{25r^6-380r^5+2281r^4-7583r^3+13501r^2-10490r+2808
 \over
 r^3(r-4)(r-3)(r-2)^2(r-1)^2(r+1)},                 \tag{3.2}
\]

\[
 c_r=-{4r^5+55r^4-536r^3+1204r^2-710r+28
 \over
 3r^3(r-2)^2(r-1)^2(r+1)},                          \tag{3.3}
\]

\[
 d_r=-{4r^5+49r^4-641r^3+1822r^2-1559r+406
 \over
 3r^3(r-2)^2(r-1)^2(r+1)}.                          \tag{3.4}
\]

Their determinant is

\[
 \boxed{
 a_rd_r-b_rc_r={P(r)\over
 3r^6(r-4)(r-3)(r-2)^4(r-1)^4(r+1)^2},}             \tag{3.5}
\]

where

\[
\begin{split}
 P(r)={}&18r^{10}-131r^9+201r^8+1889r^7+53250r^6
 -493848r^5\\
 &+1629447r^4-2796178r^3+2811252r^2-1521944r+330624.
                                                               \tag{3.6}
\end{split}
\]

There is no sign inference hidden here.  With `u=r-6`, the coefficients of
`P(u+6)`, from degree ten down to zero, are

\[
 (18,949,22287,308321,2857212,19162692,96093591,
 353036102,884265816,1323152416,879077760),          \tag{3.7}
\]

so the determinant is positive for every `r>=6`.  In fact

\[
                         a_rd_r-b_rc_r\ge {6\over r^8}.       \tag{3.8}
\]

After putting (3.5) over the denominator in (3.8), the numerator
`r^8P(r)-6Q(r)`, where `Q` is the denominator in (3.5), has, after the
same shift, the following positive coefficients from degree seventeen to
zero:

\[
\begin{split}
(&175,15873,677195,18116034,341685738,4840392669,
53509792388,472642548156,3380491146808,\\
&19680520420656,93086939932128,354661392286656,
1071506780850816,2504578057565184,4360211416770048,\\
&5312765461100544,4036251778523136,1437008502620160).
                                                               \tag{3.9}
\end{split}
\]

Equations (3.1)--(3.4) also give

\[
 (a_r,b_r)=(-25,-25)r^{-4}+O(r^{-5}),
\]

\[
 (c_r,d_r)=(-4/3,-4/3)r^{-3}+(-25,-23)r^{-4}
            +O(r^{-5}).                                      \tag{3.10}
\]

Let `B_r` be the two-by-two matrix with these two profile rows.  Since the
product of its singular values is its determinant, (3.5) and (3.10) imply

\[
 \boxed{
 \sigma_{\min}(B_r)=
 {9\over2\sqrt2}\,r^{-5}(1+O(r^{-1})).}             \tag{3.11}
\]

An explicit nonasymptotic polynomial lower bound also follows.  The crude
factor inequalities valid for `r>=6` give
`max(|a_r|,|b_r|,|c_r|,|d_r|)<=10^6/r^3`.  Therefore

\[
 \sigma_{\min}(B_r)
 \ge {|\det B_r|\over\|B_r\|_F}
 \ge {3\over10^6r^5}.                               \tag{3.12}
\]

Adding the other profile rows can only increase the least singular value.
Thus (3.12) is a genuine polynomial lower bound for the two local shore
columns.  It is not a transfer theorem for the dressed columns.

### Why the available error estimate does not transfer the angle

The proved remote estimate is pointwise `O(D_M/r^2)`.  In the normalized
profile matrix this supplies only an absolute synthesis-operator bound of
that order (up to the harmless mean/Euclidean `sqrt(b)` convention).
The certified two-row local scale in (3.11)--(3.12) is three powers smaller.
Weyl's inequality or the principal-angle perturbation lemma requires an
error smaller than the least singular scale, and hence cannot be invoked
from these estimates.

This is an insufficiency theorem about the present hypotheses.  It does
not say that the actual remote dressing is adversarial.  A valid positive
replacement would be a shore-adapted relative estimate, for example

\[
 B_{\rm rem}^{\mathsf T}B_{\rm rem}
 \preceq {C\over r^2}L^{\mathsf T}L,                 \tag{3.13}
\]

or a full cluster/cumulant identity giving the same control in the local
near-kernel direction.

## 4. Exact five-vertex bank

The next layer can be classified without asymptotics.  In the retained
Cayley graph, enumerate vertex sets containing `0,5`, take every induced
edge subset whose incident-vertex union is the whole set, and attach the
inclusion--exclusion sign `(-1)^|J|`.  The complete census is

\[
\begin{array}{c|c|c|c|c}
\text{component sizes}&|V|&|E(V)|&
 \#\text{edge subsets using all }V&\#V\\ \hline
(2,2)&4&2&1&10\\
(4)&4&3&2&6\\ \hline
(2,3)&5&3&1&54\\
(5)&5&4&3&20\\
(5)&5&4&2&6\\
(5)&5&5&8&8
\end{array}                                                   \tag{4.1}
\]

Thus the first two rows recover `10+6=16` four-vertex sets and
`10+12=22` terms.  The last four rows give

\[
 54+20+6+8=88\quad\text{five-vertex sets},
\]

\[
 54+60+12+64=190\quad\text{five-vertex terms}.       \tag{4.2}
\]

Altogether there are exactly `104` vertex sets and `212` terms.

For completeness, here is why this is one fixed finite enumeration for all
`r>=9`.  Translate the event roots to `0,5`.  The two deleted edges are then
`{6,7}` and `{6,9}`.  A blocker set on at most five vertices has no component
containing neither root: the two rooted components already need two vertices
each, and an unrooted edge would raise the total to six.  If the roots are in
one component, a simple path between them has at most four edges.  Four
steps from `{+/-1,+/-3}` have an even integer sum in `[-12,12]`; for
`b>=19`, no such sum is congruent to `5 modulo b`, since the candidates
`5,5+/-b` are odd or lie outside that interval.  Their graph distance is
three, so the component contains a three-edge path and at most one vertex
adjacent to it.  If the roots are in separate components, their component
sizes are `2,2` or `2,3`.  In either case every vertex has an integer
representative in

\[
                         \{-6,-5,\ldots,11\}.         \tag{4.2a}
\]

For `r>=10`, `b>=21`; two representatives in this interval are adjacent
modulo `b` exactly when their ordinary difference is `+/-1` or `+/-3`.
Indeed the largest difference is seventeen and `b-17>=4`.  Hence the graph,
including its two deleted edges, is literally independent of `r`.  The case
`r=9` is the one finite cycle `Z_19`; direct scanning gives the same table.

On this fixed graph, choose two or three additional vertices beside `0,5`,
list the induced edges, and scan their Boolean subsets, retaining precisely
those whose incident union is the chosen vertex set.  Component sizes,
induced-edge count, and retained-subset count give the four columns of
(4.1).  This proves stabilization and contains no numerical tolerance or
unlisted search choice; the checker independently replays the scan.

The five-vertex bank is not negligible in the harmonic profile merely
because it loses one unsigned boundary-codegree power.  As an exact finite
calibration, at `r=8,j=2`, the combined `|V|<=5` rows are

\[
\begin{array}{c|rr}
t&L^{(\le5)}_{r,2}(t)&L^{(\le5)}_{r-1,2}(t)\\ \hline
0&84461184&18108288\\
\ell=11&-15240960&19025280\\
3&356277888&280143360
\end{array}                                                   \tag{4.3}
\]

while the sixteen-atom rows are

\[
\begin{array}{c|rr}
0&-868216320&-497076480\\
11&-1471910400&-1038009600\\
3&-2340126720&-1535086080.
\end{array}                                                   \tag{4.4}
\]

Here `D_M=234101145600`.  Subtracting (4.4) from (4.3) isolates the new
five-vertex contribution; at `t=0` it is
`(952677504,515184768)`, already reversing the middle-shore sign.  These
are exact integers from (2.3), but one finite value is calibration, not an
all-`r` asymptotic theorem.

## 5. Correct remaining statement and regime split

The certified `j=2` result is now:

* the sixteen-atom two-shore matrix is polynomially nondegenerate;
* its explicit two-row certificate lives on the `r^-5` scale;
* the available absolute remote bound is not relative to that scale; and
* the complete next local layer is the explicit 190-term bank in (4.1).

For `j>=3`, exact evaluations show substantially better conditioning in
some fixed-level regimes and deterioration again near the top modules, but
no uniform theorem is asserted here.  The next proof should therefore
split at least

\[
 j=2,\qquad 3\le j\le r-C,\qquad j=r-d,              \tag{5.1}
\]

rather than apply one blunt absolute perturbation estimate.  At `j=2`, one
must resum the five-vertex bank and control all later clusters in the same
shore-adapted norm.  In the other regimes, the same exact Venn evaluator can
test and then prove the appropriate uniform relative scale.

Nothing in this note changes the exact reduction

\[
 \inf_{2\le j\le r-2}\rho^{(0)}_{r,j}\ge r^{-C}.       \tag{5.2}
\]

It sharpens what is required to prove it.

## 6. Authentication

The exact checker is

`scratch/verify_gate_b_j2_local_scale_and_five_vertex_bank_20260822.py`.

Its SHA-256 digest is

`dab28604a36c517478db1529bb7a6ddb74ef532a1e24a26816d8a7d574736eab`.

It verifies (3.1)--(3.5) against the root-subset-free evaluator for
`6<=r<=18`, checks (3.8), and replays the complete topology census (4.1)
for every `9<=r<=80`.  With `--deep`, it also recomputes the exact integers
in (4.3).  The evaluator is

`scratch/research_gate_b_local_atoms_fast_venn_20260822.py`.

Its SHA-256 digest is

`ac53061e70687df50e88f068e8feb517291edd9b388392aa298039d1423738fa`.

The checker authenticates this evaluator and the three imported frozen
Venn/Hahn helpers before doing any arithmetic.

The checker is a replay, not a premise of the algebraic proof above.
