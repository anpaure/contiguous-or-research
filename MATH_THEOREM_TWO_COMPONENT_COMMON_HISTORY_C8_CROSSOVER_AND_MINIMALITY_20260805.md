# The first exact two-component source crossover is a common-history `C8`

**Date:** 2026-08-05  
**Method:** literal de Bruijn overlap, cut-permutation parity, and Boolean
set algebra; no computation or search  
**Status:** unconditional abstract crossover theorem and unconditional
minimum-support theorem on the one-copy common-history/coatom face.  A
four-hinge packet fuses two source components at zero positional charge
while preserving the owner set, both immediate palettes, the complete
strict-lower occurrence deck, and positive depth-`d` residence.  The fixed
PBBS braid and residual components cannot contain this packet without an
owner-neighbourhood replacement, by the forced-pair common-history no-go.
Arbitrary-width exterior upper witnesses, zero-gap residence, and the typed
common cap remain explicit later interfaces.

## 0. Outcome

There are two different notions of boundary cost.

1. A **bare raw reset** keeps both source circuits fixed and inserts a word
   between their terminal order-`d` states.  In the unrestricted literal
   order-`d` de Bruijn graph its exact cost is `d` minus the longest literal
   suffix--prefix overlap.  Extra owner, palette, or cap guards can only
   increase that cost.  For the rigid PBBS braid and a residual component
   the bare cost is at least `d-2`, even after arbitrary admissible
   nonmaximal thinning.  It therefore cannot be an additive-constant
   construction.
2. A **crossover** cuts existing owner roles and permutes their complete
   right continuations.  It may have charge zero because it reuses all old
   source positions.  If it is required to preserve every owner and both
   immediate palettes while joining exactly two components, then support
   two is algebraically impossible and support three has the wrong topology
   parity.  Support four is sharp.

The sharp packet is the four-role specialization of the common-history
hinge ring.  Its old cut permutation is

\[
                         \sigma=(0\ 2)(1\ 3),
\tag{0.1}
\]

and its head rethread is the `4`-cycle

\[
                         \tau=(0\ 1\ 2\ 3).
\tag{0.2}
\]

The new component permutation is

\[
                 \tau\sigma=(0\ 3\ 2\ 1),
\tag{0.3}
\]

so two components become one.  The packet is a literal source `C8`, not
merely an incidence trade.

## 1. Exact raw-reset charge

For two literal order-`d` histories

\[
 H=(h_1,\ldots,h_d),\qquad G=(g_1,\ldots,g_d),
\]

put

\[
 \operatorname {ov}(H,G)=\max\{s:\
   (h_{d-s+1},\ldots,h_d)=(g_1,\ldots,g_s)\}.
\tag{1.1}
\]

Literal equality is meant; equality merely of the unions is insufficient.

### Lemma 1.1 (reset metric)

The minimum number of appended source letters needed to move from `H` to
`G` in the order-`d` de Bruijn digraph is

\[
             \boxed{\delta_d(H,G)=d-\operatorname {ov}(H,G)}.
\tag{1.2}
\]

#### Proof

If the overlap has length `s`, append
`g_(s+1),...,g_d`.  The final state is `G`, so the right side is an upper
bound.  Conversely, after `t<d` appended letters, the first `d-t` entries
of the final state are the last `d-t` entries of `H`.  Reaching `G`
therefore forces an overlap of length at least `d-t`.  Hence
`t>=d-ov(H,G)`.  \(\square\)

The exact resident-Johnson feasibility version is also useful.  Let two
owner traces have maximal letters `P_j^(a)` and forced sets `F_j^(a)` at
aligned source positions.  For `1<=s<=d`, the short-block freedom theorem
gives a common literal block of length `s` if and only if

\[
 \boxed{
 F_j^{(1)}\cup F_j^{(2)}
       \subseteq P_j^{(1)}\cap P_j^{(2)}
       \quad(0\le j<s).}
\tag{1.3}
\]

Indeed the common letters may be the forced-set unions.  Thus, after
optimizing cuts, orientations, and admissible antecedents, the exact bare
de Bruijn reset cost is

\[
 d-s_* ,\qquad
 s_*:=\max\{s:\text{the containments (1.3) hold on an aligned
                         `s`-block}\}.
\tag{1.4}
\]

The appended transition attaining (1.4) is not asserted to satisfy a
rank-`r` owner, Johnson, q1, upper, or typed-cap condition at its
intermediate states.  Thus (1.4) is exact before those guards and is a
lower bound for any guarded raw reset.  This is the only direction needed
for the obstruction below.

### Corollary 1.2 (rigid PBBS raw cost is unbounded)

For `m>=6` and the optimal PBBS deadline `d>=3`, a rigid braid and a
residual component have

\[
                         s_*\le2,
\qquad                  \delta_d\ge d-2.
\tag{1.5}
\]

#### Proof

The local compatibility table for the rigid components has no two
consecutive compatible regular positions in the same orientation.  Across
an `A|B` transition the required phase displacement changes by two, and a
residual seam is pointwise incompatible.  With exactly one orientation
reversed, the sole possible exceptional adjacent pair uses the regular
`A` state and the terminal odd-`A` state; every third position next to that
pair is incompatible.  Hence no compatible block has length three.  Apply
(1.4).  \(\square\)

This estimate is deliberately weaker than the exact maximal-antecedent
cost `d`: it permits every nonmaximal antecedent.  It is still
`Omega(d)=Omega(sqrt(k))` and therefore rules out raw reset as an
additive-constant mechanism.

## 2. An exact abstract source-crossover criterion

Let `q>=2`.  Start with a collection of cyclic depth-`d` rank-`r` source
circuits, each of length at least `d+1`: every cyclic source interval of
width `d+1` has rank `r`.  Choose
`q` distinct cut roles, possibly several on the same component, and at role
`i` choose a literal fragment

\[
                         X_i\,\mathcal H\,Y_i,
\qquad
 \mathcal H=(H_1,\ldots,H_d),
\tag{2.1}
\]

with the **same ordered word** `mathcal H` in every role.  The cuts are just
after `mathcal H`; cutting at all of them decomposes the old circuits into
directed de Bruijn walks from the common state `mathcal H` back to that
state.  Let

\[
                         K=\bigcup_{j=1}^d H_j.
\tag{2.2}
\]

Cut at every selected role after `mathcal H`, and move the complete right
continuation beginning with `Y_i` according to a permutation
`pi in S_q`.  The only changed owner transitions are

\[
                  K\cup X_i\quad\longrightarrow\quad
                  K\cup Y_{\pi(i)}.
\tag{2.3}
\]

Write

\[
 L_i=K\cup X_i,\qquad R_i=K\cup Y_i.
\tag{2.4}
\]

### Theorem 2.1 (literal completed-hinge criterion)

The head permutation `pi` is a zero-charge owner/Johnson/q1-exact source
crossover if and only if

1. every `L_i,R_i` has rank `r`, and both every old pair `L_i,R_i` and
   every new pair `L_i,R_(pi(i))` are Johnson-adjacent;
2. the lower colours satisfy

   \[
    \{\!\{L_i\cap R_i:i\}\!\}
      =\{\!\{L_i\cap R_{\pi(i)}:i\}\!\};
   \tag{2.5}
   \]

3. the upper colours satisfy

   \[
    \{\!\{L_i\cup R_i:i\}\!\}
      =\{\!\{L_i\cup R_{\pi(i)}:i\}\!\}.
   \tag{2.6}
   \]

Under these conditions:

* the complete owner multiset is unchanged;
* the occurrence-labelled multiset of every source interval of width at
  most `d+1` is unchanged;
* in fact every strict-lower interval-OR occurrence is transported;
* every transported strict-lower compiler matching remains a matching;
* no source position is added; and
* positive owner residence is at least `d+1`, provided every resulting
  circuit has at least `d+1` source positions.

If `sigma` is the next-cut permutation of the old components, the new
factor components are exactly the cycles of

\[
                         \pi\circ\sigma.
\tag{2.7}
\]

#### Proof

The tails `L_i` and heads `R_i` are merely re-paired, so their owner
multiset is fixed.  Conditions (2.5)--(2.6) are exactly preservation of the
two immediate palettes, and item 1 is exactly the Johnson condition.

At source level, the cut pieces are walks based at the same literal
order-`d` de Bruijn vertex.  Permuting their successor pieces is an Euler
reassembly of those walks.  The common-vertex short-deck theorem therefore
gives an occurrence bijection for every source subword of width at most
`d+1`, including the owner windows.  Since every width-`d+1` interval has
rank `r`, every strict-lower interval has width at most `d`; hence the same
bijection transports the complete strict-lower occurrence deck and every
matching on it.  This rank-`r` factor hypothesis is essential to that last
unqualified statement; without it, a long low-rank exterior interval could
cross more than one selected cut.

On a resulting circuit of length at least `d+1`, every source occurrence
belongs to `d+1` consecutive owner windows.  Unions of such cyclic arcs
have no nonempty component shorter than `d+1`, so the rethread cannot create
a shorter positive run.  Finally, cutting the old edges and
following an old path to the next cut applies `sigma`; the new head
assignment applies `pi`.  Hence (2.7).  \(\square\)

For fixed resident owner traces, the common history in (2.1) is plantable
precisely when, at every history position,

\[
 \bigcup_i F_j^{(i)}\subseteq H_j
      \subseteq\bigcap_i P_j^{(i)},
\qquad 0\le j<d,
\tag{2.8}
\]

together with the two individual screen/envelope tests producing the
declared endpoint owners.  Equation (2.8) is the exact multiport extension
of the two-component forced-pair criterion; there is no additional scalar
or flow condition at the source-history row.

## 3. Why support four is the first exact two-component packet

Assume a common-history crossover with distinct rank-`r` owners in which
every old and new tail--head pair is a Johnson edge and both immediate
palettes are preserved as multisets.  This includes the one-copy
functional/coatom face used below.

### Lemma 3.1 (support two is impossible)

A nontrivial two-role head transposition cannot preserve both immediate
palettes.

#### Proof

Write the tails as `L_0,L_1` and the heads as `R_0,R_1`.  The old pairs
are `(L_0,R_0),(L_1,R_1)` and the new pairs are
`(L_0,R_1),(L_1,R_0)`.  All four are Johnson edges.

The equality of the two lower-colour multisets is realized either directly
or crosswise, and independently the same is true for the two upper-colour
multisets.  If both equalities are direct, then

\[
 L_0\cap R_0=L_0\cap R_1,
 \qquad
 L_0\cup R_0=L_0\cup R_1,
\tag{3.1}
\]

which determines `R_0=R_1`.  If both are crosswise, the analogous two
equalities with `R_0` fixed determine `L_0=L_1`.

It remains to exclude the two mixed cases.  Suppose, by symmetry, that the
lower colours match directly.  Put

\[
 I_0=L_0\cap R_0=L_0\cap R_1,
 \qquad
 I_1=L_1\cap R_0=L_1\cap R_1.
\tag{3.2}
\]

Every displayed intersection has rank `r-1`.  If (I_0\ne I_1), their union
has size at least `r`; two distinct rank-`r` sets cannot both contain that
union.  Thus `I_0=I_1=:I`, and hence

\[
 L_0=I+a,\quad L_1=I+b,\quad R_0=I+x,\quad R_1=I+y
\tag{3.3}
\]

for labels outside `I`.  Crosswise equality of the upper colours would
give, for example,

\[
 I+a+x=I+b+x,
\tag{3.4}
\]

and therefore `a=b`, so `L_0=L_1`.  The other mixed case follows by Boolean
duality: complementing every owner exchanges intersection and union while
preserving Johnson adjacency.  It again gives `L_0=L_1` (and hence a
degenerate trade).  Every case is
degenerate.  \(\square\)

### Lemma 3.2 (support three is impossible)

No exact support-three head rethread can turn exactly two old components
into one.

#### Proof

If the head permutation is a transposition, its third role is fixed.  Its
unchanged lower and upper occurrences may be subtracted from the two
multiset identities, leaving the forbidden support-two trade of Lemma 3.1.
The only remaining nontrivial possibility is a `3`-cycle, which is even.
For a permutation on `q` cut
labels,

\[
                         \operatorname {sgn}(\eta)
                  =(-1)^{q-c(\eta)},
\tag{3.2}
\]

where `c(eta)` is its number of cycles.  Changing the number of factor
components from two to one reverses this sign.  An even head permutation
cannot do so.  \(\square\)

### Corollary 3.3 (sharp support floor)

On the declared face, a zero-position, owner-exact crossover which fuses
exactly two components has support at least four.

The lower bound combines two independent facts: support two fails exact
q1 algebra, while a genuine support-three cycle fails topology.  It does not claim that every
possible noncoatom or positive-charge packet has support four.

## 4. The sharp literal `C8`

Assume `r>=3` and that the ground set has at least `r+3` coordinates.
Choose nonempty letters with

\[
 B=H_1\cup\cdots\cup H_d,
\qquad |B|=r-2,
\tag{4.1}
\]

where overlaps between the `H_j` are allowed.  Only their ordered literal
word and its union are used below.  Thus, unlike the disjoint-history
specialization, this form does not require `d<=r-2`.

and choose distinct labels

\[
                         b,a_0,a_1,a_2,a_3\notin B.
\tag{4.2}
\]

Subscripts on the `a_i` are modulo four.  Put

\[
 X_i=\{b,a_i\},\qquad
 Y_i=\{a_{i-1},a_i\},
\tag{4.3}
\]

and use the four old literal fragments

\[
                         W_i=(X_i,H_1,\ldots,H_d,Y_i).
\tag{4.4}
\]

Their tail and head owners are

\[
 L_i=B+b+a_i,
 \qquad
 R_i=B+a_{i-1}+a_i.
\tag{4.5}
\]

All eight owners are distinct rank-`r` sets.  The old edge `L_iR_i` has

\[
 I_i=B+a_i,
 \qquad
 U_i=B+b+a_{i-1}+a_i.
\tag{4.6}
\]

Now attach to `L_i` the complete right continuation formerly beginning at
`Y_(i+1)`.  The new edge is `L_iR_(i+1)`, with

\[
 L_i\cap R_{i+1}=B+a_i=I_i,
\tag{4.7}
\]

and

\[
 L_i\cup R_{i+1}=B+b+a_i+a_{i+1}=U_{i+1}.
\tag{4.8}
\]

### Theorem 4.1 (two-component common-history `C8`)

Place old ports `0,2` on one component, in that cyclic order, and old ports
`1,3` on a second component, in that cyclic order.  The cyclic head
rethread `i -> i+1`:

1. fuses the two components into one;
2. uses every old owner exactly once;
3. preserves the lower-q1 palette pointwise and permutes the upper-q1
   palette cyclically;
4. preserves the complete strict-lower occurrence deck and every
   transported strict-lower compiler matching;
5. has positive residence floor `d+1`; and
6. has positional charge zero.

#### Proof

Equations (4.5)--(4.8) verify Theorem 2.1.  The old cut permutation is
`sigma=(0 2)(1 3)` and the head permutation is
`tau=(0 1 2 3)`.  Direct composition gives (0.3), one cycle.  The remaining
claims are the source-crossover conclusions of Theorem 2.1.  \(\square\)

Together with Corollary 3.3, this proves that the literal `C8` is
support-minimal on the one-copy common-history/coatom face.

## 5. Exact long-upper interface

The theorem above is not an arbitrary-exterior upper theorem.  Every old
occurrence which is not transported must cross a changed cut and must have
width at least `d+2`.  Moreover its value contains the old rank-`(r+1)`
hinge union `U_i` for at least one crossed hinge.  Hence the complete
possible old-value damage universe is contained
in

\[
 \mathcal A=\bigcup_{i=0}^3
       \{Z:U_i\subseteq Z\subseteq[k]\},
\tag{5.1}
\]

and

\[
                         |\mathcal A|
                     \le4\,2^{k-r-1}.
\tag{5.2}
\]

This is localization, not a bounded casualty theorem.  A protected
alternative-witness bank, a correlated exterior permutation, or a later
opening theorem must handle (5.1).  Zero-gap residence and any typed cap
route carrying data beyond the literal short cell are also separate.

To justify the cone claim, widths at most `d+1` are transported by Theorem
2.1.  For a longer interval crossing cut `i`, suppose first that its left
endpoint lies inside the common history.  The identical suffix of
`mathcal H` moves with the complete right continuation until the interval
ends or reaches another selected cut.  In the former case the interval is
transported.  In the latter case it traverses a full fragment
`X_j mathcal H Y_j` at that later cut `j`.  If instead its left endpoint is
at or before `X_i`, it already traverses the full fragment at `i`.  Thus
every untransported old interval contains some `X_j mathcal H Y_j`, whose
union is `U_j`; this proves (5.1).  Notice that this localizes values, not
physical occurrences or the number of targets that actually lose all
witnesses.

## 6. Consequence for the rigid PBBS endpoint

### Theorem 6.1 (unmodified rigid ports cannot host the `C8`)

No packet of the form in Theorem 4.1 can use unchanged old hinge
neighbourhoods from both the terminal rigid braid and a residual component.

#### Proof

All four old roles in (4.4) contain the same literal order-`d` history
`(H_1,...,H_d)`.  In particular, any braid role and any residual role would
give antecedents of the two fixed owner traces with a common length-`d`
history.  The rigid forced-pair common-history no-go excludes this for every
choice of cuts, orientations, and nonmaximal antecedents.  \(\square\)

Thus the `C8` is an exact crossover but not a decoration which can simply
be stamped onto the already frozen rigid factor.  At least one old
owner-neighbourhood must be replaced prospectively.  The split-core pivot
is relevant precisely because it supplies a literal owner-simple Johnson
collar and a controllable incoming/outgoing source state; what remains is
to embed four compatible hinge ports (or an equivalent compound endpoint)
while retaining the PBBS owner/palette resources.

There is also a sharp warning about using only one canonical split-core
pivot against one unchanged PBBS endpoint.  In its displayed output rail,
all but the first of the `d` source-state letters are rho singletons.  Every
braid and residual forced set has two distinct coordinates in the range
`m>=6,d<=m-3`.  Hence an unchanged PBBS antecedent letter cannot equal any
of those singleton state letters.  A one-pivot/common-vertex splice using
that canonical output rail is therefore impossible.  Either both shores
must be reset, the pivot rail must be generalized by legal enlargement, or
the four-hinge crossover must be planted directly.

This singleton observation is a no-go only for the displayed canonical
pivot output state; it is not a no-go for every generalized compound pivot.

## 7. Exact frontier

The boundary problem now separates cleanly.

* **Raw fixed-endpoint reset:** exact cost `d-s_*`, at least `d-2` for the
  rigid PBBS pair.
* **Abstract zero-charge exact crossover:** solved, with sharp support four,
  by Theorem 4.1.
* **Fixed rigid PBBS planting:** impossible without changing an owner
  neighbourhood, by Theorem 6.1.
* **Remaining constructive target:** replace a bounded number of rigid
  owner neighbourhoods by a split-core/pivot or resident-return collar
  which exposes the four common hinge states in (4.4), and then protect the
  long-upper cone (5.1), zero gaps, and typed cap.

The theorem therefore removes the ambiguity between a `2`-switch, a `C6`,
and a `C8`: for an exact two-component, zero-charge, owner/q1-preserving
source crossover, the `C8` is the first possible packet and is already
explicit.  The unresolved issue is physical PBBS endpoint replacement, not
the crossover algebra.

## 8. Dependencies

The forced-pair and short-block characterization is in

`MATH_THEOREM_RESIDENT_JOHNSON_FORCED_PAIRS_AND_COMMON_HISTORY_CRITERION_20260805.md`.

The fixed rigid no-go is

`MATH_THEOREM_PBBS_RIGID_ROTATION_FORCED_PAIR_COMMON_HISTORY_NOGO_20260805.md`.

For disjoint history blocks, the occurrence transport is the four-role
specialization of

`MATH_THEOREM_CYCLIC_COMMON_HISTORY_HINGE_RING_AND_SHORT_DECK_INVARIANCE_20260804.md`

and is compatible with

`MATH_THEOREM_COMMON_DEBRUIJN_VERTEX_SHORT_DECK_FUSION_20260805.md`.

The latter theorem uses only literal equality of the ordered history, not
disjointness of its letters, and therefore justifies the overlapping-cover
generalization in Section 4.

The split-core endpoint candidate is

`MATH_THEOREM_SPLIT_CORE_PIVOT_LITERAL_TWO_SIDED_COLLAR_20260801.md`.
