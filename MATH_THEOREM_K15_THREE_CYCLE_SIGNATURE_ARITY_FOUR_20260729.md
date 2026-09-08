# Exact arity-four lower bound for the `k=15` three-run move catalogue

Date: 2026-07-29

Status: exact finite theorem for the 4,037 balanced run-end 3-cycles of the
frozen resident strict-spiral seed.  It is not a lower bound for arbitrary
carrier moves and does not settle `k=15`.

## 1. Signed invariant

For a balanced three-run move `g`, let

\[
\Sigma(g)=(\Delta M(g),\Delta L_1(g)),          \tag{1.1}
\]

where `Delta M` is the signed load vector on middle translation orbits and
`Delta L_1` is the signed load vector on q1-intersection translation orbits.
The central two actions are free at `k=15`, so these vectors have integral
orbit-unit coefficients.

Every valid strict carrier has both vectors zero.  If moves have pairwise
disjoint q1-affected quotient support, their physical middle and q1 changes
are disjoint and

\[
\Sigma(g_1\circ\cdots\circ g_t)
=\Sigma(g_1)+\cdots+\Sigma(g_t).                \tag{1.2}
\]

Thus a support-disjoint repair requires a zero-sum collection of signed
vectors.  The previous exhaustive audit already established that no single
move has zero signature and no two signatures are inverses.

## 2. Frozen catalogue

The exporter reconstructs the resident carrier from explicit stable choices,
enumerates the 4,037 legal directed three-cycles, and records:

```text
move id;
three run ids and lifted endpoints;
q1-affected quotient support;
sorted signed middle/q1 orbit terms.
```

Files:

```text
scratch/export_k15_three_cycle_signatures_20260729.py
scratch/k15_three_cycle_signatures_20260729.txt
scratch/k15_three_cycle_signature_replay_20260729.json
scratch/k15_three_cycle_signature_manifest_20260729.json
```

The text catalogue SHA-256 is

```text
cbae9665d9f882360ee7ae61acf1c1e78e33abefb21d33873b56554beab56d90.
```

## 3. Exact `2+1` meet in the middle

For every unordered pair `i<j`, the C++ checker computes the additive
128-bit hash of

\[
-\Sigma(g_i)-\Sigma(g_j)
\]

and looks it up among all singleton signatures.  Hash equality is only a
prefilter: every hit is verified by an exact merge of the sorted integer term
vectors.  A true zero sum necessarily has equal additive hashes, so hashing
cannot cause a false negative.  The checker separately tests pair inverses,
run-disjoint triples, and the stronger pairwise q1-support-disjoint triples.

The exhaustive counts are

```text
moves                                      4,037
unordered pairs                        8,146,666
exact zero-signature pairs                     0
pair hashes matching a singleton target       0
exact zero-signature triples                   0
run-disjoint zero triples                      0
q1-support-disjoint zero triples               0.
```

The zero hash-candidate count is stronger than a post-filter zero: no pair
even has the two additive hashes required by a third catalogue signature.

### Theorem 3.1

No collection of at most three distinct moves from the frozen 4,037-move
catalogue has signed middle+q1 sum zero.  In particular, every
q1-support-disjoint collision-neutral composition in this move family uses
at least four balanced three-run moves.

### Proof

Each exported vector is nonzero, excluding arity one.  The exact pair loop
finds no inverse pair.  The meet-in-the-middle loop checks all
`C(4037,2)=8,146,666` pairs and finds no singleton equal to the negative pair
sum, excluding every unordered triple.  Equation (1.2) gives the
support-disjoint conclusion.  □

This does **not** exclude two or three overlapping moves: their sequential
effect can be nonlinear because a later move sees masks changed by an earlier
one.  It also says nothing about quotient-edge switches outside this scalar
run-end catalogue.

## 4. Remote CPU run

The full enumeration was run CPU-only on `ssh h100` (`arboghast`, 64-core
EPYC host); no GPU was used.

Remote directory:

```text
/home/amodo/or15/three_cycle_mitm_20260729
```

Exact command:

```bash
g++ -O3 -std=c++20 -march=native -DNDEBUG \
  k15_three_cycle_signature_mitm_20260729.cpp \
  -o k15_three_cycle_signature_mitm

/usr/bin/time -v ./k15_three_cycle_signature_mitm \
  k15_three_cycle_signatures_20260729.txt \
  k15_three_cycle_signature_mitm.result.json
```

Compiler and resources:

```text
g++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
wall time       0.13 s
user CPU        0.12 s
maximum RSS     5,632 KiB
exit status     0
```

Frozen local copies:

```text
scratch/k15_three_cycle_signature_mitm_20260729.cpp
scratch/k15_three_cycle_mitm_remote_20260729/
scratch/test_k15_three_cycle_signature_mitm_20260729.py
```

Important hashes:

```text
8909d2b46c0d2ff41f4e45e1e2f0b9d6bc58c966c75ac09d797cc3c9516f09d4  C++ source
cbae9665d9f882360ee7ae61acf1c1e78e33abefb21d33873b56554beab56d90  signature catalogue
324eec348c33b7eaeb49ad72b68de56900f1b0d5dcdd4d7c2e7eb5f4da693327  result JSON
eb710a31184e0b32dc13e18a4f1d67a705feb78a3c6b0b26903749feba719c08  time/stderr log
```

The regression test includes a synthetic positive instance with exactly one
support-disjoint zero triple, then checks the frozen `k=15` negative result:

```bash
python3 scratch/test_k15_three_cycle_signature_mitm_20260729.py
```

It reports

```text
PASS synthetic-positive and frozen-k15-negative.
```

## 5. Consequence

There is no triple to replay, so q2/q3/upper/compiler scoring is vacuous for
proof-safe candidates.  The scalar run-end neighborhood has now failed at
arities one, two, and three for an exact algebraic reason, not because an
optimizer missed a state.

The next bounded scalar experiment, if pursued, is arity four using a `2+2`
meet in the middle, with q1-support disjointness imposed before physical
replay.  More promising mathematically is to leave the scalar endpoint family
and generate alternating quotient-Johnson circuits whose middle and q1
conservation is built in rather than recovered by cancellation.
