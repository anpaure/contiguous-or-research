# Bounded components: exact completed-hinge fusion and guarded overlap tours

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical fusion and overlap theorems,
conditional physical implication under an explicitly separable guarded
connector atlas.  No search or computational construction is used.  The
result identifies the exact additional state needed after the
bounded-component pull rescue; it does not prove that every rescued factor
exposes the required completed hinges or regenerative ports.

## 0. Outcome

Suppose a protected carrier has `c` directed factor cycles after the
maximal transparent-pull-forest rescue.

There are two different ways to remove the residual component debt.

1. **Completed-hinge fusion.**  Reassign already existing protected-safe
   hinge heads.  This changes no physical length.  With one chosen hinge in
   each component, zero-cost fusion is possible exactly when the induced
   component compatibility digraph has a directed Hamilton cycle.
2. **Guarded overlap tour.**  Open each component at a declared port and
   join the resulting bodies with literal connector macros.  Relative to a
   product-separable connector atlas, the exact added length is a weighted
   Hamilton-path problem on the ports.

For bare order-`d` histories `u,v`, the exact connector distance is

\[
 \boxed{
 \delta_d(u,v)=d-\operatorname{ov}(u,v),}
\tag{0.1}
\]

where `ov` is suffix--prefix overlap.  Thus

\[
 \delta_d(u,v)\le K
 \iff
 \operatorname{suffix}_{d-K}(u)
  =\operatorname{prefix}_{d-K}(v).
\tag{0.2}
\]

In particular, two components may cost `d` even though `c=2`.

The minimal order-free `K`-regenerative history interface is a common
literal core of length `d-K`: a complete all-pairs `K`-router exists at the
history level if and only if every exit ends and every entry begins with
one common `(d-K)`-word.  Full physical regeneration must additionally
carry the complete residence, upper-witness, occurrence, cap, and compiler
boundary signature.

## 1. Literal histories and guarded connector cost

Let `Sigma` be the alphabet of nonempty literal source letters.  An
order-`d` history is a word

\[
                         u=(u_1,\ldots,u_d)\in\Sigma^d.
\]

For histories `u,v`, put

\[
 \operatorname{ov}(u,v)
 =\max\{q:0\le q\le d,
          (u_{d-q+1},\ldots,u_d)=(v_1,\ldots,v_q)\}.
\tag{1.1}
\]

A bare de Bruijn connector appends letters, shifting one position at every
step.

### Lemma 1.1 (exact bare-history distance)

The minimum number of letters which must be appended to move from `u` to
`v` is (0.1).

#### Proof

After appending `s<d` letters, the final history retains the last `d-s`
letters of `u`.  Equality with `v` requires these letters to equal the
first `d-s` letters of `v`, so

\[
                         s\ge d-\operatorname{ov}(u,v).
\]

Appending the unmatched suffix of `v` attains equality. \(\square\)

A physical connector carries more state than its history.  A **guarded
port** `p` has:

* an exit history `out(p)` and an entry history `in(p)` as applicable;
* the complete boundary residence/age state;
* every protected upper-witness and occurrence ticket;
* its cap/compiler boundary state; and
* a declared opening charge `alpha(p)>=0`.

For an exit port `p` and entry port `q`, define

\[
 \gamma(p,q)\in\mathbb Z_{\ge0}\cup\{\infty\}
\tag{1.2}
\]

to be the minimum **additional physical-position charge** of a declared
connector macro which carries the full state from `p` to `q` and preserves
every hard guard.  If no such macro exists, the value is infinity.  Every
literal macro obeys

\[
                         \gamma(p,q)
 \ge\delta_d(\operatorname{out}(p),\operatorname{in}(q)).
\tag{1.3}
\]

Equality in (1.3) requires the shortest literal append path itself to be
guard-transparent; history overlap alone does not prove that.

## 2. Exact guarded overlap-tour theorem

Let the residual directed components be

\[
                         C_1,\ldots,C_c.
\]

For component `C_i`, let `P_i` be its finite nonempty set of allowed cuts.
Cut `p in P_i` retains one directed body, gives its entry and exit guarded
ports, and has opening charge `alpha(p)`.

The connector atlas is called **product-separable** when any collection of
macros on distinct declared joins is jointly legal exactly when every macro
is legal individually, and its total physical charge is the sum of the
individual charges.  This holds, for example, when mutable supports and
unit resources are private and all remaining ledgers are additive.  If
connectors share cap units or nonlocal witnesses, those resources must
first be added to one joint product state; individual `gamma` values then
do not compose.

Define the linear-tour charge

\[
 \begin{split}
 \Gamma_{\rm lin}
 =\min_{\substack{p_i\in P_i\\
                   (i_1,\ldots,i_c)\text{ a permutation}}}
 \left[
   \sum_{i=1}^c\alpha(p_i)
   +\sum_{t=1}^{c-1}\gamma(p_{i_t},p_{i_{t+1}})
 \right].
 \end{split}
\tag{2.1}
\]

Define `Gamma_cyc` by also adding
`gamma(p_(i_c),p_(i_1))`.

### Theorem 2.1 (exact guarded overlap tour)

Relative to a product-separable cut-and-connector atlas:

1. `Gamma_lin` is the minimum additional position charge of one protected
   directed path containing every component body once; and
2. `Gamma_cyc` is the minimum additional position charge of one protected
   directed cycle containing every component body once.

#### Proof

Choose cuts and an order attaining (2.1).  Traverse the retained body of
`C_(i_1)`, its selected connector, the body of `C_(i_2)`, and so on.
Product separability makes all macros jointly legal and makes their charges
add.  This constructs the required path.  The cyclic formula adds the last
connector back to the first component.

Conversely, any object in this declared model chooses one cut in every
component and induces the order in which its component bodies are met.
Between consecutive bodies it uses an allowed connector of charge at least
the corresponding `gamma`; every selected cut pays its `alpha`.  Summing
gives the reverse inequality. \(\square\)

### Corollary 2.2 (constant-cost path criterion)

If `c<=C`, all chosen openings have total charge at most `A`, and the
component port graph has a directed Hamilton path whose every connector
has charge at most `K`, then

\[
                         \Gamma_{\rm lin}
 \le A+(C-1)K.
\tag{2.2}
\]

For absolute `A,C,K`, this is `O(1)`.  The analogous cyclic bound is
`A+CK`.

If the pull rescue leaves `c=O(d)` components, a constant cost per join
still gives `O(d)`, not an additive constant.  In that regime, all but
`O(1)` joins must have zero charge, or a zero-cost completed-hinge fusion
must act on the large component bank at once.

## 3. Exact zero-cost completed-hinge fusion

Now use existing physical packets instead of adding connector positions.
Suppose each component `C_i` contains one selected unprotected packet

\[
                         e_i=K_i(a_i,h_i),
\tag{3.1}
\]

and role `i` is a **completed hinge**: for every `h in H_i`, the packet
`K_i(a_i,h)` is a literal replacement with the same rolewise owner,
palette, residence, upper-witness, cap, and compiler payload.

All heads and packets here are occurrence-labelled.  Assume the hinges form
one jointly completed family: mutable resources are private by role, while
every shared ledger depends only on the multiset of used tails and heads.
Consequently any supported permutation which uses every selected head once
is simultaneously legal.  Separate individually completed rectangles
without this product/shared-ledger property are not enough.

Make the component compatibility digraph `Q` on `[c]` by

\[
                         i\longrightarrow j
 \iff h_j\in H_i.
\tag{3.2}
\]

### Theorem 3.1 (exact completed-hinge Hamilton criterion)

Using exactly the chosen tails `a_i`, chosen heads `h_i`, and their
completed rectangles, a zero-extra-position fusion into one factor cycle
exists if and only if `Q` contains a directed Hamilton cycle.

More generally, if `pi` is any supported permutation of `[c]`, replacing

\[
 K_i(a_i,h_i)
 \quad\text{by}\quad
 K_i(a_i,h_{\pi(i)})
\tag{3.3}
\]

produces exactly as many factor components as `pi` has permutation cycles.

#### Proof

Remove `e_i` from `C_i`.  The remaining directed body is a path from
`h_i` to `a_i`.  After (3.3), following that body continues from `a_i` to
`h_(pi(i))`.  Thus the component successor map is exactly `pi`, and the
components of the new factor are exactly its permutation cycles.

Every replacement is literal because `i->pi(i)` is an edge of `Q`.
Every head is used once, every tail is fixed, and the completed-hinge
hypothesis makes all protected payloads rolewise invariant.  No physical
position is added.  One component is obtained exactly when `pi` is one
cycle, equivalently when its arcs form a directed Hamilton cycle of `Q`.
\(\square\)

### Corollary 3.2 (common completed head bank)

If

\[
                         h_j\in H_i
 \qquad(i\ne j),
\tag{3.4}
\]

then any cyclic ordering of the components gives a zero-cost fusion.

There is a weaker cut-expansion certificate.  Put

\[
                         M_i=\{j:h_j\in H_i\}.
\]

Assume the original packet is allowed, so `i in M_i`, and for every
nonempty proper `S subset [c]` put

\[
 \mathcal D(S)
 =\sum_{i\in S}|([c]-S)-M_i|
  +\sum_{j\notin S}|S-M_j|.
\tag{3.5}
\]

### Corollary 3.3 (two-switch zero-cost fusion)

If

\[
                         \mathcal D(S)<|S|(c-|S|)
 \qquad(\varnothing\ne S\subsetneq[c]),
\tag{3.6}
\]

then `Q` has a directed Hamilton cycle, obtainable from the identity cycle
cover by completed-hinge two-switches which reduce the number of components
one at a time.

#### Proof

Take any union `S` of current permutation cycles.  If no roles
`i in S,j notin S` permit the mutual head exchange, then every one of the
`|S|(c-|S|)` cross pairs is rejected in at least one direction.  Counting
the two rejection types gives at least `mathcal D(S)`, contradicting
(3.6).  Hence a legal two-switch joins two current cycles.  The menus do
not change, so repeat until one cycle remains.  Apply Theorem 3.1.
\(\square\)

This criterion is finite when `c=O(1)`: it has only `2^c-2` nontrivial
component shores.  It is not implied merely by the component bound.

## 4. The exact regenerative history state

For `0<=K<=d`, let `U={u_i}` be exit histories and `V={v_j}` entry
histories.

### Theorem 4.1 (common-core characterization of a complete `K`-router)

The following are equivalent at the bare-history level.

1. `delta_d(u_i,v_j)<=K` for every ordered pair `(i,j)`.
2. There is one word `R in Sigma^(d-K)` such that every `u_i` ends in `R`
   and every `v_j` begins with `R`.

#### Proof

Condition 1 and (0.2) give

\[
 \operatorname{suffix}_{d-K}(u_i)
 =\operatorname{prefix}_{d-K}(v_j)
\]

for every `i,j`.  Fixing either index shows that all these words are one
common `R`.  Conversely, the common word is a suffix--prefix overlap of
length `d-K`, so every distance is at most `K`. \(\square\)

For `K=0`, every exposed exit and entry history is the same full order-`d`
state.  For fixed `K`, an order-free regenerative port must therefore retain
a literal core of length `d-O(1)`; a short checksum or scalar age label is
not enough unless a separate theorem proves it collision-free and restores
the literal word.

Theorem 4.1 characterizes a **complete** router.  One selected Hamilton
path may use different long overlaps on different joins; its weakest exact
condition remains the weighted tour (2.1).

### Definition 4.2 (full `K`-regenerative portal)

A full `K`-regenerative portal consists of:

1. the common literal core `R` of length `d-K` (or the exact per-join cores
   of one fixed tour);
2. the complete residence/age and endpoint trace state;
3. every protected upper-witness and occurrence ticket;
4. the common cap/compiler boundary signature; and
5. private guarded macros of charge at most `K` for the declared joins.

The first item is necessary from history.  The other items are necessary
because history-compatible connectors can still be physically incompatible.

## 5. Sharp obstructions

### Proposition 5.1 (two components can cost `d`)

Let `x,y in Sigma` be distinct.  Take one component whose only exposed exit
history is `x^d` and another whose only entry history is `y^d`.  Then

\[
                         \operatorname{ov}(x^d,y^d)=0,
 \qquad \delta_d(x^d,y^d)=d.
\tag{5.1}
\]

Thus a linear splice of these two fixed ports needs at least `d` appended
letters.  A bare cyclic splice using both directions costs at least `2d`.

This proves sharply that `c=2` does not imply an `O(1)` sidecar.

### Proposition 5.2 (history equality does not imply guard compatibility)

Take two full states with the same literal history `u`, but with cap flag
zero and cap flag one.  Suppose every allowed transition preserves the cap
flag.  The bare history distance is zero, yet no guarded connector exists:

\[
                         \gamma=\infty.
\]

Hence the regenerative state must contain the full boundary guard
signature, not only the last `d` letters.

### Proposition 5.3 (individual connectors need not compose)

Take two components and suppose both cross connectors are individually
legal but each consumes the same capacity-one token.  A cyclic fusion needs
both connectors and is infeasible.  The individual compatibility digraph is
a directed two-cycle, but the joint product has no feasible cycle.

Therefore Theorems 2.1 and 3.1 require product separability or a full joint
state.  Pairwise connector legality alone is not a proof.

## 6. Compiler and terminal repair after fusion

Suppose a pre-fusion physicalization has length `B(k)+s`.  After an accepted
fusion or overlap tour, let:

* `Gamma` be its additional position charge (`0`, `Gamma_lin`, or
  `Gamma_cyc`);
* `D_comp` be a **complete** compiler damage set in the final state;
* `M_0` be a reference compiler matching;
* `h` be the number of new hard tasks installed on pairwise distinct
  certified cells outside `D_comp`; and
* `H` be every remaining noncompiler target hole, with terminal repair
  complexity `R(H)`.

Put

\[
                         b=|D_{\rm comp}\cap C(M_0)|.
\tag{6.1}
\]

### Theorem 6.1 (bounded fusion-to-word charge)

If all carrier gates not listed in `H` survive in the final chronology,
then

\[
 \boxed{
 \nu(k)\le B(k)+s+\Gamma+b+h+R(H).}
\tag{6.2}
\]

#### Proof

The accepted fusion gives the final chronology with additional charge
`Gamma`.  Apply the bounded compiler-eviction theorem: install the `h` new
tasks and delete from `M_0` every matched cell in the complete damage set
or used as a new task cell.  At most `b+h` old lower targets become
casualties.  Append those casualties and a shortest repair word for `H`.
Appending destroys no existing interval witness. \(\square\)

The final compiler may be recomputed after fusion; it need not be common to
intermediate pull or hinge phases.  What must be complete is the final
damage and hole accounting in (6.2).

## 7. Consequence for the bounded-component pull rescue

The protected pull rescue gives

\[
                         c\le1+2p\lambda
\tag{7.1}
\]

for `p` wedges and pull old-phase load `lambda`.

### Corollary 7.1 (exact additive-constant interface)

Assume uniformly that:

1. `s`, `b`, `h`, and `R(H)` in (6.2) are bounded;
2. the rescued components either expose completed hinges satisfying
   Theorem 3.1, or have `Gamma_lin=O(1)` in a product-separable guarded
   atlas; and
3. every carrier gate outside the declared bounded damage state survives.

Then

\[
                         \nu(k)\le B(k)+O(1).
\]

For bounded `p,lambda`, a uniform per-join bound and Corollary 2.2 suffice.
For `p=O(d)`, a per-join constant does not suffice; one needs zero-cost
fusion of all but `O(1)` components or another globally shared reset whose
**total**, not per-component, charge is bounded.

This corollary is an exact implication, not an unconditional construction:
the current wedge and pull theorems do not yet provide the completed hinges
or full regenerative portals.

## 8. Exact frontier

The residual topology question after bounded-component rescue is no longer
just “join `c` cycles.”  It is one of the following precise objects:

\[
 \boxed{
 \begin{array}{l}
 \text{a directed Hamilton cycle in the completed-hinge compatibility
 graph,}\quad\text{or}\\[2mm]
 \text{a guarded weighted Hamilton path of total charge }O(1).
 \end{array}}
\tag{8.1}
\]

The minimal order-free literal state for the second route is the common
`(d-K)`-letter core plus the full guard signature.  The examples in Section
5 show that neither bounded component count, history equality alone, nor
individual connector feasibility can replace that state.

## 9. Dependencies

| role | file |
|---|---|
| bounded-component pull rescue and adaptive factor rank | `MATH_THEOREM_PROTECTED_FACTOR_EXCHANGE_ADAPTIVE_RANK_AND_BOUNDED_COMPONENT_RESCUE_20260804.md` |
| completed-hinge rectangles and head-permutation fusion | `MATH_THEOREM_A_PROTECTED_HINGE_INTERFACE_AND_EULER_FUSION_20260802.md` |
| exact overlap distance and two-switch expansion | `MATH_THEOREM_A_UNSATURATED_HINGE_SKELETON_DAMAGE_AND_TWO_SWITCH_EXPANSION_20260802.md` |
| bounded compiler eviction and phase decoupling | `MATH_THEOREM_BOUNDED_COMPILER_EVICTION_AND_PHASE_DECOUPLING_20260801.md` |
| terminal repair and bounded regenerative charge | `MATH_THEOREM_BOUNDED_DEFECT_REGENERATIVE_SPINE_AND_EXPLICIT_O1_CONSTANT_20260731.md` |
