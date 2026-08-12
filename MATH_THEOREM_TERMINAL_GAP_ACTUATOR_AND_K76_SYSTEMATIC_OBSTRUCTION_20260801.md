# A terminal-gap actuator family and the `k=76` obstruction to systematic residues

Date: 2026-08-01

Status: the local actuator theorem is unconditional.  The `k=76`
counterexample is an exact finite theorem with a complete breakpoint and
composition audit.  Together they settle the current “systematic
unit-descent” proposal: a one-parameter cycle library repairs every
single-hole terminal block when the required reservoir stock is present, but
the fixed systematic residue profiles themselves cease to admit *any* age
circulation at `k=76`.  This does not refute the broader Strassen route with a
different marked-profile assignment.

## 1. Age types and marked profiles

Write an age type as

```text
c=(c_0,...,c_d),  c_0>=1,  sum_i c_i=r.
```

Its available positive suffix deficits are the distinct positive values among

```text
c_d,
c_d+c_(d-1),
...,
c_d+...+c_1.
```

A marked profile is compatible with `c` when all of its deficits occur in
this set.  Put

```text
P(c)=(c_0,...,c_(d-1)),
Q(c)=(c_1,...,c_d).
```

The age edge `c->c'` is legal exactly when

```text
Q(c')<=P(c)
```

coordinatewise.

## 2. The single-hole terminal profile

Fix

```text
d>=3,  r>=d+2,  2<=j<=d,
L=r-d-1.
```

Let `C_j` be the composition

```text
(C_j)_0=1,
(C_j)_1=L,
(C_j)_j=2,
(C_j)_i=1 for every other i>=2.
```

Put

```text
m_j=d-j+1.
```

The available marked profile of `C_j` is exactly

```text
A_j = ({1,...,d}\{m_j}) union {r-1}.          (2.1)
```

Thus `C_j` is the canonical terminal-gap type with one missing small deficit
and one extreme top mark.

Remove the top mark and call

```text
H_j={1,...,d}\{m_j}                            (2.2)
```

the donor profile.

## 3. Explicit actuator types

Define

```text
D=(L+1,1,1,...,1).
```

Define `B_j` by

```text
(B_j)_0=L+1,
(B_j)_i=(C_j)_(i+1) for 1<=i<d,
(B_j)_d=0.
```

Equivalently, `B_j` has a 2 in coordinate `j-1`, a zero in coordinate `d`,
and ones in its other positive-age coordinates.  Its full cumulative
suffix-deficit list, with that zero retained, is

```text
{0} union H_j,
```

so its positive available deficit set is exactly `H_j`.  The available
deficits of `D` are all of `{1,...,d}`.  Therefore the same marked donor
profile `H_j` may be completed by either `B_j` or `D`.

For `1<=p<=j-2`, define the reservoir type

```text
R_p=(L,1,...,1), with the p-th positive-age coordinate raised to 2.
```

Every displayed vector is a valid composition of `r` with positive fresh
class.

## 4. Mark-neutral cycle theorem

### Theorem 4.1 (single-hole terminal actuator)

The types above form the legal directed cycle

```text
C_j -> D -> R_1 -> ... -> R_(j-2) -> B_j -> C_j,    (4.1)
```

where the `R` segment is empty when `j=2`.  Its length is

```text
j+1<=d+1.
```

Let `sigma` be any stationary nonnegative type measure and let `a>=0`.  If a
marked-profile construction has type measure

```text
pi_0 = sigma
       + a e_(C_j)
       + 2a e_(B_j)
       + a sum_(p=1)^(j-2) e_(R_p),                 (4.2)
```

and at least `a` of the `B_j` occurrences carry the donor profile `H_j`,
then changing those `a` completions from `B_j` to `D` gives

```text
pi_1=pi_0-a e_(B_j)+a e_D,                          (4.3)
```

which is stationary and has exactly the same marked-profile marginals.

### Proof

For `C_j->D`, every positive coordinate of `D` is one, so

```text
Q(D)<=P(C_j).
```

If `j>2`, the large fresh class `D_0=L+1` permits the 2 in `R_1`.  Each edge

```text
R_p -> R_(p+1)
```

then moves that 2 one age to the right, exactly as the window shift permits.
At the last step for `j>2`, the 2 in source coordinate `j-2` permits the 2
in target coordinate `j-1` of `B_j`; its terminal zero is harmless.  When
`j=2`, this last edge is instead `D->B_2` and is legal because
`(B_2)_1=2<=D_0=L+1`.  Finally

```text
Q(C_j)<=P(B_j)
```

coordinatewise by the definition `B_i=C_(i+1)`.  This proves (4.1).

Both `B_j` and `D` contain the same required profile `H_j`, so (4.3) does not
change any marked deficit count.  Algebraically,

```text
pi_1 = sigma
       + a(e_(C_j)+e_D+e_(B_j)+sum_p e_(R_p)).
```

The parenthesized measure is uniform mass on the directed cycle (4.1), hence
stationary.  Adding it to stationary `sigma` proves the claim.  QED.

### Interpretation

This is a genuine parametric actuator library, not a finite-dimensional
coincidence.  A single missing small deficit is repaired by:

1. one donor-completion change;
2. a right-moving age-2 token;
3. one cycle of at most `d+1` types;
4. no change to the marked rank marginals.

The theorem deliberately includes the reservoir decomposition (4.2).  Merely
having the types present with large total mass does not imply that the
remaining law is stationary after the cycle stock is removed.

The symbolic checker replayed all 1,168,749 parameter triples

```text
3<=d<=96, d+2<=r<=3d+128, 2<=j<=d
```

and all 42,441,047 cycle arcs.

## 5. Exact scan of the systematic residue law

For the systematic profiles with canonical triangular boundary and zero-fill
completion:

* zero-fill is stationary through `k=53`;
* its failures at

```text
54,56,61,63,65,67,69,72,74
```

all admit an exact one-profile completion repair;
* `k=76` is the first scanned dimension with no compatible successor profile
  at all.

The one-profile repairs need not all decompose through the particular stock
in (4.2); the exact flow may use other reservoir cycles.  The theorem and the
scan should not be conflated.

## 6. The `k=76` forced type

At `k=76`,

```text
r=38,
d=5,
h=0,
W=C(76,38)=6,892,620,648,693,261,354,600.
```

The systematic profile

```text
A_*={2,3,4,6,37}                              (6.1)
```

occurs on the exact 76-residue interval

```text
[6762138943837485613791,
 6762138943837485613867).
```

Because (6.1) has all five marks, its age type is forced:

```text
C_*=(1,31,2,1,1,2).                           (6.2)
```

Any legal successor type `Y` must obey

```text
Q(Y)<=(1,31,2,1,1).                            (6.3)
```

Let its five available deficits, with multiplicity and zeros retained, be

```text
u_1<=...<=u_5.
```

Equation (6.3) implies

```text
u_1<=1,
u_2-u_1<=1,
u_3-u_2<=2,
u_5-u_4<=1.                                   (6.4)
```

## 7. Complete profile classification at `k=76`

Exact breakpoint arithmetic gives 38 distinct systematic profiles.  They
are precisely:

```text
{1,2,3,4,6}, {1,2,3,4,7},
{1,2,3,5,7}, {1,2,3,5,8},
{1,2,4,5,t} for t in {8,9,10},
{1,2,4,6,10},
{1,3,4,6,t} for 10<=t<=14,
{2,3,4,6},
{2,3,4,6,t} for 14<=t<=37.                   (7.1)
```

No profile in (7.1) is compatible with a type satisfying (6.3):

* A five-mark profile beginning with 1 would have to equal
  `(u_1,...,u_5)`.  Every such profile in (7.1) has final gap at least two,
  contradicting `u_5-u_4<=1`.
* A five-mark profile beginning with 2 would force `u_1>=2`, contradicting
  `u_1<=1`.
* The only four-mark profile is `{2,3,4,6}`.  Since `u_1<=1`, the one extra
  slot must precede 2, leaving final two deficits 4 and 6, again contradicting
  `u_5-u_4<=1`.

This is a human-checkable proof once the finite classification (7.1) is
known.  The independent C++ audit enumerates all 768 age types satisfying
(6.3) and finds exactly zero compatible type/profile pairs.

## 8. Strassen obstruction theorem

### Theorem 8.1

No completion of the `k=76` systematic residue profiles supports a stationary
age circulation.

### Proof

Every completion law has at least 76 copies of the forced type `C_*`.  Let

```text
Delta={x:x<=(1,31,2,1,1)}.
```

Then

```text
P_*pi(Delta)>=76/W.
```

Sections 6--7 prove that no type compatible with any systematic profile has
its `Q` vector in `Delta`.  Hence

```text
Q_*pi(Delta)=0.
```

But `Q_*pi<=_st P_*pi` requires the reverse inequality on every down-set:

```text
Q_*pi(Delta)>=P_*pi(Delta).
```

Contradiction.  QED.

### Consequence

Completion-only actuator libraries cannot prove the all-dimensional result
while keeping this systematic marked-profile assignment fixed.  At or before
`k=76`, the proof must change the marked profile grouping itself.  The broad
age-composition/Strassen formulation remains viable.

The minimum such change is now known.  Swapping mark 6 from each offending
row with mark 5 from profile `{1,2,3,5,7}` is the unique two-row, one-mark
transposition which restores stationarity, and the modified law splits off an
explicit seven-cycle.  See
`MATH_THEOREM_K76_MINIMAL_MARK_REGROUPING_AND_SEVEN_CYCLE_20260801.md`.

## 9. Exact interface with a protected Catalan/pivot host

The actuator theorem is mark-neutral, which is exactly the right marginal
interface for a protected host: changing `B_j` to `D` preserves every marked
rank demand.  That alone is not enough for a physical OR word.  A valid
coupling to the protected Catalan/pivot programme needs all four of the
following literal interfaces.

1. **Pre-host mark routing.**  The marked-profile selector must avoid the
   `k=76` double-hole block, or perform a count-neutral marked-profile exchange
   before age completion.  This cannot be postponed to unmarked suffix
   completion.
2. **Private owner realization.**  Every actuator-cycle edge must lift to
   distinct owner occurrences outside the pivot collar and outside the named
   Catalan common-basis bank.  Rank symmetry alone does not supply one-copy
   owners.
3. **Protected payload transparency.**  The literal traces used for `B_j`,
   `D`, and the `R_p` reservoir must retain the host's upper-witness and
   common-cap tickets.  Equality of marked rank marginals is not equality of
   literal payloads.
4. **Euler/component splice.**  The labelled lifts of the age cycles must be
   merged into the rooted Catalan chronology by payload-transparent component
   switches, while retaining the pivot's endpoints and residence collar.

Under these four conditions, the cycle replacement (4.3) can be made wholly
outside the protected bank: it changes neither the pivot task nor the marked
lower marginals, and the labelled cycle is state-balanced before it is joined
to the host.  The fixed-bank common-basis avoidance theorem can protect a
fixed `O(d)` actuator bank, but it does not choose these physical owner
representatives or prove the component splice.

Thus the exact surviving combined target is:

> construct a protected Catalan/pivot host together with a non-systematic
> marked-profile selector whose terminal-gap blocks decompose into stocked
> actuator cycles, and round the union in one coloured-Euler selector.

The `k=76` theorem shows why the quantifier “choose the marked profiles first,
then complete them” is too rigid.

## 10. Scope and nonclaims

Proved here:

* the parametric single-hole terminal actuator;
* exact mark-neutrality and cycle length at most `d+1`;
* exact one-profile repair of every zero-fill failure through `k=75`;
* the first completion-independent systematic obstruction at `k=76`.

Not proved here:

* a replacement marked-profile construction for all `k`;
* a bounded physical actuator atlas in one-copy owners;
* a protected Catalan connector or pivot host;
* higher-shadow or common-cap preservation;
* `nu(k)<=B(k)+O(1)` or exact equality.

## 11. Artifacts

```text
scratch/audit_terminal_gap_single_hole_actuator_20260801.cpp
81d4a583b763d514691a17c02b9847b8360b451584f6ebac4bf59e86889d8786

scratch/probe_systematic_one_move_repair_range_20260801.cpp
62297e09a438c21221e6210b3b383abbc030998fa8d632d415a4c04e711f2aea

scratch/systematic_one_move_repair_k3_k76_20260801.tsv
1dcc9899d119a6aa0513ba97a39ec5a3f14eee5981d4e3ef7ac01676cf47c166

scratch/audit_systematic_k76_no_successor_20260801.cpp
41a0c38747a981c9b4b10a38887636383a79d9bcc50342fe581f51f8cb2a96f5

scratch/systematic_k76_no_successor_20260801.out
37ee832cdc02bd7106b81e83fa6e4e1b86fbd68a295695b7fac9415b644f6695

scratch/systematic_k76_no_successor_20260801.audit.json
d32d4aed88be58c3f86298e10d3f579eeb3b33982e55b1c5cd4e0b1c149fbf74
```
