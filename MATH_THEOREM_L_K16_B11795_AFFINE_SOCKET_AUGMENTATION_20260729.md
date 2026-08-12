# K16 motif 390: exact affine-socket augmentation theorem

Date: 2026-07-29  
Status: proved, solver-free.  This note determines the exact finite-capacity
Hall--Farkas payment needed to defeat the 17-colour, eight-socket affine
certificate for the internal motif-390 edge.  It separates defeat of that
one fractional ray from integral alternating recourse and from residence.

## 1. Frozen affine socket

Let `Q` be the detector-zero endpoint and `R` the fixed resident endpoint.
For an edge of `Q\R`, let `x_h>=0` denote deletion; for an edge of `R\Q`,
let `y_a>=0` denote insertion.  The branch edge is

\[
 e_*=(57902,57998),\qquad x_{e_*}=b_{11795}.                 \tag{1.1}
\]

The exact affine audit has the priced lower and upper colour sets

\[
\begin{aligned}
C_L={}&\{18526,47652,51230,57870,57894,59406,61988\},\\
C_U={}&\{27742,47645,47676,47772,59486,59950,62118,
64038,64044,65060\},                                      \tag{1.2}
\end{aligned}
\]

and the charged rank-eight socket set

\[
S=\{26718,47644,47660,59422,59918,59942,61990,64036\}.      \tag{1.3}
\]

Every colour in (1.2) has exactly one provider in `Q`.  The all-unit sum of
the seventeen resulting q1 rows and the eight degree equalities at `S` is

\[
\boxed{
b_{11795}+r_{5685}+r_{8352}+r_{9710}+r_{9960}
 +r_{10793}+r_{12168}\le0.}                                \tag{1.4}
\]

Thus `b11795=0` over the nonnegative reals.  Its active support consists of
17 blue edges and 16 red edges on 40 physical vertices.  Only the eight
vertices in (1.3), not all 40 vertices, have nonzero degree dual.

## 2. The mixed-rank socket row

For a physical Johnson edge `e=uv`, put

\[
 \ell(e)=u\cap v,\qquad U(e)=u\cup v,                       \tag{2.1}
\]

and define its colour price, socket cost, and signed gain by

\[
\begin{aligned}
p(e)&=1[\ell(e)\in C_L]+1[U(e)\in C_U],\\
s(e)&=1[u\in S]+1[v\in S],\\
g(e)&=p(e)-s(e).                                            \tag{2.2}
\end{aligned}
\]

### Theorem 2.1 (exact affine-socket row)

Let `X` be any set of allowed blue deletion columns and `Y` any set of
allowed red insertion columns.  If nonnegative vectors `(x,y)` satisfy the
seventeen q1 coverage rows and exact degree balance at every vertex of `S`,
then

\[
\boxed{
        \sum_{h\in X}g(h)x_h\le \sum_{a\in Y}g(a)y_a.}       \tag{2.3}
\]

This is a simultaneous rank-seven/rank-nine provider row charged against
rank-eight endpoint capacity.  Parallel physical seam IDs, if present, are
separate columns; endpoint incidence is counted with multiplicity.  The
present physical graph is loopless.

#### Proof

For `c in C_L union C_U`, let `e(c)` be its unique provider in `Q`.
Its exact normalized coverage row is

\[
 x_{e(c)}\le \sum_{a:\,a\text{ provides }c}y_a.             \tag{2.4}
\]

Summing (2.4) over the seventeen colours gives

\[
 \sum_h p(h)x_h\le\sum_a p(a)y_a.                           \tag{2.5}
\]

Summing the exact degree equations over `v in S` gives

\[
 \sum_h s(h)x_h=\sum_a s(a)y_a.                             \tag{2.6}
\]

Subtracting (2.6) from (2.5) proves (2.3).  No integrality is
used.  Expanding (2.3) on the frozen overlay gives exactly (1.4).  QED.

On the 33 active columns, the complete signed census is

\[
\begin{array}{c|cc}
 &g=1&g=0&g=-1\\ \hline
\text{blue deletions}&1&16&0\\
\text{red insertions}&0&10&6.
\end{array}                                                \tag{2.7}
\]

The unique positive blue column is `e_*`.  Moving the six negative red
terms to the left in (2.3) is precisely (1.4).

## 3. Finite-capacity provider/socket payment

Let `A+` be any family of exterior red seams, each with capacity `u_a>=0`.
Apply the finite-capacity global endpoint Hall--Farkas theorem with

\[
 \lambda=1_{C_L\cup C_U},\qquad w=1_S.                      \tag{3.1}
\]

All frozen red columns satisfy `p(a)<=s(a)`.  An added column has positive
dual excess

\[
 \delta(a)=[p(a)-s(a)]_+=[g(a)]_+.                          \tag{3.2}
\]

At the branch point `b11795=1`, the resource side of this ray is one and
the freed charged-socket capacity is zero.  The bounded-column Hall row is
therefore

\[
\boxed{
              1\le\sum_{a\in A^+}u_a\delta(a).}             \tag{3.3}
\]

Equation (3.3) is necessary for fractional recourse.  It is also the exact
threshold at which this fixed dual ray stops separating the capacity-
projected branch: below one the same ray still proves impossibility; at or
above one this ray alone gives no contradiction.  It is not a sufficient
condition for the augmented primal system.

If independent extra endpoint capacities `eta_v` are supplied at charged
sockets, (3.3) becomes

\[
 1\le \sum_{v\in S}\eta_v+sum_{a\in A^+}u_a\delta(a).       \tag{3.4}
\]

A physical deletion is not free socket capacity: deleting a blue edge `h`
frees `s(h)` charged endpoints but can create `p(h)` priced q1 demands.  Its
exact net payment is therefore `[-g(h)]_+`.  For any additional deletion
columns of the same frozen source `Q` for which the seventeen normalized
rows remain (2.4), allowing red and blue columns simultaneously gives the
necessary row

\[
\boxed{
1\le
 \sum_{a\in A^+}u_a[g(a)]_+
 +\sum_{h\in B^+}v_h[-g(h)]_+.}                             \tag{3.5}
\]

The undropped signed form of (2.3) is stronger and should be used in an
exact model.  In particular, columns of the opposite sign can be essential
degree routers even though they do not pay (3.5).

## 4. Complete K16 census and the exact minimum

Every priced rank-seven or rank-nine colour has 36 physical Johnson
providers.  Direct deduplication gives 595 distinct provider edges.  Their
complete `(p,s)` census is

\[
\begin{array}{c|rrrrr}
(p,s)&(1,0)&(1,1)&(1,2)&(2,1)&(2,2)\\ \hline
\#&407&166&5&14&3.
\end{array}                                                \tag{4.1}
\]

There is no `(2,0)` edge.  Equivalently, all seventeen edges that provide
both one priced lower and one priced upper colour meet at least one charged
socket: fourteen meet one and three meet two.  Hence

\[
                         \max_e |g(e)|=1                    \tag{4.2}
\]

on every provider or socket-relevant physical Johnson edge.

After removing `Q union R`, 568 priced provider edges remain.  Their exact
red-augmentation census is

\[
\begin{array}{c|rrr}
g&1&0&-1\\ \hline
\#&420&143&5.
\end{array}                                                \tag{4.3}
\]

Thus 420 and only 420 exterior red seams can weaken the affine ray.  All
have gain exactly one.  The other 148 have `delta=0`; five of them actually
strengthen the signed row.

For the socket side, the union of all priced providers and all Johnson
edges incident with `S` has 911 relevant edges.  There are 878 exterior
ones, with signed-gain histogram

\[
\begin{array}{c|rrr}
g&1&0&-1\\ \hline
\#&420&143&315.
\end{array}                                                \tag{4.4}

The 315 negative-gain edges are the complete exterior *potential*
blue/socket-donor list for these frozen weights.  Every one has gain `-1`;
none has gain `-2`.  They are not deletion columns of the present source.
If carrier surgery first makes one of them a source edge, the source loads
and row normalization must be rebuilt before (3.5) is reused.

### Corollary 4.1 (sharp fractional and unit-column minima)

For red-provider augmentation alone, the exact capacity payment required
to make the affine ray nonseparating is one full unit:

\[
                    \sum_{a:g(a)=1}u_a\ge1.                 \tag{4.5}
\]

The same one-unit minimum holds for pure blue/socket augmentation.  In
particular, unlike the doubled all-three-branch Hall row, this affine
summand has no value-two column and admits no half-column fractional escape.
For unit-capacity physical columns, one of the 420 positive red seams is
the exact minimum catalogue augmentation.  Examples are

\[
 (11358,19550)\quad\text{providing }U_{27742},\qquad
 (18527,18558)\quad\text{providing }L_{18526}.               \tag{4.6}
\]

Both have `(p,s,g)=(1,0,1)`.

For selected augmentation variables, the cheap exact search cut is

\[
\boxed{
 b_{11795}\le\sum_{a\in G_A}z_a,\qquad |G_A|=420,}          \tag{4.7}
\]

where `G_A` is the frozen list of exterior gain-one red seams.  Equation
(4.7) follows by retaining `b11795` and dropping only nonnegative terms
from the full signed row.  It is necessary, not sufficient.

## 5. Integral recourse is a separate gate

One new seam cannot be a nontrivial exact edit of a simple two-factor.  If
one old edge is deleted and one new edge inserted while every vertex keeps
degree two, their endpoint multisets coincide, so the two undirected edges
are equal.  Therefore every nontrivial factor edit needs at least two
deletions and two insertions.

That lower bound is attained for the affine branch at the guarded-core
level:

\[
\begin{array}{ll}
\text{delete}&(57902,57998),\ (59918,59948),\\
\text{insert}&(57902,59948),\ (57998,59918).
\end{array}                                                \tag{5.1}
\]

The first inserted seam has `g=1`, the second has `g=0`, and (4.7) is
tight.  This Johnson square preserves all 21 guarded q1 loads exactly and
deletes the internal motif edge.  The exhaustive frozen C4 audit finds
exactly three such guarded-safe internal-edge squares.

This is not full integral recourse.  The particular square (5.1) creates
the upper-q1 hole `U58030` and replaces motif 390 by two new length-two
motifs, increasing the short-motif count by one.  Moreover, among all 25
Johnson squares through the three motif-390 closure edges, the unique square
preserving both complete physical q1 palettes uses the incoming-boundary
branch, not the affine internal branch.  Thus:

* minimum catalogue payment for the affine ray: one red seam;
* minimum degree-balanced, guarded-q1 affine edit: two inserted seams;
* complete-q1 affine recourse by such a C4: impossible;
* longer affine recourse preserving full q1 and residence: open.

A different radius-two carrier trade can create a second `U27742`
occurrence while preserving both full q1 palettes:

\[
\begin{array}{ll}
\text{delete}&(25662,27678),\ (25694,25722),\\
\text{insert}&(25662,25722),\ (25694,27678).
\end{array}                                                \tag{5.2}
\]

This invalidates the source-unique affine certificate after the carrier is
rebuilt, but it does not itself hit motif 390 and its residence effects are
not certified.  It is preconditioning, not completion.

## 6. Consequence for the nearly-full Johnson catalogues

The exhaustive 732-edge guarded-colour provider seed contains every one of
the 420 gain-one affine columns.  Therefore any provider-star catalogue
which includes that seed has already invalidated the fixed affine ray at
depth zero.  Adding hundreds of thousands of further neutral shell edges
cannot make the old ray a proof of infeasibility again; those edges may
still be indispensable degree routers.

Consequently the stored depth-three `INFEASIBLE` result is not explained by
this affine certificate, and the stored depth-four status remains
`UNKNOWN`.  The remote depth-three/four catalogue payloads are not both
retained locally, so this statement uses their declared provider-seed
construction; local byte-level replay in this note proves only that the
complete 732-edge seed contains all 420 affine-positive columns.

For a future nearly-full search, the proof-safe use of the row is:

1. rebuild `C_L,C_U,S` after every carrier change;
2. recompute `g(e)` from the physical lower/upper colours and both endpoint
   incidences;
3. retain the full signed row (2.3), or at minimum add (4.7) when forcing
   `b11795=1`;
4. do not prune `g<=0` seams individually, since they can close an
   alternating circulation; and
5. after a positive-column escape, independently audit exact degree, both
   complete q1 palettes, every old and new residence motif, deeper shadows,
   topology, and the literal compiler.

## 7. Exact proved boundary

Proved:

* (2.3) is the exact all-real mixed-rank Hall--Farkas row for the affine
  socket;
* the finite-capacity payment is (3.3), and carrier socket donation is
  correctly netted in (3.5);
* the complete physical censuses (4.1)--(4.4) show that both maximum gains
  equal one;
* fractional certificate escape costs exactly one unit;
* one unit-capacity red seam is the minimum catalogue escape;
* two inserted seams are necessary and sufficient for degree-balanced,
  guarded-q1 affine escape; and
* all 420 positive red seams are present in the complete provider seed.

Not proved:

* (3.3), (3.5), or (4.7) is sufficient for fractional feasibility;
* any gain-one seam extends to a legal alternating circuit;
* the affine branch has a full-q1, residence-clean integral recourse; or
* either augmented-catalogue solver status settles the K16 word problem.

## 8. Frozen replay

Authoritative inputs:

```text
08ecd5601d2e43d4effe3e55f1377c87a668476917f04d34c05eafb87fd05f75
MATH_AUDIT_K16_FAILEDLIT0_GUARDED_MOTIF390_SOLVER_FREE_CORE_20260729.md

f6c34d44ca982adc1160362f8f372d77f2f7bc104631dfa3dccd2ff479ddd3c4
scratch/k16_failedlit0_b11795_affine_core_20260729.audit.json

fbd182aff3117581c7cf5216e33a30db3309da23c8d570275114e5a6165985e9
scratch/k16_resident_resume1_q1_canonical_physical_endpoints_20260729.json

9ba223ea58e00cd2f9619c5ce7f309ff45c62b5d90beabb7cea3b30aa254df70
scratch/k16_failedlit0_complete_core_q1_provider_catalogue_20260729.json
```

New solver-free replay:

```text
83eb31d7c7bbb9590753d9126e8306594933c7fafd011bf573a10873c1c46cc5
scratch/audit_k16_b11795_affine_socket_augmentation_20260729.py

44058785dad3707e9baf19ff973f9e7e418f4cd1166f042d45ca41f87183ed4f
scratch/k16_b11795_affine_socket_augmentation_20260729.audit.json
```

The replay uses only the Python standard library and enumerates 911 relevant
Johnson edges.  It performs no SAT, LP, exhaustive factor search, or remote
computation.
