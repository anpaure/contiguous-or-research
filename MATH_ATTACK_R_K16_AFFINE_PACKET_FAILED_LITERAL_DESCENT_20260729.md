# Lane R: affine packet obstructions and a q1-exact failed-literal descent

Date: 2026-07-29

## 1. Fixed objects and exact potential

Fix the residence-clean PBBS endpoint

```text
R = scratch/k16_pbbs_oriented_noaa_softq1_resume1_20260729.json
SHA-256 d28491b708d5a83e8abcde20fda8ad523cd58f9c662f46ae2d9c2507ba73e951
```

and the three saved zero-unit-core q1 factors

```text
Q0  scratch/k16_q1_endpoint_resume1_zero_full_unit_cores_20260729.json
    SHA-256 6f614ae41d1264121acc7cfb1b3303f3bb93532d57aeac1d0153e3f344a73f53
Q1  scratch/k16_q1_endpoint_resume1_zero_full_unit_cores_candidate1_20260729.json
    SHA-256 7435b0f27e035e2eec87ec5afe47130fd2d08da3bcee70669a4189f4bb7d6dff
Q2  scratch/k16_q1_endpoint_resume1_zero_full_unit_cores_candidate2_20260729.json
    SHA-256 ce17d15a6474cf20108412a6b255a91b8bab7566a27bbedf75dad8eb1002d738
```

For a fixed pair `(Q,R)`, let a blue variable be one when its edge in
`Q\R` is removed, and let a red variable be one when its edge in `R\Q` is
added.  The exact overlay rows are:

1. equal selected red and blue degree at every middle vertex;
2. at least one retained provider of every physical lower and upper q1
   colour;
3. at least one removed blue edge from the closure of every positive run of
   length at most three in `Q`.

All rows have coefficients in `{-1,+1}`.  Run exact unit propagation on all
of them.  Among the still-unhit motif rows having exactly two live blue
variables, take the union `B_2` of those variables.  Define

\[
 \Phi(Q,R)=\#\{x\in B_2:
   \text{both assumptions }x=0\text{ and }x=1
   \text{ unit-propagate to contradiction}\}.
\]

This is the **full two-choice failed-literal potential** used below: every
variable in `B_2` is probed, not sampled.  If `Phi>0`, the exact overlay is
infeasible.  The converse is false; `Phi=0` is only a necessary gate.  The
definition is tied to this fixed overlay row system and is not a canonical
graph invariant.

For `Q1/R`, the baseline is

```text
short motifs                 2250
unhit two-choice motifs       516
candidate bank |B_2|          979
failed literals Phi            93
factor components                4
short-run violations          2250
```

## 2. Why zero unit cores do not suffice

### Theorem 2.1 (common nine-row affine IIS)

Each of `Q0/R`, `Q1/R`, and `Q2/R` contains the same literal coordinate-11
length-two closure

\[
 \{(62050,64034),(62514,63538),(63538,64034)\}.
\]

Only its component, start, and numerical motif index change.  Put

\[
\begin{aligned}
x&=b_{(63538,64034)},&
y&=b_{(62050,64034)},&
z&=b_{(62514,63538)},\\
a&=r_{(63526,64546)},&
b&=b_{(63526,63750)},&
c&=r_{(61486,63526)},\\
d&=b_{(59438,63526)},&
p&=r_{(61554,63538)},&
q&=r_{(48178,63538)}.
\end{aligned}
\]

The four exact rows

\[
 x-a\le0,qquad b\le0,qquad c+a-d-b\le0,qquad d-c\le0
\]

sum to `x<=0`.  The motif row and four further exact rows

\[
 -y-z-x\le-1,quad y\le0,quad z-p\le0,quad z-q\le0,quad
 p+q-z-x\le0
\]

sum to `-2x<=-1`.  Twice the first sum plus the second is `0<=-1`.
Thus all three fixed overlays are infeasible already over the reals.

The nine-row subsystem is inclusion-minimal: deleting any one displayed row
admits a Boolean assignment to these nine variables.  This is not a claim
that nine is the globally minimum cardinality of every possible IIS.

### Theorem 2.2 (common two-motif packet)

The same three overlays also share the inherited closures

\[
\begin{aligned}
C_A&=\{(7526,7782),(7526,15714),(15466,15714)\},\\
C_B&=\{(47458,63810),(48210,63570),(63570,63810)\}.
\end{aligned}
\]

Fifteen exact palette/degree rows sum to

\[
 H_A+y\le h,qquad H_B+d\le y,
\]

where `H_A` and `H_B` are the sums of the two removable blue variables in
the corresponding closure,

```text
y = red  (48450,63810)
h = blue (15686,15698)
d = red  (57678,61766).
```

The two motif rows give `H_A>=1,H_B>=1`; the Boolean bounds give `d>=0` and
`h<=1`.  Summing yields `0<=-1`.  Equivalently, this is the negative
difference-constraint triangle

\[
 h\longrightarrow y\longrightarrow0\longrightarrow h
\]

with weights `-1,-1,+1`.  It is a two-demand-versus-one-capacity Hall
packet, again valid over the reals.

Consequently the reported absence of static, saturation, and ordinary unit
cores is strictly weaker than overlay feasibility.  A trade breaks this
particular packet exactly when a motif row changes/disappears or the
recomputed aggregate inequality ceases to contradict the unit box.  Changing
a motif or row-port signature is necessary.  Within the literal-support C6
neighborhood studied below, contact with the current support is only the
defining census filter and is not sufficient to break the packet; an
arbitrary row-changing trade need not touch an old literal.

The audited common certificates are

```text
scratch/k16_three_zero_unit_candidates_common_affine_core_20260729.audit.json
SHA-256 ed29297b30542d4c6311748bc9692e8ff1eebb8a91034244bdaafe4882317a8c

scratch/k16_three_zero_endpoints_common_two_motif_packet_20260729.audit.json
SHA-256 7b064e048c7a2594ce661e15dc73fc1a1216a9aed909bac9466d8e635cac893b
```

## 3. Complete raw-row-support C6 census at `Q1`

Take the literal edge support of the two certificates in Section 2.  The
possible distinguished deleted Q-edges are

```text
(7526,7782)     (7526,15714)    (15466,15714)  (15686,15698)
(47458,63810)   (48210,63570)   (59438,63526)  (62050,64034)
(62514,63538)   (63526,63750)   (63538,64034)  (63570,63810)
(15403,15459)   (15686,23878)   (42318,57678)  (47430,48450)
(48226,48450)   (58182,61766)   (61710,61766)
```

and the resident-only red variables in that same literal support are

```text
(48178,63538)   (48450,63810)   (57678,61766)  (61486,63526)
(61554,63538)   (63526,64546)   (15459,15970)   (15686,15716)
(15686,46406)   (40290,48450)   (61766,63810).
```

Enumerate every connected alternating C6 containing at least one of these
thirty distinguished edges, using both orientations.  Canonicalizing by the
sorted deleted and added triples gives the exact counts

```text
per-target incidence count       7213
distinct physical C6s            6775
lower/upper-q1-cover preserving    17
ordinary-unit contradictions        2
```

For the remaining fifteen trades the full failed-literal score histogram is

```text
86^1, 87^1, 88^1, 89^4, 90^1, 91^5, 93^1, 95^1.
```

This is complete for C6s containing a **current literal** of the two frozen
certificates.  It is not an enumeration of a C6 which avoids all current
literals but inserts a previously absent, nonresident blue provider into one
of the same labelled rows, nor of larger alternating circuits.

Thus support contact alone can be neutral or harmful, but the neighborhood
contains a strict descent.  The unique score-86 trade is

```text
delete (53986,62114), (55843,55970), (62050,64034)
add    (53986,55970), (55843,64034), (62050,62114).
```

It is a physical alternating C6.  Its lower q1 label multiset is unchanged:

```text
53922, 55842, 61986.
```

On the upper shore it retains `62178` and replaces `55971,64098` by
`56034,64035`; literal replay still covers every upper colour.  The factor
has exactly two components of lengths `106,12764`, no lower or upper q1
hole, and `2248` short runs.  It removes five old motifs, creates three, and
reduces

\[
 (\Phi,\mathrm{Res},\#\mathrm{components})=(93,2250,4)
       \longmapsto(86,2248,2).
\]

The complete census and the independently replayed factor are

```text
scratch/k16_candidate1_full_support_c6_failed_literal_potential_20260729.audit.json
SHA-256 37d4d717f99c48a953e55c2da5c6a9b393a91c12f8bc0686f9f247344fd0772a

scratch/k16_candidate1_failed_literal_93_to86_c6_20260729.json
SHA-256 a7a72536ac236caa804686b5c3290c12b7b996e8e71423c2924d32d8119f33e8

scratch/k16_candidate1_failed_literal_93_to86_c6_fullbank_20260729.audit.json
SHA-256 bc870655f8bdd6778d2a311ffe325b0570b4702c78b33787061b10f5598cfea3
```

## 4. A commuting packet ladder

Besides the score-86 packet `C`, use

```text
A:
  delete (7525,8036), (7526,7782), (7781,15972)
  add    (7525,7781), (7526,8036), (7782,15972)

B_soft:
  delete (47458,63810), (60802,64770), (63778,63874)
  add    (47458,63778), (60802,63874), (63810,64770)

B_hard:
  delete (47395,55587), (47458,63810), (55619,63747)
  add    (47395,47458), (55587,55619), (63747,63810).
```

The supports of `C`, `A`, and either chosen B-packet are pairwise
vertex-disjoint, so the corresponding factor switches commute.  Complete
q1 replay is still required because disjoint physical support does not by
itself preclude a shared palette label.  That replay gives the exact ladder

| packets | radius | `Phi` | short runs | components |
|---|---:|---:|---:|---:|
| none | 0 | 93 | 2250 | 4 |
| `C+B_soft` | 6 | 84 | 2247 | 3 |
| `C+B_soft+A` | 9 | 82 | 2248 | 2 |
| `C+B_hard` | 6 | 80 | 2249 | 4 |
| `C+B_hard+A` | 9 | 78 | 2250 | 3 |

Every displayed state is a simple spanning degree-two Johnson factor and
has zero lower/upper q1 holes.  Hence the full failed-literal potential is a
genuine constructive descent potential in this neighborhood; it is not
merely a post-hoc diagnosis.

The final lexicographic state is

```text
scratch/k16_candidate1_failed_literal_packet_ladder_20260729/phi78_res2250.json
SHA-256 ec43b81023def5c1bca8116fe1325d5a2eee1f7c89ec9aa5d04f6c38adb6d2db
```

and the full four-state ledger is

```text
scratch/k16_candidate1_failed_literal_packet_ladder_20260729.audit.json
SHA-256 8dfa6dad61a3c04593e5a507ab51cb427d071591fa9556c3fd6464a7229271e3
```

## 5. Exact boundary after the descent

The score-78 state is **not feasible**.  Its exact full-bank replay has

```text
unhit two-choice motifs       519
candidate bank               983
failed literals               78
minimum displayed core union  10 rows
```

and is frozen at

```text
scratch/k16_candidate1_failed_literal_packet_ladder_20260729/phi78_res2250.fullbank.audit.json
SHA-256 aab9ef7d0d59627238901d283561f0f1574e7590cc28fc0d3f2f5b9846dc5cfd
```

One smallest remaining displayed core uses the coordinate-3 length-two
closure

\[
 \{(41395,41401),(41401,42409),(42409,46497)\}
\]

and the remote `42417` palette/degree socket.  This is the next natural
support bank; no feasibility claim is made for it here.

Any resident pretrade that leaves the provider and incidence signatures in
the two common certificates of Section 2 unchanged leaves their
contradictions verbatim.  Thus a useful resident move must change a common
packet port, not merely a candidate-specific local socket.

The proved boundary is therefore:

1. all three supplied zero-unit-core endpoints are infeasible against fixed
   `R`, by explicit real-linear certificates;
2. the complete raw-row-support C6 neighborhood of `Q1` contains an exact
   q1-preserving descent, and three commuting packets give `Phi 93->78`
   without worsening total residence;
3. `Phi=78>0`, so neither an overlay, an all-depth carrier, `COMP3`, nor a
   literal k16 word has been constructed;
4. the next valid move must attack a remaining failed-literal core or alter
   the corresponding resident provider/incidence ports.  Returning to the
   zero-unit-core score would discard decisive information.

All enumeration, propagation, and replay in this note was deterministic and
local-light.  No H100 job, SAT/CP solve, web query, or GPU work was launched
under the active memory/swap moratorium.
