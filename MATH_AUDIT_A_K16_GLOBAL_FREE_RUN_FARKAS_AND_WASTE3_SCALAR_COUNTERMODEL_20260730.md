# Audit of the K16 global free-run Farkas theorem

Date: 2026-07-30  
Status: PASS after scope corrections  
Audited file: `THREAD_A_K16_GLOBAL_FREE_RUN_FARKAS_AND_WASTE3_SCALAR_COUNTERMODEL_20260730.md`

## 1. Verdict

Every unconditional theorem in the audited note is valid for an arbitrary
universal K16 word of length `12873`.  The constants in the coordinate,
pair, run and variation inequalities recompute exactly.

The two countermodels concern different relaxations:

* Section 8.2 satisfies the inventory, atom, aggregate pair-Farkas and
  numerical phase-run rows, but has no common ordering;
* Section 8.3 satisfies every pointwise free-set cardinality cut and static
  target containment, but assigns no common run/deadline chronology.

Accordingly neither is a physical word, and the note correctly leaves open
the intersection of all pointwise subset cuts with a common-order run
system.  No claim of `nu(16)>=12874` or of a physical waste-three word is
made.

## 2. Deadline and filtering checks

For a lower-prefix block `[p,p+f_p-1]`, every delivery group whose deadline
lies in the block must have a representative start before `p`; otherwise a
rank-eight delivery interval lies inside a rank-below-eight interval.  There
are at most `p` such groups, and the remaining deadlines occupy at most
`L-p-f_p` sites.  Hence

\[
                         f_p\le L-(W+G).
\]

Summing the shortened final columns gives

\[
 \Lambda\le dL-\binom d2,\qquad d=3-G.
\]

At `G=1` this is `25745<26332`; thus `G=0` and `N+F=3`.

For any coordinate set `X`, a witness avoiding `X` lies wholly in one
maximal `X`-free run.  Concatenating the runs therefore proves exactly

\[
 c_X\ge\nu(16-|X|).
\]

No run-count or residence statement transfers across the virtual seams.

## 3. Extra-incidence and atom checks

With `G=0`, flat extras give

\[
 E\in F\Delta(16,8)\cap\mathbb Z^{16}.
\]

The integer decomposition criterion is complete: for every `s<=F`,

\[
 \sum_x\min(E_x,s)\ge(s/F)\sum_xE_x=8s,
\]

so the bipartite degree flow is integral.  The corrected equations are

\[
 \ell_x+E_x=3+a_x,qquad
 \Delta=24+\sum_xa_x,qquad
 \sum_x\ell_x=\Delta+8N.
\]

The atom identity separates one primary occurrence per middle target and is
coordinatewise exact.  Sixteen forced singleton sites charge `16*7=112`,
and every flat contributes a further eight, proving

\[
 \sum_xa_x\ge64+8F.
\]

Equality would leave at least `16-F>=13` modified middle targets whose only
available contained letters are their eight singleton sites.  Sixteen
ordered singleton sites have at most nine consecutive eight-site blocks.
Thus physical equality is impossible and

\[
                         \sum_xa_x\ge65+8F.
\]

This is phase slack, not an additional first-delivery waste unit.

## 4. Pair Farkas audit

Summing pair-free counts gives

\[
 \sum_p\binom{16-|A_p|}{2}\ge120\cdot3434=412080.
\]

For a delivery, with `d=16-|A_p|` in `[8,15]`,

\[
 \binom d2\le11d-60;
\]

for a nondelivery, `binom(d,2)<=11d`.  Therefore

\[
                         11\Delta+60N\ge51636.
\]

The four exact ceiling bounds are

\[
 \Delta\ge4695,4689,4684,4678
\]

for `N=0,1,2,3`, respectively.  Subtracting `24` gives the displayed
`4671,4665,4660,4654` bounds for `sum a_x`.  The consequent non-immediate
delivery counts `671,669,668,666` also check.

## 5. Run-window audit

For one free-run length `lambda`, the counts of intervals of lengths at most
three and four are the positive-part sums.  Summing over runs gives exactly

\[
 H_3=3c-3t+s_1,qquad H_4=4c-6t+3s_1+s_2.
\]

These formulas already include both linear boundaries.  Lower witnesses,
middle deliveries and overshooting crossings are distinct intervals by OR
rank and start, so there is no disjointness assumption.  The audited
constants are therefore

\[
 3t_x-s_{x,1}\le2931+3a_x,
\]

\[
 6t_x-3s_{x,1}-s_{x,2}+E_x+j_x\le2934+4a_x.
\]

An unresolved suffix contributes at most three endpoints in one free run,
while a global jump of rank at least nine is free in at most seven
coordinates.  Hence

\[
 3T\ge\Delta+8S+J.
\]

Combining with the pair cut gives `T>=1561`; reversal gives the checked
adjacent Hamming-variation bound `3092`.  The pointwise pair-run lower bounds
`143` on the `N=0,1` faces and `142` on the `N=2,3` faces also follow.

## 6. Countermodel scope

The Section 8.2 values

\[
 \Delta=4680,\quad \delta=4656,\quad
 c_x=6729,\quad\ell_x=294,\quad t_x=98
\]

satisfy every numerical row claimed there; the pair moment is `412104`.
The run variables are not produced by one ordering.

The Section 8.3 symmetric rational point has

\[
 \theta=112/2145,qquad
 c_h=42(16-h)+(2033/2145)\binom{16-h}{8},
\]

and satisfies every pointwise subset-free length cut.  It assigns no common
first-middle intervals or run trace.  Thus the two examples prove only the
two stated relaxation-feasibility results.  A coupled higher-order
coordinate/common-run Farkas inequality remains possible, and the exact
three-hole staircase/common-envelope gate of handoff item 1998a remains the
physical frontier.

The exact bracket is unchanged:

\[
                         12873\le\nu(16)\le12874.
\]
