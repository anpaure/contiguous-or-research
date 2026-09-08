# Moment prefixes: integrated periods, sparse reserves, and threshold logic

Date: 2026-09-09. Independent pure-proof audit by
`exact_equality_structure` of Sections5–8 of
`/Users/amir.nuriyev/Downloads/MOMENT_PREFIX_ADVANCE.md`.

**Verdict:** the integrated primitive-row charge, nonprimitive correction,
sparse-reserve bound, adjacent-ratio formula, integer upper-certificate
normalization, and construction-specific predecessor argument are valid
under the retained finite construction/fibre/period premises. Expansions
in Sections5–6 apply to nonterminal `b>0` prefixes; terminal `b=0`
must use the already established separate convention below.

No mathematical program, finite-band replay, predecessor computation,
or numerical threshold recomputation was performed for this audit.
The reported 3,356 certificates and predecessor certificate have not
been supplied here. Consequently this note does **not** independently
establish the new numerical starting dimension137.

## 1. Exact inherited interfaces and notation

The relevant finite prefix interfaces were independently audited in
[the forward-prefix audit](PBBS_FORWARD_PREFIX_PERIOD_COMPLETION_AND_UNIFORM_BAND_AUDIT_20260908.md),
Sections1–6. The exact ordered-row least-period count and the
nonprimitive top-row bound were independently proved in
[the symmetry-signature/GF audit](PBBS_EXACT_SYMMETRY_SIGNATURE_RECURSION_AND_NONPRIMITIVE_TOP_GF_AUDIT_20260908.md),
Sections4–5. Those source sections were read for this audit.

A prefix at level `s` has consecutive remaining semilengths
`a=a_s`, `b=a_(s+1)`, upper-row multiplicity `w`, and known period
divisor `P`. Its exact original-root completion mass is

    M=w K(a,b),
    K(a,b)=binom(a,b) binom(a,b+1)/a.

The multiplicity includes only original ordered row classes fixed by
the prefix. No unrecorded restrictions on the remaining root shape
or individual row entries are allowed when using this mass formula.

For `b>0`, the next size ranges over

    max(0,2b-a) <= c <= b-1,

and the row mass is `ell=a-2b+c`. Its length is `p=2b+1`.
The exact number of ordered rows of least period `d` is
`C(p,ell;d)`, with `d|p`. In particular,

    sum_(d|p) C(p,ell;d)=binom(a+c,2b),
    sum_c binom(a+c,2b) K(b,c)=K(a,b).                  (1.1)

There is no necklace division or extra factor `p` in (1.1).

For the moment argument, let `H(a,b)` be the exact sum of remaining
heights over this root class. The new height-total recurrence gives

    H(a,b)=K(a,b)+sum_c binom(a+c,2b) H(b,c),
    H(a,0)=1.                                         (1.2)

The reasoning below uses an upper substitute only through

    H(a,b) <= Hhat(a,b) <= (b+1) K(a,b).                 (1.3)

Thus the separate proof of the submitted reflection-based `Hhat` is
an explicit dependency, rather than an independence assumption.

## 2. Divisibility and signs in the integrated row-period formula

Set

    beta'=(1+(2b+1) beta_s)/(2a+1),
    P_d=lcm(P,den(beta'/d)),
    P_p=lcm(P,den(beta'/p)).

Since `d|p`, the rational `beta'/d` is the integer multiple `p/d`
of `beta'/p`. The reduced denominator of an integer multiple divides
the old reduced denominator. Therefore

    P | P_d | P_p,
    0 <= 1/P_d-1/P_p <= 1/P-1/P_p.                    (2.1)

Each `P_d` divides every completed period in its row class. It need
not equal that complete period. The integrated expression below is
therefore an upper bound on the true collar contribution, not an
assertion that the remaining periods are all determined already.

Define exactly

    M_d=sum_c C(p,a-2b+c;d) K(b,c),
    R_d=sum_c C(p,a-2b+c;d) H(b,c).

For a child of height `h_child`, the original height is
`s+1+h_child`, so its weight `2h_original-1` is
`2s+1+2h_child`. Thus its row-period class has exact height-weight total

    A_d=w[(2s+1)M_d+2R_d].                              (2.2)

Equations(1.1)–(1.2) give

    sum_d M_d=K(a,b),
    sum_d R_d=H(a,b)-K(a,b),
    sum_d A_d=w[(2s-1)K(a,b)+2H(a,b)].                  (2.3)

Now add and subtract the baseline `sum_d A_d/P_p`:

    sum_d A_d/P_d
     = w[(2s-1)K+2H]/P_p
       + w sum_(d<p) [(2s+1)M_d+2R_d]
                         (1/P_d-1/P_p).               (2.4)

This proves the submitted exact decomposition(5.3). The equality is
between two valid integrated upper charges. It pays for every proper
row period, including a zero row of least period one. It does not
discard symmetric rows or substitute a typical row period.

The exact integrated upper charge is at most the unintegrated moment
charge `w[(2s-1)K+2H]/P`, since every `P_d>=P` and `A_d>=0`.
No independence between height and period is used: the sums in(2.2)
retain their full correlation through `c` and the row counts.

## 3. The coarse nonprimitive correction is in the correct direction

The earlier finite generating-function proof establishes

    b_a <= 43(25/9)^a

for the number `b_a` of size-a rooted Dyck words with a nonprimitive
top row. Since `b_a` is an integer,

    B_a=floor(43*25^a/9^a)

is an integer upper bound. This `B_a` is the nonprimitive-root bound;
it is distinct from the manuscript's reflection-tail notation `B_a(t)`.

The current `(a,b)` class contains at most `min(K(a,b),B_a)` such
roots. Each has original height at most `s+b+1`, and (2.1) bounds its
reciprocal-period correction. The entire proper-period correction is
therefore at most

    w(2s+2b+1) min(K(a,b),B_a) (1/P-1/P_p).             (3.1)

Every factor in(3.1) is nonnegative. Substituting `Hhat` for `H` in
the baseline is also valid because its coefficient is `2w/P_p>=0`.
Although the baseline's fixed `K` coefficient is `2s-1`, which is
negative at `s=0`, it is not being bounded or changed in that
substitution. The whole baseline is nonnegative: `H>=K` gives
`(2s-1)K+2H >= (2s+1)K`.

The minimum of the old height-cap charge, the `Hhat` moment charge,
and the coarse integrated charge is again a valid upper bound.
Rounding a complete charge upward, or summing separately upward-rounded
nonnegative charge components, remains safe. Rounding need not preserve
the exact unrounded refinement monotonicity, and none is required.

## 4. Terminal prefixes must be handled separately

Sections5–6 of the submitted note use `K(b,c)` and `H(b,c)` with
`0<=c<b`. These expansions assume `b>0`. At `b=0` there is one remaining
root, `K(a,0)=H(a,0)=1`, and no `c`-split. The final row still has length
one, mass `a`, and least period `d=1`.

The exact terminal divisor is obtained only after inserting its last
denominator:

    P_final=lcm(P,den(beta')).                          (4.1)

The completed original height is `s+1`, so a terminal class has exact
root-weight sum `w(2s+1)/P_final`. This is the already established
terminal convention in the forward-prefix audit, Section4.

Keeping the old `P` would still give a valid **upper** bound, since
`P<=P_final`, but cannot generally be used as an exact contribution
to the predecessor **lower** bound. No implicit `K(0,c)` or empty
`c`-sum may replace this terminal branch. The transcript replay must
check(4.1) when declaring a leaf's period exact.

## 5. Sparse next-size expansion and the reserve

For a selected next-size `c`, summing every least-period class gives
the exact child mass

    sum_(d|p) w C(p,a-2b+c;d) K(b,c)
       =w binom(a+c,2b) K(b,c).                         (5.1)

For any chosen set `S_c` of allowed next sizes, the unexpanded
complement therefore has exact mass

    M_rem=wK(a,b)-sum_(c in S_c) w binom(a+c,2b)K(b,c). (5.2)

All these completions keep the parent period divisor `P` and height
bound `s+b+1`. Their total root-weight contribution is at most

    M_rem(2s+2b+1)/P.                                   (5.3)

This is exactly the submitted reserve. The factor `w` is already
inside `M_rem`; it must not be applied a second time. The selected
children and the reserved complement partition the parent family.
Every nonprimitive row class at a selected size must still be included;
zero-count classes may of course be omitted.

An adaptive choice of `S_c`, including stopping near the mass mode,
does not alter the proof. Frozen reserves are charged in the final
sum even though no deeper prefix data are materialized for them.
The stopping rule involving `old_integer_charge/65536` has no
mathematical role beyond its effect on efficiency.

Mass conservation alone would not prove that arbitrary recorded
families are disjoint. A valid replay must establish the initial
partition and verify each actual parent-to-children replacement,
with its reserved complement, so no missing family can be offset by
counting another family twice. The submitted description of exact
prefix families and split replay is sufficient in principle; the
unprovided implementation has not been inspected.

## 6. Adjacent weight ratio and mode selection

For `b>0` let

    q_c=binom(a+c,2b) K(b,c).

At consecutive allowed values `c,c+1`,

    binom(a+c+1,2b)/binom(a+c,2b)
       =(a+c+1)/(a+c+1-2b),

    K(b,c+1)/K(b,c)
       =(b-c)(b-c-1)/[(c+1)(c+2)].

Their product is exactly the submitted ratio(6.3). All denominators
are positive on the allowed adjacent range: the fibre lower boundary
ensures `a+c+1-2b>=1`, and `c>=0`.

The first factor is `1+2b/(a+c+1-2b)` and decreases with `c`.
The second is the product `(b-c)/(c+1)` and `(b-c-1)/(c+2)`, which
are positive and decreasing before the last allowed value. Therefore
the positive adjacent ratios decrease, and the weight sequence is
unimodal. A one-value range requires no ratio test; a tie of two
neighboring modes requires a declared deterministic tie convention
if a transcript stores only the number of expanded `c` values.

Exact multiplicative/divisive updates can compute neighboring weights
without fresh binomial evaluation. Replay must retain the rational
identities or verified exact divisibility; unjustified floor division
inside a ratio is not an acceptable substitute.

Recording only how many values were expanded is sufficient only when
the independent consumer reconstructs their exact set from the same
explicit mode and visiting-order convention. The reserve proof itself
works for every chosen set and does not depend on that convention.

## 7. Integer normalization and the claimed complete band

Write `n=2r+1`. The retained constructor's collar is exactly

    C_r=N_r-W_r=n sum_root (2h-1)/v,
    W_r=n Cat_r.                                       (7.1)

Let each current exact family or frozen reserve carry an integer
upper charge for its contribution to the root sum in(7.1), and let
their sum be `U_r`. The partition argument gives

    C_r <= n U_r.

Hence the strict integer comparison

    100000 U_r < Cat_r                                  (7.2)

implies `C_r/W_r<1/100000`. The factor `n` cancels exactly. The
submission's normalization(7.1)–(7.2) is correct; no missing physical
rotation or cycle-count normalizer occurs.

The inclusive range `68<=r<=3423` contains 3,356 cases. To obtain
the claimed uniform starting dimension, each case must have an actual
certificate satisfying(7.2), with its masses, upgrades, sparse splits,
reserves and final sum checked. A reported total case count or search
summary does not establish any individual margin or completeness of
the range. Those transcripts and programs are not attached to the
material audited here.

## 8. Analytic tail and the even lift

The submitted envelope `E_r` is the previously audited one. Each
positive summand of `J_r` decreases. For its other term
`T_r=86(r+1)sqrt(r)(25/36)^r`,

    (T_(r+1)/T_r)^2
     =(625/1296)*(r+2)^2/[r(r+1)] <=125/144<1

for `r>=4`, exactly because

    9r(r+1)-5(r+2)^2=(r-4)(4r+5)>=0.

Thus the monotonicity argument passes. The previous independently
executed
[numeric envelope certificate](SYMMETRY_DESCENT_UNIFORM_THRESHOLD_EXACT_NUMERIC_CERTIFICATE_20260908.md)
already proves `E_3424<0.000009999<0.00001`; this weaker enclosure
is enough for every `r>=3424`. The newly quoted tighter rational
in the attachment was not recomputed in this audit and is unnecessary
for the logical tail argument.

If the full finite band(7.2) is verified, it and this analytic tail
cover every odd dimension from137. The specified trimmed lift has
exact length `2N_r` and width `W(2r+2)=2W_r`, preserving the strict
relative excess. Its suffix-through-the-singleton treatment of a
marked old witness ending at the final old letter is correct.
Consequently the **conditional** all-integer conclusion from137
follows without assuming monotonicity of the actual constructor ratio.

The additional inequality `0<=nu(k)-B(k)<10^(-5)W(k)` then follows
from `W(k)<=B(k)<=nu(k)`; it is not an exact-attainment assertion.

## 9. Predecessor certificate: valid direction, missing actual evidence

A terminal family has known exact height `h`, known exact period
`v`, and root mass `w` after all row constraints, including(4.1),
are included. Its contribution to the constructor collar is exactly

    n*w*(2h-1)/v.

Any disjoint collection of such terminal families gives a collar
lower bound by summation, because every omitted root has a
nonnegative contribution. Thus, at `r=67`, an exact sum `C_low`
satisfying

    100000 C_low >135 Cat_67

would prove that this specific constructor fails the tolerance at135.
Its specified doubled word would fail at136 by the unchanged relative
excess. Together with the verified all-dimension upper result from137,
this would prove minimality of137 for that constructor/lift pair.
It would not be a lower bound on the best possible words at135 or136.

For this lower certificate, use exact rational arithmetic or a
downward-rounded lower sum. The upward ceilings appropriate for
Section7 upper charges cannot be reused as lower contributions.
Terminal families must be disjoint, and an unfinished period divisor
cannot stand in for the exact `v`. These are necessary replay checks,
not observed errors in code that has not been supplied.

The actual predecessor transcript and margin are missing from the
audited attachment. Its asserted failure and the constructor-specific
minimality of137 therefore remain conditional here.

## 10. Final status and remaining evidence

The mathematical mechanism of Sections5–8 passes with the inherited
finite hypotheses and the explicit terminal convention. Its gains are
upper-bound refinements for an unchanged constructor, independent of
the exact17/18 literal constructions and independent of asymptotic
clock/sieve estimates.

Still needed to promote the new finite threshold:

* Actual `verify_moment_prefix.py` and `audit_moment_prefix.py` sources.
* The complete finite-band transcripts and positive margins for all
  3,356 cases, including all frozen reserve charges.
* The disjoint completed-family predecessor certificate and its
  exact lower comparison.

The summary's structural enumeration counts and replay counts were
not reproduced by this note. The all-dimension exact goal
`nu(k)=B(k)` remains separate and is not completed by these bounds.
