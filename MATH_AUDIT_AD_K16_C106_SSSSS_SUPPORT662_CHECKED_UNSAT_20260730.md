# AD audit: checked UNSAT of the \(C=106\) `SSSSS` 662-column support

Date: 2026-07-30  
Status: proved, independently audited, source-relative and support-local

## 1. Exact scope

Let \(S\) be the 662 positive columns of the frozen capacity-one `SSSSS`
fractional point.  On Boolean variables \(x_e\), \(e\in S\), consider

\[
\begin{aligned}
 \sum_{e\in\delta^+(v)}x_e&=\sum_{e\in\delta^-(v)}x_e\le 1
       &&\text{for every active port }v,\\
 \sum_{e:t\in H(e)}x_e&=1
       &&\text{for each of the 93 frozen targets }t,\\
 \sum_{e\in S}s_ex_e&=5. &&
\end{aligned}                                                    \tag{1.1}
\]

Here \(H(e)\) is the target set serviced by seam \(e\), and

\[
 s_e=2+y_{\operatorname{head}(e)}-y_{\operatorname{tail}(e)}
        -\sum_{t\in H(e)}b_t                                      \tag{1.2}
\]

is the exact nonnegative direct-dual slack.  The frozen target prices have
\(\sum_t b_t=207\).

Endpoint balance telescopes the potential term in (1.2).  Hence every point
obeying the 93 exact service rows satisfies

\[
 \sum_es_ex_e=2\sum_ex_e-207.                                    \tag{1.3}
\]

Thus the slack-five row in (1.1) implies, and under the other rows is
equivalent to, the requested count row

\[
 \sum_ex_e=106.                                                   \tag{1.4}
\]

The model therefore enforces endpoint balance and capacity one, all 93
targets exactly once, count 106, and slack five exactly.  It omits separation,
reverse-edge, q1, residence, survivor, deeper-shadow, and connectivity rows.
The theorem below is stronger than needed because its mathematical core uses
only balance, integrality, and 33 of the service requirements.

Frozen principal inputs are:

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

scratch/k16_direct_cycle_dual_exact_20260730.audit.json
SHA-256 29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d

scratch/k16_floor106_s5_pdlp_20260730.json
SHA-256 e934799a0f881163e621236a530b4127253a4b032653eeb21876f40e81fad00a

scratch/k16_floor106_s5_pdlp_20260730.tsv
SHA-256 e8cfd1c9f5ac8c68e49c8efeed9beae76334128b39a282a3cac126757deee494

scratch/k16_floor106_s5_capacity_exact_20260730.audit.json
SHA-256 7f9780503ca106052044dc0b13604666509602e80f9bf7df6b091bbaa62c806e

scratch/k16_floor106_s5_capacity_exact_20260730.tsv
SHA-256 bd12a626faa84fc0cef676bd2263d895ed5a63d34a59403a2ad111e27888268a
```

## 2. Exact support geometry and uniqueness

The support has 571 active ports and three strongly connected components,
with vertex/edge pairs

\[
 (2,2),\qquad(4,4),\qquad(565,656).
\]

Its circulation-space dimension is therefore

\[
 662-571+3=94.                                                    \tag{2.1}
\]

The frozen audit supplies 94 independent directed support cycles.  The 93
service rows and the slack row have full rank 94 on those cycle coordinates.
Equivalently, 568 independent balance rows together with the 93 service rows
and one of the equivalent count/slack rows form a nonsingular
\(662\times662\) rational system.  The unique real solution is the reconstructed
fractional point; every one of its 662 coordinates is strictly between zero
and one.  Its common edge denominator is

\[
 93159758129346024801758,
\]

and its largest outgoing port mass is

\[
 \frac{37778099230409452138842}{46579879064673012400879}<1.
\]

This uniqueness argument already excludes a binary solution.  It is not the
promoted proof core, because the following small parity contradiction is both
more transparent and independent of capacity, count, and slack.

## 3. Exact algebraic support core

Put

\[
\begin{split}
T=\{&33337,36132,36343,37320,39791,40066,41170,41285,
42010,46224,46811,47003,47068,49436,49572,50939,\\
&50976,51235,51252,54312,56173,56439,56941,57059,
58301,58385,59099,60983,61238,61297,61368,61918,63926\}.
                                                               \tag{3.1}
\end{split}
\]

The checked audit gives a bit \(p_v\in\mathbb F_2\) on every support port,
with 283 one-bits, such that every \(e:u\to v\) in \(S\) satisfies

\[
 |H(e)\cap T|\equiv p_u+p_v\pmod2.                              \tag{3.2}
\]

For any integral endpoint-balanced support flow,

\[
\begin{aligned}
 \sum_{t\in T}\sum_{e:t\in H(e)}x_e
 &\equiv \sum_{e:u\to v}(p_u+p_v)x_e\\
 &\equiv \sum_vp_v
    \left(\sum_{e\in\delta^+(v)}x_e+
          \sum_{e\in\delta^-(v)}x_e\right)\\
 &\equiv0\pmod2.                                                \tag{3.3}
\end{aligned}
\]

Exact-once service of the 33 targets in \(T\) makes the left side \(33\equiv1\).
This is a contradiction.

> **Theorem 3.1 (support-local integral no-go).**  The exact binary model
> (1.1) on \(S\) is infeasible.  More strongly, no integral endpoint-balanced
> flow supported on \(S\) can service every target in (3.1) an odd number of
> times.

The exact row core consists of the 33 target equations in (3.1), together
with the balance equations selected by \(p_v=1\); their mod-two sum is
\(0=1\).  The audit verifies (3.2) on all 662 columns.  It also independently
finds rank 89 for the 94-row cycle system over \(\mathbb F_2\) and rank 90
after appending the right-hand side.  No minimum-weight claim is made for the
displayed 33-target certificate.

The parity checker and result are:

```text
scratch/audit_ad_k16_c106_sssss_support_parity_escape_20260730.py
SHA-256 728b3dc859b7f1174dccad099bc621a729198bf78bd4b573d581fdb2a2628abf

scratch/ad_k16_c106_sssss_support_parity_escape_20260730.audit.json
SHA-256 d44c78780df5be82808d42f61ce1337f0f3cb18cde307f0222cf30a52c8705f5
payload 55eac841209a59fac4354eb8b19f8cd30e8c75c683792aeefc5fa0581a820a40
```

## 4. Independently checked proof-producing encoding

The deterministic emitter maps primary variables \(1,\ldots,662\) to the
authenticated seam order and emits exactly 2,251 variables and 5,588 clauses.
Its clause ledger is

\[
\begin{array}{c|r|r}
\text{family}&\text{clauses}&\text{auxiliaries}\\ \hline
\text{port activity}&2466&571\\
\text{incoming AMO}&194&91\\
\text{outgoing AMO}&195&91\\
\text{target ALO}&93&0\\
\text{target AMO}&1179&424\\
\text{slack unit proxies}&122&61\\
\text{slack threshold counter}&1337&351\\
\text{slack terminal rows}&2&0
\end{array}
\]

Port activity plus the two AMO families is equivalent to
\(\operatorname{in}(v)=\operatorname{out}(v)\in\{0,1\}\).  The target rows
are exactly-one.  Repeated slack proxies and the exact threshold-five counter
give \(\sum_es_ex_e=5\).  Equation (1.3) derives count 106, so an independent
cardinality counter is neither needed nor omitted.

```text
scratch/emit_ad_k16_c106_sssss_support662_cnf_20260730.py
SHA-256 a005b72a42048c40f490669fc0b45cae3c06f32923e7f9b74db4641bf57fb252

scratch/verify_ad_k16_c106_sssss_support662_cnf_20260730.py
SHA-256 f7235fac87588f2cd395f633310691f84c585a5f443c1be0310f811d095ca93e

scratch/ad_c106_sssss_support662.cnf
SHA-256 6b58f07605208278d1b4f602b05a2e310caf0c14e16bb1c3359fd8ee4016457f

scratch/ad_c106_sssss_support662.manifest.json
SHA-256 3abbf616a8941290b15b111d9668e6bbf2e3ffa31f61bc2071a1bf2c547b4198

scratch/ad_c106_sssss_support662_cnf.audit.json
SHA-256 81821ed7c969b6d7dd0c1fbfd6fb50aeec4c9f2aaca46d0b437df8b324c9cc9f
status PASS_CNF_LINEAGE_SYNTAX_AND_SOURCE_REPLAY
```

Kissat 4.0.4 returned UNSAT with exit status 20.  `drat-trim` checked the
DRAT, extracted 106 of the original 5,588 clauses, retained 9 of 437 lemmas
and 118 resolution steps, and used zero RAT lemmas.  The independent
`lrat-check` then checked the LRAT against the **full original CNF** and
derived empty clause 6025.

```text
scratch/ad_c106_sssss_support662.drat
SHA-256 e5a8e9de4511dbc16847cb30e4bb6d86c4aef3ee7b1b3c7c2aed17ce07de458b

scratch/ad_c106_sssss_support662.core.cnf
SHA-256 91072cb448cbaf5c3011a367862c061ff8f516463f6228cb0dfb71c3356f8a10

scratch/ad_c106_sssss_support662.core.lrat
SHA-256 bf92379f1ec2435401d7c919765645d0a9d15e410413e2507c642229b5d1e668

scratch/ad_c106_sssss_support662.drat-trim.log
SHA-256 077ef7a9f7ffd14494867193bf892f1583c915a474cce396f768076ac5c42d87
status VERIFIED

scratch/ad_c106_sssss_support662.lrat-check.log
SHA-256 950f258b6ca37a148cc547ab7531356a0493491748501363321fbaa1a7a1861d
status VERIFIED
```

The extracted `core.cnf` is diagnostic.  The LRAT retains original clause
identifiers and must be checked against the full 5,588-clause CNF, not the
renumbered 106-clause file.  Proof-tool hashes are:

```text
Kissat 4.0.4  a9c4fadcaf55fcccf67f8980b10a81d436508b8fd705a672408f7e6bb73e26d3
drat-trim      92f0aa9575ed519d66a99b8b1b3dde6ece4618ae4c202a3a4b200265dda0aa7a
lrat-check     e9e71c96b68dc9ed22db35d7581e613e6b161ffbc82c20cba5699f8320a065b8
```

The compact bundle audit is:

```text
scratch/audit_ad_k16_c106_sssss_support662_unsat_bundle_20260730.py
SHA-256 06d984bb19704ed0d9c7c5a71cf648966ab9ec84b83b6a5d2f557528022f8885

scratch/ad_k16_c106_sssss_support662_unsat_bundle_20260730.audit.json
SHA-256 f1a510e3e090cc0bd4f824db48a869c681baba90ee20bff3b8ee39d5066c1bab
payload 67d05125deb809c36b5fb90556b844d6c2886e9bf4276b451da65f27a93859cd
status PASS_CHECKED_DRAT_AND_INDEPENDENT_LRAT
```

The older file
`scratch/k16_floor106_s5_exact_seed_support_unsat_bundle_20260730.audit.json`
belongs to a different 67,414-variable explicit-count formula and is not a
manifest for this compact proof.

## 5. Exact global escape condition and annealer interface

Extend the support gauge by \(p_v=0\) off the active support vertices and put

\[
 \rho_e=|H(e)\cap T|+p_{\operatorname{tail}(e)}+
                    p_{\operatorname{head}(e)}\pmod2.             \tag{5.1}
\]

Every integral endpoint-balanced global `SSSSS` selection satisfies

\[
 \sum_e\rho_ex_e\equiv1\pmod2.                                  \tag{5.2}
\]

All 662 support columns have \(\rho_e=0\).  A selected column in the integral
slack-five face has \(s_e\le5\).  In the full frozen ledger there are exactly
9,311 columns with \(\rho_e=1\) and \(s_e\le5\).  Therefore the first exact
annealer cut is

\[
 \boxed{\sum_{e:\rho_e=1,\ s_e\le5}x_e\equiv1\pmod2},\qquad
 \sum_{e:\rho_e=1,\ s_e\le5}x_e\ge1.                            \tag{5.3}
\]

For a radius-one expansion, component balance forces the sole outside seam
to have both endpoints in the same one of the three support components.
Exactly 298 columns satisfy this return condition as well as (5.3).  Their
slack histogram is

\[
\begin{array}{c|rrrrrr}
s_e&0&1&2&3&4&5\\ \hline
\#&49&60&115&42&29&3.
\end{array}                                                       \tag{5.4}
\]

The authenticated annealer bank is

```text
scratch/ad_k16_c106_sssss_parity_escape_bank_20260730.tsv
SHA-256 cb021f38ab5e423804bcb8bb885aa20026f34ef59eb93b0500dd716cfc573600
```

The radius-one face is treated separately, with its own checked proof, in
MATH_AUDIT_AD_K16_C106_SSSSS_RADIUS1_CHECKED_UNSAT_AND_CRT_ESCAPE_20260730.md.
No conclusion in this support-only note excludes a solution after adding two or more
columns, and nothing here proves the full source-relative `SSSSS` branch
infeasible.
