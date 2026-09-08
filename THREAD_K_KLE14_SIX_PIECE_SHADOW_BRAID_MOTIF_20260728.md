# Lane K: the recurring six-piece Shadow--Braid and its exact (k=15) boundary

Date: 2026-07-28

Status: exact certificate extraction, a proved unbalanced-sector composition
lemma, a proved bounded-cut obstruction on the current (k=15) carrier, and
one sharply stated inductive source lemma.  No (k=15) solution is claimed.
All positions and coordinates are zero-based.

## 0. Verdict

The strongest recurring braid in the completed small certificates is not a
generic three-cut permutation.  It is the same **two-\(A\)-cut, one-\(B\)-ear
six-piece router** in three distinct exact certificates:

\[
                         5\to6,\qquad11\to12,\qquad13\to14.
\]

Fix a new coordinate (z).  The source middle deck is split into a sector
(A) avoiding (z) and a sector (B) containing (z).  Cut (A) twice,
cut a (B)-ear of length exactly (d+1), and alternate the six oriented
pieces.  In every exact certificate:

1. all five new seams exchange (z) with one old coordinate;
2. the two upper colours lost at the two ends of the (B)-ear identify the
   two (A)-cut vertices;
3. two new seams restore those two colours exactly;
4. the final (z)-incidence word has three one-runs (six alternating
   (A/B) blocks); and
5. the short (B)-ear erodes to one controller position whose mandatory
   core and literal source letter are both exactly ({z}).

The completed words have lengths (21,926,3434) and independently cover
all (63,4095,16383) nonzero masks.

This literal motif is absent from the current (k=15) Hall-22 carrier in two
different senses.

* A coordinate partitions the rank-eight deck into sectors of sizes
  (3003) and (3432), not two equal sectors; the imbalance is
  (429=\operatorname{Cat}_7).
* Every coordinate of Hall-22 has \(428,\ldots,432\) one-runs.  A single
  segment-interior-preserving rearrangement needs at least \(425\) old seam
  cuts to create a three-run router coordinate.  Thus no fixed-\(J\)
  small-seam braid can recreate the small-certificate mechanism from this
  carrier.  A long composition whose cumulative seam budget is at least
  \(425\) is not ruled out.

At its local core, the \(k=12,14\) routers use two upper-neutral Johnson
triangle seams and three deck-closing seams.  The \(k=6\) router installs
both alternate sides of one triangle, so it has three hinge seams and two
other deck-closing seams.  There is nevertheless a precise odd-step
candidate.  The six-piece seam
algebra does not require equal sector sizes.  It can braid a (3003)-vertex
(A) path and a (3432)-vertex (B) path if those paths already have the
required residence and shadow properties.  Starting from the exact (k=14)
path, the natural (A)-source is its first upper-shadow walk.  That walk has
all (3003) required rank-eight colours and exactly (428) surplus
occurrences; the lifted (B)-source has exactly (428) depth-three residence
defects.  This identifies the exact **Catalan-residual source gate**.  The
numerical equality is not asserted to be a canonical pairing.

## 1. The unbalanced coordinate-ear composition lemma

Let (X) be a coordinate set, (z\notin X), and let every member of the two
paths

\[
 A=(A_0,\ldots,A_{a-1}),\qquad
 B=(B_0,\ldots,B_{b-1})
\]

have rank (r), with (z\notin A_i) and
(B_j=\{z\}\cup C_j), (C_j\in\binom X{r-1}).  Assume (A) and (B)
together enumerate the complete rank-(r) layer of (X\cup\{z\}).  No
equality (a=b) is assumed.

Choose two valid internal cuts in \(A\) and an internal block

\[
                         B_2=B[s,s+d]
\]

with \(1\le s\) and \(s+d+1<b\), of length \(d+1\), giving six nonempty
pieces \(A_1,A_2,A_3,B_1,B_2,B_3\).  Orient the
pieces independently and concatenate them in an alternating (A/B) order.
Call the resulting deck order (T).

### Lemma 1.1 (cross-family seam table)

For (U\in\binom Xr) and (V=\{z\}\cup C),
(C\in\binom X{r-1}), the pair (U,V) is a Johnson edge if and only if
(C\subset U).  In that event

\[
 U\cap V=C,\qquad U\cup V=\{z\}\cup U,                 \tag{1.1}
\]

and the seam exchanges (z) with the unique member of (U\setminus C).

#### Proof

The two rank-\(r\) sets differ in exactly two coordinates precisely when
\(V\setminus U=\{z\}\) and \(U\setminus V\) is a singleton.  This is
equivalent to \(C\subset U\), and then (1.1) is immediate.  \(\square\)

The two first-upper colours deleted by cutting out (B_2) are

\[
 \{z\}\cup U^- =B_{s-1}\cup B_s,
 \qquad
 \{z\}\cup U^+ =B_{s+d}\cup B_{s+d+1}.                \tag{1.2}
\]

Here (U^-,U^+\in\binom Xr), so both occur as vertices of (A).  Cutting
next to those two vertices exposes the only canonical ports capable of
restoring (1.2) by Lemma 1.1.

### Lemma 1.2 (upper-neutral triangle hinge)

Let \(|K|=r-2\) and let \(a,b,z\) be distinct and outside \(K\).  Put

\[
 P=K\cup\{z,a\},\qquad Q=K\cup\{z,b\},\qquad
 U=K\cup\{a,b\}.                                      \tag{1.3}
\]

Then

\[
 P\cup Q=P\cup U=Q\cup U=K\cup\{z,a,b\},              \tag{1.4}
\]

whereas the three lower colours are \(K\cup\{z\}\),
\(K\cup\{a\}\), and \(K\cup\{b\}\).  Thus rotating the edge \(PQ\) to
\(PU\) or \(QU\) preserves its immediate upper colour and changes its
immediate lower colour.

#### Proof

All assertions follow by direct union and intersection of the three sets in
(1.3).  Each pair has symmetric difference two.  \(\square\)

The two ear boundaries in every completed certificate are two instances of
this hinge.  This is the literal Shadow--Braid atom; the remaining seams are
deck-closing routers.

### Theorem 1.3 (unbalanced six-piece Shadow--Braid)

In the setting above, suppose:

1. the five new cross-family seams satisfy Lemma 1.1;
2. (T) is linearly depth-(d) resident;
3. every upper rank is covered by consecutive windows of (T); and
4. writing
   \[
   E_j=\bigcap_{\max(0,j-d)\le i\le\min(j,|T|-1)}T_i,
   \]
   there are nonempty letters \(e_j\subseteq E_j\),
   \(0\le j<|T|+d\), such that
   \[
   \bigcup_{j=i}^{i+d}e_j=T_i\quad(0\le i<|T|)
   \]
   and every nonempty mask of rank below \(r\) is the union of one
   contiguous interval of the \(e_j\)'s.

Then the compiled word has length

\[
                   \binom{|X|+1}{r}+d
\]

and is universal.  If this length equals the monotone-deadline lower bound,
it is optimal.

#### Proof

Piece reversal preserves every internal window label.  Conditions 1--2 make
(T) one resident Johnson path, while the two sector decks make it an exact
enumeration of the middle layer.  Condition 4 covers the lower ideal and
reconstructs every middle state.  Every upper witness in condition 3 is a
union of consecutive middle states, hence of one longer interval of the
same source word.  These three ideals exhaust the Boolean lattice.  The proof
nowhere uses \(a=b\).  \(\square\)

This is the exact composition theorem behind the candidate odd step.  It is
fail-closed: the difficult assertions are the existence of the two source
paths, residence, higher seam collars, and the one common compiler.

### Corollary 1.4 (multipiece Shadow--Braid)

The conclusion of Theorem 1.3 remains valid if \(A\) and \(B\) are cut into
arbitrarily many nonempty segments and all segments are concatenated in any
order and orientations, provided the resulting chronology \(T\) still
satisfies hypotheses 1--4, with hypothesis 1 read as requiring every new
seam to be a Johnson edge.

#### Proof

The proof of Theorem 1.3 uses the six-piece format only to establish that
piece interiors are preserved and that all new seams are Johnson.  Those
two facts hold under the stated hypotheses for any finite number of pieces;
the residence, upper-witness, and compiler parts of the proof are unchanged.
\(\square\)

## 2. Literal certificate tables

The audit

```text
python3 scratch/audit_kle14_six_piece_shadow_braid_motif.py
```

reconstructs all three final middle paths from their strict sources and
piece specifications; it does not trust stored aggregate scores.

### 2.1 Cuts, ears, and source masks

| (k) | (d) | (A)-cuts | (B)-cut | oriented pieces | source (B)-ear with (z) removed | lost (B)-boundary colours | their positions in (A) |
|---:|---:|---|---:|---|---|---|---|
| 6 | 1 | (7,8) | 3 | `B3R A2F B2R A1R B1R A3F` | (20,6) | (28,22) | (7,8) |
| 12 | 2 | (66,459) | 409 | `A1R B1F A2R B2R A3F B3R` | (47,301,357) | (175,1381) | (460,67) |
| 14 | 2 | (418,1445) | 966 | `A1F B2R A3F B1F A2R B3F` | (2916,2406,2382) | (7012,2510) | (1445,419) |

The apparent one-unit offsets in the last column are exactly the two
before/after choices: a cut after (c) exposes both (A_c) and
(A_{c+1}).

The final piece lengths are respectively

\[
 (5,1,2,8,3,1),\quad
 (67,409,393,3,2,50),\quad
 (419,3,270,966,1027,747).                             \tag{2.1}
\]

### 2.2 All fifteen new seams

Each row records

\[
 \text{final cut position}:\quad L\to R;quad
 L\cap R,\ L\cup R;\quad\text{swapped coordinates}.
\]

For (k=6), (z=5):

```text
 4: 50 -> 22;  intersection 18, union 54; swap {2,5}
 5: 22 -> 38;  intersection  6, union 54; swap {4,5}
 7: 52 -> 28;  intersection 20, union 60; swap {3,5}
15: 26 -> 56;  intersection 24, union 58; swap {1,5}
18: 35 ->  7;  intersection  3, union 39; swap {2,5}
```

For (k=12), (z=11):

```text
 66:   95 -> 2079; intersection  31, union 2143; swap {6,11}
475: 2219 ->  235; intersection 171, union 2283; swap {6,11}
868: 1381 -> 2405; intersection 357, union 3429; swap {10,11}
871: 2095 ->  175; intersection  47, union 2223; swap {7,11}
873:  159 -> 2203; intersection 155, union 2207; swap {2,11}
```

For (k=14), (z=13):

```text
 418:  2383 -> 10574; intersection 2382, union 10575; swap {0,13}
 421: 11108 ->  2924; intersection 2916, union 11116; swap {3,13}
 691:  5422 ->  9518; intersection 1326, union 13614; swap {12,13}
1657: 15200 ->  7012; intersection 7008, union 15204; swap {2,13}
2684:  2510 ->  8654; intersection  462, union 10702; swap {11,13}
```

The restored colours are visible without interpretation:

\[
\begin{array}{c|c}
k&\text{new unions equal to the two values in (1.2)}\\ \hline
6&60=32+28,\quad54=32+22,\\
12&2223=2048+175,\quad3429=2048+1381,\\
14&15204=8192+7012,\quad10702=8192+2510.
\end{array}                                             \tag{2.2}
\]

At \(k=6\), union \(54\) occurs on two new seams; this redundancy does not
alter the restoration claim.

### 2.3 The two active upper-neutral hinges

The old \(B\)-ear boundary edge and the installed alternate triangle side
have exactly the following upper/lower ledgers:

\[
\begin{array}{c|cc}
k&\text{first hinge}&\text{second hinge}\\ \hline
6&U60:L48\longmapsto L20&U54:L34\longmapsto L18\\
12&U2223:L2091\longmapsto L47&U3429:L2404\longmapsto L357\\
14&U15204:L11104\longmapsto L7008&U10702:L8526\longmapsto L462.
\end{array}                                             \tag{2.3}
\]

The \(k=6\), \(U54\) triangle actually installs both alternate sides; the
display chooses the side sharing vertex \(50\).

At \(k=12,14\) the same operation is also an exact two-unit
Robin--Hood transfer between source shores.  Each core \(U\) lost uniquely
at a \(B\)-ear boundary is an \(A\)-vertex incident with a redundant
\(A\)-upper edge \(U\cup\{c\}\):

\[
\begin{array}{c|c|c}
k&\text{redundant \(A\)-colour removed}&
  \text{unique \(B\)-colour restored}\\ \hline
12&239=175\cup\{6\}\quad(\text{load }2)&2223=2048\cup175\\
  &1389=1381\cup\{3\}\quad(\text{load }2)&3429=2048\cup1381\\
14&2511=2510\cup\{0\}\quad(\text{load }2)&10702=8192\cup2510\\
  &7020=7012\cup\{3\}\quad(\text{load }3)&15204=8192\cup7012.
\end{array}                                             \tag{2.4}
\]

Coordinates in (2.4) are zero-based; in one-based notation the extra bits
are \(7,4,1,4\), respectively.  This gives a locally checkable candidate
move:

> Isolate a \(B\)-ear of length \(d+1\); require each lost core \(U^\pm\)
> to be an \(A\)-vertex incident with a duplicated edge colour
> \(U^\pm\cup\{c_\pm\}\); cut those two redundant edges and install the two
> upper-neutral triangle sides of colours \(\{z\}\cup U^\pm\).

Residence, the other three deck-closing seams, higher collars, and common
\(Q\) remain separate exact tests.  The local atom spends two excess units,
not the whole Catalan reservoir.

### 2.4 The singleton router slot

The three final (z)-run lists are

\[
\begin{array}{c|c|c|c}
k&z&\text{middle one-runs of }z&\text{literal singleton position}\\ \hline
6&5 &[0,5),[6,8),[16,19)&7\\
12&11 &[67,476),[869,872),[874,924)&871\\
14&13 &[419,422),[692,1658),[2685,3432)&421.
\end{array}                                             \tag{2.5}
\]

In each case the designated ear is the run of length (d+1).  Its erosion
is the single controller position displayed in the last column.  Direct
evaluation gives mandatory core and actual word letter

\[
                       2^5,\qquad2^{11},\qquad2^{13},    \tag{2.6}
\]

respectively.  Thus this is not merely singleton capacity in a maximal
envelope; the three exact words use the literal singleton.

## 3. Why the sparse router cannot be reached from Hall-22 by bounded cuts

For a binary word \(y_0,\ldots,y_{N-1}\), let \(b(y)\) be its number of
one-runs.  The identity

\[
 b(y)=\sum_i y_i-\sum_{i=0}^{N-2}y_i y_{i+1}             \tag{3.1}
\]

is exact.

### Lemma 3.1 (run-count Lipschitz law)

Cut a word at (J) adjacencies and concatenate the resulting (J+1)
segments in arbitrary order and orientations.  For every coordinate (x),

\[
                    |b_x(T')-b_x(T)|\le J.              \tag{3.2}
\]

#### Proof

The number of ones is unchanged.  Reversal preserves every internal `11`
adjacency.  Only the (J) adjacencies between pieces are replaced, and each
changes the second sum of (3.1) by at most one.  \(\square\)

In the exact \(k=12,14\) lift certificates the router coordinate has three
one-runs; old coordinates have \(83\)–\(85\) and \(263\)–\(265\),
respectively.  In the current Hall-22 path the fifteen one-run counts have
histogram

\[
                         428^4,429^5,430^2,431^3,432^1.   \tag{3.3}
\]

Consequently every segment-interior-preserving route from Hall-22 to a
three-run coordinate needs

\[
                              J\ge428-3=425.             \tag{3.4}
\]

This rules out recreating the motif by one three-cut, one six-piece, or any
single segment braid with fewer than \(425\) cuts on the frozen path.  By
telescoping (3.2), it also forces cumulative cut budget at least \(425\) on
any sequence of segment-interior-preserving braids that ends with a
three-run coordinate.

The conclusion is only about reproducing the sparse coordinate-ear normal
form.  It does **not** obstruct the already certified bounded-cut Hall
improvements, an optimal \(k=15\) carrier in which every coordinate still
has hundreds of runs, a fresh carrier, a deck-changing trade, or a
\(\Theta(\operatorname{Cat}_7)\)-cut macro.

## 4. The exact first-shadow port mismatch at Hall-22

The Hall-22 immediate-lower holes and the positions of their eight middle
supersets are

```text
5801 : 397,840,1213,3656,3858,5452,5815,6018
7267 : 731,2860,3076,3312,5546,6145,6288,6434
8877 : 0,920,2095,2369,2371,5012,5893,6024
13620: 2255,2916,3561,3639,3641,4319,4987,6044.
```

Only (8877\subseteq T_0=9901) and
(7267\subseteq T_{6434}=7779).  The holes (5801,13620) have no boundary
port.  The three repeated first-shadow colours are

\[
                         3868,\quad12685,\quad17140,     \tag{4.1}
\]

each with multiplicity two.

There is a small exact no-go around these data.  For every hole \(M\), the
audit enumerates every endpoint-fixed two-opt reversal

\[
 T[0,a]\;\overleftarrow{T[a+1,b]}\;T[b+1,N-1]          \tag{4.2}
\]

for which either new seam is between two supersets of \(M\), hence has
intersection \(M\), and the other seam is also Johnson.  The numbers
of distinct Johnson-valid reversals for
\(M=5801,7267,8877,13620\) are

\[
                              9,3,4,6.                  \tag{4.3}
\]

None reduces the four-hole count.  The complete outcome histogram
\((h_1',h_{+1}')\) is

\[
 (4,0)^7,\quad(4,1)^3,\quad(5,0)^5,\quad
 (5,1)^2,\quad(5,2)^5.                                \tag{4.4}
\]

Thus seven choices preserve complete first-upper support and merely exchange
one lower hole for another.  This is a complete no-go only for the
endpoint-fixed reversal (4.2), not for three-cut routers or compounds.

## 5. The Catalan-residual odd-step target

For even (K=2r), a fixed coordinate splits the middle layer into equal
sectors because

\[
                  \binom{2r-1}{r}=\binom{2r-1}{r-1}.   \tag{5.1}
\]

This equality is what lets one odd lower-rainbow path generate both source
sectors in the existing lift.  At (k=15), however,

\[
 |A|=\binom{14}{8}=3003,\qquad
 |B|=\binom{14}{7}=3432,\qquad
 |B|-|A|=429=\operatorname{Cat}_7.                     \tag{5.2}
\]

Thus the literal equal-sector source theorem is intrinsically unavailable.
The topology of Theorem 1.3 survives, but its source must carry one
Catalan-sized residual sector.

There is a canonical exact diagnostic.  Let (P) be the rank-seven middle
path in the exact (k=14) certificate and set

\[
                         U_i=P_i\cup P_{i+1}.            \tag{5.3}
\]

Then:

\[
\begin{array}{c|c}
\text{upper-walk slots}&3431\\
\text{distinct rank-eight colours}&3003\\
\text{multiplicity histogram}&1^{2652}2^{274}3^{77}\\
\text{repeat excess}&428=\operatorname{Cat}_7-1\\
\text{adjacent equal / Johnson / other steps}&117/3313/0.
\end{array}                                             \tag{5.4}
\]

So \(U\) is a complete rank-eight Johnson walk with stutters and nonlocal
returns.  Consecutive terms are equal or Johnson-adjacent because both
contain \(P_{i+1}\).  Choosing one occurrence of every rank-eight colour and
cutting the chosen word at every skipped-index gap partitions the \(A\)-deck
unconditionally into at most \(428+1=429\) Johnson pieces.  Every endpoint
\(U_i\) has the canonical triangle ports
\[
 \{z\}\cup P_i\;-\;U_i\;-\;\{z\}\cup P_{i+1}.          \tag{5.5}
\]

The walk is not already a Hamilton path.  Keeping first occurrences and
joining whenever the resulting endpoints are Johnson leaves \(208\)
non-Johnson gaps, hence \(209\) pieces; keeping last occurrences leaves
\(195\) gaps, hence \(196\) pieces.  Only \(298\) repeated occurrences,
belonging to \(169\) target labels, are
individually deletable while retaining a Johnson adjacency in the unchanged
walk.

Independently, using \(B=\{z\}+P\) as the \(z\)-sector at target depth three
fails residence on exactly \(428\) internal old-coordinate runs, all of length
three.  The equality

\[
 \#\{\text{upper surplus occurrences}\}
 =\#\{\text{depth-three short runs}\}=428              \tag{5.6}
\]

is exact but is not a local pairing.  In the final \(k=14\) six-piece family
decomposition:

* \(426\) upper-excess units lie on \(A\)-internal edges, whose loads are
  \(1^{938}2^{272}3^{77}\);
* all \(1713\) \(B\)-internal edge colours are distinct;
* two cross-seam colours duplicate \(B\)-internal colours, while the other
  three cross colours are new; and
* among the \(428\) short runs, \(427\) lie wholly in \(B\)-labelled pieces
  (including the distinguished coordinate-13 ear) and one crosses the
  \(A_2/B_3\) seam; none lies wholly in an \(A\)-piece.

More decisively, only three short-run collars contain even one repeated
upper occurrence:

\[
\begin{array}{c|c|c}
\text{coordinate}&\text{run}&\text{repeated edge colours}\\ \hline
13&419..421&10575\text{ at }418,\quad11116\text{ at }421\\
6&1188..1190&10575\text{ at }1187\\
3&2684..2686&2526\text{ at }2683.
\end{array}                                             \tag{5.7}
\]

Thus \(425\) short runs have no local discarded-repeat service.  Nonlocal
routing is forced.

### Lemma 5.1 (exact \(247\)-cut obstruction for the fixed \(k=14\) source)

For every internal length-three coordinate run \([a,a+2]\) of \(P\), a
segment-interior-preserving depth-three lift must cut at one of the four
edge positions

\[
                            [a-1,a+2].                  \tag{5.8}
\]

The \(428\) intervals (5.8) have transversal number exactly \(247\).
Consequently every segment-interior-preserving lift of this fixed
\(B\)-source needs at least \(247\) original \(B\)-cut positions.

#### Proof

If none of the four edges in (5.8) is cut, the flanked word
\(0\,1\,1\,1\,0\) remains wholly inside one retained segment, possibly
reversed, so the forbidden internal length-three run survives.

For intervals on a line, greedy stabbing by increasing right endpoint is
optimal.  Direct evaluation of the \(428\) literal intervals chooses \(247\)
right endpoints.  The intervals selected at those greedy steps are pairwise
disjoint, giving a matching lower bound of \(247\).  Hence the hitting and
packing numbers are both \(247\).  \(\square\)

In particular, the direct six-piece lift has only the two \(B\)-ear cuts and
cannot raise this fixed source from depth two to depth three.

### Candidate lemma \(\mathrm{ECSB}_{14}\) (extensive Catalan Shadow--Braid)

Choose one occurrence of every upper colour in (5.3), split the resulting
\(A\)-deck into oriented Johnson pieces, and cut \(B=\{z\}+P\) at a
transversal of all \(428\) collars (5.8).  There is a concatenation of all
these pieces using the canonical triangle hinges (5.5) and additional
router seams such that:

1. the selected seams use every piece endpoint once except for two global
   ends and join all pieces into one exact Hamilton path on the whole
   rank-eight deck;
2. every new-coordinate run and every old-coordinate seam collar is
   depth-three resident;
3. every lower and upper flag occurrence destroyed at every depth has an
   internal survivor or an exact new-seam replacement; and
4. the final erosion admits one injective lower pin assignment satisfying
   the common-\(Q\) criterion.

Before cutting, the two source shores have complete upper support in their
coordinate sectors: \(A=U\) supplies the no-\(z\) upper flags, while
\(B=\{z\}+P\) supplies the \(z\)-containing upper flags.  Thus item 3 is an
exact cut-aware preservation/replacement condition relative to a complete
baseline, not a new rankwise coverage conjecture.

Under these four hypotheses, Corollary 1.4 gives a literal \(k=15\) word of
length \(6438\).  The local triangle atom and the \(247\)-cut lower bound are
proved; \(\mathrm{ECSB}_{14}\)'s port-balanced extensive composition is the
missing lemma.  It may use the \(429\)-piece unconditional upper
decomposition, but no theorem says the sector imbalance can be absorbed only
at the ends.

## 6. Scope corrections and failed variants

1. The six-piece (k=6) and (k=12) words are exact optima but are not
   byte-identical to `answers/k06.word` and `answers/k12.word`.  The (k=14)
   six-piece word is byte-identical to `answers/k14.word`.
2. In the retained (7\to8) and (9\to10) source libraries there are
   respectively (175) and (186) endpoint-valid six-piece braids, but no
   residence-valid braid.  The construction is recurring, not automatic.
3. Replaying the current frozen one-hundred-source (k=14) atlas with the
   current search implementation gives (79) upper/residence/singleton
   passes and (28) scalar-Hall passes.  This does not reproduce the prose
   count “35 admit” in `MATH_ODD_EVEN_SIX_PIECE_LIFT_20260728.md`.  The
   individual (k=14) winner and its independent universal-word verification
   are unaffected.
4. The retained artifacts do not include a generator reproducing the stated
   census of (600) symmetry-normalized (k=5) sources.  The stored (k=6)
   source, braid, compiler, word, and independent verifier are individually
   complete.
5. The \(425\)-cut bound is relative to segment-interior preservation of the
   current Hall-22 path and only forbids manufacture of a three-run
   coordinate below that cumulative budget.  It is not a lower bound on
   solving Hall-22.  A non-row-power deck-changing trade is outside its
   scope.
6. The independent \(247\)-cut bound concerns the direct
   \(k=14\to15\) source \(B=\{z\}+P\), not the Hall-22 carrier.  Neither cut
   theorem excludes a non-coordinate partition into router shores.
7. Hall or shadow coverage alone is not a common-\(Q\) proof.  The completed
   \(k=6,12,14\) words have literal compilers; \(\mathrm{ECSB}_{14}\)
   explicitly keeps this as a hypothesis.

## 7. Artifacts and hashes

The new independent extractor is

```text
scratch/audit_kle14_six_piece_shadow_braid_motif.py
SHA-256 02f1144e09075850768ad18ebcc169acd709f6d0a93fd9f55f574f7685ccf86c
```

and its complete machine-readable output is

```text
scratch/k06_k12_k14_six_piece_shadow_braid_motif_audit.json
SHA-256 d46b6dce2e88bc45ebe4d4693089f407791034c530073d1b2bf962372f6d532f
```

The exact braid certificates / compiled words / independent verification
records have hashes

```text
k=6
ac116143ee8eb7402d26260fb3337be89e96d0a77f6ae2f9ff7d106e92449004  scratch/k6_intersection_sixpiece_exact.json
036b9efb42d1feb3a3fcbf82af3cc10772264567647b31d705752466bf551b43  scratch/k6_intersection_sixpiece_exact.word
ad47196959aac997b9a137aeebe029a44ac0bdcf7a644994790d83a34b353599  scratch/k6_intersection_sixpiece_exact.verify.json

k=12
f57f775c55c9ae156aeb124fa0016dd835c0efd1c472897e93bc6ea5abfc45d6  scratch/k12_intersection_sixpiece_hallpass_001.json
a29517e67dd3c9db5f773f5332b3e3e44197cfe79d3d8014ea0770c9bedeb482  scratch/k12_intersection_sixpiece_hallpass_001.word
28c6d581bc5912b6ad369cb0ae60d164fb5a8391c48655ad581eb2a3deb2e506  scratch/k12_intersection_sixpiece_hallpass_001.verify.json

k=14
d67bb4176b49c0b7be4d0ac6f232cf59e4b0247999dbb5b1f06aeb50c62bbc7d  scratch/k14_intersection_sixpiece_hallpass_004a.json
7d94117099bbb46402e8f4edda718dae7eb10e2e5e34e9b588e08a198b43db17  scratch/k14_intersection_sixpiece_hallpass_004a.word
6b5d06a9c8e65b713e80f97c00e1738d8e179df4882f94b73b91884644c9d202  scratch/k14_intersection_sixpiece_hallpass_004a.verify_generic.json
```

The current Hall-22 comparison carrier is

```text
c4d36b5972a07e8c7694a741bbc5cc4a5d657ef13c434bd42433b0fc51b01798  scratch/k15_segment_braid_hall22.json
```

The reusable pipeline is

```text
ffc090306f178410c11df0b1d3186796de320aff26781077cc0a126af1fae1a3  scratch/build_odd_even_intersection_carriers.py
827c9553e7c8de8edc316e6943c9c8ebff1101ccefeab86e16add5aeacd5804e  scratch/search_odd_even_six_piece.cpp
7fcd816845f2a36b0dfd5d061af03209a02af761ada8f0554bf9e8820ef6b8a6  scratch/materialize_odd_even_six_piece.py
e934101a852a040f85ff7ce462f3edda0027fb437802bb59a332776b47aec114  scratch/sigma_multirow_linear_compiler.py
ef7fe81cb6591d27c60143d055aa4b253219fa45573512ab2866c623c33c2799  scratch/verify_exact_or_word.py
```

The new audit performs only parsing, exact reconstruction, shadow counting,
interval stabbing, and twenty-two tiny two-opt port checks.  It launches no
SAT solver and no broad local search.
