# Multi-hole mark collapse and the physical-sidecar lower bound

Date: 2026-08-01

Status: unconditional age-composition theorem for the canonical multi-hole
terminal family.  One count-neutral mark exchange collapses an arbitrary
number of small holes to one, and an explicit reservoir of at most `d+1` age
types closes the Strassen circulation.  A separate lower bound proves that
an extreme block of multiplicity `Theta(k)` cannot be repaired by an `O(1)`
literal sidecar; its reservoir must come from existing host occurrences or a
symmetry-compressed joint construction.

## 1. Canonical `q`-hole terminal profiles

Fix

```text
d>=3,
q>=2,
1<=m<=d-1,
r>=d+q+2.
```

Put

```text
j=d-m+1,
L=r-d-1.
```

Consider the full terminal profile

```text
A_(q,m)
 = ({1,...,d-1}\{m}) union {d+q-1,r-1}.       (1.1)
```

Among the integers `1,...,d+q-1`, it omits exactly

```text
m,d,d+1,...,d+q-2,
```

so it has exactly `q` small holes.

Use the donor profile

```text
H_q={1,...,d-2,d,d+q}.                         (1.2)
```

Both profiles have exactly `d` marks.

## 2. One swap removes `q-1` holes

Exchange marks

```text
d+q-1 <-> d
```

between (1.1) and (1.2).  The resulting profiles are

```text
A' = ({1,...,d}\{m}) union {r-1},              (2.1)
H' = {1,...,d-2,d+q-1,d+q}.                    (2.2)
```

Thus the bad row goes directly from `q` holes to one hole in a single
two-row mark exchange.  Every marked-rank total is preserved exactly.

The two forced age types are

```text
X_j:
  x_0=1,
  x_1=L,
  x_j=2,
  x_i=1 for every other i>=2,                  (2.3)

Y=(L-q+1,1,q+1,1,...,1).                       (2.4)
```

The fresh class of `Y` is positive because `r>=d+q+2` gives `L-q+1>=1`.

## 3. The uniform multi-hole cycle

For `1<=p<=j-1`, define

```text
R_p=(L,1,...,1), with coordinate p raised to2. (3.1)
```

Its marked profile is

```text
K_p={1,...,d+1}\{d-p+1}.                       (3.2)
```

### Theorem 3.1 (multi-hole collapse actuator)

The types (2.3)--(3.1) form the legal directed cycle

```text
X_j -> Y -> R_1 -> R_2 -> ... -> R_(j-1) -> X_j.   (3.3)
```

Its length is `j+1<=d+1`, independent of the number `q` of holes.

Consequently, if after the mark exchange a type law decomposes as

```text
pi = sigma + a(e_(X_j)+e_Y+sum_(p=1)^(j-1)e_(R_p)), (3.4)
```

with stationary `sigma`, then `pi` is stationary and has the same rank-mark
marginals as the pre-exchange law.

### Proof

Mark balance is immediate from the two-row exchange.

For `X_j->Y`, the only nonunit inequality is

```text
Y_2=q+1<=X_1=L,
```

which is exactly `r>=d+q+2`.  For `Y->R_1`,

```text
(R_1)_1=2<=Y_0=L-q+1,
```

under the same hypothesis; all later target coordinates are one and are
bounded by `Y_1=1`, `Y_2=q+1`, or another one.

Each `R_p->R_(p+1)` shifts the unique 2 one coordinate right.  Finally,

```text
(X_j)_1=L=(R_(j-1))_0,
(X_j)_j=2=(R_(j-1))_(j-1),
```

and the other target coordinates are one.  Thus (3.3) is legal.  Uniform
mass on a directed cycle is stationary, proving (3.4).  QED.

## 4. Why this is stronger than iterative hole removal

A naive scheme would remove one hole per donor and use `O(qd)` reservoir
types.  The high-mark exchange above removes all `q-1` excess holes at once.
The reservoir size stays `O(d)`:

```text
two regrouped types + (j-1) transport types <= d+1 types.
```

The number of holes affects only the size `q+1` of the temporary age-two
class in `Y`; the transition immediately converts the unused excess into the
larger fresh class of `R_1`.

This is the sought bounded parametric library for the entire canonical
multi-hole family.

## 5. Exact finite frontier

The first profiles with three excess holes appear in the exact scan at
`k=121` and `k=123`.

At `k=121`, the zero-fill dead type is

```text
(1,51,3,1,1,2,1,1),
```

but a one-profile completion repair still exists.

At `k=123`,

```text
d=7, r=62, q=3, m=2,
A={1,3,4,5,6,9,61}.
```

Neither the one-profile completion search nor any of 156 two-row one-mark
swaps against the *existing systematic donor profiles* succeeds.  The
uniform theorem prescribes the missing jointly designed donor

```text
H_3={1,2,3,4,5,7,10}
```

and the exchange `9<->7`, producing

```text
{1,3,4,5,6,7,61},
{1,2,3,4,5,9,10}.
```

Thus `k=123` does not refute the actuator.  It proves that the donor/reservoir
bank cannot be expected to emerge automatically from the fixed systematic
grouping; it must be selected jointly.

The symbolic O3 checker replayed 51,975 parameter instances and 676,725 age
arcs for `d<=32`, `q<=8`.  The proof itself has no such bounds.

## 6. A physical-sidecar lower bound

The quotient repair is internal; it does not say that a short appended block
can supply the required literal occurrences.

### Proposition 6.1 (deficit-mass edit bound)

Let `Delta` be a Strassen down-set with deficit

```text
P_*pi(Delta)-Q_*pi(Delta)=a>0.                 (6.1)
```

Changing one age occurrence changes the left side of (6.1) by at most two:
one unit from its `P` indicator and one from its `Q` indicator.  Therefore
every repair changes at least

```text
ceil(a/2)                                      (6.2)
```

age occurrences.  If the old offending source occurrences are retained and
only new compatible target occurrences are supplied, at least `a` target
occurrences are necessary.

### Proof

For one type `c`, its contribution to (6.1) is

```text
1[P(c) in Delta]-1[Q(c) in Delta],
```

which lies in `{-1,0,1}`.  Replacing one occurrence changes this contribution
by at most two.  This proves (6.2).  Under source retention the first
indicator cannot decrease, so every new target occurrence improves the
deficit by at most one.  QED.

### Corollary 6.2 (no `O(1)` local sidecar)

An edit of `s` physical letters can alter at most `s(d+1)+O(d)` depth-`d`
windows: only windows crossing an edited position or one of the two splice
boundaries can change.  Hence a local sidecar repairing deficit mass `a`
requires

```text
s = Omega(a/d).                                (6.3)
```

For the extreme systematic blocks, `a=k`.  Since `d=Theta(sqrt(k))`,

```text
s=Omega(sqrt(k)).                              (6.4)
```

Thus no absolute-size literal sidecar can carry the terminal Strassen repair.

The explicit cycle (3.3) with mass `a` uses `a(j+1)` type occurrences, at
most `a(d+1)` and worst-case `Theta(ad)`.  Those occurrences must be drawn
from the existing `W`-scale host or selected as a symmetry orbit; they cannot
be appended as an `O(1)` dedicated block.

This lower bound concerns physical support, not extra optimal length.  The
explicit bank uses `a(j+1)=O(ad)` existing owner occurrences, and this is
`Theta(ad)` only in the long-path extreme `j=Theta(d)`.  Such reassignment
may still use only `B(k)+O(1)` positions.

## 7. Coupling to the protected Catalan/pivot host

The correct architecture is now forced.

1. Select the marked bad, donor, and `K_p` reservoir profiles jointly with
   the Catalan owner/common-basis object.
2. Realize their age-cycle edges on one-copy labelled owners outside the
   pivot's named ticket bank.
3. Preserve literal upper and common-cap payloads during the mark exchanges.
4. Join the labelled cycle components into the rooted chronology using
   protected component switches.

Post-hoc fixed-`O(d)` common-basis avoidance cannot supply the worst-case
`O(kd)` occurrence bank (which is `Theta(kd)` when `A=Theta(k)` and
`j=Theta(d)`).  Two viable forms remain:

* a joint occurrence-labelled common-basis/actuator selector; or
* an equivariant quotient in which the `k` extreme copies form one orbit,
  followed by a literal orbit lift.

The quotient theorem supplies the exact mark and age arithmetic needed by
either route.  One-copy rounding and protected payload correlation remain the
open rows.

## 8. Scope and artifacts

Proved:

* one two-row exchange collapses every canonical `q`-hole profile to one
  hole;
* an explicit stationary reservoir of at most `d+1` age types;
* a lower bound excluding an `O(1)` literal sidecar for extreme deficit mass.

Not proved:

* global stocking of all donor and reservoir profiles;
* noncanonical multi-hole profile families;
* the one-copy protected Catalan/pivot lift;
* an additive upper bound for `nu(k)`.

```text
scratch/audit_multi_hole_mark_collapse_actuator_20260801.cpp
80e9cbc91874ce61996c82c33bb90777bb1ed7eb0f933f1cca7a8bad3187f761

scratch/systematic_mark_swap_k3_k125_20260801.out
98ec5a07492356e60f3042f6d719def764e5d76fac912658f2e4350c54ce6ebc

scratch/systematic_mark_swap_k3_k125_20260801.tsv
98cbffd2a81d2346545b9429db8b7357bf4494b759f4c09c194471fcf3322358

scratch/multi_hole_mark_collapse_20260801.audit.json
23607b77b20c995aa207102e375912ddc6a4f4484d86a4fd89350d18ef3a0f67
```
