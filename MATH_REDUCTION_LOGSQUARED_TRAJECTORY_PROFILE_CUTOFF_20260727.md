# A trajectory-specific \((\log m)^2\) profile cutoff

Date: 2026-07-27

## 0. Outcome

The post-collar consecutive-spine obstruction applies only if a scalar
profile hierarchy is propagated through orders \(k\ge H\).  It is enough to
stop much earlier.  Put

\[
 J=\lceil(\log m)^2\rceil=o(H).
\tag{0.1}
\]

The proved time-zero higher-codegree theorem implies that the total marked
mass of all equality-resolved order-\(J\) terminal profiles reachable from
one physical marked incidence is

\[
 \boxed{\exp[-(1-o(1))J\log m]
       =\exp[-(1-o(1))(\log m)^3].}
\tag{0.2}
\]

Consequently a direct stopped-supermartingale quarantine of the terminal
profiles costs \(o(W)\).  No pointwise terminal estimate in an arbitrary live
subcatalogue is needed.  The remaining dynamic theorem is finite: propagate
the already proved pair-profile estimate only through orders
\(2,\ldots,J-1\), with a total crossing error \(o(1/J)\) per marked
incidence.

This is a reduction, not yet the missing uniform stopped theorem.

## 1. Static terminal mass

For \(2\le s\le J\), the ordinary-frame higher-codegree theorem gives, for
every \(s\) distinct owner resources,

\[
 \frac{d_0(X_1,\ldots,X_s)}{D_0}
 \le
 \left(\frac{C(s-1)^2}{m^2}\right)^{s-1}.
\tag{1.1}
\]

The same conclusion, with only a changed absolute constant, holds after the
finite equality resolution of top, owner, row, and compensation types used
by the physical generator.  At each extension step a catalogue edge exposes
at most \(r=O(m)\) new physical resources.  Therefore the number of ordered
terminal profiles of length \(J\) generated from one marked root occurrence
is at most \((Cm)^{J-1}\).  Multiplying by (1.1),

\[
\begin{aligned}
 \mathfrak q_J
 &\le (Cm)^{J-1}
   \left(\frac{CJ^2}{m^2}\right)^{J-1}\\
 &\le \left(\frac{CJ^2}{m}\right)^{J-1}.
\end{aligned}
\tag{1.2}
\]

Since \(J=(\log m)^2\),

\[
 \log\mathfrak q_J
 \le -(J-1)\bigl(\log m-O(\log\log m)\bigr),
\tag{1.3}
\]

which proves (0.2).  This estimate deliberately overcounts every ordered
equality type; all polynomial compiler multiplicities are absorbed.

## 2. Terminal crossings are paid at time zero

For a fixed terminal profile \(S\), let

\[
 M_S(t)=\frac{d_t(S)}{d_0(S)u_t^{r-|S|}}
\tag{2.1}
\]

with the standard integrating factor for the already controlled physical
union error.  Until the degree and lower-order stops, \(M_S\) is a
nonnegative stopped supermartingale starting at one; deaths of \(S\) are
terminal and favorable.

At threshold \(A_J\ge1\), Doob gives

\[
 \Pr(\sup_tM_S(t)\ge A_J)\le A_J^{-1}.
\tag{2.2}
\]

If a crossing quarantines its complete active incidence star, that star is
at most \(A_J\) times its natural reference at first crossing.  Hence the
factor \(A_J\) cancels (2.2).  Summing with the time-zero profile weights in
(1.2),

\[
 \boxed{
 \mathbb E[\text{terminal order-\(J\) quarantined marked incidence}]
 \le \mathfrak q_J\,\mathfrak I,}
\tag{2.3}
\]

where \(\mathfrak I\) is the marked owner/root incidence normalization.
Equation (0.2) makes this smaller than \(m^{-A}\mathfrak I\) for every fixed
\(A\).

This is trajectory-specific.  It is not contradicted by the physical
pair-star residual which falsifies a pointwise terminal condition under
arbitrary edge deletion: that residual is not inserted as a new initial
state, and reaching it from the full process would require a preceding
stopped martingale deviation.

## 3. The finite dynamic gate

For \(2\le k<J\), let \(\mathrm{PF}_k\) be the natural time-zero-profile
stop.  Suppose the equality-resolved one-step stopped estimate is proved
uniformly in this range:

\[
 \mathbb E[\mathrm{PF}_k\text{-stopped marked incidence before }
             \mathrm{PF}_{k+1}]
 \le \varepsilon_m\mathfrak I,
 \qquad J\varepsilon_m=o(1).
\tag{3.1}
\]

Stop every marked occurrence at its first violated order.  The stopped
families are disjoint, so (2.3) and (3.1) give

\[
 \boxed{
 \mathbb E[\text{all profile-stopped marked incidence}]
 \le (J\varepsilon_m+\mathfrak q_J)\mathfrak I
 =o(\mathfrak I).}
\tag{3.2}
\]

Integrating against the exact selected-incidence clock converts (3.2) to
\(o(W)\).  The closed whole-arm factorial theorem then supplies the top-strip
estimate needed by the ordinary-frame process.

## 4. Exact remaining statement

The infinite boundary is removed.  What remains is the growing but
polylogarithmic trajectory theorem (3.1).  Its order-two case, before the
triple-profile stop, is already proved using the physical theta kernel.
The required extension is only through \(J=(\log m)^2\), precisely the range
in which the static higher-codegree theorem (1.1) is valid with overwhelming
terminal slack.

No claim is made here that the one-step quadratic-variation constants are
uniform through \(J\); proving that is the sole stochastic gate left by this
reduction.
