# The authenticated `k=17` SCD forest: resident-piece factorability and the exact all-interval upper gate

Date: 2026-08-01  
Lane: A, finite `k=17` multi-component SCD carrier  
Status: independently authenticated component/source ledger, exact minimum
residence-cut artifact, and independent all-interval upper replay.  The
result isolates a finite braid/compiler gate; it does not construct the final
word.

## 0. Verdict

The authenticated SCD support on `B_17` consists of

\[
 24310\text{ rank-nine owners},\qquad 19448\text{ edges},\qquad
 4862=\operatorname{Cat}_9\text{ directed paths}.             \tag{0.1}
\]

Keeping the original paths intact does **not** give a depth-three source:

* 3,649 components pass the maximal-source owner equations;
* 1,213 fail them;
* the same 1,213 components contain an internal positive owner-trace run of
  length below four;
* after adding the component terminal lower socket, only 3,292 components
  pass the full owner/internal-lower/terminal common-source test.

The exact minimum residence repair cuts 1,419 old path edges and produces

\[
                         P=4862+1419=6281                 \tag{0.2}
\]

locally depth-three-factorable pieces whose internal positive coordinate
runs have length at least four.  The raw
lower-q1 omission count is **`P=6281`**, not the number `P-1=6280` of seams
in a final one-path braid.  Against the scalar budget 7,401, this leaves

\[
                              7401-6281=1120.             \tag{0.3}
\]

The cuts have a substantial upper cost.  For every rank, the old hole bank
and the newly lost bank are disjoint, and their union is exactly the post-cut
hole bank:

\[
\begin{array}{c|r|r|r|r}
\text{rank}&\text{universe}&\text{pre-cut holes}&
 \text{new cut losses}&\text{post-cut holes}\\ \hline
10&19448&0&1419&1419\\
11&12376&911&1543&2454\\
12& 6188&608&1047&1655\\
13& 2380&135& 473& 608\\
14&  680&  8& 114& 122\\
15&  136&  0&  15&  15\\
16&   17&  0&   0&   0\\
17&    1&  0&   0&   0.
\end{array}                                                    \tag{0.4}
\]

Thus the exact exterior upper bank of the resident pieces has size

\[
 1419+2454+1655+608+122+15=6273.                         \tag{0.5}
\]

Ranks 10 through 14 alone contribute 6,258.  The 15 rank-fifteen casualties
are real and must not be dropped from an arbitrary-width audit.

The remaining question is therefore an exact ordered/oriented piece-braid
problem: can the `6280` crossing seams simultaneously regenerate the 6,273
upper masks, use all but one of the 6,281 missing lower colours, preserve
positive-run seam safety, and admit one maximal common source?  Scalar counting does
not rule this out, but no such braid/compiler is presently certified.

## 1. Frozen inputs and independent replay

The exact SCD selected-option file is

`scratch/h2_k17_m9_multicomponent_20260801/phase_m9.selected.tsv`, SHA-256

`49d3854140ed2ef3a1e2119013dc9b21e51176e4b69e5aa1a36a9a177d21d8de`.

The component/source audit is

`scratch/h2_k17_m9_multicomponent_20260801/component_factorability.audit.json`,
SHA-256

`1a86be73b6ab1d19a104a59ab93c3a93be8c1587eb00b038c95aa2ba1931ec36`.

Its payload SHA-256 is

`5d10ff28bedd106f07876c1fea7f2333c5eecebf5385de00e0f03a4d6e8f40d3`.

The canonical minimum residence-cut and piece artifact is

`scratch/h2_k17_m9_multicomponent_20260801/h2_residence_pieces.json`,
SHA-256

`9889b94b7d18078986965b5b78290b87b2ce8dde78bfe78b03ac3d9c5ad69f88`.

Its payload SHA-256 is

`e11258479411a60abb01c1434012b2d823725780bb8d25f24eaa32e247ea12c4`.

It contains all 1,419 cut records

\[
 (\text{component},\text{cut},\text{left owner},\text{right owner},
   \text{lower},\text{upper})                         \tag{1.1}
\]

and all 6,281 pieces with roots, owners, maximal source, positive-run boundary
summaries, and complete prefix/suffix owner-union arrays.

The independent all-interval replay is

`scratch/audit_threadA_k17_m9_resident_pieces_allinterval_upper_20260801.py`,
SHA-256

`39e212607b0f4ce3473448a7fb79e2197c7aa420b277d94bcac236ef11c54cac`.

Its output is

`scratch/threadA_k17_m9_resident_pieces_allinterval_upper_20260801.audit.json`,
SHA-256

`4c4d97c487255b4b7326f2e3206269deb03a9515b3d884ecd557f0270a971cb7`.

The output payload SHA-256 is

`c61fd553b5dcf00a895585fd84a988ce24b953b960f23581337d53e2282b3dc1`.

The replay consumes the frozen piece JSON directly, reconstructs every old
component by consecutive piece coordinates, checks every cut against its two
owners and colours, and recomputes every contiguous-interval OR.  It performs
no search.

## 2. Exact component factorability and residence

For an owner component

\[
                       O_0,O_1,\ldots,O_s
\]

at depth three, its owner-only maximal source is

\[
 K_p=\bigcap_{\max(0,p-3)\le i\le\min(s,p)}O_i,
                 \qquad 0\le p\le s+3.              \tag{2.1}
\]

It is source-factorable exactly when every `K_p` is nonempty and

\[
                         O_i=K_i\cup K_{i+1}\cup K_{i+2}\cup K_{i+3}
                                                                  \tag{2.2}
\]

for every owner row.  An internal positive coordinate run of length below
four makes (2.2) fail: none of the four source positions of a row containing
that coordinate lies wholly inside its positive run.  Conversely the exact
replay shows that this is the only owner-row failure in the frozen object.

### Theorem 2.1 (uncut component ledger)

Among the 4,862 components:

\[
\begin{array}{c|r}
\text{owner-source factorable}&3649\\
\text{owner-source failed}&1213\\
\text{components with an internal positive run below four}&1213\\
\text{positive bad runs}&1736.
\end{array}                                             \tag{2.3}
\]

No maximal-source position is empty.  The failures are reconstruction
failures, not empty-cap failures.

Adding all internal lower rows and the terminal sink socket gives the exact
common-source counts

\[
\begin{array}{c|r}
\text{feasible}&3292\\
\text{failed}&1570\\
\text{owner-factorable but terminal-failed}&357.
\end{array}                                             \tag{2.4}

For a factorable component with sink root `L` and sink owner
`M_0(L)=L\cup\{x\}`, the terminal socket is feasible exactly when `x` occurs
in the sink owner and each of its preceding at most three owners.  This is a
separate common-Q row; owner factorability alone does not imply it.

### Theorem 2.2 (minimum resident segmentation)

For each component, list every wholly internal positive coordinate run of
length below four.  A cut clips such a run exactly when placed in its closed
boundary interval.  These intervals lie on a line, so greedy stabbing by the
earliest right endpoint is minimum on each component.  Summed over all
components, the minimum is exactly 1,419 cuts.

The 6,281 resulting pieces each satisfy:

1. no wholly internal positive coordinate run has length below four;
2. every maximal-source position is nonempty; and
3. the depth-three replay (2.2) returns the owner piece exactly; and
4. the derived `D^2` and `D^3` rows have no internal positive run below
   three and four, respectively.

This does not assert a separate terminal sink socket for every piece.  Those
6,281 missing lower addresses are deliberately left to the generalized
compiler/braid.

## 3. Arbitrary-width means all interval lengths

For a list `B=(O_0,\ldots,O_s)`, define its rank-`r` upper deck by

\[
 \mathcal W_r(B)=
 \left\{
   \bigcup_{i=a}^bO_i:
   0\le a\le b\le s,
   \left|\bigcup_{i=a}^bO_i\right|=r
 \right\}.                                            \tag{3.1}
\]

For a family of blocks, take the union of (3.1).  The interval length is not
fixed by `r-9`: a long owner path may remain inside one rank-`r` target and
provide it.  Any census restricted to exactly `r-8` consecutive owners is
therefore only a shortest-window subdeck, not the arbitrary-width deck.

Let `F` be the original 4,862 components and `F'` the 6,281 resident pieces.
Put

\[
 \mathcal E_r=\binom{[17]}r\setminus\mathcal W_r(F),
 \qquad
 \mathcal L_r=\mathcal W_r(F)\setminus\mathcal W_r(F').          \tag{3.2}
\]

Because every piece is an interval of its old component,

\[
                         \mathcal W_r(F')\subseteq\mathcal W_r(F),
                                                                  \tag{3.3}
\]

and hence

\[
 \binom{[17]}r\setminus\mathcal W_r(F')
                    =\mathcal E_r\mathbin{\dot\cup}\mathcal L_r. \tag{3.4}
\]

The disjoint union (3.4) is the requested exact overlap accounting.  Its
cardinalities are (0.4).

At rank ten, every old edge has a unique upper colour, so every cut deletes
one distinct q1 witness and

\[
                    \mathcal L_{10}=\{O_{c-1}\cup O_c:c\text{ is a cut}\},
 \qquad |\mathcal L_{10}|=1419.                       \tag{3.5}
\]

The independent replay verifies (3.5) as a set equality, not only a count.

## 4. Exact lower and connector accounting

The full rank-eight layer has size 24,310.  Before cuts, the 19,448 internal
edges use 19,448 distinct lower colours, leaving one terminal colour per old
component:

\[
                              24310-19448=4862.         \tag{4.1}
\]

The cuts remove 1,419 further distinct lower colours.  Therefore

\[
             \boxed{\text{raw missing lower q1 colours}=4862+1419=6281=P.}
                                                               \tag{4.2}
\]

A one-path braid of `P` pieces has `P-1=6280` seams.  If every seam is a
Johnson edge and the lower colours are injective, it must use all but one of
the bank (4.2); the unused colour is the global terminal.

The same seams have an exact q1 upper split.  Of the 6,280 seam upper
occurrences:

* 1,419 must recreate the cut colours in (3.5); and
* the remaining 4,861 are repeats of already surviving upper colours.

Thus the repeat count remains

\[
                         6280-1419=4861=C-1.           \tag{4.3}

This is precisely the size entering the connector-cocycle theorem.  If the
global endpoint owners are adjacent with missing lower colour `K_0` and
union `R_0`, the repeat multiset `R`, augmented by `R_0`, must form a
size-`C` rank-ten multiset of constant coordinate degree

\[
                 2\operatorname{Cat}_8=2\cdot1430=2860.          \tag{4.4}
\]

Abstract existence of that palette is known.  The live issue is physical endpoint realization
jointly with (3.4), not the scalar palette.

## 5. Exact crossing-deck interface

The piece artifact already stores, for every oriented piece, the cumulative
prefix and suffix owner unions.  Let

\[
 A(B)=\bigcup_{O\in B}O,qquad
 P_j(B)=\bigcup_{i=0}^jO_i,qquad
 S_j(B)=\bigcup_{i=j}^{s}O_i.                         \tag{5.1}

### Lemma 5.1 (crossing interval normal form)

In an ordered/oriented concatenation `B_1,\ldots,B_P`, every interval which
crosses at least one seam has a unique form

\[
 S_a(B_i)\ \cup\ A(B_{i+1})\ \cup\cdots\cup\ A(B_{j-1})\
               \cup\ P_b(B_j),\qquad i<j.             \tag{5.2}

Conversely every nonempty choice in (5.2) is the OR of a crossing interval.

#### Proof

Intersect the interval with the first and last pieces it meets.  These
intersections are respectively a suffix and a prefix; every intervening
piece is taken whole.  The converse is immediate by concatenation. \(\square\)

### Lemma 5.2 (common-source lift loses no owner-interval upper witness)

Suppose one source word `Q_0,\ldots,Q_{s+3}` realizes a chosen owner braid at
depth three:

\[
                         O_i=Q_i\cup Q_{i+1}\cup Q_{i+2}\cup Q_{i+3}.
                                                               \tag{5.3}
\]

Then every owner-interval value lifts literally to one source interval:

\[
                 \bigcup_{i=a}^bO_i=\bigcup_{p=a}^{b+3}Q_p.     \tag{5.4}
\]

Thus common-Q feasibility cannot delete an upper witness already present in
the selected owner braid.  Its role is to decide whether that owner braid is
physically realizable together with the lower rows and caps.

#### Proof

Expand (5.3) for `a\le i\le b`.  The union of the overlapping four-position
intervals `[i,i+3]` is exactly `[a,b+3]`, which gives (5.4). \(\square\)

Therefore an exact braid checker needs no raw interval expansion.  For each
target `X` in the 6,273-mask bank, it suffices to ask whether some consecutive
piece range has all full intermediate unions contained in `X` and whether
one stored suffix plus one stored prefix completes the union to `X`.

This gives a proof-safe finite model:

1. choose one orientation and one position for each of 6,281 pieces;
2. enforce the positive-run boundary monoid at every seam;
3. enforce lower-colour injectivity, leaving one of the 6,281 colours;
4. enforce the 1,419 q1 restoration seams and the 4,861-member repeat
   cocycle palette;
5. for each upper mask in (0.5), select one occurrence of form (5.2); and
6. impose the generalized lower/common-Q reconstruction on the same order.

The all-interval upper rows are thus exact and finite.  No independence
between masks or ranks is assumed.

## 6. Sharp proved/unknown boundary

Proved:

* the uncut forest is not depth-three factorable componentwise;
* 1,419 is the exact minimum number of within-component residence cuts for
  the frozen orientation;
* all 6,281 resulting pieces are locally factorable and resident;
* raw lower omissions are exactly 6,281, leaving scalar slack 1,120;
* the all-interval pre-hole, cut-loss and post-hole banks are exactly (0.4),
  including 15 rank-fifteen losses; and
* every possible crossing witness has the compressed form (5.2).

Not proved:

* an order/orientation satisfying all positive-run seams;
* simultaneous regeneration of the 6,273 upper masks;
* physical realization of the connector cocycle palette;
* generalized lower common-Q feasibility; or
* a length-`B(17)` word.

Hence the authenticated SCD forest survives the scalar test but does not yet
compile.  Its smallest exact remaining gate is the joint piece-braid system
in Section 5.
