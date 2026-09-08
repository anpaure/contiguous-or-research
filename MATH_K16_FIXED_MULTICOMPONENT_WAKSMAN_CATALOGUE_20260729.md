# Fixed multi-component, multi-voltage Waksman catalogue

Date: 2026-07-29  
Status: exact theorem for a prescribed unit-voltage catalogue, implemented and
physically audited at `K=8,10`; no `K=16` existence claim.

## 0. Result

The compact one-component even-`K` Waksman CNF extends to a prescribed list
of quotient components without increasing its asymptotic size and, at
`K=16`, without changing its variable count at all.

For

\[
 K=2r,\qquad n=K-1,\qquad W=\binom Kr,\qquad N=W/n,
\]

fix a catalogue

\[
 \mathcal C=((M_1,v_1),\ldots,(M_s,v_s)),\qquad
 \sum_iM_i=N,\qquad v_i\in\mathbb Z_n^*.
\tag{0.1}
\]

There is an exact componentwise `(c,t)` chart with `W` old-coordinate bits
and `N` top-coordinate bits.  It represents `s` equivariant quotient cycles
of sizes `M_i` and voltages `v_i`.  The middle, lower-shadow, and selected
upper-shadow occurrences from all components can be pooled into the same
partial-permutation Waksman cover networks used by the connected model.

This is **without loss inside the prescribed catalogue class**.  It is only
a sufficient class for the original problem: the component sizes and
relative voltages are fixed; every voltage is required to be a unit; every
component is cyclic and equivariant; and shadow-safe opening/splicing plus
the final lower compiler remain external.

The implementation is

* `scratch/search_even_multicomponent_waksman_cnf_20260729.cpp`;
* `scratch/decode_even_multicomponent_waksman_20260729.py`.

It deliberately does not modify the live one-component solver source.

## 1. Exact chart

For component `i`, let `u_i=v_i^{-1} mod n`, let

\[
 c_i\in\{0,1\}^{nM_i},\qquad t_i\in\{0,1\}^{M_i}.
\]

For integer `j`, reconstruct a middle owner `T_{i,j}` by

\[
 x\in T_{i,j}
 \quad\Longleftrightarrow\quad
 c_i[j-xu_iM_i]=1\qquad(x\in\mathbb Z_n),
\tag{1.1}
\]

with the index reduced modulo `nM_i`, and put the fixed top coordinate `z`
in `T_{i,j}` iff `t_i[j mod M_i]=1`.

Then

\[
 T_{i,j+M_i}=\rho^{v_i}T_{i,j}
\tag{1.2}
\]

exactly.  Indeed, `v_i u_i=1 mod n`, so replacing `j` by `j+M_i`
in (1.1) is the same as replacing `x` by `x-v_i`.

Consequently the `M_i` quotient columns lift to one physical cycle of length
`nM_i`.  More generally, a quotient voltage `v` lifts to `gcd(v,n)` physical
cycles.  The current implementation requires `gcd(v_i,n)=1`; this is a
deliberate subclass, not a theorem that nonunit voltages may be discarded.

### Johnson and residence constraints

At every quotient position `j`, impose:

1. `|T_{i,j}|=r`;
2. exactly one coordinate starts and exactly one coordinate ends between
   `T_{i,j}` and `T_{i,j+1}`;
3. every cyclic `1`-run of `c_i` and `t_i` has length at least `d+1`.

The first two conditions are exactly the rank-`r` Johnson condition.  The
third is exactly the minimum-residence condition on the lifted physical
cycle.  All-one component words are handled correctly: they have no short
run boundary and represent one full cyclic run.

The global top count and top-run cap are the same as in the connected chart.
No window crosses a component seam.

## 2. Exact cover semantics

For each requested statistic, the encoder builds its quotient occurrence
words over **all** components:

* middle owners;
* adjacent intersections (`q1`);
* triple intersections (`q2`, when `d>=3`);
* unions of each requested catalogue width.

Every occurrence word is given an independent phase in `Z_n`.  A Waksman
network permutes the phased occurrence words.  The first `R` outputs are
pinned to the `R` target orbit representatives; any surplus occurrence
words occupy the remaining outputs.

Thus the network is an exact compact encoding of an injection

\[
 \{\text{target orbits}\}\hookrightarrow
 \{\text{occurrence orbits}\}
\]

together with the target phases.  It is not a probabilistic relaxation and
does not use occurrence-by-target selector products.

For the middle layer the two cardinalities are equal, so its injection is a
bijection.  The independent decoder reconstructs every physical cycle and
checks rank, Johnson adjacency, residence, voltage, middle uniqueness, and
both catalogue and all-width shadow coverage directly.

## 3. What is and is not WLOG

Changing the chosen representative at quotient vertex `a` changes edge
phases by a coboundary and preserves each component voltage.  A global
coordinate multiplier can normalize one unit voltage to one, but it
multiplies every component voltage by the same unit.  Therefore relative
voltages remain genuine data.

Accordingly:

* representative gauges and component starting points/orientations are
  WLOG;
* a prescribed catalogue `(M_i,v_i)` is encoded exactly;
* one chosen unit voltage may be globally normalized to one;
* one component, all voltages equal to one, unit voltages, or a prescribed
  component-size partition are **not** WLOG for the original problem.

The fully arbitrary equivariant factor is instead described by a successor
permutation with edge phases; see
`MATH_THEOREM_AD_EVEN_MULTICOMPONENT_CT_WAKSMAN_NORMAL_FORM_20260729.md`.
The fixed-catalogue encoder here is the smaller immediately runnable
subclass suggested by the successful multi-spiral cases.

## 4. `K=16` exact counts

With default upper widths `2,3,4,6,9,13`, the balanced catalogue

\[
 (M_1,v_1)=(429,1),\qquad (M_2,v_2)=(429,4)
\]

has:

| quantity | count |
|---|---:|
| variables | 3,984,274 |
| clauses | 15,455,157 |
| literals | 44,812,639 |
| Waksman switches | 85,914 |
| phase words | 7,722 |
| phase muxes | 463,320 |
| Boolean sort comparators | 262,240 |

The highly unbalanced catalogue `(855,1),(3,4)` has the same variable count,
15,455,154 clauses, and 44,812,561 literals.  Component partitioning changes
only a handful of simplified cyclic clauses.  It does **not** reintroduce
the huge selector tensor.

Machine-readable counts are in:

* `scratch/even_multicomponent_waksman_k16_429_429_20260729.count.json`;
* `scratch/even_multicomponent_waksman_k16_855_3_20260729.count.json`.

These are count-only artifacts.  No `K=16` SAT or UNSAT result is claimed.

## 5. Small audits

### `K=8`: genuinely new two-component audit

A gauge-reduced catalogue scan found SAT for

\[
 (M_1,v_1)=(1,1),\qquad(M_2,v_2)=(9,2).
\]

The independent physical decoder reports:

* physical component lengths `7` and `63`;
* zero rank, Johnson, residence, voltage, and middle-duplicate defects;
* zero middle, `q1`, `q2`, catalogue-upper, and arbitrary-upper misses.

The certificate is
`scratch/even_multicomponent_waksman_k8_20260729_PASS.json`.

This matters structurally: the extension captures a real factor with two
different relative voltages, not merely the old connected voltage-one
solution written twice.

The balanced fixed catalogue `(5,1),(5,2)` returned scoped UNSAT in 0.92 s;
this says only that that particular component-size/voltage class is empty.

### `K=10`: backward compatibility audit

The known connected voltage-one `K=10` `(c,t)` source was pinned into the
new encoder with catalogue `(28,1)`.  Kissat returned SAT, and the independent
decoder found a single physical cycle of length `252` with zero defects and
zero misses at every audited shadow, including arbitrary upper widths.

The certificate is
`scratch/even_multicomponent_waksman_k10_20260729_PASS.json`.

A free search of the particular two-component catalogue `(1,1),(27,2)` hit
the deliberately short 180-second audit timeout.  It has no verdict and
must not be reported as UNSAT.

## 6. Correct interpretation of any future verdict

A SAT model is a strong carrier/factor certificate but still requires:

1. shadow-safe opening and splicing of its components;
2. the lower compiler;
3. literal verification of the final word.

An UNSAT result proves only nonexistence inside the fixed catalogue and the
requested width set.  It does not refute another partition, other relative
voltages, a nonunit-voltage factor, the arbitrary successor-permutation
normal form, a nonequivariant factor, or the final conjecture.

The older compact canonical-ID CP-SAT run ended with `std::bad_alloc` under
its memory cap.  That was `RESOURCE_LIMIT`, not UNSAT.  It should not be
restarted merely to duplicate this model; the Waksman/Kissat representation
is the compact live lane.
