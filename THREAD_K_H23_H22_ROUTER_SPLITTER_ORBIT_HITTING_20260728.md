# Lane K: the Hall-23 remote router, Boolean splitter, and orbit-hitting gate

**Date:** 2026-07-28  
**Status:** exact `H23 -> H23 -> H22` theorem with literal one-word
common-`Q` currents on both the old Hall-23 shore and, cumulatively, the old
Hall-24 shore; protected router--splitter composition and the conditional
orbit-hitting implication proved.  The orbit-hitting lemma itself, and hence
neutral-router transitivity, is not claimed.

## 1. Exact result

Let `T_23` be `scratch/k15_segment_braid_hall23.json`.  Put

\[
\begin{aligned}
 T_*&=\operatorname{RF}(3799,4497,6039)T_{23},\\
 T_{22}&=\operatorname{FR}(740,4051,6137)T_*.
\end{aligned}                                                    \tag{1.1}
\]

Then

\[
 \delta_H(T_{23}),\delta_H(T_*),\delta_H(T_{22})=23,23,22.       \tag{1.2}
\]

Every state is an exact permutation of the `6435` rank-eight masks, is a
Johnson path, is depth-three resident, and has complete upper support at all
depths `q=1,...,7`.  Their lower-hole vectors are

\[
 (4,19,6,1,0,0,0),\quad(4,19,6,1,0,0,0),\quad
 (4,18,6,1,0,0,0).                                               \tag{1.3}
\]

Thus the immediate-lower hole count remains four.  The second braid gains
the depth-two lower target `4877`.  In fact the neutral router preserves the
support set at every lower and upper depth `q=1,...,7`; the splitter loses no
support at any such depth and gains only `4877` at lower depth two.  The seven
degree-zero targets remain

\[
2575,5801,13616,13620,17738,21641,29776.                         \tag{1.4}
\]

The canonical DM-shore cross-gap matrix, with rows indexed by the three
graphs and columns by their canonical shores, is

\[
 \begin{pmatrix}
 23&23&22\\
 23&23&22\\
 22&22&22
 \end{pmatrix}.                                                   \tag{1.5}
\]

The first move changes 18 physical cell-shore copies, has common rank
`16350`, and has contracted boundary rank `10 -> 10`.  The second changes
41 copies, has common rank `16343`, and has contracted boundary rank
`17 -> 18`.

The first move preserves the canonical DM target shore exactly: it remains
`1007/984` with the same target-set digest.  The final shore is nested,
has size `1005/983`, and is obtained by deleting exactly

\[
                              C=\{4877,4909\}.                    \tag{1.6}
\]

The final shore again decomposes into 22 connected `gap=1` components.

## 2. The exact remote-router current

The neutral move acts on the large `161/160` component rooted at `24610`,
not on the focal component (1.6).  Let

\[
\begin{aligned}
A&=\{24614,24615,24678,24679\},\\
B&=\{24610,24611,24674,24675\},\\
C_0&=\{28707,28770,28771\}.
\end{aligned}                                                     \tag{2.1}
\]

After cancelling all common projected columns, the neutral braid is the
associator

\[
             \boxed{\{A,B\mathbin\sqcup C_0\}
              \longmapsto\{C_0,A\mathbin\sqcup B\}.}             \tag{2.2}
\]

Concretely, the two old depth-two cells are

\[
\begin{array}{c|c|c}
16675&[3800,3802]&A\\
18914&[6039,6041]&B\sqcup C_0,
\end{array}
\]

and the two new cells are

\[
\begin{array}{c|c|c}
16675&[3800,3802]&C_0\\
18218&[5343,5345]&A\sqcup B.
\end{array}                                                       \tag{2.3}
\]

Every other DM component has exactly the same projected column multiset.
If `a,b,c` indicate that a test shore meets `A,B,C_0`, respectively, then
the exact neighbourhood current of (2.2) is

\[
 I_N=c+(a\vee b)-a-(b\vee c)=b(c-a).                             \tag{2.4}
\]

In particular `I_N=0` on the whole rooted component.  Proper subshores can
change, so the router is not an identity; it is a rank-neutral reassociation.

The focal cell lies at source start `739`, whereas the first router cut is
`3799`.  The entire focal prefix and its controller collar are therefore
unchanged.  The router only changes remote return blocks, after which the
splitter with left cut `740` becomes legal.  This is an exact example of a
remote catalyst rather than a local perturbation of the discharged cell.

### 2.1 Exact RF port-routing lemma

Let $T=(T_0,\ldots,T_{W-1})$ be a Johnson path and put

\[
 T'=\operatorname{RF}(r,s,t)T
 =T_{[0,r)}\,\overleftarrow{T_{[s,t]}}\,
  T_{[r,s)}\,T_{(t,W)}.                                        \tag{2.5}
\]

Then $T'$ is a Johnson path if and only if its three new seams satisfy

\[
 T_{r-1}\sim T_t,\qquad T_s\sim T_r,\qquad
 T_{s-1}\sim T_{t+1}.                                         \tag{2.6}
\]

Moreover, if $s\le x<x+1\le t$, the old adjacent pair
$(T_x,T_{x+1})$ occurs in reverse order at new positions $(u-1,u)$
exactly when

\[
                         r+t-x=u.                               \tag{2.7}
\]

This follows directly from the index map $x\mapsto r+t-x$ on the reversed
block.  Thus (2.6)--(2.7), followed by the finite residence and ledger tests
at the changed collars, are an exact statewise port-routing criterion.

For the present router,

\[
 (r,s,t,x,u)=(3799,4497,6039,5787,4051),                       \tag{2.8}
\]

and $3799+6039-5787=4051$.  It installs

\[
 T'_{4050}=T_{5788}=13197,\qquad T'_{4051}=T_{5787}=5007.       \tag{2.9}
\]

The router seams themselves are

\[
24811\sim28779,\qquad8431\sim24687,\qquad12399\sim12523.      \tag{2.10}
\]

Without the router, applying the stored splitter directly to $T_{23}$
would expose

\[
(5037,29144),\qquad(14733,21464),                               \tag{2.11}
\]

both at Hamming distance eight, and would create the residence defects

\[
(2,737,739),(2,2826,2826),(6,740,742),(6,2827,2828),(7,739,741).
                                                                    \tag{2.12}
\]

After routing, the splitter seams are

\[
(5037,5007),\qquad(14733,13197),\qquad(6573,22925),             \tag{2.13}
\]

all at Hamming distance two, and residence passes.  Hence the neutral first
move is a literal legality router, not merely a Hall-neutral detour.

## 3. The Boolean one-cell splitter

At the portal state the component (1.6) has one projected physical column

\[
                              \{4877,4909\}.                       \tag{3.1}
\]

The improving braid replaces it by the two singleton columns

\[
                              \{4877\},\qquad\{4909\}.            \tag{3.2}
\]

For hit indicators `x,y`, the exact splitter current is

\[
 I_S=x+y-(x\vee y)=xy.                                           \tag{3.3}
\]

Thus only a shore meeting both vertices gains capacity, and the full
`2/1` component gains exactly one.

More strongly, the final maximal erosion controller realizes (3.2)
natively:

\[
\begin{array}{c|c|c|c|c}
\text{target}&\text{cell}&\text{depth}&\text{start}&
 \text{controller letters}\\ \hline
4877&7178&1&740&(781,4365)\\
4909&13614&2&739&(809,781,4365).
\end{array}                                                       \tag{3.4}
\]

The respective mandatory masks are `4612` and `4652`.  Hence the complete
cell shores restricted to the component are the two singletons in (3.2).

The same maximal controller has 983 distinct native traces on the final DM
right shore.  Those cells and targets are disjoint from (3.4).  Consequently
one unmodified, nonzero physical word realizes

\[
                             983+2=985                            \tag{3.5}
\]

distinct pins on the old `1007`-target Hall-23 shore, while reconstructing
every middle row.  Its exact common-`Q` gap on that shore is therefore

\[
                             1007-985=22.                         \tag{3.6}
\]

The unresolved targets are

\[
\begin{gathered}
449,960,1103,1920,2420,2575,2676,4213,5801,7504,8217,8218,9524,\\
13616,13620,17683,17738,18970,19568,21641,24610,29776.
\end{gathered}                                                     \tag{3.7}
\]

This is an endpoint common-word theorem.  It reselects the final native
current; it does not assert dynamic transport of an arbitrary pre-existing
global pin assignment.

### 3.1 Nested two-target circuit-splitter lemma

Let $x\subset y=x\cup\{b\}$ be the two targets of a `2/1` component.  A
compiler cell $c$ has envelope $E(c)$ and mandatory mask $M(c)$.  If
initially

\[
                         E(c)=y,\qquad M(c)\subseteq x,          \tag{3.8}
\]

and every controller letter on the cell interval meets $x$, then the
restricted cell shore is $\{x,y\}$.  Suppose an exchange replaces
it by cells $c_x,c_y$ satisfying

\[
\begin{aligned}
 E(c_x)&=x,& M(c_x)&\subseteq x,\\
 E(c_y)&=y,& M(c_y)&\subseteq y,& b&\in M(c_y).
\end{aligned}                                                   \tag{3.9}
\]

Then their restricted shores are exactly $\{x\}$ and $\{y\}$.  Indeed,
$y\nsubseteq E(c_x)$, while $b\in M(c_y)\setminus x$.  If their native
traces equal $x,y$ and a protected exterior current uses disjoint cells,
the same exchange discharges the component both in Hall rank and literally
in one common word.

Here $x=4877$ and $y=4909=x\cup\{32\}$.  Before the split, the depth-two
cell at start `739` has controller letters `(809,301,4393)`, envelope `4909`,
and mandatory mask `4876`; all three letters meet `4877`, so (3.8) and its
letter condition hold.  The two final cells in (3.4) have
envelopes `4877,4909`; their mandatory masks are `4612,4652`, and
`4652` contains bit `32`.  Thus (3.9) proves the singleton refinement without
appealing merely to a matching computation.

### 3.2 Cumulative preservation of the preceding Hall-24 discharge

The endpoint theorem above can be strengthened across both successful
macros, including the intermediate neutral state.  Let $C_{20516}$ be the
`161/160` Hall-24 component discharged in
the preceding `H24 -> H24 -> H23` step.  In the Hall-22 carrier its target
neighbourhood still has `162` cells and induced matching rank `161`.  Its
native traces are every target of $C_{20516}\setminus\{20516\}$, a second
copy of `20517`, and the one outside trace `21543`.  The duplicate singleton
cells are now at starts `3301` and `6261`.

Already at the neutral portal, the component has the same 162-cell
neighbourhood pattern, with duplicate `20517` cells at starts `3579,6261`;
it is disjoint from the 984 active native cells.  Replacing the portal letter
at `6261` by `20516` therefore gives one word with `1145` distinct pins on
the old Hall-24 shore, of exact gap `23`.  Thus the RF router itself is
protected for the full cumulative current, not merely for the 984 active
targets.

More exactly, the native Hall-24 current has `1144` target values; the first
macro extends that exact target set by `20516`, the neutral router preserves
all `1145` values, and the second macro extends it by `4877`.  These are
target-set equalities, not only equal cardinalities.

They are not address equalities.  Among the 983 target identities which stay
in the active native current from Hall 23 to Hall 22, only 186 retain their
physical cell and 797 are re-addressed.  Including `4909` in the discharged
pair gives 187 unchanged addresses among the 984 old endpoint identities.
Thus the theorem permits simultaneous reselection; it does not transport
arbitrary old intervals or side constraints attached to pin addresses.

The entire 162-cell neighbourhood is disjoint from the 983 active Hall-22
native cells and the two splitter cells in (3.4).  Keep `20517` at start
`3301`, assign start `6261` to `20516`, and make the one-letter change

\[
                        P_{6261}:20517\longmapsto20516.          \tag{3.10}
\]

Only one other selected interval meets that position; its union remains
`22565`.  All central four-windows remain exact.  Consequently one nonzero
word simultaneously realizes

\[
                  161+2+983=1146                               \tag{3.11}
\]

distinct pins on the old 1168-target Hall-24 shore.  The exact cumulative
gap is $1168-1146=22$, with unresolved set (3.7).  This proves that the
remote router/splitter preserves the particular previously discharged
component, not only that it rebuilds the active native basis.  It still does
not prove preservation of an arbitrary global pin family outside this
audited shore.

Exactness has an independent upper bound.  The final canonical shore
$U_{22}\subset U_{24}$ has `1005` targets and only `983` neighbouring cells.
Therefore any injection on the old 1168-target shore has size at most

\[
                      983+(1168-1005)=1146,                     \tag{3.12}
\]

which the constructed common word attains.

## 4. Abstract signed braids versus the legal groupoid

Ignore all Johnson, residence, shadow, and Hall tests.  A forward three-cut
braid can swap two adjacent singleton interior blocks.  These swaps generate

\[
                         \mathfrak S_{W-2}                        \tag{4.1}
\]

on the interior positions; the two outer endpoint states are fixed by every
allowed cut.  If a fixed coarse partition is regarded as a list of opaque
oriented blocks, the allowed degenerate `RR(a,a,v)` interval reversal and
adjacent block swaps generate the
hyperoctahedral group

\[
                         C_2^b\rtimes\mathfrak S_b.               \tag{4.2}
\]

Thus there is no abstract parity, root, or component invariant.  Apart from
the deck and the two outer endpoints, the abstract block algebra is fully
transitive.

The physical situation is a **groupoid**, not a group action.  Its objects
are admissible carriers; a formal generator is a morphism only when its new
endpoint seams are Johnson edges and its seam collars pass residence and
shadow tests.  `FF` is inverted by `FF` with the new middle cut, `RF` and
`FR` invert one another, and `RR` is self-inverse.  Hence the legal move
graph is undirected, but the available generators depend on the object.

Call a morphism **shore-neutral** at level `h` if it preserves admissibility,
Hall deficiency `h`, the canonical DM target shore, and the existence of a
native common-word current saturating its DM right shore.  For a specified
target family $B$, call it **$B$-protected neutral** if its endpoint has
one common-word injection of every target in $B$, allowing physical pin
addresses to be reselected.  The first move in (1.1) is shore-neutral and
preserves the 984-target native basis.  Across the complete macro, Section
3.2 proves protection of the larger 1145-target current inherited from
Hall 23; the neutral endpoint itself already realizes all 1145 targets.
A weak Hall-neutral move need not satisfy either condition.

Relative to the old chronology, cut at

\[
0<740<3799<4497<5788<6040<6138<6435
\]

and call the consecutive blocks `X_0,...,X_6`.  The composite in (1.1) is
the signed seven-block word

\[
 \boxed{X_0,\overleftarrow{X_3},X_2,X_5,X_4,
        \overleftarrow{X_1},X_6.}                                \tag{4.3}
\]

Thus the successful macro uses ordinary abstract signed-block freedom, but
its legality is genuinely state-dependent.

## 5. Router--splitter theorem

Let `G(T)` be a target--cell graph.  Suppose its reachable deficient region
is the disjoint union

\[
                  (L_i,R_i),\qquad |L_i|=|R_i|+1,
                  \qquad i=1,\ldots,h,                            \tag{5.1}
\]

and every `R_i` is saturated by a matching.  Fix a maximum matching

\[
                 M=M_{\rm ext}\sqcup M_1\sqcup\cdots\sqcup M_h, \tag{5.2}
\]

where $|M_i|=|R_i|$, all displayed right-cell sets are mutually disjoint,
and

\[
                 |M_{\rm ext}|=\nu(G(T))-\sum_i|R_i|.           \tag{5.3}
\]

Suppose one physical word realizes distinct native pins on all `R_i`.  Let
$B$ be the full cumulative target family whose common-word pins must survive,
including any previously discharged components, and let
$x\in L_j\setminus B$ be the next unresolved target.

### Theorem 5.1 (protected remote router plus native splitter)

Assume `T -> T_*` is $B$-protected shore-neutral and `T_* -> T'` has the
following properties for one component `L_j`:

1. there are an exterior matching $M'_{\rm ext}$ of size $|M_{\rm ext}|$,
   matchings $M'_i$ from $L_i$ of size $|R_i|$ for every $i\ne j$, and an injection
   $\phi_j:L_j\to R(T')$; all their right-cell sets are mutually disjoint;
2. one final physical word realizes a common-word injection of
   $B\cup\{x\}$, including every cumulative protected exterior pin;
3. the surviving `h-1` components remain gap one.

Then

\[
                         \delta_H(T')=h-1.                        \tag{5.4}
\]

Moreover, on the old deficient target shore, the same final word realizes
one more distinct pin than before.

#### Proof

The disjoint union in clause 1 has size

\[
 |M_{\rm ext}|+\sum_{i\ne j}|R_i|+|L_j|
 =\nu(G(T))+1.                                                  \tag{5.5}
\]

Conversely, the union of the surviving `h-1` components has gap `h-1`;
hence equality holds in (5.4).  Clause 2 is the literal simultaneous
common-`Q` gain $B\mapsto B\cup\{x\}$.  ∎

The theorem does not require the router component and splitter component to
coincide.  In (1.1) they are rooted at `24610` and `4877`, respectively.

## 6. Conditional orbit-hitting theorem

Let $A_h(B)$ be the class of **witnessed states**

\[
       (T,B,Q,\iota,M_{\rm ext},M_1,\ldots,M_h),                \tag{6.1}
\]

where $T$ has the unit decomposition (5.1), $Q$ is one physical word, and
$\iota$ is a target--cell injection realizing all of $B$ in $Q$; the
displayed matchings separately witness the Hall decomposition, with every
right-cell disjointness required by Theorem 5.1 recorded in the state.  Let
$N_h(T;B)$ be the orbit of such
witnessed states under $B$-protected neutral braids, inside the fixed-deck,
fixed-endpoint fibre.  Let $\Sigma_h(B)$ be the states admitting a splitter
with some $x\notin B$ whose endpoint is a witnessed member of
$A_{h-1}(B\cup\{x\})$.

Define

\[
 d_h(T;B)=\min\{\ell:\text{an }\ell\text{-router path from }T
                         \text{ reaches }\Sigma_h(B)\}.           \tag{6.2}
\]

### Theorem 6.1 (orbit hitting is sufficient)

If \(d_h(T;B)<\infty\), then `T` reaches level `h-1` in at most

\[
                              d_h(T;B)+1                          \tag{6.3}
\]

legal braids, with a one-unit endpoint common-`Q` gain.  If this hypothesis
holds recursively for every reached level, then after at most

\[
                     \sum_h(d_h(T_h;B_h)+1)                       \tag{6.4}
\]

moves all corresponding unit deficits are discharged.

#### Proof

Follow a shortest neutral path to `Sigma_h`, apply its protected splitter,
set $B_{h-1}=B_h\cup\{x_h\}$, and invoke Theorem 5.1.  Iterate.  ∎

Full transitivity of the neutral groupoid is therefore unnecessary.  It is
enough that every relevant neutral orbit hit one splitter locus.

For the authoritative Hall-23 state, exhaustive evaluation of all `9143`
resident/all-upper-safe one-braid moves found no Hall-22 neighbour.  The
first braid in (1.1) is neutral and its endpoint has the second braid as a
protected splitter.  The cumulative certificate of Section 3.2 proves that
the neutral endpoint also carries the full 1145-target family inherited from
the Hall-24 shore.  Hence (6.5) holds both for the 984-target active basis and
for this audited cumulative basis:

\[
 d_{23}(T_{23};B_{\rm active})
 =d_{23}(T_{23};B_{\rm cumulative})=1.                          \tag{6.5}
\]

## 7. What is and is not invariant

The following are proved invariants of the abstract braid fibre:

* the complete middle deck;
* the first and last middle states.

Hall level is invariant only because it is imposed in the definition of a
neutral edge.  No further invariant presently separates the Hall-23 state
from its splitter locus.

Several tempting invariants are false.  In particular, the weak-neutral
move

\[
                         \operatorname{FF}(1069,4640,6051)        \tag{7.1}
\]

replaces the actual `3/2` DM component

\[
             \{1103,1359,5199\}\quad\text{by}\quad
             \{1227,1259,5323\}.                                \tag{7.2}
\]

Thus neither the DM root list nor the native missing-root list is invariant
under weak neutral moves.  The q=2 lower support simultaneously exchanges
`1227` for `1103`, while q=3 loses `1226`; deeper lower support is not an
invariant either.

There is nevertheless a sharp local warning.  From the state in (7.1), an
exhaustive scan of all `7309` resident/all-upper-safe moves retaining four
immediate-lower holes finds exactly one move whose new depth-at-most-two
native trace equals the missing root `1227`:

\[
                         \operatorname{FF}(1069,2481,6051).       \tag{7.3}
\]

It is the exact inverse of (7.1), and restores the old component.  Therefore
the direct native-root-trace portal graph is not locally transitive at this
state.  This is not a no-go for exceptional pins, longer neutral paths, or
general boundary-profile splitters.

The Hall-23 root-atom bank gives the same lesson: 54 singleton atoms can be
safely shrunk to their six large-component roots, but each isolated shrink
displaces the atom's old native pin and keeps the total current at 984.  A
duplicate atom port or a genuine multi-column splitter is the capacity gate;
prepared root atoms alone do not imply transitivity.

## 8. Exactly one missing statewise lemma

The remaining theorem is the following.

> **Protected router orbit-hitting lemma.**  Every admissible unit-current
> carrier in the fixed endpoint/deck fibre has a shore-neutral orbit meeting
> a protected common-`Q` splitter locus; the splitter endpoint again has a
> unit-component decomposition and a common-word current, with the entire
> cumulative protected target family preserved or simultaneously reselected.

This one lemma, together with Theorem 6.1, is the exact inductive descent
gate.  It is strictly weaker than neutral-group transitivity and stronger
than the existence of isolated root atoms.  The Hall-23-to-Hall-22 pair
proves one nontrivial instance.  No statewise invariant currently refutes
it, and no general proof is known.

For a fixed `FR(a,u,v)` splitter frame, the RF lemma makes this gate more
concrete without suppressing the labels.  Define

\[
\begin{aligned}
\mathcal R_{T,B}(a,u,v)=\{(r,s,t,x):
 &0<r<s\le x<x+1\le t<W-1,\quad r+t-x=u,\\
 &T_{r-1}\sim T_t, T_s\sim T_r, T_{s-1}\sim T_{t+1},\\
 &\operatorname{RF}(r,s,t)T\text{ is }B\text{-protected neutral and fixes}\\
 &\text{the rows at positions }a-1,a,v,v+1\}.
\end{aligned}                                                    \tag{8.1}
\]

Also let

\[
 \mathcal F_{a,v}(T)=\{x:
 T_{a-1}\sim T_x, T_v\sim T_{x+1}, T_a\sim T_{v+1}\}.        \tag{8.2}
\]

A tuple in (8.1) makes the following `FR(a,u,v)` endpoint-Johnson exactly
when its $x$ lies in (8.2).  It gives a protected splitter only after four
further labelled checks: splitter residence, every protected lower/upper
support ledger, the required envelope/mandatory refinement, and one joint
$B\cup\{x_0\}$ common-word current with the exterior cell disjointness of
Theorem 5.1.  (Here $x_0$ denotes the newly discharged target, not the source
index $x$.)  The present tuple is

\[
                 (r,s,t,x)=(3799,4497,6039,5787).               \tag{8.3}
\]

For longer router paths one takes the move-generated reachability closure of
these fully witnessed, anchor-labelled states.  Thus the missing lemma is a
labelled orbit--splitter-frame intersection theorem, not an abstract
permutation theorem and not merely an unlabelled root-port assertion.

At Hall 22 the five remaining `2/1` components have the following complete
shared-column atlas.  Each row lists root, child, extra bit, cell, start, and
native controller triple.

| root | child | bit | cell | start | controller triple |
|---:|---:|---:|---:|---:|---|
| 2420 | 2932 | 512 | 17011 | 4136 | `(2836,2884,868)` |
| 2676 | 10868 | 8192 | 14569 | 1694 | `(10788,8804,8308)` |
| 9524 | 9588 | 64 | 14571 | 1696 | `(8308,9300,9552)` |
| 17683 | 21779 | 4096 | 14560 | 1685 | `(5394,21762,20739)` |
| 19568 | 27760 | 8192 | 16115 | 3240 | `(10352,11360,25696)` |

Their mandatory masks are respectively

\[
                 2416, 2672, 1332, 17683, 19536,                \tag{8.4}
\]

all contained in the corresponding root.  Hence each is exactly in the
coarse-column starting state of Lemma 3.1.  What remains is to route a legal
nested refinement to it while protecting the cumulative current.  This table
does not itself prove that any of the five frame orbits meets its splitter
locus.  The larger, `3/2`, `5/4`, and zero-cell components require the
general protected-ear version of Theorem 5.1 rather than only Lemma 3.1.

## 9. Frozen artifacts

| file | SHA-256 |
|---|---|
| `scratch/k15_segment_braid_hall23.json` | `8feab1da65f3924d29609246798fc543dc50d076ca9db363e8796dda2c22598d` |
| `scratch/k15_segment_braid_hall23_portal.json` | `9f6c2631ca0ffdd24aa0f9b4cf979b223995251e4c241cef4ad61a67026646b6` |
| `scratch/k15_segment_braid_hall22.json` | `c4d36b5972a07e8c7694a741bbc5cc4a5d657ef13c434bd42433b0fc51b01798` |
| `scratch/k15_segment_braid_h22_router_splitter_audit_20260728.json` | `e0d591d6c0a7b9715bf4f6fc2007402a7e53215051390e50c01b3be3142070f6` |
| `scratch/audit_k15_h23_rf_port_router.py` | `27fc6bba070fe7f5f62dd528c9644c73af7d49cc8569e4f6c152e6143f0e9481` |
| `scratch/k15_h23_rf_port_router_certificate.json` | `a0101ffcfe504168899d838bb50e78433aaf97e1f1703fb6af423cd49d98fa2e` |
| `scratch/audit_k15_h22_router_splitter_common_q.py` | `559d96a1fe0d490b7942ba923789e0898c9c75c4d2f1201a69bea0772a2c84a2` |
| `scratch/k15_h22_router_splitter_common_q_certificate.json` | `fb8aae805a974e9a8c8b143db860ddaf7528913ee27aaa3e7034bbba39f292e9` |
| `scratch/audit_k15_h22_cumulative_h24_common_q.py` | `38a66e3818252f2be6f29b15519e2366532adde8c117a0045769e27e478f02f0` |
| `scratch/k15_h22_cumulative_h24_common_q_certificate.json` | `cae7b0aaad67bb8f09a70b45337a549c33b34a8b904833414a14299bece3f189` |
| `scratch/audit_k15_h23_root_atom_port_bank.py` | `e048b6654d9a78b8c3adc6d049ec2402edde0a19bf1be74ec01bc7d5122a59c6` |
| `scratch/k15_h23_root_atom_port_bank_certificate.json` | `273c06a0ece68e5d0de6826b8e184b2d1afee284ba7b7e2ffa80af34afd4a375` |
| `scratch/threadD_h23_one_braid_scan_20260728.txt` | `fbccfd2fb442a2682f854a55e97bafcdd45f2638e49356fb1748fc6c311956ac` |
