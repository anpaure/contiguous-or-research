# K=16 deletion basin: complete radius-two normal form and source audit

Date: 2026-07-30

## 1. Frozen instance and verdict

Let

```
W = scratch/k16_upper12874_best_delete.word
SHA-256(W) = a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649
|W| = 12873
B = 11373 = 0x2c6d
```

Exact replay gives `B` as the sole missing nonzero contiguous-OR target.
The word is obtained by deleting zero-based position 1 (value `0x2800`)
from the authenticated universal word `answers/k16_upper12874.word`.

The deletion and radius-one prerequisites were independently recomputed by a
second implementation:

```
scratch/ad_k16_upper12874_deletion_radius1_independent_20260730.audit.json
SHA-256 2c3cc484afbf2fd07aae1a9c99f8c110ece941b7f7608f44fce0c0d7c4360fe6
```

It reproduces the complete 12,874-deletion histogram and proves that position
1 is the unique deletion leaving one hole.  On the resulting word it tests
the complete exact radius-one candidate set: 77,153 nonzero replacements
survive the necessary common-submask filter, and none is universal.  This is
stronger provenance than relying only on the provider summary named below.

The following is the exact finite conclusion supported by the frozen
catalogues and the source audit below.

**Theorem 1 (complete radius-two obstruction for this word).**  There is no
universal length-12873 word obtained from `W` by changing at most two distinct
positions to arbitrary nonzero 16-bit values.

The theorem is word-specific.  It says nothing about a different deletion,
about three or more substitutions, or about an arbitrary length-12873 word.

The primary radius-one provider summary is recorded in
`scratch/k16_upper12874_best_delete_oneedit.audit.json`; the independent
audit above validates the complete radius-zero/one prerequisite.  The
exact-two part is the union of the two exhaustive and logically complementary
cases proved in Sections 2 and 3.

## 2. Exact normal form

For a word `U` and a target `T`, write

\[
 \mathcal I_T(U)=
 \{[a,b]:\bigvee_{i=a}^b U_i=T\}.
\]

Consider two genuine substitutions at distinct sites `p<q`, with new values
`u,v`, and suppose the resulting word is universal.  Since
`\mathcal I_B(W)` is empty, precisely one of the following alternatives
applies.

### 2.1 Sequential-provider case

At least one of the two one-edit intermediates already has a `B` witness.
Orient that edit first.  If its intermediate word is `W'` and its hole set is
`D`, then the second edit must create a witness of every target in `D`.
Every such new witness contains the second site.  This gives the complete
first-provider/second-repair catalogue.  Exact scoring after the second edit
is still required, because it can destroy last witnesses of targets outside
`D`.

The frozen exhaustive result is

```
scratch/k16_12873_deletebest_twoedit_full.audit.json
SHA-256 dc46acdd4cfb6eb77ea6bf32324b67197bec919a06ef2b7f1b853162facfad69
```

It contains all 27,064 nontrivial first substitutions which individually
install `B`.  Its debt histogram sums to 27,064 and its largest debt is 19,
so the recorded cutoff 32 removes no row.  All 27,064 rows were retained and
646,720 exact second-service assignments were scored.  No completion exists;
the best residual has two holes.

### 2.2 Genuinely joint-witness case

Suppose neither one-edit intermediate has a `B` witness.  Then every final
`B` witness must contain both edited sites.  Indeed, a witness containing only
one site would already exist in the corresponding one-edit intermediate.

It follows that

1. every unchanged cell strictly between `p` and `q` is a submask of `B`;
2. `u` and `v` are nonzero submasks of `B`; and
3. if `C_{pq}` is the OR of the maximal contiguous collection of unchanged
   `B`-submask cells which can accompany `[p,q]`, excluding `p,q`, then

\[
 C_{pq}\vee u\vee v=B. \tag{2.1}
\]

Conversely, these conditions give a literal `B` interval: take the maximal
compatible extension.  Thus they characterize the joint provider exactly.

For fixed `p,q`, let `A_{pq}(T)` be the number of old `T` intervals which
contain `p` or `q`.  A nonzero target is *private* to the pair when

\[
 \#\mathcal I_T(W)=A_{pq}(T).
\]

All nonprivate targets retain an unchanged witness.  Therefore a joint
candidate is universal if and only if (2.1) holds and its new affected
intervals contain every private target.  Splitting new affected intervals
into `p`-only, `q`-only, and both-site intervals gives, for every private
target `T`, the exact finite constraint

\[
 L_{pq,T}(u)\ \lor\ R_{pq,T}(v)\ \lor\
 M_{pq,T}(u\vee v). \tag{2.2}
\]

This is the private-target criterion implemented by the joint tool.

The frozen exhaustive result is

```
scratch/k16_12873_deletebest_joint2.audit.json
SHA-256 aa2fbf3fe87069f75c4acb33cfcfcb61c4531b991a0054733a83f1f8abf99348
```

It reports 13,235 support pairs and 102,404,745 exact replacement pairs.  No
completion exists.  Its best candidate leaves the sole hole
`43117=0xa86d`:

```
p=6439: 8301=0x206d -> 8300=0x206c
q=6440: 32877=0x806d -> 1133=0x046d.
```

A separate lightweight start-by-start replay reproduced exactly this one
hole.

## 3. Completeness proof

If one edit alone installs `B`, orient it first; the final pair occurs in the
sequential catalogue because the second edit must supply every intermediate
hole.  If neither edit alone installs `B`, any final `B` interval must contain
both sites, and the pair occurs in the joint catalogue by (2.1).  These cases
exhaust all exact two-substitution completions.  Together with the separate
one-substitution census, they prove Theorem 1.

The two catalogues overlap computationally: the joint program deliberately
does not reject a pair merely because it also has a one-site `B` witness.
That overlap is harmless for a no-go theorem.

## 4. Independent catalogue checks

The target `B` has eight set bits.  In `W`, exactly 315 cells are submasks of
`B`, in runs

\[
 240\cdot 1,\qquad 27\cdot 2,\qquad 7\cdot 3.
\]

Hence the complete joint support catalogue has no gap above four and has

| distance `q-p` | supports |
|---:|---:|
| 1 | 12,872 |
| 2 | 315 |
| 3 | 41 |
| 4 | 7 |
| **total** | **13,235** |

This independently matches the joint audit.

There is also a closed-form check of the replacement count.  Put
`c=|C_{pq}|`, `d=8-c`.  Before excluding unchanged endpoint values, the
number of ordered nonzero submask pairs satisfying (2.1) is

\[
 N(C)=3^d4^c-2^{c+1}+\mathbf1_{d=0}. \tag{4.1}
\]

For a fixed nonzero endpoint submask `a`, let

\[
 r=|B\setminus(C\vee a)|,
 \qquad
 F(a,C)=
 \begin{cases}
 2^{8-r},&r>0,\\
 2^8-1,&r=0.
 \end{cases}
\]

Then the exact count for the support is

\[
 N_{pq}=N(C)
 -\mathbf1_{W_p\subseteq B}F(W_p,C)
 -\mathbf1_{W_q\subseteq B}F(W_q,C)
 +\mathbf1_{W_p,W_q\subseteq B,\ C\vee W_p\vee W_q=B}. \tag{4.2}
\]

Summing (4.2) over the 13,235 supports gives 102,404,745, exactly the
reported joint replacement count.  This check does not replay the heavy
search; it independently checks that its support/value loops were untruncated.

## 5. Source audit, including `excluded_position=-1`

Frozen sources:

```
scratch/search_k16_exact_two_edit_blocker_fortification_20260730.cpp
SHA-256 8f092cf2297691fd697e96f8859d9dec8db8c024dba4309a97051f988c08f9f0

scratch/search_k16_exact_joint_two_edit_blocker_20260730.cpp
SHA-256 2b2ed3a3775ea440de1fcc8725102197c073282c388642d2c293ca47da5eaa9c
```

No logical or off-by-one defect was found for `excluded_position=-1`.

1. In the sequential tool, no physical position equals `-1`, so no first or
   second site is skipped.  The optional external-witness test also counts all
   witnesses because no interval contains position `-1`.
2. In the joint tool, every portal-crossing comparison with `-1` is false and
   both maximal-extension loops stop only at a cell having a bit outside `B`.
   Thus the 13,235-support catalogue is global, not collar-restricted.
3. The left/right OR banks, middle prefix/suffix chains, and both-site product
   enumerate disjoint affected interval classes with exact multiplicities.
   A target is declared private exactly when all of its old occurrences are
   in those classes.  Constraint (2.2) is consequently necessary and
   sufficient.
4. Integer ranges are safe here: interval multiplicities use signed 64-bit
   counts; chain multiplicities are at most 12,873; aggregate loop counters
   use 64 bits.

### Reporting defects and caveats

The following are real provenance/reporting defects, but do not invalidate
the present conclusion after the independent count checks above.

1. Neither audit JSON embeds the input SHA or source SHA.
2. The sequential JSON omits `MAX_FIRST_ROWS`; the joint JSON omits
   `MAX_POSITION_PAIRS`.  Worse, the emitted `PASS_EXHAUSTED...` status does
   not change when either optional cap truncates a run.  For these particular
   artifacts, `first_rows=first_service_assignments=27064`, the complete debt
   histogram, and the independently derived 13,235 support count rule out
   truncation.
3. The joint source calls itself “joint-only” in its header, but does not
   enforce that neither single edit installs `B`.  It searches a superset of
   the genuine joint branch.  This creates overlap, not a false exclusion.
4. `missing_private` is truncated after 16 entries without an explicit JSON
   truncation flag.  This affects only diagnostics; zero/nonzero testing uses
   the full private set.
5. A zero result triggers an independent physical replay, but an UNSAT result
   has no DRAT-like certificate.  The theorem is an authenticated exhaustive
   program theorem plus the source proof above, not a proof-log theorem.

Future runs should write a manifest containing the word/source/audit hashes,
all invocation arguments, and the independently expected full support/row
counts.

## 6. Smallest natural complete exact model

The smallest faithful model is the disjoint logical union below, not an
82,863,501-support unrestricted pair scan.

1. **Sequential table.**  Use the 27,064 exact first-provider rows.  For each
   row and each distinct second position, intersect the per-debt service-value
   tables, then impose the exact second-position private-target constraints.
2. **Joint table.**  Use only the 13,235 supports characterized above.  Each
   support has two eight-bit nonzero submask variables `u,v`, endpoint-change
   inequalities, equation (2.1), and one table clause (2.2) per private
   target.

This model is complete for arbitrary radius two and retains literal interval
chronology.  The existing exact catalogues solve both branches negatively.
The surviving nearest state is the joint best1 with hole `0xa86d`; its next
meaningful gate is a one-substitution return from that materialized word, not
another radius-two rescan of `W`.

## 7. Materialized best1 and exact return

An independent finite auditor verifies all saved extremal rows, derives the
13,235-support gap histogram and the 102,404,745 replacement-pair count from
(4.2), and materializes the closest state:

```
scratch/audit_r_k16_upper12874_delete_radius2_normal_form_20260730.py
SHA-256 c2e75457320d7e0ddedb251c0f995462de69d3fb72ad8872501709f8e9337a53

scratch/r_k16_upper12874_delete_radius2_normal_form_20260730.audit.json
SHA-256 6ac56bab32034e179c26a0c3f3b82607c5d33abe94b402ad5e528feeefa8e6d0
payload 76cff97a63e396d2884497532a74edaf187422352c1bd13dcc986c479a49aee4

scratch/k16_upper12874_delete_radius2_best1_43117.word
SHA-256 09a60d48584a737f452a5d53c8fadec9b26cdad354f36926fbc5b1b1ceb4d166
```

The materialized word has sole hole `43117=0xa86d` under a fresh suffix-state
replay.

The complete one-substitution return from this word was then run on one H100
CPU under a 1 GiB address-space cap.  Every arbitrary nonzero replacement
which creates `0xa86d` was enumerated: there are 27,902 such assignments, at
all 12,873 positions.  None completes the word.  The collateral floor is one,
attained by exactly eight values at position 6440:

\[
 \{\mathtt{0x8041}\vee s:s\subseteq\mathtt{0x002c}\}.
\]

Every one of these rows loses exactly `11373=0x2c6d`.  Thus this closest
radius-two branch forms the exact local latch

\[
  \mathtt{0x2c6d}\longrightarrow\mathtt{0xa86d}
  \longrightarrow\mathtt{0x2c6d},
\]

not an absorber.  This closes only the one-edit continuation of this best1
state; it is not a complete radius-three obstruction from `W`.

Primary and independent return artifacts:

```
scratch/best1_return.audit.json
SHA-256 e929b73fb7f56a4df01e1b7f8cd2b4f22ea68bd6677f7e89f7fcb375afdd6b48

scratch/audit_r_k16_upper12874_delete_radius2_best1_return_20260730.py
SHA-256 3e67475741f18befb8af09d577e7116d780612cf593ade181b37cdc1307b205d

scratch/r_k16_upper12874_delete_radius2_best1_return_20260730.audit.json
SHA-256 f5540f050a565f6bba5dd5cc3570a0156f176834496ea71587fad8987409b85b
payload eb9d7bea3e237ac34799391331463d006c4547d7a9491e007d1eb82c098c7ab9
```

The global conclusion remains sharply scoped: the current exact bracket is
`12873 <= nu(16) <= 12874`, and this report excludes only substitution radius
at most two around the unique best deletion of the frozen 12,874-word (plus
the named best1 continuation just audited).

“Smallest” here means after the exact provider/private-target reductions just
proved: it is not a lower bound on the extension complexity of every possible
SAT or integer-programming encoding.
