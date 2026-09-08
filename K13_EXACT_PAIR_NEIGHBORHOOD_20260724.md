# Exact two-position replacement neighborhoods for the 1851-entry k=13 seeds

Date: 2026-07-24

This note does **not** change the certified finite-k table.  It supplies a
RunPod-ready exact search and proof encoding for a substantially larger local
neighborhood of either 1851-entry near word.

## 1. Exact scope

Fix a nonzero word

\[
A=(A_0,\ldots,A_{n-1}),\qquad 0<A_i<2^k,
\]

and an explicit finite manifest

\[
\mathcal P\subseteq\{(p,q):0\le p<q<n\}.
\]

The generated CNF is satisfiable if and only if there are

* one listed pair \((p,q)\in\mathcal P\), and
* two completely arbitrary nonzero values \(x,y<2^k\),

such that replacing \(A_p\) by \(x\) and \(A_q\) by \(y\) makes every nonzero
\(k\)-bit mask the OR of a contiguous interval.  The values are not restricted
to a palette, to submasks of the two current holes, or to the lifted half.  A
replacement is permitted to equal the old entry, so this is an "at most two
effective edits at one listed pair" neighborhood.

In particular, a manifest containing every pair incident with position 961
closes the complete 961-star around the forward one-hole seed.  The analogous
1470-star applies to the reversed one-hole seed.  These are separate seeds and
must be encoded in separate CNFs.

## 2. Exact provider reduction for a fixed pair

Fix \(p<q\).  An original witness interval avoiding both positions survives
unchanged.  A target without such a witness must be obtained by an interval of
one of three types:

1. it contains \(p\) but not \(q\), and its value is \(b\vee x\);
2. it contains \(q\) but not \(p\), and its value is \(b\vee y\);
3. it contains both, and its value is \(b\vee x\vee y\).

Here \(b\) is the OR of the unchanged entries in that interval.  All distinct
bases of the three types are computed exactly from the monotone left/right OR
chains.  Each chain has at most \(k+1\) distinct values.

For a target \(t\), bases not contained in \(t\) are impossible.  A remaining
base contributes the need

\[
n=t\setminus b.
\]

For the first type the exact condition is \(x\subseteq t\) and \(n\subseteq x\);
for the second it is \(y\subseteq t\) and \(n\subseteq y\); for the third it is
\(x,y\subseteq t\) and every bit of \(n\) belongs to \(x\vee y\).  Superset
needs are dominated and deleted without changing the disjunction.

The CNF has 26 primary value bits at \(k=13\), exactly one pair selector, and a
Tseitin selector for each undominated provider.  Provider selectors imply their
pair selector.  For every target lacking an untouched witness, selection of a
pair implies selection of at least one valid provider.  This is an equivalence,
not a relaxation:

\[
\text{CNF SAT}\iff
\exists(p,q)\in\mathcal P,\ x,y\ne0:\ A[p\leftarrow x,q\leftarrow y]
\text{ is universal}.
\]

The pair selectors use a sequential exactly-one encoding.  The DIMACS header
uses space padding (not zero padding), so `drat-trim` parses it normally.

## 3. Files

* `scratch/k13_exact_pair_neighborhood_cnf.cpp` — integrated CNF generator;
* `scratch/build_k13_pair_manifest.py` — deduplicated anchor-star / position-set
  manifest builder;
* `scratch/decode_verify_k13_pair_neighborhood.py` — independent SAT-model
  decoder and direct quadratic OR verifier;
* `scratch/run_k13_exact_pair_neighborhood.sh` — RunPod search/certification
  wrapper;
* `scratch/audit_k13_pair_neighborhood_logic.py` — exhaustive provider-identity
  audit on small words;
* `scratch/audit_k13_pair_cnf_end_to_end.py` — generated-CNF versus independent
  brute-force audit.

Typical RunPod preparation for the forward seed is:

```bash
python3 build_k13_pair_manifest.py k13_1851_onehole.word forward_961.pairs \
  --anchor 961
g++ -std=c++20 -O3 -DNDEBUG k13_exact_pair_neighborhood_cnf.cpp \
  -o k13_exact_pair_neighborhood_cnf
K13_PAIR_WORK=/root/k13_pair_neighborhood_20260724 \
  ./run_k13_exact_pair_neighborhood.sh \
  forward_star961 5 /root/k13_trim_20260724/k13_1851_onehole.word \
  forward_961.pairs search 131851 86400
```

Use mode `certify` rather than `search` to retain a Kissat DRAT proof and require
an explicit `s VERIFIED` result from `drat-trim`.  A search-mode UNSAT is marked
`UNSAT_UNCERTIFIED` and is not a mathematical certificate.  A SAT result is
decoded, checked by an implementation independent of the CNF reduction, and
then checked again by `verify_or_array`.

The manifest builder also accepts `--positions FILE`, which adds every pair
inside an explicit position set.  This permits one proof to close a selected
multi-anchor or frontier-induced family rather than thousands of unrelated
solver calls.

## 4. Audits completed locally (lightweight only)

The generator compiled warning-free with

```text
g++ -std=c++20 -O2 -Wall -Wextra -Wpedantic
```

The provider reduction was compared with direct interval enumeration on 24
random 3-bit, length-6 words:

```text
PASS words=24 assignments=17640 target_checks=123480
```

The complete generated CNF was then compared with independent exhaustive
two-value/two-position brute force on 80 random 2- and 3-bit instances:

```text
PASS cases=80 sat=61 unsat=19 seed=131851
```

A separate tiny SAT model was decoded to a word and directly verified.

## 5. Audit of the pre-existing k=13 neighborhood tools

### Exact one replacement

`scratch/k13_exact_one_replacement.cpp` is exact for all 1851 positions and all
8191 nonzero replacement values of its input seed.

* `common_left=max(left)` and `common_right=min(right)` characterize exactly
  whether every old witness contains the edited position.
* The distinct left/right OR chains enumerate every base of an interval through
  that position.
* The minimal-need dominance test is exact.
* Every reported hit is checked again by direct interval enumeration.

Its no-hit result says nothing about two simultaneous arbitrary replacements.

### Third-edit frontier wrapper

`scratch/run_k13_third_edit_frontier.sh` is exact for the following narrower
portfolio: start from the fixed one-hole seed, apply one frontier-listed edit,
then try every possible final single replacement.  It does not include an
intermediate state with two or more holes that a final edit might repair.

### Old `k13_two_repair.cpp`

That program restricts positions to the lifted suffix and values to a small
submask palette tied to 5712/5972.  It is a valid search heuristic, not an exact
arbitrary two-edit neighborhood.

### Near-word builder

`scratch/build_k13_one_interface_near.cpp` emits exactly

\[
926+1+(926-2)=1851
\]

entries: the lower 926-word, the new singleton 4096, and 924 transformed base
entries after two deletions.  Its corrected writer no longer emits the former
extra high singleton.

## 6. Audit of the relative-bit-permutation family

`scratch/k13_relative_bitperm_trim.cpp` is source-level correct for each
generated 12-bit permutation:

* it exhausts all \(\binom{926}{2}\) deletion pairs;
* the residue evaluator covers exactly intervals wholly in the high block and
  intervals crossing the unique lower/high interface;
* score 4096 is equivalent to coverage of every high-bit target, while the
  unchanged lower word covers every low target;
* the output length is \(926+1+924=1851\), and the wrapper independently checks
  it.

The `array<int,16>` OR frontiers are safe because a strict OR chain on 12 bits
has at most 13 distinct values.

Important scope limitation: after the identity map, the program generates
independent pseudorandom shuffles.  Duplicates are possible, and even setting
`PERMUTATIONS=12!` does **not** enumerate all 12! maps.  Therefore a no-hit run
is exact over every deletion pair for the actually generated permutation list,
but is not an exhaustive no-go theorem for all relative bit permutations.

## 7. Certified production-star results

Both recommended 1,850-pair stars were subsequently solved UNSAT and checked
independently with `drat-trim`.  These are exact neighborhood exclusions, not
global lower bounds.

### Forward one-hole seed, complete position-961 star

```text
seed sha256       3c1b70651f319b9a8c58adba16308c6be88157d40721271aef4770e1eeb78225
pair-manifest     1,850 pairs
variables         80,423
clauses           886,887
CNF sha256        fd627eb80a600a6d3238b77b2c18d2b85218741c81894570c9696183a90f1927
map sha256        cf864e1b55743846faaf77ac245c891a46b4fb67bf8c5acdaf7115b59c26b576
DRAT sha256       7fe2f41cddc408315362e9e56cad0597b7c7759be26fc6bc616587b14f58b1f1
check-log sha256  026013ab151c3e9a134cfe5e639c2a2a97bb477e729947d0b7f767eedebcbbb0
drat-trim         s VERIFIED (93.176 seconds)
```

The checked statement is: after starting from this one-hole seed, no word
obtained by assigning arbitrary nonzero values to position 961 and any one
other position is universal.

### Reversed one-hole seed, complete position-1470 star

```text
seed sha256       15e15d71856823fda819a4303cb4fb46d45d1f603038f4f30f882dc1b9a63d23
pair-manifest     1,850 pairs
variables         76,773
clauses           842,625
CNF sha256        856eb04d6325c7dd9283d1a525f92797600a674cb4219c3a4783bded41255ae9
map sha256        66d6d2950c367273b3aeab32991f75918a23a03e5be4be07a940f13fdef45f50
DRAT sha256       5309b3e751f6d8f7685fb1d30da9cb4e63743cad70cdcd07160db9c86e237a04
check-log sha256  e71242de62ba73510acbfcd14ae973e720f0c6557840b98b07b47eb008f2317a
drat-trim         s VERIFIED (204.421 seconds)
```

The analogous arbitrary two-position exclusion holds for position 1470 of
the reversed one-hole seed.

These proofs rigorously close 3,700 listed position pairs, each with all
(8191^2) possible nonzero replacement-value assignments represented
symbolically.  They do not exclude a two-position edit avoiding the named
anchor, a three-distinct-position edit, or another 1,851-entry architecture.
Accordingly the certified finite-(k) table is unchanged.
