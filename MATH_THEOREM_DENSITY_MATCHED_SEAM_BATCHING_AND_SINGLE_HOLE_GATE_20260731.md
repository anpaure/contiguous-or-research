# Density-matched seam batching: the exact Haxell theorem and the single-hole gate

Date: 2026-07-31  
Lane: density-matched additive-constant reset  
Status: exact batching, extraction, and selector theorem proved.  The natural
fixed-slot C6 subclass is ruled out.  One explicitly stated physical/compiler
macro theorem remains open.  No unconditional `nu(k)<=B(k)+O(1)` claim is
made.

## 0. Verdict

The numerical reset mechanism is sound.

Suppose `F=Theta(W)` occurrence-labelled seam failures are arranged in their
physical order, and put `d=Theta(sqrt(m))`.  Consecutive batching gives

\[
                 H\le \left\lceil {F\over h}\right\rceil
                    =O(W/d),\qquad h=Theta(d),                    \tag{0.1}
\]

with `O(d)` changed seams in each batch.  If one batch has a synchronized
`m x m` menu of equal-length replacements, and every constituent replacement
has the same full prefix/suffix union signature as its off-state and dominates
its old internal union deck, then the entire batch is one all-width-transparent
macro.  If at most `O(m)` parameter pairs are lost per constituent seam, the
macro retains

\[
                         m^2-O(dm)=Omega(m^2)                     \tag{0.2}
\]

options.

The exact raw C6 row energy

\[
 R_m=18m^3+51m^2-4m-5<44m^3                                  \tag{0.3}
\]

then has precisely the right density.  At

\[
                         p={\theta\over dm},                     \tag{0.4}
\]

the frozen alteration theorem gives `Theta(W/d)` retained anchors and
average external conflict

\[
                     O(pR_m)=O(m^2/d)=O(dm),                    \tag{0.5}
\]

where the last equality uses `d^2=Theta(m)`.  Per-list Markov pruning and
Haxell therefore select all `O(W/d)` macros.

This is an actual batching/selection theorem, not just a count.  It also
identifies the exact construction gap.  The repository does **not** presently
supply the synchronized quadratic macro menu in (0.2):

* a raw anchored fixed-slot C6 has only `m` full-signature-safe choices;
* adding internal-deck dominance leaves only one choice;
* concatenating `Theta(d)` abstract fixed-4 identities leaves one antipodal
  physical seam per atom and, naively, `Theta(d)` compiler reservations; and
* the task-blind sparse extraction need not satisfy Hall for the prescribed
  consecutive batches.

Thus the remaining theorem is a **candidate-dependent, single-moving-hole
buffered C6 chain** together with one correlated batch-to-anchor Hall row.
The sparse row energy and Haxell arithmetic are no longer open.

## 1. Ordered batching of the canonical failure bank

Let

\[
                  f_1,f_2,\ldots,f_F                              \tag{1.1}
\]

be the phase-resolved, occurrence-labelled elementary seam/exposure failures
in physical cyclic order.  Repeated appearances in different phases are
listed with multiplicity.  Assume

\[
                         c_-W\le F\le c_+W                       \tag{1.2}
\]

for fixed positive constants.  Let one elementary actuator change at most
`s_*` physical seams, where `s_*` is absolute.  Choose

\[
                   h=\left\lfloor {D\over s_*}\right\rfloor,    \tag{1.3}
\]

where `D=Theta(d)` and `D>=2s_*`.

Partition (1.1) consecutively into blocks `J_1,...,J_H` of order at most
`h`, with only the last block possibly shorter.

### Lemma 1.1 (exact batch count)

The partition has

\[
 H=\left\lceil {F\over h}\right\rceil
    \le {c_+s_*W\over D}+2=O(W/d),                              \tag{1.4}
\]

and every block asks to change at most `s_*h<=D` seams.

#### Proof

This is division with remainder, followed by (1.2)--(1.3).  The failures are
occurrence-labelled, so no cancellation between phases has been used.  \(\square\)

Lemma 1.1 is the proof-safe form of “batch the linear seam debt.”  It says
nothing yet about whether one physical macro can realize a block.

## 2. Transparent local replacements really do form one macro

Fix one baseline word `A`.  Inside one batch interval let

\[
                     X_1,\ldots,X_q,\qquad q\le h,               \tag{2.1}
\]

be pairwise position-disjoint subslots, in physical order, with unchanged
gaps between them.  For a parameter `omega` replace `X_i` by an equal-length
word `Y_i(omega)`.  Write `Sigma_vee` for the complete ordered prefix/suffix
OR signature and `D(X)` for the set of all internal interval unions.

Assume for every `i,omega` that

\[
       \Sigma_\vee(X_i)=\Sigma_\vee(Y_i(\omega)),\qquad
       {\cal D}(X_i)\subseteq{\cal D}(Y_i(\omega)).              \tag{2.2}
\]

Let `X` be the hull from the first position of `X_1` to the last position of
`X_q`, including the unchanged gaps, and let `Y(omega)` be the simultaneously
modified hull.

### Lemma 2.1 (macro transparency)

For every `omega`,

\[
       \Sigma_\vee(X)=\Sigma_\vee(Y(\omega)),\qquad
       {\cal D}(X)\subseteq{\cal D}(Y(\omega)).                  \tag{2.3}
\]

Consequently all `q` switches form one all-width upper-transparent macro.

#### Proof

Apply the unary replacement theorem successively to the disjoint subslots.
Every interval crossing a changed subslot keeps its value at the same
address.  In particular every prefix or suffix of the hull keeps its value,
which proves signature equality in (2.3).

An old interval internal to the hull is either unchanged, crosses the
boundary of at least one subslot and hence is pointwise preserved, or lies
wholly in one `X_i` and is rehosted inside `Y_i(omega)` by (2.2).  This proves
internal-deck dominance.  \(\square\)

This lemma is why `Theta(d^2)` internal windows do not become global packet
tickets.  Their certification is unary before selection.

## 3. A synchronized quadratic list survives `Theta(d)` local guards

Let

\[
                         \Omega=B\times C,qquad |B|=|C|=m.      \tag{3.1}
\]

For each constituent `i`, allow a bijective reindexing
`pi_i:Omega->Omega` of its native C6 parameter grid.  The macro option at
`omega` uses the `pi_i(omega)` option at every constituent.

Let `Q_i subseteq Omega` be the parameters rejected by all unary guards at
constituent `i`: signature/deck, residence, internal palette, fixed topology,
and the compiler input/output state.  Any interface guard between consecutive
constituents is charged to either endpoint.  Assume

\[
                              |Q_i|\le gm                          \tag{3.2}
\]

for an absolute `g`.

### Lemma 3.1 (quadratic macro supply)

The common good-parameter set

\[
       \Omega_J=\Omega\setminus
             \bigcup_{i\in J}\pi_i^{-1}(Q_i)                    \tag{3.3}
\]

satisfies

\[
                         |\Omega_J|\ge m^2-ghm.                  \tag{3.4}
\]

In particular, if `h<=D/s_*` and `D=o(m)`, then
`|Omega_J|=(1-o(1))m^2`.

#### Proof

Every `pi_i` is a bijection, so its pulled-back bad set still has order at
most `gm`.  Apply the union bound over at most `h` constituents.  \(\square\)

The statement needs only a linear number of rejected pairs per elementary
switch.  A common `O(1)` star cover is a convenient sufficient certificate;
independence of the guards is not required.

## 4. Exact row-energy batching

The following lemma records the useful algebra behind synchronized products.
It is independent of the Boolean specialization.

For each atomic anchor `e`, let `P_e={p_e(omega):omega in Omega}` have order
`L=m^2`.  For different anchors put

\[
 K(e,f)={1\over L}
       |\{(\omega,\eta):p_e(\omega)\sim p_f(\eta)\}|.            \tag{4.1}
\]

Partition an anchor family into batches `J`.  The full synchronized macro
list at `J` is

\[
 P_J=\{\bigcup_{e\in J}p_e(\pi_e(\omega)):\omega\in\Omega\}.    \tag{4.2}
\]

Assume that incompatibility between two macros is witnessed by an
incompatibility between at least one pair of their atomic constituents,
plus optional separately counted reservation tokens.

### Lemma 4.1 (diagonal row inequality)

Ignoring the separate reservation row,

\[
                         K(J,J')
        \le\sum_{e\in J}\sum_{f\in J'}K(e,f).                    \tag{4.3}
\]

Hence if the union of all atomic anchors is `R`-row-sparse,

\[
                 \sum_{f\ne e}K(e,f)\le R,                      \tag{4.4}
\]

then every batch of order at most `h` has macro row at most `hR`.

#### Proof

Use the union bound over constituent pairs.  For fixed `(e,f)`, the number
of conflicting macro-parameter pairs is exactly the number in (4.1), because
`pi_e,pi_f` are bijections of `Omega`.  Divide by `L` and sum.  Summing
(4.3) over all other batches and then using (4.4) gives at most `|J|R`.
\(\square\)

Lemma 4.1 is useful when a macro is literally a diagonal composition of
atomic lists.  The sharper density-matched route below treats one buffered
macro as one C6 anchor; then the factor `h` is absent and the long collar is
required to be unary/private.

## 5. Density-matched extraction at the batch scale

Let

\[
                  W={2m+1\choose m},\qquad I=(m+1)W.             \tag{5.1}
\]

The raw directed-incidence C6 atlas has `I` anchors, list order `m^2`, and
row (0.3).  Assume

\[
                 c_0m\le d^2\le c_1m,qquad d=o(m),              \tag{5.2}
\]

as holds for the deadline depth.  Suppose the batch count obeys

\[
                              H\le\gamma W/d.                    \tag{5.3}
\]

Choose a constant `theta>4gamma/3` and put `p=theta/(dm)`.

### Theorem 5.1 (unprescribed density-matched reservoir)

For all sufficiently large `m`, the raw atlas contains an anchor family `S`
with

\[
 |S|\ge {3pI\over4}>H,                                          \tag{5.4}
\]

and every retained list has average external conflict at most

\[
                    4pR_m< {176\theta m^2\over d}
                         \le {176\theta\over c_0}dm.             \tag{5.5}
\]

If every assigned guarded macro list retains at least `alpha m^2` choices,
all additional upper/compiler/topology conflicts contribute average row at
most `kappa dm` on each guarded list, and the tasks admit an injective
assignment into `S`, then one compatible option can be selected for every
task once

\[
 {1408\theta\over\alpha^2d}
       +{8\kappa d\over\alpha m}<1.                             \tag{5.6}
\]

#### Proof

Apply the tunable exact-energy alteration with density `p`.  It gives
`|S|>=3pI/4` and row at most `4pR_m`.  Since

\[
 {3pI\over4}={3\theta(m+1)W\over4dm}>{3\theta W\over4d}
              >\gamma W/d,
\]

(5.4) follows.  Equation (0.3), followed by `d^2>=c_0m`, gives (5.5).

Passing to an assigned subset of `S` cannot increase a nonnegative row.
Unary filtering of the source list from `m^2` to at least `alpha m^2`
increases its normalized row by at most `alpha^{-1}`.  Thus every guarded
part has average degree at most

\[
                        \overline\Delta
                  \le {4pR_m\over\alpha}+\kappa dm.              \tag{5.6a}
\]

Delete options of degree greater than `2 overlineDelta`.  At least half of
every part remains and the induced maximum degree is at most
`2 overlineDelta`.  Haxell applies when

\[
 {\alpha m^2\over2}\ge4\overline\Delta,
 \quad\text{i.e.}\quad
 \alpha m^2\ge {32pR_m\over\alpha}+8\kappa dm.
\]

Using `R_m<44m^3` and `p=theta/(dm)` gives the sufficient inequality
(5.6).  Pairwise independence composes globally under the fixed-skeleton,
unary-transparency, and complete-ticket hypotheses.  \(\square\)

The theorem deliberately separates two facts.  The sparse C6 theorem gives
enough anchors with the right row.  It does **not** say that a task-blind
outcome `S` satisfies Hall for the prescribed consecutive batches.

### Corollary 5.2 (exact prescribed-task interface)

Let `G=(T,S;E_G)` join a batch task to every retained anchor at which its
entire transparent macro menu is physically realizable.  If

\[
                         |N_G(X)|\ge|X|\qquad(X\subseteq T),     \tag{5.7}
\]

then Theorem 5.1 applies after any task-saturating matching in `G`.

This is just Hall plus row monotonicity.  It is the weakest exact assignment
row after `S` is fixed.

## 6. One compiler reservation per macro

The clean compiler interface is the following.  Fix one trace-guarded
matching `M_0`.  For each batch `J`, reserve one `M_0`-closed local block
`R_J` consisting of its changed compiler targets and cells.  Require:

1. the blocks `R_J` are pairwise target- and cell-disjoint;
2. every option for `J` carries an integral local matching on `R_J` with the
   same boundary pins; and
3. outside `R_J`, every incidence of `M_0` and every trace guard is unchanged.

### Lemma 6.1 (single-reservation composition)

Under these rows, one compiler reservation per selected macro is sufficient;
the restriction of `M_0` outside all `R_J`, united with the selected local
matchings, is one global trace-guarded compiler matching.

#### Proof

Closedness removes every old matching edge incident with a replaced target
or cell.  Disjointness makes the local target and cell ranges a direct sum,
and common pins make their union consistent.  Every remaining edge and guard
is literally an unchanged edge of `M_0`.  \(\square\)

An unused single cell is the smallest possible `R_J`, but it is not the only
one.  This distinction is necessary: the scalar lower-bound slack, hence the
size of a fixed unused-cell bank, has no known uniform lower bound of order
`W/d`.  A proof which asks for one distinct unused cell per macro therefore
needs an additional slack theorem.  A balanced local rematching block avoids
that artificial requirement.

## 7. Why the current C6 does not instantiate the theorem

The missing hypothesis is not hidden in the asymptotics.

### Proposition 7.1 (fixed-slot quadratic-list no-go)

For the raw anchored C6 word

\[
 (C,C+a,C-b+a,C-b+a+c,C-b+c,C+c),                        \tag{7.1}
\]

relative to one fixed off-slot `(b_0,c_0)`, full prefix/suffix union
signature permits exactly the `m` choices

\[
                              B\times\{c_0\}.                    \tag{7.2}
\]

If old internal-union coverage is also required, only `(b_0,c_0)` survives.
Consequently no batching or Haxell argument can obtain an
`Omega(m^2)` list from this fixed-slot subclass.

#### Proof

The signature determines `c` from the last cell or the first prefix
containing it, while it is independent of `b`.  The old internal singleton
`C-b_0+a` can reappear in the new six-word only when `b=b_0`.  These are the
fixed-slot signature and internal-dominance theorems.  Intersecting several
such safe sets cannot increase their order.  \(\square\)

There is a stronger length obstruction.  A common fixed Johnson slot of
length `O(d)=o(m)` whose options introduce their selected exterior coordinate
cannot have `m^2-O(md)` signature-safe choices: the common-slot arrival
theorem forces length at least `m-O(d)`.  Therefore the desired buffered
macro must use at least one of:

* candidate-dependent off-slots/addresses;
* a non-Johnson or nonflat temporary buffer;
* the balanced fixed-4 serialization; or
* a larger moving-hole ear whose visible slot is not a common anchored C6.

The balanced fixed-4 identity has exact signature and graded internal-deck
equality, but every six-owner serialization has one antipodal non-Johnson
seam.  Concatenating `Theta(d)` such identities naively leaves
`Theta(d)` antipodal seams and `Theta(d)` compiler domains.  Reducing these
to one reservation is a serial hole-transport theorem, not a consequence of
the resource identity.  The known fixed-parameter actuator transports one
head hole but changes four inherited cap assignments, so it does not yet
supply Lemma 6.1.

There is a newer, weaker coverage-level interface: inclusion of the
**distinct** prefix, suffix, and internal OR decks, plus equality of the
total OR, preserves old coverage without preserving plateau timings.  The
fixed-slot no-go above is deliberately scoped to the full ordered signature
required in this note; it does not rule out a quadratic menu under that
compressed-deck criterion.  Replacing (2.2) by the compressed conditions
leaves all batching and Haxell arguments unchanged, but still requires the
same physical single-hole serialization and prescribed Hall row.

Finally, extraction cannot simply be made task-blind.  There are task banks
with `m+1` eligible native incidences per task and automatic Hall whose every
representative assignment has raw row `Omega(m^2)`.  Since
`dm=o(m^2)`, the canonical physical order must be used to prove (5.7) or a
fractional-pressure substitute; degree alone is insufficient.

## 8. The exact remaining construction theorem

All unresolved rows can be collected into one statement.

> **Synchronized single-hole buffered-chain theorem.**  For the consecutive
> batching in Lemma 1.1, construct a density-matched anchor family `S` and a
> task-saturating matching into `S` such that every matched task--anchor pair
> has a common `m x m` parameter grid of literal `O(d)`-seam replacements
> with:
>
> 1. a candidate-dependent off-slot or balanced serialization having equal
>    full prefix/suffix union signature and internal-union dominance;
> 2. all residence, palette, and fixed-topology failures contained in
>    `O(d)` parameter stars, hence `m^2-O(md)` surviving options;
> 3. one moving physical/compiler hole which serializes every antipodal seam
>    and returns to one `M_0`-closed reservation block with fixed boundary
>    pins; and
> 4. no cross-list resource row beyond the raw C6 row plus `O(m)` private
>    reservation load.

Given this theorem, Lemmas 1.1--3.1, Theorem 5.1, and Lemma 6.1 select and
compose all `O(W/d)` macros.  The linear canonical seam debt is reset in one
dimension with no exported target loss.  Combined with the frozen bounded
terminal theorem, this is the density-matched route to

\[
                              \nu(k)\le B(k)+O(1).                \tag{8.1}
\]

The new theorem is strictly narrower than the previous four-fibre common-cap
intersection: the common cap has been replaced by one local closed block per
macro.  It is still a genuine construction theorem.  Neither raw C6
abundance, full-signature algebra, nor the sparse extraction supplies its
single moving hole or its prescribed Hall row.

## 9. Dependencies and scope

This note uses, without strengthening:

* `MATH_THEOREM_SPARSE_C6_AVERAGE_LOAD_EXTRACTION_20260731.md`;
* `MATH_AUDIT_PEER_SPARSE_C6_EXACT_ENERGY_AND_TUNABLE_EXTRACTION_20260731.md`;
* `MATH_THEOREM_K_SPARSE_C6_PRESCRIBED_TASK_SPREAD_SDR_20260731.md`;
* `MATH_THEOREM_FULL_PREFIX_SUFFIX_UNION_BOUNDARY_SIGNATURE_20260731.md`;
* `MATH_THEOREM_COMPRESSED_PREFIX_SUFFIX_DECK_TRANSPARENCY_20260801.md`;
* `MATH_THEOREM_A_INTERNAL_DOMINANCE_UPPER_GUARD_AND_FIXED4_DECK_20260731.md`;
* `MATH_THEOREM_O1_TRANSPARENT_PACKET_UNUSED_BASIS_COMPOSITION_20260731.md`;
* `MATH_THEOREM_AD_BUFFERED_HEX_GLOBAL_COMPOSITION_HAXELL_AND_BOUNDED_SIDECAR_20260731.md`; and
* `MATH_THEOREM_H2_COMPILER_DUAL_RADO_INTERVAL_LAMINAR_GATE_20260731.md`.

It proves the batching and selector implication and rules out the natural
fixed-slot realization.  It does not construct the synchronized single-hole
buffered chain, prove prescribed Hall for the canonical lift, or claim the
all-`k` upper bound.
