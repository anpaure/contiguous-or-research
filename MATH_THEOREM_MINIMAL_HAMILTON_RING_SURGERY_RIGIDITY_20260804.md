# Minimal Hamilton-cycle surgery cannot create a full common-core ring

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical rigidity theorem for the natural
one-layer endpoint surgery from a known Middle-Levels Hamilton cycle.  It
rules out that surgery as a way to evade the fixed-factor common-label
obstruction.  It does **not** rule out a deeper alternating circuit, a
jointly constructed factor, or a surgery which opens additional intermediate
vertices.

No computation or search is used.

## 0. Setting

Work in the Middle-Levels incidence graph

\[
 G=\mathrm {ML}_m
 =\binom{[2m-1]}{m-1}\longleftrightarrow
   \binom{[2m-1]}m,
 \qquad m\ge3.
\tag{0.1}
\]

Choose a disjoint decomposition

\[
 [2m-1]=B\mathbin{\dot\cup}\{b\}
             \mathbin{\dot\cup}E,
 \qquad |B|=m-2,
 \qquad E=\{a_0,\ldots,a_{m-1}\}.
\tag{0.2}
\]

Indices on the `a_i` are cyclic.  The full common-core ring has lower roots

\[
 I_i=B+a_i,
\tag{0.3}
\]

and upper owners

\[
 L_i=B+b+a_i,
 \qquad
 R_i=B+a_{i-1}+a_i.
\tag{0.4}
\]

Its two phases are

\[
 P^- =\{I_iL_i,I_iR_i: i\in\mathbb Z_m\},
\tag{0.5}
\]

and

\[
 P^+ =\{I_iL_i,I_iR_{i+1}: i\in\mathbb Z_m\}.
\tag{0.6}
\]

Both phases have the same degree vector: every `I_i` has degree two and
every member of

\[
 Y=\{L_i,R_i:i\in\mathbb Z_m\}
\tag{0.7}
\]

has degree one.

Fix an arbitrary Hamilton cycle `C` of `G`.  The following is the most
economical endpoint surgery which could try to install either phase `P`.

1. Delete the two `C`-edges at every root `I_i`.
2. Add all edges of `P`.
3. If `y in Y` lost no edge in step 1, delete exactly one of its two old
   `C`-edges.  If it lost one edge, delete no additional edge.  If it lost
   two edges, regard it as having one unit of upper deficit.
4. Join the lower endpoints exposed in step 3 to all upper deficits by a
   simple incidence matching `Q`.

The last step is the unique one-layer degree repair: it introduces no new
intermediate vertex and changes no additional old `C`-edge.

## 1. Exact endpoint ledger

For `y in Y`, let

\[
 t(y)=|E_C(y,\{I_0,\ldots,I_{m-1}\})|\in\{0,1,2\}.
\tag{1.1}
\]

Only an `R_i` can have `t(y)=2`, because `L_i` has only the one ring-root
neighbour `I_i`.

After steps 1--3, a ring owner has degree

\[
 \begin{array}{c|ccc}
 t(y)&0&1&2\\ \hline
 \text{degree before }Q&2&2&1.
 \end{array}
\tag{1.2}
\]

Thus every unhit ring owner `y` with `t(y)=0` contributes one lower deficit
`z_y`, obtained by deleting one edge `yz_y` of `C`.  The upper deficits are

* every non-ring upper endpoint of a deleted root edge, with its literal
  multiplicity; and
* one copy of every ring owner with `t(y)=2`.

The two total deficit masses agree.

### Lemma 1.1 (deficit equality)

Let

\[
 n_j=|\{y\in Y:t(y)=j\}|,
\]

and let `e_out` be the number of root incidences of `C` whose upper endpoint
does not lie in `Y`.  Then

\[
 2m=n_1+2n_2+e_{\rm out}
\tag{1.3}
\]

and

\[
 \boxed{n_0=e_{\rm out}+n_2.}
\tag{1.4}
\]

#### Proof

There are exactly `2m` cycle incidences at the `m` roots, which gives
(1.3).  Since `n_0+n_1+n_2=|Y|=2m`, subtraction gives (1.4).  The left side
is the lower-deficit mass and the right side is the upper-deficit mass.
\(\square\)

## 2. Every unhit-owner endpoint is isolated from the upper deficits

For an upper set `U=B+x+y`, call `{x,y}` its **external pair**.  Every upper
neighbour of a ring root has this form, with one of `x,y` equal to the root
label `a_i`.

### Lemma 2.1 (one-layer isolation)

Let `y in Y` satisfy `t(y)=0`, and let `z_y` be either lower neighbour of
`y` on `C`.  Then `z_y` is adjacent to no upper deficit in the ledger of
Section 1.

#### Proof

First suppose the deleted coordinate in `y z_y` lies in `B`.  Then

\[
 z_y=(B-c)\cup e(y),
 \qquad c\in B,
\tag{2.1}
\]

where `e(y)` is the two-element external pair of `y`.  If

\[
 z_y\subseteq U=B+x+x'
\tag{2.2}
\]

for a rank-`m` upper set `U`, then the two external pairs have the same
cardinality and (2.2) forces

\[
 \{x,x'\}=e(y).
\tag{2.3}
\]

Hence `U=y`.  But an unhit ring owner is not an upper deficit: step 3
removes one old edge precisely to cancel the one new ring edge.

It remains to consider deletion of an external coordinate.

* If `y=L_i=B+b+a_i`, deleting `b` gives `I_i`; the edge `L_iI_i` would
  make `t(y)>0`, contrary to the hypothesis.  Deleting `a_i` gives
  `B+b`.  An upper neighbour of a ring root contains `B+b` only when it is
  `L_j=B+b+a_j`, a ring owner.  Such an owner has `t<=1`, so it is never an
  upper deficit.
* If `y=R_i=B+a_{i-1}+a_i`, deleting either external coordinate gives
  `I_i` or `I_{i-1}`.  Again the deleted cycle edge would make `t(y)>0`.

Thus no possible `z_y` meets an upper deficit. \(\square\)

The statement is occurrence-level: multiplicity at a double-hit upper
owner does not help, because the lower endpoint has no incidence to that
owner at all.

## 3. Rigidity theorem

### Theorem 3.1 (minimal ring-surgery rigidity)

The one-layer endpoint surgery of Section 0 admits a degree-restoring
matching `Q` if and only if the original Hamilton cycle `C` already contains
one of the two complete ring phases `P^-` or `P^+`.

When this happens `Q` is empty.

#### Proof

If some ring owner is unhit, then `n_0>0`.  It contributes a lower-deficit
endpoint `z_y`, and Lemma 2.1 says that this endpoint has no neighbour among
the upper deficits.  No degree-restoring matching exists.  Therefore

\[
 n_0=0.
\tag{3.1}
\]

By (1.4), `e_out=n_2=0`.  Hence every ring owner is incident with exactly
one root edge of `C`, and every root edge of `C` ends at a ring owner.

The owner `L_i` has only one neighbour among the ring roots, namely `I_i`,
so every edge `I_iL_i` belongs to `C`.  Each root now has one remaining
cycle edge, and every `R_i` must be used exactly once.  The bipartite
incidence graph between the roots `I_i` and owners `R_i` is the cycle

\[
 I_0,R_1,I_1,R_2,\ldots,I_{m-1},R_0,I_0.
\tag{3.2}
\]

It has exactly two perfect matchings.  They are

\[
 \{I_iR_i:i\in\mathbb Z_m\}
 \quad\text{and}\quad
 \{I_iR_{i+1}:i\in\mathbb Z_m\}.
\tag{3.3}
\]

Together with the forced `I_iL_i` edges, these are exactly `P^-` and
`P^+`.  No deficits remain, so `Q` is empty.

Conversely, if `C` contains either phase, step 1 deletes exactly that phase
at the roots and step 2 restores it.  Every ring owner loses and regains one
edge, there are no further cuts, and the empty matching completes the
surgery. \(\square\)

### Corollary 3.2 (the known-Hamilton shortcut collapses)

Starting with an arbitrary known Middle-Levels Hamilton cycle and performing
only the minimum degree repair cannot manufacture a full common-history
ring.  The surgery succeeds precisely on the already solved face where the
Hamilton cycle contains the old or rethreaded ring phase in full.

Thus the full-size ring cannot be installed by:

\[
 \text{root cuts}+\text{one cut per unhit owner}
   +\text{one direct endpoint matching}.
\tag{3.4}
\]

Any genuinely new noncanonical construction must do at least one of:

1. open additional intermediate vertices and use a longer alternating
   circuit;
2. change the common-core ring owners themselves while transporting the
   witness bank;
3. construct the factor and ring simultaneously rather than repairing a
   frozen Hamilton cycle; or
4. replace literal ring containment by a proved transparent macro.

## 4. Why a longer circuit can escape

Lemma 2.1 is a one-layer obstruction, not a conserved invariant.  If an
extra old edge is opened at an intermediate upper owner, an endpoint
`(B-c)+e(y)` can first move to another lower endpoint and change its external
pair before reaching a root-created upper deficit.  Equivalently, a longer
alternating circuit can transport the pair label through a sequence of
Boolean diamonds.

The theorem therefore identifies the exact missing resource in a
noncanonical route: **external-pair transport**.  Canonical edge-disjoint
pulls have too little local wedge aperture; minimum Hamilton surgery has
zero external-pair transport; a successful joint theorem must provide a
protected transport network whose terminal pair permutation is the ring's
Hamilton predecessor cycle and whose residual factor quotient remains
connected or root-covered.

## 5. Self-audit

The proof uses only the following literal checks.

1. `|Y|=2m` and there are `2m` root incidences in a cycle.
2. A ring owner hit `t` times has degree `3-t` immediately after root
   deletion and ring insertion.
3. If a core-deleted lower endpoint `(B-c)+{x,y}` lies below an upper
   `B+{u,v}`, equality of the two external-pair sizes forces
   `{x,y}={u,v}`.
4. `B+b` lies below a root-neighbour upper only on the owner `L_i` face,
   which cannot have double root incidence.
5. The root--`R` incidence graph is one even cycle and has exactly its two
   alternating perfect matchings.

No claim is made about a surgery with extra intermediate cuts, the full
protected reservoir, arbitrary-width upper witnesses, residence, or the
common cap.

## 6. Dependencies

| role | file |
|---|---|
| common-history ring identities | `MATH_THEOREM_CYCLIC_COMMON_HISTORY_HINGE_RING_AND_SHORT_DECK_INVARIANCE_20260804.md` |
| fixed-factor canonical-pull obstruction | `MATH_THEOREM_FACTOR_FIRST_COMMON_CORE_CANONICAL_PULL_PHASE_COVER_AND_LOCAL_WEDGE_OBSTRUCTION_20260804.md` |
| rooted factor/topology criterion | `MATH_THEOREM_COMMON_CORE_ROOTED_PULL_TRANSVERSAL_AND_FIXED_MATCHING_OBSTRUCTION_20260804.md` |

