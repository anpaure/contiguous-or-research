# Edge-transitive capacity, co-criticality, and the growing-template leftover

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

For one edge-transitive multipartite orbit, the fractional matching
capacity is exactly

\[
 \nu^*(\mathcal H)=\frac{|E|}{\Delta}
 =\min_{\mathcal O}\frac{|\mathcal O|}{a_{\mathcal O}}.
\]

For a cyclic-interval template with \(a_m=n\) and
\(\theta_j=a_{m\pm j}/n\), the middle row is a capacity bottleneck exactly
when

\[
 \theta_j\le \frac{N_j}{W}.
\]

A family of \(W/n\) template copies which covers the whole signed
depth-\(j\) row necessarily satisfies the reverse inequality.  Thus an
exact capacity-sized simultaneous cover forces rowwise co-criticality.
For one fixed integral template this equality is usually obstructed by
rounding; the coefficient-one construction must use template mixtures or
retain the forced floor-defect repair ledger.

The quoted growing-template leftover

\[
 \varepsilon_{\rm BB}
 \asymp
 \exp\!\left[-\frac{\log(D/\log N)}{2(k_T-1)}\right]
 \asymp m^{-1/[2(1+\tau)]}
\]

is not small when \(\tau\sim\sqrt{\pi m}\).  It equals

\[
 1-\Theta\!\left(\frac{\log m}{\sqrt m}\right),
\]

so even an optimistic black-box application covers only a vanishing
fraction.  In addition, the actual interval orbit does not automatically
satisfy the required growing-uniformity/codegree hypotheses.

## 1. Exact orbit capacity

Let a finite group act transitively on the indexed edge set \(E\) of a
hypergraph.  Let \(\mathcal O\) run through the vertex orbits, and suppose
every edge contains exactly \(a_{\mathcal O}\) vertices in \(\mathcal O\).
Double counting incidences gives the common degree

\[
 \Delta_{\mathcal O}=\frac{|E|a_{\mathcal O}}{|\mathcal O|}.
\]

Put \(\Delta=\max_{\mathcal O}\Delta_{\mathcal O}\).  The constant edge
weight \(1/\Delta\) is a fractional matching, of value \(|E|/\Delta\).
If \(\mathcal O_*\) attains the maximum degree, every fractional matching
\(x\) satisfies

\[
 a_{\mathcal O_*}\sum_e x_e
 =\sum_{v\in\mathcal O_*}\sum_{e\ni v}x_e
 \le |\mathcal O_*|.
\]

Therefore

\[
 \boxed{
 \nu^*(\mathcal H)=\frac{|E|}{\Delta}
 =\min_{\mathcal O}\frac{|\mathcal O|}{a_{\mathcal O}}.}
 \tag{1.1}
\]

This statement is unaffected by a constant labelled multiplicity of every
simple edge.  It is a one-orbit statement: unrelated copy labels or
template types must be joined by a genuine transitive group action before
they can be treated as one indexed orbit.

## 2. Capacity and coverage force opposite inequalities

Let \(n=2m+1\), \(W=\binom nm\), and let

\[
 N_j=\binom n{m-j}
\]

with the complementary upper row having the same size.  Suppose a template
contains

\[
 a_m=n,
 \qquad a_{m\pm j}=n\theta_j.
\]

The middle capacity is \(W/n\).  The signed depth-\(j\) capacity is

\[
 \frac{N_j}{n\theta_j}.
\]

Hence the middle row is a bottleneck precisely when

\[
 \boxed{\theta_j\le N_j/W.} \tag{2.1}
\]

Now select exactly \(C_m=W/n\) copies.  They supply \(W\theta_j\)
depth-\(j\) occurrences.  Covering all \(N_j\) targets requires

\[
 \boxed{\theta_j\ge N_j/W.} \tag{2.2}
\]

Combining (2.1) and (2.2) forces equality.  If the selected copies are a
matching in the augmented hypergraph, equality also says that every
depth-\(j\) target is used exactly once.

The integrality qualification is essential.  Equality asks for

\[
 a_{m\pm j}=\frac{nN_j}{W},
\]

which need not be an integer.  With the calibrated floor

\[
 a_{m\pm j}=\left\lfloor\frac{nN_j}{W}\right\rfloor,
\]

the unavoidable uncovered count is

\[
 \delta_j=N_j-\frac Wn a_{m\pm j}.
\]

Thus exact co-criticality is not a property of one generic integral
template.  The actual augmented construction correctly keeps the sum of
these floor defects as a separate repair ledger.

## 3. The Gaussian total template load

If the central row is counted once and both signed rows are counted for
\(j\ge1\), the co-critical total is

\[
 \tau_Q
 =1+2\sum_{j=1}^Q\frac{N_j}{W}.
\]

Uniformly for \(j=o(m^{2/3})\),

\[
 \frac{N_j}{W}
 =\exp\!\left[-\frac{j(j+1)}m+O\!\left(\frac{j^3}{m^2}\right)\right].
\]

Consequently, if \(Q/\sqrt m\to\infty\) and \(Q=o(m^{2/3})\),

\[
 \boxed{\tau_Q=(1+o(1))\sqrt{\pi m}.} \tag{3.1}
\]

For \(Q=A\sqrt m\), the constant in (3.1) is instead the truncated
Gaussian integral

\[
 \sqrt m\int_{-A}^{A}e^{-u^2}\,du+o(\sqrt m).
\]

## 4. The black-box leftover tends to one

For the full coordinate orbit, the natural degree scale has

\[
 \log(D/\log N)=\Theta(m\log m).
\]

At co-critical row counts the augmented template size has

\[
 k_T-1=n(1+\tau_Q)+O(1)=\Theta(m^{3/2}),
\]

where the harmless \(1\) depends on whether the central row is included in
the definition of \(\tau_Q\).  Therefore the displayed leftover becomes

\[
 \begin{aligned}
 \varepsilon_{\rm BB}
 &\asymp
 \exp\!\left[-\frac{\log m}{2(1+\tau_Q)}\right]\\
 &=1-\frac{\log m}{2\sqrt{\pi m}}
   +O\!\left(\frac{(\log m)^2}{m}
              +\frac{\log m}{m}\right).
 \end{aligned}
 \tag{4.1}
\]

Thus \(\varepsilon_{\rm BB}\to1\), not zero.  If it denotes the unmatched
fraction, the theorem supplies only a
\(\Theta((\log m)/\sqrt m)\)-fraction matching.

Finally, (4.1) is only a numerical substitution into the quoted theorem.
Its hypotheses still have to be checked.  In the actual interval orbit,
nested adjacent targets have relative codegree \(\Theta(1/m)\), while
\(k_T=\Theta(m^{3/2})\), and logarithmic crossing squares keep the relevant
full-codegree root bounded.  Hence no generic growing-uniformity matching
theorem may be invoked from edge transitivity and capacity alone.

## 5. Implication for the augmented template

The edge-transitive symmetrization theorem remains useful: once one large
unweighted matching in a fixed orbit is known, all nonnegative weighted
residual cuts follow at the original orbit-degree scale.  What the present
capacity calculation adds is that

* the calibrated floors are mathematically forced, not cosmetic;
* exact all-row coverage by a single capacity-sized integral template is
  generally impossible without mixing or repair; and
* the quoted black-box leftover is asymptotically vacuous at the
  \(\sqrt m\)-row load.

The surviving theorem is still an orbit-specific augmented matching or
absorption result, not a consequence of fractional capacity.
