# A fixed-uniformity adjacent skeleton and an exact phase obstruction

Date: 2026-09-07. This note gives an integral selection for the three
central ranks and isolates the additional all-depth condition. It does not
give a near-width full-cube rectangle cover or prove coefficient one.

Assume `b>=4`, and put

\[
 \Omega=[2b],\qquad W={2b\choose b},\qquad
 \mathcal L={\Omega\choose b-1}.
\]

Let `mathcal V` be the set of antipodal pairs `[S]={S,S^c}` of middle
`b`-sets. Thus `|mathcal V|=W/2`. Give every member of `mathcal V` two
labelled capacity slots.

## 1. The Kneser--Johnson edge bijection

If `L,L' in mathcal L` are disjoint, their complement in `Omega` is a
two-set `{x,y}`. Associate to the Kneser edge `LL'` the folded Johnson edge

\[
 e(L,L')=[L\cup\{x\}]\,[L\cup\{y\}].                \tag{1}
\]

This is well defined without ordering `x,y`. It is a bijection between the
edges of `KG(2b,b-1)` and the edges of the folded Johnson graph
`J(2b,b)/(S~S^c)`. Its two lower colours are exactly `L,L'`: the intersection
of the displayed representatives is `L`, while the complement of their
union is `L'`.

## 2. A genuine fixed-four-uniform selection

Define a four-uniform hypergraph `mathcal H_b`. Its vertex set is

\[
 \mathcal L\ \dot\cup\ (\mathcal V\times\{0,1\}).
\]

For every disjoint pair `L,L'`, and for each choice of one slot at each
endpoint `U,V` of (1), insert

\[
                  \{L,L',(U,i),(V,j)\}.             \tag{2}
\]

The degrees are

\[
 d(L)=4{b+1\choose2}=2b(b+1),\qquad
 d((U,i))=2b^2.                                      \tag{3}
\]

Indeed a lower set has `binom(b+1,2)` disjoint partners and four slot
choices. A middle `b`-set has `b^2` Johnson neighbours, and fixing its own
slot leaves two choices at the other endpoint.

The maximum pair codegree is at most `2b`. More precisely:

* two lower vertices have codegree four if disjoint and zero otherwise;
* two middle slots have codegree at most one;
* a lower set and a middle slot have codegree at most `2b`.

For the last item, if `L subset S` for one representative of the middle
pair, write `S=L+z`. A containing edge is determined by the other leftover
coordinate `y in S^c`, giving `b` choices, and by the other endpoint slot,
giving two. The case `L subset S^c` is symmetric; the two cases cannot both
occur.

Thus `mathcal H_b` is asymptotically regular, has fixed uniformity four,
degree tending to infinity, and maximum codegree `o(max degree)`. The
fixed-uniformity Pippenger near-matching theorem applies literally: there is
a matching leaving `o(W)` vertices of `mathcal H_b` uncovered. The precise
version used is the theorem quoted in the introduction of Alon--Kim--Spencer,
<https://math.nyu.edu/~spencer/papers/alonkimjs.pdf>: for fixed uniformity,
near-regular degrees and maximum codegree `o(D)` imply an almost-perfect
matching. Uniformity here is exactly four; no growing-uniformity extension
is inferred.

Replace every selected hyperedge by the side-two centered square pair based
on its folded Johnson edge. This proves the following.

**Adjacent-skeleton lemma.** There is an integral family of side-two square
pairs such that

1. all its rank-`b-1` targets are distinct and all but `o(W)` lower targets
   occur;
2. its rank-`b+1` targets are the complements of those lower targets, so
   all but `o(W)` occur there too;
3. its graph on folded middle targets has maximum degree two;
4. all but `o(W)` middle targets occur;
5. it has `(1+o(1))W/2` folded Johnson edges and principal charge
   `(2+o(1))W` before coalescence.

For item 4, a folded middle vertex absent from every selected edge leaves
both of its slots unmatched, and only `o(W)` slots are unmatched. No
independent target sampling and no growing-uniformity matching theorem is
used.

For `b>=4`, lower-colour simplicity also makes the selected folded graph
triangle-free. A folded triangle lifts to a Johnson triangle, and every
Johnson triangle either has a common `(b-1)`-intersection or a common
`(b+1)`-union. In the first case one lower intersection colour repeats; in
the second case its complementary lower colour repeats.

## 3. Why the skeleton does not yet coalesce to near width

The all-rank merge lemma for centered squares coalesces a path of side-two
squares only while its middle trace remains geodesic. Lower-colour
simplicity ensures every two-edge path is geodesic, but it does not control
three edges.

Here is an exact counterexample for every `b>=3`. Partition the unused
coordinates into disjoint sets `K,R`, each of size `b-3`, and six displayed
coordinates. Put

\[
\begin{aligned}
 A&=K\cup\{1,2,3\},&B&=K\cup\{2,3,4\},\\
 C&=K\cup\{3,4,5\},&D&=K\cup\{1,3,5\}.
\end{aligned}                                        \tag{4}
\]

Then `A-B-C-D` is a three-edge Johnson path. Its six lower colours are

\[
 K+23,\ R+56;\qquad K+34,\ R+16;\qquad K+35,\ R+26, \tag{5}
\]

all distinct. But `A` and `D` are adjacent, so `d_J(A,D)=1`, not three.
The path cannot be one side-four geodesic trace.

Consequently the adjacent-skeleton lemma solves the integral palette and
degree-two conditions only. Reaching principal charge `W+o(W)` requires a
selection in which all but `o(W)` selected edges can be grouped into
geodesic runs of diverging average length. Covering all but `o(2^(2b))`
targets by the known band/far-rank interface requires those runs to reach
length `omega(sqrt(b))`, not merely a fixed length. The four-uniform
matching does not supply this long-range no-reuse property.

## 4. Intact phase colouring cannot realize the fractional optimum

The two-orbit fractional optimum in
`EXACT_SATURATED_PAIR_FRACTIONAL_OPTIMUM_20260907.md` has load exactly one at
every target of ranks `b-1,b,b+1`. Scale all its rational column weights by
a common denominator `D`. The resulting integral multiset has exactly `D`
incidences at every one of these targets and total cost `D OPT_frac`.

Suppose one tries to realize the fractional weights by assigning every
intact column copy one of `D` phase colours, with every phase required to
cover the three tight ranks. At any tight target there are only `D`
incidences in total. Hence each phase contains exactly one of them. Every
phase is therefore an integral three-rank cover. The dual lower bound gives
cost at least `OPT_frac` in every phase; since the costs sum to
`D OPT_frac`, equality holds phase by phase.

The equality normal form then forces every phase to contain exactly

\[
                         {W\over2b}                  \tag{6}
\]

columns. In particular such a phase resolution is impossible unless
`b` divides `Cat_(b-1)`. It fails for every prime `b`.

This rules out rational-weight realization by merely colouring intact
column copies or intact macro lanes. It does not rule out a tube refinement
that genuinely splits columns and recombines their pieces. Such a refinement
must exploit geometry beyond an ordinary phase decomposition; independent
fine-rectangle selection is already excluded by
`INDEPENDENT_FRACTIONAL_TUBE_ROUNDING_20260907.md`.

## 5. Remaining positive target

The first missing strengthening is precise: construct the matching in
Section 2 with a long-range conflict rule ensuring geodesic runs of length
`omega(sqrt(b))`, while retaining `o(W)` uncovered lower and middle
vertices. Fixed-length conflict avoidance yields only fixed-length traces
and cannot be diagonalized to the required Gaussian scale without a
quantitative growing-range theorem.

Even that strengthening would not by itself prove full band coverage:
different long squares could still collide on targets at depth at least two.
One must additionally prove `o(W)` aggregate holes throughout a widening
band (or another global almost-cover condition). Thus the skeleton supplies
a legitimate integral local starting object, not a sufficient coefficient-one
gate.

The finite checker
`scripts/check_adjacent_skeleton_20260907.py` verifies the degree, codegree,
edge-colour and three-edge-obstruction calculations at `b=3,4`. The proof,
not the check, establishes the asymptotic lemma for `b>=4`.
