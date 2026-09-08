# Independent audit: random balanced paths and the local-density switching gate

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_RANDOM_BALANCED_PATH_LOCAL_DENSITY_AND_SWITCHING_GATE_20260804.md`  
**Verdict:** all unconditional identities, probability calculations, and
obstructions are correct.  The local moment and entropy statements are
explicitly conditional and are not proved by the note.  In particular the
note does not claim the missing owner-path Hall theorem.  No computation is
used in this audit.

## 1. Claims separated by logical status

The audited note contains four unconditional pieces.

1. It conjugates the owner-subset Hall cuts into a capped union-expansion
   inequality for the complementary path family.
2. It calculates the expectation and an exponential moment bound for
   independent uniform abstract partitions with prescribed floor/ceiling
   block sizes.
3. It proves that this global exchangeable model cannot be the marginal
   law of Boolean visitor blocks, using coordinate stars.
4. It derives the correct local eligible-owner first moment under an
   explicitly stated local-uniformity hypothesis.

The final switching MGF and container sum are hypotheses of a conditional
theorem.  They are not presented as consequences of random
consecutive-layer (b)-matchings.  This distinction is essential and is
maintained throughout.

## 2. Conjugate cut audit

Fix (Q\subseteq\mathcal O) and (R=\mathcal O\setminus Q).  A target
(S) is counted by (e_s(Q)) exactly when no path in (R) visits it.
Because the path bank covers every target in the ranks under discussion,
the number not counted is the number (u_s(R)) of distinct targets hit by
(R).  Hence

\[
                         e_s(Q)=C_s-u_s(R).             \tag{2.1}
\]

With (N_s=C_s-b_s),

\[
 (e_s(Q)-b_s)_+
 =(N_s-u_s(R))_+
 =N_s-\min\{N_s,u_s(R)\}.                              \tag{2.2}
\]

The Hall inequality becomes

\[
 N-\sum_s\min\{N_s,u_s(R)\}\le d(W-|R|).              \tag{2.3}
\]

Substituting (N=dW-L) gives exactly

\[
 \sum_s\min\{N_s,u_s(R)\}\ge d|R|-L.                 \tag{2.4}
\]

There is no lost endpoint or reversed sign.  At the full complement
(R=\mathcal O), the left side is (N), equal to (dW-L); at the empty
complement both sides are zero.

The boundary-weight inequality is also correct.  If (e>b),

\[
 e-b\le e(1-b/C)
\]

is equivalent to (e\le C); if (e\le b), its left side is zero.  Thus
((e-b)_+\le((C-b)/C)e) on the entire allowed interval.

For the pair reduction, at a fixed rank

\[
 |R|-u_s(R)=\sum_{A:n_A>0}(n_A-1)
 \le\sum_A\binom{n_A}2.                                \tag{2.5}
\]

Summing counts each unordered pair once for every rank at which it meets.
The condition (|R|\le N_s) ensures (u_s(R)\le N_s), so the cap is
inactive on the chosen rank set.  The displayed sufficient pair-meeting
bound follows.  Finally, a common rank-(s) node lies inside both owners,
so (s\le|T\cap U|).  All parts of Lemma 1.3 are valid.

**Audit conclusion:** the expansion reformulation and small-complement
pair witness are exact.

## 3. Abstract uniform-partition expectation

The block counts satisfy

\[
 a_s+c_s=C_s,qquad m_sa_s+(m_s+1)c_s=W.                \tag{3.1}
\]

For a fixed labelled block of size (ell), a uniformly random placement
of the (W) labels puts the whole block inside a fixed (q)-set with
probability

\[
                         \frac{(q)_\ell}{(W)_\ell}.      \tag{3.2}
\]

There are (a_s) blocks of size (m_s) and (c_s) blocks of size
(m_s+1), proving the stated expectation.

For (q\ge1),

\[
 \frac1q\frac{(q)_\ell}{(W)_\ell}
 =\frac1W\frac{(q-1)_{\ell-1}}{(W-1)_{\ell-1}}.        \tag{3.3}
\]

As (q) increases through the integers, every numerator factor is
nondecreasing.  The quotient is zero before (q\ge\ell), so there is no
boundary exception.  Thus each summand divided by (q) is nondecreasing.
At (q=W), all block probabilities are one and the normalized expectation
is ((a_s+c_s)/W=C_s/W).  Multiplication by
(w_s=(C_s-b_s)/C_s) and summation gives

\[
 \frac1q\mathbb EY(Q)\le
 \sum_s\frac{C_s-b_s}{W}=\frac NW\le d.                \tag{3.4}
\]

This verifies exactly, rather than asymptotically, the proposed claim that
the normalized uniform-block expectation is maximized at density one.

**Audit conclusion:** Theorem 2.1 and the boundary weighting are correct.

## 4. Factorial moment bound and entropy criterion

Let (I_B) indicate capture of a labelled block (B).  For disjoint boxes
of total size (K), joint capture has probability ((q)_K/(W)_K).  If
their separate sizes are (ell_1,\ldots,\ell_t), then

\[
 \frac{(q)_K}{(W)_K}
 \le\prod_i\frac{(q)_{\ell_i}}{(W)_{\ell_i}}.           \tag{4.1}
\]

To check the direction, write each ratio as products of
(f(j)=(q-j)/(W-j)).  Since (q\le W), (f(j)) is nonincreasing in (j).
The joint probability uses one uninterrupted product, while the right side
restarts at the larger initial factors for each block.  Hence (4.1) is
correct.

Expanding

\[
 \prod_B(1+(z^{w_s}-1)I_B)                              \tag{4.2}
\]

has nonnegative coefficients for (z\ge1).  Applying (4.1) termwise gives
the two binomial factors in the theorem.  Independence of the abstract
partitions at different ranks legitimately multiplies these moment bounds.

If an exact Hall cut fails, its integer left side is at least (d|Q|+1).
The deterministic boundary-weight bound makes (Y(Q)) at least the same
quantity.  Markov's inequality gives the displayed (H_r(q)); summing over
the (\binom Wq) fixed sets is a valid union bound.  The endpoint (Q=X)
is not included and is controlled exactly by (N\le dW).

The corollary says only that the explicit finite inequality implies
existence in the abstract partition model.  It does not assert the finite
inequality, nor Boolean compatibility.

**Audit conclusion:** the moment and entropy reductions are sound and
properly scoped.

## 5. Coordinate-star obstruction

For fixed (x), the number of middle owners containing (x) is

\[
 \binom{2r-1}{r-1}=\frac12\binom{2r}r=W/2.              \tag{5.1}
\]

Every visitor of a target (S\ni x) must be an owner containing (S),
and hence belongs to (Q_x).  Therefore all
(\binom{2r-1}{s-1}) such targets are forced into (Q_x).  The identity

\[
 \binom{2r-1}{s-1}=\frac{s}{2r}\binom{2r}s             \tag{5.2}
\]

proves the rankwise lower bound.

For the total, substitute (t=s-1):

\[
 \sum_{s=1}^{r-1}\binom{2r-1}{s-1}
 =\sum_{t=0}^{r-2}\binom{2r-1}t
 =2^{2r-2}-\binom{2r-1}{r-1}
 =2^{2r-2}-W/2.                                         \tag{5.3}
\]

If (m_s\ge2), every block in the abstract benchmark has size at least
two.  At (q=W/2), its capture probability is at most (1/4), so the
whole expectation is at most (C_s/4).  When (s>r/2), the forced Boolean
lower bound ((s/(2r))C_s) is strictly larger.  Thus global exchangeability
and density-only stochastic domination are genuinely impossible.

This argument does not compare the sum of forced targets with (dW/2),
and hence does not claim that (Q_x) violates Hall.  The audited note states
exactly this narrower scope.

**Audit conclusion:** Theorem 3.1 is correct and is a sharp obstruction to
the proposed density-only random model, not to all balanced path banks.

## 6. Local eligible-owner calculation

For a fixed rank-(s) target,

\[
 D_s=\binom{2r-s}{r-s}.                                 \tag{6.1}
\]

Under the explicit local-uniform marginal hypothesis, conditional capture
probability is hypergeometric, yielding formula (4.3) in the main note.
For every (ell\ge1),

\[
 \frac{(h)_\ell}{(D)_\ell}
 =\frac hD\prod_{j=1}^{\ell-1}\frac{h-j}{D-j}
 \le\frac hD.                                          \tag{6.2}
\]

Double counting incidences with owners in (Q) gives

\[
 \sum_Sh_Q(S)=|Q|\binom rs.                             \tag{6.3}
\]

Double counting all incidences gives

\[
 C_sD_s=W\binom rs.                                    \tag{6.4}
\]

Hence the sum of the local capture benchmarks is at most
((C_s/W)|Q|).  The weighted sum is at most ((N/W)|Q|).  This part uses
only the stated marginal hypothesis and makes no assertion that the
hypothesis follows from a uniform (b)-matching.

The quantity (Delta(Q)) is nonnegative by exactly the same inequalities.
Its interpretation as an energy is descriptive; no quantitative stability
claim about it is made.

**Audit conclusion:** Proposition 4.1 is a correct conditional
first-moment statement.

## 7. Conditional switching--container theorem

Assume the MGF domination (4.11) of the main note.  If a fixed cut fails,
the deterministic boundary weighting and Markov's inequality give

\[
 \Pr(Q\text{ fails})
 \le\inf_{z>1}z^{-(d|Q|+1)}\mathcal M_Q(z).             \tag{7.1}
\]

Summing (7.1) over all proper nonempty (Q) proves existence whenever the
sum is below one.  This is a standard first-moment argument with no missing
logical step.

What is missing mathematically is precisely what the theorem labels as a
hypothesis:

* a distribution on *compatible integral balanced Boolean paths* satisfying
  the local block-event MGF domination across all ranks; and
* a proof that the resulting nonuniform entropy sum is below one.

One-block local marginals do not imply the MGF statement.  A sequence of
consecutive-layer (b)-matchings shares owner histories, so block-capture
events can be positively correlated between ranks.  Conversely, ordinary
negative dependence inside one matching does not automatically control
that cross-rank product.  The note correctly refuses both inferences.

**Audit conclusion:** Theorem 4.2 is a valid exact reduction and contains
no hidden claim that its two substantive hypotheses have been established.

## 8. Final verdict

The audited note proves a useful but deliberately incomplete conclusion:

\[
 \boxed{
 \begin{array}{c}
 \text{uniform abstract blocks have the proposed monotone expectation;}\\
 \text{within one abstract rank they have an exact factorial MGF bound;}\\
 \text{Boolean paths cannot obey the global-density model;}\\
 \text{local eligible-owner densities give the correct benchmark;}\\
 \text{local switching plus low-energy containers is the exact open gate.}
 \end{array}}                                           \tag{8.1}
\]

No full named lower-chain factor, no proof of the multisocket conjecture,
no residual nonadjacency lift, and no chronology result follows.  The
scope statements in the theorem are therefore accurate.
