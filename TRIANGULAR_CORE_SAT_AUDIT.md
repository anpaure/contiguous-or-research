# Audit of the `S=6`, length-21 completion-core SAT claim

## 1. Scope and conclusion

This audit concerns only the fixed 21-token multiset in
`scratch/core_s6_k6_multiset.txt`.  It asks whether **some ordering of that
exact multiset** is a `7`-completion core.  It does not ask whether another
length-21 multiset can be a completion core, and it does not decide the
unrestricted triangular optimum.

The source-level conclusion is:

> `scratch/triangular_core_sat.cpp` is an exact encoding of this fixed-multiset
> ordering question.  For the supplied multiset, SAT is equivalent to the
> existence of a valid ordering with all 55 strict-positive targets, a perfect
> nested terminal suffix fan through height five, and terminal `P_0`.

The generated formula has exactly 23,691 variables and 188,975 clauses.  An
independent parse confirms that all 188,975 clauses are present, all terminate
correctly, the largest variable is 23,691, and every declared variable occurs.

The final UNSAT conclusion is certified.  The exact generated CNF and complete
DRAT trace were copied into the workspace, their uncompressed hashes match the
audited formula and remote originals, and the proof was checked twice.  The
second check was a fresh compilation and invocation of `drat-trim` on a
different RunPod host.  Both checks end in `s VERIFIED`.

## 2. The exact mathematical object

Cells are

\[
  E_{s,y}=(s,y),\qquad 0\le y<s\le 6,
\]

together with `P_0=(0,0)`.  A contiguous interval represents target
`(u,r,x)` when its coordinatewise bounding box is

\[
 [u,r]\times[0,x].
\]

For a `7`-completion core, the strict-positive targets are exactly

\[
 1\le u<r\le6,\qquad1\le x<r.
\]

Their number is

\[
 
 \sum_{r=2}^{6}(r-1)^2=1+4+9+16+25=55.
\]

A perfect terminal suffix fan through height five requires one suffix with
box

\[
 [0,h+1]\times[0,h]
 \qquad(1\le h\le5).
\]

The chosen suffix starts must be nonincreasing as `h` increases.  In fact this
ordering follows already from the exact bounding boxes, but encoding it
explicitly is harmless.

The input multiset consists of:

* every positive-height cell in rows at most six exactly once, except for the
  single top-row hole `E_(6,3)`;
* one `P_0`;
* peak multiset `P_1^2 P_2^2 P_4 P_5`.

It has 21 tokens and core excess six.  Thus the spanning and top-row-hole
conditions are built into the multiset.  Only its ordering, strict-target
coverage, suffix fan, and terminal `P_0` remain to be decided.

## 3. Permutation variables and duplicate symmetry

`wordVar(position,token)` is a 21 by 21 permutation matrix.

* Every position has exactly one token.
* Every labelled token has exactly one position.

The two copies of `P_1` and the two copies of `P_2` are initially treated as
distinct tokens.  For each equal-token pair `(first,second)` with
`first<second`, the symmetry clauses force

\[
  \operatorname{pos}(first)<\operatorname{pos}(second).
\]

The implemented clause for positions `i,j` forbids `first` at `i` together
with `second` at `j` whenever `j<=i`.  This is the correct direction.  It
does not remove any unlabelled word: label equal occurrences from left to
right by increasing input-token index.

There are two equal-token pairs, so symmetry breaking contributes

\[
 2\binom{22}{2}=462
\]

clauses.

## 4. Target witnesses are encoded exactly

The generator enumerates all inclusive intervals `[left,right]` with
`left<right`.  There are

\[
 P=\binom{21}{2}=210.
\]

Omitting singleton intervals is safe because every strict target has
`u<r`; one cell can never have distinct minimum and maximum first coordinate.

For every target, a sequential exactly-one encoding selects one interval.
For a selected interval the clauses require:

1. every cell satisfies `u<=s<=r` and `y<=x`;
2. some cell has `s=u`;
3. some cell has `s=r`;
4. some cell has `y=x`;
5. some cell has `y=0`.

Because all input cells have nonnegative height, these conditions are
equivalent to bounding box `[u,r] x [0,x]`.  The four provider clauses may
be satisfied by overlapping providers, as they should be.

The sequential encoding contains an at-least-one clause and the standard
`3P-4` Sinz at-most-one clauses.  Hence it selects exactly one witness, not
merely at most one.

## 5. The suffix fan is encoded exactly

For height `h`, `fanTarget(h)` is `(0,h+1,h)`.  A sequential exactly-one
encoding chooses one suffix start, and the same allowed/provider clauses are
applied to `[start,20]`.  Therefore the selected suffix has exactly the box
`[0,h+1] x [0,h]`.

For consecutive heights, the clauses forbid

\[
  start_h<start_{h+1},
\]

so `start_h>=start_(h+1)`, the correct nested-fan direction.  The unique
`P_0` token is forced into position 20.  Consequently all fan suffixes end in
`P_0`, exactly as required.

## 6. Exact equivalence proof

### SAT implies a valid core ordering

The permutation clauses decode a permutation of the supplied multiset.
Terminal `P_0` follows from the final unit clause.  Each target's selected
interval has the exact required bounding box by the implication clauses.
Each height's selected suffix has the exact fan box, and the suffix starts
are nested.  The multiset itself supplies the spanning and one-top-row-hole
conditions.  Thus the decoded word is a valid `7`-completion core.

### A valid ordering implies SAT

Label equal occurrences from left to right, satisfying duplicate symmetry.
Choose one witnessing interval for every strict-positive target and one
suffix for every fan height.  Assign the sequential auxiliary variables in
the usual prefix manner.  Every allowed/provider implication is then true,
and terminal `P_0` satisfies the unit clause.  Hence every valid ordering
extends to a satisfying assignment.

Therefore UNSAT for this CNF proves that no ordering of this exact multiset is
a completion core.

## 7. Independent arithmetic and generated-CNF audit

For `n=21`, `T=55`, `P=210`, and `F=5`, the variable ledger is

| family | count |
|---|---:|
| permutation | `21^2 = 441` |
| target witness choices | `55*210 = 11,550` |
| target sequential auxiliaries | `55*209 = 11,495` |
| fan choices | `5*21 = 105` |
| fan sequential auxiliaries | `5*20 = 100` |
| **total** | **23,691** |

The clause ledger is

| family | count |
|---|---:|
| position/token permutation | `2*21*(1+C(21,2)) = 8,862` |
| duplicate symmetry | `462` |
| target exactly-one | `55*(3*210-3) = 34,485` |
| target interval implications | `55*(1,750+4*210) = 142,450` |
| fan exactly-one | `5*(3*21-3) = 300` |
| fan suffix implications | `5*(C(22,2)+4*21) = 1,575` |
| fan nesting | `4*C(21,2) = 840` |
| terminal `P_0` | `1` |
| **total** | **188,975** |

Here 1,750 is the sum of the lengths of all non-singleton intervals:

\[
 \sum_{\ell=2}^{21}\ell(22-\ell)=1,750.
\]

Regeneration produced:

```text
S=6 n=21 targets=55 variables=23691 clauses=188975
p cnf 23691 188975
actual clauses 188975
maxvar 23691 badterm 0 internal0 0 seenvars 23691
```

Relevant SHA-256 values are:

```text
b92758673e1804044e824e7be0cdf1f0aedd4bf8077855347ccd2fed3ad792a3  scratch/triangular_core_sat.cpp
92f463446f1a049dffdb310da1e98adbcc12695426c5e8f3a56eb1c00d971e91  scratch/core_s6_k6_multiset.txt
ad2125c3ef63684691e780412b08a1bee05af87a1e4cc0f3abc9352b8608a689  scratch/core_sat_audit/core_s6_k6.cnf
```

## 8. Positive controls

The encoder was also run on three independently known valid cores:

* `S=3`, length 6: SAT; decoded word independently passed all targets and
  fan starts `4,3`;
* `S=4`, length 10: SAT; decoded word independently passed all targets and
  fan starts `8,6,0`;
* `S=6`, length 24 (`C_6` from `R7_CERTIFICATE_STRUCTURE.md`): SAT; the
  independently checked fan starts are `21,20,18,16,15`.

The independent checker is
`scratch/core_sat_audit/verify_completion_core.cpp`.  It does not reuse the
SAT generator's target/provider routines.

These controls do not prove UNSAT of the 21-token case; they establish that
the formula accepts known valid instances at the same target rank and fan
depth and help detect reversed nesting, target-range, and endpoint mistakes.

## 9. Proof-certificate audit

The archived artifacts are:

```text
scratch/certificates/core_s6_k6.cnf.gz
scratch/certificates/core_s6_k6.drat.gz
scratch/certificates/core_s6_k6_proof.log
scratch/certificates/core_s6_k6_dratcheck.log
```

Their compressed SHA-256 values are:

```text
f5afeb332369886340d56b42d609cdf292417a450629b1d7cb78e4f57d32aeef  core_s6_k6.cnf.gz
9444f4f78499cc82c1c2c838f8533f6ee7855ea78b3ebd787d4626bc7df3c2bf  core_s6_k6.drat.gz
bde6e1eede96772c07c8ce29fd18088863815bd043aa59a06f11f5838cf8a162  core_s6_k6_proof.log
4600b9971f01ae6bc12e01e9a4b53a11b31b2bf4f2660560ee1e6e67f2f453f7  core_s6_k6_dratcheck.log
```

After decompression:

```text
ad2125c3ef63684691e780412b08a1bee05af87a1e4cc0f3abc9352b8608a689  core_s6_k6.cnf
fb4820aff3df030d83077fea4273013f3cdd9e29d0eab8a96285e8e8706705e0  core_s6_k6.drat
```

The uncompressed CNF is byte-identical to the formula independently
regenerated from the audited source and multiset.  The remote source and
multiset hashes also equal the local hashes in Section 7.

The proof-producing solver was Kissat 4.0.4.  The remote executable hash was

```text
0a0f9ef8e8f73235f37dea6bc294905ac470c41def0f1f605b4128fa0c0509c4
```

and its result log is exactly `s UNSATISFIABLE`.

The first proof check used `drat-trim` at Git revision
`2e3b2dc0ecf938addbd779d42877b6ed69d9a985`; its executable hash was

```text
be9a20191731a6a6a82e509d959d5c5c9f69f1a92765bf3209685622c0384498
```

and its archived log reports:

```text
c parsing input formula with 23691 variables and 188975 clauses
c 24183 of 188975 clauses in core
c 9622 of 40495 lemmas in core using 585688 resolution steps
c 4841 RAT lemmas in core; 4391 redundant literals in core lemmas
s VERIFIED
c verification time: 32.755 seconds
```

For the independent audit, the same revision's C source was freshly compiled
with GCC 9.4.0 on a different 16-core RunPod.  The resulting checker hash was

```text
66acaf89cd4da7bff01b2427535caf5059faf3211bf10c5863e81d24d2605bb5
```

It checked independently transferred copies with the same uncompressed hashes
and again reported the identical core/lemma counts followed by
`s VERIFIED` (53.208 seconds).  That log is archived at
`scratch/core_sat_audit/certificates/core_s6_k6_independent_dratcheck.log`,
with SHA-256

```text
50cde90751093a5ac6af4fb587662ef24d5314a5f485639e6f0213c626575693
```

Thus the UNSAT result is proof-certified rather than inferred from a solver
exit line, timeout, or failed heuristic search.

## 10. Exact logical consequence

The checked proof establishes precisely:

\[
 \boxed{\text{No permutation of }M_6^*\text{ is a `7`-completion core.}}
\]

It does **not** establish any of the following without an additional
classification theorem:

* no length-21 `7`-completion core exists;
* `rho(7)>6`;
* no triangular word of length `|T_7|+6` exists;
* the edge-balanced core conjecture fails at `S=6` for every possible
  multiset.

The fixed multiset was a concrete and mathematically motivated reduction
candidate, but it has not been proved to be the only possible excess-six
ledger.
