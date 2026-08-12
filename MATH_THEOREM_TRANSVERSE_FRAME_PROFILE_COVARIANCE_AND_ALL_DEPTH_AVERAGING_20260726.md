# Transverse frame profiles: exact covariance, sparse all-depth averaging, and the surviving floor gate

Date: 2026-07-26

Method: pure mathematics only.  The valid recursive context-array factor is
used only through the literal fact that a depth-(q) lower face preserves the
number of full pairs of its physical matching (and, by complementation, an
upper face preserves the number of empty pairs).  No crossed recursion is
used.

## 0. Result

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\tag{0.1}
\]

For a perfect matching (M) and a lower target
(T\in\binom{[2m]}{m-q}), write (F_M(T)) for the number of edges of
(M) contained in (T).  The exact coarse target profile obtained by
averaging a fixed-frame factor inside the wreath stabilizer of (M) is

\[
 R_{M,q}^-(T)=\frac{V_{F_M(T)}}{T_{F_M(T),q}},
\tag{0.2}
\]

where

\[
 V_f=\frac{m!2^{m-2f}}{f!^2(m-2f)!},\qquad
 T_{f,q}=\frac{m!2^{m-2f-q}}
 {f!(f+q)!(m-2f-q)!}.
\tag{0.3}
\]

For an upper target (U), define (R_{M,q}^+(U)) by (0.2) with
(F_M(U^c)).  Thus the two signs have identical statistics.  Exactly,

\[
 \frac1{N_q}\sum_T R_{M,q}^{\pm}(T)
 =\lambda_q:=\frac W{N_q}.
\tag{0.4}
\]

Define

\[
 \sigma_{m,q}^2
 :=\frac1{N_q}\sum_f\frac{V_f^2}{T_{f,q}}-\lambda_q^2.
\tag{0.5}
\]

If (q=x\sqrt m+O(1)), uniformly for (0\le x\le A), then

\[
 \lambda_q=e^{x^2+o(1)},\qquad
 \sigma_{m,q}^2=e^{6x^2}-e^{2x^2}+o(1).
\tag{0.6}
\]

There is a sparse deterministic catalogue of (d) exact coordinate
frames whose averaged coarse profiles

\[
 \overline R_q^{\pm}=\frac1d\sum_{i=1}^dR_{M_i,q}^{\pm}
\tag{0.7}
\]

satisfy

\[
 \sum_{q=1}^{H}\sum_{\epsilon\in\{-,+\}}
 \left\|\overline R_q^\epsilon-\lambda_q\mathbf1\right\|_2^2
 \le \frac4d\sum_{q=1}^{H}N_q\sigma_{m,q}^2.
\tag{0.8}
\]

In particular, for (H=A\sqrt m+O(1)),

\[
 \boxed{
 \sum_{q\le H,\epsilon}
 \left\|\overline R_q^\epsilon-\lambda_q\mathbf1\right\|_2^2
 \le
 \left(4J_A+o(1)\right)\frac{W\sqrt m}{d},}
\tag{0.9}
\]

where

\[
 J_A=\int_0^A\left(e^{5x^2}-e^{x^2}\right)\,dx.
\tag{0.10}
\]

The same catalogue has total coarse Hall deficit

\[
 \boxed{
 \sum_{q\le H,\epsilon}\sum_T
       (1-\overline R_q^\epsilon(T))_+
 \le
 \left(4K_A+o(1)\right)\frac{W\sqrt m}{d},}
\tag{0.11}
\]

with

\[
 K_A=\int_0^A
 \frac{e^{5x^2}-e^{x^2}}{e^{x^2}-1}\,dx
 =\int_0^A
 \left(e^{4x^2}+e^{3x^2}+e^{2x^2}+e^{x^2}\right)\,dx.
\tag{0.12}
\]

The integrand at (x=0) is interpreted as its limit (4).  Consequently
any (d/\sqrt m\to\infty) clears the entire fixed-profile Gaussian Hall
cut fractionally.  In particular (d=m) gives (O_A(W/\sqrt m)=o(W)).
This is a genuinely sparse catalogue compared with the ((2m-1)!!)
perfect matchings or the ((2m)!) coordinate frames.

This positive statement is exactly a **barycentric** one.  It does not
produce the negative floor covariance needed by an integral mixed-packet
resolution.  If (Z_i) is the integral target-load vector of resolution
(i), (w_i\ge0), (sum_iw_i=1), and
(\overline Z=\sum_iw_iZ_i), then for every floor (c),

\[
 \boxed{
 \sum_iw_i\sum_T(Z_i(T)-c)(Z_i(T)-c-1)
 =\sum_T(\overline Z(T)-c)(\overline Z(T)-c-1)
  +\sum_T\operatorname {Var}_w Z_i(T).}
\tag{0.13}
\]

Thus choosing one whole resolution realizes none of the variance reduction
in (0.8): the entire gain reappears as the last, nonnegative term of
(0.13).  A packetwise owner-disjoint selection must create the required
negative cross-packet covariance.  Coarse profile orthogonality supplies
the correct fractional first moment but does not imply that selection law.

There are two useful sharpness statements.

* A fixed number (d) of asymptotically transverse matchings does not even
  clear one depth (q=x\sqrt m), (x>0): it leaves a positive-density
  coarse Hall deficit.  Hence the catalogue size must tend to infinity.
* Exact cancellation of the first matching-profile harmonic requires at
  least (2m-1) frames and is achieved by a one-factorization of
  (K_{2m}).  Exact cancellation through the (t)-edge incidence moments
  requires at least
  
  \[
  D_t=\prod_{j=0}^{t-1}(2m-(2j+1))
  \tag{0.14}
  \]
  
  frames.  In particular the first two requirements cost at least
  (2m-1) and ((2m-1)(2m-3)), respectively.  A one-factorization removes
  the linear/full-pair mode, but edge orthogonality alone does not control
  the nonlinear profile covariance.

The exact surviving statement is therefore: find an owner-disjoint
packet selection supported on a catalogue satisfying (0.8) whose selected
packet pair law retains the barycentric floor energy in (0.13), rather
than paying its variance term.  The complete-quartet no-go does not apply
to that finer problem.

## 1. Exact fixed-frame coarse profile

Fix a perfect matching (M).  A middle owner with (f) full (M)-edges
also has (f) empty edges and (m-2f) split edges, so its number is
(V_f) in (0.3).  A lower rank-((m-q)) target with (f) full edges has
(f+q) empty edges and (m-2f-q) split edges, giving (T_{f,q}).

Every literal lower depth-(q) face empties (q) split edges.  It therefore
preserves (f), independently of the internal recursive order.  There are
exactly (V_f) lower occurrences from owners of type (f).  The wreath
stabilizer (C_2\wr S_m) is transitive on the (T_{f,q}) targets of that
type.  Averaging inside this stabilizer consequently gives the load
(V_f/T_{f,q}), proving (0.2).  Complementation changes full lower edges
to empty upper edges and proves the upper assertion.

Summing (0.2) by types gives

\[
 \sum_T R_{M,q}^-(T)
 =\sum_fT_{f,q}\frac{V_f}{T_{f,q}}
 =\sum_fV_f=W,
\tag{1.1}
\]

which proves (0.4).  The same calculation with the square gives (0.5).

It is useful to regard (0.2) as a likelihood ratio.  Put

\[
 P_m(f)=\frac{V_f}{W},\qquad
 P_{m-q}(f)=\frac{T_{f,q}}{N_q}.
\tag{1.2}
\]

Then

\[
 R_{M,q}^-(T)=\lambda_q
 \frac{P_m(F_M(T))}{P_{m-q}(F_M(T))}.
\tag{1.3}
\]

Thus (sigma_{m,q}^2/lambda_q^2) is exactly the chi-square divergence
(\chi^2(P_m\Vert P_{m-q})).

## 2. Gaussian evaluation of the profile variance

Let (q=x\sqrt m+O(1)), with (x) in a fixed compact interval.  Write

\[
 f=\frac m4+\frac{z\sqrt m}{4}+O(1).
\tag{2.1}
\]

Uniform Stirling expansion of (0.3) gives

\[
 \frac{V_f}{W}=\frac4{\sqrt m}\phi(z)(1+o(1)),\qquad
 \frac{T_{f,q}}{N_q}
 =\frac4{\sqrt m}\phi(z+2x)(1+o(1)).
\tag{2.2}
\]

Also

\[
 \frac{N_q}{W}=e^{-x^2+o(1)}.
\tag{2.3}
\]

For clarity, (2.2) follows by applying
(\log(s+u)!=\log s!+u\log s+u^2/(2s)+O_A(m^{-1/2}))
to every factorial in (0.3), after the linear terms cancel.  The estimate
is uniform for bounded (z,x).  Outside a bounded (z)-window, strict
convexity of the same factorial entropy gives

\[
 P_{m-q}(f)\left(\frac{P_m(f)}{P_{m-q}(f)}\right)^2
 \le \frac{C_A}{\sqrt m}e^{-c_A(z-2x)^2},
\tag{2.4}
\]

after increasing (C_A); at the finitely many boundary values the left
side is interpreted only where (T_{f,q}>0).  This is obtained directly
from the second finite difference of (log(f!)), which lies between
(1/(f+1)) and (1/f).  Hence (2.4) supplies uniform integrability for
the first two likelihood-ratio moments.

Under the target law, (Y=z+2x\Rightarrow N(0,1)), while (1.3) and
(2.2)--(2.3) give

\[
 R_{M,q}^-(T)=e^{,2xY-x^2+o(1)}.
\tag{2.5}
\]

Therefore

\[
 \mathbb ER=e^{-x^2}\mathbb Ee^{2xY}=e^{x^2},
\qquad
 \mathbb ER^2=e^{-2x^2}\mathbb Ee^{4xY}=e^{6x^2}.
\tag{2.6}
\]

Equations (2.3), (2.4), and (2.6) prove (0.6), uniformly on compact
(x)-intervals.

## 3. Exact pair covariance of two frames

The covariance can be computed without an asymptotic approximation.  Let
(M,M') be perfect matchings, let (c=|M\cap M'|), and let the noncommon
components of (M\cup M') be alternating cycles of lengths
(2\ell_1,\ldots,2\ell_s).  Thus (ell_j\ge2) and
(sum_j\ell_j=m-c).

For a shared edge put

\[
 S(x;y,z)=1+2x+x^2yz.
\tag{3.1}
\]

Put

\[
 L_w(x)=\begin{pmatrix}1&x\\1&xw\end{pmatrix},\qquad
 C_\ell(x;y,z)=\operatorname {tr}
                 \left((L_y(x)L_z(x))^\ell\right).
\tag{3.2}
\]

Then the exact joint enumerator is

\[
 \boxed{
 G_{M,M'}(x;y,z)
 =S(x;y,z)^c\prod_{j=1}^sC_{\ell_j}(x;y,z).}
\tag{3.3}
\]

Indeed, on a shared edge the four endpoint subsets give (3.1).  On an
alternating cycle, a transition from bit (a) to bit (b) across an edge
of colour (w) has weight (x^bw^{ab}).  Multiplication around the
cycle and taking the trace counts every vertex once and every full edge in
the appropriate colour, proving (3.2)--(3.3).

Consequently the exact profile covariance is

\[
 \boxed{
 \Gamma_q(M,M')
 =\frac1{N_q}\sum_{f,g}
 [x^{m-q}y^fz^g]G_{M,M'}
 \bigl(a_{m,q}(f)-\lambda_q\bigr)
 \bigl(a_{m,q}(g)-\lambda_q\bigr),}
\tag{3.4}
\]

where (a_{m,q}(f)=V_f/T_{f,q}).  Formula (3.4) is the requested exact
joined-profile matrix.  It records the entire alternating-cycle type, not
only the number of common matching edges.

For a catalogue ({\cal M}=(M_1,\ldots,M_d)), (3.4) gives exactly

\[
 \frac1{N_q}
 \left\|\frac1d\sum_iR_{M_i,q}^--\lambda_q\mathbf1\right\|_2^2
 =\frac1{d^2}\mathbf1^T\Gamma_q({\cal M})\mathbf1.
\tag{3.5}
\]

Thus the exact simultaneous profile-orthogonality condition is

\[
 \sum_{q\le H}N_q\,
 \frac1{d^2}\mathbf1^T\Gamma_q({\cal M})\mathbf1=o(W).
\tag{3.6}
\]

No owner-codegree statement implies (3.6).

There is a simpler exact formula for the first nonconstant harmonic.  For
(k=m-q), put (p_j=(k)_j/(2m)_j).  Directly classifying an ordered pair
of matching edges as equal, meeting in one vertex, or disjoint gives

\[
 \operatorname {Cov}(F_M,F_{M'})
 =(p_2-2p_3+p_4)
 \left(c-\frac{m}{2m-1}\right).
\tag{3.7}
\]

To see the constant term, note that there are (c) equal pairs,
(2(m-c)) distinct pairs meeting in one vertex, and
(m^2-2m+c) disjoint pairs.  Their probabilities are (p_2,p_3,p_4).
The result is affine in (c); averaging (M') uniformly makes the
covariance zero and gives (mathbb E|M\cap M'|=m/(2m-1)), proving (3.7).
In particular

\[
 \operatorname {Corr}(F_M,F_{M'})
 =\frac{(2m-1)c-m}{2m(m-1)}.
\tag{3.8}
\]

Edge-disjoint frames therefore have correlation exactly
(-1/(2m-2)).

## 4. Sparse deterministic averaging

First choose (M_1,\ldots,M_d) independently and uniformly from all perfect
matchings.  For a fixed target (T), double counting pairs ((M,T))
shows

\[
 \Pr(F_M(T)=f)=\frac{T_{f,q}}{N_q}.
\tag{4.1}
\]

Hence (R_{M,q}(T)) has mean (lambda_q) and variance
(sigma_{m,q}^2), exactly.  Independence gives

\[
 \mathbb E\left(\overline R_q(T)-\lambda_q\right)^2
 =\frac{\sigma_{m,q}^2}{d}.
\tag{4.2}
\]

Summing (4.2) over targets, depths, and signs shows that the expectation
of the left side of (0.8) is one half of its displayed right side.  Some
deterministic catalogue satisfies the sharper energy-only bound with
\(2/d\) in place of \(4/d\).  The factor \(4/d\) in (0.8) allows the same
catalogue also to satisfy the Hall-deficit bound below.  The catalogue may
be taken simple:
sampling \(d\) matchings uniformly without replacement multiplies the
variance in (4.2) by

\[
 1-\frac{d-1}{(2m-1)!!-1}\le1,
\tag{4.2a}
\]

the usual finite-population correction.  Thus none of the bounds worsens.

Using (0.6) and (N_q/W=e^{-x^2+o(1)}),

\[
 \frac{N_q}{W}\sigma_{m,q}^2
 =e^{5x^2}-e^{x^2}+o(1).
\tag{4.3}
\]

The uniformity in Section 2 permits a Riemann sum over
(1\le q\le A\sqrt m), proving (0.9).

For every real (z) and (lambda>1),

\[
 (1-z)_+\le\frac{(z-\lambda)^2}{\lambda-1}.
\tag{4.4}
\]

Indeed the assertion is trivial for (z\ge1), while for (z<1),
((\lambda-z)^2/(\lambda-1)\ge\lambda-z\ge1-z).  Apply (4.4), take
the expectation over the random catalogue, and use (4.2).  Now

\[
 \frac{N_q}{W}\frac{\sigma_{m,q}^2}{\lambda_q-1}
 =\frac{e^{5x^2}-e^{x^2}}{e^{x^2}-1}+o(1),
\tag{4.5}
\]

uniformly including (x=0) by the limiting value (4).  A second Riemann
sum gives the corresponding expectation.  Normalize the energy and
deficit objectives by their respective expectations and add them.  The
expected sum is \(2\), so one simple catalogue has both objectives at
most twice their respective expectations.  This proves (0.9) and (0.11)
with the displayed constants \(4J_A,4K_A\).

This proves that (d=m) transverse frames already remove the fixed-profile
Hall cut by (o(W)) in total over all (q\le A\sqrt m).

## 5. Fixed catalogues and exact incidence orthogonality

### 5.1 A fixed transverse family cannot work

Fix (d) and suppose (M_{1,m},\ldots,M_{d,m}) satisfy

\[
 |M_{i,m}\cap M_{j,m}|=o(m)\qquad(i\ne j).
\tag{5.1}
\]

For a uniform target (T\in\binom{[2m]}{m-q}), with
(q=x\sqrt m+O(1)), (x>0), the vector of standardized full-edge counts
converges to (d) independent standard Gaussians.  Here is a direct
moment proof.  Expand every mixed factorial moment into choices of edges
from the union of the (d) matchings.  Configurations with pairwise
disjoint vertices give the Gaussian pairings.  A connected configuration
using (r\ge3) centered factors has only (O(m)) embeddings because the
union graph has maximum degree (d), whereas the normalization is
(m^{r/2}); its cumulant is therefore (o(1)).  Configurations using a
common edge have (o(m)) embeddings by (5.1).  The second cumulants are
given by (3.7)--(3.8) and tend to the identity.  All higher cumulants
vanish, proving the claim.  The same expansion is valid under fixed-rank
sampling because every union of (s) selected vertices has probability
((m-q)_s/(2m)_s).  Moment determinacy of the Gaussian completes the
argument.

Matching exposure gives a uniform subgaussian bound for the standardized
counts, so (2.5) is uniformly integrable.  It follows that

\[
 \frac1{N_q}\sum_T
 \left(1-\frac1d\sum_{i=1}^dR_{M_i,q}^-(T)\right)_+
 \longrightarrow
 \mathbb E\left(1-\frac1d\sum_{i=1}^d
 e^{2xZ_i-x^2}\right)_+>0,
\tag{5.2}
\]

where the (Z_i) are independent (N(0,1)).  Strict positivity follows
because all (Z_i) have a positive probability of lying below a fixed
sufficiently negative number.  Multiplication by
(N_q/W\to e^{-x^2}) gives a positive-density deficit relative to (W).
Thus (d\to\infty) is necessary even before owner conflicts for a
transverse catalogue.

For independent random catalogues, (4.2)--(4.3) show more: their expected
aggregate centered energy is

\[
 (2J_A+o(1))\frac{W\sqrt m}{d}.
\tag{5.3}
\]

Hence (d/\sqrt m\to\infty) is the sharp threshold for this particular
second-moment averaging mechanism.  This is not asserted as a universal
lower bound for specially designed catalogues.

### 5.2 Exact coordinate orthogonality

Let (a_M\in\{0,1\}^{\binom{[2m]}2}) be the edge-incidence vector of
(M), and put

\[
 u_M=a_M-\frac1{2m-1}\mathbf1.
\tag{5.4}
\]

The function (F_M-\mathbb EF_M) is a pure Johnson degree-two harmonic:
it is a coordinate polynomial of degree two, and its degree-one projection
vanishes because every coordinate has matching degree one.  Formula (3.7)
is equivalently

\[
 \langle F_M-\mathbb EF_M,F_{M'}-\mathbb EF_{M'}\rangle
 =C_{m,q}\langle u_M,u_{M'}\rangle
\tag{5.5}
\]

for a positive scalar (C_{m,q}).

For \(q>0\), the function
\(a_{m,q}(f)=V_f/T_{f,q}\) is strictly increasing in \(f\).  Hence

\[
 \operatorname {Cov}(a_{m,q}(F_M),F_M)>0
\tag{5.5a}
\]

by the identity
\(2\operatorname {Cov}(g(X),X)=
\mathbb E[(g(X)-g(X'))(X-X')]\) for independent \(X,X'\).
The degree-two projection of the profile is therefore a nonzero scalar
multiple of \(F_M-\mathbb EF_M\).  Cancelling the first profile harmonic
is exactly the edge-incidence balancing problem below.

For a uniform (d)-frame catalogue, let
(p=d^{-1}\sum_i a_{M_i}).  Since every frame has (m) edges,

\[
 \left\|p-\frac1{2m-1}\mathbf1\right\|_2^2
 \ge \frac md-\frac m{2m-1}\qquad(d\le2m-1).
\tag{5.6}
\]

Indeed (sum_ep_e^2\ge m/d), with equality precisely when the frames
are edge-disjoint, and the uniform vector has squared norm
(m/(2m-1)).  Thus exact cancellation of the degree-two profile harmonic
requires (d\ge2m-1).  A one-factorization of (K_{2m}) has exactly
(2m-1) perfect matchings and attains equality by covering every
coordinate edge once.

More generally, an exact (t)-incidence design of frames makes every
(t)-edge matching occur in the same positive number of catalogue frames.
It then makes

\[
 \frac1d\sum_M\binom{F_M(T)}j
\tag{5.7}
\]

independent of (T) for every (j\le t), and therefore cancels every
polynomial profile in (F_M) of degree at most (t).  Such a catalogue
must cover all (t)-edge matchings, so

\[
 d\binom mt\ge
 \frac{(2m)!}{(2m-2t)!2^tt!}.
\tag{5.8}
\]

Dividing by \(\binom mt\) gives exactly (0.14).  This proves the stated
minimal sizes.  Since the Gaussian profile (2.5) has nonzero Hermite
coefficients of every order when (x>0), a one-factorization cancels its
first matching-incidence mode but not, from edge balance alone, the higher
modes.  Their cancellation must be verified through the full Gram matrix
(3.4), not inferred from pairwise edge disjointness.

## 6. Why this is not the floor-covariance theorem

For a load vector (Z) and an integer (c), set

\[
 Q_c(Z)=\sum_T(Z(T)-c)(Z(T)-c-1).
\tag{6.1}
\]

Since (Q_c(Z)=\sum_TZ(T)^2-(2c+1)\sum_TZ(T)+N c(c+1)), taking a convex
combination (Z_i) and using

\[
 \sum_iw_iZ_i(T)^2=\overline Z(T)^2+
                    \operatorname {Var}_wZ_i(T)
\tag{6.2}
\]

proves (0.13).  This identity is exact and holds separately at every
signed depth.

The catalogue of Section 4 makes the coarse barycenter nearly constant,
so it removes the fixed-profile Gaussian cut before owner conflicts are
resolved.  If one subsequently chooses one whole frame resolution, the
variance term in (0.13) restores the lost energy exactly.  If instead one
chooses owner-disjoint packets from several resolutions, (0.13) no longer
forces that restoration; this is precisely why the arbitrary-packet escape
survives the complete-quartet component no-go.  But then the joint packet
selection probabilities must obey the negative overlap-covariance
inequality of
`MATH_THEOREM_MULTIFRAME_PACKET_HYPERGRAPH_AND_FLOOR_BALANCED_MATCHING_GATE_20260726.md`.
Nothing in (0.8), edge-disjointness, or an incidence design supplies those
joint probabilities.

The proved boundary is therefore exact:

1. (O(m)) exact transverse frames suffice to erase the coarse fixed-frame
   Gaussian Hall obstruction simultaneously through (H=A\sqrt m), at
   the fractional barycenter.
2. A bounded number of transverse frames cannot erase even one Gaussian
   depth.
3. Whole-resolution randomization cannot improve floor energy.
4. The remaining coefficient-one gate is an integral, owner-disjoint,
   cross-depth packet law whose target-overlap covariance realizes the
   barycentric reduction rather than the variance penalty in (0.13).

## 7. Audit of the two-sign cross-quartet transport

The theorem
MATH_THEOREM_TWO_SIGN_CROSS_QUARTET_PROFILE_TRANSPORT_20260726.md
is correct as a local owner-trade statement.  It strengthens the available
packet states but does not alter either the averaging identities above or
the floor-variance identity (0.13).

Let \(C_k,B_k,S_k\) denote, respectively, the cross, large-layer, and
small-layer shores in sector \(k\).  On the common owner set of a sector,

\[
 B_k-C_k=(0,u_k),\qquad S_k-C_k=(\ell_k,0),
\tag{7.1}
\]

in the direct sum
\[
 \left(\bigoplus_{q\le H}{\cal V}_{m-q}\right)
 \oplus
 \left(\bigoplus_{q\le H}{\cal V}_{m+q}\right).
\tag{7.2}
\]

Here \(\ell_k\) is a simultaneous all-\(q\) lower-profile effect and
\(u_k\) a simultaneous all-\(q\) upper-profile effect.  Equation (7.1)
holds at every depth, not merely at depth one: tensoring with the
coordinate-disjoint reservoir means that a window using the quartet
direction has exactly the displayed quartet intersection and union, while
a window not using it is unchanged.

The two effects cannot occur on the same owner in one sector.  This is not
just a missing construction.  On \(V_k^+\), a hypothetical shore having
the small-shore lower profile and the large-shore upper profile would need
\[
 (|(X\cap Y)\cap A|,\ |(X\cup Y)\cap A|)=(k,k+1).
\tag{7.3}
\]
But both endpoints have \(A\)-rank \(k\), whereas
\[
 |(X\cap Y)\cap A|+|(X\cup Y)\cap A|
 =|X\cap A|+|Y\cap A|=2k,
\tag{7.4}
\]
contradicting \(k+(k+1)=2k+1\).  The \(V_k^-\) case is identical, with
\(A,B\) interchanged.  Thus the local common-choice polytope in one
overlap sector is the triangle
\[
 \alpha\ge0,\qquad\beta\ge0,\qquad\alpha+\beta\le1,
\tag{7.5}
\]
where \(\alpha\) is the probability of \(B_k\) and \(\beta\) that of
\(S_k\).

For that three-state choice, with \(C_k\) as origin, the exact covariance
operator is
\[
\begin{aligned}
 \Sigma_k={}&
 \alpha(1-\alpha)u_ku_k^*
 +\beta(1-\beta)\ell_k\ell_k^*\\
 &-\alpha\beta(u_k\ell_k^*+\ell_ku_k^*).
\end{aligned}
\tag{7.6}
\]
The off-diagonal term is negative, but the floor energy is a sum of a
lower quadratic form and an upper quadratic form.  Its metric is block
diagonal in (7.2), so the off-diagonal term has zero trace against that
metric.  Hence a random common shore still pays exactly
\[
 \alpha(1-\alpha)\|u_k\|_+^2
 +\beta(1-\beta)\|\ell_k\|_-^2
\tag{7.7}
\]
of diagonal rounding variance.  Cross-sign anticorrelation is not the
within-sign negative target covariance required by the floor gate.

There is nevertheless a genuine deterministic simultaneous two-sign
state, because sectors are owner-disjoint.  Use the large shore in
sectors \(k=1,2\) and the small shore in sectors \(k=3,4\).  Relative to
the cross shore in every sector, this transports upper profile on
\[
 2\left[\binom41\binom40+\binom42\binom41\right]
 =2(4+24)=56
\tag{7.8}
\]
of the \(256\) local owners, and lower profile on
\[
 2\left[\binom43\binom42+\binom44\binom43\right]
 =2(24+4)=56.
\tag{7.9}
\]
Thus one exact common all-depth factor transports both signs on density
\[
 \boxed{\frac{56}{256}=\frac7{32}}
\tag{7.10}
\]
per sign, with no owner collision or seam loss.  The choice is
complement-symmetric: the large comparison in sector \(k\) is sent by
complementation to the small comparison in sector \(5-k\).

The constant \(7/32\) is the sharp equal-sign density available from these
three shores.  The upper-only sector \(k=1\) and lower-only sector \(k=4\)
each have mass \(8\).  The two common sectors \(k=2,3\) each have mass
\(48\), and on each such owner one may transport at most one sign by
(7.3)--(7.4).  Hence if \(U,L\) are the two transported owner masses,
\[
 U\le104,\qquad L\le104,\qquad U+L\le112.
\tag{7.11}
\]
It follows that \(\min(U,L)\le56\), attained by (7.8)--(7.9).

Accordingly, the advertised \(13/32\) is valid **separately** for either
sign, while the strongest single common two-sign shore has \(7/32\) for
each sign.  This removes a one-sign support obstruction and gives a useful
local preconditioner for the multiframe catalogue.  It does not itself
select owner-disjoint packets across different coordinate decompositions,
and (0.13) shows that averaging its integral global states still does not
prove the required floor-covariance theorem.
