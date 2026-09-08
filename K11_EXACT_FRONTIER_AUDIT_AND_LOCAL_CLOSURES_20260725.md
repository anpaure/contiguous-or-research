# Exact (k=11) frontier audit and two new local closures

Date: 2026-07-25

## 1. Certified global status

Let \(\nu(k)\) be the minimum length of a word of **nonzero** \(k\)-bit
masks whose nonempty contiguous ORs contain every nonzero mask.  Let \(N(k)\)
be the minimum for the literal problem, which also requires zero.  Then

\[
N(k)=\nu(k)+1,
\]

because a nonempty OR is zero only when all entries in its witnessing
interval are zero, while prepending one zero preserves every old witness.

The strongest certified statement at the first unresolved case is still

\[
\boxed{465\le \nu(11)\le477},
\qquad
\boxed{466\le N(11)\le478}.
\]

No root-level `K11_*.md` or `MATH_ATTACK_*K11*.md` report supplies a global
endpoint improvement.  An inventory of all 206 such reports found only:

* necessary structural theorems for a hypothetical equality word;
* exact but restricted edit-neighborhood exclusions;
* guarded encodings without a terminal certified global solve; and
* heuristic near-words, all missing at least one mask.

### Lower endpoint

The rank-count theorem gives the lower bound without computation.  There are

\[
M=\binom{11}{6}=462
\]

rank-six masks.  If a word has length \(M+t\), choose one witness interval
for each rank-six mask and order the witnesses by their left endpoints.
The endpoint-order lemma puts the \(i\)-th witness inside \([i,i+t]\).
Consequently every interval of length at least \(t+1\) contains a selected
rank-six witness and has OR-rank at least six.  Hence every one of the

\[
L=\sum_{s=1}^{5}\binom{11}{s}=1023
\]

lower masks must use an interval of length at most \(t\).  The number of
such physical intervals is

\[
tM+\binom{t+1}{2}.
\]

At \(t=2\) this is \(927<1023\), so \(t\ge3\) and
\(\nu(11)\ge462+3=465\).  The arithmetic was independently recomputed by
`scratch/check_iterated_boundary_core_rigidity.py`.

### Upper endpoint and explicit word

The explicit nonzero word is `k11_completed_477.txt`, containing exactly
477 entries, all in \(\{1,\ldots,2047\}\).  Its SHA-256 is

```text
aa88d2c22431af19e4b4c4a2073251d1316d02a6e152d218cca2082bdc58d58b
```

Fresh runs gave

```text
verify_or_array:  length=477 covered=2047 required=2047
rebuilt suffix verifier: length=477 covered=2047/2047 missing=0
```

The all-mask word is the explicit 478-entry word

```text
0 || k11_completed_477.txt.
```

Fresh direct quadratic enumeration reports 2,048/2,048 masks.  The current
`construct_or_array` binary emits exactly this word on input 11; its embedded
477 nonzero entries agree entry-for-entry with the text certificate.

## 2. Strongest theorem-level equality information

The audited zero-margin line does not contradict length 465, but it now has
a very rigid normal form.  In the live \(n_5=133\) and \(n_5=132\) slices a
hypothetical survivor induces:

* a one-jump Johnson flag path through ranks four, five, and six;
* a perfect inclusion matching between all 462 five-sets and all 462
  six-sets, with completion hierarchy
  \((42,42,28,14,5,1)\);
* a spanning two-sided-rainbow Johnson forest with at most six components;
* exact central/external extension labels
  \[
  e_x^{\rm cen}=R_x^{(3)}-1+\mathbf1_{x\in H},
  \qquad
  e_x^{\rm ext}=43-R_x^{(3)}-\mathbf1_{x\in H};
  \]
* at least 319 distinct physical rank-seven hull colors, at most 11 missing
  rank-seven colors, and duplicate excess between 126 and 137; and
* the external Hall/offset capacity
  \[
  e^{\rm ext}(X)\le\min\{E-s_X,E-a_X,d_X\}\le3u_X.
  \]

These statements apply only under their recorded equality-template
hypotheses.  The abstract middle-level forest package is realizable, and all
current scalar, parity, and layer-capacity attacks retain slack.  The missing
global input remains order-sensitive physical synchronization.

## 3. New local theorem A: one prefix replacement plus eleven new entries

Let \(P\) be the certified 465-entry partial word
`k11_upper549_natural_array.txt`.  It misses 13 masks.  Consider every word
obtained by replacing one entry of \(P\) by an arbitrary nonzero 11-bit mask,
then appending eleven arbitrary nonzero entries.

### Theorem A

No word in this family is universal.

### Proof

Fix a modified prefix.  Every mask absent from it must have a witness ending
at one of the eleven new endpoints.  Suffix ORs at one endpoint form an
inclusion chain, so the missing-mask poset must have width at most eleven.

Two independent exhaustive implementations examined all

\[
465\cdot2047=951{,}855
\]

position/value choices.  One computes global interval multiplicities and
subtracts the intervals through the changed position; the other explicitly
enumerates every interval avoiding that position.  They independently use
DFS matching and Hopcroft--Karp matching for the inclusion width.  Both give
the exact distribution

```text
width 11:      2
width 12:  1,926
width 13: 17,980
width 14: 63,929
width 15:361,282
width 16:489,986
width 17: 16,750
```

The only width-feasible modifications are

```text
position 159: 288 -> 800
position 159: 288 -> 808.
```

Both leave exactly

```text
251 428 429 493 607 956 958 1267
1324 1452 1468 1694 1763 1884 1946 1990
```

and have the same terminal suffix-OR state

```text
11,31,63,127,639,1663,1919,2047.
```

The eleven rank-seven holes form an antichain and therefore use all eleven
new endpoints, one each.  The remaining masks can join them in only two
chain-compatible ways:

1. \(428<429<493\), \(956<958\), and
   \(1324<1452<1468\);
2. \(429<493\), \(428<956<958\), and
   \(1324<1452<1468\).

For an ordered suffix state \(C=(c_1\subset\cdots\subset c_s)\), appending
\(x\ne0\) changes it exactly to

\[
\operatorname{dedup}(x,x\vee c_1,\ldots,x\vee c_s).
\]

If one endpoint must carry a fixed required chain, \(x\) is a nonzero
submask of its smallest member.  Thus enumerating every remaining rank-seven
target and every such submask is exhaustive.  Independent memoized DFS and
layer-by-layer BFS traversals both terminate before a tenth appended state:

```text
host(428)=493: layer sizes
1,46,211,690,1837,3058,3316,2341,1206,102,0

host(428)=956: layer sizes
1,46,211,690,1829,3020,3169,2072,1042,84,0
```

Hence neither feasible prefix admits an eleven-entry completion.  This
closes the whole stated family.  It is not an unrestricted lower bound on
\(\nu(11)\).

## 4. New local theorem B: delete one and replace one in the 477-word

### Theorem B

Delete any one entry from `k11_completed_477.txt`.  In the resulting
476-entry word, replace any one remaining entry by any nonzero 11-bit mask.
No resulting word is universal.

### Proof

There are exactly

\[
477\cdot476\cdot2047=464{,}775{,}444
\]

triples of deleted position, replacement position, and replacement value.
For a fixed replacement position, every interval avoiding that position is
unchanged, while every interval through it has final OR \(B_I\vee x\), where
\(B_I\) is the OR of the unchanged entries of that interval.  This gives an
exact finite screen, not a heuristic filter.

The primary implementation uses total old interval multiplicities and
subtracts the affected occurrences.  An independent implementation instead
enumerates all unaffected intervals directly and builds the changed base-OR
family separately.  Both exhaust all 464,775,444 cases and find no universal
word.  Any putative positive output is additionally guarded by direct
quadratic enumeration.

Again, this is a local theorem around the current certificate, not a proof
that every 476-entry word is impossible.

## 5. Reproduction artifacts

```text
1c3f94060091f9dc6d7d1197bb2d4a25f469a453b27adb96a69b0d9dc81a3792  scratch/k11_prefix_replace_append11_screen.cpp
1131e17e49a40c9ed10e2f3e253e943cf060d69c18b69f000e4c2842d1a93ba2  scratch/audit_k11_prefix_replace_append11.cpp
35d39fa9a24fa0551e6d927248e2a2023b5982d59e265733a956b477c1fdb1d0  scratch/k11_append11_exact_dfs.cpp
a5432dbdaeb6ee5c329ce93ba24ad754dc425f23defe120ef20088cd2c5355bc  scratch/audit_k11_append11_exact_bfs.cpp
ecce624c08687500ef5c19775009baae67f71282a2ec0d3c0e302b0a0efaea32  scratch/k11_delete_one_replace_one_screen.cpp
b3a7d6381311b007c33784c675848516a0486e28f28c9d072d7369bae2b5f323  scratch/audit_k11_delete_one_replace_one.cpp
```

The principal width screen and the independent BFS audit were also rerun
under AddressSanitizer and UndefinedBehaviorSanitizer with the same output.
The two suffix-state solvers now reject missing files, non-465-entry inputs,
and entries outside `1..2047`; this closes an audit-interface gap discovered
during the root-level reproduction run.

## 6. Evidentiary gaps and nonclaims

1. `verify_or_array.cpp` does not itself reject out-of-domain input before
   indexing its table.  The explicit word was separately domain-checked,
   and `verify_or_suffix.cpp` does perform the domain check.
2. The root workspace did not contain a built `verify_or_suffix` binary in
   this audit session.  It was freshly rebuilt from the checked-in source and
   passed the 477-word.
3. Many design and runbook files contain an **expected** `PASS` line for a
   hypothetical certificate.  For example, the boundary-reservoir runbook
   explicitly says its branch is impossible and that producing its advertised
   final line would signal an error.  Such strings are not models.
4. Guarded CNF implementation audits establish encoding soundness, not a
   SAT or UNSAT endpoint.  The live five-deletion formula has no terminal
   certified verdict.
5. Several edit-neighborhood UNSAT reports are rigorous only for their named
   roots and edit sets.  They cannot raise the global lower bound.
6. The four-deletion primary aggregate scan has no completed independent
   all-branch aggregate rerun, although its fixed-102 slice, every reported
   survivor, and all survivor UNSAT certificates have separate checks.
7. Some older rank-five audit checkers were explicitly marked stale after a
   zero-state dependency repair.  Only the corrected downstream audits may be
   used.
8. The zero-margin forest/label theorems do not cover every possible
   length-465 branch, and none currently yields a contradiction.

## 7. Exact conclusion

The global numerical interval is unchanged:

\[
\boxed{465\le\nu(11)\le477}.
\]

The new progress is an exact closure of two previously unrecorded
construction neighborhoods.  A successful improvement to 476 must now lie
outside both:

* one arbitrary replacement of the 465-prefix followed by a completely new
  eleven-entry suffix; and
* one deletion plus one arbitrary replacement of the certified 477-word.

The most promising next exact construction step is a two-prefix-replacement
plus eleven-suffix screen, using the same width gate before any completion
solve.  The most promising global lower-bound step remains a genuinely
order-sensitive incompatibility between the physical rank-seven hull system
and the endpoint-ordered middle-level matching.
