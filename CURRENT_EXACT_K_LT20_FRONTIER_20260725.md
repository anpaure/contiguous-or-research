# Current exact finite frontier, \(K<20\)

The original problem asks for every mask, including zero.  Let \(\nu(K)\)
denote the nonzero-word minimum covering every nonzero mask.  Then the
literal answer is

\[
N(K)=\nu(K)+1,
\]

because one additional zero entry is necessary and sufficient for mask zero.

## Certified table

\[
\begin{array}{c|c|c}
K&\nu(K)&N(K)\\ \hline
0&0&1\\
1&1&2\\
2&2&3\\
3&4&5\\
4&7&8\\
5&12&13\\
6&21&22\\
7&37&38\\
8&72&73\\
9&128&129\\
10&254&255\\
11&465&466\\
12&926&927\\
13&[1719,1852]&[1720,1853]\\
14&[3434,3668]&[3435,3669]\\
15&[6438,7352]&[6439,7353]\\
16&[12873,14704]&[12874,14705]\\
17&[24313,29408]&[24314,29409]\\
18&[48623,58816]&[48624,58817]\\
19&[92381,117632]&[92382,117633]
\end{array}
\]

Thus the unresolved set is

\[
\{13,14,15,16,17,18,19\}.
\]

## Revalidated first open case

The stored \(K=11\) word `k11_completed_477.txt` was rechecked on
2026-07-25 with

```text
./verify_or_array 11 < k11_completed_477.txt
```

and returned

```text
length=477 covered=2047 required=2047
missing:
```

with exit code zero.  The lower-bound arithmetic was independently rerun via

```text
python3 scratch/check_iterated_boundary_core_rigidity.py
```

and returned `PASS`, including the strict \(K=11\) record

```text
rank 5: 464
rank 6: 465
```

Therefore the current rigorous first-open interval remains

\[
\boxed{465\le\nu(11)\le477.}
\]

## Exact mathematical gate at \(K=11\)

A hypothetical length-465 word is already forced into the audited
zero-margin normal form:

- one central rank-at-most-three segment whose ordinary pair, triple, and
  four-windows give distinct ranks \(4,5,6\);
- a one-jump Johnson flag path through those three layers;
- a spanning linear forest of \(J(11,5)\) with at most six components and
  distinct rank-six union colours;
- an endpoint-ordered perfect inclusion matching between all 462 five-sets
  and all 462 six-sets;
- subset-completion totals \((42,42,28,14,5,1)\);
- the exact central/external coordinate law

  \[
  e_x^{\rm cen}=R_x^{(3)}-1+\mathbf1_{x\in H},\qquad
  e_x^{\rm ext}=43-R_x^{(3)}-\mathbf1_{x\in H};
  \]
- directed external Hall capacities and the zero-run tail

  \[
  \sum_{\text{zero runs }I}(|I|-3)_+\le210.
  \]
- every forest edge has a literal width-at-most-four rank-seven hull, at
  least 319 rank-seven hull colours are distinct, and at most eleven
  rank-seven colours may be absent; and
- at most two inward interfaces lie outside the directed external Hall
  system.

No contradiction to this complete template is currently proved, and no
length-465 word is known.  A proof resolving \(K=11\) must either construct
one such template as a literal word or contradict its remaining
order-sensitive source/exposure geometry.  Restricted SAT/DRAT neighborhood
closures do not settle the global case.

The latest exact hand reduction replaces the interior source/target states
by a two-token reservoir automaton.  Each source is a two-set cache plus the
previous three missing-coordinate labels, and each matched six-set is the
same cache plus the previous four labels.  The cache either stays fixed or
replaces one token by the oldest recent label.  Both rank-four shadow
families are explicit functions of this state.  In particular, paired
lower/upper shadow occurrences are injective, lower colours have recurrence
gap at least four, and every fixed three-set has source-residence runs of
length at most three.  The complete statement and proof are in
`K11_TWO_TOKEN_RESERVOIR_AUTOMATON_AUDIT_20260725.md`.  This strengthens the
equality template but does not change the bracket.

A concrete construction lane has an exact local splice formulation.
Expanding the canonical MSW wreath factor gives 42 physical eleven-cycles.
A one-cut fusion into six paths is equivalent
to selecting one of 22 oriented cut ports on each cycle and 36 locally legal
arcs forming an acyclic directed graph of indegree/outdegree at most one.
The five seam tests, the four head double-block patterns, and the exact
support replacement ledger are proved in
`K11_MSW_PHYSICAL_CYCLE_SPLICE_GATE_20260725.md`.  The formerly quoted hole
list had one error: the displayed class-E row from \(T_4\), with
\(R\mid I=4217\mid6538\), contains \(\{1,2,7,10\}\), while
\(\{3,4,7,10\}\) is absent.  The corrected 32-hole family is now proved to
be the complete complement, and the cyclic-four support is certified as
exactly 298, by
`K11_CORRECTED_CYCLIC4_POSITIVE_SUPPORT_CERTIFICATE_20260725.md`.  The old
multiplicity histogram is retracted after two further E-table transcription
corrections; no current argument may use that histogram.  None of these
corrections alters the certified interval \(465\le\nu(11)\le477\).

The corrected backward-tail audit is now complete for the resulting 32
certified holes.  Four omitted class-E deletion incidences were restored;
the A--E maximum tail-wreath degrees are respectively

\[
8,5,8,10.
\]

Moreover, an explicit matching assigns all 32 holes to 32 distinct tail
wreaths, and the sixteen zero-containing holes admit a perfect disjointness
matching to the sixteen zero-avoiding holes.  Thus neither backward-tail
Hall nor abstract lower/upper disjointness is the remaining obstruction.
The unresolved finite gate is their physical four-way lift through the head
orientation tests, simultaneous upper-colour creation, common port choices,
cut-colour losses, and acyclicity.  The exact ledger is in
`K11_CORRECTED_TAIL_TRANSVERSAL_AND_COUPLED_GATE_20260725.md`.  The formerly
separate positive-support audit is now closed by the certificate cited
above.

Authoritative sources are `EXACT_K_LT20_STATUS_AUDIT_20260724.md`,
`FINITE_K_STATUS_20260724.md`, `K11_ZERO_MARGIN_WINDOW_ATTACK_20260724.md`,
`K11_MIDDLE_LEVELS_NEWLINE_20260724.md`, and
`K11_EXTERNAL_OFFSET_CAPACITY_20260724.md` with their independent audits.

## Certified local exclusions at $K=11$

The global interval remains unchanged, but two additional exhaustive
neighbourhoods are now closed.

1. Start from the certified 465-entry partial word
   `k11_upper549_natural_array.txt`, replace one entry by an arbitrary
   nonzero 11-bit mask, and append eleven arbitrary nonzero entries.  None
   of the

   \[
   465\cdot2047=951{,}855
   \]

   possible prefix edits admits a universal completion.  Inclusion-width
   screening leaves only the two edits $288\mapsto800,808$ at position
   159, and independent exact suffix-state DFS and BFS prove both remaining
   completion problems unsatisfiable.

2. Delete any one entry of `k11_completed_477.txt`, then replace any one of
   the remaining entries by an arbitrary nonzero 11-bit mask.  Independent
   exhaustive implementations checked all

   \[
   477\cdot476\cdot2047=464{,}775{,}444
   \]

   cases and found no universal 476-entry word.

3. From either of the two width-feasible first-edit roots
   $288\mapsto800,808$ at position 159, make one further arbitrary
   replacement and append eleven arbitrary entries.  Independent width
   screens find 1,610 feasible replacements from each root and exactly
   2,290 distinct candidate prefixes.  Every exact append-completion CNF is
   UNSAT, with all 2,290 individual DRAT proofs checked successfully.

These are exact local theorems, not a proof that every 465- or 476-entry
word is impossible.  Full statements, hashes, reproduction commands, and
the independent implementations are in
`K11_EXACT_FRONTIER_AUDIT_AND_LOCAL_CLOSURES_20260725.md`.  The larger
rooted second-replacement closure is recorded separately in
`K11_SECOND_REPLACEMENT_APPEND11_CERTIFIED_20260725.md`.
