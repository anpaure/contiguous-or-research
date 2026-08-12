# The exact provider-only floor at the K16 93-hole endpoint is 56

Date: 2026-07-30

Status: solver-free theorem once the authenticated binary seam catalogue is
accepted. This is a lower bound for every repair inside that catalogue, not
a repair and not a no-go at radius 56.

## 1. Authenticated input

The source is the audited length-eight-orbit factor

```text
scratch/k16_asymmetric_len8_orbit_repair_20260730.json
SHA-256 6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204
```

with 45 missing lower-q2 masks and 48 missing arbitrary-upper rank-11
masks. The independently cross-checked seam ledger is

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657
```

and contains 211,604 direction-coherent collar-safe seams. For each seam it
records the literal lower-q2 and fixed-width upper-q3 masks created by that
seam. Every one of the 93 missing masks has at least one provider.

## 2. Provider graph

Make a graph \(G\) on the 93 missing masks. A pair \(\{a,b\}\) is an edge
when some seam creates both masks. A seam creating only one missing mask is
regarded as a singleton service.

The exact catalogue census is

```text
seams hitting zero missing masks   206179
seams hitting one missing mask       5232
seams hitting two missing masks        193
distinct two-hit target pairs          119
```

There are no lower/lower two-hit seams. Of the 193 two-hit seams, 103 are
upper/upper and 90 are lower/upper. Most importantly, exactly 18 vertices
of \(G\) are isolated:

```text
34069 35370 35461 37972 38154 41285 41633 43089 43176
43540 46811 49802 50498 53410 53584 54312 56173 60854
```

Thus any matching of two-hit services uses only the remaining 75 vertices,
so it has size at most

\[
 \left\lfloor\frac{93-18}{2}\right\rfloor=37.
\tag{2.1}
\]

The audit certificate lists 37 pairwise target-disjoint two-hit seams, so
the bound is attained. It leaves 19 targets unmatched; the certificate also
lists one genuine singleton seam for each of those targets.

## 3. Exact floor

Use the standard edge-cover/matching identity, with one-hit services treated
as loops.  For completeness, take an inclusion-minimal provider cover.  Each
connected component made from its ordinary edges is a star: if a component
contained an edge whose two endpoints both had another incident selected
edge, that edge could be deleted.  Choose one ordinary edge from every
nontrivial star.  These choices form a matching, and the number of chosen
edges is exactly `number of covered vertices - number of services` over the
nontrivial components.  Loops contribute neither quantity.  Thus a cover of
\(93\) vertices by \(c\) services yields a matching of size at least
\(93-c\), and consequently \(c\ge93-\nu(G)\).

Here \(\nu(G)\le37\) by (2.1), so every provider cover has size at least

\[
 93-37=56.
\tag{3.1}
\]

Conversely, the 37 certified two-hit seams and 19 certified singleton seams
cover all 93 targets, using exactly 56 seams. Hence

\[
 \boxed{\tau_{\rm provider}=56.}
\tag{3.2}
\]

This supersedes the weak cardinality bound \(\lceil93/2\rceil=47\). Port
injectivity, return-flow closure, q1 preservation, cut separation, physical
residence and survivor-shadow constraints can only raise the minimum. In
particular, every feasible separated-port endpoint must use at least 56
cuts, but the displayed 56-provider cover is not asserted to be a legal
endpoint.

## 4. Reproducible certificate

```text
scratch/audit_k16_defect_provider_edge_cover_20260730.py
SHA-256 7cb0a970b9850a1b25f888f682ea29c579c9b7ab3e2ceeaee2847e5493f6baac

scratch/k16_defect_provider_edge_cover_20260730.audit.json
SHA-256 7e0d51edfa2c933eea20808e43ea1445672cfe25e60f68afe3ed11e05c56ed27
payload SHA-256 d4ee261d82cfc935116ab34c3d9bddb03a726c26b37e23e089daf80830884d5a
```

The checker uses only the standard library. It independently parses the
binary ledger, verifies the 18 isolated vertices, replays every seam in the
37-edge matching and every singleton seam, checks disjointness and complete
coverage, and emits the frozen audit payload.

An independent H100 implementation reconstructs the graph, runs a general
maximum-matching solver, emits a Tutte--Berge certificate, and constructs its
own 56-seam cover:

```text
scratch/solve_k16_defect_service_cover_20260730.py
SHA-256 b9fcf8905c9a8953415ec0a46ddab3be6a6755e6c1e21c6dc66140b8952ab5c6

scratch/k16_defect_service_cover_20260730.audit.json
SHA-256 ad14505e6080e188240559c7949e51536a89579dda1ddb20e303b9115de603c7
```

The two implementations agree on 119 pair edges, 193 physical double seams,
the same 18 isolated targets, matching number 37, and minimum cover 56.
