# A uniform double-hole marked-profile regrouping actuator

Date: 2026-08-01

Status: unconditional age-composition theorem.  It generalizes the unique
`k=76` mark exchange to every depth and every position of the surviving small
hole.  The operation changes two marked rows, preserves every rank-mark
total, and closes through a directed age cycle of length at most `d+1` once
the stated reservoir profiles are supplied.  It is not a one-copy physical
host theorem.

## 1. The double-hole terminal profile

Fix

```text
d>=3,
r>=d+4,
1<=m<=d-1,
j=d-m+1,
L=r-d-1.
```

Thus `2<=j<=d` and `L>=3`.

Consider the full `d`-mark terminal profile

```text
A_(d,m)=({1,...,d+1}\{m,d}) union {r-1}.       (1.1)
```

Among the first `d+1` deficits it has two holes, at `m` and `d`, while it
retains `d+1` and the extreme top mark `r-1`.

Use the full donor profile

```text
H_d={1,...,d-2,d,d+2}.                         (1.2)
```

Exchange the marks `d+1` and `d` between the two rows.  The new profiles are

```text
A'_(d,m)=({1,...,d}\{m}) union {r-1},          (1.3)
H'_d={1,...,d-2,d+1,d+2}.                      (1.4)
```

The exchange is count-neutral rank by rank.

## 2. The two new age types

Profile (1.3) forces the single-hole terminal type

```text
X_j:
  x_0=1,
  x_1=L,
  x_j=2,
  x_i=1 for every other i>=2.                  (2.1)
```

Profile (1.4) forces

```text
Y=(L-1,1,3,1,...,1),                           (2.2)
```

where the 3 is in coordinate two.

For `1<=p<=j-1`, define

```text
R_p=(L,1,...,1), with coordinate p raised to2. (2.3)
```

The marked profile naturally supported by `R_p` is

```text
K_p={1,...,d+1}\{d-p+1}.                       (2.4)
```

Thus the reservoir requirements are explicit marked rows, not abstract age
types with unspecified payload.

## 3. Uniform regrouping theorem

### Theorem 3.1

The types above form the legal directed cycle

```text
X_j -> Y -> R_1 -> R_2 -> ... -> R_(j-1) -> X_j.   (3.1)
```

Its length is

```text
j+1<=d+1.
```

Suppose a marked-profile law contains `a` paired copies of (1.1)--(1.2),
and after the mark exchanges its type law has the decomposition

```text
pi = sigma + a(e_(X_j)+e_Y+sum_(p=1)^(j-1)e_(R_p)), (3.2)
```

where `sigma` is stationary.  Then `pi` is stationary and has exactly the
same rank-mark totals as the pre-exchange law.

### Proof

The mark statement follows because the operation only exchanges one
`d+1`-mark and one `d`-mark.

For `X_j->Y`,

```text
Y_1=1<=X_0=1,
Y_2=3<=X_1=L,
Y_i=1<=X_(i-1) for i>=3.
```

For `Y->R_1`, the only nonunit inequality is

```text
(R_1)_1=2<=Y_0=L-1,
```

which holds because `L>=3`.  Every edge `R_p->R_(p+1)` moves the unique 2
one age to the right, so its only tight nonunit inequality is

```text
(R_(p+1))_(p+1)=2=(R_p)_p.
```

Finally,

```text
(X_j)_1=L=(R_(j-1))_0,
(X_j)_j=2=(R_(j-1))_(j-1),
```

and every other target coordinate is one.  Hence (3.1) is legal.
Uniform mass on this cycle is stationary; adding stationary `sigma` proves
(3.2).  QED.

## 4. Relation to the single-hole completion actuator

The regrouping has a clean two-stage interpretation.

1. The mark exchange turns the double-hole profile (1.1) into the
   single-hole profile (1.3).
2. The excess age token is injected at coordinate one and transported to
   coordinate `j-1`, where it supplies the 2 required by `X_j` on return.

The first stage is impossible using unmarked completion alone, as the exact
`k=76` principal-down-set obstruction proves.  The second stage is the same
age-token transport underlying the earlier single-hole actuator.

## 5. Uniformity and the transport scale

This is one parametric schema valid for every `d`, `m`, and sufficiently
large `r`; it is therefore a genuine bounded *library* result in the sense of
one algebraic move family.

Its cycle length is `O(d)`, not an absolute constant.  Under this interface
that scale is natural.  At `Y`, the only positive-age entry above one is in
coordinate two.  The transition rule can move such excess at most one age to
the right per edge.  Supplying the return requirement in coordinate `j`
therefore needs a source excess in coordinate `j-1` and, absent an additional
prepositioned reservoir excess, requires `Omega(j)` age edges.

This does not cost `O(d)` extra word positions: the cycle reassigns existing
trace occurrences.  It does mean a physical host must reserve and connect an
`O(d)`-type reservoir for a worst-position hole.

## 6. Exact finite confirmations

The first completion-independent systematic failure and the next failure of
the one-profile completion search fit the schema.

### `k=76`

```text
d=5, r=38, m=1, j=5,
A={2,3,4,6,37},
H={1,2,3,5,7},
swap 6<->5.
```

Among 97 eligible minimum transpositions this is the unique stationary hit
in the canonical leading-zero completion face used by the scan.
The actual systematic stock admits an alternative seven-type cycle and an
exact stationary residual.

### `k=89`

```text
d=6, r=45, m=2, j=5,
A={1,3,4,5,7,44},
H={1,2,3,4,6,8},
swap 7<->6.
```

Among 101 eligible minimum transpositions this is again the unique stationary
hit in that fixed completion face.  The new profiles are

```text
{1,3,4,5,6,44},
{1,2,3,4,7,8}.
```

The exact range scan through `k=100` therefore supports the same uniform
rule at two depths and two different hole positions.

## 7. What remains for a fully uniform marked grouping

The theorem is conditional on reservoir stock (2.4).  A general construction
must arrange those profiles jointly with all other rank multiplicities.  It
is not enough that each `K_p` is numerically abundant in the Boolean lattice;
they must occupy distinct physical rows compatible with the one-copy owner
selector.

Profiles with three or more small holes are not covered by this theorem
alone.  They are now covered by the later one-swap theorem
`MATH_THEOREM_MULTI_HOLE_MARK_COLLAPSE_AND_SIDECAR_LOWER_BOUND_20260801.md`.
The exact age-level profile stock is subsequently closed by
`MATH_THEOREM_AGE_LEVEL_CANONICAL_ACTUATOR_STOCKING_20260801.md`.
Occurrence-labelled owner chronology, protected upper/common-cap tickets,
and physical component joining remain open.

## 8. Protected Catalan/pivot coupling

At the quotient level the operation is ideal for the protected host: it
preserves marked rank totals exactly and exports a closed stationary cycle.
Literal coupling still requires:

1. joint selection of the donor rows and all `K_p` reservoir rows;
2. one-copy labelled owner realizations outside the pivot/common-cap bank;
3. preservation of literal upper and compiler tickets on every changed row;
4. protected component switches joining the labelled cycle to the rooted
   Catalan chronology.

For an extreme block of multiplicity `Theta(k)`, this is a `Theta(kd)`
occurrence bank if expanded literally.  It cannot be protected solely by the
existing post-hoc `O(d)` avoidance corollary.  The natural options are a joint
common-basis/actuator selector or an orbit-compressed equivariant lift.

## 9. Scope and artifacts

Proved:

* a rank-count-neutral two-row regrouping for every double-hole profile
  (1.1);
* an explicit stationary cycle of length at most `d+1`;
* the exact recurrence of the rule at `k=76` and `k=89`.

Open:

* stocking all reservoir profiles for arbitrary simultaneous tasks;
* profiles with three or more small holes;
* the one-copy protected physical lift;
* any new upper bound on `nu(k)`.

```text
scratch/probe_systematic_one_move_repair_range_20260801.cpp
62297e09a438c21221e6210b3b383abbc030998fa8d632d415a4c04e711f2aea

scratch/systematic_mark_swap_k3_k100_20260801.out
483bfd9840804b765c173354ad0e3e817da78a2792c6a3ceca5f5f9a36c3d8f3

scratch/systematic_mark_swap_k3_k100_20260801.tsv
a7a71e183302375dbb07d93a3c7ff3d634b8be423ca8ed2046f4cb0b81a4f823

scratch/systematic_mark_swap_k89_20260801.audit.json
33045d3e235c13864694fb8ecc8ec06823761c27fe4033cf210ff7b9f837856d
```
