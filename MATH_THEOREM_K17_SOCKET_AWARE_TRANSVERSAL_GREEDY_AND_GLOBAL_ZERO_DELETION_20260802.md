# K17 socket-aware outer seed: exact transversal greedy and global-zero deletion

**Date:** 2026-08-02  
**Status:** exact weighted static-selector theorem and compiled implementation.
The phase-zero global menu, weighted run, and first strict component-Pareto
incumbent are now frozen in
`MATH_AUDIT_K_K17_GLOBAL_SOCKET_MENU_WEIGHTED_SEED_AND_COMPONENT603_PARETO_20260802.md`.
This is an outer-seed theorem only; common-state
`1S`, residence, upper shadows, topology, common-cap, compiler, and word
remain separate.

The authoritative static master is
`MATH_THEOREM_K17_TWO_MATCHING_DONOR_PATH_AND_JOINT_1S_ROTS_GATE_20260802.md`
(SHA-256
`b252f59b76e5ea613842d3633ecba8fb81f47477ae9b2fa1eee467cd9aff99a5`).

## 1. Transversal-matroid formulation

Let `L=H` be the `18646` real bottom donors.  On the right put the `1748`
singleton hosts `F` and the `18646` hard row hosts `H`.  The real incidence
graph has

\[
 u\sim F\iff B_u\subsetneq R_F,
 \qquad
 u\sim v\iff B_u\subsetneq M_v.                       \tag{1.1}
\]

A set of right hosts is independent when it can be matched injectively into
the real donors.  These independent sets form the transversal matroid
`M(G)` on `F union H`.

Every augmented-perfect-matching table is a basis `B` of `M(G)` satisfying

\[
                         F\subseteq B.                \tag{1.2}
\]

The dummy/short set is

\[
                         S=H\setminus B,              \tag{1.3}
\]

and has size `1748`.

### Lemma 1.1 (mandatory singleton coverage)

Condition (1.2) is necessary, not a heuristic.  Dummy vertices have no
edges to singleton hosts, so every `F` must be matched by a real donor in
every augmented perfect matching.  Conversely, once a basis containing `F`
is chosen, the omitted `1748` hard hosts can be filled by the `1748`
indistinguishable dummies.

Thus the first exact check is whether the complete set `F` is independent.
Failure of its augmenting-path matching is a genuine terminal Hall no-go.

### Theorem 1.2 (the exact short-set matroid)

Assume `F` is independent and the real incidence graph has full transversal
rank `18646`.  Contract `F` and put

\[
                 M_{\rm short}:=(M(G)/F)^*             \tag{1.4}
\]

on ground set `H`.  Then a set `S\subseteq H` is the dummy/short set of an
augmented perfect matching if and only if `S` is a basis of
`M_short`.  In particular,

\[
                         |S|=1748.                     \tag{1.5}
\]

#### Proof

An augmented table with short set `S` has real-covered right basis

\[
                         F\mathbin{\dot\cup}(H-S).
\]

Thus `H-S` is a basis of `M(G)/F`.  Complements of bases of a matroid are
exactly the bases of its dual, proving (1.4).  The rank is

\[
 |H|-r(M(G)/F)=18646-(18646-1748)=1748.\qquad\square
\]

Consequently a declared admissible bank `A subset H` contains a feasible
short set exactly when

\[
                         r_{M_{\rm short}}(A)=1748.     \tag{1.6}
\]

The two Hall inequalities in Theorem 4.2 are the literal transversal
oracle for (1.6); they are not a separate relaxation.

### Corollary 1.3 (when socket selection is matroid intersection)

Suppose each prospective short slot is adjacent to a set of **private
one-role tickets**, and a collection of slots is socket-feasible exactly
when its members can be assigned injectively to distinct tickets.  Those
collections form a transversal matroid `T_socket` on `H`.  Selecting the
short bank is then the exact common-basis problem

\[
 S\text{ is a basis of }M_{\rm short},\qquad
 S\in\mathcal I(T_{\rm socket}),qquad |S|=1748,       \tag{1.7}
\]

and is ordinary two-matroid intersection.

This corollary does **not** apply automatically to the common-state menu.
A literal short occurrence normally consumes a correlated left endpoint,
right endpoint, address, and flag pair.  With shared endpoint or flag
resources, feasible slot sets need not be a matroid.  The smallest
**abstract fixed-ticket** counterexample has three slots

\[
 a=(\ell_1,r_1),\qquad b=(\ell_2,r_2),\qquad
 c=(\ell_1,r_2).                                      \tag{1.8}
\]

Both `{a,b}` and `{c}` are feasible matchings of the two endpoint shores,
but neither `c+a` nor `c+b` is feasible.  Hence the augmentation axiom fails.
This is not asserted to be an occurrence-labelled K17 witness: alternative
K17 tickets could restore an exchange.  Proving or refuting the matroid
axiom for the actual menu requires the complete physical ticket catalogue,
not its degree/mask projection.

There is now also a literal but deliberately narrower K17 witness in the
frozen two-socket endpoint-incidence relaxation:

\[
 I=\{4353\},\qquad J=\{2637,6211\}.                  \tag{1.9}
\]

The ticket for `I` conflicts with the first `J` ticket at successor `6218`
and with the second at predecessor `4350`, whereas the two `J` tickets are
mutually compatible.  This is independently replayed in
`scratch/r2_k17_mshort_socket_exchange_20260802/` (audit SHA
`6fee69bebcff905c8ff78b95e7ec48055fa6a5ec678ec3b2b02237710502bd65`).
It proves that this **partial fixed-table socket-packing relaxation** is not
a matroid.  It does not prove that `I` or `J` extends to a complete cycle
cover, and it does not close exchange for the bottom-dependent global
catalogue.

For any proposed compressed socket bank, the load-bearing test is therefore

\[
 I,J\in\mathcal I,\ |I|<|J|
 \Longrightarrow
 \exists e\in J-I:\ I+e\in\mathcal I.                \tag{1.10}
\]

Unless (1.10) is proved (or a literal one-role ticket representation is
exhibited), full occurrence-labelled socket tickets must remain in the
joint selector.  Per-slot degrees and flag masks are only lower-bound
pricing data.

## 2. Exact minimum-cost algorithm

Give every hard host `v` an integer dummy cost `c_v`; costs depend on the
dummy-matched slot only.  The target is

\[
                    \min_{B\text{ basis},\ F\subseteq B}
                    \sum_{v\in H\setminus B}c_v.       \tag{2.1}
\]

Since `sum_(v in H)c_v` is constant, (2.1) is equivalent to maximizing

\[
                    \sum_{v\in B\cap H}c_v.            \tag{2.2}
\]

### Theorem 2.1 (contracted transversal greedy)

The following algorithm solves (2.1) exactly.

1. Match every mandatory `F` host by alternating augmentation.  If this
   fails, report `MANDATORY_F_NOT_INDEPENDENT`.
2. If a proof-safe force-real bank `Z subset H` is prescribed, augment every
   `v in Z`.  Failure reports that the restricted face is empty.
3. Sort `H-Z` in nonincreasing order of `c_v`, breaking ties by row id.
4. For each `v` in that order, retain it exactly when one alternating
   augmenting path extends the current matching to include `v`.  Stop at
   rank `18646`.
5. Declare every omitted hard host dummy-matched.

The result minimizes (2.1) among all bases containing `F union Z`.

#### Proof

Matching all of `F union Z` proves it is independent.  Contract that set in
the transversal matroid.  The standard weighted matroid-basis greedy theorem
says that scanning the remaining elements by nonincreasing weight and adding
an element iff independence survives produces a maximum-weight basis of the
contraction.  An alternating augmenting-path search is an exact independence
oracle for a transversal matroid: it succeeds precisely when the current
right-host set plus `v` has a matching.  Equation (2.2) converts maximum
covered cost to minimum omitted/dummy cost.  \(\square\)

A failed augmentation at one prefix never becomes repairable by later
elements: dependence is upward closed.  The algorithm may rematch all
previously retained hosts; it is not a frozen-edge greedy.

### Corollary 2.2 (additive score equals min-cost flow)

Give every real bottom unit supply, give one dummy-bank node supply `1748`,
retain every real-to-host edge, join the bank to the declared admissible hard
slots, and give every right host capacity one.  Put cost `c_v` only on the
bank-to-`v` arc.  A full flow of value `20394` is exactly an augmented
perfect matching, and its cost is exactly `sum_(v in S)c_v`.

Hence min-cost flow, minimum-cost augmented matching, and Theorem 2.1's
weighted transversal-basis greedy have identical optima.  Greedy is the
specialized exact algorithm which avoids materializing the 1,748 labelled
dummy copies.

## 3. Socket-aware costs

For a shortened hard row `v`, let `Omega_v` be a declared common-state
socket catalogue and define

\[
 d_v=|\Omega_v|,
 \qquad
 q_v=|\{(\alpha,\beta):\Omega_v
                       \text{ contains that flag pair}\}|.  \tag{3.1}
\]

Any additive score can be converted to a dummy cost.  For example,

\[
 c_v=-\bigl(A\,1_{d_v>0}+Bq_v+\min\{d_v,D\}\bigr)      \tag{3.2}
\]

with explicit integer weights favors short slots having nonzero supply,
flag diversity, and high degree.  If lexicographic optimization is desired,
choose each higher-level coefficient larger than the maximum possible total
of all lower-level terms, or run the same exact algorithm serially on tied
faces.

Equivalently, if `w_v` is a nonnegative score with **larger meaning more
desirable as a short slot**, take

\[
                         c_v=C-w_v.                   \tag{3.3}
\]

The algorithm sorts by descending `c`, which is ascending `w`: low-score
hosts are covered by real bottoms first and high-score hosts are left for
dummies.  This sign convention is load-bearing.  Sorting by descending
`w` would optimize the opposite objective.

The optimality theorem is with respect to the supplied `c_v`, regardless of
how predictive those costs are.  A current-table or incomplete-catalogue
degree is therefore safe as a **heuristic cost**.  It is not safe as a hard
deletion rule.

## 4. Proof-safe global-zero deletion

For a hard row `v`, its shortened payload is fixed:

\[
                         Q_v=(M_v,R_v).                \tag{4.1}
\]

Define the **global** socket family `Omega_v^global` by enumerating every
exact five-cell common-state hyperarc using `Q_v` and:

* every predecessor/successor long payload realizable by an allowed
  augmented matching, including substituted bottoms;
* every long flag and every allowed short address;
* the declared owner phase and the declared `beta<=alpha` restriction.

### Theorem 4.1 (global-zero unit)

If a complete, independently replayed catalogue proves

\[
                         \Omega_v^{global}=\varnothing, \tag{4.2}
\]

then every `1S-ROTS` solution satisfies `s_v=0`.  Equivalently, `v` may be
forced into the real-covered basis before weighted greedy.

#### Proof

If `s_v=1`, row `v` is short with payload (4.1).  Its `1S` exact-one row
requires one common-state hyperarc.  Completeness of the global catalogue
says none exists under any legal outer completion, a contradiction.
\(\square\)

There is an edge-conditioned version for singleton hosts.  If the complete
global catalogue for the short mode

\[
                         (B_u,R_F)                     \tag{4.3}
\]

is empty, delete the terminal assignment edge `x_(u,F)`.  Again, the
catalogue must range over every compatible outer completion.

The following are **not** proof-safe global-zero certificates:

* zero degree in the fixed round-47 table;
* zero degree against only original long payloads;
* a union-over-address supplier zero;
* a catalogue omitting relay-substituted bottoms or either endpoint side.

Those quantities may be used in (3.2), but not as units.  This distinction
prevents a fixed-table Hall halo from being promoted to a global cut.

### Theorem 4.2 (exact admissible-bank Hall fail-fast)

Let `A subset H` be the declared set of hard slots allowed to be dummy/short,
and put `Z=H-A`.  For a real-bottom set `X subset H`, let `N_F(X)` and
`N_H(X)` denote its singleton-host and hard-host neighborhoods in (1.1).
There is an augmented perfect matching with every dummy in `A` if and only
if, for every `X subset H`,

\[
 |N_F(X)|+|N_H(X)|\ge |X|,                           \tag{4.4}
\]

and

\[
 |N_F(X)|+|N_H(X)\cup A|\ge |X|+1748.                \tag{4.5}
\]

Equivalently, the mandatory right-host set

\[
                         F\cup Z                     \tag{4.6}
\]

is independent in the transversal matroid.

#### Proof

Apply Hall to `X union Y`, where `Y` is a set of labelled dummies.  For
`Y=empty`, Hall is (4.4).  For nonempty `Y`, all dummies have common
neighborhood `A`; the strongest case is all 1,748 dummies and gives (4.5).
Conversely these two cases exhaust all left subsets.  The equivalence with
(4.6) follows by filling the omitted hard slots with the dummy bank.
\(\square\)

Both inequalities have an exact maxflow/mincut oracle.  For (4.5), retain
right shore `P=F union Z`, put capacity one from a source to every real
bottom and from every retained right host to the sink, and put effectively
infinite capacity on real-to-host incidences.  If the reachable real set of
a minimum cut is `X`, then

\[
 \operatorname{cut}-|P|
 =|N_F(X)|+|N_H(X)\cup A|-|X|-1748.                  \tag{4.7}
\]

The analogous full-right-shore cut gives (4.4).  Thus failure emits a
literal violating `X`, not merely a failed greedy prefix.

If `A={v:Omega_v^global is nonempty}` comes from a complete global menu,
failure is an exact necessary `1S` outer no-go.  Passing proves only that the
static outer matching can avoid globally socketless slots.  If `A` is an
approximate, soft-only, or fixed-table bank, the same Hall verdict is exact
only for that declared restricted bank and has no global-no-go force.

## 5. Benders interface

The selector emits exactly `1748` terminal `x` assignments, `16898` hard
`p` assignments, and `1748` short slots.  The selected `18646` real
assignments uniquely determine the materialized table.  Therefore an exact
fixed-child UNSAT verdict permits the proof-safe full no-good

\[
              \sum_{e\in x^*\cup p^*}z_e\le18645.      \tag{5.1}
\]

Smaller socket/Hall cuts still require a verified signed assumption core of
the complete global activation formula.  Weighted optimality does not make
a fixed child core monotone.

## 6. Implementation

The compiled source is

```text
scratch/k_rots_k17_joint_1s_20260802/
  build_k17_socket_aware_transversal_greedy_20260802.cpp
```

It:

* reconstructs the exact Boolean incidence graph by rank-seven/rank-eight
  submask lookup;
* contracts and matches all mandatory singleton hosts;
* optionally forces externally certified global-zero hard slots real;
* runs the exact admissible-bank maxflow/mincut test before greedy and emits
  the violating real-token set `X`, its complete right-neighbor list, the
  retained-`Z` hard-neighbor count, and an independently recomputed literal
  slack on failure;
* runs exact weighted transversal greedy with full alternating rematching;
* emits `x,p,s`, materializes the table, and replays all 65,535 lower
  targets, the optimal histogram, owner/root phase, and all 17 soft rows.

Input costs have schema

```text
row_donor  dummy_cost  global_socket_degree  flag_pair_mask
```

An optional force-real file has schema

```text
row_donor  global_zero_certificate_sha256
```

The implementation verifies the declared slot has zero diagnostic degree
and flag mask, but the cited certificate remains load-bearing for global
catalogue completeness.  Without such a certificate, pass `-` and use zero
degrees only as costs.

The final command argument is `global_complete` or `scoped`.  It changes no
combinatorics; it controls only whether a failed admissible-bank Hall test is
reported as a global necessary no-go or as a restricted-face obstruction.

If the mandatory contracted set `F union Z` is dependent, the implementation
reports `PROVED_GLOBAL_ZERO_FORCE_SET_NOT_EXTENDABLE`.  When all certificates
in `Z` satisfy Theorem 4.1, this is an exact outer no-go: every `1S` solution
must cover `Z` by real bottoms, but no such real matching exists.

The authenticated weighted run is reported in the audit cited at the start
of this note.  Its additive objective remains only a seed cost; it is not a
simultaneous ticket certificate.

## 7. Current K17 interface after the zero-projection report

The phase-0 relay trajectory now has an independently replayed complete
lower projection matching `16898/16898` after 47 strict exchanges, with no
isolated hard head and the static rows unchanged.  The frozen table and
independent projection audit have SHA-256 values

```text
95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735
2b79c35507d07be6c1fbb1503ceff0701ebf11184230b030bc3bfec8f761361a
```

and live under

```text
scratch/k_rots_k17_joint_1s_20260802/warm47/
```

No further lower-projection repair belongs in this lane: the remaining
exact selector must choose a basis of
`M_short` together with full occurrence-labelled common-state tickets and
the reset/chronology rows.

The defect-zero table is a warm start, not a frozen fibre.  Its fixed
relaxed-nine common-state census still has only `2,188` accepted socket
hyperarcs and `5,969` zero short roles, so that fixed child is exactly
state/reset UNSAT.  The joint master must therefore rematerialize some
`x/p/s` placements while retaining a perfect `16898` hard-head projection;
it must not resume scalar projection repair and must not pin all 47-exchange
placements.

The independently replayed fixed-soft endpoint census
`MATH_AUDIT_K_K17_FIXED_SOFT_ENDPOINT_BANK_NO_COMMON_ADDRESS_20260802.md`
shows that none of the `18,646` hard short slots can use fixed soft-long rows
on both sides.  Hence every surviving socket column must expose at least one
dynamic real-bottom long endpoint.  This is a useful column-generation
restriction, but not a global-zero unit and not a substitute for the joint
ticket selector.

The complete ordinary phase-0 local menu has `10,167` nonzero and `8,479`
zero hard slots.  Its exact admissible-bank test passes: the two Hall slacks
are `(0,0)`, so the nonzero bank contains a basis of `M_short`.  Independent
reproduction gives

```text
Hall audit
d8d7f5aa451d6ac8c3fb6b08b2cb06f3bf5b8ca8fe7ce7031ccc985998a5d92f

materialized weighted table
3886de626d55d4393d3f71f51fa9799488608f26eb977a8ff60e7be39cfac7cd
```

This is the sharp positive converse to global-zero deletion: scalar
admissibility and the short-basis row are compatible.  It still neither
assigns occurrence tickets injectively nor closes common-state degrees.

The later positive theorem
`MATH_THEOREM_Q_K17_PHASE0_RETAINED_WITNESS_PRIVATE_OUTER_BASIS_20260802.md`
does close the H-short private-ticket/outer-extension row at rank `1748`.
The current residual interface is therefore the protected `5647`
fixed/free ticket DNF and `9520`-edge long--long completion in
`MATH_THEOREM_K17_PROTECTED_H_SHORT_PRIVATE_BANK_AND_FIXEDFREE_BRANCHFLOW_GATE_20260802.md`;
further H-only dummy-slot scoring is obsolete on that protected face.
