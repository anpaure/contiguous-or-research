# The minimal cross-sector rectangle carrier, its tensor capacity, and the surviving full-family obstruction

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

There is a genuine non-product escape from the unique-carrier lemma for the
octahedral `Q_3` mosaics.  It already occurs on six active coordinates.
After suppressing a fixed core, put

\[
 P=\{t,e\},\qquad A=\{a,b,c,d\},
\]

and let

\[
 \Omega=P\times A
 =\{\{x,y\}:x\in P,\ y\in A\}.
\tag{0.1}
\]

Every perfect matching `M` of the four-set `A` partitions `Omega` into two
physical isometric squares

\[
 \mathcal F_M=\{Q(P,E):E\in M\}.                 \tag{0.2}
\]

The three choices

\[
 ab\mid cd,\qquad ac\mid bd,\qquad ad\mid bc       \tag{0.3}
\]

are therefore three exact two-cycle factors on the same eight owners.
Any two form a connected two-for-two owner trade.  In every shore the two
cycles both carry each of the lower targets `t` and `e`.  Thus local target
ownership is genuinely nonunique *inside one coefficient-one factor*.

This packet is minimal in the following exact senses.

1. A proper lower target occurs at most once in one isometric maximal cube
   cycle.  Hence two simultaneous carriers require at least two cycles.
2. Two vertex-disjoint isometric squares carrying the same depth-one target
   require at least six active coordinates.  The construction above uses
   six coordinates and eight owners, attaining both lower bounds.

The packet is genuinely cross-sector.  Put `a,b` in one macroblock `A_0`,
`c,d` in another macroblock `A_1`, and `t,e` in a third macroblock.  Relative
to the target profile `ell`, the cycles `Q(P,ab)` and `Q(P,cd)` lie in the two
different source profiles

\[
                 k^{(0)}=\ell+\mathbf e_{A_0},\qquad
                 k^{(1)}=\ell+\mathbf e_{A_1}.       \tag{0.4}
\]

Both entries `F_(k^(j),ell)` of the explicit macroprofile flow are positive.
The switched shore uses the cross-block pairs `ac|bd` and hence mixes the two
source profiles inside each cycle.  This is precisely the phenomenon omitted
by a sectorwise product-cell model.

On the carrier/profile incidence, the two shores are exactly

\[
                         2I_2\longleftrightarrow J_2.  \tag{0.4a}
\]

After normalization the crossed shore is `J_2/2`, so tensoring `q` copies
annihilates every nonconstant Walsh mode of the `2^q` predecessor-profile
cube.  On the corresponding fine target family, the restriction of the
macroprofile inclusion flow has exact load

\[
                         \lambda_{r,q}^{\rm rect}
 =\frac{4^q}{\binom rq}.                              \tag{0.4b}
\]

Hence it has genuine target-saturating fractional capacity whenever
`binom(r,q)<=4^q`; at `r=2q` the surplus is
`(1+o(1))sqrt(pi q)`.

Tensoring `r` copies yields `2^r` disjoint cells `Q_(2r)`.  A target using a
letter of `{t_i,e_i}` in each of `s` touched blocks has `2^s` simultaneous
carrier cells.  In particular, at depth `r` there are `2^r` targets, each
with `2^r` disjoint carrier `r`-faces.  If `r` is a power of two, the cells
can be resolved into isometric `C_(4r)`'s so that every one of these targets
occurs exactly

\[
                         \boxed{\frac{4^r}{2r}}       \tag{0.5}
\]

times as a consecutive depth-`r` lower window.  This is an exact positive
capacity theorem, not only a face-support statement.

There is nevertheless a sharp limitation.  Let the natural fine family at
depth `q` allow any of the six singleton labels in every touched block and
any of the eight packet owners in every untouched block.  Its size is

\[
                \binom rq6^q8^{r-q}.                 \tag{0.6}
\]

For any choice of one common cyclic direction order in each of the `2^r`
cells, even before Hamming phase restrictions, the reachable fraction is at
most

\[
 \boxed{
   \min\left\{1,
       \frac{2r}{\binom rq}\left(\frac23\right)^q
   \right\}.}                                         \tag{0.7}
\]

Consequently, for `q=A sqrt(m)+O(1)` and `q<=r<=m/4`, the rectangle tensor
reaches only

\[
 \exp\{-A\log(3/2)\sqrt m+O(\log m)\}=o(1)            \tag{0.8}
\]

of this fine family.  The all-doubled subbank avoids the consecutive-window
obstruction, but it is exactly a `3^(-q)` fraction of the six-label touched
family.  Thus the rectangle is the smallest genuine cross-sector carrier
primitive, while its naive tensor is not a coefficient-one global closure.

Finally, every exact owner trade, including packets that cross macroprofiles,
obeys the all-depth coordinate-star conservation law

\[
 \boxed{A^-_{q,x}+A^+_{q,x}=2N_x.}                   \tag{0.9}
\]

Here `N_x` is the number of middle owners in the common support containing
coordinate `x`, while `A^-_(q,x)` and `A^+_(q,x)` count depth-`q` lower and
upper window occurrences containing `x`.  On the full middle layer,
`N_x=W/2`, so the right side is `W`.  Therefore every lower coordinate-star
change of an owner trade forces the opposite upper change at the same depth.

## 1. The six-coordinate rectangle trade

Let `R` be an arbitrary fixed set disjoint from

\[
                         \{t,e,a,b,c,d\}.             \tag{1.1}
\]

For disjoint two-sets `P={t,e}` and `E={x,y}`, define

\[
 Q_R(P,E)
 =\{R\cup\{p,z\}:p\in P,\ z\in E\}.                 \tag{1.2}
\]

The four vertices in (1.2) have common rank `|R|+2`.  In cyclic order

\[
 Rtx,\ Rty,\ Rey,\ Rex,                               \tag{1.3}
\]

their transition directions are `E,P,E,P`.  Thus (1.2) is a literal
isometric `C_4`, or equivalently a physical `Q_2` cell.

Put

\[
 \Omega_R=\{R\cup\{p,z\}:p\in P,\ z\in A\}.          \tag{1.4}
\]

It has eight vertices.  If `M` is any perfect matching of `A`, then

\[
 \mathcal F_M=\{Q_R(P,E):E\in M\}                     \tag{1.5}
\]

is a two-cycle partition of `Omega_R`.

### Theorem 1.1 (exact three-shore associator)

The three matchings in (0.3) give three exact factors on the same support.
The ownership overlap of any two distinct shores is `K_(2,2)`, with every
nonempty owner intersection of size two.  In particular every two-shore
trade is connected.

#### Proof

Two distinct perfect matchings of a four-set share no edge.  Every edge of
one matching meets every edge of the other matching in exactly one letter.
Consequently

\[
 Q_R(P,E)\cap Q_R(P,E')
 =\{R\cup\{p,z\}:p\in P\},                            \tag{1.6}
\]

where `z` is the unique element of `E intersect E'`.  This intersection has
two owners.  Thus all four left-right cycle pairs intersect, giving
`K_(2,2)`.  Both shores partition (1.4), so the replacement is an exact
owner trade.  QED.

### Proposition 1.2 (exact local carrier census)

For every shore `F_M`, the depth-one lower targets, with multiplicity, are

\[
 2[R\cup\{t\}]+2[R\cup\{e\}]
   +\sum_{z\in A}[R\cup\{z\}].                       \tag{1.7}
\]

Thus `R+t` and `R+e` each have two distinct owner-disjoint carrier cycles.

#### Proof

In `Q_R(P,E)`, the two edges in direction `E` have intersections `R+t` and
`R+e`.  The two edges in direction `P` have intersections `R+x` and `R+y`,
where `E={x,y}`.  Summing over the two edges of a perfect matching `M` gives
(1.7).  QED.

Notice that all three shores have the same depth-one lower multiset.  The
primitive creates carrier multiplicity and changes pair-frame chronology; it
does not by itself create a signed depth-one load correction.

## 2. Exact cross-sector alignment with `F_(k,ell)`

Take `|R|=m-2` and put

\[
                         T_t=R\cup\{t\}.              \tag{2.1}
\]

This has rank `m-1`, while every owner in `Omega_R` has rank `m`.  Partition
the ground coordinates into macroblocks so that

\[
 a,b\in B_0,\qquad c,d\in B_1,\qquad t,e\in B_2.      \tag{2.2}
\]

Let `ell=kappa(T_t)`.  Every owner in `Q_R(P,ab)` has profile
`k^(0)=ell+e_(B_0)`, because flipping either `P` or `ab` preserves every
macroblock count.  Likewise every owner in `Q_R(P,cd)` has profile
`k^(1)=ell+e_(B_1)`.

For the explicit flow

\[
 F_{k,\ell}
 =\frac{V_k}{\binom m1}\prod_j\binom{k_j}{\ell_j},   \tag{2.3}
\]

both values in (0.4) are strictly positive: the profiles satisfy
`ell<=k^(j)` and differ by one unit.  Proposition 1.2 therefore gives two
physical carriers of the same target, one in each of two allowed predecessor
rows of the macroprofile flow.

On the `ac|bd` shore, each square contains two owners of profile `k^(0)` and
two of profile `k^(1)`.  Its direction `ac` or `bd` crosses the macroblock
boundary.  The union retains four owners of each source profile, exactly as
the old shore does.  Hence the switch is an exact integral cross-sector
recoupling, not a relabelling of one fixed source sector.

## 2A. Exact heat-bath lift of the profile flow

Fix the lower target `T_t`.  Index the two carrier cycles on a shore by
rows and the two predecessor profiles `k^(0),k^(1)` by columns.  Count in
each row the middle extensions of `T_t` having the indicated profile.  On
the parallel shore `ab|cd` and the crossed shore `ac|bd`, respectively,
the matrices are

\[
                         B_{\parallel}=2I_2,
 \qquad                  B_{\times}=J_2.             \tag{2.4}
\]

Both have row and column sums two.  After row normalization, the crossed
shore is the exact heat bath

\[
 H=\frac12J_2,
 \qquad H(1,1)=(1,1),\quad H(1,-1)=0.                \tag{2.5}
\]

Thus the trade preserves the constant profile mass and annihilates the
only nonconstant profile mode in one step.

Tensor `q` touched copies.  Carrier faces and binary predecessor profiles
are both indexed by `F_2^q`.  The two extreme shores have incidence
matrices

\[
 B_{\parallel}^{(q)}=2^qI_{2^q},
 \qquad
 B_{\times}^{(q)}=J_{2^q},                            \tag{2.6}
\]

and the normalized crossed operator is

\[
                         H^{\otimes q}
 =2^{-q}J_{2^q}.                                      \tag{2.7}
\]

Consequently every crossed carrier face contains one extension in every
binary predecessor profile, whereas every parallel carrier face contains
all `2^q` of its extensions in one profile.  This is a literal integral
coupling of the same uniform predecessor marginal.

The relation with the explicit flow is exact, not analogical.  Conditional
on this target and on these four allowed extensions in each touched block,
the containment flags underlying

\[
 F_{k,\ell}=\frac{V_k}{\binom mq}\prod_j\binom{k_j}{\ell_j}
\]

give equal weight to all `4^q` middle extensions.  Each of the `2^q`
binary predecessor profiles contains `2^q` of them, hence has conditional
mass `2^{-q}`, exactly (2.7).

There is also a sharp fractional capacity ledger.  Let
`\mathcal U_{r,q}` be the fine family in which one chooses
`I in binom([r],q)`, uses either `t_i` or `e_i` in every touched block,
and uses an arbitrary packet owner in every untouched block.  Then

\[
 |\mathcal U_{r,q}|=\binom rq2^q8^{r-q}.              \tag{2.8}
\]

In the containment graph between `Omega_r` and `mathcal U_(r,q)`, every
middle owner has degree `binom(r,q)` and every target has degree `4^q`.
Indeed a source chooses the touched set, while a target independently
chooses any of four special extensions in every touched block.  The
identity

\[
 8^r\binom rq=|\mathcal U_{r,q}|\,4^q.             \tag{2.9}
\]

audits both degrees.

### Theorem 2A.1 (restricted cross-sector capacity)

The uniform source-normalized restriction of `F` has target load

\[
                         \lambda_{r,q}^{\rm rect}
 =\frac{4^q}{\binom rq}.                              \tag{2.10}
\]

If `binom(r,q)<=4^q`, assigning weight `4^{-q}` to every containment flag
gives a fractional matching which saturates every target of
`mathcal U_(r,q)` and uses at most unit capacity at every middle owner.
If `binom(r,q)>4^q`, any construction with at most one depth-`q` occurrence
per middle owner misses at least

\[
 |\mathcal U_{r,q}|
 \left(1-\frac{4^q}{\binom rq}\right)                \tag{2.11}
\]

targets.

#### Proof

Give every containment flag weight `1/binom(r,q)`.  The source sums are
one and the target sums are (2.10), by the biregular degrees above.
Alternatively, weight every flag by `4^{-q}`; target sums are one and
source sums are `binom(r,q)/4^q`, proving the positive assertion.
For the negative assertion, there are only `8^r` source occurrences and
`|mathcal U_(r,q)|` targets; (2.9) gives (2.11).  \(\square\)

In particular, for `r=2q`,

\[
 \lambda_{2q,q}^{\rm rect}
 =\frac{4^q}{\binom{2q}q}
 =\sqrt{\pi q}\,(1+o(1)).                            \tag{2.12}
\]

Thus the rectangle has genuine surplus fractional capacity at the
Gaussian scale when `r<=2q`.  Turning that capacity into simultaneous
cyclic windows is a separate ordering problem, treated sharply in
Section 6.

## 3. Minimality

### Lemma 3.1 (one proper target per isometric cycle)

Let `C` be an isometric `C_(2h)` in a constant-weight pair cube, with
`h>=2`, and let `1<=q<h`.  A fixed rank-`(m-q)` set is the lower intersection
of at most one directed length-`q` window of `C`, modulo the repeated
antipodal copy of the direction word.

For `q=1`, in particular, one lower target belongs to at most one edge of
`C`.

#### Proof

Write the active coordinate pairs as `P_1,...,P_h` and the transition word
as `pi pi`.  A lower target of a `q`-window excludes both endpoints of the
`q` active pairs in that interval and contains one endpoint of every other
active pair.  Two different proper cyclic intervals have different active
pair sets.  Choosing a pair in their symmetric difference, one purported
target would exclude both endpoints while the other contains one endpoint,
which is impossible.

The antipodal occurrence of the same interval uses the complementary
endpoint in every one of the `h-q>=1` inactive pairs, so its lower target is
different.  QED.

### Theorem 3.2 (six active coordinates and eight owners are minimal)

Suppose two vertex-disjoint isometric squares both carry the same depth-one
target `T`.  After removing coordinates frozen in every one of their eight
owners, at least six active coordinates remain.  At least eight owners and
two cycles are necessary.

#### Proof

An edge with lower intersection `T` has endpoints `T+a,T+b` for two
coordinates `a,b` outside `T`.  Vertex-disjoint carrier edges therefore use
four distinct outside coordinates, say `a,b,c,d`.

In the first square, its other active pair is `{t_1,u_1}` with
`t_1 in T` and `u_1 notin T`; its off-carrier vertices are

\[
 T-t_1+u_1+a,\qquad T-t_1+u_1+b.                    \tag{3.1}
\]

The second square has the analogous data `{t_2,u_2}` and off-carrier
vertices

\[
 T-t_2+u_2+c,\qquad T-t_2+u_2+d.                    \tag{3.2}
\]

If `t_1` and `t_2` are distinct, they are two active target coordinates;
together with the four carrier endpoints this already gives six active
coordinates.

If `t_1=t_2=t` and only the four carrier endpoints were available outside
`T`, then `u_1` lies in `{c,d}` and `u_2` lies in `{a,b}`.  The owner

\[
                         T-t+u_1+u_2                 \tag{3.3}
\]

would occur in both squares, contrary to vertex-disjointness.  Thus a fifth
outside coordinate is required, and with `t` there are again at least six
active coordinates.

Lemma 3.1 forces two distinct cycles.  A square has four owners, so eight
owners are necessary.  The construction of Section 1 uses exactly six
active coordinates, two cycles, and eight owners.  QED.

## 4. Tensor carrier multiplicity

Take `r` disjoint labelled copies

\[
 P_i=\{t_i,e_i\},\qquad A_i=\{a_i,b_i,c_i,d_i\},      \tag{4.1}
\]

and use the matching

\[
                         M_i=\{a_ib_i,c_id_i\}.        \tag{4.2}
\]

Adjoin a fixed outside core `R_0` of size `m-2r`.  The owner support is

\[
 \Omega_r=
 \left\{R_0\cup\bigcup_{i=1}^r\{x_i,y_i\}:
        x_i\in P_i,\ y_i\in A_i\right\}.             \tag{4.3}
\]

It has `8^r` middle owners.  For every
`epsilon in {0,1}^r`, let `E_i^0=a_ib_i`, `E_i^1=c_id_i` and put

\[
 \mathcal Q_\epsilon
 =\left\{R_0\cup\bigcup_i\{x_i,y_i\}:
          x_i\in P_i,\ y_i\in E_i^{\epsilon_i}\right\}.
\tag{4.4}
\]

The `2^r` sets in (4.4) partition `Omega_r`, and each is a literal
`Q_(2r)`.

### Theorem 4.1 (exact carrier-face bank)

For every `x=(x_1,...,x_r) in product_i P_i`, set

\[
                         T_x=R_0\cup\{x_1,\ldots,x_r\}. \tag{4.5}
\]

Then `T_x` has one carrier `r`-face in every cell `Q_epsilon`.  These
`2^r` carrier faces are pairwise owner-disjoint.  For fixed `x` their union
has `4^r` owners, and as `x` varies the resulting face banks partition all
`8^r` owners.

#### Proof

In `Q_epsilon`, fix the orientation of every shared direction `P_i` to
`x_i` and vary all private directions `E_i^(epsilon_i)`.  The intersection
of this affine `r`-face is exactly (4.5).  Different cells are disjoint.
There are `2^r` cells and every face has `2^r` vertices, giving `4^r`
owners for fixed `x`.  There are `2^r` choices of `x`, and every owner in
(4.3) has a unique shared orientation `x`; hence the banks partition
`Omega_r`.  QED.

More generally, at depth `q`, a fine target touched in `I subseteq[r]`
has two carrier-cell choices in block `i` precisely when its local singleton
is `t_i` or `e_i`.  Every other touched singleton and every untouched local
owner fixes the cell choice.  Thus if `s` touched singleton labels lie in
the shared pairs, the exact number of carrier cells is

\[
                              \boxed{2^s}.             \tag{4.6}
\]

This is the discrete predecessor cube supplied by the two macroprofile rows
in (0.4).

## 5. Exact long-cycle realization at the diagonal depth

Assume `r` is a power of two.  Then `h=2r` is a power of two, so every cell
`Q_epsilon` has a vertex resolution into isometric `C_(4r)`'s with any
prescribed common direction order.  Put its private directions first and
its shared directions second:

\[
 d_1^\epsilon,\ldots,d_r^\epsilon,
 p_1,\ldots,p_r.                                      \tag{5.1}
\]

Fix one such resolution `H` of the abstract `Q_(2r)`.  For an orientation
`y in F_2^r` of the shared directions, let `n_H(y)` be the number of
depth-`r` windows in `H` whose direction block is the first block in (5.1)
and whose lower target has shared orientation `y`.  Every cycle has two
such antipodal windows, and there are `4^r/(4r)` cycles.  Therefore

\[
                  \sum_y n_H(y)=\frac{4^r}{2r}.       \tag{5.2}
\]

Translate the resolution used in cell `Q_epsilon` in its shared directions
by the vector `epsilon`.  Translation preserves the cell, isometry, and
vertex resolution.  For a fixed physical target orientation `x`, its total
number of windows over all cells is

\[
 \sum_{\epsilon\in F_2^r}n_H(x+\epsilon)
 =\sum_{y\in F_2^r}n_H(y)
 =\frac{4^r}{2r}.                                     \tag{5.3}
\]

This proves (0.5).  The total occurrence audit is

\[
 2^r\cdot\frac{4^r}{4r}\cdot2
 =\frac{8^r}{2r}
 =2^r\cdot\frac{4^r}{2r}.                            \tag{5.4}
\]

The left side counts two distinguished windows per long cycle; the right
side counts the `2^r` targets using (5.3).

## 6. The full six-label fine family and the sharp capacity bound

Fix `I in binom([r],q)`.  In a touched block `i in I`, allow an arbitrary
singleton

\[
 z_i\in\{t_i,e_i,a_i,b_i,c_i,d_i\}.                  \tag{6.1}
\]

In an untouched block, allow any packet owner

\[
                         \{x_i,y_i\},\qquad
 x_i\in P_i,\ y_i\in A_i.                            \tag{6.2}
\]

Together with `R_0`, these are rank-`(m-q)` targets.  Summing over `I`
gives the family `T_(r,q)` of cardinality (0.6).

Inside one cell `Q_epsilon`, a touched singleton has the following forced
carrier direction.

* `t_i` or `e_i` forces the private direction `d_i^epsilon`.
* An endpoint of `E_i^(epsilon_i)` forces the shared direction `p_i`.
* An endpoint of the other private pair is incompatible with the cell.

Thus a usable `q`-window is block-simple: it selects exactly one of the two
directions in each of `q` blocks.

Fix one block-simple direction set in a cell.  It carries exactly two local
singleton choices in every touched block.  In every untouched block, the
target may be any of the four vertices of that cell.  Hence one such
direction set carries exactly

\[
                         2^q4^{r-q}                   \tag{6.3}
\]

members of `T_(r,q)`.

One cyclic order on the `2r` cell directions has at most `2r` length-`q`
intervals, whether or not all are block-simple.  Therefore one cell reaches
at most

\[
                         2r\,2^q4^{r-q}               \tag{6.4}
\]

fine targets even at the affine-face level.  There are `2^r` cells.  Divide
the resulting upper bound by (0.6):

\[
\begin{aligned}
 \frac{2^r(2r)2^q4^{r-q}}
      {\binom rq6^q8^{r-q}}
 &=\frac{2r}{\binom rq}\left(\frac23\right)^q.
\end{aligned}                                         \tag{6.5}
\]

This proves (0.7).  Hamming phases can only delete affine candidates, so
the bound applies to every common-order long-cycle resolution in each cell.

For `q=A sqrt(m)+O(1)` and `r<=m/4`, use `binom(r,q)>=1` in (6.5) to obtain

\[
 \log(\hbox{reachable fraction})
 \le -A\log(3/2)\sqrt m+O(\log m),                    \tag{6.6}
\]

which proves (0.8).

The positive diagonal bank of Section 5 restricts every touched singleton
to `{t_i,e_i}`.  It therefore has size `2^r` at `q=r`, compared with `6^r`
in the full touched family: its exact relative density is `3^(-r)`.  This is
why exact nonuniqueness and exact long-cycle capacity do not contradict the
full-family no-go.

## 7. A general tensor carrier-entropy inequality

The preceding count is an instance of a packet-independent inequality.
It isolates exactly why local nonuniqueness is not by itself enough.

Let a finite owner support `Omega` be partitioned into `B` cells of a
common size `n`, so `|Omega|=Bn`.  Suppose every cell has `D` relevant local
direction slots.  Let `Z` be a local touched-target alphabet of size `a`, and
assume that a fixed relevant direction in a fixed cell carries at most
`lambda` members of `Z`.  Untouched targets are the local owners themselves.

Tensor `r` copies.  The natural depth-`q` fine family is obtained by choosing
`q` touched blocks, a member of `Z` in each touched block, and an arbitrary
owner of `Omega` in every untouched block.  Its cardinality is

\[
             \binom rq a^q|\Omega|^{r-q}.             \tag{7.1}
\]

Assume a serving window must select one relevant direction in each touched
block.  This is the usual block-simple rank ledger and is exactly the rule in
both the octahedral and rectangle packets.

### Theorem 7.1 (tensor carrier-entropy bound)

Give every one of the `B^r` product cells one arbitrary common cyclic order
of its `Dr` relevant directions, with arbitrary spectators allowed.  Then the
fraction of the fine family (7.1) which can be an affine lower face of a
consecutive `q`-window is at most

\[
 \boxed{
  \min\left\{1,
   \frac{Dr}{\binom rq}\left(\frac{B\lambda}{a}\right)^q
  \right\}.}                                          \tag{7.2}
\]

#### Proof

A cyclic order has at most `Dr` intervals of length `q` consisting entirely
of relevant directions; inserting spectators cannot increase this number.
Only block-simple intervals can serve (7.1).  Fix one such interval in one
product cell.  Every touched block permits at most `lambda` target labels,
and every untouched block permits at most the `n` owners belonging to its
local cell.  Hence the interval serves at most

\[
                         \lambda^qn^{r-q}              \tag{7.3}
\]

fine targets.  Summing over `Dr` intervals and `B^r` cells, then dividing by
(7.1), gives

\[
 \frac{B^rDr\lambda^qn^{r-q}}
      {\binom rq a^q(Bn)^{r-q}}
 =\frac{Dr}{\binom rq}
       \left(\frac{B\lambda}{a}\right)^q.             \tag{7.4}
\]

Overlaps only reduce the reachable union.  QED.

For the octahedral `Q_3` packet, restricted to its special local direction,

\[
             (B,D,\lambda,a)=(3,1,4,16),              \tag{7.5}
\]

so the entropy ratio is `B lambda/a=3/4`; the sharper run argument replaces
`r` in (7.2) by `r-q+1`.  For the six-coordinate rectangle,

\[
             (B,D,\lambda,a)=(2,2,2,6),               \tag{7.6}
\]

so `B lambda/a=2/3`, recovering (0.7).

Thus a bounded tensor primitive with

\[
                         \frac{B\lambda}{a}<1          \tag{7.7}
\]

has an unavoidable exponential full-family loss at every Gaussian depth
whenever `Dr=exp(o(q))` (in particular for a bounded local packet tensored
over `r=O(m)` blocks), regardless of how its local carrier multiplicities
are distributed.  To
remove the fine obstruction by this architecture, a new local packet must
at least reach the threshold `B lambda>=a`, and it must still overcome the
remaining factor `Dr/binom(r,q)`.  This is a quantitative design condition,
not merely a request for one target with two carriers.

## 8. An all-depth invariant for every owner trade

Let `F` be any vertex-disjoint family of isometric `C_(2h)`'s, all of the
same middle rank.  For a directed start `s` on a cycle `C`, let

\[
 L_q(C,s)=\bigcap_{j=0}^qX_{s+j},\qquad
 U_q(C,s)=\bigcup_{j=0}^qX_{s+j},\qquad 1\le q<h.      \tag{8.1}
\]

For a ground coordinate `x`, write

\[
\begin{aligned}
 A^-_{q,x}&=\#\{(C,s):x\in L_q(C,s)\},\\
 A^+_{q,x}&=\#\{(C,s):x\in U_q(C,s)\},\\
 N_x&=\#\{X\in V(F):x\in X\}.
\end{aligned}                                         \tag{8.2}
\]

### Theorem 8.1 (coordinate-star conservation)

For every `x` and every `1<=q<h`, equation (0.9) holds.

#### Proof

It suffices to work on one cycle.  If `x` is frozen full, it lies in both
`L_q` and `U_q` at all `2h` starts.  Its contribution to the left side is
`4h`, while it belongs to all `2h` cycle owners, giving the same value on
the right.  If it is frozen empty, both values are zero.

Suppose `x` is one endpoint of an active direction.  Exactly `2q` cyclic
starts have a length-`q` direction interval containing that direction.  At
those starts `x` lies in the upper union and not in the lower intersection.
At the remaining `2h-2q` starts the direction is not used, so its orientation
is constant throughout the window.  Antipodal symmetry gives `h-q` starts
with endpoint `x` selected and `h-q` with its mate selected.  Consequently

\[
 \#\{s:x\in L_q(C,s)\}=h-q,\qquad
 \#\{s:x\in U_q(C,s)\}=h+q.                          \tag{8.3}
\]

Their sum is `2h`.  The coordinate `x` occurs at exactly `h` owner vertices
of `C`, so this is again twice its owner count.  Summing over the disjoint
cycles proves (0.9).  QED.

### Corollary 8.2 (trade form)

If two exact factors have the same owner support, then at every depth and
for every coordinate

\[
                    \Delta A^-_{q,x}=-\Delta A^+_{q,x}. \tag{8.4}
\]

The statement is insensitive to macroprofile boundaries and remains valid
for cross-block direction pairs.  On the full middle layer,
`N_x=binom(2m-1,m-1)=W/2`, so (0.9) becomes

\[
                         A^-_{q,x}+A^+_{q,x}=W.        \tag{8.5}
\]

## 9. Proved boundary

The rectangle packet closes the first local question positively:

* a fine target can have several simultaneous carrier cycles in one exact
  coefficient-one packet;
* this first happens with two cycles, eight owners, and six active
  coordinates;
* the carriers can lie in different predecessor macroprofiles and the
  owner trade can mix those profiles inside its switched cycles;
* tensoring gives an exact `2^s` predecessor cube and an exact long-cycle
  realization on the all-shared target bank.

It does not close global coefficient one.  With one Hamming order per tensor
cell, the complete six-label fine family still suffers the exponential bound
(0.7).  Any successor must therefore do at least one of the following:

1. rotate the doubled pair `{t_i,e_i}` through a positive-density set of
   physical singleton labels while preserving one exact owner factor;
2. use a larger local packet whose target-to-carrier incidence has more than
   one bit of order entropy without an omitted-label loss; or
3. splice different cyclic orders inside one cell rather than merely choosing
   one common Hamming order for that cell.

Every such construction must also respect the two-sided star law (8.4).
