# Mathematical attack H: pointed cyclic-flag extraction

Date: 2026-07-25

## 0. Verdict

The unconditional pointed cyclic-flag extraction theorem is not proved.
Once a positive retained shoulder incidence is present, the all-subset
matching problem and the literal endpoint-sharing problem are completely
removed.  What remains is one exact-factor concentration question.

The main finite theorem below says that pointed extraction follows whenever
the prescribed shoulder supply exceeds the aggregate balanced cap spill by
\(\varepsilon HW\).  It preserves one integral exact factor, uses only
literal intervals already present in the wreath word, and gives genuine
same-side sharing between audited shoulder targets in different parents.

For the audited compact shoulder family and any sequence of exact factors,
failure of every \(O(W/H)\), \(\Omega(W)\) extraction from that sequence
forces

\[
\boxed{
  \mathcal E_{\mathcal A}
  \ge S_{\mathcal T}-o(HW).
}
\tag{0.1}
\]

Thus almost the entire floor-weighted shoulder supply would have to be
charged by global balanced cap spill.  This is much sharper than failure
of a Hall inequality.

An independent support formulation gives a second obstruction.  If no
exact factor admits qualitative raw globally-distinct noncentral
extraction, then uniformly over all exact factors, almost every noncentral
occurrence at almost every Gaussian depth lies in a target fibre of size
\(\omega(H)\), and

\[
\boxed{
  \mathfrak K_H(F)=\omega(H^2W).
}
\tag{0.2}
\]

Coordinate relabelling cannot change either obstruction.  No theorem
currently rules them out for one exact factor throughout a fixed Gaussian
window, and no asymptotic bad exact-factor sequence is constructed here.
Consequently this report neither proves the constant-one conjecture nor
disproves pointed extraction.

No finite search, solver, web search, or numerical experiment is used.

---

## 1. Exact signed cyclic flags

Put

\[
K=2m+1,
\qquad
W=\binom Km,
\qquad
H=\lceil A\sqrt m\rceil
\tag{1.1}
\]

for fixed \(A>0\).  Let \(F\) be an exact middle wreath factor.  Its
pointed starts are

\[
\Omega_F=\{(\pi,j):\pi\in F,\ 0\le j<K\},
\qquad
|\Omega_F|=W.
\tag{1.2}
\]

Throughout, \(m\) is sufficiently large that

\[
m\ge3H+1.
\tag{1.2a}
\]

For

\[
-H\le a\le H+1
\]

define the signed flag target

\[
Z_a(\pi,j)=I_\pi(j,m+a).
\tag{1.3}
\]

Every \(Z_a(\pi,j)\) is the OR of the literal interval of length
\(H+a+1\) beginning at the original occurrence \(E_j\) in the wreath
portal word.  Thus all targets below are already witnessed at one common
physical left endpoint.

Define

\[
\tau(a)=
\begin{cases}
-a,&a\le0,\\
a-1,&a\ge1.
\end{cases}
\tag{1.4}
\]

For \(q\ge0\), let \(\mu_q^F(S)\) be the number of length-\((m-q)\)
cyclic occurrences of \(S\) in \(F\).  If \(a\ge1\), then

\[
[K]\setminus Z_a(\pi,j)
=I_\pi(j+m+a,m-a+1).
\tag{1.5}
\]

Consequently the load histogram at signed rank \(a\) is exactly the
depth-\(\tau(a)\) lower histogram, up to complementation and a permutation
of the pointed starts.  In particular the two signed slots

\[
a=-q,\qquad a=q+1
\tag{1.6}
\]

have identical load multisets.

For every \(q\le H\), put

\[
N_q=\binom K{m-q},
\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor,
\qquad
u_q=\left\lceil\frac W{N_q}\right\rceil.
\tag{1.7}
\]

Write

\[
W=c_qN_q+\rho_q,\qquad0\le\rho_q<N_q.
\tag{1.8}
\]

A balanced quota is a vector

\[
\beta_q(S)\in\{c_q,c_q+1\},
\qquad
\sum_S\beta_q(S)=W.
\tag{1.9}
\]

Choose one minimizing

\[
O_q(F)
=\sum_S\bigl(\mu_q^F(S)-\beta_q(S)\bigr)_+.
\tag{1.10}
\]

Since the two vectors in (1.9)--(1.10) have the same total mass,

\[
\boxed{
\sum_S\bigl(\beta_q(S)-\mu_q^F(S)\bigr)_+
=O_q(F).
}
\tag{1.11}
\]

No compatibility between the quota vectors at different depths is assumed
or claimed.  They are used only to cap candidate endpoint incidences; the
exact factor and its literal word are never altered.

On the fixed Gaussian window,

\[
\log\frac W{N_q}
=\frac{q(q+1)}m+O_A(m^{-1/2}),
\tag{1.12}
\]

so

\[
\Delta_A:=\max_{q\le H}u_q=u_H=O_A(1).
\tag{1.13}
\]

---

## 2. Prescribed shoulder parents

Let

\[
\mathcal A\subseteq\{-H,\ldots,H+1\}
\tag{2.1}
\]

be a set of signed slots, and for every \(a\in\mathcal A\) let

\[
\mathcal T_a\subseteq\binom{[K]}{m+a}
\tag{2.2}
\]

be the prescribed audited shoulder targets at that rank.

Assume the targets are partitioned into product-box parents with the
following fixed-dimensional property: for some fixed \(b\), a point in one
parent has at most

\[
\binom{g+b-1}{b-1}
\tag{2.3}
\]

rank-\(g\) extensions in that same parent.  Products of \(b\) saturated
chains have (2.3), because a weak composition of \(g\) specifies at most
one extension.  The audited three/four-box shell children have this
property for fixed \(b\).

Define the exact floor-weighted shoulder supply and signed cap spill

\[
S_{\mathcal T}
=\sum_{a\in\mathcal A}
c_{\tau(a)}|\mathcal T_a|,
\tag{2.4}
\]

\[
\mathcal E_{\mathcal A}(F)
=\sum_{a\in\mathcal A}O_{\tau(a)}(F).
\tag{2.5}
\]

For the full noncentral flag

\[
D_H=\{-H,\ldots,-1,2,\ldots,H+1\},
\tag{2.6}
\]

every depth \(1\le q\le H\) occurs twice, so

\[
\boxed{
\mathcal E_{D_H}(F)=2\sum_{q=1}^H O_q(F).
}
\tag{2.7}
\]

**Imported shoulder-supply input.**  For the positive-mass compact
shoulder target family used in the audited product-box endpoint ledger,
the selected signed slots satisfy

\[
S_{\mathcal T}\ge\gamma_AHW
\tag{2.8}
\]

for a fixed \(\gamma_A>0\).  This report does not reprove that
target-family estimate.  The finite theorem below is valid for an arbitrary
prescribed family and uses only the exact quantity (2.4), so every
application may instead take (2.8) as an explicit hypothesis.

---

## 3. Exact floor-capped incidence theorem

### Lemma 3.1 (one-rank cap accounting)

Fix \(q\le H\), a target subfamily

\[
\mathcal U\subseteq\binom{[K]}{m-q},
\]

and put

\[
\widehat\mu_q(S)=\min\{\mu_q^F(S),u_q\}.
\tag{3.1}
\]

Then

\[
\boxed{
\sum_{S\in\mathcal U}\widehat\mu_q(S)
\ge c_q|\mathcal U|-O_q(F).
}
\tag{3.2}
\]

#### Proof

Because \(\beta_q(S)\le u_q\),

\[
\bigl(\beta_q(S)-\widehat\mu_q(S)\bigr)_+
\le
\bigl(\beta_q(S)-\mu_q^F(S)\bigr)_+.
\tag{3.3}
\]

Also

\[
\widehat\mu_q(S)
\ge
\beta_q(S)
-
\bigl(\beta_q(S)-\widehat\mu_q(S)\bigr)_+.
\]

Sum over \(S\in\mathcal U\), use
\(\beta_q(S)\ge c_q\), and then use (1.11).  This gives (3.2).
\(\square\)

The cap in (3.1) is only a choice of at most \(u_q\) designated
occurrences in each fibre.  It deletes no word position and no wreath.

### Lemma 3.2 (global parent-collision bound)

For a coordinate relabelling \(\sigma\), let \(Y(\sigma)\) be the number
of same-parent pairs in the full, uncapped prescribed incidence graph.
Then

\[
\mathbb E_\sigma Y(\sigma)\le P_{\mathcal A}^{\#}\le P_{\mathcal A},
\]

where

\[
P_{\mathcal A}^{\#}
=W\sum_{\substack{a<a'\\a,a'\in\mathcal A}}
\frac{\binom{a'-a+b-1}{b-1}}
     {\binom{m+1-a}{a'-a}}
\]

and

\[
P_{\mathcal A}
:=
W\sum_{g=1}^{2H+1}n_g(\mathcal A)
\frac{\binom{g+b-1}{b-1}}{\binom{m-H}{g}},
\tag{3.4}
\]

where

\[
n_g(\mathcal A)
=\#\{(a,a')\in\mathcal A^2:a<a',\ a'-a=g\}.
\tag{3.5}
\]

For \(\mathcal A\) contained in the full consecutive flag and
\(1\le g\le2H+1\),

\[
n_g(\mathcal A)\le2H+2-g,
\]

while \(n_g(\mathcal A)=0\) afterward.  Consequently one can choose one
relabeling whose full collision count is at most \(P_{\mathcal A}\), and
every subsequent cap can only decrease that count.  Moreover,

\[
\boxed{
P_{\mathcal A}
=O_{A,b}\!\left(\frac{HW}{m}\right)
=o(W).
}
\tag{3.6}
\]

#### Proof

Fix two nested targets in one pointed flag, of rank gap \(g\).  Conditional
on the relabelled lower target, the upper target is uniform among its
rank-\(g\) supersets.  If the lower signed slot is \(a\), the exact number
of choices is

\[
\binom{m+1-a}{g}.
\]

Because the upper slot satisfies \(a+g\le H+1\), this is at least
\(\binom{m-H+g}{g}\), and hence at least

\[
\binom{m-H}{g}
\]

possible supersets.  Property (2.3) gives at most
\(\binom{g+b-1}{b-1}\) same-parent choices.  Summing the exact conditional
probability over the \(W\) starts and all signed pairs gives
\(P_{\mathcal A}^{\#}\); replacing its denominator by
\(\binom{m-H}{g}\) gives (3.4).

For

\[
a_g=
\frac{\binom{g+b-1}{b-1}}{\binom{m-H}{g}},
\]

one has

\[
\frac{a_{g+1}}{a_g}
=\frac{g+b}{m-H-g}
=O_{A,b}(m^{-1/2})
\tag{3.7}
\]

uniformly for \(1\le g\le2H\).  Since

\[
a_1=\frac b{m-H}=O_b(m^{-1}),
\]

the sum in (3.4) is

\[
O_{A,b}(H/m).
\]

This proves (3.6). \(\square\)

### Theorem 3.3 (finite floor-capped pointed extraction)

There is one coordinate relabelling of the literal wreath word and a
bipartite occurrence graph \(G\), with left side \(\Omega_F\) and right
side the signed prescribed targets \((a,S)\), such that:

1. every edge is an existing literal common-left-endpoint witness;
2. every target has degree at most \(\Delta_A\);
3. at most one edge remains in each endpoint--parent cell; and
4. its edge count \(L=e(G)\) satisfies

   \[
   \boxed{
   L\ge
   S_{\mathcal T}
   -\mathcal E_{\mathcal A}(F)
   -P_{\mathcal A}.
   }
   \tag{3.8}
   \]

Put

\[
d=|\mathcal A|.
\]

For integers \(1\le s\le d\) and \(D\ge1\), define

\[
M_s=
\left\lceil
\frac{\bigl(L-(s-1)W\bigr)_+}{d-s+1}
\right\rceil,
\qquad
b_s=\left\lfloor\frac{s}{\Delta_A}\right\rfloor.
\tag{3.9}
\]

If \(b_s\ge1\) and

\[
M_s\ge
p:=\left\lceil\frac D{b_s}\right\rceil,
\tag{3.10}
\]

then \(p\) pointed starts contain \(D\) globally distinct prescribed
shoulder targets which can be assigned so that targets at one start lie
in distinct product-box parents.  Their genuine same-left-endpoint
cross-parent sharing excess is at least

\[
\boxed{D-p.}
\tag{3.11}
\]

#### Proof

Choose first a relabelling whose full, uncapped same-parent pair count is
at most (3.4).  For this relabelling, retain at most
\(u_{\tau(a)}\) occurrences of each target at every signed slot.  Apply
Lemma 3.1, using complementation (1.5) for upper signed slots.  Before
parent pruning, the retained graph has at least

\[
S_{\mathcal T}-\mathcal E_{\mathcal A}(F)
\]

prescribed incidences.  Its capped same-parent collision count is no larger
than the full count used to choose the relabelling.  Keep one incidence in
every endpoint--parent cell.
If a cell contains \(r\ge1\) incidences, this deletes

\[
r-1\le\binom r2.
\]

Thus the total loss is at most \(P_{\mathcal A}\).  The target-degree cap
and (3.8) follow.

Let \(R_s\) be the number of left vertices of degree at least \(s\).  Since
every left degree is at most \(d\),

\[
L
\le
(s-1)W+R_s(d-s+1).
\tag{3.12}
\]

Therefore \(R_s\ge M_s\).

Choose any \(p\) such starts and call their set \(J\).  For every
\(X\subseteq J\),

\[
s|X|
\le e(X,N(X))
\le\Delta_A|N(X)|.
\tag{3.13}
\]

Hence

\[
|N(X)|\ge b_s|X|.
\tag{3.14}
\]

For an arbitrary set \(Y\) of clones, let \(X\) be its set of original
starts.  Then

\[
|Y|\le b_s|X|\le |N_G(X)|=|N(Y)|.
\]

Thus Hall's theorem applies to every partial clone set.  It gives an
integral \(b_s\)-fold matching and therefore \(b_sp\ge D\) distinct
targets.  Retain exactly \(D\) matched edges, keeping at least one at each
of the \(p\) starts; this is possible because \(D\ge p\).

Parent pruning guarantees distinct parents at each start.  If \(d_v\) is
the number retained at start \(v\), then

\[
\sum_v(d_v-1)_+
=D-p.
\]

Every term is genuine sharing between prescribed audited targets at one
physical left endpoint.  No arbitrary middle baseline is counted.
\(\square\)

---

## 4. The pointed theorem conditional on one exact-factor inequality

### Corollary 4.1 (positive retained cap mass is sufficient)

Assume that for some fixed \(\varepsilon>0\),

\[
\boxed{
S_{\mathcal T}
-\mathcal E_{\mathcal A}(F)
\ge\varepsilon HW.
}
\tag{4.1}
\]

Let \(\delta>0\) be any fixed demanded endpoint-sharing coefficient.
Then, for all sufficiently large \(m\), the literal word of \(F\) has

\[
O_{A,\varepsilon,\delta}(W/H)
\]

pointed starts carrying at least \(\delta W\) globally distinct prescribed
shoulder targets in pairwise distinct parents at each start.  Their
cross-parent sharing excess is

\[
(\delta-o(1))W.
\tag{4.2}
\]

#### Proof

By (3.6) and (4.1),

\[
L\ge\varepsilon HW-o(W).
\]

Each signed slot contributes at most \(W\) to (2.4), so
\(S_{\mathcal T}\le dW\).  Hypothesis (4.1) therefore implies
\(d\ge\varepsilon H\).  Hence the following choice satisfies \(s\le d\)
for all sufficiently large \(m\).

Take

\[
s=\left\lfloor\frac{\varepsilon H}{2}\right\rfloor.
\]

Equations (3.9) and \(d\le2H+2\) give

\[
M_s=\Omega_\varepsilon(W),
\qquad
b_s=\Theta_{A,\varepsilon}(H).
\tag{4.3}
\]

For \(D=\lceil\delta W\rceil\),

\[
p=\left\lceil\frac D{b_s}\right\rceil
=O_{A,\varepsilon,\delta}(W/H)
=o(W).
\]

Thus \(p<M_s\) for large \(m\), and Theorem 3.3 applies.  Formula (3.11)
gives (4.2). \(\square\)

For the audited supply (2.8), the stronger factor condition

\[
\sum_{q=1}^H O_q(F)=o(HW)
\tag{4.4}
\]

therefore proves the required pointed extraction.  Condition (4.4) is
much weaker than fixed-window MWB, which asks for a weighted sum
\(o(W)\).

### Corollary 4.2 (exact finite contrapositive)

Fix \(s\) with \(b_s\ge1\), a target demand \(D\), and put

\[
p=\left\lceil\frac D{b_s}\right\rceil.
\]

If no extraction described in Theorem 3.3 exists, then

\[
\boxed{
\mathcal E_{\mathcal A}(F)+P_{\mathcal A}
\ge
S_{\mathcal T}
-(s-1)W
-(p-1)(d-s+1).
}
\tag{4.5}
\]

#### Proof

Failure implies that fewer than \(p\) starts have degree at least \(s\).
Substitute \(R_s\le p-1\) in (3.12), and compare the result with (3.8).
\(\square\)

### Corollary 4.3 (sharp asymptotic obstruction)

Fix a sequence of exact factors \(F_m\).  Suppose that for every fixed
\(C,\delta>0\), all sufficiently large indices admit no extraction using
at most \(C W/H\) pointed starts and carrying at least \(\delta W\)
globally distinct prescribed shoulder targets with the required
parent-rainbow property.  Then

\[
\boxed{
\mathcal E_{\mathcal A}(F)
\ge S_{\mathcal T}-o(HW).
}
\tag{4.6}
\]

In particular, for \(D_H\),

\[
2\sum_{q=1}^H O_q(F)
\ge S_{\mathcal T}-o(HW).
\tag{4.7}
\]

#### Proof

If (4.6) failed, some fixed \(\varepsilon>0\) would satisfy (4.1) along a
subsequence.  Corollary 4.1 would then give fixed constants
\(C,\delta>0\), a contradiction. \(\square\)

Thus a counterexample cannot be caused by an all-subset Hall cut, an
integrality gap, a one-parent bottleneck, or isolated reset cost.  It must
have a global signed balanced cap-spill budget at least as large as the
prescribed floor-weighted shoulder supply.  The spill need not be localized
on the prescribed target fibres.

---

## 5. Exact support functional and collision energy

The cap theorem meets any prescribed endpoint coefficient.  A second
criterion describes the raw distinct-target obstruction without choosing
quotas.

Use the \(2H\) noncentral slots \(D_H\), and set

\[
p=\left\lceil\frac WH\right\rceil.
\tag{5.1}
\]

For a signed target \(S\) at slot \(a\), let

\[
\mu_a(S)
=|\{\omega\in\Omega_F:Z_a(\omega)=S\}|.
\tag{5.2}
\]

Define

\[
\Phi_p(F)
=
\sum_{a\in D_H}\sum_{|S|=m+a}
\left(
1-\frac{\binom{W-\mu_a(S)}p}{\binom Wp}
\right),
\tag{5.3}
\]

where the numerator is zero when \(W-\mu_a(S)<p\), and define

\[
\mathfrak K_H(F)
=
\sum_{a\in D_H}\sum_S\binom{\mu_a(S)}2.
\tag{5.4}
\]

Complementation gives the exact identity

\[
\mathfrak K_H(F)
=2\sum_{q=1}^H
\sum_{S\in\binom{[K]}{m-q}}
\binom{\mu_q^F(S)}2.
\tag{5.5}
\]

### Theorem 5.1 (exact thinning functional)

Some \(p\) pointed starts contain at least \(\Phi_p(F)\) globally distinct
noncentral flag targets.  Moreover,

\[
\boxed{
\Phi_p(F)
\ge
\frac{(2Hp)^2}
{2Hp+(p/W)^2\bigl(2HW+2\mathfrak K_H(F)\bigr)}.
}
\tag{5.6}
\]

Consequently,

\[
\mathfrak K_H(F)\le C_AH^2W
\tag{5.7}
\]

for a fixed constant \(C_A\) implies

\[
\Phi_p(F)
\ge
\left(\frac2{1+C_A}-o(1)\right)W.
\tag{5.8}
\]

#### Proof

Choose a uniform \(p\)-subset of the \(W\) pointed starts.  A target of
load \(\mu\) is hit with probability exactly

\[
1-\frac{\binom{W-\mu}p}{\binom Wp}.
\]

Thus its expected number of distinct targets is (5.3), and some subset
attains at least that expectation.

Let \(X\) be the hypergeometric number of selected occurrences of a fixed
target, and put

\[
x=\mathbb EX=\frac pW\mu.
\]

Since \(\operatorname{Var}X\le x\),

\[
\Pr(X>0)
\ge\frac{(\mathbb EX)^2}{\mathbb EX^2}
\ge\frac{x}{1+x}.
\tag{5.9}
\]

Cauchy--Schwarz gives

\[
\sum\frac{x}{1+x}
\ge
\frac{(\sum x)^2}{\sum x+\sum x^2}.
\tag{5.10}
\]

There are \(2H\) signed slots, each of total occurrence mass \(W\), so

\[
\sum x=2Hp.
\tag{5.11}
\]

Also

\[
\sum\mu^2
=\sum\mu+2\sum\binom\mu2
=2HW+2\mathfrak K_H(F).
\tag{5.12}
\]

Substitute (5.11)--(5.12) in (5.10).  This proves (5.6).
Since \(p/W=H^{-1}+o(H^{-1})\), (5.8) follows from (5.7).
\(\square\)

### Proposition 5.2 (transfer to genuine audited parents)

Assume that a prescribed audited shoulder subband

\[
\mathcal Q_a\subseteq\binom{[K]}{m+a},
\qquad a\in D_H,
\]

has uniform rankwise density

\[
|\mathcal Q_a|
\ge\rho_A\binom K{m+a}
\tag{5.13}
\]

for a fixed \(\rho_A>0\), and assume that these audited families inherit a
parent partition satisfying the fixed-dimensional extension bound (2.3).
If

\[
\Phi_p(F)\ge cW
\tag{5.14}
\]

for a fixed \(c>0\), then one coordinate relabelling and \(p\) pointed
starts contain

\[
\rho_AcW-o(W)
\tag{5.15}
\]

globally distinct audited shoulder targets after parent-rainbow pruning.
Their genuine audited cross-parent sharing excess is

\[
\ge\rho_AcW-o(W).
\tag{5.16}
\]

#### Proof

Choose \(p\) starts and one occurrence of every distinct target supplied
by Theorem 5.1.  Under one uniform coordinate relabelling, each chosen
rank-\((m+a)\) target lands in \(\mathcal Q_a\) with probability at least
\(\rho_A\).

Among these \(p\) starts, Lemma 3.2 bounds the expected same-parent pair
count by

\[
p\,O_{A,b}(H/m)
=O_{A,b}(W/m)
=o(W).
\]

Therefore some one relabelling has audited hits minus same-parent pairs at
least \(\rho_A\Phi_p(F)-o(W)\).  Keep one target in every repeated parent
at each start.  The surviving targets remain globally distinct and give
(5.15).

If \(d_v\) targets survive at start \(v\), their sharing excess is
\((d_v-1)_+\).  There are at most \(p=o(W)\) nonempty starts, so

\[
\sum_v(d_v-1)_+
\ge\sum_vd_v-p
\ge\rho_AcW-o(W).
\]

Only audited shoulder targets are counted; no arbitrary middle baseline
is used. \(\square\)

**Status of (5.13).**  Proposition 5.2 is conditional on this exact
rankwise-density hypothesis.  It may be imported when a separately audited
positive-mass compact shoulder subband supplies it; it is not proved in
this report and is not asserted for an exact-equal zero-mass height slice.

---

## 6. Superconcentration forced by failure

### Theorem 6.1 (sharp collision obstruction)

Let

\[
\epsilon_m=\frac{\Phi_p(F)}W.
\]

If \(\epsilon_m\to0\), put

\[
L_m=\epsilon_m^{-1/2}.
\]

Then all but \(o(HW)\) of the \(2HW\) noncentral occurrences belong to
target fibres satisfying

\[
\mu_a(S)>L_mH=\omega(H).
\tag{6.1}
\]

Consequently

\[
\boxed{
\mathfrak K_H(F)=\omega(H^2W).
}
\tag{6.2}
\]

Moreover, at all but \(o(H)\) signed depths, \((1-o(1))W\) occurrence
mass is carried by \(o(W/H)\) distinct targets.

#### Proof

Let \(M_{\rm light}\) be the total occurrence mass in cells with

\[
\mu_a(S)\le L_mH.
\]

For such a cell, (5.9) and

\[
\theta_m=\frac{pH}{W}=1+o(1)
\]

give

\[
\Pr(X>0)
\ge
\frac{(p/W)\mu_a(S)}{1+\theta_mL_m}.
\]

Hence

\[
\Phi_p(F)
\ge
\frac{(p/W)M_{\rm light}}{1+\theta_mL_m},
\]

and therefore

\[
M_{\rm light}
\le
\frac Wp(1+\theta_mL_m)\epsilon_mW
=O(\sqrt{\epsilon_m}\,HW)
=o(HW).
\tag{6.3}
\]

For every occurrence in a fibre of load \(\mu\), its contribution to
\(2\binom\mu2\), distributed over the \(\mu\) occurrences, is
\(\mu-1\).  The heavy occurrences in (6.3) therefore give

\[
\mathfrak K_H(F)
\ge
\frac{L_mH-1}{2}\bigl(2HW-o(HW)\bigr)
=\omega(H^2W).
\]

Finally choose \(\eta_m\to0\) slowly enough that the number of signed
depths with more than \(\eta_mW\) light occurrence mass is \(o(H)\).
At every other depth, heavy fibres carry at least
\((1-\eta_m)W\) mass.  Since every heavy fibre has size \(>L_mH\), their
number is at most

\[
\frac W{L_mH}=o(W/H).
\]

This proves the last assertion. \(\square\)

Under the rankwise-density hypothesis (5.13) and the inherited parent
hypothesis (2.3), consider the existential pointed theorem and define

\[
\epsilon_m^*
=\max_{F\ {\rm exact}}\frac{\Phi_p(F)}W.
\tag{6.4}
\]

If pointed extraction fails along a subsequence, then
\(\epsilon_m^*\to0\).  The proof of Theorem 6.1 with
\(L_m=(\epsilon_m^*)^{-1/2}\) then applies uniformly to every exact factor.
Thus failure forces super-\(H\) load concentration throughout the entire
exact-factor fibre, not merely in one poorly chosen factor.

Coordinate conjugation cannot repair this:

\[
\mu_a^{\sigma F}(S)
=\mu_a^F(\sigma^{-1}S).
\tag{6.5}
\]

Therefore \(\Phi_p\), \(\mathfrak K_H\), and every load histogram are
invariant under global relabelling.  Relabelling transfers already
distinct targets into audited parents; it cannot create distinctness.

---

## 7. The unconditional multiplicity ceiling is insufficient

### Lemma 7.1 (exact middle-extension packing)

For every exact factor, every \(1\le q\le H\), and every

\[
S\in\binom{[K]}{m-q},
\]

one has

\[
\boxed{
\mu_q^F(S)
\le
\left\lfloor
\frac1{q+1}\binom{m+q+1}{q}
\right\rfloor.
}
\tag{7.1}
\]

#### Proof

In a fixed oriented wreath, a proper cyclic interval set has a unique
start, so \(S\) occurs at most once in that wreath.  One cyclic occurrence
of \(S=I_\pi(j,m-q)\) lies in the \(q+1\) distinct
middle cyclic intervals

\[
I_\pi(j-r,m),
\qquad0\le r\le q.
\tag{7.2}
\]

Occurrences of \(S\) in different wreaths produce disjoint collections
in (7.2), because the exact factor assigns every middle set to exactly one
wreath.  All sets in (7.2) are \(m\)-supersets of \(S\), of which there
are exactly

\[
\binom{K-(m-q)}q
=\binom{m+q+1}q.
\]

This proves (7.1). \(\square\)

At \(q=1\), (7.1) gives

\[
\mu_1^F(S)\le\left\lfloor\frac{m+2}{2}\right\rfloor.
\]

Already at \(q=2\), however, the ceiling is of order \(m^2\), far above
the \(H=\Theta(\sqrt m)\) congestion scale.  Thus exact middle ownership
alone does not prove either (4.1) or (5.7).  Lemma 7.1 is a capacity
ceiling, not a construction realizing concentrated loads, so it is not a
counterexample.

For comparison, the exact balanced pair-collision baseline at depth \(q\)
is

\[
B_q
=N_q\binom{c_q}{2}+\rho_qc_q.
\tag{7.3}
\]

On a fixed Gaussian window,

\[
\sum_{q\le H}B_q=O_A(HW)=o(H^2W).
\tag{7.4}
\]

The obstruction (6.2) is therefore a diverging factor above the
\(H^2W\) scale, not ordinary floor-rounding noise.

---

## 8. Exact proved/conditional boundary

### Proved unconditionally

1. Floor-capping loses at most the exact balanced spill
   \(\mathcal E_{\mathcal A}\), including all holes; no second deficit term
   is hidden.
2. One global coordinate relabelling makes the total within-endpoint
   same-parent loss \(O_{A,b}(HW/m)=o(W)\).
3. After capping and parent pruning, whenever the retained incidence is
   \(\Omega(HW)\), the \(b_s\)-fold Hall inequalities are automatic for
   every chosen set \(J\) of starts of degree at least \(s\).  The integral
   matching in Theorem 3.3 gives globally distinct targets on \(O(W/H)\)
   actual starts.
4. A positive retained cap-mass gap proves the full pointed theorem with
   any fixed endpoint-dual coefficient.
5. Qualitative failure forces the near-total-spill obstruction (4.6).
6. Independently, \(O(H^2W)\) cyclic-shadow pair energy proves qualitative
   raw extraction.  Under the additional rankwise-density hypothesis
   (5.13), it transfers to audited parents.  Raw failure forces the
   superconcentration theorem (6.1)--(6.2).
7. All selected witnesses are literal intervals in one unchanged exact
   factor word, and every sharing unit is between prescribed audited
   targets in different parents.

### Unproved

The exact remaining factor statement is:

> **Positive retained shoulder mass — UNPROVED.**  For every fixed
> \(A>0\), find one exact middle wreath factor \(F_m\) for which
>
> \[
> S_{\mathcal T}
> -2\sum_{q=1}^{H}O_q(F_m)
> \ge\varepsilon_AHW
> \]
>
> for some fixed \(\varepsilon_A>0\).

The stronger sufficient collision form

\[
\min_{F\ {\rm exact}}\mathfrak K_H(F)=O_A(H^2W)
\tag{8.1}
\]

is also unproved.

Neither statement may be replaced by a fractional factor, separate
depthwise factors, a relabelled copy of one bad factor, or an unextendible
partial wreath matching.

### Adversarial audit

1. **Exact ownership.**  Capping discards only candidate designations.
   Every wreath and every middle owner remains in the same exact factor.
2. **Upper ranks.**  Their quota and spill are transported by the exact
   complement identity (1.5), not by a symmetry heuristic.
3. **Floors and holes.**  Equation (1.11) is why holes and high-load spill
   cost one \(O_q\), not two.
4. **One global relabelling.**  The target-incidence lower bound holds for
   every relabelling; averaging is used only to choose one with few
   same-parent pairs.
5. **Genuine parents.**  The sharing count never uses an arbitrary middle
   baseline as a second parent.
6. **Integrality.**  Hall is applied after cloning starts an integer
   \(b_s\) times.  The final targets and starts are integral.
7. **Literal chronology.**  All edges are selected from the existing
   depth-\(H\) flag at one physical left endpoint.  No reset or seam word is
   appended.
8. **Collision constants.**  An unspecified
   \(\mathfrak K_H=O(H^2W)\) constant gives an unspecified positive
   extraction coefficient.  The capped theorem, not that shorthand, is
   used when a prescribed endpoint-dual coefficient must be met.
9. **Scope of failure.**  Theorem 6.1 is a necessary structure for
   failure, not an example of a bad exact factor.
10. **No constant-one claim.**  The remaining exact-factor inequality in
    Section 8 is not proved.

The cap/Hall theorem and the collision-functional theorem were derived
independently and then cross-checked against each other.  Their conclusions
agree: global parent sharing and integral target assignment are available;
only exact-factor shadow concentration remains.
