# Exact residual-pin compression for crossed ranks eight and nine at `k=11`

## Status

This note gives an exact, globally-WLOG replacement for the direct positive-bit
occurrence arrays in ranks eight and nine of the unrestricted
`k=11,n=465` forest solver.  It is mathematically sound, but its most direct
CNF realization trades clauses for variables:

```text
620,138 fewer variables
2,504,298 more clauses
```

after the rank-three reduction.  It should therefore be treated as an
optional experimental guard, not merged into the production solver without
an independent source audit and a remote build/search comparison.

The cheaper propagation-only precursor is
`K11_FOREST_UPPER_ENDPOINT_CUTS.md`.

## 1. Structural input

Choose witnesses for all masks of a fixed rank `s in {8,9}` and for all 462
rank-six masks.  The endpoint theorem gives all but at most six rank-`s`
targets a witness `J=[l,r]` with

```text
a selected rank-six proper prefix [l,x], x<r,
a selected rank-six proper suffix [y,r], y>l.
```

Let their rank-six masks be `C,D`.  The physical intervals are different and
the selected rank-six row is a permutation, so `C!=D`.  Negative target-bit
clauses imply `C union D subseteq S`, and therefore

\[
 |C\cup D|\ge7.                                      \tag{1}
\]

It follows that at most `s-7` target bits remain to be witnessed elsewhere in
`J`.  This is the only cardinality fact used; the construction does **not**
assume `C union D=S`.

## 2. Global endpoint-bit certificates

The adjacent-shadow formula already defines

```text
B[l,d] iff the selected rank-six interval beginning at l is [l,l+d],
E[r,d] iff the selected rank-six interval ending at r is [r-d,r],
```

for `0<=d<=3`.

For every physical endpoint and bit introduce certificates `BL[l,b]` and
`BR[r,b]`.  Only the sound direction is required:

```text
BL[l,b] -> OR_d B[l,d]
BL[l,b] and B[l,d] -> OR(A[l,b],...,A[l+d,b])

BR[r,b] -> OR_d E[r,d]
BR[r,b] and E[r,d] -> OR(A[r-d,b],...,A[r,b]).
```

Thus a true certificate proves that the selected rank-six interval at that
endpoint contains the bit.  Conversely, for completeness, whenever the bit
really occurs in that small interval the certificate may be set true.  No
reverse Tseitin implications are necessary.

There are `2*465*11=10,230` certificate variables.  Across one side there are
465 support clauses per bit and

\[
 465+464+463+462=1854
\]

valid endpoint/length implications per bit.  Both sides therefore use

\[
 2(465+1854)11=51,018                               \tag{2}
\]

clauses.

## 3. One crossed target

For a target `S` of rank `s`, allocate:

* an activation bit and the usual three unary interval arrays selecting `J`;
* claim bits `P_b,Q_b` for every `b in S`;
* `t=s-7` residual pin slots.

The activation bit guards the already-audited proper-prefix/proper-suffix
comparisons.  It also guards all outside-bit clauses on `J`.

The unary left threshold has a unique transition at the selected endpoint.
For every possible `l`, add the one-way implication

```text
P_b and selected-left=l -> BL[l,b].
```

Use the dual implication from `Q_b` to `BR[r,b]`.  Because claims are used only
positively below, these sound directions are sufficient: a model cannot use a
claim unless the corresponding central endpoint interval really contains the
bit, while a genuine array can set every true claim.

Each residual slot `q` has selectors `Y[q,b]` for `b in S` and physical pin
variables `H[q,p]`.  Add

```text
active -> OR_p H[q,p]
H[q,p] -> p is inside J
Y[q,b] and H[q,p] -> A[p,b].
```

No exact-one condition is needed on `Y`: allowing several selected bits is
still sound because the chosen physical pin must contain all of them.
Completeness uses at most one missing bit per slot.

Finally, for every target bit add

```text
active -> P_b OR Q_b OR Y[1,b] OR ... OR Y[t,b].
```

Together with the outside-bit clauses, these clauses prove `OR(J)=S`.

## 4. Six generic exceptions

For each rank allocate six generic exact witness slots, identical to the
already-audited rank-four/rank-seven exception slots.  A target coverage clause
says

```text
crossed-active[S] OR Q[exception 1,S] OR ... OR Q[exception 6,S].
```

One physical exact slot cannot represent two different same-rank targets.
Hence at most six targets can be inactive.  The endpoint theorem supplies a
crossed witness for every other target, establishing completeness without
guessing the exceptional set.

## 5. Exactness theorem

### Soundness

An active target has certified selected rank-six prefix and suffix intervals.
Every claimed central bit really occurs in one of them, and every residual
claimed bit occurs at a selected physical pin inside `J`.  The per-bit coverage
clauses put every bit of `S` into `J`; the guarded negative clauses exclude all
outside bits.  Thus `OR(J)=S`.  Generic slots are ordinary exact witnesses.

### Completeness

Take any universal length-465 array and choose target witnesses.  At most six
rank-`s` witnesses fail to be crossed; place them in the generic slots.  For a
crossed witness let `U=C union D`.  Set `P,Q` on the actual endpoint-mask bits.
By (1), `|S minus U|<=s-7`; assign each missing bit to a different residual
slot and choose one of its actual occurrences inside `J`.  Any unused slot may
leave all `Y` bits false.  All clauses are then satisfied.

Therefore the replacement preserves satisfiability exactly.

## 6. Projected inventory

The old direct layers use

| rank | variables | clauses |
|---:|---:|---:|
| 8 | 843,975 | 1,869,945 |
| 9 | 306,900 | 642,895 |
| **total** | **1,150,875** | **2,512,840** |

The replacement uses:

| category | variables | clauses |
|---|---:|---:|
| 165 crossed rank-eight target records | 311,025 | 3,328,050 |
| six generic rank-eight slots | 40,116 | 117,312 |
| 55 crossed rank-nine target records | 129,910 | 1,410,310 |
| six generic rank-nine slots | 39,456 | 110,448 |
| shared endpoint-bit certificates | 10,230 | 51,018 |
| **total** | **530,737** | **5,017,138** |

The net change is

```text
variables: -620,138
clauses:   +2,504,298.
```

Starting from the real rank-three-compressed forest inventory, the projected
full formula would be

```text
variables = 2,885,308 - 620,138 = 2,265,170
clauses   = 14,360,485 + 2,504,298 = 16,864,783.
```

These are design counts, not yet a generated-CNF inventory.  A standalone
counter should reproduce every category before implementation, and a guarded
real CaDiCaL build must reproduce the final totals.

## 7. Scope

Rank ten is omitted from this replacement because its eleven targets and six
possible exceptions make the straightforward residual-pin encoding larger
than the direct layer.  It should receive only the cheap endpoint propagation
cut.  Rank eleven retains its direct witness.

This compression proves no SAT or UNSAT result.  A SAT model still requires
both independent OR verifiers; an UNSAT claim still requires an archived CNF
and independently checked proof.
