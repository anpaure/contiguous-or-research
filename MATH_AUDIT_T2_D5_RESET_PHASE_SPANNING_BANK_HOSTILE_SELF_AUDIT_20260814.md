# Hostile self-audit of the `T2` `D_5` first-return reset-phase spanning bank

**Date:** 2026-08-14
**Object audited:**
`MATH_THEOREM_T2_D5_FIRST_RETURN_RESET_PHASE_SPANNING_ACTUATOR_AND_RESIDENCE_OBSTRUCTION_20260814.md`
**Verdict:** **PASS** for the finite `D_5` internal-owner construction and
its negative hypertree/residence conclusions.  **OPEN** for an all-`s`
finite-state reset grammar and a physical common-history planting.  This is a
hostile self-audit, not an independent human audit.

## 1. Audit boundary

The theorem contains six logically distinct claims.

1. The frozen first-return construction is a 41-edge label tree on all 42
   Dyck suffixes of semilength five.
2. The complete all-six-prefix global-minimum candidate bank has no
   owner/q1-colour SDR, and neither does the bank after adding the first-safe
   `P0` circuits.
3. One further prefix channel `P1` supplies a pairwise resource-disjoint
   selection on the same label tree.
4. That selection preserves aggregate q2 support and has one simultaneous
   lifted output containing every touched component and suffix representative.
5. The component support hypergraph is not a hypertree.
6. The simultaneous state is not undilated two-shore q=2 resident.

The audit does not infer an unbounded Catalan recursion from one finite
semilength, a source planting from a factor circuit, or residence from q2
support preservation.

## 2. Candidate-class and minimum scope

Every enumerated circuit is owner-simple and q1-colour-simple, goes through
the two named suffix representatives in one `T2` prefix channel, and uses
only degree-two owners of the post-`T2` factor.  Thus every toggled row has a
well-defined untouched q1 mate and exact q2 current.

All words “minimum” and “first-safe” have this internal-owner meaning.  They
do not compare against circuits using a degree-one factor endpoint.

For every selected reset circuit the hostile replay checks:

* membership by literal owner and colour sequences, not by selector index;
* agreement with the independently enumerated prefix menu;
* zero q2-safe circuits at every shorter enumerated length;
* equality of the selected length and that channel's first-safe length.

The selected rows split as

```text
22 all-prefix global-minimum circuits
10 P0 first-safe circuits
 9 P1 first-safe circuits.
```

The nine selected `P1` menus are fully enumerated at their solution length.
Some unselected `P1` menus in the larger SAT search retained only 512
witnesses at their first safe length.  That cap cannot invalidate a positive
selection, and none of those incomplete menus is used to assert a negative
result or justify a selected row.

## 3. Resource UNSAT scope

The exact 4,912-candidate global-minimum bank is UNSAT and has the verified
inclusion-minimal core `[35,38,39]`.  The exact 13,394-candidate bank after
adding all first-safe `P0` circuits is UNSAT and has core `[22,27,33,37]`.
Later iterative extension has the verified extreme child core
`[1,17,18,21]`.  Between them, partial `P1` extension produces the verified
14-edge core `[7,11,13,22,23,27,28,29,33,35,37,38,39,40]`, which meets every
first-return split class.

For each recorded core the solver deletion-shrinks and then reruns:

* the core itself, which is UNSAT;
* every one-edge deletion, which is SAT.

These are resource statements only.  They do not rule out longer circuits in
the same phase channels, a different third prefix channel, controlled
resource overlap, or a different suffix tree.

Accordingly, “smallest phase extension” in the theorem means exactly:

> the frozen global-minimum plus `P0` first-safe bank is UNSAT, while adding
> the single new channel `P1` yields the displayed certificate.

It is not an absolute chromatic theorem over every conceivable three-channel
catalogue.

## 4. Aggregate q2 encoding audit

For each old target `T`, the selector enforces

```text
old_load(T) + sum(selected candidate current at T) >= 1.
```

Signed coefficients are converted to cardinality by counting an absent gain
as a true negative literal and shifting the bound by the total possible gain.
Repeated signed literals in the chosen cardinality encoding were separately
exhausted on all assignments of small test instances on H100.

This encoding is not the final source of truth.  The frozen independent
verifier rebuilds the complete post-`T2` factor, reconstructs each removed and
added incidence, and recomputes the aggregate current.  It finds 346 removed
old occurrences, zero support losses, and minimum final old load one.

## 5. Topology-cut soundness

The topology selector does not merely block failed whole models.  For every
proper current output component `S`, it adds

```text
(some current crossing removal is deselected)
OR
(some candidate adding a crossing incidence is selected).
```

This clause is necessary.  Every fixed edge lies within a current component.
If every currently removed old edge crossing `S` remains removed and no added
edge crosses `S`, the alternative factor still has no edge across the cut.
It cannot be connected.  The code asserts that every added clause is false in
the rejected model before passing it to incremental CaDiCaL.

Seven q2/resource models are rejected with touched output counts

```text
4, 7, 8, 4, 3, 3, 2.
```

The eighth has one output.  The independent verifier then discards the CEGAR
component labels and traverses the full lifted factor from scratch.  It
reproduces

```text
base components met                        372
output components                            1
suffix-representative output components      1
component reduction                         371
output owner length per shore             12420.
```

## 6. Label tree is not a component hypertree

The suffix labels form a genuine 41-edge tree.  The separate bipartite
component--trade incidence graph has 372 component vertices, 41 trade
vertices, 447 incidences, and one connected component.  Its cycle rank is

```text
447 - (372+41) + 1 = 35.
```

Therefore no component-hypertree claim is available for this selection.  The
one-output theorem is an exact traversal theorem, just as stated.

## 7. Residence and common-history audit

The full simultaneous replay finds

```text
upper bad q=2 collars   181
lower bad q=2 collars   151
minimum seam gap          1 / 1.
```

The lower common-intersection rank is zero on two selected circuits, and every
lower palette has a nonzero loss current.  Even where a finite algebraic
intersection exists, no occurrence-disjoint, cut-separated source planting
has been supplied.  Hence the theorem correctly concludes only prospective
common-history data and a sharp undilated-residence obstruction.

## 8. Reproducibility and provenance

The frozen 115-menu bundle has SHA-256

```text
9c22615cd3058688f048f4e4062d007edadb10ab415c15ee89ed10d21b1bed8d.
```

The selector, independent verifier, and hostile replay have SHA-256 values

```text
selector  94deb656dac1d8955b20d851e92600156d703842d6de169d4b6bea356fa3ec32
verifier  ff5475083d3d836b5f107c5821c45918676b4a6df81bffc48ac1af8600e6a068
audit     1da6977f8e978c71fb90bcfb3bc54aa223f0d894850751200c3c425593c16942.
```

The hostile replay binds the literal selector to the menu bundle, checks the
three iterative cores, and confirms the independent verifier consumed exactly
the selector with the stated selector hash.

All substantive enumeration, compilation, SAT, traversal, audit, and hashing
was run through SSH on H100.  The Mac was used only for reading/editing,
artifact transfer, and Git.

## 9. Final verdict and remaining gate

The finite result survives hostile review.  A non-conjugate reset phase really
does repair the `D_5` suffix SDR, and the repaired bank has exact q2 support
and one simultaneous component output.  The construction is nevertheless
not yet an inductive reset grammar: its auxiliary signatures are edge-specific,
the Hall cores walk between split blocks before closing, and no bounded-state
recurrence has been proved beyond `D_5`.

The sharp remaining gate is therefore the conjunction

\[
 \boxed{\begin{array}{c}
 \text{a split-size finite-state reset catalogue with bounded phase/length
 complexity for every }D_s;\\
 \text{an occurrence-disjoint, cut-separated, residence-dilated physical
 common-history realization of its selections.}
 \end{array}}
\]
