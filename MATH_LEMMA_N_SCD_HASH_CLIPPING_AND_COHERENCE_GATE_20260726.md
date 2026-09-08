# Clipped SCD-chain quota hashing: joint run compatibility, negligible shadow locks, and the exact coherence gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## 0. Result and boundary

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 \lambda_q={W\over N_q},                           \tag{0.1}
\]

and write

\[
 \lambda_q=c_q+\theta_q,\qquad
 c_q=\lfloor\lambda_q\rfloor,\qquad
 0\leq\theta_q<1,\qquad r_q=\theta_qN_q.          \tag{0.2}
\]

Thus an exactly balanced depth-\(q\) histogram has baseline \(c_q\)
and a Boolean bonus family of cardinality \(r_q\).

Fix \(A<\infty\) and let \(H\leq A\sqrt m\). There is a single joint
choice of lower and upper bonus families through all depths \(q\leq H\)
with the following properties.

1. The total cardinal error from the exact bonus quotas is \(o_A(W)\).
2. The lower and upper point degrees obey the common run-vector affine
   line up to normalized total error \(o_A(W)\).
3. The total number of adjacent-depth shadow-locked targets is \(o_A(W)\).
4. If the target flag of a candidate removal row stays in one chain of a
   fixed symmetric chain decomposition, that row survives every depth
   with probability at least
   \[
                         \epsilon=m^{-1/3}.         \tag{0.3}
   \]

The construction first clips every bonus density at \(1-\epsilon\), then
uses one uniform hash on each SCD chain and the nested hash intervals
\([0,p_q]\). The clipping loss is

\[
 \sum_{q\leq H}N_q(\theta_q-p_q)
 =O_A\!\left(W(\epsilon^2\sqrt m+\epsilon)\right)
 =O_A(Wm^{-1/6})=o_A(W).                            \tag{0.4}
\]

This is a genuine all-depth near-quota construction. In particular, the
common run-vector arithmetic and the shadow-lock cut do not obstruct the
SCD-hash menu asymptotically.

There remains an exact, non-arithmetic gate. Along an arbitrary safe
suffix the target flag generally changes SCD chains. If
\(C_q(a)\) is the chain occupied at depth \(q\), then the exact
all-depth row survival probability is

\[
 \prod_C\left(1-\max\{p_q:C_q(a)=C\}\right).       \tag{0.5}
\]

Thus one chain gives survival at least \(\epsilon\), whereas many chain
changes can restore the product loss which the construction was meant to
avoid. This is not a cosmetic defect. For every SCD predecessor map and
every \((k+1)\)-set \(B\), if

\[
 c_B(x)=\#\{a\in B\setminus\{x\}:
 p(B-a)=B-\{a,x\}\},                               \tag{0.6}
\]

then

\[
                         \sum_{x\in B}c_B(x)\leq k+1.           \tag{0.7}
\]

So the average common deletion direction has at most one SCD-coherent
row. A construction must deliberately find and concatenate exceptional
parent-aligned stars; the SCD filtration alone does not supply them.

Finally, a universally hereditary target filtration cannot replace this
packet-specific coherence. Once the window crosses the first floor jump
\(\lambda_q=2\), every deletion-hereditary approximation to the exact
bonus densities has \(\Omega(W)\) two-level error. Hence the proved
construction is the strongest conclusion here: it gives a jointly
compatible bonus design and identifies the exact remaining coherence
gate, but it does not construct the required owner permutation, Hall
transversal, or small-cycle factor.

## 1. Clipping the near-integer peaks costs only \(o(W)\)

Let \(0<\epsilon<1/4\), and define

\[
                         p_q=\min\{\theta_q,1-\epsilon\}.        \tag{1.1}
\]

The exact adjacent ratio is

\[
 {\lambda_{q+1}\over\lambda_q}
 ={N_q\over N_{q+1}}
 ={m+q+1\over m-q},                                 \tag{1.2}
\]

and hence

\[
 \lambda_{q+1}-\lambda_q
 =\lambda_q{2q+1\over m-q}.                         \tag{1.3}
\]

Also

\[
 \lambda_q
 =\prod_{i=1}^q\left(1+{q\over m-q+i}\right),
 \qquad
 \log\lambda_q\leq {q^2\over m-q+1}.              \tag{1.4}
\]

### Lemma 1.1 (peak-clipping bound)

For every fixed \(A\), uniformly for \(H\leq A\sqrt m\),

\[
 \boxed{
 \sum_{q\leq H}N_q(\theta_q-p_q)
 \leq C_AW(\epsilon^2\sqrt m+\epsilon).}           \tag{1.5}
\]

#### Proof

Clipping occurs only if, for some integer \(\ell\geq2\),

\[
                         \ell-\epsilon<\lambda_q<\ell.         \tag{1.6}
\]

There are only \(O_A(1)\) possible integers \(\ell\), because (1.4)
bounds \(\lambda_q\) by a constant depending only on \(A\).

On (1.6), \(\lambda_q\geq 7/4\). Equation (1.4) then implies
\(q\geq c_A\sqrt m\). Together with (1.3), this gives

\[
 {c_A\over\sqrt m}
 \leq\lambda_{q+1}-\lambda_q
 \leq {C_A\over\sqrt m}.                           \tag{1.7}
\]

Therefore a fixed interval (1.6) contains at most
\(C_A(1+\epsilon\sqrt m)\) integer values of \(q\). On each of them,

\[
                 0<\theta_q-p_q\leq\epsilon.       \tag{1.8}
\]

Summing over the \(O_A(1)\) integer crossings and using \(N_q\leq W\)
proves (1.5). \(\square\)

Taking \(\epsilon=m^{-1/3}\) proves (0.4). Notice the useful separation
of scales

\[
 \epsilon\longrightarrow0,\qquad
 \epsilon^2\sqrt m\longrightarrow0,\qquad
 \epsilon m=m^{2/3}\longrightarrow\infty.         \tag{1.9}
\]

Thus the near-integer quota peaks can be lowered enough to leave a
polynomial row reserve while their total all-depth quota cost is still
\(o(W)\).

## 2. One SCD-chain hash for every depth and both signs

Fix any symmetric chain decomposition \({\cal C}\) of the Boolean
lattice \(2^{[n]}\). Give every chain \(C\in{\cal C}\) an independent
uniform label

\[
                              U_C\sim\operatorname{Unif}[0,1]. \tag{2.1}
\]

At rank \(m-q\), define

\[
 {cal B}_q^-
 =\left\{S\in\binom{[n]}{m-q}:U_{C(S)}\leq p_q\right\},        \tag{2.2}
\]

and use literal complementation for the upper bonus family:

\[
 {cal B}_q^+
 =\left\{[n]\setminus S:S\in{cal B}_q^-\right\}.             \tag{2.3}
\]

At one fixed rank, distinct sets lie in distinct SCD chains. Consequently

\[
 |{cal B}_q^-|\sim\operatorname{Bin}(N_q,p_q),                 \tag{2.4}
\]

and, for every coordinate \(v\),

\[
\begin{aligned}
 h_{q,v}^-&:=\#\{S\in{cal B}_q^-:v\in S\}
  \sim\operatorname{Bin}\left({m-q\over n}N_q,p_q\right),\\
 h_{q,v}^+&:=\#\{T\in{cal B}_q^+:v\in T\}
  \sim\operatorname{Bin}\left({m+q\over n}N_q,p_q\right).
                                                               \tag{2.5}
\end{aligned}
\]

The two variables in (2.5) are not independent and need not be. The
literal complement definition gives the exact identity

\[
                         h_{q,v}^-+h_{q,v}^+=|{cal B}_q^-|.    \tag{2.6}
\]

### Theorem 2.1 (joint near quotas and common-run compatibility)

Let integers \(R_v\) be chosen so that

\[
 R_v\in\left\{\left\lfloor{W\over n}\right\rfloor,
                  \left\lceil{W\over n}\right\rceil\right\},
 \qquad \sum_vR_v=W.                                \tag{2.7}
\]

There is a deterministic labeling of the SCD chains for which

\[
 \sum_{q\leq H}\left(
   \bigl||{cal B}_q^-|-r_q\bigr|
  +\bigl||{cal B}_q^+|-r_q\bigr|\right)=o_A(W),    \tag{2.8}
\]

and

\[
\begin{aligned}
 &\sum_{q\leq H}\sum_{v=1}^n
 {1\over m-q}
 \left|h_{q,v}^--\left({(m-q)r_q\over n}
                 -q\left(R_v-{W\over n}\right)\right)\right|\\
 &\quad+
 \sum_{q\leq H}\sum_{v=1}^n
 {1\over m+q}
 \left|h_{q,v}^+-\left({(m+q)r_q\over n}
                 +q\left(R_v-{W\over n}\right)\right)\right|
 =o_A(W).                                           \tag{2.9}
\end{aligned}
\]

The normalization in (2.9) is the target-\(L^1\) scale of the point
ledger: one discrepant rank-\((m\mp q)\) target contributes to at most
\(m\mp q\) point incidences.

#### Proof

For a binomial variable \(Z\) of order \(M\),

\[
                         \mathbb E|Z-\mathbb EZ|\leq {1\over2}\sqrt M.
                                                               \tag{2.10}
\]

Equations (2.4), (1.5), and (2.10) give

\[
 \mathbb E\sum_{q\leq H}
 \bigl||{cal B}_q^-|-r_q\bigr|
 \leq O(H\sqrt W)+
       \sum_{q\leq H}N_q(\theta_q-p_q)=o_A(W).     \tag{2.11}
\]

The upper family has the same cardinality.

Put \(\delta_v=R_v-W/n\), so \(|\delta_v|\leq1\). From (2.5),

\[
\begin{aligned}
 \mathbb E{1\over m-q}
 \left|h_{q,v}^--\left({(m-q)r_q\over n}-q\delta_v\right)\right|
 &\leq {1\over2(m-q)}
       \sqrt{{m-q\over n}N_q}\\
 &\quad+{N_q(\theta_q-p_q)\over n}
       +{q\over m-q}.                              \tag{2.12}
\end{aligned}
\]

Sum (2.12) over \(v\) and \(q\). Since \(H\leq A\sqrt m\), the three
terms total respectively

\[
 O_A(H\sqrt W),\qquad
 O_A\!\left(\sum_qN_q(\theta_q-p_q)\right),
 \qquad O_A(H^2).                                   \tag{2.13}
\]

All are \(o_A(W)\). The upper calculation is identical. The expectation
of the sum of the nonnegative errors in (2.8)--(2.9) is \(o_A(W)\), so
some deterministic chain labeling has the asserted bounds. \(\square\)

Theorem 2.1 does not say that these families are the histograms of an
owner permutation. It says exactly that the quota-cardinality and common
run-vector point constraints admit one all-depth, two-sign Boolean design
up to the allowed \(o(W)\) scale.

## 3. The same construction has negligible shadow lock

For \(T\in\binom{[n]}{m-q}\), call \(T\) lower locked if

\[
 T\notin{cal B}_q^-,\qquad
 \{T-x:x\in T\}\subseteq{cal B}_{q+1}^-.          \tag{3.1}
\]

This is precisely the adjacent-depth obstruction: every extension which
would add an occurrence of \(T\) creates an already-high enclosing
depth-\((q+1)\) target. Define upper lock dually.

### Lemma 3.1 (exponentially sparse locks)

Under the random SCD labeling,

\[
 \mathbb E L_q^-\leq
 N_q(1-\epsilon)^{m-q-1},                           \tag{3.2}
\]

where \(L_q^-\) is the number of lower locked targets. The same estimate
holds for upper targets. Consequently

\[
 \mathbb E\sum_{q<H}(L_q^-+L_q^+)
 \leq2HW\exp\{-\epsilon(m-H-1)\}=o_A(W).           \tag{3.3}
\]

#### Proof

The \(m-q\) facets of one rank-\((m-q)\) set are distinct sets at a
common rank, hence lie in distinct SCD chains. At most one of those chains
can equal the chain containing \(T\), namely when the SCD predecessor of
\(T\) exists. Discarding the condition that \(T\) itself is low, all the
other \(m-q-1\) independent chain labels must be at most \(p_{q+1}\).
Thus the lock probability is at most

\[
 p_{q+1}^{m-q-1}\leq(1-\epsilon)^{m-q-1}.          \tag{3.4}
\]

Sum over targets and depths. Complementation identifies the upper lock
with the same lower-facet calculation. \(\square\)

Adding the lock count to the objective in the proof of Theorem 2.1 shows
that one deterministic labeling satisfies (2.8), (2.9), and

\[
                         \sum_{q<H}(L_q^-+L_q^+)=o_A(W)         \tag{3.5}
\]

simultaneously.

This removes the gross shadow-lock obstruction at the level of the bonus
design. It does not prove the fibrewise Hall theorem required to realize
that design by owner transitions.

## 4. Exact union of forbidden rows along one suffix

Let

\[
                         P=(X_{-H+1},\ldots,X_0)                \tag{4.1}
\]

be an \(H\)-safe suffix and put

\[
 I_{q-1}=\bigcap_{i=0}^{q-1}X_{-i}.              \tag{4.2}
\]

For an eligible removal row \(a\in I_{H-1}\), the new depth-\(q\)
lower target is

\[
                         T_q(a)=I_{q-1}\setminus\{a\}.          \tag{4.3}
\]

Let \(C_q(a)=C(T_q(a))\), let \({\cal K}(a)\) be the set of distinct
SCD chains visited by this target flag, and define

\[
 P_C(a)=\max\{p_q:C_q(a)=C\}.                      \tag{4.4}
\]

### Theorem 4.1 (exact chain-block survival formula)

For the random SCD hash,

\[
 \boxed{
 \Pr\left(a\notin\bigcup_{q\leq H}{\cal R}_q(P)\right)
 =\prod_{C\in{\cal K}(a)}(1-P_C(a)).}              \tag{4.5}
\]

Therefore

\[
 \mathbb E\left|\bigcup_{q\leq H}{\cal R}_q(P)\right|
 =\sum_{a\in I_{H-1}}
   \left(1-\prod_{C\in{\cal K}(a)}(1-P_C(a))\right).          \tag{4.6}
\]

#### Proof

At depths for which the target lies in one fixed chain \(C\), the row is
allowed exactly when

\[
                         U_C>\max\{p_q:C_q(a)=C\}=P_C(a).       \tag{4.7}
\]

The labels of distinct SCD chains are independent. Multiplying (4.7)
over the distinct visited chains gives (4.5), and summing the forbidden
probabilities gives (4.6). \(\square\)

In particular, if the whole flag (4.3) stays in one SCD chain, then

\[
 \Pr(a\hbox{ survives all depths})
 =1-\max_{q\leq H}p_q\geq\epsilon.                 \tag{4.8}
\]

More generally, if \(C_*\) is a chain on which the maximum threshold is
attained, then

\[
 \Pr(a\hbox{ survives})
 \geq \epsilon
 \left(1-\sum_{C\neq C_*}P_C(a)\right)_+.          \tag{4.9}
\]

Thus the relevant measure of incoherence is not the bare number of chain
changes, but the total threshold weight of the additional chain blocks.

The intervals \([0,p_q]\) are optimal for a fixed chain: among measurable
subsets of \([0,1]\) with measures \(p_q\), the measure of their union is
at least \(\max_qp_q\), with equality for nested intervals. Hence no
other one-label interval scheme improves (4.8).

The upper-column formula is identical after complementing every upper
target. If a removal row and an insertion column each use one chain, a
fixed pair survives both signed tests with probability at least
\(\epsilon^2\) (or \(\epsilon\) if the two chain labels coincide).

## 5. Why a universal nested filtration cannot work

One might try to obtain (4.8) on every possible target flag by demanding
the hereditary relation

\[
             T\in{\cal D}_q
 \quad\Longrightarrow\quad
             \{T-x:x\in T\}\subseteq{\cal D}_{q+1}.            \tag{5.1}
\]

Write

\[
                         \alpha_q={|{\cal D}_q|\over N_q}.      \tag{5.2}
\]

### Lemma 5.1 (normalized shadow monotonicity)

Every filtration satisfying (5.1) obeys

\[
                         \alpha_q\leq\alpha_{q+1}.              \tag{5.3}
\]

#### Proof

Put \(k=m-q\). Count incidences between \({\cal D}_q\) and its lower
shadow. Every member of \({\cal D}_q\) has \(k\) facets, while a
rank-\((k-1)\) set has at most \(n-k+1\) rank-\(k\) supersets. Thus

\[
 k|{\cal D}_q|\leq(n-k+1)|{\cal D}_{q+1}|.         \tag{5.4}
\]

Since \(N_{q+1}=N_qk/(n-k+1)\), this is (5.3). \(\square\)

### Theorem 5.2 (the first floor jump costs \(\Omega(W)\))

Fix \(A>\sqrt{\log2}\) and let \(H=\lfloor A\sqrt m\rfloor\). For all
sufficiently large \(m\), every hereditary filtration (5.1) satisfies,
for some adjacent \(q,q+1\leq H\),

\[
 \boxed{
 N_q|\alpha_q-\theta_q|
 +N_{q+1}|\alpha_{q+1}-\theta_{q+1}|
 \geq\left({1\over2}-o(1)\right)W.}                \tag{5.5}
\]

#### Proof

Uniformly for fixed \(A\),

\[
                 \lambda_{\lfloor A\sqrt m\rfloor}
                 \longrightarrow e^{A^2}>2.       \tag{5.6}
\]

Let \(q\) be the last index before \(\lambda\) crosses 2. By (1.3),

\[
 \theta_q=1-O(m^{-1/2}),\qquad
 \theta_{q+1}=O(m^{-1/2}),\qquad
 N_q,N_{q+1}=\left({1\over2}+o(1)\right)W.         \tag{5.7}
\]

Because \(\alpha_q\leq\alpha_{q+1}\),

\[
 |\alpha_q-\theta_q|+|\alpha_{q+1}-\theta_{q+1}|
 \geq\theta_q-\theta_{q+1}=1-o(1).                \tag{5.8}
\]

Multiplication by the smaller of \(N_q,N_{q+1}\) proves (5.5).
\(\square\)

Thus exact downward closure, although it perfectly aligns forbidden rows,
is incompatible with even \(o(W)\) near-quota error once a floor reset is
present.

There is also no nonconstant SCD-chain label conserved along every
possible deletion edge. Consider the graph whose vertices are the SCD
chains active at rank \(m-1\), joining two chains when a rank-\((m-1)\)
set in one contains a rank-\((m-2)\) set in the other. The incidence graph
between the complete ranks \(m-1\) and \(m-2\) is connected: exchanges
between any two \((m-2)\)-sets factor through rank \(m-1\). Contracting
the within-chain edges preserves connectivity. Hence any chain label
which is unchanged on every possible target deletion is constant on all
active chains and yields only an empty or full threshold family.

Universal alignment is therefore impossible by either of the two natural
routes:

* hereditary target families incur the floor-jump cost (5.5);
* a chain hash conserved on every deletion edge is degenerate.

The construction must select a sparse, coherent subset of target flags.

## 6. Exact parent-alignment capacity

Let \(p(S)\) denote the rank-one-lower predecessor of \(S\) in the fixed
SCD, when that predecessor exists. Fix

\[
                         B\in\binom{[n]}{k+1}.      \tag{6.1}
\]

For a common deletion direction \(x\in B\), define \(c_B(x)\) by (0.6).
The row \(a\) counted there has its two consecutive targets

\[
                         B-a,\qquad B-\{a,x\}       \tag{6.2}
\]

in one SCD chain.

### Proposition 6.1 (one coherent row per average direction)

For every \(B\),

\[
                         \sum_{x\in B}c_B(x)\leq |B|=k+1.      \tag{6.3}
\]

#### Proof

Fix a row \(a\in B\). The set \(B-a\) has at most one SCD predecessor.
If it has one contained in \(B\), that predecessor identifies exactly one
coordinate \(x\in B-a\) for which

\[
                         p(B-a)=B-\{a,x\}.          \tag{6.4}
\]

Thus each of the \(k+1\) possible rows contributes to at most one summand
in (6.3). \(\square\)

An exceptional direction may have \(c_B(x)=\Theta(m)\); those exceptional
parent-aligned stars are exactly what a positive packet construction must
find. Proposition 6.1 says that they are not supplied at positive density
by an arbitrary direction choice. Coherence through \(H\) depths is still
stronger, because the same row must satisfy the predecessor identity at
every step.

## 7. Additive hashes do not remove the coherence gate

For completeness, let \(G\) be an abelian group, assign weights
\(w_v\in G\), and put

\[
                              h(S)=\sum_{v\in S}w_v.             \tag{7.1}
\]

Suppose the depth-\(q\) bonus family is defined by

\[
                         h(S)\in J_q.             \tag{7.2}
\]

Along the suffix of Section 4, the forbidden removal rows are exactly

\[
 \boxed{
 {cal R}_q(P)=
 \{a\in I_{H-1}:w_a\in h(I_{q-1})-J_q\}.}          \tag{7.3}
\]

If the next deeper intersection deletes the coordinate \(x_q\), then

\[
 h(I_q)-J_{q+1}=h(I_{q-1})-w_{x_q}-J_{q+1}.        \tag{7.4}
\]

Thus the common row hash \(w_a\) is useful, but its forbidden interval is
translated by the history-dependent weight \(w_{x_q}\). To make the
intervals intrinsically identical for every possible history, all
differences \(w_x-w_y\) must stabilize the relevant hash interval. For a
genuine interval in the circle group the stabilizer is trivial, forcing
all coordinate weights to be equal. Then \(h(S)\) depends only on
\(|S|\), so every rank family is empty or full and cannot approximate a
nontrivial bonus density.

An additive hash can therefore help only after the orientation has chosen
history directions whose translations are coherent. This is the same
packet-specific gate exposed by (4.5) and Proposition 6.1.

## 8. Proved and unproved boundary

The following statements are proved here.

1. Clipping all near-one bonus densities at \(1-m^{-1/3}\) costs only
   \(O_A(Wm^{-1/6})=o_A(W)\) over every depth \(q\leq A\sqrt m\).
2. One SCD-chain hash gives lower and complementary upper Boolean bonus
   families with \(o_A(W)\) total cardinal error and \(o_A(W)\)
   normalized common-run point error.
3. The same joint design has only \(o_A(W)\) adjacent-depth shadow-locked
   targets.
4. Formula (4.5) computes the exact union of forbidden rows along every
   fixed safe suffix.
5. A one-chain target flag retains an \(m^{-1/3}\) fraction of rows in
   expectation; extra chain blocks reintroduce the exact product in
   (4.5).
6. Universal hereditary alignment costs \(\Omega(W)\) at the first quota
   floor reset, and universal conserved SCD labels are constant.
7. The exact parent-alignment capacity identity (6.3) shows why large
   coherent row sets require deliberate exceptional directions.

The following statements are not proved.

* No \(H\)-memory circulation or owner permutation realizing these bonus
  families is constructed.
* No Hall theorem shows that the exceptional parent-aligned directions can
  be selected compatibly at every owner and every depth.
* The \(o(W)\) count of shadow-locked targets does not by itself imply an
  \(o(W)\) count of failed owner rows without a fibrewise incidence bound.
* No cycle-count theorem is obtained. In particular, the required
  \(o(W/H)\) component count remains part of the integral circulation
  gate.

The exact surviving problem is therefore narrower than independent
all-depth quota rounding: construct an integral owner circulation whose
selected target flags have small weighted SCD-chain exposure in (4.5),
using parent-aligned stars coherently through all \(H\) memories.
