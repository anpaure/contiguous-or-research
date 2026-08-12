# Alternating collar sockets have a depth-sized PBBS body ladder

**Date:** 2026-08-05  
**Method:** explicit Dyck mountains, Johnson distance, and Hall's theorem;
no computation or search  
**Status:** unconditional component-abundance and co-selection theorem.  An
alternating sharp-shield socket has at least `2d+1` distinct PBBS body
components within owner-contact distance `d`.  Consequently every fixed
bank of such sockets can be assigned distinct local PBBS bodies.  The
corresponding owner paths have `O(d)` support.  Joint resource-disjoint
planting and the colour-compatible relative alternating returns which
retain the remaining PBBS body edges are not proved here.

## 1. An explicit PBBS height ladder

Put

\[
                         r=m-1,
             \qquad     n=2r+1=2m-1.                       \tag{1.1}
\]

Represent a rank-`r` PBBS state by a cyclic zero-one word with `r` ones
and `r+1` zeros.  For

\[
                         1\le h\le r                         \tag{1.2}
\]

define

\[
 A_h=1^h0^h(10)^{r-h}0.                                   \tag{1.3}
\]

Deleting the last unmatched zero leaves the Dyck word

\[
                         D_h=1^h0^h(10)^{r-h}.              \tag{1.4}
\]

### Lemma 1.1 (height and distance)

The PBBS largest-soliton height of `A_h` is exactly `h`, and

\[
                         d_J(A_1,A_h)=\lfloor h/2\rfloor.   \tag{1.5}
\]

#### Proof

The Dyck word (1.4) has maximum height `h`, proving the first assertion.

Inside the first `2h` positions, `A_1` has ones at the odd positions,
whereas `A_h` has ones at positions `1,...,h`.  Outside that interval the
two words agree.  The new ones are the even positions at most `h`, of
which there are `floor(h/2)`, and the deleted ones are the same number of
odd positions strictly between `h` and `2h`.  A Johnson move exchanges one
new and one deleted position, giving (1.5).  `square`

Let

\[
                         T_h=[n]\setminus A_h               \tag{1.6}
\]

be the corresponding rank-`m` Middle-Levels owner, and let `C_h` be its
component in the natural PBBS two-factor.

### Corollary 1.2 (distinct local body components)

The components

\[
                         C_1,C_2,\ldots,C_s                 \tag{1.7}
\]

are pairwise distinct for every `s<=r`.  Moreover `C_h` lies within
owner-contact distance `floor(h/2)` of `C_1`, where two PBBS components
are owner-contact adjacent if they contain Johnson-adjacent owners.

#### Proof

The largest soliton part is invariant on a PBBS component.  Lemma 1.1
assigns the different values `1,...,s` to the components in (1.7), so they
are distinct.  A shortest Johnson path from `A_1` to `A_h` complements to
a Johnson path from `T_1` to `T_h`; projecting its vertices to PBBS
components gives the asserted contact walk.  `square`

Taking `s=min(2d+1,r)` gives at least `2d+1` distinct components in contact
radius `d` whenever `2d+1<=r`, as holds in the eventual central regime.

## 2. The ladder begins at the sharp shield socket

Use the paired coordinate order

\[
              \kappa,x_1,y_1,\ldots,x_r,y_r               \tag{2.1}
\]

from the low-height sharp shield.  At one endpoint the complementary PBBS
state chooses `y_i` from every pair; after a cyclic rotation its word is

\[
                         (10)^r0=A_1.                       \tag{2.2}
\]

Thus `T_1` is literally an outer owner of that sharp shield.  A cyclic
rotation of the complete construction gives the same statement at every
rotated alternating socket.

For completeness, a literal shortest connector to `T_h` is obtained as
follows.  Put `g=floor(h/2)`.  In `A_1`, replace

\[
 q_i=2\lceil h/2\rceil+2i-1
             \quad\hbox{by}\quad p_i=2i,
             \qquad1\le i\le g.                            \tag{2.3}
\]

in any fixed order.  After all `g` exchanges the state is `A_h`.
Complementing and placing the common rank-`(m-1)` facet between successive
owners gives an incidence path

\[
 T_1-I_1-T^{(1)}-I_2-\cdots-I_g-T_h                 \tag{2.4}
\]

with `g+1` owners and `g` facets.  Its incidence length is at most `2d`
for `h<=2d+1`.

Every fixed facet is contained in at most two owners of this geodesic, and
every fixed owner contains at most two of its displayed facets.  Indeed,
facets or owners at path distance at least two differ in at least two
independent exchange pairs.  Thus adjoining a fixed number of these
connector paths preserves the constant-exposure hypothesis of the fixed
sharp-shield protected-factor theorem.

## 3. Fixed-bank Hall co-selection

Let `P_1,...,P_H` be a fixed bank of pairwise resource-disjoint opened
sharp-shield/collar paths, and suppose the outer socket of each `P_i` has
the alternating form (2.2), possibly after its own cyclic rotation.  Let

\[
 \mathcal B_i=\{C_{i,h}:1\le h\le2d+1\}                  \tag{3.1}
\]

be the rotated copy of the body ladder (1.7).

### Theorem 3.1 (distinct local body assignment)

If

\[
                         H\le2d+1\le r,                      \tag{3.2}
\]

there are pairwise distinct PBBS components

\[
                         B_i\in\mathcal B_i,
                         \qquad1\le i\le H.                 \tag{3.3}
\]

Every selected `B_i` is connected to the socket of `P_i` by a literal
owner path of Johnson length at most `d` and incidence length at most
`2d`.

#### Proof

Each list `mathcal B_i` contains `2d+1` distinct components by Corollary 1.2.
For every nonempty `J subseteq [H]`,

\[
        \left|\bigcup_{i\in J}\mathcal B_i\right|
             \ge2d+1\ge H\ge|J|.                           \tag{3.4}
\]

Hall's theorem gives the system of distinct representatives (3.3).
Equation (1.5) and the explicit lift (2.4) give the path bounds. `square`

No disjointness between the *lists* is required.  They may even coincide;
their common depth-sized cardinality already proves Hall for fixed `H`.
This SDR statement concerns component names.  It does not by itself choose
the connector paths resource-disjointly from one another and from the
already planted shields.

## 4. Protected planting and component accounting

Suppose additionally that the selected connector paths are pairwise
resource-disjoint and disjoint from the `H` shield/collar paths.  Their
additional protected incidence size is at most `2Hd=O(d)`, while their
lower-star and forced-facet exposures are at most `2H`.  Under this extra
premise, the proof of the fixed sharp-shield bank extension theorem applies
with its constant enlarged by `H`: for all sufficiently large `m`, the
complete prospectively selected bank extends to an unrooted spanning
owner/q1 two-factor.

At the level of the named subsystem, a successful relative realization
would contain at most `H` collar-to-body paths.  For the two-path `C8`
application, the adaptive-phase theorem would then give one factor
component containing both protected paths: keep the old phase if the
completion has already joined them, and use the `C8` phase otherwise.

Thus body abundance is unconditional, while the `O(1)` count for **named
protected** components is conditional only on realizing the selected
connector paths.  Nothing here says that the remaining unprotected factor
has `O(1)` components.

## 5. Exact boundary: contact paths are not relative returns

Theorem 3.1 removes the arbitrary-naming obstruction.  It does not prove
the relative graft demanded by the PBBS programme.

1. The incidence path (2.4) is a prospective protected path.  It need not
   be the symmetric difference of the fixed PBBS perfect matchings with a
   colour-compatible `O(d)` directed cycle cover.
2. The Hall SDR does not prove simultaneous physical disjointness of the
   selected connector paths.
3. Unrooted protected-factor extension may replace PBBS edges far outside
   the named bodies.  It does not retain the rest of `B_i` as a prescribed
   PBBS component.
4. The typed collar endpoint state must still be aligned with the first
   `d` body occurrences, or transported by a resident return packet.
5. The localized upper-backup occurrence paths can be protected
   simultaneously at occurrence level, but their common extension with
   the relative PBBS matching and typed cap is not supplied here.

The sharpened positive target is therefore:

> **Ladder-relative return lemma.**  For at least one representative
> `B_i` in each explicit list (3.1), lift the connector path (2.4) to two
> edge-compatible alternating returns in the PBBS exchange digraphs on
> `O(d)` matching-pair units, with the declared collar state and backup
> paths fixed.

Unlike arbitrary named grafting, this statement has no soliton-height
distance obstruction: every listed body is already at contact distance at
most `d`.

## 6. Dependencies

The height-distance obstruction and its support convention are in
`MATH_OBSTRUCTION_NAMED_RELATIVE_C8_GRAFT_HEIGHT_DISTANCE_20260805.md`.

The sharp shield and its fixed-bank extension are in
`MATH_THEOREM_FULL_UNION_SHIELDS_LOCALIZE_ALL_EXTERIOR_SPLICE_DAMAGE_20260805.md`
and
`MATH_THEOREM_FIXED_SHARP_SHIELD_BANK_EXTENDS_TO_MIDDLE_LEVELS_TWO_FACTOR_20260805.md`.

The adaptive `C8` phase theorem is in
`MATH_THEOREM_C8_RELATIVE_PBBS_ALTERNATING_GRAFT_AND_UPPER_BACKUP_20260805.md`.
