# Thread D: exact lifetime/gap postprocessor and compiler Benders bridge

**Date:** 2026-07-29  
**Status:** implemented and calibrated.  The k11 compact schedule passes the exact fixed-carrier compiler and emits an independently verified optimal word; the resident k15 schedule is rejected exactly before compiler invocation.  No new k15 carrier or word is claimed.

## 1. Fail-closed compact candidate schema

Before this implementation the lifetime/gap master existed only as a theorem and pseudocode.  The retained schema is `threadD-lifetime-gap-candidate-v1`.  It stores, in physical cyclic run order,

\[
\ell_t=\text{positive lifetime},\qquad g_t=\text{following zero gap},
\qquad 0\le t<N,
\]

in voltage-one gauge with the first coordinate-zero insertion seam fixed at edge zero.  Put

\[
p_0=0,\qquad p_{t+1}=p_t+\ell_t+g_t.                 \tag{1.1}
\]

The parser requires

\[
\ell_t\ge d+1,\quad g_t\ge1,\quad
\sum_t\ell_t=rN,\quad \sum_t g_t=(k-r)N,\quad p_N=W, \tag{1.2}
\]

and both

\[
(p_t\bmod N)_t,\qquad (p_t+\ell_t\bmod N)_t          \tag{1.3}
\]

to be permutations of \(\mathbb Z_N\).  The complete literal arrays and a canonical schedule digest are mandatory; unknown JSON fields, booleans masquerading as integers, wrong sums, wrong gauges, and nonpermutation seam residues fail closed.

The scalar trace is reconstructed, not trusted:

\[
c_{p_t+a}=1\quad(1\le a\le\ell_t),                  \tag{1.4}
\]

with all other positions zero.

## 2. Exact event and carrier reconstruction

The quotient insertion and deletion symbols are forced by the lifted seam sheets:

\[
\beta_{p_t\bmod N}=-\left\lfloor\frac{p_t}{N}\right\rfloor\pmod k,
\]

\[
\alpha_{(p_t+\ell_t)\bmod N}
=-\left\lfloor\frac{p_t+\ell_t}{N}\right\rfloor\pmod k.             \tag{2.1}
\]

At physical edge \(j+sN\),

\[
\alpha_{j+sN}=\alpha_j+s,qquad
\beta_{j+sN}=\beta_j+s\pmod k.                       \tag{2.2}
\]

The maps \(\alpha,\beta:\mathbb Z_N\to\mathbb Z_k\) are ordinary repeated-value functions.  They are **not** permutations when \(N>k\).  Only the start and end residues (1.3) are permutations.  On resident k15, every label occurs roughly 25--34 times.

The carrier is reconstructed from the scalar trace by

\[
T_i=\{x\in\mathbb Z_k:c_{i-xN}=1\}.                  \tag{2.3}
\]

The postprocessor then checks every physical transition against

\[
T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.               \tag{2.4}
\]

It independently replays rank, Johnson adjacency, run-start/end transversals, residence, the erosion tower, middle ownership, and lower-q1 ownership.  Embedded source carrier hashes are comparison data only; they are never reconstruction inputs.

## 3. Exact shadow separation

For q2 the postprocessor uses the event identity

\[
T_i\cap T_{i+1}\cap T_{i+2}
=T_i\setminus\{\alpha_i,\alpha_{i+1}\}.             \tag{3.1}
\]

It evaluates (3.1) on quotient starts, expands the actual rotation orbits, and cross-checks the result against the literal physical intersection scan.

For every upper interval width \(w\), without a residence assumption,

\[
\bigcup_{a=0}^{w-1}T_{i+a}
=T_i\cup\{\beta_i,\ldots,\beta_{i+w-2}\}.           \tag{3.2}
\]

The implementation computes the next physical insertion of each currently absent coordinate, adds tied arrivals together, and enumerates every distinct insertion prefix until the full set.  This arbitrary-width result is cross-checked against both retained physical/all-width upper oracles.  No three-width, eight-width, or other fixed cap is used.

The eager carrier gate requires middle/q1 exactness, residence and erosion, every lower depth \(2\le q<d\), and unrestricted upper completeness.  Terminal depth \(d\) is deliberately left to the compiler/Hall subproblem.

## 4. Exact compiler boundary

Only a carrier passing the preceding gates is converted to the retained fixed-carrier compiler.  That compiler performs:

1. maximal cyclic erosion-envelope construction and \(D^dP=T\) replay;
2. core-free weighted quotient Hall;
3. one joint CP-SAT model over every equivariant cyclic one-core and every physical target assignment;
4. independent weighted Hall replay and a fresh physical matching;
5. exact safe-cut enumeration;
6. word construction, exhaustive missing-mask verification, and the independent literal verifier.

A durable positive additionally passes `compiler_ready_pass_report`, which rechecks exact dimensions and target counts, both Hall totals, the physical matching, safe-cut membership, output hashes, derivative identities, middle orientation, and the retained literal word.

This negative model is exact for the declared **equivariant cyclic one-core** architecture.  It does not claim to quantify arbitrary non-equivariant physical cores.  The physical target matching inside the architecture is exact.

Neither `sandwich2.py` nor `ready15.py` is imported or consulted.  In particular, `sandwich2` UNSAT and `ready15 READY` have no proof role.

## 5. Proof-safe Benders feedback

Every valid compact schedule reconstructs a unique \(c\) and carrier.  Consequently:

- a failed middle/q1/q2/all-width-upper gate yields a full `(life,gap)` assignment no-good;
- each missing q2 or upper orbit is retained as an exact symbolic target-witness row;
- those target rows may be installed directly only when the outer master channels the complete event/trace equality literals;
- without those channels, no local-run projection is claimed: only the full schedule no-good is executable;
- a guarded exact compiler failure accepted by `compile_failure_cut` is pulled back to a full schedule no-good, scoped to the equivariant-one-core compiler architecture;
- `UNKNOWN`, timeout, sampled-core failure, unsupported architecture, malformed metadata, or an in-memory-only positive result emits **no cut**.

The full no-good is

\[
\bigvee_t(\ell_t\ne\ell_t^*)\ \vee\
\bigvee_t(g_t\ne g_t^*).                              \tag{5.1}
\]

No fixed-core Hall shore is projected onto lifetimes.  Distinct shores can require incompatible cores, so such a projection would be unsound without a separately proved collar/assumption-core theorem.

## 6. Exact calibrations

### k11 positive schedule

The compact schedule derived from the retained exact carrier has

\[
\min\ell=4,\quad\max\ell=21,\quad\sum\ell=252,
\]

\[
\min g=1,\quad\max g=18,\quad\sum g=210.
\]

It reconstructs an owner-perfect carrier with zero q2, terminal, and arbitrary-width upper holes.  The exact H100-CPU compiler returns:

```text
status                         VERIFIED_OPTIMAL
envelope/selected Hall         231/231
physical matching              231
safe cuts                      242
variables / constraints        3696 / 5355
output length                  465
literal missing masks          0
```

The newly retained word has SHA-256

```text
2713ef237d315f07a4cf7311ff6313b7855f24f9e1c4537aecf41efbd84d3eb3
```

and the independent verifier confirms `VERIFIED_OPTIMAL`, all 2,047 nonempty masks, and the exact middle row.

### k11 exact compiler failure

A second compact k11 schedule passes the complete carrier gate but has one terminal-depth missing orbit.  The exact core-free envelope Hall certificate is

```text
flow / demand / deficiency      220 / 231 / 11
deficient target orbit          25
status                          ENVELOPE_HALL_INFEASIBLE
```

`compile_failure_cut` independently replays that certificate, emits an exact full-c no-good, and the postprocessor pulls it back to the 42-lifetime/42-gap no-good (5.1).

### resident k15

The resident compact schedule has lifetime range 4--32, gap range 1--44, lifetime sum 3,432 and gap sum 3,003.  Event and carrier reconstruction, ownership, and residence all pass.  Exact shadow separation gives

```text
q2 missing orbits               47
terminal q3 diagnostic          11
all-width upper missing         95
target certificates             142
```

The one-core compiler is therefore **not invoked**.  The result is an unconditional full-schedule carrier/shadow no-good, not a `sandwich2` or `ready15` conclusion.

## 7. Artifacts and hashes

| artifact | SHA-256 |
|---|---|
| `scratch/threadD_lifetime_gap_exact_postprocessor.py` | `b909e6eb9df33b1be83ceb51bdcf371912657419d4aed191dbb31fb632fecf64` |
| `scratch/test_threadD_lifetime_gap_exact_postprocessor.py` | `89dd5fa5090d37d926e1a85283089b756f68f26d270d7b1ce14db7eb6d6b71cf` |
| k11 positive candidate | `74988c79a719ad8f4de8d8cfca6f6dca3b44ff5838ecac1cc625304328a9e1ea` |
| k11 positive audit | `d0019ee52f7863ef0a75e258c753918da6caba29f78f95f62d28d9163adb865c` |
| k11 verified word | `2713ef237d315f07a4cf7311ff6313b7855f24f9e1c4537aecf41efbd84d3eb3` |
| k11 failure candidate | `435521b73202574d7e940538daedf839a3637db6192b70818a3f55541b6b7091` |
| k11 failure audit | `f95a64cddb5fed2137818a0f8fc1cea4b05bafc8cfeaabdd5bef0987d1a0c402` |
| k11 failure cut | `4be88183b05bdd6d1abdb64f332aef8667e13e713dd91785108b7815f6ca1a8f` |
| resident k15 candidate | `cb305e65d9e1ba8797555f3c9c5fd6f797597548b3495bd1822f89d286883d9b` |
| resident k15 audit | `6b088496445476bb5daa73ce9c9a0ceddda841c0bc5e384375ff0fc1aaeecb26` |
| resident k15 cut | `3579a6884cce9a260ec21dded17bfa55f4214dff3b26311272ece6e6d7c765d5` |

All heavy work used one H100 CPU core (`taskset -c 63`, `nice -n 10`; no GPU):

- k11 exact positive compile: 0.63 s;
- k11 exact envelope-Hall failure: 0.55 s;
- resident k15 reconstruction/separation: 1.85 s, with no core solve;
- original five-test H100 replay: 3.74 s; final six-test local artifact replay: 2.98 s.

## 8. Remaining gate

The postprocessor and exact fixed-carrier compiler boundary are now closed.  The missing k15 theorem is upstream: produce a compact lifetime/gap schedule with exact middle/q1 ownership, no required lower holes, and no arbitrary-width upper holes.  Such a schedule will automatically enter the retained exact compiler; any conclusive failure will return only a proof-scoped full-schedule no-good unless a stronger channelled event/collar cut is separately proved.
