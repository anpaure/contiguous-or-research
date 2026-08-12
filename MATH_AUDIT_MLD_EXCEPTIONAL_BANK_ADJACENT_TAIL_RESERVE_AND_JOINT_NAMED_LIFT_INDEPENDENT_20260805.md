# Independent audit: MLD exceptional-bank adjacent-tail absorber

**Date:** 2026-08-05  
**Method:** independent symbolic audit; pure mathematics; no computation,
search, or solver  
**Audited source:**
`MATH_THEOREM_MLD_EXCEPTIONAL_BANK_ADJACENT_TAIL_RESERVE_AND_JOINT_NAMED_LIFT_20260805.md`

## 1. Verdict

**PASS, with the stated scope.**  The proof closes the exceptional whole-job
bank at the level of the lower Boolean path/collar system:

* the next-depth tail differences are exact occurrence counts;
* at most `D` whole exceptions need at most
  `D ceil(L_max/D)` maximum-socket occurrences;
* the ordinary and exceptional capacity marks can be declared before path
  realization, so the MLD quantifier is respected;
* ordinary and exceptional named tops can be included in one pointwise
  codegree matching, so there is no hidden contraction-of-start-matroid
  premise.

The source correctly does **not** claim a resident upper-complete word.  The
remaining protected serialization problem is genuine.

## 2. Tail arithmetic

With `b=t-1`,

\[
 K_q^+=W-C_{b+q-1}=W-C_{t+q-2},
 \qquad
 K_q=W-C_{t+q-1}.
\]

Therefore

\[
 K_q^+-K_q=C_{t+q-1}-C_{t+q-2}=H_{t+q-1}
\]

for every `1<=q<=D`.  Also

\[
 K_{D+1}^+=W-C_{r-1}=H_r.
\]

Deleting `h` exact maximum occurrences lowers every capacity tail by `h`.
Deleting `Delta_g` exact capacity-`g` occurrences lowers tail `q` by
`sum_(g>=q)Delta_g`.  Thus the inequalities in Theorem 2.1 are exactly the
conjugate-tail conditions for the ordinary piece multiset after those
deletions.  Sorted matching supplies an injection into distinct actual
occurrences; it is not merely a total-capacity argument.

The actual exceptional-piece count is

\[
 p\le\sum_{J\in\mathcal E}\lceil |J|/D\rceil
 \le D\lceil L_{\max}/D\rceil=h.
\]

Every such piece has length at most `D`, so every deleted capacity-`D+1`
occurrence is eligible.

## 3. Eventual reserve size

If `L_max<=t=r-D`, then

\[
 h\le D\lceil t/D\rceil<r.
\]

If `D` divides `t`, the left side is at most `t<r`; otherwise
`D ceil(t/D)<t+D=r`.  This handles the ceiling exactly.

For `s=r-j` with `0<=j<=D=O(sqrt r)`,

\[
 H_s={2j+1\over r+j+1}{2r\choose r-j}.
\]

The ratio `binom(2r,r-j)/binom(2r,r)` stays bounded below by a positive
constant depending only on the fixed `O(sqrt r)` bound.  Hence uniformly in
the collar,

\[
 H_s\ge cW/r.
\]

This is exponential and dominates `h=O(r)`.  The existing spread-reserve
calculation gives

\[
 \sum_{g\ge q}\Delta_g=o(H_{t+q-1}),
 \qquad \Delta_{D+1}=o(H_r),
\]

so adding `h` does not invalidate any tail inequality.

## 4. MLD quantifier audit

The potentially invalid operation would be:

1. realize the random Boolean paths;
2. inspect their named geometry;
3. change socket types adaptively.

The source does not do this.  It runs sorted-tail assignment on the
deterministic multiset of job/configuration/piece tokens.  This produces
integer counts of complete capacity-mark vectors inside each deterministic
birth/configuration class.  Uniform fixed-count refinement at birth is
exactly an allowed MLD operation.

The exception counts `e_b` are themselves deterministic cohort cells from
the extreme-point rounding.  Canonical consecutive fragmentation of a
length-`L_b` exceptional path and the declaration of the maximum mark are
therefore also fixed birth data.  At every later rank, each top family is a
union of complete labels.  The MLD one-rank Laplace bound applies to the
exceptional tops just as it does to the ordinary tops.

## 5. Joint named matching audit

For every tagged start rank `u`, let `m_u` include both ordinary and
exceptional requests.  The reserve construction gives

\[
 m_u\le H_u-\Delta_{u-b}.
\]

All request tops are target-disjoint because the Boolean paths are disjoint
and every path is cut into consecutive pieces.  For each rank `s`, their
marked family has the binomial Laplace benchmark.  Generalized Holder is
valid without independence across ranks.  The MLD weighted-Bernstein theorem
therefore yields the simultaneous pointwise inequalities

\[
 \sum_{F:S_F\subset T}
 {1\over{2r-|S_F|\choose u-|S_F|}}
 \le {H_u\over C_u}
\]

under the displayed reserve condition.  The pointwise-codegree theorem
then supplies one augmented integral matching containing both continuation
edges and all request edges.  Its request images are a jointly independent
family of actual collar starts.

This is important: selecting exceptional starts first and then invoking the
unmodified ordinary concentration theorem would leave an unproved
contracted-matroid step.  The joint matching avoids it.

The source's frozen-exception fallback is also sound.  If all exceptional
tops have rank at most `b-1` and are assigned to rank `r`, each normalized
load is at most

\[
 d_*^{-1},\qquad
 d_*={2r-b+1\choose r-b+1},
\]

so the total adverse load is at most `h/d_*`.  The spread reserve dominates
this eventually.

## 6. Scope and remaining obstruction

The proved occurrence is an actual collar-chain occurrence in a named
Boolean chainization.  This certifies:

* exact capacity;
* distinctness;
* named containment;
* compatibility with all lower target-once fragments.

It does not yet certify that the same occurrence is a literal interval cell
of one rank-middle source word.  No current implication turns an arbitrary
MLD collar forest into a chronology simultaneously having:

* all central owners once;
* coordinate residence at the required depth;
* every arbitrary-width upper witness;
* the protected endpoint/topology state.

Accordingly the theorem removes the exceptional-bank capacity and naming
gate, but it leaves the exact **protected carrier serialization** gate.  No
claim about `nu(k)=B(k)+O(1)` follows without that additional theorem.

## 7. Dependency audit

The proof uses only:

1. extreme-point whole-job rounding with at most `D` exceptional jobs;
2. the conjugate-tail matching criterion;
3. uniform fixed-count MLD refinement at birth;
4. the MLD--Holder weighted concentration theorem;
5. the pointwise-codegree augmented matching theorem;
6. the already-proved adjacent-tail and spread-reserve estimates.

No total-unimodularity claim, independent-rank assumption, random-SCD
uniformity assertion, or solver evidence is used.
