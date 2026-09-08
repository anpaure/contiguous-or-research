# A stopped logarithmic-LCM estimate for the height-adaptive word

2026-09-08. Consolidated from the user's supplied derivation and checked
by the [complete independent audit](scratch/PBBS_STOPPED_LCM_FINITE_THEOREM_INDEPENDENT_AUDIT_20260908.md).
This is an
alternative proof route, on the retained finite PBBS inputs. It gives

    nu(k)/W(k) <= 1 + exp[-c (k(log k)^2)^(1/5)]

for every fixed 0<c<1/3 and all sufficiently large k. In particular c=1/4
is valid eventually. This is weaker than the depth-product coefficient
3/5 on the same scale. It improves the earlier fresh-prime route and
does not replace the strongest recorded bound. No new finite word is
supplied by this argument, and exact equality nu(k)=B(k) remains open.

The retained inputs are the literal height-adaptive construction and its
full-cube support, primitive-row particle-return divisibility, exact
inverse-pruning fibres, and the depth-uniform equality census and
bounded-change estimate. They are consolidated in
HEIGHT_ADAPTIVE_PBBS_CONSTRUCTION_20260908.md,
HEIGHT_ADAPTIVE_LOG_GCD_RATE_20260908.md and
HEIGHT_ADAPTIVE_FRESH_PRIME_RATE_20260908.md. Internal mathematical review
does not constitute external or formal certification of these inputs.

## 1. The unchanged construction and exact auxiliary kernel

For odd n=2r+1 the constructed length is

    N_n=W(n)+sum_C(2h_C-1),
    epsilon_n=(N_n-W(n))/W(n)=E_r[(2h-1)/v],
    v>=n, 0<2h-1<n.

The expectation is over original uniformly sampled middle states. When
the first L gap rows are primitive, every n_j=2r_j+1, 1<=j<=L, divides
the physical f^2 period v.

Under the auxiliary probability P_0(D)=4^(-|D|)/2, the parent of a
revealed depth-(s+1) core with semilength t and b peaks has

    r_s=t+b+Z,  N=2(t+b+Z)+1,
    Z~NB(p=2t+1,q_s=(s+2)^(-2)).

The p incoming entries are independent geometric variables under this
reverse conditional law. Revealing the entire deeper history does not
change it, since the deeper cores are determined by the current child.
At fixed original size r, no such independence is asserted. The exact
conditioning cost is at most n(n+1), because

    P_0(|D|=r)=Cat_r/(2*4^r)>=1/[n(n+1)].

## 2. Uniform atom and gcd bounds

Fix L>=2 and B=n/[2(L+1)]>1. The Fourier estimate for the NB kernel gives

    max_j P(Z=j | child)<=sqrt(pi)(1+q_s)/(2sqrt(2pq_s)).

Thus at any depth s<L with child circumference p>=B, the whole
conditional law has maximal atom at most

    mu=(63/100)[L+1+(L+1)^(-1)]/sqrt B.                (1)

Here sqrt(pi)/(2sqrt2)<63/100; t+1/t increases for t>=2, so replacing
s+2 by L+1 is valid. The integer law is unimodal because its adjacent
mass ratio q(p+j)/(j+1) decreases through one.

For a unimodal integer law of maximal atom mu, total variation of the
mass sequence gives

    P(Z=a mod d)<=1/d+2mu.                              (2)

This holds on infinite support. Multiplication by two is invertible
modulo every odd prime power. Since N is odd, even powers contribute
nothing to its divisibility tests.

Let Q be the current odd least common multiple, and assume log Q<H
with H>=2. Prime valuation expansion and (2) give

    E[log gcd(Q,N) | history]
      <=sum_(p|Q) log(p)/(p-1)+2mu log Q.

The previously proved finite prime budget is
sum_(p<=Y)log(p)/(p-1)<=log Y+16. Splitting at H, the larger primes
contribute at most (2/H)sum_(p|Q)log p<=2. Therefore

    E[log gcd(Q,N) | history]<=log H+18+2mu H.          (3)

There is no truncation of the parent law in this expectation; it is
bounded by the finite list of prime powers dividing the known Q.

## 3. Stop at a prescribed LCM threshold

Choose 0<alpha<1 and let g=alpha log B. The exact increment is

    Delta=log(lcm(Q,N)/Q)=log N-log gcd(Q,N)>=0.

Every parent is at least its child, so N>=B. Hence Delta<g implies
log gcd(Q,N)>(1-alpha)log B. Markov applied to (3) proves

    P(N<=n and Delta<g | history)<=kappa,
    kappa=(log H+18+2mu H)/[(1-alpha)log B].            (4)

Expose the depth-L core first, retaining only B<=n_L<=n. Reconstruct
depths L-1,...,1, start Q=1, and update Q with each parent circumference.
Kill a trajectory when N>n and stop successfully once log Q>=H.
No fixed-size root is killed: under |D|=r, all its pruning sizes are at
most n. No independence of the successive sizes is used.

Assume kappa<1, choose theta>0, and put

    rho=kappa+(1-kappa)exp(-theta).

On any active history, write a for surviving failure mass and b for
surviving success mass. Then a<=kappa and a+b<=1, so
a+exp(-theta)b<=rho. Removing trajectories that have hit the threshold
can only lower this expectation. Iteration of conditional expectations
over m=L-1 steps yields

    E_0[exp(-theta S) 1_survives_without_hit]<=rho^m.

On a path without a hit, g S<=log Q<H. Consequently

    P_0(survives_without_hit)
       <=exp[theta H/(alpha log B)]rho^(L-1).           (5)

The initial core restriction is not renormalized. Returning to fixed
size multiplies (5) by at most n(n+1). On paths that hit and have all
first-L rows primitive, every size used in Q divides v; therefore
v>=Q>=exp H. The LCM, rather than a product of dependent sizes, is used
throughout.

## 4. Fully specified finite error theorem

The retained concentration and reverse geometric repetition bounds give

    P_r(n_L<B)<=2n(n+1)exp[-n/(8(L+1)^2)],
    P_r(n_L>=B, some first-L row nonprimitive)
       <=L n^2(n+1)exp[-n/(3(L+1)^3)].

The second bound follows from the exact e-fold geometric repetition
probability [(1-q)^e/(1-q^e)]^(p/e)<=exp(-2pq/3) for odd e>=3,
then a union bound and the original-size conditioning cost. It does
not impose geometric independence on a fixed-size row.

Charging each exceptional state by at most one and each remaining
state by n exp(-H) gives

    epsilon_n <=2n(n+1)exp[-n/(8(L+1)^2)]
              +L n^2(n+1)exp[-n/(3(L+1)^3)]
              +n(n+1)exp[theta H/(alpha log B)]
                    [kappa+(1-kappa)exp(-theta)]^(L-1)
              +n exp(-H).                              (6)

This is valid for every odd n and integer L>=2, with B>1, H>=2,
0<alpha<1, theta>0, kappa<1, with mu and kappa defined in (1),(4).
Every constant is specified. The integer collar sum is bounded by
floor(W(n) times the right side); add W(n) for the full word length.

## 5. Eventual coefficient range

Set x=log n, w=(n x^2)^(1/5), and choose

    L=floor(w/2), H=w/3, alpha=1/1024, theta=log x.

Then log B/x tends to4/5, mu w/x tends to63/200, and

    kappa -> [1/5+2(63/200)/3]/[(1023/1024)(4/5)]
           =2624/5115 <5131/10000=:kappa_star.

The strict logarithm comparison -log kappa_star>2/3 follows from
z=4869/15131 and the positive series

    log(1/kappa_star)=2 sum_(j>=0) z^(2j+1)/(2j+1)
       >2(z+z^3/3+z^5/5)>2/3.                           (7)

In the third term of (6), the logarithmic prefactors are o(w):
log[n(n+1)]=O(x) and theta H/(alpha log B)=O(w log x/x).
The remaining log is bounded above by
(L-1)log(kappa_star+1/x)=(w/2+o(w))log(kappa_star+1/x), giving
a coefficient strictly larger than1/3. The first two terms have
negative logarithms of orders n^(3/5)x^(-4/5) and n^(2/5)x^(-6/5),
both larger than w. The logarithm of the last term is

    log[n exp(-H)]=x-w/3=-(1/3+o(1))w.

Thus epsilon_n<=exp(-c w) eventually for each fixed c<1/3. The
endpoint c=1/3 is not asserted. For even dimensions use a slightly
larger odd-case constant c' between c and1/3, then the exact doubling
lift and (k-1)/k->1 give the same chosen c.

## 6. Verification and comparison

Root checked the conditional stopped-process proof and all retained
conditioning factors. The bounded h100 script
scratch/verify_stopped_lcm_constants_20260908.py independently checked
the exact kappa limit, its strict margin below kappa_star, the positive
three-term logarithm certificate (7), and the constant63/100 using
outward rational Machin bounds for pi. Its exact report is
scratch/stopped_lcm_constants_certificate_20260908.json. It used
5 CPU seconds, 10 wall seconds and128 MiB limits. No user-reported
checker suite or search count was represented as independently rerun.

The finite theorem (6) has no unspecified constants; an explicit
starting dimension for the optimized coefficient1/4 has not been
extracted in this note. The depth-product theorem supplies a stronger
coefficient3/5 on the same scale with its own explicit onset, and the
fresh-prime theorem supplies a weaker scale with a smaller onset.
These comparisons are about proved upper bounds, not exact attainment.
