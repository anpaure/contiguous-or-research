# A fixed-factor phase--label incidence matrix is already non-TU

**Status (2026-08-21).** Every assertion below is proved.  Already at odd
block size `b=5`, with one fixed pair of complementary labelled
tight-cycle factors, the natural matrix which jointly chooses a relative
phase origin for each order pair and forbids repeated labelled upper targets
contains a `3 by 3` minor of determinant `-2`.  Thus even the fixed-`q`
physical phase--label matrix is not totally unimodular or a network matrix;
the simultaneous all-`q` matrix inherits the same minor.

More strongly, the complete twenty-column fixed-`q` packing LP for this bank
has optimum `10/3`, whereas its integral optimum is `2`.  The phenomenon
persists at every odd `b>=5`: at the extreme payload rank `r=2`, the exact LP
and integral optima are

\[
 {b(b-1)\over2(b-2)}\qquad\hbox{and}\qquad {b-1\over2},
\]

so the integrality-gap ratio is `b/(b-2)`.  Thus the natural physical
formulation has an actual gap, not merely a bad minor, for arbitrarily large
block sizes.

This is a finite formulation barrier, not an asymptotic no-go theorem.  It
does not prove a positive-density deficit for large `b`, that the
simultaneous all-`q` LP has the same gap, or that a dense central-rank order
bank cannot cover all but `o(W_b)` targets.  The ratio `b/(b-2)` tends to one
and the witness lies at the negligible extreme rank `r=2`.  It rules out
automatic integrality of the displayed natural formulation.  A separate
exchange witness also shows that the most direct tight-factor selection
independence system is not a matroid.

## 1. The fixed labelled factor bank

Let

\[
 A=\{a_0,a_1,a_2,a_3,a_4\},\qquad
 B=\{b_0,b_1,b_2,b_3,b_4\}.
\]

Use the following labelled cyclic orders on each side:

\[
 \alpha _0=\beta _0=(0,1,2,3,4),\qquad
 \alpha _1=\beta _1=(0,2,4,1,3).                 \tag{1.1}
\]

The cyclic two-window decks of `alpha_0,alpha_1` are

\[
 \{01,12,23,34,40\},\qquad
 \{02,24,41,13,30\},                              \tag{1.2}
\]

and hence partition all ten pairs.  The cyclic three-window deck of
`beta_i` consists of the complements of the pairs in the corresponding
two-window deck.  Thus `beta_0,beta_1` partition all ten triples.  Equations
(1.1)--(1.2) are therefore complementary-rank labelled tight-cycle factors
at ranks `2` and `3`.

For an order pair `e=(alpha_i,beta_j)` and a relative origin
`theta in Z_5`, form a cyclic word `w(e,theta)` of length `25` from the
periodic type schedule

\[
 \sigma=AABBB.                                      \tag{1.3}
\]

The `A` stream reads `alpha_i` cyclically starting at index zero; the `B`
stream reads `beta_j` cyclically starting at index `theta`.  Let

\[
 \mathcal U(e,\theta)
 =\left\{\{w_t,w_{t+1},\ldots,w_{t+5}\}:t\in\mathbb Z_{25}\right\} \tag{1.4}
\]

be its labelled length-six upper targets.  Every length-five window contains
two `A` letters and three `B` letters.  Moreover, all four order pairs
together cover every split-`(2,3)` middle target exactly once, independently
of `theta`.  A length-six window contains at most three `A` letters and at
most four `B` letters, fewer than the period five of either label stream, so
its six letters are distinct.

For completeness, write a starting position as `t=5m+s`, with
`m,s in Z_5`.  If

\[
 a_s=(0,1,2,2,2),\qquad b_s=(0,0,0,1,2),
\]

then the two cyclic deck indices of its length-five window are

\[
 u=2m+a_s,\qquad v=3m+b_s+\theta\pmod 5.           \tag{1.5}
\]

As `s` runs from zero to four, the invariant
`3u-2v=3a_s-2b_s-2theta` takes the five distinct residues
`-2theta+(0,3,1,4,2)`.  Hence (1.5) is a bijection onto
\(\mathbb Z_5\times\mathbb Z_5\), proving the claimed Cartesian middle
coverage.

## 2. The natural phase--label incidence matrix

Let `E` be the four fixed order pairs from Section 1 and let

\[
 \mathcal C=\{(e,\theta):e\in E,\ \theta\in\mathbb Z_5\}
\]

be the candidate origin choices.  Define the zero-one matrix `M` with
columns \(\mathcal C\) and rows consisting of the item rows `E` together with
all labelled six-set rows \(\binom{A\cup B}{6}\) by

\[
 M_{e,(e',\theta)}={\bf1}_{e=e'},\qquad
 M_{V,(e',\theta)}={\bf1}_{V\in\mathcal U(e',\theta)}.       \tag{2.1}
\]

The item rows enforce at most one origin for an order pair, while the target
rows enforce no repeated labelled upper target.  Requiring exactly one
origin changes item inequalities to equalities but does not change the
matrix whose total unimodularity is at issue.

Put `e_00=(alpha_0,beta_0)` and `e_01=(alpha_0,beta_1)`, and consider

\[
 c_1=(e_{00},3),\qquad c_2=(e_{00},0),\qquad
 c_3=(e_{01},1).                                    \tag{2.2}
\]

Define the two split-`(2,4)` upper targets

\[
 V_1=\{a_0,a_1,b_0,b_1,b_2,b_3\},\qquad
 V_2=\{a_0,a_1,b_0,b_1,b_2,b_4\}.                  \tag{2.3}
\]

Here are the three actual cyclic words, written from position zero:

\[
\begin{array}{c|l}
c_1& a0\ a1\ b3\ b4\ b0\ a2\ a3\ b1\ b2\ b3\ a4\ a0\ b4\ b0\ b1\ a1\ a2\ b2\ b3\ b4\ a3\ a4\ b0\ b1\ b2\\
c_2& a0\ a1\ b0\ b1\ b2\ a2\ a3\ b3\ b4\ b0\ a4\ a0\ b1\ b2\ b3\ a1\ a2\ b4\ b0\ b1\ a3\ a4\ b2\ b3\ b4\\
c_3& a0\ a1\ b2\ b4\ b1\ a2\ a3\ b3\ b0\ b2\ a4\ a0\ b4\ b1\ b3\ a1\ a2\ b0\ b2\ b4\ a3\ a4\ b1\ b3\ b0
\end{array}                                                    \tag{2.4}
\]

Sliding a length-six window and retaining those whose `A` part is
`{a_0,a_1}` and whose `B` part has size four gives

\[
\begin{array}{c|c}
c_1&0123,\ 0234,\ 1234\\
c_2&0124,\ 0134,\ 0234\\
c_3&0123,\ 0124,\ 0234.
\end{array}                                                    \tag{2.5}
\]

The entries in (2.5) are the `B`-index sets.  In particular,

\[
 V_1\in\mathcal U(c_1)\cap\mathcal U(c_3),\quad
 V_1\notin\mathcal U(c_2),
\]

\[
 V_2\in\mathcal U(c_2)\cap\mathcal U(c_3),\quad
 V_2\notin\mathcal U(c_1).                          \tag{2.6}
\]

The twenty words obtained from all four fixed order pairs and all five
origins each have `25` distinct length-six targets; in particular the three
columns in (2.2) are individually simple physical atoms at `q=1`.

### Theorem 2.1 (fixed-factor non-TU obstruction)

The fixed-factor matrix `M` is not totally unimodular.  The same is true of
any simultaneous multirank matrix which contains its `q=1` rows and columns.

#### Proof

On rows `e_00,V_1,V_2` and columns `c_1,c_2,c_3`, equations
(2.2) and (2.6) give

\[
 \begin{pmatrix}
  1&1&0\\
  1&0&1\\
  0&1&1
 \end{pmatrix},
 \qquad \det=-2.                                   \tag{2.7}
\]

Thus `M` is not totally unimodular.  Appending other offset rows, target
rows, item rows, or candidate columns leaves the displayed submatrix in
place, so the simultaneous matrix also fails total unimodularity.  Since
network matrices are totally unimodular, this natural formulation is not a
network matrix either.  \(\square\)

The determinant witness is strictly stronger in scope than a tokenwise
orbit witness: all three columns in (2.2) use the one fixed labelled factor
bank (1.1), and each column is an actual common-origin product word.  No
columnwise relabelling is allowed.

## 3. The complete fixed-`q` physical LP has a `5/3` gap

The half vector on the three displayed columns is feasible for the three
rows of the minor, but not for the full physical target-row system.  Indeed,
the three actual target sets have three targets in common, so those target
rows would receive load `3/2`.  A different symmetric fractional point does
give a genuine gap for the complete twenty-column system.

Write `e_ij=(alpha_i,beta_j)`.  For two different item classes, the number
of origin pairs whose upper-target sets are disjoint is

\[
\begin{array}{c|rrrr}
 &e_{00}&e_{01}&e_{10}&e_{11}\\ \hline
e_{00}&-&0&25&25\\
e_{01}&&-&25&25\\
e_{10}&&&-&0\\
e_{11}&&&&-
\end{array}.                                                   \tag{3.1}
\]

Here is a short count proving the table and the fractional claim below.
Every length-six window has split `(2,4)` or `(3,3)`.  Fix the `A` order
`alpha_i` and range over the five origins of one `B` order.

* Each candidate has fifteen split-`(2,4)` targets.  Across all five
  origins these are the twenty-five Cartesian targets formed from the five
  cyclic two-windows of `alpha_i` and the five four-subsets of `B`, each
  with multiplicity three.  This twenty-five-element target family is the
  same for `beta_0` and `beta_1`.
* Each candidate has ten split-`(3,3)` targets.  Across all five origins
  these are the twenty-five Cartesian targets formed from the five cyclic
  three-windows of `alpha_i` and the five cyclic three-windows of `beta_j`,
  each with multiplicity two.  The two `B` families are disjoint because
  `beta_0,beta_1` are a rank-three factor.

Thus, for fixed `i`, the target multiplicity vectors `(m_0,m_1)`, where
`m_j` counts origins of `e_ij` containing the target, are

\[
\begin{array}{c|ccc}
(m_0,m_1)&(2,0)&(3,3)&(0,2)\\ \hline
\hbox{number of targets}&25&25&25.
\end{array}                                                   \tag{3.2}
\]

The `A` two-window decks for `alpha_0,alpha_1` are disjoint, and so are
their complementary three-window decks.  Hence candidates with different
`A` orders have disjoint upper-target sets, proving every `25` in (3.1).
For the same `A` order but different `B` orders, each candidate contains
fifteen members of the common twenty-five-element split-`(2,4)` family.
Any two such fifteen-subsets intersect, proving the zeroes in (3.1).

### Theorem 3.1 (exact full-LP gap for the fixed bank)

For the complete matrix (2.1), the packing LP

\[
 \max\sum_{e,\theta}x_{e,\theta}
 \quad\hbox{subject to}\quad Mx\le\mathbf1,\quad x\ge0       \tag{3.3}
\]

has optimum `10/3`.  Its zero-one optimum is `2`.

#### Proof

Give every origin column of `e_(i,0)` weight `1/5` and every origin column
of `e_(i,1)` weight `2/15`, for both `i=0,1`.  The four item-row loads are
respectively `1,2/3,1,2/3`.  By (3.2), a split-`(2,4)` target has load

\[
 3\cdot{1\over5}+3\cdot{2\over15}=1,               \tag{3.4}
\]

while the two kinds of split-`(3,3)` target have loads `2/5` and `4/15`.
Targets belonging to different `A` orders are disjoint.  The point is
therefore feasible and has value

\[
 2\left(5\cdot{1\over5}+5\cdot{2\over15}\right)={10\over3}. \tag{3.5}
\]

For the matching upper bound, fix `i` and sum the twenty-five target-row
constraints for its common split-`(2,4)` family.  Every candidate with this
`A` order occurs in fifteen of those rows, so

\[
 15\sum_{j,\theta}x_{e_{ij},\theta}\le25.
\]

Summing over `i=0,1` gives value at most `10/3`, proving the fractional
optimum.

In an integral feasible set, (3.1) permits at most one candidate with
`A` order `alpha_0` and at most one with `A` order `alpha_1`.  Conversely,
any one candidate from each `A` order is target-disjoint, again by (3.1).
Thus the integral optimum is exactly two.  \(\square\)

The next section shows that the gap persists for arbitrarily large blocks,
but with vanishing relative size and only at an extreme payload rank.

## 4. An exact gap family for every odd block size

Let `b>=5` be odd and put

\[
 F={b-1\over2}.
\]

Fix Hamilton decompositions

\[
 \{\alpha_1,\ldots,\alpha_F\},\qquad
 \{\beta_1,\ldots,\beta_F\}                         \tag{4.1}
\]

of the complete graphs on the two labelled `b`-sets `A,B`.  Such
decompositions exist for every odd `b` by the elementary Walecki
construction.  The cyclic two-window decks of the `alpha_i` partition the
pairs of `A`; the cyclic `(b-2)`-window decks of the `beta_j`, being
complements of their two-window decks, partition the `(b-2)`-subsets of `B`.
Explicitly, when `b=2F+1`, on
\(\{\infty\}\cup\mathbb Z_{2F}\) one may take, for `0<=t<F`,

\[
 (\infty,t,t-1,t+1,t-2,t+2,\ldots,
   t-(F-1),t+(F-1),t-F),
\]

with finite entries modulo `2F`.  The endpoints at infinity cover all
finite vertices once, while the remaining edges alternate the two residue
sums `2t-1` and `2t`; this partitions all finite edges and verifies the
decomposition.

For every order pair `(alpha_i,beta_j)` and origin `theta in Z_b`, form the
length-`b^2` product word with schedule

\[
 A^2B^{b-2}.                                         \tag{4.2}
\]

Define the item--rank-`(b+1)` target incidence matrix exactly as in (2.1).
Every candidate is internally simple at the middle rank and at offset one.
All cyclic two-, three-, and `(b-2)`-window sets in one labelled `b`-cycle
are distinct when `b>=5`.
Indeed, if a starting position is `t=bm+s`, the middle-window deck indices
are

\[
 u=2m+a_s,\qquad v=-2m+b_s+\theta\pmod b,            \tag{4.3}
\]

where `a_s=min(s,2)` and `b_s=max(s-2,0)`.  Since `a_s+b_s=s`, the invariant
`u+v=s+theta` first determines `s`, and then `u` determines `m` because two
is invertible modulo odd `b`.  Thus (4.3) bijects the `b^2` starts with the
Cartesian product of the two middle decks.

For a length-`(b+1)` window, the `b-2` phases starting on a `B` position
have split `(2,b-1)`.  The map from a start to its `A` two-window and its
unique missing `B` label is injective, so every candidate has exactly

\[
 b(b-2)                                               \tag{4.4}
\]

distinct targets of this split.  Across all `b` origins of one fixed order
pair, these fill the common family

\[
 \mathcal P_i
 =\mathcal D_2(\alpha_i)\times {B\choose b-1},
 \qquad |\mathcal P_i|=b^2,                          \tag{4.5}
\]

each with multiplicity `b-2`.  Here \(\mathcal D_\ell(\gamma)\) denotes the
cyclic `ell`-window deck.  More explicitly, at a `B`-starting phase `s>=2`
the two-window index is `u=2m+2`, while the omitted `B`-label index is
`-2m+s-3+theta`; these two indices determine `m,s`.  Crucially,
\(\mathcal P_i\) is independent of the `B` order `beta_j`.

The remaining two phases have split `(3,b-2)`.  Across all origins their
targets fill

\[
 \mathcal Q_{ij}
 =\mathcal D_3(\alpha_i)\times\mathcal D_{b-2}(\beta_j),
 \qquad |\mathcal Q_{ij}|=b^2,                       \tag{4.6}
\]

each with multiplicity two.  At the two `A`-starting phases `s=0,1`, the
two deck indices are `u=2m+s` and `v=-2m+theta`; equality of both indices
forces equality of `m,s`.  This and the preceding omitted-label formula also
prove upper-band internal simplicity.

The families `mathcal Q_ij` are disjoint as `j` varies because the `B`
decks form a factor.  They are also disjoint as `i` varies.  To see the last
claim, if a three-set were a cyclic three-window in two edge-disjoint
Hamilton cycles, each cycle would use two of the three edges on that set;
the two two-edge paths would share an edge, a contradiction.  The families
`mathcal P_i` are disjoint as `i` varies for the simpler rank-two reason.

### Theorem 4.1 (arbitrarily large exact physical LP gap)

For every odd `b>=5`, the fixed-`q=1` packing LP of the bank (4.1)--(4.2)
has exact optimum

\[
 \operatorname{LP}(b)=F{b\over b-2}
 ={b(b-1)\over2(b-2)},                               \tag{4.7}
\]

whereas its zero-one optimum is

\[
 \operatorname{IP}(b)=F={b-1\over2}.                \tag{4.8}
\]

Hence its integrality-gap ratio is exactly

\[
 {\operatorname{LP}(b)\over\operatorname{IP}(b)}
 ={b\over b-2}=1+{2\over b-2}.                      \tag{4.9}
\]

#### Proof

Fix an `A` order `alpha_i` and sum the `b^2` target-row inequalities in
`mathcal P_i`.  Every one of its candidates occurs in `b(b-2)` of these
rows, so their total fractional mass is at most `b/(b-2)`.  The families
`mathcal P_i` are disjoint, and summing over the `F` values of `i` proves the
upper bound in (4.7).

Assign every one of the `F^2b` origin columns the common weight

\[
 w={1\over F(b-2)}.                                  \tag{4.10}
\]

Each item row has load `bw<=1`, since
`F(b-2)-b=(b^2-5b+2)/2>0` for `b>=5`.  By (4.5), every target in `mathcal P_i`
has load `F(b-2)w=1`; by (4.6), every target in `mathcal Q_ij` has load
`2w<=1`.  All other target rows have load zero.  Thus (4.10) is feasible
and has value `F^2bw=Fb/(b-2)`, proving (4.7).

For the integer optimum, two candidates with the same `A` order and
different `B` orders each contain `b(b-2)` targets from the common
`b^2`-element family `mathcal P_i`.  Since

\[
 2b(b-2)>b^2\qquad(b\ge5),                           \tag{4.11}
\]

they intersect.  Two origins of the same order pair are already forbidden
by its item row.  Thus at most one candidate may be chosen for each
`alpha_i`.  Conversely, candidates with different `A` orders have disjoint
targets by (4.5)--(4.6), so one arbitrary candidate for every `alpha_i` is
feasible.  This proves (4.8).  \(\square\)

The additive LP excess is `(b-1)/(b-2)=1+o(1)` candidate and the ratio in
(4.9) tends to one.  Moreover `r=2` carries only polynomial rather than
central-binomial mass.  The theorem therefore excludes eventual total
unimodularity of the natural matrices, but it supplies no linear-scale
obstruction to coefficient one.  A simultaneous all-offset fractional gap
is also not claimed: adding other offset rows may cut off (4.10), although
the fixed-`q` non-TU submatrix remains present.

## 5. The direct tight-factor independence system is not a matroid

There is a second elementary obstruction to a naive matroid-intersection
route.  On the ground set of cyclic orders of `[5]`, call a collection
independent when their cyclic two-window decks are pairwise disjoint.  Let

\[
 C=(0,1,2,3,4),\qquad C'=(0,2,4,1,3),\qquad
 D=(0,2,1,3,4).                                     \tag{5.1}
\]

The decks of `C,C'` are the two disjoint sets in (1.2), so
\(\mathcal B=\{C,C'\}\) is independent.  The deck of `D` is

\[
 \{02,12,13,34,40\}.                                \tag{5.2}
\]

It meets the deck of `C` in `12,34,40` and the deck of `C'` in `02,13`.
Thus \(\mathcal A=\{D\}\) is independent,
\(|\mathcal A|<|\mathcal B|\), but neither element of
\(\mathcal B\setminus\mathcal A\) can augment \(\mathcal A\).  The matroid
exchange axiom fails.

This does not prove that no clever extended or multi-matroid formulation
exists.  It proves only that the direct independence system "choose cyclic
orders with disjoint rank-two decks" cannot itself serve as one matroid in
an ordinary two-matroid-intersection proof.

## 6. Exact conclusion

The scalar profile theorem, the coherent Ferrers origin theorem, and the
fractional labelled containment theorem cannot be coinstantiated merely by
declaring the natural fixed-factor phase--label matrix totally unimodular,
turning it into an ordinary network flow, or treating direct factor
selection as a matroid.  The remaining positive route must use additional
dense structure: for example controlled switches among factor orders,
augmenting paths in a genuinely higher-order incidence system, or a bespoke
rounding theorem whose error is `o(W_b)`.
