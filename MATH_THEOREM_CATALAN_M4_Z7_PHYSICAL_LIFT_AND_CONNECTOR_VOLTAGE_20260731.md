# The two \(m=4\) cyclic repair matchings both have connected physical lifts

Date: 2026-07-31  
Status: exact theorem for the authenticated canonical \(m=4\) repair core;
the voltage-lift lemma is general

## 1. Conventions

Write

\[
[8]=\mathbb Z_7\sqcup\{\infty\},
\]

and let \(\rho\) add one to every finite coordinate and fix \(\infty\).
The source is the complete 21-edge repair core in
`scratch/catalan_m4_mixed_split_fixed_forest_closure_20260731.PASS.json`.
Its SHA-256 is

```text
e8eb60cf8401296d73fa7d39739fb85d70e7f921ecd9661548e2a768cb44f899
```

As proved in
`MATH_THEOREM_CATALAN_M4_Z7_QUOTIENT_REPAIR_CORE_20260731.md`, its three
edge-orbit representatives \((O,D,Z)\) are

\[
E=(29,7,21),\qquad K_0=(149,134,133),\qquad
K_1=(149,193,133).
\]

There are two repair matchings, \(E\cup K_0\) and \(E\cup K_1\).

For each selected occurrence \((O,D,Z)\), let \(t,O,h\) be the literal
tail, omitted facet, and head stored in its repair-core row.  Insert \(O\)
between \(t\) and \(h\) in the frozen 56-facet seam.  In the resulting
70-cycle retain the outgoing edge \(Oh\), and call the incoming edge \(tO\)
a connector.  Thus the 56 retained edges form the physical common
transversal \(F\), while the fourteen connectors form \(C\).

The voltage convention below is important.  A path beginning at
\(\rho^s(0x1d)\) is the copy \(E_s\), and a path beginning at
\(\rho^s(0x95)\) is the copy \(K_s\).  The voltage of a directed connector
from copy \(s\) to copy \(t\) is \(t-s\pmod 7\).  The two individual
voltages depend on this gauge.  Their sum around the directed quotient cycle
does not.

## 2. Exact physical lifts

Both repair matchings lift successfully.

### Choice \(E\cup K_0\)

The repair blocks are

```text
E : 1,9,17,25,33,41,49
K0: 7,15,23,31,39,47,55
```

The reconstructed physical cycle is the already authenticated canonical
70-cycle.  Deleting its fourteen incoming connectors gives a spanning
14-path forest with component profile

\[
7^7 3^7.
\]

The SHA-256 of its comma-separated lowercase hexadecimal word, with no
spaces or newline, is
`403c4b8f04ebfe6d4cadb44b58c897970ab6a1ef904bd0e391752e690eae0976`.

At the component quotient, the two directed connector gains are

\[
E_s\longrightarrow K_{s+3},\qquad
K_s\longrightarrow E_{s+6}.
\]

Hence a two-connector step advances an \(E\)-copy by

\[
3+6=2\pmod 7.
\]

Starting at \(E_0\), the lifted connector cycle is

```text
E0,K3,E2,K5,E4,K0,E6,K2,E1,K4,E3,K6,E5,K1,E0.
```

### Choice \(E\cup K_1\)

The repair blocks are

```text
E : 1,9,17,25,33,41,49
K1: 6,14,22,30,38,46,54
```

This gives a second literal Johnson cycle.  In the frozen root its vertices
are

```text
8e,0f,1d,17,56,66,e4,b4,a5,b1,b8,3c,74,5c,5a,1b,93,d1,
95,c5,e1,71,53,72,6a,6c,cc,c6,d4,96,87,47,4e,4b,2b,33,
b2,9a,d2,d8,9c,1e,3a,2e,2d,4d,c9,e8,ca,e2,f0,78,69,39,
35,36,a6,a3,aa,8b,c3,63,27,65,55,59,99,8d,a9,ac
```

(The SHA-256 of this comma-separated lowercase hexadecimal line, with no
spaces or newline, is
`9eae555be242eb08723fcfa5e97b03caef376384af872b20edfb9ece2b0c9803`.)

Deleting the fourteen incoming connectors gives a spanning 14-path forest
with component profile

\[
6^7 4^7.
\]

Its component-quotient connector gains are

\[
E_s\longrightarrow K_{s+5},\qquad
K_s\longrightarrow E_{s+4}.
\]

Again the closed voltage is

\[
5+4=2\pmod 7.
\]

The lifted connector cycle is

```text
E0,K5,E2,K0,E4,K2,E6,K4,E1,K6,E3,K1,E5,K3,E0.
```

For both choices, the 56 forest edges use every rank-three intersection
colour and every rank-five union colour exactly once.  The connector lower
colours are distinct.  Reattaching them gives a Hamilton cycle whose lower
and upper load profiles are both

\[
1^{42}2^{14}.
\]

Thus the alternate kernel orbit is a genuine physical lift, not merely the
second abstract hypergraph matching.

## 3. The physical ten-vertex quotient

The \(\mathbb Z_7\)-action is free on the seventy rank-four facets.  Rotation
\(\rho\) advances either physical cycle by forty literal positions.  Each
cycle therefore quotients to ten vertices, and one forward quotient circuit
advances the group coordinate by \(2\).

Using the least integer in each vertex orbit as gauge, the two rooted
quotient circuits are as follows.  The entries on the second line are the
directed edge gains.

For \(K_0\):

```text
87,0f,1d,17,2b,1b,93,8d,8b,95,rho^2(87)
 6, 0, 0, 1, 4, 0, 4, 2, 6, 0       (sum 2 mod 7)
```

For \(K_1\):

```text
87,0f,1d,17,2b,1b,93,8d,95,8b,rho^2(87)
 6, 0, 0, 1, 4, 0, 4, 3, 6, 6       (sum 2 mod 7)
```

Deleting the two incoming connector edge-orbits leaves two quotient paths.
Their vertex counts are \((7,3)\) for \(K_0\), and \((6,4)\) for \(K_1\).
Because a tree has no closed voltage, each quotient path lifts to seven
disjoint literal paths.  This explains the two physical component profiles
without a 70-vertex search.

## 4. Quotient path-and-voltage lift lemma

Let a finite cyclic group \(\Gamma\) act freely on a graph lift.  Suppose the
quotient selected-edge graph \(\bar F\) satisfies:

1. \(\bar F\) is a spanning path forest;
2. the omitted connector edge-orbits join endpoints of quotient paths;
3. after contracting every quotient path, the connector quotient is a
   cycle; and
4. the net voltages of its closed walks generate \(\Gamma\).

Then the lift of \(\bar F\) is a spanning path forest, and restoring the
connector lift gives one connected 2-regular spanning graph, hence one
Hamilton cycle.

Indeed, gains on every quotient tree can be gauged to zero.  Therefore each
quotient path lifts to \(|\Gamma|\) disjoint copies.  Connectivity after
contraction is exactly the standard voltage criterion: two lifted copies
are connected precisely when their group labels differ by an element of the
subgroup generated by closed-walk voltages.  If that subgroup is all of
\(\Gamma\), the lift is connected.  Since every restored endpoint has
degree two, the connected lift is a single cycle.

For the two-path quotient over \(\mathbb Z_q\), write the directed gains as

\[
E\xrightarrow{a}K\xrightarrow{b}E.
\]

The lift has exactly

\[
\gcd(q,a+b)
\]

cycle components.  Consequently it is connected if and only if
\(\gcd(q,a+b)=1\).  This criterion is necessary as well as sufficient in
the two-path case.  Here \(q=7\) and both kernel choices have \(a+b=2\), so
both close.

This is the desired quotient-level gate: the repair-core perfect matching
alone is not enough; after physical insertion, its quotient must be a path
forest and its connector cycle voltage must generate the deck group.

## 5. The correct all-\(m\) scale is the three-free subgroup

This section specializes the arithmetic reduction in
`MATH_THEOREM_CATALAN_THREE_PRIMARY_QUOTIENT_REDUCTION_20260731.md`
(SHA-256
`f3d81e2fbf86c8db930c413f3d34752bb1b79b00b4abfb08b7c9da55161a56b1`)
to the physical path-forest and connector coordinate used here.

Put

\[
q=2m-1,\qquad K=\operatorname{Cat}_m,
\qquad s=3^{v_3(q)},\qquad h=q/s,
\]

and let

\[
H=\langle s\rangle\leq\mathbb Z_q,
\qquad H\cong\mathbb Z_h.
\]

This is the maximal clean cyclic group for the three relevant Boolean
shores.

### 5.1 Freeness on all three shores

The group \(H\) acts freely on ranks \(m-1,m,m+1\) of
\(\mathbb Z_q\sqcup\{\infty\}\).  Indeed, if an element of order \(d>1\)
fixes a set, that set's finite part is a union of \(d\)-cycles.  Its size is
therefore divisible by \(d\).  Across the three ranks, the possible finite
part sizes are

\[
m-2,\quad m-1,\quad m,\quad m+1.
\]

But

\[
\gcd(q,m)=\gcd(q,m-1)=1,
\]

while

\[
\gcd(q,m-2)=\gcd(q,m+1)=\gcd(q,3).
\]

Every divisor \(d>1\) of \(h\) is prime to three, so it divides none of
these four sizes.  This proves shore freeness.

The same arithmetic gives the required component divisibility.  The
identity

\[
(m^2-1)K=2q\binom{q-1}{m-2}
\]

and

\[
\gcd(h,m^2-1)=1
\]

imply

\[
h\mid K.
\]

### 5.2 Exact quotient path-forest criterion

Let \(F\) be a fully \(H\)-invariant perfect common inclusion transversal.
It has

\[
N=\binom{2m}{m-1}=mK
\]

edges on

\[
M=\binom{2m}{m}=(m+1)K
\]

middle vertices.  If \(F\) is a spanning forest, it has exactly

\[
M-N=K
\]

components.

Every component stabilizer in \(H\) is trivial.  A setwise stabilizer acts
on the component path, whose automorphism group has order at most two.
Because \(h\) is odd, this action is trivial.  It therefore fixes every
path vertex, and middle-shore freeness forces the stabilizing group element
to be the identity.  Hence the \(K\) physical components fall into free
\(H\)-orbits, and the quotient has exactly

\[
K/h
\]

path components.

Conversely, an \(H\)-voltage quotient which is a spanning path forest with
\(K/h\) components lifts to a spanning path forest with \(K\) components:
each quotient tree can be gauged to voltage zero and therefore has \(h\)
disjoint physical copies.  This is an exact equivalence for an
\(H\)-invariant selected-edge graph; it is not merely a scalar count.

### 5.3 Unit-voltage closure

If endpoint connector orbits join those \(K/h\) quotient paths into one
quotient component cycle of net voltage \(v\in\mathbb Z_h\), then the
physical lift has exactly

\[
\gcd(v,h)
\]

cycles.  Thus the closure is Hamiltonian exactly when \(v\) is a unit
modulo \(h\).  This is Section 4's voltage criterion at the correct general
symmetry scale.

## 6. What remains of full \(\mathbb Z_q\)-equivariance

If \(3\nmid q\), then \(s=1\) and \(H=\mathbb Z_q\).  All of the preceding
path-forest and unit-voltage statements apply to the full rotation group.

If \(3\mid q\), full equivariance is too strong for an exact directed
repair: the outer ranks have order-three short orbits, so a union of free
Johnson-edge orbits cannot hit every lower colour exactly once.  The clean
target is \(H\)-equivariance together with an \(s\)-sector braid.

There is still a useful full-group **necessary** condition for a fully
\(\mathbb Z_q\)-invariant middle path forest.  The full group acts freely on
rank-\(m\) vertices because

\[
\gcd(m,q)=\gcd(m-1,q)=1.
\]

The odd-order path-stabilizer argument then gives

\[
q\mid K.
\]

This is only an obstruction for the fully invariant forest ansatz.  When
\(3\mid q\), even satisfying it would not repair the outer-shore short-orbit
obstruction.  It is not a no-go for noninvariant forests or for the
unrestricted Catalan problem.

## 7. Exact calibrations: both \(m=4\) rows and the \(m=8\) sectors

For \(m=4\), \(q=h=7\), \(K=14\), and \(K/h=2\).  The two exact quotient
rows are:

| kernel choice | quotient path orders | physical path profile | \(E\to K\) | \(K\to E\) | net voltage | physical-cycle hexadecimal CSV SHA-256 |
|---|---:|---:|---:|---:|---:|---|
| \(K_0=(149,134,133)\) | \(3,7\) | \(3^7 7^7\) | 3 | 6 | 2 | `403c4b8f04ebfe6d4cadb44b58c897970ab6a1ef904bd0e391752e690eae0976` |
| \(K_1=(149,193,133)\) | \(4,6\) | \(4^7 6^7\) | 5 | 4 | 2 | `9eae555be242eb08723fcfa5e97b03caef376384af872b20edfb9ece2b0c9803` |

For \(m=8\), the correct data are

\[
q=15,qquad s=3,qquad h=5,qquad K=1430,qquad
M=12870,qquad N=11440.
\]

Here \(H=\langle3\rangle\cong\mathbb Z_5\), and the finite coordinates
split into exactly three \(H\)-sectors:

```text
{0,3,6,9,12},  {1,4,7,10,13},  {2,5,8,11,14}.
```

An \(H\)-equivariant common-transversal forest therefore quotients to

\[
M/h=2574\text{ middle vertices},\qquad
N/h=2288\text{ edges},\qquad
K/h=286\text{ paths}.
\]

A quotient connector cycle closes it precisely when its net voltage is one
of \(1,2,3,4\pmod5\).  Its lift then has all 1430 physical paths in one
Hamilton cycle.  The three coordinate sectors still have to be braided in
the quotient construction; the theorem supplies the exact scale and gate,
not that missing construction.

## 8. Scope and audit

The literal conclusions above are exact only for the two matchings in the
authenticated canonical \(m=4\) complete core.  The \(H\)-shore freeness,
component divisibility, quotient path-forest criterion, and unit-voltage
closure are general.  This note does not assert that the required quotient
matching, path forest, or sector braid exists for every \(m\).

Individual gains \((3,6)\) and \((5,4)\) use the component gauge fixed in
Section 1.  Reversing the physical orientation negates the net voltage;
changing component representatives changes the two individual gains but
leaves their sum unchanged.

Reproduce with

```text
python3 scratch/audit_catalan_m4_z7_physical_lift_voltage_independent_20260731.py
```

The output is

```text
scratch/catalan_m4_z7_physical_lift_voltage_independent_20260731.audit.json
```
