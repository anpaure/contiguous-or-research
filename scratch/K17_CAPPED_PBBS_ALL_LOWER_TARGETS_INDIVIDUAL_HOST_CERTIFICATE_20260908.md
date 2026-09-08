# Every lower target has an individual cap host in the fixed capped k17 bank

**Status.** Exact finite census, 2026-09-08. On the unchanged 146 canonical PBBS cycles, with depth `H=min(height,3)`, every one of the 65,535 nonempty targets of ranks 1 through 8 has an individually legal cap on an interval of at most H positions. The cap retains all 24,310 prescribed rank-9 owners. This does **not** assert that the caps can be applied simultaneously, that other upper targets survive, or that the periodic bank has been compiled into a linear word of length B(17).

## 1. Fixed input and exact meaning of a host

The input is [the canonical cycle file](k17_height_adaptive_20260908/height_adaptive_canonical_cycles.json), obtained in the earlier deterministic height-adaptive construction. Its SHA-256 is

`fed20c313c639740b089428c1d2b8b572fc7138de4c11c2203be554e4acfa2a3`.

Every lower-owner cycle starts at its least integer mask and follows g=f²; cycles are ordered by that least mask. No cuts, orders, or owners were searched or changed. There are 146 cycles and 24,310 cyclic positions.

For a component with upper owners X_i, invariant height h and period v, put H=min(h,3) and

\[
D_i=\bigcap_{z=0}^{H}X_{i+z}.
\]

All indices are cyclic. The verifier rebuilt these capped-depth letters from the owners, rather than using the stored full-height source. It checked every letter is nonempty and

\[
\bigcup_{z=0}^{H}D_{j+z}=X_{j+H}
\]

at every position. The depth census is 17 positions at H=1, 2,159 at H=2, and 22,134 at H=3.

A host for target S is a cyclic interval I of length 1≤|I|≤H on which replacing D_i by D_i∩S realizes S as the interval union, leaves all letters nonempty, and retains every prescribed owner window. Other positions remain unchanged.

## 2. Exact deficit criterion

This criterion holds for any shrinking set of positions I, not just the present short intervals. Define

\[
V_I=\bigcup_{i\in I}D_i,\qquad
G_I=\bigcup_j\left(X_{j+H}\setminus
\bigcup_{i\in[j,j+H]\setminus I}D_i\right).
\]

Only windows meeting I contribute. If a shrinking cap on I has union S and retains all owner windows, then G_I⊆S⊆V_I: a coordinate absent outside I in a window must be supplied by the cap. Conversely, if G_I⊆S⊆V_I, the uniform intersection cap E_i=D_i∩S retains every window. Indeed, a required coordinate either already occurs outside I, or belongs to G_I and has an occurrence inside I that survives intersection with S. Its interval union is V_I∩S=S.

For singleton positions let Pin_i=G_{\{i\}}. The short-interval theorem in [the independent cap proof](PBBS_EXACT_SHORT_TARGET_CAPS_AND_CAPACITATED_MATCHING_REDUCTION_20260908.md), §§2–3, states

\[
\operatorname{Pin}_i=(X_i\setminus X_{i-1})\cup
(X_{i+H}\setminus X_{i+H+1}),\qquad
G_I=\bigcup_{i\in I}\operatorname{Pin}_i\quad(|I|\le H).
\]

The census does not simply assume these formulas: it computes each Pin by removing that position separately from every affected owner window, and computes each G_I directly by removing the whole interval. Every equality holds. Each Pin_i is nonempty and contained in D_i. Thus if G_I⊆S, each E_i contains Pin_i and is nonempty.

Consequently, the complete host menu on I is exactly the Boolean interval

\[
\{S:G_I\subseteq S\subseteq V_I\}.
\]

Enumerating its submasks is exhaustive; it does not miss another shrinking cap with a different distribution of coordinates inside I.

## 3. Exact census

| Target rank | Distinct targets with hosts | Missing |
|---:|---:|---:|
| 1 | 17 | 0 |
| 2 | 136 | 0 |
| 3 | 680 | 0 |
| 4 | 2,380 | 0 |
| 5 | 6,188 | 0 |
| 6 | 12,376 | 0 |
| 7 | 19,448 | 0 |
| 8 | 24,310 | 0 |
| Total | 65,535 | 0 |

There are 70,737 short intervals and 915,416 interval-target incidences. All enumerated targets already have rank at most eight. The incidence counts by capped depth are H=1: 1,088; H=2: 111,520; H=3: 802,808.

Every coordinate has exactly the same singleton census:

- 127 legal host positions, all intervals of length one;
- 44 distinct components;
- 7 positions in components of original height 2;
- 120 positions in components of original height 3;
- no singleton hosts at original height 1 or at heights 4–8.

The certificate lists the component and position of every singleton host. These are counts of actual positions, not counts of target occurrences with multiplicity inside a longer cap interval.

## 4. Independent checks and reproducibility

The [verifier](census_k17_capped_short_target_hosts_20260908.py) performed:

1. All 24,310 periodic owner reconstructions.
2. 95,047 single-position exclusion-window checks establishing the Pin formula.
3. All 70,737 direct interval-deficit comparisons with the union of Pins.
4. 347,157 owner-window replays for the minimum cap S=G_I, proving preservation for every larger cap by monotonicity.
5. A separate actual cap replay for one host of every one of the 65,535 covered targets, checking nonempty letters, exact interval union, and 334,109 affected owner windows.

The one deterministic job ran only on h100, with CPU/wall/address-space limits of 120 seconds / 150 seconds / 2 GiB. Reported runtime was 1.59 seconds. There was no optimization or random search.

Artifacts:

- [Compact certificate and all singleton hosts](k17_capped_short_hosts_20260908/capped_short_host_certificate.json).
- [One exact host for every lower target](k17_capped_short_hosts_20260908/capped_short_target_first_hosts.json).
- [Exact number of hosts for every lower target](k17_capped_short_hosts_20260908/capped_short_target_host_counts.json).
- [Executable verifier](census_k17_capped_short_target_hosts_20260908.py).

The remote verifier is `/home/amodo/census_k17_capped_short_target_hosts_20260908.py`; output directory `/home/amodo/exact-b-k17-capped-short-hosts-20260908/`.

The concrete remaining interface is simultaneous allocation of compatible caps while preserving the required target palette. Individual feasibility is now exhaustively settled for this fixed periodic bank; simultaneous feasibility is not supplied by this certificate.
