# K16 radius-three provider partition, all-three obstruction, and frozen-gap collars

Date: 2026-07-30  
Lane: R  
Status: exact reductions only; no new SAT/UNSAT claim

## 1. Frozen data

The authenticated universal word is

```text
answers/k16_upper12874.word
length 12874
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e.
```

Its unique best deletion is

```text
W = scratch/k16_upper12874_best_delete.word
length 12873
SHA-256 a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649,
```

whose sole missing target is

\[
 B=11373=\mathtt{0x2c6d}.
\]

The complete arbitrary-radius-at-most-two theorem for this exact word is
already frozen in
`MATH_AUDIT_R_K16_12873_DELETE_RADIUS2_NORMAL_FORM_20260730.md`.
The closest saved radius-two child has sole hole
`0xa86d`; its complete one-edit continuation merely returns the hole to
`0x2c6d`.  That latch closes one radius-three branch, not radius three as a
whole.

## 2. Complete radius-three provider partition

### Theorem 2.1 (one/two/three-site witness partition)

Let `W'` be obtained from `W` by making three genuine substitutions at
distinct positions (each new nonzero mask differs from the old mask).  If
`W'` is universal, then at least one of the following
holds for a literal final interval whose OR is `B`.

1. The interval contains exactly one changed position.
2. The interval contains exactly two changed positions.
3. The interval contains all three changed positions.

Conversely, the union of the three corresponding exact affected-interval
models contains every radius-three completion.

#### Proof

`W` has no `B` interval, so every final `B` interval contains at least one
changed position.  There are exactly three changed positions, giving the
three cases.  In case 1 the final value at the contained site, by itself,
already creates the same `B` interval; the other two sites lie outside it.
In case 2 the two contained final values jointly create the same interval and
the third site lies outside it.  Case 3 contains all sites.  Thus no fourth
case exists.  For fixed edited sites, all old target occurrences avoiding the
sites survive, while every lost last occurrence must be replaced by an
interval meeting the sites.  Enumerating those affected intervals with their
literal left-suffix/right-prefix ORs is therefore necessary and sufficient.
\(\square\)

This is an exact completeness theorem, but not yet a negative radius-three
theorem.  In particular, independent one-edit provider catalogues alone do
not cover cases 2 and 3.

### 2.2 Exact branch models

The smallest faithful staged global model is as follows.

* **One-site branch.** Enrich each of the already enumerated `27,064`
  one-cell `B` provider assignments by one protected literal witness
  interval.  Put the other two sites outside that interval, then use the
  exact arbitrary two-edit private-target model on the resulting word.
  The two remaining edits must be allowed to cooperate; sequential
  one-provider filtering is not complete.
* **Two-site branch.** Use the `13,235` exact pair supports from the
  radius-two joint-provider theorem, retain a literal pair witness, put the
  third site outside it, and impose an exact arbitrary one-edit completion
  ledger.  The existing `102,404,745` value-pair census is a valid starting
  bank, though a per-support SAT table is smaller than storing all rows.
* **Three-site branch.** For `p<q<r`, every unchanged cell of
  `(p,r)\setminus\{q\}` must be a submask of `B`.  Let `C_{pqr}` be the OR
  of all unchanged `B`-submask cells in the maximal compatible extension,
  omitting `p,q,r`.  The three new values `u,v,w` obey

  \[
  0<u,v,w\subseteq B,\qquad C_{pqr}\vee u\vee v\vee w=B. \tag{2.1}
  \]

  For the fixed sites, call a target private when every old witness meets at
  least one site.  A private target is required to have a new witness in one
  of the six possible affected classes

  \[
  \{p\},\{q\},\{r\},\{p,q\},\{q,r\},\{p,q,r\};
  \]

  `{p,r}` is impossible by contiguity.  Equality of the corresponding
  prefix/suffix OR expression to the target is an exact table clause.  For
  exact Hamming distance three one must additionally impose
  `u != W_p`, `v != W_q`, and `w != W_r`.  Thus every positional support
  gives a tiny iff instance with only 24 primary value bits.  Omitting those
  three inequalities is a safe relaxation for a no-go proof.

### Proposition 2.2 (exact three-site support count)

The frozen word has `B`-submask run histogram

\[
 240\cdot1,\qquad27\cdot2,\qquad7\cdot3.
\]

There are exactly `13,627` increasing positional triples `p<q<r` that can
support a literal `B` interval containing all three edited sites.  These are
potential all-three supports; they may overlap the one-site or two-site
branches before the latter branches are explicitly excluded.  Their span
histogram is

| `r-p` | supports |
|---:|---:|
| 2 | 12,871 |
| 3 | 629 |
| 4 | 110 |
| 5 | 17 |

Hence no three-site provider support has span above five.

#### Proof

For fixed endpoints `p<r`, count the source cells not contained in `B`
strictly between them.  If there are none, any of the `r-p-1` internal sites
may be `q`.  If there is exactly one, it is forced to be `q`.  If there are
at least two, no single middle edit can remove all forbidden bits.  Summing
these alternatives gives the table: `418` supports have zero bad interior
cells and `13,209` have one.  The same recurrence reproduces the already
frozen pair-support count `13,235`, with span histogram
`{1:12872,2:315,3:41,4:7}`.  \(\square\)

The independent light census is

```text
scratch/audit_r_k16_upper12874_delete_radius3_supports_20260730.py
SHA-256 ae08fcc2bfd34fcecd78e2acc2176906a110eb72be8e06934117ded761c1e5dd

scratch/r_k16_upper12874_delete_radius3_supports_20260730.audit.json
SHA-256 e300b79ad60636d5c4d010d3bd8e66d6538046aed86f87b71357664c28937aba
payload f3243351700ffe00f9c99902972c26108e4128e8d42a6fb6eb68c08aec20631b.
```

### Theorem 2.3 (solver-free exclusion of the all-three-site branch)

No universal word is obtained from `W` by three substitutions whose final
literal `B` witness contains all three edited sites.  This remains true in
the relaxation that permits any of the three new values to equal its source
value.  Hence all `13,627` potential supports in Proposition 2.2 are
impossible.

#### Proof

Fix a support `p<q<r` and put `S={p,q,r}`.  A target `T` is *private to S*
when every old literal `T` interval meets `S`; equivalently, no `T` interval
lies in any of the four components of `W-S`.  Every nonprivate target keeps
an untouched old witness, while every private target needs a new affected
witness.

An affected interval meets one of the six consecutive nonempty site classes

\[
 E\in\{p,q,r,pq,qr,pqr\}. \tag{2.2}
\]

For such a class let `F_E` be the finite family of ORs of the fixed cells in
literal intervals whose edited-site intersection is exactly `E`.  If the new
values are `u,v,w`, the interval OR is exactly

\[
 F\vee\bigvee_{s\in E}x_s,\qquad F\in F_E. \tag{2.3}
\]

In particular, because all three new values are submasks of `B`, a necessary
condition for a private target `T` to be recoverable is

\[
 \exists E\ \exists F\in F_E:\quad F\subseteq T\subseteq F\vee B. \tag{2.4}
\]

Call (2.4) the *relaxed private-target test*.  It is deliberately more
permissive than a genuine assignment: it allows the edited contribution to
be chosen independently for each target and class, allows it to be zero,
and ignores consistency among `u,v,w`.  Therefore failure of (2.4) for one
private target rigorously excludes the support.

Exact distinct-running-OR scans determine privacy without storing all
intervals.  If `f(T)` is the earliest right endpoint of an old `T` interval
and `l(T)` its latest left endpoint, then `T` is private precisely when

\[
 f(T)\ge p,\quad l(T)\le r,
\]

and `T` is absent from each of the two short open segments `(p,q)` and
`(q,r)`.  Applying (2.4) excludes `13,620` supports.  The complete survivor
list consists of seven consecutive triples:

| sites `(p,q,r)` | source values | private targets | fixed bases |
|---|---|---:|---:|
| `(1,2,3)` | `(0x2069,0x0065,0x0424)` | 11 | 21 |
| `(2686,2687,2688)` | `(0x0c68,0x0c29,0x0c2c)` | 17 | 33 |
| `(3529,3530,3531)` | `(0x2c48,0x2c60,0x2864)` | 19 | 35 |
| `(3958,3959,3960)` | `(0x0465,0x2025,0x2840)` | 17 | 39 |
| `(4486,4487,4488)` | `(0x2849,0x2408,0x2069)` | 21 | 42 |
| `(4498,4499,4500)` | `(0x2c48,0x284c,0x2849)` | 20 | 40 |
| `(5922,5923,5924)` | `(0x2829,0x280d,0x2c05)` | 25 | 31 |

It remains to check shared-value consistency on these seven.  Let

\[
 D=\{x:0<x\subseteq B\},\qquad |D|=2^8-1=255,
\]

and for a site class `E` define the exact OR-state table

\[
 A_E(T)=\{z\in D:\exists F\in F_E,\ F\vee z=T\}. \tag{2.5}
\]

A triple \((u,v,w)\in D^3\) installs `B` through all three sites exactly when
\(u\vee v\vee w\in A_{pqr}(B)\).  It recovers a private `T` exactly when
one of

\[
\begin{aligned}
u&\in A_p(T),&v&\in A_q(T),&w&\in A_r(T),\\
u\vee v&\in A_{pq}(T),&v\vee w&\in A_{qr}(T),&
u\vee v\vee w&\in A_{pqr}(T)
\end{aligned} \tag{2.6}
\]

holds.  Thus an exact solver-free dynamic program stores, for each of the
`255^2=65,025` ordered pairs `(u,v)`, the bitset of admissible `w` states,
initializes it with the all-three `B` condition, and intersects (2.6) for the
private targets.  The following short prefixes already empty every state:

| sites | contradiction prefix (hex) | surviving `(u,v)` counts |
|---|---|---|
| `(1,2,3)` | `142d,146d,246d` | `27584,2048,0` |
| `(2686,2687,2688)` | `0c29,0c69,0c6d` | `28209,2304,0` |
| `(3529,3530,3531)` | `2866,2a66,2ae6,2c60,2c66,2c6c` | `27584,27584,27584,608,544,0` |
| `(3958,3959,3960)` | `0665,2025,2465,2665,2840` | `4320,606,4,4,0` |
| `(4486,4487,4488)` | `226d,22ed,2408,2669,266d,26ed,26fd,28c9` | `36736,36736,280,88,88,88,88,0` |
| `(4498,4499,4500)` | `284d,2a4d,2b49,2b4b,2b4d,2c4d` | `37719,36736,2048,2048,2048,0` |
| `(5922,5923,5924)` | `282d,283d,2939,293d,2979,297d,2b79,2c05` | `37719,1879,162,162,162,162,162,0` |

The counts are numbers of ordered `(u,v)` pairs retaining at least one
admissible `w`, not numbers of triples.  Equations (2.5)--(2.6) enumerate
the exact 8-bit OR-state algebra; no SAT solver, heuristic cutoff, or
independent-value relaxation remains on these seven rows.  Since the DP even
allows `u=W_p`, `v=W_q`, or `w=W_r`, its empty result excludes the genuine
three-substitution fibre a fortiori.  Together with the relaxed exclusion of
the other `13,620` supports, this proves the theorem.  \(\square\)

Fail-closed artifacts:

```text
scratch/audit_r_k16_radius3_allthree_overapprox_20260730.py
SHA-256 c6b8561ad7677de6492a15d97f150c6814697dad363b52b856c4d2d582cf932a

scratch/r_k16_radius3_allthree_solverfree_obstruction_20260730.audit.json
SHA-256 51dad15c6e7bbee6b2771906588d4af79130aa0d9bfacb7456b6c8ca3f4121f8
```

The checker independently scans supports without a span cutoff, asserts the
word has sole hole `B`, pins the earlier full support-audit hash, reproduces
the complete span histogram, and asserts all seven final assignment fields
are null.

## 3. The complete frozen-gap collar alternative

The verified 12,874-word arose from three editable collars of widths
`5/9/4`, separated by two frozen gaps.  Keep both gap strings byte-for-byte
and in the same order, remove one slot from exactly one collar, and assign
arbitrary nonzero masks to all 17 surviving collar positions.

### Theorem 3.1 (three-profile exhaustion, with exact scope)

Within this architecture the only width profiles are

\[
 (4,9,4),\qquad(5,8,4),\qquad(5,9,3). \tag{3.1}
\]

For a fixed profile, the associated interval-pattern CNF is satisfiable if
and only if that frozen-gap class contains a universal length-12,873 word.

#### Proof

Exactly one of the original `5+9+4` editable slots is removed.  Removing a
slot from the first, second, or third collar gives the three profiles in
(3.1).  Its location inside that collar is immaterial because every
surviving collar value is again arbitrary; the fixed gaps and their order are
the only retained data.  This proves exhaustion **inside the stated
architecture**.

The fixed gaps have ORs `0x7fff` and `0xffff`.  The fixed runs themselves
cover all but the same 57 residual targets in each profile.  For every one of
those targets, each whole intervening gap contains a forbidden bit.  Hence a
residual witness cannot cross either gap and lies in one collar, extended by
a suffix and prefix of its adjacent frozen runs.

For each consecutive editable subinterval, the adjacent suffix and prefix OR
chains are nested.  Among bases contained in a target there is a unique
maximal base.  It dominates every smaller compatible base: if
`F OR Y = T` and `F subseteq F' subseteq T`, then `F' OR Y = T`.  Therefore
one exact equality witness per target and local editable interval is both
necessary and sufficient.  Intervals wholly in fixed runs were already
retained.  This proves the iff statement.  \(\square\)

This exhaustion does **not** cover deletion of a frozen-gap cell, movement of
a gap boundary, alteration/reordering of either gap, nonlocal rethreading, or
an arbitrary length-12,873 word.

### Theorem 3.2 (245-value closure normal form)

Let `R` be the 57 residual targets.  For any nonzero value `v` contained in
some member of `R`, define

\[
 N(v)=\bigcap\{T\in R:v\subseteq T\}.
\]

If `v` is contained in no member of `R`, replace it by the live sentinel
`0x0001`.  This normalization preserves satisfiability.  Its exact nonzero
image has 245 values and a 257-clause, 932-literal bit-CNF per cell.

#### Proof

Whenever `v subseteq T` with `T in R`,

\[
 v\subseteq N(v)\subseteq T.
\]

Thus replacing every cell of a literal `T` witness by its closure cannot
lose a bit of `T` or introduce a bit outside `T`.  A dead value occurs in no
residual witness; changing it to the sentinel cannot destroy one.  Targets
outside `R` retain their witnesses wholly inside fixed runs.  Conversely, a
normalized assignment is itself an allowed arbitrary nonzero assignment.
Hence the original and normalized fibres are equisatisfiable.  Direct
intersection closure and exhaustive evaluation of the defining CNF both
give exactly 245 nonzero models.  \(\square\)

The exact reduced dimensions are:

| profile | local intervals | value bits | witnesses | variables | clauses |
|---|---:|---:|---:|---:|---:|
| `4/9/4` | 65 | 272 | 3,705 | 3,977 | 124,558 |
| `5/8/4` | 61 | 272 | 3,477 | 3,749 | 109,268 |
| `5/9/3` | 66 | 272 | 3,762 | 4,034 | 127,201 |

The closure-domain clause count is `17*257=4,369`; the displayed totals omit
the 17 duplicate standalone nonzero clauses already present in that domain
CNF.

Frozen light-audit artifacts:

```text
scratch/audit_k16_12873_three_profile_closure_model_20260730.py
SHA-256 29b4b252b3014abf7e9f0c28747b2ffdd02636f73ace645985794d5f0034b7d2

scratch/k16_12873_three_profile_closure_model_20260730.audit.json
SHA-256 2753f984a606bee946423e1296198a80ff0f0c497c9c05cda3798606af0ce892
payload d33f79a5dbbc002471828cd286a482609b5780ec032daf13dc966f58252c0b47.
```

No solver verdict is asserted by this theorem.

## 4. Recommended next exact model

Do not duplicate the already running `4/9/4` job.  If it does not produce an
authenticated answer, the smallest independent exact frozen-gap model **by
both displayed CNF dimensions among (3.1)** is the closure-normalized
`5/8/4` profile:

```text
3,749 variables; 109,268 clauses; 245 allowed cell values;
representative source SHA-256
982a9e9c4ecc19fee69dfa9f5cdbdd51874647e66ee735e139bf445236ec00a3.
```

It is smaller than `4/9/4` by 228 variables and 15,290 clauses and smaller
than `5/9/3` by 285 variables and 17,933 clauses.  A SAT row must be decoded
and independently replayed against all 65,535 targets.  An UNSAT claim needs
a checked proof log.

If the priority is instead a **globally complete substitution-radius-three
theorem around `W`**, Theorem 2.3 has now closed the all-three-site branch.
The exact remaining work is the two-site-plus-one-edit branch and the
one-site-plus-two-edit branch of Section 2.2.  Excluding the all-three bank is
not by itself a global radius-three result.

## 5. Exact boundary

Proved here:

* the complete one/two/three-site provider partition for radius three;
* the exact 13,627-support all-three-site bank and span-five bound;
* the solver-free exclusion of every all-three-site support;
* the iff interval model for each of the three frozen-gap profiles; and
* the 245-value equisatisfiable closure reduction with exact dimensions.

Not proved here:

* existence or nonexistence of a universal length-12,873 word;
* feasibility of any of the three profile CNFs;
* infeasibility of global radius three around `W` (the one-site-plus-two-edit
  and two-site-plus-one-edit branches remain); or
* any claim outside the two fixed-gap architecture.
