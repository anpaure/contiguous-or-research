# Independent audit: collar desaturation, local plateau, rank-row transport,
# and literal `L1` waste

**Date:** 2026-08-04  
**Method:** pure proof audit; no computation, search, solver, or finite census  
**Status:** **GO after two proof repairs and several notation repairs.**  The
four mathematical conclusions survive at their stated scopes.  None proves
the remaining cross-endpoint duplicate bound or an additive upper bound.

## 0. Frozen inputs after audit repairs

| artifact | SHA256 |
|---|---|
| `MATH_THEOREM_TWO_SIDED_MANDATORY_COLLAR_DESATURATION_AND_ZERO_RANK_LEAKAGE_20260804.md` | `ae74f498e858aed27837d9630c540c1676f58afdd548d083d8a62839c6e505b5` |
| `MATH_AUDIT_TWO_SIDED_MANDATORY_COLLAR_DESATURATION_SELF_20260804.md` | `b878b6cee8cdcfb253c7647e2c4826cf336367caeabbd3b876bc962654089871` |
| `MATH_THEOREM_ZERO_LOCAL_PLATEAU_AND_CROSS_ENDPOINT_COLLISION_NORMAL_FORM_20260804.md` | `c514b4de0e1ed04265a184913edff905039bc75fa2fd9b81b707e2e2c4635593` |
| `MATH_AUDIT_ZERO_LOCAL_PLATEAU_AND_CROSS_ENDPOINT_COLLISION_SELF_20260804.md` | `faa7f86fb89687568764ff68609848ea92d8bbf0b50ad4b33aca8077d9193d1e` |
| `MATH_THEOREM_PINNED_RAY_RANK_ROW_TRANSPORT_AND_COLLAR_DEBT_COLLAPSE_20260804.md` | `6997db7cc44f18761532d3cf96ffeda9b4f96abbb9a36308c7e6566256347d49` |
| `MATH_AUDIT_PINNED_RAY_RANK_ROW_TRANSPORT_AND_COLLAR_DEBT_COLLAPSE_SELF_20260804.md` | `c96e0de46a8090311490345a9cdda194674960df31c46c960bb66e0e453cb334` |
| `MATH_COROLLARY_LITERAL_LOWER_DECK_WASTE_AS_L1_DISCREPANCY_20260804.md` | `d9f762732f240be4c0126dc91e0546a290159f0f9778bc43f492f5b80bff8e64` |

The first collar theorem originally had SHA
`7867d74df49d0d080cfd1850325715003e3c892ca5d052923b1735f64e13aaa9`.
Its two preservation proofs were not valid as written: membership at two
owner indices does not imply continuous membership between them, because a
coordinate may leave and later re-enter.  The theorem statement is still
true.  The repaired proof conditions on the **maximal positive run containing
the audited occurrence**, which is the correct invariant.  The self-audit was
updated in parallel.

The `L1` corollary also had missing display terminators and missing TeX
backslashes.  Those were notation defects only.  The zero-plateau duplicate
formula had one missing backslash before `\left`.  The rank-row theorem now
states explicitly that its exact minimum-run interpretation is cyclic; an
opened linear word has separately priced clipped runs.

## 1. Two-sided mandatory collar: GO after proof repair

### 1.1 Exact run support of the maximal envelope

Let a coordinate have a maximal positive owner run `[a,b]`.  Directly from

\[
 E_p=\bigcap_{i:\,p\in[i,i+d]}T_i
\]

its contribution to the source envelope is

\[
 \begin{cases}
 [0,b],&a=0,\ b<W-1,\\
 [a+d,b],&0<a\le b<W-1,\\
 [a+d,W+d-1],&0<a,\ b=W-1,\\
 [0,W+d-1],&a=0,\ b=W-1.
 \end{cases}                                           \tag{1.1}
\]

For an internal positive run, residence of at least `d+1` owners is exactly
the assertion `a+d<=b`.  Formula (1.1) is the clean way to audit both
collars, including leave-and-re-enter histories.

### 1.2 Left collar

Fix `i<d` and an occurrence `x in T_i`, and use the positive run `[a,b]`
containing that occurrence.

- If `a>0`, then `max(i,a+d)` belongs to `[i,i+d]` and to the appropriate
  support interval in (1.1).  It is at least `d+1` and at most `2d-1<W`, so
  the source position is unmodified.
- If `a=0` and `b>=d`, source position `d` supplies `x`.
- If `a=0` and `b<d`, then `x=alpha_b`, and the retained singleton at `b`
  lies in `[i,i+d]` because `i<=b`.

These cases remain exhaustive even when `x` has other positive runs.  The
original endpoint-membership proof did not.

For `p<d`, the run ending with departure `alpha_p` contains every owner
whose window contains source position `p`.  Otherwise an internal run ending
by transition `p<d` would have fewer than `d+1` owners.  Hence
`alpha_p in E_p`, so the replacement introduces no extraneous label.

### 1.3 Right collar

Fix `W-d<=i<W` and again use the positive run `[a,b]` containing the
occurrence.

- If `b<W-1`, then `min(b,i+d)` belongs to `[i,i+d]` and to `[a+d,b]`; it
  lies below source position `W` and is unmodified.
- If `b=W-1` and `a<=W-d-1`, source position `W-1` supplies `x`.
- If `b=W-1` and `a>W-d-1`, write `u=a-1`.  The retained arrival singleton
  is at `u+d+1=a+d`.  Since `a>=W-d` and `a<=i<=W-1`,

  \[
                         i\le a+d\le i+d,
  \]

  so it lies in the required owner window.

For `W<=p<W+d`, the arrival `beta_(p-d-1)` remains present throughout every
owner whose window contains `p`; an earlier departure would create an
internal positive run shorter than `d+1`.  Thus the replacement is contained
in `E_p`.

### 1.4 Boundary indices and rank leakage

A `q`-cell `[j,j+q-1]`, `1<=q<=d`, is contained in precisely the owners

\[
 [\max(0,j+q-1-d),\min(j,W-1)].                     \tag{1.2}
\]

Under `W>2d`, this interval is a singleton exactly when `j=0` or
`j+q-1=W+d-1`.  Every other cell lies in two consecutive distinct Johnson
owners, so its value lies in an `(r-1)`-set.  The two exceptional cells are
unions of `q` consecutive departure or arrival singletons.  Repetition in
either list would enclose an internal positive run shorter than `d+1`.
Their ranks are therefore exactly `q<r`.  Hence `R_A=0`.

The pin claim is also correctly scoped: separation from the **complete
affected-owner halo**, not merely from the visible pin cells, is required.
The source-letter replacement preserves owner order and one linear trail;
it does not assert cyclic closure of the modified word.

**Verdict for theorem 1:** **GO after repair.**

## 2. Zero local plateau and collision normal form: GO

For a right-endpoint chain, adding source position `p<=W-2` exposes
`alpha_p`, which lies in `A_p` and is absent from the complete next owner
window.  For `p=W-1`,

\[
 |E_{W-1}|\ge r-d\ge d
\]

while the remaining suffix uses at most `d-1` singleton arrivals.  For
`p>=W`, consecutive arrival labels are distinct.  Every extension is strict.

The left-endpoint argument is the exact reverse.  At `p>=d+1`,
`beta_(p-d-1)` is present in `A_p` and absent from the preceding owner
window.  At `p=d`, `|E_d|>=r-d>=d` beats the at-most-`d-1` singleton
prefix.  At `p<d`, consecutive departure labels are distinct.

All these cells are strict-lower by Section 1.  Therefore each right
endpoint contributes a genuine set-chain, and every physical short cell
belongs to exactly one such endpoint chain.  If `m_A(S)` is target
multiplicity, strictness inside a chain gives

\[
 m_A(S)=|\{j:S\in\mathcal K_j\}|.
\]

The total number of short cells is

\[
 \sum_{q=1}^d(W+d-q+1)
 =dW+\binom{d+1}{2}=\Lambda+\sigma.
\]

Hence

\[
 D_A=(\Lambda+\sigma)-\left|\bigcup_j\mathcal K_j\right|,
\]

and `D_A<=sigma+C` is exactly support at least `Lambda-C`.

The hypothesis `r>=2d` is load-bearing only at the two pivot envelopes.
No bound on the global cross-endpoint collision count follows.

**Verdict for theorem 2:** **GO**, conditional only on the repaired collar
theorem and its stated `r>=2d` hypothesis.

## 3. Pinned-ray rank-row transport: GO only at rank projection

### 3.1 Forced rows

In row `q<d`, the two pinned rays are `X_q` and `Y_(d-q)`.  Both have rank

\[
                         s_q=r-d-1+q.
\]

For `r>=2d`,

\[
 s_q-2q=r-d-1-q\ge r-2d\ge0.
\]

They therefore consume no overlap debt.

### 3.2 Exact Ferrers cuts

After reserving the two pins in rows `q<d`, capacities are `W-2` there and
`W` in row `d`.  An item of rank `s>=2` has nested eligible rows
`[1,min(d,floor(s/2))]`; a singleton has only row one.  For `t<d`, the
items whose entire neighbourhood lies in the first `t` rows are exactly
those of rank at most `2t+1`.  At `t=d`, the cut is total demand.  These are
the complete capacitated Hall cuts, not a subset of them.

Since `d=Theta(sqrt(k))`,

\[
 \sum_{s=1}^{2d-1}\binom{k}{s}
 =\exp(O(\sqrt{k}\log k))=o(W),
\]

so eventually it is at most `W-2d`.  For `1<=t<d`,

\[
 W-2d\le t(W-2),
\]

with difference `(t-1)W+2(d-t)`.  The total cut follows by removing the
`2(d-1)` distinct nonboundary pins from demand at most `dW`.  Integral
transportation therefore gives the asserted named-target-to-**row-copy**
assignment.

### 3.3 Exact scope

For `q>1`, every scheduled rank obeys `s>=2q`; for `q=1`, only singleton
items contribute.  On the cyclic resident-factor face, the right side of
the mandatory-collar inequality counts exact minimum positive runs when
`q=1`.  This interpretation does not silently include clipped linear
boundary runs; the repaired statement now says so.

The theorem does not map any row copy to a physical address, prove
`K_(j,q) subseteq S subseteq E_(j,q)`, make pins coexist in one word, or
construct the labelled minimum-run transversal.  “One correctly labelled
minimum run per singleton” is a remaining carrier hypothesis, not an output
of the Ferrers flow.

**Verdict for theorem 3:** **GO at its stated rank-row projection and cyclic
run-census scope.  NO-GO as evidence of a physical lower-deck lift**, which
the theorem itself explicitly excludes.

## 4. Literal `L1` discrepancy: GO

After deleting exact forced target/address pairs, residual short cells
partition into unforced strict-lower occurrences, extra occurrences of
forced values, and rank-`r` cells.  Consequently

\[
 \sum_Sm(S)-|\mathcal L\setminus L(\Pi)|
 =\sigma-Q-R=D-M.                                   \tag{4.1}
\]

For the integer occurrence vector,

\[
 V=\sum_S|m(S)-1|=M+D.                              \tag{4.2}
\]

Solving (4.1)--(4.2) gives exactly

\[
 2M=V+Q+R-\sigma,
 \qquad
 2D=V-Q-R+\sigma.
\]

Parity, the exact complete-coverage criterion, and the unit-transfer descent
all follow immediately.

For an exact pin bank with distinct strict-lower target values, deleting one
chosen occurrence of a forced value with original multiplicity `m` leaves
`m-1` occurrences counted by `Q`.  This is precisely that value's original
duplicate contribution.  Unforced multiplicities and rank-`r` cells do not
change, and every removed target was present.  Hence

\[
 D_A^\Pi+Q_A^\Pi=D_A,
 \qquad R_A^\Pi=R_A,
 \qquad M_A^\Pi=M_A.
\]

The identities are fixed-word statements.  They do not show that the
occurrence-vector transfer `m-e_U+e_Z` is physically realizable.

**Verdict for corollary 4:** **GO after notation repair.**

## 5. Combined proof-safe conclusion

On a sufficiently long resident simple Johnson path with a separated pin
halo, the repaired collar theorem gives `R_A=0`.  Exact pins only reclassify
duplicates.  Under `r>=2d`, every endpoint slot is already a strict Boolean
chain.  Therefore the terminal lower scalar is exactly

\[
 M_A=D_A-\sigma
     =\Lambda-\left|\bigcup_j\mathcal K_j\right|.   \tag{5.1}
\]

Thus the remaining lower theorem really is the global coherent rainbow
problem

\[
                         D_A\le\sigma+O(1),          \tag{5.2}
\]

or equivalently endpoint-chain support at least `Lambda-O(1)`.  The audited
rank-row theorem proves that aggregate rank/run cuts do not obstruct this
goal.  It does not prove (5.2).  Integral one-copy chainization, physical
aperture assignment, carrier construction, upper completeness, and
regeneration remain open.

