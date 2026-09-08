# Promotion rings: all sublinear Johnson-character sectors have no macroscopic linear gap

Date: 2026-07-26

Method: pure mathematics.  This extends the degree-two audit without
requiring exact higher-order cyclic-distance formulas.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad R=\binom nM,
\]

with \(H=o(m)\), and choose one oriented cyclic frame on every \(M\)-top.
For a rank \(k=m+o(m)\), let \(a_k\) be the resulting cyclic-window load
and put

\[
 f_k=a_k-{MR\over\binom nk}{\bf1}.
\tag{0.1}
\]

Write \(P_j^{(k)}\) for projection onto Johnson degree \(j\) on the
rank-\(k\) layer.

> **All-low-degree energy theorem.**  If frames are chosen independently
> and uniformly on their tops, then for every \(2\le t\le
> \min(k,n-k)\),
> \[
> \boxed{
> \mathbb E\|P_t^{(k)}f_k\|_2^2
> \le
> {R\binom Mt M^2\over\binom{n-2t}{k-t}}.}
> \tag{0.2}
> \]

Consequently, for the tuned promotion parameters

\[
 H=O(\sqrt{m\log m}),\qquad k\in\{m,m-q_0\},qquad q_0=o(m),
\]

and every \(d=d(m)\) satisfying

\[
 d=o(m),
 \tag{0.3}
\]

there is one **integral** one-frame-per-top selection, common to the two
ranks, for which

\[
 \boxed{
 \sum_{k\in\{m,m-q_0\}}\sum_{t=2}^{d}
 \|P_t^{(k)}f_k\|_2^2=\exp(o(m)).}
 \tag{0.4}
\]

In particular, let \(\alpha_m,\beta_m\) be arbitrary functions supported
on Johnson degrees \(2,\ldots,d\) at the two ranks, with

\[
 \|\alpha_m\|_\infty+\|\beta_m\|_\infty=\exp(o(m)).
 \tag{0.5}
\]

For the integral selection in (0.4),

\[
 \boxed{
 |\langle\alpha_m,f_m\rangle+
   \langle\beta_m,f_{m-q_0}\rangle|=o(W),
 \qquad W=\binom{2m}m.}
 \tag{0.6}
\]

Therefore no bounded, polynomial-coefficient, or more generally
subexponential-coefficient linear Johnson-character inequality of
sublinear degree separates the uniform fractional point from every
integral frame selection by \(\Omega(W)\).

A surviving statewise obstruction must be at least one of:

1. degree \(\Omega(m)\);
2. equipped with exponentially large normalized coefficients; or
3. nonlinear in the support variables, such as the literal collision and
   hole indicators.

This does not prove low collision/hole defect: low-degree load discrepancy
is much weaker than support-sensitive coverage at mean one.

### Corollary 0.1 (one selection for the whole promotion band)

Let \(\mathcal K_m\) be any family of \(\exp(o(m))\) ranks satisfying

\[
                         |k-m|=o(m)\qquad(k\in\mathcal K_m).
\tag{0.7}
\]

Then one integral frame selection satisfies

\[
 \sum_{k\in\mathcal K_m}\sum_{t=2}^{d}
 \|P_t^{(k)}f_k\|_2^2=\exp(o(m))
 \qquad(d=o(m)).
\tag{0.8}
\]

The analogous \(o(W)\) conclusion holds for a sum of load-linear
functionals over all these ranks when their combined coefficient scale is
\(\exp(o(m))\).  In particular, (0.8) applies simultaneously to every
rank in the full promotion band

\[
                         m-H\le k\le m+H
\]

when \(H=O(\sqrt{m\log m})\).  Thus coupling many depths does not revive
any sublinear-degree, subexponential-coefficient **linear load**
obstruction.

## 1. Higher inclusion compression

For \(1\le t\le k\), define

\[
 (\mathcal I_{k,t}f)(e)=\sum_{Q\supset e}f(Q),
 \qquad e\in\binom{[n]}t.
\tag{1.1}
\]

The standard inclusion-matrix decomposition gives

\[
 \|\mathcal I_{k,t}f\|_2^2
 =\sum_{j=0}^{t}
 \binom{n-t-j}{k-t}\binom{k-j}{t-j}
 \|P_j^{(k)}f\|_2^2.
\tag{1.2}
\]

Only nonnegativity and the top coefficient will be needed.  Namely,

\[
 \boxed{
 \|P_t^{(k)}f\|_2^2
 \le{\|\mathcal I_{k,t}f\|_2^2\over
          \binom{n-2t}{k-t}}.}
\tag{1.3}
\]

For completeness, (1.2) follows by applying
\(\mathcal I_{k,t}\mathcal I_{k,t}^*\) to the multiplicity-free Johnson
decomposition of the \(t\)-set permutation module.  Its kernel depends
only on intersection size, and its eigenvalue on degree \(j\) is

\[
 \binom{n-t-j}{k-t}\binom{k-j}{t-j}.
\]

At \(j=t\) this is exactly \(\binom{n-2t}{k-t}\), proving (1.3).

## 2. Compression of an actual random cyclic-frame selection

Fix a \(t\)-subset \(e\).  Only tops \(U\supset e\) contribute to
\((\mathcal I_{k,t}a_k)(e)\).  For such a top and frame \(\pi_U\), let

\[
 D_{k,t}^{\pi_U}(e)
 =\#\{Q\in I_k(\pi_U):e\subseteq Q\}.
\tag{2.1}
\]

The exact mean is not needed.  We use only

\[
 0\le D_{k,t}^{\pi_U}(e)\le M,
 \qquad
 \operatorname {Var}(D_{k,t}^{\pi_U}(e))\le M^2.
\tag{2.2}
\]

The constant subtracted in (0.1) is exactly the sum of the one-top means,
by double counting flags \((e,Q,U)\).  Therefore

\[
 (\mathcal I_{k,t}f_k)(e)
 =\sum_{U\supset e}
   \left(D_{k,t}^{\pi_U}(e)-
         \mathbb ED_{k,t}^{\pi_U}(e)\right).
\tag{2.3}
\]

The summands are independent over tops.  There are
\(\binom{n-t}{M-t}\) such tops, hence

\[
 \mathbb E(\mathcal I_{k,t}f_k)(e)^2
 \le\binom{n-t}{M-t}M^2.
\tag{2.4}
\]

Sum over \(e\in\binom{[n]}t\) and use the flag identity

\[
 \binom nt\binom{n-t}{M-t}=R\binom Mt.
\tag{2.5}
\]

This gives

\[
 \mathbb E\|\mathcal I_{k,t}f_k\|_2^2
 \le R\binom MtM^2.
\tag{2.6}
\]

Combining (2.6) with (1.3) proves (0.2).

## 3. Uniform subexponential bound

Assume now the tuned parameters and \(t\le d=o(m)\).  Uniformly for
\(k=m+o(m)\), elementary binomial-ratio estimates give

\[
 {W\over\binom{n-2t}{k-t}}
 =\exp\!\left(O\!\left(t+{t^2\over m}+{q_0^2\over m}
                     +{tq_0\over m}\right)\right).
\tag{3.1}
\]

Also \(R\le W\), \(M^2\le m^{O(1)}\), and

\[
 \binom Mt\le\left({eM\over t}\right)^t.
\tag{3.2}
\]

Equations (0.2), (3.1), and (3.2) imply

\[
 \mathbb E\|P_t^{(k)}f_k\|_2^2
 \le\exp\!\left(O\!\left(
      t\log{eM\over t}+q_0^2/m+t^2/m\right)\right).
\tag{3.3}
\]

Under (0.3),

\[
 t\log{eM\over t}=o(m)
\]

uniformly for \(t\le d\), because
\((t/m)\log(em/t)\to0\).  For the standing \(q_0=m^{1/4}\) (or any
\(q_0=o(m)\)), the right
side is \(\exp(o(m))\), uniformly for \(t\le d\).  Summing (3.3) over
the two ranks and \(t\le d\), then choosing a realization no larger than
the expectation, proves (0.4).

Finally

\[
 \|\alpha_m\|_2+\|\beta_m\|_2
 \le\sqrt{2W}\,\exp(o(m)),
\]

while (0.4) gives a combined projected-load norm \(\exp(o(m))\).
Cauchy--Schwarz yields

\[
 |\langle\alpha_m,f_m\rangle+
   \langle\beta_m,f_{m-q_0}\rangle|
 \le\sqrt W\,\exp(o(m))=o(W),
\]

because \(W=\exp((2\log2+o(1))m)\).  This proves (0.6).

All estimates above are uniform for \(|k-m|=o(m)\).  Summing their
expectations over \(\exp(o(m))\) such ranks still gives \(\exp(o(m))\).
Choosing one realization below this aggregate expectation proves
Corollary 0.1; the same combined Cauchy--Schwarz estimate proves its
functional statement.

## 4. Exact implication boundary

Proved here:

1. the explicit higher-degree energy bound (0.2) for actual cyclic-frame
   columns;
2. simultaneous subexponential energy through every sublinear degree
   \(d=o(m)\); and
3. the resulting no-go for all normalized subexponential-coefficient
   linear separators in those sectors.

Not proved here:

1. small collision or hole objective for the supplied integral selection;
2. absence of a high-degree or exponentially weighted linear separator;
3. absence of a nonlinear support-sensitive integral-hull inequality; or
4. the globally correlated promotion-frame theorem.
