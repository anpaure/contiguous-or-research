# Independent symbolic audit: ring-surgery rigidity and open-hex transport

**Date:** 2026-08-04  
**Verdict:** `GO`, with the scopes stated in the two source theorems.  This
audit uses a second, role-table derivation of every degree and component
identity.  It uses no computation or search.

Audited sources:

* `MATH_THEOREM_MINIMAL_HAMILTON_RING_SURGERY_RIGIDITY_20260804.md`;
* `MATH_THEOREM_OPEN_HEX_PAIR_TRANSPORT_AND_FIXED_RING_PLANTING_20260804.md`.

## 1. Minimal-surgery ledger

There are `2m` ring owners and `2m` Hamilton-cycle incidences at the `m`
ring roots.  If `n_j` ring owners receive exactly `j` of those incidences
and `e_out` incidences go to non-ring owners, then

\[
 n_0+n_1+n_2=2m,
 \qquad
 n_1+2n_2+e_{\rm out}=2m.
\]

Subtraction gives

\[
 n_0=e_{\rm out}+n_2.
\]

After root deletion and insertion of one target-ring edge at each ring
owner, the degree is `3-j`.  Thus `j=0` requires one extra deletion,
`j=1` is balanced, and `j=2` requires one new edge.  This agrees exactly
with the preceding scalar identity.

Let an unhit ring owner expose a lower endpoint `z`.

* If a core coordinate `d in B` is deleted, then

  \[
  z=(B-d)+p
  \]

  for the owner's external pair `p`.  A root-neighbour upper has form
  `B+q`, and `z subseteq B+q` forces `p=q`; hence that upper is the same
  ring owner, which has no upper deficit.
* For `L_i=B+b+a_i`, deleting `b` reaches its ring root and contradicts
  unhit status.  Deleting `a_i` gives `B+b`, whose root-neighbour uppers
  are only the `L_j`; none can have upper deficit.
* For `R_i=B+a_(i-1)+a_i`, either external deletion reaches a ring root and
  again contradicts unhit status.

Therefore every lower deficit created at an unhit ring owner is isolated
from the full upper-deficit bank.  A repair matching forces `n_0=0`, hence
`e_out=n_2=0`.  Every ring owner is hit exactly once.  All `L_i` incidences
are forced; the remaining root--`R` graph is one even cycle and has its two
alternating perfect matchings.  These are exactly the old and rethreaded
ring phases.  The rigidity theorem is correct.

## 2. One transport role is exactly one incidence hexagon

For one role suppress indices and write

\[
 p=\{a,s\},
 \qquad q=\{a,z\},
 \qquad d\in B,
 \qquad H=(B-d)+a.
\]

The six vertices used in the fixed-ring construction are

\[
 \begin{array}{c|ccc}
 \text{lower}&I=H+d&A=H+s&C=H+z\\
 \text{upper}&U=H+d+z&Y=H+d+s&W=H+s+z.
 \end{array}
\]

The old matching is

\[
 IU,quad AY,quad CW,
\]

and the new matching is

\[
 IY,quad AW,quad CU.
\]

These are literally the two alternating perfect matchings of the incidence
hexagon on core `H` and active labels `d,s,z`.  Hence the degree ledger in
Theorem 2.1 is exact role by role.

The open transport path

\[
 A-W-C-U
\]

is the new--old--new half of this hexagon.  If two external pairs are
disjoint, a cross-pair gives two such half-hexes in series.  This verifies
the line-graph diameter-two statement.

## 3. Disjointness and protected-factor budget

For the fixed `c`-ring, role `(i,e)` has

\[
 s=b\ (e=0),
 \qquad s=a_{i-1}\ (e=1),
 \qquad z=z_e.
\]

The source pair `{a_i,s}` and target pair `{a_i,z_e}` intersect only in
`a_i`.  All source owners are distinct for `c>=3`; all targets are distinct
because `(i,e)` is recovered from `{a_i,z_e}`.

Distinct missing core labels `d_(i,e)` separate every nonroot physical
vertex belonging to different roles.  The two roles at root `I_i` share
only `I_i`; their old edges and new edges are distinct.  Therefore the old
bank has:

\[
 |D|=3(2c)=6c,
 \qquad
 \Delta(D)=2,
\]

with degree two only at the roots.  The hypothesis `m>=6c+2` gives
`6c<=m-2`, so the cited small protected-factor theorem applies exactly.

Toggling all role hexagons changes one spanning two-factor to another and
places all old ring edges.  The cyclic head shift merely replaces one
degree-one ring incidence at every owner while preserving degree two at
every root, so it produces the second factor phase.

## 4. Component rank

Each strict role hexagon meets at most three current cycles and can lower
component count by at most two.  Thus `2c` roles lower it by at most `4c`.

If the component--hexagon incidence multigraph is a tree and every atom has
three distinct component neighbours, it has

\[
 6c=|\operatorname {Comp}(F_0)|+2c-1
\]

edges, whence

\[
 |\operatorname {Comp}(F_0)|=4c+1.
\]

Contracting one atom star in an incidence tree preserves a tree.  Induction
therefore proves that all toggles are strict component merges and end in one
cycle.  This confirms both the hypertree criterion and the necessary
`4c+1` component-capacity bound.

## 5. Scope exclusions

The audit does not infer any of the following:

1. a prescribed Hamilton cycle contains the old transport matching;
2. the arbitrary factor completion has at most `4c+1` components;
3. the full `c=m` ring fits the `m-2` protected-edge budget;
4. the complete upper witness reservoir is present;
5. residence, cap, compiler, or regeneration guards survive.

Accordingly the correct status is:

\[
 \boxed{
 \text{fixed-size ring planting: proved;}\qquad
 \text{joint bounded/rooted component completion: open.}
 }
\]

