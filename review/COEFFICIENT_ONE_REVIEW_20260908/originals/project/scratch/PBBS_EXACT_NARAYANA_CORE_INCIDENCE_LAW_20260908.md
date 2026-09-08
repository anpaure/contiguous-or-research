# Exact Narayana-class law of the exposed core under base incidence

2026-09-08. Pure proof; no computation. Root and independent direct-route
full-file audits passed. This identifies the law after summing the upper fibres. It keeps
the fixed original size and the actual short-clock/offset conditioning.

## 1. Domain and notation

Fix c>0, original size r, H=floor(c sqrt(r))<r, and an integer S>=1.
Use the original family

    F_0={GOOD,T<=H,Z_(0,0)=0},
    mu_0=E[(T+2)1_(F_0)]>0.

The actual incidence atoms (D,j), with 0<=j<=T(D)+1, have mass
1/(Cat_r mu_0). The accepted exact fibre is
`pbbs_finite_layer_zero_triangle_incidence_fibre.md` in worktree c69c.
Write E=D_S, t=|E|, k=pk(E), so r_S=t and r_(S+1)=t-k. The candidate
core clock is the actual chronological C_S^S T_S word from phase zero;
denote its odd endpoint by G_S^*(E), and set T_S^*=(G_S^*-1)/2.

Use the EXACT profile domain (2) of that fibre, together with the zero
triangle F_S=0. For a nonempty core E, this domain is equivalent to

    t>H,                 height(E)>=S.              (1)

Indeed h(D)=height(E)+S. Pruning sizes decrease, so the smallest p_s
for s<S is 2t+1, and p_s>2H+1 is equivalent to t>H. Also height(E)>=S
implies t>=S, hence p_s>=2S+1>=2(s+1) for every s<S. Conversely the
height and last circumference conditions in the fibre imply (1).

Do not additionally condition on the auxiliary sufficient event
L>=max(S,2) used to prove safety. That event can inspect more of the
profile. It is enough that this auxiliary event implies (1), so the
exact domain in (1), together with F_S=0, has actual incidence
probability 1-o(1) for every fixed S as r tends to infinity.

## 2. Integrating the upper profiles exactly

For a candidate upper size sequence r_0=r,r_1,...,r_(S-1), with
r_S=t and r_(S+1)=t-k, set

    ell_s=r_s-2r_(s+1)+r_(s+2),
    M_s=binom(ell_s+2r_(s+1)-s-1, 2r_(s+1)-s-1).

Sum over feasible sequences with ell_s>=0 and the usual decreasing
sizes. On (1), every free-slot count 2r_(s+1)-s is positive, so the
displayed binomial is an ordinary weak-composition count, including
ell_s=0. The inverse-array bijection supplies every such completion.

The specific GOOD condition in
`PBBS_ORIGINAL_PROFILE_CONCENTRATION_20260907.md` depends only on
(r,r_1,r_2): it tests N_1=2r_1+1 and N_2=2r_2+1. Define

    W_(r,S)^GOOD(t,k)
      =sum_(r_1,...,r_(S-1)) 1_GOOD(r,r_1,r_2)
                                product_(s<S) M_s. (2)

For S=1 or S=2 the already specified endpoint sizes supply r_1 or
r_2 where necessary. Every factor in (2) depends only on the summed
upper sizes and (t,k). There is no dependence on the remaining shape
or deeper pruning profile of E. If a different GOOD condition were
allowed to inspect that deeper profile, this conclusion would need
to be revisited.

The exact incidence formula is therefore

    Pr_inc,0(D_S=E,j,F_S=0,domain (1))
       = W_(r,S)^GOOD(t,k)/(Cat_r mu_0)
         *1{t>H, height(E)>=S,
             G_S^*(E)<=2H+1, 0<=j<=T_S^*(E)+1}.    (3)

This follows by summing equation (12) of the accepted fibre over
the upper profiles. Every completion counted in (2) has the same
base clock and permitted offsets by its forward/reverse clock theorem.
No new conditioning on the free upper coordinates remains.

## 3. A precise Narayana-class Palm description

Let D_(t,k) be the set of Dyck roots with t up-steps and k peaks.
For every positive-mass (t,k), conditional on these two values and
the zero-triangle/domain event, (3) gives the following exact law:

    (E,j) is uniform over all E in D_(t,k) and offsets j
    satisfying height(E)>=S, T_S^*(E)<=H,
                         0<=j<=T_S^*(E)+1.          (4)

Equivalently, the marginal core law has density proportional to

    (T_S^*(E)+2) 1{height(E)>=S,T_S^*(E)<=H}         (5)

relative to the uniform Narayana class D_(t,k). Conditional on E,
the offset is uniform on its T_S^*(E)+2 allowed values. Conditional
on a specified j instead, the core is uniform on the class with the
extra survival test j<=T_S^*(E)+1.

For completeness this reference class has an exact elementary sampler.
Choose independently a uniform positive composition of t into k
one-run lengths and a uniform positive composition of t+1 into k
zero-run lengths. Concatenate the alternating runs cyclically and
take the unique canonical Dyck rooting of the cyclic word. The total
numbers of ones and zeros are coprime, so this word has no nontrivial
rotational period. Every rooted Dyck word in D_(t,k) has exactly k
such ordered-run representations, one per one-run start. Thus the
sampler is uniform, and counting its pairs gives

    |D_(t,k)|
      = (1/k) binom(t-1,k-1) binom(t,k-1)
      = (1/t) binom(t,k) binom(t,k-1).              (6)

The canonical rooting is the usual unique cycle-lemma rooting for a
cyclic word with one more zero than one; equivalently rotate first to
D0 with nonnegative proper prefix sums, then rotate its final zero
to the front. More explicitly, start just after the FIRST global
minimum of the cumulative sums. Later partial sums are no smaller;
earlier ones are strictly larger integers, so after wrapping and
subtracting one the proper partial sums remain nonnegative. Conversely
these inequalities force the start to follow that first global minimum.
No extra rooting weight is needed.

Thus (4)-(5) specify a concrete reference distribution and its entire
remaining change of measure. They do NOT say that the actual core is
uniform in its Narayana class before that displayed conditioning.

## 4. The exact inverse-pruning generating-function transform

Fix a nonempty core of size t and k peaks, and prescribe q DISTINCT
incoming-gap coordinates to be zero. If q<=2t, there are 2t+1-q
free coordinates. At total free mass ell, the upper size is t+k+ell
and its peak count is k+ell. Hence its full bivariate preimage sum is

    sum_(ell>=0) binom(ell+2t-q,2t-q)
                      x^(t+k+ell) y^(k+ell)
       =(1-xy)^(q-1)
          [x/(1-xy)^2]^t (xy)^k.                  (7)

This is the weak-composition series. If q=2t+1, all slots are forced
zero and only ell=0 is allowed; the expression on the right still
reduces to x^t(xy)^k. If q>2t+1, counting q distinct forced slots is
impossible, and interpreting the indices cyclically introduces repeats:
the same formula must NOT be used with that q. Empty cores require
their separate bottom-row convention. Neither issue arises on (1).

Put x_0=x,y_0=y,A_0=1, and iterate

    x_(s+1)=x_s/(1-x_s y_s)^2,
    y_(s+1)=x_s y_s,
    A_(s+1)=A_s(1-x_s y_s)^s.                      (8)

Since the row-s triangle has q=s+1 forced slots, repeated application
of (7), from the top row downward, shows that the generating function
of all zero-triangle upper completions of a fixed safe core E is

    A_S(x,y) x_S(x,y)^t y_S(x,y)^k.                 (9)

In particular, with GOOD omitted, their exact fixed-size number is

    W_(r,S)(t,k)
        =[x^r] A_S(x,1) x_S(x,1)^t y_S(x,1)^k.     (10)

The GOOD-filtered number remains exactly (2). Replacing (2) by (10)
without handling GOOD is not an exact operation. Asymptotically at
fixed c it is permitted at the incidence-law level with o(1) total
variation error: the accepted discarded BAD raw incidence is o(1),
while mu_0 is bounded below. The resulting normalization changes by
only that discarded raw mass. The safety/triangle restriction also
has probability 1-o(1) for fixed S.

## 5. Critical evaluation and the fixed-size guard

At x=1/4,y=1, direct induction in (8) gives

    x_S=(S+1)^2/(S+2)^2,
    y_S=1/(S+1)^2,
    x_S y_S=1/(S+2)^2,
    A_S=2(S+2)^(S-1)/(S+1)^S.                     (11)

The formulas include S=0. To verify the scalar, its ratio between
successive S is (1-1/(S+2)^2)^S, as required by (8), and its initial
value is one. Each geometric-series ratio is less than one, so for
a fixed safe core the evaluation is a convergent positive sum:

    sum_r 4^(-r) W_(r,S)(t,k)
                    =A_S x_S^t y_S^k.             (12)

The effective parameters satisfy

    x_S (1+sqrt(y_S))^2=1.                         (13)

For the terminology, let F(x,y) count all Dyck words, including the
empty word. The first-return decomposition 1A0B gives
F=1+xyF+x(F-1)F: A empty contributes a peak, while A nonempty does
not create an additional peak. The quadratic solution analytic at zero
has its first positive discriminant zero at x=(1+sqrt(y))^(-2),
where F=1+sqrt(y). Thus (13) is exactly the algebraic critical Narayana
parameter curve. Its use here requires no probabilistic substitution:
(12) simply sums over ALL possible original upper sizes with weight
4^(-r).

In (10)-(12), W without GOOD is the algebraic completion count. The
clock and domain indicators remain external, exactly as in (3).
In particular the sum in (12) does not reimpose t>H(r) at every r;
doing that would be a different restricted generating function.

For the actual problem, original size r is fixed. The retained weight
is (10), or (2) with GOOD, rather than the right side of (12).
If one starts with the critical completion distribution of (12),
conditioning its original size to equal r introduces precisely the
factor 4^(-r)W_(r,S)(t,k)/(A_S x_S^t y_S^k).
There is no proof here that this factor can be dropped or replaced
uniformly on the clock-conditioned cores.

## 6. What this resolves, and the remaining abundance step

Equations (3)-(5) remove a genuine ambiguity about the actual deeper
environment: once its size and peak count are fixed, every hidden
upper-profile weight is constant on that Narayana class. The only
remaining shape dependence is the explicit height and chronological
C_S^S T_S clock/offset test. Equation (6) supplies an elementary
reference sampler for that class. These statements are exact at fixed
r,S, with the scope in (1), rather than an unconditioned Boltzmann
model asserted to be the actual environment.

They do not yet prove an abundance bound. In particular the short
C_S^S T_S test may correlate with the moving labels and all partner
clock tests inside the same core. Uniform run compositions before
canonical rooting and before (5) do not make those reached tests fresh.
To deduce J-divergence one still needs a quantitative statement about
eligible PHYSICAL phases under the explicit Narayana-class Palm law
(4), followed by its actual (t,k) mixture. No such recurrence or
divergence statement is asserted here.
