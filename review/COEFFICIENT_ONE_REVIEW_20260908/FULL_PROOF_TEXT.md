# Full proof text for external review

Proposed coefficient-one proof; internal AI-agent review only. No external or formal verification. This file contains unabridged source documents; local navigation links are made portable. Exact original bytes are in `originals/`. Historical status statements are preserved and must be read in their chronology. Required external theorem: Kuniba–Sakamoto arXiv:nlin/0611046v2, Theorem 5.1; see README.md.

## Contents

1. [COEFFICIENT_ONE_PROOF_20260908.md](#document-01)
2. [COEFFICIENT_ONE_CONSTRUCTION_20260908.md](#document-02)
3. [PBBS_COMMON_DEEP_BOUNDARY_ELIGIBILITY_BY_GROWING_DEPTH_FLUX_20260908.md](#document-03)
4. [PBBS_ACTUAL_COMMON_BOUNDARY_SHIFTED_TRIANGLE_RENEWAL_20260908.md](#document-04)
5. [PBBS_STATIONARY_CORE_CLOCK_FLUX_AND_RELAXED_DEPTH_ABUNDANCE_20260908.md](#document-05)
6. [PBBS_EXACT_NARAYANA_CORE_INCIDENCE_LAW_20260908.md](#document-06)
7. [PBBS_ORIGINAL_ARRAY_CONE_RENEWAL_20260908.md](#document-07)
8. [PBBS_ORIGINAL_PROFILE_CONCENTRATION_20260907.md](#document-08)
9. [PBBS_EXACT_ALL_DEPTH_PRUNING_CENSUS_20260907.md](#document-09)
10. [PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md](#document-10)
11. [PBBS_SQRTLOG_GAUSSIAN_SHORT_INCIDENCE_20260907.md](#document-11)
12. [PBBS_TOP_ZERO_ALL_SHORT_OVERLAP_REDUCTION_20260908.md](#document-12)
13. [PBBS_TWO_ROW_VIRTUAL_ZERO_CLOCK_REDUCTION_20260908.md](#document-13)
14. [PBBS_SAME_PARTICLE_SHORT_TRACE_MULTIPLICITY_20260907.md](#document-14)
15. [PBBS_TRUE_GAUSSIAN_RAW_CENSUS_OBSTRUCTION_20260907.md](#document-15)
16. [PBBS_CROSS_CUTOFF_OCCUPIED_SUPPORT_REDUCTION_20260908.md](#document-16)
17. [PBBS_OCCUPIED_SUPPORT_TO_PACKING_20260908.md](#document-17)
18. [PBBS_ABUNDANCE_TO_COEFFICIENT_ONE_VERIFIED_COMPILER_CHAIN_20260908.md](#document-18)
19. [PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md](#document-19)
20. [PBBS_PEAK_DELETION_PASSAGE_RECURSION_20260725.md](#document-20)
21. [PBBS_PEAK_SPACING_AUDIT_20260725.md](#document-21)
22. [PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md](#document-22)
23. [MATH_THEOREM_PBBS_EXACT_RUN_SPECTRUM_FLAT_ANTECEDENT_NOGO_AND_FULL_UPPER_DECK_20260813.md](#document-23)
24. [MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md](#document-24)
25. [PBBS_GENERAL_MARK_LADDER_AUDIT_20260725.md](#document-25)
26. [MATH_AUDIT_PBBS_FIRST_SHADOW_THEOREM_20260726.md](#document-26)
27. [MATH_THEOREM_O_PRODUCT_SCD_TAIL_MIXED_CYCLE_INTERFACE_20260726.md](#document-27)
28. [MATH_AUDIT_PBBS_SUBROOT_BAND_AND_PRODUCT_SCD_QUANTIFIER_20260726.md](#document-28)
29. [PBBS_K17_FINITE_COMPILER_LEDGER_20260908.md](#document-29)
30. [pbbs_finite_layer_zero_triangle_incidence_fibre.md](#document-30)
31. [pbbs_uniform_early_triangle_incidence.md](#document-31)
32. [pbbs_gaussian_clock_genealogy_structural_audit.md](#document-32)
33. [pbbs_stationary_lifetime_identities.md](#document-33)
34. [pbbs_quantitative_clock_polylog_short_mass.md](#document-34)
35. [pbbs_zero_budget_gaussian_band_weighted_lower_bound.md](#document-35)
36. [pbbs_original_forest_product.md](#document-36)
37. [pbbs_uninterrupted_record_peeling.md](#document-37)
38. [pbbs_q6_independent_audit.md](#document-38)
39. [pbbs_original_array_shift_cocycles.md](#document-39)
40. [pbbs_original_incidence_window_kernel.md](#document-40)
41. [pbbs_short_repair_incidence_law.md](#document-41)


---

<a id="document-01"></a>

## Document 01: COEFFICIENT_ONE_PROOF_20260908.md

Source: `/Users/amir.nuriyev/Documents/problem/COEFFICIENT_ONE_PROOF_20260908.md`

[Portable document](MANUSCRIPT.md) · [Exact original](originals/project/COEFFICIENT_ONE_PROOF_20260908.md)

<!-- BEGIN COMPLETE SOURCE 01 -->

# Coefficient one for complete interval-union words

**Status: proposed proof with AI-agent internal reviews. It has not been
externally reviewed or formally verified. No gap was found in the current
reviews; their PASS labels must not be read as independent human certification.**

2026-09-08. Consolidated proof with supporting finite lemmas linked below.
The two new main lemmas and the passage through the existing literal word
compiler have passed root, direct-route and appendix mathematical audits.
This is a proof manuscript, not a formal proof-assistant certificate.
No mathematical computation was used in this PBBS proof. The manuscript
was recorded in MASTER_HANDOFF.md, Section 9.2, on 2026-09-08 as a proposed
proof [P], retaining the review status above.

## Theorem

Let nu(n) be the minimum length of a word of nonempty subsets of [n]
whose nonempty contiguous interval unions include every nonempty subset
of [n]. With W(n)=binom(n,floor(n/2)),

$$
\boxed{\displaystyle \nu(n)=(1+o(1))\binom{n}{\lfloor n/2\rfloor}.}
\tag{1}
$$

This holds in every sufficiently large dimension and covers every rank.
No explicit convergence rate is asserted.

The new argument proves abundant overlap for ALL Gaussian-short PBBS
repair intervals. It combines growing-depth stationary flux with an
exact renewal law for ACTUAL shifted triangles. The earlier raw-cone
renewal alone did not provide this physical interface.

## 1. The physical reduction and exact base fibre

Work in dimension 2r+1; write R=sqrt(r) and
W_r=binom(2r+1,r)=(2r+1)Cat_r. The full PBBS factor has W_r edges.
A newborn lifetime T includes the consuming update, its native physical
same-label return has length 2T+1, and its repair trace has T+2 edges.

For fixed 0<c<C put H_c=floor(cR), H_C=floor(CR) and

    F_c={GOOD,Z_(0,0)=0,T<=H_c}, F_C={GOOD,Z_(0,0)=0,T<=H_C}.

GOOD is the established invariant profile condition. Actual base
incidence weights a uniform Dyck root by(T+2)1_(F_c)/mu_c, then samples
offset j uniformly in{0,...,T+1}. The accepted bounds are
mu_c=Theta_c(1) and mu_C=O_C(1). Let K_C count the ACTUAL F_C traces
containing the sampled edge. It will suffice to prove K_C tends to
infinity under this law.

Let D_s be the original depth-s pruned core, r_s its semilength,
p_s=2r_(s+1)+1 and ell_s=r_s-2r_(s+1)+r_(s+2). The exact inverse-pruning
rows Z_s are independent uniform weak compositions conditional on the
complete profile. On the safe base zero triangle through depth S, expose

    E_S=(complete original profile, all original rows at depths>=S, j).

Conditional on this environment, row s<S is uniform on P_s=p_s-s-1
free slots, and its slots0,-1,...,-s are fixed zero. The short-base
condition introduces no further weight on these free entries.

The physical clocks C_s and T_s select the next predecessor and next
same label. They commute, C preserves parity, and T reverses parity.
A zero gap gives the exact short-horizon rules C->C and T->CT under
pruning, including reverse grouping. Profiles and height are invariant.

## 2. Growing-depth flux supplies eligible boundaries

Here and below all quoted finite identities are proved in the linked
supporting notes, with their original source dependencies recorded.
Set L=floor(r^(2/5)). The accepted sampled-base triangle and safety
bounds retain depth L with probability1-o(1): triangle failure costs
O_c(L^2/r), and the safe-profile exception is exponentially small in
r/L^2. This does not require simultaneous zero triangles for all partners.

Sum all upper completions to obtain the EXACT unnormalized stationary
core measure q_(r,L), divided by Cat_r, retaining GOOD and safety. Define

    M_L=sum_E q_(r,L)(E) pk(E).

The new profile calculation proves, for every fixed eta>0,

    M_L<=C_eta r/L^(3-eta)+superpolynomially small error.          (2)

Briefly, uniform original-depth concentration through2L gives
r_u=(1+o(1))r/(u+1), and convexity gives
d_u=r_u-r_(u+1)<=O(r/u^2). The exact zero-triangle probability is
product_(u<L)(p_u-1)_(u+1)/(ell_u+p_u-1)_(u+1). Its negative logarithm
is at least sum_(u<L)(u+1)ell_u/(p_u+ell_u). The exact Abel identity for
sum(u+1)(u+2)ell_u supplies2r log L-O(r). Thus the zero probability is
at most C_eta L^(-1+eta). Multiplication by d_L proves(2), including
the negligible exceptional-profile contribution. With eta=1/8,
M_L=O(r^(-3/20)).

On the base core let b_0 be the endpoint of Q_L=C_L^L T_L. For fixed K,
t_K=C_L^K(0) and Delta_K=C_L^K(b_0)-b_0. The exact stationary C index
is the peak count. The Q_L endpoint permutation preserves q_(r,L), even
when switching parity. Consequently

    sum q_(r,L)t_K=2K M_L, sum q_(r,L)Delta_K=2K M_L.     (3)

In the actual Palm sum the base weight is at most H_c+2. Markov and
offset counting give

    P_inc,c(t_K>=L)=O(r^(-1/20))+o(1),
    Delta_K=o(R), P_inc,c(2j<t_K)=o(1).                  (4)

Fix S>=K. Base zeros identify the first K common C boundaries at depths
S and L by reverse grouping inside the already short base endpoint
b_0<=2H_c+1; this supplies a finite safe horizon for that identification.
Require K extra zeros immediately after each base prefix in
rows S,...,L-1. Their exact composition-product probability tends to

    product_(u=S)^infinity(1-1/(u+2)^2)^K
                         =[(S+1)/(S+2)]^K.             (5)

The tail is uniform because the finite Abel bound
sum_(u=m)^(L-1)ell_u/r_(u+1)<=O(1/m) controls all remaining extra slots.
No growing-depth geometric approximation is used.

On this collar, C_S^(S+k)T_S reverse-groups from the FINITE endpoint
C_L^k(b_0). By(4) it passes the fixed larger cutoff C with probability
1-o(1). Grouping is used only after that safe endpoint test. If A_S
is the set of common boundaries passing the deep cutoff and the
sampled-edge overlap test, then

    liminf_r P_inc,c({0,...,K} subset A_S)
                              >=[(S+1)/(S+2)]^K.        (6)

## 3. The exact actual multipoint law

Equation(4), together with h>=2L on the retained safe base, prevents
any repeated selected label before t_K at every upper depth. For fixed
S it is enough to restrict to the E_S-MEASURABLE event

    t_K<2(h-S)+1, n_S=2r_S+1>=2S+1.                    (7)

This has probability1-o(1) and guarantees no repeats for EVERY upper
completion, so the exact row law remains unchanged. The depth-S sites
0,-1,...,-K are original zero bits: they are first selected at even times.

Let I_s be the ORIGINAL initial insertion map, with

    I_s(0)=0, I_s(a)-I_s(a-1)=1+epsilon_(s,a)+2Z_(s,a),
    I_s(a+p_s)=I_s(a)+n_s.

Here epsilon records whether adjacent child bits differ. The physical
position cocycle is I_s plus a previous-visit count. That count vanishes
on(7), so the actual shifted labels are the nested static images

    xi_S(k)=-k, xi_s(k)=I_s(xi_(s+1)(k)).                (8)

Define Y_k by the FULL shifted zero triangle

    Z_(s,xi_(s+1)(k)-u)=0 for0<=s<S, 0<=u<=s.           (9)

Two exact geometric facts determine its joint law. First, insertion
maps expand integer distances and are periodic; thus
n_v+xi_v(k)>=n_S-k. Every query block lies in the same fundamental
arc(-p_s,0], for every fibre configuration. There are no cyclic collisions.
Second, for successive requested successes i<j and g=j-i, their row-s
blocks add exactly min(g,s+1) new positions. If g<=s+1, the earlier
HIGHER-row zero tests preserve a consecutive zero block through each
insertion, so the centers are exactly g apart. If g>=s+1, increasing
maps separate the centers by at least g, making the blocks disjoint.

Therefore, for0=k_0<...<k_m<=K, g_a=k_a-k_(a-1), and
M_s=sum_a min(g_a,s+1), revealing whole rows downward gives EXACTLY

    P(Y_(k_1)=...=Y_(k_m)=1 | E_S)
       =product_(s=0)^(S-1)
            (P_s-1)_(M_s)/(ell_s+P_s-1)_(M_s).          (10)

The locations depend on deeper rows, but the probability of M_s new
zeros depends only on the profile. No independence of survival events
or freshness after failed chronological tests is assumed. These events
need not equal original-index cones pointwise.

For fixed S,K, actual-incidence profile concentration gives
ell_s/(ell_s+P_s)->1/(s+2)^2. The limiting multipoint probabilities are

    product_a u_(g_a,S),
    u_(g,S)=1/(g+1)*[(S+2)/(S+1)]^g, 1<=g<=S.           (11)

For fixed K let S tend to infinity. Finite inclusion-exclusion identifies
the full indicator vector with the renewal process of masses u_n=1/(n+1).
It is proper: U(z)=-log(1-z)/z and

    F(z)=1-1/U(z)=1-integral_0^1(1-z)^t dt

has nonnegative coefficients
-integral_0^1(-1)^n binom(t,n)dt for n>=1, constant coefficient0 and
F(1-)=1. Its gaps are finite positive integers almost surely. Hence its
number R_K of renewals through K tends to infinity almost surely.

## 4. Native partners, occupied support, and packing

If k is deep-eligible and Y_k=1, the tested finite C_S^S T_S word
reverse-groups through all rows to the native T_0 clock. It is H_C-short
and its trace contains the sampled edge. Row zero supplies its actual
top gap0, and invariant GOOD is preserved. Distinct k give distinct
physical births. Therefore K_C>=sum_(k=0)^K Y_k on{0,...,K} subset A_S.

For each fixed M, use this bound and a union bound. First send r to
infinity at fixed S,K, then S to infinity at fixed K, using(6),(11).
The resulting limsup of P_inc,c(K_C<=M) is at most P(R_K<=M).
Sending K to infinity proves

    K_C -> infinity under actual base-c incidence
                         for every fixed0<c<C.         (12)

The cutoff remains fixed; C=2c suffices. Equivalently choose finite K,
then finite S, then all r beyond a threshold. No independence between
eligibility and survival or interchange of growing parameters is needed.

The established deterministic cross-cutoff inequality is

    |U_c|/W_r<=mu_c P_inc,c(K_C<M)+mu_C/M.               (13)

Equations(12),(13) give |U_c|=o_c(W_r). The accepted negligible
top-gap/BAD incidence extends this to ALL births with T<=H_c.
For fixed epsilon>0 the low-height birth count and edge-capacity split
bound their maximum edge-disjoint packing P_c(r) by

    R P_c(r)/W_r<=C_c exp(-b_c/epsilon^2)
                              +|U_all,c|/(epsilon W_r).

Let r tend to infinity and then epsilon decrease to zero. Thus

    P_c(r)=o_c(W_r/sqrt(r)) for every fixed c>0.         (14)

## 5. Literal word, all ranks, and every dimension

The audited PBBS owner-corridor theorem supplies every required central
target. Erosion, actual dominance-staircase cut charts, and the existing
product-SCD exterior word give the finite all-target ledger

    nu(2r+1)<=W_r+2H Cat_r
               +2(5H-1)P({T<=H-1})+2L_r(r-H),           (15)
    2L_r(r-H)/W_r<=C exp(-(H-1)^2/(8r)),

for2H<=r+1. All witnesses are ordinary contiguous interval unions;
the exact exterior boundary and every seam are charged in(15).

For each fixed integer j use H=floor(jR)+1 and(14). Choose successive
finite thresholds after which both normalized central excesses are
at most1/j. A sufficiently slow diagonal j(r)->infinity keeps H=o(r)
and2H<=r+1. Both central excesses and the exterior term then vanish,
giving nu(2r+1)<=(1+o(1))W_r. The exact trimmed one-coordinate lift
doubles the word length, while W(2r+2)=2W_r, proving the even case.
At a fixed right endpoint the interval unions are nested, so at most
one middle-rank target is realized there. Hence nu(n)>=W(n), proving(1).

## Supporting proofs and contribution record

* [Exact stationary core law and flux](sources/essential/project/scratch/PBBS_STATIONARY_CORE_CLOCK_FLUX_AND_RELAXED_DEPTH_ABUNDANCE_20260908.md).
* [Full growing-depth eligibility and insertion-interface proof](sources/essential/project/scratch/PBBS_COMMON_DEEP_BOUNDARY_ELIGIBILITY_BY_GROWING_DEPTH_FLUX_20260908.md).
* [Exact actual multipoint renewal and native-partner proof](sources/essential/project/scratch/PBBS_ACTUAL_COMMON_BOUNDARY_SHIFTED_TRIANGLE_RENEWAL_20260908.md).
* [Complete previously audited literal compiler, tail and parity chain](sources/essential/project/scratch/PBBS_ABUNDANCE_TO_COEFFICIENT_ONE_VERIFIED_COMPILER_CHAIN_20260908.md).

This consolidated manuscript also passed complete independent reads by
both direct-route and appendix, with no mathematical correction required.
The eligibility and renewal files have root, direct-route and appendix
full-file audits marked PASS. Both independent auditors also reread the
complete cross-cutoff and literal compiler chain. This manuscript
consolidates those checked arguments and retains their exact quantifiers.

The user's separate selective-truncation construction proves the explicit
coefficient 1.177987. Its geometry, padding, literal compilation, energy
identity and moment certification also pass independent checks; the
small exact numerical check ran only on h100. That construction and
the earlier finite-completion refinement are credited to the user.
Neither is used in the PBBS proof above.

The zero-budget renewal/packing theorem rederived during this continuation
already appeared in a September7 note. The new result here concerns the
FULL Gaussian-short family, including positive-budget runs.


<!-- END COMPLETE SOURCE 01 -->


---

<a id="document-02"></a>

## Document 02: COEFFICIENT_ONE_CONSTRUCTION_20260908.md

Source: `/Users/amir.nuriyev/Documents/problem/COEFFICIENT_ONE_CONSTRUCTION_20260908.md`

[Portable document](CONSTRUCTION.md) · [Exact original](originals/project/COEFFICIENT_ONE_CONSTRUCTION_20260908.md)

<!-- BEGIN COMPLETE SOURCE 02 -->

# What the coefficient-one manuscript constructs

2026-09-08. Companion to `COEFFICIENT_ONE_PROOF_20260908.md`.

The manuscript specifies a finite deterministic construction of ordinary
interval-union words. Its new proposed theorem concerns their asymptotic
length. An executable implementation of this PBBS construction has not
been delivered in this continuation, and no improved k=17 word has been
produced from it. The proof has internal AI-agent reviews, not independent
external review or formal verification.

## 1. Finite recipe in odd dimension

Given n=2r+1, try every positive integer H with 2H<=r+1. Fix a
lexicographic order to resolve arbitrary choices.

1. Enumerate the rank-r states of the canonical parenthesis-matching
   PBBS permutation. Take their complements and traverse by two steps,
   obtaining rank-(r+1) owner cycles X_i. The map and conventions are in
   `PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`, Sections 1, 8, and 9,
   and `PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md`.

2. List positive coordinate runs of at most H owners. Their repair
   intervals include the insertion edge, internal edges, and removal
   edge. On each cycle with such intervals, choose an edge in one
   interval and cut there. Hit the remaining line intervals by the
   greedy right-endpoint algorithm. This uses at most twice the maximum
   number of disjoint repair intervals on that active cycle.

3. On each resulting path X_0,...,X_(v-1), extend X constantly beyond
   both endpoints. Output the v+H nonempty subset letters

       D_i = intersection_(j=0)^H X_tilde_(i+j),  -H<=i<=v-1.

   On a cycle needing no cuts, output the cyclic version and repeat
   its first 2H letters. This is the endpoint-capped erosion construction
   in Section 22 of the residence note.

4. At each cut use the ORIGINAL cyclic owners to form

       P_(s,t) = intersection_(i=-s)^(t-1) X_i,  1<=s,t<=H.

   Record the capped positive extents (u_x,v_x) of each coordinate
   present on both sides. Join their Pareto-minimal points by the
   east-before-south unit path from (1,H) to (H,1), and emit P_(s,t)
   at its 2H-1 vertices. Then emit X_(-H),...,X_(H-1). These two words
   restore crossing lower and upper targets. Section 24 and
   `MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md` give the
   formulas and proof.

5. Append the product symmetric-chain tail word. On two r-coordinate
   halves, take standard symmetric-chain decompositions. For each
   chain pair C,D with minimum ranks a+b<=r-H, concatenate C's reversed
   increment word and D's forward increment word. Lift this tail word
   to 2r+1 coordinates by the rule below. The complete recipe is in
   `MATH_THEOREM_O_PRODUCT_SCD_TAIL_MIXED_CYCLE_INTERFACE_20260726.md`,
   Sections 1 and 2.

6. Concatenate all blocks and retain the shortest output among the
   finitely many H candidates. Each witness stays inside its block.

For small dimensions with no admissible H, use a direct complete word,
for example listing all nonempty subsets. No running-time claim is made.

Trying every H avoids needing the nonexplicit thresholds in the
asymptotic proof: the shortest candidate is no longer than the one chosen
by its slow diagonal. This is a finite selection rule, not a rate estimate.

## 2. Even dimensions

For a complete word Q_1,...,Q_N on the preceding odd dimension, add a
new coordinate z and output

    Q_1,...,Q_N, {z}, Q_1 union {z},...,Q_(N-1) union {z}.

This has 2N letters. Old witnesses remain in the first copy. Witnesses
with z use the last block or an old suffix followed by {z}.

## 3. The actual construction at k=17

`answers/k17_upper25745.word` is a retained 25,745-letter word. Its saved
independent exhaustive verification reports all 131,071 nonempty targets
covered, zero missing. It is an earlier boundary splice, not an output
of the new coefficient-one PBBS analysis.

Using `answers/k16.word` as the Python list X, its exact recipe is

```python
Y = X[1:][::-1] + [65536, 50122, 33642] + [x | 65536 for x in X[3:]]
```

Each integer encodes a subset; bit j represents coordinate j+1. Targets
are bitwise ORs of nonempty contiguous, nonwrapping intervals. The
generator and source-only proof are in
`scripts/k17_boundary_splice_20260906_b7e41_audit.py`.

The review package includes both words, the generator, independent
verifier, and saved verification in its `finite_construction` directory.

At r=8, the PBBS ledger has four admissible H choices. Even dropping
its nonnegative packing term, the right-hand sides are 97,786; 94,374;
81,106; and 62,910. Thus that ledger cannot certify a better k=17 word.
These figures do NOT lower-bound all words or exclude a more economical
implementation. See `scratch/PBBS_K17_FINITE_COMPILER_LEDGER_20260908.md`
for the exact remote calculation and its scope.

The recorded finite bounds remain 24,313 <= nu(17) <= 25,745.

## 4. Comparison with the user's new coefficient 1.15325

The user's endpoint-partition argument claims
nu(k)<=(1.15325+o(1))W(k). This is the same full-cube leading coefficient
as our proposed nu(k)=(1+o(1))W(k). If the coefficient-one proof is
correct, it is asymptotically stronger and optimal in its leading
coefficient. It does not imply exact equality nu(k)=W(k), or replace a
verified finite word at k=17.

The new 1.15325 argument has not been independently audited here.
The supplied labels for its proof and verifier contained no accessible
paths or URLs; no claim is made to have run that external verifier.


<!-- END COMPLETE SOURCE 02 -->


---

<a id="document-03"></a>

## Document 03: PBBS_COMMON_DEEP_BOUNDARY_ELIGIBILITY_BY_GROWING_DEPTH_FLUX_20260908.md

Source: `/Users/amir.nuriyev/Documents/problem/scratch/PBBS_COMMON_DEEP_BOUNDARY_ELIGIBILITY_BY_GROWING_DEPTH_FLUX_20260908.md`

[Portable document](sources/essential/project/scratch/PBBS_COMMON_DEEP_BOUNDARY_ELIGIBILITY_BY_GROWING_DEPTH_FLUX_20260908.md) · [Exact original](originals/project/scratch/PBBS_COMMON_DEEP_BOUNDARY_ELIGIBILITY_BY_GROWING_DEPTH_FLUX_20260908.md)

<!-- BEGIN COMPLETE SOURCE 03 -->

# Common deep C boundaries are eligible with an explicit probability

2026-09-08. Pure proof, no mathematical execution. Direct-route deduction.
Root and appendix_a independently read and checked Sections 1-5 in full:
both audits PASS. Root also read and checked the no-repeat/static-position
corollary in Section 6: PASS. Appendix_a's full Section 6 audit, including
the zero-bit and finite-span observations: PASS. Its final deterministic
two-arc guard was proposed by appendix_a and independently checked by
direct-route.

Fix 0<c<C. For every fixed S>=K>=1, under the ACTUAL base-c incidence
law, the first K common depth-S C boundaries all pass the deep partner
cutoff and sampled-edge overlap test with limiting lower probability

    [(S+1)/(S+2)]^K.                                    (1)

Thus, for each fixed K, that probability tends to one as S tends to
infinity after r. This resolves an eligibility issue in the common-
boundary transfer. Survival through the actual intermediate shifted
triangles, and hence divergence of L_0, are not proved here.

## 1. Exact inputs and the sampled-base/all-partner distinction

Use H_c=floor(c sqrt(r)), H_C=floor(C sqrt(r)), and the retained family
F_c={GOOD,T<=H_c,Z_(0,0)=0}, with raw incidence normalizer mu_c=Theta_c(1).
The accepted sources are:

* the exact original composition fibre and uniform depth concentration
  recorded in `PBBS_ORIGINAL_ARRAY_CONE_RENEWAL_20260908.md`;
* the exact core law in
  `PBBS_EXACT_NARAYANA_CORE_INCIDENCE_LAW_20260908.md`;
* the stationary core measure and C-clock index in
  `PBBS_STATIONARY_CORE_CLOCK_FLUX_AND_RELAXED_DEPTH_ABUNDANCE_20260908.md`;
* the original uniform early-triangle source
  `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_uniform_early_triangle_incidence.md`,
  Section 6, especially (18).

The last source bounds the SAMPLED BASE triangle failure under short
incidence by O_c(L^2/r), together with the accepted safe-profile tail
O_c,C(exp(-b_c,C r/L^2)). These bounds allow every deterministic
L=o(sqrt(r)). They do not include the additional sqrt(r) loss incurred
when asking that ALL partners simultaneously have zero triangles.
The all-partner statement is not used at the growing depth below.

Set

    L=floor(r^(2/5)).                                    (2)

Let B_L be the event that the sampled base has F_L=0 and the exact
depth-L safe profile domain, strengthened to the partner cutoff C:

    r_L>H_C,                  h>=2L.                    (3)

Then P_inc,c(B_L)=1-o(1). All upper circumferences exceed 2H_C+2, so
the accepted forward and reverse grouping applies whenever the finite
candidate endpoint is at most 2H_C+1. No expansion to the bottom row,
nor endpoint of an infinite oracle, will be used.

## 2. A stationary weighted peak mass tends to zero

Write a_u=r_u, d_u=a_u-a_(u+1)=pk(D_u), and
ell_u=d_u-d_(u+1)>=0. Thus a_u decreases and d_u is nonincreasing.
The original uniform-root concentration input states, for every u and x,

    P_D(|a_u-r/(u+1)|>(4+x)sqrt(r))<=2 exp(-x^2/6).

With B_r=(4+log r)sqrt(r), define A_r by these simultaneous inequalities
with B_r on the right for every u<=2L+2. Its failure probability is at
most (4L+6)exp(-(log r)^2/6), smaller than every fixed inverse power of
r. On A_r, uniformly in this range,

    (1-delta_r)r/(u+1)<=a_u<=(1+delta_r)r/(u+1),
    delta_r=(2L+3)B_r/r=o(1).                            (4)

Convexity gives, for u>=2,

    d_u <= [a_floor(u/2)-a_u]/[u-floor(u/2)]
                                              <= C_0 r/u^2. (5)

In particular d_L<=C_0r/L^2. The same estimates supply (3), positivity
through 2L, and all distinct-slot margins for large r.

Conditional on the original complete profile, on A_r the probability
that the whole canonical depth-L triangle is zero is EXACTLY

    product_(u=0)^(L-1)
             (p_u-1)_(u+1)/(ell_u+p_u-1)_(u+1),
    p_u=2a_(u+1)+1,                                    (6)

with falling factorials. We claim that, for every fixed eta>0, a
constant C_eta bounds this probability by

    C_eta L^(-1+eta).                                   (7)

Here is a uniform proof. A row's negative logarithm in (6) is at least
(u+1)ell_u/(p_u+ell_u), using log(1+x)>=x/(1+x). By (4)-(5), for every
sufficiently large fixed m=m(eta), and then sufficiently large r,

    (u+1)ell_u/(p_u+ell_u)
      >=(1-eta/4)(u+1)(u+2)ell_u/(2r),   m<=u<L,         (8)

after making the fixed tolerance smaller if needed. Indeed ell_u<=d_u
and p_u+ell_u<=2r/(u+2)[1+delta_r+O(1/u)]. No relative approximation
to the individual second differences ell_u is being assumed.

For w_u=(u+1)(u+2), discrete summation by parts gives the exact identity

    sum_(u=m)^(L-1) w_u ell_u
      =w_m d_m-w_(L-1)d_L
        +2(m+2)a_(m+1)-2L a_L
        +2 sum_(u=m+2)^(L-1) a_u.                       (9)

The two negative boundary terms have magnitude O(r) by (4)-(5).
The sum of a_u in the last term, before its factor 2, is at least
(1-delta_r)r log L-O_m(r).
Consequently (8)-(9), with sufficiently small tolerances, give total
negative logarithm at least (1-eta)log L-O_eta(1). This proves (7).

Let q_(r,L) be the EXACT unnormalized stationary core measure from the
core-law and flux notes: each D_L=E of size t and peak count k has
weight W_(r,L)^GOOD(t,k)/Cat_r, restricted to t>H_C and height(E)>=L.
Define its weighted peak mass

    M_L=sum_E q_(r,L)(E) pk(E).

The inverse-array bijection identifies this with the original uniform-
root expectation of d_L on GOOD, the domain, and F_L=0. On A_r use
(5) and (7); on its complement use d_L<=r. Thus

    M_L <= C_eta r/L^(3-eta)+r P_D(A_r^c).               (10)

Taking eta=1/4 and L from (2) proves

    M_L=O(r^(-1/10))+o(1)=o(1).                          (11)

The estimate is for the STATIONARY UNNORMALIZED reference measure,
not for peaks in a freshly sampled short-conditioned endpoint.

## 3. Small initial boundary times and small extra endpoint times

The exact depth-L base-incidence law conditional on B_L is

    q_(r,L)(E)/mu_(r,L,c)
       *1{a_L^*(E)<=H_c, 0<=j<=a_L^*(E)+1},              (12)

where Q_L=C_L^L T_L has physical endpoint b_0=2a_L^*+1. Its normalizer
satisfies mu_(r,L,c)/mu_c=P_inc,c(B_L)->1, by Section 1.

For a fixed K, put t_K=C_L^K(0). The exact C-even index says the
stationary mean of its edge duration t_K/2 is K pk(E) on each invariant
class. Consequently

    sum_E q_(r,L)(E)t_K(E)/2=K M_L.                      (13)

For each E, at most t_K/2 permitted integer offsets satisfy 2j<t_K.
Summing (12) and using (13) gives

    P_inc,c(2j<t_K | B_L)<=K M_L/mu_(r,L,c)=o(1).         (14)

Next let Delta_K=C_L^K(b_0)-b_0. The endpoint map Q_L is a bijection
of physical selection events: C and T are commuting bijections, and
Q_L goes from even starts to odd endpoints. Use the finite physical
lift if necessary; these maps are equivariant under spatial translation
and descend to canonical roots. The measure q_(r,L) is PHI-invariant,
not merely tau-invariant: its weight and domain depend on sizes, peak
counts and height, all invariant under the physical update. Hence the
Q_L endpoint permutation preserves this reference measure even when it
switches tau components. It follows that

    sum_E q_(r,L)(E)Delta_K(E)=2K M_L.                   (15)

This is an unconditioned reference transport. In the actual base Palm
sum keep the short-base weight, bounding it by H_c+2. For every fixed
delta>0, Markov's inequality and (15) then yield

    P_inc,c(Delta_K>delta sqrt(r) | B_L)
       <=2K(H_c+2)M_L/[delta sqrt(r)mu_(r,L,c)]
       =o(1).                                          (16)

Thus the first fixed K deep boundaries occur before the sampled edge,
and the K additional deep C clocks AFTER the odd base endpoint have
duration o(sqrt(r)) in the actual incidence law. Bottom clocks have
not been approximated or expanded. All statements concern the finite
nonempty core D_L.

## 4. Exact extra-slot collar probability, with a uniform tail bound

Fix S>=K>=1 independently of r. On B_L expose

    E_L=(full original profile, all rows u>=L, offset j).

Rows u<L are the independent exact base-zero compositions. Define the
original-coordinate collar event

    A_(S,K,L)={Z_(u,-u-i)=0:
                         S<=u<L, 1<=i<=K}.               (17)

These are the K slots immediately after the u+1 base-forced coordinates
in each row. On the profile domain they are distinct free coordinates.
Writing P_u=p_u-u-1, its exact conditional probability is

    Q_(r,S,K,L)=product_(u=S)^(L-1)
                     (P_u-1)_K/(ell_u+P_u-1)_K.          (18)

For each fixed upper depth m, finite-depth profile concentration gives
the usual fixed-parameter limit for the product S<=u<m. We must also
control the rows between m and L; they cannot be replaced uniformly by
a geometric oracle.

On A_r, P_u>=a_(u+1) and P_u>=2 for u<L, for all large r. Another exact
summation by parts, using ell_u=d_u-d_(u+1), gives

    sum_(u=m)^(L-1) ell_u/a_(u+1)
      =d_m/a_(m+1)-d_L/a_L
        +sum_(u=m+1)^(L-1)d_u^2/[a_u a_(u+1)]
      <= C_1/m.                                        (19)

The last step follows from (4)-(5). For a free coordinate of row u,
its nonzero probability is ell_u/(ell_u+P_u-1)<=2ell_u/P_u. A union
bound over the K collar slots and (19) therefore bounds the conditional
probability of any collar failure at depths m,...,L-1 by C_2 K/m.

First take r to infinity for fixed m,S,K, then m to infinity. The finite
product limit and this uniform tail bound prove that (18) converges in
probability, under the ACTUAL E_L marginal, to

    product_(u=S)^infinity [1-1/(u+2)^2]^K
                        =[(S+1)/(S+2)]^K.                (20)

It also converges in mean, being bounded by one. The probability of
A_r^c under incidence is o(1), since the incidence density over the
original root law is O_c(sqrt(r)). This handles the exceptional profiles
in (19)-(20). No uniform growing-depth approximation of ell_u/P_u was
used; only the exact composition and the deterministic tail estimate.

## 5. The finite reverse grouping proves eligibility

At depth u the chronological zero-gap expansion of a word with u+k C
nodes and one T node queries the prefix 0,-1,...,-(u+k). The base
triangle supplies its first u+1 zeros, and the collar (17) supplies
the remaining k<=K. Thus on A_(S,K,L), the candidate word from depth S
has the formal endpoint expansion

    C_S^(S+k)T_S  ->  C_L^(L+k)T_L.                     (21)

We only use this as a physical identity AFTER its finite depth-L
endpoint passes the cutoff. By commutation that endpoint is

    b_k=C_L^k(b_0),              0<=k<=K.

Equations (14)-(16), with a fixed margin smaller than 2(C-c), imply
with probability 1-o(1) under (12) that

    t_K<=2j,       b_K<=2H_C+1.                          (22)

The latter also bounds every smaller b_k. All groups in (21) then lie
inside the tested safe horizon, so the accepted reverse grouping
identifies them with the actual depth-S words.

The first k C boundaries themselves agree at depths S and L: at every
intervening row their first k incoming coordinates are base-forced zero,
since k<=K<=S. Therefore t_k=C_S^k(0)=C_L^k(0). The candidate word from
the boundary t_k has endpoint b_k by commutation. It is short because
b_k-t_k<=b_K<=2H_C+1; it covers the sampled edge because

    t_k<=t_K<=2j,                 b_k>=b_0>=2j-1.

The event (22) is E_L-measurable and has probability 1-o(1). Combining
it with (18)-(20) shows that its intersection with the collar has
probability tending to [(S+1)/(S+2)]^K. Finally restore B_L's o(1)
exception. This proves the limiting lower bound (1).

Equivalently, if A_S is the actual deep eligibility set in
`PBBS_COMMON_DEEP_BOUNDARY_SHIFTED_ZERO_TRANSFER_20260908.md`, then

    liminf_(r->infinity) P_inc,c({0,...,K} subset A_S)
                                      >=[(S+1)/(S+2)]^K,

and for each fixed K the right side tends to one as S tends to infinity.

This is an actual probability/number-of-eligible-boundaries statement.
It uses a growing but finite retained base fibre to control late times,
not an infinite prefix oracle endowed with a physical endpoint. The
remaining lower-row shifted-zero survival problem is separate. Neither
independence of those survival events nor L_0-divergence follows from
the eligibility statement alone.

## 6. Initial boundary times have no repeated labels or visit corrections

There is a stronger initial-time consequence of the same weighted flux.
For every fixed delta>0, (12)-(13) and Markov give

    P_inc,c(t_K>delta sqrt(r) | B_L)
       <=2K(H_c+2)M_L/[delta sqrt(r)mu_(r,L,c)]=o(1).      (23)

Thus t_K=o(sqrt(r)) in actual incidence probability. In fact a smaller
time scale is available, without any Gaussian-height truncation. Take
eta=1/8 in (10). It yields M_L=O(r^(-3/20))+o(r^(-A)) for every fixed
A in the superpolynomial exceptional term. Hence

    P_inc,c(t_K>=L | B_L)
       <=2K(H_c+2)M_L/[L mu_(r,L,c)]
       =O(r^(-1/20))+o(1).                               (24)

On B_L, h>=2L. At every depth v<=L the reached height is h-v>=L, so
any two selections of one original physical label are separated by at
least 2L+1 physical updates. On t_K<L there are therefore NO repeated
labels in [0,t_K], simultaneously in all the trajectories D_v, v<=L.

To state the consequence without a position-convention ambiguity, define
the ORIGINAL initial particle-position map I_s on integer lifts by

    I_s(0)=0,
    I_s(j)-I_s(j-1)
       =2Z_(s,j)+1+epsilon_(s,j),
    epsilon_(s,j)=1{the original core bits j-1 and j differ}.

Extend periodically by I_s(j+p_s)=I_s(j)+n_s, where n_s=2r_s+1.
This is exactly the map called C_s in Section 2 equations (4)-(6) of
`/Users/amir.nuriyev/.codex/worktrees/e333/problem/research_round1/pbbs_original_array_shift_cocycles.md`.
That source's exact formula is

    lambda_s(t)=I_s(lambda_(s+1)(t))
       +M_(s+1,lambda_(s+1)(t))(t) modulo n_s,            (25)

where M counts selections at times 0<=u<t, EXCLUDING the current
update. The physical edge position has a minus one and the omitted-site
formula adds one; these cancel in (25). There is no further +1.

On the no-repeat event, the label selected at t_k has not been selected
previously in [0,t_k). Consequently the M term in (25) is zero for
every k<=K and every s<L. The initial shifts are therefore exactly
nested STATIC original insertion maps:

    lambda_L(t_k)=-k modulo n_L,
    lambda_s(t_k)=I_s(lambda_(s+1)(t_k)) modulo n_s.       (26)

For any fixed S>=K, the same t_k are the first k C_S boundaries, as
explained in Section 5; the equality of these initial C boundaries
requires only the base forced zeros and NO collar event.

The original deep-core bits at sites 0,-1,...,-K are also zero with
probability 1-o(1), for every fixed S>=K. Indeed these sites are selected
at even times t_k, without earlier selections in [0,t_k). Before a
site's first selection, its bit has been complemented exactly t_k
times. Since t_k is even and the selected bit is zero, its original
bit was zero. This is a condition on D_S itself, hence E_S-measurable;
restricting to it does not change the exact conditional upper-row
composition law.

Each I_s is strictly increasing on its integer lift, with increments
at least one. Thus the recursively chosen integer representatives in
(26), starting at -k, satisfy for k<l<=K

    lambda_s(t_k)-lambda_s(t_l)>=l-k                    (27)

when read as those lifts. For a fixed row, sufficiently separated
indices therefore have disjoint extended query intervals on the line.
There is also a DETERMINISTIC cyclic guard, due to appendix_a. Periodicity
and positive increments give the following for the static lifts
j_S(k)=-k and j_s(k)=I_s(j_(s+1)(k)):

    n_s+j_s(k)
      =I_s(n_(s+1)+j_(s+1)(k))
      >=n_(s+1)+j_(s+1)(k)>=n_S-k.                      (28)

This follows inductively from j_S(k)=-k; both complementary arcs expand
under insertion. Consequently, for every row u<S and k<=K,

    j_(u+1)(k)-u
      >=-n_(u+1)+n_S-K-u > -n_(u+1),                  (29)

because the safe domain has n_S>=2S+1 and K<=S. All these query blocks
lie in the same fundamental interval (-n_(u+1),0]. Their integer-lift
union therefore has EXACTLY its cyclic cardinality for every upper-row
realization. No no-wrap conditioning or probabilistic wrap error is
needed for the fixed collection of boundaries.

For completeness, the following stronger tightness observation remains
useful independently of the deterministic cyclic guard.

Fix S,K and define static lifts j_S(k)=-k and
j_s(k)=I_s(j_(s+1)(k)) on ALL original arrays, before restricting to the
no-repeat event. Put B_s=-j_s(K)>=0. Conditional on the deeper rows and
the full profile in the exact base-S fibre, B_(s+1) and the original
epsilon bits are known. Every free row-s coordinate has exact mean
ell_s/P_s, and the forced ones have mean zero. Summing the defining
increments of I_s therefore gives

    E[B_s | deeper rows,profile]
                         <=2(1+ell_s/P_s)B_(s+1).        (30)

This remains valid for a winding input, since linearity counts any
repeated coordinate with its multiplicity. On a fixed-depth typical
profile, all ell_s/P_s are uniformly bounded. Iterating (30) gives
E[B_s|E_S,profile]<=C_S K, uniformly over its allowed deep core, for
the finitely many intermediate rows. Hence the B_s are tight as r tends
to infinity. All row circumferences p_s tend to infinity, so with
probability 1-o(1) none of the extended row-s query intervals for
0<=k<=K crosses the cyclic boundary at -p_s. Their integer-lift unions
then have exactly their cyclic cardinalities.

This estimate is made in the unchanged composition fibre. Only AFTER
proving it do we intersect the high-probability no-repeat event, on
which j_s(k) equals the physical shift. No freshness assertion has
been conditioned on no-repeat. For this fixed collection of depths and
boundaries, (27)-(29) already justify using linear separation to distinguish
the physical query slots deterministically.

This corollary removes the dynamic VISIT COUNTS from the finite common-
boundary shifts with probability 1-o(1). The original bits in I_s still
belong to the original core; no independent bit law has been asserted.
Any renewal or joint shifted-zero law derived from the nested insertion
maps requires its own proof. No such law or L_0-divergence is included
in this corollary.


<!-- END COMPLETE SOURCE 03 -->


---

<a id="document-04"></a>

## Document 04: PBBS_ACTUAL_COMMON_BOUNDARY_SHIFTED_TRIANGLE_RENEWAL_20260908.md

Source: `/Users/amir.nuriyev/Documents/problem/scratch/PBBS_ACTUAL_COMMON_BOUNDARY_SHIFTED_TRIANGLE_RENEWAL_20260908.md`

[Portable document](sources/essential/project/scratch/PBBS_ACTUAL_COMMON_BOUNDARY_SHIFTED_TRIANGLE_RENEWAL_20260908.md) · [Exact original](originals/project/scratch/PBBS_ACTUAL_COMMON_BOUNDARY_SHIFTED_TRIANGLE_RENEWAL_20260908.md)

<!-- BEGIN COMPLETE SOURCE 04 -->

# Actual common-boundary shifted triangles have a recurrent renewal law

2026-09-08. Pure proof, no mathematical execution. Ternary_lift derives
the exact multipoint law from the new physical static-insertion interface.
Root, direct_route, and appendix_a independently checked the key slot-count
and deterministic arc arguments before this file was written. Root's
subsequent full-file audit passed. Independent direct_route and appendix_a
full adversarial audits also passed, including the native-partner and
final compiler implications. No correction was required.

The proof concerns ACTUAL shifted triangles at common deep C boundaries.
It does not identify them pointwise with original-index cones. It uses
all rows0,...,S-1, so a successful eligible phase is a native short
top-gap-zero PBBS partner. No virtual-row thinning is needed.

The dynamical input is the separately proved finite growing-depth flux
and eligibility theorem in
`PBBS_COMMON_DEEP_BOUNDARY_ELIGIBILITY_BY_GROWING_DEPTH_FLUX_20260908.md`.
The joint-law proof below does not assume independent survival indicators,
freshness after a failed test, or a renewal law at a reached root.

## 1. Exact base fibre and its measurable good sector

Fix0<c<C<infinity and put H_c=floor(c sqrt(r)), H_C=floor(C sqrt(r)).
Sample the ACTUAL incidence law of

    F_c={GOOD,Z_(0,0)=0,T<=H_c}.

For fixed integers S>=K>=1, retain the safe base zero triangle

    Z_(s,-u)=0, 0<=s<S, 0<=u<=s,

and expose E_S=(full original profile, all original rows u>=S, offset j).
The finite-layer incidence-fibre theorem proves that this restriction
has probability1-o(1). Conditional on each feasible E_S, rows s<S are
independent uniform weak compositions of ell_s into

    P_s=p_s-s-1, p_s=2r_(s+1)+1=n_(s+1)

free slots; the displayed s+1 base slots are fixed zero. There is no
additional lifetime weight or constraint on the free entries. The law
of E_S itself remains the original actual-incidence law.

Let t_k=C_S^k(0), 0<=k<=K, on the ONE original depth-S trajectory.
These are distinct even physical times, with selected original labels
lambda_S(t_k)=-k. The flux theorem's Section6 proves

    t_K=o(sqrt(r)) in actual incidence probability.

The actual safe-height bound, or its stronger growing-L version, makes
the following E_S-MEASURABLE good condition have probability1-o(1):

    t_K<2(h-S)+1, n_S>=2S+1,                         (1)

together with the fixed-depth safe profile margins. Every upper-level
completion has height h-s at depth s<=S. Its same-label return gap is
at least2(h-s)+1. Thus (1) prevents ANY repeated selected original label
in[0,t_K], simultaneously at all depths s<=S and for EVERY completion
in this fibre. Conditioning on(1) therefore leaves the exact upper-row
composition law unchanged. This is not conditioning on a realized
survival or a hidden upper-row no-repeat event.

At depth S the sites0,-1,...,-K have original bit zero. Each is first
selected at its even time t_k; before its first selection its bit has
been complemented exactly t_k times. This zero spine is part of E_S.

## 2. Actual shifts are initial insertion maps

Let I_s be the initial particle-position map on integer lifts, with

    I_s(0)=0,
    I_s(a)-I_s(a-1)=1+epsilon_(s,a)+2Z_(s,a),
    I_s(a+p_s)=I_s(a)+n_s,

where epsilon_(s,a) is1 if the two adjacent ORIGINAL depth-(s+1)
core bits differ, and0 otherwise. These maps are strictly increasing
and expand integer distances.

The exact physical cocycle is

    lambda_s(t)=I_s(lambda_(s+1)(t))
      +M_(s+1,lambda_(s+1)(t))(t) modulo n_s,

where M counts previous selections, excluding the current update.
On(1) its visit term vanishes at every t_k. Hence the actual shifts
are represented by the nested STATIC images

    xi_S(k)=-k,
    xi_s(k)=I_s(xi_(s+1)(k)), 0<=s<S.                (2)

The original insertion maps, including their epsilon bits, are used.
No independent law for those bits is asserted.

Define the full shifted-triangle indicator Y_k by

    Y_k=1 iff Z_(s,xi_(s+1)(k)-u)=0
                for every0<=s<S and0<=u<=s.         (3)

All indices in(3) are the actual original-array indices at time t_k.
The base gives Y_0=1.

## 3. Deterministic cyclic guard for every fibre completion

The composed insertion map from depth S to depth v sends0 to0 and
-n_S to-n_v. It expands each unit distance by at least one. Therefore

    n_v+xi_v(k)>=n_S-k, 0<=k<=K.                    (4)

For the row-s query interval

    J_s(k)=[xi_(s+1)(k)-s, xi_(s+1)(k)],

(4) and n_S>=2S+1, K<=S imply

    -p_s < xi_(s+1)(k)-s <= xi_(s+1)(k) <=0.         (5)

Thus all query intervals, including the forced base interval[-s,0],
lie in the SAME integer fundamental arc(-p_s,0]. Their unions have
exactly their integer cardinalities after cyclic projection.

This holds for every row configuration. No maximum-gap restriction,
no-wrap conditioning, probabilistic query cutoff, or growing-coordinate
geometric approximation is required.

## 4. Short-gap reset and long-gap separation

Fix i<j<=K and write g=j-i. Before row s is exposed, suppose the
row-u tests for Y_i have passed at every higher row u>s.

If g<=s+1, then

    xi_(s+1)(j)=xi_(s+1)(i)-g.                      (6)

Here is the exact static induction. At depth S the g+1 sites from-i
through-j are consecutive zero bits. At a higher row u>s, the successful
triangle at i forces its first g incoming coordinates to zero: the
required indices have offsets0,...,g-1, and g-1<=u. If the g+1 child
sites are consecutive zeros, their adjacent epsilon values are zero.
The insertion increments across those g gaps are consequently all1.
The inverse-pruning encoding sends each child site's recorded bit to
the same bit at its parent image. Their images are therefore again
consecutive zero sites in the parent. Descend
through rows S-1,...,s+1. This proves(6).

If g>=s+1, no success assumption is needed: distance expansion in(2)
gives

    xi_(s+1)(i)-xi_(s+1)(j)>=g>=s+1.                (7)

The two row-s intervals of length s+1 are then disjoint. Statements
(6)-(7) include the common boundary g=s+1 consistently.

This is the physical replacement for the invalid static-cone map.
Failures may shift later centers farther left, but they cannot shrink
a long separation. A prior success supplies exactly the short alignment
needed when intervals can overlap.

## 5. Exact finite conditional multipoint formula

Choose0=k_0<k_1<...<k_m<=K, and put g_a=k_a-k_(a-1). Define

    M_s=sum_(a=1)^m min(g_a,s+1), 0<=s<S.

Then, on every feasible good environment from Section1,

    P(Y_(k_1)=...=Y_(k_m)=1 | E_S,base triangle)
      =product_(s=0)^(S-1)
          (P_s-1)_(M_s)/(ell_s+P_s-1)_(M_s).       (8)

Factorials fall. Since M_s<=sum g_a=k_m<=K and the safe margins give
P_s>K, every ratio in(8) is within its ordinary stars-and-bars range.

Proof: reveal entire rows S-1,S-2,...,0. Conditional on higher rows,
all row-s centers are determined, and row s keeps its independent
base-zero composition law. On the event that all higher tests passed,
add the requested intervals in increasing k order, starting with the
base interval J_s(0). For a gap g_a<=s+1, (6) says the new interval
adds exactly g_a slots to the left of the previous leftmost interval.
For g_a>=s+1, (7) says it adds all s+1 slots. Earlier intervals lie
farther right and cannot change this count. By(5) there are no cyclic
coincidences. Exactly M_s NEW FREE row-s slots must therefore be zero.
Their uniform-composition probability is precisely the row ratio in(8).
It is independent of the locations and of all other higher-row data.
Iterating these conditional probabilities proves(8).

This computes all finite intersections of success events. It does not
claim that testing candidates chronologically leaves a fresh law after
failed tests; no such assertion is needed.

## 6. Fixed-depth limiting law and proper renewal

At every fixed S, the accepted original-profile concentration under
ACTUAL base incidence gives, in probability,

    ell_s/(ell_s+P_s) -> 1/(s+2)^2, 0<=s<S.

The finite safe and good exceptions above are o(1). Hence(8), integrated
over the unchanged E_S law, gives

    lim_(r->infinity) P_inc,c(all Y_(k_a)=1)
       =product_(a=1)^m u_(g_a,S),                 (9)

where

    u_(g,S)=product_(s=0)^(S-1)
                [1-1/(s+2)^2]^min(g,s+1).

For1<=g<=S this telescopes exactly to

    u_(g,S)=1/(g+1)*[(S+2)/(S+1)]^g.               (10)

One may verify it by dividing the g product by the g-1 product; the
tail ratio is g(S+2)/[(g+1)(S+1)]. In particular, with K fixed, sending
S to infinity in(9) gives the multipoint probabilities

    product_(a=1)^m 1/(g_a+1).                     (11)

These specify the renewal process begun at0 with renewal masses
u_n=1/(n+1). For completeness, write

    U(z)=sum_(n>=0)u_n z^n=-log(1-z)/z,
    F(z)=1-1/U(z)=1-integral_0^1 (1-z)^t dt.

The coefficient at n>=1 is

    f_n=-integral_0^1 (-1)^n binom(t,n)dt >=0,

because binom(t,n) has sign(-1)^(n-1) for0<t<1. Also f_0=0 and
F(1-)=1. Thus f is a probability distribution on finite positive
integer gaps, with renewal mass U=1/(1-F). Its regeneration identity
is exactly(11). Finite inclusion-exclusion determines every finite
binary indicator-vector law from its success intersections, so this
identifies the limiting law of the ACTUAL indicators, not only their
individual expectations.

Let R_K be its number of renewals in{0,...,K}. Since all interarrival
times are finite positive integers almost surely, R_K tends to infinity
almost surely. Consequently for every fixed integer M,

    lim_(K->infinity) P(R_K<=M)=0.                 (12)

Equations(9)-(12) use the order r->infinity first at fixed S,K, then
S->infinity at fixed K, then K->infinity. They require no uniform
growing-S approximation to geometric rows and no second-moment shortcut.

## 7. Eligible successes are native physical partners

Let A_S be the deep eligibility set from the transfer and flux notes.
For k in A_S, the depth-S word C_S^S T_S starting at t_k has endpoint
b_k satisfying

    b_k-t_k<=2H_C+1, t_k<=2j, b_k>=2j-1.            (13)

If Y_k=1, all shifted triangles through rows0,...,S-1 vanish.
Starting with this FINITE tested depth-S word, apply the accepted reverse
grouping C->C and T->CT at its actual chronological endpoints. At row
s it queries exactly the s+1 zero coordinates in(3), giving C_s^s T_s.
The profile circumferences exceed the entire horizon in(13), so these
groups are actual clocks, not formal infinite expansions. At depth0
this produces the native T clock of the original birth at t_k/2.

Its lifetime is (b_k-t_k-1)/2<=H_C. The row0 condition in(3) gives
its actual incoming top gap zero. GOOD is profile-measurable and
invariant under PBBS, so the shifted birth belongs to F_C. Its trace
covers the sampled edge j by the two endpoint inequalities in(13).

Different k give distinct even starting times, and on(1) even have
distinct original top labels. Thus, writing K_C for ACTUAL physical
partner congestion under the base-c incidence law,

    K_C >= sum_(k=0)^K Y_k
          whenever {0,...,K} is contained in A_S.   (14)

No row-one virtual feasibility, top-row thinning, or factor-two label
conversion is involved.

## 8. Abundance, occupied support, and the compiler consequence

The independently proved eligibility estimate states, for fixed S>=K,

    liminf_(r->infinity)
      P_inc,c({0,...,K} subset A_S)
          >=[(S+1)/(S+2)]^K.                      (15)

No independence from Y is assumed. By the union bound and(14),

    P_inc,c(K_C<=M)
       <=P_inc,c(sum_(k=0)^K Y_k<=M)
            +P_inc,c({0,...,K} not subset A_S)
            +o(1).                               (16)

For any fixed K, (9)-(11) and(15) make the limsup of(16), first in r
and then in S, at most P(R_K<=M). Send K to infinity and use(12).
Equivalently, given a desired error, choose K finite first, then S
finite, then r sufficiently large. This proves

    K_C -> infinity in ACTUAL base-c incidence probability
                     for every fixed0<c<C.        (17)

The partners remain in one fixed larger cutoff C; C does not grow
with r, S, or K. Taking C=2c suffices for every fixed c>0.

The deterministic cross-cutoff inequality in
`PBBS_CROSS_CUTOFF_OCCUPIED_SUPPORT_REDUCTION_20260908.md` gives

    |U_c|/W <= mu_c P_inc,c(K_C<M)+mu_C/M,

with mu_c=Theta_c(1), mu_C=O_C(1). First let r tend to infinity using
(17), then M tend to infinity. Thus |U_c|=o_c(W). The accepted negligible
discarded-top-gap/BAD incidence bound extends this to all physical
births with T<=floor(c sqrt(r)). The occupied-support-to-packing theorem
then gives packing o_c(W/sqrt(r)).

Finally the already audited chain
`PBBS_ABUNDANCE_TO_COEFFICIENT_ONE_VERIFIED_COMPILER_CHAIN_20260908.md`
has no further compatibility premise: its literal erosion/cut compiler,
correct tail boundary, slow fixed-c diagonal, and opposite-parity lift
turn this physical packing conclusion into coefficient one.

This final deduction is to be accepted only together with the stated
finite core-law/flux/eligibility input and adversarial full-file audits.
The new point of this note is the exact ACTUAL multipoint law(8), with
measurable conditioning, deterministic arc separation, and native
partner realization. None of these conclusions follows from the old
original-index cone theorem alone.


<!-- END COMPLETE SOURCE 04 -->


---

<a id="document-05"></a>

## Document 05: PBBS_STATIONARY_CORE_CLOCK_FLUX_AND_RELAXED_DEPTH_ABUNDANCE_20260908.md

Source: `/Users/amir.nuriyev/Documents/problem/scratch/PBBS_STATIONARY_CORE_CLOCK_FLUX_AND_RELAXED_DEPTH_ABUNDANCE_20260908.md`

[Portable document](sources/essential/project/scratch/PBBS_STATIONARY_CORE_CLOCK_FLUX_AND_RELAXED_DEPTH_ABUNDANCE_20260908.md) · [Exact original](originals/project/scratch/PBBS_STATIONARY_CORE_CLOCK_FLUX_AND_RELAXED_DEPTH_ABUNDANCE_20260908.md)

<!-- BEGIN COMPLETE SOURCE 05 -->

# Stationary core-clock flux and relaxed depth abundance

2026-09-08. Pure proof; no mathematical execution. Appendix_a deduction.
Independent direct-route full-file audit: PASS, including stationary
transport, label sums, clock indices, and the relaxed-abundance scope.
Root full-file audit, including the original structural clock and native
repair-congestion sources: PASS. The fixed original size and actual short-clock
Palm law are retained throughout.

The new conclusions are an exact backward-age formula for the depth-two
distinct-label count, an exact unrestricted clock congestion, and a growing
RELAXED depth-S phase count. The last count does not yet pull back to many
actual depth-two zero-feasible phases.

## 1. Sources and exact stationary reference measure

Use the fully audited notes

* `PBBS_EXACT_NARAYANA_CORE_INCIDENCE_LAW_20260908.md`;
* `PBBS_ZERO_OR_ONE_FEASIBILITY_AND_DISTINCT_LABEL_RECIPROCAL_20260908.md`;
* `PBBS_BAD_PARTNER_UNION_TRANSFER_AND_ZERO_ONLY_FEASIBILITY_20260908.md`;
* `PBBS_HEIGHT_FREE_INTERVAL_STABBING_AND_RECIPROCAL_EQUIVALENCE_20260908.md`.

The physical edge/clock conventions also follow the exact structural
source `pbbs_gaussian_clock_genealogy_structural_audit.md` and stationary
source `pbbs_stationary_lifetime_identities.md` in worktree c69c. Original
label transport is equation (3) of `pbbs_original_array_shift_cocycles.md`
in worktree e333.

Fix original size r, constants 0<c<=C, H_c=floor(c sqrt(r)),
H_C=floor(C sqrt(r)), and a fixed integer S>=2. For a nonempty core E
write t=|E| and k=pk(E). Retain the domain

    t>H_C,                    height(E)>=S.                 (1)

This is invariant under the rooted physical shift tau=phi^2. Its stronger
partner-cutoff circumference requirement changes the actual safe base
event by o(1), for fixed S,c,C as r tends to infinity.

Let W_(r,S)^GOOD(t,k) be the EXACT upper-completion count from the
Narayana-core note, including GOOD and the base zero triangle. Define a
finite, generally subprobability measure on cores by

    q_(r,S)(E)=W_(r,S)^GOOD(t,k)/Cat_r *1_(domain (1)),
    z_(r,S)=sum_E q_(r,S)(E).                              (2)

Every size/peak/height class is tau invariant. Since (2) is constant on
each such class, q_(r,S) is stationary under tau. This stationarity is
obtained AFTER summing the upper fibres. The original event that its
canonical triangle is zero need not itself be invariant under tau.

For the chronological core word Q_S=C_S^S T_S define

    a_S(E)=(endpoint(Q_S at physical time 0)-1)/2.

The exact fibre identifies the restricted actual base-incidence law with

    P(E,j)=q_(r,S)(E)/mu_(r,S,c)
             *1{a_S(E)<=H_c, 0<=j<=a_S(E)+1},             (3)

where

    mu_(r,S,c)=sum_E q_(r,S)(E)
                          (a_S(E)+2)1{a_S(E)<=H_c}.       (4)

This is the original fixed-r law, conditioned on its safe zero-triangle
event. In particular mu_(r,S,c)/mu_c tends to one for each fixed S. No
Boltzmann or independently refreshed core law is used.

## 2. Move the sampled edge to time zero

For a core F and H>=0 put

    K_(S,H)(F)=sum_(u=0)^(H+1)
       1{u-1<=a_S(tau^(-u)F)<=H}.                         (5)

These are actual even core birth phases whose Q_S clock has duration at
most 2H+1 and whose inclusive edge interval contains the current edge.
The phase at age u was born at physical time -2u. Set

    J_(S,C)(E,j)=K_(S,H_C)(tau^j E).

For S>2 this is a RELAXED core phase count: it has not tested the actual
intermediate original rows 2,...,S-1. For S=2 it is exactly J_0 on the
safe depth-two fibre, since sum zero is composition-admissible there.

For every function f of the shifted core, stationarity in (2) gives the
exact finite identity

    E_(3)[f(tau^j E)]
       = [sum_F q_(r,S)(F) K_(S,H_c)(F) f(F)]
                                                    /mu_(r,S,c). (6)

Indeed substitute F=tau^j E into each summand of (3). Its survival test
becomes j-1<=a_S(tau^(-j)F)<=H_c, and j runs from 0 to H_c+1.

Since K_(S,H_C)>=K_(S,H_c), equation (6) implies

    E_(3)[1/J_(S,C)] <= z_(r,S)/mu_(r,S,c).                (7)

The summand with zero base congestion is interpreted as zero. When C=c,
there is the exact identity

    E_(3)[1/J_(S,c)]
      = [sum_F q_(r,S)(F)1{K_(S,H_c)(F)>0}]
                                                    /mu_(r,S,c). (8)

Thus (7) uses the stationary reference mass, not an asserted uniform
distribution at a moving original root.

## 3. An exact formula for the distinct depth-two labels

Specialize to S=2 and fix a shifted core F. Set n=2|F|+1 and, for
0<=u<=H_C+1, define

    e_u=1{u-1<=a_2(tau^(-u)F)<=H_C},
    b_0=0,
    b_u=sum_(v=1)^u omega(tau^(-v)F) modulo n.             (9)

Here omega(G)=|R|+1 if G=P1Q0R is its first-maximum, first-return
factorization; lengths are numbers of letters. The exact signed shift
cocycle says b_u is the ORIGINAL core label selected at physical time
-2u, measured relative to the current selected label zero. There is no
replacement of b_u by -u and no deletion of its possible spatial wraps.

Consequently the distinct zero-feasible label count is exactly

    L_0(F)=|{b_u:e_u=1}|.                                 (10)

The audited strict interval bound gives at most two eligible ages for
each label. Hence there is also the exact two-time expression

    L_0(F)=sum_u e_u
              -sum_(u<v) e_u e_v 1{b_u=b_v}.              (11)

Combining (6) with (10) or (11) gives its exact fixed-r Narayana-class
Palm distribution. For example its lower tail is

    P_(3)(L_0<=M)
      = [sum_F q_(r,2)(F)K_(2,H_c)(F)1{L_0(F)<=M}]
                                                    /mu_(r,2,c). (12)

This reduces distinct-label counting to a backward itinerary and explicit
modular sums in one stationary core. It does not make the summands or
their modular coincidences independent.

## 4. Exact clock flux and a finite congestion recursion

On one signed physical core trajectory, write C and T for the predecessor
and same-label endpoint maps. Strict adjacent-selection alternation makes
C bijective: each selection of label i-1 has exactly one preceding
selection of i paired to it. T is bijective by successive same-label
returns. C preserves time parity; T reverses it. They commute.

Thus, in edge time,

    c(d)=C(2d)/2,
    R_S(d)=(C^S T(2d)+1)/2                              (13)

are bijections of the signed integers. They commute with translation by a
physical period. In particular the full Q_S interval family has one birth
and one inclusive right endpoint at each edge.

The even-started C intervals have exact congestion k=pk(E). To see this,
consider the cyclic edge between labels i-1 and i. Selection at i changes
its incoming bits 00 to 10; until the next selection at i-1 both endpoint
bits are complemented together at each update. Selection at i-1 ends the
unequal interval. At an even observation time, this edge has pattern 01
precisely when that active C interval began at an even time. There are
exactly k cyclic 01 edges. This proves congestion k for intervals
(d,c(d)]. Bijection of c makes the congestion of [d,c(d)) the same.

The accepted native T repair intervals have exact congestion t+2. Split
the Q_S interval into its S half-open C stages and its final inclusive
native T interval. Endpoint bijectivity reindexes the starts of each
stage over every edge once. Therefore

    sum_d 1{d<=j<=R_S(d)}=t+Sk+2                       (14)

at every edge j. Long intervals here may have wrap multiplicities; they
are not asserted to be legal short partners. Averaging (14) over any
nonempty tau-invariant core class gives the additional exact identity

    E[a_S(E)]=t+Sk.                                      (15)

For a cutoff H, let B_H(d)=1{R_S(d)-d-1<=H}. With d_*(j) the unique birth
whose endpoint R_S(d_*(j))=j, the short congestion obeys

    K_H(j+1)-K_H(j)=B_H(j+1)-B_H(d_*(j)).                 (16)

This is an exact finite flux recursion, including the inclusive endpoint
convention. It does not supply a mixing or short-tail estimate.

## 5. The relaxed phase count really grows with depth

The reference mass in (2) is exactly the original uniform-root probability
of GOOD, domain (1), and F_S=0. For each FIXED S, original-depth profile
concentration gives

    p_s/r -> 2/(s+2),
    ell_s/r -> 2/[(s+1)(s+2)(s+3)]   for s<S.

Conditional on the full original profile, the rows are independent uniform
weak compositions. The probability that their s+1 distinct triangle slots
are zero is

    (p_s-1)_(s+1)/(ell_s+p_s-1)_(s+1),                    (17)

where the factorials fall. The fixed-S domain and GOOD have unweighted
probability tending to one. For example r_(2S) is positive with probability
tending to one, which supplies the height requirement. Bounded convergence
in (17) therefore gives

    z_(r,S) -> rho_S
       =product_(s=0)^(S-1)(1-1/(s+2)^2)^(s+1)
       =(S+2)^S/(S+1)^(S+1).                             (18)

The last identity follows by cancellation of the powers of each integer
in the product; rho_S is asymptotic to e/(S+1).

Put m_c=liminf_(r->infinity) mu_c>0, using the accepted retained-incidence
normalizer. Equations (7) and (18), and restoration of the o(1) safe
exception for each fixed S, imply for every fixed positive integer M

    limsup_(r->infinity) P_inc,c(J_(S,C)<=M)
                                     <= M rho_S/m_c.     (19)

Define J_(S,C)=1 on that exception if an everywhere-defined variable is
needed. In particular,

    lim_(S->infinity) limsup_(r->infinity)
                         P_inc,c(J_(S,C)<=M)=0.           (20)

This is a positive abundance statement for the RELAXED physical core
phases, proved under the actual original incidence law. The limits are
fixed S first, then r to infinity, then S to infinity. No uniform growing-S
estimate or interchange of these limits has been used.

## 6. The exact remaining pullback issue

For S=2, the relaxed count is the actual exposed J_0, and (10)-(12) give
L_0. For S>2, a phase counted in (5) need not have zero translated triangle
in its ACTUAL original rows 2,...,S-1. The accepted short forward/reverse
clock theorem pulls it back to a depth-two C_2^2 T_2 phase when those
coordinates are zero. The new zero-only theorem proves that all genuinely
depth-two feasible phases have these zeros with high probability; its
implication runs from actual feasibility to the deep test, not conversely.

The missing converse cannot be inserted into (20). In particular a large
number of relaxed core phases may still be lost upon exposing the actual
intermediate rows. Those rows must be sampled in their exact base-zero
fibre, with their moving original indices and shared coordinates retained.
Their individual zero probabilities decrease with the depth: the product
for disjoint newly tested triangle slots has the same order 1/S appearing
in (18). Thus the core abundance scale alone does not overcome the
pullback loss by an elementary independent-thinning argument.

No L_0 divergence, occupied-support decay, or improved compiler coefficient
is claimed. Equations (11), (16), and the actual relaxed abundance theorem
(20) are the new finite-count and mass-transport inputs.


<!-- END COMPLETE SOURCE 05 -->


---

<a id="document-06"></a>

## Document 06: PBBS_EXACT_NARAYANA_CORE_INCIDENCE_LAW_20260908.md

Source: `/Users/amir.nuriyev/Documents/problem/scratch/PBBS_EXACT_NARAYANA_CORE_INCIDENCE_LAW_20260908.md`

[Portable document](sources/essential/project/scratch/PBBS_EXACT_NARAYANA_CORE_INCIDENCE_LAW_20260908.md) · [Exact original](originals/project/scratch/PBBS_EXACT_NARAYANA_CORE_INCIDENCE_LAW_20260908.md)

<!-- BEGIN COMPLETE SOURCE 06 -->

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


<!-- END COMPLETE SOURCE 06 -->


---

<a id="document-07"></a>

## Document 07: PBBS_ORIGINAL_ARRAY_CONE_RENEWAL_20260908.md

Source: `/Users/amir.nuriyev/Documents/problem/scratch/PBBS_ORIGINAL_ARRAY_CONE_RENEWAL_20260908.md`

[Portable document](sources/essential/project/scratch/PBBS_ORIGINAL_ARRAY_CONE_RENEWAL_20260908.md) · [Exact original](originals/project/scratch/PBBS_ORIGINAL_ARRAY_CONE_RENEWAL_20260908.md)

<!-- BEGIN COMPLETE SOURCE 07 -->

# Recurrent shifted cones in the original arrays under actual short incidence

2026-09-08. Root pure-proof deduction; no computation.
Status: full independent root-helper and task03 audits PASS. These are
ORIGINAL-INDEX array events, not yet physical shifted births or eligible
virtual intervals.

## 1. Setting and the precise accepted inputs

Let D be a Dyck root of semilength r, with pruning sizes r_s, height h,
and original inverse-pruning rows Z_s. Put

    H=floor(c sqrt(r)), c>0 fixed,
    F0={GOOD,T<=H,Z_(0,0)=0},
    mu0=E_D[(T+2)1_F0]=Theta_c(1).

The actual incidence law first weights the original uniform Dyck law by
(T+2)1_F0/mu0, then chooses j uniformly in {0,...,T+1}. The row labels
are persistent original labels, not positions in a newly rooted state.
Write

    p_s=2r_(s+1)+1,
    ell_s=r_s-2r_(s+1)+r_(s+2),
    F_S=sum_(s=0)^(S-1) sum_(u=0)^s Z_(s,-u).

The following previously proved inputs are used explicitly.

1. [Finite-layer incidence fibre](sources/essential/c69c/research_round1/pbbs_finite_layer_zero_triangle_incidence_fibre.md): on a profile with h>=2S, p_s>2H+1 and p_s>=2(s+1) for s<S, fix the entire profile, all original rows of index at least S, and j. Conditional on F_S=0 and a feasible environment, rows s<S are independent uniform weak compositions of ell_s into p_s-s-1 free coordinates, their s+1 base-triangle coordinates being zero. No lifetime constraint on a free coordinate remains.
2. [Actual safe-depth and zero-triangle bounds](sources/essential/project/scratch/PBBS_TOP_ZERO_ALL_SHORT_OVERLAP_REDUCTION_20260908.md), Section6: the preceding profile domain and F_S=0 have actual incidence probability at least 1-C_c S^2/r-C_c exp(-b_c r/S^2), for deterministic 1<=S<=sqrt(r), by restricting to the stated safe-depth event.
3. [Original one-depth concentration](sources/essential/project/scratch/PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md), Section2: for every s and x>=0,

       P_D(|r_s-r/(s+1)|>(4+x)sqrt(r))<=2exp(-x^2/6).

The first input was fully read by root and passed a separate full clock,
measurability, composition, and incidence audit. The other inputs are
already accepted. The deduction below requires no new dynamic law.

## 2. Fixed original free coordinates have a stable product limit

Fix S>=1 and finitely many distinct nonbase coordinates in each row
s<S. On the actual incidence law, all of their values jointly converge
in total variation to independent random variables G_(s,i) with

    P(G_(s,i)=a)=(1-q_s)q_s^a, a=0,1,...,
    q_s=1/(s+2)^2.                                  (1)

Coordinates in the base triangle have limiting value zero. The free
product limit is also stable relative to the exposed environment: the
mean, over feasible environments, of the conditional total-variation
distance from the fixed law (1) tends to zero.

Proof. The marginal root density under incidence is at most C_c sqrt(r).
Input3 therefore implies, for every fixed finite set of depths,

    r_s/r -> 1/(s+1)

in actual incidence probability. For example take deviations r^(3/4):
the original failure probability is exp(-Omega(sqrt(r))), and the extra
sqrt(r) factor is harmless. Thus uniformly on a set of incidence
probability tending to one, for each fixed s<S,

    p_s/r -> 2/(s+2),
    ell_s/r -> 2/[(s+1)(s+2)(s+3)],
    ell_s/(ell_s+p_s-s-1) -> 1/(s+2)^2.              (2)

The safety and zero-triangle exception in Input2 is o(1) for fixed S.
Now use the EXACT conditional fibre, not an unconditioned product law.
Put P=p_s-s-1 and ell=ell_s. For m fixed distinct free coordinates with
specified values a_1,...,a_m, whose sum is a, stars and bars gives

    P(Z_1=a_1,...,Z_m=a_m | environment,F_S=0)
      = binom(ell-a+P-m-1,P-m-1)/binom(ell+P-1,P-1). (3)

For all sufficiently large r the displayed parameters are positive;
the probability is zero if a>ell. Along every sequence satisfying (2),
the ratio (3) tends to (1-q_s)^m q_s^a. Its limiting masses sum to one,
so pointwise convergence on this countable state space implies total-
variation convergence: first restrict to a finite set with limiting
mass close to one, then bound the complementary mass in both laws.
This reasoning is uniform on shrinking typical-profile sets, or else
a violating parameter sequence would contradict the same limit.
Conditional row independence proves the assertion for all queried rows.
The atypical and infeasible-environment masses are o(1). This proves
the mean conditional TV assertion and its unconditional consequence.

The exposed environment itself need NOT have its original unweighted
law. In particular (1) is not an independent model for a reached root.

The new [initial-P-run estimate](sources/contextual/c69c/research_round1/pbbs_initial_p_run_incidence_divergence.md)
has a useful compatibility consequence. For any deterministic
m_r=o(r^(1/4)), adding the restriction p0>m_r does not change the
UNCONDITIONAL finite-coordinate limit (1). Its complement has actual
incidence probability at most C_c(m_r+1)^2/sqrt(r)=o(1); intersecting
any event changes its probability by at most this amount, and
conditioning divides by a probability tending to one. Thus finite
free-gap randomness persists even on long-initial-P bases. This does
not assign an unchanged conditional law at each individual environment
after the extra restriction, or itself prove a physical misalignment.

## 3. Shifted array cones and their exact limiting joint law

For an integer d>=0 define the depth-S ORIGINAL-INDEX cone event

    Q_S^(r)(d)=1{Z_(s,-d-u)=0 for 0<=s<S, 0<=u<=s}. (4)

Indices are cyclic at their row. For each fixed finite collection of
d's and S, the relevant indices are distinct as ordinary integer
indices modulo p_s for all sufficiently large typical profiles. On
exceptional roots without these rows define the indicator to be zero;
Input2 makes that convention asymptotically irrelevant. The base d=0
cone has probability tending to one under actual F0 incidence.

Fix 0=d_0<d_1<...<d_k and write g_j=d_j-d_(j-1). The limiting joint
probability of all their cones is

    lim_(r->infinity) P_inc(Q_S^(r)(d_j)=1 for j=0,...,k)
      = product_(j=1)^k u_(g_j,S),                  (5)

where

    u_(g,S)=product_(s=0)^(S-1)
             [ (s+1)(s+3)/(s+2)^2 ]^min(g,s+1).    (6)

Indeed, in row s each cone uses an integer interval of s+1 coordinates.
Adding these equal-length intervals in increasing d order adds exactly
min(g_j,s+1) NEW coordinates at its jth addition. The base interval is
already forced to zero. All newly requested coordinates are free, so
(1) gives (5)-(6), including coincidences between cones. Neither cones
nor their indicators have been declared independent.

For g<=S the product telescopes exactly to

    u_(g,S)=1/(g+1) * [(S+2)/(S+1)]^g.              (7)

One quick verification divides the product for g by the product for
g-1. The ratio is the tail product over s>=g-1, namely
g(S+2)/[(g+1)(S+1)]. Multiplying these ratios for g=1,... gives (7).
For g>S the product is the same as for g=S. In particular

    lim_(S->infinity) u_(g,S)=1/(g+1)               (8)

for every fixed positive g.

## 4. The infinite-array cone process is a recurrent renewal process

Construct independent G_(s,i) on all free original integer coordinates,
with law (1), and set the base cone coordinates to zero. Let Q_S(d)
be the corresponding event (4), and Q_infinity(d)=inf_S Q_S(d).
For every fixed finite collection of d's, monotone convergence and
(5)-(8) give

    P(Q_infinity(d_j)=1 for j=0,...,k)
      =product_(j=1)^k 1/(g_j+1).                  (9)

These are the joint indicators of a proper recurrent renewal process
started at zero. For completeness, put u_n=1/(n+1) and

    U(z)=sum_(n>=0)u_n z^n=-log(1-z)/z,
    F(z)=1-1/U(z)=1-integral_0^1(1-z)^t dt.

For n>=1 the coefficient

    f_n=-integral_0^1 (-1)^n binom(t,n)dt

is nonnegative: binom(t,n) has sign (-1)^(n-1) for 0<t<1. Also f_0=0
and F(1-)=1, so the f_n form a probability distribution on positive
finite integers. The renewal process with iid increments of this law
has mass sequence u_n, because 1/(1-F)=U. Regeneration gives exactly
(9). Finite inclusion-exclusion determines the law of every finite
binary indicator vector from these joint probabilities. Hence it is
the law of Q_infinity. Almost surely its number R_L of renewals in
{0,...,L} tends to infinity: every fixed finite number of its positive,
almost surely finite increments has a finite sum.

The auxiliary construction also bounds finite-depth errors. For S>=L,
the probability that any Q_S(d) differs from Q_infinity(d), 1<=d<=L,
is at most

    sum_(d=1)^L [u_(d,S)-1/(d+1)] <= C L/(S+1).     (10)

Use (7) and e^x-1<=C x for 0<=x<=1. This is a bound in the limiting
independent ORIGINAL array model; it does not assert a growing-r
uniform approximation to that model.

## 5. Actual incidence has many array cones in an iterated limit

For fixed L, use S=L in (4). Section2 gives convergence of the finite
indicator vector under actual F0 incidence to (Q_L(d))_(d=0)^L.
In the auxiliary coupling Q_L(d)>=Q_infinity(d), coordinatewise.
Consequently, for every fixed integer M>=0,

    limsup_(r->infinity)
      P_inc(sum_(d=0)^L Q_L^(r)(d)<=M)
        <=P(R_L<=M).

Let L tend to infinity. We obtain the unconditional actual-incidence
ARRAY conclusion

    lim_(L->infinity) limsup_(r->infinity)
      P_inc(sum_(d=0)^L Q_L^(r)(d)<=M)=0.            (11)

A diagonal choice gives some L_r tending to infinity arbitrarily
slowly, with L_r=o(sqrt(r)), for which the cone count diverges in
actual incidence probability. No quantitative rate in r is claimed.
For the diagonal, apply (11) successively with M=1,2,... and errors
tending to zero, taking each r threshold after the fixed-L limit; it
may also be increased to enforce any prescribed diverging upper bound
on L_r. The particular finite diagonals can be chosen increasing.

## 6. The missing physical interface is not part of this theorem

An array index d in (4) has NOT been identified with physical birth d.
At a physical time t, the queried initial label at level s is determined
by the reached selection cocycle at that level. These labels need not
all equal -d, and may depend on the free rows whose zeros appear in (4).

Even if the starting labels aligned, finite-depth zero clocks alone
do not show that their deeper C^S T remainder meets T<=H or that their
repair interval covers the sampled offset j. Those are separate clock
transport and endpoint assertions. The recent long initial P-run lemma
does not supply them by itself; bounded-gap one-neighbor amplification
also warns against a uniform deterministic endpoint comparison.

Thus (11) is NOT k0 divergence, occupied support o(W), a physical
packing theorem, or coefficient one. It supplies the recurrent random
array structure under the correct short-incidence law. To use it, one
must map enough of these cone events to distinct eligible ORIGINAL F0
partner labels through exact physical dynamics. No shifted cone test
has been added to the definition of the target partner family F0.


<!-- END COMPLETE SOURCE 07 -->


---

<a id="document-08"></a>

## Document 08: PBBS_ORIGINAL_PROFILE_CONCENTRATION_20260907.md

Source: `/Users/amir.nuriyev/Documents/problem/scratch/PBBS_ORIGINAL_PROFILE_CONCENTRATION_20260907.md`

[Portable document](sources/essential/project/scratch/PBBS_ORIGINAL_PROFILE_CONCENTRATION_20260907.md) · [Exact original](originals/project/scratch/PBBS_ORIGINAL_PROFILE_CONCENTRATION_20260907.md)

<!-- BEGIN COMPLETE SOURCE 08 -->

# Quantitative regularity of the original PBBS pruning profile

2026-09-07. Root pure-proof deduction; no computation.
The complete proof passed independent root, task05 and task08 audits.
It addresses the first two ORIGINAL pruning counts, not the law of a
reached root or the short-return trajectory.

## 1. Cyclic equality-edge pruning

For a cyclic binary word w of odd length n>=3, let E(w) be the cyclic
word formed by recording the common bit on each edge whose two bits
are equal, in cyclic edge order. Define

    N_1(w)=|E(w)|,    N_2(w)=|E(E(w))|.

Every cyclic binary word has an even number of unequal edges. Hence
E(w) has positive odd length, and these definitions are unambiguous.
For a one-letter cyclic word its unique self-edge counts as equal.

For a rooted Dyck word D of semilength r, put n=2r+1 and w=0D.
The accepted equality-particle/pruning identity identifies the recorded
word E(0D), up to its root, with 0(partial D), where partial removes
all peaks simultaneously. Applying it twice gives

    N_1=2r_1+1,    N_2=2r_2+1,

where r_j is the semilength after j pruning rounds. This is the sole
PBBS-specific input. It is explicitly proved in Section1 of the
accepted source
/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_gaussian_clock_genealogy_structural_audit.md.

The level-zero composition parameters are therefore

    p=N_1,    ell=(n-2N_1+N_2)/2.                     (1)

## 2. Exact expectations before conditioning

Now take the n bits of w independently and uniformly. Then

    E N_1=n/2,
    E N_2=n/3+epsilon_n,
    epsilon_n=(n/6)4^(-(n-3)/2).                       (2)

The first identity is immediate from the n edges. For the second,
let V be the number of unequal consecutive bits in E(w). Then
N_2=N_1-V.

For a fixed original equality edge at i, suppose the next equality
edge is at i+m, in the forward direction. Their recorded bits differ
exactly when m is even: the m-1 intervening edges are all unequal.
For 1<=m<=n-2 the required two equality edges and intervening unequal
edges prescribe m+2 consecutive bits, up to one free initial bit.
Their probability is 2^(-(m+1)). Only

    m=2,4,...,n-3

contribute to V. The remaining distinct-edge distance m=n-1 would
leave n-2 unequal edges around the original cycle, an odd number,
and is impossible. If there is only one equality edge, its return
to itself gives no unequal adjacency in E(w).

Every unequal adjacency of E(w) is counted exactly once in this way.
Thus

    E V=n sum_(j=1)^((n-3)/2) 2^(-(2j+1))
       =(n/6)(1-4^(-(n-3)/2)),

with the empty sum at n=3. Subtraction proves (2).

## 3. Bounded changes and elementary concentration

Changing a single original bit toggles equality on exactly its two
incident original edges. All other recorded edge bits are unchanged.
Thus E(w) changes by at most two cyclic insertions/deletions.

One insertion or deletion in a cyclic binary word changes its number
of equal adjacencies by at most one. Indeed inserting x between a,b
changes that count by

    1_{a=x}+1_{x=b}-1_{a=b},

which is +1 or -1 for binary symbols. The same bound holds for the
empty and one-letter intermediates: the empty edit-intermediate has
equal-adjacency count zero, and a one-letter cycle has count one.
Therefore changing one original bit changes EACH of N_1,N_2 by at
most two.

For completeness, exposing independent input bits successively gives
a martingale for either statistic. Each conditional martingale increment
has mean zero and range of length at most two. For a mean-zero variable
of range length c, the log moment generating function has second
derivative equal to a tilted variance, at most c^2/4. Integrating twice
from zero gives log E exp(lambda X)<=lambda^2 c^2/8. Iterating this
bound over the n martingale increments and optimizing lambda gives

    Pr(|N_j-E N_j|>a)<=2 exp(-a^2/(2n)).

A union bound for j=1,2 yields

    Pr(max_j |N_j-E N_j|>a)<=4 exp(-a^2/(2n)).          (3)

No independence between N_1 and N_2 is used.

## 4. Conditioning to the uniform Dyck root

The event that w is exactly 0D for some Dyck_r word has probability

    Cat_r/2^n >= 1/[2(r+1)n].

Indeed Cat_r=binom(2r,r)/(r+1), and the largest of the n binomial
coefficients in the sum4^r is at least4^r/n. Conditional on this
event, D is uniform. Thus (3) gives the finite bound

    Pr_D(max(|N_1-n/2|,|N_2-n/3-epsilon_n|)>a)
        <=8(r+1)n exp(-a^2/(2n)).                     (4)

Let

    a_n=sqrt(24n log(n+1))

and let BAD denote the event in (4) with a=a_n. Since r+1=(n+1)/2,

    Pr_D(BAD)<=4n/(n+1)^11<=4/(n+1)^10.               (5)

On the complement,

    |p-n/2|<=a_n,
    |ell-n/6|<=(3/2)a_n+epsilon_n/2.

In particular, uniformly on these good profiles as n tends to infinity,

    p/n=1/2+O(sqrt(log n/n)),
    ell/p=1/3+O(sqrt(log n/n)).                       (6)

The centering epsilon_n in the finite statement is retained; it
decays exponentially and causes no asymptotic loss.

## 5. Discarding bad profiles without an unknown normalizer

Use the physical PBBS convention in which a retained repair trace
has T+2 edges, and the full physical factor has W=n Cat_r births.
Fix ANY integer cutoff H<r and retain any specified subclass of
births with T<=H. Let U_BAD be the union of its traces whose ORIGINAL
root profile is BAD. Counting trace incidences gives

    |U_BAD|/W
       <= E_D[(T+2)1_{T<=H}1_BAD]
       <= (H+2)Pr_D(BAD)
       <= 4(r+1)/(n+1)^10
       = 2/(n+1)^9.                                 (7)

This bound holds before normalizing an incidence probability law,
and regardless of how rare the retained subclass is. Additional
restrictions on the birth event only make the bound smaller.

Hence the occupied-support problem for Gaussian-short repairs,
including the residual B>J_r sector, may discard BAD original
profiles at o(W) cost. On all remaining profiles p is linear in r,
ell/p tends uniformly to1/3, and every H=o(r) satisfies H=o(p).
These are exactly the profile assumptions of the original-slot
geometric limit in the finite incidence kernel.

If the full retained raw-incidence normalizer mu tends to zero,
its occupied support is already o(W). Otherwise, on subsequences
where mu>=epsilon>0, (7) also makes BAD incidence probability o(1).
There is no need to claim that normalized incidence profiles are
typical uniformly when mu is arbitrarily small.

This does NOT make the deeper arrays typical under their incidence
weight, control the predecessor-visit intervals, prove growing-lag
independence, or bound the remaining product mu E_inc[1/K].
It removes the first-level profile-conditioning issue only.

## 6. Restriction preserves congestion on good components

The accepted original pruning profile is invariant under the physical
PBBS dynamics, including the root shift tau. Thus GOOD and BAD profiles
occupy disjoint physical components. For any retained birth family A,
its edge congestion satisfies the exact identity

    K_(A intersect GOOD)(e)=1_GOOD(e) K_A(e).

In particular discarding BAD components does not change the congestion
of any retained good incidence. This is stronger than merely bounding
the difference of the occupied unions.

For the following slot-limit conclusion, SPECIALIZE the retained family
to A={m(profile)<=T<=H}, where m>=height is profile-measurable. All-short
births use m=height; the residual B>J_r family uses m=height+J_r+1.
Additional restrictions may inspect the conditioned environment below,
but not extra level-zero slot values. The slot conclusion is not claimed
for an arbitrary subclass A from the preceding paragraph.

For H=o(r), the uniform conditional original-slot lemma in task08's
finite incidence kernel now applies throughout GOOD for this family. It gives joint
total-variation convergence to independent geometric variables with
Pr(G=a)=(3/4)(1/4)^a for any FIXED number of distinct nonzero original
level-zero slots selected using only the profile, deeper arrays and
sampled offset j. On subsequences with mu bounded below, (7) shows
that mixing over the actual incidence law preserves this conclusion.
If mu tends to zero, occupied support is already negligible instead.

This statement concerns the selected slot VALUES only. The distribution
of the environment selecting their labels and lifetime-test intervals
is still uncharacterized. It gives no growing-number independence,
fresh reached-root law, or solution of the weighted reciprocal problem.


<!-- END COMPLETE SOURCE 08 -->


---

<a id="document-09"></a>

## Document 09: PBBS_EXACT_ALL_DEPTH_PRUNING_CENSUS_20260907.md

Source: `/Users/amir.nuriyev/Documents/problem/scratch/PBBS_EXACT_ALL_DEPTH_PRUNING_CENSUS_20260907.md`

[Portable document](sources/essential/project/scratch/PBBS_EXACT_ALL_DEPTH_PRUNING_CENSUS_20260907.md) · [Exact original](originals/project/scratch/PBBS_EXACT_ALL_DEPTH_PRUNING_CENSUS_20260907.md)

<!-- BEGIN COMPLETE SOURCE 09 -->

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



<!-- END COMPLETE SOURCE 09 -->


---

<a id="document-10"></a>

## Document 10: PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md

Source: `/Users/amir.nuriyev/Documents/problem/scratch/PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md`

[Portable document](sources/essential/project/scratch/PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md) · [Exact original](originals/project/scratch/PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md)

<!-- BEGIN COMPLETE SOURCE 10 -->

# Bounded Gaussian-short PBBS raw incidence

2026-09-08. Root pure-proof synthesis. Sections1-8 pass complete-file
root/helper/task05 audits, including the corrected Dyck convention and
the probability corollary. Sections9-10 also pass full independent
root-helper and task05 audits, including the actual birth-count packing
bound and the two correctly normalized all-short laws.
No computation. The theorem is about uniform ORIGINAL newborn
roots, not resampled reached states and not the incidence-biased law.

## 1. The theorem and its scope

Let D be a uniform Dyck word of semilength r. Write h for its height,
r_s for its size after s peak-pruning rounds, and T(D) for its PBBS
newborn lifetime INCLUDING the consuming update. A repair trace has
T+2 edges. For every fixed c>0, put H=floor(c sqrt(r)). Then

    mu_H:=E_D[(T+2)1_{T<=H}] = O_c(1).                 (1)

The same proof gives the stronger unweighted statement

    Pr_D(T<=floor(c sqrt(r)))=O_c(r^(-1/2)).           (1a)

The constant may depend on c. No uniform-in-growing-c bound is asserted.
The full raw trace incidence is therefore O_c(W), where
W=(2r+1)Cat_r. It need not be o(W): the already proved zero-budget
contribution has nonvanishing raw mass. Sufficient overlap, residual
packing, target repair and coefficient one are NOT consequences of (1).

The exact pruning census/edit facts and the finite original-clock path
identities used below are already proved in the root notes
PBBS_EXACT_ALL_DEPTH_PRUNING_CENSUS_20260907.md and
PBBS_SQRTLOG_GAUSSIAN_SHORT_INCIDENCE_20260907.md, and in task05's
pbbs_quantitative_clock_polylog_short_mass.md, Sections4-5. The new
random profile envelope and its complete deterministic use are proved
here. No inverse-height tail theorem is needed for this proof.

## 2. One-depth profile concentration without a conditioning cost

Set R=sqrt(r), n=2r+1. Equality pruning of an odd cyclic binary word w
has size N_s(w) after s rounds. Its accepted finite facts are

    N_s(0D)=2r_s+1;
    one bit flip changes N_s by at most2, uniformly in s;
    0<=E_iid N_s-n/(s+1)<=2sqrt(n), uniformly in s.     (2)

The last inequality follows from the exact cosine census and a Gaussian
sum integral, including all depths. At s=0 the size is constant.

Couple iid fair bits to the uniform slice with r ones by uniformly
flipping the excess or deficit of ones. Permutation symmetry makes the
output uniform on that slice. If K is the iid number of ones, then
2E|K-r|<=sqrt(n+1), so (2) gives

    |E_slice N_s-n/(s+1)|<=2sqrt(n)+sqrt(n+1).          (3)

Expose the bits of a uniform slice word in order. The two possible
completions after the next bit is chosen can be coupled by one swap:
add one uniform unused position to a uniform (k-1)-subset to obtain a
uniform k-subset. Their N_s values differ by at most4. Hence the Doob
increments have conditional range length at most4, and the elementary
bounded-range MGF bound gives

    E_slice exp(lambda[N_s-E_slice N_s])<=exp(2n lambda^2).

A word with r ones and r+1 zeros has exactly one rotation of the form
D0, with D Dyck in the convention1=up: cut after the FIRST minimum of
its one-minus-zero partial sums at times0,...,n-1. Later sums are at
least this minimum, and earlier sums are strictly larger, so every
proper partial sum after this cut is nonnegative, while the full sum
is -1. A later occurrence of the same minimum would fail after wrapping;
any larger cut level would encounter a smaller level, so the cut is
unique. Moving the terminal zero to the front gives the unique rotation
0D. Its n rotations are distinct because a nontrivial repetition would
divide the total excess1. Each Dyck root has exactly n slice preimages.
The entire rotation-invariant pruning profile has exactly the Dyck law
on this slice, with no probability reweighting. Equations (2)-(3) and
the MGF bound therefore imply, for every s>=0 and x>=0,

    Pr_D(|r_s-r/(s+1)|>4R+xR)<=2exp(-x^2/6).          (4)

This is also the complete finite argument in task05's
pbbs_fixed_count_pruning_profile_subgaussian.md, which root has fully
read. Across-depth independence is neither needed nor asserted.

## 3. A profile-measurable subGaussian envelope parameter

Put e_s=r_s-r/(s+1), J=ceil(R), and for each integer1<=j<=J define

    g_j=ceil(R/j)-1.

Index both depths g_j and g_j-1 when nonnegative. Repeated indices
are harmless: the following union bound is over indexed copies.
Define the following function of the FULL ORIGINAL profile:

    a=1+max_{indexed (j,t)}
          [ (|e_t|/R-4)_+/8-sqrt(log(j+2)) ]_+ .     (5)

In particular a>=1. Applying (4) to at most two indices per j gives,
for x>=0 and p=64/6>2,

    Pr(a>1+x)
       <=4sum_{j>=1} exp[-p(x+sqrt(log(j+2)))^2]
       <=C exp(-p x^2).                              (6)

Thus all fixed exponential moments of a are bounded uniformly in r.

We claim, with one absolute constant C0 (for example64), that

    |e_s|<=E_s:=C0 R[a+sqrt(log(2+R/(s+1)))]
                    for EVERY integer s>=0.          (7)

Here is the interpolation, including its rounding. Let v=R/(s+1).
If v>1 is not an integer, put j=floor(v). Then

    u=g_{j+1}<=s<=w=g_j-1.

Both indexed endpoints exist. Monotonicity gives r_u>=r_s>=r_w.
Their deterministic means bracket r/(s+1) within R: the endpoint
means lie between jR and (j+1)R whenever this bin contains s.
Their indexed bounds from (5), with logarithms at j and j+1, prove
(7), absorbing this R interpolation error and the additive constants.
If v is an integer j, then g_j=s and no interpolation is needed.
If v<=1, then g_1<=s, r_s<=r_{g_1}, and both deterministic means
are at most R. This proves (7) on all larger depths as well, including
after extinction. Large one-step drops are why both crossing indices
were included in the grid. C0=64 dominates the displayed constants.

## 4. A legal profile-dependent depth

For t>=1 write

    E(t)=C0 R[a+sqrt(log(2+R/t))],    E_s=E(s+1),
    A=a+sqrt(log(a+2)).

We have 1<=A<=3a. Choose a sufficiently small positive constant
kappa=kappa_c; all requirements on it are stated below. Set

    L=floor(kappa R/A).                               (8)

The FULL profile determines a and L before any inverse-pruning row is
examined. Conditional on that profile, L is a deterministic integer.

For L>=2, flooring gives

    L>=kappa R/(2A),
    L E(L)/r<=delta_kappa,
    delta_kappa:=C0 kappa[1+sqrt(log(8/kappa))].        (9)

Indeed R/L<=2A/kappa and
sqrt(log(2+2A/kappa))<=sqrt(log(a+2))+sqrt(log(8/kappa)).
The function tE(t) is increasing, while E(t) is decreasing. Thus for
t<=2L+2<=3L,

    tE(t)/r<=3L E(L)/r<=3delta_kappa.

Choose kappa so 3delta_kappa<=1/4. Equation (7) now yields

    (3/4)r/(s+1)<=r_s<=(5/4)r/(s+1),  0<=s<=2L+1.   (10)

In particular r_{2L}>0, so h>2L. This automatically deals with the
height condition; we do not discard a constant-probability low-height
set. Cases L<2 will be bounded directly at the end.

A second consequence needed below is

    E(1)<=L E(L),
    sum_{s=0}^{L-1}E_s<=C L E(L).                    (11)

For the sum, use
sqrt(log(2+R/t))<=sqrt(log(2+R/L))+sqrt(log(L/t))
for1<=t<=L, and sum the integrable decreasing function
sqrt(log(1/x)) over right endpoints t/L. No depth independence enters.

## 5. The deterministic clock potentials

For0<=s<L let

    ell_s=r_s-2r_{s+1}+r_{s+2}>=0,
    p_s=2r_{s+1}+1,
    q_s=ell_s/(r_s+r_{s+2}+1).

The convexity ell_s>=0 and monotonicity of r_s are standard exact
pruning-profile properties. Define

    Phi=sum_{s<L}(s+1)q_s,
    A_t=sum_{t<s<L}(s-t)q_s,
    B_L=sum_{t<L}(t+1)q_t exp(-2A_t).

Uniformly for all profiles satisfying (7), with L>=2 as in (8),

    Phi>=log L-C,
    A_t>=log[L/(t+1)]-C,  0<=t<L,
    B_L<=C.                                           (12)

All constants here are absolute once C0 is fixed; they do not depend
on a, r, or the profile. We prove the error accounting in full.

Let

    b_s=r/(s+1)+r/(s+3),
    beta_s=1/b_s=[s+2-1/(s+2)]/(2r).

The actual denominator differs from b_s by at most3E_s. Comparability
(10) consequently gives

    |q_s-beta_s ell_s|<=C(s+2)^2 E_s ell_s/r^2,
    q_s<=C(s+2)ell_s/r.                               (13)

It is essential not to replace the correlated E_s ell_s product by
separate averages. Instead let f_s=(s+2)^3 E_s. This sequence is
increasing, and its interior second differences obey

    |f_s-2f_{s-1}+f_{s-2}|<=C(s+2)E_s,       s>=2.    (14)

For completeness put u=log(2+R/t), alpha=R/(2t+R), g=sqrt(u).
Direct differentiation gives

    g'=-alpha/(2t sqrt(u)),
    g''=[alpha(2-alpha)/(2sqrt(u))
               -alpha^2/(4u^(3/2))]/t^2>=0.

Since u>=log2, |tE'| and t^2 E'' are at most E/(2log2).
Thus f(t)=(t+1)^3E(t) is increasing and |f''(t)|<=C(t+1)E(t).
On the backward interval of length two, the argument ratios are at
most3 and E changes by at most an absolute factor. Integrating f''
proves (14). The initial two summation coefficients are O(E(1)).

For any increasing weights f_s, the last two summation-by-parts terms
against ell_s are

    -[f_{L-1}-f_{L-2}]r_L-f_{L-1}(r_L-r_{L+1})<=0.

Apply this with (14) and the upper bound in (10). It yields

    sum_{s<L}(s+2)^3 E_s ell_s
       <=C r[E(1)+sum_{s<L}E_s].                     (15)

Consequently the total reciprocal-denominator debit in either Phi
or A_t is, by (11), at most

    C r^-2 sum_{s<L}(s+2)^3 E_s ell_s
       <=C L E(L)/r<=C delta_kappa=O(1).              (16)

For the baseline terms, convexity with m=floor(L/2) and (10) gives

    r_L<=Cr/L,
    d_L:=r_L-r_{L+1}<=[r_m-r_L]/(L-m)<=Cr/L^2.

The exact identity

    sum_{s<L}(s+1)^2ell_s
       =r+2sum_{j=1}^{L-1}r_j-(2L-1)r_L-L^2d_L

and (11) bound it below by2r log L-Cr. Since
(s+1)beta_s>=(s+1)^2/(2r), (16) proves the Phi bound.

For A_t use g_s=(s-t)[s+2-1/(s+2)] for s>=t. The first nonzero
summation coefficient is at least2, the interior second differences
are2+2(t+2)/[s(s+1)(s+2)]>=2, and the two final terms are O(r)
uniformly in t. Thus its beta_s baseline is at least

    sum_{j=t+1}^{L-1}r_j/r-C
       >=log[L/(t+1)]-C-r^-1 sum_{j<L}E_j
       >=log[L/(t+1)]-C.

The empty t=L-1 case is immediate. Equation (16) proves the second
part of (12). Finally ordinary polynomial summation by parts and
(10) give sum_{s<L}(s+2)^4ell_s<=CrL^2. With (13),

    B_L<=C/(rL^2) sum_{s<L}(s+2)^4ell_s<=C,

completing (12).

## 6. Exact original-row clock bound at the chosen depth

Conditional on the FULL original profile, the original rows Z_s are
independent uniform weak compositions of ell_s into p_s parts.
They are queried in fixed original order0,-1,-2,... . If W_s is the
sum of the queried entries, the exact clock recurrence is

    n_s=s+1+2sum_{t<s}(s-t)W_t,
    m_L=1+2sum_{s<L}W_s.                               (17)

Thus each query count depends only on earlier original rows. For a
specified path with sum W_s<=K and p_s>=2(n_s+W_s), the exact
composition-prefix probabilities give

    Pr(path | profile)
       <=Q0 product_{t<L}
          [6(K+1)(t+1)q_t exp(-2A_t)]^(W_t)/W_t!,
    Q0<=exp(-Phi).                                    (18)

These finite identities and inequalities are the previously audited
original-clock path bound, not an independent-slot approximation.
Using (12) and the multinomial theorem to sum the nonnegative paths,

    Pr(sum_{s<L}W_s<=K | profile)<=C/L exp[C(K+1)].    (19)

We check every depth/size requirement for the physical use of (17).
On L>=2, (10) implies uniformly s<L

    p_s>=r/L>=RA/kappa.

Every short physical lifetime T<=H has clock length2T+1<=2H+1.
Choose kappa additionally small enough depending only on fixed c so
p_s>2H+1. Then the accepted physical clock partition applies through L.
Since h>2L, its disjoint depth-L leaves each have length at least
2(h-L)+1; on a short lifetime this forces sum W_s<=H/h.
Set K=ceil(H/h). Every path included in (19) has

    n_s+W_s<=3(K+1)(s+1)<=(3/2)H+6L.

Taking, for example, kappa<=1/[100(c+1)] in addition to the earlier
condition makes p_s>=2(n_s+W_s) for all sufficiently large r. Thus
all physical and composition conditions hold for EVERY summed path.
Equations (18)-(19) imply, conditional on this original full profile,

    Pr(T<=H | profile)<=C/L exp[C(1+H/h)].             (20)

There is no new conditioning on a reached profile. The cutoff L is a
function only of the original profile, which was already conditioned on.

## 7. Average the profile bound; no discarded profile sector

For L>=2, use (9) and h>2L in (20). The conditional raw incidence is
at most

    C(H+2)/L exp[C(1+H/h)]<=C_c A exp(C_c A).          (21)

For L<2, the floor in (8) means R<2A/kappa. The trivial conditional
bound H+2 is then at most C_c A, so (21) remains valid without using
any clock argument. Small finite r can also be absorbed into C_c.

Finally A<=3a, and (6) makes E[A exp(C_c A)] finite uniformly in r.
Averaging (21) proves mu_H<=C_c, which is (1).

For (1a), retain the probability form of (20): when L>=2 it is
at most C_c A exp(C_c A)/R. When L<2, R<2A/kappa implies the
trivial bound1<=2A/(kappa R). Averaging over the same envelope
parameter therefore gives Pr(T<=H)<=C_c/R. Multiplying by H+2
is also a direct proof of (1).

## 8. Exact remaining gap

The occupied-edge fraction is mu_H E_inc[1/K_overlap]. Bounded mu_H
reduces this question to overlap control, but supplies none by itself.
The positive-budget residual and the low-score trajectory estimate in
PBBS_SQRTLOG_SCORE_TO_PACKING_REDUCTION_20260907.md remain open.
No low-score hypothesis, fresh-root law, stationary-incidence law or
coefficient-one conclusion was used or established in this proof.

## 9. A handled sector: positive early original triangles

Let S be any deterministic integer1<=S<=sqrt(r). In the cyclic original
row coordinates, define

    B_S={sum_{s=0}^{S-1} sum_{i=0}^s Z_{s,-i}>0}.     (22)

Rows beyond extinction are extended by their unique zero composition.
Indices are interpreted in the original cyclic row; on every safe
clock used below the queried prefixes are shorter than its circumference
and contain distinct slots. There is no shifted-root sampling in (22).

Uniformly in S,

    Pr(T<=H, B_S)<=C_c S^2/r^(3/2),
    E[(T+2)1_{T<=H,B_S}]<=C_c S^2/r.                 (23)

To prove this, condition on the complete original profile as before.
First suppose L>=max(S,2). Put b_t=(t+1)q_t exp(-2A_t). Equation (12),
(13), and polynomial summation by parts truncated at S give

    sum_{t<S}b_t
       <=C/(rL^2) sum_{t<S}(t+2)^4ell_t
       <=C S^2/L^2.                                 (24)

The terminal terms of the truncated summation are nonpositive. Its
interior bound uses r_s<=Cr/(s+1) through S+1; for S=1 use ell_0<=r.
On a safe short clock, (22) is equivalent to W_t>0 for some t<S:
before the first positive row, (17) queries exactly0,-1,...,-t;
conversely every actual query prefix contains these t+1 original slots.

Keep this restriction while summing (18). After applying the path bound
on total W<=K, enlarge only the NONNEGATIVE WEIGHT sum to all paths.
With theta=6(K+1), its restricted exponential sum is

    exp(theta B_L)-exp(theta[B_L-sum_{t<S}b_t])
       <=theta (sum_{t<S}b_t)exp(theta B_L).

Together with Q0<=C/L and (24), this proves

    Pr(T<=H,B_S | profile)
       <=C S^2/L^3 exp[C(K+1)]
       <=C_c (S^2/R^3) A^3 exp(C_c A).               (25)

All probability bounds were applied only to the paths whose size
hypotheses were checked in Section6; adding the other product weights
does not assert that they are possible physical paths.

If L<max(S,2), then A>kappa R/(2S). Therefore

    1_{L<max(S,2)} <=4S^2 A^2/(kappa^2 R^2).

The GLOBAL conditional probability bound proved with (1a), including
L<2, is C_c A exp(C_c A)/R. Multiply it by this indicator bound,
and ignore B_S. This gives the same upper bound as (25) without using
an unsafe genealogy. Averaging (25) over a, whose fixed exponential
moments are uniformly finite, proves the first part of (23). Multiplying
by H+2 proves its raw-incidence part.

In physical coordinates there are at most

    C_c W S^2/r^(3/2)

such short births, so their maximum edge-disjoint repair packing is
bounded by that same number. Consequently for EVERY prescribed
S=S_r=o(sqrt r), all Gaussian-short births with a positive original
triangle before S have packing o(W/sqrt r), and raw incidence o(W).
This conclusion needs no division by the budget cutoff J_r.

The remaining short births have all entries of the growing original
triangle in (22) equal to zero, including Z_{0,0}=0. No abundance of
overlapping SHIFTED short births follows from that unshifted condition.
The packing of this complementary sector and coefficient one remain
open. Estimate (23) strengthens the separately audited earlier
logarithmic-cutoff early-branch bound from task08.

## 10. Sharp orders and the two correctly normalized short laws

The accepted elementary zero-budget Gaussian-band lower bound in
PBBS_TRUE_GAUSSIAN_RAW_CENSUS_OBSTRUCTION_20260907.md supplies, for
every fixed0<a_0<b_0<min(c,1/2), at least a positive constant times
r^(-1/2) newborn probability with T=h in[a_0 sqrt r,b_0 sqrt r].
Those lifetimes lie below H for all sufficiently large r. Their
T+2 weights are at least a_0 sqrt r. Together with (1) and (1a),
this proves the matching orders

    Pr(T<=floor(c sqrt r))=Theta_c(r^(-1/2)),
    E[(T+2)1_{T<=floor(c sqrt r)}]=Theta_c(1).         (26)

This invokes only the previously accepted elementary positive lower
bound, not a new local-limit or independence assertion.

Consequently (23) can be normalized under either of the following
ACTUAL all-short laws:

    Pr(B_S | T<=H)=O_c(S^2/r),
    Pr_short-inc(B_S)=
       E[(T+2)1_{T<=H,B_S}]/mu_H=O_c(S^2/r).         (27)

Both statements hold uniformly for deterministic1<=S<=sqrt r.
Thus every prescribed S=o(sqrt r) gives an all-zero original
triangle through S with probability1-o(1) under BOTH laws. They
are not statements about a positive-budget-only or other restricted
incidence law whose normalizer might be smaller. Nor do they imply
that nearby shifted newborns remain short or share a repair witness.


<!-- END COMPLETE SOURCE 10 -->


---

<a id="document-11"></a>

## Document 11: PBBS_SQRTLOG_GAUSSIAN_SHORT_INCIDENCE_20260907.md

Source: `/Users/amir.nuriyev/Documents/problem/scratch/PBBS_SQRTLOG_GAUSSIAN_SHORT_INCIDENCE_20260907.md`

[Portable document](sources/essential/project/scratch/PBBS_SQRTLOG_GAUSSIAN_SHORT_INCIDENCE_20260907.md) · [Exact original](originals/project/scratch/PBBS_SQRTLOG_GAUSSIAN_SHORT_INCIDENCE_20260907.md)

<!-- BEGIN COMPLETE SOURCE 11 -->

# Square-root-logarithmic Gaussian-short PBBS incidence

2026-09-07. Root pure proof, independently derived by a root helper.
The complete written proof passes an independent root audit. No computation.
This strengthens the accepted
O_c((log r)^2) short-clock bound; it does not prove shared repair or
coefficient one.

## 1. Statement and precise inputs

Let D be uniform among Dyck words of semilength r. Let T(D) be the
accepted PBBS newborn lifetime INCLUDING its consuming update. Write h
for the Dyck height, n=2r+1 and W=n Cat_r. For fixed c>0 set
H=floor(c sqrt(r)) and

    mu_H=E_D[(T+2) 1_{T<=H}].

Then

    mu_H=O_c(sqrt(log(r+1))).                         (1)

Thus the RAW total length of these repair traces is at most
O_c(W sqrt(log r)). This is not a bound of o(W) on that raw total.

Inputs are the exact all-depth pruning census in
PBBS_EXACT_ALL_DEPTH_PRUNING_CENSUS_20260907.md and the original-clock
identities, exact composition path bound and inverse-height tail in
/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_quantitative_clock_polylog_short_mass.md,
Sections4-6. The deterministic estimates that change the cutoff are
proved here; the probabilistic inputs are repeated explicitly below.

## 2. An absolute-error profile event

Let r_s be the size after s rounds of peak pruning. The exact census,
with iid cyclic fair bits before conditioning to0D, gives

    E_iid N_s=n/(s+1) sum_{j=0}^s cos^(n-1)(pi j/(s+1)),
    N_s(0D)=2r_s+1.

Its Gaussian upper bound and a decreasing-function integral give,
UNIFORMLY in every s>=0,

    0<=E_iid N_s-n/(s+1)
       <=[2n/(s+1)] sum_{j>=1} exp(-a_s j^2)
       <=sqrt(2/pi) n/sqrt(n-1)<=2sqrt(n),
    a_s=(n-1)pi^2/[2(s+1)^2].                         (2)

The s=0 case is immediate. The depth-uniform two-edit concentration,
union bound through r+1 depths, and Dyck conditioning in that note give

    Pr_D(exists1<=s<=r+1:
         |N_s-E_iid N_s|>sqrt(32n log(n+1)))
       <=2/(n+1)^13.                                 (3)

For all sufficiently large r put

    a=16sqrt(r log(r+1)),   kappa=1/64,
    L=floor(kappa r/a).

Equations (2)-(3), and |[n/(s+1)-1]/2-r/(s+1)|<=1/2,
show that outside the event in (3),

    |r_s-r/(s+1)|<=a       for EVERY s>=0.             (4)

For s>r the Dyck core is empty, so that part is automatic.
Call (4) GOOD. BAD contributes at most

    (H+2)Pr(BAD)<=2(H+2)/(n+1)^13=o(1)                (5)

to mu_H. There is no division by an unknown incidence normalizer.

## 3. Deterministic summation with absolute errors

The following estimates hold whenever a>=1, L>=2,
aL/r<=kappa, and the nonnegative decreasing convex sequence r_s
satisfies (4) through L+1, with r_0=r. All constants below are absolute.
Put

    ell_s=r_s-2r_{s+1}+r_{s+2}>=0,
    p_s=2r_{s+1}+1,
    q_s=ell_s/(p_s+ell_s)=ell_s/(r_s+r_{s+2}+1),
    N_s=s+1,                       0<=s<L.

For large r, a(L+2)/r<=1/8; hence throughout this range
r_s is comparable to r/(s+1). Set

    b_s=r/(s+1)+r/(s+3),
    beta_s=1/b_s=[s+2-1/(s+2)]/(2r).

The actual denominator differs from b_s by at most3a. Since
b_s>=2r/(s+2), both denominators are comparable, and

    |q_s-beta_s ell_s|
       <=C a(s+2)^2 ell_s/r^2,
    q_s<=C(s+2)ell_s/r.                               (6)

Let d_L=r_L-r_{L+1}. Convexity with m=floor(L/2) gives

    r_L<=r/(L+1)+a,
    0<=d_L<=[r_m-r_L]/(L-m)
             <=C(r/L^2+a/L).                         (7)

For j=3,4, twice summing by parts gives

    sum_{s<L}(s+2)^3 ell_s<=C(rL+aL^2),
    sum_{s<L}(s+2)^4 ell_s<=C(rL^2+aL^3).             (8)

Here the initial coefficients contribute O(r), interior coefficients
are nonnegative and at most C(s+2)^(j-2), and the two terminal terms
are nonpositive: -[f_{L-1}-f_{L-2}]r_L-f_{L-1}d_L for increasing
f_s=(s+2)^j. Use r_s<=r/(s+1)+a in the interior sum. This proves
(8) without approximating the individual integer ell_s.

Define

    Phi=sum_{s<L}(s+1)q_s,
    A_t=sum_{t<s<L}(s-t)q_s,
    B_L=sum_{t<L}(t+1)q_t exp(-2A_t).

We claim

    Phi>=log L-C,
    A_t>=log[L/(t+1)]-C,        0<=t<L,
    B_L<=C.                                           (9)

For Phi, the beta_s baseline dominates (s+1)^2/(2r), and

    sum_{s<L}(s+1)^2ell_s
       =r+2sum_{j=1}^{L-1}r_j-(2L-1)r_L-L^2d_L
       >=2r log L-C(r+aL).

Its reciprocal-denominator correction, by (6) and the cubic moment
in (8), is at most

    C(a/r^2)(rL+aL^2)
       =C[aL/r+(aL/r)^2]=O(1).                       (10)

This proves the first part of (9). In particular no fixed relative
error is multiplied by log L.

For A_t let

    g_s=(s-t)[s+2-1/(s+2)],     s>=t.

Its first nonzero summation coefficient g_{t+1} is at least2, and its
interior second differences are

    g_s-2g_{s-1}+g_{s-2}
       =2+2(t+2)/[s(s+1)(s+2)]>=2.

For t<=L-2, summation by parts therefore bounds its baseline below by

    [1/(2r)] sum_{s=t+1}^{L-1}g_s ell_s
       >=sum_{j=t+1}^{L-1}1/(j+1)-C(1+aL/r)
       >=log[L/(t+1)]-C.

The two terminal terms are
-[g_{L-1}-g_{L-2}]r_L-g_{L-1}d_L= -O(r+aL),
using (7). The accumulated absolute profile errors cost at most O(aL),
and the reciprocal-denominator correction is again bounded by (10).
The empty case t=L-1 is immediate. This proves the second part of (9).
Finally (6), the second part of (9), and the quartic moment give

    B_L<=C/(rL^2) sum_{t<L}(t+2)^4ell_t
         <=C(1+aL/r)<=C,

proving the last part.

## 4. Transfer through the exact original clock

Conditional on the FULL pruning profile, the original arrays Z_s are
independent uniform weak compositions of ell_s into p_s parts. The
clock queries original slots0,-1,-2,... in each row. If W_s is their
sum, the exact original-row recurrence is

    n_s=s+1+2sum_{t<s}(s-t)W_t,
    m_L=1+2sum_{s<L}W_s.                              (11)

The row query count depends only on EARLIER rows. For a specified
nonnegative path with sum W_s<=K, the exact weak-composition formula
and p_s>=2(n_s+W_s) imply

    Pr(path | profile)
       <=Q0 product_{t<L}
          [6(K+1)(t+1)q_t exp(-2A_t)]^(W_t)/W_t!,
    Q0<=exp(-Phi).                                    (12)

These are the finite inequalities (15)-(17) in the accepted clock
note; they include the future zero-query penalty. Summing all paths,
using the multinomial theorem and (9), gives

    Pr(sum_{s<L}W_s<=K | profile)
       <=C/L exp[C(K+1)].                            (13)

On GOOD, p_s>=c_0 r/L=Theta(sqrt(r log r)) uniformly for s<L.
For a short physical lifetime T<=H these circumferences exceed
2H+1 for sufficiently large r, with c fixed, so (11) applies to the
actual physical genealogy through depth L.

When h>=2L, disjoint physical depth-L leaves each have length at
least2(h-L)+1. Their count in (11) consequently implies

    sum_{s<L}W_s<=H/h.

Take K=ceil(H/h). On paths with total at most K,

    n_s+W_s<=3(K+1)(s+1)
             <=(3/2)H+6L=O_c(sqrt r).

Thus p_s>=2(n_s+W_s) holds uniformly, validating (12) for every
summed path. Equations (12)-(13) prove

    Pr(T<=H | profile)
       <=C/L exp[C(1+H/h)]            on GOOD,h>=2L.  (14)

No adaptively reached profile is resampled.

## 5. Height integration and conclusion

The accepted exact-height coefficient estimate supplies

    Pr(h<=m)<=C exp[-r/(4(m+2)^2)],
    E exp(tX)<=C exp(Ct^2),
    X=sqrt r/(h+2),                 t>=0.             (15)

The coefficient estimate retains its h^(-4) prefactor before summing;
there is no missing polynomial-in-r loss in (15).
For L>=2,

    r/[4(2L+2)^2]>=r/(36L^2)
       >=16^2 log(r+1)/(36 kappa^2).

Therefore (H+2)Pr(h<2L)=o(1). On GOOD,h>=2L, multiply (14) by
H+2 and average over the full original profile. Since
H/h<=2cX, (15) at a fixed parameter depending only on c gives

    mu_H<=o(1)+C_c(H+2)/L
          =O_c(sqrt(log(r+1))),

as asserted. Height is profile-measurable, so this averaging makes
no false independence assumption.

## 6. What is still missing

The occupied-edge fraction is mu_H E_inc[1/K_overlap]. Estimate (1)
controls its first factor but does not prove sufficient overlap. In
particular O_c(1), o(1), and a vanishing occupied fraction are NOT
consequences of this note. Positive-budget residual packing and the
full-cube coefficient-one construction remain open.


<!-- END COMPLETE SOURCE 11 -->


---

<a id="document-12"></a>

## Document 12: PBBS_TOP_ZERO_ALL_SHORT_OVERLAP_REDUCTION_20260908.md

Source: `/Users/amir.nuriyev/Documents/problem/scratch/PBBS_TOP_ZERO_ALL_SHORT_OVERLAP_REDUCTION_20260908.md`

[Portable document](sources/essential/project/scratch/PBBS_TOP_ZERO_ALL_SHORT_OVERLAP_REDUCTION_20260908.md) · [Exact original](originals/project/scratch/PBBS_TOP_ZERO_ALL_SHORT_OVERLAP_REDUCTION_20260908.md)

<!-- BEGIN COMPLETE SOURCE 12 -->

# All Gaussian-short overlap reduces to zero top gaps, with no shifted triangle

2026-09-08. Root pure-proof synthesis. Complete independent root-helper
and task05 full-file audits PASS through Section5; Section6 also passes
an independent full root-helper audit. No computation. This is a
reduction, NOT a proof of the eligible-label abundance condition.

The new observation is to use the accepted early-triangle estimate at
depth S=1, instead of imposing a growing clean triangle and a residual
budget floor. This retains almost all ALL-short raw incidence, so its
normalizer is bounded above and below. Partners need no deeper-triangle
test. The remaining condition is ordinary divergence in probability of
one exactly defined number of distinct labels.

## 1. Inputs and physical normalization

Fix c>0. Let r tend to infinity, R=sqrt(r), n=2r+1,
H=floor(cR), and W=n Cat_r. A uniform original Dyck root D has
pruning profile (r_s), height h, and lifetime T including consumption.
Its physical repair trace has T+2 consecutive edges; T>=h. The full
physical PBBS factor has W edges, and each cycle has period at least n.
For sufficiently large r, H<r and H+2<n, so every short repair has
distinct edges. Physical births, not quotient-root shapes, are counted.

The accepted root theorem
PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md, Sections9-10, gives

    mu_H=E[(T+2)1_{T<=H}]=Theta_c(1),
    E[(T+2)1_{T<=H,Z_(0,0)>0}]=O_c(1/r).             (1)

The second statement is exactly its S=1 case: the triangle contains
only the nonnegative original entry Z_(0,0). No deeper row is tested.

Use GOOD from PBBS_ORIGINAL_PROFILE_CONCENTRATION_20260907.md. It is
invariant under the PBBS dynamics, depends only on the original profile,
and, with p=2r_1+1 and ell=r-2r_1+r_2, gives uniformly

    p/n=1/2+o(1),  ell/p=1/3+o(1),
    E[(T+2)1_{T<=H,BAD}]<=2/(n+1)^9.                 (2)

Let G be all births with T<=H and retain just

    F0={GOOD, T<=H, Z_(0,0)=0}.                      (3)

There is NO positive-budget restriction, small-height removal, or
deeper-triangle predicate in (3). Height one has T=r and is automatically
absent because H<r. Thus each positive-mass retained profile has h>=2.
Writing mu0=E[(T+2)1_F0], (1)-(2) imply

    delta:=mu_H-mu0=O_c(1/r),   mu0=Theta_c(1).       (4)

If U_G and U0 are the occupied-edge unions, every edge of U_G minus U0
is covered by at least one discarded trace. Counting discarded raw
incidences therefore proves

    0<=|U_G|/W-|U0|/W<=delta.                        (5)

This does not identify the two families' congestions; each congestion
below is consistently that of F0.

## 2. Exact base-incidence environment

The exact original-coordinate kernel and same-particle bound are in
task08's pbbs_original_incidence_window_kernel.md and the root note
PBBS_SAME_PARTICLE_SHORT_TRACE_MULTIPLICITY_20260907.md. Their physical
phase convention is retained here: tau=phi^2, birth shift d begins
at edge e_d and ends at e_(d+T(tau^d D)+1).

Sample a uniform F0 repair-edge incidence. Its environment is

    E=(profile, y, j),

where y comprises ALL original arrays at levels s>=1 and j is the
sampled edge offset. These data determine the entire signed-time reduced
omitted-site trajectory lambda_1(t), independently of row zero. In
particular lambda_1(0)=0. For every integer d define

    a_d=lambda_1(2d) mod p,
    N_d(t)=#{1<=v<=2t+1:lambda_1(2d+v)=a_d-1 mod p}.

For d in {j-H-1,...,j}, put

    L_d=max(h,j-d-1,1),
    I_d=[floor(N_d(L_d-1)/2),floor(N_d(H)/2)-1].       (6)

The interval is empty if L_d>H or its endpoints are reversed.
The exact kernel states that a short birth d covers e_j precisely
when Z_(0,a_d) belongs to I_d. The h floor uses only the universal
T>=h fact; no extra residual lifetime floor is present.

Every feasible base environment has GOOD profile and 0 in I_0. Set
N=p-1. Conditional on E, the base gap is Z_(0,0)=0 and

    (Z_(0,1),...,Z_(0,p-1))
       is uniform over weak compositions of ell into N parts. (7)

Indeed recording the offset j cancels the lifetime incidence weight.
All feasible original arrays at that fixed offset have the same atom
weight; after fixing Z_(0,0)=0, the only base lifetime/overlap test is
0 in I_0, already measurable from E. No remaining row-zero coordinate
is filtered. More explicitly the environment has mass

    binom(ell+N-1,N-1)/(Cat_r mu0)

when these conditions hold, and mass zero otherwise, with the physical
deck phase marginalized out. This is the ACTUAL incidence law, not the
unweighted deeper-array distribution or a newly sampled reached root.

## 3. Eligible distinct labels and an exact hypergeometric law

Define

    V_i(E)={d in {j-H-1,...,j}:a_d=i and 0 in I_d},
    k0(E)=#{i in {1,...,p-1}:V_i(E) is nonempty}.      (8)

The eligibility tests are exclusively the original signed trajectory
and the two count thresholds in (6). Equivalently 0 in I_d means

    L_d<=H, N_d(L_d-1)<=1, N_d(H)>=2.                (9)

No shifted-triangle test is included. The candidate labels are selected
before examining any remaining top-row gap. Let Y count those k0
eligible nonzero labels whose top-row gap equals zero.

An F0 birth d covers the sampled edge exactly when 0 in I_d and
Z_(0,a_d)=0: GOOD is invariant and no other membership condition exists.
The base contributes one. Every label counted in Y contributes at least
one. The same-particle theorem gives at most one such contribution per
zero-gap label, except that the single current label a_j may contribute
two. Consequently the ACTUAL F0 congestion satisfies pointwise

    1+Y<=K0<=2+Y.                                   (10)

The proof counts distinct labels rather than independently counting
repeated visits to one label. It includes both trace boundary edges.

For ell>=1, stars and bars applied to (7) gives probability
(N-1)_q/(ell+N-1)_q that any q specified slots all vanish. Thus

    Y | E ~ Hypergeom(ell+N-1,N-1,k0).               (11)

These all-subset probabilities determine the indicator-vector law.
For ell=0, Y=k0 deterministically instead. The identity
binom(Q,y)/(y+1)=binom(Q+1,y+1)/(Q+1), followed by Vandermonde, yields

    E[1/(Y+1)|E]
      =(ell+N)/(N(k0+1))
         *[1-binom(ell,k0+1)/binom(ell+N,k0+1)]
      <=(1+ell/N)/(k0+1).                            (12)

The deterministic ell=0 case satisfies the same upper bound. On GOOD,
ell/N->1/3 uniformly, so (10)-(12) imply, for large r,

    1/[2(k0+1)]<=E[1/K0|E]<=2/(k0+1).               (13)

## 4. The exact remaining qualitative condition

Incidence counting within F0 is exact:

    |U0|/W=mu0 E_inc,F0[1/K0].

Together with (5) and (13), this gives the two-sided bounds

    (mu0/2) E_inc,F0[1/(k0+1)]
      <=|U_G|/W
      <=delta+2mu0 E_inc,F0[1/(k0+1)].               (14)

Because delta->0 and mu0 is bounded above AND away from zero, these
statements are equivalent as r tends to infinity at fixed c:

    (i)   |U_G|=o(W);
    (ii)  E_inc,F0[1/(k0+1)]->0;
    (iii) for EVERY FIXED M, Pr_inc,F0(k0<=M)->0.      (15)

For (ii)=>(iii), bound the reciprocal below by1/(M+1) on k0<=M.
For the converse, split its expectation at M, bound by
Pr(k0<=M)+1/(M+1), take r to infinity, then M to infinity.
Thus (iii) is precisely k0 tending to infinity in probability under
the specified actual incidence-environment law, with no quantitative
rate, growing threshold, or unknown vanishing normalizer.

If (15) is proved, the accepted occupied-support-to-packing theorem
PBBS_OCCUPIED_SUPPORT_TO_PACKING_20260908.md gives packing(G)=o(W/R).
In fact, writing v=|U_G|/W, its finite modulus gives

    packing(G)<=C_c (W/R) v sqrt(log(e/v)).

This directly handles all fixed-Gaussian short births, not only the
positive-budget residual. The already proved low-budget and early-
triangle results remain valid and may still help establish (iii), but
they need not be imposed as extra membership tests on partners in (8).

Condition (iii) is STILL UNPROVED. Nothing here supplies enough eligible
labels, establishes a growing-c bound, or completes the remaining word
compiler. The equivalence is to the occupied-support property (i), not
to the full conjecture or to a necessary condition for arbitrary words.

## 5. A useful admissible restriction: all gaps through the safe depth

This additional lemma passes independent root-helper and task05 audits. It removes very large
original gaps from the actual incidence problem, but supplies no bound
on the amplification of small gaps by shifted dynamics.

Use the accepted profile envelope parameter a>=1, A<=3a, and
L=floor(kappa_c R/A). On L>=2 its proved profile bounds are

    (3/4)r/(s+1)<=r_s<=(5/4)r/(s+1), 0<=s<=2L+1,
    h>2L,  L<=R,  Pr(a>1+x)<=C exp(-b x^2).

For each row s<L, monotonicity gives ell_s<=r_s. With p_s=2r_(s+1)+1,

    ell_s/(ell_s+p_s-1)
      <=5(s+2)/[5(s+2)+6(s+1)]<=5/8.                (16)

For a uniform weak composition of ell_s into p_s parts, any specified
slot satisfies

    Pr(Z_(s,i)>=m | profile)
      =(ell_s)_m/(ell_s+p_s-1)_m <=(5/8)^m,          (17)

with value zero if m>ell_s. The ratios decrease at successive factors,
so the inequality holds for every integer m>=1. There are at most
L(2r+1)<=3r^(3/2) slots in the first L rows. Conditional on the profile,
a union bound therefore bounds ANY gap at least m in these rows by
3r^(3/2)(5/8)^m. No across-row independence is needed for this step.

To transfer this bound to F0 incidence, use its actual density
(T+2)1_F0/mu0, bounded by C_c R in view of (4). Also L<2 implies
a>kappa_c R/6, so its newborn probability is at most C_c exp(-b_c r),
and multiplying by C_c R preserves such an exponential bound. Hence

    Pr_inc,F0(L<2 OR some Z_(s,i)>=m with s<L)
      <=C_c r^2(5/8)^m+C_c exp(-b_c r).              (18)

For any fixed D>0, taking

    m=ceil((D+3)log(r+1)/log(8/5))

makes (18) O_(c,D)(r^(-D)). This controls ALL original slots through
the random safe depth, including adaptively selected labels there,
under the actual incidence law. In particular a counterexample
requiring a macroscopic level-one gap lies in a negligible exceptional
set. A [later audited construction] (historical local link not bundled)
uses only logarithmic gaps while making an adjacent virtual lifetime
of order sqrt(r)log(r), with a base lifetime of order sqrt(r), on the
same GOOD profile class. Thus these gap bounds do not imply uniform
one-step Gaussian-scale endpoint stability. That exceptional family's
frequency and k0 divergence remain separate questions.

## 6. The profile envelope remains tight under actual short incidence

This further lemma passes independent full proof audit. Unlike the whole-root
density bound used for the gap union in Section5, conditioning only on
the PROFILE lets us retain the sharp short-birth normalization.
The accepted global clock estimate, valid on every profile, is

    Pr(T<=H | profile)<=C_c A exp(C_c A)/R.           (19)

For any profile event E, the F0-incidence probability is at most

    (H+2)/mu0 * E[1_E Pr(T<=H | profile)]
      <=C_c E[A exp(C_c A)1_E].                      (20)

This is an inequality, not a claim that the original profile law is
unchanged. Since A<=3a and the newborn a has a uniform subGaussian
tail, Cauchy-Schwarz and its finite exponential moments imply

    Pr_inc,F0(a>1+x)<=C_c exp(-b_c x^2), x>=0.       (21)

The constants may be enlarged for bounded x. There is no extra factor
R in (21): the factor R from the maximal incidence weight is cancelled
by the conditional1/R in (19).

For every deterministic integer1<=S<=R, the event
L<max(S,2) forces A>kappa_c R/(2S) and hence a>kappa_c R/(6S).
Applying (21), and absorbing bounded R/S into its constant, proves

    Pr_inc,F0(L<max(S,2))<=C_c exp(-b_c r/S^2).      (22)

The raw early-triangle bound and mu0=Theta_c(1) also give

    Pr_inc,F0(Triangle_S>0)<=C_c S^2/r.              (23)

Thus for EVERY prescribed S=o(sqrt r), with S>=1, the sampled base
simultaneously has a zero original triangle through S and a valid safe
clock depth at least max(S,2), with probability tending to one. Neither
condition is imposed on its candidate partner births. This supplies
a legitimate high-probability base restriction for conditional finite-
layer arguments. It does not prove their claimed fibre law, any shifted
lifetime comparison, or eligible-label divergence.


<!-- END COMPLETE SOURCE 12 -->


---

<a id="document-13"></a>

## Document 13: PBBS_TWO_ROW_VIRTUAL_ZERO_CLOCK_REDUCTION_20260908.md

Source: `/Users/amir.nuriyev/Documents/problem/scratch/PBBS_TWO_ROW_VIRTUAL_ZERO_CLOCK_REDUCTION_20260908.md`

[Portable document](sources/essential/project/scratch/PBBS_TWO_ROW_VIRTUAL_ZERO_CLOCK_REDUCTION_20260908.md) · [Exact original](originals/project/scratch/PBBS_TWO_ROW_VIRTUAL_ZERO_CLOCK_REDUCTION_20260908.md)

<!-- BEGIN COMPLETE SOURCE 13 -->

# Two-row virtual-zero clocks and the exact phase-count reduction

2026-09-08. Pure proof; no computation. This is a positive reduction of the physical eligible-label gate to an original-row-one query function and its geometric comparison under the same actual deeper environment. It does not prove divergence of that function. Root full-file audit: PASS. Independent cover-selectors full-file audit: PASS, with the no-wrap and threshold clarifications incorporated below. The growing-query theorem used in Section 7 has separately passed both full audits.

The exact clock and indexing inputs are the accepted notes

- `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_gaussian_clock_genealogy_structural_audit.md`, Sections 2–4;
- `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_finite_layer_zero_triangle_incidence_fibre.md`;
- `/Users/amir.nuriyev/.codex/worktrees/e333/problem/research_round1/pbbs_original_array_shift_cocycles.md`, Sections 1–3;
- `PBBS_SAME_PARTICLE_SHORT_TRACE_MULTIPLICITY_20260907.md` and `PBBS_TOP_ZERO_ALL_SHORT_OVERLAP_REDUCTION_20260908.md`.

## 1. Base incidence, partner cutoff, and the exact fibre

Fix constants `0<c<=C<infinity` before sending `r` to infinity. Write

\[
 H_c=\lfloor c\sqrt r\rfloor,\quad H_C=\lfloor C\sqrt r\rfloor,
 \quad G_C=2H_C+1.
\]

The BASE incidence is that of the original family

\[
 F_{0,c}=\{\mathrm{GOOD},\ T\le H_c,\ Z_{0,0}=0\},
 \qquad \mu_{0,c}=\mathbb E[(T+2)\mathbf1_{F_{0,c}}]=\Theta_c(1).
\]

After weighting a root by `(T+2)1_(F_(0,c))`, sample its edge offset `j` uniformly from `{0,...,T+1}`. Keep this base law throughout; it is not replaced by incidence at cutoff `C`.

Use the accepted depth-two safe base event, so the original triangle satisfies

\[
 Z_{0,0}=Z_{1,0}=Z_{1,-1}=0,
\]

the profile has `h>=4`, and the finite-layer fibre domain holds. Further restrict only the exposed profile to

\[
 \boxed{G_C+1<\min(n_1,n_2),\qquad n_s=2r_s+1.} \tag{1}
\]

For every fixed `c,C`, these restrictions have base-incidence probability tending to one. The triangle and safe-depth assertion is the accepted fixed-`S=2` bound. The extra inequality follows from original-depth profile concentration under actual incidence: `n_1/r -> 1` and `n_2/r -> 2/3`, whereas `G_C=O_C(sqrt r)`. Thus (1) does not introduce an unproved persistence or dynamical condition. The strict margin also excludes a circumference-minus-one C-clock alternative.

Expose

\[
 E_2=(\text{entire profile, all original rows }s\ge2,\ j).
\]

On every feasible environment in this safe event, the accepted fibre says:

- row zero has its coordinate zero fixed to zero and is otherwise a uniform weak composition of `ell_0` into `p_0-1` labelled parts;
- row one has coordinates `0,-1` fixed to zero and is otherwise a uniform weak composition of `ell_1` into `p_1-2` labelled parts;
- these two rows are conditionally independent, where `p_s=n_(s+1)`.

The environment retains its actual conditioned base-incidence distribution. Its feasibility includes the short base clock and sampled-offset test. On the triangle-zero fibre the base clock is the chronological `C_2 C_2 T_2` word from time zero, entirely determined by `E_2`; no new lifetime conditioning on free row-one values is needed.

## 2. Signed original trajectories and virtual-zero intervals

Let `lambda_s(t)` be the omitted physical site in the ORIGINAL fixed-site process of `D_s=partial^s D`, before the update at integer time `t`. Negative times use the inverse finite permutation on the same original labelled orbit. All levels use this same signed physical time, and `lambda_s(0)=0`.

The exposed rows determine the complete original `D_2` and its signed trajectory `lambda_2`. They do not determine `lambda_1`; the algorithm below will not request it.

At a physical phase whose selected site is `i`, C means the first later selection of site `i-1`, and T means the first later selection of the same site `i`. Their physical durations are positive even and odd integers respectively. Define the virtual-zero endpoint at a birth phase `t_d=2d` as the endpoint of the chronological `C_1 T_1` word beginning at `t_d`. Equivalently, it is the second strictly later selection of `lambda_1(t_d)-1`. Denote its physical gap by `g_0(d)` and put

\[
 T_0(d)=\frac{g_0(d)-1}{2},\qquad
 R_0(d)=d+T_0(d)+1,\qquad
 J_d^*=[d,R_0(d)]\cap\mathbb Z. \tag{2}
\]

Both endpoints of this edge interval are included. These virtual objects are defined from the original `D_1` trajectory, independently of every top-row gap. They are not asserted to be the actual lifetimes of births whose top-row gaps are positive.

The height floor holds without an additional test:

\[
 \boxed{T_0(d)\ge h.} \tag{3}
\]

Indeed `C_1>=2`, while its following reached `T_1` has physical duration at least `2(h-1)+1`: every reached level-one root has height `h-1`. Thus `g_0(d)>=2h+1`. The parity of C and T makes `g_0(d)` odd.

If the original top gap at label `i=lambda_1(2d)` is zero and `T_0(d)<=H_C<r`, the original predecessor-count theorem identifies the virtual endpoint with the actual top-level return. The full spatial-lap alternative needs at least `n_0=2r+1` physical time and cannot occur within `G_C`. Conversely every top-zero actual short birth has this virtual endpoint. This is the exact connection with the partner family `F_(0,C)`.

## 3. Exact two-query replay theorem

For every signed integer `d`, put

\[
 b_d=\lambda_2(2d)\pmod{p_1},\qquad
 u_d=Z_{1,b_d},\qquad v_d=Z_{1,b_d-1}. \tag{4}
\]

All indices are original persistent labels. The two-query leaf word is

\[
 \boxed{(C_2T_2^{2u_d})(C_2T_2^{2v_d+1}).} \tag{5}
\]

Replay it chronologically on the ONE exposed `D_2` orbit starting at physical time `2d`. An exponent zero means that the corresponding T block is empty. No clock is restarted at a freshly rooted or independently sampled state.

### Theorem 1

Under (1), replay (5) exactly decides whether `T_0(d)<=H_C`, and gives the exact virtual endpoint whenever this holds. Replay may stop and reject as soon as its cumulative physical duration exceeds `G_C`. It need not identify an unrestricted long virtual endpoint through an invalid no-wrap expansion.

**Proof of the two labels.** The original selection cocycle for row one is `kappa_1(t)=lambda_2(t)`. Therefore the initial C1 query at time `2d` is exactly `Z_(1,b_d)`. The one-level clock partition gives `C_1 -> C_2 T_2^(2u_d)`. Its first child C changes the selected level-two site from `b_d` to `b_d-1`; every following child T returns to that same selected site. Hence completion of this C1 node leaves selected level-two label `b_d-1`. The next parent T1 consequently queries `Z_(1,b_d-1)` and expands as the second block in (5). This reasoning remains valid when `u_d>0` and at negative starting times. It needs neither an absolute level-one site nor a cumulative original gap sum.

**Forward cutoff implication.** If the actual virtual C1T1 word has duration at most `G_C`, its whole horizon satisfies the source no-wrap hypothesis at both levels. The two one-level partitions are therefore exact, and (5), with these original labels, has the same endpoint.

**Reverse cutoff implication.** If candidate (5) finishes within `G_C`, group its first block into C1 and its second into T1. Every child interval lies inside this same short horizon. Condition (1) excludes the wrap alternatives in each reverse grouping, so both are actual parent clocks. Their concatenation is exactly the virtual C1T1 word. Thus a candidate exceeding the cutoff cannot conceal a virtual endpoint within it: the forward implication would force equality. These arguments use time differences only and apply across physical time zero as well. `square`

## 4. Commutation and a count interval depending only on adjacent sums

The endpoint maps C and T commute exactly. To see this, begin at any selected site `i`. Strict alternation of selections of `i` and `i-1` gives the order

\[
 t<\text{first later }(i-1)<\text{first later }i
   <\text{second later }(i-1).
\]

Both CT and TC end at that second later predecessor selection, in the same physical state. Repeated adjacent swaps therefore preserve the endpoint of any finite C/T word. This endpoint statement does not declare the intermediate clock roots independent.

Consequently (5) has the same endpoint as

\[
 \boxed{C_2^2T_2^{2w_d+1},\qquad
 w_d=Z_{1,b_d}+Z_{1,b_d-1}.} \tag{6}
\]

Let `a_d` be the first later selection time of `b_d-1` in `lambda_2`, starting after `2d`; this is the first C2 endpoint. The endpoint of (6) is the `(2w_d+2)`-nd selection of `b_d-2` **strictly after `a_d`**. Visits of that label before `a_d` are not counted.

For an integer `l>=0`, define the exposed count

\[
 B_d(l)=\#\{t\in\mathbb Z:a_d<t\le2d+2l+1,
                    \ \lambda_2(t)=b_d-2\pmod{p_1}\}, \tag{7}
\]

with value zero when the upper endpoint is at or before `a_d`. Both the strict lower endpoint and inclusive upper endpoint in (7) are part of the definition.

For candidate phases

\[
 \mathcal D_C=\{j-H_C-1,\ldots,j\},\qquad
 L_d=\max(h,j-d-1,1), \tag{8}
\]

set the following integer interval to be empty if `L_d>H_C` or its endpoints are reversed:

\[
 \boxed{I_d^{(2)}=
 \left[\left\lfloor\frac{B_d(L_d-1)}2\right\rfloor,
       \left\lfloor\frac{B_d(H_C)}2\right\rfloor-1\right]
       \cap\mathbb Z.} \tag{9}
\]

Every item in (8)–(9), including `b_d`, `a_d`, and the count function, is measurable from `E_2`. Theorem 1, parity, and the order-statistic description above give the exact test

\[
 \boxed{\{T_0(d)\le H_C,\ j\in J_d^*\}
       \quad\Longleftrightarrow\quad w_d\in I_d^{(2)}.} \tag{10}
\]

To check the endpoints explicitly, the upper cutoff requires
`B_d(H_C)>=2w_d+2`. The lower lifetime requirement `T_0(d)>=L_d` requires that the designated odd endpoint occur strictly after `2d+2L_d-1`, equivalently `B_d(L_d-1)<=2w_d+1`. These two inequalities are precisely (9). The overlap requirement is `T_0(d)>=j-d-1`; (3) supplies the height floor already included in `L_d`. Thus (10) retains the deletion boundary `j=R_0(d)` and insertion boundary `j=d`.

A related general identity is useful only when the actual one-level no-wrap clock partition is valid throughout the parent word: a chronological parent word with `a` C nodes and `b` T nodes queries its first `a+b` original incoming coordinates and expands, after commuting child endpoint maps, to `C^(a+b) T^(b+2 sum z)`. Its chronological starting indices still have to be justified in the actual phase. Endpoint commutation alone does not authorize expansion of a long parent word, or remove the indexing or conditioning obligation.

## 5. Deterministic query union and the actual conditional law

Define the exposed index union

\[
 \boxed{Q_C(E_2)=\bigcup_{d\in\mathcal D_C}\{b_d,b_d-1\}
               \subseteq\mathbb Z_{p_1}.} \tag{11}
\]

It is chosen before reading any free row-one value, and

\[
 |Q_C(E_2)|\le2(H_C+2). \tag{12}
\]

Query each free coordinate of this union once, retain its value, and reuse it in every test (10). Coordinates `0,-1` return their forced zeros. Repeated phases and coincident labels create shared variables, not independent replicas. No row-zero coordinate is queried.

The virtual eligible phase count is therefore the exact function

\[
 \boxed{N_{c\to C}=
 \sum_{d\in\mathcal D_C}\mathbf1_{
 Z_{1,b_d}+Z_{1,b_d-1}\in I_d^{(2)}}.} \tag{13}
\]

The subscript records its BASE incidence law at `c` and its partner cutoff `C`. It is measurable from `E_2` and at most `2(H_C+2)=O_C(sqrt r)` original row-one queries.

Conditional on every feasible `E_2` on the safe event, these queries read the exact uniform composition of `ell_1` into `p_1-2` free coordinates described in Section 1. The environment is not reweighted or replaced. At `d=0`, `b_0=0` and the two forced row-one values are zero; feasibility of `E_2` makes the base phase eligible. Since `C>=c`, increasing the partner cutoff retains that eligibility.

## 6. Exact comparison with distinct eligible top labels

Let

\[
 k_{c\to C}=\#\{i\in\mathbb Z_{p_0}\setminus\{0\}:
 \exists d\in\mathcal D_C,\ \lambda_1(2d)=i,
 \ T_0(d)\le H_C,\ j\in J_d^*\}. \tag{14}
\]

This is the original distinct-label gate, with the larger partner cutoff allowed. The algorithm does not need to compute the individual labels in (14).

### Theorem 2

Pointwise on the safe base-incidence event,

\[
 \boxed{k_{c\to C}+1\le N_{c\to C}\le k_{c\to C}+2.} \tag{15}
\]

In particular, divergence in base-incidence probability of these two quantities is equivalent, for each fixed `c,C`. At `C=c`, `k_(c->c)` is exactly `k_0` in the top-zero overlap reduction.

**Proof, including interval boundaries.** Fix an original level-one physical label `i`. Enumerate its even selection times bi-infinitely as

\[
 \ldots<2d_{-1}<2d_0<2d_1<\ldots.
\]

Such an enumeration exists by the full-label property and finite invertibility. Consecutive selections of the same label are separated by odd physical times, so its even selections are every second selection. Starting at `2d_k`, strict alternation puts the second later selection of `i-1` after the intervening odd-time selection of `i` and strictly before its next even selection `2d_(k+1)`. The first later predecessor selection has even relative time; the next same-predecessor gap is odd. Thus this second predecessor selection is at an odd absolute time `t_k^*`, and its virtual edge endpoint satisfies

\[
 \boxed{d_k+1\le r_k^*:=(t_k^*+1)/2\le d_{k+1}.} \tag{16}
\]

This is a direct fact about the virtual-zero intervals `[d_k,r_k^*]`. It does not require pretending to set all actual top-row gaps to zero, or altering any composition.

If `d_m<j<d_(m+1)`, only interval `m` can cover `j`: all preceding intervals end no later than `d_m`, and all following ones start no earlier than `d_(m+1)`. If `j=d_m`, only intervals `m-1` and `m` can cover it. The former contributes only when its inclusive right endpoint equals `j`; the latter includes its left endpoint `j`. This is the only possible doubling.

The equality `j=d_m` for a label can occur only for the unique currently selected label `i=lambda_1(2j)`. Hence every other label contributes at most one eligible phase, and the current label contributes at most two. Restricting to phases in `mathcal D_C` and lifetimes at most `H_C` only removes intervals and preserves the bound.

The eligible label set includes the original base label zero, because the sampled base interval covers `j` and its lifetime is at most `H_c<=H_C`. Thus the number of distinct eligible labels is exactly `k_(c->C)+1`. Each contributes at least one phase, and at most one extra phase is possible globally. This proves (15). Negative birth indices and intervals crossing time zero are covered by the same bi-infinite ordering argument. For large `r`, `H_C+2` is below the physical cycle period, so the candidate window has no duplicate representatives of one physical birth. `square`

More precisely, (15) gives the shifted lower-tail brackets

\[
 \mathbb P(N_{c\to C}\le m+1)
 \le\mathbb P(k_{c\to C}\le m)
 \le\mathbb P(N_{c\to C}\le m+2) \tag{17}
\]

under the safe conditioned base law, for every deterministic threshold `m`, including a threshold depending on `r`. Under the full base-incidence law, an `o(1)` safe-exception error may be added to these brackets. Divergence in probability is therefore equivalent, but arbitrary moving lower-tail thresholds cannot be equated without their additive shifts. The exact function (13) tests the phase count without reconstructing absolute top-label indices. This is a reduction, not a proof that either count diverges.

## 7. Proved growing-query transfer under the same actual environment

The independently audited theorem in `PBBS_GROWING_ADAPTIVE_GAP_QUERY_FRESHNESS_20260908.md`, especially its actual-incidence estimate (8), applies to (11)–(13). The number of free row-one requests is at most `M=2(H_C+2)=O_C(sqrt r)`, and their indices are `E_2`-measurable.

Define the comparison counter by first sampling `E_2` with its SAME actual base-incidence marginal. Conditional on that environment, set `G_0=G_{-1}=0`, assign independent marks to the other distinct indices of `Q_C(E_2)` with

\[
 \mathbb P(G_i=a\mid E_2)=\frac89\left(\frac19\right)^a,
 \qquad a=0,1,2,\ldots, \tag{18}
\]

and cache every repeat of an index. Thus `Geom(1/9)` here denotes the geometric law on the nonnegative integers with ratio `1/9`. Apply the exact same function as in (13):

\[
 \widetilde N_{c\to C}
 =\sum_{d\in\mathcal D_C}
   \mathbf1_{G_{b_d}+G_{b_d-1}\in I_d^{(2)}}. \tag{19}
\]

### Corollary 3

For every fixed `0<c<=C<infinity`, the joint laws under this common environment marginal satisfy

\[
 d_{\mathrm{TV}}\bigl(\mathcal L(E_2,N_{c\to C}),
                         \mathcal L(E_2,\widetilde N_{c\to C})\bigr)
 =o(1). \tag{20}
\]

On the accepted safe event, the mean conditional total variation is
`O_(c,C)(r^(-1/4) sqrt(log r))` plus the profile-tail error. Restoring the safe exceptions adds `o(1)`. This is an averaged conditional estimate, equivalently a joint estimate with the common actual `E_2` marginal; it is not claimed uniformly over every feasible environment.

**Proof.** Conditional on a safe feasible environment, the actual free marks form a uniform weak composition of `ell_1` into `P_1=p_1-2` labelled parts. Original-depth profile concentration under the actual incidence law gives `P_1` of order `r` and mean-matched geometric ratio

\[
 q_{1,r}=\frac{\ell_1}{\ell_1+P_1}
       =\frac19+O\!\left(\sqrt{\frac{\log r}{r}}\right)
\]

outside a profile event of arbitrarily small polynomial probability. The growing-query theorem compares at most `M` fresh individual requests with cached independent geometric replies. Its mean conditional error is bounded by

\[
 O_{c,C}\!\left(\frac{M+\log r}{r}
           +\sqrt{\frac{M\log r}{r}}\right)
\]

plus that profile error. With `M=O_C(sqrt r)`, this is the stated rate. The index union, the intervals `I_d^(2)`, and the finite function (13) are already determined by the environment and these replies. Data processing therefore proves (20) on the safe event. Assigning the same arbitrary output on its complement and then restoring the original count costs at most the safe-exception probability, which tends to zero. `square`

In particular, under the stated base-incidence laws,

\[
 k_{c\to C}\xrightarrow{\mathbb P}\infty
 \quad\Longleftrightarrow\quad
 N_{c\to C}\xrightarrow{\mathbb P}\infty
 \quad\Longleftrightarrow\quad
 \widetilde N_{c\to C}\xrightarrow{\mathbb P}\infty. \tag{21}
\]

The first equivalence uses (15), with its safe-exception error, and the second uses (20). Formula (20) also compares every event depending on `(E_2,N)` with the same event for `(E_2,tilde N)`, including arbitrary moving count thresholds; the comparison with `k` still requires the shifts in (17).

The actual row-one marks remain a conditional uniform composition. The independent geometric marks define the comparison counter only. They do not reconstruct an entire independent-geometric array as a valid PBBS root, assign an unweighted law to `D_2`, or condition again on an oracle base lifetime. Base eligibility is already preserved by exposed feasibility and the forced zeros.

The remaining gate is abundance of the feasible virtual phases in the actual deeper environment, expressed equivalently by divergence of (19). This note proves the finite-query interface and the equivalences (20)–(21), not that divergence, an occupied-support estimate, a packing improvement, or coefficient one.


<!-- END COMPLETE SOURCE 13 -->


---

<a id="document-14"></a>

## Document 14: PBBS_SAME_PARTICLE_SHORT_TRACE_MULTIPLICITY_20260907.md

Source: `/Users/amir.nuriyev/Documents/problem/scratch/PBBS_SAME_PARTICLE_SHORT_TRACE_MULTIPLICITY_20260907.md`

[Portable document](sources/essential/project/scratch/PBBS_SAME_PARTICLE_SHORT_TRACE_MULTIPLICITY_20260907.md) · [Exact original](originals/project/scratch/PBBS_SAME_PARTICLE_SHORT_TRACE_MULTIPLICITY_20260907.md)

<!-- BEGIN COMPLETE SOURCE 14 -->

# Same-particle multiplicity in short PBBS repair congestion

2026-09-07. Root pure-proof deduction; no computation.
The complete note passes independent root and task08 audits. It uses
the accepted physical clock and original-slot identities, not a new
law at a reached root. The bound is an UPPER multiplicity bound; it
does not assert the overlap lower bound needed for shared repair.

## 1. Conventions and the two clock inputs

Let D have semilength r, n=2r+1, and height at least two. In the
original level-one fixed-site process, lambda_1(t) is the omitted
particle label at every signed integer physical time t. For an original
level-zero particle label i let z=Z_(0,i), its invariant incoming-gap
coordinate. A projected birth at index d occurs at physical time2d
and has original particle label lambda_1(2d).

Retain any collection of births with lifetime T<=H, where H<r is an
integer. The consuming update is included in T. Its full repair trace
has edge indices

    d,d+1,...,d+T+1.

We use two already proved clock facts:

1. Selections of adjacent level-one labels i and i-1 strictly alternate.
   Consecutive selections of a fixed label have odd physical-time gaps.
   At a selection of i, the first later selection of i-1 is at an
   even relative time.
2. If lambda_1(2d)=i and T<=H<r, the original return at physical time
   2d+2T+1 is EXACTLY the (2z+2)-nd later selection of i-1.

These facts are in Section3 of task05's
pbbs_gaussian_clock_genealogy_structural_audit.md and Sections1-2 of
task08's pbbs_original_incidence_window_kernel.md. The second fact
uses the strict window2H+1<n, so a full spatial lap cannot win the
first-return race. No such assertion is made for a long birth.

## 2. The exact virtual endpoint bracket

Enumerate all EVEN physical selection times of label i as

    ...,2d_(-1),2d_0,2d_1,...,

with the d_k strictly increasing integers. The full-label property
and finite invertibility provide this bi-infinite enumeration.
Because consecutive selections of i are separated by odd gaps,
these even times are every second selection of i.

Starting from2d_k, let t_k^* be the physical time of the (2z+2)-nd
subsequent selection of i-1, whether or not the corresponding original
birth is short. Strict alternation of i and i-1 implies that t_k^*
falls between the (2z+1)-st and (2z+2)-nd subsequent selections of i.
In particular,

    2d_(k+z) < t_k^* < 2d_(k+z+1).

The first subsequent predecessor selection has even relative time;
its successive same-label gaps are odd. Therefore its even-numbered
selection t_k^* has odd physical time. The integer virtual right
endpoint r_k^*=(t_k^*+1)/2 consequently satisfies

    d_(k+z)+1 <= r_k^* <= d_(k+z+1).                  (1)

For a retained short birth, clock fact2 gives

    r_k^*=d_k+T+1,

its ACTUAL final repair-edge index. Long births are used only to
define the virtual endpoint bracket; their actual return need not
equal t_k^*.

## 3. Congestion contributed by one original particle

At a fixed edge index j, let k_i(z) count retained short births of
original label i whose full trace contains that edge. Then

    k_i(z)<=z+2.                                      (2)

If j is not itself one of the birth indices d_k, the stronger bound is

    k_i(z)<=z+1.                                      (3)

Proof. By (1), any contributing retained interval is contained in
[d_k,d_(k+z+1)]. If j=d_m, containment requires

    m-z-1<=k<=m,

giving at most z+2 indices. If d_m<j<d_(m+1), it requires

    m-z<=k<=m,

giving at most z+1. Lifetime floors or any other removal of births
can only reduce the count. No assumption on disjoint original labels
or independent lifetime tests is used. Square.

This is a bound on unwrapped PHYSICAL births. Repeated rooted shapes
are not identified, and signed-time histories are included. When
H<r, the finite window of births that can cover a given edge has
lengthH+2 below the physical cycle period, so it contains no duplicate
representatives of one physical birth.

## 4. A logarithmic uniform cap outside negligible occupied support

The accepted root profile-concentration theorem permits discarding
bad original profiles at short-support cost at most2W/(n+1)^9.
On every remaining profile, p/n tends uniformly to1/2 and ell/p
to1/3. Conditional on the complete profile, the p original level-zero
slots form a uniform weak composition of ell.

For any slot and integer m>=0, stars-and-bars gives

    Pr(Z_i>=m | profile)
      =binom(ell-m+p-1,p-1)/binom(ell+p-1,p-1)
      <=[ell/(ell+p-1)]^m,                            (4)

with probability zero if m>ell. On good profiles the bracket in
(4) is at most1/2 for all sufficiently large n. Let

    m_n=ceil(14 log_2(n+1)).

Since p<=n, a union bound gives

    Pr(max_i Z_i>=m_n AND profile good)
          <=n/(n+1)^14.

The short-trace support of those exceptional roots costs at most

    (H+2)W n/(n+1)^14 <= W n/[2(n+1)^13].

Together with the earlier bad-profile contribution this is o(W).
Outside it, (2) bounds EVERY original-label contribution by m_n+1.

The maximum of the persistent original slot values is invariant under
the dynamics (canonical rerooting only permutes those values).
This exceptional set therefore also consists of whole physical
components; discarding it leaves congestion unchanged on all retained
good components.

## 5. Scope

The result controls repeated-label multiplicity in the exact original
incidence kernel. It does not show that many DISTINCT labels actually
have an admissible lifetime window at the sampled edge. In particular
(2) is an UPPER bound, not the lower-overlap estimate needed to prove
that the total occupied short-repair support is o(W).

The maximum-slot restriction is used to discard components at directly
bounded cost. It is not silently added to a conditional composition
law or used as a claim that the remaining slots are independent.


<!-- END COMPLETE SOURCE 14 -->


---

<a id="document-15"></a>

## Document 15: PBBS_TRUE_GAUSSIAN_RAW_CENSUS_OBSTRUCTION_20260907.md

Source: `/Users/amir.nuriyev/Documents/problem/scratch/PBBS_TRUE_GAUSSIAN_RAW_CENSUS_OBSTRUCTION_20260907.md`

[Portable document](sources/essential/project/scratch/PBBS_TRUE_GAUSSIAN_RAW_CENSUS_OBSTRUCTION_20260907.md) · [Exact original](originals/project/scratch/PBBS_TRUE_GAUSSIAN_RAW_CENSUS_OBSTRUCTION_20260907.md)

<!-- BEGIN COMPLETE SOURCE 15 -->

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


<!-- END COMPLETE SOURCE 15 -->


---

<a id="document-16"></a>

## Document 16: PBBS_CROSS_CUTOFF_OCCUPIED_SUPPORT_REDUCTION_20260908.md

Source: `/Users/amir.nuriyev/Documents/problem/scratch/PBBS_CROSS_CUTOFF_OCCUPIED_SUPPORT_REDUCTION_20260908.md`

[Portable document](sources/essential/project/scratch/PBBS_CROSS_CUTOFF_OCCUPIED_SUPPORT_REDUCTION_20260908.md) · [Exact original](originals/project/scratch/PBBS_CROSS_CUTOFF_OCCUPIED_SUPPORT_REDUCTION_20260908.md)

<!-- BEGIN COMPLETE SOURCE 16 -->

# A larger fixed partner cutoff suffices for occupied-support decay

2026-09-08. Pure proof; no computation. Independent cover-selectors audit
passed. Root also read the full note and passed the incidence, Cauchy--Schwarz,
conditional-fibre, and scope checks.
This weakens a sufficient dynamical gate; it does not prove abundance.

Fix constants 0<c<=C<infinity and set H_c=floor(c sqrt(r)),
H_C=floor(C sqrt(r)). Use the same profile-measurable GOOD condition
and define the nested physical birth families

    F_c={GOOD, Z_(0,0)=0, T<=H_c},
    F_C={GOOD, Z_(0,0)=0, T<=H_C}.

Write U_c for the occupied edge union of F_c, K_c and K_C for the two
actual physical congestions, and mu_c,mu_C for their normalized raw
incidence masses. The accepted top-zero reduction gives mu_c=Theta_c(1)
and mu_C=O_C(1). All expectations below sample an actual F_c incidence;
partner congestion is always K_C.

## 1. Two deterministic inequalities

For every integer M>=1, split U_c according to K_C<M or K_C>=M. Every
edge in the first set has at least one base incidence. The second set
contains at most the total partner raw incidence divided by M. Hence

    |U_c|/W <= mu_c Pr_inc,c(K_C<M) + mu_C/M.        (1)

There is also the reciprocal bound

    (|U_c|/W)^2 <= mu_C mu_c E_inc,c[1/K_C].        (2)

Indeed, nesting ensures K_C>=K_c>=1 on U_c. Exact incidence counting is

    mu_c E_inc,c[1/K_C]
        = (1/W) sum_(e in U_c) K_c(e)/K_C(e)
        >= (1/W) sum_(e in U_c) 1/K_C(e).

Cauchy--Schwarz and sum_e K_C(e)=mu_C W now give (2). In particular
we do NOT replace the base incidence identity by |U_c|/W equal to
mu_c E_inc,c[1/K_C]; that equality would generally be false.

## 2. The exact top-row fibre still applies

Expose the base environment E=(full profile, all rows s>=1, offset j)
under actual F_c incidence. Its conditional top row is the same exact
uniform composition as in the accepted top-zero reduction: Z_(0,0)=0
and the other N=p-1 entries uniformly compose ell. The environment
keeps its base-c incidence law.

For partner shifts d in {j-H_C-1,...,j}, use that SAME original signed
trajectory and put

    a_d=lambda_1(2d),
    L_d=max(h,j-d-1,1),
    I_d^C=[floor(N_d(L_d-1)/2), floor(N_d(H_C)/2)-1],

with the accepted empty-interval conventions. Let k_(c->C)(E) count
distinct nonzero labels i for which some such d has a_d=i and 0 in I_d^C.
No shifted triangle is imposed.

Let Y be the number of these labels whose actual top gap is zero.
The base birth belongs to F_C. The same-particle virtual endpoint
argument and the exact F_C membership test therefore give

    1+Y <= K_C <= 2+Y.

Conditional on E, Y has precisely the hypergeometric zero-count law of
the accepted top-zero note, with k=k_(c->C). Consequently, on GOOD,

    E_inc,c[1/K_C | E] <= 2/[k_(c->C)(E)+1]          (3)

for sufficiently large r. Enlarging the partner window has not changed
the conditional fibre or its parameter ell/N.

Combining (2)-(3) gives

    |U_c|/W <= sqrt(2 mu_C mu_c
                      E_inc,c[1/(k_(c->C)+1)]).     (4)

## 3. The weaker sufficient gate and its scope

It is sufficient to prove the following statement:

    For every fixed c>0 there exists a finite C(c)>=c such that
    k_(c->C(c)) tends to infinity in actual base-c incidence probability.

Equations (1) or (4), with mu_C bounded for each fixed C, then imply
|U_c|=o(W). The accepted discarded-top-gap estimate transfers this to
ALL births with T<=H_c. The accepted occupied-support-to-packing theorem
then gives their packing o(W/sqrt(r)).

The larger cutoff must remain fixed while r tends to infinity. No
uniform bound in a growing C is asserted. This gate does not require
partner lifetime at most the base cutoff, but it still requires actual
physical lifetime and sampled-edge overlap tests. Its truth, a complete
repair compiler, and the coefficient-one conclusion remain unproved.


<!-- END COMPLETE SOURCE 16 -->


---

<a id="document-17"></a>

## Document 17: PBBS_OCCUPIED_SUPPORT_TO_PACKING_20260908.md

Source: `/Users/amir.nuriyev/Documents/problem/scratch/PBBS_OCCUPIED_SUPPORT_TO_PACKING_20260908.md`

[Portable document](sources/essential/project/scratch/PBBS_OCCUPIED_SUPPORT_TO_PACKING_20260908.md) · [Exact original](originals/project/scratch/PBBS_OCCUPIED_SUPPORT_TO_PACKING_20260908.md)

<!-- BEGIN COMPLETE SOURCE 17 -->

# Vanishing occupied support now suffices for Gaussian-short packing

2026-09-08. Root pure-proof synthesis. Complete root-helper and task05
full-file audits PASS; the quantitative modulus below also passes
independent audits. No computation. The small-height estimate is the new input
that removes the earlier quantitative logarithmic rate requirement.

## 1. Uniform small-height tightness at the short-birth scale

Let r>=1, R=sqrt r, W=(2r+1)Cat_r, and H=floor(cR), with c>0 fixed.
Use the profile-measurable a>=1, A=a+sqrt(log(a+2))<=3a, and
L=floor(kappa_c R/A) of the accepted theorem
PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md. Its proved inputs are

    Pr(a>1+x)<=C exp(-b x^2),
    Pr(T<=H | full profile)<=C_c A exp(C_c A)/R.       (1)

The second estimate holds on EVERY profile, including L<2.
There is also the following global height bound:

    R/(h+1)<=A/kappa_c.                              (2)

If L>=2, the accepted proof gives h>2L and
2L>=kappa_c R/A, proving (2). If L<2, then A>kappa_c R/2;
since every nonempty Dyck root has h>=1, (2) follows again.

Fix0<epsilon<=1 and take r large enough that R>=1/epsilon. Then
h<epsilon R implies h+1<=2epsilon R. By (2) and A<=3a,

    a>=kappa_c/(6epsilon).

The height event and a are measurable from the ORIGINAL full profile.
Multiplying the global conditional bound in (1) by this indicator,
then using Cauchy-Schwarz and the uniform subGaussian tail, gives

    Pr(T<=H, h<epsilon R)
       <=C_c exp(-b_c/epsilon^2)/R.                   (3)

Here C_c,b_c>0 are independent of r and epsilon. Explicitly,
E[A exp(C_c A)1_{a>=t}] is at most its uniformly bounded L2 norm
times Pr(a>=t)^(1/2), hence at most C_c exp(-b' t^2), after
absorbing the shift by one into the constant. Substitute
t=kappa_c/(6epsilon). This is at the SHORT-BIRTH scale1/R;
a bound only on unconditional low height would not suffice.

## 2. A deterministic packing split

Let F_r be ANY retained family of physical repair traces with T<=H.
It need not be invariant under the dynamics or coordinate rotations.
Let U_F be its occupied-edge union and P(F) its maximum size of an
edge-disjoint subfamily. Every trace has T+2 edges and T>=h.
The accepted full physical factor has W edges in total and each
physical period has length at least2r+1. A trace has consecutive edge
indices d,...,d+T+1. For fixed c and sufficiently large r,
T+2<=H+2<2r+1, so all its T+2 edges are distinct.

Split any packing into births with h<epsilon R and the others.
The first part has at most the number of ALL physical short births
of that height, at most W times (3). Every trace in the second part
has at least epsilon R distinct edges, and these edges are disjoint
and contained in U_F. Therefore

    R P(F)/W
       <=C_c exp(-b_c/epsilon^2)+|U_F|/(epsilon W).    (4)

This bound is uniform over every retained F_r. If |U_F|=o(W), first
let r tend to infinity at fixed epsilon, then let epsilon decrease
to zero. Equation (4) proves

    |U_F|=o(W)  ==>  P(F)=o(W/sqrt r).                (5)

No o(1/sqrt(log r)) rate on occupied support is required. The earlier
budget-floor division remains valid but is no longer needed for this
implication. Conversely, no statement that occupied support actually
vanishes is proved by (4) or (5).

### 2.1. A quantitative modulus

Write u=|U_F|/W, so0<=u<=1. There is a constant depending only on c
such that

    P(F)<=C_c (W/R) u sqrt(log(e/u)),                 (5a)

with value zero at u=0. For0<u<=1 put b=min(b_c,1/2) and
epsilon=sqrt(b/[2log(e/u)]). If epsilon>=1/R and r is sufficiently
large, (4) applies uniformly: its exponential term is at most
C_c(u/e)^2 and its other term is sqrt(2/b)u sqrt(log(e/u)).
The first is absorbed into the second. If epsilon<1/R, use the
elementary P(F)<=|U_F| instead, obtaining

    R P(F)/W<=Ru<u/epsilon=sqrt(2/b)u sqrt(log(e/u)).

If u=0 the packing is empty. Finitely many smaller r are absorbed
into C_c using P(F)<=|U_F| and sqrt(log(e/u))>=1. Thus (5a) holds
uniformly over retained families, not only invariant ones.

## 3. Consequence for the clean-triangle overlap problem

Task08's fully audited
pbbs_clean_triangle_hypergeometric_reciprocal.md defines a clean
retained family F_clean of residual short births. Its omitted sector
already has packing o(W/sqrt r). The accepted low-budget theorem
also handles all B<=J_r births, independently of the lifetime cutoff.

For the clean family let mu_clean=E[(T+2)1_clean]. Its actual incidence
environment E determines the number k(E) of eligible DISTINCT nonzero
original labels, including the shifted deeper-triangle gate and BOTH
lifetime/edge-overlap threshold tests. The exact top-row composition law
and same-particle multiplicity give

    (mu_clean/2) E_inc,clean[1/(k+1)]
       <=|U_clean|/W
       <=2mu_clean E_inc,clean[1/(k+1)].              (6)

If mu_clean=0, interpret all these quantities as zero. Its upper bound
is at most the now proved total short-incidence bound C_c.
Combining (5)-(6), a sufficient remaining condition is simply

    mu_clean E_inc,clean[1/(k+1)] ->0.                (K_c)

There is no prescribed logarithmic convergence rate in (K_c).
Equivalently, using bounded mu_clean, it is enough and necessary that

    mu_clean Pr_inc,clean(k<=M) ->0
                       for EVERY fixed integer M>=0. (7)

Necessity follows because 1/(k+1)>=1/(M+1) on k<=M.
For sufficiency split at M; the reciprocal mass is at most the
left side of (7) plus C_c/(M+1), then take limits in that order.
If the incidence law is defined and k tends to infinity in its
probability, this is sufficient, but a lower bound on mu_clean is
not needed for the raw formulation (7).

Condition (K_c) or (7) is still UNPROVED. If supplied for every fixed c,
(5) would give clean packing o(W/sqrt r); add the already handled
removed and low-budget sectors to get the whole fixed-Gaussian packing
step. The earlier conditional slow-diagonal argument can then be used
with its exact scope. No complete repair compiler, all-target word,
coefficient-one theorem, or exact equality is being claimed here.


<!-- END COMPLETE SOURCE 17 -->


---

<a id="document-18"></a>

## Document 18: PBBS_ABUNDANCE_TO_COEFFICIENT_ONE_VERIFIED_COMPILER_CHAIN_20260908.md

Source: `/Users/amir.nuriyev/Documents/problem/scratch/PBBS_ABUNDANCE_TO_COEFFICIENT_ONE_VERIFIED_COMPILER_CHAIN_20260908.md`

[Portable document](sources/essential/project/scratch/PBBS_ABUNDANCE_TO_COEFFICIENT_ONE_VERIFIED_COMPILER_CHAIN_20260908.md) · [Exact original](originals/project/scratch/PBBS_ABUNDANCE_TO_COEFFICIENT_ONE_VERIFIED_COMPILER_CHAIN_20260908.md)

<!-- BEGIN COMPLETE SOURCE 18 -->

# Exposed feasibility abundance suffices for coefficient one

2026-09-08. Cover-selectors independent goal-chain audit. Pure proof;
no computation. The deterministic compiler, its all-target support,
the physical packing interface, exact tail boundaries, and diagonal
quantifiers have been checked against the sources listed below.
Root integration audit passed, including the residence cutoff, exterior
tail boundary, slow diagonal, and even-dimensional lift. The abundance
hypothesis remains open.

## 1. Exact sufficient hypothesis and conclusion

Put R=sqrt(r), W_r=binom(2r+1,r)=(2r+1)Cat_r. For fixed c>0,
let G_c be ALL physical births with lifetime T<=floor(cR). A trace
has T+2 consecutive projected transition edges. Let P_c(r) be the
largest number of edge-disjoint traces in G_c.

The following implication is complete:

    For every fixed c>0, P_c(r)=o_c(W_r/R)
      ==> nu(k)=(1+o(1)) binom(k,floor(k/2)).          (1)

In particular, the sufficient exposed-environment hypothesis is:

    For every fixed c>0, there is a FIXED finite C(c)>=c
    such that J_(c->C(c))(E_2) tends to infinity in probability
    under the ACTUAL base-c incidence-environment law.             (2)

Here J is exactly the feasible-phase count in
PBBS_EXPOSED_PHASE_FEASIBILITY_RECIPROCAL_REDUCTION_20260908.md,
including the physical lifetime and sampled-edge overlap thresholds.
It is not a count of arbitrary recurrent labels or unweighted Dyck roots.
The special choice C(c)=c suffices. Only positive integer c is needed
for the final diagonal.

The current J-reduction and (1) leave no additional all-target,
simultaneous-depth, owner, frame, tail-interface, or parity compatibility
theorem to prove. They do NOT prove (2).

## 2. From J to the full physical packing hypothesis

For fixed c<=C, retain F_c={GOOD,Z_(0,0)=0,T<=floor(cR)} and its
occupied union U_c. Write K_C for the actual partner congestion from F_C,
and mu_c,mu_C for normalized raw incidence masses. The accepted results give

    mu_c=Theta_c(1),   mu_C=O_C(1),
    (|U_c|/W_r)^2 <= mu_C mu_c E_inc,c[1/K_C].       (3)

Under the same actual E_2 marginal, J-divergence is equivalent to
divergence of the virtual-phase count N and the eligible DISTINCT
original-label count k. This follows from the exact finite composition
mean/variance bound at every fixed positive height truncation, followed
by removal of the small-height sector. The limit order is r->infinity
first, then the height cutoff epsilon->0. No fresh law for E_2 is used.
The top-row fibre gives E[1/K_C|profile,rows>=1,j]<=2/(k+1).
Thus (2) implies that the expectation in (3) tends to zero.

Discarded top-gap/BAD traces have normalized raw incidence O_c(1/r),
so their occupied union has that same upper bound. Consequently

    |U_(G_c)|/W_r = o_c(1).                          (4)

For ANY retained short family F, the accepted small-height theorem and
the deterministic edge-capacity split give, for fixed 0<epsilon<=1,

    R P(F)/W_r <= C_c exp(-b_c/epsilon^2)
                    + |U_F|/(epsilon W_r).          (5)

Indeed low-height packed traces are bounded by their number of births,
whose normalized count is at most C_c exp(-b_c/epsilon^2)/R; every other
trace has at least epsilon R distinct edges. Physical cycle lengths
are at least 2r+1, so the short traces do not wrap. Apply (5) to ALL G_c,
send r to infinity and then epsilon to zero, to obtain (1)'s hypothesis.
There is no quantitative logarithmic convergence rate to establish.

This is a full physical-factor statement. No quotient-to-deck estimate,
separate winding case, clean-triangle partner condition, or low-budget
recombination is needed for this version of the chain.

## 3. All targets supplied by the unmodified PBBS owner cycles

Let A_i be the oriented rank-r PBBS states and X_i=[2r+1]\A_i.
The X_i, traversed by step two, are rank-(r+1) Johnson owner cycles;
their lengths sum to W_r and their number is at most Cat_r.

The global-maximum unmatched-mark corridor theorem, Section 21.2 of
PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md, says that for every
q>=0 and every rank-(r-q) target S, some oriented q-edge step-two
PBBS path satisfies S=intersection_(t=0)^q A_(i+2t). The q=0 case is
the complete PBBS vertex factor. This is support for EVERY target;
no lower multiplicity estimate beyond one is needed.

The lower/upper conversion for the actual X owner cycles is exact:

    X_i intersect X_(i+2) = A_(i+1),
    intersection_(t=0)^q X_(i+2t)
       = intersection_(t=0)^(q-1) A_(i+2t+1)  (q>=1),
    union_(t=0)^q X_(i+2t)
       = complement(intersection_(t=0)^q A_(i+2t)).   (6)

The first identity follows because A_(i+1) is disjoint from both
adjacent PBBS states and has their complement-intersection's rank r.
The others follow by associativity and complementation.
Therefore intended windows of at most H+1 owners include every target
of every rank in

    [r+1-H, r+1+H].                                 (7)

Correct lower windows have their Johnson floor rank. Oversized lower
intersections are unnecessary, so the staircase's floor-correctness
restriction loses no required target. All needed occurrences can be
selected before the cuts; the compiler restores any selected crossing
occurrence, simultaneously over all depths through H.

## 4. Literal main word and exact physical cut ledger

The indexing guard is

    positive residence length = T+1,
    residence trace edge count = T+2,
    nu_H(P_r) = P({T<=H-1}).                         (8)

Assume 2H<=r+1. On an active owner cycle choose a transversal of all
positive residences of length at most H. Circular interval packing gives
at most 2 nu_H cuts on active cycles. Once cut, each internal positive
coordinate run has at least H+1 owners. Endpoint-capped erosion then
uses v+H letters on a path of v owners, retaining every intended
intersection/union whose owner window stays inside that path.

At each cut the extent-point Pareto staircase has 2H-1 letters and
represents every floor-correct crossing lower intersection. Its proof
uses the first-departure injection to exclude a strictly southwest
extent point, and then the east-before-south rectangle-interception
identity. The literal 2H-owner collar represents every crossing upper
union. Thus the exact appended chart length is 4H-1, and including
endpoint erosion the charge is 5H-1 per cut. Charts use ORIGINAL cyclic
owners, so nearby cuts and windows crossing several cuts are harmless.
Every staircase letter has at least r+2-2H>=1 coordinates.

An inactive cycle uses its cyclic erosion word with a 2H collar.
All chosen target witnesses stay inside a path word or a cut chart;
concatenation cannot destroy them. Hence

    L_central(r,H)
       <= W_r + 2H Cat_r + 2(5H-1) nu_H(P_r).       (9)

The W_r term counts every original owner exactly once in the baseline.
The second term covers ALL inactive-cycle collars, and the third covers
ALL active-path initialization plus crossing-target repair. There is no
unrecorded multiplicity, component, or concatenation charge.

Equation (9) is the unconditional complete compiler of Sections 22 and
24. The older sufficient O_c(Cat_r) estimate is stronger than required:
the actual critical gate is nu_H=o_c(Cat_r sqrt(r)), equivalently
o_c(W_r/sqrt(r)). This is precisely Theorem 24.4, not merely the older
Catalan-order Theorem 24.3.

## 5. Exact all-rank exterior and zero interface charge

For s>=0 let

    A_r(a)=binom(r,a)-binom(r,a-1),
    w_r(0)=r,   w_r(a)=r-2a+1 (a>0),
    C_r(t)=0 (t<0),
           binom(r,min(t,floor(r/2))) (t>=0),
    L_r(s)=2 sum_(a=0)^floor(r/2) A_r(a)w_r(a)C_r(s-a).

The factor-blind product-SCD theorem constructs a word of exact length
L_r(s) on 2r coordinates covering both tails |S|<=s and |S|>=2r-s.
Its trimmed one-coordinate lift has length 2L_r(s) and covers every
odd-dimensional rank outside [r-h,r+h+1] when s=r-h-1.

Use h=H-1, NOT h=H, to match (7). The odd tail costs 2L_r(r-H)
and covers ranks <=r-H and >=r+H+1. Together with (7) this covers
every nonempty target; there is overlap at rank r+H+1. In particular
there is no uncharged missing rank r-H.

The uniform proved estimate is

    2L_r(r-H)/W_r
       <= 2(r+1)/(2r+1) C_0 exp(-(H-1)^2/(8r)).      (10)

Each product-SCD witness remains internal to its own chain-pair gadget.
Appending the tail to the central word costs exactly its length and
ZERO extra seam letters. Neither a shared frame nor a common PBBS
endpoint is required. Thus the explicit finite all-target ledger is

    nu(2r+1) <= W_r + 2H Cat_r
                   + 2(5H-1)P_(H-1)(r)
                   + 2L_r(r-H),                    (11)

where P_t means the packing of all births with integer lifetime T<=t.

## 6. Slow diagonal and opposite parity

For each positive integer j set H_j(r)=floor(j sqrt(r))+1 and

    epsilon_j(r)=sqrt(r) P_j(r)/W_r ->0,

where here P_j is the fixed-Gaussian family of Section 1. By (8),
nu_(H_j)(P_r)=P_j(r). Choose strictly increasing finite thresholds M_j
such that for EVERY r>=M_j,

    epsilon_j(r) <= 1/[10j(j+1)],
    2H_j(r)/(2r+1) <= 1/j,
    2H_j(r)<=r+1,   r>=j^6.

This is possible independently for each fixed j. Let j(r)=j on
[M_j,M_(j+1)), and H=H_(j(r))(r). Then j(r)->infinity, H=o(r), and
the two excesses in (9), divided by W_r, are each at most 1/j(r):
the packing coefficient is at most 10(j+1)epsilon_j. The tail in
(10) tends to zero since (H-1)/sqrt(r)=j(r)+O(1/sqrt(r))->infinity.
This proves nu(2r+1)<=W_r(1+o(1)). Fixed-c hypotheses are used only
beyond their individual thresholds; no uniform growing-c theorem is used.

For any complete nonzero word Q_1,...,Q_N on 2r+1 coordinates, the
trimmed lift

    Q_1,...,Q_N, {z}, Q_1 union {z},...,Q_(N-1) union {z}

has 2N letters and covers the complete (2r+2)-cube. Witnesses ending
at Q_N use their old suffix followed by {z}; other witnesses use the
last block. Since binom(2r+2,r+1)=2W_r exactly, the leading coefficient
is unchanged. The antichain lower bound supplies the matching 1-o(1)
lower estimate in both parities.

## 7. Sources and precise remaining boundary

The compiler audit reads Sections 21-27 of
PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md; the full standalone
MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md; the corrected
critical-scale argument in
MATH_ATTACK_L_CORRECTED_CHRONOLOGY_TRACE_GATE_20260725.md; and Sections
1-2 and 11-12 of
MATH_THEOREM_O_PRODUCT_SCD_TAIL_MIXED_CYCLE_INTERFACE_20260726.md.
The later sub-Gaussian/tail caveat in
MATH_AUDIT_PBBS_SUBROOT_BAND_AND_PRODUCT_SCD_QUANTIFIER_20260726.md is
respected: a fixed-j tail is NOT o(W_r); only the slow j->infinity
diagonal makes it negligible.

The current probability interface uses the exact J-reciprocal note,
PBBS_TOP_ZERO_ALL_SHORT_OVERLAP_REDUCTION_20260908.md,
PBBS_CROSS_CUTOFF_OCCUPIED_SUPPORT_REDUCTION_20260908.md, and
PBBS_OCCUPIED_SUPPORT_TO_PACKING_20260908.md in this scratch directory.

There is no remaining compiler compatibility gap conditional on (2).
There remains the substantive, unproved assertion that J diverges under
the ACTUAL incidence-biased depth-two environment at every fixed base
cutoff, or for a fixed larger partner cutoff. This is a sufficient
route to coefficient one, not a necessary condition for arbitrary
literal words and not an unconditional construction.


<!-- END COMPLETE SOURCE 18 -->


---

<a id="document-19"></a>

## Document 19: PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md

Source: `/Users/amir.nuriyev/Documents/problem/PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`

[Portable document](sources/essential/project/PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md) · [Exact original](originals/project/PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md)

<!-- BEGIN COMPLETE SOURCE 19 -->

# PBBS residence is an exact short-return packing problem

Date: 2026-07-25

No computation or web search is used in this note.

## 0. Outcome

Let

\[
N=2r+1,\qquad A={N\choose r},\qquad B=A/N,
\]

and let \(P_r\) be the canonical PBBS odd-graph cycle factor.  Orient the
**complement-projected** step-two Johnson cycles, whose owners have rank
\(r+1\).  Consecutive occurrences of one omitted label at odd gap
\(2s+1\) give one positive coordinate-residence interval of length
\(s+1\) in the projected owner cycle.  Let \(\mathcal I_H\) be the
intervals with \(s+1\le H\).

Write \(\nu_H(P_r)\) for the largest number of members of
\(\mathcal I_H\) which are pairwise disjoint as sets of step-two transition
edges.  Write \(J_H(P_r)\) for the least number of path runs obtained by
cutting the projected cycles so that every remaining path is a genuine
radius-\(H\) rotor run.  Throughout the rotor statements assume
\(H\le (r+1)/2\), which contains the mesoscopic range used below.

The main exact reduction is

\[
\boxed{
   \nu_H(P_r)\le J_H(P_r)
   \le \nu_H(P_r)+c_2(P_r),
}
\tag{0.1}
\]

where \(c_2(P_r)\le B\) is the number of projected step-two cycles.  Thus,
at every scale \(H=o(r)\), a Catalan bound

\[
\nu_H(P_r)=O(A/r)
\tag{0.2}
\]

is equivalent, up to a harmless Catalan term, to the desired physical
PBBS row bound.

There is also an exact inversion of the previously proved PBBS rank-excess
sequence.  If

\[
 E_q(P_r)=\sum_{I\in\mathcal I_\infty}(q-s(I))_+,
\]

then the number of short projected residence intervals is

\[
\boxed{
 |\mathcal I_H|=E_H(P_r)-E_{H-1}(P_r).
}
\tag{0.3}
\]

Consequently

\[
\boxed{
 {E_H-E_{H-1}\over r+2}
 \le J_H
 \le E_H-E_{H-1}+c_2(P_r).
}
\tag{0.4}

This does not prove the Catalan packing bound (0.2).  It identifies the
remaining theorem sharply: one must rule out a super-Catalan packing of
edge-disjoint PBBS returns of temporal length at most \(H\).  Merely
bounding the total number of short returns is stronger than necessary.

The later sections sharpen this status in six directions.

1. Gap three is impossible, so the PBBS depth-two rank excess is actually
   zero pointwise.
2. Peak deletion is an exact PBBS renormalization and proves the sharp
   pointwise bound \(g\ge2\operatorname{ht}(D)+1\).  It yields
   \(\nu_H=o(B)\) for \(H=o(\sqrt{r/\log r})\).
3. The formerly proposed stronger vacancy bound
   \(g\ge2(r-\operatorname{pk}(D))+1\) is explicitly **retracted and
   disproved**: height-three roots of arbitrarily large peak defect have gap
   seven.  All gap-seven roots are nevertheless classified, and their whole
   physical packing is only \(\Theta(N2^r)=o(B)\).
4. In the intended range \(H\log N=o(r)\), (0.2) is equivalent to the
   super-sparse quotient assertion \(\overline\nu_H=O(B/N)\).  This aggregate
   Dyck-quotient clustering theorem remains open and is the authoritative
   residual of the PBBS residence lane.
5. A global-maximum corridor in the combined forward/reverse unmatched-mark
   word proves complete correct PBBS intersection support at **every** depth.
   Thus target support itself is no longer conjectural.
6. A dominance-staircase seam replaces the former quadratic singleton
   repair by an exact \(O(H)\) chart at each cut.  Consequently constant
   one follows from the weaker fixed-window estimate
   \[
      \nu_{\lceil A\sqrt r\rceil}(P_r)=O_A(B)
   \]
   for every fixed \(A\).  The explicit sharp ledger is recorded in
   Section 24.

## 1. Omitted labels and projected residence intervals

Consider one oriented PBBS component

\[
 A_0,A_1,\ldots,A_{L-1}
\]

and let \(\lambda_i\) be the omitted label of the odd-graph edge
\(A_iA_{i+1}\).  The audited recurrence is

\[
 A_{i+2}=A_i-\{\lambda_{i+1}\}+\{\lambda_i\}.
\tag{1.1}
\]

Every label occurs \(\ell=L/N\) times.  The cyclic gap between consecutive
occurrences of the same label is odd and at least three.

The physical owners in the middle-levels transition construction are the
complements

\[
 X_i=[N]\setminus A_i,
\]

and (1.1) becomes

\[
 X_{i+2}=X_i-\{\lambda_i\}+\{\lambda_{i+1}\}.
\tag{1.2}
\]

Suppose consecutive occurrences of a label are at positions \(i\) and
\(i+2s+1\).  At the projected transition indexed by \(i-1\), that label is
inserted as \(\lambda_i\); at the projected transition indexed by
\(i+2s+1\), it is removed as \(\lambda_{i+2s+1}\).  These transition
indices differ by \(2s+2\), or \(s+1\) step-two moves.  Thus its positive
projected residence length is

\[
 \ell=s+1={g+1\over2}.
\tag{1.3}
\]

This one-step shift is important at depth one: gap three gives projected
residence two, not one.  In particular, projected PBBS cycles have no
positive residence-one obstruction.

Denote by

\[
 I_i=\{i-1,i+1,\ldots,i+2s+1\}
\tag{1.4}
\]

the corresponding circular set of step-two transition edges.  It has
\(s+2=\ell+1\) edges: the insertion edge, the internal residence edges,
and the removal edge.  Cutting any member of \(I_i\) prevents that insertion
and removal from lying in one path run.  Reversing a projected cycle merely
uses the gaps in reverse cyclic order and does not change the resulting
packing/transversal statistics.

Let \(\mathcal I_H(C)\) be the intervals (1.4) on one projected cycle with
\(s+1\le H\), and let

\[
 \tau_H(C)=\min\{|D|:D\text{ is a set of transition edges meeting every }
                         I\in\mathcal I_H(C)\}.
\tag{1.5}
\]

The prescribed-cycle rotor theorem gives

\[
 J_H(C)=\max\{1,\tau_H(C)\}.
\tag{1.6}
\]

The one in (1.6) is the cut needed to linearize a compatible cycle.

## 2. Circular interval packing is exact up to one

Let \(\nu_H(C)\) be the maximum cardinality of a pairwise edge-disjoint
subfamily of \(\mathcal I_H(C)\).

### Theorem 2.1 (circular packing--transversal sandwich)

For every projected cycle,

\[
\boxed{
 \nu_H(C)\le J_H(C)\le \nu_H(C)+1.
}
\tag{2.1}

#### Proof

Every cut edge meets at most one member of a pairwise disjoint family, so
\(\tau_H(C)\ge\nu_H(C)\).  Hence (1.6) gives the lower bound in (2.1).

If \(\mathcal I_H(C)\) is empty, one arbitrary cut gives \(J_H(C)=1\), so
the upper bound holds.  Otherwise choose any transition edge \(e\) which
belongs to one short interval.  Use \(e\) as one cut.  All intervals not
hit by \(e\) avoid \(e\); after opening the circle at \(e\), they are
ordinary intervals on a line.  For line intervals, the greedy
right-endpoint algorithm gives a transversal whose size equals the maximum
number of pairwise disjoint intervals.  That packing number is at most
\(\nu_H(C)\).  Thus all short intervals, and the cycle itself, are cut by
at most \(1+\nu_H(C)\) edges.  This proves (2.1).  \(\square\)

Summing (2.1) over all projected cycles proves (0.1).

The PBBS level ledger gives

\[
c_2(P_r)\le B=A/(2r+1).
\tag{2.2}
\]

Therefore, whenever \(H=o(r)\),

\[
 Hc_2(P_r)=o(A).
\tag{2.3}
\]

The cycle-linearization term is not part of the mesoscopic obstruction.

## 3. Exact slope inversion of the PBBS rank excess

Let \(M_s\) be the number of consecutive omitted-label gaps \(2s+1\),
summed over all PBBS components.  The audited gap identity is

\[
 E_q(P_r)=\sum_{s\ge1}(q-s)_+M_s.
\tag{3.1}
\]

### Theorem 3.1 (discrete derivative identities)

For every \(q\ge1\),

\[
\boxed{
 E_q-E_{q-1}=\sum_{s\le q-1}M_s,
}
\tag{3.2}
\]

and

\[
\boxed{
 M_q=E_{q+1}-2E_q+E_{q-1}.
}
\tag{3.3}

In particular (0.3) holds.

#### Proof

For one integer \(s\ge1\),

\[
 (q-s)_+-(q-1-s)_+=\mathbf1_{\{s\le q-1\}}.
\]

Sum this identity against \(M_s\) to obtain (3.2), and difference once
more to obtain (3.3).  \(\square\)

Thus the number of short residence intervals is the *slope*, not the value,
of the PBBS rank-excess potential.

## 4. Exact edge congestion

### Lemma 4.1

Every directed projected step-two transition edge belongs to exactly
\(r+2\) of the full positive-residence intervals \(I_i\), before the cutoff
\(s+1\le H\) is imposed.

#### Proof

Write one projected Johnson transition as

\[
 X\longrightarrow Y=X-\{a\}+\{b\}.
\]

The projected owners have rank \(r+1\).  The positive run of each coordinate
in \(X\cap Y\), of which there are \(r\), contains this edge internally.
The positive run of \(a\) ends at the edge, and the positive run of \(b\)
begins at it.  These are all the possibilities, giving
\(r+2\).  \(\square\)

It follows that one cut edge meets at most \(r+2\) short intervals.  Hence

\[
 { |\mathcal I_H|\over r+2}\le \tau_H(P_r)\le J_H(P_r).
\tag{4.1}
\]

Combining (4.1) with (0.3) gives the lower bound in (0.4).  The trivial
choice of one edge from every short interval gives

\[
 J_H(P_r)\le |\mathcal I_H|+c_2(P_r),
\]

which is the upper bound in (0.4).

There is also a universal, but only constant-order, packing estimate.  If
\(\mathcal P\subseteq\mathcal I_H\) is pairwise disjoint, then

\[
 \sum_{I\in\mathcal P}|I|\le A.
\tag{4.2}
\]

For an interval of projected residence \(\ell=s+1\), its contribution to
\(E_H\) is \(H-s=H+1-\ell\), while \(|I|=\ell+1\).  Therefore

\[
\boxed{
 \nu_H(P_r)\le {A+E_H(P_r)\over H+2}.
}
\tag{4.3}

Equation (4.3) explains why the already known nonnegative gap energy alone
does not give coefficient one: even \(E_H=o(A)\) yields only
\((1+o(1))A/H\) cuts, whose radius-\(H\) initialization still costs order
\(A\), not \(o(A)\).  What is needed is a genuinely subcritical packing
bound.

## 5. Exact residual for the pair-omission PBBS construction

In the pair-omission construction, let

\[
 r=m-1,\qquad A_m={2m-1\choose m-1}.
\]

The first-avoided-pair extraction uses only \(O(\log m)\) nonnegligible
phases.  Its category-boundary and PBBS cycle terms are already

\[
 O(A_m\log^2m/m).
\tag{5.1}

By Theorem 2.1, the remaining residence term may be written with no loss as
the short-return packing number.  A sufficient statement is

\[
\boxed{
 \nu_H(P_{m-1})
 =o\!\left({A_m\over H\log m}\right).
}
\tag{5.2}

For a whole local PBBS factor, (5.2) is also necessary up to the harmless
cycle term: every family of pairwise disjoint short-return arcs requires that
many distinct row cuts.  Category restriction can discard some arcs before
they become physical requirements, so (5.2) is only a clean sufficient
uniform estimate for the global first-avoided extraction, not a necessity for
every more adaptive category assignment.

A Catalan estimate

\[
\boxed{
 \nu_H(P_{m-1})=O(A_m/m)
}
\tag{5.3}

is more than enough throughout

\[
 H=\sqrt m\,\omega(m),\qquad
 \omega(m)\to\infty,\qquad
 \omega(m)=o\!\left({\sqrt m\over\log^2m}\right),
\tag{5.4}

because

\[
 {A_m/m\over A_m/(H\log m)}={H\log m\over m}=o(1).
\]

At \(H=1\), the projected interval family is empty.  In fact the exact
Dyck-quotient calculation below shows that PBBS has no gap-three return, so

\[
 |\mathcal I_2|=E_2(P_{m-1})=0.
\]

Thus (5.3) is trivial at \(H=2\).  No theorem presently extends (5.3) to
the growing window in (5.4).

## 6. The remaining positive theorem

The PBBS residence lane is therefore reduced exactly to the following
statement.

> **PBBS Catalan short-return packing theorem.**  For the canonical PBBS
> factor on \(KG(2m-1,m-1)\), every family of pairwise edge-disjoint
> omitted-label return arcs with odd gaps at most \(2H-1\) has size
> \(O(A_m/m)\), uniformly for \(H\) in (5.4).

This is strictly weaker than asking that the *number* of such returns be
Catalan.  Many short coordinate returns are permitted, provided they cluster
through Catalan-many transition edges.  It is also the sharp statistic for
literal factorization: Theorem 2.1 loses at most one cut per PBBS cycle and
nothing else.

The complete-colour theorem, point homomesy, odd-gap rule, and the known
\(g=3\) estimate do not prove this packing theorem.  A proof must use the
specific parenthesis/PBBS dependence to show that short returns cluster, or
else replace the PBBS chronology by a row-coherent splice.

## 7. Quotient size and exact point margins do not prove the packing bound

The following deterministic construction shows why merely quotienting by
coordinate rotation cannot prove (5.3).  It is a theorem about projected
Johnson cycles, not a counterexample to the canonical PBBS map.

### Theorem 7.1 (many packed short returns with exact rank)

Let \(N=2r+1\), put \(k=r+1\), and let

\[
 2\le H=o(N).
\]

For all sufficiently large \(N\), there is a simple directed Johnson cycle

\[
 X_0,X_1,\ldots,X_{N-1}
 \quad\text{in }J(N,k)
\]

with all of the following properties.

1. Every coordinate is the entering coordinate exactly once and the
   departing coordinate exactly once.
2. The sum of all coordinate residence lengths is exactly \(Nk\), as it
   must be for rank \(k\).
3. The cycle contains at least

   \[
      \left\lfloor {N\over4H}\right\rfloor
   \]

   pairwise edge-disjoint positive-residence intervals of length exactly
   \(H\).

Thus exact arrival/departure margins and distinct projected owners permit
\(\Omega(N/H)\) packed short intervals in a single cycle.

#### Proof

Work in \(\mathbb Z_N\).  For a permutation \(\tau\) without fixed points,
put

\[
 R_i=(\tau(i)-i)\bmod N\in\{1,\ldots,N-1\}.
\tag{7.1}
\]

Coordinate \(i\) will be present at owner times

\[
 i,i+1,\ldots,i+R_i-1.
\tag{7.2}

Choose

\[
 p=\left\lfloor {N\over4H}\right\rfloor
\]

disjoint blocks of length \(4H\).  In block \(j\), choose two positions

\[
 a_j=4Hj+1,\qquad b_j=a_j+H,
\]

and make \((a_j\ b_j)\) a transposition of \(\tau\).  All these endpoints
have both cyclic neighbours outside the chosen endpoint set.  The two
residences supplied by this transposition are

\[
 R_{a_j}=H,\qquad R_{b_j}=N-H.
\tag{7.3}

Let \(R\) be the remaining set of positions and put \(M=|R|=N-2p\).
Then \(M\) is odd.  List its members in increasing cyclic order as

\[
 x_0<x_1<\cdots<x_{M-1}
\]

and set

\[
 w={M+1\over2},\qquad
 \tau(x_j)=x_{j+w\pmod M}.
\tag{7.4}

Since \(2w-M=1\), one has \(\gcd(w,M)=1\), so (7.4) is one cycle on all
of \(R\).  In the sorted cyclic order, the step \(j\mapsto j+w\) wraps
exactly \(w\) times.  Hence

\[
 \sum_{x\in R}R_x=wN.
\tag{7.5}

Every transposition contributes \(N\) to the residence sum.  Since

\[
 w={N-2p+1\over2}=k-p,
\]

equations (7.3)--(7.5) give

\[
 \sum_{i\in\mathbb Z_N}R_i=pN+wN=kN.
\tag{7.6}

Define

\[
 X_t=\{i:t-i\pmod N\in\{0,1,\ldots,R_i-1\}\}.
\tag{7.7}

The departure times \(\tau(i)=i+R_i\) are distinct.  Thus one coordinate
enters and one coordinate leaves at every transition.  All \(|X_t|\) are
equal, and (7.6) says their average is \(k\); hence every \(X_t\) is a
\(k\)-set and consecutive owners are Johnson adjacent.

We next verify simplicity.  For two times \(a\ne b\), let \(I\) be the
proper cyclic interval of arrival indices encountered after \(a\) and through
\(b\).  Then

\[
 X_a=X_b
 \quad\Longleftrightarrow\quad
 \tau(I)=I.
\tag{7.8}

Indeed, equality across the interval means that every coordinate has either
both its arrival and departure in \(I\), or neither; this is exactly
\(\tau(I)=I\).

Every invariant set of \(\tau\) is a union of some chosen transposition
pairs and, possibly, the one large cycle \(R\).  A nonempty union of chosen
pairs is not a cyclic interval: every one of its points has a neighbouring
unchosen point, and the two endpoints of each pair are separated by
\(H\ge2\).  Its complement is not a cyclic interval for the same reason.
Therefore no nonempty proper invariant set is a cyclic interval.  By (7.8),
the \(X_t\)'s are distinct.

Finally, each coordinate \(a_j\) has residence interval
\([a_j,b_j)\) of length \(H\).  The containing blocks have length \(4H\),
so even after adjoining the insertion and removal transition edges, these
\(p\) intervals are pairwise edge-disjoint.  This proves all assertions.
\(\square\)

### Consequence

Theorem 7.1 rules out a proof of the PBBS Catalan packing theorem using only

* one rotation quotient state per coordinate orbit;
* bijective arrival and departure labels;
* exact rank/point-incidence totals; and
* simplicity of the projected Johnson cycles.

The missing restriction is the actual parenthesis map.  In normalized
Dyck-root coordinates it is a specific skew product, not an arbitrary
departure permutation.  Any successful proof of (5.3) must exploit that
specific cocycle.

## 8. Even actual PBBS components can have linearly large packing

The next exact family shows that a Catalan proof cannot work component by
component.  One genuine PBBS component of quotient level three already has
\(\Theta(N)\) disjoint projected residence-three intervals.

### 8.1 The normalized Dyck-root cocycle

Normalize a middle state by rotating its unique unmatched zero to the first
position.  It then has the form

\[
 0D,
\]

where \(D\) is a Dyck word of semilength \(r\).  Let the first visit to the
maximum height of \(D\) end with the marked up-step in

\[
 D=P\,1\,Q,
\]

and put

\[
 \delta(D)=|P|+1,
 \qquad
 \phi(D)=\overline Q\,0\,\overline P.
\tag{8.1}
\]

Here the bar interchanges zero and one.

### Lemma 8.1 (exact PBBS skew product)

The word \(\phi(D)\) is Dyck, and the parenthesis/PBBS map is

\[
 (u,D)\longmapsto (u+\delta(D)\pmod N,\phi(D)),
\tag{8.2}
\]

where \(u\) is the coordinate of the unmatched zero.

#### Proof

The marked step is the first step reaching the maximum height \(h\).
The suffix \(Q\), read from height \(h\), never goes above its starting
height and ends at zero.  Thus \(\overline Q\) has nonnegative partial sums
and total height \(h\).  The following zero lowers this to \(h-1\).
Every prefix of \(P\) has height at most \(h-1\), so, when read from height
\(h-1\), \(\overline P\) never goes below zero and ends at zero.  Hence
\(\phi(D)\) is Dyck.

The PBBS update leaves the unmatched zero fixed and complements every bit
of \(D\), giving the cyclic word \(0\overline D\).  Its new unmatched zero
is exactly the complemented marked up-step at position \(|P|+1\).  Cutting
immediately after it reads \(\overline Q0\overline P\), proving (8.2).
\(\square\)

### Theorem 8.2 (a level-three PBBS packing family)

For every \(r\ge3\), the canonical PBBS factor on \(KG(2r+1,r)\) has one
component of length \(3N\) whose complement-projected step-two cycle obeys

\[
 \boxed{\nu_3\ge \lfloor N/2\rfloor=r.}
\tag{8.3}
\]

#### Proof

Put \(t=r-3\), and consider the three Dyck words

\[
\begin{aligned}
D_0&=110100(10)^t,\\
D_1&=1011(01)^t00,\\
D_2&=(10)^t110010.
\end{aligned}
\tag{8.4}
\]

Their first maximum-reaching up-steps occur respectively at positions

\[
 2,\qquad4,\qquad2t+2=N-5.
\tag{8.5}
\]

Applying (8.1) directly gives

\[
 D_0\longmapsto D_1\longmapsto D_2\longmapsto D_0,
\tag{8.6}
\]

so the quotient voltages are

\[
 (2,4,N-5).
\tag{8.7}
\]

Their total is \(N+1\equiv1\pmod N\), so this quotient three-cycle lifts
to one PBBS component of length \(3N\).  Starting at \(D_1\), the first
five voltage sums are

\[
 4,\quad N-1,\quad N+1,\quad N+5,\quad2N.
\tag{8.8}
\]

The first four are nonzero modulo \(N\), whereas the fifth is zero.  Thus
the next occurrence of the omitted coordinate has gap five and projected
residence three.

Take all \(N\) spatial rotations of this return interval.  The interval
uses four projected transition edges.  Three lie in distinct quotient-edge
orbits; the remaining quotient-edge orbit is used twice, at phases differing
by two.  Hence two rotations by phases \(a,b\in\mathbb Z_N\) intersect if
and only if

\[
 a-b\equiv\pm2\pmod N.
\tag{8.9}
\]

Their conflict graph is therefore
\(\operatorname{Cay}(\mathbb Z_N,\{\pm2\})\cong C_N\), since \(N\) is
odd.  Its independence number is \(\lfloor N/2\rfloor=r\).  Choosing a
maximum independent set gives \(r\) pairwise projected-edge-disjoint
residence-three intervals inside the single lifted component. \(\square\)

### Consequence for the Catalan attack

Theorem 8.2 is not a counterexample to the global bound (5.3), because the
global Catalan mass \(B\) is exponentially larger than \(N\).  It does prove
two useful negative facts about a prospective proof:

1. no bound \(O(\ell)\) is possible for a PBBS quotient component of level
   \(\ell\); and
2. one cannot inject packed arcs with bounded multiplicity into the quotient
   states of their own component.

A proof of (5.3) must instead be an **aggregate enumeration theorem over all
Dyck-root quotient cycles**.  It must show that components like (8.4) have
small total Catalan mass, even though each such component is individually
bad.

## 9. Two PBBS steps are an exact first-maximum block rotation

The one-step formula (8.1) can be sharpened substantially.  Let the marked
up-step of a Dyck word (D) be its first step which attains the global
maximum.  Starting immediately after that step, let the displayed zero below
be the first step which returns the path to height zero.  There is then a
unique factorization

\[
 D=P\,1\,R\,0\,S.                                      \tag{9.1}
\]

Thus (S) is a Dyck word: it is precisely the suffix of complete primitive
components lying after the first primitive component which attains the
global maximum.  The words (P) and (R) need not themselves be Dyck.

### Theorem 9.1 (two-step block rotation and deficit voltage)

For the factorization (9.1),

\[
 \boxed{
 \begin{aligned}
  \delta(D)&=|P|+1,\\
  \delta(\phi D)&=|R|+1,\\
  \phi^2(D)&=S\,1\,P\,0\,R.
 \end{aligned}}
                                                               \tag{9.2}
\]

Consequently, on putting

\[
 d(D)=|S|+1,
                                                               \tag{9.3}
\]

the two-step voltage obeys the ordinary integer identity

\[
 \boxed{
  \delta(D)+\delta(\phi D)=N-d(D),
 }
                                                               \tag{9.4}
\]

and the even-time skew product is

\[
 \boxed{
  (u,D)\longmapsto (u-d(D)\pmod N,\ \phi^2D).
 }
                                                               \tag{9.5}
\]

#### Proof

In (9.1), the suffix after the marked up-step is (R0S).  Formula
(8.1) gives

\[
 \phi(D)=\overline R\,1\,\overline S\,0\,\overline P.
                                                               \tag{9.6}
\]

Before the displayed (1), the path in (9.6) is the complement of the
descent from the old maximum down to height one.  It stays below the old
maximum height and reaches that height for the first time at the displayed
(1).  The remainder (overline S0\overline P) never exceeds it.  Hence
this displayed (1) is exactly the first maximum-reaching step of
(phi(D)), proving (delta(\phi D)=|R|+1).

Applying (8.1) once more to (9.6) gives

\[
 \phi^2(D)
 =\overline{\,\overline S0\overline P\,}\,0\,
   \overline{\overline R}
 =S1P0R,
\]

which proves (9.2).  Since

\[
 |P|+1+|R|+1+|S|=2r=N-1,
\]

equation (9.4) follows.  Reducing (9.4) modulo (N) in the skew product
(8.2) proves (9.5).  \(□\)

The important feature of (9.5) is that the complicated pair of
first-maximum positions has disappeared.  Its residue is the negative of a
positive odd integer (d(D)), and that integer is the length of an explicit
terminal Dyck suffix plus one.

## 10. Exact short-return word equations

Put

\[
 \tau=\phi^2.
\]

For (D_h=\tau^hD), use the unique decomposition

\[
 D_h=P_h1R_h0S_h                                      \tag{10.1}
\]

from (9.1).  Theorem 9.1 is equivalent to the word recursion

\[
 \boxed{
  P_{h+1}1R_{h+1}0S_{h+1}=S_h1P_h0R_h.
 }
                                                               \tag{10.2}
\]

### Theorem 10.1 (complete odd-return criterion)

The omitted coordinate at ((u,D)) returns after (2s+1) PBBS steps if
and only if

\[
 \boxed{
  \sum_{h=0}^{s-1} (|S_h|+1)
       \equiv |P_s|+1 \pmod N.
 }
                                                               \tag{10.3}
\]

It is the *first* return exactly when the same congruence fails with (s)
replaced by every (0\le j<s).  Equivalently, for a uniquely determined
integer (a\ge0),

\[
 \boxed{
  \sum_{h=0}^{s-1} (|S_h|+1)=|P_s|+1+aN.
 }
                                                               \tag{10.4}
\]

#### Proof

After (s) applications of (9.5), the spatial root is

\[
 u-\sum_{h=0}^{s-1}d(D_h)\pmod N.
\]

The final odd PBBS step adds (delta(D_s)=|P_s|+1).  It returns to (u)
precisely when (10.3) holds.  Positivity gives the unique integer form
(10.4), and applying the same statement to each shorter odd prefix gives
the first-return assertion.  \(□\)

Thus the aggregate PBBS problem has been reduced to a system of literal word
equations (10.2), the first-maximum admissibility conditions in (10.1), and
one length equation (10.4).  For the family in Theorem 8.2, start the
gap-five return at \(D_1\).  Then \(s=2\), \(\tau D_1=D_0\), and, with
\(t=r-3\),

\[
 \bigl(d(D_1),d(D_0)\bigr)=(1,2t+1)=(1,N-6),
 \qquad
 \delta(\tau^2D_1)=\delta(D_2)=N-5.
\]

Thus \(1+(N-6)=N-5\), so the return lies in the zero-winding case
\(a=0\).  The shorter display \((1,3)\) with endpoint deficit \(4\)
is only the special case \(r=4\), not the general family.

## 11. Exact enumeration of the one-step deficit

Although correlations between successive deficits remain unresolved, the
marginal distribution of (d(D)) has a closed Catalan generating function.
Let (C_h(z)) be the generating function for Dyck paths of height at most
(h), with semilength marked by (z).  Set

\[
 C_{-1}(z)=0,qquad C_0(z)=1,qquad
 C_h(z)={1\over1-zC_{h-1}(z)}.                       \tag{11.1}
\]

Let (b_{r,j}) be the number of (D\in\mathcal D_r) for which the suffix
(S) in (9.1) has semilength (j), equivalently (d(D)=2j+1).

### Theorem 11.1 (first-highest-component formula)

For (0\le j<r),

\[
 \boxed{
 b_{r,j}
 =\sum_{h\ge1}
  [z^{,r-j}]\,
     zC_{h-1}(z)\bigl(C_{h-1}(z)-C_{h-2}(z)\bigr)
  \;[z^j]C_h(z).
 }
                                                               \tag{11.2}
\]

Equivalently, the full bivariate generating series is

\[
 \boxed{
 \sum_{r\ge1}\sum_{0\le j<r} b_{r,j}x^{r-j}y^j
 =\sum_{h\ge1}
   xC_{h-1}(x)\bigl(C_{h-1}(x)-C_{h-2}(x)\bigr)C_h(y).
 }
                                                               \tag{11.3}
\]

#### Proof

Decompose a nonempty Dyck path into its primitive components.  Let (h) be
its global height and distinguish the first primitive component of height
(h).  The components preceding it form an arbitrary Dyck path of height
at most (h-1), contributing (C_{h-1}).  A primitive component of exact
height (h) has the form (1E0), where (E) has exact height (h-1),
and therefore contributes

\[
 z\bigl(C_{h-1}-C_{h-2}\bigr).
\]

The suffix after that distinguished component is an arbitrary Dyck path of
height at most (h), contributing (C_h).  The decomposition is unique,
and marking the first two parts by (x) and the suffix by (y) proves
(11.3), hence (11.2).  \(□\)

As a consistency check, setting (x=y=z) and using

\[
 zC_{h-1}(C_{h-1}-C_{h-2})C_h=C_h-C_{h-1}
\]

telescopes (11.3) to (C(z)-1), as required.

Theorem 11.1 removes the one-step counting problem completely.  The exact
remaining enumeration is genuinely a **correlation** problem for the block
rotation (10.2): bound edge-disjoint solutions of (10.2)--(10.4) after
summing over all Dyck roots.  In particular, replacing the successive
suffixes (S_h) by independent samples from (11.2) would discard precisely
the PBBS structure still needed for the Catalan packing theorem.

## 12. Winding is exactly chargeable; zero winding is the irreducible case

For a return interval (I) of odd PBBS gap (2s+1), define its
**two-step winding** (a(I)) by (10.4).  Its (s) step-two edges carry the
deficit weights

\[
 d(D_0),d(D_1),\ldots,d(D_{s-1}).
\]

Let

\[
 \mathscr D_r=\sum_{D\in\mathcal D_r}d(D)
              =\sum_{j=0}^{r-1}(2j+1)b_{r,j}.          \tag{12.1}
\]

### Theorem 12.1 (exact winding ledger for a packed family)

If (mathcal P) is any pairwise step-two-edge-disjoint family of PBBS
return intervals, then

\[
 \boxed{
  \sum_{I\in\mathcal P}
    \bigl(\delta(D_{s(I)}(I))+N a(I)\bigr)
  \le N\mathscr D_r.
 }
                                                               \tag{12.2}
\]

In particular,

\[
 \boxed{
  \sum_{I\in\mathcal P}a(I)\le\mathscr D_r.
 }
                                                               \tag{12.3}
\]

#### Proof

Equation (10.4) says that the deficit weight summed on the step-two edges
of (I) is exactly

\[
 \delta(D_{s(I)}(I))+Na(I).
\]

The intervals in (mathcal P) use disjoint step-two edges.  Every
normalized Dyck edge type (D) has exactly (N) spatial translates in the
full PBBS factor.  Hence the total available deficit weight on all physical
step-two edges is exactly (N\sum_Dd(D)=N\mathscr D_r).  Summing over the
packed intervals proves (12.2), and dropping the positive terminal terms
proves (12.3).  \(□\)

The theorem cleanly separates what a scalar voltage argument can and cannot
do.  Every positive-winding return consumes a full additional (N) units
of the explicit Catalan deficit mass (12.1).  But the family in Theorem 8.2
has (a(I)=0) for all of its short returns, so no estimate based only on
winding can control the required packing.  The irreducible enumeration
problem is therefore the zero-winding word equation

\[
 \boxed{
  \sum_{h=0}^{s-1}(|S_h|+1)=|P_s|+1,
 }
                                                               \tag{12.4}
\]

together with (10.2) and its positive-winding perturbations.  This is a
strictly narrower target than arbitrary modular cocycle return.

## 13. Endpoint parity alone is already saturated on the Gaussian scale

There is a tempting weaker approach to (10.2): retain only the initial and
terminal Dyck words.  That loses too much information at exactly the desired
scale.

Let (D) be a Dyck word and give a (1)-step sign (+1) and a (0)-step
sign (-1).  If an odd PBBS segment of length (g) begins and ends with the
same unmatched coordinate, then outside the coordinates which occur an odd
number of times as intermediate unmatched coordinates, the terminal Dyck
word is the bitwise complement of (D).  If the odd-support positions in
the balanced part are (R), the terminal height is therefore

\[
 H_E(t)=-H_D(t)+2\sum_{i\in R,,i\le t}\operatorname{sgn}_D(i).
                                                               \tag{13.1}
\]

The next theorem shows that this necessary endpoint condition is essentially
vacuous once (g) reaches the natural Dyck-height scale.

### Theorem 13.1 (canonical complement repair by record steps)

Let (D) have height (h).  For each (1\le a\le h), mark

* the first up-step of (D) which enters height (a); and
* the last down-step of (D) which leaves height (a).

Let (R(D)) be these (2h) marked positions, and obtain (E(D)) by
keeping the bits of (D) on (R(D)) and complementing every other bit.
Then

\[
 \boxed{E(D)\text{ is a Dyck word and }
        |{i:E_i(D)=D_i}|=2h.}                     \tag{13.2}
\]

#### Proof

The marked up-steps contribute (+1) and the marked down-steps contribute
(-1), so the correction term in (13.1) ends at zero and (E(D)) is
balanced.

At a time (t), let (M(t)) be the greatest height reached by (D) up to
time (t), and let (L(t)) be the greatest level whose last downward exit
has already occurred.  Before any marked last exits, the correction in
(13.1) is (2M(t)), which dominates (H_D(t)).  More generally, after the
last exit from levels (h,h-1,\ldots,a+1), the future path has height at
most (a), while the correction still has value (2a).  Between record
events its value is constant.  Thus at every time

\[
 2\sum_{i\in R(D),,i\le t}\operatorname{sgn}_D(i)
 \ge H_D(t),
\]

and (13.1) gives (H_E(t)\ge0).  Hence (E(D)) is Dyck.  The first-entry
up-steps and last-exit down-steps are all distinct, giving exactly (2h)
agreements.  \(□\)

Thus every height-(h) Dyck root satisfies the endpoint parity algebra of
an odd segment using only (2h+1) odd-support coordinates (including the
returned unmatched coordinate).  Height-bounded Dyck paths are counted
exactly by

\[
 [z^r]C_h(z).
                                                               \tag{13.3}
\]

For (h) on the order of (sqrt r), this is already a nonnegligible
fraction of the Catalan scale (as follows, for example, from the standard
finite-path transfer matrix for (11.1)).  Consequently no argument using
only

* the parity formula for the two endpoint states,
* the number of exceptional coordinates, and
* Dyck nonnegativity at the two endpoints

can prove the required Catalan packing bound in a Gaussian window.  The
intermediate first-maximum constraints in the word recursion (10.2) are
indispensable.  This is an endpoint-level obstruction, not a counterexample
to the actual PBBS theorem.

## 14. Exact peak-deletion renormalization

There is a further exact self-similarity which is invisible in the scalar
deficit ledger.  It does not by itself prove the Catalan packing theorem, but
it turns every prospective violation of the vacancy-gap bound into a smaller
PBBS passage problem.

Let a cyclic rank-\(r\) word \(w\) have distinguished unmatched zero \(u\),
so that cutting after \(u\) gives \(0D\) with \(D\) Dyck.  Put

\[
 k=\operatorname{pk}(D),\qquad d=r-k,
 \qquad p=N-2k=2d+1.                                  \tag{14.1}
\]

Call an edge of the coordinate cycle an **equality particle** when its two
endpoint bits agree.  There are exactly \(p\) such edges: each peak accounts
for one \(10\)-edge and cyclic balance gives equally many \(01\)-edges, so
the other \(N-2k\) edges are equal.  The edge immediately before \(u\) is a
\(00\)-particle and the edge immediately after \(u\) is unequal.

Label the equality particles in cyclic order.  Record on a particle the
common bit on its two endpoints.  Start at the particle immediately before
\(u\).  The resulting cyclic word has the form

\[
 0\,\partial D,                                      \tag{14.2}
\]

where \(\partial D\) is obtained from \(D\) by simultaneously deleting
every peak \(10\).

### Theorem 14.1 (PBBS renormalizes on equality particles)

The word \(\partial D\) is Dyck of semilength \(d\).  Under one PBBS
update of the original \(N\)-site state:

1. the distinguished equality particle moves forward by one physical edge;
2. every other equality particle stays on its physical edge;
3. the bit recorded on the distinguished particle remains zero, while all
   other recorded bits are complemented; and
4. the newly distinguished equality particle is the unique unmatched zero
   of the updated length-\(p\), rank-\(d\) particle word.

Consequently the recorded particle word evolves by the canonical PBBS map on
\(KG(p,d)\).

#### Proof

Write

\[
 D=1^{a_1}0^{b_1}\cdots1^{a_k}0^{b_k}.
\]

Deleting the last \(1\) and first \(0\) at every peak leaves

\[
 1^{a_1-1}0^{b_1-1}\cdots1^{a_k-1}0^{b_k-1},          \tag{14.3}
\]

with empty powers omitted.  This is exactly the sequence of common bits on
the equality edges after the distinguished root particle.  Simultaneous
deletion of peak pairs from a Dyck path leaves a Dyck path: deleting a local
\(10\) excursion changes neither endpoint height nor any height outside that
two-step excursion.  Its semilength is \(r-k=d\), proving (14.2).

The original PBBS update complements every bit except the unmatched zero
\(u\).  Hence an equality edge not incident with \(u\) stays equal and its
recorded bit is complemented.  The equality edge before \(u\) is \(00\) and
becomes unequal; the edge after \(u\) is \(01\) and becomes \(00\).  Thus the
distinguished particle moves from the former edge to the latter and keeps
recorded bit zero.  Its destination was not occupied by another equality
particle, so cyclic particle order is preserved.

Apply the first paragraph to the updated original state.  Its particle word,
rooted immediately before its new unmatched coordinate, again has a Dyck
tail.  Therefore that root particle is precisely the unique unmatched zero
of the particle word.  The recorded-bit update is complement-everything-
except-that-zero, which is the PBBS rule on \(KG(2d+1,d)\). \(\square\)

Label the equality particles persistently in cyclic order, and let
\(x_j(t)\in\mathbb Z_N\) be the physical edge occupied by particle \(j\) at
time \(t\).  If \(\kappa_t\) is the omitted label of the renormalized PBBS,
then Theorem 14.1 gives the exact skew system

\[
 \boxed{
 \begin{aligned}
  x_{\kappa_t}(t+1)&=x_{\kappa_t}(t)+1,\\
  x_j(t+1)&=x_j(t)\quad(j\ne\kappa_t),\\
  \lambda_t&=x_{\kappa_t}(t)+1.
 \end{aligned}}
                                                               \tag{14.4}
\]

All positions are read modulo \(N\); integer lifts may be chosen so that
particle order is preserved.

### Corollary 14.2 (a short return is an adjacent-particle passage)

Suppose \(\lambda_t=\lambda_{t+g}\), with no intervening occurrence of that
physical label, and \(g<N\).  If particle \(a=\kappa_t\) makes the first
entry into that physical edge, then

\[
 \boxed{\kappa_{t+g}=a-1\pmod p,}                    \tag{14.5}
\]

where \(a-1\) is the immediate predecessor in cyclic particle order.
Moreover particle \(a\) is selected at least once at an intermediate time.

#### Proof

After time \(t\), particle \(a\) occupies the edge labelled
\(\lambda_t\).  It must be selected again before that edge can be entered a
second time.  Equality particles never overtake.  Hence the next particle
which can enter the vacated edge is the immediate predecessor of \(a\).
The alternative in which \(a\) itself travels once around the physical
cycle uses at least \(N\) particle moves, impossible because \(g<N\).
This proves both assertions. \(\square\)

At this stage the formerly proposed vacancy-gap statement
\(g\ge p=2d+1\) becomes an adjacent-particle passage assertion in the smaller
PBBS.  Section 18 below explicitly disproves it.  The recursive reduction is
nevertheless useful: it proves the sharp height bound in Section 16 and gives
the complete gap-seven classification in Section 18.

## 15. Depth two is completely covered

Let \(B_i=A_{2i}\) be an original PBBS step-two Johnson cycle and put

\[
 C_i=B_i\cap B_{i+1},\qquad T_i=C_i\cap C_{i+1}.
                                                               \tag{15.1}
\]

The \(C_i\)'s are the depth-one lower colours, while

\[
 T_i=B_i\cap B_{i+1}\cap B_{i+2}                       \tag{15.2}
\]

is the depth-two target produced by the consecutive two-edge turn.  The
no-gap-three theorem says exactly that \(C_i\ne C_{i+1}\), and hence \(T_i\)
has the desired depth-two rank.  Coverage requires an additional
deficit-five argument, which is now available.

Write

\[
 \mu^{\rm turn}_2(S)=\#\{i:T_i=S\},\qquad
 M^{\rm turn}_2=\#\{S:\mu^{\rm turn}_2(S)=0\}.        \tag{15.3}
\]

### Theorem 15.1 (complete second PBBS turn shadow)

For the canonical PBBS on \(KG(2m+1,m)\), every
\(S\in\binom{[2m+1]}{m-2}\) occurs, and

\[
 \boxed{1\le\mu^{\rm turn}_2(S)\le10.}               \tag{15.4}
\]

#### Proof

Fix \(S\), and let \(U_+(S)\) and \(U_-(S)\) be its five forward and five
reverse unmatched zeros.  In physical circular order form a ten-symbol word:
write \(A_x\) for \(x\in U_+(S)\), \(C_x\) for
\(x\in U_-(S)\), and at a shared coordinate use the local order
\(C_x,A_x\).  The word contains five symbols of each kind, so it has a cyclic
transition

\[
 A_c,C_b.                                             \tag{15.5}
\]

An arbitrary \(A\to C\) transition need not work; this corrects the
earlier version of this proof.  Index the \(C\)-symbols cyclically and let
\(z_i\) be the number of \(A\)-symbols between consecutive \(C_i,C_{i+1}\).
Choose \(C_i\) at a global maximum of the prefix potential with increments
\(z_i-1\), as in Lemma 21.1.  Its preceding symbol is an \(A\), and at this
boundary there are at most one \(A\)-symbol before the next \(C\)-symbol and,
dually, at most one \(C\)-symbol before the previous \(A\)-symbol.

Let \(a\) be the next \(C\)-mark after \(C_b\), and let \(d\) be the
previous \(A\)-mark before \(A_c\).  Flipping \(b\) leaves the three old
forward marks immediately preceding \(b\) and the three old reverse marks
immediately succeeding \(b\).  The two corridor inequalities therefore make
\(A_c,C_a\) the surviving strict predecessor/successor pair.  The reversed
statement at \(c\) makes \(A_d,C_b\) the other pair.  The exact
deficit-three rule gives

\[
 f^2(S\cup\{a,b\})=S\cup\{b,c\},\qquad
 f^2(S\cup\{b,c\})=S\cup\{c,d\}.                   \tag{15.6}
\]

The three even-time states contain \(S\), and the no-gap-three theorem says
their intersection has rank exactly \(m-2\); it is therefore \(S\).  This
proves the lower bound in (15.4).  For the upper bound, a correct path deletes
two distinct labels from its initial state, both among the five reverse
unmatched zeros of \(S\).  That unordered pair determines the initial state
and hence the PBBS path, giving at most \(\binom52=10\) occurrences.
\(\square\)

For all sufficiently large \(m\), the depth-two balanced floor is one.  Put

\[
 R_2=W-\binom{2m+1}{m-2}
 ={6(m+1)W\over(m+2)(m+3)}<12\operatorname{Cat}_m.   \tag{15.7}
\]

Complete support and total mass give

\[
 \sum_S(\mu^{\rm turn}_2(S)-1)=R_2.                 \tag{15.8}
\]

Consequently the balanced overload and floor-corrected pair collision obey

\[
 \boxed{
  O_2(P_m)\le R_2<12\operatorname{Cat}_m,
  \qquad
  \sum_S\binom{\mu^{\rm turn}_2(S)-1}{2}
  \le4R_2<48\operatorname{Cat}_m.}                  \tag{15.9}
\]

The second inequality uses \(\mu-1\le9\) and
\(\binom{x}{2}\le4x\) for \(0\le x\le9\).  Thus both depth-two gates are
closed: every turn has the correct rank, every target occurs, and its total
overload/collision defect is Catalan.  The unresolved multidepth core now
begins genuinely at depth three.

## 16. Return gap dominates Dyck height

The renormalization theorem proves a pointwise restriction which is sharp but
still subcritical for the desired Gaussian-above window.

### Theorem 16.1 (height-gap theorem)

Let \((u,D)\) start a consecutive omitted-label return of odd gap \(g\) in
the PBBS on \(KG(2r+1,r)\).  Then

\[
 \boxed{g\ge 2\operatorname{ht}(D)+1.}               \tag{16.1}
\]

#### Proof

We induct on \(g\).  If \(g\ge N=2r+1\), then
\(\operatorname{ht}(D)\le r\le(g-1)/2\), so suppose \(g<N\).

Use the equality-particle PBBS of Theorem 14.1.  At the initial return edge,
particle \(a\) moves into the physical edge which is to be revisited.  By
Corollary 14.2, \(a\) must be selected again before the predecessor particle
can make the final entry.  Let \(h\) be its first subsequent selection time.
Then \(h\) is a consecutive omitted-label gap in the renormalized PBBS.
Same-label gaps are odd, and equality at gap one would repeat a factor state;
hence \(h\ge3\).  Also \(h<g\), and since both are odd,

\[
 h\le g-2.                                            \tag{16.2}
\]

The normalized Dyck root of the renormalized PBBS is \(\partial D\).
By induction (the case in which its circumference is at most \(h\) is
already covered by the first, trivial branch),

\[
 \operatorname{ht}(\partial D)\le {h-1\over2}.       \tag{16.3}
\]

Simultaneously deleting every peak from a nonempty Dyck path lowers its
height by exactly one.  This is immediate in the plane-tree contour
bijection: peaks are precisely leaf edges, and pruning every leaf lowers the
tree height by one.  Therefore

\[
 \operatorname{ht}(D)
 =\operatorname{ht}(\partial D)+1
 \le {h+1\over2}
 \le {g-1\over2},
\]

which is (16.1).  The induction starts because a gap-one return is
impossible. \(\square\)

For gap five the argument is sharper.  The intermediate return in the
renormalized PBBS must have gap three.  The no-gap-three theorem forces that
renormalized system to have rank one.  Hence every gap-five root satisfies

\[
 r-\operatorname{pk}(D)=1.                           \tag{16.4}
\]

This explains why the explicit family in Theorem 8.2 has only polynomial
Catalan mass despite its linear spatial-translate packing.

### Corollary 16.2 (sub-Gaussian Catalan packing)

If

\[
 H=o\!\left(\sqrt{r/\log r}\right),                  \tag{16.5}
\]

then the *total number*, not merely the maximum packing, of PBBS residence
intervals of length at most \(H\) is \(o(B)\).  In particular,

\[
 \boxed{\nu_H(P_r)=o(B).}                            \tag{16.6}
\]

#### Proof

A residence interval of length at most \(H\) comes from a gap at most
\(2H-1\).  Theorem 16.1 forces its normalized root to have height at most
\(H-1\).  The number of Dyck paths of semilength \(r\) and height at most
\(h\) is the number of length-\(2r\) closed walks from zero in the path graph
on \(\{0,1,\ldots,h\}\).  Its adjacency spectral radius is

\[
 2\cos{\pi\over h+2},
\]

so this number is at most

\[
 (2\cos(\pi/(h+2)))^{2r}
 \le 4^r\exp(-c r/h^2)                               \tag{16.7}
\]

for an absolute \(c>0\).  Every quotient root has exactly \(N\) physical
rotations.  Since \(B=\operatorname{Cat}_r\asymp4^r/r^{3/2}\), the ratio of
all possible short-return starts to \(B\) is at most

\[
 O\!\left(r^{5/2}e^{-c r/H^2}\right)=o(1)            \tag{16.8}
\]

under (16.5).  This proves (16.6). \(\square\)

Theorem 16.1 is sharp at the level of height: the recorded rank-six example
has height three and gap seven.  But typical Dyck height is of order
\(\sqrt r\), so (16.7) becomes useless when
\(H=\sqrt r\,\omega(r)\).  The remaining constant-one theorem must therefore
use packedness or a statistic stronger than height; endpoint parity and peak
pruning alone cannot reach the required window.

## 17. Exact deck reduction to a super-sparse Dyck-quotient packing

The spatial rotation deck can be removed completely after the short quotient
cycles are discarded.  This identifies the scale of the genuinely global
enumeration theorem.

Let \(\overline P_r\) be the quotient of the complement-projected step-two
factor by cyclic coordinate rotation.  Its directed edge set is naturally
indexed by the \(B\) Dyck roots, and its cycle permutation is
\(\tau=\phi^2\).  A physical short-return interval projects to a consecutive
edge interval in one \(\tau\)-cycle; the return criterion is independent of
the spatial phase, so every quotient interval has all \(N\) spatial lifts.

Call a quotient cycle **short** when its length is at most \(H+1\), the
largest number of projected transition edges in a residence-\(H\) interval.
Let \(Z_H\) be the number of quotient edges on short cycles.  On the other
cycles every relevant quotient interval is nonwrapping and uses distinct
quotient edges.  Let \(\overline\nu_H\) be the maximum cardinality of an
edge-disjoint family of these nonwrapping quotient intervals.

### Theorem 17.1 (deck packing/transversal equivalence)

Let \(\tau_H(P_r)\) be the minimum number of physical transition edges
meeting every residence-\(H\) interval.  Then

\[
 \boxed{
  N\overline\nu_H
  \le \nu_H(P_r)
  \le \tau_H(P_r)
  \le 2N\overline\nu_H+NZ_H .}
                                                               \tag{17.1}
\]

#### Proof

Choose an edge-disjoint quotient family of size \(\overline\nu_H\).  For one
member, its \(N\) spatial lifts use different physical edges above every
quotient edge in its trace, and hence are pairwise disjoint.  Lifts belonging
to two selected quotient intervals are also disjoint because their quotient
edge traces are disjoint.  This gives the first inequality in (17.1).

For the reverse direction, work on one long quotient cycle which contains at
least one short-return interval.  The circular interval packing--transversal
sandwich gives a quotient hitting set of size at most \(\bar\nu_C+1\).  Since
\(\bar\nu_C\ge1\), this is at most \(2\bar\nu_C\).  Lift every chosen quotient
edge through all \(N\) spatial phases.  The lifted set hits every physical
lift of every interval on that quotient cycle.  Summing over long cycles
costs at most \(2N\overline\nu_H\).  Finally, cutting every physical edge
above every short-cycle quotient edge costs \(NZ_H\) and hits all remaining
intervals.  This proves the last inequality; the middle inequality is the
elementary packing lower bound for a transversal. \(\square\)

The quotient short-cycle term is negligible throughout the intended PBBS
range.  Indeed, an ordered voltage itinerary of length \(q\) determines a
quotient \(\phi\)-cycle of period \(q\), so the number of quotient states on
cycles of period at most \(Q\) is at most \(QN^Q\).  A \(\tau\)-cycle of
length at most \(H+1\) comes from a \(\phi\)-cycle of length at most
\(2H+2\).  Hence

\[
 Z_H\le (2H+2)N^{2H+2}.                              \tag{17.2}
\]

If \(H\log N=o(r)\), in particular in (5.4), then

\[
 NZ_H=\exp(o(r))=o(B).                               \tag{17.3}
\]

### Corollary 17.2 (the exact quotient gate)

Uniformly when \(H\log N=o(r)\),

\[
 \boxed{
  \nu_H(P_r)=O(B)
  \quad\Longleftrightarrow\quad
  \overline\nu_H=O(B/N).}                           \tag{17.4}
\]

The implication from right to left uses (17.1)--(17.3); the converse uses
the first inequality of (17.1).

Thus a successful PBBS proof must establish an unexpectedly sparse global
fact inside the Dyck quotient: among its \(B\) transition edges, all
short-return intervals together have interval packing number only
\(O(B/N)\).  A single bad quotient interval on a long cycle already supplies
\(N\) disjoint physical intervals.  The explicit level-three obstruction is
harmless only because one quotient interval is still negligible compared
with \(B/N\).  Marginal voltage rarity, endpoint parity, and componentwise
estimates do not imply (17.4); the needed input is a cross-orbit clustering or
enumeration theorem at the precise \(1/N\) quotient scale.

## 18. Peak-defect vacancy is false: an all-dimensional gap-seven family

The stronger candidate

\[
 g\ge 2(r-\operatorname{pk}(D))+1                   \tag{18.1}
\]

is false.  The equality-particle recursion gives an explicit symbolic
counterfamily without search.

First classify defect-one roots.  For semilength \(d\), every Dyck path with
\(d-1\) peaks has a unique form

\[
 E(a,b,c)=(10)^a\,1(10)^b0\,(10)^c,                 \tag{18.2}
\]

where \(a,c\ge0\), \(b\ge1\), and \(a+b+c=d-1\).  Direct substitution in
(8.1) gives

\[
 \boxed{
  \phi E(a,b,c)=E(b-1,c+1,a),\qquad
  \delta(E(a,b,c))=2(a+1).}                         \tag{18.3}
\]

In particular this affine action has period three, and the three voltages are

\[
 2(a+1),\qquad2b,\qquad2(c+1),                       \tag{18.4}
\]

whose sum is \(2d+2=(2d+1)+1\).

Fix \(d\ge2\), put \(p=2d+1\), and take

\[
 E_d=E(d-2,1,0)=(10)^{d-2}1100.                    \tag{18.5}
\]

Starting its omitted particle label at zero, (18.3) gives the first eight
labels

\[
 0,\quad p-3,\quad p-1,\quad1,\quad p-2,\quad0,
 \quad2,\quad p-1.                                  \tag{18.6}
\]

Thus particle zero returns at time five, while its immediate cyclic
predecessor \(p-1\) is selected at times two and seven.

### Theorem 18.1 (gap seven with arbitrary peak defect)

Let \(d\ge2\) and \(r\ge2d-1\).  Put

\[
 D_{r,d}
 =(10)^{,r-(2d-1)}(1100)^{d-2}111000.              \tag{18.7}
\]

Then \(D_{r,d}\) is a Dyck word of semilength \(r\), has height three and
peak defect \(d\), and starts a consecutive PBBS omitted-label return of gap
seven.  Hence (18.1) fails whenever \(d\ge4\).  In particular it fails in
every semilength \(r\ge7\) by taking \(d=4\).

#### Proof

Every displayed block in (18.7) is Dyck, so the concatenation is Dyck and its
height is three.  It has

\[
 r-(2d-1)+(d-2)+1=r-d
\]

peaks, hence peak defect \(d\).  Simultaneous peak deletion gives

\[
 \partial D_{r,d}=(10)^{d-2}1100=E_d.               \tag{18.8}
\]

Because \(D_{r,d}\) ends in \(000\), the distinguished equality particle
and its immediate predecessor occupy adjacent physical edges.  Let the
returned physical coordinate be \(u\).  At time zero, particle zero moves
from edge \(u-1\) to edge \(u\).  By (18.6), particle \(p-1\) moves at time
two; it starts at edge \(u-2\), so it moves to \(u-1\).  Particle zero is not
selected again until time five, when it moves from \(u\) to \(u+1\).
Particle \(p-1\) is next selected at time seven and moves from \(u-1\) to
\(u\).  No particle can enter the occupied edge \(u\) earlier, and after time
five the predecessor already blocks it until time seven.  Equation (14.4)
therefore gives a consecutive physical omitted-label return exactly at gap
seven.

For \(d\ge4\), its proposed vacancy lower bound is \(2d+1\ge9>7\), proving
the counterexample. \(\square\)

Theorem 18.1 shows that no pointwise statistic depending only on peak defect,
the number of equality particles, or the first pruned core can establish the
mesoscopic residence estimate.  The true pointwise restriction (16.1) is
already sharp on a family with unbounded defect.  What remains in (17.4) is
therefore irreducibly an aggregate packing/clustering theorem over many Dyck
quotient cycles.

The gap-seven roots can in fact be classified and counted exactly.

### Theorem 18.2 (complete gap-seven classification)

A Dyck root \(D\) of semilength \(r\) starts a consecutive gap-seven return
if and only if, for some \(d\ge2\),

\[
 \boxed{
  \partial D=(10)^{d-2}1100
  \quad\text{and}\quad D\text{ ends in }00.}          \tag{18.9}
\]

Consequently the exact number of quotient roots starting a gap-seven return
is

\[
 \boxed{R_7(r)=2^{r-1}-r.}                           \tag{18.10}
\]

#### Proof

Suppose first that \(D\) starts a gap-seven return and let
\(E=\partial D\) be the equality-particle PBBS root of rank \(d\).  The
leading particle must be selected again before the final predecessor entry.
Its first repeat in the compressed PBBS has odd gap either three or five.

If that gap is three, the no-gap-three theorem forces \(d=1\).  But the
rank-one PBBS omitted labels advance cyclically by one on three labels, so at
time seven the selected label is the successor, not the predecessor, of the
initial label.  This contradicts Corollary 14.2.

Hence the compressed repeat has gap five.  As noted after Theorem 16.1, this
forces \(E\) to have defect one.  Write it as \(E(a,b,c)\) in (18.2).  The
first five voltages are the first two full-cycle voltages repeated after the
three-voltage sum \(p+1\).  Modulo \(p=2d+1\), their sum is

\[
 1+2(a+1)+2b=p-2c.                                  \tag{18.11}
\]

It vanishes exactly when \(c=0\).  After this return, the next two voltages
are \(2\) and \(2(a+1)\), so the selected particle is the predecessor at time
seven exactly when

\[
 2a+4=p-1=2d.                                       \tag{18.12}
\]

Thus \(a=d-2\), \(b=1\), proving the first condition in (18.9).

For this compressed root, the predecessor particle is selected exactly at
times two and seven.  It enters the original returned physical edge on its
second move if and only if it started immediately behind the distinguished
particle.  In the rooted word \(0D\), those two equality particles occupy
adjacent edges exactly when the last two bits of \(D\) are \(00\).  This
proves necessity.  The particle itinerary (18.6) proves the converse exactly
as in Theorem 18.1.

It remains to count.  Under the plane-tree contour bijection, \(\partial D\)
is obtained by pruning every leaf.  Fix a nonempty core tree \(T\) with
\(d\) edges and \(k\) leaves.  Every preimage is obtained by attaching new
leaf children in the ordered child slots of the \(d+1\) core vertices, with
at least one new child at each of the \(k\) core leaves.  Since the sum of
the numbers of child slots is

\[
 \sum_{v\in T}(\deg^+(v)+1)=2d+1,                   \tag{18.13}
\]

the attachment generating function is

\[
 {z^k\over(1-z)^{2d+1}}.                            \tag{18.14}
\]

For the core in (18.9), \(k=d-1\).  The terminal condition \(D\) ends in
\(00\) forbids new leaf children in the final root slot (the rightmost core
child is already nonleaf), reducing the exponent in (18.14) by one.  The
number of semilength-\(r\) preimages is therefore

\[
 [z^{r-d}]{z^{d-1}\over(1-z)^{2d}}
 =\binom r{2d-1}.                                    \tag{18.15}
\]

Summing over \(d\ge2\) gives the sum of all odd binomial coefficients except
\(\binom r1\):

\[
 R_7(r)=\sum_{d\ge2}\binom r{2d-1}=2^{r-1}-r.
\]

This proves (18.10). \(\square\)

### Corollary 18.3 (the exact exponential scale of gap-seven packing)

Let \(\nu^{(7)}(P_r)\) be the maximum number of pairwise projected-edge-
disjoint residence intervals arising specifically from gap-seven returns.
Then

\[
 \boxed{
 {N\over9}\bigl(2^{r-1}-r-O(N^{10})\bigr)
 \le \nu^{(7)}(P_r)
 \le N(2^{r-1}-r).}                                 \tag{18.16}
\]

In particular

\[
 \boxed{\nu^{(7)}(P_r)=\Theta(N2^r)=o(B).}           \tag{18.17}
\]

#### Proof

Every gap-seven quotient interval contains five consecutive projected
transition edges.  Quotient \(\tau\)-cycles of length at most five contain
only \(O(N^{10})\) quotient states by the voltage-itinerary estimate used in
(17.2).  On every remaining quotient cycle the intervals are ordinary
length-five intervals.  One such interval intersects intervals beginning at
at most nine possible quotient edges.  A greedy packing therefore selects at
least one ninth of all their starts.  Lifting each selected quotient interval
through all \(N\) phases gives the lower bound in (18.16), by Theorem 17.1.
The upper bound is simply the total number \(NR_7(r)\) of physical gap-seven
starts.  Finally \(B\asymp4^r/r^{3/2}\), which proves (18.17). \(\square\)

Thus gap seven already supplies exponentially many short returns and an
exponentially large physical packing, but only at base two rather than the
Catalan base four.  It is rigorously harmless for constant one.  Any genuine
obstruction to (17.4) must arise from gaps growing with \(r\), where the
iterated pruned cores have enough entropy to approach Catalan scale.

For reference, the same calculation gives an exact classification one gap
earlier.

### Corollary 18.4 (all gap-five roots)

A semilength-\(r\) Dyck root starts a consecutive gap-five return if and only
if

\[
 \boxed{D=(10)^a1(10)^b0,qquad a\ge0, b\ge1, a+b=r-1.}
                                                               \tag{18.18}
\]

Hence there are exactly \(r-1\) quotient roots and \(N(r-1)\) physical
gap-five starts.

#### Proof

The intermediate equality-particle return has gap three, so the pruned PBBS
has rank one; equivalently \(D\) has defect one.  Write \(D=E(a,b,c)\) as in
(18.2).  Equation (18.11) is the gap-five congruence and holds exactly when
\(c=0\).  The proper partial returns are excluded by the odd-gap rule and the
no-gap-three theorem.  There are \(r-1\) pairs \((a,b)\). \(\square\)

At rank depth three, gap three is absent and every gap-five start contributes
one unit to the PBBS intersection-rank excess.  Therefore

\[
 \boxed{E_3(P_r)=N(r-1).}                            \tag{18.19}
\]

This is polynomial, hence much smaller than the Catalan scale.  Thus the
depth-three rank gate is also closed after polynomially many local cuts; its
target-support question is separate, just as depth-two support required the
deficit-five theorem in Section 15.

## 19. A literal five-rank PBBS word

The complete depth-two support theorem is already strong enough to produce a
genuine contiguous-OR word for five consecutive ranks, with no separate
factorability or pin-survival hypothesis.

### Theorem 19.1 (literal depth-two PBBS conversion)

Put \(n=2m+1\) and \(W=\binom{n}{m}\).  For every \(m\ge2\), there is a
nonzero contiguous-OR word of length at most

\[
 \boxed{W+4\operatorname{Cat}_m}                    \tag{19.1}
\]

which covers every set in the five ranks

\[
 \boxed{m-1,m,m+1,m+2,m+3.}                         \tag{19.2}
\]

In particular its length is \(W+O(W/m)\).

#### Proof

Let \((A_i)\) run over the PBBS odd-graph factor on the rank-\(m\) sets,
and put \(X_i=[n]\setminus A_i\).  The step-two sequences

\[
 \ldots,X_i,X_{i+2},X_{i+4},\ldots                  \tag{19.3}
\]

form disjoint Johnson cycles on rank \(m+1\).  Consecutive occurrences of an
omitted label have gap at least five.  By the residence calculation (1.3),
every positive coordinate run in every cycle (19.3) therefore has at least
three vertices.

On one such cycle, reindex consecutive vertices as
\(X_0,\ldots,X_{L-1}\), cyclically, and define

\[
 D_i=X_i\cap X_{i+1}\cap X_{i+2}.                   \tag{19.4}
\]

Emit

\[
 D_0,D_1,\ldots,D_{L-1},D_0,D_1,D_2,D_3.            \tag{19.5}
\]

For a fixed coordinate, its indicator on the \(X\)-cycle is a union of
cyclic one-runs of length at least three.  Taking the indicators in (19.4)
erodes every run by two positions.  Dilating back by unions of consecutive
entries gives, pointwise and hence as set identities,

\[
\begin{aligned}
D_i&=X_i\cap X_{i+1}\cap X_{i+2},\\
D_i\cup D_{i+1}&=X_{i+1}\cap X_{i+2},\\
D_i\cup D_{i+1}\cup D_{i+2}&=X_{i+2},\\
D_i\cup\cdots\cup D_{i+3}&=X_{i+2}\cup X_{i+3},\\
D_i\cup\cdots\cup D_{i+4}&=X_{i+2}\cup X_{i+3}\cup X_{i+4}.
                                                               \tag{19.6}
\end{aligned}
\]

The four repeated entries in (19.5) expose all windows crossing the cyclic
seam.

It remains to identify the five target families.  Restoring the original
PBBS indices, disjointness of adjacent odd-graph states gives

\[
\begin{aligned}
X_i\cap X_{i+2}\cap X_{i+4}
 &=A_{i+1}\cap A_{i+3},\\
X_i\cap X_{i+2}
 &=[n]\setminus(A_i\cup A_{i+2})=A_{i+1},\\
X_i&=[n]\setminus A_i,\\
X_i\cup X_{i+2}
 &=[n]\setminus(A_i\cap A_{i+2}),\\
X_i\cup X_{i+2}\cup X_{i+4}
 &=[n]\setminus(A_i\cap A_{i+2}\cap A_{i+4}).       \tag{19.7}
\end{aligned}
\]

The first equality uses the correct rank supplied by no gap three; the
containment is immediate from adjacent disjointness and both sides have size
\(m-1\).  The PBBS complete first-shadow theorem says the two-state
intersections in (19.7) cover every rank-\((m-1)\) set.  Theorem 15.1 says
the three-state intersections cover every rank-\((m-2)\) set.  Complements
and the middle ownership of the factor therefore show that the five lines of
(19.6) cover respectively every set of ranks

\[
 m-1,m,m+1,m+2,m+3.
\]

All entries \(D_i\) have size \(m-1\), so they are nonzero.  Finally, a PBBS
component of length \(\ell N\) gives at most \(\ell\) step-two cycles, and
the sum of all levels \(\ell\) is \(W/N=\operatorname{Cat}_m\).  Thus the
number of words (19.5) is at most \(\operatorname{Cat}_m\).  Their unextended
parts contain exactly \(W\) entries, and the four seam entries per cycle cost
at most \(4\operatorname{Cat}_m\).  Concatenating the words proves (19.1).
\(\square\)

This is a genuine depth-two result: rank correctness, complete lower and
upper shadows, erosion factorization, coordinate residence, and cyclic seam
repair are all proved.  It upgrades the earlier three-rank first-band theorem
to five ranks in one parity.  It still does not address a growing central
band, so it does not by itself prove constant one.

## 20. A literal seven-rank PBBS word

The complete third-turn support theorem gives one further exact band.  At
this depth four-fold erosion is not everywhere invertible: a projected
coordinate can have a positive run of length three.  The obstruction is
nevertheless negligible, because such runs are exactly the gap-five returns
classified in Corollary 18.4.

### Theorem 20.1 (literal depth-three PBBS conversion)

Put \(n=2m+1\), \(W=\binom{n}{m}\), and assume \(m\ge3\).  There is a
nonzero contiguous-OR word of length at most

\[
 \boxed{
 W+6\operatorname{Cat}_m+21(2m+1)(m-1)}              \tag{20.1}
\]

which covers every set in the seven ranks

\[
 \boxed{m-2,m-1,m,m+1,m+2,m+3,m+4.}                 \tag{20.2}
\]

In particular its length is \(W+O(W/m)\).

#### Proof

Use the complement-projected step-two PBBS cycles \(X_i=[n]\setminus A_i\)
from Theorem 19.1, and on one such cycle reindex consecutive vertices as
\(X_0,\ldots,X_{L-1}\).  Put

\[
 D_i=X_i\cap X_{i+1}\cap X_{i+2}\cap X_{i+3}.       \tag{20.3}
\]

The identity \(X_i\cap X_{i+1}=A_{i+1}\), with the old PBBS indices
restored, shows more generally that \(D_i\) is the intersection of three
consecutive states on the interleaved step-two \(A\)-cycle.  The pointwise
depth-two rank theorem therefore gives

\[
 |D_i|=m-2,                                           \tag{20.4}
\]

so every emitted entry is nonzero.

Emit around this cycle

\[
 D_0,D_1,\ldots,D_{L-1},D_0,D_1,\ldots,D_5.          \tag{20.5}
\]

First suppose a fixed coordinate has no positive \(X\)-run of length three.
Every positive run then has length at least four.  Four-fold erosion followed
by dilation gives, pointwise and hence as set identities,

\[
\begin{aligned}
D_i&=X_i\cap X_{i+1}\cap X_{i+2}\cap X_{i+3},\\
D_i\cup D_{i+1}&=X_{i+1}\cap X_{i+2}\cap X_{i+3},\\
D_i\cup D_{i+1}\cup D_{i+2}&=X_{i+2}\cap X_{i+3},\\
D_i\cup\cdots\cup D_{i+3}&=X_{i+3},\\
D_i\cup\cdots\cup D_{i+4}&=X_{i+3}\cup X_{i+4},\\
D_i\cup\cdots\cup D_{i+5}&=X_{i+3}\cup X_{i+4}\cup X_{i+5},\\
D_i\cup\cdots\cup D_{i+6}&=X_{i+3}\cup X_{i+4}\cup X_{i+5}\cup X_{i+6}.
                                                               \tag{20.6}
\end{aligned}
\]

A positive run of length three is erased completely by (20.3).  For that
coordinate it spoils at most respectively

\[
 1,2,3,4,5,6                                           \tag{20.7}
\]

of the windows on the last six lines of (20.6), and none on the first line.
Thus it creates at most \(21\) bad intended windows.  For every intended
window on which (20.6) fails, append its right-hand-side target literally.

By (1.3), positive projected runs of length three are in bijection with
consecutive omitted-label gaps of length five.  Corollary 18.4 counts exactly

\[
 (2m+1)(m-1)                                           \tag{20.8}
\]

such starts.  Hence all literal repairs together cost at most the last term
in (20.1).

It remains to identify the intended target families.  With the original
indices restored, the first four lines of (20.6) are respectively

\[
\begin{aligned}
X_i\cap X_{i+2}\cap X_{i+4}\cap X_{i+6}
  &=A_{i+1}\cap A_{i+3}\cap A_{i+5},\\
X_i\cap X_{i+2}\cap X_{i+4}
  &=A_{i+1}\cap A_{i+3},\\
X_i\cap X_{i+2}&=A_{i+1},\\
X_i&=[n]\setminus A_i.                                \tag{20.9}
\end{aligned}
\]

The last three lines are complements of, respectively, two-, three-, and
four-state intersections on the other step-two (A)-cycle.  Complete
depth-one support, Theorem 15.1, and the complete third-turn support theorem
therefore show that the seven right-hand sides cover every set in the ranks
listed in (20.2).  At depth three we use only the correct-rank four-state
occurrences supplied by that theorem; if one of their intended windows is
bad, it was included in the literal repair above.

The unextended cycle words contain exactly \(W\) entries in total.  As in
Theorem 19.1, the number of step-two cycles is at most
\(\operatorname{Cat}_m\), and six repeated entries per cycle expose every
window crossing a seam.  Adding the repair bound proves (20.1).  \(\square\)

Theorem 20.1 settles literal factorability through depth three.  It remains
a fixed-depth theorem: constant one still requires an analogue for a band
whose depth tends past the Gaussian scale.

## 21. Every PBBS turn shadow has complete support

The fixed-label ladder is false for an arbitrary \(A\to C\) boundary; an
explicit counterexample is recorded in
PBBS_GENERAL_MARK_LADDER_AUDIT_20260725.md.  The stronger global-maximum
boundary in Lemma 21.1 avoids that obstruction.  Independent targeted
audits of both its forward and reverse surviving-mark calculations, including
shared coordinates, verify the proof below.

Thus the target-support question is removed at every depth.  The remaining
constant-one obstruction is the physical residence/erosion cost.

Fix \(1\le q\le m\) and

\[
 S\in\binom{[2m+1]}{m-q}.
\]

The word of \(S\) has \(d=2q+1\) forward-unmatched zeros and \(d\)
reverse-unmatched zeros.  Form their expanded circular word by writing
\(A_x\) at every forward mark and \(C_x\) at every reverse mark, with the
local order \(C_x,A_x\) at a shared coordinate.

### Lemma 21.1 (global-maximum two-sided corridor)

There is an \(A_0,C_0\) boundary such that, if
\(C_0,C_1,\ldots,C_{d-1}\) are the \(C\)-symbols in forward order and
\(A_0,A_1,\ldots,A_{d-1}\) are the \(A\)-symbols in backward order, then

\[
\begin{aligned}
x_j&:=\#\{\text{\(A\)-symbols strictly between \(C_0\) and \(C_j\)}\}
     \le j,\\
y_j&:=\#\{\text{\(C\)-symbols met backwards from \(A_0\) to \(A_j\)}\}
     \le j
\end{aligned}                                                   \tag{21.1}
\]

for every \(1\le j\le d-1\).

#### Proof

Index the \(C\)-symbols cyclically and put

\[
 z_i=\#\{\text{\(A\)-symbols strictly between \(C_i\) and \(C_{i+1}\)}\}.
\]

Then \(\sum_i z_i=d\).  Define a periodic prefix potential by

\[
 H(i+1)-H(i)=z_i-1.                                  \tag{21.2}
\]

Choose \(i\) at a global maximum of \(H\).  Since
\(H(i)-H(i-1)=z_{i-1}-1\ge0\), the gap before \(C_i\) contains an
\(A\)-symbol, and its final symbol supplies the required \(A_0,C_0\)
boundary.  For every \(j\ge1\),

\[
 \sum_{h=0}^{j-1}z_{i+h}-j=H(i+j)-H(i)\le0,           \tag{21.3}
\]

which is \(x_j\le j\).

For the reverse inequality, the \(L\) gaps immediately preceding \(C_i\)
contain

\[
 \sum_{h=1}^{L}z_{i-h}
 =d-\sum_{h=0}^{d-L-1}z_{i+h}\ge L.                  \tag{21.4}
\]

Taking \(L=j+1\), the current gap and the preceding \(j\) gaps contain at
least \(j+1\) \(A\)-symbols.  Starting at the final \(A\)-symbol of the
current gap, the \(j\)-th previous \(A\)-symbol is therefore reached after
crossing at most \(j\) \(C\)-symbols.  Thus \(y_j\le j\).  \(\square\)

### Theorem 21.2 (complete correct PBBS support at every depth)

For every \(1\le q\le m\) and every
\(S\in\binom{[2m+1]}{m-q}\), there is a canonically oriented \(q\)-edge
path under \(g=f^2\),

\[
 B_0\longrightarrow B_1\longrightarrow\cdots\longrightarrow B_q,
\]

such that

\[
 \boxed{\bigcap_{t=0}^{q}B_t=S.}                     \tag{21.5}
\]

Moreover the number of correct-rank occurrences satisfies

\[
 \boxed{
 1\le\mu_{P,q}^{\mathrm{corr}}(S)\le\binom{2q+1}{q}.} \tag{21.6}
\]

#### Proof

Use the boundary from Lemma 21.1 and define

\[
 P_t=
 \{C_0,\ldots,C_{q-t-1}\}
 \cup
 \{A_0,\ldots,A_{t-1}\},
 \qquad0\le t\le q.                                  \tag{21.7}
\]

We prove that \(B_t=S\cup P_t\) are the required states.  Fix
\(0\le t<q\), put \(r=q-t-1\), and let

\[
 K_t=S\cup\{C_0,\ldots,C_{r-1}\}
          \cup\{A_0,\ldots,A_{t-1}\}.                \tag{21.8}
\]

This is the proposed common rank-\((m-1)\) core of \(B_t,B_{t+1}\).
Write the forward marks as

\[
 F_0=A_0,F_1,\ldots,F_{d-1},
 \qquad A_j=F_{d-j}.
\]

Process the flips \(C_0,\ldots,C_{r-1}\).  Inductively, the first \(j\)
flips remove \(F_1,\ldots,F_{2j}\): before \(C_j\) is flipped,
\(x_j\le j\le2j\) says every old forward mark preceding it has already
been removed, so its flip removes the next two surviving marks
\(F_{2j+1},F_{2j+2}\).  The selected cyclically consecutive marks
\(A_0,\ldots,A_{t-1}\) then remove themselves and the next \(t\)
surviving marks.  Exactly

\[
 U_+(K_t)=\{A_t,A_{t+1},A_{t+2}\}                   \tag{21.9}
\]

remain.  The inequality \(x_r\le r\le2r\) makes \(A_t\) the strict
predecessor of \(C_r\) in this triple.  The reversed argument gives

\[
 U_-(K_t)=\{C_r,C_{r+1},C_{r+2}\},                  \tag{21.10}
\]

with \(C_r\) the strict successor of \(A_t\).  The exact deficit-three
predecessor/successor law now gives

\[
 g(K_t\cup\{C_r\})=K_t\cup\{A_t\},                  \tag{21.11}
\]

which is the \(t\)-th arrow.

It remains only to exclude collisions between selected \(A\)- and
\(C\)-labels.  If \(C_j=A_h\), the forced local order \(C_x,A_x\) gives

\[
 d-h-1=x_j\le j.                                    \tag{21.12}
\]

This is incompatible with \(j+h\le q-1\).  Hence no coordinate is
duplicated inside a \(P_t\), and none belongs to every \(P_t\).  Thus every
\(|P_t|=q\) and \(\bigcap_tP_t=\varnothing\), proving (21.5).

For the cap, the \(q\) labels deleted from the initial state are distinct
members of the \(2q+1\) reverse-unmatched zeros of \(S\), and determine the
oriented PBBS path.  This gives (21.6).  \(\square\)

Theorem 21.2 is an all-depth support theorem, but not yet an all-depth
literal word.  To erode by \(q+1\) consecutive projected owners and dilate
back, every positive coordinate run shorter than \(q+1\) must be cut or
repaired.  By (0.1), the exact remaining assertion is still

\[
 \nu_H(P_m)=O\!\left(\frac{W}{m}\right)
\]

for \(H=\sqrt m\,\omega(m)\), equivalently the quotient packing bound
\(\overline\nu_H=O(\operatorname{Cat}_m/(2m+1))\) from Corollary 17.2.

The preceding (O(W/m)) target belongs to the pair-omission residence
architecture studied earlier in this note.  For a direct all-depth
erosion of the PBBS turn shadows, cut repair carries a quadratic-in-(H)
toll.  The following fixed-window little-oh formulation is a clean
residence-only sufficient theorem for the literal constant-one problem.

## 22. Fixed-window residence packing implies constant one

Put

\[
 B_m=\operatorname{Cat}_m=\frac{W}{2m+1},
 \qquad H_A=\lceil A\sqrt m\rceil .                 \tag{22.1}
\]

Consider the following statement for each fixed \(A>0\):

\[
 \boxed{\nu_{H_A}(P_m)=o_A(B_m).}                   \tag{RP_A}
\]

Here the little-oh is as \(m\to\infty\), with \(A\) fixed.  No uniformity
in \(A\) is required.

### Lemma 22.1 (exact endpoint-capped erosion)

Let

\[
 X_0,X_1,\ldots,X_{v-1}
\]

be a directed Johnson path of rank-\((m+1)\) owners.  Assume every
internally bounded positive coordinate run has at least \(H+1\) owners.
Extend the path constantly at its endpoints:

\[
 \widetilde X_i=
 \begin{cases}
 X_0,&i<0,\\
 X_i,&0\le i<v,\\
 X_{v-1},&i\ge v.
 \end{cases}
\]

For \(-H\le i\le v-1\), put

\[
 D_i=\bigcap_{j=0}^{H}\widetilde X_{i+j}.            \tag{22.2}
\]

Then the word

\[
 D_{-H},D_{-H+1},\ldots,D_{v-1}                     \tag{22.3}
\]

has length \(v+H\), all its entries are nonempty, and it represents every
intersection and every union of at most \(H+1\) consecutive owners lying
wholly in the path.

More exactly, for \(1\le t\le H+1\),

\[
 \bigcup_{a=0}^{t-1}D_{i+a}
 =\bigcap_{a=t-1}^{H}\widetilde X_{i+a},             \tag{22.4}
\]

and, for \(0\le s\le H\),

\[
 \bigcup_{a=0}^{H+s}D_{i+a}
 =\bigcup_{a=H}^{H+s}\widetilde X_{i+a}.             \tag{22.5}
\]

#### Proof

Fix one coordinate.  Constant endpoint extension makes every positive run
touching an endpoint infinite, while every internally bounded positive run
has length at least \(H+1\).  The indicator of \(D_i\) is the ordinary
\((H+1)\)-fold erosion of this binary run sequence.  Unions of \(t\)
consecutive eroded indicators dilate it back by \(t-1\) positions.  On
each positive run this gives exactly (22.4) for \(t\le H+1\), and then
(22.5) for the following \(H\) dilations.  The identities are coordinatewise,
hence are set identities.

For an intersection \(X_b\cap\cdots\cap X_{b+p-1}\), choose
\(t=H-p+2\) and \(i=b-H+p-1\) in (22.4).  For a union
\(X_b\cup\cdots\cup X_{b+p-1}\), choose \(s=p-1\) and \(i=b-H\) in
(22.5).  The inequalities \(1\le p\le H+1\) and
\(0\le b\le b+p-1<v\) put all required \(D\)-indices in
\([-H,v-1]\).

Finally, an intersection of \(H+1\) consecutive rank-\((m+1)\) Johnson
owners loses at most one coordinate per transition, and therefore has size
at least \(m+1-H>0\).  Endpoint repetitions only increase it.  Thus every
entry in (22.3) is nonzero.  \(\square\)

### Theorem 22.2 (residence-only constant-one reduction)

If \((\mathrm{RP}_A)\) holds for every fixed \(A>0\), then

\[
 \boxed{\nu(k)\le(1+o(1))
        \binom{k}{\lfloor k/2\rfloor}.}             \tag{22.6}
\]

#### Proof

Work first in odd dimension \(n=2m+1\).  Use the complement-projected
step-two PBBS Johnson cycles \(X_i=[n]\setminus A_i\), of rank \(m+1\).
Their total number \(c_2(P_m)\) is at most \(B_m\), and their total number
of vertices is \(W\).

Fix \(H<m\).  Call a projected cycle *good* if it has no positive
coordinate residence of length at most \(H\).  On a good cycle of length
\(L\), use the cyclic \(H\)-fold erosion

\[
 D_i=\bigcap_{j=0}^{H}X_{i+j}
\]

and repeat its first (2H) entries.  The erosion--dilation identities
give a literal word of length (L+2H) exposing every intended lower
intersection and upper union through depth (H), including those crossing
the cyclic seam.

Now let \(C\) be a bad cycle.  Choose a transversal of its short residence
intervals.  By Theorem 2.1 it has size

\[
 \tau_H(C)\le\nu_H(C)+1\le2\nu_H(C),               \tag{22.7}
\]

because a bad cycle has \(\nu_H(C)\ge1\).  Cut at those transition
edges.  Every resulting path has no short internal positive run, so the
endpoint-capped erosion theorem applies.  The erosion entries cost
\(L+H\tau_H(C)\).  At one cut, at depth \(q\), at most \(q\) lower and
\(q\) upper intended windows are destroyed.  Appending every destroyed
target literally therefore costs at most

\[
 2\sum_{q=1}^{H}q=H(H+1)                            \tag{22.8}
\]

per cut.  Thus the complete bad-cycle cost is at most

\[
 L+(H^2+2H)\tau_H(C)
 \le L+2(H^2+2H)\nu_H(C).                          \tag{22.9}
\]

Summing good and bad cycles yields a literal central-band word of length

\[
 \boxed{
 W+2HB_m+2(H^2+2H)\nu_H(P_m).}                     \tag{22.10}
\]

All its entries are nonempty, since an \(H\)-edge Johnson window can lose
at most \(H\) coordinates from a rank-\((m+1)\) owner and \(H<m\).

Before cutting, the intended lower families are consecutive intersections
of projected owners, hence shifted consecutive intersections of PBBS middle
states.  The intended upper families are their complements.  Theorem 21.2
supplies every correct lower target at every depth, and hence also every
complementary upper target.  The literal repair counted in (22.8) restores
every intended occurrence destroyed by cutting.  Consequently the word in
(22.10) covers all ranks

\[
 m+1-H,m+2-H,\ldots,m+1+H.                         \tag{22.11}
\]

For fixed \(A\), take \(H=H_A\).  Under \((\mathrm{RP}_A)\), the two
normalized excesses in (22.10) satisfy

\[
 \frac{HB_m}{W}=O_A(m^{-1/2})=o_A(1),
 \qquad
 \frac{H^2\nu_H(P_m)}{W}=o_A(1).                  \tag{22.12}
\]

We now diagonalize.  For each positive integer \(j\), choose \(M_j\) so
large that for \(m\ge M_j\),

\[
 \nu_{\lceil j\sqrt m\rceil}(P_m)\le B_m/j^4,
 \qquad m\ge j^4.                                  \tag{22.13}
\]

Increase the \(M_j\)'s further so that the already proved product-SCD tail
word outside the depth-\(j\sqrt m\) band has normalized length tending to
zero as \(j\to\infty\).  Put \(a(m)=j\) on
\(M_j\le m<M_{j+1}\) and \(H_m=\lceil a(m)\sqrt m\rceil\).  Then

\[
 a(m)\to\infty,\qquad H_m=o(m),                    \tag{22.14}
\]

and (22.10), (22.13) give

\[
 \frac{2H_mB_m+2(H_m^2+2H_m)\nu_{H_m}(P_m)}{W}
 =O\!\left(\frac{a(m)}{\sqrt m}+\frac1{a(m)^2}\right)
 =o(1).                                             \tag{22.15}
\]

Appending the product-SCD tail word therefore covers every remaining rank
at cost \(o(W)\).  This proves (22.6) in odd dimension.  The standard
trimmed one-coordinate lift transfers the same leading constant to even
dimension. \(\square\)

Theorem 22.2 removes every shadow-support and multiplicity issue, but its
singleton repair is not optimal.  Section 24 replaces the quadratic term
in (22.10) by a linear cut seam; the resulting sufficient packing gate is
big-oh Catalan rather than little-oh Catalan.

## 23. Retraction of a proposed zero-winding converse

An attempted converse asserted that \(d(D)=1\) forces the next omitted-label
return to have gap \(2\operatorname{ht}(D)+1\).  That assertion and the
resulting claimed counterexample to \((\mathrm{RP}_A)\) are **retracted**.

The error was in a proposed first-deepest-spine sector shift: after applying
\(\tau\), a transported \(A_i\)-forest can become the new first deepest
branch.  Controlling only the transported \(B_i\)-forests does not preserve
the displayed spine.

A concrete counterexample is

\[
 D=1110011000.
 \tag{23.1}
\]

It has \(d(D)=1\), but its quotient orbit has

\[
 (\delta,d)=(3,1),(3,5),(7,1)
 \tag{23.2}
\]

and returns to \(D\).  At the proposed height time the cumulative deficit
is not the terminal first-maximum position, so the claimed return does not
occur.  A second example is

\[
 D=11100011110000,
 \tag{23.3}
\]

whose \(\tau\)-orbit has deficits \((1,1,7)\) and first-maximum positions
\((10,4,4)\); again the claimed gap fails.

The converse also fails inside the primitive family used in the attempted
Catalan lower bound.  The primitive root

\[
 D=1111100001110000
 \tag{23.4}
\]

has height five and \(d(D)=1\), but its five-state \(\tau\)-cycle has
deficits \((1,1,1,7,1)\) and first-maximum positions
\((11,5,5,5,11)\) in cycle order.  Starting at the displayed root, the
five deficits sum to \(11\) while the terminal first-maximum position is
\(5\), so there is no gap-eleven return.

The path-graph estimate showing that primitive height-\(O(\sqrt r)\) roots
have positive Catalan mass is correct, but the primitive counterexample
shows that it yields no residence lower bound.  Therefore
\((\mathrm{RP}_A)\) is currently neither proved nor disproved.  The
independent counteraudit is recorded in
PBBS_ZERO_WINDING_CONVERSE_COUNTERAUDIT_20260725.md.

## 24. Linear dominance-staircase seams and the weakened packing gate

The \(H(H+1)\) literal-repair term in (22.8) is not intrinsic. Fix one
cut between adjacent rank-\((m+1)\) owners \(X_{-1},X_0\), and assume
\(2H\le m+1\). For \(1\le s,t\le H\), set

\[
 P_{s,t}=\bigcap_{i=-s}^{t-1}X_i,
 \qquad C=X_{-1}\cap X_0.
\tag{24.1}
\]

For each \(x\in C\), let \(u_x,v_x\in[H]\) be the capped left and right
lengths of its positive run through the cut. Then

\[
 P_{s,t}=\{x\in C:u_x\ge s,\ v_x\ge t\}.
\tag{24.2}
\]

Call \(P_{s,t}\) floor-correct when
\(|P_{s,t}|=m+2-s-t\).

### Lemma 24.1 (southwest exclusion)

If \(P_{s,t}\) is floor-correct, there is no \(x\in C\) with
\(u_x<s\) and \(v_x<t\).

#### Proof

The window in (24.1) has \(s+t-1\) Johnson transitions. Map each
coordinate of \(X_{-s}\setminus P_{s,t}\) to its first departure
transition. This is injective. A coordinate with both strict extent
inequalities has an internal arrival and a later internal departure; that
later departure is not the first departure of any initial coordinate.
Hence at most \(s+t-2\) transitions occur in the injection, which gives
\(|P_{s,t}|\ge m+3-s-t\), a contradiction. \(\square\)

Take the Pareto-minimal points among the distinct pairs \((u_x,v_x)\).
Join them, in increasing first and decreasing second coordinate, by a
southeast unit lattice path \(\Gamma\) from \((1,H)\) to \((H,1)\), moving
east before south between consecutive minima. It has exactly \(2H-1\)
vertices. Emit the set-letter \(P_z\) at every vertex \(z\) of \(\Gamma\).

### Lemma 24.2 (linear lower chart)

For every floor-correct \(q=(s,t)\),

\[
 \boxed{
 P_q=\bigcup_{\substack{z\in V(\Gamma)\\z\ge q}}P_z.}
\tag{24.3}
\]

The selected vertices form one contiguous subpath, and every emitted
letter is nonempty.

#### Proof

Monotonicity of the two coordinates along \(\Gamma\) makes the selected
vertices contiguous, and (24.2) gives one inclusion. Conversely, if
\(x\in P_q\), choose a Pareto-minimal extent point below
\((u_x,v_x)\). Lemma 24.1 excludes the strictly southwest case. The
east-before-south convention then forces \(\Gamma\) to meet the rectangle
\([q,(u_x,v_x)]\); at such a vertex \(z\), (24.2) gives \(x\in P_z\).
Finally \(P_z\) intersects at most \(2H\) owners, so its size is at least
\(m+2-2H\ge1\). \(\square\)

The literal owner word

\[
 X_{-H},X_{-H+1},\ldots,X_{H-1}
\tag{24.4}
\]

has length \(2H\) and represents every crossing upper union of at most
\(H+1\) owners. Concatenating (24.3) and (24.4) gives a nonzero one-cut
chart of exact length

\[
 \boxed{4H-1.}
\tag{24.5}
\]

If a cycle of length \(L\) is opened at a residence transversal of size
\(J\), endpoint-capped erosion costs \(L+HJ\), and the charts cost
\((4H-1)J\). Thus its complete cost is

\[
 \boxed{L+(5H-1)J.}
\tag{24.6}
\]

Taking a minimum transversal on every active projected cycle and using
\(J\le2\nu_H\), while inactive cycles retain their cyclic \(2H\) collars,
gives the global central-band ledger

\[
 \boxed{
 L_H\le W+2HB_m+2(5H-1)\nu_H(P_m).}
\tag{24.7}
\]

### Theorem 24.3 (Catalan-order residence packing suffices)

Suppose that for every fixed \(A>0\), with
\(H_A=\lceil A\sqrt m\rceil\),

\[
 \boxed{\nu_{H_A}(P_m)=O_A(B_m).}
\tag{CP_A}
\]

Then

\[
 \nu(k)\le(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\tag{24.8}
\]

#### Proof

For fixed \(A\), (24.7) has excess
\(O_A(H_AB_m)=O_A(W/\sqrt m)=o_A(W)\). Diagonalize over integer
\(A\to\infty\) slowly enough to absorb the implicit constants in
\((CP_A)\), append the proved product-SCD tail, and use the trimmed
one-coordinate lift for the other parity, exactly as in Theorem 22.2.
\(\square\)

After discarding the negligible short quotient cycles, \((CP_A)\) is
equivalent, up to absolute factors, to

\[
 \boxed{
 \overline\nu_{H_A}=O_A\!\left({B_m\over2m+1}\right).}
\tag{24.9}
\]

This big-oh Catalan packing statement is a convenient strong sufficient
input, but the linear ledger (24.7) permits the following weaker threshold.

### Theorem 24.4 (critical reciprocal-height packing suffices)

Suppose that, for every fixed \(A>0\),

\[
 \boxed{\nu_{H_A}(P_m)=o_A(B_m\sqrt m).}
\tag{ST_A}
\]

Then (24.8) holds. Equivalently, after discarding the negligible short
quotient cycles,

\[
 \boxed{\overline\nu_{H_A}=o_A(B_m/\sqrt m).}
\tag{QST_A}
\]

#### Proof

The last term of (24.7) is
\(O_A(\sqrt m)\,o_A(B_m\sqrt m)=o_A(mB_m)=o_A(W)\),
and the collar term is already \(o_A(W)\). The same diagonal tail and
parity argument as Theorem 24.3 completes the proof. The deck equivalence
uses the exact long-cycle inequalities
\(N\overline\nu_H\le\nu_H\le2N\overline\nu_H+NZ_H\), with
\(NZ_{H_A}=\exp(o(m))\).
\(\square\)

The height-gap theorem and the exact Dyck height spectrum already give

\[
 \overline\nu_{H_A}=O_A(B_m/\sqrt m).
\tag{24.10}
\]

Thus the sharp remaining input of the separate-cut architecture is only a
vanishing improvement over reciprocal-height saturation.  The stronger
\((CP_A)\) remains useful for the fixed-core completion route.  The
complete independent seam proof is recorded in
MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md, and the corrected
threshold audit in MATH_ATTACK_L_CORRECTED_CHRONOLOGY_TRACE_GATE_20260725.md.

## 25. Reduction to simple fixed-core open-wreath sectors

Call a consecutive omitted-label return of gap \(2s+1\) **simple** when
its half-open label list

\[
 \lambda_0,\lambda_1,\ldots,\lambda_{2s}
\]

is pairwise distinct.  Write

\[
 a_j=\lambda_{2j}\ (0\le j\le s),
 \qquad b_j=\lambda_{2j+1}\ (0\le j<s).
\]

The PBBS recurrence alone then gives disjoint cores \(K,K'\), each of
size \(r-s\), such that

\[
 A_{2j}=K\cup\{a_0,\ldots,a_{j-1}\}
             \cup\{b_j,\ldots,b_{s-1}\},
\tag{25.1}
\]

\[
 A_{2j+1}=K'\cup\{b_0,\ldots,b_{j-1}\}
               \cup\{a_{j+1},\ldots,a_s\}.
\tag{25.2}
\]

Thus both owner parities are fixed-core consecutive halves of one cyclic
window system, and the two endpoint Kneser edges form the exact core-swap
square

\[
 (K\cup U,K'\cup V),
 \qquad (K'\cup U,K\cup V),
\tag{25.3}
\]

where \(U=\{b_0,\ldots,b_{s-1}\}\) and
\(V=\{a_1,\ldots,a_s\}\).  No winding assumption is used.

### Theorem 25.1 (factor-two minimal-return reduction)

Every projected-edge-disjoint family of return intervals contains a
projected-edge-disjoint family of simple returns of at least half its
cardinality, with no increase in the maximum gap.

#### Proof

Inside each return, repeatedly choose two consecutive occurrences of an
internally repeated label.  The resulting strictly nested process ends at a
simple subreturn.  If that subreturn begins an even number of one-step
edges after its parent, its projected trace is contained in the parent
projected trace.  If it begins an odd number, its projected trace is
contained in the global one-edge translate of the parent trace.  Split all
subreturns by this parity.  Translation is a bijection of the full
projected edge set, so each parity class is edge-disjoint; retain the larger
class. \(\square\)

Consequently

\[
 \nu_H^{\rm simp}(P_r)\le\nu_H(P_r)
 \le2\nu_H^{\rm simp}(P_r),
\tag{25.4}
\]

and the same holds in the long-cycle rotation quotient.  Therefore
\((CP_A)\) is, up to a factor two, exactly the statement that the
fixed-core open-wreath sectors (25.1)--(25.3) have quotient packing
\(O_A(B_r/(2r+1))\).  Internal nesting and the zero/positive-winding split
are no longer part of the local geometry.  The full proof and parity audit
are recorded in PBBS_MINIMAL_RETURN_FIXED_CORE_NORMAL_FORM_20260725.md.

## 26. Multi-cut clustering removes the per-cut initialization toll

The one-cut chart can be shared by every collection of cuts lying in one
short owner interval.  If a cut cluster has leftmost and rightmost cuts
separated by span \(S\), and

\[
 3H+S\le m+1,
\tag{26.1}
\]

then a single global endpoint-plane Pareto staircase covers all
floor-correct lower targets crossing the cluster, including the lower
targets formerly carried by the negative endpoint-erosion prefix.  One
owner halo covers the corresponding upper targets and singleton owners.
The exact auxiliary length is at most

\[
 \boxed{7H+3S-3.}
\tag{26.2}
\]

The base erosion word keeps only its nonnegative entries, so its total
length over all cut paths is exactly the original owner length, with no
remaining \(HJ\) initialization term.

More explicitly, every maximal positive coordinate run \([L,R]\) is
represented by the endpoint point \((-L,R)\).  An owner intersection over
\([a,b]\) contains that coordinate exactly when

\[
 (-L,R)\ge(-a,b).
\]

Floor correctness again excludes a point strictly southwest of the query.
One east-before-south Pareto path through the endpoint rectangle therefore
gives all cluster intersections as contiguous unions.  Adding virtual cuts
in the first \(H\) positions after every actual path start supplies exactly
the witnesses lost by deleting the negative erosion entries.  The full
proof is in PBBS_MULTI_CUT_DOMINANCE_CLUSTER_20260725.md.

For cut clusters of spans \(S_j\) on all physical owner cycles, define

\[
 \mathfrak S_H=\sum_j(7H+3S_j-3).
\tag{26.3}
\]

Then the complete central-band word has length

\[
 \boxed{W+2HB_m+\mathfrak S_H.}
\tag{26.4}
\]

### Theorem 26.1 (clustered-span sufficient gate)

If, for every fixed \(A>0\), one can choose residence transversals and
clusters at \(H_A=\lceil A\sqrt m\rceil\) satisfying (26.1) and

\[
 \boxed{\mathfrak S_{H_A}=o_A(W),}
\tag{CS_A}
\]

then coefficient one follows by the same diagonal product-tail argument as
Theorems 22.2 and 24.3.

For deck-invariant choices, the quotient form of \((CS_A)\) asks for
clustered-span cost \(o_A(B_m)\).  The current direct packing-and-clustering
ledger gives only \(O_A(B_m)\).  Thus this fusion route is missing a
vanishing active-span density.  The weakest separate-cut route is
\((QST_A)\), asking for a vanishing improvement over
\(O_A(B_m/\sqrt m)\); \((CP_A)\) is the stronger fixed-core completion
target.

## 27. Fractional ambient completions give a second scalar form of \((CP_A)\)

For a simple return of gap \(2s+1\), retain the notation of Section 25 and
put

\[
 U=\{b_0,\ldots,b_{s-1}\},\qquad
 A=\{a_0,\ldots,a_s\},\qquad q=r-s.
\]

Order the two inactive cores \(K,K'\) independently and uniformly.  The
resulting ambient wreath consists of the fixed open PBBS segment and two
random Boolean chains.  For a fixed middle vertex \(T\), its probability
of occurring outside the open segment is exactly

\[
 \mathbf1_{\{T\cap Z=U\}}
 {1\over\binom qj^2},
 \qquad j=|T\cap K|,
 \tag{27.1}
\]

or

\[
 \mathbf1_{\{T\cap Z=A\}}
 {1\over\binom qj\binom q{j+1}},
 \qquad j=|T\cap K'|.
 \tag{27.2}
\]

The excluded odd endpoints already belong to the fixed open segment.  The
formula follows by requiring the indicated subsets to be prefixes or
suffixes of the two independent core orders.

For a projected-edge-disjoint simple-sector family, every middle vertex
lies in at most four fixed open segments.  If \(\pi_I(T)\) denotes the sum
of (27.1)--(27.2), the exact double-counting criterion is therefore

\[
 \boxed{
  \sup_T\sum_{I\in\mathcal P}\pi_I(T)=O_A(1)
  \quad\Longrightarrow\quad
  |\mathcal P|=O_A(B_r).}
 \tag{27.3}
\]

Indeed every completed wreath contains \(N=2r+1\) middle vertices, so

\[
 N|\mathcal P|
 =\sum_T\sum_I\Pr(T\hbox{ lies in the completion of }I)
 \le (O_A(1)+4)\binom Nr.
\]

Compatibility in (27.1)--(27.2) means that the entire simple omitted-label
word alternates across \((T,T^c)\).  Equivalently, the two PBBS owner
parities form oppositely directed unit-slope staircases in
\(h_T(Y)=|T\cap Y|\).  Generic Johnson-level or bounded-endpoint-degree
counting still loses one factor \(\sqrt r\); the unresolved assertion is
PBBS-specific suppression of these long perfectly alternating staircases.
The exact kernel and its independent audit are recorded in
PBBS_SIMPLE_SECTOR_AMBIENT_COMPLETION_KERNEL_20260725.md and
PBBS_OPEN_WREATH_COMPLETION_CONGESTION_GATE_20260725.md.


<!-- END COMPLETE SOURCE 19 -->


---

<a id="document-20"></a>

## Document 20: PBBS_PEAK_DELETION_PASSAGE_RECURSION_20260725.md

Source: `/Users/amir.nuriyev/Documents/problem/PBBS_PEAK_DELETION_PASSAGE_RECURSION_20260725.md`

[Portable document](sources/essential/project/PBBS_PEAK_DELETION_PASSAGE_RECURSION_20260725.md) · [Exact original](originals/project/PBBS_PEAK_DELETION_PASSAGE_RECURSION_20260725.md)

<!-- BEGIN COMPLETE SOURCE 20 -->

# Peak deletion reduces PBBS returns to decorated shorter returns

Date: 2026-07-25

No computation or external input is used.

## 0. Outcome

Let \(D\) be a Dyck root of semilength \(r\), and let
\(\partial D\) be the Dyck root obtained by simultaneous peak deletion.
The exact equality-particle theorem gives a useful recursion.  A physical
return prunes to a genuinely shorter physical return in the particle PBBS,
with an additional prescribed continuation:

\[
 \boxed{\text{physical short return}
        \longrightarrow
        \text{shorter particle return followed by its predecessor}.}
\]

For a fixed pruned core the inverse peak-deletion fibre is counted exactly
below.  The resulting formula shows:

1. the return counts satisfy a recursive upper bound through smaller PBBS
   systems;
2. the sharp recursion retains a continuation condition after the smaller
   return; discarding it recovers only the bounded-height estimate;
3. using no information about those returns gives exactly the Catalan
   count back, with no saving;
4. even imposing literal adjacency of the two relevant equality particles
   removes only a constant fraction of a typical inverse fibre, not an
   extra factor \(1/r\).

Thus repeated pruning does not by itself prove the fixed-window residence
gate.  The missing quantitative input is a genuine decorated-return or
phase-clustering estimate.

## 1. Return and passage classes

Let \(\mathcal R_g(r)\) be the set of semilength-\(r\) Dyck roots which,
in some (equivalently every) spatial lift, start a consecutive omitted-label
return of gap at most \(g<2r+1\).

For a semilength-\(d\) PBBS root \(E\), label its particle coordinates
persistently in cyclic order.  Let \(\mathcal A_g(d)\) be the set of roots
for which, during the first \(g\) PBBS updates, there are a coordinate
\(a\) and times

\[
 0<h<t\le g
\]

such that the selected particle identities are

\[
 \kappa_0=a,\qquad \kappa_h=a,qquad \kappa_t=a-1,
 \tag{1.1}
\]

where \(a-1\) is the immediate cyclic predecessor of \(a\), and \(h\) is
the first positive reoccurrence time of \(a\).  Thus

\[
 \mathcal A_g(d)\subseteq\mathcal R_{g-2}(d),       \tag{1.2a}
\]

and (1.1) records the extra continuation from that shorter return to the
predecessor coordinate.  Call this a decorated short return.  Refine by
the number of leaves (peaks):

\[
 A_g(d,k)=\#\{E\in\mathcal A_g(d):\operatorname{pk}(E)=k\}.
 \tag{1.2}
\]

### Lemma 1.1 (exact decorated return under pruning)

If \(D\in\mathcal R_g(r)\), then

\[
 \boxed{\partial D\in\mathcal A_g(d)
        \subseteq\mathcal R_{g-2}(d)},
 \qquad d=r-\operatorname{pk}(D).                  \tag{1.3}
\]

#### Proof

Use the equality-particle dynamics of Theorem 14.1 in
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`.  At the first occurrence
of the returned physical label, one equality particle \(a\) enters its
edge.  Before that same edge can be entered again, particle \(a\) must be
selected once more and vacate it.  Let \(h\) be its first subsequent
selection time.  In the recorded particle word, coordinate \(a\) is
therefore the omitted label at times zero and \(h\), with no intervening
occurrence: this is a genuine consecutive omitted-coordinate return in the
smaller PBBS system.  Same-label gaps are odd; gap one would repeat a
factor state, and the final predecessor entry needs at least two further
updates.  Hence \(h\le g-2\).  Equality particles never overtake, so the
particle making the final entry is the immediate predecessor \(a-1\).
The recorded equality-particle word evolves by the canonical PBBS map and
is precisely \(0\partial D\).  This proves (1.1)--(1.3). \(\square\)

The distinction between \(\mathcal R\) and \(\mathcal A\) is still
essential: \(\mathcal A_g\) remembers which coordinate is selected after
the shorter return.  Dropping that continuation gives a valid recursive
upper bound, but loses exactly the information absent from the height-only
argument.

## 2. Exact inverse peak-deletion fibres

Fix a plane tree \(E\) with \(d\ge1\) edges and \(k\) leaves.  A tree
\(D\) satisfies \(\partial D=E\) precisely when new leaf children are
inserted in the ordered child slots of the \(d+1\) vertices of \(E\), with
at least one new child at each old leaf.  The total number of slots is

\[
 \sum_{v\in E}(\deg^+(v)+1)=2d+1.                  \tag{2.1}
\]

If \(D\) has \(r\) edges, then \(r-d\) leaves were added.  After assigning
one compulsory new leaf to each of the \(k\) old leaves, the remaining
\(r-d-k\) leaves are distributed freely among the \(2d+1\) slots.

### Lemma 2.1 (exact fibre size)

For \(r\ge d+k\),

\[
 \boxed{
 \#\{D:|D|=2r,\ \partial D=E\}
 =\binom{r+d-k}{2d}.}                              \tag{2.2}
\]

If one specified noncompulsory slot is required to receive no new leaf,
then the number is

\[
 \boxed{\binom{r+d-k-1}{2d-1}.}                   \tag{2.3}
\]

The ratio of (2.3) to (2.2) is exactly

\[
 \boxed{\frac{2d}{r+d-k}.}                        \tag{2.4}
\]

#### Proof

After the compulsory assignments, stars and bars in \(2d+1\) boxes gives

\[
 \binom{(r-d-k)+(2d+1)-1}{(2d+1)-1}
 =\binom{r+d-k}{2d}.
\]

Forbidding one box leaves \(2d\) boxes and gives (2.3).  Dividing the two
binomial coefficients gives (2.4). \(\square\)

The terminal adjacency used in the exact gap-seven classification is one
instance of (2.3): it forbids new leaves in the final root slot.  Formula
(2.4) is the exact price of that constraint.

## 3. The rigorous return-to-passage recurrence

Lemma 1.1 and the fibre partition give immediately:

### Theorem 3.1 (peak-deletion passage bound)

For every \(g<2r+1\),

\[
 \boxed{
 |\mathcal R_g(r)|
 \le
 \sum_{d=1}^{r-1}\sum_{k=1}^{d}
 A_g(d,k)\binom{r+d-k}{2d}.}                       \tag{3.1}
\]

Writing

\[
 R_{g-2}(d,k)
 =\#\{E\in\mathcal R_{g-2}(d):\operatorname{pk}(E)=k\},
\]

the inclusion in Lemma 1.1 gives the closed coarse recursion

\[
 \boxed{
 |\mathcal R_g(r)|
 \le
 \sum_{d=1}^{r-1}\sum_{k=1}^{d}
 R_{g-2}(d,k)\binom{r+d-k}{2d}.}                   \tag{3.2}
\]

If a specified empty-slot condition is separately proved necessary for a
subclass of returns, its contribution is bounded instead by

\[
 \sum_{d,k}A_g(d,k)\binom{r+d-k-1}{2d-1}.          \tag{3.3}
\]

#### Proof

Partition \(\mathcal R_g(r)\) by the pruned root
\(E=\partial D\).  Lemma 1.1 restricts \(E\) to
\(\mathcal A_g(d)\), and Lemma 2.1 counts its complete inverse fibre.
Summing proves (3.1).  Lemma 1.1 and
\(A_g(d,k)\le R_{g-2}(d,k)\) give (3.2).  If one slot is forbidden, use
(2.3) instead. \(\square\)

## 4. Why pruning alone gives no asymptotic saving

If the return/continuation condition is discarded, replace \(A_g(d,k)\) by the
Narayana number counting all \(d\)-edge plane trees with \(k\) leaves.
Then the right side of (3.1) is exactly

\[
 \operatorname{Cat}_r-1,                           \tag{4.1}
\]

because every \(r\)-edge plane tree other than the root with \(r\) leaf
children has one unique nonempty pruned core.  Adding that single omitted
tree gives \(\operatorname{Cat}_r\).
Thus an unquantified pruning statement recovers the full
Catalan space and nothing less.

Nor does a single literal adjacency supply the desired \(1/r\).  On the
bulk regime \(d=\Theta(r)\) and \(k=\Theta(d)\), formula (2.4) is bounded
away from zero.  For example, at the central profile

\[
 d=\frac r2+O(1),\qquad k=\frac d2+O(1),
\]

the ratio tends to

\[
 \frac{2(r/2)}{r+r/2-r/4}=\frac45.                 \tag{4.2}
\]

So an empty terminal slot removes only one fifth of a typical inverse
fibre.  The hoped-for factor \(1/r\) must come from the *dynamics of the
decorated continuation* in (1.1), or from a sharp use of the smaller-return
distribution in (3.2), not from inverse peak deletion or terminal adjacency
by itself.

## 5. Exact quantitative target left by the recursion

For total-root counting to imply the fixed-window residence packing gate at

\[
 g\le2A\sqrt r+1,
\]

it is enough to prove

\[
 \boxed{
 \sum_{d,k}A_g(d,k)\binom{r+d-k}{2d}
 =o_A\!\left(\frac{\operatorname{Cat}_r}{2r+1}\right).}
                                                               \tag{5.1}
\]

Indeed every quotient return root has \(2r+1\) spatial lifts, so (5.1)
makes the *total* physical number of short returns \(o_A(\operatorname{Cat}_r)\),
and hence makes their maximum edge-disjoint packing little-oh Catalan.

Condition (5.1) is stronger than necessary because packing may exploit
clustering.  Its value is that it identifies the precise missing
probability scale: after averaging through the inverse-fibre kernel, a
Gaussian-window decorated return must occur with probability
\(o_A(1/r)\).  Peak deletion supplies the kernel exactly, but it supplies
no such passage probability bound.

The next genuinely new theorem in this lane must therefore control the
short selected-coordinate pattern

\[
 a,\ldots,a,\ldots,a-1
\]

inside the canonical PBBS quotient, or use phase clustering to prove the
weaker packing estimate directly.

## 6. Every return branches into two shorter returns after pruning

There is more structure in the continuation than was used in (3.2).
Assume throughout this section that the original gap (t) is less than the
physical circumference (2r+1), as it is in every fixed Gaussian window
for all sufficiently large (r).

Let (a=kappa_0) be the equality particle which enters the returned
physical edge at time zero, and let (b=a-1) be its immediate predecessor.
Choose integer lifts of the particle positions preserving cyclic order, as
in Theorem 14.1, and put

\[
 \Delta=x_a(0)-x_b(0)\ge1.                         \tag{6.1}
\]

### Lemma 6.1 (two-child return lemma)

If the original omitted label returns for the first time at time (t),
then in the pruned PBBS:

1. coordinate (a) has a consecutive return on an interval
   ([0,h]) with (0<h<t);
2. coordinate (b) is selected exactly (Delta+1) times in
   ([0,t]), including time (t), and therefore supplies (Delta)
   consecutive return intervals wholly contained in ([0,t]).

In particular the pruned root contains at least two distinct shorter
return occurrences, one labelled (a) and one labelled (b).

#### Proof

At time zero, (14.4) gives

\[
 \lambda_0=x_a(0)+1=:u,
\]

and the update moves particle (a) from (u-1) into (u).  Before (u)
can be entered again, (a) must be selected and move out.  Let (h>0) be
its first subsequent selection.  Then (kappa_0=kappa_h=a), with no
intermediate (a), so ([0,h]) is a consecutive omitted-coordinate
return in the particle PBBS.  Since the final entrant is a different
particle, (h<t).

At the final return, Corollary 14.2 gives (kappa_t=b), and

\[
 \lambda_t=x_b(t)+1=u.
\]

Thus, immediately before the time-(t) update,

\[
 x_b(t)=u-1=x_a(0).                                 \tag{6.2}
\]

Every selection of (b) increases its integer-lifted position by exactly
one, and no other update changes it.  Because (t<2r+1), no particle can
make a full physical circuit inside the interval, so (6.1)--(6.2) imply
that (b) was selected exactly (Delta) times before time (t), and once
more at time (t).  Consecutive selection times of the same coordinate are
consecutive omitted-coordinate returns in the particle PBBS.  Hence the
(Delta+1) selections yield (Delta) such return intervals.  Since
(a\ne b), at least one is distinct from the (a)-return. \(\square\)

### Lemma 6.2 (exact terminal inverse-slot spacing)

Normalize the state as \(0D\), and write the nonempty pruned core as
\(E=e_1\cdots e_{2d}\).  In the plane-tree inverse construction of
Section 2, let \(z\) be the number of free new leaf peaks placed in the
terminal root corner, after the last core letter \(e_{2d}\).  Then

\[
 \boxed{\Delta=2z+1.}                               \tag{6.3}
\]

In particular (z=0) is precisely the physically adjacent case, while
(z\ge1) forces at least four shorter return occurrences in the pruned
window: the (a)-return and at least three (b)-returns.

#### Proof

Every inverse expansion has the unique contour form

\[
 D=(10)^{z_0}e_1(10)^{z_1}\cdots
   e_{2d}(10)^{z_{2d}}.
\]

The relevant variable is \(z=z_{2d}\).  Since every nonempty Dyck word
ends in zero, the physical segment from the last core letter to the leading
unmatched zero is

\[
 0(10)^z0.
\]

The equality edge entering the first zero is particle \(b\); the equality
edge entering the final zero is the distinguished particle \(a\); and all
intermediate edges alternate.  Their lifted edge coordinates are therefore
separated by exactly \(2z+1\).  Lemma 6.1 then gives \(2z+1\)
predecessor-return intervals plus the leader return, hence at least
\(2z+2\) child occurrences. \(\square\)

The terminal root corner is always noncompulsory for a nonempty core.
For a fixed core \(E\), the \(z=0\) part of its inverse fibre is exactly
(2.3), while the \(z\ge1\) part is the difference between (2.2) and (2.3).
Thus every parent return obeys the exact dichotomy

\[
\begin{array}{c|c|c}
\text{inverse slot}&\text{fibre fraction}&
   \text{short returns forced in the core window}\\ \hline
z=0&\displaystyle {2d\over r+d-k}&\ge2\\[2mm]
z\ge1&\displaystyle 1-{2d\over r+d-k}&\ge4.
\end{array}                                         \tag{6.4}
\]

More precisely, fixing the terminal occupancy to equal \(z\) leaves

\[
 \binom{r+d-k-z-1}{2d-1}
\]

inverse expansions.  Thus the dynamics prescribes an exact Pascal slot,
not merely the alternatives \(z=0\) and \(z\ge1\).

This is a genuine branching constraint, not merely the height bound.
However, it is not yet a Catalan estimate.  Distinct parent preimages of one
core can induce the same child return occurrences, and descendant branches
from the same time window can merge after further pruning.  A proof of
\((\mathrm{RP}_A)\) must quantify that merging, or show that repeated
selection of the (z=0) branch has sufficiently small inverse-fibre mass.

## 7. Two endpoint chains survive repeated pruning

Although the full binary descendant family can merge, two canonical
lineages cannot: always take the leader child at the left endpoint and the
predecessor child at the right endpoint.

Let an original return occupy the PBBS time interval $[0,t]$.  Define the
pruning tower

\[
 D^{(0)}=D,\qquad D^{(j+1)}=\partial D^{(j)},
 \qquad r_j=\tfrac12|D^{(j)}|.                     \tag{7.1}
\]

Peak defect, and hence $r_{j+1}$, is constant along the whole PBBS orbit
of $D^{(j)}$, because the equality particles persist.  Thus pruning
commutes with following the time interval $[0,t]$ in the sense supplied by
Theorem 14.1.

### Theorem 7.1 (two-sided endpoint return chains)

For every $j\ge1$ for which

\[
 2r_{j-1}+1>t,                                      \tag{7.2}
\]

the level-$j$ PBBS contains two distinct consecutive omitted-coordinate
returns

\[
 I_j^L=[0,h_j],\qquad I_j^R=[s_j,t],               \tag{7.3}
\]

with

\[
 0<h_j<t,\qquad0<s_j<t.                            \tag{7.4}
\]

Moreover the left gaps and right gaps each drop by at least two at every
further pruning step on which (7.2) remains valid.

#### Proof

At level zero use the given parent return.  Apply Lemma 6.1.  Its leader
child is a consecutive return beginning at time zero; call it $I_1^L$.
Its predecessor child has a last consecutive return ending at time $t$;
call it $I_1^R$.  They have different coordinate labels, so they are
distinct.

Now apply the same construction to $I_j^L$, always retaining its leader
child.  Because the child return is strictly shorter and has the same left
endpoint, this gives $I_{j+1}^L=[0,h_{j+1}]$ with
$h_{j+1}\le h_j-2$.  Apply the construction to $I_j^R$ and retain its
last predecessor child.  It has the same right endpoint and strictly
shorter odd gap, so $I_{j+1}^R=[s_{j+1},t]$ with
$t-s_{j+1}\le t-s_j-2$.

Condition (7.2) is exactly what permits the order-preserving integer lift
used in Lemma 6.1 at level $j-1$.  The equality-particle renormalization
identifies the level-$(j+1)$ time evolution with the PBBS evolution of
$D^{(j+1)}$, completing the induction. \(\square\)

The two lineages in (7.3) are endpoint-anchored, so no child-merging
argument can identify them with one another.  Full binary growth is not
claimed: interior descendants from different branches may coincide.

This gives a sharper necessary class than bounded height.  Define
$\mathcal B_g(r)$ to consist of roots whose entire pruning tower, through
the first level reached from a core of circumference greater than $g$,
carries the two endpoint chains (7.3).
Then

\[
 \boxed{\mathcal R_g(r)\subseteq\mathcal B_g(r).}  \tag{7.5}
\]

A Catalan estimate

\[
 |\mathcal B_{2A\sqrt r+1}(r)|
 =o_A\!\left(\frac{\operatorname{Cat}_r}{r}\right) \tag{7.6}
\]

would prove the total-root form of $\mathrm{RP}_A$.  Unlike the one-sided
height constraint, (7.5) simultaneously constrains both temporal endpoints
at every surviving pruning level.  Establishing (7.6), or finding a
Catalan-scale counterfamily inside $\mathcal B_g(r)$, is now the precise
iterated-core problem.


<!-- END COMPLETE SOURCE 20 -->


---

<a id="document-21"></a>

## Document 21: PBBS_PEAK_SPACING_AUDIT_20260725.md

Source: `/Users/amir.nuriyev/Documents/problem/PBBS_PEAK_SPACING_AUDIT_20260725.md`

[Portable document](sources/essential/project/PBBS_PEAK_SPACING_AUDIT_20260725.md) · [Exact original](originals/project/PBBS_PEAK_SPACING_AUDIT_20260725.md)

<!-- BEGIN COMPLETE SOURCE 21 -->

# Exact audit of the inverse peak-spacing identity

Date: 2026-07-25

No computation or external input is used.

## 1. Outcome

The candidate identity

\[
\Delta=2z+1
\]

is correct, provided that \(z\) is identified precisely: it is the number
of newly inserted leaf peaks in the **terminal root corner** of the
normalized pruned plane tree.  In particular, for every nonempty pruned
core this corner is noncompulsory.  The alternative in which the
distinguished corner is an old-leaf corner cannot occur in this application.

More is true.  For a fixed pruned core, the terminal occupancy required by
a physical return is determined exactly by the equality-particle itinerary.
This gives an exact fixed-occupancy fibre formula and an exact return kernel.
It also shows the limitation of the spacing identity by itself: occupancy
zero may have fibre ratio one, so there is no uniform entropy loss at one
pruning step.  Any iterative gain must use the correlation between the
prescribed occupancies and the successive PBBS itineraries.

## 2. Contour expansion of an inverse peak-deletion fibre

Let

\[
E=e_1e_2\cdots e_{2d}
\]

be a nonempty Dyck word.  Its plane tree has \(2d+1\) ordered child
corners.  In contour-word coordinates these are exactly the gaps before,
between, and after the letters of \(E\).  Consequently every Dyck word
\(D\) with \(\partial D=E\) has a unique expression

\[
\boxed{
D=(10)^{z_0}e_1(10)^{z_1}e_2\cdots
e_{2d}(10)^{z_{2d}} .}
\tag{2.1}
\]

Here every \(z_i\) is nonnegative, and

\[
z_i\ge 1
\quad\hbox{whenever the gap }(e_i,e_{i+1})
\hbox{ is a peak }10.
\tag{2.2}
\]

There are no other lower bounds.  In particular, the terminal variable

\[
z_\infty:=z_{2d}
\tag{2.3}
\]

is unconstrained, because it is the child corner of the root after its last
old child.  It is not the corner of an old leaf.

To prove (2.1), observe that adding one leaf child in a specified plane-tree
corner inserts one contour peak \(10\) in the corresponding word gap.
Conversely, every peak deleted by \(\partial\) is such a newly inserted leaf.
An old leaf of the core has one child corner, and at least one leaf must be
inserted there to prevent the old peak of \(E\) itself from being deleted;
this gives exactly (2.2).

## 3. The spacing identity

Normalize the original cyclic PBBS state as \(0D\), with the leading zero
the unique unmatched coordinate.  Let \(a\) be the distinguished equality
particle immediately before that zero, and let \(b=a-1\) be its immediate
cyclic predecessor.  Choose order-preserving integer lifts of their physical
edge positions and put

\[
\Delta=x_a(0)-x_b(0).
\tag{3.1}
\]

### Theorem 3.1 (exact terminal spacing)

With \(z_\infty\) as in (2.3),

\[
\boxed{\Delta=2z_\infty+1.}
\tag{3.2}
\]

#### Proof

Every nonempty Dyck word ends in zero.  In the expanded word (2.1), the
physical segment from the last core letter \(e_{2d}=0\) to the leading
unmatched zero is

\[
0(10)^{z_\infty}0.
\tag{3.3}
\]

The edge entering the first zero in (3.3) is an equality edge.  Indeed, if
the preceding core gap is not expanded, then the preceding core letter is
zero; if it is a core peak, its compulsory inserted block ends in zero.
This equality edge is particle \(b\).

Inside the open segment following that edge, all successive bit pairs
alternate.  The only next equality edge is the final \(00\)-edge entering
the leading unmatched zero, namely particle \(a\).  Their destination-edge
coordinates are separated by the \(2z_\infty\) inserted sites and one final
step.  Hence their lifted separation is \(2z_\infty+1\).  \(\square\)

Thus the ``adjacent'' case is exactly \(z_\infty=0\).  It is also exactly
the word condition that \(D\) ends in \(00\), in agreement with the
gap-seven classification.

## 4. Exact fixed-occupancy fibre

Let the core \(E\) have \(d\) edges and \(k\) leaves, and let the parent
have \(r\) edges.  Put

\[
L=r-d-k,
\qquad
M=L+2d=r+d-k.
\tag{4.1}
\]

After the \(k\) compulsory insertions, \(L\) free leaves are distributed
among \(2d+1\) corners.  Since the terminal root corner is noncompulsory,
fixing \(z_\infty=z\) gives

\[
\boxed{
F_{r,z}(E)=
\binom{r+d-k-z-1}{2d-1}
=\binom{M-z-1}{2d-1}}
\tag{4.2}
\]

for \(0\le z\le L\), and zero otherwise.  Relative to the full fibre

\[
F_r(E)=\binom{M}{2d},
\tag{4.3}
\]

the exact mass is

\[
\boxed{
\frac{F_{r,z}(E)}{F_r(E)}
=\frac{2d}{M}
\prod_{j=0}^{z-1}\frac{L-j}{M-1-j}.}
\tag{4.4}
\]

Equivalently, the exact tail is

\[
\boxed{
\Pr_E(z_\infty\ge s)
=\frac{\binom{M-s}{2d}}{\binom{M}{2d}}
=\prod_{j=0}^{s-1}\frac{L-j}{M-j}.}
\tag{4.5}
\]

Formula (4.2) is stars and bars after fixing one of the \(2d+1\) free
coordinates.  Formulae (4.4)--(4.5) follow by division.

The case \(z=0\) recovers

\[
\frac{F_{r,0}(E)}{F_r(E)}=\frac{2d}{r+d-k}.
\tag{4.6}
\]

There is no uniform contraction here: (4.6) equals one whenever
\(r=d+k\), that is, whenever every inserted leaf is compulsory.

## 5. Exact matching with the particle itinerary

Let \(\kappa_t(E)\) be the omitted-coordinate itinerary of the pruned PBBS,
labelled so that \(\kappa_0=a\), and put \(b=a-1\).  Define

\[
h(E)=\min\{t>0:\kappa_t(E)=a\},
\tag{5.1}
\]

and let \(T_j(E)\) be the time of the \(j\)-th occurrence of \(b\) after
time zero.

There is a useful universal ordering fact:

\[
\boxed{h(E)<T_2(E).}
\tag{5.2}
\]

Indeed, take any inverse expansion with terminal occupancy zero.  Such an
expansion always exists because the terminal root corner is noncompulsory.
After the time-zero move, the first selection of \(b\) moves it into the
old edge of \(a\).  A second selection of \(b\) cannot occur while \(a\)
still occupies the next edge.  Since equality particles never collide or
overtake, \(a\) must first be selected and vacate that edge.  The particle
itinerary depends only on \(E\), so (5.2) holds independently of the chosen
inverse expansion.

For \(g<2r+1\), set

\[
\mathcal Z_g(E)=
\{z\ge0:T_{2z+2}(E)\le g\}.
\tag{5.3}
\]

### Theorem 5.1 (exact return-occupancy criterion)

An inverse expansion \(D\) of \(E\), with terminal occupancy
\(z_\infty=z\), starts a consecutive physical omitted-label return by time
\(g\) if and only if

\[
\boxed{z\in\mathcal Z_g(E).}
\tag{5.4}
\]

The return time is then exactly \(T_{2z+2}(E)\).

#### Proof

At time zero particle \(a\) enters the returned edge.  It vacates that edge
at time \(h(E)\).  By order preservation, the next possible entrant is
\(b\).  If its initial lifted distance is \(\Delta\), then it must be
selected \(\Delta\) times before reaching the edge immediately behind the
target, and its next selection enters the target.  Thus the return time is
the \((\Delta+1)\)-st selection of \(b\).  Theorem 3.1 gives
\(\Delta+1=2z+2\).  By (5.2), the target has already been vacated before
\(T_{2z+2}(E)\).  Since \(g<2r+1\), particle \(a\) cannot
make a full physical circuit, and no other particle can overtake \(b\).
Therefore this entrance is the first repeated occurrence of the physical
label.  The converse is the same argument read backwards.  \(\square\)

Consequently the former passage upper bound can be sharpened to the exact
kernel

\[
\boxed{
|\mathcal R_g(r)|
=\sum_{d=1}^{r-1}\ \sum_{E\in\mathcal D_d}
  \sum_{\substack{z\in\mathcal Z_g(E)\\z\le r-d-\operatorname{pk}(E)}}
  \binom{r+d-\operatorname{pk}(E)-z-1}{2d-1}.}
\tag{5.5}
\]

The case \(d=0\) contributes nothing when \(g<2r+1\), because its unique
equality particle needs a full physical circuit to return.

The allowed occupancies form an initial interval.  If

\[
B_g(E)=\#\{1\le t\le g:\kappa_t(E)=b\},
\qquad
s_g(E)=\left\lfloor\frac{B_g(E)}2\right\rfloor-1,
\tag{5.6}
\]

then \(\mathcal Z_g(E)=\{0,1,\ldots,s_g(E)\}\), with the convention that
this set is empty when \(s_g(E)<0\).  Hence the contribution of a fixed
core can also be written exactly as

\[
\boxed{
F_r(E)-\binom{M-s-1}{2d},
\qquad s=\min\{L,s_g(E)\},}
\tag{5.7}
\]

when \(s_g(E)\ge0\), and as zero otherwise.  This is the hockey-stick sum
of (4.2).

## 6. What this does and does not give iteratively

Equation (5.5) is a genuine strengthening: the inverse terminal occupancy
is not merely empty or nonempty; it must match one exact odd passage count
in the smaller PBBS.  Nevertheless no one-step \(1/r\) saving follows.
The largest term is usually \(z=0\), its mass is (4.6), and that mass can
even be one.

There is a clean exact interpretation of repeated \(z=0\).  In a plane
tree, terminal occupancy zero means that the root's rightmost child is not
a newly deleted leaf.  Requiring terminal occupancy zero for \(J\)
successive pruning levels is equivalent to requiring the rightmost root-to-
leaf branch to have at least \(J+1\) edges.  The number of \(r\)-edge plane
trees with rightmost branch length at least \(s\) is

\[
\boxed{
T_{r,s}=[x^{r-s}]C(x)^{s+1}
=\frac{s+1}{2r-s+1}\binom{2r-s+1}{r-s}.}
\tag{6.1}
\]

Indeed an arbitrary prefix forest may precede each distinguished rightmost
spine child, giving the generating function

\[
(xC(x))^s C(x).
\tag{6.2}
\]

Uniformly for \(s=o(\sqrt r)\),

\[
\frac{T_{r,s}}{\operatorname{Cat}_r}
=(1+o(1))(s+1)2^{-s}.
\tag{6.3}
\]

Thus a long all-zero occupancy lineage does carry real entropy.  But this is
not yet a bound for returns: positive occupancies are allowed, and after
summing over all possible terminal profiles one recovers the entire class of
trees of the relevant height.  The exact gain can only come from showing
that the predecessor-selection count \(B_g(E)\) is usually too small to
capture the high-mass part of the kernel (4.4), or from using the two
endpoint lineages simultaneously.

In particular, the spacing identity alone does not establish an iterative
Catalan saving.  Its rigorous contribution is the exact arithmetic matching
(5.3)--(5.7), which is the correct starting point for such a proof.

## 7. Exact harmonic-tower obstruction to a seam-only induction

There is an even sharper reason that the identity alone cannot be iterated
as a product of empty-slot savings.  Let

\[
D_j=\partial^jD_0,
\qquad |D_j|=2r_j.
\tag{7.1}
\]

At the inverse step \(D_{j+1}\mapsto D_j\), the core \(D_{j+1}\) has

\[
\operatorname{pk}(D_{j+1})=r_{j+1}-r_{j+2}.
\tag{7.2}
\]

Therefore its full inverse fibre, conditional on the three ranks, has size

\[
\binom{r_j+r_{j+2}}{2r_{j+1}},
\tag{7.3}
\]

whereas the subfibre with terminal occupancy zero has size

\[
\binom{r_j+r_{j+2}-1}{2r_{j+1}-1}.
\tag{7.4}
\]

The exact conditional ratio is consequently

\[
\frac{2r_{j+1}}{r_j+r_{j+2}}.
\tag{7.5}
\]

Now choose an integer \(R\) divisible by \(1,2,\ldots,J+2\), and put

\[
r_j=\frac{R}{j+1}
\qquad(0\le j\le J+1).
\tag{7.6}
\]

All inverse free masses are nonnegative because

\[
r_j-2r_{j+1}+r_{j+2}
=\frac{2R}{(j+1)(j+2)(j+3)}>0,
\tag{7.7}
\]

and a bottom Dyck root with the required peak count exists.  Prescribing
terminal occupancy zero at every one of the \(J\) inverse levels retains
the exact fraction

\[
\begin{aligned}
\prod_{j=0}^{J-1}\frac{2r_{j+1}}{r_j+r_{j+2}}
&=\prod_{j=0}^{J-1}
  \frac{(j+1)(j+3)}{(j+2)^2}\\
&=\boxed{\frac{J+2}{2(J+1)}}
\longrightarrow\frac12.
\end{aligned}
\tag{7.8}
\]

The first two lower ranks are

\[
r_1=R/2,
\qquad r_2=R/3,
\tag{7.9}
\]

so the first inverse step lies at the critical Pascal saddle
\((d,k)=(R/2,R/6)\).

Thus even an unbounded tower of prescribed empty terminal seams need not
have vanishing **conditional fibre** mass.  This does not construct PBBS
passages on the harmonic tower, so it is not a counterexample to residence
packing.  It does prove that no argument multiplying only the spacing-slot
probabilities can close the theorem.  A successful iteration must use the
dynamical predecessor-passage condition in (5.6), or a capacity/clustering
statement coupling the two endpoint descendants.


<!-- END COMPLETE SOURCE 21 -->


---

<a id="document-22"></a>

## Document 22: PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md

Source: `/Users/amir.nuriyev/Documents/problem/PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md`

[Portable document](sources/essential/project/PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md) · [Exact original](originals/project/PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md)

<!-- BEGIN COMPLETE SOURCE 22 -->

# Audit: orbitwise coordinate homomesy for the periodic box-ball map

Date: 2026-07-24

## Verdict

The stated coordinate-homomesy theorem is **valid** for (0<N<L/2), and the
Kneser-cycle consequences stated with it are valid.  The theta-function proof
does cover repeated soliton amplitudes.  No unproved genericity or
distinct-amplitude assumption is being smuggled into the argument.

There is one bridge that should be stated in the manuscript rather than left
implicit: the cyclic parenthesis-flip map (f) is the periodic box-ball
evolution (T_l) for any carrier capacity (l) at least the largest soliton
amplitude (in particular, (l=N) suffices).  A short proof of this bridge is
included below.

The audit used the primary sources:

- A. Kuniba and R. Sakamoto, *Combinatorial Bethe ansatz and ultradiscrete
  Riemann theta function with rational characteristics*, arXiv:nlin/0611046v2.
- A. Merino, T. Mütze and Namrata, *Kneser graphs are Hamiltonian*,
  arXiv:2212.03918v4.
- J. Petr and P. Turek, *The wreath matrix*, arXiv:2501.07269v2.

This is a mathematical audit, not a bibliographic-priority determination.

## 1. Parenthesis flip equals the infinite-capacity PBBS evolution

Interpret a 1-bit as a ball and a 0-bit as an empty box.  Because (L>2N),
cyclic parenthesis matching pairs every 1 with a 0 and leaves (L-2N) zeroes
unmatched.

Choose a cyclic cut immediately after an unmatched zero.  Starting with an
empty carrier and scanning from this cut, pick up a ball at every 1 and, at a
0, drop a ball exactly when the carrier is nonempty.  The carrier load is the
usual parenthesis height.  Thus the zeroes at which a ball is dropped are
exactly the matched zeroes.  At the end of the scan the carrier is empty again.
Consequently the update changes every 1 to 0, every matched 0 to 1, and leaves
the unmatched zeroes unchanged: this is precisely the map (f).

The carrier never holds more than (N) balls, so capacity (l=N) is already
infinite for this state.  Both the periodic-carrier rule and (f) commute with
cyclic rotation, so the choice of the cut does not alter the resulting labelled
cyclic state.  This identifies (f) with (T_l) for (l\ge N), hence with the
flow denoted (T_\infty) in the theta-function argument.

## 2. The Kuniba--Sakamoto formula applies with repeated amplitudes

For a fixed action variable, let the distinct soliton amplitudes be indexed by
ℐ, with multiplicities (m_i\ge1).  In the notation of arXiv:nlin/0611046,

\[
 F_{ij}=\delta_{ij}p_i+2\min(i,j)m_j,
 \qquad M=\operatorname{diag}(m_i),
 \qquad \Omega=MF.
\]

The paper explicitly states that its Theorem 5.1 covers all states and extends
the earlier distinct-amplitude formula.  Repeated amplitudes enter through the
rational characteristics and the correction
χ\((s;\widetilde I)\).  Under (T_\infty), every rigging having amplitude
(i) is translated by the same amount (i).  Therefore all differences
(I_{i,\beta}-I_{i,\alpha}), and hence χ, are invariant.  Meanwhile the bundled
angle variable is translated by (M h_\infty).  Thus the time-dependent tau
function really has the form

\[
 \tau_t(j)=\max_{s\in\mathbb Z^g/M\mathbb Z^g}
 \left\{
 \Theta_{M^{-1}s}(z_{t,j})+\chi(s;\widetilde I)
 \right\},
 \quad
 z_{t,j}=I+M\left(t h_\infty-jh_1-\frac p2\right),
\]

and the state bit is

\[
 x_{j,t}=\tau_t(j)-\tau_t(j-1)-\tau_{t+1}(j)+\tau_{t+1}(j-1).
\]

No multiplicity-one hypothesis is used here.

## 3. The determinant translation is a genuine period

Let

\[
 D=\det F>0,
 \qquad u=\operatorname{adj}(F)h_\infty\in\mathbb Z^g.
\]

Then (Fu=Dh_\infty), and hence

\[
 z_{t+D,j}-z_{t,j}=DMh_\infty=MFu=\Omega u.
\]

Kuniba--Sakamoto's quasi-periodicity formula is, for any
(v\in\Omega\mathbb Z^g),

\[
 \Theta_a(z+v)=\Theta_a(z)+v^{\mathsf T}\Omega^{-1}
 \left(z+\frac v2\right).
\]

With (v=\Omega u), the additive term is

\[
 u^{\mathsf T}z+\frac12u^{\mathsf T}\Omega u,
\]

independent of the rational characteristic (a).  It therefore passes through
the maximum over characteristics, giving

\[
 \tau_{t+D}(j)-\tau_t(j)
 =u^{\mathsf T}z_{t,j}+\frac12u^{\mathsf T}\Omega u.
\]

The right-hand side is separately affine in (t) and (j).  Its mixed finite
difference vanishes, so the four-term tau formula gives
(x_{j,t+D}=x_{j,t}).  Therefore (D) is an orbit period.  (For the trivial
(N=0) state, homomesy is immediate and this action-variable discussion can be
omitted.)

## 4. Telescoping proves site homomesy

Summing the four-term expression from (t=0) through (D-1) gives

\[
\begin{aligned}
 S_j
 &=\sum_{t=0}^{D-1}x_{j,t}\\
 &=\tau_0(j)-\tau_0(j-1)-\tau_D(j)+\tau_D(j-1)\\
 &=u^{\mathsf T}(z_{0,j-1}-z_{0,j})
 =u^{\mathsf T}Mh_1,
\end{aligned}
\]

which is independent of (j).  Each of the (D) time slices has (N) balls,
so summing over the (L) sites yields

\[
 S_j=\frac{DN}{L}.
\]

If (P) is the fundamental period, then (P\mid D), and the first (D)
iterates are (D/P) repetitions of the fundamental orbit.  Dividing by
(D/P) proves

\[
 \sum_{t=0}^{P-1}(T^t x)_j=\frac{PN}{L}
\]

for every site (j).  Integrality is equivalent to

\[
 \frac{L}{\gcd(L,N)}\mid P.
\]

## 5. Three-state refinement

Every 1 is matched, so at any time there are exactly (N) matched ones.  A
site is a matched zero at time (t) exactly when it is occupied at time
(t+1).  Hence each site is a matched one and a matched zero exactly (PN/L)
times over a fundamental orbit.  The remaining count is

\[
 P-2\frac{PN}{L}=\frac{P(L-2N)}{L},
\]

which is the unmatched-zero count at that site.

## 6. Kneser-cycle consequences

Merino--Mütze--Namrata prove directly that (f) is invertible and that its
orbits form a cycle factor of (K(n,k)).  Adjacent supports are disjoint because
all old 1s are flipped to 0 and only matched zeroes become 1.

Put

\[
 g=\gcd(n,k),\qquad M_0=n/g,\qquad s=k/g.
\]

For a parenthesis orbit (C) of length (P), the theorem gives

\[
 M_0\mid P,
 \qquad P=\ell M_0,
 \qquad d_v(C)=Pk/n=\ell s
\]

for every ground point (v).  Thus every individual cycle is point-regular.
Summing its lengths over the cycle factor gives

\[
 \sum_C\ell_C=\frac1{M_0}\binom nk
 =\frac gn\binom nk,
\]

the number of wreaths required by a decomposition.

## 7. Critical-diagonal reconstruction is correct

Assume

\[
 n=(2s+1)g,\qquad k=sg,
\]

and let (A_0,A_1,\ldots,A_{2s}) be a point-regular
(C_{2s+1}) in (K(n,k)).  Point regularity forces every point to occur in
exactly (s) of the (A_i).

For a point (x), its occurrence positions are an independent (s)-set in
the odd cycle (C_{2s+1}).  Such an independent set has exactly one edge whose
two endpoints are both absent: its cyclic binary word has (s) isolated ones
and (s+1) zeroes, hence exactly one run of two zeroes and all other zero-runs
have length one.

Set

\[
 B_i=[n]\setminus(A_i\cup A_{i+1}).
\]

Every point lies in exactly one \(B_i\), and \(|B_i|=n-2k=g\), so the
(B_i) partition the ground set.  If (x\in B_j), its occurrence positions
must be

\[
 j+2,j+4,\ldots,j+2s.
\]

Consequently

\[
 A_i=B_{i-2}\cup B_{i-4}\cup\cdots\cup B_{i-2s}.
\]

Because multiplication by `-2` permutes `Z/(2s+1)Z`, put
`P_c=B_{-2c}`.  Writing `i=-2a`, the last display becomes

\[
 A_{-2a}=P_{a+1}\cup\cdots\cup P_{a+s}.
\]

Thus the family is precisely all cyclic windows of `s` consecutive
`g`-blocks.  This is an `(n,k)`-wreath under the Petr--Turek/Baranyai
definition (successive wreath starts advance by `k=sg`, i.e. by `s`
blocks, and `gcd(s,2s+1)=1`).

It follows in particular that every minimum-length parenthesis orbit on this
diagonal is a wreath.

## 8. Audited examples and scope

A light independent enumeration reproduces the stated parenthesis orbits

\[
 13,24,35,46,15,26
\]

at ((n,k)=(6,2)), and

\[
 135,246,357,468,157,268,137,248
\]

at ((8,3)).  It also reproduces exactly the claimed cycle-length set at
((13,6)):

\[
 13,39,65,91,117,273.
\]

The two examples correctly show that point regularity alone does not split a
long orbit into wreaths and does not characterize wreaths away from the
critical diagonal.  Therefore the proposed balanced inter-orbit switching step
is still genuinely missing, and the Wreath Conjecture is not proved by the
homomesy theorem.

One small expository issue remains: if the finite-capacity-(2) counterexample
is retained, the manuscript should name its initial state (or print the orbit),
so the displayed alternating occupation vector is reproducible from the note
itself.


<!-- END COMPLETE SOURCE 22 -->


---

<a id="document-23"></a>

## Document 23: MATH_THEOREM_PBBS_EXACT_RUN_SPECTRUM_FLAT_ANTECEDENT_NOGO_AND_FULL_UPPER_DECK_20260813.md

Source: `/Users/amir.nuriyev/Documents/problem/MATH_THEOREM_PBBS_EXACT_RUN_SPECTRUM_FLAT_ANTECEDENT_NOGO_AND_FULL_UPPER_DECK_20260813.md`

[Portable document](sources/essential/project/MATH_THEOREM_PBBS_EXACT_RUN_SPECTRUM_FLAT_ANTECEDENT_NOGO_AND_FULL_UPPER_DECK_20260813.md) · [Exact original](originals/project/MATH_THEOREM_PBBS_EXACT_RUN_SPECTRUM_FLAT_ANTECEDENT_NOGO_AND_FULL_UPPER_DECK_20260813.md)

<!-- BEGIN COMPLETE SOURCE 23 -->

# PBBS has a complete upper deck but no growing-depth flat antecedent: the exact run--return spectrum

**Date:** 2026-08-13  
**Status:** unconditional reduction from the audited PBBS return and flag
theorems.  The canonical PBBS owner factor covers every upper width, but its
minimum positive coordinate residence is exactly `3`.  Thus it cannot be
used unchanged as the depth-`d` full-aperture carrier when
`q=d+1>=4`.  The exact missing modification is a short-return-free,
flag-preserving rethreading, not an additional upper-shadow theorem.

## 0. Verdict

Put

\[
 n=2m+1,
 \qquad
 f:{[n]\choose m}\longrightarrow {[n]\choose m}
\]

for the canonical cyclic-parenthesis/PBBS permutation.  On an `f`-orbit
write

\[
 A_t=f^t(A_0),
 \qquad
 \lambda_t=[n]\setminus(A_t\cup A_{t+1}).          \tag{0.1}
\]

The complement-centered owner factor consists of the rank-`m+1` states

\[
 X_t=A_t^c
\]

with directed successor `t -> t+2`.  If an `f`-orbit is even this gives
two cycles; if it is odd it gives one.

The exact conclusions are:

1. If two consecutive occurrences of one omitted label have cyclic
   `f`-gap `g=2s+1`, they create exactly one positive coordinate run of
   length

   \[
   s+1={g+1\over2}                                  \tag{0.2}
   \]

   and exactly one zero run of length

   \[
   s={g-1\over2}                                    \tag{0.3}
   \]

   in the complete step-two owner factor.  Every nonconstant coordinate
   run arises uniquely this way.

2. PBBS has exactly

   \[
   n(m-1)                                           \tag{0.4}
   \]

   consecutive gap-five starts and exactly

   \[
   n(2^{m-1}-m)                                     \tag{0.5}
   \]

   consecutive gap-seven starts.  Hence the owner factor has exactly the
   same respective numbers of positive runs of lengths `3` and `4`.
   In particular its minimum positive run is exactly `3`; its minimum
   zero run is exactly `2`.

3. A cyclic set trace has a flat `q`-antecedent if and only if every
   proper positive coordinate run has length at least `q`.  Therefore the
   canonical PBBS owner chronology has no flat `q`-antecedent for any

   \[
   q\ge4.                                           \tag{0.6}
   \]

   This includes the target regime `q=d+1 asymp sqrt(m)`.

4. Nevertheless PBBS already covers the complete upper deck.  For every
   width `1<=w<=m+1`, every rank-`m+w` target occurs as the union of `w`
   consecutive complement-centered owners.  For `w>=2`, its number of
   correct-rank designated occurrences lies between

   \[
   1
   \quad\hbox{and}\quad
   {2w-1\choose w-1}.                              \tag{0.7}
   \]

Thus PBBS and the long-aperture MSW construction have complementary
strengths: PBBS has the complete all-width deck but fails growing
residence, while the MSW wreath chronology has flat growing residence but
does not automatically cover its second shadow.

## 1. Centered recurrence

Adjacent PBBS states are disjoint and omit one coordinate.  The standard
recurrence is

\[
 A_{t+2}
 =A_t\setminus\{\lambda_{t+1}\}\cup\{\lambda_t\}. \tag{1.1}
\]

After complementation,

\[
 \boxed{
 X_{t+2}
 =X_t\setminus\{\lambda_t\}\cup\{\lambda_{t+1}\}.}
                                                               \tag{1.2}
\]

Thus, on the step-two owner graph, `lambda_t` is deleted on the edge
starting at `X_t`, and it is inserted on the edge starting at `X_(t-1)`.

Fix a coordinate `x`.  Consecutive occurrences of `x` in the cyclic
omitted-label word have odd separation.  Indeed, `x` is absent at both
ends of an edge labelled `x`; at every intervening edge not labelled `x`,
its membership in the odd-graph state is complemented.  Returning to an
absent endpoint therefore requires an even number of ordinary flips, so
the edge-index gap is odd.  The audited PBBS no-gap-one/no-gap-three
theorems strengthen this to

\[
                         g\ge5.                    \tag{1.3}
\]

## 2. Exact run--return dictionary

### Theorem 2.1 (positive and zero spectra)

Let `lambda_t=lambda_(t+g)=x` be consecutive occurrences on a lifted
`f`-orbit, where `g=2s+1`.  Then:

* `x` is present on the step-two owner vertices

  \[
  X_{t+1},X_{t+3},\ldots,X_{t+g},                  \tag{2.1}
  \]

  a maximal positive run of `s+1=(g+1)/2` states;
* on the other step-two arc, `x` is absent on

  \[
  X_{t+2},X_{t+4},\ldots,X_{t+g-1},                \tag{2.2}
  \]

  a maximal zero run of `s=(g-1)/2` states.

As the coordinate, orbit, and consecutive return vary, (2.1) gives every
nonconstant positive run exactly once and (2.2) gives every nonconstant
zero run exactly once.

#### Proof

By (1.2), the occurrence at `t` inserts `x` on the edge

\[
 X_{t-1}\longrightarrow X_{t+1},                  \tag{2.3}
\]

whereas the next occurrence deletes it on

\[
 X_{t+g}\longrightarrow X_{t+g+2}.                \tag{2.4}
\]

There is no intervening occurrence of `x`, so no intervening transition
can toggle it.  This gives (2.1), whose number of terms is

\[
 {t+g-(t+1)\over2}+1={g+1\over2}.                 \tag{2.5}
\]

Starting instead immediately after the deletion at `t`, the coordinate
is absent until its insertion at `t+g`; the intervening vertices are
exactly (2.2), whose number is `(g-1)/2`.

Conversely, the left and right boundary transitions of any maximal
positive run are respectively an insertion and a deletion of its
coordinate.  Formula (1.2) labels both by consecutive occurrences of that
coordinate in the omitted-label word.  The same argument applies to a
zero run.  This proves both bijections. `square`

### Census check from componentwise homomesy

If the underlying `f`-orbit has length `L=ell*n`, componentwise PBBS
homomesy says that each coordinate occurs exactly `ell` times in its
omitted-label word.  If its consecutive gaps are `g_1,...,g_ell`, then

\[
 \sum_i g_i=L.                                     \tag{2.6}
\]

Theorem 2.1 gives total positive and zero occupation

\[
 \sum_i{g_i+1\over2}=\ell(m+1),
 \qquad
 \sum_i{g_i-1\over2}=\ell m,                       \tag{2.7}
\]

exactly the required site-homomesy counts for the rank-`m+1`
complemented owner trace.  This independently checks both off-by-one
terms in (0.2)--(0.3).

## 3. The first two exact spectral atoms

The audited PBBS return classification gives:

\[
 M_5=n(m-1),                                       \tag{3.1}
\]

because the normalized gap-five roots are exactly

\[
 D=(10)^a1(10)^b0,
 \qquad a\ge0, b\ge1, a+b=m-1,                  \tag{3.2}
\]

and each has `n` spatial phases.  The next exact return census is

\[
 M_7=n(2^{m-1}-m).                                 \tag{3.3}
\]

Applying Theorem 2.1 proves

\[
 \boxed{N_3^+=n(m-1),\qquad
        N_4^+=n(2^{m-1}-m).}                       \tag{3.4}
\]

Here `N_r^+` denotes the number of coordinate-labelled proper positive
runs of length `r` in the full complement-centered owner factor.  It also
gives `N_2^0=M_5`, where the superscript `0` denotes zero runs.

Equivalently, on the uncomplemented rank-`m` centered row the same
gap-five returns give exactly `n(m-1)` positive runs of length `2`.
Thus there is no ambiguity between the two possible middle-shore
conventions: the upper-middle rank-`m+1` owner trace has minimum positive
run `3`, while the lower-middle rank-`m` trace has minimum positive run
`2`.

The first equality in (3.4) proves that the minimum positive run is at
most three; (1.3) and (0.2) prove it is at least three.  The analogous
argument gives minimum zero run exactly two.

The gap-seven atom shows that the failure is not merely a fixed finite
exception.  Once `q>=5`, the canonical chronology contains at least

\[
 N_3^++N_4^+
 =n(2^{m-1}-1)                                     \tag{3.5}
\]

short positive runs.

### Corollary 3.1 (incidence distance from a flat trace)

For `q>=5`, let `Y` be any set trace on the same indexed slots which has
all proper positive coordinate runs of length at least `q`.  Then

\[
 \boxed{
 \sum_t|X_t\mathbin\triangle Y_t|
 \ge n(2^{m-1}-1).}                                \tag{3.6}
\]

#### Proof

For every positive run `R` of `X` of length three or four, adjoin the
immediately preceding and following zero states of the same coordinate.
The resulting coordinate-labelled collars are pairwise disjoint.  Indeed,
Theorem 2.1 and (1.3) say every intervening zero run has length at least
two, so the right collar point of one positive run differs from the left
collar point of the next.

If `Y` agreed with `X` throughout one such collar, `R` would remain an
isolated positive run of length less than `q` in `Y`.  Hence every collar
contains a changed incidence.  Disjointness and (3.5) prove (3.6).
`square`

This is an aligned-incidence obstruction.  A nonlocal permutation of the
owner chronology can move exponentially many incidences without changing
the owner sets, so (3.6) does not rule out rethreading.  It does rule out a
bounded local correction of the fixed PBBS chronology.

## 4. Exact flat-antecedent criterion

Let `T=(T_i)` be any cyclic set trace.  A **flat `q`-antecedent** is a
cyclic source trace `P=(P_i)` satisfying, up to a harmless index reversal,

\[
 T_i=\bigcup_{h=0}^{q-1}P_{i-h}.                   \tag{4.1}
\]

### Lemma 4.1 (binary dilation image)

A flat `q`-antecedent exists if and only if every proper nonempty positive
coordinate run of `T` has length at least `q`.

#### Proof

Work one coordinate at a time.  Every source occurrence `p_j=1` creates
`q` consecutive ones in the dilated trace (4.1).  Connected components of
a union of cyclic `q`-intervals therefore have length at least `q`, unless
they fill the whole cycle.

Conversely, define the coordinate of `P_i` to be one precisely when it is
present in all of

\[
 T_i,T_{i+1},\ldots,T_{i+q-1}.                     \tag{4.2}
\]

On a positive run of length `r>=q`, (4.2) is one on its first `r-q+1`
starts, and dilating these starts by (4.1) recovers the whole run.  It also
recovers constant-zero and constant-one traces.  Applying this independently
to every coordinate gives a set-valued antecedent. `square`

Combining Lemma 4.1 with Theorem 2.1 gives an exact PBBS criterion:

\[
 \boxed{
 \text{PBBS is flat at aperture }q
 \Longleftrightarrow
 \text{every consecutive omitted-label gap satisfies }g\ge2q-1.}
                                                               \tag{4.3}
\]

Since (3.1) supplies gap five, (4.3) fails for every `q>=4`.  Rotation,
reversal, and component rephasing preserve the cyclic run spectrum, so
none repairs the failure.  If dual residence is also required, (0.3)
shows that a gap `g` requires `g>=2q+1`; gap five already defeats dual
`q`-residence for `q>=3`.

## 5. The complete upper deck survives abstractly

The residence failure must not be confused with an upper-support failure.
The audited all-depth PBBS fan theorem states that for every
`0<=r<=m` and every

\[
 S\in{[n]\choose m-r},
\]

some directed step-two fan has

\[
 \bigcap_{j=0}^{r}A_{t+2j}=S,                     \tag{5.1}
\]

and its correct-rank load lies in

\[
 1\le\mu_r^-(S)\le {2r+1\choose r}.               \tag{5.2}
\]

### Theorem 5.1 (all-width upper support)

For every `1<=w<=m+1` and every

\[
 U\in{[n]\choose m+w},
\]

there is a width-`w` interval of complement-centered owners whose union is
exactly `U`.  For `w>=2`, the correct-rank occurrence load satisfies

\[
 \boxed{
 1\le\mu_w^{\rm up}(U)
 \le {2w-1\choose w-1}.}                           \tag{5.3}
\]

At `w=1`, every owner occurs exactly once.

#### Proof

Put `r=w-1` and `S=U^c`, so `|S|=m-r`.  Choose (5.1).  Then

\[
 \bigcup_{j=0}^{w-1}X_{t+2j}
 =[n]\setminus\bigcap_{j=0}^{r}A_{t+2j}
 =S^c=U.                                           \tag{5.4}
\]

Complementation is occurrence-preserving, so (5.2) becomes (5.3).
For `w=1`, complementation of the PBBS middle layer is an exact owner
factor. `square`

The theorem counts designated correct-rank windows.  Many other PBBS
windows have a repeated toggle and the wrong union rank.  Complete support
therefore does not imply the pointwise dilation identity required by a flat
source.

## 6. The precise PBBS modification now required

Let the target aperture be `q=d+1`.  On every untouched PBBS fragment,
(4.3) says that a growing-depth construction must intercept every
consecutive omitted-label return arc

\[
                         g\le2q-3.                 \tag{6.1}
\]

Cutting such arcs is not by itself sufficient: some upper targets in
Theorem 5.1 can have only one designated occurrence, so an arbitrary cut
can destroy their last witness.

The exact positive replacement theorem to seek is therefore the following.

### PBBS `q`-safe flag-rethreading problem

Rethread the exact multiset of complement-centered owners into Johnson
cycles or paths so that:

1. every owner is still used exactly once;
2. every proper positive coordinate run has length at least `q`;
3. for every width `w` and every required upper target `U`, at least one
   designated width-`w` union interval from Theorem 5.1 is retained, or a
   replacement interval with the same union is created;
4. every new seam satisfies the same run condition, rather than merely
   cutting the old short-return arcs.

Conditions 1--4 are precisely enough for the owner/upper part of the
full-aperture compiler.  Indeed, Lemma 4.1 gives the maximal source

\[
 P_i=\bigcap_{h=0}^{q-1}T_{i+h},                  \tag{6.2}
\]

and every letter in (6.2) has the required rank `m-q+2`.  To check the
rank, inspect any block of `q-1` Johnson transitions.  If a coordinate
inserted inside the block were deleted again inside the block, its new
positive run would have fewer than `q` owner states.  Hence no inserted
coordinate is deleted, all `q-1` deletion labels are distinct coordinates
of the initial owner, and the common intersection loses exactly `q-1`
coordinates from rank `m+1`.

Finally, any retained width-`w` owner union becomes a literal interval
union of `q+w-1` consecutive source letters.  Thus all of Theorem 5.1's
upper targets survive in one flat, fixed-rank source word.

Equivalently, a cut-and-sew proof needs a transversal of the PBBS return
arcs (6.1), together with a **flag-safe sewing theorem** which creates no
new short run and does not erase the last designated occurrence of any
upper target.  This is stronger than component fusion and stronger than a
return-packing estimate alone.

## 7. Consequence for the current architecture

The canonical PBBS factor cannot replace the full-aperture MSW factor
unchanged: its growing-depth antecedent fails already at `q=4`, and for
`q>=5` it is exponentially far from a flat trace in the aligned incidence
metric.  On the other hand, PBBS completely eliminates the abstract
all-width upper-support gate.

The sharp hybrid target is therefore:

\[
 \boxed{
 \text{transport PBBS's designated all-width fan bank through a
 `q`-safe rethreading.}}
                                                               \tag{7.1}
\]

If such transport is proved, the flat source and every upper width follow
formally from Lemma 4.1 and Theorem 5.1.  Without it, PBBS supplies an
excellent occurrence atlas but not the resident chronology required for
`B(k)+O(1)`.

## 8. Dependencies and audit boundary

The recurrence (1.1), odd-gap rule, componentwise homomesy, no-gap-three
theorem, gap-five census, and gap-seven census are proved and independently
audited in:

* `MATH_AUDIT_PBBS_FIRST_SHADOW_THEOREM_20260726.md`;
* `MATH_AUDIT_O_PBBS_CENTERED_Q2_CHRONOLOGY_AND_RETURN_GATE_20260726.md`;
* `PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`.

The all-depth fan support and load bound used in Section 5 are in:

* `MATH_THEOREM_PBBS_Q_FAN_SUPPORT_Q2_AND_GAUSSIAN_MULTIPLICITY_20260726.md`;
* `MATH_AUDIT_PBBS_ALL_DEPTH_FAN_AND_MULTIPLICITY_20260726.md`.

No claim is made here that the `q`-safe flag rethreading exists.  The note
proves the exact canonical no-go, preserves the positive all-upper theorem,
and isolates the modification which would turn the PBBS occurrence atlas
into a literal growing-depth carrier.


<!-- END COMPLETE SOURCE 23 -->


---

<a id="document-24"></a>

## Document 24: MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md

Source: `/Users/amir.nuriyev/Documents/problem/MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md`

[Portable document](sources/essential/project/MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md) · [Exact original](originals/project/MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md)

<!-- BEGIN COMPLETE SOURCE 24 -->

# Lane H: a linear PBBS crossing seam by a dominance staircase

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
web search is used.

## 0. Verdict

The one-cut literal fusion problem has a linear solution.  Let

\[
 X_{i+1}=X_i-\{r_i\}+\{a_i\}
\]

be a cyclic Johnson walk of rank \(m+1\), cut between \(X_{-1}\) and
\(X_0\).  If

\[
 2H\le m+1,
\tag{0.1}
\]

then one nonzero word of length

\[
 \boxed{4H-1}
\tag{0.2}
\]

represents every correct-rank lower intersection and every upper union of
at most \(H+1\) consecutive owners which crosses the cut.

The upper part is the literal owner segment of length \(2H\).  The lower
part has length \(2H-1\): attach to each coordinate its two positive-run
extents at the cut and follow a southeast lattice staircase through their
Pareto-minimal points.  Every correct lower target is the union of one
contiguous subpath of this staircase.

This is stronger than a zero-winding seam theorem: no PBBS return
classification is used.  In particular it is unaffected by the failure of
the proposed implication \(d(D)=1\Rightarrow g=2\operatorname{ht}(D)+1\)
recorded in `PBBS_ZERO_WINDING_CONVERSE_COUNTERAUDIT_20260725.md`.

For completeness, that motivating converse fails literally at semilength
five.  With \(N=11\), put

\[
 D_0=1110011000,\qquad
 D_1=1110001100,\qquad
 D_2=1100111000.
\tag{0.3}
\]

Direct first-maximum factorization gives

\[
 \tau D_0=D_1,\quad \tau D_1=D_2,\quad \tau D_2=D_0,
\]

and

\[
 (\delta(D_0),d(D_0))=(3,1),\quad
 (\delta(D_1),d(D_1))=(3,5),\quad
 (\delta(D_2),d(D_2))=(7,1).
\tag{0.4}
\]

Although \(D_0\) is primitive, has height three, and has \(d(D_0)=1\),
its three-step-two deficit sum is

\[
 1+5+1=7\not\equiv3=\delta(D_0)\pmod {11}.
\tag{0.5}
\]

The earlier two sums are \(1\ne3\) and \(6\ne7\), so there is no claimed
gap-seven return.  The failed sector proof overlooks an old right-spine
forest after that forest is transported to positive depth on the left: its
relative height is below the global height, but relative height plus its
new attachment depth can attain the global height first.  Nothing below
uses the false iteration.

For \(J\) cuts on a cyclic owner component of length \(\ell\), the exact
endpoint-erosion plus seam cost is

\[
 \boxed{\ell+(5H-1)J.}
\tag{0.6}
\]

Thus the old \(\Theta(H^2)\) singleton-repair toll per cut is removed.
The fixed-window packing statement \((RP_A)\) remains neither proved nor
disproved.  The linear seam nevertheless weakens the sufficient residence
hypothesis from little-oh Catalan packing to big-oh Catalan packing.  This
is proved in Section 9.  If instead a regime contains \(\Theta(W/H)\)
essential cuts, paying \(\Theta(H)\) independently at all of them is still
\(\Theta(W)\); there the surviving fallback is genuine cross-cut chart
sharing.

## 1. The crossing Pascal triangle

Put

\[
 C=X_{-1}\cap X_0.
\tag{1.1}
\]

Because the two owners are adjacent rank-\((m+1)\) sets,

\[
 |C|=m.
\tag{1.2}
\]

For \(1\le s,t\le H\), define

\[
 P_{s,t}=\bigcap_{i=-s}^{t-1}X_i.
\tag{1.3}
\]

This window contains \(s+t\) owners and \(s+t-1\) Johnson transitions.
Its floor rank is therefore

\[
 m+1-(s+t-1)=m+2-s-t.
\tag{1.4}
\]

We call \(P_{s,t}\) **floor-correct** when equality holds:

\[
 |P_{s,t}|=m+2-s-t.
\tag{1.5}
\]

Every intended correct lower mask crossing the cut and using at most
\(H+1\) owners is one of these queries, with

\[
 s+t-1\le H.
\tag{1.6}
\]

It is convenient, and costs nothing, to construct the chart for the whole
square \([H]^2\).

For \(x\in C\), define its capped left and right positive-run extents by

\[
 u_x=\max\{u\in[H]:x\in X_{-u}\cap\cdots\cap X_{-1}\},
\tag{1.7}
\]

\[
 v_x=\max\{v\in[H]:x\in X_0\cap\cdots\cap X_{v-1}\}.
\tag{1.8}
\]

Write

\[
 p_x=(u_x,v_x),\qquad
 \mathcal D=\{p_x:x\in C\}\subseteq[H]^2,
\tag{1.9}
\]

with multiplicities allowed.

### Lemma 1.1 (dominance formula)

For every \((s,t)\in[H]^2\),

\[
 \boxed{P_{s,t}=\{x\in C:u_x\ge s,\ v_x\ge t\}.}
\tag{1.10}
\]

#### Proof

The defining owner window contains \(X_{-1}\) and \(X_0\), so its
intersection is contained in \(C\).  A coordinate of \(C\) survives the
whole window precisely when its positive run through the cut reaches at
least \(s\) owners leftward and at least \(t\) owners rightward.  This is
exactly (1.10). \(\square\)

For \(s,t<H\), put

\[
 R_{s,t}=P_{s,t}\setminus(P_{s+1,t}\cup P_{s,t+1}).
\tag{1.11}
\]

By (1.10), \(R_{s,t}\) consists exactly of the coordinates with
\((u_x,v_x)=(s,t)\).  Hence the literal Pascal recurrence is

\[
 \boxed{P_{s,t}=P_{s+1,t}\cup R_{s,t}\cup P_{s,t+1}.}
\tag{1.12}
\]

The nonempty \(R_{s,t}\)'s are precisely the short-run pins which make
independent repair of all triangle cells quadratic.

## 2. Floor correctness gives southwest exclusion

### Lemma 2.1

If \(P_{s,t}\) is floor-correct, no extent point lies strictly southwest
of \((s,t)\):

\[
 \boxed{
 \nexists x\in C\quad u_x<s\text{ and }v_x<t.}
\tag{2.1}
\]

#### Proof

List the \(L=s+t\) owners in (1.3) as

\[
 Y_0=X_{-s},Y_1,\ldots,Y_{L-1}=X_{t-1}.
\]

For each coordinate of \(Y_0\) missing from the total intersection, mark
the transition at which it first departs.  Different initial coordinates
have different marked transitions, because a Johnson transition departs
only one coordinate.  Thus this is an injection from
\(Y_0\setminus P_{s,t}\) into the \(L-1\) internal transitions.

Suppose \(x\in C\) satisfies \(u_x<s\) and \(v_x<t\).  The first
inequality means that \(x\) is absent somewhere on the left of its
positive run through the cut, so \(x\) has an internal arrival.  The
second means that it later has an internal departure on the right.

That later departure transition is not the first-departure image of any
initial coordinate.  If \(x\notin Y_0\), then \(x\) is not initial.  If
\(x\in Y_0\), it already departed before the internal arrival, so the
later departure is not its first departure.  Since the transition departs
\(x\), it cannot be the marked first departure of another coordinate.

At most \(L-2\) transitions are therefore used by the injection.  Hence

\[
 |P_{s,t}|
 =|Y_0|-|Y_0\setminus P_{s,t}|
 \ge(m+1)-(L-2)
 =m+3-s-t,
\]

contradicting (1.5). \(\square\)

The strict inequalities in (2.1) matter.  Extent points directly west,
directly south, or northeast of a correct query are allowed.

## 3. The Pareto staircase

Discard multiplicities in \(\mathcal D\), take its Pareto-minimal points,
and list them as

\[
 d_1=(a_1,b_1),\ldots,d_r=(a_r,b_r)
\tag{3.1}
\]

with increasing first coordinate.  Their second coordinates strictly
decrease.

Construct a southeast unit lattice path \(\Gamma\) from \((1,H)\) to
\((H,1)\) through \(d_1,\ldots,d_r\).  On the initial segment, between
successive minima, and on the final segment, move east first and then
south.  The path makes \(H-1\) east and \(H-1\) south steps, so

\[
 \boxed{|V(\Gamma)|=2H-1.}
\tag{3.2}
\]

### Lemma 3.1 (rectangle interception)

Let \(q\in[H]^2\) have no point of \(\mathcal D\) strictly southwest of
it.  If \(p\in\mathcal D\) and \(p\ge q\), then

\[
 \boxed{V(\Gamma)\cap[q,p]\ne\varnothing.}
\tag{3.3}
\]

#### Proof

Choose a Pareto-minimal point \(d\in\mathcal D\) with \(d\le p\).
Such a point is obtained by descending inside the finite set
\(\mathcal D\cap(-\infty,p]\).

If \(d\ge q\), use \(d\).  The forbidden southwest case leaves two
possibilities.

If \(d_1<q_1\) and \(d_2\ge q_2\), follow \(\Gamma\) forward.  Before
its first coordinate reaches \(q_1\), no Pareto minimum can have second
coordinate below \(q_2\), since that would be a point strictly southwest
of \(q\).  The east-before-south convention therefore supplies a vertex

\[
 z=(q_1,z_2),\qquad z_2\ge q_2.
\]

Forward motion from \(d\) never raises the second coordinate, so
\(z_2\le d_2\le p_2\), and clearly \(z_1=q_1\le p_1\).  Thus
\(q\le z\le p\).

If \(d_1\ge q_1\) and \(d_2<q_2\), follow the path backward.  Backward
motion goes north before west.  Until height \(q_2\) is reached, every
Pareto minimum has first coordinate at least \(q_1\), again by southwest
exclusion.  Hence there is a vertex

\[
 z=(z_1,q_2),\qquad z_1\ge q_1.
\]

Backward motion from \(d\) never raises the first coordinate, so
\(z_1\le d_1\le p_1\), while \(z_2=q_2\le p_2\).  Thus
\(q\le z\le p\) in this case as well.  The same argument includes the
initial and terminal endpoint segments of \(\Gamma\). \(\square\)

## 4. The linear lower word

For each staircase vertex \(z=(s,t)\), use the actual set-letter

\[
 W_z=P_{s,t}.
\tag{4.1}
\]

Emit these \(2H-1\) letters in their order along \(\Gamma\).

### Theorem 4.1 (literal lower staircase identity)

For every floor-correct query \(q=(s,t)\),

\[
 \boxed{
 P_{s,t}
 =\bigcup_{\substack{z\in V(\Gamma)\\ z\ge(s,t)}}W_z.}
\tag{4.2}
\]

The letters on the right form one contiguous subword.  Every emitted
letter is nonzero.

#### Proof

Along \(\Gamma\), the first coordinate is nondecreasing and the second is
nonincreasing.  Thus the condition \(z_1\ge s\) selects a suffix and
\(z_2\ge t\) a prefix; their intersection is a contiguous subpath.

If \(z\ge(s,t)\), (1.10) gives \(W_z\subseteq P_{s,t}\).  Conversely,
take \(x\in P_{s,t}\).  Then \(p_x\ge(s,t)\).  Lemma 2.1 gives the
southwest-exclusion hypothesis of Lemma 3.1, so there is

\[
 z\in V(\Gamma)\cap[(s,t),p_x].
\]

Since \(p_x\ge z\), (1.10) gives \(x\in W_z\).  This proves (4.2).

Finally, \(W_z=P_{s,t}\) intersects \(s+t\le2H\) consecutive owners.
At most one initial coordinate is lost at each of the \(s+t-1\)
transitions, so

\[
 |W_z|\ge m+2-s-t\ge m+2-2H\ge1
\]

by (0.1). \(\square\)

## 5. The upper word and exact one-cut length

Emit the owner segment

\[
 W^+=X_{-H},X_{-H+1},\ldots,X_{H-1}.
\tag{5.1}
\]

Every upper union of at most \(H+1\) consecutive owners crossing the cut
is exactly the union of its corresponding contiguous subsegment of
\(W^+\).  These \(2H\) owner letters are nonzero.

Concatenate the lower staircase word and \(W^+\).  All chosen witnesses
stay inside their own block, so no compatibility condition is introduced
at the concatenation.  The total length is

\[
 \boxed{(2H-1)+2H=4H-1.}
\tag{5.2}
\]

This proves (0.2), with every target witnessed by a literal contiguous OR.

## 6. Several cuts

Consider a cyclic projected-owner component of length \(\ell\), and cut
it at \(J\ge1\) transition edges meeting every positive residence of
length at most \(H\).  Endpoint-capped erosion of the resulting \(J\)
paths uses

\[
 \ell+HJ
\tag{6.1}
\]

letters and preserves every correct target whose owner window remains
inside a path.

Append the \((4H-1)\)-letter chart at every cut.  If a depth-at-most-\(H\)
window crosses several nearby cuts, choose any one of them.  Relative to
that cut the window uses \(s,t\ge1\) and satisfies \(s+t-1\le H\), and
the chart is defined from the original cyclic owners, not from unrelated
endpoint dummies.  Hence it represents the window exactly.

The total component length is

\[
 \ell+HJ+(4H-1)J
 =\boxed{\ell+(5H-1)J}. 
\tag{6.2}
\]

Projected PBBS owner cycles have length at least \(2m+1\).  Under (0.1),
all indices in each \(2H\)-owner chart therefore lie in one unambiguous
cyclic neighborhood.

There is an exact source of sharing which the additive bound (6.2) ignores.
If the cut is between \(X_{c-1}\) and \(X_c\), write

\[
 P^{(c)}_{s,t}=\bigcap_{i=c-s}^{c+t-1}X_i.
\tag{6.3}
\]

Then adjacent cuts satisfy the literal diagonal identity

\[
 \boxed{
 P^{(c)}_{s,t}=P^{(c+1)}_{s+1,t-1}}
\tag{6.4}
\]

whenever \(1\le s,t\le H\), \(t\ge2\), and \(s+1\le H\).  Both sides
are the intersection over the same global owner interval.  More generally,
two cells at two cuts are identical whenever their global left and right
endpoints agree.

Thus a bulk construction should place all selected cuts in the global
endpoint plane and share repeated staircase cells there.  Merely appending
the local paths discards this exact equality.  Identity (6.4) alone does
not give a sublinear global bound when successive selected cuts are
typically \(\Theta(H)\) apart, but it identifies the correct object for the
next fusion step.

## 7. Linear order is unavoidable

### Proposition 7.1

Suppose one cut has \(t\) distinct crossing targets of one common rank.
Every literal word which represents all of them has length at least \(t\).
Consequently a strong depth-\(H\) Johnson collar, whose \(H\) crossing
upper targets are distinct and have one rank, requires at least \(H\)
letters in any seam chart.

#### Proof

Choose one witnessing interval for each target.  If two chosen intervals
have the same left endpoint, one contains the other.  Their ORs are then
comparable by inclusion.  Distinct sets of the same cardinality are
incomparable, so this is impossible.  Thus the \(t\) witnesses have
distinct left endpoints, and a word containing them has at least \(t\)
positions. \(\square\)

Hence the \(4H-1\) construction has optimal order of growth.  This lower
bound does not assert that its constant four is sharp.

The following explicit collar strengthens the constant in this order
lower bound for the full arbitrary-Johnson scope.

### Proposition 7.2 (explicit triangular counting lower bound)

Assume \(2H\le m+1\).  There is a rank-\((m+1)\) Johnson collar for which
all

\[
 \frac{H(H+1)}2
\]

required lower crossing targets are floor-correct and distinct, and the
same is true of the upper targets.  Any word covering just the lower
triangle has length at least \(H\); any word covering both triangles has
length at least

\[
 \boxed{
 \left\lceil\frac{\sqrt{1+8H(H+1)}-1}{2}\right\rceil
 = (\sqrt{2}+o(1))H.}
\tag{7.1}
\]

#### Proof

Choose pairwise disjoint sets

\[
 K,\quad A=\{\alpha_1,\ldots,\alpha_{H-1}\},\quad
 B=\{\beta_1,\ldots,\beta_{H-1}\},
\]

\[
 L=\{\ell_0,\ldots,\ell_{H-1}\},\quad
 R=\{\rho_0,\ldots,\rho_{H-1}\},
\]

with \(|K|=m-2H+2\).  They use \(m+2H\le2m+1\) coordinates.  For
\(1\le s,t\le H\), define

\[
 X_{-s}
 =K\cup B\cup\{\alpha_u:u\ge s\}
       \cup\{\ell_0,\ldots,\ell_{s-1}\},
\tag{7.2}
\]

\[
 X_{t-1}
 =K\cup A\cup\{\beta_v:v\ge t\}
       \cup\{\rho_0,\ldots,\rho_{t-1}\}.
\tag{7.3}
\]

Every owner has size \(m+1\).  Consecutive negative-side owners exchange
\(\ell_{s-1}\) for \(\alpha_{s-1}\), consecutive positive-side owners
exchange \(\beta_t\) for \(\rho_t\), and the cut exchanges \(\ell_0\)
for \(\rho_0\).  Thus this is a literal Johnson collar.

Direct intersection and union give

\[
 P_{s,t}
 =K\cup\{\alpha_u:u\ge s\}
       \cup\{\beta_v:v\ge t\},
\tag{7.4}
\]

\[
 U_{s,t}
 =(K\cup A\cup B)
   \cup\{\ell_0,\ldots,\ell_{s-1}\}
   \cup\{\rho_0,\ldots,\rho_{t-1}\}.
\tag{7.5}
\]

Hence

\[
 |P_{s,t}|=m+2-s-t,\qquad |U_{s,t}|=m+s+t,
\]

and both indexed families are injective.  Restricting to
\(s,t\ge1\), \(s+t-1\le H\), gives \(H(H+1)/2\) lower targets and the
same number of upper targets.  The two families are disjoint by
cardinality.

A word of length \(n\) has only \(n(n+1)/2\) nonempty intervals, hence at
most that many distinct interval-OR outcomes.  The lower family alone
forces

\[
 \frac{n(n+1)}2\ge\frac{H(H+1)}2,
\]

so \(n\ge H\).  Both families together force

\[
 \frac{n(n+1)}2\ge H(H+1),
\]

which is (7.1). \(\square\)

This construction proves order optimality for the theorem's arbitrary
Johnson-cut domain.  It is not asserted that this exact collar occurs at
every PBBS cut.

## 8. Exact scope and adversarial audit

1. The construction is integral and factor-native.  Every helper letter is
   an actual owner intersection, and every upper helper is an actual owner.
2. Floor correctness is essential.  Lemma 2.1 need not hold for an
   oversized intersection, and the theorem makes no claim for one.
3. The east-before-south corner convention is essential in the two
   one-sided cases of Lemma 3.1.
4. The constants \(4H-1\) and \(5H-1\) are exact for this construction.
5. No FIFO, LIFO, zero-winding, primitive-root, or endpoint-order
   hypothesis is used.  The known local endpoint permutation \(213\) is
   therefore harmless.
6. The theorem solves sharing among the \(\Theta(H^2)\) targets destroyed
   at one cut.  It does not share the \(\Theta(H)\)-letter charts belonging
   to different cuts.

Consequently, in a dense-residence regime with \(J=\Theta(W/H)\), the
local theorem alone still pays \(\Theta(W)\).  The smallest remaining
fusion statement is:

> Given the actual family of selected PBBS cuts, merge their dominance
> staircases in the global endpoint plane and merge their owner charts into
> total added length \(o(HJ)\), while
> retaining one literal contiguous witness for every correct crossing
> target and the endpoint-capped internal targets.

That is a cross-cut sharing problem.  The quadratic one-cut Pascal toll is
no longer part of the obstruction.

## 9. Conditional coefficient-one theorem with the weakened packing gate

Let

\[
 B_m=\operatorname{Cat}_m=\frac{W}{2m+1}.
\]

Here \(\nu_H(P_m)\) is the full-deck complement-projected residence
packing number, exactly as in Section 22 of the residence reduction; it is
the sum of the packing numbers of the physical owner cycles, not the
quotient packing
\(\overline\nu_H\).

For every active projected cycle \(C\), choose a minimum transversal of its
residence intervals of length at most \(H\).  If \(J_C\) is its size, the
circular interval packing--transversal theorem gives

\[
 J_C\le\nu_H(C)+1\le2\nu_H(C),
\tag{9.1}
\]

because an active cycle has \(\nu_H(C)\ge1\).  Inactive cycles use their
cyclic erosion words, at overhead \(2H\) each.  The number of projected
cycles is at most \(B_m\).  Summing (6.2) therefore gives the explicit
deterministic upper ledger

\[
 \boxed{
 L_H\le
 W+2HB_m+2(5H-1)\nu_H(P_m).}
\tag{9.2}
\]

### Theorem 9.1 (Catalan-order residence packing suffices)

Assume that for every fixed \(A>0\), with

\[
 H_A=\lceil A\sqrt m\rceil,
\]

one has

\[
 \boxed{\nu_{H_A}(P_m)=O_A(B_m).}
\tag{CP_A}
\]

Then

\[
 \boxed{
 \nu(k)\le(1+o(1))
 \binom{k}{\lfloor k/2\rfloor}.}
\tag{9.3}
\]

#### Proof

For fixed \(A\), let \(K_A<\infty\) be a constant in \((CP_A)\).  At
\(H=H_A\), (9.2) gives

\[
 \frac{L_H-W}{W}
 \le
 \frac{2H+2K_A(5H-1)}{2m+1}
 =O_{A,K_A}(m^{-1/2})=o_A(1).
\tag{9.4}
\]

Thus the complete audited PBBS support in every fixed Gaussian central
window has one literal word of length \(W+o_A(W)\).

For completeness, diagonalize without requiring uniformity in \(A\).
For each integer \(j\ge1\), choose a valid constant \(K_j\) and then,
recursively, an increasing threshold \(M_j\) so large that, for every
\(m\ge M_j\),

\[
 \nu_{\lceil j\sqrt m\rceil}(P_m)\le K_jB_m,
 \qquad
 \frac{j(1+K_j)}{\sqrt m}\le\frac1j,
 \qquad 2\lceil j\sqrt m\rceil\le m+1,
 \qquad m\ge j^{12}.
\tag{9.5}
\]

The audited product-SCD tail theorem gives, for fixed \(j\), normalized
tail cost

\[
 O\!\left((1+j^2)e^{-j^2+o_m(1)}\right).
\tag{9.6}
\]

Increase \(M_j\) so that this cost is at most
\(\eta_j=C(1+j^2)e^{-j^2/2}\), for one absolute \(C\); then
\(\eta_j\to0\).  Define \(a(m)=j\) on
\(M_j\le m<M_{j+1}\) and put

\[
 H_m=\lceil a(m)\sqrt m\rceil.
\]

Then \(a(m)\to\infty\), \(H_m=o(m)\), the central excess in (9.2) is
\(o(W)\) by (9.5), and the outer-tail word also has length \(o(W)\).
This proves (9.3) in odd dimension.  The audited trimmed one-coordinate
lift gives the same leading constant in even dimension. \(\square\)

The hypothesis \((CP_A)\) is strictly weaker than \((RP_A)\), but it is
still unproved; what was retracted is the claimed disproof of \((RP_A)\).
The linear seam closes the literal
quadratic repair loss; the remaining positive gate is now Catalan-order,
chronology-sensitive residence packing, or an even stronger cross-cut
fusion which avoids paying (9.2) independently.

For fixed \(A\), the deck reduction makes this gate equivalently

\[
 \boxed{
 \overline\nu_{H_A}=O_A\!\left(\frac{B_m}{2m+1}\right).}
\tag{9.7}
\]

Indeed,

\[
 (2m+1)\overline\nu_H
 \le\nu_H(P_m)
 \le2(2m+1)\overline\nu_H+(2m+1)Z_H,
\]

and \((2m+1)Z_H=o(B_m)\) throughout every fixed Gaussian window.  Thus
the exact remaining packing scale is big-oh \(B_m/(2m+1)\), rather than
the little-oh quotient scale forced by singleton seam repair.


<!-- END COMPLETE SOURCE 24 -->


---

<a id="document-25"></a>

## Document 25: PBBS_GENERAL_MARK_LADDER_AUDIT_20260725.md

Source: `/Users/amir.nuriyev/Documents/problem/PBBS_GENERAL_MARK_LADDER_AUDIT_20260725.md`

[Portable document](sources/essential/project/PBBS_GENERAL_MARK_LADDER_AUDIT_20260725.md) · [Exact original](originals/project/PBBS_GENERAL_MARK_LADDER_AUDIT_20260725.md)

<!-- BEGIN COMPLETE SOURCE 25 -->

# Audit of the proposed general PBBS mark ladder

Date: 2026-07-25

Method: exact unmatched-zero calculus. No search or computation is used.

## 0. Verdict

The proposed implication

\[
 A_0\longrightarrow C_0
 \quad\Longrightarrow\quad
 g(S\cup P_i)=S\cup P_{i+1}\quad(0\le i<q)
\]

is **false for an arbitrary \(A\to C\) boundary**. The first obstruction
is already present at \(q=2\), and there is a direct \(q=3\)
counterexample.

The valid clean-label rule says that flipping a zero keeps the old
forward marks immediately preceding that zero and the old reverse marks
immediately succeeding it. What fails is the next inference: after
flipping \(C_0\), the next reverse mark \(C_1\) need not be preceded by
the originally chosen \(A_0\) among the *surviving* forward marks. Some
forward marks lying in the physical arc \((C_0,C_1)\) can survive. Thus
the boundary \(A_0\to C_0\) need not peel to \(A_0\to C_1\).

This does **not** refute the strengthened construction in
PBBS_Q3_DEFICIT7_COMPLETE_SUPPORT_20260725.md. That construction chooses
the boundary after a global maximum of a gap potential. Its inequalities

\[
 x_j\le j,\qquad y_j\le j
\]

do force every required surviving boundary. Sections 6--8 below give an
independent audit of that repair. The resulting conclusions are:

1. the arbitrary-transition ladder is false;
2. Lemma 6.2 (global-maximum corridor) is correct;
3. Theorem 6.1 (corridor \(\Rightarrow\) \(q\)-edge PBBS ladder) is
   correct;
4. hence the updated complete-support theorem is not affected by the
   counterexamples in Sections 3--4.

## 1. The valid clean-label rule

Let a cyclic binary word have zero excess \(d\ge3\), so its forward and
reverse parenthesis matchings each leave \(d\) unmatched zeros. If a
zero \(u\) is changed to one, the new word has zero excess \(d-2\).

### Lemma 1.1

After changing \(u\) to one:

1. the forward unmatched zeros are the \(d-2\) old forward marks
   immediately preceding \(u\) in physical circular order;
2. the reverse unmatched zeros are the \(d-2\) old reverse marks
   immediately succeeding \(u\) in physical circular order.

Here the predecessor/successor is strict if \(u\) itself is a mark.

#### Proof

Cut the old word at its forward unmatched zeros and write it as

\[
 0_{a_0}D_0\,0_{a_1}D_1\cdots0_{a_{d-1}}D_{d-1},
\]

where every \(D_j\) is Dyck. If \(u=a_j\), changing it to one consumes
\(a_j\) and the next forward unmatched zero. If \(u\) is a down-step in
some \(D_j\), the changed block has final height two, and those two units
consume the first two forward unmatched zeros after \(u\). In either
case precisely the two forward marks at or immediately after \(u\)
disappear. The remaining \(d-2\) marks are exactly the strict
predecessors asserted above. Reversing the physical circle proves the
reverse statement. \(\square\)

The lemma is not the source of the failure.

## 2. Where the proposed peeling induction breaks

Suppose the combined mark word, with a shared coordinate displayed in
local order \(C,A\), has a transition

\[
 A_0\longrightarrow C_0.
\]

After flipping \(C_0\), Lemma 1.1 leaves the \(d-2\) forward marks
immediately preceding \(C_0\), and the \(d-2\) reverse marks immediately
succeeding \(C_0\). It does **not** follow that \(A_0\) is immediately
followed by \(C_1\) in the new combined mark word. Indeed, if at least
three old forward marks lie in the physical arc \((C_0,C_1)\), then all
but the first two of them survive and occur before \(C_1\).

This invalidates the claimed induction

\[
 A_0\to C_0
 \Longrightarrow A_0\to C_1
 \Longrightarrow A_0\to C_2\longrightarrow\cdots.
\]

The same issue occurs in the opposite direction when the proposed
ladder begins flipping \(A\)-marks.

## 3. A direct \(q=3\) counterexample

Take \(q=3\), \(m=10\), and \(n=21\). Let \(S\) be the rank-seven set
whose cyclic binary word is

\[
 \boxed{
 0_a\,1\,0_z\,
 0_{b_1}0_{b_2}0_{b_3}0_{b_4}0_{b_5}0_{b_6}\,
 1^6\,
 0_{c_1}0_{c_2}0_{c_3}0_{c_4}0_{c_5}0_{c_6}.}
\tag{3.1}
\]

It has seven ones and fourteen zeros, hence zero excess seven as
required for a rank-\((m-3)\) target.

Forward matching leaves exactly

\[
 U_+(S)=\{a,b_1,b_2,b_3,b_4,b_5,b_6\}.
\tag{3.2}
\]

Indeed, the displayed word has the forward Dyck decomposition

\[
 0_a(10_z)\,0_{b_1}\,0_{b_2}\,0_{b_3}\,0_{b_4}\,0_{b_5}\,
 0_{b_6}(1^60^6).
\]

Reverse matching pairs \(a\) with the first displayed one and pairs
\(b_6,b_5,\ldots,b_1\) with the later six ones. Hence

\[
 U_-(S)=\{z,c_1,c_2,c_3,c_4,c_5,c_6\}.
\tag{3.3}
\]

The combined mark word therefore contains the genuine consecutive
transition

\[
 A_a\longrightarrow C_z.
\tag{3.4}
\]

Choose it as the proposed \(A_0\to C_0\). With the prescribed indexing,

\[
 A_0=a,\quad A_1=b_6,\quad A_2=b_5,
\]

\[
 C_0=z,\quad C_1=c_1,\quad C_2=c_2.
\tag{3.5}
\]

The first claimed ladder edge is therefore

\[
 S\cup\{c_2,c_1,z\}
 \stackrel{?}{\longmapsto}
 S\cup\{c_1,z,a\}.
\tag{3.6}
\]

Put

\[
 R=S\cup\{z,c_1\}.
\]

This is a rank-\((m-1)\) core. Apply Lemma 1.1 twice. After flipping
\(z\), the forward and reverse marks are

\[
 \{a,b_6,b_5,b_4,b_3\},
 \qquad
 \{c_1,c_2,c_3,c_4,c_5\}.
\]

After then flipping \(c_1\), the marks of \(R\) are

\[
 U_+(R)=\{b_6,b_5,b_4\},
 \qquad
 U_-(R)=\{c_2,c_3,c_4\}.
\tag{3.7}
\]

In their surviving combined order, \(A_{b_6}\) is immediately followed
by \(C_{c_2}\). The exact deficit-three PBBS rule consequently gives

\[
 \boxed{
 g\bigl(R\cup\{c_2\}\bigr)=R\cup\{b_6\}.}
\tag{3.8}
\]

For completeness, the deficit-three rule follows because
\(r_+(R\cup\{c_2\})=b_6\) and
\(r_-(R\cup\{b_6\})=c_2\). Hence

\[
 f(R\cup\{c_2\})
 =[n]\setminus(R\cup\{b_6,c_2\})
 =f^{-1}(R\cup\{b_6\}),
\]

and applying \(f\) proves (3.8).

Since \(a\ne b_6\), equations (3.6)--(3.8) give the claimed failure:

\[
 \boxed{
 g\bigl(S\cup\{c_2,c_1,z\}\bigr)
 =S\cup\{c_1,z,b_6\}
 \ne S\cup\{c_1,z,a\}.}
\tag{3.9}
\]

Thus the first edge of the proposed \(q=3\) ladder can already be wrong.

## 4. The same obstruction already occurs at \(q=2\)

Take \(m=7,n=15\), and use the rank-five word

\[
 0_a\,1\,0_z\,
 0_{b_1}0_{b_2}0_{b_3}0_{b_4}\,
 1^4\,
 0_{c_1}0_{c_2}0_{c_3}0_{c_4}.
\tag{4.1}
\]

Its forward marks are \(a,b_1,b_2,b_3,b_4\), its reverse marks are
\(z,c_1,c_2,c_3,c_4\), and \(A_a\to C_z\) is consecutive. The proposed
first edge is

\[
 S\cup\{c_1,z\}
 \stackrel{?}{\longmapsto}
 S\cup\{z,a\}.
\]

But the core \(R=S\cup\{z\}\) has forward marks
\(a,b_4,b_3\) and reverse marks \(c_1,c_2,c_3\). Its surviving boundary
at \(c_1\) is \(A_{b_4}\to C_{c_1}\), so

\[
 \boxed{
 g(S\cup\{c_1,z\})=S\cup\{z,b_4\}\ne S\cup\{z,a\}.}
\tag{4.2}
\]

This does not contradict the separate theorem that every depth-two
target has some PBBS three-state witness. It only shows that an arbitrary
combined \(A\to C\) transition does not supply the advertised fixed-label
ladder. In (4.1), the later transition \(A_{b_4}\to C_{c_1}\) is the
well-positioned one.

## 5. The corrected exact gate

For the proposed windows \(P_i\), define their rank-\((m-1)\) common
cores

\[
 R_i=(S\cup P_i)\cap(S\cup P_{i+1})
 \qquad(0\le i<q).
\tag{5.1}
\]

Let

\[
 x_i=C_{q-1-i},\qquad y_i=A_i
\]

be respectively the deleted and inserted coordinates at step \(i\).
Then the exact PBBS criterion is

\[
 \boxed{
 g(R_i\cup\{x_i\})=R_i\cup\{y_i\}
 \iff
 \begin{cases}
 r_+(R_i\cup\{x_i\})=y_i,\\
 r_-(R_i\cup\{y_i\})=x_i.
 \end{cases}}
\tag{5.2}
\]

Equivalently, in the deficit-three mark data of \(R_i\), the surviving
forward mark \(A_{y_i}\) must immediately precede the surviving reverse
mark \(C_{x_i}\). The original single adjacency \(A_0\to C_0\) verifies
none of these later \(q\) conditions by itself.

Therefore a repaired all-depth theorem has to prove one of the following
genuinely stronger assertions:

1. every deficit-\((2q+1)\) word has a transition whose induced fixed
   labels satisfy all \(q\) conditions (5.2); or
2. a dynamically relabelled construction always produces a length-\(q\)
   path in the fibre over \(S\); or
3. a different PBBS argument supplies the required path.

The original arbitrary-cut argument proved none of them. The updated
global-maximum corridor lemma proves the first assertion; this is audited
next. The obstruction above is therefore an obstruction to the naive
selection rule, not to the strengthened all-depth theorem.

## 6. Audit of the global-maximum corridor lemma

Let the expanded mark word contain \(d=2q+1\) symbols of each type.
Index its \(C\)-symbols cyclically. Put

\[
 z_i=\#\{\text{\(A\)-symbols strictly between \(C_i\) and \(C_{i+1}\)}\}.
\tag{6.1}
\]

Then \(\sum_i z_i=d\). Define a periodic potential by

\[
 H(i+1)-H(i)=z_i-1.
\tag{6.2}
\]

Choose \(i\) at a global maximum of \(H\). Since

\[
 H(i)-H(i-1)=z_{i-1}-1\ge0,
\]

the gap immediately before \(C_i\) contains an \(A\)-symbol. Its final
\(A\)-symbol, called \(A_0\), is immediately followed by
\(C_0:=C_i\).

For \(j\ge1\), the number \(x_j\) of \(A\)-symbols strictly between
\(C_0\) and \(C_j=C_{i+j}\) is

\[
 x_j=\sum_{h=0}^{j-1}z_{i+h}.
\]

Maximality gives

\[
 x_j-j=H(i+j)-H(i)\le0,
\]

so

\[
 \boxed{x_j\le j.}
\tag{6.3}
\]

For the reverse inequality, the \(L\) gaps ending at the selected gap
contain

\[
\begin{aligned}
\sum_{h=1}^{L}z_{i-h}
&=d-\sum_{h=0}^{d-L-1}z_{i+h}\\
&\ge d-(d-L)=L.
\end{aligned}
\tag{6.4}
\]

Take \(L=j+1\). The current gap and the preceding \(j\) gaps contain at
least \(j+1\) \(A\)-symbols. Starting from the final \(A\)-symbol in the
current gap, the \(j\)-th preceding \(A\)-symbol is therefore reached
after crossing at most \(j\) \(C\)-symbols. Hence

\[
 \boxed{y_j\le j.}
\tag{6.5}
\]

This proves Lemma 6.2, including both orientations. The argument remains
valid when an \(A\)- and \(C\)-symbol share a physical coordinate,
because the expanded local order \(C,A\) assigns that \(A\)-symbol to
the gap following its \(C\)-copy.

## 7. Audit of the corridor-to-ladder theorem

Assume now only the weaker corridor bounds

\[
 x_j\le2j,\qquad y_j\le2j
 \quad(1\le j\le q-1).
\tag{7.1}
\]

At the selected boundary index the \(A\)-marks forward as

\[
 F_0=A_0,F_1,\ldots,F_{d-1},
\qquad A_h=F_{d-h}\quad(\bmod d),
\tag{7.2}
\]

and index the \(C\)-marks forward as \(C_0,C_1,\ldots,C_{d-1}\).

Fix \(0\le t<q\) and put

\[
 r=q-t-1,
\]

\[
 K_t=S\cup\{C_0,\ldots,C_{r-1}\}
          \cup\{A_0,\ldots,A_{t-1}\}.
\tag{7.3}
\]

This is the proposed common rank-\((m-1)\) core.
The coordinate-distinctness check in Section 8 is independent of the
mark-elimination calculation and may formally be read first; it ensures
that every displayed flip below changes a zero to one.

### 7.1 Forward marks

Flip \(C_0,C_1,\ldots,C_{r-1}\) in order. After the first \(j\) flips,
the removed forward marks are exactly

\[
 F_1,F_2,\ldots,F_{2j}.
\tag{7.4}
\]

Indeed, \(x_j\le2j\) says that every \(A\)-mark strictly between
\(C_0\) and \(C_j\) is among those already removed. Thus the first two
current forward marks at or after \(C_j\) are
\(F_{2j+1},F_{2j+2}\), and Lemma 1.1 removes precisely those two.

After the \(r\) \(C\)-flips, the forward marks are

\[
 F_0,F_{2r+1},F_{2r+2},\ldots,F_{d-1}.
\tag{7.5}
\]

Now flip \(A_0,A_1,\ldots,A_{t-1}\). Each is a current forward mark:
the flip removes that mark itself at the high-index end and the next
current mark at the low-index end. Since

\[
 d-2r=2t+3,
\]

the three final forward marks are exactly

\[
 \boxed{U_+(K_t)=\{A_t,A_{t+1},A_{t+2}\}.}
\tag{7.6}
\]

The bound \(x_r\le2r\) places \(C_r\) before all three surviving marks
in the forward traversal from \(C_0\). They occur in the order
\(A_{t+2},A_{t+1},A_t\), so the strict forward predecessor of \(C_r\)
is \(A_t\).

### 7.2 Reverse marks

Analyze the same final set in the opposite flip order. First flip
\(A_0,\ldots,A_{t-1}\). The inequalities \(y_j\le2j\) show inductively
that these flips remove the last \(2t\) \(C\)-marks. Then flip the
current reverse marks \(C_0,\ldots,C_{r-1}\). Each removes itself and
the final current reverse mark. Since again \(d-2t-2r=3\), this leaves

\[
 \boxed{U_-(K_t)=\{C_r,C_{r+1},C_{r+2}\}.}
\tag{7.7}
\]

The bound \(y_t\le2t\) puts \(A_t\) after all removed preceding
\(C\)-marks and before the first surviving one. Therefore the strict
reverse successor of \(A_t\) is \(C_r\).

The deficit-three law now gives

\[
 \boxed{
 g(K_t\cup\{C_r\})=K_t\cup\{A_t\}.}
\tag{7.8}
\]

This proves every arrow in the proposed \(q\)-edge path.

## 8. Coordinate coincidences and the common intersection

It remains to check that shared \(A/C\) coordinates do not collapse a
state or survive in every state. Suppose \(C_j=A_h\). Because the local
expanded order is \(C_j,A_h\), for the relevant indices
\(0\le j,h\le q-1\) one has

\[
 x_j=d-h-1.
\tag{8.1}
\]

If \(j+h\le q-1\), then

\[
 x_j=2q-h\ge q+j+1>2j,
\]

contradicting the corridor inequality. Thus

\[
 \boxed{C_j=A_h\ \Longrightarrow\ j+h\ge q}
\tag{8.2}
\]

throughout the selected index ranges.

Coordinates \(C_j\) and \(A_h\) occur together in some \(P_t\) only
when \(j+h\le q-2\), so (8.2) proves that every \(P_t\) has \(q\)
distinct coordinates. Their two ranges of appearances cover all
\(t=0,\ldots,q\) only when \(j+h\le q-1\), again excluded by (8.2).
Hence no extra coordinate survives all \(q+1\) states, and

\[
 \boxed{\bigcap_{t=0}^{q}(S\cup P_t)=S.}
\tag{8.3}
\]

The endpoint case \(j=0\) is harmless: a shared \(A\)-copy immediately
after \(C_0\) is \(A_{d-1}\), outside the selected range
\(A_0,\ldots,A_{q-1}\).

Therefore the global-maximum cut supplies a valid corridor and the
corridor supplies the complete PBBS ladder. The arbitrary-cut
counterexamples remain correct but do not invalidate Theorems 6.1--6.3
of the updated note.


<!-- END COMPLETE SOURCE 25 -->


---

<a id="document-26"></a>

## Document 26: MATH_AUDIT_PBBS_FIRST_SHADOW_THEOREM_20260726.md

Source: `/Users/amir.nuriyev/Documents/problem/MATH_AUDIT_PBBS_FIRST_SHADOW_THEOREM_20260726.md`

[Portable document](sources/essential/project/MATH_AUDIT_PBBS_FIRST_SHADOW_THEOREM_20260726.md) · [Exact original](originals/project/MATH_AUDIT_PBBS_FIRST_SHADOW_THEOREM_20260726.md)

<!-- BEGIN COMPLETE SOURCE 26 -->

# Independent audit of the PBBS first-shadow theorem

Date: 2026-07-26

Audited file:
`MATH_ATTACK_O2_FIRST_SHADOW_FACTOR_20260724.md`, especially Sections
2--3 and the imported orbit-length assertion.

Finite diagnostic:
`scratch/audit_pbbs_first_shadow.py`.

## 0. Verdict

The theorem passes.

For the canonical cyclic-parenthesis/PBBS permutation `f` on
`\binom{[2m+1]}m`, and every
`S\in\binom{[2m+1]}{m-1}`, the angle load satisfies

\[
                              1\le\mu_P(S)\le3.               \tag{0.1}
\]

The lower-bound witness and the multiplicity-three upper bound in the
attacked note are correct.  Their prose suppresses two elementary matching
lemmas, but no false implication is hidden.  Those lemmas are supplied in
Sections 2--4 below.

The PBBS orbit assertion also passes, with an important dependency label:

\[
                 \text{every PBBS orbit length is divisible by }2m+1.
                                                                    \tag{0.2}
\]

This does **not** follow merely from `f` being a cyclic-equivariant
permutation.  It uses the componentwise coordinate-homomesy theorem for the
periodic box-ball map.  The proof chain in
`PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md` is valid: parenthesis flip is
the infinite-capacity periodic BBS evolution, the theta-function period is
genuine even with repeated soliton amplitudes, and telescoping gives exact
site homomesy.  Section 6 records the short implication from homomesy to
(0.2).  Thus (0.2) is rigorous but imported, not proved internally in the
attacked note.

Finally, centering the two PBBS neighbours at every Kneser vertex gives a
simple spanning `2`-factor of `J(2m+1,m)` with:

* every rank-`(m+1)` union colour exactly once;
* lower intersection histogram exactly `\mu_P`; and
* at most

  \[
                              2\operatorname {Cat}_m
                              =\frac{2W}{2m+1}=O(W/m)        \tag{0.3}
  \]

  components.

No counterexample occurs in exhaustive exact checks through `m=8` for all
local matching assertions and through `m=10` for the load, orbit, and
projection assertions.  The finite checks are diagnostic only; the proof
of (0.1)--(0.3) is symbolic.

Accordingly the PBBS first-shadow theorem and its centered Johnson-factor
corollary are safe to use, provided the orbit-divisibility statement remains
explicitly attributed to PBBS homomesy.

## 1. Exact matching conventions

Put

\[
                              n=2m+1.                         \tag{1.1}
\]

Write a subset as a cyclic binary word, with `1` an opening step and `0` a
closing step.

The **forward matching** repeatedly removes cyclic adjacent `10` pairs.
The **reverse matching** repeatedly removes cyclic adjacent `01` pairs.
When a word has more zeros than ones, the survivors are zeros.  The result
is independent of the deletion order: cut immediately after one surviving
zero and use the ordinary stack matching on the resulting linear word.
Equivalently, these are the two orientations of the unique cyclic
noncrossing matching.

For `A\in\binom{[n]}m`, each matching leaves one zero.  Denote the forward
and reverse survivors by

\[
                              r_+(A),\qquad r_-(A).            \tag{1.2}
\]

The PBBS map is

\[
                              f(A)=A^c\setminus\{r_+(A)\}.    \tag{1.3}
\]

### Lemma 1.1 (inverse formula)

The map `f` is a permutation and

\[
                              f^{-1}(A)=A^c\setminus\{r_-(A)\}. \tag{1.4}
\]

#### Proof

Forward matching pairs every `1` of `A` with a matched `0`.  Formula (1.3)
flips both bits in every pair and leaves the unique unmatched zero fixed.
The same pairs in the new word are noncrossing `01` pairs, and reverse
matching leaves the same zero unmatched.  Flipping those reverse pairs
recovers `A`.  This proves both invertibility and (1.4). `\square`

Adjacent PBBS states are disjoint because every old `1` is changed to zero.
Thus the permutation orbits are closed walks in `KG(n,m)`.  Once (0.2) is
known, their lengths are at least `n>=5` for `m>=2`, so they are simple
cycle components and `f(A)\ne f^{-1}(A)`.

## 2. The clean-label lemma used by the upper bound

Fix

\[
                              S\in\binom{[n]}{m-1},
 \qquad                       T=[n]\setminus S.              \tag{2.1}
\]

Both cyclic matchings of the deficit-three word `S` leave three zeros.
Let their survivor sets be

\[
                              U_+(S),\qquad U_-(S),
 \qquad |U_+(S)|=|U_-(S)|=3.                                \tag{2.2}
\]

For `u\in T`, define

\[
 \alpha_S(u)=r_+(S\cup\{u\}),
 \qquad
 \beta_S(u)=r_-(S\cup\{u\}).                               \tag{2.3}
\]

### Lemma 2.1 (clean-label images)

One has

\[
 \boxed{alpha_S(T)\subseteq U_+(S)},
 \qquad
 \boxed{eta_S(T)\subseteq U_-(S)}.                        \tag{2.4}
\]

#### Proof

Contract every old forward-matched pair of `S`.

If `u` is one of the three unmatched zeros, flipping it leaves, after the
old contractions, one `1` and two old unmatched zeros.  Forward reduction
therefore leaves one of those old zeros.

If `u` was matched, omit its old pair from the contraction.  Its old
partner is a `1`, and the flipped `u` is now another `1`.  The reduced
cyclic word has two `1`s and the same three old unmatched zeros.  Reducing
it leaves one of those three zeros.  In either case
`\alpha_S(u)\in U_+(S)`.

The identical argument with `01` pairs proves the reverse inclusion for
`\beta_S`. `\square`

This contraction proof is the precise justification for the
“deficit-three clean-label argument” in line (3.9) of the attacked note.
It does not assume that `u` is an unmatched zero or that the Dyck blocks
have distinct heights.

## 3. Exact occurrence/fixed-point bijection

For `u\in T`, formulas (1.3)--(1.4) give

\[
 f(S\cup\{u\})
 =T\setminus\{u,\alpha_S(u)\},                              \tag{3.1}
\]

and

\[
 f^{-1}(S\cup\{v\})
 =T\setminus\{v,\beta_S(v)\}.                              \tag{3.2}
\]

The unmatched coordinate cannot be the newly flipped coordinate, so

\[
                              \alpha_S(u)\ne u,
 \qquad                       \beta_S(v)\ne v.               \tag{3.3}
\]

### Lemma 3.1 (angle occurrences are fixed points)

Directed PBBS two-paths

\[
 S\cup\{u\}\longrightarrow X\longrightarrow S\cup\{v\}  \tag{3.4}
\]

whose endpoint intersection is `S` are in bijection with the fixed points
of `\beta_S\circ\alpha_S` on `T`.

#### Proof

Equations (3.1)--(3.2) give the same middle state `X` exactly when

\[
                 \{u,\alpha_S(u)\}=\{v,\beta_S(v)\}.        \tag{3.5}
\]

The two endpoints in (3.4) are distinct, and (3.3) holds, so (3.5) is
equivalent to

\[
                              v=\alpha_S(u),
 \qquad                       u=\beta_S(v).                  \tag{3.6}
\]

This is precisely `\beta_S(\alpha_S(u))=u`.  Conversely a fixed point
gives (3.4) with

\[
                              X=T\setminus\{u,\alpha_S(u)\}. \tag{3.7}
\]

The predecessor label `u` determines `X`, so distinct fixed points are not
double-counted. `\square`

By Lemma 2.1, every fixed point belongs to

\[
                       \beta_S(T)\subseteq U_-(S),           \tag{3.8}
\]

a set of size three.  Therefore

\[
                              \mu_P(S)\le3.                  \tag{3.9}
\]

The upper-bound argument in the attacked note is consequently correct.

## 4. The constructive fixed point used by the lower bound

List the forward-unmatched zeros of `S` in cyclic order.  Cutting at them
gives the unique decomposition

\[
 0_{z_0}D_0\,0_{z_1}D_1\,0_{z_2}D_2,                       \tag{4.1}
\]

where every `D_i` is a possibly empty Dyck word.  Since `m>=2`, the word
contains `m-1>0` ones, so at least one block is nonempty.

Choose `D_i` of maximum height.  Let `u` be the down-step immediately after
the rightmost occurrence of its maximum.  Such a step exists because
`D_i` returns to height zero.

### Lemma 4.1 (forward label)

\[
                              r_+(S\cup\{u\})=z_i.           \tag{4.2}
\]

#### Proof

In the old matching, `u` is paired with an earlier opening step in `D_i`.
Contract all other old matched pairs.  After flipping `u`, the reduced
cyclic word, starting at `z_i`, has the form

\[
                       0_{z_i}\,1\,1\,0_{z_{i+1}}\,0_{z_{i+2}}. \tag{4.3}
\]

Forward reduction matches the two `1`s to `z_{i+1}` and `z_{i+2}` and
leaves `z_i`. `\square`

We also need the standard reverse cycle lemma.

### Lemma 4.2 (reverse survivor from height)

In a cyclic `0/1` word with one more zero than one, the reverse-unmatched
zero is the down-step following the rightmost global maximum of the prefix
height (`1=+1`, `0=-1`).

#### Proof

Let `M` be the global maximum and rotate the word to begin with the zero
step which leaves the rightmost occurrence of `M`.  Treat `0` as an opening
step and `1` as a closing step.  Before the rotation wraps, the original
height never returns to `M`, so every reverse-height prefix is positive.
After the wrap, the original total is `-1` and every original prefix has
height at most `M`; the reverse-height prefix is again positive.  Its total
is one.  Ordinary linear `01` stack matching therefore pairs every symbol
except the initial zero.  Rotating back preserves the cyclic noncrossing
matching.  This is the reverse form of the usual cycle lemma. `\square`

Now flip `z_i` instead of `u` and rotate the resulting middle word as

\[
                         1D_i\,0D_{i+1}\,0D_{i+2}.           \tag{4.4}
\]

If `H(D)` denotes maximum Dyck height, the maximum prefix heights in its
three regions are at most

\[
 1+H(D_i),\qquad H(D_{i+1}),\qquad H(D_{i+2})-1.             \tag{4.5}
\]

The first is strictly largest because `D_i` was chosen with maximum height.
Its rightmost occurrence is the rightmost maximum of `D_i`, followed by
`u`.  Lemma 4.2 gives

\[
                              r_-(S\cup\{z_i\})=u.           \tag{4.6}
\]

Equations (4.2) and (4.6) say

\[
 \alpha_S(u)=z_i,
 \qquad
 \beta_S(z_i)=u.                                            \tag{4.7}
\]

Thus `u` is a fixed point of `\beta_S\circ\alpha_S`, and Lemma 3.1 gives

\[
                              \mu_P(S)\ge1.                  \tag{4.8}
\]

For `m=2`, the three blocks contain in total one opening and one closing;
exactly one is `10`, so the same construction applies.  This verifies every
step of the lower-bound proof.

Combining (3.9) and (4.8) proves (0.1).

## 5. Load identities and the claimed `O(W/m)` exception set

Let

\[
 a_j=\#\{S:\mu_P(S)=j\},\qquad 1\le j\le3.                 \tag{5.1}
\]

There are

\[
 N=\binom n{m-1}
\]

lower targets and `W=\binom nm` angle occurrences.  Since there are no
holes and no loads above three,

\[
 a_1+a_2+a_3=N,
 \qquad
 a_1+2a_2+3a_3=W.                                          \tag{5.2}
\]

Subtracting gives

\[
 a_2+2a_3=W-N=\frac{2W}{m+2}.                              \tag{5.3}
\]

Consequently

\[
 \boxed{a_3\le\frac{W}{m+2}=O(W/m).}                       \tag{5.4}
\]

The only loads outside `{1,2}` are the load-three targets, so the attacked
note's defect conclusion is exact.

## 6. Orbit lengths: valid imported theorem and exact implication

The attacked note invokes the following external PBBS homomesy theorem.

### PBBS site-homomesy theorem

For a periodic BBS orbit of fundamental period `P` on words of length `L`
and weight `K<L/2`, every coordinate is occupied exactly

\[
                              \frac{PK}{L}                   \tag{6.1}
\]

times during the orbit.

The dedicated audit
`PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md` checks the complete proof
chain:

1. cutting after an unmatched zero identifies the cyclic parenthesis flip
   with the infinite-capacity periodic carrier evolution;
2. the Kuniba--Sakamoto formula used there allows repeated soliton
   amplitudes;
3. translating by `D=det F` is a genuine theta period; and
4. the time telescope is independent of the spatial coordinate and equals
   `DK/L`, hence `PK/L` on the fundamental orbit.

No generic-amplitude assumption or unproved orbit transitivity is used.
Accepting that named periodic-BBS theorem, the orbit-length conclusion here
is immediate and exact.

### Proposition 6.1 (PBBS orbit divisibility)

Every orbit of `f` on `\binom{[2m+1]}m` has length divisible by `2m+1`.

#### Proof

Apply (6.1) with `L=2m+1` and `K=m`.  The occupation count `Pm/L` is an
integer.  Since

\[
                              \gcd(2m+1,m)=1,                \tag{6.2}
\]

one has `2m+1\mid P`. `\square`

This is the only place where the first-shadow package needs the external
homomesy theorem.  Cyclic equivariance of `f` by itself would not prove
Proposition 6.1.

Since the orbit lengths sum to `W`, their number is at most

\[
                              \frac W{2m+1}=B=\operatorname {Cat}_m. \tag{6.3}
\]

## 7. Centered projection audit

Let `F_P` be the PBBS Kneser cycle factor.  For each center `X`, define

\[
                    e_X=\{f^{-1}(X),f(X)\}.                  \tag{7.1}
\]

### Theorem 7.1 (exact centered Johnson factor)

The family `\{e_X\}` is a simple spanning `2`-factor of `J(2m+1,m)`.
Its union colours are all members of `\binom{[n]}{m+1}`, exactly once, its
intersection histogram is `\mu_P`, and it has at most `2B` components.

#### Proof

Both members of `e_X` are PBBS neighbours of `X`, hence are disjoint from
`X`.  They are distinct by Proposition 6.1.  They are distinct `m`-subsets
of the `(m+1)`-set `X^c`, so

\[
 f^{-1}(X)\cup f(X)=X^c,
 \qquad
 f^{-1}(X)\cap f(X)=\chi_P(X).                              \tag{7.2}
\]

Thus `e_X` is a Johnson edge with the stated colours.  The center is
recoverable from the edge as

\[
                              X=(\bigcup e_X)^c,              \tag{7.3}
\]

so distinct centers give distinct edges.  As `X` ranges over all middle
sets, `X^c` ranges bijectively over every upper colour.

A Johnson vertex `Y` lies in the two centered edges belonging to its two
Kneser-factor neighbours.  Hence every Johnson vertex has degree two and
the centered graph is a simple spanning `2`-factor.

On a PBBS component of length `P`, centering joins cyclic positions `j-1`
and `j+1`.  The step-two graph on `\mathbb Z_P` has `\gcd(2,P)\le2`
components.  Proposition 6.1 and (6.3) therefore give at most `2B`
Johnson components. `\square`

Combining Theorem 7.1 with (0.1) and (5.4) proves every PBBS assertion used
in the Mersenne/non-Mersenne successor note.

## 8. Exact small-case counterexample search

The independent checker

[`scratch/audit_pbbs_first_shadow.py`] (historical local link not bundled)

constructs the cyclic `10` matching directly.  It does not import an orbit
table or angle histogram.  For every tested lower target it also checks:

\[
 \alpha_S(T)\subseteq U_+(S),
 \qquad
 \beta_S(T)\subseteq U_-(S),
 \qquad
 \mu_P(S)=|\operatorname {Fix}(\beta_S\circ\alpha_S)|.       \tag{8.1}
\]

It then checks permutation/inverse consistency, Kneser adjacency, orbit
divisibility, centered-edge uniqueness, Johnson degree two, exact union
coverage, equality of the centered and PBBS angle histograms, and the
component bound.

The complete structural check through `m=8` gives:

\[
\begin{array}{c|r|rrrr|rr|r}
m&W&\mu=0&\mu=1&\mu=2&\mu=3&c(P)&c(J)&\max(P)/(2m+1)\\ \hline
1&3&0&0&0&1&1&1&1\\
2&10&0&0&5&0&2&2&1\\
3&35&0&7&14&0&3&3&3\\
4&126&0&45&36&3&6&6&5\\
5&462&0&209&110&11&12&12&7\\
6&1716&0&884&377&26&26&26&21\\
7&6435&0&3630&1320&55&73&73&11\\
8&24310&0&14722&4590&136&146&146&77
\end{array}                                                  \tag{8.2}
\]

A lighter full histogram/orbit/projection scan at `m=9,10` likewise found
no hole, no load above three, no nondivisible orbit, and no projection
failure.  At those parameters the load triples were respectively

\[
\begin{array}{c|rrr}
m&\#(\mu=1)&\#(\mu=2)&\#(\mu=3)\\ \hline
9&59223&15922&437\\
10&236733&55608&1589.
\end{array}                                                  \tag{8.3}
\]

These computations found no counterexample, including the boundary case
`m=2`.  They are not used to infer the general theorem.

## 9. Corrections and dependency discipline

No mathematical retraction is needed.  Two expository corrections should
be observed when reusing the result.

1. The sentence “Since `gcd(n,m)=1`, every orbit length is divisible by
   `n`” is not a consequence of coprimality alone.  Its missing premise is
   PBBS site homomesy.  Proposition 6.1 supplies the exact implication.
2. The image inclusions in the multiplicity-three proof use confluence of
   cyclic matching after contraction.  Lemma 2.1 supplies that argument;
   the informal phrase “the third old unmatched zero remains” is correct
   but too compressed to serve as the proof by itself.

With those dependencies exposed, the chain

\[
 \text{PBBS permutation}
 \Longrightarrow 1\le\mu_P\le3
 \Longrightarrow \text{complete lower shadow and }O(W/m)\text{ bad loads}
\]

and

\[
 \text{PBBS homomesy}
 \Longrightarrow (2m+1)\mid P
 \Longrightarrow O(W/m)\text{ centered Johnson components}
\]

is fully rigorous.


<!-- END COMPLETE SOURCE 26 -->


---

<a id="document-27"></a>

## Document 27: MATH_THEOREM_O_PRODUCT_SCD_TAIL_MIXED_CYCLE_INTERFACE_20260726.md

Source: `/Users/amir.nuriyev/Documents/problem/MATH_THEOREM_O_PRODUCT_SCD_TAIL_MIXED_CYCLE_INTERFACE_20260726.md`

[Portable document](sources/essential/project/MATH_THEOREM_O_PRODUCT_SCD_TAIL_MIXED_CYCLE_INTERFACE_20260726.md) · [Exact original](originals/project/MATH_THEOREM_O_PRODUCT_SCD_TAIL_MIXED_CYCLE_INTERFACE_20260726.md)

<!-- BEGIN COMPLETE SOURCE 27 -->

# Factor-blind product-SCD tails for mixed-frame middle cycles

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict and the tensor plug-in

The product-SCD exterior word is completely independent of the middle
factor.  It may be concatenated after arbitrary mixed-frame recoupling,
cycle splitting, exact replacement, or deletion.  It requires no common
frame, owner, endpoint, chronology, phase, or separator.

Define

\[
 A_m(a)=\binom ma-\binom m{a-1},
 \qquad
 w_m(a)=
 \begin{cases}
 m,&a=0,\\
 m-2a+1,&a>0,
 \end{cases}                                             \tag{0.1}
\]

and

\[
 C_m(t)=
 \begin{cases}
 0,&t<0,\\[1mm]
 \displaystyle\binom m{\min(t,\lfloor m/2\rfloor)},&t\ge0.
 \end{cases}                                             \tag{0.2}
\]

Put

\[
 \boxed{
 L_m(r)=2\sum_{a=0}^{\lfloor m/2\rfloor}
 A_m(a)w_m(a)C_m(r-a).}                                 \tag{0.3}
\]

There is an absolute constant `C_0` such that, for every `m>=1` and
`0<=H<=m-1`,

\[
 \boxed{
 \frac{L_m(m-H-1)}{\binom{2m}m}
 \le C_0\exp\!\left(-\frac{H^2}{8m}\right).}           \tag{0.4}
\]

The word counted by (0.3) covers **both** tails in even dimension.  Its
trimmed one-coordinate lift has length `2L_m(m-H-1)` and covers both tails
in odd dimension.  Consequently

\[
                         \frac H{\sqrt m}\longrightarrow\infty
 \quad\Longrightarrow\quad
 \text{exterior cost}=o(W),                             \tag{0.5}
\]

with no moderate-deviation upper restriction on `H`.

The central tensor interface is as follows.

* In `Q_(2m)`, a retained `H`-safe middle cycle costs its number of middle
  owners plus exactly `2H` collar letters.
* In `Q_(2m+1)`, an `H`-safe alternating `X/Y` cycle, encoded by its
  cyclic `m`-set shore, costs its number of `X` owners plus exactly
  `2H+1` collar letters.
* A legal residual cycle may simply remain as a separate component.  It
  incurs only this collar charge, independently of its owner mass.
* If residual cycles belong to a fully `H`-safe pre-deletion factor,
  balanced multiplicity floors charge total deleted owner mass `r` by
  `O(r sqrt(m))`, uniformly in `H`.
* A mixed-frame junction has zero extra cost if its actual state sequence
  remains `H`-safe.  A junction which is not certified safe must be cut or
  included in the actual central-deficit ledger.  A bare unsafe cut can
  cost `H(H+1)` two-sided shadow occurrences in even dimension and
  `(H+1)^2` in odd dimension.

Thus the tail, component collars, deleted residual cycles, and physical
recoupling seams are four separate ledgers.  Exact middle ownership alone
does not control the remaining central shadow deficit.

## 1. The exact product-SCD exterior word

Split a `2m`-element ground set as `X disjoint-union Y`, with
`|X|=|Y|=m`, and choose arbitrary symmetric-chain decompositions of the two
half-cubes.

A symmetric chain with minimum rank `a` has the form

\[
 C_a\subset C_{a+1}\subset\cdots\subset C_{m-a}.
                                                               \tag{1.1}
\]

Writing `C_j setminus C_(j-1)={e_j}`, define its forward increment word

\[
 R(C)=
 \begin{cases}
 \{e_1\},\ldots,\{e_m\},&a=0,\\
 C_a,\{e_{a+1}\},\ldots,\{e_{m-a}\},&a>0,
 \end{cases}                                             \tag{1.2}
\]

and let `L(C)` be its reversal.  Both have length `w_m(a)`.  Every nonempty
member of `C` is the union of a prefix of `R(C)` and also the union of a
suffix of `L(C)`.

The number of half-cube chains of minimum rank `a` is

\[
                         A_m(a)=\binom ma-\binom m{a-1}. \tag{1.3}
\]

For each ordered pair of chains `(C,D)` with minimum ranks `a,b` satisfying

\[
                              a+b\le r,                 \tag{1.4}
\]

emit the literal gadget

\[
                              L(C)\mathbin\Vert R(D).   \tag{1.5}
\]

Concatenate the gadgets in an arbitrary order.

### Theorem 1.1 (simultaneous two-tail coverage)

The word (1.5), over all pairs satisfying (1.4), covers every nonempty set
`S subseteq X union Y` such that

\[
                         |S|\le r
 \quad\hbox{or}\quad
                         |S|\ge2m-r.                   \tag{1.6}
\]

Its exact constructed length is `L_m(r)` from (0.3).

#### Proof

Write `S=S_X disjoint-union S_Y`, and let `C,D` be the unique half-chains
containing `S_X,S_Y`, with minimum ranks `a,b`.

If `|S|<=r`, then `a+b<=|S|<=r`.  If `|S|>=2m-r`, symmetry of the chains
gives

\[
 a\le m-|S_X|,
 \qquad b\le m-|S_Y|,
 \qquad a+b\le2m-|S|\le r.                              \tag{1.7}
\]

Thus the relevant gadget is present.  A suffix of `L(C)` has union `S_X`
and a prefix of `R(D)` has union `S_Y`; their concatenation is one literal
contiguous interval.  If one part is empty, use only the other side.

The total gadget length is

\[
 \sum_{a+b\le r}A_m(a)A_m(b)(w_m(a)+w_m(b)).             \tag{1.8}
\]

The two summands are equal after interchanging the half-cubes, while

\[
 \sum_{b=0}^{\min(t,\lfloor m/2\rfloor)}A_m(b)
 =\binom m{\min(t,\lfloor m/2\rfloor)}.                 \tag{1.9}
\]

Equations (1.8)--(1.9) give (0.3).  \(\square\)

The same gadgets cover both tails.  The leading factor `2` in (0.3) comes
from the two sides of the chain-pair length in (1.8); it is not a second
copy for the upper tail.

### Lemma 1.2 (trimmed odd lift)

If `Q=(Q_1,...,Q_N)` covers a family of nonempty targets on `V`, then, for
a new coordinate `z`,

\[
 Q_1,\ldots,Q_N,\{z\},
 Q_1\cup\{z\},\ldots,Q_{N-1}\cup\{z\}                 \tag{1.10}
\]

has exactly `2N` entries and covers the old family, `{z}`, and every old
target with `z` adjoined.

#### Proof

Old witnesses stay in the first copy.  If an old witness ends before
`Q_N`, use its translated copy in the last block.  If it ends at `Q_N`, use
the corresponding suffix in the first copy followed by `{z}`.  \(\square\)

At `r=m-H-1`, Theorem 1.1 covers every even-dimensional rank outside

\[
                              [m-H,m+H],                \tag{1.11}
\]

and Lemma 1.2 covers every odd-dimensional rank outside

\[
                              [m-H,m+H+1].              \tag{1.12}
\]

### Theorem 1.3 (uniform exponential tail)

Equation (0.4) holds uniformly for every `0<=H<=m-1`.  Consequently the
even exterior word has length `o(binomial(2m,m))`, and the odd exterior word
has length `o(binomial(2m+1,m))`, whenever `H/sqrt(m)->infinity`.

#### Proof

Put

\[
 h=\lfloor m/2\rfloor,
 \qquad \epsilon=m-2h,
 \qquad x=h-a,
 \qquad d=H+1-\epsilon.                                 \tag{1.13}
\]

For `0<=x<h`, direct subtraction in (1.3) gives

\[
 B_{m,x}:=A_m(h-x)w_m(h-x)
 =\binom m{h-x}
 \frac{(2x+\epsilon+1)^2}{h+x+\epsilon+1},             \tag{1.14}
\]

while `B_(m,h)=m`.  The exact parity-uniform form of (0.3) is

\[
 L_m(m-H-1)
 =2\sum_{x=0}^{h}B_{m,x}
 \binom m{h-(d-x)_+},                                   \tag{1.15}
\]

and

\[
                              \sum_{x=0}^{h}B_{m,x}=2^m-1. \tag{1.16}
\]

The elementary central-ratio estimate is

\[
 \frac{\binom m{h-y}}{\binom mh}\le e^{-y^2/m}
 \qquad(0\le y\le h).                                  \tag{1.17}
\]

It follows by writing the ratio as a product of successive binomial ratios
and using `log(1-u)<=-u`.  Equations (1.14) and (1.17) imply

\[
 \frac{B_{m,x}}{\binom mh}
 \le\frac{8(x+1)^2}{m}e^{-x^2/m}
 \qquad(x<h).                                           \tag{1.18}
\]

Split (1.15) at `t=floor(d/2)`.  For `x<=t`, the second binomial in (1.15)
is at most

\[
                         \binom mh e^{-H^2/(4m)}.       \tag{1.19}
\]

Using (1.16), this part divided by `binomial(2m,m)` is

\[
 O\!\left(
  \frac{2^m\binom mh}{\binom{2m}m}e^{-H^2/(4m)}
 \right).                                               \tag{1.20}
\]

For `x>t`, use

\[
 e^{-x^2/m}\le e^{-H^2/(8m)}e^{-x^2/(2m)}.             \tag{1.21}
\]

Equations (1.15) and (1.18) bound this part, after normalization, by

\[
 O\!\left(
 \frac{\binom mh^2}{\binom{2m}m}
 e^{-H^2/(8m)}
 \left[\frac1m\sum_{x\ge0}(x+1)^2e^{-x^2/(2m)}\right]
 \right).                                               \tag{1.22}
\]

The bracket is `O(sqrt(m))`.  Wallis' inequalities give

\[
 \frac{2^m\binom mh}{\binom{2m}m}=O(1),
 \qquad
 \frac{\binom mh^2\sqrt m}{\binom{2m}m}=O(1).          \tag{1.23}
\]

The exceptional `x=h` term is exponentially smaller.  Equations
(1.20)--(1.23) prove (0.4).  Finally

\[
 \binom{2m+1}m=\frac{2m+1}{m+1}\binom{2m}m             \tag{1.24}
\]

proves the normalized odd assertion.  \(\square\)

No hypothesis `H<=m/2` or `H=o(m^(2/3))` was used.  If `H>=m`, the exterior
family is empty and its charge may be taken to be zero.

For comparison with the older truncated-ideal shorthand, put
`W=binomial(2m,m)` and

\[
 \rho_H=\frac{\binom{2m}{m-H}}{\binom{2m}m}.
\]

The exact product formula gives

\[
 \rho_H
 =\prod_{j=0}^{H-1}\frac{m-j}{m+j+1}
 \le\exp\!\left(-\frac{H^2}{m+H}\right)
 \le\exp\!\left(-\frac{H^2}{2m}\right).               \tag{1.25}
\]

Hence

\[
 \left(1+\frac{H^2}{m}\right)\binom{2m}{m-H}=o(W)     \tag{1.26}
\]

whenever `H/sqrt(m)->infinity`.  Conversely, if `H/sqrt(m)` has a bounded
subsequence, pass to one on which it tends to `c<infinity`; then
`rho_H->e^(-c^2)`, and the normalized right side of (1.26) tends to
`(1+c^2)e^(-c^2)>0`.  Thus `H/sqrt(m)->infinity` is exactly the threshold
for that familiar envelope.  Only the forward implication is needed below.

## 2. Concatenation is the whole product-tail interface

For a literal word `U`, let `Cov(U)` be its family of contiguous interval
unions.  For arbitrary words `U,V`,

\[
                    \operatorname{Cov}(U)\cup
                    \operatorname{Cov}(V)
 \subseteq          \operatorname{Cov}(U\Vert V).      \tag{2.1}
\]

Indeed, an interval internal to either word stays contiguous after
concatenation.  Cross-interface intervals may create additional targets but
cannot destroy an old witness.

### Theorem 2.1 (parity-neutral black-box composition)

Let `A_(m,H)` be any literal central word and `R_(m,H)` any literal repair
word for its residual central targets.  Then

\[
 \boxed{
 \nu(2m)\le |A_{m,H}|+|R_{m,H}|+L_m(m-H-1)}             \tag{2.2}
\]

provided the first two words cover ranks `[m-H,m+H]`, and

\[
 \boxed{
 \nu(2m+1)\le |A_{m,H}|+|R_{m,H}|+2L_m(m-H-1)}         \tag{2.3}
\]

provided they cover ranks `[m-H,m+H+1]`.

There is exactly zero additional `A`--tail seam charge.

#### Proof

Concatenate `A_(m,H)`, `R_(m,H)`, and the appropriate exterior word from
Section 1, and apply (2.1).  \(\square\)

This proves factor-blindness in its strongest form: the product tail does
not even require Stage A to arise from a factor.

## 3. Finite factorization of arbitrary geodesic middle components

The next lemma is the only literal-word input needed from a middle cycle.
It depends on the actual state sequence, not on the frame which produced
it.

Let

\[
                         T=(T_1,\ldots,T_v)             \tag{3.1}
\]

be a linear sequence of subsets of one ground set.  Say that `T` is
**delay-`H` safe** if no coordinate changes twice in any block of at most
`H+1` consecutive transitions.  Equivalently, every internal positive
coordinate run has at least `H+1` states.  Boundary runs may be shorter.
The “at most” clause is needed for path remnants having fewer than `H+1`
transitions; the condition is not intended to be vacuous there.

Define

\[
 A_j=\bigcap_{i=\max(1,j-H)}^{\min(v,j)}T_i,
 \qquad 1\le j\le v+H.                                  \tag{3.2}
\]

### Lemma 3.1 (finite delay factor)

For every `1<=i<=v`,

\[
                         T_i=\bigcup_{j=i}^{i+H}A_j.    \tag{3.3}
\]

For every `1<=a<=b<=v` with `b-a<=H`,

\[
 \bigcap_{i=a}^{b}T_i=\bigcup_{j=b}^{a+H}A_j.           \tag{3.4}
\]

For every `1<=a<=b<=v`, with **no restriction on `b-a`**,

\[
 \bigcup_{i=a}^{b}T_i=\bigcup_{j=a}^{b+H}A_j.           \tag{3.5}
\]

Hence every displayed intersection or union is a literal contiguous OR in
the factor word `(A_1,...,A_(v+H))`.

#### Proof

Fix one coordinate and examine its binary state row.  If it is one at
position `i`, the positive run containing `i` either reaches a boundary or
has at least `H+1` states.  It therefore contains one defining window for
some `A_j` with `i<=j<=i+H`.  This proves the nontrivial direction of
(3.3); the reverse direction is immediate because every such defining
window contains `i`.

If the coordinate is one throughout `[a,b]` and `b-a<=H`, the same run
contains a defining window whose right endpoint `j` lies in
`[b,a+H]`.  Conversely every defining window with such an endpoint contains
`[a,b]`.  This proves (3.4).

Finally, take the union of (3.3) over `a<=i<=b`.  The union of the index
intervals `[i,i+H]` is exactly `[a,b+H]`, proving (3.5) without any
restriction on the length of `[a,b]`.  \(\square\)

The unrestricted range in (3.5) is important for the odd `X/Y` compiler:
an upper depth-`H` target uses `H+2` consecutive `X`-states, although the
factor delay remains `H`.

Empty factor entries may be deleted after all witnesses are fixed.  The
remaining entries of every old witness stay consecutive and retain their
union.

### Corollary 3.2 (path and cycle costs)

A delay-`H` safe path of `v` middle states has a literal factor word of
length `v+H` covering all its internal lower intersections through depth
`H` and all its internal upper unions.

If `(X_i)_(i mod v)` is cyclically delay-`H` safe, cut it once and copy its
first `H` states.  Lemma 3.1 gives a word of length

\[
                              v+2H                       \tag{3.6}
\]

which covers every cyclic intersection and union of at most `H+1`
states.  More generally, copying only `0<=sigma<=H` prefix states gives
length

\[
                              v+H+\sigma.               \tag{3.7}
\]

At signed depth `q`, exactly `(q-sigma)_+` cyclic starts are unavailable.

#### Proof

The path statement is Lemma 3.1.  In the cyclic case, copying `H` prefix
states makes every cyclic window of at most `H` transitions an ordinary
linear interval.  With only `sigma` copied states, the `q` wraparound
windows require respectively `1,...,q` copied states, so precisely the last
`(q-sigma)_+` remain unavailable.  \(\square\)

## 4. Even-dimensional exact cycle theorem

Put

\[
 W=\binom{2m}m,
 \qquad
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.                  \tag{4.1}
\]

Let `F` be any exact middle cycle factor: its pairwise vertex-disjoint
oriented cycles

\[
 C=(X_0,\ldots,X_{\lambda_C-1}),
 \qquad X_i\in\binom{[2m]}m,                            \tag{4.2}
\]

partition all `W` middle sets.  Delete an arbitrary union of complete
cycles of total middle-owner mass `r`, and assume every **retained** cycle
is cyclically delay-`H` safe.  In particular, every retained cyclic segment
of `q<=H` transitions is a Johnson geodesic.  Define its lower and upper
flags by

\[
 L_{i,q}=\bigcap_{j=0}^{q}X_{i+j},
 \qquad
 U_{i,q}=\bigcup_{j=0}^{q}X_{i+j}.                     \tag{4.3}
\]

They have ranks `m-q` and `m+q`.

For each retained cycle choose a copied-prefix length

\[
                              0\le\sigma_C\le H.        \tag{4.4}
\]

Let `M_q^-` and `M_q^+` be the actual numbers of lower and upper targets
not represented by the surviving certified windows, and put

\[
                        D_H^{\rm ret}
                        =\sum_{q=1}^H(M_q^-+M_q^+).     \tag{4.5}
\]

### Theorem 4.1 (direct-support cycle/tail interface)

For every such factor, deletion, and collar choice,

\[
 \boxed{
 \nu(2m)\le
 W+\sum_{C\ \mathrm{retained}}(H+\sigma_C)
 +D_H^{\rm ret}+L_m(m-H-1).}                           \tag{4.6}
\]

In particular, full collars give

\[
 \boxed{
 \nu(2m)\le W+2H K+D_H^{\rm ret}+L_m(m-H-1)}           \tag{4.7}
\]

where `K` is the number of retained cycles.

#### Proof

By Corollary 3.2, a retained cycle `C` contributes
`lambda_C+H+sigma_C` factor letters.  The total retained middle mass is
`W-r`, so all retained cycle words have total length

\[
                    (W-r)+\sum_C(H+\sigma_C).           \tag{4.8}
\]

Append the `r` deleted middle sets once each.  This restores the baseline
to exactly

\[
                         W+\sum_C(H+\sigma_C).          \tag{4.9}
\]

Thus the middle leave cancels exactly; it has no multiplicative `H` charge.
Append every missing certified central shadow once, at cost
`D_H^(ret)`, and append the independent exterior word.  Theorem 2.1 proves
(4.6).  \(\square\)

The direct-support form is the logically sharp factor-blind theorem.  It
does not assume any quota or balance property.

## 5. Floor-buffer leave theorem

For the stronger floor-buffer certificate in this section, assume in
addition that **every** cycle of the full pre-deletion factor `F`, including
the cycles later deleted, is cyclically delay-`H` safe.  Thus its two signed
depth-`q` histograms are rank-correct and have total mass exactly `W`.

For `1<=q<=H`, put

\[
                         c_q=\left\lfloor\frac W{N_q}\right\rfloor. \tag{5.1}
\]

A balanced quota on either signed rank takes values in `{c_q,c_q+1}` and
has total mass `W`.  Let `mu_q^+` and `mu_q^-` be the two occurrence
histograms of the full, pre-deletion exact factor.  Both have total mass
`W`.  Define

\[
 O_q^\pm(F)=
 \min_{b_q}\sum_S(\mu_q^\pm(S)-b_q(S))_+,              \tag{5.2}
\]

where the minimum is over balanced quotas, and put

\[
 J_H(F)=\sum_{q=1}^H\frac{O_q^-(F)+O_q^+(F)}{c_q},
 \qquad
 S_H=\sum_{q=1}^H\frac1{c_q}.                          \tag{5.3}
\]

### Lemma 5.1 (floor-buffer deletion)

Let `mu` be a nonnegative integral vector of total mass `W`, let
`b in {c,c+1}^X` have total mass `W`, and let `0<=delta<=mu`.  Then

\[
 \boxed{
 c\,|\{S:(\mu-\delta)(S)=0\}|
 \le\sum_S(b(S)-\mu(S))_++\|\delta\|_1.}              \tag{5.4}
\]

#### Proof

At a new hole, `mu(S)=delta(S)` and

\[
 c\le b(S)\le(b(S)-\mu(S))_++\delta(S).                \tag{5.5}
\]

Sum over the holes and enlarge the first sum to all coordinates.  \(\square\)

Since `mu` and `b` have equal total mass, overload equals underload for a
minimizing quota.

### Lemma 5.2 (uniform reciprocal floors)

Uniformly for every `H<=m`,

\[
 \boxed{
 S_H\le\frac{4^m}{W}-1
       =(\sqrt\pi+o(1))\sqrt m.}                       \tag{5.6}
\]

#### Proof

For every `x>=1`, `1/floor(x)<=2/x`; hence `1/c_q<=2N_q/W`.  Also

\[
 \sum_{q=1}^{m}N_q=\frac{4^m-W}{2}.                    \tag{5.7}
\]

Sum and use the central-binomial asymptotic.  \(\square\)

### Theorem 5.3 (exact partial-collar leave certificate)

Under the hypotheses of Theorem 4.1,

\[
 \boxed{\begin{aligned}
 \nu(2m)\le{}&
 W+\sum_{C\ \mathrm{retained}}(H+\sigma_C)
 +J_H(F)+2rS_H\\
 &+2\sum_{C\ \mathrm{retained}}\sum_{q=1}^H
       \frac{(q-\sigma_C)_+}{c_q}
 +L_m(m-H-1).
 \end{aligned}}                                        \tag{5.8}
\]

Full collars give the clean form

\[
 \boxed{
 \nu(2m)\le
 W+2HK+J_H(F)+2rS_H+L_m(m-H-1).}                       \tag{5.9}
\]

#### Proof

Deleting complete cycles of total mass `r` removes exactly `r` occurrences
at every depth and sign.  At depth `q`, a partial collar on `C` removes
exactly `(q-sigma_C)_+` further cyclic starts.  Apply Lemma 5.1 separately
to the two signed histograms.  It gives

\[
 M_q^-+M_q^+
 \le\frac{O_q^-(F)+O_q^+(F)+2r
 +2\sum_C(q-\sigma_C)_+}{c_q}.                         \tag{5.10}
\]

Sum (5.10) and substitute it for the actual deficit in (4.6).  \(\square\)

Thus the uniform balanced size-only deletion rate is

\[
                              r=o(W/\sqrt m).           \tag{5.11}
\]

Without the balanced-overload hypothesis and with full collars, deletion of
owner mass `r` can create at most one new hole per deleted occurrence, at
every sign and depth.  Therefore the direct support inequality is

\[
 D_H^{\rm ret}\le D_H^{\rm full}+2Hr,                  \tag{5.12}
\]

and `r=o(W/H)` is the corresponding crude size-only sufficient rate.  A
structured larger leave is allowed whenever its actual deficit in (4.5) is
`o(W)`.

## 6. Mixed-frame recoupling and unsafe seams

The phrase “mixed frame” carries no cost by itself.  Only the resulting
successor word matters.

Let `F` and `F'` be two exact cyclic factors on the same middle owners, and
suppose their directed successor maps differ at `s` owner positions.  At
signed depth `q`, a window changes only if one of its `q` transitions uses
one of those positions.  Hence at most `sq` occurrence slots change.
Therefore

\[
 \frac12\|\mu_q^\pm(F')-\mu_q^\pm(F)\|_1\le sq.        \tag{6.1}
\]

For equal-mass histograms,

\[
 O_q^\pm(\mu)=\frac12\min_{b_q}\|\mu-b_q\|_1.          \tag{6.2}
\]

Distance to a fixed set is one-Lipschitz, so

\[
 J_H(F')\le J_H(F)+2sQ_H,
 \qquad
 Q_H:=\sum_{q=1}^H\frac q{c_q}.                        \tag{6.3}
\]

The weighted seam moment has an exact uniform bound.

### Lemma 6.1 (even recoupling moment)

For every `H<=m`,

\[
 \boxed{2Q_H\le2m.}                                    \tag{6.4}
\]

#### Proof

Again `1/c_q<=2N_q/W`.  The exact binomial moment identity is

\[
 \sum_{q=1}^{m}q\binom{2m}{m-q}
 =\frac m2\binom{2m}m.                                 \tag{6.5}
\]

It follows, for example, by writing `q=m-k`, using
`(m-k)binomial(2m,k)=m[binomial(2m-1,k)-binomial(2m-1,k-1)]`, and
telescoping over `0<=k<m`.  Equations (6.4)--(6.5) follow.  \(\square\)

Consequently

\[
                         J_H(F')\le J_H(F)+2ms.         \tag{6.6}
\]

This term is needed only when one transfers a pre-recoupling estimate.  If
`J_H(F')` or the actual post-recoupling deficit is measured directly, the
history and `s` disappear completely.

### Unsafe-junction caveat

The recoupled factor must still be delay-`H` safe for Theorem 4.1.  A new
Johnson edge is not automatically safe with the preceding and following
`H` transitions.  If a junction cannot be certified, cut there.  A bare
cut has factor overhead `H`, but at depth `q` it removes `q` cyclic starts
on each side.  Thus its raw two-sided shadow charge is at most

\[
                        2\sum_{q=1}^Hq=H(H+1).          \tag{6.7}
\]

With `b` such cuts, the completely unweighted support estimate is

\[
             D_H^{\rm cut}\le D_H^{\rm cyclic}+H(H+1)b. \tag{6.8}
\]

The balanced-floor version replaces (6.7) by `2Q_H<=2m`, so its total
collateral is at most `2mb`.  Therefore

\[
 b=o(W/H^2)                                             \tag{6.9}
\]

is the crude support-blind rate, while

\[
 b=o(W/m)                                               \tag{6.10}
\]

is the weighted-floor rate.  Merely asserting `b=o(W/H)` is insufficient
unless the crossing shadows are certified or already included in the
actual deficit.

## 7. Residual cycles should normally be retained

Suppose the post-recoupling exact factor consists of `K` main cycles and
`z` additional legal residual cycles `R_1,...,R_z`, with owner masses
`r_1,...,r_z`.  There are two factor-blind choices.

1. Retain residual cycle `R_i`; its exact full-collar charge is `2H`.
2. Delete it; its middle leave cancels from the baseline, and its
   floor-buffer shadow charge is at most `2r_iS_H`.

Choosing independently gives

\[
 \boxed{\begin{aligned}
 \nu(2m)\le{}&W+2HK+J_H(F)
 +2\sum_{i=1}^z\min\{H,r_iS_H\}\\
 &+L_m(m-H-1).
 \end{aligned}}                                        \tag{7.1}
\]

In the direct-support ledger, replace `J_H` and every deletion certificate
by the actual resulting deficit.

If every main and residual cycle has length at least `2ell`, retaining all
cycles gives

\[
 2H(K+z)\le\frac H\ell W.                              \tag{7.2}
\]

Thus `H/ell->0` makes even a linear residual owner mass harmless.  More
generally the exact residual-cycle requirement is

\[
                              Hz=o(W).                  \tag{7.3}
\]

If deletion is forced, total residual owner mass `r=sum_i r_i` is harmless
under `r=o(W/sqrt(m))` with floor balance, or under `r=o(W/H)` using only
raw support.

In particular, suppose an Ordered-Hall or successor-cover theorem supplies
a defect number `Delta` for which the residual cycles have total owner mass
at most `Delta` and count `z`.  The exact factor-blind residual term may be
taken to be

\[
                         2\min\{Hz,\ \Delta S_H\}.      \tag{7.3a}
\]

This is the only way the routing defect enters the exterior interface; no
shape or frame information about the residual cycles is used.

If a tensor construction instead outputs `p` delay-`H` safe open path
remnants and `z` safe closed cycles covering `W-u` owners, Lemma 3.1 gives
the exact direct-support bound

\[
 \boxed{
 \nu(2m)\le
 W+Hp+2Hz+D_H^{\rm actual}+L_m(m-H-1).}                \tag{7.4}
\]

Here `D_H^(actual)` is computed only from the surviving internal path
windows and the cyclic windows of the retained cycles.  Equation (7.4)
does not silently assume that a broken boundary remains certified.

## 8. Odd alternating `X/Y` cycle interface

This is the form directly compatible with an exact middle-level tensor
factor on `n=2m+1` coordinates.  Put

\[
 W=\binom{2m+1}m,
 \qquad
 N_q=\binom{2m+1}{m-q}
     =\binom{2m+1}{m+1+q},
 \qquad
 c_q=\left\lfloor\frac W{N_q}\right\rfloor.           \tag{8.1}
\]

Encode an alternating middle-level cycle by a cyclic `m`-set sequence
`(X_i)` such that

\[
                              Y_i=X_i\cup X_{i+1}.      \tag{8.2}
\]

An exact `X/Y` cycle factor means that the `X_i` occurrences partition rank
`m` and the `Y_i` occurrences partition rank `m+1`.

At depth `q`, define

\[
 L_{i,q}=\bigcap_{j=0}^qX_{i+j},
 \qquad
 U_{i,q}=\bigcup_{j=0}^{q+1}X_{i+j}.                  \tag{8.3}
\]

The lower target has rank `m-q`, while the upper target has rank
`m+1+q`.  Assume every `H+1` consecutive cyclic transitions form a Johnson
geodesic.  Lemma 3.1 with delay `H` represents all lower intersections.
Its union identity (3.5) is unrestricted in interval length, so it also
represents the `H+2`-state upper window at `q=H`.

After cutting a cycle, copy `H+1` prefix states to preserve every upper
wraparound window.  The resulting linear row has `lambda+H+1` states, and
the delay factor adds `H` more letters.  Hence the exact full-collar cycle
cost is

\[
                              \lambda+2H+1.             \tag{8.4}
\]

This `2H+1` constant is not an off-by-one: the extra copied state is needed
on the upper side, whereas the factor delay remains `H`.

For the two signed histograms at `1<=q<=H`, define `O_q^pm`, `J_H`, and
`S_H` exactly as in (5.2)--(5.3).

### Theorem 8.1 (full-collar odd tensor interface)

After arbitrary exact, `H`-safe mixed-frame recoupling, delete complete
alternating cycles of total `X`-owner mass `r` and retain `K` cycles.  Then

\[
 \boxed{
 \nu(2m+1)\le
 W+(2H+1)K+r+J_H(F)+2rS_H
 +2L_m(m-H-1).}                                        \tag{8.5}
\]

The exact direct-support version replaces `J_H+2rS_H` by the actual total
lower and upper holes at depths `1,...,H`.

#### Proof

The retained factor words have length

\[
                         (W-r)+(2H+1)K.                 \tag{8.6}
\]

Deleting whole alternating cycles removes `r` distinct rank-`m` owners and
`r` distinct rank-`m+1` owners.  Appending both middle shores costs `2r`,
so the baseline becomes

\[
                         W+(2H+1)K+r.                  \tag{8.7}
\]

At each positive depth and sign, deletion removes exactly `r` occurrences.
Lemma 5.1 bounds all remaining holes by

\[
 \sum_{q=1}^H(M_q^-+M_q^+)
 \le J_H(F)+2rS_H.                                     \tag{8.8}
\]

Append those holes and the odd product-SCD word.  \(\square\)

The extra `+r`, absent in even dimension, is necessary in this literal
ledger because both middle shores must be repaired.

For odd ranks,

\[
 \boxed{
 S_H\le\frac{2\cdot4^m}{W}-2
       =(\sqrt\pi+o(1))\sqrt m.}                      \tag{8.9}
\]

Indeed `1/c_q<=2N_q/W` and
`sum_(q=1)^m N_q=4^m-W`.

### Theorem 8.2 (exact odd partial collars)

Choose `0<=sigma_C<=H+1` copied prefix states on each retained cycle.  Its
factor seam is `H+sigma_C`.  At depth `q`, the exact unavailable counts are

\[
 (q-\sigma_C)_+
 \quad\hbox{on the lower side},
 \qquad
 (q+1-\sigma_C)_+
 \quad\hbox{on the upper side}.                         \tag{8.10}
\]

Let `z_0` be the number of cycles with `sigma_C=0`; each such bare cut also
loses its wraparound `Y` owner.  Then

\[
 \boxed{\begin{aligned}
 \nu(2m+1)\le{}&
 W+\sum_C(H+\sigma_C)+r+z_0+J_H(F)\\
 &+\sum_{q=1}^H\frac{
 2r+\sum_C\bigl((q-\sigma_C)_+
                 +(q+1-\sigma_C)_+\bigr)}{c_q}\\
 &+2L_m(m-H-1).
 \end{aligned}}                                        \tag{8.11}
\]

Full collars `sigma_C=H+1` reduce (8.11) to (8.5).  A bare odd cut loses
exactly

\[
 1+\sum_{q=1}^H(2q+1)=(H+1)^2                         \tag{8.12}
\]

raw occurrences over the two shores, including the lost middle `Y` owner.

### Corollary 8.3 (standard odd cyclic rows)

Let `n=2m+1`, `B=W/n`, and suppose every cycle row has `X`-length `n`.
Deleting `R` complete rows means `r=nR`, and Theorem 8.1 is equivalently

\[
 \boxed{\begin{aligned}
 \nu(2m+1)\le{}&
 (B-R)(n+2H+1)+J_H(F)\\
 &+2nR(1+S_H)+2L_m(m-H-1).
 \end{aligned}}                                        \tag{8.13}
\]

For a complement-symmetric wreath factor the two signed overloads are
equal, so `J_H(F)` here is twice the usual one-sided weighted overload.
Thus (8.13) is exactly the standard arbitrary-row deletion interface, now
seen as a specialization of the mixed-cycle theorem.

### Corollary 8.4 (odd cycle/path remnants, actual-deficit form)

Let `p` delay-`H` safe open `X`-paths and `z` cyclically safe closed
`X/Y` cycles be pairwise owner-disjoint and cover `W-u` rank-`m` owners.
Let `M_0^+` be the actual number of rank-`m+1` targets not represented by
the internal path edges or cyclic edges, and for `q>=1` let `M_q^pm` be the
actual signed deficits of the surviving windows.  Then

\[
 \boxed{\begin{aligned}
 \nu(2m+1)\le{}&W+Hp+(2H+1)z+M_0^+\\
 &+\sum_{q=1}^H(M_q^-+M_q^+)
 +2L_m(m-H-1).
 \end{aligned}}                                        \tag{8.14}
\]

#### Proof

Lemma 3.1 gives `v+H` factor letters for an open path, while (8.4) gives
`v+2H+1` for a closed cycle.  Their total base is

\[
                         (W-u)+Hp+(2H+1)z.             \tag{8.15}
\]

Append the `u` omitted rank-`m` owners, the actual missing upper-middle
targets, the positive-depth holes, and the odd exterior word.  \(\square\)

If the paths arise by making `p` bare cuts in a pre-cut exact cycle factor
without deleting `X` owners, then `M_0^+<=p`.  Hence their baseline seam is
at most `(H+1)p`; their full raw cut ledger through depth `H` is
`(H+1)^2p`.  Transferring a balanced pre-cut estimate instead costs
`O(mp)`.  Thus path remnants must use (8.14) or these explicit cut charges;
they are not covered silently by the complete-cycle deletion theorem.

## 9. Odd recoupling moment and residual cycles

Suppose two exact odd `X/Y` factors have successor maps differing at `s`
directed `X` positions.  A lower depth-`q` window uses `q` transitions and
an upper depth-`q` window uses `q+1`.  The same `L^1` argument as in
Section 6 gives

\[
 J_H(F')\le J_H(F)
 +s\sum_{q=1}^H\frac{2q+1}{c_q}.                       \tag{9.1}
\]

The exact odd binomial moment is

\[
 \sum_{q=1}^{m}(2q+1)\binom{2m+1}{m-q}
 =m\binom{2m+1}m.                                      \tag{9.2}
\]

Indeed, with `k=m-q` and `n=2m+1`,

\[
 (2q+1)\binom nk=(n-2k)\binom nk
 =n\left(\binom{n-1}k-\binom{n-1}{k-1}\right).        \tag{9.2a}
\]

Summing over `0<=k<m` telescopes to
`n binomial(2m,m-1)=m binomial(2m+1,m)`.

Using `1/c_q<=2N_q/W`,

\[
 \boxed{
 \sum_{q=1}^H\frac{2q+1}{c_q}\le2m}
 \qquad
 J_H(F')\le J_H(F)+2ms.                                \tag{9.3}
\]

Thus `s=o(W/m)` transfers an `o(W)` overload bound across arbitrary choices
of recoupled junctions, provided the resulting cycles are physically
`H`-safe.  Direct measurement of the post-recoupling `J_H` removes this
term.

If an odd recoupling junction is not `H`-safe and is cut bare, it adds `H`
factor letters and loses one middle `Y` owner together with `2q+1` signed
positive-depth occurrences at depth `q`.  Its exact raw repair ceiling is
therefore `(H+1)^2`, as in (8.12).  With balanced floors, the q-zero loss
plus (9.3) is at most `(2m+1)` per cut.  Hence `b=o(W/m)` is again the
uniform weighted sufficient rate for `b` uncertified odd cuts.

If there are `z` additional legal residual `X/Y` cycles with `X`-masses
`r_i`, retaining residual cycle `i` costs `2H+1`; deleting it costs the
factor-blind ledger

\[
                         r_i+2r_iS_H.                   \tag{9.4}
\]

Thus the sharp componentwise upper choice is

\[
 \boxed{\begin{aligned}
 \nu(2m+1)\le{}&W+(2H+1)K+J_H(F)\\
 &+\sum_{i=1}^z
   \min\{2H+1,\ r_i(1+2S_H)\}\\
 &+2L_m(m-H-1),
 \end{aligned}}                                        \tag{9.5}
\]

where `K` counts the nonresidual retained cycles.

If every alternating cycle has total middle-level length `2ell`, hence
`X`-shore length `ell`, retaining all main and residual cycles gives

\[
                  (2H+1)(K+z)\le\frac{2H+1}{\ell}W.   \tag{9.6}
\]

Accordingly `H/ell->0` kills the whole cycle collar even if residual cycles
carry a linear proportion of the owners.  If only the residual-cycle count
is controlled, the exact condition is `Hz=o(W)`.  If deletion is forced,
`sum_i r_i=o(W/sqrt(m))` is sufficient.

If a successor-cover defect `Delta` bounds the total residual `X`-owner
mass and `z` bounds the residual-cycle count, the odd residual term is

\[
 \min\{(2H+1)z,\ \Delta(1+2S_H)\}.                     \tag{9.7}
\]

Again this depends only on the two scalar defect ledgers, not on the
recoupling frames.

## 10. Constant-one corollaries

### Corollary 10.1 (even tensor architecture)

Let `H=H_m` and `ell=ell_m`.  Suppose a mixed-frame construction, after all
recoupling and before deletion, produces an exact cyclic factor in
`Q_(2m)` such that:

1. every cycle of this pre-deletion factor, including every cycle later
   deleted, is cyclically delay-`H` safe;
2. every main cycle has length at least `2ell`;
3. its post-recoupling, pre-deletion weighted overload satisfies
   `J_H=o(W)`;
4. an arbitrary union of complete residual cycles, of total owner mass
   `r=o(W/sqrt(m))`, is deleted; and
5. retained short residual cycles have count `z=o(W/H)`.

If

\[
 \frac H{\sqrt m}\longrightarrow\infty,
 \qquad
 \frac H\ell\longrightarrow0,                          \tag{10.1}
\]

then

\[
                         \nu(2m)\le W+o(W).             \tag{10.2}
\]

If `J_H` is known only before changing `s` successor positions, add the
sufficient condition `s=o(W/m)`.

#### Proof

The main collars are at most `(H/ell)W=o(W)` by (7.2); short residual
collars are `o(W)` by hypothesis.  Lemma 5.2 makes the deletion term
`O(r sqrt(m))=o(W)`, while `J_H=o(W)`.  Theorem 1.3 makes the exterior word
`o(W)`.  Substitute in Theorem 5.3 or (7.1).  \(\square\)

### Corollary 10.2 (odd `X/Y` tensor architecture)

Under the odd analogues of the preceding hypotheses—exactness and `J_H`
measured after recoupling and before deletion, every cycle in that factor
`H`-safe, and deletion restricted to complete alternating cycles—with cycle
`X`-length at least `ell`, one has

\[
 \frac H{\sqrt m}\to\infty,qquad
 \frac H\ell\to0,qquad
 J_H=o(W),qquad
 r=o(W/\sqrt m),qquad
 Hz=o(W)
 \quad\Longrightarrow\quad
 \nu(2m+1)\le W+o(W).                                  \tag{10.3}
\]

Again `s=o(W/m)` suffices if the overload estimate is transferred from a
pre-recoupling factor.

#### Proof

Use (8.5), (8.9), (9.3), (9.6), and the odd half of Theorem 1.3.  The
additional odd middle-leave term `r` is already `o(W)` under
`r=o(W/sqrt(m))`.  \(\square\)

### Corollary 10.3 (actual-deficit form)

The overload hypotheses in Corollaries 10.1--10.2 may be replaced by the
strictly more direct condition that the actual post-deletion central repair
family is `o(W)` and that the compiled central word has length `W+o(W)`.
For the odd theorem this repair family includes both missing middle shores,
so it automatically detects the extra `+r` in (8.5).  In that black-box
form, no pre-deletion balance, recoupling count, or separate deletion-rate
hypothesis is logically required.  Those quantities are only uniform
sufficient certificates for the two actual conditions.

## 11. Fixed-window diagonalization

At a fixed Gaussian window `H_A=ceil(A sqrt(m))`, (0.4) gives only a
constant depending on `A`; the exterior word is not yet `o(W)` when `A` is
fixed.  Suppose the central tensor estimates hold for every fixed integer
`A`, with normalized error `epsilon_A(m)->0` as `m->infinity`.  Choose
thresholds `M_A` so that `epsilon_A(m)<=1/A` for `m>=M_A`, and then choose a
slow integer function `A=A(m)->infinity` with `m>=M_(A(m))` and all seam,
leave, and local-geodesicity scale restrictions still valid.  Put

\[
                         H_m=\lceil A(m)\sqrt m\rceil.  \tag{11.1}
\]

Then the central error is `o(W)` and Theorem 1.3 gives

\[
 \frac{\text{tail}}W
 \le C_0e^{-A(m)^2/8}=o(1).                            \tag{11.2}
\]

Thus the theorem plugs directly into a fixed-window tensor construction;
no uniform-in-growing-`A` central theorem is needed.

## 12. Exact implication boundary and independent audit

The following statements are proved.

1. The product-SCD word literally covers both exterior tails at the exact
   charges `L_m(m-H-1)` in even dimension and `2L_m(m-H-1)` in odd
   dimension.
2. Its normalized charge is at most `C_0 exp(-H^2/(8m))` for every
   `0<=H<=m-1`; `H/sqrt(m)->infinity` is sufficient without an upper
   moderate-deviation hypothesis.
3. The product-tail concatenation seam costs exactly zero.
4. Mixed frames themselves cost nothing.  The post-recoupling state
   sequences need only satisfy the stated local geodesicity condition.
5. Full cycle collars cost exactly `2H` in even dimension and `2H+1` for
   odd alternating `X/Y` cycles.
6. A legal residual cycle can be retained independently; no global fusion
   is needed.
7. The literal middle leave cancels in even dimension.  In odd dimension,
   deleting `r` alternating-cycle owners leaves the necessary extra `+r`
   because both middle shores are lost.
8. For a fully `H`-safe pre-deletion factor, balanced floors reduce an
   arbitrary whole-cycle deletion from the crude `O(Hr)` shadow charge to
   `O(r sqrt(m))`.
9. A recoupling estimate transferred across `s` changed successors incurs
   at most `2ms`; direct post-recoupling measurement incurs none.

The following statements are not proved and must not be inferred.

1. Exact middle ownership does not imply `D_H=o(W)` or `J_H=o(W)`.
2. A frame-changing Johnson edge is not automatically delay-`H` safe.
3. An `o(W/H)` number of uncertified cuts is not enough in the raw ledger;
   their factor-blind cost is quadratic in `H` per cut.
4. The product tail repairs no target inside the mesoscopic core and proves
   no MWB, owner synchronization, or cycle-rounding theorem.
5. The deletion rates above are sufficient, not necessary.  Larger
   structured leaves are permitted whenever their actual central deficit is
   `o(W)`.

The decisive constants and off-by-one points were independently audited:

* the factor `2` in (0.3) already covers both even tails;
* the odd lift is the only second doubling;
* the even full collar is `2H`;
* the odd full collar is `2H+1`, because (3.5) is unrestricted for unions;
* a bare even cut loses `H(H+1)` signed occurrences;
* a bare odd cut loses `(H+1)^2`, including its wraparound `Y` owner;
* `S_H=O(sqrt(m))` and both recoupling moments are `O(m)` uniformly in
  `H`.

Therefore the product-SCD tail/leave gate is closed in a form ready for the
tensor architecture.  The sole nonexternal input still required is a
post-recoupling simultaneous central-shadow estimate.


<!-- END COMPLETE SOURCE 27 -->


---

<a id="document-28"></a>

## Document 28: MATH_AUDIT_PBBS_SUBROOT_BAND_AND_PRODUCT_SCD_QUANTIFIER_20260726.md

Source: `/Users/amir.nuriyev/Documents/problem/MATH_AUDIT_PBBS_SUBROOT_BAND_AND_PRODUCT_SCD_QUANTIFIER_20260726.md`

[Portable document](sources/essential/project/MATH_AUDIT_PBBS_SUBROOT_BAND_AND_PRODUCT_SCD_QUANTIFIER_20260726.md) · [Exact original](originals/project/MATH_AUDIT_PBBS_SUBROOT_BAND_AND_PRODUCT_SCD_QUANTIFIER_20260726.md)

<!-- BEGIN COMPLETE SOURCE 28 -->

# PBBS sub-Gaussian band and the product-SCD quantifier

Date: 2026-07-26

## Verdict

Two separate assertions must not be conflated.

1. The present PBBS compiler already gives an unconditional
   \((1+o(1))W\)-length literal word for every paired central band of
   half-width

   \[
      h=o(\sqrt m).
   \]

2. A separately appended exterior-tail word cannot have length \(o(W)\)
   at a fixed Gaussian cutoff \(H=A\sqrt m\), and a fortiori cannot do so
   at \(H=o(\sqrt m)\).  For a separate tail, the condition
   \(H/\sqrt m\to\infty\) is not merely an artefact of the product-SCD
   upper bound: it is forced by the boundary antichain.

Thus the sub-Gaussian PBBS theorem is a genuine unconditional advance, but
it does not overlap the product-SCD exterior construction.  Bridging the
strip between the two cutoffs requires a new reuse/strip theorem (or the
open critical little-oh improvement); changing the quantifier in the
existing tail theorem does not close it.

## 1. The unconditional PBBS estimate

Put

\[
 n=2m+1,\qquad W=\binom{2m+1}{m},\qquad
 B=\operatorname {Cat}_m={W\over n}.
\]

The audited reciprocal-height trace at the fixed window
\(H_0=\lceil\sqrt m\rceil\), followed by the deck comparison, gives

\[
 \overline\nu_{H_0}=O(B/\sqrt m),
 \qquad
 \nu_{H_0}(P_m)=O(B\sqrt m).
 \tag{1.1}
\]

Indeed

\[
 \nu_{H_0}(P_m)
 \le 2n\overline\nu_{H_0}+nZ_{H_0},
\]

and the short-cycle term satisfies \(nZ_{H_0}=o(B)\).  Since the residence
packing number is monotone in the cutoff,

\[
 \boxed{\nu_H(P_m)=O(B\sqrt m)\quad(1\le H\le\sqrt m).}
 \tag{1.2}
\]

The linear dominance-seam compiler is unconditional and says

\[
 L_H\le W+2HB+2(5H-1)\nu_H(P_m),                 \tag{1.3}
\]

provided \(2H\le m+1\).  Combining (1.2)--(1.3), uniformly for
\(H\le\sqrt m\),

\[
 \boxed{
 {L_H\over W}
 \le 1+O(H/m)+O(H/\sqrt m).
 }
 \tag{1.4}
\]

Consequently \(H=o(\sqrt m)\) gives \(L_H=(1+o(1))W\).

The compiler with parameter \(H\) covers ranks

\[
 m-H+1,m-H+2,\ldots,m+H+1.                       \tag{1.5}
\]

There is a harmless one-rank asymmetry in (1.5).  In the usual paired
notation, for any integer \(h=o(\sqrt m)\), apply (1.4) with \(H=h+1\).
It gives a word of length \((1+o(1))W\) covering every target in

\[
 \boxed{
 \bigcup_{q=0}^{h}
 \left(
   \binom{[2m+1]}{m-q}
   \cup
   \binom{[2m+1]}{m+1+q}
 \right).
 }
 \tag{1.6}
\]

The word actually covers one additional upper rank.  The standard
one-coordinate lift transfers the same \((1+o(1))\) statement to the
opposite parity, with only the corresponding endpoint shift.

This is a central-band theorem, not yet the full constant-one theorem.

## 2. Why a separate fixed-\(A\) tail cannot be negligible

We use the elementary antichain lower bound for literal words.

### Lemma 2.1 (one endpoint per antichain member)

If a linear literal word of length \(L\) covers every member of an
antichain \(\mathcal A\), then \(L\ge|\mathcal A|\).

#### Proof

Choose one witnessing interval for every member of \(\mathcal A\) and
map it to its right endpoint.  The unions of intervals with a common
right endpoint are nested as the left endpoint moves.  Thus two distinct
incomparable targets cannot have the same right endpoint.  The map is
injective. \(\square\)

In even dimension, the product-SCD exterior word at central cutoff \(H\)
covers, in particular, the whole rank

\[
 r=m-H-1.
\]

Hence every such separate exterior word has length at least

\[
 \binom{2m}{m-H-1}.                                \tag{2.1}
\]

Writing \(k=H+1\),

\[
 {\binom{2m}{m-k}\over\binom{2m}{m}}
 =\prod_{j=0}^{k-1}{m-j\over m+j+1},              \tag{2.2}
\]

and, uniformly for \(k=O(\sqrt m)\),

\[
 \log {\binom{2m}{m-k}\over\binom{2m}{m}}
 =-{k^2\over m}+O(k^3/m^2).                       \tag{2.3}
\]

Therefore, if \(H=A\sqrt m+O(1)\) with fixed \(A\),

\[
 \boxed{
 L_{\rm tail}\ge(e^{-A^2+o(1)})\binom{2m}{m}.
 }
 \tag{2.4}
\]

If \(H=o(\sqrt m)\), the lower bound is \((1-o(1))\binom{2m}{m}\).
The odd-dimensional boundary rank gives the same conclusion, using

\[
 {\binom{2m+1}{m-H}\over\binom{2m+1}{m}}
 =e^{-H(H+1)/m+o(1)}
\]

in the Gaussian range.

The proved product-SCD estimate

\[
 {L_m(m-H-1)\over\binom{2m}{m}}
 \le C_0e^{-H^2/(8m)}                              \tag{2.5}
\]

is therefore correctly quantified:

* fixed \(A\) gives only an \(O_A(W)\) exterior word, and (2.4) shows its
  cost cannot be \(o(W)\);
* \(A\to0\) is worse, with a tail cost at least \((1-o(1))W\);
* \(H/\sqrt m\to\infty\) makes (2.5) \(o(W)\), and the boundary-rank
  lower bound shows that this Gaussian escape is essentially necessary
  for any **separately appended** exterior word.

## 3. Exact remaining gap

The unconditional PBBS word ends at a cutoff \(h=o(\sqrt m)\).  The
factor-blind tail becomes negligible only at a cutoff
\(H=\sqrt m\,\omega(1)\).  Hence these two existing mechanisms leave the
mesoscopic strip

\[
 h<q<H.                                             \tag{3.1}
\]

No choice of a fixed Gaussian constant removes (3.1).  The live options
are therefore:

1. prove the critical residence improvement that lets the PBBS compiler
   reach \(H=\sqrt m\,\omega(1)\);
2. recycle the PBBS baseline nonlocally across the mesoscopic strip; or
3. prove the independent integral fine-strip/owner-recycling theorem.

The standard parity lift and the product-SCD concatenation introduce no
additional obstruction once one of these strip interfaces is supplied.


<!-- END COMPLETE SOURCE 28 -->


---

<a id="document-29"></a>

## Document 29: PBBS_K17_FINITE_COMPILER_LEDGER_20260908.md

Source: `/Users/amir.nuriyev/Documents/problem/scratch/PBBS_K17_FINITE_COMPILER_LEDGER_20260908.md`

[Portable document](sources/essential/project/scratch/PBBS_K17_FINITE_COMPILER_LEDGER_20260908.md) · [Exact original](originals/project/scratch/PBBS_K17_FINITE_COMPILER_LEDGER_20260908.md)

<!-- BEGIN COMPLETE SOURCE 29 -->

# Finite PBBS compiler ledger at k=17

2026-09-08. One tiny exact binomial evaluation executed remotely through
`ssh h100`; reported remote hostname: `arboghast`. No PBBS factor enumeration,
packing computation, or word search was performed. No mathematical code was
executed on the Mac.

The published compiler ledger in
`PBBS_ABUNDANCE_TO_COEFFICIENT_ONE_VERIFIED_COMPILER_CHAIN_20260908.md`,
equation (11), is

    B(r,H) = W_r + 2H Cat_r
             + 2(5H-1) P(T<=H-1) + 2L_r(r-H).

At k=17, r=8, W_r=24310, Cat_r=1430, and the admissible positive integer
depths under 2H<=r+1 are H=1,2,3,4. The known comparison word has length
25745.

The exact evaluations, setting the nonnegative packing term to zero, are:

| H | 2H Cat_8 | L_8(8-H) | 2L_8(8-H) | Packing coefficient | B(8,H) with P=0 | Excess over 25745 |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2860 | 35308 | 70616 | 8 | 97786 | 72041 |
| 2 | 5720 | 32172 | 64344 | 18 | 94374 | 68629 |
| 3 | 8580 | 24108 | 48216 | 28 | 81106 | 55361 |
| 4 | 11440 | 13580 | 27160 | 38 | 62910 | 37165 |

Thus none of these four instances of this ledger can certify a word shorter
than 25745, even if its packing number were zero. Already the baseline plus
collar term is at least 24310+2860=27170>25745 for every admissible H, so the
tail evaluation is supplementary and no packing enumeration is necessary.

These are lower bounds on the numerical right-hand side of a sufficient
upper-bound ledger. They are not lower bounds on all complete words, nor
lower bounds on the actual length of every word made by a more economical
implementation of the construction. They rule out improving the known
k=17 word using this published ledger alone. The proposed asymptotic
coefficient-one proof does not supply an effective k=17 improvement.

## Exact remote evaluation provenance

The following Python body was supplied once to `ssh h100 'python3 -'` by
heredoc. It uses the exact tail formula from equation (11)'s source.

```python
from math import comb
import socket
r = 8
W = comb(2*r+1, r)
cat = comb(2*r,r)//(r+1)

def C(t):
    return 0 if t < 0 else comb(r, min(t,r//2))

def L(s):
    return 2*sum((comb(r,a)-(comb(r,a-1) if a else 0))*(r if a == 0 else r-2*a+1)*C(s-a) for a in range(r//2+1))

print('Remote host:', socket.gethostname())
print('r=',r,'W=',W,'Cat_r=',cat,sep='')
print('H | collar | L_r(r-H) | odd_tail=2L | packing_coefficient | ledger_with_P=0 | excess_over_25745')
for H in range(1,5):
    collar=2*H*cat
    tail=2*L(r-H)
    val=W+collar+tail
    print(H,collar,L(r-H),tail,2*(5*H-1),val,val-25745,sep=' | ')
```


<!-- END COMPLETE SOURCE 29 -->


---

<a id="document-30"></a>

## Document 30: pbbs_finite_layer_zero_triangle_incidence_fibre.md

Source: `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_finite_layer_zero_triangle_incidence_fibre.md`

[Portable document](sources/essential/c69c/research_round1/pbbs_finite_layer_zero_triangle_incidence_fibre.md) · [Exact original](originals/c69c/research_round1/pbbs_finite_layer_zero_triangle_incidence_fibre.md)

<!-- BEGIN COMPLETE SOURCE 30 -->

# The finite-layer zero-triangle incidence fibre

2026-09-08. Pure proof; no computation. This note conditions the BASE
birth on finitely many original triangle rows and identifies its exact
remaining fibre. Shifted partner births retain their original F_0
membership; no shifted zero-triangle gate is added.

Complete-file reviews by the worktree lead and independent recency
reader pass. The coordinator has accepted the lemma after its own
full read and independent reverse-clock and incidence audit.

## 1. Original arrays and the safe profile domain

Fix r, H=floor(c sqrt(r))<r, and the original top-row-zero family

    F_0={GOOD, T<=H, Z_(0,0)=0},
    mu_0=E[(T+2)1_(F_0)].

The incidence assertions assume mu_0>0, as holds for all sufficiently
large r at fixed c by the accepted mu_0=Theta_c(1) bound. If mu_0=0,
there is no F_0 incidence to condition; the deterministic clock identity
below remains valid.

GOOD here is the accepted PROFILE-MEASURABLE condition. Write
D_s=partial^s D, r_s=ups(D_s), h=ht(D), and

    p_s=2r_(s+1)+1,
    ell_s=r_s-2r_(s+1)+r_(s+2).

Conditional on a complete feasible pruning profile, the original rows
Z_s are independent uniform weak compositions of ell_s into p_s parts.
The row labels are persistent original particle labels, and their
canonical initial selected label is zero. For a deterministic S>=1, put

    F_S=sum_(s=0)^(S-1) sum_(u=0)^s Z_(s,-u).          (1)

All indices in (1) are cyclic. In the exact fibre argument below, fix a
full profile satisfying

    h>=2S,
    p_s>2H+1 and p_s>=2(s+1)            for 0<=s<S.  (2)

Thus all queried cores are nonempty and the s+1 triangle coordinates in
row s are distinct. In particular p_s-s-1>=1. Fix also every original
row with index at least S. These rows reconstruct the ORIGINAL root D_S
uniquely. They do not determine the remaining coordinates in rows s<S.

## 2. The candidate clock uses only D_S

At any PBBS level, a C clock runs to the next selection of the physical
predecessor of the currently selected label; its length is even. A T
clock runs to the next selection of the same label; its length is odd.
Their usual numerical lengths are 2C and 2T+1, respectively.

Starting at time zero in the fixed-site process of D_S, concatenate
exactly S C clocks and then one T clock. More explicitly, let t_0=0;
the ith C clock ends at the first later selection of label -i, for
i=1,...,S. After t_S, end the final T clock at the next selection of
label -S. Set

    G_S^*=t_(S+1),       T_S^*=(G_S^*-1)/2.           (3)

Every clock is taken at its actual chronological reached phase of this
ONE original D_S trajectory. There is no reinitialization between
clocks. G_S^* is finite and odd, and is a function only of D_S, hence
only of the full profile and rows with index at least S.

The reduced height is h-S. Since each C length is at least two and the
last T length is at least 2(h-S)+1, one also has

    G_S^*>=2h+1,       T_S^*>=h.                     (4)

## 3. Both directions of the clock identity

The exact one-level partition at a node with incoming coordinate z is

    C parent -> C child followed by 2z T children,
    T parent -> C child followed by 2z+1 T children.   (5)

The children are adjacent chronological intervals in the same reduced
trajectory. Before the first spatial wrap, (5) identifies the actual
parent clocks. At z=0 it reduces to

    C -> C,                  T -> C T.              (6)

The original chronological row-s query order is 0,-1,-2,...: every
completed row-s node has one child C, which moves the selected label
at level s+1 by -1, followed only by T clocks, which leave that selected
label unchanged at their endpoints. Every level initially has label
zero. This proves the query order without using any unqueried row
coordinate or any guessed physical shift at another level.

FORWARD DIRECTION. Suppose an upper-array completion satisfies F_S=0
and T(D)<=H. Its outer physical horizon G=2T(D)+1 is at most 2H+1,
strictly below all the circumferences required by (2). Starting from
one T node, (6) gives the exact depth-s clock word

    C^s T,

by induction for 0<=s<=S. At depth s<S this word queries precisely
0,-1,...,-s, all zero by (1). Consequently its depth-S word is the
candidate word in (3), with the same initial root and the same successive
physical phases. Its total duration is unchanged by partitioning:

    G=G_S^*,       T(D)=T_S^*.                       (7)

In particular, if the fixed deeper environment has G_S^*>2H+1, NO
upper-array completion with F_S=0 can have T<=H. This conclusion does
not require first defining an untruncated parent genealogy for a long
completion.

CONVERSE DIRECTION. Suppose G_S^*<=2H+1 and take ANY upper-array
completion whose triangle coordinates are all zero. Start with the
candidate depth-S chronological word C^S T and group it as

    C^(S-1) (C T).

Each initial singleton C lifts through (6) to a parent C, and the final
pair C T lifts to a parent T. At row S-1, the successive queried
original labels are 0,-1,...,-(S-1), all zero. The phase of each group
is its actual left endpoint in the same reduced trajectory; completion
of a group changes that reduced selected label by exactly -1.

These lifts are actual clocks: their entire candidate horizon is at most
2H+1, strictly below p_(S-1), and a fortiori below the parent
circumference. Thus neither a full-lap same-site return nor the
same-particle lap to the predecessor can precede the specified hit.
For the even C intervals, their lengths are also strictly smaller than
the odd total G_S^*, so the possible circumference-minus-one alternative
is excluded. This is the one-level no-wrap justification for using (6)
in reverse, not an assumption that a long parent has the same clock.

We have obtained the actual parent word C^(S-1)T with the SAME total
duration. Repeat this grouping at rows S-2,...,0. At every row s the
needed labels are exactly 0,-1,...,-s, and (2) supplies the same horizon
bound. The final result is the actual outer T clock of duration G_S^*.
Therefore T(D)=T_S^*<=H for every such completion.

Combining both directions, for every offset j>=0 and every upper
completion on the profile domain (2), one has the exact event identity

    {T<=H, F_S=0, j<=T+1}
      ={all Z_(s,-u)=0 for 0<=u<=s<S}
         intersect {G_S^*<=2H+1, j<=(G_S^*+1)/2}.     (8)

The second event is measurable from the fixed deeper environment.
The inclusive survival endpoint is T_S^*+1=(G_S^*+1)/2.

## 4. Exact incidence mass and the product of free fibres

Sample the ACTUAL F_0 repair-incidence law: choose a root with weight
(T+2)1_(F_0), then choose j uniformly from 0,...,T+1. After marginalizing
the uniform physical deck, every allowed pair (D,j) has the constant
probability

    1/(Cat_r mu_0).                                  (9)

The lifetime weight cancels exactly against the offset choice. We do
not assign the original unweighted law to the remaining environment.

Fix an environment E=(R,y,j), where R is the entire profile satisfying
(2), y comprises ALL original rows with index at least S, and j>=0.
Call it feasible if R is GOOD and

    G_S^*(y)<=2H+1,       j<=(G_S^*(y)+1)/2.          (10)

On F_S=0 the top-row condition Z_(0,0)=0 is automatic. Formula (8)
shows that (10) is the complete remaining base-lifetime and survival
test. Every choice of the unforced coordinates is then admissible.
In row s<S, there are exactly

    q_s^free=p_s-s-1

unforced coordinates, and their sum is ell_s. Its number of completions
is therefore

    M_s=binom(ell_s+p_s-s-2,p_s-s-2).                 (11)

This includes ell_s=0. Since the original inverse-array encoding is
bijective, the number of upper completions of a feasible E is exactly
the product of these M_s. Consequently its joint mass under the
ORIGINAL F_0 incidence law is

    P_inc,0(E=(R,y,j), F_S=0)
      =1_(E feasible)/(Cat_r mu_0) product_(s<S) M_s.  (12)

Profiles outside (2) are outside this formula's stated domain. For a
nonfeasible environment within (2), the joint mass is zero, so there
is no conditional fibre law to assign.

For every positive-mass feasible environment, (9)-(12) prove that,
conditional on E and F_S=0, the original rows s<S are independent;
in row s its triangle entries are fixed at zero, and its remaining
entries are a uniform weak composition of ell_s into p_s-s-1 parts.
No residual lifetime weighting, mixture, or constraint on the free
entries remains. The distribution of E itself is still the actual
incidence distribution in (12).

## 5. The safe zero-triangle restriction has asymptotically full mass

This section uses the accepted quantitative original-profile envelope
and uniform early-triangle estimate. Put R=sqrt(r). Their inputs are:

* A profile-measurable a>=1 satisfies
  P(a>t)<=C exp(-b t^2), with an adjustment of C for bounded t.
* A=a+sqrt(log(a+2))<=3a and L=floor(kappa_c R/A).
* If L>=2, the profile has h>2L and satisfies all physical/query safety
  inequalities in (2) for S<=L.
* Uniformly in the original profile,

      E[(T+2)1{T<=H} | profile]<=C_c A exp(C_c A).

* mu_0 is bounded above and below by positive constants depending on c.
* For deterministic 1<=S<=R,

      E[(T+2)1{T<=H,F_S>0}]<=C_c S^2/r.              (13)

These are original-profile and original-incidence statements. In
particular the same a has a uniform subGaussian upper tail under the
ACTUAL F_0 incidence law. Indeed, using A<=3a, the raw bound and the
positive lower bound on mu_0 give

    P_inc,0(a>t)
      <=C_c E[a exp(C_c a)1{a>t}]
      <=C_c (E[a^2 exp(2C_c a)])^(1/2) P(a>t)^(1/2)
      <=C_c exp(-b_c t^2).                           (14)

The exponential moment is finite by the original subGaussian tail;
the constants are uniform in r. Bounded t is again absorbed into C_c.

Set M=max(S,2). If L<M, then A>kappa_c R/M, hence
a>kappa_c R/(3M)>=kappa_c R/(6S). Formula (14) yields, for every
deterministic 1<=S<=R,

    P_inc,0(L<max(S,2))<=C_c exp(-b_c r/S^2).         (15)

Dividing (13) by mu_0 gives

    P_inc,0(F_S>0)<=C_c S^2/r.                       (16)

Thus the actual F_0 incidence law assigns probability at least

    1-C_c S^2/r-C_c exp(-b_c r/S^2)                  (17)

to the base event {F_S=0, L>=max(S,2)}. In particular this probability
tends to one for every deterministic S=o(sqrt(r)). On this event the
profile domain (2) holds, so Sections 2-4 apply without a new law at a
reached root.

## 6. Scope and conditioning guard

The exact product in Section 4 is a BASE conditioning statement. A
shifted partner contributes precisely when it belongs to the original
family F_0 and its repair interval covers the sampled edge. No partner
is required to satisfy a shifted F_S=0 event. Its test must still be
evaluated through the original arrays and the exact physical cocycles.

Likewise the exact uniform compositions are not additionally conditioned
on a maximum-gap event. Such an event can be proved to have high
probability under this law or its complement bounded separately; adding
it as a conditioning restriction changes the exact product fibre. The
profile-only nature of GOOD and of the safety conditions is essential
to the formula as written.

This lemma does not prove that many shifted labels pass their virtual
lifetime cutoff, and gives no occupied-support or packing conclusion.

Sources: pbbs_gaussian_clock_genealogy_structural_audit.md, especially
its exact clock partition and deterministic original-slot query order;
the original incidence-window constant-atom identity;
pbbs_uniform_early_triangle_incidence.md; and the accepted bounded
Gaussian short-incidence envelope and top-row-zero reduction.


<!-- END COMPLETE SOURCE 30 -->


---

<a id="document-31"></a>

## Document 31: pbbs_uniform_early_triangle_incidence.md

Source: `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_uniform_early_triangle_incidence.md`

[Portable document](sources/essential/c69c/research_round1/pbbs_uniform_early_triangle_incidence.md) · [Exact original](originals/c69c/research_round1/pbbs_uniform_early_triangle_incidence.md)

<!-- BEGIN COMPLETE SOURCE 31 -->

# Uniform early original-triangle birth and incidence bounds

2026-09-08. Pure proof; no computation or original-project edits.
This is the next derived corollary of the complete root-envelope proof,
fully read and passed by the worktree lead and independent Gaussian
reader. The coordinator has accepted Sections 1-8
of the root envelope theorem. The early-triangle corollary itself is
under separate coordinator review.

The precursor is task08's read-only note
`/Users/amir.nuriyev/.codex/worktrees/e333/problem/research_round1/pbbs_early_branch_raw_incidence_bound.md`.
Its restricted exact path sum is retained here. The stronger depth and
averaging input is the root's read-only synthesis
`/Users/amir.nuriyev/Documents/problem/scratch/PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md`.
All laws below concern ORIGINAL roots and original pruning arrays.

## 1. Statement and a global original-triangle definition

Let r>=1, R=sqrt(r), and let D be uniform among Dyck roots of semilength
r. Fix c>0 and put H=floor(cR). Let T include the consuming update, so
a repair trace has T+2 edges. Fix a deterministic integer 1<=S<=R.

Write h for the height and r_s for the original pruning profile. Put

    p_s=2r_(s+1)+1,
    ell_s=r_s-2r_(s+1)+r_(s+2).

For 0<=s<h-1, use the actual original incoming-gap array Z_s, with its
fixed original particle indexing. At the last height-one row extend
this convention by

    p_(h-1)=1,       Z_(h-1,0)=ell_(h-1)=r_(h-1).

For s>=h set p_s=1 and Z_(s,0)=0. These are the natural one-part
composition conventions; at the height-one row the sole incoming
particle gap has length 2r_(h-1)+1. Interpret every index cyclically
modulo p_s, and define on every root

    F_S(D)=sum_(s=0)^(S-1) sum_(i=0)^s Z_(s,-i).       (1)

This global definition can repeat a slot in very short rows. The
physical interpretation below is used only where all relevant slots
are distinct; outside that sector the whole short event is bounded.

There is a constant C_c, independent of r and S, such that

    P(T<=H, F_S>0) <= C_c S^2/r^(3/2),                (2)

    E[(T+2)1{T<=H,F_S>0}] <= C_c S^2/r.              (3)

For W=(2r+1)Cat_r, the exact original-birth dictionary therefore gives

    number of physical births in this sector
        <= C_c (W/sqrt(r))(S^2/r).                   (4)

Every pairwise disjoint subfamily of their intervals or full repair
traces has cardinality at most the same bound. This is a count bound
for this specified sector, not a packing estimate for its complement.

## 2. The envelope supplies global conditional probability bounds

The root envelope is a function of the FULL original pruning profile.
It supplies a random a>=1 with uniform subGaussian upper tail and

    A=a+sqrt(log(a+2)),       1<=A<=3a.

For every fixed m>=0 and t>=0,

    E[A^m exp(tA)]<=C_(m,t),                          (5)

uniformly in r. Choose the root proof's fixed sufficiently small
kappa=kappa_c and put

    L=floor(kappa R/A).                               (6)

When L>=2, the profile has coarse bounds through 2L+1, h>2L, and all
physical-circumference and composition-prefix conditions hold at L.
Conditional on this FULL profile, the original-clock bound is

    P(T<=H | profile)<=C/L exp[C(1+H/h)].              (7)

The floor gives L>=kappa R/(2A), so H/h<=H/(2L)<=cA/kappa. Thus on
L>=2, (7) implies

    P(T<=H | profile)<=C_c A exp(C_c A)/R.            (8)

If L<2, (6) gives kappa R/A<2. The trivial probability bound one is
then at most 2A/(kappa R), so (8) holds on this sector too, after
increasing C_c. Hence (8) is GLOBAL, not restricted to typical
profiles. Multiplication by H+2 also gives

    E[(T+2)1{T<=H} | profile]<=C_c A exp(C_c A).       (9)

The constants may depend on fixed c through kappa. No growing-c
uniformity is asserted. Both (8) and (9) are conditional on the same
original profile that determines A and L.

## 3. The restricted path sum when L>=max(S,2)

On this sector, all rows s<S are above the height-one row, and their
query prefixes are distinct original slots. Define the usual exact
path weights at depth L:

    q_s=ell_s/(r_s+r_(s+2)+1),
    A_t^clock=sum_(t<s<L)(s-t)q_s,
    b_t=(t+1)q_t exp(-2A_t^clock),
    B=sum_(t<L)b_t,       B_early=sum_(t<S)b_t.

The superscript distinguishes the clock potential A_t^clock from the
profile-envelope parameter A. The accepted deterministic bounds are

    q_t<=C(t+2)ell_t/r,
    exp(-2A_t^clock)<=C((t+1)/L)^2,
    B<=C.                                             (10)

The coarse convex bounds truncate at every S<=L to give

    sum_(t<S)(t+2)^4ell_t<=CrS^2.                    (11)

For example put d_t=r_t-r_(t+1). Convexity and coarse bounds give
d_t<=Cr/(t+1)^2. One summation by parts with f_t=(t+2)^4 has final
term -f_(S-1)d_S<=0 and initial term 16d_0. Its interior terms are
at most C(t+1)^3d_t, whose sum is O(rS^2). This also covers S=1
directly by 16ell_0<=16r. Equations (10)-(11) imply

    B_early<=C S^2/L^2.                              (12)

On a valid short clock, let W_s be the actual mass queried in row s.
The exact row-count identity is

    n_s=s+1+2sum_(t<s)(s-t)W_t.

Before the first positive W_s, it gives n_s=s+1. Hence a first
positive actual row before S has a positive entry in (1). Conversely,
every actual query prefix contains the first s+1 original entries,
so positivity in (1) forces a positive actual row before S. Thus,
on this valid sector and T<=H,

    F_S>0 iff sum_(s<S)W_s>=1.                       (13)

Let K=ceil(H/h), theta=6(K+1), and Q0<=C/L be the exact path
comparison constants. The physical leaf bound gives sum_(s<L)W_s<=K.
For every such nonnegative path, the exact composition-prefix formula
gives the majorant

    Q0 product_(t<L)(theta b_t)^(W_t)/W_t!.

Retain (13) while summing this majorant. Extending the algebraic sum
to all nonnegative paths only increases it, and yields exactly

    Q0[exp(theta B)-exp(theta(B-B_early))]
       <=Q0 theta B_early exp(theta B).

No probability comparison is asserted for the newly added paths;
only their nonnegative algebraic majorants are added. By (10)-(12),
absorbing K+1 into an exponential gives

    P(T<=H,F_S>0 | profile)
       <=C S^2/L^3 exp[C(1+H/h)]
       <=C_c S^2 A^3 exp(C_c A)/R^3.                 (14)

Every row-law comparison was made conditional on the complete
original profile. The original rows are independent under that
conditioning, while entries within a row need not be independent.
No reached-root or same-orbit fresh-law statement has been used.

## 4. The complementary depth sector is also small

Put M=max(S,2). Since M is an integer, L<M implies

    kappa R/A<M<=2S,
    A>kappa R/(2S).

Therefore, deterministically,

    1{L<M}<=(2SA/(kappa R))^2.                       (15)

On this sector it is unnecessary to identify (1) with any physical
genealogy. Drop the F_S event entirely and use the GLOBAL conditional
probability bound (8). As L<M is profile-measurable, (15) gives

    E[1{L<M} P(T<=H,F_S>0 | profile)]
       <=C_c S^2/R^3 E[A^3 exp(C_c A)]
       <=C_c S^2/R^3.                               (16)

On L>=M, average (14) and use the same moment (5). Adding the two
sectors proves (2). Multiplying by H+2<=(c+2)R proves (3).
The exact physical birth normalization and the elementary fact that
a packing has no more members than its ambient family prove (4).

## 5. Scope

The estimates are uniform over deterministic integers 1<=S<=sqrt(r).
In particular, if S=o(sqrt(r)), this sector has o(W) raw trace
incidence and o(W/sqrt(r)) births, hence at most that many pairwise
disjoint members. Any further subfamily, including a residual
low-score subfamily with F_S>0, inherits these upper bounds.

Nothing here bounds the complementary all-zero original triangle
F_S=0, which remains the relevant unresolved trajectory sector.
The result neither estimates correlations at shifted birth times nor
asserts a fresh distribution after an orbit shift. It does not prove
packing for all positive-budget runs, sufficient shared repair, or a
coefficient-one construction.

## 6. Conditional concentration and tight normalizers

The accepted zero-budget Gaussian-band theorem in
pbbs_zero_budget_gaussian_band_weighted_lower_bound.md, Sections 1-4,
provides positive lower normalizers. Indeed choose any fixed
0<u<v<c. For the zero-budget roots with uR<=h=T<=vR, their birth
probability is asymptotic to a positive constant divided by R, and
their raw length-weighted mass converges to a positive constant.
They are all H-short for sufficiently large r. Combined with the
root envelope upper bounds, this gives

    P(T<=H)=Theta_c(1/R),
    mu_H=E[(T+2)1{T<=H}]=Theta_c(1).                 (17)

Thus division by these particular normalizers is justified. Let the
short-incidence marginal on original births be the law with density
(T+2)1{T<=H}/mu_H relative to the uniform original-root law. Equations
(2)-(3) and (17) imply, for every deterministic 1<=S<=R,

    P(F_S>0 | T<=H)<=C_c S^2/r,
    P_short-incidence(F_S>0)<=C_c S^2/r.             (18)

In particular the original triangle through every prescribed
S=o(sqrt(r)) is entirely zero with probability tending to one under
both laws. These are statements about the sampled ORIGINAL birth.
They assert no stationarity or fresh law at a shifted birth, and do
not estimate the overlap of different repair traces.


<!-- END COMPLETE SOURCE 31 -->


---

<a id="document-32"></a>

## Document 32: pbbs_gaussian_clock_genealogy_structural_audit.md

Source: `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_gaussian_clock_genealogy_structural_audit.md`

[Portable document](sources/essential/c69c/research_round1/pbbs_gaussian_clock_genealogy_structural_audit.md) · [Exact original](originals/c69c/research_round1/pbbs_gaussian_clock_genealogy_structural_audit.md)

<!-- BEGIN COMPLETE SOURCE 32 -->

# PBBS short clocks expose a deterministic triangle of original pruning slots

Date: 2026-09-07. Pure proof, written by the Gaussian residual subagent.
Original project files are read-only. No computation was used.
Local review record: the worktree lead and the independent recency-gate
agent fully reviewed Sections 1-5 and Appendix A; both reviews pass.
The reached-height invariance clarification also passed. The coordinator
has now accepted the theorem after separate structural and analytic
audits, both passing on 2026-09-07.

This note supplies a structural estimate for the actual full-lifetime
event. It uses the exact equality-particle renormalization and the
one-start renewal identity, rather than a fresh law at reached states.
The separate analytic transfer is in pbbs_gaussian_clock_analytic_transfer.md.

The principal conclusion is (12): a short lifetime at height comparable
to its cutoff forces a bounded sum over a FIXED triangular collection of
original inverse-pruning coordinates. The number of these coordinates
at pruning depth s is s+1. The coordinates are not newly sampled at
different dynamical visits.

## 1. Original pruning arrays and their exact law

For a Dyck root D, put D_s=partial^s D and r_s=|D_s|_up, where partial
simultaneously deletes all peaks. Write h=ht(D), so r_h=0 and r_s>0
for s<h. Fix the entire feasible profile (r_0,...,r_h).

At a level s with nonempty core D_(s+1), let

    p_s=2r_(s+1)+1,
    ell_s=r_s-2r_(s+1)+r_(s+2).                         (1)

There are p_s equality particles in the cyclic word 0D_s. Label them
persistently in cyclic order, with label 0 on the edge immediately
before the original unmatched zero. The recorded particle word is
0D_(s+1). For particle j, let L_j be the positive cyclic distance from
particle j-1 to particle j, and let epsilon_j be one if their recorded
bits differ, zero otherwise. Define the original incoming-gap coordinate

    Z_(s,j)=(L_j-1-epsilon_j)/2.                         (2)

Between consecutive equality edges, physical bits alternate. Therefore
L_j=2Z_(s,j)+1+epsilon_j with Z_(s,j)>=0. Summing distances gives

    sum_j Z_(s,j)=ell_s.

Here sum epsilon_j=2 pk(D_(s+1)) and
pk(D_(s+1))=r_(s+1)-r_(s+2).

The vector Z_s is an exact encoding of the inverse-pruning fibre over
D_(s+1). The core bits and all gap distances reconstruct the original
cyclic word and its specified root uniquely. Its vector is a weak
composition of ell_s into p_s parts. Conversely, the known exact fibre
size is binom(ell_s+p_s-1,p_s-1), exactly the number of such compositions.
Injection and this finite equality prove that every composition is
admissible. This also identifies the usual terminal free-leaf occupancy
with Z_(s,0).

Consequently, conditional on the complete pruning profile, the original
vectors Z_s are independent uniform weak compositions. This follows by
reconstructing from the bottom core upward: at each level the fibre size
depends only on the profile, not the particular core word. The last
nonempty core is the uniquely determined height-one word (10)^(r_(h-1)).
Only nonempty-core levels will be queried below.

## 2. Every gap coordinate is invariant under the dynamics

Apply one physical PBBS update at a level with nonempty reduced core.
Its selected equality particle a advances one physical edge. Thus its
incoming distance L_a increases by one and its outgoing distance
L_(a+1) decreases by one. Other distances do not change.

In the recorded particle word rooted at a, the selected bit is zero,
its predecessor bit is zero, and its successor bit is one. The update
complements every other recorded bit and leaves the selected zero fixed.
Hence epsilon_a changes from zero to one and epsilon_(a+1) changes
from one to zero. All other epsilon values are unchanged. Formula (2)
therefore shows that EVERY Z_(s,j) is invariant, with persistent indices.

In particular, a later terminal occupancy query reads one of the
ORIGINAL coordinates Z_(s,j), without a time-dependent offset. This is
not a statement that the queries are independent: repeated queries of
one coordinate read the same value.

## 3. Two exact clocks

At a physical PBBS phase with selected label a, define two clocks:

* T is the interval until the next selection of that same label a.
  Its physical length is 2T(D)+1, with the established newborn-lifetime
  convention.
* C is the interval until the next selection of the physical predecessor
  label a-1. Its physical length is 2C(D).

The notation C in this note denotes this clock, not a Catalan generating
function. Selections of adjacent physical labels strictly alternate.
To see this, consider edge (a-1,a). A selection at its right endpoint
requires incoming bits 00 and changes the edge to unequal bits 10.
Until an endpoint is selected, both bits are complemented together, so
equality cannot change. Another right-endpoint selection is impossible
until the left endpoint is selected. A left-endpoint selection requires
outgoing bits 01 and changes them to 00; another such selection is
impossible until the right endpoint is selected. The full-label property
ensures eventual events in both directions. Initial predecessor bit zero
forces the first predecessor selection time to be even.

In the reduced PBBS, call the currently selected equality particle b and
its predecessor b-1. Let

    0<B_1<B_2<... 

be successive positive selection times of b-1. If the original terminal
coordinate is z, the initial particle distance is 2z+1: both recorded
endpoint bits are zero. Before a spatial wrap, particle b-1 selects the
physical label a-1 on its (2z+1)st move and the physical label a on its
(2z+2)nd move. The exact physical clock partition is therefore

    C parent: child C, then 2z child T clocks;
    T parent: child C, then 2z+1 child T clocks.         (3)

The child C runs from the starting time to B_1; the subsequent child T
clocks are the intervals [B_j,B_(j+1)]. These intervals are adjacent,
disjoint except for endpoints, and cover the parent clock exactly.
Their child roots are actual reached phases of the same reduced PBBS.

For example, writing F=partial D, Psi(F)=phi^(B_1)F, and R for the
same-label return permutation on reduced phases, (3) is equivalent to

    C(D)=C(F)+sum_(j=0)^(2z-1) T(R^j Psi(F))+z,
    T(D)=C(F)+sum_(j=0)^(2z)   T(R^j Psi(F))+z.         (4)

An empty sum is zero. The terms are generally correlated. No product law
on the reached roots R^j Psi(F) is being asserted.

We use (3) only while the entire outer physical horizon G is smaller
than the circumferences at the relevant levels. This excludes the wrap
alternative. All child clocks lie inside that same outer interval, so
the restriction automatically passes to every node in the truncated
genealogy. Taking G<2r_L+1 is sufficient for levels s<L; on a short root
the even C subintervals are strictly shorter than the possible N-1
move of one particle around to the predecessor site.

## 4. The original slot order is deterministic

Expand an outer T clock using (3), through L pruning levels for which
the preceding circumference condition holds. At every depth the nodes
are a chronological partition of the SAME physical interval [0,G].
Their left endpoints are distinct.

At depth s, a node queries the incoming gap of the currently selected
persistent particle at level s+1. A C clock at level s+1 changes that
level's selected physical label by -1. A T clock at that level ends at
the same selected physical label. Every depth-s node has exactly ONE
child C, followed only by child T clocks. Its completion therefore
changes the selected particle index at level s+1 by exactly -1.

Initially the selected persistent label is 0 at every level. It follows
that the chronological depth-s queries are exactly

    Z_(s,0), Z_(s,-1), Z_(s,-2), ...                    (5)

with indices modulo p_s. There is no dependence of this order on any
unexposed coordinate. The number of queries can depend on their values.
If fewer than p_s nodes occur, all queried coordinates are distinct.

This is stronger than bounding repetitions by a return-time argument.
It also avoids a deferred-decisions assumption about a trajectory oracle.
The necessary event derived below concerns a fixed prefix of (5).

## 5. A short outer lifetime allows only bounded total queried mass

Let n_s be the number of all clocks at depth s, m_s the number of T
clocks, and W_s the sum of their n_s queried gap coordinates. Start with
n_0=m_0=1. Formula (3) gives exact identities

    m_(s+1)=m_s+2W_s,
    n_(s+1)=n_s+m_s+2W_s.                              (6)

Thus

    n_s>=s+1,
    sum_(s=0)^(L-1) W_s=(m_L-1)/2.                   (7)

The original pruning profile remains the profile at every reached phase.
Indeed equality-particle renormalization preserves cyclic particle order
and count, and identifies the recorded word after an update with the
PBBS update of the peak-deleted word. Thus partial commutes with phi;
iterating gives partial^j phi^t D=phi^t partial^j D (with the appropriate
reduced map on the right). At each level its rank is unchanged by that
reduced dynamics, so every r_j is invariant. Height is the first pruning
depth at which the word becomes empty. Consequently every REACHED
depth-L root has height exactly h-L, not merely the original root D_L.

Every depth-L T interval therefore has physical length at least
2(h-L)+1, by the proved height-gap theorem. These intervals are disjoint
within the outer interval, so

    m_L <= G/[2(h-L)+1].                               (8)

All node intervals have positive integer lengths, hence n_s<=G. Suppose

    G=2T(D)+1<=2H+1,
    h>L,
    p_s>G for 0<=s<L.                                  (9)

Then the first n_s entries in (5) have not wrapped and, by n_s>=s+1,
nonnegativity gives

    sum_(s=0)^(L-1) sum_(j=0)^s Z_(s,-j)
      <= sum_(s=0)^(L-1) W_s
      <= ( G/[2(h-L)+1]-1 )/2.                       (10)

Every coordinate on the left side is an original fibre coordinate with
a predetermined index. In particular, for fixed a,c>0, if

    h>=a sqrt(r),   T(D)<=c sqrt(r),

then for every fixed L and sufficiently large r satisfying (9),

    sum_(s=0)^(L-1) sum_(j=0)^s Z_(s,-j) <= K_(a,c),  (11)

where any fixed integer K_(a,c)>c/(2a) suffices. The exact constant is
unimportant; it is independent of r and L in the iterated-limit use.

Thus the structural conclusion is

    {h>=a sqrt(r), T<=c sqrt(r), regular first L levels}
       is contained in
    {sum of the fixed triangular coordinates <=K_(a,c)}. (12)

The number of levels L may first be fixed, r sent to infinity, and only
then L sent to infinity. No estimate for a growing number of pruning
levels is necessary.

## 6. Exact probabilistic transfer target

For a uniform composition of ell into p parts, any fixed finite list of
distinct coordinates converges to independent geometric variables when
ell,p tend to infinity with a fixed positive ratio. The limiting positive
probability is q=ell/(ell+p), and P(Z=k)=(1-q)q^k. This follows directly
from the ratio of the two stars-and-bars counts after fixing those
coordinates.

If the standard fixed-depth Catalan fringe law is supplied in the form

    r_s/r -> 1/(s+1) in probability,
          for every fixed s,                           (13)

then (1) gives

    ell_s/p_s -> 1/[(s+1)(s+3)],
    q_s -> 1/(s+2)^2.                                  (14)

Conditional-profile independence from Section 1 makes the finitely many
triangular coordinates asymptotically independent across all fixed
levels. No reached-state independence is used. Let S_L be their sum.
For each fixed L,

    limsup P(S_L<=K)
      <= exp{K-(1-e^(-1)) sum_(s=0)^(L-1)
                                   (s+1)/(s+2)^2}.    (15)

Indeed 1{S_L<=K}<=exp(K-S_L), and a geometric variable
satisfies E exp(-Z)<=1-(1-e^(-1))P(Z>0).
The sum in (15) diverges as log L. Consequently (12)-(15) give

    P(h>=a sqrt(r), T<=c sqrt(r)) -> 0                 (16)

for every fixed a,c>0, using (13) as proved in Appendix A. Letting a
decrease to zero and applying the Dyck-height small-ball estimate proved
in pbbs_gaussian_clock_analytic_transfer.md gives

    P(T<=c sqrt(r)) -> 0 for every fixed c>0.          (17)

The coordinator's independent structural and analytic audits passed.
Appendix A below gives a direct proof of the profile input (13). The strongest new
structural input is the deterministic implication (12), not an averaged
entry kernel or a reset of the residual lifetime law.

## 7. A literal one-level clock check

The existing symbolic family from
pbbs_original_node_charge_counterexample.md is useful here. Put A=10 and

    D_b=111000 1 A^b 0,       b>=3.

It has height three, semilength b+4, and lifetime T=6, so its physical
horizon 13 is below its outer circumference 2b+9. Its core is

    F=partial D_b=110010,
    partial F=10.

The original level-zero gap array, indexed as in (2), is

    (Z_(0,0),...,Z_(0,6))=(0,0,0,0,0,0,b-1).

This follows by listing the seven equality edges: the only enlarged
interparticle gap is from the up-equality edge at the start of 1 A^b 0
to its final down-equality edge. Its distance is 2b, and its epsilon is
one. In particular the FIRST query is the original terminal z=0,
although a different original slot contains arbitrarily large mass.

In the reduced phase F, the next-predecessor clock is C(F)=4, and its
endpoint is Psi(F)=101100. The literal lifetimes are T(F)=5 and
T(Psi(F))=2. Thus the one-level partition gives

    C(D_b)=4,
    T(D_b)=C(F)+T(Psi(F))=4+2=6.

The reached child is explicitly Psi(F), not a fresh copy of F. The
second original level-zero slot is not resampled. This example checks
the local clock identity only: its reduced circumference is seven, so
the stronger sufficient global no-wrap condition in (9) is not met.
It is not a Gaussian profile example.

## Appendix A. A direct fixed-depth pruning-profile law

Here C(z)=sum Cat_r z^r is the ordinary Catalan series for plane trees
with edges counted by z. A fringe subtree at a vertex consists of that
vertex and all its descendants. Fix one plane-tree shape A with k edges,
and let N_A(D) count its fringe occurrences, including the root if it
matches. The generating function of contexts with one subtree hole is

    1/(1-zC(z)^2).

Indeed every ancestor of the hole has a distinguished child edge and
arbitrary ordered lists of children on both sides, giving zC^2 per
ancestor. Therefore

    sum_D N_A(D) z^(|D|_up)=z^k/(1-zC^2).             (A1)

Since zC^2=C-1 and
1/(2-C)=(1+(1-4z)^(-1/2))/2, for r>k the coefficient
in (A1) is (1/2) binom(2(r-k),r-k). Thus

    E N_A(D)/r -> 4^(-k)/2.                            (A2)

For fixed shapes A,B of sizes k,l, ordered pairs of disjoint fringe
occurrences have generating function

    z^(k+l) 2z^2 C^3/(1-zC^2)^3.                     (A3)

To obtain (A3), use a context above their lowest common ancestor, the
two distinguished child branches below it in either order, the three
intervening child lists, and independent contexts in the two branches.
The leading singular term of (A3) at z=1/4 is

    4^(-k-l) (1-4z)^(-3/2)/8.

Dividing coefficients by Cat_r gives

    E[ordered disjoint pair count]/r^2
       ->4^(-k-l)/4.                                  (A4)

The overlapping pairs contribute O(r): if one fixed-shape occurrence
contains the other, it has only a bounded number of possible descendant
occurrences. Equations (A2)-(A4) prove convergence in probability of
N_A(D)/r to 4^(-k)/2, jointly for every finite list of shapes.

To pass from finite lists to an arbitrary bounded fringe indicator,
truncate by fringe size. The expected number of fringe occurrences of
size exactly k<r is

    Cat_k (1/2) binom(2(r-k),r-k)/Cat_r.

After dividing by r, the usual central-binomial bounds give a summand
at most

    C sqrt(r)/[(k+1)^(3/2)(r-k+1)^(1/2)].

For M<k<=r/2 their sum is O(M^(-1/2)); for r/2<k<r it is
O(r^(-1/2)). The root occurrence k=r contributes 1/r. Therefore the
expected fraction of vertices with fringe size above M is at most

    C M^(-1/2)+O(r^(-1/2)).                            (A5)

Markov's inequality, finite-shape convergence, and then M->infinity
prove the fringe law for every bounded indicator. The limiting fringe
tree has probability 4^(-k)/2 for each shape with k edges; the masses
sum to C(1/4)/2=1.

A nonroot edge survives s simultaneous leaf-pruning rounds exactly
when its child vertex has a fringe subtree of height at least s. The
root changes the vertex count by at most one. Under the limiting fringe
law, for s>=1,

    P(fringe height>=s)
      =1-C_(s-1)(1/4)/2
      =1/(s+1).

The s=0 case is immediate. This proves (13), jointly for every fixed
finite number of depths, without a growing-depth concentration theorem
or a dynamical mixing assertion.


<!-- END COMPLETE SOURCE 32 -->


---

<a id="document-33"></a>

## Document 33: pbbs_stationary_lifetime_identities.md

Source: `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_stationary_lifetime_identities.md`

[Portable document](sources/essential/c69c/research_round1/pbbs_stationary_lifetime_identities.md) · [Exact original](originals/c69c/research_round1/pbbs_stationary_lifetime_identities.md)

<!-- BEGIN COMPLETE SOURCE 33 -->

# Exact stationary PBBS lifetime and residual-life identities

Date: 2026-09-07. Pure proof; no computation or enumeration.

The main result is a finite stationary marked-Dyck permutation and its exact
return-section identities. Uniform newborn lifetime has mean r, even after
conditioning on height. Uniformly sampling an existing up-step gives a
different, length-biased law. None of these identities assumes Q6, independent
renewal increments, mixing, or a local central limit theorem.

## 1. Sources, prior overlap, and conventions

Read-only sources inspected:

- PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md, Sections 1, 3, 4, 8, 9;
- MATH_THEOREM_PBBS_EXACT_RUN_SPECTRUM_FLAT_ANTECEDENT_NOGO_AND_FULL_UPPER_DECK_20260813.md,
  Sections 1 and 2;
- PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md, including the full-label
  consequence of componentwise homomesy;
- MATH_THEOREM_PBBS_ST_EXACT_ADDITIVE_RENEWAL_AND_TWO_TIME_CENSUS_20260726.md,
  Section 1;
- MATH_THEOREM_PBBS_ST_EXACT_RENEWAL_THRESHOLD_AND_TWO_POINT_KERNEL_20260726.md;
- PBBS_TWO_DIMENSIONAL_RENEWAL_LOCAL_CLT_GATE_20260725.md.

The run-length shift and occupation census are already explicit in the
exact run-spectrum source. The identities below reorganize them into a
marked-Dyck stationary object. No novelty claim is made for the general
finite renewal/occupation counting principle.

Fix r>=1 and n=2r+1. Let f be the PBBS permutation on rank-r subsets,
g=f^2, phi its rooted-Dyck quotient, and tau=phi^2. Write D=P1R0S for the
first-maximum factorization. Then

    tau(D)=S 1_new P 0 R.                                  (1)

The old first-maximum up-step is consumed, the new divider is planted,
and the other up-steps keep their coordinate identities.

T(D) counts the subsequent g updates from immediately after planting in
(1) through the consuming update. It equals the number of rank-r owner
states in that positive coordinate run. In particular a mountain of
height r has T=r. This is the convention used in the corrected conservation
identity in pbbs_q6_independent_audit.md.

## 2. Why there are no permanent coordinates here

The PBBS-specific input used in this section is the already audited
full-label property: on any f component of length L, each coordinate
occurs L/n>0 times in its omitted-label word. It is stated in the
residence-reduction source, Section 1, and independently used in the
run-spectrum source's componentwise homomesy census.

Consecutive occurrences of a label have odd cyclic separation. If L is
odd, the step-two cycle visits the whole f component, so every coordinate
is inserted and deleted on that g cycle. If L is even, occurrences of
each coordinate alternate between the two parities. Their positive total
number is consequently even, and both parities contain occurrences.
Again each of the two g cycles has an insertion and deletion of every
coordinate. Thus no coordinate is permanently present or permanently
absent on any g component. The same holds after complementation.

This hypothesis cannot be omitted for a general Johnson cycle. A permanent
core contributes occupation but no births. On a rank-r cycle with a
permanent core of size c, counting only born runs gives mean lifetime
r-c, not r. The permanent-core examples in short_trade_core_obstruction.md
therefore do not obey the PBBS mean identity.

## 3. A finite stationary marked-Dyck permutation

Let Omega be any nonempty tau-invariant set of semilength-r Dyck roots.
Examples include one tau orbit, all roots of one specified height, all
roots, or a union remaining after deletion of complete short tau cycles.
An arbitrary noninvariant class, such as the primitive roots, is not an
admissible conditioning class for the claims below.

Define the finite state space

    M_Omega={(D,j): D in Omega, j is an up-step position of D}.

It has r|Omega| states. Under (1), transport a retained marked up-step
with its block. If the mark is the consumed first-maximum up-step, reset
the mark to the newly planted divider. This defines a permutation F of
M_Omega: tau is a permutation of Omega, and at each update the retained
up-steps map bijectively to retained up-steps, while the consumed step
maps bijectively to the new one.

Let B_Omega be the image under F of the first-maximum marked states.
This birth section has exactly one marked state above each D, hence
|B_Omega|=|Omega|. Its marked position above D is the new divider planted
by the transition from tau^(-1)D.

Every marked orbit hits B_Omega. Otherwise its mark would survive forever
without being consumed. Lifting the finite rooted orbit to the finitely
many physical spatial phases would give a permanent coordinate on a g
component, contrary to Section 2.

The F orbit from one birth-section visit to its next visit follows one
physical marked coordinate until consumption, then resets it. Its return
time is exactly T(tau^(-1)D). Since tau permutes Omega, uniform sampling
of B_Omega gives the same lifetime distribution as uniform D in Omega.
The uniform measure on M_Omega is stationary, but successive return times
need not be independent.

## 4. Exact mean lifetime, including height conditioning

Each state of M_Omega lies in exactly one excursion from the birth section
to its next visit, with the initial birth state included and the terminal
birth state excluded. Consequently

    sum_(D in Omega) T(D)=r|Omega|,
    E_Omega[T]=r.                                         (2)

Equivalently, the lift to n|Omega| physical states has one birth per edge
and r occupied-coordinate incidences per vertex. With no permanent
coordinates, every incidence belongs to exactly one born run, giving
the same count.

Height is tau-invariant, so in every nonempty height stratum

    E[T | height=h]=r.                                    (3)

Let P_count, R_count, S_count count the nonconsuming P,R,S updates in a
born run. The correct endpoint convention gives

    T=h+2 R_count+S_count.

Thus the exact conditional mean interruption budget is

    E[2 R_count+S_count | height=h]=r-h.                   (4)

This is an expectation identity. It does not imply concentration of T or
of the interruption budget.

## 5. Uniform existing marks: age, residual life, and length bias

Choose D uniformly in Omega and then choose one of its r up-steps
uniformly. This is the stationary uniform measure on M_Omega. Let A>=0
be the age of the current physical mark since its birth, and let R>=1
be the number of future updates through its consumption. Let L=A+R be
the total lifetime of its current run.

Write p_l=P_birth(T=l), with birth law uniform over Omega as in (2).
Each excursion of length l contains exactly one state with (A,R)=(a,b)
for each a>=0,b>=1 satisfying a+b=l. Therefore

    P_stat(A=a,R=b)=p_(a+b)/r.                            (5)

This gives the exact formulas

    P_stat(L=l)=l p_l/r,
    P_stat(R=b)=P_birth(T>=b)/r,
    P_stat(R>=b)=E_birth[(T-b+1)_+]/r,                    (6)
    P_stat(R<=H)=E_birth[min(T,H)]/r <= H/r.               (7)

In particular a uniformly chosen existing up-step has only O(r^(-1/2))
probability of being consumed in the next O(sqrt(r)) updates. This is
fully compatible with a positive fraction of newborn runs having such
short lifetimes: existing marks are sampled with length bias.

The moments are also exact:

    E_stat[R]=(E_birth[T^2]+r)/(2r),
    E_stat[A]=(E_birth[T^2]-r)/(2r).                       (8)

For a concrete unmarked-root statistic, let B_H(D) be the number of the
currently present up-steps that are consumed in the next H updates. Then

    E_D[B_H(D)]=E_birth[min(T,H)] <= H.                    (9)

This supplies a valid finite marked-Dyck transfer target. If
F_H=P_stat(R<=H), F_0=0, then the newborn distribution is recovered exactly
by discrete differences:

    P_birth(T=H)=r(2F_H-F_(H-1)-F_(H+1)),                 (10)
    P_birth(T<=H)=1-r(F_(H+1)-F_H).

Thus approximating the residual distribution coarsely is insufficient
for a sharp newborn count; the differences in (10) are amplified by r.

## 6. Return gaps, complement projection, and repair-edge lengths

On an f component write A_i=f^i(A_0) and lambda_i for its omitted label.
The exact recurrence is

    A_(i+2)=A_i minus {lambda_(i+1)} union {lambda_i}.

If consecutive occurrences of a label have f gap 2t+1, the label's rank-r
positive g run has length t. The paired complement-projected positive
run has length t+1. The dictionary for one gap start is therefore

    f return gap                  2T+1,
    rank-r positive g lifetime    T,
    complement positive lifetime  T+1,
    repair interval edge count    T+2.                    (11)

The last count includes insertion and deletion edges. A projected
residence cutoff H means T+1<=H, equivalently T<=H-1. It does not mean
T<=H, and it does not cut off repair intervals at H edges.

For a phi-invariant Omega, including all roots of a given height, the
complement newborn lifetime law is distributionally T+1 under the same
uniform root law. Its mean is r+1, and its stationary existing-coordinate
law is obtained from (5)-(8) by replacing T by T+1 and r by r+1. For
example,

    P_comp(R=b)=P_birth(T+1>=b)/(r+1).                    (12)

For an arbitrary merely tau-invariant Omega, the same comparison uses
the T law on phi(Omega): on the complement edge at A_i the incoming label
is lambda_(i+1), whose gap starts at f(A_i). This phase shift must not be
silently dropped. Both Omega and phi(Omega) still have mean T=r.

The edge-incidence analogue of length bias weights a gap-start run by
T+2. Its normalizer is r+2, agreeing with the exact r+2 repair-interval
congestion at each projected transition in the residence-reduction file.
This is a congestion count, not an edge-disjoint packing estimate.

## 7. Connection to the existing exact renewal formulas

For D_j=tau^jD define

    a_j=delta(D_j), c_j=d(D_j), c_hat_j=d(phi D_j).

The existing additive-renewal identity is

    a_(j+1)-a_j=c_j-c_hat_j,
    sum_(j=0)^(t-1)c_j-a_t=sum_(j=0)^(t-1)c_hat_j-a_0.

Its first return index is precisely the rank-r newborn lifetime:

    T(D)=min{t>=1: sum_(j=0)^(t-1)c_hat_j in a_0+n Z_(>=0)}.  (13)

Indeed the corresponding omitted-label gap is 2t+1, and (11) identifies
the rank-r lifetime as t. Nonnegative winding follows because a_t<n
and the positive increment sum makes a congruent multiple larger than
-n; it must therefore be a nonnegative multiple of n.

The exact ST_A one-point indicator is consequently 1{T<=H-1}, and the
two-point statistic uses this indicator at D and tau^jD in the same
deterministic sequence. The stationary construction above supplies neither
independence nor a mixing estimate for those indicators.

The two-dimensional-renewal local-CLT note already retracts the proposed
diffusion assumption for the natural PBBS record state: its transfer is
triangular. Nothing in (2)-(13) reinstates that application. Uniform
stationarity and a return-section interpretation do not imply a local
central limit theorem.

## 8. A precise second-moment test for a short newborn tail

For any class Omega as above, fix H<r and write

    p=P_birth(T<=H),       V=Var_birth(T).

Then

    V >= [p/(1-p)](r-H)^2,
    p <= V/[V+(r-H)^2].                                 (14)

For p=0 this is immediate, and p=1 is incompatible with E[T]=r>H.
Otherwise put a=E[T|T<=H]<=H. The other conditional mean is
(r-pa)/(1-p). Dropping the two nonnegative conditional variances gives

    V >= p(a-r)^2 + (1-p)((r-pa)/(1-p)-r)^2
       = [p/(1-p)](r-a)^2,

which proves (14). Thus any positive lower bound on the fraction of
newborn lifetimes at a sublinear cutoff forces variance of order r^2.
Conversely, a separately proved V=o(r^2) estimate would imply a vanishing
newborn fraction at every H=o(r). No such variance estimate is supplied
here; the identity for E_stat[R] in (8) is another exact formulation of
that missing moment control.

## 9. What remains unknown

The exact mean r, even at fixed height, and the residual identities are
rigorous. They do not determine P_birth(T<=H) at Gaussian or larger
sublinear scales: rare very long excursions can carry a substantial part
of the mean. Nor do one-point counts alone control the overlap packing
nu_H. The remaining dynamic problem is the distribution of the return
time (13), together with the correlations of its short-return indicators.


<!-- END COMPLETE SOURCE 33 -->


---

<a id="document-34"></a>

## Document 34: pbbs_quantitative_clock_polylog_short_mass.md

Source: `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_quantitative_clock_polylog_short_mass.md`

[Portable document](sources/essential/c69c/research_round1/pbbs_quantitative_clock_polylog_short_mass.md) · [Exact original](originals/c69c/research_round1/pbbs_quantitative_clock_polylog_short_mass.md)

<!-- BEGIN COMPLETE SOURCE 34 -->

# A polylogarithmic raw-incidence bound for Gaussian-short PBBS lifetimes

Date: 2026-09-07. Pure proof; no computation or original-project edits.
The worktree lead and independent recency reader fully audited this note.
The coordinator then completed a full read and a separate independent
full audit; all passed. The fixed-c raw-incidence theorem (1) is accepted.
The worktree lead supplied the adaptive branching improvement; this note
records the quantitative proof. The complete marked-fringe profile proof
is retained as a verified independent route alongside the coordinator's
exact all-depth pruning census. No master document was edited.

Follow-up, 2026-09-08: the coordinator has accepted the stronger
mu_H=O_c(1) and P(T<=H)=O_c(r^(-1/2)) theorem. Its envelope proof is
/Users/amir.nuriyev/Documents/problem/scratch/PBBS_BOUNDED_GAUSSIAN_SHORT_INCIDENCE_20260908.md,
Sections 1-8; the independent coarse-profile proof is
pbbs_bounded_gaussian_short_incidence.md in this directory. The complete
original proof below is retained, particularly its finite adaptive
path comparison. Its stated lack of an O(1) conclusion describes this
older estimate by itself, not the current accepted theorem.

For every fixed c>0, with H=floor(c sqrt(r)),

    mu_H=E_D[(T(D)+2)1{T(D)<=H}] <= C_c(log r)^2          (1)

for sufficiently large r. D is uniform among ORIGINAL Dyck roots of
semilength r. Subscript-c constants may depend on c; other constants
below are absolute and may change between displays.

Extra branches in the clock genealogy increase later query counts and
incur extra zero-slot costs. Keeping these costs removes the larger
exp[O_c((log log r)^2)] bound obtained from the fixed triangle alone.
Equation (1) does not prove bounded raw incidence, a vanishing occupied
union, a target-repair bound, or a packing theorem. No growing-c
uniformity is asserted.

## 1. Uniform marked-fringe generating functions

Let r_s=|partial^s D|_up. An original nonroot tree vertex contributes to
r_s exactly when its fringe subtree has height at least s. Fix s>=1 and
put A_s(x)=C_(s-1)(x), the GF of trees of height at most s-1. Let F_s
mark ALL vertices with fringe height at least s, including the root;
let G_s mark only nonroot such vertices. Ordered root children give

    G_s=1/(1-xF_s),       F_s=uG_s+(1-u)A_s,

so G_s counts r_s exactly and

    xuG_s^2-[1-x(1-u)A_s]G_s+1=0.                     (2)

There are absolute gamma,C_0>0 such that

    A_s(1/4)=2s/(s+1),
    1<=A_s(x)<=3,       0<=A_s'(x)<=C_0(s+1),
    0<=x<=x_+=(1/4)[1+gamma/(s+1)^2].                 (3)

Here is a positive-factor justification of the derivative bound. Write
A_s=sum_(a=0)^(s-1) Z_a, where Z_0=1 and

    Z_a=x^a/[P_a P_(a+1)],
    Z_a(1/4)=2/[(a+1)(a+2)]             for a>=1,
    P_m(x)=product_(k=1)^floor(m/2)
                [1-4x cos^2(pi k/(m+1))].

Here P_m denotes the Fibonacci polynomial, separately from the marked
series F_s in (2).

Put delta=4x_+-1. For m<=s, a normalized inverse factor at x_+ is
[1-delta cot^2(pi k/(m+1))]^(-1). The inequalities

    delta cot^2(pi k/(m+1))<=C gamma/k^2,
    sum_k cot^2(pi k/(m+1))<=C(m+1)^2

follow from sin(pi k/(m+1))>=2k/(m+1). Choose gamma small. The product
of these changes is bounded uniformly, and xZ_a'/Z_a at x_+ is at most
C(a+1)^2. Thus Z_a(x_+)<=C/(a+1)^2 and Z_a'(x_+)<=C. Sum over a;
positivity extends the derivative bound to smaller x. The critical
value and a further reduction of gamma give A_s<=3.

There are absolute C_1,c_1>0 such that, for |theta|<=c_1/(s+1), the
positive combinatorial series is finite at

    u=e^theta,
    x_theta=(1/4)exp[-theta/(s+1)-C_1 theta^2],

and

    G_s(x_theta,e^theta)<=4.                           (4)

We prove this without assuming a radius of convergence. Put
a=1/(s+1), z=4x_theta, A=A_s(x_theta), b=1-x_theta(1-u)A. Its
discriminant is

    Dscr=b^2-4x_theta u
      =1-z+(z/2)(A-2)(u-1)+(z^2/16)A^2(u-1)^2.

For C_1 fixed and c_1 small, x_theta is in (3), b>=1/2, and

    |A-(2-2a)|<=C_0(s+1)|z-1|/4,
    |z-1|<=2[a|theta|+C_1 theta^2].

The logarithm of (1-a)+a e^theta has second derivative at most 1/4.
Consequently

    1-z[1+a(u-1)]>=1-exp[-(C_1-1/8)theta^2].

This is at least a fixed multiple of C_1 theta^2 if C_1 is large and
c_1 small. The remaining possibly negative error in Dscr is at most
C(1+C_1 c_1)theta^2; its final squared term is nonnegative. Choosing
C_1 first large and c_1 afterward small gives Dscr>=0, with equality
allowed at theta=0. The same choices also give

    1-x_theta(1+u)A>=a/2.                              (5)

Indeed its value at theta=0 is a, and its perturbation is bounded by
C(c_1+C_1 c_1^2)a using (3).

The smaller root G_star=2/(b+sqrt(Dscr)) is at most four and is at least
A. For the latter statement, the polynomial in (2), evaluated at A,
is 1-A+x_theta A^2>0 by the bounded-height recurrence, while (5) puts
A to the left of its vertex. Set F_star=uG_star+(1-u)A. Then F_star>=A,
it is a fixed point of u/(1-xF)+(1-u)A, and x_theta F_star<1.

Now truncate trees by total height. Starting with F^(s-1)=A, their
successive evaluations satisfy

    F^(d)=u/[1-x_theta F^(d-1)]+(1-u)A,       d>=s.

They increase as positive combinatorial sums and are bounded by F_star,
because this map is increasing below 1/x_theta. Monotone convergence
therefore proves finiteness and G_s<=G_star, including u<1. This proves
(4) without a radius assumption.

Positive coefficient evaluation and Cat_r>=c4^r r^(-3/2) imply

    E exp(theta[r_s-r/(s+1)])
       <=C r^(3/2)exp(C_1 r theta^2).                 (6)

Chernoff at theta=+/-eps/[2C_1(s+1)] gives, for an absolute eps_0>0
and 0<eps<=eps_0,

    Pr(|r_s-r/(s+1)|>eps r/(s+1))
       <=C r^(3/2)exp[-c eps^2r/(s+1)^2].             (7)

## 2. Growing good profiles

For large r put L=floor(sqrt(r)/(log r)^2), eps=1/log r. A profile is
good when

    (1-eps)r/(s+1)<=r_s<=(1+eps)r/(s+1),
                          0<=s<=L+1.                 (8)

The s=0 condition is automatic. Union bounding (7) gives

    Pr(bad)<=C L r^(3/2)exp[-c eps^2r/(L+2)^2]
            <=C r^2 exp[-c'(log r)^2].                (9)

Thus (H+2)Pr(bad)=o(1), even uniformly for H<r. This is an absolute
incidence-mass estimate, without normalization by mu_H.

At a good profile set, for 0<=s<L,

    ell_s=r_s-2r_(s+1)+r_(s+2),       p_s=2r_(s+1)+1,
    q_s=ell_s/(p_s+ell_s)=ell_s/[r_s+r_(s+2)+1],
    N_s=s+1.                                          (10)

The ell_s are nonnegative but need not individually approximate their
formal means; near L they are often small integers. We use weighted
sums instead.

## 3. Deterministic weighted profile bounds

Define

    Phi=sum_(s=0)^(L-1) N_s q_s,
    A_t=sum_(s=t+1)^(L-1)(s-t)q_s,
    B_L=sum_(t=0)^(L-1)(t+1)q_t exp(-2A_t).

Uniformly on (8),

    Phi>=log L-C,       B_L<=C.                        (11)

Here are the summation details. Put d_L=r_L-r_(L+1). Convexity and
(8), with m=floor(L/2), give

    d_L<=[r_m-r_L]/(L-m)<=Cr/L^2,       r_L<=Cr/L.     (12)

Put D=1+eps+(L+1)/(2r). Since r_s+r_(s+2)+1<=2rD/(s+1),

    Phi>=(2rD)^(-1)sum_(s=0)^(L-1)(s+1)^2ell_s,

    sum_(s=0)^(L-1)(s+1)^2ell_s
       =r+2sum_(j=1)^(L-1)r_j-(2L-1)r_L-L^2d_L.

The last expression is at least 2(1-eps)r log L-Cr. Since
eps log L=O(1) and (L/r)log L=o(1), the first bound in (11) follows.

For A_t use the sharper upper denominator bound

    r_s+r_(s+2)+1<=2rD(s+2)/[(s+1)(s+3)].

Put g_s=(s-t)[(s+2)-1/(s+2)], s>=t. Then

    A_t>=(2rD)^(-1)sum_(s=t+1)^(L-1)g_s ell_s.

Its first summation coefficient g_(t+1) is at least two, and its
interior second differences are

    g_s-2g_(s-1)+g_(s-2)
       =2+2(t+2)/[s(s+1)(s+2)]>=2.

For t<=L-2 the final boundary terms are exactly

    -[g_(L-1)-g_(L-2)]r_L-g_(L-1)d_L.

They are O(r) uniformly in t, using (12), g_(L-1)=O(L^2), and
g_(L-1)-g_(L-2)=O(L). Therefore

    A_t>=alpha log[L/(t+1)]-C,       alpha=(1-eps)/D.  (13)

The empty case t=L-1 satisfies this too. For large r, a=2alpha is
in [1,2]. Since q_t<=C(t+1)ell_t/r, (13) gives

    B_L<=[C/(rL^a)]sum_(t=0)^(L-1)(t+1)^(a+2)ell_t.

The second differences of (t+1)^(a+2) are at most C(t+1)^a,
uniformly for a in [1,2]. Summation by parts has nonpositive final
boundary terms. Dropping them and using (8) gives

    sum_(t=0)^(L-1)(t+1)^(a+2)ell_t
       <=Cr+Cr sum_(j=1)^(L-1)(j+1)^(a-1)
       <=CrL^a.

This proves B_L<=C.

## 4. The exact cost of an adaptive branching path

Conditional on the FULL original profile, the arrays Z_s are independent
uniform weak compositions of ell_s into p_s parts. Their chronological
queries are original slots 0,-1,-2,... . Let W_s be the sum of the n_s
queried coordinates. The accepted clock recurrence is

    n_s=N_s+2sum_(t<s)(s-t)W_t,
    m_L=1+2sum_(s<L)W_s.                               (14)

Thus n_s depends only on EARLIER original rows. No reached root is
sampled afresh.

For a uniform composition of ell into p parts, the sum of n distinct
specified coordinates has exact law

    P(w;n)=binom(w+n-1,w)
           binom(ell-w+p-n-1,p-n-1)/binom(ell+p-1,p-1).

Put P0(n)=P(0;n), q=ell/(p+ell). If n>=N, then

    P0(n)/P0(N)
      =product_(j=N)^(n-1)(p-1-j)/(ell+p-1-j)
      <=exp[-(n-N)q].                                 (15)

If 0<=w<=ell and p>=2(n+w), the exact relative mass is

    P(w;n)/P0(n)
      =binom(n+w-1,w)(ell)_w/(ell+p-n-1)_w
      <=[2(n+w)q]^w/w!,                               (16)

with falling factorials. Impossible values have probability zero;
zero exponents and empty products have their usual value one.

On any nonnegative path with sum W_s<=K, (14) implies
n_s<= (2K+1)N_s and n_s+W_s<=3(K+1)N_s. Assuming
p_s>=2(n_s+W_s) on every such path, multiply (15)-(16) to obtain

    Pr(path | profile)
      <=Q0 product_(t=0)^(L-1)
        [6(K+1)N_t q_t exp(-2A_t)]^(W_t)/W_t!,
    Q0=product_(s=0)^(L-1)P0_s(N_s).                  (17)

The accumulated exponential penalty follows from the exact identity

    sum_s(n_s-N_s)q_s=2sum_t W_t A_t.

Also Q0<=exp(-Phi)<=C/L. Summing (17) over all paths by the multinomial
theorem and using (11) gives

    Pr(sum_(s<L)W_s<=K | profile)
      <=Q0 sum_(k=0)^K [6(K+1)B_L]^k/k!
      <=(C/L)exp[C(K+1)].                             (18)

This uses exact within-row composition laws, not independence of the
coordinates in a row. The row process can be defined abstractly by
(14); on a short physical clock satisfying the circumference conditions,
it is precisely the actual genealogy.

## 5. Apply the bound to actual short lifetimes

On (8), p_s>=c_0 sqrt(r)(log r)^2 for all s<L, with absolute c_0>0.
For the fixed Gaussian constant c and large r,
all these circumferences exceed G=2H+1. The physical clock construction
therefore applies through depth L on T<=H.

Consider h>=2L. Every depth-L T leaf has physical length at least
2(h-L)+1, so disjointness and (14) imply

    sum_(s<L)W_s
      <={G/[2(h-L)+1]-1}/2
      <=H/[2(h-L)]<=H/h.

Take K=ceil(H/h). On the relevant event h<=H, K>=1, and for h>=2L
it is O_c((log r)^2). Every path of total at most K consequently has
n_s+W_s<=C_c sqrt(r), whereas p_s>=c_0 sqrt(r)(log r)^2. Thus all row
hypotheses in (16)-(18) hold. Uniformly on these FULL profiles,

    Pr(T<=H | profile)
       <=(C/L)exp[C(1+H/h)],
                 for good profiles with h>=2L.         (19)

Height is measurable from the full profile. Dropping the good-profile
indicator after (19) therefore makes no independence assumption.

## 6. Inverse-height integration

The accepted uniform exact-height coefficient bound is

    [x^r]Z_h(x)<=C4^r(h+2)^(-4)
                         exp[-r/(2(h+2)^2)].          (20)

Retaining its prefactor gives a small-height tail without a power of r.
For h<=m, split its exponential into two equal halves. One half is at
most exp[-r/(4(m+2)^2)]. The remaining complete height sum satisfies

    sum_(h>=1)(h+2)^(-4)exp[-r/(4(h+2)^2)]
       <=Cr^(-3/2),

by its integral bound or a dyadic split at sqrt(r). Division by
Cat_r>=c4^r r^(-3/2) gives

    Pr(h<=m)<=Cexp[-r/(4(m+2)^2)].                     (21)

Thus X=sqrt(r)/(h+2) has a uniform sub-Gaussian upper tail, and

    E exp(tX)<=Cexp(Ct^2),       t>=0.                  (22)

This follows directly by integrating
1+t integral_0^infinity exp(tx)Pr(X>x)dx.

Bad profiles contribute o(1) to mu_H by (9). Roots with h<2L contribute
at most

    (H+2)Cexp[-r/(4(2L+2)^2)]=o(1)                    (23)

by (21). On the other profiles, (19) bounds the raw incidence by

    [C(H+2)/L] E exp[C(1+H/h)].

For h>=2L and large r, H/h<=2cX. Extend the expectation to all heights
after this bound, and apply (22) at the fixed parameter 2Cc. The last
display is at most C_c H/L<=C_c(log r)^2. Together with (9) and (23),
this proves (1).

## 7. Scope and inputs

Profile concentration concerns original uniform Dyck roots. The
branching calculation conditions on their full profile and uses
independent ROWS of original arrays, with exact within-row laws.
Reached clocks enter only through the accepted deterministic partition.

The occupied fraction is still mu_H E_inc[1/K_overlap]. Its vanishing
requires another overlap estimate; no such estimate is asserted here.

Source inputs: pbbs_gaussian_clock_genealogy_structural_audit.md,
Sections 1-5, for profile fibres, persistent slot order and clocks;
pbbs_growing_budget_uniform_bound.md, equation (18), for (20). The
marked-fringe Chernoff estimate, weighted profile bounds and adaptive
path summation are proved above.


<!-- END COMPLETE SOURCE 34 -->


---

<a id="document-35"></a>

## Document 35: pbbs_zero_budget_gaussian_band_weighted_lower_bound.md

Source: `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_zero_budget_gaussian_band_weighted_lower_bound.md`

[Portable document](sources/essential/c69c/research_round1/pbbs_zero_budget_gaussian_band_weighted_lower_bound.md) · [Exact original](originals/c69c/research_round1/pbbs_zero_budget_gaussian_band_weighted_lower_bound.md)

<!-- BEGIN COMPLETE SOURCE 35 -->

# True zero-budget Gaussian bands have nonvanishing length-weighted mass

Date: 2026-09-07. Pure proof; no computation or original-source edits.

For every fixed 0<a<b, the TRUE newborn class

    E_(r;a,b)={D in Dyck_r: T(D)=ht(D),
                         a sqrt(r)<=ht(D)<=b sqrt(r)}

has probability Theta_(a,b)(r^(-1/2)). Its length-weighted mass converges
to a strictly positive constant. Consequently, for every fixed c>0,
short complement repair intervals at cutoff H=floor(c sqrt(r)) have
total physical edge incidence Omega_c(W), even though their newborn
count is o_c(W) by the accepted Gaussian theorem.

These are incidence and energy lower bounds. They are not lower bounds
for an edge-disjoint packing, distinct damaged targets, or the optimal
cost of a construction that shares repairs.

## 1. Exact generating function and the limiting density

Use the accepted full zero-budget identity

    G_h(x)=sum_(D: ht(D)=T(D)=h) x^(|D|_up)
          =x^h/[F_(m_1)(x)F_(m_2)(x)F_(m_3)(x)],      (1)

where F_0=F_1=1, F_m=F_(m-1)-xF_(m-2), and m_1,m_2,m_3 are
balanced integers with sum 2h+1. In particular m_i/h->2/3 and

    G_h(1/4)=2/product_(i=1)^3(m_i+1)
             ~27/(4h^3).                              (2)

The positive determinant factorization is

    F_m(x)=product_(k=1)^floor(m/2)(1-4q_(m,k)x),
    q_(m,k)=cos^2(pi*k/(m+1)).                          (3)

Normalize the coefficients of G_h at x=1/4. Their size variable N_h is
h plus the sum of independent geometric variables on {0,1,...}, with
parameters q_(m_i,k). For each fixed k, its geometric variable divided
by h^2 converges to an exponential of rate

    lambda_k=9 pi^2 k^2/4.

The sum of the means of the modes k>K, divided by h^2, is O(1/K),
uniformly in h: use sin(pi*k/(m+1))>=2k/(m+1). Thus

    N_h/h^2 -> Y=sum_(i=1)^3 sum_(k>=1) E_(i,k),       (4)

where the E_(i,k) are independent exponentials of rate lambda_k.
The sum is finite almost surely. Its Laplace transform is

    E exp(-uY)=[(2sqrt(u)/3)/sinh(2sqrt(u)/3)]^3.       (5)

The value at u=0 is one, and E Y=2/9, agreeing with the geometric
mean identity sum_k q_(m,k)/(1-q_(m,k))=m(m-1)/6.

Let g denote the density of Y, extended by zero on (-infinity,0]. It is
continuous and strictly positive on (0,infinity). For positivity, split
off one exponential X and call
the remaining sum V. Every finite partial sum of V can be arbitrarily
small with positive probability, and its independent tail has arbitrarily
small mean. Hence P(V<t)>0 for every t>0. The convolution density
E[lambda_1 exp(-lambda_1(t-V))1_(V<t)] is then positive.

## 2. Uniform local limit, rather than only weak convergence

Keep the k=1 geometric mode from two of the three determinant factors.
Their parameters satisfy 1-q=Theta(h^(-2)). At Fourier argument t/h^2,
with |t|<=pi h^2, their product of characteristic-function moduli is
bounded by

    C/(1+t^2),                                        (6)

using
|1-q exp(i theta)|^2=(1-q)^2+2q(1-cos theta)
and 1-cos theta>=2theta^2/pi^2 for |theta|<=pi.
All other factors have modulus at most one. The same integrable bound
holds for the limiting characteristic function.

Pointwise convergence from (4), followed by dominated convergence in
Fourier inversion, therefore gives the UNIFORM lattice local limit

    sup_(n in Z) |h^2 P(N_h=n)-g(n/h^2)| -> 0.         (7)

The supremum follows because the Fourier L1 error bounds the inversion
error uniformly in n/h^2. In particular, (7) is uniform when r/h^2
stays in any compact subset of (0,infinity). This also proves the
continuity used above. No unproved local central limit theorem is assumed.

Since

    [x^r]G_h(x)=4^r G_h(1/4) P(N_h=r),

(2) and (7) yield, uniformly on every fixed positive Gaussian band,

    [x^r]G_h(x)
      =4^r h^(-5)[(27/4)g(r/h^2)+o(1)].               (8)

Divide by Cat_r~4^r/(sqrt(pi)r^(3/2)). Define

    kappa(u)=(27sqrt(pi)/4) u^(-5) g(u^(-2)), u>0.     (9)

It is continuous and positive, and uniformly for a<=h/sqrt(r)<=b,

    P_(Dyck_r)(T=ht=h)
       =r^(-1)[kappa(h/sqrt(r))+o(1)].                 (10)

## 3. Band counts and weighted limits

Riemann summation of (10) proves

    sqrt(r) P(E_(r;a,b)) -> K_(a,b),
    K_(a,b)=integral_a^b kappa(u) du>0.                (11)

In particular this proves both sides of the claimed Theta(r^(-1/2))
estimate. More generally, for each fixed integer j>=0,

    r^((1-j)/2) E[(T+2)^j 1_(E_(r;a,b))]
       -> integral_a^b u^j kappa(u) du.                (12)

The +2 affects no leading constant in a positive Gaussian band.
For j=1 the limit is a strictly positive finite constant; for j=2 the
unscaled moment has order sqrt(r).

## 4. Actual short-run incidence and rank energy

Fix c>0 and choose any 0<a<b<c. Put H=floor(c sqrt(r)). Every root
in E_(r;a,b) has T+1<=H for sufficiently large r. Therefore

    liminf E[(T+2)1_(T+1<=H)]
       >= integral_a^b u kappa(u)du>0,                 (13)

and

    liminf r^(-1/2) E[(T+2)^2 1_(T+1<=H)]
       >= integral_a^b u^2 kappa(u)du>0.               (14)

The exact rank-energy weight has the additional lower bound

    liminf E(H-T)_+
       >= integral_a^b(c-u)kappa(u)du>0.               (15)

Indeed (10) applies uniformly to the band and
(H-h)/sqrt(r)->c-u. The same positive lower bound holds with (H-T-1)_+;
the subtraction of one changes the band contribution by O(r^(-1/2)).

Let W=(2r+1)Cat_r and let I_H denote the full physical family of
complement residence intervals with T+1<=H. Each gap start contributes
one such interval, of T+2 edges. The exact identities are

    sum_(I in I_H)|I|=W E[(T+2)1_(T+1<=H)],
    E_H(P_r)=W E(H-T)_+.                              (16)

Consequently (13)-(15) prove

    sum_(I in I_H)|I|=Omega_c(W),
    E_H(P_r)=Omega_c(W),
    sum_(I in I_H)|I|^2=Omega_c(W sqrt(r)).             (17)

The quadratic raw run charge ell(ell+1)/2, with ell=T+1, likewise has
total Omega_c(W sqrt(r)); its band limit constant is one half of the
integral in (14). Already the zero-budget band alone supplies all of
these lower bounds.

The accepted global zero-budget upper bound
P(T=ht)=O(r^(-1/2)) also shows that its cutoff-H length-weighted mass
is O_c(1). Thus the contribution of the zero-budget class itself to the
first quantity in (17) is Theta_c(W), rather than only Omega_c(W).

## 5. Scope for a repair ledger

These estimates coexist with the accepted full newborn rarity
P(T+1<=H)=o_c(1). In fact (11) gives the complementary lower bound

    P(T+1<=H)=Omega_c(r^(-1/2)).                       (18)

Thus it is impossible to strengthen the TRUE unweighted short-run count
to o_c(W/H) at a fixed Gaussian cutoff. This says nothing comparable
about the maximum edge-disjoint subfamily.

There is also an immediate monotonic consequence for larger cutoffs.
If H_r/sqrt(r)->infinity, a single fixed band E_(r;a,b) still lies below
H_r for all large r. Therefore

    |I_(H_r)|>=c_(a,b) W/sqrt(r),
    H_r |I_(H_r)|/W -> infinity.                        (19)

This uses inclusion of one fixed band, not a new rate or limit theorem
with growing c. In particular, the RAW census requirement (9.1) in
MATH_THEOREM_RUNLENGTH_CRITERION_AND_CENTRAL_UCYCLE_EQUIVALENCES_20260820.md
is impossible: its left side includes this fixed band and is at least
Omega(4^r/r^2), whereas (9.1) asks for o(4^r/(r^2 sqrt(log r))).
This rejects that stronger raw-count sufficient route only. The
residence-packing criterion and a construction that shares repairs
remain undecided by the lower bound.

The raw sum of repair-interval lengths is not o(W). A ledger charging
every run separately at a fixed positive cost per interval edge therefore
has an Omega(W) charge. A quadratic raw per-run ledger has an
Omega(W sqrt(r)) charge. An H-per-run charge also has an Omega_c(W)
contribution from (11). These facts rule out those raw sums being
negligible; they do not prove that every legal repair must pay those sums.

Intervals can overlap, one cut can hit several intervals, and targets
can be represented more than once. Accordingly (17) proves neither a
packing lower bound nor a distinct-target-loss lower bound. To obtain
an o(W) repair contribution one needs an argument that shares, clusters,
discounts, or otherwise avoids the separate raw incidence charges.

Sources: the accepted exact product in
research_round1/pbbs_original_forest_product.md, Section 5; its positive
geometric factorization as used in pbbs_zero_budget_uniform_bound.md;
and the exact physical dictionary in
pbbs_gaussian_age_residual_and_cut_charges.md, Sections 1 and 5.

## Appendix. An elementary certificate for the positive weighted lower bound

The positive lower bounds in (17)-(18) also follow without a local limit
theorem, if explicit constants for every prescribed band are not needed.
Choose 0<a<b<min(c,1/2). Separate one largest-parameter geometric G
from the normalized size in Section 1, writing N_h=h+G+R with G and R
independent. For all sufficiently large h,

    E R<=h^2,       1-q=Theta(h^(-2)),

where q is the parameter of G. For a sqrt(r)<=h<=b sqrt(r), Markov's
inequality gives P(R<=r/2)>=1-2b^2>1/2. For large r, on that event,
0<=r-h-R<=r. Consequently

    P(N_h=r)
      >= (1/2)(1-q)q^r
      >= c_1 h^(-2) exp[-c_2 r/h^2]
      >= c_(a,b) h^(-2).

Multiply by G_h(1/4)=Theta(h^(-3)) and 4^r. Summing the resulting
coefficient lower bound over this positive Gaussian band gives
P(E_(r;a,b))>=c'_(a,b)/sqrt(r). Multiplication by h, h^2, or H-h
gives the positive first-moment, second-moment, and rank-energy lower
bounds used in (17). The exact constants for arbitrary fixed bands remain
those obtained by the uniform local limit above.

## Appendix B. Global zero-budget moments and their exact constants

The accepted uniform coefficient bound supplies both tails missing from
the fixed-band local limit. This appendix and all constants below passed
an independent analytic audit on 2026-09-07. Put chi=1{T=ht} and

    nu_r=sqrt(r) sum_h P(T=ht=h) delta_(h/sqrt(r)).

Equation (10) gives vague convergence of nu_r on (0,infinity) to
kappa(u)du. For an absolute C the uniform-bound note gives, for h>=2,

    P(T=ht=h) <= C r^(3/2) (h+1)^(-5)
                   exp[-(r-h)/(2(h+1)^2)].             (B1)

For r>1 the h=1 class is empty. If h<=a sqrt(r), then h<=r/2 for
sufficiently large r. For each j=0,1,2, Riemann summation in (B1) gives

    limsup_r integral_(0,a] u^j dnu_r
      <= C_j integral_0^a u^(j-5) exp[-1/(4u^2)]du
      ->0 as a decreases to zero.                      (B2)

For the high tail, drop the exponential and sum the power. This yields

    limsup_r integral_(b,infinity) u^j dnu_r
      <= C'_j b^(j-4) ->0 as b increases to infinity.  (B3)

Thus vague convergence extends to the total mass and the first two
moments. With y=u^(-2), equation (9) gives

    integral_0^infinity u^j kappa(u)du
      =(27 sqrt(pi)/8) E[Y^(1-j/2)],  j=0,1,2.         (B4)

Since EY=2/9, the count constant is 3sqrt(pi)/4. The +2 in repair
lengths has no effect on these leading limits: its error terms are
controlled by the already bounded lower moments. Consequently

    sqrt(r) P(T=ht) -> 3sqrt(pi)/4,
    E[(T+2)chi] -> (27sqrt(pi)/8) E[sqrt(Y)],
    r^(-1/2) E[(T+2)^2 chi] -> 27sqrt(pi)/8.            (B5)

The middle constant has a closed form. The fractional-moment identity
and the Laplace transform (5), with x=2sqrt(s)/3, give

    E[sqrt(Y)]
      =(1/(2sqrt(pi))) integral_0^infinity
          [1-E exp(-sY)] s^(-3/2) ds
      =(2/(3sqrt(pi))) I,
    I=integral_0^infinity [x^(-2)-x csch(x)^3]dx.       (B6)

These nonnegative integrals are legitimate by Tonelli; finiteness also
follows from E sqrt(Y)<=sqrt(EY). Put f(x)=csch(x), so f''=f+2f^3.
Integrating with lower cutoff epsilon gives exactly

    I_(epsilon,infinity)
      =1/epsilon+[epsilon f'(epsilon)-f(epsilon)]/2
        +(1/2) integral_epsilon^infinity x f(x)dx.

The expansion epsilon f'(epsilon)-f(epsilon)
=-2/epsilon+O(epsilon^3) cancels the boundary singularity. Hence

    I=(1/2) integral_0^infinity x csch(x)dx
      =sum_(n>=0) (2n+1)^(-2)=pi^2/8,
    E[sqrt(Y)]=pi^(3/2)/12.                            (B7)

The global zero-budget first repair-incidence limit is therefore

    E[(T+2)chi] -> 9pi^2/32.                           (B8)

In particular the complete zero-budget root count is asymptotic to
(3/4)4^r/r^2. On the full physical factor, its birth count is asymptotic
to (3sqrt(pi)/4)W/sqrt(r), its total full repair-edge incidence to
(9pi^2/32)W, and its quadratic repair-edge incidence to
(27sqrt(pi)/8)W sqrt(r). Replacing T+2 by T+1 gives the same first
constant for complement owner-coordinate incidence.

These remain raw incidence statements. The separate renewal-clustering
proof establishes sharing and small support; it is not a consequence
of the moment limits alone. All statements here concern T=ht only.


<!-- END COMPLETE SOURCE 35 -->


---

<a id="document-36"></a>

## Document 36: pbbs_original_forest_product.md

Source: `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_original_forest_product.md`

[Portable document](sources/essential/c69c/research_round1/pbbs_original_forest_product.md) · [Exact original](originals/c69c/research_round1/pbbs_original_forest_product.md)

<!-- BEGIN COMPLETE SOURCE 36 -->

# Original PBBS peeling forests: universal caps and an exact product law

Date: 2026-09-07. Pure proof; no computation or original-source edits.
The universal caps, graded bijection, exact zero-budget product, and
shifted-cap algebra were independently audited by the recency-gate agent
and reviewed by the root task. The subsequent first-packet majorant in
pbbs_growing_budget_first_packet_majorant.md yields the uniform growing-
budget estimate in pbbs_growing_budget_uniform_bound.md without using
the unproved maximum-excess coupling discussed below.

The terminal half-height caps previously used for T=h are universal for
the original formal peeling of every height-h Dyck root. The suffixes
have complementary universal caps. Together these give an exact product
encoding of all height-h roots, before any statement about their newborn
lifetime. In particular, terminal-cap violations cannot measure the
interruption budget: there are no such violations.

The budget-dependent condition for T=h is instead ht(U_i)<=i. In the
exact original-root product law, these are independent forest events at
critical Boltzmann weight. This does not make subsequently reached marked
states independent, and no growing-budget coupling is asserted here.

## 1. Original formal peeling and universal prefix clearance

For an original height-h Dyck word D=A_0, define its full formal peeling

    A_i=L_i 1 R_i 0 U_i,
    A_(i+1)=L_i 0 R_i, read from height i+1,             (1)

for i=0,...,h-1. The selected up-step first reaches h and the selected
down-step first returns to zero afterward. Each A_i starts at i, ends
at zero, stays in [0,h], and attains h. The selected up-steps are the
original first-hitting steps of levels h,h-1,...,1. Thus the terminal
A_h starts at h and never revisits h after its first down-step.

For every i, the prefix through the last visit to h in A_i stays at
height at least i. This is a property of every original root, not only
of roots with T=h. To prove it forward, start with nonnegativity of A_0.
The prefix L_i before the first maximum lies in the protected prefix.
In A_(i+1) it is raised by one and ends at h, whereas the entire remainder
after the following down-step has height at most h-1. This proves the
induction.

Equivalently, in the inverse of (1), the cut at the last visit to h must
occur before any visit below the starting height. One can also prove this
by inverse persistence: an old prefix before a cut remains before every
later inverse cut and is lowered at each remaining inverse step. A vertex
below the current starting height would become negative in A_0.

No suffix cap ht(U_i)<=i is used in either argument.

## 2. Both universal forest caps

Decompose the terminal path by successive first descents:

    A_h=0 V_0 0 V_1 ... 0 V_(h-1).                     (2)

The original unrestricted cap of V_j is j, and its initial baseline is
h-1-j. The universal prefix clearance sharpens this to

    ht(V_j)<=ceil(j/2).                                (3)

Indeed, after k inverse operations, while the cut has remained before
this block, its baseline is h-1-j+k in the path starting at h-k. If
2k<j+1, that baseline is below the starting height, so the cut must stay
before the block and the block cannot attain h. Apply this at
k=floor(j/2), obtaining ht(V_j)<=j-k=ceil(j/2).

There is a complementary universal cap for the original suffixes:

    ht(U_i)<=h-ceil(i/2),       0<=i<h.                  (4)

For i=0 this is the ordinary height cap h. For i>=1, the suffix U_i starts
at baseline zero in A_i. After q inverse operations whose cuts stayed
before it, its baseline is q in the path starting at i-q. If 2q<i, the
baseline lies below the starting height. Universal prefix clearance
therefore keeps the next cut before U_i and forbids any height-h visit
inside it. The block remains unchanged and its baseline rises by one at
the next inverse operation. At q=floor((i-1)/2), absence of height h gives

    q+ht(U_i)<=h-1,
    ht(U_i)<=h-1-floor((i-1)/2)=h-ceil(i/2).

Both proofs permit later cuts to split or transport the forest once its
baseline is no longer below the current start. They do not assume that
the forest remains intact throughout the complete inverse.

## 3. The caps characterize the full original-root encoding

Let C_j(x) count Dyck words of height at most j, with C_0=1 and
C_j=1/(1-x C_(j-1)). Let F_0=F_1=1 and F_m=F_(m-1)-x F_(m-2), so
C_j=F_j/F_(j+1).

Consider all tuples of independent forest choices satisfying exactly

    ht(V_j)<=ceil(j/2),
    ht(U_i)<=h-ceil(i/2),              0<=i,j<h.         (5)

Assign degree h+sum ups(V_j)+sum ups(U_i). The original formal peeling
maps height-h roots injectively into these tuples: the terminal is (2),
and the canonical last-height-h inverse recovers the original word
uniquely whenever its admissibility checks pass.

The unrestricted generating function for the tuples in (5) is

    x^h product_(j=0)^(h-1) C_ceil(j/2)
        product_(i=0)^(h-1) C_(h-ceil(i/2)).             (6)

The combined multiset of caps contains h once, each of 1,...,h-1 twice,
and zero once. Consequently (6) equals

    x^h C_h [product_(j=0)^(h-1) C_j]^2
      = x^h/(F_h F_(h+1))
      = C_h-C_(h-1).                                   (7)

The last expression is exactly the generating function for all roots
of height h. Each degree contains finitely many tuples and finitely many
roots. The injection and coefficient equality therefore prove surjectivity.

Thus every tuple obeying the two universal caps (5) passes all canonical
inverse admissibility checks, and the encoding is a bijection. This
conclusion follows from a graded counting argument; the checks have not
been silently discarded during an attempted reconstruction.

## 4. Exact critical product law

At x=1/4, give a forest W with cap m the normalized law

    P_m(W)=4^(-ups(W))/C_m(1/4),
    C_m(1/4)=2(m+1)/(m+2).                              (8)

Choose all V_j and U_i independently with their caps in (5), and reconstruct
the unique original root. By (7), its law is precisely

    P(D)=4^(-semilength(D)) / [C_h(1/4)-C_(h-1)(1/4)],
    C_h(1/4)-C_(h-1)(1/4)=2/[(h+1)(h+2)].              (9)

This is a law on original rooted words with varying semilength. Conditional
on semilength r, it is uniform on roots of height h, but the forest choices
are then coupled by their total size. No product-law assertion is made
for a subsequently reached marked state or for fixed semilength without
that conditioning.

## 5. Exact uninterrupted counting function

The exact suffix characterization already established by record peeling is

    T(D)=h  iff  ht(U_i)<=i for every 0<=i<h.            (10)

Combining (10) with the bijection in Section 3 gives the exact identity

    G_(h,h)(x)
      = x^h product_(j=0)^(h-1) C_ceil(j/2)
          product_(i=0)^(h-1) C_min(i,h-ceil(i/2)).      (11)

This also resolves the inverse indicators in the earlier zero-budget
upper bound: once both universal caps are retained, no further inverse
restriction remains. The earlier upper bounds are still valid.

There is a compact form. Let a,b,c be the three integers differing by
at most one whose sum is 2h+1. Then

    G_(h,h)(x)=x^h/[F_a(x) F_b(x) F_c(x)].               (12)

To check the cap multiset, for j>=1 the number of factors in (11) whose
cap is at least j is

    max(0,h-2j+1)
      + max(0,min(h-1,2h-2j)-j+1)
      = max(0,2h+1-3j).                                (13)

Writing 2h+1=3q+r with r in {0,1,2}, the exponent of C_j is therefore
three for 1<=j<q, r for j=q, and zero above q. Telescoping gives
F_q^(3-r) F_(q+1)^r in the denominator, proving (12).

At critical weight,

    G_(h,h)(1/4)=2/[(a+1)(b+1)(c+1)]
                 ~ 27/(4h^3).                         (14)

This is an equality for the full uninterrupted class; it does not identify
that class with a previously proposed stable-spine cone.

## 6. Where growing-budget defects must be measured

Terminal caps (3) have no defects for any original root, so counting their
violations cannot distinguish B=T-h=0 from B>0. In contrast, the stricter
suffix conditions (10) can fail.

Under the exact product law (8), put M_i=h-ceil(i/2). The indicators
1{ht(U_i)>i} are independent, with probabilities

    q_i=0                                      if M_i<=i,
    q_i=(M_i-i)/[(i+2)(M_i+1)]                  if M_i>i. (15)

This follows by dividing C_i(1/4) by C_(M_i)(1/4). Their joint absence
has the exact probability

    P(T=h)=(h+1)(h+2)/[(a+1)(b+1)(c+1)].                (16)

For a growing-budget argument, a new structural result would have to
relate the actual interruption budget to these original suffix defects,
their excess heights, or another function of the exact independent
original forests. No bound of the form B>=number of defects, no bound
on their total height excess, and no analogous coupling is proved here.
The availability of the product law alone does not establish such a
coupling or a growing-budget density estimate.

## 7. Exact shifted-cap partition, without a budget assertion

For 0<=J<=h, let K_(h,J)(x) count original roots satisfying

    ht(U_i)<=i+J for every 0<=i<h.                       (17)

This is a precisely defined positive family, whether or not it contains
every root with interruption budget at most J. By the product bijection,

    K_(h,J)(x)
      = x^h product_(j=0)^(h-1) C_ceil(j/2)
          product_(i=0)^(h-1) C_min(i+J,h-ceil(i/2)).    (18)

Let a,b,c be balanced integers with sum 2h+1+J. Then

    K_(h,J)(x)=x^h F_J(x)/[F_a(x) F_b(x) F_c(x)].        (19)

For an explicit check, the number N_j of factors in (18) with cap at
least j is

    N_j=2h+1-2j                         for 1<=j<=J,
    N_j=max(0,2h+1+J-3j)                for j>J.         (20)

Thus the cap exponents are two below J and three from J up to the final
balanced truncation. Telescoping produces F_J in the numerator of (19).
Equation (18), rather than the alternating-coefficient numerator alone,
is the positive partition underlying this identity.

At critical weight the formula is particularly simple:

    K_(h,J)(1/4)=2(J+1)/[(a+1)(b+1)(c+1)]
                 =O((J+1)/(h+1)^3), uniformly 0<=J<=h. (21)

The cases J=0 and J=h recover respectively the exact uninterrupted
count and the full height-h count. No statement

    T-h<=J  implies  ht(U_i)<=i+J

has been proved here. Establishing that implication, a weakened version
with a controlled multiple of J, or a counterexample is the remaining
structural step before using (18)-(21) as a growing-budget majorant.


<!-- END COMPLETE SOURCE 36 -->


---

<a id="document-37"></a>

## Document 37: pbbs_uninterrupted_record_peeling.md

Source: `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_uninterrupted_record_peeling.md`

[Portable document](sources/essential/c69c/research_round1/pbbs_uninterrupted_record_peeling.md) · [Exact original](originals/c69c/research_round1/pbbs_uninterrupted_record_peeling.md)

<!-- BEGIN COMPLETE SOURCE 37 -->

# PBBS uninterrupted lifetimes: exact suffix caps and record peeling

Date: 2026-09-07. Pure proof; no computation, enumeration, or original-source
modification. This note records the suffix-cap characterization and active-path
compression proposed by the uninterrupted-weight agent and independently
audited by the caps-audit agent.

For every exact height h, the complete class of roots with newborn lifetime
T=h admits a unique record-peeling encoding. The encoding yields the
coefficientwise bound

    G_(h,h)(x) <= x^h / F_h(x)^2,

where F_0=F_1=1 and F_h=F_(h-1)-x F_(h-2) for h>=2. In particular,

    G_(h,h)(1/4) <= 1/(h+1)^2.

This is a bound for the full uninterrupted class, not an identification with
a stable-spine cone. It does not supply a uniform exponential weight bound,
a growing-lifetime coefficient estimate, or a Gaussian-scale short-run
density estimate.

Follow-up: pbbs_uninterrupted_critical_weight.md strengthens the terminal
forest caps and the critical upper bound to O(h^(-3)). Its coefficient
transfer in pbbs_zero_budget_uniform_bound.md bounds the complete T=h
class, summed over all heights, by O(4^r/r^2). These later improvements
use the exact encoding proved here and do not cover positive budgets.

## 1. Exact map, conventions, and prior inputs

Use the exact first-maximum/first-return factorization

    D=P 1 R 0 S,              tau(D)=S 1_new P 0 R.       (1)

Here D is a nonempty rooted Dyck word of exact height h. The displayed old
up-step is the first step attaining h, and the displayed old down-step is
the first subsequent return to height zero. All letters in P,R,S retain
their identities. The displayed new up-step is newly planted. Height h is
invariant under tau.

Let D_0=D and D_j=tau^j(D). Plant the marked up-step in the update D_0 -> D_1.
Its newborn lifetime T(D) counts the subsequent updates beginning with
D_1 -> D_2 and ending with, and including, the update consuming that mark.
Thus T=h means the mark survives the h-1 updates out of D_1,...,D_(h-1)
and is consumed in the update out of D_h.

The exact map and height invariance are the inputs from
PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md, Sections 8 and 9. The corrected
marked-height accounting, audited in pbbs_q6_independent_audit.md, is

    T=h+2 rho+sigma.                                      (2)

Here rho and sigma count the nonconsuming updates in which the marked
up-step lies in R and S, respectively. A mark in P rises by one height
unit; a mark in R falls by one; a mark in S keeps its height. In particular,
T=h holds exactly when all h-1 surviving updates put the mark in P.

For a possibly empty Dyck word W, ht(W) denotes its maximum height, with
ht(empty)=0. Maximum and minimum heights of paths include their endpoints.

## 2. Complete dynamic suffix-cap characterization

Let S_i be the canonical suffix S(D_i) in (1). Then

    T(D)=h  iff  ht(S_i)<=i for every 0<=i<h.              (3)

To prove this, suppose first that the mark has survived only in P before
state D_j. The word B_j preceding the mark in D_j is then exactly

    B_j=S_(j-1) 1 S_(j-2) 1 ... 1 S_0.                  (4)

There are j-1 ordinary up-steps between these suffixes. The formula starts
with B_1=S_0. A further P update sends this prefix to S_j 1 B_j, proving
the induction. Each S_i is a Dyck word, so B_j ends at height j-1 and

    maxheight(B_j)
      = max_(0<=i<j) [j-1-i+ht(S_i)].                    (5)

If every cap in (3) holds, (5) is at most j-1. For j<h, the mark itself
ends at height j<h, and no preceding up-step has reached h. Since D_j has
height h, its first maximum lies later, so the mark is in P. This proves
the induction through j=h. In D_h the mark reaches h and no earlier step
does; the next update consumes it, giving T=h.

Conversely, T=h and (2) force every surviving update to be P. Formula (4)
therefore holds at D_h. Consumption there requires maxheight(B_h)<=h-1.
Equation (5), with j=h, gives ht(S_i)<=i for every i<h.

Both endpoints matter: the i=0 cap says S_0 is empty, and the final
i=h-1 cap is required for consumption. Initial emptiness alone is not
sufficient. For example, the independently audited height-three family
D=1(1100)^q0 has S_0 empty but lifetime 3q; for q>=2 its suffix S_1 has
height two and violates the cap ht(S_1)<=1.

## 3. A formal active-path process for every initial root

Define a formal process independently of whether (3) holds. A_i is a
path starting at height i, ending at zero, staying in [0,h], and attaining
h. Set A_0=D. For 0<=i<h, since its initial height is less than h, A_i
has a first up-step attaining h. Factor

    A_i=L_i 1 R_i 0 U_i,                                (6)

at that up-step and the first later return to zero, and put

    A_(i+1)=L_i 0 R_i, read from initial height i+1.       (7)

The suffix is denoted U_i here to distinguish it from S(D_i) until the
connection to the actual marked dynamics has been established.

In (6), L_i runs from i to h-1, stays in [0,h-1], and has no visit to h.
The path R_i runs from h to 1 and stays in [1,h]. The suffix U_i is an
ordinary Dyck word of height at most h.

In (7), the heights along L_i are increased by one. Thus this prefix
stays in [1,h] and ends at h. The displayed down-step leads to h-1.
The heights along R_i are decreased by one, so this remainder stays in
[0,h-1] and ends at zero. This proves that the process exists inductively
through A_h, with A_(i+1) staying in [0,h] and attaining h.

At each step an up-step is changed to a down-step, the subsequent return
down-step is deleted, and the terminal suffix U_i is discarded. No other
letters are changed or reordered.

### Which up-steps are selected

In the original word D, let u_k be the first up-step attaining level k.
The successive selected up-steps in (6) are precisely

    u_h, u_(h-1), ..., u_1.                             (8)

The case i=0 is the definition of u_h. For the induction, when
1<=i<h, the original prefix strictly before u_(h-i+1) is still an
unchanged initial prefix of A_i; previous selections and deletions
occurred later. Reading that prefix from height i, its first visit to h
occurs at the original step u_(h-i). This step precedes u_(h-i+1), so
the same property holds at the next stage.

Because u_1 is the first letter of a nonempty Dyck word, the final selected
up-step is the first letter of A_(h-1), and L_(h-1) is empty. Consequently

    A_h starts at h, begins with a down-step,
    and thereafter stays in [0,h-1] until ending at zero. (9)

In particular, A_h has no visit to h after its initial vertex.

## 4. Connection to the actual marked dynamics

The formal suffixes satisfy the exact equivalent criterion

    T(D)=h  iff  ht(U_i)<=i for every 0<=i<h.             (10)

For sufficiency, after planting, the actual marked word is

    D_1=U_0 * A_1,

where * is the marked up-step. Suppose that up to D_i the caps have kept
the mark in P. Its actual word is then

    D_i=B_i * A_i,
    B_i=U_(i-1) 1 U_(i-2) 1 ... 1 U_0.                 (11)

The prefix-height computation (5) gives maxheight(B_i)<=i-1. For i<h,
the first maximum therefore lies in A_i, at the selected step of (6).
Applying (1) to (11) gives

    D_(i+1)=U_i 1 B_i * L_i 0 R_i
           =(U_i 1 B_i) * A_(i+1).                    (12)

This proves the induction and shows that the actual suffix S(D_i) equals
the formal suffix U_i at every stage used. At D_h, the prefix cap makes
the mark the first up-step attaining h, hence T=h.

For necessity, T=h forces all P updates. Applying (12) successively
identifies the actual active paths and suffixes with the formal ones;
then (3) gives all the caps in (10).

Thus (10) describes the entire height-h, lifetime-h class. It does not
assume that every active path has only one arch, that later suffixes are
empty, or that original side forests stay in a fixed spine position.

## 5. Unique inverse and its exact admissibility check

An encoding consists of the terminal path A_h and the ordered suffixes
(U_0,...,U_(h-1)). To reconstruct, work backwards for i=h-1,...,0.

Given A_(i+1), locate its last visit to height h. The next step must be
a down-step, since the path stays at most h and ends at zero. This uniquely
factors its word as

    A_(i+1)=L_i 0 R_i,                                  (13)

with the cut immediately after that last height-h vertex. The suffix R_i
then stays at most h-1. The one additional inverse admissibility check is

    every height along the prefix L_i is at least 1.     (14)

If (14) holds, set A_i=L_i 1 R_i 0 U_i, reading it from height i.
The heights along L_i are lowered by one, so they stay in [0,h-1]. The
inserted up-step first reaches h. The heights along R_i are raised by
one, so they stay in [1,h], ending at 1. The inserted down-step is
therefore the first subsequent return to zero. Appending a Dyck suffix
U_i of height at most i preserves the required range [0,h].

This proves that (14), together with the stated terminal-path and suffix
conditions, is sufficient as well as necessary. Necessity follows because
every forward prefix L_i was raised from a nonnegative path. The last
height-h visit in (13) is the correct cut: the forward prefix ends at h,
whereas the entire remainder after its next down-step stays at most h-1.

Starting from (9), and passing (14) at each inverse step, therefore
reconstructs a unique original Dyck word D whose formal suffixes are
exactly the prescribed U_i. By (10), this word has T=h. Conversely every
height-h root with T=h supplies such an admissible tuple. We have a
bijection with the tuples that pass all inverse checks, and an injection
into all tuples obeying only the terminal condition (9) and ht(U_i)<=i.

The inverse tests must not be silently omitted when asserting equality
of generating functions. Omitting them is legitimate for an upper bound.

## 6. The coefficientwise generating-function bound

Let C_j(x) count Dyck words of height at most j by their number of up-steps:

    C_0(x)=1,
    C_j(x)=1/(1-x C_(j-1)(x)) for j>=1.                 (15)

Let G_(h,h)(x) count original roots of exact height h and lifetime h by
semilength. The unrestricted suffix tuple contributes

    product_(i=0)^(h-1) C_i(x).                          (16)

The terminal paths in (9), weighted by their number of up-steps, have
the same generating function. For an explicit decomposition, the first
step is the compulsory descent from h to h-1. Before the first descent
from a later level j to j-1, the intervening segment is a Dyck excursion
above j with relative height at most h-1-j. After the first arrival at
zero, the remaining tail is a Dyck word of height at most h-1. These
unique pieces contribute C_0,C_1,...,C_(h-1), once each; all separating
down-steps have weight one.

At each forward step (7), the number of up-steps drops by
1 plus the number of up-steps in U_i. Hence

    semilength(D)=h+ups(A_h)+sum_(i=0)^(h-1) ups(U_i).    (17)

The injection at the end of Section 5 now gives, coefficientwise,

    G_(h,h)(x) <= x^h [product_(j=0)^(h-1) C_j(x)]^2.   (18)

For the continuant convention used here, define

    F_0(x)=F_1(x)=1,
    F_h(x)=F_(h-1)(x)-x F_(h-2)(x) for h>=2.            (19)

Equation (15) gives C_j=F_j/F_(j+1), so the product telescopes:

    product_(j=0)^(h-1) C_j(x)=1/F_h(x).

Therefore the promised upper bound is

    G_(h,h)(x) <= x^h/F_h(x)^2.                         (20)

No equality is claimed in general. Both sides have nonnegative power
series, and at x=1/4 every finite C_j is finite. Since

    C_j(1/4)=2(j+1)/(j+2),

equation (18) yields

    G_(h,h)(1/4) <= (1/4)^h [2^h/(h+1)]^2
                 =1/(h+1)^2.                           (21)

The critical-weight bound is polynomial in h. It is not a proof of
exponential suppression in h and does not by itself estimate the
coefficient at semilength r uniformly when h grows with r.

## 7. Previously verified small-height checks

For h=1, a root is (10)^r and its newborn lifetime is r. Thus

    G_(1,1)(x)=x,

which agrees with (20), since F_1=1. The suffix cap requires U_0 empty,
and the terminal path is the single down-step.

For h=2, the independently verified complete T=2 class at exact height
two is

    D=(10)^a 1(10)^b 0,  a>=0, b>=1.

There are r-1 such roots at semilength r>=2, giving

    G_(2,2)(x)=x^2/(1-x)^2.

This agrees with (20), since F_2=1-x. These are height-specific checks;
the additional height-one root 1010 also has lifetime two but is counted
in G_(1,2), not in G_(2,2). No complete height-three formula is asserted
or needed here.

## 8. Scope and the remaining gap

The suffix criterion (3) and the admissible inverse encoding describe
the full class T=h. A stable-spine family, if separately proved to obey
these caps, is only a subfamily. Its proposed product formula cannot be
substituted for the full-class count, and no earlier cone formula or
pole claim is used in this proof.

The present upper bound follows by forgetting inverse constraints, not
by enumerating them. It supplies neither a uniform exponential bound
on the critical weight nor control of classes with interruptions
T=h+2 rho+sigma>h. In particular, no estimate for the full event T<=H
at H of order sqrt(r), and no Gaussian-scale density or packing conclusion,
has been obtained. All independent upper bounds for the original covering
problem remain separate from this result.


<!-- END COMPLETE SOURCE 37 -->


---

<a id="document-38"></a>

## Document 38: pbbs_q6_independent_audit.md

Source: `/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_q6_independent_audit.md`

[Portable document](sources/essential/c69c/research_round1/pbbs_q6_independent_audit.md) · [Exact original](originals/c69c/research_round1/pbbs_q6_independent_audit.md)

<!-- BEGIN COMPLETE SOURCE 38 -->

# Independent PBBS Q6 audit: primitive height-three words with unbounded exit time

Date: 2026-09-07. Pure proof, with no computation, enumeration, or source
modification.

**Verdict: Theorem Q6 is false.** For every integer q>=1, the primitive
Dyck word

    D_q = 1(1100)^q0

has height 3 and empty canonical terminal suffix S(D_q), but the letter
planted at its next tau-step has exact lifetime 3q. Thus neither the stated
height-plus-O(1) bound nor a uniform O(height) repair holds for all such
words. This disproves the asserted pointwise mechanism. It does not by
itself determine the density or packing of short runs in the canonical
cover.

## 1. Sources and prior overlap

The exact maps used below are proved in
PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md, Lemma 8.1 and Theorem 9.1.
For the first-maximum/first-return factorization

    D=P 1 R 0 S,

the exact two-step map is

    tau(D)=S 1_new P 0 R.                                (1)

Here the displayed old first-maximum up-step is consumed, the new divider
is the freshly planted coordinate, and all letters in P,R,S retain their
identities. This is also the necklace interpretation in Q1 of
MATH_THEOREM_PBBS_QUEUE_FLUSH_DYNAMICS_AND_RUN_CONSERVATION_20260820.md.

Prior overlap is significant. Section 23 of the residence-reduction file
and PBBS_ZERO_WINDING_CONVERSE_COUNTERAUDIT_20260725.md already retract a
different primitive height-time converse. Their first counterexample is
D_2=1110011000, exactly the q=2 case below, and they record its three-word
tau orbit. The present proof explicitly tracks the planted letter and
extends that example to a fixed-height family with arbitrarily long
lifetimes. No novelty claim is made for the individual q=2 word or its
orbit.

## 2. A fixed lifetime convention and the Q4 endpoint issue

Let T be the number of subsequent tau updates from the state immediately
after planting through the update that consumes the planted letter.
Equivalently, T counts the consecutive owner states in which that newly
entered coordinate is present. This is the convention under which planting
in 111000 gives T=3, as in the source's sanity check.

Before the final consuming update, let p,rho,sigma count the updates at
which the marked letter lies in P,R,S respectively. Its height starts at
1; a P update raises it by 1, an R update lowers it by 1, and an S update
leaves it unchanged. It is consumed at height h. Therefore

    p-rho=h-1,
    T-1=p+rho+sigma,
    T=h+2rho+sigma.                                      (2)

The height changes in Q3 are valid. The displayed Q4 identity with h-1
instead of h is valid only when its T excludes the final consuming update;
it does not use the same convention as the source's T=3 sanity check for
111000. This is an endpoint discrepancy of one, separate from the
unbounded error in Q6 established below.

## 3. Exact three-word orbit of the counterfamily

Put

    A=111000,    B=1100,
    D_q=1 B^q 0,
    E_q=A B^(q-1),
    F_q=B^(q-1) A.

D_q is primitive: after the initial 1, each B is read above baseline
height 1, and only the last 0 returns to height zero. Its height is 3.
Its first maximum is in the first B, and its first subsequent return to
zero is the last letter. Thus S(D_q) is empty.

The first-maximum factorizations are explicitly

    D_q = (11) 1 (00 B^(q-1)) 0,
    E_q = (11) 1 (00) 0 B^(q-1),
    F_q = (B^(q-1) 11) 1 (00) 0.

Applying (1) gives

    D_q -> E_q -> F_q -> D_q.                            (3)

For q=1 these three words coincide with A; otherwise they are three
distinct words. This harmless degeneracy does not affect the argument.

In particular, already at the planting step from the primitive D_q the
new word E_q consists of a height-three arch followed by q-1 complete
height-two arches. For q>=2 it is not a single arch, and its canonical
suffix S is nonempty. This directly contradicts the starting structural
assertion and the induction used in Q6.

## 4. Marked-letter evolution and exact lifetime

Mark the letter planted at D_q -> E_q. It is the first up-step of A in
E_q, at height 1.

The first subsequent update E_q -> F_q retains the mark in P. In F_q
it is the second up-step of the final A, at height 2. The next update
F_q -> D_q again retains it in P. It becomes the second up-step, hence
the peak, of the LAST B copy in D_q, at height 3.

Number the B copies in D_q from left to right by 1,...,q. Suppose the
mark is the peak of B_j with j>1. Under the three subsequent updates:

1. D_q -> E_q: the first maximum is in B_1, so the mark lies in R.
   It is moved to the peak of B_(j-1) in the trailing B forest, and its
   height drops from 3 to 2.
2. E_q -> F_q: the mark lies in S. That forest moves to the front,
   and the mark stays at height 2.
3. F_q -> D_q: the mark lies in P. The newly planted outer divider
   raises it to height 3, at the peak of B_(j-1) in D_q.

Thus one R,S,P round takes exactly three updates and moves the marked
peak one B copy to the left. When it reaches B_1, it is the first
maximum-attaining up-step and is consumed on the very next update.

There are two initial climbing updates, q-1 such three-update rounds,
and one consuming update. Therefore

    T(D_q)=2+3(q-1)+1=3q.                               (4)

The nonconsuming counts are p=q+1, rho=q-1, sigma=q-1, consistent
with (2): 3+2(q-1)+(q-1)=3q.

This calculation tracks physical letter identities through (1); it does
not merely compare unmarked binary strings that happen to coincide.
The semilength is r=2q+1, so these primitive height-three words have
T=3(r-1)/2, linear in semilength despite constant height.

### Fully explicit q=2 check

For q=2 the unmarked orbit is

    1110011000 -> 1110001100 -> 1100111000 -> 1110011000.

Starting immediately after the first arrow, the marked letter's successive
positions within the currently rooted Dyck word are

    1 -> 6 -> 7 -> 8 -> 2 -> 3 -> consumed.

Its nonconsuming locations are P,P,R,S,P, followed by consumption.
Thus T=6 although h=3. The family (4), rather than this single finite
example alone, disproves the claimed uniform additive constant.

## 5. Exact unsupported statement and downstream scope

The failing assertion is not just an omitted justification. The implication

    S(D)=empty => the planted word and all its successors are single arches

is false. In (3), the first successor of D_q has q-1 suffix arches. Their
later transport puts first-maximum material ahead of the mark and creates
the R,S interruptions recorded in Section 4. The no-interruption claim
and the claimed T=h+O(1) bound are both false.

Q1's exact necklace update and Q3's height changes survive this audit.
With a consistent endpoint convention, the conservation law survives as
(2). The uninterrupted-climber statement in Q5 does not prevent the
interruptions here: the marked letter is explicitly swept and rested, and
transported old material becomes positioned before it.

Corollaries Q6.1 and Q6.2 and any status conclusion whose sole run-density
input is Q6 therefore lack that claimed proof. The present family has
only one specified word at each semilength 2q+1. It does not prove that
long-lived primitive roots have positive Catalan density, does not
disprove a positive-density short-run statement by another mechanism,
and gives no asymptotic estimate for the edge-disjoint packing nu_H.
Any independent proof of the canonical PBBS obstruction must be audited
separately; this note makes no assertion about proofs outside the stated
Q6 dependency.

A repair cannot uniformly bound all primitive/S-empty roots by a constant
multiple of their height. To recover a positive-density fast-exit theorem,
one needs a further structural restriction on the transported suffix
forests, together with a justified count of that restricted family.


<!-- END COMPLETE SOURCE 38 -->


---

<a id="document-39"></a>

## Document 39: pbbs_original_array_shift_cocycles.md

Source: `/Users/amir.nuriyev/.codex/worktrees/e333/problem/research_round1/pbbs_original_array_shift_cocycles.md`

[Portable document](sources/essential/e333/research_round1/pbbs_original_array_shift_cocycles.md) · [Exact original](originals/e333/research_round1/pbbs_original_array_shift_cocycles.md)

<!-- BEGIN COMPLETE SOURCE 39 -->

# PBBS shifted short returns in the original pruning coordinates

Date: 2026-09-07. Pure finite proof; no computation.

Read-only sources: worktree c69c, research_round1,
`pbbs_gaussian_clock_genealogy_structural_audit.md`,
`pbbs_zero_budget_pair_product_and_overlap_divergence.md`, and
`pbbs_stationary_lifetime_identities.md`; and the original
`/Users/amir.nuriyev/Documents/problem/PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`,
Sections 8-9 and 14. The source lifetime convention is retained:
the physical omitted-label return gap at root D is 2T(D)+1, and
tau=phi^2. This note concerns original coordinates and finite events,
not an asymptotic cluster or incidence-weight assertion.

## 1. Persistent indices and the correct translated arrays

Fix one root D of positive semilength r and height h. Put

    D_s=partial^s D,    r_s=|D_s|_up,    n_s=2r_s+1,
    p_s=n_(s+1),       0<=s<h.

At level s, the equality particles are labelled cyclically modulo p_s,
with original label zero on the edge immediately before the unmatched
zero of 0D_s. Let Z_(s,j) be the original incoming-gap coordinate from
the structural source, for nonempty-core levels 0<=s<h-1. If a bottom
array is desired, its single coordinate is deterministically
Z_(h-1,0)=r_(h-1). These coordinates are invariant under physical PBBS
updates when particle labels are persistent.

On the ORIGINAL fixed-site cyclic word w_s=0D_s, number sites
0,...,n_s-1, and let lambda_s(t) be its omitted site at every integer
time t, before that time's update. Negative times use the inverse of
the finite PBBS permutation on the SAME original labelled orbit; no
new root is sampled. Thus lambda_s(0)=0. All levels use the same
signed physical time t. Equality-particle renormalization
identifies the selected particle at level s with the omitted site of
the fixed-site process at level s+1. Write

    kappa_s(t)=lambda_(s+1)(t)  modulo p_s.             (1)

**Exact shift identity.** If Z^t denotes the canonical pruning arrays
of the new root phi^t D, whose particle labels are reset to start at
its current distinguished particle, then

    Z^t_(s,j)=Z_(s,kappa_s(t)+j),                      (2)

with indices modulo p_s. In particular, for the root tau^d D use
t=2d at EVERY pruning level, for every integer d, positive or negative.

Indeed the newly distinguished particle has old label kappa_s(t).
Persistent cyclic order makes its new successor j equal to old label
kappa_s(t)+j, and gap-coordinate invariance gives (2). The physical
formula omitted site = particle edge position +1 does not add a one
to this PARTICLE-indexed shift. Renormalization advances one step at
every level per physical update; there is no level-dependent time
rescaling. Identity (2) permits arbitrary previous spatial wraps.
The forward identities also hold at each negative-time transition of
the same bi-infinite orbit, so invertibility gives (2) at all integer
times.

For an explicit quotient cocycle at a nonempty reduced core
(0<=s<h-1), let delta(F) be the position of the
first maximum-reaching up-step of F. If F=P1R0S is its first-maximum,
first-return factorization, put omega(F)=|S|+1. The original skew-product
identities give, for all integers t,d,

    kappa_s(t)=sum_(v=0)^(t-1) delta(phi^v D_(s+1))
                                                   modulo p_s,
    kappa_s(2d)=-sum_(v=0)^(d-1) omega(tau^v D_(s+1))
                                                   modulo p_s. (3)

Every sum from 0 to t-1 is SIGNED: it is the ordinary sum over
0<=v<t when t>=0, and minus the sum over t<=v<0 when t<0.
Use the same convention with d in the second identity. Thus (3)
telescopes the original voltage increments in either time direction.
For example kappa_s(-1)=-delta(phi^(-1)D_(s+1)), while
kappa_s(-2)=+omega(tau^(-1)D_(s+1)), each modulo p_s.

Equivalently the even-time shift theta_s(d)=kappa_s(2d) obeys

    theta_s(0)=0,
    theta_s(d+1)=theta_s(d)-omega(tau^d D_(s+1)) mod p_s.

The increment identity holds for every integer d.

For the optional bottom slot, kappa_(h-1) is identically zero modulo
one, as is lambda_h; no value of delta at an empty core is invoked.

These are deterministic cocycles of the ORIGINAL reduced process, not
a new probability law at its visited roots. Generally theta_s(d) is
not -d. For example D_(s+1)=(10)^k has delta=1 at every step, hence
theta_s(d)=2d modulo 2k+1. Different pruning depths generally have
different shifts.

## 2. A bottom-up recursion entirely from the original data

The preceding cocycle can also be evaluated without using a reached-root
oracle. For s<h-1 let b_(s+1,j) be bit j of the original word 0D_(s+1),
and put

    epsilon_(s,j)=1{b_(s+1,j-1) != b_(s+1,j)},
    L_(s,j)=2Z_(s,j)+1+epsilon_(s,j),
    C_s(0)=0,
    C_s(j)=sum_(k=1)^j L_(s,k),       1<=j<p_s.        (4)

These are fixed original constants. The arrays and pruning profile
reconstruct the original reduced words by the source's inverse-pruning
bijection, so (4) uses no additional random information.

Define the signed visit count at every integer time by

    M_(s+1,j)(t)= #{0<=u<t: lambda_(s+1)(u)=j},   t>=0,
                 -#{t<=u<0: lambda_(s+1)(u)=j},   t<0. (5)

It satisfies M_(s+1,j)(0)=0 and
M_(s+1,j)(t+1)-M_(s+1,j)(t)=1{lambda_(s+1)(t)=j}
for EVERY integer t. The complete omitted-site sequences satisfy the
following recursion, also for every integer t:

    lambda_(h-1)(t)=t modulo n_(h-1),

    lambda_s(t)=C_s(lambda_(s+1)(t))
                 +M_(s+1,lambda_(s+1)(t))(t)
                 modulo n_s,             s=h-2,...,0. (6)

To prove this, the initial edge position of particle j at level s is
x_(s,j)(0)=-1+C_s(j). It moves forward once precisely when the reduced
omitted site equals j. At negative times the inverse update undoes that
same move. Telescoping the particle-position increments with (5) gives

    x_(s,j)(t)=-1+C_s(j)+M_(s+1,j)(t) modulo n_s.

The original renormalization identity is
lambda_s(t)=x_(s,lambda_(s+1)(t))(t)+1, proving (6).
For t>0 the count excludes update t; for t<0 the inverse sum includes
update t with a minus sign. Both conventions put the particle at its
position BEFORE update t. At the bottom, D_(h-1)=(10)^(r_(h-1)); its
rooted shape is fixed by phi and its voltage is one in both time
directions, proving lambda_(h-1)(t)=t modulo n_(h-1) for all integer t.
Formula (6) is valid through all spatial wraps and needs no resetting
of the original arrays at a negative-time phase.

Thus the original profile and arrays determine every shift and every
finite return predicate, by integer counts and residues alone. This is
a mathematical recursion, not a computational experiment.

## 3. Exact full-return and predecessor-count predicates

At any integer physical starting phase t_0 define

    g_D(t_0)=min{u>=1: lambda_0(t_0+u)=lambda_0(t_0)}.

The full-label property ensures a finite return, and the accepted
phase convention gives the exact identity

    2T(phi^(t_0)D)+1=g_D(t_0).                         (7)

Consequently, with G=2H+1,

    T(tau^dD)<=H
      iff some 1<=u<=G has lambda_0(2d+u)=lambda_0(2d). (8)

Together with (4)-(6), this is an original-array characterization for
every integer d and every finite H>=0, including negative birth shifts
and windows allowing spatial wraps.

There is a more economical exact predicate when G<n_0. Suppose h>=2,
put t_0=2d, a=lambda_1(t_0), and z=Z_(0,a). Then

    T(tau^dD)<=H
      iff #{1<=u<=G: lambda_1(t_0+u)=a-1 mod n_1}
                      >=2z+2.                        (9)

At t_0 the selected particle a and its predecessor both record zero,
so their incoming separation is 2z+1. If ell=lambda_0(t_0), their
lifted edge positions are ell-1 and ell-2z-2. The predecessor's k-th
selection strictly after t_0 therefore omits ell-2z-2+k. Its first
omission of ell is precisely its (2z+2)-nd such selection. No overtaking
forces this predecessor to be the first distinct particle to reach
ell again. A return by particle a after a full spatial lap takes at
least n_0 further selections, excluded by G<n_0. This proves (9).

The upper endpoint u=G is included: its omitted site is recorded before
that update. No condition G<n_1 is needed for (9); reduced dynamics can
wrap during the counting window. If h=1, T(D)=r and the short event is
empty when G<n_0. The natural one-slot convention z=r makes the
right side of (9) false as well, but the distinct-predecessor proof is
then replaced by this direct boundary case.

For any finite collection of shifts, conjoin the predicates (8), or
(9) in its stated range. All of them use the SAME original arrays
and sequences, giving an exact joint finite event without independence
or an original-to-reached reset. The collection may contain both
positive and negative shifts.

## 4. The correctly translated triangular obstruction

Assume h>L and p_s>G for 0<=s<L, where G=2H+1. Apply the accepted clock
genealogy to the root tau^dD for any integer d. Its chronological
queries at depth s, expressed in original indices, are exactly

    Z_(s,kappa_s(2d)), Z_(s,kappa_s(2d)-1), ... .      (10)

The minus one per chronological node comes from completion of that
node's unique child C clock. It is a genealogy index advance, distinct
from the two-step time cocycle in (3).

In detail, start v_0=u_0=1, let v_s count all depth-s clocks, u_s count
their T clocks, and let W_s be the sum of the first v_s queried entries
in (10). The exact source recursion remains

    u_(s+1)=u_s+2W_s,
    v_(s+1)=v_s+u_s+2W_s.

Hence v_s>=s+1 and sum_(s<L) W_s=(u_L-1)/2. The pruning profile is
invariant at every reached phase. Each depth-L T clock therefore has
physical length at least 2(h-L)+1. On the shifted short event its
whole interval has length at most G, so the source's disjoint-clock
bound yields

    sum_(s=0)^(L-1) sum_(j=0)^s
       Z_(s,kappa_s(2d)-j)
          <= [G/(2(h-L)+1)-1]/2.                     (11)

This is a NECESSARY consequence, not an equivalent full-return test.
The exact test is (8) or (9). The no-wrap hypothesis p_s>G applies
only to the new window beginning at 2d; there is no restriction on
how much the process wrapped before that time.

The shifts in (11) depend on original deeper pruning data. They cannot
be replaced by a common deterministic -d without an additional proof.
Different shifted triangles can query the same original slots; such
repeated queries read the same values. Conditioning on another short
event or choosing d from the observed trajectory does not supply a
fresh composition law.

These formulae isolate the exact finite dependence that a later cluster
argument would need to analyze. They make no claim about a growing-lag
limit, independent returns, stationary incidence weights, or packing.
An independent audit checked (2)-(3), the recurrence (6), and both the
threshold and phase endpoints in (9). The signed negative-time
extension, including the inverse-step evaluation points and the
empty-core convention, also passed an independent sign audit.


<!-- END COMPLETE SOURCE 39 -->


---

<a id="document-40"></a>

## Document 40: pbbs_original_incidence_window_kernel.md

Source: `/Users/amir.nuriyev/.codex/worktrees/e333/problem/research_round1/pbbs_original_incidence_window_kernel.md`

[Portable document](sources/essential/e333/research_round1/pbbs_original_incidence_window_kernel.md) · [Exact original](originals/e333/research_round1/pbbs_original_incidence_window_kernel.md)

<!-- BEGIN COMPLETE SOURCE 40 -->

# PBBS original-coordinate incidence window kernel

2026-09-07. Pure finite proof and a conditional original-slot limit;
no computation. This is the requested first deliverable: the exact
original-coordinate law of a sampled repair incidence and all shifted
short-return events that can cover its sampled edge. It does not prove
a new asymptotic clustering or packing theorem.

Inputs are the accepted original pruning-coordinate bijection and
physical lifetime dictionary in task05's notes. The detailed phase,
signed-time, and incidence proofs are in the companion notes
[original-array shift cocycles](sources/essential/e333/research_round1/pbbs_original_array_shift_cocycles.md)
and [short-repair incidence law](sources/essential/e333/research_round1/pbbs_short_repair_incidence_law.md).
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


<!-- END COMPLETE SOURCE 40 -->


---

<a id="document-41"></a>

## Document 41: pbbs_short_repair_incidence_law.md

Source: `/Users/amir.nuriyev/.codex/worktrees/e333/problem/research_round1/pbbs_short_repair_incidence_law.md`

[Portable document](sources/essential/e333/research_round1/pbbs_short_repair_incidence_law.md) · [Exact original](originals/e333/research_round1/pbbs_short_repair_incidence_law.md)

<!-- BEGIN COMPLETE SOURCE 41 -->

# Exact PBBS short-repair incidence law in original coordinates

2026-09-07. Pure proof; no computation. This is a finite sampling and
overlap dictionary, not a new renewal or overlap asymptotic.

Read-only sources: task05's `pbbs_stationary_lifetime_identities.md`,
`pbbs_gaussian_age_residual_and_cut_charges.md`, and
`pbbs_zero_budget_pair_product_and_overlap_divergence.md` in worktree
c69c/research_round1; the authoritative scratch note
`PBBS_ZERO_BUDGET_RENEWAL_CLUSTER_PACKING_20260907.md`.
The original-array fiber representation in Section 3 is an explicit
input from the current pruning-coordinate audit.

## 1. Birth phase and inclusive edge endpoints

Fix r>=1, n=2r+1, and the full physical complement-projected PBBS factor,
with W=n Cat_r edges. Write f for the rank-r PBBS permutation, g=f^2,
phi for the rooted quotient, and tau=phi^2. The lifetime T(D) includes
the consuming update. Thus a gap-start root D with omitted-label return
gap 2T(D)+1 gives a complement positive run with T(D)+1 owners and a
repair interval with T(D)+2 edges.

To fix the complement phase literally, let B be the physical rank-r
state at the omitted-label gap start, with root D. Put

    B_d=f^(2d)B,
    e_d : (f^(2d-1)B)^c -> (f^(2d+1)B)^c,   d in Z.       (1)

The birth on e_d has gap-start root tau^d D. The repair interval born
on e_0 contains precisely

    e_0,e_1,...,e_(T(D)+1).                               (2)

Offset j=0 is the insertion edge; offset j=T+1 is the deletion edge;
offsets 1,...,T are internal. At this cut the positive run has j owners
on the left and T+1-j on the right, including a zero side at a boundary.

Equivalently, if one starts with a complement edge A_i^c -> A_(i+2)^c,
its birth root is root(A_(i+1))=phi(root(A_i)). On all Dyck roots the
common phi shift preserves uniform measure and commutes with tau. For
a merely tau-invariant owner-root family Omega, the birth-root family
is phi(Omega); it cannot silently be replaced by Omega.

Let P be the actual physical period of (1). The prebirth owner lacks
the inserted coordinate and returns after P steps, so the coordinate
is first deleted by e_(P-1). Hence T(D)+2<=P for every birth on this
cycle. The accepted full-label property also gives P>=2r+1. A root's
tau-period may be shorter than P: repeated roots at different physical
phases are distinct births and must remain distinct in overlap counts.

Our cutoff below is T<=H. A cutoff H_res on complement residence instead
means T<=H_res-1.

## 2. Uniform retained repair-edge incidence

Let A(D) be any zero-one birth predicate and set

    mu_A=E_D[(T(D)+2)A(D)],                              (3)

where D is uniform among the Cat_r roots. There are exactly W mu_A
retained repair-edge incidences. If mu_A=0 the family is empty and its
incidence probability law is undefined. Otherwise its exact sampler is:

1. Choose D with probability (T(D)+2)A(D)/(Cat_r mu_A).
2. Choose uniformly one of its n physical spatial phases u, thereby
   fixing B and the entire deterministic trajectory (1).
3. Choose j uniformly in {0,...,T(D)+1}.

Thus every admissible triple (D,u,j) has probability 1/(W mu_A), and

    E_inc,A Psi = (1/mu_A) E_(D,u)
                       [ A(D) sum_(j=0)^(T(D)+1) Psi(D,u,j) ]. (4)

For A_H=1{T<=H} and p_t=Pr_D(T=t), in particular,

    Pr_inc,H(T=t,j=v)=p_t/mu_H,
          1<=t<=H, 0<=v<=t+1;
    Pr_inc,H(T=t)=(t+2)p_t/mu_H.                         (5)

Conditioned on the explicit offset j, the root is uniform among those
with max(1,j-1)<=T<=H. Uniform retained births and uniform retained
repair incidences are different measures.

## 3. Disintegration on the original pruning-coordinate fibers

Assume the supplied exact coordinate bijection: each root is represented
once by a feasible pruning profile R and an original array x in its
Cartesian product C_R of weak-composition fibers. Before conditioning,
given R the original array is uniform on C_R. It is this original array,
not a newly sampled array at a reached root, that determines every
T(tau^d D).

Marginalizing out the physical phase in (4) gives the exact atom law

    Pr_inc,A(R,x,j)
      = A(D(R,x)) 1{0<=j<=T(D(R,x))+1}/(Cat_r mu_A).      (6)

For a positive-mass conditioning event (R,j), x is therefore uniform
on

    {x in C_R: A(D(R,x))=1, T(D(R,x))>=j-1}.             (7)

For a positive-mass conditioning event R alone, its law is proportional
to (T(D(R,x))+2)A(D(R,x)) on C_R. Thus recording j cancels the length
factor, but it leaves a survival condition. Neither conditioning
preserves the original product independence unless separately proved.
The physical phase, when needed, is still uniform given (R,x,j).

## 4. Exact shifted overlap, with negative shifts and wrap

At a sampled e_j, let K_A(B,j) count all retained repair intervals on
its physical cycle that contain this edge. For each physical birth
residue d modulo P put T_d=T(tau^d D). With [v]_P in {0,...,P-1},

    K_A(B,j)=sum_(d mod P) A(tau^d D)
                         1{[j-d]_P<=T_d+1}.             (8)

This is valid without a cutoff and counts each physical birth once.
It is a deterministic function of the original state; there are no
independently renewed roots in (8).

If A implies T<=H and H+2<=P, the H+2 possible earlier birth residues
have the unique lifted representatives j-H-1,...,j. Therefore

    K_A(D,j)=sum_(d=j-H-1)^j A(tau^d D)
                                    1{T_d>=j-d-1}.      (9)

For H=o(r), the accepted lower bound P>=2r+1 makes (9) applicable to
every physical component for all sufficiently large r. Otherwise use
(8), or replace H in the age-window bound by min(H,P-2).

Negative d are genuinely earlier births. For d=-a their lifetime must
be at least j+a-1. Positive d can contribute only when d<=j and still
must satisfy T_d>=j-d-1. At the left endpoint d=j-H-1, an overlapping
retained interval has T_d=H and e_j is its deletion edge. At d=j, e_j
is its insertion edge. The sampled base birth d=0 always contributes.

In particular, a shifted event T_d<=H alone does not guarantee overlap:
the later retained interval may already have ended. The zero-budget
fixed-height argument avoids this issue because all its lengths agree.

Every finite joint law follows by inserting products of these original-
trajectory indicators in (4). For example the probability that fixed
physical birth residues d_1,...,d_s all supply retained intervals at
the sampled edge is exactly

    (1/mu_A) E_(D,u) [ A(D) sum_(j=0)^(T(D)+1)
        product_l A(tau^(d_l)D)
                    1{[j-d_l]_P<=T(tau^(d_l)D)+1} ].     (10)

The physical-period convention in (10) is essential when a root orbit
has a shorter period. No factorization of (10) is asserted.

For an integer budget threshold bcut>=0, take

    A_(H,bcut)(D)=1{T(D)<=H, T(D)-h(D)>bcut},             (11)

where height h is tau-invariant. Formula (9) specializes to

    K_(H,bcut)(D,j)=sum_(d=j-H-1)^j
      1{max(h(D)+bcut+1,j-d-1,1)<=T(tau^d D)<=H}.        (12)

Its sampling measure is (4) or (6) with predicate (11); the offset j
and budget threshold bcut are separate parameters.

## 5. The exact occupied-edge target and low-budget deletion

Write K_A(e) for the same congestion at physical edge e. Counting
incidences in the two orders gives

    E_edge K_A=mu_A,
    Pr_inc,A(sampled edge=e)=K_A(e)/(W mu_A),
    #{e:K_A(e)>0}/W=mu_A E_inc,A[1/K_A].                 (13)

On the incidence law, 1<=K_A<=r+2, the upper bound following from the
full repair family, whose congestion is exactly r+2 at every edge.

The target for negligible occupied support is the PRODUCT in (13).
If mu_A=O(1), divergence of K_A in incidence probability would suffice.
For all Gaussian-short runs, the current short-birth bound alone gives
only mu_H=o(H), which may diverge. Then one needs
E_inc,H[1/K_H]=o(1/mu_H), or an equivalent product estimate. Full-family
sampling illustrates the issue: mu=r+2 and K=r+2 diverge while every
edge is occupied. No new overlap-divergence result is proved here.

Put B=T-h. The separate all-lifetime low-budget inputs have DIFFERENT
forms for zero and positive budgets:

    #{edges in some B=0 repair interval}/W=o(1),
    Z_+=E[(T+2)1{0<B<=bcut_r}]=o(1).                   (14)

Zero-budget RAW incidence E[(T+2)1{B=0}] is Theta(1), so it must not be
included in the second estimate. The accepted authoritative note
`PBBS_NEAR_GAUSSIAN_BUDGET_SHARED_REPAIR_20260907.md` supplies (14) for
its explicit bcut_r=J_r of order sqrt(r/log r), without a lifetime
cutoff. Only the first line uses sharing among repair intervals.

Let mu_H be the all-short normalizer, mu_+ the normalizer for
A_+=1{T<=H,B>0}, and mu_res the normalizer for (11). Set

    delta_+=mu_+-mu_res <= Z_+,
    delta_H=mu_H-mu_res
           =E[(T+2)1{T<=H,B=0}]+delta_+.               (15)

Whenever the corresponding laws are defined, conditioning gives the
exact identities

    TV(P_inc,+,P_inc,res)=delta_+/mu_+,
    TV(P_inc,H,P_inc,res)=delta_H/mu_H.                 (16)

Thus positive-short and residual incidence laws are asymptotically
close when mu_+ is bounded below. All-short and residual incidence laws
are close only under the additional relative-mass condition
delta_H=o(mu_H); a lower bound on mu_H alone is insufficient because
the removed zero-budget raw mass need not vanish.

For OCCUPIED support no such relative-mass condition is needed. Every
edge lost on passing from all-short to residual is in a zero-budget
repair interval or in one with 0<B<=bcut_r. By (14),

    0 <= #{e:K_H(e)>0}/W-#{e:K_res(e)>0}/W
      <= #{edges in some B=0 interval}/W+Z_+=o(1).       (17)

If mu_H tends to zero, the occupied all-short fraction already tends
to zero by (13), since it is at most mu_H. Closeness of any sampling
laws alone does not identify their congestion observables. The remaining
overlap target is still mu_res E_inc,res[1/K_res]=o(1), with the empty
residual family interpreted as having zero occupied support.


<!-- END COMPLETE SOURCE 41 -->
