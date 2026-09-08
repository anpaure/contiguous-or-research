# True-four-filter endpoint reroot: exact all-shadow carrier and marginal Hall pass

Date: 2026-07-31  
Lane: R  
Status: proved for the stated parent, target order, and P/Q schedule; the joint capped-envelope compiler and literal word are not yet proved

## 1. Authenticated lineage

Let \(w=(w_0,\ldots,w_{6437})\) be the file

    scratch/K15_FOURFILTER_SEED_20260731.word

whose SHA-256 is

    51f57125ea3e145e08ed9d5f8816d22313a010907588457260c824c6f40217f4.

This is the genuine four-filter K15 parent with opening
\((5134,0,5,1,0)\). It is not any of the seed0-derived files whose historical
names contain fourfilter_insert_aug.

Put \(z=0x8000\), and define

\[
D^2_i=w_i\vee w_{i+1}\vee w_{i+2},\qquad
D^3_i=w_i\vee w_{i+1}\vee w_{i+2}\vee w_{i+3}.
\]

Exactly \(D^2_{6390}\) has rank six; the other 6,435 \(D^2_i\)'s have rank
seven. All 6,435 \(D^3_i\)'s have rank eight. The genuine natural K16
chronology is

\[
T=\operatorname{rev}(z\vee D^2_{[0,6390)})
  \;\Vert\;D^3_{[0,6435)}
  \;\Vert\;\operatorname{rev}(z\vee D^2_{(6390,6436)}).
\tag{1.1}
\]

Its canonical newline-terminated SHA-256 is

    0f6d64e9311ef634169964350baa8f817b17b9d1619970c881f87e7346550a5c.

It contains every rank-eight mask exactly once. Its missing q1 colours are

\[
U=0xb3cc,\qquad V=0xd3cc,
\]

and its complete missing upper tower is

\[
\{0xb3cc,0xd3cc,0xd3ce,0xf3cc,0xdbce,0xfbce\}.
\tag{1.2}
\]

## 2. Exact two-reroot construction

Number target positions from zero. Define

\[
T^*=\operatorname{rev}(T[0..6388])
     \;\Vert\;T[6389..12825]
     \;\Vert\;\operatorname{rev}(T[12826..12869]).
\tag{2.1}
\]

The frozen target is

    scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word

with SHA-256

    c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906.

### Theorem 2.1

The order \(T^*\) has all of the following properties.

1. It contains all \(\binom{16}{8}=12,870\) middle targets exactly once.
2. Every rank-nine q1 colour occurs on an adjacent pair.
3. Every upper mask of every rank \(9,\ldots,16\) occurs as a literal
   contiguous interval OR.
4. The exact three-hole P/Q maximum selected area is 32,226, attained at

   \[
   X=(12870,12871,12872),\qquad Y=(0,1,6386).
   \]

   Its formal \(+9\) scalar upper bound is 32,235, and its exact number of
   physical lower cells is 32,232. Both exceed the required lower mass 26,332.
5. The generalized lower Hall graph for that maximum-area schedule has
   matching size 26,331. Its entire Hall obstruction is the isolated singleton
   target 0x8000.

### Proof

Reversing blocks permutes the middle targets, proving (1). All internal
adjacencies of each reversed block are preserved as unordered pairs. Only the
two boundary pairs change. At the prefix boundary,

\[
(0xc3ca,0xc3cc)\longmapsto(0xd38c,0xc3cc),
\]

so the boundary union changes from 0xc3ce to the missing colour 0xd3cc. The
old colour 0xc3ce had multiplicity two. At the suffix boundary,

\[
(0xb38c,0xf30c)\longmapsto(0xb38c,0xb1cc),
\]

so the union changes from 0xf38c to the missing colour 0xb3cc. The old colour
0xf38c also had multiplicity two. No q1 colour is lost, and the two missing
colours are inserted. This proves (2).

For upper replay, use the following exhaustive enumeration lemma. For a fixed
left endpoint \(i\), let \(n_i(c)\) be the first position at or after \(i\)
containing coordinate \(c\). Starting with \(T_i\), the OR of \(T[i..j]\)
changes only when \(j\) reaches one of the at most sixteen values \(n_i(c)\).
Sorting those first-occurrence events lists all distinct interval ORs starting
at \(i\). Thus all interval ORs are enumerated exactly using \(O(16N)\)
first-occurrence events.

That enumeration gives

\[
\operatorname{Cov}(T)\subseteq\operatorname{Cov}(T^*)
\]

and

\[
\operatorname{Cov}(T^*)\setminus\operatorname{Cov}(T)
=\{0xb3cc,0xd3cc,0xd3ce,0xf3cc,0xdbce,0xfbce\}.
\tag{2.2}
\]

No old upper mask is lost. Explicit witnesses for the six new masks are:

| mask | inclusive interval in \(T^*\) |
|---|---:|
| 0xd3cc | [6388,6389] |
| 0xd3ce | [6387,6389] |
| 0xdbce | [6386,6389] |
| 0xb3cc | [12825,12826] |
| 0xf3cc | [12824,12826] |
| 0xfbce | [12824,12828] |

Together with (1.2), this proves (3).

The exact finite-state P/Q recurrence retains, at each physical position, the
numbers of used start/deadline holes and the OR accumulators of every active
middle row. Equal states have identical feasible futures, so retaining only
the greatest area for each state is exact. It has at most sixteen states on
this instance and returns the schedule and area in (4). The generalized Hall
replay constructs every individually feasible length-at-most-three lower
interval cell from its allowed union, mandatory carrier, and active
envelopes. At the maximum-area schedule it has 32,232 cells and 347,696
incidences; maximum matching is \(26,331/26,332\), with canonical shore
\(\{0x8000\}/\varnothing\). This proves (4) and (5). ∎

## 3. Minimality within endpoint reroots

### Proposition 3.1

No single connected reversal of \(T\) installs both missing q1 colours.
Among prefix reversals that install 0xd3cc, exactly one is q1-safe: the prefix
[0..6388]. Among suffix reversals that install 0xb3cc, exactly two are
q1-safe: the suffixes starting at positions 12,781 and 12,826. Consequently
two endpoint reroots are necessary and sufficient within this family.

### Proof

The rank-eight facet positions of 0xb3cc are

\[
1099,1792,2301,2792,3107,5628,12780,12825,12869,
\]

and those of 0xd3cc are

\[
0,554,759,1099,3290,5272,5472,6389,12779.
\]

For a reversal of [a+1..b], the two new pairs are
\((T_a,T_b)\) and \((T_{a+1},T_{b+1})\). To create both missing colours, both
cut indices must belong either to

\[
I_{U,V}=\{i:T_i\subset U,\ T_{i+1}\subset V\}
\]

or to \(I_{V,U}\), according to which new pair creates which colour. Directly
from the displayed facet positions and successors,

\[
I_{U,V}=\varnothing,\qquad I_{V,U}=\{12779\}.
\]

Neither set contains two cut indices, proving the single-reversal no-go.

A prefix reroot can add 0xd3cc only at cut positions

\[
553,758,1098,3289,5271,5471,6388,12778.
\]

At seven positions the removed q1 colour is unique; only cut 6388 removes a
repeated colour. A suffix reroot can add 0xb3cc only after

\[
1099,1792,2301,2792,3107,5628,12780,12825.
\]

Only the last two cuts remove repeated q1 colours. This proves the exact
classification. The choice after 12,825 is (2.1). ∎

This proposition is scoped to connected segment reversals and endpoint
reroots. It does not assert minimality among general alternating circuits or
multi-segment braids.

## 4. Exact singleton-host retiming

The deficiency in Theorem 2.1 is not a fixed-order obstruction.

### Theorem 4.1

Over all realizable three-start/three-deadline-hole P/Q schedules for the
fixed order \(T^*\), the greatest selected area subject to a physical
length-at-most-three host for 0x8000 is 32,224. It is attained by

\[
X=(12870,12871,12872),\qquad Y=(0,1,6388),
\tag{4.1}
\]

with a singleton host beginning at physical position 6,389 and having length
one. The formal scalar capacity is 32,233, and the exact number of physical
lower cells is 32,230.

For schedule (4.1), the uncapped generalized lower Hall graph has 26,332
targets, 32,230 cells, 347,734 incidences, zero zero-host targets, and a
perfect matching of size 26,332.

More strongly, cap physical position 6,389 from 0xc304 to 0x8000 and reserve
its length-one cell for the singleton. Every middle row still replays exactly.
After removing that target and cell, the residual graph has 26,331 targets,
32,229 available cells, 347,677 incidences, zero zero-host targets, and a
perfect matching of size 26,331.

### Proof

Augment the exact P/Q state by a three-state host automaton (not started,
active, done), remaining host length, accumulated host OR, and owning middle
row. At each active host cell use the maximal safe cap
\(E\cap\{0x8000\}\), where \(E\) is the current active-row envelope. This
loses no singleton witness: every feasible cell is contained in that cap, and
enlarging to the cap can only help the singleton OR and active middle unions.
Reject a selected-start host if its owner closes before the host ends. Thus
the dynamic programme enumerates every legal P/Q schedule and every host of
length one, two, or three. It reaches at most 98 states and returns exactly
(4.1) and area 32,224.

The generalized-Hall construction gives the uncapped counts. The independent
pin replay then replaces the maximal envelope at physical position 6,389,
originally 0xc304, by the maximal safe singleton cap 0x8000. Literal middle
replay has zero failures. Reserving this cell and removing the singleton
target gives the displayed residual counts and perfect matching. ∎

## 5. Exact remaining gate

For this genuine-four-filter target order, the following gates are now exact
and passed:

1. middle ownership;
2. q1 coverage;
3. every upper depth;
4. scalar lower capacity;
5. an explicit singleton cap for 0x8000;
6. residual individual physical lower-host Hall.

The remaining compiler gate is joint capped-envelope realization of a perfect
residual matching (equivalently the common-Q/cell-value compatibility
problem), followed by literal word materialization and exhaustive replay.
Marginal Hall does not imply that simultaneous gate. Therefore this note does
not claim a K16 word or \(\nu(16)=12,873\).

## 6. Frozen artifacts

- Materializer and carrier replay:
  scratch/materialize_r_k16_true_fourfilter_endpoint_reroot_20260731.py
- Carrier audit:
  scratch/k16_true_fourfilter_endpoint_reroot_20260731.audit.json
- Exact all-schedule singleton-host DP:
  scratch/audit_r_k16_true_fourfilter_endpoint_reroot_host8000_dp_20260731.py
  and scratch/k16_true_fourfilter_endpoint_reroot_host8000_dp_20260731.audit.json
- Uncapped marginal-Hall replay:
  scratch/k16_true_fourfilter_endpoint_reroot_host8000_maxpq_hall_20260731.audit.json
- Independent carrier replay:
  scratch/r_k16_true_fourfilter_two_reroot_independent_20260731.audit.json
  (SHA-256 469e88277dd100dfb4ee6a2f39fed77ba1f9d0f19f32ea99db0b90ecf9dd5f5a;
  payload f3662f28fd979601eebc22b29d82cecd2a71ca5cd41e9754dc88a33cb5db3bc4).
- Independent singleton-capacity replay:
  scratch/r_k16_true_fourfilter_reroot_pin8000_capacity_20260731.audit.json
  (SHA-256 0f75bca6cadef6b243e11c78a320c59bb8b2b29414eb2519b1d57c49fc0661f1;
  payload 585913e8b5022cb31895631d267ee30dca7222a404208a2155286d6636124c87).
- Independent reserved-pin Hall replay:
  scratch/r_k16_true_fourfilter_reroot_pin8000_hall_20260731.audit.json
  (SHA-256 7dc309006db70c84be5e2065f38045863cefe54270d26c300ad03fa05f79dc15;
  payload adb4a0248a5d50848e071d631bac0a432b98e7db0ef7f1d7025e9a16765b6e47).
