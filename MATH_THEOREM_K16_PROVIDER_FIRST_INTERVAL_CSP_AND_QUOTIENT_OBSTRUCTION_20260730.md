# K16 provider-first radius two: exact interval CSP and quotient obstruction

Date: 2026-07-30  
Status: exact reduction and finite obstruction audit; no global NO_PASS  
Global bracket: `12873 <= nu(16) <= 12874` (unchanged)

## 1. Executive result

The provider-first complement of the global all-joint theorem has an exact
fixed-support formulation with only 32 value bits.  For a deletion and two
changed positions `p<q`, every required target gives one constraint

```text
P_t(u) OR Q_t(v) OR B_t(u OR v),
```

where each predicate is membership in an explicit Boolean interval.  Choosing
one witnessing role per target yields an exact three-role Hall/CSP, and a
given role assignment is decided by one 16-bit subset scan.

This removes arbitrary-mask enumeration **for a fixed physical support**.
It does not yield a feasible global census: there are

```text
1,066,618,984,872 deletion / unordered-position-pair supports.
```

The proposed first-action quotient cannot bridge this gap.  Any quotient that
preserves the exact signed first interval column is injective in the new cell
value.  Quotienting only by supplied-hole signature and output debts is not an
exact transition quotient; a literal K16 counterexample is recorded below.

## 2. Why exact signed first columns do not compress

Fix a deletion word, a changed position `p`, and a new value `u`.  Let
`N_u(t)` be the number of intervals containing `p` whose union is `t` after
the change.  Every such union contains `u`, while the singleton interval
`[p,p]` has union exactly `u`.  Therefore

```text
u = intersection { t : N_u(t) > 0 }.
```

Thus `N_u` determines `u`.  Since the old local column is fixed, the signed
column `N_u-N_old` also determines `u`.

> **Injectivity theorem.** At a fixed deletion and physical position, two
> distinct replacement values never have the same exact signed first column.

So retaining exact signed columns after a supplied-hole/signature grouping
recovers every literal value and provides no compression.

There is an exact numerical lower bound.  Across the `12,874` deletions there
are `116,073` deletion-hole incidences.  At each of the `12,873` remaining
positions, setting `u=h` supplies hole `h` as a singleton.  None of these is
an unchanged assignment: if a surviving cell equalled `h`, `h` would not be a
deletion hole.  Hence the first-provider atlas already contains exactly

```text
12,873 * 116,073 = 1,494,207,729
```

distinct genuine actions before optional values are included.

## 3. Debt/signature quotient is not transition-exact

The frozen best deletion word supplies a literal counterexample.  At first
position `0`, both values

```text
u_a = 11373,
u_b = 11332
```

install the unique original hole and leave exactly the same debts

```text
{18553,26745}.
```

At prospective second position `3236`, however, their exact private-target
sets differ:

```text
private_a = private_b union {11332}.
```

Their maximal second-value lower bounds are correspondingly different:

```text
state a: lower 27773, upper 2112,
state b: lower 27769, upper 2112.
```

Both happen to be infeasible, consistently with the already proved radius-two
no-go for this root, but their exact transition constraints are different.
Thus equal supplied-hole and debt sets do not determine the next exact column.
Using one representative is not a proof-preserving quotient.

## 4. Exact fixed-support service intervals

Fix a deletion word `w`, sites `p<q`, and a target `t`.

Partition affected intervals into:

1. `P`: intervals containing `p` but not `q`;
2. `Q`: intervals containing `q` but not `p`;
3. `B`: intervals containing both.

For role `P`, extend left and right from `p` as far as possible through
unchanged cells whose values are submasks of `t`, stopping before `q`.  Let
`C_t^P` be the OR of this maximal unchanged context.  It is an actual interval
context and contains every other compatible P-context.  Define

```text
a_t = t minus C_t^P.
```

Then a p-only witness exists exactly when

```text
a_t subseteq u subseteq t.                 (P_t)
```

Define `b_t` analogously for q-only intervals.  For both-cell intervals the
forced interior `p+1,...,q-1` must be a submask of `t`; otherwise role `B` is
unavailable.  When available, maximal compatible extension gives context
`C_t^B` and

```text
c_t = t minus C_t^B,
c_t subseteq (u OR v) subseteq t.          (B_t)
```

These are equalities, not relaxations.

## 5. Exact private-target formula

Let `H` be the original deletion holes.  In the deletion word compute the
exact old multiplicity of every target and the old multiplicity contributed
by intervals meeting `p` or `q`.  Put

```text
T = H union { t : every old witness of t meets p or q }.
```

Targets outside `T` retain an unchanged witness.  Therefore the two-edit word
is universal exactly when, for every `t in T`,

```text
P_t(u) OR Q_t(v) OR B_t(u OR v).           (1)
```

The provider-first complement additionally requires

```text
OR over h in H of (P_h(u) OR Q_h(v)).      (2)
```

Condition (2) is precisely the complement needed after the all-joint branch:
some original hole has a final witness containing exactly one edited site,
so that edit supplies it in the one-edit intermediate word.

## 6. Three-role Hall form

Choose for each `t in T` one role `rho(t) in {P,Q,B}` witnessing (1), with at
least one original hole assigned `P` or `Q`.  For a role assignment define

```text
L_u = OR_{rho(t)=P} a_t,
U_u = AND_{rho(t) in {P,B}} t,

L_v = OR_{rho(t)=Q} b_t,
U_v = AND_{rho(t) in {Q,B}} t,

L_z = OR_{rho(t)=B} c_t.
```

The value constraints are exactly

```text
L_u subseteq u subseteq U_u,
L_v subseteq v subseteq U_v,
L_z subseteq u OR v,
u,v nonzero and genuinely changed.
```

Ignoring only the final two inequalities, feasibility is equivalent to

```text
L_u subseteq U_u,
L_v subseteq U_v,
L_z subseteq U_u OR U_v.                  (3)
```

For the fully exact test, enumerate `u` in `[L_u,U_u]` (at most `2^16`
values), set

```text
R_v(u) = L_v OR (L_z minus u),
```

and check whether `[R_v(u),U_v]` contains a nonzero value different from the
old q-cell while `u` is nonzero and different from the old p-cell.  This is
necessary and sufficient.

The role CSP itself has a Hall-like forbidden-pattern description:

- two P targets conflict when their Boolean intervals are incompatible;
- likewise for Q and B;
- a P lower bound conflicting with a B upper bound forbids that P/B pair;
- likewise Q/B;
- a B-required bit forbidden by one P upper and one Q upper gives a ternary
  forbidden role triple.

Thus a fixed support is a small, exact three-role CSP followed by a 16-bit
value check.  The number of target variables is bounded by the distinct OR
labels in the three affected interval classes (at most a few hundred here),
not by `65,535`.

## 7. Why the global run is not presently feasible

The exact finite census gives:

```text
deletion hole sets                         12,874 distinct / 12,874
common-hole masks                           9,737 distinct
source left OR-chain profiles              12,874 distinct / 12,874
source right OR-chain profiles             12,874 distinct / 12,874
source paired left/right profiles          12,874 distinct / 12,874
unordered p,q pairs per deletion           82,850,628
deletion,p,q supports                    1,066,618,984,872
```

Consequently neither deletion holes nor one-site OR profiles supply a shared
parent quotient.  Even a constant-time fixed-support oracle would leave more
than a trillion supports.  The per-support CSP removes the value explosion but
not the positional explosion.

The next valid attack must therefore find a theorem on physical supports—for
example, a stabbing/locality theorem for private singleton witnesses, or a
shared interval-profile automaton across deletion and both sites.  Enumerating
the 1.494-billion injective first actions, or solving a tiny SAT instance for
every physical triple, is not an acceptable exact global strategy.

## 8. Authentication and scope

The counterexample engine enumerated all `27,064` provider actions of the
frozen one-hole deletion word, grouped them by first position and exact debt
set, and compared exact q-private/maximal-completion profiles.  It ran on one
low-priority H100 CPU in `3.67 s`, using `20,992 KiB` RSS and no swap.

Artifacts:

```text
scratch/audit_k16_provider_first_debt_quotient_counterexample_20260730.cpp
  SHA-256 c3e14b42d219da11ae258c1c549a2b168285056aa38fb5d25b8078745b90f74a

scratch/k16_provider_first_quotient_counterexample_20260730/audit.json
  SHA-256 bf8f7009d558aec26188b7662988b87d94d5a54895bb9da6740a50c6daf9bf57

scratch/audit_k16_provider_first_symbolic_complexity_20260730.py
  SHA-256 2f446f221e4199a162c8fb9e38323e775f910659afe8a4dfd92ff39cd16cb57f

scratch/k16_provider_first_symbolic_complexity_20260730.audit.json
  SHA-256 0819ffb8e1c8dd47409710ed10196d0b7738c3a7a365e69ba226728ad88a2bf2
  payload 698383c951a09bc33a2509ba9b59e218689472399afb1d5c501e40da60479f11
```

This theorem gives the smallest exact fixed-support provider-first model and
proves why the proposed global first-column quotient does not work.  It does
not exclude the provider-first branch and does not change the K16 bound.
