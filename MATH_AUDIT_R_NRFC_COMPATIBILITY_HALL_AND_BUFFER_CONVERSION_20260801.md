# Independent audit: NRFC compatibility, Hall cuts, and buffer conversion

Date: 2026-08-01  
Lane: R, one-copy sequel to aggregate rotor rounding  
Verdict: **PASS**

Audited results:

```text
MATH_THEOREM_R_NRFC_LABELLED_COMPATIBILITY_HALL_AND_OWNER_SYMMETRY_LIMIT_20260801.md
MATH_THEOREM_R_NRFC_OWNER_COMPATIBILITY_AND_LINEAR_BUFFER_OBSTRUCTION_20260801.md
MATH_THEOREM_R_PRIMITIVE_MIXED_ROTOR_SHARP_BUFFERED_ONE_COPY_LIFT_20260801.md
```

## 1. Literal transition counts

For compatible positive types `c,c'`, put

```text
delta_i=c_i-c'_(i+1)       (0<=i<d).
```

A literal transition satisfies

```text
C'_(i+1)=C_i-C'_0.
```

For a fixed source partition, choose `delta_i` reset elements from every
young cell and then choose the remaining `c_d` source-letter elements from
the old terminal cell together with the `k-r` outside coordinates.  Thus

```text
D^+=C(k-r+c_d,c_d) prod_(i<d) C(c_i,delta_i).
```

Reversing the construction partitions `c'_0-c_d` target-source elements
into the reset cells and then chooses the old terminal cell.  Hence

```text
D^-=C(k-r+c_d,c_d)
     c'_0!/[c_d! prod_(i<d)delta_i!].
```

Substitution into

```text
|Omega_c|=k!/[(k-r)! prod_i c_i!]
```

gives `|Omega_c|D^+=|Omega_c'|D^-`.  Therefore every complete labelled
layer obeys the normalized Hall inequality

```text
|N(S)|/|Omega_c'| >= |S|/|Omega_c|.
```

This calculation is exact and occurrence-labelled.

## 2. Owner projection and its limit

For a fixed source state with owner `T`, the possible next owners are
exactly

```text
(T-D) union E,
D subseteq C_d, E subseteq [k]-T, |D|=|E|.
```

Only terminal coordinates can leave; this is a terminal-star, not an
arbitrary Johnson ball.  For fixed owners at Johnson distance `t`, a pair
exists iff `t<=c_d`, with exact multiplicity

```text
(r-t)!/[(c_d-t)! prod_(i<d)c'_(i+1)! prod_(i<d)delta_i!].
```

Static role-to-owner matching is consequently trivial under full symmetry,
and every single rank separately has an owner SDR.  Neither statement
selects a common nested flag or a cyclic state-consistent section.

For a chosen one-state-per-owner, exact-target transversal `X`, a successor
cycle cover exists iff

```text
|N^+(A) intersect X|>=|A|             for every A subseteq X.
```

Equivalently its deficiency is

```text
delta(X)=max_A (|A|-|N^+(A) intersect X|).
```

This is an ordinary bipartite min-cut only after `X` is fixed.  Jointly
choosing `X` consumes one owner and several nested target resources per
state, so complete-layer biregularity does not prove it.  The exact open
selection theorem is OFHT, equivalent to multiple-cycle NRFC.

## 3. Infinite multiplicity-one obstruction

For every `d>=2,K>=0`, the reciprocal type pair

```text
(K+1,2,1,...,1) <-> (K+2,1,1,...,1)
```

has no two-state literal cycle, even with different owners.  If the states
are `X,Y`, the first transition gives

```text
|X_0 intersect Y_0|=K,
```

and the return gives `X_1=Y_0-X_0`.  Hence
`Y_2=X_1-Y_0` is empty, contradicting its required singleton size.  Both
complete transition layers nevertheless satisfy normalized Hall, and the
owner projection permits reciprocal adjacent-owner moves.  This is a
literal common-section obstruction, not an owner scarcity.

Likewise a formal positive-age type self-loop is not a one-state labelled
loop: `X->X` would force `X_1=X_0-X_0` empty.  Thus the conductor's formal
unit buffers are not themselves physical unit cycles.

## 4. Sharp buffered repair

For `s=r-d>=2`, the primitive adjacent-buffer generator has types

```text
P=(s-1,2,1,...,1),       H=(s,1,...,1).
```

Every owner-simple depth-`d` cyclic component containing a source of size
below `r` has length at least `d+2`: for period at most `d+1`, every owner
window contains all period letters and all owners coincide.  Therefore one
primitive pair requires at least `d` additional occurrences, regardless of
their types.

The bound is attained by the explicit source cycle

```text
S_0=G+{w},
S_i=G+{b,v_i}       (1<=i<=d+1),       |G|=s-2.
```

It has one `P` state and `d+1` `H` states, exact literal recurrence, and
owners equal to the `d+2` distinct facets of the `(r+1)`-set
`G+{b,w,v_1,...,v_(d+1)}`.  Its prescribed primitive marks plus `d` short
low-buffer patterns have the exact aggregate signature; at every rank the
marked prefixes are distinct cyclic private-tag intervals.

Unbuffered, the exact primitive multiplicity is

```text
ceil((d+2)/2).
```

The alternating common-core word `(PH)^m` gives the upper bound at this
value; the total-length inequality gives the lower bound.

Thus two extra buffer occurrences repair the smallest `d=2` case, but fail
for every `d>=3`.  There is no dimension-independent local private-buffer
conversion.  The Ferrers banks are large enough to pay the `Theta(d)` local
tax, but selecting globally disjoint owner facets and prescribed residual
targets is precisely the still-open OFHT/NRFC packing problem.

No finite computation is used in these results.
