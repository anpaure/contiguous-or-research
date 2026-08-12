# Exact radius-one exclusion for the C106 SSSSS basis and the radius-two annealer gate

Date: 2026-07-30  
Lane: AD, exact circulation/basis audit  
Status: **radius zero and radius one are proved impossible in the frozen SSSSS model**

This note is separate from the canonical floor-106 theorem.  It does not edit
or replace that theorem.

## 1. Frozen scope

The frozen inputs are:

- seam ledger `scratch/k16_len8_source_seam_ledger_20260730.bin`, SHA-256
  `832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657`;
- target prices and endpoint potential
  `scratch/k16_direct_cycle_dual_exact_20260730.audit.json`, SHA-256
  `29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d`;
- exact SSSSS basis
  `scratch/k16_floor106_s5_capacity_exact_20260730.audit.json`, SHA-256
  `7f9780503ca106052044dc0b13604666509602e80f9bf7df6b091bbaa62c806e`;
- parity escape bank
  `scratch/ad_k16_c106_sssss_parity_escape_bank_20260730.tsv`, SHA-256
  `cb021f38ab5e423804bcb8bb885aa20026f34ef59eb93b0500dd716cfc573600`.

Let \(S\) be the 662-seam positive support of the exact SSSSS fractional
point.  A **SSSSS selection** in this note is a binary seam vector \(x\)
satisfying

\[
 Bx=0,\qquad
 \sum_{e\in\delta^+(v)}x_e\le1,\qquad
 \sum_{e:t\in H(e)}x_e=1\quad(t\in\mathcal T),
 \qquad \sum_es_ex_e=5,                                      \tag{1.1}
\]

where \(|\mathcal T|=93\), the target-price total is 207, and \(s_e\) is
the frozen nonnegative direct-dual slack.  Balance and the direct accounting
identity imply

\[
 2\sum_ex_e=207+5=212,
\]

so every vector in (1.1) has selected mass 106.  Define its support radius by

\[
 z_S(x)=\sum_{e\notin S}x_e.                                \tag{1.2}
\]

No separation, q1, reverse-edge, residence, survivor, deeper-shadow,
connectivity, carrier, or compiler row is imposed.  Consequently every
no-go below remains valid after any of those rows are added, but no positive
carrier or word claim follows.

## 2. Why exactly 298 seams exhaust radius one

The support graph has 571 vertices, three weak (and directed) components,
and circulation dimension

\[
 662-571+3=94.                                               \tag{2.1}
\]

The frozen mod-two support certificate gives a parity label \(\rho_e\) such
that \(\rho_e=0\) for every \(e\in S\), while every SSSSS selection obeys

\[
 \sum_{e\notin S}\rho_ex_e=1\pmod2.                         \tag{2.2}
\]

Suppose \(z_S(x)=1\), and call the unique outside seam \(h\).  Then:

1. (2.2) forces \(\rho_h=1\);
2. nonnegative total slack five forces \(s_h\le5\);
3. summing endpoint balance over each support component forces both endpoints
   of \(h\) to lie in the same support component.

The raw-ledger audit enumerates exactly 298 seams satisfying these three
conditions.  Hence a proof for those 298 cases is a complete radius-one proof,
not a heuristic neighbourhood scan.

## 3. One 94-by-94 system with 298 exact right-hand sides

The deterministic positive-flow decomposition of \(S\) gives 94 independent
directed cycles \(C_1,\ldots,C_{94}\).  Since their number equals (2.1), they
form a real basis of the support circulation space.

For a radius-one candidate \(h=(u,v)\), take the deterministic breadth-first
directed support path \(P_h\) from \(v\) back to \(u\).  Put

\[
 y_h={\bf1}_{\{h\}}+{\bf1}_{P_h}.                           \tag{3.1}
\]

### Lemma 3.1 (complete affine parametrization)

Every real endpoint-balanced vector supported on \(S\cup\{h\}\) with
coordinate \(x_h=1\) has a unique representation

\[
 x=y_h+\sum_{j=1}^{94}\lambda_jC_j.                         \tag{3.2}
\]

#### Proof

The vector \(y_h\) is balanced.  Thus \(x-y_h\) is a circulation supported
on \(S\), so it lies in the span of the \(C_j\).  Their independence gives
uniqueness.  \(\square\)

Let \(A\in\mathbb Z^{94\times94}\) have, in column \(j\), the 93 target
service counts and the slack of \(C_j\).  For candidate \(h\), let \(b_h\)
be the required all-one service vector and slack five after subtracting the
base flow (3.1).  The exact candidate system is

\[
 A\lambda=b_h.                                               \tag{3.3}
\]

The independently replayed ranks of \(A\) modulo
\(1000000007,1000000009,998244353\) are all 94.  Therefore (3.3) has one
exact rational solution for every \(h\).  Solving all 298 columns in one
fraction-free multi-right-hand-side call gives the common denominator

\[
 D=14905561300695363968281280.                              \tag{3.4}
\]

The candidate return paths have lengths from 1 through 66.  Their complete
path bank, right-hand-side matrix, and numerator matrix are frozen by hashes
in the audit artifact.

### Theorem 3.2 (exact 298-case radius-one no-go)

For every one of the 298 candidates \(h\), the unique vector (3.2) satisfying
all 93 service equations and slack five is nonbinary.  In fact:

- all 662 support coordinates are fractional in all 298 cases;
- every case has a negative support coordinate;
- 288 cases also have a coordinate above one and a capacity violation;
- the fixed support seam 2739 is nonbinary in every case, taking 283 distinct
  exact rational values across the bank.

Consequently no binary radius-one SSSSS selection exists.

#### Proof

Full rank makes (3.2)--(3.3) the unique equality flow for each fixed \(h\).
The exact multi-RHS replay reconstructs it and checks balance, all 93 services,
count 106, slack five, nonnegativity, binarity, and port load.  For each
candidate, the value of seam 2739 is neither zero nor one.  Any binary solution
would be the unique equality flow and would therefore have that same
nonbinary coordinate, a contradiction.  \(\square\)

The exactifier is
`scratch/exactify_ad_k16_c106_sssss_radius1_mrhs_20260730.py`, SHA-256
`a3bb5ddb2a8b1e20edba6525f5b82a43c61300b8068c05bc7c1145f8b22683b2`.
Its artifact is
`scratch/ad_k16_c106_sssss_radius1_exact_mrhs_20260730.audit.json`, SHA-256
`a3eb54464e670f69d50eaf9cab46cd2ae2d055beb8ab11568331b5e70531e668`,
payload SHA-256
`8bfb2b21a77666cc906aa1cf7729b70e18bf97ef17ee7c1609f24a0435505a1a`.
It used one H100 CPU, 63,352 KiB maximum RSS, and 2.45 seconds wall time.

## 4. Independent raw-ledger replay

The independent checker does not import the exactifier and invokes no solver.
Starting from the raw seam ledger, it:

1. reconstructs all 662 support and 298 outside physical arc records;
2. checks all 94 directed cycles and independently rebuilds \(A\);
3. reconstructs every deterministic return path;
4. verifies all \(94\times298\) integer equalities
   \(AN=D B\);
5. reconstructs every full rational physical flow and replays balance, all 93
   service rows, count 106, and slack five;
6. independently evaluates the frozen seam-2739 witness in every column and
   checks that it is never zero or one.

The checker
`scratch/audit_ad_k16_c106_sssss_radius1_mrhs_raw_20260730.py` has SHA-256
`7b7f57a74dc971dae77aaac23fc35b7dce119b4e8a4066636b2b9ea2a54f44e1`.
The PASS artifact
`scratch/ad_k16_c106_sssss_radius1_exact_mrhs_raw_audit_20260730.audit.json`
has SHA-256
`8de779255bc83e2a4a21601fc88a0e9c50840888e27f4749d7e34a7e6ff858c4`
and payload SHA-256
`f1df0bb3f8e573cf9bc1e212d5407e1f4777df85adc5f6de9eb8eeae34cccbdc`.

## 5. A smaller mathematical obstruction: one mod-457 row

The 94 signed fundamental support cycles give an integral basis of the
support circulation lattice.  Their 93-service-plus-count feature matrix
\(M\) has

\[
 \det M=-7452780650347681984140640
 =-2^5\cdot5\cdot457\cdot63079\cdot33852407\cdot47731799.    \tag{5.1}
\]

Modulo 457, \(M\) has rank 93.  Let
\(a=(a_t:t\in\mathcal T;a_0)\) be its left null row normalized so that its
dot product with \((1^{93};106)\) is one.  Here \(a_0=241\).  Lifting the
support edge label to a vertex potential \(p\), define

\[
 R(e)=241+\sum_{t\in H(e)}a_t+p(u(e))-p(v(e))\pmod{457}.      \tag{5.2}
\]

Every support edge has \(R(e)=0\).  Endpoint balance, exact service, and
count 106 give the global equation

\[
 \sum_{e\notin S}R(e)x_e=1\pmod{457}.                       \tag{5.3}
\]

None of the 298 radius-one seams has residue one.  Thus radius one is
impossible even for signed integral circulations, without nonnegativity,
Boolean bounds, or capacity.

The corrected fail-closed certificate is
`scratch/ad_k16_c106_sssss_radius1_mod457_separator_v2_20260730.audit.json`,
SHA-256
`e2fa6fa2fe42152566af9a771b029af3b1977f1b61e62dfe58527b500ed35aff`,
payload SHA-256
`5c53ab031a84b0061582d5c50cf01a1c79ebd97d6d8418a33a81631fad36cc4c`.
Its checker has SHA-256
`d75430205f7941be821dd63d54cf94f5c961662ab175f3f7d8b12356b124e0e1`.
The full proof is in
`MATH_AUDIT_AD_K16_C106_SSSSS_RADIUS1_MOD457_LATTICE_SEPARATOR_20260730.md`,
SHA-256
`298e788556e31622e6cd36a29a45333d0496b07b5149468c675f1c4e75a6ee71`.

**Provenance warning.**  The earlier unsuffixed mod-457 JSON with SHA prefix
`b255ab9c` is superseded: a presentation-loop variable shadowed its serialized
`modulus` field.  Only the fail-closed `v2` artifact above is valid for
citation.

### Corollary 5.1 (global support-radius cut)

Every binary SSSSS selection satisfies

\[
 \boxed{z_S(x)\ge2}.                                        \tag{5.4}
\]

Radius zero is excluded by either the support parity contradiction or (5.3),
and radius one is excluded by Theorem 3.2 or the mod-457 replay.

## 6. Independent proof-producing CNF

For a second proof route, primary variables 1 through 662 are the support
seams and variables 663 through 960 are the sorted 298 outside candidates.
The CNF encodes:

- incoming and outgoing capacity one and equality through one activity bit per
  active port;
- exactly one provider for each of the 93 targets;
- exact total slack five;
- exactly one selected outside variable.

Count 106 is derived as in Section 1.  The deterministic formula has

\[
 7344\text{ variables},\qquad 22390\text{ clauses}.          \tag{6.1}
\]

Its SHA-256 is
`9edb848f63f29b65afe197709f143af83cfb507fa8983f67804722241fa484c5`;
its manifest SHA-256 is
`0eb45bb4a6721d44d7b99d8268923e4991e9ba4ac9c0c01035b8e30c7eabf2e0`.
The exact source that emitted this formula is frozen separately as
`scratch/emit_ad_k16_c106_sssss_radius1_cnf_frozen_b61e54db_20260730.py`,
SHA-256
`b61e54db78b5d61025b5bf7847e7bdca05871dce0a3d502a07caca2170919581`.

Kissat emitted a DRAT proof with SHA-256
`5795bf17883aba3e68c806e5dc7c27587c6da9a7615f8567f928aec9a5deace0`.
`drat-trim` verified it, reduced the source to 20 clauses, and emitted the
LRAT proof
`scratch/ad_k16_c106_sssss_radius1_662plus298.core.lrat`, SHA-256
`6e2479881d0aae168d37ffd78389329b34bc17aedaaf7018852cb9fe2f6c0383`.
`lrat-check` independently returned `VERIFIED` against the original
7344-variable, 22390-clause CNF.  The 20-clause core mentions only six primary
seams:

\[
 66749,\ 131841,\ 138199,\ 161195,\ 177012,\ 207270.         \tag{6.2}
\]

The independent bundle checker replays all 960 physical arc records from the
raw ledger, authenticates the primary map and every source-row census, parses
the full CNF, and pins the checked proof transcripts.  Its artifact
`scratch/ad_k16_c106_sssss_radius1_662plus298.proof_bundle.audit.json`
has SHA-256
`4659f05da19ee64321a4e05bf70354e05c20f7560ff756da1337d8b5ddf8ad09`
and payload SHA-256
`50cc073ae9ae657fb8351b08535d5f6129c2eb4c37557068fe6c60e5c0763b3b`.
The checker has SHA-256
`d5691295b6c8cfd9ecb98286b1d44a3d9a3abefa3497de6a3ddcadc192e40e96`.

Thus the exact-rational, modular, and checked-LRAT routes independently agree
on radius-one infeasibility.

## 7. Exact CRT pricing for the next annealer radius

Let \(\rho(e)\in\mathbb Z/2\mathbb Z\) be the parity escape label and let
\(R(e)\in\mathbb Z/457\mathbb Z\) be (5.2).  Since 2 and 457 are coprime,
define the unique combined price \(q(e)\in\mathbb Z/914\mathbb Z\) by

\[
 q(e)\equiv\rho(e)\pmod2,\qquad q(e)\equiv R(e)\pmod{457}.   \tag{7.1}
\]

With representatives \(0\le R(e)<457\), this is explicitly

\[
 q(e)=
 \begin{cases}
 R(e),&R(e)\equiv\rho(e)\pmod2,\\
 R(e)+457,&R(e)\not\equiv\rho(e)\pmod2.
 \end{cases}                                                \tag{7.2}
\]

Every support seam has \(q(e)=0\), and every SSSSS selection obeys the one-row
cycle-pricing equation

\[
 \boxed{\sum_{e\notin S}q(e)x_e=1\pmod{914}.}               \tag{7.3}
\]

This single congruence simultaneously enforces the parity and mod-457 locks.

Contract each of the three support components to one quotient vertex and
leave every port outside the support as a singleton quotient vertex.  For an
outside seam \(e\), write \(\bar e\) for its quotient arc.

### Theorem 7.1 (exact radius-two topology and arithmetic filter)

If a binary SSSSS selection has \(z_S(x)=2\), with outside seams \(a,b\),
then all of the following hold:

1. \(\{\bar a,\bar b\}\) is Eulerian in the contracted quotient;
2. equivalently, either both quotient arcs are loops on support components,
   or they form a directed quotient two-cycle \(U\to V\to U\);
3. \(q(a)+q(b)\equiv1\pmod{914}\), so \(\rho(a)\ne\rho(b)\);
4. \(s_a+s_b\le5\);
5. \(a,b\) have distinct raw tails and distinct raw heads;
6. \(H(a)\cap H(b)=\varnothing\).

#### Proof

Summing endpoint balance over each quotient vertex makes the selected outside
multidigraph Eulerian, because every support arc contracts to a loop.  A
two-arc Eulerian directed multigraph consists either of two loops or of two
oppositely directed nonloops.  The frozen seam ledger has no raw self-loops,
so a quotient loop outside \(S\) has both endpoints in one support component.
Equation (7.3) gives item 3.  Nonnegative total slack five gives item 4.
Outgoing and incoming capacity one give item 5.  Exact-once target service and
nonnegativity give item 6.  \(\square\)

These conditions are **necessary, not sufficient**: after they hold, the
support coordinates must still solve the service/balance system within
\(\{0,1\}\), and all omitted physical rows remain to be checked.  They are,
however, an exact first-stage annealer filter.  No scalar search radius below
two need be considered.

The compact pricing catalogue
`scratch/ad_k16_c106_sssss_crt914_outside_slack5_v2_20260730.tsv` has SHA-256
`da46d259648bf01db3b678cfafca857a49cac79c47f05e5abb3de90b457bb69e`.
It contains 210,763 outside seams of slack at most five, one seam per row, with
columns

```text
seam_id  slack  q  tail_port  head_port  tail_class  head_class  topology
```

and is deliberately not a raw pair dump.  There are 645 quotient-loop seams
and 210,118 quotient-arc seams.  Exact bucket counting followed by an
independent explicit replay leaves only

\[
 \boxed{208=204+4}                                           \tag{7.4}
\]

unordered structural pairs: 204 loop--loop pairs and four directed quotient
two-cycles.  All 208 also satisfy the target-disjointness condition in item 6;
none is removed by that additional exact-service filter.  The canonical
unordered pair set is stored only by SHA-256
`55d24bcc086ceea1941759958cbac79b8212a272e7ee2a34f1cf51b67cd696a7`.

The interface manifest
`scratch/ad_k16_c106_sssss_crt914_radius2_v2_20260730.audit.json` has SHA-256
`9dce75365e9ce98cd16f8096ea206803e8f83326919cc7b4e01e41ebcc62f4ff`
and payload SHA-256
`adb22c4a988aa28b21545a5fed645ebe7ea43a740878dffa46e14820d3f417b1`.
The independent pair replay has SHA-256
`bd33a7a86c27aa45cbc6d9178165e90b065fb633309fa75478a8707820a3c26c`.
The separate raw-ledger service-disjoint audit
`scratch/ad_k16_c106_sssss_crt914_radius2_service_disjoint_20260730.audit.json`
has SHA-256
`d74a1cf145dcf6660772055931f80dff0ede34138e9fe185ff8822f0064c20e0`
and payload SHA-256
`42bc348d70fcdc4260ea43788d8edcb08718fcada615d1686398bc132910e8f4`.
The full CRT theorem note is
`MATH_THEOREM_AD_K16_C106_SSSSS_CRT914_RADIUS2_ANNEALER_INTERFACE_20260730.md`,
SHA-256
`ceb4afc6da6d48d919f2fbde3884cea088cea58a3120447d3934afdc5fc6770a`.

## 8. Precise proved boundary

Proved:

1. every possible one-column expansion is among the exact 298-row bank;
2. the 298 affine equality flows are exactly solved and all are nonbinary;
3. an independent raw checker replays every path, RHS, and decisive witness;
4. one mod-457 circulation row rejects all 298 even over signed integers;
5. a separately checked LRAT proof refutes the exact radius-one binary CNF;
6. every SSSSS binary selection has support radius at least two;
7. equations (7.1)--(7.3) and Theorem 7.1 give the exact first-stage
   arithmetic/topological filter for radius two.

Not proved:

1. existence or nonexistence at radius two or any larger radius;
2. feasibility of any of the other 1023 C106 five-lock signatures;
3. q1, separation, residence, survivor, reverse-edge, connectivity, carrier,
   compiler, or literal contiguous-OR feasibility at C106;
4. a lower bound above 106.
