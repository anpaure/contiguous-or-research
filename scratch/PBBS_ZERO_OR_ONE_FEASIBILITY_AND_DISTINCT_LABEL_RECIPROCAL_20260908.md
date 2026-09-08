# Physical feasibility reduces to sums0/1 and a distinct-label reciprocal

2026-09-08. Pure proof, no mathematical execution. Direct-route found the
physical birth-shift reduction. Root independently checked its short proof
and proposed the distinct-label reciprocal strengthening; direct-route
checked that strengthening with the profile-domain guard below. Full-file
audits now include root's complete independent read and verification of
the physical shift, phase-spacing bound, finite probabilities, covariance
count, and tower estimate: PASS. Appendix_a independently checked the
complete file, including all probability constants and scope guards: PASS.

This is a new reduction of the actual exposed-environment gate. It does
not show that the resulting number of physical eligible labels diverges.

## 1. Exact inherited domain and two fixed clock words

Fix0<c<=C<infinity, H_c=floor(c sqrt(r)), H=floor(C sqrt(r)), and
G=2H+1. Use the safe depth-two base incidence fibre from
`PBBS_TWO_ROW_VIRTUAL_ZERO_CLOCK_REDUCTION_20260908.md` and
`PBBS_EXPOSED_PHASE_FEASIBILITY_RECIPROCAL_REDUCTION_20260908.md`.
Its exposed environment is

    E_2=(full original profile, all original rows s>=2, offset j).

Row one conditionally composes ell=ell_1 into P=p_1-2 free labelled
parts. Its original slots0,-1 are forced zero. The base phase d=0 is
successful with sum0 for every completion. The strict no-wrap margin
holds for horizonG, and h>=4 on this safe fibre. All clocks below are
on the ONE exposed, signed, original D_2 trajectory.

At a selected phase t, let T return to the next selection of the same
label and C to the next selection of its predecessor. Their endpoint
maps commute, C has positive even duration, and T positive odd duration.
These are the accepted adjacent-selection identities, not an independence
assumption or a reset to a newly sampled state.

For an even birth t=2d, whose original D_2 label is i=lambda_2(t), define

    Phi_w(t)=endpoint of C^2 T^(2w+1) from t.

The exact two-row theorem says that d is feasible in J precisely when
some composition-admissible nonnegative w at the pair(i,i-1) satisfies

    Phi_w(t)-t<=G,        t<=2j,        Phi_w(t)>=2j-1.          (1)

The final inequality includes the right overlap boundary. The height
floor follows automatically from an actual short reverse grouping.
The candidate window is d in[j-H-1,j]. It also follows directly from
(1), since t>=Phi_w(t)-G>=2j-1-G.

Define J_01 to count the same physical phases, restricting the allowed
sum to{0,1}. Define L to be the number of DISTINCT original D_2 labels
i occurring in J_01. These labels qualify through actual even birth
times and the physical clock tests(1); they are not static/cone labels.

For sum1 to be admissible, the pair must contain a free slot and ell>=1.
Sum0 is always admissible on this safe domain, which has unused free
slots to absorb any remaining mass. Both-forced pairs allow only sum0.

## 2. A later legal birth reduces the required sum

### Theorem1

The set of original D_2 labels occurring in J is EXACTLY the set counted
by L. In particular every feasible label has a physical feasible phase
whose sum is0 or1.

Proof. Start from a feasible even phase t with allowed sum w. If w=0,
there is nothing to prove. If w>0 and t'=T^2(t)<=2j, replace the birth
by t' and the sum by w-1. This is a later EVEN selection of the SAME
original label. By commutation,

    Phi_(w-1)(T^2(t))=Phi_w(t).                     (2)

The endpoint is unchanged and the duration decreases. The sampled edge
still lies in the trace, and the new birth remains in the legal window.
Its queried original row-one pair is exactly the same pair(i,i-1).

Repeat until the sum becomes0 or the next even selection lies after2j.
This terminates after at most the original w shifts. In the latter case,
if the remaining w>1, replace it by1 without moving the birth. The new
endpoint is no later than the old endpoint, and

    Phi_1(t)=C^2 T^3(t)>T^3(t)>T^2(t)>2j.          (3)

Thus it still covers the sampled edge and remains within the cutoff.
Monotonicity in w here is within successive returns of the same label,
as given by commutation; no global monotonicity across unrelated labels
is asserted.

Every new sum is smaller. Reduce the previous assignment on its free
slots to that smaller sum and place the released mass in an unused free
slot. Forced zeros remain zero, and the total composition is unchanged.
If both pair slots are forced, the original w was0. Consequently the
new sum remains feasible in the SAME actual incidence fibre.

All new durations are at most the original short duration. The accepted
safe reverse grouping therefore turns these short core clock words into
the required physical virtual lifetimes. No identity for a long parent
clock is invoked. The reverse inclusion of label sets is immediate since
J_01 is a restriction of J. This proves the theorem.

Only the two fixed words C^2T and C^2T^3 are now needed to test whether a
label has any feasible phase. The actual sampled row-one values have
not been changed in a probability argument: the preceding proof concerns
the existential definition of feasibility.

## 3. Quantitative phase-to-label comparison

Every D_2 same-label return has duration at least g=2h-3. Even selections
are every second selection, so their spacing is at least2g. The tested
physical time window has length2(H+1). Thus each label occurs at most

    M_h=1+floor((H+1)/(2h-3))

times in that window. Theorem1 gives the deterministic bounds

    1<=L<=J_01<=J<=M_h L.                          (4)

The base label0 contributes to L. On h>=epsilon sqrt(r), M_h is bounded
by a constant depending only on C,epsilon. Hence the existing small-height
incidence estimate proves that J, J_01, and L diverge in actual incidence
probability simultaneously: take r to infinity at fixed epsilon, then
epsilon to zero. Safe exceptions have probability o(1).

This particular equivalence argument uses height truncation. The UPPER
reciprocal bound proved next does not. The subsequent zero-only theorem
and `PBBS_HEIGHT_FREE_INTERVAL_STABBING_AND_RECIPROCAL_EQUIVALENCE_20260908.md`
remove the truncation entirely: J=J_0 with probability 1-o(1), and
L_0<=J_0<=2L_0 deterministically. That note also proves J_01<=3L before
invoking zero-only feasibility and a two-sided reciprocal comparison
afterward.

## 4. Exact conditional probability at a selected phase

Work on the additional exposed profile event

    P>=8,             1/16<=ell/P<=1/4.            (5)

The accepted original-depth concentration in Section3 of
`PBBS_GROWING_ADAPTIVE_GAP_QUERY_FRESHNESS_20260908.md` gives P of order r
and ell/P->1/8 under actual base incidence. Thus(5) has probability1-o(1)
for every fixed c,C. It imposes NO positive height truncation.

The original GOOD event alone controls r_1,r_2, whereas ell_1 also uses
r_3. Therefore(5), rather than bare GOOD, is the precise domain for a
uniform positive probability of a sum1 assignment.

For each label counted by L, choose one successful pair(d_i,w_i) with
w_i in{0,1}, using only E_2. For label0 choose d_0=0,w_0=0. For every
other label, any fixed lexicographic choice works. Let

    Y_i=1{Z_(1,i)+Z_(1,i-1)=w_i},   X=sum_i Y_i.

These are one selected PHYSICAL phase per distinct label. Different
labels give different chosen phases. Consequently

    1<=X<=N_virt,

because the base event Y_0 is forced to1 and every successful selected
phase is counted by the actual virtual counter.

If t distinct free coordinates have assigned values of total A, their
exact uniform-composition probability is

    (P-1)_t (ell)_A /(ell+P-1)_(A+t),               (6)

with falling factorials. Here each selected event involves at most two
free coordinates and sum at most1. On(5), a specified assignment1,0 to
two free coordinates has probability at least

    (P/2)^2*(P/16)/(5P/4)^3=1/125.

A single free coordinate equal to1 has probability at least1/50, while
zero assignments have larger fixed lower bounds; an all-forced allowed
event is certain. Hence uniformly

    E[X|E_2]>=p L,             p=1/125.            (7)

For two disjoint free supports, their joint event involves at most four
coordinates and total at most2. Factoring the bounded number of terms
in(6), uniformly under(5), compares it to the corresponding independent
geometric probability with error O(1/P). Summing the at most four
assignments for the two sum events gives an ABSOLUTE constant B with

    |Cov(Y_i,Y_k|E_2)|<=B/P                        (8)

when their free supports are disjoint. This is an exact finite-fibre
estimate; the actual marks have not been declared independent.

For distinct labels, the supports{i,i-1} overlap only for the two cyclic
neighbors i-1,i+1. Removing forced slots can only reduce overlap. Thus
there are at most2L ordered overlapping pairs, and L<=p_1=P+2. It follows
from(8) and |Cov|<=1 that an absolute D satisfies

    Var(X|E_2)<=3L+B L^2/P<=D L.                  (9)

All constants in(7)-(9) are independent of h,c,C,r on the specified
profile domain. They concern the actual conditional composition.

## 5. A height-free upper reciprocal estimate

Split according to X>=pL/2. Equations(7)-(9), Chebyshev, and X>=1 give

    E[1/N_virt|E_2] <= E[1/X|E_2]
       <= [2/p+4D/p^2]/L = A/L.                   (10)

Let k be the actual distinct eligible original level-zero partner-label
count and K_C the partner congestion. The accepted exact relations are

    k+1<=N_virt<=k+2,
    E[1/K_C|profile,rows>=1,j]<=2/(k+1).

Therefore the tower property and N_virt<=2(k+1) imply

    E_inc,c[1/K_C|E_2]<=4A/L.                      (11)

There is NO h>=epsilon sqrt(r) condition in(10)-(11). The only additions
to the accepted safe incidence domain are(5). Restoring its o(1) profile
and safe exceptions adds o(1) to an unconditional reciprocal expectation,
since reciprocals are bounded by1. The law of E_2 remains its actual
base-c incidence law throughout.

## 6. Precise remaining dependence

The unresolved quantity can now be taken to be the number L of distinct
original D_2 labels with an eligible actual even phase for C^2T or C^2T^3,
respecting the sampled-edge overlap and the fixed partner cutoff. The
label set is chosen before exposing row-one values. Only adjacent pairs
can share a free mark, and their exact finite-composition dependence is
already controlled by(8)-(11).

What remains is the joint occurrence of these two FIXED clock tests on
the exposed signed D_2 trajectory, under its actual short-base-clock and
offset law. No fresh law at a moving root, static cone count, or canonical
predecessor-boundary count has been substituted for those physical tests.

L-divergence would give the reciprocal decay needed by the verified
coefficient-one compiler chain. Theorem1 and(4) give an equivalence to
the previous J-divergence gate using the accepted small-height limit.
The subsequent zero-only and interval-multiplicity notes cited in
Section3 strengthen this to a height-free equivalence and a two-sided
reciprocal comparison. This note proves the physical reduction and the
stronger reciprocal estimate, not divergence, a packing improvement, or
coefficient one.
