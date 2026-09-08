# Depth-dependent reverse product: finite probability, charge, parity, and onset

2026-09-08. Independent audit by `exact_b_finite_frontier`. Pure proof and source reads; no new mathematical computation or construction search was run.

**Verdict.** The depth-dependent product argument passes, including a finite shifted-Riemann estimate. Its onset can be reduced to `log r >= 65536`. Together with the linked finite PBBS construction and local arithmetic inputs, it proves

\[
\boxed{\displaystyle
\frac{\nu(k)}{W(k)}\le 1+
\exp\!\left[-\frac35\bigl(k(\log k)^2\bigr)^{1/5}\right]
\quad\text{for every integer }k\ge 2^{131073}+1.}
\tag{1}
\]

This is an upper bound realized by the height-adaptive construction. It is not an exact-equality result for ν(k)=B(k). All logarithms in this note are natural.

## 1. Finite domain and scale estimates

Put

\[
X=\log r\ge 65536,\quad D=\log X,\quad
\Gamma=r^{1/5}X^{-3/5},\quad
T=\Gamma X=(rX^2)^{1/5},\quad L=\lfloor2T\rfloor.
\]

On this entire domain,

\[
D\le X/4000.
\tag{2}
\]

At the endpoint, `log 65536 = 16 log 2 < 16 < 65536/4000`; the derivative of `X/4000-log X` is positive for X>4000. It follows that

\[
\log(\Gamma/X)=\frac{X-8D}{5}\ge X/6\ge100,
\quad \Gamma\ge2^{100}X,
\quad T\ge2^{100}X^2,
\quad \Gamma^2\ge2^{100}T.
\tag{3}
\]

Here e>2 was used. Also

\[
\log T=(X+2D)/5<X/4,\quad
L+2\le3T<r,\quad r/T^3=\Gamma^2.
\tag{4}
\]

In particular T≥4000, T≥600X, T≥200 log 2, and

\[
\frac{\sqrt r}{L+2}\ge\frac{\Gamma\sqrt T}{3}>800.
\tag{5}
\]

These explicit guards replace the older requirement `log log r >= 2^20`; no argument below relies on that larger domain.

## 2. Established finite local inputs

The complete local proof and exact arithmetic certificate are in
[the sharp residue/NB/integral audit](PBBS_SHARP_UNIMODAL_NB_AND_DEPTH_INTEGRAL_INDEPENDENT_AUDIT_20260908.md), which was read for this audit. It proves the following uniformly on the domain in §1.

Use the auxiliary probability law `P*(D)=4^{-|D|}/2` on all finite rooted Dyck words. Conditional on the entire deeper profile at a depth 0≤s<L, put b=a_{s+1}, c=a_{s+2}. The full parent law is

\[
a_s=2b-c+\operatorname{NB}(2b+1,(s+2)^{-2}).
\]

When the two child values are within one percent of their reference values r/(s+2), r/(s+3), the full conditional law satisfies

\[
2a_s+1\ge Y_0:=r/(L+2),\qquad
\rho_s\le\frac{1.001(s+2)^{3/2}}{2\sqrt{.99\pi r}}.
\]

The finite NB lemma requires pq≥1000. Here pq≥r/(L+2)^3≥Γ²/27, so (3) verifies this requirement explicitly. The support is infinite; no parent-regularity or primitive-row condition is imposed on this law.

For every deterministic integer 1≤v≤exp(7T/10), the sharp logarithmic-gcd inequality gives

\[
\Pr_*\bigl(v\bmod(2a_s+1)=0\mid\text{entire deeper profile}\bigr)
\le b_s:=\frac{251}{1000}+
\frac14\left(\frac{s+2}{T}\right)^{3/2}.
\tag{6}
\]

The finite constants in (6) can be checked directly from (2):

\[
\log Y_0\ge .8X-.4D-\log3\ge .799X,
\]

\[
\log(2+\log v)+20\le .2X+.4D+20,
\quad .4D+20\le X/10000+X/3000<.000549X.
\]

Since `.251*.799=.200549`, the first term divided by log Y_0 is at most .251. The second coefficient is less than 1/4 by π>25/8 and the exact rational comparison

\[
\left(\frac{7007}{3995}\right)^2<\frac{99}{32}.
\]

The cited audit supplies the sharp unimodal discrepancy and finite Stirling proof needed here, rather than assuming an asymptotic Gaussian atom estimate.

Let

\[
\phi(t)=-\log\left(\frac{251}{1000}+\frac{t^{3/2}}4\right),
\qquad I=\int_0^2\phi(t)\,dt.
\]

The independently executed rational certificate in
[depth_product_rational_certificate_20260908.json](depth_product_rational_certificate_20260908.json)
proves

\[
I>1.41158740928968704395986676100717634170197891388258
>1.411.
\tag{7}
\]

The first number is a lower bound furnished by a finite rational sum, not a claimed exact integral value. No floating-point integration is a premise.

## 3. The shifted finite product

The function φ is decreasing and positive through t=2.01. Positivity follows, for example, from `sqrt(2.01)<10/7`, which gives `.251+(2.01)^{3/2}/4 < .251+201/280 < 1`. Also φ(0)<2, since `1000/251<4<e²`.

The tested sample points are j/T for j=2,...,L+1. They are shifted two units, so an uncorrected appeal to a limiting Riemann integral would leave a gap. Monotonicity gives the finite estimate

\[
\begin{aligned}
\frac1T\sum_{s=0}^{L-1}\phi\left(\frac{s+2}{T}\right)
&\ge\int_{2/T}^{(L+2)/T}\phi(t)\,dt\\
&\ge I-\int_0^{2/T}\phi(t)\,dt
\ge I-\frac{2\phi(0)}T.
\end{aligned}
\]

Here `(L+2)/T>2`, while `(L+2)/T<=2+2/T<=2.01`; thus the extra integral beyond 2 is nonnegative. Using (7), φ(0)<2 and T≥4000 gives

\[
\sum_{s=0}^{L-1}\phi((s+2)/T)>1.411T-4\ge1.41T.
\]

Consequently the actual finite product satisfies

\[
\boxed{\prod_{s=0}^{L-1}b_s\le e^{-1.41T}.}
\tag{8}
\]

## 4. Coarse-profile and primitive-row exceptions

Under the uniform fixed-size Dyck law P_r define

\[
\mathcal A=\{\lvert a_j-r/(j+1)\rvert\le .01r/(j+1),\ 0\le j\le L+1\}.
\]

The finite one-depth concentration input is

\[
\Pr_r(\lvert a_j-r/(j+1)\rvert>(4+x)\sqrt r)\le2e^{-x^2/6}.
\]

It is the input used in §2 of
[the earlier fixed-size profile audit](PBBS_REVERSE_PROFILE_FIXED_SIZE_TRANSFER_EXPLICIT_DOMAIN_AUDIT_20260908.md).
That earlier note used another depth; here we recheck the concentration parameter for the present L. By (5),

\[
.01\sqrt r/(j+1)-4\ge\sqrt r/[200(L+2)].
\]

Depth zero is fixed, so a union over the other L+1 depths gives

\[
\Pr_r(\mathcal A^c)
\le2(L+1)e^{-r/[240000(L+2)^2]}.
\tag{9}
\]

The auxiliary whole-row law and primitive estimate are proved in
[the whole-row and tower audit](PBBS_LOG_GCD_WHOLE_ROW_LAW_AND_SUCCESSIVE_CONDITIONING_AUDIT_20260908.md), §§1–2 and 5. The inverse fixed-size conditioning probability is bounded by

\[
Q_r=2(r+1)(2r+1)\le12r^2.
\tag{10}
\]

This Q_r is an upper bound for that inverse probability, not an assertion of equality. The exact row law before fixed-size conditioning is an iid geometric vector of odd length p=2a_{s+1}+1. Its probability of nonprimitivity is at most `p exp(-2pq/3)`, where q=(s+2)^{-2}; a one-entry row has no primitive failure. Dropping other restrictions before using that kernel, paying (10) once, and summing over depths proves

\[
\Pr_r(\mathcal A\text{ and a tested row is nonprimitive})
\le Q_r L(3r+1)e^{-2r/[3(L+2)^3]}.
\tag{11}
\]

Let G be A together with primitivity of the first L rows. To verify a finite clean error bound, use L+2≤3T in (9)–(11):

\[
\frac{r}{240000(L+2)^2}\ge\frac{T\Gamma^2}{2160000}\ge4T,
\quad \log(2(L+1))\le\log(6T)\le X\le T,
\]

\[
\frac{2r}{3(L+2)^3}\ge\frac{2\Gamma^2}{81}\ge4T,
\quad \log(Q_rL(3r+1))\le\log(96r^3T)\le4X\le T.
\]

All comparisons follow from (3); in particular Γ²≥2^{100}T is far more than the constants require. Each exceptional probability is at most e^{-3T}. Hence

\[
\boxed{\Pr_r(G^c)\le2e^{-3T}\le e^{-2T}.}
\tag{12}
\]

No regularity of second differences or separate composition truncation is needed in G.

## 5. Reverse conditioning, fixed-size transfer, and period union

Fix a deterministic integer v≤exp(.7T). For 0≤s≤L let E_s impose all A ranges at depths s,...,L+1 and all divisibility tests `2a_j+1 | v` at depths j=s,...,L−1. The event E_{s+1} is measurable in the entire deeper-profile sigma-field and supplies both child ranges required in (6).

Inside the conditional kernel, drop the parent A_s restriction and apply (6). The tower property gives

\[
\Pr_*(E_s)\le b_s\Pr_*(E_{s+1}).
\]

The tail event E_L imposes only A_L and A_{L+1}, so its probability is at most one. Iteration and (8) show

\[
\Pr_*(\mathcal A\text{ and all tests})\le e^{-1.41T}.
\]

This is a succession of conditional estimates, not an independence assertion. In particular, the NB kernel is never conditioned on successful shallower tests, primitivity, or a_0=r. Imposing a_0=r only after the auxiliary estimate gives

\[
\Pr_r(\mathcal A\text{ and all tests})\le Q_r e^{-1.41T}.
\tag{13}
\]

On G, the established synchronous primitive-row theorem implies that all tested circumferences divide the actual physical g=f² period. Apply (13) to each fixed integer candidate and union-bound; there are at most exp(.7T) such candidates. Combining with (12),

\[
\Pr_r(v_{\rm actual}\le e^{.7T})
\le e^{-2T}+Q_r e^{-.71T}.
\]

Now `log Q_r<=3X<=T/200`, so the second term is at most e^{-.705T}. Since T≥200 log 2,

\[
\boxed{\Pr_r(v_{\rm actual}\le e^{.7T})\le e^{-.7T}.}
\tag{14}
\]

Primitivity supplies only the deterministic divisibility implication. It was not used to condition the full reverse law.

## 6. Exact word charge

The exact height-adaptive cycle construction has normalized overhead

\[
\mathbb E\frac{2h-1}{v_{\rm actual}}.
\]

The expectation can be taken under P_r: the uniform middle-state law corresponds to a uniform Dyck word together with a uniform root rotation, and height and physical period are rotation-invariant. The global period theorem gives `v_actual>=n=2r+1` without primitive assumptions, so `(2h-1)/v_actual<=1` everywhere.

For periods above exp(.7T), the integrand is at most n exp(-.7T). Split the expectation there and use (14):

\[
\frac{\nu(n)}{W(n)}-1
\le(n+1)e^{-.7T}\le e^{-.69T}.
\tag{15}
\]

The last step is finite: `log(n+1)<=2X<=T/100`. Thus both the polynomial collar prefactor and the addition of exceptional mass are paid explicitly.

## 7. Every dimension and the smaller explicit onset

Let

\[
k\ge k_*:=2^{131073}+1.
\]

Take n=k for odd k and n=k−1 for even k, and r=(n−1)/2. Then r≥2^{131072}, so

\[
\log r\ge131072\log2>65536.
\]

The established literal lift to the next even dimension doubles both length and central width. Therefore (15) gives the same normalized bound for k.

For an explicit comparison with the scale in (1), the present onset implies k≥2000 and log k≥1000. Hence

\[
\frac rk\ge\frac{k-2}{2k}\ge .499,
\quad \frac{\log r}{\log k}\ge1-\frac1{\log k}\ge.999.
\]

The logarithm comparison uses `.499>e^{-1}`. Exact rational inequalities give

\[
.499(.999)^2>.498>\left(\frac{20}{23}\right)^5;
\]

for the last one, `249*23^5=1602649407>1600000000=500*20^5`. Consequently

\[
\frac{T}{(k(\log k)^2)^{1/5}}>\frac{20}{23}.
\]

Finally `.69*(20/23)=3/5`. Substitute this strict finite comparison into (15) to obtain (1) on the entire stated integer domain. This is stronger than merely using the asymptotic relation r∼k/2, and does not retain an unspecified sufficiently-large condition.

The new argument establishes a sharper explicit asymptotic error for an actual general construction. It does not evaluate ν(k) exactly, reduce the verified k17 word by itself, or close the exact-equality goal.
