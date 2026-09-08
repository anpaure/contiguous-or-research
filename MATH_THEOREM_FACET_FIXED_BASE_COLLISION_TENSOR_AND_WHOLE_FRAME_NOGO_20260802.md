# Fixed-base facet frames: exact collision tensor and the whole-frame packing no-go

Date: 2026-08-02  
Status: unconditional exact intersection formula, unconditional no-go for
packing intact maximum fixed-base frames, and an unconditional probabilistic
extraction of `Theta(W/q^2)` pairwise owner/target-disjoint individual
modules for all sufficiently large canonical parameters.  The extraction
is only at the named-resource layer; it does not allocate source
occurrences, build a chronology, or prove an OR-word upper bound.

## 0. Outcome

Put

\[
 q=d+2,\qquad c=r-q+1,
\]

and consider the fixed-base subset-core frame

\[
 [k]=D\ \dot\cup\ G\ \dot\cup\ V,
 \qquad |D|=a\ge1,\quad |V|=q,
\]

whose modules are indexed by

\[
 X\in\binom G{c-a}.
\]

The first result below gives the exact collision tensor between two such
frames, at the owner row and at every named-target rank.  Every tensor entry
is one binomial coefficient, or zero, determined by compatibility of two
partial `0/1` assignments.

The formula has a decisive consequence for the proposed global batching
route.  For singleton-base frames, if

\[
                         r\ge2q,\qquad k-r\ge2,                 \tag{0.1}
\]

then **every two intact frames share a rank-`r` owner**.  Thus, in the
canonical asymptotic range, the maximum number of mutually
resource-disjoint intact singleton-base frames is one, not
`Theta(2^q/q^2)`.

The first open finite case is even sharper.  At

\[
             k=17,\qquad q=5,\qquad c=5,\qquad r=9,            \tag{0.2}
\]

one singleton-base frame has

\[
                         \binom{11}{4}=330                      \tag{0.3}
\]

modules.  Any two frames either share an owner, or are in the unique
owner-disjoint support configuration.  In that configuration their named
deck intersections, rank by rank, are

\[
\begin{array}{c|ccccc}
\text{rank}&5&6&7&8&9\\ \hline
\text{common resources}&10&10&125&25&0.
\end{array}                                                    \tag{0.4}
\]

In particular no two intact `330`-module frames are resource-disjoint.
Numerically three intact frames would contain `990` modules, just above
`W/q^2=24310/25`, but that tempting three-frame shortcut is impossible.

The generalized reservoir remains valuable as a **candidate cluster**.
What survives is the proper-subfamily problem: select module subsets from
many overlapping frames so that all cylinder images are disjoint.  The
tensor below is an exact finite kernel for that matching problem.  Section
9 solves this asymptotically at the order-of-magnitude level: sample
`Theta(2^q/q^2)` frames and delete every module which collides with another
sampled frame.  The expected deleted fraction is bounded away from one, so
`Theta(W/q^2)` modules remain.  Treating a whole frame as one hyperedge is
false, but expanding the clusters and pruning them succeeds.

## 1. Every resource occurrence is a Boolean cylinder

Fix a frame

\[
 {\cal R}=(D,V,\beta,\sigma,w,h),
 \qquad \beta\in D,\quad w,h\in V,\quad w\ne h.              \tag{1.1}
\]

For disjoint sets `R,F` and an integer `s`, write

\[
 {cal Q}_s(R,F)
 =\left\{S\in\binom{[k]}s:R\subseteq S,\ S\cap F=\varnothing\right\}.
                                                                    \tag{1.2}
\]

The complete resource deck of the frame is the following collection of
cylinders.

\[
\begin{array}{c|c|c|c}
\text{row label }\rho&s_\rho&R_\rho&F_\rho\\ \hline
P&c&(D-\{\beta\})\cup\{w\}&\{\beta\}\cup(V-\{w\})\\
H&c+1&D\cup\{h\}&V-\{h\}\\
I_{j,u}&c+j&D\cup I_{j,u}(\sigma)&V-I_{j,u}(\sigma),\quad
                   2\le j\le q-2, u\in\mathbb Z/q\\
O_v&r&D\cup(V-\{v\})&\{v\},\quad v\in V.
\end{array}                                                     \tag{1.3}
\]

Here `I_(j,u)(sigma)` is the cyclic `j`-interval of `sigma` beginning at
`u`.

### Lemma 1.1 (exact cylinder representation)

For every row label `rho`, the resources of that occurrence over all
modules `X in binom(G,c-a)` are exactly

\[
                         {cal Q}_{s_\rho}(R_\rho,F_\rho).      \tag{1.4}
\]

Every member of (1.4) belongs to a unique module, namely the module indexed
by its intersection with `G`.  In particular every cylinder has size

\[
                         \binom{k-a-q}{c-a}.                   \tag{1.5}
\]

#### Proof

For the `H`, interval and owner rows, a resource is `D union X union A`,
where `A` is respectively `{h}`, `I_(j,u)`, or `V-{v}`.  It contains the
selected part `D union A`, avoids `V-A`, and its remaining `c-a` points are
exactly `X subseteq G`.

For `P`, the resource is

\[
                 (D-\{\beta\})\cup X\cup\{w\}.
\]

It contains `(D-beta)+w`, avoids `beta` and every tag other than `w`, and
again has precisely the free part `X`.  This proves (1.4), uniqueness, and
(1.5). \(\square\)

## 2. The exact collision tensor

Let `mathcal R` and `mathcal R'` be two frames, with their corresponding
data `(s_rho,R_rho,F_rho)` and `(s'_(rho'),R'_(rho'),F'_(rho'))`.
Only labels of the same rank can collide.  For such labels define

\[
 \Theta_{\rho,\rho'}({\cal R},{\cal R}')
 =\left|{cal Q}_{s_\rho}(R_\rho,F_\rho)
            \cap{cal Q}_{s_\rho}(R'_{\rho'},F'_{\rho'})\right|. \tag{2.1}
\]

Use the convention that a binomial coefficient is zero if its lower
argument is negative or exceeds its upper argument.

### Theorem 2.1 (partial-assignment collision tensor)

Put

\[
 U=R_\rho\cup R'_{\rho'},\qquad
 Z=F_\rho\cup F'_{\rho'}.
\]

Then

\[
 \boxed{
 \Theta_{\rho,\rho'}
 ={\mathbf 1}_{\{U\cap Z=\varnothing\}}
   \binom{k-|U|-|Z|}{s_\rho-|U|}.}
                                                                    \tag{2.2}
\]

The intersection of the complete rank-`s` decks is the sum of (2.2) over
the row labels at rank `s`.  No resource is double-counted in this sum.

Moreover, every common resource determines a unique ordered pair of
modules, one in each frame.  Hence (2.2) is simultaneously the exact
resource-collision tensor and the exact multiplicity tensor of the
bipartite module-conflict graph.

#### Proof

If `U cap Z` is nonempty, one frame requires a coordinate which the other
forbids, so the intersection is empty.  Otherwise a common resource must
contain all of `U`, avoid all of `Z`, and choose its remaining
`s_rho-|U|` points freely from the `k-|U|-|Z|` unassigned coordinates.
This is (2.2).

Within one frame, the selected tag set is recovered as `S cap V` (and for
`P` there is only one label).  Distinct same-rank labels therefore give
disjoint cylinders.  Lemma 1.1 recovers the module from `S cap G` in each
frame. \(\square\)

Formula (2.2) is the promised exact tensor.  It includes arbitrary
overlaps among `D,V,D',V'`, arbitrary cyclic orders, and both low rows.  No
independence or generic-position hypothesis is present.

## 3. A useful closed form for disjoint singleton supports

Take singleton bases `D={d}` and `D'={d'}` and suppose

\[
                 (\{d\}\cup V)\cap(\{d'\}\cup V')=\varnothing. \tag{3.1}
\]

Then Theorem 2.1 gives the following order-independent spectrum.

### Corollary 3.1 (disjoint-support collision spectrum)

\[
\begin{array}{c|c}
\text{row}&\text{number of common resources}\\ \hline
P&\displaystyle \binom{k-2q-2}{c-2}\\[3mm]
H&\displaystyle \binom{k-2q-2}{c-3}\\[3mm]
c+j,\quad2\le j\le q-2
 &\displaystyle q^2\binom{k-2q-2}{c-j-2}\\[3mm]
r
 &\displaystyle q^2\binom{k-2q-2}{c-q-1}.
\end{array}                                                     \tag{3.2}
\]

#### Proof

For `P`, the two required sets have total size two and the two forbidden
sets total size `2q`.  For `H`, the totals are four and `2q-2`.  For one
pair of cyclic `j`-intervals they are `2j+2` and `2q-2j`; there are `q^2`
ordered interval pairs.  For one pair of owners they are `2q` and two;
there are again `q^2` pairs.  Substitute these four rows into (2.2).
\(\square\)

The last row explains the change between the finite `k=17` boundary and
the asymptotic regime: it vanishes when `c<q+1`, but is positive once the
core is much wider than the tag cycle.

## 4. Intact singleton frames cannot be packed asymptotically

### Theorem 4.1 (owner-clique theorem)

Assume (0.1).  Every two singleton-base fixed-core frames share a rank-`r`
owner.  Consequently no two intact frames are resource-disjoint.

#### Proof

Write the two tag sets as `V,V'` and put `I=V cap V'`.

If `I` is nonempty, choose `x in I` and omit `x` from both owner facets.
The two partial assignments agree on the tag overlap.  Neither base marker
can equal `x`, because each marker lies outside its own tag set.  Thus the
two owner cylinders are compatible.

If `I` is empty, choose an omitted tag in `V` different from the other
frame's marker if that marker lies in `V`, and symmetrically in `V'`.
This is possible because `q>=2`.  Again the assignments are compatible.

In either case the union `U` of required coordinates has size at most
`2q`, while the union `Z` of the two omitted-tag sets has size at most two.
Therefore

\[
             0\le r-|U|\le k-|U|-|Z|
\]

by (0.1).  The owner entry (2.2) is positive. \(\square\)

Canonically `q=Theta(sqrt(r))`, so (0.1) holds for every sufficiently
large `k`.  Hence the proposed packing of `Theta(2^q/q^2)` **whole**
singleton-base frames is not merely unproved; it is false.

This does not contradict the simplicity theorem inside one frame.  The
fixed-base invariant separates different `X` values only while `D,V` are
fixed.  Once the partial assignment itself changes, the large Boolean
cylinders overlap.

## 5. Exact `k=17` specialization

Now impose (0.2).  A singleton frame has `G` of size eleven and uses all
four-subsets `X` of `G`, proving (0.3).  Its complete ledger is

\[
\begin{array}{c|ccccc}
\text{rank}&5&6&7&8&9\\ \hline
\text{resources}&330&330&1650&1650&1650.
\end{array}                                                     \tag{5.1}
\]

The total named deck has `5610=330(5^2-2\cdot5+2)` resources.

There is an exact characterization of when two such frames avoid owner
collisions.  Put

\[
 b=|V\cap V'|,\quad
 \epsilon={\bf1}_{\{d\in V'\}},\quad
 \epsilon'={\bf1}_{\{d'\in V\}},\quad
 m=|\{d,d'\}|,
\]

and

\[
                         s_0=10-b+m-\epsilon-\epsilon'.        \tag{5.2}
\]

### Proposition 5.1 (exact owner intersection at `k=17`)

The number of common owners is

\[
 \boxed{
 b\binom{17-s_0}{10-s_0}
 +(5-b-\epsilon)(5-b-\epsilon')
       \binom{17-s_0}{11-s_0}.}                               \tag{5.3}
\]

It is zero if and only if

\[
 V\cap V'=\varnothing,\qquad d\ne d',\qquad
 d\notin V',\qquad d'\notin V.                              \tag{5.4}
\]

#### Proof

Compatible owner omissions have exactly two forms.

* A common omitted point in `V cap V'`.  There are `b` choices; required
  union size is `s_0-1`, and the forbidden union has size one.
* Two omitted points outside the intersection.  They must avoid the two
  cross-markers, giving
  `(5-b-epsilon)(5-b-epsilon')` choices; required union size is `s_0-2`,
  and the forbidden union has size two.

The two corresponding instances of (2.2) are exactly (5.3).

If `b=0`, the second binomial is positive unless
`s_0=12`, which is precisely (5.4).  If `b>=1`, then `s_0<=11`.  For
`s_0<=10` the first term is positive; the only remaining case is
`b=1,s_0=11`, when the second term is positive.  This proves the zero
characterization. \(\square\)

Under (5.4) the two six-coordinate supports are disjoint, so Corollary 3.1
gives (0.4) immediately:

\[
\begin{aligned}
 |P\cap P'|&=\binom53=10,\\
 |H\cap H'|&=\binom52=10,\\
 |T_7\cap T'_7|&=25\binom51=125,\\
 |T_8\cap T'_8|&=25\binom50=25,\\
 |O\cap O'|&=25\binom5{-1}=0.
\end{aligned}                                                  \tag{5.5}
\]

### Corollary 5.2 (no two intact `k=17` reservoirs)

No two singleton-base `330`-module frames at `k=17` have disjoint complete
named decks.

If their owner decks meet, this is immediate.  Otherwise (5.4)--(5.5)
give `170` common named targets.  The ten common primitive-`P` targets lie
in ten different modules on each side, so they form a ten-edge matching in
the bipartite module-conflict graph.  Consequently even in the
owner-disjoint case at least ten modules must be discarded before the two
frames can coexist; this lower bound ignores the additional `H`, rank-7
and rank-8 collisions.

## 6. The exact surviving extraction problem

Let `mathcal R_i` be candidate frames and let `mathcal X_i` be a selected
subfamily of their module indices.  A proof at the desired scale must find

\[
 \sum_i|{\cal X}_i|=\Theta(W/q^2)                              \tag{6.1}
\]

such that every pair of selected modules has zero collision in all tensor
rows (2.2).  Equivalently, it is a matching in the resource hypergraph
obtained by **expanding** each frame edge into its individual module edges.

The scalar/fractional side has ample room.  At total mass `W/q^2`, uniform
symmetry gives owner and high-target load of order `1/q`, and low-target
load of order `1/q^2`.  Thus the obstruction exposed here is not a
fractional capacity cut.  It is the integral correlation among the
`Theta(q^2)` named resources carried by one module.

Theorems 2.1 and 4.1 rule out two tempting shortcuts:

1. selecting `Theta(2^q/q^2)` intact frames; and
2. applying a whole-frame matching theorem after treating internal frame
   simplicity as if it implied inter-frame sparsity.

A valid positive theorem must instead do one of the following.

* **Cylinder transversal:** choose proper `mathcal X_i` jointly so that
  all partial-assignment cylinders are hit at most once.
* **Collision clustering:** arrange that all inter-frame collisions are
  supported on a small, explicitly discardable subfamily of module
  indices.
* **Algebraic ownership:** assign each named resource to one of the many
  frames containing it, while retaining all resources of each accepted
  module together.

No full-scale rounding theorem is proved here.  The next section gives one
nontrivial exact partial extraction at `k=17`, and Section 8 records a sharp
ceiling for the most immediate marker-signature clustering idea.

## 7. A clean two-frame extraction at `k=17`

Take two singleton frames with disjoint six-coordinate supports

\[
 A=\{d\}\dot\cup V,\qquad
 A'=\{d'\}\dot\cup V',\qquad
 H=[17]-(A\cup A'),\quad |H|=5.                              \tag{7.1}
\]

Fix the tags `w,h in V` and `w',h' in V'`.  Let
`Int_j(sigma')` be the five cyclic `j`-intervals in the second frame.  In
the first frame define the following four disjoint families of module
indices:

\[
\begin{aligned}
 {\cal B}_P&=\{\{w'\}\cup Y:Y\in\tbinom H3\},\\
 {\cal B}_H&=\{\{d',h'\}\cup Y:Y\in\tbinom H2\},\\
 {\cal B}_7&=\{\{d'\}\cup J\cup\{y\}:
                  J\in\operatorname {Int}_2(\sigma'),\ y\in H\},\\
 {\cal B}_8&=\{\{d'\}\cup J:
                  J\in\operatorname {Int}_3(\sigma')\}.
\end{aligned}                                                 \tag{7.2}
\]

Their sizes are respectively

\[
                         10,\quad10,\quad25,\quad5.           \tag{7.3}
\]

They are disjoint because their members have respectively the following
`(d', |X cap V'|, |X cap H|)` profiles:

\[
          (0,1,3),\quad(1,1,2),\quad(1,2,1),\quad(1,3,0).     \tag{7.4}
\]

### Theorem 7.1 (exact two-frame optimum)

Every module of the first frame which shares any named resource with the
second frame has its index in

\[
                         {\cal B}={\cal B}_P\dot\cup
                         {\cal B}_H\dot\cup
                         {\cal B}_7\dot\cup{\cal B}_8.       \tag{7.5}
\]

Consequently, deleting these exactly `50` modules from the first frame and
retaining all `330` modules of the second gives `610` pairwise
owner/target-disjoint modules.  This is optimal: every collision-free
subfamily of the two frames has size at most `610`.

#### Proof

The support-disjoint tensor calculation in (5.5) also identifies the first
frame's module endpoint of every collision.

* A common `P` target is `w+w'+Y`, `Y in binom(H,3)`, so its first-frame
  index is `w'+Y`.
* A common `H` target is `d+h+d'+h'+Y`, `Y in binom(H,2)`, so its index is
  `d'+h'+Y`.
* A common rank-7 target is `d+J_2+d'+J'_2+y`; its first-frame index is
  `d'+J'_2+y`.
* A common rank-8 target is `d+J_3+d'+J'_3`; its first-frame index is
  `d'+J'_3`.
* There are no common owners.

These are precisely the four rows in (7.2).  Conversely every displayed
index occurs in the corresponding collision row, so (7.5) is exact.
After deleting `mathcal B`, no cross-frame common resource remains.  Each
individual frame was already simple, proving the `280+330=610` extraction.

For optimality, construct fifty pairwise vertex-disjoint conflict edges.
Match the two `P` layers by

\[
             \{w'\}\cup Y\longleftrightarrow\{w\}\cup Y,
             \qquad Y\in\tbinom H3,
\]

and the two `H` layers by

\[
       \{d',h'\}\cup Y\longleftrightarrow\{d,h\}\cup Y,
       \qquad Y\in\tbinom H2.
\]

Choose arbitrary bijections between the five cyclic 2-intervals of the two
orders and between their five cyclic 3-intervals.  Pair the rank-7 layers
using the first bijection and the same `y in H`, and pair the rank-8 layers
using the second.  The endpoints in all four rows are distinct by (7.4),
and every paired endpoint shares the evident union target.  This is a
matching of size `10+10+25+5=50` in the bipartite module-conflict graph.

The set `mathcal B` is a vertex cover of size fifty, while this matching has
size fifty.  By Koenig's theorem the minimum deletion number is exactly
fifty, and the maximum independent union has size `660-50=610`.
\(\square\)

This is a genuine gain over one `330`-module reservoir, but it is still
below `ceil(W/q^2)=973`.  It also displays the desired kind of collision
clustering: the `170` common resources from (5.5) are supported on only
`50` module indices on either side.

In particular, three singleton frames can contribute `973` modules only if
their three six-coordinate supports are pairwise intersecting.  A disjoint
support pair already caps those two frames at `610`; even adding all `330`
modules of the third gives at most `940`.

The same argument has an exact all-parameter form for two disjoint
singleton supports.  Put

\[
                         n_0=k-2q-2.
\]

The first-frame bad indices lie in

\[
\begin{aligned}
 &\{w'\}\cup\tbinom H{c-2},\\
 &\{d',h'\}\cup\tbinom H{c-3},\\
 &\{d'\}\cup\operatorname {Int}_j(\sigma')
      \cup\tbinom H{c-j-2},\quad2\le j\le q-2,\\
 &\{d'\}\cup\{V'-v:v\in V'\}
      \cup\tbinom H{c-q-1},
\end{aligned}                                                 \tag{7.6}
\]

where `|H|=n_0`; incompatible binomial layers are empty.  The layers are
disjoint by their `(d',V',H)` profile, and hence their exact total is

\[
 B_\perp=\binom{n_0}{c-2}+\binom{n_0}{c-3}
   +q\sum_{j=2}^{q-2}\binom{n_0}{c-j-2}
   +q\binom{n_0}{c-q-1}.                                    \tag{7.7}
\]

Thus two disjoint-support frames always yield the constructive extraction

\[
                         2M_1-B_\perp.                        \tag{7.8}
\]

At `k=17`, (7.7) is `10+10+25+5+0=50`.

## 8. Persistent marker signatures have a one-frame ceiling

The natural next attempt is to place a common marker bank `M` inside every
frame reservoir and assign different marker signatures to different
frames.  The following observation shows the exact limit of that method.

Fix `M subseteq G_i` for every participating singleton frame, with
`|M|=m`, and let `a_0=c-1` be the module-core size.  For frame `i`, suppose
we retain only a family `mathcal X_i` whose exact marker traces

\[
                         {\cal T}_i=\{X\cap M:X\in{\cal X}_i\} \tag{8.1}
\]

are disjoint from the trace families assigned to every other frame.  This
condition is sufficient to separate every named resource, since the
persistent intersection of every resource with `M` is `X cap M`.

### Proposition 8.1 (Vandermonde marker ceiling)

Under the exact-trace separation above,

\[
                         \sum_i|{\cal X}_i|
                         \le\binom{k-q-1}{c-1}=M_1.           \tag{8.2}
\]

The same bound holds for containment signatures `S_i subseteq X` whenever
the corresponding upper shadows in `binom(M,<=a_0)` are pairwise disjoint.

#### Proof

For one exact trace `T subseteq M`, `|T|=t`, there are at most

\[
                         \binom{k-q-1-m}{a_0-t}               \tag{8.3}
\]

module indices with `X cap M=T`.  Since the trace families are disjoint,
summing (8.3) over all assigned traces is at most the sum over every trace:

\[
 \sum_{t=0}^{a_0}\binom mt
      \binom{k-q-1-m}{a_0-t}
 =\binom{k-q-1}{a_0}                                        \tag{8.4}
\]

by Vandermonde's identity.  This is (8.2).  A containment-signature scheme
with disjoint upper shadows assigns each exact trace to at most one frame,
so it is the same argument. \(\square\)

At `k=17`, (8.2) is `330` regardless of the number or size of the marker
signatures.  Thus private persistent-marker bits alone cannot even improve
on one reservoir.  The `610` construction in Theorem 7.1 succeeds because
it uses the full row-dependent collision geometry, not a universal marker
partition.

The next finite positive target is consequently narrower: find three or four
frames whose row-dependent bad-index families analogous to (7.6) have a
small transversal, or prove a correlated random/algebraic choice for which
the union of those bad families is `o(M_1)` per new frame.  Merely adding
more persistent signatures cannot do this.

## 9. Random clustered pruning reaches `Theta(W/q^2)` modules

This section returns to the canonical asymptotic regime and uses only
singleton-base frames.  Put

\[
 Q=q+1,\qquad n=k-Q=k-q-1,\qquad a_0=c-1=r-q,
 \qquad M_1=\binom n{a_0}.                                  \tag{9.1}
\]

A frame support is

\[
                         A=\{\beta\}\dot\cup V,\qquad |A|=Q. \tag{9.2}
\]

Choose a support uniformly from `binom([k],Q)`, choose its base point,
cyclic order and low tags by any symmetric rule, and include the full
`M_1`-module reservoir before pruning.

For two frames `mathcal R,mathcal R'`, let

\[
 B({\cal R},{\cal R}')
 =\#\{X\in\tbinom{[k]-A}{a_0}:
       \text{module }X\text{ shares a named resource with }{\cal R}'\}.
                                                                    \tag{9.3}
\]

### Lemma 9.1 (one other frame fixes only `O(q^2)` core traces)

Let `A,A'` be the two supports and put

\[
                         E=A'-A,\qquad b=|E|.                 \tag{9.4}
\]

For each occurrence cylinder `(R',F')` of the second frame, every
first-frame module which collides with that cylinder satisfies the single
exact trace equation

\[
                         X\cap E=R'\cap E.                    \tag{9.5}
\]

There are exactly

\[
                         L=q^2-2q+2                           \tag{9.6}
\]

occurrence cylinders in one named deck.  Consequently

\[
 B({\cal R},{\cal R}')
 \le \sum_{\rho'}
       \binom{n-b}{a_0-|R'_{\rho'}\cap E|}.                  \tag{9.7}
\]

#### Proof

Every resource of a singleton-base module has intersection with the
complement of its own support `A` exactly equal to its module index `X`.
If it belongs to the second-frame cylinder `Q_s(R',F')`, its intersection
with `A'` must be exactly `R'`.  Restricting to `E=A'-A subseteq [k]-A`
gives (9.5), independently of which same-rank occurrence of the first
module supplied the collision.

The deck has one `P`, one `H`, `q` cylinders at each of the `q-3` high
target ranks, and `q` owner cylinders.  This is (9.6).  For a fixed trace
of size `p`, exactly `binom(n-b,a_0-p)` module indices realize it.  Union
bounding over the second-frame cylinders proves (9.7). \(\square\)

The crucial saving is visible in (9.5): the `q` possible starts in the
first module do **not** introduce another factor `q`.  Once a second-frame
occurrence is fixed, all first-frame starts demand the same trace on the
other-only support.  This is the general version of the `170` resources on
only `50` bad indices in Section 7.

### Lemma 9.2 (uniform trace probability)

There is an absolute constant `C_0` such that, for every sufficiently large
canonical `k`, every `B subseteq [n]` of size `b<=Q`, and every `P subseteq
B`,

\[
 {\binom{n-b}{a_0-|P|}\over\binom n{a_0}}
 \le C_0\,2^{-b}.                                          \tag{9.8}
\]

#### Proof

The left side is the probability that a uniformly random `a_0`-subset has
the prescribed `0/1` trace `P` on `B`.  Writing `p=|P|`, it is

\[
                         {(a_0)_p(n-a_0)_{b-p}\over(n)_b}.    \tag{9.9}
\]

Hence it is at most

\[
 \left({\max(a_0,n-a_0)\over n-b+1}\right)^b
 =2^{-b}
   \left({2\max(a_0,n-a_0)\over n-b+1}\right)^b.             \tag{9.10}
\]

Here `a_0=r-q`, `n=k-q-1`, and `b<=q+1`.  The logarithm of the last factor
is `O(q^2/r)`, uniformly in `b`.  The canonical relation
`q^2/r=O(1)` therefore bounds it by one absolute constant. \(\square\)

### Lemma 9.3 (bounded exponential overlap moment)

For two independent uniform `Q`-subsets `A,A'` of `[k]`, if
`S=|A cap A'|`, then

\[
                         \mathbb E\,2^S\le
 \exp\left({Q^2\over k-Q+1}\right)=O(1).                    \tag{9.11}
\]

#### Proof

Expand `2^S` as the number of subsets of `A cap A'`.  For a fixed
`t`-subset of `A`, the probability that it lies in `A'` is
`(Q)_t/(k)_t`.  Therefore

\[
 \mathbb E\,2^S
 =\sum_{t=0}^Q\binom Qt{(Q)_t\over(k)_t}
 \le\sum_{t\ge0}{1\over t!}
       \left({Q^2\over k-Q+1}\right)^t,                     \tag{9.12}
\]

which is (9.11).  Canonically `Q^2/k=O(1)`. \(\square\)

### Proposition 9.4 (mean pair damage)

For two independent random singleton-base frames,

\[
 \boxed{\mathbb E\,B({\cal R},{\cal R}')
          \le C_1 M_1{q^2\over2^q}}                          \tag{9.13}
\]

for an absolute constant `C_1` and all sufficiently large canonical `k`.

#### Proof

Condition on the supports.  With `S=|A cap A'|`, equation (9.4) gives
`b=Q-S`.  Lemmas 9.1 and 9.2 imply

\[
 B({\cal R},{\cal R}')
 \le C_0 L M_1 2^{-Q+S}.                                    \tag{9.14}
\]

Average and use Lemma 9.3, `L<=q^2`, and `Q=q+1`. \(\square\)

### Theorem 9.5 (clustered-pruning extraction theorem)

For every sufficiently large canonical `k`, the facet module atlas
contains

\[
                         \Omega(W/q^2)                        \tag{9.15}
\]

pairwise owner- and named-target-disjoint, fully named-deck-labelled length-`q`
modules.

#### Proof

Choose independently

\[
                         R=\left\lfloor
                         {2^q\over4C_1q^2}\right\rfloor      \tag{9.16}
\]

singleton-base frames.  Initially they contain `RM_1` module occurrences.
Call a module occurrence bad if it shares any named resource with any
module in another sampled frame, and delete every bad occurrence.

The number of bad occurrences is at most

\[
                         \sum_{i\ne j}B({\cal R}_i,{\cal R}_j). \tag{9.17}
\]

By Proposition 9.4 and (9.16), its expectation is at most `RM_1/4`.
Therefore some choice of frames leaves at least `3RM_1/4` good modules.
Every two surviving modules are resource-disjoint by the definition of
badness, and modules inside one frame were already resource-simple.

Finally the sharp frame asymptotic gives

\[
                         M_1\sim2^{-(q+1)}e^{-\pi/16}W.
\]

Substitution into (9.16) yields

\[
                         {3\over4}RM_1=\Omega(W/q^2),
\]

proving (9.15). \(\square\)

The proof is deliberately conservative: it deletes a module even if its
collision partner will also be deleted, and it uses only a first moment.
Its importance is qualitative.  The formerly missing factor `q` is gained
because a whole second-frame occurrence fixes one core trace and clusters
the `q` first-frame starts.

Theorem 9.5 closes the owner/named-target **order-of-magnitude** packing
gate.  It does not yet give an arbitrary prescribed leading constant, avoid
a protected bank, bind the selected modules to the exact primitive and
short-buffer occurrence inventory, serialize their source cycles, fuse
components, or preserve the remaining upper/residence/compiler interfaces.
Those rows remain separate.

### 9.6 Proof-scope audit

For clarity, the five possible hidden steps in Theorem 9.5 are as follows.

1. **Every named row has the same outside trace.**  For a singleton frame
   `A={beta} dotcup V`, the `P`, `H`, interval and owner resources are
   respectively

   \[
   X+w,\quad \beta+X+h,\quad \beta+X+J,
       \quad \beta+X+(V-v).
   \]

   Their intersection with `[k]-A` is always exactly `X`.  In the second
   frame, every occurrence has `R' dotcup F'=A'`.  Thus membership means
   `S cap A'=R'`, and restriction to `E=A'-A` proves (9.5) for `P`, `H`,
   every rank `c+j` (`2<=j<=q-2`), and the owner rank `r`.  Cross-rank
   collisions are irrelevant because named resources of different ranks
   are different species.

2. **The trace constant is uniform.**  In even dimension,

   \[
   {2\max(a_0,n-a_0)\over n-b+1}
   \le {2(r-1)\over2r-2q-1};
   \]

   in odd dimension it is at most

   \[
   {2(r-2)\over2r-2q-2}.
   \]

   Raising either expression to `b<=q+1` gives
   `exp(O(q^2/r))=O(1)`.  Hence `C_0` in (9.8) is independent of the
   supports, their overlap, the prescribed trace and the row label.

3. **The overlap moment is exact before bounding.**  Conditional on `A`,

   \[
   \mathbb E\,2^{|A\cap A'|}
    =\sum_{t=0}^{Q}\binom Qt{(Q)_t\over(k)_t},
   \]

   because both sides count pairs `(T,A')` with `T subseteq A cap A'`.
   Inequality (9.12) is therefore a direct termwise bound, not an
   independence approximation.

4. **Multiple collisions are overcounted safely.**  A module bad against
   several frames is counted several times in (9.17), so (9.17) is an upper
   bound.  After every bad occurrence is deleted, two survivors from
   different sampled frames cannot share a resource; otherwise both would
   have been declared bad.  Duplicate sampled frames and duplicate module
   occurrences are covered by the same rule.  Internal simplicity handles
   two survivors from one frame.

5. **Exact exclusions.**  The edge packed in Theorem 9.5 consists only of
   the `q` owners, one target at ranks `c,c+1`, and `q` targets at every rank
   `c+2,...,r-1`.  It does not contain or allocate primitive-source
   occurrences, the `d` short `H` buffers, physical positions, component
   links, arbitrary exterior upper witnesses, global coordinate residence,
   protected interfaces, or compiler/common-cap incidences.  No conclusion
   about those resources, chronology, topology, or `nu(k)` follows from
   Theorem 9.5 alone.

## 10. Dependencies

The internal fixed-base amplifier and its sharp asymptotics are in
`MATH_THEOREM_FACET_CODIMENSION_ONE_MARKER_FRAME_AMPLIFIER_20260802.md`.
The literal named deck and corrected primitive/buffer ledger are in
`MATH_THEOREM_FACET_MODULE_LEDGER_AND_WEIGHTED_JOINT_GREEDY_SPREAD_20260802.md`.
The independent low-label Hall boundary is in
`MATH_THEOREM_FACET_LOW_RANK_HALL_MULTIPLICITY_AND_AFFINE_LINE_COUNTEREXAMPLE_20260802.md`.
