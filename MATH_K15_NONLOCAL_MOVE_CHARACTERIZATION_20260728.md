# What a successful `k=15` move must do

Date: 2026-07-28

Status: rigorous structural synthesis, with finite-census statements scoped
exactly as indicated.  No `k=15` solution is claimed.  **Correction trail:**
an independent signal audit found an allocation-order bug in the first
`early0` channel, so its proof was quarantined.  A two-pass corrected channel
was then checked on every propagated mask and boundary bit, and a new DRAT
proof independently verifies the corrected scoped UNSAT stated below.

## 0. Conclusion

Four facts that initially look unrelated have one common interpretation.

1. In the canonical optimal compilers through `k=13`, every source letter is
   cut out of the maximal erosion by **one** lower owner.  At `k=14` this
   remains true except at exactly five positions, where two owners suffice.
2. On the canonical `k=15` Hall-29 carrier, degree-one peeling freezes 1,489
   owners and leaves a conditional kernel of 35 targets on six live cells.
3. In the fixed-endpoint five-parent root atlas, every cycle-free
   source-to-sink path completion for root 17738 through successor support 34
   fails depth-three residence; the other root motifs have path-closure
   support floors as large as 38.
4. The exact space between two successor factors is a Boolean cube on the
   cycles of their relative permutation, but Hamiltonicity, residence, and
   compiler Hall are not additive on those cycles.

The corrected native unrestricted-radius test gives a scoped no-go.  In the
five-parent directed union, no Hamilton chronology simultaneously preserves
the 1,489 H29-anchor-transported frozen owners and matches all 35 residual
targets within the retained transported defect-at-most-one atlas.  Residence
and upper-shadow constraints were omitted.  Hence a solution in this scope
must change an owner transport, use a deeper residual option, or leave the
arc union.

For the narrower **cycle-free source-to-sink path closure** enumerated by the
root kernel, support is at least 35 for root 17738 and at least 38 when all
seven audited root families are imposed.  A general modification can escape
those support bounds by adding disjoint alternating cycles; this is not a
minor caveat, but one of the compound mechanisms the conclusion points to.

The global difficulty is therefore in **joint chronology and owner
re-anchoring/rematching**, not merely collar coupling with the old anchored
skeleton.  The data still suggest that a final compiler may have local owner
dimension at most two, but its defining owners need not retain their H29
anchors.

The support bounds are finite statements about the named catalogue, motif
families, and cycle-free completion kernel.  They are not lower bounds for
arbitrary `k=15` carriers or even for every modification in the five-parent
union.

## 1. Owner meet dimension

Fix a middle row `T`, its maximal erosion `P=(P_p)`, and an injective lower
owner assignment

\[
 \phi:X\longmapsto J_X.
\]

At a position `p`, let

\[
 \mathcal O_p=\{X:p\in J_X\}.
\]

The maximal word associated with `phi` is

\[
 A_p=P_p\cap\bigcap_{X\in\mathcal O_p}X.                 \tag{1.1}
\]

This is just the negative-window formula written positionwise: a coordinate
of `P_p` survives exactly when no owner interval covering `p` omits it.

Define the **owner meet dimension**

\[
 \kappa_p(\phi)=\min\left\{|S|:
     S\subseteq\mathcal O_p,
     \ P_p\cap\bigcap_{X\in S}X=A_p\right\}.           \tag{1.2}
\]

### Lemma 1.1 (one-owner normal form)

`kappa_p<=1` if and only if either `A_p=P_p`, or the trace family

\[
 \{P_p\cap X:X\in\mathcal O_p\}
\]

has a least member, equal to `A_p`.

#### Proof

If one owner `X` defines `A_p`, then `P_p cap X=A_p`; because (1.1) is
contained in every owner trace, this trace is least.  Conversely a least
trace equals the intersection of all traces and therefore defines `A_p`.
The empty subfamily gives `A_p=P_p`.  `square`

Thus owner load and owner dimension are different quantities.  Many owner
intervals can cover a position while all but one are locally redundant.

### Finite Fact 1.2 (raw optimal compilers)

For the canonical negative-window fixed points extracted from the optimal
words:

\[
 \max_p\kappa_p\le1\quad(6\le k\le13).                 \tag{1.3}
\]

At `k=14`, exactly five positions have `kappa_p=2`; all other positions have
dimension at most one.  The complete histogram is

\[
        0^{1910}\,1^{1519}\,2^5.                       \tag{1.4}
\]

At each exceptional position the two displayed owner traces are
incomparable and their meet is the source letter.  These are the five records
in
`scratch/raw_optimal_k06_k14_compiler_normal_form_audit.json`.

The proof is literal evaluation of (1.2).  For each position the audit tries
subfamilies by cardinality and verifies equality in (1.2); no search
heuristic is used.

### Interpretation

The first departure from the one-owner model is not a proliferation of
constraints.  It is five binary meets among 3,434 source positions.  Hence
the evidence points toward a bounded-arity negative compiler even while the
chronology becomes globally difficult.

## 1A. Erosion envelopes are graded exactly

The one-owner geometry is tied to residence by an exact identity.  Let
`T_0,...,T_{W-1}` be the rank-`r` middle path and put

\[
 P_p=\bigcap_{i=\max(0,p-d)}^{\min(p,W-1)}T_i,
 \qquad0\le p<W+d.                                     \tag{1A.1}
\]

Assume every coordinate run in `T` has length at least `d+1`.

### Lemma 1A.1 (boundary-clipped erosion union)

For `1<=ell<=d+1` and `0<=j<=W+d-ell`,

\[
 \bigcup_{p=j}^{j+\ell-1}P_p
 =\bigcap_{i=a}^{b}T_i,                                 \tag{1A.2}
\]

where

\[
 a=\max(0,j+\ell-d-1),\qquad b=\min(j,W-1).            \tag{1A.3}
\]

#### Proof

Fix a coordinate `x` and one maximal run `[u,v]` of `x` in `T`.  By (1A.1),
this run contributes `x` to `P_p` exactly when

\[
 u\le\max(0,p-d)\quad\hbox{and}\quad
 \min(p,W-1)\le v.                                     \tag{1A.4}
\]

Taking the union over `p in [j,j+ell-1]`, the two inequalities in (1A.4)
have a common solution exactly when the run covers every middle index from
`a` through `b`.  This is membership in the right side of (1A.2).  Distinct
runs cannot jointly fake that condition: the interval `[a,b]` has length at
most `d+1`, while consecutive runs are separated by a zero.  Apply the
argument coordinatewise.  `square`

### Lemma 1A.2 (rank grading)

If `T` is a Johnson path, then

\[
 \left|\bigcup_{p=j}^{j+\ell-1}P_p\right|=r-(b-a).     \tag{1A.5}
\]

In particular, away from the boundary,

\[
 \left|\bigcup_{p=j}^{j+\ell-1}P_p\right|
       =r-(d-\ell+1).                                  \tag{1A.6}
\]

#### Proof

The interval `[a,b]` has `b-a` Johnson transitions.  Their deleted
coordinates are distinct: a repeated deletion would require a reinsertion
and a second deletion within at most `d` transitions, producing a run of
length at most `d`.  No coordinate inserted during `[a,b]` can be deleted
again there for the same reason.  Hence every transition removes one new
coordinate from the intersection in (1A.2), proving (1A.5).  The interior
formula substitutes `b-a=d-ell+1`.  `square`

Put `s=r-d` and let a short compiler cell have depth `h=ell-1`.  Its maximal
envelope therefore has interior rank

\[
                            s+h.                       \tag{1A.7}
\]

Three observed phenomena are now consequences rather than coincidences.

1. `ell=1` gives the flat rank-`s` erosion, with (1A.5) giving the exact
   boundary ramp.
2. A rank-`t` lower target cannot be owned before

\[
                         h\ge\max(0,t-s),              \tag{1A.8}
\]

   which is precisely the nominal owner row in the raw census.
3. At `k=15,r=8,d=3`, the top grades are rank seven/depth two, rank
   six/depth one, and rank five/depth zero.  These are exactly the three
   degree-one peeling rounds `1013,395,81`.

The identity explains the grading and peeling order.  It does not by itself
prove the observed degree-one counts or rule out the boundary and one-row
spill exceptions.

## 2. Why Hall alone is insufficient

For a fixed carrier, let `G` be the bipartite graph of locally eligible
target-cell pairs.  A complete matching of `G` need not be jointly
realizable, because an owner `X->J_X` removes every coordinate outside `X`
from every source position in `J_X`.

The exact `k=7` counterexample is

\[
 7\mapsto[1,2],\qquad1\mapsto[1],\qquad4\mapsto[2].    \tag{2.1}
\]

All three pairs are locally eligible and cell-distinct.  The latter two
owners both omit coordinate one and jointly erase it from positions one and
two, so the first interval realizes mask `5`, not mask `7`.

### Lemma 2.1 (global owner criterion)

An injective owner assignment `phi` is realizable with fixed middle row `T`
if and only if, with

\[
 Z_x=\{p:x\in P_p\}\setminus
       \bigcup_{X:\,x\notin X}J_X,                     \tag{2.2}
\]

the following hold:

\[
 J_X\cap Z_x\ne\varnothing\quad(x\in X),              \tag{2.3}
\]

\[
 [i,i+d]\cap Z_x\ne\varnothing\quad(x\in T_i),       \tag{2.4}
\]

and every source position lies in some `Z_x`.

This is the fixed-middle full-witness theorem.  It explains why a successful
carrier edit must solve two problems: create enough eligible cells *and*
choose owners whose negative windows are compatible.

## 3. The exact Hall-29 repair tax

Let `F` be the 1,489 forced owner pairs obtained by iterative degree-one
peeling of the canonical Hall-29 DM graph.  Delete their targets and reserved
cells.  The residual instance has

\[
 35\text{ targets},\qquad6\text{ live cells},qquad
 \operatorname{def}=29.                                \tag{3.1}
\]

Its twelve live edges are six collisions: each live cell is the unique live
choice of one rank-six and one rank-seven target.  The other 23 targets have
live degree zero.

This is a conditional kernel after reserving `F`, not a raw 35-target Hall
shore.

### Lemma 3.1 (29-fresh-cell tax)

Suppose a new carrier preserves all pairs in `F` and admits a matching of the
35 residual targets into unreserved cells.  Then at least 29 matched cells
lie outside the six old live cells.

#### Proof

A matching uses at most six of the six old live cells.  Its remaining
`35-6=29` edges have distinct cells outside that set.  `square`

Now restrict to the retained baseline-defect-at-most-one atlas.  It contains

\[
 12\text{ exact options},\quad3807\text{ missing-one options},\quad
 238\text{ mandatory-one options}.                     \tag{3.2}
\]

There are no per-position-meet defect-one options in this atlas.

### Corollary 3.2 (29 literal repairs)

Any successful carrier in the compact peeled architecture makes at least 29
previously false fixed-mask predicates true on distinct physical cells.
Each such predicate repairs exactly one of:

1. a missing coordinate in the cell envelope; or
2. an extra coordinate in the cell mandatory core.

This is a genuine parallel repair requirement.  Improving one scalar Hall
score by 29 is not enough unless the gains occur on distinct cells and admit
a transversal of all 35 residual targets.

### Native Result 3.3 (corrected anchor-transported no-go)

The corrected two-pass channel passes an independent audit of 32,178 mask
rows and 19,305 boundary bits with zero errors.  The unrestricted corrected
formula has 842,541 variables and 4,942,711 clauses and is UNSAT.  Its new
ASCII DRAT proof was independently verified by `drat-trim`; the backward
core uses 9,259 original clauses, 5,389 proof lemmas, and 23,408 resolution
steps.  The corrected CNF and DRAT hashes are respectively

```text
e688f2123df6e89cbb14a33d1d09811d6b33c7f0001b8036d51d5ff98440be03
7727fc221331c1a18192d1332551167fe093446e2af8993abf3209ad6a7369f6
```

The first buggy formula and proof are explicitly quarantined and have no
mathematical status.  Full provenance is in
`K15_NATIVE_CHRONOLOGY_OWNER_FORMULATION_20260728.md`.

### Corollary 3.4 (scoped three-way escape)

Within the corrected architecture, every successful `k=15` construction
must do at least one of the following:

1. change the H29 anchor transport of a frozen or residual owner;
2. use a residual option outside the retained baseline-defect-at-most-one
   atlas; or
3. use a directed middle arc outside the five-parent union.

This does not constrain ordinal-position ownership or any other transport
not encoded by the corrected formula.

## 4. Residence is an exact collar condition

Let `H=(V_0,...,V_{W-1})` be a Johnson path.  At a seam `V_i->V_{i+1}` write

\[
 x=V_{i+1}\setminus V_i,\qquad y=V_i\setminus V_{i+1}. \tag{4.1}
\]

### Lemma 4.1 (depth-`d` seam collar)

Assume the operation cuts an existing chronology into contiguous pieces and
rejoins two such pieces at this seam, without reordering either piece
internally.  Assume also that both inherited piece interiors already have
minimum coordinate-run length `d+1`.  Their concatenation has the same
property at the seam if and only if

\[
 x\in V_{i+1}\cap V_{i+2}\cap\cdots\cap V_{i+d+1},     \tag{4.2}
\]

and

\[
 y\in V_i\cap V_{i-1}\cap\cdots\cap V_{i-d}.          \tag{4.3}
\]

Terms beyond a linear endpoint are omitted.

#### Proof

The only new run beginning at the seam is the run of `x`; it must occupy at
least the `d+1` states in (4.2).  The only run ending at the seam is the run
of `y`; it must occupy at least the `d+1` states in (4.3).  Every other run is
internal to one inherited piece and is safe by hypothesis.  `square`

For `d=3`, every changed seam therefore carries a four-state forward and
four-state backward obligation.  This gives a precise meaning to
"residence repair": a new seam that exposes a short run must be accompanied
by another change inside its collar.

### Lemma 4.2 (disjoint-collar additivity)

Let a resident base path be cut into contiguous pieces and rejoined at several
seams, with every piece internally unchanged.  Define each closed depth-`d`
collar using predecessor and successor distance in the **resulting
chronology**.  If these collars are pairwise disjoint and each modified seam
is unsafe in its own collar, then their union is not resident.  More
precisely, the set of new residence violations is the disjoint union of the
violations in the individual collars.

#### Proof

Residence is determined by words `0 1^j 0`, `1<=j<=d`, hence by a bounded
collar.  Under the disjointness hypothesis, changing one seam cannot alter
the trace in another seam's collar.  The local violation predicates are
therefore unchanged and disjoint.  `square`

Consequently several individually nonresident switches can cancel their
defects only by **collar interaction**.  Their supports may be disjoint as
permutation cycles, but their chronological collars must overlap.

## 5. Exact hybrid cube

Close two Hamilton paths with the same dummy convention, obtaining successor
cycles `p,q` on `Omega`.  Put

\[
 \varphi=p^{-1}q.                                      \tag{5.1}
\]

Let `C_1,...,C_c` be the nontrivial cycles of `varphi`.  For
`S subseteq[c]`, let `varphi_S` act as `varphi` on cycles in `S` and as the
identity elsewhere, and put

\[
                         h_S=p\varphi_S.               \tag{5.2}
\]

### Theorem 5.1 (all pointwise hybrids)

The bijections `h` satisfying

\[
                     h(v)\in\{p(v),q(v)\}\quad(v\in\Omega) \tag{5.3}
\]

are exactly the `2^c` maps `h_S`.

#### Proof

Let `psi=p^{-1}h`.  Then `psi(v)` is either `v` or `varphi(v)`.  On one cycle
`(v_0,...,v_{ell-1})` of `varphi`, put `b_i=1` when
`psi(v_i)=varphi(v_i)=v_{i+1}` and `b_i=0` when `psi(v_i)=v_i` (indices
modulo `ell`).  The number of preimages of `v_i` is

\[
                         (1-b_i)+b_{i-1}.
\]

Bijectivity makes this number one, so `b_i=b_{i-1}` for every `i`.  Thus the
choice is uniform around the entire cycle.  Conversely either uniform choice
is a permutation on that cycle.  Multiply over the disjoint cycles.  `square`

This proves that the observed three-component/eight-hybrid space is forced,
not accidental.  It also explains why component switching is a natural
large neighborhood: degrees and middle ownership are automatic at every
corner of the cube.

What is *not* automatic is the one-cycle condition.  `h_S` is Hamiltonian
exactly when it has one successor cycle.  Nor are residence or compiler Hall
additive in `S`.  The exact Hall-30/Hall-37 three-component census gives
Hamilton deficiencies `30,31,33,33,34,35,36` and one disconnected corner,
already refuting a scalar additive component score.

### Corollary 5.2 (collar-coupled components are necessary)

Suppose every selected relative cycle, switched alone, has a residence
violation, and the depth-`d` collars of the selected cycles are disjoint in
the combined chronology.  Then the hybrid is nonresident.

Thus a resident compound hybrid made from individually unsafe cycles must
contain an interacting cluster in the residence-collar overlap graph.

## 6. The finite support barrier

The exact fixed-endpoint exchange enumerator starts from an audited interior
root motif and completes the displaced successor owners by vertex-disjoint
alternating exchange paths from the forced sources to the forced sinks.  It
enumerates every completion in this **cycle-free path-closure kernel** up to a
declared changed-tail support.  It does not enumerate the product with an
additional alternating cycle disjoint from those paths.

### Finite Fact 6.1 (root 17738)

For root `17738`:

- the unique minimum-support completion has support 19 and is non-Hamilton;
- through support 34, exactly 4,869,850 exchange systems are enumerated;
- 49,392 are Hamilton; and
- none is depth-three resident.

Therefore any fixed-endpoint, five-parent, residence-safe Hamilton completion
in the cycle-free path-closure kernel containing one of the audited
root-17738 motifs has support at least 35.

The other audited root families have completion-support floors

\[
\begin{array}{c|rrrrrr}
\text{root}&21641&5801&13620&2575&13616&29776\\ \hline
\text{floor}&21&30&30&35&36&38.
\end{array}                                             \tag{6.1}
\]

Hence a cycle-free path-closure repair imposing an audited motif for every one
of the seven roots has support at least 38.

These are exact finite statements in the path-closure kernel produced by
`scratch/search_k15_root_motif_exchange.cpp`.  Before publication the run
summaries and input hashes should be frozen beside the source; the logical
implications above use only exhaustive coverage and the literal residence
audit.

The scope exclusion is witnessed concretely.  The minimum root-17738 path
closure has support 19.  Multiplying it by the disjoint atlas transfer cycle

\[
                         (3036,6620,7128)               \tag{6.2}
\]

gives a support-22 modification omitted by the kernel.  No residence or Hall
claim is made for that example; it proves only that the path enumeration is
not a global support census.

### Lemma 6.2 (one-component alternatives)

Relative to the dummy-closed H29 successor `p`, let `gamma` be one nontrivial
transfer cycle and consider `p gamma`.

1. If `gamma` has even length, `p gamma` is not Hamiltonian.
2. If `gamma` has length three, every factorable Hamilton child in the exact
   five-parent atlas has Hall deficiency at least 29.

Consequently a successful factorable Hall improvement has at least two
nontrivial transfer cycles, or one odd transfer cycle of length at least five.

#### Proof

The permutation `p` is a 6,436-cycle and hence has sign `-1`.  An even-length
cycle `gamma` also has sign `-1`, so `p gamma` has sign `+1`; a 6,436-cycle
has sign `-1`, proving item 1.  For length three, the exhaustive atlas has 404
simple transfer cycles, 202 Hamilton children, 28 resident/factorable
children, and their deficiencies lie in `29,...,34`.  This proves item 2.
The final assertion exhausts the remaining one-cycle parities.  `square`

### Why this is stronger than a failed local search

The enumerator does not sample `s`-opt moves.  Once a root word is forced, it
enumerates every vertex-disjoint alternating path family pairing the displaced
sources and sinks, up to support 34.  Thus it closes the entire *cycle-free
path-family* class.  Lemma 4.1 explains the failure geometrically: all
Hamilton completions in that scoped class and radius leave at least one
exposed short-run collar.  Additional disjoint alternating cycles are a
separate, explicitly open factor.

## 7. The corrected anchor-transported architecture is closed

Native Result 3.3 and its independently checked proof close exactly the
five-parent, H29-anchor-transported, retained-option architecture.  The
absolute-position model, alternative owner transports, changed frozen
owners, defect-two residual cells, and larger arc catalogues remain open.

The other structural lemmas remain useful after an escape:

- any cut-and-rejoin chronology must still satisfy Lemma 4.1 at every seam;
- every two-parent pointwise hybrid is still a whole-cycle choice by Theorem
  5.1;
- any cycle-free audited root closure still obeys the scoped support bounds
  of Section 6; and
- any new Hall matching must still pass the global owner criterion of Lemma
  2.1.

## 8. The remaining conjecture in its smallest useful form

The target is now a global re-anchoring/rematching/new-chronology statement,
not a repair inside the anchor-transported peeled architecture.

### Conjecture 8.1 (global bounded-meet compiler)

There exists a depth-three resident middle carrier `T` and a complete lower
owner assignment `phi` such that:

1. `T` is Hamilton and its upper rows are complete;
2. `phi` satisfies the full global coordinate conditions (2.3)--(2.4);
3. the resulting source word is nonzero and universal; and
4. its owner meet dimension satisfies

\[
                         \max_p\kappa_p\le2.            \tag{8.1}
\]

The bounded-meet assertion is the only extrapolation from `k<=14`.  The
other conditions are the exact certificate definition of an optimal
`k=15` word.

## 9. Search consequence

The next search must use one of the three scoped escapes rather than repeat
the now-closed anchor-transported lane.

1. **Owner re-anchoring/rematching branch.** First test the exact
   absolute-position inverse-order model, where cell `s` remains ordinal
   rather than following `H29[s]`.  More generally, unfreeze a controlled set
   of the 1,489 peeled pairs and recompute the DM peeling and negative-window
   system together.  Degree-one in the H29 graph is not permanent after the
   carrier moves.
2. **Defect-ladder branch.** Admit baseline defect-two cells, but only through
   their exact dynamic fixed-mask predicates; a scalar defect score is not a
   certificate.
3. **Catalogue-expansion branch.** Add directed arcs outside the five-parent
   union, preferably as whole alternating components with audited residence
   collars.

The 35-target peeled matching remains a useful diagnostic, not a sufficient
final model.  Every Hall-zero candidate must still run the complete sparse
global owner system and measure owner meet dimension.

This preserves the two-scale picture seen in every exact optimum: a globally
nonlocal chronology and rematching, but plausibly a locally one- or two-owner
compiler.

## 10. Primary artifacts

```text
scratch/raw_optimal_k06_k14_compiler_normal_form_audit.json
scratch/analyze_raw_optimal_compiler_normal_form.py
MATH_OWNER_MAP_GEOMETRY_AND_K15_PEELED_CIA_20260728.md
scratch/k15_h29_one_owner_cia_audit.json
scratch/search_k15_root_motif_exchange.cpp
scratch/audit_k15_open_overlay_hybrids.py
scratch/k15_h30_h37_c3_hybrids.json
MATH_ATTACK_R_K15_DETERMINISTIC_FUSION_COMPONENT_ATLAS_20260728.md
```
