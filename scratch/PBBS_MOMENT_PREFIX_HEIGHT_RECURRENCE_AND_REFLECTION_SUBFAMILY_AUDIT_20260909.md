# Height-moment prefixes: exact recurrence and finite reflection bound

Date: 2026-09-09. Independent pure-proof audit by `exact_b_induction`.

Reviewed input: `/Users/amir.nuriyev/Downloads/MOMENT_PREFIX_ADVANCE.md`,
with the requested focus on Sections 3–4. Verdict: **PASS**, with the
domain and implementation guards stated explicitly below. No mathematical
execution, generator run, height-table computation, or transcript replay
was performed by this reviewer.

The uploaded proof and a reported verification log do not supply the
claimed 3356 finite certificates or their generator/transcript package.
This audit therefore does not independently certify the claimed uniform
starting dimension137 or any reported execution count.

## 1. Definitions and finite inherited fibre

For integers a>=1 and 0<=b<a, let

    K(a,b)=binomial(a,b)*binomial(a,b+1)/a,
    H(a,b)=sum_{|D|=a, |partial D|=b} h(D).

K is the exact number of rooted Dyck words in this class; H is its integer
height TOTAL. It is not a mean or a probability-weighted approximation.
The original rooted inverse-pruning bijection, audited in
`scratch/PBBS_FORWARD_PREFIX_PERIOD_COMPLETION_AND_UNIFORM_BAND_AUDIT_20260908.md`,
Sections 3–4, says that a child of size b with next size c has exactly

    binomial(a+c,2b)

parents of size a, provided max(0,2b-a)<=c<b. Equivalently, its original
incoming row has 2b+1 slots and nonnegative mass a-2b+c. Every such row
is included, without a root-rotation or necklace quotient.

The empty Dyck word has size and height zero, but the displayed K(a,b)
formula is NOT defined at a=0. The algorithmic terminal case is b=0 with
a>=1, handled directly rather than calling K(0,c) or H(0,c).

## 2. Exact height-total recurrence

Deleting all peaks simultaneously lowers the height of a nonempty Dyck
word by exactly one. To see both directions, every vertex at the old
maximum is a peak and is removed, so the new height is at most one less.
Immediately before the first highest peak, an up-step reaching height
h-1 is not itself deleted as part of a peak, since the next step is up.
For h>=2 it remains and attains height h-1 after the zero-net-height peak
pairs are removed. For h=1 the remaining word is empty, of height zero.
Thus the decrease is exactly one in every case.

When b=0 the parent is the unique word (10)^a, of height one. Hence

    K(a,0)=H(a,0)=1.                                    (2.1)

For b>0, every child E in the class (b,c) has the same number
binomial(a+c,2b) of preimages, and every such parent has height h(E)+1.
Summing this equality over all children and all allowed c gives

    H(a,b)=sum_c binomial(a+c,2b)*(H(b,c)+K(b,c))
          =K(a,b)+sum_c binomial(a+c,2b)*H(b,c).          (2.2)

The last equality is the exact completion-mass identity already proved
from the same fibre. The range is max(0,2b-a)<=c<=b-1, including its lower
boundary when the row mass is zero. The recursive first argument b is
strictly less than a, and b=0 is a terminal base, so this is a finite
triangular integer recurrence with no circular dependence.

In particular every class member has h(D)<=b+1, giving

    K(a,b)<=H(a,b)<=(b+1)*K(a,b).                        (2.3)

The illustrative decimal H(100,50)/K(100,50) in the uploaded proof was
not evaluated by this audit and is not a premise of any result here.

## 3. Exact unfinished-prefix moment charge

At depth s>=0, suppose the specified upper rows have multiplicity w and
the remaining class is (a,b). The original height is s+h(D), and the
period divisor P is common to EVERY completion. Its contribution to the
unnormalized root sum is bounded by

    (w/P)*sum_D (2s+2h(D)-1)
       =w*((2s-1)*K(a,b)+2H(a,b))/P.                    (3.1)

This uses the pointwise inequality 1/v(D)<=1/P before summing. It does
not factor a correlated height/period expectation. For s=0 the coefficient
2s-1 is negative, but K is exact and H>=K makes the total numerator
2H-K>=K>0. Replacing H by an upper bound remains safe because its
coefficient is positive. One must not replace the negative K term by
an arbitrary upper estimate; the proposed method uses exact K.

Equation (2.3) shows that (3.1) is no greater than the previous cap

    w*K(a,b)*(2s+2b+1)/P.

At b=0 it becomes w*(2s+1)/P, matching the exact height s+1. If the
final one-slot period row has not yet been included in P, this is still
a valid upper bound; including its exact denominator improves it. The
terminal period rule remains the one in the earlier forward-prefix audit.

The exact unrounded moment charge is nonincreasing under complete
refinement: the children partition the parent family, preserve its total
original-height weight, and have period divisors that are multiples of
P. This observation does not assert monotonicity after separate ceilings
or after replacing exact height totals by independently chosen bounds.

## 4. Reflection counts with the correct endpoints

Fix a>=1, n=2a+1. Encode the n-site physical words as bridges with a
up-steps +1 and a+1 down-steps -1. Their total increment is -1. At a
fixed linear cut let M and m be the maximum and minimum partial sums,
including both endpoints. Thus M>=0 and m<=-1.

For every integer j>=1, the reflection bijections give

    number{M>=j}=binomial(n,a-j),
    number{-m>=j}=binomial(n,a+1-j),                     (4.1)

with out-of-range binomials zero. For the upper event, reflect the tail
after its first hit of j: the final height becomes 2j+1, so the number
of up-steps is a+j+1 and the count is binomial(n,a-j). Conversely every
bridge ending at 2j+1 must hit j, giving the inverse. For the lower event,
reflection after the first hit of -j changes the endpoint to 1-2j,
with a+1-j up-steps. Again that endpoint forces the required hit. These
arguments give exactly the two different shifts in (4.1).

Every rooted size-a Dyck word has n distinct physical rotations, because
gcd(a,2a+1)=1 precludes any nontrivial cyclic repetition of its step word.
There are n*Cat_a=binomial(n,a) physical words, and each has the unique
canonical Dyck rooting. Thus summing over all physical bridges is exactly
summing all n rotations of each Dyck root once.

Its canonical height h satisfies h<=M-m at EVERY cut. Indeed, in the
canonical root there is a proper cyclic interval of increment h from
height zero to a highest vertex. If it does not wrap the chosen linear
cut, the range is at least h. If it wraps, the complementary nonwrapping
interval has increment -1-h, so that range is at least h+1. This proves
the needed inequality without assuming the ranges of different cuts
are equal.

## 5. Finite excess bound for every subfamily

For any integer t>=0,

    (h-2t)_+ <= (M-t)_+ + (-m-t)_+.                     (5.1)

This follows from h<=M-m and (x+y)_+<=x_++y_+, applied to M-t and -m-t.
Let F be ANY subfamily of K size-a Dyck roots, including a peak-conditioned
class. Then

    sum_{D in F} h(D)
      <=2tK+sum_{all roots}(h(D)-2t)_+.

Apply (5.1) to every rotation of every root, sum, and divide by n. For
integer-valued maxima, summing their positive tails uses j>=t+1, so
only the positive-j reflection formulas above are needed. Since M<=a
and -m<=a+1, for 0<=t<a and j_0=a-t one obtains

    sum_F h(D) <=2tK+B_a(t),

    B_a(t)=(sum_(i=0)^(j_0-1) binomial(n,i)
                  +sum_(i=0)^j_0 binomial(n,i))/n.       (5.2)

The upper-maximum sum ends at j_0-1 and the lower-minimum sum ends at
j_0. These off-by-one endpoints exactly reflect the bridge endpoint -1.
The division by n is required and justified by the complete rotation
count; there is no extra independence or uniform-cycle assumption.

The t=0 case is included: the tail sums run through a-1 and a and the
bound pays the entire positive height total. The case K=0 is also valid
as a subfamily bound, though not needed for the positive Narayana classes.
For t>=a no reflection estimate is needed: h(D)<=a, and the deterministic
class cap in (2.3) suffices. The displayed B and G formulas are not to be
evaluated at a negative binomial index when t>a.

## 6. Geometric upper bound for the two binomial tails

For 0<=j<=a<n/2, consecutive lower-tail terms satisfy

    binomial(n,i-1)/binomial(n,i)=i/(n-i+1)
        <=j/(n-j+1)<1, 1<=i<=j.

Bounding the finite backwards sum by its infinite geometric series gives

    sum_(i=0)^j binomial(n,i)
       <=binomial(n,j)*(n-j+1)/(n-2j+1).                (6.1)

With j=j_0=a-t>=1 this factor is (a+t+2)/(2t+2). For the other tail use
j_0-1, and write

    binomial(n,j_0-1)
        =binomial(n,j_0)*(a-t)/(a+t+2).

Its geometric factor is (a+t+3)/(2t+4). Substituting both expressions
in (5.2) proves exactly

    B_a(t)<=G_a(t)
      =binomial(2a+1,a-t)/(2a+1)
        *((a+t+2)/(2t+2)
          +(a-t)*(a+t+3)/((a+t+2)*(2t+4))).              (6.2)

All denominators are positive at 0<=t<a. At j_0=1, corresponding to
t=a-1, the second tail consists only of binomial(n,0)=1 and the displayed
expression handles it exactly. The t=0 formula is finite and valid too.
Every quantity is rational; no normal approximation or floating-point
tail estimate is involved.

## 7. Safe finite height bound and implementation guards

For a>=1, 0<=b<a, K(a,b)>0. Therefore the least nonnegative q with
2^q*K(a,b)>=Cat_a exists. The proposed

    t=floor(sqrt((a+1)*(q+2)))+1

is a permissible integer choice, but its efficiency is not part of the
proof. If t<a, equations (2.3), (5.2) and (6.2) give

    H(a,b) <= Hhat(a,b)
      :=min((b+1)*K(a,b), 2t*K(a,b)+ceil(G_a(t)))
      <=(b+1)*K(a,b).                                  (7.1)

If t>=a, use only (b+1)*K(a,b) BEFORE attempting to evaluate G. At a=0
there is the separate empty core, not this formula. For an abstract empty
subfamily K=0, (5.2) is valid but the q heuristic is undefined and should
not be invoked. Actual K(a,b) in its specified domain is always positive.

Using exact H for a<=250 and (7.1) for larger a preserves the claimed
height bound. Whether an uploaded implementation really computes that
table, guards these cases and rounds outward still requires its source
and replay; those files were not included with the material reviewed here.

## 8. Scope of this PASS

Sections 3–4 of the uploaded proof provide valid new height-total and
reflection-subfamily bounds on the retained finite fibre. They can safely
replace the old deterministic height cap in a prefix upper certificate.
This audit does not by itself certify the row-symmetry corrections,
sparse-reserve implementation, predecessor calculation, or 3356-case
transcript band from the other sections. Root is reviewing those parts.

In particular the supplied proof/verification log is not the actual
certificate collection. The uniform threshold137 remains conditional on
the finite calculations being supplied and independently checked. The
active objective nu(k)=B(k) for all k remains separate from this finite
upper-bound improvement.

## 9. Subsequent pre-execution review of an independent bounded checker

This author subsequently read all of
`scratch/verify_moment_prefix_structure_and_r68_20260909.py` and reported
PASS before execution, with no correction required. This is a newly
written independent checker for one r=68 attempt; it is not the missing
uploaded generator or3356-case transcript package.

The source builds exact K and H through a=100 using the proved adjacent
binomial ratio and checks every class mass. Direct Dyck generation through
a=10 checks counts, heights and one-step pruning. Direct deficit-one
bridges through a=9 check the two shifted reflection formulas, canonical
rooting and n rotations per root. The geometric-tail comparison includes
every t=0,...,a-1 through100; the heuristic branch checks t<a before G.

Ordered composition rows are separately enumerated in the small domain.
All terminal small-prefix classes are compared with a hash-pinned prior
period census. The chosen r=68 charge integrates the next row over every
c and every least-period class using exact H and exact rational arithmetic;
no approximate symmetry correction or sparse reserve is used. The program
checks the primitive-baseline decomposition and that the exact integrated
charge does not exceed the exact moment charge in its small-prefix audit.

All child classes are retained at each r=68 split, and child mass must
equal parent mass. Rounded charges may increase and are freshly summed
from the final complete frontier. The priority-free replay regenerates
all children, recomputes period updates with Fraction, sums direct c/d
height contributions, and consumes every final leaf exactly once. It uses
the same exact H table generated and structurally validated earlier in
that run; it does not claim an unrelated second height-table algorithm.

The source has h100 and hash guards, 60 CPU seconds, 90 wall seconds and
1 GiB address-space limits, with build stops reserving time for replay.
A hard interruption before completed replay is not a completed certificate.
No execution result is asserted in this pre-execution review, and even a
successful r=68 check would certify only that single finite case.
