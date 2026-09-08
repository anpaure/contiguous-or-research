# Audit of the `Q_9 -> Q_11` wreath-insertion search

## Verdict

`Q11_WREATH_INSERTION_SEARCH.md` is correct for the candidate family it
defines.  The literal insertion family contains 1,260 dihedral cycles and has
no exact middle-layer factor.  The conclusion is supported by a direct
three-base combinatorial certificate; it does not depend on solver trust or
on the optional vertical clauses.

The conclusion must not be enlarged: it rules out only cycles obtained by
inserting symbols 10 and 11 while preserving one of the fourteen old cyclic
orders.  General `Q_11` wreath factors remain possible.

## 1. Candidate-family audit

The independent script
`scratch/verify_q11_wreath_insertion_obstruction.py` reconstructs candidates
without importing the SAT generator.

For one old cycle:

* different insertion gaps give `9*8=72` labelled cycles;
* a common gap gives `9*2=18` cycles;
* dihedral canonicalization leaves all 90 distinct.

Deleting 10 and 11 recovers the old dihedral cycle, so candidates belonging
to different source rows cannot collide.  The script obtains exactly
`14*90=1260` candidates.

It also checks that every candidate is an eleven-symbol permutation and that
the complete family has nonzero incidence on every target through rank five.
At rank five the target-incidence range is 20 through 60, so the UNSAT result
is not a zero-column artifact.

## 2. Counting reduction audit

For a candidate, let `a` count length-five windows containing both new
symbols.  Each new symbol lies in five windows.  Therefore:

```text
both new:        a
exactly one:     5+5-2a = 10-2a
neither:         11-a-(10-2a) = a+1.
```

An exact cover of the 252 one-new and 84 two-new targets therefore selects
exactly 42 cycles.

Every one-new window descends to a cyclic rank-four interval of its source
row.  Rank-four exactness of the source factor makes that row unique.  If
`n_b` cycles are selected above source row `b`, their two-new count is
`5*n_b-9`.  Those windows descend to at most nine cyclic old triples and must
be distinct, so `n_b<=3`.  Fourteen such bounds and the forced total 42 give
`n_b=3` for every row.  This reduction is exact and uses no lower-rank
coverage hypothesis.

## 3. Local enumeration audit

For each source row, the independent checker:

1. forms the eighteen tagged old rank-four targets;
2. recursively enumerates exact covers of them by exactly three candidates;
3. retains a cover only if its six two-new old triples are distinct;
4. complements those six triples inside the source row's nine cyclic
   triples.

It obtains 60 clean candidate triples and 30 distinct omission packets, every
packet occurring twice.  Converted to cyclic position indices, every packet
has gap multiset `1,1,7`, `1,2,6`, or `3,3,3`; conversely all 30 such packets
occur.

The old factor's rank-three incidence histogram is independently recomputed
as

```text
multiplicity 1: 44 targets
multiplicity 2: 38 targets
multiplicity 3:  2 targets.
```

Discarding packets that omit a multiplicity-one target leaves domain sizes

```text
1,2,9,10,6,14,5,4,3,20,2,4,6,3,
```

matching the main note and certificate.

## 4. Certificate audit

Only three domains are needed.

* Row 1 has the unique packet `{456,567,678}`.  The target 129 occurs only in
  rows 1 and 4.  Since row 1 retains it, row 4 must omit it.
* Row 11 has packets `{267,148,478}` and `{148,478,139}`.  The target 356
  occurs only in rows 4 and 11.  Since row 11 retains it in either case, row 4
  must omit it.
* Direct inspection of the ten row-4 packets shows that none contains both
  129 and 356.

For a target appearing in two source rows, exactly one row must omit it;
otherwise its two-new lift is covered either twice or zero times.  The two
forced omissions at row 4 are therefore incompatible.  This is a complete
finite proof of middle-layer UNSAT.

Running

```text
python3 scratch/verify_q11_wreath_insertion_obstruction.py
```

prints `UNSAT PASS` after checking all assertions.

## 5. SAT audit and limitation

The search generator produces:

```text
middle only       14,658 variables  40,194 clauses
with ranks 1--4   14,658 variables  40,755 clauses.
```

Kissat reports UNSAT for both.  A solver-emitted DRAT trace is archived for
the middle instance, but no separate DRAT checker is claimed here.  This is
not a trust gap because the direct omission certificate proves the same
UNSAT statement independently.

No assertion in the note establishes the nonexistence of:

* a general exact wreath factor on eleven coordinates;
* a lift that changes the cyclic order of old symbols;
* a lift that couples or switches different parent rows;
* a length-465 universal OR word.

The result is therefore a valid no-go theorem for one sharply defined
inductive construction, not a resolution of the original OR problem.
