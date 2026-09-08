# Hall 23: component-root diamond refinement and the repeatable descent gate

Date: 2026-07-28

Status: exact `H24 -> H24 -> H23` component discharge; exact local
one-common-word lift on the discharged component; proved reusable
native-root split lemma; exhaustive one-braid H23 audit.  This historical
note itself constructs no H22 carrier.  The later authoritative
`H23 -> H23 -> H22` router/splitter and cumulative common-controller theorem
are in `THREAD_D_H22_NEUTRAL_ROUTER_CIRCUIT_SPLITTER_THEOREM_20260728.md`.
No global coefficient-one word is constructed.

## 0. Outcome

The authoritative projected Hall frontier is now 23.  Starting from the
canonical Hall-24 carrier, the two braids

\[
 H24\xrightarrow{\operatorname{FF}(212,3732,4717)}H24^{\rm portal}
 \xrightarrow{\operatorname{FF}(210,1501,4867)}H23                 \tag{0.1}
\]

preserve the exact middle deck, Johnson chronology, depth-three residence,
every upper support layer, and four immediate-lower holes.  The pair removes
the entire `161/160` Dulmage--Mendelsohn component rooted at mask `20516` and
adds no replacement DM target.

The mechanism is more precise than a scalar Hall improvement.

1. The neutral braid regroups two boundary shores of the rooted component
   without changing its matching rank.
2. The second braid refines a punctured Boolean diamond.  Relative to the
   common component core, the old boundary contributes rank four and the new
   boundary contributes rank five.
3. The component is saturated with one unused component-neighbour cell.  That
   unique exportable spare has native trace `21543` and is used by the exterior
   matching, giving the global rank gain.
4. The final component cells have native traces equal to every component
   target except the root, with one duplicate trace `20517`.  Repinning one
   duplicate cell from `20517` to `20516` realizes all 161 component targets
   in one physical word while preserving every central four-window.

This proves a reusable theorem: a unit DM component is discharged when a
legal braid creates a duplicate child of its root, one copy is safely
deletable to the root, and the component saturation is compatible with an
exterior matching.  Every remaining H23 component already has the required
native atlas; the missing datum is a physical neutral-plus-refining braid and
an exportable spare.

There is no unconditional copy-by-relabel theorem.  The remaining large
components are not physical-incidence copies of the `20516` component, and
the improving braid itself is illegal before the neutral preconditioner.  An
exhaustive H23 scan of all `9,143` resident/all-upper-safe one-braid moves
finds best score `(Hall,zeros)=(23,7)`: no adjacent H22 and no adjacent
zero-six state.

Finally, “lower holes four” in (0.1) means the immediate lower row only.  The
full lower-hole vector changes from

\[
                  (4,19,4,1,0,0,0)\quad\hbox{to}\quad
                  (4,19,6,1,0,0,0),                         \tag{0.2}
\]

losing depth-three targets `17445` and `28677`.  Any coefficient-one
iteration must repair or deliberately route those losses.

## 1. Exact carriers and finite audit

The three canonical paths and their SHA-256 digests are

| state | file | SHA-256 |
|---|---|---|
| H24 | `scratch/k15_segment_braid_hall24.json` | `49eb1060ccbe86f056295f0b96fe409f275737b8b759f5b7ca0ee2fa7ca0416e` |
| portal | `scratch/k15_segment_braid_hall24_portal.json` | `3bc6aa08d3df1b45709cef7e66ccc8bd9f9384a2b247c624252d81a637a032d4` |
| H23 | `scratch/k15_segment_braid_hall23.json` | `8feab1da65f3924d29609246798fc543dc50d076ca9db363e8796dda2c22598d` |

Exact reconstruction gives

\[
                 D(H24),D(H24^{\rm portal}),D(H23)=24,24,23. \tag{1.1}
\]

At all three states:

* all `6435` rank-eight masks occur exactly once;
* every adjacent pair is a Johnson edge;
* depth-three residence has no violation and maximal erosion reconstructs
  the middle chronology;
* all upper depths `q=1,...,7` have zero holes;
* immediate-lower holes equal four;
* the same seven targets have degree zero:

  \[
  2575,5801,13616,13620,17738,21641,29776.          \tag{1.2}
  \]

The unmatched-rank profile changes from `(rank 6,rank 7)=(5,19)` to
`(5,18)`.  The full lower vectors are the two vectors in (0.2).

For the two individual transitions, full-profile contraction gives

\[
                 8\longrightarrow8,qquad19\longrightarrow20 \tag{1.3}
\]

for the contracted boundary ranks.  Direct H24-to-H23 cancellation gives a
common profile multigraph of right-cell multiplicity `19282`, residual banks
of `29` cells on each side, common rank `16336`, and contracted ranks

\[
                             23\longrightarrow24.               \tag{1.4}
\]

The canonical-shore cross-gap matrix is

\[
 \begin{pmatrix}
 24&24&23\\
 24&24&23\\
 22&22&23
 \end{pmatrix}.                                                   \tag{1.5}
\]

## 2. The unit-component decomposition

The H24 canonical DM shore has `1168` targets and `1144` cells.  It is the
disjoint union of 24 connected incidence components, each with target excess
one.  The component `C` containing target

\[
                              R=20516                              \tag{2.1}
\]

has

\[
 |C|=161,qquad |N(C)|=160,qquad
 (n_4,n_5,n_6,n_7)=(1,9,43,108),                  \tag{2.2}
\]

and

\[
                         \bigcap_{S\in C}S=R.                      \tag{2.3}
\]

The portal state has the identical canonical shore and the identical rooted
component.  In H23 the canonical shore is `1007/984` and is exactly the old
shore with all 161 targets of `C` removed.  No target is added, and every
other old component keeps its neighbourhood size and matching rank.

The remaining H23 components are:

| roots | type |
|---|---:|
| `1920` | `169/168` |
| `960,8217,24610` | `161/160` |
| `449,8218` | `160/159` |
| `4213,7504` | `5/4` |
| `1103,18970` | `3/2` |
| `2420,2676,4877,9524,17683,19568` | `2/1` |
| `2575,5801,13616,13620,17738,21641,29776` | `1/0` |

Thus Hall 23 is not a diffuse deficit: it is exactly 23 rooted unit deficits.

## 3. Exact Boolean-diamond ledger

Write `+` for disjoint union of coordinate masks, and set

\[
 a=1,qquad b=2^{10},qquad c=2^{13},qquad
 d=2^{11},qquad e=2^3.                           \tag{3.1}
\]

All masks below contain the root `R`.  Restrict complete cell profiles to the
target component `C`.

The neutral braid replaces the two shores

\[
\begin{aligned}
O_1={}&\{R,R+a,R+a+b,R+c,R+a+c,R+b+c,R+a+b+c\},\\
O_2={}&\{R+d,R+a+d,R+d+c,R+a+d+c\}
\end{aligned}                                                       \tag{3.2}
\]

by

\[
\begin{aligned}
P_1={}&\{R+a+b,R+b+c,R+a+b+c\},\\
P_2={}&\{R,R+a,R+d,R+a+d,R+c,R+a+c,R+d+c,R+a+d+c\}.
\end{aligned}                                                       \tag{3.3}
\]

The component common core has rank 158, and both old and new boundary pairs
add rank two.  This is the exact neutral preconditioning.

At the second braid, after restricted-profile cancellation, the three old
shores are

\[
\begin{aligned}
Q_1&=\{R,R+a,R+c,R+a+c\},\\
Q_2&=\{R+a+b,R+b+c,R+a+b+c\},\\
Q_3&=\{R+e,R+a+e,R+e+c,R+a+e+c\},
\end{aligned}                                                       \tag{3.4}
\]

and the five new shores are

\[
\begin{aligned}
Q'_1&=\{R,R+a\},&Q'_2&=\{R+a+b\},\\
Q'_3&=\{R+c,R+a+c\},&Q'_4&=\{R+b+c,R+a+b+c\},\\
Q'_5&=\{R+e+c,R+a+e+c\}.                         
\end{aligned}                                                       \tag{3.5}
\]

Thus the punctured cube

\[
 \{R+x:x\subseteq\{a,b,c\}\}\setminus\{R+b\}                  \tag{3.6}
\]

is refined into its four `(b,c)` fibres, with the unavailable `R+b` vertex
removed.  This is the component-root Boolean-diamond refinement.

Using complete, not merely component-projected, cell profiles, the component
common core has rank 156.  The four old boundary columns add rank four.  The
six new boundary columns have contracted matroid

\[
                         U_{2,3}\oplus3U_{1,1},                    \tag{3.7}
\]

and hence add rank five.  The unique three-column circuit uses physical cells

\[
                         3579,\quad10016,\quad17744.             \tag{3.8}
\]

Their component shores are respectively

\[
 \{R,R+a\},qquad \{R+a+b\},qquad \{R,R+a,R+a+b\}.               \tag{3.9}
\]

The other three new columns are independent singleton summands in the
contraction.  Therefore

\[
                         156+4=160,qquad156+5=161.                \tag{3.10}
\]

The final component has 162 neighbouring cells and matching rank 161.  It
can be saturated without cell `17744`; this cell is the unique member of the
circuit whose native trace lies outside the component, namely `21543`.
Returning it to the exterior raises the exterior rank from `16198` to
`16199`.  The two disjoint matchings have total size

\[
                            161+16199=16360,                        \tag{3.11}
\]

which is the H23 global matching.

## 4. Unit-DM-component discharge theorem

The preceding calculation has a reusable graph-theoretic form.

### Theorem 4.1 (component discharge with exterior export)

Let `G` be a bipartite target/cell graph with matching size `nu`, and let
`C` be a connected component of a canonical DM shore satisfying

\[
                             |C|-|N_G(C)|=1.                       \tag{4.1}
\]

Let a legal chronology trade produce `G'`.  Suppose there are disjoint cell
sets `D_C,D_E` such that:

1. `G'[C,D_C]` has a matching saturating all of `C`;
2. `G'[L\setminus C,D_E]` has a matching of size
   `nu-(|C|-1)`; and
3. the union of these two matchings is cell-disjoint.

Then

\[
                              \nu(G')\ge\nu(G)+1.                  \tag{4.2}
\]

If in addition `A\setminus C`, where `A` is the old canonical shore, has
deficit exactly `D(G)-1` in `G'`, then equality holds in (4.2),
`D(G')=D(G)-1`, and no smaller scalar claim is being used.

#### Proof

The old contribution of `C` to a maximum matching is `|C|-1`.  Conditions
1--3 give a matching of size

\[
 |C|+\nu-(|C|-1)=\nu+1.
\]

The residual shore gives the matching upper bound `nu+1`, proving equality
and the deficiency assertion.  \(\square\)

### Corollary 4.2 (contracted boundary certificate)

Let `K` be the common component-profile multigraph after cancelling old and
new cells, and let `O,N` be the residual old and new banks.  If

\[
 r_C(K\sqcup O)=|C|-1,qquad r_C(K\sqcup N)=|C|,                   \tag{4.3}
\]

and a size-`|C|` component matching is compatible with the exterior matching,
then Theorem 4.1 applies.  A cell unused by the component matching but used by
the exterior is an **exportable spare**.

For (0.1), (4.3) is exactly (3.10), and `17744` is the exportable spare.

## 5. Native-root split and one common word

For a resident chronology `T` with maximal erosion controller `P`, define the
native trace of a physical cell `I` by

\[
                         \tau(I)=\bigcup_{p\in I}P_p.              \tag{5.1}
\]

### Theorem 5.1 (native-root split)

Let `C` be a unit DM component with root

\[
                              R=\bigcap_{S\in C}S.                 \tag{5.2}
\]

Assume there is a native cell atlas bijecting a selected cell set with
`C\setminus\{R\}`.  Suppose a legal chronology trade creates a second cell
whose native trace is one child `R+a`, so two selected cells have trace
`R+a`, and suppose one of those two cells `I_*` also admits target `R`.

Assign one copy natively to `R+a`, assign `I_*` to `R`, and keep every other
atlas cell native.  This is an injective target/cell assignment saturating
`C`.

Moreover, it is realized by one physical word if deleting `a` on `I_*`
satisfies all three exact conditions:

1. every central `(d+1)`-window still has union `T_i`;
2. every other selected pin interval retains its prescribed union; and
3. every changed physical letter remains nonempty.

#### Proof

The two copies of `R+a`, together with the native atlas, give one distinct
cell for every target of `C`.  Set `A=P` outside `I_*` and delete `a` from
the letters on `I_*`.  The three displayed hypotheses say respectively that
the middle row, all simultaneous target pins, and source nonzeroness survive.
The union on `I_*` is `R`, while every other selected interval retains its
old union.  Hence one word realizes the whole assignment.  \(\square\)

For a singleton `I_*={p}`, the common-word test becomes especially local:
every central window and every other positive pin interval containing `p`
must retain another occurrence of `a` whenever its label needs `a`.

### The concrete common-word certificate

At H23, the 161 component cells used for `C` have native trace types exactly

\[
                           C\setminus\{20516\},                   \tag{5.3}
\]

and only trace `20517=20516+1` is duplicated, at depth-zero cells `3579` and
`6261`.  Keep `3579 -> 20517`, repin

\[
                         6261:20517\longmapsto20516,              \tag{5.4}
\]

and retain all other native component pins.  Thus only one physical letter
changes:

\[
                         A_{6261}:20517\longmapsto20516.           \tag{5.5}
\]

All central four-windows reconstruct.  The only other selected interval
meeting position `6261` is the depth-one cell starting at `6260`, labelled
`22565`, and its union is unchanged.  Every letter is nonempty.  Hence all
161 component targets are realized simultaneously in one word.

Cell `17744` retains its native exterior trace `21543`.  The resulting 162
component-plus-export pins are distinct and simultaneously literal.  This is
stronger than an abstract Hall edge, but it is still a local component atlas,
not a target injection for all `16383` lower masks.

## 6. What repeats and what does not

The H23 canonical shore has a global native atlas: its `984` DM cells have
distinct native traces, and those traces are exactly all `1007` shore targets
except the 23 component roots listed in Section 2.  The maximal erosion word
realizes all 984 pins simultaneously.  Therefore every remaining unit
component already satisfies the atlas hypothesis of Theorem 5.1.

This does **not** make the physical refinement automatic.

1. The successful `20516` component is not coordinate-relabel equivalent to
   the remaining `161/160` components.  Its optional-coordinate degree
   multiset is

   \[
   [1,32,37,41,43,43,44,44,44,45,45],              \tag{6.1}
   \]

   whereas the remaining large target families have

   \[
   [0,32,37,40,44,44,44,44,44,45,45].              \tag{6.2}
   \]

   The remaining three `161/160` target families are mutually set-family
   isomorphic, but their native cell-shore incidences are not carried to the
   discharged component by those coordinate maps.  For example, the
   restricted right-degree counts include

   \[
   \begin{array}{c|ccc}
   \text{root}&\deg4&\deg5&\deg8\\ \hline
   20516&85&1&22\\
   960&81&0&24.
   \end{array}                                                       \tag{6.3}
   \]

2. The improving braid `FF(210,1501,4867)` is not a legal move on the
   unprepared H24 carrier.  It is non-Johnson, has six residence defects, and
   loses one upper-depth-one and two upper-depth-two targets.  The neutral
   braid in (0.1) is a genuine physical preconditioner, not a bookkeeping
   convenience.

3. Even after preconditioning, the improvement loses the two lower-depth-three
   targets in (0.2).  Iterating only the Hall rank ledger can therefore
   accumulate a forbidden cross-stratum debt.

The repeatable theorem is consequently conditional but useful:

> Find a resident/all-upper-safe neutral braid which creates a duplicate
> child of one remaining component root; then find a refining braid whose
> contracted component rank rises by one, with an exportable spare and a
> deletion-safe duplicate copy.  Theorems 4.1 and 5.1 then give both the Hall
> descent and the local common-word lift.

## 7. Exact H23 one-braid no-go

The complete implemented `FF/RF/FR/RR` catalogue was evaluated from the
canonical H23 carrier with no lower-hole cap.  The exact census is

\[
\begin{array}{c|r}
\text{Johnson move descriptions}&553356\\
\text{resident}&12001\\
\text{resident and all-upper-safe}&9143.
\end{array}                                                       \tag{7.1}
\]

Among all 9,143 evaluated candidates,

\[
                   \min D=23,qquad\min z=7.                     \tag{7.2}
\]

There are 7,114 descriptions of score `(23,7)`, but no score `(22,*)` and no
score `(*,6)`.  Hence H23 is a one-braid local minimum for both Hall
deficiency and the zero-target count in this exact catalogue.  Plateau moves
remain plentiful, so the result points to another neutral-plus-improving
pair; it is not a two-braid no-go.

The audit ran on the H100 CPU in approximately 143 seconds.  The source/input
hashes and full score distribution are frozen in
`scratch/threadD_h23_one_braid_scan_20260728.txt`.

## 8. Sharp H22 and zero-reduction targets

### H22 by another nonzero component

For a remaining rooted component `C_R`, it is enough to certify:

1. a legal neutral portal retaining the deck, residence, all upper supports,
   and every protected lower occurrence;
2. a final component contraction satisfying (4.3);
3. a component matching compatible with the exterior, preferably witnessed
   by an exportable spare;
4. a duplicate native child `R+a` with a copy deletable to `R` under Theorem
   5.1.

The small components are not excluded.  In fact their root deficit has the
same native-atlas form; their physical braid may be easier than the remaining
`161/160` components.  The one-braid no-go forces at least a plateau move,
an interacting simultaneous macro, or a move outside the four-type catalogue.

### Reducing the seven zero targets

A `1/0` component has no native child cell.  It must first acquire a cell and
then start a genuine global augmenting path.  The separate Pareto branch

\[
                    (25,7)\longrightarrow(26,6)\longrightarrow(25,6) \tag{8.1}
\]

creates a literal cell for target `2575`: depth two, start `5179`, native
trace `2607`.  Deleting coordinate `2^5` realizes `2575` in one common word.
But this merely exchanges unresolved target `2575` for native target `2607`;
it is a Robin--Hood swap and gains no matching rank.

Thus a true zero reduction needs the new zero-target cell to be the first edge
of an augmenting path whose other endpoint is a genuinely free/exported cell.
Equivalently, the displaced native target must be reabsorbed elsewhere rather
than becoming the new root deficit.  Combining the `2575` literal portal with
a component-root export such as `17744` is the exact next compound pattern;
no such combined chronology is presently certified.

## 9. Artifacts and proved boundary

The deterministic audits are:

* `scratch/audit_k15_h23_component_root_refinement.py`;
* `scratch/audit_k15_h23_component_root_common_q.py`;
* `scratch/k15_segment_braid_h23_component_refinement_audit_20260728.json`;
* `scratch/k15_h23_component_root_common_q_certificate.json`;
* `scratch/k15_hall23_native_dm_pins_certificate.json`;
* `scratch/threadD_h23_one_braid_scan_20260728.txt`.

They prove the exact H23 Hall score, removal of the whole rooted component,
the contracted rank gain, the local common-word component atlas, and the
one-braid local minimum.  They do not prove a global all-target matching or a
common word realizing all lower masks.  The precise next theorem is one more
root-split/export package, with the depth-three lower debt included in the
same signed ledger.
