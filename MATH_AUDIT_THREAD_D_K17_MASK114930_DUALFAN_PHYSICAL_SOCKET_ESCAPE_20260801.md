# K17 round02 mask-114930 dual fan: physical decoding and exact socket-escape criterion

**Date:** 2026-08-01  
**Status:** proved for the frozen round02 q1 core; all one-cut local escapes independently replayed  
**Scope:** fixed-factor q1 socket exact cover only.  This note neither proves a
one-cut no-go nor claims residence, deeper shadows, topology, or compiler
completion.

## 1. Frozen inputs and independent replay

The replay uses

* `scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv`, SHA-256
  `7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df`;
* `scratch/k17_h2_two_cut_closure_20260801/k17_two_cut.candidates.tsv`, SHA-256
  `fa1133f5ffc8b70bf7d1713dfa930670508fb6bb6e1255d570f00ea851d00cc6`;
* `scratch/threadD_k17_mask114930_core_20260801/round02.bank.tsv`, SHA-256
  `48670b1bf5388ed4c8f47a408e4659c145ec26dc3d6a6bb31cd379a1e70ad649`;
* the extracted 139-clause core
  `scratch/threadD_k17_mask114930_core_20260801/round02.core.cnf`, SHA-256
  `354e3aef1fa6512c29409656a7ab93c1049759f33b9bd2852830cb77ce54f56f`.

The independent decoder is
`scratch/audit_threadD_k17_mask114930_dualfan_decode_20260801.cpp`, SHA-256
`7dbf003851d082cdc37fe61fb241546d0ac93c00a3d08e568caf03f100e49c6a`.
It reconstructs the 7,612 pieces from the factor, the 20,477-cut catalogue,
and the selected bank; it does not trust serialized physical-piece numbers.
Its structured output is
`scratch/threadD_k17_mask114930_core_20260801/round02.physical_decode.audit.json`,
SHA-256
`8befed64f3f6ce148424a4933991a016a128ad049e0c012ff98719be28c7e7a5`.
The extracted core itself is independently `UNSATISFIABLE` under Kissat.
The existing DRAT replay reports 139 original clauses, 45 lemmas, 1,851
resolution steps, and no RAT lemma.

## 2. Canonical owner-mask decoding

Let

\[
 c=114930=\texttt{0x1c0f2}
   =\{1,4,5,6,7,14,15,16\},
\]

where coordinates are zero based.  Its colour index in the selected-cut
palette is 6961; that number is not physical piece 6961.

Reconstruction gives the two central physical sockets

\[
 \begin{aligned}
 s&=115442=c\cup\{9\}=\texttt{0x1c2f2},\\
 t&=115186=c\cup\{8\}=\texttt{0x1c1f2}.
 \end{aligned}                                                    \tag{2.1}
\]

Their serialized locations, now backed by masks, are:

| socket | physical piece | base piece | selected cut | side | path length |
|---|---:|---:|---:|---:|---:|
| `s` | 3669 | 1834 | 9924 | 1 | 8 |
| `t` | 3670 | 1835 | 9933 | 0 | 2 |

In both pieces the displayed socket is the terminal endpoint in stored
orientation 0 and the initial endpoint in orientation 1.  Consequently it
is an outgoing socket in orientation 0 and an incoming socket in orientation
1.  Thus choosing either orientation still requires exactly one seam at the
same physical socket.

The physical leaf sockets occurring in the core are

\[
 c\cup\{0\},\ c\cup\{3\},\ c\cup\{12\},\ c\cup\{10\},\
 c\cup\{13\},\ c\cup\{11\},                                  \tag{2.2}
\]

at pieces 1827, 2198, 3370, 3671, 5585, and 7423 respectively.
Every core seam incident with `s` or `t` has lower colour `c`.

There is no literal `s--t` seam in the full q1 atlas.  Geometrically it
would be the Johnson seam

\[
 s\cap t=c,\qquad s\cup t=115698=\texttt{0x1c3f2}.             \tag{2.3}
\]

It is excluded by exact two-block residence: coordinate 1 has endpoint ages
`2+1=3` from `s` to `t`, and `1+2=3` in reverse, whereas depth 3 requires at
least 4.  Neither block is all-one in that coordinate.

### Index-extraction correction

The first line `139 69 0` in `round02.core.orientations.tsv` is spurious.
The integer 139 is the clause count in the DIMACS header
`p cnf 892058 139`; variable 139 does not occur in the core body.  The actual
piece-orientation variables in the core are only

\[
 (7339,7340)\leftrightarrow3669,
 \quad(7341,7342)\leftrightarrow3670,
 \quad(14847,14848)\leftrightarrow7423.                         \tag{2.4}
\]

All physical conclusions below use endpoint masks, not that extracted row.

## 3. Exact dual-fan contradiction

Contract the forced rows and leaf implications retained by the DRAT core.
For either orientation of piece 3669, one selected seam must meet socket
`s`: it is outgoing in orientation 0 and incoming in orientation 1.  The
same argument forces one selected seam at `t` for either orientation of
piece 3670.

Every surviving seam at either central socket has colour `c`, and no seam
meets both `s` and `t`.  Socket matching therefore needs two distinct seams
of colour `c`, while the lower-colour exact-one row permits only one.  In
the socket-versus-colour quotient this is exactly

\[
       Y=\{s,t\},\qquad N(Y)=\{c\},\qquad |Y|=2>|N(Y)|=1.       \tag{3.1}
\]

This proves the dual-fan interpretation.  It is not a shortage of raw
`c`-providers: the full atlas has directed `c`-degree 80.

## 4. Necessary-and-sufficient local socket escape

The right one-cut statistic is a two-socket rainbow matching rank, not the
degree of `c`.

Fix any changed cut bank `D`.  Rebuild its physical socket atlas and apply
the same protected-row restrictions and forced contractions used to define
the local core face.  Let `G_D` be the resulting graph whose vertices are
physical socket occurrences and whose edges are resident-legal seams,
labelled by their selected lower colour.  Socket occurrences, rather than
owner masks or pieces, are the vertices; in particular the two sockets of a
singleton piece remain distinct resources.

For `Y={s,t}`, define

\[
 \rho_D(Y)=\max_M\left|Y\cap\bigcup_{e\in M}e\right|,           \tag{4.1}
\]

where `M` ranges over sets of pairwise socket-disjoint seams having pairwise
distinct colour labels.

### Theorem 4.1 (exact two-socket escape criterion)

Assume the changed bank still exposes the two owner-mask sockets `s` and `t`
as the corresponding forced central sockets.  Then it destroys the local
dual-fan certificate (3.1) if and only if

\[
                         \rho_D(\{s,t\})=2.                    \tag{4.2}
\]

Equivalently, at least one of the following holds:

1. there is one resident-legal seam whose endpoints are exactly `s,t`;
2. there are seams `e_s` at `s` and `e_t` at `t` with distinct colour
   labels and distinct outside socket endpoints.

If a rethread makes `s` or `t` internal, or moves the forced endpoint role
to another owner occurrence, then the old certificate is also destroyed;
one applies (4.2) to the new forced-socket pair to test for a replacement
dual fan.

#### Proof

A local socket matching covering two named sockets either uses one edge
covering both, which is item 1, or uses two different edges.  In the latter
case socket matching forces their outside endpoints to be distinct and
rainbow exactness forces their labels to be distinct, giving item 2.
Conversely either item is itself a rainbow socket matching covering `Y`.
This is precisely (4.2).  If an old named socket ceases to be externally
required, (3.1) is no longer a constraint on the changed instance. \(\square\)

The theorem is necessary and sufficient for eliminating this *local
certificate*.  It is only necessary, not sufficient, for extending the
choice through the rest of the global q1 exact cover.

## 5. Consequence for one-cut auditing

The completed 16,667-move census establishes only

\[
 13043\text{ zero-265-preserving moves},\qquad
 \Delta\deg_D(c)\le 0\text{ for all of them}.                  \tag{5.1}
\]

Equation (5.1) does not decide (4.2).  In particular:

* a new non-`c` seam at `s` or `t` can make item 2 true while
  `deg_D(c)` is unchanged;
* a count-neutral replacement can create the direct `s--t` seam in item 1;
* changing an endpoint role can remove the old fan without adding any
  provider;
* conversely, adding another leaf provider of colour `c` does not help:
  the two sockets still compete for one colour ticket.

A proof-safe one-cut socket audit must therefore, for each protected
zero-265-preserving bank:

1. reconstruct the two central socket occurrences by owner masks;
2. detect endpoint-role relocation;
3. enumerate all literal resident seams incident with the surviving pair,
   with their physical outside sockets and colour labels;
4. evaluate the explicit two-vertex condition in Theorem 4.1; and
5. for every local escape, rebuild and solve the full q1 formula before
   claiming a q1 repair.

This audit is now complete at the *local-certificate* level.  The corrected
Lane-L scan over all 16,667 substitutions finds, among the 13,043 zero-265
children,

\[
 \begin{array}{c|c}
 \text{different-colour socket escapes}&12\\
 \text{direct resident }s\text{--}t\text{ seams of colour }c&0\\
 \text{zero-265-clean true endpoint-role relocations}&0.
 \end{array}                                                     \tag{5.2}
\]

The twelve rows are frozen in
`round02.socket_escape_v2.tsv` (SHA-256
`88893f08ea810662df0ef44be9d227ad53ff19485f27034d8827c6083f6b29ef`).
The independent literal replay source
`scratch/audit_threadD_k17_round02_dualfan_socket_escape_20260801.cpp` has
SHA-256
`125c66d4e258fffbc3c60d55538cca78912f96ff76d30a8d03896f8cf29a9a28`.
Their exact socket/colour ledger is:

| base piece | cut replacement | escaped socket | new lower colour |
|---:|---:|:---:|---:|
| 540 | `2838->2842` | `t` | 115122 |
| 3680 | `19815->19818` | `t` | 98802 |
| 1284 | `6831->6832` | `s` | 82674 |
| 3613 | `19443->19445` | `t` | 115058 |
| 1379 | `7364->7380` | `t` | 115154 |
| 1801 | `9773->9771` | `s` | 99058 |
| 3254 | `17426->17428` | `t` | 49650 |
| 1532 | `8180->8181` | `s` | 115378 |
| 2251 | `12065->12067` | `t` | 115170 |
| 3029 | `16232->16234` | `s` | 115410 |
| 3344 | `17953->17957` | `t` | 82418 |
| 2251 | `12065->12066` | `s` | 115426 |

An independent owner-mask replay verifies all 12 scores and 92 directed
non-`c` seam occurrences, collapsing to 12 move/socket/colour triples.  Its
detail, explicit matching-witness, and audit hashes are respectively
`0c3f844d19a04ee42e644ca7af5ec460e5418c55c05c419d359be3d1effe6128`
,
`e55eb587014a3a94c099050e34d4e0dad3da2df96309fc69e822a36e9caefab2`,
and
`acd445b17f288de6d60f51b9b95b8bbd2868f2589f321501e5f8b6e4222427d4`.

Each row really satisfies Theorem 4.1, rather than merely exposing a
different label.  The changed base pieces in the table are disjoint from
the six core-leaf bases `913,1099,1685,1835,2793,3712`; hence every old
114930 arm at the opposite central socket survives.  That opposite star has
at least five distinct physical leaf sockets.  At most one can coincide
with the outside socket of the new arm, so a disjoint old 114930 arm exists.
The two labels are different by construction.  The replay emits one literal
pair for every row and checks all twelve pairs directly.

There is exactly one true central endpoint-role-changing substitution,
base 1835 cut `9933->9932`; it replaces colour 114930 by 115184 but has
`bad=1`, solely one common-orientation zero, so it is not zero-265-clean.

It is essential here not to define a socket role by the entire path behind
it.  Eight other substitutions change the `(outer owner,length)` path
signature while retaining the same terminal socket owner.  The apparent
clean example `base1834:9924->9923` merely changes the `s`-ending path from
length 8/outer 64081 to length 9/outer 129601; owner 115442 remains the same
terminal socket.  Those are path-signature changes, not role relocations.

Thus round02 is **not** a one-cut-stable local core.  Whether any of the 12
children satisfies the full q1 exact cover is a separate solver question.
In particular no two-cut, C6, C8, or higher-order necessity follows from
this core.
