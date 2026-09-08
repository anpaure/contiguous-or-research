# AD audit: exact radius-three `SSSSS` MITM no-go

Date: 2026-07-30  
Status: proved and independently replayed for the frozen source-relative
\(C=106\), `SSSSS` seam catalogue

## 1. Scope

Let \(S\) be the frozen 662-column fractional support and let \(E\) be the
frozen 211,604-seam source-relative catalogue.  A physical selection satisfies

\[
\begin{aligned}
 \operatorname{out}_x(v)&=\operatorname{in}_x(v)\le1,\\
 \sum_{e:t\in H(e)}x_e&=1 &&(t\in\mathcal T,\ |\mathcal T|=93),\\
 \sum_ex_e&=106,\\
 \sum_es_ex_e&=5,\\
 x_e&\in\{0,1\}.
\end{aligned}                                                     \tag{1.1}
\]

All direct slacks are nonnegative.  The checked preceding theorem excludes
zero, one, and two selected columns outside \(S\), so every physical solution
already obeys \(z_{\rm out}\ge3\).  This note closes radius three.

The result is source-relative.  It is not an impossibility theorem for the
full `SSSSS` branch or for arbitrary signed triples that violate a physical
necessary condition.

## 2. Exact additive support-lattice signature

The support graph has 662 edges, 571 vertices, three components, and cycle
rank

\[
 662-571+3=94.                                                    \tag{2.1}
\]

Let \(M\in\mathbb Z^{94\times94}\) be the 93-service-plus-count feature
matrix of a spanning-forest fundamental-cycle basis.  Its exact determinant is

\[
 \det M=-7452780650347681984140640,                              \tag{2.2}
\]

with

\[
 |\det M|=2^5\cdot5\cdot457\cdot63079\cdot33852407\cdot47731799.\tag{2.3}
\]

For every complete left annihilator \(\lambda M=0\pmod n\), choose a support
potential \(p_\lambda\) satisfying

\[
 \lambda\Phi(e)+p_\lambda(\operatorname{tail}e)
 -p_\lambda(\operatorname{head}e)=0\pmod n                     \tag{2.4}
\]

on every \(e\in S\), with gauge zero at each component root and each
off-support singleton.  Define the corrected outside-column signature by the
left side of (2.4).

The frozen atlas uses five additive generators for the complete 32-element
mod-32 annihilator group and one generator for each of the five odd prime
factors.  Thus every outside seam has a ten-coordinate signature with moduli

\[
 32,32,32,32,32,5,457,63079,33852407,47731799.                  \tag{2.5}
\]

The five mod-32 generator orders are \(2,2,2,4,2\); their generated closure
has exactly 32 elements.  The desired `SSSSS` signature is

\[
 (16,16,0,16,16,0,256,26131,32237008,8090040).                  \tag{2.6}
\]

> **Lemma 2.1 (exact signed-recourse test).**  Let \(F\subseteq E\setminus S\)
> have zero incidence after contracting each support component and retaining
> every off-support port as a singleton.  Then \(F\) has an integral signed
> support completion satisfying balance, all 93 service rows, and count 106
> if and only if
> \[
> \sum_{e\in F}\sigma(e)=\sigma_*                                \tag{2.7}
> \]
> in all ten coordinates.

**Proof.**  Zero quotient incidence permits an integral signed forest return
for \(F\).  Any two returns differ by an integral support circulation.  The
94 fundamental cycles are a \(\mathbb Z\)-basis of that circulation lattice,
so completion is equivalent to membership in \(M\mathbb Z^{94}\).  Smith
normal form reduces membership to the prime powers in (2.3).  The complete
mod-32 annihilator group and the five odd left-null generators test precisely
those local memberships.  Potentials cancel under global balance.  \(\square\)

The column atlas is

```text
scratch/ad_k16_c106_sssss_radius3_signature_atlas_20260730.tsv
rows 210763; loops 645; nonloop arcs 210118
SHA-256 fea507c8e0dcfe987dccecfbbbfc8993defe7f2d6a6233bf7f2d732216ffdf0b
```

Each row contains the physical seam ID, slack, CRT-914 price, raw endpoints,
quotient endpoints, topology, semantic-bank flag, 93-target bit mask, and the
ten exact signature coordinates.

## 3. Exhaustive radius-three topology

Delete quotient loops from a balanced three-arc directed multigraph.  Its
nonloop part is a disjoint union of directed cycles.  Therefore exactly one of
the following occurs:

1. three quotient loops;
2. one quotient loop plus a reciprocal directed two-cycle;
3. one directed three-cycle on three distinct quotient classes.

These three cases are exhaustive.

The checked 27-clause semantic theorem gives a 217-column bank \(B\) such that
every physical solution of (1.1), at any radius, selects at least one member
of \(B\).  Each triple is enumerated exactly once by taking as anchor the least
seam ID in \(F\cap B\).  For a fixed anchor, the two partner roles are unique
in each of the three topology cases.  This is a canonical one-plus-two
meet-in-the-middle enumeration; importantly, it does not make the unsound
assumption that the partner pair is one of the 208 balanced radius-two pairs.

Every candidate is filtered by

\[
 \sum_{e\in F}s_e\le5,
 \qquad
 \sum_{e\in F}q_e=1\pmod {914},                                  \tag{3.1}
\]

then by the complete signature (2.7), raw tail/head capacity, and pairwise
target disjointness.

## 4. Primary exhaustive census

The H100 single-CPU run produced the following exact stage counts:

\[
\begin{array}{l|r}
\text{stage}&\text{canonical triples}\\ \hline
\text{semantic anchor plus quotient topology}&1,158,239\\
\text{total outside slack at most five}&726,260\\
\text{CRT-914 total price one}&872\\
\text{complete signed-support signature}&0.
\end{array}                                                       \tag{4.1}
\]

The unfiltered topology split is

\[
\begin{array}{l|r}
\text{three loops}&1,028,810\\
\text{loop plus reciprocal two-cycle}&127,805\\
\text{directed three-cycle}&1,624.
\end{array}                                                       \tag{4.2}
\]

Thus all 872 CRT survivors already fail the exact signed-support lattice.
Raw capacity and target-disjointness do not need to reject any later survivor.

As a startup regression, the same signature atlas replays the complete frozen
radius-two pair set:

- 208 structural pairs;
- pair-set SHA-256
  `55d24bcc086ceea1941759958cbac79b8212a272e7ee2a34f1cf51b67cd696a7`;
- zero signed-lattice survivors;
- frozen first-failure split \(198/8/2\) at moduli \(32/5/63079\).

Primary artifacts:

```text
scratch/build_ad_k16_c106_sssss_radius3_mitm_20260730.py
SHA-256 e7dd36b6e989e8b3945426a54331833844dcabbf3a1ca1b59744c59aa0be1783

scratch/ad_k16_c106_sssss_radius3_mitm_20260730.audit.json
SHA-256 ea8c60a5218a50563121e9e2f9ea26a901ee5be54c54268f8e80c490289d65f4
payload 8463b1c8ddc45b7b925e6bc4c63e2643553cb6026bdf10e89928c4769df8f897
status PASS_RADIUS3_PHYSICAL_INTERFACE_NO_GO_BY_SIGNED_RECOURSE

scratch/ad_k16_c106_sssss_radius3_signed_survivors_20260730.tsv
SHA-256 7b6c6f54410ac589e9294d012d1ad979f7618fbb7c4cc7eeff08765b7eb33a6b
```

The survivor TSV contains only its header.  The canonical empty survivor-set
SHA-256 is
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

The run used one H100 CPU, a 2 GiB address-space cap, 16.03 seconds wall time,
and 201,240 KiB maximum resident memory.  No GPU and no heavy local process
were used.

## 5. Independent reverse-MITM replay

The independent auditor does not reuse the primary enumeration.  It reparses
the raw ledger, reconstructs all 210,763 outside rows, the support forest,
the \(94\times94\) feature matrix and determinant, verifies that the five
mod-32 rows generate all 32 annihilators, checks every odd rank, recomputes
every support potential, all ten atlas coordinates, and every CRT-914 price.

It then builds exact closing-column dictionaries keyed by quotient direction,
CRT price, and the full signature.  For each canonical semantic anchor and
second seam it queries the unique required third-seam key.  This reverse
lookup independently finds

\[
 0\text{ signature hits},\qquad0\text{ physical-interface survivors}.\tag{5.1}
\]

```text
scratch/audit_ad_k16_c106_sssss_radius3_mitm_20260730.py
SHA-256 f42fe449e31e1ec17b68181909cc7727914b6f9bef8bdb6f442b56c5bb5bf1f6

scratch/ad_k16_c106_sssss_radius3_mitm_independent_replay_20260730.audit.json
SHA-256 06c72e245dd7d8428f6e239f250d024ae57b9a922865ec821d5c9da22f08505f
payload 910ea79b9209a28a7db71993435170f57052a7032854c1f32a10a53624584ea4
status PASS_INDEPENDENT_RAW_LEDGER_AND_REVERSE_MITM_RADIUS3_NO_GO
```

The independent run used one H100 CPU, a 2 GiB address-space cap, 9.09
seconds wall time, and 225,436 KiB maximum resident memory.

The combined command/resource record is
`scratch/ad_k16_c106_sssss_radius3_h100_resource_20260730.txt`, SHA-256
`45ab5972d1178931ea9401e56604cd19cba3c95f7dd0f6837c748245c3732240`.

## 6. The radius-four lower bound

Combining the checked radius-zero, radius-one, radius-two, and radius-three
certificates proves:

> **Theorem 6.1 (frozen source-relative expansion bound).**  Every physical
> solution of (1.1) satisfies
> \[
> \boxed{z_{\rm out}:=\sum_{e\notin S}x_e\ge4.}                 \tag{6.1}
> \]

The radius-three proof uses physical necessary cuts—especially incidence in
the 217-column semantic bank and nonnegative slack budget.  Therefore (6.1)
is a physical expansion theorem.  It does not say that every abstract signed
outside triple fails lattice membership.

## 7. Reusable condition beyond radius three

The atlas is immediately reusable at radius four and higher.  For any outside
set \(F\), the exact necessary interface is:

1. \(|F|\ge4\);
2. quotient incidence zero;
3. \(\sum_{e\in F}s_e\le5\);
4. \(\sum_{e\in F}q_e=1\pmod{914}\);
5. \(\sum_{e\in F}\sigma(e)=\sigma_*\) in the ten-coordinate exact lattice
   signature;
6. distinct raw tails and distinct raw heads;
7. outside target multiplicity at most one; and
8. \(F\cap B\ne\varnothing\).

At radius four, quotient-balanced topologies have directed-cycle length
partitions

\[
 1+1+1+1,\quad2+1+1,\quad2+2,\quad3+1,\quad4.                  \tag{7.1}
\]

These give the next exact MITM catalogue.  Passing all eight conditions proves
only signed support recourse plus outside physical necessities.  Support
nonnegativity/binarity/capacity and all q1, residence, separation,
connectivity, and later physical rows still require explicit replay.

## 8. Precise boundary

Proved:

1. the complete frozen physical radius-three interface has no signed-support
   recourse survivor;
2. the primary census and an independently implemented reverse lookup agree;
3. every frozen source-relative physical solution has at least four outside
   columns; and
4. the ten-coordinate atlas gives an exact signed-recourse oracle at every
   larger radius.

Not proved:

1. existence or nonexistence at radius four;
2. infeasibility of all abstract signed triples;
3. full `SSSSS` branch infeasibility; or
4. a physical carrier, q1/residence completion, or literal compiler at
   \(C=106\).
