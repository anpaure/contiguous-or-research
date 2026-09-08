# K17 h1 full-q1 ordered-overlap packet circulation theorem

**Date:** 2026-08-02  
**Status:** exact finite-state theorem, calibrated at an independently audited
frozen checkpoint.  
**Scope:** ordered state-relative `C6` and four-petal star-`C8` packets.  No
catalogue-completeness, regenerative-expansion, source, compiler, resident, or
word claim is made.

## 1. Frozen calibration and three residence counts

Let `F_*` be the primary factor

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
    checkpoint_fullq1_escape_res1994/model
SHA256 127f97f02d238215367a1d5291853e0dd7ecb6d2d227cfcfed1c365e68d5ebcd
```

The frozen passive and independent replays give the following data.

```text
ordinary necessary non-D provider palette       19412 / 19412
opened rank-10 deck, orientation 0              19448 / 19448
opened rank-10 deck, orientation 1              19448 / 19448
opened short-run histogram, orientation 0       (1267,727)
opened short-run histogram, orientation 1       (1268,726)
opened residence, both orientations             1994
opened upper holes, both orientations            (0,1520,271,4,0,0,0,0)
opened deep aggregate, both orientations         1795
```

The two opened orientations have different length-`1,2` splits but the same
total and upper profile.  The ordinary auxiliary component histogram is
`(0,1267,725)`, its cyclic total is `1992`, and the passive cut count is
`1993`.  These are different observables; none may be substituted for the
opened objective `1994`.

The frozen checkpoint is bound by

```text
MANIFEST.sha256
  SHA256 0dc6f0fbba8b9d8e509811b329e02bd35ec6493d1b82c92cf28969bc26aef714
passive.audit.json
  SHA256 9673e703985640504c41b95953cc96134be2a481639312ca59f553deaaab2343
independent.audit.json
  SHA256 6bae984f36d2d72ca65af39e2e8438ef488404f21d8446e487c034037783e148
provenance.summary.tsv
  SHA256 bc160c262b23f9977902fe02ddf4ea5bdc9d0f7b4c4135c51d2cbc8d2352081f
```

The stable manifest binds exactly the displayed model, passive audit,
single-model independent audit, and provenance summary.  The independent
audit passes degree, boundary, the `16,261` frozen guards, exact ordinary q1
providers, lollipop connectivity, and passive literal chronology at this
endpoint.  Its explicit exclusions are residence success, arbitrary-width
deeper-upper success, source, compiler, and a universal word.  None of the
abstract theorems below depends on the numerical calibration.

An earlier transient expanded manifest/audit pair with SHAs `76e29482...` and
`e444dbc0...` and lineage SHA `3492efa5...` remains visible as separate
evidence, but is not part of the current canonical checkpoint and is not used
to enlarge its independent-audit scope below.

The exact face below also retains the frozen `16,261` guard clauses, the named
protected boundary branch, exact incidence degrees and boundary conditions,
and one augmented-incidence component.  The theorem treats those rows as
literal predicates to replay, not as consequences of the four displayed
scores.

## 2. The strict full-q1 face

For a primary selection `y`, rebuild every derived ordinary-pair variable and
write

```text
chi(y) = (y,p(y)),                 p[q,a,b]=y[q,a]y[q,b].       (2.1)
```

Let `n_U(y)` be the exact provider load of ordinary necessary non-D target
`U`.  For opened orientation `omega in {0,1}`, let `L^omega_r(U;y)` be the
exact opened witness load of rank-`r` target `U`, obtained by replaying that
whole opening.  Define `X` to be the factors satisfying all of the following.

1. `y` is binary and obeys every exact owner/facet degree and boundary row.
2. Every one of the `16,261` frozen clauses is true under `chi(y)`.
3. `n_U(y)>=1` for all `19,412` ordinary necessary non-D targets.
4. `L^omega_10(U;y)>=1` for all `19,448` rank-ten targets and both
   `omega=0,1`.
5. The named protected branch is unchanged.
6. The full augmented-incidence graph has exactly one component.

An **ordered strict packet** from `F in X` is a sequence

```text
q_1,...,q_t,        F_0=F,        F_i=q_i(F_(i-1)),       (2.2)
```

in which `q_i` is an alternating `C6` or four-petal star-`C8` in the current
state `F_(i-1)` and every `F_i` lies in `X`.  Thus every strict prefix, not only
the terminal union, preserves both full opened decks and all other hard rows.
Residence and ranks `11,12,13` may be neutral or worse at a prefix.

No root-disjointness condition occurs in (2.2).  Supports and roots may
overlap, provided the displayed order remains alternating, binary, and in
`X`.  A move deleted by one prefix may therefore disappear from the next
catalogue, and a move absent at the root may become alternating later.

## 3. Exact one-opening and two-opening objectives

For one complete opening put

```text
v_omega(F)=(R_omega(F),h^omega_11(F),h^omega_12(F),h^omega_13(F)). (3.1)
```

All four entries in (3.1) must come from the same opening.  The exact
best-common-opening objective is

```text
Psi_min(F)=min_lex {v_0(F),v_1(F)}.                        (3.2)
```

This permits the winning orientation to change, but never permits
coordinatewise mixing.  If both orientations are to be retained in the
objective, sort the two complete vectors and use

```text
Psi_2(F)=(v_(1)(F),v_(2)(F)),     v_(1)<=_lex v_(2).      (3.3)
```

At the authenticated frozen root,

```text
v_0(F_*)=v_1(F_*)=(1994,1520,271,4).                      (3.4)
```

For (3.2), the exact K17 mixed-radix scalar is

```text
S(R,h11,h12,h13)
  = (((R*12377+h11)*6189+h12)*2381+h13).                 (3.5)
```

Indeed `h11<=C(17,11)=12376`, `h12<=6188`, and `h13<=2380`.
The coarse global bound `R<=17(24310+1)=413287` is sufficient.  Hence one
unit in any earlier coordinate in (3.5) outweighs every possible change in
all later coordinates.  Also

```text
S(Psi_min(F_*)) = 363703240664577,
S_max            = 75378599565326176,                    (3.6)
```

so the one-opening scalar fits a signed 64-bit integer.  For `Psi_2`, use
successive lexicographic optimal faces.  The formally equivalent scalar
`S(v_(1))(S_max+1)+S(v_(2))` requires wider arithmetic; no 64-bit claim is
made for it.

## 4. Cycle-space projection versus ordered realizability

Let `A` contain the linear exact-degree, facet, and fixed-boundary equations.
For an ordered packet write

```text
z_i=y(F_i)-y(F_(i-1)).                                   (4.1)
```

Every primitive has `A z_i=0`, and consequently its terminal displacement
lies in the integer cycle space:

```text
y(F_t)-y(F_0)=sum_i z_i in ker_Z(A).                      (4.2)
```

Equation (4.2) is necessary but not sufficient.  It forgets binary prefix
occupancy, current-state alternation, the nonlinear variables `p(y)`, last
provider loads, the two opened chronologies, protected rows, and connectivity.
In particular, symmetric-difference or matroid circuit decomposition does
not prove that its circuits can be ordered inside `X`.

Conversely, a vector in `ker_Z(A)` is realizable by the declared primitives
with strict full-q1 prefixes exactly when it has a decomposition (4.1) whose
materialized states satisfy (2.2).  This is an equivalence, but the right-hand
side is an ordered lifted-state property rather than a static cycle-space
property.

The conservative root-disjoint batch is therefore a subgraph of the exact
builder below: it fixes a root catalogue and keeps only commuting proposals
with disjoint roots.  Its plateau is not a dual certificate for the larger
state-relative graph.  It omits at least same-root revisits, overlapping
ordered supports, and circuits enabled only after a prefix.

### 4.1 Exact scope of the strict18 zero-acceptance result

Let `F_P` be the independently frozen prior plateau

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
    checkpoint_fullq1_res2025/model
model SHA256    5499b2fb492a6307e531bf33f20341a3e1c89c44cd45e0ee88ae6a8556c5e4fa
manifest SHA256 5a1186ca9c4f205a33b754f11a6afae1b66d850874d4b9a5833582f9ae134022
independent audit SHA256
                0e5c580a9233b88f2610d40c7fdcbf64582cb2f0a9e52d555ec7563987046d08
```

It has

```text
Psi_min(F_P)=(2025,1521,279,4),    ordinary auxiliary residence=2023. (4.3)
```

The strict18 audit takes the identical `fullq1_strict17.best.model` as input.
Its SHA is

```text
14b0d6e09eb6b72ea0d4dbf741dc1815421910323d0df731c4a46131afd78f74.
```

This strict18 audit is a separate downstream artifact and is **not** a member
of the frozen `checkpoint_fullq1_res2025` manifest.  It is used here only for
the narrowly stated zero-acceptance observation below; no manifest or
independent-audit status is transferred to it.

Within its declared actuator it reports

```text
guard-safe root catalogue                     14119
lossless ordinary-residence-improving moves       0
greedy batch accepted moves                        0
chosen catalogue ids                              []
```

This is an exact no-go only for that audited greedy direct/static-candidate
face.  In particular, its optimized residence is the ordinary auxiliary
value `2023`, not the opened value `2025`, and its scope explicitly excludes
the deeper-upper objective.  The zero count does **not** say that there is no
hard-row-legal neutral or worsening root arc: the guard-safe catalogue itself
is nonempty.  It also does not enumerate the regenerated second-layer
catalogue after such an arc, overlapping or same-root paths, or debt-bearing
pairs and triples.  Therefore it supplies neither the unreachable Farkas
certificate (5.7) nor the nonnegative potential (5.8) for `Gamma_L(F_P)`.

Equivalently, the zero-acceptance result closes a filtered subgraph
`Gamma_greedy(F_P)` of `Gamma_L(F_P)`.  A negative ordered packet remains
possible precisely through the suffix inequality (6.3).  Deciding that
possibility requires either an exact negative path in the larger graph or its
exact dual potential; a zero greedy batch is neither.

### 4.2 Authenticated two-stage neutral escape: exact finite scope

Let `F_E` denote the independently frozen residence-2018 endpoint with model
SHA `c8f961413aeea43cbad5036e801c08f854f84889eaef11c281aa83bea46c057d`
and checkpoint-manifest SHA
`224499fd6c3df28d7f0c656a4a53dd73a7fc9b9467418e01f2c3adaef6880957`.
The visible seed-2 actuator chain from `F_P` to `F_E` has the following
hash-bound artifacts.

| artifact | SHA-256 | declared role |
|---|---|---|
| `escape_s2_bridge.audit.json` | `77cbcd9cff041446208984d0b6a8b5e6b6e9c281f62ed81cfc2e4b1bc152e28e` | neutral bridge audit from `F_P` |
| `escape_s2_bridge.best.model` | `748bc5cfe639028fd6642f044249740f333e5849556c9684af551e4f7356ef64` | bridge endpoint `F_B` |
| `escape_s2_quench.audit.json` | `8976bfd4854338672de88dfe0036cdddf46c46095c164d836056e1be1890d280` | state-relative quench audit from `F_B` |
| `escape_s2_quench.best.model` | `c8f961413aeea43cbad5036e801c08f854f84889eaef11c281aa83bea46c057d` | terminal, identical to frozen `F_E` |

The first stage chooses catalogue id `2508` with a neutral budget of one.  It
keeps ordinary auxiliary residence `2023`, all `19,412` ordinary necessary
providers, the `16,261` guards, the protected boundary, and connectivity.
The second stage regenerates at `F_B`, where it chooses ids
`2446,12688,2243`; its terminal has ordinary auxiliary residence `2016` and
is exactly the independently frozen `F_E`.  The declared
guard-safe root catalogue changes from `14,119` at `F_P` to `14,122` at
`F_B`, a direct finite marker that the neutral move changed the next proposal
state.  At the two frozen endpoints,

```text
Psi_min(F_P)=(2025,1521,279,4),
Psi_min(F_E)=(2018,1518,278,4),
S(Psi_min(F_E))-S(Psi_min(F_P))=-1276757294159.           (4.4)
```

The current canonical residence-1994 independent audit is a single-model
endpoint audit; it does not reconstruct these four historical prefixes.  The
transient expanded audit `e444dbc0...` reported such a replay, but it is not
bound by the stable checkpoint manifest.  Therefore (4.4) is hash-bound
two-stage actuator and frozen-endpoint evidence for the Section 6 mechanism,
not a canonical proof of `mu_4(F_P)<0`.  It still shows why zero acceptance in
the filtered strict18 greedy face is not a dual certificate for a regenerated
builder.  The separately audited true pair in Section 4.4 supplies the exact
strict-prefix theorem instance.

### 4.3 Repeated bridge/quench endpoints and what they prove

Starting at `F_E`, seed13 applies three further named bridge/quench phases.
The phase endpoints and physical move counts are

| endpoint | bridge + quench moves | `Psi_min=(R,h11,h12,h13)` | deep sum |
|---|---:|---|---:|
| `F_E` | -- | `(2018,1518,278,4)` | 1800 |
| `F_1` | `2+3=5` | `(2013,1522,276,4)` | 1802 |
| `F_2` | `3+5=8` | `(2003,1518,273,4)` | 1795 |
| `F_*` | `5+4=9` | `(1994,1520,271,4)` | 1795 |

Every displayed phase endpoint is lexicographically lower because its
residence coordinate falls, even though the first phase increases the deep
sum.  The canonical provenance summary binds residence, deep totals, and
move counts.  The displayed rankwise splits come from separate phase-passive
audits with SHAs `d75814e0...`, `29a69dbb...`, and `9673e703...`; only the
last is a canonical checkpoint member.  The endpoint scalar differences are

```text
S(Psi_min(F_*))-S(Psi_min(F_E)) = -4377272546081,
S(Psi_min(F_*))-S(Psi_min(F_P)) = -5654029840240.         (4.5)
```

The transient expanded lineage reported `22` valid physical prefixes, but is
noncanonical under the current freeze; hence this note does not turn the two
differences in (4.5) into claims about `mu_22` or `mu_26`.  The endpoints are
repeated **evidence** of regeneration on visited roots, not a uniform motif
theorem.  The stages named `bridge` after `F_E` may already contain improving
moves; the repeatable semantic object is therefore a bounded exploratory
bridge followed by a regenerated quench, not one fixed literal circuit or an
always-neutral first move.  Seed11's separately reported endpoint `1995` is
not promoted to an additional theorem claim here.

### 4.4 Independently isolated shared-root C6/C6 provider handoff

There is a separate, hash-bound length-two certificate inside seed13
iteration 3.  Let `F` be the state after the first four direct bridge moves,
and define

```text
A: C6 core 24136, labels (5,7,15), roots (24168,24264,56904),
B: C6 core  7880, labels (0,2,14), roots ( 7881, 7884,24264). (4.6)
```

The circuits share exactly root `24264`, although they toggle different
incidences there.  Thus a root-disjoint batch excludes the pair.  The frozen
packet has SHA
`f930f8563e62e843b65872bf8bd9c1e5da42856784b6291602f32b636bfe50b3`,
and its independent materialization audit has SHA
`533a973be249590648d319b30cbb412aa63adc3212a6aeb0c9c92f6959d4d4f6`.

| state | model SHA prefix | hard-face status | opened `R` | holes `(h11,h12,h13)` |
|---|---|---|---:|---:|
| `F` | `9d0a16a0` | full q1/guards/connected | 1999 | `(1522,270,4)` |
| `A(F)` | `73234ce2` | full q1/guards/connected | 1999 | `(1521,270,4)` |
| `B(F)` | `dca857e4` | blocked: one ordinary/opened q1 hole and one guard row | 1999 | `(1522,271,4)` after the rank-10 hole |
| `B(A(F))` | `4fc61f19` | full q1/guards/connected | 1997 | `(1519,270,4)` |

The full primary-model SHAs are

```text
F          9d0a16a07df123044859e212a4a486dcded7cb8d74731009418537f285a033ab
A(F)       73234ce27d5b5b15f01d1e349a807a026f5d18167f7c21a53bbbd13c3f47e818
B(F)       dca857e43751b979cf2a664cde61c3c12f877c4bfc01439b0ac4af5a90361bb6
B(A(F))    4fc61f197379a89f2f4647cf97134271c925e44d8c6608aa2e0fc38126f1642f
```

The independent single-model audit SHAs for `F,A(F),B(A(F))` are respectively
`3cca0672a8034d1cb4f0bc3ed8d4de7f8fc8734b8bcb85da703c0ec4964903e4`,
`fd9083989d820c6ec43da70de1b5b19ae4421aa60b6f296421f426f58c48b4f6`,
and `d5cd4fff3ac582ca5d54e9b28f93198d275f910bb07221d0996270af335027ae`.
Their passive audit SHAs are `c8fb3756f23a2772a75a3a6f7c69019703554c701e1d798ce20fcfdf10c74097`,
`9d540e742bf50036e6672fbfc47ae6db3a3a7aaa7ab260011460301f83554b95`,
and `173107e99e9888955eb046a3c6631aed214fa7e6b963932b39ebdd0abad71f0c`.
The counterfactual `B(F)` passive audit has SHA
`79143c27634bfbf1470e284f40a3a2e18575551b717d62dd9e904110618a8f91`.
These pair artifacts are separate from the canonical residence-1994
checkpoint manifest.

The exact failed-row audit has SHA
`8e8d9ae90384c3f04c59a47c9e3ff8afca10b911232053ab0c046f600c67ea20`;
its one-row TSV has SHA
`c5aa9f3688829c92bdeb2d68161c5509fd5934263568a64e922a25103b040565`.
The independently reconstructed guard-cut audit has SHA
`3a307521c607cda4b74ca3514b97be01c0dcd6ac29247628ced711135da97cf1`
and is bound by its separate manifest SHA
`68464a331aa213d82c3b7fe3f94c79805cf8c769798bfa2d4c3122a444147fd8`.

The unique failed guard is zero-based row `12668`, one-based row `12669`.
It is the positive `45`-literal Hall/q1 provider cut for

```text
U=24300={2,3,5,6,7,9,10,11,12,14},
C_U = OR_(p in P(U)) p,                  |P(U)|=45,
equivalently sum_(p in P(U)) p >= 1.                     (4.7)
```

On the audited four-state square, `43` literals are identically false and
the only possible live providers are

```text
p_old = p262698 = y10993 AND y10996
      = p(root 7884; owners 7916,24268),
p_new = p387503 = y42195 AND y42197
      = p(root 24264; owners 24268,24296).                (4.8)
```

Their exact truth table is

| state | `p_old` | `p_new` | `C_U` | ordinary/opened holes at `U` |
|---|---:|---:|---:|---:|
| `F` | 1 | 0 | 1 | `0/(0,0)` |
| `A(F)` | 1 | 0 | 1 | `0/(0,0)` |
| `B(F)` | 0 | 0 | 0 | `1/(1,1)` |
| `B(A(F))` | 0 | 1 | 1 | `0/(0,0)` |

The nonlinear point is exact: A alone plants half-edge `y42197`, B plants
the complementary `y42195` while deleting `y10996`, and only their ordered
composition makes `p_new=y42195*y42197` true.  Thus the provider load follows
`1,1,0,1`; equivalently the guard truth has mixed Boolean finite difference
one.  B is alternating, degree/topology applicable, and connected at `F`, but
is absent from the strict full-q1 graph because it leaves `19411/19412`
ordinary targets, one opened rank-ten hole in each orientation, and exactly
the failed row (4.7).  After A, B is a legal state-relative arc.

The pair is a genuine minimal **residence-decreasing** packet:

```text
Delta R(A|F)=0,       B is hard-blocked at F,
Delta R(B|A(F))=-2.                                      (4.9)
```

For the full lexicographic objective, A already lowers `h11` by one, so no
claim of lexicographic length-two minimality is made.  Nevertheless the
ordered pair is strictly negative and gives

```text
S(Psi_min(B(A(F))))-S(Psi_min(F))=-364819374813,
mu_2(F) <= -364819374813 < 0.                            (4.10)
```

This is a pointwise K17 certificate.  It proves neither that every blocked
primitive has such a handoff nor that the mechanism renews at the next root.

### 4.5 Canonical-root activated C6/star-C8 minimal pair

A stronger pair starts directly at the canonical residence-1994 factor
`F_*`.  Its constituents are

```text
A: C6 core 7946, labels (4,14,7), roots (7962,24330,8074),
B: star-C8 core 5914, labels (11,14,15,13),
   roots (7962,22298,38682,14106).                        (4.11)
```

A replaces incidence variables

```text
11156,42258,11437  ->  11158,42261,11433,
```

and B then replaces

```text
11158,37889,68776,22443  ->  11157,37887,68777,22445.    (4.12)
```

Thus the circuits overlap at root `7962`, and B is not alternating at the
root: it requires selected incidence `11158`, which A installs.  B is absent
from the root catalogue rather than merely rejected by an objective filter.

The search witness audit has SHA
`e081853a125821c406804f6f6062fd2ddd328e928d9863b0365792b0bfd19d72`;
the packet TSV has SHA
`415240ce187d0e2caadcbb3d5c7f43ce92914a19d08352444c579664d59b7538`.
Independent materialization has SHA
`b7b8f48a1029b38cf77753bdaaee2fbb3eba5bda32756d14e562a137616e15b3`.
The prefix and terminal primary models are

```text
A(F_*)       a73b5fe36e4bd7944c275ffefed5181d502370e9d08ef059c834f39b9fa8142b
B(A(F_*))    a9f0d53bdee43fc5db770ecac57781899c4d0f4fbed3b83ca0ac8b6af00008dd
```

Both prefixes pass independent degree/boundary, all `16,261` guards, ordinary
q1, protected boundary, connectivity, and passive opened replay.  Their
independent audit SHAs are
`934dbf0d9ff2b908d9b783c10bf1999eb02a1ca82df434db1edd4891119bc4d7`
and `eb54a9bd5a06e32878d8c9c3f7415c9ab97e5199848c653e7c8f4e3947ca6874`;
their passive audit SHAs are
`569ce1d005d7f714618ae894fcb506ff6a79a4ff7caf7fa98174ff9ed8b453be`
and `ba04d2df64a0d7087dbac0668fd7d3a9a5d8f359775ec168cb163a4694ee7dbb`.
Both also pass the complete `7,163,170`-clause DIMACS replay; the audit JSON has SHA
`777306ca8ae7cb641d9dc98522b8fa797d9088679764d593d007e169b4e0c224`.

The exact opened profiles are

```text
Psi_min(F_*)       = (1994,1520,271,4),
Psi_min(A(F_*))    = (1994,1520,271,4),
Psi_min(B(A(F_*))) = (1993,1521,271,4).                  (4.13)
```

Hence A has exactly zero cost, while the ordered pair is negative.  For the
aggregate tuple `(R,Hdeep)`, the exact radix

```text
S_agg(R,Hdeep)=21779 R+Hdeep
```

gives `Delta S_agg=-21779+1=-21778`.  For the finer scalar (3.5),

```text
Delta S=-182387583393+14736009=-182372847384,
mu_2(F_*) <= -182372847384 < 0.                          (4.14)
```

This is a genuine minimal pair for its two displayed constituents: A is
neutral and B is root-inapplicable, while A;B is a strict negative packet.
The search was sampled and does not prove that no unrelated root singleton
improves `F_*`.  Nor does this pair prove renewal at its residence-1993
terminal.

## 5. Markov-complete lifted builder

Fix a physical length bound `L`.  A proof-safe vertex contains either the
whole materialized factor or an injective equivalent of

```text
Sigma=(i,y,chi, all guard slacks, all n_U,
       all L^0_10(U), all L^1_10(U),
       degree/boundary/protected ledgers,
       full component/port state Pi,
       opened trace states Theta_0,Theta_1,
       v_0,v_1).                                         (5.1)
```

Here `i<=L` is the number of physical primitives already used.  Aggregate
hole counts, a scalar component count before materialization, or root labels
alone are not Markov-sufficient quotients of (5.1).

Let `Gamma_L(F)` have root `s=(0,F)`.  From every retained state regenerate
the complete declared `C6`/star-`C8` catalogue and add precisely the moves
whose materialized heads are in `X`.  Put

```text
c(u,v)=S(Psi_min(F_v))-S(Psi_min(F_u))                    (5.2)
```

on a physical arc.  From every nonroot retained state add a zero-cost analytic
arc to a sink `tau`.  Analytic arcs do not count toward `L`.  Costs telescope,
so an `s`--`tau` path has cost

```text
S(Psi_min(F_terminal))-S(Psi_min(F)).                     (5.3)
```

For `Psi_2`, replace (5.2) by its eight-coordinate vector difference and use
successive lexicographic faces.

### Theorem 5.1 (exact min-cost path and normalization)

Let `N` be the head-minus-tail node-arc incidence matrix of `Gamma_L(F)` and
`b=e_tau-e_s`.  Then

```text
mu_L(F)=min {c^T f : Nf=b, f>=0}                          (5.4)
```

has an integral path optimum whenever `tau` is reachable, and
`mu_L(F)<0` if and only if the declared builder contains a strict ordered
packet of length at most `L` decreasing (3.2).

Equivalently, add one zero-cost reset arc `rho:tau->s` and impose

```text
N_hat f=0,       f>=0,       f_rho=1.                    (5.5)
```

The normalized circulation (5.5) has the same optimum.  The equation
`f_rho=1` is essential: without it the zero circulation is always feasible,
while an unnormalized negative accepting cycle can be repeated without bound.

#### Proof

The physical graph is layered, hence acyclic.  The network unit-flow
polytope is integral, and every integral feasible flow in (5.4) contains one
`s`--`tau` path.  Removing any nonnegative extraneous flow cannot improve over
the cheapest such path; no physical directed cycle exists.  Equation (5.3)
then proves the first equivalence.

In the augmented graph every directed cycle uses `rho`.  Fixing its flow to
one forces exactly one unit of accepting flow from `s` to `tau`; deleting or
adding `rho` gives the bijection with (5.4).  This proves (5.5).  \(\square\)

For the vector objective, start with the unit-flow polytope `P_0` and set

```text
mu_j=min {c_j^T f:f in P_(j-1)},
P_j=P_(j-1) intersect {f:c_j^T f=mu_j}.                   (5.6)
```

Every `P_j` is a face of an integral network polytope, so an integral
lex-optimal accepting path remains.  This applies directly to either (3.2)
or the exact two-orientation objective (3.3).

### Theorem 5.2 (Bellman--Ford/Farkas alternative)

Exactly one applicable branch holds.

1. If `tau` is unreachable and `R_s` is the root-reachable set, then
   `z=-1_(R_s)` satisfies

   ```text
   N^T z<=0,              b^T z=1,                        (5.7)
   ```

   which is a Farkas certificate that (5.4) is infeasible.
2. If `tau` is reachable and `mu_L(F)<0`, an integral negative ordered packet
   exists.
3. If `tau` is reachable and `mu_L(F)>=0`, there is a potential `pi` with

   ```text
   pi[v]-pi[u]<=c(u,v)   for every arc u->v,
   pi[tau]-pi[s]=mu_L(F)>=0.                              (5.8)
   ```

   It certifies that every accepted packet in this exact finite builder is
   nonnegative.

Adding the reset inequality `pi[s]-pi[tau]<=0` gives the equivalent
no-negative-cycle Bellman--Ford certificate.  These are exhaustive only for
the declared primitive family, state encoding, and length bound.  Sampling
failure or exhaustion of the root-disjoint subgraph supplies none of (5.7)--
(5.8) for the overlap graph.

#### Proof

If `tau` is unreachable, no arc leaves `R_s`.  With the head-minus-tail
convention this gives `N^T(-1_(R_s))<=0`, while
`(e_tau-e_s)^T(-1_(R_s))=1`; multiplying a hypothetical feasible unit flow by
this vector gives the contradiction `1<=0`.  If `tau` is reachable, network
integrality and Theorem 5.1 identify a negative optimum with a negative
packet.  Otherwise linear-programming duality for (5.4) gives
`N^T pi<=c` and `b^T pi=mu_L(F)`, which are exactly (5.8).  Conversely,
summing the arc inequalities along any accepting path lower-bounds its cost
by `pi[tau]-pi[s]>=0`.  \(\square\)

## 6. Exact preconditioner criterion when root singletons are blocked

For a retained state `v`, define the bounded suffix value recursively by

```text
D_0(v)=0,
D_r(v)=min(0, min_(v->w physical) {c(v,w)+D_(r-1)(w)}).   (6.1)
```

The zero option means stop and take the analytic sink arc.  Suppose every
legal root primitive is objective-blocked:

```text
c(s,v)>=0                    for every physical s->v.     (6.2)
```

Then a negative strict compound packet of length at most `L` exists if and
only if

```text
min_(s->v physical) {c(s,v)+D_(L-1)(v)} < 0.             (6.3)
```

Thus an objective-neutral or worsening first primitive can be a genuine
preconditioner exactly when its regenerated suffix is more negative than its
initial debt.

For two primitives, (6.3) says precisely that there are

```text
F_1=q_1(F),       F_2=q_2(F_1),
c(F,F_1)>=0,      c(F,F_1)+c(F_1,F_2)<0,                 (6.4)
```

with `F_1,F_2 in X`.  The second circuit may be absent at the root, or may
have nonnegative root cost; only its state-relative arc and cost in (6.4)
matter.  Three primitives obey the identical condition with three
telescoping costs.  More explicitly, if no negative packet of length at most
two exists, a minimal negative triple is exactly an ordered path in `X` with

```text
c_1>=0,        c_1+c_2>=0,        c_1+c_2+c_3<0.         (6.5)
```

The inequalities are prefix objective statements only; all three prefixes
already satisfy every hard row by membership in `X`.

### Corollary 6.1 (quadratic last-provider handoff)

Let a required positive provider cut be

```text
C_U = OR_(p in P(U)) p,          p=y_i AND y_j.           (6.6)
```

Suppose `F in X`, A is a legal primitive with `A(F) in X`, and B is
alternating and incidence/topology applicable at `F`.  Assume the following
four-state identities.

1. `p_old=y_r*y_d` is the last live provider of `C_U` at `F` and `A(F)`.
2. B changes `y_d:1->0` and `y_b:0->1`; A changes `y_a:0->1`, leaves
   `p_old` live, leaves the incidences needed by B available, and B remains
   state-relative alternating after A.
3. `p_new=y_b*y_a` is another literal of `C_U`; B alone leaves `y_a=0`, and
   all other provider literals remain false on the four-state square.
4. Every other hard row holds at the retained prefixes `F,A(F),B(A(F))`, and
   the terminal objective is lower than at `F`.

Then

```text
(p_old,p_new,C_U):
F         = (1,0,1),
A(F)      = (1,0,1),
B(F)      = (0,0,0),
B(A(F))   = (0,1,1).                                    (6.7)
```

Consequently B is hard-blocked at the root by the last-provider cut, but A
followed by B is a legal negative strict packet.  Its guard truth has mixed
Boolean finite difference one.  This conclusion is an exact consequence of
the deterministic quadratic `p=y*y` channel; a linear incidence cycle-space
or scalar provider count without the two half-edges cannot prove it.

#### Proof

Conditions 1--3 give (6.7) by direct Boolean multiplication.  Condition 4
puts both retained prefixes in `X`, so the displayed order is a strict path;
the endpoint inequality makes its telescoping cost negative.  \(\square\)

The Section 4.4 instance has `|P(U)|=45`,

```text
(y_r,y_d,y_b,y_a)=(y10993,y10996,y42195,y42197),
(p_old,p_new)=(p262698,p387503).                          (6.8)
```

It is not an instance of assumption (6.2), because A itself lowers the
lower-priority lexicographic coordinate `h11`.  It is instead the sharp
mechanism by which a root-hard-blocked B becomes the second arc of a
residence-decreasing pair.

### Corollary 6.2 (activated-schema pair)

Let `F in X` and let A be a zero-cost strict arc to `F_1`.  Let B be a
primitive schema absent at `F` because one required deletion incidence `e`
is unselected.  Suppose A installs `e`, preserves every other deletion
incidence required by B, and leaves every B insertion incidence unselected,
so B is alternating at `F_1`.  If B takes `F_1` to `F_2 in X` with negative
cost, then A;B is a strict negative pair even though B has no root arc.

#### Proof

A is a retained zero-cost prefix.  The occupancy hypotheses are exactly the
alternation conditions for B at `F_1`; final membership gives resource
closure.  The telescoping pair cost is `0+c(F_1,F_2)<0`.  \(\square\)

Section 4.5 realizes this condition with `e=11158`, a C6 prefix A, and an
activated star-C8 B.  It is the exact `c_1=0`, `c_1+c_2<0` case of (6.4).

There is one unavoidable logical boundary.  If “every primitive is blocked”
means that the root has no legal physical outgoing arc at all, then no strict
packet exists: every strict packet has a first primitive.  A bypass is
possible only when at least one first primitive is hard-row legal but blocked
by the objective.  Atomic terminal-only cancellation would be a different
semantics and would not prove the strict-prefix claim here.

#### Proof of (6.3)

Dynamic programming on the remaining layers shows that `D_r(v)` is exactly
the cheapest additional cost of stopping at `v` or taking at most `r` more
physical arcs.  Every nonempty root path has a unique first arc, so its
cheapest total cost is the left side of (6.3).  Conditions (6.2) and (6.3)
then give the stated debt-versus-suffix interpretation.  \(\square\)

## 7. One-shot escape versus regenerative renewal

Let `Y` be a family contained in `X`, and let `T` be its declared terminal
set.  First impose **renewal-state completeness**: after a packet commits,
every fact used to generate and accept the next packet is determined by the
materialized endpoint and the explicit state coordinates (5.1).  In
particular, a root-disjoint mask used only inside one batch is cleared before
regeneration.  Any persistent used-root ban, consumed backup, support budget,
or one-use ticket must instead be stored in the endpoint state.  Without this
condition, returning only the factor `F'` does not return to the same
construction class.

### 7.1 Exact bridge/quench motif value

Fix bridge and quench length bounds `b,q` and a bridge-debt ceiling `D`.
For `F in Y`, let `B_b^D(F)` be the endpoints `G` of exact accepted bridge
paths of one to `b` primitives such that

```text
beta(F,G)=S(Psi_min(G))-S(Psi_min(F)) <= D.               (7.1)
```

The bridge may be neutral, worsening, or already improving.  Let `Q_q(G)` be
the endpoints `H in Y` of exact accepted regenerated quench paths of at most
`q` primitives, and put

```text
gamma(G,H)=S(Psi_min(G))-S(Psi_min(H)).                   (7.2)
```

Define the named-motif value, with the minimum of an empty set equal to
`+infinity`, by

```text
kappa_(b,q,D)(F)
  = min_(G in B_b^D(F), H in Q_q(G))
      {beta(F,G)-gamma(G,H)}.                             (7.3)
```

### Proposition 7.1 (exact motif characterization)

Within this declared bridge/quench family, a negative macro exists from `F`
if and only if `kappa_(b,q,D)(F)<0`.  Equivalently, some regenerated quench
credit strictly exceeds its bridge debt:

```text
gamma(G,H)>beta(F,G).                                    (7.4)
```

The two-primitive criterion (6.4) is the case `b=q=1`; a minimal triple has
`b=1,q=2`.  The 2025 escape is the special basin-reset case with a neutral
first bridge.  The later seed13 phases show why neutrality must not be built
into the general definition.  The canonical-root pair of Section 4.5 gives
the exact finite value
`kappa_(1,1,0)(F_*)<=-182372847384` for its declared two-schema family.

#### Proof

Concatenate the two accepted paths.  Its telescoping cost is
`S(H)-S(F)=beta-gamma`; minimizing gives (7.3).  Conversely every declared
macro has one bridge endpoint `G`, so every negative macro supplies a term
of (7.3) satisfying (7.4).  \(\square\)

There is also an exact dual.  Add a bridge/quench phase bit to the lifted
state, allow the phase switch only after a member of `B_b^D(F)`, and connect
only returned states `H in Y` to the sink.  Add the unit reset of (5.5).
The normalized macro circulation is negative exactly when (7.3) is negative;
otherwise the Bellman--Ford potential certifies every macro in this bounded
two-phase family nonnegative.  This dual says nothing about paths excluded by
the bridge/quench phase rules.

For an exact greedy-plateau recurrence, take a plateau set `P`, define bridges
only at `F in P`, and include all subsequent greedy descent in the quench
until it returns to `P`.  Then (7.3) is a plateau-to-plateau basin-reset
criterion.  The reported 2025 two-stage actuator event is endpoint evidence
of this form, but its expanded prefix replay is noncanonical under the current
freeze.  The later phase labels do not by themselves prove that their roots
are plateaux.

### 7.2 When a motif description proves a family theorem

A finite motif label `sigma(F)` is sufficient for a positive recurrence only
if every representative with that label has a certified bridge/quench
construction satisfying the same hard rows, bounds, margin, and allowed
endpoint-label rule.  This one-way uniform construction is enough to prove
existence.

To transfer a no-go or optimal value from a finite signature quotient, much
more is required: `sigma` must be an exact weighted bisimulation.  Hard
acceptance and terminal membership must be constant on fibres, and every
regenerated transition with its cost and endpoint signature must be matched
in both directions by every state in the fibre.  Only then does a quotient
Bellman--Ford potential lift to the materialized graph.  Residence and deep
totals alone are not such a signature; they omit provider loads, literal
slacks, topology, and trace state.

For `delta>=1`, define the exact renewal hypothesis.

> **Regenerative ordered overlap expansion `ROOE(L,delta;Y,T)`.** For every
> `F in Y-T`, regenerate `Gamma_L(F)` from its complete current state.  There
> is an accepting path with at most `L` physical primitives, cost at most
> `-delta`, and terminal factor in `Y`.

### Theorem 7.2 (bounded regenerative descent)

Under renewal-state completeness, `ROOE(L,delta;Y,T)` implies that repeated
regeneration reaches `T` after at most

```text
ceil((S(Psi_min(F_initial))-min_(G in Y)S(Psi_min(G)))/delta) (7.5)
```

packets, each of physical length at most `L`.  Conversely, any assertion that
every nonterminal `F in Y` admits such an `L`-bounded, `delta`-decreasing
renewable step necessarily implies `ROOE` on those states.  Thus `ROOE` is
the exact missing state-uniform expansion statement, not a conclusion of one
finite escape.

#### Proof

The endpoint belongs to `Y`, and renewal-state completeness permits the same
quantified hypothesis to be invoked again.  Every commit decreases the
nonnegative integer scalar by at least `delta`; summing these decreases gives
(7.5).  The converse merely unpacks the promised step at each state and the
definition of the exact builder.  \(\square\)

Strict `Psi_2` descent gives the same termination conclusion by finiteness,
without scalarizing its eight coordinates.  Reaching residence zero requires
`ROOE` at every reachable state of positive residence and requires `T` to be
exactly the zero-residence set.  A family that excludes an inconvenient
reachable endpoint is not endpoint closed and cannot support this induction.

A replayed pair, triple, or longer packet from one factor proves only the one
instance

```text
mu_L(F)<0.                                                (7.6)
```

It proves neither `mu_L(F')<0` at its endpoint nor a uniform length bound.
Section 4.4 gives the exact finite pair instance `F -> B(A(F))`.  Sections
4.2--4.3 give hash-bound actuator and phase-endpoint evidence, while their
expanded lineage replay remains noncanonical.  None of these proves the next
renewal step at residence `1994`: that catalogue must be regenerated at
`F_*` and must yield a new negative accepted path, or an exact dual potential
may prove the declared bounded builder closed there.

The frozen `F_*` now has the exact negative pair of Section 4.5, but this is
one instance, not `ROOE`; it gives no next packet at the residence-1993
terminal.  The strict18 zero-acceptance result closes only
`Gamma_greedy(F_P)`, while the separate continuation evidence and the two
exact local mechanisms show why that filtered closure is not the full renewal
closure.  They do not establish a state-uniform expansion theorem.

## 8. Explicit exclusions

This theorem preserves only the rows listed in Section 2.  Deeper ranks
`11,12,13` are objective coordinates, not frozen monotonicity rows, so an
earlier lexicographic improvement may worsen a later one.  Ranks `14+` may be
added as hard loads or further objective coordinates, but are not silently
asserted here.  Source flags and compiler cells are outside the state and
outside every conclusion.  Nothing here proves a resident factor, a terminal
word, a dimension-uniform packet bound, or completeness of any finite
actuator.
