# Genuine-four-filter endpoint reroot: all upper shadows and pinned marginal Hall

Date: 2026-07-31  
Lane: R  
Status: exact for the displayed parent, target order, and P/Q schedule. The simultaneous common-cap compiler and literal K16 word remain unproved.

## 1. Authenticated source

The sole parent is

```text
scratch/K15_FOURFILTER_SEED_20260731.word
SHA-256 51f57125ea3e145e08ed9d5f8816d22313a010907588457260c824c6f40217f4
opening (5134,0,5,1,0), direction fwd
```

This is the genuine four-filter K15 parent. No seed0-derived file whose
historical name contains `fourfilter_insert_aug` enters the construction.

For its physical letters \(w_0,\ldots,w_{6437}\), put

\[
D^2_i=w_i\vee w_{i+1}\vee w_{i+2},\qquad
D^3_i=w_i\vee w_{i+1}\vee w_{i+2}\vee w_{i+3},
\]

and let \(z=\mathtt{0x8000}\). The \(D^3_i\) are the \(6{,}435\) distinct
old rank-eight masks. The \(D^2_i\) consist of the \(6{,}435\) distinct old
rank-seven masks and the unique rank-six value \(D^2_{6390}=\mathtt{0x13c8}\).
Consequently the natural K16 middle order is

\[
T=operatorname{rev}(z\vee D^2_{[0,6390)})
  \mathbin\Vert D^3_{[0,6435)}
  \mathbin\Vert\operatorname{rev}(z\vee D^2_{(6390,6436)}).
\tag{1.1}
\]

Its three piece lengths are \(6{,}390,6{,}435,45\). Its canonical
newline-terminated serialization has SHA-256

```text
0f6d64e9311ef634169964350baa8f817b17b9d1619970c881f87e7346550a5c.
```

The natural order contains every K16 rank-eight mask once. Its complete
upper deficit is

\[
\{\mathtt{b3cc},\mathtt{d3cc},\mathtt{d3ce},
  \mathtt{f3cc},\mathtt{dbce},\mathtt{fbce}\}.
\tag{1.2}
\]

The first two masks are its q1 holes. Its all-schedule three-hole scalar
maximum is only \(25{,}744+9=25{,}753<26{,}332\); thus the natural order
itself is compiler-dead. This is the fixed-order theorem recorded separately
in handoff item 2091.

## 2. Two exact endpoint reroots

Number target positions from zero and define

\[
T^*=operatorname{rev}(T[0..6388])
   \mathbin\Vert T[6389..12825]
   \mathbin\Vert\operatorname{rev}(T[12826..12869]).
\tag{2.1}
\]

The frozen order is

```text
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
SHA-256 c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906.
```

### Theorem 2.1

The order \(T^*\):

1. contains every one of the \(\binom{16}{8}=12{,}870\) middle masks exactly once;
2. has no q1 hole; and
3. contains every upper mask of every rank \(9,\ldots,16\) as a literal contiguous interval OR.

### Proof

The two reversals only permute middle masks. At the prefix cut, the removed
boundary union \(\mathtt{c3ce}\) has old multiplicity two and the inserted
boundary union is the missing colour \(\mathtt{d3cc}\). At the suffix cut,
the removed union \(\mathtt{f38c}\) has old multiplicity two and the inserted
union is the missing colour \(\mathtt{b3cc}\). Hence the complete q1 palette
is retained and the two q1 holes are filled.

For arbitrary widths, an exact OR-event replay gives

\[
\operatorname{Cov}(T)\subseteq\operatorname{Cov}(T^*)
\]

and

\[
\operatorname{Cov}(T^*)\setminus\operatorname{Cov}(T)
=\{\mathtt{b3cc},\mathtt{d3cc},\mathtt{d3ce},
    \mathtt{f3cc},\mathtt{dbce},\mathtt{fbce}\}.
\tag{2.2}
\]

The replay is exhaustive because, for each fixed left endpoint, the running
OR changes only at the first occurrence of one of the sixteen coordinates.
Explicit new witnesses are

| mask | inclusive interval in \(T^*\) |
|---|---:|
| `d3cc` | `[6388,6389]` |
| `d3ce` | `[6387,6389]` |
| `dbce` | `[6386,6389]` |
| `b3cc` | `[12825,12826]` |
| `f3cc` | `[12824,12826]` |
| `fbce` | `[12824,12828]` |

Equation (2.2), together with (1.2), proves complete upper coverage. ∎

## 3. Exact P/Q schedules

For a fixed middle order, a three-hole P/Q schedule chooses three omitted
physical starts \(X\) and three omitted deadlines \(Y\). Pair the remaining
starts and deadlines in order. At a physical position, the maximal safe
letter is the intersection of all active middle targets.

The exact event-DAG state is the pair of used-hole counts together with the
OR accumulators of the active middle rows. Two histories reaching the same
state have identical feasible futures, so retaining only the greater selected
prefix area is exact.

### Theorem 3.1

For \(T^*\), the unrestricted three-hole maximum is

\[
X=\{12870,12871,12872\},\qquad
Y=\{0,1,6386\},\qquad A=32{,}226.
\tag{3.1}
\]

The optimistic scalar capacity is \(32{,}235\), and the exact physical
lower-cell count is \(32{,}232\). At (3.1), the exact generalized lower Hall
graph has \(347{,}696\) incidences and matching size
\(26{,}331/26{,}332\). Its complete alternating shore is the isolated target
\(\{\mathtt{0x8000}\}\) with empty neighbourhood.

Thus the maximum-area schedule misses only the physical singleton channel;
there is no nontrivial residual Hall component.

## 4. Singleton retiming and pinned perfect Hall

Augment the event-DAG state by a host automaton with states not-started,
active, and done, the remaining host length, accumulated host OR, and its
owning middle row. For a requested lower target \(S\), an active host cell
uses the maximal safe cap \(E\cap S\), where \(E\) is the active-row
envelope. Reject a selected-start host if its owning middle row ends before
the host. This enumerates every legal host of length one, two, or three over
every realizable three-hole schedule.

### Theorem 4.1

Subject to a physical host for \(S=\mathtt{0x8000}\), the exact maximum is

\[
X=\{12870,12871,12872\},\qquad
Y=\{0,1,6388\},\qquad A=32{,}224.
\tag{4.1}
\]

The host is the singleton interval `[6389,6389]`. Its maximal envelope is
\(\mathtt{0xc304}\), and capping that cell to \(\mathtt{0x8000}\) preserves
every middle row. The optimistic scalar capacity is \(32{,}233\); the exact
physical lower-cell count is \(32{,}230\).

For (4.1), the complete generalized lower Hall graph has

\[
26{,}332\text{ targets},\quad
32{,}230\text{ cells},\quad
347{,}734\text{ incidences},
\]

zero zero-host targets, and a perfect matching of size \(26{,}332\).
More strongly, reserve physical interval index 12,781 for the singleton
\(\mathtt{0x8000}\). The remaining graph has \(26{,}331\) targets,
\(32{,}229\) cells, \(347{,}677\) incidences, no zero host, and a perfect
matching of size \(26{,}331\). Thus the Hall pass does not hide the singleton
inside an incompatible matching.

### Proof

The host-DP described above reaches at most 98 states and returns (4.1). The
literal schedule replay has no empty envelope and no middle-row failure.

For each physical lower cell, let \(E_1,\ldots,E_s\), \(s\le3\), be its
maximal envelopes, and let \(M\) be the carrier bits forced by the middle
rows. The cell individually hosts a lower target \(S\) exactly when

\[
M\subseteq S\subseteq E_1\vee\cdots\vee E_s,
\qquad E_i\cap S\ne\varnothing\quad(1\le i\le s).
\tag{4.2}
\]

Indeed the maximal safe cap at position \(i\) is \(E_i\cap S\); conditions
(4.2) say precisely that these caps are nonempty, have union \(S\), and
retain every forced carrier bit. Enumerating all nonempty rank-below-eight
targets through (4.2), followed by exact bipartite matching, gives the counts
above. A second implementation reserves the singleton cell before matching
and independently obtains the displayed \(26{,}331\)-matching. ∎

## 5. Exact remaining boundary

The genuine-four-filter construction has now passed, integrally and for one
common physical middle order:

1. exact middle ownership;
2. q1 coverage;
3. every upper depth;
4. scalar lower capacity;
5. a prescribed physical singleton host; and
6. the full marginal lower Hall/SDR condition after reserving that host.

What remains is the simultaneous common-cap/common-Q problem. The matched
lower intervals overlap in physical letter positions, so individual caps from
(4.2) need not be mutually compatible. One must construct nonzero physical
letters \(Q_p\subseteq E_p\) which preserve every middle row and realize all
matched lower targets at once, then materialize and exhaustively replay the
literal length-12,873 word. Perfect marginal Hall alone does not prove this.

Accordingly, this theorem does **not** claim a universal K16 word or
\(\nu(16)=12{,}873\).

## 6. Frozen artifacts

- Target materializer:
  `scratch/materialize_r_k16_true_fourfilter_endpoint_reroot_20260731.py`,
  SHA-256 `79528735675ed1e2816de7839378d7953c1c8859415eef20e3b3c8dd43be2fac`.
- Target order:
  `scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word`,
  SHA-256 `c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906`.
- Carrier audit:
  `scratch/k16_true_fourfilter_endpoint_reroot_20260731.audit.json`,
  SHA-256 `7342b65eb6a082dc0c2e463e33015dedcddafab0f3c69632d950e3501d0ff10c`,
  payload `e8a85adffd28b415e03bbcfe842b5785271c25caa74e9f1a6ae6329a9aa1a1b3`.
- Exact all-schedule singleton-host DP:
  `scratch/k16_true_fourfilter_endpoint_reroot_host8000_dp_20260731.audit.json`,
  SHA-256 `eb3b607cacb166d79d7963e033c9da3f580bf72c148dd185616c3f86ea1b9766`,
  payload `cbf4fe763f250a5e6c4c5c2eedd76c2a949cb78e6b5b565985facdae1c1ed81c`.
- Full pinned-schedule Hall replay:
  `scratch/k16_true_fourfilter_endpoint_reroot_host8000_maxpq_hall_20260731.audit.json`,
  SHA-256 `725a9cfbc5f7d1bb4c7c8f5e9ae06ceef4bbaae873332a8dc244a12179f12c8d`,
  payload `09896b296606ad7e4b98b2f5d8cacdff79301131d392b97d721c57930a4599a3`.
- Independent two-reroot replay:
  `scratch/r_k16_true_fourfilter_two_reroot_independent_20260731.audit.json`,
  SHA-256 `469e88277dd100dfb4ee6a2f39fed77ba1f9d0f19f32ea99db0b90ecf9dd5f5a`,
  payload `f3662f28fd979601eebc22b29d82cecd2a71ca5cd41e9754dc88a33cb5db3bc4`.
- Independent pinned capacity and Hall replays:
  `scratch/r_k16_true_fourfilter_reroot_pin8000_capacity_20260731.audit.json`
  (SHA-256 `0f75bca6cadef6b243e11c78a320c59bb8b2b29414eb2519b1d57c49fc0661f1`,
  payload `585913e8b5022cb31895631d267ee30dca7222a404208a2155286d6636124c87`) and
  `scratch/r_k16_true_fourfilter_reroot_pin8000_hall_20260731.audit.json`
  (SHA-256 `7dc309006db70c84be5e2065f38045863cefe54270d26c300ad03fa05f79dc15`,
  payload `adb4a0248a5d50848e071d631bac0a432b98e7db0ef7f1d7025e9a16765b6e47`).
