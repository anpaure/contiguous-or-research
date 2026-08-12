# C7BE common-Q: dominating-socket exchanges and the exact `0017/4027` repair

## 0. Scope and verdict

This note concerns only the authenticated genuine-four-filter target order

```text
scratch/k16_true_fourfilter_two_reroot_uppercomplete_targets_20260731.word
SHA-256 c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906
```

with the pinned monotone schedule

```text
X = {12870,12871,12872},   Y = {0,1,6388},
```

the reserved singleton `0x8000` at physical position `6389`, and the frozen
default marginal perfect matching in
`scratch/k16_c7be_commoncap_default_20260731.matching.tsv`.

The named overlap

```text
0x0017 -> [7648]
0x4027 -> [7648,7649]
```

is **not** an obstruction.  There is an exact one-edge matching exchange

```text
0x4027 : [7648,7649] -> [11105]
```

to a previously unused cell.  The cell at `11105` already carries the
physical letter `0x4027`, so the new assignment imposes no new cap anywhere.
The old cap is released at positions `7648,7649`, changing the two letters

```text
0x0007 -> 0x0017,      0x4025 -> 0x4035.
```

No middle failure, lower failure, or empty position is introduced; the two
lower failures `0x0017` and `0x4035`, both missing bit `0x0010`, disappear.

This is a rigorous local advance, not a full compiler.  The frozen default
matching still has many other common-cap failures.  Marginal Hall expansion
alone does not imply the filtered expansion needed below.

## 1. Abstract common-cap system

Let `P` be a finite set of physical positions.  Every `p in P` has a fixed
nonempty maximal envelope `E_p subseteq [k]`.  A physical cell `c` is a subset
of `P` (in the application, an interval of length at most three).  Let
`S` be the set of lower targets and let `G subseteq S x C` be the marginal
candidate graph.

A complete marginal matching `M` assigns a distinct cell `M(s)` to every
target `s`.  Its common-cap letter at `p` is

```text
Q_M(p) = E_p intersect intersection {s : p in M(s)}.                 (1.1)
```

The fixed middle obligations are intervals `I` with targets `T_I`; the
envelope construction already ensures `E_p subseteq T_I` for `p in I`.
Thus such an obligation is valid exactly when

```text
union_{p in I} Q_M(p) = T_I.                                        (1.2)
```

The lower obligation belonging to `s` is

```text
union_{p in M(s)} Q_M(p) = s.                                       (1.3)
```

We also require `Q_M(p)` nonempty for every physical position.

### Definition 1.1 (dominating incidence)

For a fixed matching `M`, a candidate incidence `(s,c) in G` is
**M-dominating** if

```text
Q_M(p) subseteq s                       for every p in c,             (1.4)
union_{p in c} Q_M(p) = s.                                            (1.5)
```

Condition (1.4) says that installing cap `s` on `c` cannot delete a bit of
any current physical letter.  Condition (1.5) says that the old letters in
`c` already realize every bit of the moved target.

## 2. Exact alternating-path/cycle lemma

### Theorem 2.1 (dominating alternating exchange)

Let `M` be a complete marginal matching.  Let

```text
s_0, c_1, s_1, c_2, ..., s_{ell-1}, c_ell                         (2.1)
```

be a simple alternating path such that

1. `c_i=M(s_i)` for `1<=i<ell`;
2. `c_ell` is unmatched;
3. every `(s_{i-1},c_i)` is `M`-dominating.

Define `M'` by

```text
M'(s_{i-1})=c_i  (1<=i<=ell),                                      (2.2)
```

leaving every other assignment unchanged.  Then

```text
Q_M(p) subseteq Q_{M'}(p)             for every p.                  (2.3)
```

Every moved target satisfies its lower obligation under `M'`.  Hence every
fixed middle obligation, every unmoved lower obligation, and every nonempty
position which was valid under `M` remains valid under `M'`.

The same conclusion holds for a simple alternating cycle if all its new
target-cell incidences are `M`-dominating.

#### Proof

Fix a position `p`.  Write `U_p` for `E_p` intersected with the targets of
all unchanged assignments covering `p`.  The old letter is `U_p` intersected
with some of the removed path targets.  The new letter is `U_p` intersected
with some of the added path targets.  By (1.4), the old letter `Q_M(p)` is
contained in every added target whose new cell covers `p`.  It is also
contained in `U_p`.  Therefore it is contained in their intersection,
which is `Q_{M'}(p)`.  This proves (2.3), including when several path cells
overlap.

For a moved target `s_{i-1}`, (1.5) and (2.3) give

```text
s_{i-1}=union_{p in c_i}Q_M(p)
         subseteq union_{p in c_i}Q_{M'}(p).
```

The reverse containment holds because the newly installed assignment caps
every letter in `c_i` by `s_{i-1}`.  Thus equality holds.  An unmoved lower
cell is still capped by its own target, while (2.3) prevents loss of any old
provider.  Fixed middle rows remain subsets of their targets by the envelope
law and lose no provider by (2.3).  A nonempty old letter stays nonempty.
The cycle proof is identical.  QED.

### Corollary 2.2 (strict descent)

Let `Phi(M)` count all missing fixed-row bit obligations, all missing lower
target bit obligations, and all empty physical positions.  An exchange from
Theorem 2.1 never increases `Phi`.  It strictly decreases `Phi` if either

* a moved target was invalid before the exchange; or
* deleting the old cell of `s_0` exposes a missing fixed/unmoved-target bit
  at a position at which none of the newly installed caps deletes that bit.

This follows directly from (2.3), the validity of every moved target, and
the stated strict exposure.

## 3. A checkable expansion hypothesis and termination

For a current matching `M`, form a directed alternating graph `D_M`:

* direct `s -> c` for every `M`-dominating incidence;
* direct an occupied cell `c -> t` when `M(t)=c`.

For a specified missing obligation bit and an exposing root `s_0`, delete
from `D_M` any arc whose newly installed cap would delete the chosen exposed
bit at its witness position.  Let `R` be the targets reachable from `s_0`
and `N_D(R)` their outgoing cells.

### Proposition 3.1 (dominating-socket expansion)

If

```text
|N_D(R)| > |R|,                                                     (3.1)
```

then a free cell is reachable from `s_0`; the corresponding alternating path
is a strict `Phi`-decreasing exchange of Theorem 2.1.

#### Proof

If every cell of `N_D(R)` were occupied, its owner would also be reachable
and hence lie in `R`.  Distinct occupied cells have distinct owners, so this
would give `|N_D(R)|<=|R|`, contradicting (3.1).  The path to a free cell is
bit-preserving by construction, and Corollary 2.2 makes the descent strict.
QED.

Consequently, if at every nonzero-defect state there is an exposing root for
which (3.1) holds (or a strict dominating alternating cycle), repeated exact
exchanges terminate after at most `Phi(M_0)` steps at a zero-defect common-cap
matching.  This is a deterministic finite theorem; the expansion hypothesis
is state-dependent and must be checked in the **dominating** graph, not in the
marginal Hall graph.

## 4. Exact c7be local certificate

In the frozen default matching,

```text
M(0x0017) = cell16558 = [7648],
M(0x4027) = cell16559 = [7648,7649].
```

The old common-cap letters and cap sources are

```text
p=7648: E_p=0x0037, Q_M(p)=0x0007;
p=7649: E_p=0x4035, Q_M(p)=0x4025.
```

Thus `0x4027`, which omits bit `0x0010`, simultaneously removes the last
`0x0010` provider from lower cells `0x0017` and `0x4035`.

Among the 34 marginal candidate cells for `0x4027`, exactly two are
`M`-dominating:

```text
cell16559 = [7648,7649], current letters (0x0007,0x4025), occupied by 0x4027;
cell26929 = [11105],     current letter  0x4027,        free.
```

Hence the rooted dominating neighborhood already has strict surplus
`2>1`, and the length-one path to `cell26929` is available.  After moving
`0x4027`, the complete exact replay changes only

```text
Q(7648): 0x0007 -> 0x0017,
Q(7649): 0x4025 -> 0x4035.
```

The new socket letter at `11105` remains `0x4027`.  The middle-failure list
is byte-for-byte unchanged, the empty-position list remains empty, the lower
failure count drops from `5037` to `5035`, and the exact removed lower
failures are `{0x0017,0x4035}`.  No lower failure is introduced.

For comparison, `0x0017` itself has one free dominating socket,
`cell22444=[9610]`, whose current letter is exactly `0x0017`; moving the
blocker `0x4027` is stronger because it repairs both named casualties at
once.

## 5. What marginal Hall does not prove

The frozen marginal certificates prove a perfect matching in the candidate
graph.  They do not record the current letters `Q_M(p)` and therefore cannot
imply (1.4), (1.5), or (3.1).

This logical gap is real even in the smallest abstract example.  Take two
disjoint target labels `{a}` and `{b}`, two distinct cells

```text
c_1={p},    c_2={p,q},    E_p=E_q={a,b},
```

and let the marginal graph be `K_{2,2}`.  Every marginal Hall inequality is
tight and both perfect matchings exist.  But every perfect matching caps the
shared position `p` by `{a} intersect {b}=empty`; the target assigned to
`c_1` is not realized.  Thus marginal Hall alone cannot certify any common-
cap matching or dominating exchange.

The precise remaining constructive condition for c7be is therefore:

> prove the state-dependent dominating-socket expansion (3.1), or exhibit
> strict dominating cycles, for every residual common-Q defect after exact
> exchanges.

The named `0017/4027` overlap passes this condition exactly.  The present
audit does not claim it for the full 26,332-target system.

## 6. Reproducible audit

```text
scratch/audit_r_k16_c7be_dominating_socket_exchange_20260731.py
  SHA-256 e74db6f2ea9d589b563d15811c596fadb6b5299dc6c704f23cb44294669cb056

scratch/k16_c7be_dominating_socket_exchange_20260731.audit.json
  SHA-256 5ecffbd3e9df092467cb9bc255b45452555f2538bbe81fd4f96452dc392c3d4e
  payload  12b3e0d4a288a83ff9fe695de31ee8f9a18dba897327c9cdcf36af178cab4aa7

scratch/audit_r_k16_c7be_dominating_socket_exchange_independent_20260731.py
  SHA-256 32d58e0baa801c1c37d22f62f181f4f27a6e3141eeea38eecca560dff21455a7

scratch/k16_c7be_dominating_socket_exchange_independent_20260731.audit.json
  SHA-256 27aff3ada0c02f3492c2f21f53444b86f59bb180a0cc0e3bc7b4264c54de52a6
  payload  7ba7105e162749148d7d7ad1ef4a9554a17fddb0363b6bcc72153032de3efcc8

scratch/k16_c7be_commoncap_default_20260731.matching.tsv
  SHA-256 666cfdded7462574e7e035a8169a7a9c9efde33d979ce8b03382585fcabfca74
```

The audit authenticates the c7be target, reconstructs the exact pinned
candidate graph, enumerates candidate cells only for `0x0017` and `0x4027`,
checks the dominating conditions, performs the one-edge exchange, and
replays all middle and assigned-lower intervals literally.

The second audit imports no project checker.  It independently rebuilds the
schedule, maximal envelopes, common caps, middle replay, and every matched
lower replay directly from the target word and matching TSV; it obtains the
same two changed letters and the same exact defect delta.
