# Lane G: exact constants for recursive parent trades versus hereditary PCap

## 0. Verdict

Let

\[
 p=2m+1,\qquad W=\binom{2m+1}{m},\qquad
 r=\min\{s:\operatorname{Cat}_s\ge 4p\},
\]

and retain the Catalan overshoot

\[
 d=\operatorname{Cat}_r,\qquad \theta=\frac d p.
\]

Minimality gives the exact range

\[
 4\le \theta<16-\frac{24}{r+1}.
\]

The fixed-scale recursive parent family contains

\[
 T_{m,r}=H_{m,r+1}\operatorname{Cat}_{r-1}
       =\left(\frac1{64\sqrt\pi}+o(1)\right)
          \frac{W}{r^{3/2}}
\]

switches.  Even under perfect routing, one switch can lower one depth's
cap tail by at most four.  Its total ideal supply at one depth is therefore

\[
 \boxed{
 S_r^{\mathrm{ideal}}=4T_{m,r}
  =\left(\frac1{16\sqrt\pi}+o(1)\right)
       \frac{W}{r^{3/2}}.}
\]

The certified Catalan plateau demands

\[
 \boxed{
 D_r(\theta)=H_{m,r}\left(\frac d2-p\right)
  =\left(\frac{\theta-2}{8\theta\sqrt\pi}+o(1)\right)
       \frac{W}{r^{3/2}}}
\]

at every protected depth, before the negligible ambient term
\(W-N_q\) is subtracted.  Hence

\[
 \boxed{
 \frac{S_r^{\mathrm{ideal}}}{D_r(\theta)}
   =\frac{\theta}{2(\theta-2)}+o(1).}
\]

The ratio is one only at the bottom endpoint \(\theta=4\), and decreases
to \(4/7\) as \(\theta\) approaches sixteen.  Thus the known family is
not uniformly large enough.  For every fixed \(\varepsilon>0\), if
\(\theta\ge4+\varepsilon\), it misses the certified demand even if all
four arms of every switch are routed perfectly at every depth.

There is a narrow finite-\(r\) exception.  Put \(k=m-r\).  The exact
counting threshold is

\[
 \boxed{
 \theta\le \theta_c(m,r):=
 \frac{2(2k-1)(2r-1)}
      {(2k-1)(2r-1)-2k(r+1)}.}
\]

Equivalently,

\[
 \theta_c(m,r)=4+\frac6r+O(r^{-2}+m^{-1}).
\]

Only in this width-\(O(1/r)\) band above four does raw four-arm supply
meet the certified demand.  Passing this count is not a construction:
it requires essentially every arm to drain an overloaded target into a
nonoverloaded one.  The present parent theorem proves no such routing.

## 1. First-principles normalization

Write

\[
 H_{m,s}=\frac12\binom{2(m-s)}{m-s}
\]

for the number of aligned size-\(s\) hole contexts.  Stirling's formula
in the central-binomial form

\[
 \binom{2a}{a}=\frac{4^a}{\sqrt{\pi a}}(1+o(1))
\]

gives, uniformly for \(s=O(\log p)=o(m)\),

\[
 \begin{aligned}
 W&=\binom{2m+1}{m}
   =\frac{2m+1}{m+1}\binom{2m}{m}
   =\frac{2\,4^m}{\sqrt{\pi m}}(1+o(1)),\\
 H_{m,s}&=\frac{4^{m-s}}{2\sqrt{\pi(m-s)}}(1+o(1)),\\
 \frac{H_{m,s}}W&=\frac{4^{-s}}4(1+o(1)).
 \end{aligned}
\]

Also

\[
 \operatorname{Cat}_s
 =\frac1{s+1}\binom{2s}{s}
 =\frac{4^s}{\sqrt\pi\,s^{3/2}}(1+o(1)).
\]

Consequently

\[
 \boxed{
 \frac{H_{m,r}\operatorname{Cat}_r}{W}
 =\left(\frac1{4\sqrt\pi}+o(1)\right)r^{-3/2}.}
 \tag{1.1}
\]

This is the common normalization for supply and demand.  In particular,
neither side may hide its leading constant inside a \(\Theta\)-symbol.

The cutoff relation \(d=\theta p\), together with the Catalan asymptotic,
also yields

\[
 r=\frac{
  \log p+\frac32\log\log p+\log\theta+\frac12\log\pi
       -\frac32\log\log4}{\log4}+o(1),
\]

and hence

\[
 r^{-3/2}=(\log4)^{3/2}(\log p)^{-3/2}(1+o(1)).
 \tag{1.2}
\]

Thus every constant below can be converted to the \((\log p)^{-3/2}\)
normalization by multiplying it by \((\log4)^{3/2}\).

Finally, minimality of \(r\) says \(\operatorname{Cat}_{r-1}<4p\).  Since

\[
 \frac{\operatorname{Cat}_r}{\operatorname{Cat}_{r-1}}
 =\frac{2(2r-1)}{r+1}=4-\frac6{r+1},
\]

we obtain

\[
 4\le\theta<4\left(4-\frac6{r+1}\right)
 =16-\frac{24}{r+1}.
 \tag{1.3}
\]

The overshoot \(\theta\) cannot be silently replaced by four: the
Catalan scale advances by an asymptotic factor four.

## 2. Exact hereditary plateau demand

At every depth \(r\le q\le m/2\), the aligned size-\(r\) plateau proof
gives

\[
 K_q(F_{\mathrm{MSW}})\ge
 H_{m,r}\left(\frac d2-p\right).
 \tag{2.1}
\]

The factor \(1/2\) is the exact boundary-overlap loss: a rooted occurrence
can be charged by at most the left boundary context and the right boundary
context.  Substituting \(p=d/\theta\) and (1.1) proves

\[
 \frac1W H_{m,r}\left(\frac d2-p\right)
 =\left(\frac{\theta-2}{8\theta\sqrt\pi}+o(1)\right)r^{-3/2}.
 \tag{2.2}
\]

For PCap one subtracts

\[
 \Delta_q:=W-N_q,
 \qquad N_q=\binom{2m+1}{m-q}.
\]

Here there is an exact product

\[
 \frac{N_q}{W}=\prod_{j=0}^{q-1}\frac{m-j}{m+j+2}.
 \tag{2.3}
\]

For \(q=o(\sqrt m)\), expanding the logarithm of this product gives

\[
 \frac{\Delta_q}{W}
 =\frac{q(q+1)}m+O\!\left(\frac{q^4}{m^2}
                          +\frac{q^3}{m^2}\right).
 \tag{2.4}
\]

Take the standard hereditary cutoff

\[
 Q=\left\lfloor\frac{p^{1/4}}4\right\rfloor,
 \qquad \mathcal Q=\{r,r+1,\ldots,Q\}.
\]

Then \(\Delta_q/W=o(r^{-3/2})\) uniformly on \(\mathcal Q\), and

\[
 \sum_{q=r}^Q\frac{\Delta_q}{W}
 =\frac{Q^3}{3m}(1+o(1))
 =\left(\frac1{96}+o(1)\right)p^{-1/4}.
 \tag{2.5}
\]

The subtraction is negligible compared with the plateau sum.  Therefore

\[
 \boxed{
 \operatorname{PCap}_Q(F_{\mathrm{MSW}})
 \ge\left(\frac{\theta-2}{32\theta\sqrt\pi}+o(1)\right)
       \frac{Wp^{1/4}}{r^{3/2}}.}
 \tag{2.6}
\]

This is the hereditary PCap demand.  On the shorter traditional band
\([p^{1/4}/8,p^{1/4}/4]\), every constant in (2.6) is divided by two;
the supply-to-demand ratio is unchanged.

There is a useful factor two which the ordinary one-Lipschitz estimate
misses.  If \(\mu,\nu\) are two histograms of the same total mass, then

\[
 \boxed{
 K_p(\mu)-K_p(\nu)\le\frac12\|\mu-\nu\|_1.}
 \tag{2.7}
\]

Indeed, the positive and negative parts of \(\nu-\mu\) have the same
mass, namely \(\|\nu-\mu\|_1/2\), and only mass removed from old
coordinates can lower \(K_p\).

It follows that any exact factor \(F\) satisfying
\(\operatorname{PCap}_Q(F)=o(W)\) must obey

\[
 \boxed{
 \sum_{q=r}^Q
 \|\mu_q^F-\mu_q^{F_{\mathrm{MSW}}}\|_1
 \ge\left(\frac{\theta-2}{16\theta\sqrt\pi}+o(1)\right)
       \frac{Wp^{1/4}}{r^{3/2}}.}
 \tag{2.8}
\]

To see this without any pointwise assumption on \(F\), sum (2.7) and use

\[
 K_q(F)\le \Delta_q+\bigl(K_q(F)-\Delta_q\bigr)_+.
\]

Equation (2.8) is the exact leading hereditary distance demand.

## 3. Exact recursive parent-trade supply

The certified fixed-scale family has one switch for each pair consisting
of

1. an aligned size-\(r+1\) parent context, and
2. a spectator root in \(D_{r-1}\).

Thus

\[
 T_{m,r}=H_{m,r+1}\operatorname{Cat}_{r-1}.
 \tag{3.1}
\]

Relative to the common mass \(H_{m,r}d\), this has the exact ratio

\[
 \begin{aligned}
 \rho_{m,r}
 :=\frac{T_{m,r}}{H_{m,r}d}
 &=\frac{H_{m,r+1}}{H_{m,r}}
   \frac{\operatorname{Cat}_{r-1}}{\operatorname{Cat}_r}\\
 &=\frac{m-r}{2(2(m-r)-1)}
   \frac{r+1}{2(2r-1)}\\
 &=\boxed{
 \frac{(m-r)(r+1)}
      {4(2(m-r)-1)(2r-1)}}.
 \end{aligned}
 \tag{3.2}
\]

In particular

\[
 \rho_{m,r}=\frac1{16}(1+o(1)),
 \qquad
 \frac{T_{m,r}}W
 =\left(\frac1{64\sqrt\pi}+o(1)\right)r^{-3/2}.
 \tag{3.3}
\]

At an interior lower rank, toggling one switch replaces at most four old
targets by four new targets.  Therefore it has

\[
 \text{cap-tail decrease}\le4,
 \qquad
 \text{histogram }L^1\text{ action}\le8.
 \tag{3.4}
\]

These bounds remain valid for a nonadditive simultaneous cube by toggling
the switches sequentially and applying the triangle inequality at each
toggle.  Hence perfect one-depth supply is

\[
 4T_{m,r}
 =\left(\frac1{16\sqrt\pi}+o(1)\right)
   \frac W{r^{3/2}},
 \tag{3.5}
\]

while perfect hereditary supply over \(\mathcal Q\) is at most

\[
 \boxed{
 \begin{aligned}
 \text{cap decrease}&\le
 \left(\frac1{64\sqrt\pi}+o(1)\right)
       \frac{Wp^{1/4}}{r^{3/2}},\\
 L^1\text{ action}&\le
 \left(\frac1{32\sqrt\pi}+o(1)\right)
       \frac{Wp^{1/4}}{r^{3/2}}.
 \end{aligned}}
 \tag{3.6}
\]

The two lines differ by exactly the same factor two as demand (2.6)
versus distance demand (2.8).  They therefore give the identical capacity
test.

## 4. Exact comparison and the overshoot gate

At one depth, perfect routing can meet the main certified demand only if

\[
 4T_{m,r}\ge H_{m,r}\left(\frac d2-p\right).
\]

After division by \(H_{m,r}d\), this is

\[
 4\rho_{m,r}\ge\frac12-\frac1\theta.
 \tag{4.1}
\]

With \(k=m-r\), (3.2) gives

\[
 4\rho_{m,r}=\frac{k(r+1)}{(2k-1)(2r-1)}.
\]

Solving (4.1) for \(\theta\) proves the exact threshold

\[
 \theta\le
 \theta_c(m,r)=
 \frac{2(2k-1)(2r-1)}
      {(2k-1)(2r-1)-2k(r+1)}.
 \tag{4.2}
\]

Since \(r=O(\log p)\) and \(k\sim m\),

\[
 \theta_c(m,r)=4+\frac6r+O(r^{-2}+m^{-1}).
 \tag{4.3}
\]

Away from this narrow gate, the one-depth ideal deficit has the exact
leading constant

\[
 \boxed{
 D_r(\theta)-S_r^{\mathrm{ideal}}
 =\left(\frac{\theta-4}{16\theta\sqrt\pi}+o(1)\right)
       \frac W{r^{3/2}}.}
 \tag{4.4}
\]

Over \(\mathcal Q\), the hereditary cap-tail deficit is

\[
 \boxed{
 \left(\frac{\theta-4}{64\theta\sqrt\pi}+o(1)\right)
       \frac{Wp^{1/4}}{r^{3/2}},}
 \tag{4.5}
\]

and the corresponding hereditary \(L^1\) deficit is twice (4.5).
For every fixed \(\theta>4\), this is much larger than \(W\), so it is
incompatible with the necessary condition
\(\operatorname{PCap}_Q=o(W)\).

Equivalently, the ideal supply fraction is

\[
 \begin{array}{c|c}
 \theta& S^{\mathrm{ideal}}/D\\ \hline
 4&1\\
 8&2/3\\
 16^-&4/7.
 \end{array}
\]

The finite correction in (4.2), not the leading table, governs the
exceptional regime \(\theta-4=O(1/r)\).

## 5. Why the perfect-routing audit is optimistic

The supply above grants four useful units to every switch at every depth.
The known geometry proves substantially less.

At the packet's own depth \(q=r\), the marked boundary profile is

\[
 (d,e,e)\longmapsto(d-e,2e,e),
 \qquad e=\operatorname{Cat}_{r-1}.
\]

Because \(d\ge4p\), one has \(e>p\) and \(d-e>p\).  All displayed loads
remain above the cap, so the two marked boundary arms have exactly zero
cap-tail gain.  Only the two opposite arms can help.  Thus at \(q=r\)

\[
 \text{actual certified supply}\le2T_{m,r}
 =\left(\frac1{32\sqrt\pi}+o(1)\right)
       \frac W{r^{3/2}},
\]

only half the demand even when \(\theta=4+o(1)\).  This single-depth
deficit is itself \(o(W)\), so it does not by itself settle hereditary
PCap; it does show that the four-unit assumption is genuinely optimistic.

At larger depths, no theorem currently places all four negative endpoints
above the cap and all four positive endpoints below it.  Near the raw
threshold (4.2), all but a negligible fraction of the switches would have
to attain that extremal configuration at essentially every protected
depth.  Marked-target congestion or perfect routing of only the
distinguished arm is therefore irrelevant: the distinguished intrinsic
flow preserves cap tail.

## 6. Final decision

The known fixed-scale recursive parent family does **not** have a uniform
constant advantage over hereditary PCap demand.  Its best conceivable
four-arm supply meets the demand only when the Catalan overshoot lies in
the exceptional band

\[
 4\le\frac{\operatorname{Cat}_r}{p}
 \le4+\frac6r+O(r^{-2}+m^{-1}).
\]

For \(\operatorname{Cat}_r/p\ge4+\varepsilon\), the family is
quantitatively impossible even under perfect routing, with the explicit
deficits (4.4)--(4.5).  In the exceptional band the count is merely
critical; the current trade geometry falls far short of proving the
near-perfect four-arm drain that would be required.  Therefore this known
one-parent, one-scale family cannot close the coefficient-one lane as it
stands.  A viable repair must add parent orientations or scales with a
strict leading-constant surplus, or replace the seed so that the four-arm
endpoints are transverse to the overloaded sets.
