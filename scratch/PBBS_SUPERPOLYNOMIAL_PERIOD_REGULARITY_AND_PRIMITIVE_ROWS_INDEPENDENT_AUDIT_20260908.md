# Regular pruning profiles and primitive rows for the superpolynomial period claim

2026-09-08. Independent pure-proof audit by `exact_b_induction`.
No mathematical program was run.

Verdict: the required original-profile and primitive-row probability
estimate passes with explicit constants. The small-divisor arithmetic
used to turn these divisors into a long period is a separate root and
`exact_equality_structure` audit.

## 1. Explicit finite statement

All logarithms are natural. Let

    u=log r >= 2^20,
    L=floor(r^(1/6)/u),
    B=r/(L+3)^3,
    Delta=B/100.

Let G be the event that

* `|r_s-r/(s+1)|<=Delta` for every `0<=s<=L+1`; and
* each of the first L original incoming-gap rows is primitive.

Then, for the uniform Dyck root of semilength r,

    boxed: Pr(G^c)<=exp[-2^(-26)(log r)^6].                 (1)

The requested weaker constant `b=2^-28` is therefore valid, without
a polynomial prefactor. On G all `r_0,...,r_(L+1)` are positive and
strictly decreasing. In particular the physical period v has L+1
distinct divisors `n_s=2r_s+1`, `0<=s<=L`, all at most `n=2r+1`, and
v>=n. These deterministic conclusions use the already audited primitive
row period theorem, not independence of the dynamics.

## 2. The finite one-depth concentration input

The exact source is
`scratch/PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md`, section 2,
equation (4). Its finite pruning census, bounded-difference proof on
the uniform slice, and unique-root argument give

    Pr(|r_s-r/(s+1)|>(4+x)sqrt(r))<=2 exp(-x^2/6),

for every s>=0 and x>=0. This is uniform in the depth s, not a
fixed-depth asymptotic statement. No independence across depths is
needed below.

Put A=r^(1/6)/u. Since `exp(u/6)>=u^2/72`, the present domain gives
A>=3, L>=1, and

    L+3<=A+3<=2A.

Consequently

    Delta/sqrt(r)>=u^3/800.

This is at least eight. Taking
`x=Delta/sqrt(r)-4 >= u^3/1600`, the union bound gives

    Pr(profile not regular)
      <=2(L+2) exp[-u^6/15360000]
      <=2(L+2) exp[-2^-24 u^6].

Here 15360000<2^24. Also `L+2<=3exp(u/6)`, so
`log(2(L+2))<=u/6+log6<=u`, and `u<=2^-25 u^6` on the stated domain.
It follows that

    Pr(profile not regular)<=exp[-2^-25 u^6].             (2)

## 3. Every regular row has large mass and length

For row s, `0<=s<L`, put

    ell_s=r_s-2r_(s+1)+r_(s+2),
    p_s=2r_(s+1)+1.

The exact second difference of the deterministic center is

    2r/[(s+1)(s+2)(s+3)].

On the regular event, its error is at most `4Delta=B/25`. Therefore

    ell_s>=2B-B/25>=B.                                   (3)

Also `r_(s+1)>=r/(s+2)-Delta` and
`Delta<=r/[100(L+2)]`, so

    p_s>= (198/100)r/(L+2)>=r/(L+3).                      (4)

Thus `min(p_s,ell_s)>=B`. These cores are nonempty, with p_s>1 and
ell_s>0; the terminal single-part or zero-row exceptions do not occur
on this event.

For strict decrease, at every `0<=s<=L`,

    r_s-r_(s+1)
      >=r/[(s+1)(s+2)]-2Delta
      >=r/(L+3)^2-r/[50(L+3)^3]>0.                       (5)

Finally `r_(L+1)>=r/(L+2)-Delta>0`. This proves all positivity and
distinct-divisor premises explicitly, including the two profile levels
needed by the last tested second difference.

## 4. A uniform exact composition repetition bound

Conditional on the FULL original pruning profile, row s is uniform
over the weak compositions of ell=ell_s into odd p=p_s parts. This
finite law, independent across original rows, is proved in
`/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_gaussian_clock_genealogy_structural_audit.md`,
sections 1 and 2, and checked in
`scratch/PBBS_INVARIANT_GAP_ROW_PERIOD_DIVISIBILITY_INDEPENDENT_AUDIT_20260908.md`.

Write `D=binom(ell+p-1,p-1)`. A nonprimitive row is j repetitions
of a shorter row, for some divisor j>=3 of p. If j does not divide
ell, no such row exists. Otherwise the number of these rows is

    D_j=binom(ell/j+p/j-1,p/j-1).

Concatenating j independently chosen shorter compositions injects
`D_j^j` distinct full compositions into the D possibilities. Thus
`D_j/D<=D^(-2/3)`. A union bound over at most p possible j gives

    Pr(nonprimitive | profile)<=p D^(-2/3).

Let `m=min(ell,p-1)`. Since `D>=binom(2m,m)>=2^m` and
`m>=min(ell,p)-1`, this proves the convenient uniform bound

    Pr(nonprimitive | profile)
       <=2p exp[-(2log2/3) min(p,ell)].                   (6)

This slightly strengthens the proposed repetition bound with an extra
composition-size prefactor. No geometric approximation, typical-row
limit, or condition on a dynamically reached word is used.

## 5. Union over the growing number of rows

On every fixed regular full profile, (3)-(6), `p_s<=n<=3r`, `L<=r`,
and `2log2/3>=1/3` give

    Pr(some first-L row nonprimitive | profile)
       <=2Ln exp(-B/3)
       <=exp(3u-B/3).

The lower bound on B is particularly strong:

    B>=exp(u/2)u^3/8.

For u>=128, the exponential series gives
`exp(u/2)>=u^6/46080>=8u^3`; therefore B>=u^6. Since
`3u<=u^6/12` on our domain,

    Pr(some tested row nonprimitive | regular profile)
       <=exp(-u^6/4).                                   (7)

Every estimate is uniform over the regular profile. Averaging (7) and
adding (2) yields

    Pr(G^c)<=exp(-2^-25 u^6)+exp(-u^6/4)
            <=2exp(-2^-25 u^6)
            <=exp(-2^-26 u^6),

where the last step uses `2^-26 u^6>=log2`. This proves (1).
Independence of different rows was not needed for this union bound;
the exact conditional marginal law of each original row suffices.

## 6. Correct measure and deterministic period consequences

A labelled rank-r binary state of length n=2r+1 has a unique unmatched
zero and hence a unique normalized Dyck root D. Conversely every D
has exactly n distinct labelled rotations: a nontrivial repetition
would divide the total zero-minus-one excess one. Thus uniform physical
middle states correspond to uniform D and a uniform physical root
location, with `W_r=n Cat_r`.

Profile values and primitivity of each original row are unchanged by
physical rotations. Consequently (1) holds under uniform middle states
with exactly the same normalization. There is no additional conditioning
cost and no reweighting by g-cycle size. The period v and height h have
this same rotation-invariant interpretation.

The invariant-row period theorem gives, on G,

    lcm_{0<=s<L}(n_s n_(s+1)) divides v.

In particular each `n_0,...,n_L` divides v, and (5) proves these L+1
divisors are distinct. Each is at most n and the first is n. This is
the precise input to the separate small-divisor lemma. Merely knowing
that they are distinct does not justify replacing the least common
multiple by their product.

The divisor count has no floor loss: `L+1>r^(1/6)/log r`. Since
`r=(n-1)/2>=n/3`, `3^(1/6)<2`, and `log r<log n`, it follows that

    L+1 > (1/2)n^(1/6)/log n.

This is the quantitative count supplied to the small-divisor lemma.

For the height-adaptive word the relative collar charge is exactly
`E[(2h-1)/v]`. On G^c it is at most `Pr(G^c)`, because `v>=n` and
`2h-1<n` everywhere. Thus no additional polynomial probability debit
is introduced when the exceptional event is charged to the word.

## 7. The proposed explicit final threshold is sufficient

Let `k>=ceil(exp(exp(256)))`, and let the odd source dimension be n=k
or n=k-1 according to parity. Then `r=(n-1)/2>=k/4`, giving

    log r>=exp(256)-log4>exp(255)>2^20.

Hence all preceding estimates apply. To separate this audit's scope,
suppose the independently audited small-divisor step gives on G

    log v>=a(log n)^(6/5),   a=2^-24.

Put X=log n. At this threshold `X^(1/5)>=exp(51)>2^25=2/a`, so the
numerator `2h-1<n` is absorbed and the good contribution is at most
`exp[-2^-25 X^(6/5)]`.

The weaker advertised exceptional constant b=2^-28 already gives
`b(log r)^6>=2^-34 X^6`, since `log r>=X/2`. This exceeds
`2^-25 X^(6/5)` on the stated domain. Adding the two contributions
and absorbing the factor two gives `exp[-2^-26 X^(6/5)]`.

Finally `log n>=0.5log k`; the parity conversion loses less than a
factor four in the exponent. Thus the resulting bound has coefficient
at least `2^-28`, and the proposed smaller explicit coefficient
`c=2^-32` is safe. This last paragraph checks the conversion conditional
on the separately audited small-divisor lower bound; it is not a proof
of that number-theoretic lemma.
