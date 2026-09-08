# K17 h1 C6/C6 topology bypass on the 26-hole q1 incumbent

## 1. Authenticated face

Let `F0` be the primary incidence factor

```text
/home/amodo/or15/work/root_k17_q1_targeted_static_20260802/
    census22.independent.model
SHA256 645de2d68cb0b012bbea2d7f7027b7f62f86e9d4e43b9b70fceb22c60dc00a4a
```

For every factor `F`, rebuild the ordinary-pair channel deterministically and
write

```text
chi(F) = (y(F), p(F)),       p[q,a,b] = y[q,a] y[q,b].
```

The authenticated global map has 218,790 incidence variables and 875,088
derived pair variables. The accumulated bank has 16,261 literal clauses and
SHA-256

```text
e64219c98e4191bbef8e6ba32567cec6286c777755782030fd9cca13669971fc.
```

For a clause `r = (P_r,N_r)`, its exact slack is

```text
ell_r(F) = sum(chi_v(F), v in P_r)
         + sum(1-chi_v(F), v in N_r) - 1.                (1)
```

The clause passes exactly when `ell_r(F) >= 0`. A score is not a substitute
for these literal inequalities.

For each of the 19,412 necessary non-D rank-ten targets `U`, define

```text
n_U(F) = sum(p : union(p)=U),       I_U(F) = 1[n_U(F)>0]. (2)
```

The q1 fibre used here is exact presence-pattern equality:

```text
I_U(F) = I_U(F0) for every U.                              (3)
```

It is not provider-load equality. The loads on eight present targets change
in the displayed packet. What is invariant is the same 19,386 present targets
and the same 26 missing targets. The common 26-row missing-target file has
SHA-256

```text
70ed7ac6cd23f5830639cc898224e34887982057e7614372d037ac2363897dbc.
```

Those 26 frontier rows are violated repair rows, not members of the satisfied
16,261-row accumulated bank; this lane does not add or solve them.

Let `V = V8 disjoint-union V9` be the full rank-eight/rank-nine augmented
incidence vertex set, and let `delta(S)` be the selected-y incidence cut of
`S`. Together with the exact h1 degree and protected-boundary rows,
augmented-incidence connectivity is exactly

```text
sum(y_e(F), e in delta(S)) >= 1
for every nonempty proper subset S of V.                    (4)
```

The retained product-state coordinate `Pi(F)` must contain the full port
matching, component partition, and any declared voltage data. A scalar
component count or total voltage is not Markov sufficient.

The principal residence potential is

```text
Phi_o(F) = sum over coordinates x of
           non-seam order-1,2,3 components in the
           x-induced ordinary owner graph.                  (5)
```

This is the passive cyclic/component metric, not a directed-run count. Let
`Phi_l(F)` be the better exact opened-q-path short-run total. At the incumbent,

```text
Phi_o(F0) = 0 + 2963 + 2609 = 5572,
Phi_l(F0) = 2964 + 2610      = 5574.                        (6)
```

For this calibrated search, a negative target additionally obeys

```text
Phi_o(F) < 5572 and Phi_l(F) <= 5574.                       (7)
```

Condition (7) is an objective predicate, not part of resource closure.

## 2. Exact finite lifted-state theorem

Fix a length/support bound and literal C6/C8 proposal semantics. A complete
materialized state is

```text
Sigma = (j, d, a, chi(F), d_clause, d_q1, d_prot, d_cap,
         Pi, Theta, DeltaPhi).                              (8)
```

Here `d` and `a` are integer removal/addition multiplicity vectors;
`d_clause` contains every signed slack from (1); `d_q1` contains the exact
loads and presence bits from (2); `Pi` is the full topology state; and
`Theta` is the retained trace/open-run transfer state. The literal rewrite
vectors cannot be projected away: aggregate debts alone do not determine
alternation or collisions.

There are two different exact builders.

### Strict-prefix builder

`Gamma_strict` is a finite layered graph. An arc is a current-state legal
C6/C8 toggle. Its head is retained only if it is binary and degree exact,
preserves the declared protected and cap rows, satisfies every accumulated
clause and q1 row, and passes augmented-incidence connectivity. Residence may
rise within a declared debt bound.

A nonroot materialized state is closed when it satisfies all those resource
conditions and any declared secondary bound, such as `Phi_l <= 5574`.
Objective sign is not used to decide closure. Connect every closed state to
the sink with a zero-cost sink arc. Put cost

```text
c(F -> F') = Phi_o(F') - Phi_o(F)                           (9)
```

on each materialized arc. Costs therefore telescope. A strict pair needs an
ordering with a feasible first prefix and a closed union. A strict triple also
needs a feasible two-move prefix in some ordering. If no singleton prefix is
feasible, no strict packet exists.

Packet length counts physical C6/C8 toggle arcs only. The analytic sink arc
has length zero and is not a packet primitive.

### Atomic terminal-commit builder

`Gamma_atom` is a finite proposal DAG. A pending state retains the exact
integer vectors `d,a`, order or canonical-batch semantics, and all collision
and resource data. A pending fixed-base batch need not be a factor, so it must
not be assigned fictitious topology or residence.

At commit, first materialize

```text
y(FP) = y(F0) - d + a,     coordinatewise in {0,1}.        (10)
```

Then rebuild every pair variable and directly replay degrees, protection,
accumulated clauses, the declared q1/cap face, full topology/voltage, and the
secondary terminal conditions. Proposal arcs cost zero and the commit arc
costs `Phi_o(FP)-Phi_o(F0)`. An atomic certificate proves the simultaneous
terminal rewrite only; it proves no legal intermediate sequence.

For the length bound, count physical proposal primitives only; analytic
commit, sink, and reset arcs have length zero.

### Bellman-Ford/Farkas alternative

Let `N` be the head-minus-tail node-arc incidence matrix of either finite
layered builder, let `s` be its root, let `tau` be the closed-state sink, and
put `b = e_tau - e_s`. Then

```text
mu = min { c^T f : N f = b, f >= 0 }.                      (11)
```

Total unimodularity gives an integral path optimum. Therefore:

- `mu < 0` is exactly a negative closed packet in the declared builder;
- if `tau` is unreachable and `R` is the set reachable from `s`, then
  `z = -1_R` satisfies `N^T z <= 0` and `b^T z = 1`, an exact Farkas cut;
- if `tau` is reachable and `mu >= 0`, the dual potential satisfies
  `pi[v]-pi[u] <= c[u,v]` and `pi[tau]-pi[s]=mu`, certifying every declared
  closed packet nonnegative.

This alternative is scoped to the enumerated catalogue, length, support,
resource face, and complete state. A random no-witness run proves none of its
nonexistence branches.

## 3. Authenticated neutral-preconditioner/topology-blocked pair

For a rank-seven core `S` and ordered outside labels `a,b,c`, define the C6
phase toggle

```text
(S+a, S+a+b), (S+b, S+b+c), (S+c, S+c+a)
    <->
(S+a, S+a+c), (S+b, S+b+a), (S+c, S+c+b).                (12)
```

The independently materialized packet is move A followed by move B:

| move | core | labels | removed y | added y |
|---|---:|---|---|---|
| A | 49972 | 13,0,3 | 106174,90155,90197 | 106176,90161,90190 |
| B | 107589 | 11,1,4 | 195427,191594,191644 | 195429,191599,191638 |

Their ordinary roots are respectively

```text
(58164,49973,49980) and (109637,107591,107605).            (13)
```

Every displayed A-then-B prefix satisfies all 7,163,170 clauses of the frozen
round4 formula after deterministic extension, hence in particular all 16,261
accumulated rows. Each has exactly the incumbent 26-hole q1 presence pattern,
preserves `383->511` and `510->511`, and has one connected augmented-incidence
h1 lollipop.

| state | formula/q1 | augmented topology | Phi_o | best Phi_l | best linear upper holes 10--13 |
|---|---|---:|---:|---:|---:|
| F0 | pass / same 26 holes | 1 component | 5572 | 5574 | 48,1534,288,7 |
| A(F0) | pass / same 26 holes | 1 component | 5572 | 5574 | 48,1535,288,7 |
| B(F0) | pass / same 26 holes | 2 components | not defined on the closed face | not defined | not defined |
| B(A(F0)) | pass / same 26 holes | 1 component | 5568 | 5570 | 48,1535,289,7 |

Thus A is strict-face feasible but residence-neutral. B is an alternating C6
at the root and passes the full CNF and q1 presence face there, but is blocked
by augmented-incidence connectivity. Neither displayed constituent is an
accepting negative root singleton. After A changes the port state, the
state-relative B arc is present and gives

```text
Delta Phi_o = -4,       Delta Phi_l = -4.                 (14)
```

This is a strict-prefix topology-bypass certificate, stronger than an atomic
terminal-only certificate because both displayed prefixes are accepted
factors. It also isolates why scalar Hall/q1 projections are insufficient:
the root B proposal passes them but fails `Pi`.

This is a state-dependent arc phenomenon, not a finite Mobius interaction:
the B arc is absent from `Gamma_strict` at F0, while the B arc out of A(F0)
is present and reaches the displayed negative terminal.

The claim is about these two constituents only. The producer also sampled
nine other root occurrences with ordinary decrease, so this certificate does
not show that the incumbent or the full primitive catalogue is globally
singleton-blocked, nor that compound descent is necessary.

## 4. Regenerative descent and its exact missing hypothesis

Let `T` be a declared terminal subset of an accepted state family `F`. The
additional expansion hypothesis needed for regeneration is:

> Bounded accepting-path expansion `RE(L,delta)`: for every `F` in `F-T`,
> regenerate the complete state-relative builder at `F`; it contains a strict
> or explicitly atomic closed path of length at most `L` to `F'` in `F` with
> `Phi_o(F') <= Phi_o(F)-delta`.

If `RE(L,delta)` holds with `delta>0`, repeated regeneration reaches the
declared terminal set after at most `ceil(Phi_o(F0)/delta)` packets, because
`Phi_o` is a nonnegative integer. It reaches residence zero only when the
declared nonterminal set is exactly `Phi_o>0`.

The present witness proves only the pointwise conclusion at `F=F0` with
`L<=2` and `delta>=4`. It proves neither a minimal L nor `RE(2,4)` on a family
containing later states.

The upper-hole vector worsens from `48,1534,288,7` to `48,1535,289,7`.
Therefore this pair is not an arc of a stronger recurrence that freezes or
monotonically decreases the deep-upper ticket. Such a recurrence needs upper
slack in the lifted state or a further repair packet that jointly returns the
upper debt. Source and compiler tickets were not evaluated.

## 5. Audit boundary

The producer was a seeded random strict-prefix sampler. It stopped after
58,286 proposals inside a five-million-proposal budget. Randomness found the
candidate; it is not part of the proof. A separate materializer checked the
C6 formula, phase, ordered applicability, both prefixes, and both root
singletons. Independent full-formula, q1, topology, residence, and upper
replays established the table above.

The certificate proves existence for this incumbent and exact face. It does
not prove catalogue completeness, optimality, terminal-only debt cancellation,
deep-upper preservation, source/compiler feasibility, regeneration at the
next state, residence zero, residency, or a word.

The frozen artifacts are in

```text
scratch/k17_h1_q1_26_compound_c6c6_residence_20260802/
```

The terminal primary model has SHA-256

```text
f6ddc13a3fdb9276f0a31b8e41bfabebda188f92210fdf6fd4bd406ecda024b9.
```
