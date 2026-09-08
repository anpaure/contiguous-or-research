# Ramsey coordinate covers on the depth-three functional face: owner-forbidden rectangles and the support-three escape

**Date:** 2026-08-01  
**Lane:** K, functional attachment after an opened rolling reset  
**Status:** unconditional direct-cell obstruction and an exact smallest
two-sided-cover counterexample.  The result rules out bounded-state
Cartesian coordinate-cover hosts for the functional predecessor graph.  It
does not rule out occurrence-labelled non-Cartesian menus, complete literal
return paths, Boolean support-three packets, or the bidirectional reset
phase trade.

## 0. Verdict and source audit

The repository's relevant coordinate-cover statement is
`MATH_ASSESSMENT_SATURATED_ENDPOINT_MATRICES_MEDIAN_EXPANDER_AND_PROTECTED_RESET_GATE_20260801.md`.
It is a **conditional applicability theorem**, not a constructed Ramsey
host.  It distinguishes

* two-sided coordinate cover (every row and column is nonempty), from
* universal endpoint compatibility (every row--column pair has a complete
  literal return path).

Its entries are assumed to record compatible tail, head and owner turns,
all provider tickets, phase data, compiler hazards, and a common represented
exterior after contraction.  Therefore the assessment is a **downstream
combination lemma** for already constructed literal returns.  It does not
select the flag table or the functional bijection `theta`; using it for that
purpose would put the missing functional data inside every matrix cell.
This is not circular as a certification format, but it gives no existence
theorem for the present gate.

On the direct depth-three functional face, neither alternative supplies the
missing high-target table and functional attachment.

1. Universal Cartesian compatibility is incompatible with owner
   injectivity as soon as both shores contain two occurrences: every
   literal `2 x 2` predecessor rectangle has one common owner.
2. Two-sided cover is too weak: an explicit literal `m=4` block has no
   isolated row or column, has distinct lower targets, head targets and
   owners, but has Hall deficiency one.
3. More generally, a Cartesian host with `a` row states and `b` column
   states and a perfect predecessor matching has at most `ab` residual
   occurrences.  Thus no bounded-state Ramsey refinement can host the
   residual Catalan-sized problem.  At opened-reset `k=17`, it requires
   `ab>=1423`.

Separated chronology palettes do not change these set identities.  The
live escape is necessarily non-Cartesian: a support-three Boolean/hex
packet may change three root options jointly, and the bidirectional rolling
reset changes one owner attachment path and two predecessor parity paths
all at once.  Their remaining gate is a common occurrence-labelled lift,
not another endpoint-type Ramsey argument.

## 1. The literal functional cell

Fix `d=3`, `k=2m+1`, and one physical owner-alignment label `z`.  A selected
tail flag is written

\[
                         (S,z),\qquad |S|=m-2,               \tag{1.1}
\]

and an aligned head column is written

\[
                         (H,\gamma;z),\qquad |H|=m-1,
                         \quad\gamma\in H.                  \tag{1.2}
\]

The exact direct-cell law is

\[
 (S,z)\sim(H,\gamma;z)
 \quad\Longleftrightarrow\quad
 S\subset H,\quad\gamma\in S.                              \tag{1.3}
\]

Equivalently, the possible tails at `(H,gamma;z)` are

\[
                         (H-\{\beta\},z),
                  \qquad \beta\in H-\{\gamma\}.             \tag{1.4}
\]

The owner of the column is

\[
                         O(H,z)=H\cup\{0,z\}.                \tag{1.5}
\]

These are the normalized formulas in
`MATH_THEOREM_D3_QUOTIENT_FLAG_NORMAL_FORM_FUNCTIONAL_HALL_AND_COMPACT_CODESIGN_20260801.md`
and
`MATH_THEOREM_K_RESET_CONTRACTED_POINTED_SHADOW_REGULARITY_AND_MINIMAL_STAR_OBSTRUCTION_20260801.md`.
After contracting the opened reset bank, the same formulas hold on the
undeleted rows and columns.

## 2. Every direct rectangle is owner-monochromatic

### Theorem 2.1 (owner-forbidden `C4`)

Let `S_1\ne S_2` and let `(H_1,gamma_1;z)`,
`(H_2,gamma_2;z)` be distinct aligned head columns.  If all four direct
cells

\[
                         S_i\sim(H_j,\gamma_j;z)
                         \qquad(i,j\in\{1,2\})               \tag{2.1}
\]

are legal, then

\[
                         H_1=H_2=S_1\cup S_2                 \tag{2.2}
\]

and the two head columns have the same owner.

Consequently, for a functional head--owner bijection `theta`, the direct
predecessor graph `B_theta` is `C4`-free.

#### Proof

Both `S_1` and `S_2` are distinct `(m-2)`-subsets of the `(m-1)`-set
`H_j`.  Hence they are two different facets of `H_j`, so

\[
                         |S_1\cup S_2|=m-1,
                         \qquad H_j=S_1\cup S_2.             \tag{2.3}
\]

This holds for `j=1,2`, proving (2.2).  Formula (1.5) then gives

\[
                         O(H_1,z)=O(H_2,z).                  \tag{2.4}
\]

A functional attachment uses every owner once, so two distinct selected
head columns cannot form such a rectangle.  \(\square\)

The pointers `gamma_1,gamma_2` and any separated palette tags are irrelevant
to (2.4).  The obstruction is the Boolean owner identity itself.

### Corollary 2.2 (no direct universal endpoint matrix)

A direct functional block with at least two tail occurrences and at least
two head occurrences cannot have universal endpoint compatibility.  In
particular, the universal-cell hypothesis of the saturated endpoint-matrix
lemma cannot be instantiated by individual depth-three predecessor turns.

It may still be instantiated by a **compound literal return path** whose
internal turns and owners are occurrence-labelled.  That is the explicitly
conditional scope of the assessment theorem; such paths are not supplied
by a coordinate-cover or Ramsey statement alone.

## 3. Exact bounded-state Cartesian no-go

Partition the residual tail occurrences into row states

\[
                         L=L_1\dot\cup\cdots\dot\cup L_a
\]

and the head columns into column states

\[
                         R=R_1\dot\cup\cdots\dot\cup R_b.
\]

Call the host **Cartesian by state** if for every `(i,j)` either no direct
cell in `L_i x R_j` is offered or every cell in `L_i x R_j` is offered.
The state is required to include the physical alignment label `z`; thus an
offered block is a literal block of (1.3), not a quotient-only projection.

### Theorem 3.1 (state-product capacity)

If a Cartesian-by-state direct host admits a functional owner bijection and
a perfect predecessor matching, then

\[
                         |L|=|R|\le ab.                      \tag{3.1}
\]

In particular, a symmetric `s`-state host has at most `s^2` occurrences.

#### Proof

By Theorem 2.1, every offered state block `L_i x R_j` has

\[
                         \min\{|L_i|,|R_j|\}=1,              \tag{3.2}
\]

since otherwise it contains a `C4`.

Fix a row class `L_i`.  If `|L_i|>1`, then every neighbouring column class
is a singleton by (3.2).  There are at most `b` column classes, so

\[
                         |N(L_i)|\le b.                      \tag{3.3}
\]

Hall's inequality for the perfect matching gives `|L_i|<=b`.  The same
bound is trivial when `|L_i|=1`.  Summing over the `a` row classes proves
(3.1).  \(\square\)

### Corollary 3.2 (opened `k=17` lower bound)

After the seven protected reset turns are contracted, the residual problem
has `1423` tails and heads.  Any direct Cartesian state host satisfying the
functional theorem must obey

\[
                         ab\ge1423.                          \tag{3.4}
\]

For equal state counts this requires `s>=38`.  Hence no absolute
bounded-state coordinate cover can supply the missing functional table at
`k=17`, let alone uniformly in `m`.

This conclusion applies to a host whose cells are direct predecessor turns
and whose compatibility is determined by bounded endpoint states.  It does
not apply to occurrence-dependent entries, non-Cartesian menus, or compound
paths.  But those escapes must carry essentially the full occurrence-level
matching information which the bounded-state reduction was meant to avoid.

## 4. Two-sided cover still does not imply Hall

The preceding obstruction might suggest weakening universal compatibility
to one nonempty cell in every row and column.  The following literal block
shows that this loses exactly the needed conclusion.

### Proposition 4.1 (owner- and target-injective cover with deficiency one)

Take `m=4`, `k=9`, normalize at coordinate `0`, and use alignment `z=8`.
Let the four selected tail targets be

\[
 S_1=12,\qquad S_2=13,\qquad S_3=36,\qquad S_4=37,          \tag{4.1}
\]

and the four aligned head columns be

\[
\begin{aligned}
 g_1&=(123,1;8),& g_2&=(124,1;8),\\
 g_3&=(135,1;8),& g_4&=(367,3;8).
\end{aligned}                                               \tag{4.2}
\]

Intersecting their complete punctured-facet lists with (4.1) gives

\[
\begin{aligned}
 N(g_1)&=\{S_1,S_2\},&N(g_2)&=\{S_1\},\\
 N(g_3)&=\{S_2\},&N(g_4)&=\{S_3,S_4\}.                    \tag{4.3}
\end{aligned}
\]

Thus every row and every column is covered, but

\[
                         |N(\{g_1,g_2,g_3\})|=2<3.          \tag{4.4}
\]

The four owners

\[
 01238,\qquad01248,\qquad01358,\qquad03678                 \tag{4.5}
\]

are distinct, and their cyclic gap words are pairwise nonconjugate.  The
lower targets `S_i`, the immediate targets `S_i union {0}`, and the head
sets in (4.2) likewise lie in pairwise distinct cyclic orbits in their
respective rows (the four rank-two distances are `1,2,3,4`).  Hence neither
physical nor quotient owner/target injectivity repairs the missing Hall
cut.

#### Proof

Formula (1.4) gives the full predecessor pairs

\[
\begin{array}{c|c}
g_1&12,13\\
g_2&12,14\\
g_3&13,15\\
g_4&36,37.
\end{array}
\]

Intersect with (4.1), yielding (4.3).  Equations (4.4)--(4.5) are then
immediate.  \(\square\)

This is a local normalized block, not a completed quotient SCD selector or
an obstruction to every global table.  Its exact purpose is to refute the
implication

\[
 \text{two-sided coordinate cover + separated palettes + injective labels}
 \quad\Longrightarrow\quad\text{functional Hall}.          \tag{4.6}
\]

## 5. What Ramsey thinning can and cannot do

Suppose a Ramsey or finite-type argument makes direct endpoint
compatibility homogeneous on row and column state classes.

* If homogeneity means universal cells on a nontrivial state rectangle,
  Theorem 2.1 gives a repeated owner.
* If it means only a nonempty row and column margin, Proposition 4.1 gives
  Hall deficiency one even with distinct target and owner labels.
* If it refines until all useful cells are occurrence-specific, the state
  count must grow as in Theorem 3.1 or the entries must cease to be
  Cartesian.  That is no longer a bounded-state coordinate-cover proof.

Palette separation can make independently chosen **physical paths**
resource-disjoint, but it cannot change equations (1.3) or (1.5).  Thus the
Ramsey/separated-palette construction in its direct-cell form cannot supply
the missing nonregular `d=3` table and `theta`.

## 6. The exact non-Cartesian escape

The Boolean support-three packet and the rolling-reset phase trade remain
outside the obstruction.

### 6.1 Support-three packet

For a normalized flag `f=(S,z)`, the two high-target resources are

\[
                         T(f)=[S],\qquad P(f)=[S\cup\{0\}].  \tag{6.1}
\]

A three-root packet is resource-zero exactly when it separately permutes
the three `T` occurrences and the three `P` occurrences; on a fixed
alignment face it must also permute the three `z` occurrences.  The Latin
cross

\[
 (P_0,T_0),(P_1,T_1),(P_2,T_2)
 \longmapsto
 (P_1,T_2),(P_2,T_0),(P_0,T_1)                              \tag{6.2}
\]

is the smallest such non-Cartesian packet.  The external-puncture plus
protected-two-sum theorem proves it improves a fixed Hall shore when its
three literal root options exist outside the protected shore and preserve
all old neighbours.  It does not prove that every critical shore has such a
packet.  These statements are Theorems 2.1 and 4.3 of
`MATH_THEOREM_A_D3_NORMALIZED_RESOURCE_CIRCUITS_AND_FUNCTIONAL_CUT_DESCENT_BOUNDARY_20260801.md`.

### 6.2 Bidirectional reset

Changing the opened rolling reset from forward to reverse phase exports

1. one head--owner alternating path, and
2. two predecessor parity paths.

Edgewise phase mixing is impossible under owner injectivity: it creates the
closed reciprocal doubleton.  Therefore the phase change is itself a
compound non-Cartesian state transition.  It becomes useful only if the
ambient table supplies all three boundary returns as projections of one
common literal turn-triple lift.  This is the exact opened signature in
`MATH_THEOREM_K_BIDIRECTIONAL_ROLLING_RESET_FUNCTIONAL_ATTACHMENT_AND_DOUBLETON_GATE_20260801.md`.

The support-three packet has exactly the first possible arity for such a
lift.  A proof-safe bounded-interface programme is therefore:

1. keep only the phase bit and its three exposed boundary defects as the
   abstract state;
2. realize every transition by an occurrence-labelled support-three packet
   satisfying (6.2) and the frozen-alignment resource equation; and
3. verify the all-subfamily Rado/gammoid cuts of the reset-contracted phase
   router.

The last cuts are exactly Theorem 5.1 of
`MATH_THEOREM_K_RESET_CONTRACTED_DUAL_FUNCTIONAL_FLOW_AND_RADO_PHASE_ROUTER_20260801.md`.

This is a bounded **boundary** state, not a bounded Cartesian coordinate
host.  Its missing assertion is literal packet accessibility on every
critical Hall cut.

## 7. Exact boundary

Proved here:

* direct functional `C4`s are owner-monochromatic;
* bounded Cartesian endpoint-state hosts have capacity at most `ab`;
* two-sided coordinate cover plus separate palettes and injective labels
  does not imply Hall; and
* support-three/reset moves evade the obstruction only by being joint,
  occurrence-labelled, non-Cartesian transitions.

Not proved here:

* an all-`m` reset-compatible high-target table and functional `theta`;
* accessibility of a Latin-cross/support-three packet on every critical
  Hall cut;
* the common three-return lift for the opened reset; or
* connectivity, voltage, exterior residence, arbitrary upper shadows, and
  compiler feasibility.

The correct remaining theorem is therefore not a Ramsey coordinate-cover
lemma.  It is an occurrence-level support-three accessibility or
Rado/gammoid cut theorem for a prospectively chosen nonregular table.
