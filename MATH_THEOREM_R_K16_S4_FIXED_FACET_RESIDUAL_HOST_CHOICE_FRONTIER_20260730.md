# Frozen S4 collar: fixed facets, exact residual host choice, and the compensator frontier

Date: 2026-07-30  
Lane: R  
Status: **the full frozen S4 collar is proved impossible by a fixed-body
deadline-capacity obstruction; the host-choice reductions, sharp cascade,
and empty five-rehost equality face are independently audited**

## 1. Scope and frozen input

Let `P=k15seed_4.word`, and form the length-12,873 three-window word

\[
 Q_0\;P[6:6436]\;Q_1\;
 (0x8000\vee P[7:6432])\;Q_2,
 \qquad (|Q_0|,|Q_1|,|Q_2|)=(4,9,5).
 \tag{1.1}
\]

The physical collar positions, in their order as eighteen logical cells, are

\[
V=\{0,1,2,3\}\cup\{6434,\ldots,6442\}
  \cup\{12868,\ldots,12872\}.
\tag{1.2}
\]

The frozen bundle is

```text
scratch/k16_triwindow_s4_495_lead_20260730/frozen_atlas/
```

with authoritative hashes

```text
k15seed_4.word
  57a8370c1df54e2f79eb3af269f57b3b9840546cbb6c4862d6cf2adbcd94b2ae
lead_score2.cells
  ddc6675f0e5a3946e215bfdd389732b5965829d643c83772fe8b4218150133ad
lead_score2.word
  598e31a5dbec81df3e2dc1a8447e4697109850e480ba41a2cb86013715c38760
model.map.json
  fc2c4f185e294b963c391af56379e4dfbfbf9655a2b7457aa798a7d854ff73f2
residual_witness_incidence.tsv
  5df821abdd06e74a7aa1f8206aa0bc483d55afb0afaaf8c7cd042fd52def8cd5
```

This is a literal OR-collar calibration instance.  It is **not** an
equality-valid repeat-free parent pair: seed 4 has a repeated retained
rank-seven `D^2` trace when used as the marked parent.  No positive or
negative result below is silently transferred to the twelve item-1997d-valid
ordered openings `X\in\{0,\ldots,5\}, Y\in\{1,5\}`; only the marked parent is
forced to be repeat-free.  The abstract host theorem transfers once the
complete atlas for such an opening is supplied.

## 2. The three named facets are fixed-body rows

### Theorem 2.1 (fixed-only facet witnesses)

The three masks

\[
0x4c71,\qquad 0x4879,\qquad 0x4c39
\tag{2.1}
\]

each have exactly one literal witness in the frozen S4 word.  These witnesses
are, respectively,

| target | inclusive positions | literal cells |
|---|---:|---|
| `0x4c71` | `2300..2302` | `0x4421,0x0010,0x0c61` |
| `0x4879` | `5581..5583` | `0x0808,0x0050,0x4021` |
| `0x4c39` | `6243..6245` | `0x4029,0x4c21,0x4810` |

Every displayed interval lies wholly in the fixed lower body and is disjoint
from `V`.  Consequently arbitrary substitutions at all eighteen collar cells
preserve all three masks.  They require no provider variable and must be
removed from the variable residual problem.

#### Proof

For a fixed target `T`, scan every start and accumulate interval ORs until
the OR first contains a bit outside `T`; later endpoints cannot return below
`T`, so this stopping rule is exhaustive.  Exactly the three rows in the
table survive, one for each target.  Direct OR evaluation gives the stated
targets and the position audit gives empty intersection with `V`.  This is a
literal-word statement, independent of any witness encoding.  ∎

## 3. Complete residual semantic atlas

The two frozen bodies cover exactly 65,466 of the 65,535 nonzero masks.  Let

\[
\mathcal R=\{T\ne0:T\text{ is not covered by a fixed body}\}.
\tag{3.1}
\]

Then

\[
|\mathcal R|=69.
\tag{3.2}
\]

A semantic host option for `T` is a triple

\[
h=(T,F_h,Q_h),
\tag{3.3}
\]

where `Q_h` is the nonempty set of collar cells in one literal interval and
`F_h` is the OR of the fixed cells in that interval.  It is potentially
valid precisely when

\[
F_h\subseteq T.
\tag{3.4}
\]

Literal intervals with the same `(T,F_h,Q_h)` are semantically identical.
Exhaustive monotone interval scanning, followed by this collapse, gives
exactly 5,867 options.  An independent reconstruction has zero omitted and
zero extra rows relative to the frozen map.  The incumbent collar realizes
77 semantic options and misses exactly

\[
S=0x31ce,qquad L=0x7bce,qquad S\subset L,qquad L\setminus S=0x4a00.
\tag{3.5}
\]

There are 79 options for `S` and 83 for `L`.

## 4. Exact integral maximal-core theorem

### Theorem 4.1 (one provider per target)

Choose one semantic option

\[
h_T=(T,F_T,Q_T)
\tag{4.1}
\]

for every `T` in some target family.  For every collar cell `p`, put

\[
K_p=\bigcap_{T:p\in Q_T}T,
\tag{4.2}
\]

where an empty intersection is the full mask `0xffff`.  The selected options
have simultaneous nonzero integral cell values if and only if

\[
K_p\ne0\quad\text{for every incident cell }p
\tag{4.3}
\]

and

\[
F_T\vee\bigvee_{p\in Q_T}K_p=T
\quad\text{for every selected target }T.
\tag{4.4}
\]

When these conditions hold, the maximal canonical realization is simply

\[
x_p=K_p.
\tag{4.5}
\]

#### Proof

In any realization, every cell used by the option for `T` is a submask of
`T`.  Hence the value at `p` is a submask of every incident target and thus
of `K_p`.  This proves nonzeroness (4.3) and shows that the right side of
(4.4) is an upper bound on the OR attainable by that row.  Since the row must
equal `T`, (4.4) is necessary.

Conversely, assign (4.5).  Definition (4.2) makes every assigned value a
submask of every target whose row uses it, (4.3) makes it a legal nonzero
letter, and (4.4) realizes every selected target literally.  No fractional
rounding or rankwise recombination occurs.  ∎

### Corollary 4.2 (same-support fixed-OR dominance)

For a fixed target and fixed `Q`, an option with fixed OR `F_2` dominates one
with `F_1` whenever `F_1\subseteq F_2`: both impose identical cell caps,
whereas

\[
T\setminus F_2\subseteq T\setminus F_1.
\tag{4.6}
\]

Deleting all dominated options is exact.  In this S4 atlas it leaves exactly
70 options per target, hence 4,830 rows.  No dominance between unequal `Q`
sets is asserted.

## 5. Fixed-support provenance form

Let `c_p` be the incumbent collar values and fix a set `U\subseteq V` of
cells allowed to change.  Fold the unchanged collar cells into the fixed OR:

\[
A_U(h)=Q_h\cap U,qquad
G_U(h)=F_h\vee\bigvee_{p\in Q_h\setminus U}c_p.
\tag{5.1}
\]

Discard the option if `G_U(h)` has a bit outside its target.  A protected
target is automatically safe if it has an incumbent-realized option disjoint
from `U`; let `D_U` be the other protected targets.  Choose the required hole
providers and one option for every member of `D_U`.  Theorem 4.1, with
`F_h,Q_h` replaced by `G_U(h),A_U(h)`, is necessary and sufficient for a
completion supported in `U`.  Targets omitted from the selected system keep
their disjoint incumbent witness.

For coordinate `b`, define the blocker set

\[
B_b=\bigcup_{h:b\notin T_h}A_U(h).
\tag{5.2}
\]

Then

\[
b\in K_p\iff p\notin B_b.
\tag{5.3}
\]

Thus the exact conditions are:

1. every active cell lies outside at least one blocker `B_b`; and
2. for every selected row `h` and every demanded bit
   `b\in T_h\setminus G_U(h)`,
   \[
   A_U(h)\not\subseteq B_b.
   \tag{5.4}
   \]

This is a sixteen-colour broadcast condition, not a capacity-one matching.
The one-option-per-target choice is the integral coupling.

Primitive exact failure leaves are:

- `CELL_ZERO`: one cell and a minimal selected-row family whose omitted-bit
  sets cover all sixteen coordinates;
- `DEMAND_COVER`: a selected root row, one demanded bit, and a minimal
  blocker family covering its active set;
- `UNHOSTED`: one unassigned target together with exhaustion of its complete
  current option list.

In a `4/9/5` window, a cell-zero certificate uses at most sixteen selected
rows; a demand certificate uses at most nine blocker rows plus its root.

## 6. Exact all-pair hole screen

### Theorem 6.1 (nested-mask pair compatibility)

Let `(F_S,Q_S)` and `(F_L,Q_L)` be legal options for the two holes in (3.5).
They are jointly feasible exactly when

\[
Q_L\setminus Q_S\ne\varnothing
\quad\text{or}\quad
0x4a00\subseteq F_L.
\tag{6.1}
\]

#### Proof

Every `Q_S` cell is capped by `S`.  A cell of `Q_L\setminus Q_S` is capped
only by `L` and its maximal core is `L`, so one such private cell supplies
all of `L`.  If no private cell exists, all variable contribution to the
large row is contained in `S`; consequently all bits of `L\setminus S` must
already lie in `F_L`.  In either case the small row receives a maximal `S`
core and is automatic.  ∎

The complete count is

\[
79\cdot83=6557\text{ raw pairs}
=5692\text{ compatible}+865\text{ incompatible}.
\tag{6.2}
\]

The old condition `Q_S\subseteq Q_L` retains only 774 compatible anchors.
It is a strict scoped subfamily.  No full-S4 verdict may be inferred from
those 774 anchors.  A complete computation must use all 5,692 pairs,
including nonnested positional intervals.

## 7. Sharp incumbent-displacement frontier

For a compatible hole pair `P`, call a covered residual target
**incumbent-displaced** if every incumbent-realized semantic option for that
target fails Theorem 4.1 after adjoining `P`.

### Theorem 7.1 (three compensators are necessary)

Every one of the 5,692 compatible pairs incumbent-displaces at least three
of the other 67 residual targets.  Exactly nine pairs attain three.  They are

\[
\{36,68,69\}\times\{2,3,133\},
\tag{7.1}
\]

where the first factor lists the `S` shape and the second the `L` shape:

| target | shape | fixed OR | physical cells |
|---|---:|---:|---|
| `S` | 36 | `0x0000` | `6437,6438,6439` |
| `S` | 68 | `0x0000` | `12871,12872` |
| `S` | 69 | `0x0000` | `12872` |
| `L` | 2 | `0x0000` | `0,1,2` |
| `L` | 3 | `0x0000` | `0,1,2,3` |
| `L` | 133 | `0x6308` | `0,1,2,3` |

For shape 36 the displaced target set is

\[
\{0x73cc,0xb0cc,0xb0ce\};
\tag{7.2}
\]

for shape 68 or 69 it is

\[
\{0x3cc8,0x3ce8,0x73cc\}.
\tag{7.3}
\]

The complete displacement histogram is bound into the independent audit
artifact.  This count is not the number of complement runs and not the
number of changed physical cells.

### Proposition 7.2 (no five-row Hall obstruction)

For each of the nine attaining pairs, every displaced target has at least 44
individually compatible alternatives, and one can select an alternative for
each of the three displaced targets so that the resulting five rows pass
Theorem 4.1 jointly.  Thus the exact next obstruction, if present, is a
compensator cascade involving the remaining 64 protected rows.  There is no
singleton empty domain and no obstruction on the five selected rows alone.

### Theorem 7.3 (sharp pairs force a five-rehost cascade)

For each of the nine raw pairs in (7.1), every completion must additionally
abandon incumbent provenance for at least two further protected targets.  If
exactly two further targets are rehosted, their set is uniquely

\[
A=0x31cc,
\qquad B=0x33cc.
\tag{7.4}
\]

Consequently no sharp-pair completion uses only the three initially
displaced protected rows.  Its protected-row rehost count is at least

\[
3+2=5.
\tag{7.5}
\]

#### Proof

Fix a sharp pair.  Remove its three initially displaced targets from the
selected system altogether.  This is the strongest possible relaxation:
any actual replacement option can only intersect cell cores further.

For a demanded bit `b` of the selected large-hole row and a cell `p` of its
support, let

\[
\mathcal B_{b,p}
 =\{T:\text{the selected incumbent }Q_T\text{ contains }p, b\notin T\}.
\tag{7.6}
\]

Bit `b` can survive at `p` only if every target in
`\mathcal B_{b,p}` is rehosted.  Thus, after fixing one incumbent-realized
`Q_T` for every protected target, the minimum additional relaxation needed
by the large row is exactly

\[
\min_{p_b\in Q_L}
 \left|\bigcup_{b\in L\setminus F_L}\mathcal B_{b,p_b}\right|.
\tag{7.7}
\]

Same-`Q` dominance leaves six protected targets with multiple incumbent
supports, with multiplicities

\[
2,3,3,3,2,2;
\tag{7.8}
\]

hence exactly 216 incumbent-`Q` assignments per raw sharp pair.  Exhausting
the `9\cdot216` rows in (7.7) gives minimum two and the same unique minimizer

\[
\{A,B\}=\{0x31cc,0x33cc\}
\tag{7.9}
\]

in every case.  This proves a lower bound of two and identifies the unique
equality case; it does **not** say that every larger relaxation set contains
`A` and `B`.  An independent maximal-core implementation makes the
stronger equality-face relaxation explicit.  When every other
non-displaced row is retained, keeping either `A` or `B` makes all of the
incumbent-`Q` choices fail to supply the large row (216 choices when `B` is
retained and 72 when it is omitted): its always-missing bits are `0x4802`
when `F_L=0`, and `0x0802` when `F_L=0x6308`.  When both are omitted, all 72
remaining relaxed choices restore the large row, so the equality-two
assertion in (7.4) is sharp at this
relaxation.  Adding actual rows for any omitted target cannot add a bit to a
maximal core.  This proves (7.4)--(7.5).  ∎

### Search consequence

`THREE_COMPENSATOR` is therefore solver-free UNSAT and must not consume a
remote search slot.  On the exact rehost-count-five face, a sharp reduced
root may force `0x31cc,0x33cc` to nonincumbent options.  In an unbounded full
search this would be unsound: a larger blocker relaxation may avoid one or
both, so their incumbent domains must remain and only the branch order may
prefer the equality pair.  Theorem 7.3 says nothing about nonsharp pairs.

### Corollary 7.4 (the exact five-rehost equality fibre is empty)

Fix a sharp pair and permit nonincumbent options only for its three initially
displaced targets and the equality pair `0x31cc,0x33cc`.  Restrict every
other protected target to an incumbent-realized `Q` class.  This system has
no completion.  Consequently a completion through a sharp pair, if the
fixed-ghost obstruction were ignored, would require at least six protected
rehosts.

#### Proof

After the two hole rows and all incumbent-pinned rows are selected, retain
only base states satisfying every maximal-core equation.  There are exactly
24 valid incumbent bases for small shape 36 and 36 for each of small shapes
68 and 69; the count is independent of the large shape in
`{2,3,133}`.  For each base and each of the five relaxed targets, exhaust its
complete semantic option domain and test it together with every pinned row.

For small shape 36, all 24 bases leave the four targets

\[
\{0x33cc,0x73cc,0xb0cc,0xb0ce\}
\tag{7.10}
\]

individually unhostable.  For small shape 68 or 69, all 36 bases leave all
five relaxed targets

\[
\{0x31cc,0x33cc,0x3cc8,0x3ce8,0x73cc\}
\tag{7.11}
\]

individually unhostable.  A simultaneous completion would in particular
give every relaxed target one individually compatible option, so none
exists.  An independent implementation recomputes the maximal cores from
the raw 5,867-row incidence table and matches the `24/36` base counts and
both dead-row histograms.  ∎

For minimum-rehost search ordering, the 33 raw displacement-four pairs and
the 77 raw displacement-five pairs now precede the sharp pairs.  This is an
ordering rule, not a pruning rule in the unbounded full CSP.

## 8. Three-window partition and its limitation

Every proper residual host uses collar cells from exactly one of the three
windows.  For window `w`, let `I_w` be the hereditary family of target sets
which admit local options satisfying Theorem 4.1 on that window.  Then the
full residual problem is feasible exactly when

\[
\mathcal R=R_0\sqcup R_1\sqcup R_2,
\qquad R_w\in I_w.
\tag{8.1}
\]

Local realizations concatenate because their cell sets are disjoint;
conversely, partition the chosen hosts of any global realization by their
window.  This gives an exact set-partition formulation.

The systems `I_w` are not automatically matroids.  With two cells `p,q`, let
`X={a,b}` have fixed OR empty and singleton options on either cell, let
`Y={a,c}` use both cells
with fixed OR `{a}`, and let `Z={b,c}` use both with fixed OR `{b}`.  Then
`{X}` and `{Y,Z}` are feasible, while neither `{X,Y}` nor `{X,Z}` is.
Therefore ordinary matroid-partition Hall inequalities do not solve (8.1)
without an additional exchange theorem.

## 9. The full S4 fibre is empty: a deficiency-one deadline certificate

The preceding host-choice system can be closed without a finite search.  The
obstruction is not one of the 69 residual masks; it is a forced repeated
middle delivery already present in the fixed marked body.

The argument specializes the marked-parent exclusion already proved in
handoff item 2002a and uses the architecture-free ghost-free deadline theorem
of item 1997d.  The literal positions and arithmetic are independently
replayed below; the deadline inequality itself is an imported proved lemma,
not reproved from first principles here.

### Theorem 9.1 (fixed-ghost S4 no-go)

For arbitrary nonzero collar values in all three windows, the word (1.1) is
not universal.

#### Proof

The marked seed `P=k15seed_4.word` has the repeated rank-seven three-cell OR

\[
R=15554=0x3cc2
\tag{9.1}
\]

at parent starts 45 and 1145.  The two literal triples are

\[
\begin{aligned}
P[45..47]&=(0x0c82,0x1800,0x30c2),\\
P[1145..1147]&=(0x2482,0x3042,0x0800).
\end{aligned}
\tag{9.2}
\]

Their cumulative old-coordinate OR ranks are, respectively,

\[
(4,5,7)\quad\text{and}\quad(4,6,7).
\tag{9.3}
\]

Hence 47 and 1147 are their distinct earliest rank-seven deadlines.  The
marked fixed body in (1.1) begins at physical position 6443 and maps parent
position `j` to `j+6436`.  Therefore the child word has two fixed intervals

\[
[6481,6483],\qquad[7581,7583]
\tag{9.4}
\]

whose cumulative child ranks are `(5,6,8)` and `(5,7,8)` and whose common
first-middle target is

\[
M=0x8000\vee R=0xbcc2.
\tag{9.5}
\]

Both intervals lie wholly in the marked fixed body.  Thus arbitrary values
at all eighteen collar positions preserve the two first-middle deliveries,
and their distinct deadlines force at least one ghost extra:

\[
G\ge1.
\tag{9.6}
\]

For `K=16`, put

\[
W=\binom{16}{8}=12870,
\qquad n=W+3=12873,
\qquad
\Lambda=\sum_{s=1}^{7}\binom{16}{s}=26332.
\tag{9.7}
\]

The architecture-free first-delivery deadline theorem gives every universal
length-`W+3` word

\[
\Lambda\le(3-G)(n+G).
\tag{9.8}
\]

At `G\ge1`, the right side is at most

\[
2(12874)=25748<26332,
\tag{9.9}
\]

a contradiction.  ∎

### Corollary 9.2 (complete host-choice frontier is empty)

There is no selection of one semantic option for each of the 69 residual
targets satisfying Theorem 4.1.

#### Proof

Such a selection would assign the integral maximal cores (4.5), literally
realize every target not covered by a fixed body, and retain every fixed-body
target.  It would therefore materialize a universal nonzero word of the form
(1.1), contradicting Theorem 9.1.  ∎

### Minimal exact deficiency interpretation

This is not an ordinary target-option Hall cut within the 69 residual rows:
`0xbcc2` is already fixed-covered and hence absent from that list.  The
smallest honest augmented certificate has one middle-target vertex
`0xbcc2`, two forced deadline-group tokens `{6483,7583}`, and capacity one
under `G=0`.  Its deficiency is exactly

\[
2-1=1.
\tag{9.10}
\]

Thus the full fibre is rigorously closed, while a residual-only branching
proof remains useful only as an independent explanation of how the
compensator cascade manifests the same impossibility.

## 10. Proof-producing MRV frontier

The exact search state stores:

- the set of assigned targets;
- for each of the eighteen cells, the current maximal core `K_p`;
- for each coordinate `b`, the inclusion-minimal antichain of contiguous
  `Q` sets belonging to selected rows which demand `b`.

Adding an option intersects `K_p` with its target on every `p\in Q`, inserts
`Q` into each demanded coordinate's antichain (discarding redundant
supersets), and rejects immediately if a core is zero or a demanded `Q` is
disjoint from the current support of its coordinate.  This is the transposed
blocker form of (4.3)--(4.4), not a relaxation.
For every unassigned target the solver recomputes the exact surviving option
domain, prioritizes the two hole rows, and then branches on a minimum-domain
target (with safe ordering preferences on the sharp roots).  No cell-bit SAT
variables are present.

Two verdict scopes are deliberately distinct:

1. `THREE_COMPENSATOR`: only the nine anchors in (7.1) are used; the three
   displaced targets have their complete semantic domains, and each of the
   remaining 64 protected targets may use any `Q` class containing an
   incumbent-realized option, represented after exact dominance by that
   class's unique greatest fixed OR.
   This decides whether three rehosted rows suffice.
2. `FULL_5692`: every one of the 5,692 compatible raw hole pairs is retained,
   and all 67 protected targets have their complete semantic domains.  The
   exact same-`(T,Q)` fixed-OR dominance of Corollary 4.2 collapses these to
   4,300 compatible reduced roots, without deleting a possible completion.
   This is the only computational mode whose verdict independently decides
   the full frozen S4 residual CSP.

A time, memory, filesystem, or state cap returns `UNKNOWN`.  In particular,
neither an UNSAT result on the 774 nested anchors nor an UNSAT result in mode
1 is a full mode-2 verdict.

The nine raw minimum-displacement anchors of (7.1) similarly collapse to six
distinct reduced `Q` roots because the shape-133 fixed OR dominates shape 3
on the common four-cell support.  UNSAT for the dominating root also excludes
the dominated raw presentation.  SAT at the dominating root is a literal
completion for its own raw shape-133 presentation but does not imply SAT for
the dominated shape-3 presentation; one SAT is nevertheless enough for the
existential portfolio.  An implementation must state whether it runs six
reduced roots or all nine raw presentations.

Mode 1 is retained only as a proof-replay calibration.  Theorem 7.3 already
proves it UNSAT, so it is not launched merely to duplicate that deduction.

A separate exact `(U,R)` implementation launched 63 disjoint shards over all
5,692 raw roots.  Once Theorem 9.1 was recognized as a solver-free closure,
all 63 workers were terminated deliberately with exit 143 and no SAT/UNSAT
result.  Those partial logs are `UNKNOWN` and are not used anywhere in this
proof.

The frozen computational implementation is retained for independent replay:

```text
scratch/search_k16_s4_residual_provider_ur_exact_20260730.cpp
  240c41086dcd210699713a4d4959464bf177a1e749ba7e21682e9c8958fe6d0b
scratch/search_k16_s4_residual_provider_caps_exact_20260730.cpp
  05adb9e9de600bf1e6c7627bcabdbdaf0f50b95719073e9e6ed1ece104bd2191
scratch/run_l_k16_s4_provider_ur_63shards_20260730.sh
  5c4b3985ca6e628ee65c967e493e758daf2fece173958d95c8319b58796dc922
scratch/audit_k16_s4_residual_provider_ur_63shards_20260730.py
  9366a077df20ebf77c1e59a859b1b3b6be9bc3c7db8417f931d46705fe6bb12c
```

**Pending computational certificate insertion.**  Authenticated mode-1 or
mode-2 outcomes, resource bounds, proof-tree hashes, and independent replay
verdicts are inserted here only after the files exist and their input hashes
agree with Section 1.  Theorem 9.1 already supplies the unconditional full
fibre verdict, so a bounded mode-2 timeout remains `UNKNOWN` as a computation
and does not weaken that theorem.

## 11. Independent audit and precise boundary

The independent nonsearch audit is

```text
MATH_AUDIT_R_K16_S4_FROZEN_HOST_CHOICE_FRONTIER_20260730.md
  4e5cd804035434e64145418fa146c4ef7e5bbf694786e4d152badabc2200bd4a
scratch/audit_r_k16_s4_host_choice_frontier_independent_20260730.py
  ebf76071c15d5f09eb75262aba4830dcbc864b6b3f558276a4ccc3162d485931
scratch/k16_triwindow_s4_495_lead_20260730/frozen_atlas/
  host_choice_frontier.independent.audit.json
  f374631a9b4ccac3a543758a5d8ba060f1efb5a1fb40898d597b396e9ce5681c
scratch/audit_r_k16_s4_fixed_ghost_residual_closure_20260730.py
  18afac27c1231bf6b984e41e4e4f7bd5ab1b771e078ece9d938b6c60305f828a
scratch/k16_triwindow_s4_495_lead_20260730/frozen_atlas/
  fixed_ghost_residual_closure.independent.audit.json
  bd0a6de2f371ad179cea6253167839c23babe2cf59ccfb93c0622448834bb63d
MATH_AUDIT_K16_S4_SHARP_PAIR_FIVE_REHOST_FLOOR_20260730.md
  91f5778bfbb1f9e1303eaf08649fb613e2c98f8a18e46ba330f3328e2dd3c701
scratch/audit_k16_s4_sharp_pair_five_rehost_floor_20260730.py
  8fbfcd751b2ab4a1ebd1a1d75f4c7638bca173f67e9c6b746336603adfb6c6b0
scratch/k16_s4_sharp_pair_five_rehost_floor_20260730.audit.json
  85deda18dbd83f6be1662e75181152504c99a689952535ae24d3fe84f879255c
scratch/audit_r_k16_s4_sharp_pair_cascade5_20260730.py
  b287239e7bc0ea1a2cf30e3fcd2a0cb7f8d7e86b7dae20dfdf5b0832b6046b0f
scratch/k16_triwindow_s4_495_lead_20260730/frozen_atlas/
  sharp_pair_cascade5.independent.audit.json
  8af65cb32507c9be15065debdd860865fd825d3e07d8cdc240aee1eb7587681c
```

The host-choice audits independently prove the fixed-only facets, the
69-row/5,867-option atlas, the 5,692 pair count, the sharp minimum-three
displacement theorem, the positive immediate five-row cores, the lower
cascade to five rehosts, and emptiness of the exact five-rehost equality
fibre.  The fixed-ghost audit independently authenticates the two literal
deliveries and the numerical contradiction, while importing the proved
deadline inequality from item 1997d.

The present proved boundary is therefore:

- the named facets impose no collar variables;
- ordinary one-row Hall and each immediate holes-plus-three provider core
  pass;
- every repair attempt needs at least three nonincumbent protected rows, but
  each of the nine sharp pairs actually needs at least six because its unique
  five-rehost equality face is empty;
- the complete residual frontier is empty by the separate deficiency-one
  fixed-deadline obstruction of Theorem 9.1, using item 1997d;
- seed 4 is not an equality-valid marked parent, so even a collar calibration
  result must not be promoted to the global `K=16` bracket without a literal
  valid-parent construction.
