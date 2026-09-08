# Exact status for every \(K<20\)

> Revalidated finite frontier and direct 2026-07-25 verifier commands:
> `CURRENT_EXACT_K_LT20_FRONTIER_20260725.md`.

The project uses \(\nu(K)\) for the minimum length of a word whose nonempty
contiguous ORs cover the nonzero masks.  The literal all-mask answer is
\[
N(K)=\nu(K)+1,
\]
because one zero entry is necessary and sufficient to realize mask \(0\).

The common rigorous lower bounds are the evaluated rank-count bounds in
MATHEMATICAL_HANDOFF.md.  Every upper endpoint below is either a directly
verified witness or a deterministic consequence of the proved trimmed
one-bit lift.

| \(K\) | rigorous \(\nu(K)\) | literal \(N(K)\) | evidence |
|---:|---:|---:|---|
| 1 | **1** | **2** | handoff §9; construct_or_array.cpp |
| 2 | **2** | **3** | same |
| 3 | **4** | **5** | same |
| 4 | **7** | **8** | same |
| 5 | **12** | **13** | same |
| 6 | **21** | **22** | same |
| 7 | **37** | **38** | k7_length37.analysis |
| 8 | **72** | **73** | k8_optimal.txt, k8_length72.analysis |
| 9 | **128** | **129** | k9_optimal.txt, k9_length128.analysis |
| 10 | **254** | **255** | k10_optimal_nonzero.txt, k10_optimal_verification.txt |
| 11 | **[465,477]** | **[466,478]** | lower rank count; k11_completed_477.txt and exhaustive/suffix logs |
| 12 | **926** | **927** | k12_optimal_nonzero.txt, k12_optimal_verification.txt |
| 13 | **[1719,1852]** | **[1720,1853]** | lower rank count; proved lift of \(K=12\) |
| 14 | **[3434,3676]** | **[3435,3677]** | lower rank count; k14_completed_3676.txt and exhaustive/suffix logs |
| 15 | **[6438,7352]** | **[6439,7353]** | lower rank count; proved lift of \(K=14\) |
| 16 | **[12873,14704]** | **[12874,14705]** | same |
| 17 | **[24313,29408]** | **[24314,29409]** | same |
| 18 | **[48623,58816]** | **[48624,58817]** | same |
| 19 | **[92381,117632]** | **[92382,117633]** | same |

Thus the exact values are proved for
\[
K\in\{1,2,\ldots,10,12\},
\]
and the irreducible unresolved set is
\[
\boxed{\{11,13,14,15,16,17,18,19\}}.
\]

Their current gap widths for \(\nu(K)\) are respectively
\[
12,\ 133,\ 242,\ 914,\ 1831,\ 5095,\ 10193,\ 25251.
\]

## New theorem-level structural information (no endpoint change)

The 30-lane mathematical attack did not change any numerical interval in
the table, but two independently audited finite theorems now constrain any
future equality or near-equality witness.

First, the nonsaturated endpoint-fork theorem applies to a word of odd
dimension \(2m+1\) and length \(M+d\), with
\(M=\binom{2m+1}{m}\).  A fixed choice of witnesses for the two middle
ranks yields at least \(M-3d\) common two-sided endpoints and, under the
recorded rank cap, all but at most \(4d-h\) low positions are double-fork
junctions.  The forks form a directed linear forest.  Coordinate-restricted
versions of the same fixed forest, a width-two/three exclusion law, and
rainbow Johnson-run consequences are all exact.

For the unresolved finite cases this gives, among other consequences:

- at \(K=11\), at least \(319+h\) double forks, including at least
  \(44+h\) of entry rank at most two and \(154+h\) of entry rank at most
  three; at least \(199+h\) relevant bases omit each prescribed coordinate;
- at \(K=14\), at least \(1136\) rank-5/6/7 double-diamond bases, with at
  least \(421\) bases omitting each coordinate;
- at \(K=15,17,19\), respectively at least \(125,2634,16778\) full
  four-rank flags;
- at \(K=17,19\), the homogeneous-run ledger forces at least
  \(2285+3h\) and \(26955+3h\) Johnson edges.

Second, the rank-sensitive lift-slack theorem shows that an appended repair
of length \(r\) must pay exact many-run losses at each newly lifted rank;
in particular the hard even-to-odd minimum repair counts inherited from
old dimensions \(12,14,16,18\) are \(5,9,17,31\).  These are necessary
conditions and do not yet improve a displayed upper or lower endpoint.

The audited sources are
`NONSATURATED_ENDPOINT_FORK_STABILITY.md`,
`NONSATURATED_ENDPOINT_FORK_STABILITY_AUDIT.md`,
`FINITE_LIFT_SLACK_THEOREMS_20260724.md`, and
`FINITE_LIFT_SLACK_THEOREMS_AUDIT_20260724.md`.

Third, a solver-free analysis now classifies the strongest nonsaturated
zero-margin \(K=11\) equality slices as necessary cell templates.  It
eliminates zero margin at \(n_5=134\), gives the exact double filtration at
\(n_5=133\), and reduces \(n_5=132\) to five coarse modes.  Every surviving
central four-window is a distinct rank-six witness.  A second audited
theorem turns the central witnesses into a one-jump Johnson flag path and,
after fixing witness families, an endpoint-ordered perfect inclusion
matching between all rank-five and rank-six sets.  This induces a spanning
rainbow forest in \(J(11,5)\) with at most six components and at least 456
distinct upper colors, equivalently an alternating path cover of all 924
middle-level vertices by at most six paths.  Exact coordinate extension
counts are 42 per coordinate.

These are necessary conditions only; no contradiction or length-465 word
is obtained.  Therefore the numerical interval \([465,477]\) is unchanged.
The audited sources are
`K11_NONSATURATED_ONE_DEFECT_CORE_20260724.md`,
`K11_NONSATURATED_ONE_DEFECT_CORE_FINAL_AUDIT_20260724.md`,
`K11_ZERO_MARGIN_WINDOW_ATTACK_20260724.md`, and
`K11_ZERO_MARGIN_WINDOW_ATTACK_AUDIT_20260724.md`.

Two further audited proof-only refinements preserve the same interval.  The
subset-flow hierarchy fixes all perfect-matching completion totals

\[
(\Delta_1,\ldots,\Delta_6)=(42,42,28,14,5,1)
\]

and determines the central/external extension split exactly by

\[
e_x^{\rm cen}=R_x^{(3)}-1+\mathbf1_{x\in H},
\qquad
e_x^{\rm ext}=43-R_x^{(3)}-\mathbf1_{x\in H}.
\]

The external-offset theorem then gives set-valued Hall capacities

\[
e^{\rm ext}(X)\le\min\{E-s_X,E-a_X,d_X\}\le3u_X
\]

and the zero-run tail bound \(\sum(\ell-3)_+\le210\).  They narrow the live
finite gate to the order-sensitive literal source/exposure geometry, but do
not contradict a survivor.  Sources:
`K11_MIDDLE_LEVELS_NEWLINE_20260724.md`,
`K11_MIDDLE_LEVELS_NEWLINE_AUDIT_20260724.md`,
`K11_EXTERNAL_OFFSET_CAPACITY_20260724.md`, and
`K11_EXTERNAL_OFFSET_CAPACITY_AUDIT_20260724.md`.

## Evidence classification

- The upper witnesses for \(K=7,\ldots,12,14\) have complete mask-coverage
  verification logs.  The remaining upper endpoints follow from the proved
  lift and deterministic constructor.
- Every lower endpoint is a theorem-level global lower bound, not an
  inference from a failed search.
- The stored \(K=11\) length-476 and \(K=13\) length-1851 near-words still
  miss a mask and are not upper bounds.
- DRAT certificates for selected edit neighborhoods at \(K=11,13,14\) are
  rigorous local theorems only; they do not raise the global lower bounds.
- The last recorded \(K=11\) length-465 and \(K=14\) append-241 runs had no
  terminal constructive model or certified global UNSAT result and therefore
  have no effect on this table.
