# K17 h1 ordinary-q1 closure by alternating circulations

## Status

This note freezes a positive finite construction, not a `k=17` word.

For the authenticated `k=17`, `h=1` augmented rank-8/rank-9 incidence
factor, there is now a connected degree-exact model satisfying every frozen
guard and covering all

\[
  19,412
\]

required ordinary rank-10 colours (the rank-10 masks not containing the
fixed exceptional root `D`).  An independent extension and exact q1 replay
returns

```text
PASS_K17_H1_EXACT_Q1_CUT required=19412 covered=19412 missing=0 cut_literals=0
```

The other 36 rank-10 masks, residence, ranks 11 and above, source letters,
and the lower compiler are outside this statement.

## 1. Alternating-circulation reduction

Let `Q` be an ordinary rank-8 root.  Its two selected incident rank-9 owners
are

\[
  Q+a,\qquad Q+b,
\]

and its ordinary q1 colour is

\[
  U(Q)=Q+\{a,b\}.
\]

Replacing the selected incidence `Q--(Q+a)` by the unselected incidence
`Q--(Q+c)`, while retaining `Q--(Q+b)`, is represented by a directed arc

\[
  Q+a\longrightarrow Q+c
\]

on the rank-9 owner shore.  Its signed q1 current is exactly

\[
  [Q+\{b,c\}]-[Q+\{a,b\}].                 \tag{1}
\]

Consequently, a directed owner cycle whose arcs use distinct roots is an
alternating circuit in the original incidence graph.  Toggling the circuit
preserves every root degree and every owner degree.  Formula (1) gives its
complete signed effect on the 19,412 q1 multiplicities before any mutation
is made.

This contains alternating `C6` and star-`C8` moves as its length-three and
special length-four cases, but also exposes non-star `C8`s and arbitrarily
long circuits.

Every promoted circuit was then checked literally against:

1. the two protected boundary incidences;
2. all 16,261 frozen incidence/pair clauses;
3. exact q1 provider multiplicities;
4. exact connectivity of the 48,620-vertex augmented factor.

No score surrogate is used for promotion.

## 2. Exact finite descent

The starting connected incumbent covered 19,341 colours and had 71 holes.
The repair proceeded through four successively larger exact move classes.

### 2.1 Complete current-state `C6`/star-`C8` catalogue

At the initial state the exhaustive catalogue contained:

- 2,333,760 rank-7-core `C6` geometries;
- 47,072 alternating unprotected `C6`s;
- 9,027 guard-safe `C6`s;
- 12,252,240 four-petal star-`C8` cyclic geometries (all three cyclic
  orders of each four-set, not one sampled order);
- 55,912 alternating unprotected star-`C8`s;
- 5,612 guard-safe star-`C8`s.

Thus 14,639 signed guard-safe moves were catalogued exactly.  Direct moves
and all root-disjoint compatible pairs were replayed.  Repeating this exact
descent reduced 71 holes to 26, where the complete `C6`/star-`C8` class had
no improving move or compatible pair.

### 2.2 Loss-safe arbitrary alternating circuits

For every residual arc, first require that its removed q1 colour have
multiplicity at least two.  A forced arc installs a missing colour; a return
path in the contracted owner digraph closes an alternating circuit.  Exact
guard and connectivity replay retained only lossless improvements.

This escaped the 26-hole local optimum and monotonically reduced it to five
holes.  At that point the loss-safe residual graph had 129,325 arcs and 13
forced missing-colour installs, but none had any return path even with depth
128.  This is an exact obstruction to this restricted residual class, not
to the full factor problem.

### 2.3 Weighted and transported-hole circuits

The full residual graph has 340,305 arcs.  Allowing at most two temporary
unique-provider removals, followed by exact signed replay, reduced five
holes to three.

At the three-hole plateau a connected neutral circuit transported the hole

\[
  109870\longrightarrow109994
\]

without changing total coverage.  This changed the residual reachability
class.  Subsequent exact weighted circuits reduced three holes to one.  The
last missing colour was `32058`.

### 2.4 Two-debt closure

A residual state `(T,d_1,d_2)` records the current owner and at most two
temporarily uncovered unique q1 colours.  An arc deletes its new colour from
the debt set, when present, and inserts its old colour exactly when the old
provider was unique.  Reaching the forced tail with empty debt gives a
candidate positive circulation.  The candidate is still replayed from the
literal factor, so the debt automaton is only a search accelerator.

For the final mask `32058`, the bounded two-debt search saw:

- 20 forced installs;
- 11 return paths before the per-source node cap;
- 11 root-simple, guard-safe candidates;
- 6 connected positive candidates.

A length-seven alternating circulation closed the last hole.  The resulting
factor covers 19,412/19,412 required ordinary q1 colours.

## 3. Frozen authoritative artifacts

H100 root:

```text
/home/amodo/or15/work/root_k17_q1_targeted_static_20260802
```

Primary files and hashes:

```text
q1zero.independent.model
  b1fc0d9ca69c8411aad96557f5a47fe031616c88644f5d5691bec705b2b61a31
q1zero.independent.extended.model
  f544cbc2a6c3bf9f9d7500202b4a60cb06660c3b5a1cdd382daec4d8dd4bbb90
q1zero.independent.q1cut.out
  f9333055d70af89c45d08c7272eb779e92055cee9e09e135390faacf27c2d573
debt2_1_cap2m.audit.json
  1065dd9ecf422a806acc361162f73606d25b15b08d1e83777a783a3d131b54ad
debt2_1_cap2m.debt2_cycles.tsv
  3c5a86ac5dda09536a352ef53ad3cf7ae44bad424a591a88938344de08c26032
src/search_k17_h1_q1_targeted_debt2_20260802.cpp
  29d0e6dc52c5dac13b1d81e374119fa2542935420465127228cadc85c71b0d18
targeted_debt2
  d4dbaa52e9b1ab12cf6c25fbed26f9e3594a2098222d9e85f10df37c95f2eae4
q1zero.passive.audit.json
  b7d78582ca8f0aaeddbbb0413f00a95b569f2ba7c577dedcd94e57997684f0c2
```

The complete frozen manifest is `q1zero.manifest.sha256` in the same root.

## 4. Exact scope

Proved for this model:

- augmented factor connected;
- prescribed root and owner degrees exact;
- both protected boundary incidences retained;
- every frozen guard clause satisfied;
- every required ordinary rank-10 q1 colour covered.

The passive two-orientation replay remains negative downstream.  It reports
5,584 cyclic short ordinary residence components; the best linear opening
has residence count 5,586 and rank-10-through-13 upper holes
`[22,1533,286,7]` (total 1,848).  Its generated clauses are named
`q1zero.passive.cuts.DO_NOT_ADD.cnfpart` and are not part of the construction.

Not proved here:

- positive residence floor four;
- coverage at ranks 11 through 17;
- a literal depth-three source word;
- the strict-lower compiler;
- `nu(17)=24313`;
- any all-dimensional existence theorem.

The mathematical gain is narrower but reusable: arbitrary alternating
incidence circuits, searched through bounded q1-debt states, are an exact
actuator class strictly stronger than local `C6`/star-`C8` descent.  They
close the central/ordinary-q1 gate on the authenticated `k=17`, `h=1`
factor without displacing a single final colour.
