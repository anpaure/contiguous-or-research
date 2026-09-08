# A protected-mass dual for the pruned adjacent-scale cube

Date: 2026-07-26

Method: pure mathematics only.

Let (r) be minimal with

\[
                         d=C_r\ge4p,
 \qquad t={d\over p}\in[4,16),
\tag{0.1}
\]

and consider the exact interlaced Boolean cube

\[
 {\cal E}_r\dot\cup\widetilde {\cal E}_{r+1}
\tag{0.2}
\]

of `MATH_THEOREM_ADJACENT_SCALE_RECTANGLE_INTERLACING_CUBE_20260726.md`.
Write

\[
 M_r=H_{m,r+1}C_{r-1},
 \qquad
 \widetilde M_{r+1}=H_{m,r+2}(C_r-C_{r-1}).
\tag{0.3}
\]

The raw scalar capacity audit counts four units per bit.  At the matched
depth (q=r), this is not the true protected-mass capacity.  There is one
common dual vector, namely the indicator of the canonical overloaded set,
which gives every scale-(r) bit value at most two and every retained
scale-(r+1) bit value at most four.  Consequently every integral state,
and even every probability mixture of states, has cap tail at least

\[
 \boxed{
 H_{m,r}(d/2-p)-2M_r-4\widetilde M_{r+1}.}
\tag{0.4}
\]

In the asymptotic regime (r=o(m)), this is positive whenever

\[
                         t>{16\over3}+o(1).
\tag{0.5}

Thus the pruned two-scale cube does not have enough **oriented** capacity
to make the self-depth scalar defect identically zero over most of the
Catalan overshoot interval.  This is a genuine minimax obstruction: one
fixed fractional target potential witnesses it, so product biases cannot
average it away.

The residual is only (Theta(W/r^{3/2})=o(W)) when
(r\to\infty).  Therefore this theorem refutes exact scalar saturation,
not the desired (o(W)) aggregate conclusion by itself.

## 1. Exact dual contribution of one four-arm column

For a target weight
\(\alpha:\binom{[n]}{m-q}\to[0,1]\), define the discrete coordinate
derivative

\[
 \nabla^{\alpha}_{\beta\gamma}(K)
   =\alpha(K\cup\{\gamma\})-
      \alpha(K\cup\{\beta\}).
\tag{1.1}
\]

The exact isolated lower action of an MSW rectangle is

\[
 a_{q,e}={}
   \partial K_{O,s}+\partial K_{E,s}
  -\partial K_{E,p}-\partial K_{O,p},
 \qquad
 \partial K=e_{K\cup\{\gamma\}}-e_{K\cup\{\beta\}}.
\tag{1.2}
\]

Hence its weighted four-arm drain is exactly

\[
\boxed{
 \alpha(N_{q,e})-\alpha(P_{q,e})
 =\nabla^\alpha_{\beta\gamma}(K_{E,p})
  +\nabla^\alpha_{\beta\gamma}(K_{O,p})
  -\nabla^\alpha_{\beta\gamma}(K_{O,s})
  -\nabla^\alpha_{\beta\gamma}(K_{E,s}).}
\tag{1.3}
\]

Formula (1.3) is the prefix/suffix normal form of the weighted dual.  In
particular, if

\[
                         \alpha(S)=c+\sum_{i\in S}w_i,
\tag{1.4}
\]

then every derivative in (1.3) equals (w_\gamma-w_\beta), and the two
prefix and two suffix terms cancel.  Thus every coordinate-additive
potential keeps all four arms exactly neutral.

These neutral potentials do not give a new obstruction beyond the
unavoidable total-mass and point-margin baselines: every exact wreath
factor has the same total load and the same one-coordinate marginals at a
fixed depth.  A harmful dual must therefore contain a genuinely
higher-order target interaction.

## 2. The canonical overloaded-set potential

At depth (q=r), let

\[
                         \Omega_r=\{S:\mu_r^{MSW}(S)>p\},
 \qquad                  \alpha_r=\mathbf1_{\Omega_r}.
\tag{2.1}
\]

Then

\[
 \langle\alpha_r,\mu_r^{MSW}-p\mathbf1\rangle
 =K_{r,p}(F_{MSW})
 \ge H_{m,r}(d/2-p).
\tag{2.2}
\]

Inside one scale-(r) parent context, the three marked canonical loads
are

\[
                         (d,e,e),
 \qquad e=C_{r-1},
\tag{2.3}
\]

and every one is strictly above (p).  The complete rectangle packet
changes them as

\[
                         (d,e,e)\longmapsto(d-k,e,e+k).
\tag{2.4}
\]

Thus the two marked arms of every elementary scale-(r) switch have both
endpoints in (Omega_r).  Their contribution to (1.3) for
(alpha_r) is zero.  Only the two opposite cyclic arms can cross the
fixed cut.  Therefore

\[
 \boxed{
 \alpha_r(N_{r,e})-\alpha_r(P_{r,e})\le2
 \qquad(e\in{\cal E}_r).}
\tag{2.5}
\]

For a retained scale-(r+1) switch, the universal four-arm bound gives

\[
 \boxed{
 \alpha_r(N_{r,e})-\alpha_r(P_{r,e})\le4.}
\tag{2.6}
\]

No unproved orientation statement is used in (2.6); it deliberately
grants every larger-scale bit its maximum conceivable value.

## 3. One common cut controls every cube state

### Theorem 3.1 (statewise and fractional dual bound)

Let (F_x) be any integral state of the pruned interlaced cube.  Then

\[
\boxed{
 \left\langle\alpha_r,\mu_r^{F_x}-p\mathbf1\right\rangle
 \ge
 K_{r,p}(F_{MSW})-2M_r-4\widetilde M_{r+1}.}
\tag{3.1}
\]

Consequently

\[
\boxed{
 K_{r,p}(F_x)
 \ge H_{m,r}(d/2-p)-2M_r-4\widetilde M_{r+1}.}
\tag{3.2}
\]

The same lower bound holds for the cap tail of the mean histogram under
any probability law on cube states, including every product-bias law.

#### Proof

Toggle all selected scale-(r) switches first.  At their self-depth these
switches are additive, and (2.5) says that each can decrease the fixed
(alpha_r)-mass by at most two.  Next toggle the selected retained
scale-(r+1) switches.  The interlacing theorem says the final exact
factor is independent of this ordering.  Boundary locality says one
toggle changes at most four old targets into four new targets at depth
(r), so (2.6) bounds its decrease of the fixed
(alpha_r)-mass by four, even in the current state.  Telescoping proves
(3.1).

For every (0\le\alpha\le1),

\[
 K_p(y)=\sum_S(y(S)-p)_+
       \ge\langle\alpha,y-p\mathbf1\rangle.
\]

Use (alpha=\alpha_r), then (2.2), to obtain (3.2).

Every state satisfies the same linear inequality (3.1).  Averaging it
over an arbitrary law preserves the inequality, and applying the last
display to the mean histogram proves the fractional assertion.  (square)

This is stronger than a dynamic cap argument with a changing overloaded
set: it is one explicit protected-mass dual witness valid simultaneously
for all states.

## 4. Exact overshoot threshold

Put

\[
                         k=m-r-1,
\]

and recall

\[
 \rho_{m,r}={M_r\over H_{m,r}d}
 ={(k+1)(r+1)\over4(2k+1)(2r-1)}.
\tag{4.1}
\]

The retained next-scale ratio is

\[
 x_{m,r}:={\widetilde M_{r+1}\over M_r}
 ={3k(r-1)\over2(2k-1)(r+1)}.
\tag{4.2}
\]

Divide (3.2) by (H_{m,r}d).  Its normalized right side is

\[
 \boxed{
 \frac12-\frac1t
 -\rho_{m,r}\bigl(2+4x_{m,r}\bigr).}
\tag{4.3}
\]

For (r=o(m)),

\[
 \rho_{m,r}\bigl(2+4x_{m,r}\bigr)
 ={5\over16}+O\left({1\over r}+{r\over m}\right).
\tag{4.4}
\]

Hence the exact threshold is

\[
 t^\dagger_{m,r}
 =\left[
    \frac12-\rho_{m,r}(2+4x_{m,r})
   \right]^{-1}
 ={16\over3}+O\left({1\over r}+{r\over m}\right),
\tag{4.5}
\]

whenever the bracket is positive.  If

\[
                         t\ge{16\over3}+\varepsilon
\]

and (r=o(m)), then every cube state and every fractional mixture has

\[
 K_{r,p}\ge
 c_\varepsilon H_{m,r}C_r
 =\Theta_\varepsilon\left({W\over r^{3/2}}\right).
\tag{4.6}
\]

At the extreme (t\to16), the normalized residual tends to

\[
                         {7\over16}-{5\over16}={1\over8}.
\]

## 5. Minimax verdict

The Catalan prefix/suffix form has two exact implications.

1. Degree-zero and degree-one target potentials keep every four-arm
   column neutral, but they see only the universal balanced baselines.
2. The higher-order potential (alpha_r=\mathbf1_{\Omega_r}) is a
   genuine protected-mass witness.  It proves that the pruned adjacent
   cube cannot exactly saturate the matched depth for
   (C_r/p>16/3+o(1)), even fractionally and even if every retained larger
   switch is optimally oriented.

The theorem does **not** rule out (operatorname {PCap}=o(W)), because
the one-depth residual in (4.6) is itself (o(W)) at the logarithmic
scale.  To obtain an aggregate no-go one would have to propagate one
common higher-order dual through a growing range of depths.  Conversely,
a positive construction must show that the larger-scale arms defeat all
such non-additive fractional tests after summing coherently over depth.

### Scope correction: this pruning is not weighted-maximal

The \(16/3\) threshold is exact for the specified cube, which deletes the
larger endpoint of every adjacent-scale conflict. It is not the maximum
self-depth capacity among all literal two-scale prunings. At depth \(r\),
the two conflict endpoints have weights two and four, so the
capacity-maximizing choice deletes the scale-\(r\) endpoint. Its envelope
is

\[
 2M_r+4M_{r+1}-2E_r
 =\left({11\over32}+o(1)\right)H_{m,r}C_r,
\]

and its raw threshold is \(t=32/5+o(1)\). The full three-scale audit is
given in
MATH_THEOREM_MSW_THREE_SCALE_RMINUS_MENU_AND_DUAL_AUDIT_20260726.md.
