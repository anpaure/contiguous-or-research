# The hidden structure of the exact contiguous-OR optima

Date: 2026-07-27

## 1. Scope and status

This note originally analyzed the certified nonzero optima at

\[
k=1,\ldots,10,12
\]

and the then-best length-465 near-solution at (k=11).  It does not infer a theorem
from search output.  Every numerical statement in the original census was recomputed by
`scratch/analyze_exact_beauty.py`; the full raw census is
`scratch/exact_beauty_report.txt`.

### Exact k=11 update

The near-solution status in the historical sections below is now superseded.
The translation-quotient sigma search and Hall compiler produced
`scratch/sigma_sat_k11_465.word`, which independently covers all 2047
nonempty masks.  Together with the monotone-deadline lower bound this proves

\[
\boxed{\nu(11)=B(11)=465}.
\]

Its SHA-256 is
`746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850`.
The exact tableau strengthens rather than breaks the pattern described here:

\[
\begin{array}{c|c|c}
\text{row}&\text{length}&\text{rank profile}\\ \hline
D^0&465&1^{11},2^{55},3^{399}\\
D^1&464&2^1,3^1,4^{462}\\
D^2&463&5^{463}\\
D^3&462&6^{462}.
\end{array}
\]

All lower and upper cyclic shadows are complete through every depth, the
rank-seven cyclic load is exactly (1^{198}2^{132}), and the cyclic residence
minimum is four.  Thus every reference below to the old thirteen-hole word
should be read as historical evidence about the route, not the current
finite status.  The authoritative certificate is
`K11_EXACT_465_SEARCH_CERTIFICATE_20260727.md`.

The central finding is that the stored answers are not merely short words.
From (k=6) onward they are instances of one coherent object: a
Boolean-valued Pascal triangle whose central row is a combination Gray path,
whose lower rows compile the lower ideal, and whose upper rows cover successive
upper ranks.

## 2. The OR-Pascal tableau

For a row (X=(X_0,\ldots,X_{n-1})) define

\[
(DX)_i=X_i\cup X_{i+1}.
\]

Associativity and idempotence give

\[
(D^jX)_i=X_i\cup X_{i+1}\cup\cdots\cup X_{i+j}.
\tag{2.1}
\]

Thus all interval ORs are the cells of the triangular tableau

\[
A,\ DA,\ D^2A,\ldots .
\]

Put

\[
r=\lceil k/2\rceil,\qquad W=\binom kr,\qquad d=B(k)-W.
\]

Every stored nontrivial optimum from (k=6) onward has

\[
\boxed{D^dA\text{ equal to a permutation of }\binom{[k]}r.}
\tag{2.2}
\]

For (k=7,8,9,10,12), (d=2); at (k=6), (d=1).  The first unresolved case,
(k=11), has (d=3), and its best near-solution also satisfies (2.2) exactly.

This is a strong construction normal form, not a proved consequence of
optimality.

## 3. The rank grading has an exact canonical form

The first census showed only a near-grading because several stored
representatives contained a handful of premature masks.  Those defects were
not forced.  Envelope-preserving edits of one entry at (k=7), four at
(k=10), two at (k=11), and four at (k=12) leave the central row (and
full coverage, where present) unchanged and give the canonical files

\[
\begin{gathered}
\texttt{k7\_published\_rank\_exact.txt},\quad
\texttt{k10\_optimal\_rank\_exact.txt},\\
\texttt{k11\_upper549\_rank\_exact\_flag.txt},\quad
\texttt{k12\_optimal\_rank\_exact.txt}.
\end{gathered}
\]

Together with the existing (k=6,8,9) representatives, every informative
answer from (k=6) onward therefore has a **rank-monotone,
capacity-exact** representative: scanning shortest window lengths from left
to right never skips over a lower rank, and at most one rank straddles a row
boundary.  The sole straddle in the clean exact data is forced at (k=9):
there are 129 masks of ranks at most three but only 128 length-one cells.

For (k=7,10,12) the normal form is even sharper.  Put
(s=r-d).  Every nonzero mask satisfies the rank clock

\[
\boxed{
\text{shortest window length of }S
=\max\{1,\,|S|-s+1\}.}
\tag{3.0}
\]

The canonical (k=11) near-word satisfies the same identity for every mask
it covers, while leaving exactly the same thirteen upper masks absent.  The
identity and every edit are checked by
`scratch/verify_rank_exact_representatives.py`; the complete factor theorem
behind the boundary edits is in
`MATH_BOUNDARY_FLAG_FACTOR_THEOREM_20260727.md`.

The new masks first appearing in the bottom rows have the following form.

| object | row 0 | row 1 | row 2 | row 3 |
|---|---|---|---|---|
| (k=6) optimum | all ranks 1--2 | all rank 3 | -- | -- |
| (k=7) canonical optimum | all ranks 1--2 | all rank 3 | all rank 4 | -- |
| (k=8) optimum | all ranks 1--2 | all rank 3 | all rank 4 | -- |
| (k=9) optimum | all ranks 1--2 and 83/84 rank-3 sets | last rank-3 set plus all rank 4 | all rank 5 | -- |
| (k=10) canonical optimum | all ranks 1--3 | all rank 4 | all rank 5 | -- |
| (k=11) canonical near-word | all ranks 1--3 | all rank 4 | all rank 5 | all rank 6 |
| (k=12) canonical optimum | all ranks 1--4 | all rank 5 | all rank 6 | -- |

Here “row (j)” means (D^jA), and a mask is charged to its shortest window.

The (k=11) line is especially important.  Its lower triangle is already
perfect: all 1,023 lower masks occur in the first three rows, and the fourth
row is the complete central layer.  The thirteen absent masks are twelve
rank-seven sets and one rank-eight set.  The difficulty at the first
(d=3) case is therefore not lower-rank capacity or factor labeling; it is
entirely in the upper chronology.

For these small delays, the rows happen to align almost one-for-one with
ranks:

\[
\begin{array}{c|c}
D^0A&\text{ranks at most }r-d,\\
D^jA&\text{rank }r-d+j\quad(1\le j<d),\\
D^dA&\text{rank }r,\\
D^{d+q}A&\text{rank }r+q\quad(q\ge1),
\end{array}
\tag{3.1}
\]

where “rank” means that the row covers that complete layer; unavoidable
duplicates and boundary cells may have other ranks.  Equation (3.1) is a
finite low-delay pattern, **not** a viable asymptotic theorem.  Indeed
(d\sim\sqrt{\pi k/8}), while a normal approximation gives

\[
\sum_{j\le r-d}\binom kj=\Theta(2^k)
=\Theta(\sqrt{k}\,W),
\]

whereas row zero has only (W+d=(1+o(1))W) cells.  For large (k), row zero
cannot possibly contain all ranks through (r-d).

The correct general target is therefore **capacity-ordered grading**:

1. the first (d) rows contain no masks above the middle rank;
2. their new masks cover the whole lower ideal;
3. shortest-witness depth is nondecreasing with rank (one rank may straddle a
   row boundary when a row capacity cuts through it); and
4. (D^dA) is the central permutation, after which the upper rows cover the
   successive upper layers.

This formulation keeps the cell-by-cell lower-bound geometry without making
the impossible demand that one derivative row equal one rank asymptotically.

The arithmetic behind this corrected formulation is now exact.  Write

\[
c_j=W+d-j,\qquad
L=\sum_{s<r}\binom ks,\qquad
e=\sum_{j<d}c_j-L,
\]

and let \(u_j\) be the number of lower masks first witnessed in row \(j\).
Then

\[
0\le u_j\le c_j,\qquad \sum_{j<d}u_j=L,
\tag{3.1a}
\]

so the row wastes \(\delta_j=c_j-u_j\) are nonnegative and sum exactly to
the rank slack \(e\).  If

\[
Q_j=\sum_{h\le j}c_h,qquad U_j=\sum_{h\le j}u_h,
\]

then every rank-monotone schedule lies in the sharp quantile envelope

\[
\boxed{Q_j-e\le U_j\le\min\{Q_j,L\}.}
\tag{3.1b}
\]

Conversely, every integer slack path inside this envelope gives an abstract
rank-ordered allocation (the OR--Pascal recurrence is the remaining geometric
condition).  Thus there is no hidden *rank-count* obstruction once a rank is
allowed to split at a row boundary.  Whole-rank rows are genuinely too rigid:
at \(k=14\), row zero is forced to take between \(1572\) and \(1964\) of the
\(2002\) rank-five masks.

The maximally deferred quantile has

\[
U_{d-1-t}=L-tW-\binom{t+1}{2}.
\tag{3.1c}
\]

Its last few cuts move about one rank per row, explaining the finite rank
clock.  Its row-zero cut is instead typically
\(\Theta(\sqrt{k\log k})\) below the middle when row zero carries
\(\Theta(W)\) new masks.  This moderate-deviation transition is the precise
large-\(k\) replacement for the misleading boundary \(r-d\).  The full proof
and the finite waste vectors are in
`MATH_CAPACITY_ORDERED_OR_PASCAL_QUANTILES_20260727.md`.

There is also a normalization-independent skeleton forced by equality at
\(B(k)\).  Choose one physical interval for each middle-rank target and order
them by left endpoint:

\[
I_i=[a_i,b_i]\qquad(1\le i\le W).
\]

Equal-rank intervals cannot nest, so both endpoint sequences are strictly
increasing and

\[
\boxed{I_i\subseteq[i,i+d].}
\tag{3.1d}
\]

Every interval of length at least \(d+1\) contains one of these middle
witnesses; hence every lower target must be assigned to the width-\(d\) band
of shorter physical intervals.  Fixed-left and fixed-right intervals form
two transverse strict inclusion chains, and the number of unused band cells
is exactly the rank slack \(e\).  Thus equality forces an **ordered
orthogonal double-chain packing** of the entire lower ideal, even before any
central-row normalization is assumed.

What equality does *not* force is flatness.  The optimal \(k=4\) word

\[
(10,9,5,1,2,4,8)
\]

is universal at length \(B(4)=7\), but its first derivative is not the middle
layer, and no one-entry nonzero edit can make it so.  The beautiful flat
central row seen from \(k=6\) onward is therefore a selected global normal
form, not a formal consequence of the scalar lower bound.

There is now a short normalization-free proof of that scalar lower bound.
For column \(i\), let \(f_i\) be the number of its initial cells below the
middle rank, and put \(F_i=i+f_i\).  Inclusion of the shifted cells gives

\[
f_{i+1}\ge f_i-1,
\qquad F_{i+1}\ge F_i.
\tag{3.1e}
\]

Distinct middle targets have distinct deadlines \(F_i\): if two equal-rank
intervals end at the same position, the later one is contained in the
earlier and hence has the same OR label.  Thus a length \(W+e\) word has at
least \(W\) distinct finite deadlines, which forces

\[
f_i\le\min\{e,W+e-i+1\}.
\]

Counting all lower targets now gives

\[
\sum_{s<r}\binom ks
\le\sum_i f_i
\le eW+\binom{e+1}{2}.
\tag{3.1f}
\]

This proves \(e\ge d(k)\), hence \(\nu(k)\ge B(k)\), directly.  At
\(e=d\), if

\[
\sigma_k=dW+\binom{d+1}{2}-\sum_{s<r}\binom ks,
\]

then the inequality has the exact loss decomposition

\[
\boxed{\sigma_k
=\sum_i\bigl(\min\{d,W+d-i+1\}-f_i\bigr)
+\left(\sum_i f_i-\sum_{s<r}\binom ks\right).}
\tag{3.1g}
\]

The two terms are, respectively, unused deadline depth and repeated lower
occurrences.  Therefore \(\sigma_k=0\) really does force the flat central
row and a bijective lower band (as at \(k=6,9\)); positive slack does not.
The full proof and the corrections to the stronger equality claims are in
`MONOTONE_DEADLINE_LOWER_BOUND_AND_EQUALITY_AUDIT_20260727.md`.

Arbitrary witness retiming nevertheless has an exact test.  For a prescribed
interval \(I_S\) for every nonzero mask, define

\[
Z_b=[n]\setminus\bigcup_{S:\,b\notin S}I_S.
\]

The whole assignment is realizable by a nonzero word if and only if every
positive interval \(I_S\) meets every required \(Z_b\) and
\(\bigcup_bZ_b=[n]\).  The maximal realization is \(A_i=\{b:i\in Z_b\}\).
Consequently the missing normalization theorem is now precise: a coupled
central-straightening exchange and rank cut-compression exchange, each
preserving the other's witness system.  See
`MATH_OPTIMAL_NORMALIZATION_EXCHANGE_20260727.md`.

For (k=11), (3.1) asks for row capacities

\[
465\ge231,\qquad464\ge330,\qquad463\ge462,\qquad462=462,
\]

which explains why the observed grading is arithmetically exact.

There is an even sharper cell-by-cell statement.  The rank-slack lower bound
counts exactly the cells in rows (0,\ldots,d-1):

\[
\sum_{j=0}^{d-1}(W+d-j)=dW+\binom{d+1}{2}.
\tag{3.2}
\]

The stored tableaux use this pool with no high-rank waste:

| object | short cells | lower-rank occurrences | central occurrences | high-rank occurrences | repeated lower occurrences |
|---|---:|---:|---:|---:|---:|
| (k=6) | 21 | 21 | 0 | 0 | 0 |
| (k=7) | 73 | 73 | 0 | 0 | 10 |
| (k=8) | 143 | 143 | 0 | 0 | 51 |
| (k=9) | 255 | 255 | 0 | 0 | 0 |
| (k=10) | 507 | 505 | 2 | 0 | 120 |
| (k=11), near | 1,392 | 1,392 | 0 | 0 | 369 |
| (k=12) | 1,851 | 1,849 | 2 | 0 | 264 |

In every row, “repeated lower occurrences + short central occurrences” is
exactly the arithmetic slack in the lower-bound inequality.  In particular,
the zero-slack (k=9) optimum makes the first two derivative rows a literal
bijection onto the entire lower ideal.  The lower bound is not merely met in
length; its proof is realized geometrically cell by cell.

Each vertical diagonal is itself an inclusion chain,

\[
A_i\subseteq (DA)_i\subseteq\cdots\subseteq(D^dA)_i=T_i
\subseteq(D^{d+1}A)_i\subseteq\cdots .
\tag{3.3}
\]

Thus the tableau is a system of (W) chains crossing the middle layer, coupled
by the Pascal relation between neighboring columns.  At (k=9), the lower
parts of these diagonals partition the lower ideal exactly.  This is the
closest finite analogue of an SCD in the data, but with a crucial extra
condition: neighboring chains are not independent; their cells must union to
the cell directly above them.  “SCD plus Pascal compatibility” is a concise
description of the exact construction problem.

## 4. The central row is a two-sided universal Gray path

In the clean representatives at (k=6,7,8,9,10,11,12), consecutive central
sets are Johnson adjacent.  Write

\[
T_{i+1}=T_i-\{a_i\}+\{b_i\}.
\tag{4.1}
\]

Then, for every (q),

\[
\bigcap_{j=0}^qT_{i+j}
=T_i\setminus\{a_i,\ldots,a_{i+q-1}\},
\qquad
\bigcup_{j=0}^qT_{i+j}
=T_i\cup\{b_i,\ldots,b_{i+q-1}\}.
\tag{4.2}
\]

The formula remains true when a coordinate repeats: set union/deletion
automatically ignores repetitions.  Hence the whole shadow tower is encoded
by the two transition words (a_0a_1\cdots) and (b_0b_1\cdots).

The central path is therefore much more than Hamiltonian.  Its consecutive
deletion prefixes cover lower ranks and its consecutive arrival prefixes
cover upper ranks.

There is an exact local-time identity behind the rank impurities.  In a block

\[
T_i,T_{i+1},\ldots,T_{i+q}
\]

let (Z_0(i,q)) be the number of coordinate zero-runs which are strictly
internal to the block (a coordinate is present, absent for a nonempty run,
then present again), and define (Z_1(i,q)) dually.  Then

\[
\boxed{
\begin{aligned}
\left|\bigcup_{j=0}^qT_{i+j}\right|&=r+q-Z_0(i,q),\\
\left|\bigcap_{j=0}^qT_{i+j}\right|&=r-q+Z_1(i,q).
\end{aligned}}
\tag{4.3}
\]

Indeed, the block has exactly (q) additions.  The first addition of a
coordinate absent from (T_i) enlarges the union; every other addition closes
one internal zero-run and does not.  The intersection identity is the dual
count for removals.  The analyzer checks (4.3) block by block for every stored
answer.

Summed over all starting positions, (4.3) turns derivative-row waste into a
weighted run spectrum.  An internal zero-run of length (\ell<q), away from
the two global boundaries, lies inside exactly (q-\ell) depth-(q) blocks;
it therefore contributes (q-\ell) units of upper rank deficit.  Internal
one-runs give the identical formula for lower rank excess.  For example, the
(k=11) near-word has 44 zero-runs of length one and 80 of length two.  Its
depth-two upper row has exactly 44 units of rank deficit, and its depth-three
row has

\[
2\cdot44+80=168
\]

units.  Likewise its 149 minimum-length four-runs account for the 149
non-rank-one cells at lower depth five.  Thus the conspicuous row impurities
are not noise from the search: they are the precise local-time shadow of the
residence process.

At depth one the census is:

| object | lower holes / CPCR | upper holes / CPCR | upper load profile |
|---|---:|---:|---|
| (k=7) | 1 / 0 | 0 / 4 | (1^{10}2^9 3^2) |
| (k=8), clean alternative | 2 / 4 | 0 / 2 | (1^{44}2^{11}3) |
| (k=9) | 1 / 0 | 0 / 14 | (1^{50}2^{27}3^7) |
| (k=10) | 0 / 2 | 0 / 4 | (1^{171}2^{37}3^2) |
| (k=11), near | 1 / 0 | 12 / 60 | (0^{12}1^{193}2^{107}3^{18}) |
| (k=12) | 0 / 4 | 0 / 24 | (1^{672}2^{110}3^9 4) |

Here CPCR is

\[
\sum_S(L(S)-c)(L(S)-c-1),\qquad
c=\left\lfloor{\text{number of path edges}\over\text{number of colours}}\right\rfloor.
\]

The successful immediate shadows are extraordinarily close to the integrality
floor: their CPCR errors are (O(k)), not (\Theta(W)).  This is the finite
counterpart of the current asymptotic balanced-shadow objective.

For (k=10), every lower and upper sliding shadow of the central path is
complete.  For (k=12), every upper shadow is complete; all lower shadows are
complete except one rank-three set at depth three.  The path is therefore a
genuine multidepth object, not merely a depth-one rainbow path.

## 5. Missing lower shadows form a boundary flag

The lower-shadow failures are much more organized than arbitrary holes.

* At (k=7), the only missing central intersections are
  \(\{5,7\}\subset\{1,5,7\}\).
* At (k=9), they are
  \[
  \{2,4\}\subset\{2,4,6\}\subset\{2,4,6,8\}.
  \tag{5.1}
  \]
* At (k=8), one clean representative misses only one immediate lower colour.
* At (k=10), there is no lower-shadow hole.

The missing objects in (5.1) form one flag.  The extra boundary cells in the
factor rows supply exactly that flag.  Thus the linear cut does not create a
cloud of unrelated defects; it removes one nested boundary object.

This suggests a stronger and more constructive target than raw shadow
coverage:

> Construct a central Hamilton path whose lower sliding-shadow deficits are
> contained in one flag and whose upper sliding shadows are complete.

For general delay (d), one boundary flag has exactly the right shape to be
absorbed by the (d) extra cells of a length-(W+d) factor.

There is a sharper interpretation in odd dimension.  Write (k=2m+1), so
the central row consists of the (W) rank-((m+1)) sets and the next lower
rank also has size (W).  Suppose the (W-1) adjacent intersections

\[
C_i=T_i\cap T_{i+1}
\]

are distinct, miss only (C_*), and (C_*\subset T_{W-1}).  Then

\[
T_0,C_0,T_1,C_1,\ldots,C_{W-2},T_{W-1},C_*
\tag{5.2}
\]

is a Hamilton path of the middle-levels graph on ranks (m) and (m+1).
Conversely, projecting any such endpoint-oriented middle-levels Hamilton
path onto its rank-((m+1)) vertices gives exactly this central-path
condition.  This is immediate because consecutive terms in (5.2) are
incident, and the two rank classes are each exhausted once.

The published (k=7) optimum, the (k=9) optimum, and the (k=11)
near-word all pass this test; their terminal lower vertices are respectively
(81,170,31) in bit-mask notation.  Thus their immediate lower-rainbow
property is not merely analogous to the Middle Levels Theorem: the stored
central rows are literal projections of endpoint-rooted middle-levels
Hamilton paths.  At (k=7,9), the deeper missing shadows continue downward
from this terminal vertex as the flag above.

This changes the natural search space.  For odd (k), the immediate lower
shadow and its boundary repair can be built in by searching endpoint-rooted
middle-levels Hamilton paths.  The nonclassical requirements are then:

1. their projected Johnson path must cover the opposite (union) colours;
2. its coordinate residence must be at least (d+1); and
3. its deeper intersection deficits must stay inside the terminal flag.

The exact examples say these three conditions can coexist; the usual middle
levels theorem supplies only the underlying Hamilton path.

The endpoint absorption question itself is now exact.  For
(x\in T_{W-1}), let (\lambda_x) be its terminal residence length, and let

\[
F_1\supseteq F_2\supseteq\cdots\supseteq F_d
\]

be the desired right OR-Pascal anti-diagonal.  There is a delay-(d) factor
with precisely this boundary flag if and only if

\[
F_q\subseteq T_{W-1},\qquad
\{x:\lambda_x\le d-q+1\}\subseteq F_q
\quad(1\le q\le d).
\tag{5.3}
\]

This is Theorem 4.1 of
`MATH_BOUNDARY_FLAG_FACTOR_THEOREM_20260727.md`.  Its proof is
coordinatewise: the zero preceding a terminal 1-run forces the first legal
factor occurrence to position (W-\lambda_x+d), and the desired suffix
height determines its last occurrence.  Thus “one flag” is not merely a
shape heuristic; terminal residence gives a necessary-and-sufficient local
test.  The canonical (k=11) word realizes the literal flag

\[
31\supset15\supset11.
\]

The same report proves a more general fact: after central and lower cells are
specified, feasibility is exactly an interval-hitting test for each
coordinate.  Hence factor completion has no hidden integrality gap.  The
remaining lower-side issue is solely the selection of a compatible set of
nonboundary pins.

## 6. Factor labels are sparse shrinkings of a maximal object

Once (T=D^dA) is fixed, put

\[
E_j=\bigcap\{T_i:[i,i+d]\ni j\}.
\tag{6.1}
\]

Every legal factor satisfies (A_j\subseteq E_j), and (E) is the unique
coordinatewise maximal factor.  The stored words preserve the maximal factor
at the following numbers of positions:

| object | (A_j=E_j) | penultimate derivative preserved | central row preserved |
|---|---:|---:|---:|
| (k=7) | 26/37 | 33/36 | 35/35 |
| (k=9) | 81/128 | 124/127 | 126/126 |
| (k=10) | 146/254 | 238/253 | 252/252 |
| (k=11), near | 173/465 | 461/463 at (D^2), 393/464 at (D) | 462/462 |
| (k=12) | 503/926 | 870/925 | 924/924 |

Hundreds of entries can therefore be shrunk to encode small masks while the
next derivative row changes at only a small fraction of its cells and the
central row does not change at all.  This is an error-correcting phenomenon:
the maximal intersection envelopes provide redundancy, and factor labeling
spends that redundancy on the lower ideal.

It points toward a labeling theorem based on *preservable shrink sites*, not
merely envelope containment.  A useful sufficient statement would identify a
large set of positions at which arbitrary prescribed submasks can be installed
while a designated cover in each of the next (d-1) rows retains at least one
unchanged witness.

This labeling stage now has an exact normal form.  After the chosen
intermediate cells prune the envelopes to (F_p), choose a coordinatewise
interval-stabbing core (H_p\subseteq F_p).  A set (mathcal L_0) of
row-zero target masks can be installed if and only if the bipartite graph

\[
L\sim p\iff H_p\subseteq L\subseteq F_p
\tag{6.2}
\]

has a matching saturating (mathcal L_0), for some such core (H).
Conversely, a matching gives the factor explicitly: put (A_p=L) at matched
sites and (A_p=F_p) elsewhere.  This is Theorem 3.1 of
`MATH_PRESERVABLE_SHRINK_HALL_THEOREM_20260727.md`.  Thus preservable
shrinking is **interval stabbing plus ordinary Hall**, with no further
rounding problem.

The distinction between minimum witness mass and Hall compatibility is real.
For the canonical (k=12) central row, the right-endpoint minimum core has
one five-target/four-position Hall obstruction; splitting the coordinate-12
witness at position 527 into positions 526 and 528 adds one bit and repairs
the matching completely.  In the full finite audit, Hall-compatible protected
cores exist at (k=7,10,11,12), and reconstruct all certified lower pins
while leaving every upper derivative unchanged.  The remaining theorem is
therefore a joint *choice* theorem for pins and witness phases, not factor
completion.

The words are simultaneously fragile.  The numbers of masks having a unique
shortest witness are

\[
101/127,\ 184/255,\ 437/511,\ 776/1023,\ 3247/4095
\]

for the displayed (k=7,8,9,10,12) representatives.  Most targets therefore
cannot survive an arbitrary local edit.  This explains why successful repair
moves have to be shadow-preserving circuits rather than independent position
changes: the redundancy exists in the envelope rows, but it is highly
structured.

## 7. Residence is saturated at the factorability threshold

The exact factorization criterion says that every internal coordinate 1-run
in (T) must have length at least (d+1).  In every clean stored central path,
the minimum is exactly (d+1):

\[
2\text{ at }(k,d)=(6,1),\qquad
3\text{ in all }d=2\text{ examples},\qquad
4\text{ in the }k=11,d=3\text{ near-word}.
\]

Many runs attain the minimum.  Thus the central path sits on the boundary of
factorability.  Short residence creates diverse shadows; too-short residence
destroys the preimage.  The optima balance those two demands exactly.

For a fully Johnson central path this is also a local condition on the two
transition words.  If (b_i=x) is the entry of coordinate (x), and its next
removal is (a_{i+\ell}=x), then the resulting internal 1-run has length
(\ell).  Consequently delay-(d) factorability is equivalent (apart from
the two boundary runs) to the cooldown rule

\[
b_i\ne a_{i+\ell}\qquad(1\le \ell\le d).
\tag{7.1}
\]

The analyzer verifies zero matches at these lags in every fully Johnson clean
example, followed by a large spike at lag (d+1).  The words do not merely
respect (7.1); they reuse a coordinate as soon as factorability permits.

The zero-runs are not similarly bounded: quick departures and returns create
the lower-rank contaminants in upper derivative rows.  Equation (4.2) shows
that repeated arrival/departure labels, rather than a mysterious high-order
effect, are the entire source of those contaminants.

More precisely, a match (a_i=b_{i+\ell}) records an internal zero-run of
length (\ell).  Such a removal/reentry inside a block makes a later arrival
already belong to the block's first central set, so the corresponding union
fails to gain the expected rank.  Thus the two temporal collision spectra

\[
b_i=a_{i+\ell}\quad\hbox{and}\quad a_i=b_{i+\ell}
\tag{7.2}
\]

have different jobs: the first is the hard factorability constraint; the
second is the exact accounting of upper-row waste.  A useful central search
should therefore impose the first spectrum as a hard cooldown and optimize
the second spectrum jointly with upper-shadow CPCR, instead of treating all
coordinate repetitions alike.

The cooldown also has a purely tableau-local form.  Put

\[
L_i^{(q)}=\bigcap_{h=0}^{q}T_{i+h}.
\]

If all internal 1-runs have length at least (q), then

\[
\boxed{L_i^{(q)}=L_{i+1}^{(q)}\iff b_i=a_{i+q}.}
\tag{7.3}
\]

The equality on the right is precisely a 1-run of length (q).  Under the
shorter-run exclusion, passing from (L_i^{(q)}) to (L_{i+1}^{(q)})
either replaces (a_{i+q}) by (b_i), or does nothing when they coincide.
Induction on (q) therefore gives an equivalent staged factorability test:

> A Johnson path has internal 1-runs at least (d+1) if and only if, for
> every (1\le q\le d), the depth-(q) intersection row has no equal
> adjacent cells.

This is much weaker than requiring every lower shadow to be globally
rainbow.  The new q1-perfect (k=11) overlay certificate has no length-one
runs automatically; its 83 length-two runs are exactly its 83 adjacent
repetitions at depth two.  A connector search can therefore impose two local
no-repeat constraints at depths two and three instead of encoding the whole
delay-three factor.

## 8. The beauty is structural, not symmetric

The analyzer found no coordinate permutation carrying the principal central
paths to their reversals or complement-reversals.  It also found no literal
coordinate-section isomorphism from the stored (k=7) path to the (k=8) path,
or from (k=9) to (k=10).  Earlier deletion audits likewise showed that simple
two-coordinate filtering does not recover smaller optima.

So the recurring object is not one visibly recursive word.  What recurs is
the *category* of the object:

1. exact central derivative row;
2. long-enough coordinate residence;
3. nearly balanced two-sided sliding shadows;
4. a nested boundary defect; and
5. a sparse shrinking of the maximal factor.

This makes a theorem about an ensemble or a compiler more plausible than a
single closed-form Gray code.

## 9. A new exact projection from the k=12 optimum

The (k=12) central path contains one distinguished coordinate, number 12.
It changes only 50 times; the other coordinates change about 160 times.
Delete coordinate 12 and split the path at its changes.

* The 462 central sets not containing 12 form a rank-six forest in the
  eleven-cube with 26 components and 436 edges.  Its rank-seven union colours
  cover all 330 targets.  Its rank-five intersection colours cover 428/462.
* The 462 central sets containing 12, after deleting 12, form a rank-five
  forest with 25 components and 437 edges.  Its rank-four intersection
  colours cover all 330 targets.  Its rank-six union colours cover 426/462.

This is an instance of a general projection lemma.

### Lemma 9.1 (coordinate sections of a two-sided path)

Let (T) be a Hamilton path in (J(2m,m)) whose adjacent unions cover every
(m+1)-set and whose adjacent intersections cover every (m-1)-set.  Fix a
coordinate (z).

1. The vertices avoiding (z) form a spanning rank-(m) path forest on the
   remaining (2m-1) coordinates, and its adjacent unions cover every
   (m+1)-set of that ground set.
2. The vertices containing (z), after deleting (z), form a spanning
   rank-(m-1) path forest, and its adjacent intersections cover every
   (m-2)-set.

#### Proof

An (m+1)-target avoiding (z) can only be the union of two central sets which
both avoid (z); its witnessing edge therefore lies inside an avoiding run.
The lower statement is the complement: an (m-1)-target containing (z) can
only be the intersection of two central sets which both contain (z).  Delete
(z) from that edge.  The spanning statements follow because (T) lists the
whole central layer.  QED.

If (c_z^0) is the number of avoiding runs, then

\[
\sum_zc_z^0=m+(W-1),
\tag{9.1}
\]

because the initial central set omits (m) coordinates and each Johnson
transition starts exactly one new zero-run.  Hence some coordinate has only

\[
{W+m-1\over2m}=O(W/m)
\]

components.  Projection therefore produces Catalan-scale one-sided forests
for free.  The exceptional coordinate 12 in the stored optimum is a factor
three better than this average.

This gives a concrete recursive route: prove a coloured connector theorem
which joins the (O(W/m)) section components while preserving their already
perfect side and repairing the opposite (O(W/m)) colour defect.

## 10. The k=11/k=12 sparse overlay

Overlay the rank-six avoiding forest from Section 9 with the current (k=11)
near-Hamilton path.

\[
\begin{array}{c|c|c|c}
&\text{edges}&\text{lower colours}&\text{upper colours}\\ \hline
k=12\text{ section forest}&436&428&330\\
k=11\text{ near path}&461&461&318\\
\text{union}&532&461&330.
\end{array}
\tag{10.1}
\]

The paths share 365 edges.  Thus the union contains both desired colour
marginals in a graph with only 532 of the 6,930 Johnson edges.

The raw union is not itself sufficient.  If one selects one edge of each of
the 461 available lower colours and insists on every upper colour, singleton
colour classes force degree three at six vertices.  The exact offending
vertices are

\[
1699,1880,1203,365,243,948.
\]

This is a statewise obstruction to the naive splice, but it is highly local.
It says exactly what a reservoir must do: provide alternative realizations of
the seven forced upper colours meeting those vertices.  A connectivity-cut
SAT search using `scratch/search_k11_k12_overlay.py` has now produced a
certificate path.  Its lower colours are (1^{461}) (sole hole (31)); its upper
profile is (1^{223}2^{86}3^{18}4^3), so all 330 upper colours occur.  The path
uses 295 edges outside (10.1), hence lies in an explicit 827-edge augmentation
of the raw overlay.  The result and independent verifier are recorded in
`K11_K12_OVERLAY_CERTIFICATE_20260727.md` and
`scratch/verify_k11_k12_overlay_certificate.py`.

This closes only the depth-one coloured-connector gate.  The path has 150
internal coordinate one-runs of length two or three, so it is not the third
derivative of a length-465 factor.  Delay-three residence remains open.

That residence defect has now been reduced to a genuinely small exchange
problem.  Cutting \(s\) path edges exposes \(2s\) component ends; every
reconnection is exactly a perfect matching of those ends, and it is a
Hamilton path exactly when the contracted component graph is connected.
Lower colours, upper colours, and residence are static labels/filters on the
new matching edges.

More precisely, a length-\(q\) internal one-run has a \((q+1)\)-edge witness
interval.  Any reconnection whose cut set misses that interval leaves the run
unchanged.  Hence the minimum possible order of a one-shot stage-\(q\) repair
is at least the transversal number of an ordinary interval family (and that
number is greedily computable).

Colour-preserving staged 3-opt descent on the verified depth-one path reduces
the short-run spectrum from

\[
(83,67)\quad\hbox{to}\quad(10,77)
\]

at lengths two and three.  The ten remaining length-two witness intervals
are pairwise disjoint, proving that any one-shot depth-two repair uses at
least ten cuts.  The first natural ten-cut choice was then ruled out by a
hand certificate: each exposed endpoint contains only its original removed
lower colour from the admissible palette, so the unique rainbow perfect
matching merely restores the deleted edges.  Across all one-cut-per-witness
choices the missing lower colour is absent from all forty relevant vertices;
any viable connector must therefore contain a nontrivial rainbow alternating
circuit on the ten removed colours.  Independently, one cut hits at most four
length-three witnesses, so a direct delay-three repair requires at least
twenty cuts.

This is negative locally but positive conceptually: “repair residence” is no
longer a 462-vertex Hamilton search.  It is a staged coloured matching
problem on 20 ends for depth two, followed by a necessarily larger matching
for depth three.  The exact exchange theorem and the two finite obstructions
are in `STAGED_RESIDENCE_CONNECTOR_20260727.md` and
`K11_TEN_CUT_S0_MATCHING_OBSTRUCTION_20260727.md`.

## 11. A two-coordinate diamond lift

Let the old ground set have size (2m+1), let
(T_i,T_{i+1}) be a central Johnson edge, and put

\[
C_i=T_i\cap T_{i+1},\qquad U_i=T_i\cup T_{i+1}.
\]

After adding coordinates (x,y), the four sets

\[
C_i\cup\{x,y\},\quad
T_i\cup\{x\},\quad
U_i,\quad
T_{i+1}\cup\{y\}
\tag{11.1}
\]

all have the new central rank and form a Johnson 4-cycle.  The four sectors
of the new middle layer are exactly

\[
\binom{[n]}{m}\!+xy,\quad
\binom{[n]}{m+1}\!+x,\quad
\binom{[n]}{m+1}\!+y,\quad
\binom{[n]}{m+2}.
\]

Thus an old path with near-rainbow lower colours and surjective upper colours
already names every vertex needed for a two-coordinate central lift.  The
remaining problem is a routing problem through overlapping diamonds, not a
search for labels.

### Lemma 11.1 (central diamond lift)

Suppose the old central path has distinct lower colours (C_i), missing only
(C_*), with (C_*\subseteq T_{W-1}), and its upper colours cover the whole
rank-(m+2) layer.  Then the new central layer has a Hamilton path.

#### Proof

Put (X_i=T_i+x), (Y_i=T_i+y), and (Z_i=C_i+xy).  Traverse

\[
X_0,Z_0,X_1,Z_1,\ldots,Z_{W-2},X_{W-1},C_*+xy,Y_{W-1}.
\]

For every distinct upper colour (U), choose one index (i) with (U_i=U).
Continue backward through (Y_{W-1},\ldots,Y_0), inserting the chosen (U_i)
between (Y_{i+1}) and (Y_i).  Every displayed step is a Johnson edge, by
(C_i\subset T_i,T_{i+1}\subset U_i).  The four sectors are disjoint and the
choices use each upper set once, so every new central set occurs exactly
once.  QED.

Applied to the exact (k=9) path, this gives an explicit 462-vertex Hamilton
path in (J(11,6)).  The direct experiment is diagnostically useful but not a
solution: it covers only 283/462 lower and 210/330 upper immediate colours,
and one new coordinate has 207 internal one-runs of length one.  Individual
upper insertions destroy delay-three factorability.

The correction is forced by arithmetic: upper-sector vertices must be
batched.  Let

\[
N_+=\binom{2m+1}{m+2}={m\over m+2}W.
\]

A block of (s) upper-sector vertices inserted into a spine contributes
(s-1) internal lower colours and two seam colours, hence (s+1) zero-new-bit
lower colours.  Covering all (W) such colours with (N_+) vertices requires
exactly

\[
W-N_+={2W\over m+2}
\tag{11.2}
\]

blocks at the no-waste threshold.  Split them evenly between the (x)- and
(y)-spines.  Each spine then has average gap

\[
{W\over (W-N_+)/2}=m+2,
\]

which exceeds the required delay-four residence at the (k=9\to11) step.
This is the sharp residence-compatible version of the diamond lift: a
two-lane Catalan block schedule, not isolated insertions.

The block schedule is in fact forced by the one-flag property.  Let
(K=2r-1), and suppose a rank-(r) Hamilton path has distinct adjacent
intersections comprising every rank-((r-1)) set except (C_*).  For a pair
({x,y}), let (b_{xy}) be the number of maximal path blocks in which both
coordinates occur.  Then

\[
\boxed{b_{xy}=C_{r-1}+\mathbf 1_{\{x,y\}\subseteq C_*}.}
\tag{11.3}
\]

To prove this, let (V_{xy}) count central vertices containing the pair and
(E_{xy}) count path edges whose intersection contains it.  Each 1-block
contributes one more vertex than internal edge, so

\[
b_{xy}=V_{xy}-E_{xy}
=\binom{K-2}{r-2}-\binom{K-2}{r-3}
+\mathbf1_{\{x,y\}\subseteq C_*},
\]

and the binomial difference is (C_{r-1}).  Consequently, choosing any pair
not contained in (C_*) gives exactly the Catalan number of both-present
blocks.  Moreover their internal edges are automatically rainbow: the global
intersection colours are distinct and omit only (C_*), which does not
contain the chosen pair.

Thus Target B feeds the recursive lift much more directly than first
expected.  A one-missing-colour lower-rainbow path already supplies the
correct Catalan forest, its exact component count, and all of its lower
colours—no separate batching selection theorem is needed.

The complete verified pair-block distributions are

\[
\begin{array}{c|c|c}
k&C_{r-1}&\{b_{xy}\}\ \text{over all pairs}\\ \hline
7&5&5^{18},6^3\\
9&14&14^{30},15^6\\
11&42&42^{45},43^{10}.
\end{array}
\tag{11.4}
\]

The ceiling pairs are exactly the pairs inside the missing terminal colour.
For the (k=11) pair ({6,10}), the four sector block counts are
((42,41,43,36)), both new-coordinate residence minima are four, all 84
both-present lower colours occur once, and the neither-present upper sector
is complete.  The immediate residue is precisely one boundary lower colour
and twelve upper colours, split (3+4+5) among the other three sectors.
These facts and (11.3) are proved and reproduced in
`DIAMOND_BRAID_ANALYSIS_20260727.md`.

The same vertex-minus-edge proof works for every fixed (t)-set (Q).  Its
containment indicator along the path has

\[
b_Q=\frac tr\binom{2r-1-t}{r-t}
  +\mathbf1_{Q\subseteq C_*}
\tag{11.5}
\]

blocks.  The induced (Q)-containing section is a rainbow path forest whose
only possible omitted lower colour is (C_*).  Thus a one-hole lower-rainbow
path simultaneously carries the entire Catalan/ballot triangle of section
forests, in every codimension.  For (k=11), the verified (t=3) profile is
(28^{155},29^{10}); the ten exceptional triples are exactly those inside
the five-set (C_*).  This all-order balance is substantially stronger than
the original two-coordinate observation and is a natural recursive invariant
for a future construction.

There is a particularly clean consequence hidden by the raw counts.  If
\(Q\not\subseteq C_*\), the section has

\[
V_Q=\binom{2r-1-t}{r-t},\qquad b_Q={t\over r}V_Q,
\]

and therefore its **mean component length is exactly**

\[
\boxed{{V_Q\over b_Q}={r\over t}.}
\tag{11.5a}
\]

The singleton, pair, and triple sections are not unrelated coincidences;
they are one scale-free law.  In particular the section scale becomes
\(\Theta(\sqrt r)\) precisely when \(t=\Theta(\sqrt r)\), the same scale as
the optimal delay \(d\).  This does not prove the recursion, but it identifies
where the finite Catalan decomposition meets the asymptotic square-root
slack.

The identity also has an oriented-edge form.  If \(b_i\) is the coordinate
added across the edge with lower colour \(C_i\), then

\[
\#\{i:b_i\in Q,\ Q\setminus\{b_i\}\subseteq C_i\}
=b_Q-\mathbf1_{Q\subseteq T_0}.
\tag{11.5b}
\]

Thus the arrival labels of an endpoint-rooted middle-levels path form an
all-order balanced choice function on the lower colours.  This is a stronger
construction invariant than coordinate-frequency balance and suggests
building the path as an oriented design before imposing its Hamilton order.

At (t=1), the same formula fixes the *number* of coordinate 1-runs.  Their
total number is (W+r-1), while their total length is (rW); the average run
therefore has length (r-o(1)).  For a nonexceptional pair, the average
both-present block has length exactly (r/2).  Since the factor delay is only
(d=\Theta(\sqrt r)), residence has ample average capacity.  What distinguishes
the factorable (k=11) near-path from the new q1-perfect overlay path is not
run count—it is forced to be the same—but equitable run *lengths*.  This
turns the finite residue into a sharply stated balancing problem: repair the
twelve upper colours without creating a short block in the Catalan/ballot
decomposition.

There is also an exact dual transform.  If (z_Q) counts blocks of central
vertices avoiding a fixed (t)-set (Q), and (mu^+(U)) is the immediate
upper-colour load, then

\[
z_Q=\binom{2r-1-t}{r}
 -\sum_{U\cap Q=\varnothing}\mu^+(U).
\tag{11.6}
\]

At the top value \(t=r-2\), put \(Q=[2r-1]\setminus U\).  There is then
only one rank-\((r+1)\) set disjoint from \(Q\), so (11.6) becomes the
pointwise identity

\[
\boxed{\mu^+(U)=r+1-z_{U^c}.}
\tag{11.7}
\]

Immediate upper coverage is therefore exactly the assertion that every
complementary \((r-2)\)-section has at most \(r\) zero-blocks.  This turns the
upper-colour condition from an external colouring requirement into an
intrinsic excursion bound on the same binary coordinate traces.

The whole upper vector has an even tighter normal form.  Complement each
upper colour and put

\[
w(A)=\mu^+([2r-1]\setminus A)-1,
\qquad A\in\binom{[2r-1]}{r-2}.
\]

Then

\[
\sum_Aw(A)=\operatorname{Cat}_r-1,
\]

and every zero-section count is an inclusion degree of this one signed
weight:

\[
z_Q=\binom{2r-1-t}{r}-\binom{2r-1-t}{r+1}
 -\sum_{A\supseteq Q}w(A).
\tag{11.8}
\]

Moreover the immediate upper CPCR is exactly

\[
\Phi^+=\sum_Aw(A)(w(A)-1).
\tag{11.9}
\]

If \(H\) is the number of holes and
\(P=\sum_A(w(A)-1)_+\), then
\(\Phi^+\ge2(H+P)\).  Consequently there is a genuine simple family
\(\mathcal D\subseteq\binom{[2r-1]}{r-2}\), of the forced size
\(\operatorname{Cat}_r-1\), with

\[
\|w-\mathbf1_{\mathcal D}\|_1\le\Phi^+.
\tag{11.10}
\]

Thus the CPCR values \(4,14,60\) in the finite paths say something much
stronger than “small variance”: their upper profiles are respectively only
\(4,14,60\) unit edits from simple Catalan-cardinality designs.  First-order
regularity is automatic—the upper vertex degrees differ only by endpoint
corrections of size at most two—so the nontrivial design problem begins at
higher inclusion degrees.

This design has an exact graph-theoretic realization.  Every Johnson edge is
uniquely the rank-two Boolean interval

\[
(C,U),\qquad |C|=r-1,quad |U|=r+1,quad C\subset U,
\]

whose two middle vertices are the two sets strictly between \(C\) and \(U\).
Equivalently, for each lower colour \(C\), choose one unordered pair
\(\{a,b\}\subseteq[2r-1]\setminus C\); this selects the edge

\[
C\cup\{a\}\;--\;C\cup\{b\}
\]

and gives upper colour \(U=C\cup\{a,b\}\).  Therefore an endpoint-rooted
central path is exactly a transition system satisfying:

1. one selected chord for every \(C\ne C_*\);
2. central degree two, except degree one at \(T_0,T_{\rm end}\);
3. connectivity; and
4. the prescribed multiplicities on the upper \(U\)'s.

Without clause 3, clauses 1--2 give a path/cycle factor.  When CPCR is zero,
clause 4 says precisely that the complements in
\(\mathcal D\) receive load two and every other upper colour load one.  This
is a concrete “design first, cycle-join second” decomposition of the central
construction; residence is the additional ordering constraint on the joined
factor.

Equivalently, in the closed version define one map

\[
\sigma:\binom{[2r-1]}{r-1}\longrightarrow\binom{[2r-1]}{r+1},
\qquad C\subset\sigma(C),
\tag{11.10}
\]

and select at \(C\) the two middle neighbours lying strictly between
\(C\) and \(\sigma(C)\).  Then the selected graph is a spanning 2-factor
exactly when every middle set receives degree two; its lower colours are
automatically perfect, and its upper-union multiset is exactly
\(\{\sigma(C)\}\).  Hence

\[
\boxed{\text{two-sided q1-rainbow cycle}}
\iff
\boxed{\sigma\text{ is surjective, degree-two, and connected}.}
\tag{11.10'}
\]

This is an exact compression of the immediate-shadow gate.  Hall proves
surjectivity if the degree equations are ignored, and an ordinary bipartite
2-factor proves the degree equations if the upper colours are ignored.  Their
conjunction is a coloured diamond-factor problem: one \(\sigma(C)\) variable
simultaneously uses one lower constraint, two middle-degree constraints, and
one upper colour.  Its matrix is not merely a bipartite network matrix.

For the prime-equivariant \(k=11\) instance this becomes 42 lower-orbit
variables, 15 choices per variable, 42 middle-degree equations, and 30 upper
coverage inequalities.  The relaxed integral system is already realized by
the complemented centered PBBS factor, with all upper loads in
\(\{1,2,3\}\); at least one quotient component has nonzero voltage.  Thus
the remaining q1 task is connectivity (or, in the stronger CPCR-zero form,
connectivity plus the profile \(1^{18}2^{12}\)).  Even a connected q1
certificate would not yet prove \(\nu(11)=465\): after a safe cut,
delay-three residence and rank-eight coverage remain.  See
`SURJECTIVE_SIGMA_Q1_REFORMULATION_AUDIT_20260727.md` and
`MATH_PRIME_EQUIVARIANT_SIGMA_FACTOR_AUDIT_20260727.md`.

Once (G_\sigma) is connected, the same map actually determines the whole
central shadow tower.  If its middle cycle is (Y_i), then

\[
L_i^{(q)}=\bigcap_{h=0}^qY_{i+h},\qquad
U_i^{(q)}=\bigcup_{h=0}^qY_{i+h},
\]

so in particular (U_i^{(2)}=\sigma(X_i)\cup\sigma(X_{i+1})).  Residence
is the local transition condition that no inserted coordinate is deleted in
the next (d) steps.  Under it, the maximal factor has exact derivative
identities: its lower rows are the consecutive intersections and its upper
rows the consecutive unions.  Hence “one map” is a valid normal form for
all central constraints, but surjectivity alone is not the theorem; the same
map must satisfy residence, every shadow-surjectivity condition, the boundary
flag, and the final lower pinning Hall test.  See
`SIGMA_FULL_CENTRAL_SHADOW_NORMAL_FORM_20260727.md`.

Connectivity also has a newly exact local marginal algebra.  Every
marginal-preserving trade inside one four-coordinate Boolean octahedron is a
circulation of \(K_4\).  Triangle circulations are alternating-six-cycle
alpha trades; four-cycle circulations are component-inert.  The alpha
component effect depends on the interlacement of its six exposed strands: it
can merge three components, and in the correct two-on-one configuration it
can also merge two.  Thus there is no component-parity obstruction; the open
condition is a spanning supply of residence-safe, correctly interlaced alpha
charts.  All three alpha edges flip the same spare coordinate, so in an
\(H\)-fresh factor the two cuts on one component are automatically more than
\(H\) apart—a useful built-in separation for the binary join.  See
`PRESCRIBED_DESIGN_CYCLE_JOINING_THEOREM_20260727.md`.

At (k=11), the unmodified complemented PBBS seed fails this supply test in
a statewise way.  It has 38 translation-orbits of pure alpha charts (418
labelled charts), but its alternating component is incident with no alpha
chart whatsoever, pure or mixed.  Therefore no static spanning alpha tree
exists.  The smallest successor gate is a marginal-preserving preparatory
trade that creates a portal to this component, or a larger absorber meeting
it directly.  See `K11_PBBS_ALPHA_CHART_SYMBOLIC_AUDIT_20260727.md`.

The algebra of every such fixed-core larger move is now closed.  On an
arbitrary outside coordinate set (Q), write (z_{i\mid jk}) for the
diamond rooted at (i) with upper triple ({i,j,k}).  The simultaneous
lower, middle, and upper kernel is generated over (mathbb Z) by the
ordinary four-coordinate alpha triangles.  Thus a (K_5/K_6) portal is not
a new lattice direction: it must be a **nonconformal alpha commutator** in
which unavailable intermediate alpha edges cancel.  See
`GENERAL_LOCAL_SIGMA_TRADE_ALPHA_GENERATION_20260727.md`.

The first canonical nonconformal circuit is a (5\leftrightarrow5)
pentagon, but the PBBS endpoint audit shows that neither side is executable
through the alternating route, before or after either boundary four-
transport.  In fact exactly two initial (K_4) transports touch that route;
both are inert, and one transport exposes neither an alpha nor a second
noninverse (K_4).  A one-common-core portal therefore needs at least five
negative rows.  The smallest remaining mechanisms are a changing-core
two-alpha commutator or a noncanonical (K_5) circuit.  See
`K11_PBBS_FIXED_CORE_PORTAL_COMMUTATOR_LOWER_BOUND_20260727.md` and
`K11_PBBS_K5_PENTAGON_PORTAL_AUDIT_20260727.md`.

The static half of this decomposition is now solved.  Choose both central
endpoints adjacent to the missing lower colour,

\[
T_0=C_*\cup\{a\},\qquad T_{\rm end}=C_*\cup\{b\},
\]

and put \(B=[2r-1]\setminus(C_*\cup\{a,b\})\).  The forced vertex degrees of
a simple excess design collapse to

\[
d_{\mathcal D}(x)=A-\mathbf1_{x\in B},\qquad
A={r-2\over2r-1}\operatorname{Cat}_r.
\tag{11.10a}
\]

A cyclic-orbit remainder construction realizes exactly these degrees and
\(|\mathcal D|=\operatorname{Cat}_r-1\) for every \(r\).  Selecting the
remaining full translation orbits by sampling without replacement gives,
simultaneously for every \(t=O(\sqrt r)\), relative inclusion-degree error
\(\exp(-\Omega(r))\), while keeping the vertex degrees exact.  Thus neither
Catalan divisibility nor static higher-order discrepancy is the obstruction.

Closing the endpoint-rooted path restores one chord whose complementary
block is \(B\).  Hence

\[
\widetilde{\mathcal D}=\mathcal D\cup\{B\},\qquad
|\widetilde{\mathcal D}|=\operatorname{Cat}_r,qquad
d_{\widetilde{\mathcal D}}(x)\equiv A.
\]

So the canonical closed target is especially elegant: a lower-rainbow
Hamilton cycle carrying a **regular simple Catalan excess design**.  Opening
one edge creates exactly the boundary defect required by the OR--Pascal
factor.

Realizability imposes one further exact second-order identity.  If
\(h_{ij}\) is the number of selected transitions exchanging coordinates
\(i,j\), and \(d_{\widetilde{\mathcal D}}(ij)\) is the pair degree in the
complement excess design, then

\[
\boxed{
h_{ij}=d_{\widetilde{\mathcal D}}(ij)
+\frac{(5-r)\operatorname{Cat}_r}{2(2r-1)}.}
\tag{11.10b}
\]

For \(r\ge6\), nonnegativity of \(h_{ij}\) is a genuine pair-degree lower
bound on any prescribed design.  The cyclic-orbit construction clears it by
its proved pair quasirandomness, but cardinality and point regularity alone
would not.

The unresolved theorem is precisely the inverse one: realize such a design
as the chord set of one connected, residence-controlled transition system.
See `STATIC_EXCESS_DESIGN_CYCLIC_ORBIT_THEOREM_20260727.md`.

Thus q1 upper-load balancing and zero-run balance are algebraically the same
data at different resolutions.  This is why an upper-colour repair can
damage deeper shadows through short zero excursions, and why CPCR plus the
weighted zero-run spectrum is the correct coupled objective.

At every greater depth the same duality survives.  If \(F_q(Q)\) counts
length-\((q+1)\) central windows whose union avoids \(Q\), and the maximal
zero-blocks of \(Q\) have lengths \(\ell\), then

\[
F_q(Q)=\sum_{\text{zero-blocks }B}(\ell(B)-q)_+.
\tag{11.11}
\]

Boolean inversion recovers every higher union-incidence degree from these
truncated local times.  The ideal residual-life ratio at section order \(t\)
is

\[
{\binom{r-q}{t}\over\binom rt}
=\exp(-qt/r+o(1)).
\tag{11.12}
\]

Combined with the exact mean \(r/t\), this says the correct recursive model
is not equal-length Catalan blocks but an approximately geometric,
low-discrepancy **hazard schedule** with departure rate \(t/r\).  One such
chronology would control many depths at once, precisely the correlation that
depth-by-depth random constructions fail to provide.  The complete theorem
and its all-depth moment identities are in
`BALLOT_UPPER_DUALITY_THEOREM_20260727.md`.

The local hazard compatibility can itself be realized exactly.  Its finite
law is hypergeometric,

\[
\alpha_{r,t}(q)={\binom{r-q}{t}\over\binom rt}.
\tag{11.13}
\]

For one section, integer block lengths can match every ideal truncated local
time simultaneously within additive \(r+1\).  More strongly, consider the
ordered-queue transition

\[
(x_1,\ldots,x_r)\longmapsto(x_2,\ldots,x_r,y),
\qquad y\notin\{x_1,\ldots,x_r\}.
\]

Euler tours in its higher-block graph give a deterministic high-multiplicity
system satisfying \(F_q(Q)=F_0(Q)\alpha_{r,t}(q)\) for every \(Q\) and every
prescribed \(q\).  A weaker finite-memory version, forbidding any coordinate
from being flipped twice in an \(H\)-window, is regular of degree

\[
(r-H)(r-1-H)
\]

and has perfectly uniform aggregate lower and upper shadows through depth
\(H\).  Therefore freshness and simultaneous hazard balance have no local or
fractional incompatibility.

The unresolved step is again integral projection: select one lift of each
middle set so that the selected lifts form the endpoint-rooted lower-rainbow
Hamilton path and retain aggregate CPCR.  A full queue transversal already
contains the hard linear-uniformity subset-Ucycle problem; the finite-memory
\(H=\Theta(\sqrt r)\) version is strictly weaker and is the correct
PBBS/middle-levels target.  This is not an ordinary TU rounding: the q1
diamond matrix already contains a determinant-two triangle minor.  Moreover,
the rotor theorem fixes one-point marginals, whereas CPCR is exactly a
two-point equal-target collision functional.  The minimal missing statement
is therefore a pair-balanced projected-circulation decomposition, followed
by label-preserving cycle joining.  See
`MATH_ROTOR_HAZARD_SCHEDULE_20260727.md` and
`MATH_FRESH_ROTOR_TRANSVERSAL_ROUNDING_GATE_20260727.md`.

There is now a concrete deterministic q1 specialization of that statement.
Take a 1-factorization \(M_1\dot\cup\cdots\dot\cup M_r\) of the
lower--middle inclusion graph and, for every colour pair \(p\), form the
2-factor \(F_p=M_i\cup M_j\).  For an upper interval \(A\), the colour pairs
on its diamonds form an \((r+1)\)-regular multigraph \(G_A\) on \(r\)
colours.  If \(\Delta_A\) is its collision excess above
\(K_r\) plus a spanning 2-factor, then exactly

\[
\frac1{\binom r2}\sum_p\Phi_1^+(F_p)
=\frac2{\binom r2}\sum_A\Delta_A.
\tag{11.14}
\]

Consequently average \(\Delta_A=o(r^2)\) gives one q1 factor with
CPCR \(o(W)\), while average \(O(r)\) gives \(O(W/r)\).  The new explicit
target is a locally almost-orthogonal 1-factorization; random edge marginals
alone cannot supply it.

The local and global parts of this target have now been separated exactly.
For every prime-power \(r\ge3\), an explicit projective finite-field chart
on one upper interval has

\[
G_A=K_r+\text{a spanning 2-factor},\qquad \Delta_A=0.
\]

Thus there is no pointwise design obstruction.  A global 1-factorization is
equivalent to a coherent atlas of these row-Latin skew charts, with one
overlap equation on every shared incidence edge.  That overlap equation is
the entire remaining q1 obstruction.  It now has an exact nonabelian normal
form: coordinate transitions must have transposition curvature, while the
induced (S_r)-valued row transport must have trivial holonomy.  Star
triangles are automatically flat, so only top triangles on (r+2) points
and commuting exchange squares on (r+3) points remain.  A flat coordinate
atlas is impossible because it would inject (2r-1) physical points into
(mathbb P^1(mathbb F_r)), and the natural affine curved prolongation also
fails.

After fixing one chart, the entire first top patch is encoded by (r+1)
permutations (pi_iin S(mathbb P^1(mathbb F_r))).  If
(u_i=pi_i(i)) and
(Gamma_i=R_ipi_i^{-1}R_{u_i}^{-1}), its irreducible equation is

\[
Gamma_iQ(pi_i(j),pi_i(x))
=Gamma_jQ(pi_j(i),pi_j(x))
\]

for all distinct (i,j,x).  A completed-row sign theorem now refutes this
projective chart family for every prime-power (r\ge7).  The punctured
conjugacy equations force either pairwise sign reversal on a triangle, or a
two-clique graph with more functional arcs than the patch possesses.  Thus
flat-coordinate, affine-curved, and projective exact-local prolongations are
all closed.  Any atlas successor needs a genuinely different completed-row
sign profile.  See `PROJECTIVE_ROOM_ATLAS_COCYCLE_GATE_20260727.md`.

In particular the standard
Kierstead--Trotter lexical factorization does *not* solve it: after aligning
its parameter \(s=r-1\), the factor pair \(M^0\cup M^1\) has exactly

\[
H_{01}=W\frac{(r-3)(r-4)}{2(r+1)(2r-3)}
=\left(\frac14+O(r^{-1})\right)W
\]

missing upper colours for \(r\ge5\).  The zero-defect examples at \(r=4\)
are the exceptional vanishing case of this formula, not evidence that the
lexical charts glue in general.  See
`LOCALLY_ORTHOGONAL_FACTORIZATION_PROJECTIVE_ATLAS_20260727.md`.

The (C_i+xy) vertices must likewise sometimes be linked consecutively to
expose their own intersection shadows.  This precisely identifies the
strengthened lift theorem to seek—a braid of four sector path covers with
the block count (11.2), rather than independent insertions.

There is now a second, exact q1 normal form.  Choose one map

\[
 \sigma:\binom{[2r-1]}{r-1}\to\binom{[2r-1]}{r+1},
 \qquad X\subset\sigma(X).
\]

Joining (X) to the two middle sets between (X) and (sigma(X)) gives a
middle-level 2-factor exactly when every rank-(r) vertex has degree two.
The factor is a doubly-rainbow q1 Hamilton cycle exactly when it is connected
and (sigma) is surjective.  For prime (k=11), translation reduces this to 42
variables with 15 choices, 42 degree equations, and 30 coverage constraints.
The relaxed system is already solved by complemented PBBS; the open q1
condition is one nonzero-voltage quotient cycle.

The same map determines every higher central shadow.  At (k=11), a
nonzero-voltage quotient cycle has exactly 126 delay-three residence tests
and 15 rank-eight q2 colour constraints.  Equivariance strengthens residence:
one short run has eleven disjoint translated copies, so no cut can hide it.
Once residence holds, every cut has exactly nine compatible
(5\supset4\supset3) endpoint flags.  A cut must still be simultaneously
nonessential for its q1 colour and its two adjacent q2 colours.  These exact
predicates are proved in
`K11_EQUIVARIANT_SIGMA_RESIDENCE_Q2_QUOTIENT_20260727.md`.

The q1 static marginals are also now completely benign.  An explicit union
of twelve cyclic orbits of four-sets has pair codegrees

\[
 (14,15,14,15,14),
\]

giving the optimally balanced exchange-quota vector
(8,9,8,9,8) for a cap-two upper excess design.  It clears every known
scalar and pair-capacity obstruction, though prescribed fractional and
integral realization remain open.  On the constructive PBBS side, a sharp
three-alpha fork gives a simple (7\leftrightarrow7) trade that opens both
ports of the formerly isolated alternating component with zero q1 damage.
This solves the local portal gate; phase-resolved joining, residence, and q2
compatibility remain global.

There is one sharp local exception.  In the pure chronological diamond
ladder, the final both-present vertex (A(C_*)) is incident with three forced
edges if one insists on the final both-present lower colour and both one-new
lower colours (C_*+x,C_*+y).  Path degree two therefore forces one boundary
hole.  A single reservoir edge removes the obstruction, or the hole may be
left to the boundary flag.  This explains—not merely observes—the persistent
one-hole lower profile of the odd exact examples.

## 12. Concrete new targets

### Target A: the optimal OR-Pascal tableau theorem

Prove that for every (k) there is a word of length (B(k)) with a
capacity-ordered lower triangle, (D^dA) a central-layer permutation, and
complete upper derivatives.  This is stronger than the exact-value conjecture
and matches every informative stored answer.  The literal one-rank-per-row
pattern (3.1) is required only when the finite row capacities permit it.

### Target B: one-flag central paths

Construct a central Hamilton path with run length at least (d+1), complete
upper sliding shadows, and lower intersection-shadow deficits contained in
one nested flag.  For (k=11,d=3), the desired flag has ranks 3,4,5 and can be
fed through the three boundary cells.  Boundary feeding is no longer an open
sublemma: (5.3) is its exact criterion, and (11.5) shows that the immediate
one-flag condition automatically supplies all Catalan/ballot section forests.
The unresolved content is the compatible upper chronology.

### Target C: a coloured section-forest connector

Starting from Lemma 9.1, join a spanning one-sided-perfect forest with
(O(W/m)) components into one path, changing only (O(W/m)) edges, while
retaining the perfect colours and filling the opposite colour defect.  This
would convert even-dimensional two-sided paths into odd-dimensional ones and
would also strengthen the PBBS compiler architecture.  At (k=11), the q1
version is now solved by the verified 827-edge overlay certificate; adding
delay-three residence is the remaining finite connector gate.

### Target D: a preservable-shrink labeling theorem

Given maximal envelopes (E_j), find many sites at which prescribed low masks
can replace (E_j) while designated witnesses in (DE,\ldots,D^{d-1}E)
survive.  The exact examples show that roughly half the entries may be shrunk
while over 94% of the penultimate row survives at (k=10,12).
Once the pins are selected, Theorem 3.1 of the boundary report makes
feasibility a coordinatewise interval-hitting test.  The target is therefore
a quantitative pin-selection/Hall theorem, not an integrality theorem.

### Target E: balanced Hamiltonian transversals

At depth one, a Johnson edge is uniquely an incidence pair

\[
(C,U),\qquad |C|=r-1,\ |U|=r+1,\ C\subset U.
\]

Equivalently, seek one (sigma) satisfying degree two, connectedness, upper
surjectivity, residence, and the adjacent-(sigma) q2 colour conditions.  At
(k=11), all predicates are now explicit on the 42-vertex quotient cycle.
The exact answers show that the fiber loads can sit within (O(k)) CPCR of the
integer floor.  This is a more informative objective than maximizing the
number of distinct colours alone.

## 13. Search consequences

The stored answers suggest the following search hierarchy.

1. Search the central transition word (a_i,b_i), not raw array entries.
2. Enforce the run floor (d+1) and central Hamiltonicity exactly.
3. Optimize the complete vector of shadow loads using CPCR plus hole counts;
   reward nested, rather than scattered, lower deficits.
4. Impose delay-(d) residence in stages by forbidding adjacent equalities in
   the depth-(q) intersection row for (q=1,\ldots,d); do not encode global
   lower rainbowness where local no-repeat is sufficient.
5. Track the Catalan/ballot sector profile (11.5) and preserve its rainbow
   all-present forests during any upper-colour repair.
6. For (k=11), use both complementary seeds: the current path is lower-perfect
   and the coordinate-12 section forest is upper-perfect.
7. Expose new edges first only for singleton/missing upper colours and the
   forced-degree vertices of Section 10; use lower-colour-preserving
   alternating circuits as the move primitive.
8. Run the exact pin-survival/factor-label test only after the central path is
   upper-complete.  The present (k=11) word proves that the lower compiler can
   already succeed at delay three.

## 14. Honest limitations

1. These solutions were selected by structured search, so their properties
   need not be forced in every optimum.
2. The first odd (d=3) case is now exact: (k=11).  This is one finite
   certificate, not yet a dimension-uniform construction.
3. The absence of simple coordinate symmetry or literal recursion means that
   a closed formula has not been uncovered.
4. The sparse-overlay and diamond-lift ideas isolate smaller gates but do not
   yet prove the general exact conjecture.  The separate quotient sigma lane
   does prove (\nu(11)=465).

Nevertheless, the data support a much sharper interpretation than “SAT found
some short words”: the known answers are coherent, multirank, two-sided
compiler tableaux.  Their recurrent object is the OR-Pascal geometry itself.
