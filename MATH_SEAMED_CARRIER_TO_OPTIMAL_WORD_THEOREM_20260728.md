# From a resident carrier 2-factor to an optimal OR word

Date: 2026-07-28

## 1. Setup

For a set word (A=(A_0,ldots,A_{L-1})), write

\[
 (D^jA)_i=\bigcup_{t=0}^{j}A_{i+t}.
\]

Put

\[
 r=\lceil k/2\rceil,qquad W=\binom kr,qquad
 \Lambda=\sum_{s=1}^{r-1}\binom ks,
\]

and let (d=d(k)) be the least integer such that

\[
 dW+\binom{d+1}{2}\ge \Lambda.
\tag{1.1}
\]

Thus (B(k)=W+d) is the endpoint-blocker lower bound.

A **middle chronology** is a listing

\[
 T=(T_0,\ldots,T_{W-1})
\]

of all (r)-subsets of ([k]).  It is a Johnson path if consecutive sets
differ by one deletion and one insertion.  For a block of (q+1) consecutive
middle sets define its lower and upper colours by

\[
 \ell_q(T_i,\ldots,T_{i+q})=\bigcap_{j=0}^{q}T_{i+j},qquad
 u_q(T_i,\ldots,T_{i+q})=\bigcup_{j=0}^{q}T_{i+j}.
\tag{1.2}
\]

The chronology is **linearly (d)-resident** if every internal 1-run of
every coordinate has length at least (d+1).  Equivalently, its maximal
linear erosion

\[
 E_p=\bigcap_{\max(0,p-d)\le i\le\min(W-1,p)}T_i,
 \qquad 0\le p<W+d,
\tag{1.3}
\]

satisfies (D^dE=T).

We use **PCSH** for the pin-compatible sandwich Hall condition of
`MATH_EXACT_CENTRAL_COMPILER_THEOREM_20260727.md`: the lower masks can be
assigned to compatible cells of a nonzero factor (A\subseteq E), while all
coordinatewise central and intermediate pins survive.  PCSH is deliberately
stronger than a scalar capacity inequality or an unlabelled Hall matching.

## 2. The transfer lemma

### Lemma 2.1 (middle and upper transfer)

Suppose (A) has length (W+d) and (D^dA=T).  Then, for every (q\ge0),

\[
 D^{d+q}A=D^qT.
\tag{2.1}
\]

Consequently, if the cells of (D^qT) contain every
((r+q))-subset for every (q\ge1), then all masks of rank greater than
(r) occur as contiguous ORs of (A).

#### Proof

Both sides of (2.1), at position (i), are the union of
(A_i,A_{i+1},\ldots,A_{i+d+q}).  The final assertion follows immediately.
\(\square\)

This is the reason the upper half is a property of the carrier chronology,
whereas the lower half is delegated to the compiler.

## 3. Cutting and joining a carrier 2-factor

Let (F=C_1\sqcup\cdots\sqcup C_c) be a 2-factor of (J(k,r)) whose cycles
partition the middle layer.  Cut one edge from each cycle, orient and order
the resulting paths, and add (c-1) cross-component Johnson edges.  The
result is a Hamilton path (T) through the middle layer.

For an edge (XY), its lower-q1 colour is (X\cap Y).

### Lemma 3.1 (exact lower-q1 seam ledger, odd case)

Assume (k=2r-1) and the (W) edges of (F) have pairwise distinct
lower-q1 colours.  Since

\[
 \binom{k}{r-1}=\binom{k}{r}=W,
\]

these colours are exactly all members of \(\binom{[k]}{r-1}\).

Let (R) be the (c)-set of colours of the cut edges and let (S) be the
set of colours used by the (c-1) new seams.  Then the lower-q1 colours
missing from the Hamilton path are exactly

\[
 H=R\setminus S,qquad
 h:=|H|=c-|R\cap S|.
\tag{3.1}
\]

In particular,

\[
 1\le h\le c.
\tag{3.2}
\]

The ideal seam tree has (c-1) distinct seam colours in (R), in which case
(h=1).

#### Proof

All uncut edges retain all colours outside (R).  A new seam repairs a lost
colour precisely when its colour belongs to (R).  There are only (c-1)
seams, proving both (3.1) and (3.2). \(\square\)

### Lemma 3.2 (upper-window loss ledger)

At depth (q), opening one sufficiently long cycle deletes exactly (q)
cyclic windows of length (q+1).  Thus (c) cuts delete (cq) old windows;
each seam creates (q) new cross-seam windows.  In particular, at most
(cq) upper colours can be lost before the new windows are counted.

More exactly, the spliced path remains upper-complete at depth (q) iff
every colour whose occurrences all met the deleted-window set occurs either
in a retained window or in a new cross-seam window.

This is a finite seam condition, not a consequence of the cardinality count.
The crude sufficient condition that every upper colour have more than (cq)
old witnesses is usually far stronger than necessary.

## 4. Exactly two boundary channels for missing lower-q1 colours

The following fact explains why the one lost colour in the (k=13) path is
harmless, but an arbitrary many-component splice is not.

### Lemma 4.1 (boundary capacity two)

Let (T) be a Johnson path and let (A) be any depth-(d) factor,
(D^dA=T).  Any ((r-1))-set occurring as a contiguous OR of (A), but not
as one of the path-edge colours

\[
 T_i\cap T_{i+1}\qquad(0\le i<W-1),
\]

must occur on one of the two boundary chains

\[
 (D^jA)_0\quad(0\le j<d),
 \qquad
 (D^jA)_{W+d-j-1}\quad(0\le j<d).
\tag{4.1}
\]

Each chain is nested, hence contains at most one distinct set of rank
(r-1).  Therefore at most two missing lower-q1 colours can be supplied away
from the path edges.

#### Proof

An OR interval of rank (r-1) has length at most (d): an interval of
length at least (d+1) contains a full depth-(d) window, whose OR is one of
the rank-(r) sets (T_i).

Consider a cell (B=(D^jA)_p) with (j<d).  The middle cells whose physical
windows contain ([p,p+j]) have indices

\[
 \max(0,p+j-d)\le i\le\min(p,W-1).
\tag{4.2}
\]

Unless (B) is the leftmost or rightmost cell in its row, (4.2) contains two
consecutive indices.  Hence

\[
 B\subseteq T_i\cap T_{i+1}.
\]

Both sides have rank (r-1), so equality holds.  The only exceptions are the
two cells displayed in (4.1).  Along either boundary, increasing (j) only
adds entries to the OR, so the cells are nested.  Two distinct nested sets
cannot have the same rank. \(\square\)

### Corollary 4.2

In the setting of Lemma 3.1, if (h>2), no depth-(d) word having (T) as
its middle chronology can be universal.  If (h=2), the two missing colours
must be assigned to opposite boundaries.  If (h=1), one compatible boundary
flag is enough.

Containment in an endpoint is necessary: a left repair colour must be a
subset of (T_0), and a right repair colour must be a subset of (T_{W-1}).
The exact additional condition is the endpoint interval-hitting criterion of
`MATH_BOUNDARY_FLAG_FACTOR_THEOREM_20260727.md`.

Thus the phrase “(W+1) cells in row (d-1)” hides a sharper statement:
there are two boundary chains, but each has capacity only one at rank
(r-1).

In the odd case the accounting is exact.  Row $d-1$ has $W+1$ cells:
$W-1$ interior cells attached to path edges and two boundary cells.  If the
path has $h$ missing colours, its interior cells have $h-1$ repetitions.
Using $h$ boundary repairs leaves exactly one unavoidable spare cell.  For
the ideal case $h=1$, all $W-1$ interior colours are distinct, one boundary
cell supplies the missing colour, and the other boundary cell is the familiar
single spare flag position.

## 5. The reusable sufficient theorem

### Theorem 5.1 (seamed-carrier compiler theorem)

Let (F=C_1\sqcup\cdots\sqcup C_c) be a middle-layer carrier 2-factor.
Suppose cuts, orientations and (c-1) Johnson seams produce a Hamilton path
(T) with the following properties.

1. **Residence:** (T) is linearly (d)-resident.
2. **Upper-safe splicing:** for every (q\ge1) with (r+q\le k), the cells
   of (D^qT) cover \(\binom{[k]}{r+q}\).
3. **Lower compiler:** (T), together with any prescribed intermediate
   lower-shadow pins and at most two endpoint flags, satisfies PCSH at depth
   (d).

Then there is a nonzero word (A) of length (W+d) whose contiguous ORs
contain every nonempty subset of ([k]).  Hence

\[
 \nu(k)\le W+d.
\tag{5.1}
\]

For (d=d(k)),

\[
 \boxed{\nu(k)=B(k)=W+d(k)}.
\tag{5.2}
\]

If (k=2r-1) and the carrier has a rainbow lower-q1 edge colouring, the
number of endpoint flags demanded by item 3 is exactly the seam deficit
(h=|R\setminus S|).  Consequently the seam architecture requires (h\le2),
and the robust target is (h=1).

#### Proof

Residence gives a maximal factor (E) with (D^dE=T).  PCSH gives a
nonzero (A\subseteq E) with (D^dA=T) whose first (d) OR--Pascal rows
cover every rank below (r).  The central row (T) covers rank (r).
Lemma 2.1 and upper-safe splicing cover every rank above (r).  Thus (A)
is universal and has length (W+d).  The endpoint-blocker theorem supplies
the reverse inequality when (d=d(k)). \(\square\)

### What the theorem does and does not make automatic

The theorem is lossless, but it does not claim that abundance of Johnson
seams implies compatibility.  The three genuinely labelled conditions are:

- residence across every seam;
- survival or replacement of the deleted upper-window witnesses;
- PCSH, including placement of the one or two missing lower-q1 colours.

These are exactly the conditions checked by the successful (k=13)
enumerator and compiler.

## 6. The (k=13) instance

For (k=13),

\[
 r=7,qquad W=\binom{13}{7}=1716,qquad d(13)=3.
\]

The source certificate is a depth-3-resident, all-shadow-complete 2-factor
with two physical cycles of lengths (1547) and (169).  Thus (c=2).
The selected cross seam is

\[
 2515\longrightarrow2391.
\]

It has the following audited properties.

- The resulting Hamilton path is depth-3 resident.
- Every upper shadow at depths (1,\ldots,6) remains complete.
- The original lower-q1 edge colouring is rainbow.
- Two cut colours and one seam colour leave exactly one missing colour,
  (2135).  Thus (h=1).
- The missing colour lies under the right endpoint and is realized by the
  last base entry of the compiled word.
- The full lower PCSH/Hall graph has matching (4095/4095), and the exact
  coordinate compiler is satisfiable.

The resulting word has length (1719) and covers all (8191) nonempty
masks.  This proves \(\nu(13)=1719\).

What is general is Theorem 5.1, the seam ledger, and the two-channel boundary
bound.  What is special to the finite (k=13) certificate is the existence
of a seam simultaneously satisfying all three labelled conditions.  Neither
translation equivariance nor cycle connectivity is needed in the final
theorem.

## 7. A conditional odd-to-even dual-sector recurrence

There is a clean recurrence template, but the present (k=13) word does not
yet satisfy its residence hypothesis.

Let (k=2r-1), introduce a new point (x), and split the middle layer of
([k]\cup\{x\}) into

\[
 \mathcal A=\{S:S\in\tbinom{[k]}r\},
 \qquad
 \mathcal B=\{\{x\}\cup([k]\setminus S):S\in\tbinom{[k]}r\}.
\tag{7.1}
\]

For a path (Q) on \(\binom{[k]}r\), write

\[
 B(Q_i)=\{x\}\cup([k]\setminus Q_i).
\]

For every consecutive block,

\[
 \bigcup_{j=0}^{q}B(Q_{i+j})
 =\{x\}\cup\left([k]\setminus\bigcap_{j=0}^{q}Q_{i+j}\right),
\tag{7.2}
\]

\[
 \bigcap_{j=0}^{q}B(Q_{i+j})
 =\{x\}\cup\left([k]\setminus\bigcup_{j=0}^{q}Q_{i+j}\right).
\tag{7.3}
\]

Thus lower shadows of (Q) become upper shadows in the (B)-sector, and
upper shadows become lower shadows.

### Proposition 7.1 (conditional odd-to-even lift)

Let (P,Q) be Hamilton paths through \(\binom{[k]}r\).  Put
(d_+=d(k+1)).  Assume:

1. (P) is upper-complete and linearly (d_+)-resident.
2. (Q) is lower-complete at every needed depth and is linearly
   (d_+)-**coresident**, meaning every internal 0-run of every coordinate
   has length at least (d_++1).
3. There are endpoints (S=P_{\rm end}), (T=Q_{\rm start}) and a point
   (a\in S) such that
   \[
   T=([k]\setminus S)\cup\{a\}.
   \tag{7.4}
   \]
   Equivalently, (S) and (B(T)) form a Johnson seam.
4. Every coordinate run crossing that seam has total length at least
   (d_++1).  Explicitly, if \(\tau_P(y)\) is the terminal 1-run of (y)
   in (P), and \(\zeta_Q(y)\) is the initial 0-run of (y) in (Q), then
   \[
   \tau_P(a)\ge d_++1,
   \qquad
   \tau_P(y)+\zeta_Q(y)\ge d_++1
   \quad(y\in S\setminus\{a\}).
   \tag{7.5}
   \]
5. Any sole lower-q1 colour (X) missing from (Q) satisfies
   (X=[k]\setminus S).  Then the cross seam has union
   \(\{x\}\cup S\), exactly the (B)-sector upper-q1 mask dual to (X).
6. The concatenated path (P\,B(Q)) satisfies the depth-(d_+) PCSH lower
   compiler.

Then Theorem 5.1 applies in dimension (k+1), and

\[
 \nu(k+1)=B(k+1).
\tag{7.6}
\]

#### Proof

The two sectors in (7.1) partition the new middle layer.  Condition (7.4)
makes their concatenation a Johnson path.  Conditions 1--4 give exact
linear residence.  Upper masks not containing (x) are covered in the
(A)-sector by (P).  By (7.2), upper masks containing (x) are covered by
the lower shadows of (Q); condition 5 repairs the only q1 exception at the
cross seam.  PCSH covers the lower half.  Theorem 5.1 finishes the proof.
\(\square\)

### The (13\to14) audit

For (k+1=14),

\[
 W_{14}=\binom{14}{7}=3432,qquad d(14)=2,qquad
 2W_{14}+\binom32-\sum_{j=1}^{6}\binom{14}{j}=392.
\tag{7.7}
\]

So the scalar lower-cell ledger has slack (392), not an obstruction by
itself.  The exact (k=13) seam path also has the right shadow duality: it
has one lower-q1 hole and no other lower-shadow hole, and a coordinate
permutation can align that hole with (7.4)--(7.5)'s q1 seam target.

However, its coordinate gaps are not 2-coresident.  A direct audit gives
minimum internal 0-run length (1), with (415) internal 0-runs of length
one or two.  Consequently the dual (B)-sector has hundreds of short
internal 1-runs, and its maximal depth-2 erosion does not reproduce the
middle path.  Endpoint alignment cannot repair an internal failure.

Therefore the present (k=13) certificate does **not** by itself prove the
(k=14) case.  A reusable odd-to-even recurrence needs a biresident source
path (or a different (B)-sector construction), followed by the genuine
PCSH check.  Equality \(\nu(k)=B(k)\) alone is insufficient to imply equality
at (k+1).

## 8. Induction target

Define \(\mathsf{SC}(k)\) to mean that dimension (k) has a carrier and a
seam tree satisfying the three hypotheses of Theorem 5.1 at depth (d(k)).
Then

\[
 \mathsf{SC}(k)\Longrightarrow \nu(k)=B(k).
\tag{8.1}
\]

A true (k\mapsto k+2) induction would follow from a **seam-compatible
carrier lift** preserving:

1. middle-layer partition;
2. residence at the new delay;
3. upper-shadow coverage with replacement witnesses at the lifted cuts;
4. a rainbow seam tree with deficit (h\le2), ideally (h=1);
5. PCSH after the two endpoint flags are installed.

The diamond-sector recursion is a candidate for such a lift, but no theorem
currently establishes items 2--5 simultaneously.  The (k=13) proof changes
the induction target in an important way: one need not merge carrier cycles
into a Hamilton cycle.  It is enough to find a seam tree producing a
Hamilton path with one boundary-repairable lower colour.
