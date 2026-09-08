# AD audit: checked radius-one `SSSSS` no-go and exact CRT escape state

Date: 2026-07-30  
Status: proved and independently checked for the frozen source-relative
\(C=106\), `SSSSS` seam catalogue

Radius-two continuation: see
`MATH_AUDIT_AD_K16_C106_SSSSS_RADIUS2_SIGNED_LATTICE_NO_GO_20260730.md`,
which proves that all 208 structurally admissible pairs fail even the signed
support lattice and strengthens the source-relative bound to
\(\sum_{e\notin S}x_e\ge3\).  The boundary statements at the end of this
file record the earlier radius-one checkpoint; the continuation is
authoritative for radius two.

## 1. Scope and antecedent

Let \(S\) be the 662 positive seams in the exact capacity-one `SSSSS`
fractional basis.  The support-only binary face is UNSAT by both a checked
DRAT/LRAT proof and an explicit 33-target mod-two coboundary certificate; see
`MATH_AUDIT_AD_K16_C106_SSSSS_SUPPORT662_CHECKED_UNSAT_20260730.md`.

This note treats the exact radius-one face: select seams from \(S\cup\{h\}\),
where exactly one selected seam \(h\) lies outside \(S\), subject to

\[
\begin{aligned}
 \operatorname{out}_x(v)&=\operatorname{in}_x(v)\le1 &&(v\text{ a port}),\\
 \sum_{e:t\in H(e)}x_e&=1 &&(t\text{ one of the 93 targets}),\\
 \sum_ex_e&=106,\\
 \sum_es_ex_e&=5,\\
 x_e&\in\{0,1\}.
\end{aligned}                                                     \tag{1.1}
\]

As before, the count and slack rows are equivalent under balance and exact
service, because

\[
 \sum_es_ex_e=2\sum_ex_e-207.                                    \tag{1.2}
\]

Separation, reverse-edge, q1, residence, survivor, deeper-shadow, and
connectivity rows are omitted.  Consequently the no-go below applies to every
stronger physical model on this radius-one column set, but it is not a no-go
for the full `SSSSS` branch.

## 2. Why exactly 298 outside columns are exhaustive

The support certificate gives a set \(T\) of 33 targets and a bit potential
\(p^{(2)}\) such that

\[
 \rho_e:=|H(e)\cap T|+p^{(2)}_{\operatorname{tail}(e)}+
                     p^{(2)}_{\operatorname{head}(e)}\pmod2       \tag{2.1}
\]

vanishes on \(S\), while every integral balanced exact-service selection
satisfies

\[
 \sum_e\rho_ex_e\equiv1\pmod2.                                  \tag{2.2}
\]

Thus a sole outside seam must have \(\rho_h=1\).  Since every direct slack is
nonnegative and the total is five, it must also have \(s_h\le5\).  The frozen
ledger has exactly 9,311 seams meeting these two conditions.

The support graph has three components.  Summing endpoint balance over each
component, and separately at every port outside the support vertex set, shows
that the endpoints of a sole outside seam must belong to the same support
component.  A single seam joining different components, touching exactly one
support component, or joining two new distinct ports leaves a nonzero quotient
imbalance.  The physical ledger has no self-loop seams.  Exactly 298 of the
9,311 seams survive this return condition, with slack histogram

\[
\begin{array}{c|rrrrrr}
s_h&0&1&2&3&4&5\\ \hline
\#&49&60&115&42&29&3.
\end{array}                                                       \tag{2.3}
\]

Therefore the `S662 + exactly one of 298` face is precisely the complete
radius-one face, not a heuristic candidate subset.

The authenticated bank is

```text
scratch/ad_k16_c106_sssss_parity_escape_bank_20260730.tsv
SHA-256 cb021f38ab5e423804bcb8bb885aa20026f34ef59eb93b0500dd716cfc573600
```

## 3. Proof-producing exact binary model

The deterministic radius-one formula has 960 primary variables: the 662
support seams followed by the 298 outside seams.  It encodes port balance and
capacity one, the 93 exact-one service rows, exactly one outside primary, and
slack exactly five.  Count 106 is derived by (1.2).  The emitted formula has

\[
 7,344\text{ variables},\qquad22,390\text{ clauses}.             \tag{3.1}
\]

The independent verifier reparses the raw 211,604-seam ledger, recomputes the
entire 9,311-column odd/slack-at-most-five bank and its endpoint classes,
reconstructs the 298-column return bank, rebuilds every CNF clause using a
separate implementation, and matches the emitted clause sequence exactly.

```text
scratch/emit_ad_k16_c106_sssss_radius1_cnf_20260730.py
SHA-256 efd3b639e48abb77341797f088093a33899b7fa428d7ff8ff064ea0adf54ae59

scratch/verify_ad_k16_c106_sssss_radius1_cnf_20260730.py
SHA-256 a107c8dade2c33b3d84f1352e6b5bf47e99e2d2c4ad05d36182f3b3afec8ce82

scratch/ad_c106_sssss_radius1.cnf
SHA-256 8d853bd2532fac6d7662d6e67cc4aa3cfa284f57772f4f519dd8ae7307ab6c06

scratch/ad_c106_sssss_radius1.manifest.json
SHA-256 27ba5ff39f78d6ed7d5e2467df19fab20aca17782d41c240897b9496a261fab5

scratch/ad_c106_sssss_radius1_cnf_source_replay.audit.json
SHA-256 eb73eb1d68b3112c80ca214a275cf43d1f889e01690a59f7898cd83cab02db3f
status PASS_EXACT_CNF_RECONSTRUCTION_AND_FULL_PHYSICAL_BANK_REPLAY
```

Kissat 4.0.4 returned UNSAT.  `drat-trim` checked its DRAT, retained 27 of
22,390 source clauses and 3 of 892 lemmas, used 29 resolution steps and no RAT
lemmas, and emitted an LRAT.  `lrat-check` verified that LRAT against the full
original CNF.

```text
scratch/ad_c106_sssss_radius1.drat
SHA-256 5066dac60660a4a43da3c1902204b94e9915f0e546ee0fe55f3ac8f90764159f

scratch/ad_c106_sssss_radius1.core.cnf
SHA-256 c8dbfaaafb2bcef842bcc5b86c5b7bbe8087ef94c540d64b5ae5b385126f9028

scratch/ad_c106_sssss_radius1.core.lrat
SHA-256 324ed7f00ca2862a6a9511b2c1c90a7dceb5cde0727bf461bd40a9a6ff2b9687

scratch/ad_c106_sssss_radius1.drat-trim.log
SHA-256 69b5ec793bb30989f0cb4cc9f3cb08290f8ae59ff413813a9b7381798a1b93e6
status VERIFIED

scratch/ad_c106_sssss_radius1.lrat-check.log
SHA-256 7839da4e1d0e97144d4fed75ce9cb7f2a08b32be8bc9e6ef86d5295ccdceee91
status VERIFIED
```

The extracted 27-clause `core.cnf` is diagnostic.  The LRAT uses original
clause identifiers and is checked against the full formula.  The checked
bundle is

```text
scratch/audit_ad_k16_c106_sssss_radius1_unsat_bundle_20260730.py
SHA-256 640b20a7b31e600391839be57c55a0894f8cb4903dedf7af7e8b348194fac28c

scratch/ad_k16_c106_sssss_radius1_unsat_bundle_20260730.audit.json
SHA-256 b1f9e87c8ebdcf3654dc95d7b4c4a5e50d5423dba766bd4e4359dca54618a154
payload 273c63ee481331fd5ea6115cdfa517c935c5047ea0f2f5074855abadf8e48242
status PASS_CHECKED_DRAT_LRAT_AND_FULL_PHYSICAL_RADIUS1_REPLAY
```

The H100 proof run used a 512 MiB address-space cap.  Frozen proof-tool
SHA-256 values are: Kissat 4.0.4,
3ee4239c0bef4d237ab72827613426855b17c636d3b5843158fe5e549b175b0d;
drat-trim,
92f0aa9575ed519d66a99b8b1b3dde6ece4618ae4c202a3a4b200265dda0aa7a;
and lrat-check,
e9e71c96b68dc9ed22db35d7581e613e6b161ffbc82c20cba5699f8320a065b8.

This proves:

> **Theorem 3.1 (checked radius-one no-go).**  The exact binary model (1.1)
> is infeasible for every possible choice of its sole outside seam.

## 4. Two independent exact mathematical certificates

### 4.1 Exact 298-right-hand-side reconstruction

Choose 94 independent directed cycles \(C_1,\ldots,C_{94}\) of \(S\).  For
each candidate \(h:u\to v\), choose a directed support path \(P_h\) from \(v\)
to \(u\).  Every balanced real flow on \(S\cup\{h\}\) with \(x_h=1\) has the
form

\[
 x=\mathbf1_h+\mathbf1_{P_h}+
      \sum_{j=1}^{94}\lambda_j\mathbf1_{C_j}.                    \tag{4.1}
\]

The 93 service rows plus the slack row form a nonsingular \(94\times94\)
integer matrix in the \(\lambda_j\).  One exact multi-right-hand-side solve,
with common denominator

\[
 14905561300695363968281280,
\]

therefore gives the unique equality flow for every candidate.  All 298 flows
are nonbinary; indeed all 662 support coordinates are fractional in every
case, and every case has negative support coordinates.  Seam 2739 is a
canonical nonbinary witness in all 298 systems.

The independent checker rebuilds the paths and matrix from the raw ledger,
checks full rank modulo three large primes, verifies every exact matrix
equation, replays balance/service/count/slack, and checks seam 2739 directly.

```text
scratch/exactify_ad_k16_c106_sssss_radius1_mrhs_20260730.py
SHA-256 a3bb5ddb2a8b1e20edba6525f5b82a43c61300b8068c05bc7c1145f8b22683b2

scratch/ad_k16_c106_sssss_radius1_exact_mrhs_20260730.audit.json
SHA-256 a3eb54464e670f69d50eaf9cab46cd2ae2d055beb8ab11568331b5e70531e668
payload 8bfb2b21a77666cc906aa1cf7729b70e18bf97ef17ee7c1609f24a0435505a1a

scratch/audit_ad_k16_c106_sssss_radius1_mrhs_raw_20260730.py
SHA-256 7b7f57a74dc971dae77aaac23fc35b7dce119b4e8a4066636b2b9ea2a54f44e1

scratch/ad_k16_c106_sssss_radius1_exact_mrhs_raw_audit_20260730.audit.json
SHA-256 8de779255bc83e2a4a21601fc88a0e9c50840888e27f4749d7e34a7e6ff858c4
payload f1df0bb3f8e573cf9bc1e212d5407e1f4777df85adc5f6de9eb8eeae34cccbdc
status PASS_INDEPENDENT_RAW_298_PATH_MRHS_AND_NONBINARY_REPLAY
```

### 4.2 One mod-457 circulation separator

Use 93 target-incidence coordinates and one count coordinate.  A spanning-
forest fundamental-cycle basis of the integral support circulation lattice
gives a \(94\times94\) feature matrix \(M\) with

\[
 \det M=-7452780650347681984140640,
\]

and rank 93 modulo 457.  Its normalized left-null row consists of target
coefficients \(a_t\in\mathbb Z/457\mathbb Z\) and count coefficient \(a_0=241\),
with

\[
 241\cdot106+\sum_ta_t\equiv1\pmod {457}.                         \tag{4.2}
\]

The corresponding support-edge functional is a coboundary.  Thus there is a
potential \(p^{(457)}\) on the 571 support ports such that

\[
 R_e:=241+\sum_{t\in H(e)}a_t+
      p^{(457)}_{\operatorname{tail}(e)}-
      p^{(457)}_{\operatorname{head}(e)}\equiv0\pmod {457}        \tag{4.3}
\]

for every \(e\in S\).  Extend the potential by zero off the support vertices.
For every integral globally balanced exact-service/count-106 selection,

\[
 \boxed{\sum_{e\notin S}R_ex_e\equiv1\pmod {457}.}               \tag{4.4}
\]

None of the 298 physically admissible sole-outside candidates has \(R_h=1\).
For each such candidate, the modular row excludes even its signed-support-
completion relaxation, before capacity or Boolean upper bounds.  This signed
relaxation statement is candidate-scoped: allowing arbitrary signed support
coefficients would invalidate the slack-based reduction of all catalogue
seams to the 298 physical candidates.

```text
scratch/audit_ad_k16_c106_sssss_radius1_lattice_20260730.py
SHA-256 d75430205f7941be821dd63d54cf94f5c961662ab175f3f7d8b12356b124e0e1

scratch/ad_k16_c106_sssss_radius1_mod457_separator_v2_20260730.audit.json
SHA-256 e2fa6fa2fe42152566af9a771b029af3b1977f1b61e62dfe58527b500ed35aff
payload 5c53ab031a84b0061582d5c50cf01a1c79ebd97d6d8418a33a81631fad36cc4c
status PASS_EXACT_MOD457_RADIUS_ONE_LATTICE_SEPARATOR
```

The unsuffixed earlier JSON with SHA prefix `b255ab9c` had a shadowed
presentation field and is superseded.  Only the fail-closed `v2` artifact is
citable.

## 5. Exact two-or-more-column escape state for cycle pricing

Theorem 3.1 and the mod-457 separator (4.4), together with the support parity
theorem, give the exact proved source-relative expansion-radius lower-bound
cut

\[
 \boxed{z:=\sum_{e\notin S}x_e\ge2.}                              \tag{5.1}
\]

The strongest compact state established here combines the mod-two and
mod-457 residues.  Extend \(p^{(2)}\) by zero off the support vertex set.
For each seam define

\[
 \epsilon_e:=|H(e)\cap T|+p^{(2)}_{\rm tail(e)}+
                 p^{(2)}_{\rm head(e)}\pmod2                     \tag{5.2}
\]

and \(R_e\) by (4.3).  Let \(q_e\in\{0,\ldots,913\}\) be their Chinese-
remainder lift:

\[
 q_e=R_e+457\bigl((\epsilon_e-R_e)\bmod2\bigr).                  \tag{5.3}
\]

Then \(q_e\equiv R_e\pmod {457}\), \(q_e\equiv\epsilon_e\pmod2\), every
support seam has \(q_e=0\), and every integral balanced `SSSSS` selection
obeys the single exact residue equation

\[
 \boxed{\sum_{e\notin S}q_ex_e\equiv1\pmod {914}.}               \tag{5.4}
\]

This is the appropriate finite state for the cycle-pricing annealer.  For a
directed cycle \(C\), endpoint potentials cancel, so its price is computable
without port labels:

\[
\begin{aligned}
 \epsilon(C)&=\sum_{e\in C}|H(e)\cap T|\pmod2,\\
 R(C)&=241|C|+\sum_ta_t\,m_C(t)\pmod {457},\\
 q(C)&=\operatorname{CRT}_{2,457}(\epsilon(C),R(C)).              \tag{5.5}
\end{aligned}
\]

Cycle prices add modulo 914.  Final exact states must have \(z\ge2\) and
total price one.  In a service-exact/count-exact balanced state, (5.4) is an
implied equality; its value is as an exact support-escape separator and a
column-generation/annealing state, not as a replacement for the 93 service
rows.

For an exactly two-outside-column proposal \(\{a,b\}\), the following filters
are all necessary:

\[
 q_a+q_b\equiv1\pmod {914},\qquad s_a+s_b\le5,\qquad
 H(a)\cap H(b)=\varnothing.                                     \tag{5.6}
\]

the two tails are distinct, the two heads are distinct, and the two quotient
arcs are Eulerian after contracting each of the three support components and
leaving every off-support port as a singleton.  With two arcs, quotient
Eulericity has exactly two forms:

1. both arcs are quotient loops, so each individually has both endpoints in
   one support component; or
2. the two nonloop quotient arcs go between the same two quotient nodes in
   opposite directions.

The frozen compact pricing catalogue contains all 210,763 seams outside
\(S\) with slack at most five.  Exact bucket counting and an independent
explicit replay reduce the radius-two structural interface to only

\[
 \boxed{208=204+4}
\]

These are 204 quotient-loop pairs and four directed quotient two-cycles.
All 208 also satisfy \(H(a)\cap H(b)=\varnothing\), so target-disjointness
removes none.  The sorted canonical pair-set SHA-256 is
55d24bcc086ceea1941759958cbac79b8212a272e7ee2a34f1cf51b67cd696a7.

The frozen catalogue and independent replays are:

- scratch/ad_k16_c106_sssss_crt914_outside_slack5_v2_20260730.tsv,
  SHA-256 da46d259648bf01db3b678cfafca857a49cac79c47f05e5abb3de90b457bb69e;
- scratch/ad_k16_c106_sssss_crt914_radius2_v2_20260730.audit.json,
  SHA-256 9dce75365e9ce98cd16f8096ea206803e8f83326919cc7b4e01e41ebcc62f4ff,
  payload adb22c4a988aa28b21545a5fed645ebe7ea43a740878dffa46e14820d3f417b1;
- scratch/ad_k16_c106_sssss_crt914_radius2_pairs_replay_20260730.audit.json,
  SHA-256 bd33a7a86c27aa45cbc6d9178165e90b065fb633309fa75478a8707820a3c26c,
  payload 620a816024ed530e6d67a716a4559fa942566805b1661740b1adc769911c14b5;
- scratch/ad_k16_c106_sssss_crt914_radius2_service_disjoint_20260730.audit.json,
  SHA-256 d74a1cf145dcf6660772055931f80dff0ede34138e9fe185ff8822f0064c20e0,
  payload 42bc348d70fcdc4260ea43788d8edcb08718fcada615d1686398bc132910e8f4;
- MATH_THEOREM_AD_K16_C106_SSSSS_CRT914_RADIUS2_ANNEALER_INTERFACE_20260730.md,
  SHA-256 ceb4afc6da6d48d919f2fbde3884cea088cea58a3120447d3934afdc5fc6770a.

These conditions give a one-residue exact radius-two pricing interface.  They
are not sufficient for a support completion: the remaining support variables
must still meet all service, count/slack, and port-capacity rows.  The next
exact master now needs only the 208 frozen pairs, each followed by a support-
completion subproblem.

The existing `--escape-basis-json` code in
`scratch/k16_balanced_cycle_anneal_20260730.cpp` counts seams whose two
endpoints are outside the support **vertex set**.  That heuristic is not the
same as \(z\), which counts seam IDs outside \(S\), and it does not implement
(5.4).  A proof-aware annealer should retain an `in_S[seam]` bit, compute the
single \(q\in\mathbb Z/914\mathbb Z\) cycle price from (5.5), and require
\(z\ge2\), \(q=1\) at exact acceptance.

## 6. Precise proved boundary

Proved:

1. the complete radius-zero and radius-one binary `SSSSS` faces are UNSAT;
2. the radius-one result has checked DRAT and LRAT certificates and a full
   independent physical/CNF replay;
3. every global source-relative `SSSSS` solution uses at least two seams
   outside \(S\);
4. every such solution obeys the exact mod-457 row (4.4), equivalently the
   CRT residue (5.4);
5. (5.6) and quotient Eulericity are necessary for an exact radius-two pair;
6. exactly 208 unordered pairs pass this complete structural interface, and
   all 208 are target-disjoint.

Not proved:

1. feasibility or infeasibility with two or more outside seams;
2. sufficiency of any radius-two pair;
3. any q1/residence/separation/connectivity completion;
4. global infeasibility of the `SSSSS` branch or a floor above 106.
