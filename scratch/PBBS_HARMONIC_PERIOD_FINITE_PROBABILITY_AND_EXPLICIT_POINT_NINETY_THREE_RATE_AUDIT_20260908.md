# Harmonic period weighting: finite theorem and explicit 0.93 rate

2026-09-08. Independent pure-proof audit by `exact_b_finite_frontier`. The finite probability/conditioning argument, height moment, harmonic sum, and numerical domain all pass with one formulation correction: **the cutoff z in the displayed finite theorem is an integer at least two**. For a real cutoff, replace M/z by M/floor(z). All supplied applications already use integer z.

The local sharp residue/NB proof and the separate exact arithmetic certificate were read. This audit ran no mathematical program and made no construction search.

On the retained finite PBBS inputs, the same actual height-adaptive construction satisfies

\[
\boxed{\displaystyle
\frac{\nu(k)}{W(k)}\le1+
\exp\!\left[-\frac{93}{100}\bigl(k(\log k)^2\bigr)^{1/5}\right]
\quad(k\ge2^{131073}+1).}
\tag{1}
\]

The onset is explicit and applies to every integer dimension in that range. This remains a construction upper bound, not a proof of ν(k)=B(k). All logarithms are natural.

## 1. Exact construction charge and a finite first moment

For odd n=2r+1, write h and v for the normalized height and physical g=f² period of a uniform middle state. The proved height-adaptive word has exact normalized collar charge

\[
\epsilon_r:=\frac{N_n-W(n)}{W(n)}
=\mathbb E\frac{2h-1}{v},\qquad n\mid v,\qquad 2h-1<n.
\tag{2}
\]

The uniform middle-state/Dyck-root correspondence is a bijection with a uniform root rotation. Thus the expectation in (2) is the uniform fixed-size Dyck expectation for these rotation-invariant quantities. No additional cycle-length weighting is introduced in that probability law.

The [one-row moment audit](PBBS_ONE_ROW_PERIOD_MOMENTS_AND_EXPLICIT_N_THREE_HALVES_RATE_20260908.md), §3, proves by reflection and the range comparison that

\[
\mathbb E(2h-1)\le2t-3,\qquad t=2^{2r+1}/\binom{2r+1}{r}.
\]

The finite central-binomial bound

\[
c_r:=4^{-r}\binom{2r}{r}\ge\frac1{2\sqrt r}
\]

therefore yields

\[
\mathbb E(2h-1)
\le\frac{8(r+1)\sqrt r}{2r+1}-3
=4\sqrt r+\frac{4\sqrt r}{2r+1}-3\le4\sqrt r.
\tag{3}
\]

The last inequality holds for every r≥1; for example `2r+1>=2sqrt(r)` bounds the added fraction by two. The same central-binomial bound gives the sharper auxiliary fixed-size debit. Under `P*(D)=4^{-|D|}/2`,

\[
\Pr_*(a_0=r)=\frac{c_r}{2(r+1)},\qquad
\Pr_*(a_0=r)^{-1}\le Q_r:=4(r+1)\sqrt r.
\tag{4}
\]

See [the exact Boltzmann/profile audit](PBBS_AUXILIARY_BOLTZMANN_JOINT_PROFILE_ATOM_INDEPENDENT_AUDIT_20260908.md), §5. The expression Q_r is an upper bound for the inverse probability, not a claim of equality.

## 2. The finite parameters and local bound

Let r≥1, `0<delta<=1/6`, integer L≥1, integer z≥2, and real M≥0 satisfy

\[
\frac{\delta\sqrt r}{L+2}\ge4,
\qquad \frac{2(1-\delta)r}{(L+2)^3}\ge1000.
\tag{5}
\]

Define

\[
\begin{aligned}
E_A&=2(L+1)\exp\!\left[-\frac{(\delta\sqrt r/(L+2)-4)^2}{6}\right],\\
E_P&=Q_rL(3r+1)\exp\!\left[-\frac{4(1-\delta)r}{3(L+2)^3}\right],\\
A_z(M)&=\sum_{p\le z}\frac{\log p}{p-1}+\frac Mz,\\
\rho_s&=\frac{1.001(s+2)^{3/2}}{2\sqrt{\pi(1-\delta)r}},\\
y_s&=\frac{4(1-\delta)r}{s+2}-\frac{2(1+\delta)r}{s+3}+1,\\
b_s&=\min\!\left\{1,\frac{A_z(M)+M\rho_s}{\log y_s}\right\},\quad0\le s<L.
\end{aligned}
\tag{6}
\]

Every prime sum in this note is over primes. The denominator is positive: the coefficient of r in y_s−1 has numerator

\[
(2-6\delta)s+8-16\delta>0
\]

over the positive denominator `(s+2)(s+3)`.

The exact whole-deeper-profile reverse law under P* is

\[
a_s=2b-c+\operatorname{NB}(p=2b+1,q=(s+2)^{-2}),
\quad b=a_{s+1},\ c=a_{s+2}.
\]

When the child values obey the relative delta ranges, the entire parent support obeys `2a_s+1>=y_s`, and

\[
pq\ge\frac{2(1-\delta)r}{(s+2)^3}\ge1000.
\]

The finite sharp NB lemma thus bounds the maximal atom by rho_s. It is uniform over the full infinite support, without imposing a parent range. The sharp residue/NB argument is fully proved in
[the local sharp audit](PBBS_SHARP_UNIMODAL_NB_AND_DEPTH_INTEGRAL_INDEPENDENT_AUDIT_20260908.md), §§1–2.

For a deterministic integer u with `log u<=M`, its prime-power budget satisfies

\[
S(u):=\sum_{p^j\mid u}\frac{\log p}{p^j}\le A_z(M).
\tag{7}
\]

Indeed the primes p≤z contribute at most their full geometric sums. For p>z, integrality of z gives p−1≥z, so their total is at most `sum_{p|u,p>z}log(p)/z<=log(u)/z`. This is the precise reason for the integer-cutoff correction. With noninteger z, p−1≥z need not hold.

The sharp unimodal discrepancy gives

\[
\mathbb E_*\log\gcd(2a_s+1,u)\le S(u)+\rho_s\log u.
\]

On the divisibility event this logarithm is at least log y_s. Therefore

\[
\Pr_*\bigl(u\bmod(2a_s+1)=0\mid\text{entire deeper profile}\bigr)\le b_s.
\tag{8}
\]

The candidate u is fixed throughout each use of this conditional inequality. No random-period conditioning is introduced.

## 3. Exceptional profiles and the reverse product

Let A impose

\[
|a_j-r/(j+1)|\le\delta r/(j+1),\quad0\le j\le L+1,
\]

and let G additionally require primitivity of the first L original incoming-gap rows. The finite one-depth concentration estimate, at the nonnegative parameter in (5), gives

\[
\Pr_r(A^c)\le E_A.
\tag{9}
\]

Depth zero is fixed, leaving L+1 terms in the union bound.

Conditional on the entire child hierarchy under P*, the original row is an iid geometric vector of odd length p=2a_{s+1}+1. Its nonprimitive probability is at most `p exp(-2pq/3)`; when p=1 it is zero. On the child range,

\[
pq\ge\frac{2(1-\delta)r}{(L+2)^3},\qquad p\le3r+1.
\]

Drop fixed-size and irrelevant profile restrictions before using the full row kernel, then pay (4) once and sum over depths. This proves

\[
\Pr_r(A\text{ and a tested row is nonprimitive})\le E_P,
\quad \Pr_r(G^c)\le E_A+E_P.
\tag{10}
\]

The exact geometric-row and reverse-conditioning foundations are in
[the whole-row/tower audit](PBBS_LOG_GCD_WHOLE_ROW_LAW_AND_SUCCESSIVE_CONDITIONING_AUDIT_20260908.md).

For completeness, fix u≤e^M. At reverse step s, let E_s impose the A ranges at depths s,...,L+1 and all tests `2a_j+1 | u` at depths j=s,...,L−1. The event E_{s+1} is measurable in the entire deeper-profile sigma-field and supplies both child ranges needed in (8). Drop only the parent A_s restriction inside the kernel, obtaining

\[
\Pr_*(E_s)\le b_s\Pr_*(E_{s+1}).
\]

The terminal event has probability at most one. Iterate and then impose a_0=r to obtain

\[
\Pr_r(A\text{ and all tests})\le Q_r\prod_{s=0}^{L-1}b_s=:B.
\tag{11}
\]

This is successive conditioning, not independence across depths. Primitivity and fixed size are absent from the conditional NB laws. On G, the proved synchronous primitive-row theorem implies all these tests whenever the actual period is u. Consequently

\[
\Pr_r(G\text{ and }v=u)\le B\qquad(1\le u\le e^M).
\tag{12}
\]

## 4. Harmonic weighting removes the candidate-count loss

Equation (12) is a good-event point-mass bound. For the small-period contribution, retain the reciprocal period in the exact charge (2). Because n divides v, write v=nj. Then

\[
\begin{aligned}
\mathbb E\left[\frac{2h-1}{v};G,v\le e^M\right]
&\le\sum_{1\le j\le\lfloor e^M/n\rfloor}\frac1j\Pr_r(G,v=nj)\\
&\le B H_{\lfloor e^M/n\rfloor}\le B(1+M).
\end{aligned}
\tag{13}
\]

The empty sum is zero. For a nonempty sum, `H_N<=1+log N<=1+M`. Thus the number e^M of potential periods is not paid as an unweighted union bound.

On v>e^M, (3) bounds the contribution by `4sqrt(r)e^{-M}`. On G^c, (2) bounds the integrand by one. Combining (9)–(13) gives the corrected, fully finite theorem

\[
\boxed{\displaystyle
\epsilon_r\le4\sqrt r\,e^{-M}
+Q_r(1+M)\prod_{s=0}^{L-1}b_s+E_A+E_P.}
\tag{14}
\]

No independence of height and period, or of different rows, has been assumed. The large-period height expectation is unconditional; the small-period argument uses only `2h-1<n` and the point-mass bound.

## 5. A finite prime budget for the asymptotic parameters

Use the elementary Chebyshev bound theta(x)<3x, as proved and used in §4 of [the fresh-prime construction note](../HEIGHT_ADAPTIVE_FRESH_PRIME_RATE_20260908.md). For an integer m≥2,

\[
\psi(m)\le3m+3\sqrt m\log_2m<7m.
\]

The last inequality follows from `log m/sqrt m<=2/e`, `log2>2/3`, and `e>8/3`: the added coefficient is less than 27/8, and `3+27/8<7`.

The factorial identity and its floor error therefore give

\[
\sum_{p^a\le m}\frac{\log p}{p^a}\le\log m+7.
\]

For each prime p≤m, the geometric tail starting at its first power above m is at most 2/m. Summing its log p weights gives at most `2theta(m)/m<6`. Hence

\[
\sum_{p\le m}\frac{\log p}{p-1}\le\log m+13.
\tag{15}
\]

For z=floor M≥2, `M/z<1+1/z<=3/2`. Equation (15) proves the convenient finite bound

\[
A_z(M)\le\log(M+2)+15.
\tag{16}
\]

## 6. Explicit depth envelope at log r≥65536

Put

\[
X=\log r\ge65536,\quad D=\log X,\quad
\Gamma=r^{1/5}X^{-3/5},\quad T=\Gamma X,
\]

and choose

\[
\delta=.01,\qquad L=\lfloor25T/16\rfloor,\qquad
M=1.07T,\qquad z=\lfloor M\rfloor.
\tag{17}
\]

The sharper logarithm estimate

\[
D\le X/5000
\tag{18}
\]

holds throughout this domain. At X=65536, `16log2<11.2<65536/5000`, using log2<.7; thereafter the difference increases. The inequality log2<.7 follows already from the first four nonnegative terms of exp(.7), whose sum exceeds two.

The earlier scale proof remains valid with room to spare:

\[
\Gamma\ge2^{100}X,\quad T\ge2^{100}X^2,\quad
\Gamma^2\ge2^{100}T,\quad \log T<X/4.
\tag{19}
\]

In particular T≥4000, L+2≤2T<r, and both finite guards in (5) hold. The smallest pq is at least `1.98Gamma²/8>1000`.

For each tested s, `y_s>=r/(L+2)`, and

\[
\log y_s\ge .8X-.4D-\log2\ge .7999X.
\tag{20}
\]

Indeed `.4D<=X/12500`, and `log2<.7<=X/80000`; the sum of those two coefficients is less than .0001.

Equations (16)–(17) imply

\[
A_z(M)\le .2X+.4D+16.
\]

Since X≥64000, `.4D+16<=X/12500+X/4000=.00033X<.0007749X`. As `.251*.7999=.2007749`, the non-atom term in b_s is at most .251.

The atom coefficient is also finite, not a limiting claim. The existing Machin lower bound gives

\[
\pi>281476/89625>157/50,
\quad\sqrt{.99\pi}>1.763.
\]

Therefore

\[
\frac{1.001\cdot1.07}{2\cdot.7999\sqrt{.99\pi}}<.38,
\tag{21}
\]

because `.76*.7999*1.763=1.071770012>1.07107=1.001*1.07`. The weaker lower bound π>25/8 alone would not certify this new .38 constant; the stronger bound is explicitly used.

The identity `T^{5/2}=sqrt(r)X` now proves the uniform envelope

\[
b_s\le\frac{251}{1000}+\frac{19}{50}\left(\frac{s+2}{T}\right)^{3/2}.
\tag{22}
\]

## 7. The shifted finite product and four-term absorption

Let

\[
\phi(t)=-\log(.251+.38t^{3/2}),\qquad a=25/16.
\]

The [independent exact arithmetic certificate](HARMONIC_PERIOD_THREE_FINITE_ROWS_AND_INTEGRAL_RATIONAL_CERTIFICATE_20260908.md), §3, proves

\[
I:=\int_0^a\phi(t)\,dt>
\frac{1074181933864880728}{10^{18}}>1.074.
\tag{23}
\]

This is a finite rational right-endpoint/logarithmic-series lower sum; all 1,250 downward-rounded cell numerators are retained. No numerical quadrature premise is used.

The function is decreasing, φ(0)<2, and is positive up to a+.001. For the last assertion, `sqrt(a+.001)<1.251`, so

\[
.251+.38(a+.001)^{3/2}
<.251+.38(1.5635)(1.251)=.99425663<1.
\]

Since T≥4000, `(L+2)/T` lies between a and a+.001. Monotonicity, including the two-position shift, gives

\[
\sum_{s=0}^{L-1}\phi((s+2)/T)
\ge T\int_{2/T}^{(L+2)/T}\phi(t)\,dt
\ge TI-2\phi(0)>1.074T-4\ge1.073T.
\]

Consequently

\[
\prod_{s=0}^{L-1}b_s\le e^{-1.073T}.
\tag{24}
\]

The exceptional probabilities are bounded on the same entire finite domain. Since `sqrt(r)/(L+2)>=Gamma sqrt(T)/2>800`, the coarse exponent in E_A is at least `r/[240000(L+2)^2]>=TGamma²/960000>=4T`. Its log-prefactor is at most X≤T. The primitive exponent in E_P is at least `Gamma²/8>=4T`, while

\[
Q_rL(3r+1)\le64r^{5/2}T,
\quad\log(64r^{5/2}T)\le4X\le T.
\]

Thus each exception is at most e^{-3T}, and

\[
E_A+E_P\le e^{-2T}.
\tag{25}
\]

Substituting (24)–(25) in (14), the two remaining prefactors satisfy

\[
\log(4\sqrt r)\le X\le T/2000,
\quad\log(Q_r(1+M))\le3X\le T/2000.
\]

The three terms after combining the exceptions are therefore each at most e^{-1.0695T}. Since `log3<2<=T/2000`, their sum is at most e^{-1.069T}. We have proved

\[
\boxed{\epsilon_r\le e^{-1.069T}\qquad(\log r\ge65536).}
\tag{26}
\]

Every prefactor and finite Riemann error is charged explicitly; no remaining eventual qualification occurs in (26).

## 8. Both parities and the coefficient 0.93

For an integer k≥2^{131073}+1, take n=k if k is odd and n=k−1 if it is even. Then r=(n−1)/2≥2^{131072}, so `log r>=131072log2>65536`. The proved literal even lift doubles both word length and central width, preserving the normalized error.

On this range k≥10000 and log k≥10000. Hence

\[
r/k\ge .4999,\qquad \log r/\log k\ge .9999.
\]

The second estimate uses `.4999>e^{-1}`, so `log r>=log k-1`. Also

\[
.4999(.9999)^2>.499,
\quad\left(\frac{930}{1069}\right)^5
<\left(\frac{87}{100}\right)^5=.4984209207<.499.
\]

The first comparison inside the second chain is just `93000<93003`. Therefore

\[
\frac{T}{(k(\log k)^2)^{1/5}}>\frac{930}{1069}.
\]

Since `1.069*(930/1069)=.93`, equation (26) proves (1) for every dimension in its stated finite domain.

## 9. The supplied three finite numerical rows

The independent outward-rational execution recorded in
[the harmonic arithmetic audit](HARMONIC_PERIOD_THREE_FINITE_ROWS_AND_INTEGRAL_RATIONAL_CERTIFICATE_20260908.md)
uses delta=.1 and integer z=M. It checks every guard and each of the four terms in (14), proving:

| r | L | M | Certified epsilon_r bound |
|---:|---:|---:|---:|
| 10^12 | 1,100 | 790 | <10^{-330} |
| 10^14 | 3,500 | 2,250 | <10^{-950} |
| 10^16 | 10,200 | 6,150 | <10^{-2600} |

The present proof clears the probabilistic interface for those calculations. They apply at n=2r+1 and, by the exact lift, at n+1. The numerical audit evaluated only those fixed parameters, not a parameter search. Its full report and rounded integral cells are retained under `scratch/harmonic_period_rational_certificates_20260908/`.

The improvement is in estimating the same verified general construction. Neither (1), (14), nor the finite rows certify a new short word at k17 or settle the exact optimum there.
