# Audit of the atomic FIFO portal tile and doublet host

**Date:** 2026-08-06  
**Audited source:**
`MATH_THEOREM_ATOMIC_FIFO_PORTAL_TILE_AND_BALANCED_DOUBLET_REDUCTION_20260806.md`  
**Method:** independent symbolic replay of every FIFO row and every orbit
incidence count; no computation or search  
**Verdict:** **PASS WITH EXPLICIT GLOBAL SCOPE.**  The local portal normal
form, the sharp `d-1` aperture, the atomic tile, the orientation-cylinder
transfer, the balanced-doublet fractional factor, and the augmented-host
pair-codegree ledger are valid under their stated central spare-coordinate
conditions.  The source does not prove integral doublet packing, a full
higher-codegree hierarchy, or the hereditary unordered macro cylinder.

## 1. Literal FIFO replay

For one portal macro let the first lower deletion be `a`, the first two
insertions be `(u,v)`, and put

\[
                         H=S_0-a+u+v.                      \tag{1.1}
\]

After transition one,

\[
                         S_1=H-v.                          \tag{1.2}
\]

If the queue after that transition has underlying set `R_c`, the level-one
owner is `(H-v) union R_c`.  Swapping `(u,v)` gives `(H-u) union R_c` and
changes the mark from `v` to `u`.  Hence the header `(H;R_1,...,R_h)` is
fixed and the state is exactly its missing coordinate.  This verifies
equations (1.3)--(1.5) of the source.

For the canonical header `R_c={a} dotcup Y_c`, with post-transition queue

\[
                         (x_2^c,\ldots,x_d^c,a),           \tag{1.3}
\]

the second lower deletion `g` and second insertion `v` give

\[
 S_2=H-g,
 \qquad
 Q_2^c=(x_3^c,\ldots,x_d^c,a,g),
 \qquad
 T_2^c=H\cup(R_c-\{x_2^c\}).                             \tag{1.4}
\]

Both `S_2` and `T_2^c` are invariant under the first-insertion switch.  The
map `x_2^c -> T_2^c` is injective and `x_2^c` has only `d-1` possible values
in `Y_c`.  This proves the aperture upper bound independently of every
deeper queue choice.

## 2. Atomic-tile replay

For portal `i`, the construction uses

\[
 S_0^i=H-\{u_i,v_i\}+a,
 \quad S_1^i=H-v_i,
 \quad \widetilde S_1^i=H-u_i,
 \quad S_2^i=H-g_i.                                      \tag{2.1}
\]

The `3q` labels in (2.1) are distinct.  Thus all first-role current,
first-role alternative, and second-role lower resources are distinct; the
initial resources are distinguished by their missing unordered port pair
and by the outside label `a`.  From transition three onward macro `i`
retains `p_i`, which no other macro uses.  This verifies lower privacy.

For owner privacy:

* `T_0^{i,c}` contains the private initial FIFO head `x_1^{i,c}`;
* `T_1^{i,c}` is the portal resource `(H-v_i) union R_c`;
* `T_2^{i,c}` is (1.4), and the `x_2^{i,c}` are distinct for fixed `c`;
* from level three onward `p_i` separates macros;
* a remaining member of the private `Y_c`, or the terminal insertion,
  separates copies.

Different levels cannot accidentally coincide: level zero misses two
`H`-labels and contains its private head; level one misses one `H`-label and
contains all of `R_c`; level two contains all of `H` and misses one member
of `R_c`; later levels contain `p_i`.  Therefore every alternative portal
bundle avoids the invariant bank, and all alternatives in the independent
tile are pairwise disjoint.  The exact simultaneous-toggle criterion applies
to every subset.  After a toggle, the same two-state component persists in
the reverse direction, so the hereditary rank really is `q`, not merely an
initial packing number.

The external label use is `O_h(d)`: `h(d-1)` tail labels, `hq` initial
heads, `q` private third insertions, and `O(d+h)` common continuation and
terminal labels.  This is compatible with the stated sufficient central
spare-coordinate inequality.

## 3. Cylinder replay

Conditional on the unoriented selected resources, distinct independent
portals use independent fair orientation coins.  Hence `m` prescribed
orientations on still-unexposed portals have conditional probability
`2^{-m}`.  This proves the cylinder division in Theorem 4.1, including the
stopped version restricted to unexposed occurrences.

Within one balanced doublet, either one prescribed orientation or the two
compatible opposite orientations have probability `1/2`.  For `q=1,2`,

\[
                         {1\over2}\le(2^{-1/2})^q.         \tag{3.1}
\]

Independence between doublets proves the `sqrt(2)` fixed-factor loss.  This
calculation transfers an **existing unordered** cylinder; it does not prove
that cylinder for the macro-selection law.  Its stopped form requires a
doublet-closed filtration.  After revealing one member alone, the mate's
orientation is forced, so no subunit conditional bound is valid for that
mate.  The augmented host naturally treats a doublet as one superedge, but
this closure must be preserved by any rounding proof.

## 4. Fractional-factor replay

A balanced doublet contains `2d` lower resources and `2h(d+1)` owners.
Uniform weight `M/(2d|D_h|)` gives total lower incidence `M` and owner
incidence `Mh(d+1)/d`.  Coordinate transitivity therefore gives lower load
one and owner load

\[
                         \eta_h={h(d+1)\over\rho d}.       \tag{4.1}
\]

The coefficients

\[
 \lambda_2=3-{\rho d\over d+1},
 \qquad
 \lambda_3={\rho d\over d+1}-2                            \tag{4.2}
\]

are nonnegative, sum to one, and make the mixed owner load one.  Each
doublet has two mark incidences, so its total weighted mark mass is `M/d`,
or `M/(kd)` at every coordinate.  Its `2h` pointed level-two occurrences
give total weighted mass `hM/d`; (4.2) and transitivity on the `Wr` pointed
owners give `1/[r(d+1)]`.  This verifies Theorem 4.3.

After adding `L^2` endpoint-slot copies, the three fixed-`h` degrees are

\[
 {2d|D_h|L^2\over M},
 \qquad
 {2h(d+1)|D_h|L^2\over W},
 \qquad
 {2|D_h|L\over k}.                                       \tag{4.3}
\]

The weight in Theorem 5.1 yields lower/owner load one and slot load
`M/(kdL)=L_*/L`.  An integral matching cannot repeat a slot, so its doublet
degree at a coordinate is at most `L`; opposite orientations then enforce
the mark cap literally.

## 5. Codegree replay

For same-shore resources, fixing one vertex and summing over a Johnson
distance orbit gives at most `O(d)` other roles per doublet.  The smallest
nontrivial orbit has size `Theta(k^2)`, proving `O(d/k^2)`.

For a lower-owner pair the relevant orbit has size

\[
                         {t\choose q}{k-t\choose d+q},    \tag{5.1}
\]

which is at least `binom(k-t,d)` over the `q=O(d)` template range.  The
reverse count gives `binom(r,d)`.  Two fixed distinct-coordinate slots have
one slot-pair realization over each base doublet, giving exactly
`1/[L(k-1)]` after division by the slot degree.  Same-coordinate slots never
co-occur.  Fixing one slot in a lower-slot or owner-slot pair contributes
`1/L`, while coordinate-orbit double counting contributes `O(1/k)`.

These checks give the displayed maximum pair-codegree estimate.  They do
not give power decay in the number of prescribed vertices; the only
unconditional higher-codegree consequence is the same pair bound after
retaining a pair.

For the separated doublet template, two cross-half level-two owners both
contain the port pair and have Johnson distance `j_*=4d-1`.  Conditional on
one pointed owner `(T,{u,v})`, its stabilizer is transitive on exactly

\[
                         {r-2\choose j_*}{k-r\choose j_*} \tag{5.2}
\]

possible partner owners.  There are only `h` partner-copy roles.  This
independently verifies the static merger bound

\[
 {h\over {r-2\choose j_*}{k-r\choose j_*}}
      =\exp[-\Omega(d\log d)].                            \tag{5.3}
\]

It does not prove that a stopped matching algorithm retains this conditional
spread.

## 6. Exact residual theorem

The audited local work reduces the colour/portal part to:

> Find a matching in the typed slot-augmented doublet host leaving
> `O(M/d)` lower resources, with a fixed-factor unordered marked cylinder
> through order `O(d)`, hereditarily after separator exposure, and with a
> terminal joinable queue state.  A doublet-orientation implementation must
> expose doublets atomically.

The host rank is `6d+6` or `8d+8`; its pair codegree ratio is
`O(d/k^2)`, but the requested relative leave is `O(1/d)`.  The existing
rank-two protected matching extension theorem is inapplicable, and the
currently audited fixed-rank nibble theorems do not provide constants
uniform in both parameters or the stopped cylinder.  Hence the remaining
lemma is genuinely a correlated growing-rank rounding statement.
