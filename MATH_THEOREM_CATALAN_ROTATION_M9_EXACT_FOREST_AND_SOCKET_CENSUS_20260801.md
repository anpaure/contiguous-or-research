# An exact parity-completed rotation forest at `m=9`

Date: 2026-08-01  
Status: exact finite certificate and literal replay.  This extends the
rotation-factor census through `m=9`; it is not an all-`m` theorem.

## 0. Result

On a ground set of size `18`, there is a `C_18`-invariant selection of
ordered Boolean-diamond orbits with all of the following properties.

1. Every rank-eight lower colour occurs exactly once.
2. Every rank-ten upper colour occurs exactly once.
3. Every rank-nine middle vertex has physical degree at most two.
4. The physical rank-nine graph is a forest.
5. The complete nonfree antipodal sector is the deterministic quotient
   matching from the odd-rotation parity theorem.

Numerically,

\[
 \begin{array}{c|r}
 \text{selected quotient orbits}&2438\\
 \text{antipodal half-orbits}&14\\
 \text{literal physical edges}&43758\\
 \text{path components}&4862=\operatorname{Cat}_9\\
 \text{cycle components}&0.
 \end{array}                                                \tag{0.1}
\]

The middle-degree histogram is

\[
                         0^{938}1^{7848}2^{39834}.             \tag{0.2}
\]

In the signed quotient-frame representation, the factor has

\[
 \begin{aligned}
 e_{\rm ord}&=2424,&q_-&=14,\\
 c_{\rm ord}&=225,&u_-&=14,\\
 r_{\rm fr}&=2438,&\delta_{\rm fr}&=0.                       \tag{0.3}
 \end{aligned}
\]

Thus the exact frame criterion independently certifies acyclicity.

This is the first finite rotation-quotient factor beyond the previous
`m<=8` census.  The deterministic antipodal matching was fixed before the
SAT solve; only the full/full selector remained free.

## 1. Literal certificate replay

The candidate family consists of all outer-simple `C_18` edge orbits.  The
certificate gives one candidate ID for each lower necklace.  The replay
regenerates the complete candidate list from first principles and verifies:

* the selected IDs form exact lower- and upper-necklace permutations;
* developing the selected orbits gives literal lower and upper bijections;
* the 14 selected half-orbits are exactly the developed quotient matching
  between ranks four and five of `B_9/C_9`, up to canonical rotation;
* the literal rank-nine degrees satisfy the cap two;
* all 48,620 middle vertices form 4,862 paths and no cycle; and
* the signed-frame nullity is zero.

The independent replay is

`scratch/audit_catalan_rotation_m9_half_certificate_20260801.py`.

Its output is

`scratch/catalan_rotation_m9_half_certificate_20260801.audit.json`.

Script SHA-256:

`7fddaae550b381bac42c8c2df23c2ff756fec473796fff1939d53478b95f0ab8`

Audit SHA-256:

`6f5a44176a6ca177d67b18d3ac7ecd1aaabe39c89806fc20bda55f86bd18e3eb`

Canonical payload SHA-256:

`1c7224a014864f1e2dc3448091df6ac8e4f614a030586e643157abc36dee38ad`

The compact selected-orbit certificate itself is

`scratch/catalan_rotation_m9_half_full_20260801.audit.json`, SHA-256

`f48e74dbfaad4e761db2cee374ea5e01cfa2c2db6ce18f887192a12240a83bde`.

The resulting literal edge-set SHA-256 is

`005dfdc24b643e4bd3176548ee2ae0deeb00d31ec3b9404d4a4c7f2e0982f7c1`.

## 2. The parity completion is doing real work

An unconstrained exact cap-two solve also succeeds, but its physical graph
has three cycles.  Those three cycles form one rotation orbit, and the
signed quotient has frame nullity one.  Fixing the deterministic antipodal
matching and resolving the full/full selector produces the zero-nullity
certificate above.

This is finite evidence for the exact conditional Hall/component-colour
reduction:

* outer palettes and cap two alone can leave one topology unit;
* the half-sector completion can be chosen so that no ordinary quotient
  tree receives two negative loops; and
* the resulting frame-independent selector develops to a literal forest.

It is not evidence that every full-sector selector admits such a completion,
nor a proof that the conditional Hall row is automatically satisfiable for
all odd `m`.

## 3. Exact component and socket census

Every forest component has exactly two unused middle-capacity slots: the two
degree-one endpoints of a nontrivial path, or two parallel slots at an
isolated vertex.  Hence (0.2) gives

\[
 2\cdot938+7848=9724=2\operatorname{Cat}_9.                  \tag{3.1}
\]

The 4,862 components form 280 rotation orbits.  The endpoint-bearing middle
vertex orbits are

\[
 \begin{array}{c|r}
 \text{orbit size / free slots per vertex}&\text{number of orbits}\\ \hline
18/1&436\\
18/2&51\\
6/2&3\\
2/2&1.
 \end{array}                                                \tag{3.2}
\]

Thus the factor exposes a very large, rotation-invariant **topological
socket bank**.

The full path-length and component-orbit census is replayed by

`scratch/audit_catalan_rotation_m9_component_sockets_20260801.py`,

with output

`scratch/catalan_rotation_m9_component_sockets_20260801.audit.json`.

Script/audit SHA-256 values are

`5d472ee878f139c9e8c7b95592e4bdb4bf486331cf379217e0e440ddfcb092da`

and

`1ee9e9ea8e0de69875847a593dda548e4d2e96713ad82fac67d7ae3eb55a8ac5`;
the payload SHA-256 is

`00adfac40f20f8fa8eaa7d9d499e6cf1b7aa0d65df80e2ed1e390c96912aca72`.

## 4. What the sockets do not yet provide

The selected-orbit factor records outer colours and physical middle edges.
It does **not** contain:

* an ordering/orientation and concatenation of all path components into one
  source chronology;
* depth-`d` erosion addresses;
* exterior interval-union witness tickets;
* the octagon phase's eight/nine native source-ray anchors; or
* unused lower-compiler cells in one common cap.

Consequently the 9,724 slots in (3.1) are topology sockets, not yet the
strict-gammoid sink bank of a compiler exterior-ear theorem.  Nor can the
`8/9` octagon rays be read from this quotient certificate: those are typed
positions in an actual source word, data forgotten by the central factor.

The next exact interface is therefore an occurrence-labelled physicalization
of some of the 280 component orbits which simultaneously assigns:

1. path orientations and seam positions;
2. the constant octagon ray-anchor bank; and
3. distinct unused terminal compiler cells.

Only after that lift may the central sockets serve as endpoints of guarded
exterior ears.

## 5. Scope

Proved: one exact `m=9` rotation-invariant outer-bijective, cap-two physical
forest, with a deterministic complete antipodal sector and a literal compact
certificate.

Not proved: an all-`m` selector theorem, occurrence-labelled source
physicalization, a closed octagon host atlas, a compiler exterior-ear rank
bound, or `nu(k)<=B(k)+O(1)`.

