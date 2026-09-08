# Exact Waksman/Kissat encoding of the compact even-
\(K\) catalogue

Date: 2026-07-29

## Result

The default audited compact canonical-ID model in
`scratch/search_even_eager_canonical_id_20260729.py` has an exact CNF
projection that needs neither canonical-min integer variables nor
`AllDifferent`/`Element` products.

The implementation is

```text
scratch/search_even_eager_benes_cnf_20260729.cpp
scratch/decode_even_benes_kissat_20260729.py
```

For \(K=16\), widths `2,3,4,6,9,13`, and the safe middle-origin
symmetry break, the exact source count is

```text
3,984,274 variables
15,455,173 clauses
44,812,655 literal occurrences
85,914 Waksman switches
7,722 independently phased physical words
```

The count-only construction took 1.08 seconds and about 14 MB peak RSS on
the local machine.  It generated no CNF and performed no solve.  This is a
large propositional model, but its storage is predictable and is many orders
smaller than the old rotated-target selector expansion (which had
122,731,752 upper selector variables before their implication rows).

No \(K=16\) solve has been launched.  An UNSAT result from this model would
mean only

```text
UNSAT_CATALOGUE_RESTRICTED:
no connected unit-voltage (c,t) carrier whose upper witnesses all use
the explicit width catalogue 2,3,4,6,9,13.
```

It would not be an all-carrier or all-word theorem.

## The partial-permutation lemma

Let \(v_1,\ldots,v_M\in\{0,1\}^K\) be the actual quotient windows for one
gate, let \(\rho\) rotate the first \(K-1\) coordinates, and let
\(R=\{r_1,\ldots,r_D\}\) be the canonical representatives of the required
orbits, where \(D\le M\).  Then the following are equivalent.

1. Every orbit represented in \(R\) is met by some \(v_i\).
2. There are phases \(a_i\in\mathbb Z_{K-1}\) and a permutation \(\pi\) of
   the \(M\) phased objects such that
   \[
   (\pi(\rho^{a_1}v_1,\ldots,\rho^{a_M}v_M,0,\ldots,0))_j=r_j
   \quad(1\le j\le D).
   \]

For `(1) => (2)`, choose one distinct occurrence of every required orbit,
rotate it to its canonical representative, and permute those occurrences to
the designated outputs.  The remaining actual words fill the other outputs.
For `(2) => (1)`, every required representative came from a distinct actual
input; rotating it back gives an occurrence of its orbit.

A recursive Waksman network realizes every permutation on an arbitrary
number \(M\) of wires.  Its first and last stages pair the inputs/outputs,
and its two recursive subnetworks have sizes \(\lceil M/2\rceil\) and
\(\lfloor M/2\rfloor\).  The standard alternating-cycle routing proof gives
rearrangeability.  Bit-blasting a switch on a \(K\)-bit word costs one control
and two multiplexers per bit.  A four-stage barrel rotator chooses a phase in
\(\mathbb Z_{15}\); phase `15` is forbidden.

The model applies this lemma independently to:

| family | actual words | switches | required outputs |
|---|---:|---:|---:|
| middle | 858 | 8078 | 858 |
| q1 | 858 | 8078 | 764 |
| q2 | 858 | 8078 | 536 |
| upper, six widths | 5148 | 61680 | 1763 |

This is why target-by-window selectors are unnecessary.  The phases are
auxiliary existential witnesses; they do not change `(c,t)`.  They are also
independent between gates, exactly as canonicalization was.

## Equivalence to the canonical-ID projection

The base CNF reproduces the nonredundant CP constraints:

- `sum(t)=N/2` and every middle column has rank `r`;
- forbidden cyclic runs of lengths `1..d` in `c` and `t`;
- exact one start and one end per quotient class;
- the top-run cap;
- optionally, the same safe fixed middle origin.

Boolean bitonic networks encode cardinalities.  The q1 physical words have
rank exactly \(r-1\), and q2 words have rank in
\(\{r-2,r-1\}\), matching the canonical-ID domains.  Upper words contain
their first rank-\(r\) column, so their ranks are automatically in
`r..K`.

The four partial-permutation constraints are equivalent to, respectively,

- middle canonical IDs forming the complete middle-orbit permutation;
- every required q1 ID occurring;
- every required q2 ID occurring;
- every required upper ID occurring in the stated catalogue.

The top-capacity inequalities and aggregate start/end identities omitted
from the CNF are redundant consequences of these exact constraints.  For
example, different required top-orbits must occupy different top-containing
physical words in the partial permutation.

## Independent \(K=8\) validation

The generator produced

```text
9,070 variables
34,293 clauses
98,333 literal occurrences
```

Kissat returned SAT remotely on the H100 host's CPU (24.34 seconds, about
33 MB peak RSS under a 1 GB address-space cap).  The independent physical
decoder then checked all of the
following, without consulting any network variable:

```text
rank_bad_count       = 0
middle_unique        = 70 / 70
johnson_bad_count    = 0
residence_bad_count  = 0
q1_rank_bad_count    = 0
missing middle       = 0
missing q1           = 0
missing upper catalogue = 0
missing arbitrary upper = 0
```

The decoded positive artifact is
`scratch/even_waksman_k8_20260729_PASS.json`.

Pinning the previously known compact \(K=8\) `(c,t)` values made the routing
CNF solve in 0.008 seconds, an additional check that the network accepts the
known projection.

For \(K=10\), the final Waksman model has 47,328 variables and 183,673
clauses.  An earlier padded-network revision did not finish a deliberately
capped 30-second lightweight check.  That obsolete result is `UNKNOWN`, not
UNSAT and not evidence against equivalence.  It nevertheless warns that the
permutation extension has more SAT symmetry than native CP `Element`; the
encoding solves the memory problem, not automatically the search-order
problem.  The final K10 Waksman model has only been counted, not solved.

## Reproduction

```bash
c++ -O3 -DNDEBUG -std=c++17 \
  -o /tmp/even_benes scratch/search_even_eager_benes_cnf_20260729.cpp

# exact count only; no solver and no large file
/tmp/even_benes 16 --count-only --fix-middle-origin

# small validation
/tmp/even_benes 8 --cnf /tmp/even_benes_k8.cnf --fix-middle-origin
kissat --quiet /tmp/even_benes_k8.cnf > /tmp/even_benes_k8.model
python3 scratch/decode_even_benes_kissat_20260729.py \
  8 /tmp/even_benes_k8.model \
  --output-json scratch/even_waksman_k8_20260729_PASS.json
```

For \(K=16\), generation and solving belong only on the H100 host's CPU and
only after checking current memory/swap pressure.  The generator is streaming
and deterministic, but Kissat should still be placed under an explicit RSS
cap.  A SAT output must be decoded and physically audited before it can be
used; a carrier PASS still does not authorize the compiler by itself.

The guarded launcher is
`scratch/launch_even_waksman_k16_capped_20260729.sh`.  It refuses to run while
the older compact CP-SAT K16 process exists, below 32 GiB available memory, or
below 2 GiB free swap.  It checks the source hash and exact count fingerprint,
caps generation at 2 GiB, caps single-threaded Kissat at 16 GiB, and decodes a
SAT model through the independent physical audit.  It has not been launched.
