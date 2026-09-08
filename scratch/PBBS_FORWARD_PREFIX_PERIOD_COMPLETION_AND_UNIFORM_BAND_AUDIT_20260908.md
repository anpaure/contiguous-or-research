# Forward period prefixes, exact completion masses, and the claimed 57/87 band

Date: 2026-09-08. Independent pure-proof audit by `exact_b_induction`.

Input: `scratch/FORWARD_PREFIX_PERIOD_UNIFORM_USER_CLAIMS_20260908.md`.
No mathematical computation, prefix census, or transcript replay was run
for this audit. The finite method below passes, subject to the retained
PBBS support, particle-reduction, and original rooted pruning-fibre
theorems. The claimed 713 numerical certificates were not supplied with
the transcribed submission and are not certified by this note.

## 1. Source interfaces and indexing

The exact period and rooted multiplicity inputs are proved in
`scratch/PBBS_EXACT_TRANSLATED_RETURN_PERIOD_AND_SIGNATURE_MULTIPLICITY_AUDIT_20260908.md`,
Sections 2–6. The equivalent time-and-rotation recursion and ordered-row
Möbius count are proved in
`scratch/PBBS_EXACT_SYMMETRY_SIGNATURE_RECURSION_AND_NONPRIMITIVE_TOP_GF_AUDIT_20260908.md`,
Sections 1–4. In particular, these are counts of original ordered gap
rows, without division by a row-rotation or necklace factor.

Write the successive nonempty pruning sizes and their terminal zero as

    a_0=r > a_1 > ... > a_(h-1) > a_h=0,
    n_s=2a_s+1.

The terminal physical circumference is n_h=1. Row s has n_(s+1) slots,
least cyclic period d_s dividing n_(s+1), and total mass

    ell_s=a_s-2a_(s+1)+a_(s+2),

where the terminal convention is a_(h+1)=0. For its one-slot final row,
ell_(h-1)=a_(h-1) and d_(h-1)=1. A zero row has least period one too.

The original inverse-pruning fibre is a rooted bijection: given a child
of semilength t with p peaks, a parent has semilength t+p+ell, and its
incoming row is an arbitrary weak composition of ell into 2t+1 slots.
Its cardinality is binomial(ell+2t,2t). This source is restated explicitly
in `scratch/PBBS_AUXILIARY_BOLTZMANN_JOINT_PROFILE_ATOM_INDEPENDENT_AUDIT_20260908.md`,
Section 1. The fact used here is the finite bijection, not the auxiliary
probability measure from later sections of that note.

All statements below concern r>=1, as do the submitted finite bands.
The empty r=0 word can be treated separately and is not assigned the
undefined expression K(0,b).

## 2. Forward beta and partial period divisors

Set beta_0=0 and compute

    beta_(s+1)=(1+n_(s+1)*beta_s)/n_s.                    (2.1)

Let sigma_j=sum_(i=0)^(j-1) 1/(n_i*n_(i+1)), with sigma_0=0.
Then induction gives

    beta_j=n_j*sigma_j.                                  (2.2)

Indeed, substituting beta_s=n_s*sigma_s in (2.1) gives
1/n_s+n_(s+1)*sigma_s=n_(s+1)*sigma_(s+1). Thus

    beta_(s+1)/d_s
      =(n_(s+1)/d_s)*sigma_(s+1).                        (2.3)

The already proved exact denominator formula therefore becomes

    v=lcm_(s=0)^(h-1) den(beta_(s+1)/d_s).               (2.4)

This is exact, including nonprimitive and zero rows. All n_s are odd,
so every denominator and their lcm are odd. Consequently v is both the
physical f period and the g=f^2 owner-cycle period.

Moreover n_0 divides v. At the first row beta_1=1/n_0, so the first
denominator is exactly n_0*d_0. Equivalently, the equality-particle
displacement identity at an unrotated physical return says v=n_0*m
for an integer m. The latter also explains why this divisibility is
available before any row has been processed.

Hence, after processing rows j<s, the quantity

    P_s=lcm(n_0, den(beta_(j+1)/d_j) for j<s)             (2.5)

divides every complete period of a root extending that prefix. Its
correct initial value is P_0=n_0. Refining row s changes it to

    P_(s+1)=lcm(P_s, den(beta_(s+1)/d_s)),                (2.6)

which is a positive integer multiple of P_s. No unprocessed row period
is guessed or replaced by a primitive-row period.

## 3. Exact Narayana completion mass

For integers a>=1 and 0<=b<a, let K(a,b) be the number of rooted Dyck
words of semilength a whose first pruning has semilength b. Pruning
deletes exactly one up-step per peak, so these are precisely the words
with a-b peaks. The exact Narayana count gives

    K(a,b)=binomial(a,b)*binomial(a,b+1)/a.               (3.1)

The two binomial choices are complementary to the usual expression
binomial(a,a-b)*binomial(a,a-b-1)/a. For an independent counting
derivation, `scratch/PBBS_EXACT_NARAYANA_CORE_INCIDENCE_LAW_20260908.md`,
Section 3, counts cyclic positive run compositions and divides by the
number of one-run starts; its equation (6) gives exactly this Narayana
formula without an additional root-rotation weight.

At a prefix ending in specified consecutive sizes

    a_s=a, a_(s+1)=b,

suppose w is the product of the exact ordered-row class counts for
rows j<s. All those row masses are determined, because their formulas
use sizes only through a_(s+1). The still-unspecified depth-s core is
any of the K(a,b) words just counted. The original rooted inverse-array
bijection allows every choice of each upper row for every such core,
and the counts depend only on the specified sizes and periods. Therefore
the exact number of original roots represented by this prefix is

    M=w*K(a,b).                                         (3.2)

This is a cardinality identity, not an independence approximation.
The prefix must not impose unrecorded restrictions on core shape or
individual row coordinates; such restrictions would require a different
completion mass.

The natural initial leaves are (s,a,b,w)=(0,r,b,1), for 0<=b<r. Their
masses sum to Cat_r, because

    sum_(b=0)^(r-1) binomial(r,b)*binomial(r,b+1)/r
      =binomial(2r,r-1)/r=Cat_r.                         (3.3)

Thus they partition all rooted words before any least-period row has
been selected. A single initial root node of mass Cat_r can equivalently
be split into these leaves.

## 4. Refinement identity and all boundary cases

Assume b>0. A depth-(s+1) core of semilength b has some next pruning
size c with 0<=c<b, and hence b-c peaks. Its parent of size a requires

    ell=a-b-(b-c)=a-2b+c>=0.

The complete allowed range is consequently

    max(0,2b-a) <= c <= b-1.                             (4.1)

It is nonempty whenever 0<b<a: since a>=b+1, its lower endpoint is
at most b-1. For such a core, the parent incoming row has 2b+1 slots
and ell units, so its total number of ordered choices is

    binomial(ell+2b,2b)=binomial(a+c,2b).                 (4.2)

There are K(b,c) possible child cores. The rooted inverse-pruning
bijection partitions the parents counted by K(a,b) according to c,
then that child, then its incoming row. Hence the exact finite identity
is

    K(a,b)=sum_(c=max(0,2b-a))^(b-1)
                          binomial(a+c,2b)*K(b,c).      (4.3)

This is also a direct combinatorial proof of the submitted binomial
identity. Terms outside the lower boundary would require a negative
row mass and are not included. There is no K(b,b) term, because a
nonempty Dyck word has at least one peak.

Split each row count (4.2) into its exact least-period classes
chi(2b+1,ell;d). The classes are disjoint, their sum is (4.2), and
the established divisor-inversion formula includes ell=0 and d=1.
Each refined prefix then has

    s'=s+1, a'=b, b'=c,
    w'=w*chi(2b+1,ell;d),
    P'=lcm(P,den(beta_(s+1)/d)).

Zero-mass classes can be omitted. Summing its exact mass w'*K(b,c)
over every permitted c and d gives exactly w*K(a,b). Thus refinement
preserves mass, not just an upper bound on mass.

If b=0, (3.1) gives K(a,0)=1. The remaining depth-s word is the unique
height-one word of semilength a. There is no c refinement and no use
of K(0,c). Its incoming row is still row s: it has one slot, total
mass a, and least period d_s=1. Its final denominator
den(beta_(s+1)) must be included before declaring the completed period
exact. Stopping before that inclusion still gives a valid period lower
bound P and hence a valid upper charge, but it is not the exact terminal
period unless that denominator already divides P.

## 5. Height cap and refinement monotonicity

The height of a rooted Dyck word is its number of nonempty successive
peak-pruning levels. At a prefix ending in a_s=a and a_(s+1)=b, the
original height is s plus the height of the depth-s word. Its nonempty
parent contributes one more level, while a child of semilength b has
height at most b. Therefore

    h <= H=s+b+1.                                       (5.1)

For b=0 this is exact: h=s+1. At a nonterminal refinement to c<b,

    H'=s+c+2 <= s+b+1=H.                                (5.2)

Together with P' being a multiple of P and mass conservation, this
proves

    sum_children M'*(2H'-1)/P' <= M*(2H-1)/P.            (5.3)

Thus the sum of unrounded leaf charges never increases under any
sequence of valid refinements. The priority order is irrelevant to
validity; it can affect how soon a desired upper certificate is found.

This assertion must not be transferred to independently rounded leaf
charges: replacing one ceiling by several can increase their sum.
The user's stated distinction between unrounded monotonicity and
rounded validity is correct.

## 6. Literal construction charge and an integer certificate

For the retained height-adaptive constructor in odd dimension n=2r+1,
each owner cycle of period v and height h contributes its v letters
and 2h-1 collar letters. Every normalized root has n distinct physical
rotations, and height and period are rotation invariant. Consequently
its excess C=N-W(n) has the exact root-average expression

    C=n*sum_roots (2h-1)/v,
    C/W(n)=(1/Cat_r)*sum_roots (2h-1)/v,                (6.1)

where W(n)=n*Cat_r. This is the retained construction's charge; it is
not a lower bound on the optimum nu(n).

For any finite complete leaf partition with exact masses M, period
divisors P, and height caps H, (2.5) and (5.1) give

    C/W(n) <= (1/Cat_r)*sum_leaves M*(2H-1)/P.            (6.2)

No assumption that individual roots or leaves are independent is used.
It suffices that the leaves partition every root once with the proved
mass. Even an adaptive stopping rule is valid when every replacement
uses the complete children from Section 4.

Define the integer

    U=sum_leaves ceil(M*(2H-1)/P).                       (6.3)

Then C<=nU and hence N<=W(n)+nU. For any positive integer D,

    D*U < Cat_r                                         (6.4)

therefore proves the strict inequality

    nu(n) <= N < (1+1/D)*W(n).                           (6.5)

The ceiling can be computed with integer arithmetic as
(M*(2H-1)+P-1)//P. Every stopping point gives a valid U; no monotonicity
of rounded U is required. To certify a reported value, a replay must
check the prefix partition, all row counts and period updates, terminal
handling, height caps, and the sum of these integer ceilings. An
unaccompanied final decimal estimate is not a replacement for that data.

## 7. What the claimed finite band would imply

The submission reports (6.4) with D=1000 for r=28,...,42 and D=10000
for r=43,...,740. These are 15 and 698 cases, respectively, totaling
713. They would cover odd dimensions 57,...,1481 with the stated
piecewise accuracy. The standard trimmed one-coordinate lift has
length 2N and the next even width is exactly twice the odd width, so
each strict relative bound also holds in the succeeding even dimension.

The retained analytic envelope E_r is decreasing for r>=4. Its
independently verified certificate at r=741 gives

    E_741 <= 99868373195185/10^18 < 1/10000.

The value and monotonicity are recorded in
`HEIGHT_ADAPTIVE_UNIFORM_FINITE_THRESHOLDS_20260908.md` and
`scratch/SYMMETRY_DESCENT_UNIFORM_THRESHOLD_EXACT_NUMERIC_CERTIFICATE_20260908.md`.
This audit relies on that existing certificate and has not rerun it.
It supplies all odd dimensions from 1483 and their succeeding evens.

Therefore, IF the 713 reported integer certificates pass, the combined
argument proves

    nu(k)<1.001*W(k) for every k>=57,
    nu(k)<1.0001*W(k) for every k>=87.

The claimed predecessor failures at odd dimensions 55 and 85, together
with the same specific doubled lift at 56 and 86, would show minimality
of these uniform thresholds for that unchanged constructor and lift.
They would not prove minimality of the thresholds for nu(k), since a
different word can improve the constructor.

## 8. Audit outcome and missing evidence

The forward beta formula, its equivalence to the exact period theorem,
partial divisibility, K(a,b) completion mass, full refinement identity,
terminal b=0 convention, height cap, unrounded monotonicity, and rounded
integer upper certificate all PASS the pure-proof audit.

The supplied transcription contains no actual U_r values or prefix
transcripts for the 713 newly claimed cases. The reported 361709
refinements, 38326911 prefix nodes, maximum depth18, and 180 replays
remain user-reported counts. This note does not reproduce those counts,
the additional reported small-state checks, or the predecessor census.
Until the finite package is supplied and independently checked, the
uniform starting points57/87 remain conditional on that missing finite
certificate rather than newly verified numerical results.

This is an audit of a sharper finite upper-bound method. It does not
change the active all-k exact objective or assert that the optimal word
has zero excess above B(k).
