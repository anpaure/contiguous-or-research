# Independent audit: socketed odd counterflow and complement rotation

**Date:** 2026-08-06  
**Audited file:**
`MATH_THEOREM_ODD_SOCKETED_COUNTERFLOW_CYCLE_CRITERION_20260806.md`  
**Method:** direct source/terminal accounting, cycle-by-cycle matching, and
odd-order quotient lifting; no computation or search  
**Verdict:** PASS, with the scope restrictions recorded below.

## 1. Deterministic permutation accounting

For a selected boundary-pair index `i`, the construction retains the
original path `P_i -> a_i` and reroutes the distinct source path
`P_{pi(i)}` to `b_i`.  Therefore a selected index set `I` is legal exactly
when

\[
                  \pi(I)=[\delta]\setminus(I\cup S),
\]

where `S` is the socket set.  The resulting terminal count is
`2|I|+|S|=delta`.  The last-intersection and suffix-disjointness hypotheses
are exactly what is needed to concatenate the prefixes and suffixes into a
strict-gammoid linkage.

On one permutation cycle, no socket forces alternating selected-pair and
rerouted-source indices, hence even length.  One socket breaks an odd cycle
into an even path and permits alternation.  Thus the minimum socket count is
one per odd cycle.  Fixed points count as odd cycles and two-cycles give one
ordinary support edge.

## 2. General matching form

An oriented support edge `j -> i` consumes the two distinct indices `j`
and `i`.  Two chosen suffixes cannot share either index: sharing `j` repeats
a source path, while using one index once as a retained pair and once as a
rerouted source asks the same original path to have two terminals.  Hence
every construction from the stated atlas projects to an ordinary matching
in `G_partial`.

Conversely, matching-faithfulness is precisely the hypothesis that every
ordinary graph matching lifts to mutually disjoint physical suffixes.  A
matching of size `q` therefore yields `q` physical pairs and
`delta-2q` sockets.  Maximizing gives the exact formula

\[
                    \delta-2\nu(G_\partial).
\]

This formula is not asserted for a non-matching-faithful atlas.

## 3. Central parity and the complement-rotation permutation

The complement involution on

\[
               \mathcal T_{m,m}=\{u\in\{0,1,2\}^m:\sum u_i=m\}
\]

has the unique fixed point `1^m`, so the central source count is odd.

Write `m=2^a ell` with `ell` odd.  Rotation by `2^a` positions has odd
order `ell`.  For

\[
                        J=\mathsf c R^{2^a},
\]

an odd `J`-period `t` gives

\[
                        u=\mathsf c R^{2^a t}u.
\]

Every coordinate cycle of the rotation on the right has odd length.
Alternating a digit with its complement around such a cycle forces that
digit to equal one.  Hence `1^m` is the unique odd `J`-orbit.  Rotation and
complement preserve the undirected cyclic token graph, so `J` is a genuine
source-graph automorphism.

## 4. Odd stabilizer quotient

If an odd group `H` commutes with `J` and an orbit `[x]` has odd induced
period `t`, then `J^t x=h x` for some `h in H`.  Raising to the odd order of
`h` gives an odd ordinary `J`-period.  The preceding paragraph forces
`x=1^m`.  Thus the unique-odd-orbit property survives every commuting odd
quotient.

This is only a source-level quotient theorem.  It does not construct the
orbit-clock aperture or prove orbit-injective physical hub colours.

## 5. Exact open premise

The audited theorem does **not** prove a physical counterflow atlas.  To
deduce an odd current one must still construct suffixes after their last
intersections with the root-clock paths and prove either:

1. matching-faithfulness plus bounded matching deficiency; or
2. a deterministic last-intersection permutation with bounded odd-cycle
   count.

The complement-rotation `J` is a parity-perfect target, not yet a physical
lift through the fixed root/cut.
