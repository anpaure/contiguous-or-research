# DERF rooted packets: the transfer minor, a strict five-edge escape, and the fixed-`Q` obstruction

Date: 2026-07-31  
Status: exact all-finite-graph exchange theorem; exact strict packet on the
authenticated `n=3` structural parent; exhaustive fixed-`Q` census on that
parent.  No all-parameter bounded-packet supply theorem is claimed.

## 0. Verdict

The direct edgewise recursion has two different exchange languages.

* At fixed `Q`, every palette-preserving representative change is a union
  of matching-alternating **cycles**.
* When `Q` changes, the two representative differences also contain
  alternating **paths** whose endpoints are exactly the changed tail and
  head punctures.

For either language, the rooted graphic row has one exact certificate.  If
the packet removes `t` edges of a rooted tree and inserts `t`, then its
fundamental-cut transfer matrix `K` is nonsingular if and only if the new
support is again a rooted tree.  More precisely,

\[
 t-\operatorname{rank}K
   =\beta(T')=\kappa(T')-1.                              \tag{0.1}
\]

This is the correct packet-level replacement for ordinary one-edge basis
exchange.

There is an exact positive actuator on the authenticated structural
`n=3` parent.  Starting from the chained state with retained child edge
`q=11`, exchange `e=5 in Q` with `f=11 notin Q`.  One upper and one lower
direct representative are redirected, while the seam/central block changes
three edges.  Exactly five old physical edges are replaced by five new
ones:

```text
old: 15-23, 30-142, 135-149, 150-198, 197-212
new: 15-30, 23-135, 142-150, 149-197, 198-212.          (0.2)
```

Both endpoints are literal strict DERF forests with exact palettes, rooted
side supports, 56 physical edges on 70 owners and 14 components.  The lower
direct map changes `4->21` to `4->22`; the upper map changes `7->31` to
`14->31`.  Thus (0.2) is a genuine bounded **augmenting** packet which
changes the lower-shore representative state.  Five is the minimum number
of old/new occurrence-labelled structural selections for a one-element
`Q` exchange; in this fixture all ten displayed physical edges are
distinct.

The corresponding fixed-`Q` circuit hope is nevertheless false already on
this first structural base.  Exhausting all direct occurrences on all four
strict common bases gives full joint states only for retained edges `5` and
`11`, and the lower palette permutation is unique on each such fixed-`Q`
face.  A genuine rooted upper `C6` exists on retained edge `1`, but every
rooted lower completion leaves contracted cycle rank `1` or `4`.  Therefore
no accepted-to-accepted fixed-`Q` direct packet changes the lower
permutation on this fixture.  The minimum escape is precisely to admit
puncture-changing alternating paths such as (0.2), or to change the
structural parent.

Finally, the new independent-filler theorem changes the recursive
quantifier.  The structural parent `F` supplies `Q`, direct occurrences,
seams and the three-sector topology, while an arbitrary Catalan forest `G`
may independently occupy the isolated `c`-rail.  Every packet in this note
acts only on `F`; it is automatically transparent to `c+G`.  Thus the
fixed-parent census below is not an immutable-c-rail obstruction, and an
all-parameter theorem may choose `F` for packet supply and `G` for guarded
residence/shadow state.

## 1. Direct occurrence states

Let `F` be an oriented Catalan linear forest at parameter `n`.  Write a
child atom as

\[
 q=(L_q,U_q,t_q,h_q),\qquad
 L_q=t_q\cap h_q,\quad U_q=t_q\cup h_q.                \tag{1.1}
\]

The strict upper occurrence `q up x` exists only for `x notin U_q` and has
palette endpoints and physical edge

\[
 (L_q+x,U_q+x),\qquad \{t_q+x,h_q+x\}.                \tag{1.2}
\]

The strict lower occurrence `q down x` exists only for `x in L_q` and has

\[
 (L_q-x,U_q-x),\qquad \{t_q-x,h_q-x\}.                \tag{1.3}
\]

Fix a common bank `Q`.  Put

\[
 D^-(Q)=X\setminus T(Q),\qquad
 D^+(Q)=X\setminus H(Q),                              \tag{1.4}
\]

where `X` is the rank-`n` middle layer.  A strict state consists of a
perfect occurrence matching `M^-` between the upper outer palette and
`D^-(Q)`, and a perfect occurrence matching `M^+` between the lower outer
palette and `D^+(Q)`, together with the physical cap and graphic rows.

Occurrence labels matter.  Parallel occurrences may have the same two
palette endpoints, and may even have the same undirected physical edge.
Every assertion below is made first on occurrence-labelled matchings and
then replayed on the physical multigraph.

## 2. Exact cycle/path normal form

### Theorem 2.1 (fixed-`Q` circuit normal form)

Fix `Q` and one direct shore.  If `M,M'` are two exact occurrence
matchings on the prescribed palette banks, then

\[
                         M\mathbin\triangle M'          \tag{2.1}
\]

is a vertex-disjoint union of occurrence-labelled alternating even cycles.
Conversely, toggling any vertex-disjoint family of `M`-alternating cycles
gives another exact matching on the same two palette banks.

#### Proof

In the symmetric difference, every palette vertex has degree zero or two:
it is matched once in both states, and a common occurrence cancels.  Hence
every nonempty component is an even cycle alternating between old and new
occurrences.  Toggling such cycles again leaves degree one at every palette
vertex. `square`

Contracting the edges of `M`, a nonmatching occurrence from the left
endpoint of matched edge `i` to the right endpoint of matched edge `j`
becomes an arc `i->j`.  The cycles in Theorem 2.1 are exactly the directed
cycles of this exchange digraph.  A `C_(2s)` composes the representative
bijection with an `s`-cycle.

### Theorem 2.2 (`Q`-changing augmenting normal form)

Let `(Q,M^-,M^+)` and `(Q',M'^-,M'^+)` be two exact direct incidence
states, with

\[
 A=Q\setminus Q',\qquad B=Q'\setminus Q,\qquad |A|=|B|=s. \tag{2.2}
\]

Then the upper symmetric difference is a disjoint union of alternating
cycles and exactly `s` alternating paths whose endpoint set is

\[
                         T(A)\sqcup T(B).              \tag{2.3}
\]

The lower symmetric difference has the analogous path endpoint set

\[
                         H(A)\sqcup H(B).              \tag{2.4}
\]

Before physical identification and cancellation, the occurrence-labelled
structural old and new selection lists each contain at least `5s` entries.
Equality in this list count holds exactly when both shores use `s`
length-two alternating paths and there are no matching cycles.  Distinct
physical support of the listed entries is a separate literal check.

#### Proof

Every outer-palette vertex is matched in both states, so it has degree zero
or two after cancellation.  A middle vertex surviving in both punctured
banks has the same property.  A vertex in `T(A)` is matched only in the old
upper state, while one in `T(B)` is matched only in the new state.  These
are exactly the degree-one vertices, so they are paired by `s` alternating
paths.  The head/lower statement is identical.

For each exchanged child edge, the old structural block loses either two
seams or one central edge and the new block gains the complementary three
edges.  Thus the `Q`/central block contributes `3s` old and `3s` new edges.
Each of the two shore path systems contributes at least `s` old and `s`
new occurrence entries.  This proves the occurrence-labelled lower bound
and its equality case.  It does not identify parallel physical images.
`square`

Theorems 2.1 and 2.2 are complete move languages for the palette rows.
They do not imply physical capacity or graphic legality.

### Lemma 2.3 (ordinary one-edge exchange is sterile)

If `M-a+b` is again a perfect matching on the same two palette banks, then
`b` joins the same two palette vertices exposed by deleting `a`.  Hence it
is `a`, or a parallel occurrence which leaves the representative
permutation unchanged.

#### Proof

Deleting `a` leaves precisely its two endpoints unmatched.  One inserted
edge can restore degree one everywhere only by joining those endpoints.
`square`

Thus every nontrivial fixed-`Q` permutation repair is genuinely
packet-level.

## 3. Rooted graphic transfer

Let `S` be one selected physical side forest, let `A_0` be its anchor bank,
and choose one root edge `rho-a` into each side component.  By the rooted
tree lemma,

\[
                       T=S\cup R_\rho                 \tag{3.1}
\]

is a spanning tree, and such an `R_rho` exists exactly when every component
of `S` contains an anchor.

### Theorem 3.1 (rooted packet transfer matrix)

Let `T` be a spanning tree.  After cancelling common edges, let a packet
remove `Abar subset E(T)` and insert an equal-size labelled multiset
`Bbar`, with

\[
                         |Abar|=|Bbar|=t.              \tag{3.2}
\]

If the chosen root star changes from `R_0` to `R_1`, include
`R_0-R_1` in `Abar` and `R_1-R_0` in `Bbar`.  Orient `T` arbitrarily.  For
`a in Abar,b in Bbar`, let

\[
 K_{a,b}\in\{-1,0,1\}                                \tag{3.3}
\]

be the signed coefficient of `a` on the unique oriented `T`-path joining
the endpoints of `b`.  Put

\[
                         T'=T-Abar+Bbar.               \tag{3.4}
\]

The following are equivalent.

1. `T'` is a spanning tree.
2. After contracting every component of `T-Abar`, the `Bbar` multigraph is
   loopless and is a tree on the resulting `t+1` vertices.
3. `det K=+1` or `-1`.
4. The packet admits an ordering of ordinary fundamental graphic pivots
   from `T` to `T'` (although the palette packet itself need not be legal
   at any proper prefix).

Moreover, over `F_2` or over the rationals,

\[
 t-\operatorname{rank}K
   =\beta(T')=\kappa(T')-1.                           \tag{3.5}
\]

#### Proof

Deleting `t` tree edges gives `t+1` components.  The columns of `K` are
the incidence vectors, in the fundamental-cut basis, of the inserted
edges on this quotient.  Their rank is therefore the graphic rank gained
by `Bbar`.  Hence the quotient has

\[
       \kappa(T')=t+1-\operatorname{rank}K.            \tag{3.6}
\]

Since `T'` has `|V(T)|-1` edges, its cycle rank equals its number of
components minus one, proving (3.5) and the equivalence of (1)--(2).

Alternatively delete one row from the oriented vertex-edge incidence
matrix.  The columns of `T` form a unimodular basis; expressing every new
edge in that basis gives its signed path vector.  Replacing the columns
`Abar` by `Bbar` changes the basis determinant by `det K`.  Network
matrices are totally unimodular, so the new columns form a tree basis
exactly when `det K=+-1`.  This proves (3).

If the target is a tree, the fundamental cycle of some still-new target
edge must contain a still-old edge; otherwise that cycle would lie in the
target tree.  Pivot and induct.  This proves (4); its converse is immediate.
`square`

If root edges may be reselected rather than fixed, the equivalent flexible
test is simpler: the terminal side support is a forest and every one of its
components meets the terminal anchor bank.  One then chooses one root edge
per component.

### Corollary 3.2 (complete structural packet test)

A direct circuit/augmenting packet is a legal structural DERF packet if
and only if all of the following hold.

1. Every new occurrence is authenticated in the appropriate strict
   `q up x` or `q down x` catalogue, and Theorem 2.1 or 2.2 holds.
2. The literal degree, anchor and (when frozen) directed tail/head ledgers
   satisfy

   \[
        d'(v)=d(v)-d_{old}(v)+d_{new}(v)               \tag{3.7}
   \]

   and their prescribed caps.
3. Each required rooted side row passes Theorem 3.1, or its flexible-root
   version.
4. After deleting the old packet from the complete structural support, the
   new packet is loopless and graphic-independent on the component
   quotient.  Equivalently, the contracted attachment graph `Gamma` is a
   forest.

#### Proof

Theorems 2.1--2.2 give exactly the palette rows.  Equation (3.7) is the
literal capacity row.  Theorem 3.1 gives the rooted side rows.  Finally,
adding edges to a residual forest creates a cycle exactly when their images
after component contraction contain a loop or a cycle.  These are all the
central strict conditions. `square`

For an edited shore whose old/new double-anchor matchings are `Pi,Pi'`,
let `H` contain the other shore, the central relation, and
`Pi intersection Pi'`.  Then the exact topology delta is

\[
 \beta(H\cup\Pi')-\beta(H\cup\Pi)
 =\rho_H(\Pi\setminus\Pi')-\rho_H(\Pi'\setminus\Pi),  \tag{3.8}
\]

where `rho_H(E)` is the graphic-rank gain from `E`.  Thus the rooted-side
minor and the joint-`Gamma` minor are separate tests.

## 4. Two exact bounded packets at `n=3`

Use the authenticated child paths

```text
19-49,
13-28,
37-35-42-14-22-50-56-25-11-7-21-52-44-41,
38,
26.                                                    (4.1)
```

Child edges are indexed in this order.

### 4.1 A genuine rooted direct `C6`, but no joint completion

Retain child edge `1` and put every other child edge in `Q`.  On the strict
upper shore, the rooted direct selections

```text
A = {4,5,11,16,17,18},
B = {5,6,9,17,18,19}                                  (4.2)
```

refer to the occurrence IDs in the frozen direct catalogue.  Their old
and new palette halves are

```text
old: (41,47), (38,62), (26,59)
new: (38,47), (26,62), (41,59),                       (4.3)
```

with `(49,55),(28,61),(13,31)` fixed.  Thus (4.3) is one direct
matching-alternating `C6`.  Both selections use the same nine root representatives

```text
23,27,30,39,45,53,54,57,60.                           (4.4)
```

Deleting the three old physical edges leaves four rooted-tree components;
the three new quotient edges form a tree.  No one-edge or equicardinal
two-toggle on the six-occurrence support is palette-exact.

This is not a full strict extension.  The complete direct census below
shows that the two upper palette classes have contracted cycle ranks `4`
and `1`, respectively, against every rooted lower state.  The `C6` is a
strict rooted descent `4->1`, but the residual unit cannot be closed in
this fixed-`Q` face.

It is also not an identity transition for the guarded endpoint state.  Its
changed directed rooted pairs are

```text
old: 27<-58, 45->43, 54<-46
new: 30<-58, 39->46, 57->43.                          (4.5)
```

Thus it must export a new polarity/socket signature.

### 4.2 The support-minimal cross-`Q` escape

Start instead with retained child edge `11` (so `5 in Q`) and make the
one-element common-bank exchange

\[
                        Q'=Q-5+11.                    \tag{4.6}
\]

The two length-two occurrence paths are

```text
upper: (7,31)  -> (14,31),
lower: (4,21) -> (4,22).                              (4.7)
```

Together with the seam/central change, their complete old/new physical
supports are exactly (0.2).  Literal replay verifies both endpoints have
exact lower and upper palettes, maximum degree two, cycle rank zero and 14
components.  Both side anchor histograms are `(c0,c1,c2)=(0,4,5)`, so both
are rooted graphic bases after choosing one terminal root per component.
In the inverse, retained-`5` to retained-`11` direction, the canonical root
stars exchange `rho-23` for `rho-30` above and `rho-5` for `rho-6` below;
both augmented side graphs are spanning trees.  Exhausting all `4*16=64`
accepted endpoint pairs proves that one changed occurrence on each shore is
minimum, with four ties.

By Theorem 2.2, any one-element `Q` change uses at least five old and five
new occurrence-labelled structural entries.  Literal replay verifies that
all ten entries in (0.2) have distinct physical images, so this packet
attains the occurrence lower bound with an honest physical `5->5`
exchange.  The `4*16` endpoint census separately proves that one changed
occurrence per shore is minimum on these two faces.  It is the first exact
escape from the fixed-`Q` lower-permutation obstruction: the changed lower
row in (4.7) is an augmenting path whose endpoints are the changed head
punctures `21,22`.

## 5. Exhaustive fixed-`Q` obstruction on the same parent

The independent audit generates only literal occurrences (1.2)--(1.3),
then exhausts all occurrence-labelled perfect matchings for the four
strict common bases `E-{r}` with

\[
                         r\in\{0,1,5,11\}.            \tag{5.1}
\]

A rooted-valid side must pass tail and head injectivity, anchor capacity,
maximum degree two, side acyclicity, `c0=0`, and the root-star spanning-tree
test.  Every rooted minus/plus product is tested in contracted `Gamma`; each
`beta=0` product is then replayed as all 56 ambient edges on all 70 owners.

The complete counts are

\[
\begin{array}{c|rr|rr|r|r}
 r&\text{raw }M^-&\text{raw }M^+&\text{rooted }M^-&
 \text{rooted }M^+&\text{joint }\beta=0&
 \#\text{ lower permutations in joint states}\ \\ \hline
 0 & 8&4&4&0&0&0\\
 1 &16&8&8&4&0&0\\
 5 & 8&4&6&2&4&1\\
11 & 8&4&8&4&16&1.
\end{array}                                            \tag{5.2}
\]

At `r=1`, all 32 rooted products have positive cycle rank, with histogram

\[
                         1^{16},4^{16}.                \tag{5.3}
\]

At `r=5,11`, all multiplicity in the lower accepted states comes from
reverse-parallel occurrence labels on one fixed palette/physical matching.
Consequently:

> **Fixed-`Q` obstruction.**  On the authenticated oriented `n=3`
> structural parent, no accepted-to-accepted strict direct packet changes
> the lower-shore palette permutation within any common-basis fibre.

This is exhaustive for (4.1) and the four bases (5.1).  It is not a claim
for another child orientation, another structural parent, a packet changing
`Q`, or `n>=4`.  In particular, (4.6)--(4.7) is an explicit positive
`Q`-changing escape.

### 5.1 Why the tempting synchronized `C6 x C8` is outside DERF

The unrestricted containment packet on retained edge `0` has the attractive
cycle-rank ledger `0,1,1,0`; both compound endpoints replay as literal
70-owner, 56-edge, 14-path Catalan forests.  It nevertheless fails the
first condition of Corollary 3.2.  The new upper pair

```text
(38,55)
```

is no `q up x` occurrence of (4.1), and the lower pairs

```text
(4,13), (32,49)
```

are no `q down x` occurrences.  The packet is therefore an unrestricted
collar calibration, not a DERF circuit.

## 6. No abstract bounded-basis theorem

### Proposition 6.1 (unbounded rooted circuit support)

For every `ell>=2` there is a palette-matching/rooted-graphic instance with
two rooted feasible states such that its only nontrivial palette packet has
half-support `ell`.

#### Proof

Take the occurrence graph `C_(2ell)`.  It has exactly its two alternating
perfect matchings `M,M'`.  Map their occurrences alternately to the physical
cycle

\[
 p_0p_1p_2\cdots p_{2\ell-1}p_0,                     \tag{6.1}
\]

so `M` maps to `p_(2i)p_(2i+1)` and `M'` to
`p_(2i+1)p_(2i+2)`, cyclically.  Declare every even vertex `p_(2i)` an
anchor and use the same root star `rho-p_(2i)` in both states.  Each selected
physical edge contains exactly one anchor, so both matching-plus-star
graphs are spanning trees and all anchor side degrees are one.  But the
occurrence cycle has no chord and no third perfect matching; the only
nontrivial move toggles all `ell` old occurrences. `square`

This is an abstract matching/graphic instance, not a Boolean direct
counterexample.  It proves that exact palettes plus the rooted invariant
alone cannot yield a dimension-independent bounded circuit basis.  The
missing Boolean theorem must supply short direct alternating cycles/paths
whose degree rows pass and whose relevant network minors are nonsingular.

### Proposition 6.2 (smallest rooted failure)

Already on occurrence `K_(2,2)`, map one matching to physical edges
`12,34`, the other to `13,24`, and take root edges `rho-1,rho-3`.  The old
state is a rooted tree.  The new state has an anchor-free component `{2,4}`
and a rooted triangle on `{rho,1,3}`.  Its transfer matrix is

\[
                         \begin{pmatrix}0&1\\0&1\end{pmatrix},    \tag{6.2}
\]

of rank one, so (3.5) gives `beta=kappa-1=1`.  This is the minimum abstract
root obstruction because a nontrivial simple matching difference has at
least two old edges.

## 7. Independent filler and guarded scope

Let `F` be the structural parent used above and let `G` be any Catalan
forest at the same parameter.  The independent-filler theorem places
`c+G` on a middle-vertex bank disjoint from every strict side, seam and
`z`-rail edge.  Therefore:

### Corollary 7.1 (filler-transparent packet)

Every structural packet satisfying Corollary 3.2 for `F` remains palette-
and topology-valid after adjoining `c+G`.  The packet changes no coordinate
trace, deep-shadow witness or compiler cell wholly owned inside `c+G`.

#### Proof

The palettes and physical support are direct sums.  The packet has empty
support on the `c`-rail, so both the selected edge set and every rail-
internal literal window remain unchanged. `square`

This removes `G`-owned body guards from the packet boundary state.  It does
not make a structural packet guardedly transparent.  On the three-sector
support one must still carry:

* residual undirected and directed endpoint capacities;
* the component partitions for both rooted side minors and `Gamma`;
* exposed endpoint labels, orientation pins and capped run records;
* every changed structural shadow window or compiler cell; and
* the parent socket/mark signature.

### Proposition 7.2 (SBE is an endpoint-orientation Boolean cut system)

Fix the undirected structural forest `F`.  Its two direct occurrence
multigraphs, including palette labels and undirected physical images, do
not depend on the coherent orientation of its path components.  Write

\[
 N={2n\choose n-1},\quad P={2n\choose n-2},\quad
 C=\operatorname{Cat}_{n+1},\quad R=N-C=P-\operatorname{Cat}_n.   \tag{7.0}
\]

Let `Z_0`
be the isolated child vertices.  For every nontrivial child path `P_i` with
endpoints `a_i,b_i`, let a bit `epsilon_i` choose the upper terminal
`z_i^-(epsilon_i)`; the lower terminal `z_i^+(epsilon_i)` is the opposite
endpoint.

For either shore `sigma`, an outer family `U` with fixed occurrence
neighbour bank `N_sigma(U)` satisfies strict balanced expansion exactly
when

\[
 \sum_i \mathbf 1\{z_i^\sigma(\epsilon_i)\in N_\sigma(U)\}
 \ge
 \left\lceil {N|U|-R|N_\sigma(U)|\over N-R}\right\rceil
 -|Z_0\cap N_\sigma(U)|.                              \tag{7.1}
\]

Consequently two-shore SBE is precisely the conjunction of the upper and
lower Boolean cuts (7.1).  It is independent of the later choice of `Q`.
In particular, every fixed-`F`, fixed-orientation circuit or augmenting
packet of Sections 2--4 preserves the **current parent's** SBE certificate;
changing `Q` cannot repair an orientation which violates (7.1).  This says
nothing about SBE of the output child, whose path endpoints and Boolean cut
system must be rebuilt.

#### Proof

The direct occurrence definitions (1.2)--(1.3) use only the unordered
child edge through `L_q,U_q` and its unordered physical image.  Orienting
a path removes exactly its terminal vertex from the tail image and exactly
its initial, opposite endpoint from the head image.  Thus the terminal
bank on shore `sigma` is

\[
             Z^\sigma=Z_0\cup\{z_i^\sigma(\epsilon_i):i\}.        \tag{7.2}
\]

The SBE weight is one on `Z^sigma` and `R/N` on its complement.  Therefore

\[
 |U|\le {R\over N}|N_\sigma(U)|
       +{N-R\over N}|N_\sigma(U)\cap Z^\sigma|.       \tag{7.3}
\]

Multiplication by `N`, separation of the fixed isolated contribution and
integer rounding give (7.1).  Neither the occurrence graph nor (7.2)
contains `Q`, proving the last assertions. `square`

The exact `n=4` endpoint census has `7600` satisfying assignments among
the `2^14` orientations, and one path flip repairs the stored chained
orientation.  At `n=3` no orientation is two-shore SBE, although strict
common bases and physical extensions exist.  Hence SBE is a useful
sufficient orientation face, not a necessary incidence condition.  The
proof order is exact:

```text
choose endpoint-orientation bits satisfying (7.1)
    -> invoke SBE common-base integrality to choose Q
    -> choose/root or packet-switch the physical representatives.          (7.4)
```

The `Q` and rooted-forest stages cannot be used to conceal a failure of the
first line.

The direct upper `C6` (4.5) is an exact warning: palette and rooted-tree
success can change six root-labelled polarity ports.  A packet is a legal
node of the guarded transparent induction only after the exported endpoint
relation is accepted and every changed structural witness is preserved or
privately regenerated.

The corrected existential all-parameter target is therefore weaker than a
one-parent invariant:

> choose a structural parent `F` exporting a short direct circuit/augmenting
> atlas with simultaneous nonsingular rooted/`Gamma` minors, and independently
> choose a guarded filler `G` whose isolated rail carries the required
> residence/shadow state.

Neither factor is presently known uniformly.  The fixed-parent obstruction
in Section 5 does not obstruct this two-parent quantifier.

## 8. Reproducible finite evidence and exact boundary

The fixed-`Q` direct census and unrestricted-packet scope audit are

```text
scratch/audit_ad_derf_n3_direct_packet_census_20260731.py
scratch/ad_derf_n3_direct_packet_census_20260731.audit.json
```

They reconstruct every occurrence and physical edge rather than trusting a
catalogue claim.  At freeze time their SHA-256 values are

```text
script  44e20eff568b498370873f872dc74aa68b64caffaecf12fa8cf1ec33ec76cd4f
JSON    c0b2c3e8e6e1f82733995651ebda8c822d8f8ae2c6fc40d64e172ff06446a1a5
payload 321edd602f8704548395d6da452e81ce37a8545e164d7ccedf916fd60b3e525f.
```

The strict five-edge packet is independently reconstructed in

```text
MATH_THEOREM_THREAD_D_CATALAN_STRICT_FIVE_EDGE_PACKET_AND_MOTIF_DESCENT_20260731.md
scratch/audit_threadD_catalan_strict_five_edge_packet_n3_n5_20260731.py
scratch/threadD_catalan_strict_five_edge_packet_n3_n5_20260731.audit.json
```

and the two-parent substitution in

```text
MATH_THEOREM_CATALAN_INDEPENDENT_C_RAIL_FILLER_20260731.md
scratch/audit_catalan_independent_c_rail_filler_20260731.py
scratch/catalan_independent_c_rail_filler_20260731.audit.json.
```

The endpoint-orientation reduction and the `n=4` `7600/2^14` census are
proved and sourced in

```text
MATH_THEOREM_R_CATALAN_EDGEWISE_ROOTED_DOUBLE_RAINBOW_EAR_AND_TWO_PARENT_GATE_20260731.md.
```

The proved boundary is exact:

* rooted packet legality has the determinant/contraction certificate of
  Theorem 3.1;
* a support-minimal strict augmenting packet exists at `n=3` and changes
  the lower representative state;
* fixed-`Q` lower-permutation circuits are absent on the complete first
  structural fixture;
* no bounded packet theorem follows from abstract palette/root axioms;
* the structural packet and guarded filler may be chosen from two parents;
* uniform Boolean short-packet supply, guarded structural regeneration,
  deeper shadows and the compiler remain unproved.
