# Whole-bite ordinary profiles: exact coalescence serialization and the signed reachable gate

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad r=m-q_0,\qquad
 q_0=a\sqrt m+O(1),\qquad H=b\sqrt m+O(1),
\tag{0.1}
\]

where \(0<a<b\) are fixed, and put

\[
 J=H-q_0,\qquad V_d=\binom{[n]}{r-d},\qquad
 N_d=|V_d|\quad(0\le d\le J).
\tag{0.2}
\]

This note attacks the whole-bite gate in
`MATH_THEOREM_ORDINARY_ANNULAR_STOPPED_PROFILE_FUNCTIONAL_20260727.md`.
There are four conclusions.

1. **Same-bite coalescence is exactly serializable.** If a legal bite
   \(\mathcal B=\{e_1,\ldots,e_s\}\) is exposed in any order, then its
   exact whole-bite loss equals the sum of the exact one-packet losses in
   the successively updated state:

   \[
    \boxed{
    L_{\mathcal M}(\mathcal B)
       =\sum_{h=1}^s\ell_{\mathcal M\cup
                    \{e_1,\ldots,e_{h-1}\}}(e_h).}
   \tag{0.3}
   \]

   A current hole hit \(k\) times in the bite is fresh for its first
   packet and is a covered-target collision for the remaining \(k-1\)
   packets. These \(k-1\) terms are exactly \((k-1)_+\), the
   coalescence \(\chi\). Thus changing bite size or packet order merely
   moves a debit between the old--new and new--new ledgers.

2. **The cumulative conservation law is terminal and bite-independent.**
   For any ordered partition of a terminal entrance matching
   \(\mathcal M_*\) into legal bites,

   \[
    \boxed{
    \sum_j\left(O_j+X_j-R_j\right)
       =\sum_{d=0}^J
          \left(\min\{G_*,N_d\}-|S_{d,*}|\right)
       =:\mathfrak C(\mathcal M_*).}
   \tag{0.4}
   \]

   Here \(O_j\) is the covered-target occurrence debit, \(X_j\) is
   same-bite coalescence on current holes, and
   \(R_j=\sum_d(nb_j-c_{d,j})\) is the exact scalar saturation credit.
   In particular, there is no hidden favorable covariance obtained by
   taking a large bite.

3. **Coalescence itself can be made negligible.** Suppose a conditional
   law on a legal bite has packet marginals \(p_e\), pair marginals
   \(p_{ef}\), and target intensities

   \[
     \lambda_d(T)=\sum_{e:T\in e_d}p_e.
   \tag{0.5}
   \]

   If

   \[
     p_{ef}\le(1+\eta)p_ep_f,
     \qquad
     \max_{d,T}\lambda_d(T)\le\theta,
   \tag{0.6}
   \]

   then

   \[
    \boxed{
    \mathbb E[X_j\mid\mathcal F_j]
       \le {1+\eta\over2}\theta n(J+1)
          \mathbb E[b_j\mid\mathcal F_j].}
   \tag{0.7}
   \]

   Therefore every slow diffuse bite process satisfying
   \(\theta J=o(1)\), \(\eta=O(1)\), and selecting altogether
   \(O(W/n)\) packets has cumulative expected coalescence \(o(W)\).
   Singleton bites have \(X_j=0\) identically and need no hypothesis.

4. **The remaining gate is exactly first-order and reachable.** Define

   \[
    F_j:=\sum_dc_{d,j}
       -\sum_d\sum_{T\in\mathcal H_{d,j}}\lambda_{d,j}(T).
   \tag{0.8}
   \]

   The exact drift is \(F_j+\mathbb E[X_j\mid\mathcal F_j]\). Hence a
   slow diffuse bite law with one common entrance leave proves the desired
   annulus theorem once

   \[
    \boxed{
       \mathbb E\sum_{j<\tau}F_j=o(W),
       \qquad \theta J=o(1),
       \qquad L_\tau=O(N_0/\sqrt m).}
   \tag{0.9}
   \]

   Under the displayed diffuse assumptions, the first condition is also
   the only remaining stopped-profile expectation condition. It is the
   joint shallow-debit/deep-credit assertion.
   It cannot be inferred from separate rank marginals: there are
   separately floor-perfect formal states in which every legal packet has
   loss \(\Omega(m^{3/2})\). Such states have not been realized by one
   common entrance matching. Thus the exact unresolved condition is a
   signed Hall inequality on reachable common-history states, not
   same-bite coalescence and not an independent-rank leave.

The note consequently closes the \(\chi\) part of the whole-bite audit.
It does not assert the still-missing reachable signed Hall inequality in
(0.9).

## 1. Exact whole-bite ledger

Let \(\mathcal M\) be the current entrance matching. Put

\[
 G=n|\mathcal M|,\qquad
 S_d=\bigcup_{f\in\mathcal M}f_d,\qquad
 \mathcal H_d=V_d\setminus S_d.
\tag{1.1}
\]

Let \(\mathcal B\) be a legal bite of \(s\) new packets. For
\(T\in V_d\), write

\[
 \nu_d(T)=|\{e\in\mathcal B:T\in e_d\}|.
\tag{1.2}
\]

The scalar capacity increment and fresh support are

\[
 c_d=\min\{G+ns,N_d\}-\min\{G,N_d\},
\tag{1.3}
\]

\[
 Z_d=\left|\mathcal H_d\cap
       \bigcup_{e\in\mathcal B}e_d\right|.
\tag{1.4}
\]

Define

\[
 O_d=\sum_{T\in S_d}\nu_d(T),
 \qquad
 X_d=\sum_{T\in\mathcal H_d}(\nu_d(T)-1)_+,
 \qquad
 R_d=ns-c_d.
\tag{1.5}
\]

Here \(O_d\) is the old--new collision occurrence count, \(X_d\) is
the exact same-bite coalescence, and \(R_d\) is the scalar credit from
crossing or lying beyond saturation at depth \(d\).

### Lemma 1.1 (exact occurrence decomposition)

At every depth,

\[
 \boxed{c_d-Z_d=O_d+X_d-R_d.}
\tag{1.6}
\]

Consequently

\[
 \boxed{
 L_{\mathcal M}(\mathcal B)
 :=\sum_d(c_d-Z_d)
 =O(\mathcal B)+X(\mathcal B)-R(\mathcal B),}
\tag{1.7}
\]

where the three capital letters on the right denote sums over \(d\).

#### Proof

The bite contains \(ns=\sum_T\nu_d(T)\) occurrences at depth \(d\).
On current holes,

\[
 \sum_{T\in\mathcal H_d}\nu_d(T)-Z_d
 =\sum_{T\in\mathcal H_d}(\nu_d(T)-1)_+=X_d.
\]

Therefore \(ns-Z_d=O_d+X_d\). Add \(c_d-ns=-R_d\).
\(\square\)

The identity shows why a first-moment exposure calculation which omits
\(X_d\) is not a whole-bite calculation. It also shows that \(X_d\)
is target-restricted: multiple hits on a target already in \(S_d\) are
all counted in \(O_d\), not again in \(X_d\).

## 2. Serialization theorem

Fix an ordering \(e_1,\ldots,e_s\) of \(\mathcal B\), and put

\[
 \mathcal M^{h}=\mathcal M\cup\{e_1,\ldots,e_h\},
 \qquad G^h=G+nh.
\tag{2.1}
\]

Let

\[
 S_d^h=S_d\cup\bigcup_{i\le h}(e_i)_d,
 \qquad \mathcal H_d^h=V_d\setminus S_d^h.
\tag{2.2}
\]

The one-packet scalar increment and loss at substep \(h\) are

\[
 c_d^h=\min\{G^h,N_d\}-\min\{G^{h-1},N_d\},
\tag{2.3}
\]

\[
 \ell_{\mathcal M^{h-1}}(e_h)
 =\sum_d\left(c_d^h-|(e_h)_d\cap\mathcal H_d^{h-1}|\right).
\tag{2.4}
\]

### Theorem 2.1 (exact serialization)

For every ordering of every legal bite,

\[
 \boxed{
 L_{\mathcal M}(\mathcal B)
 =\sum_{h=1}^s\ell_{\mathcal M^{h-1}}(e_h).}
\tag{2.5}
\]

Moreover, at each depth,

\[
 \boxed{
 X_d=\sum_{h=1}^s
 \left|(e_h)_d\cap
 \left(S_d^{h-1}\setminus S_d\right)\right|.}
\tag{2.6}
\]

#### Proof

The scalar terms telescope:

\[
 \sum_{h=1}^sc_d^h
 =\min\{G+ns,N_d\}-\min\{G,N_d\}=c_d.
\tag{2.7}
\]

For a fixed current hole \(T\), suppose \(\nu_d(T)=k\). Its first
occurrence in the chosen order contributes one to the fresh-support sum;
the remaining \(k-1\) occurrences meet
\(S_d^{h-1}\setminus S_d\). Hence their total is
\((k-1)_+\). Summing over current holes proves (2.6). It also gives

\[
 \sum_{h=1}^s|(e_h)_d\cap\mathcal H_d^{h-1}|=Z_d.
\tag{2.8}
\]

Combine (2.7)--(2.8) and sum over \(d\). \(\square\)

Thus simultaneous and sequential nibble implementations have the same
pathwise profile loss after the state is updated within the bite. The
term \(\chi\) is necessary in a simultaneous conditional expectation,
but it is not an additional terminal obstruction.

## 3. Conservation over a complete trajectory

Let \(\mathcal B_0,\ldots,\mathcal B_{t-1}\) be any ordered bite
decomposition of a terminal entrance matching \(\mathcal M_*\). Put

\[
 G_*=n|\mathcal M_*|,qquad
 \mu_d(T)=|\{e\in\mathcal M_*:T\in e_d\}|,
 \qquad S_{d,*}=\{T:\mu_d(T)>0\}.
\tag{3.1}
\]

### Theorem 3.1 (global collision-credit conservation)

For each depth,

\[
 \boxed{
 \sum_j(O_{d,j}+X_{d,j})
   =\sum_T(\mu_d(T)-1)_+
   =G_*-|S_{d,*}|,}
\tag{3.2}
\]

and

\[
 \boxed{
 \sum_jR_{d,j}
   =G_*-\min\{G_*,N_d\}=(G_*-N_d)_+.}
\tag{3.3}
\]

Consequently (0.4) holds.

#### Proof

Fix \(d,T\), and expose all occurrences of \(T\) chronologically.
When \(\mu_d(T)>0\), its first occurrence is fresh. Every later
occurrence is counted once: in \(O_{d,j}\) if \(T\) was covered before
bite \(j\), and in \(X_{d,j}\) if its first and a later occurrence lie
in the same bite. This proves (3.2). Equation (3.3) is the telescoping
identity for \(\min\{G,N_d\}\). Their difference is

\[
 G_*-|S_{d,*}|-(G_*-N_d)_+
 =\min\{G_*,N_d\}-|S_{d,*}|.
\]

Sum over \(d\). \(\square\)

An immediate consequence is that bite regrouping cannot repair a bad
terminal family. Conversely, a good terminal family remains good under
every bite decomposition, although the split between \(O\) and \(X\)
may change substantially.

## 4. A quantitative diffuse-bite bound for \(\chi\)

Condition on the current filtration and let \(\mathcal B\) be a random
legal bite. Put

\[
 p_e=\Pr(e\in\mathcal B),\qquad
 p_{ef}=\Pr(e,f\in\mathcal B),
\tag{4.1}
\]

and define \(\lambda_d(T)\) by (0.5). We do not assume independent
packet choices; entrance legality generally makes them dependent.

### Lemma 4.1 (hole-restricted pair domination)

For every bite law,

\[
 \boxed{
 \mathbb E[X\mid\mathcal F]
 \le\sum_{d=0}^J\sum_{T\in\mathcal H_d}
       \sum_{\{e,f\}:T\in e_d\cap f_d}p_{ef}.}
\tag{4.2}
\]

#### Proof

For every integer \(k\ge0\),
\((k-1)_+\le\binom k2\). Apply this with
\(k=\nu_d(T)\), take conditional expectations, and expand the falling
pair moment. \(\square\)

### Theorem 4.2 (slow diffuse bites close coalescence)

Assume (0.6), with \(\eta\ge0\). Then

\[
 \begin{aligned}
 \mathbb E[X\mid\mathcal F]
 &\le {1+\eta\over2}
       \sum_{d,T\in\mathcal H_d}\lambda_d(T)^2\\
 &\le {1+\eta\over2}\theta
       \sum_{d,T\in\mathcal H_d}\lambda_d(T)\\
 &\le {1+\eta\over2}\theta n(J+1)\,
       \mathbb E[|\mathcal B|\mid\mathcal F].
 \end{aligned}
\tag{4.3}
\]

In particular, if a stopped process selects altogether at most
\(C W/n\) packets, then

\[
 \boxed{
 \mathbb E\sum_{j<\tau}X_j
 \le {C(1+\eta)\over2}\theta(J+1)W=o(W)}
\tag{4.4}
\]

whenever \(\theta J=o(1)\).

#### Proof

Use (4.2) and \(p_{ef}\le(1+\eta)p_ep_f\). For fixed \(d,T\),

\[
 \sum_{e<f:T\in e_d\cap f_d}p_ep_f
 \le\frac12\left(\sum_{e:T\in e_d}p_e\right)^2
 =\frac12\lambda_d(T)^2.
\]

The second line of (4.3) uses \(\lambda_d(T)\le\theta\). For the last
line, every selected packet contributes exactly \(n\) targets at each
of the \(J+1\) depths. Sum (4.3) over the process. \(\square\)

The scale \(\theta=o(1/J)\) is sharp for this first-pair estimate: there
are \(J+1=\Theta(\sqrt m)\) target layers, and each unit of packet mass
appears \(n\) times in every layer. The theorem does not require
rankwise leaves or independent choices across ranks.

### Corollary 4.3 (deterministic bite extracted from a diffuse law)

Suppose the law in Theorem 4.2 is supported on legal bites of one fixed
size \(s\). Then at least one bite in its support satisfies

\[
 \boxed{
 L_{\mathcal M}(\mathcal B)
 \le \sum_dc_d
   -\sum_{d,T\in\mathcal H_d}\lambda_d(T)
   +{1+\eta\over2}\theta n(J+1)s.}
\tag{4.5}
\]

#### Proof

The conditional expectation of the left side is the first two terms on
the right plus \(\mathbb E X\). Apply (4.3). A finite collection cannot
have every member larger than its average. \(\square\)

Thus any proof of the signed first-moment inequality automatically has a
deterministic bite implementation; the stochastic law may be used only
as an averaging certificate.

## 5. Signed shallow/deep drift after \(\chi\) is removed

For a conditional bite law define

\[
 A_j=\sum_{d=0}^J\sum_{T\in\mathcal H_{d,j}}
       \lambda_{d,j}(T),
 \qquad
 F_j=\sum_{d=0}^Jc_{d,j}-A_j.
\tag{5.1}
\]

The exact conditional identity is

\[
 \boxed{
 \mathbb E[L_j\mid\mathcal F_j]
 =F_j+\mathbb E[X_j\mid\mathcal F_j].}
\tag{5.2}
\]

The first term has the desired signed interpretation. For clarity,
serialize the bite and consider one packet \(e\) in the current
within-bite state. Partition the depths into

\[
 \mathcal U=\{d:G+n\le N_d\},\qquad
 \mathcal S=\{d:N_d\le G\},
\tag{5.3}
\]

and the at-most-one boundary depth \(\mathcal D\), where
\(G<N_d<G+n\). Then

\[
 \boxed{
 \begin{aligned}
 \ell_{\mathcal M}(e)
 &=\sum_{d\in\mathcal U}|e_d\cap S_d|\\
 &\quad+\sum_{d\in\mathcal D}
   \left(|e_d\cap S_d|-(G+n-N_d)\right)\\
 &\quad-\sum_{d\in\mathcal S}|e_d\cap\mathcal H_d|.
 \end{aligned}}
\tag{5.4}
\]

Thus collisions at shallow unsaturated depths are positive debits, while
hits on deep saturated holes are negative credits. Both use the same
packet and the same reachable support family. Formula (5.4), summed over
the serialized bite, equals \(F_j+X_j\), not a collection of independent
rankwise objectives.

### Theorem 5.1 (whole-bite sufficient theorem)

Suppose a stopped legal bite process satisfies

\[
 \mathbb E\sum_{j<\tau}F_j=o(W),
\tag{5.5}
\]

and either uses singleton bites or satisfies the hypotheses of Theorem
4.2 with \(\theta J=o(1)\). Then

\[
 \boxed{\mathbb E\mathfrak C_\tau=o(W).}
\tag{5.6}
\]

If, in addition,

\[
 L_\tau=N_0-G_\tau=O(N_0/\sqrt m),
\tag{5.7}
\]

then some realization has \(o(W)\) aggregate holes across the complete
lower annulus, and hence also across the complementary upper annulus.

#### Proof

The stopped-profile martingale and (5.2) give

\[
 \mathbb E\mathfrak C_\tau
 =\mathbb E\sum_{j<\tau}F_j
  +\mathbb E\sum_{j<\tau}X_j.
\]

The second term is zero for singleton bites and is \(o(W)\) by Theorem
4.2 otherwise. This proves (5.6). The common scalar leave contributes

\[
 B(L_\tau)=\sum_d(N_d-G_\tau)_+
 =O\left(L_\tau+{L_\tau^2\sqrt m\over N_0}\right)=o(W).
\]

Finally

\[
 \sum_dH_d=B(L_\tau)+\mathfrak C_\tau.
\]

Nonnegativity and conditional expectation give a realization with the
claimed bound. Complementation preserves the support ledger. \(\square\)

## 6. Deterministic selection and the exact signed Hall cut

At a fixed state and fixed bite size, randomization cannot improve the
best conditional loss. Indeed, for every distribution \(\pi\) on the
finite family of legal bites,

\[
 \mathbb E_\pi L_{\mathcal M}(\mathcal B)
 \ge\min_{\mathcal B}L_{\mathcal M}(\mathcal B).
\tag{6.1}
\]

Thus whenever a law proves
\(\mathbb E[L_{\mathcal M}(\mathcal B)]\le\varepsilon\), one may select
deterministically a bite with loss at most \(\varepsilon\). Applied
successively, this is the method of conditional expectations; no extra
rounding loss occurs.

For singleton steps the exact statewise cut is especially transparent.
Let \(\mathcal L(\mathcal M)\) be the legal next-packet catalogue and
let \(\ell_{\mathcal M}(e)\) be (5.4). Then a next packet with drift at
most \(\varepsilon\) exists if and only if

\[
 \boxed{
 \min_{e\in\mathcal L(\mathcal M)}
       \ell_{\mathcal M}(e)\le\varepsilon.}
\tag{6.2}
\]

Equivalently, a nonnegative weighting \(w\), not identically zero,
certifies it whenever

\[
 \begin{aligned}
 &\sum_{e}w(e)
 \left[
  \sum_{d\in\mathcal U}|e_d\cap S_d|
  +\sum_{d\in\mathcal D}
      (|e_d\cap S_d|-(G+n-N_d))
  -\sum_{d\in\mathcal S}|e_d\cap\mathcal H_d|
 \right]\\
 &\hspace{45mm}\le\varepsilon\sum_ew(e).
 \end{aligned}
\tag{6.3}
\]

This is the exact signed Hall cut. It is joint in all depths and refers
to the supports generated by the same current matching. A theorem that
checks (6.3) with cumulative \(\varepsilon=o(W)\) along a trajectory
proves (5.5). Separate Hall inequalities at individual depths do not.

## 7. Why an arbitrary-state proof is impossible

We record the obstruction at the scale relevant to (6.2). Choose a
constant \(\rho>0\) with \(G=\rho N_0+O(n)<N_J-n\). Fix an
entrance-legal packet \(e^*\). Choose \(S_0\) disjoint from \(e_0^*\),
and for \(1\le d\le J\) choose independently a uniform \(G\)-subset
\(S_d\subseteq V_d\).

For a fixed packet \(e\),

\[
 X_e=\sum_{d=1}^J|e_d\cap S_d|
\tag{7.1}
\]

has mean \(\Theta(nJ)\). Hypergeometric negative association and the
multiplicative Chernoff inequality give

\[
 \Pr(X_e<c nJ)\le e^{-c'nJ}.
\tag{7.2}
\]

There are only \((n-1)!/2\) ordinary packets, and

\[
 \log((n-1)!/2)=O(m\log m)=o(nJ).
\tag{7.3}
\]

Hence a union bound gives a deterministic choice with

\[
 X_e\ge c nJ=\Omega(m^{3/2})
 \quad\hbox{for every packet }e.
\tag{7.4}
\]

All depths are unsaturated, so (5.4) has no negative deep term. Every
legal packet, and hence every nonempty legal bite after serialization,
has loss \(\Omega(m^{3/2})\) per packet. Every separate rank is exactly
at its integer support floor.

These supports were selected independently and are not shown to have the
reachable form

\[
 S_d=\bigcup_{f\in\mathcal M}f_d
\tag{7.5}
\]

for one entrance matching. Therefore (7.4) is not a trajectory
counterexample. It proves that reachability is indispensable in (6.3):
rank sizes, separate floor balance, complete-catalogue degrees, and
unconditioned pair spread cannot establish the signed cut.

## 8. Exact remaining theorem

The whole-bite problem is now separated into two parts.

* The same-bite term is closed either exactly by serialization or
  quantitatively by Theorem 4.2. A slow diffuse implementation needs
  only \(\lambda_{\max}=o(1/J)\).
* The one-common-leave accounting is closed by (5.7); it contributes
  \(o(W)\) once, not once per rank.

The remaining assertion is the following reachable signed-profile
theorem:

> Construct a legal ordinary entrance-packet trajectory reaching
> \(L=O(N_0/\sqrt m)\) such that its reachable supports satisfy (6.3),
> with signed cumulative error \(o(W)\).

Equivalently, construct a terminal critical-leave entrance matching
\(\mathcal M_*\) with

\[
 \sum_{d=0}^J
 \left(\min\{n|\mathcal M_*|,N_d\}
       -\left|\bigcup_{e\in\mathcal M_*}e_d\right|\right)=o(W).
\tag{8.1}
\]

By Theorem 3.1, no choice of bite grouping, no omission of \(\chi\), and
no independent rank leave can weaken (8.1). A positive proof must use
the common-history reachability in (7.5); a negative proof must construct
an actual critical entrance matching or a reachable residual violating
the signed cut. This is the precise surviving boundary.
