# Reverse-profile concentration and the explicit one-fifth error bound

**Later improvement:** the [logarithmic-gcd reverse test](/Users/amir.nuriyev/Documents/problem/HEIGHT_ADAPTIVE_LOG_GCD_RATE_20260908.md)
gains another factor of \(\log k\) in the exponent and removes the
local-profile smoothing premise. The proof and constants below remain
valid as an intermediate result.

2026-09-08. The reverse negative-binomial law, finite tails, transfer to
fixed size, full conditional smoothing, first-moment sieve and final word
charge have completed internal proof review and root reading. Internal
AI-agent review is not external mathematical review or formal verification.

For natural logarithms, the same deterministic height-adaptive construction
now has the fully specified bound
\[
 \boxed{\nu(k)\le W(k)\left[1+
 \exp\left(-2^{-330}\frac{k^{1/5}}{(\log k)^{3/5}}\right)\right],
 \quad k\ge\lceil\exp(\exp(2^{21}))\rceil.}              \tag{1}
\]
The constants are deliberately conservative. They are a sufficient finite
choice, not an optimized crossover dimension or an assertion about the
true rate of the construction.

Consequently, for every fixed \(0<\theta<1/5\), some \(c_\theta>0\)
gives \(\nu(k)\le W(k)(1+e^{-c_\theta k^\theta})\) eventually; in
particular \(\theta=1/6\) is available. This is stronger asymptotically
than the preceding one-seventh scale and all recorded powers of \(\log k\)
in the exponent. It is an upper-bound improvement, not exact attainment
of \(B(k)\).

The current independently verified finite word has 24,668 letters and
leaves a 355-position gap at dimension 17. The subsequently reported
24,660-word has not been supplied locally and is not promoted to a
verified bound by its pasted verification report.

## 1. Finite inputs and the unchanged construction

For odd \(n=2r+1\), the
[height-adaptive all-rank construction](/Users/amir.nuriyev/Documents/problem/HEIGHT_ADAPTIVE_PBBS_CONSTRUCTION_20260908.md)
has exact length and relative charge
\[
 N_r=W_r+\sum_{\mathcal C}(2h_{\mathcal C}-1),\qquad
 \frac{N_r-W_r}{W_r}=\mathbb E_A\frac{2h(A)-1}{v(A)},     \tag{2}
\]
where \(W_r=\binom{2r+1}{r}\) and \(A\) is uniform over physical
middle states. The finite strict-height corridor supplies every nonempty
target. Everywhere \(v\ge n\) and \(2h-1<n\), so the charge is below
one. No exterior word or residence repair is needed.

The retained [particle-return theorem](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_INVARIANT_GAP_ROW_PERIOD_DIVISIBILITY_INDEPENDENT_AUDIT_20260908.md)
implies that if the first \(L\) original gap rows are primitive then
each \(n_s=2a_s+1\), \(0\le s\le L\), divides the actual period.
The finite inverse-pruning fibre gives the exact profile weight
\[
 \mathcal W(\mathbf a)=\prod_{j\ge0}
                         \binom{a_j+a_{j+2}}{2a_{j+1}},  \tag{3}
\]
padded by zeros after extinction. The finite original-size concentration
is uniform in every depth:
\[
 \Pr_r(|a_j-r/(j+1)|>(4+x)\sqrt r)\le2e^{-x^2/6}.       \tag{4}
\]
These are the finite inputs. The older clock, renewal, overlap and
nonquantitative diagonal arguments are not used.

## 2. Exact reverse kernel under an auxiliary size mixture

Let \(\Pr_*(D)=4^{-|D|}/2\) on all finite Dyck words, including the
empty word. Conditioning on \(|D|=r\) gives exactly the original uniform
fixed-size law. After summing the profile coordinates before depth \(s\),
the remaining tail has mass
\[
 K_s x_s^{a_s}y_s^{a_{s+1}}
 \prod_{j\ge s}\binom{a_j+a_{j+2}}{2a_{j+1}},
 \quad x_s=(s+2)^{-2},\ y_s=(s+1)^2,\ K_s=\frac{s+1}{s+2}.
\]
For fixed deeper coordinates \(b=a_{s+1}\), \(d=a_{s+2}\), write
\(a_s=2b-d+t\). Normalizing the nonnegative sum
\(\sum_{t\ge0}\binom{2b+t}{2b}x_s^t=(1-x_s)^{-2b-1}\) proves
\[
 \Pr_*(\ell_s=t\mid\text{entire deeper profile})
 =\binom{2b+t}{2b}(1-x_s)^{2b+1}x_s^t,\qquad
 \mu_s=\frac{2b+1}{(s+1)(s+3)}.                         \tag{5}
\]
This includes the one-part kernel above the empty core. It is not
asserted to hold after conditioning on the original size \(a_0=r\).

For this negative-binomial law, with \(q\le1/4\), exponential Markov
bounds at \(\log(4/3)\) and \(-\log2\) give
\[
             \Pr(\ell_s<\mu_s/2\text{ or }\ell_s>2\mu_s)
                         \le2e^{-\mu_s/32}.             \tag{6}
\]
The [kernel and smoothing audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_REVERSE_PROFILE_NB_TAILS_AND_EXISTENCE_ONLY_SMOOTHING_INDEPENDENT_AUDIT_20260908.md)
derives the exact normalization and the rational bounds in both transforms.

## 3. Concentrate the second differences at their own scale

Put
\[
 X=\log r,\quad d=\log X\ge2^{20},\quad
 \Gamma=r^{1/5}X^{-3/5},\quad T=\Gamma X,\quad L=\lfloor T\rfloor.
                                                                    \tag{7}
\]
The exact identity \(r/T^3=\Gamma^2\) is central. Throughout this
domain, \(L+2\le2T\), \(L\ge T/2\), \(L\le r/2\), and
\(\Gamma^2\ge2^{50}X\).

Let \(\mathcal A\) require one-percent relative accuracy of every
\(a_j\), \(0\le j\le L+1\), and let \(\mathcal B\) require
\(\mu_s/2\le\ell_s\le2\mu_s\) for \(0\le s<L\).
The coarse relative tolerance in (4) gives
\[
 \Pr_r(\mathcal A^c)
 \le2(L+2)e^{-r/[240000(L+2)^2]}
 \le e^{-2^{-24}\Gamma^2}.                              \tag{8}
\]
For each \(s\), retain only the allowed \(\mathcal A\)-range on its
child size \(b\). Then \(\mu_s\ge r/(L+2)^3\ge\Gamma^2/8\).
Drop \(a_0=r\) and all other regularity restrictions before applying
the reverse kernel (5), and afterwards divide by
\[
 \Pr_*(a_0=r)=\operatorname{Cat}_r/(2\,4^r)
                  \ge1/[2(r+1)(2r+1)].
\]
The inverse normalizer is at most \(12r^2\). Thus
\[
 \Pr_r(\mathcal A\cap\mathcal B^c)
 \le24r^2L e^{-\Gamma^2/256}\le e^{-\Gamma^2/512}.         \tag{9}
\]
This explicitly pays for fixed-size conditioning. No negative-binomial
law is assumed under that conditioning.

On a fixed full profile in \(\mathcal A\cap\mathcal B\), each original
row remains a uniform weak composition, with
\(\min(p_s,\ell_s)\ge\Gamma^2/16\). The exact odd-row repetition
bound \(2p\exp[-(2\log2/3)\min(p,\ell)]\) gives total primitive-row
failure at most \(6r^2e^{-\Gamma^2/48}\le e^{-\Gamma^2/96}\).
For \(\mathcal G=\mathcal A\cap\mathcal B\) together with primitive
first \(L\) rows, the three errors therefore satisfy
\[
                         \Pr_r(\mathcal G^c)
                           \le e^{-2^{-26}\Gamma^2}.     \tag{10}
\]
Every guard and prefactor absorption is checked in the
[explicit fixed-size transfer audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_REVERSE_PROFILE_FIXED_SIZE_TRANSFER_EXPLICIT_DOMAIN_AUDIT_20260908.md).

## 4. Full conditional smoothing needs only one good completion

Free every third profile size in \([\lceil L/2\rceil,L-2]\), giving
at least \(L/8\) free depths, and expose every other coordinate. The
exact profile product (3) makes the free variables independent under
their full feasible conditional laws. For \(x=a_s\), that law has
weight
\[
 w(x)=\binom{A+x}{2b}\binom{b+c}{2x}\binom{x+D}{2c}
\]
on \(\max(2b-A,2c-D)\le x\le\lfloor(b+c)/2\rfloor\).

Suppose the exposed coordinates admit at least one completion in
\(\mathcal A\cap\mathcal B\). Its value \(x_*\) supplies three
adjacent second differences in \([m/4,8m]\), where
\(m=r/(s+1)^3\). This bounds the width of the entire conditional
support between \(3m/8\) and \(12m\), without truncating that support
to good completions. The exact adjacent ratio is decreasing, and puts
its mode a fixed fraction of \(m\) from each endpoint. Near the mode
the derivative of its log-ratio is \(O(1/m)\).

The finite proof, including a trivial small-\(m\) branch, gives
\[
 \boxed{\max_x\Pr_r(a_s=x\mid\text{exposed})
           \le\min(1,2^{20}/\sqrt m)\le2^{20}/\Gamma.}  \tag{11}
\]
The reference good completion is used only to bound the fixed weight.
The free outcomes are never conditioned to be good. This distinction
preserves their exact conditional independence.

## 5. A first-moment sieve with explicit constants

For any unimodal integer law with maximal atom \(\rho\), every residue
class has probability within \(2\rho\) of its reciprocal modulus.
For selected odd primes absent from a candidate period \(v\), put
\(Q=\sum_p\mathbf1_{p\mid2a_s+1}\), \(J=\#\{p\}\), and
\(\lambda=\sum_p1/p\). Then
\[
                          \mathbb EQ\ge\lambda-2J\rho.
\]
If every selected prime exceeds \(Y\) and \(Y^7>2r+1\), the full
feasible support \(0\le a_s\le r\) implies \(Q\le6\) pointwise.
Consequently
\[
 \Pr(2a_s+1\nmid v)\ge\Pr(Q>0)
                         \ge[\lambda-2J\rho]_+/6.       \tag{12}
\]
There is only a first-moment residue error \(J\rho\), rather than
the earlier pair error \(J^2\rho\).

Use the finite elementary estimates
\[
 \pi(y)\le16y/\log y,\qquad
 \left|\sum_{Y<p\le Z}1/p-\log(\log Z/\log Y)\right|
                                    \le32/\log Y.
\]
They follow from central binomial coefficients, the prime factorization
of \(N!\), and partial summation, as proved in the
[preceding prime audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_PROFILE_PRIME_SIEVE_AND_EXPLICIT_ONE_SEVENTH_RATE_INDEPENDENT_AUDIT_20260908.md).

Choose the fixed numerical parameters
\[
 B_0=2^{256},\qquad \delta=2^{-40},\qquad a=2^{-320},
 \qquad Y=\delta\Gamma/B_0,\quad Z=\delta\Gamma.          \tag{13}
\]
Put \(H=\log\Gamma\). On the domain in (7), \(X/6\le H\le X/5\),
\(\log Y\ge H/2\), and \(Y^7>2r+1\). The whole band has reciprocal
mass at least \(1/H\). If \(\log v\le a\Gamma\), its prime divisors
remove at most \(2aB_0/(\delta H)=2^{-23}/H\). Also
\(J\le32\delta\Gamma/H\); even the weaker
\(\rho\le2^{22}/\Gamma\) in (11) gives \(2J\rho\le2^{-12}/H\).
Hence the rejection in (12) is at least
\[
                              1/(12H)\ge1/(12X).        \tag{14}
\]
These bounds are uniform over every candidate and every exposed
configuration admitting a good completion.

## 6. Product, union and the actual finite word

For each fixed candidate, first apply (14) under the independent full
conditional laws. Drop the restrictions on the free coordinates being
good, and integrate over exposed configurations admitting a good
completion. Since \(L\ge\Gamma X/2\),
\[
 \Pr_r(\mathcal A\cap\mathcal B,
       2a_s+1\mid v\text{ at all free depths})
                            \le e^{-\Gamma/192}.
\]
On \(\mathcal G\), the actual period necessarily passes these tests,
by the fixed-label return lemma. Union over the at most
\(e^{a\Gamma}\) candidate integers and add (10):
\[
                       \Pr_r(v(A)\le e^{a\Gamma})
                            \le e^{-\Gamma/512}.         \tag{15}
\]
Primitivity is used only for the necessary divisibilities. The sieve
law is not conditioned on primitivity or on a small actual period.

In (2), short-period states cost at most (15), and all others cost at
most \(n e^{-a\Gamma}\). The explicit guard
\(\Gamma\ge2^{400}\log r\) absorbs this numerator and the sum:
\[
 \boxed{\frac{N_r-W_r}{W_r}\le e^{-2^{-322}\Gamma(r)},
                   \qquad\log\log r\ge2^{20}.}          \tag{16}
\]
In particular the finite odd-dimensional integer bound is
\(\nu(2r+1)\le W_r+\lfloor W_r e^{-2^{-322}\Gamma(r)}\rfloor\)
on this domain.

For \(k\ge\lceil e^{e^{2^{21}}}\rceil\), the odd source dimension is
\(n=k\) or \(k-1\), and \(r=(n-1)/2\ge k/4\). Thus
\(\log\log r\ge2^{20}\) and \(\Gamma(r)\ge\Gamma(k)/2\).
The even lift doubles word length and width together. Equation (16)
therefore permits coefficient \(2^{-323}\); the conservative
\(2^{-330}\) in (1) is valid with room to spare.

The [complete first-moment sieve and numerical audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_FIRST_MOMENT_PROFILE_SIEVE_EXPLICIT_ONE_FIFTH_RATE_AUDIT_20260908.md)
checks all constants, prime estimates, full-support bounds and both
parities. No prime number theorem or new dynamics assumption is used.

## 7. What this establishes

The same deterministic full-cube word has a stronger proved length
estimate on the linked finite inputs. Its relative excess is now bounded
on the \(k^{1/5}/(\log k)^{3/5}\) exponent scale. The supplied sandbox
checker and its reported enumeration totals were unavailable here; they
were not rerun or used as premises of this internal written-proof audit.

Using the exact lower bound, (1) also gives
\(0\le\nu(k)-B(k)\le W(k)e^{-2^{-330}\Gamma(k)}\) on its stated
domain. Because \(W(k)\) is exponential, the remaining absolute error
need not be zero. Exact equality remains open.
