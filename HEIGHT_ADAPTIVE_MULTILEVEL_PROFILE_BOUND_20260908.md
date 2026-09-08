# Multilevel joint-profile estimate and the 24,668-letter certificate

2026-09-08. Consolidation of the user's alternative period argument.
The joint-profile bound, complete finite error, upper-period identity and
divisor-average deduction have completed internal proof review and root reading.
Internal review is not external mathematical review or formal verification.

The claimed general rate is
\[
 \nu(k)\le W(k)\{1+e^{-c\log k\log\log k}\}
 \quad\text{for every fixed }0<c<1/(2\log2),             \tag{1}
\]
eventually. It improves the one-row \(k^{-3/2}\) estimate. It is
asymptotically weaker than the separately reviewed
\(e^{-c(\log k)^{6/5}}\) bound and the subsequent profile-sieve rates.
Its value is a different finite joint-profile estimate and a fully
specified finite bound, rather than a new strongest asymptotic rate.

The separately supplied literal word has been independently verified:
\[
                        24313\le\nu(17)\le24668.
\]
See [the complete word certificate](/Users/amir.nuriyev/Documents/problem/K17_UPPER24668_VERIFIED_20260908.md).
Its 355-position gap does not depend on any general period estimate.

## 1. The same finite construction and multilevel divisibility

For odd \(n=2r+1\), the height-adaptive all-rank word has relative excess
\[
 \epsilon_n=\frac{N_n-W(n)}{W(n)}
           =\mathbb E\frac{2h(A)-1}{v(A)}.               \tag{2}
\]
The expectation is under uniform original middle states, and the summand
is below one. The finite corridor supplies coverage; the word is unchanged.

If the first \(L\) original incoming-gap rows are primitive, the
[persistent-label return theorem](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_INVARIANT_GAP_ROW_PERIOD_DIVISIBILITY_INDEPENDENT_AUDIT_20260908.md)
gives
\[
 \operatorname{lcm}_{0\le s<L}(n_sn_{s+1})\mid v,
 \quad n_s=2r_s+1.                                     \tag{3}
\]
Each \(n_s\) divides \(v\). Shared factors are retained; no full
product of the sizes is asserted to divide the period.

## 2. An auxiliary measure gives a fixed-size joint atom bound

Let \(\Pr_0(D)=4^{-|D|}/2\) on all finite Dyck words. Conditional on
\(|D|=r\), this is the required uniform size-\(r\) law. Its depth-\(s\)
pruned word has exact mass
\[
 \Pr_s(E)=x_s^{|E|}y_s^{\operatorname{pk}(E)}/Z_s,
 \quad x_s=\frac{(s+1)^2}{(s+2)^2},\quad
 y_s=\frac1{(s+1)^2},\quad Z_s=\frac{s+2}{s+1}.
\]
For a child of size \(t\) with \(b\) peaks, inverse pruning gives
\[
 \sum_{\partial D=E}x^{|D|}y^{\operatorname{pk}(D)}
  =\frac1{1-xy}\left(\frac{x}{(1-xy)^2}\right)^t(xy)^b.
\]
This proves the exact marginal laws and normalization inductively.
Conditional on the complete child, the parent surplus is negative binomial
with \(N=2t+1\) parts and parameter \(q=(s+2)^{-2}\). Fourier inversion
gives the uniform atom bound
\[
                       \max_m\Pr(\ell_s=m\mid E)
                       \le\frac{s+2}{\sqrt{2t+1}}.       \tag{4}
\]

The Narayana count gives an exact core-size identity. Put \(j=s+1\)
and let \(B\sim\operatorname{Bin}(t,1/(j+1))\). Then
\[
 \Pr_s(|E|=t)=\frac1{t(j+1)}
       \sum_{b=1}^t\Pr(B=b)\Pr(B=b-1)
 \le\frac1{\sqrt{2j}\,t^{3/2}}\quad(t\ge1).             \tag{5}
\]
The inequality follows from the elementary binomial atom bound
\(\max_b\Pr(B=b)\le[2tp(1-p)]^{-1/2}\). The empty core is handled
by its exact mass and is not used in the positive-size hypothesis below.

Suppose \(a_j\ge r/[2(j+1)]\) for \(1\le j\le L\). Start with the
depth-\(L\) core, then prescribe the parent sizes successively. Applying
(4) uniformly to each complete child and (5) once gives
\[
 \Pr_0(r_0=r,r_1=a_1,\ldots,r_L=a_L)
 \le2(L+1)((L+1)!)^{3/2}r^{-(L+3)/2}.
\]
Divide by the actual conditioning probability
\(\Pr_0(r_0=r)=\operatorname{Cat}_r/(2\,4^r)\ge1/(8r^{3/2})\).
Thus the original fixed-size law satisfies
\[
 \boxed{\Pr_r(r_1=a_1,\ldots,r_L=a_L)
 \le16(L+1)((L+1)!)^{3/2}r^{-L/2}
 \le C_Lr^{-L/2},\quad
 C_L=16(L+1)((L+1)!)^2.}                                \tag{6}
\]
The [complete independent joint-profile audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_AUXILIARY_BOLTZMANN_JOINT_PROFILE_ATOM_INDEPENDENT_AUDIT_20260908.md)
derives both Fourier bounds and handles all boundary cases. No
independence of the profile sizes is asserted; each conditional atom is
bounded uniformly and the original-size conditioning is explicitly paid.

## 3. Finite good-profile and primitivity error

For odd \(n\) and integer \(L\ge1\), assume
\(n\ge4096(L+3)^6\). Define
\[
 \delta_{n,L}=2(L+1)n(n+1)e^{-n/[2048(L+3)^6]}
               +Ln\,2^{-n/[6(L+3)^3]}.                 \tag{7}
\]
The finite original-bit census gives
\(0\le\mathbb EN_j-n/(j+1)\le2\sqrt n\), and changing one original
bit changes any recording size by at most two. Put
\(\tau=n/[16(L+3)^3]\). On the displayed domain,
\(2\sqrt n\le\tau/2\), so bounded differences at \(\tau/2\), a union
over \(j=1,\ldots,L+1\), and root-conditioning probability at least
\(1/[n(n+1)]\) give the first error in (7).

Outside it, \(|n_j-n/(j+1)|\le\tau\). The relevant second differences
satisfy
\[
 \ell_s=(n_s-2n_{s+1}+n_{s+2})/2
       \ge n/(L+3)^3-2\tau\ge n/[2(L+3)^3].
\]
Also \(a_j=(n_j-1)/2\ge r/[2(j+1)]\). The exact composition repetition
bound \(p\binom{p+\ell-1}{p-1}^{-2/3}\), together with
\(\min(\ell,p-1)\ge n/[4(L+3)^3]\), gives the second error in (7)
after a union over the \(L\) rows. Thus, with probability at least
\(1-\delta_{n,L}\), all size hypotheses of (6) hold and the first
\(L\) rows are primitive.

## 4. Average divisor counts instead of multiplying sizes

Let \(d(m)\) denote the number of positive divisors of \(m\), and put
\(A_L=16(L+1)3^L((L+1)!)^2\). For a prescribed period \(v\), the
good event allows at most \(d(v)^L\) possible tuples of sizes
\(n_1,\ldots,n_L\). Since \(r\ge n/3\), (6) gives the convenient
bound
\[
 \Pr(\text{good},v(A)=v)\le A_Ln^{-L/2}d(v)^L,
 \qquad n\mid v.                                      \tag{8}
\]
This counts all tuples, even infeasible ones, which is safe for an upper
bound. The good event is a subset of the corresponding profile event;
there is no division by the probability of primitivity.

The elementary divisor inequality needed to sum (8) is
\[
                 \sum_{u\le Y}\frac{d(u)^L}{u}
                 \le(1+\log Y)^{2^L}\quad(Y\ge1).       \tag{9}
\]
For a prime exponent \(e\), encode a tuple of \(L\) divisor exponents
by the subset of divisors containing each of the levels \(1,\ldots,e\).
The counts assigned to the \(2^L\) subsets sum to \(e\) and determine
the original exponent tuple. This injects \(L\)-tuples of divisors of
\(u\) into ordered \(2^L\)-factor factorizations of \(u\). Summing
their reciprocal products with product at most \(Y\) is at most
\((\sum_{a\le Y}1/a)^{2^L}\), proving (9).

In (2), bad states cost at most \(\delta_{n,L}\). Periods larger than
\(T=n^{L+1}\) cost at most \(n/T=n^{-L}\). For smaller periods write
\(v=nu\), so the numerator bound \(2h-1<n\) leaves weight at most
\(1/u\). Using (8), \(d(nu)\le d(n)d(u)\), and (9), we obtain
\[
 \boxed{\epsilon_n\le\delta_{n,L}+n^{-L}
 +A_Ln^{-L/2}d(n)^L(1+L\log n)^{2^L}.}                 \tag{10}
\]
The [finite regularity and primitivity audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_FINITE_MULTILEVEL_REGULARITY_AND_PRIMITIVITY_DELTA_AUDIT_20260908.md)
proves every constant and domain used in (7). All constants in (10) are
specified. There is no extra factor \(n\) in the
last term, since it cancels when \(v=nu\).

## 5. The growing-depth consequence

Let \(X=\log n\), \(D=\log X\), and take
\[
 L=\left\lfloor\frac{D-2\log D}{\log2}\right\rfloor.
\]
Eventually \(L\ge1\), \(L\sim D/\log2\),
\(2^L\le X/D^2\), and the finite domain of (10) holds.

The standard elementary bound \(\log d(n)=o(\log n)\) is sufficient
here. One proof fixes \(\eta>0\): for all primes above
\(2^{1/\eta}\), \(e+1\le2^e\le p^{\eta e}\); for the finitely many
smaller primes, \(e+1\le C_{p,\eta}p^{\eta e}\). Multiplication gives
\(d(n)\le C_\eta n^\eta\), for every fixed \(\eta>0\).

The logarithm of the last term in (10) is therefore
\[
 \log A_L-\tfrac12 LX+L\log d(n)
             +2^L\log(1+LX)
 =-\left(\frac1{2\log2}+o(1)\right)XD.
\]
Indeed \(\log A_L=O(L\log L)\), the divisor term is \(o(LX)\), and
the final logarithmic factor is \(O(X/D)\). The term \(n^{-L}\) has
twice the leading decay exponent, while (7) decays on the much larger
scale \(n/O(D^6)\). Absorbing their sum proves (1) for odd dimensions.
The exact even lift preserves normalized length; choosing an intermediate
constant between \(c\) and \(1/(2\log2)\) absorbs the change from
\(n=k-1\) to \(k\). Thus (1) holds in both parities.

For every fixed \(A>0\), \(c\log\log k>A\) eventually. Hence this
one fixed construction has \(\nu(k)=W(k)(1+O_A(k^{-A}))\), while its
absolute excess is not forced to vanish.

## 6. A complementary exact upper-period theorem

If the full profile ends at \(n_h=1\), put
\(M=\operatorname{lcm}_{0\le s<h}(n_sn_{s+1})\). Then
\[
                              f^M(A)=A.
\]
At any return time \(T\) of a \(p\)-site child, let \(C_i\) count
selections of site \(i\), and let \(E_i\) be the outgoing equality-edge
indicator. The exact update gives \(\Delta E_i=C_i-C_{i+1}\). A return
therefore forces every count to equal \(T/p\). For \(p=1\) the same
count follows directly. Thus, if \(np\mid T\), every parent particle
advances a multiple of its circumference and returns with its recorded
bit. Induct upward from the fixed one-site bottom to prove the display.

Every \(n_s\) is odd, so \(M\) is odd. The minimal physical \(f\)-period
is odd and equals its \(f^2\)-period. If every gap row is primitive,
the lower divisibility (3) forces that period to be exactly \(M\).
The [full upper-period audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_FULL_PROFILE_UPPER_PERIOD_AND_PRIMITIVE_EQUALITY_AUDIT_20260908.md)
checks the physical labels, same-time reduction and terminal case. This
upper-period statement is not needed to prove (10).

## 7. Records and limits

The user's sandbox verification package and rewrite sources were not
supplied here; the stated enumeration totals have not been reproduced.
The actual 24,668-letter file was supplied and independently verified in
full. The two claims have separate evidence and dependency chains.

The auxiliary joint-profile lemma and the divisor argument give a reviewed
alternative route with the checked finite inputs in Section 3. The
stronger profile-sieve bounds remain the leading asymptotic records.
No exact all-dimensional construction of length \(B(k)\) is established.
