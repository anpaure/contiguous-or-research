# K17 owner-deck defects do not measure physical compiler overhead

Date: 2026-07-31  
Status: solver-independent implication boundary and bounded-defect reduction;
no K17 word or all-k upper bound is claimed

## 0. Result

The authenticated cycle

```text
scratch/k17_parent_induced_macro_port_cycle_20260731.cycle
SHA-256 39cc3abe6a8991dc101a585123989deab863030060c00d3e0a2a60cd73252de6
```

is a literal Hamilton cycle on the `24310` rank-nine owners and uses every
rank-eight intersection colour once.  Its downstream census has

\[
 H_{\rm upper}=1891+910+128+3=2932,
 \qquad
 H_{\rm shadow}=1623+1013=2636.                 \tag{0.1}
\]

These `5568` counts are **not** a count of missing targets in a physical
length-`24313` word, and they give neither an upper nor a useful lower bound
on the number of physical edits or extra cells needed.  The reasons are
structural:

1. the lower counts in (0.1) are missing *intersections of owner windows*,
   whereas the lower compiler must realize targets as *unions of physical
   cells*;
2. the cycle supplies no physical word, schedule, or common-cap assignment
   to which a target-hole repair lemma could be applied;
3. `605` length-three runs lie strictly inside the selected fixed macros,
   and, more strongly, every occurrence transversal for the authenticated
   parent forces at least `165` such runs; the exact coupled minimum is
   `180`, certified by a replayed witness and a verified bound-`179` DRAT
   refutation, so neither port-flow reconnection
   nor changing the retained repeated-colour occurrences can make this
   parent flat depth-three resident; and
4. adding any number of cells to a **flat** window realization only raises
   its required internal run length, so flat additive overhead cannot repair
   those runs.

Consequently the new owner/q1 theorem does not combine with the closed even
splice to prove \(B(k)+O(1)\).  The closed splice still has excess
\(2e+c_{2m}\), where \(c_{2m}\in\{d_{2m},d_{2m}+2\}=\Theta(\sqrt m)\),
and the macro flow supplies no physical operation which removes that excess.

The exact weaker theorem sufficient for a constant-additive bound is instead
a **bounded physical defect theorem**: construct an actual word of length
\(B(k)+C_0\) missing at most \(C_1\) targets, for absolute constants
\(C_0,C_1\).  Appending those missing masks gives

\[
                         \nu(k)\le B(k)+C_0+C_1.     \tag{0.2}
\]

The word and the word-level hole bound are essential quantifiers.  An owner
cycle with a bounded or unbounded shadow census is not a substitute.

## 1. Three different defect spaces

Let \(T=(T_i)\) denote the rank-nine owner cycle.  There are three distinct
objects in the current project.

### 1.1 Owner-shadow defects

The finite audit forms intersections of consecutive owners.  Its q2 and q3
rows are

\[
 \left|\binom{[17]}7\setminus\{T_i\cap T_{i+1}\cap T_{i+2}\}\right|=1623,
                                                               \tag{1.1}
\]

and

\[
 \left|\binom{[17]}6\setminus
 \{T_i\cap T_{i+1}\cap T_{i+2}\cap T_{i+3}\}\right|=1013.    \tag{1.2}
\]

They test whether a maximal erosion of the owner chronology would expose
the required lower labels.  They are not witnesses in a word.

### 1.2 Upper owner-union defects

The upper census forms unions of consecutive owner rows.  It misses `2932`
targets of ranks ten through thirteen and none of ranks fourteen through
seventeen.  These are genuine defects of this owner chronology as an upper
carrier, but an edit can alter quadratically many interval unions.  Thus the
number `2932` is a target count, not an edit distance.

### 1.3 Physical common-cap defects

A compiler first chooses a legal schedule and nonempty physical letters
\(Q_p\) whose prescribed intervals reproduce every owner.  Its lower cells
are physical intervals \(J\), with values

\[
                              \bigcup_{p\in J}Q_p.   \tag{1.3}
\]

Only after \(Q\) exists is it meaningful to count missing lower targets of
the physical word.  The q2/q3 intersection counts (1.1)--(1.2) cannot be
substituted for the physical hole count in the spectral-defect identity.

At the tight K17 one-pivot schedule, the physical atlas has

\[
 3\binom{17}{9}+\binom42=72936,
 \qquad
 \sum_{j=1}^8\binom{17}{j}=65535,                  \tag{1.4}
\]

and scalar surplus `7401` before the schedule loss.  At loss `7401` the
surplus is zero, so a lower-complete compiler must biject its `65535`
physical cells with the `65535` lower targets.  Owner/q1 rainbowness does
not construct this bijection.  The known chain-aligned common-cap
counterexamples show that scalar capacity, individual providers, and
ordinary Hall do not imply it either.

## 2. What target counts can say about edits

The following elementary bounds make the quantifier issue precise.

### Lemma 2.1 (safe append repair)

If an actual word \(Q\) misses exactly \(h\) nonempty targets, appending one
letter equal to each missing target produces a universal word after at most
\(h\) extra cells.

#### Proof

Every old witness remains a contiguous interval in the unchanged prefix.
Each appended letter is itself a one-cell witness for its target. \(\square\)

This lemma cannot be applied to the K17 owner cycle: the owners are not the
physical letters and the cycle has not been compiled.

### Lemma 2.2 (one edit has nonconstant interval influence)

In a physical word of length \(L\), substituting position \(p\) can change
only intervals containing \(p\), but there are

\[
                              (p+1)(L-p)             \tag{2.1}
\]

such intervals.  Therefore \(c\) substitutions can affect as many as
\(c\max_p(p+1)(L-p)=\Theta(cL^2)\) interval
occurrences.

#### Proof

Choose the left endpoint in \(\{0,\ldots,p\}\) and the right endpoint in
\(\{p,\ldots,L-1\}\).  Every other interval is unchanged. \(\square\)

Consequently a missing-target count alone has no dimension-free conversion
to edit distance.  Even in a physical word the generic incidence lower
bound is only

\[
 c\ge
 \left\lceil{h\over\max_p(p+1)(L-p)}\right\rceil,   \tag{2.2}
\]

which is merely `1` for either K17 census in (0.1).  Conversely, Lemma 2.1
gives an upper bound only after a physical partial word has been supplied.

## 3. Flat additive overhead cannot repair the frozen chronology

### Lemma 3.1 (flat-window run lower bound)

Suppose a fixed owner chronology is represented by flat windows

\[
                         T_i=Q_i\cup\cdots\cup Q_{i+s}             \tag{3.1}
\]

of \(s+1\) nonempty physical positions.  Every internal positive coordinate
run in \(T\) has length at least \(s+1\).

#### Proof

If coordinate \(x\) occurs in physical letter \(Q_p\), then it occurs in
all owner rows whose window contains \(p\).  Away from the two linear
boundaries those rows form a block of length \(s+1\).  The owner support of
\(x\) is a union of such blocks; each internal connected component therefore
has length at least \(s+1\). \(\square\)

For K17, \(B(17)=24310+3\), so the flat depth-three realization has
\(s=3\) and requires internal runs of length at least four.  The independent
macro audit finds `605` length-three runs whose complete `0 111 0` pattern
is internal to one selected macro.  They survive every macro reversal,
permutation, and port completion.

The strengthened occurrence audit closes the apparent upstream escape
inside this parent chronology.  A rank-six colour may have several physical
parent edges; introduce a one-hot variable for which edge is retained.  Each
potential internal `0 111 0` pattern forbids retaining all four of its
edges.  There are `1425` exact clauses.  In `165` patterns all four edge
colours have unique occurrences, so the corresponding forbidden clause is
empty.  There are exactly eleven such forced patterns for each of the
fifteen old coordinates.  Hence **every** occurrence transversal for this
parent retains at least `165` internal length-three runs.  This conclusion
is solver-free; the CNF is only a literal catalogue of the empty-clause
certificate.

The coupled optimum is exactly `180`: an independently replayed transversal
leaves twelve packets per old coordinate, and the exact at-most-`179` CNF is
UNSAT with a retained DRAT proof independently accepted by `drat-trim`.
This strengthens the packet count but still gives no edit or extra-cell
lower bound.

The same obstruction has a dimension-uniform interface explanation.  In an
odd diamond, each proper parent coordinate run of length at least two loses
exactly one position under (C_i=T_i\cap T_{i+1}); singleton runs vanish and
an all-one trace is unchanged.  Thus a flat depth-(d) child is automatic
from parent proper minimum run (d+2), not merely (d+1).  A recursive
state without that extra unit must instead export a jointly feasible
cut/facet/nonflat compensation hitting every minimum packet.  Hitting is a
local necessary escape condition, not by itself a global compiler proof.

If \(C\) additive cells are used simply by increasing the flat depth to
\(s=3+C\), Lemma 3.1 raises the required run length to \(4+C\); it does not
repair even one of the fixed length-three runs.  Thus any completion of
this parent-induced branch must use at least one of two genuinely different
operations:

* change the parent chronology; or
* use a nonflat schedule with a separately proved envelope and common-cap
  assignment.

This is a topology statement, not a numerical lower bound of `605` edits.
One rethread can change many runs, and the present audit gives no disjoint
support certificate converting `605` to an edit count.

## 4. Exact equality gate and constant-additive gate

For this K17 branch, the minimal single theorem for equality can be stated
without reference to the construction history.

> **K17 physical completion theorem.** There is a rethreaded rank-nine
> chronology \(T'\), obtainable by any allowed upstream operation, and a
> legal chain-aligned schedule on `24313` nonempty physical letters such
> that (i) every owner is reproduced, (ii) every upper target has a
> consecutive owner occurrence, and (iii) the exact maximal-common-cap
> equations realize every lower target.

This statement is equivalent to producing the missing length-`24313` word;
the point of the formulation is that all three clauses must be joint.  The
new Hamilton theorem supplies only the owner/q1 part of clause (i).

For an all-k constant-additive result, the following strictly weaker target
is sufficient.

### Theorem 4.1 (bounded physical-defect reduction)

Assume absolute constants \(C_0,C_1\) exist such that, for every \(k\), one
can construct a nonempty physical word \(Q_k\) of length at most
\(B(k)+C_0\) whose contiguous unions contain every nonempty target except
possibly a set \({\cal H}_k\) with \(|{\cal H}_k|\le C_1\).  Then

\[
                         \nu(k)\le B(k)+C_0+C_1.     \tag{4.1}
\]

#### Proof

Append the members of \({\cal H}_k\) and apply Lemma 2.1. \(\square\)

This theorem allows bounded compiler debt and is therefore weaker than an
exact common-cap theorem.  But its hypotheses are physical.  To derive it
from the Pascal/odd-macro programme one still needs a uniform construction
which simultaneously:

1. rethreads or nonflat-schedules all but boundedly many residence defects,
   equivalently exporting one extra proper-run unit or a certified
   compensation ledger rather than losing one unit per odd step;
2. protects all but boundedly many upper targets through the cuts; and
3. materializes a common-cap assignment with at most bounded word-level
   holes.

Neither the closed even splice nor the K17 macro b-flow supplies any of
these three implications.  In particular, the closed splice arithmetic

\[
 |\mathcal S_z(X)|-B(2m)=2e+c_{2m},\qquad
 c_{2m}=\Theta(\sqrt m),                            \tag{4.2}
\]

remains the best unconditional accounting from that splice.  An abstract
odd owner/q1 factor cannot be composed with (4.2) until it has been turned
into a physical bounded-defect compiler.

## 5. Scope

Proved here:

* the exact separation between owner shadows, owner upper unions, and
  physical common-cap cells;
* the safe bounded-hole append reduction;
* the nonconstant interval influence of one edit;
* the flat-window run lower bound, including the fact that flat additive
  overhead cannot repair the selected `605` internal runs;
* the independently authenticated occurrence-transversal strengthening:
  all transversals of this parent force at least `165` internal runs, with
  exact coupled minimum `180`; and
* the precise physical theorem sufficient for \(B(k)+O(1)\).

Not proved here:

* that K17 requires more than `24313` cells;
* any lower bound of `605` edits or cells;
* impossibility of a nonflat compiler for the frozen parent chronology;
* a bounded repair packet; or
* an unconditional \(B(k)+O(1)\) recurrence.

## 6. Audit

The lightweight deterministic audit

```text
scratch/audit_k17_owner_defects_vs_physical_overhead_20260731.py
```

rechecks the authenticated dependency hashes, all finite sums used above,
the K17 scalar ledger, the fixed-run count, the occurrence-transversal CNF
header and empty clauses, and the closed-splice depth arithmetic.  It emits

```text
scratch/k17_owner_defects_vs_physical_overhead_20260731.audit.json
```
