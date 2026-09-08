# K16 weighted port-potential audit: from floor 95 to the exact cycle-packing floor 98

Date: 2026-07-30  
Lane: AD  
Status: proved for the frozen source-relative, direction-coherent
`q<=3`/upper-width-four seam catalogue.  The weighted certificate gives the
linear cut $c\ge95$; the equality-face replay gives $c\ge96$; and an exact
three-target directed-cycle packing gives $c\ge98$ in the same scope.  No
feasible selection at 98 is authenticated, so 98 is a lower bound, not a
proved integral optimum.

**Supersession notice (2026-07-30).**  The floor-98 argument below remains a
valid independent closed-walk/cycle-packing certificate, but it is no longer
the numerical frontier.  The exact scale-140 composite target-potential
certificate in
`MATH_THEOREM_K16_RATIONAL_TARGET_POTENTIAL_FLOOR101_20260730.md`, independently
audited in `MATH_AUDIT_AD_K16_SECOND_STAGE_PORT_DUAL_FLOOR101_20260730.md`,
uses the same endpoint-balance and 93 service rows and proves $c\ge101$.

## 1. Frozen scope

The source factor and compact seam ledger have SHA-256 values

```text
source factor  6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204
binary ledger  832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657
```

The ledger has 12,870 transition ports and 211,604 directed collar-safe
seams.  Its zero-baseline service bank is

\[
 \mathcal H=\mathcal H^-_2\sqcup\mathcal H^+_3,
 \qquad |\mathcal H^-_2|=45,\quad |\mathcal H^+_3|=48.
\]

For a seam $a=(\ell(a),r(a))$, let $H(a)\subseteq\mathcal H$ be the set
of distinct source defects gained by its new lower-q2 or upper-q3 crossing
windows.  Exactly 5,425 seams have $H(a)\ne\varnothing$; call these provider
seams.  The remaining 206,179 seams have $H(a)=\varnothing$.

Let $x_a\ge0$ be a selected-seam vector satisfying the endpoint-balance
equations

\[
 \sum_{a:r(a)=v}x_a=\sum_{a:\ell(a)=v}x_a
 \qquad\text{for every transition port }v                         \tag{1.1}
\]

and all 93 additive service rows

\[
 \sum_{a:t\in H(a)}x_a\ge1\qquad(t\in\mathcal H).                 \tag{1.2}
\]

For an integral selected port permutation, $x_a\in\{0,1\}$ and
$c=\sum_a x_a$ is its seam/cut count.  The proof below first holds for the
fractional relaxation.

The theorem uses no q1 row, separation row, reverse-edge row, survivor row,
residence row, or arbitrary-upper replay row.

## 2. Exact seven-orbit weights

Let \(\rho\) cyclically permute coordinates $0,\ldots,14$ and fix
coordinate 15.  Assign the following integer weight $w_t$ to each target
in the indicated \(\rho\)-orbit.

| family | representative | orbit size | weight | contribution |
|---|---:|---:|---:|---:|
| lower q2 | 33337 | 15 | 11 | 165 |
| lower q2 | 33609 | 15 | 22 | 330 |
| lower q2 | 34069 | 15 | 36 | 540 |
| upper q3 | 36343 | 15 | 19 | 285 |
| upper q3 | 36599 | 15 | 18 | 270 |
| upper q3 | 39791 | 15 | 16 | 240 |
| upper q3 | 46811 | 3 | 23 | 69 |

These seven orbits are disjoint, equal the complete 93-target bank, and give

\[
                  W:=\sum_{t\in\mathcal H}w_t=1899.              \tag{2.1}
\]

The orbit assertions and (2.1) were independently replayed with integer
arithmetic.  All weights are positive, and their minimum is 11.

## 3. Exact port potential

The frozen certificate supplies an integer potential

\[
       \phi:\{0,\ldots,12869\}\longrightarrow\{0,\ldots,20\}   \tag{3.1}
\]

whose vector SHA-256 is

```text
884f1ac7a95994ea2761673915132d7d8af6f351b8382c9b9418a6e5357914f0
```

and which satisfies, for every one of the 5,425 provider seams,

\[
 \sum_{t\in H(a)}w_t
       \le 20+\phi(r(a))-\phi(\ell(a)).                          \tag{3.2}
\]

The exact replay has potential range $[0,20]$, zero maximum violation,
1,388 tight provider inequalities, and slack histogram totaling 5,425.
For a nonprovider seam, (3.2) holds automatically with zero left side,
because $0\le\phi\le20$.  Thus (3.2) is valid for every one of the
211,604 catalogue seams.

### Theorem 3.1 (weighted endpoint Farkas cut)

Every nonnegative $x$ satisfying (1.1)--(1.2) obeys

\[
                         1899\le20\sum_a x_a.                    \tag{3.3}
\]

Consequently every integral selected port permutation servicing all 93
defects has

\[
                             c\ge95.                              \tag{3.4}
\]

#### Proof

Multiply the target row (1.2) by $w_t$ and sum over $t$.  Since all
weights are nonnegative,

\[
 1899
 \le \sum_a x_a\sum_{t\in H(a)}w_t.                              \tag{3.5}
\]

Apply (3.2) to every seam.  The potential terms cancel by endpoint balance:

\[
\begin{aligned}
 \sum_a x_a\sum_{t\in H(a)}w_t
 &\le20\sum_a x_a+
       \sum_a x_a\bigl(\phi(r(a))-\phi(\ell(a))\bigr)\\
 &=20\sum_a x_a.
\end{aligned}                                                     \tag{3.6}
\]

This proves (3.3).  If $x$ is binary, $c=\sum_a x_a$ is integral, so
$c\ge\lceil1899/20\rceil=95$.  QED.

This is the requested localization: the lower bound is forced solely by a
weighted combination of the 93 service rows and the transition-port balance
rows.  The compact eager consequence is the single linear inequality

\[
                         20c\ge1899.                              \tag{3.7}
\]

No opaque infeasibility solve is needed.

### Equivalent provider-path proof

If the selected integral circulation is decomposed into cycles and its
zero-hit seams are deleted, let $p$ be the number of provider seams, $s$
the number of nonempty provider paths, and $z$ the number of deleted
zero-hit seams.  Summing (3.2) on a provider cycle cancels the potential;
summing on a provider path leaves an endpoint difference at most 20.  Hence

\[
 1899\le20(p+s),\qquad s\le z,qquad p+z=c,                       \tag{3.8}
\]

which again gives $c\ge95$.  The direct proof of Theorem 3.1 is stronger
and shorter: it also proves the fractional circulation inequality without
choosing a path decomposition.

## 4. The equality-95 face is empty

For a provider seam define its integer slack

\[
 \sigma(a)=20+\phi(r(a))-\phi(\ell(a))
             -\sum_{t\in H(a)}w_t,                               \tag{4.1}
\]

and for a nonprovider seam define

\[
 \sigma(a)=20+\phi(r(a))-\phi(\ell(a)).                          \tag{4.2}
\]

Every \(\sigma(a)\) is a nonnegative integer.

### Lemma 4.1 (unit-slack equality reduction)

If an integral endpoint-balanced service selection had $c=95$, then:

1. every target would be supplied exactly once;
2. its weighted service would equal 1899;
3. \(\sum_{a:x_a=1}\sigma(a)=1\); and
4. every selected seam would satisfy \(\sigma(a)\le1\).

#### Proof

Theorem 3.1 gives weighted service between 1899 and 1900.  Repeating any
target would add at least the minimum target weight 11, which is impossible.
Thus every target is supplied exactly once and the weighted service is 1899.
Summing (4.1)--(4.2) and cancelling potentials by endpoint balance gives

\[
 \sum_{a:x_a=1}\sigma(a)=20\cdot95-1899=1.
\]

Nonnegativity and integrality prove the last assertion.  QED.

Let $G_{\le1}$ be the directed graph consisting of catalogue seams with
\(\sigma(a)\le1\).  Every selected seam in a balanced integral selection
lies on a selected directed cycle, hence its endpoints lie in the same
strongly connected component of $G_{\le1}$.

The exact replay gives

```text
slack-at-most-one arcs                 3,558
  provider                             2,148
  nonprovider                          1,410
nontrivial SCCs                   15 of size 5
cycle-eligible arcs                       90
  provider                                60
  nonprovider                             30
targets with no cycle-eligible provider   63
```

In particular, target 33337, and in fact the following complete list, has no
cycle-eligible provider:

```text
33337 33906 35044 36343 36417 36599 36935 37320 39791 39918 40066
40430 41102 41872 46811 46814 46835 47003 47068 47327 47343 47364
48092 48347 48583 48867 49436 50939 50976 51067 51235 52663 56173
56185 56269 56431 56439 56941 57059 57201 58237 58301 58385 59099
60854 60860 60902 60983 60987 61238 61297 61368 61886 61918 61960
62317 63259 63261 63416 63926 64397 64398 64966
```

### Theorem 4.2 (cycle obstruction at equality)

No integral endpoint-balanced selection satisfying all 93 service rows has
$c=95$.  Therefore, in the frozen catalogue,

\[
                              c\ge96.                             \tag{4.3}
\]

#### Proof

There is a slightly stronger direct formulation.  Since target 33337 has no
cycle-eligible provider in $G_{\le1}$, every directed catalogue cycle which
contains a provider for 33337 contains some seam of cost at least two.  All
seam costs are nonnegative integers, so every such cycle has total cost at
least two.

An integral endpoint-balanced selection decomposes into directed cycles, and
its service row for 33337 puts a 33337-provider on at least one selected
cycle.  Hence

\[
             \sum_{a:x_a=1}\sigma(a)\ge2.                       \tag{4.4}
\]

If $M=\sum_a x_a\sum_{t\in H(a)}w_t$ is its weighted service, endpoint
balance gives the exact restitution identity

\[
             20c=M+\sum_{a:x_a=1}\sigma(a).                     \tag{4.5}
\]

The 93 service rows give $M\ge1899$.  Combining this with (4.4) yields the
integer cycle-strengthened cut

\[
                             20c\ge1901,                          \tag{4.6}
\]

and therefore $c\ge96$.  In particular $c=95$ is impossible.  QED.

Theorem 4.2 is an exact equality-face obstruction, not an optimality result:
no feasible integral selection at 96 or any later count is authenticated by
this audit.

At count 96 the exact identity has residual budget

\[
 21=\sum_{t\in\mathcal H}w_t(\mu_t-1)
       +\sum_{a:x_a=1}\sigma(a),                                \tag{4.7}
\]

where \(\mu_t\) is the service multiplicity of target \(t\).  Because the
weights are positive integers, precisely five multiplicity cases remain:

1. no repeated target and total slack 21;
2. one repeated weight-11 target and total slack 10;
3. one repeated weight-16 target and total slack 5;
4. one repeated weight-18 target and total slack 3; or
5. one repeated weight-19 target and total slack 2.

Two repeats, or a repeat of weight 22, 23, or 36, are impossible.  This was
the exact count-96 face before the aggregate cycle-packing certificate below.

## 5. Three-target cycle-packing theorem

Set

\[
                    E=\{46811,56173,60854\}.                    \tag{5.1}
\]

These are exactly the three weight-23 targets.  Direct binary replay gives
exactly 60 provider seams for each target.  Every such provider has that
single defect as its complete hit set, and the three provider-seam banks are
pairwise disjoint.

For a nonempty subset $S\subseteq E$, let $\kappa(S)$ be the minimum reduced
cost of a directed catalogue cycle servicing every target in $S$.  The audit
computes a relaxation by choosing one provider arc for each target and
joining consecutive chosen arcs by independently shortest directed return
paths.  Those connector paths may overlap, repeat ports, or incidentally
service other targets.  Therefore their optima are lower bounds for a
physical simple selected cycle, which is the direction needed here.

Exact nonnegative Dijkstra replay on all 211,604 seams gives

\[
\begin{array}{c|c}
S&\text{closed-walk lower bound for }\kappa(S)\\ \hline
\{46811\},\{56173\},\{60854\}&17\\
\{46811,56173\},\{46811,60854\},\{56173,60854\}&39\\
E&55.
\end{array}                                                       \tag{5.2}
\]

The computation ranges over all 60 providers for each requested target and
all cyclic orders.  It also stores explicit shortest closed-walk witnesses
attaining 17, 39, and 55; these witnesses establish equality in the relaxed
closed-walk problem but are not asserted to be physically simple cycles.

### Theorem 5.1 (special-target cycle-hypergraph dual)

Every integral endpoint-balanced selection satisfying the 93 service rows
has total reduced cost at least 51.  Consequently

\[
                         20c\ge1899+51=1950,
 \qquad                         c\ge98.                          \tag{5.3}
\]

#### Proof

Decompose the selected balanced integral seam multigraph into directed
cycles.  For each selected cycle $C$, let $S_C\subseteq E$ be the set of
distinct special targets it services.  Formula (5.2) gives

\[
                       \sigma(C)\ge17|S_C|.                      \tag{5.4}
\]

Indeed the singleton constraint is tight, while the pair and triple bounds
have margins $39-34=5$ and $55-51=4$.  Every member of $E$ is serviced by at
least one selected cycle, even if service is repeated, so

\[
 \sum_C|S_C|\ge3,
 \qquad \sum_C\sigma(C)\ge17\sum_C|S_C|\ge51.                 \tag{5.5}
\]

All remaining cycles have nonnegative reduced cost.  Weighted service is at
least 1899, and the endpoint restitution identity (4.5) therefore yields
(5.3).  QED.

Equivalently, assigning dual weight 17 to each member of $E$ is a valid
three-row cycle-hypergraph inequality.  It is robust to repeated targets,
multiple selected components, and closed-walk contamination.

At exact count 98, repeated service is impossible: a repeat has weight at
least 11, and

\[
                     1899+11+51=1961>20\cdot98.
\]

Thus the exact count-98 face, if nonempty, has every target serviced once and
total reduced cost exactly $1960-1899=61$.  This audit does not construct
such a face.

## 6. Comparison with the earlier pseudoforest bounds

The independent provider-only edge-cover minimum $p\ge56$ and the
33-target path bound $s\ge17$ gave $c\ge73$.  The potential certificate
couples provider cost and path endpoints and strictly subsumes that sum.

Two persisted 17-mask witnesses were also audited:

* The original relaxed 17-mask cover has total exceptional-mask cardinality
  55 on a 48-target union, hence overlap surplus seven.  At $p=56$, the 18
  double-degree-zero defects permit at most 94 provider memberships, only one
  above the 93 distinct targets.  Therefore this fixed mask cover cannot
  lift to the $p=56$ equality face.
* The corrected joint-v6 masks partition the 48 exceptional targets, but an
  exact BFS in the complete 5,425-provider digraph gives independent shortest
  exact-mask path lengths summing 154, which is 98 above the $p=56$ budget.
  Thus an equality decomposition that assigns those exact masks one-to-one
  to its seventeen provider paths cannot have $p=56$.  This does not exclude
  a different 17-mask family or authenticate a joint vertex-disjoint lift;
  the persisted audit deliberately records that narrower scope.

These facts are ancillary; Theorems 3.1, 4.2, and 5.1 do not use them.

What may safely be called exact is:

* the provider-only edge-cover minimum 56;
* the weighted circulation lower bound 95;
* the equality-95 obstruction and resulting lower bound 96; and
* the special-target cycle-packing lower bound 98.

There is no authenticated feasible integral provider pseudoforest at 98, so
there is no authenticated integral optimum.  The old exact-count 70 and 73
CP-SAT `INFEASIBLE` transcripts are superseded lower-count evidence, not an
optimality certificate.  A floating LP record at objective 94.95 was used to
discover the weights, but the theorem uses only the displayed integer
weights and potential.

Accordingly, the requested construction stops in this order:

1. the original 17-mask witness fails the provider-membership budget;
2. the corrected fixed partition fails the 56-provider physical-path budget;
3. arbitrary path masks still face the universal weighted port-potential
   cut, the equality-95 singleton Hall obstruction, and the weight-23
   cycle-packing cut; and
4. q1 balance is never reached.

No 73-cut candidate survives these stages.

## 7. Independent replay and provenance audit

The strongest independent standard-library verifier parses the binary
ledger directly, checks its byte SHA, verifies the seven rotation orbits,
replays all 5,425 inequalities, reconstructs the same potential, and verifies
the original certificate payload:

```text
scratch/verify_k16_provider_weight_potential_floor95_20260730.py
  SHA 125053164750cbaa36aae8a4e470156da82e5b991f0c8dd2095cb2a00061e293

scratch/k16_provider_weight_potential_floor95_independent_20260730.audit.json
  SHA 60c4dfca8085c1f7e853d822079a9124fcffa1b855990383e8373e4d090f6215
  payload ad95dba0f6f1120ffc1a764c05d4753beb05be679c398fc74e501e98f1d65bb5
```

A second pinned generator/replay gives the same weights, potential-vector
hash, slack histogram and tight-arc count:

```text
scratch/audit_k16_provider_path_weighted_floor95_20260730.py
  SHA a29f2dadd47d228bc4ee07800398e5646dfda147de578d0949d90fc7ee2346aa

scratch/k16_provider_path_weighted_floor95_20260730.audit.json
  SHA 6e6a7e52c72b29b3300028e27d931dfb11d6a8a050f7a4e08b79f0ea95ad8c36
```

The current equality-face replay is

```text
scratch/threadA_audit_k16_provider_potential_floor95_and_equality_face_20260730.py
  SHA ebff922ce388607b0b91acc8884a5d39909dd5a1686b2972ca71012717d57459

scratch/threadA_k16_provider_potential_floor96_v2_20260730.audit.json
  SHA f2690358e51df3546d96ca79942b75fede07c18e7707225c4b98381b4ca00ada
  payload b31dac838bf0f972e3aaff11ab5b6cb3d5d836c50b7a6c25a36407bacbd4e4e0
```

A separate C++ verifier uses a second binary-record parser, independently
checks the seven phase orbits and all 5,425 provider inequalities, rebuilds
the reduced-cost-at-most-one SCC obstruction, and reproduces the singleton
target 33337.  The ledger byte hash was checked separately immediately
before this replay.

```text
scratch/audit_ad_k16_provider_weight_potential_floor95_independent_20260730.cpp
  SHA 26a2af36e42df7078ef5e9297c9b8ebc10738542b8e54ea843397bac2533d144

scratch/ad_k16_provider_weight_potential_floor96_v2_20260730.audit.json
  SHA a57e445f266ff88287429712d7701ab70a2957d61de6008ef21a7048c0192a3d
```

The primary three-target cycle-packing replay is

```text
scratch/audit_k16_exact96_special_cycle_cost_20260730.py
  SHA 154036ed7aed97e86fd1ead9eb6d555e5d2ac4483201a2673aec57370ccaf861

scratch/threadA_k16_balanced_service_floor98_20260730.audit.json
  SHA b6ecb5104cdaabcf52d3fa1fad02ded9a3b659431396224da528782ce9fc178a
  payload 296858837fd8abaf330f15d2dea3d704fcb14e4b792f4c0f4be8e32b96f9b53b
```

An independent direct-binary verifier imports no shared parser, asserts that
all 180 special providers are singleton-hit and that the three 60-arc banks
are pairwise disjoint, reconstructs the complete required distance table,
and stores explicit 17/39/55 closed-walk witnesses:

```text
scratch/audit_ad_k16_special3_cycle_packing_floor98_20260730.py
  SHA f41a1bb3da1b1a609486277b0db597d47784ad2ffa6b467f088732fcb757704d

scratch/ad_k16_special3_cycle_packing_floor98_20260730.audit.json
  SHA b0ba786b627b78dbc8230282ea0359c36d0d561aec5853735a6cb8d5a14051fc
  payload 568ab73e4877b571775e430c08b811f8c90f588199090b96f5ae54c368001dec
```

The independent replay used one H100 CPU for 10.17 seconds and 134,176 KiB
maximum RSS.  No optimizer was invoked.

The targeted 17-mask replay is

```text
scratch/audit_ad_k16_explicit17_provider_path_lift_20260730.py
  SHA 83b224172a961e2d3fedc22c1031a9b96627b2d0c3fa9ba96cb4594c03de9515

scratch/ad_k16_explicit17_provider_path_lift_20260730.audit.json
  SHA d54ffbe4a1ca875456357aee8892c75ae4ff159072aa52ee724d0d754ee07439
```

Audit correction: the short discovery checker
`audit_k16_provider_weight_potential_floor95_20260730.py` (SHA
`294893...`) records the binary SHA in its output but does not hard-code that
SHA before parsing, does not pin the imported parser, and does not reject an
output symlink.  It should not be the sole fail-closed verifier.  The
standard-library verifier above hard-pins and hashes the complete binary and
does not import the shared parser, so these provenance defects do not affect
the mathematical certificate.

## 8. Scope boundary

Theorems 3.1, 4.2, and 5.1 apply only to endpoint-balanced selections from the
frozen SHA-`832ddd` catalogue and its 93 fixed additive service rows.  They do
not transfer without a fresh replay to:

* the older combined `WIDTH45` classification, whose 150 width-five-only
  singleton providers change the provider digraph;
* close or interacting nonseparated windows;
* reverse-orientation seams absent from the catalogue;
* unrestricted compound rethreads or a different K16 carrier; or
* a literal K16 impossibility theorem.

Within the frozen model, however, the earlier global floor 68 is not the
frontier: the exact service-plus-port-cycle consequence is $c\ge98$.
