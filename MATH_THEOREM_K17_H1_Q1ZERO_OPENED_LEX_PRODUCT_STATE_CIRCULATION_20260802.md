# K17 h1 full-palette opened-chronology lexicographic circulation theorem

## 1. Authenticated rebase and the two different q1 notions

Let `F0` be

```text
/home/amodo/or15/work/root_k17_q1_targeted_static_20260802/
    q1zero.independent.model
SHA256 b1fc0d9ca69c8411aad96557f5a47fe031616c88644f5d5691bec705b2b61a31
```

It is a complete assignment of the 218,790 primary incidence variables. Its
deterministic y+p extension has SHA-256

```text
f544cbc2a6c3bf9f9d7500202b4a60cb06660c3b5a1cdd382daec4d8dd4bbb90.
```

For every ordinary non-D rank-ten target `U`, define its provider load

```text
n_U(F) = sum(p : union(p)=U).
```

The ordinary q1 invariant in this theorem is

```text
n_U(F) >= 1 for all 19,412 targets U.                      (1)
```

At `F0`, (1) is complete: `19412/19412`. This is a presence condition, not
provider-load equality. It is also not opened rank-ten completeness. The
opened chronology depends on the exceptional D branch, boundary, and chosen
orientation, which are absent from the ordinary-pair projection.

The exact opened metrics at `F0` are

```text
orientation 0: residence 5586, holes 22,1533,286,7,0,0,0,0;
orientation 1: residence 5587, holes 22,1534,286,7,0,0,0,0.
```

Thus the authenticated starting tuple is

```text
psi(F0) = (22,5586,1826),                                 (2)
```

where the last coordinate is the sum of opened holes at ranks 11 through 17.

## 2. One opening must supply the entire tuple

For a connected h1 factor `F` and one legal opening/orientation `omega`, let

```text
h_r(F,omega) = number of absent opened rank-r targets,
R(F,omega)   = number of internal positive q-runs of lengths 1 or 2,
H(F,omega)   = sum(h_r(F,omega), r=11,...,17),
psi(F,omega) = (h_10(F,omega), R(F,omega), H(F,omega)).    (3)
```

Either retain `(F,omega)` as the product state or define

```text
psi(F) = lexicographic minimum of psi(F,omega)
         over all legal omega.                             (4)
```

Coordinatewise minima taken from different openings are invalid. Hole counts
alone are also not Markov sufficient: a later move may delete the last witness
of a currently covered target.

## 3. Exact lifted state

For a bounded packet builder, a complete materialized state contains at least

```text
Sigma = (j, d, a, chi(F), clause slacks, all n_U,
         protected/cap ledgers, Pi, opening profile, Theta,
         all opened witness loads L[r,U]).                 (5)
```

Here `d,a` are integer multiplicity-aware literal rewrite vectors;
`chi(F)=(y(F),p(F))` with every p channel rebuilt deterministically; `Pi` is
the full port matching, component partition, and declared per-component
voltage state; and `Theta` is the exact trace/open-run transfer state. The
literal masks, witness loads, and topology state cannot be replaced by their
aggregate scores.

## 4. Strict and atomic builders

### Strict-prefix builder

`Gamma_strict` is layered by the number of physical C6/C8 toggles. Regenerate
the state-relative circuit catalogue at every materialized prefix. Retain an
arc head only when it is binary and degree exact, preserves every protected,
cap, and accumulated row, satisfies the full palette condition (1), and has
the declared connected augmented-incidence topology and legal opening state.

Objective coordinates may temporarily worsen inside an explicitly declared
debt box. Objective sign never determines resource closure. Every nonroot
resource-closed state has a zero-cost analytic arc to the sink. A physical arc
has vector cost

```text
c(F,F') = psi(F') - psi(F),                               (6)
```

so costs telescope. Packet length counts physical proposal/toggle arcs only;
analytic sink/reset arcs have length zero.

### Atomic terminal-commit builder

A pending atomic state stores exact integer vectors `d,a`, canonical batch or
ordered semantics, and collision/resource data. It need not be a factor, so
it receives no fictitious palette, topology, opening, or objective values.

At commit, first require

```text
y(FP) = y(F0) - d + a, coordinatewise in {0,1}.           (7)
```

Then rebuild p and replay every invariant row, (1), complete topology/opening,
and the exact objective profile. Proposal arcs cost zero; the commit cost is
`psi(FP)-psi(F0)`. An atomic witness proves the simultaneous terminal rewrite
only. It proves no legal intermediate sequence.

## 5. Exact vector min-cost flow

Let `N` be the head-minus-tail node-arc incidence matrix of either finite
layered builder, `s` its root, `tau` its sink, and `b=e_tau-e_s`. The exact
problem is

```text
lex-minimize sum(c_e f_e)
subject to N f = b and f >= 0.                            (8)
```

No big-M is needed. Solve successive optimal faces:

```text
P0 = {f : Nf=b, f>=0};
mu_i = min { c_i^T f : f in P_(i-1) };
P_i = P_(i-1) intersect {f : c_i^T f = mu_i}.             (9)
```

The unit-flow polytope is integral, and every `P_i` is a face of it. Hence an
integral lex-optimal accepting path survives every stage.

## 6. Proved mixed-radix scalarization

For the declared K17 opened tuple, global combinatorial bounds are

```text
0 <= h_10 <= C(17,10) = 19448,
0 <= R    <= 17(24310+1) = 413287,
0 <= H    <= sum(C(17,r),r=11,...,17) = 21778.            (10)
```

The residence bound is deliberately coarse but valid: there are 17
coordinates and 24,311 opened q positions. Empirical incumbent ranges are not
bounds.

Therefore the exact scalar encoding is

```text
S(h_10,R,H) = 9000999352 h_10 + 21779 R + H.              (11)
```

Indeed, one unit in an earlier coordinate outweighs the maximum contribution
of all later coordinates. Thus tuple lexicographic order and scalar order in
(11) agree over the entire bounded box. The value fits signed 64-bit integer
arithmetic at K17.

Scalar physical-arc cost is `S(psi(F'))-S(psi(F))`; an atomic commit uses the
endpoint difference. This is a proved radix, not an assumed penalty weight.

## 7. Bellman-Ford/Farkas and normalized circulation

For scalarized costs, define

```text
mu = min { c^T f : Nf=b, f>=0 }.                          (12)
```

- If `tau` is unreachable and `R_s` is the root-reachable set, then
  `z=-1_(R_s)` satisfies `N^T z<=0` and `b^T z=1`.
- If `tau` is reachable and `mu<0`, an integral lex-improving closed packet
  exists.
- If `tau` is reachable and `mu>=0`, a dual potential with
  `pi[v]-pi[u]<=c[u,v]` and `pi[tau]-pi[s]=mu` certifies that no lex-improving
  packet exists inside the declared finite builder.

A random no-witness run proves none of these no-go branches.

Equivalently, add a zero-cost analytic reset arc `tau->s` and fix its flow to
one. Without this normalization, the zero circulation hides existence and a
negative accepting cycle may be repeated without bound.

## 8. Regenerative hypothesis

Let `C_full` be an endpoint-closed family satisfying (1) and every declared
resource/topology row. `RE_lex(L,delta)` requires that every state outside a
declared terminal set have a regenerated strict or explicitly atomic packet
using at most L physical C6/C8 proposals and satisfying

```text
S(psi(F')) <= S(psi(F)) - delta, with delta >= 1.          (13)
```

Then repeated regeneration terminates after at most

```text
ceil((S(psi(F0))-S_min)/delta)
```

packets. Pure lex decrease also proves termination because the tuple lies in a
finite bounded box. It reaches a zero tuple only if the declared terminal set
is exactly that tuple.

Lex descent may worsen lower-priority coordinates whenever an earlier
coordinate improves. A hard deeper/source/compiler condition must therefore
be an invariant state row, not merely a lower-priority objective.

## 9. Scope of the finite actuator

The companion actuator searches bounded strict-prefix paths directly from
the authenticated model (2). Every retained prefix must preserve all 19,412
ordinary colours, all 16,261 accumulated rows, protection, exact degrees, and
connected augmented topology. It targets opened rank-ten holes at most 20,
which is lexicographically stronger than any tuple whose first coordinate is
21, irrespective of residence or deeper debt.

A replayed witness proves existence only at this base and in its declared
packet family/debt/length envelope. It proves neither lex optimality,
catalogue completeness, regeneration, source/compiler feasibility, residency,
nor a word.
