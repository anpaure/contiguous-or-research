# PBBS original-coordinate incidence window kernel

2026-09-07. Pure finite proof and a conditional original-slot limit;
no computation. This is the requested first deliverable: the exact
original-coordinate law of a sampled repair incidence and all shifted
short-return events that can cover its sampled edge. It does not prove
a new asymptotic clustering or packing theorem.

Inputs are the accepted original pruning-coordinate bijection and
physical lifetime dictionary in task05's notes. The detailed phase,
signed-time, and incidence proofs are in the companion notes
[original-array shift cocycles](pbbs_original_array_shift_cocycles.md)
and [short-repair incidence law](pbbs_short_repair_incidence_law.md).
All three notes use the same convention: T includes consumption,
the physical omitted-label return gap is 2T+1, and the full repair
trace has T+2 edges.

## 1. Sampled incidence and the original environment

Fix semilength r and an integer 1<=H<r. The intended application is
H=floor(c sqrt(r)) for fixed c>0. Write n=2r+1, W=n Cat_r,
tau=phi^2, and h=h(D). Both height and the full pruning profile are
invariant under tau.

Choose an integer lifetime floor m>=h that is a function of the
pruning profile. Two cases of interest are

    m=h                    for all T<=H births,
    m=h+bcut+1             for T<=H and B=T-h>bcut.

Let A(D)=1{m<=T(D)<=H} and mu=E_D[(T+2)A]. If mu=0 there are no
retained incidences. Otherwise choose a root D with weight (T+2)A,
a uniform one of its n physical phases u, and a uniform offset
j in {0,...,T+1}. Every admissible triple (D,u,j) has probability
1/(W mu).

In the literal complement-birth phase, let B be the rank-r state at
the omitted-label gap start, and let

    e_d : (f^(2d-1)B)^c -> (f^(2d+1)B)^c.

Birth d has root tau^d D. Its repair interval is
e_d,...,e_(d+T(tau^d D)+1), including both boundary edges.
The sampled edge is e_j. All integers d here are physical birth
shifts. A repeated rooted shape does not identify distinct births.

The original root is represented uniquely by a feasible pruning
profile R and its arrays Z_s. At level zero put

    p=2r_1+1,   ell=r-2r_1+r_2,
    sum_(i=0)^(p-1) Z_(0,i)=ell.

Given R, the arrays at the nonempty-core levels are independent
uniform weak compositions. Let y denote ALL original arrays at
levels s>=1. Fixing (R,y) fixes the complete original reduced
omitted-site trajectory lambda_1(t), for every integer t, independently
of Z_0. Negative t are inverse times on this same labelled process.

The companion cocycle note gives this trajectory directly from the
original arrays. In particular its signed visit-count recursion is

    lambda_s(t)=C_s(lambda_(s+1)(t))
                 +M_(s+1,lambda_(s+1)(t))(t) mod (2r_s+1),

where C_s uses original incoming gaps. The signed count M_j(t) is
sum_(0<=u<t) 1{lambda(u)=j} for t>=0, and
-sum_(t<=u<0) 1{lambda(u)=j} for t<0; the inverse-time sum includes
update t with a minus sign. At the bottom,
lambda_(h-1)(t)=t mod (2r_(h-1)+1). Every pruning level uses the same
physical time. Thus the original particle label selected at birth d
is a_d=lambda_1(2d), not generally -d.

For h=1, T=r, so A is empty under H<r. Hence all positive-mass
conditioning below has h>=2 and p>=3.

## 2. Exact lifetime windows are single-coordinate intervals

For any integer d and integer t>=0, define from the fixed deeper data

    a_d=lambda_1(2d) mod p,
    N_d(t)=#{1<=u<=2t+1 :
                 lambda_1(2d+u)=a_d-1 mod p}.             (1)

The signed-time recursion makes (1) meaningful at negative d.
The exact predecessor-count criterion is

    T(tau^d D)<=t  iff  N_d(t)>=2 Z_(0,a_d)+2,             (2)

for 0<=t<=H. Its only spatial-window requirement is
2H+1<n; there is no requirement 2H+1<p. At t=0 both sides of
(2) are false, since N_d(0)<=1.

Consequently, for 1<=L<=H,

    L<=T(tau^d D)<=H
      iff floor(N_d(L-1)/2) <= Z_(0,a_d)
                              <= floor(N_d(H)/2)-1.      (3)

The lower endpoint follows by NEGATING T<=L-1; the floor in (3)
is valid for both odd and even predecessor counts. The upper
endpoint includes the physical return at time 2H+1.

Define I_d(L,H) to be the integer interval in (3). Set it empty
when L>H, or when its lower endpoint exceeds its upper endpoint.
Every nonempty such interval is a subset of {0,...,H-1}.
These are exact lifetime predicates, not merely the necessary
shifted triangular obstruction.

## 3. Conditional incidence law on the original level-zero fiber

Now also fix the sampled offset j, with 0<=j<=H+1. Define

    L_base=max(m,j-1,1),
    I_base=I_0(L_base,H).                                (4)

The condition that this base incidence is retained and reaches e_j
is exactly Z_(0,0) in I_base, since a_0=lambda_1(0)=0.

After the physical phase is marginalized out, the incidence atom law is

    Pr_inc(R,y,Z_0,j)
      = 1{Z_(0,0) in I_base}/(Cat_r mu),                 (5)

for feasible Z_0 with sum ell. Therefore, conditional on a
positive-mass environment (R,y,j), Z_0 is a UNIFORM weak composition
of ell into p parts conditioned on its original coordinate zero
lying in I_base. There is no residual (T+2) weight in this conditional
law: recording j removes that factor and leaves the survival
condition in (4).

For the formal series

    F_I(x)=sum_(z in I, z>=0) x^z,
    F_N(x)=(1-x)^(-1),

the number of admissible compositions is exactly

    Q_base=[x^ell] F_(I_base)(x) (1-x)^(-(p-1)).          (6)

It must be positive before conditioning. The actual environment
law is

    Pr_inc(R,y,j)=Q_base/(Cat_r mu).                     (7)

In particular the deeper arrays have the weighting (7). Their
newborn product law cannot be substituted for this incidence law.

## 4. Every overlapping shifted short repair, including earlier births

The physical cycle period P satisfies P>=2r+1. Since H+2<=P,
all possible retained births covering e_j have distinct physical
representatives in the integer window

    D_j={j-H-1,...,j}.

For d in D_j set

    L_d=max(m,j-d-1,1),
    I_d=I_d(L_d,H).                                     (8)

Then the EXACT congestion at the sampled edge is

    K(D,j)=sum_(d in D_j) 1{Z_(0,a_d) in I_d}.           (9)

The lower threshold j-d-1 is indispensable: a shifted short return
alone can end before the sampled edge. Formula (9) includes the
insertion endpoint d=j and the deletion endpoint d=j-H-1.
It also includes the base birth d=0, whose interval is I_base.

All indices a_d and all intervals I_d in (8) are measurable from
(R,y,j). Thus (9) uses only the original level-zero composition
under the explicit conditioning (4). Arbitrary spatial wraps and
negative birth shifts have already been incorporated into (1).

For a specified finite set S of shifts in D_j, intersect the
intervals I_d for every d in S with a_d=i. At label i=0 also
intersect with I_base. Call the resulting allowed set J_i,
using all nonnegative integers for an unconstrained label.
The exact conditional joint probability that every shift in S
covers the sampled edge is

    Pr_inc(all d in S contribute | R,y,j)
      = [x^ell] product_(i=0)^(p-1) F_(J_i)(x)
        / Q_base.                                      (10)

An empty intersection gives zero. Repeated particle labels create
intersections of constraints on the SAME value, not independent
tests.

The chosen shifts in (10) may be functions of (R,y,j). If they
inspect the remaining Z_0 coordinates, their selection event
must also be included; (10) alone then does not describe the
selected event.

One can record the complete conditional law of K, not just joint
events. Define the deterministic integer-valued functions

    k_i(z)=#{d in D_j : a_d=i and z in I_d}.

Then its probability generating function is the coefficient ratio

    E_inc[v^K | R,y,j]
      = [x^ell] (
           sum_(z in I_base) x^z v^(k_0(z))
         ) product_(i=1)^(p-1) (
           sum_(z>=0) x^z v^(k_i(z))
         ) / Q_base.                                   (11)

All sums are formal in x, so only z<=ell matters. In (11),
k_0(z)>=1 on I_base because d=0 contributes. Hence K>=1 on
this conditioning, as required. For 0<=v<=1 the same formula
also gives the reciprocal moment by integrating v^(K-1):

    E_inc[1/K | R,y,j]
      = integral_0^1 E_inc[v^K | R,y,j] dv/v.            (12)

The apparent endpoint at v=0 is harmless because K>=1.
Equations (7), (11), and (12) are an exact finite expression
for the needed incidence reciprocal under original coordinates.

## 5. A valid conditional geometric law for untouched original slots

There is a limited probabilistic simplification of this kernel.
Consider any sequence of positive-mass environments (R,y,j) with

    p->infinity,  ell/p->rho in (0,infinity),  H=o(p).

For any fixed k distinct NONZERO particle labels selected using
only (R,y,j), their level-zero coordinates converge jointly in
total variation to independent geometric variables on the
nonnegative integers with

    Pr(G=a)=(1-q)q^a,   q=rho/(1+rho).                  (13)

This convergence is uniform over every positive-mass base interval
I_base contained in {0,...,H}. The interval can have probability
tending to zero under the original unconditioned composition law.

Proof. Given Z_(0,0)=z, the other n'=p-1 coordinates form a uniform
weak composition of M=ell-z. For specified values x_1,...,x_k
with s=sum x_i, and eventually n'>k, their exact mass is

    binom(M-s+n'-k-1,n'-k-1) / binom(M+n'-1,n'-1)
      = (n'-1)_k (M)_s / (M+n'-1)_(s+k),                (14)

with falling factorials; it is zero if s>M. Since H=o(p),

    sup_(0<=z<=H, z<=ell) |(ell-z)/(p-1)-rho| -> 0.

Thus (14) converges uniformly on each finite set of vectors to
(1-q)^k q^s. Exchangeability gives
E[sum X_i | z]=kM/n', uniformly bounded by kC for some C.
Markov's inequality controls the tail sum>R by kC/R uniformly
in z. The limiting geometric vector has the corresponding tail
bound k rho/R. Finite-set convergence followed by R->infinity
proves uniform total-variation convergence. Mixing over any
positive-mass conditional law of z preserves the bound. This
proves (13).

On a profile with ell/p->1/3, q=1/4. The argument above alone is
conditional; the quantitative original-profile theorem and the
incidence reduction in Section 9 below now justify removing bad
profiles and mixing this limit under the actual incidence law.
This does not supply a fresh law at a reached root. It concerns
finitely many untouched ORIGINAL slots.
It does not control the potentially growing collection in (9),
the visit-count intervals themselves, or labels chosen after
examining these level-zero values.

## 6. Occupied support and the precise unresolved estimate

Let U_A be the occupied physical edge union. Exact incidence
counting gives

    |U_A|/W = mu E_inc[1/K].                            (15)

For all Gaussian-short births the currently accepted newborn
bound gives only mu_H=o(H), so mu_H can still diverge. Proving
K->infinity in incidence probability alone would not settle
(15) unless mu were bounded. The needed assertion is the
PRODUCT mu E_inc[1/K]->0, or an equivalent estimate.

The accepted coordinator note
/Users/amir.nuriyev/Documents/problem/scratch/PBBS_NEAR_GAUSSIAN_BUDGET_SHARED_REPAIR_20260907.md
already handles every B<=J_r with
J_r=Theta(sqrt(r/log r)), without a lifetime cutoff.
Its two inputs must be kept separate:

* The B=0 occupied union is o(W), although its raw incidence
  remains of order W.
* The 0<B<=J_r raw incidence is o(W), hence so is its occupied
  union.

Therefore the all-short and residual B>J_r occupied unions differ
by o(W). They need not have close incidence-sampling laws: the
removed zero-budget raw mass need not be negligible. For
positive-short births versus B>J_r births, the incidence laws
are close when the positive-short normalizer is bounded below,
because the removed POSITIVE raw incidence is o(W).

Taking m=h+J_r+1 in this note gives the exact kernel for the
remaining sector. Its missing asymptotic input is control of
the environment law (7) and of the weighted reciprocal in
(11)-(15). No lower bound on the number of effective shifted
intervals, no growing-lag renewal statement, and no asymptotic
cluster conclusion is claimed here. The coefficient-one
conjecture remains open.

## 7. A checked limit on deterministic reduced-leaf transfer

Task05's note
/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_reduced_leaf_lift_obstruction.md
gives a symbolic obstruction that is visible directly in this kernel.
For K>=0 and M>2K, let

    D_(K,M)=1(10)^(M+1)0(10)^K.

It has r=K+M+2, height two, reduced root 10, and original level-zero
array (K,0,M). Its reduced trajectory is lambda_1(t)=t mod 3.
The original return gap is 6K+5, so T=3K+2. Its first-level clock
partition contains 2K+1 reduced T leaves, each of length three,
starting at physical times 3q-1 for q=1,...,2K+1.

At every such start the selected original particle is label two,
whose incoming-gap coordinate is M. The original newborn at that
phase has T>=M+1: a return by time 2M+1 could not contain the required
2M+2 predecessor selections. In the same projected birth phase,
the corresponding shifts are d=3a+1 for a=0,...,K. Formula (9)
reads Z_(0,2)=M at each of these shifts and correctly excludes
them whenever H<M+1.

Taking K->infinity and M/K^2->infinity makes the outer T Gaussian-short
while every proposed original lift at these leaf starts is long.
Thus reduced short leaves cannot be transferred deterministically
to short original births at their starting phases. The source
also checks the role word (P R S)^K P C, giving rho=sigma=K.

These examples have height two and p=3; they do not satisfy the
regular-profile assumptions of Section 5. No incidence mass,
overlap failure, packing obstruction, or absence of short births
at other shifts follows. The stated choice of M/K^2 also does not
by itself guarantee B>J_r. The finite source and this kernel
interpretation passed a separate independent read-only audit.

## 8. A checked limit on S-created newborn lifetime comparison

A second finite example is in task05's note
/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_s_created_newborn_lifetime_obstruction.md.
To avoid using H both for a word and a cutoff, write here

    A=10,   Q=1100,   V_b=1A^(b+1)0,   D_b=V_b Q,
    b>=1.

The unmarked roots follow the exact five-cycle

    V_b Q -> Q Q A^b -> Q A^b Q -> A^b Q Q -> Q V_b -> V_b Q.

An old mark planted in the first transition has roles S P S C
and lifetime four. The newborn beta created at its first S update
has roles

    S P S (R S S P S)^b C

and lifetime 5b+4. The preliminary S P S moves beta to the last
inner leaf of V_b; each subsequent five-step block moves it one
leaf left, until consumption at the first inner leaf.

The precise intermediate position in A^b Q Q is the first up-step
of the FIRST Q, which supplies the stated P role. Two independent
readers identified a second-Q positional typo in the source.
Task05 corrected it, and its Gaussian reader independently passed
the full trace with the first-Q position.

In birth-root notation, T(D_b)=4 while T(tau D_b)=5b+4. The roots
have height two and semilength b+4. Hence no universal upper bound
for every S-created newborn follows from the old lifetime and
height alone. For fixed Gaussian cutoff and large b, the old
birth is short while this immediately subsequent birth is long.
The example refutes equality and the upper comparison T_new<=T_old;
opposite survival-order and lower-overlap questions remain open.

The old budget is two, so this particular old run lies in the
already handled B<=J_r sector for large r. The example supplies
no residual incidence-mass, support, or packing obstruction.
It also does not rule out a statement about a suitable fraction
of S-created newborns. Both upper lifetime control and survival
through the sampled edge still require proof before such births
can be counted in (9).

## 9. Quantitative profile elimination closes the first-level gap

The follow-up note
[original-profile incidence reduction] (historical local link not bundled)
now supplies the missing quantitative regular-profile step. Its
stronger form uses the coordinator's critically checked theorem
/Users/amir.nuriyev/Documents/problem/scratch/PBBS_ORIGINAL_PROFILE_CONCENTRATION_20260907.md.
With n=2r+1, there is an explicit ORIGINAL-profile event G_star with

    Pr_D(G_star^c)<=4/(n+1)^10,
    p/n=1/2+O(sqrt(log n/n)),
    ell/p=1/3+O(sqrt(log n/n))

uniformly on G_star. For every retained A=>T<=H, H<r, its bad-profile
raw incidence and occupied support divided by W are at most
2/(n+1)^9. This discards bad profiles independently of mu_A.

The full profile is phi/tau invariant, so this restriction removes
whole physical components. Exactly,

    K_(A intersect G_star)(e)=1_(G_star(e)) K_A(e).

For A_(m,H), H=o(r), and any subsequence mu_A>=epsilon>0, Section 5
therefore yields an actual-incidence joint total-variation limit:
any fixed number of distinct nonzero original level-zero slots chosen
using (profile, deeper arrays, sampled offset) tend to iid geometric
variables with mass (3/4)(1/4)^a at a. The selected finite slot vector
also decouples from that environment in total variation, while the
environment keeps its actual incidence-weighted law. If mu_A->0,
the occupied-support problem is already negligible directly.

This resolves the profile marginal issue mentioned in Sections 5-6.
The deeper-array law, effective shifted intervals, and the weighted
reciprocal mu_A E_inc[1/K_A] remain uncontrolled. No growing number
of slots or new clustering conclusion is asserted.

## 10. A finite deeper-visit reciprocal decomposition

The follow-up
[deeper-visit score decomposition] (historical local link not bundled)
now gives an explicit sufficient target on the remaining actual
environment law. Group the exact intervals by nonzero original label,
using U_i=union_(d:a_d=i) I_d. Then K>=1+sum_i 1{Z_(0,i) in U_i}.
For each feasible base value z, let Gamma_z be geometric with parameter
(ell-z)/(ell-z+p-1), and define

    Lambda_*(E)=min_(z in I_base intersect {0,...,ell})
                     sum_(i=1)^(p-1) Gamma_z(U_i).

The other composition coordinates are EXACTLY independent Gamma_z
variables conditioned on their fixed total. Paying an elementary
conditioning cost yields a finite reciprocal bound. For H=o(r),
only o(p) labels are queried, and the
[constant-density addendum] (historical local link not bundled)
bounds their marginal density by 80 times the z-dependent independent
reference. Integration on GOOD therefore gives

    |U_A|/W <=nu_BAD+nu_low(L)
                +mu/(1+L/2)+80mu exp(-L/8),

where nu_low(L) is the RAW incidence weight of GOOD environments
with Lambda_*<L. Thus mu/L_r->0 and nu_low(L_r)->0 suffice,
without a separate logarithmic threshold. No new law for those
environments or estimate of this raw low-score mass is asserted.

A direct signed-time certificate counts distinct nonzero labels with
some shift satisfying L_d<=H, N_d(L_d-1)<=1, and N_d(H)>=2.
Every such label has 0 in U_i; on GOOD the score is at least two
thirds of this count. Both lifetime bounds and the sampled-edge
survival requirement remain in L_d. The detailed note proves all
normalizers and constants and records the still-unproved low-score
incidence target. This is a finite conditioning argument, not a
growing-slot independence limit.

The accepted fixed-c bound mu_H=O_c(sqrt(log r)) now permits score
threshold L_r=(log r)^(3/2). For the residual B>J_r family, the proved
reduction makes

    nu_low((log r)^(3/2))=o(1/sqrt(log r))

a sufficient still-UNPROVED packing target. It would give occupied
support o(W/sqrt(log r)); dividing by the minimum residual trace
length of order J_r=Theta(sqrt(r/log r)) gives packing o(W/sqrt r).
Adding the accepted low-budget packing bound would complete the
fixed-Gaussian packing step. Mere nu_low=o(1) does not supply this
packing rate by the same argument. No growing-c or full-coefficient
conclusion is asserted.

Review record: independent audits passed the lifetime-window floors,
conditional composition and environment laws, repeated-label grouping,
congestion generating function, reciprocal integral, and the uniform
untouched-slot lemma. A separate phase/reduction audit passed Sections
1 and 6. Its signed-time wording clarification is incorporated above.
Task05's lead also fully read and passed the note, including the lower
threshold floors, physical offsets, cancellation of the length weight,
environment normalization, repeated-label constraints, full generating
function and reciprocal identity, and the rare-base-event slot limit.
Task05's Gaussian agent subsequently completed another independent
full read and passed the companion complement phase, conditioning
normalizers, rare-base-event limit, and weighted-reciprocal scope.
