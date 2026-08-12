# Independent symbolic audit of the moving-core pull-clock rail

**Date:** 2026-08-02
**Audited file:**
`MATH_THEOREM_K_MOVING_CORE_PULL_CLOCK_DEPTH_ONE_HAMILTON_RAIL_AND_DEPTH_TWO_BOUNDARY_20260802.md`

**Verdict:** PASS within its stated lower-side scope.  This audit uses only
the literal predecessor identity, Middle Levels incidence, and elementary
set algebra.  It does not use degree heuristics or a finite search.

## 1. Depth-one predecessor replay

Write one Middle Levels wedge as

\[
                         q_i\subset T_i\supset q_{i+1},
 \qquad |q_i|=|q_{i+1}|=r-1.                          \tag{1.1}
\]

For role `i`, the proposed head is `q_(i+1)`.  Its owner gap is

\[
                         P_i=T_i-q_{i+1}=q_i-q_{i+1}.   \tag{1.2}
\]

The proposed predecessor token is `q_i`, so

\[
                         P_i\subset q_i\subset T_i.     \tag{1.3}
\]

At depth one the rail state is empty.  Thus (1.3) is exactly the Boolean
rail predecessor test, not merely a projected Middle Levels adjacency.
Cycling through all wedges uses each lower token and each upper owner once.

## 2. Pull-clock type replay

Within `T_i`, the current head facet `q_(i+1)` has size `r-1`; the unique
point in `T_i-q_(i+1)` has age one.  Hence the novelty partition is
`(r-1,1)`, the depth-one all-high type.  No fixed-core assertion is used.

## 3. SCD quantifier replay

The matching `q_(i+1)-T_i` is one parity matching of the Hamilton cycle,
hence is perfect.  The audited central-matching extension theorem applies
to an arbitrary such perfect matching and produces an SCD retaining every
matching edge.  Assigning its chains by these central edges gives a
bijection with the roles.  Because an SCD partitions the full Boolean
lattice, every lower-rank target appears in exactly one assigned chain.

This verifies the static payload statement.  It does not imply that the
deeper chain vertices are suffix unions of the depth-one source word; the
theorem explicitly excludes that inference.

## 4. Depth-two necessity and sufficiency

Let a rank-correct overlap block between `q_i` and `q_(i+1)` be `C_i`.
Literal containment forces

\[
 C_i\subseteq q_i\cap q_{i+1}.                        \tag{4.1}
\]

Both sides have rank `r-2`, so `C_i` is forced to equal the intersection.
The head for `q_i` is therefore the pair

\[
 q_{i-1}\cap q_i,\qquad q_i\cap q_{i+1}.              \tag{4.2}
\]

Its union equals `q_i` unless the point added on entering `q_i` is the point
deleted on leaving it.  In that exceptional case both blocks in (4.2) are
the same set `q_i-{b}` and their union misses `b`.  This is exactly a
one-position positive run.  Thus all four conditions in Theorem 3.1 are
equivalent.

When the union condition holds, the identities at indices `i+1` and `i+2`
give two consecutive lower windows.  Taking their union shows that three
consecutive blocks have union

\[
 (q_i\cap q_{i+1})\cup(q_{i+1}\cap q_{i+2})
 \cup(q_{i+2}\cap q_{i+3})
 =q_{i+1}\cup q_{i+2},                                \tag{4.3}
\]

after the theorem's cyclic index shift.  This is the corresponding owner.
Hence the proposed block word is a literal lift.

## 5. Palette and scope audit

The rank-`(r-2)` overlap values are forced, so target exactness at that row
is equivalent to support-surjectivity followed by marking one occurrence
per target; it is not a bijection claim.  Absence of singleton runs
only prevents equal consecutive overlap values; it does not imply global
surjectivity.  The theorem states this distinction correctly.

No step proves upper shadows, an exterior path opening, terminal
common-cap matching, or residence beyond the explicit run condition.  The
SCD extension proves static target bookkeeping only.  These exclusions are
necessary and correctly retained.
