# Window-rank deficit capacity and near-deadline protection

Date: 2026-09-09. Status: pure-proof PASS under the explicit rank-floor
hypotheses stated below. No mathematical execution or table validation.

The reported length357,442 dimension21 word was not supplied and is weaker
than the already verified353,297 incumbent. This audit does not verify
that report or replace the incumbent. The capacity statements below are
separate from either construction claim.

## 1. Arbitrary-word rank-deficit inequality

Let A be a linear word of N nonempty subset letters, t>=1, and
1<=q<=N+1. Let D_<t be the number of distinct represented nonempty targets
of rank less than t. For each actual q-window put

    R_i = union_(j=i)^(i+q-1) A_j.

Then

    D_<t <= (q-1)(N+1)-q(q-1)/2
                         + sum_i (t-|R_i|)_+.          (1.1)

To prove this, assign one witness to each represented target and separate
those whose assigned witness has length<q. The number of such intervals
is exactly the first term in (1.1). At each remaining start i, extend the
q-window towards the end of the word. Its distinct OR values form a
strict inclusion chain; ranks strictly increase whenever the set changes.
Thus it has at most (t-|R_i|)_+ distinct targets of positive rank<t.
Summing this bound over starts overcounts possible repeated targets,
which is harmless. No independence, fixed middle layer, or universality
assumption is used. The case q=1 has zero short-interval term. The case
q=N+1 counts all intervals in that term and has an empty window sum.

For a cyclic word of period M and 1<=q<=M, the same argument gives

    D_<t <= (q-1)M + sum_(i modulo M)(t-|R_i|)_+.       (1.2)

There are M indexed windows of each positive length<q. Every cyclic
target has a witness of length at most M, so extending only to one full
period suffices. Again collisions between indexed windows only loosen
the bound. A range guard on q is appropriate; the linear polynomial
should not be used for arbitrary q>N+1.

This extends the retained chain-at-a-start and short-interval capacity
arguments. The universal endpoint count is in
[MASTER_HANDOFF Section2](../MASTER_HANDOFF.md), and the width-sized cyclic
capacity specialization is already in Section3.8 and
[the uniform-window audit](UNIFORM_CYCLIC_MIDDLE_WINDOW_CAPACITY_AND_OPENING_OBSTRUCTION_20260909.md).

## 2. Exact finite protection obstruction

Use the TRUE all-rank endpoint bound B(k), whose central maximizer is
proved in MASTER_HANDOFF Section2. Write

    s=ceil(k/2),   M=binom(k,s),   d=B(k)-M,
    Lambda=sum_(j=1)^(s-1)binom(k,j),
    T(a)=a(a+1)/2,   sigma_lin=dM+T(d)-Lambda.

Let 0<=g<=min(d,s-1), set q=d-g+1, and define

    Delta_g=sum_(j=1)^g [M-binom(k,s-j)].

Suppose a universal linear word has exact length N=M+d and EVERY q-window
has rank at least s-g. Applying (1.1) with t=s-g makes the deficit sum zero.
The demand and short-interval capacity are exactly

    Lambda_(s-g)=Lambda-gM+Delta_g,
    count(length<q)=(d-g)M+T(d)-T(g).

Therefore

    Delta_g+T(g) <= sigma_lin.                         (2.1)

For a universal cyclic word of period M satisfying the same rank floor,
(1.2) instead gives

    Delta_g <= sigma_cyc := dM-Lambda.                 (2.2)

The case g=0 is included. Sigma_cyc can be negative; then the hypothesized
cyclic rank floor is impossible. It should not silently be replaced by
the nonnegative linear slack. The case g=s-1 simply has t=1 and no
positive target below t, and the displayed algebra remains valid.

The intended compiler hypothesis is an explicit FLAT RANK LADDER:
the native q-window rank is s-d+q-1=s-g and these q-windows are protected
under recoding. This immediately supplies the required rank floor.
Merely asserting that the native (d+1)-windows have rank s does not,
without further structure, establish the shorter-window floor. The q
here is the protected native window length, not the witness length of
a maximal-rank target in an arbitrary cyclic universal core.

These are necessary conditions for exact-budget coverage. They do not
construct a compiler, a matching, or a source satisfying the rank floor.

## 3. The sharp cube-root bound on the protection gap

Minimality of d gives

    0<=sigma_lin<M+d,       d=Theta(sqrt(k)).            (3.1)

The second estimate and its leading constant are already proved for B(k)
in MASTER_HANDOFF Section2. Thus either (2.1) or (2.2) implies
Delta_g/M<=1+o(1), because sigma_cyc<=sigma_lin.

Here is the needed binomial expansion with its uniformity made explicit.
For odd k=2r+1 and s=r+1,

    binom(k,s-j)/M
       = product_(i=1)^(j-1) (r+1-i)/(r+1+i).

For even k=2r and s=r,

    binom(k,s-j)/M
       = product_(i=0)^(j-1) (r-i)/(r+i+1).

First g=o(sqrt(k)): otherwise a subsequence g>=epsilon sqrt(k), together
with g<=d=O(sqrt(k)), gives a constant positive deficit for each of
Theta(g) indices j between g/2 and g. This follows directly by taking
logs in these products. Their sum would make Delta_g/M unbounded,
contradicting (3.1).

Taylor expansion of these finite products, uniformly for j<=g=o(sqrt(k)),
then gives, when g grows,

    Delta_g/M = 2g^3/(3k)
                          + O(g^2/k + g^5/k^2).       (3.2)

For odd k the leading single-rank deficit is 2j(j-1)/k; for even k it is
2j^2/k, with the difference absorbed by the displayed error. In both
cases the relative error in (3.2) tends to zero for growing g=o(sqrt(k)).
If g stays bounded the desired conclusion below is automatic.

Combining (3.1)-(3.2) proves

    g <= (3k/2)^(1/3)(1+o(1)),
    q >= d+1-(3k/2)^(1/3)(1+o(1)).                   (3.3)

Since 1<=q<=d+1 and d=Theta(sqrt(k)), this yields q/d -> 1.
It is a restriction on protected window length under the explicit rank
floor, not a new unconditional lower bound on every source aperture.

## 4. Tight odd dimensions give the sixth-root gap

Let k_j be the largest odd dimension with d(k_j)<=j. The already proved
same-parity recurrence in
[the Catalan-slack note, Section1](../MATH_ATTACK_H_KPLUS2_DIAMOND_CATALAN_SEAM_RELAXED_INDUCTION_20260728.md)
states that odd d is nondecreasing and changes by at most1 at each step.
Together with its unbounded asymptotic growth, this gives d(k_j)=j and
d(k_j+2)=j+1.

Write k_j=2r+1 and M=binom(k_j,r). The next width and lower demand are

    M^+=4M-2M/(r+2),      Lambda^+=4Lambda+3.

Depth j fails at the next dimension. Substitution gives the exact strict
inequality

    4 sigma_lin < [2j/(r+2)] M + 3T(j)+3.              (4.1)

This is precisely the old Catalan-slack threshold with its parameter
shift, not a new recurrence. Since j=Theta(sqrt(k_j)), (4.1) implies

    sigma_lin/M=O(k_j^(-1/2)).

Combining with (2.1) or (2.2) and (3.2) gives

    g=O(k_j^(1/6)).                                   (4.2)

The reported finite table of critical odd dimensions
9,21,39,61,89,123 for budgets2,...,7 was not independently certified in
this audit. No numerical run was authorized or performed. Formula (4.1)
supplies an exact way to verify each entry when exact arithmetic records
are provided; the table is not a premise of the asymptotic proof.

## 5. What the dimension21 pair bound actually says

Taking q=2 and t=9 in (1.1) yields for a universal21 word of length N

    sum_i (9-|A_i union A_(i+1)|)_+
            >= sum_(j=1)^8 binom(21,j)-N
             = 401929-N.                             (5.1)

Thus the displayed49,210 bound is for a PUTATIVE EXACT-length word
N=B(21)=352719. It is not the numerical deficit bound at the incumbent
length353297 or at the unprovided weaker reported length357442.
The exact-budget implication is meaningful: pairs of rank at least9
contribute zero, while rank-deficient pairs must collectively supply the
required deficit. It gives no lower-target assignment by itself.

## 6. Audit boundary

The arbitrary-word inequalities, exact slack obstruction, cube-root
protection restriction, and critical-subsequence sixth-root restriction
all pass under the stated hypotheses. Their proofs do not use the new
word report or its unprovided constructor. All-k equality remains open.

