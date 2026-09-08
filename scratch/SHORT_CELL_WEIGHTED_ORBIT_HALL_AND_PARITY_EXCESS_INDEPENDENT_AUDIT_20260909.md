# Short-cell candidates, weighted orbit deficiency, and parity excess

Date: 2026-09-09. Status: all three transcribed mathematical claims pass,
with the individual-versus-simultaneous and matching-versus-equivariance
qualifications below. This is an independent pure-proof audit by the
induction agent. No mathematical execution was performed.

The root supplied the exact claim formulas. No unavailable construction
package or Hall-flow transcript is assumed. In particular this audit does
not certify the reported physical deficiency462.

## 1. The individual short-cell criterion

Let E_i be nonempty finite-set envelopes. Let I range over a specified
family of protected windows, each with original union U_I. Fix a nonempty
cell J, leave all letters outside J unchanged, and seek nonempty caps
A_i subseteq E_i inside J such that all protected unions survive and
the union on J is exactly S. Put

    U_J = union_(i in J) E_i,
    K_J = union_(protected I meeting J)
              [U_I minus union_(i in I minus J) E_i].

Then feasibility is exactly

    K_J subseteq S subseteq U_J,
    S intersect E_i is nonempty for every i in J.       (1.1)

Necessity: a coordinate of K_J cannot be supplied outside J to at least
one protected window, so it must be retained in the union S. No cap can
introduce anything outside U_J. Every nonempty cap A_i contributing to S
requires S intersect E_i nonempty.

For sufficiency set A_i=E_i intersect S on J. These caps are nonempty by
(1.1), and their union is S because S subseteq U_J. If a protected-window
coordinate lacks a supplier outside J, it belongs to K_J and hence to S;
all its original occurrences inside J are retained. Every other such
coordinate has an unchanged outside supplier. Thus every protected union
is exactly preserved; caps cannot enlarge one.

This proof works for arbitrary protected sets and arbitrary cells, so it
applies in particular to cyclic q-windows and proper cells of length<q.
For q=1 the stated short-cell range is empty. If cyclic indices repeat,
the sets in the displayed unions are interpreted as physical positions;
there is no multiplicity contribution to OR.

Attribution: the deficit core and the explicit maximal cap are already
proved in [the exact short-target note, Section2](PBBS_EXACT_SHORT_TARGET_CAPS_AND_CAPACITATED_MATCHING_REDUCTION_20260908.md).
That note has nonempty forced pins inside K_J, which make its nonempty-cap
condition automatic. The present explicit intersection condition is the
correct generalization when no such pin hypothesis is given.

The theorem is for ONE selected cell while its exterior stays unchanged.
Several individually feasible overlapping cells need not be simultaneously
realizable. Neither a target-to-cell matching nor its exact cardinality
removes those shared-letter and protected-window constraints.

## 2. Arbitrary finite-group orbit deficiency is exact physically

Let G=(X,Y;E) be a finite bipartite graph, and let a finite group Gamma act
by automorphisms preserving both sides. Include the empty set when defining

    delta = max_(A subseteq X) (|A|-|N(A)|).

For f(A)=|A|-|N(A)|, neighborhood union equality and intersection inclusion
give

    f(A union B)+f(A intersect B) >= f(A)+f(B).          (2.1)

If both A and B attain delta, both sets on the left must attain delta as
well: neither value exceeds delta and their sum is at least2delta.
Every group translate of a maximizer is a maximizer. The finite union of
all its translates is therefore an invariant maximizer.

An invariant subset is a union of whole X-orbits, and its neighborhood is
a union of whole Y-orbits. A right orbit is in that neighborhood exactly
when the quotient support graph has an edge from a selected left orbit.
Consequently

    delta = max_(S subseteq X/Gamma)
               [sum_(O in S)|O| - sum_(P in Nbar(S))|P|]. (2.2)

There is no freeness or equal-orbit-size assumption. The empty choice
keeps delta nonnegative. The deficiency form of Hall's theorem yields
the physical maximum matching cardinality |X|-delta. Equivalently this
is the maximum flow with source-to-left-orbit capacities |O|, right-orbit-
to-sink capacities |P|, and sufficiently large capacities on quotient
support edges. Integrality gives an integer optimum, and the invariant
deficiency proof shows that its VALUE equals the physical matching optimum.

This does not claim an equivariant matching or a direct phase lift of
every quotient flow matrix. For example, let the cyclic group of order6
act transitively on each side of K_(2,3), by its actions modulo2 and modulo3.
The quotient optimum and physical matching cardinality are2. An equivariant
injection from the two-point orbit into the three-point orbit cannot exist:
the group element2 fixes every left vertex but no right vertex.

Attribution: arbitrary finite groups and weighted orbit Hall already occur
in [the actuator note, Theorem2.1](../MATH_THEOREM_L_ORBIT_WEIGHTED_ACTUATOR_PLANTING_AND_GUARDED_STAR_CUT_20260801.md).
The maximum-deficiency symmetrization is also explicitly retained in
[the chronological-upset audit, Section1](../MATH_AUDIT_CHRONOLOGICAL_UPSET_HALL_AND_ADAPTIVE_ORBIT_REPAIRS_20260802.md).
The physical optimum interpretation appears in
[the flag-aperture note, Section4](../MATH_THEOREM_UNIFORM_FLAG_APERTURE_TARGET_MATCHING_20260803.md).
The submission is a valid restatement of this existing mechanism.

Applying it to the graph of individually feasible cells computes that
graph's exact physical matching number. It still does not prove a common
cap for overlapping cells. The numerical assertion delta=462 requires
the actual graph and checked primal/dual certificates; none is supplied
by these abstract arguments.

## 3. The all-rank definition of B really reduces to the central rank

The retained definition in [MASTER_HANDOFF Section2](../MASTER_HANDOFF.md)
is

    B(k)=max_(1<=s<=k) [M_s+tau_s],
    M_s=binom(k,s),  Lambda_s=sum_(1<=j<s)binom(k,j),
    tau_s=min {t>=0: t M_s+t(t+1)/2 >= Lambda_s}.

The same section proves that s=ceil(k/2) attains this maximum. Its exact
quantity F_s=M_s(M_s+1)+2Lambda_s satisfies

    F_(s+1)-F_s=(M_s+M_(s+1))(M_(s+1)-M_s+1).

Binomial unimodality and this difference locate the central maximum.
Writing a proposed length as N, each rank condition is N(N+1)>=F_s,
so the central condition suffices for all ranks. Thus the d(k)=B(k)-W(k)
in the parity claim is the true all-rank endpoint excess, not a separately
assumed central approximation. None of this asserts nu(k)=B(k).

## 4. Exact odd-to-even excess drop and threshold

Let r>=0, W=binom(2r+1,r), Lambda=4^r-1 and T(t)=t(t+1)/2. By the proved
central reduction and binomial symmetry,

    d=d(2r+1)=min {d>=0: dW+T(d)>=Lambda},
    e=d(2r+2)=min {e>=0: 2eW+T(e)>=2Lambda-W+1}.       (4.1)

The even width is exactly2W. Its smaller-rank count is exactly
2Lambda-W+1; the +1 must be retained.

First d<=r: Lambda sums r ranks, each of size at most W, so Lambda<=rW.
Also T(d)<=T(r)<=W-1. For r>=2, unimodality gives
W>=binom(2r+1,2)=r(2r+1)>T(r); r=0,1 are direct.
It follows from Lambda<=dW+T(d) that

    2Lambda-W+1 <= 2dW+2T(d)-W+1 <= 2dW+T(d),

so e<=d. For d>=2, odd minimality and integrality give
Lambda>=(d-1)W+T(d-1)+1. Subtracting the even capacity at d-2 from its
required count gives a quantity at least

    W+2T(d-1)-T(d-2)+3 > 0.

Thus e>=d-1. For d=0 or1 the lower bound follows from e>=0. Therefore

    e belongs to {d-1,d}.                              (4.2)

Put sigma=dW+T(d)-Lambda. For d>=1, substituting into the even inequality
at e=d-1 gives precisely

    e=d-1  iff  2sigma >= W+T(d)+d+1.                  (4.3)

For r=0, d=e=0 and the right side of (4.3) is false, so the statement
remains consistent if the inadmissible value d-1=-1 is interpreted as
not attained. In particular there is no hidden small-d exception to the
claimed drop-by-zero-or-one law.

The submitted examples 19/20:3/3, 21/22:3/3 and 23/24:4/3 satisfy (4.1).
For the last pair, W=1,352,078 and Lambda=4,194,303, and the exact checks are

    3W+6 = 4,056,240 < Lambda <= 4W+10 = 5,408,322,
    4W+3 = 5,408,315 < 2Lambda-W+1 = 7,036,529
                                <= 6W+6 = 8,112,474.

These are scalar algebraic substitutions, not a construction or numerical
run. Earlier finite-lift and same-parity Catalan-slack notes already use
these endpoint quantities; (4.3) is recorded here as the audited precise
odd-to-even algebraic consequence, without claiming a new all-k solution.

## 5. Separate literal-checker source reviews

I independently read the complete sources before execution for:

- `scratch/verify_k21_k22_upper_forward_first_occurrence_20260909.py`;
- `scripts/verify_k21_k22_upper_suffix_and_lift.py`.

Both source reviews passed. The first enumerates grouped first-coordinate
arrivals at every ordinary start. The second enumerates complete suffix
families and separately checks every target witness using range OR,
then checks the ordinary doubled22 word by masks and exact bytes. Both
compute the lower bound over every rank and report upper bounds without
assuming exact optimality. These are source-review findings, not execution
certificates from this agent. Literal verification and its resulting counts
belong to the executing root/frontier agents' separate reports.

