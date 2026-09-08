# Annular slow bite: the exact slice-drift gate, simultaneous anti-clustering, and a literal stall

**Date:** 2026-07-27  
**Status:** rigorous conditional anti-clustering theorem and rigorous obstruction to any deterministic trajectory invariant.  The remaining probabilistic question is reduced to one explicit integrated degree-bias estimate.

## 0. Verdict

Put

\[
 n=2m,\qquad r=m-q_0,\qquad q_0=a\sqrt m+O(1),\qquad
 N=\binom nr,\qquad K=n=2m.
\]

For \(A\in\binom{[n]}m\), let

\[
 \mathcal B_A=
 \left\{S\in\binom{[n]}r:
 |S\cap A|\in\{\lfloor r/2\rfloor,\lceil r/2\rceil\}\right\},
 \qquad \beta={|\mathcal B_A|\over N}.
\]

The value of \(\beta\) is independent of \(A\), and the hypergeometric
local limit estimate gives, uniformly for fixed \(a\),

\[
 c_a m^{-1/2}\leq \beta\leq C_a m^{-1/2}.              \tag{0.1}
\]

More explicitly, with duplicate central values included only once,

\[
 \beta={1\over\binom{2m}r}
 \sum_{t\in\{\lfloor r/2\rfloor,\lceil r/2\rceil\}}
 \binom mt\binom m{r-t}.                                  \tag{0.1a}
\]

Stirling's formula at the hypergeometric mean, whose variance is
\(r(2m-r)/(4(2m-1))=m/8+O_a(1)\), gives the parity-resolved leading term

\[
 \beta=
 \begin{cases}
 (2+o(1))/\sqrt{\pi m},&r\text{ even},\\
 (4+o(1))/\sqrt{\pi m},&r\text{ odd}.
 \end{cases}                                               \tag{0.1b}
\]

There is a notational point worth fixing.  In the source audit,
\(\mathcal B_A\) is the **central hitting slice**: every packet meets it.
Its complement

\[
 \mathcal U_A=\binom{[n]}r\setminus\mathcal B_A              \tag{0.2}
\]

is the edge-free residual.  Thus “concentration into a slice complement”
means depletion of \(\mathcal B_A\), not concentration into
\(\mathcal B_A\).

For completeness, if \(I_j\) are the consecutive windows of a packet and
\(x_j=|I_j\cap A|\), then
\(x_{j+1}-x_j\in\{-1,0,1\}\) and
\(K^{-1}\sum_jx_j=r/2\).  A unit-step integer walk with this average must
visit \(\lfloor r/2\rfloor\) or \(\lceil r/2\rceil\).  Hence every packet
meets \(\mathcal B_A\), proving that \(\mathcal U_A\) contains no packet.

The conclusions are as follows.

1. At residual density \(z=m^{-1/2}\), the natural surviving mass of every
   central slice is
   \[
   z|\mathcal B_A|=\Theta_a(N/m).                            \tag{0.3}
   \]
   This, rather than \(N/\sqrt m\), is the scale at which collision waste
   and predictable drift must be controlled.

2. For any adapted packet trajectory, simultaneous anti-clustering follows
   from one exact condition: the cumulative positive discrepancy between
   the slice proportion seen by the next packet and the slice proportion
   among the currently live vertices is \(o(\beta)\).  Once this predictable
   drift is controlled, Freedman's inequality gives failure probability
   \[
   \exp\{-\Omega_a(N/m^{5/2})\},                              \tag{0.4}
   \]
   even after union over all \(\binom{2m}m\) choices of \(A\).

3. The raw independently marked incidence ledger in the full-catalogue
   first bite has zero slice drift exactly and satisfies the required
   simultaneous concentration by a direct Bernstein estimate.
   Static codegrees and edge-local collision energy, however, do not imply
   that the drift remains small after conditioning on the previous bites.

4. No deterministic trajectory invariant can forbid a stall.  In the
   “delete every vertex touched by any marked edge” slow bite of the source
   audit, there is a positive-probability marking event which deletes
   exactly \(\mathcal B_A\) and leaves the absorbing edge-free state
   \(\mathcal U_A\), of density \(1-\Theta_a(m^{-1/2})\).  This event is
   astronomically rare and is not a high-probability obstruction, but it
   proves that an almost-sure invariant is impossible.

Accordingly, the ST-type annular gate is neither settled by a slice entropy
union bound nor refuted by a typical-stall calculation.  It is exactly the
integrated live-degree bias in (3.9) below.

## 1. Catalogue identities

Let \(\mathcal E\) be the annular packet catalogue.  A packet is the set of
the \(K=n\) cyclic intervals of length \(r\) in an unoriented cyclic order.
The exact vertex degree and packet count are

\[
 D={r!(n-r)!\over2},
 \qquad
 E:=|\mathcal E|={ND\over K}={(n-1)!\over2}.                 \tag{1.1}
\]

For a packet \(e\), define its \(A\)-slice load by

\[
 b_A(e)=|e\cap\mathcal B_A|.                                \tag{1.2}
\]

Double counting the incidences \((S,e)\) with
\(S\in\mathcal B_A\subset e\) gives

\[
 \sum_{e\in\mathcal E}b_A(e)=|\mathcal B_A|D,
 \qquad
 {1\over E}\sum_{e\in\mathcal E}b_A(e)=K\beta.             \tag{1.3}
\]

Also, since \(0\leq b_A(e)\leq K\),

\[
 \sum_{e\in\mathcal E}b_A(e)^2
 \leq K\sum_{e\in\mathcal E}b_A(e)
 =K\beta ND.                                                \tag{1.4}
\]

These identities use no independence and no approximation.

## 2. The first bite is simultaneously balanced

Mark every catalogue packet independently with probability

\[
 p={\gamma\over KD}.                                        \tag{2.1}
\]

Let \(\xi_e\) be its mark indicator and put

\[
 Z_A=\sum_{e\in\mathcal E}\xi_e\bigl(b_A(e)-K\beta\bigr).
                                                                    \tag{2.2}
\]

Then \(\mathbb EZ_A=0\) by (1.3).  Moreover, (1.4) and
\((x-y)^2\leq2x^2+2y^2\) give

\[
 \begin{split}
 \operatorname {Var}Z_A
 &\leq p\sum_e(b_A(e)-K\beta)^2\\
 &\leq 2pK\beta ND+2pEK^2\beta^2
 \leq 4\gamma\beta N.                                     \tag{2.3}
 \end{split}
\]

Every summand has absolute value at most \(K\).  Bernstein's inequality
therefore yields

\[
 \Pr(|Z_A|\geq u)
 \leq2\exp\left{-{u^2\over
 C(\gamma\beta N+Ku)}\right}.                              \tag{2.4}
\]

Since

\[
 \log\binom{2m}m
 =2m\log2-{1\over2}\log(\pi m)+O(m^{-1})
 \leq2m\log2,                                              \tag{2.5}
\]

and \(\mathcal B_A=\mathcal B_{A^c}\), there are at most
\(\frac12\binom{2m}m\) distinct slice events.  Keeping the harmless factor
two and union bounding over all labelled \(A\) gives

\[
 \max_{A\in\binom{[n]}m}|Z_A|
 =O\left(\sqrt{\gamma\beta Nm}+Km\right)                  \tag{2.6}
\]

with probability at least \(1-e^{-cm}\), after increasing the absolute
constant in (2.6).  Because \(N\) is exponential in \(m\), the right-hand
side is negligible compared with \(N/m\) for every polynomially small
\(\gamma\).

This proves that the raw marking ledger of the complete initial catalogue
has no simultaneous slice problem.  Passing from marked incidences to
isolated retained packets still requires the collision correction.  The
estimate also says nothing by itself about a later live catalogue: its
conditional packet law is weighted by all previous deletions.

## 3. Exact trajectory identity

Consider any adapted sequence of pairwise vertex-disjoint selected packets

\[
 e_1,e_2,\ldots,e_T.                                        \tag{3.1}
\]

First form the **virtual matching residual**, which ignores side deletions
but removes every selected packet.  Let

\[
 R_i=N-Ki,
 \qquad
 B_{A,i}=\left|\mathcal B_A\setminus\bigcup_{j\leq i}e_j\right|,
 \qquad
 X_{A,i}={B_{A,i}\over R_i}.                                \tag{3.2}
\]

Thus \(X_{A,0}=\beta\).  Write

\[
 b_{A,i}=b_A(e_i),
 \qquad
 \theta_{A,i}={1\over K}
 \mathbb E(b_{A,i}\mid\mathcal F_{i-1}).                   \tag{3.3}
\]

The quotient update is exact:

\[
 X_{A,i}-X_{A,i-1}
 ={KX_{A,i-1}-b_{A,i}\over R_i}.                            \tag{3.4}
\]

Consequently

\[
 X_{A,T}=\beta-\mathfrak D_A(T)+M_A(T),                     \tag{3.5}
\]

where

\[
 \mathfrak D_A(T)=
 \sum_{i\leq T}{K(\theta_{A,i}-X_{A,i-1})\over R_i},       \tag{3.6}
\]

and

\[
 M_A(T)=
 \sum_{i\leq T}{K\theta_{A,i}-b_{A,i}\over R_i}           \tag{3.7}
\]

is a martingale.  Thus \(\mathfrak D_A>0\) is precisely the
predictable depletion of the slice proportion.  There is no hidden
covariance objective in (3.6): it is the literal missing-slice drift.

The identities (3.2)--(3.7) remain valid when collision-waste deletions
occur during the process and influence all later choices: their influence
is already present in the conditional law in (3.3).  At the end one must
subtract their vertex set from the virtual residual, as done in (4.7).

If there are no side deletions and the next packet is conditionally
uniform in the current live catalogue \(\mathcal E(R)\), then

\[
 \theta_{A}(R)=\widehat\beta_A(R):=
 {\sum_{S\in R\cap\mathcal B_A}d_R(S)
  \over
  \sum_{S\in R}d_R(S)}
 = {\sum_{S\in R\cap\mathcal B_A}d_R(S)
  \over K|\mathcal E(R)|}.                                  \tag{3.8}
\]

Hence the exact required invariant is

\[
 \boxed{
 \sup_A\sum_{i\leq T}{K\over R_i}
 \left(\widehat\beta_A(R_{i-1})
       -{|R_{i-1}\cap\mathcal B_A|\over R_{i-1}}
 \right)=o(\beta).}                                         \tag{3.9}
\]

For the actual isolated-mark rule, \(\widehat\beta_A\) in (3.9) is to be
replaced by the actual conditional packet law \(\theta_{A,i}\).  This
absorbs exactly, rather than heuristically, the isolation bias.
If total side deletion is \(o(N/m)\), its contribution to a slice
proportion before density \(z=m^{-1/2}\) is \(o(m^{-1/2})=o(\beta)\).

The scale in (3.9) is sharp, but the weighting is favorable.  Since

\[
 \sum_{i\leq T}{K\over R_i}
 =\log {N\over R_T}+O(K/R_T)
 ={1\over2}\log m+o(1),                                   \tag{3.10}
\]

a roughly constant absolute bias \(\delta\) accumulates as
\(\delta\log(1/z)\).  The critical average absolute bias is therefore

\[
 {\beta\over\log(1/z)}=\Theta_a\left({1\over\sqrt m\log m}\right).
                                                                    \tag{3.11}
\]

In particular, a genuinely uniform absolute bias \(O(1/m)\) would be
subcritical by a factor \(\log m/\sqrt m=o(1)\).  What the static overlap
calculation does not decide is whether its formal
\(O((mz)^{-1})\) parameter controls the **absolute** slice bias, a
relative degree error, or neither after hereditary conditioning.  That
translation is precisely what (3.9) demands.

### 3.1 The exact first-moment invariant

Assume the slow-bite rule is label-equivariant, as is the uniform marking
and isolation rule.  At every fixed selected-packet count \(i\) for which
the state is defined almost surely, the law of the virtual residual is
invariant under \(S_n\).  Since \(S_n\) is transitive on
\(\binom{[n]}r\), every rank-\(r\) vertex has the same survival
probability.  As \(R_i=N-Ki\) is deterministic,

\[
 \mathbb E B_{A,i}=\beta R_i,
 \qquad
 \mathbb E X_{A,i}=\beta                                  \tag{3.12}
\]

for every fixed \(A\).  More generally, let \(T\) be a bounded
permutation-invariant stopping time for the selected-packet filtration.
Conditional on each value of \(T\), the virtual residual law is still
\(S_n\)-invariant, so \(\mathbb EX_{A,T}=\beta\).  Optional stopping in
(3.7), followed by expectation in (3.5), yields the exact identity

\[
 \mathbb E\mathfrak D_A(T)=0.                              \tag{3.13}
\]

Thus there is no systematic slice drift in the first moment, even after
many bites.  This does not imply a lower-tail bound: an equivariant process
may first choose a random balanced coordinate \(A_0\) and then approach
\(\mathcal U_{A_0}\).  Equations (3.12)--(3.13) therefore cannot replace
the simultaneous concentration condition (5.3).

## 4. Simultaneous anti-clustering theorem

**Theorem 4.1 (trajectory criterion).**  Let \(z=m^{-1/2}\), and stop an
adapted disjoint-packet trajectory at any time \(T\) with \(R_T\geq zN\).
Suppose the following bound holds almost surely (or restrict attention to
the event on which it holds):

\[
 \sup_{A\in\binom{[n]}m}\mathfrak D_A(T)\leq\beta/4.        \tag{4.1}
\]

Then the probability that (4.1) holds but the conclusion below fails is at
most

\[
 2\binom{2m}m
 \exp\{-c_aN/m^{5/2}\},                                    \tag{4.2}
\]

and hence, except on that event, simultaneously for every \(A\),

\[
 |R_T\cap\mathcal B_A|\geq {\beta\over2}|R_T|
 \geq {c_a\over2}{N\over m}.                               \tag{4.3}
\]

The same conclusion holds at all stopping times before density \(z\),
with a change of the absolute constant in (4.2).

**Proof.**  The increments of (3.7) are bounded by \(K/R_i\).  Their
conditional quadratic variation is at most

\[
 \sum_{i\leq T}{K^2\over R_i^2}
 \leq {2K\over R_T}
 \leq {2K\over zN}.                                        \tag{4.4}
\]

The integral comparison in (4.4) uses that the denominator decreases in
steps of exactly \(K\).  Freedman's maximal inequality, with threshold
\(\beta/4\), gives for a fixed \(A\)

\[
 \Pr\left(\inf_{t\leq T}M_A(t)\leq-\beta/4\right)
 \leq
 \exp\left\{-{c\beta^2\over K/(zN)+(K/(zN))\beta}\right}
 \leq \exp\{-c_aN/m^{5/2}\}.                               \tag{4.5}
\]

Here \(K=2m\), \(z=m^{-1/2}\), and \(\beta\asymp_a m^{-1/2}\).
On the complementary event, (3.5) and (4.1) give
\(X_{A,T}\geq\beta/2\).  Union over \(A\), using (2.5), proves
(4.2)--(4.3).  Since \(N/m^{5/2}\gg m\), the slice entropy is negligible.
\(\square\)

The exponent in (4.2) was not optimized.  Its role is to record the exact
comparison

\[
 \underbrace{\log\binom{2m}m}_{O(m)}
 \ll
 \underbrace{N/m^{5/2}}_{\text{martingale exponent}}.        \tag{4.6}
\]

### Collision-waste deletions

Suppose that, in addition to the selected disjoint packets, at most \(w\)
vertices are deleted as collision waste.  These deletions can remove at
most \(w\) vertices from any one \(\mathcal B_A\).  Therefore Theorem 4.1
still gives

\[
 |R_T^{\rm final}\cap\mathcal B_A|
 \geq {\beta zN\over2}-w.                                  \tag{4.7}
\]

In particular, it is enough that

\[
 w=o(\beta zN)=o(N/m).                                      \tag{4.8}
\]

The source audit gives expected total collision waste
\(O(\gamma N)\).  Thus \(\gamma=m^{-1}\) is only critical for this
slice argument, whereas, for example, \(\gamma=m^{-2}\) gives
\(\mathbb Ew=O(N/m^2)\).  Markov at threshold \(N/m^{3/2}\) then gives
\(w=o(N/m)\) with probability \(1-O(m^{-1/2})\).

## 5. Why the static overlap estimates do not prove (3.9)

The initial identity (1.3) says that the packet-seen slice proportion is
exactly \(\beta\).  At a later residual \(R\), the corresponding identity
is (3.8), which weights each live vertex by its residual degree \(d_R(S)\).
The desired count proportion is instead

\[
 \beta_A(R)={|R\cap\mathcal B_A|\over|R|}.                  \tag{5.1}
\]

Thus the obstruction is the covariance

\[
 \widehat\beta_A(R)-\beta_A(R)
 ={1\over K|\mathcal E(R)|}
 \sum_{S\in R}
 \bigl(1_{\mathcal B_A}(S)-\beta_A(R)\bigr)d_R(S).          \tag{5.2}
\]

Pair codegrees and the time-zero edge collision energy control one-step
fluctuations before conditioning.  They do not control the sign of (5.2)
for a residual selected by the previous trajectory.  In particular, at
the edge-free residual \(R=\mathcal U_A\), every live degree vanishes and
the next-packet law has ceased to exist.  Any claimed hereditary proof
must therefore establish (3.9) along the random trajectory; it cannot be a
uniform theorem over all residuals of the same density.

This also identifies the minimal useful strengthening of the static
moment argument.  It is enough to prove, with high probability,

\[
 \sup_A\sum_{i\leq T}{K\over R_i}
 \bigl(\theta_{A,i}-X_{A,i-1}\bigr)_+=o(m^{-1/2}),           \tag{5.3}
\]

not full residual regularity and not all higher link moments.

## 6. A literal absorbing stall for the collision-waste bite

Fix \(A\).  Call an unoriented cyclic order **alternating** if labels from
\(A\) and \(A^c\) alternate around the cycle.  Let \(\mathcal F_A\) be
the corresponding packet family.

**Lemma 6.1.**

\[
 \bigcup_{e\in\mathcal F_A}e=\mathcal B_A.                  \tag{6.1}
\]

**Proof.**  Every length-\(r\) interval in an alternating balanced binary
cycle contains either \(\lfloor r/2\rfloor\) or
\(\lceil r/2\rceil\) labels of \(A\); hence its packet lies in
\(\mathcal B_A\).  Conversely, if \(S\in\mathcal B_A\), its \(A\)- and
\(A^c\)-labels can be ordered alternately in a linear word of length
\(r\).  The complementary labels also have counts differing by at most
one.  Choose the starting parity of the complementary alternating word
opposite to the last parity of the first word.  Because the total two
colour counts are both \(m\), the last complementary colour is opposite
to the first colour of the first word.  The concatenation is therefore an
alternating cycle having \(S\) as a length-\(r\) interval.  \(\square\)

The exact number of alternating packets is

\[
 F:=|\mathcal F_A|={(m-1)!m!\over2},                         \tag{6.2}
\]

because, after anchoring one fixed \(A\)-label, the remaining same-parity
slots and the opposite-parity slots can be ordered in
\((m-1)!\) and \(m!\) ways, and reversal identifies two orientations.
Together with (1.1),

\[
 {F\over E}={1\over\binom{2m-1}{m}}
 ={2\over\binom{2m}{m}}.                                   \tag{6.3}
\]

Now use exactly the slow-bite convention of the source audit in which all
vertices belonging to any marked packet are deleted, while intersecting
marks are charged as collision waste.  The event

\[
 \xi_e=1\ (e\in\mathcal F_A),
 \qquad
 \xi_e=0\ (e\notin\mathcal F_A)                             \tag{6.4}
\]

has probability

\[
 p^F(1-p)^{E-F}>0.                                          \tag{6.5}
\]

On (6.4), Lemma 6.1 says that the deleted set is exactly
\(\mathcal B_A\).  The residual is \(\mathcal U_A\), which contains no
packet, so the process stalls at density

\[
 1-\beta=1-\Theta_a(m^{-1/2}).                              \tag{6.6}
\]

The stall spends \(\Theta_a(N/\sqrt m)\) collision-waste vertices, far
above the admissible \(o(N/m)\) budget in (4.8).  Thus it is consistently
excluded by the quantitative anti-clustering theorem even though it is a
literal sample path.

This is a genuine trajectory of the random slow bite.  It refutes any
almost-sure slow-bite invariant forbidding slice-complement concentration.
It does **not** refute a high-probability theorem: (6.5) is far smaller
than any relevant error probability.  It also uses the collision-waste
deletion convention.  For a process deleting only isolated retained
packets, (6.4) retains none of the heavily intersecting alternating
packets and does not give the same stall.

## 7. Exact remaining problem

The annular slow-bite slice problem is now reduced to the following single
statement.

> **Integrated slice-degree problem.**  For the actual isolated-packet
> slow bite, run until \(|R|=zN\), \(z=m^{-1/2}\).  Prove
> \[
> \Pr\left(
> \sup_{A\in\binom{[n]}m}
> \sum_i {K\over R_i}
> \bigl(\theta_{A,i}-X_{A,i-1}\bigr)_+>\beta/4
> \right)=o(1).                                             \tag{7.1}
> \]

Theorem 4.1 then supplies the full simultaneous conclusion

\[
 \min_A|R\cap\mathcal B_A|=\Omega_a(N/m),                   \tag{7.2}
\]

provided collision waste is \(o(N/m)\).  Conversely, any typical stall
near a slice complement must create an integrated positive degree bias of
order \(\beta\) in (7.1).  This makes (7.1) both the sufficient
anti-clustering invariant and the quantitative certificate that every
high-probability counterexample must violate.

The key audit conclusion is therefore sharp: entropy over the balanced
coordinates \(A\) is harmless; the hereditary sign of the live
degree-weighted slice covariance (5.2) is the sole unresolved mechanism.
