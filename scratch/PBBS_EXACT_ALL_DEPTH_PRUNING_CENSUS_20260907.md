# Exact iterated-pruning census and growing-depth Dyck concentration

2026-09-07. Root pure proof; no computation.
The finite renewal transform, Chebyshev coefficient calculation and
depth-uniform edit bound have separate independent audits. This note
assembles them into the growing-depth profile input needed by PBBS.

## 1. Cyclic equality pruning

For a cyclic binary word w, E(w) records, in cyclic order, the common
bit at each equal adjacent edge. Set E(empty)=empty. A one-letter
cycle has one equal self-edge. Define N_s(w)=|E^s(w)|, with N_0=|w|.

If |w|=n is odd, its number of unequal edges is even, so every N_s is
positive and odd. For a Dyck word D with r up-steps, take w=0D and
n=2r+1. Simultaneous deletion of all peaks10 removes one symbol from
each cyclic constant run; equality recording also leaves exactly
length-minus-one symbols from each such run. The distinguished extra
zero persists. Therefore E(0D), up to its root, is0(partial D), and

    N_s(0D)=2r_s+1,                                    (1)

where r_s is the number of up-steps after s peak-pruning rounds.
The identity remains valid after the Dyck word becomes empty.

## 2. A depth-uniform edit bound

Inserting a binary symbol x between adjacent symbols a,b changes E
by at most ONE cyclic insertion or deletion:

* If a=b=x, one equal-edge symbol becomes two copies: one insertion.
* If a=b!=x, the old equal-edge symbol disappears: one deletion.
* If a!=b, exactly one new edge is equal: one insertion.

The same statement holds for empty and singleton intermediates under
the conventions above. Deletion is the reverse operation. Hence E
does not increase cyclic insertion/deletion distance.

Flipping one bit of the original odd word toggles equality on its two
incident edges and changes no other recorded edge symbol. After the
first E this is at most two edits. Nonexpansivity then gives, for
EVERY s>=1,

    |N_s(w)-N_s(w with one bit flipped)|<=2.            (2)

Let the n input bits now be independent and fair. Exposing them gives
a Doob martingale with each increment of conditional range length at
most two. A centered variable of range length c has log moment
generating function at most lambda^2 c^2/8: its log-MGF second derivative
is a tilted variance at most c^2/4, and integration twice proves this.
Iterating over the n increments and optimizing lambda gives

    Pr(|N_s-E N_s|>a)<=2 exp(-a^2/(2n)),               (3)

uniformly in s. No independence between pruning depths is used.

## 3. Exact marked-renewal enumeration

Write the original cyclic edge marks as differences modulo two between
successive bits. Their law is uniform iid fair edge marks conditioned
on an even total mark. Each even edge-mark vector has exactly two bit
preimages. Survival under E depends only on these edge marks.

At level zero, each gap between successive surviving sites is one edge.
Its unnormalized length PGFs, distinguished by equal or different
endpoint bits, are

    A_0(z)=B_0(z)=z/2.

A site survives the next pruning exactly when its outgoing current-level
gap has equal endpoints. Starting at such a site, the next-level gap
consists of ONE A gap followed by j B gaps. Its endpoints agree exactly
when j is even. Thus, as formal series,

    A_(s+1)=A_s/(1-B_s^2),
    B_(s+1)=A_s B_s/(1-B_s^2).                        (4)

The decomposition is unique at every stage: the A gaps are precisely
the boundaries retained by the next pruning; all intervening gaps are B.
This is a weighted word-language enumeration, not an independence
claim for a finite pruned cycle.

Put F_s=A_s+B_s and D_s=A_s-B_s. If a specified original site survives
s rounds, the cycle rooted there is uniquely a concatenation of k>=1
level-s gaps. Projecting to an even total mark contributes

    (F_s^k+D_s^k)/2.

The factor1/2 is canceled by conditioning the original iid edge marks
to even parity. Summing k, and multiplying the probability that a
specified site survives by n, proves the exact coefficient identity

    E N_s=n[z^n] S_s(z),
    S_s=F_s/(1-F_s)+D_s/(1-D_s).                     (5)

Original odd cycles always have a survivor at every depth, so no
empty-survivor cycle is lost by this rooted enumeration. Multiple
survivors are counted once each by the fixed-site probability in (5);
there is no division by a cycle length or symmetry factor.

## 4. Chebyshev evaluation: an exact formula at every depth

Define T_j,U_j by

    T_0=1, T_1=x;       U_0=1, U_1=2x;
    P_(j+1)=2x P_j-P_(j-1).

Thus T_j(cos theta)=cos(j theta) and
U_j(cos theta)=sin((j+1)theta)/sin theta. The recurrences give

    U_(s+1)^2-1=U_s U_(s+2).

With x=1/z, induction in (4) yields

    A_s=U_s(x)/U_(s+1)(x),
    B_s=1/U_(s+1)(x).

Substitution into (5), or the displayed trigonometric expressions, gives

    S_s(z)=T_(s+1)(x)/[(x-1)U_s(x)]-1.                (6)

Since T_(s+1)/U_s is odd in x, the odd part of this series is

    (S_s(z)-S_s(-z))/2
       =T_(s+1)(x)/[(x^2-1)U_s(x)]
       =(1/(s+1))[x/(x^2-1)+U_s'(x)/U_s(x)].         (7)

The second equality follows from
(x^2-1)U_s'=(s+1)T_(s+1)-xU_s, proved by differentiating the
trigonometric expressions and then as a polynomial identity.

The roots of U_s are cos(pi j/(s+1)), j=1,...,s, all simple.
Taking its logarithmic derivative in (7), and using

    [z^n](x-c)^(-1)=c^(n-1),  x=1/z,

proves for EVERY odd n>=3 and EVERY s>=0

    E N_s=
       n/(s+1) sum_(j=0)^s cos^(n-1)(pi j/(s+1)).    (8)

The j=0 term comes from x/(x^2-1), whose odd coefficients are one.
For s=0 the logarithmic derivative is zero and (8) gives N_0=n.
The even power n-1 handles the roots near -1 as well as those near1.

For example (8) gives E N_1=n/2 and
E N_2=n/3+4n/(3*2^n). These are identities, not computational checks.

## 5. A uniform expectation error

Pair the roots j and s+1-j. For 0<=theta<=pi/2,
cos(theta)<=exp(-theta^2/2): differentiate log cos(theta)+theta^2/2,
using tan(theta)>=theta. Formula (8) therefore gives

    0<=E N_s-n/(s+1)
       <=[2n/(s+1)] sum_(j>=1) exp(-a_s j^2),
    a_s=(n-1)pi^2/[2(s+1)^2].                        (9)

In particular

    sum_(j>=1) exp(-a j^2)<=exp(-a)/(1-exp(-3a)),      (10)

because j^2>=1+3(j-1). Thus E N_s~n/(s+1) uniformly on every
depth range with n/(s+1)^2 tending to infinity. Formula (8), rather
than this asymptotic approximation, remains valid at larger depths.

## 6. Conditioning to Dyck and growing-depth regularity

Under iid bits, the event w=0D for a Dyck_r word has probability

    Cat_r/2^n >=1/[2(r+1)n].

Indeed Cat_r=binom(2r,r)/(r+1), and the largest binomial coefficient
is at least the average4^r/(2r+1). Conditional on this event D is uniform.

For ANY integer depth M>=1, (3) and a union bound consequently give

    Pr_D(exists1<=s<=M: |N_s-E_iid N_s|>a)
        <=4M(r+1)n exp(-a^2/(2n)).                   (11)

For sufficiently large odd n put

    L=floor(sqrt(n)/(log(n+1))^2),    M=L+2,
    a_n=sqrt(32n log(n+1)).

Since M<=n, the probability in (11) is at most

    2/(n+1)^13.                                      (12)

For s<=M, let
A_n=(n-1)pi^2/[2(M+1)^2] and
b_n=exp(-A_n)/(1-exp(-3A_n)).
Outside the event in (12), equations (9)-(10) give simultaneously

    |N_s-n/(s+1)|<=a_n+[2n/(s+1)]b_n.

Using (1), n=2r+1 and b_n=exp[-Omega((log n)^4)], this implies

    sup_(0<=s<=M) |r_s/[r/(s+1)]-1|
        =O((log n)^(-3/2)).                          (13)

Indeed the relative error is at most
[(M+1)a_n+2n b_n+M]/(n-1).
In particular it is at most1/log r for all sufficiently large r.
It also ensures that these pruning cores are nonempty, so using them
does not inadvertently pass the last nonempty core.

More generally (9) and (11) give simultaneous relative concentration
through any M=o(sqrt(n/log n)), with the corresponding union-bound
deviation. No growing-depth independence statement is asserted.

## 7. PBBS application and its limit

The full pruning profile is invariant under the accepted PBBS dynamics.
For any retained birth family with T<=H<r, the full trace has T+2 edges.
The BAD event from (12) therefore contributes raw short-trace incidence,
and hence occupied support, at most

    (H+2)W Pr_D(BAD)<=W/(n+1)^12.                    (14)

BAD consists of whole physical components. Removing it changes no
congestion on a retained good component. Intersecting this good event
with the earlier first-two-level good event preserves both conclusions.

The estimate (13) supplies a QUANTITATIVE GROWING ORIGINAL-profile
input. Conditional on any one such profile, the accepted original
inverse-pruning arrays still have their exact independent uniform
weak-composition law. It does not make adaptively reached arrays fresh,
or establish the law of a sampled incidence environment.

Applying (13) inside the full original clock-tree path sum is a
separate step. This note by itself gives no short-return mass bound,
overlap lower bound, packing theorem, or coefficient-one conclusion.

