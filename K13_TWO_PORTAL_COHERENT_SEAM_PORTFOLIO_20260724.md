# Exact coherent two-portal seam: the next `k=13`, length-1,851 lane

Date: 2026-07-24

## Outcome

This note defines and audits a candidate-first family that is genuinely
outside both completed search geometries:

* it is not a fixed two- or three-entry edit of either 1,851-entry one-hole
  seed; and
* it is not a one-interface lift, for any relative bit permutation.

The unchanged 926-entry `k=12` word is physically bracketed by **two** high-bit
singleton portals.  The retained lifted alphabet is split across the two
sides.  The right side may additionally use a fixed relative dihedral bit map
before the common unknown 12-bit permutation.  For each fixed structural
state, all `12!` common permutations are represented by only 144 Boolean map
variables.

A warning-free RunPod compilation and an independent exhaustive
reduced-instance audit were completed.  After this lane was prepared, the
entire center/identity first tier was run and then rerun in certification
mode.  All thirty shards are DRAT-verified UNSAT, formally excluding
883,278,950,400 assignments.  The nonidentity relative maps and the endpoint
lane remain unsearched.  The certificate audit is in
`K13_TWO_PORTAL_IDENTITY_CENTER_CERTIFICATE_AUDIT_20260724.md`.

## 1. Candidate architecture

Let

```text
B = (B_0,...,B_925)
```

be `k12_optimal_nonzero.txt`, let `O` be `B` or its reversal, and choose

```text
0 <= d0 < d1 < d2 < 926,
0 <= cut <= 926.
```

Delete `O[d0],O[d1],O[d2]`.  The retained entries before `cut` form `L`; the
retained entries from `cut` onward form `R`.  Both pieces are required to be
nonempty.

Let `tau` be a fixed relative permutation of the old bit coordinates and let
`pi` be an arbitrary common permutation.  The candidate is

\[
 (2^{12}\vee\pi(L))\ \Vert\ (2^{12})\ \Vert\ B\ \Vert\
 (2^{12})\ \Vert\ (2^{12}\vee\pi(\tau(R))).                 \tag{1.1}
\]

It has exactly

\[
 923+2+926=1851
\]

entries.  Every target omitting the new bit is still covered inside the
unchanged contiguous copy of `B`.  Both copies of the high singleton are real
entries, not formal separators.

The implemented relative maps are the 24 dihedral maps

\[
 \tau_{\epsilon,a}(i)=\epsilon i+a\pmod {12},
 \qquad \epsilon\in\{-1,+1\},\quad 0\le a<12.             \tag{1.2}
\]

The identity-only tier is the subfamily `epsilon=1,a=0`.

## 2. Exact residue decomposition

For a word `X`, write

* `Int(X)` for all ORs of nonempty intervals of `X`;
* `Pre(X)` for its distinct prefix-OR chain, including zero; and
* `Suf(X)` for its distinct suffix-OR chain, including zero.

Put

\[
 I=\{0,4095\}\cup\operatorname{Int}(L)
                 \cup\operatorname{Int}(\tau(R)).         \tag{2.1}
\]

The `0` is supplied by either high singleton.  The value `4095` is supplied by
every high-containing interval that crosses both portals, because such an
interval contains all of `B`.

Every upper residue in (1.1) is in exactly the following union:

\[
\begin{aligned}
 \pi(I)
 &\cup\{\pi(s)\vee p:s\in\operatorname{Suf}(L),
                         p\in\operatorname{Pre}(B)\}\\
 &\cup\{p\vee\pi(t):p\in\operatorname{Suf}(B),
                         t\in\operatorname{Pre}(\tau(R))\}.
                                                               \tag{2.2}
\end{aligned}
\]

This is an equality, not a relaxation:

* intervals wholly in one high piece give `pi(Int(piece))`;
* intervals crossing the left portal and ending in the lower word give the
  first crossing family;
* intervals starting in the lower word and crossing the right portal give the
  second crossing family; and
* intervals crossing both portals contain the whole lower word and give only
  residue `4095`.

Thus the only targets requiring clauses are the fixed holes

\[
 H=[0,4095]\setminus I.                                     \tag{2.3}
\]

## 3. Maximal-chain compression

Fix `h in H`.  A left provider `(s,p)` repairs the target `pi(h)` precisely
when

\[
 s\subseteq h,qquad
 \pi(h\setminus s)\subseteq p\subseteq\pi(h).              \tag{3.1}
\]

The identical criterion holds on the right, with
`s in Pre(tau(R))` and `p in Suf(B)`.

The transformed source chains are inclusion chains.  If (3.1) holds for one
`s`, it also holds for the largest chain member `s_h` contained in `h`:
adding elements of `h` to `s` cannot contaminate the target and can only
reduce `h minus s`.  Hence each hole needs only

* one maximal left source crossed with the (nine, for the supplied base) lower
  prefix values; and
* one maximal right source crossed with the nine lower suffix values.

For a fixed provider, (3.1) has a compact exact permutation encoding:

* every source bit in `h minus s_h` maps into `p`; and
* every target bit in `p` has its preimage in `h`.

Under the permutation-matrix constraints these implications are equivalent to
(3.1).  A provider selector gates them.  Each structural-state selector gates
the disjunction of providers for each of its holes, and exactly one structural
state is selected.

Therefore the generated CNF is exact:

```text
CNF SAT
iff one listed structural state and one of all 12! common maps pi
    yield a universal 1,851-entry word of the form (1.1).
```

## 4. First immutable portfolio tiers

`scratch/build_k13_two_portal_manifests.py` supplies two structural lanes.

### Center lane

For each `2 <= cut <= 923`, delete

```text
cut-1, cut, cut+1
```

and split at `cut`.  There are 922 structural states.

### Endpoint lane

For each `2 <= cut <= 923`, delete

```text
0, cut, 925
```

and split at `cut`.  This spends the same two endpoint deletions as the proved
one-interface ceiling, but the third deletion and two physical portals give a
different interval geometry.  There are another 922 structural states.

The exact parameter-assignment ledgers are:

| tier | orientations | structural/relative states | assignments including `pi` |
|---|---:|---:|---:|
| center, identity `tau` | 2 | `2*922` | `883,278,950,400` |
| center, all dihedral `tau` | 2 | `2*922*24` | `21,198,694,809,600` |
| both lanes, all dihedral `tau` | 2 | `2*1844*24` | `42,397,389,619,200` |

The table counts exact parameter assignments.  It does not assert that no two
assignments ever emit the same physical word; that injectivity is unnecessary
for search completeness.

The portfolio order is:

1. center/identity, both orientations (**completed and DRAT-certified
   UNSAT**);
2. center/dihedral, omitting the already searched identity rows (the `+2`
   rotation is also now completed and DRAT-certified UNSAT);
3. endpoint/dihedral.

The identity center tier has only fifteen 64-state shards per orientation.

## 5. Independent audit

`scratch/audit_k13_two_portal_reduction.py` does not import or invoke the C++
generator.  On deterministic four- and five-bit instances it exhausts every
bit permutation and compares:

1. direct interval-OR coverage of the physical two-portal word;
2. the complete uncompressed crossing formula; and
3. the maximal-chain reduction used by the CNF.

Run remotely, it reports

```text
PASS cases=372 assignments=26208 set_comparisons=52416
```

The C++ generator also compiled warning-free under
`-Wall -Wextra -Wpedantic` (the RunPod compiler supports `-std=c++17`; a newer
compiler may use `-std=c++20`).

As a production sizing check, the first 64 forward center/identity states gave

```text
states=64
holes=986
maximum_holes=20
providers=2576
impossible_holes=156
variables=3111
clauses=27828
CNF bytes=722204
```

The subsequent complete center/identity pass produced fifteen DRAT-verified
UNSAT blocks per orientation.  An independent replay regenerated every
formula byte-for-byte and freshly rechecked all thirty proofs.  The compact
ledger hash is

```text
56f8a913fe4b086599af9f68bacfc3e789fad5057e2b62ad676efd9238f7cb0f
```

The next fixed relative map `tau(i)=i+2 mod 12` was likewise completed and
independently replayed.  Its thirty compressed certificates exclude another
883,278,950,400 assignments.  Its compact ledger hash is

```text
9c5e006a54a94b02dfe78fb6ab0c811cdb912731f9a07f481e1fba49213850d5
```

## 6. RunPod-safe preparation and search

The commands below describe the now-completed first tier and remain the launch
template for later tiers.

Compile on RunPod:

```bash
g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  k13_two_portal_exact_cnf.cpp -o k13_two_portal_exact_cnf
```

Build the first manifests:

```bash
python3 build_k13_two_portal_manifests.py \
  /root/k13_two_portal/manifests/center_identity \
  --lanes center --tau identity --shard-size 64 \
  --prefix center_identity
```

Set explicit tool paths:

```bash
export K13_TWOPORTAL_GENERATOR=/root/k13_two_portal/k13_two_portal_exact_cnf
export K13_TWOPORTAL_DECODER=/root/k13_two_portal/decode_verify_k13_two_portal.py
export K13_TWOPORTAL_RUNNER=/root/k13_two_portal/run_k13_two_portal_block.sh
export K13_TWOPORTAL_WORK=/root/k13_two_portal/results
export VERIFY_OR_ARRAY=/root/verify_or_array
```

Then use one sequential portfolio per assigned RunPod CPU:

```bash
./run_k13_two_portal_portfolio.sh \
  center_id_forward 39 /root/k13_two_portal/k12_optimal_nonzero.txt \
  /root/k13_two_portal/manifests/center_identity 0 search 230100 300

./run_k13_two_portal_portfolio.sh \
  center_id_reverse 30 /root/k13_two_portal/k12_optimal_nonzero.txt \
  /root/k13_two_portal/manifests/center_identity 1 search 240100 300
```

The block runner:

* refuses pre-existing tag artifacts;
* hashes the base, immutable state shard, CNF, map, and statistics before the
  solve;
* rejects CNFs above 256 MiB or ten million clauses unless the explicit
  environment caps are changed;
* limits Kissat to 4 GiB virtual memory when `prlimit` is available;
* deletes large search-mode UNSAT temporaries after hashing;
* reconstructs every SAT word independently in Python; and
* accepts SAT only after the separate `verify_or_array` binary reports all
  8,191 nonzero targets.

Certification mode retains a DRAT proof and requires an explicit
`s VERIFIED` from `drat-trim` before marking an UNSAT block certified.

## 7. Files and hashes

```text
scratch/k13_two_portal_exact_cnf.cpp
  8a7675bba778e4c24e11501829b238caedf09eb4554819e2e0b627797949e179
scratch/decode_verify_k13_two_portal.py
  1b5f1d1e9f5239fb549ce1a4ab8847f594ed8d0e5532c3e0a91472566eae6263
scratch/audit_k13_two_portal_reduction.py
  53ad98ea576d3d5bf564bd3950b8546de050e39e8ea29aa43754162b09bdb917
scratch/build_k13_two_portal_manifests.py
  a97b216b598ca6b4e28899704b196c30d676846e1bd375f16b1f03be1a66e1e5
scratch/run_k13_two_portal_block.sh
  baf1b29fa937f87262f5afa3274121c8ff7f0a418165a56baf9299f2802b1d7c
scratch/run_k13_two_portal_portfolio.sh
  5821a2b63225869461780b6b592300753c6e89b0f1031ccafbea4dd2e98acbe8
scratch/audit_k13_two_portal_identity_certificates.py
  e32642e5a2a4fc980444e0d8f7e604f7b09fcb7088335287518277979c27cafc
scratch/k13_two_portal_identity_center_certificate_ledger.json
  56f8a913fe4b086599af9f68bacfc3e789fad5057e2b62ad676efd9238f7cb0f
scratch/audit_k13_two_portal_fixed_tau_certificates.py
  387e3697bf489738f2690e8bc33797cb54c6cb25952de33025a4102dba722e54
scratch/k13_two_portal_tau_p2_certificate_ledger.json
  9c5e006a54a94b02dfe78fb6ab0c811cdb912731f9a07f481e1fba49213850d5
```

## Scope

This is a new exact candidate family, not a bound improvement.  The identity
and `+2` relative maps, totaling 1,766,557,900,800 assignments, are now
formally excluded; a SAT word in a later tier would prove `nu(13) <= 1851`.
The current certified finite-`k` table is unchanged.
