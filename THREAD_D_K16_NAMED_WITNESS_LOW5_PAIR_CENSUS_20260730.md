# Thread D: exact low-debt named-witness pair census at K16

**Date:** 2026-07-30  
**Status:** complete scoped negative; no length-12,874 word is claimed

## 1. Statement

Write

\[
 A=43129=\mathtt{0xa879},\qquad
 H=10365=\mathtt{0x287d},\qquad
 E=20067=\mathtt{0x4e63}.
\]

Two authenticated length-12,874 one-hole words and one representative sharp
portal in each word were used:

| phase | source word | source hole | fixed portal | blocker after portal |
|---|---|---:|---|---:|
| append | `k16_append0200_12874_onehole.word` | (H) | (p_{6440}\gets8197) | (A) |
| fivephase | `k16_fivephase_rex_hole20067.word` | (E) | (p_{12873}\gets20067) | (H) |

For each portal state, enumerate every one-cell **external fortification** that

1. supplies the blocker by an interval avoiding the portal cell, and
2. leaves at most five literal uncovered targets.

There are exactly 387 such rows in the append state and 500 in the
fivephase state.  For every retained row, a second census then enumerates
every arbitrary nonzero one-cell substitution capable of covering all its
literal debts and evaluates its exact final interval-OR multiplicities.

No pair is universal.  Moreover, no pair produces a new best singleton
phase label:

* all 10,913 minimum append pairs leave precisely (A);
* the 23,019 minimum fivephase pairs leave (H) 23,003 times and (E)
  16 times;
* after forbidding a second edit of the terminal portal itself, all 23,003
  fivephase minima leave (H).

Thus this complete low-debt two-edit fortification fibre returns only to the
already materialized (A/H/E) phase graph.  It contains neither a zero nor a
new sole-hole label.

## 2. Exact completeness lemma

Fix a literal word (W), a portal edit \(\pi\), and a retained fortification
edit (e).  Let

\[
 \mathcal H_e=\{T:c_{W^{\pi,e}}(T)=0\}
\]

be its exact post-fortification hole set.  If a second substitution changes
position (p) to (x\ne0) and yields a universal word, then every
(T\in\mathcal H_e) gets a new witness interval containing (p).  Hence

\[
 x\subseteq T\quad(T\in\mathcal H_e),
 \qquad
 x\subseteq\bigcap_{T\in\mathcal H_e}T. \tag{2.1}
\]

It is therefore complete to enumerate every position (p) and every
nonzero submask of the intersection in (2.1).  For each candidate, let
(L_p,R_p) be the multiplicity-weighted suffix-OR and prefix-OR banks on the
two sides of (p), including the empty state.  If the old and new cell
values are (o,x), the exact change in every target multiplicity is

\[
\Delta c(U)=
-\!\sum_{\ell\in L_p,r\in R_p}
 m(\ell)m(r)[\ell\vee o\vee r=U]
+\!\sum_{\ell\in L_p,r\in R_p}
 m(\ell)m(r)[\ell\vee x\vee r=U]. \tag{2.2}
\]

Equation (2.2) is the literal interval ledger: it includes repeated
witnesses, intervals crossing other edited cells, and every loss as well as
gain.  A candidate is called compatible exactly when its new intervals
cover every member of \(\mathcal H_e\).  The final debt set is then obtained
from (2.2), without a unique-owner or additive approximation.

This proves that the rowwise census is complete for the declared pair
fibre.  In particular, if the minimum final debt is positive in every row,
there is no universal pair in that fibre.

## 3. External-witness certification

The portal position is made a hard break in independent left/right OR banks.
For a fortification at (p\ne p_\pi), an advertised blocker witness is
accepted only if its interval is contained wholly in one of the two open
segments of (W\setminus\{p_\pi\}).  Therefore the witness cannot contain
the portal cell and survives the fixed portal edit literally.

The fortification catalogue stores its exact debt set.  The aggregate audit
reconstructs (W^{\pi,e}) row by row and rejects unless that stored set is
exactly its literal hole set.  It also checks the fortification position,
old value, new value, portal position and portal value against the catalogue.

## 4. Exact ledgers

### 4.1 Append portal

The 387 retained fortifications have debt histogram

\[
 2^{65},\quad3^{17},\quad4^{303},\quad5^2.
\]

Across them the complete second-edit scan evaluated 718,459,318
position/value assignments.  Exactly 280,805 covered every current debt and
were therefore compatible mutual-debt pairs.  Every fortification row has
minimum final debt one; the 10,913 attaining pairs all have final debt set

\[
 \{A\}=\{43129\}.
\]

No candidate word was emitted.

### 4.2 Fivephase terminal portal

The 500 retained fortifications have debt histogram

\[
 1^{16},\quad2^{136},\quad3^1,\quad4^{313},\quad5^{34}.
\]

The complete second-edit scan evaluated 912,277,388 assignments.  Exactly
1,001,631 were compatible mutual-debt pairs.  Again every fortification row
has minimum final debt one.  Among the 23,019 attaining pairs,

\[
 \{H\}\text{ occurs }23,003\text{ times},\qquad
 \{E\}\text{ occurs }16\text{ times}.
\]

The 16 (E)-returns edit the terminal portal cell.  Restricting the second
edit to positions outside that portal leaves exactly the 23,003 (H)-rows.
No candidate word was emitted.

### 4.3 Combined conclusion

The two batches contain 887 fortification rows, 1,630,736,706 evaluated
second assignments, and 1,282,436 compatible pairs.  Every row has a
strictly positive exact final debt.  The only minimum singleton labels are
(A,H,E), so the census neither closes the hole nor enlarges the known phase
graph.

## 5. Scope boundary

The negative result is exact for:

* the two authenticated source words above;
* the representative portals (p_{6440}\gets8197) and
  (p_{12873}\gets20067);
* every one-cell external fortification in the exact catalogues with final
  debt at most five; and
* every arbitrary second one-cell substitution after each such
  fortification.

It does **not** exclude:

* a fortification leaving six or more debts;
* a cooperative first pair in which neither edit alone creates the external
  blocker witness;
* another sharp portal value among the 16 append or 128 fivephase phases;
* insertions, deletions, reordering, or three or more auxiliary edits; or
* another length-12,874 word.

In particular this is not a lower bound for \(\nu(16)\).  The exact global
bracket remains

\[
 12873\le\nu(16)\le12875.
\]

## 6. Reproducible artifacts

Inputs:

* `scratch/k16_append0200_12874_onehole.word`  
  SHA-256 `aa17f3ca70525115c941e906fecf1384bad8302cd95b236413c7f2f3f8777c18`;
* `scratch/k16_fivephase_rex_hole20067.word`  
  SHA-256 `eef3555aa12675de8707de994d20300aaf8e96538b4691880810d84454fbb1b5`;
* `scratch/threadD_k16_append0200_external_low5_20260730.audit.json`  
  SHA-256 `b61885f7095a7885d2f1baa5f835379d0564968b183cbbda506c1e6d0e192812`;
* `scratch/threadD_k16_fivephase_external_low5_20260730.audit.json`  
  SHA-256 `9b7ec70195f7cb72dcae91359ef6e35c26cf93f5fdd90bc98c15181584c07622`.

Exact evaluator and aggregation:

* `scratch/threadD_k16_twohole_return_substitution_census_20260730.cpp`  
  SHA-256 `253df2cc565722d7e9fc6308947f513a35198e94dfc3fd4ad663542652ea83e7`;
* retained H100 binary SHA-256
  `bb966708099ec7889e9a5032a002577aed6ffa26eb85656d8ce5e01ea51d723d`,
  compiled with `g++ 13.3.0`;
* `scratch/threadD_run_named_pair_batch_20260730.sh`  
  SHA-256 `68b945a8cfed83058ad1aab20168de263d633b86d9e2f1aea69b12627df3316d`;
* `scratch/audit_threadD_k16_named_witness_low5_pair_census_20260730.py`  
  SHA-256 `7c2862e1565cf47db2ee8310b4dd708ac9d6a2b748d47841496104898f2c21b7`.

Aggregates and full raw row archives:

* `scratch/threadD_k16_append0200_external_low5_pair_census_20260730.audit.json`  
  SHA-256 `72d2daa0872be8fbbfb47fdd7897da0d28b8b03e4b33074f5579e13391760703`,
  canonical payload `ee431a6e5211708d81d552184fc1edfda526c0a8764aa6685bedaee92a4de9ae`;
* `scratch/threadD_k16_fivephase_external_low5_pair_census_20260730.audit.json`  
  SHA-256 `f03e64eb3fba95fc15c1f64d76a444c9917e3aa89e8c27095e2a88f06e5a42a8`,
  canonical payload `b6184a5cda95a01b2d513910bbba37865fe3c21b4a1e647321267563b42dc4c7`;
* `scratch/threadD_k16_append0200_external_low5_pair_raw_20260730.tar.gz`  
  SHA-256 `e13005e4ba9fb32f758e7e2a765db49b03c8e698a803822a5c482d7bb1540aa2`;
* `scratch/threadD_k16_fivephase_external_low5_pair_raw_20260730.tar.gz`  
  SHA-256 `63f4bb6ac2b024c1dc37e419a533c44761889f21c96de568ba95235bde3484b0`.

Each aggregate embeds the SHA-256 of every raw row audit plus a compact
row-by-row ledger.  Local schema/tar replay verifies 387 and 500 distinct
raw rows respectively.  H100 execution used one CPU and a 512 MiB address
space cap.  Append took 45.81 seconds and fivephase took 57.58 seconds; both
exited zero with 20,480 KiB maximum RSS and no swap.
