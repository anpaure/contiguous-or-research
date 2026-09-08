# Audit of the variable-delete recency CNF

## Verdict

No soundness or completeness flaw was found in

```text
scratch/delete_append_recency_cnf.cpp
```

The formula is an exact encoding of:

```text
delete exactly d entries from the fixed nonzero prefix,
append exactly q nonzero entries,
cover every nonempty mask by a contiguous OR interval.
```

The selected rank AMOs and consecutive-rank label channels are redundant
propagation constraints and preserve satisfiability.

The supplied finite checker passes 1,601 exhaustive/sampled instances.  Its
one coverage gap is that it always sets `history_cap=8`, larger than every
small tested witness cap, so it does not exercise the generator's fallback to
the unbounded `seen` state.  A separate exhaustive run at history caps 0, 1,
and 2 passed 1,074 additional small instances.

No source edit was made during this audit.

## 1. Exact deletion counter

Let `D_i` be the deletion variable of original prefix position `i`.  After
each position, state literal `C_j` means exactly `j` deletions have occurred.
Initially only `C_0` is true.

For each active state, the generator forces

```text
C_j and not D_i  -> C'_j,
C_j and D_i      -> C'_{j+1}.
```

Deleting from state `d` is explicitly forbidden.  The successor states have
an at-most-one constraint.  Inductively, one successor is forced and all
others are false, so the counter stays exactly one-hot.  Finally `C_d` is
forced.  Therefore precisely `d` original positions are deleted.

The sequential AMO circuit is the standard sound prefix encoding.  Its
auxiliary prefix variables need not be functionally unique; every at-most-one
input assignment has an extension, which is all this use requires.

## 2. Gated fixed-prefix recency

The recency state contains:

- `seen[b]`: coordinate `b` has appeared in a retained physical entry;
- `newer[a,b]`: the last retained occurrence of `a` is strictly later than
  that of `b`;
- `recent[b,age]`: `b` occurs in the retained physical entry at the specified
  age, truncated at `history_cap`.

At a fixed prefix position:

- if it is deleted, all three state families are preserved exactly;
- if it is retained, present coordinates become seen, pairwise recency is
  updated with correct ties, and the recent register shifts by one physical
  position.

The special pair cases are correct:

```text
second present: kept -> newer=false; deleted -> preserve;
first present only: kept -> newer=true; deleted -> preserve;
neither present: preserve.
```

If both coordinates are present, the first case sets both strict directions
false, correctly representing a tied last-occurrence block.

The `make_mux` simplifications for constant inputs agree with the general
multiplexer in all four constant cases.

## 3. Append recurrence

For an appended mask with bits `x_a,x_b`, the new strict comparison is

```text
newer'(a,b) =
    true          if x_a=1 and x_b=0,
    false         if x_b=1,
    newer(a,b)    if x_a=x_b=0.
```

The four emitted clauses are exactly the truth table of this recurrence.
The seen state ORs in each new bit, and the recent register shifts with the
new entry at age zero.  A clause requires every appended entry to be nonzero.

## 4. Occurrence semantics and endpoint guards

At any retained or appended endpoint `e`, a nonempty target `T` is a suffix
OR exactly when

```text
every bit of T has occurred, and
last_e(b) > last_e(c) for every b in T and c outside T.
```

The occurrence flag implies precisely these comparisons.  When the general
containment cap `L` is at most `history_cap`, the seen requirement is replaced
by the stronger exact condition that every target bit appears in one of the
last `L` retained physical entries.  This selects a genuine capped witness.

When `L>history_cap`, the generator uses `seen`.  This does **not** introduce
a false target occurrence: seen plus the strict recency cut still defines a
genuine suffix OR, possibly longer than `L`.  It merely omits a redundant cap
that every universal completion is known to satisfy somewhere.

An occurrence at an original position implies that position is not deleted.
The state after a deleted position duplicates the previous compressed state,
but its endpoint is unphysical and cannot be selected.  Later retained states
correctly treat deletion gaps as absent physical positions.  Append endpoints
need no guard.

Every target has an at-least-one selected endpoint.  Conversely, any valid
completion can select one genuine endpoint for each target.  Thus target
coverage is exact.

## 5. WLOG propagation constraints

Selecting exactly one occurrence endpoint per target is WLOG: extra witnesses
are irrelevant to existence.

At a fixed endpoint, suffix ORs form one inclusion chain.  Hence at most one
selected target of any fixed rank may use that endpoint.  The optional
same-rank AMOs are sound.

For selected consecutive ranks, the lower target must be contained in the
upper target.  The label channel enforces this bitwise.  If one of the two
ranks has no selected target at an endpoint, its labels are free: choose all
zeros below a selected upper label or all ones above a selected lower label.
Across several absent ranks, free labels can interpolate whenever the actual
selected endpoint targets are comparable, which the recency semantics already
guarantees.  Therefore the channel does not remove a completion.

## 6. Finite checker

The supplied checker

```text
scratch/audit_delete_append_recency_cnf.py
```

independently enumerates every exact deletion set and every append word for:

- all nonzero prefixes through length three at `k=1`;
- all nonzero prefixes through length four at `k=2`;
- all prefixes through length two and a deterministic spread of length-three
  prefixes at `k=3`.

It compares literal brute-force existence with the generated CNF's SAT
status.  For every SAT result it decodes the chosen deletion set and append
entries and rechecks the completed word by direct quadratic interval OR
enumeration.  The durable output is

```text
PASS exhaustive_and_sampled_instances=1601
```

An additional no-edit audit invoked the same generator with history caps
0, 1, and 2 over exhaustive `k=1,2` families and obtained

```text
PASS fallback_history_caps instances 1074
```

This closes the only material branch not exercised by the supplied checker.

## 7. Current hashes

```text
5fa707184dbec376f20566a885d9acc102bc21ba2901fbff5ff8278e5b5465b6  scratch/delete_append_recency_cnf.cpp
bf6368adf5843c531a3f588764147dd5385bed19cc3ae3c648dd394f977ec6ab  scratch/audit_delete_append_recency_cnf.py
```

## 8. Full delete-five build audit

The production parameters are

```text
k=11
prefix_length=465
deletions=5
append=16
amo_ranks=5,6
history_cap=15
```

The generated formula at

```text
scratch/k11_length476_five_deletion_variable_20260724/delete5_append16.cnf
```

has exact inventory

```text
variables                     2,523,666
clauses                      43,004,593
literals                    131,092,440
empty clauses                         0
file bytes                 1,000,837,997
SHA-256
7362799ace9a7d8062658f646a5a079858c0c14263ac116e4fff161d6faf0f55
```

The independent streaming parser

```text
scratch/audit_dimacs_stream.cpp
```

confirmed that the declared and actual clause counts agree, the maximum
referenced variable is exactly 2,523,666, every clause is terminated, and no
literal is out of range.  Its source SHA-256 is

```text
c1086b85a0447a31477e5af1ea978ab713380a3137e3c704c6616e21e394a243
```

The 3,286-byte map has SHA-256

```text
262e23f644625d61b1dad97fd1b0507a84986debcea7e49cc7f14ebdd005b64c
```

Independent parsing verified:

- the five metadata fields exactly match the production parameters;
- there are 465 deletion variables, exactly `1,...,465`;
- there are 16 append rows in endpoint order, each with 11 variables;
- all 641 exported variables are positive, unique, and within the DIMACS
  variable range.

Finally, the source was separately compiled with `clang++ -O2`; that binary
has SHA-256

```text
faf85c717546376b20e0003d1915ac9c9ee3c8b7fceb284693c1f695e21327e7
```

instead of the production binary hash

```text
6ef35d27ff056be36b60f644c5c24b9e874fb5b47487a216781e5a336bcf0546
```

The independent binary regenerated both the one-billion-byte CNF and the map
byte for byte: `cmp` reported no difference and both regenerated files have
the same hashes above.

## 9. Scope

This audit proves that the generated CNF is the correct finite decision
problem.  It does not establish that the full `k=11,d=5,q=16` formula is SAT
or UNSAT, nor that solving it will be computationally easy.  It does justify
using one variable-deletion formula in place of enumerating
`C(465,5)` fixed deletion branches.
