# Exact C6 row energy and an endpoint-disjoint Catalan extraction

Date: 2026-07-31  
Status: unconditional for the **raw local** incidence-C6 token catalogue.
It strengthens the average-load extraction by giving the exact token-pair
energy and an explicitly endpoint-disjoint anchor family.  Complete cap,
upper-witness and topology tickets are outside its scope.

## 1. Exact row energy

Let

\[
  W={2m+1\choose m},\qquad I=W(m+1),\qquad L=m^2.
\]

There are `I` oriented middle-level incidence anchors and `L` C6 candidates
at each anchor.  For anchors `e,f`, define

\[
 K(e,f)=\frac1L\sum_r a_e(r)a_f(r),
\]

where `a_e(r)` is the number of candidates in the list at `e` containing
the typed rank-`m`, rank-`m+1`, or incidence token `r`.  Thus `K(e,f)` is
the average number of token-conflict witnesses from one candidate of `e`
into the entire list at `f`.  It may count one conflicting pair more than
once, so it upper-bounds average external packet degree.

### Theorem 1.1

For every anchor `e`,

\[
 \sum_{f\ne e}K(e,f)
   =18m^3+51m^2-4m-5=:R_m.                         \tag{1.1}
\]

In particular `R_m<44m^3` for `m>=2`.

### Proof

The exact full-atlas load of a vertex token on either shore is
`3(m+1)m^2`.  One local list has `3m^2` vertex-token occurrences on each
shore.  By the weighted role table, the sum of squared local
multiplicities on either shore is

\[
                  m^4+m^3+m^2.                       \tag{1.2}
\]

Indeed the source-fixed role has multiplicity `m^2`, the `m` one-free
roles have multiplicity `m`, and the `m^2` zero-free roles have
multiplicity one.  Therefore the two vertex shores contribute

\[
 2\,\frac{3m^2\cdot3(m+1)m^2-(m^4+m^3+m^2)}{m^2}
 =18m^3+16m^2-2m-2.                                  \tag{1.3}
\]

The full-atlas incidence-token load is `6m^2`.  A local list has `6m^2`
incidence occurrences and squared-multiplicity sum

\[
                  m^4+2m^3+3m^2.                     \tag{1.4}
\]

Its contribution is

\[
 \frac{6m^2\cdot6m^2-(m^4+2m^3+3m^2)}{m^2}
 =35m^2-2m-3.                                         \tag{1.5}
\]

Adding (1.3) and (1.5) proves (1.1).  QED.

## 2. Endpoint-disjoint sparse extraction

Two anchors are endpoint-adjacent when their source incidences share a
rank-`m` or rank-`m+1` endpoint.  The middle-level incidence graph is
`(m+1)`-regular, so every anchor has `2m` endpoint-neighbours and there are
exactly `Im` unordered endpoint-adjacent pairs.

### Theorem 2.1

For every `m>=2` there is an endpoint-disjoint anchor family `A` with

\[
             |A|\ge {W\over32m}                       \tag{2.1}
\]

and

\[
             \sum_{f\in A\setminus\{e\}}K(e,f)\le16m
             \qquad(e\in A).                         \tag{2.2}
\]

### Proof

Choose every anchor independently with probability

\[
                         p={1\over16m^2}.
\]

Let `S` be the chosen set, `X` the number of selected endpoint-adjacent
pairs, and

\[
             Z=\sum_{\{e,f\}\subset S}K(e,f).
\]

Then

\[
 \mathbb E|S|=pI,\qquad
 \mathbb EX=p^2Im,\qquad
 \mathbb EZ\le {p^2IR_m\over2}.                       \tag{2.3}
\]

Delete at most one anchor for every endpoint-adjacent pair.  Next delete
every remaining anchor whose weighted degree exceeds `16m`.  The second
deletion removes at most `2Z/(16m)` anchors.  Hence the expected number of
survivors is at least

\[
 pI-p^2Im-{p^2IR_m\over16m}
 \ge pI\left(1-{1\over16m}-{11\over64}\right)
 >{pI\over2}.                                         \tag{2.4}
\]

Some outcome therefore has at least `pI/2` survivors.  Since

\[
 {pI\over2}={W(m+1)\over32m^2}\ge {W\over32m},
\]

it gives (2.1).  The two deletion rules give endpoint-disjointness and
(2.2).  QED.

### Corollary 2.2

For `m>=128`, one may choose one raw local C6 from every retained anchor so
that the chosen C6 supports are pairwise token-disjoint.

Indeed (2.2) bounds the average external packet degree of every list by
`16m`.  Per-list Markov pruning followed by Haxell applies when

\[
                        m^2\ge8(16m),
\]

which is exactly `m>=128`.

## 3. Why maximum token load is the wrong statistic here

The endpoint-disjoint owner-star family gives the clean calibration.  A
single one-free upper token occurs in `m` candidates from each of `m`
lists.  Its total token load is `m^2`, and a packet containing it has
`m(m-1)` conflicting packets through that token.  Nevertheless its
contribution to the **average** external degree of one list is only

\[
             {m\cdot m(m-1)\over m^2}=m-1.            \tag{3.1}
\]

Thus the maximum-load route rejects a configuration that the average route
handles by deleting only the `1/m` fraction of high-degree candidates.
Source-source collisions remain different: they contribute `m^2` to the
row energy and are removed by endpoint-disjointness.

Endpoint-disjointness by itself is nevertheless insufficient.  Fix one
anchor `e_0=(C,C+a_0)`.  Enumerate the other `m` points outside `C` as
`b_1,...,b_m`, and choose distinct `a_i in C`.  Put

\[
 U_i=C+b_i,\qquad C_i=U_i-a_i,qquad f_i=(C_i,U_i).
\]

The `m+1` anchors `e_0,f_1,...,f_m` have pairwise distinct lower and upper
source endpoints.  In list `f_i`, the one-free lower role obtained by
deleting `b_i` is exactly `C`, in `m` candidates.  Since `C` is source-fixed
in all `m^2` candidates of `e_0`,

\[
                   K(e_0,f_i)\ge m,qquad
       \sum_iK(e_0,f_i)\ge m^2.                       \tag{3.2}
\]

Thus an arbitrary endpoint matching can still have one list with quadratic
average conflict, far above `O(md)` when `d=o(m)`.  The sparse weighted
alteration, or an equivalent spread condition, is genuinely necessary.

## 4. Buffered extension and exact remaining gate

The same alteration works for complete packets if their full-atlas row
energy obeys

\[
 \sup_e\sum_{f\ne e}K_{\rm full}(e,f)=O(d(m)m^3).      \tag{4.1}
\]

It then extracts `Theta(W/m)` lists with per-list average external conflict
`O(d(m)m)`, sufficient for Haxell when `d(m)=o(m)` and the guarded lists
remain quadratic.

Condition (4.1) is strictly weaker than `O(m)` maximum token load.  It is
not implied by the local C6 table for complete common-cap, replacement-
witness, or topology tickets.  A cap cut vertex used by every option of many
lists can violate (4.1) by an arbitrarily large factor.

There is one further quantifier.  The theorem chooses its task/anchor family
from the full incidence atlas.  A prescribed Catalan leave requires either

1. freedom to identify its tasks with the retained anchors; or
2. a spread distribution on eligible task--anchor matchings with comparable
   pair marginals.

Ordinary Hall existence supplies neither.  This spread matching statement,
plus the complete-ticket row energy (4.1), is the precise surviving bridge
from the raw extraction to `B(k)+O(1)`.

## 5. Independent replay

The small-parameter enumerator

```text
scratch/audit_dispersed_catalan_average_conflict_20260731.py
```

checks (1.1) for every anchor at `m=2,3,4,5` and checks the owner-star
identity (3.1).  Its output is

```text
scratch/dispersed_catalan_average_conflict_20260731.audit.json
```

with canonical payload

```text
03766531a0d246bdb5c141de35a81ae7ad6bbcd14dfea838dda5141dd1df0183.
```
