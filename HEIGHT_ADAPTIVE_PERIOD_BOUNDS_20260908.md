# Height-adaptive PBBS period bounds and the verified 24,715-letter word

2026-09-08. This record consolidates the two period advances that completed
internal proof review. Their finite inputs are the height-adaptive all-rank
construction, invariant equality-particle reduction, original pruning
fibre, and finite concentration/counting identities. Internal AI-agent
review is not external mathematical review or formal verification.

The later profile-sieve submission is reviewed separately. It must not be
confused with either of the fully explicit results recorded here.

At completion of the two period audits, the verified finite bound was
\[
 \boxed{24313=B(17)\le\nu(17)\le24715.}
\]
The later supplied 24,668-word has since passed the same complete checks,
reducing the current gap to 355; see
[the new literal certificate](/Users/amir.nuriyev/Documents/problem/K17_UPPER24668_VERIFIED_20260908.md).
None of the following asymptotic estimates establishes exact equality
with \(B(k)\).

## 1. Results and their different quantitative uses

All logarithms are natural. Put \(W(k)=\binom{k}{\lfloor k/2\rfloor}\).
The stronger asymptotic estimate has the explicit constants
\[
 \boxed{\frac{\nu(k)}{W(k)}\le
 1+\exp[-2^{-32}(\log k)^{6/5}],\qquad
 k\ge\lceil\exp(\exp256)\rceil.}                         \tag{1}
\]
It follows that \(0\le\nu(k)-B(k)=O_m(W(k)/k^m)\) for every fixed
\(m>0\). The enormous threshold is a sufficient bound from conservative
finite estimates, not an assertion about when the actual construction
first becomes effective.

A separate one-row estimate gives a useful fully numerical finite bound.
For odd \(n=2r+1\ge5\), set
\[
 \beta_n=4n(n+1)(242/243)^n+n(99/100)^n.
\]
Then
\[
 \boxed{\nu(n)\le W(n)+\left\lfloor
 \frac{2^{n+2}+2W(n)}{n^2}+W(n)\beta_n\right\rfloor.}       \tag{2}
\]
The floor encloses the entire sum. The exact one-coordinate lift doubles
this odd-dimensional length and its width, giving the corresponding even
bound. At small dimensions one can take the minimum with the earlier
height-adaptive bound in Section 9.13 of the master handoff.

In particular,
\[
 \nu(k)\le W(k)\left(1+\frac{2\sqrt{2\pi}}{k^{3/2}}
                           +O(k^{-2})\right),             \tag{3}
\]
and exact arithmetic plus monotonicity gives
\[
 \boxed{\nu(k)<1.01W(k)\ (k\ge5643),\qquad
        \nu(k)<1.001W(k)\ (k\ge6255).}                    \tag{4}
\]
Equation (1) is asymptotically stronger than (3). Equation (2) supplies
the much more useful finite thresholds in (4). The order in which the
user submitted these bounds does not reverse that comparison.

## 2. The unchanged word and its exact overhead

The [height-adaptive construction](/Users/amir.nuriyev/Documents/problem/HEIGHT_ADAPTIVE_PBBS_CONSTRUCTION_20260908.md)
uses cycles of \(g=f^2\), where \(f\) is the physical parenthesis-flip
map on the middle layer of \(n=2r+1\) coordinates. A cycle \(\mathcal C\)
has invariant height \(h_{\mathcal C}\), period \(v_{\mathcal C}\), and
nonzero erosion letters
\(D_i=\bigcap_{j=0}^{h_{\mathcal C}}X_{i+j}\).
Emit its period and its first \(2h_{\mathcal C}-1\) letters. The
strict-height global-maximum corridor supplies every nonempty target,
including all exterior ranks. Thus the literal construction has length
\[
 N_n=W(n)+\sum_{\mathcal C}(2h_{\mathcal C}-1).
\]
For a uniformly chosen physical middle state \(A\), this is exactly
\[
 \frac{N_n-W(n)}{W(n)}=
 \mathbb E_A\frac{2h(A)-1}{v(A)}.                         \tag{5}
\]
The measure is uniform on states, not on cycles. Since \(v(A)\ge n\)
and \(2h(A)-1<n\), the summand is always below one. The new results
sharpen the denominator in this already valid finite compiler.

## 3. Persistent particles force a larger period divisor

At one pruning level, let \(p\) be the odd number of equality particles.
Their cyclically indexed incoming gaps have invariant coordinates
\(Z_j=(L_j-1-\epsilon_j)/2\). Let \(d\mid p\) be the least cyclic
period of this gap row. Persistent particle labels are not reassigned
when the physical root changes.

Lift the positions so that \(x_{j+p}=x_j+n\). Each physical update moves
one particle by one edge, without overtaking. At a physical return after
\(t\) updates, order preservation gives an integer \(m\) with
\(x_j(t)=x_{j+m}(0)\) for every \(j\). Summing one period of
displacements gives
\[
 t=\sum_{j=0}^{p-1}(x_{j+m}(0)-x_j(0))=nm.
\]
The returning physical word has its old gap data at every edge, while
the persistent row has remained fixed. Hence \(Z_j=Z_{j+m}\), so
\(d\mid m\). Taking \(t=2v\), and using oddness of \(n,d\), proves
\[
                         \boxed{nd\mid v.}              \tag{6}
\]

If the row is primitive, \(d=p\), every particle returns to its own
edge and original recorded bit. The reduced word therefore returns with
its labels fixed after the same \(t\) reduced updates. Iterating through
\(L\) primitive rows gives
\[
 \operatorname{lcm}_{0\le s<L}(n_sn_{s+1})\mid v,
 \qquad n_s=2r_s+1.                                     \tag{7}
\]
In particular all \(n_0,\ldots,n_L\) divide \(v\). Their full product
is not asserted to divide \(v\). The one-particle terminal case is
handled directly; a zero row with more than one particle is nonprimitive.

The complete [particle-return audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_INVARIANT_GAP_ROW_PERIOD_DIVISIBILITY_INDEPENDENT_AUDIT_20260908.md)
identifies the finite reduction and invariant-row source statements and
checks the fixed-label descent without a hidden time rescaling.

## 4. The one-row finite estimate

Conditional on the full original pruning profile, a row is a uniform
weak composition of \(\ell\) into \(p\) parts. If an odd-length row is
\(e>1\) repetitions, then \(e\ge3\), \(e\mid\ell\), and its count is
\(D_e=\binom{(p+\ell)/e-1}{p/e-1}\), among
\(D=\binom{p+\ell-1}{p-1}\) possible rows. Concatenating independently
chosen shorter compositions gives \(D_e^e\le D\). Therefore
\[
 \Pr(d<p\mid\text{profile})\le pD^{-2/3}.
\]
When \(p\ge9n/22\) and \(\ell\ge n/33\), taking
\(q=\lceil n/33\rceil\) gives
\(D\ge\binom{2q}{q}\ge2^q\), and the failure probability is at most
\(n(99/100)^n\).

Write \(N_1,N_2\) for the first two equality-recording sizes. Their exact
fair-bit expectations and bounded differences are
\[
 \mathbb EN_1=n/2,\quad
 \mathbb EN_2=n/3+4n/(3\,2^n),\quad
 |\Delta N_i|\le2
\]
under a single input-bit change. A deviation \(n/11\), followed by
conditioning to a uniform Dyck root, costs at most
\(4n(n+1)(242/243)^n\). Outside this event,
\(p=N_1\ge9n/22\) and
\(\ell=(n-2N_1+N_2)/2\ge n/33\). Consequently the event
\(p\ge9n/22,d=p\) has probability at least \(1-\beta_n\).
This is the original uniform-state law; no clock or cycle-size bias is
introduced.

Let \(t=2^n/W(n)\). Exact reflection and cyclic-edge counting give
\[
 \mathbb E(2h-1)\le2t-3,\quad
 \mathbb Eh^2\le2n,\quad
 \mathbb E(p-n/2)^2\le n/3.
\]
For completeness, if \(M,m\) are the maximum and minimum of the linear
bridge ending at \(-1\), its reflection moments are
\(\mathbb EM^2=r+2-t\), \(\mathbb Em^2=r+1\), and \(h\le M-m\).
Counting cyclic \(10\) edges gives
\(\mathbb Ep=r\) and \(\operatorname{Var}(p)=(r^2-1)/(2r-1)\).
Cauchy–Schwarz therefore yields
\(\mathbb E[h|p-n/2|]\le\sqrt{2/3}\,n\), without independence.

On the good event, (6) gives \(v\ge np\) and
\[
 \frac1p\le\frac2n+\frac{44}{9n^2}|p-n/2|.
\]
Charge bad states by their probability in (5). It follows that
\[
 \frac{N_n-W}{W}\le
 \frac{2(2t-3)}{n^2}+\frac{88\sqrt6}{27n^2}+\beta_n
 \le\frac{4t+2}{n^2}+\beta_n,
\]
since \(88\sqrt6/27<8\). Integer rounding proves (2).

The [complete moment and finite-bound audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_ONE_ROW_PERIOD_MOMENTS_AND_EXPLICIT_N_THREE_HALVES_RATE_20260908.md)
includes the first-two-recording census and all finite domain checks.

Put \(R(n)=(4t+2)/n^2+\beta_n\). It decreases along odd \(n\ge485\):
use \(t(n+2)=t(n)(n+3)/(n+2)\) for the first term; the two terms in
\(\beta_n\) decrease for integer \(n\ge484\). Exact rational arithmetic
on `h100` gives the following strict enclosures, each upper endpoint being
the listed lower endpoint plus \(10^{-24}\):

| Odd dimension | Lower endpoint for \(R(n)\) | Exact comparison |
|---:|---:|---|
| 5641 | 0.010065906889287253783526 | \(R(n)>1/100\) |
| 5643 | 0.009990393077418169965223 | \(R(n)<1/100\) |
| 6253 | 0.001000477920417412307465 | \(R(n)>1/1000\) |
| 6255 | 0.000992967613437660795735 | \(R(n)<1/1000\) |

The [exact threshold certificate](/Users/amir.nuriyev/Documents/problem/scratch/pbbs_beta_rational_threshold_certificate_20260908.json)
retains the rational numerators, denominators and integer comparisons.
Monotonicity and the even lift prove (4) in every stated dimension.

## 5. Many primitive rows give the explicit superpolynomial estimate

Put \(u=\log r\ge2^{20}\),
\(L=\lfloor r^{1/6}/u\rfloor\), and
\(\Delta=r/[100(L+3)^3]\). The retained finite estimate is
\[
 \Pr(|r_s-r/(s+1)|>(4+x)\sqrt r)\le2e^{-x^2/6}
 \quad(s\ge0,x\ge0).
\]
A union over \(0\le s\le L+1\), together with the exact second
difference of \(r/(s+1)\), shows that with probability at least
\(1-e^{-2^{-26}u^6}\) these profile values are regular and all first
\(L\) rows are primitive. Indeed, regularity fails with probability at
most \(e^{-2^{-25}u^6}\); every regular row has both length and mass at
least \(r/(L+3)^3\), and the repetition count above makes the remaining
failure at most \(e^{-u^6/4}\).

On this good event, the sizes \(n_0,\ldots,n_L\) are positive and
strictly decreasing. Equation (7) gives more than
\(\tfrac12 n^{1/6}/\log n\) distinct divisors of \(v\), all at most
\(n\). The [complete probability audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_SUPERPOLYNOMIAL_PERIOD_REGULARITY_AND_PRIMITIVE_ROWS_INDEPENDENT_AUDIT_20260908.md)
checks the floors, extinction boundary and original-root normalization.

Here is the arithmetic step with its constants. If
\(\log\log x\ge12\), \(v\ge x\), and \(v\) has at least
\(\tfrac12 x^{1/6}/\log x\) divisors at most \(x\), then
\[
                         \log v\ge2^{-24}(\log x)^{6/5}. \tag{8}
\]
To see this, put \(M=\log v\), \(X=\log x\). The central-binomial
prime estimate gives \(\pi(y)\le16y/\log y\), and hence, uniformly for
\(1/12\le\sigma\le1/6\),
\[
 \sum_{p\mid v}p^{-\sigma}\le512M^{1-\sigma}/\log M.
\]
The finite divisor product then implies
\[
 \log D_x(v)\le\sigma X+2^{14}M^{1-\sigma}/\log M.
\]
If \(M<X^{6/5}\), choose \(\sigma=1/6-1/\log X\). The assumed
divisor count gives a left excess at least \(X/(2\log X)\), whereas
\(M^{1-\sigma}<4M^{5/6}\) and \(\log M\ge\log X\). Thus
\(M\ge2^{-102/5}X^{6/5}\ge2^{-24}X^{6/5}\), proving (8).
The [finite arithmetic audit](/Users/amir.nuriyev/Documents/problem/scratch/PBBS_BOUNDED_SMALL_DIVISORS_AND_LONG_PERIOD_RATE_ARITHMETIC_AUDIT_20260908.md)
proves each elementary prime estimate and numerical inequality.

Apply (8) on the good event in (5), and charge all other states by one.
For \(\log r\ge2^{20}\), \(\log\log n\ge12\), this gives the explicit
intermediate bound
\[
 \frac{\nu(n)}{W(n)}\le1+
 n e^{-2^{-24}(\log n)^{6/5}}+e^{-2^{-28}(\log r)^6}.     \tag{9}
\]
For \(k\ge\lceil e^{e^{256}}\rceil\), all finite guards hold, the
factor \(n\) is absorbed into the first exponent, and the second term
is smaller. Absorbing their sum and taking the odd source dimension
\(n=k\) or \(k-1\) proves (1) with \(2^{-32}\). The width and word
length both double in the even lift, so no prefactor two is lost there.

## 6. The actual 24,715-letter certificate

The supplied file `/Users/amir.nuriyev/Downloads/k17_upper24715.word`
is retained as [the word](/Users/amir.nuriyev/Documents/problem/answers/k17_upper24715.word).
Its SHA-256 is

```text
3e7da8c69f8d32ca73750e12b8746fc483f9d56a441ad94f1d3a2e9b4c11b2fe
```

The [standalone checker](/Users/amir.nuriyev/Documents/problem/scripts/verify_k17_upper24715.py)
was run on `h100`, with a 90 CPU-second, 110 wall-second, 1 GiB cap.
It independently enumerated the distinct suffix unions at every endpoint,
recorded one ordinary interval for every target, then checked all 131,071
witness intervals again using a separate segment-tree range-OR routine.
All letters are nonempty 17-bit masks. The
[executed report](/Users/amir.nuriyev/Documents/problem/witnesses/k17_upper24715/literal24715_verification.json)
and [all witnesses](/Users/amir.nuriyev/Documents/problem/witnesses/k17_upper24715/literal24715_target_witnesses.json)
are retained. This is a complete finite verification, independent of the
general PBBS proof and the user's local rewrite acceptance tests.

The claimed regeneration/search sequence was not supplied and has not
been independently reproduced. It is unnecessary for the literal upper
bound. The user’s separately mentioned 24,864-letter file was not supplied;
its claim is superseded here by the actual shorter verified word.

The earlier independently generated 24,957-word and the 24,947-word with
an optimal 118-leaf repair forest remain as construction provenance.
The latter's ten possible binary parents give a matching upper bound on
its ten saved positions within that specific 128-hole repair model; this
does not restrict arbitrary words. The literal 24,715 certificate is the
verified intermediate record, leaving 402 positions at that stage. The
later 24,668-word is the current finite record, leaving 355 positions.
