# The all-six-marked private-triple conjecture fails in the standard `m=5` gluing family

Date: 2026-07-31  
Status: exact finite family theorem and first counterexample to the proposed
standard-family strengthening; no claim about nonstandard gluing operations

## 0. Verdict

The all-six-marked private-triple conjecture from
`MATH_THEOREM_CATALAN_LEAF_PEELABLE_TRANSPARENT_GLUING_STATE_20260731.md`
is false for the full standard Merino--Mička--Mütze plane-tree gluing family.
The first failure is the very next case, `m=5` (the middle levels `4,5` of
`Q_9`).

There are three plane-tree components and three nonexceptional standard
gluing labels.  Exactly two labelled auxiliary spanning trees produce a
physical Hamilton cycle.  Each Hamilton cycle has only `81` distinct lower
turn colours and `81` distinct upper turn colours, rather than the required
`84` of each.  Both miss the same period-three lower orbit

\[
 \{73,146,292\}
 =\{001001001,010010010,100100100\}.                 \tag{0.1}
\]

Consequently neither cycle has even a Catalan decoration.  In particular,
neither can have a leaf-peelable decoration or a private-triple decoration.

This is a narrow but decisive refutation.  It does **not** say that `m=5`
has no decorable middle-levels cycle, nor that private triples cannot work
after a nonstandard hexagon, a switch, or a change of the base factor.  It
says that the unmodified standard plane-tree gluing family cannot support
the proposed induction.

## 1. Complete standard-family census

Write the paper parameter as `n=m-1=4`.  The fourteen Dyck words of
semilength four form three plane-tree classes.  The full nonexceptional
standard gluing-label list is

\[
\begin{array}{c|c|c|c}
 &x&y&([x],[y])\\ \hline
 g_0&11001010&10101010&(10101100,10101010)\\
 g_1&11001100&10101100&(10111000,10101100)\\
 g_2&11011000&10111000&(10101100,10111000).
\end{array}                                           \tag{1.1}
\]

The labels `g_1,g_2` are parallel at plane-tree level.  Thus a spanning tree
must use `g_0` and exactly one of `g_1,g_2`.  Both choices survive the exact
physical Hamiltonicity test.  There are no other labelled spanning trees in
the standard family.

The two Hamilton outputs have the exact deficits

\[
\begin{array}{c|c|c}
 \text{tree}&\text{missing lower turns}&\text{missing upper turns}\\ \hline
 \{g_0,g_2\}&\{73,146,292\}&\{221,365,438\},\\
 \{g_0,g_1\}&\{73,146,292\}&\{219,365,438\}.
\end{array}                                           \tag{1.2}
\]

On both shores the multiplicity histogram is

\[
                      1^{36}2^{45}.                  \tag{1.3}
\]

Hence exactly three colours are missing and exactly forty-five are repeated.

## 2. The private triples are locally present; the global palette is the failure

The more informative of the two trees is `\{g_0,g_1\}` in the indexing of
(1.1), namely the labels

\[
 (11001010,10101010),\qquad(11001100,10101100).
\]

For this tree, marking all six ports of each hexagon preserves both local
owner palettes across both toggles.  Its selected lower-owner triples are

\[
                         \{82,84,88\},\qquad
                         \{50,52,56\},                \tag{2.1}
\]

and these two triples are disjoint.  Thus the elementary local features
suggested by the `m=4` path really do persist: all six ports can be marked,
the lower owner triples are explicit, and different gluing nodes have
disjoint local triples.

Nevertheless the final lower turn map misses (0.1).  No choice of one
representative from each attained colour can create an occurrence of a
colour which is absent from the turn map.  The failure therefore precedes
the laminar/private attachment question: the standard gluing tree does not
have a global palette to decorate.

The other Hamilton tree fails even earlier.  At its non-potential label
`(11011000,10111000)`, all-six marking changes the local upper-owner palette

\[
                 \{221,287,411\}\longrightarrow
                 \{219,287,413\},                    \tag{2.2}
\]

so that toggle is not transparent for the all-six port set.

## 3. Exact implication

### Theorem 3.1

No Hamilton cycle obtained from the `m=5` MMM base factor by a labelled
spanning tree of standard incidence-hexagon gluing operations admits a
Catalan decoration.

#### Proof

The defining Dyck-word formula gives exactly the three labels (1.1).  The
auxiliary multigraph has exactly the two spanning trees described above.
Literal symmetric difference with their two physical incidence hexagons
gives one Hamilton cycle in each case.  Directly listing the turn colours of
the two cycles gives (1.2), so neither turn map is surjective.  Surjectivity
of both turn maps is necessary for a decoration.  \(\square\)

### Corollary 3.2

The all-six-marked private-triple conjecture is false when "standard
plane-tree gluing tree" means the full MMM standard-label family on its
canonical base factor.

The corrected recursive target must permit at least one of:

1. a preliminary turn-palette repair before the plane-tree merges;
2. nonstandard transparent incidence hexagons;
3. a different component factor; or
4. a state which changes the decoration representatives and the gluing
   family jointly rather than decorating the standard output.

The local private-triple path remains a useful sufficient face once a global
palette exists.  What fails is its proposed universality on the standard
family.

## 4. Audit

Run

```text
python3 scratch/audit_catalan_private_triple_standard_m5_refutation_20260731.py
```

The dependency-free audit reconstructs the Dyck rotation map, the physical
base factor, all standard labels, both spanning-tree Hamilton cycles, all
turn images, and every all-six local owner palette.  Its frozen output is

```text
scratch/catalan_private_triple_standard_m5_refutation_20260731.audit.json
```

The audit is exhaustive only for `m=5` and only for this exact standard
gluing-label family.
