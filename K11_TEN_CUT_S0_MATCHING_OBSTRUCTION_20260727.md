# The explicit ten-cut set `S0` is lower-colour rigid

Date: 2026-07-27

## 1. Outcome

Consider the certified `k=11` staged-residence local minimum

`scratch/k11_q1_threeopt_local_min.txt`

and the proposed ten-cut set

\[
 S_0=\{17,88,171,181,201,284,303,397,416,422\}.
\]

The resulting twenty-end connector instance has a complete hand-checkable
obstruction:

\[
\boxed{\text{the only q=1 lower-rainbow perfect matching is the deleted
matching itself.}}
\]

Consequently `S0` cannot eliminate any of the ten length-two residence
defects.  This failure occurs before upper-colour surjectivity, connectivity,
or the seam-residence test is imposed.

The obstruction also gives a smaller first gate for every subsequent cut
choice.  One should first search for a nontrivial **rainbow alternating
circuit in the lower-label incidence graph**.  Only cut sets passing that
test need any upper-colour or residence analysis.

Everything through Section 4 below is an exact calculation from the stored
path.  Section 5 states the remaining finite problem and does not claim its
solution.

## 2. The twenty exposed ends

Masks are written in decimal and as subsets of bit positions
`{0,1,...,10}`.  Cutting the path edge at position `s` exposes `T_s` and
`T_{s+1}`.  The static path gives:

\[
\begin{array}{c|c|l|c|l}
s&T_s&\operatorname{supp}(T_s)&T_{s+1}&\operatorname{supp}(T_{s+1})\\ \hline
17&853&\{0,2,4,6,8,9\}&869&\{0,2,5,6,8,9\}\\
88&1366&\{1,2,4,6,8,10\}&1622&\{1,2,4,6,9,10\}\\
171&470&\{1,2,4,6,7,8\}&918&\{1,2,4,7,8,9\}\\
181&621&\{0,2,3,5,6,9\}&748&\{2,3,5,6,7,9\}\\
201&1229&\{0,2,3,6,7,10\}&221&\{0,2,3,4,6,7\}\\
284&189&\{0,2,3,4,5,7\}&573&\{0,2,3,4,5,9\}\\
303&1985&\{0,6,7,8,9,10\}&1733&\{0,2,6,7,9,10\}\\
397&1701&\{0,2,5,7,9,10\}&1953&\{0,5,7,8,9,10\}\\
416&1579&\{0,1,3,5,9,10\}&1675&\{0,1,3,7,9,10\}\\
422&797&\{0,2,3,4,8,9\}&783&\{0,1,2,3,8,9\}
\end{array}
\tag{2.1}
\]

Their ten deleted lower colours are

\[
R_{S_0}=\{837,1110,406,620,205,61,1729,1697,1547,781\},
\tag{2.2}
\]

in the same row order as (2.1).  The sole lower colour omitted by the old
path is

\[
C_*=59=\{0,1,3,4,5\}.
\tag{2.3}
\]

For reference, the ten deleted upper colours are

\[
\{885,1878,982,749,1245,701,1989,1957,1707,799\}.
\tag{2.4}
\]

## 3. The lower-label incidence certificate

Let

\[
\mathcal A=R_{S_0}\cup\{C_*\}.
\]

For every exposed end `x`, inspect the members of `A` contained in `x`.
The complete incidence table is

\[
\begin{array}{c|c@{\qquad}c|c}
\text{deleted seam}&\text{left end}&\text{right end}
 &\{L\in\mathcal A:L\subseteq x\}\\ \hline
17&853&869&\{837\}\text{ on both ends}\\
88&1366&1622&\{1110\}\text{ on both ends}\\
171&470&918&\{406\}\text{ on both ends}\\
181&621&748&\{620\}\text{ on both ends}\\
201&1229&221&\{205\}\text{ on both ends}\\
284&189&573&\{61\}\text{ on both ends}\\
303&1985&1733&\{1729\}\text{ on both ends}\\
397&1701&1953&\{1697\}\text{ on both ends}\\
416&1579&1675&\{1547\}\text{ on both ends}\\
422&797&783&\{781\}\text{ on both ends}
\end{array}
\tag{3.1}
\]

In particular:

1. every exposed end contains exactly one admissible lower colour;
2. it is the colour of its original deleted seam;
3. each deleted colour occurs on exactly its original two ends; and
4. no exposed end contains the hole `59`.

These four assertions can be checked directly from the support sets in
(2.1).  No search result is being used here.

### Proposition 3.1 (rigidity of `S0`)

Let `M` be a perfect matching of the twenty ends whose ten new seams preserve
q=1 lower rainbowness.  Then `M=M0`, where `M0` is the matching consisting of
the ten deleted path edges.

#### Proof

The old path has 461 distinct lower colours and omits only `C_*`.  After the
ten colours `R_{S0}` are removed, every new lower label must be a distinct
member of `A`; otherwise it duplicates an unremoved colour or another new
colour.  If `xy` is a new seam with lower label `L`, then

\[
 L=x\cap y,
\]

so `L` must be contained in both `x` and `y`.  Table (3.1) says that two
exposed ends contain a common member of `A` if and only if they are the two
ends of the corresponding deleted seam.  Thus every edge of `M` is an edge
of `M0`.  Since both are perfect matchings, `M=M0`.  QED.

Equivalently, after q=1 lower-colour filtering, the auxiliary seam graph is
the disjoint union of ten copies of `K2`.  The nominal 190 possible pairs
collapse to ten forced pairs.

## 4. Residence and upper shadows

Reinserting `M0` restores the original undirected Hamilton path (up to global
reversal).  Therefore all audited statistics are unchanged:

* the sole q=1 lower hole remains `59`;
* all 330 q=1 upper colours remain covered, with load profile
  `1^210 2^109 3^11`;
* the ten length-two internal one-runs remain, with witness intervals

  \[
  [17,19],[88,90],[171,173],[181,183],[201,203],
  [284,286],[303,305],[397,399],[416,418],[420,422];
  \]

* the length-three run count remains 77.

Thus `S0` has no constructive connected perfect matching other than the
inert one.  In particular it cannot reach the q=2 residence stage, so there
is no new q=2 or q=3 shadow multiset to audit.

There is also a cut-count obstruction to demanding delay three from **any**
ten-cut move on this local minimum.  Each of the 77 length-three runs has a
four-edge witness interval.  A fixed cut edge belongs to at most four such
intervals, so ten cuts hit at most forty of them.  By the uncut-defect lemma,

\[
\rho_3(P_M)\ge 77-4|S|=37
\tag{4.1}
\]

for every ten-cut reconnection `P_M`, independently of its seam matching.
Consequently a one-shot delay-three repair requires at least

\[
\left\lceil\frac{77}{4}\right\rceil=20
\tag{4.2}
\]

cuts.  The proposed ten-cut problem can only be a q=2 stage; after it, the
q=3 witness family must be recomputed and hit by a second exchange.  For
`S0` the sharper identity conclusion gives `rho_3=77`, not merely the lower
bound 37.

## 5. The smallest remaining finite gate

For a general choice `S` of one cut from each of the ten three-edge witness
intervals, let `X_S` be its twenty exposed ends, let `M0(S)` be its deleted
matching, and define the **lower-label incidence graph**

\[
G_{\rm low}(S)=\bigl\{xy:\ x,y\in X_S,\ x\ne y,\
 x\cap y\in R_S\cup\{C_*\}\bigr\},
\tag{5.1}
\]

with every edge coloured by `x cap y`.

Any non-inert q=1-preserving reconnection necessarily gives a nonempty
`M0(S)`-alternating circuit in `G_low(S)` whose new edges have distinct
colours.  Conversely, exchanging along any union of such circuits gives a
new lower-rainbow perfect matching; one must then impose contracted
connectivity, upper-colour surjectivity, and the depth-two seam test.

Therefore the next gate is not a 462-vertex Hamilton search and not even an
unfiltered 190-edge matching search.  It is:

> Find a cut choice `S` among the ten witness intervals for which
> `G_low(S)` contains a nontrivial rainbow `M0(S)`-alternating circuit that
> is connected after component contraction and passes the q=1 upper and
> depth-two seam constraints.

There are at most `3^10=59049` raw cut choices before spacing reductions.
The first, cheapest necessary test is purely the incidence test (5.1).
`S0` fails it maximally: every endpoint has mobility degree zero beyond its
old mate.

There is one further exact reduction common to all these raw choices.  The
four path vertices belonging to the ten witness intervals are respectively

\[
\begin{array}{c|l}
[17,19]&(853,869,365,461)\\
[88,90]&(1366,1622,1628,1372)\\
[171,173]&(470,918,903,423)\\
[181,183]&(621,748,492,366)\\
[201,203]&(1229,221,725,717)\\
[284,286]&(189,573,1565,1309)\\
[303,305]&(1985,1733,1613,1641)\\
[397,399]&(1701,1953,1960,1720)\\
[416,418]&(1579,1675,1677,1581)\\
[420,422]&(813,317,797,783).
\end{array}
\tag{5.2}
\]

A direct support check shows that none of these forty vertices contains
`C_*=59={0,1,3,4,5}`.  Hence the lower hole is unavailable for **every**
one-cut-per-witness choice, not only for `S0`.  Any successful connector in
this family must therefore reuse every member of `R_S` exactly once: its new
lower labels are a permutation of its ten deleted lower labels.  This turns
the first gate into a colour-exact alternating-circuit problem on the lower
side.

For completeness, the three possible deleted lower colours in the ten
witness intervals are

\[
\begin{array}{c|ccc}
\text{cut positions}&\text{left choice}&\text{middle choice}&\text{right choice}\\ \hline
17,18,19&837&357&333\\
88,89,90&1110&1620&1116\\
171,172,173&406&902&391\\
181,182,183&620&236&364\\
201,202,203&205&213&709\\
284,285,286&61&541&1053\\
303,304,305&1729&1605&1609\\
397,398,399&1697&1952&1704\\
416,417,418&1547&1673&1549\\
420,421,422&301&285&781.
\end{array}
\tag{5.3}
\]

Thus a cut vector chooses one colour from each row of (5.3), and a viable
new matching must realize that same ten-colour set exactly once on different
endpoint pairs.

If a q=2-safe circuit is found, q=3 must then be recomputed on the new path;
the present count `77` is not a valid list of staged q=3 defects until q=2
has vanished.

## 6. Epistemic status

Checked facts:

* all twenty masks and their support sets in (2.1);
* all ten removed lower and upper colours;
* the incidence certificate (3.1);
* Proposition 3.1 and the unchanged q=1/q=2/q=3 statistics for the forced
  matching;
* the one-shot lower bound of twenty cuts for delay three on the present
  path.

Open:

* whether another one-cut-per-witness choice has a nontrivial rainbow
  alternating circuit;
* whether such a circuit can also satisfy upper surjectivity and delay two;
* the subsequent delay-three and factor-recompilation gates.
