# Logarithmic-gcd reverse tests: the explicit endpoint one-fifth bound

2026-09-08. The logarithmic-gcd lemma, reverse full-row law, successive
conditioning and finite probability accounting have completed internal
proof review; the completed audit files are linked below. This is a
deduction on the retained finite construction, particle-return, pruning
fibre and concentration inputs. Internal AI-agent review is not external
mathematical review or formal verification.

The completed [whole-row and successive-conditioning audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_LOG_GCD_WHOLE_ROW_LAW_AND_SUCCESSIVE_CONDITIONING_AUDIT_20260908.md)
and [finite probability, collar and parity audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_LOG_GCD_REVERSE_PRODUCT_AND_EXPLICIT_ENDPOINT_RATE_AUDIT_20260908.md)
have both been read in full by root. Together with the logarithmic-gcd
audit linked in Section 3, they check every interface in this record.

For natural logarithms, the same fixed height-adaptive construction obeys
\[
 \boxed{\nu(k)\le W(k)\left[1+
 \exp\left(-\frac{(k(\log k)^2)^{1/5}}{128}\right)\right],
 \qquad k\ge\lceil\exp(\exp(2^{21}))\rceil.}             \tag{1}
\]
The user's eventual coefficient \(1/128\) is retained. The explicit
starting dimension is an additional conservative consequence of the
finite audits, not an optimized threshold.

On this same domain, \((\log k)^{2/5}\ge128\), so
\[
 \boxed{\nu(k)\le W(k)(1+e^{-k^{1/5}}),
 \qquad k\ge\lceil\exp(\exp(2^{21}))\rceil.}             \tag{2}
\]
This improves the preceding exponent \(k^{1/5}/(\log k)^{3/5}\) by
a full factor \(\log k\). The construction is unchanged. No new
finite word at dimension 17 is supplied by this argument; the verified
finite interval remains \(24313\le\nu(17)\le24668\).

## 1. Exact finite accounting and necessary period divisors

For odd \(n=2r+1\), let \(W_r=\binom{2r+1}{r}\). The
[height-adaptive all-rank word](/Users/amir.nuriyev/Documents/problem/HEIGHT_ADAPTIVE_PBBS_CONSTRUCTION_20260908.md)
has length and normalized excess
\[
 N_r=W_r+\sum_{\mathcal C}(2h_{\mathcal C}-1),\qquad
 \frac{N_r-W_r}{W_r}=\mathbb E_r\frac{2h(A)-1}{v(A)}.    \tag{3}
\]
The expectation is over uniform original middle states, equivalently
uniform Dyck roots for these rotation-invariant quantities. The finite
strict-height corridor guarantees every nonempty target. Always
\(v\ge n\) and \(0<2h-1<n\), so the summand is below one.

For original pruning sizes \(a_s=r_s\), write \(n_s=2a_s+1\).
If the first \(L\) incoming-gap rows are primitive, the
[persistent-label period theorem](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_INVARIANT_GAP_ROW_PERIOD_DIVISIBILITY_INDEPENDENT_AUDIT_20260908.md)
gives \(\operatorname{lcm}_{s<L}(n_sn_{s+1})\mid v\), hence
\(n_s\mid v\) at every depth used below. This is used only as a
necessary condition for an actual short period.

## 2. Exact reverse full-row law and primitivity

The original profile weight is
\(\prod_{j\ge0}\binom{a_j+a_{j+2}}{2a_{j+1}}\), padded by zeros.
Under the auxiliary probability \(\Pr_*(D)=4^{-|D|}/2\), the exact
reverse conditional sum law at depth \(s\) is
\[
 \ell_s\mid(a_{s+1}=b,a_{s+2},\ldots)
 \sim\operatorname{NB}(p_s,q_s),
 \quad p_s=2b+1,\quad q_s=(s+2)^{-2}.                   \tag{4}
\]
It is the normalized inverse fibre, before fixing \(a_0\).
Conditional on the sum \(t\), the row is a uniform weak composition
of \(t\) into \(p_s\) parts. Its composition count cancels the
binomial coefficient in (4). Therefore the full row has exact mass
\[
 \Pr_*(Z_s=z\mid\text{entire deeper profile})
                         =(1-q_s)^{p_s}q_s^{\sum z_j}.  \tag{5}
\]
Thus its coordinates are independent geometric variables under this
specific reverse conditional law. No dynamically sampled or fixed-size
geometric law is being asserted.

For an odd row length \(p\) and repetition factor \(e>1\) dividing
\(p\), the exact repeated-row probability is
\[
 \left(\frac{(1-q)^e}{1-q^e}\right)^{p/e}
 \le(1-q)^{p-p/e}\le e^{-2pq/3}.
\]
Here \(e\ge3\). Union over the possible factors gives
\[
 \Pr_*(Z_s\text{ nonprimitive}\mid\text{deeper profile})
                          \le p_s e^{-2p_sq_s/3}.        \tag{6}
\]
For \(p=1\) no nontrivial repetition exists. This estimate has already
summed every row mass; no separate second-difference regularity event is
needed.

Returning to size \(r\) is done explicitly:
\[
 \Pr_*(a_0=r)=\operatorname{Cat}_r/(2\,4^r)
 \ge1/Q_r,\qquad Q_r=2(r+1)(2r+1)\le12r^2.
                                                                    \tag{7}
\]
For any event, drop the restriction \(a_0=r\) before applying a reverse
kernel, then divide by the exact conditioning probability. This costs
at most \(Q_r\), once per event being transferred.

## 3. A logarithmic-gcd divisibility bound

Let \(U\) have a unimodal integer law of maximal atom \(\rho\), and
suppose \(Y=2U+1\ge Y_0>1\) throughout its possibly infinite support.
Every residue class modulo \(m\) has probability at most \(1/m+2\rho\),
by the total variation of the unimodal probability sequence. For any
integer \(v\ge1\), expansion of prime valuations gives
\[
 \mathbb E\log\gcd(Y,v)
 =\sum_{p^j\mid v}(\log p)\Pr(p^j\mid Y)
 \le S(v)+2\rho\log v,
 \quad S(v)=\sum_{p^j\mid v}\frac{\log p}{p^j}.
\]
Odd prime powers each specify one residue class; powers of two never
divide \(Y\), and adding their upper bounds is harmless. On \(Y\mid v\),
the same nonnegative statistic is at least \(\log Y_0\). Hence
\[
                  \Pr(Y\mid v)\le
                       \frac{S(v)+2\rho\log v}{\log Y_0}.           \tag{8}
\]

The elementary prime-factorization estimate already proved in the earlier
prime audit is \(|\sum_{p\le y}(\log p)/p-\log y|\le16\).
All higher powers contribute less than three. Split primes at
\(M=2+\log v\); the small primes cost at most \(\log M+19\), and
the large prime powers dividing \(v\) cost at most \((\log v)/M<1\).
Thus the entirely explicit arithmetic bound is
\[
                         S(v)\le\log(2+\log v)+20.       \tag{9}
\]
No prime number theorem, support truncation or independence of residues
is needed. The [complete logarithmic-gcd audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_LOG_GCD_DIVISIBILITY_AND_FINITE_REVERSE_TEST_AUDIT_20260908.md)
proves (8)–(9), including \(v=1\) and infinite supports.

## 4. Constant rejection under the reverse kernel

Put
\[
 X=\log r,\quad D=\log X\ge2^{20},\quad
 J_r=(rX^2)^{1/5},\quad L=\lfloor J_r\rfloor.
                                                                    \tag{10}
\]
Let \(\mathcal A\) impose one-percent relative accuracy of \(a_j\)
through depth \(L+1\), including \(a_0\). In the fixed-size law its
depth-zero condition is automatic; under the auxiliary law it is a
range centered at the fixed reference parameter \(r\).

At a reverse step \(s<L\), assume only the two child sizes \(b,c\)
are in these ranges. The whole conditional parent law is
\(a_s=2b-c+T\), where \(T\) has (4). A Fourier bound gives
\(\max_t\Pr(T=t)\le1/\sqrt{p_sq_s}\). The child ranges imply
\[
 \rho\le\sqrt{(L+2)^3/r},\qquad
                       2a_s+1\ge r/(L+2)=Y_0            \tag{11}
\]
on the entire conditional support. The parent itself is not conditioned
to be regular.

For a fixed \(v\le e^{L/16}\), (8)–(11) give
\[
 \Pr_*(2a_s+1\mid v\mid\text{deeper profile})
 \le\frac{\log(2+L/16)+20+(L/8)\sqrt{(L+2)^3/r}}
              {\log(r/(L+2))}\le\frac12.                \tag{12}
\]
The last comparison is finite throughout (10). Indeed \(X\ge128D\),
\(J_r\ge100\), and
\(L\sqrt{(L+2)^3/r}\le(11/10)X\). The numerator is at most
\((27/80)X+(2/5)D+20\); the denominator is at least
\((4/5)X-(2/5)D-\log2\). Half the latter exceeds the former because
\(X/16\ge(3/5)D+20+(\log2)/2\).

## 5. Successive conditioning replaces conditional independence

For each fixed \(v\), keep the coarse ranges and all divisibility tests
at depths \(0,\ldots,L-1\). Conditional on the whole deeper profile,
integrate the first parent size; drop its own range restriction when
applying (12). Its two child ranges are still present. Repeat the same
tower argument for the next parent size. At every step the retained
child ranges justify the next factor \(1/2\). Therefore
\[
 \Pr_*(\mathcal A,\ 2a_s+1\mid v\text{ for all }s<L)
                       \le2^{-L}.
\]
Equivalently this is an induction for conditional expectations of the
products of the first \(s\) indicators. It is not independence of the
sizes, and it does not recondition a kernel on earlier successes.
Pay (7) afterwards:
\[
 \Pr_r(\mathcal A,\ 2a_s+1\mid v\text{ for all }s<L)
                       \le Q_r2^{-L}.                   \tag{13}
\]

Let \(\mathcal G\) be \(\mathcal A\) and first-\(L\) primitivity.
The original one-depth concentration and (6), with fixed-size transfer,
give the finite bound
\[
 \Pr_r(\mathcal G^c)\le
 2(L+1)e^{-r/[240000(L+2)^2]}
 +Q_rL(3r+1)e^{-2r/[3(L+2)^3]}.                          \tag{14}
\]
The prior explicit scale guards apply because this is exactly the same
depth as the earlier reverse-profile construction: if
\(\Gamma=r^{1/5}X^{-3/5}\), then \(J_r=\Gamma X\) and
\(\Gamma\ge2^{400}X\) on (10). They make (14) at most \(e^{-L}\).

On \(\mathcal G\), a small actual period must pass every test in
(13). Union over at most \(e^{L/16}\) candidate integers gives
\[
 \Pr_r(v(A)\le e^{L/16})
 \le e^{-L}+Q_re^{L/16}2^{-L}\le e^{-L/3}.               \tag{15}
\]
The proof never conditions the reverse law on primitivity. It uses
primitivity only for the deterministic necessary divisibilities.

## 6. Word length, explicit domain and both parities

Split the exact charge (3) at the period threshold in (15). Short-period
states cost at most their probability, and all other states cost at most
\(n e^{-L/16}\). The finite guards above imply
\(\log Q_r\le L/16\), \(\log n\le L/64\), and
\(L\ge64\log2\). Thus
\[
 \frac{N_r-W_r}{W_r}\le n e^{-L/16}+e^{-L/3}
                  \le e^{-L/32}\qquad(D\ge2^{20}).      \tag{16}
\]

For \(k\ge\lceil e^{e^{2^{21}}}\rceil\), use its largest odd source
dimension \(n=2r+1\). Then \(r\ge k/3\),
\(\log r\ge\tfrac12\log k\), and \(\log\log r\ge2^{20}\).
Consequently
\[
 J_r\ge\tfrac12(k(\log k)^2)^{1/5},\qquad
 L\ge J_r/2\ge\tfrac14(k(\log k)^2)^{1/5}.
\]
The exact even lift doubles length and width together. Inserting these
bounds in (16) proves (1) in both parities, with the stated numerical
threshold. On that threshold \(\log\log k\ge2^{21}\) also implies
\((\log k)^{2/5}\ge128\), proving (2).

## 7. Scope and finite status

This is a stronger estimate for one fixed all-rank word, with all openings
already included in (3). It removes the local-profile smoothing and
missing-prime selection steps used in the preceding route. It does not
remove the inherited finite support, pruning and concentration premises.
The user's sandbox checker and its reported test totals were not available
here and have not been rerun. The internal proof audit supplies the
general deductions independently of those reported finite experiments.

Using the handoff's exact lower bound, (1) also gives
\(0\le\nu(k)-B(k)\le W(k)e^{-(k(\log k)^2)^{1/5}/128}\)
on its numerical domain. The absolute excess need not be zero, since
\(W(k)\) grows exponentially. Exact equality remains open.

The complete verified finite word is still
[the 24,668-letter certificate](/Users/amir.nuriyev/Documents/problem/K17_UPPER24668_VERIFIED_20260908.md).
The separately reported 24,660 word awaits its actual mask list; no new
finite upper bound follows from this general theorem at dimension 17.
