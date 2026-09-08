# True Gaussian PBBS rarity does not make raw repair charges negligible

2026-09-07. Pure proof; no computation. This is independent of the
retracted Q6/primitive-height argument. It uses the accepted EXACT
zero-budget product for the true lifetime, with the consuming update
included. Root and a separate analytic auditor checked the new full
local-limit proof; the simpler lower-bound proof below already suffices
to refute the stronger raw census target.

Subsequent positive development: the separate, fully audited note
`PBBS_ZERO_BUDGET_RENEWAL_CLUSTER_PACKING_20260907.md` proves that ALL
zero-budget traces nevertheless have occupied-edge union o(W) and actual
maximum edge-disjoint packing o(W/sqrt(r)). Their raw mass clusters. The
raw lower bounds below remain valid; they are not packing lower bounds.
The still-open full PBBS packing problem concerns positive-budget returns
as well.

## Definitions and accepted exact input

Let Dyck_r be the Dyck words of semilength r, Cat_r their number, and
T(D) the planted rank-r PBBS lifetime, through consumption. Put
W=(2r+1)Cat_r. A normalized root has omitted-label gap 2T+1;
its complement positive residence has T+1 owners and its full repair
trace has T+2 edges. The complete physical factor has 2r+1 copies per
normalized root. These are raw incidence counts, not disjoint packings.

For height h, the previously proved zero-budget identity is

    G_h(x)=sum_(D: T(D)=height(D)=h) x^{semilength(D)}
          =x^h/[F_(m1)(x)F_(m2)(x)F_(m3)(x)],

where F_0=F_1=1, F_m=F_(m-1)-xF_(m-2), and the three indices are
balanced integers with sum 2h+1. Thus m_i/h tends to 2/3. Its positive
factorization and critical value are

    F_m(x)=product_(k=1)^floor(m/2)(1-4q_(m,k)x),
    q_(m,k)=cos^2(pi*k/(m+1)),
    G_h(1/4)=2/product_i(m_i+1)=Theta(h^{-3}).

The exact product's proof is in task05's
`research_round1/pbbs_original_forest_product.md`, Section 5. No
independence after conditioning on semilength is assumed below.

## Elementary fixed-Gaussian-band lower bound

Normalize the coefficients at x=1/4. The resulting size variable N_h
is h plus a sum of independent geometric variables on {0,1,...},
one of parameter q_(m_i,k) per factor. Consequently

    [x^r]G_h(x)=4^r G_h(1/4) Pr(N_h=r).

Fix c>0 and choose constants 0<a<b<min(c,1/2). Isolate one first
geometric mode G, writing N_h=h+G+R. Then G and R are independent,
E R<=h^2 for all sufficiently large h, and 1-q=Theta(h^{-2}) for
the parameter q of G. The mean bound follows from the exact identity
sum_k q_(m,k)/(1-q_(m,k))=m(m-1)/6.

Uniformly for a sqrt(r)<=h<=b sqrt(r), Markov's inequality gives
Pr(R<=r/2)>=1-2b^2>1/2. On that event, for sufficiently large r,
0<=r-h-R<=r. The geometric point probabilities therefore give

    Pr(N_h=r) >= (1/2)(1-q)q^r
               >= c_1 h^{-2} exp(-c_2 r/h^2)
               >= c_(a,b) h^{-2}.

Multiplying by the critical value and summing over the Theta(sqrt(r))
integer heights in this band proves

    #{D in Dyck_r: T(D)=height(D) in [a sqrt(r),b sqrt(r)]}
       >= c_(a,b) 4^r/r^2.

After Catalan normalization the probability is Omega(r^{-1/2}).
The separately audited uniform local-limit theorem strengthens this
to an asymptotic K_(a,b)/sqrt(r), with K_(a,b)>0, for EVERY fixed
0<a<b. The elementary lower bound is enough for all conclusions below.

## Raw count, weighted incidence, and the refuted target

Let I_H be the complete physical family of complement residence traces
with T+1<=H. At fixed H=floor(c sqrt(r)), the preceding band implies

    |I_H| >= c_c W/sqrt(r),
    sum_(I in I_H)|I| >= c_c W,
    sum_(I in I_H)|I|^2 >= c_c W sqrt(r),
    W E(H-T)_+ >= c_c W.

All constants here are positive and may depend on c. These bounds
coexist with the new global theorem Pr(T<=c sqrt(r))->0: the latter
has no rate strong enough to cancel the physical length factors.

More generally, if H_r/sqrt(r) tends to infinity, one FIXED positive
Gaussian band is eventually contained in I_(H_r). Hence

    H_r |I_(H_r)|/W -> infinity.                       (1)

Let A_g(r) count all normalized newborn roots with gap g. Then for
the cutoff used in the historical equation (9.1),

    sum_(3<=g<=2 ceil(sqrt(r log r))) A_g(r)
       >= c 4^r/r^2.

It cannot be o(4^r/(r^2 sqrt(log r))). Thus that STRONGER RAW-COUNT
sufficient target is false. This is a new valid refutation, not a
revival of Q6 and not an inference from a sparse fixed-height example.

## What these lower bounds do not prove

They do not bound the largest EDGE-DISJOINT subfamily from below, the
number of DISTINCT damaged targets, or the unavoidable word repair cost.
Overlapping traces may share a cut, and many failed occurrences may
represent one target. The residence-packing criterion and coefficient
one remain open.

For the always-legal raw erosion word V_H, let mu_H(S) be the number
of intended correct occurrences of target S and F_H(S) the number
whose eroded interval fails. The exact sufficient ledger remains

    actual missing <= #{S: F_H(S)=mu_H(S)}
                   <= D_H:=sum_S F_H(S)/mu_H(S),
    length after target repair <= W+2H Cat_r+D_H.

An unsigned sum over runs cannot be o(W): already the q=0 owner
incidences total W E[(T+1)1_{T+1<=H}]=Omega(W). This does NOT refute
D_H=o(W), because several short coordinates may damage the same owner,
and incidental intervals may supply additional representations.

Complete audited sources in task05's worktree c69c:
`pbbs_zero_budget_gaussian_band_weighted_lower_bound.md`,
`pbbs_gaussian_age_residual_and_cut_charges.md`, and
`pbbs_target_multiplicity_and_erosion_charge.md`. The age/cut path count
J_H means the MINIMUM achievable count or the cited transversal
construction's count, not the count from arbitrary additional cuts.
