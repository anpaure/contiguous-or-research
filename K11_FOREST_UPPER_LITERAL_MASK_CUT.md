# The k=11 upper-literal-mask cut

## 1. Outcome

Let a candidate nonzero array have length `465` on eleven coordinates.  The
audited odd cross-layer theorem proves the following array-level fact:

```text
among all literal array entries of rank six,
at most one distinct mask may occur.
```

Repeated occurrences of that one mask are allowed.  The theorem concerns the
array itself, not merely which rank-six witnesses happen to be selected by
the central-band encoding.

This note gives two exact CNF encodings.

1. A coordinate-labelled necessary cut using one selector per rank-six mask.
   It composes with arbitrary other hard constraints.
2. A smaller coordinate-symmetry WLOG cut fixing the possible mask to one
   canonical 6-set.  This is the recommended encoding for the current
   coordinate-equivariant `k11_forest_sat.cpp` formula.

No change to the live solver source is made here.

## 2. Why the theorem is genuinely array-level

Write `k=11=2*5+1`.  At `n=C(11,5)+3=465`, the audited theorem gives

```text
x0<=1
```

for **every independently chosen** rank-five and rank-six witness family,
where `x0` is the number of rank-six targets whose selected witness is a
singleton.

Suppose two distinct rank-six masks `S` and `T` occurred literally at
positions `p` and `q`.  Deliberately select `[p,p]` as the witness for `S`
and `[q,q]` as the witness for `T`; choose all other upper and lower witnesses
arbitrarily.  The theorem applies to this choice and gives `x0>=2` and
`x0<=1`, a contradiction.

This quantifier is what permits a direct cut on the eleven array-bit variables
at every physical position.

## 3. Selector encoding

Let

```text
A[p,b], 0<=p<465, 0<=b<11
```

be the existing array-bit variables.  Enumerate the

```text
M=C(11,6)=462
```

rank-six masks.  Introduce a selector `z_S` for every such mask.  The intended
meaning is only

```text
if S occurs literally, then z_S is true.
```

The reverse direction is unnecessary.

For every physical position `p` and rank-six mask `S`, add

```text
(A[p] != S) OR z_S.                         (3.1)
```

In literals this is the single 12-literal clause

```text
z_S
 OR (OR_(b in S)     -A[p,b])
 OR (OR_(b not in S)  A[p,b]).              (3.2)
```

The polarity is important.  Every mismatch literal is false exactly when
`A[p]` agrees with `S`; hence (3.2) then forces `z_S`.  If `A[p]!=S`, at least
one mismatch literal is true and the clause imposes nothing.

Impose at most one on the 462 selectors.  Then two different literal
rank-six masks force two different selectors and contradict the circuit.

### 3.1 Sequential at-most-one circuit

Number the selectors `z_0,...,z_(m-1)`, with `m=462`, and introduce
`s_0,...,s_(m-2)`.  Add

```text
-z_0 OR s_0,

for 1<=i<=m-2:
    -z_i     OR s_i,
    -s_(i-1) OR s_i,
    -z_i     OR -s_(i-1),

-z_(m-1) OR -s_(m-2).
```

If `z_a` and `z_b` were both true with `a<b`, the first occurrence propagates
the prefix state through `s_(b-1)`, contradicting the clause for `z_b`.
Conversely, when at most one `z_j` is true, take

```text
s_i=false for i<j,
s_i=true  for i>=j,
```

with all `s_i=false` when there is no true selector or when only the last
selector is true.  Thus the circuit is an exact existential encoding of AMO.

### 3.2 Soundness and completeness, including no occurrence

* If two distinct rank-six masks occur, their implication clauses force two
  selectors, violating AMO.
* If no rank-six mask occurs, set every selector and every sequential
  auxiliary false.  Every implication contains a true mismatch literal.
* If exactly one distinct rank-six mask `S` occurs, set `z_S=true`, all other
  selectors false, and use the threshold assignment above for the
  auxiliaries.  Repetitions of `S` cause no problem.

Therefore existentially eliminating the new variables yields exactly the
audited array-level condition.

One may add the long clause

```text
z_0 OR ... OR z_461
```

to obtain exact-one rather than at-most-one.  This remains complete even when
no rank-six entry occurs, because an arbitrary unused selector may be chosen.
It is not recommended: in the no-occurrence case it creates 462 semantically
unanchored choices.  AMO naturally admits the canonical all-false extension.

### 3.3 Exact inventory

The implication family has

```text
465*462 = 214830 clauses of length 12.
```

The sequential AMO circuit has

```text
462 selectors,
461 auxiliary variables,
3*462-4 = 1382 binary clauses.
```

Therefore the recommended selector encoding adds exactly

```text
923 variables,
216212 clauses,
2580724 literal occurrences.
```

The exact-one variant has the same variables and adds one clause of length
462:

```text
923 variables,
216213 clauses,
2581186 literal occurrences.
```

For solver phases, set all selectors and sequential variables false unless a
phase seed has a unique rank-six literal mask.  If it does, phase that mask's
selector true and phase the sequential prefix accordingly.  Phases do not
affect completeness.

## 4. Stronger canonical-mask symmetry break

The universal-OR problem is invariant under every permutation of its eleven
coordinates.  The symmetric group on eleven coordinates acts transitively on
the 6-subsets.  Therefore, if a solution has one distinct literal rank-six
mask `S`, a coordinate permutation maps `S` to the canonical mask

```text
C={0,1,2,3,4,5}, decimal 63.
```

If a solution has no rank-six literal, it already satisfies the canonical
restriction.  Hence, for an existence search, one may impose WLOG

```text
every literal rank-six array entry equals C.         (4.1)
```

For every position `p` and every rank-six mask `S!=C`, add only the mismatch
clause

```text
(OR_(b in S)     -A[p,b])
 OR (OR_(b not in S)  A[p,b]).                       (4.2)
```

Clause (4.2) has **11 literals**, not 12: the selector literal from (3.2) is
absent.  It is false exactly for the forbidden assignment `A[p]=S`.

The exact inventory is

```text
new variables: 0,
clauses:       465*(462-1)=214365,
clause length: 11,
literal occurrences: 2358015.
```

This saves, relative to the selector-AMO design,

```text
923 variables,
1847 clauses,
222709 literal occurrences.
```

No clause forces `C` to occur.  Thus arrays with no rank-six entries remain
admitted, as required.

### 4.1 Exact scope of the symmetry argument

The canonical gate is not a coordinate-labelled necessary condition: a
labelled solution whose sole literal mask is `S!=C` violates it.  It is a
satisfiability-preserving WLOG symmetry break.  It is safe only when the rest
of the hard CNF is coordinate-equivariant, or when all other hard symmetry
breaks are permuted compatibly.

The inspected `k11_forest_sat.cpp` snapshot (SHA-256
`31cb278b5e4e5741d7d9c0ee8eee48f902a177536d44861b1aa408b8626707d7`)
has coordinate-equivariant hard constraints:

* direct and central targets enumerate complete ranks;
* subset-cardinality clauses enumerate all coordinate subsets uniformly;
* band, joint-band, adjacent-shadow, rank-three, and endpoint-alignment cuts
  depend on ranks, endpoint positions, and widths rather than distinguished
  coordinate labels; and
* the input seed affects `solver.phase(...)` calls only, not hard clauses.

Consequently the canonical gate is safe for the current formula.  If a future
version fixes another mask as a hard symmetry break, transitivity must be
rechecked under the stabilizer of that earlier mask.  For example, after a
rank-five set is fixed, rank-six sets split into orbits according to their
intersection size with it, so two independent canonical choices would not in
general be safe.

For phase quality, a seed with a unique literal rank-six mask should be
coordinate-permuted so that this mask becomes `63`.  If the seed has no such
entry, it needs no change.  A seed with several distinct rank-six entries is
inconsistent with the new theorem, but because a seed supplies phases rather
than clauses it still cannot remove a satisfying solution.

### 4.2 Optional schedule anchoring, proved but not implemented

When the canonical gate and `JointBandCutPlan` are both enabled, let `e` be
the joint plan's exact indicator `x0` for a selected rank-six singleton.
The following additional implication is satisfiability-preserving:

```text
A[p]=63 -> e,  for every physical position p.        (4.3)
```

It uses one 12-literal clause per position: the eleven mismatch literals for
mask `63`, followed by `e`.  Its exact inventory would be

```text
new variables: 0,
clauses: 465,
literal occurrences: 5,580.
```

To prove the existential schedule coupling, start with a solution containing
a literal rank-six mask.  The canonical symmetry break relabels that mask as
`63`.  Select its singleton occurrence as the witness for target `63`, and
select witnesses for all other rank-six masks arbitrarily.  No other selected
rank-six witness can contain this position: its OR would contain the 6-set
`63`, and an equal-rank OR containing `63` must equal `63`, whereas only one
witness is selected for that target.  Therefore the reselected equal-rank
family remains nonnested and, when sorted, has the usual monotone band with
`e=x0=1`.

The lower witness family can be chosen independently.  The band, joint-band,
adjacent-shadow, rank-three-shadow, and endpoint-alignment theorems used by
the current solver apply to every such independently chosen pair of central
witness families (with their existential exception-slot choices rerun after
reselection).  Hence the full auxiliary schedule can be rebuilt around the
singleton choice.  If no rank-six literal occurs, (4.3) is vacuous.

Conversely, `e=1` already means the selected upper schedule contains a
singleton.  Its central value has exact rank six, and the canonical gate
forces its physical entry to be `63`.  Thus under the canonical gate, `e` is
equivalent to the existence of a literal rank-six entry.

This anchoring is proved for the current universally quantified structural
cuts, but is deliberately **not implemented** in the present patch.  It
should be guarded by both the canonical-entry and joint-band options.  If a
future auxiliary restriction is only WLOG for one preselected schedule rather
than for every reselected family, composition must be re-audited first.

## 5. A companion short-pool theorem

The same audited framework yields another compact necessary cut in every odd
dimension.

Let

```text
k=2r+1,
M=C(k,r)=C(k,r+1),
n=M+d,
L=sum_(s=1)^(r-1) C(k,s).
```

Choose one witness for every mask through rank `r+1`, and let `x_j` count
selected rank-`r+1` witnesses of width `j`.  Suppose `x0<=1`, as supplied by
the upper-singleton theorem in the finite cases of interest.  Put

```text
C_d(n)=sum_(ell=1)^d (n-ell+1)
      =d*n-d*(d-1)/2.
```

### Theorem 1 (short-pool cut)

Every candidate satisfies

```text
x_d >= L+2*M-C_d(n)+(d-1)*x0.              (5.1)
```

### Proof

Every rank-at-most-`r-1` target has a witness of physical length at most `d`:
an interval of length at least `d+1` contains a selected rank-`r+1` witness
and therefore has OR rank at least `r+1`.  This contributes `L` distinct
short physical intervals.

Every selected rank-`r` witness also has length at most `d`, contributing `M`
more.  Finally, precisely `M-x_d` selected upper witnesses have width at most
`d-1`, hence length at most `d`.  All these intervals are distinct because
their OR masks are distinct, both within and across ranks.  Therefore the
short-interval pool already contains

```text
L+M+(M-x_d)=L+2*M-x_d
```

chosen witnesses.

If `x0=1`, let `[p,p]` be the selected upper singleton witness, with value
`S` of rank `r+1`.  For each length `ell=2,...,d`, choose any physical
length-`ell` interval containing `p`; one exists even when `p` is an endpoint
of the array.  These `d-1` intervals are distinct by length.  None can be one
of the counted witnesses:

* its OR contains `S`, so it cannot represent a target of rank at most `r`;
* if its OR has rank `r+1`, it must equal `S`, but the selected witness for
  target `S` is already `[p,p]`, and only one witness was selected per target;
* if its OR has larger rank, it is not one of the selected upper-middle
  witnesses either.

Thus `d-1` further physical short intervals are unusable by the counted
witness set.  When `x0=0` there is no extra term.  Since `x0` is zero or one,

```text
C_d(n) >= L+2*M-x_d+(d-1)*x0,
```

which rearranges to (5.1).  The proof works at both physical boundaries and
does not double-count intervals.

### 5.1 Exact values at `B(k)`

| `k` | `d` | `C_d(M+d)` | base bound on `x_d` | bound if `x0=1` |
|---:|---:|---:|---:|---:|
| 7  | 2 | 73      | 25     | 26 |
| 9  | 2 | 255     | 126    | 127 |
| 11 | 3 | 1,392   | 93     | 95 |
| 13 | 3 | 5,154   | 657    | 659 |
| 15 | 3 | 19,311  | 3,507  | 3,509 |
| 17 | 3 | 72,936  | 16,909 | 16,911 |
| 19 | 3 | 277,140 | 77,381 | 77,383 |

For `k=9`, the `x0=1` branch would require `x_2>=127>M=126` and is therefore
impossible.  Hence every optimal k=9 witness selection has `x0=0`, and all
126 selected upper witnesses have width two.

For k=11, the immediately useful solver cut is

```text
x3 >= 93+2*x0.
```

This is a selected-band profile cut and is logically separate from the
array-level canonical-mask gate.

## 6. Machine check

The small exhaustive checker

```text
scratch/verify_k11_upper_literal_mask_cut.cpp
```

uses the four-coordinate rank-two analogue and verifies all two-entry words.
It existentially projects the selector and sequential variables and proves
by exhaustion that both AMO and exact-one accept exactly the words containing
at most one distinct literal middle-upper mask.  It separately enumerates all
coordinate permutations and checks that the canonical-mask gate accepts one
orbit representative exactly for the same words.  It also checks transitivity
on every mask of the test layer and asserts the exact k=11 inventories.

Compile with

```text
g++ -O3 -std=c++20 -Wall -Wextra -pedantic \
    scratch/verify_k11_upper_literal_mask_cut.cpp \
    -o verify_k11_upper_literal_mask_cut
./verify_k11_upper_literal_mask_cut
```

The expected output is

```text
small_selector_projection=PASS
small_exact_one_projection=PASS
small_canonical_orbit_projection=PASS
k11_selector_variables=923 clauses=216212
k11_exact_one_variables=923 clauses=216213
k11_canonical_variables=0 clauses=214365
```

## 7. Recommendation

For the current fully coordinate-equivariant k=11 existence formula, use the
canonical mask `C=63` and the 214,365 zero-variable clauses (4.2).  Keep it
behind its own environment guard and print the exact clause delta.  Before
combining it with any future coordinate-labelled hard symmetry break, audit
the joint stabilizer action.

The selector-AMO version remains the robust fallback: it is a genuine
coordinate-labelled necessary cut, composes with arbitrary hard constraints,
and still adds fewer than one thousand variables.
