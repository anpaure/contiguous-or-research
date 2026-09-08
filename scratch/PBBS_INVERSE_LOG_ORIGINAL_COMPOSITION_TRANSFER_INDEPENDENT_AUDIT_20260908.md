# Original finite-composition transfer for the inverse-log clock bound

2026-09-08. Independent pure-proof audit of the finite-row and physical
transfer in USER_PBBS_INVERSE_LOG_CLOCK_CLAIM_20260908.md.
No mathematical program was run.

**Verdict:** the transfer is valid for the ORIGINAL unconditioned
composition rows given the full profile. With kappa=2^-40 it gives the
global conditional bounds

    Pr(T<=H | Pi)
      <=2^73 exp(2^18+55) (b+1)^2 Q^2/sqrt(r),

    E[(T+2)1{T<=H} | Pi]
      <=2^74 exp(2^18+55) (b+1)^3 Q^2,                         (1)

for every r>=1,b>=1 and integer0<=H<=b sqrt(r).
In particular the common conservative constant

    K_mu=2^100 exp(2^18+64)

is valid. The geometric budget estimate used in this transfer is proved in
GEOMETRIC_CLOCK_FINITE_PGF_AND_PREFIX_RESTART_INDEPENDENT_AUDIT_20260908.md.
This audit subsequently read that complete proof and independently passed
its Wronskian, nonlinear comparison, half-PGF, prefix restart, and
C_budget constants. It does not replace that theorem with an assumption
about independent entries in a finite composition.

## 1. Sources and exact parameter match

The original-row law and finite physical recurrence are the established
ones in

* PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md, sections2–6;
* PBBS_QUANTITATIVE_CUTOFF_UNIFORMITY_AND_EXPLICIT_CONSTANTS_INDEPENDENT_AUDIT_20260908.md,
  especially sections2–4 and its numerical energy estimates; and
* review/COEFFICIENT_ONE_REVIEW_20260908/sources/essential/c69c/research_round1/pbbs_quantitative_clock_polylog_short_mass.md,
  section4, together with its physical original-clock structural source.

All scratch references above are in the current workspace's scratch
directory. The exact structural source is also retained at
/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_gaussian_clock_genealogy_structural_audit.md.

Condition on the FULL ORIGINAL pruning profile Pi. Write

    a_s=r_s,    ell_s=a_s-2a_(s+1)+a_(s+2),
    P_s=2a_(s+1)+1.

The original row s is a uniform weak composition of ell_s into P_s
parts, and different rows are independent under this conditioning.
Therefore

    N_s=ell_s+P_s-1=a_s+a_(s+2),
    pi_s=(P_s-1)/N_s=2a_(s+1)/(a_s+a_(s+2)),
    q_s=ell_s/N_s=1-pi_s.                                  (2)

These are EXACTLY the geometric theorem's parameters.

In particular P_s is not the free-slot count2a_(s+1)-s that occurs
after conditioning the different candidate-incidence construction on
a zero triangle. No candidate-fibre shift, lifetime weighting, or
sampled-edge Palm condition is imposed on the rows used in (2).

## 2. One finite row versus its geometric row

Let ell>=0 and P>=2 be integers, put N=ell+P-1, and fix1<=n<=P-1
distinct row coordinates. Their sum W has the exact distribution

    Pr_comp(W=w)
       =binom(n+w-1,w)
          (ell)_w (P-1)_n /(N)_(n+w),      0<=w<=ell,          (3)

where factorials fall. This is the usual two-stage weak-composition
count: first compose w into n coordinates and ell-w into the other
P-n coordinates, then divide by the total composition count.

Factor the denominator as

    (N)_(n+w)=(N)_w (N-w)_n.

Because w<=ell and n<=P-1,

    (ell)_w/(N)_w<=(ell/N)^w,
    (P-1)_n/(N-w)_n<=((P-1)/(N-w))^n.

Each comparison follows by bounding the corresponding falling-factorial
ratios term by term; their numerators never exceed their denominators.
For the sum of n independent geometrical variables with probabilities
Pr(Z=j)=pi q^j, pi=(P-1)/N and q=ell/N, this proves

    Pr_comp(W=w)
       <=Pr_geom(W=w)(1-w/N)^(-n).                          (4)

For w<=N/2,

    Pr_comp(W=w)<=Pr_geom(W=w) exp(2nw/N).                   (5)

If ell=0 both sums are zero deterministically, and the comparison has
factor one. A path with w>ell is impossible under the composition and
has zero mass, so only the feasible w need be compared.

## 3. Conditional path probabilities, without an adaptive-row error

The original clock recurrence queries

    n_s=s+1+2 sum_{j<s}(s-j)W_j

coordinates in row s. This number depends only on earlier rows, not
on W_s or any unexamined coordinates in row s.

For a prescribed mass path w_0,...,w_(d-1), the number n_s is therefore
fixed when row s is exposed. The same recurrence defines the geometric
comparison process. Conditional independence across ORIGINAL rows makes
the two path probabilities products of their respective row probabilities.
There is no adaptive stopping inside a currently sampled row.

If sum_s w_s<=M, then

    n_s<=(2M+1)(s+1).

Under the .99 profile bounds, N_s>=r/(s+2). Assuming the finite guards
checked below, (5) consequently bounds the logarithm of the total
likelihood factor by

    sum_{s<d} 2n_s w_s/N_s
      <=2(2M+1)M d(d+1)/r
      <=4M(M+1)(d+1)^2/r.                                (6)

One sums (6) only over composition-feasible paths. Enlarging that sum
to every geometric path of mass at most M is an upper bound, not an
assertion that those added paths are physically possible.

## 4. A numerical legal depth and the profile domain

Put R=sqrt(r), B=(b+1)Q, and choose

    kappa=2^-40,    d=floor(kappa R/B).

The independently established geometric height bound is

    h>=c_h R/Q,       c_h=2^-25.

The existing geometric profile depth with kappa_g=2^-24 has relative
error at most3delta_(kappa_g)<21/2^18<.01.
Since the new d is smaller, whenever d>=2 it supplies

    .99 r/(s+1)<=a_s<=1.01 r/(s+1),   0<=s<=2d+1.             (7)

It also ensures every relevant original core is nonempty.
Alternatively, directly using the smaller kappa in the same envelope
estimate gives even stronger margins.

Set M=ceil(H/h). The height bound gives

    M+1<=2^25 bQ+2<=2^26 B.                                (8)

For d>=2, the floor gives

    d+1<=3d/2<=3kappa R/(2B).

Substitution in (6) yields

    4M(M+1)(d+1)^2/r
         <=9*2^52 kappa^2
         =9*2^-28<1.                                     (9)

Thus the entire finite-composition likelihood debit is at most e.

## 5. All physical and finite-query guards

These inequalities hold for EVERY summed path of total mass at most M.
For0<=s<d, (7) and d>=2 give

    P_s-1=2a_(s+1)
       >=(99/50)r/(d+1)>=r/d>=BR/kappa.

Also N_s>=P_s-1. The bounds below are therefore uniform in the row.

* Distinct queried coordinates:
  n_s<=2(M+1)d<=2^27 kappa R<P_s-1.

* Small row mass:
  w_s/N_s<=2^26 kappa/R<=2^-14<1/2.

* Even the stronger old composition guard holds:
  n_s+w_s<=3(M+1)d, so
  2(n_s+w_s)<=6*2^26 kappa R<P_s.

* Physical horizon:
  P_s>=BR/kappa>2bR+1>=2H+1.

* Height:
  2d<=kappa R/Q<c_h R/Q<=h.

The original chronological query order is therefore unwrapped and uses
distinct slots. Its forward clock partition is the actual finite
physical partition through depth d, rather than a formal infinite
genealogy.

The partition has1+2V_d terminal T clocks, where V_d=sum_{s<d}W_s.
Each has duration at least2(h-d)+1>=h+1 and is part of the original
clock of duration2T+1. On T<=H,

    (1+2V_d)(h+1)<=2H+1.

This implies V_d<=H/h, and hence V_d<=M. The exact T-length convention,
including its consuming update, causes no omitted additive term.

## 6. The geometric zero path and numerical budget input

Let E=2^18. For every prefix m<=d the already audited energy estimate,
applied at depth m, gives

    sum_{s<m}(s+1) ell_s/(a_s+a_(s+2)+1)>=log m-E

when m>=2. Since the denominator in (2) is smaller, its geometric
q_s is at least this old energy coefficient. Therefore

    Z_m=product_{s<m} pi_s^(s+1)
       <=exp(-sum_{s<m}(s+1)q_s)
       <=exp(E)/m<=2exp(E)/(m+1).

The cases m=0,1 follow directly from Z_m<=1. Thus

    C_Z=2exp(E)                                               (10)

is valid, with no use of a shifted or conditioned composition law.

The finite geometric-clock theorem in
GEOMETRIC_CLOCK_FINITE_PGF_AND_PREFIX_RESTART_INDEPENDENT_AUDIT_20260908.md
supplies

    Pr_geom(V_d<=M)<=C_budget (M+1)/(d+1),
    C_budget=64 exp(54) C_Z
            =2^7 exp(E+54).                                (11)

This is the exact point at which that theorem is used. The transfer
does not assume a uniform geometric approximation to all row entries.
Only (3)–(9) compare the two actual finite path probabilities.

## 7. Conditional polynomial clock cost, including d<2

For d>=2, (9), (11), and the physical implication V_d<=M give

    Pr(T<=H | Pi)
       <=2^7 exp(E+55) (M+1)/(d+1).

The useful reciprocal floor bound has no factor two:

    1/(d+1)<B/(kappa R).

Together with (8) and kappa^-1=2^40 this proves

    Pr(T<=H | Pi)
       <=2^73 exp(E+55) (b+1)^2Q^2/R.                     (12)

If d<2, then kappa R/B<2. Hence B^2/R>kappa B/2>=kappa.
The right side of (12) exceeds one, so the trivial probability bound
proves (12) on this complementary sector as well.
No unsafe genealogy is assigned a physical meaning there.

Finally H+2<=(b+2)R<=2(b+1)R. Multiplication in (12) gives

    mu_H(Pi)<=2^74 exp(E+55)(b+1)^3Q^2,                    (13)

proving (1). The proposed larger
K_mu=2^100 exp(E+64) is consequently valid with substantial margin.
The bounds are global in the original profile and include all finite
r>=1 and0<=H<=bR, provided b>=1.

## 8. What this audit does and does not establish

The finite composition law, exact pi_s match, complete path likelihood,
original clock query order, low-budget implication, small-depth fallback,
and numerical conditional constants all pass independently.
They concern the original root law given Pi, before a short-incidence
Palm selection. The downstream terminal/cutoff-support proof must keep
that distinction, as in the existing profilewise argument.

The remaining deductions to dyadic packing, the literal compiler, and
the final inverse-log constant are handled in the root synthesis.
No assertion about an unavailable25374-letter full-cube word, or exact
equality at k=17, is part of this audit.
