# K17 singleton topology LNS: exact fixed-exterior scope audit

Date: 2026-08-01  
Lane: K, independent audit  
Status: direct-`A` restriction proved exact; complement-master version rejected
unless its global orientation break is removed or separately shown redundant.

## 1. Inputs and scope

The authenticated complement-dual seed is the matching in

```text
scratch/threadD_k17_complement_dual_splice_20260801/seed.best.tsv
```

with SHA-256

```text
a3f9eac037ae66a460349b12d578a31222afe1a7d168da641e77967a44ddbab3.
```

Its independently replayed direct permutation `A=C D` has quotient cycle
lengths `[1429,1]`, with singleton owner `425`.  The exact fixed-exterior
builder audited here is

```text
scratch/build_k17_direct_A_topology_lns_20260801.cpp
```

with SHA-256

```text
6835a6c22487555fa33484adcccc394bb5289b7731e37f4a92051e3d3dc0c51d.
```

This is a sufficient-subclass calculation.  It concerns the
complement-dual direct-`A` fibre with a fixed exterior, eager rank-ten
coverage, and an exact quotient Hamilton condition.  It is not an
unrestricted K17 no-go.

## 2. Exact contracted assignment graph

Let `A_0` be the seed permutation.  For every legal direct arc

\[
                         e:u\longrightarrow h,
\]

put

\[
                         \rho(e)=A_0^{-1}(h).
\]

Thus the selected seed arc at `u` contracts to the loop `u--u`, while an
alternative arc is the assignment edge `u--rho(e)`.  Let `Gamma` be the
undirected graph obtained from all nonloop assignment edges, with parallel
physical incidences suppressed only for distance computation.

For a root set `X`, leave the variable of `e` free exactly when

\[
                         u\in X\quad\hbox{and}\quad\rho(e)\in X.       \tag{2.1}
\]

Every other arc is pinned to its seed truth value.

### Theorem 2.1 (fixed-exterior pinning equivalence)

Under the exact one-out and one-in rows of the direct-`A` master, the unit
restriction (2.1) is equivalent to the following statement:

1. every tail outside `X` keeps its seed head;
2. the candidate heads used by tails in `X` are exactly `A_0(X)`;
3. after contracting the seed arcs, the symmetric difference is a disjoint
   union of assignment cycles wholly contained in the induced graph
   `Gamma[X]`.

Conversely every legal collection of such cycles gives a unique assignment
satisfying all units and all one-in/one-out rows.

#### Proof

If `u` is outside `X`, every nonseed outgoing variable at `u` is pinned
false and its seed variable is pinned true.  If `u` is in `X`, every arc
from `u` to a contracted head root outside `X` is pinned false.  Applying
the same argument to the one-in row at every seed head shows that the free
tails use precisely the seed head bank `A_0(X)`.  Hence

\[
                  \pi=A_0^{-1}\circ A\bigm|_X
\]

is a permutation of `X`; its nontrivial cycles are exactly the
seed-alternating assignment cycles.  The converse follows by reversing the
argument.  Notice that parallel incidence choices at one contracted pair
remain separately free, as required.  \(\square\)

This also proves that leaving auxiliary turn/order variables unpinned is
sound: the direct-`A` arc support determines them through the inherited
base clauses.

## 3. Radius completeness

Let `s` be the singleton root and let

\[
                         X_r=B_\Gamma(s,r).
\]

### Corollary 3.1

Every single seed-relative alternating assignment cycle through `s` with
at most `2r+1` changed roots is contained in `X_r`.  Thus radius two
contains every such support-at-most-five exchange and radius three every
support-at-most-seven exchange.

#### Proof

On a root cycle of length `t`, every vertex has cycle distance at most
`floor(t/2)` from `s`; graph distance in `Gamma` is no larger.  \(\square\)

The converse is not asserted: a radius ball can contain larger exchanges
because of chords.  More importantly, UNSAT at radius `r` does **not**
exclude a connector cycle through the singleton together with a disjoint
palette-compensating cycle outside `X_r`.  It closes exactly the fixed-
exterior induced-ball fibre of Theorem 2.1.

## 4. Exact direct-`A` Hamilton semantics

The base builder

```text
scratch/build_k17_age_direct_A_cycle_master_20260801.cpp
```

uses eleven order bits.  Owner zero has order zero; every other owner is
required to have nonzero order.  Every selected nonloop arc whose head is
not zero enforces

\[
                         q(Au)=q(u)+1
\]

with no eleven-bit overflow.  Loops are forbidden, while the one arc whose
head is zero is the unique permitted wrap.

### Lemma 4.1

Together with the one-in/one-out rows, these clauses are equivalent to `A`
being one quotient Hamilton cycle.

#### Proof

A directed cycle avoiding zero would make the integer order strictly
increase around a closed loop, which is impossible.  Hence every
permutation cycle contains zero and there can be only one.  Conversely, on
a Hamilton cycle assign orders `0,1,...,1429` from zero; eleven bits suffice
and every increment/no-overflow row holds.  \(\square\)

The master does not impose nonzero physical voltage; that remains a later
literal replay/CEGAR row.  Its eager rank-ten clauses and the direct
`p != n` row are inherited unchanged by the LNS.

## 5. Rejected complement-master shortcut

The exact complement-dual one-matching master contains the additional
global symmetry break

\[
                 \operatorname{id}(D(0))<\operatorname{id}(H(0)).     \tag{5.1}
\]

It is encoded by all clauses

```text
-D_e  -D_complement(h)
```

for owner-zero incidences with `e>h`.  In the unrestricted complement-dual
master this is valid: swapping `D` and `H` reverses `A`, so one orientation
of every solution satisfies (5.1).

After exterior `D` units are fixed, that symmetry argument fails.  The
reversed matching generally leaves the fixed-exterior fibre.  Therefore an
UNSAT result obtained by simply appending halo units to that base closes
only the extra orientation-broken subfibre, unless both incidences compared
in (5.1) are pinned and the seed already satisfies (5.1).  It is not a
proof-safe UNSAT certificate for the full halo in general.

The direct-`A` exact master has no such orientation row and is the correct
base for the current LNS.  An alternative is to rebuild the complement-
dual master with (5.1) disabled.

## 6. Independent checker

The lightweight independent checker is

```text
scratch/audit_k17_direct_A_topology_lns_scope_20260801.cpp
```

with SHA-256

```text
d9650e0482fca52efe1858928763f80298fab7c931915b98b25d5578ad9cd944.
```

It independently reconstructs:

- the `D`-incidence to direct-`A`-arc bijection;
- the `[1429,1]` seed cycle decomposition;
- the singleton and contracted root graph;
- the radius ball;
- every free, positive-pinned, negative-pinned, and boundary arc count; and
- the exact proof scope of Corollary 3.1.

A companion diagnostic for the rejected complement-master restriction is

```text
scratch/audit_k17_complement_dual_topology_lns_scope_20260801.cpp
```

with SHA-256

```text
8391ea167899d302c37b3ace66a71270f71599c3578137c90a6f8d18f88018ce.
```

It reports whether (5.1) is actually redundant in a specified halo.  No
SAT conclusion is part of this source-level audit.

## 7. Exact conclusion

The BFS contraction and pin construction are correct.  The radius-two
UNSAT certificate built from the exact **direct-`A`** base is proof-safe for
its stated fixed-exterior fibre.  The radius-three run is `UNKNOWN` and has
no certificate.  The previously considered complement-master implementation
is not proof-safe for the full fibre without removing or proving redundancy
of its orientation symmetry break.  The scoped radius-two UNSAT does not
rule out remote compensating exchanges, larger halos, the nondual splice
after obtaining a Hamilton `A`, or the unrestricted K17 carrier problem.
