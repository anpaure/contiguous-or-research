# Narayana reciprocal-particle moment and a monotone uniform finite envelope

2026-09-08. Independent pure-proof audit by `exact_equality_structure`
of the analytic part of
[SYMMETRY_DESCENT_UNIFORM_THRESHOLDS_USER_CLAIMS_20260908.md](SYMMETRY_DESCENT_UNIFORM_THRESHOLDS_USER_CLAIMS_20260908.md).

**PASS.** The reciprocal moment, rational inequality, both Vandermonde
bounds, the displayed J_r and E_r, and strict decrease of E_r for
r>=4 are valid. Together with the separately executed exact finite
comparisons, they prove

    nu(k)<1.01 W(k)     for every integer k>=29;
    nu(k)<1.001 W(k)    for every integer k>=327;
    nu(k)<1.0001 W(k)   for every integer k>=1483;
    nu(k)<1.00001 W(k)  for every integer k>=6849.

No mathematical program was run for this proof. The numerical and
finite-band checks are explicitly attributed to the independent
certificate in Section 8, which was read in full. This is an improved
uniform finite analysis of the retained construction, not a new
asymptotic power or a new literal word at k=17.

## 1. Probability space and the exact collar charge

Put n=2r+1, r>=1, W_r=binom(n,r), and
Cat_r=binom(2r,r)/(r+1). A uniform physical middle state corresponds
bijectively to a uniform Dyck word of semilength r and one of n
labelled locations for its unique unmatched zero. Thus

    W_r=n Cat_r.

The height h, child circumference p, and primitivity of the original
top incoming-gap row are rotation invariant. Their joint law under
uniform physical states is exactly their joint uniform-Dyck law.
There is no weighting by the PBBS cycle length and no extra factor
n in the probability of a root event.

Let v be the physical g=f^2 period. Write L_r for the nonzero
height-adaptive word length and C_r for its collar charge:

    L_r=W_r+C_r,
    C_r=sum_(physical g cycles C)(2h_C-1).

This notation avoids confusing the construction length with the
handoff's separate N(k)=nu(k)+1 convention. The finite all-rank
compiler is proved in
[the height-adaptive finite-word audit](PBBS_HEIGHT_ADAPTIVE_FINITE_WORD_AND_RANGE_BOUND_INDEPENDENT_AUDIT_20260908.md).
It gives exactly

    C_r/W_r=E_state[(2h-1)/v].                         (1.1)

The physical averaging is important: every cycle contributes v
states, each with charge (2h-1)/v. It is not an average over equally
weighted cycles.

The previously proved moment and period inputs are

    E h^2<=2n,       v>=n,
    v>=np when the original top gap row is primitive.  (1.2)

The height reflection calculation and its uniform-law scope are in
[the one-row moment audit](PBBS_ONE_ROW_PERIOD_MOMENTS_AND_EXPLICIT_N_THREE_HALVES_RATE_20260908.md),
Sections 1 and 3. The original gap-row period implication nd|v, hence
the primitive case of (1.2), is proved in
[the invariant-row period audit](PBBS_INVARIANT_GAP_ROW_PERIOD_DIVISIBILITY_INDEPENDENT_AUDIT_20260908.md).
The new exact signature recursion is not needed to strengthen this
particular implication.

## 2. Exact Narayana law for the child circumference

Let K be the number of peaks of a uniform Dyck_r word. Deleting all
peaks removes K up-steps, so the child semilength is

    d=r-K,       p=2d+1.

For completeness, the Narayana enumeration follows from the ordinary
first-return Dyck decomposition. If C(z,u) counts Dyck words by
semilength z and peaks u, then

    C=1+z C (u+C-1).

With F=C-1 this is F=z(1+F)(u+F). Formal Lagrange inversion gives,
for 1<=k<=r,

    [z^r u^k]F
      =(1/r)[t^(r-1)u^k](1+t)^r(u+t)^r
      =(1/r)binom(r,k)binom(r,k-1).

Replacing k by r-j and normalizing by Cat_r proves

    Pr(d=j)=binom(r,j)binom(r,j+1)/(r Cat_r),
    0<=j<=r-1.                                        (2.1)

In particular Pr(d=0)=1/Cat_r. The resulting one-slot row p=1 is
always primitive, including a constant row. This endpoint is kept
in the reciprocal moment and excluded correctly from the bad-row
generating function below.

## 3. The rational majorant, including the exceptional endpoint

For integer j>=1 the proposed inequality is

    1/(2j+1)^2
      <=1/[4(j+1)(j+2)]
          +5/[3(j+1)(j+2)(j+3)].                       (3.1)

Subtracting the left side from the right side gives EXACTLY

    (j-1)(56j+43)
      /[12(j+1)(j+2)(j+3)(2j+1)^2].                   (3.2)

Every denominator is positive. Thus (3.1) holds for j>=1, with
equality at j=1. At j=0 the right side is 29/72, so the precise
missing amount is 43/72. Consequently the all-j inequality is

    1/(2j+1)^2
      <=1/[4(j+1)(j+2)]
        +5/[3(j+1)(j+2)(j+3)]
        +(43/72) 1_{j=0}.                              (3.3)

This is why the correction term is 43/(72 Cat_r), not an unspecified
small-error term or a correction that requires d to grow.

## 4. Both Vandermonde calculations, with their exact missing terms

Define

    A_r=E[1/((d+1)(d+2))],
    B_r=E[1/((d+1)(d+2)(d+3))].

From (2.1) and

    binom(r,j)/((j+1)(j+2))
      =binom(r+2,j+2)/((r+1)(r+2)),

Vandermonde gives

    A_r=[binom(2r+2,r+1)-(r+2)]
          /[r(r+1)(r+2)Cat_r].                         (4.1)

Indeed, put ell=j+2 in the convolution
sum_ell binom(r+2,ell)binom(r,r+1-ell). The original j-range
0,...,r-1 omits exactly the nonzero ell=1 term, equal to r+2;
the other omitted boundary terms vanish. This verifies the
subtraction in the submitted exact formula.

The exact central-binomial ratio is

    binom(2r+2,r+1)/Cat_r=2(2r+1)<4(r+1).

Dropping the negative term in (4.1) therefore proves

    A_r<=4/[r(r+2)].                                   (4.2)

For the second moment use instead

    binom(r,j)/((j+1)(j+2)(j+3))
      =binom(r+3,j+3)/((r+1)(r+2)(r+3)).

The same convolution with ell=j+3 now yields the useful exact
identity

    B_r=[binom(2r+3,r+2)-binom(r+3,2)]
          /[r(r+1)(r+2)(r+3)Cat_r].                    (4.3)

The sole omitted nonzero boundary term is ell=2, equal to
binom(r+3,2). The relevant ratio is

    binom(2r+3,r+2)/Cat_r
      =2(2r+3)(2r+1)/(r+2)<8(r+1),

because

    8(r+1)(r+2)-2(2r+3)(2r+1)=8r+10>0.

Dropping the negative term in (4.3) gives the second claimed bound

    B_r<=8/[r(r+2)(r+3)].                              (4.4)

All identities and inequalities above hold for r>=1, including
r=1. No truncation of the Narayana law has been made.

## 5. The resulting reciprocal-particle bound J_r

Take expectation of (3.3) under (2.1) and insert (4.2), (4.4):

    E p^(-2)
      <=(1/4)A_r+(5/3)B_r+43/(72 Cat_r)
      <=1/[r(r+2)]+40/[3r(r+2)(r+3)]+43/(72 Cat_r)
      =:J_r.                                          (5.1)

Combining the first two fractions gives exactly

    J_r=(3r+49)/[3r(r+2)(r+3)]+43/(72 Cat_r).           (5.2)

This moment is under the full uniform root/state law. It is not
conditioned on the top row being primitive. That is legitimate and
useful in the Cauchy–Schwarz bound: discarding the primitive-event
indicator only enlarges the nonnegative quantity being bounded.

## 6. Full bad-row probability and the Cauchy–Schwarz envelope

The original rooted inverse-pruning fibre, including its ordered
incoming-gap coordinates, is proved in Sections 1–2 of
[the genealogy structural audit](</Users/amir.nuriyev/.codex/worktrees/c69c/problem/research_round1/pbbs_gaussian_clock_genealogy_structural_audit.md>).
For a fixed child Dyck word of semilength d and k peaks, its parent
row has p=2d+1 slots, mass ell, and parent semilength

    r=d+k+ell.

There is exactly one parent root per admissible ordered row. These
are not necklaces and there is no division by p. This is the precise
fibre needed in the following bad-row count, and it is the same
original law used in (2.1).

Let b_r count roots with a nonprimitive top row. Necessarily d>=1.
For a repetition factor e>1 dividing odd p, one has e>=3, and its
row-mass generating function is (1-x^e)^(-p/e). For 0<x<1 this is
at most (1-x^3)^(-p/3). Union-bounding at most p possible factors
overcounts nonprimitive rows in the correct direction.

The child's peak enumerator obeys

    N_d(x)=(1/d)sum_k binom(d,k)binom(d,k-1)x^k
            <=sqrt(x)/d * (1+sqrt(x))^(2d).             (6.1)

To see this, put y=sqrt(x). Each summand is y/d times
binom(d,k)y^k binom(d,k-1)y^(k-1); summing these nonnegative
products is at most the product of the full two binomial sums.

Take x=9/25 and A=51/50. Exact rational arithmetic gives

    A^3(1-x^3)=1975969296/1953125000>1,
    B=A^2 x(1+sqrt(x))^2=374544/390625<1.

Thus the row generating function is at most A^p and

    sum_r b_r x^r
      <=sum_(d>=1) x^d N_d(x)(2d+1)A^(2d+1)
      <=3 sqrt(x) A B/(1-B)
      =85957848/2010125<43.                             (6.2)

The last strict comparison has positive integer margin 477527.
The convergent positive geometric majorant justifies the summation;
nonnegative coefficients give b_r<=43(25/9)^r for every r.
This full argument was independently checked in
[the signature and generating-function audit](PBBS_EXACT_SYMMETRY_SIGNATURE_RECURSION_AND_NONPRIMITIVE_TOP_GF_AUDIT_20260908.md),
Sections 5–6, which this audit read.

The elementary Catalan estimate

    Cat_r>=4^r/[2(r+1)sqrt(r)]                          (6.3)

holds for all r>=1. One direct proof starts from
c_1=binom(2,1)/4=1/2 and uses
c_(r+1)/c_r=(2r+1)/(2r+2); the inequality
(2r+1)^2>4r(r+1) inductively preserves c_r>=1/(2sqrt(r)).
Combining (6.2)–(6.3) gives

    Pr(bad top row)<=86(r+1)sqrt(r)(25/36)^r.           (6.4)

There is no physical-state factor n here, because every root has
exactly n rotations and the event is invariant under rotation.

On the primitive event G, (1.2) bounds the state collar by 2h/(np).
Everywhere, h<=r and v>=2r+1 imply (2h-1)/v<1. Hence (1.1) gives

    C_r/W_r
      <=(2/n)E[h/p;G]+Pr(G^c)
      <=(2/n)sqrt(E h^2 * E p^(-2))+Pr(G^c)
      <=2sqrt(2J_r/(2r+1))
            +86(r+1)sqrt(r)(25/36)^r
      =:E_r.                                          (6.5)

No independence of h and p is used: this is unconditional
Cauchy–Schwarz. No conditioning on a dynamically reached state,
incidence measure, or primitive row is substituted into the moments.
The bound is valid for every r>=1 even when its bad-event majorant
exceeds one in a small dimension.

## 7. Strict monotonicity from r=4

In the decomposition (5.1), both rational summands decrease strictly
with r. Catalan numbers increase for r>=1 because

    Cat_(r+1)/Cat_r=2(2r+1)/(r+2)>1.

Thus J_r decreases strictly for r>=1, and so does
2sqrt(2J_r/(2r+1)).

For the second term Q_r=86(r+1)sqrt(r)(25/36)^r, the exact squared
successive ratio is

    (Q_(r+1)/Q_r)^2
      =(25/36)^2 (r+2)^2/[r(r+1)].                     (7.1)

For r>=4,

    (r+2)^2/[r(r+1)]<=9/5,

since 9r(r+1)-5(r+2)^2=(r-4)(4r+5)>=0. Therefore

    (Q_(r+1)/Q_r)^2<=125/144<1.                        (7.2)

Both terms of E_r decrease strictly for all r>=4. This proves
the stated finite-to-infinite monotonicity; it makes no assertion
that the exact construction ratios C_r/W_r themselves are monotone.

## 8. Certified thresholds and the exact parity bridge

The separately executed and fully read
[numeric certificate](SYMMETRY_DESCENT_UNIFORM_THRESHOLD_EXACT_NUMERIC_CERTIFICATE_20260908.md)
uses outward rational square-root enclosures and proves

    E_45   <0.009272   <1/100,
    E_163  <0.000992   <1/1000,
    E_741  <0.00009987 <1/10000,
    E_3424 <0.000009999<1/100000.

It also checks all 31 cases r=14,...,44 in the already verified exact
construction census, with that census's hash pinned. Each satisfies
125 C_r<W_r. The unique largest ratio is at r=16 (dimension 33):

    C_16/W_16=4479616/583401555<1/125<1/100.

This finite band covers odd dimensions 29 through 89. Equation (6.5),
the first numerical enclosure, and monotonicity cover every odd
dimension from 91 onward. The other three enclosures start at odd
dimensions 327, 1483, and 6849. No finite-census monotonicity is used.

For clarity, the exact even lift is literal. Given a complete nonzero
word A_1,...,A_m on the odd-dimensional ground set, emit

    A_1,...,A_m,{z},A_1 union {z},...,A_(m-1) union {z}.

Its length is 2m. Old witnesses remain. A target with z uses its
lifted witness if the old witness ends before m, or its old suffix
followed by {z} if the witness ends at m. The singleton {z} is the
bridge itself. Since W(2r+2)=2W_r, the normalized odd-dimensional
bound therefore holds unchanged in the next even dimension. This
supplies every integer in each of the four headline ranges.

The numeric audit's single h100 run, finite-band comparisons, and
certificate hashes are its own execution record. This proof did not
rerun its arithmetic or the underlying partition census. The exact
symmetry recursion and census validation are separate retained proof
inputs, not assumed consequences of the envelope calculation.

## 9. Scope and absence of defects

No algebraic, averaging, conditioning, or parity defect was found in
the submitted envelope. The endpoint d=0, the missing Vandermonde
boundary terms, the ordered-row normalization, and the bad-event
contribution are all accounted for explicitly above.

The thresholds are sufficient uniform ranges for a proved finite
construction. They are not claimed to be the first dimensions where
the unknown optimum satisfies each ratio. These estimates do not
by themselves determine an exact optimal word at any fixed k.
