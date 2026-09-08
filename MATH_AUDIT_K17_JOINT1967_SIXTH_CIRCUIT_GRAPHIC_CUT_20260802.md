# Exact K17 joint1967 sixth-circuit graphic cut

**Date:** 2026-08-02  
**Status:** exact historical negative-prefix audit.  This is not the current
promotion root.  At freeze time the sole promoted root has already advanced
to `(R,D)=(1941,1743)`; no assertion about its outgoing fan is made here.

## 1. What is and is not in the authenticated descent

The circuit called “the sixth” is not a prefix of the accepted
`1980 -> 1953` lineage.  The accepted ancestry is:

```text
res1980 -> joint1967 -> joint1961 -> joint1953.
```

The first five rows of the root-disjoint continuation from `joint1967` give
the authenticated connected `joint1961` checkpoint.  A sixth commuting row
was tested and rejected.  A different five-row connected continuation then
gives authenticated `joint1953`.  Therefore the phrase “sixth-circuit split”
denotes a historical boundary witness, not a defect in any promoted model.

The exact models and packet tables used below are bound by the checkpoint
manifests.  In particular,

```text
joint1967 model SHA256 = f56a56a375119c337ed64d94bf22bfcf1ab9d17e144679c0f3d127f89bf43b43
joint1961/quint SHA256 = 8ea103e2bfc14cf6b73ce7156645f112a59d3b97e5c5673e5c595a14310283a1
sext rejected SHA256   = 84a8580ff1b5bbd639da67a18d7524def47bbd9424608215740e686c40a92865
incidence map SHA256   = 80980012d7b1449c8ce3932e77ee7e5e47f5d6eb6f18d219687358cbd024355a
```

The independent endpoint audits give

```text
after 2 circuits: connected, (R,D)=(1964,1768),
after 3 circuits: connected, (R,D)=(1963,1767),
after 5 circuits: connected, (R,D)=(1961,1767).
```

The lightweight cut auditor independently reconstructs connectivity at all
six literal circuit prefixes, rather than only these saved combined models.

## 2. The canonical detached shore

Let `H_i=(V,E_i)` be the complete selected lower--owner incidence graph after
the first `i` rows, with `H_0=joint1967`.  The sixth endpoint `H_6` has exactly
two connected components.  Define `W` canonically as the component not
containing either exceptional lower root

```text
D=255,                 M=383.
```

The exact component census is

```text
W lower vertices       1,022
W owner vertices       1,022
selected edges in W    2,044
```

Every vertex of `W` is ordinary and has selected degree two.  Thus `W` is a
single 2,044-edge incidence cycle.  The complementary component contains
`M,D` and is the remaining lollipop component.

The complete incidence-map cut has

```text
|delta(W)| = 13,746.
```

The auditor regenerated this set from the 218,790-row incidence map and
proved literal equality with the 13,746-variable connectivity clause emitted
by the frozen passive replay.  The sorted shore hashes are

```text
lower masks FNV64 = ceacc98620d5789a,
owner masks FNV64 = 1ff6c05eedea7130.
```

Full sorted mask and cut-variable lists are frozen with the audit.

## 3. Exact prefix cut ledger

Put

```text
k_W(i)=|E_i intersect delta(W)|.
```

The exact ledger in the declared order is

| prefix `i` | components | `k_W(i)` |
|---:|---:|---:|
| 0 | 1 | 8 |
| 1 | 1 | 6 |
| 2 | 1 | 6 |
| 3 | 1 | 6 |
| 4 | 1 | 6 |
| 5 | 1 | 4 |
| 6 | 2 | 0 |

The move increments are

```text
Delta k_W = (-2,0,0,0,-2,-4).
```

The rejected sixth circuit is exactly

```text
old: 2449,4402,1381,291
new: 2452,4403,1378,292.
```

All four old incidences cross `delta(W)`:

| variable | lower | owner | endpoint sides `(lower,owner)` |
|---:|---:|---:|:---:|
| 2449 | 3033 | 3035 | `(W,bar W)` |
| 4402 | 4056 | 4057 | `(bar W,W)` |
| 1381 | 2010 | 4058 | `(W,bar W)` |
| 291 | 987 | 2011 | `(bar W,W)` |

All four new incidences are internal: `2452,1378` lie inside `W`, while
`4403,292` lie inside its complement.  Hence the exact transition identity is

```text
k_W(6)=k_W(5)-4=0.                                      (3.1)
```

This is stronger than a component-count observation: it identifies the
unique violated graphic shore and every incidence responsible for the loss.

## 4. Why singleton legality and reordering do not save the six-row batch

The six circuit supports are pairwise incidence-disjoint.  Each circuit is
alternating at `H_0`, and applying any one of them alone to `H_0` leaves one
connected component.  Their singleton `k_W` values are respectively

```text
6,8,8,8,6,4.
```

Thus the sixth primitive is not intrinsically topology-illegal.  It becomes
illegal after earlier circuits have spent four units of the same global cut
slack.  This is the exact failure of root-only singleton screening.

Because the supports are disjoint, the six toggles commute and every
permutation has the same endpoint `H_6`.  Consequently no ordering of these
same six circuits can be a closed hard-legal packet: some last prefix is the
disconnected endpoint.  An ordering can only postpone the violation.

This conclusion is scoped to these six circuits.  It does not exclude an
overlapping preparer or ear which plants new crossing incidences before the
cut-consuming move.

## 5. The sharp topology ticket

For every degree-preserving state on this vertex shore,

```text
2|W| = 2|E(W)| + k_W.                                   (5.1)
```

Since `W` contains neither exceptional lower root, (5.1) implies

```text
k_W is even.                                             (5.2)
```

On this fixed degree face, connectivity across `W` is therefore not merely
`k_W>=1`; it is equivalently

```text
k_W>=2.
```

Define the integer topology socket

```text
t_W=k_W/2.
```

The quint has `t_W=2`; the sixth circuit consumes two sockets and leaves
zero.  A preparer which leaves the sixth circuit otherwise unchanged must
therefore establish

```text
t_W >= 3 before the sixth move,
```

equivalently it must plant at least one net crossing **pair** before that
move.  One untyped “backup edge” is not a realizable degree-preserving ticket
on this shore.  Planting one pair is the exact minimum for this cut, though it
is not by itself sufficient for all provider, opening, or other topology
rows.

The frozen connectivity clause is the weaker Boolean form

```text
OR_(e in delta(W)) y_e,
```

whose 13,746 literals are all false at `H_6`.  Equation (5.2) sharpens its
right-hand side from one to two inside the exact factor-degree face.

## 6. Opening behavior and separation from the CNF face

Prefixes zero through five are connected and retain the prescribed degree
sequence: one lower of degree one, one lower of degree three, and every other
lower and owner of degree two.  Hence each is one lollipop and has the two
licensed global openings.

At prefix six, the main component remains a lollipop on 46,576 vertices, but
the 2,044 vertices of `W` form a separate cycle.  Opening the main lollipop
therefore yields only 46,577 trail entries (the lollipop vertices plus the
repeated junction), not the required 48,621.  This is exactly the frozen
independent failure

```text
FAIL_INDEPENDENT_STATIC_CHAIN trail length.
```

Accordingly there is no legal global opening at `H_6`; opened q1 and upper
chronology coordinates are not legitimate terminal payloads there.

The independently rebuilt extended assignment nevertheless satisfies all
7,164,257 clauses of the frozen round-5 DIMACS.  The passive replay reports

```text
PASS_H1_GLOBAL_DISCONNECTED components=2 cuts=1.
```

Thus the split is specifically a missing dynamic connectivity shore, not a
DIMACS/provider refutation.  The emitted `DO_NOT_ADD` clause is the exact
separating row.

## 7. Consequence for a state-relative expansion theorem

Let `Gamma_L(F)` be a regenerated compound fan.  The weakest proof-safe
topology condition is not “every constituent is root-safe” and not “the
endpoint XOR lies in the cycle space.”  Every physical arc must have a head
inside the connected hard state space, equivalently

```text
k_W(F_i)>=1 for every nontrivial W and every physical prefix i. (7.1)
```

On shores containing only degree-two vertices, (7.1) may be stored sharply as
`t_W(F_i)>=1`.  A topology debt vector need retain only threatened cuts, but
it must be updated at the actual tail before a move is admitted.

For this witness, any fan quotient that identifies the quint state with the
root by objective, provider, or individual-circuit data alone admits a false
sixth arc.  Retaining `t_W=2` at the quint rejects it immediately.  A repaired
fan may admit a preparer `A` followed by the sixth circuit only if

```text
Delta_A t_W >= 1
```

before the sixth prefix and all other hard rows remain true.

Therefore the state-relative renewal hypothesis must quantify over paths in
the **connected lifted graph**:

```text
for every retained nonterminal F, there is a bounded closed path
F=F_0 -> ... -> F_s
such that every F_i satisfies all hard rows including (7.1),
and the declared common integer Lyapunov function strictly falls. (7.2)
```

Condition (7.2) is sufficient for repeated descent by well-foundedness.  The
sixth-circuit witness proves that deleting the prefix cut coordinates from
(7.2) is unsound.  It does not prove that a crossing-pair preparer is absent
from a larger regenerated fan.

## 8. Frozen scope

The lightweight auditor parses the raw 218,790-row incidence map and three
primary assignments, replays the six exact packet rows, checks root
applicability, incidence-disjointness, every prefix component count, exact
identity with the quint and sext models, regenerates `delta(W)`, and compares
it byte-for-set with the frozen connectivity clause.  It does not recompute
guards, q1, residence, or upper holes; those statements above are restricted
to separately frozen independent reports.  No source, compiler, resident
factor, universal word, or current-root expansion claim is made.
