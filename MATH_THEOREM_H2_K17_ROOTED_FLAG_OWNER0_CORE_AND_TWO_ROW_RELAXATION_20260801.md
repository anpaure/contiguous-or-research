# K17 rooted flags: owner-0 core and the exact two-row repair primitive

Date: 2026-08-01  
Lane: H2 independent theorem/audit  
Status: **fixed-certificate UNSAT independently GO; minimal uniform local
factor-preserving repair arity is two; simultaneous global packing remains
open**

## 1. Exact scope and verdict

The frozen input is the rank-eight-rooted flag certificate

```text
scratch/h2_k17_rooted_flag_attachment_cycle_v2_20260801/
  k17_rank8_rooted_static_age_flag_20260801.certificate.tsv
SHA-256 ad9e15f724b5048c00cf43ae007d0e02c03c72204a5c169736461e946a166eab
```

and the compressed loop-free attachment model generated from it.  It has

```text
rank-8 rooted rows             1,430
rank-9 owner orbits            1,430
attachment states             12,870
literal transitions            7,296
variables / clauses      50,064 / 130,067
```

The DRAT verdict and its ten-input-clause core are sound.  The core is the
owner-orbit-0 exact-one clause together with nine zero-indegree units.  This
is an owner-0 **zero-in** obstruction and is distinct from the previously
published rooted-row-0 zero-out obstruction.

Opening all nine attachments therefore does not rescue this fixed flag
certificate.  Conversely, the obstruction is not invariant under flag
repartitioning.  One same-ticket row rephase already repairs owner 0, and an
exact O3 catalogue proves that every one of the 782 incoming-dead owners has
an individual factor-preserving two-row componentwise-ticket exchange that
creates a literal incoming transition.

The word “individual” is essential: no simultaneous consistent selection of
these exchanges is asserted here.

## 2. Transition recurrence from first principles

Let a rooted row be

\[
 Q=C_0\mathbin{\dot\cup}C_1\mathbin{\dot\cup}C_2,
\]

and attach it to a rank-nine owner by a shifted incidence
`e=(q,o,sigma)`.  Its fourth class is the singleton omitted from the owner to
obtain the aligned root.  If an old-root incidence
`h=(q,o',tau)` carries the next owner, then the common physical gauge is

\[
 \delta=\sigma-\tau\pmod {17}.                       \tag{2.1}
\]

Writing `tilde C_j=rho^delta C_j(next)`, the literal depth-three update is
equivalent to

\[
 \beta\in\widetilde C_0,
 \qquad \widetilde C_1\subseteq C_0,
 \qquad \widetilde C_2\subseteq C_1,
 \qquad \widetilde C_3\subseteq C_2.                \tag{2.2}
\]

The age-zero class is then forced by the two owner partitions:

\[
 \widetilde C_0=\{\beta\}\mathbin{\dot\cup}
 (C_0-\widetilde C_1)\mathbin{\dot\cup}
 (C_1-\widetilde C_2)\mathbin{\dot\cup}
 (C_2-\widetilde C_3).                              \tag{2.3}
\]

Thus the builder's entering-membership test and its three subset tests are
necessary and sufficient; it does not omit an independent refresh equation.
The independent auditor reconstructs all incidences and rotations from the
certificate, validates all 7,296 stored transitions against (2.1)--(2.3),
and rechecks the exact type and suffix ledgers.

## 3. The ten-clause core

Variables `1,...,9` are exactly the nine states attached to owner orbit

\[
 T=0x001ff=\{0,1,\ldots,8\}.
\]

Their incoming degrees are all zero; their outgoing degrees are

```text
0,0,1,0,0,1,1,0,0.
```

The model therefore contains

\[
 (z_1\vee\cdots\vee z_9),\qquad
 \neg z_1,\ldots,\neg z_9.                           \tag{3.1}
\]

These are all input clauses.  Unit propagation on the nine negative units
falsifies the first clause, so (3.1) is already a complete human UNSAT proof.
The full proof SHA is

```text
464388a349601c13bc40b791fe45f6c3fcd560ba6f755034c3f5926b6ef723c1
```

and the extracted core SHA is

```text
c09b148177964a85c6f7ebf3a4480aa3b859cf5837956bdc4a6da887d2ea7455.
```

The stored `drat_verify.out` reports `s VERIFIED` and identifies ten of the
130,067 input clauses.  The file named `core_verify.out` actually records a
second parse of the full model, not a direct parse of `core.cnf`; that is a
provenance-label defect, not a mathematical defect.  The independent audit
checks `core.cnf` directly, confirms that every clause occurs in the full
model, and verifies its unit-propagation contradiction.

## 4. Solver-free owner-0 obstruction

Index the nine facets of `T` by their deleted bits.  For `b in T`, write

\[
 Q_b=T-\{b\},\qquad C_3^b=\{b\},
\]

with all classes aligned into the common `T` gauge.  An incoming transition
whose old H-root is `Q_x` and whose next D-root is `Q_b` is legal exactly when

\[
 b\in C_2^x,qquad C_2^b\subseteq C_1^x,qquad
 C_1^b\subseteq C_0^x.                              \tag{4.1}
\]

These conditions also force `x in C_0^b` and (2.3).  The first test in
(4.1) reduces all 72 ordered distinct-facet pairs to eleven.  Their remaining
defects are:

| `x -> b` | `C2(b) - C1(x)` | `C1(b) - C0(x)` |
|---|---|---|
| `0 -> 6` | `{4}` | `{7}` |
| `1 -> 0` | `{6}` | empty |
| `1 -> 3` | `{1}` | `{0,5}` |
| `2 -> 6` | `{4}` | `{1,7}` |
| `3 -> 1` | `{3}` | `{5}` |
| `4 -> 2` | `{6}` | `{1}` |
| `4 -> 3` | empty | `{2,4}` |
| `5 -> 1` | `{0,3}` | `{5}` |
| `6 -> 4` | `{2,3}` | `{1}` |
| `7 -> 4` | `{3}` | `{1}` |
| `8 -> 5` | `{1}` | `{6}` |

Every row has a nonempty defect, so no facet pair is legal.  The fourth-class
attachment cannot alter (4.1), proving simultaneously that all nine owner-0
states have indegree zero.  Allowing the omitted disconnected self-loop face
does not help: the parallel root-0 pair is included in this common-owner
test and also fails.

## 5. How large a certificate change is necessary?

The fixed catalogue has

```text
incoming-dead owner orbits       782
outgoing-dead owner orbits        12
incoming-dead rooted rows        848
outgoing-dead rooted rows        761
```

Any new incoming transition at a formerly dead owner uses two rank-eight
rows incident with that owner.  Hence changing a nonincident row cannot help.
The number of incoming-dead owners incident with each rooted row has exact
histogram

```text
degree:count = 0:1, 1:12, 2:63, 3:165, 4:304,
               5:386, 6:305, 7:135, 8:53, 9:6.
```

The 102 largest degrees sum to only

\[
 6\cdot9+53\cdot8+43\cdot7=779<782.                \tag{5.1}
\]

Therefore every literal repartition repair of all dead owners changes at
least **103 rooted rows**, even if each changed row is granted arbitrary
repair power on every incident owner.  This is a solver-free necessary bound;
it does not claim that 103 rows suffice.  A greedy incidence cover uses 173
rows, but it is only a touch-cover and does not supply replacement flags.
The optional bound-150 and bound-160 cover solves both timed out and are
recorded as `UNKNOWN`, not UNSAT.

## 6. Minimal factor-preserving local primitive

For a row define its static ticket

\[
 \theta(Q)=(\operatorname{type},[C_0],[C_0\cup C_1]). \tag{6.1}
\]

Keeping `theta(Q)` fixed preserves that row's contribution to the type
ledger and both exact suffix palettes.

### 6.1 Owner 0 needs only one row

Root row 1 in the frozen certificate is

```text
root=383, type=1, (C0,C1,C2)=(8,359,16), ticket=(1,1,367).
```

The replacement

```text
(C0,C1,C2)=(2,365,16)
```

has the same root, type and ticket, and creates a literal incoming transition
at owner 0.  Thus the ten-clause core is not stable under even one
factor-preserving row rephase.

### 6.2 One row is not a uniform solution

The exact same-ticket catalogue contains

```text
raw rows including identity             3,987
nonidentity rows                         2,557
roots with a nonidentity rephase           488
useful alternatives                        694
fixed dead owners singly repairable         500 / 782
maximum owners repaired by one row             3.
```

Exactly 282 dead owners have no one-row same-ticket repair.  Allowing two
same-ticket rephases jointly repairs only three more, leaving 279.
Consequently no uniform arity-one factor-preserving local repair theorem is
possible for this certificate.

### 6.3 Two componentwise-ticket rows suffice locally

For two rows, independently keep or swap each of the three coordinates in
(6.1).  Every such componentwise exchange preserves the two-row multiset in
all three global ledgers, hence preserves the complete static rooted factor.
The exact H100 O3 catalogue enumerates all 2,722,720 raw rooted flags and
finds

```text
exchange row pairs                       26,867
feasible component-swap patterns         26,961
literal realization pairs               213,670
dead owners with an individual witness  782 / 782.
```

An independent decoder replays one stored witness for each dead owner,
checks both row partitions, checks the three two-row ticket multisets, and
checks the literal incoming recurrence.  All 782 pass.

It follows that the minimal **uniform local** factor-preserving repair arity
is exactly two: some owners admit no one-row rephase, while every owner admits
a two-row componentwise-ticket exchange.

This is not yet a repaired certificate.  Exchange witnesses for different
owners can share rows or assign incompatible alternatives to the same row;
additional changed incident rows can also destroy a witness.  The precise
surviving gate is a simultaneous exchange-packing/CSP with at least 103
changed rows, followed by full transition-cycle, voltage and upper checks.

## 7. H100 provenance and frozen artifacts

The catalogues ran on one H100 CPU core (`taskset -c 47`, `nice 19`) with O3
native binaries and explicit memory/time caps.  They completed normally;
the only capped jobs were the optional incidence-cover bounds just labelled
`UNKNOWN`.

Primary fixed-model files:

```text
model.cnf
  SHA 30e7387bd92de6c6175abf6f4ea48e4283f1115cd5cb804670a4c1f50a7fb52e
model.map.tsv
  SHA f000c8055a4ecce7e37c7870d9a953bca3b804d197f06e445f13e20ef5b2b95d
model.transitions.tsv
  SHA 375d015b66201e1b94cb383e2f924387aa172b1c02fc3e657b492b52eaa228cc
```

Independent core/row-bound audits:

```text
scratch/audit_h2_k17_rooted_flag_attachment_core_20260801.py
  SHA 7009bec523df694827175855b6686928ff00219fe1fd7df416933e82d92b3887
scratch/h2_k17_rooted_flag_attachment_core_20260801.audit.json
  SHA e5c7ad3fdcf33da0e86c87c73cb7fa322651e231a3071b4a87a759ec5025be9d
  payload ac4c15e3aa6f231d045cd95e7322bc6749bc222c06d7ef7ce97119cdaaec2067
scratch/audit_h2_k17_rooted_flag_owner_support_relaxation_20260801.cpp
  SHA a38ffc8b61a1d63f0b690f0ef087295eba1d571fd4dbf804c9b07e57393201f5
scratch/h2_k17_rooted_flag_owner_support_relaxation_20260801.audit.json
  SHA 906abbf580c260ae89f4c3ec7a02f51df62f0cc689a5cd52961402151aaa03a7
```

Exact repair catalogues:

```text
scratch/catalogue_h2_k17_rooted_flag_same_ticket_rephase_20260801.cpp
  SHA 428aa7e119754dcc32ee1eb23e018dcd7a19788b03556d3d30e0e9cafc5c1eff
scratch/h2_k17_rooted_flag_attachment_cycle_v2_20260801/same_ticket_v2.audit.json
  SHA 2bbadc4fa01d3c06952463f9941ea8c2a41cefe30e4b81c5cc1420effba0ba45
scratch/catalogue_h2_k17_rooted_flag_two_row_ticket_exchange_20260801.cpp
  SHA f3a4d23616ebf982117218f6bad37fc1b4ef9f863c38024ca7fee8e8d637a5cb
scratch/h2_k17_rooted_flag_attachment_cycle_v2_20260801/general_two_row_exchange.audit.json
  SHA 7c0459cd0be08d8feb9434b089ac62be73432d31f46edc692412e46026ddcadd
scratch/h2_k17_rooted_flag_attachment_cycle_v2_20260801/general_two_row_exchange.tsv
  SHA 197744b267f0cbbfc92ce2c42d48d4c9525aba7a52a789928784c9063ccd317f
```

Independent positive-witness replay:

```text
scratch/audit_h2_k17_rooted_flag_exchange_witnesses_20260801.py
  SHA 138295ac71d68548597f37c3870ca457d51a3709a98ea7233a3052253552244b
scratch/h2_k17_rooted_flag_exchange_witnesses_20260801.audit.json
  SHA a339f2e7c78c4c13e2cadbee526a1e27e2497379661ef230b86a3feffb06ef26
  payload 8187a21a2cf78e981d2011e55dbe746cc7fb721a00e2e91f43254099b978440e
  status PASS_INDEPENDENT_LITERAL_REPLAY_OF_ALL_782_TWO_ROW_EXCHANGE_WITNESSES
```

Remote run directory:

```text
/home/amodo/or15/work/h2_k17_rooted_flag_owner_cover_20260801
```

## 8. Scope boundary

The negative theorem is only for certificate SHA `ad9e15f7...` and its exact
loop-free literal transition model.  The positive theorem is only a catalogue
of per-owner one/two-row static-factor-preserving local repairs.  Neither
proves a simultaneous rooted certificate, a cycle cover, Hamiltonicity,
nonzero voltage, upper shadows, a safe opening, source/common-cap/compiler
compatibility, or any unrestricted K17 impossibility or construction.
