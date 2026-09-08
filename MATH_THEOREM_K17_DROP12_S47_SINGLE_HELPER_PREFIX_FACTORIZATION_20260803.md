# K17 drop-12 S47 single-helper prefix factorization and exact finite replay

**Date:** 2026-08-03

**Status:** exact occurrence-domain theorem, complete residual two-mode
occurrence no-go, and executed support-one triple reduction on the canonical
consumer parent. The exact directed source-prefix relation has three records,
all with pair occurrence zero. The complete 334,639-row endpoint-safe
extension shore of those records by an `S` or `Z` third has an empty lossless
helper-option upper. The independently authenticated 329-row `S x N` prefix
screen is also empty. Combined with the frozen inherited-Hall class credits,
this proves that every occurrence-valid, no-`H`, deficiency-at-most-20
three-mode child with a distinguished `S` source must use both other hosts.
This is a bilateral **necessity** statement only: no bilateral packing,
supplier deficiency 20, higher-arity child, or K17 word is claimed.

The canonical compressed/final parent is

```text
e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb
fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c
```

Throughout, phase 0 is the literal native-b268 owner table and phase 1 is
the transported-s7 owner table. The transported phase is not promoted to
an independently native phase.

## 1. Frozen scope and exact censuses

Let \(S\) be the 47 authenticated rank-16,877 modes. Their exact unary
replay, with the private 7,213-row bank and literal phase reservations, has

```text
|S|                              47
phase-0 reserved rows            20
phase-1 reserved rows            20
reservation intersection         17
reservation union                23
exact common unary anchors         0
parent supplier deficiency        21
```

Let \(Z\) be the 112,099 residual fixed-bank-safe structural modes after
removing H468 and the seven negative modes from U112621, and put

\[
 R=S\mathbin{\dot\cup}Z,\qquad |R|=112146.                \tag{1.1}
\]

The exact structural directed source/helper census is

\[
 47\cdot112146=5270862
 \longrightarrow 5268793                                  \tag{1.2}
\]

after removing 2,069 endpoint conflicts. Its decomposition is

```text
directed S x Z incidences             5,267,163
directed S x S incidences                 1,630
endpoint-disjoint unordered S pairs         815
minimal unordered structural children 5,267,978
per-source directed minimum              112,080
per-source directed maximum              112,138
```

The 1,630 S-by-S orientations remain distinct until the distinguished
source prefix has been evaluated. None of these structural counts is a
prefix-positive, occurrence-positive, or supplier-positive count.

The frozen unary evidence is SHA-bound by

```text
8311bb9909d22e8361c50d700909c46ed9e287df1aa2f91842d5328068c6c8c2
  s47_unary.tsv
78d722f86deadf220bdec233f834481a047f57231db5feda794a4b225bae89ab
  s47_unary.audit.json
```

The structural census payloads are SHA-bound in the accompanying audit
bundle. Section 4 records the subsequent authoritative phasewise upper on
this entire directed domain.

## 2. Pair-child source tickets

For an endpoint-disjoint selected set \(I\), phase \(\phi\), source short
\(s\), and declared key \(k\), let

\[
 {\cal T}_s^\phi(k;I)                                    \tag{2.1}
\]

be the **complete physical ticket relation** after every donor in \(I\) has
been deleted, every host in \(I\) inserted at all admissible flags, the
private and phase-reservation rules applied, and the exact incoming,
outgoing, and literal five-cell predicates checked. Every record retains
both physical provider rows, their flags, its phase footprint, and its
row-to-flag map.

For a ticket \(t\), write \(F(t)\) for its physical row footprint and
\(\gamma_t\) for its row-to-flag map. A source option is

\[
 o=(k,t^0,t^1),\qquad
 t^\phi\in{\cal T}_s^\phi(k;I),                          \tag{2.2}
\]

where \(\gamma_{t^0}\cup\gamma_{t^1}\) is a function. A tuple count or
first witness is not an option relation.

Fix \(s\in S\) and one endpoint-disjoint helper \(f\in R\). In the pair
child \(I=\{s,f\}\), partition the phase tickets into

\[
\begin{aligned}
 B_{s\mid f}^\phi(k)
   &=\{t\in{\cal T}_s^\phi(k;\{s,f\}):h_f\notin F(t)\},\\
 G_{s\leftarrow f}^\phi(k)
   &=\{t\in{\cal T}_s^\phi(k;\{s,f\}):h_f\in F(t)\}.
                                                               \tag{2.3}
\end{aligned}
\]

Here \(B\) means a unary phase ticket surviving deletion of \(d_f\), and
\(G\) means a ticket created or supported by the installed helper host.
More precisely,

\[
 B_{s\mid f}^\phi(k)
 =\{t\in{\cal T}_s^\phi(k;\{s\}):d_f\notin F(t)\}.       \tag{2.4}
\]

Equation (2.4) follows because passing from the unary child to the pair
child changes only \(-d_f,+h_f\). Let \(\bowtie_k\) require the same
declared key and a single-valued union of the two phase flag maps.

### Theorem 2.1 (exact three-mask source-prefix factorization)

The complete pair-child source-option relation is the disjoint union

\[
\boxed{
 {\cal P}_{s\leftarrow f}
 =\bigcup_k\left[
   B_{s\mid f}^0(k)\bowtie_kG_{s\leftarrow f}^1(k)
   \;\dot\cup\;
   G_{s\leftarrow f}^0(k)\bowtie_kB_{s\mid f}^1(k)
   \;\dot\cup\;
   G_{s\leftarrow f}^0(k)\bowtie_kG_{s\leftarrow f}^1(k)
 \right].}                                               \tag{2.5}
\]

Thus every exact directed source prefix uses \(h_f\) in phase mask 01, 10,
or 11. No feasible option for the helper short \(f\) is assumed.

#### Proof

Every pair-child source option has a \(B/G\) type in each phase. A \(B/B\)
option would, by (2.4), be the same internally flag-consistent, same-key
option in the unary child. The authenticated S47 unary replay says no such
option exists. Hence only the three displayed masks remain. Conversely,
each displayed join consists of two exact pair-child tickets at one key
with a single-valued flag map, so it is an exact source option. The masks
are disjoint. \(\square\)

An exact two-role occurrence no-go does **not** imply
\({\cal P}_{s\leftarrow f}=\varnothing\): the source may have an option
while the helper has none, or all source/helper option pairs may conflict.
This is why a feasible pair prefix is not used below.

## 3. Restriction and lift of a support-one triple option

Fix an endpoint-disjoint triple \(I=\{s,f,g\}\), with \(s\in S\) and
\(f,g\in R\). For a source option \(o_s\), define its external host support

\[
 A_s(o_s)=\{y\in\{f,g\}:h_y\in F(t_s^0)\cup F(t_s^1)\}.
                                                               \tag{3.1}
\]

Unary emptiness implies \(A_s(o_s)\ne\varnothing\): a triple source option
using neither helper host avoids both absent donors and would remain a
unary option after both helpers were removed.

### Theorem 3.1 (single-helper restriction/lift)

If an exact triple source option satisfies \(A_s(o_s)=\{f\}\), then the
identical physical option belongs to \({\cal P}_{s\leftarrow f}\).
Conversely, for \(p\in{\cal P}_{s\leftarrow f}\), the identical option is
valid in the triple child and has support exactly \(\{f\}\) if and only if

\[
 F(p):=F(t_p^0)\cup F(t_p^1)
 \quad\text{satisfies}\quad
 F(p)\cap\{h_g,d_g\}=\varnothing.                      \tag{3.2}
\]

#### Proof

The triple option uses no \(h_g\), and it cannot use \(d_g\), which is
absent from the triple provider bank. Removing \(h_g\) and restoring
\(d_g\) therefore leaves its two physical tickets, key, flags, and every
eligibility predicate unchanged. It is a pair-child source option and lies
in (2.5).

In the other direction, adding \(g\) to the pair child deletes \(d_g\) and
inserts \(h_g\). The fixed physical option survives and remains supported
exactly by \(f\) precisely when it uses neither changed endpoint. Theorem 2.1
supplies use of \(h_f\) in at least one phase. Hence (3.2) is necessary and
sufficient. \(\square\)

Theorem 3.1 is independent of supplier deficiency. It applies, in
particular, to every hypothetical deficiency-at-most-20 triple witness.

## 4. Lossless prefix screen without the 5,268,793-row outer sweep

Equation (2.5) gives an exact output-sensitive evaluation plan.

1. Rebuild the complete unary **phase-ticket** relations for every
   \(s\in S\), retaining all keys, physical alternatives, footprints, and
   flags. Index them by source, phase, key, and flag map. A base ticket
   carries every row in its footprint as a donor-kill label.
2. Enumerate exact source tickets containing an installed residual host
   \(h_f\). Each host-aperture posting binds its helper \(f\) directly.
   Reject a posting if its other provider is the deleted donor \(d_f\), and
   retain the installing mode, host row and flag, tuple side, complete
   footprint, and flag map.
3. For each \(G\) posting, probe the opposite-phase \(B\) index at the same
   source and key, filtering \(d_f\notin F(t)\), and probe opposite-phase
   \(G\) postings with the same helper. Apply the exact cross-phase flag
   join and emit the three terms of (2.5).

Every output contains a \(G\) phase by Theorem 2.1, so every output is
reached from an installed-host posting. Conversely, the join emits only
exact source options. The blind directed rectangle (1.2) is therefore an
audited structural domain, not a required loop. This does not promise a
small worst-case output: if the exact prefix relation itself is large, a
lossless explicit ledger must represent it.

Each prefix record must contain at least

```text
source mode and helper mode; all four endpoint rows;
source declared key; the two complete physical tickets;
phase footprints; global row-to-flag map; helper-host phase mask;
donor-kill rows; canonical option hash; completion/input hash.
```

Deduplicating only on source/helper IDs, keys, marginal tuple counts, or a
first witness is not lossless.

### 4.1 Authoritative complete phasewise upper

The complete source/helper screen has now been executed and frozen at

```text
/home/amodo/or15/work/root_k17_s47_aperture_20260803_80042630
```

using the source with SHA-256

```text
80042630bbd302620df9c85bb83c6be2ed48f7e3a3f0b1e82fcf9341bb35414c
```

The authoritative run reports

\[
 \boxed{5268793\ \hbox{directed rows}\longrightarrow 3
        \ \hbox{phasewise same-key survivors}.}          \tag{4.1}
\]

All three rows have source hit 42, source edge 92903, and reported source
key 70:

```text
source_hit  source_edge  source_host  source_donor  helper_edge  helper_host  helper_donor
42          92903        21221        9049          25925        9054         1170
42          92903        21221        9049          25927        9054         7615
42          92903        21221        9049          25929        9054         22761
```

The output payload SHA-256 is

```text
f3f643bd5740507d7ad14874b74d99bbc2b7d4c1114ed7dde543cd6db5c486cd
```

The authoritative handoff reports audit prefix `4fc8fe69...`, pre-manifest
prefix `3757ec...`, post-manifest prefix `5e8b98...`, and PASS for both
manifests. The full remote payloads are not mirrored in this lightweight
bundle, so only the complete output digest is represented as a full local
hash pointer.

Every exact option in \({\cal P}_{s\leftarrow f}\) supplies phasewise
same-key tickets and therefore must project to one of these three rows.
Consequently

\[
 \boxed{
 \{(s,f):{\cal P}_{s\leftarrow f}\ne\varnothing\}
 \subseteq
 \{(92903,25925),(92903,25927),(92903,25929)\}.}          \tag{4.2}
\]

This is a lossless reduction of the exact prefix replay from 5,268,793
directed rows to three. It is not an assertion that any of the three has an
internally cross-phase-consistent source option: the upper does not enforce
the exact join (2.5), literal helper-host use, helper occurrence, or joint
capacity. Its diagnostic first witness remains non-pruning.

All three helpers share physical host row 9054 but delete different donors.
Their mode identities, installed long states, and donor-kill filters must
remain separate. The old H verifier is outside this source class and is not
admissible evidence.

### 4.2 Exact three-row replay and complete two-mode no-go

The genuine S47 package is frozen at

```text
scratch/codex_019fc39a_k17_s47_exact3_20260803
```

with

```text
FINAL_MANIFEST.sha256 file  bd4451e9804cfb369eff7df5e6ec68fd4a645b1e0151ae41f6859287049fbde8
exact output TSV             5eb03ef94410cb21fd346fd76226680de766b6aafac626a205449da1ced65b88
exact audit JSON             324b9bf45a466d1bfdf107772b7abf715e86f6f553253a679e240f6364b49413
```

The exact replay gives

```text
source  helper  source p0/p1  source anchors  partner p0/p1  option edges  positive
92903   25925   1 / 1         1               0 / 1          0             0
92903   25927   1 / 1         1               0 / 0          0             0
92903   25929   1 / 1         1               0 / 0          0             0
```

### Theorem 4.2 (complete residual two-mode occurrence no-go)

Every one of the 5,267,978 endpoint-disjoint unique residual
S-by-\((S\cup Z)\) two-mode children is occurrence-negative.

#### Proof

The authenticated phasewise upper is lossless on all 5,268,793 directed
incidences and rejects all but the three rows in Section 4.1. The genuine
S47 exact verifier enumerates complete physical menus for both roles on
those three rows and finds zero compatible option edges. Thus every directed
incidence is negative. Identifying the two directions of each of the 815
endpoint-disjoint S-by-S children leaves 5,267,163 S-by-Z children plus 815
S-by-S children, hence 5,267,978 unique negative children. \(\square\)

No two-mode occurrence witness or two-mode supplier-replay request remains.

### Theorem 4.3 (three exact source prefixes survive)

The exact source-prefix relation (2.5) is not empty. It consists of exactly
one source option on each of the three directed rows:

\[
 \boxed{
 \{(s,f,p):p\in{\cal P}_{s\leftarrow f}\}
 =
 \{(92903,f,p_f^*):f\in\{25925,25927,25929\}\},}         \tag{4.3}
\]

where the common physical row/flag projection of the three \(p_f^*\) is

\[
\begin{array}{c|c|c|c|c}
\text{key}&q&(\alpha,\beta)&\text{phase 0}&\text{phase 1}\\ \hline
70&7&(0,0)&(9054,8994)&(9069,8994).
\end{array}                                             \tag{4.4}
\]

The helper mode identity remains part of each record even though the
physical projection is common.

#### Proof

For every row, the exact verifier reports one source phase-0 tuple, one
source phase-1 tuple, one two-phase combination examined, and one
internally consistent source option using the partner host. Therefore each
row has exactly one member of (2.5). The SHA-bound one-row-per-helper upper
request records the unique key and physical phase tuples in (4.4).
Theorem 2.1 excludes all other directed rows. \(\square\)

This is the precise boundary: pair occurrence fails on the partner side,
not on the source-prefix side. A third mode can insert a new host and create
the missing partner ticket(s), so Theorem 4.2 does not imply that a
support-one triple is impossible.

Indeed, \(F(p_f^*)=\{9054,8994,9069\}\). Any third mode \(g\) preserving the
prefix must satisfy \(F(p_*)\cap\{h_g,d_g\}=\varnothing\), in addition to
six-endpoint disjointness. For helper 25925, every triple partner phase-0 ticket must use
\(h_g\). For helpers 25927 and 25929, every triple partner ticket in both
phases must use \(h_g\). In the latter two branches, unit capacity forces the
third role itself to avoid \(h_g\) in both phases. These are exact
donor-delete/host-insert consequences, not existence claims.

## 5. Exact finite extension replay

For a prefix \(p\in{\cal P}_{s\leftarrow f}\), define the exact third-mode
shore

\[
 \Gamma(p)=\{g\in R\setminus\{s,f\}:
   |\{h_s,d_s,h_f,d_f,h_g,d_g\}|=6,\
   F(p)\cap\{h_g,d_g\}=\varnothing\}.
                                                               \tag{5.1}
\]

For \(g\in\Gamma(p)\), let \({\cal O}_f(s,f,g)\) and
\({\cal O}_g(s,f,g)\) be the complete internally flag-consistent same-key
two-phase option menus in the literal triple child. These menus are rebuilt
without requiring a feasible pair packing.

For two options \(u,v\), put \(C(u,v)=1\) exactly when their same-phase
footprints are disjoint in both phases and their combined row-to-flag map is
a function; put \(c(u,v)=1-C(u,v)\). With a minimum over an empty set equal
to \(+\infty\), define

\[
 \Lambda(s,f,p,g)=
 \min_{u\in{\cal O}_f(s,f,g),\ v\in{\cal O}_g(s,f,g)}
 \max\{c(p,u),c(p,v),c(u,v)\}.                          \tag{5.2}
\]

### Theorem 5.1 (exact support-one occurrence oracle)

The residual non-H triple face has an occurrence-valid packing whose
distinguished S source uses exactly helper \(f\) if and only if

\[
\boxed{
 \exists s\in S,\ f\in R,\ p\in{\cal P}_{s\leftarrow f},\
 g\in\Gamma(p):\quad \Lambda(s,f,p,g)=0.}               \tag{5.3}
\]

#### Proof

Given a packing with source support \(\{f\}\), Theorem 3.1 restricts its
source option to a prefix \(p\) and proves \(g\in\Gamma(p)\). The two other
role options lie in the complete triple-local menus. Unit phase capacity
and the single physical flag address make all three pairs compatible, so
(5.2) has value zero.

Conversely, value zero supplies the surviving exact source prefix and one
exact option for each helper. Pairwise same-phase disjointness gives joint
unit capacity, and a pairwise-consistent union of row-to-flag functions is a
function. The six tickets form a literal occurrence packing. The source
option uses \(h_f\) and not \(h_g\). \(\square\)

The helper-\(f\) menus admit a second exact incremental factorization. If
\({\cal T}_f^\phi(k;\{s,f\})\) is the pair-child menu, then

\[
\begin{aligned}
 {\cal S}_{f\mid g}^\phi(k)
   &=\{t\in{\cal T}_f^\phi(k;\{s,f\}):d_g\notin F(t)\},\\
 {\cal G}_{f\leftarrow g}^\phi(k)
   &=\{t\in{\cal T}_f^\phi(k;\{s,f,g\}):h_g\in F(t)\},\\
 {\cal T}_f^\phi(k;\{s,f,g\})
   &={\cal S}_{f\mid g}^\phi(k)
     \mathbin{\dot\cup}{\cal G}_{f\leftarrow g}^\phi(k).
                                                               \tag{5.4}
\end{aligned}
\]

Thus an implementation can join surviving helper tickets and third-host
aperture postings instead of rebuilding a blind pair square. The complete
third-role menu is still mandatory; a repaired \(f\) menu alone is not an
occurrence witness.

For fixed \(p,g\), (5.2) is the exact triangle test

\[
 \exists u\in F_{p,g},\ v\in G_{p,g}(u),                 \tag{5.5}
\]

where

\[
\begin{aligned}
 F_{p,g}&=\{u\in{\cal O}_f:C(p,u)=1\},\\
 G_{p,g}(u)&=\{v\in{\cal O}_g:C(p,v)=C(u,v)=1\}.
                                                               \tag{5.6}
\end{aligned}
\]

Footprint and unequal-flag conflict bitsets give an exact finite replay;
empty (5.6) is a proof-safe rejection. All prefix IDs and tested \(g\)-shore
IDs must be covered by row-set equality in the replay manifest.

### Theorem 5.2 (executed `S union Z` third-shore no-go)

The complete extension of the three prefixes (4.3) by an
endpoint-disjoint third mode in \(S\dot\cup Z\) was executed at

```text
/home/amodo/or15/work/root_k17_s47_support1_sz3_20260803_08d45ad52d80
```

The source package pre-includes the genuine S47 occurrence primitives before
renaming the embedded pair-verifier `main`; it does not use the old H
verifier. Its frozen source identities are

```text
common header  08d45ad52d809952ef2747a47ef4ac25863412ce0b55181d102244f94061bf34
upper source   0b0fdd50a237db041645c8679fcea53a27026506e7910d692bbfe35aef0fa2e0
exact source   165cf0c09fabe3a805b26724ec24977a7f5d2a930b67fb10b13674f5446090c9
```

For each prefix the screen requires six-endpoint disjointness and the full
lift condition \(F(p)\cap\{h_g,d_g\}=\varnothing\). The audited census is

```text
raw 3 x (S union Z) rows             336438
endpoint-and-prefix-safe rows        334639
per-prefix rows          110864, 112007, 111768
third-class S rows                        138
third-class Z rows                     334501
helper-option upper survivors       0, 0, 0
```

The upper rebuilds the complete phase menus of the frozen helper after the
simultaneous third-donor deletion and third-host insertion. It permits every
same-key, cross-phase flag-consistent helper option compatible with the
fixed source prefix and deliberately defers the third-role menu. Therefore
every exact occurrence packing extending one of (4.3) would survive this
upper. None does. The exact stage receives zero requests and is correctly
vacuous; it is not represented as 334,639 full three-role exact replays.

The result and package identities are

```text
upper TSV                    e636a9ee27e90d57934fbd9bfff7d8dd766557d3d07bdefef6414e16172dc2dd
upper audit                  924ffb1c86aa5818f0554f4434f91f2fedb8672a01c1b2399bc1323ea1e6aa69
exact header TSV             d5783322d678673e798e8ef004a168df81956d9a31b984043646138b8327ca33
exact audit                  96cfe80671f4c4d4a335587aac2ff7b00284f7638fd276509e35a5f063bbff14
RUN_INPUTS.sha256 file       957da903494ba682d13c4707bf0f215d464a7a86ae94662ceeb3505d5889b082
OUTPUTS.sha256 file          d443d347bf798cf05f39ff3b7f1c56319605cb234978dad1041e5b3d75cd792f
FINAL_MANIFEST.sha256 file   13f09c24b3ab43ab4843a4a6c702e105749096a1cd1ce8394f8f659b8923629b
```

All three nested exact3 provenance manifests and all three new package
manifests passed `sha256sum -c` in the frozen H100 root.

### Theorem 5.3 (authenticated `S x N` prefix no-go)

The separate authenticated S-by-N package checks all

\[
 |S|\,|N|=47\cdot7=329
\]

endpoint-disjoint directed prefixes and finds zero phasewise same-key source
prefixes. Its exact consequence is: an S source supported by exactly one N
helper is occurrence-dead. The independent audit is

```text
MATH_AUDIT_K17_DROP12_S47_N_HELPER_PREFIX_NOGO_INDEPENDENT_20260803.md
SHA-256  2a33d3e228b21022a7e8631c914de7f0e3e1e5c09936b71e608a550b85c53997
```

and the authenticated H100 `FINAL_MANIFEST.sha256` file has SHA-256

```text
0c4e2b404bb1d8f8bc3a0cea50a45def575cfad8cde51598bb5e29f1bbf7289f
```

The independent compact-bundle manifest file has SHA-256
`e17e72caf098a59cd45d1b51455acaffe958f9032de90b9c921237251596dacf`.

### Corollary 5.4 (complete target-capable no-H support-one closure)

Consider an endpoint-disjoint no-H triple with a distinguished S source
that could have supplier deficiency at most 20. The final inherited-Hall
cover theorem, SHA-256

```text
7556ec953b062a88810b81f26163ff8c86616019dbaa44a6ac9ce1216d1b30ca
```

assigns credits `S=+1`, `Z=0`, and `N=-1`, with every N sharing one
endpoint. Hence a target-capable such triple either has both other modes in
\(S\cup Z\), or has class `S,S,N`. A class `S,Z,N` triple has total credit
at most zero and cannot reach deficiency 20; two N modes cannot be
endpoint-disjoint.

In the first case any support-one source option restricts by Theorem 3.1 to
the complete prefix relation (4.3), and Theorem 5.2 rejects every admissible
third extension. In class `S,S,N`, support by N is rejected by Theorem 5.3;
support by the S helper would restrict to an S-by-S prefix, but the complete
relation (4.3) contains only the three Z helpers. Thus it is also impossible.
Therefore

\[
\boxed{\text{every occurrence-valid target-capable no-H S-source triple
must use both other hosts.}}                              \tag{5.7}
\]

This is only a forced-bilateral reduction. It does not assert that any of
the nine bilateral source joins is occurrence-valid or supplier-positive,
and it says nothing about higher arity.

## 6. Exact bilateral criterion

For two possible helpers, a source has \(4^2-1=15\) nonempty ordered
phase-support pairs. They split exactly as

\[
 \boxed{15=3\text{ using only }f
          +3\text{ using only }g
          +9\text{ using both}.}                       \tag{6.1}
\]

At the coarser complete host-incidence-matrix level, there are 61 admissible
one-phase assignments. Of these, 46 avoid \(h_f\to s\), 46 avoid
\(h_g\to s\), and 34 avoid both. Hence the unary-forced 2,565 matrices
split as

\[
\begin{aligned}
 2565&=61^2-34^2,\\
 960&=46^2-34^2 &&\text{source uses only }f,\\
 960&=46^2-34^2 &&\text{source uses only }g,\\
 645&=2565-2\cdot960 &&\text{source uses both}.
                                                               \tag{6.2}
\end{aligned}
\]

### Corollary 6.1 (executed target-face bilateral reduction)

By Corollary 5.4, every occurrence-valid no-H S-source triple capable of
supplier deficiency at most 20 lies in the nine source-support joins,
equivalently the 645-matrix part of (6.2). The support-one parts have been
eliminated, rather than merely deferred.

This does not certify any one of the nine joins. Every future
occurrence-positive unordered bilateral child must still be materialized
once by jointly applying all three transfers to canonical fa491, preserving
all 7,213 protected rows, and must receive a fresh complete supplier
matching. No additive supplier credits, mismatched parent, marginal phase
counts, or separate transfer materializations can establish deficiency 20.

Triples containing an H468 role remain in the separately SHA-frozen H-source
theorem lane. This note's bulk enumerated helper universe is
\(R=S\dot\cup Z\), supplemented only by the authenticated 329-row S-by-N
prefix no-go. It does not silently recertify the H lane.

Accordingly, the proof-safe target-capable no-H S-source three-mode frontier
is reduced to

\[
 \boxed{\text{the irreducible bilateral-source joins}.} \tag{6.3}
\]

No existence, supplier, or higher-arity conclusion is contained in (6.3).

## 7. Frozen certificate and remaining scope

The support-one reduction is frozen by:

1. the exact three-record prefix relation and full endpoint/lift condition;
2. the 334,639-row per-prefix shore census and the empty lossless
   helper-option upper, with its H100 input/output/final manifests;
3. the authenticated 329-row S-by-N empty prefix screen; and
4. the final inherited-Hall class theorem excluding the remaining
   target-incapable N-containing signatures.

The complete phasewise coverage ledger, exact \(B/G\) prefix relation, and
all 5,267,978 two-mode occurrence no-gos are already frozen.

This theorem proves the three-mask source-prefix factorization, exact
restriction/lift equivalence, complete residual two-mode occurrence no-go,
the three-record exact prefix relation, the empty 334,639-row lossless
third-shore upper, the S-by-N prefix no-go, and the resulting target-face
forced-bilateral reduction. The zero upper makes the downstream exact stage
vacuous; no supplier replay, positive bilateral packing, chronology,
residence, arbitrary upper, compiler, higher-arity, or word check is claimed.
