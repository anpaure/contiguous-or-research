# K16 H1 radius four: uncapped catalogue decision reduction and the no-installer exclusion

Date: 2026-07-30

Status: exact all-catalogue decision procedure; exact solver-free exclusion of
the disjoint branch in which no two edited sites install the source hole.
The complementary H-installing-pair branch is reduced to the exact stateful
`A(x)+B(y)+C(x OR y)` join and has an authenticated necessary-value census,
but its remaining literal geometry join has not been exhausted here.

## 1. Frozen scope

The rooted source is

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
length 12873; sole hole H=0x2c6d.
```

The finite move catalogue is

```text
scratch/k16_h1_radius4_mitm_catalogue_20260730.tsv
SHA-256 19a48659bdd50abf0a17d3baa3755b79fa88ab7c69a1361dd39a51eb9cd2d4a0
7,099 nonzero genuine replacements on 288 physical positions;
479 distinct replacement values.
```

Every assertion below concerns four **distinct** positions and one catalogue
replacement at each.  There is no intermediate-hole cap.  The old 775,506
repair bank and its source-positive-gain condition are not used as a universe.
This is not an arbitrary-value or arbitrary-position radius-four theorem.

The number of literal exact-four catalogue words is the fourth elementary
symmetric sum of the 288 position-domain sizes:

```text
85,816,527,647,778.
```

## 2. Uniform canonical spatial decision

Sort a final four-edit support as

\[
                         a<b<r<s
\]

and canonically put `P={a,b}`, `R={r,s}`.  This definition does not require
`P` to install `H`.  Set `u=w^P`, and let `D(P)` be every nonzero target absent
from `u`; in particular, `H` belongs to `D(P)` when `P` does not install it.

For proposed values `x,y` at `r,s`, partition every interval changed after
`u` into the three exact classes

```text
meets r but not s;   meets s but not r;   meets both r and s.
```

Their signed multiplicity columns depend respectively only on `x`, `y`, and
`x OR y`.  Therefore, on all 65,536 labels,

\[
 M(u^{r\leftarrow x,s\leftarrow y})-M(u)
   =A_r^P(x)+B_s^P(y)+C_{rs}^P(x\lor y).                 \tag{2.1}
\]

Equation (2.1) is the stateful form of the six endpoint-order rectangle
identity proved in the preceding cross-interaction theorem.  It covers the
separated, nested and alternating words without a full-gap assumption.

For an absent target `T`, maximal compatible collars give exact Boolean
witness sets `A_T(x),B_T(y),C_T(x OR y)`.  Thus restoration of every current
debt is exactly

\[
                 A(x)\cup B(y)\cup C(x\lor y)=D(P).      \tag{2.2}
\]

After (2.2), the exact ten-class `four_delta` test is still mandatory.  Debt
cover alone does not protect a previously covered label whose last witness is
destroyed by the repair.  A positive Pareto/SOS query must likewise expand
every qualifying literal action before exact replay; replaying only a profile
dominator is incomplete.

### Theorem 2.1 (canonical completeness)

Enumerating every canonical left pair `P={a,b}`, every right position pair
`r<s`, every literal catalogue value, and applying (2.1)--(2.2) followed by
exact replay decides all 85,816,527,647,778 exact-four catalogue words exactly
once.

#### Proof

Every four-position support has a unique two-leftmost/two-rightmost split.
The interval classes in (2.1) partition all changes from `u`, including every
cross-pair interval.  Every missing label must acquire one of those three
witness forms, proving necessity of (2.2), and their maximal collars prove
sufficiency for the current debts.  The final all-label multiplicity check is
equivalent to universality.  No other word or split is omitted.  QED.

This canonical procedure is the smallest mathematical specification.  The
following disjoint H-witness partition is the smaller implementation.

## 3. Disjoint practical partition

For a subset `Q` of final edits, write `I(Q)=1` when applying `Q` alone to the
source installs `H`.

1. **Installer branch.** Some two-subset `Q` has `I(Q)=1`.  Choose the
   lexicographically first such pair as portal `P`, and join the other two
   literal actions with (2.1).
2. **Triple-plus-one branch.** No pair installs `H`, but some three-subset
   does.  Choose the first such triple and invert its fourth cell exactly.
3. **Direct-four branch.** No pair or triple installs `H`.  Every final
   `H`-witness meets all four edits; enumerate its literal four-site packet and
   invert one cell.

This is complete.  If a final `H` witness meets at most two edits, its edited
intersection itself gives an installing two-subset; in the one-edit case, add
any second final edit outside the witness interval.  With no installing pair,
the witness therefore meets three or four edits.  In the three-edit case the
fourth edit is outside that witness and deleting it leaves an installing
triple.  Otherwise all four edits lie on the witness.

A useful locality consequence is immediate.  For sorted support `a<b<r<s`,
every no-pair final `H` witness crosses the fixed central gap, so

\[
             \operatorname{OR}_w(b+1,\ldots,r-1)\subseteq H. \tag{3.1}
\]

Thus the no-installer complement is intrinsically an H-compatible packet
problem.  A fixed `0xffff` central gap makes this branch impossible.

## 4. The uncapped pair census and the safe value cut

An exact uncapped pass over every distinct-position catalogue pair gives

```text
all pair actions                                      24,348,717
single actions installing H                                  619
pair states installing H                               3,997,398
  installing and containing a singleton installer      3,995,624
  genuinely pair-only installers                           1,774
```

No pair state is universal.  All pair states have between one and 29 holes;
the H-installing portals have between one and 28.  This removes the old
cap-eight portal restriction at the census level.

The installer branch must admit **all 24,348,717** pairs as possible repairs.
It cannot use the old 775,506 repair bank, because a source-negative marginal
column can be positive after portal cross-interaction.

There is, however, a safe position-free value cut.  Fix an H-installing portal
and one of its debts `T`.  Every final `T` witness meets repair site `r` or
`s`; every edited value which it meets is a submask of `T`.  Hence necessarily

\[
                         x\subseteq T\quad\hbox{or}\quad y\subseteq T. \tag{4.1}
\]

For fixed `x`, put

\[
                  U_x=\bigcap_{T\in D(P):\ x\not\subseteq T}T.        \tag{4.2}
\]

Condition (4.1) on every debt is equivalent to `y subseteq U_x`.  A 16-bit
subset-SOS over the 479 distinct catalogue values therefore decides whether
the positionless value domain is empty.  Zero is a sound portal rejection;
positive is only an overapproximation because positions, order type,
collateral and literal action availability are not yet enforced.

The authenticated census reports

```text
unique portal debt sets                                  81,228
value-incompatible debt sets                              1,362
value-compatible debt sets                               79,866
value-incompatible H portals                            158,090
value-compatible H portals                            3,839,308
weighted median ordered unique-value pairs                2,521
weighted sum of ordered unique-value pairs        16,974,616,970
maximum for one debt set                                147,072
```

The weighted sum counts positionless value pairs, not literal repair actions.
The remaining 3,839,308 portals still require the position-specific
`A+B+C` join and exact replay.  This turn did not duplicate the separately
coordinated broad pair/pair job, so these positive rows are not claimed
negative.

## 5. Exact H-packet catalogue

Among the 7,099 catalogue moves, exactly 1,436 values on 269 positions are
submasks of `H`.  A literal H packet is obtained by choosing its edited-site
intersection and forcing every fixed interior source cell to be an H-submask.
The maximal H-compatible outer collar then makes the final witness condition
one OR equality.

The exact structural census is

| packet | live supports | raw value assignments |
|---|---:|---:|
| three sites | 58 | 1,330,507 |
| four sites | 35 | 50,466,281 |

These are raw witness packets, not completion counts.  Exact subset-installer
tests sharpen them as follows:

```text
three-site packets with no installing pair                16,420
  live supports after that filter                              7

four-site packets with no installing pair                660,764
  with at least one installing triple                    502,760
  with no installing pair and no installing triple       158,004
  supports carrying the direct 158,004 rows                    3
```

The direct rows are concentrated as

```text
sites [6434,6435,6436,6437]      157,968
sites [4497,4498,4499,4500]           18
sites [4498,4499,4500,4501]           18.
```

The 502,760 count is only the all-four-witness overlap with triple-plus-one.
The complete triple-plus-one branch starts from all 16,420 primitive triples
and queries every distinct fourth catalogue action; that action need not lie
on an all-four H witness.

The primitive producer validates its fast H-component predicate against a
literal modified-word component walk on 159,249 triple-pair truth rows,
286,983 four-pair truth rows and 6,982,205 four-triple truth rows.  A separate
Python literal replay reproduces all 1,330,507 triple assignments and the
16,420 primitive survivors; an independent clang build reproduces the full
JSON byte-for-byte.

## 6. Exact last-cell inverse

Let `u` be a three-edit prefix and `q` a prospective fourth position.  Let
`D(u)` be the exact holes of `u`.  For `T in D(u)`, remove the incumbent at
`q` and let `c_q^u(T)` be the OR of the maximal fixed T-compatible collar
about `q`.  Define

\[
 L_q(u)=\bigvee_{T\in D(u)}(T\setminus c_q^u(T)),\qquad
 U_q(u)=\bigcap_{T\in D(u)}T.                             \tag{6.1}
\]

### Lemma 6.1 (last-cell inverse)

A nonzero genuine value `z` restores every current hole through `q` exactly
when

\[
                         L_q(u)\subseteq z\subseteq U_q(u).             \tag{6.2}
\]

#### Proof

Since `T` is absent from `u`, every final T witness must meet `q`.  Such an
interval cannot contain a bit outside `T`, so `z subseteq T`.  Enlarging its
fixed part to the maximal compatible collar loses no bit; a witness exists
exactly when `c_q^u(T) OR z=T`, equivalently
`T minus c_q^u(T) subseteq z subseteq T`.  Intersect these Boolean intervals
over all holes.  QED.

The final `four_delta` check remains necessary in general to protect covered
labels.  In the present negative census no literal value survives (6.2), so
no final replay is reached.

For the direct-four branch, choose a largest H-submask domain as the inverse
site.  This reduces 50,466,281 raw assignments to exactly 1,554,083
three-value prefixes before any interval query.

## 7. Exact no-installer disposition

Two independently written C++ engines implement the packet partition and
last-cell inverse.

### Triple-plus-one

```text
raw installing triples                                  1,330,507
triples with no installing pair                            16,420
intermediate universal triples                                  0
common upper U_q empty before positions                    11,068
candidate fourth positions after exact collars                  0
literal fourth values                                           0
```

The remaining 5,352 triples have nonzero common target intersection but no
position-specific catalogue value in an exact last-cell interval.

### Direct four

```text
largest-domain three-value prefixes                     1,554,083
prefixes with no internal installing pair                 111,024
prefixes already installing H by the triple                11,848
genuinely direct prefixes                                  99,176
empty exact inverse intervals                              99,176
literal inverse values                                          0
```

The primary implementation refines the last line: 63,287 direct prefixes
already have zero common upper bound, and all remaining prefixes fail their
lower/position-domain query.  The independent implementation obtains the
same zero by a separately organized submask/value posting enumeration.

### Corollary 7.1 (no-two-installer catalogue no-go)

No exact four-distinct-site word from the 7,099-move catalogue is universal
if none of its six two-subsets installs `H` in isolation.

#### Proof

By Section 3, every such completion belongs to triple-plus-one or direct
four.  Sections 5--7 exhaust both exact packet families and find no legal
fourth literal value.  QED.

This also incorporates the earlier rooted radius-three frontier correctly.
The exact all-three-H-witness and two-site-plus-one theorems already exclude
support-three completion; the 144,191,783 one-site-portal/joint-pair theorem
strictly contains the independently checked 1,341-support nested-portal
no-go.  The new census is nevertheless self-contained at radius four: its
`triple_zero_holes=0` is recomputed with no intermediate cap, and an arbitrary
fourth action is admitted after every primitive triple.

## 8. Independent audits and resources

The primary no-installer decision ran on one H100 CPU, core 27, under

```text
/home/amodo/or15/work/laneL_k16_h1_no_pair_packet_decision_20260730_559eba12
```

with a one-GiB address cap, no swap and no `/dev/shm` write.  It used 0.52
seconds wall time and 58,368 KiB maximum RSS.  The independent engine ran on
core 63 under a different `/home` directory, used 0.35 seconds and 10,752 KiB
RSS, and returned the same scoped no-go.  Exit code one is the documented
no-witness return of both engines.

The uncapped pair histogram used one H100 CPU for 3:45.09 and 8,192 KiB RSS.
The necessary value census used one CPU for 6:19.61 and 19,968 KiB RSS.  Both
used unique `/home` directories, explicit caps and no swap.

Key retained artifacts are:

```text
scratch/audit_k16_h1_radius4_all_pair_portal_histogram_20260730.cpp
  SHA cca0bc3deb52dac300316d284769ec5a2d6f3af071e5c947b0317b165edc8280
scratch/k16_h1_radius4_all_pair_portal_histogram_20260730.audit.json
  SHA 3a70f6bb83b244855cc0bcbe29d019df6cdb2fcf6f27f86d9bc7574375198dc8
scratch/k16_h1_radius4_all_pair_portal_histogram_independent_20260730.audit.json
  SHA bf41e47b526ddf9626db15fb299594e220e1e8d14c04a6dce1a739820cbf740d

scratch/audit_k16_h1_radius4_hportal_debt_value_compatibility_20260730.cpp
  SHA 615bcd9a8770d90f82fd76291633f3d05c76357caa35cbee2092a2145c72526b
scratch/k16_h1_radius4_hportal_debt_value_compatibility_20260730.audit.json
  SHA 407a9744b16a81de9234bd1eb50feb4dd757b8c0fa945e3191c0fb89c61f8fad
scratch/k16_h1_radius4_hportal_debt_value_compatibility_independent_20260730.audit.json
  SHA e7c57b85a7212dc7cff587bafedbcd2f50f986e0b715ae698350be0b21c617e9

scratch/census_k16_h1_radius4_primitive_h_packets_20260730.cpp
  SHA ce4f5a36864cb86b290cdde5334cfb596def372e5a8b70dfbfb4b21fd773b820
scratch/k16_h1_radius4_primitive_h_packets_20260730.audit.json
  SHA 54752dea4787e6f29639b9fac1399d16bf86dabe63865db521f06d545e4edc8c
scratch/l_k16_h1_radius4_primitive_h_packets_independent_20260730.audit.json
  SHA bfb9cd3c94469189151b1b36a98db5d54fd971e4937ecb591cf5e85e3c59ca83

scratch/search_l_k16_h1_radius4_no_pair_packet_decision_20260730.cpp
  SHA 559eba124662d1e5bfc935f7f7cb93e3b493e2d44eb1f770707bbe60e0129a4e
scratch/k16_h1_radius4_no_pair_packet_decision_20260730.audit.json
  SHA 3b90c50f5c2536d3e2eaf4c124a5cfbc0fc997e5f0385bcce75f4367826cef6e
scratch/decide_k16_h1_radius4_no_pair_h_installer_lastcell_20260730.cpp
  SHA 5792506bd6efb734d1d37d4154f74dc19d82e8275b4cef0332d4bab30880a940
scratch/k16_h1_radius4_no_pair_packet_decision_independent_20260730.audit.json
  SHA 87c46b87ebf39e47fee209e54c49eb36c2b134d518d3833ad715318635800c0c
scratch/l_k16_h1_radius4_no_pair_packet_decision_independent_20260730.audit.json
  SHA 4bde7966b8219cdf2afc7d3b479629b6b42579ce4e12cd5d87788afd28bbdf16
  payload 5977ff149b245d8a30f2b5592a1192dbe138721cfc7c710f9be7802199b3fc64

scratch/test_k16_h1_radius4_no_pair_h_installer_lastcell_20260730.cpp
  SHA 894334714f0123f4c10d508685a99a2ee7f177bb689abf0ed9a90c1885944dd5
scratch/k16_h1_radius4_no_pair_lastcell_selftest_20260730.audit.json
  SHA bafc87e8954384aa3ae8851ec2d8ebf6d5dd7e06ba0ca3e0e9a613846c39adad
```

The light self-test independently checks 20,000 pair-H component predicates,
120 triple deltas against full recounts and 3,063 last-cell target clauses.
The final cross-auditor authenticates both decision sources/results, the
primitive census, resources and all counter identities.

## 9. Exact frontier

The old repair-bank restriction is gone from the theorem and census.  The
complete catalogue radius-four decision now has only one unresolved disjoint
branch:

```text
some pair installs H;
portal is one of 3,997,398 uncapped H-installing pair states;
repair is any disjoint member of all 24,348,717 catalogue pairs;
3,839,308 portals survive the safe positionless value cut;
apply the literal six-order-type A(x)+B(y)+C(x OR y) join and exact replay.
```

The no-installer branch is closed exactly.  The installer branch is not closed
by the zero-value census and is not silently delegated to the old 775,506
repair bank.  Consequently no full catalogue radius-four no-go, arbitrary-
value rooted no-go, or unrestricted K16 theorem is claimed here.

The global numerical bracket remains

```text
12873 <= nu(16) <= 12874.
```
