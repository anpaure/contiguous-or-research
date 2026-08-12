# Audit of the age-composition quotient and systematic unit-descent reduction

Date: 2026-08-01

Status: the age-composition quotient and Theorem 3's systematic multiplicity
and gap statements are proof-safe.  The proposed Unit-descent circulation is
still a conjecture.  The claim that only adjacent unit descents remain needs an
endpoint correction: the terminal/top gap is uncontrolled and can be large.

## 1. Age-composition quotient

For a `(d+1)`-letter trace, let `C_i` be the coordinates whose most recent
occurrence has age `i` and put `c_i=|C_i|`.  The proper suffix ranks are

```text
s_j=c_0+...+c_(j-1),  1<=j<=d.
```

For consecutive traces the necessary type inequality is

```text
c'_(i+1) <= c_i,  0<=i<d.
```

It is sufficient: choose the `c'_(i+1)` survivors from `C_i` and refresh all
other coordinates, including `C_d`.  The relation between partitions of two
fixed types is biregular.  Uniformly lifting a balanced type flow therefore
gives a balanced flow on labelled age partitions.  Its directed cycles emit
periodic nonempty letters because every head has `c'_0>0`; the resulting
periodic `(d+1)`-windows are literal de Bruijn edges.  This supplies the one
clarification missing from the informal proof: types are vertices of the
window-shift lift, and the lifted partition cycles, rather than abstract type
cycles alone, produce the literal circulation.

Marks at distinct available suffix ranks are independent.  After owner and
coordinate symmetrization, the usual identity

```text
C(k-s,r-s)/C(r,s) = C(k,r)/C(k,s)
```

gives the required target load.  Consequently Theorem 2 is correct:
`q in ST_(k,r,d)` is equivalent to a normalized circulation on the
`C(r+d-1,d)` age types whose stationary node mass supplies the marked-rank
capacities.

## 2. Exact monotonicity of the deficit counts

Write

```text
n_t = C(k,r-t)-b_(r-t),  1<=t<r.
```

The attachment states that `n_t` is nonincreasing only for sufficiently large
`k`.  In fact it is nonincreasing in every relevant dimension.

For `1<=s<r`,

```text
C(k,s)-C(k,s-1)
 = C(k,s) (k+1-2s)/(k-s+1) >= k-1.
```

For `s=1` this is equality.  For `s>=2`, use `C(k,s)>=C(k,2)`; the last factor
is at least `3/k` when `k` is even and `2/k` when `k` is odd.  On the other
hand `b_s-b_(s-1)<=d<=r-1<k-1` (with absent columns assigned multiplicity
zero).  Hence

```text
n_t-n_(t+1)
 = C(k,s)-C(k,s-1) - (b_s-b_(s-1)) >= 0.
```

Thus no asymptotic qualification or special extreme-tail argument is needed.

## 3. Theorem 3 is correct

The half-open interval `[N_(t-1),N_t)` has length `n_t<=W`, so it contains
each residue modulo `W` at most once and exactly `n_t` residues.  This proves
the multiplicities.  Since the union of these intervals has length at most
`dW`, every residue row has at most `d` marks.

For one nonempty row, its selected integers are exactly

```text
y_i=a+(i-1)W.
```

If `t_i` and `t_(i+1)` are consecutive selected deficits, the earlier block
`[t_(i-1)+1,t_i-1]` has mass below `W`, while the later block
`[t_i,t_(i+1)]` has mass above `W`.  For `i=1`, the earlier block is
`[1,t_1-1]` and has mass at most `a<W`.  Nonincreasing `n_t` then rules out a
later block that is no longer, proving

```text
g_(i+1) >= g_i-1.
```

An exact endpoint scan through `k=1000` finds the first strict descent at

```text
k=18, A={2,3}, gaps=(2,1),
```

and no drop larger than one, as required by the proof.

## 4. The missing endpoint/top inequality

Let a full row have `d` marked deficits

```text
A={t_1<...<t_d},  g_1=t_1,  g_i=t_i-t_(i-1).
```

Its age composition is forced to be

```text
c=(r-t_d, g_d, g_(d-1), ..., g_1).
```

A stationary self-loop requires

```text
g_1<=g_2<=...<=g_d<=r-t_d.                 (top condition)
```

Theorem 3 controls only the first `d-1` comparisons, and only from below by
one.  It gives no bound on the final comparison `g_d<=r-t_d`; upward jumps are
also unrestricted.  For example, the genuine `k=17` systematic profile

```text
A={1,2,8}
```

has harmless internal gaps `(1,1,6)` but forces type `(1,6,1,1)`, far from a
self-loop.  Since the row already has `d=3` marks, no unmarked suffix can be
inserted into that row to split the terminal jump.

More generally, any stationary circulation satisfies the averaged inequalities

```text
E[c_0] >= E[c_1] >= ... >= E[c_d],
```

obtained by averaging `c'_(i+1)<=c_i` under equal head and tail marginals.
These are the forced-top inequalities.  They are not consequences of the
local unit-drop law.  Therefore the accurate residual lemma is:

> Complete the systematic profiles, including their terminal gaps, and find a
> balanced age-type flow satisfying all componentwise transition inequalities.

Calling this solely a “unit-descent” problem hides a separate endpoint supply
condition, although it does not make the conjecture false.

## 5. Finite circulation replay

Two independent H100 audits give positive evidence, not a general proof.

* For every triangular boundary choice at `3<=k<=9`, a row-labelled model
  selects one completion per systematic row and an exact successor permutation
  of the rows.  All cases are SAT; this includes the noncanonical balanced
  `k=6` clock.
* An aggregate integer model allocates every systematic profile occurrence to
  a completed age type and places exactly that integer type mass on both sides
  of a balanced type flow.  It is SAT in every dimension `17<=k<=25`, including
  the forced-top profile `{1,2,8}`, the first strict unit-drop profile `{2,3}`,
  and the later `{1,3,4}` profile.

The aggregate witnesses use between 14 and 38 positive flow arcs.  They are
stronger than fractional membership for those dimensions, but do not prove the
all-dimensional lemma.

A later exact interval audit sharpens this substantially.  Leading-zero
completion passes through `k=53` but has its first Strassen failure at `k=54`:
54 copies of the forced type `(1,21,2,1,1,1)` have no legal target type in the
zero-fill support.  This is only a failure of that completion rule.  Replacing
the leading zero by deficit 8 on 54 occurrences of profile `{1,2,4,7}` gives
type `(19,1,3,2,1,1)` and restores stationarity through an explicit five-type
cycle.  See
`MATH_AUDIT_SYSTEMATIC_ZERO_FILL_K54_STRASSEN_CUT_AND_ONE_PROFILE_REPAIR_20260801.md`.

The completion freedom itself eventually fails.  At `k=76`, profile
`{2,3,4,6,37}` occurs 76 times and forces type `(1,31,2,1,1,2)`.  Of the 768
types reachable from it, none contains any of the 38 systematic profiles.
The principal down-set therefore has positive `P` mass and zero `Q` mass for
every completion.  The systematic marked-profile law, not merely zero-fill,
is impossible there.  The exact actuator theorem and obstruction are in
`MATH_THEOREM_TERMINAL_GAP_ACTUATOR_AND_K76_SYSTEMATIC_OBSTRUCTION_20260801.md`.

## 6. Exact implication to `ST`

The final implication is valid with one wording requirement.  Suppose every
systematic row is completed to an age type containing its marked deficits and
the completed occurrences carry a balanced nonnegative type flow, with equal
incoming and outgoing mass at every type.  Normalize by `W`.  Deficit `t`
then has marked mass `n_t/W=q_(r-t)`.  The age-composition quotient lifts the
flow to a literal invariant circulation, so

```text
q in ST_(k,r,d).
```

A mere ordering of rows, or pairwise legal transitions without balanced type
multiplicities, is insufficient.  The word “circulation” must retain this
equal-marginal meaning.

## 7. Relation to the J6 triangular boundary debt

The `k=17,d=3` J6 continuation census produces one fresh label with each of
the endpoint ages `3,2,1`.  At the age-type level this is the tail

```text
(c_1,c_2,c_3)=(1,1,1),
```

and with the six-coordinate live core it is the self-loop type

```text
c=(6,1,1,1) in C_(9,3).
```

Thus the quotient correctly sees no accumulating scalar defect: the triangular
bundle can circulate forever.  The literal continuation audit simultaneously
shows what the quotient forgets: filling one bundle replaces it by three fresh
private labels of ages `3,2,1`.  No native one-component continuation saturates
the socket.  Literal label identities, topology, upper providers and common-cap
resources remain outside `ST`.

## 8. Corrections to the pull-clock/TPC support claims

The stationary-window inequality, private-label pull clock, triangular atom
formula, and implication `TPC => q in ST` are correct.  Two qualifications are
needed.

1. The span identity directly gives `e_(a+1)-e_(c+j)` for `a<=c-1`.
   The missing `s=c+1` transfers follow by subtracting two transfers through
   `e_c` when `c>=1`; the text should state this.  The `c=0` small boundary case
   is separate.
2. The discrete-convexity calculation is positive for deficit
   `j=r-s>=d+1`.  A general pull block with core size `a` and window length `q`
   produces rank `s=a+q`, whose deficit can be as small as one.  Therefore the
   assertion that all ranks serviced by pull blocks lie in the convex region is
   false unless one explicitly restricts to `a+q<=r-d-1`.  This weakens the
   proposed route to TPC, but not the TPC statement or its implication.

## Artifacts

```text
scratch/audit_systematic_age_composition_circulation_20260801.py
1f11eb254f3d9c26b30faa39f2740b031e2524badc0b8a4191479f3ecd34dafd

scratch/systematic_age_composition_circulation_20260801.audit.json
4a95db78edce7efa025c0319316a7365a53c4e099462000367690f0ad4fe3703

scratch/audit_systematic_age_composition_aggregate_flow_20260801.py
c95554e383498f544e0a6017532e43b5bfdc93298aaa54e6c9b7bf475fedef94

scratch/systematic_age_composition_aggregate_flow_20260801.audit.json
1b16fb920b54c55a2a083fd82164ad9c4f489b83c9ac10d0294d37951ddf9f15
```

All solver-backed checks ran on H100 CPU resources.  They are finite audits;
the all-dimensional Unit-descent circulation remains open.
