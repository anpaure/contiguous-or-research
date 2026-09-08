# Independent audit: cycle-aligned wedge linkage and factor materialization

**Date:** 2026-08-04  
**Method:** independent symbolic proof replay; no computation or search  
**Audited theorem:**
`MATH_THEOREM_CYCLE_ALIGNED_WEDGE_LINKAGE_FACTOR_MATERIALIZATION_20260804.md`  
**Audited theorem SHA-256:**
`3cdea7f8ff2f0649da152b1d4aef48ec57e3ddb5f6fb86208eefe15682daa04a`  
**Verdict:** **GO at the stated Boolean-linkage and serialized-factor
occurrence scope.**

## 1. Sequential Hamilton-cycle quantifiers

The underlying bounded-turn theorem constructs `H_i` only after all
terminals assigned at stages `<i` have been deleted from the current
terminal graph.  Its induction invariant is strong enough for the present
reuse:

- every newly assigned terminal at one stage is an edge of that stage's
  Hamilton cycle;
- shared owner ports retain their earlier assignment and receive no second
  terminal;
- all assignments remain globally injective.

Nothing in the new wedge choice changes `H_i` or the assignment rule.  The
wedge is selected from the already constructed and oriented cycle, so the
full-port linkage induction remains valid.

## 2. Existence of a cycle edge with two new owner endpoints

For a current source `L_i`, each earlier owner star intersects its owner
star in at most one value.  Therefore the set `F_i` of old owner
coordinates has size at most `i-1`.

In a simple cycle, the number of edges incident with a vertex subset `F_i`
is at most `2|F_i|` (overlap between incident edge pairs only lowers this
number).  The parameter range gives

\[
 2|F_i|\le2(i-1)\le2(p-1)<m=|E(H_i)|.
\]

Hence at least one edge of `H_i` has neither endpoint in `F_i`.  This
argument is valid for every stage, including `i=1`, and does not assume
pairwise separation of the lower turns.

## 3. The forced identity `phi(U_i)=Z_i`

Orient the chosen cycle edge as `a_i -> b_i`.  Both endpoint owner values
are new at stage `i`, so the full-port rule applies to each rather than
retaining an older assignment.  In particular the outgoing edge from
`a_i` is exactly the selected edge, and therefore

\[
 \phi(L_i+a_i)=L_i+a_i+b_i=Z_i.
\]

No statement about `phi(L_i+b_i)` is required.  Its outgoing edge is the
next edge of the oriented Hamilton cycle, so injectivity is not threatened
by the fact that the selected undirected edge is incident with `b_i`.

At stage `i`, both selected owner values lie outside the entire earlier
owner-star union; hence all `2p` selected owners are globally distinct.
Every edge of `H_i` avoids every earlier assigned terminal, and every
earlier selected `Z_j` is one of those assigned terminals.  Hence all
selected `Z_i` are globally distinct.

## 4. Protected-factor completion

The protected wedge bank `M` has degree two at each selected lower vertex
and degree one at each selected upper vertex, because the selected owner
values are globally distinct.  Thus `Delta(M)=2` and `|M|=2p`.

The theorem separately assumes that `P_* union M` is degree-compatible.
Together with `|P_*|+2p<=m-2`, this is exactly the hypothesis needed by
the small protected-factor theorem; no unproved compatibility is inferred
from the scalar edge count.

At a selected lower vertex, its two protected incidences exhaust factor
degree two.  Consequently they form one turn with owner values `U_i,U_i'`
and q1 union value

\[
 U_i\cup U_i'=L_i+a_i+b_i=Z_i.
\]

The protected-factor occurrence lift supplies the source and owner
addresses, and the turn-diamond occurrence theorem supplies the literal
owner-to-q1 containment.  Choosing the `U_i` branch therefore realizes the
same value edge `U_i -> phi(U_i)` selected by the Boolean linkage.

Distinct lower, selected owner and selected terminal values make the
selected occurrence paths pairwise distinct.  Since every path has only
its displayed owner as interior, these branches are pairwise
vertex-disjoint in the serialized source/owner/q1 complex.

## 5. Scope guardrails

The proof establishes the correlation

`Boolean linkage edge = selected wedge branch = serialized q1 occurrence`.

It does **not** establish any of the following, and the theorem correctly
keeps them outside its conclusion:

1. survival after freezing a compensation/background linkage;
2. terminal-type, phase, flag, or guard acceptance in one cap state;
3. a private continuation beyond the q1 occurrence;
4. compatibility with a two-coordinate product cap; or
5. nonaccumulating regeneration.

The theorem's range `p<=floor((m+2)/4)` is inherited from the sequential
Dirac construction.  The protected-factor row independently requires the
stronger contextual edge budget `|P_*|+2p<=m-2`; neither condition is used
as a substitute for the other.

## 6. Audit conclusion

All requested quantifiers replay correctly.  In particular, the edge with
two new endpoints is chosen *after* `H_i` exists, both endpoints are new
relative to the complete earlier star union, the inherited orientation
forces `phi(U_i)=Z_i`, and the protected factor makes that exact terminal a
literal q1 turn occurrence.  No mathematical correction is required.
