# Height-free physical interval multiplicity and reciprocal equivalence

2026-09-08. Pure proof, no mathematical execution. Root proposed the
interval bound and checked the direct congestion comparison. Direct-route
independently checked the signed clocks, strict endpoint inequality,
inclusive-boundary count, and conditional-law scope. Root's independent
mathematical audit of these statements: PASS. Root subsequently read
the completed file end to end and checked the strict endpoint handling,
unrestricted-envelope scope, conditioning, and exceptional-set restoration:
full-file audit PASS.

On the regular safe environments where exposed feasibility is zero-only,
the physical phase count J and the distinct-label count L_0 satisfy

    L_0 <= J = J_0 <= 2 L_0.

Moreover the actual top-zero partner reciprocal is comparable to 1/L_0
with absolute constants. Neither conclusion requires a positive Gaussian
height truncation. Neither proves that L_0 diverges.

## 1. Inherited domain and the unrestricted interval envelope

Fix 0<c<=C<infinity and H=floor(C sqrt(r)). Retain the ACTUAL base-c
incidence law and its safe depth-two base fibre from
`PBBS_TWO_ROW_VIRTUAL_ZERO_CLOCK_REDUCTION_20260908.md`. Write

    E_2=(full original profile, all original rows s>=2, offset j).

The full signed D_2 selection trajectory is exposed. Its same-label
return map T and predecessor-selection map C satisfy the accepted global
strict adjacent-selection alternation identities. In particular,

    C(t)<T(t),                 CT=TC.                         (1)

Every C duration is positive and even, and every T duration is positive
and odd. These are identities of the original signed trajectory. They
hold independently of whether a clock word fits the short cutoff. The
inherited safe domain has distinct predecessor labels and nonempty cores.
No long-parent reverse-grouping assertion is made here.

For an even birth t=2d and integer w>=0 set

    Phi_w(t)=C^2 T^(2w+1)(t),
    R_w(d)=(Phi_w(2d)+1)/2,
    I_w(d)=[d,R_w(d)] intersect Z.                           (2)

R_w is an integer. I_w is the unrestricted inclusive edge interval of
this clock word. When w is composition-admissible and its duration is at
most 2H+1, the accepted short reverse grouping identifies it with the
virtual top-zero partner interval. Unrestricted intervals in (2) will
only be used as containing sets, never as additional legal partners.

## 2. Exact deterministic interval multiplicity

### Proposition 1

For any fixed original D_2 label i, any integer w>=0, and any integer
edge j, at most w+2 of the intervals I_w(d) starting at even selections
of i contain j. This includes edges exactly equal to a birth or a right
overlap endpoint.

Proof. Apply (1) at the selected phases C(t) and T(t):

    C^2(t)<T(C(t))=C(T(t))<T^2(t).

Thus, applying this inequality at T^(2w+1)(t),

    Phi_w(t)<T^(2w+3)(t).                                  (3)

For even t, both sides of (3) are odd integer times. The next same-label
selection T^(2w+4)(t) is even and strictly later. Consequently,

    (Phi_w(t)+1)/2 < T^(2w+4)(t)/2.                         (4)

In particular the inclusive right endpoint in (2) is STRICTLY before
the (w+2)-nd later EVEN selection of the same label.

Enumerate all even selections of i as ...<d_k<d_(k+1)<... in edge time.
They exist in both signed directions, and T^2(2d_k)=2d_(k+1). Formula
(4) says

    d_k <= j <= R_w(d_k) < d_(k+w+2)                       (5)

whenever its interval contains j. If q is the last index with d_q<=j,
then (5) forces q-w-1<=k<=q. There are at most w+2 such indices. The
strict last inequality makes this argument valid also when j=d_q or
j=R_w(d_k). This proves the proposition.

Let J_w count feasible physical phases with the fixed sum w, and let L_w
count their distinct D_2 labels. Restricting (5) to feasible intervals
gives J_w<=(w+2)L_w. In particular,

    J_0<=2L_0.                                             (6)

For the union of sums 0 and 1, commutation gives
Phi_1(t)=T^2(Phi_0(t))>Phi_0(t). Hence I_0(d) is contained in I_1(d).
Every phase counted by J_01 is therefore in its label's unrestricted
sum-one envelope. Proposition 1 gives

    J_01<=3L,                                              (7)

where L counts distinct labels with some feasible sum-zero or sum-one
phase. An envelope need not itself meet the cutoff or admit sum one in
the composition; its use in (7) is purely a containment argument. A
phase feasible for both sums is counted once.

## 3. Zero-only feasibility removes the height truncation

The fully audited note
`PBBS_BAD_PARTNER_UNION_TRANSFER_AND_ZERO_ONLY_FEASIBILITY_20260908.md`
proves that, with probability 1-o(1) under the actual base-c incidence
law, no E_2-feasible physical phase admits a positive sum. On that
E_2-measurable event,

    J=J_0,                 L=L_0.

The base phase contributes a forced successful sum zero, so L_0>=1.
Together with (6), this yields

    1<=L_0<=J=J_0<=2L_0.                                  (8)

Thus J diverges in actual incidence probability if and only if L_0
does. Only the o(1) safe, regular-profile, and zero-only exceptions are
discarded. No h>=epsilon sqrt(r) truncation or epsilon limit is needed.
The older general phase-spacing estimate remains true but is unnecessary
for this equivalence after zero-only feasibility has been proved.

## 4. Two-sided reciprocal comparison under the same actual law

Impose the regular profile domain used in the fully audited note
`PBBS_ZERO_OR_ONE_FEASIBILITY_AND_DISTINCT_LABEL_RECIPROCAL_20260908.md`:

    P=p_1-2>=8,             1/16<=ell_1/P<=1/4.             (9)

It has actual-incidence probability 1-o(1). On the safe fibre, row-one
coordinates 0,-1 and the base top-row coordinate are forced zero. The
other upper coordinates retain their exact conditional composition laws.
Restrict further to the E_2-measurable zero-only event of Section 3;
doing so does not alter those conditional laws at a fixed E_2.

Let N_virt be the actual virtual phase counter after row one is sampled.
Let K_C be the number of ACTUAL top-zero, C-short partner traces covering
the sampled edge, after row zero is sampled as well, including the base.
All share the invariant GOOD profile. Every actual such partner has a
physical birth phase counted by N_virt, and every successful virtual
phase is a feasible phase. Therefore, pointwise for every upper-row
completion in this fibre,

    1<=K_C<=N_virt<=J_0<=2L_0.                              (10)

In particular,

    E_inc,c[1/K_C | E_2, safe base] >= 1/(2L_0).            (11)

The selected-label composition argument of the 0/1 note gives an absolute
constant A with E[1/N_virt|E_2,safe base]<=A/L on (9). Its exact top-row
reciprocal and tower step then give E[1/K_C|E_2,safe base]<=4A/L.
Here L=L_0, so altogether

    1/(2L_0) <= E_inc,c[1/K_C | E_2, safe base]
                                      <= 4A/L_0.          (12)

These constants do not depend on h,c,C,r on the stated domain. The
probability of its complement may depend on the fixed c,C. K_C in
(10)-(12) is the top-zero partner congestion used by the compiler; the
pointwise comparison has not been asserted for a larger unrestricted
partner family.

For an unconditional formulation, define L_0=1 on the discarded
exceptional set. Reciprocals are bounded by one, and the safe base event
has probability 1-o(1). Integrating (12) therefore gives

    (1/2) E_inc,c[1/L_0]-o(1)
       <= E_inc,c[1/K_C]
       <= 4A E_inc,c[1/L_0]+o(1).                         (13)

Consequently reciprocal decay, L_0-divergence, and J-divergence are
equivalent in this actual-incidence setting. For positive integer counts,
E[1/L_0]->0 is equivalent to L_0 tending to infinity in probability;
boundedness of the reciprocal and P(L_0<=M)<=M E[1/L_0] prove both
directions. This identifies the remaining abundance question precisely.
It does not answer that question or establish coefficient one.
