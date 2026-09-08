# Height-adaptive profile sieve: stretched-exponential relative error

2026-09-08. Consolidated proof record. The local profile law, prime sieve,
original-law conditioning and word charge have completed independent
internal review and root reading. No external or formal verification is
claimed. The later reverse-profile argument improves the exponent scale
further; this proof remains a valid, fully quantified intermediate result.

For natural logarithms, put
\[
 F(k)=k^{1/7}\left(\frac{\log\log k}{\log k}\right)^{6/7}.
\]
The submitted theorem is that the same fixed height-adaptive construction
satisfies, for some absolute \(c>0\) and all sufficiently large \(k\),
\[
 \boxed{\nu(k)\le W(k)\{1+e^{-cF(k)}\}.}                 \tag{1}
\]
An explicit conservative choice is
\[
 \boxed{c=2^{-50},\qquad k\ge\lceil\exp(\exp(2^{21}))\rceil.}       \tag{1a}
\]
It implies \(\nu(k)\le W(k)(1+e^{-c_\theta k^\theta})\) eventually
for each fixed \(0<\theta<1/7\), including \(\theta=1/8\).
The absolute excess may still be large; exact equality with \(B(k)\)
does not follow.

This is asymptotically stronger than both
\(e^{-c(\log k)^{6/5}}\) and the later submitted
\(e^{-c\log k\log\log k}\) estimate. The latter improves the earlier
polynomial estimate but does not supersede (1). The finite word record,
independent of these asymptotic arguments, is
\(24313\le\nu(17)\le24668\).

## 1. Finite inputs and the exact charge

Let \(n=2r+1\), \(W_r=\binom{2r+1}{r}\). The already reviewed
[height-adaptive construction](/Users/amir.nuriyev/Documents/problem/HEIGHT_ADAPTIVE_PBBS_CONSTRUCTION_20260908.md)
has exact length
\[
 N_r=W_r+\sum_{\mathcal C}(2h_{\mathcal C}-1),\qquad
 \frac{N_r-W_r}{W_r}=\mathbb E_A\frac{2h(A)-1}{v(A)}.    \tag{2}
\]
Here the expectation is over uniform original middle states. The finite
global-maximum corridor and its strict-height refinement give full-cube
coverage. Every cycle satisfies \(n\mid v\), \(1\le h\le r\), so
the integrand is below one.

The [particle-return theorem](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_INVARIANT_GAP_ROW_PERIOD_DIVISIBILITY_INDEPENDENT_AUDIT_20260908.md)
proves that if the first \(L\) original gap rows are primitive then
\[
 \operatorname{lcm}_{0\le s<L}(n_sn_{s+1})\mid v,
 \qquad n_s=2a_s+1,quad a_s=r_s.                        \tag{3}
\]
In particular each \(n_0,\ldots,n_L\) divides \(v\). This is a
fixed-label return, not a return only modulo rotation.

The other retained inputs are the exact inverse-pruning fibre and the
finite original-profile concentration, uniform at every depth:
\[
 \Pr\{|a_s-r/(s+1)|>(4+x)\sqrt r\}\le2e^{-x^2/6}.
                                                                    \tag{4}
\]
No clock, residence-overlap estimate, renewal limit or asymptotic
coefficient-one theorem is a premise here.

## 2. Exact conditional profile law

Pad every profile by zeros after extinction, so \(a_0=r\) and
\(a_r=a_{r+1}=0\). Its feasible nonnegative integer coordinates satisfy
\(a_j-2a_{j+1}+a_{j+2}\ge0\). The inverse fibre gives exactly
\[
 \mathcal W(\mathbf a)=
 \prod_{j=0}^{r-1}\binom{a_j+a_{j+2}}{2a_{j+1}}          \tag{5}
\]
Dyck roots with that profile. Factors after extinction equal one;
the normalization is \(\operatorname{Cat}_r\).

For \(20\le L\le r\), take every third index in
\([\lceil L/2\rceil,L-2]\), forming a set \(J\) with
\(|J|\ge L/8\). Expose all \(a_j\) outside \(J\). A free coordinate
\(x=a_s\) affects precisely factors \(s-2,s-1,s\). With
\(A=a_{s-2},b=a_{s-1},c=a_{s+1},D=a_{s+2}\), its weight is
\[
 w_s(x)=\binom{A+x}{2b}\binom{b+c}{2x}\binom{x+D}{2c}.  \tag{6}
\]
Its entire support is
\[
 \max(2b-A,2c-D)\le x\le\lfloor(b+c)/2\rfloor.          \tag{7}
\]
The affected factors for distinct free coordinates are disjoint, and each
convexity constraint contains at most one free coordinate. The support
therefore factors as well as the weight. Conditional on the exposed
coordinates, the free variables are exactly independent, with laws
proportional to (6) on (7).

There is no omitted monotonicity or extinction condition: the padded
convex profile is nonincreasing, and the bounds in (7) already imply
\(c\le x\le b\). Conditioning these free values to be regular would
change their laws and is not done.

## 3. A finite bound on every conditional atom

Assume the exposed neighbors are within
\(\Delta=r/[10^4(L+3)^3]\) of their harmonic centers. Put
\(x_0=r/(s+1)\), \(m=r/(s+1)^3\). Since \(s\ge10\), the three
central slacks
\(A+x_0-2b\), \(x_0+D-2c\), \(b+c-2x_0\) all lie in
\([m,3m]\). The entire support has width between \(3m/2\) and
\(9m/2\).

The exact adjacent-weight ratio is
\[
 \frac{w_s(x+1)}{w_s(x)}=
 \frac{(A+x+1)(D+x+1)(b+c-2x)(b+c-2x-1)}
 {(A+x+1-2b)(D+x+1-2c)(2x+1)(2x+2)}.                   \tag{8}
\]
It decreases across the support, so the law is unimodal. Direct estimates
in (8) put every mode at least \(m/200\) from either integer endpoint
when \(m\ge400\). For \(m\ge2^{20}\), within distance \(\sqrt m\)
of a mode the derivative of the log-ratio has magnitude at most
\(4096/m\). At least \(\sqrt m/128\) neighboring weights are then
within a factor \(e^{1/4}\) of the maximum. The small-\(m\) case uses
the trivial atom bound one. Thus the full conditional law satisfies
\[
 \boxed{\max_x\Pr(a_s=x\mid E)
 \le\min(1,1024/\sqrt m)
 \le\min\left(1,1024\sqrt{(L+1)^3/r}\right).}           \tag{9}
\]
The [complete finite local-law proof](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_EVERY_THIRD_PROFILE_CONDITIONAL_LAW_AND_MAXIMAL_ATOM_INDEPENDENT_AUDIT_20260908.md)
checks both integer endpoints, the exact normalization, and all constants.

## 4. A missing-prime test for a prescribed period

If an integer-valued unimodal law has maximal atom \(\rho\), its total
variation as a sequence is \(2\rho\). Summation by parts against the
bounded partial sums of a residue-class indicator gives, for every
modulus \(d\) and residue \(b\),
\[
 \left|\Pr(X\equiv b\pmod d)-1/d\right|\le2\rho.        \tag{10}
\]
Fix an integer \(v\) and a collection \(\mathcal P_v\) of odd primes
not dividing \(v\). Let
\(Y_v(X)=\sum_{p\in\mathcal P_v}\mathbf1_{p\mid2X+1}\),
\(J_v=|\mathcal P_v|\), and \(\lambda_v=\sum_{p\in\mathcal P_v}1/p\).
Each prime condition and each distinct pair intersection is a single
residue class, by the Chinese remainder theorem. Therefore
\[
 \mathbb EY_v\ge\lambda_v-2J_v\rho,\qquad
 \mathbb EY_v^2\le\lambda_v+\lambda_v^2+2J_v^2\rho,
\]
and Cauchy–Schwarz gives
\[
 \Pr(Y_v>0)\ge
 \frac{[\lambda_v-2J_v\rho]_+^2}
 {\lambda_v+\lambda_v^2+2J_v^2\rho}.                    \tag{11}
\]
If \(2X+1\mid v\), then \(Y_v=0\). A positive lower bound in (11)
is consequently a rejection probability for that candidate period.

## 5. Scales, original regularity and the sieve

Put \(X=\log r\), \(D=\log X\), and choose
\[
 L=\left\lfloor(rX/D)^{1/7}\right\rfloor,
 \qquad F_r=r^{1/7}(D/X)^{6/7}.                         \tag{12}
\]
Then \(r/L^6\asymp F_r\) and \(LD/X\asymp F_r\).
Equation (4), at the tolerance \(\Delta\) above, gives
\(\Pr(\text{irregular})\le e^{-c_0F_r}\) eventually. On regular
profiles, for \(s<L\),
\[
 \ell_s=a_s-2a_{s+1}+a_{s+2}\ge r/(L+3)^3,\qquad
 p_s=2a_{s+1}+1\ge r/(L+3).
\]
The exact repeated-composition bound
\(\Pr(\text{nonprimitive}\mid\text{profile})
 \le2p\exp[-(2\log2/3)\min(p,\ell)]\)
makes the union of all first-\(L\) nonprimitive events exponentially
smaller than \(e^{-c_0F_r}\). Let \(G\) be regularity plus these
primitive rows. Thus
\[
                         \Pr(G^c)\le e^{-c_1F_r}.        \tag{13}
\]

For each candidate \(v\le e^{F_r/6400}\), take absent odd primes in
\[
 Y=r^{1/7}X^{-4/5}<p\le Z=r^{1/7}X^{-7/10}.             \tag{14}
\]
The elementary reciprocal-prime estimate gives
\[
 \sum_{Y<p\le Z}1/p=
 \log\frac{\log Z}{\log Y}+O(1/\log Y)
 =\left(\frac7{10}+o(1)\right)D/X.
\]
It follows from the central-binomial prime bound, the prime-factorization
identity for \(N!\), and partial summation; no prime number theorem or
short-interval prime theorem is required.

The prime divisors of a candidate \(v\) remove mass at most
\[
 \frac{\log v}{Y\log Y}
 =O(D^{6/7}X^{-37/35})=o(D/X).
\]
The maximal atom in (9) is
\(\rho\le C r^{-2/7}(X/D)^{3/14}\), and \(J_v\le Z\) gives
\[
 J_v^2\rho\le C X^{-83/70}D^{-3/14}=o(D/X).
\]
Thus (11) implies, uniformly in regular exposed data and every candidate,
\[
                    \Pr(2a_s+1\mid v\mid E)
                       \le1-D/(100X).                  \tag{15}
\]

## 6. Correct conditioning and the union over periods

For a fixed \(v\), first condition only on exposed coordinates. If they
are regular, drop the regularity restrictions on the free coordinates
when taking an upper bound. Their full conditional laws are independent,
so (15) multiplies. Integrating afterwards gives
\[
 \Pr(\text{regular and }2a_s+1\mid v\ \forall s\in J)
 \le(1-D/(100X))^{|J|}\le e^{-F_r/1600}.                 \tag{16}
\]
The sieve is applied under the original profile law, never under the law
conditioned on primitive rows. Primitivity is used only for the
deterministic inclusion supplied by (3): on \(G\), an actual period
\(v\) must pass every divisibility test in (16).

There are at most \(e^{F_r/6400}\) candidate integers. Union-bounding
them and adding (13) yields
\[
                   \Pr(v(A)\le e^{F_r/6400})\le e^{-c_2F_r}.
                                                                    \tag{17}
\]
Use (17) in (2). Long-period states cost at most
\(n e^{-F_r/6400}\); the others cost at most their probability. Since
\(F_r/\log r\to\infty\),
\[
                    (N_r-W_r)/W_r\le e^{-c_3F_r}         \tag{18}
\]
eventually. Replacing \(r\) by the odd dimension changes the rate scale
by a bounded factor. The exact even lift doubles the width and word
length together. Decreasing \(c_3\) proves (1) in both parities.

For every fixed \(0<\theta<1/7\), \(F(k)/k^\theta\to\infty\), which
proves the stretched-exponential corollaries. Also
\(0\le\nu(k)-B(k)\le W(k)e^{-cF(k)}\), by the handoff's exact lower
bound and \(B(k)\ge W(k)\).

## 7. Explicit constants and verification scope

The [prime-sieve audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_PROFILE_PRIME_SIEVE_AND_EXPLICIT_ONE_SEVENTH_RATE_INDEPENDENT_AUDIT_20260908.md)
proves \(\pi(y)\le16y/\log y\) and
\[
 \left|\sum_{Y<p\le Z}\frac1p-
             \log\frac{\log Z}{\log Y}\right|\le32/\log Y.
\]
For \(D=\log\log r\ge2^{20}\), these make the rejection in (15)
at least \(D/(8X)\), so the weaker constant 100 used above is valid
throughout that numerical domain.

The [complete original-law and charge audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_PROFILE_SIEVE_ORIGINAL_LAW_AND_CHARGE_BOOKKEEPING_AUDIT_20260908.md)
checks \(F_r\ge2^{50}\log r\) there, bounds irregularity by
\(e^{-2^{-39}F_r}\), the combined bad event by \(e^{-2^{-40}F_r}\),
the short-period probability by \(e^{-2^{-41}F_r}\), and the word charge
by \(e^{-2^{-42}F_r}\). For both parities and
\(k\ge\lceil e^{e^{2^{21}}}\rceil\), the odd source has
\(\log\log r\ge2^{20}\) and \(F_r\ge F(k)/4\). Thus even the
coefficient \(2^{-44}\) is available; (1a) retains a conservative margin.

This record concerns written finite identities and analytic estimates.
The user's attached sandbox checker and its reported enumeration totals
were not available here and have not been rerun. The independent local
law audit supplies explicit constant 1024; the final constant and sufficient
threshold are specified in (1a). The constants are conservative and are
not claimed optimal. The computations reported in the user's sandbox
package remain separate from this written proof review.

The independent finite upper bound is established by the actual
[24,668-letter word and complete checks](/Users/amir.nuriyev/Documents/problem/K17_UPPER24668_VERIFIED_20260908.md).
It does not rely on (1), and verifying that word does not certify the
general argument. Exact equality with \(B(k)\) remains open.
