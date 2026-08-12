# The `k=17` minimum-cut blocks fail endpoint rounding at singleton Hall

**Date:** 2026-08-01  
**Status:** exact contracted formulation and authenticated finite no-go for
the deterministic minimum residence decomposition of the protected
seven-factor.  The obstruction holds in a deliberately relaxed necessary
residence atlas.  It does not rule out a nonminimum decomposition, changing
block interiors, or a nonlocal seam gadget.

## 0. Outcome

The protected seven-component `ML_9` factor has exact minimum residence-cut
number 3,807.  Choose the deterministic rightmost-greedy protected-gap-
avoiding minimum transversal emitted by the cited audit on every component.
This partitions all 24,310
rank-nine owners into exactly

\[
                              3807                               \tag{0.1}
\]

depth-three-factorable paths and deletes 3,807 distinct rank-eight `q1`
colours.

Treat those paths as atomic trace blocks and permit either orientation of
every block.  Before residence filtering, the Boolean endpoint atlas has a
perfect matching in every two-shore projection.  Thus owner and raw endpoint
supply are not the obstruction.

After imposing only a **necessary** two-block residence condition, the atlas
has

\[
 \boxed{
 1289\text{ deleted rank-eight colours with no candidate seam},\qquad
 368\text{ blocks with no outgoing candidate and }368
 \text{ with no incoming candidate}.}                         \tag{0.2}
\]

Its block-to-colour matching number is exactly

\[
                         2518=3807-1289.                        \tag{0.3}
\]

Therefore the one-copy endpoint stage suggested by the corrected stationary
pull-clock theorem cannot be completed on this frozen factor merely by
matching the endpoints of these minimum-cut blocks while retaining their
interiors and the `q1` palette.  More blocks, interior rethreading, or whole
seam gadgets are mandatory.

## 1. The exact contracted endpoint master

Let \(\mathcal B\) be a path partition of a one-copy rank-\(r\) owner factor
and let \(\mathcal C\) be the set of rank-\((r-1)\) colours deleted at its
cuts.  For a block \(B\), write \(B^+\) and \(B^-\) for its two
orientations.

A seam atom is a triple

\[
                         e=(B^\sigma,D^\tau,I),                  \tag{1.1}
\]

where the last owner of \(B^\sigma\) and first owner of \(D^\tau\) are
distinct Johnson neighbours with intersection \(I\in\mathcal C\).  Add
whatever exact endpoint-flag or residence predicate is required by the
construction.

Use binary variables \(z_{B,\sigma}\) and \(y_e\).  The complete contracted
one-copy equations are

\[
 \sum_{\sigma\in\{+,-\}}z_{B,\sigma}=1                         \tag{1.2}
\]

for every block,

\[
 \sum_{e:\operatorname{tail}(e)=B^\sigma}y_e=z_{B,\sigma},
 \qquad
 \sum_{e:\operatorname{head}(e)=B^\sigma}y_e=z_{B,\sigma},    \tag{1.3}
\]

and

\[
                         \sum_{e:\operatorname{colour}(e)=I}y_e=1
                         \qquad(I\in\mathcal C).               \tag{1.4}
\]

The owner equations are automatic: block interiors partition the owner
layer.  Equation (1.4) is the missing rank-`r-1` colour row.  Directed
subtour cuts make the resulting cycle cover connected.  If a bounded set of
cut colours is intentionally exported to a linear boundary sidecar, replace
the corresponding equalities in (1.4) by the explicitly priced exceptions.

This is the exact endpoint/owner/colour formulation requested after the
pull-clock fractional theorem.  It is a three-resource matching with one
orientation variable shared by the incoming and outgoing occurrence of each
block.

## 2. A necessary residence relaxation

For an oriented block `B` and coordinate `x`, let

* `pre_B(x)` be the length of its positive prefix;
* `suf_B(x)` be the length of its positive suffix; and
* `all_B(x)` say that every owner of `B` contains `x`.

All lengths may be truncated at four.  Every block is internally resident
by construction.

Consider a seam `B|D`.  If neither block is all-one in `x`, global
depth-three residence necessarily gives:

\[
\begin{array}{c|c|c}
x\in\operatorname{last}(B)&x\in\operatorname{first}(D)&
\text{necessary inequality}\\ \hline
1&1&\operatorname{suf}_B(x)+\operatorname{pre}_D(x)\ge4,\\
1&0&\operatorname{suf}_B(x)\ge4,\\
0&1&\operatorname{pre}_D(x)\ge4.
\end{array}                                                  \tag{2.1}
\]

If either block is all-one, impose **no** condition.  A future block is
allowed to rescue that run.  Call the resulting seam set `E_rel`.

### Lemma 2.1 (relaxed atlas contains every resident assembly)

Every seam of every globally depth-three-resident cyclic assembly of the
atomic blocks belongs to `E_rel`.

#### Proof

When neither block is all-one, a positive suffix starts after a zero inside
`B`, and a positive prefix ends before a zero inside `D`.  Hence each run in
(2.1) is bounded internally exactly as displayed and must have length at
least four.  When one block is all-one, dropping the test only enlarges the
atlas.  \(\square\)

Thus infeasibility in `E_rel` is a theorem for every exact stateful endpoint
automaton; it cannot be blamed on an overly conservative local seam rule.

For comparison, the audit also uses the sufficient pairwise rule which
does not permit a future rescue through a short all-one block.  It is not
needed for the no-go.

## 3. Exact `k=17` endpoint census

The deterministic minimum cut family avoids all 26 protected internal
gaps.  It produces 3,807 blocks, 7,614 oriented states, and 3,807 deleted
rank-eight colours.

### 3.1 Raw Boolean seams

With only Johnson adjacency and exact intersection colour imposed, there
are

\[
                              56,790                            \tag{3.1}
\]

oriented seam atoms.  Every cut colour has degree between two and eight.
There are no zero tail states, head states, tail blocks, head blocks, or
colours.  Exact maximum matchings are:

\[
\begin{array}{c|c}
\text{projection}&\text{matching size}\\ \hline
\text{block tail--block head}&3807,\\
\text{block tail--colour}&3807,\\
\text{colour--block head}&3807,\\
\text{oriented tail--oriented head}&7614.
\end{array}                                                  \tag{3.2}
\]

So the raw endpoint graph satisfies ordinary Hall on every two-shore
projection.  This is the strongest unconditional expansion lower bound
available from Boolean endpoint incidence alone.

### 3.2 Necessary residence atlas

After applying only Lemma 2.1, 13,174 seam atoms remain.  The exact census
is

\[
\begin{array}{c|r}
\text{quantity}&\text{value}\\ \hline
\text{zero cut colours}&1289,\\
\text{zero outgoing oriented states}&2462,\\
\text{zero incoming oriented states}&2462,\\
\text{zero outgoing physical blocks}&368,\\
\text{zero incoming physical blocks}&368,\\
\text{block tail--block head matching}&3364,\\
\text{block tail--colour matching}&2518,\\
\text{colour--block head matching}&2518,\\
\text{oriented tail--head matching}&4726.
\end{array}                                                  \tag{3.3}
\]

In particular, the necessary residence-filtered graph has no positive
expansion theorem at all: it fails the singleton Hall cuts on both block
shores and on 1,289 colour vertices.

The conservative sufficient seam rule retains 9,618 atoms and has 1,686
zero colours; this stronger failure is only diagnostic.

## 4. The minimal correlated obstruction

The uncut interiors already use every rank-eight colour outside
\(\mathcal C\) exactly once.  Therefore an exact `q1` reassembly by atomic seams
must satisfy (1.4).  But 1,289 rows of (1.4) have an empty left side even in
the relaxed necessary atlas.

### Theorem 4.1 (minimum-cut atomic endpoint no-go)

No globally depth-three-resident reassembly of the 3,807 deterministic
minimum-cut blocks can simultaneously:

1. retain every block interior;
2. use every block once, in either orientation; and
3. restore every deleted rank-eight colour by an ordinary Johnson seam.

If `b` deleted colours are exported to separately priced boundary or gadget
cells, at least

\[
                              1289-b                            \tag{4.1}
\]

further cut colours remain unserved.

#### Proof

By Lemma 2.1 every seam of such an assembly belongs to `E_rel`.  Each of the
1,289 zero colours has no incident atom of `E_rel`, contradicting its row in
(1.4).  Exporting `b` of those rows leaves the stated residual.  \(\square\)

This is sharper than a fractional-denominator warning.  The raw endpoint
projections are integral and Hall-perfect; the obstruction appears only in
the **correlation between residence and the named deleted colour**.

The result is scoped to this minimum decomposition.  It leaves three viable
routes:

* make additional cuts so the zero colours acquire different endpoints;
* alter/rethread block interiors rather than treating them atomically; or
* use a whole seam/socket gadget whose internal cells deliver a zero colour
  without requiring it to be the direct endpoint intersection.

The 29-owner protected bank survives untouched in all three routes.

## 5. Reproducible artifacts

The standalone C++20 audit is

```text
scratch/audit_k17_h2_contracted_endpoint_hall_20260801.cpp
SHA256 28b2349ef9a0a7de8d5623e16ed5900b45f7852fe0b14ec5f779d94cf9778498
```

and the retained output, including every zero-colour mask, is

```text
scratch/k17_h2_contracted_endpoint_hall_20260801.out
SHA256 1161654663b7f935feaadbfda60e3255bbcb4d2696c884331bb8b486f04a2245
```

It was compiled and run on H100 with
`g++ -std=c++20 -O3 -DNDEBUG`.  No heavy local computation or Python was
used.  The final verdict is

```text
PASS_K17_H2_CONTRACTED_ENDPOINT_HALL
```

The input factor is

```text
scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv
SHA256 7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df
```

and the minimum-cut theorem/audit are recorded in
`MATH_THEOREM_K17_H2_PROTECTED_FACTOR_ONECOPY_HALL_AND_RESIDENCE_CUT_20260801.md`.
