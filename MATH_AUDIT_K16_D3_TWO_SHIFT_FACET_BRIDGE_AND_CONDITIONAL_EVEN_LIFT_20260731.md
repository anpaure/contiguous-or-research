# K16 two-shift facet bridge and a conditional variable-staircase even lift

Date: 2026-07-31  
Lane: K, downstream RSB / odd-to-even lift  
Status: exact solver-free K15--K16 anatomy; exact sufficient lift theorem;
no all-dimension existence claim

## 1. Verdict

The newly observed structure in the authenticated optimal words is exact.
Put

\[
 A=\texttt{answers/k15.word},\qquad
 B=\texttt{answers/k16.word},\qquad z=2^{15},
\]

and write \(D^q\) for the OR of \(q+1\) consecutive letters.  Then
\(T=D^3A\) is a 6,435-term permutation of the rank-eight sets on the old
15 coordinates.  It is naturally split into Johnson cycles of lengths
6,390 and 45.  The 12,870 values of \(D^3B\) are distinct and have rank
histogram

\[
                         8^{6484}9^{6386}.                 \tag{1.1}
\]

After separating the values according to whether they contain \(z\), and
deleting \(z\) on the marked side, each side has 6,435 terms.  The unmarked
side is exactly two independently rerooted parent cycles.  The marked side
is 6,386 parent owners followed by a 49-facet bridge.

The numerical constants now have an exact explanation.

* The two displayed marked shifts differ by

  \[
                         5158-5113=45,                       \tag{1.2}
  \]

  because 45 is the omitted small parent component; it is the correction
  between indexing in the full 6,435-term deck and indexing in the
  6,390-term large cycle.
* The bridge size is

  \[
                              49=45+4.                       \tag{1.3}
  \]

  It contains the whole small parent component and the four omitted large
  parent owners at indices 5109, 5110, 5111, 5112.  The equality
  \(4=d+1\) for the present depth \(d=3\) is literal in this certificate.
  It is not, by itself, a theorem that every future seam costs \(d+1\).

The 49 bridge facets and the 49 omitted parent owners have a 128-edge
containment graph with a perfect matching.  More strongly, their literal
occurrence-socket graph has 96 edges and a perfect matching in which every
missing marked immediate-upper target is realized by a two-owner interval.

This still does **not** make containment SDR sufficient for an even
recursion.  It settles the central partition and the missing marked
immediate-upper row.  A recursive theorem additionally needs:

1. a protected-span condition for all deeper upper targets;
2. the exact schedule-aware residence/event condition; and
3. one simultaneous maximal-common-cap lower compiler, not only marginal
   Hall.

Theorem 5.1 states the exact sufficient package.

## 2. Literal two-shift identities

The authoritative hashes are

```text
answers/k15.word
  f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b

answers/k16.word
  890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe
```

Let \(M\) be the subsequence of \(D^3B\) containing \(z\), with \(z\)
deleted, and let \(N\) be the subsequence avoiding \(z\).  Literal replay
gives

\[
 |M|=|N|=6435,\qquad
 \operatorname{rk}(M)=8^{6386}7^{49},\qquad
 \operatorname{rk}(N)=8^{6435}.                              \tag{2.1}
\]

With half-open slices and parent indices modulo 6,435,

\[
\begin{aligned}
N={}&T[5112:6390]\Vert T[0:5112]\\
   &\Vert T[6426:6435]\Vert T[6390:6426].                    \tag{2.2}
\end{aligned}
\]

Thus its four chunks have lengths and global shift constants

\[
                 (1278,5112),(5112,5157),(9,36),(36,6426).  \tag{2.3}
\]

The first 6,386 marked projections are

\[
 M[0:6386]=T[5113:6390]\Vert T[0:5109].                     \tag{2.4}
\]

Equivalently,

\[
 M_j=T_{j+5113}\quad(0\le j<1277),                           \tag{2.5}
\]

and

\[
 M_j=T_{j+5158\pmod {6435}}\quad(1277\le j<6386).          \tag{2.6}
\]

Equation (1.2) is now forced: after wrapping inside the 6,390-cycle, the
global-index correction is \(6435-6390=45\).

The omitted parent-index set is exactly

\[
 \mathcal O=\{5109,5110,5111,5112\}\cup\{6390,\ldots,6434\}. \tag{2.7}
\]

The last 49 terms \(F_0,\ldots,F_{48}\) of \(M\) are distinct rank-seven
facets.

## 3. The 128-edge value SDR and the stronger 96-edge socket SDR

Join a bridge facet \(F_j\) to omitted owner \(T_i\) when
\(F_j\subset T_i\).  The graph has exactly 128 edges.  Its degree
histograms are

\[
\begin{array}{c|rrrr}
\text{facet degree}&1&2&3&4\\ \hline
\text{number}&1&17&31&0
\end{array}
\qquad
\begin{array}{c|rrrr}
\text{owner degree}&1&2&3&4\\ \hline
\text{number}&1&18&29&1.
\end{array}                                                   \tag{3.1}
\]

An explicit perfect matching sends bridge positions \(j=0,\ldots,48\) to
parent indices

\[
\begin{aligned}
 &(5109,5110,5111,5112),\\
 &(6426,6427,\ldots,6434),\\
 &(6390,6391,\ldots,6425).                                  \tag{3.2}
\end{aligned}
\]

Every matched pair differs by exactly one old coordinate.

There is a stronger occurrence-level statement.  The bridge occurrences
lie at child chronology positions

\[
 6386,6387,6388,6389,12825,12826,\ldots,12869.               \tag{3.3}
\]

Connect a bridge occurrence to owner \(T_i\) when some contiguous child
chronology interval containing that occurrence has OR \(z\cup T_i\).  This
socket graph has 96 edges: 47 bridge occurrences have degree two and two
have degree one.  It has the explicit perfect matching

\[
\begin{aligned}
 &(5109,5110,5111,5112),\\
 &(6425,6426,\ldots,6434),\\
 &(6390,6391,\ldots,6424).                                  \tag{3.4}
\end{aligned}
\]

For the first four facets use the outgoing intervals
\([6386,6387],\ldots,[6389,6390]\).  The first small-component facet uses
the incoming seam \([12824,12825]\).  Every later small-component facet
uses its incoming two-owner interval.  Direct OR replay gives \(z\cup T_i\)
on every one of these 49 intervals.

Thus the bridge is not merely a numerical replacement deck: it has a
literal one-step immediate-upper service system.  Notice that (3.2) and
(3.4) are different matchings.  Value containment alone forgets the
chronological socket.

## 4. The exact variable staircase

The optimum uses all starts \(s_i=i\) and the deadline set

\[
 \{0,1,\ldots,12872\}\setminus\{0,1,6388\}.                 \tag{4.1}
\]

If \(\delta_i\) is its \(i\)-th retained deadline, the middle chronology is

\[
 C_i=\bigvee_{p=i}^{\delta_i}B_p.                            \tag{4.2}
\]

The first 6,386 rows have three physical letters and all remaining 6,484
rows have four:

\[
 C_i=(D^2B)_i\quad(i<6386),\qquad
 C_i=(D^3B)_i\quad(i\ge6386).                               \tag{4.3}
\]

This sequence is byte-for-byte

```text
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
SHA c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906
```

It consists of all 12,870 rank-eight targets exactly once, with 6,435 on
each \(z\)-shore.  Its contiguous OR deck contains all 26,333 strict upper
targets.  Therefore (1.1) is diagnostic of the one-cell extensions of the
shallow rows; it is not the child middle chronology.  This is the exact
reason a flat \(D^3\) induction would incorrectly reject the optimal K16
word.

### Lemma 4.1 (two-component bridge arithmetic)

Let a parent trace of size \(W\) be the disjoint union of cyclic blocks of
orders \(W-s\) and \(s\).  Suppose an odd-to-even lift has:

1. an unmarked rail consisting of rerooted copies of both blocks;
2. a shallow marked rail consisting of the large block with one consecutive
   collar of \(d+1\) parent owners removed; and
3. a deep marked bridge consisting of the small block plus those \(d+1\)
   collar replacements.

Then the shallow length \(a\) and bridge length \(b\) are forced to be

\[
                   a=W-s-(d+1),\qquad b=s+d+1.              \tag{4.4}
\]

When the two pieces of the rerooted large block are written with global
indices modulo \(W\), their affine shift constants differ by \(s\).  In the
deadline normal form (5.2), the exceptional omitted deadline is

\[
                        a+d-1=W-s-2.                         \tag{4.5}
\]

#### Proof

The retained marked block has the stated large-block size minus its collar,
which gives \(a\).  Its complement in one \(W\)-term shore gives \(b\).
After wrapping in a cycle of order \(W-s\), global indexing modulo \(W\)
accumulates the discrepancy \(W-(W-s)=s\).  Substitution gives (4.5).
\(\square\)

For K16, \((W,s,d)=(6435,45,3)\), hence
\[
 a=6386,\qquad b=49,\qquad a+d-1=6388.
\]
The lemma is bookkeeping under the three displayed structural hypotheses.
It does not prove that an all-dimension parent supplies the collar or its
facet replacements.

## 5. Abstract variable-staircase facet-bridge theorem

Let \(|V|=2r-1\), let \(z\notin V\), and put

\[
 W=\binom{2r-1}{r}=\binom{2r-1}{r-1}.                        \tag{5.1}
\]

Fix a depth \(d\ge1\), a bridge size \(b\), and \(a=W-b\).  Let a proposed
child carrier have \(2W\) ordered central rows and physical length
\(2W+d\).  Use all starts \(0,\ldots,2W-1\) and delete from the physical
deadline set exactly

\[
          Y=\{0,1,\ldots,d-2\}\cup\{a+d-1\}.                \tag{5.2}
\]

Write \(\delta_i\) for the increasing retained deadlines and
\(I_i=[i,\delta_i]\).  Then

\[
 |I_i|=d\quad(i<a),\qquad |I_i|=d+1\quad(i\ge a).            \tag{5.3}
\]

Suppose the following five conditions hold.

**M (middle partition).**  The proposed row values \(C_i\) are distinct
rank-\(r\) sets and

\[
 \{C_i:z\notin C_i\}=\binom{V}{r},\qquad
 \{C_i\setminus\{z\}:z\in C_i\}=\binom{V}{r-1}.            \tag{5.4}
\]

**Q1 (retained owners plus literal bridge sockets).**  With the same
physical caps \(A_p\) used in H below, extending every shallow row by its
next physical letter supplies \(z\cup P\) for all
\(P\in\binom{V}{r}\setminus\mathcal O\).  The deep marked bridge rows are
rank-\((r-1)\) facets, and there is an occurrence-level socket matching
which assigns every \(P\in\mathcal O\) to a contiguous interval containing
its matched bridge occurrence and having OR \(z\cup P\).

**U (protected all-depth inheritance).**

1. every old target \(Q\subseteq V\) with \(|Q|>r\) has a transported
   unmarked interval of OR \(Q\); and
2. every \(Q\subseteq V\) with \(|Q|>r\) has a transported marked interval
   of OR \(z\cup Q\).

It is enough to verify U by the exact cutwise debt identity: all internal
parent witnesses persist, and every vulnerable cut-crossing target occurs
on a declared new seam or bridge ray.

**R (residence / row recovery).**  The child occurrence event stream and
the schedule (5.2) pass the exact safe-corridor inequalities, including all
hypotheses of that criterion.  Independently, every row interval is
recovered exactly:

\[
                         \bigvee_{p\in I_i}A_p=C_i.           \tag{5.5}
\]

For a terminal construction, (5.5) is the row-recovery statement actually
used below.  For recursion, the safe-corridor condition and capped
endpoint-run/event state are exported, because (5.5) alone does not certify
compatibility with a later cut.

**H (one common lower compiler).**  Let

\[
 E_p=\bigcap_{i:p\in I_i}C_i.                               \tag{5.6}
\]

There is an injective assignment \(\mu\) of every nonempty target below
rank \(r\) to an admissible physical lower cell such that the maximal
common caps

\[
 A_p=E_p\cap\bigcap_{S:p\in\mu(S)}S                         \tag{5.7}
\]

are nonempty and satisfy both the middle equations (5.5) and

\[
                         \bigvee_{p\in\mu(S)}A_p=S           \tag{5.8}
\]

for every assigned lower target.

### Theorem 5.1 (conditional even facet-bridge lift)

Under M, Q1, U, R and H, the word \((A_p)\) is universal on
\(V\cup\{z\}\) and has length \(2W+d\).  If this length is the deadline
lower bound \(B(2r)\), it proves equality in that dimension.

#### Proof

Condition M and (5.5) realize every central target.  A strict upper target
avoiding \(z\) is supplied by U(1).  A strict upper target containing
\(z\) is \(z\cup Q\).  If \(|Q|=r\), it is supplied either by a retained
one-cell extension or by its Q1 bridge socket.  If \(|Q|>r\), U(2) supplies
it.

All row intervals \(I_i\) are chain-aligned: their starts increase by one
and their deadlines are increasing.  Hence a consecutive block of carrier
rows has one contiguous physical union.  The OR of the physical caps over
that union is the OR of the carrier rows, so every declared upper witness
is literal in \((A_p)\).

Finally, H makes every letter nonempty and gives every lower target its
literal contiguous interval.  Thus every nonempty subset is realized.
The length assertion is immediate. \(\square\)

### Corollary 5.2 (finite protected transition state)

For a sealed-fragment recursion, Theorem 5.1 can be checked from the joint
state consisting of:

1. the middle shore partition and the value-plus-socket bridge matching;
2. the exact endpoint short-run event records;
3. the occurrence-labelled cutwise upper-debt rays at every depth; and
4. the exposed maximal-common-cap relation of H.

Natural join of these four fields is exact.  If an all-dimension Pascal
atlas is left-total on this state, the odd-to-even RSB step follows.

The fourth field cannot presently be replaced by a scalar Hall number.
The K16 solution uses a global, asymmetric common-cap matching; parent
compiler feasibility does not automatically extend across the facet
bridge.

## 6. What K16 proves and what it does not

For K16, M, Q1 and U are independently replayed here.  The target chronology
contains all 12,870 middle and 26,333 strict upper masks.  R and H are the
authenticated variable-schedule/common-cap certificate which decodes to
`answers/k16.word` and then passes literal 65,535-mask replay.

This supplies a positive base for the even facet-bridge transition
language.  It does not prove that a bridge of size \(s+d+1\) always exists,
that containment Hall automatically has occurrence sockets, that deeper
upper rays are automatic, or that the common-cap relation has bounded
adhesion.  Those are the exact extra hypotheses required for an all-
dimension induction.

## 7. Independent replay

The lightweight solver-free script

```text
scratch/audit_k16_d3_two_shift_facet_bridge_20260731.py
SHA 8ab36f49c9a53f15386afe17dfe5273ff5c3e7d3dc4fa77d76469180b3b041fb
```

checks both word hashes, both derivative histograms, the two parent Johnson
cycles, every equality in (2.2)--(2.6), the exact omitted set (2.7), the
128-edge containment graph and explicit SDR, the 96-edge occurrence-socket
graph and explicit SDR, the variable deadline schedule, equality with the
frozen target chronology, and complete middle/upper coverage.  Its
normalized payload SHA-256 is

```text
82217744647c185fa1c07923501ff8539b80842229fe56e150571d1a017a3846
```

The audit is finite evidence only for the displayed K15--K16 transition;
Theorem 5.1 is the general conditional statement.
