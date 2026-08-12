# Pair-square decay and the hereditary bow-tie gate

Date: 2026-07-25

Method: pure mathematics only.  No computation or search is used.

## 0. Outcome

This note isolates the exact binary/common-link covariance skeleton in
the geodesic catalogue nibble and proves that its **raw** value is already
summable on the coefficient-one scales.  The nonlinear priority version
is the weighted four-walk (6.3), whose hereditary estimate remains open.

For the symmetrized bounded-displacement **geodesic-chunk** catalogue, let

\[
 K(x,y)=\frac{d(x,y)}{\sqrt{d(x)d(y)}}
 \tag{0.1}
\]

be the symmetrically normalized codegree kernel on the protected target
fibres.  The diagonal is removed whenever (x,y) are in the same fibre.
If (x) has rank (r), and (K_h(x,\cdot)) is its row restricted to
rank (r+h), then the exact pair formula gives

\[
 \|K_0(x,\cdot)\|_2^2=O_D(m^{-2})
 \tag{0.2}
\]

and, for (h\ne0),

\[
 \|K_h(x,\cdot)\|_2^2
 \le C_D (|h|+1)^2 |h|!\left(\frac{C_D}{m}\right)^{|h|}.
 \tag{0.3}
\]

Consequently

\[
 \sum_h\|K_h(x,\cdot)\|_2=O_D(m^{-1/2}).
 \tag{0.4}
\]

Every rank-to-rank block of (K) has operator norm at most
((1+o(1))g), where (g=m^{1/2+o(1)}) is the chunk length.  A further
cover/remainder split improves the bow-tie energy to

\[
 \boxed{
 \sum_{\substack{y,z\ne x\\y\ne z}}
 K(x,y)K(y,z)K(z,x)
 =O_D\left(\frac1{m^2}+\frac g{m^{3/2}}\right).}
 \tag{0.5}
\]

The diagonal contribution is (O_D(1/m)).  Thus the full raw triangle
energy is

\[
 O_D\left(\frac1m+\frac g{m^{3/2}}\right)=m^{-1+o(1)}.
 \tag{0.5a}
\]

This remains summable not only over (O(\log\log m)) effective nibble time
but also after aggregating all (2Q+1) protected target ranks.

The same proof is hereditary provided the residual pair-square profile
inflates by no more than the ideal factor (z^{-2}) at resource density
(z).  At the stopping density (z=1/\log m), this gives

\[
 \mathfrak T_z(x)
 \le m^{o(1)}(\log m)^2
 \left(\frac1m+\frac g{m^{3/2}}\right)
 =m^{-1+o(1)},
 \tag{0.6}
\]

and still closes the vertex-degree martingale.

Therefore the full exponential hereditary hierarchy is not needed for
the binary one-vertex degree covariance, nor for a priority process whose
hazard multipliers admit the corresponding weighted pair-square bound.
The remaining theorem is precisely the propagation of that weighted
pair-square profile (equivalently a weighted four-walk/bow-tie energy).
Section 6 gives the exact priority martingale kernel.

Under four-antichain quarantine, all raw estimates become easier: the bad
fraction is (m^{-5+o(1)}), and width-three intersections have a
summable (w\le C\log m) census.  A fixed (s=4) pruning is nevertheless
still impossible, because its retained degree is only polynomial.  The
viable version remains dynamic quarantine plus the weighted residual
four-walk estimate.

No claim of coefficient one is made.

## 1. Pair-square profile from the exact pair formula

Write (n=2m).  All ranks below lie in the protected band, so

\[
 r,n-r=m+O(Q),\qquad Q=o(m),
 \tag{1.1}
\]

and two flags in one carrier have symmetric-difference parameters at
most (H+O(Q)=o(m)).

Fix targets (S,T), with

\[
 |S|=r,\qquad |S\setminus T|=a,\qquad |T\setminus S|=b.
 \tag{1.2}
\]

Thus (h=|T|-|S|=b-a).  The proof of the exact pair formula in
`MATH_ATTACK_H_CATALOGUE_OVERLAP_HIERARCHY_20260725.md` applies verbatim
after restricting to a geodesic chunk: coordinate symmetry is unchanged,
and the claimed phase-pair count is merely restricted to the physical
chunk phases.  Together with the near-interval phase bound it implies

\[
 \frac{d(S,T)}{d(S)}
 \le
 \frac{C_D(1+a+b)}
 {\binom ra\binom{n-r}b}.
 \tag{1.3}
\]

The calibrated target degrees at every protected rank are
((1-o(1))A).  Hence replacing the left side of (1.3) by the symmetric
normalization (0.1) changes it by a factor (1+o(1)), uniformly in the
band.

For a fixed (S), the number of (T)'s with parameters ((a,b)) is

\[
 \binom ra\binom{n-r}b.
 \tag{1.4}
\]

Squaring (1.3) and summing (1.4) therefore gives

\[
 \sum_{T:\,(a,b)}K(S,T)^2
 \le
 \frac{C_D(1+a+b)^2}
 {\binom ra\binom{n-r}b}.
 \tag{1.5}
\]

This is the useful direction: one copy of the ambient pair count cancels,
but the second remains in the denominator.

### Lemma 1.1 (factorial rank-gap decay)

Uniformly for protected ranks,

\[
 \sum_{\substack{T:|T|=r\\T\ne S}}K(S,T)^2=O_D(m^{-2}),
 \tag{1.6}
\]

and for (h\ne0),

\[
 \sum_{T:|T|=r+h}K(S,T)^2
 \le C_D (|h|+1)^2 |h|!
 \left(\frac{C_D}{m}\right)^{|h|}.
 \tag{1.7}
\]

#### Proof

Assume first that (h\ge0), so (b=a+h).  Since
(a,b\le H+O(Q)=o(m)),

\[
 \binom ra\ge \frac{(m/2)^a}{a!},\qquad
 \binom{n-r}{a+h}\ge\frac{(m/2)^{a+h}}{(a+h)!}
 \tag{1.8}
\]

for all sufficiently large (m).  The (a)-th summand in (1.5) is at
most

\[
 C_D(1+2a+h)^2a!(a+h)!
 \left(\frac2m\right)^{2a+h}.
 \tag{1.9}
\]

The ratio of the ((a+1))-st term to the (a)-th is

\[
 O_D\left(\frac{(a+1)(a+h+1)}{m^2}\right)=o(1)
 \tag{1.10}
\]

uniformly through the allowed carrier range.  The series is therefore at
most twice its first term.  For (h>0), the first term is (a=0), which
is bounded by the right side of (1.7).  For (h=0), the diagonal term
(a=0) is omitted, so the first term is (a=1), giving (O_D(m^{-2})).
The case (h<0) follows by reversing (S,T), or identically by starting
with (a=b+|h|).  This proves (1.6)--(1.7).  \(\square\)

Taking square roots and using that the ratio of successive factorial
terms is (O(\sqrt{(|h|+1)/m})) proves

\[
 \boxed{
 \sum_h
 \left(\sum_{T:|T|=r+h,\,T\ne S}K(S,T)^2\right)^{1/2}
 =O_D(m^{-1/2}).}
 \tag{1.11}
\]

The leading terms are the two adjacent nested ranks.  Same-rank defect
one contributes only (O(m^{-2})) to the squared row norm.

### 1.2 Mixed exposed/claimed occurrences

The priority process needs a slightly more general form.  A base grid
**exposes** all (g) physical phases in every protected row, while a
decorated selected chunk **claims** only (c_r\le g) of them.  Put

\[
 k_r^{\rm exp}=g,\qquad k_r^{\rm cl}=c_r.
 \tag{1.11a}
\]

For either occurrence mode (\epsilon,\delta\in\{\rm exp,cl\}), define
the mixed symmetrically normalized codegree by dividing the
(\epsilon,\delta)-pair degree by the square root of its two occurrence
degrees.  The phase-pair numerator is at most

\[
 \min(k_r^\epsilon,k_{r+h}^\delta)C_D(1+a+b).
 \tag{1.11b}
\]

After symmetric normalization, the prefactor in (1.11b) is at most one:

\[
 \frac{\min(k_r^\epsilon,k_{r+h}^\delta)}
 {\sqrt{k_r^\epsilon k_{r+h}^\delta}}\le1.
 \tag{1.11c}
\]

More explicitly, if (R_r=\binom nr) and

\[
 P_{a,b}=\binom ra\binom{n-r}b,
 \tag{1.11d}
\]

then coordinate transitivity gives the exact shell identity

\[
 P_{a,b}\bigl(K^{\epsilon\delta}(S,T)\bigr)^2
 =
 \frac{(J_{a,b}^{\epsilon\delta})^2}
 {k_r^\epsilon k_{r+h}^\delta P_{a,b}}
 \frac{R_{r+h}}{R_r}.
 \tag{1.11e}
\]

The rank-orbit ratio (R_{r+h}/R_r=m^{o(1)}) uniformly in the protected
band.  Combining (1.11b)--(1.11e), every mixed exposed/claimed block
obeys

\[
 \|K^{\epsilon\delta}_0(x,\cdot)\|_2^2
 =m^{-2+o(1)},
 \tag{1.11f}
\]

and

\[
 \sum_h\|K_h^{\epsilon\delta}(x,\cdot)\|_2
 =m^{-1/2+o(1)}.
 \tag{1.11g}
\]

This is the form used in the exact priority influence bound (6.3c).

### Lemma 1.2 (the tag block is negligible)

Let (U) be a labelled chunk tag.  Inside (U), coordinate symmetry gives,
for a rank-(r) target (S\subseteq U),

\[
 \frac{d(U,S)}{d(U)}=\frac{k_r}{\binom Mr},
 \tag{1.12}
\]

where (k_r\le g) is the number of claimed rank-(r) flags in one chunk.
Here the tag fixes the carrier copy and chunk position, while the phase
labelling remains uniform.  Both the tag orbit and each target orbit are
transitive under the ambient coordinate action.
Consequently

\[
 \sum_{S:|S|=r}K(U,S)^2
 \le (1+o(1))\frac{k_r^2}{\binom Mr}.
 \tag{1.13}
\]

All protected ranks are central inside the (M=m+H) carrier, so (1.13)
is exponentially small, uniformly after summing over the (2Q+1) rank
strata.  By transitivity/Frobenius double counting, the reverse
target-to-tag squared row has the same bound multiplied by the tag/target
orbit-size ratio, which is at most one in the calibrated catalogue, and
is also exponentially small.  Thus
adjoining the tag stratum does not change (1.11).

## 2. Rank-block operator norms

Let (V_i) be one protected rank stratum, with the tag stratum also
allowed and assigned (k_{\rm tag}=1).  Every catalogue chunk contains
exactly (k_i\le g) vertices of (V_i).  Let (D_i) be the common
degree in that stratum.  The block

\[
 K_{ij}:\ell_2(V_j)\longrightarrow\ell_2(V_i)
 \tag{2.1}
\]

has nonnegative entries.  For (x\in V_i),

\[
 \sum_{y\in V_j}K(x,y)
 =k_j\sqrt{D_i/D_j},
 \tag{2.2}
\]

while the reverse row sum is

\[
 \sum_{x\in V_i}K(x,y)
 =k_i\sqrt{D_j/D_i}.
 \tag{2.3}
\]

Schur's test gives the exact cancellation of the degree ratio:

\[
 \boxed{\|K_{ij}\|_{2\to2}\le\sqrt{k_ik_j}\le g.}
 \tag{2.4}
\]

For (i=j), removing the identity diagonal changes this bound by at most
one.

The same statement holds in a residual catalogue whenever degrees inside
each stratum differ from a reference (D_i(t)) by a factor (1+\epsilon):

\[
 \|K_{ij}^{(t)}\|_{2\to2}
 \le (1+O(\epsilon))\sqrt{k_ik_j}.
 \tag{2.5}
\]

This uses only the exact number of vertices of each stratum in one chunk;
it does not use randomness.

## 3. The raw bow-tie theorem

Fix (x\in V_{i_0}), and write

\[
 a_i(y)=K(x,y)\mathbf1_{y\in V_i,\,y\ne x}.
 \tag{3.1}
\]

Let (K^\circ) be (K) with its within-stratum identity diagonal removed.
The off-diagonal triangle, or bow-tie, energy is

\[
 \mathfrak B(x)=
 \sum_{\substack{y,z\ne x\\y\ne z}}
 K(x,y)K(y,z)K(z,x)
 =\sum_{i,j}\langle a_i,K^\circ_{ij}a_j\rangle.
 \tag{3.2}
\]

Let (\mathcal C(x)) be the Boolean covers and cocovers of (x) in the two
adjacent protected ranks.  Split

\[
 a=a_{\mathcal C}+b.
 \tag{3.3}
\]

The leading (a=0,|h|=1) term in Lemma 1.1 is exactly
(a_{\mathcal C}).  Removing it from the adjacent-rank shells and using
the next term of (1.9) gives

\[
 \|a_{\mathcal C}\|_2=O_D(m^{-1/2}),
 \qquad
 \sum_i\|b_i\|_2=O_D(m^{-1}).
 \tag{3.4}
\]

Two distinct members of (\mathcal C(x)) are either same-rank Johnson
neighbours or form a nested rank-gap-two pair.  Equation (1.3) gives,
uniformly for such a pair,

\[
 K(y,z)=O_D(m^{-2}).
 \tag{3.5}
\]

Moreover (|\mathcal C(x)|=O(m)), so Cauchy--Schwarz and (3.4) give

\[
 \sum_{y\in\mathcal C(x)}K(x,y)=O_D(1).
 \tag{3.6}
\]

The cover--cover part of (3.2) is therefore (O_D(m^{-2})).  For the two
cross terms and the remainder--remainder term, use (2.4) and (3.4):

\[
\begin{aligned}
 \mathfrak B(x)
 &\le
 O_D(m^{-2})
 +2g\|a_{\mathcal C}\|_2\sum_i\|b_i\|_2
 +g\left(\sum_i\|b_i\|_2\right)^2\\
 &=O_D\left(m^{-2}+g m^{-3/2}+g m^{-2}\right).
\end{aligned}
 \tag{3.7}
\]

If the full common-killer triangle is allowed to use (y=z), its diagonal
contribution is

\[
 \sum_{y\ne x}K(x,y)^2=O_D(m^{-1}).
 \tag{3.8}
\]

We have proved:

### Theorem 3.1 (raw triangle bound)

For every protected target (x) in the symmetrized fixed-(D)
catalogue,

\[
 \boxed{
 \mathfrak T(x):=
 \sum_{y,z\ne x}K(x,y)K(y,z)K(z,x)
 =O_D\left(m^{-1}+g m^{-3/2}\right).}
 \tag{3.9}
\]

The same proof with the mixed vectors (1.11f)--(1.11g) gives the raw
exposure--claim--claim common-link bound

\[
 \boxed{
 \mathfrak T^{\rm mixed}(x)
 \le m^{o(1)}\left(m^{-1}+g m^{-3/2}\right)
 =m^{-1+o(1)}.}
 \tag{3.10}
\]

The estimate is independent of the number (2Q+1) of protected ranks.
This is the point of retaining the factorial rank-gap profile before
applying Schur: replacing (1.11) by a uniform row bound would incorrectly
lose a factor (Q).

## 4. Exact covariance identity for one bite

The following calculation explains why (3.5) is the correct quantity.
For clarity, first take a (k)-uniform (D)-regular residual
hypergraph.  Fix a vertex (x).  A bite marks every edge independently
with probability

\[
 p=\frac{h}{kD}.
 \tag{4.1}
\]

Condition on (x) itself not being covered.  Let (Z_x) be the number of
edges through (x) which survive the bite.  For an edge (G\not\ni x),
put

\[
 A_G(x)=\#\{E\ni x:(E\setminus\{x\})\cap G\ne\varnothing\}.
 \tag{4.2}
\]

The shared-killer identity is

\[
 \sum_{E,F\ni x}
 \#\{G:G\cap(E\setminus x)\ne\varnothing,
       G\cap(F\setminus x)\ne\varnothing\}
 =\sum_{G\not\ni x}A_G(x)^2.
 \tag{4.3}
\]

Moreover,

\[
 A_G(x)\le\sum_{y\in G}d(x,y).
 \tag{4.4}
\]

Expanding the square and using

\[
 \sum_{G\supseteq\{y,z\}}1=d(y,z)
 \tag{4.5}
\]

gives

\[
 \sum_GA_G(x)^2
 \le
 \sum_{y,z}d(x,y)d(y,z)d(z,x)
 =D^3\mathfrak T(x).
 \tag{4.6}
\]

Since (p) times the number of shared killers controls the covariance of
two survival indicators (the factor is bounded because
(p|\Gamma(E)\cap\Gamma(F)|\le pkD=h=O(1))),

\[
 \boxed{
 \frac{\operatorname{Var}Z_x}{D^2}
 \le O(D^{-1})+O\left(\frac hk\mathfrak T(x)\right).}
 \tag{4.7}
\]

There are (O((k/h)\log\log m)) effective bites before density
(1/\log m).  Thus the total covariance budget is

\[
 O(\mathfrak T(x)\log\log m).
 \tag{4.8}
\]

By Theorem 3.1, the raw contribution is

\[
 O_D\left(\left(\frac1m+\frac g{m^{3/2}}\right)
 \log\log m\right)=o(1).
 \tag{4.9}
\]

For the actual tag-activated priority nibble, target coincidences do not
act as hard binary conflicts: they change the factorial priority weight.
Its exact analogue is therefore (6.3), not a literal substitution
(pD=\alpha) into (4.7).

## 5. Hereditary pair-square condition

Let (z\ge1/\log m) be the current unused-resource density.  Suppose the
following two residual properties hold.

1. Every protected fibre degree is within (1+o(1)) of its stratum
   reference degree.
2. The blockwise pair-square profile obeys the ideal inflation bound

\[
 \sum_{y\in V_{r+h}}K_z(x,y)^2
 \le C z^{-2}
 \begin{cases}
  m^{-2},&h=0,\[1mm]
  (|h|+1)^2|h|!(C/m)^{|h|},&h\ne0.
 \end{cases}
 \tag{5.1}
\]

Let (\mathcal C(x)) again be the covers/cocovers of (x).  Under (5.1),

\[
 \|a_{\mathcal C}\|_2=O((z\sqrt m)^{-1}),
 \qquad
 \sum_i\|b_i\|_2=O((zm)^{-1}).
 \tag{5.2}
\]

To handle the cover--cover block without a pointwise residual codegree
bound, use (5.1) for every anchor (y\in\mathcal C(x)).  The relevant
(z)'s are either in the same rank as (y), off the diagonal, or at rank
gap two.  Hence

\[
 \|K_z[\mathcal C(x),\mathcal C(x)]\|_{\rm F}^2
 \le C\frac{|\mathcal C(x)|}{z^2m^2}
 \le\frac C{z^2m}.
 \tag{5.3}
\]

Its operator norm is therefore at most (C/(z\sqrt m)).  Repeating the
cover/remainder proof of Theorem 3.1 gives

\[
 \boxed{
 \mathfrak T_z(x)
 \le C\left[
 {1\over z^2m}
 +{g\over z^2m^{3/2}}
 +{1\over z^3m^{3/2}}
 \right].}
 \tag{5.4}
\]

At (z=1/\log m),

\[
 \mathfrak T_z(x)\log\log m
 =m^{-1+o(1)}.
 \tag{5.5}
\]

More importantly for the weighted fibre ledger,

\[
 \boxed{
 Q\sup_{z\ge1/\log m}\sup_x
 \mathfrak T_z(x)\log\log m=o(1).}
 \tag{5.6}
\]

Indeed (Q=m^{1/2+o(1)}) and (g=m^{1/2+o(1)}), while every explicit
logarithmic factor in (5.4) is (m^{o(1)}).

Therefore the complete binary one-vertex degree martingale closes under
(5.1).  The same conclusion holds for the priority process if (5.1) is
replaced by its hazard-weighted form (6.3).  The surviving hereditary
assertion is exactly this weighted pair-square statement, or a weighted
average version sufficient after declaring (o(W)) exceptional fibres.

This is strictly weaker than controlling all multiple codegrees.  It is a
pair-square statement, and its one-step variance is a weighted four-walk
kernel.

## 6. Weighted bow-tie identity in the actual priority catalogue

At time (t), let

\[
 p_{t,F}(P)=\frac{a_t(P)}{D_t(F)}
 \tag{6.1}
\]

be the current distribution of candidate base grids (P) in fibre (F).
Let (h_t(P,E)\in[0,1]) be the exact fraction of feasible priorities of
(P) killed by tentative chunk (E); owner overlap is represented by
(h_t(P,E)=1).  Define

\[
 K_t(P,P')=
 \sum_U\mathbb E_{E\sim\nu_{t,U}}
 [h_t(P,E)h_t(P',E)].
 \tag{6.2}
\]

The squared influence of one bite on (F) is exactly

\[
\begin{aligned}
 J_t(F)
 &:={}
 \sum_U\mathbb E_{E\sim\nu_{t,U}}
 \left(\sum_{P\in F}p_{t,F}(P)h_t(P,E)\right)^2\\
 &=
 \sum_{P,P'\in F}p_{t,F}(P)p_{t,F}(P')K_t(P,P').
\end{aligned}
 \tag{6.3}
\]

There is also a direct resource-kernel majorant.  Let

\[
 \pi_{t,F}(x)=\Pr_{P\sim p_{t,F}}(x\in P),
 \qquad
 \pi_{t,U}(x,y)=\Pr_{E\sim\nu_{t,U}}(x,y\in E).
 \tag{6.3a}
\]

Losing a fraction of priorities requires at least one newly conflicting
resource, so

\[
 h_t(P,E)\le\mathbf1_{\{P\cap E\ne\varnothing\}}
 \le\sum_{x\in P\cap E}1.
 \tag{6.3b}
\]

Expanding the square and averaging therefore gives the exact upper bound

\[
 \boxed{
 J_t(F)
 \le
 \sum_{x,y}
 \pi_{t,F}(x)\pi_{t,F}(y)
 \sum_U\pi_{t,U}(x,y).}
 \tag{6.3c}
\]

At uniform time zero, (6.3c) is precisely the symmetrically normalized
triangle/common-link form bounded in Theorem 3.1, up to the harmless
stratum degree ratios.  At later times it is the weighted residual
pair-square object.

Thus the variance term in the exact Efron--Stein transfer energy is at
most

\[
 C\alpha\sum_F\operatorname{wt}(F)J_t(F).
 \tag{6.4}
\]

Equation (6.3) is the weighted residual version of (4.6).  In a regular
binary hypergraph it is precisely a normalized common-link four-walk;
after anchoring one vertex it reduces to the triangle kernel of
Theorem 3.1.

The raw Theorem 3.1 does not prove (6.4) at later times: the weights
(a_t(P)) may concentrate on a rare correlated subcatalogue.  Conversely,
a maximum point-mass hypothesis is stronger than necessary.  The exact
within-bite bad-pair term is only the weighted bad-edge mass

\[
 \mathscr B_t=
 \sum_{U,V}
 \mathbb E_{P\sim\nu_{t,U},\,E\sim\nu_{t,V}}
 \mathbf1_{\{P\sim_B E\}}.
 \tag{6.5}
\]

A sequential ordering of the activated tags, with immediate quarantine
after each accepted chunk, removes simultaneous bad pairs entirely; in a
parallel bite (6.5), rather than
(\max_{U,P}A\nu_{t,U}(P)), is the quantity which pays for the alteration.

The exact remaining propagation gate in this language is therefore

\[
 \boxed{
 \sum_{t<R}
 \left[
  g\alpha^2\mathscr B_t+
  \alpha\sum_F\operatorname{wt}(F)J_t(F)
 \right]=o(W),}
 \tag{6.6}
\]

together with the already stated mean-drift tolerance.  Condition (5.1)
is a clean sufficient route to the (J_t) part.

### Proposition 6.1 (sequential quarantine removes the point-mass gate)

There is an equivalent sequential formulation which has no simultaneous
bad-pair alteration.  Process the activated tags in a random order.  On
reaching tag (U), sample one candidate (E) from its **current**
distribution, and immediately quarantine every bad neighbour of (E)
before processing the next tag.

For a fibre (F), let

\[
 I_{s,F}(E)=\frac{D_s(F)-D_{s+1}(F)}{D_s(F)}
 \tag{6.7}
\]

be its exact fractional loss at sequential step (s), including owner
deletion, target deletion, the factorial priority update, and dynamic
quarantine.  Put

\[
 \bar I_{s,F}=\mathbb E[I_{s,F}(E_s)\mid\mathcal F_s].
 \tag{6.8}
\]

Then

\[
 M_{t,F}=\sum_{s<t}(I_{s,F}(E_s)-\bar I_{s,F})
 \tag{6.9}
\]

is a martingale and

\[
 \mathbb E M_{t,F}^2
 =\mathbb E\sum_{s<t}
 \operatorname{Var}(I_{s,F}(E_s)\mid\mathcal F_s)
 \le
 \mathbb E\sum_{s<t}\mathbb E[I_{s,F}(E_s)^2\mid\mathcal F_s].
 \tag{6.10}
\]

Consequently, for every tolerance (\eta>0), the expected total weight of
fibres with (|M_{t,F}|>\eta) is at most

\[
 \boxed{
 \frac1{\eta^2}
 \sum_F\operatorname{wt}(F)
 \mathbb E\sum_{s<t}I_{s,F}(E_s)^2.}
 \tag{6.11}
\]

#### Proof

The martingale assertion follows from (6.8).  Orthogonality of martingale
increments gives the equality in (6.10), and conditional variance is at
most the conditional second moment.  Apply Chebyshev to each fibre,
multiply by its accounting weight, and sum.  \(\square\)

The summand in (6.11) is again a weighted common-link square: expanding
the exact loss of (F) against the sampled (E_s) gives (6.3).  Sequential
quarantine therefore removes the need for either the maximum point mass
(\kappa_t) or the parallel bad-edge term (\mathscr B_t).  It does **not**
remove the weighted bow-tie gate; it states that gate in its minimal form.

The corresponding sequential sufficient condition is

\[
 \boxed{
 \sum_F\operatorname{wt}(F)
 \mathbb E\sum_s I_{s,F}(E_s)^2=o(W\eta^2),}
 \tag{6.12}
\]

plus an (o(1))-accurate common mean drift within every stratum.  This is
the direct martingale version of the transfer-energy condition.

## 7. Audit under four-antichain quarantine

Let (B_4) join two base grids when their full intersection contains a
four-element antichain.  The membership-atom calculation gives

\[
 \frac{\Delta(B_4)}A
 \le
 m^{1+o(1)}\left(\frac{C}{m}\right)^6
 =m^{-5+o(1)}.
 \tag{7.1}
\]

### 7.1 Fixed pruning still fails

Balanced one-shot thinning at density
(p\asymp[L(\Delta(B_4)+1)]^{-1}) leaves typical base-grid degree at
most

\[
 \mu_4=m^{5-o(1)}.
 \tag{7.2}
\]

A chunk uses (g=m^{1/2+o(1)}) owners.  At residual owner density
(z=1/\log m),

\[
 \mu_4 z^g
 =m^{5-o(1)}(\log m)^{-m^{1/2+o(1)}}=o(1).
 \tag{7.3}
\]

Thus (s=4) does not rescue fixed-before-the-nibble pruning.

### 7.2 Dynamic quarantine has negligible raw cost

For a selected family of at most (W/g) chunks, the deterministic
quarantine ledger with tolerance (\eta=m^{-1}) loses tag-fibre weight at
most

\[
 Wm^{-4+o(1)}=o(W).
 \tag{7.4}
\]

If every grid lies in (K\le g(2Q+1)=m^{1+o(1)}) protected target
fibres, the lost target-fibre weight is at most

\[
 \frac{WK}{g}m^{-4+o(1)}=o(W).
 \tag{7.5}
\]

Unlike (7.2), this retains the original exponential base-grid entropy.

### 7.3 Width-three raw census

After (B_4)-quarantine, the intersection of a candidate grid with every
previously selected grid has width at most three.  If its coordinate span
is (t), Dilworth gives size at most (3(t+1)).  Covering it by three
chains and encoding their steps gives at most

\[
 m^{o(1)}C^t
 \tag{7.6}
\]

possible shapes for fixed endpoints.  The relative coordinate-labelling
cost is at most

\[
 m^{o(1)}\frac{t+1}{\binom{m-g}{t}}.
 \tag{7.7}
\]

Weighting an intersection by (w^{|\mathcal L|}), the ratio of successive
span terms is

\[
 O\left(\frac gm(Cw)^3\right).
 \tag{7.8}
\]

For (w\le C\log m) and (g=m^{1/2+o(1)}), (7.8) is (o(1)).  Hence
the width-three exponential census is summable at time zero.  The same
count can be applied separately to the two links in (6.3).  Dropping the
compatibility constraint between the two link shapes only enlarges the
sum, and the successive-span ratio is then at worst

\[
 O\left(\frac gm(Cw)^6\right)=o(1).
 \tag{7.9}
\]

Thus the raw, unweighted four-walk expansion is also summable.

What it does not control is the later tilted measure
(p_{t,F}(P)p_{t,F}(P')\nu_{t,U}(E)).  This is exactly the hereditary
weighted gate (6.6).

## 8. Exact frontier

The following statements are now proved.

1. Raw normalized pair squares decay factorially with rank gap,
   (1.6)--(1.7).
2. The sum of their block (\ell_2)-norms is (O(m^{-1/2})), with no
   factor (Q).
3. The raw common-killer triangle is
   (O(m^{-1}+gm^{-3/2})=m^{-1+o(1)}).
4. This triangle is exactly the covariance kernel for one-vertex degree
   propagation.
5. Ideal (z^{-2}) inflation through (z=1/\log m) still gives a
   summable covariance budget.
6. Under (s=4), fixed pruning remains impossible, whereas dynamic
   quarantine has (m^{-5+o(1)}) bad density and a valid raw width-three
   exponential census.

The remaining theorem is no longer an unspecified higher-codegree
hierarchy.  It is one of the following equivalent-strength routes:

* propagate the residual pair-square profile (5.1) in weighted average;
* prove the weighted common-link estimate (6.6);
* construct an aligned sequential column nibble for which (6.3) is
  dominated by its raw (z^{-2})-tilt.

No one of these hereditary weighted assertions is proved here.
