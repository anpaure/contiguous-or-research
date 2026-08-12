# Independent-boundary Boolean absorbers

Date: 2026-07-31  
Status: exact all-`m` local theorem for endpoint distance at least three;
exhaustive orbit audit through `m=7`; no robust packing theorem

## 0. Verdict

The fixed-filler absorber can be strengthened in precisely the direction
needed by a critical reserve.  Let

```text
L in C([2m],m-1),     U in C([2m],m+1),
s = |L-U|.
```

If `s>=3`, then **any** prescribed Boolean diamond above `L` and **any**
prescribed Boolean diamond below `U` are the two boundary edges of one
alternating-path absorber.  Its off state covers exactly the internal outer
vertices; its on state covers the same vertices together with `L,U`; and in
each state every physical rank-`m` endpoint is distinct.  The support path
has at most `2m+1` edges.

Thus the common-filler obstruction in the first absorber is not intrinsic:
at distance at least three the start and end resource pairs are completely
independent.  This is still a local theorem.  It neither packs many gadgets
resource-disjointly nor correlates a nibble leave with a reserve.

## 1. A collision lemma for a monotone lower path

Let

```text
X_0,X_1,...,X_r in C([2m],m-1)
```

be a Johnson geodesic,

```text
X_(i+1)=X_i-a_i+b_i,
```

where the `a_i` are distinct, the `b_i` are distinct, and the two lists are
disjoint.  Put

```text
Z_i=X_i union X_(i+1)=X_i+b_i.
```

Choose `c_i notin Z_i` and set

```text
V_i=Z_i+c_i.
```

The two alternating edges at `V_i` have middle endpoints

```text
on:   Z_i, C_i=X_i+c_i,
off:  Z_i, D_i=X_(i+1)+c_i.
```

### Lemma 1.1

All on-state middle endpoints are distinct if

```text
c_i != a_(i-1)       (i>=1),
```

and all off-state middle endpoints are distinct if

```text
c_i != b_(i+1)       (i<=r-2).
```

Under the same conditions all `V_i` are distinct.

### Proof

The `Z_i` are distinct.  If `|i-j|>=2`, the rank-`m-1` sets `X_i,X_j`
differ in at least two elements on each side, so no rank-`m` set contains
both.  Hence an auxiliary endpoint based at `X_i` can collide only with an
adjacent `Z`.

The previous union is

```text
Z_(i-1)=X_i+a_(i-1),
```

so `C_i=Z_(i-1)` exactly when `c_i=a_(i-1)`.  Similarly

```text
Z_(i+1)=X_(i+1)+b_(i+1),
```

so `D_i=Z_(i+1)` exactly when `c_i=b_(i+1)`.  An auxiliary endpoint cannot
equal its own `Z_i`, since `c_i` was chosen outside `Z_i`.  These are all
possible middle collisions.

For the outer vertices, nonadjacent `Z_i,Z_j` have union of size at least
`m+2`.  Equality `V_i=V_(i+1)` would force simultaneously
`c_i=b_(i+1)` and `c_(i+1)=a_i`, already excluded by the displayed
conditions.  Thus all `V_i` are distinct.  `square`

There are exactly `m` choices outside each `Z_i`, and at most two are
forbidden.  In particular the fillers can always be chosen when `m>=3`.

## 2. Independent prescribed boundary diamonds

Prescribe a start diamond

```text
U_0=L+{p,q},          p,q notin L,
```

and an end diamond

```text
L_*=U-{r,t},          r,t in U.
```

The desired alternating path will start

```text
L, U_0, X_1
```

and end

```text
L_*, U.
```

### Theorem 2.1 (independent-boundary absorber)

If `s=|L-U|>=3`, there are lower vertices

```text
X_0=L,X_1,...,X_R=L_*
```

and internal upper vertices `V_0=U_0,V_1,...,V_(R-1)` such that

```text
L= X_0,V_0,X_1,V_1,...,V_(R-1),X_R=L_*,U
```

is an alternating inclusion path with the following two matchings:

```text
M^- = {X_(i+1)V_i: 0<=i<R},
M^+ = {X_iV_i: 0<=i<R} union {L_*U}.
```

`M^-` covers every internal outer vertex and neither `L` nor `U`;
`M^+` covers the same internal vertices and both endpoints.  In either
matching all physical rank-`m` endpoints are pairwise distinct.  Moreover
`R<=m`, so the alternating support has at most `2m+1` edges.

### Proof

Choose three distinct elements

```text
a_0,a_1,a_* in L-U.
```

Choose either member of the prescribed start pair and call it `p`; call the
other one `q`.  Put

```text
X_1=L-a_0+p,             X_*=L_*=U-{r,t}.
```

Let

```text
A=X_1-X_*,     B=X_*-X_1,     d=|A|=|B|.
```

The set `A` contains `(L-U)-{a_0}`, so `d>=s-1>=2` and both `a_1,a_*`
belong to `A`.  Since `X_1` and `X_*` are distinct `(m-1)`-sets, their
union misses at least two ground elements.  One is `a_0`; choose

```text
f notin X_1 union X_*,       f != a_0.
```

Choose `b_1 in B-{q}`.  This is possible because `|B|=d>=2`.  Order the
members of `A` and `B` as

```text
a_1, ..., a_*              and              b_1, ...,
```

with `a_1` first and `a_*` last, and form the monotone Johnson geodesic

```text
X_(i+1)=X_i-a_i+b_i        (1<=i<=d),
```

ending at `X_(d+1)=X_*`.  Define

```text
V_0=U_0,
V_1=X_1 union X_2 union {f},
V_i=X_i union X_(i+1) union {a_0}       (2<=i<=d).
```

All displayed sets have the required ranks: `f` and `a_0` are absent from
every lower vertex on the geodesic.  The lower vertices are distinct.  The
internal transition unions

```text
Z_i=X_i union X_(i+1)=X_i+b_i
```

are distinct because `|Z_i intersect X_*|` increases strictly with `i`.
The upper vertices are also distinct.  Namely, `V_1` contains `f` and not
`a_0`; every `V_i` for `i>=2` contains `a_0` and not `f`.  Also

```text
V_0=X_1+{a_0,q},        V_1=X_1+{b_1,f}.
```

Equality here would force `{a_0,q}={b_1,f}`, impossible because
`b_1` is neither `a_0` (it lies in `X_*-X_1`, while `a_0` lies outside
`X_*`) nor `q` (by choice).  Finally, `V_0` contains `a_1` and omits
`b_1`, whereas every `V_i` for `i>=2` contains `b_1` and omits `a_1`.
Every internal upper
vertex contains `a_*` until the last transition union, so it differs from
`U`; the last one still contains `a_* notin U`.

It remains to check the middle resources.  The start diamond contributes

```text
on:  L+p, L+q;                 off: L+p, X_1+q.
```

The first internal transition contributes

```text
on:  Z_1, X_1+f;              off: Z_1, X_2+f,
```

and every later transition contributes

```text
on:  Z_i, X_i+a_0;            off: Z_i, X_(i+1)+a_0.
```

Finally the on state uses `X_*+r,X_*+t`.  The `Z_i` are mutually distinct.
The choice `b_1!=q` prevents `Z_1=X_1+q`.  All resources after the first
internal transition contain `b_1` and omit `a_1`, which separates them from
the start resources.  The `f`-resources contain `f`; all later transition
unions omit it.  The `a_0`-resources contain `a_0`; all internal transition
unions and final resources omit it.  Within either filler family distinct
lower bases give distinct resources.  An `f`-resource cannot equal a final
resource even if `f` is `r` or `t`, because its lower base is not `X_*`.
For the common transition unions, every one before the last misses a member
of `X_*`; the last is `X_*+a_*`, distinct from `X_*+r,X_*+t` because
`a_* notin U`.  These observations exhaust the possible collisions in both
states.

The geodesic length is `d<=m-1`; including the prescribed first transition
gives `R=d+1<=m`.  The two alternating edge sets have exactly the asserted
outer supports.  `square`

## 3. Consequence for critical reserves

For a fixed lower endpoint, its possible boundary middle vertices are the
`m+1` supersets of size `m`; a boundary diamond chooses two of them.  The
same statement holds dually at the upper endpoint.  Theorem 2.1 says that,
for `|L-U|>=3`, one may choose these two boundary pairs independently and
then connect them.

This removes the sharp defect of the fixed-filler construction, where both
boundaries had to use one common coordinate `c`.  It does **not** show that
the internal path can be embedded in sparse unused tail/head pools, nor
that absorbers for many endpoint pairs can be selected resource-disjointly.
The remaining central statement is still a robust packing/correlation
theorem, now for gadgets with independent boundary ports.

## 4. Audits

The exploratory standard-library audit

```text
scratch/probe_variable_boundary_absorber_20260731.py
```

uses exactly the construction above, with exhaustive filler backtracking.
The action of `S_(2m)` on `(L,U)` is determined by `s=|L-U|`, so one
canonical endpoint pair per `s` suffices.  For every prescribed start and
end boundary diamond it obtains:

```text
m=4: s=3             100/100 PASS
m=5: s=3,4           225/225 PASS at each s
m=6: s=3,4,5         441/441 PASS at each s
m=7: s=3,4,5,6       784/784 PASS at each s.
```

The same census intentionally records failures at `s<3`; Theorem 2.1 does
not claim those boundary pairs.  The JSON artifact is

```text
scratch/variable_boundary_absorber_m2_m7_20260731.audit.json.
```

Two independent deterministic audits implement the closed formula in the
proof rather than filler backtracking:

```text
scratch/audit_independent_boundary_absorber_constructive_20260731.py
scratch/audit_boolean_prescribed_boundary_absorber_20260731.py
```

The second checks every prescribed boundary in every canonical distance
orbit through `m=8`, a total of 11,489 instances.  Its retained JSON is

```text
scratch/boolean_prescribed_boundary_absorber_m4_m8_20260731.audit.json.
```
