# Literal-link repair and the containment-energy martingale for RPRN

Date: 2026-07-26

Scope: constant-one repaired promotion-ring packing only.  This note has
two purposes.  First, it repairs the support-reachable obstruction by
distinguishing static containment from an actual surviving root--owner
link.  Second, it determines how that obstruction can arise under the
unbiased slow nibble.

## 0. Verdict

Put

\[
 W=\binom{2m}{m},\qquad N_H=\binom{2m}{m-H},\qquad
 M=m+H,\qquad Q=\binom MH,
\]

and let \(R,D=\rho R\) be the root and owner degrees of the repaired
catalogue.

The reachable construction is a genuine literal-link counterexample.
For \(\delta=1/400\), it gives a matching of size \(o(N_H)\) and a family
\(\mathcal F'\) of \(o(W)\) surviving owners such that

\[
 (1-40\delta-o(1))D
 \le d_{\rm res}(X)
 \le(1-\delta/2)D\qquad(X\in\mathcal F'),              \tag{0.1}
\]

while at least

\[
 (1-80\delta-o(1))N_H=(4/5-o(1))N_H                 \tag{0.2}
\]

surviving roots have an actual surviving catalogue edge with some
\(X\in\mathcal F'\).  Static containment is not used as a surrogate in
(0.2).

The stochastic conclusion is different.

* In one fresh unbiased bite with \(\gamma\le\delta/100\), the probability
  of creating such a root-covering constant-defect family is

  \[
     Q\exp[-\Omega_\delta(m^2)]=o(1).                 \tag{0.3}
  \]

* Along \(T=O_z(m)\) slow bites, stopped while the current path-influence
  estimate remains valid, the probability that martingale noise creates
  an actual-link family covering \(\eta N_H\) roots and lying a fixed
  factor below its predictable degree trajectory is

  \[
    {TQ\over\eta}\exp[-\Omega_{z,\varepsilon}(m)]=o(1). \tag{0.4}
  \]

Thus the support-reachable obstruction is not a typical fluctuation of
the unbiased nibble.  If an unbiased trajectory creates it with
nonnegligible probability, then before its creation one of two things must
happen:

1. the repaired path-influence bound itself ceases to regenerate; or
2. a root-covering owner family acquires a systematically adverse
   predictable marked-conflict/acceptance drift.

The second alternative contains path-link clustering and nonuniform
isolation slack in compensator form.  The containment-energy martingale
removes random fluctuation as a third possibility; it does not, by itself,
prove that the predictable accepted-loss drift is uniform.

## 1. The literal residual-link repair

For a residual catalogue \(\mathcal H_{\rm res}\), define

\[
 \Lambda_{\rm res}(A,X)
 =\mathbf1_{\{\exists f\in\mathcal H_{\rm res}:A,X\in f\}}.      \tag{1.1}
\]

The assertion \(A\subset X\) is only static containment.  The assertion
\(\Lambda_{\rm res}(A,X)=1\) is the literal residual link.

The sparse scheduling lemma in the repaired counterexample can be run
with the following extra pruning.  If \(\mathcal M_X\) denotes the edges
chosen while processing the centre \(X\), then the width-two influence
bound gives

\[
 \sum_{e\in\mathcal M_X}a_X(e)
 \le 2\delta m^2{20+o(1)\over m^2}D
 =(40\delta+o(1))D.                                  \tag{1.2}
\]

For the edges chosen at other centres, reverse the conflict count.  For
every fixed edge \(e\),

\[
 {1\over W}\sum_X{a_X(e)\over D}
 \le {r(R+rD)\over WD}=O(m^2/W).                    \tag{1.3}
\]

The matching has size \(O(\alpha Wm^2)\), where

\[
 \alpha={m^2\over Q}.
\]

Consequently the mean cross-centre loss, normalized by \(D\), is

\[
 O\!\left({|\mathcal M|m^2\over W}\right)
 =O(\alpha m^4)=o(1).                                  \tag{1.4}
\]

Markov pruning removes only \(o(|\mathcal F|)\) centres and makes the
cross-centre sum \(o(D)\) at every remaining centre.  Since a deleted
option through \(X\) is counted by at least one of the quantities
\(a_X(e)\), (1.2)--(1.4) imply the lower bound in (0.1).  The
distance-one double count from the original construction gives the upper
bound in (0.1).

For \(A\subset X\), the original root--owner pair degree is exactly

\[
 K=d(A,X)={rR\over Q}={D\over\binom mH}.              \tag{1.5}
\]

Residual edges through \(X\) are partitioned by their root, and every
nonempty residual root-link contributes at most \(K\) edges.  Hence

\[
 \sum_A\Lambda_{\rm res}(A,X)
 \ge {d_{\rm res}(X)\over K}
 \ge(1-40\delta-o(1))\binom mH.                       \tag{1.6}
\]

The random covering family was chosen so that every root has between
\(m^2/2\) and \(2m^2\) containers in \(\mathcal F\).  Also

\[
 |\mathcal F|\binom mH=(1+o(1))N_Hm^2.               \tag{1.7}
\]

The discarded centres contribute \(o(N_Hm^2)\) failed incidences, and
(1.6) contributes at most
\((40\delta+o(1))N_Hm^2\) further failed incidences.  A root having no
literal residual link to \(\mathcal F'\) consumes at least \(m^2/2\) of
them.  Therefore at most \((80\delta+o(1))N_H\) roots have no such link.
Deleting the \(o(N_H)\) roots used by \(\mathcal M\) changes only the
error term.  This proves (0.2).

## 2. One fresh unbiased bite

Mark every current edge independently with

\[
 p={\gamma\over rR},\qquad 0<\gamma<1/20,
\]

and accept only isolated marked edges.  For an owner \(X\), let

\[
 Z_X=\sum_{e\not\ni X}a_X(e)\xi_e.                  \tag{2.1}
\]

If \(X\) survives the bite, its actual degree loss is at most \(Z_X\),
because every accepted edge is marked.  The exact repaired-path estimates
give

\[
 \operatorname {Var}Z_X\le {C\gamma\over m^2}D^2,
 \qquad
 \Pr(|Z_X-\mathbb EZ_X|>\varepsilon D)
 \le2e^{-c m^2\varepsilon^2/(\gamma+\varepsilon)}.    \tag{2.2}
\]

Also

\[
 {\mathbb EZ_X\over D}
 \le p(R+rD)\le2\gamma.                              \tag{2.3}
\]

Choose the bite genuinely slowly, say \(\gamma\le\delta/100\).  An owner
with post-bite degree at most \((1-\delta/2)D\) must then satisfy

\[
 Z_X-\mathbb EZ_X\ge(\delta/3)D                    \tag{2.4}
\]

for all sufficiently large \(m\).  Thus the probability that any fixed
owner becomes counterexample-defective is

\[
 p_{\rm bad}\le\exp[-c_\delta m^2].                  \tag{2.5}
\]

The relevant union is not a union over all owners.  It is a containment
energy.  Let \(\mathcal B\) be the post-bite owners satisfying (2.4), and
put

\[
 \mathscr C(\mathcal B)
 =\sum_A\sum_{X\supset A}\mathbf1_{\{X\in\mathcal B\}}.
                                                               \tag{2.6}
\]

Every owner has \(\binom mH\) static root containers, so, by symmetry and
(2.5),

\[
 \mathbb E\mathscr C(\mathcal B)
 \le W\binom mH e^{-c_\delta m^2}
 =N_HQe^{-c_\delta m^2}.                              \tag{2.7}
\]

If the actual surviving root links of \(\mathcal B\) meet \(\eta N_H\)
roots, then its static containment energy is at least \(\eta N_H\).
Markov's inequality therefore yields

\[
 \Pr\bigl(\mathcal B\text{ has actual links to }\eta N_H
          \text{ roots}\bigr)
 \le {Q\over\eta}e^{-c_\delta m^2}=o(1).             \tag{2.8}
\]

This proves (0.3).  No independence between different owners is used.

## 3. The stopped multibite martingale

We now separate martingale noise from predictable drift.  This separation
is necessary: a martingale theorem cannot rule out an adverse compensator.

At the beginning of bite \(j\), let \(d_j(X)\) be the current link size
of a surviving owner.  Define

\[
 Z_{j,X}=\sum_{e\not\ni X}a_{j,X}(e)\xi_{j,e},
 \qquad z_{j,X}={Z_{j,X}\over d_j(X)}.               \tag{3.1}
\]

Stop at the first bite \(\tau\) at which either

\[
 \max_{e\not\ni X}a_{j,X}(e)>{C_z\over m^2}d_j(X)    \tag{3.2}
\]

for an owner under consideration, or the current degree ratios make
\(p_j(R_j+rD_j)>1/8\).  Before \(\tau\), conditional Bernstein gives

\[
 \mathbb E\!\left[
  e^{\theta(z_{j,X}-\mathbb E[z_{j,X}\mid\mathcal G_j])}
       \mid\mathcal G_j\right]
 \le \exp\!\left({C_z\theta^2\over m^2}\right)       \tag{3.3}
\]

for \(0\le\theta\le c_zm^2\).  This is the conditional version of (2.2).
Indeed, the residual reverse count is
\(\sum_ea_{j,X}(e)\le d_j(X)(R_j+rD_j)\), while every summand is at
most \(C_zd_j(X)/m^2\).

Put

\[
 g(u)=-\log(1-\min\{u,1/2\}),
\]

and stop additionally if \(z_{j,X}>1/2\).  The truncated function \(g\)
is \(2\)-Lipschitz on \([0,\infty)\).  Conditional bounded-difference
Bernstein applied to the independent marking variables therefore shows
that the centred variables

\[
 U_{j,X}=g(z_{j,X})-
          \mathbb E[g(z_{j,X})\mid\mathcal G_j]       \tag{3.4}
\]

obey the same sub-Gaussian estimate as (3.3), with changed constants.
For \(t\le T\wedge\tau\), define

\[
 M_t(X)=\sum_{j<t}U_{j,X},\qquad
 P_t(X)=\sum_{j<t}\mathbb E[g(z_{j,X})\mid\mathcal G_j],
 \qquad \widehat d_t(X)=D e^{-P_t(X)}.              \tag{3.5}
\]

Iteration of the conditional moment bound gives the exponential
supermartingale

\[
 \mathbb E e^{\theta M_t(X)}
 \le\exp\!\left({C_zT\theta^2\over m^2}\right).
                                                               \tag{3.6}
\]

For \(T\le C_zm\), Chernoff optimization and Ville's maximal inequality
yield

\[
 \Pr\left(\max_{t\le T\wedge\tau}M_t(X)>\varepsilon\right)
 \le2\exp[-c_z\varepsilon^2m].                    \tag{3.7}
\]

The additional stopping event \(z_{j,X}>1/2\) has probability
\(T\exp[-\Omega(m^2)]\) for a fixed owner and is absorbed in (3.7).

If \(X\) survives, every lost option meets an accepted marked edge, so

\[
 d_{j+1}(X)\ge d_j(X)-Z_{j,X}=d_j(X)(1-z_{j,X}).      \tag{3.8}
\]

Consequently

\[
 d_t(X)\ge D\exp\!\left[-\sum_{j<t}g(z_{j,X})\right]. \tag{3.9}
\]

Combining (3.5) and (3.9),

\[
 d_t(X)\le e^{-\varepsilon}\widehat d_t(X)
 \quad\Longrightarrow\quad M_t(X)\ge\varepsilon.    \tag{3.10}
\]

Thus (3.7) is an actual downward-degree tail, relative to the exact
predictable marked-conflict trajectory \(\widehat d_t(X)\).

## 4. Containment energy through the Gaussian-height run

Let

\[
 \mathcal B_t(\varepsilon)
 =\{X:X\text{ survives and }
       d_t(X)\le e^{-\varepsilon}\widehat d_t(X)\}.    \tag{4.1}
\]

Define its static containment energy

\[
 \mathscr C_t
 =\sum_A\sum_{X\supset A}\mathbf1_{\{X\in\mathcal B_t(\varepsilon)\}}.
                                                               \tag{4.2}
\]

By (3.7) and double counting,

\[
 \mathbb E\mathscr C_t
 \le N_HQ\,2e^{-c_z\varepsilon^2m}.                \tag{4.3}
\]

If actual surviving links from \(\mathcal B_t(\varepsilon)\) meet
\(\eta N_H\) roots, then \(\mathscr C_t\ge\eta N_H\).  Markov's
inequality and a union bound over \(T\le C_zm\) bite times give

\[
 \Pr\left(\exists t\le T\wedge\tau:
  \begin{array}{c}
  \mathcal B_t(\varepsilon)\text{ has actual links}\\
  \text{to at least }\eta N_H\text{ roots}
  \end{array}\right)
 \le {2TQ\over\eta}e^{-c_z\varepsilon^2m}.            \tag{4.4}
\]

Finally,

\[
 \log Q
 =\Theta(H\log(m/H))=o(m),                            \tag{4.5}
\]

because \(H=(1+o(1))\sqrt{m\log m}\).  Therefore the right side of
(4.4) tends to zero.  This proves (0.4).

## 5. What is proved and what remains

The repaired support-reachable construction is literal: its exceptional
owners have actual surviving links to a positive fraction of roots.

For the unbiased slow bite, however, the same configuration cannot be
created by martingale fluctuation with nonnegligible probability.  The
containment factor \(Q\) costs only \(e^{o(m)}\), while the multibite
degree-noise tail is \(e^{-\Omega(m)}\).

There remains one exact alternative.  Let \(D_t^{\rm com}\) be the common
owner degree scale.  If a root-covering family satisfies

\[
 \widehat d_t(X)\le e^{-\varepsilon}D_t^{\rm com}      \tag{5.1}
\]

for its owners, then the marked-conflict lower trajectory is already below
the actual common scale; (4.4) does not calibrate the isolation slack
between these two quantities.  This includes both owner-specific
path-link clustering and a nonuniform marked-to-accepted conversion.
Equivalently, the next theorem needed for full typical RPRN is

\[
 \boxed{
 \text{no positive-containment-energy family has adverse predictable
 accepted-loss drift before the path-influence stopping time.}} \tag{5.2}
\]

More formally, let \(\mathsf A_T(\eta,\varepsilon)\) be the event that
before time \(T\) there is a surviving owner family whose actual links
meet at least \(\eta N_H\) roots and for which

\[
 d_t(X)\le e^{-\varepsilon}D_t^{\rm com}.
\]

Let \(\mathsf D_T(\eta/2,\varepsilon/2)\) be the analogous event with

\[
 \widehat d_t(X)\le e^{-\varepsilon/2}D_t^{\rm com}.
\]

Partition every owner witnessing \(\mathsf A_T\) according as
\(d_t(X)\le e^{-\varepsilon/2}\widehat d_t(X)\) or not.  The actual root
neighbourhoods of the two classes have union of size at least
\(\eta N_H\), so one class meets at least \(\eta N_H/2\) roots.  The
first class is controlled by (4.4), while the second satisfies the
display defining \(\mathsf D_T\).  Hence

\[
 \boxed{
 \Pr(\mathsf A_T(\eta,\varepsilon))
 \le \Pr(\tau\le T)
    +\Pr(\mathsf D_T(\eta/2,\varepsilon/2))
    +{4TQ\over\eta}e^{-c_z\varepsilon^2m}.}            \tag{5.3}
\]

This is the exact trajectory reduction.  The last term is \(o(1)\).

If (5.2) fails with nonnegligible probability, it supplies the requested
typical trajectory obstruction.  If it holds and the stopping time in
(3.2) is itself negligible, then the containment-energy martingale closes
this sparse-family lane.  Neither conclusion follows from static
codegrees alone.
