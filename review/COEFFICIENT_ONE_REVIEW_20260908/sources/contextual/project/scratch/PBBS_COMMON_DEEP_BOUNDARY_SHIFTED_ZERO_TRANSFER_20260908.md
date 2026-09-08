# Actual shifted-zero transfer at common deep C boundaries

2026-09-08. Pure proof, no mathematical execution. Direct-route deduction.
Appendix_a independent full-file audit: PASS. Root read the entire proof
and independently checked the actual row conditioning, harmonic product,
count bounds, and counterexample against the original clock dictionary:
PASS. The later note
`PBBS_COMMON_DEEP_BOUNDARY_ELIGIBILITY_BY_GROWING_DEPTH_FLUX_20260908.md`
proves useful deep eligibility for every fixed initial set of boundaries.
Surviving-count abundance is not established by either note.

This note gives an exact conditional lower bound for a deep eligible
physical phase to survive the actual intermediate rows. At the k-th
common deep C boundary its limiting lower bound has order 1/(k+1), rather
than the generic order 1/S at depth S. This note itself does not establish
that enough of those boundary intervals meet the cutoff; the subsequent
eligibility note cited above addresses that issue. Neither proves here
that their surviving count diverges in probability.

## 1. The exact incidence fibre and the remaining deep clock test

Fix 0<c<=C<infinity, H_c=floor(c sqrt(r)), H_C=floor(C sqrt(r)), and
G_C=2H_C+1. Fix S>=2 before taking r to infinity. Work under actual
base-c incidence, restricted to its depth-S zero-triangle safe event.
Use the exact fibre of
`/Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_finite_layer_zero_triangle_incidence_fibre.md`.

We impose the stronger partner-cutoff profile margins through S and,
when needed below, P_s>s+1. They are profile-measurable and have
probability 1-o(1) for fixed S,c,C. Expose

    E_S=(full original profile, all original rows u>=S, offset j).

Conditional on this feasible E_S and the safe base event, rows s<S
are independent uniform compositions with their base slots
0,-1,...,-s forced zero. Put

    P_s=p_s-s-1,                 ell_s=sum Z_(s,i).

There is no additional hidden lifetime restriction on a free upper slot.
In particular E_S retains its actual short-base-clock and offset law.

All clocks next refer to the one original signed D_S trajectory. Let

    t_k=C_S^k(0),       0<=k<=S,
    b_k=C_S^S T_S(t_k)=C_S^(S+k) T_S(0).                  (1)

The base endpoint is b_0, and t_0,...,t_S are distinct even times inside
its chronological C_S^S T_S word. Define the E_S-measurable eligible set

    A_S(E_S)={0<=k<=S: t_k<=2j and b_k-t_k<=G_C}.          (2)

Commutation and positivity give b_k>=b_0>=2j-1. Thus (2) is precisely
the deep cutoff and inclusive overlap test for these boundary phases.
The base index 0 always belongs to A_S. The values b_k for k>0 need
not lie inside the base horizon; their cutoff is explicitly tested.

## 2. Revealing actual shifted slots gives a probability lower bound

For any phase t_k define Y_k to mean that its ACTUAL shifted triangle
in the intermediate rows vanishes:

    Z_(s,lambda_(s+1)(t_k)-u)=0
             for 2<=s<S and 0<=u<=s.                     (3)

The canonical shift is the exact original-array cocycle, with the SAME
signed physical time at every depth. No original-index cone is
substituted for (3).

### Proposition 1

On the stated finite fibre, put m_s(k)=min(k,s+1). Then

    P(Y_k | E_S,safe base) >= p_(r,k,S)
       :=product_(s=2)^(S-1)
               (P_s-1)_(m_s(k))
                 /(ell_s+P_s-1)_(m_s(k)),                 (4)

where factorials fall and an empty product is one.

Proof. Reveal the entire rows S-1,S-2,...,2 in that order. Before row s
is revealed, lambda_(s+1)(t_k) is determined by the exposed deeper data.
The row remains its independent base-zero uniform composition. If (3)
uses m new free slots in that row, their exact joint zero probability is

    a_s(m)=(P_s-1)_m/(ell_s+P_s-1)_m.                    (5)

It is decreasing in m. Always m<=s+1, regardless of any lower-index
misalignment or previously observed zeros.

For s>=k-1, the stronger bound m<=k holds. Indeed, in every intermediate
row u>=s+1 the first k incoming coordinates are already forced zero,
since u+1>=k. The first k deep C clocks consequently lift through those
rows as k consecutive C clocks. Their selected original D_(s+1) label
at t_k is exactly -k. The shifted interval [-k-s,-k] of row-s indices
adds at most k slots to its already forced interval [-s,0]. Cyclic
coincidences can only reduce that number. For s<k-1, the bound s+1
already equals min(k,s+1). Thus in every row m<=m_s(k).

Conditional on all higher revealed rows, whether or not their tests
passed, (5) is at least a_s(m_s(k)). Iterate these lower bounds downward.
This proves (4). Full-row revelation is permitted in this proof; no
claim of a fresh distribution at a reached root or a bounded-query
trajectory oracle has been made.

If k belongs to (2) and Y_k holds, reverse grouping inside the tested
short horizon gives the actual D_2 word C_2^2 T_2 from time t_k with
endpoint b_k. Inductively, the zero incoming slots expand
C_s^s T_s to C_(s+1)^(s+1) T_(s+1), preserving its actual endpoint.
Thus d=t_k/2 is a LEGAL zero-sum feasible phase of the D_2 problem.
Row-one sum zero can be completed in the inherited composition fibre.

## 3. Boundary-specific harmonic weights and a statistical count bound

At each fixed k,S, accepted fixed-depth actual-incidence profile
concentration makes (4) converge in probability to

    p_(k,S)=product_(s=2)^(S-1)
          [1-1/(s+2)^2]^min(k,s+1).                      (6)

The telescoping original-cone product is used here only to evaluate
this numerical lower bound, not to identify the events. For 1<=k<=S,

    p_(1,S)=(3/4)(S+2)/(S+1),
    p_(k,S)=27/[16(k+1)] *[(S+2)/(S+1)]^k,   k>=2.       (7)

For k=0 the value is one. To verify (7), include rows s=0,1 in (6).
Their full product is [(S+2)/(S+1)]^k/(k+1). Divide by 2/3 for k=1,
and by (3/4)(8/9)^2=16/27 for k>=2. In particular, for k>=2,

    p_(k,S)>=27/[16(k+1)].                              (8)

These are fixed-depth limiting statements. No uniform growing-depth
profile approximation is inferred from them; the finite inequality
(4) is the applicable assertion without that approximation.

Let

    X_S=sum_(k in A_S) 1_(Y_k),
    F_S^*=sum_(k in A_S) p_(r,k,S),       n_S=|A_S|.

The t_k are distinct physical births. Each success is counted by J_0,
and the height-free interval bound gives J_0<=2L_0. Hence

    E[L_0 | E_S,safe base] >= (1/2)F_S^*.                (9)

This is a lower bound under the exact actual incidence fibre. It does
not assume independence of the Y_k. A bounded-tail consequence, if
desired, follows from 0<=X_S<=n_S and E[X_S|E_S]>=F_S^*:

    P(L_0>=F_S^*/4 | E_S,safe base)
                                    >=F_S^*/(2n_S).     (10)

Indeed E X_S<=F_S^*/2+n_S P(X_S>=F_S^*/2), and X_S<=2L_0.
The base contributes X_S>=1, but is not needed for this inequality.

In particular, many eligible initial common boundaries would give a
harmonic lower bound on the conditional mean. Neither the deep test
(2) nor the dependence among the Y_k has been removed. The separate
stationary-core abundance theorem concerns ALL deep physical phases,
not necessarily the common boundaries in (2).

## 4. Why the raw-cone deterministic transfer still fails for L_0

There is a direct one-level-deeper version of the accepted fixed-gap
misalignment example that concerns the NEW existential zero-sum test.
Take S>=5 and the common boundary t_5. Base zeros give

    lambda_4(t_k)=-k,  k<=5,
    lambda_3(t_k)=-k,  k<=4.

Set the free coordinate Z_(3,-4)=1. At t_4 the incoming separation of
the selected D_4 particle from its predecessor is three. Its first later
predecessor selection is t_5, and the exact particle-position formula
therefore gives

    lambda_3(t_5)=-7.                                  (11)

The raw original-index cone Q_S(5) asks row-two zeros at -5,-6,-7 and
leaves -8 free; it asks row-three zeros at -5,-6,-7,-8 and leaves -4
free. It is consequently compatible with both Z_(3,-4)=1 and
Z_(2,-8)=M, for any fixed positive integer M.

If C_2^2 T_2 from t_5 were short, its valid one-level expansion would
query row two at original labels -7,-8,-9. Its depth-three T count
would therefore be at least 2M+1. Reached height is h-3, so its duration
would be at least

    (2M+1)[2(h-3)+1].                                  (12)

On h>=epsilon sqrt(r), choose fixed M with (2M+1)epsilon>C. Formula
(12) contradicts the C cutoff for all sufficiently large r. The larger
sum words C_2^2 T_2^(2w+1) have still later endpoints and also fail.
Thus this particular common-boundary phase is not feasible at all,
regardless of any actual or hypothetical row-one values.

The imposed coordinates are free and disjoint from the base and raw
cone zeros. At fixed S,M their joint event has positive limiting
probability in the exact incidence fibre, by the accepted stable
finite-coordinate law; the actual-incidence small-height bound permits
choosing epsilon with a positive-mass height sector. This establishes a
positive-incidence obstruction to that deterministic map. It does not
say the same cone has no other useful physical birth or that L_0 is tight.

Here the stable law is used CONDITIONALLY relative to the exposed
profile/deeper environment. Choose a height sector of positive mass
first, then its fixed M; conditional stability preserves positive mass
for the finite-coordinate event in that sector. No comparison of an
unconditional small-height error with an M-dependent rare-event
probability is needed.

Proposition 1 survives precisely because it imposes the ACTUAL shifted
slots (3). Its low-row slot budget tolerates (11); it never declares a
raw cone successful at its natural boundary.
