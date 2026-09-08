# Auxiliary Boltzmann law and an exact joint-profile atom bound

2026-09-08. Independent pure-proof audit by `exact_b_induction`.
No mathematical program was run. Verdict: the auxiliary-law argument and
the stated joint-profile bound pass. The calculation actually gives the
slightly stronger factorial exponent 3/2 in place of 2.

The downstream rate inferred from this lemma is outside this bounded
audit. In particular this note does not replace the stronger every-third
profile-sieve argument by an unproved independence assertion.

## 1. Exact inverse-pruning generating function

For a Dyck word E with semilength t and b peaks, its parent D under
simultaneous peak deletion has

    |D|=t+b+ell,       pk(D)=b+ell,

where the original inverse-pruning gap row is a weak composition of
ell into `2t+1` parts. Hence the number of such parents is
`binom(ell+2t,2t)`.

This is the retained exact inverse-pruning fibre from
`/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_gaussian_clock_genealogy_structural_audit.md`,
section 1. Consequently, for q=xy<1,

    sum_(D:partial D=E) x^|D| y^pk(D)
       =x^t q^b sum_(ell>=0) binom(ell+2t,2t) q^ell
       =(1-q)^(-1) [x/(1-q)^2]^t q^b.                   (1)

The empty child has t=b=0. Its parents are the unique height-one words
of each semilength (including the empty word), so the same geometric
formula applies without a terminal exception.

## 2. The auxiliary measures are exact pruning pushforwards

The probability measure

    P_0(D)=4^(-|D|)/2

is normalized because the Catalan generating function at 1/4 is 2.
For s>=0 define

    x_s=(s+1)^2/(s+2)^2,
    y_s=1/(s+1)^2,
    Z_s=(s+2)/(s+1),
    P_s(E)=x_s^|E| y_s^pk(E)/Z_s.

These are exactly the depth-s pruning distributions under P_0.
Indeed `q_s=x_s y_s=(s+2)^(-2)` and direct algebra gives

    x_s/(1-q_s)^2=x_(s+1),
    q_s=y_(s+1),
    Z_s(1-q_s)=Z_(s+1).

Equation (1) therefore maps P_s to P_(s+1). This proves the
normalization inductively as well as the claimed marginal law.

Conditional on the complete child word E at depth s+1, its parent
surplus `ell=|D|-t-b` has the exact negative-binomial mass

    Pr(ell=k | E)
       =binom(k+N-1,N-1)(1-q_s)^N q_s^k,
    N=2t+1.                                             (2)

The peak count b changes only the shift of the parent size, not the
maximal atom. This conditional law is finite and exact; it is not a
geometric approximation of a conditioned fixed-size composition.

## 3. A direct finite maximal-atom bound for (2)

For any integer-valued random variable, Fourier inversion bounds each
atom by the average modulus of its characteristic function. For the
negative-binomial variable in (2) the modulus is

    [1+4q(1-q)^(-2) sin^2(theta/2)]^(-N/2).

Using `log(1+z)>=z/(1+z)`, and then `sin(|theta|/2)>=|theta|/pi`
for |theta|<=pi, this is at most

    exp[-2Nq sin^2(theta/2)/(1+q)^2]
      <=exp[-2Nq theta^2/(pi^2(1+q)^2)].

Enlarging the Fourier integral to the real line gives

    max_k Pr(ell=k)
       <=sqrt(pi)(1+q)/(2sqrt(2Nq)).

Here `0<q=q_s<=1/4`. Since pi<4 and `5/(4sqrt(2))<1`, the requested
simple uniform bound follows:

    boxed: max_k Pr(ell=k | E)
       <=1/sqrt(Nq_s)=(s+2)/sqrt(2t+1).                 (3)

It is harmless when the right side exceeds one. In particular the
single-part case N=1 is included.

## 4. The exact depth-L core-size identity

At arbitrary depth s put j=s+1. For t>=1, the Narayana count gives

    P_s(|E|=t)
      =1/[t Z_s] sum_(b=1)^t binom(t,b)binom(t,b-1)
                                x_s^t y_s^b.

Let B have binomial distribution with t trials and success probability
`p=1/(j+1)`. The displayed powers give the exact identity

    boxed: P_s(|E|=t)
       =1/[t(j+1)] sum_(b=1)^t Pr(B=b)Pr(B=b-1).         (4)

For completeness the standard binomial maximal-atom bound follows by
the same Fourier argument: its characteristic-function modulus is

    [1-4p(1-p)sin^2(theta/2)]^(t/2)
       <=exp[-2tp(1-p)sin^2(theta/2)].

The Gaussian integral then gives

    max_b Pr(B=b)
       <=sqrt(pi)/(2sqrt(2tp(1-p)))
       <=1/sqrt(2tp(1-p)).

Bounding one factor in the sum in (4) by this maximum, and summing
the other factor to at most one, proves

    boxed: P_s(|E|=t)<=1/[sqrt(2j)t^(3/2)].               (5)

The t=0 case is not covered by (5) and does not need to be: its exact
mass is 1/Z_s. The joint-profile hypothesis below has a_L>=1.

## 5. Joint size probabilities and conditioning back to fixed r

Fix r>=1 and a profile prefix `a_0=r,a_1,...,a_L` satisfying

    a_j>=r/[2(j+1)],       0<=j<=L.                     (6)

In particular each a_j is a positive integer. Under P_0, start with
the depth-L word and disintegrate successively into its parents.
The reverse chain uses the exact kernels (2): all still deeper words
are deterministic functions of the current child, so there is no
extra conditioning on them.

At each step s, the probability of prescribing the parent size a_s,
uniformly in the complete child of size a_(s+1), is at most (3).
Therefore

    P_0(|D_s|=a_s for 0<=s<=L)
       <=P_L(|E|=a_L)
           product_(s=0)^(L-1) (s+2)/sqrt(2a_(s+1)+1).

From (5)-(6),

    P_L(|E|=a_L)<=2(L+1)r^(-3/2),

and each factor in the product is at most
`(s+2)^(3/2) r^(-1/2)`. Hence

    P_0(the prescribed prefix)
       <=2(L+1)((L+1)!)^(3/2) r^(-(L+3)/2).              (7)

Conditioning P_0 on |D|=r produces exactly the uniform Dyck_r law,
since y_0=1. Its conditioning probability is

    P_0(|D|=r)=Cat_r/(2*4^r)>=1/(8r^(3/2)).              (8)

Here is a finite elementary proof of the bound: if
`c_r=binom(2r,r)/4^r`, then c_1=1/2 and

    c_(r+1)/c_r=(2r+1)/(2r+2)>=sqrt(r/(r+1)),

because the squared comparison differs by one in the numerator.
Thus `c_r>=1/(2sqrt(r))`, and (8) follows from r+1<=2r.

Dividing (7) by (8) proves

    boxed: Pr_Dyck_r(r_j=a_j for 1<=j<=L)
       <=16(L+1)((L+1)!)^(3/2) r^(-L/2)
       <=16(L+1)((L+1)!)^2 r^(-L/2).                    (9)

This is the requested finite joint-profile atom estimate. An
infeasible profile has probability zero, so no separate feasibility
assumption beyond the stated positive-size use is needed for the bound.

## 6. Scope

All steps are exact for the auxiliary probability law and its original
pruning chain. The proof does not assume independence of profile sizes,
does not apply a fixed-size composition law after imposing new size
constraints, and does not use a dynamically reached-root distribution.
The Boltzmann normalization is divided out explicitly only once, in (8).

Equation (9) is a second, distinct anti-concentration tool. The separate
every-third conditional-law proof supplies a different interface and
supports the stronger profile-sieve analysis. Neither atom bound alone
is a period estimate or a proof of exact equality.
