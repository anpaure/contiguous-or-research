# Gate A: unconditioned random clock and the mixture-of-slices reference

**Date:** 2026-08-22  
**Status:** exact structural bypass of per-round exact-size conditioning;
the unconditioned scalar drift/erosion comparison remains open

The residual target sizes in the isolated-edge process are random.  The
current Gate-A presentation conditions every transition on its exact shore
decrement and compares it with one deterministic nested uniform-slice
kernel.  That conditioning creates the residual-environment likelihood in
(G.76)--(G.77).

It is not necessary.  Keep the actual bite unconditioned and use, as the
reference at time \(j\), the mixture of uniform slices having the **same
random size law** as the actual residual.  The actual joint law of two
successive size vectors canonically induces a nested reference kernel
between these mixtures.  Uniform reference bounds on every slice in a
narrow density bin pass to the mixture with no loss.

This is a rigorous bypass of the G.76 environment factor, not a proof of
Gate A.  The remaining comparison is now an unconditioned one: control the
relative scalar drift, including erosion and the random realized center,
under the actual stopped law.  The finite-bite survival-selection remainder
for that law is proved in
`MATH_THEOREM_GATE_A_FINITE_BITE_CARRIER_SURVIVAL_REMAINDER_20260822.md`.

## 1. Uniform-slice mixtures

Let

\[
 V=\mathop{\dot\bigcup}_{\sigma=1}^qV_\sigma,
 \qquad |V_\sigma|=N_\sigma,
\]

and, for a feasible size vector \(\mathbf n=(n_1,\ldots,n_q)\), put

\[
 \Omega_{\mathbf n}
 =\{S\subseteq V:|S\cap V_\sigma|=n_\sigma\ \forall\sigma\},
 \qquad
 \lambda_{\mathbf n}(S)=|\Omega_{\mathbf n}|^{-1}.          \tag{1.1}
\]

Consider any deletion-only random process

\[
                         S_{j+1}\subseteq S_j               \tag{1.2}
\]

and let \(\nu_j\) be the law of \(S_j\).  Write

\[
 \mathbf N_j=(|S_j\cap V_1|,\ldots,|S_j\cap V_q|),
 \qquad
 w_j(\mathbf n)=\Pr(\mathbf N_j=\mathbf n).                  \tag{1.3}
\]

Define the symmetrized reference law

\[
 \boxed{
 \Lambda_j=\sum_{\mathbf n}w_j(\mathbf n)\lambda_{\mathbf n}.} \tag{1.4}
\]

This definition uses only the size marginal of the actual unconditioned
law.  It does not assert that \(\nu_j\) is uniform conditional on size.

## 2. The canonical nested mixture kernel

Let

\[
 \kappa_j(\mathbf n,\mathbf n')
 =\Pr(\mathbf N_j=\mathbf n,\mathbf N_{j+1}=\mathbf n')      \tag{2.1}
\]

be the actual joint size law.  By (1.2), it is supported on
\(\mathbf n'\le\mathbf n\) coordinatewise.  When
\(w_j(\mathbf n)>0\), put

\[
 K_j(\mathbf n,\mathbf n')
 ={\kappa_j(\mathbf n,\mathbf n')\over w_j(\mathbf n)}.      \tag{2.2}
\]

For \(S\in\Omega_{\mathbf n}\), define

\[
 U_j(S,S')=
 \sum_{\mathbf n'\le\mathbf n}K_j(\mathbf n,\mathbf n')
 {\mathbf1_{\{S'\subseteq S,\ S'\in\Omega_{\mathbf n'}\}}
  \over
  \prod_\sigma {n_\sigma\choose n'_\sigma}}.               \tag{2.3}
\]

Rows with \(w_j(\mathbf n)=0\) may be defined arbitrarily.

### Theorem 2.1 (random-size nested reference)

The kernel (2.3) is Markov on the support of \(\Lambda_j\), is deletion
only, and satisfies

\[
                         \boxed{\Lambda_jU_j=\Lambda_{j+1}.} \tag{2.4}
\]

#### Proof

Only (2.4) needs proof.  Fix \(S'\in\Omega_{\mathbf n'}\).  For every
\(\mathbf n\ge\mathbf n'\), the number of supersets
\(S\in\Omega_{\mathbf n}\) of \(S'\) is

\[
                         \prod_\sigma
 {N_\sigma-n'_\sigma\choose n_\sigma-n'_\sigma}.            \tag{2.5}
\]

The elementary identity

\[
 {N_\sigma\choose n_\sigma}{n_\sigma\choose n'_\sigma}
 ={N_\sigma\choose n'_\sigma}
  {N_\sigma-n'_\sigma\choose n_\sigma-n'_\sigma}           \tag{2.6}
\]

therefore gives

\[
\begin{aligned}
 (\Lambda_jU_j)(S')
 &= {1\over|\Omega_{\mathbf n'}|}
    \sum_{\mathbf n\ge\mathbf n'}
      w_j(\mathbf n)K_j(\mathbf n,\mathbf n')\\
 &= {w_{j+1}(\mathbf n')\over|\Omega_{\mathbf n'}|}
  =\Lambda_{j+1}(S').                                      \tag{2.7}
\end{aligned}
\]

The second equality is the second marginal identity for \(\kappa_j\).
This proves (2.4).  \(\square\)

The construction is canonical at the level needed here: it uses the actual
joint size coupling, but replaces the conditional residual state by a
uniform nested subset.  No exact value of the accepted count is revealed to
or conditioned into the actual transition.

## 3. Uniform slice estimates pass to the mixture

Let \(F,t\ge0\) be any two state functionals and put

\[
 f_{\mathbf n}=\mathbb E_{\lambda_{\mathbf n}}F,qquad
 t_{\mathbf n}=\mathbb E_{\lambda_{\mathbf n}}t.             \tag{3.1}
\]

### Lemma 3.1 (ratio convexity)

Assume that
\(f_{\mathbf n}=0\) whenever
\(w_j(\mathbf n)>0\) and \(t_{\mathbf n}=0\).  If
\(\sum_{\mathbf n}w_j(\mathbf n)t_{\mathbf n}>0\), then

\[
 {\mathbb E_{\Lambda_j}F\over\mathbb E_{\Lambda_j}t}
 ={\sum_{\mathbf n}w_j(\mathbf n)t_{\mathbf n}
               (f_{\mathbf n}/t_{\mathbf n})
   \over\sum_{\mathbf n}w_j(\mathbf n)t_{\mathbf n}},       \tag{3.2}
\]

where zero-\(t_{\mathbf n}\) fibres are omitted.  In
particular,

\[
 \boxed{
 {\mathbb E_{\Lambda_j}F\over\mathbb E_{\Lambda_j}t}
 \le\sup_{\mathbf n:w_j(\mathbf n)t_{\mathbf n}>0}
       {f_{\mathbf n}\over t_{\mathbf n}}.}                 \tag{3.3}
\]

#### Proof

Expand (1.4) in the numerator and denominator and regroup the numerator as
\(w_jt_{\mathbf n}(f_{\mathbf n}/t_{\mathbf n})\).  This is (3.2), and
(3.3) follows because (3.2) is a convex combination.  \(\square\)

Without the displayed zero-tail hypothesis, a positive-\(f\), zero-\(t\)
fibre makes the natural supremum in (3.3) infinite; no finite ratio claim is
intended.  In the Gate-A application the hypothesis is automatic for
\(F=F_c\), \(t=T_{12}\), and \(c\ge11\): if \(T_{12}=0\), every root has
degree below twelve and hence \(F_c=0\).

For Gate A, take \(F=F_c\) and \(t=T_{12}\).  Appendix C.3ter/C.12 of
the master handoff proves the needed product-to-uniform-slice moment bounds
uniformly over every exact two-shore slice in a fixed-ratio density bin.
Lemma 3.1 therefore transfers those bounds immediately to \(\Lambda_j\).
There is no penalty involving the number of possible size vectors and no
minimum probability of an individual size fibre.

The same argument works after restricting the size law to a bin.  If
\(B\) is a set of size vectors with positive mass, replace \(w_j\) by its
conditional restriction to \(B\).  Equation (3.3) remains unchanged.  Thus
a narrow random density clock is sufficient whenever the reference bound
is uniform throughout the bin.

## 4. Palm recursion for the mixture

Let a labelled carrier \(\gamma\) have
\(b_{\gamma\sigma}\) distinct targets on shore \(\sigma\).  Conditional
on the current size \(\mathbf n\), its survival factor under (2.3) is

\[
 a_j^0(\mathbf n,\gamma)
 =\sum_{\mathbf n'}K_j(\mathbf n,\mathbf n')
   \prod_\sigma{(n'_\sigma)_{b_{\gamma\sigma}}
                       \over(n_\sigma)_{b_{\gamma\sigma}}}. \tag{4.1}
\]

This depends on the carrier only through its finite shore footprint and on
the process only through the random size decrement.  The exact Palm
recursion (G.89)--(G.94) applies to \((\Lambda_j,U_j)\) without change,
because Theorem 2.1 supplies the sole required identity
\(\Lambda_jU_j=\Lambda_{j+1}\).

There is also a uniform finite-bite expansion.  Put

\[
 \delta_\sigma(\mathbf n,\mathbf n')
 =1-{n'_\sigma\over n_\sigma},
 \qquad
 g_{\mathbf n,\mathbf n'}(\gamma)
 =\sum_\sigma\delta_\sigma b_{\gamma\sigma}.                \tag{4.2}
\]

Let \(\mathcal G(\mathbf n,\mathbf n')\) be a set of good decrements on
which

\[
 \delta_\sigma\le1/4,qquad
 b_{\gamma\sigma}\le n_\sigma/2,qquad
 g_{\mathbf n,\mathbf n'}(\gamma)\le\eta,                  \tag{4.3}
\]

and put

\[
 \beta(\mathbf n)=
 \Pr_{K_j}(\mathcal G^c\mid\mathbf N_j=\mathbf n).           \tag{4.3a}
\]

Then Lemma 2.2 of the finite-bite note, averaged over the good part of
\(K_j\), gives

\[
 a_j^0=1-
 \mathbb E_{K_j}[\mathbf1_{\mathcal G}
                 g_{\mathbf n,\mathbf N'}(\gamma)]
 +O\!\left(\eta^2+
   \mathbb E_{K_j}\left[\mathbf1_{\mathcal G}
      \sum_\sigma
    {\delta_\sigma b_{\gamma\sigma}^2\over n_\sigma}
      \right]+\beta(\mathbf n)\right).                       \tag{4.4}
\]

Indeed, on a bad transition both its exact survival factor and the baseline
one lie in \([0,1]\), so deleting the bad part changes the average by at
most \(\beta(\mathbf n)\).  This explicit split is necessary; Lemma 2.2
itself says nothing pointwise on \(\mathcal G^c\).

At the punctured scale \(b_{\gamma\sigma}=O_m(r)\),
\(n_\sigma=e^{\Omega(r)}\), and a Taylor-safe bite has
\(\delta_\sigma=O(\epsilon/r)\) on the accepted-count good event.
The stopped accepted-count estimate gives
\(\sup_{\mathbf n}\beta(\mathbf n)=e^{-\Omega(r)}\) on the active
size support (or the same bound after averaging over that support).
Hence (4.4) has an \(O_m(\epsilon^2)+e^{-\Omega(r)}\) remainder.  The
reference side therefore retains the same summable finite-bite accuracy as
a deterministic exact-slice schedule.

## 5. Random density clock

In the punctured process, every accepted configuration deletes exactly
\(2r\) targets from each shore.  If \(Q_j\) is the number accepted in
round \(j\), then pathwise

\[
 n_{j+1,\sigma}=n_{j,\sigma}-2rQ_j.                         \tag{5.1}
\]

Thus the two shore sizes lie on a one-dimensional random clock, and their
absolute difference is invariant before unequal purges.  The stopped
accepted-count estimate already proved in Appendix C.5 gives, on its good
event, two-sided constant-factor control of \(Q_j\) by its predictable
mean.  Consequently the usual geometric density-bin argument can be run at
the random entrance times of the bins.  No statement conditional on a
particular value of \(Q_j\) is required.

For clarity, the deterministic summation fact used here has the following
pathwise random-clock form.  Suppose \(x_j\) is nonincreasing and, before a
bounded stop,

\[
 \log{x_j\over x_{j+1}}\ge c{\epsilon_j\over r}.             \tag{5.2}
\]

For every nondecreasing \(G(1/x)\), comparison with the logarithmic
integral, or simply grouping the terms between successive powers of two,
gives

\[
 \boxed{
 \sum_{j<J}{\epsilon_j\over r}G(1/x_j)
 \le {1\over c}\int_{x_J}^{x_0}G(1/x){dx\over x}.}          \tag{5.3}
\]

Indeed, (5.2) bounds \(\epsilon_j/r\) by
\(c^{-1}\log(x_j/x_{j+1})\), and throughout
\([x_{j+1},x_j]\) monotonicity gives
\(G(1/x)\ge G(1/x_j)\).  Sum the resulting disjoint integrals.
If a bin argument stops immediately before one overshooting step, that
single omitted step is charged separately by its displayed summand.

For \(G(1/x)=r^{-a}x^{-b}\), this is
\(O(r^{-a}x_J^{-b})\), exactly the deterministic estimate (G.15).  The
proof is pathwise, so expectation and stopping may be applied afterward.

## 6. What this bypasses, and what remains indispensable

The mixture construction shows that a deterministic exact-size schedule is
**not** indispensable for any of the following:

1. a nested uniform reference Markov chain;
2. uniform-slice tail or collision estimates within a density bin;
3. the exact scalar Palm recursion;
4. Taylor control of the reference carrier-survival factor; or
5. logarithmic density-clock summation.

It is indispensable only to the **particular fibrewise likelihood
presentation** in (G.64)--(G.77): once the actual transition is conditioned
on \(\mathbf N_{j+1}=\mathbf n'\), its conditional residual environment
appears and must be compared on that fibre.  Under the present construction
the actual transition is never so conditioned, so that factor is absent;
the actual carrier survival is the local unconditioned quantity handled by
the finite-bite theorem.

Three genuine tasks remain.

* The actual and reference scalar drifts must still be compared.  The
  degree-conditioned carrier-hazard inversion controls the actual
  survival-selection term, but it does not yet compare the favourable
  erosion with the product/mixture reference erosion.
* The predictable reference center in a bin must be transferred to the
  realized random center.  Narrow bins give only a fixed-ratio comparison;
  the \(o(x_*/r)\) accumulated center error required by the shadow-purge
  ledger still needs its stated quantitative proof.
* A killed stopped law should be handled by adjoining a cemetery state, or
  equivalently by freezing at the stop and inserting live indicators in the
  drift.  Conditioning on the future event that the stop never occurs is
  still invalid.

Accordingly the exact revised Gate-A route is

\[
\boxed{
 \begin{array}{c}
 \text{unconditioned isolated-edge process}\ +
 \text{random-size uniform-slice mixture}\ +
 \text{uniform bin estimates}\ +
 \text{unconditioned scalar drift/center control}.
 \end{array}}                                                \tag{6.1}
\]

This route removes G.76 as an obligation.  It does not remove the
punctured-specific carrier-hazard regression (or an equivalent signed
drift theorem), the reference-relative erosion comparison, or the stopped
realized-center ledger.
