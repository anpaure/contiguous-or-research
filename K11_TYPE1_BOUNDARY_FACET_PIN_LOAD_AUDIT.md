# Proof and encoding audit: Type-I boundary-facet pin load

## Verdict

**PASS as a theorem and production design.**  In every hypothetical Type-I
`k=11,n=465` word, every five-set `R` has at least 20 supporting positions
inside the unique rank-at-most-four core.  The six facets of the fixed
endpoint value `T=63` can be exposed, reusing existing exact support and rank
literals, with exactly

```text
8,304 variables / 49,788 clauses.
```

No solver source has been edited and this audit makes no SAT/UNSAT claim.

An adversarial recheck made two presentation-only repairs: the finite
checker now includes the tautological `rho>=1` condition when `p>0` (needed
only to make its helper exact at `p=1`), and the theorem note now gives the
correct `11,136`-clause premium for rebuilding each facet support directly
from seven literals.  Neither repair changes the theorem or the main
`8,304 / 49,788` inventory.

## 1. Exact inner-core setup

The separately audited Type-I filtration gives

```text
A = 63 || P_5 || C_4 || Q_5.
```

Deleting the unique rank-six endpoint leaves an exact length-464 rank-five
equality word.  If `z=|P_5|+|Q_5|`, then

```text
m=|C_4|=464-z,
q=462-z=m-2
```

nonliteral rank-five targets may be assigned selected witnesses wholly in
`C_4`.  The targets are distinct, so the selected intervals are pairwise
noncontaining and have increasing left and right endpoints.  The local
segment slack is exactly two.

The same filtration theorem says `C_4` itself covers every nonempty target of
rank at most four.  Thus the later use of all 30 proper nonempty subsets of a
five-set is justified wholly inside `C_4`; it does not accidentally use a
literal rank-five boundary cell.

## 2. Why long support runs force distinct witnesses

Index `C_4` locally as `1,...,q+2`.  Order the selected rank-five intervals
as `I_1,...,I_q`.  The endpoint-slack normal form gives

```text
I_i subseteq [i,i+2].                                  (2.1)
```

If `J=[a,b]` has length `L>=3`, then for every

```text
i=a,...,b-2
```

equation (2.1) gives `I_i subseteq J`.  These are exactly `L-2` different
indices and hence `L-2` distinct selected rank-five target values.  Boundary
indices are safe: `b<=q+2` implies `b-2<=q`.

Now fix a five-set `R` and a run on which all entries are contained in `R`.

* A run of length four contains `I_a` and `I_(a+1)`.  Their values are two
  distinct rank-five subsets of `R`, but `R` has only one rank-five subset,
  namely itself.  Contradiction.
* Each run of length three contains one selected rank-five interval whose
  value is `R`.  Two distinct support runs are disjoint, so the selected
  intervals they contain are distinct physical intervals and therefore have
  distinct selected target names.  They cannot both have name `R`.

This explicitly rules out the possible loophole that two length-three
windows might merely contain the same selected witness.  That can happen for
overlapping length-three windows inside a hypothetical length-four run, but
the length-four argument uses the two guaranteed distinct indices `a,a+1`
and rules the run out first.  Distinct maximal support runs are disjoint, so
one selected interval cannot lie in both.

Hence every support run has length at most three and at most one run has
length three.

## 3. Proper-subset witnesses really have length at most two

Let `S` be a nonempty proper subset of `R`.  Since `|S|<=4`, Type-I
boundary--core rigidity supplies a witness `J subseteq C_4` with OR `S`.
If `|J|>=3`, Section 2 puts a selected rank-five witness inside `J`.  Its
rank-five value would be contained in `U(J)=S`, impossible.  Therefore every
one of the 30 proper targets has a witness of length one or two inside an
`R`-support run.

Different target values require different physical cells.  If the support
run lengths are `g_1,...,g_rho` and `p=sum g_j`, the number of singleton and
adjacent-pair cells is

```text
sum_j (g_j+(g_j-1)) = 2p-rho.                          (3.1)
```

The run restrictions give `p<=2rho+1`, so
`rho>=ceil((p-1)/2)`.  At `p<=19`, the right side of (3.1) is at most 29.
This cannot hold 30 distinct labels.  Thus `p_R^C>=20`.

The checker records an exact partition of the 30 proper masks of `B_5` into
ten gadgets `X,Y,X union Y`.  Consequently 20 positions in ten separated
two-cell runs attain the cell count, so the constant 20 cannot be improved
by this support-run argument alone.

## 4. Six endpoint facets and gate semantics

For `T=63` and `b in T`, a suffix position belongs to the support of
`R_b=T\{b}` inside `C_4` exactly when all three conditions hold:

```text
support_T[i], !A[i,b], !rank5[i].                      (4.1)
```

The Type-I suffix rank cap makes `!rank5[i]` equivalent to rank at most four;
the one-component theorem then identifies these positions with `C_4`.
The four clauses

```text
!y or support_T
!y or !A[i,b]
!y or !rank5[i]
y or !support_T or A[i,b] or rank5[i]
```

define (4.1) bidirectionally.  The checker exhausts all 16 truth assignments.

## 5. Frozen counter and comparator inventory

There are `6*464=2,784` three-input gates, each using one variable and four
clauses:

```text
2,784 variables / 11,136 clauses.
```

The production Wallace algorithm for 464 equal-weight inputs performs 452
compressor full adders.  The residual rows occupy eight weights, so the final
ripple uses eight more full adders and retains its ninth carry bit.  Thus one
counter uses exactly

```text
460 full adders = 920 variables / 6,440 clauses.
```

Six counters use `5,520/38,640`.  The direct first-difference encoding of
`count>=20` emits one clause for each set bit of `20=10100_2`, hence two
clauses per counter and twelve total.  The checker independently simulates
the Wallace bucket populations and exhausts all 512 nine-bit comparator
inputs.

Adding the three rows gives

```text
variables = 2,784+5,520 = 8,304,
clauses   = 11,136+38,640+12 = 49,788.
```

The count assumes that `support_T` and the true constant are retained from
the already-enabled six-subcube plan; retaining that existing vector changes
no clauses or variables.

## 6. Nonredundancy scope

The checker verifies the displayed abstract ledger in the theorem note:

```text
entry ranks = (11,45,110,258,40,1),
y=(40,284,138), x=(1,42,284,135), z7=(0,4,42,284).
```

It passes the current cumulative rank, local moment, joint width, named-cell
width, and rank-seven truncated-width rows.  Six-subcube counts

```text
32, 44 repeated 406 times, 43 repeated 55 times
```

sum to the exact rank-six moment 20,261 and have zero unrestricted run
charge.  Yet scalar support counts do not restrict an intersection with one
facet of `T`; that facet support can be declared below 20.  This is a strict
separation from the current *scalar ledger*, not a purported assignment to
the full interval-OR CNF.  The base CNF already implies every valid theorem;
the proposed module exists to expose this otherwise distributed consequence.

## 7. Outer-rectangle scope

At the outer rank-six peel there is one boundary cell, not two variable
boundary chains.  Its crossing-complement formula is

```text
([11]\T) intersect E_j,
```

a single threshold chain.  Residual coordinate lex fixes it to the six
canonical prefix masks already handled by
`K11_FOREST_TYPE1_PREFIX_CHAIN`.  No second loss-chain or rectangle circuit
is mathematically available there.  The new facet rows arise at the inner
rank-five peel, where the coordinate-complete `C_4` and its two literal
rank-five boundaries create new pin load.

## 8. Artifacts

The independent arithmetic/circuit checker is

```text
scratch/check_k11_type1_boundary_facet_pin_load.py
```

and reports

```text
support-run capacity p<=19 -> at most 29 cells: PASS
sharp 20-position V-gadget partition: PASS
three-input support gate and >=20 comparator: PASS
464-input Wallace count: 452+8=460 full adders: PASS
scalar-ledger strictness witness: PASS
encoding inventory: 8304 variables / 49788 clauses: PASS
```
