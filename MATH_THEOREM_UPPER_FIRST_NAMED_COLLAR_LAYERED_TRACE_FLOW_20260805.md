# Upper-first named collars serialize exactly by one layered trace flow

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact interface theorem.  After an owner order and
an owner-rooted named lower-flag system are fixed, protected serialization is
one ordinary unit-flow/reachability problem in a layered de Bruijn graph.
An accepting path gives the source word, residence, all named lower cells,
and transports every arbitrary-width upper witness of the fixed owner order.
The theorem also identifies the precise quantifier gap in trying to choose an
upper carrier first and then invoke the existing MLD collar theorem.  It does
not prove that the required layered path exists for an MLD collar forest.

## 1. Data exported by the lower theorem

Fix `k,r` and put

\[
                    W={k\choose r},\qquad h=D+1.
\tag{1.1}
\]

Let

\[
                   P=(T_0,T_1,\ldots,T_{W-1})
\tag{1.2}
\]

be a permutation of the rank-`r` layer.  For every owner `T`, let

\[
 \mathcal C_T=(S_{T,1}\subsetneq\cdots\subsetneq S_{T,m_T}\subsetneq T),
 \qquad 0\le m_T\le h,                              \tag{1.3}
\]

be an occurrence-labelled strict flag.  Empty flags are allowed.  Assume
that the members of all flags are pairwise distinct.  In the adjacent-depth
application, the MLD theorem supplies the flags for the **canonical residual
histogram** and the owner label `T` is the central owner of the actual
collar-chain occurrence to which the fragment was attached.  Any targets in
the separately priced triangular boundary/collar bank must be adjoined as a
disjoint owner-rooted flag bank.  The MLD theorem by itself does not say that
its residual flags are the complete strict lower ideal.

Put

\[
                 \mathcal A=2^{[k]}\setminus\{\varnothing\}.
\tag{1.4}
\]

An **`h`-trace realizing `(T,C_T)`** is a word

\[
                   e=(B_0,B_1,\ldots,B_h)\in\mathcal A^{h+1}
\tag{1.5}
\]

such that

\[
                         \bigcup_{j=0}^{h}B_j=T                 \tag{1.6}
\]

and there are strictly increasing suffix lengths

\[
             1\le \ell_1<\ell_2<\cdots<\ell_{m_T}\le h
\tag{1.7}
\]

for which

\[
             S_{T,a}=\bigcup_{j=h-\ell_a+1}^{h}B_j
             \qquad(1\le a\le m_T).                            \tag{1.8}
\]

Write `Tr_h(T,C_T)` for this menu.  Every individual menu is nonempty: this
is the canonical consecutive-clock lemma for a strict chain of length at
most `h`.  Individual nonemptiness, however, will not imply simultaneous
serialization.

The first and last `h` letters of a trace are its de Bruijn states

\[
 \operatorname{pre}(e)=(B_0,\ldots,B_{h-1}),\qquad
 \operatorname{suf}(e)=(B_1,\ldots,B_h).                       \tag{1.9}
\]

Any additional literal protection local to one owner window---a fixed
source letter, a pin, an endpoint role, or a finite trace state---may be
incorporated simply by deleting from `Tr_h(T,C_T)` the traces which violate
it.

## 2. The layered protected-serialization network

Make a layered directed graph `L(P,C)` with layers `0,...,W`.  Its layer
states are copies of `A^h`.  For every

\[
                       e\in\operatorname{Tr}_h(T_i,{\cal C}_{T_i})
\tag{2.1}
\]

put one occurrence-labelled arc

\[
             (i,\operatorname{pre}(e))
                  \longrightarrow
             (i+1,\operatorname{suf}(e)).                       \tag{2.2}
\]

Join a supersource to every state in layer zero and every state in layer
`W` to a supersink.  Prescribed initial or terminal source state is imposed
by retaining only the corresponding supersource or supersink arc.

### Theorem 2.1 (upper-first protected serialization equivalence)

The following are equivalent.

1. There is a nonempty source word

   \[
                   A=(A_0,A_1,\ldots,A_{W+h-1})                 \tag{2.3}
   \]

   such that

   \[
                   \bigcup_{p=i}^{i+h}A_p=T_i
                   \qquad(0\le i<W),                            \tag{2.4}
   \]

   and every flag member `S_(T_i,a)` occurs as a distinct proper suffix
   cell ending at `i+h`.

2. `L(P,C)` has a supersource--supersink directed path.

3. The ordinary unit-flow system on `L(P,C)` is feasible.

The flow polytope in item 3 is integral.  Thus, after `P` and `C` are
fixed, there is no further fractional-rounding, Hall, matroid, or common-cap
gap: the exact remaining interface is one network path.

#### Proof

Suppose item 1 holds.  Its consecutive windows

\[
                 e_i=(A_i,A_{i+1},\ldots,A_{i+h})               \tag{2.5}
\]

belong to the menu (2.1).  Consecutive windows share their literal `h`
letters, so the arcs (2.2) form a path through the layers.

Conversely, let `e_0,...,e_(W-1)` be a layered path.  Write the `h` letters
of `pre(e_0)` and then append the terminal letter of every traversed arc.
Because adjacent states in the path are equal, this spells one word (2.3)
whose window at `i` is exactly `e_i`.  Equations (1.6) and (1.8) give
(2.4) and all named flag cells.

Within one owner, the suffix lengths in (1.7) are distinct.  Between two
owners, the suffix cells have different right endpoints `i+h`.  Hence all
named physical cells are distinct, with no extra matching argument.

Items 2 and 3 are equivalent because a directed path is a unit flow, while
the node--arc incidence matrix of a directed graph is totally unimodular.
Any feasible unit flow therefore has an integral extreme point, which is a
supersource--supersink path after deleting flow cycles; the layered graph
has no directed cycles in any event. \(\square\)

### Corollary 2.2 (protected word consequence)

Assume in addition that:

1. after adjoining any separately priced boundary/collar flag bank, the
   complete flags in (1.3) partition every nonempty target of rank below
   `r`;
2. for every target `U` of rank above `r`, there is an interval `[a,b]`
   such that

   \[
                            U=\bigcup_{i=a}^{b}T_i.               \tag{2.6}
   \]

If `L(P,C)` has a path, its spelling `A` is universal and has length

\[
                              W+h.                               \tag{2.7}
\]

In the adjacent-depth application `h=D+1`, this is `B(k)+1`.

#### Proof

The flags cover the strict lower ideal and (2.4) covers every rank-`r`
owner once.  For (2.6), associativity gives

\[
 \bigcup_{i=a}^{b}T_i
   =\bigcup_{i=a}^{b}\bigcup_{p=i}^{i+h}A_p
   =\bigcup_{p=a}^{b+h}A_p.                                  \tag{2.8}
\]

Thus every upper target is an interval union of the same source word.
Every source letter is nonempty by (1.4). \(\square\)

The existence of the path also supplies the exact depth-`h` residence
antecedent.  Therefore residence need not be imposed again after this
flow.  If a proposed owner order passes only a run-count surrogate but the
network is empty, it has no source spelling carrying the declared flags.

## 3. Relation to Shadow--Braid and common `Q`

Theorem 2.1 is a fixed-order specialization of the coloured trace--Euler
criterion.  It is weaker than carrying the full RSB fragment relation:
the owner order has already been chosen, is already connected, and its
upper service has already been certified.  What remains is only the
literal overlap of the owner-labelled trace menus.

It is also an exact replacement for the terminal common-`Q` test on this
suffix-flag face.  The path spells the source letters themselves, so every
positive hit and every negative equality is already literal.  Conversely,
any source word satisfying the common-`Q` system produces the layered path
by taking its consecutive windows.  Hence there is no hidden implication
from named containment to common `Q`: common `Q` is precisely what the
trace overlaps enforce here.

There is a useful sufficient subface.  Suppose the maximal erosion of `P`
is nonempty and satisfies the central residence equation.  For every
interior owner position and `1<=q<=h` with `i+q<W`, put

\[
                 N_{i,q}=\bigcap_{j=0}^{q}T_{i+j}.                \tag{3.1}
\]

The maximal erosion word `E` satisfies the exact natural-pin identity

\[
                 N_{i,q}=\bigcup_{p=i+q}^{i+h}E_p.               \tag{3.2}
\]

Consequently, if every declared interior flag is a subflag of

\[
             N_{i,h}\subseteq N_{i,h-1}\subseteq\cdots
                 \subseteq N_{i,1}\subseteq T_i,                 \tag{3.3}
\]

then all those pins coexist automatically in `E`.  Natural pins are
negative-inert, and with no nonnatural pins there is no additional
positive-hit failure.  The terminal `h` owner positions and any opening or
seam pins remain boundary data; (3.2) does not silently certify them.

Thus an upper-first proof has two exact options:

* prove that the named collar forest embeds in the natural towers (3.3),
  plus a boundary collar; or
* prove reachability in the complete layered network of Section 2.

The first is stronger but makes literal compatibility automatic.  The
second is necessary and sufficient.

## 4. Exact quantifier boundary

Let `U` be any class of owner orders already certified to be owner-once,
connected, and arbitrary-upper-complete.  Let `F_low^comp` be the class of
completed named lower flag systems obtained by adjoining a disjoint,
already-priced boundary/collar bank to a canonical residual MLD forest.  The
exact upper-first target is

\[
 \boxed{
   \exists P\in\mathcal U\ \exists\mathcal C\in\mathcal F_{\rm low}^{\rm comp}
   \quad s\leadsto t\text{ in }L(P,\mathcal C).}
\tag{4.1}
\]

At the level of bare existential logic the two existential quantifiers in
(4.1) commute.  At the level of the available theorems they do not
decouple:

* the upper theorem, if available, would produce `P` without flags;
* the MLD theorem produces some residual named forest using unconditioned
  uniform Boolean interface matchings, while the boundary/collar bank is a
  separate priced input; and
* neither theorem proves that their outputs intersect the reachability
  relation in (4.1).

Conditioning the MLD process on `s -> t` reachability is not covered by the
MLD preservation theorem: the event is a global conjunction of literal
overlap constraints and may depend on the realized Boolean paths.  Hence
the inference

\[
 \text{choose an upper carrier }P
 \quad\Longrightarrow\quad
 \text{apply the existing MLD theorem afterward}                \tag{4.2}
\]

is not valid without a new carrier-conditioned MLD theorem or a direct
proof of (4.1).

For a fixed `P`, the weakest exact reversed-order statement is simply

\[
 \boxed{
  \exists\mathcal C\in\mathcal F_{\rm low}^{\rm comp}:
       L(P,\mathcal C)\text{ has a unit flow}.}                  \tag{4.3}
\]

This is not vague compatibility: after `C` is fixed it is the explicit
network of Section 2.  If the lower flags are also left variable inside
the network, their target-once equations are side constraints

\[
       \sum_{e:\,S\text{ is marked on }e}x_e=1
       \qquad(S\text{ every strict lower target}),               \tag{4.4}
\]

coupled to the layer-flow equations.  The pure network integrality of
Theorem 2.1 applies only after the named forest is fixed; it does not make
the enlarged coloured exact-cover matrix totally unimodular.

## 5. A literal two-owner no-go

Named containment and individual trace existence do not imply the layered
path condition, even when the owner segment itself has an unmarked
depth-two spelling.

Take `h=2` and the two rank-three owners

\[
                         T_0=\{1,2,4\},\qquad
                         T_1=\{1,2,3\}.                         \tag{5.1}
\]

The word

\[
                              (\{4\},\{2\},\{1\},\{3\})          \tag{5.2}
\]

spells this owner segment, so the unmarked segment is genuinely
depth-two resident.  Give the owners the target-disjoint full flags

\[
 \{1\}\subset\{1,2\}\subset T_0,
 \qquad
 \{3\}\subset\{2,3\}\subset T_1.                              \tag{5.3}
\]

Each flag is individually traceable.  The first flag forces the terminal
letter of its trace to be exactly `{1}`: a one-letter suffix with union
`{1}` has no other possibility.  In every trace for the second flag, its
penultimate letter `B` satisfies

\[
                 B\cup\{3\}=\{2,3\},
 \qquad\text{so}\qquad 2\in B\subseteq\{2,3\}.                  \tag{5.4}
\]

If a trace of the first owner is followed by a trace of the second, their
two-letter de Bruijn states overlap.  The terminal letter of the first
trace is therefore the penultimate letter of the second.  This would require
`{1}=B`, contradicting (5.4).  Hence the two-layer network is empty.

This is a local no-go, not a claim about extending (5.1) to a complete
upper carrier.  Its exact scope is enough to refute any local implication

\[
 \text{resident owner segment + named contained flags
       + individual clocks}
 \Longrightarrow
 \text{common literal spelling}.                              \tag{5.6}
\]

The missing row is precisely the overlap flow of Theorem 2.1.

## 6. The sharpened protected-serialization frontier

Combining the MLD exceptional-bank theorem with the present equivalence
leaves the following single exact theorem on the lower/physical interface:

> **Carrier-conditioned named trace-flow theorem.**  There is an
> owner-once, arbitrary-upper-complete order `P` and a completed named lower
> flag system `C` (canonical residual MLD forest plus its disjoint priced
> boundary/collar bank) for which `L(P,C)` has a unit flow, with the required
> endpoint and next-lift protected arcs retained.

An accepting flow immediately gives:

1. one connected linear owner order;
2. a nonempty depth-`D+1` resident source word;
3. every named lower target in a distinct actual suffix cell;
4. every arbitrary-width upper witness already certified on `P`; and
5. any finite literal protection incorporated in the trace menus.

No separate compiler, common-`Q`, lower Hall, or serialization theorem
remains after that flow.  What is still open is existence of the correlated
pair `(P,C)` and its path; neither upper completeness nor the MLD collar
theorem alone implies it.

## 7. Dependencies and scope

1. `MATH_THEOREM_MLD_EXCEPTIONAL_BANK_ADJACENT_TAIL_RESERVE_AND_JOINT_NAMED_LIFT_20260805.md`;
2. `MATH_THEOREM_MLD_ADJACENT_DEPTH_ZERO_DEFECT_LOWER_FOREST_AND_SAME_DEPTH_C0_BOUNDARY_20260805.md`;
3. `MATH_SYNTHESIS_FRACTIONAL_CONFIGURATION_TO_ZERO_DEFECT_ADJACENT_COLLAR_20260805.md`;
4. `MATH_THEOREM_BOUNDED_CHAIN_TRACE_EULER_SERIALIZATION_AND_SIDECAR_DISTANCE_20260801.md`;
5. `MATH_AUDIT_CORRECTED_SHADOW_BRAID_SUFFICIENCY_AND_PASCAL_SEAM_20260728.md`;
6. `MATH_THEOREM_FLAG_INTERVAL_RUN_AUTOMATON_AND_LITERAL_SERIALIZATION_20260804.md`.

This note proves no all-price configuration inequality, no existence of an
upper-complete owner order, no carrier-conditioned MLD theorem, and no
`B(k)+1`, `B(k)+O(1)`, or exact all-`k` result.
