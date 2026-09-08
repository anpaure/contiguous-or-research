# Dynamic-cross component sockets at `k=16`

## A same-face edit-98 lower bound and the unique local q1 descent

Date: 2026-07-29  
Lane: H  
Status: **proved finite transition theorems; the resident repair is not yet constructed**

## 1. Verdict

Let `F_0` be the canonical q1-perfect top-bi-resident quotient Hamilton
factor in

```text
scratch/k16_qfactor_q1_topresident_hamilton_20260729.json
```

and let `F_1` be the dynamic-cross radius-147 round-0 factor stored in

```text
scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json.
```

The exact byte hashes are

```text
F_0  f76ab4e5c30c3269da87788c275777a3b40deea96f4fbf892cd5c6027280a7a5
F_1  d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8.
```

Independent literal replay proves that `F_1` has quotient degree two,
both q1 palettes `764/764`, top-one and top-zero run length at least four,
three quotient components, and five physical components of lengths

\[
705,\ 1890,\ 3425,\ 3425,\ 3425.
\]

It lies at deletion/insertion radius 147 from `F_0`.  Its old-coordinate
short runs give 147 exact motif orbits.  Their edge-intersection graph has
85 components, maximum component size 9, and

\[
 \nu(\mathcal M_1)=\tau(\mathcal M_1)=97.                 \tag{1.1}
\]

This note proves four new facts.

1. The exact component transition is a socket `b`-matching with two q1
   colour-cover systems and an old-packing-row restoration system.
2. Any next factor which remains at radius 147 from `F_0`, retains quotient
   degree two, and kills both the 226 old motifs and all 147 motifs of
   `F_1` must remove **at least 98** edges of `F_1`.  Equality 97 is
   impossible before q1, top residence, connectivity, or the compiler is
   imposed.
3. Among all 85 components, only two have a minimum-transversal closure
   supported entirely on their own deficient vertices which preserves both
   q1 palettes.  Only one of those stays on the original radius-147 face.
4. The phase-parallel replacement

   \[
                  14079\longmapsto 14077                 \tag{1.2}
   \]

   is a literal same-face q1-safe top-resident local descent.  It changes
   two motif orbits into one and reduces the physical short-run count from
   2205 to 2190.  It does **not** lower the packing/transversal value 97.

Thus componentwise routing is real, but independent component closure is
not the answer.  Seventy-eight components lack any local degree closure;
five more close degree locally but fail local q1 and therefore require
nonlocal palette service, cross-component socket routing, or extra
deletions.  The endpoint analysis in Section 4 in fact raises the next-edit
lower bound to 99.

## 2. Provenance correction

The top-level status of the `F_1` file is `UNKNOWN`, because its second
CEGAR round timed out.  Its stored edge set is the round-0 `OPTIMAL`
incumbent, not a resident CEGAR solution.  Moreover, its embedded payload
digest is invalid: the stored value is `45992a...`, whereas recomputation
after removing the digest field gives `493d76...`.  This is a producer bug
also present in the remote copy.

Accordingly, no theorem below trusts that embedded digest or the top-level
status.  The authority is the whole-file SHA above together with independent
literal replay.  By contrast, the clean motif min-max artifact

```text
scratch/k16_dynamic_cross_r147_round0_motif_minmax_20260729.audit.json
```

has whole-file SHA

```text
e08ea84e60f4abb35295a5f832b619a42e4213efe274e390c18d2d5f273dcb38
```

and a valid embedded digest

```text
10ceb9d055480a71fafc4b1a7b34b58cf9a613cc7875a9b3d96232199a9f8ad1.
```

## 3. Exact transition variables

Let `Gamma` be the loopless rotational Johnson quotient catalogue.  For a
lower or upper q1 colour `t`, let `P_t^-` and `P_t^+` denote its complete
provider sets in `Gamma`, and put

\[
 m_1^\pm(t)=|F_1\cap P_t^\pm|.
\]

Let `F_2` be another quotient factor and split its symmetric difference
from `F_1` as follows:

\[
 D=F_1\setminus F_2,                                  \tag{3.1}
\]

\[
 H=(F_2\setminus F_1)\cap F_0,                        \tag{3.2}
\]

\[
 C=(F_2\setminus F_1)\setminus F_0.                   \tag{3.3}
\]

Thus `H` restores canonical source edges currently absent from `F_1`,
whereas `C` consists of genuinely new off-source seams.  Write

\[
 D_0=F_0\setminus F_1.
\]

The new canonical-source deletion set is exactly

\[
 D_0'=(D_0\setminus H)\cup(D\cap F_0).                \tag{3.4}
\]

For a quotient vertex `v`, `deg_E(v)` counts incidences of edges in `E`.

### Theorem 3.1 (exact socket and palette equations)

The set

\[
 F_2=(F_1\setminus D)\cup H\cup C                     \tag{3.5}
\]

has quotient degree two, remains on the original radius-147 motif face,
kills every motif in the current family `M_1`, and has both q1 palettes if
and only if all the following conditions hold.

1. **Current-motif hits:**

   \[
             D\cap M\ne\varnothing\qquad(M\in\mathcal M_1). \tag{3.6}
   \]

2. **Old face:**

   \[
              |D_0'|=147,
   \qquad D_0'\cap S\ne\varnothing\quad(S\in\mathcal M_0), \tag{3.7}
   \]

   where `M_0` is the 226-motif family of `F_0`.

3. **Socket balance:**

   \[
       \deg_C(v)=\deg_D(v)-\deg_H(v)\ge0
       \qquad(v\in V(\Gamma)).                         \tag{3.8}
   \]

4. **Both q1 covers:** for every lower and upper colour `t`,

   \[
   m_1^\pm(t)-|D\cap P_t^\pm|
      +|H\cap P_t^\pm|+|C\cap P_t^\pm|\ge1.           \tag{3.9}
   \]

5. The domains are explicitly

   \[
   D\subseteq F_1,\qquad H\subseteq F_0\setminus F_1=D_0,
   \qquad C\subseteq E(\Gamma^\circ)\setminus(F_0\cup F_1), \tag{3.10}
   \]

   and these sets are pairwise disjoint as forced by their domains.

#### Proof

At a vertex `v`, deleting `D` lowers degree by `deg_D(v)` and adding
`H union C` raises it by `deg_H(v)+deg_C(v)`.  Since `F_1` has degree two,
the new degree is two exactly when (3.8) holds.  Formula (3.4) is the literal
source-deletion set, so (3.7) is exactly radius 147 plus destruction of all
old motifs.  Equation (3.6) says precisely that none of the presently
visible short-run certificates survives.  Finally, (3.9) is the literal
provider multiplicity in `F_2`.  These conditions are plainly necessary,
and substituting them in (3.5) proves sufficiency.  Degree two gives
`|F_2|=|F_0|=858`; hence deletion radius 147 in (3.7) also gives insertion
radius 147.  QED.

The theorem concerns the two fixed motif families.  Added seams may create
new residence motifs; those require the next literal CEGAR audit.

### Corollary 3.2 (component socket matching)

The fresh-motif hitting condition decomposes by intersection component.
Choose a transversal `T_K` in each fresh motif component `K`, and let

\[
                  D=E\cup\bigcup_K T_K,               \tag{3.11}
\]

where `E` is an extra-deletion set.  Before defining `H`, every old packed
row `Pi_i` with current missing edge `h_i` must satisfy

\[
 |D\cap(\Pi_i\setminus\{h_i\})|\in\{0,1\},\qquad
 h_i\in H\Longleftrightarrow
 |D\cap(\Pi_i\setminus\{h_i\})|=1.                    \tag{3.12}
\]

Any source deletion outside the packed union, or two new source deletions
in one row, is infeasible.  Once these coupled row conditions determine
`H`, the off-source additions `C` must be a loopless `b`-matching
with

\[
              b(v)=\deg_D(v)-\deg_H(v).                \tag{3.13}
\]

It must simultaneously cover every residual lower and upper q1 row in
(3.9).  This is the exact cross-component object.  Only raw fresh-motif
hitting decomposes.  Old packed-row validity already couples transversal
choices; endpoint sockets and q1 debts add the further couplings
(3.13) and (3.9).

## 4. The edit-98 lower bound

The key obstruction is one two-motif component.  With zero-based IDs it is
component 71:

\[
 M_{112}=\{8058,8081,8778,14575\},                    \tag{4.1}
\]

\[
 M_{113}=\{8058,8081,20096,20100\}.                   \tag{4.2}
\]

Its only minimum transversals are

\[
                         \{8058\},\quad\{8081\}.       \tag{4.3}
\]

In the certified 147-row packing of the old factor, row 65 is

\[
        \Pi_{65}=\{8058,8081,8969,14575\}.             \tag{4.4}
\]

The current missing edge of this row is 8969.  The relevant quotient
endpoints are

\[
 8058=(169,374),\qquad8081=(169,550),\qquad8969=(191,373). \tag{4.5}
\]

### Theorem 4.1 (strict next-edit lower bound)

Let `F_2` have quotient degree two, lie at radius 147 from `F_0`, and kill
all 226 motifs of `F_0` and all 147 motifs of `F_1`.  Then

\[
                    |F_1\setminus F_2|\ge98.           \tag{4.6}
\]

This conclusion does not use q1, top residence, connectivity, voltage,
deeper shadows, or the compiler.

#### Proof

Suppose instead that \( |F_1\setminus F_2|=97 \).  The 97 pairwise edge-disjoint
fresh motifs force every deletion to be used by the fresh transversal.
Equality in (1.1), component by component, therefore makes `D` the union of
one minimum transversal from each of the 85 components.

Component 71 forces deletion of 8058 or 8081 by (4.3).  The 147 old packing
rows are pairwise edge-disjoint.  A radius-147 source deletion set killing
all of them has exactly one missing edge in every row.  Since 8969 is the
current missing edge of row 65, deleting 8058 or 8081 forces restoration of
8969.

Hence the added set has an incidence at each of quotient vertices 191 and
373.  Degree balance (3.8) requires `D` to have an incidence at each of
those vertices.  Exact enumeration of all 261 component-minimum options
shows that no minimum option in any component contains an edge incident
with 191 or 373.  This contradicts (3.8), proving (4.6).  QED.

This local obstruction raises the proved lower bound from 97 to 98; it does
not certify feasibility at 98.  The size-two
hit

\[
                         \{8778,20096\}                 \tag{4.7}
\]

kills both (4.1)--(4.2), consists of two current off-source seams, and has
socket set

\[
                         \{186,373,540,542\}.           \tag{4.8}
\]

The next theorem shows that even this escape cannot extend to a simultaneous
edit-98 completion.

### Theorem 4.2 (the 99th cut is forced at component 41)

In fact edit 98 is impossible.  Every factor satisfying the hypotheses of
Theorem 4.1 obeys

\[
                    |F_1\setminus F_2|\ge99.           \tag{4.9}
\]

The forcing endpoint is quotient vertex 589.

#### Proof

At edit 98 there is only one deletion beyond the fresh packing value 97.
First consider a minimum hit `8058` or `8081` in component 71.  Restoring
8969 requires deletion incidence at both 191 and 373.  No edge in any other
fresh component meets 191, no edge outside component 71 in the fresh union
meets 373, and no currently selected edge joins 191 to 373.  One extra edge
therefore cannot pay both endpoint debts.

It remains to spend the unique extra deletion inside component 71.  Exact
enumeration of its thirteen size-two transversals leaves six compatible
with the old packed rows.  Five still have signed socket `-1` at vertex
191, which no other component-minimum deletion can meet.  The sole locally
nonnegative option is

\[
                         \{8778,20096\}.                \tag{4.10}
\]

Thus (4.10) is forced and every other component must use a minimum
transversal.

Now component 41 consists of

\[
 M_{49}=\{17540,19329,20402\},                        \tag{4.11}
\]

\[
 M_{133}=\{17922,17955,19329,20402\}.                 \tag{4.12}
\]

Its minimum options are `19329` and `20402`.  Both lie in old packed row

\[
                  \Pi_8=\{19320,19329,20402\},         \tag{4.13}
\]

whose current missing edge is 19320.  Hence either minimum option forces
restoration of 19320.  The endpoints are

\[
 19320=(520,589),\quad19329=(520,548),\quad20402=(548,564). \tag{4.14}
\]

In either case the signed socket has value `-1` at vertex 589.  No edge in
the entire fresh motif union is incident with 589; the two current edges at
589 are 17470 and 18039, both outside that union.  Since the unique extra
deletion was already consumed by (4.10), the socket equation (3.8) fails at
589.  This proves (4.9).  QED.

The proof has the one-coordinate integer dual

\[
                         w_v=\mathbf 1_{v=589}.         \tag{4.15}
\]

The fixed component-71 escape has score zero; component 41 has maximum
score `-1` over both row-valid minimum options; every other component has
maximum score zero.  Their total maximum is therefore `-1`, contradicting
coordinatewise nonnegative socket balance.

### Corollary 4.3 (no independent component-41 plus one-extra repair)

After using (4.10), no one-extra component-41 surgery can preserve degree,
even before q1 and top residence are imposed.

Indeed, pairing a minimum option with a current edge at 589 leaves two
positive sockets which are not joined by an admissible off-source quotient
edge.  The only off-source companion is 18039; with deletion 19329 and
restoration 19320 the residual sockets are 486 and 548, and the catalogue
has no edge between them.  Deletion 20402 cannot cover both restoration
endpoints with one companion.  The two-edge transversal avoiding
`{19329,20402}` is either `{17540,17922}` or `{17540,17955}`.  The first
forces restoration 17938 and leaves a negative socket at 730; the second
has sockets `{474,484,520,564}`, among which there is no admissible
off-source perfect matching.  Thus any radius-99 attempt must route
component 41 through other components rather than close it independently.

## 5. Exact local-closure census

For a fresh component `K`, call `(T,A)` a **minimum local closure** when

1. `T` is a minimum transversal of the motifs of `K`;
2. `A` consists of unselected loopless catalogue edges whose endpoints are
   among the deficient vertices of `T`; and
3. `deg_A=deg_T` at every quotient vertex.

This is deliberately the strongest independent-component architecture: it
exports no endpoint debt.

### Theorem 5.1 (local closures are exceptional)

The 85 components have 261 minimum-transversal choices.  The histogram of
the number of choices per component is

\[
1^{11},\ 2^{16},\ 3^{31},\ 4^{21},\ 5^1,\ 6^2,\ 8^3. \tag{5.1}
\]

Exactly 260 of the 261 choices delete vertex-disjoint quotient edges.  Only
the following seven components have any minimum local degree closure:

\[
                    4,26,50,51,63,75,77.              \tag{5.2}
\]

Only components 63 and 75 have a local closure preserving both q1
palettes.  Only component 63 has one which also remains on the original
radius-147 face.

#### Proof

For each component, enumerate all subsets of its edge union of the stored
minimum size and retain exactly those hitting every motif.  At most four
edges are selected.  Their incidence vector has at most eight sockets.
Choose the first positive socket and recursively pair it by every unselected
loopless catalogue edge induced on the remaining sockets.  Decrement the
two endpoint demands and continue.  This enumerates every local
degree-balanced addition and nothing else.  Literal provider counts then
test both q1 palettes; source distance and all 226 source motifs test the
old face.  The resulting exact census is (5.1)--(5.2).  QED.

For component 75, the q1-safe parallel closures are

\[
 13230\mapsto13227,
 \qquad13230\mapsto13232,                              \tag{5.3}
\]

but both move from source radius 147 to radius 148.  They are not admissible
same-face primitives.

## 6. The unique same-face parallel descent

Component 63 has motif IDs 93 and 94 and edge union

\[
 \{2277,2281,13097,14063,14079\}.                     \tag{6.1}
\]

The edge 14079 hits both motifs.  Edges 14079 and 14077 are parallel in the
quotient catalogue and both lie outside `F_0`, so (1.2) exchanges one added
seam for another without changing the source deletion or insertion count.

### Theorem 6.1 (literal phase-parallel descent)

Put

\[
          F_1'=(F_1\setminus\{14079\})\cup\{14077\}.  \tag{6.2}
\]

Then:

1. `F_1'` has quotient degree two and remains at source radius 147;
2. all 226 source motifs remain hit;
3. both q1 supports remain `764/764`;
4. top-one and top-zero residence remain valid;
5. quotient/physical component counts remain `3/5`, with the same physical
   cycle lengths;
6. the fresh motif-orbit count drops from 147 to 146; and
7. physical short-run violations drop from 2205 to 2190.

The exact motif exchange is

\[
\begin{split}
 &\{2277,2281,14063,14079\},\\
 &\{2277,13097,14063,14079\}
\end{split}                                             \tag{6.3}
\]

removed and

\[
                  \{13094,13097,14063,14077\}          \tag{6.4}
\]

created.

#### Proof

Parallel quotient endpoints prove degree preservation.  Both exchanged
edges are off-source, proving preservation of source radius.  Direct set
intersection verifies every source motif.  Exact lower/upper provider
counts give `764/764`.  The literal 12,870-vertex lift verifies the two top
run systems, components, and run census.  Finally, reconstructing every
short-run edge motif before and after gives (6.3)--(6.4).  QED.

The new 146-motif family still has 85 components and

\[
                         \nu=\tau=97.                  \tag{6.5}
\]

Thus this is a strict motif-count and physical-run descent, but not a
packing-potential descent.

### Theorem 6.2 (small alternating-switch frontier)

Consider every one-edge parallel replacement and every ordinary
four-distinct-endpoint alternating two-switch whose removed set hits an
entire fresh motif component.  Impose the old radius-147 face, all old
motifs, both q1 palettes, and top bi-residence.  The exact census is

```text
distinct catalogue switches                         3247
old-face safe                                        184
both-q1 safe                                           6
top-bi-resident                                         3
strict motif-count descents                             1
strict physical-short-run descents                      1.
```

The unique strict descent is (1.2).  The other two top-safe switches are

```text
remove 15985,17540  add 15996,19600
remove 24374,26166  add 24380,25082.
```

Both are motif-count neutral; the second simultaneously services two fresh
components but increases physical component count to 17.

This theorem is exhaustive only for the displayed support-one/two move
class.  Adjacent-red-edge circuits, support at least three, and jointly
palette-compensated switch packets remain open.

## 7. Smallest remaining exact gate

By Theorem 4.2, the first possible same-face repair has

\[
                         |D|=99.                       \tag{7.1}
\]

The exact parameterization must quantify over every 99-edge set
\(D\subseteq F_1\) which hits all fresh motifs and satisfies the old packed-row
validity equations (3.12).  It is not enough to choose minimum transversals
plus two extra edges: an inclusion-minimal size-`tau_K+1` transversal need
not contain a minimum transversal.  Determine `H` from the valid old rows.
The remaining exact feasibility problem is:

> Find a loopless off-source set `C` with
> `deg_C=deg_D-deg_H`, satisfying both families of inequalities (3.9), all
> 79 nonpacked old-motif rows, and all fresh-motif rows.

This is a finite coloured socket `b`-matching.  A solution is still only a
carrier-core candidate: it must then pass the literal tests for newly
created positive and top-zero motifs, connectivity/voltage, deeper shadows,
and the compiler.  An infeasibility proof at edit 99 would raise the bound
again; a feasible carrier would supply the next exact CEGAR state.

## 8. Audited artifacts

```text
scratch/k16_dynamic_cross_r147_round0_motif_minmax_20260729.audit.json
SHA-256 e08ea84e60f4abb35295a5f832b619a42e4213efe274e390c18d2d5f273dcb38

scratch/k16_dynamic_r147_next_edit98_lower_bound_20260729.audit.json
SHA-256 5da2b672925a6be54a9b05c882622f55c5cfa6b3ecce7cf6c8b3ac793aa7c47e

scratch/k16_dynamic_r147_component_socket_closures_20260729.audit.json
SHA-256 cdca665b95075fecd7394f0c7ff01809adf44a25c8a21e5648e68c7147b1daff

scratch/k16_dynamic_r147_component_2switch_atlas_20260729.json
SHA-256 dca99e5af6b791bfb1fb98c208fd1df9eb765a6e72f78cfb4f3fb1cd3390125a

scratch/k16_dynamic_r147_component63_parallel_descent_20260729.audit.json
SHA-256 d9e92847809201afd07f0ace632fa3f5c536617282a1359944ec66a548d97b66

scratch/k16_dynamic_r147_component63_parallel_descent_minmax_20260729.audit.json
SHA-256 54e1c02e4edc8496c2f0e259463c70e5e4ffbb94df309a3f205b5d1edc633fc9
```

Audit scripts:

```text
scratch/audit_k16_dynamic_r147_edit98_lower_bound_20260729.py
SHA-256 6fcf7a29f0429235528b166c3b9cce3763ef32d09084857d1c57ab0f020c6292

scratch/audit_k16_dynamic_component_socket_closures_20260729.py
SHA-256 e33a6c2621a6e5891df05ff05e4737aac5294c4725628081e20d2f3d2cabadec

scratch/search_k16_dynamic_component_2switch_20260729.py
SHA-256 2e00b812231bf30dbd8f9fd23b156cbd32d202e7a8793cdd924c98b5282dd153

scratch/audit_k16_dynamic_component_parallel_descent_20260729.py
SHA-256 2a461ab4bf536562db3084ab2ff26502539de22519ca0743500fa83efeb6bda9
```

The two finite local audits ran in seconds and perform no SAT search.  The
two-switch enumeration ran on the H100 CPU.  No GPU was used.  None of these
artifacts claims a fully resident factor or a `k=16` word.
