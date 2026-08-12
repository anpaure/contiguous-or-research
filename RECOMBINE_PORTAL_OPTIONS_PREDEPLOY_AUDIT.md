# Predeployment audit of the portal-suffix options in `recombine_paths_sat.cpp`

## Verdict

**PASS for the literal low-level meanings of the three switches, but FAIL as
a complete encoding of extension of the fixed `q=19` factor prefix.  Do not
deploy the combined portal-suffix search as an exact branch yet.**

The three additions are individually understandable:

```text
RECOMBINE_EXCLUDE_MASKS       removes named central vertices;
RECOMBINE_PRECOVERED_MASKS    assumes named targets are supplied externally;
RECOMBINE_START_CONTAINS      restricts the oriented first remaining vertex.
```

With all three switches absent, the historical SAT variable allocation and
clause stream are unchanged.  However, `START_CONTAINS=550` is only a
necessary boundary condition for the fixed 22-entry factor, not a sufficient
one, and the supplied precovered file records only upper masks.  The reduced
suffix formula therefore cannot yet be promoted as equivalent to extending
that prefix.

## Audited artifacts

```text
b221b089ef9f2ab19ce83daad4f5103e30f46309cd0f12bd714a67b8c4373a0b
  recombine_paths_sat.cpp
3a2df97798296a9c7e9f3953ed6ef1486c0572ffc3cd994218938556e1d0a22d
  k11_partial_switch_excluded_rank6.txt
d65a6c20ea47df87c562c069d859fd0fd1b96937186bc1d979ca06498d225dad
  k11_partial_switch_precovered_upper.txt
```

## 1. `RECOMBINE_EXCLUDE_MASKS`

The source reads the file into a set, erases every named value from every
supplied path, and requires

```text
old size - new size = number of distinct excluded masks
```

for each input.  Thus every named mask must occur exactly once in every valid
permutation input.  The first remaining path is subsequently checked for
correct rank and uniqueness, and every value of every other remaining path
must belong to that same vertex set.  For the supplied nineteen-mask file,
this correctly constructs the 443-vertex induced rank-six problem.

There are two configuration hazards:

1. In an `all...` mode, the old canonicalization gate becomes true even
   though the explicit excluded set has broken coordinate symmetry.  The
   canonical endpoint normalization is no longer WLOG for the fixed-prefix
   branch.  With the present prefix it also conflicts with the desired start:
   canonical mask `63` does not contain `550`.  A portal-suffix invocation
   must at minimum set `RECOMBINE_NO_CANONICAL=1`, and the program should
   preferably reject the unsafe combination automatically.
2. If a future excluded file removes either canonical mask while
   canonicalization remains enabled, the corresponding `index` is `-1` and
   later canonical-edge code is not safe.  The mode should validate this or,
   more naturally, disable canonicalization whenever an explicit excluded set
   is active.

These do not invalidate the induced-graph operation itself; they invalidate
an unguarded combination with the older symmetry module.

## 2. `RECOMBINE_PRECOVERED_MASKS`

The parser accepts distinct nonzero masks in `1,...,2^k-1` and records them in
a bitset.  A precovered rank-`r+1` target is omitted from the eager upper-colour
clauses, and every listed target begins marked covered in the lazy checker.
This is logically sound **conditional on an external certificate** proving
those masks are present in the fixed prefix.  It introduces no link to such a
prefix inside the recombination CNF, so a suffix SAT result must be composed
with and checked against that certificate before it means anything about an
OR word.

The supplied file lists the eighteen certified rank-seven portals and seam
`958`; all nineteen are indeed covered by the 22-entry prefix.  But it is not
a complete external-coverage description for a reduced central suffix:

* the nineteen removed rank-six masks are also covered by the prefix yet are
  absent from the file;
* the eighteen internal adjacent intersections

```text
425 428 812 796 852 1860 1606 1730 1219
227 115 91 31 542 666 1178 1432 412
```

  are distinct rank-five masks and equal the actual two-entry ORs in the
  sparse factor, but are absent from the file.

In a lazy full check, the omitted rank-six masks are therefore seen as missing
and can cause every candidate suffix path to be blocked.  More fundamentally,
the eager lower-colour endpoint clauses do not consult `externally_covered`
at all.  A 443-vertex suffix has only 442 internal edges and cannot by itself
supply the lower-colour accounting of the original 462-vertex row.  The
prefix lower colours and the mixed seam must be incorporated explicitly.

This is primarily a false-UNSAT/overconstraint problem for the current file,
not permission for a false SAT model: the option only removes obligations for
masks the caller explicitly asserts.  Nevertheless it means the proposed
combined search is not the intended exact extension problem.

The parser also treats a missing/unreadable coverage file as an empty list.
That is logically safe but operationally dangerous; an explicitly requested
file should fail closed if it cannot be opened.

## 3. `RECOMBINE_START_CONTAINS`

Inside the ordered-path encoding, every dummy edge has two directed arc
variables.  Since `add_edge(real,dummy)` stores `real` as `u` and the dummy as
`v`, `arc[id][1]` is exactly `dummy -> real`.  The source prohibits this arc
for every real mask not containing the requested subset.  The unique outgoing
dummy arc therefore selects a start mask containing the subset.  The bit test

```text
(mask & subset) == subset
```

and the arc orientation are correct.

Two guards are missing:

* in an unordered mode there are no arc variables and the option is silently
  ignored; it should require `ordered` or reject;
* negative values below `-1` silently disable the option, and malformed
  decimal text throws rather than producing the normal validation status.

The decisive mathematical issue is that containment of `550` fixes only the
first central suffix window.  The known final factor entries are, zero-based,

```text
A[19]=4, A[20]=32, A[21]=514.
```

For a quadruple central suffix `Q_0,Q_1,...`, exact continuation requires at
least the following boundary incidences:

```text
550 subset Q_0,
546 subset Q_1,
514 subset Q_2.
```

Moreover, every one of the two extra bits in the rank-six set
`Q_0 \ 550` must be supplied by the new entry `A[22]`; consequently those
bits must persist through `Q_1,Q_2,Q_3`.  Equivalently,

```text
Q_0 \ 550 subset Q_1 intersection Q_2 intersection Q_3.
```

The ordinary internal run condition deliberately permits arbitrary short
left-boundary runs and does not imply these constraints.  Thus a suffix model
with only `START_CONTAINS=550` can be factorable in isolation while having no
factor whose first three entries equal the fixed prefix boundary.  Such a
model would be a false positive for the claimed *factor-prefix extension*,
even though it is a valid abstract central suffix.

A safe exact implementation can branch over the 21 possible rank-six
supersets `Q_0` of `550`, require the two extra bits through `Q_3`, require
`546` through `Q_1`, and require `514` through `Q_2`; or encode the same
conditional boundary signature without branching.

## 4. Default-mode preservation

The recorded patch consists only of the three opt-in blocks and two guarded
uses of an all-zero coverage bitset.  With all switches absent:

* no path is erased;
* `externally_covered` is all zero, so every old eager upper clause is emitted;
* the lazy `covered` vector starts all zero exactly as before;
* `required_start_subset=-1`, so no arc clause is added;
* no SAT variable is allocated by the new host-side data.

Hence the historical variable allocation and clause order are preserved.  The
only additional work is allocation of a small host vector.

## 5. Required repair before deployment

An exact fixed-prefix suffix branch needs all of the following:

1. disable/reject old coordinate canonicalization under explicit exclusions;
2. require ordered mode for `START_CONTAINS`;
3. encode the complete four-row boundary signature above, not only
   `Q_0 superset 550`;
4. mark the nineteen excluded rank-six masks and certified prefix lower
   shadows as externally covered where the relevant constraints use them;
5. model the mixed prefix/suffix seam and remaining boundary lower witnesses
   explicitly;
6. make requested files fail closed and independently verify any returned
   joined word/factor.

Until those repairs are made, these switches are useful exploratory filters,
not a sound-and-complete exact portal-extension encoding.
