# Independent proof-carrying audit of K17 packets 3836 and 919

Date: 2026-07-31  
Status: exact replay PASS in the augmented occurrence/common-core scope; **not**
a full ordered four-transversal or a K17 carrier certificate.

## 1. Independence and provenance

The audit script

`scratch/threadD_independent_audit_k17_commonext_packets_3836_919_20260731.py`

reconstructs the source factor directly from the frozen component cycles.  It
does not import either the common-exterior catalogue builder or its replay.
Its SHA-256 is

`09ed27ca81302477545c55bc793f51cc2859612a17e77479c1a081d15ecbc2d8`.

The source component SHA-256 is

`3f663cd2117ad6096b4cc9e6bc9d6fcf881382b4ee546dc64219bf94aafd5f2e`.

The packet-file hashes are

* serial 3836: `1b309fecc60e4631c1e8f301437992f5995781c7285f7819aab53a42ffed773a`;
* serial 919: `93617348dfc7b01673236dab22879a99a78b4b9ee06817255d97933951eec9a2`.

The 1,297-colour shared-shell file has SHA-256

`3d66f121f819f2954d377bf454d699aa68263335ed6f64b5e908680dac53378d`.

The proof-carrying output is

`scratch/threadD_k17_commonext_packets_3836_919_independent_20260731.audit.json`,

file SHA-256

`1bfb7c83f8431f6dffd7ef3b2b36d2dde45a0aec3d0225c80cbfcf467f7eb2a8`,

with canonical payload SHA-256

`ad6cdd48e0a81304b1c0fc61ce5691718f3d8022066a231b1ae22c6da2448da4`.

The single capped H100 run used one CPU, 2.72 seconds wall time, and 194,224
KiB peak RSS.  Its stdout/stderr are frozen under the unique
`scratch/threadD_k17_packet3836_919_independent_20260731.run.*` names.

## 2. Literal factor reconstruction

The eleven input lines partition all

\[
\binom{[17]}9,
\]

and close cyclically to a 24,310-edge Johnson 2-factor.  For every tested
packet the audit removes exactly the five advertised edges and inserts exactly
the five advertised edges, then reconstructs all degrees and components from
scratch.

For both packets:

1. every candidate owner has degree two;
2. every candidate edge is Johnson;
3. edge intersections use every rank-8 mask exactly once;
4. the complete rank-10 edge-union multiset is unchanged, and in particular
   remains surjective;
5. lower turns are recomputed as the rank-7 triple intersections at the
   24,310 owners.

The source component orders are

\[
3,7,64,98,134,970,3070,4139,4907,5382,5536.
\]

## 3. Packet 3836

The candidate has component orders

\[
3,7,64,98,134,335,970,4139,18560.
\]

It loses no lower-turn colour and gains exactly

\[
0x9435,\quad 0x949c,\quad 0x9515,\quad 0x1111d.
\]

The first three lie in the frozen 1,297-colour common shell; the last does not.
Thus lower-turn holes decrease from 3,826 to 3,822.

In the augmented occurrence graph, the independently certified ranks are

\[
\rho(G_0)=39624,\qquad
\rho(H)=39622,\qquad
\rho(G_1)=39628.
\]

Equivalently, the deficiencies are (4134,4136,4130).  The JSON contains an
explicit matching and an explicit vertex cover of the same size for each
graph, together with the alternating Hall witness.  Hence each rank is
independently checkable by Konig's theorem.  The symmetric difference of the
exported common and candidate matchings has exactly six vertex-disjoint
augmenting components and no deaugmenting component, certifying

\[
4130=4136-6.
\]

The occurrence deficiency improves by four, exactly matching the four-colour
support gain.  Consequently the correlation excess remains (308); this
packet raises support but does not reduce that excess.

## 4. Packet 919

The candidate has component orders

\[
3,7,98,134,970,2097,4139,4907,11955.
\]

It loses no lower-turn colour and gains exactly

\[
0x2aac,\quad 0xa8aa.
\]

Only (0x2aac) lies in the frozen common shell.  Lower-turn holes decrease
from 3,826 to 3,824.

The independently certified occurrence ranks are

\[
\rho(G_0)=39624,\qquad
\rho(H)=39623,\qquad
\rho(G_1)=39627,
\]

with deficiencies (4134,4135,4131).  Four explicit vertex-disjoint
common-to-candidate augmenting components certify

\[
4131=4135-4.
\]

Here matching rank improves by three while support improves by two, so the
correlation excess decreases from (308) to (307).  This is the sharper
integral-correlation packet of the pair.

## 5. Exact scope

The augmented occurrence graph has left shore

\[
\{\text{rank-8 A-slots}\}\sqcup\{\text{rank-7 lower-turn colours}\}
\]

and right shore

\[
\{\text{rank-9 B-owner slots}\}\sqcup\{\text{rank-10 upper-turn colours}\}.
\]

The exported matching/cover certificates prove the exact common-core Hall
ranks in this graph.  They do **not** supply the other typed rails of an
ordered four-transversal, nor residence, deeper shadows, a compiler, or a K17
word.  In particular, the old-rail atoms visible in these packets must not be
reported as full four-transversals.
