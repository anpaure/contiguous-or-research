# Audit of the `k=11` cyclic two-run braid

## Verdict

The concrete 42-seed certificate is valid, with one essential correction:
the quotient boundary has translation voltage `+1`.  Literal modulo-42
closure has different ranks and misses a third rank-five orbit.

The cyclic component obstruction is correct under the stated row grading.
It is a one-way consequence of strict containment: a rank-five triple must
lie on an edge induced by the rank-four pair positions.  The converse is not
automatic.

For a linear word of length 465, the proposed row grading permits either one
or two runs of rank-four pairs.  Two runs are the completely tight case; they
are not forced by saturation and distinctness alone.

Finally, the numerical row grading

\[
\begin{array}{c|rrrrrr}
 &1&2&3&4&5&6\\ \hline
\text{singletons}&11&55&165&234&0&0\\
\text{pairs}&0&0&0&96&368&0\\
\text{triples}&0&0&0&0&94&369
\end{array}
\tag{0.1}
\]

is a coherent saturated construction ansatz, not a consequence of the
rank-count theorem alone.

The independent checker is `scratch/verify_two_run_braid.py`.

## 1. Correct quotient convention

Let `tau` cyclically translate the eleven coordinates.  The seed is

\[
\begin{split}
B={}&(33,108,46,166,550,534,1042,1052,1164,204,580,645,660,540,\\
&564,1060,176,1074,42,1036,3,522,552,516,76,1,1098,18,28,140,\\
&160,104,1568,1121,1061,53,561,536,1553,1680,1296,1170).
\end{split}
\tag{1.1}
\]

The developed cyclic word of length `42*11=462` is

\[
 A_{42q+i}=\tau^q B_i
 \qquad(0\le q<11,\ 0\le i<42).
\tag{1.2}
\]

Consequently the correct quotient extension is

\[
 B_{42}=\tau B_0,\qquad B_{43}=\tau B_1,
\tag{1.3}
\]

not `B_42=B_0`.  Define

\[
 E_i=B_i,\quad P_i=B_i\cup B_{i+1},\quad
 T_i=B_i\cup B_{i+1}\cup B_{i+2}
 \qquad(0\le i<42),
\tag{1.4}
\]

using (1.3) at the seam.  Since rank and translation orbit are invariant
under `tau`, the quotient positions still form a 42-cycle.

### Zero-voltage warning

If one instead reads (1.4) literally modulo 42, the profiles are

\[
\begin{array}{c|l}
E&1^1,2^5,3^{15},4^{21}\\
P&4^9,5^{32},6^1\\
T&5^7,6^{33},7^1,9^1.
\end{array}
\tag{1.5}
\]

The missing rank-five orbit representatives are then

\[
 157,199,333.
\tag{1.6}
\]

Thus the claimed profile is false at voltage zero, even though the 126
orbit colours happen still to be distinct.  Voltage `+1` is not cosmetic.

## 2. Strict containment and the cyclic obstruction

Assume all orbit colours represented by the 42 singletons, 42 pairs, and 42
triples are distinct.  Then every physical containment in the short-window
triangle is strict.  For example,

\[
 E_i\subsetneq P_i,\qquad E_{i+1}\subsetneq P_i,
\tag{2.1}
\]

and

\[
 P_i\subsetneq T_i,\qquad P_{i+1}\subsetneq T_i.
\tag{2.2}
\]

If equality held in (2.1) or (2.2), the two cells would have the same mask
and hence the same translation orbit, contradicting distinctness.

Now impose the cyclic row grading

\[
 E:1^1,2^5,3^{15},4^{21},qquad
 P:4^9,5^{33},qquad
 T:5^{t_5},6^{42-t_5}.
\tag{2.3}
\]

Let

\[
 H=\{i\in\mathbb Z/42\mathbb Z:|P_i|=4\}.
\tag{2.4}
\]

Thus `|H|=9`.  Regard `H` as a set of vertices in the positional cycle
whose edges are the adjacencies `i--(i+1)`.

### Lemma 2.1 (one-way induced-edge law)

If `|T_i|=5`, then `i` and `i+1` both belong to `H`.

#### Proof

Both `P_i` and `P_{i+1}` are strict subsets of `T_i`.  They therefore have
rank at most four.  Under (2.3), pair ranks are only four or five, so both
have rank four.  QED.

The converse is not a theorem: two adjacent rank-four pairs may have union
of rank six or higher.

For a subset `H` of a cycle, let `e(H)` be its number of induced positional
edges.  Explicitly,

\[
 e(H)=
 \begin{cases}
  0,&H=\varnothing,\\
  |H|,&H=\mathbb Z/42\mathbb Z,\\
  |H|-r(H),&0<|H|<42,
 \end{cases}
\tag{2.5}
\]

where `r(H)` is the number of cyclic runs in the proper nonempty case.
It is sometimes convenient to define the boundary-corrected defect

\[
 c(H)=|H|-e(H).
\tag{2.6}
\]

Then `c(H)=r(H)` for a proper nonempty set, while `c(H)=0` for both the empty
and full-cycle boundary cases.  Using the ordinary component count in the
full-cycle case would incorrectly lose the wrap edge.

Lemma 2.1 gives

\[
 t_5\le e(H)=|H|-c(H).
\tag{2.7}
\]

The singleton and pair rows in (2.3) already contain `33` of the `42`
rank-five translation orbits.  Complete rank-five coverage would require
`t_5=9`.  But `H` is proper and nonempty, so `c(H)>=1`, and

\[
 t_5\le9-c(H)<9.
\tag{2.8}
\]

Hence a cyclic seed with this grading cannot cover every rank-five orbit.
It misses at least `c(H)` such orbits.  This is a valid obstruction, but it
is conditional on the grading (2.3).

## 3. What the linear length-465 count really implies

Let a linear word have positions `1,...,465`.  Write

\[
 E_i=A_i\quad(1\le i\le465),
\]

\[
 P_i=A_i\cup A_{i+1}\quad(1\le i\le464),
\]

and

\[
 T_i=A_i\cup A_{i+1}\cup A_{i+2}\quad(1\le i\le463).
\]

First impose the stronger saturated-short-band hypothesis used in the
proposed argument:

\[
 \{U(I):|I|\le3\}
 =\{S:1\le|S|\le5\}\mathbin{\dot\cup}\mathcal F_6,
 \qquad |\mathcal F_6|=369,
\tag{3.1}
\]

with all 1392 values distinct and every member of `mathcal F_6` of rank
exactly six.

No singleton can then have rank five.  Such a singleton lies in an adjacent
pair of rank at least six, and that pair lies in a triple which must strictly
contain it and hence have rank at least seven, contradicting (3.1).  The same
argument handles the word boundaries because every singleton lies in a pair
which lies in a triple.  Similarly, no pair can have rank six, because every
pair lies in a triple and containment is strict.  Therefore

\[
 |E_i|\le4,\qquad |P_i|\le5.
\tag{3.2}
\]

Let `c` be the number of rank-five triples, and define

\[
 H=\{i\in[464]:|P_i|\le4\}.
\tag{3.3}
\]

All 462 rank-five masks must occur in the pair or triple row.  Hence the
number of rank-five pairs is `462-c`, and

\[
 |H|=464-(462-c)=c+2.
\tag{3.4}
\]

Every rank-five triple has both adjacent pairs in `H`.  If `H` has `r`
components in the path, then

\[
 c\le e(H)=|H|-r=c+2-r,
\]

and therefore

\[
 r\le2.
\tag{3.5}
\]

This is the valid general consequence of (3.1).  The identity
`|H|=c+2` does not force equality in the induced-edge bound.

Now specialize to the proposed row grading (0.1).  Then `c=94`, every member
of `H` has rank exactly four, and, writing

\[
 C=\{i\in[463]:|T_i|=5\},
\tag{3.6}
\]

one has

\[
 |H|=96,\qquad |C|=94.
\tag{3.7}
\]

Strict containment gives only

\[
 C\subseteq\{i:i\in H,\ i+1\in H\}.
\tag{3.8}
\]

If the nonempty set `H` has `r` runs in the path of 464 pair positions, its
induced-edge count is `96-r`.  Therefore `94<=96-r`, so

\[
 r\in\{1,2\}.
\tag{3.9}
\]

This is the exact conclusion.

* If `r=2`, then all `94` induced edges of `H` must be rank-five triples.
  This is the completely tight two-run realization.
* If `r=1`, then `H` has `95` induced edges and one of them can jump above
  rank five while the other `94` give the required rank-five triples.

Thus two components are **allowed and extremal**, but are not necessary.
The numerical identity

\[
 |H|=|C|+2
\tag{3.10}
\]

implies two runs only after adding the converse of Lemma 2.1, namely that
every induced edge of `H` produces a rank-five triple.  That converse is an
extra no-jump ansatz.

### Portal off-by-one in the two-run case

Under the tight two-run choice, suppose the two `H`-runs have lengths
`ell_1,ell_2`, with `ell_1+ell_2=96`.  Their rank-five triple runs have
lengths `ell_1-1` and `ell_2-1`.  A length-four window consists of two
adjacent triples.  Hence the number of length-four windows whose two
constituent triples are both rank five is only

\[
 (\ell_1-2)+(\ell_2-2)=92.
\tag{3.11}
\]

But after the 369 rank-six triple values in (0.1), there remain

\[
 \binom{11}{6}-369=93
\tag{3.12}
\]

rank-six masks to cover.  A length-four window containing a rank-six triple
cannot give a *new* rank-six value: by containment and equal rank, its
rank-six union would equal that already used triple value.  Thus the 92
canonical two-triple portals are one short of the 93 remaining masks.

This is not an impossibility theorem.  It says that a literal claim that the
two runs supply all 93 portals has an off-by-one error.  A successful braid
must obtain at least one remaining rank-six mask from a longer window, or
alter the rank-five-edge arrangement.  In particular, the one-component
case can place 94 rank-five triples consecutively and then has 93 adjacent
pairs.

## 4. Forced aggregate count versus row-grading ansatz

At `k=11`, rank six gives

\[
 M=\binom{11}{6}=462,qquad n=M+3=465.
\]

Every target below rank six has a witness of length at most three.  There are

\[
 \sum_{s=1}^5\binom{11}{s}=1023
\tag{4.1}
\]

such masks, while the number of singleton, pair, and triple cells is

\[
 465+464+463=1392=1023+369.
\tag{4.2}
\]

If all 1392 short cells have distinct OR values, the following facts are
forced:

1. every mask of ranks one through five appears exactly once among them;
2. the other 369 cells have distinct values of rank at least six; and
3. every containment between nested short cells is strict.

These facts do **not** determine which row contains a given rank.  A rank-two
or rank-three value can in principle occur in a pair cell if its singleton
predecessors are smaller; similarly a rank-five value can occur as a
singleton.  Distinctness alone does not rule this out.

The profile (0.1) follows after adding the following placement choices:

* all ranks one through three are placed in singleton cells;
* all remaining singleton cells are rank four;
* pair cells finish rank four and then carry rank five;
* triple cells finish rank five, and every residual short cell is rank six.

Under those choices the arithmetic is exact:

\[
 465-(11+55+165)=234,
\tag{4.3}
\]

\[
 330-234=96,qquad 464-96=368,
\tag{4.4}
\]

\[
 462-368=94,qquad 463-94=369.
\tag{4.5}
\]

So (0.1) is an excellent collision-free target, but it is not WLOG and must
not be entered in the theorem ledger as forced by equality.

## 5. Independent certificate verification

With the voltage-`+1` convention (1.3), direct enumeration gives

\[
\begin{array}{c|l}
E&1^1,2^5,3^{15},4^{21}\\
P&4^9,5^{33}\\
T&5^7,6^{35}.
\end{array}
\tag{5.1}
\]

The 126 canonical translation-orbit representatives in the three rows are
pairwise distinct.  The union of the rows covers every translation orbit in
ranks one through four.  At rank five it covers 40 of 42 orbits, with exact
missing representatives

\[
 157,qquad199.
\tag{5.2}
\]

These are two **orbits**, hence 22 individual rank-five masks, not two
individual masks.  The triple row contains 35 distinct rank-six orbits.

The rank-four pair positions, in zero-based quotient indexing, are

\[
 20,21,22,23,24,\qquad27,28,29,30.
\tag{5.3}

They form two cyclic runs of lengths five and four.  Their seven induced
edges are

\[
 20,21,22,23,\qquad27,28,29,
\tag{5.4}
\]

and these are exactly the seven rank-five triple positions.  Thus the seed
attains equality in (2.7) with `|H|=9` and `c(H)=2`.

Developing the seed through all eleven translations produces 1386 distinct
actual short-window OR values, with profiles

\[
\begin{array}{c|l}
E&1^{11},2^{55},3^{165},4^{231}\\
P&4^{99},5^{363}\\
T&5^{77},6^{385}.
\end{array}
\tag{5.5}

This is a valid cyclic 462-term partial object.  It is not by itself the
linear 465-cell grading (0.1); a separate cut-and-three-position completion
argument is still required.

## 6. Correct theorem ledger

### Proved

* Distinct orbit colours make all short-window containments strict.
* Under the cyclic row grading, rank-five triples occur only on edges induced
  by rank-four pair positions.
* A proper nonempty cyclic `H` misses at least one rank-five orbit, and at
  least `c(H)` under the notation (2.6).
* Under the linear grading (0.1), the rank-four pair positions have at most
  two runs.
* A tight two-run layout supplies only 92 adjacent-rank-five-triple
  length-four portals for 93 rank-six masks left outside the triple row.
* The supplied seed, with voltage `+1`, has the exact certificate recorded in
  Section 5.

### Not proved

* That every saturated length-465 solution can be put in the grading (0.1).
* That the linear rank-four pair positions must have exactly two runs rather
  than one.
* That an induced edge of rank-four pairs must have rank-five triple union.
* That the portal off-by-one can be repaired by a longer window while
  preserving the remaining upper-shadow requirements.
* That the cyclic seed can be cut and completed with three positions while
  preserving distinctness, pin survival, and all upper masks.

The seed is strong evidence for a two-run construction, but the remaining
linear completion is a genuine theorem, not a bookkeeping formality.
