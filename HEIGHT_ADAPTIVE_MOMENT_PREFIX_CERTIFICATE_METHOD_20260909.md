# Height-weighted pruning prefixes: reviewed method and verified first pair

2026-09-09. The new height-total and integrated-period arguments pass
independent internal proof review. A standalone implementation, followed
by a complete replay, independently certifies

\[
 \nu(137)<1.00001W(137),\qquad \nu(138)<1.00001W(138).
\]

The user's stronger **uniform** claim for every integer \(k\ge137\)
is recorded separately. The attached proof and verification log do not
contain the 3,356 finite-case transcripts, their programs, or the
predecessor lower certificate. Those calculations have not been
independently replayed here. The verified first pair does not establish
the rest of that band or the minimality of the proposed threshold.

All construction-length conclusions retain the finite height-adaptive
construction, matching-corridor, particle-reduction and pruning-fibre
premises. Internal proof/code audits and finite checks are not external
or formal certification. No enormous universal word was materialized.

## 1. Exact height totals replace a uniform height cap

For \(a\ge1\) and \(0\le b<a\), put

\[
 K(a,b)=\frac1a\binom ab\binom a{b+1},\qquad
 H(a,b)=\sum_{|D|=a,\,|\partial D|=b}h(D).
\]

The exact inverse-pruning fibre and the one-unit height decrease give

\[
 H(a,0)=1,\qquad
 H(a,b)=K(a,b)+\sum_{c=\max(0,2b-a)}^{b-1}
                 \binom{a+c}{2b}H(b,c)\quad(b>0).
\]

At depth \(s\), with upper-row multiplicity \(w\) and a period divisor
\(P\) shared by every completion, the entire family's root-weight charge
is at most

\[
 \frac{w\bigl((2s-1)K(a,b)+2H(a,b)\bigr)}P.
\]

This follows by first using \(1/v\le1/P\) for each completion and then
summing its height. It makes no independence assumption. The old charge
replaced \(H(a,b)\) by \((b+1)K(a,b)\). The new bound is therefore at
least as strong. At \(s=0\), the coefficient of \(K\) is negative, but
\(K\) remains exact and \(H\ge K\) makes the full numerator positive.

The independent height table confirms

\[
 16.428245020843044252579122292728
 \le\frac{H(100,50)}{K(100,50)}
 <16.428245020843044252579122292729.
\]

The prior class cap was 51. For larger cores, the submitted reflection
bound also passes review: sum the positive height tail over all rotations
and divide by \(2a+1\), then bound each binomial tail geometrically.
Its implementation must handle \(t\ge a\) before evaluating an
out-of-range binomial index. The first-pair computation uses exact height
totals throughout and does not need that approximation.

## 2. Integrate one further period row, retaining symmetric classes

At sizes \(a,b\), the forward recurrence gives

\[
 p=2b+1,\quad \beta'=\frac{1+p\beta}{2a+1},\quad
 P_d=\operatorname{lcm}(P,\operatorname{den}(\beta'/d)).
\]

Let \(A_d\) be the exact original-height weight of completions whose
current ordered gap row has least period \(d\). Since \(d\mid p\),
\(P\mid P_d\mid P_p\), and hence

\[
 \sum_{d\mid p}\frac{A_d}{P_d}
 =\frac{\sum_d A_d}{P_p}
   +\sum_{d<p}A_d\left(\frac1{P_d}-\frac1{P_p}\right).
\]

Every correction is nonnegative. Exact ordered-composition counts
evaluate the corrections without treating a symmetric row as primitive.
The submitted coarse correction for large cores is also valid when used
with its proved upper count and height cap.

At terminal \(b=0\), include the last one-slot-row denominator before
calling the period exact. For sparse expansion, every omitted next-size
family remains in an explicit reserve with its exact mass and the parent
height/period charge. Mass conservation must come from replaying disjoint
parent-to-child replacements; a final total alone would not suffice.

## 3. Independently executed certificate for r=68

The sole new numerical run used exact heights through core size 100,
full next-size expansions, and exact proper-period classes. It performed
162 refinements, generated 2,571 nodes, and retained all 2,409 final
leaves, including 2,388 unfinished leaves. Maximum processed depth was
three. No sparse reserve or approximate symmetry correction was needed.

The complete replay recomputed the forward rational recurrence and row
counts without using the search priority. Its exact integers are

```text
Cat_68 = 86218923998960285726185640663701108500
U      = 860872256709126171307785011672491
Cat_68 - 100000 U
       = 131698328047668595407139496452008500 > 0
```

Thus the relative construction excess is less than
\(0.000009984725125072396316850761\). The integer bound is

```text
W(137) = 11811992587857559144487432770927051864500
nu(137) <= 11812110527356728294772901937473650995767
```

The run additionally checked all 23,713 nonempty Dyck roots through
semilength 10; all 125,475 middle bridges through semilength 9 and their
reflection counts; 2,575 directly enumerated ordered gap rows; and 288
small prefix states against the prior exact cycle census. It took
1.5324 wall seconds on `h100`, under predeclared 60 CPU seconds,
90 wall seconds and 1 GiB limits. Root and a separate agent read the
complete source before execution. No retry or additional dimension ran.

Full evidence:

- [Independent numerical certificate](scratch/MOMENT_PREFIX_R68_INDEPENDENT_NUMERICAL_CERTIFICATE_20260909.md).
- [Standalone generator and replay](scratch/verify_moment_prefix_structure_and_r68_20260909.py).
- [Complete report](scratch/moment_prefix_structural_and_r68_20260909/moment_prefix_complete_certificate.json).
- [All final leaves](scratch/moment_prefix_structural_and_r68_20260909/r68_frontier/final_leaves.jsonl).
- [All split records](scratch/moment_prefix_structural_and_r68_20260909/r68_frontier/splits.jsonl).
- [Height/reflection proof audit](scratch/PBBS_MOMENT_PREFIX_HEIGHT_RECURRENCE_AND_REFLECTION_SUBFAMILY_AUDIT_20260909.md).
- [Integrated-period and reserve proof audit](scratch/MOMENT_PREFIX_INTEGRATED_PERIOD_SPARSE_RESERVE_AND_THRESHOLD_INDEPENDENT_AUDIT_20260909.md).
- [Pre-execution code audit](scratch/MOMENT_PREFIX_STRUCTURE_AND_R68_CHECKER_PREEXECUTION_CODE_AUDIT_20260909.md).

Report SHA-256:
`4a72d1ed42e689b59eff6e7b80bf082e5cc7044b436731a18313834794df16d4`.

## 4. What would complete the uniform claim

The submitted band is \(68\le r\le3423\). If every actual certificate
satisfies \(100000U_r<\operatorname{Cat}_r\), the previously proved
decreasing envelope with \(E_{3424}<10^{-5}\) supplies the entire
remaining tail. The standard even lift preserves the ratio. This
finite-to-infinite logic passes review and does not assume monotonicity
of the actual constructor's excess.

The supplied log reports generation of all 3,356 cases and separate
replay of 1,016 of them. These are user-reported execution counts, not
our replay counts. The new independent run verifies only \(r=68\).
The prior independently certified uniform ten-parts-per-million
threshold remains 6,849 until the missing band is checked.

The claimed failure at dimensions 135/136 needs the actual disjoint
terminal-family lower certificate, computed with exact or downward
arithmetic. Upward prefix ceilings cannot serve that purpose. Even a
verified failure would concern this constructor and its prescribed lift,
not the unrestricted optimum \(\nu\).

The exact cases remain solved through 18. No new literal word, improved
19/20 bound, stronger eventual exponent, or all-dimensional equality
theorem is supplied by this continuation.
