# Gate A audit: pair-arc masks, quadratic discrepancy, and selection drift

Date: 2026-09-06

Status: new theorems about large induced punctured catalogues, including a
quadratic obstruction to a deterministic shortcut and a self-correction
calculation for that obstruction. The stopped arrival estimate C.5a.7,
Gate A persistence, and the full nu conjecture remain OPEN.

This investigation adds this file and its uniquely named checker. Its
conclusions do not change the open status of any matching or covering gate.

## 0. Audit verdict

I audited the stated arguments in:

- `MATH_REDUCTION_GATE_A_AVERAGE_CONFLICT_STOPPED_DESCENT_20260905.md`;
- `MATH_RESEARCH_GATE_A_TRIANGLE_SURPLUS_AND_HARMONIC_ARRIVAL_20260905_d42b7.md`;
- `MASTER_HANDOFF.md`, Sections 4.2--5 and Appendix C.5a.

I found no defect in the average-conflict stopped alternative, its bounded
exact-slice test, the first-harmonic theorem, or the sequential integrated-
surplus criterion. This audit takes the two cited exact-slice fourth moments
as inputs; it does not independently reprove the entire earlier carrier
hierarchy. Their application here does not justify an adaptive transfer.

The new result is more specific than an arbitrary-hypergraph warning:

**For every fixed K, there are induced punctured catalogues of constant
positive target density with chi>K, factorially many edges, current-scale
high/low codegree estimates, and summably small first harmonics. They can
also satisfy every numerical shore-size identity of a matching residual.
Their quadratic harmonic energy stays bounded away from zero.**

Crucially, I do NOT prove that their deleted targets can be partitioned into
punctured rows. Nor do I prove that the actual process reaches these states.
Consequently this is not a counterexample to C.5a.7. It rules out deducing
that estimate merely from the listed state statistics, even after adding
label exchangeability and the correct exact shore sizes.

The same example has strong negative uniform-row drift once developed.
Thus it is not a dynamical trap. That calculation gives a concrete positive
self-correction test for further work, rather than evidence that the
conjectured arrival estimate is false.

## 1. Definitions and the new theorem

Write

\[
 b=2r+1,\qquad s=2r,\qquad
 N_k=\binom bk,\qquad Z_0=b!,\qquad D_k=sZ_0/N_k,
 \qquad k\in\{r,r-1\}.
\]

The directed punctured row of a permutation w consists of its rank-r and
rank-(r-1) cyclic windows at starts 1,...,b-1. All residual hypergraphs below
are induced: they contain EVERY original row whose targets are retained.

Fix an integer m>=2, independently of r, and distinguish m disjoint ground-
label pairs

\[
 \{a_1,b_1\},\ldots,\{a_m,b_m\}.
\]

A target A splits pair i when it contains exactly one of a_i,b_i. Define

\[
 j(A)=\#\{i:|A\cap\{a_i,b_i\}|=1\},\qquad
 R_k=\{A\in\tbinom{[b]}k:j(A)\le1\}.
 \tag{1.1}
\]

Let H be the catalogue induced by R_r,R_(r-1). Set

\[
 \xi_m={m+1\over2^m},\qquad
 a_m={(m-1)!\over(2m-1)!},\qquad
 g_m=2^{m-1}a_m.
 \tag{1.2}
\]

As in C.5a, all retained targets, including isolated ones, count in n_k.
Put z_k=sZ/n_k and

\[
 \chi={\bar C\over s(z_r+z_{r-1})}.
\]

For harmonic statements use the UNIFORM ORIGINAL k-layer inner product and

\[
 u_k(A)=\mathbf1_{R_k}(A)(d_H(A)/z_k-1).
 \tag{1.3}
\]

Let P_1 be projection onto zero-mean linear ground-label functions. Let P_2
be projection onto polynomials of degree at most two orthogonal to all
polynomials of degree at most one on the layer.

### Theorem 1.1 (macroscopic induced quadratic discrepancy)

For every fixed m>=2, as r tends to infinity:

\[
 {n_k\over N_k}=\xi_m+O_m(r^{-1}),\qquad
 {Z\over Z_0}=a_m+O_m(r^{-1}),\qquad
 {z_k\over D_k}={a_m\over\xi_m}+O_m(r^{-1}).
 \tag{1.4}
\]

Uniformly over retained targets of either shore,

\[
 {d_H(A)\over z_k}=
 \begin{cases}
 (m+1)/2+O_m(r^{-1}),&j(A)=0,\\
 (m+1)/(2m)+O_m(r^{-1}),&j(A)=1.
 \end{cases}
 \tag{1.5}
\]

In particular,

\[
 \boxed{\chi(H)={(m+1)^2\over4m}+O_m(r^{-1}).}
 \tag{1.6}
\]

The empirical degree moments on each retained shore satisfy

\[
 U_{2,k}={(m-1)^2\over4m}+O_m(r^{-1}),
\]
\[
 U_{4,k}={(m-1)^4\over16(m+1)}(1+m^{-3})+O_m(r^{-1}).
 \tag{1.7}
\]

Nevertheless the first harmonic is small:

\[
 \|P_1u_k\|_2^2=O_m(r^{-2}),\qquad
 \|P_1u_k\|_4^4=O_m(r^{-4}),
 \tag{1.8}
\]

whereas the second harmonic is not:

\[
 \boxed{\|P_2u_k\|_2^2\longrightarrow
                  {(m-1)^2\over m4^m}>0.}
 \tag{1.9}
\]

These states also have the following CURRENT-scale geometry. With high
pairs defined as middle-middle disjointness or lower-middle containment,

\[
 \max_{u\ne v}\lambda_{uv}=O_m(z_r/r),\qquad
 \max_{\substack{\{u,v\}\\\text{low}}}\lambda_{uv}=O_m(z_r/r^2),
 \tag{1.10}
\]

and, for every current row F,

\[
 \sum_{\substack{\{u,v\}\subset F\\\text{high}}}\lambda_{uv}=O_m(z_r),
 \qquad
 \sum_{\substack{\{u,v\}\subset F\\\text{low}}}\lambda_{uv}=O_m(z_r/r).
 \tag{1.11}
\]

The high-pair graph is triangle-free, exactly as in the audited note.
All constants in this theorem may depend on fixed m.

For example m=2 gives limiting chi=9/8 and second-harmonic energy 1/32.
For K=2, m=6 gives limiting chi=49/24>2. For arbitrary fixed K choose m
with (m+1)^2/(4m)>K. The resulting xi_m and a_m are small but positive
CONSTANTS, not quantities tending to zero with r.

## 2. The circle-arc calculation

This section proves the edge-count and incidence assertions, including the
fact that these are uniform measures on induced catalogues, not arbitrarily
weighted row subfamilies.

### 2.1 The continuous limit

Place the 2m distinguished labels independently and uniformly on a circle
of circumference one. Read windows of length 1/2. For one pair, the
indicator that the moving window splits the pair is 1/2-periodic. On the
quotient circle of circumference 1/2 it is the indicator of one oriented
arc.

After rescaling the quotient circle to circumference one, the arc's start
is uniform and its length is uniform on [0,1], independently. Different
pairs give independent arcs.

Here is a direct verification of the distribution statement. The positions
of a pair modulo 1/2 are independent uniform points, and their half-circle
bits are independent fair bits. The split indicator toggles at the two
quotient positions. The relative half-circle bit chooses, with probability
1/2 each, one of the two complementary arcs between them. An oriented pair
of independent uniform endpoints has independent uniform start and uniform
clockwise length. There remains one independent fair common half-circle
flip of both labels. It preserves the split arc and complements both
membership bits at any fixed window start.

Write the arc lengths as l_1,...,l_m and L=sum_i l_i. All windows satisfy
(1.1) exactly when the interiors of these m arcs are disjoint.

For prescribed lengths with L<1, the probability over independent uniform
starts that the arcs are disjoint is

\[
                         (1-L)^{m-1}.                 \tag{2.1}
\]

To check the constant, rotate the start of arc 1 to zero. For any of the
(m-1)! circular orders of the other labelled arcs, the m gaps are
nonnegative and sum to 1-L. The volume in the remaining m-1 start
coordinates is (1-L)^(m-1)/(m-1)!. Sum over the circular orders. If L>1 the
probability is zero. Boundary cases have measure zero.

Consequently the probability of the allowed-row event E is

\[
 \Pr(E)=\int_{l_i\ge0,\ L\le1}(1-L)^{m-1}\,dl_1\cdots dl_m
        ={(m-1)!\over(2m-1)!}=a_m.
 \tag{2.2}
\]

For clarity, integrate first at a fixed L. The simplex cross-section has
volume L^(m-1)/(m-1)!, and the remaining integral is the elementary beta
integral. Conditional on E, L has density proportional to

\[
                       L^{m-1}(1-L)^{m-1},\quad0<L<1.
 \tag{2.3}
\]

It follows by the same beta integrals and symmetry that

\[
 \mathbb E[L\mid E]=1/2,\qquad
 \mathbb E[l_i\mid E]=1/(2m),\qquad
\operatorname{Var}(L\mid E)={1\over4(2m+1)}.
\tag{2.4}
\]

There is an independent check of (2.2): anchor the first arc's start in the
circular order of the 2m independent uniform endpoints. The remaining
(2m-1)! endpoint orders are equiprobable. Disjointness holds exactly when
each start is immediately followed by its own end. There are (m-1)! such
orders, one for each circular order of the m labelled blocks.

Thus a uniform window of a uniform allowed row splits no pair with
probability 1/2, and splits each specified pair with probability 1/(2m).
The independent common half-circle flips described above remain fair after
conditioning on E. Conditional on any split pattern, the m remaining
membership-orientation bits are independent fair bits.

### 2.2 Why the discrete two-shore catalogue has this limit

The distinguished positions in a uniform permutation of b labels are
uniform distinct grid points. Couple these with independent continuous
positions by rounding to a b-grid and conditioning on distinct rounded
positions. A collision of rounded positions has probability O_m(1/b).

The transition points of the continuous moving-window membership pattern
are the 2m positions and their translates by -1/2. The probability that
any two of these 4m transition points are within 10/b is O_m(1/b); the two
transition points of the same label are always distance 1/2 apart and do
not contribute to this exceptional event.

Outside this exceptional event, rounding positions and replacing window
length 1/2 by either r/b or (r-1)/b move transitions by less than 3/b and
do not change their cyclic order. Every intervening membership pattern is
still attained at several grid starts. Omitting just start zero cannot
erase a forbidden pattern. Conversely an allowed continuous pattern
sequence remains allowed on both discrete shores. Thus E agrees with the
actual two-shore row-survival event except with probability O_m(1/b).

The empirical proportion of starts giving any fixed distinguished-label
membership pattern also changes by O_m(1/b), outside the exceptional event:
there are only 4m moving endpoints. Omitting a single start adds O(1/b).
All variables in these comparisons are bounded. Since a_m>0 is fixed,
division by the row-survival probability is harmless for large r.

This proves

\[
 Z/Z_0=a_m+O_m(r^{-1}),                                  \tag{2.5}
\]

and transfers all the conditional window-pattern probabilities in (2.4)
with O_m(r^-1) error. The same proof applies if survival is tested on ONLY
one of the two shores. In particular the number of rows passing a
one-shore test but failing the two-shore test is O_m(Z_0/r).

### 2.3 From pattern probabilities to degrees

For any fixed membership pattern epsilon on the 2m distinguished labels,
a uniform original k-target has that pattern with probability

\[
 {\binom{b-2m}{k-|\epsilon|}\over\binom bk}
       =2^{-2m}+O_m(r^{-1}).                            \tag{2.6}
\]

There are 2^m zero-split patterns and m2^m one-split patterns. Hence the
retained density is xi_m+O_m(r^-1).

Under a uniform allowed row and a uniform retained start, (2.4) and the
independent common flips give probability

\[
 \begin{cases}
 2^{-m-1}+O_m(r^{-1}),&\text{each zero-split pattern},\\
 (m2^{m+1})^{-1}+O_m(r^{-1}),&\text{each one-split pattern}.
 \end{cases}                                           \tag{2.7}
\]

The induced catalogue is invariant under permutations of undistinguished
labels. Thus all targets with a specified distinguished membership pattern
have the same degree. Double-count the incidences in that pattern class:
its total degree is sZ times its window probability in (2.7). Divide by
its class size from (2.6), and then by z_k=sZ/n_k. This gives (1.5).

This argument uses uniform current rows and their literal incidences. No
independent-retention approximation is used for these residual masks.

## 3. Conflict and harmonic calculations

### 3.1 The conflict normalization

Let D=D_r. The complete-catalogue pair inventory in Appendix C.8 gives,
uniformly over EVERY original row F,

\[
 \sum_{\{u,v\}\subset F}d_{H_0}(u,v)=O(D).
 \tag{3.1}
\]

For the induced residual, therefore,

\[
 0\le\sum_{v\in F}d_H(v)-C_F
     =\sum_{G\in H}(|F\cap G|-1)_+
     \le O(D).                                         \tag{3.2}
\]

The self-overlap is included in both sides. Averaging gives

\[
 \chi=\sum_{k\in\{r,r-1\}}{z_k\over z_r+z_{r-1}}
                  (1+U_{2,k})+O_m(r^{-1}),              \tag{3.3}
\]

because z_k=Theta_m(D) and s=2r. Among uniform retained targets the
zero-split class has limiting mass 1/(m+1), and the total one-split class
has mass m/(m+1). Substitution of (1.5) proves (1.6)--(1.7).

Monotonicity of codegrees under target deletion, (1.4), and the complete
high/low pair inventory give (1.10)--(1.11). This use of initial estimates
is legitimate HERE because z_k/D_k converges to the positive constant
a_m/xi_m. It is not legitimate for an arbitrary depleted adaptive state.

### 3.2 First harmonics

For any current row family and any retained shore R of density xi, let
p_i be the fraction of dirty rank-k windows containing label i. The exact
cyclic incidence count gives

\[
 \delta_i:=\mathbb E_{\rm layer}[u_k(A)\mathbf1_{i\in A}]
       ={\xi\over s}(k-p_i)
            -\Pr_{\rm layer}(A\in R,\ i\in A).
 \tag{3.4}
\]

For the masks (1.1), complementing all distinguished membership bits
preserves membership in R. Equation (2.6) implies, for each distinguished
label,

\[
 \Pr(A\in R,\ i\in A)=\xi k/b+O_m(r^{-1}).
\]

Hence delta_i=O_m(1/r) there. Both the mask and the induced catalogue are
invariant under permutations of the other b-2m labels. Their deltas are
equal. Since sum_i delta_i=k E u_k=0, each undistinguished delta is
O_m(r^-2).

On the zero-sum coefficient space the linear coordinate Gram eigenvalue is

\[
 \lambda_1={k(b-k)\over b(b-1)}=\Theta(1).
\]

Consequently

\[
 P_1u_k(A)=\sum_{i\in A}{\delta_i\over\lambda_1},\qquad
 \|P_1u_k\|_2^2={1\over\lambda_1}\sum_i\delta_i^2=O_m(r^{-2}).
 \tag{3.5}
\]

The sum of the O(r^-2) undistinguished coefficients and the bounded number
of O(r^-1) distinguished coefficients has absolute value O_m(r^-1)
pointwise. This also proves the fourth-moment assertion in (1.8).

### 3.3 The nonzero quadratic component

In the limiting independent fair-bit model put

\[
 Q_i=(2\mathbf1_{a_i\in A}-1)(2\mathbf1_{b_i\in A}-1).
\]

Q_i is +1 for an unsplit pair and -1 for a split pair. The limiting u is

\[
 u_\infty=
 \begin{cases}
 (m-1)/2,&j=0,\\
 -(m-1)/(2m),&j=1,\\
 0,&j\ge2.
 \end{cases}                                           \tag{3.6}
\]

It has mean zero and is invariant under simultaneously flipping the two
bits of any one pair. Thus its linear coefficients and all cross-pair
quadratic coefficients vanish. For each specified pair,

\[
 \mathbb E[u_\infty Q_i]
 ={1\over2^m}\left\{{m-1\over2}
                -(m-2){m-1\over2m}\right\}
 ={m-1\over m2^m}.                                     \tag{3.7}
\]

The Q_i are orthonormal quadratic functions. The squared norm of the
quadratic projection is therefore (m-1)^2/(m4^m).

To justify passage from the product cube to slice harmonics, rather than
identifying them without proof, observe that u_k is a function only of
the 2m distinguished membership bits. Its projection onto slice
polynomials of degree at most two is invariant under every permutation of
undistinguished labels. Any invariant polynomial of degree at most two
reduces on the k-layer to a polynomial of degree at most two in the
distinguished bits: replace the sum of other bits by k minus their sum,
and the sum of other pair products by its binomial coefficient of order
two. The analogous statement holds for degree at most one.

There are only finitely many resulting monomials. Their Gram matrices
converge, by (2.6), to the positive definite fair-bit Gram matrices.
Their inner products with u_k converge by (1.5). Orthogonal projections,
including the difference between degrees at most two and at most one,
therefore converge. This proves (1.9) rigorously.

## 4. Enforcing the exact matching-size identities

The unmodified masks need not have the correct difference n_r-n_(r-1).
The following adjustment removes that purely numerical objection without
asserting any matching reachability.

### Theorem 4.1 (size-compatible version)

For all sufficiently large r there are supersets R_k^+ of the masks above
whose induced catalogue H^+ satisfies

\[
 |R_k^+|=N_k-st_r\quad(k=r,r-1)
 \quad\text{for one integer }t_r\ge0,                    \tag{4.1}
\]

and still has (1.4), (1.6), (1.7), (1.9), (1.10), and (1.11), with
o(1) in place of any rate needed for (1.9). Its first harmonics satisfy

\[
 \|P_1u_k^+\|_2^2=O_m(r^{-1}),\qquad
 \|P_1u_k^+\|_4^4=O_m(r^{-2}).                           \tag{4.2}
\]

In particular their contribution to the C.5a fourth-moment arrival test,
summed over O_K(r log r) checkpoints at these constant densities, is o(1).
The padding can in fact be chosen so that the stronger bounds (1.8) hold
as well. This also gives the audited numerical bound
\(\|P_1u_k^+\|_2^2\le1/(2r)\) for all sufficiently large r.

#### Proof

Let Delta_0=N_r-N_(r-1)=2N_(r-1)/r. Complement invariance of (1.1) implies
that its density as a function of the rank k is symmetric about b/2.
More explicitly, sum

\[
              {(k)_{|\epsilon|}(b-k)_{2m-|\epsilon|}\over(b)_{2m}}
\]

over allowed patterns epsilon. This is a polynomial in k divided by
(b)_(2m), symmetric about b/2, with second derivative O_m(b^-2) in a
fixed-width central interval. Therefore the densities at r and r-1 differ
by O_m(r^-2). It follows that

\[
 n_r-n_{r-1}=\xi_m\Delta_0+O_m(N_{r-1}/r^2).
 \tag{4.3}
\]

Pad the lower mask by h_L<s targets so that

\[
 n_{r-1}^+=N_{r-1}-s\left\lfloor{N_{r-1}-n_{r-1}\over s}\right\rfloor.
\]

Then pad the middle mask to size n_r^+=n_(r-1)^++Delta_0. By (4.3) its
padding size is

\[
 h_M=(1-\xi_m)\Delta_0+O_m(N_{r-1}/r^2)+O(r),
\]

which is positive and O_m(N_r/r). There are enough excluded middle targets.
This establishes (4.1), including divisibility. The added targets can be
chosen arbitrarily.

Rows in H^+ not already in H either pass the ORIGINAL lower-mask test, or
contain one of the h_L added lower targets. Section 2.2 bounds the number
of the former extra rows by O_m(Z_0/r). The latter number is at most
h_L D_(r-1)=O(r^2 Z_0/N_(r-1))=o(Z_0/r). Hence

\[
                         0\le Z^+-Z=O_m(Z_0/r).         \tag{4.4}
\]

All degrees are at most the original degrees, and z_k,z_k^+ are
Theta_m(D_k). Both extended normalized deviations are thus bounded in
absolute value by a constant depending only on m. Also

\[
 {1\over N_k}\sum_A(d_{H^+}(A)-d_H(A))
            ={s(Z^+-Z)\over N_k}=O_m(D_k/r).
\]

Together with the O(1/r) relative change of z_k and O(1/r) added target
mass this proves

\[
 \|u_k^+-u_k\|_1=O_m(r^{-1}),\qquad
 \|u_k^+-u_k\|_2^2=O_m(r^{-1}).                          \tag{4.5}
\]

The degree-moment limits, conflict limit, and quadratic-projection limit
are preserved. Codegree bounds follow as before from the positive current
degree scale.

For the first harmonic, use (3.4). Padding changes every target coordinate
marginal by at most O_m(1/r), and every dirty marginal lies in [0,1]. Thus
every delta_i^+ is O_m(1/r), with sum zero. The projection coefficients
c_i=delta_i^+/lambda_1 satisfy

\[
 \max_i|c_i|=O_m(1/r),\quad \sum_i c_i^2=O_m(1/r),\quad
 \sum_i c_i^4=O_m(1/r^3),\quad \sum_i c_i=0.
\]

This proves the squared-norm bound in (4.2). For the fourth moment, writing
p_j=(k)_j/(b)_j, the exact equality-pattern expansion is

\[
 \mathbb E\left(\sum_{i\in A}c_i\right)^4
 =(p_1-7p_2+12p_3-6p_4)\sum_i c_i^4
   +3(p_2-2p_3+p_4)\left(\sum_i c_i^2\right)^2.
\]

The coefficients are bounded, proving O_m(r^-2). Restriction to the
retained shore costs only its reciprocal constant density. This proves
the assertions for arbitrary padding.

For the stronger optional choice, choose the h_M middle padding targets
uniformly without replacement from the excluded middle mask. Its coordinate
inclusion probabilities are k/b+O_m(1/r), by the same fixed-pattern counts
and complement symmetry used in Section 3.2. Each padding coordinate count
has variance at most h_M. Chebyshev and a union bound over b labels show
that, with probability tending to one, all these counts differ from
h_M k/b by O_m(N_r/r^2): the fluctuation threshold N_r/r^2 has total
failure probability O_m(r^4/N_r). Choose one such padding. The fewer than
s lower padding targets already satisfy the analogous error bound.

For old and new dirty marginals, (4.4) and H contained in H^+ imply
\(\max_i|p_i^+-p_i|=O_m(1/r)\). Subtract (3.4) in the two states. If h
targets were added in that shore, the density contribution minus the
padding coordinate count is

\[
 {h\over N_k}\left\{{k-p_i\over s}-{k\over b}\right\}
                      +O_m(r^{-2})=O_m(r^{-2}),
\]

and the dirty-marginal change contributes another O_m(r^-2). Therefore
every delta_i changes by O_m(r^-2). The bounded number of distinguished
coordinates still have delta_i^+=O_m(1/r), and all the others have
delta_i^+=O_m(r^-2). The proof of (3.5), including its pointwise bound,
now gives (1.8) for this chosen padding. This finishes the theorem.

This elementary without-replacement experiment is only an existence proof
for the padding. It is not an assertion about the matching-arrival law.

Theorem 4.1 supplies the equations required of a matching complement, NOT
a decomposition of that complement into t_r disjoint rows. That extra
combinatorial assertion would be substantial and has not been established.

For m=2 there is even an explicit reason these masks are not matching
residuals. A fixed pair is split by exactly 2d full rank-r windows, where
d is its shorter cyclic positional distance, 1<=d<=r. To be split at all
2r retained starts, it must have d=r and its unique unsplit window must
be the dirty window. That window contains neither label; the pair is
then uniquely the two endpoints of its complementary (r+1)-position arc.
Two disjoint pairs cannot both have this property. Every punctured row
therefore has a retained middle target splitting at most one of the two
pairs. Thus R_r meets every original row, and the complement of any R^+
from this construction contains no row when m=2. This reinforces, rather
than removes, the distinction between this static theorem and an actual
arrival statement. No corresponding reachability assertion is made for
the larger m used to violate a given cap, such as m=6 for K=2.

## 5. What this says about independent masks and actual arrivals

Fix K>1 and then m with (m+1)^2/(4m)>K. For all sufficiently large r,

\[
                         T_K(H^+)=1.                    \tag{5.1}
\]

The shore sizes obey exactly the matching identities, their densities tend
to xi_m>0, and

\[
 z_r^+=\Theta_m(D_r)=\exp((2+o(1))r\log r).
\]

Apply a uniform random permutation of the ground labels to this one
deterministic state. The resulting law is label-exchangeable and supported
on ONE exact shore-size fibre. Equations (1.10)--(1.11), (4.1)--(4.2), and
(5.1) hold on every sample.

In contrast, the independently uniform exact-shore slice with these same
sizes satisfies the audited theorem

\[
                       \mathbb E_{\rm sl}T_K=O_{K,m}(r^{-2}).
 \tag{5.2}
\]

Thus exact sizes, label exchangeability, a factorial edge floor, summable
first harmonics, and even the stated current-scale codegree bounds do not
imply a bounded-test comparison to a uniform slice. The loss can already
be at least order r^2 for this one statistic.

This is a separation of two laws, not a substitution of this law for the
actual nibble. The actual sufficient estimate remains

\[
 \mathbb E\big[\mathbf1_{j<\tau}\mathbf1_{x_{j+1}>x_*}
                         T_K(H_{j+1})\big]
 \le r^{\kappa+o(1)}(rx_*^3)^{-2}+e^{-\Omega(r)},
 \qquad\kappa<1-6\alpha.
 \tag{5.3}
\]

Neither matching reachability of H^+ nor a lower bound on its arrival
probability has been proved. A theorem using the actual history can
therefore exclude or suppress these shapes without contradicting anything
here. Conversely, conditioning a raw child to be capped still removes the
first-exit event and cannot establish (5.3).

## 6. Selection attempts and a positive self-correction calculation

### 6.1 Changing the first selected row cannot give exact monotonicity

The complete punctured catalogue is row-transitive under ground-label
permutations. Deleting any one row therefore gives isomorphic children,
with the same value of chi. The audited triangle-surplus theorem says the
uniform average of their chi increments is Theta(D_r/(r Z_0))>0.

It follows that, for every sufficiently large r, EVERY first row has that
positive increment. In particular no deterministic rule, min-child-chi
rule, inverse-conflict weighting, or other distribution on a single first
row can make chi nonincreasing at the initial state.

This rules out an uncorrected monotonicity proof, not a fixed-K selection
theorem: the increment is very small. A corrected potential or the
integrated-surplus criterion could still work.

### 6.2 The pair-arc examples themselves strongly self-correct

The macroscopic examples above do not show that uniform-row selection has
bad drift. In fact their drift is good. Here is a quantitative theorem for
the UNPADDED H of Theorem 1.1.

Let V_C=Var_F C_F, T=Z bar C, and let B be the closed conflict matrix.
Then

\[
 {\bar C\over sD_r}\longrightarrow g_m{m+1\over m},\qquad
 {V_C\over s^2D_r^2}\longrightarrow
              {g_m^2(m-1)^2\over m^2(2m+1)}>0.           \tag{6.1}
\]

Indeed, for a uniform current row its limiting proportion of starts
splitting some pair is L, with the law (2.3). On both shores the zero-
and one-split target degrees, divided by D_r, tend uniformly to g_m and
g_m/m. Hence, using (3.2),

\[
 {C_F\over sD_r}\ \Longrightarrow\
        2g_m\{1-(1-1/m)L\}.                             \tag{6.2}
\]

All these variables are uniformly bounded for fixed m, so first and
second moments converge. Equations (2.4) give (6.1).

The triangle estimate in the audited note is also effective at this
current scale. To see this without assuming a missing adaptive theorem,
decompose the target codegree matrix as Lambda=P+Q into high and low pairs.
The high graph within a row has maximum degree at most four, and thus

\[
 \|P\|_{\rm op}=O(D_r),\quad \|Q\|_{\rm op}=O(rD_r),\quad
 \operatorname{tr}(P^2)=O_m(ZD_r),\quad
 \operatorname{tr}(Q^2)=O_m(ZD_r/r).
\]

The last two bounds follow by double-counting the pair sums in (1.11).
Triangle-freeness of the high graph and the trace inequality (2.2) in the
audited note yield tr(Lambda^3)=O_m(ZD_r^2). Also
sum_v d(v)^3=O_m(rZD_r^2). Therefore

\[
                     \operatorname{tr}(B^3)=O_m(rZD_r^2).
 \tag{6.3}
\]

Use the sequential criterion's exact definitions

\[
 A(H)={\operatorname{tr}(B^3)-2ZV_C\over ZT},\qquad
 \rho={f(n_r,n_{r-1})\over f(n_r-s,n_{r-1}-s)}-1,
\]
\[
 f(n_r,n_{r-1})={n_rn_{r-1}\over s^2(n_r+n_{r-1})}.
\]

Here rho=O_m(D_r/Z). Combining (6.1)--(6.3) gives

\[
 \boxed{A(H)-\rho
 =-\left\{{2g_m(m-1)^2\over m(m+1)(2m+1)}+o(1)\right\}
                         {sD_r\over Z}<0.}
 \tag{6.4}
\]

Thus the sequential positive surplus R(H)=[A(H)-rho]_+ is zero on these
states for all sufficiently large r, despite their large chi.

There is also an actual negative finite-jump drift, not just a tangent.
The exact upper bound used before taking the positive part in the audited
note is

\[
 {\mathbb E[\chi(H')\mid H]\over\chi(H)}
       \le {1+A(H)+8\delta\beta\over1+\rho},\qquad
 \delta={\max C_F\over Z},\quad\beta={\bar C\over Z}.
\]

Here delta,beta=O_m(sD_r/Z), so delta beta=o(sD_r/Z). Equation (6.4)
therefore makes the right side strictly less than one. In particular some
deterministic next-row choice reduces chi from each such state.

This is a genuine self-correction result for a specific family of induced
quadratic distortions. It does not bound the integrated positive surplus
on arbitrary stopped histories. It also explains why the bad-state
construction should not be misrepresented as a failure of uniform greedy
dynamics.

### 6.3 The precise missing step after these attempts

The first-harmonic estimates alone cannot force small higher-harmonic
energy: Theorems 1.1 and 4.1 exhibit constant quadratic energy with a large
current catalogue and the strong pair estimates already in force.

The triangle exclusion has not supplied the required integrated bound for
tr(B^3)-2Z V_C-ZT rho on the actual history. Section 6.2 succeeds because
the FULL induced row law is explicitly computable by disjoint arcs, which
provides a positive current-scale variance of companion loads. No such
lower bound, or substitute signed inequality, has been proved uniformly
for the arrival states of the punctured nibble.

For the parallel law, the remaining information is genuinely about how
the history biases quadratic and higher target patterns. For a different
selection law, one must prove either a compensated-potential trajectory or
an integrated-surplus bound, not just optimize the initial distribution
or use label symmetry. Neither conclusion is established by this audit.

No four-block, almost-cover selection, or all-depth continuation has been
used or claimed.

## 7. Verification

New checker:
`scratch_gate_a_pair_arc_masks_20260906_87c2e.py`.

It uses exact integer/fraction arithmetic for finite catalogues and moments.
Distinguished-label placements are counted modulo within-pair swaps and
pair permutations; every placement is restored with multiplicity
2^m m! (b-2m)!. Its compressed census was checked against full permutation
enumeration at (r,m)=(2,2),(3,2),(3,3), including the empty finite case.

It checks the limiting degree and quadratic-coefficient identities for
m=2,...,10, exhaustively checks the disjoint-arc endpoint orders for
m=2,...,5, and checks exact finite degree moments and linear projections at
(r,m)=(4,2),(8,2),(16,2),(24,2),(5,3),(8,3). Small-r values need not be
monotone in r. For example at m=2, the edge fraction is 0.13695904 at r=24,
approaching 1/6; the middle quadratic test is 0.13704709, approaching 1/8.
These are checks of the calculations, not proofs of the limiting theorem.

The two existing checkers were also rerun unchanged:

- Mean-conflict checker: 3,297 graph/mark-law checks and 2,189 hypergraph
  checks passed.
- Triangle/harmonic checker: 1,099 graph checks, both literal catalogues,
  320 harmonic cases, and its large-r rational surplus/drift certificates
  passed.

No check here samples or estimates the actual stopped arrival law.
