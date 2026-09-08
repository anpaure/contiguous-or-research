# ST_A for simple fixed-core sectors: exact capacity defects and the residual fractional tail gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Verdict

Put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil,
\]

where (A>0) is fixed.  Let \(\tau=\phi^2\) be the normalized
step-two PBBS permutation on the (B_m) Dyck roots.  We consider
pairwise quotient-edge-disjoint families of simple fixed-core return
sectors with step-two residence (s+1\le H), on quotient cycles longer
than (H+1).

The full estimate

\[
 |\mathcal P|=o_A(B_m/\sqrt m)                    \tag{ST_A}
\]

is **not** proved here.  What is proved is the following sharp
quarantine theorem and an exact fractional completion inequality for the
quarantined class.

For a height (h), let (b_{m,h}) be the number of height-(h) Dyck
roots and put

\[
 \alpha_h(\mathcal P)
  ={(h+2)|\mathcal P_h|\over b_{m,h}},            \tag{0.1}
\]

with value zero if (b_{m,h}=0).  Thus (0\le\alpha_h\le1) is the
fraction of the exact reciprocal-height edge capacity used in stratum
(h).  Transport the canonical first-deepest frame along a return and
write (R(I)) for the number of genuine frame changes among its
(s(I)-1) internal step-two transitions.

For (0<a<A), (0<\delta<1), and (0<\varepsilon<1/16), define the
critical class

\[
 \begin{split}
 \mathfrak N(a,\delta,\varepsilon)
 =\{I\in\mathcal P:;&a\sqrt m\le h(I)\le H-1,\\
 &\alpha_{h(I)}(\mathcal P)>\delta,
 \quad R(I)>\varepsilon s(I)\}.
 \end{split}                                      \tag{0.2}
\]

There are a function \(\eta(a)\downarrow0\) and constants
(C_{a,A}<\infty) such that

\[
 \boxed{
 \limsup_{m\to\infty}{\sqrt m\over B_m}
 |\mathcal P\setminus\mathfrak N(a,\delta,\varepsilon)|
 \le
 \eta(a)+{\delta\over a}
 +C_{a,A}2^{-\lfloor1/(8\varepsilon)\rfloor}.}
 \tag{0.3}
\]

Consequently, after first fixing (a), then sending
(\delta,\varepsilon\downarrow0), and finally sending (a\downarrow0),
the complement of \(\mathfrak N\) is (o_A(B_m/\sqrt m)).  In
particular, reciprocal-height saturation is impossible outside a class
which simultaneously has Gaussian height, positive stratum utilization,
and a positive density of genuine canonical reframings.

Equivalently, a diagonal choice gives deterministic sequences
\(a_m,\delta_m,\varepsilon_m\downarrow0\), independent of the packing,
for which

\[
 |\mathcal P\setminus
   \mathfrak N(a_m,\delta_m,\varepsilon_m)|
 =o_A(B_m/\sqrt m).                              \tag{0.3a}
\]

Now lift every quotient sector in \(\mathfrak N\) through all (N)
cyclic label phases and denote the resulting physical family by
\(\mathfrak N^\uparrow\).  For a physical middle set (T), let
\(L^{\rm bulk}_{\mathfrak N,J}(T)\) be the exact ambient-completion
tail load from the kernel of
`PBBS_SIMPLE_SECTOR_AMBIENT_COMPLETION_KERNEL_20260725.md`, retaining only

\[
 \min\{j,q-j\}>J                              \tag{0.4a}
\]

in the odd tail and

\[
 \min\{j,q-1-j\}>J                            \tag{0.4b}
\]

in the even tail.  Here (q=m-s).  Then the following finite-rank
inequality is exact apart from the displayed, already audited endpoint
estimate:

\[
 \boxed{
 |\mathcal P|
 \le |\mathcal P\setminus\mathfrak N|
 +{B_m\over N-2H}
 \left(
   \sup_T L^{\rm bulk}_{\mathfrak N,J}(T)+E_{A,J}(m)
 \right),}                                      \tag{0.5}
\]

where, for (J=\lfloor\gamma\sqrt m\rfloor),

\[
 E_{A,J}(m)
 \le C_A\gamma
       e^{C_A(\gamma+\gamma^2)}\sqrt m+o_A(\sqrt m).
                                                        \tag{0.6}
\]

Thus the exact remaining (ST_A)-scale statement is only

\[
 \lim_{\gamma\downarrow0}\limsup_{m\to\infty}
 {1\over\sqrt m}\sup_T
 L^{\rm bulk}_{\mathfrak N,J}(T)=0,             \tag{0.7}
\]

after the quarantine parameters are sent to zero in the order above.
No (O_A(1)) bound is requested.  Hence (0.5) is an (ST_A) gate, not
the stronger (CP_A) gate.

The equality and near-equality cases of the reciprocal-height and
fixed-core enclosure ledgers are also completely classified below.
Exact reciprocal-height equality means an edge tiling by minimal
height-gap returns (s=h), a class which includes the genuine
zero-winding critical corners.  Near equality forces almost all quotient
edges to be covered, total winding excess (o(b_{m,h})), and, in the
full physical lift, utilization (1-o(1)) on almost every enclosing
inactive-core residence gap on both translated parities.  Therefore a
putative family which also approaches the full reciprocal-height constant
is not an arbitrary fixed-core path packing: its edge and core ledgers are
double-gap near-tilings.  A merely positive \(ST_A\)-scale counterfamily
need only have the weaker positive-utilization condition in (0.2).

## 1. Simple sectors and the exact completion kernel

A simple return of gap (2s+1) has half-open omitted-label word

\[
 a_0,b_0,a_1,b_1,\ldots,a_{s-1},b_{s-1},a_s.
                                                        \tag{1.1}
\]

Put

\[
 U=\{b_0,\ldots,b_{s-1}\},\qquad
 A=\{a_0,\ldots,a_s\},\qquad q=m-s.              \tag{1.2}
\]

There are disjoint inactive cores (K,K'), each of size (q), for
which the two owner arms are

\[
 X_{2t}=K\cup\{a_0,\ldots,a_{t-1}\}
                 \cup\{b_t,\ldots,b_{s-1}\},    \tag{1.3}
\]

\[
 X_{2t+1}=K'\cup\{b_0,\ldots,b_{t-1}\}
                 \cup\{a_{t+1},\ldots,a_s\}.    \tag{1.4}
\]

Independently order (K) and (K') uniformly and complete the open
sector to an ambient wreath.  After deleting its (2s+2) fixed open
middle vertices, the probability that a middle set (T) occurs in the
random tails is

\[
 \begin{aligned}
 \pi_I(T)={}&
 \mathbf1_{\{T\cap(A\cup U)=U\}}
 \mathbf1_{\{1\le j\le q-1\}}
 {1\over\binom qj^2}\\
 &+\mathbf1_{\{T\cap(A\cup U)=A\}}
 {1\over\binom qj\binom q{j+1}},
 \end{aligned}                                   \tag{1.5}
\]

where (j=|T\cap K|) in the first line and (j=|T\cap K'|) in the
second.  In particular,

\[
 \boxed{\sum_{T\in\binom{[N]}m}\pi_I(T)=N-(2s+2).}
                                                        \tag{1.6}
\]

The two indicator conditions in (1.5) have an exact chronology meaning.
The first is equivalent to the membership word

\[
 0,1,0,1,\ldots,1,0,                              \tag{1.7}
\]

on the labels in (1.1); the second is equivalent to its reverse.  Thus
every nonzero bulk term in (0.5) is a genuine strictly alternating PBBS
sector, not merely an abstract pair of monotone Johnson paths.

## 2. Exact reciprocal-height defect identity

The permutation \(\tau\) preserves Dyck height.  Regard each height-(h)
root as the directed quotient edge leaving that root, so the height
stratum has exactly (b_{m,h}) quotient edges.  For a return sector (I),
write

\[
 \ell(I)=s(I)+2                                      \tag{2.1}
\]

for the number of quotient edges in its projected trace.  The exact
height-gap theorem says

\[
 s(I)\ge h(I),\qquad \ell(I)\ge h(I)+2.           \tag{2.2}
\]

Fix (h), and define the number of uncovered stratum edges by

\[
 u_h=b_{m,h}-\sum_{I\in\mathcal P_h}\ell(I)\ge0. \tag{2.3}
\]

### Proposition 2.1 (exact edge defect)

For every quotient-edge-disjoint family,

\[
 \boxed{
 b_{m,h}-(h+2)|\mathcal P_h|
 =u_h+\sum_{I\in\mathcal P_h}(s(I)-h).}
                                                        \tag{2.4}
\]

#### Proof

Use (2.1) in (2.3):

\[
 \begin{aligned}
 b_{m,h}-(h+2)|\mathcal P_h|
 &=u_h+\sum_I\bigl((s(I)+2)-(h+2)\bigr)\\
 &=u_h+\sum_I(s(I)-h).
 \end{aligned}
\]

Every term is nonnegative by edge-disjointness and (2.2).  \(\square\)

This proves (0\le\alpha_h\le1) and gives the exact equality
classification:

\[
 \alpha_h=1
 \quad\Longleftrightarrow\quad
 u_h=0\ \hbox{ and }\ s(I)=h\ \hbox{ for every }I\in\mathcal P_h.
                                                        \tag{2.5}
\]

Thus equality is a partition of every height-(h) quotient edge into
minimal (h+2)-edge sectors.  The condition (s=h) is exactly equality
in the PBBS height-gap theorem.  It includes the genuine zero-winding
critical-corner case; no converse from height equality to zero winding is
used here.

The stability statement is equally exact.  If
(\alpha_h\ge1-\zeta), then

\[
 u_h+\sum_I(s(I)-h)\le\zeta b_{m,h}.             \tag{2.6}
\]

Consequently (u_h/b_{m,h}\le\zeta), and for every (t\ge1),

\[
 \#\{I\in\mathcal P_h:s(I)-h\ge t\}
 \le{\zeta b_{m,h}\over t}.                     \tag{2.7}
\]

Relative to the selected sectors, (2.7) is

\[
 {\#\{I:s(I)-h\ge t\}\over|\mathcal P_h|}
 \le {\zeta(h+2)\over(1-\zeta)t}.               \tag{2.8}
\]

In particular, if \(\zeta=o(1)\), then all but (o(1)) of the sectors
have winding excess (o(h)), after the usual two-parameter choice of the
threshold in (2.8).

## 3. Fixed-core enclosure defects on both parities

The fixed-core normal form gives more rigidity than (2.4).  Lift the
height-(h) quotient stratum through every spatial phase; its physical
edge volume is (Nb_{m,h}).  For a physical coordinate (z), its
positive residence gaps partition the corresponding owner edges.  The
sum of their lengths over all coordinates is

\[
 (m+1)Nb_{m,h}.                                   \tag{3.1}
\]

Indeed each Johnson edge is counted by the (m-1) common coordinates
and by its departing and arriving boundary coordinates, for a total of
(m+1).

Every (z\in K_I) has one positive residence gap (J) containing the
whole trace of (I).  The corresponding statement for (z\in K'_I)
holds on the translated parity.  For the (K)-parity define

\[
 \rho_J={1\over|J|}
 \sum_{\substack{\widetilde I\subseteq J\\z\in K_{\widetilde I}}}
 \ell(\widetilde I)\le1,                        \tag{3.2}
\]

where \(\widetilde I\) runs over the full physical lift.  Pairwise
quotient-edge-disjointness makes the physical traces in one gap
edge-disjoint.

### Proposition 3.1 (exact enclosure defect)

Let

\[
 \Delta_h^K=\sum_{z,J}|J|(1-\rho_J).             \tag{3.3}
\]

Then

\[
 \boxed{
 \Delta_h^K
 =(m+1)Nb_{m,h}
   -N\sum_{I\in\mathcal P_h}(m-s(I))(s(I)+2).}
                                                        \tag{3.4}
\]

The translated (K')-parity has the same formula and hence the same
total defect, although its individual residence gaps are different.

#### Proof

Sum (3.2) first over all positive gaps of one coordinate and then over
all coordinates.  A lifted sector is counted once for every inactive
core label, namely (q_I=m-s(I)) times.  Thus the utilized length is

\[
 \sum_{\widetilde I}q_I\ell(\widetilde I)
 =N\sum_I(m-s(I))(s(I)+2).
\]

Subtract this from (3.1).  The (K') proof is the translated copy.
\(\square\)

Exact equality \(\Delta_h^K=0\) holds if and only if every positive
residence gap is tiled edge-for-edge by the selected sector traces
assigned to it.  The same statement holds independently on the
translated parity.

Near reciprocal-height equality forces near enclosure equality at the
scale relevant here.  If (s+1\le H) and
\(\alpha_h\ge1-\zeta), then (2.6) gives

\[
 \sum_I\ell(I)=b_{m,h}-u_h\ge(1-\zeta)b_{m,h}.
\]

The residence convention gives \(m-s(I)\ge m-H+1\), so (3.4) implies

\[
 {\Delta_h^K\over(m+1)Nb_{m,h}}
 \le \zeta+{H\over m+1}.                        \tag{3.5}
\]

Therefore, with residence-length probability measure

\[
 \mu_h(\mathcal J)
 ={1\over(m+1)Nb_{m,h}}\sum_{J\in\mathcal J}|J|,
\]

Markov's inequality gives, for every (0<\gamma<1),

\[
 \boxed{
 \mu_h\{J:\rho_J\le1-\gamma\}
 \le {\zeta+H/(m+1)\over\gamma}.}               \tag{3.6}
\]

The identical estimate holds on the (K')-parity.  This is the promised
quantitative near-equality classification: an asymptotically full
reciprocal-height stratum almost tiles almost every enclosing core gap on
both translated parities.

For completeness, the exact defect in the enclosure-derived bound can
also be written without an inequality.  With
\(d=(m-H+1)(h+2)\),

\[
 \begin{aligned}
 &(m+1)Nb_{m,h}-Nd|\mathcal P_h|\\
 &\quad=\Delta_h^K
 +N\sum_{I\in\mathcal P_h}
 \bigl((H-1-s(I))(s(I)+2)+(m-H+1)(s(I)-h)\bigr).
                                                        \tag{3.7}
 \end{aligned}
\]

Thus equality in that particular relaxed bound requires simultaneously
gap tiling, (s(I)=H-1), and (s(I)=h) for every selected sector.  This
explains why the relaxed enclosure bound has asymptotic constant one but
usually no literal finite-rank equality away from the top height.

## 4. Chronology contraction and the fast-reframing residual

Let a return have successive step-two roots

\[
 D_0,D_1,\ldots,D_{s-1}.                         \tag{4.1}
\]

Transport the canonical first-deepest spine through each transition.  A
transition is a frame change if the transported spine is not the
canonical first-deepest spine at the next root.  Let (R(I)) count these
changes.

For an integer (t\ge1), call a root (t)-stable if this same displayed
spine remains canonical for the next (t) transitions.  There are
(s-t) possible internal (t)-windows in (4.1), and one frame change
can invalidate at most (t) of them.  Hence (I) contains at least

\[
 w_t(I)=\max\{s(I)-t-tR(I),0\}                  \tag{4.2}
\]

(t)-stable starts.

Let (c_{m,h}^{(t)}) be the number of height-(h), semilength-(m),
(t)-stable roots.  Charging a stable start to the directed quotient
edge leaving that root gives the exact packing inequality

\[
 \boxed{
 \sum_{I\in\mathcal P_h}w_t(I)\le c_{m,h}^{(t)}.}
                                                        \tag{4.3}
\]

This remains true for intervals crossing an arbitrary written cut of a
long quotient cycle: the charged edges are internal to the cyclic
interval, and quotient-edge-disjointness makes all charges distinct.

The stable-root atlas is explicit.  Define

\[
 F_0(z)=F_1(z)=1,\qquad F_{j+1}(z)=F_j(z)-zF_{j-1}(z).
                                                        \tag{4.4}
\]

If (t=2v), then

\[
 \sum_{m\ge h}c_{m,h}^{(2v)}z^m
 ={z^h\over F_{h-v}(z)F_{h-v+1}(z)},            \tag{4.5}
\]

while if (t=2v+1), then

\[
 \sum_{m\ge h}c_{m,h}^{(2v+1)}z^m
 ={z^h\over F_{h-v}(z)^2}.                      \tag{4.6}
\]

These formulas follow by decomposing a Dyck path around its first deepest
spine.  A pre-spine forest originally at depth (k) has cap

\[
 \max\{h-k-t-1,0\},                              \tag{4.7}
\]

and a post-spine forest has cap

\[
 h-\max\{k,t-k\}.                                \tag{4.8}
\]

The finite-height forest products telescope to (4.5)--(4.6).  At
(z=1/4), their ratio to the unrestricted height-(h) kernel contains
the exact displacement factor (2^{-t}).  Standard positive-coefficient
convolution of the two finite-strip kernels gives, uniformly for

\[
 a\sqrt m\le h\le A\sqrt m,qquad t\le h/2,
\]

\[
 c_{m,h}^{(t)}\le C_{a,A}4^m2^{-t}h^{-4}.       \tag{4.9}
\]

Since

\[
 \sum_{h\ge a\sqrt m}h^{-4}=O_a(m^{-3/2}),
 \qquad B_m\asymp4^m m^{-3/2},                  \tag{4.10}
\]

we obtain

\[
 \sum_{a\sqrt m\le h\le A\sqrt m}
 c_{m,h}^{(t)}\le C_{a,A}2^{-t}B_m.             \tag{4.11}
\]

If (t\le s/4) and (R(I)\le s/(4t)), then (4.2) gives
(w_t(I)\ge s/2\ge h/2\).  Combining (4.3) and (4.11) proves

\[
 \boxed{
 \#\{I\in\mathcal P:
 a\sqrt m\le h(I)\le A\sqrt m,
 R(I)\le s(I)/(4t)\}
 \le C_{a,A}2^{-t}{B_m\over\sqrt m}.}          \tag{4.12}
\]

Choose

\[
 t=t(\varepsilon)=\left\lfloor{1\over8\varepsilon}\right\rfloor.
                                                        \tag{4.13}
\]

For sufficiently small fixed \(\varepsilon\), (t\ge1),
(t\le a\sqrt m/4) eventually, and
(R(I)\le\varepsilon s(I)) implies
(R(I)\le s(I)/(4t)).  Hence

\[
 \limsup_{m\to\infty}{\sqrt m\over B_m}
 \#\{I:a\sqrt m\le h(I)\le A\sqrt m,
 R(I)\le\varepsilon s(I)\}
 \le C_{a,A}2^{-t(\varepsilon)}.                \tag{4.14}
\]

This coefficient tends to zero as \(\varepsilon\downarrow0\).

## 5. Proof of the quarantine estimate

We need two elementary height-spectrum facts.  First,

\[
 \sum_{h<a\sqrt m}{b_{m,h}\over h+2}
 \le(\eta(a)+o(1)){B_m\over\sqrt m},
 \qquad \eta(a)\downarrow0.                     \tag{5.1}
\]

This follows from the path-graph spectral bound

\[
 \#\{D:\operatorname {ht}(D)\le h\}
 \le C B_m(\sqrt m/h)^3e^{-cm/h^2}              \tag{5.2}
\]

on dyadic height bands.  Second, for (h\ge a\sqrt m),

\[
 \sum_h{b_{m,h}\over h+2}
 \le {B_m\over a\sqrt m}.                       \tag{5.3}
\]

Now every sector outside \(\mathfrak N(a,\delta,\varepsilon)\) belongs
to at least one of the following three classes:

1. (h<a\sqrt m);
2. (h\ge a\sqrt m) and \(\alpha_h\le\delta\);
3. (h\ge a\sqrt m) and (R(I)\le\varepsilon s(I)).

By (2.4) and (5.1), the first class has size at most

\[
 (\eta(a)+o(1)){B_m\over\sqrt m}.               \tag{5.4}
\]

By the definition of \(\alpha_h\) and (5.3), the second has size at
most

\[
 {\delta\over a}{B_m\over\sqrt m}.              \tag{5.5}
\]

The third is bounded by (4.14).  A union bound proves (0.3).

This argument is deliberately at the reciprocal-height scale.  It does
not attempt to prove a Catalan-order (CP_A) estimate.

### Corollary 5.1 (literal little-oh after quarantine)

For each fixed \(A\), there are deterministic step functions
\(a_m,\delta_m,\varepsilon_m\downarrow0\), with
\(\delta_m/a_m\to0\), such that (0.3a) holds uniformly over every
eligible quotient packing.

#### Proof

Choose \(a_k\downarrow0\) so that \(\eta(a_k)\le1/k\).  After \(a_k\)
is fixed, choose
\(\delta_k>0\) with \(\delta_k/a_k\le1/k\), and then choose
\(\varepsilon_k>0\) so small that

\[
 C_{a_k,A}2^{-\lfloor1/(8\varepsilon_k)\rfloor}\le {1\over k}.
\]

Finally choose \(M_k\) increasing so rapidly that the finite-rank
limsup error in (0.3) is at most \(1/k\) for \(m\ge M_k\), and that
the horizon in (4.13) is at most
\(a_k\sqrt m/4\).  Use the \(k\)-th triple on
\(M_k\le m<M_{k+1}\).  The right side of (0.3) is then at most
\(4/k\).  All estimates used in (0.3) are uniform over the packing, so
the diagonal choice is also uniform.  \(\square\)

## 6. The exact fractional tail-load inequality

The cyclic translation action on physical middle sets is free.  Indeed,
if a nontrivial translation subgroup has orbit size (d>1), every
invariant set has size divisible by (d); but (d\mid N) and
(\gcd(m,N)=1).  Hence every quotient sector has exactly (N) physical
lifts, and

\[
 |\mathfrak N^\uparrow|=N|\mathfrak N|.          \tag{6.1}
\]

Apply (1.6) to every physical lift.  Since (s+1\le H),

\[
 \begin{aligned}
 (N-2H)N|\mathfrak N|
 &\le\sum_T\sum_{I\in\mathfrak N^\uparrow}\pi_I(T)\\
 &\le NB_m\sup_T
       \sum_{I\in\mathfrak N^\uparrow}\pi_I(T).
 \end{aligned}                                   \tag{6.2}
\]

Split the last load into the endpoint strips complementary to
(0.4a)--(0.4b) and the bulk.  Endpoint throughput and the exact Johnson
level counts give, uniformly in (T),

\[
 L^{\rm end}_{\mathfrak N,J}(T)\le E_{A,J}(m),  \tag{6.3}
\]

with (0.6).  Dividing (6.2) by (N(N-2H)) proves

\[
 |\mathfrak N|
 \le{B_m\over N-2H}
 \left(\sup_TL^{\rm bulk}_{\mathfrak N,J}(T)
       +E_{A,J}(m)\right).                       \tag{6.4}
\]

Adding \(|\mathcal P\setminus\mathfrak N|\) gives (0.5).

For reference, the bulk term in (6.4) is literally

\[
 \begin{aligned}
 L^{\rm bulk}_{\mathfrak N,J}(T)
={}&\sum_{\substack{I:\ T\cap Z_I=U_I\\
          \min(j,q_I-j)>J}}
 {1\over\binom{q_I}j^2}\\
 &+\sum_{\substack{I:\ T\cap Z_I=A_I\\
          \min(j,q_I-1-j)>J}}
 {1\over\binom{q_I}j\binom{q_I}{j+1}}.
 \end{aligned}                                   \tag{6.5}
\]

All sectors in (6.5) have one of the strict alternating membership words
(1.7), both inactive cores are genuinely mixed relative to (T), their
height strata use more than a \(\delta\)-fraction of reciprocal capacity,
and (R(I)>\varepsilon s(I)).

Combining (0.3) and (6.4) yields the normalized form

\[
 \begin{aligned}
 \limsup_{m\to\infty}{\sqrt m\over B_m}|\mathcal P|
 \le{}&\eta(a)+{\delta\over a}
 +C_{a,A}2^{-t(\varepsilon)}\\
 &+\limsup_{m\to\infty}{\sqrt m\over N-2H}
 \left(\sup_TL^{\rm bulk}_{\mathfrak N,J}(T)
       +E_{A,J}(m)\right).
                                                        \tag{6.6}
 \end{aligned}
\]

Since (N-2H\sim2m), a bound (o_A(\sqrt m)) on the residual bulk
load makes the last line vanish after \(\gamma\downarrow0\).  This proves
the asserted (ST_A)-scale nature of the gate.

Conversely, if

\[
 |\mathfrak N|\ge c{B_m\over\sqrt m},            \tag{6.7}
\]

then (6.2)--(6.3) give a physical middle set (T) for which

\[
 \boxed{
 L^{\rm bulk}_{\mathfrak N,J}(T)
 \ge {N-2H\over B_m}|\mathfrak N|-E_{A,J}(m)
 \ge (2c-o_A(1))\sqrt m-E_{A,J}(m).}            \tag{6.8}
\]

Taking \(\gamma\) sufficiently small leaves a positive multiple of
\(\sqrt m\).  Thus a failure of (ST_A) has a single exact fractional
tail witness in the mixed alternating quarantine; it cannot hide in
endpoint layers or in an average over different targets.

## 7. Equality and near-equality summary

There are three distinct notions of saturation, and conflating them is a
source of false shortcuts.

### 7.1 Reciprocal-height equality

Equation (2.4) is an identity.  Equality holds exactly when the selected
traces tile every quotient edge in the stratum and every sector is a
minimal (s=h) return.  A (1-o(1)) equality has the quantitative
defects (2.6)--(2.8).

### 7.2 Fixed-core enclosure equality

Equation (3.4) is an identity.  Equality holds exactly when every
inactive-coordinate residence gap is tiled by the sector traces it
encloses.  Near reciprocal equality gives (3.6) on each of the two
translated parities.  The two numerical total defects agree, but the two
gap tilings are different constraints.

### 7.3 Chronology equality

The stable-window inequality (4.3) can be tight only if all of the
following occur:

1. each frame change destroys the maximum possible number (t) of
   previously unspoiled (t)-windows, apart from the two boundary losses;
2. the surviving stable starts from different sectors are all distinct
   (forced by edge-disjointness) and exhaust the available stable-root
   atlas in the relevant height band;
3. the sectors meet the height-gap lower bound whenever the division by
   (h/2) in (4.12) is tight.

The first condition fails when the (t)-neighbourhoods of successive
frame changes overlap.  Hence a family which avoids the exponential
(2^{-t}) contraction must have frame changes separated densely enough
to spoil a linear fraction of all horizons.  The quantitative residual
condition (R>\varepsilon s) in (0.2) is therefore intrinsic, not a
one-step marginal rarity assumption.

Putting the ledgers together gives two levels of rigidity.  An
asymptotically full reciprocal-height near-equality family must have,
outside \(o(1)\) edge/residence measure,

\[
 \begin{array}{ll}
 \text{edge geometry:}&s=h+o(h)\text{ and almost complete stratum cover},\\
 \text{core geometry:}&\rho_J=1-o(1)\text{ on both translated parities}.
 \end{array}                                      \tag{7.1}
\]

Exact equality strengthens these to literal tilings and \(s=h\).
Separately, every positive \(ST_A\)-scale countersequence contains a
positive critical subfamily with

\[
 R(I)>\varepsilon s(I),\qquad
 \alpha_{h(I)}>\delta,                            \tag{7.2}
\]

for some fixed \(a,\delta,\varepsilon>0\), and (6.8) supplies one target
\(T\) carrying a positive \(\sqrt m\)-scale weighted load from strictly
alternating sectors with two genuinely mixed cores.  The assertion in
(7.2) is about a positive critical subfamily; the fixed-target statement
is about weighted kernel load.  Neither says that every selected sector
has those properties.

## 8. Exact remaining boundary

The note proves a vanishing improvement over reciprocal-height capacity
for every simple fixed-core family after excluding the quantified class
\(\mathfrak N(a,\delta,\varepsilon)\).  It also proves the exact
fractional tail-load inequality (0.5) for that class and identifies every
equality defect.

What is not proved is (0.7) for linearly reframing sectors.  Individual
Gaussian returns with a frame change at every step are known, so no
pointwise assertion (R=o(s)) is possible.  Conversely, known local
reciprocal-height saturators occupy globally negligible short-core
fibres.  The unresolved statement is therefore aggregate: rule out a
Catalan-density family satisfying the positive-utilization,
linear-reframing, mixed-alternating conditions (6.5) and (7.2), or
construct such a family and refute (ST_A).  Only a family approaching the
full reciprocal-height constant is additionally forced into the
double-gap near-tiling conditions (7.1).

This is strictly weaker and more accurately calibrated than (CP_A).
The residual load may be (o(\sqrt m)), not (O(1)), and only the
quarantined mixed-tail class needs to be controlled.

## 9. The two-point \(C_H\) statistic gives a conditional refutation, not a positive proof

This section audits the proposed two-point route to (0.7).  Let \(E_H\)
be the roots on quotient cycles longer than \(H+1\) which start an
eligible PBBS first return, and put

\[
 R_H=|E_H|,\qquad
 \mathcal C_H=\sum_{t=1}^{H+1}|E_H\cap\tau^{-t}E_H|.           \tag{9.1}
\]

Make the conflict graph \(G_H\) on \(E_H\), joining two starts precisely
when their actual residence traces share a quotient edge.  Every trace has
at most \(H+1\) consecutive edges.  Hence

\[
 |E(G_H)|\le\mathcal C_H.                         \tag{9.2}
\]

The Caro--Wei inequality followed by Cauchy--Schwarz gives

\[
 \boxed{
 \overline\nu_H=\alpha(G_H)
 \ge {R_H^2\over R_H+2\mathcal C_H}.}            \tag{9.3}
\]

The next theorem connects this statistic to the residual tail load, with
all losses from simplicity and quarantine included.

### Theorem 9.1 (bounded two-point clustering refutes (0.7))

Suppose that along a sequence of ranks

\[
 \liminf {\sqrt m\,R_H\over B_m}=\kappa>0,
 \qquad
 \limsup {\mathcal C_H\over R_H}=\chi<\infty.     \tag{9.4}
\]

Then one can fix \(0<a<A\), \(\delta>0\), and \(\varepsilon>0\) such
that, for the mixed window \(J=\lfloor\gamma\sqrt m\rfloor\),

\[
 \boxed{
 \lim_{\gamma\downarrow0}\limsup_{m\to\infty}
 {1\over\sqrt m}\sup_T
 L^{\rm bulk}_{\mathfrak N,J}(T)
 \ge {\kappa\over2(1+2\chi)}>0.}                 \tag{9.5}
\]

In particular, (9.4) refutes (0.7), \(ST_A\), and the corresponding
separate-cut route.

#### Proof

Equation (9.3) gives an edge-disjoint quotient residence family of size

\[
 \left({\kappa\over1+2\chi}-o(1)\right)
 {B_m\over\sqrt m}.                              \tag{9.6}
\]

The minimal-simple-return reduction, including its start-parity split,
retains at least half of this family.  Thus there is a quotient-edge-
disjoint simple family \(\mathcal P\) with

\[
 |\mathcal P|
 \ge\left({\kappa\over2(1+2\chi)}-o(1)\right)
 {B_m\over\sqrt m}.                              \tag{9.7}
\]

Choose \(a,\delta,\varepsilon\), in that order, so that the right side of
(0.3) is smaller than

\[
 {\kappa\over4(1+2\chi)}.                        \tag{9.8}
\]

This is possible because \(\eta(a)\downarrow0\), then
\(\delta/a\downarrow0\), and finally
\(C_{a,A}2^{-\lfloor1/(8\varepsilon)\rfloor}\downarrow0\).
Equations (0.3), (9.7), and (9.8) give

\[
 |\mathfrak N(a,\delta,\varepsilon)|
 \ge\left({\kappa\over4(1+2\chi)}-o(1)\right)
 {B_m\over\sqrt m}.                              \tag{9.9}
\]

Apply the exact kernel witness (6.8) to this family.  It yields

\[
 {1\over\sqrt m}\sup_TL^{\rm bulk}_{\mathfrak N,J}(T)
 \ge {\kappa\over2(1+2\chi)}
 -{E_{A,J}(m)\over\sqrt m}-o(1).                 \tag{9.10}
\]

By (0.6), the middle term has limsup at most
\(C_A\gamma e^{C_A(\gamma+\gamma^2)}\), which tends to zero with
\(\gamma\).  This proves (9.5). \(\square\)

### Corollary 9.2 (a necessary PBBS clustering law)

If (0.7) holds uniformly over eligible packings and
\(R_H\ge\kappa B_m/\sqrt m\) along a subsequence, then

\[
 \boxed{\mathcal C_H/R_H\longrightarrow\infty.}  \tag{9.11}
\]

This is just the contrapositive of Theorem 9.1.  Notice the direction:
bounded two-point clustering disproves the desired tail contraction.
Thus a positive proof of (0.7) would require eligible starts to occur in
clusters of diverging mean size.

## 10. Divergent \(C_H/R_H\) does not imply (0.7)

The necessary condition (9.11) is not sufficient for a small maximum
packing.  This already fails for cyclic interval systems with exactly the
same support geometry as the PBBS conflict graph.

### Proposition 10.1 (two-point clustering has no upper-packing converse)

There are cyclic interval systems with horizon \(H\to\infty\) for which

\[
 {\mathcal C_H\over R_H}\longrightarrow\infty,
 \qquad
 {\alpha(G_H)\over R_H}\longrightarrow {1\over2}.              \tag{10.1}
\]

#### Proof

Choose integers \(k=k(H)\to\infty\) with \(k\le H/3\).  In one
macroblock put \(k\) starts in \(k\) consecutive positions and give each
the interval of length \(H+1\).  These intervals have a common edge and
form a \(k\)-clique.  In the same macroblock put another \(k\) intervals,
separated from one another and from the clique by more than \(H+1\)
edges.  Repeat \(n\) mutually separated macroblocks around a sufficiently
long cycle.

There are \(R_H=2kn\) starts.  The only pairs of starts at positive
distance at most \(H+1\) lie within the dense cliques, so

\[
 \mathcal C_H=n\binom k2,
 \qquad
 {\mathcal C_H\over R_H}={k-1\over4}\longrightarrow\infty.
                                                               \tag{10.2}
\]

An independent family contains all \(kn\) isolated intervals and one
interval from each clique.  Conversely a clique contributes at most one.
Therefore

\[
 \alpha(G_H)=n(k+1),
 \qquad
 {\alpha(G_H)\over R_H}={k+1\over2k}\longrightarrow {1\over2}.
                                                               \tag{10.3}
\]

This proves (10.1). \(\square\)

The example is an abstract interval system, not a PBBS construction.  Its
logical consequence is exact: no inequality depending only on
\((R_H,\mathcal C_H)\) can prove (0.7).  A positive PBBS theorem must use
higher-order cluster geometry or the decorated predecessor-passage
structure, not merely divergence of the scalar two-point statistic.

## 11. Both translated parities give no independent local Hall gain

It is also important to record why the two fixed-core parity decks do not
close the gap left by Proposition 10.1.  Let \(\sigma\) be the one-edge
translation from the first step-two deck to the second.  For all traces
\(I,J\),

\[
 \boxed{\sigma I\cap\sigma J=\sigma(I\cap J).}   \tag{11.1}
\]

Thus pairwise disjointness of the translated traces is exactly the same
conflict constraint with renamed edge rows.  It is not a second
independent packing condition.

There is a full mixed core-subset hierarchy.  In a height subdeck of edge
volume \(E\), every trace-disjoint simple-sector family satisfies, for
all \(t,u\ge0\),

\[
 \boxed{
 \sum_I\binom{q_I}{t}\binom{q_I}{u}|I|
 \le \Delta_{m;t,u}E,}                           \tag{11.2}
\]

where

\[
 \Delta_{m;t,u}
 =\binom{m+1}{t}\binom{m+1}{u}
  -\binom m{t-1}\binom m{u-1}.                  \tag{11.3}
\]

Indeed the two \((m+1)\)-sets of residence coordinates available at a
paired edge meet in exactly the intervening omitted label.  The first
term in (11.3) chooses a \(t\)-subset and a \(u\)-subset from the two
columns; the second subtracts the choices using their unique common
coordinate in both subsets.  Edge-disjointness permits this charge at
most once per edge, proving (11.2).

Under the present convention \(s+1\le H\), put \(q_*=m-H+1\).  Dividing
(11.2) by
\(\binom{q_*}{t}\binom{q_*}{u}\) gives only the multiplier

\[
 {\Delta_{m;t,u}\over
   \binom{q_*}{t}\binom{q_*}{u}}.                \tag{11.4}
\]

For \(t,u=o(\sqrt m)\), (11.4) is \(1+o_A(1)\); for
\(t,u=O(\sqrt m)\), it stays between positive constants depending only
on \(A\) and the two Gaussian-order bounds.  Hence neither the separate
parity ledgers nor their complete Gaussian-order mixed Hall hierarchy
contains a vanishing coefficient.

This local sharpness is realized inside genuine PBBS dynamics by the
Gaussian mountain inverse fibres: they have simple minimum-gap returns
whose original and translated traces are both disjoint and whose
utilization in (11.2), for
\(t/\sqrt m\to\alpha,\ u/\sqrt m\to\beta\), tends to

\[
 {1-e^{-4c^2}\over2}e^{-c(\alpha+\beta)}>0.       \tag{11.5}
\]

Those fibres have only \(\exp(o(m))\) roots and are removed by the
positive-utilization quarantine.  Thus (11.5) does not refute (0.7);
it proves that the required gain must be global across reduced cores.

## 12. Audited status of equation (0.7)

The strict-alternation kernel and both translated parity decks do not, by
themselves, prove (0.7).  The scalar two-point statistic has the following
one-sided decision power:

\[
 \boxed{
 R_H=\Omega(B_m/\sqrt m),\quad
 \mathcal C_H=O(R_H)
 \ \Longrightarrow\ 
 \text{(0.7) is false}.}                         \tag{12.1}
\]

On the other hand,

\[
 \boxed{
 \text{(0.7) true at critical }R_H
 \ \Longrightarrow\ 
 \mathcal C_H/R_H\to\infty,}                    \tag{12.2}
\]

but Proposition 10.1 shows that (12.2) has no converse at the level of
two-point interval data.

Therefore (0.7) remains neither proved nor refuted by the presently
audited PBBS identities.  Its exact positive input would be a
Pascal-weighted theorem saying that decorated predecessor-passage starts
in the long-period critical reduced-core strata form clusters whose
*maximum independent set*, not merely whose two-point energy, is
\(o(B_m/\sqrt m)\).  Its exact negative input is the pair of asymptotics
in (9.4), which by Theorem 9.1 would also produce a literal mixed
strict-alternation tail witness of order \(\sqrt m\).

## 13. The full two-point degree profile

The scalar \(\mathcal C_H\) records only the first moment of local
clustering.  The exact stronger statistic is the conflict degree

\[
 d_H(D)
 =\#\{E\in E_H\setminus\{D\}:I_D\cap I_E\ne\varnothing\},
                                                               \tag{13.1}
\]

where \(I_D\) is the actual quotient residence trace starting at \(D\).
For \(K\ge0\), put

\[
 R_H^{\le K}=\#\{D\in E_H:d_H(D)\le K\}.          \tag{13.2}
\]

### Theorem 13.1 (degree-profile packing inequality)

For every rank and horizon,

\[
 \boxed{
 \overline\nu_H
 \ge\sum_{D\in E_H}{1\over d_H(D)+1}
 \ge {R_H^{\le K}\over K+1}
 \qquad(K\ge0).}                                  \tag{13.3}
\]

#### Proof

Order the vertices of the conflict graph \(G_H\) uniformly at random and
retain a vertex when it appears before every one of its neighbours.  The
retained vertices form an independent set.  A vertex \(D\) is retained
with probability \(1/(d_H(D)+1)\), so the expected size of the retained
set is the first sum in (13.3).  Some ordering attains at least its
expectation, proving the first inequality.  Every summand with
\(d_H(D)\le K\) is at least \(1/(K+1)\), proving the second. \(\square\)

This inequality removes the defect in Proposition 10.1: a small dense
part cannot hide a positive mass of isolated or bounded-degree starts.

### Theorem 13.2 (bounded-degree mass refutes the residual tail gate)

Fix an integer \(K\ge0\).  Suppose that along a sequence of ranks

\[
 \liminf_{m\to\infty}
 {\sqrt m\,R_H^{\le K}\over B_m}=\kappa_K>0.      \tag{13.4}
\]

Then one can fix quarantine parameters \(a,\delta,\varepsilon>0\) so
that

\[
 \boxed{
 \lim_{\gamma\downarrow0}\limsup_{m\to\infty}
 {1\over\sqrt m}\sup_T
 L^{\rm bulk}_{\mathfrak N,J}(T)
 \ge {\kappa_K\over2(K+1)}>0.}                   \tag{13.5}
\]

Consequently (13.4) refutes (0.7) and \(ST_A\).

#### Proof

Theorem 13.1 gives a quotient packing of size at least

\[
 \left({\kappa_K\over K+1}-o(1)\right)
 {B_m\over\sqrt m}.                              \tag{13.6}
\]

The minimal-simple-return reduction retains half, giving a simple family
of normalized size at least
\(\kappa_K/(2(K+1))-o(1)\).  Choose the quarantine parameters so that
the right side of (0.3) is smaller than
\(\kappa_K/(4(K+1))\).  The quarantined subfamily then has normalized
size at least \(\kappa_K/(4(K+1))-o(1)\).  Equation (6.8), followed by
\(\gamma\downarrow0\), multiplies this constant by two and proves
(13.5). \(\square\)

### Corollary 13.3 (clustering in probability is necessary)

Assume \(R_H\ge\kappa B_m/\sqrt m\) along a subsequence.

1. If \(ST_A\) holds, then for every fixed \(K\),

   \[
   R_H^{\le K}=o_A(B_m/\sqrt m),
   \qquad
   {R_H^{\le K}\over R_H}\longrightarrow0.        \tag{13.7}
   \]

2. The same conclusion follows from the uniform residual assertion
   (0.7).

Hence, under either positive conclusion,

\[
 \boxed{d_H(D)\longrightarrow\infty
 \quad\text{in probability for }D
 \text{ uniform on }E_H.}                        \tag{13.8}
\]

#### Proof

From (13.3),

\[
 R_H^{\le K}\le(K+1)\overline\nu_H.               \tag{13.9}
\]

The first assertion follows from \(ST_A\); divide by the assumed lower
bound for \(R_H\) to get the ratio statement.  The second assertion is
the contrapositive of Theorem 13.2. \(\square\)

This is strictly stronger than
\(\mathcal C_H/R_H\to\infty\).  Indeed rare high-degree clusters can make
the mean diverge while (13.8) fails, exactly as in Proposition 10.1.

There is also a rate form.  If

\[
 \eta_m={\sqrt m\,\overline\nu_H\over B_m}\to0
\quad\text{and}\quad R_H\ge\kappa B_m/\sqrt m,
                                                               \tag{13.10}
\]

choose any \(K_m\to\infty\) with \(K_m\eta_m\to0\).  Then

\[
 {R_H^{\le K_m}\over R_H}
 \le{(K_m+1)\eta_m\over\kappa}\longrightarrow0.   \tag{13.11}
\]

Thus a positive proof forces a genuinely growing local conflict
multiplicity on almost every eligible start, not merely an unbounded
average along a sparse subsequence.

## 14. Equality in the two-point packing chain

The degree-profile theorem has a complete finite equality
classification.

### Theorem 14.1 (Caro--Wei equality)

For a finite graph \(G\),

\[
 \alpha(G)=\sum_{v\in V(G)}{1\over d(v)+1}        \tag{14.1}
\]

if and only if every connected component of \(G\) is a complete graph.

#### Proof

If a component is a clique on \(r\) vertices, its contribution to the
sum is \(r/r=1\), equal to its independence number.  Add over
components.

Conversely, suppose a connected component \(C\) is not complete.  Then
\(\alpha(C)\ge2\).  Root a spanning tree of \(C\), order its root first,
and order every other vertex after its parent.  In the random-order
construction from Theorem 13.1, this particular ordering retains only
the root: every other vertex has an earlier neighbour.  Every ordering
retains at most \(\alpha(C)\) vertices, while this ordering retains
strictly fewer.  Since every ordering has positive probability, the
expected retained size is strictly smaller than \(\alpha(C)\).  The
Caro--Wei inequality is therefore strict on \(C\), and hence on \(G\).
\(\square\)

### Theorem 14.2 (equality in the scalar \(C_H\) bound)

Assume \(R_H>0\).  Equality in the complete chain

\[
 \overline\nu_H
 \ge\sum_{D\in E_H}{1\over d_H(D)+1}
 \ge {R_H^2\over R_H+2|E(G_H)|}
 \ge {R_H^2\over R_H+2\mathcal C_H}              \tag{14.2}
\]

holds if and only if all three conditions below hold.

1. \(G_H\) is a disjoint union of complete graphs.
2. All those complete graphs have the same order.
3. \(|E(G_H)|=\mathcal C_H\).  Equivalently, the forward-lag
   incidences counted in (9.1) map bijectively to the conflict edges:
   there are no counted nonconflicts and no conflict pair is counted in
   both cyclic orientations.

#### Proof

Equality in the first step is Theorem 14.1.  Equality in
Cauchy--Schwarz,

\[
 \sum_D{1\over d_H(D)+1}
 \ge{R_H^2\over\sum_D(d_H(D)+1)},
\]

holds exactly when all \(d_H(D)+1\) are equal.  In a disjoint union of
cliques this says that all clique orders are equal.  The final inequality
in (14.2) is equality exactly when
\(|E(G_H)|=\mathcal C_H\). \(\square\)

Thus the equality objects are equal-size pairwise-conflicting
circular-interval clusters, with no additional short-lag incidence.  If
the union of one such cluster omits a cycle edge, cut the cycle at that
edge; the ordinary interval Helly property then shows that every trace in
the cluster contains one common edge.  A cluster covering its entire
cycle is the only possible non-Helly circular exception.  A maximum
packing chooses exactly one interval from each clique cluster.

This classification separates two possible PBBS outcomes.

* Bounded clique-cluster order on a positive critical mass gives (13.4) and
  refutes \(ST_A\).
* A positive proof requires local clique/cluster order to diverge for almost
  every eligible start, in the strong degree-profile sense (13.8).

The exact remaining dynamical question is now sharper than the scalar
\(C_H\) gate: determine whether the decorated predecessor-passage starts
in the Pascal-critical long-period strata have a positive critical mass
of bounded conflict degree, or instead satisfy (13.8).
