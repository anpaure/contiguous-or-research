# Independent audit: containment caps in the generic and append-completion solvers

## Verdict

**PASS for the intended nonzero domain `1 <= k < 20`, `q >= 0`.**

Both implementations apply the simultaneous containment-multiplicity theorem
correctly.  In particular:

* `exact_or_sat.cpp` loses no universal arrays when it removes witness
  intervals longer than the simultaneous rank cap;
* `append_completion_sat.cpp` loses no fixed-prefix completions when it keeps
  only the shortest fixed suffix having each suffix-OR value and then applies
  the same cap to the resulting physical interval;
* with `APPEND_CONTAINMENT_CAPS=0`, the nontrivial completion formula is
  byte-for-byte unchanged from the frozen pre-cap source;
* for all three live `k=11` deletion candidates, even enabling the caps leaves
  the DIMACS file byte-for-byte unchanged;
* the formerly crashing case in which the fixed prefix is already universal
  is now handled by a correct nonzero-padding return.

The current source hashes are

```text
e60b88613d65a448679ab01e407e06ea5844e203156bc4d80d7836372d4a535b
    append_completion_sat.cpp
c1832b235f75be91066fc454ac7c6c46d29610a22aa2826d34c404915600f550
    exact_or_sat.cpp
```

The audit also proves a stronger consequence for the `k=11,n=465` local-
density module.  Its six-set inequality should use `p_U >= 28`, not the
previous `p_U >= 23`.  More generally, marked-run packing gives the cap-only
subcube bounds

```text
s:       1  2  3  4   5   6   7   8    9   10
p_s >=   1  2  4  8  16  28  45  76  129  214.
```

## 1. Mathematical cap used by both sources

For a universal array of total length `n`, choose one witness interval for
each member of a rank-`r` layer of size

\[
 M_r=\binom{k}{r}\le n,
 \qquad d_r=n-M_r.
\]

Ordering these intervals by their left endpoints, incomparability of distinct
equal-rank masks forces their right endpoints into the same strict order.  The
`i`-th selected interval is therefore contained in `[i,i+d_r]`.

If a physical interval `J` of length `ell` has OR-rank `s`, then, for
`ell>d_r`, it contains at least `ell-d_r` selected rank-`r` witnesses.  They
are distinct rank-`r` subsets of the `s`-set `OR(J)`.  Consequently

\[
 \ell\le
 \begin{cases}
 d_r,&r>s,\\
 d_r+\binom{s}{r},&r\le s.
 \end{cases}
\]

Taking the minimum over all ranks whose layer fits in `n` gives

\[
 c_s(k,n)=\min_{\binom{k}{r}\le n}
 \left(n-\binom{k}{r}
       +\mathbf 1_{r\le s}\binom{s}{r}\right),             \tag{1}
\]

with the harmless outer cap `c_s<=n`.

This theorem bounds **every** physical interval of OR-rank `s`, not merely a
particular selected witness.  Hence a universal array always has all of its
target witnesses inside the domains retained by either solver.  Separate
rank-`r` witness families may be chosen for separate values of `r`; no
compatibility assumption is used in deriving (1).

The two implementations calculate (1) exactly.  For `k<20`, all binomial
values fit easily in their respective integer types.  Since ranks with
`M_r>n` are skipped, each candidate before the binomial addend is nonnegative.
If the final cap is zero, a nonempty target genuinely cannot have a witness;
the generic generator reports this contradiction instead of silently keeping
an invalid interval.

## 2. Audit of `exact_or_sat.cpp`

`maximum_witness_length(k,n,s)` is exactly (1).  During selector generation,
the source omits every interval whose physical length exceeds this value.
The shared interval-OR gates still encode the exact OR of every retained
interval, and each target chooses exactly one selector.

Completeness follows immediately from Section 1: given any universal array,
choose any witness for each target.  Every such interval obeys the cap, so its
selector remains.  Soundness is unchanged because the new operation only
deletes selectors; a satisfying selector still points to a physical interval
whose gate bits equal the target exactly.

The source requires every entry to be nonzero.  This is without loss even
when testing a nonminimal exact length `n`: delete all zero entries from a
putative solution, preserving every nonzero witness, and append arbitrary
nonzero entries until length `n` is restored.  Appending cannot destroy an
old witness.  The solver intentionally addresses the nonzero problem; the
single literal zero required by the original full problem is handled outside
this encoding.

There is no containment-cap disable switch in this source: the upgrade is
mandatory and theorem-preserving.  Thus the disabled-mode regression below
applies to the optional append solver, not to this generator.

## 3. Shortest fixed-suffix substitution

Let the fixed prefix have length `P`.  Every interval that crosses its right
boundary has the unique form

\[
 [i,P-1]\;\Vert\;[0,e]
\]

in fixed-prefix and appended coordinates.  To the appended variables, the
fixed part matters only through

\[
 F=\bigvee_{j=i}^{P-1} A_j.
\]

Scanning suffixes from right to left visits their physical lengths in the
order `1,2,...,P`.  The first time a new OR value is pushed is therefore the
shortest suffix that realizes that value.  This proves that the stored pair

```text
{ fixed suffix OR, shortest physical suffix length }
```

has its advertised meaning.

Now take any crossing witness in a genuine completion.  Replace its fixed
suffix by the stored shortest suffix with the same OR, retaining its appended
portion `[0,e]`.  Its total OR is unchanged, while its physical length can
only decrease.  Therefore, if the old witness obeyed `c_s(k,P+q)`, the stored
representative also obeys it and is emitted by the solver.

Conversely, every emitted crossing representative is an actual contiguous
interval: it starts `shortest_length` positions before the seam and ends at
append position `e`.  The selector clauses enforce precisely that no outside
target bit appears and every target bit not already in the fixed OR appears
in the append prefix.  Thus the substitution preserves both completeness and
soundness.

The total length passed to the theorem is correctly computed **after** an
optional prefix deletion:

```text
prefix.size() + q.
```

This is the length of the actual completed word.  Existing prefix-covered
masks need no selectors because appending entries cannot invalidate their old
witnesses.  Any missing mask in a valid completion must be witnessed either
inside the appended block or across the seam, exactly the two candidate
families encoded by the source.

## 4. Zero and boundary cases

Append entries are constrained to be nonzero.  This is also without loss for
an exact append length: delete every zero append entry, compressing witnesses,
then append arbitrary nonzero padding to restore `q`.  Old witnesses remain.

The following cases were checked separately:

* empty fixed prefix: there are no crossing suffixes and the encoding reduces
  correctly to append-only intervals;
* `q=0` with missing targets: a target has empty support and the program
  correctly reports impossibility;
* `q=0` with a universal prefix: the trivial return emits an empty append;
* universal prefix with `q>0`: the current source emits `q` copies of mask
  `1`, which is valid for `k>=1` and preserves all prefix witnesses.

Before the last case was added, the phase heuristic evaluated
`position % missing.size()` with an empty missing family and raised `SIGFPE`.
The early padding return repairs that pre-existing bug without touching any
nontrivial formula.  A remote `k=1`, universal-prefix, `q=1` regression now
returns one appended `1` and independently verifies `1/1` nonzero masks.

The CLI still assumes its documented mathematical input domain `k>=1` and
`q>=0`; negative lengths and the degenerate zero-bit problem are not validated
by this specialized nonzero completion executable.

## 5. Exact disabled-mode and live-formula regression

The frozen source immediately before the append caps has SHA-256

```text
852247ff77a69219b63eabdf83edce3411a999473e95414ec6f650aaa3e934b2
```

When `APPEND_CONTAINMENT_CAPS=0` and the missing family is nonempty, replacing
the old integer suffix vector by the new structs does not alter the suffix
order, OR values, selector order, clauses, or variable numbering.  The only
observable textual difference is the stderr diagnostic
`containment_caps=0`.

This was checked more strongly on the three current hard `k=11` deletion
instances.  For each instance, DIMACS was generated by the current source
with the caps both disabled and enabled and compared against the frozen
pre-cap DIMACS:

| skipped prefix index | variables | clauses | candidates | SHA-256 of all three DIMACS files |
|---:|---:|---:|---:|---|
| 7 | 1806 | 113634 | 1674 | `7bee63cc6bd6576e1cbc0fd3b6c1e6c1ad5f14342eb9c3d95c4bb5c07602c56b` |
| 89 | 1650 | 102478 | 1518 | `17ab8f79efb55cbf5796f75166e9b28f47d2ce3349c9ec65f2758f4147bb920f` |
| 196 | 1650 | 101906 | 1518 | `4871d26ed7dd2444e6199eb98aad07eaea640f437ce6b0e0c265bc2c452f06e7` |

All six comparisons were byte-identical.  Thus the caps genuinely make no
formula change to these three runs; this is stronger than comparing only
counts.  Their previous proof/search state remains applicable.

## 6. Lightweight executable regressions

All compilation and solving was performed on the remote Linux host.  No
production solve was launched on the local Mac.  Both current sources compile
under GCC with `-O3 -Wall -Wextra -Wpedantic` with zero warning bytes.

### Generic exact solver

The capped generic source generated and Kissat solved the exact optimum
`k=3,n=4` instance:

```text
variables=195 clauses=578
decoded array: 1 2 4 1
independent suffix verifier: length=4 covered=7/7 missing=0
```

Artifact hashes:

```text
844e36470b3e213211244e622086cb4838851840cb1beddff8aa8e14376ab139
    k3n4.cnf
2ccfc81e078b8d8ce449bdfc13ce05e485681bc27e871c455d41b453413e95e2
    k3n4.model
b701f41417f334e6db409f347426bc868a87b15fabb7197d66c4d8bd24db9b9e
    decoded array file
```

### Append solver

For the fixed `k=4` prefix

```text
5 9 1 2 4
```

and `q=2`, the disabled formula had 18 candidates, 26 variables and 119
clauses.  Enabling the cap removed two candidates and produced 16 candidates,
24 variables and 101 clauses.  Both modes returned a length-seven completion
and independently verified all `15/15` nonzero masks.  One capped result was

```text
5 9 1 2 4 8 2.
```

The completed word has SHA-256

```text
e62fcea7caee38341e5a5cc5bf18637339750b9cf1c9c36b07fe611ca5cda29c.
```

These are small executable regressions, not evidence about any unresolved
large instance; logical completeness comes from Sections 1--3.

## 7. Stronger marked-run theorem for `k=11,n=465`

The simultaneous cap vector is

```text
rank s:   1  2  3  4  5  6   7   8   9   10  11
c_s:      3  3  3  3  3  4  10  31  87  213 465.
```

Fix an `s`-set `U` and mark every physical position `i` for which
`A_i subseteq U`.  The marked positions split into runs.  The cap sequence is
nondecreasing in target rank: each candidate function in (1) is
nondecreasing, and so is their pointwise minimum.  A marked run longer than
`c_s` would contain an interval of length `c_s+1` whose OR has some rank at
most `s`, contradicting its cap.  Therefore every marked run has length at
most `C=c_s`.

For `t>=1`, put

\[
 F_t(\ell)=\sum_{j=1}^{\min(t,\ell)}(\ell-j+1).
\]

Every mask `T subseteq U` whose rank `r` satisfies `c_r<=t` has a distinct
witness of length at most `t`, wholly inside one marked run.  Thus the marked
runs must supply at least

\[
 H_s(t)=\sum_{\substack{1\le r\le s\\c_r\le t}}\binom{s}{r}       \tag{2}
\]

such intervals.

For total marked mass `p` and run cap `C`, the maximum possible supply is

\[
 G_{C,t}(p)=\left\lfloor\frac pC\right\rfloor F_t(C)
             +F_t(p\bmod C).                                  \tag{3}
\]

To prove (3), observe that

\[
 F_t(\ell)-F_t(\ell-1)=\min(t,\ell)
\]

is nondecreasing.  Moving one position from a smaller nonempty run to a
larger nonfull run never decreases the supply.  Iterating leaves as many full
`C`-runs as possible and one remainder, proving the claimed maximum.

Combining (2)--(3) at every distinct cap threshold gives the following exact
cap-only lower bounds:

| `s` | decisive target count | largest supply at `p_s-1` | `p_s` | supply at `p_s` |
|---:|---:|---:|---:|---:|
| 1 | `H(3)=1` | 0 | 1 | 1 |
| 2 | `H(3)=3` | 1 | 2 | 3 |
| 3 | `H(3)=7` | 6 | 4 | 7 |
| 4 | `H(3)=15` | 13 | 8 | 15 |
| 5 | `H(3)=31` | 30 | 16 | 31 |
| 6 | `H(3)=62` | 60 | 28 | 63 |
| 7 | `H(3)=119` | 117 | 45 | 120 |
| 8 | `H(3)=218` | 216 | 76 | 219 |
| 9 | `H(3)=381` | 378 | 129 | 381 |
| 10 | `H(3)=637` and `H(4)=847` | 636 and 846 | 214 | 637 and 847 |

All larger thresholds were checked and are slack at the displayed `p_s`.

The requested six-set statement is the `s=6` row.  A run has length at most
four.  Its numbers of intervals of length at most three are respectively
`1,3,6,9` for run lengths `1,2,3,4`.  With at most 27 marked positions, (3)
gives six four-runs and one three-run, hence at most

\[
 6\cdot9+6=60<2^6-2=62
\]

proper nonempty subsets.  Therefore

\[
 \boxed{p_U\ge28.}
\]

No `p_U>=29` conclusion follows from interval cardinality alone: at `p=28`,
seven four-runs provide 63 eligible short intervals for 62 proper targets.
Improving 28 would require an OR-collision, ordering, or pin-survival argument.

## 8. Aggregate pseudo-Boolean cuts

Let `n_j` denote the number of literal array entries of rank `j`.  Double
counting pairs `(i,U)` with `A_i subseteq U`, over all `s`-sets `U`, gives

\[
 \sum_{j=1}^{s}\binom{11-j}{s-j}n_j
 \ge p_s\binom{11}{s}.                                      \tag{4}
\]

The cap-only cuts are therefore:

```text
s=1:   n1 >= 11
s=2:   10n1+n2 >= 110
s=3:   45n1+9n2+n3 >= 660
s=4:   120n1+36n2+8n3+n4 >= 2640
s=5:   210n1+84n2+28n3+7n4+n5 >= 7392
s=6:   252n1+126n2+56n3+21n4+6n5+n6 >= 12936
s=7:   210n1+126n2+70n3+35n4+15n5+5n6+n7 >= 14850
s=8:   120n1+84n2+56n3+35n4+20n5+10n6+4n7+n8 >= 12540
s=9:   45n1+36n2+28n3+21n4+15n5+10n6+6n7+3n8+n9 >= 7095
s=10:  10n1+9n2+8n3+7n4+6n5+5n6+4n7+3n8+2n9+n10 >= 2354.
```

Relative to the ordinary subcube restriction `p_U>=nu(s)` using the certified
exact values through ten bits, the cap-only bounds agree for `s=1,2,3`, are
strictly stronger for every `s=4,...,9`, and are weaker at `s=10`, where the
known exact value gives `p_U>=254` and right side `2794` instead of `2354`.
The `s=1` cut is already literal-singleton necessity, and `s=2` follows from
`n1>=11`; they need not be separately encoded.

For the current local-density PB module the immediate required update is

```text
10626  ->  12936
```

in its six-set comparator.  Its five-set cut remains exactly the audited
`7392` cut.  The `s=4,7,8,9` inequalities are additional valid theorem cuts
and are genuinely stronger than the corresponding previously known subcube
bounds.  Whether their propagation benefit justifies four more binary sums
is an engineering choice; the mathematical recommendation is to make them
optional and share the already-built exact entry-rank layer.  The `s=10`
cap-only cut should not be added in place of the stronger certified
`p_U>=254` dimension cut.

## 9. Scope

This audit proves only the validity, completeness preservation, regressions,
and marked-run consequences of the containment-cap changes.  It does not
claim SAT or UNSAT for any unresolved `k=11` or `k=14` search.  The three
live deletion formulas are unchanged, so the cap option cannot alter their
search outcome; its value is in formulas whose candidate intervals actually
exceed the new rank caps.
