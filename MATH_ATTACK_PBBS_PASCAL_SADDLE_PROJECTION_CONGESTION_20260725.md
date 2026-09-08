# PBBS peak deletion: Pascal-saddle projection congestion

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, or web search
is used.

## 0. Verdict

Let \(r\) be the outer semilength. For a one-step peak-deletion core
\(E\in\mathcal D_d\) with \(k=\operatorname{pk}(E)\), the exact inverse
fibre is

\[
 P_r(d,k)=\binom{r+d-k}{2d}.                         \tag{0.1}
\]

The induced Pascal measure on cores has its saddle at

\[
 d=\frac r2,\qquad k=\frac r6,\qquad \frac kd=\frac13. \tag{0.2}
\]

This is an exact obstruction to rank-only scalar induction. The
peak-\(1/3\) core class is exponentially negligible under uniform Catalan
measure at rank \(d\), yet one saddle lattice cell has outer inverse-fibre
mass \(\Theta(\operatorname{Cat}_r/r)\), exactly the quotient scale in
Theorem 17.1.

This does not itself disprove \((\mathrm{RP}_A)\): the cores must also obey
the PBBS predecessor-passage condition. It proves that neither an unweighted
lower-rank packing estimate nor a rank-only scalar charge can control the
lift. A valid recursion must retain peak, prescribed-slot, and passage data.

## 1. Exact Pascal cell mass

The number of rank-\(d\) Dyck cores with \(k\) peaks is

\[
 \mathsf N(d,k)=\frac1d\binom dk\binom d{k-1}.       \tag{1.1}
\]

Stars-and-bars over the \(2d+1\) child slots gives (0.1). Hence the exact
outer mass above the cell \((d,k)\) is

\[
 \boxed{\mathsf M_r(d,k)=
 \frac1d\binom dk\binom d{k-1}\binom{r+d-k}{2d}.}    \tag{1.2}
\]

These cells partition the outer Dyck roots once the elementary \(d=0\)
fully-pruned boundary term is included:

\[
 \sum_{d,k}\mathsf M_r(d,k)=\operatorname{Cat}_r.   \tag{1.3}
\]

Every inverse root is a distinct outer quotient edge. Thus the point
congestion over one reduced quotient edge in cell \((d,k)\) is exactly
\(P_r(d,k)\).

## 2. One critical cell, with constants

Let \(r=6n,d=3n,k=n\), and put

\[
 \mathcal C_n=\{E\in\mathcal D_{3n}:
                   \operatorname{pk}(E)=n\}.
\]

Then

\[
 |\mathcal C_n|
 =\frac1{3n}\binom{3n}{n}\binom{3n}{n-1},
 \qquad
 P_{6n}(3n,n)=\binom{8n}{6n}.                       \tag{2.1}
\]

Stirling's formula gives

\[
 \frac{|\mathcal C_n|}{\operatorname{Cat}_{3n}}
 \sim
 \frac{3\sqrt3}{8\sqrt\pi}\,n^{-1/2}
 \left(\frac{27}{32}\right)^{2n},                  \tag{2.2}
\]

but

\[
 \boxed{
 \frac{|\mathcal C_n|P_{6n}(3n,n)}
      {\operatorname{Cat}_{6n}}
 \sim \frac{3\sqrt2}{4\pi n}
 =\frac{9\sqrt2}{2\pi r}.}                          \tag{2.3}
\]

Indeed,

\[
 6\mathsf H(1/3)+8\mathsf H(1/4)=12\log2,           \tag{2.4}
\]

where \(\mathsf H(x)=-x\log x-(1-x)\log(1-x)\). Thus an
exponentially \(o(\operatorname{Cat}_{3n})\) set of cores can carry outer
mass at the critical \(\operatorname{Cat}_{6n}/r\) scale.

## 3. The Gaussian saddle

Put

\[
 u=\frac{k-r/6}{\sqrt r},\qquad
 v=\frac{d-r/2}{\sqrt r}.                            \tag{3.1}
\]

### Theorem 3.1

Uniformly for bounded \(u,v\) along admissible integer pairs,

\[
 \boxed{
 \frac{\mathsf M_r(d,k)}{\operatorname{Cat}_r}
 =
 \frac{9\sqrt2}{2\pi r}
 \exp\!\left[-\frac{81u^2-18uv+33v^2}{8}\right]
 (1+o(1)).}                                         \tag{3.2}
\]

#### Proof

The exponential part of (1.2), with \(x=k/r,y=d/r\), is

\[
 F(x,y)=2y\mathsf H(x/y)
 +(1+y-x)\mathsf H\!\left(\frac{2y}{1+y-x}\right).
                                                               \tag{3.3}
\]

Its unique interior maximum is

\[
 (x,y)=(1/6,1/2),\qquad F(1/6,1/2)=\log4.            \tag{3.4}
\]

The negative Hessian at the maximum is

\[
 Q=-D^2F(1/6,1/2)
 =\frac14
 \begin{pmatrix}81&-9\\-9&33\end{pmatrix},
 \qquad \det Q=162.                                  \tag{3.5}
\]

Stirling's formula and quadratic Taylor expansion give (3.2), since the
lattice-Gaussian normalizing density is

\[
 \frac{\sqrt{\det Q}}{2\pi}=\frac{9\sqrt2}{2\pi}.
 \qquad\square
\]

For example, fixing \(k=\lfloor r/6\rfloor\) and summing over
\(|d-r/2|\le a\sqrt r\) yields

\[
 \sum_d\mathsf M_r(d,k)
 \sim
 \frac{9\sqrt2}{2\pi\sqrt r}
 \left(\int_{-a}^{a}e^{-33v^2/8}\,dv\right)
 \operatorname{Cat}_r.                              \tag{3.6}
\]

Thus one curve of \(\Theta(\sqrt r)\) saddle cells already carries
\(\Theta(\operatorname{Cat}_r/\sqrt r)\) outer edges.

## 4. A prescribed return slot costs only a constant

If a predecessor passage prescribes \(z\) leaves in the final root slot,
the exact number of inverse roots producing the return is

\[
 K_r(d,k,z)=\binom{r+d-k-z-1}{2d-1}.                \tag{4.1}
\]

Writing \(A_0=r+d-k\) and \(q=2d\),

\[
 \boxed{
 \frac{K_r(d,k,z)}{P_r(d,k)}
 =\frac q{A_0}
  \prod_{j=0}^{z-1}\frac{A_0-q-j}{A_0-1-j}.}        \tag{4.2}
\]

At the saddle, for every fixed \(z\),

\[
 \frac{K_r(d,k,z)}{P_r(d,k)}
 \longrightarrow \frac34\,4^{-z}.                  \tag{4.3}
\]

In the exact central cell,

\[
 \frac{|\mathcal C_n|K_{6n}(3n,n,z)}
      {\operatorname{Cat}_{6n}}
 \sim
 \frac{9\sqrt2}{16\pi n}\,4^{-z}
 =\frac{27\sqrt2}{8\pi r}\,4^{-z}.                  \tag{4.4}
\]

So bounded slot prescription causes no entropy loss at the dangerous
Pascal saddle.

## 5. Exact passage-packing capacity

Let \(\mathcal S_{d,k}(g,z)\) be any set of rank-\(d\), peak-\(k\)
cores for which \(g\) is a predecessor passage prescribing slot \(z\).
Every inverse root counted by (4.1) starts a genuine outer gap-\(g\)
return. If \(g\le2H-1\), deletion of short outer quotient cycles and
equal-length greedy packing give

\[
 \boxed{
 \overline\nu_H\ge
 \frac{\bigl(
 |\mathcal S_{d,k}(g,z)|K_r(d,k,z)-Z_H
 \bigr)_+}{g+2}.}                                   \tag{5.1}
\]

A gap-\(g\) interval has \((g+3)/2\) quotient edges, hence at most \(g+2\)
possible conflicting starts.

### Theorem 5.2 (fatal saddle-tube density)

Fix \(A,a,\eta>0\) and \(z_0\ge0\). Put

\[
 H=A\sqrt r+O(1),\qquad H\log(2r+1)=o(r).
\]

Suppose that, for every integer \(d\) with
\(|d-r/2|\le a\sqrt r\), at least an \(\eta\)-fraction of the cores in
the cell \(k=\lfloor r/6\rfloor\) have some predecessor passage
\(g\le2H-1\) with prescribed slot \(z\le z_0\). Then

\[
 \boxed{
 \liminf_{r\to\infty}
 \frac{r\,\overline\nu_H}{\operatorname{Cat}_r}
 \ge
 \frac{27\sqrt2\,\eta}
      {4\pi A\,4^{z_0+1}}
 \int_{-a}^{a}e^{-33v^2/8}\,dv>0.}                  \tag{5.2}
\]

#### Proof

Equations (3.6) and (4.3) give at least

\[
 \left(\frac34\,4^{-z_0}+o(1)\right)
 \frac{9\sqrt2\,\eta}{2\pi\sqrt r}
 \left(\int_{-a}^{a}e^{-33v^2/8}\,dv\right)
 \operatorname{Cat}_r                               \tag{5.3}
\]

outer short-return starts. Variable-length greedy packing divides by at
most \(2H+1=2A\sqrt r+o(\sqrt r)\). The short-cycle term is
\(\exp(o(r))\) and is negligible. This proves (5.2). \(\square\)

By Theorem 17.1, (5.2) lifts to a physical packing
\(\Omega_A(\operatorname{Cat}_r)\), contradicting the little-oh required
by \((\mathrm{RP}_A)\).

## 6. No rank-only scalar weight can close the lift

At outer rank \(6n\) and reduced rank \(3n\), the largest inverse fibre
occurs at one peak:

\[
 P_{\max}=\binom{9n-1}{6n}.                         \tag{6.1}
\]

If a rank-only scalar charge \(w_n\) dominates every inverse fibre, then
\(w_n\ge P_{\max}\), and

\[
 \frac{\operatorname{Cat}_{3n}w_n}
      {\operatorname{Cat}_{6n}}
 \ge
 \exp\!\left[
 \left(\log\frac{3^9}{2^{12}}+o(1)\right)n
 \right].                                           \tag{6.2}
\]

Since \(3^9/2^{12}>1\), its total budget is exponentially larger than the
outer Catalan mass. Conversely, any rank-only budget polynomially bounded
by \(\operatorname{Cat}_{6n}\) undercharges the largest fibres by the
reciprocal exponential factor.

The same dichotomy holds for weights with only subexponential variation
over peak classes. It also persists after prescribing any fixed root-slot
occupancy, because replacing \(P_r(d,k)\) by \(K_r(d,k,z)\) changes the
relevant exponential rates by zero. This does not rule out the exact peak-sensitive,
target-rank-dependent Pascal kernel; that kernel, together with the slot
and passage condition, is precisely the remaining legitimate induction.

## 7. Scope

This is an adversarial capacity theorem, not an actual counterexample to
\((\mathrm{RP}_A)\).

* Actual exponential projection congestion occurs over the fixed
  gap-seven cores.
* Across many cores, the Gaussian Pascal saddle has enough capacity to
  refute \((\mathrm{RP}_A)\) if bounded-slot short passages have positive
  density along one saddle curve.
* Proving that this passage density vanishes is a strictly stronger task
  than bounding the unweighted lower-rank packing number.

Therefore scalar induction on
\(\overline\nu_H(d)\), or on an unweighted count of bad cores, is invalid.
The first viable recursive statement must be peak- and slot-weighted and
uniform across the full two-dimensional Pascal saddle.
