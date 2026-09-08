# TRP temporal propagation: exact pair-density tensorization and the fresh-round certificate barrier

Date: 2026-07-25

This note uses only the truncated carrier rotor. It audits and strengthens
the temporal claim following Theorem 6.1 of
DYNAMIC_TRP_ROUND_HALL_AND_FLAG_OBSTRUCTION_20260725.md.

## 0. Outcome

Put

\[
 M=m+H,\qquad
 \mathcal U=\binom{[2m]}M,\qquad
 n=|\mathcal U|=N_H,\qquad
 D=(m-Q)(H-Q).
\]

There is an exact temporal tensorization theorem. Suppose the law of the
current states of every two distinct carriers is at most \(R_t\) times the
product stationary law. Suppose also that, conditional on the *entire*
current configuration, a randomized simultaneous transversal has every
two-carrier transition probability at most \(\kappa_t\) times the product
uniform-rotor probability. Then

\[
 \boxed{R_{t+1}\leq \kappa_tR_t.}
 \tag{0.1}
\]

No independence between carriers, between rounds, or between the
transversal and the previous history is assumed.

The local-lemma construction admits an exact pairwise local law. If every
retained carrier has at least \(s\) of its \(D\) options, the option-conflict
graph has maximum degree \(\Delta\), and

\[
 8D\Delta\leq s^2,
 \tag{0.2}
\]

then conditioning independent uniform part choices on no conflict gives

\[
 \boxed{
 \kappa\leq
 \left(\frac Ds\right)^2
 \left(1-\frac2{s^2}\right)^{-2D\Delta}.}
 \tag{0.3}
\]

Thus an LLL witness can be sampled with controlled two-coordinate
marginals; an unspecified deterministic LLL witness would not imply
(0.3).

For the TRP rotor, define

\[
 \lambda_q=\frac{W}{N_q},
 \qquad
 \epsilon_m=
 \frac{1+2\sum_{q=1}^Q\lambda_q}{\lambda_H}.
 \tag{0.4}
\]

If the current pair density is \(R_t\), the expected average degree in the
full fresh conflict graph is at most \(R_tD\epsilon_m\). Consequently the
exact smallness condition furnished by this pair-density estimate is

\[
 \boxed{R_t\epsilon_m=o(1).}
 \tag{0.5}
\]

By (0.1), a sufficient condition is

\[
 \max_{t\leq M}\prod_{j<t}\kappa_j=o(1/\epsilon_m).
 \tag{0.6}
\]

The stronger condition \(\sum_{j<M}\log\kappa_j=o(1)\) preserves
\(R_t=1+o(1)\), but is not necessary for (0.5).

Two exact barriers prevent the existing fresh-round proof from being
iterated as written.

1. If \(B\) state-slots are discarded, one can lose \(B\) targets in each
   of the \(2Q+1\) controlled rows. Therefore \(B=o(W)\) is insufficient.
   Without a finer rowwise repair, coefficient one requires

   \[
    \boxed{B=o(W/Q).}
    \tag{0.7}
   \]

   This is a missing factor \(Q\) in the temporal sentence following the
   fresh-round theorem.

2. At the calibrated \(Q\),

   \[
    \boxed{
    \epsilon_m=\Theta(\lambda_Q/Q),\qquad
    Q\epsilon_m=\Theta(\lambda_Q)
    =(\log m)^{1+o(1)}\longrightarrow\infty.}
    \tag{0.8}
   \]

   The current Markov-pruning/symmetric-LLL estimate cannot certify an
   exceptional rate \(o(1/Q)\), even in one round. Its certified temporal
   pair cost also violates the weaker product condition (0.6) long before
   \(M\) rounds.

Finally, the one-step uniform rotor kernel has exact upper-density
contraction coefficient \(1\). Hence no hidden one-step mixing offsets the
factor \(\kappa_t\). A successful temporal argument must instead produce a
much more balanced law on whole transversals, prove a genuine multi-round
contraction, or use a weaker conflict-adapted norm with a separate closing
theorem.

This is a conditional invariant theorem and a rigorous no-go for the
present fresh-round pruning/LLL certificate. It is not a disproof of TRP.

## 1. Rotor states and pair density

For \(U\in\mathcal U\), a radius-\(Q\) state is

\[
 \omega=(L;z_1,\ldots,z_{2Q};R),
 \qquad |L|=m-Q,\qquad |R|=H-Q.
\]

For \(x\in L\) and \(y\in R\), the rotor transition is

\[
 (L;z_1,\ldots,z_{2Q};R)
 \longmapsto
 (L-x+y;x,z_1,\ldots,z_{2Q-1};R-y+z_{2Q}).
 \tag{1.1}
\]

Every state has indegree and outdegree \(D\). Let \(\Omega(U)\) be the
state space, let \(\pi_U\) be its uniform measure, and let \(P_U\) choose
one of the \(D\) outgoing transitions uniformly. Regularity gives

\[
 \pi_UP_U=\pi_U.
 \tag{1.2}
\]

Let \(Z_t=(Z_{U,t})_{U\in\mathcal U}\) be a random state configuration.
No product assumption is made. Define

\[
 R_t=
 \max_{U\ne V}
 \max_{\omega\in\Omega(U),\,\eta\in\Omega(V)}
 \frac{\Pr(Z_{U,t}=\omega,Z_{V,t}=\eta)}
 {\pi_U(\omega)\pi_V(\eta)}.
 \tag{1.3}
\]

Always \(R_t\geq1\), since every density in (1.3) has product-measure
average one. Independent uniform initial states have \(R_0=1\).

## 2. Exact propagation without independence

We first state the theorem for time-dependent reference measures.

### Theorem 2.1 (moving-reference pair-density propagation)

For every carrier \(U\) and time \(t\), let \(\mu_{U,t}\) be a probability
measure on a finite state space and let \(K_{U,t}\) be a Markov kernel such
that

\[
 \mu_{U,t}K_{U,t}=\mu_{U,t+1}.
 \tag{2.1}
\]

Suppose

\[
 \Pr(Z_{U,t}=u,Z_{V,t}=v)
 \leq R_t\mu_{U,t}(u)\mu_{V,t}(v)
 \tag{2.2}
\]

for every \(U\ne V,u,v\). A global randomized update may depend on the
entire configuration. Assume only that for every full configuration
\(\mathbf z\), every \(U\ne V\), and every successor pair \(u',v'\),

\[
 \Pr(Z_{U,t+1}=u',Z_{V,t+1}=v'\mid Z_t=\mathbf z)
 \leq
 \kappa_tK_{U,t}(z_U,u')K_{V,t}(z_V,v').
 \tag{2.3}
\]

Then

\[
 \boxed{R_{t+1}\leq\kappa_tR_t.}
 \tag{2.4}
\]

Consequently

\[
 R_t\leq R_0\prod_{j=0}^{t-1}\kappa_j.
 \tag{2.5}
\]

#### Proof

Fix \(U\ne V,u',v'\). Sum (2.3) over all coordinates of \(\mathbf z\)
except \(z_U,z_V\), and then use (2.2):

\[
\begin{aligned}
 &\Pr(Z_{U,t+1}=u',Z_{V,t+1}=v')\\
 &\quad\leq
 \kappa_tR_t
 \sum_{u,v}\mu_{U,t}(u)\mu_{V,t}(v)
 K_{U,t}(u,u')K_{V,t}(v,v')\\
 &\quad=
 \kappa_tR_t\mu_{U,t+1}(u')\mu_{V,t+1}(v'),
\end{aligned}
\]

where the last equality is (2.1). This proves (2.4); induction proves
(2.5). No conditional product law was used. \(\square\)

For the stationary rotor, take \(\mu_{U,t}=\pi_U\) and
\(K_{U,t}=P_U\). It is enough that for every full current configuration and
every two specified outgoing options \(e,f\),

\[
 \Pr(e_U=e,e_V=f\mid Z_t=\mathbf z)
 \leq\frac{\kappa_t}{D^2}.
 \tag{2.6}
\]

### 2.2 A contraction refinement

Let \(f\) be a two-carrier density relative to its product reference and
put

\[
 \rho(f)=\max(f-1).
\]

Suppose the reference pair kernel obeys

\[
 \rho(\mathcal P_tf)\leq\vartheta_t\rho(f),
 \qquad 0\leq\vartheta_t\leq1,
 \tag{2.7}
\]

for every probability density \(f\). Under (2.3), writing
\(\rho_t=R_t-1\), one has

\[
 \boxed{
 \rho_{t+1}
 \leq(\kappa_t-1)+\kappa_t\vartheta_t\rho_t.}
 \tag{2.8}
\]

Indeed the reference-propagated density is at most
\(1+\vartheta_t\rho_t\), and (2.3) multiplies it by at most \(\kappa_t\).
If \(\rho_0=0\), iteration gives

\[
 \rho_t\leq
 \sum_{j=0}^{t-1}(\kappa_j-1)
 \prod_{\ell=j+1}^{t-1}\kappa_\ell\vartheta_\ell.
 \tag{2.9}
\]

Thus a block contraction can replace the product restriction (0.6), but it
must be proved rather than inferred from regularity.

## 3. Pairwise local law for an LLL transversal

Let \(I\) be a set of carrier parts. Carrier \(i\) has an available option
set \(A_i\), where

\[
 s\leq |A_i|\leq D.
 \tag{3.1}
\]

Join two options from distinct parts when they conflict in at least one
controlled rank. Assume the resulting option-conflict graph has maximum
degree \(\Delta\).

Choose \(X_i\) independently and uniformly from \(A_i\). For every
conflict edge \(e=ab\), let \(B_e\) be the event that both endpoints are
chosen. Then

\[
 \Pr(B_e)\leq s^{-2}.
 \tag{3.2}
\]

Each \(B_e\) shares a carrier variable with at most \(2D\Delta\) other bad
events.

### Lemma 3.1 (conditional LLL local law)

Suppose \(x\in(0,1)\) satisfies

\[
 s^{-2}\leq x(1-x)^{2D\Delta}.
 \tag{3.3}
\]

Condition the product choice on no bad event. If \(E\) specifies the
chosen options in \(k\) distinct carrier parts, then

\[
 \Pr(E\mid\text{no conflict})
 \leq\Pr(E)(1-x)^{-kD\Delta}.
 \tag{3.4}
\]

#### Proof

The standard inductive LLL proof gives, for every bad event \(B\) and
every collection \(\mathcal S\) of other bad events,

\[
 \Pr\left(B\;\middle|\;
 \bigcap_{C\in\mathcal S}\overline C\right)\leq x.
 \tag{3.5}
\]

Indeed, split \(\mathcal S\) into neighbors and nonneighbors of \(B\), use
independence from the latter, and expose neighboring complements one at a
time; (3.3) closes the induction.

The event \(E\) is independent of every bad event not using one of its
\(k\) carrier variables. At most \(kD\Delta\) bad events use such a
variable. In a chain-rule exposure of the bad-event complements, (3.5)
shows that each of these complements costs at most a factor
\((1-x)^{-1}\), while all remaining complements cost no factor for \(E\).
This proves (3.4). \(\square\)

Take \(x=2/s^2\). If \(8D\Delta\leq s^2\), Bernoulli's inequality gives

\[
 \left(1-\frac2{s^2}\right)^{2D\Delta}
 \geq1-\frac{4D\Delta}{s^2}\geq\frac12,
\]

so (3.3) holds. With \(k=2\), relative to two independent uniform choices
among all \(D\) rotor transitions, (3.4) gives

\[
 \kappa\leq
 \left(\frac Ds\right)^2
 \left(1-\frac2{s^2}\right)^{-2D\Delta}.
 \tag{3.6}
\]

Moreover

\[
\begin{aligned}
 \log\kappa
 &\leq
 2\log\frac Ds+
 2D\Delta\log\frac1{1-2/s^2}\\
 &\leq
 2\log\frac Ds+\frac{4D\Delta}{s^2-2}.
\end{aligned}
\tag{3.7}
\]

If some carriers are declared exceptional, choose their transitions
independently and uniformly and charge their flags instead of imposing
conflict conditions on them. The \(k=1\) case of (3.4) gives cost at most
\(\sqrt\kappa\) for a retained-exceptional pair, and an
exceptional-exceptional pair has cost \(1\). Hence \(\kappa\) remains a
valid common pair bound.

## 4. Pair density and the fresh conflict count

Fix a controlled rank \(r=m\pm q\). Under a uniform state and uniform
outgoing option in a fixed carrier \(U\), the successor rank-\(r\) flag is
uniform in \(\binom Ur\).

For a fixed target \(S\in\binom{[2m]}r\), the expected number of option
vertices producing \(S\), summed over all carriers, is

\[
 \binom{2m-r}{M-r}\frac{D}{\binom Mr}
 =\frac{Dn}{N_q}.
 \tag{4.1}
\]

Therefore, under product-uniform carrier states, the expected number
\(C_r\) of cross-carrier conflict edges in this row satisfies

\[
 \mathbb EC_r\leq\frac{D^2n^2}{2N_q}.
 \tag{4.2}
\]

If the current two-carrier density is at most \(R\), every nonnegative
two-state statistic has expectation at most \(R\) times its product
expectation. Hence

\[
 \mathbb EC_r\leq R\frac{D^2n^2}{2N_q}.
 \tag{4.3}
\]

Sum the owner row once and the two rows at every depth
\(1\leq q\leq Q\). Since \(n/W=1/\lambda_H\),

\[
 \boxed{
 \frac{2\mathbb EC}{Dn}
 \leq RD\epsilon_m,\qquad
 \epsilon_m=
 \frac{1+2\sum_{q=1}^Q\lambda_q}{\lambda_H}.}
 \tag{4.4}
\]

This proves (0.5) as the condition under which this estimate certifies
vanishing normalized average option degree.

### Proposition 4.1 (pruning, exceptions, and pair cost)

Fix \(0<\alpha<1\) and \(\delta>0\). In a realized conflict graph, delete
every option of degree greater than \(\delta D\). Declare a carrier
exceptional if more than \(\alpha D\) of its options were deleted. Then

\[
 \boxed{
 \frac{\mathbb EB}{n}
 \leq\frac{R\epsilon_m}{\alpha\delta}.}
 \tag{4.5}
\]

Every retained carrier has at least \(s=(1-\alpha)D\) options, and the
remaining conflict graph has maximum degree at most \(\delta D\). If

\[
 8\delta\leq(1-\alpha)^2,
 \tag{4.6}
\]

then these carriers admit a random simultaneous transversal with pair
factor at most \(\exp\overline\eta(\alpha,\delta,D)\), where

\[
 \boxed{
 \overline\eta(\alpha,\delta,D)=
 2\log\frac1{1-\alpha}
 +\frac{4\delta}{(1-\alpha)^2-2/D^2}.}
 \tag{4.7}
\]

#### Proof

Let \(J\) be the number of deleted option vertices. Since the sum of all
option degrees is \(2C\),

\[
 J\delta D\leq2C.
\]

Equation (4.4) gives

\[
 \frac{\mathbb EJ}{Dn}\leq\frac{R\epsilon_m}{\delta}.
\]

Every exceptional carrier accounts for more than \(\alpha D\) deleted
vertices, proving (4.5). Condition (4.6) implies (0.2), and substitution of
\(s=(1-\alpha)D\), \(\Delta=\delta D\) into (3.7) proves (4.7).
\(\square\)

There is a quota-aware extension. Before degree pruning, delete every
option that hits an exhausted target in any controlled row. If the expected
number \(F_t\) of predeleted options obeys

\[
 \frac{\mathbb EF_t}{Dn}\leq\phi_t,
 \tag{4.8}
\]

then the same proof gives

\[
 \frac{\mathbb EB_t}{n}
 \leq
 \frac1{\alpha_t}
 \left(\phi_t+\frac{R_t\epsilon_m}{\delta_t}\right).
 \tag{4.9}
\]

The pair cost (4.7) is unchanged. Thus prior quota saturation is a
separate one-coordinate loss term; pair density alone does not control it.

Combining Theorem 2.1 and Proposition 4.1 gives, in the unsaturated case,

\[
 R_{t+1}\leq R_te^{\overline\eta_t},
 \qquad
 \frac{\mathbb EB_t}{n}
 \leq\frac{R_t\epsilon_m}{\alpha_t\delta_t}.
 \tag{4.10}
\]

This is one random construction over all rounds. It does not resample an
independent current configuration at each time.

## 5. Exact exceptional-slot accounting

Let \(T=Mn=MN_H\). For each controlled rank \(r\), fix a balanced integral
quota vector \(b_r(S)\) of total mass \(T\), as in the dynamic Hall
reduction. Suppose all retained state-slots respect these quotas. Let \(B\)
be the total number of exceptional state-slots over all rounds and
carriers, and discard every flag emitted at those slots.

At a fixed rank \(r\), the retained quota usage has total mass \(T-B\).
Thus

\[
 \sum_S\bigl(b_r(S)-u_r(S)\bigr)=B,
 \tag{5.1}
\]

where \(0\leq u_r(S)\leq b_r(S)\). Every positive-quota target absent from
the support contributes at least one to (5.1). Hence the support loss at
this rank, beyond the audited balanced-quota baseline, is at most \(B\).

There are \(2Q+1\) controlled rows. Therefore the total extra hard-band
deficit is at most

\[
 \boxed{(2Q+1)B.}
 \tag{5.2}
\]

The balanced-quota baseline is

\[
 O(WH^{3/2}/m)=o(W).
\]

Consequently a temporal exceptional scheme proves TRP only if

\[
 \boxed{B=o(W/Q),}
 \tag{5.3}
\]

unless a separate theorem shows that an exceptional slot damages
\(o(Q)\) rows on average. The assertion \(B=o(W)\) does not imply (5.3)
because \(Q\to\infty\).

Since \(T=W-o(W)\), condition (5.3) is equivalent to

\[
 \frac1M\sum_{t=0}^{M-1}\frac{B_t}{n}=o(1/Q).
 \tag{5.4}
\]

This factor \(Q\) is mandatory in a coefficient-one deduction from partial
round transversals.

## 6. Sharp size of the fresh conflict parameter

### Lemma 6.1

At the calibrated parameters,

\[
 \lambda_H=(1+o(1))m,
 \qquad
 \sum_{q=1}^Q\lambda_q
 =\Theta\left(\frac mQ\lambda_Q\right).
 \tag{6.1}
\]

Consequently

\[
 \boxed{
 \epsilon_m=\Theta(\lambda_Q/Q),\qquad
 Q\epsilon_m=\Theta(\lambda_Q)
 =(\log m)^{1+o(1)}.}
 \tag{6.2}
\]

#### Proof

The first-crossing definition gives \(\lambda_H\geq M\) and
\(\lambda_{H-1}<M\). Since

\[
 \frac{\lambda_H}{\lambda_{H-1}}
 =\frac{N_{H-1}}{N_H}
 =\frac{m+H}{m-H+1}=1+o(1),
\]

we have \(\lambda_H=(1+o(1))M=(1+o(1))m\).

Also

\[
 \lambda_q=\prod_{j=1}^q\frac{m+j}{m-j+1}.
\]

Taylor expansion, uniform for \(q\leq Q=o(m^{2/3})\), gives

\[
 \log\lambda_q
 =\frac{q^2}{m}
 +O\left(\frac qm+\frac{q^3}{m^2}\right)
 =\frac{q^2}{m}+o(1).
 \tag{6.3}
\]

For \(0\leq u\leq Q\),

\[
 \frac{\lambda_{Q-u}}{\lambda_Q}
 =\exp\left(-\frac{2Qu-u^2}{m}+o(1)\right).
 \tag{6.4}
\]

The terms with \(0\leq u\leq c\,m/Q\), for any fixed small \(c>0\), are
a fixed positive fraction of \(\lambda_Q\), proving the lower bound in
(6.1). For \(Q/2\leq q\leq Q\), split into intervals of length
\(\lfloor m/Q\rfloor\); (6.4) gives a geometrically decreasing upper bound
of order \((m/Q)\lambda_Q\). The remaining terms satisfy

\[
 \sum_{q<Q/2}\lambda_q
 \leq Q\exp(Q^2/(4m)+o(1))
 =o\left(\frac mQ\lambda_Q\right).
\]

Finally

\[
 \frac{Q^2}{m}
 =\log\log m+\gamma(m)+o(1)
\]

implies

\[
 \lambda_Q=\exp(Q^2/m+o(1))=(\log m)^{1+o(1)}.
\]

Substitution into (0.4) proves (6.2). \(\square\)

## 7. What the present certificate cannot propagate

First consider exceptional-slot cost. Under (4.6),

\[
 \alpha_t\delta_t
 \leq\frac{\alpha_t(1-\alpha_t)^2}{8}
 \leq\frac1{54},
 \tag{7.1}
\]

with equality in the second inequality at \(\alpha_t=1/3\). Thus the
smallest numerical upper bound furnished by (4.5) is only of order
\(R_t\epsilon_m\). To certify (5.4), its right side would have to be
\(o(1/Q)\), but

\[
 Q R_t\epsilon_m\geq Q\epsilon_m
 =\Theta(\lambda_Q)\to\infty.
 \tag{7.2}
\]

Therefore no choice of \(\alpha_t,\delta_t\) makes the present pruning/LLL
bound strong enough for the coefficient-one exception ledger. This is a
failure of the certificate, not a lower bound on the actual number of
exceptional carriers.

There is also a temporal pair-density barrier even if one temporarily asks
only for average exceptional fraction \(o(1)\). Numerically, (4.7) obeys

\[
 \overline\eta_t
 \geq2\alpha_t+4\delta_t
 \geq4\sqrt{2\alpha_t\delta_t}.
 \tag{7.3}
\]

For the bounds (4.5) to certify average exceptional fraction \(o(1)\), one
would need

\[
 \epsilon_m\sum_{t<M}\frac1{\alpha_t\delta_t}=o(M).
 \tag{7.4}
\]

Put \(p_t=\alpha_t\delta_t\). By Cauchy--Schwarz,

\[
 \sum_{t<M}\frac1{\sqrt{p_t}}
 \leq\sqrt{M\sum_{t<M}\frac1{p_t}},
\]

and

\[
 M^2
 \leq
 \left(\sum_{t<M}\sqrt{p_t}\right)
 \left(\sum_{t<M}\frac1{\sqrt{p_t}}\right).
\]

Under (7.4),

\[
 \sum_{t<M}\sqrt{p_t}\gg M\sqrt{\epsilon_m}.
\]

Hence

\[
 \sum_{t<M}\overline\eta_t
 \gg M\sqrt{\epsilon_m}.
 \tag{7.5}
\]

At the calibrated scale,

\[
 M\sqrt{\epsilon_m}\gg\log(1/\epsilon_m).
 \tag{7.6}
\]

The certified product \(\prod_{t<M}e^{\overline\eta_t}\) therefore exceeds
the admissible \(o(1/\epsilon_m)\) scale from (0.6) by an exponential
margin. The actual coefficient-one requirement (5.4) is stronger still.

Thus the existing average-conflict estimate, Markov pruning, and symmetric
LLL cannot simultaneously certify enough retained flags and enough
temporal pair pseudorandomness. This conclusion concerns that proof
package; it does not exclude a better balanced distribution on the same
legal transversals.

## 8. Exact absence of one-step contraction

Let

\[
 F=|\Omega(U)|=\frac{M!}{(m-Q)!(H-Q)!}.
\]

For the uniform rotor kernel \(P\), define

\[
 \vartheta(P)=
 \sup_{\substack{f\geq0,\ \pi(f)=1\\ f\ne1}}
 \frac{\max(P^*f-1)}{\max(f-1)},
 \tag{8.1}
\]

where \(P^*\) propagates densities relative to \(\pi\). Since \(P^*f\) is
an average of \(f\), always \(\vartheta(P)\leq1\).

### Proposition 8.1

For the TRP rotor,

\[
 \boxed{
 \vartheta(P)=1,\qquad
 \vartheta(P_U\otimes P_V)=1.}
 \tag{8.2}
\]

#### Proof

Fix a target state \(\omega'\). Its predecessor set \(A\) has exactly
\(D\) states. Moreover

\[
 F=(M)_{2Q}\binom{M-2Q}{m-Q}\geq M(M-1),
\]

whereas

\[
 2D=2(m-Q)(H-Q)
 \leq\frac{(M-2Q)^2}{2}<M(M-1).
\]

Thus \(a:=D/F<1/2\). For sufficiently small \(c>0\), define

\[
 f(\omega)=
 \begin{cases}
 1+c,&\omega\in A,\\
 1-c\,a/(1-a),&\omega\notin A.
 \end{cases}
 \tag{8.3}
\]

Then \(f\geq0\), \(\pi(f)=1\), and \(\max(f-1)=c\). The reverse transition
law into \(\omega'\) is uniform on \(A\), so

\[
 (P^*f)(\omega')=1+c.
\]

Hence \(\vartheta(P)\geq1\), proving equality. The same construction on a
product predecessor set, of size \(D^2\) inside \(F^2\), proves the product
statement. \(\square\)

The queue shift in (1.1) explains this equality: one rotor step retains a
rigid predecessor fibre rather than averaging over the full state space.
Any contraction used in (2.9) must therefore be genuinely multi-step or
measured in a weaker, conflict-adapted norm.

## 9. Precise proved/conditional boundary

A temporal pair-pseudorandomness proof of TRP would follow from the
following data.

1. At every round, after options forbidden by the balanced quota ledger
   are removed, a random simultaneous-transversal kernel satisfies (2.3).
2. Its prefix products obey

   \[
    \max_{t\leq M}\prod_{j<t}\kappa_j=o(1/\epsilon_m),
   \]

   or a proved block contraction makes the right side of (2.9)
   \(o(1/\epsilon_m)\) at the level needed for (0.5).
3. The total charged state-slot count is \(o(W/Q)\), or a sharper rowwise
   charging theorem replaces (5.2).
4. The separate quota-option loss \(\phi_t\) in (4.9) is controlled at the
   same charged scale.

Under these hypotheses, Theorem 2.1 preserves the pair bound needed to
repeat the fresh conflict estimate. The balanced-quota argument and (5.2)
then give TRP, after which the audited outer reservoir gives the
coefficient-one word ledger.

The current fresh-round proof does not supply these hypotheses. Its
exception estimate misses the necessary scale by
\((\log m)^{1+o(1)}\), its certified pair distortion violates the minimal
product condition (0.6), and its one-step reference kernel has no strict
upper-density contraction. The next exact statement must therefore concern
a balanced law on whole transversals or a nontrivial multi-round
negative-dependence mechanism; pairwise fresh sparsity alone is not yet a
temporal invariant.
