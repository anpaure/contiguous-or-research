# Fresh primes in the exact pruning kernel: a stretched-exponential error

## 1. Main result and scope

Let W(k)=binomial(k,floor(k/2)). Retain the height-adaptive word construction
from HEIGHT_ADAPTIVE.md. For odd n its length is

    N_n = W(n) + sum_C (2h_C-1).

Its all-rank support still uses the finite global-maximum corridor lemma and
its strict-height refinement. This note changes the estimate of that same
construction, not its definition. It does not import the proposed
clock/renewal/overlap proof in FULL_PROOF_TEXT.

**Theorem.** For every fixed real c with 0<c<9/512, and all sufficiently
large k (depending on c),

    nu(k) <= W(k) [1 + exp(-c k^(1/5))].                         (1)

In particular c=1/128 works. There is also a conservative explicit onset:
that c=1/128 bound holds for every integer k>=2^2048+1. The enormous onset is
a proof certificate, not a claim of practical optimality; earlier finite
bounds are more useful at moderate dimensions.

The relative error in (1) is stretched exponential in the dimension. It is
asymptotically smaller than exp(-c (log k)^2) for every positive constant c.
It is not an additive polynomial error, and does not prove nu(k)=B(k).

The new step exposes the original pruning hierarchy in reverse order under
its exact auxiliary measure. A uniform residue bound for each conditional
negative-binomial law bounds the probability of a surviving step failing to add a
new large prime. Distinct selected primes divide the physical period. The
argument does not assert independence of the pruning sizes or of the prime
success events. Fixed-size conditioning is done only after the auxiliary
probability bound has been proved.

## 2. Finite inputs retained from the earlier notes

For a uniform physical middle state in dimension n=2r+1, let h be its height,
v its f^2-cycle length, and n_s=2r_s+1 the size after s pruning rounds. The
following inputs were derived in the working notes:

    epsilon_n := (N_n-W(n))/W(n) = E[(2h-1)/v],
    v>=n,  2h-1<n.                                             (2)

If the first L incoming gap rows are primitive, then

    lcm(n_0 n_1, n_1 n_2, ..., n_(L-1) n_L) divides v.           (3)

In particular every n_1,...,n_L divides v. This is a physical return theorem,
not a claim that those integers are coprime.

We also retain the exact inverse-pruning law. On all finite Dyck words put

    P_0(D)=4^(-|D|)/2.

This is a probability measure. Conditional on |D|=r it is uniform on Dyck-r.
If D_(s+1)=E has semilength t and b peaks, then conditional on this core the
p=2t+1 incoming gap entries in the parent row are independent geometric
variables with probability (1-q_s)q_s^j, where

    q_s=1/(s+2)^2,
    r_s=t+b+ell_s,
    ell_s=sum of the p gaps.                                   (4)

Thus n_s=2(t+b+ell_s)+1 is an affine image, with multiplier 2, of a
negative-binomial variable. The deeper cores are deterministic functions of
E. Consequently (4) remains its exact conditional law after the entire deeper
hierarchy is exposed.

For reference, this law follows from the inverse-pruning identity

    sum_(partial D=E) x^|D| y^pk(D)
      = (1-xy)^(-1) [x/(1-xy)^2]^t (xy)^b.

Its depth-s parameters are x_s=(s+1)^2/(s+2)^2 and y_s=1/(s+1)^2.
No fixed-size law has been substituted by independent gaps: we explicitly
condition back in Section 7.

Finally, for iid fair bits on an odd n-cycle, if N_L is the length after L
equality recordings, the inherited finite census and bounded-change result
imply

    E N_L >= n/(L+1),
    P(N_L-E N_L <= -a) <= 2 exp(-a^2/(2n)).                    (5)

The first inequality follows from the exact nonnegative cosine sum in the
all-depth census. The second follows because changing one input bit changes
N_L by at most two. Uniform Dyck roots and uniform physical middle states
have the same distribution of rotation-invariant statistics.

These inputs are in MULTILEVEL_ADVANCE.md, Sections 2-5, and the finite
all-depth pruning census in the supplied proof archive. The new proof does
not need the joint-profile point-mass bound, the old sixth-power exceptional
estimate, or any fractional-LCM moment theorem.

## 3. Residues of a unimodal lattice law

**Lemma 1.** If Z is integer-valued with unimodal probability mass function,
and m=max_j P(Z=j), then for every positive integer d and every residue a,

    P(Z=a mod d) <= 1/d + 2m.                                 (6)

Extend the mass function by zero at both ends (or use its limits at infinity).
Its total variation is 2m. Partition the integers into d-point blocks starting
at the selected residue. Within a block, the mass at its first point is at
most the block average plus the oscillation of the mass function on that
block. Sum over the blocks. The total of their oscillations is at most the
full variation 2m. This proves (6), including infinite support by monotone
limits.

The negative-binomial law in (4) is unimodal: its successive mass ratio is
q_s(p+j)/(j+1), which decreases through one. Fourier inversion gives

    max_j P(ell_s=j | E) <= (s+2)/sqrt(2t+1).                   (7)

For completeness, its characteristic function has modulus to the p-th power

    [1+4q sin^2(theta/2)/(1-q)^2]^(-p/2)
       <= exp[-2pq theta^2/(pi^2(1+q)^2)]  (|theta|<=pi).

Use sin(|theta|/2)>=|theta|/pi and log(1+z)>=z/(1+z), then integrate over the
real line. This bounds the mass by sqrt(pi)(1+q)/(2sqrt(2pq)). Since q<=1/4
and pi<4 this is at most 1/sqrt(pq), proving (7).

For every odd d, multiplication by 2 is invertible modulo d. Therefore the
same residue bound applies to the parent size n_s=2(t+b+ell_s)+1. Powers of 2
never divide this odd size; they can simply be omitted.

## 4. An elementary small-prime logarithmic budget

For real Y>=2,

    sum_(p prime <=Y) log(p)/(p-1) <= log Y + 16.                (8)

Here is a proof with constants. The central-binomial divisibility argument
at powers of two gives theta(x)=sum_(p<=x)log p <3x for x>=2.
For an integer m>=2 put psi(m)=sum_(p^a<=m)log p. Then

    psi(m) <= 3m + 3 sqrt(m) log_2 m <= 8m.

Indeed log(m)/sqrt(m)<=2/e, log 2>1/2, and e>8/3 give a constant below 8.
The factorial identity gives

    log(m!) = sum_(p^a<=m) floor(m/p^a) log p
             >= m sum_(p^a<=m) log p/p^a - psi(m).

Thus the truncated prime-power sum is at most log m+8. For each prime p<=m,
let p^a be its first power greater than m. The remaining geometric series is
at most 2/m. Its contribution, summed over p, is at most
2 theta(m)/m<=6. Hence the complete sum is at most log m+14. Take m=floor Y
to obtain (8), with the deliberately looser constant 16.

This is an upper bound only. No prime number theorem or asymptotic estimate
for smooth numbers is used.

## 5. One conditional step produces a new prime

Fix an odd n, an integer L>=2, and a real Y>=2. Put

    B = n/[2(L+1)] > 1,
    mu = (L+1)/sqrt(B),
    Kappa(n,L,Y) = [log Y+16+2mu Y log n]/log B
                   + L(1/Y+2mu).                             (9)

Suppose a revealed child core has size between B and n. At every upward
step s<=L-1, (7) bounds its conditional mass by mu.

Let Gamma be ANY previously chosen set of at most L distinct primes greater
than Y, measurable from the already exposed deeper cores. Call the next size
N successful if N<=n and it has a prime factor greater than Y outside Gamma.
Otherwise, if N>n, kill this trajectory.

**Lemma 2.** Conditional on any such deeper history,

    P(N<=n and no new prime | history) <= Kappa(n,L,Y).         (10)

The parent always has N>=B because inverse pruning cannot decrease size.
Let Q_Y(N) be the largest divisor of N composed only of primes <=Y. On
N<=n, residue bound (6) yields

    E[log Q_Y(N); N<=n | history]
      <= sum_(p<=Y) log p/(p-1) + 2mu pi(Y) log n
      <= log Y+16+2mu Y log n.                                (11)

Only powers p^a<=n need be included. The total error weight for each prime
is at most 2mu log n; the prime 2 has zero actual contribution and causes no
problem in this upper bound.

If N is Y-smooth, its log Q_Y equals log N>=log B. Markov's inequality and
(11) bound the probability of that case by the first term in (9).

If N is not Y-smooth but has no new prime, some prime in Gamma divides N.
Each such prime has conditional divisibility probability at most 1/Y+2mu,
by (6). A union bound proves (10).

Gamma contains ONLY one prime selected per previous success. It need not
contain all prime factors of all earlier sizes. This distinction is useful:
its cardinality is at most L, not L log n/log Y. Nevertheless every prime
selected by this procedure is distinct and divides one of the pruning sizes.

## 6. Many successes without independence

Assume Kappa(n,L,Y)<=5/8. Expose D_L first, retaining only B<=n_L<=n.
Then reconstruct D_(L-1),...,D_1 using the exact conditional kernels (4).
Start Gamma empty. At a successful step choose the smallest permitted new
prime and add it to Gamma. Stop and kill a trajectory when a size exceeds n.
There are m=L-1 steps.

Let S be the number of successes on an unkilled trajectory. On each active
history the joint probability of survival and failure is at most 5/8. Thus

    E[2^(-increment) 1_survive | history] <= 13/16.

This bound does not assume independence or that survival has probability one.
Iterating over the killed process gives

    E_0[2^(-S) 1_all_sizes_admissible] <= (13/16)^m.

By Markov's inequality,

    P_0(all sizes admissible and S<=m/16)
       <= 2^(m/16) (13/16)^m
       <= exp(-9m/64).                                    (12)

The last inequality uses log(13/16)<=-3/16 and log 2<3/4.
The initial restriction on D_L only decreases the left side; its law need
not be characterized or normalized anew.

Every success supplies a different prime >Y dividing some n_j, 1<=j<L.
On the primitive-row event (3), their product divides v. Consequently

    S>=(L-1)/16  ==>  v >= Y^((L-1)/16).                     (13)

A success may reuse a prime factor that occurred, but was not SELECTED, at
an earlier step. It cannot reuse a selected prime, so (13) is valid.

## 7. Conditioning back and bounding nonprimitive rows directly

The mass of |D|=r under P_0 is

    p_r=Cat_r/(2*4^r) >= 1/[n(n+1)].                        (14)

The lower bound follows because binomial(2r,r)>=4^r/(2r+1). Conditional on
that event, P_0 is precisely the required uniform-root law. Thus (12) gives

    P_r(B<=n_L and too few successes)
       <= n(n+1) exp[-9(L-1)/64].                           (15)

Under |D|=r, all sizes are <=n automatically and decrease with depth, so
n_L>=B makes all sizes in the exploration admissible. The event was bounded
BEFORE conditioning on r. No geometric law is asserted after that conditioning.

### Depth-L size

By (5), the fair-bit event N_L<B has probability at most
2 exp[-n/(8(L+1)^2)]. Conditioning those bits to be 0D has probability p_r.
Therefore

    P_r(n_L<B) <= 2n(n+1) exp[-n/(8(L+1)^2)].                (16)

### Nonprimitive rows under the exact auxiliary kernel

For p odd independent geometric(q) entries, a repetition factor e>1 must
be an odd divisor of p, so e>=3. Its probability is exactly

    [(1-q)^e/(1-q^e)]^(p/e).

Since 1-q^e>=1-q, this is at most

    (1-q)^(p(1-1/e)) <= exp(-2pq/3).

Union over at most p candidate repetition factors. On B<=p<=n and s<L,
q_s>=1/(L+1)^2, hence

    P_0(row s nonprimitive | child) <= n exp[-n/(3(L+1)^3)].

Drop the eventual root-size restriction before applying this conditional
bound, then union over s=0,...,L-1 and divide by p_r. This gives

    P_r(n_L>=B and some first-L row nonprimitive)
       <= L n^2(n+1) exp[-n/(3(L+1)^3)].                    (17)

This avoids the previous need to concentrate every second difference of the
profile. In particular, there is no n/(L+3)^6 exponent in the new exceptional
estimate. Empty reduced cores are covered by (16), since B>1.

## 8. Explicit finite error theorem

For odd n, L>=2, Y>=2, B>1, and Kappa(n,L,Y)<=5/8, the SAME height-adaptive
word satisfies

    epsilon_n <= 2n(n+1) exp[-n/(8(L+1)^2)]
                 + L n^2(n+1) exp[-n/(3(L+1)^3)]
                 + n(n+1) exp[-9(L-1)/64]
                 + n Y^(-(L-1)/16).                        (18)

Every quantity in (18) is explicit. To prove it, use (16), (17), and (15)
for the three bad events. By (2), their overhead per state is less than one.
On the remaining event, (13) and 2h-1<n bound the overhead by the final term
of (18). No independence, uniform-in-profile geometric approximation, or
new dynamical mixing assertion is needed.

Multiplying the right side by W(n) and taking a floor gives an explicit
finite upper bound on nu(n). Earlier bounds may be smaller at moderate n.

## 9. Polynomially many usable depths

Set w=n^(1/5) and choose

    L=floor(w/8),    Y=w.                                    (19)

Then

    log B/log n -> 4/5,
    mu Y -> 1/16,
    L/Y -> 1/8,
    2L mu -> 1/64.

Consequently

    Kappa(n,L,Y) -> 13/32+9/64 = 35/64 < 5/8.                (20)

The finite hypotheses eventually hold. The logarithms of the four terms of
(18), in order, are

    -Omega(n^(3/5)),
    -Omega(n^(2/5)),
    -(9/512+o(1)) n^(1/5),
    -(1/640+o(1)) n^(1/5) log n.                             (21)

Thus for every c<9/512, epsilon_n<=exp(-c n^(1/5)) for all sufficiently
large odd n. The standard doubling lift from odd n=k-1 preserves the
relative bound. Starting with a slightly larger odd-case constant proves
the same fixed c in both parities. This proves (1).

There is also a period statement behind the estimate: outside a set of
probability exp[-(9/512+o(1)) n^(1/5)], the period is at least
exp[(1/640+o(1)) n^(1/5) log n]. The more precise finite statement is
(13) together with (15)-(17).

### 9.1 An explicit, deliberately conservative onset

Suppose x=log n>=1024. Then w=exp(x/5)>=16x^2 (use the fourth term of its
power series), so w>=56 and

    L+1<=w/7,
    mu Y<=sqrt(2/343)<1/12,
    log B>=4x/5,
    L/Y<=1/8.

Therefore

    Kappa <= 3/8+(11/4)(1/12)+20/x
           <= 29/48+5/256=479/768 < 5/8.                    (22)

The first two terms in (18) are at most exp(-w/2), since their negative
exponents are at least (49/8)w^3 and (343/3)w^2, respectively, whereas
their logarithmic prefactors are at most 1+2x and 1+4x.

For the third term, L-1>=w/8-2 gives

    log(term_3)<=1+2x+9/32-9w/512
                <=-w/64-log 4,

using w/512>=x^2/32>=32x. The fourth term is at most exp(-w/2): indeed
L-1>=w/16 and x>=1024 give

    log(term_4)<=x-wx/1280<=-w/2.

Each exp(-w/2) is also at most (1/4)exp(-w/64). Summing gives

    epsilon_n<=exp(-n^(1/5)/64),  n odd and log n>=1024.     (23)

Since log 2>1/2, the integer threshold k>=2^2048+1 ensures that the relevant
odd n has log n>=1024. Also (k-1)^(1/5)>=k^(1/5)/2 for k>=2. Thus

    nu(k)<=W(k)[1+exp(-k^(1/5)/128)]

at every such k. This proves the explicit onset stated in Section 1.

## 10. Dependencies, interpretation, and verification boundary

The arithmetic and conditional-probability argument in Sections 3-9 is proved
here. The retained finite structural inputs are the height-adaptive support,
physical primitive-row divisibility, exact inverse-pruning kernels, and the
all-depth equality census/bounded-change facts. They are supplied with this
package for audit. No theorem about independent uniformly sampled integers
is being applied to the dependent pruning sizes.

This is a written proof, not a formal proof-assistant artifact. The original
archive itself labels its earlier coefficient-one manuscript as internally
AI-reviewed rather than externally/formally verified. The present argument
does not turn those review labels into additional premises, and does not use
the old proposed clock/renewal proof.

The finite tests in verify_fresh_primes.py exercise the new residue bounds,
exact geometric repetition law, killed-process inequalities, prime budget,
and constant arithmetic. The inherited diagnostic script can separately
recheck finite period/kernel identities. Those tests do not replace the
general arguments above. The finite 17-coordinate word is verified by an
independent full interval-OR enumeration and range-query check, separately
from this asymptotic proof.
