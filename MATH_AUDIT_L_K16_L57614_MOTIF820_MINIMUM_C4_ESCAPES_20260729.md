# L57614-only successor: exact minimum q1-perfect C4 escapes from motif 820

Date: 2026-07-29  
Status: proved by a bounded exact Johnson/provider replay.  Two successor
factors are materialized.  No rebuilt-overlay feasibility, residence descent,
or deeper-shadow claim is made.

## 1. Frozen endpoint and successor core

The source is the factor obtained by applying only the `L57614` q1-safe
preconditioner to the detector-zero endpoint:

```text
scratch/k16_failedlit0_mixed_hall_escape_l57614_20260729.json
SHA-256 167aa8534d0fc3b1483c2e60d965faf94bfea1f233a5f4cb593c620191e00651
```

It is a spanning degree-two Johnson factor with both physical q1 palettes
complete, component lengths `(13,12857)`, and exactly `2222` short-residence
violations.

Its deletion-minimal guarded successor core is

```text
scratch/k16_mixed_hall_escape_l57614_guarded_core_20260729.json
SHA-256 60c01989449f066e5daa943fda7282e637a5bfba3250d89b174918455692bf96
```

The ten lower and eight upper q1 rows, all provider indices, and the physical
closure

\[
 \mathcal M=
 \{(64036,64040),(64036,65028),(64040,64264)\}                 \tag{1.1}
\]

are identical to the twice-preconditioned successor core.  Only the stored
cyclic occurrence data differ: this artifact records motif index `790`, start
`5535`, whereas the composed endpoint records index `820`, start `7706`.
Thus “motif 820” below names the common physical affine socket (1.1), not a
claim that the occurrence indices agree.

The solver-free signed replay on this source gives exactly the same primitive
identity

\[
 a_{6484}+a_{7719}+b_{12315}
 +b_{12455}+b_{12456}+b_{12457}\le 0,                         \tag{1.2}
\]

while residence requires the sum of the last three terms to be at least one.
It also verifies that no common source/resident edge has positive signed gain.
The remaining possible signed-socket break, insertion of a negative-gain
Q-only seam, is exhausted separately in Section 2.

## 2. Complete minimum-radius reduction

A nontrivial degree-preserving edit cannot delete and insert one undirected
edge: equality of all vertex degrees forces the inserted edge to have the same
endpoint multiset and hence to equal the deleted edge.  Therefore its radius
is at least two.

For each guarded rank-seven or rank-nine colour there are exactly
`binom(9,2)=36` physical provider seams.  Once a proposed new provider `uv` is
fixed, a degree-balanced radius-two completion deletes one of the two current
edges at `u`, one of the two at `v`, and reconnects their other endpoints;
there are at most four completions.  The audit records exactly
`18*36=648` abstract provider slots, checks up to four neighbour pairings for
each provider absent from the source, and deduplicates to `173` literal
Johnson C4s.  It then replays all `11440` lower and all `11440` upper q1 rows.

Exactly two C4s remain q1-complete and break (1.2).  Since any direct deletion
from (1.1) removes a source-unique guarded provider and must replace it, the
same census contains every direct motif hit.  The signed-socket audit finds
no positive-gain common edge and checks all 342 Q-absent negative-gain seams:
their 97 degree-balanced completions have zero full-q1 survivor.  Hence the
following list is complete at radius two, and radius two is the exact literal
minimum.

## 3. Guarded-redundancy escape

The first C4 is

\[
\begin{array}{ll}
\mathrm{delete}&(43789,47629),\ (44557,44809),\\
\mathrm{insert}&(43789,44809),\ (44557,47629).
\end{array}                                                  \tag{3.1}
\]

Its complete nonzero q1 ledger is

\[
L_{43785}:1\to2,\quad L_{44553}:2\to1,\quad
U_{47885}:3\to2,\quad U_{48653}:1\to2.                      \tag{3.2}
\]

Thus it breaks the fixed normalization by duplicating the guarded colour
`L43785`; it does not touch (1.1).  It removes one old short motif and creates
four.  Relative to the L-only base it changes

\[
 2222\longmapsto2225                                         \tag{3.3}
\]

residence violations and changes component lengths from `(13,12857)` to
`(13,5576,7281)`.  It is a certificate escape but is strictly worse for the
residence objective.

The exact materialization is

```text
scratch/k16_l57614_motif820_escape_redundancy_l43785_20260729.json
SHA-256 cd379fd288d515fd58c96d71e8034c96a9114165ba7447bb8c4cdd8be73a8590
```

## 4. Direct collar slide

The second C4 is

\[
\begin{array}{ll}
\mathrm{delete}&(56088,64024),\ (64040,64264),\\
\mathrm{insert}&(56088,64264),\ (64024,64040).
\end{array}                                                  \tag{4.1}
\]

Its complete nonzero q1 ledger is

\[
L_{55832}:2\to1,\quad L_{56072}:1\to2,\quad
U_{64056}:1\to2,\quad U_{64296}:2\to1.                      \tag{4.2}
\]

It deletes `(64040,64264)` from (1.1), replacing its unique `L64008`
provider exactly.  The old occurrence disappears, but a new coordinate-five,
length-two defect has closure

\[
 \{(64024,64040),(64036,64040),(64036,65028)\}.              \tag{4.3}
\]

The residence count is exactly unchanged,

\[
 2222\longmapsto2222,                                        \tag{4.4}
\]

while the component lengths become `(13,2270,10587)`.  This is therefore
neutral defect transport, not a strict residence descent.  Among the two
minimum C4s it is the unique one that does not worsen total residence, but it
creates an additional physical component.

The exact materialization is

```text
scratch/k16_l57614_motif820_escape_direct_slide_20260729.json
SHA-256 c47a7f231496414a9bfad028bd5f0816e85e53fccae7d657a919a183ffd49e74
```

## 5. Does the radius-two chain continue?

Yes in the exact carrier/certificate sense, but not yet in the overlay or
residence sense.

Both C4 supports are edge- and vertex-disjoint from each of the two previous
preconditioners:

```text
U27742:
  delete (25662,27678),(25694,25722)
  insert (25662,25722),(25694,27678)

L57614:
  delete (57487,57615),(57550,57742)
  insert (57487,57550),(57615,57742)
```

Hence either move composes literally after the `L57614` preconditioner and
produces another spanning degree-two factor with both q1 palettes complete.
This proves a second radius-two certificate-breaking step; the first escape
did not exhaust local q1-perfect mobility.

However, the exact red/blue overlay has not been rebuilt after either new
C4.  The direct move transports the guarded short collar with no residence
gain, and the redundancy move adds three violations.  Thus neither artifact
is evidence that the iterative dual chain terminates or that exact overlay
feasibility has improved.

## 6. Permanent light replay

```text
scratch/audit_k16_motif820_sparse_hall_20260729.py
SHA-256 00697aeedbee798212eb7e27b86891595b6f76572e631b4bf2db197fe4b281e2

scratch/audit_k16_motif820_l57614_sparse_hall_20260729.py
SHA-256 aec277604f3f6749e4dcfa79b534653fecee4bf965ae8080e9ad3ae5c1e73cfe

scratch/k16_motif820_l57614_sparse_hall_20260729.audit.json
SHA-256 983c5f573889cf8ba7cb836b6b53968b0e5b0505143433e306ff00bcf4a6c17b

scratch/audit_k16_motif820_active_colour_c4_20260729.py
SHA-256 d8ab47dc02d17539d5bd7c04e9306a6f7ecc72ace9cb6f509e0885491b8c3ce3

scratch/audit_k16_motif820_l57614_active_colour_c4_20260729.py
SHA-256 d979c7c2a8cfd0e47e09e667d898759c262f91ca26c4378b8885755860907241

scratch/k16_motif820_l57614_active_colour_c4_20260729.audit.json
SHA-256 a7f67624d3b0c196e465df0b0ddb5bfe1db09480e2090cd54b46c5c0c699d070

scratch/materialize_k16_motif820_l57614_c4_escapes_20260729.py
SHA-256 cc648d24900725e1b57d047d4d2de19daeb874be8ac2b1e7685c31921f7d9958

scratch/k16_l57614_motif820_c4_materialization_20260729.audit.json
SHA-256 da10a5e3552cb35090f43d72b6b7919b04495e13a5c3b05a7fe109b60df58758
```

All replays use only the Python standard library and frozen local factor
helpers.  They perform bounded provider enumeration or deterministic `O(W)`
factor audits; no SAT, CP, LP, remote job, or sustained search is used.
