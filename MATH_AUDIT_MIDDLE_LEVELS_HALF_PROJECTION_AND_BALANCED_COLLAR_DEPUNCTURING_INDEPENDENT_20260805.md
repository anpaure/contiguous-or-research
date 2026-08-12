# Independent audit: middle-levels half projection and balanced-collar depuncturing

**Date:** 2026-08-05  
**Method:** pure mathematics; independent line-by-line symbolic audit; no
computation, search, or solver  
**Audited theorem:**
`MATH_THEOREM_MIDDLE_LEVELS_HALF_PROJECTION_AND_BALANCED_COLLAR_DEPUNCTURING_20260805.md`  
**Input SHA256:**
`bceed054d2bddb40ef946d487d745e3a53b36bb41be9938881f1ee091347a33e`  
**Corrected theorem SHA256:**
`7b091bf20ccd259edf61d1199f334ed784d0f829427138bfec5fdc365fe32734`

## 1. Verdict

The half-projection theorem, the opposite-half scope, all vertex/edge and
component counts, the run dictionary, the balanced-collar deletion and
restoration bijection, defect preservation, and the endpoint-role matching
criterion are correct.

One genuine scope overstatement was corrected.  The locations of the
vertical `z`-crossings determine the initial and terminal boundaries of the
projected paths, but do **not** by themselves determine the pairing/order of
the components under the later formal collar arcs.  The theorem already
carried the component-order hypothesis in Definitions 4 and 5; only the
summary's claimed equivalence was too strong.  The corrected text now keeps
the terminal bank and acyclic component order explicit.  This changes no
existence conclusion.

The audit verdict is

\[
 \boxed{\text{GO AFTER THE STATED SCOPE CORRECTION}.}
\]

## 2. Four-sector middle-levels decomposition

Let `|Omega|=2r` and distinguish `z`.  In the rank-`r/r+1`
middle-levels graph on `Omega dot union {z}`, the four sectors are exactly

\[
 A={\Omega\choose r},\qquad
 B=z+{\Omega\choose r-1},\qquad
 C_+={\Omega\choose r+1},\qquad
 D=z+{\Omega\choose r}.
\]

Containment permits precisely:

* `A-C_+` edges inside the `z`-absent half;
* `B-D` edges inside the `z`-present half; and
* the vertical perfect matching `X-(z+X)` from `A` to `D`.

There are no `B-C_+` edges because a set containing `z` cannot be contained
in a set omitting `z`.  An `A-D` containment has equal `Omega`-parts of
rank `r`, so it is necessarily the displayed vertical edge.  Thus the
three-sector assertion is exact.

The layer counts are

\[
 |A|=|D|=W={2r\choose r},\qquad
 |B|=|C_+|=U={2r\choose r+1},
\]

and

\[
 C=W-U={W\over r+1}=\operatorname{Cat}_r.
\]

## 3. The `z`-free half projection

Fix a Hamilton cycle `H`.  Each `R in C_+` has both cycle neighbours in
`A`.  They are two distinct rank-`r` facets `T_R,H_R` of `R`, so

\[
 T_R\cup H_R=R,
\]

and they differ by one Johnson exchange.  The union recovers `R`, hence two
different upper vertices cannot project to the same Johnson edge.  The
projected edge count is therefore exactly `U`, and the edge-union map is a
bijection onto the entire rank-`r+1` palette.

At `X in A`, the Hamilton cycle uses its unique vertical edge either zero
or one times.  Hence

\[
 d_F(X)=2-\mathbf 1_{\{X-(z+X)\in H\}}\in\{1,2\}.
\]

Thus the projection spans all `W` owners and has maximum degree two.  A
cycle component in the projection would lift to an alternating
`A-C_+` cycle in which every participating vertex has both of its `H`
edges internal.  It would be a whole connected component of `H`, impossible
because `B,D` are nonempty.  The projection is consequently a linear
forest.

It has

\[
 |E(F)|=U=W-C,
\]

so it has exactly `C` components.  Its degree-one vertices are precisely
the `A` owners whose vertical edge lies in `H`.  There are two endpoints
per path, hence exactly `2C` selected vertical edges.  This independently
verifies Theorem 2.1, including the endpoint and vertical-edge counts.

## 4. Opposite half and exact scope

For `z+L in B`, its two `D`-neighbours in `H` have the form `z+X,z+Y`,
where `X,Y` are distinct rank-`r` supersets of the rank-`r-1` set `L`.
Consequently

\[
 X\cap Y=L.
\]

Deleting `z` therefore projects the `B-D` half to another spanning
`C`-path forest on the same owner set whose edge intersections enumerate
all rank-`r-1` colours exactly once.  The two projected forests share the
same endpoint set (both endpoint sets record the selected vertical edges),
but their edge sets need not agree.  In particular, the theorem proves an
upper-exact forest and a separate lower-exact forest; it does not prove both
palettes on one forest.  The source states this limitation correctly.

## 5. Run dictionary

Removing the `2C` vertical edges from the cyclic Hamilton traversal leaves
alternating `z`-absent and `z`-present arcs.  Hence there are exactly `C`
maximal arcs of each type.  Suppressing the intervening `C_+` vertices in
one `z`-absent arc gives exactly one path component of the upper
half-projection.  If the arc contains `ell` owners in `A`, the projected
path contains `ell` vertices.  The absent arcs partition `A`, so

\[
 \sum_{i=1}^{C}\ell_i=W.
\]

A stem with `s` edges has `s+1` owner vertices.  Thus prescribing it as an
initial component segment requires a distinct absent run of owner length at
least `s+1`, as claimed.  A vertical crossing at `M_0` certifies the initial
boundary and one at `P` certifies a terminal boundary.  Those boundary
locations do not, without an additional hypothesis, prescribe which
terminal is joined to which initial component; this is the correction made
to the theorem.

## 6. Balanced-collar count and deletion audit

For one collar

\[
 P,M_0,M_1,\ldots,M_h,N,
\]

put `s=h+1`.  Its nonrepeated stem

\[
 M_0-M_1-\cdots-M_h-N
\]

has:

* `s+1=h+2` owner vertices;
* `s=h+1` edges;
* exactly `s` distinct upper colours `U_1,...,U_h,U_*`.

The deleted owner set is only `M_0,...,M_h`, so it has `s` vertices.  The
endpoint `N` remains.  The omitted left seam `P-M_0` has colour `U_1`,
which is already the colour of `M_0-M_1`; it is the unique forced repeat.

For `b=C-1` owner-disjoint collars with mutually disjoint stem palettes,

\[
 |R|=bs,\qquad |\mathcal U_B|=bs,
\]

and therefore

\[
 |V_0|=W-bs,
 \qquad
 |\mathcal U_0|=U-bs=|V_0|-C.
\]

If a stem is an initial segment of a path component, deleting
`M_0,...,M_h` removes exactly its `s` stem edges and merely truncates the
component to the initial endpoint `N`.  It neither splits nor deletes the
component.  Distinct stem components therefore leave exactly `C`
components.  Since the deleted edges carry exactly `mathcal U_B`, the
remaining edge-union map is a bijection onto `mathcal U_0`.

Conversely, at an exposed initial endpoint `N`, adjoining

\[
 M_0-M_1-\cdots-M_h-N
\]

adds `s` new owners and `s` edges to the same component, creates no cycle,
and restores exactly `mathcal U_B`.  Owner-disjointness allows all
attachments simultaneously.  These deletion/restoration operations are
literal inverses.

The endpoint/path-order conditions are essential and are now explicit:
each `N_j` is an initial endpoint, each `P_j` is a terminal endpoint, and
the component arcs `P_j -> N_j` form a directed spanning path on the `C`
components.  After restoring the stems, these are exactly the formal left
seams `P_j -> M^j_0`.  Adding the `C-1` seams gives

\[
 (W-C)+(C-1)=W-1
\]

edges on all `W` owners, hence one Hamilton path.  It covers every upper
colour and adds exactly one second occurrence of `U^j_1` per collar.

## 7. Defect preservation

Suppose a collar-structured spanning forest has upper-palette defect `D`,
all missing and repeated colours lie outside `mathcal U_B`, and every
colour of `mathcal U_B` occurs only on its declared stem.  Deleting the
stems removes one occurrence of every `mathcal U_B` colour and no
complementary occurrence.  The missing/repeated multiset on `mathcal U_0`
is therefore unchanged.  Restoring the stems reverses this operation, and
adding the left seams contributes only the declared `C-1` repeats.  Thus
the number of punctures does not multiply the residual defect.  The source
correctly makes the exclusivity hypotheses explicit; without them the
corollary would be false.

## 8. Three-partite endpoint matching equivalence

For a `C`-component oriented path forest, its `C` initial endpoints are

\[
 \mathcal S=\{M^j_0\}_{j<C}\cup\{a_*\},
\]

and its `C` terminal endpoints are

\[
 \mathcal T=\{P_j\}_{j<C}\cup\{z_*\}.
\]

The active tail and head role copies have sizes

\[
 |\mathcal X\setminus\mathcal T|
 =|\mathcal X\setminus\mathcal S|
 =W-C=U,
\]

matching the upper-colour part.  An order-`U` matching of atoms

\[
 (T\cup H,T,H)
\]

that saturates all three parts gives outdegree one at every nonterminal,
indegree one at every nonsource, and zero in the omitted roles.  Thus its
directed graph is the union of `C` source-to-terminal paths (isolated
source/terminal coincidences included) and possible directed cycles.

The fixed `C-1` formal arcs use all but one omitted tail role and all but
one omitted head role.  The augmented graph has exactly

\[
 U+(C-1)=W-1
\]

distinct directed edges.  With indegree and outdegree at most one, any
undirected cycle is necessarily a directed cycle.  Hence absence of a
directed cycle makes the augmented graph a forest with `W-1` edges on `W`
vertices, so it is one spanning directed path.  Conversely a collar-adapted
Hamilton path clearly yields the required matching.  Requiring all named
stem atoms makes each `M^j_0` path begin with its prescribed stem.  This
proves the equivalence in Theorem 5.1.

If one potential `phi` strictly increases along every selected atom and
every formal collar arc, no directed cycle is possible.  Thus on a fixed
forward face, the endpoint and graphic condition really does reduce to one
protected perfect matching in the balanced three-partite atom system.  The
potential condition is sufficient, not asserted necessary, and the theorem
does not assert that this protected matching exists.

## 9. Exact remaining scope

The audited result establishes only:

1. an unconditional **unprotected, upper-only** Catalan forest, by applying
   the Middle Levels Theorem;
2. a separate lower-only forest from the opposite half;
3. an exact deletion/restoration equivalence for an already supplied collar
   bank with explicit endpoint and component-order conditions; and
4. an exact matching formulation, with a sufficient common-potential face.

It does **not** establish:

* one forest carrying both immediate palettes;
* a middle-levels Hamilton cycle whose half-projection contains the
  Catalan-scale protected stem bank;
* the prescribed component order merely from vertical-crossing positions;
* residence, arbitrary-width/deeper upper witnesses, named lower flags, or
  the terminal common cap; or
* a complete universal word or any new value of `nu(k)`.

The corrected theorem states these exclusions.  The protected
middle-levels-cycle problem remains open and is the exact owner/upper-q1
frontier on this route.
