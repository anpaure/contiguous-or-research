# K16 special-cycle cost theorem: the separated master needs at least 98 cuts

Date: 2026-07-30

## Statement

For the frozen K16 length-eight source and its complete catalogue of 211,604
direction-coherent, positive-residence-safe seams, every selected port
permutation that services all 93 fixed q<=3 defects contains at least 98 seams
and cuts.

This is a direct solver-independent consequence of the denominator-20
weight/potential certificate and exact relaxed closed-walk costs through three
distinguished defects.  Those costs are lower bounds for physical selected
cycles.  The theorem supersedes the equality-face floors 95, 96, and 97.

## Reduced-cost accounting

For a seam `e : u -> v`, define

```text
rho(e) = 20 + phi(v) - phi(u) - weight(H(e)) >= 0,
```

where `H(e)` is the set of zero-baseline defects gained by `e`.  The total
weight of one copy of every defect is 1899.

If a selected port permutation has `C` seams, sum around its directed cycles.
The potential telescopes:

```text
20 C = A + R,                                              (1)
```

where `A` is the gained weighted service, including duplicate service, and
`R=sum rho(e)` is its total nonnegative reduced cost.  Coverage gives
`A>=1899`, hence

```text
R <= 20 C - 1899.                                         (2)
```

## Three unavoidable expensive cycle occurrences

Consider the three residual-block targets

```text
T = {46811, 56173, 60854}.
```

For each `t in T`, let `P_t` be its provider-seam bank.  Hardened raw replay
gives

```text
|P_t| = 60,
H(e) = {t} for every e in P_t,
P_s intersect P_t = empty for s != t.                 (4)
```

Thus the no-double-hit assertion is stronger than merely saying that one seam
cannot hit two members of `T`: a provider of a distinguished target hits no
other defect at all.

Give the entire 211,604-seam directed graph the exact nonnegative arc lengths
`rho`.  For a specified provider seam `a:u->v`, a closed walk containing it
costs at least

```text
rho(a) + shortest_rho_path(v,u).
```

For nonempty `S subset T`, define `f(S)` to be the minimum `rho`-cost of a
closed directed walk in the complete seam graph which contains a member of
`P_t` for every `t in S`.  For fixed cyclically ordered marked provider arcs
`e_i=(u_i,v_i)`, its permissive relaxation has exact cost

```text
sum_i rho(e_i) + sum_i dist_rho(v_i,u_(i+1)).          (5)
```

Minimizing (5) over the marked arcs and all cyclic orders gives the exact
closed-walk values

```text
f({t}) for every t in T                                     17
f({s,t}) for every specified pair                           39
f(T)                                                        55
```

Now choose one selected provider occurrence for each member of `T`.  The
selected directed cycles partition those three marked occurrences.  If a
selected cycle receives the marked target set `S`, it is itself an admissible
closed walk in the definition of `f(S)` and hence has cost at least `f(S)`.
Therefore every possible partition among selected cycles costs at least

```text
three singletons:        17+17+17 = 51
one pair + singleton:       39+17 = 56
one triple:                       55
```

so in every feasible selected port permutation

```text
R >= 51.                                                   (3)
```

The shortest-path calculation is permissive: return segments may repeat
vertices or arcs and different target cycles need not be disjoint.  It is
therefore a lower bound for actual vertex-disjoint selected cycles.

Equivalently, giving each member of `T` cycle-dual weight 17 is valid: a
selected cycle that services `j=1,2,3` distinct members has cost at least
`17j`, with margins respectively 0, 5, and 4.

## Cut floor

Combining (2) and (3),

```text
51 <= 20 C - 1899,
```

and consequently

```text
C >= ceil((1899+51)/20) = ceil(97.5) = 98.
```

QED.

## Exact 98-cut face

The same proof sharply constrains equality at 98 cuts.  Put

```text
D = A - 1899 = sum_t weight(t) (mu_t - 1),
```

where `mu_t` is the service multiplicity.  At `C=98`, (1) says

```text
R + D = 61.
```

Since `R>=51`, one has `D<=10`.  The least target weight is 11, so `D=0`:
every defect is serviced exactly once and `R=61`.  According as the three
distinguished providers lie on three cycles, two cycles, or one cycle, their
partition consumes at least 51, 56, or 55 reduced-cost units, leaving at most
10, 5, or 6 units elsewhere.  This is an equality-face restriction, not an
existence result at 98.

## Sound eager row

The exact full q<=3 separated-port master may safely add

```text
cut_count >= 98
```

as a redundant propagation constraint.

## Scope

This theorem is source-relative to the frozen direction-coherent,
q<=3/upper-width-four separated seam catalogue.  It uses no cut separation,
reverse-edge, q1, survivor, residence, or deeper-shadow condition, but it does
not rule out a different K16 carrier or a non-separated transformation.

## Audit lineage

```text
binary seam catalogue
  scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

weight/potential certificate
  scratch/k16_provider_weight_potential_floor95_20260730.audit.json
  SHA-256 7d64defc48cdacbde21aeab3757d051bc2a63623f263d110eb5922749db44e56

hardened three-target cycle-partition audit
  scratch/threadA_k16_balanced_service_floor98_20260730.audit.json
  SHA-256 b6ecb5104cdaabcf52d3fa1fad02ded9a3b659431396224da528782ce9fc178a

cycle-partition checker
  scratch/audit_k16_exact96_special_cycle_cost_20260730.py
  SHA-256 154036ed7aed97e86fd1ead9eb6d555e5d2ac4483201a2673aec57370ccaf861

H100 resource ledger
  scratch/threadA_k16_balanced_service_floor98_20260730.resource.txt
  SHA-256 09170685431ce87c8b6fe761dbfb6a1a9c5ee2eb8891effca4dc1f7b49e8e04a

independent reverse-Dijkstra partition audit
  scratch/threadA_k16_balanced_service_floor98_independent_20260730.audit.json
  SHA-256 d9ef077f2df7682fe93f6c1c959676a16b5d1ebe43ae250030d2592530385b7a

independent reverse-Dijkstra checker
  scratch/threadA_verify_k16_balanced_service_floor98_20260730.py
  SHA-256 3922929a6ac317d747691897a5d65478b58e8ac6565a9db0e864a94b8fd3888f

independent per-target Dijkstra audit
  scratch/k16_floor97_target_cycle_cost_independent_20260730.audit.json
  SHA-256 9dca9e7085a583e85de918361a0ebca17ed7a0c63b10c60f0c125c197126744e

independent per-target checker
  scratch/audit_k16_floor97_target_cycle_cost_20260730.py
  SHA-256 dd139cee912d24aa8ac9093cfd3e8ecf381b5755ae729403a7d1ce46b8315a07
```

The independent audit separately confirms that all three single-target cycle
minima are 17.  The partition audit supplies the pair and triple minima needed
to make the 51-unit bound unconditional under every cycle partition.

The older compact artifact
`scratch/k16_exact96_special_cycle_cost_20260730.audit.json` (SHA-256
`3cf4a515...`) is retained only as historical lineage: it records the
historical generating-driver hash `6aabff...`.  The hardened primary checker
reproduces the singleton/pair/triple closed-walk values `17/39/55`, pins the
raw binary and certificate, verifies (4), and adds the cycle-hypergraph-dual
diagnostics.  The independent checker parses through a separate canonical
parser and uses reverse rather than forward Dijkstra.  The definitive primary
replay command is:

```text
python3 scratch/audit_k16_exact96_special_cycle_cost_20260730.py \
  --binary scratch/k16_len8_source_seam_ledger_20260730.bin \
  --certificate scratch/k16_provider_weight_potential_floor95_20260730.audit.json \
  --output NEW_OUTPUT.audit.json
```
