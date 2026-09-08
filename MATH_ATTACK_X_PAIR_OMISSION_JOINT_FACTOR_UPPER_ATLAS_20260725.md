# Pair-omission joint factors: exact upper atlas and chronology barrier

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
web search is used.

## 0. Outcome

Put

\[
n=2m+1,\qquad
W=\binom{2m+1}{m},\qquad
T=\binom{2m+1}{m-1}=\frac{m}{m+2}W,\qquad
A_m=\binom{2m-1}{m-1}.
\tag{0.1}
\]

All star-atlas statements below are for \(m\ge3\) and
\(1\le H\le m-2\).

Partition \(2m\) coordinates into ordered pairs
\(P_1,\ldots ,P_m\), leaving one coordinate unpaired. For every omitted
pair \(P\), let \(F_P\) be an exact middle wreath factor on
\(Q_P=[n]\setminus P\).

This note proves the following direct statements.

1. The first-avoided extraction has, uniformly in all local factor choices,

   \[
   J=O\!\left(\frac{W\log ^2m}{m}\right).
   \tag{0.2}
   \]

   Hence \(J=o(W/H)\) whenever \(H\log ^2m/m\to0\), including
   \(H=O(\sqrt{m\log m})\).

   More strongly, the local factors can be chosen jointly by coordinate
   relabelling so that

   \[
   J\le \frac{T}{2m-1}+\frac{12A_m}{m-1}=O(W/m).
   \tag{0.2a}
   \]

   This order is optimal and gives \(J=o(W/H)\) throughout \(H=o(m)\).

2. If \(d_j\) is the number of phase-\(j\) tokens and \(z_{j,q}\) is the
   number of phase-\(j\) depth-\(q\) upper targets, then the unavoidable
   category support deficit satisfies, uniformly for \(H=o(m)\),

   \[
   \sum_{q\le H}\left(
      z_{\infty,q}+\sum_{j=1}^m(z_{j,q}-d_j)_+
   \right)=o(W).
   \tag{0.3}
   \]

   Thus first-avoided category confinement is not the missing support
   obstruction.

3. Fixing \(A=P_1\), one can choose a star of local factors jointly as
   coordinate conjugates of one \(F_A\). Every phase-one token then has a
   literal alternate which fixes its lower endpoint, middle owner, and all
   lower flags while changing all upper flags. Arbitrary old/alternate
   choices remain one integral central matching. The all-upper joined Gram
   is nonnegative, and the fully alternate phase-one first-upper flags are
   internally injective. The star may simultaneously be chosen so that its
   unmodified first-avoided base has the optimal bound (0.2a).

4. This exact positive atlas has a sharp chronology defect. Its fully
   alternate endpoint has at least

   \[
   m\operatorname {Cat}_{m-1}=\Theta(W)
   \tag{0.4}
   \]

   singleton source-row runs. Switching \(r\) tokens has the safe exact
   ledger

   \[
   J(M_r)\le J(M_0)+2r.
   \tag{0.5}
   \]

   Conversely, a recoding which genuinely keeps common ordered middle
   packets and changes \(J_\Sigma\) total seam incidences can change at
   most \(qJ_\Sigma\) depth-\(q\) upper occurrences.

There is also an essential floor distinction. If the window contains a
fixed band

\[
\beta\sqrt{m\log m}\le q\le\alpha\sqrt{m\log m},
\qquad \frac1{\sqrt2}<\beta<\alpha,
\tag{0.6}
\]

then the unweighted phase-one category overload is
\(\Omega(W\log m)\). Thus an unweighted all-depth \(o(W)\) demand is false
for this extraction. With the coefficient-one weights \(1/c_q\), the exact
same category cut is \(o(W)\). The weighted target survives.

The simultaneous low-interface weighted upper theorem is not proved. No
constant-one conclusion is claimed.

## 1. Token identities and exact common-row scope

Let

\[
\pi=(x_0,\ldots ,x_{2m-2})
\]

be a cyclic row of \(F_P\). With cyclic indices, put

\[
S_i=I_\pi(i,m-1),\qquad
Y_i=I_\pi(i-1,m),
\tag{1.1}
\]

and

\[
L_q(i)=I_\pi(i+q-1,m-q),\qquad
U_q(i)=I_\pi(i-1,m+q)
\quad(1\le q\le m-2).
\tag{1.2}
\]

### Lemma 1.1 (flags are determined by the central row)

For every \(q\le m-2\),

\[
\boxed{
U_q(i)=\bigcup_{h=0}^{q}Y_{i+h},\qquad
L_q(i)=\bigcap_{h=0}^{q}Y_{i+h}.}
\tag{1.3}
\]

#### Proof

The position intervals for \(Y_i,\ldots ,Y_{i+q}\) run from
\([i-1,i+m-2]\) through \([i+q-1,i+q+m-2]\). Their union is
\([i-1,i+m+q-2]\), of length \(m+q\), and their intersection is
\([i+q-1,i+m-2]\), of length \(m-q\). Injectivity of \(\pi\) gives
(1.3). \(\square\)

Thus a common ordered middle row freezes every bulk signed flag. Common-row
machinery has no additional interior flag variable once the \(Y_i\)'s are
fixed.

## 2. Factor-uniform first-avoided chronology

For \(X\subseteq[n]\), define

\[
\kappa(X)=\min\{j:X\cap P_j=\varnothing\}
\tag{2.1}
\]

when the set on the right is nonempty. Every \((m-1)\)-set has finite
category. In phase \(j\), select in \(F_{P_j}\) exactly the starts with
\(\kappa(S_i)=j\).

Set

\[
A_m=\binom{2m-1}{m-1},\qquad
R=\frac{A_m}{2m-1}=\operatorname {Cat}_{m-1}.
\tag{2.2}
\]

The exact phase size is

\[
d_j=[x^{m-1}]
x^{j-1}(2+x)^{j-1}(1+x)^{2m-2j+1},
\tag{2.3}
\]

or, equivalently,

\[
d_j=\sum_{h=0}^{j-1}(-1)^h\binom{j-1}{h}
       \binom{2m-1-2h}{m-1}.
\tag{2.4}
\]

### Theorem 2.1 (exact run ledger)

If \(J_j\) is the number of selected cyclic source-row runs in phase \(j\),
then

\[
\boxed{J_1=R,}
\tag{2.5}
\]

and, for \(j\ge2\),

\[
\boxed{J_j\le\min\{d_j,\,2(j-1)R\}.}
\tag{2.6}
\]

Consequently, for every \(1\le t<m\),

\[
\boxed{
J\le R\bigl(1+t(t-1)\bigr)+\sum_{j>t}d_j.}
\tag{2.7}
\]

There is an absolute \(C\) such that

\[
\sum_{j>t}d_j
\le C\sqrt m\,T\left(\frac34\right)^t.
\tag{2.8}
\]

#### Proof

Every local start of \(F_{P_1}\) avoids \(P_1\), so every start is selected
and each of the \(R\) cyclic rows gives one run. This is (2.5).

For \(j\ge2\), selection means meeting each of the \(j-1\) earlier pairs.
For one fixed earlier pair, the starts whose length-\((m-1)\) window avoids
that pair form at most two cyclic intervals. The union of all failure sets,
and therefore its complement, has at most \(2(j-1)\) components. This
proves (2.6), and summation gives (2.7).

For (2.8), the tail consists of \((m-1)\)-sets meeting the first \(t\)
pairs. Put \(p=(m-1)/(2m+1)\). Evaluating its generating polynomial at the
binomial saddle gives

\[
\frac{\sum_{j>t}d_j}{T}
\le
\frac{(2p-p^2)^t}
{\binom{2m+1}{m-1}p^{m-1}(1-p)^{m+2}}.
\tag{2.9}
\]

The denominator is a binomial mass at its mean, hence at least
\(c/\sqrt m\) by Stirling. Also \(2p-p^2<3/4\). This proves (2.8).
\(\square\)

The exact comparison

\[
\frac{R}{W}=\frac{m+1}{2(2m-1)(2m+1)}
\tag{2.10}
\]

and \(t=\lceil20\log m\rceil\) now give (0.2). No factor geometry entered
the proof.

The uniform bound can be sharpened by choosing the factors.

### Theorem 2.2 (order-optimal jointly relabelled chronology)

Fix arbitrary exact reference factors on the local universes. Apply an
independent uniform coordinate permutation to each phase factor. Then

\[
\boxed{
\mathbb E J\le
\frac{T}{2m-1}+\frac{12A_m}{m-1}.}
\tag{2.11}
\]

Consequently one deterministic joint tuple satisfies the same bound. Since
every source row has \(2m-1\) starts,

\[
J\ge\left\lceil\frac{T}{2m-1}\right\rceil
\tag{2.12}
\]

for every extraction, so (2.11) has the optimal order \(W/m\).

#### Proof

In one cyclic local row of length \(L=2m-1\), write \(a_i=1\) when its
\((m-1)\)-window has the phase category of that row. Every cyclic binary
word satisfies

\[
J(a)\le
\frac1L\sum_i a_i+\sum_i(1-a_{i-1})a_i.
\tag{2.13}
\]

For a nonconstant word the second term is exactly its run count. For the
all-one word the first term is one, and for the all-zero word both sides
vanish. Summed over every phase and row, the first terms in (2.13) total
exactly \(T/L\), because every global \((m-1)\)-set has one finite
first-avoided category.

Fix a directed adjacent-window edge \(S_-\to S_+\) in phase \(j\), and put
\(r=j-1\). Under a uniform coordinate relabelling it is uniform among
directed Johnson edges on the local universe. Conditional on \(S_+\), the
entering element \(u=S_+\setminus S_-\) is uniform in the \(m-1\) elements
of \(S_+\). If \(S_+\) has category \(j\) but \(S_-\) does not, then in at
least one of the \(r\) earlier pairs, \(u\) is the unique point of \(S_+\)
in that pair. Hence

\[
\Pr(a_-=0\mid a_+=1,S_+)\le\frac{r}{m-1}.
\tag{2.14}
\]

For a uniform \((m-1)\)-subset of a \((2m-1)\)-set, the exact probability
of meeting one fixed coordinate pair is

\[
p=1-\frac{m(m-1)}{(2m-1)(2m-2)}
=\frac{3m-2}{4m-2}<\frac34.
\tag{2.15}
\]

The events of meeting disjoint pairs are negatively associated under
fixed-size sampling, so

\[
\Pr(a_+=1)\le p^r<\left(\frac34\right)^r.
\tag{2.16}
\]

For completeness, the needed negative association follows by exposing
disjoint pairs successively. Conditional on the number already selected
in their union, the event that all exposed pairs are met is increasing in
that number, while the chance of meeting the next disjoint pair is
decreasing because the total sample size is fixed. The opposite-monotonicity
covariance inequality and induction give (2.16).

Each phase factor has exactly \(A_m\) directed row edges. From
(2.14)--(2.16), their expected selected \(0\)-to-\(1\) boundary total is at
most

\[
\frac{A_m}{m-1}
\sum_{r=0}^{m-1}r\left(\frac34\right)^r
\le\frac{12A_m}{m-1}.
\tag{2.17}
\]

Equations (2.13) and (2.17) prove (2.11). Averaging gives a deterministic
tuple. Finally every run has at most \(L\) selected starts, proving
(2.12). \(\square\)

### Corollary 2.3 (optimal chronology inside the star family)

The factors in the star construction of Section 6 may be chosen so that
their first-avoided base matching satisfies (2.11).

#### Proof

Start with one abstract exact factor \(G\) on a \((2m-1)\)-set. Choose a
uniform bijection \(\sigma_A\) to \(Q_A\), put \(F_A=\sigma_AG\), and for
every \(B\subset Q_A\) put \(F_B=\theta_BF_A\), as in (6.1). For each
partition pair \(P_j\), the transported map
\(\theta_{P_j}\sigma_A\) is a uniform bijection onto \(Q_{P_j}\). Thus
every phase factor has exactly the uniform marginal used in the proof of
Theorem 2.2. Independence of phases was not used after linearity of
expectation, so (2.11) holds for the correlated star family. Some choice
of \(\sigma_A\) attains it. \(\square\)

## 3. An unconditional category support theorem

Every selected upper flag preserves category:

\[
S\subseteq U_q\subseteq Q_{P_j}
\quad\Longrightarrow\quad
\kappa(U_q)=\kappa(S)=j.
\tag{3.1}
\]

Indeed, \(U_q\) avoids \(P_j\) and contains \(S\), which meets every earlier
pair.

Let

\[
z_{j,q}=[x^{m+q}]
x^{j-1}(2+x)^{j-1}(1+x)^{2m-2j+1}
\tag{3.2}
\]

be the number of depth-\(q\) upper targets of finite category \(j\), and
let

\[
z_{\infty,q}=[x^{m+q}]x^m(2+x)^m(1+x)
\tag{3.3}
\]

count targets meeting every partition pair. Define

\[
B_q^{\mathrm{cat}}
=z_{\infty,q}+\sum_{j=1}^m(z_{j,q}-d_j)_+.
\tag{3.4}
\]

### Lemma 3.1 (positive deficits occur only in late categories)

If \(j\le q+1\), then

\[
d_j\ge z_{j,q}.
\tag{3.5}
\]

#### Proof

Count inclusions \(S\subset U\) with
\(|S|=m-1\), \(|U|=m+q\), and
\(\kappa(S)=\kappa(U)=j\).

Every \(S\) has exactly \(\binom m{q+1}\) such extensions, obtained by
adding inside \(Q_{P_j}\setminus S\).

For a fixed \(U\), choose one protected representative from each of the
\(j-1\) earlier pairs. Forbid deleting these \(j-1\) chosen coordinates.
Any deletion set avoiding them leaves every earlier pair met, even when
\(U\) originally contained both coordinates of some pair. At least
\(m+q-j+1\) coordinates remain freely deletable. Hence \(U\) has at least

\[
\binom{m+q-j+1}{q+1}
\]

same-category \((m-1)\)-subsets. For \(j\le q+1\), this is at least
\(\binom m{q+1}\). Double counting proves (3.5). \(\square\)

### Theorem 3.2 (aggregate category deficit)

Uniformly for \(H=o(m)\),

\[
\boxed{\sum_{q=1}^{H}B_q^{\mathrm{cat}}=o(W).}
\tag{3.6}
\]

#### Proof

First suppose \(q\le L=\lceil20\log m\rceil\). Couple a uniform
\((m-1)\)-set \(S\) to a uniform \((m+q)\)-set \(U\) by choosing a uniform
\((q+1)\)-set \(D\subseteq[n]\setminus S\) and setting \(U=S\cup D\).
The resulting \(U\) is uniform because every \(U\) has the same number of
\((m-1)\)-subsets. The category changes only if \(D\) hits the first pair
avoided by \(S\), so

\[
\Pr(\kappa(U)\ne\kappa(S))
\le\frac{2(q+1)}{m+2}.
\tag{3.7}
\]

Moreover

\[
\left|\binom{2m+1}{m+q}-T\right|
\le C W\frac{q^2+1}{m}
\tag{3.8}
\]

in this range. Comparing the two normalized category histograms through
the coupling, and then restoring their total masses, gives

\[
B_q^{\mathrm{cat}}\le
C W\frac{q^2+q+1}{m}.
\tag{3.9}
\]

Its sum through \(L\) is \(o(W)\).

For \(q>L\), Lemma 3.1 gives

\[
B_q^{\mathrm{cat}}
\le
\#\{U:|U|=m+q,\ U\text{ meets }P_1,\ldots ,P_{q+1}\}.
\tag{3.10}
\]

For completeness, if \(k=m+q\), \(p=k/(2m+1)\), and \(s=q+1\), the same
saddle estimate gives

\[
\frac{[x^k](2x+x^2)^s(1+x)^{2m+1-2s}}
     {\binom{2m+1}{k}}
\le C\sqrt m\,(2p-p^2)^s.
\tag{3.11}
\]

Since \(q=o(m)\), eventually \(2p-p^2\le4/5\). Therefore

\[
B_q^{\mathrm{cat}}\le
C W\sqrt m\left(\frac45\right)^q.
\tag{3.12}
\]

The sum of (3.12) over \(q>L\) is \(o(W)\), proving (3.6).
\(\square\)

This is a positive capacity theorem only. It does not assert that canonical
interval flags in any chosen factors attain the available support.

## 4. Phase-one floor cut: unweighted and weighted

Phase one selects every start of \(F_A\), where \(A=P_1\). Put

\[
B_q=\binom{2m-1}{m+q},\qquad
N_q=\binom{2m+1}{m+q}.
\tag{4.1}
\]

For final word mass \(W\), write

\[
\lambda_q=\frac{W}{N_q}=c_q+\theta_q,\qquad
c_q=\lfloor\lambda_q\rfloor,\qquad
r_q=W-c_qN_q=\theta_qN_q.
\tag{4.2}
\]

Even optimistically assigning every available high quota cell to phase one,
its forced category overload is

\[
\boxed{
F_{1,q}
=\bigl[A_m-c_qB_q-\min\{r_q,B_q\}\bigr]_+.}
\tag{4.3}
\]

At \(q=1\),

\[
\boxed{F_{1,1}=A_m-B_1=\frac{W}{2m+1}.}
\tag{4.4}
\]

The exact ratios are

\[
\frac{A_m}{W}=\frac{m+1}{2(2m+1)},\qquad
\frac{B_q}{N_q}
=\frac{(m-q)(m+1-q)}{2m(2m+1)},
\tag{4.5}
\]

and

\[
R_q:=\frac{A_m/B_q}{\lambda_q}
=\frac{m(m+1)}{(m-q)(m+1-q)}.
\tag{4.6}
\]

In particular,

\[
A_m-\lambda_qB_q
=\frac{Wq(2m+1-q)}{2m(2m+1)}.
\tag{4.7}
\]

### Proposition 4.1 (unweighted Gaussian-band obstruction)

Fix \(1/\sqrt2<\beta<\alpha\). Uniformly on the band (0.6), for all
sufficiently large \(m\),

\[
\bigl[A_m-(c_q+1)B_q\bigr]_+
\ge c_{\alpha,\beta}\frac{A_mq}{m}.
\tag{4.8}
\]

Therefore, whenever the chosen window contains that band,

\[
\boxed{\sum_qF_{1,q}=\Omega_{\alpha,\beta}(W\log m).}
\tag{4.9}
\]

#### Proof

Uniformly on the band,

\[
\lambda_q=m^{q^2/(m\log m)+o(1)},\qquad
R_q-1=(2+o(1))q/m.
\]

Since \(\beta^2>1/2\), \(\lambda_q(R_q-1)\to\infty\). Hence

\[
A_m-(c_q+1)B_q
=B_q(\lambda_qR_q-c_q-1)
\ge\frac12B_q\lambda_q(R_q-1)
\ge c\frac{A_mq}{m}.
\]

The sum of \(q\) over the band is \(\Theta(m\log m)\), proving (4.9).
\(\square\)

Thus raw unweighted all-depth \(o(W)\) balance is the wrong target on this
window.

### Proposition 4.2 (the weighted category cut is sublinear)

For every fixed \(C>0\), uniformly for

\[
H\le C\sqrt{m\log m},
\]

one has

\[
\boxed{
\sum_{q=1}^{H}\frac{F_{1,q}}{c_q}
=O_C\!\left(\frac{W(1+\log m)^{3/2}}{\sqrt m}\right)
=o(W).}
\tag{4.10}
\]

#### Proof

Set \(z_q=B_q/N_q\) and
\(\delta_q=\lambda_q(R_q-1)\). Dividing (4.3) by \(N_q\) gives

\[
\frac{F_{1,q}}{N_q}
=\bigl[z_q(\theta_q+\delta_q)
       -\min\{\theta_q,z_q\}\bigr]_+.
\tag{4.11}
\]

For \(q=o(m)\), \(z_q\) is bounded above and below by positive absolute
constants. Thus (4.11) can be positive only when the fractional part
\(\theta_q\) is within \(O(\delta_q)\) of \(0\) or \(1\), and always

\[
\frac{F_{1,q}}{c_q}\le C\frac{Wq}{mc_q}.
\tag{4.12}
\]

The exact recurrence

\[
\frac{\lambda_{q+1}}{\lambda_q}
=\frac{m+q+1}{m+1-q}
\tag{4.13}
\]

gives

\[
\lambda_{q+1}-\lambda_q
=\frac{2q}{m+1-q}\lambda_q,
\qquad
\frac{\delta_q}{\lambda_{q+1}-\lambda_q}
=\frac{2m+1-q}{2(m-q)}.
\tag{4.14}
\]

We use the following elementary discrete crossing fact. Let
\(s_q=\lambda_{q+1}-\lambda_q\). On every range \(q=o(m)\), the sequence
\(s_q\) is increasing and

\[
\frac{s_{q+1}}{s_q}
=1+O\!\left(\frac1q+\frac qm\right).
\tag{4.14a}
\]

For each fixed \(K\), if \(s_q<1\) and
\(\operatorname {dist}(\lambda_q,\mathbb Z)\le Ks_q\), then \(q\) is
within \(O_K(1)\) indices of the unique crossing of the nearest integer.
Consequently each integer is assigned by only \(O_K(1)\) such indices.
Indeed, before a crossing the distance to it contains the sum of all
intervening increments; after the crossing the same is true in the other
direction. Formula (4.14a) makes all increments in any fixed number of
neighboring indices comparable. If more than \(2K+O(1)\) indices
intervened, that sum would exceed \(Ks_q\), a contradiction. This also
proves bounded charge multiplicity rather than merely asserting it.

While the increment in (4.14) is below one, every active \(q\) can
therefore be charged to an integer crossed immediately before or after
\(q\), with bounded multiplicity. Near an integer \(k\), (4.12) contributes
at most

\[
C\frac{W}{\sqrt m}\frac{\sqrt{1+\log k}}{k},
\tag{4.15}
\]

because the product formula for \(\lambda_q\) gives
\(q\le C\sqrt{m(1+\log k)}\). Summing (4.15) over
\(k\le c_{H+1}+1\) gives

\[
O\!\left(
\frac{W(1+\log c_{H+1})^{3/2}}{\sqrt m}
\right).
\tag{4.16}
\]

Once the increment reaches one, discard the activity restriction and use
the exact telescope

\[
\frac{q}{m\lambda_q}
=\frac{m+q+1}{2m}
\left(\frac1{\lambda_q}-\frac1{\lambda_{q+1}}\right).
\tag{4.17}
\]

At the first such index,
\(\lambda_q\ge(m+1-q)/(2q)\to\infty\), so throughout this tail
\(c_q\ge\lambda_q/2\) and \(1/c_q\le2/\lambda_q\).
This tail is \(O(W\sqrt{\log m/m})\). Finally
\(\log c_{H+1}=O_C(1+H^2/m)=O_C(1+\log m)\). Together with (4.4), this
proves (4.10). \(\square\)

Propositions 4.1--4.2 separate a false raw target from the actual
coefficient-one normalization. They do not control geometric collision
inside a chosen factor.

## 5. Phase orthogonality and the embedded local gate

For the unmodified first-avoided extraction, (3.1) makes upper target
supports from different phases disjoint. Hence every genuinely targetwise
additive upper functional with fixed local quotas and whose summand
vanishes at load zero decomposes as

\[
\mathcal E_H^+(F_{P_1},\ldots ,F_{P_m})
=\sum_{j=1}^m\mathcal E_{j,H}^+(F_{P_j}).
\tag{5.1}
\]

For a floor functional whose zero-load summand is nonzero, (5.1) holds
after adding the factor-independent contribution of unreachable targets.
If overload is minimized over one globally prescribed total of \(r_q\)
high cells, the remaining coupling is only the allocation of those high
cells among the disjoint phase categories; the minimized objective need
not literally equal the right side of (5.1). In either formulation, no
load or collision contributed by one factor can cancel a within-phase
histogram defect of another factor.

Phase one is especially rigid. It selects every local start. In \(Q_A\),
the complement of \(U_q(i)\) is the complementary cyclic interval of
length \(m-1-q\). Thus the complete phase-one depth-\(q\) upper histogram
is exactly the ordinary depth-\(q\) interval-shadow histogram of the one
factor \(F_A\), up to complementation. Coordinate relabelling merely
permutes it.

At \(q=1\), if

\[
\mu_A(U)=\#\{(\pi,i):\pi\in F_A,\ U_1(\pi,i)=U\},
\]

the phase-one duplicate-occurrence loss is

\[
C_1(F_A)
=\sum_U(\mu_A(U)-1)_+
=A_m-|\operatorname {supp}\mu_A|.
\tag{5.2}
\]

The number of missing possible local targets is instead

\[
B_1-|\operatorname {supp}\mu_A|
=C_1(F_A)-(A_m-B_1).
\tag{5.2a}
\]

The arithmetic minimum is

\[
C_1(F_A)\ge A_m-B_1=\frac{W}{2m+1},
\tag{5.3}
\]

with equality exactly when every possible local first-upper target occurs.
No theorem here proves \(C_1(F_A)=o(W)\), nor simultaneous weighted control
of all deeper shadows.

## 6. A literal star-conjugate all-upper atlas

The phase orthogonality of Section 5 can be left by moving tokens to factors
whose omitted pairs are not their original first-avoided pair.

Fix \(A=P_1\) and one exact factor \(F_A\) on \(Q_A\). For every pair
\(B\subset Q_A\), choose a bijection

\[
\iota_B:B\longrightarrow A.
\]

Let \(\theta_B\) exchange each \(b\in B\) with \(\iota_B(b)\), fixing all
other coordinates, and set

\[
\boxed{F_B=\theta_BF_A.}
\tag{6.1}
\]

This is an exact factor on \(Q_B\). Factors not specified by (6.1) may be
chosen arbitrarily.

Globally index a token by \(t=(\pi,i)\). To keep formulas readable, the
subscript \(i\) below is shorthand for this full token index; every sum,
comparison, and choice ranges over distinct pairs \((\pi,i)\), not merely
over row-local integers.

For a row \(\pi=(x_0,\ldots ,x_{2m-2})\in F_A\) and a start \(i\), put

\[
z_i=x_{i+m-1},\qquad
y_i=x_{i+m},\qquad
B_i=\{z_i,y_i\}.
\tag{6.2}
\]

The two coordinates of \(B_i\) immediately follow the middle window
\(Y_i=I_\pi(i-1,m)\), so \(B_i\cap Y_i=\varnothing\). Define

\[
\widetilde e_i=\theta_{B_i}e_i,
\tag{6.3}
\]

which lies literally in the row \(\theta_{B_i}\pi\) of \(F_{B_i}\).

### Theorem 6.1 (exact star atlas)

The alternate token has

\[
\widetilde S_i=S_i,\qquad
\widetilde Y_i=Y_i,
\tag{6.4}
\]

and every lower flag is fixed. Its upper flags are

\[
\boxed{
\widetilde U_1(i)=Y_i\cup\{\iota_{B_i}(z_i)\},}
\tag{6.5}
\]

and, for \(2\le q\le m-2\),

\[
\boxed{
\widetilde U_q(i)=(U_q(i)\setminus B_i)\cup A.}
\tag{6.6}
\]

Consequently:

1. replacing any set of phase-one tokens by alternates preserves the full
   lower-saturating central matching, even with every later phase unchanged;
2. the fully alternate phase-one first-upper flags are all distinct;
3. every old upper target avoids \(A\), while every alternate upper target
   meets \(A\);
4. for arbitrary positive upper weights \(w_q\), with

   \[
   d_i=(\delta_{\widetilde U_q(i)}-\delta_{U_q(i)})_{q\le H},
   \]

   distinct globally indexed tokens \(t=(\pi,i)\) and
   \(t'=(\pi',k)\) satisfy

   \[
   \boxed{
   \langle d_i,d_k\rangle_w
   =\sum_{q\le H}w_q\left(
      \mathbf1_{U_q(i)=U_q(k)}
      +\mathbf1_{\widetilde U_q(i)=\widetilde U_q(k)}
   \right)\ge0.}
   \tag{6.7}
   \]

   At \(q=1\), the second indicator vanishes.

#### Proof

The pair \(B_i\) is disjoint from \(Y_i\), and both \(A\) and \(B_i\) are
disjoint from \(S_i\subset Y_i\). Thus \(\theta_{B_i}\) fixes \(S_i\),
\(Y_i\), and every lower flag.

The first upper flag is \(U_1(i)=Y_i\cup\{z_i\}\) and does not contain
\(y_i\), proving (6.5). For \(q\ge2\), the upper interval contains both
\(z_i\) and \(y_i\), proving (6.6).

Since every lower endpoint and middle owner is unchanged, arbitrary token
choices preserve the original matching exactly.

Every middle \(m\)-set occurs once in \(F_A\). Each set in (6.5) contains
exactly one coordinate of \(A\). Equality of two such sets first forces
the same coordinate of \(A\), and deleting it forces the same middle owner.
Thus the two tokens coincide, proving first-upper injectivity.

Old targets avoid \(A\), while (6.5) meets \(A\) once and (6.6) contains
all of \(A\). Therefore old/alternate cross equalities are impossible.
Expanding the signed incidence inner product leaves exactly the two
same-sign indicators in (6.7). \(\square\)

### Corollary 6.2 (floor-exact upper Haar identity)

Let \(M_0\) be the first-avoided matching, let \(M_1\) replace every
phase-one token by its alternate, and choose each token independently with
a fair old/alternate bit. For arbitrary integers \(c_q\) and positive
upper weights, define the quadratic adjacent-integer floor energy

\[
\mathcal Q_w^+(M)
=\sum_{q\le H}w_q\sum_{|U|=m+q}
(\mu_{q,U}(M)-c_q)(\mu_{q,U}(M)-c_q-1).
\tag{6.8a}
\]

Then

\[
\boxed{
\mathbb E\mathcal Q_w^+(M_\eta)
=\frac{\mathcal Q_w^+(M_0)+\mathcal Q_w^+(M_1)}2
-\frac{\mathfrak A-\mathfrak V}{4},}
\tag{6.8}
\]

where

\[
\mathfrak A-\mathfrak V
=2\sum_{i<k}\langle d_i,d_k\rangle_w\ge0.
\tag{6.9}
\]

At the first upper rank, its old-target contribution is exactly

\[
2w_1\sum_U\binom{\mu_A(U)}2.
\tag{6.10}
\]

The identity is floor-exact because each corner has the same rankwise total
mass; the floor baseline is constant. It guarantees a corner no worse than
the coherent endpoint average, not necessarily one below the better
endpoint.

### Corollary 6.3 (exact phase-one first-upper repair)

For each old phase-one first-upper target \(U\), retain one of its
\(\mu_A(U)\) old occurrences and switch all the others. Then every
phase-one first-upper target in the resulting corner is distinct. The
number of switches is exactly

\[
r=C_1(F_A)=\sum_U(\mu_A(U)-1)_+,
\tag{6.11}
\]

the full central matching is preserved, and

\[
J(M_r)\le J(M_0)+2C_1(F_A).
\tag{6.12}
\]

#### Proof

The retained old targets are distinct by construction. The alternate
targets are distinct by Theorem 6.1, and an old target avoids \(A\) while
an alternate target meets \(A\). Hence there are no cross collisions.
The matching assertion is Theorem 6.1 and the run bound is (7.1).
\(\square\)

This is phase-one internal repair. Alternate targets can collide with
unchanged later-phase targets, which also meet \(A\); no global first-upper
injectivity is asserted. In particular (6.12) is useful at the required
chronology scale only if \(C_1(F_A)=o(W/H)\), a local factor estimate not
proved here.

## 7. Exact chronology cost of the star atlas

### Theorem 7.1 (singleton-row ledger)

If \(r\) phase-one tokens are switched, then

\[
\boxed{J(M_r)\le J(M_0)+2r.}
\tag{7.1}
\]

With the joint star choice of Corollary 2.3 this becomes

\[
\boxed{
J(M_r)\le
\frac{T}{2m-1}+\frac{12A_m}{m-1}+2r.}
\tag{7.1b}
\]

Every corner is a collection of literal factor-row runs carrying its full
two-parent flags. With the standard \(H\)-entry contexts, its core word
length is therefore

\[
T+O\!\left(H(J(M_0)+2r)\right).
\tag{7.1a}
\]

In particular, throughout \(H=o(m)\), the base term in (7.1b) is
\(o(W/H)\); if also \(r=o(W/H)\), the corner preserves the \(T+o(W)\)
literal core ledger.

If all \(A_m\) phase-one tokens are switched, their alternate tokens occupy
\(A_m\) distinct source rows. At least

\[
\boxed{mR}
\tag{7.2}
\]

of those rows belong to omitted-pair factors outside
\(\{P_1,\ldots ,P_m\}\), and hence are singleton runs in the global
matching. In particular,

\[
\boxed{J(M_1)\ge mR=\Theta(W).}
\tag{7.3}
\]

#### Proof

Deleting one selected token from a cyclic row increases its run count by
at most one. Inserting the alternate into another row also increases the
run count by at most one. This proves (7.1).

For one row \(\pi\), the pairs

\[
B_i=\{x_{i+m-1},x_{i+m}\}
\]

are its \(2m-1\) distinct adjacent coordinate pairs. Thus no two starts of
that row move to the same omitted-pair factor. If tokens from distinct
rows moved to the same physical source row, applying \(\theta_B^{-1}\)
would identify the original rows. Hence all \(A_m=(2m-1)R\) alternate
source rows are distinct.

Because \(B_i\subset Q_A\), one has \(B_i\ne A=P_1\). Hence at most
\(m-1\) of the \(2m-1\) adjacent pairs of one row belong to the fixed
partition-pair family. At least \(m\) therefore belong to factors unused
by the original extraction. Their selected alternate tokens are isolated.
Summing over the \(R\) rows proves (7.2)--(7.3). \(\square\)

The atlas has exact positive upper curvature, but buys it with one physical
source row per switched token.

## 8. Common-row seam rigidity

### Theorem 8.1 (bulk upper flags cannot change)

Consider two literal packet systems obtained from the same collection of
ordered middle-owner packets by reconnecting packet ends. Inside every
packet the token positions and ordered owners are identified and unchanged.
Let \(J_\Sigma\) be the total number of seam incidences in the two systems
(a join used in both is counted in both systems). At depth \(q\), at most
\(qJ_\Sigma\) occurrence positions have a \(q+1\)-owner window crossing
one of these seam incidences. Therefore the two depth-\(q\) upper
occurrence multisets differ by at most \(qJ_\Sigma\) substitutions, or by
at most \(2qJ_\Sigma\) in \(\ell_1\) distance.

At \(q=1\), a common-row recoding can decrease

\[
\sum_U(\mu(U)-1)_+
\]

by at most \(J_\Sigma\).

#### Proof

By Lemma 1.1, the flag at a token position is the union of the \(q+1\)
consecutive middle owners beginning there. At one seam, exactly the \(q\)
starts immediately before it cross the seam. Every other union is
unchanged.

For \(q=1\), one occurrence substitution can increase support by at most
one, while

\[
\sum_U(\mu(U)-1)_+
=\text{total occurrences}-|\operatorname {supp}\mu|.
\]

The final assertion follows. \(\square\)

Thus the existing common-row mechanism has a precise limitation. If the
ordered central row is the common object, it preserves rather than balances
all bulk upper flags. A phase-one factor with \(C_1(F_A)=\Omega(W)\) cannot
be repaired when both systems have \(o(W/H)\) seams, since then
\(J_\Sigma=o(W/H)\).

## 9. Proved and unproved boundary

The following are proved.

1. The first-avoided extraction has exact lower ownership, distinct middle
   ownership, and literal complete two-parent flags. Uniformly in the
   factors, \(J=O(W\log ^2m/m)\); a jointly relabelled tuple, including one
   inside the star family, has the order-optimal \(J=O(W/m)=o(W/H)\) for
   every \(H=o(m)\).
2. Its aggregate category support deficit is \(o(W)\) for every \(H=o(m)\).
3. Its raw phase-one Gaussian-band floor demand is impossible, while its
   required \(1/c_q\)-weighted category cut is \(o(W)\).
4. A star of jointly conjugate exact factors gives a literal integral
   phase-one atlas with fixed lower flags, fixed middle owners, an
   internally injective first-upper endpoint, and nonnegative joined Gram
   at all upper depths.
5. The fully alternate endpoint has \(\Theta(W)\) singleton runs, and a
   truly common central packet system changes only \(qJ_\Sigma\)
   depth-\(q\) flags.

The following remains unproved.

> **Missing joint low-interface upper theorem.** Choose the local exact
> factors and one integral lower-saturating token matching so that its
> correctly weighted first and deeper upper overload is \(o(W)\), while
> \(J=o(W/H)\).

For the unchanged first-avoided extraction, this already contains a
one-factor phase-one multidepth near-equitability theorem. The star atlas
escapes that phase orthogonality, but its tokenwise form has linear
chronology. Retaining the old common middle rows cannot cure the issue by
Theorem 8.1. A successful next operation must change a positive density of
central-row adjacencies while sharing their physical source rows, or must
construct locally balanced exact factors before extraction.

No such operation is proved here, so no coefficient-one theorem is claimed.
