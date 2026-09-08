# AD22: dependent cyclic-order rounding needs global covariance

Date: 2026-07-25

Pure mathematics only.  No computation, search, solver, or web input is
used.

## 0. Outcome

Use the calibrated first crossing

\[
 H=\min\{h:\lambda_h\ge m+h\},\qquad M=m+H,
 \qquad S=M N_H=(1-o(1))W,                                \tag{0.1}
\]

and choose one cyclic order in every top
\(U\in\binom{[2m]}M\).  Put

\[
 Q=\left\lfloor\sqrt{m\log\log m}\right\rfloor.            \tag{0.2}
\]

The choice in one top is one nested column: the same cyclic order supplies
all interval ranks.  No rankwise resampling is allowed below.

This report proves a sharp obstruction to local or pairwise-independent
dependent rounding.

1. At rank \(r=m\pm q\), \(q\le Q\), let \(Z_T\) be the number of selected
   packets containing target \(T\), let

   \[
    \mu_q=\frac{S}{N_q},\qquad k_q=\lfloor\mu_q\rfloor,
    \qquad\theta_q=\mu_q-k_q,
   \]

   and define the exact floor energy

   \[
    F_q=\sum_T(Z_T-k_q)(Z_T-k_q-1).                         \tag{0.3}
   \]

   If every top order has the uniform marginal and distinct tops are
   pairwise independent, then

   \[
    \mathbb EF_q
    =N_q\bigl(k_q+\theta_q^2-\mu_qp_q\bigr)
    =\Theta(W),                                             \tag{0.4}
   \]

   uniformly through \(q\le Q\), where

   \[
    p_q=\frac{M}{\binom{M}{m\pm q}}.
   \]

2. For an arbitrary marginal-uniform dependent rounding, (0.4) acquires
   exactly twice the summed cross-top covariance.  Achieving
   \(\mathbb EF_q=o(W)\) therefore requires negative covariance
   \(-\Theta(W)\) at every shallow rank, hence \(-\Theta(QW)\) in
   aggregate.

3. Suppose the top-valued random variables have a dependency graph of
   maximum degree \(\Delta\).  Put

   \[
    h_*=H-Q,qquad
    b_*={h_*M\over\binom M{h_*}}.                            \tag{0.5}
   \]

   If

   \[
    \Delta\le {M\over6b_*}
    ={1\over6h_*}\binom M{h_*},                             \tag{0.6}
   \]

   then

   \[
    \mathbb EF_q\ge S/6                                    \tag{0.7}
   \]

   at every one of the \(2Q+1\) middle and two-sided shallow ranks.
   Thus every polynomial-degree, bounded-range, or pairwise-independent
   scheme fails by an enormous margin.  A successful symmetric rounding
   must correlate each top with at least

   \[
    \Omega\!\left({1\over H}\binom M{H-Q}\right)            \tag{0.8}
   \]

   other tops, or use a mechanism not represented by a bounded dependency
   graph.

4. Let

   \[
    E_q=\sum_T\bigl[(k_q-Z_T)_+
                +(Z_T-k_q-1)_+\bigr]                       \tag{0.9}
   \]

   be the exact balanced-load excess.  If all shallow target loads are at
   most \(L\), then under (0.6)

   \[
    \mathbb E\sum_{|q|\le Q}E_q
       \ge { (2Q+1)S\over6(L+1)}.                           \tag{0.10}
   \]

   In particular, the natural bound \(L=O(\log m)\) gives
   \(\omega(W)\), not \(o(W)\), aggregate excess.  More generally, an
   \(o(W)\) aggregate target would force multiplicity spikes
   \(L/Q\to\infty\) if the dependence remains local.

5. Fixed-top four-order exchanges do not evade this theorem.  On a
   one-packet-per-top transversal no elementary negative pair is present;
   batching fixed-top rectangles gives no nonzero legal trade with at most
   one packet per top.  Allowing owner load two makes the pair present but
   preserves its owner-defect vector forever.

This does not refute a global dependent rounding or the calibrated
augmented perfect matching.  It proves that such a rounding must be
genuinely global and must build the nested negative covariance, rather
than obtain it from independent orders, bounded-degree resampling, a
bounded-multiplicity martingale, or fixed-top local rectangles.

## 1. Exact one-target marginals through the growing shallow window

Fix a proper rank \(r=m\pm q<M\), and put

\[
 h=M-r=H\mp q,qquad
 B_r=\binom Mr,qquad p_r={M\over B_r}.                     \tag{1.1}
\]

A uniformly random cyclic order of a containing top has exactly \(M\)
rank-\(r\) intervals among the \(B_r\) possible \(r\)-subsets, so it hits
a prescribed target with probability \(p_r\).

The number of tops containing a prescribed target is

\[
 a_r=\binom{2m-r}{M-r}.                                    \tag{1.2}
\]

Consequently

\[
 a_rp_r={MN_H\over\binom{2m}{r}}
 ={S\over N_q}=:\mu_q.                                    \tag{1.3}
\]

At the calibrated crossing,

\[
 c={\lambda_H\over M}=1+O(H/m),qquad
 \mu_q={\lambda_q\over c}.                                \tag{1.4}
\]

Uniformly for \(q\le Q\),

\[
 {1\over2}\le\mu_q\le (1+o(1))\log m.                    \tag{1.5}
\]

Indeed \(\mu_0=1/c=1-o(1)\), while

\[
 \log\lambda_q={q^2\over m}
 +O\!\left({q\over m}+{q^3\over m^2}\right)
 \le\log\log m+o(1).                                     \tag{1.6}
\]

Moreover \(Q=o(H)\), so

\[
 H-Q\le h\le H+Q=(1+o(1))H.                              \tag{1.7}
\]

The interval probability in (1.1) is uniformly superpolynomially small:

\[
 p_r\le {M\over\binom M{H-Q}}=o(m^{-K})                   \tag{1.8}
\]

for every fixed \(K\).

## 2. The exact covariance identity

Let \(\Pi_U\) be the selected cyclic order in top \(U\).  Assume only
that each \(\Pi_U\) is marginally uniform; arbitrary dependence between
different tops is allowed.  For \(T\subset U\), let

\[
 I_{U,T}={\bf1}_{\{T\text{ is a cyclic interval of }\Pi_U\}}.
\]

Then

\[
 Z_T=\sum_{U\supset T}I_{U,T},qquad \mathbb EZ_T=\mu_q.    \tag{2.1}
\]

Put

\[
 \mathcal C_r=sum_T\sum_{U<V\,:\,U,V\supset T}
            \operatorname{Cov}(I_{U,T},I_{V,T}).            \tag{2.2}
\]

### Theorem 2.1 (floor-energy covariance identity)

Writing \(k=k_q\) and \(\theta=\theta_q\),

\[
 \boxed{
 \mathbb EF_q
 =N_q\bigl(k+\theta^2-\mu_qp_r\bigr)+2\mathcal C_r.}        \tag{2.3}
\]

#### Proof

For one target,

\[
 \begin{split}
 \mathbb E(Z_T-k)(Z_T-k-1)
 &=\operatorname{Var}(Z_T)
   +(\mu_q-k)(\mu_q-k-1)\\
 &=\operatorname{Var}(Z_T)-\theta(1-\theta).               \tag{2.4}
 \end{split}
\]

The diagonal Bernoulli variances sum to

\[
 \sum_T\sum_{U\supset T}p_r(1-p_r)
 =N_qa_rp_r(1-p_r)
 =N_q\mu_q(1-p_r).                                         \tag{2.5}
\]

The off-diagonal variances sum to \(2\mathcal C_r\).  Finally

\[
 \mu_q-\theta(1-\theta)
 =k+\theta^2,                                               \tag{2.6}
\]

which gives (2.3). \(\square\)

If distinct tops are pairwise independent, \(\mathcal C_r=0\), proving
(0.4).  The scale is uniformly linear in \(W\).  Indeed, if \(k=0\),
then \(\theta=\mu_q\ge1/2\), so

\[
 N_q\theta^2=S\theta\ge S/2.                              \tag{2.7}
\]

If \(k\ge1\), then \(\mu_q<k+1\le2k\), so

\[
 N_qk={S k\over\mu_q}\ge S/2.                             \tag{2.8}
\]

By (1.8), the subtracted term \(N_q\mu_qp_r=Sp_r=o(S)\).
Thus

\[
 N_q(k+\theta^2-\mu_qp_r)\ge S/3                          \tag{2.9}
\]

for all sufficiently large \(m\), uniformly through the window.

Equation (2.3) now quantifies the required dependence: to make one rank's
expected energy \(o(W)\), one needs

\[
 \mathcal C_r\le-S/6+o(W).                                 \tag{2.10}
\]

Summed through the \(2Q+1\) ranks, the required negative covariance is
\(-\Omega(QW)\).

## 3. Capacity of one dependent top pair

Let two distinct tops \(U,V\) have distance

\[
 t=|U\setminus V|=|V\setminus U|\ge1.
\]

For fixed \(r\), their total covariance contribution is

\[
 \Gamma_{UV}^{(r)}
 =\sum_{T\subset U\cap V,\ |T|=r}
       \operatorname{Cov}(I_{U,T},I_{V,T}).                 \tag{3.1}
\]

Joint probabilities are nonnegative, hence

\[
 \Gamma_{UV}^{(r)}
 \ge-\binom{M-t}{r}p_r^2.                                  \tag{3.2}
\]

The right side is largest in magnitude at \(t=1\).  Since

\[
 \binom{M-1}{r}={M-r\over M}\binom Mr={h\over M}B_r,
\]

we obtain the exact uniform bound

\[
 \boxed{
 \Gamma_{UV}^{(r)}\ge-b_r,qquad
 b_r={hM\over\binom Mh}.}                                  \tag{3.3}
\]

The exact consecutive ratio for the function \(h/\binom Mh\) is

\[
 { (h+1)/\binom M{h+1}\over h/\binom Mh}
 ={(h+1)^2\over h(M-h)}.
\]

It is less than one throughout our actual window
\(h=H+O(Q)=o(M)\).  Therefore (1.7) gives

\[
 b_r\le b_*={h_*M\over\binom M{h_*}},qquad h_*=H-Q.        \tag{3.4}
\]

This is the most negative covariance one top pair can supply at one rank,
regardless of how their two cyclic orders are coupled.

## 4. Bounded dependency cannot flatten one rank

Suppose the family \((\Pi_U)_U\) has a dependency graph \(G\): random
orders indexed by disjoint vertex sets with no graph edge between them are
independent.  Let its maximum degree be \(\Delta\).  Nonedges have zero
covariance, so (3.3)--(3.4) give

\[
 \mathcal C_r
 \ge-|E(G)|b_*
 \ge-{N_H\Delta b_*\over2}.                               \tag{4.1}
\]

Since \(S=MN_H\), equations (2.3), (2.9), and (4.1) imply

\[
 \mathbb EF_q
 \ge {S\over3}-N_H\Delta b_*.                             \tag{4.2}
\]

If (0.6) holds, the last term is at most \(S/6\), proving (0.7).

The threshold in (0.6) is enormous.  Uniformly,

\[
 \log\binom M{H-Q}
 =(1+o(1))(H-Q)\log\frac{M}{H-Q}\longrightarrow\infty     \tag{4.3}
\]

faster than any multiple of \(\log m\).  Thus no polynomial-degree
dependency graph comes close to the required covariance.

This theorem includes pairwise-independent rounding as \(\Delta=0\).  It
also includes any bounded-range scheme in which each top's final order is
a function of random seeds shared with only \(\Delta\) other tops.  It
does not include a global permutation, a global matching, or a long
exchange process whose dependence propagates through the entire top graph.

Any deterministic successful selection can of course be randomized by a
uniform global coordinate relabelling.  That symmetrized law has the
uniform marginals assumed here, but the one global relabelling couples all
tops and gives a complete dependency graph.  Thus symmetrization does not
contradict the theorem; it exhibits exactly the global-dependence escape
left open by it.

## 5. From floor energy to aggregate collision excess

For an integral load \(z\),

\[
 (z-k)(z-k-1)=
 \begin{cases}
  d(d+1),&z=k-d<k,\\
  0,&z\in\{k,k+1\},\\
  e(e+1),&z=k+1+e>k+1.
 \end{cases}                                                \tag{5.1}
\]

Thus \(F_q\ge2E_q\), but that direction alone does not turn a quadratic
lower bound into a linear lower bound.  A load cap does.

### Proposition 5.1 (bounded-multiplicity consequence)

If \(0\le Z_T\le L\) for every target in the window, then

\[
 F_q\le(L+1)E_q.                                            \tag{5.2}
\]

Consequently, under (0.6),

\[
 \mathbb E\sum_{|q|\le Q}E_q
 \ge{(2Q+1)S\over6(L+1)}.                                  \tag{5.3}
\]

#### Proof

In the deficit case of (5.1), \(d\le k\le L\), so
\(d(d+1)\le(L+1)d\).  In the surplus case,
\(e+1\le L+1\), so \(e(e+1)\le(L+1)e\).  Sum over targets and then use
(0.7) at all \(2Q+1\) ranks. \(\square\)

For \(L=O(\log m)\),

\[
 {Q\over L}
 \asymp{\sqrt{m\log\log m}\over\log m}\longrightarrow\infty,           \tag{5.4}
\]

so (5.3) is \(\omega(W)\).  Even the desired balanced scale
\(L\asymp\max_{q\le Q}\mu_q=O(\log m)\) is therefore incompatible with
bounded-degree dependence.

At the middle rank, \(k_0=0\) and

\[
 F_0=\sum_X Z_X(Z_X-1).                                    \tag{5.5}
\]

If owner multiplicities are bounded by two, this is exactly twice the
owner-collision excess.  Therefore (0.6) already forces expected middle
collision excess at least \(S/12\).  The cap-two relaxation does not even
produce an owner near-transversal under local dependence.

Without a load cap, a large factorial moment can be concentrated on very
rare, very high target spikes.  Equations (2.3)--(4.2) then do not by
themselves rule out \(o(W)\) linear excess.  The exact surviving escape is
therefore explicit: a local-dependence construction would need target
multiplicity \(\omega(Q)\), far above the balanced clone loads, or else it
must abandon local dependence.

## 6. Why fixed-top local exchanges do not create the covariance

The four-order rectangle identity changes two old orders to two new orders
inside one top.  A one-order-per-top selection contains neither negative
pair.  More strongly, the exact rectangle-lattice audit proves:

* the complete middle-owner vector is preserved separately in each top by
  every nonmiddle rank-selector square;
* any sum whose two signs are owner packings and use at most one packet per
  top has zero interval effect at every rank; and
* a same-top negative diagonal pair shares at least \(M-4\) middle owners.

Thus a local-exchange martingale cannot even start inside the calibrated
matching state space.  Enlarging the state space to owner load at most two
makes the pair present, but all rectangle moves preserve the resulting
owner holes and doubles exactly.  Restricting packet variables to
\(\{0,2\}\) additionally makes every target correction even.

A viable exchange martingale must therefore use the nonlocal owner-transfer
circulations: owner-changing packet replacements in different tops whose
middle effects cancel only globally.  Such a process necessarily lies
outside the bounded fixed-top dependency model proved impossible above.

## 7. Exact boundary

The report proves no invariant against an arbitrary global distribution on
one cyclic order per top.  In particular, a perfect matching in the
calibrated augmented packet hypergraph can have the required correlations.

What is closed is the broad local class:

1. independent or pairwise-independent topwise order selection;
2. any marginal-uniform rounding with dependency degree below (0.8);
3. any such rounding with balanced multiplicities \(O(\log m)\) and target
   aggregate excess \(o(W)\); and
4. fixed-top rectangle exchange or cap-two variants.

The next positive theorem must directly construct a global nested
covariance or a packet matching.  Rankwise concentration, bounded-degree
resampling, and post-hoc local repair cannot provide the required scale.
