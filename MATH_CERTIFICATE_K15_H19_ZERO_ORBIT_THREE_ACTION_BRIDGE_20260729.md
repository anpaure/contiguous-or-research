# The Hall-19 zero orbits and the exact three-action quotient bridge

Date: 2026-07-29

Status: exact finite certificate.  This note identifies the six degree-zero
targets of the authoritative Hall-19 compiler, proves that they lie in six
different cyclic orbits, compares those orbits across the saved quotient
seeds, and gives a **minimum three-choice** degree-two/upper-q1-preserving
bridge that supplies every relevant orbit.  It does **not** produce a
resident carrier, a Hall-18 compiler, or a length-6438 word.

## 1. The six targets are six different orbits

The authoritative carrier is

```text
scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json
SHA-256 86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b
```

Reconstructing its complete 16,383-by-19,311 compiler graph gives exactly

```text
5801, 13616, 13620, 17738, 21641, 29776
```

as its degree-zero targets.  Under cyclic rotation of fifteen coordinates,
their orbit representatives and phases are

| target | rank | orbit representative | phase |
|---:|---:|---:|---:|
| 5801 | 7 | 4821 | 3 |
| 13616 | 6 | 851 | 4 |
| 13620 | 7 | 3405 | 2 |
| 17738 | 6 | 2709 | 14 |
| 21641 | 6 | 2473 | 7 |
| 29776 | 6 | 1861 | 4 |

Thus the current Hall-19 defect is **not** six phases of the old canonical
orbit 2709.  It is one bad phase in each of six distinct orbits.  Directly,
each of the six orbit-degree profiles has precisely one zero entry, at the
displayed phase; all other fourteen phases have positive compiler degree.

The two rank-seven orbit representatives 4821 and 3405 are automatically
supplied by any quotient selector choosing one edge over every rank-seven
lower orbit.  The nontrivial quotient resource question is therefore the four
rank-six representatives

\[
                 851,\qquad 1861,\qquad 2473,\qquad 2709.       \tag{1.1}
\]

For an equivariant degree-two selector, one physical lower-q2 witness for a
representative creates all fifteen rotated witnesses.

## 2. What the saved seeds supply

For every degree-two snapshot below, the entry records which member of (1.1)
is absent from its cyclic lower-q2 shadow.

| selector | physical cycles | absent zero orbit |
|---|---:|---:|
| resident seed | `6435` | 1861 |
| joint scaffold | not degree two | none at the raw-pair level |
| d86 | `1209^5,270,120` | 851 |
| d92 | `2080^3,195` | 1861 |
| d93 | `6435` | 1861 |
| d94 | `1287^5` | 1861 |
| d83 | `429^15` | 2709 |

The exact source hashes are recorded by
`scratch/verify_k15_zero_orbit_choice_bridge.py`.  In particular, the q1
factors are not all failing for the same reason: they realize three different
faces of a four-orbit trade-off.

### Saved-union cut

Take, at each of the 429 lower orbits, only choices appearing in one of the
seven rows above.  This gives 760 allowed choices.  Exact enumeration of the
degree-two selectors gives only 39 factors.  Their lower-q2 patterns on the
three variable representatives are

```text
{851,2709}   and not 1861 : 27 factors
{1861,2709}  and not 851  :  8 factors
{851,1861}   and not 2709 :  4 factors
```

Every factor also supplies 2473.  Hence the saved-choice polytope satisfies
the exact integer cut

\[
 z_{851}+z_{1861}+z_{2709}\le2.                              \tag{2.1}
\]

The cut remains valid after upper-q1 completeness is dropped.  Thus no hybrid
made solely from the saved choices can repair all six zero orbits.  This is a
catalogue obstruction, not a global obstruction.

## 3. A three-action bridge in the full catalogue

Starting from the d93 Hamilton selector, replace exactly these three choices:

| lower owner | old choice | new choice |
|---:|---|---|
| 1837 | `(1837,12,13)` | `(1837,6,13)` |
| 1893 | `(1893,3,14)` | `(1893,12,14)` |
| 4759 | `(4759,11,13)` | `(4759,10,11)` |

The quotient endpoint-current changes are

\[
 392\longrightarrow96,qquad
 96\longrightarrow349,qquad
 349\longrightarrow392,                                     \tag{3.1}
\]

or, in middle-orbit representatives,

\[
 5783\longrightarrow1901\longrightarrow5307\longrightarrow5783.
\]

Consequently the net endpoint current is zero and every middle-orbit degree
remains exactly two.

The upper-q1 colour ledger is

\[
 -3803-5815-6005+5819+5949+7605.                             \tag{3.2}
\]

The deleted colour loads in d93 are respectively 4, 3, and 2, so no colour is
lost.  All upper-q1 orbits remain covered.

The new selector has two physical cycles of lengths 5400 and 1035.  Direct
physical, rather than quotient, enumeration gives the following q2 loads:

| rank-six orbit | physical q2 witnesses |
|---:|---:|
| 851 | 15 |
| 1861 | 15 |
| 2473 | 45 |
| 2709 | 15 |

The new 1861 witness uses choices

```text
(1893,12,14) and (2653,8,14).
```

The other two actions in (3.1) are the minimum circulation closure that pays
for that useful change while retaining degree two.

The selector is stored in

```text
scratch/k15_zero_orbit_full_k3.result.json
SHA-256 42be4bc5ccb87bd550c5cc7888a19e398ca1bdcd5852cba8a3e7f4e89c09a1a8
```

## 4. Three actions are minimal

The exact CNF for a selector at Hamming distance at most two from d93 has:

```text
11,998 catalogue choices
136,011 Boolean variables
546,160 clauses
```

It imposes:

1. exactly one choice per lower orbit;
2. exactly degree two at every middle orbit;
3. complete upper-q1 coverage;
4. a physical lower-q2 witness for each representative in (1.1); and
5. at most two changed lower-orbit choices from d93.

Kissat returns UNSAT.  Its binary DRAT proof was independently checked by
`drat-trim`:

```text
CNF   677506dd845258b575be1edd41c024ad4c810d9a9fb6e98e0c9c02f82b5b2638
DRAT  fc2f6dfe316ddd1af5ef919f393df32600ba49210df2a95a28f251d851cb4244
check 890cebb91723583dba0f6e3141e4ae665d8e6b57e675c24e3ed445b54d0b58c7
```

The checker reports

```text
s VERIFIED
```

The files are

```text
scratch/k15_zero_orbit_full_k2.cnf
scratch/k15_zero_orbit_full_k2.drat
scratch/k15_zero_orbit_full_k2.dratcheck.log
```

Together with the three-action witness, this proves that the minimum action
count for this exact quotient bridge problem is three.

The H100 CPU commands were

```bash
/home/amodo/tools/kissat/build/kissat --quiet \
  k15_zero_orbit_full_k2.cnf k15_zero_orbit_full_k2.drat \
  > k15_zero_orbit_full_k2.proof.log

/home/amodo/or15/drat-trim/drat-trim \
  k15_zero_orbit_full_k2.cnf k15_zero_orbit_full_k2.drat \
  > k15_zero_orbit_full_k2.dratcheck.log 2>&1
```

## 5. Scope and next use

This is a real escape from the old orbit defect, but not yet a Hall descent.
The d93 base is nonresident, and the three-action factor still has 1,065
cyclic residence violations, 55 missing lower-q2 orbits in total, 20 missing
lower-q3 orbits, and 17 deeper upper misses.  Therefore its q2 witnesses are
not yet literal cells of a valid common depth-three compiler.

What the certificate proves is sharper and reusable:

* the six Hall-19 zeros do not form one cyclic orbit;
* equivariance can nevertheless service all six orbit classes at once;
* neither degree two nor upper-q1 capacity is the obstruction;
* the saved portfolio was trapped behind the exact cut (2.1); and
* one new three-action current cycle crosses that cut optimally.

The next construction target is to transplant the current cycle (3.1), or
its 1861-producing motif, into a resident/shadow-complete selector.  Because
it is a closed quotient current and consumes only duplicated q1 colours, it is
the smallest possible orbit-aware primitive for that transplant.

## 6. Reproduction

The model builder and independent verifier are

```text
scratch/audit_k15_zero_orbit_choice_bridge.py
scratch/verify_k15_zero_orbit_choice_bridge.py
```

Run the lightweight independent audit with

```bash
PYTHONPATH=scratch python3 scratch/verify_k15_zero_orbit_choice_bridge.py
```

It reconstructs the authoritative Hall-19 graph, checks the unique bad phase
in every zero orbit, rebuilds the physical factor without using the search
model, verifies the three-choice current and q1 ledger, directly counts all
q2 witnesses, checks artifact hashes, and confirms the DRAT-verifier status.
