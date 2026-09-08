# Literal lineage of the solved even optima and the splice savings

Date: 2026-07-31  
Status: deterministic positive-certificate audit  
Scope: the retained \(k=10,12,14,16\) words and their authenticated seeds

## 1. Result

For an odd parent word \(X\) on \(k-1\) coordinates, the closed-form even
splice is

\[
             X\;\Vert\;[z]\;\Vert\;(z\cup X[0:-1]).
\tag{1.1}
\]

It has length \(2|X|\) and is universal. The audit reconstructs (1.1)
from each canonical parent, verifies it literally, and compares it with the
retained even optimum.

| child \(k\) | parent length | naive length | answer length | shaved \(q\) |
|---:|---:|---:|---:|---:|
| 10 | 128 | 256 | 254 | 2 |
| 12 | 465 | 930 | 926 | 4 |
| 14 | 1,719 | 3,438 | 3,434 | 4 |
| 16 | 6,438 | 12,876 | 12,873 | 3 |

The saving is not a list of \(q\) deletions from the canonical splice. It
is a global boundary-overhead compression around a newly constructed middle
deck.

## 2. Exact owner-surplus ledger

Let \(r=k/2\). Starting at every physical position, stop when the running
OR first has rank at least \(r\). A start is:

* a **delivery** when that first rank is exactly \(r\);
* a **jump** when it is larger than \(r\); or
* a **stall** when the suffix never reaches \(r\).

All eight audited words—the four splices and four answers—deliver every one
of the

\[
                         W_k=\binom{k}{r}
\]

middle labels. If \(R\) is delivery-repeat excess, \(J\) the jump count and
\(S\) the stall count, then tautologically

\[
                  |A|-W_k=R+J+S.                         \tag{2.1}
\]

The literal census is:

| \(k\) | splice \((R,J,S)\) | splice surplus | answer \((R,J,S)\) | answer surplus | removed surplus |
|---:|---:|---:|---:|---:|---:|
| 10 | \((1,2,1)\) | 4 | \((1,0,1)\) | 2 | 2 |
| 12 | \((4,0,2)\) | 6 | \((1,0,1)\) | 2 | 4 |
| 14 | \((3,2,1)\) | 6 | \((1,0,1)\) | 2 | 4 |
| 16 | \((5,0,1)\) | 6 | \((3,0,0)\) | 3 | 3 |

Write the odd-parent length as \(W_{k-1}+d_{k-1}\), where
\(W_k=2W_{k-1}\), and write the answer length as \(W_k+d_k\). Then

\[
 q=2(W_{k-1}+d_{k-1})-(W_k+d_k)
   =2d_{k-1}-d_k.                                      \tag{2.2}
\]

The four identities are

~~~
k10: 2*2 - 2 = 2
k12: 2*3 - 2 = 4
k14: 2*3 - 2 = 4
k16: 2*3 - 3 = 3.
~~~

Thus every shaved unit is accounted for literally as one fewer physical
start that fails to introduce a new middle owner. This is a counting
ledger, not a claim that a particular splice cell can be deleted.

The repeated answer-tail labels are:

~~~
k10: 0x00c7, multiplicity 2; one final stall
k12: 0x0371, multiplicity 2; one final stall
k14: 0x351a, multiplicity 2; one final stall
k16: 0xf30c, multiplicity 4; no stall.
~~~

## 3. Literal \(D^{d(k)}\) audit

For \(k=10,12,14\), ordinary uniform erosion is exact:

| \(k\) | \(d(k)\) | \(D^{d(k)}A\) rank distribution | distinct | Johnson edges | minimum internal one-run | flat run deficit |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 2 | \(5^{252}\) | 252 | 251/251 | 3 | 0 |
| 12 | 2 | \(6^{924}\) | 924 | 923/923 | 3 | 0 |
| 14 | 2 | \(7^{3432}\) | 3,432 | 3,431/3,431 | 3 | 0 |

In each case the adjacent intersections cover the complete rank-\((r-1)\)
layer, the triple intersections cover the complete rank-\((r-2)\) layer,
and all upper union layers are complete.

The complete derivative rank distributions, including the lower rows, are:

~~~
k10:
 D0 {1:16,2:90,3:144,4:4}
 D1 {3:15,4:236,5:2}
 D2 {5:252}

k12:
 D0 {1:20,2:137,3:262,4:507}
 D1 {3:9,4:46,5:868,6:2}
 D2 {6:924}

k14:
 D0 {1:22,2:156,3:455,4:1018,5:1782,6:1}
 D1 {3:3,4:45,5:260,6:3124,7:1}
 D2 {7:3432}
~~~

### K16 is genuinely variable-depth

The literal uniform derivatives of "answers/k16.word" are:

~~~
D0 {1:17,2:127,3:604,4:2037,5:6824,6:3260,7:3,8:1}
D1 {3:4,4:45,5:360,6:6691,7:5770,8:2}
D2 {7:6483,8:6388}
D3 {8:6484,9:6386}.
~~~

Hence \(D^3A\) is not the rank-eight carrier. The exact schedule uses all
starts \(0,\ldots,12869\), deletes deadlines

~~~
0, 1, 6388,
~~~

and has span histogram

~~~
3:6386, 4:6484.
~~~

Its middle row is exactly

\[
 D^2A[0:6386]\;\Vert\;D^3A[6386:],
\tag{3.1}
\]

which is the authenticated rank-eight Hamilton carrier. The maximal
envelope ranks are

~~~
5:6481, 6:6388, 7:2, 8:2,
~~~

the decoded answer is pointwise below those envelopes, and physical position
6389 is the pinned singleton "0x8000".

The rank-eight carrier itself has all 12,869 Johnson edges, complete lower
intersection decks through the required depth three, and all upper union
decks. Its ordinary flat
depth-three run deficit is 1,423; this is not a defect in the certificate,
because the certificate uses the nonuniform schedule (3.1).

## 4. Why the canonical splices are not the archived answers

The canonical splice hashes are:

| \(k\) | canonical splice SHA-256 |
|---:|---|
| 10 | "6bf207c18e3ff36393571bb64dba28f4db043161c06b087e4a3ede0147dc5572" |
| 12 | "01be061700fc5a887233736f79fe17547fbbb35b329e28bcf0ce4872db551ca0" |
| 14 | "882d29f01c7ea334981508738a4f612f73113a0022c5697595f4319b80c8ae61" |
| 16 | "9d0214f6c7cea45a1f26d031687ecada9ac34500e925dcfc127bdf1514b624c8" |

After deleting the required \(q\) cells, the rank histograms alone force at
least

~~~
k10:   77 substitutions
k12:  188 substitutions
k14:  958 substitutions
k16: 1233 substitutions
~~~

to obtain the archived answers, even if positions are reordered and
coordinates relabelled. Therefore the answers are not deletion-only
versions of these literal splices.

This statement is intentionally scoped. It does **not** say that no other
multi-deletion subsequence of a splice can be universal: deleting additional
cells creates new adjacencies, so coverage is not monotone under subsequence
deletion.

The undirected owner-edge overlap between the canonical splice chronology
and the answer carrier is:

~~~
k10:    19 / 251
k12:    57 / 923
k14:  1781 / 3431
k16: 12861 / 12869.
~~~

## 5. The four literal seed/deck mechanisms

### K10: one-exception derivative deck, followed by a global rethread

For "answers/k09.word",

~~~
D1 ranks = {3:1,4:126}
D2 ranks = {5:126}.
~~~

The unique low row is \(D^1[22]=\mathtt{0x091}\), of rank three. Removing
it leaves every rank-four mask exactly once, while \(D^2\) contains every
rank-five mask exactly once. Interleaving the two shores

\[
         (z\cup\text{rank-four }D^1)\quad\text{and}\quad D^2
\]

reconstructs "k10_middle_path_seed.txt" exactly.

The deck identity is perfect but its order has depth-two run deficit 248.
The answer carrier has the same 252 vertices but only 18 of the seed's 251
undirected edges. The useful late predecessor "central_path_966.txt"
already shares 234 edges with the final carrier. Thus K10's two saved cells
are paid by a direct global rethread into one depth-two carrier—not by a
favourable depth drop or a deletion from the splice.

### K12: completed intersection shore and the depth drop \(3\to2\)

The historical source was "k11_lower956_upper549.txt", not today's
"answers/k11.word". It is a complete rank-six deck. Its adjacent
intersections contain every rank-five mask except "0x01f"; inserting that
endpoint-accessible hole and lifting the completed row by the new coordinate
reconstructs "k12_lift_from_k11_upper549.txt" exactly.

The lift and final carrier share 773 of 923 undirected edges. The lift has
one unit of depth-two run deficit; the final \(D^2\) carrier has zero and
complete shadows. Here the source depth three drops to child depth two, so
the intersection shore is nearly resident and the repair shares one global
two-cell child boundary instead of two three-cell parent boundaries.

The later six-piece K12 word is a distinct optimum and must not be conflated
with the archived answer.

### K14: the three-ear/two-port six-piece identity

Two authenticated K13 rank-seven paths supply the shores:

* after the recorded coordinate permutation, \(A\) is every rank-seven mask;
* reversing the B source, taking adjacent intersections, and appending its
  missing "0x151a" gives every rank-six mask; adding the new coordinate gives
  the \(B\) shore.

The strict \(A\Vert B\) path is cut at

~~~
A: after 418 and 1445
B: three-vertex ear beginning 966
~~~

and reassembled as

~~~
A1F B2R A3F B1F A2R B3F.
~~~

The B-ear cuts lose old colours "0x1b64" and "0x09ce". They occur exactly
at A positions 1445 and 419, so the two A cuts expose the precise ports that
restore the two lifted upper colours. All five new seams are Johnson.
The braid preserves 3,427 of the strict path's 3,431 undirected edges.

The depth drop \(3\to2\) makes the intersection shore resident; the internal
three-vertex B ear supplies the singleton slot. This exact local identity
is what permits the four-unit global boundary saving.

### K16: two exact views that must not be conflated

K16 has both an answer-only derivative anatomy and a construction/compiler
provenance. They describe different rows of the same certificate.

#### Promoted-answer anatomy: shifted chunks plus a 49-facet bridge

Let

\[
 T^{15}=D^3(\texttt{answers/k15.word}),\qquad
 T^{16}=D^3(\texttt{answers/k16.word}),\qquad z=2^{15}.
\]

The 6,435 entries of \(T^{15}\) are the complete rank-eight layer and split
literally into Johnson cycles of lengths 6,390 and 45. The top-bit trace in
the mixed-rank \(T^{16}\) is

\[
                         1^{6390}0^{6435}1^{45}.
\tag{5.1}
\]

After removing \(z\), the plain subsequence is exactly

\[
 T^{15}[5112:6390]\,T^{15}[0:5112]\,
 T^{15}[6426:6435]\,T^{15}[6390:6426],
\tag{5.2}
\]

while the marked rank-eight-parent portion is

\[
                    T^{15}[5113:6390],T^{15}[0:5109].
\tag{5.3}
\]

Thus the omitted parent middles are the four-vertex collar
\(T^{15}[5109:5113]\) and the whole 45-cycle
\(T^{15}[6390:6435]\). They are replaced, slot for slot, by four incoming
edge facets of the collar and all 45 edge facets of the small cycle, rotated
by 35. In the physical \(D^3\) row the four path facets occupy
\([6386,6390)\), the whole plain rail lies between them, and the 45 cycle
facets occupy \([12825,12870)\). The two facet blocks are internally Johnson,
but the consecutive-looking filtered join is not a physical Johnson edge.
All 49 facets are distinct. Their containment graph against the 49
omitted middles has 128 edges, degree profiles

\[
 1^1 2^{17}3^{31}\quad\hbox{and}\quad1^1 2^{18}3^{29}4^1,
\]

and a perfect matching of size 49. Independently, the distinct top-containing
rank-eight counts in \(D^0,D^1,D^2,D^3\) are

\[
                          1,2,6388,49,
\]

with new contributions \(1,1,6386,47\). The last two rows have complete
rank-seven union and intersection size two.

This proves the uniform depth-three profile

\[
 6435\text{ plain rank-8}+6386\text{ marked rank-9}
 +49\text{ marked rank-8}.
\tag{5.4}
\]

It is the literal content of the promoted-answer shifted-chunk theorem; no
construction checkpoint is used.

#### Construction provenance: four-filter deck and common-cap schedule

The construction source is

~~~
scratch/K15_FOURFILTER_SEED_20260731.word
SHA 51f57125ea3e145e08ed9d5f8816d22313a010907588457260c824c6f40217f4,
~~~

not "answers/k15.word". Its derivatives satisfy

~~~
D2 {6:1,7:6435}, all 6436 rows distinct
D3 {8:6435}, all rows distinct.
~~~

The unique low row is \(D^2[6390]=\mathtt{0x13c8}\). Removing it leaves the
complete rank-seven deck, while \(D^3\) is the complete rank-eight deck.
Therefore

\[
 \operatorname{reverse}(z\cup D^2[0:6390])
 \;\Vert\;D^3
 \;\Vert\;\operatorname{reverse}(z\cup D^2[6391:])
\tag{5.5}
\]

is exactly the full K16 rank-eight owner deck. Two endpoint reversals,
\([0,6388]\) and \([12826,12869]\), change only two undirected edges and
complete the upper palette. The final nonuniform staircase (3.1), together
with the pinned singleton, realizes this rank-eight deck with spans three
and four. This scheduled owner deck is not the mixed-rank uniform row
\(T^{16}\) in (5.1)--(5.4).

#### The two exact counts

| quantity | value | what it counts | exact effect |
|---|---:|---|---|
| bridge size \(h\) | \(45+4=49\) | omitted rank-eight parent slots replaced by lower edge facets inside uniform \(D^3\) | slot preserving: 49 out, 49 in |
| compiler saving \(q\) | \(2\cdot3-3=3\) | physical cells saved from the canonical two-copy splice | length \(12876-12873=3\) |

There is no identity equating \(h\) and \(q\). The bridge changes the rank
types occupying 49 existing middle slots and explains the mixed-rank
chronology. The saving comes from fusing two parent three-cell halos into one
global three-cell child staircase. In particular, the facet bridge does not
delete 49 physical cells and is not the arithmetic explanation of \(q=3\).

## 6. Theorem versus solver provenance

The mathematical evidence used here is:

* byte-authenticated seed files and displayed deck transformations;
* literal answer words;
* exhaustive interval-OR replay;
* exact middle-deck, transition, run, and schedule identities.

Historical beam searches and SAT label models explain how some files were
found. They are not inputs to this audit and are not promoted as theorem
evidence. The positive decoded words and their independent literal replay
are the certificates.

No general odd-to-even recurrence follows from the four cases. K10 needs a
global rethread, K12/K14 exploit a depth drop, and K16 combines a selected
four-filter construction seed and variable-depth common schedule with the
promoted answer's independently visible 49-facet substitution anatomy.

## 7. Deterministic artifacts

The complete catalogue is generated by

~~~
scratch/audit_even_optimal_splice_shaving_lineage_20260731.py
~~~

and stored in

~~~
scratch/even_optimal_splice_shaving_lineage_20260731.audit.json.
~~~

The authoritative answer-only K16 anatomy and its independent replay are

~~~
MATH_THEOREM_K16_SHIFTED_CHUNK_FACET_SUBSTITUTION_ANATOMY_20260731.md
scratch/audit_k16_shifted_chunk_facet_bridge_20260731.py
scratch/k16_shifted_chunk_facet_bridge_20260731.audit.json.
~~~

The separate corrected K10/K12 provenance cross-audit is

~~~
scratch/audit_even_k10_k12_answer_lineage_20260731.py
scratch/K10_K12_ANSWER_LINEAGE_AUDIT_20260731.md.
~~~
