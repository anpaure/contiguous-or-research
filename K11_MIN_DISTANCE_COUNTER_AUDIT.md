# Audit of the truncated `at_least` counter and `RECOMBINE_MIN_DISTANCE`

## 1. Verdict

The new `at_least` lambda in `recombine_paths_sat.cpp` is an exact CNF
encoding of

\[
                         \sum_{t=1}^N[\ell_t]\ge m, \tag{1.1}
\]

where every input `ell_t` may be an arbitrary signed DIMACS literal.  The
auxiliary states are constrained by equivalences, not merely one-way
implications, and truncating the unary counter at column `m` loses no
information relevant to (1.1).

For the intended call

```text
N = 461 seed-edge drop literals
m = 18
```

the counter adds exactly

```text
8,145 auxiliary variables
32,102 clauses
```

and no graph edges.  Starting from the documented orbit-search base counts,
the initial formula with `RECOMBINE_MIN_DISTANCE=18` therefore has

```text
462 rank-six vertices
6,930 real Johnson edges
462 real--dummy edges
68,287 variables
687,353 clauses
```

before later lazy cuts.  The 461 literals passed to the counter are precisely
the negations of the immutable preferred real-edge variables, so the encoded
condition is exactly “at least 18 preferred edges are absent,” equivalently
“at most 443 preferred edges remain.”

Importing the value 18 is logically licensed for the intended
`k11_lower956_upper549.txt` seed.  `K11_DISTANCE17_AUDIT.md` certifies that no
edge set within 17 dropped seed edges satisfies a **weaker** model which even
allows disconnected cycle components.  Every model of the full ordered,
canonical-prefix, second-orbit, target-958 search projects to an edge set
satisfying all conditions of that audited relaxation.  Hence the lower bound
removes no candidate from the stronger search.

Two scope qualifications should remain explicit.

1. `RECOMBINE_MIN_DISTANCE` is a generic user-supplied assumption.  The code
   checks the number of seed edges but does not authenticate the seed file or
   verify a certificate.  Setting it to 18 for another seed is not justified
   by the k=11 audit.
2. “Distance 18” here means at least 18 **dropped seed edges**.  Since both
   the seed and every qualifying path have 461 real edges, this is equivalent
   to ordinary edge-set symmetric difference at least 36, not 18.

No encoding defect was found.

## 2. Exact recurrence represented by the states

Let the input literals be

\[
                         \ell_1,\ldots,\ell_N.       \tag{2.1}
\]

For a fixed truth assignment to their underlying variables, write

\[
 x_i=[\ell_i\text{ is true}],
 \qquad s_i=x_1+\cdots+x_i.                         \tag{2.2}
\]

The intended meaning of auxiliary state `S[i][j]`, using zero-based `j`, is

\[
 S_{i,j}\quad\Longleftrightarrow\quad s_i\ge j+1,  \tag{2.3}
\]

for

\[
                         0\le j<\min\{m,i\}.        \tag{2.4}
\]

The exact Boolean recurrences are:

\[
 S_{1,0}\longleftrightarrow \ell_1,                 \tag{2.5}
\]

\[
 S_{i,0}\longleftrightarrow
       \bigl(S_{i-1,0}\lor\ell_i\bigr)             \tag{2.6}
\]

for `i>=2`, and, for `j>=1`,

\[
 S_{i,j}\longleftrightarrow
 \begin{cases}
  S_{i-1,j}\lor(\ell_i\land S_{i-1,j-1}),
       &j<\min\{m,i-1\},\\[2mm]
  \ell_i\land S_{i-1,j-1},
       &j=i-1<m.
 \end{cases}                                       \tag{2.7}
\]

The second line is the creation of a new highest column.  Once the counter
has width `m`, only the first line is used and the top state evolves as

\[
 S_{i,m-1}\longleftrightarrow
 S_{i-1,m-1}\lor(\ell_i\land S_{i-1,m-2}).          \tag{2.8}
\]

Counts larger than `m` never need a separate state: they already make
`S[i][m-1]` true.  This is the precise reason truncation is exact.

## 3. Clause-by-clause audit

### 3.1 First input

The two clauses

```text
-literal  current[0]
-current[0]  literal
```

encode

\[
                         S_{1,0}\leftrightarrow\ell_1. \tag{3.1}
\]

### 3.2 Column zero

For later inputs the clauses are

```text
-literal      current[0]
-previous[0]  current[0]
-current[0]   literal previous[0]
```

They are the standard exact encoding

\[
 current[0]\longleftrightarrow
      (literal\lor previous[0]).                    \tag{3.2}
\]

The first two implications force `current[0]` when either disjunct holds;
the third prevents it when both are false.

### 3.3 An already existing higher column

Put

```text
c = current[j]
s = previous[j]
b = previous[j-1]
l = literal.
```

The four clauses

```text
-s       c
-l -b    c
-c  s l
-c  s b
```

encode

\[
                         c\leftrightarrow s\lor(l\land b). \tag{3.3}
\]

Indeed, the first two clauses give `s -> c` and `(l and b) -> c`.  If
`c` is true and `s` is false, the final two clauses force both `l` and `b`.
This is exactly the first line of (2.7).

### 3.4 A newly created highest column

When `j==previous.size()`, no state `previous[j]` exists.  The three clauses

```text
-l -b   c
-c      l
-c      b
```

encode

\[
                         c\leftrightarrow l\land b, \tag{3.4}
\]

which is the second line of (2.7).

### 3.5 Final assertion

When `m<=N`, the final state vector has width exactly `m`.  The unit clause

```text
previous[minimum-1]
```

therefore asserts

\[
                         S_{N,m-1},                 \tag{3.5}
\]

which by (2.3) is precisely (1.1).

## 4. Inductive exactness, including signed literals

Fix any truth assignment to all original SAT variables.  No independence of
the input literals is assumed.  They may repeat, share underlying variables,
or contain both a variable and its negation.

Induct on `i`.  Equation (3.1) gives the claimed meaning for the first state.
Assume every state in row `i-1` has meaning (2.3).

* There is at least one true literal among the first `i` inputs exactly when
  either there was one among the first `i-1` or `ell_i` is true.  Thus (3.2)
  gives the correct column-zero state.
* For `j>=1`, at least `j+1` of the first `i` literal occurrences are true
  exactly when either at least `j+1` were already true, or `ell_i` is true
  and at least `j` were previously true.  This is (3.3).
* At the newly created top column `j=i-1`, the first alternative is
  impossible—fewer than `i` inputs existed—so all `i` inputs must be true.
  This is (3.4).

Every auxiliary value is consequently forced to its unique intended truth
value, and the final unit clause is satisfiable exactly for assignments with
at least `m` true input literal occurrences.

This proof is unchanged when an input is a negative DIMACS literal.  In a
clause, C++ expression `-literal` is the Boolean complement of the supplied
literal whether `literal` itself is positive or negative.  The recurrence
uses only the truth value of the literal occurrence, so arbitrary signs and
correlations cause no exception.

The boundary branches are also correct:

* `minimum<=0` adds no clauses, as every assignment satisfies an at-least-zero
  bound;
* `minimum>literals.size()` adds an empty clause, as the requested bound is
  impossible; and
* for an empty input list, these two branches cover every permitted minimum,
  so `previous[minimum-1]` is never accessed illegally.

## 5. Exact variable and clause counts

Assume `1<=m<=N`.  At input position `i`, the lambda allocates

\[
                         \min\{m,i\}                \tag{5.1}
\]

auxiliary variables.  Hence

\[
 \begin{aligned}
 V(N,m)
 &=\sum_{i=1}^N\min\{m,i\}\\
 &=\frac{m(m+1)}2+m(N-m)\\
 &=mN-\frac{m(m-1)}2.                              \tag{5.2}
 \end{aligned}
\]

For the clauses, row one contributes two.  For each row `2<=i<=m`, column
zero contributes three clauses, each old higher column contributes four,
and the one new top column contributes three.  The row total is

\[
                         3+4(i-2)+3=4i-2.           \tag{5.3}
\]

Thus the first `m` rows contribute

\[
                         2+\sum_{i=2}^m(4i-2)=2m^2.\tag{5.4}
\]

Every subsequent row has one column-zero OR and `m-1` existing higher
columns, contributing

\[
                         3+4(m-1)=4m-1             \tag{5.5}
\]

clauses.  Finally, the output assertion contributes one unit clause.  The
total is

\[
                         C(N,m)=2m^2+(N-m)(4m-1)+1. \tag{5.6}
\]

For `N=461,m=18`,

\[
 \begin{aligned}
 V(461,18)&=18\cdot461-\frac{18\cdot17}{2}=8145,\\
 C(461,18)&=2\cdot18^2+443\cdot71+1=32102.
 \end{aligned}                                      \tag{5.7}
\]

The documented base formula has `60,142` variables and `655,251` clauses.
Adding (5.7) gives

\[
                         68,287\text{ variables},
 \qquad 687,353\text{ clauses}.                    \tag{5.8}
\]

This remains comfortably below the ordinary variable reserve.

The documented base counts themselves are consistent with the source.  Its
variables decompose as

```text
7,392   selected-edge variables (6,930 real + 462 dummy)
28,644  real-vertex at-most-two counter variables
922     dummy-degree prefix variables
14,784  directed-arc variables
4,158   binary position variables
3,234   binary carry variables
1,008   witnesses for the initial rank-eight target 958
------
60,142
```

For target `958`, the induced graph is `J(8,6)`.  At each of its 28 centers,
one endpoint must add the first missing coordinate and the other endpoint the
second; there are `6*6=36` unordered endpoint pairs.  Hence it contributes
exactly `28*36=1,008` witness variables and `3*1,008+1=3,025` clauses.

The base clauses decompose as

```text
84,084  real degree-exactly-two clauses
2,764   dummy degree-exactly-two clauses
29,568  edge/arc equivalence clauses
6       canonical endpoint/first/second arc units
926     incoming/outgoing nonempty clauses
9,702   binary carry equivalences
475,398 gated path-position increment clauses
49,778  lower/upper colour and endpoint-access clauses
3,025   initial target-958 clauses
-------
655,251
```

Thus both the pre-counter and post-counter totals are independently accounted
for, rather than merely copied from a solver log.

## 6. Edge and literal counts in the k=11 call

The rank-six layer has

\[
                         \binom{11}{6}=462          \tag{6.1}
\]

vertices.  Every vertex of `J(11,6)` has degree

\[
                         6(11-6)=30,                \tag{6.2}
\]

so the number of real Johnson edges is

\[
                         \frac{462\cdot30}{2}=6930.\tag{6.3}
\]

The augmented degree encoding adds one dummy edge at every real vertex, for
462 additional graph-edge variables and 7,392 graph-edge variables in total.
The distance counter does not alter any of these counts.

The preferred input is a simple Hamilton path through the 462 masks and has
exactly 461 distinct real edges.  During setup, `seed_edge[id]` is set only
for those immutable preferred edges.  `RECOMBINE_PHASE_REPAIRS` may later
change `phase_edge` but cannot change `seed_edge`.  The code also checks

```cpp
if((int)dropped_seed.size()!=n-1) return 9;
```

before adding the bound.  Thus in the intended invocation the counter input
is exactly

\[
                         \{-x_e:e\in E_0\},         \tag{6.4}
\]

where `x_e` means that real edge `e` is selected.

Requiring at least 18 literals in (6.4) to be true means

\[
                         |E_0\setminus E|\ge18.     \tag{6.5}
\]

Equivalently,

\[
                         |E_0\cap E|\le461-18=443. \tag{6.6}
\]

Once the degree equations impose `|E|=461`, (6.5) also gives

\[
 |E\setminus E_0|=|E_0\setminus E|\ge18,
 \qquad |E\triangle E_0|\ge36.                     \tag{6.7}
\]

## 7. Why the certified lower bound transfers

The theorem independently certified in `K11_DISTANCE17_AUDIT.md` says there
is no real-edge set `E` satisfying all of:

1. two real vertices have degree one and all others degree two, even allowing
   disconnected cycle components;
2. `|E_0 setminus E|<=17` for the exact score-549 seed `E_0`;
3. 461 distinct rank-five intersection colors;
4. every rank-seven union color; and
5. containment of the unique omitted rank-five color in an endpoint.

Now take any hypothetical model of the current full ordered orbit branch
without the imported minimum-distance clause.  Delete the dummy vertex and
forget:

* arc directions and binary positions;
* connectedness;
* the canonical omitted color, endpoint, and first two edges;
* the explicit target-958 witness;
* factorability and every deeper-shadow cut; and
* all SAT auxiliary variables.

The remaining real-edge set still satisfies conditions 1, 3, 4, and 5 of the
audited relaxation.  If it dropped at most seventeen preferred edges, it
would also satisfy condition 2, contradicting the verified UNSAT theorem.
Therefore every model of the stronger search obeys (6.5), and adding the
counter is redundant.

The current canonical bit labels do not create a loophole.  The certified
distance theorem was proved with **no** omitted-color, endpoint, direction,
first-edge, or coordinate canonicalization.  It excludes every labeled edge
set in the radius-17 ball, including those which happen to satisfy the later
canonical prefix.  No claim that distance is invariant under relabeling is
being used.

Similarly, the fact that the certificate allows disconnected cycle covers
only makes it stronger for this purpose: the connected ordered Hamilton-path
models are a subset of its search space.

## 8. Scope and implementation qualifications

### 8.1 Seed identity is an external precondition

The code verifies that `seed_edge` contains `n-1` distinct candidate edges,
but it does not verify that they are the exact 461 edges whose SHA-256 and
distance theorem appear in `K11_DISTANCE17_AUDIT.md`.  Thus

```text
RECOMBINE_MIN_DISTANCE=18
```

is certified only when `paths.back()` is exactly
`k11_lower956_upper549.txt` (or an independently proved equivalent seed).
For another seed, the CNF remains a correct encoding of the requested lower
bound, but the claim that the bound is redundant may be false.

This is acceptable for a deliberately user-supplied imported theorem, but
runner scripts and proof manifests must record the preferred-seed hash.  A
dedicated certified option could additionally check `k==11`, `rank==6`,
`n==462`, full-graph mode, and the known seed hash before accepting the value
18.

### 8.2 Model strength

The logical transfer requires the final formula to impose all five structural
conditions of the audited relaxation.  The documented `allordinc` orbit
search does so.  The generic environment option can also be supplied in modes
which omit one of those conditions; in such a mode the k=11 distance theorem
does not automatically license the bound.  Again, the encoder itself is
exact, but the imported numerical premise is the caller's responsibility.

### 8.3 Full-layer guard

The recently tightened `RECOMBINE_SECOND_ORBIT` guard now requires
`all_edges`, `k==11`, and `rank==6`, which fixes the sparse-mode issue found in
the earlier audit for the intended 462-mask input.  Strictly, `all_edges`
means all Johnson edges induced by the supplied masks; the program still does
not explicitly test `n==462`.  Adding that test (unique rank-six masks are
already checked) would make “complete rank-six layer” self-enforcing rather
than an input precondition.

## 9. Final ledger

### Verified

* exact truncated-unary recurrence;
* exact CNF equivalences in every column;
* correctness for arbitrary positive or negative input literals;
* all minimum boundary cases;
* 8,145 added variables and 32,102 added clauses for `(461,18)`;
* 6,930 real, 462 dummy, and 461 preferred-edge counts;
* exact interpretation as at least 18 dropped seed edges; and
* logical transfer of the audited radius-17 exclusion to the stronger
  intended full ordered orbit search.

### External preconditions

* the preferred path must be the proof-certified score-549 seed;
* the mode must imply the structural relaxation used by the certificate; and
* any claim of WLOG full-layer orbit splitting assumes all 462 rank-six masks
  are supplied.

Subject to these explicit preconditions, `RECOMBINE_MIN_DISTANCE=18` is a
sound redundant strengthening and the implementation is correct.
