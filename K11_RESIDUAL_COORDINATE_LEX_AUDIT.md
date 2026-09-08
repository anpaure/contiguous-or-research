# Independent audit of the residual-coordinate lexicographic symmetry break

## Verdict

**PASS.**  The optional

```text
K11_FOREST_RESIDUAL_COORD_LEX=1
```

module is an exact satisfiability-preserving symmetry break in each of the
two exhaustive v2 rank-filtration branches.

* In Type II it may sort all eleven complete occurrence columns.
* In Type I it may sort bits `0,...,5` and `6,...,10` independently.
* Every adjacent-column comparator is an exact lexicographic `<=` circuit;
  its prefix-equality variables are bidirectional and uniquely determined.
* The group sizes, variable counts, clause counts, and integrated build
  deltas are exact.
* With the guard absent or equal to `0`, no variable or clause is added and
  the complete solver-add stream is unchanged.

No production-source edit was required.

The audited source is

```text
aeddeccadb9e307d30a5bacd37033ea3b610e62634dbba9df36ce6e365c6c0e7
  k11_forest_sat.cpp
```

The independent checker is

```text
185429c74b4f9e6edaef672e7bbf60dfbedc205ed37b0cb5395ed1d327424dc5
  scratch/verify_k11_residual_coordinate_lex.py
```

## 1. Exact comparator semantics

For adjacent coordinate columns `left,right`, write

\[
 x_p=A[p][left],\qquad y_p=A[p][right],\qquad0\le p<465.
\]

The production circuit starts with a unit literal `one` and uses
`equal_above=one`.  At position `p` it emits

\[
 \neg equal\_above\ \vee\ \neg x_p\ \vee\ y_p. \tag{1.1}
\]

Thus, while every earlier pair is equal, the forbidden first difference is
`x_p=1,y_p=0`.

For every nonfinal position it creates `next_equal` with the five clauses

\[
\begin{aligned}
 next\_equal&\longrightarrow equal\_above,\\
 next\_equal&\longrightarrow(x_p\longrightarrow y_p),\\
 next\_equal&\longrightarrow(y_p\longrightarrow x_p),\\
 equal\_above\wedge x_p\wedge y_p&\longrightarrow next\_equal,\\
 equal\_above\wedge\neg x_p\wedge\neg y_p&\longrightarrow next\_equal.
\end{aligned} \tag{1.2}
\]

Together these are exactly

\[
 next\_equal\ \longleftrightarrow\
 equal\_above\wedge(x_p\leftrightarrow y_p). \tag{1.3}
\]

In particular, an auxiliary flag cannot be set false merely to deactivate a
later first-difference clause.  Induction on `p` makes `equal_above` exactly
the equality of the two column prefixes through position `p-1`.  Equations
(1.1)--(1.3) therefore enforce

\[
 (x_0,x_1,\ldots,x_{464})
 \le_{\rm lex}
 (y_0,y_1,\ldots,y_{464}), \tag{1.4}
\]

with position zero compared first.

The independent checker exhausts every pair of binary columns through
length four and every assignment to the auxiliary equality variables.  It
verifies both:

1. the CNF has an extension exactly when (1.4) holds; and
2. that extension is unique.

It reports

```text
residual lex comparator truth tables length 1..4: PASS
```

## 2. Residual symmetry in Type II

The Type-II rank-filtration circuit forces every literal array entry to have
rank at most five.  Hence no literal rank-six entry exists.  The
coordinate-canonical rank-six clauses are therefore semantically vacuous on
the Type-II solution set: although those clauses are not syntactically
invariant under all of `S_11`, every coordinate permutation of a Type-II
array still satisfies them because ranks remain at most five.

All other enabled v2 objects are coordinate-equivariant:

* direct targets and exception targets are complete rank families;
* rank-five/rank-six target columns are merely permuted;
* endpoint states, width cuts, and boundary orientation do not name a
  coordinate;
* the local-density and containment circuits depend only on ranks;
* the subcube circuit sums over all six-sets;
* the Type-II component circuit asks for a component containing all eleven
  coordinates, not for named coordinates; and
* the seed array affects solver phases only, not clauses.

Thus the full `S_11` action survives on satisfying arrays.  Any eleven binary
occurrence columns can be sorted lexicographically by a coordinate
permutation.  The call

```cpp
add_group(0, 10);
```

creates the ten adjacent comparisons for the size-eleven group
`0,...,10`, and loses no Type-II solution orbit.

The same conclusion remains valid with the optional `e0c1` component module:
its equations are coordinatewise and introduce no coordinate name.

## 3. Residual symmetry in Type I

Type I fixes

\[
 A[0]=63=\{0,1,2,3,4,5\}
\]

as the unique literal six-set.  Its residual coordinate stabilizer is

\[
 S_{\{0,\ldots,5\}}\times S_{\{6,\ldots,10\}}
 \cong S_6\times S_5. \tag{3.1}
\]

Every enabled v2 Type-I clause is equivariant under (3.1).  In particular,
the suffix-core subcube correction singles out the set `63`, but that set is
fixed setwise by (3.1); the rank-six branch profile and endpoint orientation
do not further distinguish coordinates inside either part.

The production calls

```cpp
add_group(0, 5);
add_group(6, 10);
```

mean inclusive groups `0,...,5` and `6,...,10`: `add_group(first,last)` emits
comparators for `bit=first,...,last-1`.  They therefore create five plus four
adjacent comparisons.  Sorting independently inside the two stabilizer
orbits loses no Type-I solution.

The optional `e1c2` schedule is likewise coordinatewise, and its fixed
endpoint value is exactly the already stabilized mask `63`.

## 4. Guard scope

The lex guard is accepted only when exactly one of

```text
K11_FOREST_RANK_FILTRATION_TYPE1
K11_FOREST_RANK_FILTRATION_TYPE2
```

is active.  With neither active, the program exits with status two and the
message

```text
K11_FOREST_RESIDUAL_COORD_LEX requires exactly one of
K11_FOREST_RANK_FILTRATION_TYPE1 or K11_FOREST_RANK_FILTRATION_TYPE2
```

The pre-existing Type-I/Type-II guards separately enforce their band,
joint-band, density, and branch prerequisites.  Portal modes are already
incompatible with either rank-filtration type, so the lex module cannot be
accidentally combined with a coordinate-named portal prefix.

No variable is allocated until after this validation and only when the lex
boolean is true.

## 5. Exact inventory

One 465-bit adjacent-column comparator has

```text
prefix variables = 464
comparison clauses = 465
prefix-equivalence clauses = 5*464 = 2320
total clauses = 2785.
```

There is one shared constant-true variable and one unit clause per complete
plan.

### Type II

Ten adjacent comparators give

```text
variables = 1 + 10*464 = 4641
clauses   = 1 + 10*2785 = 27851.
```

The integrated build changes exactly from

```text
3640328 variables / 19476694 clauses
```

to

```text
3644969 variables / 19504545 clauses.
```

### Type I

Nine adjacent comparators give

```text
variables = 1 + 9*464 = 4177
clauses   = 1 + 9*2785 = 25066.
```

The integrated build changes exactly from

```text
3633121 variables / 19448586 clauses
```

to

```text
3637298 variables / 19473652 clauses.
```

The production diagnostics reproduce all four totals.  The independent
checker reports

```text
group sizes and Type I/II inventories: PASS
production wiring anchors: PASS
```

The source also compiles cleanly with
`-Wall -Wextra -Wpedantic` against the build-only CaDiCaL test double.

## 6. Guard-off identity

The absent and explicit-zero guard builds have identical inventories and
identical complete `solver.add()` fingerprints.

Type II:

```text
CLAUSE_STREAM_FNV64=74515b6d2178098e ADD_CALLS=85329775
```

Type I:

```text
CLAUSE_STREAM_FNV64=325b7d6a6eb412fe ADD_CALLS=85224013
```

For reference, enabled fingerprints are

```text
Type II: CLAUSE_STREAM_FNV64=f889f86c1d628c1b ADD_CALLS=85445817
Type I:  CLAUSE_STREAM_FNV64=1059dcbbf38dc087 ADD_CALLS=85328451
```

The hash executable is only a deterministic clause-stream auditor, never a
SAT solver.

## 7. Evidentiary scope

This module chooses one lexicographically sorted representative from every
residual coordinate-symmetry orbit.  It does not add a mathematical
necessary condition beyond symmetry and proves neither SAT nor UNSAT.

A satisfying model still needs both independent interval-OR verifiers.  An
UNSAT conclusion still needs a frozen formula, archived proof, and
independent proof checking for both exhaustive rank-filtration branches.
