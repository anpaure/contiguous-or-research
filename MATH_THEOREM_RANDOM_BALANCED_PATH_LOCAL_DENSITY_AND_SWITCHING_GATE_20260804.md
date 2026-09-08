# Random balanced paths: local-density switching and the exact expansion gate

**Date:** 2026-08-04  
**Status:** unconditional cut duality, unconditional exchangeable-partition
calculation, and an exact conditional switching/entropy reduction.  The
global-density random-partition model is proved incompatible with Boolean
containment.  This note does **not** construct a balanced Boolean path bank
satisfying every multisocket cut.  No computation is used.

## 0. Outcome

Put

\[
 k=2r,\qquad
 \mathcal O=\binom{[2r]}r,\qquad
 W=|\mathcal O|,\qquad
 C_s=\binom{2r}s .                                      \tag{0.1}
\]

Fix an owner-rooted downward path bank and write

\[
 V_s(S)=\{T\in\mathcal O:P_T(s)=S\},\qquad
 e_s(Q)=|\{S:V_s(S)\subseteq Q\}|.                      \tag{0.2}
\]

At rank (s), let (b_s) targets be disposable and put

\[
 N_s=C_s-b_s,\qquad N=\sum_sN_s,\qquad L=dW-N\ge0.       \tag{0.3}
\]

The multisocket Hall inequalities

\[
 \sum_s(e_s(Q)-b_s)_+\le d|Q|\qquad(Q\subseteq\mathcal O) \tag{0.4}
\]

have the following exact conjugate form.  If

\[
 u_s(R)=|\{P_T(s):T\in R\}|                              \tag{0.5}
\]

is the number of distinct rank-(s) sets hit by a path family (R), then
(0.4) is equivalent to

\[
 \boxed{
 \sum_s\min\{u_s(R),N_s\}\ge d|R|-L
 \qquad(R\subseteq\mathcal O).}                         \tag{0.6}
\]

Thus the random-path problem is exactly a capped union-expansion problem.

There is a clean answer to the proposed *exchangeable* model.  Put

\[
 m_s=\left\lfloor\frac W{C_s}\right\rfloor,\quad
 a_s=(m_s+1)C_s-W,\quad c_s=W-m_sC_s.                    \tag{0.7}
\]

Partition (W) abstract path labels uniformly into (a_s) labelled blocks
of size (m_s) and (c_s) labelled blocks of size (m_s+1), independently
at different ranks.  For a fixed (q)-set (Q), the exact expected forced
count is

\[
 \boxed{
 \mathbb E e_s(Q)
 =a_s\frac{(q)_{m_s}}{(W)_{m_s}}
  +c_s\frac{(q)_{m_s+1}}{(W)_{m_s+1}}.}                 \tag{0.8}
\]

Here ((x)_j=x(x-1)\cdots(x-j+1)).  The quotient of (0.8) by (q) is
nondecreasing in (q), and at (q=W) it equals (C_s/W).  Consequently,
after the exact boundary weighting

\[
 w_s=\frac{N_s}{C_s},\qquad
 (e_s-b_s)_+\le w_se_s,                                 \tag{0.9}
\]

the normalized expected weighted count is maximized at (q=W) and is
exactly (N/W\le d).  An exact negative-dependence moment bound and a
finite entropy criterion for this abstract model are given in Section 2.

The exchangeable model cannot be imported into the Boolean path problem.
For a coordinate (x), let

\[
 Q_x=\{T\in\mathcal O:x\in T\},\qquad |Q_x|=W/2.         \tag{0.10}
\]

Every rank-(s) set containing (x) has all its possible visitors in
(Q_x), so every Boolean path bank satisfies

\[
 e_s(Q_x)\ge\binom{2r-1}{s-1}.                           \tag{0.11}
\]

In a central rank with (s>r/2) and (m_s\ge2), the right side is
strictly larger than (C_s/4), whereas the exchangeable density-(1/2)
expectation in (0.8) is at most (C_s/4).  Hence neither global
exchangeability nor a density-only stochastic domination can hold for
random Boolean paths, regardless of how the balanced consecutive-layer
(b)-matchings are sampled.

The correct statistic is local.  For (S\in\binom{[2r]}s), put

\[
 \mathcal U_s(S)=\{T\in\mathcal O:S\subseteq T\},\quad
 D_s=|\mathcal U_s(S)|=\binom{2r-s}{r-s},\quad
 h_Q(S)=|Q\cap\mathcal U_s(S)|.                          \tag{0.12}
\]

Under a locally uniform visitor-block marginal, the global powers in
(0.8) are replaced by

\[
 \frac{a_s}{C_s}\frac{(h_Q(S))_{m_s}}{(D_s)_{m_s}}
 +\frac{c_s}{C_s}\frac{(h_Q(S))_{m_s+1}}{(D_s)_{m_s+1}}. \tag{0.13}
\]

Their sum is always at most ((C_s/W)|Q|).  This gives the exact correct
first-moment benchmark, but not concentration and not simultaneous control
of all (Q).

The remaining random-path theorem is therefore a two-part statement:

1. a **local switching moment bound** for a probability law on integral
   balanced Boolean flows, using (h_Q(S)/D_s), not (|Q|/W); and
2. an **energy-sensitive container bound** showing that the Boolean owner
   families for which the local first-moment gap is small have sufficiently
   small entropy.

Section 4 states the exact conditional lemma.  Coordinate stars show why
ordinary union over the (\binom Wq) sets of density (q), combined only
with the exchangeable formula (0.8), is not a valid proof of (0.4).

## 1. Exact conjugate union expansion

Assume every rank under consideration is visited by the path bank.  This
holds in particular for a floor/ceiling-balanced bank.  Let (Q\subseteq
\mathcal O), put (R=\mathcal O\setminus Q), and define (u_s(R)) by
(0.5).

### Theorem 1.1 (conjugate multisocket expansion)

For every (s),

\[
 e_s(Q)=C_s-u_s(R).                                     \tag{1.1}
\]

Consequently the complete cut family (0.4) is equivalent to (0.6).

### Proof

A rank-(s) target (S) is counted by (e_s(Q)) precisely when no path
from (R) visits (S).  Since every target is visited, the targets not
counted by (e_s(Q)) are exactly the (u_s(R)) distinct targets hit by
(R).  This proves (1.1).

Now

\[
 \begin{aligned}
 (e_s(Q)-b_s)_+
  &=(C_s-u_s(R)-b_s)_+\\
  &=(N_s-u_s(R))_+\\
  &=N_s-\min\{u_s(R),N_s\}.
 \end{aligned}                                          \tag{1.2}
\]

Sum (1.2), use (|Q|=W-|R|) and (N=dW-L), and rearrange.  The result is
exactly (0.6). \(\square\)

The cap in (0.6) matters only for very large (R), but keeping it makes the
duality exact at every scale.  At (R=\mathcal O), its two sides are
(N=dW-L).  At (R=\varnothing), both sides are zero.

### Lemma 1.2 (boundary-weighted sufficient cut)

For every integer (0\le e\le C_s),

\[
 (e-b_s)_+\le \frac{C_s-b_s}{C_s}\,e=w_se.              \tag{1.3}
\]

Therefore (0.4) follows from the stronger weighted inequalities

\[
 Y(Q):=\sum_sw_se_s(Q)\le d|Q|\qquad(Q\subseteq\mathcal O). \tag{1.4}
\]

### Proof

If (e\le b_s), the left side of (1.3) is zero.  If (e>b_s), then

\[
 e-b_s\le e-\frac{b_s}{C_s}e
\]

because (e\le C_s).  Summation proves the second assertion. \(\square\)

The weighted cut is only sufficient.  Its advantage is that the boundary
is incorporated exactly into the scalar expectation:

\[
 \sum_s w_s\frac{C_s}{W}=\frac NW\le d.                 \tag{1.5}
\]

### Lemma 1.3 (pair-meeting reduction for small complements)

For (R\subseteq\mathcal O), let

\[
 n_s^R(S)=|\{T\in R:P_T(s)=S\}|,
 \qquad
 M_J(T,U)=|\{s\in J:P_T(s)=P_U(s)\}|.                  \tag{1.6}
\]

If (J) is a set of ranks and (|R|\le\min_{s\in J}N_s), then

\[
 \sum_s\min\{u_s(R),N_s\}
 \ge |J||R|-\sum_{\{T,U\}\in\binom R2}M_J(T,U).        \tag{1.7}
\]

In particular, the cut indexed by (R) follows if

\[
 \sum_{\{T,U\}\in\binom R2}M_J(T,U)
 \le (|J|-d)|R|+L.                                     \tag{1.8}
\]

Moreover

\[
 P_T(s)=P_U(s)\quad\Longrightarrow\quad s\le|T\cap U|. \tag{1.9}
\]

### Proof

At rank (s),

\[
 |R|-u_s(R)=\sum_{S:n_s^R(S)>0}(n_s^R(S)-1)
 \le\sum_S\binom{n_s^R(S)}2.                           \tag{1.10}
\]

Sum (1.10) over (s\in J) and interchange the order of summation over
path pairs.  Because (u_s(R)\le|R|\le N_s) on (J), no cap is active
there, and all ranks outside (J) make nonnegative contributions.  This
gives (1.7); comparison with (0.6) gives (1.8).  If two paths meet at a
rank-(s) set, that set is contained in both owners, proving (1.9).
\(\square\)

Lemma 1.3 is one precise target for consecutive-layer switching: on small
complements it is enough to control induced pair-meeting weight in the
Johnson-local owner graph.  It does not by itself handle dense (R), where
higher-order block information is essential.

## 2. What independent uniform balanced partitions really prove

This section deliberately drops Boolean containment and nesting.  Let
(X) be a set of (W) abstract path labels.  At rank (s), take
(a_s) labelled boxes of size (m_s) and (c_s) labelled boxes of size
(m_s+1), and put a uniformly random bijection from (X) to all box
positions.  Forget the order inside each box.  Make these random partitions
independent at different ranks.

For an integer (q\ge0), use the convention ((q)_j=0) when (j>q).

### Theorem 2.1 (exact expectation and monotonicity)

For every fixed (Q\subseteq X) of size (q), equation (0.8) holds.  For
(q\ge1),

\[
 q\longmapsto\frac{\mathbb E e_s(Q)}q                  \tag{2.1}
\]

is nondecreasing, and

\[
 \frac{\mathbb E e_s(X)}W=\frac{C_s}{W}.                \tag{2.2}
\]

Consequently

\[
 \frac1q\mathbb E\!\left[\sum_sw_se_s(Q)\right]
 \le\frac NW\le d.                                    \tag{2.3}
\]

### Proof

A specified box of size (ell) lies wholly in (Q) with probability

\[
 \theta_\ell(q):=\frac{(q)_\ell}{(W)_\ell}.             \tag{2.4}
\]

Linearity of expectation over the (a_s+c_s=C_s) boxes proves (0.8).
For (ell\ge1),

\[
 \frac{\theta_\ell(q)}q
 =\frac1W\frac{(q-1)_{\ell-1}}{(W-1)_{\ell-1}},         \tag{2.5}
\]

which is nondecreasing in the integer (q).  A nonnegative linear
combination proves (2.1).  At (q=W), every box is captured, so
(e_s(X)=a_s+c_s=C_s), proving (2.2).  Multiply by (w_s), sum, and use
(1.5) to obtain (2.3). \(\square\)

Thus the proposed normalized expectation is indeed maximized at density
one.  The exact finite formula uses falling factorials; the powers
(q^{m_s}) and (q^{m_s+1}) are its fixed-density asymptotics after (q)
is normalized by (W).

There is also an exact moment estimate which contains all within-rank
negative dependence needed by the elementary first-moment method.

### Theorem 2.2 (uniform-box factorial moment bound)

For every (z\ge1),

\[
 \mathbb E z^{w_se_s(Q)}
 \le
 \left(1+(z^{w_s}-1)\theta_{m_s}(q)\right)^{a_s}
 \left(1+(z^{w_s}-1)\theta_{m_s+1}(q)\right)^{c_s}.     \tag{2.6}
\]

### Proof

For a box (B), let (I_B) be the indicator that all its positions are
occupied by labels of (Q).  Expand

\[
 z^{w_se_s(Q)}=\prod_B\bigl(1+(z^{w_s}-1)I_B\bigr).     \tag{2.7}
\]

For distinct boxes of sizes (ell_1,\ldots,\ell_t), their position sets
are disjoint and

\[
 \Pr(I_{B_1}=\cdots=I_{B_t}=1)
 =\frac{(q)_{\ell_1+\cdots+\ell_t}}
        {(W)_{\ell_1+\cdots+\ell_t}}
 \le\prod_{i=1}^t\frac{(q)_{\ell_i}}{(W)_{\ell_i}}.     \tag{2.8}
\]

Indeed the factors ((q-j)/(W-j)) decrease with (j), so restarting the
factor product at (j=0) for every box can only increase it.  Substitute
(2.8) term by term into the nonnegative expansion of (2.7).  The resulting
product is exactly the right side of (2.6). \(\square\)

Independence between ranks now gives a completely explicit entropy test.
Define

\[
 \begin{aligned}
 H_r(q):=\inf_{z>1}\;&z^{-(dq+1)}\\
 &\prod_s
 \left(1+(z^{w_s}-1)\theta_{m_s}(q)\right)^{a_s}
 \left(1+(z^{w_s}-1)\theta_{m_s+1}(q)\right)^{c_s}.
 \end{aligned}                                         \tag{2.9}
\]

### Corollary 2.3 (exact abstract entropy criterion)

If

\[
 \sum_{q=1}^{W-1}\binom Wq H_r(q)<1,                   \tag{2.10}
\]

then some family of independent abstract balanced partitions satisfies all
multisocket cuts (0.4).

### Proof

By Lemma 1.2, a failed cut for a (q)-set (Q) implies
(Y(Q)>dq).  The unweighted failed-cut quantity is an integer, so in fact
(Y(Q)\ge dq+1).  Markov's inequality, Theorem 2.2, and independence of
the rank partitions bound this probability by (H_r(q)).  Sum over all
proper nonempty (Q).  If (2.10) holds, with positive probability no such
cut fails.  The empty cut is automatic; the full cut is the scalar
inequality (N\le dW). \(\square\)

Corollary 2.3 is a criterion, not an assertion that (2.10) has been proved
at the optimal parameters.  More importantly, even a proof of (2.10) would
construct only abstract partitions, not compatible Boolean paths.

## 3. Boolean containment destroys global exchangeability

For every Boolean owner path and every target (S),

\[
                         V_s(S)\subseteq\mathcal U_s(S). \tag{3.1}
\]

This elementary support restriction is already enough to disprove the
global-density model.

### Theorem 3.1 (coordinate-star obstruction)

Fix (x\in[2r]) and let (Q_x) be (0.10).  For every owner-path bank and
every (1\le s<r),

\[
 e_s(Q_x)\ge\binom{2r-1}{s-1}=\frac{s}{2r}C_s.           \tag{3.2}
\]

Moreover

\[
 \sum_{s=1}^{r-1}\binom{2r-1}{s-1}
 =2^{2r-2}-\frac W2.                                    \tag{3.3}
\]

If (s>r/2) and (m_s\ge2), then

\[
 e_s(Q_x)>\frac{C_s}{4}
 \ge
 a_s\frac{(W/2)_{m_s}}{(W)_{m_s}}
 +c_s\frac{(W/2)_{m_s+1}}{(W)_{m_s+1}}.                \tag{3.4}
\]

### Proof

There are (\binom{2r-1}{r-1}=W/2) owners containing (x).  If (S)
contains (x), every owner which can visit (S) also contains (x).
Thus (V_s(S)\subseteq Q_x), even if (V_s(S)) is empty, and all
(\binom{2r-1}{s-1}) such targets are counted by (e_s(Q_x)).  This proves
(3.2).

Substitute (t=s-1).  For the odd row (2r-1),

\[
 \sum_{t=0}^{r-1}\binom{2r-1}t=2^{2r-2},\qquad
 \binom{2r-1}{r-1}=W/2.
\]

Removing the last term proves (3.3).

For (ell\ge2),

\[
 \frac{(W/2)_\ell}{(W)_\ell}\le2^{-\ell}\le\frac14.   \tag{3.5}
\]

Since (a_s+c_s=C_s), the exchangeable expectation is at most (C_s/4).
On the other hand (s>r/2) makes ((s/(2r))C_s>C_s/4).  This proves
(3.4). \(\square\)

The theorem is not a bad Hall cut: the right side of (0.4) is also
macroscopic for (Q_x).  Its conclusion is narrower and decisive.  The
law of (V_s(S)) cannot be that of a globally uniform block of path labels,
and no negative-dependence proof may replace the eligible density
(h_Q(S)/D_s) by the global density (|Q|/W).

An even more local form of the same warning is useful.  For every target
(S), the owner family (Q=\mathcal U_s(S)) captures (S) with probability
one under every random Boolean path law, whereas a globally exchangeable
block would assign it probability approximately
((|Q|/W)^{m_s}).  The discrepancy is forced by support, not by a poor
choice of random (b)-matching measure.

## 4. The correct local benchmark and the missing lemma

Let

\[
 \eta_s=\frac{a_s}{C_s},\qquad 1-\eta_s=\frac{c_s}{C_s}. \tag{4.1}
\]

Consider the following one-block marginal hypothesis for a random balanced
Boolean path bank:

\[
 \begin{array}{l}
 \Pr(|V_s(S)|=m_s)=\eta_s,\\[2mm]
 \text{conditional on }|V_s(S)|=\ell,
 \quad V_s(S)\text{ is a uniform }\ell\text{-subset of }\mathcal U_s(S).
 \end{array}                                            \tag{4.2}
\]

No existence of a path law satisfying (4.2) is asserted.

### Proposition 4.1 (local hypergeometric first moment)

Under (4.2), for every (Q\subseteq\mathcal O),

\[
 \begin{aligned}
 \mathbb E e_s(Q)=\sum_{S\in\binom{[2r]}s}
 \biggl[
 &\eta_s\frac{(h_Q(S))_{m_s}}{(D_s)_{m_s}}\\
 &+(1-\eta_s)\frac{(h_Q(S))_{m_s+1}}{(D_s)_{m_s+1}}
 \biggr].                                               \tag{4.3}
 \end{aligned}
\]

In particular,

\[
 \mathbb E e_s(Q)\le\frac{C_s}{W}|Q|,                  \tag{4.4}
\]

and hence

\[
 \mathbb E Y(Q)\le\frac NW|Q|\le d|Q|.                \tag{4.5}
\]

### Proof

Formula (4.3) is the hypergeometric probability that all (ell) visitors
belong to the (h_Q(S)) eligible owners in (Q).  For (1\le\ell\le D_s),

\[
 \frac{(h)_\ell}{(D_s)_\ell}\le\frac h{D_s}.           \tag{4.6}
\]

Double counting pairs (S\subseteq T), with (T\in Q), gives

\[
 \sum_{S\in\binom{[2r]}s}h_Q(S)=|Q|\binom rs.           \tag{4.7}
\]

The full incidence count is

\[
 C_sD_s=W\binom rs.                                    \tag{4.8}
\]

Apply (4.6), (4.7), and (4.8) to (4.3) to obtain (4.4).  Multiply by
(w_s), sum, and use (1.5), proving (4.5). \(\square\)

The strict gap hidden in (4.4) is the relevant Boolean energy.  Define

\[
 \begin{aligned}
 \Delta(Q):=\frac NW|Q|-\sum_sw_s\sum_{S\in\binom{[2r]}s}
 \biggl[
 &\eta_s\frac{(h_Q(S))_{m_s}}{(D_s)_{m_s}}\\
 &+(1-\eta_s)\frac{(h_Q(S))_{m_s+1}}{(D_s)_{m_s+1}}
 \biggr]\ge0.                                          \tag{4.9}
 \end{aligned}
\]

For a pseudorandom (Q), many local densities lie strictly between zero
and one and (Delta(Q)) is large.  Coordinate stars have many local
densities equal to one and can have a much smaller, only macroscopic, gap.
There are very few coordinate stars compared with (\binom W{W/2}).  This
is why an entropy argument must be organized by local energy rather than
by cardinality alone.

Here is an exact conditional formulation of the remaining probabilistic
step.  Put

\[
 \begin{aligned}
 \mathcal M_Q(z):=\prod_s\prod_{S\in\binom{[2r]}s}
 \biggl(1+(z^{w_s}-1)\biggl[
 &\eta_s\frac{(h_Q(S))_{m_s}}{(D_s)_{m_s}}\\
 &+(1-\eta_s)\frac{(h_Q(S))_{m_s+1}}{(D_s)_{m_s+1}}
 \biggr]\biggr).                                      \tag{4.10}
\end{aligned}
\]

### Theorem 4.2 (local switching--container reduction)

Suppose there is a probability law on integral floor/ceiling-balanced
owner-path banks such that, for every (Q\subseteq\mathcal O) and every
(z\ge1),

\[
 \boxed{\mathbb E z^{Y(Q)}\le\mathcal M_Q(z).}           \tag{4.11}
\]

If in addition

\[
 \boxed{
 \sum_{\varnothing\ne Q\subsetneq\mathcal O}
 \inf_{z>1}z^{-(d|Q|+1)}\mathcal M_Q(z)<1,}             \tag{4.12}
\]

then some balanced owner-path bank satisfies every exact multisocket cut
(0.4).

### Proof

For a fixed (Q), a failed exact cut has an integer left side at least
(d|Q|+1).  Lemma 1.2 then gives (Y(Q)\ge d|Q|+1).  Markov's inequality
and (4.11) bound the probability of this event by the corresponding
summand in (4.12).  A union bound shows that with positive probability no
proper nonempty cut fails.  The empty cut is automatic for a balanced
cover, and the full cut is (N\le dW). \(\square\)

The two boxed hypotheses are deliberately separate.

* Equation (4.11) is the **local switching lemma**.  It must be proved for
  a law on compatible integral Boolean paths, not for independent abstract
  rank partitions.  One-block marginals such as (4.2) do not imply it,
  because visitor events at different ranks share path histories.
* Equation (4.12) is the **energy-sensitive entropy lemma**.  Replacing
  (mathcal M_Q) by a function of (|Q|) alone discards the distinction
  between generic owner families and low-boundary families such as
  coordinate stars.

Theorem 4.2 is an exact sufficient reduction, not a proof of either boxed
hypothesis.

## 5. Consecutive-layer balanced (b)-matchings

At a transition from rank (s+1) to rank (s), split the current path
flow into labelled occurrences ((T,U)) with (P_T(s+1)=U).  Join this
occurrence to the (s+1) children (S\subset U).  Prescribing every child
load to be (m_s) or (m_s+1) turns the transition into an integral
(b)-matching.  A sequence of compatible transition (b)-matchings is
exactly an integral balanced path flow.

Sampling uniformly, or with maximum entropy, from these (b)-matchings is
a natural construction.  The preceding results identify precisely what
such a sampling argument must and must not claim.

1. Inside a complete abstract box model, the factorial estimate (2.8)
   gives the required negative dependence directly.
2. In a Boolean transition graph, the support of a child block is
   (mathcal U_s(S)), not all (W) owners.  The coordinate-star theorem
   rules out global-density domination.
3. Conditioning consecutive transitions on common path histories can
   create positive cross-rank correlations.  Negative association of edge
   indicators in one matching, even when available, does not by itself
   imply the block-event moment inequality (4.11).
4. The correct switching proof must compare configurations while keeping
   all prescribed node loads integral and must pay for the local densities
   (h_Q(S)/D_s).
5. Even (4.11) leaves the nonuniform entropy sum (4.12).  A stability or
   container theorem for owner families of small energy (4.9) is then
   required.

There is an alternative complement-side target.  Lemma 1.3 says that on a
range of small complements it is enough to show that every owner set has
small induced weight in the random pair-meeting graph.  The deterministic
support (1.9) makes that graph Johnson-local.  This may be more tractable
than proving the full block MGF at those scales, but it still requires a
uniform switching/container argument over all owner subsets.

## 6. Final scope

The proposed random calculation has a proof-safe part and an unproved
part.

The proof-safe part is

\[
 \boxed{
 \begin{array}{c}
 \text{the exact Hall cut is capped union expansion (0.6);}\
 \text{the abstract uniform-block expectation is (0.8);}\
 \text{its normalized value is maximized at density one;}\
 \text{the abstract within-rank moment bound is (2.6);}\
 \text{Boolean containment requires local densities (0.12).}
 \end{array}}                                           \tag{6.1}
\]

The unsupported leap would be

\[
 \boxed{
 \text{abstract exchangeable partitions}
 \Longrightarrow
 \text{compatible balanced Boolean paths satisfying all cuts}.}          \tag{6.2}
\]

Coordinate stars rigorously invalidate that leap when it is based only on
the global density of (Q).  The exact remaining probabilistic theorem is
the local switching bound (4.11) together with the energy-sensitive entropy
bound (4.12), or an equally strong direct proof of the capped union
expansion (0.6).  Neither is proved here.  Residual nonadjacency, a literal
Ferrers boundary, and physical chronology are all later and stronger gates.
