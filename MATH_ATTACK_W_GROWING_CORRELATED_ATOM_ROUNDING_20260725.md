# Lane W: integral rounding of growing correlated necklace atoms

## 0. Outcome

This report proves a genuine integral low-collision rounding theorem for
growing physical atoms and a matching no-go theorem for the canonical
full-reservoir product architecture.

The positive theorem is parity-sharp.  Suppose physical two-state atoms
have fixed, pairwise-disjoint middle-owner cells, preserve their complete
type ledgers, and hence preserve exact middle ownership at every global
sign corner.  For target class \(j\), let

\[
 T_j=c_jN_j+\rho_j,\qquad 0\leq\rho_j<N_j,
\]

and let \(\Delta_j\) be its balanced second-factorial excess.  If \(B_w\)
is the coordinatewise optimal pair-sum floor of the doubled two-state
system and \(z_i\) is the incidence difference of atom \(i\), then one
common integral signing satisfies

\[
 \boxed{
 \sum_jw_j\Delta_j
 \leq \frac{B_w}{2}+\frac18\sum_i\|z_i\|_w^2.
 }                                                          \tag{0.1}
\]

No negative-dependence hypothesis is used.  Every corner is already
physical and integral.

For the audited aligned two-necklace diamonds,

\[
 \|z_i\|_w^2=16\sum_{q=2}^{d_i}w_q.                         \tag{0.2}
\]

With the SCD radius law, paired downward type rounding, \(R=2\ell\), and
\(w_q\leq1\), the complete rounding action is at most

\[
 \boxed{
 \frac18\sum_i\|z_i\|_w^2
 \leq \frac WR\sum_{q=2}^hw_q\rho_q
 \leq
 \left(\frac{\sqrt\pi}{4}+o(1)\right)
 \frac{W\sqrt m}{\ell}=o(W).
 }                                                          \tag{0.3}
\]

Thus an aligned physical diamond atomization with \(B_w=o(W)\) rounds to
an integral exact-owner family with \(o(W)\) balanced factorial excess.
For the direct even necklace construction, the resulting slot deficit and
central-band holes are \(o(W)\); physical linearization, singleton repair,
and the audited outer-tail word then give a literal contiguous-OR word of
length \(W+o(W)\).

The unproved input is now sharply localized: construct an almost-spanning
aligned atomization with \(B_w=o(W)\).  The existing diamonds have zero
depth-one action, so the first shadow must already be good.

The negative theorem closes a different tempting route.  Independent
random packets whose union has exact middle ownership almost surely must
own deterministic, disjoint middle cells.  The positive-marginal co-block
graph of the full physical necklace reservoir is connected.  Therefore a
product law representing the canonical full-reservoir fractional point has
only one nonempty global packet.  There is no decomposition into
independent subglobal growing atoms.  Even after restricting support enough
to disconnect the owner graph, diffuse independent packets pay
\(\Omega(W\sqrt m)\) pair-factorial collision in the direct even model.

This is not a complete proof of \(\nu(k)\leq(1+o(1))W(k)\).  It is a proved
integral theorem which composes quantitatively into constant one under one
explicit physical atomization hypothesis, together with a rigorous
ownership no-go which definitively closes full-reservoir product/nibble
rounding.

Throughout the main direct-even application,

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 \rho_q=\frac{N_q}{W}.
\]

No computational or finite search is used.

## 1. Balanced second-factorial excess

Let \(\mathcal U\) be a target class of size \(N\).  Every allowed integral
configuration has fixed total load

\[
 T=cN+\rho,\qquad c=\left\lfloor\frac TN\right\rfloor,
 \qquad 0\leq\rho<N,\qquad \theta=\rho/N.                   \tag{1.1}
\]

For an integer \(x\geq0\), put

\[
 e_c(x)=\frac{(x-c)(x-c-1)}2.                               \tag{1.2}
\]

For a load vector \(\mu\), define

\[
 \Delta_2(\mu)=\sum_{S\in\mathcal U}e_c(\mu(S)).             \tag{1.3}
\]

### Lemma 1.1 (exact balanced-floor identity)

One has

\[
 \Delta_2(\mu)
 =
 \sum_S\binom{\mu(S)}2
 -(N-\rho)\binom c2-\rho\binom{c+1}2.                       \tag{1.4}
\]

Equivalently,

\[
 \boxed{
 2\Delta_2(\mu)
 =
 \|\mu-(c+\theta)\mathbf1\|_2^2
 -N\theta(1-\theta).
 }                                                          \tag{1.5}
\]

In particular, \(\Delta_2(\mu)\geq0\), with equality exactly when every
load lies in \(\{c,c+1\}\).

#### Proof

Expanding (1.2) and using \(\sum_S\mu(S)=cN+\rho\) gives

\[
 \begin{aligned}
 \sum_Se_c(\mu(S))
 &=
 \sum_S\binom{\mu(S)}2
 -c(cN+\rho)+N\binom{c+1}2\\
 &=
 \sum_S\binom{\mu(S)}2
 -N\binom c2-\rho c,
 \end{aligned}
\]

which is (1.4).  Expanding the squared norm gives (1.5).  An
integer-valued vector of fixed total has minimum square sum at the
floor/ceiling vector, proving the last assertion.  \(\square\)

The normalized higher factorial hierarchy is unnecessary here: its
quadratic member is the smallest normalized certificate.  Thus all
factorial statements below use \(r=2\).

### Lemma 1.2 (hole conversion)

Let \(M(\mu)=|\{S:\mu(S)=0\}|\).

If \(c\geq1\), then

\[
 \boxed{
 M(\mu)\binom{c+1}{2}\leq\Delta_2(\mu).
 }                                                          \tag{1.6}
\]

If \(c=0\), so \(T<N\), then

\[
 \boxed{
 M(\mu)\leq (N-T)+\Delta_2(\mu).
 }                                                          \tag{1.7}
\]

#### Proof

For (1.6), fill one hole successively from load \(0\) to load \(c\).
Before each transfer, some donor has load at least \(c+1\); otherwise the
total load would be below \(cN\).  Moving one unit from a donor of load
\(y\geq c+1\) to a receiver of load \(t<c\) decreases the second
factorial moment by

\[
 (y-1)-t\geq c-t.
\]

The \(c\) transfers therefore decrease it by at least

\[
 \sum_{t=0}^{c-1}(c-t)=\binom{c+1}{2}.
\]

Repeat for all original holes and then balance the remaining vector.  Its
final factorial moment is the balanced minimum in (1.4), proving (1.6).

For \(c=0\), \(\Delta_2=\sum_S\binom{\mu(S)}2\).  The exact coverage
identity is

\[
 M=N-T+\sum_S(\mu(S)-1)_+.
\]

Since \((x-1)_+\leq\binom x2\) for every integer \(x\geq0\), (1.7)
follows.  \(\square\)

For several classes \(j\), choose the literal-repair weights

\[
 w_j=
 \begin{cases}
 1,&c_j=0,\\[1mm]
 \binom{c_j+1}{2}^{-1},&c_j\geq1.
 \end{cases}                                               \tag{1.8}
\]

Then Lemma 1.2 gives

\[
 \boxed{
 \sum_jM_j
 \leq
 \sum_{j:c_j=0}(N_j-T_j)+\sum_jw_j\Delta_j.
 }                                                          \tag{1.9}
\]

## 2. Exact covariance and quadratic-variation ledger

Suppose random packets \(i=1,\ldots,s\) contribute integer target loads
\(X_{i,S}\geq0\), and put

\[
 C_S=\sum_iX_{i,S},\qquad
 \ell_S=\mathbb EC_S,\qquad
 \lambda=T/N=c+\theta.
\]

Every outcome is assumed to have total class load \(T\).

### Theorem 2.1 (arbitrary packet covariance identity)

For an arbitrary joint packet law,

\[
 \boxed{
 \begin{aligned}
 \mathbb E\Delta_2(C)
 =\frac12\bigg[
 &\sum_{i,S}\operatorname{Var}X_{i,S}
 +2\sum_{i<i',S}\operatorname{Cov}(X_{i,S},X_{i',S})\\
 &+\sum_S(\ell_S-\lambda)^2
 -N\theta(1-\theta)
 \bigg].
 \end{aligned}
 }                                                          \tag{2.1}
\]

In particular, if the packets are independent and the target marginals
are uniform,

\[
 \boxed{
 \mathbb E\Delta_2(C)
 =\frac12\left[
 \sum_{i,S}\operatorname{Var}X_{i,S}
 -N\theta(1-\theta)
 \right].
 }                                                          \tag{2.2}
\]

#### Proof

For one integer random variable \(Z\) of mean \(a\),

\[
 \mathbb E\binom Z2=\frac12(\operatorname{Var}Z+a^2-a).
\]

Sum over targets and subtract the balanced floor in (1.4).  Because
\(\sum_S\ell_S=T=N\lambda\),

\[
 \sum_S\ell_S^2=N\lambda^2+\sum_S(\ell_S-\lambda)^2.
\]

The scalar residual between \(N(\lambda^2-\lambda)/2\) and the balanced
floor is \(-N\theta(1-\theta)/2\).  Expanding
\(\operatorname{Var}C_S\) into packet variances and covariances proves
(2.1); independence and uniformity give (2.2).  \(\square\)

The same identity has a sequential form.  For a filtration
\(\mathcal F_0\subset\cdots\subset\mathcal F_r\) with
\(\mathcal F_0\) trivial (modulo null sets) and \(C\) measurable with
respect to \(\mathcal F_r\),

\[
 \sum_S\operatorname{Var}C_S
 =
 \sum_{a=1}^r
 \mathbb E\left\|
 \mathbb E[C\mid\mathcal F_a]
 -\mathbb E[C\mid\mathcal F_{a-1}]
 \right\|_2^2.                                             \tag{2.3}
\]

Thus a successful globally dependent construction must prove near-minimal
integer quadratic variation.  Calling its packets “correlated” internally
does not remove this ledger.

### Corollary 2.2 (exact product localization)

Assume the packets are independent.  At one target \(S\), write

\[
 \mathbb EX_{i,S}=a_i+r_i,\qquad
 a_i\in\mathbb Z_{\geq0},\qquad 0\leq r_i<1,
\]

and \(\sum_i(a_i+r_i)=c+\theta\).  Then

\[
 \begin{aligned}
 2\left(
 \mathbb E\binom{C_S}{2}
 -\binom c2-c\theta
 \right)
 &=
 \sum_i\left(\operatorname{Var}X_{i,S}-r_i(1-r_i)\right)\\
 &\quad+
 \left(\sum_ir_i(1-r_i)-\theta(1-\theta)\right).
                                                               \tag{2.4}
 \end{aligned}
\]

Both terms on the right are nonnegative.  Equality holds if and only if:

1. every \(X_{i,S}\) is supported on
   \(\{a_i,a_i+1\}\); and
2. at most one \(r_i\) lies strictly between zero and one.

Thus floor-sharp product rounding is targetwise deterministic except for
one adjacent two-point variable carrying the whole fractional remainder.

#### Proof

An integer random variable of mean \(a+r\) has

\[
 \operatorname{Var}X-r(1-r)
 =\mathbb E[(X-a)(X-a-1)]\geq0,
\]

with equality exactly on \(\{a,a+1\}\).

For the second term, take independent Bernoulli variables of means \(r_i\).
Their sum is integer-valued with mean whose fractional part is \(\theta\).
Its variance \(\sum_ir_i(1-r_i)\) is at least the universal integer
variance floor \(\theta(1-\theta)\).  Equality forces the Bernoulli sum to
be supported on two adjacent integers.  Under independence this is
equivalent to at most one nondegenerate Bernoulli variable.  Substitution
in (2.2) proves (2.4).  \(\square\)

Quantitatively,

\[
 \operatorname{Var}X-r(1-r)
 \geq2\Pr\{X\notin\{a,a+1\}\}.                              \tag{2.5}
\]
Thus small product excess forces quantitative localization of every atom
law onto its adjacent-integer support, not merely a small average variance.

### Corollary 2.3 (diffuse product packets have macroscopic excess)

Assume uniform target marginals and

\[
 \max_{i,S}\mathbb EX_{i,S}\leq\varepsilon\leq1.
\]

Then

\[
 \boxed{
 \mathbb E\Delta_2
 \geq
 \frac N2\left[(1-\varepsilon)\lambda-\theta(1-\theta)\right].
 }                                                          \tag{2.6}
\]

#### Proof

For a nonnegative integer variable of mean \(\alpha\leq1\),

\[
 \operatorname{Var}X
 =\mathbb EX^2-\alpha^2
 \geq\alpha-\alpha^2
 \geq(1-\varepsilon)\alpha.
\]

Sum over packets and targets in (2.2).  \(\square\)

On every fixed Gaussian window, \(\lambda\geq1\) and
\(\lambda=O_A(1)\).  For \(\varepsilon=o(1)\), (2.6) is
\((1/2-o_A(1))N\) per target class.  After the bounded factorial weights
are applied and \(q\leq A\sqrt m\) is summed, the obstruction is
\(\Omega_A(W\sqrt m)\), not \(o(W)\).

In the direct even necklace fractional design, every certified target has
mean one and the certified universe has

\[
 V_h=(\sqrt\pi+o(1))W\sqrt m.                               \tag{2.7}
\]

For packet-simple incidences \(X_{i,S}\in\{0,1\}\), put
\(p_{i,S}=\Pr(X_{i,S}=1)\) and \(p_*(S)=\max_i p_{i,S}\).
Then

\[
 \boxed{
 \mathbb E\sum_S\binom{C_S}{2}
 =\frac12\sum_S\left(1-\sum_ip_{i,S}^2\right)
 \geq\frac12\sum_S(1-p_*(S)).
 }                                                          \tag{2.8}
\]

Diffuse \(p_*(S)=o(1)\) therefore gives

\[
 \left(\frac{\sqrt\pi}{2}+o(1)\right)W\sqrt m              \tag{2.9}
\]

expected pair collision.  Conversely, an \(o(W)\)
**expected-potential** product-law certificate, or a conditional-expectation
derandomization whose guarantee is this expectation, requires

\[
 \sum_S(1-p_*(S))=o(W).                                    \tag{2.10}
\]

Almost every target must already be assigned to one packet with aggregate
error \(o(1/\sqrt m)\).  This is essentially the near-perfect physical
design that the rounding was meant to construct.

## 3. Exact middle ownership forbids a full-support product atomization

The preceding variance obstruction concerns nonmiddle targets.  Exact
middle ownership itself yields a stronger structural theorem.

Let \(\mathcal B\) be any family of physical necklace blocks with nonempty
simple middle supports

\[
 M(B)\subseteq\binom{[2m]}m.
\]

Random packets may output finite multisets of blocks.

### Theorem 3.1 (product exact-ownership rigidity)

Let \(\Xi_1,\ldots,\Xi_s\) be independent random finite block multisets and
put \(\mathcal F=\biguplus_i\Xi_i\).  Suppose that, almost surely,

\[
 \sum_i\sum_{B\in\Xi_i}\mathbf1_{\{X\in M(B)\}}=1
 \quad\text{for every }X\in\binom{[2m]}m.                   \tag{3.1}
\]

Then there is a deterministic partition

\[
 \binom{[2m]}m=V_1\sqcup\cdots\sqcup V_s                  \tag{3.2}
\]

such that packet \(i\) covers every \(X\in V_i\) exactly once and every
\(X\notin V_i\) zero times, almost surely.

Moreover, if a block \(B\) occurs in packet \(i\) with positive
probability, then

\[
 M(B)\subseteq V_i.                                        \tag{3.3}
\]

#### Proof

For fixed \(X\), define the nonnegative integer variable

\[
 Y_{i,X}=\sum_{B\in\Xi_i}\mathbf1_{\{X\in M(B)\}}.
\]

The variables \(Y_{i,X}\) are independent over \(i\), and their sum is one
almost surely.  Nonnegativity and exactness give
\(0\leq Y_{i,X}\leq1\) almost surely, so they are automatically
square-integrable.  Therefore

\[
 0=\operatorname{Var}\left(\sum_iY_{i,X}\right)
  =\sum_i\operatorname{Var}Y_{i,X}.
\]

Each \(Y_{i,X}\) is deterministic.  Its value is a nonnegative integer,
and the values sum to one.  There is thus one unique owner packet \(i(X)\).
Put \(X\in V_{i(X)}\).

If \(B\) occurs in \(\Xi_i\) with positive probability and \(X\in M(B)\),
then \(Y_{i,X}\geq1\) on that event.  Its deterministic value is therefore
one, so \(X\in V_i\).  This proves (3.3).  Multisets cause no loophole:
exactness prevents a positive-probability packet outcome from covering the
same middle vertex twice.  \(\square\)

Define the positive-support co-block graph on the middle layer by joining
\(X,Y\) whenever some positive-marginal block contains both.

### Corollary 3.2 (support-component classification)

Every connected component of the positive-support co-block graph lies in
one cell \(V_i\).  If that graph is connected, exactly one packet is
nonempty on the middle layer.

This classifies every possible independent atomization: its atom cells
must coarsen the positive-support components.

### Lemma 3.3 (the full physical reservoir is connected)

For the full mixed-pair \(2\ell\)-necklace reservoir, the co-block graph
contains the Johnson graph \(J(2m,m)\), and is therefore connected.

#### Proof

Take Johnson neighbours

\[
 X=S\cup\{a\},\qquad Y=S\cup\{b\}.
\]

Choose a coordinate perfect matching containing the active pair
\(\{a,b\}\).  Choose \(\ell-1\) further cross pairs between distinct
elements of \(S\) and distinct elements outside \(X\cup Y\), and pair all
remaining elements of \(X\) bijectively with all remaining elements of
\([2m]\setminus X\).  Thus every matching pair is split at \(X\).

Activate \(\{a,b\}\) and the chosen \(\ell-1\) cross pairs, and put
\(\{a,b\}\) first in the standard direction word \(\pi\pi\).  The
resulting physical block begins with the transition \(X\to Y\).  Hence
every Johnson edge is a co-block edge.  The Johnson graph is connected.
\(\square\)

The identical statement holds for odd physical wreaths: any two Johnson
neighbours can be placed as consecutive length-\(m\) cyclic windows of one
wreath.

### Corollary 3.4 (full-reservoir product no-go)

The canonical symmetric fractional necklace point gives positive marginal
to every typed physical block.  Any product of independent correlated
packets which preserves those marginals and has exact middle ownership
almost surely therefore has one global nonempty packet.  In particular:

1. it admits no decomposition into two nonempty independent packets;
2. when every selected block has \(R\) simple middle vertices, every
   outcome of that global packet contains exactly \(W/R\) selected blocks
   (so exact ownership in this pure-block model already requires
   \(R\mid W\)); in particular its selected size is not \(o(W/R)\); and
3. one fixed additive product cube whose independent coordinates output
   nonnegative subglobal block packets cannot represent the uniform
   full-reservoir point.

A sequentially and globally coupled process is not excluded.  Nor is a
product law on a deliberately sparse support whose co-block graph has
already been split into fixed middle cells.  Constructing that sparse
cellular support is a substantive part of the problem.

## 4. General common-core growing-atom rounding

The preceding no-go does not forbid independent rounding after fixed
middle-owner cells have been constructed.  In that setting there is an
exact positive theorem.

Let \(j\) index target classes \(\mathcal U_j\) of sizes \(N_j\), with
fixed totals \(T_j=c_jN_j+\rho_j\).  Let atom \(i\) have a finite state
space \(\Omega_i\).  A state \(\omega\in\Omega_i\) is a physical typed
necklace-block family with incidence vector \(a_i^\omega\).

Assume:

1. every state of atom \(i\) has the same complete middle incidence and
   covers that middle cell simply;
2. the middle cells of distinct atoms are disjoint;
3. frozen physical blocks or singleton owners cover the remaining middle
   leave exactly once; and
4. every state of atom \(i\) has the same type multiset, so all class totals
   \(T_j\) are fixed.

Thus every global state choice is an integral physical selection with
exact middle ownership and identical slot ledgers.

Give the states of different atoms independent laws, and write

\[
 \bar a_i=\mathbb Ea_i,\qquad
 \bar\mu=\sum_i\bar a_i+a_{\mathrm{frozen}}.
\]

For class weights \(w_j\geq0\), define

\[
 \|x\|_w^2=\sum_jw_j\sum_{S\in\mathcal U_j}x_j(S)^2,
\qquad
 J_w=\sum_jw_jN_j\theta_j(1-\theta_j).                     \tag{4.1}
\]

### Theorem 4.1 (growing correlated-atom dependent rounding)

Some integral global state choice satisfies

\[
 \boxed{
 \sum_jw_j\Delta_j
 \leq
 \frac12\|\bar\mu-\lambda\|_w^2
 +\frac12\sum_i\mathbb E\|a_i-\bar a_i\|_w^2
 -\frac12J_w,
 }                                                          \tag{4.2}
\]

where \(\lambda\) is the vector which equals \(T_j/N_j\) on class \(j\).

#### Proof

Apply (1.5) classwise.  Independence gives

\[
 \mathbb E\|\mu-\lambda\|_w^2
 =
 \|\bar\mu-\lambda\|_w^2
 +\sum_i\mathbb E\|a_i-\bar a_i\|_w^2.
\]

Hence the right side of (4.2) is exactly the expected weighted factorial
excess.  At least one integral outcome is no larger than its expectation.
All ownership and physical assertions hold outcome by outcome, not merely
on average.  \(\square\)

This theorem allows arbitrarily large atoms and arbitrary internal
correlation.  Its quantitative requirement is near-minimal aggregate
variance, not pairwise negative dependence.

## 5. Parity-sharp two-state rounding

Suppose atom \(i\) has two states \(a_i^0,a_i^1\).  Put

\[
 z_i=a_i^1-a_i^0,\qquad
 t=\sum_i(a_i^0+a_i^1)+2a_{\mathrm{frozen}}.                \tag{5.1}
\]

For a sign vector \(\varepsilon\in\{-1,1\}^s\), the corresponding load is

\[
 \mu^\varepsilon
 =\frac12\left(t+\sum_i\varepsilon_i z_i\right).            \tag{5.2}
\]

The complementary corner has load \(\mu^{-\varepsilon}\), and their
coordinatewise pair sum \(t\) is invariant.

For integers \(c,t\geq0\), define

\[
 b_c(t)=
 \min_{\substack{u,v\in\mathbb Z_{\geq0}\\u+v=t}}
 \{e_c(u)+e_c(v)\}
 =
 \left\lfloor\frac{(t-2c-1)^2}{4}\right\rfloor.             \tag{5.3}
\]

Put

\[
 B_w=\sum_jw_j\sum_{S\in\mathcal U_j}b_{c_j}(t_j(S)),
\qquad
 O_w=\sum_jw_j|\{S:t_j(S)\text{ is odd}\}|.                 \tag{5.4}
\]

### Lemma 5.1 (exact pair-sum identity)

If \(d\equiv t\pmod2\), then

\[
 \boxed{
 e_c\left(\frac{t+d}{2}\right)
 +e_c\left(\frac{t-d}{2}\right)
 =
 b_c(t)+\frac{d^2-\mathbf1_{\{t\ {\rm odd}\}}}{4}.
 }                                                          \tag{5.5}
\]

#### Proof

Put \(a=t-2c\).  Direct expansion of the left side gives

\[
 \frac{(a-1)^2+d^2-1}{4}.
\]

Among integers \(d\equiv t\pmod2\), the minimum of \(d^2\) is zero for
even \(t\) and one for odd \(t\).  This minimum is exactly the floor in
(5.3), proving (5.5).  \(\square\)

### Theorem 5.2 (two-state exact-owner rounding)

Some integral physical corner satisfies

\[
 \boxed{
 \sum_jw_j\Delta_j(\mu^\varepsilon)
 \leq
 \frac{B_w}{2}+\frac18\sum_i\|z_i\|_w^2.
 }                                                          \tag{5.6}
\]

More sharply, the expected excess under independent fair signs is exactly

\[
 \boxed{
 \mathbb E_\varepsilon\sum_jw_j\Delta_j(\mu^\varepsilon)
 =
 \frac{B_w}{2}
 +\frac18\sum_i\|z_i\|_w^2
 -\frac18O_w.
 }                                                          \tag{5.7}
\]

#### Proof

Pair each sign vector with its negative.  In (5.5), the coordinatewise
difference of their loads is

\[
 d^\varepsilon=\sum_i\varepsilon_i z_i.
\]

Therefore their average weighted excess is

\[
 \frac{B_w}{2}
 +\frac18\left(\|d^\varepsilon\|_w^2-O_w\right).
\]

For independent Rademacher signs,

\[
 \mathbb E\|d^\varepsilon\|_w^2=\sum_i\|z_i\|_w^2.
\]

This proves (5.7).  Some sign pair is no worse than the expectation, and
the better of its two physical corners proves (5.6).  Equivalently, one
may fix the signs by conditional expectation.  \(\square\)

The pair-sum hypothesis is not a disguised one-factor conclusion.
\(b_c(t)=0\) for all

\[
 t\in\{2c,2c+1,2c+2\}.                                     \tag{5.8}
\]

Two endpoint systems may have complementary linear defects while their
pair-sum floor is zero.  The sparse common signing in Theorem 5.2 can then
select one low-excess integral corner.

## 6. Coupled two-necklace diamonds

Take the audited physical \(2\ell\)-blocks with direction word
\(\pi\pi\).  An aligned coupled diamond of common type \(d\) consists of
two old blocks and two new blocks with:

1. the same common core, exterior, outside direction trace, and phase;
2. each old pair and each new pair internally consists of two
   middle-disjoint blocks, so each state simply covers the same
   \(4\ell\)-mask middle cell;
3. identical complete middle multiplicity vectors in the old and new
   states;
4. identical type multisets;
5. zero incidence difference at middle rank and at both depth-one signs;
6. for every \(2\leq q\leq d<\ell-2\), exactly four removed and four added
   lower targets, and exactly four removed and four added upper targets.

### Proposition 6.1 (exact diamond action)

For an aligned diamond \(i\) of type \(d_i\leq h<\ell-2\),

\[
 \boxed{
 \|z_i\|_w^2=16\sum_{q=2}^{d_i}w_q.
 }                                                          \tag{6.1}
\]

In particular, unweighted,

\[
 \|z_i\|_2^2=16(d_i-1)_+.                                  \tag{6.2}
\]

#### Proof

At one depth and one sign there are four old-only and four new-only masks.
The incidence difference is \(-1\) on the former and \(+1\) on the latter.
Thus that sign contributes eight to the squared norm; the two signs
contribute sixteen.  The supported depths are exactly
\(q=2,\ldots,d_i\).  \(\square\)

Suppose \(k_d\) type-\(d\) blocks are paired into \(k_d/2\) disjoint
diamonds.  Then

\[
 \frac18\sum_i\|z_i\|_w^2
 =
 \sum_dk_d\sum_{q=2}^dw_q.                                 \tag{6.3}
\]

For the SCD radius law

\[
 p_0=1-\rho_1,\qquad
 p_d=\rho_d-\rho_{d+1}\ (1\leq d<h),\qquad
 p_h=\rho_h,                                                \tag{6.4}
\]

and downward type counts \(k_d\leq Wp_d/R\), tail summation gives

\[
 \boxed{
 \frac18\sum_i\|z_i\|_w^2
 \leq
 \frac WR\sum_{q=2}^hw_q\rho_q.
 }                                                          \tag{6.5}
\]

For \(w_q\leq1\), \(h/\sqrt m\to\infty\), and \(R=2\ell\),

\[
 \sum_{q=2}^h\rho_q
 =
 \left(\frac{\sqrt\pi}{2}+o(1)\right)\sqrt m,
\]

so

\[
 \boxed{
 \frac18\sum_i\|z_i\|_w^2
 \leq
 \left(\frac{\sqrt\pi}{4}+o(1)\right)
 \frac{W\sqrt m}{\ell}.
 }                                                          \tag{6.6}
\]

This is \(o(W)\) as soon as \(\ell/\sqrt m\to\infty\).  The physical
certification and linearization hypotheses used below retain the stronger
\(h=o(\ell)\).

The exact limitation is just as important.  Since \(z_i=0\) at depth one,
(5.5) gives

\[
 \boxed{
 \frac{B_{1}}2=\Delta_{1}
 }                                                          \tag{6.7}
\]

for the unchanged starting depth-one system.  These diamonds cannot repair
a bad first shadow.

## 7. Direct even-necklace constant-one corollary

Assume

\[
 \frac h{\sqrt m}\to\infty,\qquad
 h=o(m^{2/3}),\qquad h=o(\ell),\qquad \ell=o(m),
 \qquad R=2\ell.                                            \tag{7.1}
\]

Choose strictly downward-rounded even type counts

\[
 \boxed{
 k_d=2\left(\left\lceil\frac{Wp_d}{2R}\right\rceil-1\right).
 }                                                          \tag{7.2}
\]

Then

\[
 0<Wp_d-Rk_d\leq2R.
\]

Let

\[
 L=W-R\sum_{d=0}^hk_d.
\]

The exact rounding bounds are

\[
 \boxed{
 0<L\leq2R(h+1),
 }                                                          \tag{7.3}
\]

and, for every \(1\leq q\leq h\),

\[
 \boxed{
 0<N_q-R\sum_{d=q}^hk_d\leq2R(h-q+1).
 }                                                          \tag{7.4}
\]

Consequently the total two-sided slot deficit satisfies

\[
 \boxed{
2\sum_{q=1}^h
 \left(N_q-R\sum_{d=q}^hk_d\right)
 \leq2Rh(h+1)=o(W).
 }                                                          \tag{7.5}
\]

Use \(L\) fixed singleton middle owners.  Suppose the remaining middle
owners admit a disjoint aligned-diamond atomization with the type counts
(7.2).  Every sign corner then has exact middle ownership and designated
base length

\[
 R\sum_dk_d+L=W.                                           \tag{7.6}
\]

Each signed nonmiddle class has total load at most its class size, so its
balanced floor is \(c_q=0\).  Define its invariant pair-sum floor by

\[
 B=
 \sum_{\substack{1\leq q\leq h\\\sigma\in\{-,+\}\\
                  S\in\mathcal U_q^\sigma}}
 \left\lfloor
 \frac{(t_{q,\sigma}(S)-1)^2}{4}
 \right\rfloor.                                            \tag{7.7}
\]

### Theorem 7.1 (literal low-collision consequence)

If

\[
 \boxed{B=o(W),}                                           \tag{7.8}
\]

then some integral physical sign corner has:

1. exact middle ownership;
2. every type count exactly equal to (7.2);
3. total pair collision
   \[
   \sum_{q,\sigma,S}\binom{\mu_{q,\sigma}(S)}2=o(W);
   \]
4. total raw collision excess \(o(W)\); and
5. \(o(W)\) uncovered central-band masks.

It yields a literal contiguous-OR word of length \(W+o(W)\), and the
standard parity lift gives the same constant-one asymptotic in odd
dimension.

#### Proof

Apply Theorem 5.2 with all \(w_q=1\).  Equations (6.6) and (7.8) give
total balanced pair excess \(o(W)\).  Since every nonmiddle class has
\(c_q=0\), this excess is exactly its pair collision count.

For an integer load \(x\),

\[
 (x-1)_+\leq\binom x2.
\]

The classwise coverage identity and (7.5) therefore give \(o(W)\) raw
collisions and holes.

Every selected object is a physical necklace block.  The base designated
length including singleton owners is exactly \(W\) by (7.6).  The audited
cycle linearization costs

\[
 O\left(\frac{hW}{R}\right)=o(W)
\]

under \(h=o(\ell)\).  Append every remaining band mask literally, at cost
\(o(W)\).  The audited product-SCD outer-tail word also costs \(o(W)\)
under (7.1).  Every witness is therefore a literal contiguous OR in one
word of total length \(W+o(W)\).
\(\square\)

This theorem is noncircular at depths \(q\geq2\): small \(B\) is a
two-cover pair-sum condition, not the conclusion that either endpoint
system is good.  But (6.7) shows that depth one must be prepared separately.
Neither (7.8) nor the existence of the aligned atomization is proved here.

## 8. A physical lattice floor

There is a secondary exact invariant.  It rules out exact zero collision
in infinitely many dimensions, but its magnitude is only polynomial and
does not obstruct \(o(W)\) excess.

For a selected standard \(\pi\pi\)-block family and \(q<\ell\), define

\[
 D_{i,q}
 =
 \sum_{U\ni i}\mu_q^+(U)
 -\sum_{S\ni i}\mu_q^-(S).                                 \tag{8.1}
\]

### Proposition 8.1 (point-margin divisibility)

For every coordinate \(i\),

\[
 \boxed{
 D_{i,q}=2qA_{i,q}\in2q\mathbb Z,
 }                                                          \tag{8.2}
\]

where \(A_{i,q}\) is the number of selected type-at-least-\(q\) blocks in
which \(i\) belongs to an active pair.

#### Proof

In one standard block, an active coordinate toggles at exactly two cycle
edges, separated by \(\ell\).  Exactly \(q\) cyclic
\((q+1)\)-windows contain each toggle, and no such window contains both
because \(q<\ell\).  Each toggle contributes \(q\) to the upper-minus-lower
point margin, with the same sign after the two complementary half-cycle
transitions.  Thus an active block contributes \(2q\), while an inactive
coordinate contributes zero.  Summing gives (8.2).  \(\square\)

If both signed depth-\(q\) load vectors were perfect one-covers, then

\[
 D_{i,q}
 =
 \binom{2m-1}{m+q-1}
 -\binom{2m-1}{m-q-1}
 =\frac{qN_q}{m}.                                          \tag{8.3}
\]

Hence a collision-free perfect one-cover—zero collisions and zero holes,
with both signed slot totals equal to \(N_q\)—requires

\[
 \boxed{2m\mid N_q.}                                       \tag{8.4}
\]

At \(q=1\),

\[
 \frac{N_1}{2m}=\frac{\operatorname{Cat}_m}{2}.
\]

The Catalan number is odd exactly when \(m=2^r-1\).  Indeed,

\[
 v_2\binom{2m}{m}=s_2(m),\qquad
 v_2(\operatorname{Cat}_m)=s_2(m)-v_2(m+1),
\]

and equality of the two binary quantities occurs exactly when the binary
expansion of \(m\) consists only of its trailing ones.  Thus a
collision-free perfect depth-one one-cover is impossible for every
Mersenne \(m\).  Collision-free partial coverage with holes is not ruled
out by this divisibility statement.

There is a quantitative form.  Put

\[
 \alpha_q=\frac{qN_q}{m},\qquad
 d_q=\operatorname{dist}(\alpha_q,2q\mathbb Z).
\]

If the two signed slot totals both equal \(N_q\), and

\[
 P_q=\sum_S\binom{\mu_q^-(S)}2+
     \sum_U\binom{\mu_q^+(U)}2,
\]

then

\[
 \boxed{
 P_q\geq\frac{m}{m+q}\,d_q.
 }                                                          \tag{8.5}
\]

To prove this, write \(\delta^\pm=\mu^\pm-\mathbf1\).
For a nonnegative integer mean-one load vector,

\[
 \|\delta^\pm\|_1\leq2P_q^\pm.
\]

Therefore

\[
 2m\,d_q
 \leq\sum_i|D_{i,q}-\alpha_q|
 \leq2(m+q)P_q,
\]

which is (8.5).  Since \(d_q\leq q\), this floor is only polynomial over
every polynomial-depth window and hence is \(o(W)\).

## 9. Exact boundary and adversarial audit

The proved conclusions are:

1. The balanced factorial objective has the exact covariance and
   quadratic-variation identities (2.1)--(2.3).
2. Independent diffuse packets cannot achieve low factorial collision;
   equality forces targetwise deterministic localization.
3. Samplewise exact middle ownership forces deterministic owner cells for
   independent packets.
4. The full physical reservoir has connected co-block graph, so a
   full-support product atomization collapses to one global atom.
5. Once disjoint common-core physical atoms exist, arbitrary growing
   internally correlated states round by Theorem 4.1.
6. For two-state atoms, Theorem 5.2 is parity-sharp and uses one common
   signing at all depths.
7. Coupled necklace diamonds have exact action \(16(d-1)_+\) and total
   radius-averaged toll
   \[
   \left(\frac{\sqrt\pi}{4}+o(1)\right)
   W\sqrt m/\ell=o(W).
   \]
8. Under the explicit atomization and pair-sum hypotheses, Theorem 7.1
   constructs a literal word of length \(W+o(W)\).
9. A collision-free perfect one-cover has the divisibility obstruction
   (8.4), but that obstruction is too small to affect coefficient one.

The following points remain unproved:

1. an almost-spanning decomposition of the rounded type family into aligned
   two-block diamond cells;
2. the pair-sum condition \(B=o(W)\);
3. a depth-one-active physical atom family, or an independently good
   depth-one starting system.

The no-go theorem explains why those inputs cannot be obtained by simply
partitioning the canonical full-reservoir fractional point into independent
unbiased growing packets.  The full support is connected, so exact
ownership permits no such product decomposition.  The positive theorem
escapes precisely by first restricting to sparse fixed middle cells; that
restriction is the unresolved global combinatorial construction.

Therefore the integral **signing** step for growing common-core atoms is
closed.  The surviving Lane-W problem is physical atomization with a
low pair-sum floor, not generic dependent rounding.  A successful future
route must either:

* construct the aligned fixed cells before rounding;
* use a sequential globally coupled law with order-\(W\) target-local
  covariance cancellation; or
* introduce depth-one-active trades outside the present diamond class.

No implication to labelled common-owner synchronization is asserted.
