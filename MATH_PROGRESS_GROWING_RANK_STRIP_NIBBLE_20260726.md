# Quantitative growing-rank audit of the critical strip nibble

Date: 2026-07-26

Method: pure mathematics.  The probability calculations below are
self-contained; no fixed-uniformity matching theorem is invoked.

## 0. Outcome

Let \(\mathcal H_{\rm crit}\) be the \(6h\)-uniform hypergraph whose
vertices are the three ranks \(m-1,m,m+1\), and whose edges are the
critical targets of physical \(C_{2h}\)-strips.  Put

\[
                         k=6h,\qquad D=D_1.
\tag{0.1}
\]

Its degrees are \(D,D,\frac{m}{m+1}D\), and its maximum pair codegree is

\[
                         C=\frac{2D}{m+1}.
\tag{0.2}
\]

The exact conflict degree of one strip satisfies

\[
 \boxed{
 |\Gamma(E)|
 =kD\left(1+O\!\left(\frac{k}{m}\right)\right).}
\tag{0.3}
\]

Consequently one independent Bernoulli bite, retaining only isolated
sampled strips, rigorously produces a matching which covers

\[
 \left(\frac1{ek}+o\!\left(\frac1k\right)\right)
\tag{0.4}
\]

of each side rank and the same absolute number of middle vertices.
This tracks the growing uniformity exactly: one bite covers
\(\Theta(1/h)\), not a constant fraction.

The ideal multiround trajectory is nevertheless quantitatively viable.
If the residual hypergraph remains quasiregular, then
\(\Theta(h\log m)\) bites leave \(m^{-\gamma}\) of every rank uncovered
for any fixed

\[
                         0<\gamma<\frac14.
\tag{0.5}
\]

Throughout that trajectory the ideal residual degree is still

\[
 \exp\!\left((2-6\gamma+o(1))h\log m\right),
\tag{0.6}
\]

and the growing-rank codegree parameter remains

\[
 k\,\frac{C_t}{D_t}
 =m^{-1/4+\gamma+o(1)}=o(1).
\tag{0.7}
\]

Thus there is no mean-field or degree-exhaustion obstruction.  The one
unproved step is a uniform concentration theorem showing that the actual
random-greedy residual stays quasiregular for
\(\Theta(h\log m)\) rounds.  Fixed-uniformity Pippenger--Spencer does not
supply this dependence, and the elementary one-bite calculation cannot
be iterated without it.

No almost-perfect matching is claimed here.

## 1. Exact conflict-neighbourhood size

For a critical hyperedge \(E\), let

\[
 \Gamma(E)=\{F\ne E:F\cap E\ne\varnothing\}.
\tag{1.1}
\]

The edge \(E\) has \(4h\) side vertices of degree \(D\) and \(2h\)
middle vertices of degree

\[
                         D_0=\frac{m}{m+1}D.
\tag{1.2}
\]

For \(v\in E\), let
\(\mathcal A_v=\{F\ne E:v\in F\}\).  Then

\[
 \Gamma(E)=\bigcup_{v\in E}\mathcal A_v.
\tag{1.3}
\]

The union bound gives

\[
 |\Gamma(E)|
 \le4h(D-1)+2h(D_0-1)
 =kD\left(1+O(m^{-1})\right).
\tag{1.4}
\]

Bonferroni and (0.2) give

\[
 \begin{aligned}
 |\Gamma(E)|
 &\ge
 \sum_{v\in E}(d(v)-1)
 -\sum_{\{u,v\}\in\binom E2}
      (d(u,v)-1)\\
 &\ge
 4h(D-1)+2h(D_0-1)
 -\binom{k}{2}\frac{2D}{m+1}\\
 &=kD\left(1-O\!\left(\frac{k}{m}\right)\right).
 \end{aligned}
\tag{1.5}
\]

Equations (1.4)--(1.5) prove (0.3).  Coordinate transitivity makes
\(|\Gamma(E)|\) independent of the chosen strip, but uniformity is already
enough for the estimates.

For

\[
 h=m^{3/4+o(1)}
\tag{1.6}
\]

the relative error in (0.3) is
\(O(m^{-1/4+o(1)})\).

## 2. One rigorous random bite

Choose every catalogue strip independently with probability

\[
                         p=\frac{a}{kD},
\qquad 0<a\le1,
\tag{2.1}
\]

and retain a chosen strip precisely when no intersecting strip was
chosen.  The retained strips form a matching.

For a fixed strip \(E\),

\[
 \begin{aligned}
 \Pr(E\text{ is retained})
 &=p(1-p)^{|\Gamma(E)|}\\
 &=\frac{a}{kD}
 \exp\!\left[
 -a+O\!\left(\frac{ak}{m}+\frac1{kD}\right)
 \right].
 \end{aligned}
\tag{2.2}
\]

Let \(M=|E(\mathcal H_{\rm crit})|\).  Counting incidences on either
side layer gives

\[
                         M\cdot2h=N_1D,
\qquad
 M=\frac{3N_1D}{k}.
\tag{2.3}
\]

Therefore the expected number of retained strips is

\[
 \mathbb E|\mathcal M|
 =
 \left(ae^{-a}+o(1)\right)
 \frac{3N_1}{k^2}.
\tag{2.4}
\]

Every retained strip covers \(2h=k/3\) vertices in each of the three
parts.  Hence the expected number covered in either side rank is

\[
 \left(ae^{-a}+o(1)\right)\frac{N_1}{k},
\tag{2.5}
\]

and the middle rank has the same absolute coverage.  Some outcome has at
least the expected number of retained strips, proving the existence of a
matching with (2.5).

The function \(ae^{-a}\) is maximized at \(a=1\).  Thus this entire
one-shot “sample and keep isolated edges” scheme has its natural scale
\(1/(ek)=1/(6eh)\) per rank.  An almost-perfect matching necessarily
requires iteration or a different global mechanism.

## 3. The ideal iterative trajectory

This section is a conditional parameter audit, not a concentration
proof.  Suppose at round \(t\) the residual hypergraph has:

1. all side degrees \((1+o(1))D_t\);
2. all middle degrees
   \((\frac m{m+1}+o(1))D_t\); and
3. relative codegree \(\delta_t=C_t/D_t\) with \(k\delta_t=o(1)\).

Apply the bite (2.1) with \(D_t\) in place of \(D\).  The calculation in
Section 2 gives the common side coverage fraction

\[
 \theta_t=
 \frac{ae^{-a}}k
 \left(1+O(k\delta_t)+o(1)\right).
\tag{3.1}
\]

Ignoring the displayed vanishing error, after

\[
 T=
 \frac{k}{ae^{-a}}\log\frac1\varepsilon
\tag{3.2}
\]

rounds the uncovered fraction is \(\varepsilon+o(1)\).

Under independent-thinning heuristics, a degree requires the other
\(k-1\) vertices of an edge to survive, while a codegree requires only
\(k-2\).  Thus at residual vertex density \(\varepsilon\),

\[
 D_T\asymp D\,\varepsilon^{k-1},
\qquad
 \frac{C_T}{D_T}\asymp\frac{C/D}{\varepsilon}.
\tag{3.3}
\]

These two predictions can be audited numerically without any hidden
constant.  Stirling gives

\[
 \log D
 =\log\frac{(m+1)!(m-1)!}{2(m-h)!^2}
 =(2+o(1))h\log m.
\tag{3.4}
\]

Take \(\varepsilon=m^{-\gamma}\).  Since \(k=6h\),

\[
 \log D_T
 =
 (2-6\gamma+o(1))h\log m.
\tag{3.5}
\]

This remains superpolynomially large for every \(\gamma<1/3\).
Moreover, using \(C/D=2/(m+1)\),

\[
 k\frac{C_T}{D_T}
 =
 m^{-1/4+\gamma+o(1)}.
\tag{3.6}
\]

It tends to zero for every \(\gamma<1/4\).  Choosing, for example,
\(\gamma=1/8\) would leave \(m^{-1/8}W=o(W)\) vertices while retaining
enormous degree and vanishing \(k\)-scaled codegree.

The common conflict-neighbourhood correction in (0.3) does not obstruct
this trajectory.  In one bite it changes the coverage probability by
relative \(O(k/m)\), hence by absolute \(O(1/m)\).  Across
\(T=O(k\log m)\) ideal bites its cumulative scalar effect is

\[
                         O\!\left(\frac{k\log m}{m}\right)
 =o(1).
\tag{3.7}
\]

The correction may change the clock parametrization but not the predicted
endpoint.

## 4. The exact missing lemma

To turn Section 3 into a theorem one needs the following growing-rank
residual statement.

> **Residual quasiregularity lemma.** With positive probability, after
> every one of \(T=O(k\log m)\) isolated-edge bites, all but \(o(W)\)
> surviving vertices have degrees
> \((1+o(1))D_t\), the two side ranks have the same density, the middle
> rank differs by only \(1+O(1/m)\), and
> \(kC_t/D_t=o(1)\).

If the exceptional vertices in this lemma are quarantined once, rather
than afresh at every round, the retained isolated edges form a matching
covering all but \(m^{-\gamma+o(1)}W=o(W)\) vertices in each rank.

The difficulty is concentration, not the deterministic dependency
ledger.  For two incident candidate strips, the number of common
conflict variables is controlled by sums of higher codegrees, and a
single sampled strip can affect many residual degrees.  A fixed-rank
Chernoff argument therefore does not apply verbatim.  The enormous value
of \(D_t\) makes a polynomial-concentration proof plausible, but it is
not supplied here.

In particular, merely citing the fixed-\(k\) Pippenger--Spencer theorem
would leave exactly the dependence in (3.5)--(3.6) unchecked.

## 5. Rigorous conclusion

Proved:

* the uniform conflict-neighbourhood estimate (0.3);
* the exact one-bite coverage law (2.5), with all dependence on \(h\)
  displayed;
* the absence of a mean-field, residual-degree, or codegree barrier down
  to \(m^{-\gamma}\) density for every \(\gamma<1/4\).

Not proved:

* simultaneous residual-degree concentration for \(O(h\log m)\) bites;
* an almost-perfect matching; or
* a quantitative obstruction to such a matching.

The growing-uniformity issue has therefore been reduced to one precise
concentration lemma.  All scalar parameters remain favorable throughout
the required trajectory.
