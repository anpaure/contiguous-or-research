# Promotion rings: an exact block-factor hole floor and the superpolynomial correlation scale

Date: 2026-07-26

Method: pure mathematics. No computation or external theorem is used.

## 0. Outcome

Put

\[
 v=2m,\qquad M=m+H,\qquad
 W=\binom{2m}{m},\qquad N_H=\binom{2m}{m-H},
\]

and suppose throughout that

\[
 H=(1+o(1))\sqrt{m\log m},\qquad H=o(m).
\]

A **root** is a set \(A\in\binom{[2m]}{m-H}\), its top is
\(U_A=[2m]\setminus A\), and a cyclic frame on \(U_A\) selects the
\(M\) middle complements

\[
                 D=A\cup J,
 \tag{0.1}
\]

where \(J\) runs over the cyclic \(H\)-windows of the frame.  (Taking
complements converts these \(D\)'s into the literal middle owners in the
promotion-ring notes.)

Set

\[
 R=\binom mH,\qquad L=\binom MH,\qquad
 p={M\over L},\qquad
 \theta=Rp={MN_H\over W}.
 \tag{0.2}
\]

At the critical covering-side height, \(\theta=1+o(1)\).

This note proves the following exact obstruction to local correlated
rounding.

> **Block-factor hole theorem.** Partition the \(N_H\) roots into blocks
> of size at most \(b\). In each block choose its cyclic frames by an
> arbitrary joint law, but suppose distinct blocks are independent and
> every individual root frame has the uniform cyclic-frame marginal.
> Let \(Z\) be the number of middle targets \(D\in\binom{[2m]}m\) missed
> by all the full rings. If
> 
> \[
>                         bp\le\alpha<1,
> \tag{0.3}
> \]
> 
> then
> 
> \[
> \boxed{
>  \mathbb E Z\ge
>  W\exp\!\left(-{\theta\over1-\alpha}\right).}
> \tag{0.4}
> \]

In particular, if \(bp=o(1)\), then

\[
                         \mathbb E Z\ge(e^{-1}-o(1))W.
 \tag{0.5}
\]

Deleting blank phases or imposing tags can only increase this hole count.
Consequently no block-product law supported entirely on \(o(W)\)-hole
tagged selections can have \(b=o(1/p)\).  More quantitatively, such a law
forces

\[
 \boxed{
 b\ge(1-o(1)){1\over p}
   =(1-o(1)){\binom{m+H}{H}\over m+H}
   =(1-o(1)){1\over\theta}\binom mH.}
 \tag{0.6}
\]

There is also a targetwise strengthening.  In any such sequence of good
block-product laws, for every fixed \(\eta>0\), all but \(o(W)\) middle
targets \(D\) have a block satisfying

\[
 \boxed{
 |\mathcal B_j\cap\mathcal R(D)|
 \ge {1-\eta\over p}
 =(1-\eta+o(1))R.}
 \tag{0.6a}
\]

Thus almost every target must see almost its whole root star inside one
genuinely coupled block (after the usual diagonal choice
\(\eta=\eta_m\downarrow0\)).

At the critical height this is a superpolynomial correlation block:

\[
 \boxed{
 \log {1\over p}
   =\left({1\over2}+o(1)\right)
      \sqrt m\,(\log m)^{3/2}.}
 \tag{0.7}
\]

Thus the surviving vertical-frame theorem cannot come from independent
tops, bounded-size top trades, polynomial-size top blocks, or any
multiscale product construction whose largest genuinely coupled block is
\(\exp(o(\sqrt m(\log m)^{3/2}))\).  A successful symmetrized law must
couple essentially all \(\binom{m}{H}\) possible roots of almost every
middle target in one correlation block.

This is a no-go for local/product correlated rounding, not a
nonexistence theorem for a single globally designed selection.  A single
good deterministic selection, averaged over \(S_{2m}\), gives a law with
uniform marginals but global dependence, so it is fully consistent with
the theorem.

## 1. Root-middle normal form

Fix a middle target \(D\in\binom{[2m]}m\).  The roots capable of selecting
\(D\) are exactly

\[
             \mathcal R(D)=\{A\in\tbinom D{m-H}\},
 \tag{1.1}
\]

and hence

\[
                         |\mathcal R(D)|=R=\binom mH.
 \tag{1.2}
\]

For \(A\in\mathcal R(D)\), put \(J=D\setminus A\).  This is an
\(H\)-subset of \(U_A\).  A cyclic frame has \(M\) distinct \(H\)-windows,
and the symmetric group on \(U_A\) is transitive on its \(H\)-subsets.
Therefore a uniform cyclic frame selects \(D\) with probability

\[
                         p={M\over\binom MH}.
 \tag{1.3}
\]

The two binomial ratios satisfy

\[
 {R\over L}
 = {m!^2\over(m-H)!(m+H)!}
 = {N_H\over W}.
 \tag{1.4}
\]

Consequently the mean full-ring load of every middle target is

\[
                         Rp={MN_H\over W}=\theta.
 \tag{1.5}
\]

This recovers the exact fractional design directly in the
root-middle tight-cycle formulation.

## 2. Proof of the block-factor hole theorem

Let the root blocks be \(\mathcal B_1,\ldots,\mathcal B_s\).  For a fixed
middle target \(D\), define

\[
 X_{A,D}=\mathbf1\{\text{the frame at }A\text{ selects }D\},
 \qquad
 Y_{j,D}=\sum_{A\in\mathcal B_j\cap\mathcal R(D)}X_{A,D}.
 \tag{2.1}
\]

Write

\[
 r_{j,D}=|\mathcal B_j\cap\mathcal R(D)|,
 \qquad
 \mu_{j,D}=\mathbb EY_{j,D}=r_{j,D}p.
 \tag{2.2}
\]

No independence inside one block is assumed.  Markov's inequality alone
gives

\[
 \Pr(Y_{j,D}=0)
 =1-\Pr(Y_{j,D}\ge1)
 \ge1-\mathbb EY_{j,D}
 =1-\mu_{j,D}.
 \tag{2.3}
\]

By (0.3), \(0\le\mu_{j,D}\le bp\le\alpha<1\).  The blocks are
independent, so

\[
 \Pr(D\text{ is missed})
 =\prod_j\Pr(Y_{j,D}=0)
 \ge\prod_j(1-\mu_{j,D}).
 \tag{2.4}
\]

For \(0\le x\le\alpha<1\),

\[
                   \log(1-x)\ge-{x\over1-x}
                                      \ge-{x\over1-\alpha}.
 \tag{2.5}
\]

Moreover (1.2)--(1.5) give

\[
                         \sum_j\mu_{j,D}=Rp=\theta.
 \tag{2.6}
\]

Taking logarithms in (2.4), applying (2.5)--(2.6), and exponentiating
proves

\[
 \Pr(D\text{ is missed})
 \ge\exp\!\left(-{\theta\over1-\alpha}\right).
 \tag{2.7}
\]

Summing (2.7) over the \(W\) middle targets proves (0.4).  If \(bp=o(1)\)
and \(\theta=1+o(1)\), use \(\alpha=bp\) in the proof to obtain (0.5).

Finally, blanks only delete selected middle targets.  Hence every target
missed by all full rings is also missed after blank deletion, regardless
of the tag placement.  This proves the tagged assertion.  If a sequence
of block-product laws is supported on selections having \(o(W)\) holes,
then its expected number of holes is \(o(W)\).  Equation (0.4) rules this
out whenever \(bp\le1-\eta\) for some fixed \(\eta>0\).  Letting
\(\eta\downarrow0\) proves the necessary scale (0.6).  \(\square\)

For completeness, retain the target-dependent maximum

\[
 \alpha_D=p\max_j r_{j,D}.
 \tag{2.8}
\]

The same proof, with \(\alpha_D\) in place of the global \(\alpha\), gives

\[
 \Pr(D\text{ is missed})
 \ge\exp\!\left(-{\theta\over1-\alpha_D}\right)
 \qquad(\alpha_D<1).
 \tag{2.9}
\]

If a fixed \(\eta>0\) and a positive fraction of targets satisfied
\(\alpha_D\le1-\eta\), (2.9) would force a positive linear expected hole
count.  A law supported on \(o(W)\)-hole selections cannot do this.
Therefore all but \(o(W)\) targets have
\(\alpha_D>1-\eta\), which is precisely (0.6a).

## 3. Critical asymptotics of the correlation block

Since \(H=o(M)\), Stirling's formula gives

\[
 \log\binom MH
 =H\log{M\over H}+H
  +O\!\left({H^2\over M}+\log H\right).
 \tag{3.1}
\]

Therefore

\[
 \log{1\over p}
 =H\log{M\over H}+H-\log M
  +O\!\left({H^2\over M}+\log H\right).
 \tag{3.2}
\]

At \(H=(1+o(1))\sqrt{m\log m}\) and \(M=m+H=(1+o(1))m\),

\[
 \log{M\over H}
 ={1\over2}\bigl(\log m-\log\log m\bigr)+o(\log m).
 \tag{3.3}
\]

The first term in (3.2) dominates all the others, and (0.7) follows.

The equivalent expression in terms of \(R\) follows exactly from
\(Rp=\theta\):

\[
                         {1\over p}={R\over\theta}.
 \tag{3.4}
\]

Thus a typical middle target's whole root star, up to the harmless factor
\(\theta=1+o(1)\), is the necessary correlation scale.

## 4. Pair-covariance calibration

The same scale appears already at second order.  Suppose merely that root
frames have uniform marginals and that nonadjacent roots in a dependency
graph are pairwise independent.  If the graph has maximum degree
\(\Delta\), then for every \(D\), at least

\[
                         \binom R2-{R\Delta\over2}
 \tag{4.1}
\]

pairs in \(\mathcal R(D)\) are independent.  Hence, if \(L_D\) is the
full-ring load,

\[
 \mathbb E\binom{L_D}{2}
 \ge p^2\left(\binom R2-{R\Delta\over2}\right)
 ={\theta^2\over2}
  \left(1-{\Delta+1\over R}\right).
 \tag{4.2}
\]

After summing over \(D\), cancellation of the independent pair baseline
to \(o(W)\) requires

\[
                         \Delta=(1-o(1))R.
 \tag{4.3}
\]

Equation (4.2) is only a quadratic calibration: by itself it does not
turn an \(L^2\) lower bound into an \(L^1\) hole lower bound, because high
multiplicities may concentrate.  The block theorem is stronger precisely
because independence of whole blocks lets (2.4) control literal holes.

## 5. Boundary and use

What is proved:

1. the exact root-middle parameters \(R,L,p,\theta\);
2. the literal middle-hole lower bound (0.4), with arbitrary dependence
   inside each block;
3. the necessary block scale (0.6)--(0.7) for any block-product law
   supported on good selections;
4. the targetwise root-star concentration (0.6a); and
5. the matching pair-covariance scale (4.3).

What is not proved:

1. nonexistence of a single globally correlated good frame selection;
2. a higher-degree integral-hull inequality valid against such a global
   selection; or
3. the tuned vertical-frame theorem.

The practical conclusion is nevertheless sharp.  The unresolved theorem
is not a matter of correlating neighboring tops or packing a polynomial
number of local alternating circuits.  At the critical height, one must
coordinate essentially the entire superpolynomial root star of a typical
middle target, and then do so coherently across all targets and all nested
annular ranks.
