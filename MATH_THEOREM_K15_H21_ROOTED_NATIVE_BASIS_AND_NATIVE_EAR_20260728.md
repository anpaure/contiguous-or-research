# The rooted native basis of the Hall-21 carrier and the exact native-ear gate

Date: 2026-07-28

Status: exact finite theorem for the frozen `k=15` Hall-21/six-zero carrier;
exact necessary-and-sufficient native-ear criterion inside the fixed-shore
all-native route; exact variable-shore rooted-compression theorem; exact
common-`Q` basis-pivot distinction; and a sharply scoped next
router/splitter target.  No independently audited Hall-20 carrier and no
global literal matching lift are claimed.

## 0. Verdict

Let `G_21` be the lower compiler graph reconstructed from

```text
scratch/k15_segment_braid_hall21_zero6.json.
```

Its canonical Dulmage--Mendelsohn shore has size

\[
 |X|/|Y|=846/825
\tag{0.1}
\]

and is the disjoint union of 21 connected gap-one components.  Each
component has a distinguished root `K`, and the native trace map on its
right cells is a bijection

\[
 \tau:Y_C\longrightarrow X_C\setminus\{K\}.
\tag{0.2}
\]

Thus the 825 right cells are not merely matchable: the one maximal erosion
controller realizes all 825 target/cell pins simultaneously, one for every
target of `X` except the 21 roots.  Reserving these pins leaves an exterior
matching of size 15,537, so they extend combinatorially to the full Hall-21
matching rank

\[
 825+15537=16362.
\tag{0.3}
\]

The ten small nonzero components are exact rooted stars.  Their roots all
have rank six.  Every leaf `K+e` has one depth-two native cell whose
restricted shore is `{K,K+e}`.  A new distinct depth-one cell of native
trace `K` saturates the whole star and is automatically common-`Q` safe.

This yields the exact native-ear gate.  Within a protected fixed-shore route
which retains the 825 native basis and the exterior matching, Hall 20 is
obtained if and only if one missing positive root receives a distinct native
ear and a gap-20 shore remains.  More generally, after a legal basis pivot,
the ear must fill the newly exposed target.  A pivot without a second cell
does not change rank.

The five large component roots have rank four, whereas every maximal-
controller letter has rank at least five.  They admit no native root ear.
Consequently a literal-safe all-native splitter preserving the six zeros
must target one of the ten rank-six nonloop stars; a large component can
serve only as a router/return reservoir unless exceptional common-`Q` pins
are introduced.

The exhaustive protected one-braid census is also final: Hall 21 is a
one-braid local minimum in the audited class.  The next route must therefore
use at least a neutral router plus a splitter, or leave that class.

A new two-braid chain is now a prospective second instance of the same
rooted-circuit mechanism:

\[
H21/z6
\xrightarrow{\operatorname{RF}(1510,5017,6136)}
H21/z6
\xrightarrow{\operatorname{RF}(885,1393,3668)}
H20/z6.
\tag{0.4}
\]

The two JSON files report the displayed scores, and the shared search report
assigns the portal shore size `702/681`.  Neither transition nor that DM
statement is independently audited in this note.  The exact theorem below
shows what would turn (0.4) into a second rooted compression certificate and
separates those missing facts from the already proved arithmetic.

## 1. Frozen inputs and scope of the one-braid minimum

The audited descent is

\[
 H22/z6
 \xrightarrow{\operatorname{FF}(1320,5339,6194)}H22/z6
 \xrightarrow{\operatorname{FR}(778,2292,6368)}H21/z6.
\tag{1.1}
\]

The final carrier and descent audit have SHA-256 values

```text
8a294110b530ba016b790f08f59c9d5bca3471af732867e27b0cb4a0b628b447
cc862804ea8910371283e8fdb42c1ac94ce9ed1cb5e0d3b5cdd94e8d74211e5c
```

respectively.  The final carrier is a permutation of all
`binom(15,8)=6435` middle masks, is Johnson-adjacent and depth-three
resident, has complete upper support at every depth `1,...,7`, and has
lower-hole vector

\[
 (4,18,9,1,0,0,0).
\tag{1.2}
\]

### Proposition 1.1 (protected one-braid local minimum)

For the frozen H21 carrier, the complete three-cut/reversal census has:

\[
\begin{array}{c|r}
\text{stage}&\text{descriptions}\ \hline
\text{Johnson-valid}&546890\cr
\text{depth-three resident}&12012\cr
\text{all-upper-support safe}&9185\cr
\text{also immediate-lower holes at most four}&7300.
\end{array}
\tag{1.3}
\]

Among the 7,300 fully scored descriptions, the Hall/zero distribution is

\[
\begin{array}{c|rrrrrrrrr}
(h,z)&(21,6)&(21,7)&(22,6)&(22,7)&(23,6)&(23,7)&(24,6)&(25,6)&(26,6)\cr
\#&7120&2&121&5&43&2&3&2&2.
\end{array}
\tag{1.4}
\]

In particular no protected one-braid endpoint has deficiency at most 20.
Of the 7,120 H21/six-zero descriptions, 6,433 are the identity encodings
`RR(a,a,a)` and 687 are nontrivial.

#### Proof

The counts and scores are the completed exhaustive output of the frozen
enumerator.  Their sum in (1.4) is 7,300.  Every line is independently
subject to the Johnson, residence, upper-support, immediate-lower, and full
Hall tests stated above.  The smallest displayed deficiency is 21.  For
`W=6435`, the permitted singleton reversals have
`1<=a<=W-2`, giving exactly 6,433 identity descriptions; subtraction gives
687.  \(\square\)

The proposition is a local minimum only in this protected one-braid class.
It says nothing against two-braid compounds, more general segment
permutations, or endpoints that spend additional immediate-lower support.
The census is complete and is not rerun here.

## 2. Native traces and rooted DM components

Let

\[
 P=(P_0,\ldots,P_{6437})
\tag{2.1}
\]

be the maximal depth-three erosion of the final middle chronology.  For a
physical lower cell `c=(q,s)`, `q in {0,1,2}`, define its native trace

\[
 \tau_P(c)=\bigcup_{p=s}^{s+q}P_p.
\tag{2.2}
\]

A pin `c -> tau_P(c)` is negative-inert and is realized by the one word
`A=P`.  Hence target- and cell-distinct native traces form an exact common-
`Q` matching, not merely an abstract compiler-graph matching.

Fix a maximum matching and its canonical alternating shore `(X,Y)`.  Let
`(X_C,Y_C)` be a connected component of its induced bipartite graph.  Its
root is

\[
 K_C=\bigcap_{S\in X_C}S.
\tag{2.3}
\]

### Theorem 2.1 (exact rooted native-basis decomposition)

The H21 shore has exactly the following component decomposition:

\[
\begin{aligned}
846/825={}&169/168+3(161/160)+160/159\cr
          &+2(5/4)+2(3/2)+6(2/1)+6(1/0).
\end{aligned}
\tag{2.4}
\]

The component roots are

\[
\begin{array}{c|l}
169/168&1920\cr
161/160&960,8217,24610\cr
160/159&8218\cr
5/4&4213,7504\cr
3/2&1103,18970\cr
2/1&2420,2575,2676,9524,17683,19568\cr
1/0&5801,13616,13620,17738,21641,29776.
\end{array}
\tag{2.5}
\]

Every component has left/right gap one and is a transversal-matroid
circuit.  Componentwise, the native trace map is a bijection

\[
 \tau_P:Y_C\overset{\sim}{\longrightarrow}
 X_C\setminus\{K_C\}.
\tag{2.6}
\]

Consequently the 825 traces are pairwise distinct and their missing target
set is exactly

\[
\begin{split}
\mathcal R=\{&960,1103,1920,2420,2575,2676,4213,5801,7504,8217,
8218,9524,\cr
&13616,13620,17683,17738,18970,19568,21641,24610,29776\}.
\end{split}
\tag{2.7}
\]

Their depth/rank census is

\[
\begin{array}{c|ccc}
q&0&1&2\cr
\#\text{ cells}&45&216&564\cr
|\tau_P(c)|&5&6&7.
\end{array}
\tag{2.8}
\]

No root in (2.7) is the native trace of any of the 19,311 current physical
lower cells.

#### Proof

Exact compiler reconstruction gives `(0.1)` and the 21 connected
components.  Their sizes sum to

\[
169+3\cdot161+160+2\cdot5+2\cdot3+6\cdot2+6=846
\]

on the left and

\[
168+3\cdot160+159+2\cdot4+2\cdot2+6=825
\]

on the right.  Direct intersection gives the roots (2.5).  In every
component the exact native trace of each right cell belongs to that
component; these traces are distinct and equal all component targets except
the root, proving (2.6)--(2.8).

For the circuit assertion, orient unmatched edges left-to-right and matched
edges right-to-left.  Each left vertex of a connected alternating DM
component is reached from its exposed root by an alternating path.  Toggling
that path produces a matching of all other left vertices and exposes the
chosen endpoint.  Thus every one-vertex deletion is matchable, which is the
transversal-circuit property.  Finally, enumerating (2.2) over all 19,311
cells finds none of the roots.  \(\square\)

The finite statements in the proof are recorded in two independent audit
artifacts.  No search choice enters them.

## 3. The ten positive star components

### Theorem 3.1 (exact star normal form)

Every nonzero component of size at most `5/4` has a rank-six root `K` and is
exactly

\[
 X_K=\{K\}\cup\{K+e:e\in E_K\},
 \qquad
 Y_K=\{c_e:e\in E_K\},
\tag{3.1}
\]

where

\[
 N_{X_K}(c_e)=\{K,K+e\},
 \qquad \tau_P(c_e)=K+e.
\tag{3.2}
\]

The axes and depth-two cell starts are

\[
\begin{array}{c|l|l}
K&E_K\text{ (one-based coordinates)}&s_e\cr \hline
2420&10&5788\cr
2575&6&3809\cr
2676&14&2895\cr
9524&7&2897\cr
17683&13&2886\cr
19568&14&3824\cr
1103&9,13&4439,6114\cr
18970&9,8&4331,4405\cr
4213&4,14,9,11&414,2735,4119,5417\cr
7504&4,14,6,2&516,3831,5350,5826.
\end{array}
\tag{3.3}
\]

The six `2/1` rows have the explicit target/cell data

\[
\begin{array}{c|c|c|c|c}
K&K+e&e&c_e&(q,s;\,\text{mandatory})\cr \hline
2420&2932&10&18663&(2,5788;2416)\cr
2575&2607&6&16684&(2,3809;519)\cr
2676&10868&14&15770&(2,2895;2672)\cr
9524&9588&7&15772&(2,2897;1332)\cr
17683&21779&13&15761&(2,2886;17683)\cr
19568&27760&14&16699&(2,3824;19536).
\end{array}
\tag{3.4}
\]

#### Proof

For the ten listed components, exact component reconstruction gives one
rank-six root and respectively `|E_K|=1,2,4` rank-seven nonroot targets.
Each nonroot differs from `K` in one coordinate.  The unique associated
right cell has depth two, native trace that nonroot target, and restricted
shore exactly the root and that leaf.  This proves (3.1)--(3.4).  \(\square\)

Thus the current component matching uses every leaf cell and exposes the
root.  No coordination among the leaves is missing; the sole missing
resource is a root cell.

## 4. Global extension of the rooted native basis

### Theorem 4.1 (native basis extends to the Hall-21 maximum)

Reserve all 825 native target/cell pairs from Theorem 2.1.  There is a
matching of size

\[
 15537=16383-846
\tag{4.1}
\]

on the targets outside `X`, using cells outside the reserved 825.  Hence
their union is a matching of size 16,362.  The 825 reserved pins are
simultaneously realized by the one physical word `P`.

#### Proof

Start with the canonical maximum matching defining the alternating shore.
Inside each DM component, toggle an alternating path so that its root is the
exposed left vertex, and then use the native trace bijection (2.6) on its
right side.  These toggles do not touch the matching outside the DM shore.
Every target outside `X` remains saturated on a cell outside `Y`.  There are
exactly `16383-846=15537` such targets.  Adding the 825 native component
edges gives (0.3).  Native-pin simultaneity follows from (2.2).  \(\square\)

This is stronger than 825 independent feasible edges and weaker than a
global literal compiler: no common-`Q` certificate is asserted for the
15,537 exterior matching pins.

## 5. Rank grading and the native root socket

For every fully interior position, `P_p` has rank `8-3=5`.  The depth-three
residence identities imply, for `0<=q<3`,

\[
 \left|\bigcup_{j=0}^{q}P_{p+j}\right|=5+q.
\tag{5.1}
\]

Indeed, the controller path is Johnson and the successive additions within
three positions are distinct; a repeated addition would give a carrier
coordinate run shorter than four.

### Lemma 5.1 (native root-edge criterion)

Let `K` have rank six and let `c=(1,u)` be a fully interior depth-one cell.
Then

\[
 \tau_P(c)=P_u\cup P_{u+1}=K
\tag{5.2}
\]

if and only if there are distinct `a,b in K` such that

\[
 P_u=K\setminus\{a\},
 \qquad P_{u+1}=K\setminus\{b\}.
\tag{5.3}
\]

In this event the native cell has restricted shore `{K}` inside the star
`X_K`.

#### Proof

The two controller states are distinct adjacent rank-five sets.  If their
union is the rank-six set `K`, each is a codimension-one subset of `K` and
their omitted coordinates differ, giving (5.3).  The converse is immediate.
Since the cell envelope is exactly `K`, it is adjacent to no proper
superset `K+e`; its native target `K` is feasible.  \(\square\)

### Corollary 5.2 (which H21 roots admit native sockets)

The five large-component roots have rank four and cannot be a native trace:
every clipped controller letter has rank at least five, so every nonempty
native interval union has rank at least five.  The ten positive star roots
have rank six and require depth-one sockets by (5.1).  The six loop roots
have rank six or seven and could use depth-one or depth-two sockets, but
servicing one would reduce the zero count.

Therefore a fixed-endpoint all-native H21-to-H20 route retaining six zeros
must target one of the ten stars in Theorem 3.1.

## 6. Necessary and sufficient native-ear theorem

Call a protected final state a **fixed-shore native one-ear extension at
`K`** when:

1. it has 825 target- and cell-distinct native pins with trace set
   `X\setminus\mathcal R`;
2. it has one further distinct native cell `c_K` with trace `K`, where `K`
   is a positive star root;
3. it has a 15,537-edge matching on the targets outside `X`, disjoint from
   these 826 cells; and
4. it retains a Hall shore of gap 20.

### Theorem 6.1 (fixed-shore native ear iff H20)

Every fixed-shore native one-ear extension at `K` has matching rank exactly

\[
 15537+826=16363
\tag{6.1}
\]

and Hall deficiency exactly 20.  Its 826 critical-shore pins are realized
simultaneously by the one final maximal controller.

Conversely, inside the class of protected fixed-shore edits which retain
the 825 native basis and the 15,537-edge exterior matching and gain exactly
one critical-shore cell by an all-native pin, an H20 descent saturating one
positive component is possible only if the extra native trace is that
component's exposed root.  Thus the root ear is necessary and sufficient in
this class.

#### Proof

For sufficiency, match every nonroot shore target to its retained native
cell, match `K` to `c_K`, and adjoin the disjoint exterior matching.  This
gives (6.1), so deficiency is at most 20.  The retained gap-20 shore gives
the reverse bound.  All 826 shore pins are native under one controller and
are therefore simultaneously literal.

For necessity, the retained 825 traces already match exactly
`X\setminus\mathcal R`.  In the selected positive component they match
every leaf and expose only its root.  A single additional all-native cell which
saturates this component must be assigned to that root; hence its native
trace is `K`.  \(\square\)

The gap-20 condition cannot be dropped: a local component gain can create a
different tight shore.  The exterior condition cannot be replaced by local
star saturation.  And this theorem does not cover exceptional common-`Q`
pins or component-compression routes which change the canonical shore.

### Theorem 6.2 (exposed-target form after a legal pivot)

Suppose a common-`Q`-legal neutral pivot replaces the component basis
`X_K\setminus{x}` by `X_K\setminus{x'}` while preserving its number of
cells, all other 20 component bases, and the exterior matching.  Then the
component rank is unchanged and `x'` is exposed.  A subsequent one-ear edit
perfects the component if and only if it supplies a distinct cell legally
pinned to `x'`; in the all-native subroute this means native trace `x'`.

#### Proof

Both bases have `|X_K|-1` cells and match that many component targets, so a
pivot only changes the exposed target.  Adding one cell saturates the
circuit exactly when it can match the exposed target.  The common-`Q`
qualification makes that graph edge a literal pin.  \(\square\)

This is the exact router/splitter normal form: the router may move the
deficit, but the splitter must add physical capacity at the moved deficit.

## 7. Exact basis pivots and the uniqueness obstruction

For each `2/1` component `{K,K+e}`, intersect the three physical letters on
the unique depth-two leaf cell with `K`.  Exact audit gives:

\[
\begin{array}{c|c|c|c}
K&K+e&s&\text{new three letters}\cr \hline
2420&2932&5788&(356,2372,2324)\cr
2575&2607&3809&(2569,2570,2572)\cr
2676&10868&2895&(2596,612,116)\cr
9524&9588&2897&(8244,9236,9488)\cr
17683&21779&2886&(1298,17666,16643)\cr
19568&27760&3824&(2160,3168,17504).
\end{array}
\tag{7.1}
\]

### Proposition 7.1 (common-`Q` root/leaf pivot, but no rank gain)

For every row of (7.1), the refined word remains nonzero, retains every
depth-three central middle window, and preserves all other 824 native pin
traces.  It changes only the displayed leaf-cell union from `K+e` to `K`.
The leaf `K+e` then becomes exposed.  Since the displayed leaf cell is the
unique native occurrence of `K+e`, the pivot alone cannot increase matching
rank.

#### Proof

The displayed three letters are the old controller letters intersected
with `K`.  Direct four-window union identities show that every central row
is unchanged; all entries remain nonempty.  Every selected native interval
other than the displayed cell retains its union, including the overlapping
`2676/9524` cells.  Hence the refined word is a simultaneous common-`Q`
certificate for the rebased 825-pin system.  But one target/cell edge has
merely replaced another and the component still has one right cell, so its
rank stays one.  Uniqueness of the old leaf occurrence forces that leaf to
be the new exposed target.  \(\square\)

Thus a successful splitter must create or import a second occurrence.  A
mere label switch, controller refinement, or root/leaf exchange is a router,
not a descent.

There are also 45 audited single-position common-`Q` root/atom pivots in the
five large components.  They remain exceptional relative to the maximal
controller, and Corollary 5.2 shows why they cannot become all-native
rank-four root sockets.

## 8. Exact seam equation for a native root ear

Consider a fully interior new seam with oriented middle collars

\[
 L_{-2},L_{-1},L_0\mid R_0,R_1,R_2.
\tag{8.1}
\]

Its three fully mixed controller states are

\[
\begin{aligned}
C_0&=L_{-2}\cap L_{-1}\cap L_0\cap R_0,\cr
C_1&=L_{-1}\cap L_0\cap R_0\cap R_1,\cr
C_2&=L_0\cap R_0\cap R_1\cap R_2.
\end{aligned}
\tag{8.2}
\]

### Theorem 8.1 (fully mixed native-ear equation)

For a rank-six star root `K`, the seam creates a fully mixed native root ear
if and only if

\[
 C_0\cup C_1=K
 \quad\text{or}\quad
 C_1\cup C_2=K,
\tag{8.3}
\]

where the contributing pair consists of distinct rank-five subsets of `K`.

#### Proof

The two new fully mixed depth-one physical cells have controller pairs
`(C_0,C_1)` and `(C_1,C_2)`.  Apply Lemma 5.1 to each.  \(\square\)

Equation (8.3) is the correct local constraint for a targeted router/splitter
proof.  It is not sufficient by itself: the complete braid must also retain
the leaf atlas, exterior matching, gap-20 shore, deck, Johnson seams,
residence, upper support, the declared lower support, and the common-
`Q` ledger over both collars.

## 9. Concrete next sockets

The existing star-arm cells have controller-axis pattern `111`: all three
controller letters contain their leaf coordinate `e`.  Hence shortening or
relabeling the existing native arm cannot create the root trace while also
retaining the leaf.  A genuinely second root/leaf occurrence is necessary.

### 9.1 Root 2676

For

\[
 K=2676=\{3,5,6,7,10,12\},
\]

the rank-five boundary states occur at

\[
\begin{array}{c|c|l}
\text{missing coordinate}&P&\text{controller positions}\cr \hline
3&2672&1540,2031,5523\cr
5&2660&1162,5290,5612\cr
6&2644&1166,4233,5281\cr
7&2612&987,3978,5279,5288\cr
10&2164&4363,5533\cr
12&628&279,466,686,2029.
\end{array}
\tag{9.1}
\]

The closest abstract root edges are

\[
(2029,2031):(628,2672),\quad
(5279,5281):(2612,2644),\quad
(5288,5290):(2612,2660).
\tag{9.2}
\]

Their intervening controller states are respectively `4720,2582,2597`, all
outside the Boolean boundary of `K`.  Thus the needed edge is present in the
controller-state set but not in the current chronology.

### 9.2 Root 19568 and the axis-14 return corridor

For

\[
 K=19568=\{5,6,7,11,12,15\},
\]

the closest root-edge pair is

\[
 (4271,4273):(19536,19504),
\tag{9.3}
\]

with intervening controller state `19600`.  Its current axis-14 arm begins
at `s=3824` with controller triple

\[
 (10352,11360,25696),
 \qquad\tau=27760=19568+\{14\}.
\tag{9.4}
\]

The root-7504 axis-14 arm begins at `s=3831` with

\[
 (12624,10576,9552),
 \qquad\tau=15696=7504+\{14\}.
\tag{9.5}
\]

At depth three, a seam can affect a depth-two signature beginning at `s`
only when its cut lies in `[s-5,s+5]`.  Therefore one seam can influence
both (9.4) and (9.5) only for

\[
 \boxed{3826\le a\le3829.}
\tag{9.6}
\]

This makes (9.6) the cleanest same-axis local return corridor.  It is only a
necessary influence condition, not a braid certificate.  The most direct
positive targets are therefore:

1. create a 2676 root ear using one pair from (9.2), with an axis-14 return;
2. create a 19568 root ear using (9.3), while using the 7504 arm in (9.6) as
   the neutral axis-14 return.

No legal segment braid satisfying all global conditions is asserted.

## 10. Variable-shore rooted compression

The fixed-shore number `846/825` is not intrinsic to the native-ear
argument.  What matters is a rooted basis of the deficient shore and a
disjoint matching of its complement.

Let `G=(T,C;E)` be a bipartite compiler graph with `|T|=N`.  A **rooted
native shore certificate of deficit `h`** consists of:

1. a shore `X subseteq T` with `Y=N_G(X)` and
   \[
   |X|-|Y|=h;
   \tag{10.1}
   \]
2. a root set `R subseteq X` of size `h` and a bijection
   \[
   \tau:Y\overset{\sim}{\longrightarrow}X\setminus R
   \tag{10.2}
   \]
   whose target/cell pins are all native under one controller; and
3. a matching `M_out` of `T\setminus X` into `C\setminus Y`, necessarily of
   size `N-|X|`.

No connectedness assumption is needed.  In the componentwise form relevant
here, `R` contains one exposed root from each unit-defect rooted circuit.

### Theorem 10.1 (variable-shore rooted one-ear theorem)

Assume a portal has a rooted native shore certificate of deficit `h`.
Suppose a protected final edit, under one final controller,

1. retains or rebaselines `|Y|` distinct native cells with trace set
   `X\setminus R`;
2. supplies one further distinct native cell with trace `K in R`; and
3. retains a matching of `T\setminus X` into cells disjoint from those
   `|Y|+1` cells.

Then the final compiler graph has a matching of size

\[
(N-|X|)+|Y|+1=N-h+1,
\tag{10.3}
\]

and hence Hall deficiency at most `h-1`.  If the final graph also has a
shore of gap `h-1`, then its deficiency is exactly `h-1`.

Conversely, in the pin-preserving one-ear all-native class, where the only
new critical-shore assignment is one further native pin, this assignment
raises the displayed matching rank by one if and only if its trace belongs
to `R`.  To perfect a specified rooted component, its trace must be that
component's exposed root.

#### Proof

The rooted native basis matches `X\setminus R` on `|Y|=|X|-h` cells.  The
exterior matching uses `N-|X|` disjoint cells, so together they have size

\[
|X|-h+N-|X|=N-h.
\]

The new cell matches `K`, which is the only additional target used, and is
disjoint from both retained cell sets.  This proves (10.3).  The
deficiency bound follows from Hall's theorem, and a gap-`h-1` shore gives
the reverse inequality.

For the converse, the retained assignments already use every target in
`X\setminus R` and every target outside `X`.  The only uncovered targets of
this displayed matching are the roots in `R`.  A single new native pin
increases its size precisely when its trace is one of those roots.  If a
particular component is to become perfect, that root is forced.  \(\square\)

The converse is intentionally restricted.  It does not rule out an
augmenting rearrangement using exceptional nonnative common-`Q` pins, a
different exterior matching, or several interacting new cells.

### Theorem 10.2 (exact all-shore current test)

For a portal graph `G_0` of deficiency `h` and a final graph `G_1` on the
same target set, put

\[
\delta_i(S)=|S|-|N_{G_i}(S)|,
\qquad
J(S)=|N_{G_1}(S)|-|N_{G_0}(S)|.
\tag{10.4}
\]

Then

\[
h(G_1)\le h-1
\quad\Longleftrightarrow\quad
J(S)\ge \delta_0(S)-(h-1)
\quad\hbox{for every }S\subseteq T.
\tag{10.5}
\]

In particular every `h`-tight portal shore must receive current at least
one.  If one final shore has gap `h-1`, then (10.5) is equivalent to
`h(G_1)=h-1`.

#### Proof

The identity

\[
\delta_1(S)=\delta_0(S)-J(S)
\tag{10.6}
\]

holds for every `S`.  Taking the maximum over `S` proves (10.5) and the
last assertion.  \(\square\)

Theorem 10.1 is a primal certificate for all the inequalities (10.5): its
explicit matching already prevents a hidden new shore of gap at least `h`.
The current test remains useful when a proposed splitter is described only
through changed cells and no retained exterior matching has yet been
exhibited.

### Corollary 10.3 (native/exterior conservation under shore compression)

For fixed `N` and `h`, a rooted native shore certificate with `|X|=x` has

\[
b_{\rm native}=x-h,
\qquad
b_{\rm out}=N-x,
\qquad
b_{\rm native}+b_{\rm out}=N-h.
\tag{10.7}
\]

Thus replacing a certified shore of size `x` by one of size `x-d` transfers
exactly `d` assignments from the automatically common-`Q` native basis to
the exterior matching.  It saves no assignment in the total matching
ledger.

#### Proof

These are respectively `|Y|`, `|M_out|`, and their sum in the proof of
Theorem 10.1.  \(\square\)

In particular the prospective change from `846/825` to `702/681` transfers
144 assignments:

\[
825-681=15681-15537=144.
\tag{10.8}
\]

The smaller shore may expose a simpler rooted circuit, but it is not by
itself a literal common-`Q` saving.  Its larger exterior matching must still
be lifted under the same final physical word.

### 10.4 The prospective `702/681` compression

The shared search report gives the following candidate chain:

\[
\begin{array}{ccl}
G_{21}&\xrightarrow{\operatorname{RF}(1510,5017,6136)}&G_{21}^{\rm port},
\cr
G_{21}^{\rm port}&\xrightarrow{\operatorname{RF}(885,1393,3668)}&G_{20}^{?}.
\end{array}
\tag{10.9}
\]

The candidate JSONs declare respectively `(hall,zero,lower_holes)=(21,6,4)`
and `(20,6,4)`, contain middle paths of length 6,435 with endpoints
`9901,7779`, and correctly chain their parent pathnames.  They contain no
embedded hashes, DM decomposition, matching, native-trace, residence,
shadow, or common-`Q` certificate.  Thus these are search reports, not the
independent audit of (10.7).

The additional shared report says that the portal's canonical tight shore
is `702/681` and is the unique minimum among the 687 nonidentity neutral
H21 descriptions.  The precise ordering meant by "minimum" and the
`702/681` reconstruction are likewise not encoded in the two JSON files.

If the portal admits a rooted native shore certificate, its arithmetic is
forced:

\[
h=702-681=21,
\qquad N-|X|=16383-702=15681,
\tag{10.10}
\]

and therefore

\[
681+15681=16362=N-21,
\qquad
682+15681=16363=N-20.
\tag{10.11}
\]

Consequently the new chain becomes a second rooted-circuit compression
instance if and only if the independent endpoint audit supplies all of the
following certificate data:

1. both RF reassemblies, Johnson chronology, residence, six zeros, all
   required upper supports, and the declared immediate-lower count;
2. exact matching ranks 16,362 and 16,363 and the portal shore `702/681`;
3. a 681-cell native bijection onto `X\setminus R`, with `|R|=21`;
4. preservation or common-controller rebaselining of that basis through the
   second braid;
5. one distinct final native ear whose trace is an exposed root;
6. a disjoint final exterior matching of size 15,681; and
7. either a final gap-20 shore or the equivalent all-shore current
   inequalities (10.5).

Items 3--6 are stronger than an abstract Hall-20 score.  Even if the score
in (10.9) is independently confirmed, a literal full compiler still needs
the exterior matching pins to pass the one common-`Q` chronology test; the
native 682-pin subsystem alone does not supply that lift.

The candidate artifacts have SHA-256 values

```text
1a6985b38d9ae85f957a98a2b05d154e6c21e878a72826fec98fe2490655f394
0740f2a73b6bf2b01a5f30713e69c636f60bf8cf8c47c8bbb798d69787fc43be
```

for the portal and final JSON respectively.  These hashes identify the
current files; they do not certify their mathematical claims.

## 11. Exact proved/conditional boundary

Proved:

1. the complete H21 component decomposition and native trace bijection;
2. simultaneous common-`Q` realization of all 825 shore pins;
3. extension of those pins to a graph matching of rank 16,362;
4. the exact rooted-star form of all ten small nonzero components;
5. the fixed-shore native-ear necessary-and-sufficient condition for H20;
6. the rank grading which excludes all five large roots from native-ear
   service;
7. six exact common-`Q` basis pivots and the unique-leaf obstruction;
8. the mixed seam equation (8.3); and
9. the protected one-braid local minimum and 687 nontrivial neutral
   descriptions; and
10. the variable-shore rooted one-ear theorem, exact all-shore current test,
    and native/exterior conservation law.

Not proved:

* a protected router realizing any equation (8.3);
* preservation or regeneration of the 825 native basis through such a
  router;
* the required 15,537-edge exterior matching at its endpoint;
* a gap-20 endpoint, an H20 carrier, or a global exterior common-`Q` lift;
* preservation of the deeper lower-support vector beyond what is explicitly
  audited; or
* any of the native-basis, exterior-matching, and common-controller
  certificates for the prospective `702/681` portal.

The exact next theorem is consequently either the pending independent audit
of (10.9), followed by its native/exterior certificate, or a physical
native-ear installation at another neutral portal.  The proved theorem asks
for one new root trace while retaining the rooted basis and exterior
matching; another Hall marginal statement is insufficient.

## 12. Audit artifacts

The exact component and socket statements are independently reconstructible
from

```text
scratch/audit_k15_segment_braid_hall22_to21.json
scratch/audit_k15_h21_dm_components.py
scratch/audit_k15_h21_dm_components.json
scratch/audit_k15_h21_component_ports.py
scratch/k15_h21_component_ports_audit_20260728.json
scratch/k15_h21_zero6_one_braid_scan_20260728.txt
scratch/k15_h21_zero6_neutral_emit_20260728.txt
```

with relevant SHA-256 values

```text
cc862804ea8910371283e8fdb42c1ac94ce9ed1cb5e0d3b5cdd94e8d74211e5c
eb33370c853bed9fa8df325c24a9ec5eac52024281cbd7fc2d6bc7a7939d18e7
8e190085dabbabc46e31ae7ee1a8ef44e40dd733a7c93a5a94f8f5c331d5c8df
9f695f6d4680e18fb9d86cb526930d55302ab5b24e1d06dc68196f7fd3823d19
d13f72b50835f03cb765acffa7d93957fd541b32bf08b85eca3bd4a0db0af8b7
```

respectively for the descent audit, component audit, port audit, one-braid
census, and neutral emit.  The exhaustive census ran only on H100 CPU; all
local work in this lane was proof audit, parsing, and small exact
reconstruction.

The prospective, not-yet-audited chain is stored in

```text
scratch/k15_h21_h20_root1801_chain/router/candidate_0000.json
scratch/k15_h21_h20_root1801_chain/final/candidate_0000.json
```

and is deliberately excluded from the preceding list of independent audit
artifacts.
