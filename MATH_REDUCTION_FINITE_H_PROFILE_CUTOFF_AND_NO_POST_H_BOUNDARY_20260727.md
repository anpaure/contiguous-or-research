# Finite geometric profile cutoff: the post-\(H\) spine need not be entered

Date: 2026-07-27

## 0. Purpose and status

The scalar all-order profile energy is impossible because the aggregate
consecutive-spine child kernel becomes order one at

\[
H=\Theta(\sqrt{m\log m}).
\]

This note proves a conditional reduction which stops **at** that crossover.
It does not assume, and does not need, any contraction for profile orders
\(k\ge H\).

The remaining catalogue input is the equality-resolved low-order child
estimate (CPS\(_{<H}\)) below.  Once that estimate and the already audited
stopped-generator calculation are available uniformly for \(k<H\), the
entire profile boundary has \(o(W)\) marked incidence.  Thus the consecutive
spine no-go does not force propagation past \(H\); it identifies the correct
place to terminate it.

## 1. Relevant child relation

Let

\[
q_k(S)=\frac{d_0(S)}{D_0}
\]

for an equality-resolved physical \(k\)-profile.  A child of \(S\) is not an
arbitrary extra resource.  It is one of the ordered column--row or
compensation fibres which occurs after exposing the first new physical
resource in the stopped generator.  Write this finite multiset as
\(\mathscr C(S)\), with the physical equality multiplicities retained.

The required low-order estimate is

\[
\boxed{
 \sum_{T\in\mathscr C(S)}q_{k+1}(T)
 \le \frac{C}{m}q_k(S),
 \qquad 2\le k<H.}
\tag{CPS\(_{<H}\)}
\]

No assertion is made at \(k=H\).  The exact consecutive-spine calculation
shows that an extension of (CPS\(_{<H}\)) past \(H\) would be false.

Iterating the displayed inequality gives, for every order-two root profile
\(S_2\),

\[
\boxed{
 \sum_{S_2\leadsto S_H}q_H(S_H)
 \le \left(\frac{C}{m}\right)^{H-2}q_2(S_2),}
\tag{1.1}
\]

where the sum is over equality-resolved child chains and includes their
ordered multiplicities.  This is a literal induction; no independence or
product approximation is used.

## 2. Direct terminal quarantine at order \(H\)

For a live profile \(S\) of order \(k\), use its natural normalized link

\[
 M_S(t)=\frac{d_t(S)}{d_0(S)u_t^{r-k}},
\tag{2.1}
\]

multiplied by the harmless integrating factor which absorbs the already
proved whole-arm error.  Up to the degree and lower-profile stops,
\(M_S\) is a nonnegative stopped supermartingale with
\(M_S(0)=1\).  Terminal deaths only decrease it.

Fix a terminal threshold \(A_H\ge1\).  Doob's inequality gives

\[
 \Pr\!\left(\sup_t M_{S_H}(t)\ge A_H\right)\le A_H^{-1}.
\tag{2.2}
\]

Weight (2.2) by the time-zero marked occurrence mass of \(S_H\), and sum
over all relevant order-\(H\) descendants of a marked order-two profile.
For the **number of crossing profiles**, equation (1.1) yields

\[
\boxed{
 \mathbb E[\hbox{terminal order-\(H\) crossing-profile mass}]
 \le \frac1{A_H}
      \left(\frac{C}{m}\right)^{H-2}
      \mathfrak I_2.}
\tag{2.3}
\]

Here \(\mathfrak I_2\) is the initial marked order-two incidence mass.  The
estimate already includes the number of relevant child profiles.  There is
no union bound over ambient \(H\)-sets.

If stopping one crossing profile quarantines its whole active incidence
star, that star has size at most \(A_H\) times its natural reference at the
first crossing.  This cancels the factor \(A_H^{-1}\), giving the safe
physical-incidence estimate

\[
\boxed{
 \mathbb E[\hbox{terminal order-\(H\) quarantined incidence}]
 \le
       \left(\frac{C}{m}\right)^{H-2}
       \mathfrak I_2.}
\tag{2.3a}
\]

Since \(H\to\infty\), the factor in (2.3) is

\[
 \exp[-(1+o(1))H\log m],
\tag{2.4}
\]

and is negligible even after every polynomial type, arm, cohort, and
position multiplicity used by the compiler.

## 3. Closing the lower orders

Assume the stopped one-step profile estimate is available uniformly for
\(2\le k<H\): before the order-\((k+1)\) stop, order-\(k\) crossings have
marked incidence at most

\[
 \varepsilon_m\,\mathfrak I_k,
 \qquad
 H\varepsilon_m=o(1).
\tag{3.1}
\]

This is the same physical-union/Freedman statement already proved at
\(k=2\) before the triple-fibre stop.  It must be audited uniformly only in
the contracting range \(k<H\).

Stop a marked occurrence at its first violated order.  The stopped families
are disjoint.  Summing (3.1) over \(k<H\), then adding (2.3), gives

\[
\boxed{
 \mathbb E[\hbox{total profile-stopped marked incidence}]
 \le H\varepsilon_m\,\mathfrak I_2
   +(C/m)^{H-2}\mathfrak I_2
 =o(\mathfrak I_2).}
\tag{3.2}
\]

After integration against the exact selected-incidence clock, whose total
mass is \((1+o(1))W(1-z)\), equation (3.2) is \(o(W)\).

Equivalently, one may package the levels \(2,\ldots,H\) in the finite
factorial EGF characteristic.  Its input fugacity is \(O(\log(1/z))\), and
the omitted top coefficient is charged by (2.3).  The direct stopped-family
form above makes clear that no post-\(H\) scalar weight is introduced.

## 4. Exact remaining theorem

The post-\(H\) consecutive spine is no longer a gate.  The remaining
statement is the following finite but growing geometric theorem:

> For every equality-resolved physical child orbit of the ordinary-frame
> catalogue and every \(2\le k<H\), prove (CPS\(_{<H}\)) and the uniform
> one-step stopped estimate (3.1), with \(H\varepsilon_m=o(1)\).

The order-two instance and its theta quadratic-variation estimate are
already proved.  What remains is uniformity through the collar scale, not an
all-order extension to complete edges.

This reduction is compatible with the scalar-spine no-go: it never assigns
weights to orders \(k>H\), precisely where the aggregate kernel ceases to
contract.
