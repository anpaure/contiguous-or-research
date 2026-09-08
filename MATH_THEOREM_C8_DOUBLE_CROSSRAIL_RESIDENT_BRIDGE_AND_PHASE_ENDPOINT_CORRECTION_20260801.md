# Both folded-C8 cross banks fit one resident Johnson bridge

Date: 2026-08-01  
Lane: corrected C8 endpoint / physical prefix bank  
Status: unconditional all-`d` local owner/source construction, plus an exact
finite correction to the authenticated endpoint census.  The local bridge
carries both zero-block cross matchings in one maximal-envelope cap state.
It extends to a thirteen-component protected forest carrying all sixteen
canonical folded upper values.  Embedding that protected forest into one
spanning carrier while transporting the exterior compiler is not proved.

## 0. Outcome

There are two separate conclusions.

First, the existing one-ended endpoint audit omitted a literal family which
is present at the other end of its descending filler block.  On the first
symmetry seam, the old phase contains the complete paired bank

\[
             P_0(j)\longleftrightarrow S_1(j+1),
             \qquad 1\le j<d,                         \tag{0.1}
\]

and on the second symmetry seam, the new phase contains

\[
             P_1(j)\longleftrightarrow S_0(j+1).
                                                               \tag{0.2}
\]

Each ticket in (0.1)--(0.2) uses two adjacent disjoint physical cells.  The
prefix cells are released from the target-labelled transported background
matching; the suffix cells are outside its image.  This is exact in the
authenticated folded factors for `2<=d<=12`.  It does **not** put (0.1) and
(0.2) into one phase state: the two complete banks occur on the two
symmetry-related seam/phase choices.

Second, there is a dimension-uniform bridge which does put both banks into
one state.  It has:

* `2d+4` distinct rank-`r` owners in one Johnson path;
* `2d+3` distinct immediate lower colours;
* strict depth-`d` residence;
* one exact maximal-envelope source antecedent;
* `4(d-1)` pairwise-distinct ray cells forming the two cross matchings; and
* four of the sixteen canonical folded upper values.

Twelve disjoint two-owner components supply the remaining twelve upper
values.  Their union with the bridge is a componentwise resident thirteen-component
forest on `2d+28` owners with `2d+15` distinct lower colours and all sixteen
upper values.

Thus the physical prefix occurrence bank is no longer missing locally.
The remaining theorem is a protected embedding/background theorem for this
explicit `O(d)` forest.

## 1. The endpoint correction

Use the notation of
`MATH_THEOREM_C8_BOUNDARY_RAY_CROSSMATCH_FOREST_ACTUATOR_20260801.md`.
After splitting the endpoint, its local source begins

\[
 \{z,b\},\ \{z,c\},\ \{z,c,f_d\},\ldots,
 \{z,c,f_2\},\ \{z,c,f_1\}.                         \tag{1.1}
\]

The earlier theorem used only the left intervals

\[
                    I^S_j=[1,d-j+1].                 \tag{1.2}
\]

There is also the right family

\[
                    I^P_j=[d-j+2,d+1].               \tag{1.3}
\]

Directly,

\[
 \operatorname {OR}(I^S_j)=\{z,c\}\cup F[j+1,d],
 \qquad
 \operatorname {OR}(I^P_j)=\{z,c\}\cup F[1,j].     \tag{1.4}
\]

Moreover

\[
                 \max I^S_j+1=\min I^P_j.            \tag{1.5}
\]

So every pair is an adjacent disjoint two-cell ticket and all `2d-2` cells
are distinct.

On the first authenticated seam, the right-end base is `c=a_3` in both
phases.  Hence its old phase has `P_0` together with `S_1`, while its new
phase has `P_0` together with `S_0`.  On the symmetry-related seam, the
right-end base is `c=a_1` in both phases.  Hence its new phase has `P_1`
together with `S_0`, while its old phase has `P_1` together with `S_1`.
This proves (0.1)--(0.2) and also explains why one fixed seam does not close
both cross banks.

The prefix addresses are in the transported full-block image.  However,
every transported old address landing at `I^P_j` has value exactly
`P_epsilon(j)`: the only address collisions in the endpoint map have one
common set value.  Release those prefix targets from the old background
matching and reassign them to (1.3).  Every remaining transported edge then
avoids all cells (1.2)--(1.3).  If the suffix masks are also vertices of that
same old target matching, their old edges must be released as well before
the suffix cells are added; being outside the transport image gives cell
privacy but not target-shore privacy.

This is literal target-equality, one-vertex-per-mask transport only.  In a
mere containment incidence graph, two distinct target supersets may use two
equal-core old cells and then collide under the address map.  The underlying
address map can merge old occurrences having the same OR and can increase
their width.  It therefore does not preserve arbitrary protected
multiplicities, exact-width/deadline rows, or chronology/address guards
without a separate retained-edge replay.

## 2. The double-crossrail owner path

Fix `d>=2`.  Let

\[
 F=\{f_0,f_1,\ldots,f_d,f_{d+1}\},
 \qquad F^\circ=\{f_1,\ldots,f_d\},                  \tag{2.1}
\]

and let `K,z,a_1,a_3` and the fillers be pairwise disjoint.  Assume

\[
                         |K|=r-d-3.                   \tag{2.2}
\]

Put

\[
 U=K\cup\{z,a_1,a_3\}\cup F^\circ,
 \qquad M_+=U\cup\{f_{d+1}\},
 \qquad M_-=U\cup\{f_0\}.                            \tag{2.3}
\]

For `1<=i<=d`, define

\[
 G_i=M_+-\{f_i\},\qquad H_i=M_--\{f_i\},            \tag{2.4}
\]

and define four chord endpoints

\[
\begin{aligned}
 B&=M_+-\{a_3\},& A&=M_--\{a_3\},\\
 D&=M_--\{a_1\},& E&=M_+-\{a_1\}.
\end{aligned}                                         \tag{2.5}
\]

Consider the owner word

\[
 \boxed{
 G_1,G_2,\ldots,G_d,B,A,H_1,H_2,\ldots,H_d,D,E.}
                                                               \tag{2.6}
\]

### Theorem 2.1 (owner, palette, and upper ledger)

The word (2.6) is a simple rank-`r` Johnson path.  All its `2d+3`
intersections are distinct.  Its upper-union support is exactly

\[
 \boxed{
 \left\{
 M_+,
 (K\cup\{z,a_1\}\cup F),
 M_-,
 (K\cup\{z,a_3\}\cup F)
 \right\}.}                                           \tag{2.7}
\]

#### Proof

All displayed owners have size `|K|+d+3=r`.  Consecutive owners are
different facets of one rank-`r+1` set, except for the two chord edges
`BA,DE`; these exchange `f_0` and `f_(d+1)`.  Hence every step is Johnson.

The intersections, in order, are

\[
\begin{aligned}
 &M_+-\{f_i,f_{i+1}\} &&(1\le i<d),\\
 &M_+-\{f_d,a_3\},\quad
   K\cup\{z,a_1\}\cup F^\circ,\\
 &M_--\{a_3,f_1\},\\
 &M_--\{f_i,f_{i+1}\} &&(1\le i<d),\\
 &M_--\{f_d,a_1\},\quad
   K\cup\{z,a_3\}\cup F^\circ.
\end{aligned}                                         \tag{2.8}
\]

The boundary filler and active-label signatures distinguish the lines of
(2.8), and the omitted pair distinguishes values within one line.  Thus
they are all different.  The `G` edges have union `M_+`, the first chord has
union `K+za_1+F`, the `H` edges have union `M_-`, and the second chord has
union `K+za_3+F`.  This proves (2.7). \(\square\)

### Theorem 2.2 (exact residence)

Every internal positive coordinate run in (2.6) has length at least `d+1`.

#### Proof

Coordinates in `K union {z}` persist throughout.  Coordinate `a_1` occurs
from `G_1` through `H_d`, a run of length `2d+2`; coordinate `a_3` has a
left-clipped `G` run and the internal/right run `H_1,...,H_d,D,E` of length
`d+2`.  Coordinate `f_0` has the run `A,H_1,...,H_d,D` of length `d+2`.
Coordinate `f_(d+1)` has the safe run `G_1,...,G_d,B` of length `d+1` and
a right-clipped terminal occurrence at `E`.

For an internal filler `f_s`, its two absences are `G_s` and `H_s`.  The
run strictly between them is

\[
 G_{s+1},\ldots,G_d,B,A,H_1,\ldots,H_{s-1},           \tag{2.9}
\]

whose length is

\[
                  (d-s)+2+(s-1)=d+1.                 \tag{2.10}
\]

The other two runs meet the path boundaries. \(\square\)

## 3. One maximal-cap source carrying both cross banks

Let `T` be the owner path (2.6), indexed from zero, and let

\[
 E_p=\bigcap_{\max(0,p-d)\le i\le\min(2d+3,p)}T_i
 \qquad(0\le p\le3d+3)                               \tag{3.1}
\]

be its maximal depth-`d` source envelope.

Start with the source word `(E_p)` and replace two disjoint `d`-position
blocks.  At positions

\[
                         p=d+s\qquad(1\le s\le d)     \tag{3.2}

put

\[
 Q_s^{(1)}=
 \begin{cases}
 K\cup\{z,a_1,f_s\},&s\in\{1,d\},\\
 \{f_s\},&1<s<d,
 \end{cases}                                         \tag{3.3}
\]

and at positions

\[
                         p=2d+2+s\qquad(1\le s\le d) \tag{3.4}
\]

put

\[
 Q_s^{(3)}=
 \begin{cases}
 K\cup\{z,a_3,f_s\},&s\in\{1,d\},\\
 \{f_s\},&1<s<d.
 \end{cases}                                         \tag{3.5}
\]

Call the resulting source word `Q`.

### Theorem 3.1 (cap legality and exact dilation)

Every new letter is nonempty and lies in its maximal cap `E_p`, and

\[
                              D^dQ=T.                 \tag{3.6}
\]

#### Proof

At the left rail position `d+s`, the covering owners are

\[
 G_{s+1},\ldots,G_d,B,A,H_1,\ldots,H_{s-1},          \tag{3.7}
\]

with empty ranges suppressed.  None omits `f_s`; the two endpoint active
letters in (3.3) are also contained in every relevant owner.  This proves
`Q_s^(1) subseteq E_(d+s)`.  At the right rail position `2d+2+s`, the
covering owners begin after `H_s`; none omits `f_s`, and all relevant
owners contain the required `a_3` at the two endpoint positions.  This
proves the second cap inclusion.

It remains to prove equality after dilation.  For `G_s`, the left rail
prefix `Q_1^(1),...,Q_(s-1)^(1)` supplies exactly the fillers which are not
already forced by unchanged maximal cells in its window.  The windows of
`B,A` see the complete left rail, whose union is

\[
                         K\cup\{z,a_1\}\cup F^\circ; \tag{3.8}
\]

their two adjacent unchanged cap cells add respectively `f_(d+1)` and
`f_0`.  For `H_s`, the suffix of the left rail supplies
`F[s+1,d]` and the prefix of the right rail supplies `F[1,s-1]`; the omitted
coordinate is precisely `f_s`.  Finally the windows of `D,E` see the whole
right rail, of union

\[
                         K\cup\{z,a_3\}\cup F^\circ, \tag{3.9}
\]

and their unchanged boundary cells add `f_0,f_(d+1)`.  Thus every owner
window reconstructs its displayed value.  Since all source letters were
already below their envelopes, no owner can overshoot. \(\square\)

### Theorem 3.2 (both physical cross matchings)

For `1<=j<d`, the left rail has the adjacent disjoint cells

\[
 [d+1,d+j],\qquad[d+j+1,2d],                         \tag{3.10}
\]

of respective values

\[
 P_1(j)=K\cup\{z,a_1\}\cup F[1,j],\qquad
 S_0(j+1)=K\cup\{z,a_1\}\cup F[j+1,d].              \tag{3.11}
\]

The right rail has the adjacent disjoint cells

\[
 [2d+3,2d+2+j],\qquad[2d+3+j,3d+2],                 \tag{3.12}
\]

of values

\[
 P_0(j)=K\cup\{z,a_3\}\cup F[1,j],\qquad
 S_1(j+1)=K\cup\{z,a_3\}\cup F[j+1,d].              \tag{3.13}
\]

All `4d-4` cells are distinct.  Each pair in (3.10) has constant union
`K+za_1+F^circ`, and each pair in (3.12) has constant union
`K+za_3+F^circ`.  Hence these are literal realizations of both zero-block
cross perfect matchings in one owner/cap state.

This is a mask-level realization on newly addressed cells.  A bridge prefix
has width `j` and its suffix has width `d-j`.  In the authenticated endpoint
construction of Section 1, the cell carrying the same suffix mask has width
`d-j+1`.  Set identity therefore does not transport an exact-width, phase,
or address type; such a guard must accept the new bridge occurrence or be
rehosted explicitly.

#### Proof

Equations (3.11) and (3.13) follow by taking prefix and suffix unions of
(3.3) and (3.5).  The two intervals in one ticket partition its rail and
the two rails occupy disjoint source positions. \(\square\)

All `4d-4` displayed target masks are distinct.  Thus the owner rows and
both cross banks have one exact local common-cap witness, namely `Q` itself.
More precisely, intersecting the owner caps with every incident cross-row
target gives the maximal letters

\[
 K_p^*=\begin{cases}
 K\cup\{z,a_1,f_s\},&p=d+s,\ 1\le s\le d,\\
 K\cup\{z,a_3,f_s\},&p=2d+2+s,\ 1\le s\le d,\\
 E_p,&\text{off the two rails}.
 \end{cases}                                           \tag{3.14}
\]

They are nonempty, contain the displayed source `Q` pointwise, and
reconstruct every owner and cross row.  Hence an additional lower-bound
vector `L` is locally compatible exactly when `L_p subseteq K_p^*` at every
position (before any further outside row is intersected).  In particular a
lower row forcing `a_3` on the left rail, or `a_1` on the right rail, fails.
This is not an incumbent-matching transport theorem.  In the ordinary
one-target-per-mask compiler, an ambient matching must first release all
`4d-4` cross target vertices.  Its retained edges then require either an
injective old-to-new literal address map preserving every occurrence guard,
or a fresh residual Hall matching in `Q`.  No such address map is constructed
in this theorem.  With occurrence-labelled equal-mask copies, explicit
cell avoidance is additionally required.

## 4. Completing all sixteen local upper values

Assume additionally that the ground set contains two further active
coordinates `a_0,a_2`; equivalently this local completion uses `r+4`
distinct coordinates and requires `k>=r+4`.  The canonical sixteen
folded upper values consist of the eight high values

\[
 K\cup A\cup F,
 \quad
 A\in\{za_0,za_1,za_2,za_3,
       a_0a_1,a_1a_2,a_2a_3,a_3a_0\},                \tag{4.1}
\]

and the eight boundary values

\[
 K\cup R\cup F^\circ\cup\{b\},
 \quad
 R\in\{za_0a_2,za_1a_3,a_0a_1a_2,a_0a_2a_3\},
 \quad b\in\{f_0,f_{d+1}\}.                         \tag{4.2}
\]

The bridge already carries the two high values with active signatures
`za_1,za_3` and the two boundary values with signature `za_1a_3`.

For each of the other six values `K union A union F` in (4.1), take the isolated
Johnson edge between its facets obtained by deleting `f_0` and
`f_(d+1)`.  For each of the other six values in (4.2), take the isolated
edge between its facets obtained by deleting `f_1` and `f_2`.

### Theorem 4.1 (sixteen-support protected forest)

The bridge together with these twelve edges is a componentwise resident
forest with:

\[
 \boxed{
 13\text{ components},\qquad
 2d+28\text{ owners},\qquad
 2d+15\text{ edges}.}                                 \tag{4.3}
\]

Every owner is distinct, every lower edge colour is distinct, and its upper
support is exactly the sixteen values (4.1)--(4.2).

#### Proof

Different active signatures distinguish the auxiliary high components,
the auxiliary boundary components, and the bridge.  The two boundary
choices in (4.2) are distinguished by `f_0` versus `f_(d+1)`.  Thus all
twenty-four auxiliary owner facets are distinct and disjoint from the
bridge owners.  Their intersections retain the same active/boundary
signature and delete the chosen filler pair, so all auxiliary lower colours
are distinct and none equals a value in (2.8).  Their unions are, by
construction, precisely the twelve missing values.  Every isolated edge is
resident as a two-vertex component by boundary clipping, and Theorem 2.2
handles the bridge.  This last assertion is componentwise: an arbitrary
later concatenation or spanning-factor embedding need not preserve those
clipped runs.  A protected completion must extend the endpoint runs or
retain the corresponding component boundaries. \(\square\)

## 5. Exact frontier

This theorem closes the previously missing **local physical prefix banks**.
It also removes the local all-sixteen-support objection: the protected
forest has that support literally, not merely by a counter identity.

Three global rows remain.

1. **Protected owner embedding.**  The `O(d)` owner/lower-colour forest must
   be embedded in a spanning middle owner factor without duplicating its
   owners or consuming the protected upper witnesses.  Its thirteen
   components are constant in number, but a suitable protected completion
   theorem is still required.  The small fixed-`H` planting theorem supplies
   only an abstract owner/lower-incidence extension; it does not preserve
   source addresses or the clipped residence flags of the auxiliary edges.
2. **Background compiler.**  The source `Q` is prospectively planted below
   one maximal cap.  Unlike a pure full-block split, it does not by itself
   transport an arbitrary incumbent exterior matching.  A protected
   triangular/background matching must be selected jointly or returned by
   an injective literal address theorem.  That theorem must preserve width,
   deadline, boundary, chronology and phase guards.  Once such a literal
   matching exists and the cross target vertices are released, the word `Q`
   itself proves one common-cap state; common-cap is not a second Hall gate.
3. **Regeneration.**  A same-parity induction must reproduce or recycle the
   bridge state with bounded total physical charge.

The important quantifier change is that neither a second reflected endpoint
socket nor a phase-address isomorphism is needed for the ray bank itself.
Both cross banks coexist in the one explicit bridge (2.6)--(3.5).

## 6. Replays

The actual endpoint correction is replayed by

```text
scratch/audit_c8_actual_phase_two_ray_crossbank_20260801.py
  SHA-256 bc635c1401b7abe71c977dd96247062611ef58e165489a87a4ccf4ce30dbc146
scratch/c8_actual_phase_two_ray_crossbank_20260801.audit.json
  SHA-256 a802b7c3de50985e3026f65e70ce9da0f6effa5a33d9b777d676b147368323db
```

It reconstructs both authenticated symmetry seams and both phases for every
`2<=d<=12`.

The dimension-uniform bridge and sixteen-support forest are replayed for
every `2<=d<=64` by

```text
scratch/audit_c8_double_crossrail_resident_bridge_20260801.py
  SHA-256 23be11a67d06218dc9869004605766e3d5984426728b49a00c2d78879e682f3e
scratch/c8_double_crossrail_resident_bridge_20260801.audit.json
  SHA-256 e9e1ec35c45bf569085f68a109f0971d06ba1a19c4303a0727519cca15f576bc
```

The proof is dimension-uniform; the finite replay is an independent formula
audit, not an extrapolation.  Both replays were run on the remote CPU host.
