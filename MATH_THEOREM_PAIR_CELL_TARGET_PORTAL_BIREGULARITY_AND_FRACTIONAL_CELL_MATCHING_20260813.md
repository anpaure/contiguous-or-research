# Pair-cell target portals form explicit biregular graphs with fractional cell matchings

**Date:** 2026-08-13  
**Method:** direct counting of sentinel choices, perfect matchings, pair-cell
statuses, and transition-direction blocks.  Exact arithmetic identities
were replayed on `h100`.  
**Status:** unconditional occurrence-labelled degree and matching theorem.
It gives an integral injection of **all** covered lower targets, across all
covered ranks simultaneously, into distinct labelled pair cells.  It does
not choose one common pair frame or one common owner factor, and distinct
cell frames selected by the matching may still intersect in owner vertices.

## 1. Pair-cell occurrences

Put

\[
 k=2R-1,qquad p=R-1.                                               \tag{1.1}
\]

An occurrence-labelled pair cell consists of:

1. a sentinel `z in [k]`;
2. a perfect matching of the remaining `2p` labels;
3. a status `S,D,E` on every matched pair; and
4. a sentinel sector `epsilon in {0,1}`.

If there are `m` singleton pairs, then

\[
 a={R-\epsilon-m\over2},qquad b=p-m-a                              \tag{1.2}
\]

are the numbers of double and empty pairs.  For fixed legal
`(m,epsilon,a,b)`, the number of cell occurrences is

\[
 \boxed{
 H_{m,\epsilon}
 =k(2p-1)!!{p\choose m}{p-m\choose a}.}                             \tag{1.3}
\]

Here `(x)_j=x(x-1)\cdots(x-j+1)` denotes a falling factorial, and the
usual convention `(-1)!!=1` is in force.

Fix once and for all one pointed long-run Hamilton Gray cycle on every
good cube dimension.  Coordinate relabelling transports its pointed block
of distinct transition directions to any prescribed singleton pairs.  The
right shore counted in (1.3) consists only of the labelled cell frames; a
portal incidence also records the transported pointed cycle.  Thus two
different incidences at one frame may use different coordinate relabellings.

## 2. Programmable-letter portal degrees

Let `q>=2`, let

\[
                         h=\lceil3\log_2p\rceil,qquad M=q+h,         \tag{2.1}
\]

and assume `M<=p`.  Fix a rank

\[
                         h+1\le s\le R-q.                           \tag{2.2}
\]

Put

\[
 m=s+q-1,qquad
 \epsilon\equiv R-m\pmod2,qquad
 a={R-\epsilon-m\over2},qquad b=p-m-a.                             \tag{2.3}
\]

For a target `S in binom([k],s)`, call a dimension-`m` cell a
**structural singleton portal** when:

* its sentinel is outside `S`;
* exactly `s` singleton pairs have one endpoint in `S` and one outside;
* its other `q-1` singleton pairs lie wholly outside `S`; and
* every double and empty pair lies wholly outside `S`.

The `q-1` outside singleton pairs may be relabelled as the pointed
transition directions; orient each crossing pair toward its endpoint in
`S`.  The distributed-core source letter at the pointed address then has
fixed variable part exactly `S`, while every permanent coordinate is
outside `S` and may be scheduled to avoid that address.

### Theorem 2.1 (middle portal biregularity)

Every rank-`s` target has exactly

\[
 \boxed{
 D_s={ (k-s)!\over
       2^{p-s}(q-1)!a!b!}}                                        \tag{2.4}
\]

structural singleton-portal cells.  Every legal dimension-`m` cell is a
portal for exactly

\[
 \boxed{
 e_s={m\choose q-1}2^s}                                           \tag{2.5}
\]

rank-`s` targets.  Consequently

\[
 {k\choose s}D_s=H_{m,\epsilon}e_s.                                \tag{2.6}
\]

#### Proof

Fix `S`.  Choose its outside sentinel, then a distinct outside mate for
each of the `s` target labels.  From the remaining outside labels choose
`q-1` unordered transition pairs.  Pair the last `2(p-m)` labels and
choose which `a` of those pairs are double.  The count is

\[
 \begin{aligned}
 &(k-s)(k-s-1)_s
 { (k-2s-1)!\over
   (2(p-m))!2^{q-1}(q-1)!}\\
 &\hspace{12mm}\cdot
 { (2(p-m))!\over2^{p-m}(p-m)!}
 {p-m\choose a},
 \end{aligned}                                                     \tag{2.7}
\]

which simplifies to (2.4), since

\[
                         q-1+p-m=p-s.                               \tag{2.8}
\]

Conversely, in a fixed cell choose the `q-1` transitioned singleton
pairs, then one endpoint from each remaining singleton pair.  This gives
(2.5), and the structural conditions are forced by the resulting target.
Double counting incidences proves (2.6).  \(\square\)

Every incidence in Theorem 2.1 promotes to a literal pointed source
portal: relabel the fixed abstract long-run cycle so its marked transition
block is the chosen `q-1` pairs and its untouched selected sides are the
elements of `S`.

### Corollary 2.2 (exact fixed-pair-frame criterion)

Fix only the sentinel and the perfect matching, before assigning pair
statuses.  A rank-`s` target in the range (2.2) has a middle portal in this
frame if and only if

* the sentinel is outside the target; and
* the target meets every matched pair in at most one coordinate.

When eligible, it has exactly

\[
 g_s={p-s\choose q-1}{p-m\choose a}                       \tag{2.9}
\]

status-cell portals in that fixed frame.  The number of pair frames in
which a fixed target is eligible is

\[
 F_s={ (k-s)!\over2^{p-s}(p-s)!},                         \tag{2.10}
\]

and `D_s=F_sg_s`.

#### Proof

Every target coordinate must occupy one side of a crossing singleton pair,
which is possible exactly under the two displayed conditions.  The `s`
crossing pairs are then forced singleton.  Among the `p-s` pairs disjoint
from the target, choose `q-1` transition-singleton pairs, and among the
remaining `p-m` pairs choose the `a` double ones.  This proves (2.9).

For (2.10), choose the outside sentinel, injectively mate the `s` target
coordinates to outside coordinates, and perfectly match the remaining
`2(p-s)` outside coordinates.  The resulting count is

\[
 (k-s)(k-s-1)_s(2(p-s)-1)!!
 ={(k-s)!\over2^{p-s}(p-s)!}.
\]

Multiplying (2.9) and (2.10) gives (2.4).  \(\square\)

For orientation, in one fixed frame there are exactly

\[
                         {p\choose s}2^s                 \tag{2.11}
\]

eligible rank-`s` targets and

\[
                         {p\choose m}{p-m\choose a}       \tag{2.12}
\]

legal status cells.  Equations (2.5) and (2.9) give the corresponding
fixed-frame incidence double count.  This exposes the precise frame-level
obstruction hidden by global symmetry: targets having a double matched pair,
or containing the sentinel, have degree zero in this middle portal graph.

## 3. The top programmable-letter row

Now put

\[
                         s=R-q+1,qquad m=p.                         \tag{3.1}
\]

Use the sentinel-present all-singleton sector.  A target portal contains
its sentinel, has `s-1` crossing singleton pairs, and has `q-1` singleton
pairs wholly outside the target.

### Theorem 3.1 (top-letter biregularity)

The target and cell degrees are

\[
 \boxed{
 D_s={s(k-s)!\over2^{q-1}(q-1)!},qquad
 e_s={p\choose q-1}2^{s-1}.}                                      \tag{3.2}
\]

With

\[
                         H_p=k(2p-1)!!,                             \tag{3.3}
\]

one has

\[
                         {k\choose s}D_s=H_pe_s.                    \tag{3.4}
\]

#### Proof

Choose the sentinel from `S`, match every other target label to a distinct
outside mate, and pair the final `2(q-1)` outside labels.  This gives the
first formula.  In a fixed all-singleton cell, choose the `q-1` transition
pairs and orient the other pairs toward the target, giving the second.
\(\square\)

For a fixed pair frame, a top-letter target is eligible exactly when it
contains the sentinel and its other `s-1` coordinates lie in distinct
matched pairs.  There is only one sentinel-present all-singleton status
cell in that frame, and all

\[
                         {p\choose s-1}2^{s-1}=e_s        \tag{3.5}
\]

eligible targets are possible pointed portals of that cell.

## 4. Consecutive-intersection fan rows

Let

\[
 R-q+2\le s\le R-1,qquad r=R-s,                                   \tag{4.1}
\]

so `1<=r<=q-2`.  Again use the sentinel-present dimension-`p` cells.  A
target is the intersection of `r+1` consecutive owners when its sentinel
is present, `s-1` singleton pairs cross its boundary, and the other `r`
pairs lie outside it and are used as the consecutive transition block.

### Theorem 4.1 (fan-row biregularity)

The exact degrees are

\[
 \boxed{
 D_s={s(k-s)!\over2^r r!},qquad
 e_s={p\choose r}2^{s-1}.}                                        \tag{4.2}
\]

They satisfy

\[
                         {k\choose s}D_s=H_pe_s.                    \tag{4.3}
\]

Every incidence gives a literal source interval of width `q-r` through
the maximal-antecedent identity.

#### Proof

Identical to Theorem 3.1, with `r` outside transition pairs in place of
`q-1`.  Relabel `r` consecutive directions of the fixed long-run cycle;
they are distinct because `r<q`.  \(\square\)

Here too, in a fixed pair frame eligibility means that the target contains
the sentinel and its other `s-1` coordinates lie in distinct pairs.  The
one all-singleton status cell has exactly

\[
                         {p\choose s-1}2^{s-1}
                         ={p\choose r}2^{s-1}=e_s         \tag{4.4}
\]

possible rank-`s` fan portals.

## 5. Fractional matching with cell capacity

For each one of the rank-specific bipartite graphs above, assign every
target--cell incidence weight `1/D_s`.  Every target then has load one,
while every cell has load

\[
                         \rho_s={e_s\over D_s}.                     \tag{5.1}
\]

### Theorem 5.1 (capacity-one fractional portal matching)

For every rank covered in Sections 2--4,

\[
                         D_s\ge e_s.                                \tag{5.2}
\]

Hence the uniform incidence weights form a fractional matching which
covers every target exactly once and uses every labelled cell with total
weight at most one.

#### Proof

For the middle ranks, cancellation in (2.4)--(2.5) gives

\[
 {D_s\over e_s}
 ={s!(k-s)!\over2^p a!b!m!}.                                      \tag{5.3}
\]

Since `a+b+m=p`,

\[
                         a!b!m!\le p!.                              \tag{5.4}
\]

Also `1<=s<=p`, so factorial log-convexity, or the elementary ratio
test, gives

\[
                         s!(2p+1-s)!\ge p!(p+1)!.                   \tag{5.5}
\]

Finally `(p+1)!>=2^p`, proving (5.2).

For the top-letter and fan rows, put `t=q-1` or `t=r` respectively.
Since `s=p+1-t`, both ratios simplify to

\[
 {D_s\over e_s}
 ={s!(p+t)!\over2^p p!}
 \ge{(p+1)!\over2^p}\ge1.                                        \tag{5.6}
\]

Indeed, before division by `2^p`, the numerator ratio

\[
                         f(t)={ (p+1-t)!(p+t)!\over p!}
\]

is increasing for `t>=1`, because

\[
                         {f(t+1)\over f(t)}
                         ={p+t+1\over p+1-t}>1,
\]

and `f(1)=(p+1)!`.

This proves the theorem.  \(\square\)

### Corollary 5.2 (integral rankwise portal injection)

For every one covered rank `s`, all rank-`s` targets can be assigned to
pairwise distinct occurrence-labelled portal cells.

#### Proof

Let `X` be any set of target vertices and `N(X)` its cell neighbourhood.
The number of incidence edges leaving `X` is `D_s|X|`, while every cell in
`N(X)` receives at most `e_s` of them.  Hence

\[
                         D_s|X|\le e_s|N(X)|.
\]

Theorem 5.1 gives `D_s/e_s>=1`, so `|N(X)|>=|X|`.  Hall's theorem gives
the claimed injection.  Equivalently, one may use integrality of the
bipartite matching polytope on the fractional matching above.  \(\square\)

### Theorem 5.3 (simultaneous all-covered-rank cell injection)

All targets of ranks

\[
                         h+1\le s\le R-1
\]

can be assigned simultaneously to pairwise distinct occurrence-labelled
portal cells.

#### Proof

For every middle row except its endpoint `s=R-q`, the dimension
`m=s+q-1` is less than `p` and is different for different `s`.  Hence the
cell shores of these rank graphs are disjoint, and their Corollary 5.2
matchings coexist automatically.

It remains to combine the `m=p` rows.  They are exactly

* the endpoint middle row `s=R-q`;
* the top-letter row `s=R-q+1`; and
* the `q-2` fan rows of Section 4.

Thus there are `q` rows on the common all-singleton, sentinel-present
cell shore of size `H_p`.  On the union of these rank graphs, give an edge
in row `s` weight `1/D_s`.  Every target again has load one.  By the proof
of Theorem 5.1, every one of these rows satisfies

\[
                         {e_s\over D_s}\le {2^p\over(p+1)!}.
\]

Consequently every common cell has total load at most

\[
                         {q2^p\over(p+1)!}
                         \le {p2^p\over(p+1)!}\le1.                \tag{5.7}
\]

Here `q<=p` follows from `q+h<=p`, and `p2^p<=(p+1)!` for `p>=3`
(equality at `p=3`, followed by an immediate ratio induction); our standing
assumption `q+h<=p` is already stronger.  This is a fractional matching
covering every target in the union graph, so bipartite matching integrality
gives an integral target-saturating matching into distinct `m=p` cells.
Combining it with the disjoint lower-dimensional matchings proves the
claim.  \(\square\)

Theorem 5.1 is strictly stronger than a fractional target cover which
ignores its host: it respects one unit of capacity per occurrence-labelled
cell.  Theorem 5.3 turns the whole covered target bank into an exact
occurrence-cell injection, so each selected cell needs only one marked
portal and its own coordinate-relabelled cycle.  This still is not a common
owner factor: the selected cell frames have unrelated pair partitions and
can share owner vertices.  Therefore no collision-free physical atlas or
common owner factor follows.

## 6. Exact same-rank target codegrees

The same symmetry also gives closed codegree formulas.  In this section
write `binom(n,j)=0` when `j` lies outside `[0,n]`.

### Theorem 6.1 (middle-row codegrees)

Fix two rank-`s` middle targets `S,T` with `|S\cap T|=j`.  The number
`lambda_{s,j}` of occurrence-labelled status cells which are portals for
both targets is

\[
 \boxed{
 \lambda_{s,j}
 ={D_s n_{s,j}\over
   {s\choose j}{k-s\choose s-j}},}                         \tag{6.1}
\]

where

\[
 n_{s,j}
 =\sum_{c=0}^{s}
   {s\choose c}{q-1\choose s-c}{c\choose j}2^{s-c}.        \tag{6.2}
\]

#### Proof

Work first in one fixed legal cell and condition on one of its eligible
targets `S`.  Its pair support has size `s`, leaving `q-1` singleton pairs
unused.  If a second target uses `c` of the same pair supports, choose those
supports, choose its other `s-c` supports from the unused pairs, choose the
`j` common supports on which it takes the same endpoint as `S`, and orient
its new supports arbitrarily.  On the other `c-j` common supports it must
take the opposite endpoint.  This gives (6.2).

There are `H_{m,epsilon}e_sn_{s,j}` ordered triples
`(cell,S,T)` with intersection `j`.  On the other hand there are

\[
 {k\choose s}{s\choose j}{k-s\choose s-j}
\]

ordered target pairs of this intersection type, and transitivity of the
symmetric group makes their common cell degree constant.  Use (2.6) and
cancel `{k\choose s}` to obtain (6.1).  \(\square\)

### Theorem 6.2 (top-letter and fan-row codegrees)

For either a top-letter row with `t=q-1` or a fan row with `t=r`, put
`u=s-1=p-t`.  Two rank-`s` targets with intersection size `j` have common
cell degree

\[
 \boxed{
 \lambda_{s,j}
 ={D_s n^{\rm top}_{s,j}\over
   {s\choose j}{k-s\choose s-j}},}                         \tag{6.3}
\]

where

\[
 n^{\rm top}_{s,j}
 =\sum_{c=0}^{u}
   {u\choose c}{t\choose u-c}{c\choose j-1}2^{u-c}.       \tag{6.4}
\]

In particular `lambda_{s,0}=0`.

#### Proof

Every target adjacent to one fixed all-singleton cell contains that cell's
sentinel.  After removing it, repeat the support-overlap count above with
`u` used pairs and `t` unused pairs; the remaining target intersection has
size `j-1`.  The same global ordered-pair double count, now using (3.4) or
(4.3), gives (6.3).  Disjoint targets cannot share the required sentinel,
which is also immediate from (6.4).  \(\square\)

These formulas measure overlap only in the occurrence-cell portal graph.
They do not assert that the two incidences use the same transported Gray
cycle; Theorem 5.3 deliberately assigns at most one target to each selected
cell.

## 7. Verification artifact

`verify_pair_cell_portal_biregular_degrees.py` replays (2.4)--(4.3) with
exact integers and evaluates the minimum `log(D_s/e_s)`.  On `h100`, the
instances `k=101,201,301,401,641,1001` all returned `PASS`; their minimum
ratios occurred in the rank-`R-1` fan row and already had logarithms

\[
 117.75, 299.04, 506.07, 729.91, 1313.63, 2270.97,               \tag{6.1}
\]

respectively.  The computation audits the formulas; Theorem 5.1 is the
symbolic all-parameter proof.
