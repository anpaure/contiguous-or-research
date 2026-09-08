# Joint near-rounding of the owner-memory circulation: run-compatible target tables, nested bonus menus, and the exact chronology gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad \mathcal M=\binom{[n]}m,\qquad
 W=|\mathcal M|=\binom{2m}m,
\]

and, for \(1\le q<m\),

\[
 N_q=\binom{2m}{m-q},\qquad
 W=c_qN_q+\rho_q,\qquad 0\le \rho_q<N_q.       \tag{0.1}
\]

An \(H\)-safe owner permutation has lower and upper traces

\[
 L_q(X)=\bigcap_{i=0}^qP^iX,\qquad
 U_q(X)=\bigcup_{i=0}^qP^iX.                     \tag{0.2}
\]

The same history must realize every \(q\le H\) and both signs. This note
proves the following statements.

1. **The common run arithmetic can be rounded jointly.** There is one
   balanced integer run vector \(R=(R_v)\), \(\sum_vR_v=W\), and, at
   every depth and both signs, nonnegative integral target-load tables
   with the exact point margins

   \[
   \sum_{S\ni v}\mu_q^-(S)=\frac W2-qR_v,\qquad
   \sum_{T\ni v}\mu_q^+(T)=\frac W2+qR_v.        \tag{0.3}
   \]

   For \(H=o(m)\), every load lies between \(c_q-1\) and \(c_q+2\),
   and the total signed floor deficit, ceiling excess, and number of
   holes are each at most

   \[
                         mH(H+1)=o(W).             \tag{0.4}
   \]

   Thus all depths use one run vector fixed in advance. The subsequent
   target-table transfers are still performed separately by depth; the
   joint conclusion is exactly the common point-margin compatibility, not
   chronology.

2. **This does not round chronology.** If one independently samples the
   symmetric wreath-window law at each root, then even the best possible
   hindsight deletion restoring memory conservation retains in expectation
   at most

   \[
                         \frac{W}{(m)_{H-1}^2}.    \tag{0.5}
   \]

   Consequently memory balance must be built from correlated cycles or
   interaction components from the outset.

3. **There is an exact joint forbidden-row calculus.** If \(D_q\) is the
   saturated lower bonus family and

   \[
   E_q=\{(S,x):S\in D_q,\ x\in S,\ S-x\notin D_{q+1}\},       \tag{0.6}
   \]

   then the union of all forbidden removal rows along one safe suffix is
   bounded by the final forbidden envelope plus the actual shadow defects
   in (0.6). Exact shadow nesting makes the forbidden rows pointwise
   nested and collapses an \(H\)-term union to one terminal envelope.

4. **Universal shadow nesting is impossible in the full Gaussian
   window.** Normalized bonus densities of a shadow-nested filtration are
   nondecreasing. At the first floor reset of \(W/N_q\), near

   \[
                  q=(\sqrt{\log2}+o(1))\sqrt m,                 \tag{0.7}
   \]

   the balanced bonus density falls from \(1-o(1)\) to \(o(1)\).
   Therefore every universally shadow-nested approximation pays at least

   \[
                         \left(\frac12-o(1)\right)W             \tag{0.8}
   \]

   on those two ranks. Approximate nesting instead has defect density
   \(1-o(1)\) there.

5. **Two positive joint menus survive.** Before the first reset, the
   pair-radius filtration gives shadow-nested, point-regular bonus
   envelopes with aggregate quota error \(o(W)\), expected joint
   row-plus-column union \((2+o(1))H^2\), and only \(o(W)\) shadow-lock
   exceptions for

   \[
                         H=o\!\left(\sqrt{m/\log m}\right).     \tag{0.9}
   \]

   For every fixed \(A\) and \(H\le A\sqrt m\), a clipped SCD-chain
   hash gives a stronger Gaussian-range Boolean menu with \(o_A(W)\)
   total quota error, normalized common-run point error, and adjacent
   shadow locks. For every fixed suffix, the random-label ensemble has
   exact row-survival law

   \[
    \Pr(a\hbox{ survives})=
    \prod_C\left(1-\max\{p_q:C_q(a)=C\}\right).                \tag{0.10}
   \]

   Hence a fixed one-chain flag survives with probability at least
   \(m^{-1/3}\) in that ensemble, while arbitrary flags may again suffer
   a product over many chains. No one deterministic labeling is proved to
   retain this density simultaneously for every suffix.

6. **The remaining sufficient gate package is explicit.** Neither menu is proved to lie in
   the fractional projection of the prescribed-profile \(H\)-memory
   circulation, still less in its integral projection. For an SCD
   predecessor map, the common-direction capacity satisfies

   \[
                         \sum_{x\in B}c_B(x)\le |B|,            \tag{0.11}
   \]

   so an arbitrary direction supplies only one coherent row on average.
   One must construct exceptional parent-aligned stars through all
   memories, or a different low-exposure packet theorem.

7. **Cycle economy is also integral.** The symmetric orbit-average of one
   length-\(2m\) wreath cycle has coefficient mass
   \(W/(2m)=o(W/H)\) for \(H=o(m)\), so the
   desired cycle count is fractionally compatible with every depth at
   once. But safe cycles of length \(2H+2\) can have injective traces at
   every protected depth. Thus local safety and local trace quality do
   not imply \(o(W/H)\) cycles.

The proved advance is therefore a joint all-depth target design and a
sharp reduction of the chronology obstruction. No owner permutation, no
literal contiguous-OR word, and no constant-one theorem is claimed.

## 1. The approximate integral memory problem

Let \(\Gamma_H\) be the safe length-\(H\) Johnson paths

\[
                 \gamma=(X_0,X_1,\ldots,X_H).                  \tag{1.1}
\]

Write \(\operatorname{pre}\gamma=(X_0,\ldots,X_{H-1})\) and
\(\operatorname{suf}\gamma=(X_1,\ldots,X_H)\). An integral partial
memory circulation is a vector \(z_\gamma\in\{0,1\}\) satisfying

\[
 \sum_{\gamma:X_0=X}z_\gamma\le1                              \tag{1.2}
\]

at every owner and

\[
 \sum_{\gamma:\operatorname{pre}\gamma=\sigma}z_\gamma
 =
 \sum_{\gamma:\operatorname{suf}\gamma=\sigma}z_\gamma       \tag{1.3}
\]

at every \((H-1)\)-memory. It decomposes into directed memory cycles.
The root constraint makes their owner sets disjoint. Put

\[
 \begin{aligned}
 L(z)&=W-\sum_\gamma z_\gamma,\\
 \ell_{q,S}^-(z)&=\sum_{\gamma:L_q(\gamma)=S}z_\gamma,\\
 \ell_{q,T}^+(z)&=\sum_{\gamma:U_q(\gamma)=T}z_\gamma,
 \end{aligned}                                                   \tag{1.4}
\]

and let \(\kappa(z)\) be the number of selected memory cycles. A strong
near-rounding target is

\[
 L(z)=o(W),\qquad
 \sum_{q,\pm,R}(c_q-\ell_{q,R}^{\pm}(z))_+=o(W),\qquad
 \kappa(z)=o(W/H).                                  \tag{1.5}
\]

Since \(c_q\ge1\), the middle term dominates the literal number of
uncovered signed targets.

### Proposition 1.1 (fractional cycle-economy compatibility)

There is a fractional packing of whole coordinate-wreath cycles \((x_C)\)
such that

\[
 \sum_{C\ni X}x_C=1                                             \tag{1.6}
\]

for every owner,

\[
 \sum_Cx_Ca_{q,R}^{\pm}(C)=\frac W{N_q}                         \tag{1.7}
\]

for every signed target and depth, and

\[
                         \sum_Cx_C=\frac W{2m}.                 \tag{1.8}
\]

Here \(a_{q,R}^{\pm}(C)\) is the number of rooted \(q\)-windows of
cycle \(C\) with target \(R\).

#### Proof

Fix one cyclic coordinate order and its single length-\(2m\) wreath
cycle. Average all coordinate conjugates of this cycle, with the common
weight normalized so that every owner has total incidence one. Coordinate
transitivity gives (1.6). Counting owner incidences gives

\[
                         2m\sum_Cx_C=W,
\]

which is (1.8), without any divisibility assumption on \(W\). At one
fixed signed depth, coordinate transitivity also makes every target have
one common average load. Its total is again \(W\), so that common load is
\(W/N_q\). This is (1.7). \(\square\)

Thus neither target coverage nor the desired cycle scale has a fractional
obstruction. Rounding (1.6)--(1.8) while retaining whole, owner-disjoint
cycles is the correlated integral problem.

## 2. One run vector supports all near-balanced target tables

### Theorem 2.1 (joint run-compatible marginal rounding)

Assume \(1\le H<m\) and

\[
 \binom{2m-2}{m-q-1}\ge2mq\qquad(1\le q\le H).                 \tag{2.1}
\]

There is one integer vector \(R=(R_v:v\in[n])\) with

\[
 R_v\in\left\{\left\lfloor\frac Wn\right\rfloor,
                  \left\lceil\frac Wn\right\rceil\right\},
 \qquad \sum_vR_v=W,                                           \tag{2.2}
\]

and, simultaneously for every \(q\le H\), nonnegative integral loads
\(\mu_q^-\) on rank \(m-q\) and \(\mu_q^+\) on rank \(m+q\) such that

\[
 \sum_S\mu_q^-(S)=\sum_T\mu_q^+(T)=W,                         \tag{2.3}
\]

the exact margins (0.3) hold, and

\[
                         c_q-1\le\mu_q^\pm\le c_q+2.           \tag{2.4}
\]

For each sign and depth,

\[
 \begin{aligned}
 \sum_R(c_q-\mu_q^\pm(R))_+&\le mq,\\
 \sum_R(\mu_q^\pm(R)-c_q-1)_+&\le mq.
 \end{aligned}                                                   \tag{2.5}
\]

In particular, each sign has at most \(mq\) holes, and summing both
signs through \(H\) gives (0.4).

#### Proof

Write \(W=nr+s\), \(0\le s<n\), choose a fixed \(s\)-set \(D\), and put

\[
 R_v=\begin{cases}r+1,&v\in D,\\r,&v\notin D.\end{cases}       \tag{2.6}
\]

Fix \(q\), put \(k=m-q\), and define the residual degree forced above
the \(c_q\)-baseline by

\[
 a_{q,v}=\frac W2-qR_v-c_q\binom{n-1}{k-1}.                    \tag{2.7}
\]

This is integral, because
\(W/2=\binom{2m-1}{m-1}\). Since
\(\binom{n-1}{k-1}=kN_q/n\),

\[
 a_{q,v}=\frac{k\rho_q}{n}
          -q\left(R_v-\frac Wn\right),                         \tag{2.8}
\]

and hence

\[
 \sum_va_{q,v}=k\rho_q,
 \qquad
 \left|a_{q,v}-\frac{k\rho_q}{n}\right|<q                    \tag{2.9}
\]

unless \(s=0\), in which case the difference is zero.

We use the following elementary design lemma. For every
\(0\le t\le\binom nk\), there is a simple family \(\mathcal F\) of
exactly \(t\) distinct \(k\)-sets whose point degrees are the two nearest
integers to \(kt/n\). Indeed, minimize \(\sum_vd_v^2\) over all such
families. If \(d_u\ge d_v+2\), some edge containing \(u\) and not \(v\)
can be switched from \(u\) to \(v\) without duplicating an edge; otherwise
the switch map injects all \(u\)-not-\(v\) edges into the
\(v\)-not-\(u\) edges, contradicting the degree difference. The switch
strictly lowers the quadratic energy. Thus all degrees differ by at most
one.

Apply the lemma with \(t=\rho_q\), and write its degrees as \(d_v\). Put

\[
                         e_v=d_v-a_{q,v}.                         \tag{2.10}
\]

Then \(e_v\) is integral, \(\sum_ve_v=0\), and \(|e_v|\le q\). Therefore

\[
 T_q:=\sum_{e_v>0}e_v=\frac12\sum_v|e_v|\le mq.                \tag{2.11}
\]

Start with the genuine floor/ceiling table

\[
                         \lambda(S)=c_q+\mathbf1_{\{S\in\mathcal F\}}.   \tag{2.12}
\]

Pair the \(T_q\) surplus coordinate units \(e_u>0\) with the deficit
units \(e_v<0\). For a pair \((u,v)\), choose a \(k\)-set \(S\) with
\(u\in S\), \(v\notin S\), and transfer one load unit

\[
                         S\longmapsto S-u+v.                      \tag{2.13}
\]

There are \(\binom{n-2}{k-1}\) possible sources. Choose greedily so that
all source and recipient sets in all \(T_q\) transfers are distinct. At
step \(t\), fewer than \(2(t-1)\) endpoint sets are forbidden, and each
forbids at most one candidate source or its unique inverse recipient.
Condition (2.1) leaves a choice.

Every source initially has load at least \(c_q\ge1\), so the final table
is nonnegative. Endpoint disjointness gives the pointwise range (2.4).
The transfers change the residual point vector from \(d\) to \(a_q\),
proving the lower identity in (0.3). Each transfer creates at most one
floor-deficit unit and at most one ceiling-excess unit, proving (2.5).

Define the upper loads by literal complementation,

\[
                         \mu_q^+(T)=\mu_q^-([n]\setminus T).     \tag{2.14}
\]

Then

\[
 \sum_{T\ni v}\mu_q^+(T)
 =W-\sum_{S\ni v}\mu_q^-(S)
 =\frac W2+qR_v.                                                \tag{2.15}
\]

All error bounds are unchanged. Summing \(2mq\) over \(q\le H\) proves
(0.4). \(\square\)

For \(H=o(m)\), (2.1) holds eventually: the smallest left side is
\(\binom{2m-2}{m-H-1}=\exp((\log4-o(1))m)\), while the right side is
polynomial. Also \(mH(H+1)=o(W)\). The endpoint \(q=m\) is genuinely
excluded: the lower layer consists only of the empty set and no Johnson
degree transfer is available.

### Boundary of Theorem 2.1

The tables in Theorem 2.1 satisfy every total and point constraint forced
by one common run vector. They do not satisfy the cocycle identities,
the overlap-memory equations, or any owner-root equation. They need not
even lie in the fractional target projection of the memory polytope.
Thus Theorem 2.1 removes the arithmetic obstruction and nothing stronger.

## 3. Independent per-root rounding cannot be repaired

Assume \(1\le H\le m\), and write
\((m)_r=m(m-1)\cdots(m-r+1)\). Conditioned on a root \(X\), the symmetric
wreath-window law is obtained
by choosing independent uniform orders

\[
 (a_1,\ldots,a_m)\text{ of }X,
 \qquad
 (b_1,\ldots,b_m)\text{ of }X^c,                               \tag{3.1}
\]

and setting

\[
 X_i=X\setminus\{a_1,\ldots,a_i\}
       \cup\{b_1,\ldots,b_i\}.                                 \tag{3.2}
\]

Sample one such \(H\)-window \(\gamma_X\) independently at every root.

### Theorem 3.1 (memory entropy obstruction)

Let \(\mathcal A\) be any subcollection, chosen after all samples are
visible, which satisfies every memory-balance equation. Then

\[
 \mathbb E\max_{\mathcal A}|\mathcal A|
 \le\frac{W}{(m)_{H-1}^2}.                                      \tag{3.3}
\]

Consequently, for every \(\eta>0\),

\[
 \Pr\left(\max_{\mathcal A}|\mathcal A|\ge\eta W\right)
 \le\frac1{\eta(m)_{H-1}^2}.                                   \tag{3.4}
\]

#### Proof

Let \(Y=X_1\). If \(\gamma_X\) is retained, its suffix memory can only
be balanced by the unique sampled edge rooted at \(Y\). That edge must
begin with \((X_1,\ldots,X_H)\). Conditional on \(\gamma_X\), this fixes
the first \(H-1\) deletion letters of \(\gamma_Y\) to be
\((a_2,\ldots,a_H)\), and similarly fixes its first \(H-1\) addition
letters. The exact probability is

\[
                         ((m)_{H-1})^{-2}.                         \tag{3.5}
\]

Let \(I_X\) indicate this compatibility. Deterministically every retained
root has \(I_X=1\), even when \(\mathcal A\) is selected adversarially
after sampling. Hence

\[
                         |\mathcal A|\le\sum_XI_X.               \tag{3.6}
\]

Take expectations and apply Markov's inequality. \(\square\)

More generally, for independent root laws \(\nu_Y\), put

\[
 \eta_0=\max_{Y,\sigma}
 \nu_Y\{\gamma_Y:\operatorname{pre}\gamma_Y=\sigma\}.          \tag{3.7}
\]

The same proof gives
\(\mathbb E\max|\mathcal A|\le\eta_0W\). This is why an Eulerian repair
after independent discrepancy rounding cannot work.

## 4. Exact nested-family calculus on one safe suffix

Let a safe suffix end at \(X_0\). Write its recent insertion word as
\(b_1,\ldots,b_{H-1}\), backwards from the endpoint, and put

\[
 I_{q-1}=X_0\setminus\{b_1,\ldots,b_{q-1}\}.                    \tag{4.1}
\]

The common eligible removal rows form \(A=I_{H-1}\), of size
\(m-H+1\). For \(a\in A\), the new lower target is

\[
 T_q(a)=I_{q-1}-a,
 \qquad
 T_{q+1}(a)=T_q(a)-b_q.                                         \tag{4.2}
\]

Let \(D_q\subseteq\binom{[n]}{m-q}\) be the saturated lower bonus
family, and define

\[
 R_q=\{a\in A:T_q(a)\in D_q\},                                 \tag{4.3}
\]

\[
 E_q=\{(S,x):S\in D_q,\ x\in S,\ S-x\notin D_{q+1}\},        \tag{4.4}
\]

\[
 \alpha_q=\frac{|D_q|}{N_q},\qquad
 e_q=\frac{|E_q|}{(m-q)N_q}.                                   \tag{4.5}
\]

### Theorem 4.1 (joint row union with shadow defects)

Pointwise on every safe suffix,

\[
 \boxed{
 |\bigcup_{q\le H}R_q|
 \le |R_H|+
 \sum_{q<H}\#\{a\in A:(T_q(a),b_q)\in E_q\}.}                 \tag{4.6}
\]

On a uniform relative coordinate orbit of suffixes,

\[
 \boxed{
 \mathbb E|\bigcup_{q\le H}R_q|
 \le(m-H+1)\left(\alpha_H+\sum_{q<H}e_q\right).}              \tag{4.7}
\]

Moreover,

\[
                         e_q\ge(\alpha_q-\alpha_{q+1})_+.       \tag{4.8}
\]

#### Proof

If a row belongs to some \(R_q\) but not to \(R_H\), it has a last
transition from forbidden to allowed. At such a transition (4.2) is an
edge of \(E_q\). This proves (4.6).

By coordinate symmetry, \(T_H(a)\) is uniform on its target layer, so
\(\mathbb E|R_H|=(m-H+1)\alpha_H\). Likewise the incidence
\((T_q(a),b_q)\) is uniform over the \((m-q)N_q\) pointed rank-
\((m-q)\) targets. Therefore the expectation of the \(q\)-th defect term
is exactly \((m-H+1)e_q\), proving (4.7).

Finally, the \((m-q)|D_q|\) shadow incidences from \(D_q\) can land in
\(D_{q+1}\) at most \((m+q+1)|D_{q+1}|\) times. Subtract and use

\[
                         N_{q+1}=N_q\frac{m-q}{m+q+1}            \tag{4.9}
\]

to get (4.8). \(\square\)

The upper-column statement is the exact complement. If
\(\partial D_q\subseteq D_{q+1}\), then \(E_q=\varnothing\), the sets
\(R_q\) are pointwise nested, and their entire union is \(R_H\).

## 5. Floor resets rule out universal hereditary bonuses

Let

\[
 \lambda_q=\frac W{N_q},\qquad
 \theta_q=\lambda_q-\lfloor\lambda_q\rfloor.                    \tag{5.1}
\]

The balanced bonus family at depth \(q\) has normalized density
\(\theta_q\). The exact increment is

\[
 \lambda_{q+1}-\lambda_q
 =\lambda_q\frac{2q+1}{m-q}.                                   \tag{5.2}
\]

### Theorem 5.1 (hereditary floor-reset obstruction)

Suppose \(D_q\) and \(D_{q+1}\) satisfy
\(\partial D_q\subseteq D_{q+1}\). At an integer crossing
\(\lambda_q<c\le\lambda_{q+1}\), where \(q=O_A(\sqrt m)\) and
\(c\) is fixed,

\[
 \begin{aligned}
 &N_q\left|\frac{|D_q|}{N_q}-\theta_q\right|
 +N_{q+1}\left|\frac{|D_{q+1}|}{N_{q+1}}-\theta_{q+1}\right|\\
 &\hspace{35mm}\ge\left(\frac1c-o_A(1)\right)W.                \tag{5.3}
 \end{aligned}
\]

At the first crossing \(c=2\), this is (0.8). If the two cardinal errors
are instead \(o(W)\), then their shadow-defect density obeys

\[
                         e_q\ge1-o(1).                            \tag{5.4}
\]

#### Proof

Shadow inclusion and (4.9) give \(\alpha_q\le\alpha_{q+1}\). Equation
(5.2) is \(O_A(m^{-1/2})\) at a fixed Gaussian crossing, so

\[
 \theta_q=1-O_A(m^{-1/2}),\qquad
 \theta_{q+1}=O_A(m^{-1/2}),\qquad
 N_q,N_{q+1}=(c^{-1}+o_A(1))W.                                  \tag{5.5}
\]

For \(x\le y\),

\[
                         |x-1|+|y-0|\ge1.                        \tag{5.6}
\]

Equations (5.5)--(5.6) give (5.3). If the cardinal errors are \(o(W)\),
then \(\alpha_q-\alpha_{q+1}=1-o(1)\), and (4.8) gives (5.4).
\(\square\)

Since \(\lambda_{\lfloor A\sqrt m\rfloor}\to e^{A^2}\), the first
crossing lies at (0.7). Thus one globally shadow-nested bonus filtration
cannot handle all fixed \(A\).

## 6. Positive menu I: pair-radius envelopes before the reset

Partition the coordinates into \(m\) unordered pairs. For a set \(T\),
let \(d(T)\) be the number of pairs wholly contained in \(T\). If
\(|T|=m-q\), then

\[
 \Pr(d(T)=d)
 =\frac{m!\,2^{m-q-2d}}
 {d!\,(q+d)!\,(m-q-2d)!\,N_q}.                                 \tag{6.1}
\]

Deleting a coordinate never increases \(d\). Hence families

\[
                         \mathcal H_q^-={T:d(T)\le r_q\}       \tag{6.2}
\]

are shadow-nested whenever \(r_q\) is nondecreasing; upper families are
their complements.

### Theorem 6.1 (audited pair-radius filtration)

If

\[
                         H=o\!\left(\sqrt{m/\log m}\right),     \tag{6.3}
\]

there are nondecreasing integer thresholds \(r_q\) for which

\[
 \sum_{q\le H}\left||\mathcal H_q^-|-(W-N_q)\right|=o(W),      \tag{6.4}
\]

and the same holds above. The families are exactly point-regular. On a
uniform relative coordinate orbit,

\[
 \mathbb E\left(
 |\bigcup_qR_q|+|\bigcup_qC_q|\right)
 \le(2+o(1))H^2.                                                \tag{6.5}
\]

The total two-sign transition-band locks are at most

\[
                         (2+o(1))\frac{WH^2}{m}+o(W)=o(W),      \tag{6.6}
\]

and outside those bands and an exponentially small tail, every demanded
target has at least \((m-q)/4\) unsaturated shadow exits.

#### Proof audit

The ratio of adjacent masses in (6.1) is

\[
 \frac{A_{q,d+1}}{A_{q,d}}
 =\frac{(m-q-2d)(m-q-2d-1)}{4(d+1)(q+d+1)},                    \tag{6.7}
\]

so the law is log-concave. Its lower-tail atom-to-tail ratio at probability
between \(m^{-1}\) and \(o(1)\) is
\(O(\sqrt{\log m/m})\): if the quantile is \(t\) below the mode, ratio
products give \(t=O(\sqrt{m\log m})\), and the preceding
\(\Omega(m/(t+\sqrt m))\) atoms stay within a constant factor of the
boundary atom. The exact uniform-deletion coupling is

\[
 F_{q+1}(r)=F_q(r)+\Pr(d(T)=r+1)\frac{2(r+1)}{m-q}.             \tag{6.8}
\]

In this pre-reset range \(\theta_q=W/N_q-1\), and

\[
 \theta_{q+1}-\theta_q
 =(1+\theta_q)\frac{2q+1}{m-q}.                                \tag{6.9}
\]

this makes the least quota quantiles nondecreasing under (6.3). Their
aggregate overshoot is

\[
 O\!\left(W\frac{H^3\sqrt{\log m}}{m^{3/2}}\right)=o(W).       \tag{6.10}
\]

Theorem 4.1 then reduces the row union to the terminal density
\((1+o(1))H^2/m\), proving (6.5). The exact lock classification is

\[
 r_q<d(T)\le r_{q+1},                                           \tag{6.11}
\]

plus the no-singleton-pair boundary. More precisely, the ordinary band
has normalized size

\[
 F_q(r_{q+1})-F_q(r_q)
 \le \theta_{q+1}-\theta_q
 +O\!\left(\theta_{q+1}\sqrt{\frac{\log m}{m}}\right).          \tag{6.12}
\]

Summing (6.12), using \(N_q\le W\), and adding the exponentially small
no-singleton tail gives (6.6). Thus the bands telescope, and
outside them deleting any singleton-pair coordinate is an escape. This
proves the theorem. \(\square\)

This theorem is a target-menu theorem only. Point regularity verifies the
rational common-run line, but the integer correction inside the same
envelopes and the prescribed-profile fractional memory circulation are
not proved.

## 7. Positive menu II: clipped SCD hashing at Gaussian depth

Fix \(A<\infty\), \(H\le A\sqrt m\), and

\[
                         \epsilon=m^{-1/3},\qquad
 p_q=\min\{\theta_q,1-\epsilon\}.                               \tag{7.1}
\]

Fix a symmetric chain decomposition of the Boolean lattice, attach one
independent uniform label \(U_C\) to every chain, and define

\[
 \mathcal B_q^-=
 \{S\in\tbinom{[n]}{m-q}:U_{C(S)}\le p_q\},
 \qquad
 \mathcal B_q^+=\{[n]\setminus S:S\in\mathcal B_q^-\}.        \tag{7.2}
\]

### Theorem 7.1 (clipped SCD-chain menu)

There is one deterministic choice of the chain labels for which:

\[
 \sum_{q\le H,\pm}
 \left||\mathcal B_q^\pm|-\rho_q\right|=o_A(W),                \tag{7.3}
\]

the normalized all-depth point discrepancy from one balanced common run
line is \(o_A(W)\), meaning, with \(\delta_v=R_v-W/n\),

\[
 \begin{aligned}
 &\sum_{q,v}\frac1{m-q}
 \left|h_{q,v}^--\left(\frac{(m-q)\rho_q}{n}-q\delta_v\right)\right|\\
 &\quad+\sum_{q,v}\frac1{m+q}
 \left|h_{q,v}^+-\left(\frac{(m+q)\rho_q}{n}+q\delta_v\right)\right|
 =o_A(W),                                                       \tag{7.3a}
 \end{aligned}
\]

and the total number of lower and upper adjacent-depth shadow locks is
\(o_A(W)\).

For every fixed safe suffix and removal row \(a\), if \(C_q(a)\) is the
SCD chain containing its depth-\(q\) target, then the random-label
ensemble has exact survival law (0.10). This probability identity is not
a simultaneous row guarantee for the deterministic labeling selected by
the first-moment argument.

#### Proof

The exact increment (5.2) is \(\Theta_A(m^{-1/2})\) near every fixed
integer crossing. There are \(O_A(1)\) crossings and at most
\(O_A(1+\epsilon\sqrt m)\) clipped depths before each. Therefore

\[
 \sum_{q\le H}N_q(\theta_q-p_q)
 =O_A(W(\epsilon^2\sqrt m+\epsilon))
 =O_A(Wm^{-1/6}).                                               \tag{7.4}
\]

At one rank, different sets occupy different SCD chains. Hence
\(|\mathcal B_q^-|\) is binomial with parameters \((N_q,p_q)\), and the
degree of a fixed coordinate is binomial with parameters
\((\binom{n-1}{m-q-1},p_q)\). The elementary bound
\(\mathbb E|Z-\mathbb EZ|\le\sqrt{\operatorname{Var}Z}\), summed over
all \(q\) and coordinates and normalized by target rank, gives

\[
 O_A(H\sqrt W)+O_A(Wm^{-1/6})+O_A(H^2)=o_A(W).                  \tag{7.5}
\]

This proves the cardinal and point statements by the probabilistic
method.

The facets of a fixed target lie in distinct SCD chains, and at most one
facet shares the target's own chain. A lower target can be locked only if
the remaining \(m-q-1\) independent labels are all at most
\(p_{q+1}\le1-\epsilon\). Thus

\[
 \mathbb E L_q^-\le N_q(1-\epsilon)^{m-q-1}.                    \tag{7.6}
\]

The same holds above, and their sum is
\(O(HW\exp(-\epsilon(m-H-1)))=o_A(W)\). Include this nonnegative
quantity in the probabilistic-method objective.

Finally, all depths at which row \(a\) visits one fixed chain \(C\) are
simultaneously allowed exactly when

\[
                         U_C>\max\{p_q:C_q(a)=C\}.               \tag{7.7}
\]

Distinct chain labels are independent, so multiplying (7.7) proves
(0.10). \(\square\)

The nested intervals \([0,p_q]\) are optimal on one chain because the
union of measurable subsets with measures \(p_q\) has measure at least
\(\max p_q\). If one row visits one chain, its survival probability is at
least \(\epsilon\). If it visits many high-threshold chains, the product
in (0.10) may be tiny. These are ensemble statements for a fixed row;
selecting one labeling that also works on every eventually chosen history
is part of the chronology gate.

The menu can also be corrected to exact totals and exact common-run point
margins using only \(o_A(W)\) exceptional target-load units. To see this
without importing a hidden realization claim, include in the
probabilistic-method objective the raw centered degree error

\[
 \sum_{q,v}\left|h_{q,v}^--\frac{m-q}{n}|\mathcal B_q^-|\right|.
                                                                    \tag{7.8}
\]

Its expectation is \(O_A(mH\sqrt W)=o(W)\). At depth \(q\), first add or
remove \(\bigl|\rho_q-|\mathcal B_q^-|\bigr|\) units on a nearly regular simple
family so that the total bonus mass becomes \(\rho_q\). The aggregate
number of these changes is \(o_A(W)\) by (7.3). The remaining point-error
vector is integral, has sum zero, and has aggregate \(L^1\)-norm
\(o_A(W)\) by (7.8), the degree-spread-one lemma, and
\(|R_v-W/n|\le1\). Pair its positive and negative units and use the
Johnson transfers (2.13). Uniformly for \(q\le A\sqrt m\),

\[
 \binom{n-2}{m-q-1}=\Theta_A(W),                                \tag{7.9}
\]

whereas the number of remaining transfers is in fact
\(O_A(mH\sqrt W+mH^2)=o(W)\), so the transfers can be endpoint-disjoint.
At each fixed Gaussian depth the source pool has size \(\Theta_A(W)\);
the \(o_A(W)\) targets touched by the total-mass correction may therefore
also be avoided whenever they have become zero. Thus every transfer has a
positive source and the corrected table remains nonnegative.
Complementation supplies the upper table.

This is still only an arithmetic target-load ledger. The exceptional
changes need not preserve the menu's fibrewise shadow escape, and the
corrected tables are not shown to lie in the memory projection.

## 8. The exact SCD coherence capacity

Let \(p(S)\) be the predecessor of \(S\) in the fixed SCD when it exists.
For \(B\in\binom{[n]}{k+1}\), define

\[
 c_B(x)=\#\{a\in B\setminus\{x\}:
            p(B-a)=B-\{a,x\}\}.                                \tag{8.1}
\]

### Proposition 8.1 (one coherent row per average direction)

For every \(B\),

\[
                         \sum_{x\in B}c_B(x)\le k+1.            \tag{8.2}
\]

#### Proof

For a fixed row \(a\), the set \(B-a\) has at most one SCD predecessor.
If that predecessor lies inside \(B\), it determines a unique coordinate
\(x\). Thus each of the \(k+1\) rows contributes to at most one summand.
\(\square\)

An exceptional direction can have \(c_B(x)=\Theta(m)\), but (8.2) gives
no positive-density supply of such directions. Coherence through all
\(H\) memories requires the same row to satisfy the predecessor identity
repeatedly. This exceptional-star concatenation is the exact constructive
gate left by Theorem 7.1.

There is no nonconstant SCD label conserved along every Boolean deletion
edge in the central band. The incidence graph of two consecutive complete
ranks is connected; after contracting within-chain edges it remains
connected. A label conserved on every deletion edge is therefore constant
and yields only empty or full threshold families. The coherence must be
packet-specific.

## 9. Additive and coordinate hashes: exact obstruction formulas

Let \(G\) be an abelian group, give coordinate \(v\) weight \(w_v\), and
put \(h(S)=\sum_{v\in S}w_v\). For bonus intervals \(J_q\subseteq G\),
the exact forbidden-row formula is

\[
 R_q=\{a\in A:w_a\in h(I_{q-1})-J_q\},                          \tag{9.1}
\]

while

\[
                         h(I_q)=h(I_{q-1})-w_{b_q}.              \tag{9.2}
\]

Thus nested intervals at the origin do not imply nested translated row
sets. Along one fixed suffix, the sufficient alignment condition is

\[
                         J_q-w_{b_q}\subseteq J_{q+1}.           \tag{9.3}
\]

If \(\Xi\subseteq G\) is the set of attainable next-insertion weights and
one demands (9.3) for every \(\xi\in\Xi\), then, with
\(J_q-\Xi:=\bigcup_{\xi\in\Xi}(J_q-\xi)\),

\[
                         J_q-\Xi\subseteq J_{q+1}.               \tag{9.4}
\]

Over \(\mathbb Z_p\), repeated Cauchy--Davenport gives

\[
 |J_{q+t}|\ge
 \min\{p,\ |J_q|+t(|\Xi|-1)\}.                                \tag{9.5}
\]

Necessity of (9.4) requires the corresponding rankwise subset-sum
attainability; it must not be inferred from the hash labels alone. Under
that attainability, a high-entropy coordinate hash fills the interval
rapidly. A constant hash avoids the expansion but is constant on every
rank and cannot encode a nontrivial bonus fraction.

A lexicographic hash on \(d\) marked coordinates can align rows inside
one floor block, but it has an exact all-or-few link dichotomy. If
\(\chi(S)=\sum_{i\le d}2^{i-1}\mathbf1_{\{v_i\in S\}}\) and
\(D_q=\{S:\chi(S)\le t_q\}\), then for an
upper memory \(I\), either every unmarked deletion is forbidden or only
the \(d\) marked deletions can be forbidden. Across a suffix, with
\(s_{q-1}=\chi(\{b_1,\ldots,b_{q-1}\})\) and

\[
                         \tau=\max_q(t_q+s_{q-1}),               \tag{9.6}
\]

all unmarked rows are forbidden at some depth exactly when
\(\chi(X_0)\le\tau\); otherwise at most \(d\) rows are forbidden.
This is maximal alignment but maximal link concentration.

Thus this elementary coordinate hash converts the union problem into an
all-or-few link distribution rather than a diffuse Hall supply. Without a
separate quantile-and-rank-drift estimate it gives no Gaussian shadow-lock
bound, and none is claimed here. The SCD-chain hash instead spreads the
facets over independent chains at the menu level, but then exposes the
coherence product (0.10).

## 10. Local trace quality permits short-cycle fractional support

Fix \(H<w\le m\), a set \(I\) of size \(m-w\), and a cyclically ordered
\(2w\)-set \(z_0,\ldots,z_{2w-1}\), disjoint from \(I\). Put

\[
                         X_t=I\cup\{z_t,\ldots,z_{t+w-1}\}.     \tag{10.1}
\]

Then \((X_t)_{t\in\mathbb Z_{2w}}\) is an \(H\)-safe owner cycle, and

\[
 \begin{aligned}
 L_q(X_t)&=I\cup\{z_{t+q},\ldots,z_{t+w-1}\},\\
 U_q(X_t)&=I\cup\{z_t,\ldots,z_{t+w+q-1}\}.
 \end{aligned}                                                    \tag{10.2}
\]

For every \(q\le H\), both target maps in (10.2) are injective in \(t\).
When \(H<m\), taking \(w=H+1\) gives cycles of length \(2H+2\). Averaging all coordinate
conjugates and normalizing root load gives a symmetric fractional
circulation with exact target load \(W/N_q\) at every signed depth, but
fractional cycle mass

\[
                         \frac{W}{2H+2}=\Theta(W/H).             \tag{10.3}
\]

Thus exact symmetric fractional target balance, safety, and within-cycle
injectivity admit a representation supported entirely on short cycles.
The coefficient sum in (10.3) is a property of this fractional
representation, not the component count of an integral circulation, and
it does not preclude a different long-cycle representation. Proposition
1.1 shows that the desired coefficient scale is also available
fractionally on length-\(2m\) wreath cycles. An integral rounding must
select the long-cycle support from the outset or supply a genuinely global
fusion packet.

Pairwise trace-neutral fusion is already impossible at depth one. The
intersection and union colors \((S,T)\), with \(|S|=m-1\), \(|T|=m+1\),
uniquely determine an undirected Johnson edge. If two vertex-disjoint
edges were head-swapped while preserving both two-element color
multisets, a nontrivial reassignment would have to change their incidences
from

\[
                         (S_1,T_1),(S_2,T_2)
\]

to

\[
                         (S_1,T_2),(S_2,T_1).
\]

If either the two lower colors or the two upper colors were equal, the
crossed incidence multiset would equal the uncrossed one; uniqueness of
the edge belonging to a fixed \((S,T)\) pair and vertex-disjointness would
then make the reassignment trivial. Thus in the nontrivial case
\(S_1\ne S_2\) and \(T_1\ne T_2\). All four containments now give

\[
 |S_1\cup S_2|\ge m,\qquad |T_1\cap T_2|\le m,
\]

and force

\[
                         S_1\cup S_2=T_1\cap T_2
\]

to be a common middle owner of both old edges: for every incidence
\((S_i,T_j)\), its unique Johnson edge has \(S_1\cup S_2\) as one of its
two middle endpoints. In particular both old edges contain that endpoint,
contradicting vertex disjointness. Hence exact neutral fusion requires at
least three cuts and must cancel all depths in one common seam choice. No
three-cut packet is asserted to exist, and this does not rule out an
approximate two-cut trade with explicitly charged loss.

## 11. Exact proved and conditional boundary

The following are proved.

1. One balanced integer run vector admits simultaneous signed target-load
   tables with exact point margins and only \(O(mH^2)=o(W)\) aggregate
   deficit/excess.
2. Independent sampling from the symmetric wreath-window law followed by
   optimal Eulerian deletion retains only the fraction in (0.5); for a
   different root law the general bound is its largest memory-prefix atom.
3. The exact shadow-defect formula (4.6)--(4.8) controls the union of all
   forbidden rows without separating depths.
4. Pair-radius envelopes solve that row-union problem up to
   \(H=o(\sqrt{m/\log m})\), with \(o(W)\) lock exceptions.
5. For every fixed Gaussian constant \(A\), clipped SCD hashing produces
   one all-depth, two-sign near-quota menu with \(o_A(W)\) cardinal,
   normalized point, and shadow-lock error.
6. Universal hereditary nesting is ruled out by the exact floor-reset
   cost, and additive hashes are governed by the history translations in
   (9.1)--(9.5).
7. The fractional system simultaneously admits exact target balance and
   \(W/(2m)\) cycle mass.

The following are unproved and are not consequences of the preceding
theorems.

1. No prescribed pair-radius or SCD-hash profile is shown to lie in the
   fractional projection of the \(H\)-memory circulation. Uniform
   fractional target loads do not imply this.
2. No integral owner circulation is constructed. In particular, the
   semigroup/cocycle identities and all memory-overlap equations remain.
3. The \(o(W)\) arithmetic corrections to a menu need not preserve its
   fibrewise shadow escape.
4. No theorem produces enough parent-aligned SCD stars to make the
   weighted exposure product (0.10) large at every selected history.
5. No integral theorem preserves the fractional \(W/(2m)\) cycle scale,
   and no higher neutral seam packet is constructed.

Therefore the following is a sufficient next gate, not a proved
equivalence:

> Construct a correlated integral packing of long safe owner cycles whose
> target flags have low weighted SCD-chain exposure, or prove that the
> parent-alignment capacity (8.2) forces \(\Omega(W)\) aggregate target
> loss. The construction and the obstruction must use all depths and both
> signs in the same memory state.

This is strictly narrower than the former independent quota-rounding
problem, but it is still the unproved chronology step required for a
literal constant-one contiguous-OR construction.
