# The all-block pair after the linear-edit theorem: exact fluctuation dichotomy and correlated component routing

Date: 2026-07-26

Method: pure mathematics only. No enumeration, finite search, solver, or
web input is used.

## 0. Verdict

Let

\[
 \eta_s=(2\ 3)(4\ 5)\cdots(2s-2\ \ 2s-1),
 \qquad
 G_s(P)=\eta_sF_s(\eta_sP),
\]

where \(F_s\) is the canonical anchored \(D_s\)-port factor. The theorem

\[
 \Xi(F_s,G_s)\ge
 \frac{(s-1)(s-2)}{2s-1}
 =\left(\frac12+o(1)\right)s
\tag{0.1}
\]

kills the sparse-edit sufficient estimate for this pair. It does **not**
kill the exact CRH mean/remainder mechanism.

There are three exact conclusions.

First, (0.1) can be strengthened from a Kendall-distance statement to a
carrier-position statement. If \(d_\partial(P)\) is the number of changed
proper prefix-set cuts of the two rooted row words and \(e(P)\) is the
number of equal adjacent \(\eta_s\)-blocks, then

\[
 \boxed{d_\partial(P)\ge e(P)}
\tag{0.2}
\]

for every root. Consequently

\[
 \boxed{
 \alpha_s:=
 \frac{\sum_{P\in D_s}d_\partial(P)}
      {(2s-2)C_s}
 \ge \frac{s-2}{2(2s-1)}
 \longrightarrow\frac14.}
\tag{0.3}
\]

At least \(1/3-o(1)\) of all roots have \(\Theta(s)\) changed cuts. Thus
the all-block pair has coefficient-scale **tagged** carrier supply. This
closes the activity gate left open in the earlier carrier-tensor report.

Second, let \(\mu^\varepsilon\) be the complete physical histogram of an
integral child of the actual full \(X/Y\)-ownership cube, after every
depth, cyclic start, exterior carrier, and crossing collar is included.
For balanced quotas \(\beta\), put

\[
 H_\beta(\varepsilon)
 =\sum_{q,T}\frac1{c_q}
       \bigl(\mu_q^\varepsilon(T)-\beta_q(T)\bigr)_+,
 \qquad
 L_\beta=\min_\varepsilon H_\beta(\varepsilon).
\tag{0.4}
\]

Every arbitrarily correlated component law \(\mathbb P\) satisfies

\[
 \boxed{
 {\cal R}_\beta(\mathbb P)
 \ge \max\{0,L_\beta-\Phi_\beta(\mathbb P)\},}
\tag{0.5}
\]

and, more sharply,

\[
 \boxed{
 \inf_{\mathbb P}
 \bigl(\Phi_\beta(\mathbb P)+{\cal R}_\beta(\mathbb P)\bigr)
 =L_\beta.}
\tag{0.6}
\]

Thus a linear fluctuation lower bound for every law with
\(\Phi_\beta=o(W)\) is equivalent to the genuinely integral assertion
\(L_\beta=\Omega(W)\). The edit moment \(\Xi\), even together with
(0.3), does not prove this assertion.

Third, there is an exact correlated escape from every componentwise
\(\Xi\)-estimate. If \(\delta_I\) are the complete physical component
effects and \(x_I\in\{\pm1\}\), the uniform law on the two complementary
literal children has the fair endpoint mean and

\[
 \boxed{
 {\cal R}_\beta
 =\frac14\left\|\sum_Ix_I\delta_I\right\|_{w,1},
 \qquad
 \|z\|_{w,1}:=
 \sum_{q,T}\frac{|z_q(T)|}{c_q}.}
\tag{0.7}
\]

For a conjugate pair of components \(K,K^*=\eta_sK\), correlation may
route the fluctuation into either the invariant or the anti-invariant
physical carrier mode. The component sizes and all Kendall edit
amplifications disappear from (0.7).

What is not proved is that the fair mean has
\(\Phi_\beta=o(W)\), or that the signed physical discrepancy in (0.7) is
\(o(W)\). Nor is \(L_\beta=\Omega(W)\) proved. Therefore the exact status
is:

\[
 \boxed{\text{linear }\Xi\text{ kills only the sparse-edit proof;
 the quantitative CRH gate for the pair remains open.}}
\tag{0.8}
\]

If the phrase “genuinely unrelated factors” in the formal statement of
\(\mathrm{CRH}_A\) is imposed literally, this coordinate-conjugate pair is
not itself a formal witness. Statement (0.8) concerns the substantive
mean/remainder component-rounding gate that the pair was proposed to
satisfy.

## 1. The actual complete physical component vectors

This section fixes the physical, rather than generic edit-moment,
observable.

Write the rooted coordinate word of a row as

\[
 \omega_H(P)
 =(a_1^H,\ldots,a_s^H,b_1^H,\ldots,b_s^H,\star),
 \qquad H\in\{F,G\},
\]

and let \(\Pi_c^H(P)\) be its first-\(c\) prefix set. Thus

\[
 \Pi_s^F(P)=\Pi_s^G(P)=P,
 \qquad
 \Pi_{2s}^F(P)=\Pi_{2s}^G(P)=J,
\tag{1.1}
\]

where \(J\) is the \(2s\)-coordinate local ground set.

Consider one first-fringe ambient context \(C\) in a cyclic word of
length \(2m+1\), and assume

\[
 2s+1<m-H.
\tag{1.2}
\]

For \(q\le H\), every charged ambient interval has at most one boundary
cut strictly inside the displayed local block. Let
\(E^-_{C,q,c},E^+_{C,q,c}\) be the two exterior collars at cut \(c\), and
let \(\iota_C\) be the local coordinate embedding. The complete signed
lower-shadow row profile is exactly

\[
\boxed{
\begin{aligned}
d_{C,P,q}=\sum_{c=1}^{2s}\Big(&
 e_{E^-_{C,q,c}\cup\iota_C(\Pi_c^G(P))}
-e_{E^-_{C,q,c}\cup\iota_C(\Pi_c^F(P))}\\
&+
 e_{E^+_{C,q,c}\cup
       \iota_C(J^\star\setminus\Pi_c^G(P))}
-e_{E^+_{C,q,c}\cup
       \iota_C(J^\star\setminus\Pi_c^F(P))}
\Big),
\end{aligned}}
\tag{1.3}
\]

where \(J^\star=J\cup\{\star\}\). The terms at the common cuts vanish.
The upper-shadow profile is the complement push-forward of (1.3).
Therefore (1.3) includes all cyclic starts and both crossing collars on
the charged lower side; the upper side is its complementary copy. In the
CRH convention used here, it is not stacked as a second charged
coordinate.

Let \(K\) be a component of the actual full \(X/Y\)-ownership overlay,
and let \(U_{C,K,q},V_{C,K,q}\) be its complete \(F\)- and \(G\)-shore
profiles. Define

\[
 \delta_{C,K,q}:=V_{C,K,q}-U_{C,K,q}
 =\sum_{P\in K}d_{C,P,q}.
\tag{1.4}
\]

The overlay involution sends \(K\) to

\[
 K^*=\eta_sK.
\]

If \(J_C=\eta_{C*}\) denotes the physical target permutation inherited
in context \(C\), the exact component transport law is

\[
 \boxed{
 V_{C,K,q}=J_CU_{C,K^*,q},
 \qquad
 \delta_{C,K^*,q}=-J_C\delta_{C,K,q}.}
\tag{1.5}
\]

Equations (1.3)--(1.5), rather than a word-edit surrogate, are the
physical vectors used below.

Different contexts generally have different \(J_C\). There is no
unproved global Reynolds permutation in this report. Stack all charged
lower depths and all physical targets. If \(I\) ranges over
the true independently switchable components of the installed exact
factor, write their stacked effects as \(\delta_I\). With the all-\(F\)
child as baseline,

\[
 \boxed{
 \mu^\varepsilon
 =\mu^0+\sum_I\varepsilon_I\delta_I,
 \qquad
 \varepsilon\in\{0,1\}^{\mathcal I}.}
\tag{1.6}
\]

Physical target collisions are already summed in (1.6). If a global
ownership closure merges several local slots, \(I\) means that merged
global component and \(\delta_I\) is the corresponding sum. Hence none
of the results below assumes contextwise target disjointness.

## 2. Equal blocks force a positive density of changed carrier cuts

For a root \(P\in D_s\), let

\[
 e(P)=
 \#\{1\le i\le s-1:P_{2i}=P_{2i+1}\}.
\tag{2.1}
\]

The all-block linear-edit theorem proves that every counted coordinate
pair \(\{2i,2i+1\}\) has reversed relative order between
\(\omega_F(P)\) and \(\omega_G(P)\). Since the two coordinates are both
in \(P\) or both outside \(P\), they lie in the same deletion or insertion
half.

Define

\[
 d_\partial(P)=
 \#\{1\le c\le2s-1:
       c\ne s,\ \Pi_c^F(P)\ne\Pi_c^G(P)\}.
\tag{2.2}
\]

### Theorem 2.1 (equal-block cut theorem)

For every \(P\in D_s\),

\[
                         d_\partial(P)\ge e(P).
\tag{2.3}
\]

#### Proof

Take all cuts \(c\) at which the two prefix sets agree. They include
\(0,s,2s\). Consecutive common cuts partition both rooted words into the
same ordered sequence of symbol-set blocks. Every internal cut of one
such block is noncommon.

A certified reversed pair cannot have its two symbols in different
blocks: the common block order is the same in both words, so symbols in
different blocks have the same relative order. Hence every one of the
disjoint certified pairs lies in one common-set block.

A block of length \(L\) contains at most \(\lfloor L/2\rfloor\)
certified pairs and contributes \(L-1\) changed internal cuts. For
\(L\ge2\),

\[
 \lfloor L/2\rfloor\le L-1.
\]

The cut \(s\) is common, so no block crosses the deletion/insertion
boundary and none of these internal cuts is excluded by (2.2). Summing
over the blocks proves (2.3). \(\square\)

The exact equal-block total is

\[
 \sum_{P\in D_s}e(P)
 =C_s\frac{(s-1)(s-2)}{2s-1}.
\tag{2.4}
\]

Combining (2.3) and (2.4) gives

\[
\boxed{
\sum_{P\in D_s}d_\partial(P)
\ge C_s\frac{(s-1)(s-2)}{2s-1},}
\tag{2.5}
\]

and hence (0.3).

There is also a positive-density row statement.

### Corollary 2.2 (linear activity on at least one third of the roots)

For \(s\ge3\), the fraction of roots satisfying

\[
 d_\partial(P)\ge\frac{s-2}{4}
\tag{2.6}
\]

is at least

\[
 \boxed{
 \frac{(s-2)(2s-3)}
      {(2s-1)(3s-2)}
 =\frac13-o(1).}
\tag{2.7}
\]

#### Proof

It is enough to count roots with
\(e(P)\ge(s-2)/4\). Put \(p_s\) for their fraction. Since
\(0\le e(P)\le s-1\), (2.4) gives

\[
 \frac{(s-1)(s-2)}{2s-1}
 \le p_s(s-1)+(1-p_s)\frac{s-2}{4}.
\]

Solving for \(p_s\) gives the right side of (2.7), and (2.3) gives
(2.6). \(\square\)

## 3. Exact critical-scale tagged action

Let

\[
 P_{m,s}=\frac{C_m-a_{m,s}}{C_s}
\]

be the number of disjoint first-fringe contexts, where \(a_{m,s}\) is
the number of size-\(m\) Catalan roots having no size-\(s\) fringe
subtree. Let

\[
 H=\lceil A\sqrt m\rceil,\qquad
 \Omega_{A,m}=\sum_{q\le H}\frac1{c_q},
\qquad
 \frac{\Omega_{A,m}}{\sqrt m}\longrightarrow
 J_A:=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}.
\tag{3.1}
\]

The row/start/cut-tagged action of the complete two-collar lower-shadow
tensor (1.3) is

\[
 \mathscr A^{\rm tag}_{A,m,s}
 =2\Omega_{A,m}P_{m,s}
       \sum_{P\in D_s}d_\partial(P).
\tag{3.2}
\]

Theorem 2.1 gives the explicit lower bound

\[
\boxed{
\mathscr A^{\rm tag}_{A,m,s}
\ge
2\Omega_{A,m}(C_m-a_{m,s})
\frac{(s-1)(s-2)}{2s-1}.}
\tag{3.3}
\]

If

\[
 \frac{s}{\sqrt m}\longrightarrow\kappa\in(0,\infty),
 \qquad
 a_{m,s}=o(C_m),
 \qquad
 W=(2m+1)C_m,
\]

then

\[
 \boxed{
 \liminf_{m\to\infty}
 \frac{\mathscr A^{\rm tag}_{A,m,s}}W
 \ge\frac{\kappa J_A}{2}.}
\tag{3.4}
\]

Thus the earlier open condition
\(\liminf\alpha_s>0\) is proved, with the constant \(1/4\).

This is a tagged theorem, not yet a physical collision theorem. For each
actual component and depth, (1.3) only gives

\[
 \frac12\|\delta_{C,K,q}\|_1
 \le
 \text{the corresponding tagged changed-occurrence count}.
\tag{3.5}
\]

There is no reverse inequality in the current theory. Opposite signed
cut occurrences may land on the same physical target and cancel, both
within one component and across contexts. In particular, the central
\(X/Y\)-ownership token projection cancels componentwise: the two shores
of one full overlay component own exactly the same token set, even when
the rooted row words have positive Kendall distance and positive
\(d_\partial\).

If every row/start/cut tag were physically recoverable, the fair
all-\(F\)/all-\(G\) law would have

\[
 {\cal R}^{\rm tag}
 =\frac12\mathscr A^{\rm tag},
\]

and (3.4) would give

\[
 \liminf\frac{{\cal R}^{\rm tag}}W
 \ge\frac{\kappa J_A}{4}.
\tag{3.6}
\]

Recoverability is false as an assumption-free statement and is not used
later. Formula (3.6) only quantifies the amount of tagged action which a
successful physical collision/signing theorem must compress to \(o(W)\).

## 4. Why a large \(\Xi\) cannot by itself lower-bound fluctuation

For a component \(K\), let \(D_K\) be the total rooted Kendall distance
of its paired rows and \(b_K=|K|\). Then

\[
 \Xi(F_s,G_s)=\frac1{C_s}\sum_Kb_KD_K.
\tag{4.1}
\]

For an arbitrary law on the actual bits in (1.6), let

\[
 \Sigma_{IJ}=\operatorname{Cov}(\varepsilon_I,\varepsilon_J).
\]

At one charged physical target,

\[
 \boxed{
 \operatorname{Var}\mu_q(T)
 =d_{q,T}^{\,T}\Sigma d_{q,T},
 \qquad
 d_{q,T}(I)=\delta_{I,q}(T).}
\tag{4.2}
\]

Thus fluctuation depends on signed, physically pushed-forward component
vectors and on their full covariance matrix. The statistic (4.1)
contains neither datum. It was used to upper-bound (4.2) after discarding
sign and target collisions. A lower bound on that upper estimate cannot
be reversed.

The separation is exact inside the actual \(X/Y\) overlay: the ownership
token incidence effect of each component is zero, while its \(D_K\) can
be positive. More generally, (3.5) is only one-sided. Consequently no
inequality of the form

\[
 \Xi(F_s,G_s)\le C\,{\cal R}_\beta
\]

or even a positive lower bound on \({\cal R}_\beta\) follows from the
proved data.

There is a still simpler obstruction to any unsigned argument: every
deterministic integral child has

\[
                         {\cal R}_\beta=0
\tag{4.3}
\]

regardless of \(\Xi\). Therefore a universal fluctuation obstruction for
all low-mean-hinge laws must first prove that no deterministic child has
low hinge.

## 5. Exact fluctuation versus integral-overload theorem

For a law \(\mathbb P\) on the actual cube (1.6), set

\[
 \bar\mu_q(T)=\mathbb E_{\mathbb P}\mu_q(T),
\]

\[
 \Phi_\beta(\mathbb P)
 =\sum_{q,T}\frac1{c_q}
      \bigl(\bar\mu_q(T)-\beta_q(T)\bigr)_+,
\tag{5.1}
\]

and

\[
 {\cal R}_\beta(\mathbb P)
 =\frac12\sum_{q,T}\frac1{c_q}
      \sqrt{\operatorname{Var}_{\mathbb P}\mu_q(T)}.
\tag{5.2}
\]

### Theorem 5.1 (exact integral gap theorem)

With \(L_\beta\) as in (0.4), every law satisfies (0.5), and the
optimization identity (0.6) holds.

#### Proof

For any integrable scalar random variable \(X\), with \(a=\mathbb EX\),

\[
 \mathbb E(X-b)_+-(a-b)_+
 \le\mathbb E(X-a)_+
 =\frac12\mathbb E|X-a|
 \le\frac12\sqrt{\operatorname{Var}X}.
\tag{5.3}
\]

Apply (5.3) to every \(\mu_q(T)\), multiply by \(1/c_q\), and sum. This
gives

\[
 \mathbb E_{\mathbb P}H_\beta(\varepsilon)
 \le\Phi_\beta(\mathbb P)+{\cal R}_\beta(\mathbb P).
\tag{5.4}
\]

Every support child has \(H_\beta(\varepsilon)\ge L_\beta\); hence

\[
 L_\beta
 \le\mathbb E H_\beta
 \le\Phi_\beta+{\cal R}_\beta.
\]

This proves (0.5). Conversely, choose an integral minimizer
\(\varepsilon^*\) in (0.4) and take the Dirac law at it. Then

\[
 \Phi_\beta=H_\beta(\varepsilon^*)=L_\beta,
 \qquad
 {\cal R}_\beta=0.
\]

This proves (0.6). \(\square\)

### Corollary 5.2 (exact asymptotic dichotomy)

Along any fixed-\(A\) critical-scale sequence:

1. If \(L_\beta\ge c_AW\) for all sufficiently large \(m\), then every
   law with \(\Phi_\beta=o(W)\) has

   \[
   {\cal R}_\beta\ge(c_A-o(1))W.
   \]

2. If \(L_\beta=o(W)\) along a subsequence, a deterministic literal
   exact child has

   \[
   \Phi_\beta=o(W),\qquad {\cal R}_\beta=0
   \]

   along that subsequence.

Therefore the requested universal targetwise fluctuation lower bound is
equivalent to the integral physical overload obstruction
\(L_\beta=\Omega(W)\). Neither (0.1) nor (0.3) establishes it.

For a fixed installed cube and quota sequence, Theorem 5.1 also gives the
exact existence equivalence

\[
\boxed{
\begin{aligned}
&\exists\,\mathbb P_m:
 \Phi_\beta(\mathbb P_m)+{\cal R}_\beta(\mathbb P_m)=o(W)\\
&\qquad\Longleftrightarrow\quad L_\beta=o(W)\\
&\qquad\Longleftrightarrow\quad
 \exists\,\varepsilon_m:
 H_\beta(\varepsilon_m)=o(W).
\end{aligned}}
\tag{5.5}
\]

Thus correlation can be a useful way to prove that a good child exists,
but it cannot make the zero-margin existence statement stronger than the
best integral child.

## 6. Complementary correlated laws on the actual component cube

Fix arbitrary signs \(x_I\in\{\pm1\}\), and define two complementary
children by

\[
 \varepsilon_I^+=\frac{1+x_I}{2},
 \qquad
 \varepsilon_I^-=\frac{1-x_I}{2}.
\tag{6.1}
\]

Let \(\mathbb P_x\) be uniform on these two literal exact children.

### Theorem 6.1 (exact complementary-law formula)

Every component marginal under \(\mathbb P_x\) is \(1/2\). Hence every
\(\mathbb P_x\) has the same mean, namely the fair endpoint barycenter

\[
 \bar\mu=\mu^0+\frac12\sum_I\delta_I.
\tag{6.2}
\]

Putting

\[
 Z_x=\sum_Ix_I\delta_I,
\tag{6.3}
\]

the two physical loads are \(\bar\mu\pm Z_x/2\), and

\[
 \boxed{
 \Phi_\beta(\mathbb P_x)=\Phi_\beta(\bar\mu),
 \qquad
 {\cal R}_\beta(\mathbb P_x)
 =\frac14\|Z_x\|_{w,1}.}
\tag{6.4}
\]

Consequently

\[
 \boxed{
 \min_{\text{complementary two-child laws}}{\cal R}_\beta
 =\frac14
   \min_{x\in\{\pm1\}^{\mathcal I}}
   \left\|\sum_Ix_I\delta_I\right\|_{w,1}.}
\tag{6.5}
\]

#### Proof

Equations (1.6) and (6.1) give

\[
 \mu^{\varepsilon^\pm}
 =\mu^0+\frac12\sum_I\delta_I
       \pm\frac12\sum_Ix_I\delta_I.
\]

Thus the mean is (6.2), and at each target the standard deviation is
\(|Z_x|/2\). Substitution into (5.1)--(5.2) gives (6.4), and minimization
gives (6.5). \(\square\)

The synchronized choice \(x_I=1\) is the fair law on the complete
all-\(F\) and all-\(G\) factors. It has

\[
 \boxed{
 {\cal R}_\beta
 =\frac14\|\mu^G-\mu^F\|_{w,1}.}
\tag{6.6}
\]

All factors \(b_KD_K\) in \(\Xi\) disappear. This is an explicit
correlated component law which evades the large-\(\Xi\) variance
estimate. It is a quantitative CRH witness only if its fair mean hinge
and its aggregate physical endpoint distance are both \(o(W)\), which
has not been proved.

There is one exact obstruction applying to every fair-marginal law.

### Proposition 6.2 (physical parity lower bound)

Let

\[
 D=\sum_I\delta_I=\mu^G-\mu^F.
\]

For every law satisfying
\(\mathbb E\varepsilon_I=1/2\) for all \(I\),

\[
 \boxed{
 {\cal R}_\beta
 \ge
 \frac14
 \sum_{\substack{q,T\\D_q(T)\ {\rm odd}}}\frac1{c_q}.}
\tag{6.7}
\]

#### Proof

At a target with odd \(D_q(T)\), the fair mean

\[
 \mu_q^0(T)+\frac12D_q(T)
\]

is half-integral. The random load is integer-valued, so its distance from
its mean is at least \(1/2\) in every outcome. Its variance is therefore
at least \(1/4\). Insert this in (5.2). \(\square\)

For complementary laws, the same obstruction follows from

\[
 Z_x\equiv D\pmod2
\]

coordinatewise. No current theorem counts the odd support in (6.7)
after the actual physical prefix/suffix collisions.

## 7. Exact \(\eta\)-pair covariance routing

Return to one lifted context \(C\), where the physical involution
\(J_C\) in (1.5) is defined. Suppress \(C\) from the notation.

For a non-self-conjugate pair \(\{K,K^*\}\), put

\[
 a=U_K,\qquad b=U_{K^*},\qquad
 P^\pm=\frac{I\pm J_C}{2}.
\]

Let \(x,y\in\{0,1\}\) be the switch bits on \(K,K^*\). Their exact
complete physical contribution is

\[
 L_{x,y}
 =(1-x)a+xJ_Cb+(1-y)b+yJ_Ca.
\tag{7.1}
\]

Writing \(a^\pm=P^\pm a\), \(b^\pm=P^\pm b\), direct projection gives

\[
\boxed{
\begin{aligned}
 P^+L_{x,y}
 &=a^++b^++(x-y)(b^+-a^+),\\
 P^-L_{x,y}
 &=(1-x-y)(a^-+b^-).
\end{aligned}}
\tag{7.2}
\]

Thus the four integral states are

\[
\boxed{
\begin{array}{c|c}
(x,y)&L_{x,y}\\ \hline
00&a+b\\
11&J_C(a+b)\\
10&2b^+\\
01&2a^+
\end{array}}
\tag{7.3}
\]

and every entry includes the full physical collars in (1.3).

In terms of component increments, define

\[
\begin{aligned}
 A_K
 &:=\delta_K+\delta_{K^*}
   =(I-J_C)\delta_K
   =(J_C-I)(a+b),\\
 S_K
 &:=\delta_K-\delta_{K^*}
   =(I+J_C)\delta_K
   =(I+J_C)(b-a).
\end{aligned}
\tag{7.4}
\]

The uniform same-shore coupling \(00/11\) routes the pair fluctuation
into \(A_K\). The uniform opposite-shore coupling \(10/01\) routes it
into \(S_K\). Both have the same fair mean. A self-conjugate component
has

\[
 \delta_K=(J_C-I)U_K
\]

and only an anti-invariant mode.

Most importantly, either opposite-shore state \(10\) or \(01\) is itself
a deterministic literal exact choice. It realizes one endpoint of the
potential \(J_C\)-invariant pair mode in (7.3) with **zero fluctuation**.
The pair mode is productive only when \(S_K\ne0\) and its complete
physical hinge direction is favorable. Therefore a large edit moment
cannot rule out an integral orientation of the potentially productive
component-pair modes.

If the installed global ownership closure preserves the local
context-component pairs, then for a complementary global signing every
nonstable pair contributes either a signed \(A_K\) or a signed \(S_K\)
to (6.3), according as its two signs agree or disagree. In that case
(6.5) becomes the exact actual-profile discrepancy problem

\[
\boxed{
\min
\left\|
 \sum_{\text{self }K}\pm\delta_K
 +\sum_{\{K,K^*\}}
       \pm\bigl(A_K\ \text{or}\ S_K\bigr)
\right\|_{w,1}.}
\tag{7.5}
\]

When several preserved contexts are present, (7.2)--(7.5) are applied
with their own \(J_C\). No common global involution is asserted. If the
true global \(X/Y\)-ownership closure merges local slots, (7.5) is not
available before recomputing the merged component vectors; the
unconditional formula is then the global discrepancy theorem (6.5).

## 8. Exact proved boundary and the remaining lemma

The following statements are proved.

1. The linear-\(\Xi\) lower bound closes the sparse-edit sufficient
   theorem for the all-block endpoint pair.
2. The stronger cut theorem (2.3) gives
   \(\liminf\alpha_s\ge1/4\), the critical tagged lower bound
   (3.4), and linear cut activity on at least \(1/3-o(1)\) of roots.
3. Every component law obeys the exact integral gap theorem
   (0.5)--(0.6).
4. Complementary correlated laws obey the exact full-profile formula
   (6.4), and conjugate component pairs have the four-state physical
   normal form (7.3).
5. The fair-marginal parity obstruction (6.7) is exact.

The following statements are **not proved**.

1. A reverse inequality retaining a positive fraction of the tagged
   action after the physical prefix/suffix push-forward.
2. A uniform classification of the self-conjugate and paired components
   of the full \(X/Y\) overlay.
3. The fair full-profile mean estimate
   \(\Phi_\beta(\bar\mu)=o(W)\).
4. The signed physical discrepancy estimate in (6.5) or (7.5).
5. The integral no-go \(L_\beta=\Omega(W)\).

The single minimal pair-specific gate is integral.

> **Integral physical child theorem
> \(\mathrm{IPC}_A(F_s,G_s)\) (unproved).**
> At the critical first-fringe scale
> \(s/\sqrt m\to\kappa\in(0,\infty)\), with every charged lower depth
> \(q\le\lceil A\sqrt m\rceil\), all cyclic starts, and both crossing
> collars included through (1.3), for every sufficiently large \(m\)
> choose balanced quotas \(\beta\) and one literal global
> \(X/Y\)-component child satisfying
> \[
>                  H_\beta(\varepsilon)=o_A(W).
> \]

By (5.5), this theorem is exactly equivalent to the substantive
mean/remainder existence clause for this installed pair. A pair-specific
no-go requires the opposite quota-uniform statement: for some
\(c_A>0\) and infinitely many \(m\),

\[
 \min_{\substack{\beta\ {\rm balanced}\\
                  \varepsilon\ {\rm an\ actual\ child}}}
 H_\beta(\varepsilon)
 \ge c_AW.
\tag{8.1}
\]

A useful sufficient route to \(\mathrm{IPC}_A\), but not an equivalent
reformulation of it, is the correlated complementary route

\[
 \Phi_\beta(\bar\mu)=o_A(W),
 \qquad
 \min_x\left\|\sum_Ix_I\delta_I\right\|_{w,1}=o_A(W).
\tag{8.2}
\]

Theorem 6.1 then supplies an explicit two-child correlated law with
\(\Phi_\beta+{\cal R}_\beta=o_A(W)\), and Theorem 5.1 extracts a good
integral support child. A good integral child could also exist even if
the fair barycenter or every complementary discrepancy in (8.2) is
large; this is why (8.2) is sufficient rather than minimal.

The new theorem \(\Xi=\Omega(s)\) proves neither
\(\mathrm{IPC}_A\) nor the no-go (8.1). It shows that the tagged input is
extensive; the unresolved question is whether the actual full \(X/Y\)
carrier projection preserves an obstruction or admits coefficient-scale
cancellation.
