# The physical basepoint plateau in the multikernel Hamming-fibre factor

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

The multikernel construction in
`MATH_ATTACK_R_MULTIKERNEL_RAINBOW_TILING_20260726.md` balances its
**direction-set** ledger, but its actual physical face ledger has a
deterministic and very large collision plateau.  The obstruction is already
inside each top-level right-cycle fibre and is unaffected by the random
coordinate conjugations, balanced merge words, merge phases, affine
translations, or by using different physical pair frames in different
owner-disjoint cells.

Write the top dimension as

\[
                         h=2d.
\]

Here \(d\) is a power of two, as in the recursive construction.  The
counting argument below in fact needs only that the displayed parallel
factor and the top product factor exist.

For every integer \(1\le q<d\) satisfying

\[
                         2^{q/4}\ge 6d(q+1),             \tag{0.1}
\]

the forward depth-\(q\) face histogram of one multikernel factor on
\(Q_{2d}\) has factorial pair count

\[
 \boxed{
 P_q\ge
 2^{2d}\,{2^{q/4}\over36d(q+1)^2}.}                    \tag{0.2}
\]

Every ordinary orientation-cube embedding into a Boolean middle layer
maps equality of cube faces to equality of both their physical lower and
upper targets.  Consequently (0.2) holds separately for the physical lower
and upper histograms.

In particular, if \(q=\lfloor a\sqrt h\rfloor\), where \(a>0\) is fixed,
then

\[
 {P_q\over2^h}
 \ge {2^{a\sqrt h/4+O(1)}\over18h(q+1)^2}
 \longrightarrow\infty.                               \tag{0.3}
\]

Thus a bank of such cells containing \(G=W-o(W)\) middle owners has
\(P_q^\pm/W\to\infty\) at one Gaussian depth.  In the ambient Boolean
problem the balanced floor/ceiling baseline is only \(O_A(W)\) for
\(q\le A\sqrt m\).  Hence its collision excess is not merely non-vanishing:
it is \(\omega(W)\).  The joint pair-energy hypothesis of the outer literal
Hall theorem therefore fails decisively.

There is also a direct Hall plateau.  Without using direction balance,
the same packet geometry forces a duplicate fraction
\(1/2-o(1)\) at a sub-Gaussian depth.  Using the proved multikernel
direction balance strengthens this to \(1-o(1)\) whenever
\(q/\log h\to\infty\).  In particular, at
\(q=(1+o(1))(\log_2d)^2\), an ordinary mixed-frame embedding misses

\[
                         W-o(W)
\]

physical lower targets and the same number of upper targets.  This holds
for the balanced factor selected by the multikernel theorem and survives
an \(o(W)\)-owner completion.

The internal obstruction does have a precise repair: replace every
refreshed left Hamming factor by the recursive half-depth trace-rainbow
factor.  The direction proof is template-independent after coordinate
averaging, and the modified construction becomes internally face-simple
outside an aggregate \(o(W)\) occurrence quarantine.  Independent outer
cell choices still retain the separate \(e^{-\lambda_q}\) missing plateau;
the exact surviving requirement is negative cross-cell Gram cancellation.

The obstruction is not to mixed pair frames in general.  It is to the
specific operation used at every multikernel doubling step: over one right
cycle, all left cycles come from a single parallel one-order Hamming
factor.  To escape it, one must refresh basepoints *inside* a right-cycle
fibre, replace that parallel factor by a genuinely trace-rainbow factor, or
construct an exterior-moving packet in which equal abstract left traces no
longer have one common physical pair-frame chart.

## 1. Face traces and factorial collisions

Let \(F\) be an oriented isometric cycle factor of \(Q_s\).  For a start
\(x\), let \(D_q^F(x)\) be the set of the \(q\) directions in the forward
window, and encode its affine face by

\[
 \tau_q^F(x)=
 \left(D_q^F(x),x|_{[s]\setminus D_q^F(x)}\right).       \tag{1.1}
\]

For a trace \(t\), put

\[
 n_q(t)=|\{x:\tau_q^F(x)=t\}|,
 \qquad
 P_q(F)=\sum_t\binom{n_q(t)}2.                          \tag{1.2}
\]

If \(Q_s\) is embedded as the orientation cube of \(s\) split physical
pairs, with all full, empty, and external coordinates fixed, the lower
intersection and upper union of a \(q\)-face are both injective functions
of its trace (1.1).  Indeed, the lower target makes precisely the active
pairs in \(D\) empty and records the chosen endpoint of every other split
pair; the upper target makes precisely those pairs full and records the
same outside orientations.  Therefore

\[
P_q^-(F)=P_q^+(F)=P_q(F)                               \tag{1.3}
\]

inside one such physical cell.

The earlier multikernel theorem controls only the row sums of this
histogram.  For a direction set \(D\in\binom{[h]}q\) and an affine
basepoint class \(b\in Q_h/\langle D\rangle\), write

\[
 r_q(D,b)=\#\{x:\tau_q^F(x)=(D,b)\}.                  \tag{1.4}
\]

If \(A_q(D)\) is the number of factor cycles whose cyclic order contains
\(D\) as a \(q\)-interval, then every such cycle contributes its two
antipodal faces, and therefore

\[
\boxed{\sum_b r_q(D,b)=2A_q(D).}                      \tag{1.5}
\]

There are \(2^{h-q}\) basepoint classes.  Hence, on every good direction
set in the multikernel theorem,

\[
\boxed{
 {1\over2^{h-q}}\sum_b r_q(D,b)
 =(1\pm\varepsilon_h){2^q\over\binom hq}.}            \tag{1.6}
\]

The quantity on the right is the density of selected affine \(q\)-faces
inside one orientation cube.  It is much smaller than one in the
Gaussian range.  Equation (1.6) is an exact average over basepoints; it
does not bound any individual \(r_q(D,b)\), its support size, or its
factorial second moment.  The next sections compute the concentration
which the specific Hamming-fibre construction hides behind this small
average.

## 2. One-order Hamming image bound

Let \(\mathcal P_d\) be a parallel Hamming factor on \(Q_d\): every cycle
has the same cyclic direction order, up to a common coordinate
conjugation.  At depth \(a<d\), only the \(d\) cyclic \(a\)-sets in that
order can occur.  For each direction set there are at most \(2^{d-a}\)
outside orientations.  Hence

\[
 \boxed{
 |\tau_a^{\mathcal P_d}(Q_d)|\le d\cdot2^{d-a}.}        \tag{2.1}
\]

This bound survives every coordinate permutation and every affine
translation of the whole factor.  Such a conjugacy only relabels the trace
domain and image.

## 3. Product-trace factorization

Fix a right cycle \(D\) of length \(2d\).  Over this cycle, the
multikernel construction places one coordinate-conjugated parallel
Hamming factor \(\mathcal P_L(D)\) on \(Q_L\), \(|L|=d\).  For every left
cycle \(C\), an arbitrary balanced merge and phase factors \(C\times D\)
into isometric \(4d\)-cycles.  The merge words and phases may be chosen
completely differently for different \(C\)'s; no randomness is assumed in
this report.

For a product start \(z=(x,y)\in Q_L\times V(D)\), let

\[
 a(z)=\text{the number of left directions in its output }q\text{-window},
 \qquad b(z)=q-a(z).                                    \tag{3.1}
\]

Projecting the interleaved geodesic window onto its two factors gives an
\(a(z)\)-step forward segment of the left cycle starting at \(x\) and a
\(b(z)\)-step forward segment of \(D\) starting at \(y\).  Therefore the
full face trace is exactly determined by the ordered pair

\[
 \left(\tau_{a(z)}^{\mathcal P_L(D)}(x),
       \tau_{b(z)}^D(y)\right).                         \tag{3.2}
\]

Conversely, restricting a full trace to \(L\) and \(R\) recovers this
pair.  In particular, among all starts with \(a(z)=a\), the number of
possible traces is at most

\[
 \boxed{
 M_a\le
 \bigl(d2^{d-a}\bigr)(2d)
 =2d^2\cdot2^{d-a}.}                                  \tag{3.3}
\]

The second factor \(2d\) is only the number of starts on the single right
cycle; no injectivity assertion about that right trace is needed.

## 4. Every balanced merge has a large-left stratum

The right-cycle fibre has

\[
 V=|Q_L\times V(D)|=2d\cdot2^d                         \tag{4.1}
\]

starts.  Put

\[
 V_a=|\{z:a(z)=a\}|.                                    \tag{4.2}
\]

Every output cycle is isometric on the \(2d\) directions and has exactly
\(d\) left and \(d\) right directions in its first half.  On a cyclic
word, every direction occurrence lies in exactly \(q\) forward
\(q\)-windows.  Consequently, after summing over all output cycles in the
fibre,

\[
 \sum_{a=0}^qV_a=V,
 \qquad
 \sum_{a=0}^q aV_a={qV\over2}.                          \tag{4.3}
\]

Let \(B=\sum_{a\ge q/4}V_a\).  Since \(a<q/4\) off this range and
\(a\le q\) everywhere, (4.3) gives

\[
 {qV\over2}
 \le {q\over4}(V-B)+qB,
\]

and hence

\[
                         B\ge {V\over3}.                \tag{4.4}
\]

There are at most \(q+1\) possible integer values of \(a\).  Thus some
\(a_*\ge q/4\) satisfies

\[
 \boxed{
 V_{a_*}\ge {V\over3(q+1)}.}                            \tag{4.5}
\]

Combining (3.3) and (4.5), the average nonzero trace multiplicity in this
stratum is at least

\[
 \boxed{
 {V_{a_*}\over M_{a_*}}
 \ge {2^{a_*}\over3d(q+1)}
 \ge {2^{q/4}\over3d(q+1)}.}                            \tag{4.6}
\]

This is the physical basepoint plateau.  For example, at least half of
the occurrences in the stratum lie on traces whose multiplicity is at
least one half of the right side of (4.6); otherwise all \(M_{a_*}\)
traces together would carry fewer than \(V_{a_*}/2\) such occurrences.
Thus at least \(V/[6(q+1)]\) fibre occurrences lie on physical faces of
multiplicity at least

\[
                         {2^{q/4}\over6d(q+1)}.          \tag{4.7}
\]

## 5. Exact collision lower bound

Let \(n_t\) be the loads of the traces in the \(a_*\)-stratum.  By
Cauchy--Schwarz, (3.3), and (4.5),

\[
 \begin{aligned}
 \sum_t\binom{n_t}{2}
 &=\frac12\left(\sum_tn_t^2-V_{a_*}\right)\\
 &\ge\frac12\left({V_{a_*}^2\over M_{a_*}}-V_{a_*}\right).
                                                               \tag{5.1}
 \end{aligned}
\]

Under (0.1), (4.6) is at least two.  Hence (5.1) is at least
\(V_{a_*}^2/(4M_{a_*})\), and the displayed bounds give

\[
 \boxed{
 P_q(\text{one right-cycle fibre})
 \ge {2^{d+a_*-1}\over9(q+1)^2}
 \ge {2^{d+q/4-1}\over9(q+1)^2}.}                      \tag{5.2}
\]

There are exactly

\[
                         N_d={2^{d-1}\over d}            \tag{5.3}
\]

right cycles, and their owner sets \(Q_L\times V(D)\) are disjoint.
Factorial pairs already formed inside one such set remain collision pairs
in the full histogram.  Summing (5.2) over (5.3) proves

\[
 \begin{aligned}
 P_q(Q_{2d})
 &\ge {2^{2d+q/4-2}\over9d(q+1)^2}\\
 &=2^{2d}{2^{q/4}\over36d(q+1)^2},                     \tag{5.4}
 \end{aligned}
\]

which is (0.2).

The proof used only the parallel one-order nature of the left factor and
the fact that every output cycle has a balanced left/right direction
ledger.  It applies to every possible deterministic choice of coordinate
conjugations, merge words, and phases.  In particular, selecting a rare
outcome of the direction-ledger concentration argument cannot evade it.

### 5.1 A direct positive-density Hall plateau

The same packet count gives a stronger statement about distinct physical
targets, without passing through quadratic energy.  For an integer
\(0\le k<q/2\), put

\[
                         B_k=\sum_{a\ge k}V_a.          \tag{5.5}
\]

Using (4.3), \(a\le k\) off this range, and \(a\le q\) everywhere gives

\[
 {qV\over2}\le k(V-B_k)+qB_k,
\]

and therefore

\[
 \boxed{
 B_k\ge {q/2-k\over q-k}\,V.}                         \tag{5.6}
\]

By (3.3), all strata with \(a\ge k\) together use at most

\[
 \sum_{a=k}^q2d^2\,2^{d-a}
 \le4d^2\,2^{d-k}                                    \tag{5.7}
\]

distinct traces.  Hence their duplicate excess, and therefore the
duplicate excess \(C_q^{\rm fib}=V-|\operatorname {im}\tau_q|\) of the
whole right-cycle fibre, satisfies

\[
\boxed{
 C_q^{\rm fib}
 \ge V\left(
 {q/2-k\over q-k}-2d\,2^{-k}
 \right).}                                            \tag{5.8}
\]

Duplicate excess is superadditive when occurrence families are merged:
equal traces belonging to different fibres can only reduce the size of
the union image.  Summing (5.8) over all right cycles and then over all
owner-disjoint physical cells gives, separately for both signs,

\[
\boxed{
 C_q^\pm
 \ge G\left(
 {q/2-k\over q-k}-2d\,2^{-k}
 \right).}                                            \tag{5.9}
\]

Put \(L=\log_2d\).  Take \(q\) to be the largest multiple of four not
exceeding \(L^3\), and put \(k=\lceil L^2\rceil\).  Then

\[
 q=o(\sqrt h),\qquad
 {k\over q}=o(1),\qquad
 2d\,2^{-k}=o(1),
\]

so

\[
\boxed{C_q^\pm\ge(1/2-o(1))G.}                        \tag{5.10}
\]

Let \(N_q\) be the ambient number of signed physical targets.  For a
histogram of \(G\) occurrences the exact identity is

\[
 M_q^\pm=N_q-G+C_q^\pm,                               \tag{5.11}
\]

where \(M_q^\pm\) is the number of missed targets.  If \(h\le m\),
then the chosen \(q\) is \(o(\sqrt m)\), so \(N_q=W-o(W)\).  For
\(G=W-o(W)\), (5.10)--(5.11) give

\[
\boxed{M_q^\pm\ge(1/2-o(1))W.}                        \tag{5.12}
\]

Adding the \(W-G=o(W)\) omitted owners can cover at most that many new
targets, so the same asymptotic lower bound survives every completion.
Thus the original Hamming-fibre multikernel factor violates the outer
literal Hall theorem directly at a sub-Gaussian depth lying inside every
fixed window \(q\le A\sqrt h\).

### 5.2 Direction balance strengthens the plateau to \(1-o(1)\)

The preceding \(1/2-o(1)\) bound used no conclusion of the direction
concentration theorem.  For the factor actually selected there, almost
every start lies in a central left/right split, which gives a sharper
result.

Let

\[
 \mathcal C_q=
 \left\{S\in\binom{[h]}q:
 {q\over3}\le|S\cap L|\le{2q\over3}\right\}.           \tag{5.13}
\]

For a uniform \(q\)-set, hypergeometric Hoeffding gives

\[
 {|\binom{[h]}q\setminus\mathcal C_q|\over\binom hq}
 \le2e^{-q/18}.                                       \tag{5.14}
\]

At most a

\[
 \delta_{h,q}
 =\binom{d_0}{2}{q(q-1)\over h(h-1)}+2rh^{-8}
\]

fraction of all supports are exceptional in the multikernel theorem, and
every nonexceptional support has at least a
\((1-\varepsilon_h)\)-fraction of its uniform start load.  Hence the
number \(X_q^\pm\) of signed starts whose support is both central and
nonexceptional satisfies

\[
\boxed{
 X_q^\pm\ge
 (1-\varepsilon_h)
 (1-\delta_{h,q}-2e^{-q/18})\,2^h.}                  \tag{5.15}
\]

Put \(k=\lceil q/3\rceil\).  In one right-cycle fibre, (3.3) bounds the
number of traces in all central strata by

\[
 \sum_{a=k}^{q}2d^2\,2^{d-a}
 \le4d^2\,2^{d-k}.                                    \tag{5.16}
\]

After multiplication by the \(N_d=2^{d-1}/d\) right fibres, all central
starts of one \(Q_h\)-cell occupy at most

\[
\boxed{Y_q\le2d\,2^{h-k}}                              \tag{5.17}
\]

physical traces.  Therefore

\[
\boxed{
 C_q^\pm\ge X_q^\pm-Y_q,}                             \tag{5.18}
\]

and Cauchy--Schwarz also gives

\[
\boxed{
 P_q^\pm\ge{(X_q^\pm)^2\over2Y_q}-{X_q^\pm\over2}.}   \tag{5.19}
\]

Uniformly for \(q\le A\sqrt h\), one has
\(\delta_{h,q}+\varepsilon_h=o_A(1)\).  If in addition

\[
                         {q\over\log h}\longrightarrow\infty,     \tag{5.20}
\]

then \(e^{-q/18}=o(1)\) and \(Y_q/2^h\le2d\,2^{-q/3}=o(1)\).
Equations (5.15)--(5.19) become

\[
\boxed{
 C_q^\pm=(1-o_A(1))2^h,\qquad
 P_q^\pm\ge
 (1-o_A(1))\,2^h{2^{q/3}\over4d}.}                   \tag{5.21}
\]

The same statements sum over owner-disjoint mixed-frame cells.  Taking
\(q=\lceil(\log_2d)^2\rceil\), adjusting by at most one if needed, gives
\(q=o(\sqrt h)\) and (5.20).  If \(G=W-o(W)\) and \(h\le m\), then
\(N_q=W-o(W)\), so the exact identity (5.11) and arbitrary
\(o(W)\)-owner completion yield

\[
\boxed{M_q^\pm=W-o(W).}                               \tag{5.22}
\]

Thus direction balance and physical basepoint balance are not merely
logically distinct here: in the original construction they coexist with
an asymptotically total literal-Hall failure.

## 6. Mixed physical pair frames do not cancel the plateau

Consider owner-disjoint orientation-cube cells, possibly embedded using
different physical pair frames, different fixed spectators, and different
affine cube charts.  Install the multikernel factor in every cell.  Let
\(x_{c,q}^\pm(T)\) be the physical lower or upper target histogram of cell
\(c\).  By (1.3) and (5.4),

\[
 \sum_T\binom{x_{c,q}^\pm(T)}2
 \ge |c|\,{2^{q/4}\over36d(q+1)^2}.                    \tag{6.1}
\]

For the aggregate histogram \(x_q^\pm=\sum_cx_{c,q}^\pm\), the exact
collision decomposition is

\[
 \sum_T\binom{x_q^\pm(T)}2
 =\sum_c\sum_T\binom{x_{c,q}^\pm(T)}2
  +\sum_{c<c'}\sum_Tx_{c,q}^\pm(T)x_{c',q}^\pm(T).      \tag{6.2}
\]

The cross-cell term is nonnegative.  If the cells contain altogether
\(G\) owners, (6.1)--(6.2) yield

\[
 \boxed{
 P_q^\pm\ge
 G\,{2^{q/4}\over36d(q+1)^2}.}                         \tag{6.3}
\]

Thus changing pair frames *between* cells merely relabels the internal
plateaux and may add cross-frame collisions.  It cannot remove a collision
pair which is already present inside one cell.

## 7. Failure of the outer literal-Hall pair-energy interface

For the ambient middle-layer problem, let \(W\) be the number of middle
owners and \(N_q\) the number of lower or upper rank targets.  Throughout
\(q\le A\sqrt m\),

\[
 {W\over N_q}=O_A(1),                                   \tag{7.1}
\]

so the balanced floor/ceiling factorial baseline satisfies

\[
                         P_q^{\min}=O_A(W).              \tag{7.2}
\]

Suppose \(h\le m\), choose fixed \(0<a<A\), and put
\(q=\lfloor a\sqrt h\rfloor\).  Suppose also that
\(G=W-o(W)\) owners are partitioned into physical \(Q_h\)-cells,
\(h=2d\), carrying the multikernel factors above.  The remaining owners,
however completed, can only add nonnegative collision pairs.  Equations
(6.3)--(7.2) imply

\[
 \Pi_q^\pm=P_q^\pm-P_q^{\min}
 \ge
 (W-o(W)){2^{q/4}\over36d(q+1)^2}-O_A(W).              \tag{7.3}
\]

For \(q=\lfloor a\sqrt h\rfloor\) and \(h\to\infty\), the coefficient of
\(W\) on the right tends to infinity.  Hence

\[
                         \Pi_q^-+\Pi_q^+=\omega(W).      \tag{7.4}
\]

This contradicts the needed pair-energy condition even at one depth, and
a fortiori contradicts its weighted sum through a Gaussian window.
Explicitly, writing

\[
 c_j=\left\lfloor {W\over N_j}\right\rfloor,
\]

it contradicts the sharp sufficient pair-energy condition

\[
 \sum_{j\le A\sqrt m,\ \epsilon=\pm}
 {\Pi_j^\epsilon\over\binom{c_j+1}{2}}=o(W),           \tag{7.5}
\]

because \(1\le c_q=O_A(1)\).  The denominator in (7.5) is the exact
scalar cost of a hole at floor \(c_j\), not an unspecified constant.

The outer mixed-frame literal Hall theorem is not contradicted.  That
theorem may assign each owner occurrence to any compatible physical
\(q\)-face and then use an integral convex min-cost flow to choose nearly
balanced loads.  An actual cycle factor supplies only the single face
given by the consecutive \(q\)-window at that owner.  The multikernel
factor's direction support says that almost every direction set occurs the
right number of times; it says nothing about the projected basepoint map.
Sections 4--6 prove that this restricted consecutive-window map has huge
self-collision energy.  Therefore the Hall assignment cannot be composed
with this factor.

In the block Gram decomposition, the same obstruction can be recorded in
either of two ways:

* taking each right-cycle fibre as a block gives the internal terms (5.2);
* taking individual output cycles as shadow-simple blocks moves exactly
  the same pairs into their positive pairwise overlap terms.

Changing the block granularity does not change the physical histogram.
Centered cross terms cannot repair (7.4), because the raw factorial count
already exceeds the entire balanced baseline by \(\omega(W)\).

## 8. Exact functional Hall and Gram identities

The relation to the outer literal theorem can be stated without any
sufficient-condition slack.  Let the retained physical packets or cells
be indexed by \(P\), and at a fixed signed depth write

\[
 z_P(T)=\text{the number of actual consecutive windows in \(P\)
                     whose physical target is \(T\)},              \tag{8.1}
\]

\[
 n(T)=\sum_Pz_P(T),\qquad
 A=\sum_Tn(T),\qquad N=\#\{T\}.                        \tag{8.2}
\]

Every retained owner start has one actual target.  Hence the
owner--target graph is functional on the owner side, and its maximum
matching contains exactly one edge for every hit target.  Therefore its
target-side Hall deficiency is exactly

\[
\boxed{
 \operatorname {def}G
 =\sum_T(1-n(T))_+
 =\#\{T:n(T)=0\}.}                                    \tag{8.3}
\]

Thus the outer literal Hall theorem for actual cycle windows asks for

\[
\boxed{
 \sum_{q\le H,\ \epsilon=\pm}
 \#\{T:n_q^\epsilon(T)=0\}=o(W).}                     \tag{8.4}
\]

This must not be confused with the already proved Hall theorem for all
compatible faces of a frozen owner frame: that larger graph lets an owner
choose a face which need not be a consecutive window of its cycle.

Put

\[
 \lambda={A\over N}=c+\theta,\qquad
 c=\lfloor\lambda\rfloor,\quad0\le\theta<1,            \tag{8.5}
\]

and

\[
 P=\sum_T\binom{n(T)}2,\qquad
 P_{\rm bal}=cA-\binom{c+1}{2}N.                       \tag{8.6}
\]

The second expression is the exact factorial pair count of a
floor/ceiling load vector with mean \(\lambda\).  For every integer
\(u\ge0\),

\[
 \binom u2-cu+\binom{c+1}{2}
 ={(u-c)(u-c-1)\over2}\ge0.                            \tag{8.7}
\]

Summing (8.7) over targets gives

\[
\boxed{
 \#\{T:n(T)=0\}\binom{c+1}{2}
 \le P-P_{\rm bal}\qquad(c\ge1).}                     \tag{8.8}
\]

The constant is sharp at the scalar energy level because a hole
\(u=0\) contributes exactly \(\binom{c+1}{2}\) to (8.7).  When \(c=0\),
the corresponding elementary bound is

\[
 \#\{T:n(T)=0\}\le N-A+P.                              \tag{8.9}
\]

There is also an exact random-law Gram identity.  Suppose the legal
packet histograms \(z_P\) are jointly random, put

\[
 Y_P=z_P-\mathbb Ez_P,\qquad
 K_{PP'}=\mathbb E\langle Y_P,Y_{P'}\rangle,           \tag{8.10}
\]

and retain the deterministic total mass \(A\).  Since

\[
 2(P-P_{\rm bal})
 =\|n-\lambda\mathbf1\|_2^2-N\theta(1-\theta),
\]

expectation and variance decomposition give

\[
\boxed{
\begin{aligned}
 2\mathbb E(P-P_{\rm bal})
 ={}&\|\mathbb En-\lambda\mathbf1\|_2^2
   +\sum_PK_{PP}+2\sum_{P<P'}K_{PP'}\\
  &-N\theta(1-\theta).
\end{aligned}}                                        \tag{8.11}
\]

If packets are internally face-simple, their diagonal variance has order
\(A\).  A coefficient-one conclusion therefore needs negative
cross-packet Gram cancellation of the same order.  Independent packet
choices have \(K_{PP'}=0\) for \(P\ne P'\) and cannot provide it.

Even after replacing the present Hamming fibres by an ideal
shadow-injective factor, independent uniform affine choices retain a
second, outer plateau.  If a target has \(d(T)\) candidate cells and a
uniform conjugate hits its unique candidate face with

\[
                         p={2^q\over\binom hq},         \tag{8.12}
\]

then

\[
 \mathbb E M=\sum_T(1-p)^{d(T)},\qquad
 \mathbb EP=p^2\sum_T\binom{d(T)}2.                   \tag{8.13}
\]

The exact first moment is \(\sum_Td(T)=A/p\).  Convexity yields

\[
 {\mathbb EM\over N}
 \ge(1-p)^{\lambda/p}\longrightarrow e^{-\lambda},    \tag{8.14}
\]

and

\[
 \mathbb EP
 \ge {N\over2}\bigl(\lambda^2-\lambda p\bigr).         \tag{8.15}
\]

At shallow depth \(\lambda=1+o(1)\) and \(p=o(1)\), these are respectively
the \(e^{-1}\) missing plateau and a \((1/2-o(1))N\) collision plateau.
At fixed Gaussian height \(\lambda=O_A(1)\), both remain positive-density
constants.  Hence internal trace-rainbowness is necessary but not
sufficient: the outer choices must be correlated so that the
off-diagonal term in (8.11) cancels the diagonal variance.

## 9. A trace-rainbow fibre replacement removes the internal plateau

The Hamming-fibre obstruction can be removed without changing the
direction-support theorem.  This does not solve the outer Gram problem,
but it separates the two gates exactly.

Let \(R_d\) be the audited recursive factor whose forward and reverse
trace maps are injective through depth \(d/2\).  Modify the multikernel
recursion as follows:

1. use \(R_{d_0}\) on the anchor;
2. over every right cycle at a \(d\)-to-\(2d\) step, use an independently
   coordinate-conjugated copy \(\rho_DR_d\rho_D^{-1}\) on the entire left
   cube;
3. retain the same independently chosen balanced torus merges and phases.

### Theorem 9.1 (internal trace-rainbow repair)

For every fixed \(A\), the modified construction has the same direction
balance, the same exceptional proportion

\[
 \delta_{h,q}
 =\binom{d_0}{2}{q(q-1)\over h(h-1)}+2rh^{-8},         \tag{9.1}
\]

and the same relative error \(\varepsilon_h\) as the original
multikernel theorem.  Moreover, for every spine-sparse direction set
\(S\), both physical trace maps are injective on the starts whose
depth-\(q\) support is \(S\).

If \(B_q^\pm\) is the number of starts at signed depth \(q\) whose support
is not spine-sparse, then

\[
 B_q^\pm
 \le(\delta_{h,q}+\varepsilon_h)2^h.                  \tag{9.2}
\]

Consequently, for every \(H\le A\sqrt h\),

\[
\begin{aligned}
 {1\over2^h}\sum_{q=1}^H B_q^\pm
 \le{}&
 \binom{d_0}{2}
 {H(H+1)(H-1)\over3h(h-1)}\\
 &+2rHh^{-8}+H\varepsilon_h
 =O_A\!\left({r^6\over\sqrt h}\right)=o(1).           \tag{9.3}
\end{aligned}
\]

Thus, after quarantining \(o(2^h)\) signed depth occurrences in aggregate,
every retained window is internally face-simple.

#### Proof

For an arbitrary exact isometric factor \(F\) on \(Q_d\), let
\(A_a^F(U)\) be its cycle load on direction set \(U\).  Every cycle
supplies \(d\) cyclic \(a\)-intervals, so

\[
 \sum_{|U|=a}A_a^F(U)=N_dd=2^{d-1}.                  \tag{9.4}
\]

For a uniform coordinate permutation \(\rho\),

\[
 \boxed{
 \mathbb E_\rho A_a^{\rho F\rho^{-1}}(S)
 ={2^{d-1}\over\binom da}.}                           \tag{9.5}
\]

The original packet proof uses the left factor only through this
expectation.  Multiplying (9.5) by the unchanged torus coefficients
\(\alpha_{d;a,b}\) or \(\beta_{d;0,b}\) reproduces the packet mean exactly.
Packet independence, packet cap \(2^{d-1}\), exact ownership, and the
Hoeffding argument are unchanged.  At the anchor, the permitted nonempty
sets are singletons, whose cycle load is exact in every factor.  Hence the
complete direction theorem survives verbatim.

It remains to prove trace injectivity.  Consider two equal output
depth-\(q\) traces with common support

\[
                         S=S_L\sqcup S_R,
 \qquad a=|S_L|,\quad b=|S_R|.                         \tag{9.6}
\]

Projection of an interleaved product window to the left and right factors
gives respectively the consecutive parent \(a\)-trace and \(b\)-trace.
Equality of the global traces therefore implies equality of both parent
traces.  For a spine-sparse support, \(a<d/2\), so two-sided injectivity of
\(R_d\) identifies the left start.  The restricted support \(S_R\) is
again spine-sparse, so induction identifies the right start.  The product
start is therefore unique.  The argument is identical for reverse
windows.  The base case has anchor support of size at most one and follows
from the depth-one injectivity of \(R_{d_0}\).

Finally, every good direction set carries at least

\[
 (1-\varepsilon_h){2^h\over\binom hq}
\]

start occurrences, while at least a \(1-\delta_{h,q}\) fraction of all
direction sets are good.  The bad occurrence mass is at most

\[
 [1-(1-\delta_{h,q})(1-\varepsilon_h)]2^h
 \le(\delta_{h,q}+\varepsilon_h)2^h,
\]

which proves (9.2).  Summing \(q(q-1)\) gives
\(H(H+1)(H-1)/3\), proving (9.3). \(\square\)

The conclusion is deliberately a quarantine statement.  Without deleting
the bad occurrences, their factorial collision count could still be as
large as their mass times \(2^q\).  After deletion, the diagonal
within-cell collision term is zero.  The cross-cell physical overlaps and
the negative Gram cancellation required by (8.11) remain completely open.

## 10. Exact scope and possible escapes

### Proved obstruction

The lower bound applies whenever:

1. a top-level product has two \(d\)-direction halves;
2. over each fixed right cycle, the complete left owner cube carries one
   parallel one-order factor;
3. every product torus is rebundled into isometric cycles, hence has the
   balanced left/right direction ledger; and
4. the fibre is embedded through one ordinary physical orientation-cube
   chart, so a cube face has one literal lower and upper target.

These are exactly the features of the reported multikernel construction
and its ordinary mixed-pair-frame embedding.

### Repair status and remaining escapes

Theorem 9.1 proves that replacing the parallel Hamming factor by the
recursive trace-rainbow factor removes the internal obstruction after an
aggregate \(o(W)\) quarantine.  It does not supply the negative outer Gram
term.  The remaining alternatives not ruled out here are:

1. a legal packet which refreshes the physical pair-frame chart separately
   inside one right-cycle fibre while preserving all crossing collars;
2. an exterior-moving construction in which the product trace no longer
   factors as (3.2); or
3. a correlated joint selection of the trace-rainbow repaired factors from
   the outer Hall graph, satisfying (8.11).

Further concentration of the original Hamming-fibre coordinate
permutations or merge phases cannot help.  After Theorem 9.1, the precise
positive continuation is outer cross-packet correlation.

## 11. Independent audit

The decisive calculation was checked independently from the explicit
torus parametrization.  In one torus, every cyclic merge position occurs
with exactly \(2d\) product vertices, and a balanced merge word satisfies

\[
 \sum_{t\bmod 2d}
 |\{u\in[t,t+q):\sigma_u=L\}|=qd.
\]

This recovers (4.3) directly.  The auditor also verified the product-image
bound (3.3) and the constants in (5.2)--(5.4); its form
\(2^{d+a_*}/(18(q+1)^2)\) for one fibre is identical to (5.2).

The direct Hall plateau was audited separately.  The check recovered
(5.6), the geometric support sum \(4d^2\,2^{d-k}\), superadditivity of
occurrence-minus-support duplicate excess, and the exact identity
\(M=N-G+C\).  Taking \(q\sim(\log_2d)^3\) and
\(k\sim(\log_2d)^2\) gives the independently verified constant
\(1/2-o(1)\).

The direction-balanced refinement (5.13)--(5.22) was independently
rederived from the hypergeometric Hoeffding tail and the same image
census.  The audit obtained the identical central-start lower bound,
the capacity \(Y_q\le2d\,2^{h-\lceil q/3\rceil}\), and hence the
\(1-o(1)\) duplicate and missing fractions whenever
\(q/\log h\to\infty\).

Finally, two independent audits checked Theorem 9.1.  Both recovered the
template-independent mean (9.5), confirmed trace projection for arbitrary
merge words and phases in both orientations, and obtained the same
summed exceptional-mass formula (9.3).  Both also confirmed the stated
boundary: the repair proves an \(o(W)\) internal occurrence quarantine,
not a factorial bound on the discarded starts and not the outer
cross-cell Gram cancellation.
