# Independent audit: fixed-orbit residence-four quotient cuts

Date: 2026-07-29  
Status: PASS after one editorial hardening; no solver or search used.

Audited source:
`MATH_THEOREM_AD_FIXED_ORBIT_RESIDENCE_QUOTIENT_WALK_CUTS_20260729.md`.

## 1. Strict boundary theorem

For one coordinate let `U` be its positive shore and `H=J(K,r)[U]`.
On a spanning simple two-factor `F`, `F[U]` has maximum degree two.  Its
path components are the nonconstant positive runs and its cycle components
are the constant-one factor components.  Under the stated strict finite-
cycle convention, residence four is therefore equivalent to every
component of `F[U]` having at least four vertices.

If a nonempty connected `S subseteq U`, `|S|<=3`, has zero selected
`H`-boundary, every `F[U]` component meeting `S` is contained in `S`, so a
short run exists.  Conversely the vertex set of a short path or cycle
component has zero selected boundary.  Disconnected sets add over their
`H`-components.  Theorem 1.1 is exact.

The constant correction is also exact: a simple factor has no one- or
two-vertex component, so the only constant positive component shorter than
four is a triangle.

## 2. Orbit projection and repeated orbit IDs

For an edge orbit `e`, the coefficient

\[
 d_e(a,S)=|E(e)\cap\delta_a(S)|
\]

is literal.  A nonloop orbit meets a fixed physical owner at most once; a
quotient-loop orbit meets it at most twice.  Hence
`0<=d_e(a,S)<=2|S|<=6`.  The support-only clause is equivalent to the
weighted row only because the variables are Boolean and the right side is
one.

For a labelled bracket walk, several displayed physical edges may belong
to the same orbit.  Deduplicating its support is sound: `y_e=1` selects the
entire physical orbit and hence every repeated physical edge in the walk.
At each internal physical vertex the displayed pair saturates degree two,
so the selected factor traverses that walk.  The source theorem now defines
“cyclically simple” explicitly, excluding repeated vertices and edges except
the common endpoints of a completed simple cycle.  The width-four walk
no-goods are therefore exact on the weighted degree-two face.

## 3. Burnside and row arithmetic

For one coordinate shore `H=J(15,7)`:

\[
 |V(H)|=6435,\quad |E(H)|=180180,
\]

\[
 T(H)=\binom{15}{6}\binom93+\binom{15}{8}\binom83=780780,
\]

and the number of connected triples is

\[
 6435\binom{56}{2}-2T(H)=8,348,340.
\]

Thus one labelled coordinate contributes

\[
 R_*=6435+180180+8,348,340=8,534,955.
\]

The old-coordinate label makes the `C_15` action free, so all fifteen old
coordinates still give exactly `R_*` row orbits.

For the fixed top coordinate, singleton and edge orbit counts are `429` and
`12,012`.  Only `rho^5,rho^10` can fix a connected three-set.  For either,
a rank-seven set adjacent to its translate has exactly one singly occupied
coordinate 3-cycle and two full 3-cycles.  There are

\[
 5\cdot3\cdot\binom42=90
\]

such vertices, hence `30` invariant triangles.  Therefore

\[
 R_{z,3}=\frac{8,348,340+30+30}{15}=556,560,
\]

\[
 R_z=429+12,012+556,560=569,001,
\]

and

\[
 R_{\rm res}=8,534,955+569,001=9,103,956.
\]

Adding `858` weighted factor equations and the independently proved
`764+764` both-`q1` rows gives

\[
 9,103,956+858+764+764=9,106,342
\]

indexed rows on exactly `27,456` binary edge-orbit variables.  Residence
adds zero auxiliaries.  The four exceptional `q1` target orbits retain
physical load coefficient three; their Boolean coverage rows remain support
clauses.

## 4. Scope verdict

PASS for arbitrary equivariant successor permutations and arbitrary zero,
nonunit, or unit component voltages.  The theorem is strict one-sided
positive residence.  Bordered residence uses the separately stated signed
coefficient inequality, and genuine bi-residence doubles the shore family.
No connectivity, opening, FRR, or compiler claim follows.

