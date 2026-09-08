# Independent audit of odd-dimensional literal boundary rigidity

## Verdict

**PASS, with one harmless low-slack proof clarification.**

The theorem in `ODD_LITERAL_BOUNDARY_RIGIDITY.md` is correct.  Under its three
explicit hypotheses

```text
x0 <= 1,
xd > 0,
L > P_(d-2)(n-2),
```

every literal upper-middle entry is the same mask, every occurrence is a word
endpoint, and the two endpoints cannot both contain such an entry.  Reversal
and coordinate permutation therefore give the claimed canonical-left
existence normal form.

The proof as written is fully direct for `d>=2`, including every application
with odd `7<=k<20`.  If the theorem is read literally for `d=1`, the sentence
assigning endpoint slack `d-2=-1` should instead stop immediately: after
deleting the endpoints, only `M-1` positions remain and cannot support `M`
incomparable rank-`r` witnesses.  This is a proof case split, not a
counterexample.  For `d=0`, the standing selected-band hypotheses are already
incompatible in every nontrivial case.  Thus the stated conclusion remains
valid.

## 1. Frozen inputs and dependencies

```text
e9eb8669dac8378d546ef60c7486e1fca9f624d3016ceee82653c97e5a368f43
    ODD_LITERAL_BOUNDARY_RIGIDITY.md

8a9794eef38321a4fa1488e3ab2b877065b91a2a372c2e31e52c5a6225817354
    ODD_CROSS_LAYER_WIDTH_THEORY.md

5c4f7a2117b91dae15bc87e4c957e056b91f55687fbcef8a61e6f247994a1478
    scratch/verify_odd_cross_layer_widths.cpp

916f78167d01a0072517467128610ca7ae219c254e694c41219916e046c78a64
    scratch/verify_k11_upper_literal_mask_cut.cpp
```

The first two hypotheses must hold for **every independently selected**
upper-middle witness family.  This quantifier is explicitly present in the
general cross-layer and short-pool proofs:

* `x0<=1` is obtained from omitted endpoints and the lower fan bound;
* `xd>0` is obtained from the short-interval pool and therefore does not rely
  on one preferred central schedule.

The rigidity theorem would not follow from a claim about only one frozen
witness selection.  The supplied hypotheses have the required stronger
quantifier.

## 2. Distinct masks and deliberate reselection

Let two different rank-`r+1` masks `S,T` occur literally at positions `p,q`.
Select `[p,p]` and `[q,q]` as the witnesses for those two targets and select
one arbitrary interval for every other rank-`r+1` and rank-`r` target.

This selection is always legitimate.  Two selected intervals for distinct
equal-rank masks cannot contain one another, because physical containment
would imply containment of their OR masks, while distinct equal-cardinality
sets are incomparable.  Hence no additional simultaneous compatibility
condition is missing.

The chosen family has `x0>=2`, contradicting `x0<=1`.  Therefore every
literal upper-middle entry, if any, has one common mask `C`.

Repeated occurrences of `C` do not evade the theorem.  For each particular
occurrence `[p,p]`, reselect that occurrence alone as the witness for target
`C` and rebuild all other witnesses.  Only one interval is selected for the
target `C`, so repeated unselected occurrences do not increase `x0`; the
universally quantified hypotheses nevertheless apply to this newly selected
family.  The localization argument can therefore be run separately for every
physical occurrence.

An interval containing `[p,p]` cannot be forced on another upper-middle
target: its OR contains `C`, and a rank-`r+1` set containing `C` must equal
`C`.  This gives an additional direct check that deliberate reselection does
not obstruct the remaining target choices.

## 3. General-`d` state comparability

For the reselected upper family, equal-rank nonnesting gives the monotone band

\[
 I_i=[i+\alpha_i,i+\beta_i],
 \qquad 0\le\alpha_i\le\beta_i\le d,
\]

with both offset sequences nondecreasing.

A width-`d` interval has

\[
 \beta_i-\alpha_i=d,
\]

and the offset bounds make `(0,d)` its unique possible state.  A width-zero
state is `(a,a)`.  If it occurs before `(0,d)`, coordinatewise monotonicity
requires

\[
 (a,a)\le(0,d),
\]

so `a=0`.  If it occurs afterward, `(a,a)>=(0,d)` forces `a=d`.  There are no
other comparable width-zero states.

The hypothesis `xd>0` ensures that `(0,d)` occurs.  Deliberately selecting a
literal gives `x0>=1`, while the other hypothesis gives `x0<=1`; hence there
is exactly one width-zero selected interval.  A sole `(0,0)` is the first
schedule slot and equals `[0,0]`.  A sole `(d,d)` is the last slot and equals

\[
 [(M-1)+d,(M-1)+d]=[n-1,n-1].
\]

Since every literal occurrence may be selected in turn, all occurrences are
word endpoints.  This argument works unchanged for every `d>=1`; for `d=0`
the states `(0,d)` and `(0,0)` coincide and the nontrivial hypotheses already
force an impossible number of selected singletons.

## 4. Deleting two endpoints and reindexing

Assume both endpoints have rank `r+1`.  Any interval whose OR has rank at most
`r` avoids both endpoints.  Therefore every target through rank `r` has a
witness in the contiguous interior word of length

\[
 n'=n-2=M+d-2.
\]

Deleting the endpoints merely subtracts one from every surviving physical
index.  It neither joins two separated pieces nor changes an OR.  Select one
interior witness for each of the `M` rank-`r` masks and sort them afresh; no
old endpoint numbering is reused.

### The main case `d>=2`

Put `D=d-2`, so `n'=M+D`.  The equal-rank band theorem gives

\[
 I_i\subseteq[i,i+D].                            \tag{1}
\]

Every physical interval of length at least `D+1=d-1` contains `I_a`, where
`a` is its left endpoint, and consequently has OR rank at least `r`.  Thus a
target of rank at most `r-1` needs an interval of length at most `D=d-2`.

The exact number of available nonempty intervals of these lengths is

\[
 P_D(n')=
 \sum_{\ell=1}^{d-2}(n'-\ell+1).                 \tag{2}
\]

There are

\[
 L=\sum_{s=1}^{r-1}{k\choose s}
\]

distinct lower targets.  One physical interval has one OR value, so the
strict inequality `L>P_D(n')` is a contradiction.

### Low-slack edge cases

* `d=2`: `D=0`; all `M` selected rank-`r` witnesses in the `M`-position
  interior are singletons.  Every nonempty interval has rank at least `r`, so
  no lower target can occur.  Formula (2) is the empty sum zero, exactly as
  stated.
* `d=1`: the interior has only `M-1` positions.  Equal-rank endpoint
  injectivity already makes `M` selected rank-`r` witnesses impossible.  The
  theorem remains true, but this immediate contradiction should replace the
  formal phrase "slack `-1`."
* `d=0`: already incompatible with `x0<=1` and a nontrivial full upper layer;
  no application in the displayed range uses it.

Thus deletion and endpoint shifting expose no counterexample.

## 5. Independent arithmetic for odd `7<=k<20`

Recomputing the rank-count bound, central binomials, lower ideals, and
short-pool bound gives:

| `k` | `r` | `M` | `B(k)` | `d` | `L` | `P_(d-2)(n-2)` | base lower bound on `xd` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 7  | 3 | 35 | 37 | 2 | 28 | 0 | 25 |
| 9  | 4 | 126 | 128 | 2 | 129 | 0 | 126 |
| 11 | 5 | 462 | 465 | 3 | 561 | 463 | 93 |
| 13 | 6 | 1,716 | 1,719 | 3 | 2,379 | 1,717 | 657 |
| 15 | 7 | 6,435 | 6,438 | 3 | 9,948 | 6,436 | 3,507 |
| 17 | 8 | 24,310 | 24,313 | 3 | 41,225 | 24,311 | 16,909 |
| 19 | 9 | 92,378 | 92,381 | 3 | 169,765 | 92,379 | 77,381 |

The short-pool column is

\[
 L+2M-\left(d(M+d)-{d\choose2}\right),          \tag{3}
\]

the `x0=0` form of the stronger bound.  Every entry is positive, proving
`xd>0` for every selected family.  The audited cross-layer calculation gives
`x0<=1` in all seven rows.

For `d=2`, `L>0` verifies condition (1).  For `d=3`, the pool in (2) has one
length class and size `M+1`; every displayed `L` is strictly larger.  The
arithmetic in the source note is exact.

Two independent compiled checks passed:

```text
verify_odd_cross_layer_widths: odd_cross_layer_widths=PASS
verify_k11_upper_literal_mask_cut: all embedded short-pool rows PASS
```

The first checker recomputes `B(k)` rather than embedding the displayed
excesses.  The second independently asserts all seven short-pool values.

## 6. Canonical reversal/coordinate normal form

After Sections 2--4, there is at most one literal rank-`r+1` occurrence.
If it is at position `n-1`, reverse the word.  Reversal bijects contiguous
intervals and preserves each interval OR.  Then use a coordinate permutation
to send its `(r+1)`-set to

\[
 \{0,1,\ldots,r\}.
\]

The symmetric group on `2r+1` coordinates is transitive on `(r+1)`-subsets,
and coordinate permutations commute with union/OR.  If no upper-middle
literal occurs, the restriction is vacuous.  Therefore every solution orbit
has a canonical-left representative, exactly as claimed.

This is an existence WLOG, not a labelled/oriented necessary condition.  It
must be jointly audited before composition with a separate hard coordinate or
left/right symmetry break.  No such extra break is part of the abstract
theorem.

## 7. Counterexample search ledger

| attempted escape | result |
|---|---|
| two distinct literal upper masks | deliberate singleton reselection gives `x0>=2` |
| repeated copies of one upper mask | select each occurrence in a separate witness family; each localizes to an endpoint |
| width-zero state `aa` with `0<a<d` | incomparable with mandatory state `(0,d)` |
| both endpoint occurrences | lower ideal exceeds the exact interior short-interval pool |
| deletion shifts endpoints | witnesses are reindexed and the band theorem is reapplied |
| equality rather than strictness in (1) | gives no contradiction; the theorem correctly assumes strict `>` |
| no literal occurrence | canonical restriction is vacuous |
| occurrence at the right endpoint | reversal supplies the left representative |
| noncanonical mask | coordinate transitivity maps it to the first `r+1` coordinates |

No counterexample survives the stated hypotheses.

## Final assessment

The general rigidity theorem and every `k=7,9,...,19` application pass.  The
only editorial improvement suggested by the audit is an explicit `d=1` case
split in the two-endpoint proof; it does not affect validity or any intended
application.
