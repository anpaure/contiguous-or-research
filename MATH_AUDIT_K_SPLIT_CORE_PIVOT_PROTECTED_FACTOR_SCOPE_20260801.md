# Audit of the split-core pivot: literal incidence count and protected-factor scope

Date: 2026-08-01  
Lane: K, protected Hamilton path / source-occurrence interface  
Status: **GO** for the local source theorem and the count `6h`; exact
quantifiers recorded for every fixed-`H` factor invocation.  The graph
extension does not by itself embed the literal source block.

## 0. Verdict

The construction in
`MATH_THEOREM_SPLIT_CORE_PIVOT_LITERAL_TWO_SIDED_COLLAR_20260801.md`
is correct.  Its final source has `4h+1` letters, its depth-`h` row has
`3h+1` distinct rank-`r` owners, and that owner row has exactly `3h`
Johnson transitions.  Since every transition lifts through its distinct
rank-`r-1` intersection, its middle-levels lift has exactly

\[
                             2(3h)=6h                         \tag{0.1}
\]

distinct incidence edges.

For `H` copies, the total is exactly `6Hh` only when the named occurrences
map to pairwise distinct owner and lower-colour vertices.  Under that
resource-disjointness hypothesis the union has maximum degree two.  The
small protected-factor theorem then applies after the specialization

\[
 r=m,\qquad \text{ground set }[2m-1],\qquad 6Hh\le m-2.   \tag{0.2}
\]

If `b` further boundary incidence edges must be fixed, the correct condition
is `6Hh+b<=m-2`.

No error was found in the split-core source factorization, the old-deck
transport, the two lower rays, or the local residence calculation.  The
remaining issue is semantic: containment of the `6Hh` set-valued incidence
edges is weaker than containment of `H` named source-word occurrences with
their exterior histories.

## 1. Exact lift and its natural phase

Write the owner path as

\[
 V_0,I_0,V_1,I_1,\ldots,I_{3h-1},V_{3h},               \tag{1.1}
\]

where the `V_j` are the `3h+1` owners in the displayed order and
`I_j=V_j\cap V_{j+1}`.  The theorem proves that the `V_j` are distinct and
that the `I_j` are distinct.  Consequently the two incidence sets

\[
 P_0=\{I_jV_j:0\le j<3h\},\qquad
 P_1=\{I_jV_{j+1}:0\le j<3h\}                           \tag{1.2}
\]

are disjoint matchings, each of size `3h`.  Their union is the literal
incidence path (1.1), and (1.2) declares its forward phase.  Swapping the
two classes reverses that phase.

Thus the path has `6h` physical graph edges, not `3h` and not `8h`.  The
`4h+1` source-letter count is a different ledger.  The pre-insertion
rank-`r+1` cells `U_j` are likewise not edges of `ML_m` and are not included
in (0.1).

## 2. The perfect-class phase is feasible for the pure collar

For completeness, any matching of size `t<=m-1` in `ML_m` extends to a
perfect matching.  Delete its `t` endpoints on each shore.  For a family
`A` of remaining lower vertices put `c=W-|A|`.  Then `c>=t`, and the sharp
middle-shadow surplus gives

\[
 |N(A)|-|A|\ge\min\{m-1,c\}\ge t.                      \tag{2.1}
\]

After deleting the `t` prescribed middle endpoints, Hall still holds.

For `H` resource-disjoint copies of (1.1), orient every copy and take the
union of its predecessor classes as `P_0`.  It has size `3Hh`.  Condition
(0.2) implies `3Hh<=m-1`, so (2.1) gives a perfect matching `M_0`
containing it.  Every edge of `P_1` shares its lower endpoint with its
`P_0` partner, and hence is automatically outside `M_0`.

This proves only the perfect-class/phase subgate.  A protected Hamilton
path still requires a near-perfect matching containing `P_1`, an
upper-exact representative forest, and the directed free-port connector
path.  The arbitrary protected two-factor theorem does not supply those
correlated rows.

## 3. Fixed-`H` coordinate and upper-colour quantifiers

One copy uses `|B|+4h=m+3h` coordinates after `r=m`.  One explicit way to
realize `H` graph-resource-disjoint copies is to share the base `B` of size
`m-h` and give every copy disjoint
`\Lambda,P,q^-,q^+,D^-,D^+` banks.  This
uses

\[
                         (m-h)+4Hh=m+(4H-1)h             \tag{3.1}
\]

coordinates.  The inequality `6Hh<=m-2` implies (3.1) is at most `2m-1`,
so there is no hidden coordinate shortage on this explicit face.

The weaker phrase “resource-disjoint” means only distinct owner and lower
vertices.  It does not in general imply distinct rank-`m+1` upper colours
between copies.  The explicit disjoint-label realization above does imply
that stronger property.  Without it, all protected non-`M_0` edges may
remain in the final path, but they cannot all be designated members of the
bijective upper-representative bank `Q_0` when two carry the same upper
colour; the surplus forced edges must be assigned to the connector bank.

## 4. Source-occurrence boundary

The protected-factor and Hamilton-path certificates live in the ordinary
set-valued incidence graph.  Their edge containment has the following exact
meaning.

* Both incidences at every internal `I_j` remain, so the adjacent owners,
  the lower colour, and the upper turn are fixed.
* The component remains a contiguous incidence subpath, with direction
  fixed only after the phase (1.2) is declared.
* Distinct physical packet occurrences are represented only if their map to
  graph edges is injective.  Duplicate occurrences of the same `(I,V)`
  collapse in the ordinary graph.

It does **not** retain the `4h+1` source positions, their exact letters, the
`h`-letter histories on the two sides, or their exterior OR contexts.
Therefore a global Hamilton/factor completion containing (1.1) does not by
itself prove that the literal source block occurs in a global antecedent.
One still needs a source-level socket whose prefix and suffix histories
agree with (2.1) of the source theorem, or a direct construction of the
global source around that block.  Endpoint joins and any incidence edges
used to enforce those sockets must be separately protected and counted in
`b` in Section 0.

This is precisely consistent with the theorem's stated scope: the local
two-sided collar is literal and correct, while global exterior guards,
upper-exact path completion, and regeneration remain open.

## 5. Independent replay

The dependency-free symbolic replay

```text
python3 scratch/audit_split_core_pivot_literal_two_sided_collar_20260801.py
```

checks `297` cases (`2<=h<=12`, both split shores nonempty), every old
interval occurrence, both immediate palettes, all short cells, and the run
ledger.  It reports

```text
PASS
cases=297 h_range=2..12
```

No finite search is used.
