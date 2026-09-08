# L1 missing shadows: the fixed-frame quotient hinge and the diffuse-orbit obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web
input is used.

## 0. Verdict

Use the audited exact constant-one target

\[
 \mathfrak H
 =\sum_{q\le H}\sum_{\epsilon\in\{-,+\}}
       \sum_{T\in\mathcal T_q^\epsilon}
              (1-L_q^\epsilon(T))_+=o(W),
\tag{0.1}
\]

or, equivalently,

\[
 \mathfrak X
 =\sum_{q,\epsilon}
 \left[\sum_T(L_q^\epsilon(T)-1)_+-(G-N_q)\right]=o(W),
\tag{0.2}
\]

since \(G>N_q\) at every protected positive depth.  This is strictly
weaker than CPCR.

Fix one Gaussian depth

\[
 q=A\sqrt m+O(1),\qquad A>0,qquad
 \lambda_A={G\over N_q}=e^{A^2+o(1)}.
\tag{0.3}
\]

There are two different conclusions.

### Fixed frame

For the full-capacity quotient coefficients \(c^F\), the weighted
certificate score satisfies

\[
 \log S_F(T)=2AZ-A^2+o_{\mathbb P}(1),qquad Z\Rightarrow N(0,1).
\tag{0.4}
\]

Hence its exact lower-hinge defect is

\[
 \boxed{
 \sum_T(1-S_F(T))_+
 =\bigl(\Delta_A+o(1)\bigr)N_q=\Omega_A(W),}
\tag{0.5}
\]

where

\[
 \Delta_A
 =\Phi(A/2)-e^{A^2}\Phi(-3A/2)>0.
\tag{0.6}
\]

If a proposed random packet/source realization has expected target load

\[
                         \mu(T)=S_F(T)+o_{L^1}(1),
\tag{0.7}
\]

then it has \(\Omega_A(W)\) expected missing targets, independently of
all correlations:

\[
 \boxed{
 \sum_T\Pr\{L(T)=0\}
 \ge\sum_T(1-\mu(T))_+
 \ge(\Delta_A-o(1))N_q.}
\tag{0.8}
\]

Thus the canonical uniform status-stratum realization of the quotient
flow is still linearly bad for the exact L1 target.

But (0.5) alone is **not** a universal fixed-frame missing-shadow
obstruction.  The score \(S_F\) is a sufficient uniform-capacity Hall
certificate, not an upper bound on every nonuniform matching or every
legal packet selection.  A different routing inside the same graph may
have target marginal \(\mu\ne S_F\).  Therefore the fixed-frame
lognormal theorem obstructs the quotient realization, not the entire
maximal fixed-frame graph.

### Moving-frame conjugacy

Normalized full conjugacy averaging removes (0.5) at the one-point level:
it makes every ordered-profile ratio constant and can give
\(\mu(T)\ge1\) with slack.  Nevertheless the natural product orbit
distribution is diffuse.  If

\[
 p_P(T)=\Pr\{T\in I_P^{\omega_P}\},qquad
 \mu(T)=\sum_Pp_P(T),qquad
 \eta_m=\max_{P,T}p_P(T)=o(1),
\tag{0.9}
\]

then

\[
 \boxed{
 \widetilde{\mathfrak H}_q
 =\sum_T\prod_P(1-p_P(T))
 \ge {N_q\over2}
       \exp\left[-{2\lambda_A\over1-\eta_m}\right]
 =\Omega_A(W).}
\tag{0.10}
\]

Full local orbit averaging has \(\eta_m=e^{-\Omega(m)}\) on the safe
ordered-profile core, so (0.10) applies.  Consequently the normalized
orbit point cannot be rounded to the desired L1 conclusion merely by
invoking the product-uncovered conditional-expectation theorem: its
starting product cost is already linear.

This is not an impossibility theorem for every correlated moving-frame
choice.  An exceptional integral choice may have much smaller cost than
the uniform product average.  What (0.10) proves is that first-moment
orbit flattening supplies no low-cost product point.  A positive L1
construction must polarize/homing the marginals or introduce a genuinely
correlated cross-parent resolution.

There is one exact correlated no-go.  If the averaging orbit consists
only of global relabelings of one complete state, then every orbit member
has exactly the same hole count.  Such averaging can make the mean load
constant but cannot improve missing shadows at all.

## 1. Exact L1 and repeat ledgers

Fix one signed depth and abbreviate \(N=N_q\).  Every integral legal state
has loads

\[
 L(T)\in\mathbb Z_{\ge0},\qquad \sum_TL(T)=G.
\tag{1.1}
\]

Put

\[
 M=\#\{T:L(T)=0\},qquad
 E=\sum_T(L(T)-1)_+.
\tag{1.2}
\]

Then

\[
 G=(N-M)+E,
\]

so, because \(G>N\),

\[
 \boxed{M=E-(G-N).}
\tag{1.3}
\]

Also, integrality gives

\[
 \boxed{M=\sum_T(1-L(T))_+.}
\tag{1.4}
\]

Equations (1.3)--(1.4) show that every missing-target lower bound below
is simultaneously a repeat-excess lower bound.  No covariance or
balanced-quota term is involved.

## 2. Two universal uncovered inequalities

Let \(L(T)\) be the load of a target under an arbitrary random legal
state and put

\[
                         \mu(T)=\mathbb EL(T).
\tag{2.1}
\]

### Lemma 2.1 (one-point lower hinge)

For every target,

\[
 \boxed{\Pr\{L(T)=0\}\ge(1-\mu(T))_+.}
\tag{2.2}
\]

#### Proof

Since \(L\) is a nonnegative integer,
\(\mathbf1_{\{L>0\}}\le L\).  Hence
\(\Pr\{L>0\}\le\mathbb EL=\mu\), which is (2.2). \(\square\)

This proof uses no independence.  Thus any random realization with the
fixed-frame quotient marginal (0.7) has the linear missing expectation
(0.8).

Now suppose one packet option is sampled independently for every packet.
Define

\[
 p_P(T)=\Pr\{T\in I_P^{\omega_P}\}.
\tag{2.3}
\]

Packet injectivity makes its contribution a Bernoulli variable, and
independence gives

\[
                         \Pr\{L(T)=0\}
 =\prod_P(1-p_P(T)).
\tag{2.4}
\]

### Lemma 2.2 (diffuse product lower bound)

If \(p_P(T)\le\eta<1\) for all \(P\), then

\[
 \boxed{
 \prod_P(1-p_P(T))
 \ge\exp\left[-{\mu(T)\over1-\eta}\right],
 \qquad \mu(T)=\sum_Pp_P(T).}
\tag{2.5}
\]

#### Proof

For \(0\le x\le\eta\),

\[
 -\log(1-x)=\int_0^x{dt\over1-t}
 \le{x\over1-\eta}.
\]

Sum over packets and exponentiate. \(\square\)

Since every packet emits one target per retained owner occurrence,

\[
 \sum_T\mu(T)=G=\lambda_A N_q.
\tag{2.6}
\]

At least \(N_q/2\) targets therefore satisfy
\(\mu(T)\le2\lambda_A\).  Lemma 2.2 proves (0.10).

The exact asymptotic under the stronger uniform relations

\[
 \max_{P,T}p_P(T)=o(1),qquad
 \mu(T)=\lambda_A+o(1)
\tag{2.7}
\]

is

\[
 \Pr\{L(T)=0\}=e^{-\lambda_A+o(1)}.
\tag{2.8}
\]

Thus perfect first marginals at constant Gaussian load naturally produce
a Poisson-sized hole set, not an \(o(W)\) hole set.

## 3. Re-evaluation of the fixed-frame lognormal score

For the full-capacity quotient lift in one fixed rank-matching array,
`MATH_THEOREM_WEIGHTED_QUOTIENT_LIFT_GAUSSIAN_OBSTRUCTION_20260726.md`
proves

\[
                         \log S_F=2AZ-A^2+o_{\mathbb P}(1)
\tag{3.1}
\]

on typical ordered profiles, with the required exponential uniform
integrability.  Therefore

\[
\begin{aligned}
 {1\over N_q}\sum_T(1-S_F(T))_+
 &\longrightarrow
 \int_{-\infty}^{A/2}(1-e^{2Az-A^2})\phi(z)\,dz\\
 &=\Phi(A/2)-e^{A^2}\Phi(-3A/2)=\Delta_A.
\end{aligned}
\tag{3.2}
\]

The canonical status-stratum realization distributes the reserved source
capacity uniformly over every exact target stratum.  Its incoming target
marginal is precisely \(S_F(T)\), up to the already recorded
\(o_{L^1}(1)\) unsafe/eligibility correction.  Lemma 2.1 then gives

\[
 \mathbb E M_q^\epsilon
 \ge(\Delta_A-o(1))N_q=\Omega_A(W).
\tag{3.3}
\]

By taking expectations in (1.3), the same statement is

\[
 \mathbb E\left[
    \sum_T(L(T)-1)_+-(G-N_q)
               \right]
 \ge(\Delta_A-o(1))N_q.
\tag{3.4}
\]

This is a genuine L1 obstruction to the canonical quotient
realization.

It must not be upgraded to a universal Hall cut.  The inequality used to
derive \(S_F\) is a status-biregular capacity certificate.  Failure of
that uniform certificate allows a nonuniform flow to favor some targets,
and different allocation components may repair one another on a raw
subset.  Neither (3.1) nor (3.2) supplies a dual vector satisfying the
max-dual inequality against every cross-profile routing.  Therefore the
maximal fixed-frame missing-shadow theorem remains open.

## 4. Full conjugacy averaging and source capacity

Let \(\Gamma\) be the product of the local half-coordinate permutation
groups.  It acts transitively on every exact ordered target profile.
For a fixed profile arc,

\[
 {1\over|\Gamma|}\sum_{g\in\Gamma}R_{\tau\kappa}^g(T)
 ={E_{\tau\kappa}\over|\tau|},
\tag{4.1}
\]

independently of \(T\in\tau\).  If the same normalized state law is used
for every target profile, the exact source time-sharing constraint is

\[
 \sum_\tau c_{\tau\kappa g}\le p_g,qquad
 \sum_gp_g=1.
\tag{4.2}
\]

Uniform \(p_g=|\Gamma|^{-1}\) is legal and proves the annealed pointwise
weighted inequality with \(e^{A^2+o(1)}\) slack.  Thus no source-profile
reuse occurs in the normalized orbit average.

However, (4.1) is only a one-point identity.  To apply the exact
product-uncovered theorem, conjugate options must be legal independent
packet-level choices.  If the conjugacy changes a rank matching shared by
many packets, it is instead one common frame variable and the packetwise
product theorem does not apply.  In the packet-local case, on a safe
ordered profile \(\tau\), orbit transitivity
gives

\[
 p_P(T)={|I_P\cap\tau|\over|\tau|}le {2^R\over|\tau|}.
\tag{4.3}
\]

For logarithmic macroblocks, every safe profile has

\[
                         |\tau|=e^{\Omega(m)},
\tag{4.4}
\]

whereas the admissible packet theorem has \(2^R=e^{o(m)}\), or in the
audited linear-scale variant \(R\le m/64\), still with an exponential
gap in (4.3).  Consequently

\[
                         \eta_m=\max_{P,T}p_P(T)=e^{-\Omega(m)}.
\tag{4.5}
\]

Equations (2.6), (4.5), and Lemma 2.2 prove the linear product-uncovered
bound (0.10).  The normalized orbit construction therefore moves enough
raw incidence to repair the fixed-frame lower hinge, but it spreads that
incidence among exponentially many packet options.  This is the wrong
geometry for the L1 target.

Thus the conjugacy proposal has an exact dichotomy.  A shared frame
conjugacy is correlated and cannot be fed into packetwise product
rounding; a packet-local conjugacy is eligible for product rounding but
obeys the diffuse lower bound (0.10).

## 5. What conditional-expectation rounding does here

For packetwise independent distributions,

\[
 \widetilde{\mathfrak H}(x)
 =\sum_{q,\epsilon,T}\prod_P(1-p_{P,q}^\epsilon(T))
\tag{5.1}
\]

is exactly the expected integral hole count.  Conditional expectation
shows that some one-state packet choice has cost at most (5.1).  It does
not lower (5.1) before rounding.

For the normalized orbit product point, a single Gaussian depth already
contributes \(\Omega_A(W)\) by (0.10).  Hence the conditional-expectation
theorem gives no \(o(W)\) conclusion from that point.  This is an explicit
failure of the proposed averaging-then-rounding proof.

This does not show that every state in the product support has linearly
many holes: an average may conceal an exceptional low-cost state.  Since
delta packet distributions are themselves product points, finding such a
state is exactly the original nonconvex product-uncovered problem, not a
consequence of orbit flattening.

There is one case in which orbit averaging provably cannot hide an
exceptional state.

### Proposition 5.1 (global-orbit invariance)

Suppose every state in the orbit is obtained from one complete legal
state \(\omega\) by a common target permutation \(g\):

\[
                         L_{g\omega}(T)=L_\omega(g^{-1}T).
\tag{5.2}
\]

Then

\[
 \boxed{
 \sum_T(1-L_{g\omega}(T))_+
 =\sum_T(1-L_\omega(T))_+}
\tag{5.3}
\]

for every \(g\).  The repeat excess is likewise invariant.

#### Proof

Equation (5.2) merely permutes the load coordinates.  Both displayed
functionals are symmetric sums of coordinatewise functions. \(\square\)

Thus a common global conjugacy orbit can flatten annealed marginals while
leaving the L1 cost of every state unchanged.  Any genuine improvement
must choose different conjugacy phases across packets or parents.  Once
that is allowed, the remaining problem is exactly a correlated
cross-parent resolution problem.

## 6. The required polarization scale

The diffuse lower bound also gives a necessary structural form for every
successful product construction.  Suppose at one fixed Gaussian depth

\[
                         \mu(T)\le\Lambda_A
\tag{6.1}
\]

outside \(o(N_q)\) targets, for a fixed constant \(\Lambda_A\).  If

\[
                         \max_Pp_P(T)\le1-\varepsilon,
\]

then the extreme-point bound for \(\prod_P(1-p_P(T))\) gives a positive
constant depending only on \(\Lambda_A,\varepsilon\).  Therefore

\[
                         \widetilde{\mathfrak H}_q=o(W)
\tag{6.2}
\]

forces, outside \(o(N_q)\) targets,

\[
 \boxed{\max_Pp_P(T)=1-o(1).}
\tag{6.3}
\]

Thus the L1 target needs an almost-deterministic home packet for almost
every target, or an equivalent correlated construction which creates the
same coverage without product independence.  Uniform conjugacy averaging
has \(\max_Pp_P(T)=e^{-\Omega(m)}\), the exact opposite regime.

## 7. Final boundary

Proved:

1. the fixed-frame quotient certificate has \(\Omega_A(W)\) lower-hinge
   defect;
2. every realization whose expected target load is the canonical
   quotient score has \(\Omega_A(W)\) expected holes and repeat excess;
3. this does not constitute a universal fixed-frame Hall cut;
4. normalized orbit averaging obeys shared source-profile capacity and
   repairs the one-point score;
5. its natural diffuse product implementation has
   \(\Omega_A(W)\) exact product-uncovered cost;
6. common global conjugacy preserves every state's L1 cost exactly; and
7. successful product marginals must polarize to near-home packets.

Open:

1. a nonuniform fixed-frame routing which bypasses the quotient score;
2. a polarized moving-frame packet distribution common to every depth
   and both signs; or
3. a correlated cross-parent construction with \(o(W)\) direct missing
   shadows.

The exact constant-one residual is therefore no longer quadratic
covariance.  It is the L1 homing/polarization problem for cross-parent
packet images.  Neither common-order syndrome nor any within-packet gate
is reopened.
