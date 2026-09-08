# Owner-intersection language invariance and the read-only PBBS section payload gate

**Date:** 2026-08-06  
**Method:** exact dependence-on-data audit; no computation or search  
**Status:** unconditional no-go for the proposed fixed-row complement
supermacro, and a positive quantifier reduction.  Grouping or thinning
source blocks cannot create a new owner-intersection value while the
labelled owner chronology is fixed.  On the PBBS face all such values are
already present in a read-only whole-fan section, so the remaining deep
problem is only a target-to-source-block atlas.

## 1. Two languages of a source factor

Let `A=(A_i)` be a cyclic source word and

\[
                         T_i=\bigcup_{h=0}^{d}A_{i+h}
\tag{1.1}
\]

its labelled owner chronology.  Define

\[
 \mathcal I(T)=
 \left\{
   \bigcap_{j\in J}T_j:
   J\text{ a nonempty cyclic owner interval}
 \right\}
\tag{1.2}
\]

and

\[
 \mathcal U(T)=
 \left\{
   \bigcup_{j\in J}T_j:
   J\text{ a nonempty cyclic owner interval}
 \right\}.
\tag{1.3}
\]

The short source language

\[
 \mathcal C_{\le d}(A)=
 \left\{
   \bigcup_{p\in I}A_p:1\le |I|\le d
 \right\}
\tag{1.4}
\]

depends on the antecedent and may change under thinning.

### Theorem 1.1 (fixed-row language invariance)

If `A` and `A'` have the same labelled owner row `T`, then

\[
                         \mathcal I(T),\qquad\mathcal U(T)
\]

and every occurrence address in those two languages are identical for the
two source words.  Consequently no operation consisting only of

* thinning letters inside maximal envelopes;
* grouping already consecutive source blocks;
* declaring a block and its complement to be one supermacro; or
* changing payload labels while retaining every `T_i`

can add a value to `\mathcal I(T)` or `\mathcal U(T)`.

#### Proof

Both (1.2) and (1.3) are functions of the ordered tuple `(T_i)` alone.
The listed operations do not change that tuple. \(\square\)

### Corollary 1.2 (sharp complement-supermacro no-go)

Let `S` be a deep value installed by a thinned source interval.  If

\[
                         S\notin\mathcal I(T)
\]

before the thinning, then no grouping of `O(d)` or any other number of
thinned blocks, and no formal complement closure of that group, makes `S`
an owner intersection without changing the labelled owner chronology.

Thus a complement-closed bottom supermacro cannot turn an arbitrary
payload atlas into an all-depth intersection atlas on a fixed row.

## 2. Changing only the owner multiset is not enough

If “the same global owner row” is weakened to “the same owner multiset,”
Theorem 1.1 no longer applies, but neither does the desired conclusion.
The intersection/union languages depend on adjacency and order.  Two
Hamilton orderings of the same owner set can have different immediate
upper palettes, and a fortiori different all-width languages.

Therefore a block permutation which changes owner order must supply, as
new theorem input,

1. a literal source homotopy or new antecedent;
2. the immediate lower and upper palette ledger;
3. retention or replacement of every named upper witness; and
4. residence and opening data.

Calling the permuted blocks one complement-closed supermacro proves none of
these rows.

## 3. The PBBS section changes the quantifier

Let `\mathcal S` be the fixed PBBS whole-fan section.  For every strict-lower
target `S`, it already contains a named owner interval

\[
                         K_S
\]

with

\[
                         \bigcap_{j\in K_S}T_j=S.
\tag{3.1}
\]

The paths `K_S` may overlap heavily.  This is harmless: they are witnesses
in one fixed owner factor, not capacity-one services in a target matching.
After complementation, the same fixed paths give the paired proper-upper
values.  A polynomial puncture of the section is repaired by the
complement-paired backup theorem.

Suppose now that a block bank `R` in one antecedent of the **same** owner
row carries source intervals `I_S` satisfying

\[
                         \bigcup_{p\in I_S}A_p=S
\tag{3.2}
\]

for every deep target, with the `I_S` distinct and satisfying the exact
payload cuts.

### Theorem 3.1 (read-only section pairing principle)

The pairing

\[
                         S\longmapsto(K_S,I_S)
\tag{3.3}
\]

creates no new owner-side capacity constraint.  The owner paths `K_S` may
be retained read-only with arbitrary mutual overlap, while only the source
addresses `I_S` must be injective.  Payload thinning which realizes
(3.2) preserves every owner path and its complementary upper witness.

#### Proof

The owner interval (3.1) is already present in the fixed factor and is not
selected from a capacity-one port bank.  Multiple exact target witnesses
may share owner edges.  Equation (3.2), by contrast, is a literal compiler
matching and therefore requires distinct physical source intervals.

Thinning changes only `A`, not `T`.  Theorem 1.1 retains (3.1), and the
long-deck rigidity identity retains its complementary upper-union witness.
Thus the two occurrence coordinates in (3.3) coexist without a common-cap
matching. \(\square\)

## 4. Exact remaining target

The failed supermacro idea removes one false objective.  The next theorem
does **not** need to make deep targets into new owner intersections; PBBS
already did that.  It needs only:

> **Relative deep payload atlas.**  In an antecedent of the repaired PBBS
> owner row, choose a separated block bank avoiding one canonical
> rank-`(r-d)` lock from every value fibre, and inject every lower target of
> rank below `r-d` into a block interval satisfying the mandatory-core and
> positive-hit cuts.

Once this atlas exists, the fixed whole-fan section supplies the read-only
owner-intersection/complementary-upper coordinate, terminal compiler
functoriality transports the source coordinate, and no terminal common cap
is required.

Balanced-doublet rounding may still help produce the separated block bank,
but only if it is made relative to the fixed PBBS owner row.  A standalone
bottom factor followed by a formal complement grouping does not solve this
relative theorem.

## 5. Scope

Proved here:

* exact invariance of the owner intersection/union languages;
* impossibility of creating new intersection values by fixed-row payload
  grouping;
* absence of owner-side capacity coupling for the read-only PBBS section;
  and
* the reduction to one relative source-atlas selector.

Not proved here:

* that relative atlas;
* integral balanced-doublet rounding on the PBBS row;
* resident source completion of the factor;
* upper-safe opening; or
* `nu(k)<=B(k)+O(1)`.
