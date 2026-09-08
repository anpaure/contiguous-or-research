# Fractional LCM moments and a squared-logarithm error estimate

2026-09-08. Internal proof record of the user's additional arithmetic
route. The finite Euler-product lemma, profile application and optimization
have completed independent review and root reading. This is not external
review or formal verification.

For the fixed height-adaptive construction, the claimed and internally
checked asymptotic deduction is
\[
 \boxed{\nu(k)\le W(k)(1+e^{-c(\log k)^2})
 \quad\text{for every fixed }0<c<\frac1{6144e^2},}
                                                                    \tag{1}
\]
for all sufficiently large \(k\). In particular \(c=1/65536\) has a
strict margin. This route does not specify a numerical starting dimension.

Equation (1) improves the preceding joint-profile
\(e^{-c\log k\log\log k}\) estimate and the older
\(e^{-c(\log k)^{6/5}}\) estimate. It is asymptotically weaker than
the separately reviewed one-seventh and one-fifth stretched-exponential
rates. It is therefore retained as an alternative arithmetic proof, not
as the strongest current upper bound.

The user's accompanying claim \(\nu(17)\le24660\) awaits its actual
word body. Only a sandbox link was supplied; the expected local file
`/Users/amir.nuriyev/Downloads/k17_upper24660.word` was absent when checked.
The independently verified finite record remains
\(24313\le\nu(17)\le24668\), with gap 355. The claimed gap 347 is not
yet an independently checked result.

## 1. Uniform finite inputs

For odd \(n=2r+1\), the height-adaptive all-rank word has
\[
 \epsilon_n=(N_n-W(n))/W(n)=\mathbb E[(2h-1)/v],
 \qquad v\ge n,\quad2h-1<n.
\]
On the event that the first \(L\) original gap rows are primitive,
every reduced circumference \(n_1,\ldots,n_L\) divides \(v\).
The [joint-profile and finite error record](/Users/amir.nuriyev/Documents/problem/HEIGHT_ADAPTIVE_MULTILEVEL_PROFILE_BOUND_20260908.md)
gives, for each good profile, probability at most \(A_Ln^{-L/2}\), where
\[
 A_L=16(L+1)3^L((L+1)!)^2.
\]
For odd \(n\ge4096(L+3)^6\), the probability that either the required
size conditions or primitivity fails is at most
\[
 \delta_{n,L}=2(L+1)n(n+1)e^{-n/[2048(L+3)^6]}
                       +Ln\,2^{-n/[6(L+3)^3]}.          \tag{2}
\]
These estimates are uniform in \(L\) and under the original fixed-size
law. They do not assert independence of pruning sizes.

## 2. A finite uniform fractional-LCM theorem

For integer \(L\ge2^{16}\), let
\[
 \frac13\le\beta\le\frac12,\quad0<\eta\le\frac16,
 \quad\alpha=1+\eta-\beta,\quad
 Y=\left(\frac{2L}{\log L}\right)^{1/\beta}.
\]
Then \(1/2<\alpha\le5/6<1\). For every positive integer \(M\),
\[
 \boxed{\sum_{1\le u_1,\ldots,u_L\le M}
 \operatorname{lcm}(u_1,\ldots,u_L)^{-\alpha}
 \le M^{\beta L}(1+\eta^{-1})^L e^{96Y}.}               \tag{3}
\]

Here is the full accounting. Weight the infinite tuple sum by
\((u_1\cdots u_L)^{-\beta}\). Its nonnegative Euler factor is
\[
 F_p=\sum_{e_1,\ldots,e_L\ge0}
             p^{-\alpha\max e_i-\beta\sum e_i}.
\]
The elementary dyadic central-binomial prime bound gives
\(\pi(y)\le8y/\log y\). Partial summation then yields
\[
 \sum_{p\le Y}p^{-\beta}\le48Y^{1-\beta}/\log Y,
 \qquad \sum_{p>Y}p^{-a}\le32Y^{1-a}/\log Y\quad(a\ge4/3).
\]
On \(L\ge2^{16}\), \(\log Y\ge(3/2)\log L\) and
\(Y\ge L^{5/3}\). Dropping the maximum factor for the small primes,
\(\log F_p\le5Lp^{-\beta}\), so their total cost is at most \(80Y\).

For \(p>Y\), put \(z=p^{-\beta}\), \(w=p^{-\alpha}\),
\(u=z/(1-z)\). Then \(z\le\log L/(2L)\le1/4\) and
\(Lu\le(2/3)\log L\). The exactly one-positive-coordinate contribution
is
\(Lp^{-1-\eta}/(1-p^{-1-\eta})\). For support size at least two,
retain \(w\), giving
\[
 w\sum_{j=2}^L\binom Lj u^j
 \le\tfrac12w(Lu)^2e^{Lu}
 \le L^{8/3}p^{-1-\eta-\beta}.
\]
It follows that
\[
 F_p\le(1-p^{-1-\eta})^{-L}
                   (1+L^{8/3}p^{-1-\eta-\beta}).
\]
The prime-tail estimate bounds the logarithm of the correction product
by \((32/3)Y\). Thus the entire weighted series is at most
\(\zeta(1+\eta)^Le^{(272/3)Y}\le(1+\eta^{-1})^Le^{96Y}\).
These estimates prove convergence; nonnegative finite-prime products
justify passage to the full series. On tuples \(u_i\le M\), remove
the weights at cost at most \(M^{\beta L}\), proving (3).

The [complete finite Euler-product audit](/Users/amir.nuriyev/Documents/problem/scratch/FRACTIONAL_LCM_MOMENT_EXPLICIT_EULER_PRODUCT_INDEPENDENT_AUDIT_20260908.md)
checks every prime estimate, cutoff guard, coefficient and convergence step.
No coprimality assumption or prime-distribution asymptotic is used.

## 3. Apply the moment to original profile probabilities

On the good event, \(m=\operatorname{lcm}(n_1,\ldots,n_L)\) divides
\(v\). Since \(m\ge1\) and \(0<\alpha<1\),
\[
                         (2h-1)/v\le n/m\le n/m^\alpha.
\]
Every good size tuple has probability at most \(A_Ln^{-L/2}\). Sum
over those tuples, then enlarge the nonnegative sum to all ordered tuples
between 1 and \(n\). Equation (3), with \(M=n\), gives
\[
 \boxed{\epsilon_n\le\delta_{n,L}+
 nA_Ln^{-(1/2-\beta)L}(1+\eta^{-1})^L
 \exp\left[96\left(\frac{2L}{\log L}\right)^{1/\beta}\right].}
                                                                    \tag{4}
\]
Its finite domain is \(L\ge2^{16}\), \(n\ge4096(L+3)^6\), and
the parameter ranges above. All constants in this inequality are explicit.
There is no conditioning of the joint law on primitivity: the probability
of a good tuple is simply bounded by that of the tuple itself. The bad
event costs at most (2), because the original integrand is below one.

## 4. Optimize with growing \(L\)

Put \(x=\log n\), \(y=\log x\), and choose
\[
 \beta=\frac12-\frac1{2y},\qquad \eta=1/x,
 \qquad L=\lfloor\lambda xy\rfloor
\]
for a fixed \(\lambda>0\). All finite hypotheses of (4) eventually
hold. The logarithm of its second term is
\[
 x+\log A_L-\frac{Lx}{2y}+L\log(1+x)
             +96(2L/\log L)^{1/\beta}.                 \tag{5}
\]
The first, second and fourth terms total \(O(xy^2)=o(x^2)\).
Also \(1/\beta=2+2/(y-1)\), and
\[
 (2L/\log L)^{1/\beta}=(4\lambda^2e^2+o(1))x^2.
\]
The slowly varying exponent supplies the factor \(e^2\); it cannot
be discarded. Thus (5) is
\[
 -\{\lambda/2-384e^2\lambda^2+o(1)\}x^2.
\]
The maximum coefficient is \(1/(6144e^2)\), attained at
\(\lambda=1/(1536e^2)\). Alternatively, the rational choice
\(\lambda=1/8192\) gives
\[
 \frac{32-3e^2}{524288}>\frac1{65536},
\]
using \(e^2<8\). The failure term (2) is exponentially smaller on
the scale \(n/O((\log n\log\log n)^6)\). This proves (1) in odd
dimensions. For even dimensions the exact doubling lift preserves the
normalized length; an intermediate coefficient between the requested
\(c\) and the strict limiting margin absorbs \(\log(k-1)\sim\log k\).

## 5. Evidence and remaining scope

The [independent profile-application and optimization audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_FRACTIONAL_LCM_PROFILE_APPLICATION_AND_LOG_SQUARED_RATE_AUDIT_20260908.md)
checks the original-law probability sum, all finite parameter ranges,
the varying exponent, the strict numerical margin and both parities.

The written proof is reviewed on the retained finite PBBS support and
profile inputs. The user's sandbox checker and its reported test counts
were not available and have not been rerun. The public paper
[On the reciprocal sum of lcm of k-tuples](https://arxiv.org/abs/2106.01638)
is relevant background on reciprocal LCM sums; none of its theorems is
needed for the uniform finite proof (3).

The new 24,660 upper bound is recorded only as awaiting the actual word.
Once its nonzero mask list is available it can be checked independently
of this arithmetic. Until then the complete verified word remains
[the 24,668-letter certificate](/Users/amir.nuriyev/Documents/problem/K17_UPPER24668_VERIFIED_20260908.md).

Even \(W(k)e^{-c(\log k)^2}\) can be exponentially large in \(k\).
Neither this estimate nor the stronger stretched-exponential estimates
proves exact equality \(\nu(k)=B(k)\).
