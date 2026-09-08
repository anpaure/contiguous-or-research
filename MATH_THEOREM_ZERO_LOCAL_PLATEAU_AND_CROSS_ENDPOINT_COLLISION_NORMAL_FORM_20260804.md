# Zero local plateau and the cross-endpoint collision normal form

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional consequence of the two-sided collar construction
when `r>=2d`.  It identifies the duplicate term exactly as a global
cross-endpoint collision count.  It does not bound that count.

## 0. Outcome

Let `A=(A_0,...,A_(W+d-1))` be the antecedent supplied by
`MATH_THEOREM_TWO_SIDED_MANDATORY_COLLAR_DESATURATION_AND_ZERO_RANK_LEAKAGE_20260804.md`.
Assume in addition

\[
                              r\ge 2d.                \tag{0.1}
\]

For every right endpoint `j`, its short suffix values

\[
 S_{j,q}=\bigcup_{p=j-q+1}^{j}A_p,
 \qquad 1\le q\le\min(d,j+1),                       \tag{0.2}
\]

form a strictly increasing chain.  For every left endpoint `i`, its short
prefix values

\[
 U_{i,q}=\bigcup_{p=i}^{i+q-1}A_p,
 \qquad 1\le q\le\min(d,W+d-i),                     \tag{0.3}
\]

also form a strictly increasing chain.  Every value in both families has
rank below `r`.

Thus the source word has no local plateau waste.  If

\[
 {cal K}_j=\{S_{j,q}:1\le q\le\min(d,j+1)\},        \tag{0.4}
\]

then each `K_j` is a set-chain and

\[
 \boxed{
 D_A=\sum_{S\in\mathcal L}
       \bigl(|\{j:S\in\mathcal K_j\}|-1\bigr)_+
     =\sum_j|\mathcal K_j|-\left|\bigcup_j\mathcal K_j\right|.}
                                                               \tag{0.5}
\]

Since `sum_j |K_j|=Lambda+sigma` and `R_A=0`, the remaining scalar gate is
equivalently

\[
 D_A\le\sigma+C
 \quad\Longleftrightarrow\quad
 \left|\bigcup_j\mathcal K_j\right|\ge\Lambda-C.    \tag{0.6}
\]

In words: after paying the mandatory two-sided collar and one rooted Euler
trail exactly, the lower problem is purely to make the coherent endpoint
chains globally rainbow up to `C` omitted Boolean targets.  There is no
within-chain duplication, rank leakage, pin surcharge, or route reset left
in the scalar.

## 1. Strict right-endpoint chains

Compare `S_(j,q)` with `S_(j,q-1)`.  The new leftmost source position is

\[
                              p=j-q+1.               \tag{1.1}
\]

There are three cases.

### 1.1 An ordinary departure position

If `p<=W-2`, then `alpha_p in A_p`.  Moreover

\[
 \alpha_p\notin T_{p+1}
            =\bigcup_{h=p+1}^{p+d+1}A_h.            \tag{1.2}
\]

Since `j<=p+d-1`, the old suffix `A_(p+1) union ... union A_j` is contained
in `T_(p+1)`.  Hence `alpha_p` is new and

\[
                         S_{j,q-1}\subsetneq S_{j,q}. \tag{1.3}
\]

### 1.2 The last unmodified source position

If `p=W-1`, then `A_p=E_(W-1)`.  Its rank is at least `r-d`, because it is
the intersection of at most `d+1` consecutive rank-`r` Johnson owners.
The old suffix uses at most `d-1` of the final singleton arrival letters,
so its rank is at most `d-1`.  Condition (0.1) gives

\[
                         |E_{W-1}|\ge r-d\ge d>d-1.  \tag{1.4}
\]

Therefore `E_(W-1)` is not contained in the old suffix, and (1.3) again
holds.

### 1.3 The right arrival collar

If `p>=W`, then

\[
                        A_p=\{\beta_{p-d-1}\}.       \tag{1.5}
\]

All later letters in the cell are consecutive singleton arrival labels.
Arrival labels cannot repeat within at most `d` transitions, since such a
repeat would enclose an internal positive run shorter than `d+1`.
Therefore the singleton in (1.5) is new.

These cases prove strictness of every right-endpoint chain.  The
zero-leakage theorem proves that all their values are strict-lower.

## 2. Strict left-endpoint chains

Compare `U_(i,q)` with `U_(i,q-1)` and put

\[
                              p=i+q-1.               \tag{2.1}
\]

Again there are three cases.

If `p>=d+1`, the mandatory arrival coordinate

\[
                         \beta_{p-d-1}\in A_p        \tag{2.2}
\]

is absent from owner

\[
 T_{p-d-1}=\bigcup_{h=p-d-1}^{p-1}A_h.              \tag{2.3}
\]

The preceding part of the cell has length at most `d-1` and lies in that
owner window, so (2.2) is new.

If `p<d`, the left collar gives `A_p={alpha_p}`.  The earlier letters in
the cell are distinct consecutive departure singletons, so `alpha_p` is
new.

The only remaining case is `p=d`.  Then `A_d=E_d`, whose rank is at least
`r-d>=d`, while the preceding part of the cell uses at most `d-1` left
collar singletons.  Hence `E_d` is not contained in the old prefix.

Thus every left-endpoint chain is also strict.  Its values are the same
physical short-cell values already proved strict-lower.

## 3. Exact collision accounting

Every physical short cell has a unique right endpoint, so the multiset
union of the chains `K_j` is exactly the multiset of all short-cell values.
Strictness says a target occurs at most once in any fixed `K_j`.  Therefore
its multiplicity is

\[
                       m_A(S)=|\{j:S\in\mathcal K_j\}|. \tag{3.1}
\]

Summing `(m_A(S)-1)_+` gives the first equality in (0.5).  For any finite
multiset, total cardinality minus support cardinality is the same sum,
giving the second equality.

There are

\[
 \sum_j|\mathcal K_j|
 =\sum_{q=1}^d(W+d-q+1)
 =\Lambda+\sigma                                      \tag{3.2}
\]

cells.  Substitution into (0.5) proves (0.6).

For exact distinct forced lower pins, the fixed-word reclassification
identity leaves the same `D_A`; thus (0.5)--(0.6) apply unchanged inside
the pinned fibre.

## 4. What this rules out and what remains

The exact endpoint-capacity vector is

\[
             (d^{\,W+1},d-1,d-2,\ldots,1).          \tag{4.1}
\]

The theorem shows that a literal word on the desaturated face already
realizes each slot as a genuine Boolean chain of its full capacity.  Hence
the remaining lower obstruction is not:

- failure to use a slot;
- a plateau inside one endpoint chain;
- rank-`r` leakage;
- forced-ray reclassification; or
- an Euler-component reset.

It is exactly the **cross-slot rainbow defect** in (0.5), subject to the
fact that all chains arise from one common countdown word.  The proved
fractional endpoint-triangular theorem makes every named target load one in
expectation, but does not choose one globally rainbow coherent chain in
each slot.  Generic perfect-graph or Greene--Kleitman integrality is known
not to imply such a choice.

Thus an integral one-copy theorem sufficient for `B(k)+O(1)` may now be
stated sharply:

> Construct a resident, owner-once rooted Euler chronology extending the
> protected ray halo whose desaturated endpoint chains have support at
> least `Lambda-O(1)`.

This theorem does not construct that chronology and does not prove an
additive upper bound.

## 5. Dependencies

- `MATH_THEOREM_TWO_SIDED_MANDATORY_COLLAR_DESATURATION_AND_ZERO_RANK_LEAKAGE_20260804.md`;
- `MATH_COROLLARY_LITERAL_LOWER_DECK_WASTE_AS_L1_DISCREPANCY_20260804.md`;
- `MATH_THEOREM_ENDPOINT_TRIANGULAR_BOUNDED_CHAIN_FRACTIONAL_EXACTNESS_20260804.md`.
