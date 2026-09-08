# The minimal rectangle carrier: exact cross-sector tensor capacity and its sharp bounded-branch limit

Date: 2026-07-26

Method: pure mathematics only.

## 0. Theorem-level verdict

There is a smaller and cleaner escape from the octahedral unique-carrier
lock than a larger Johnson cell.  On six coordinates put

\[
 \Omega=\{\{s,y\}:s\in\{t,e\},\ y\in\{a,b,c,d\}\}.                \tag{0.1}
\]

For every perfect matching `M` of `K_4[a,b,c,d]`,

\[
 \mathcal F_M
 =\bigl\{\{t,e\}*P:P\in M\bigr\}                                 \tag{0.2}
\]

is an exact partition of the eight owners in `Omega` into two literal
`C_4`'s.  The singleton targets `{t}` and `{e}` each have two simultaneous,
owner-disjoint carriers.  The three perfect matchings of `K_4` give three
alternative exact `2`-cycle factors of the same support, and change the
physical pairing of the four source extensions.

This is the smallest possible simple pair-flip cycle packet with two
carriers: four distinct middle extensions are necessary, and two `C_4`'s
already require eight owners.  The rectangle attains both bounds.

Putting the two extension pairs in different coarse blocks makes (0.2) a
literal cross-sector carrier kernel.  For

\[
 M_0=ab\mid cd,\qquad M_1=ac\mid bd,\qquad M_2=ad\mid bc,        \tag{0.3}
\]

the three physical pairing polynomials are

\[
 y_{ab}+y_{cd},\qquad y_{ac}+y_{bd},\qquad y_{ad}+y_{bc}.          \tag{0.4}
\]

Their common extension marginal is

\[
                         z_a+z_b+z_c+z_d.                           \tag{0.5}
\]

Thus this packet realizes a genuine integral part of the macroprofile
flow while exposing the extra datum that the marginal flow forgets:
physical extensions must be paired into cycle directions.

Tensor `r` copies and adjoin `d` spectator axes so that

\[
                         h=2r+d
\]

is a power of two.  As a literal subpacket of the middle layer
`binom([2m],m)`, this uses a fixed-full core of size `m-2r-d` and a
fixed-empty complement of size `m-4r-d`; hence the exact ambient condition
is

\[
                         4r+d\le m.                              \tag{0.5a}
\]

There are `2^r` owner-disjoint cells `Q_h`.  A fine
target touching a prescribed `q`-set of rectangle blocks has exactly
`2^q` carrier cells.  If

\[
                         \log_2h+1\le q<h,                         \tag{0.6}
\]

one exact factor covers every labelled target for that fixed touched set
across all of its carrier cells, with total exact multiplicity

\[
                         \boxed{4^q/h}.                             \tag{0.7}
\]

So cross-sector nonunique carriage is real and quantitatively abundant.

It is nevertheless insufficient when all touched sets must be handled by
one bounded tensor atlas.  In the class of cell factors having one common
doubled-permutation order per cell, the optimal reached fraction
`rho_(r,q)` of the natural fine family satisfies

\[
 1-\left(1-{1\over\binom rq}\right)^{2^q}
 \le \rho_{r,q}
 \le \min\left\{1,{2^q(r-q+1)\over\binom rq}\right\}.             \tag{0.8}
\]

Hence, for `q=o(r)` and `2^q/binom(r,q)=o(1)`,

\[
 \log\rho_{r,q}
 =-q\log(r/q)+(\log2-1)q
   +O\left({q^2\over r}+\log r+\log q\right).                     \tag{0.9}
\]

Even with arbitrary cycle orders, the owner-start count gives

\[
 \boxed{
 \rho^{\rm arbitrary}_{r,q}
 \le \min\left\{1,{8^q\over\binom rq}\right\}.}                  \tag{0.10}
\]

Thus at `q=A sqrt(m)+O(1)` and `r/q -> infinity`, every bounded rectangle
tensor reaches only `o(1)` of this fine family.  A local bank with `t`
carriers in every local cell position needs

\[
                         t\ge(e-o(1)){r\over q}                    \tag{0.11}
\]

when `q=o(r)` and `log r=o(q)`, as in the Gaussian regime.  The next
exact positive statement must therefore be a
growing carrier bank, not another bounded rectangle.

Finally, every cycle factor, whether tensorial or not, obeys the exact
two-sided coordinate-star law

\[
                         A^-_{q,x}+A^+_{q,x}=2M_x.                  \tag{0.12}
\]

Here `M_x` is the number of middle owners containing coordinate `x`, and
`A^-_(q,x),A^+_(q,x)` count lower and upper depth-`q` occurrences
containing `x`.  For a full middle layer, `M_x=W/2`, so the right side is
`W`.  Consequently every lower cross-sector correction has a forced
upper correction.  This is compatible with the ideal uniform ledgers,
but rules out treating the two signs as independent transport problems.

The results below are packet/tensor theorems, not an ambient
`Omega(W)` obstruction.  Cross-sector packets outside this atlas may feed
the same physical targets.

## 1. Three exact rectangle factors

For two disjoint two-sets `P,Q`, write

\[
                         P*Q=\{\{p,q\}:p\in P,q\in Q\}.             \tag{1.1}
\]

In the Johnson graph on two-subsets, `P*Q` is the physical square

\[
 (p_0q_0,p_0q_1,p_1q_1,p_1q_0).                                  \tag{1.2}
\]

Its two directions exchange the endpoints of `P` and of `Q`; hence it is
a literal isometric `Q_2=C_4`.

Let `A={a,b,c,d}`.  For a perfect matching `M={P_1,P_2}` of `A`, define

\[
                         \mathcal F_M
                         =\{\{t,e\}*P_1,\{t,e\}*P_2\}.             \tag{1.3}
\]

### Theorem 1.1 (exact `2`-by-`2` associator)

Every `mathcal F_M` is a partition of `Omega` into two physical `C_4`'s.
The three matchings in (0.3) therefore give three exact alternative cycle
factors of the same eight-owner support.

#### Proof

The two pairs `P_1,P_2` partition `A`.  Hence the two products in (1.3)
are disjoint and their union is

\[
 \{t,e\}*A=\Omega.
\]

Each product is a physical square by (1.2).  \(\square\)

The overlap of two different rectangle factors is connected.  Indeed,
the union of two different perfect matchings on four vertices is an
alternating `C_4`; taking products with `{t,e}` preserves one connected
four-cycle ownership overlap.  Thus changing the matching is a genuine
two-cycle component trade, not a union of independent one-cycle choices.

### Lemma 1.2 (exact lower carriers)

For `P={x,y}`, the cycle `{t,e}*P` has lower-target sequence

\[
                         t,y,e,x                                  \tag{1.4}
\]

up to cyclic orientation.  Consequently, in every factor `mathcal F_M`,

\[
 L_t=L_e=2,qquad L_a=L_b=L_c=L_d=1.                              \tag{1.5}
\]

#### Proof

Orient the square as

\[
                         tx,ty,ey,ex,tx.
\]

Successive intersections are respectively `t,y,e,x`.  There are two
matched pairs, so `t,e` each occur once in each square.  Every element of
`A` lies in one matched pair and occurs once there.  \(\square\)

For the target `{t}`, the two physical carrier edges are exactly the two
matching edges `P_1,P_2` on its four extensions `ta,tb,tc,td`.  Changing
`M` changes their pairing while retaining every extension and every owner.

### Proposition 1.3 (absolute local minimality)

Any two owner-disjoint edge carriers of one target use at least four
different middle extensions.  Moreover, one physical isometric
`C_(2h)` contains a fixed depth-one target at most once.  Therefore an
exact simple-isometric-cycle packet with two carriers has at least two
cycles and eight owners.  The rectangle factor has four extensions and
eight owners, so both bounds are sharp.

#### Proof

A carrier is an edge between two distinct middle extensions of the target.
Owner-disjoint carriers have disjoint endpoint pairs and therefore need
four extensions.

An isometric `C_(2h)` has a fixed core and `h` pairwise disjoint active
coordinate pairs.  The lower target of an edge in direction `i` contains
one chosen endpoint of every active pair except pair `i`.  Hence lower
targets belonging to two different directions cannot agree.  The two
edges in the same direction occur at antipodal phases; when `h>=2`, their
orientations on every other active pair are complementary, so their lower
targets also differ.  Thus one target occurs at most once on the cycle.
Under the simple-cycle convention `h>=2`, so every such cycle has at least
four owners.  Two carriers consequently need two cycles and at least
eight owners.  Theorem 1.1 and Lemma 1.2 attain equality.  \(\square\)

## 2. Macroprofile kernel and the missing pairing datum

Let `ell` be the macroprofile of `{t}` together with an arbitrary fixed
outside core.  Put `a,b` in coarse block `B_0` and `c,d` in coarse block
`B_1`.  In the factor `M_0=ab|cd`, the two carrier cycles feed `{t}` from

\[
                         k^{(0)}=\ell+e_{B_0},\qquad
                         k^{(1)}=\ell+e_{B_1}.                       \tag{2.1}
\]

Their carrier-cell polynomial and extension polynomial are

\[
                         z_{B_0}+z_{B_1},\qquad
                         2z_{B_0}+2z_{B_1}.                        \tag{2.2}
\]

If `a,b,c,d` are put in four different coarse blocks, the extension
marginal is instead

\[
                         z_a+z_b+z_c+z_d,                          \tag{2.3}
\]

while (0.4) records the three possible physical pairings of those four
terms.  Thus the abstract inclusion flow sees (2.3), whereas the cycle
compiler must additionally choose one of the three matchings (0.4).

At depth one,

\[
 {F_{\ell+e_j,\ell}\over V_{\ell+e_j}}
 ={1\over m}\binom{\ell_j+1}{\ell_j}
 ={\ell_j+1\over m},                                             \tag{2.4}
\]

which is the row-side deletion multiplicity.  A carrier bank is organized
around a fixed target, so the relevant normalization is instead

\[
 {F_{\ell+e_j,\ell}\over T_\ell}
 ={8-\ell_j\over m}.                                             \tag{2.5}
\]

Indeed,

\[
 \binom8{\ell_j+1}\binom{\ell_j+1}{\ell_j}
 =\binom8{\ell_j}(8-\ell_j).                                    \tag{2.6}
\]

Thus an exact target-rooted local lift needs `8-ell_j` extension tokens
of sector `j`, followed by a physical matching of those tokens into
carrier directions.  Equations (2.3)--(2.6) separate the two requirements
exactly:

1. the weighted extension marginal; and
2. an integral matching of extensions with no repeated middle owner.

The rectangle solves the second requirement on four tokens and realizes a
positive equal-weight subkernel of the first.

At depth `q` the refinement is stricter still.  A physical `q`-face
chooses `q` disjoint carrier pairs, and its `2^q` middle corners choose one
endpoint from each pair.  Thus a lift of the full target-rooted
coefficient

\[
                         \prod_j\binom{8-\ell_j}{d_j}               \tag{2.7}
\]

requires a matching/transversal design on the available extension tokens;
an arbitrary integral flow of unpaired tokens is not enough.

For coordinate-disjoint rectangles, tensoring is literal.  With block `i`
assigned sector increments `B_(i,0),B_(i,1)`, a touched set `I` has
carrier polynomial

\[
                         \prod_{i\in I}
                         (z_{B_{i,0}}+z_{B_{i,1}}).                 \tag{2.8}
\]

Every one of its `2^q` binary source macroprofiles occurs with coefficient
one.  No fractional decomposition is being used.

## 3. Tensor packet and fine targets

Take `r` coordinate-disjoint rectangles and fix one matching factor in
each.  Adjoin `d` disjoint spectator pairs and choose

\[
                         h=2r+d=2^s.                               \tag{3.1}
\]

For an ambient central layer on `[2m]`, assume `4r+d<=m`.  Add a fixed-full
core of size `m-2r-d` and leave the remaining `m-4r-d` coordinates fixed
empty.  Every packet owner then has rank exactly `m`; after touching `q`
rectangle blocks, every target below has rank exactly `m-q`.  The abstract
packet statements do not otherwise depend on this embedding.

The product owner set

\[
                         \Omega^{(r,d)}
                         =\Omega_1\times\cdots\times\Omega_r
                           \times Q_d                              \tag{3.2}
\]

has size

\[
                         8^r2^d.                                  \tag{3.3}
\]

Choosing one of the two local squares in every rectangle gives `2^r`
pairwise disjoint cells

\[
                         Q_2^{\square r}\square Q_d=Q_h.           \tag{3.4}
\]

The count

\[
                         2^r2^h=2^r2^{2r+d}=8^r2^d                \tag{3.5}
\]

audits exact ownership.

Fix `I in binom([r],q)`.  Let `mathcal T_I` consist of the targets which
have local restriction `{t_i}` in every `i in I`, an arbitrary local
middle owner in every `i notin I`, and an arbitrary spectator orientation.
An exterior core embeds this packet at the ambient middle rank.  Then

\[
                         |\mathcal T_I|=8^{r-q}2^d,                \tag{3.6}
\]

and the disjoint union over touched sets has

\[
                         |\mathcal T_{r,q}|
                         =\binom rq8^{r-q}2^d.                     \tag{3.7}
\]

### Lemma 3.1 (exact `2^q` carrier multiplicity)

Every target in `mathcal T_I` is a lower `q`-face in exactly `2^q`
product cells.

#### Proof

In a touched rectangle, `{t_i}` has one carrier in each of the two local
squares.  In an untouched rectangle, the prescribed middle owner belongs
to exactly one local square.  The `q` touched choices are independent,
giving `2^q`.  Product cells are disjoint, so all these carriers are
simultaneously legal.  \(\square\)

## 4. A prescribed-direction full-face factor

We record the cycle lemma needed to turn carrier faces into literal
windows.

### Lemma 4.1

Let `h=2^s`, let `D` be a prescribed `q`-set of directions of `Q_h`, and
assume `s+1<=q<h`.  There is a vertex partition of `Q_h` into isometric
`C_(2h)` cycles with a common doubled-permutation transition word such
that `D` is a cyclic interval and every `D`-face occurs exactly `2^q/h`
times as a consecutive lower window.

#### Proof

Let `U=F_2^s`, `Sigma=U direct-sum <v>`.  Order the directions so that
`D` contains cyclic positions `h,1,...,s`.  List `U` as

\[
 u_0=0,\qquad u_j=e_1+\cdots+e_j\quad(1\le j\le s),               \tag{4.1}
\]

followed by the unused vectors in any order.  Define

\[
 \phi(e_j)=u_j+u_{j-1}\ (j<h),\qquad
 \phi(e_h)=v+u_{h-1}.                                             \tag{4.2}
\]

The first-half prefix syndromes of the standard doubled-permutation cycle
are all `u_j`; the second-half syndromes are all `v+u_j`.  Hence the
cycle is a complete syndrome transversal and its translates by
`K=ker(phi)` partition `Q_h`.

The syndromes of `e_1,...,e_s` are a basis of `U`, and `phi(e_h)` has
nonzero `v`-component.  Thus `phi(F_2^D)=Sigma`.  Projection of `K` onto
the coordinates outside `D` is surjective, with every fibre of size

\[
                         |K\cap F_2^D|=2^{q-s-1}.                  \tag{4.3}
\]

The proper cyclic interval `D` occurs twice in the doubled word.  Every
`D`-face therefore occurs

\[
                         2\cdot2^{q-s-1}=2^q/h                    \tag{4.4}
\]

times.  The doubled-permutation cycles are isometric because no direction
repeats on an arc of at most `h` transitions.  \(\square\)

### Theorem 4.2 (complete fixed-`I` coverage)

Assume (0.6).  For every fixed `I in binom([r],q)` there is one exact
factor of the tensor packet into physical isometric `C_(2h)` cycles in
which every target in `mathcal T_I` occurs exactly `4^q/h` times.

#### Proof

In each product cell let `D` be its `q` carrier directions in the blocks
of `I`, and apply Lemma 4.1.  The cell factors unite to an exact packet
factor because the cells are owner-disjoint.  By Lemma 3.1 each target has
one relevant `D`-face in `2^q` cells, and each face has multiplicity
`2^q/h`.  The product is `4^q/h`.  \(\square\)

For `q=A sqrt(m)+O(1)` and `log h=o(sqrt(m))`, this multiplicity equals

\[
                         \exp(A\log4\sqrt m-\log h+o(\sqrt m)).    \tag{4.5}
\]

Thus one prescribed cross-sector flow cell has far more than constant
physical capacity.

## 5. One exact factor over all touched sets

In every product cell independently choose a uniform
`J in binom([r],q)` and install the full-face factor of Lemma 4.1 for its
`J` carrier directions.  In choosing the common order, put the `J`
carrier directions in one run and separate every other carrier direction
from the next by an unmarked direction.  There are at least `r` unmarked
directions, so this is possible.  Consequently `J` is the only all-carrier
`q`-interval in that cell.  These choices always preserve exact ownership.

A fixed target in `mathcal T_I` has `2^q` candidate cells.  By the
separation just imposed, it is covered in a candidate precisely when that
cell chose `J=I`.  Hence its miss
probability is

\[
                         \left(1-{1\over\binom rq}\right)^{2^q}.   \tag{5.1}
\]

Taking expectations over all targets proves the lower bound in (0.8):
some deterministic exact factor reaches at least that fraction.

## 6. Common-order upper bound and exact exponent

Now allow an arbitrary common doubled-permutation order independently in
every product cell.  Mark its one carrier direction from each rectangle.
There are `r` marked and at least `r` unmarked directions.  If the marked
positions have cyclic run lengths `s_1,...,s_j`, the number of all-marked
`q`-intervals is

\[
 \sum_{i=1}^j(s_i-q+1)_+\le r-q+1.                               \tag{6.1}
\]

For every such interval support `I`, one cell contains at most

\[
                         4^{r-q}2^d                               \tag{6.2}
\]

targets from `mathcal T_I`: every untouched local square has four owners,
while touched local targets and spectator orientations are fixed as in
(3.6).  With `2^r` cells, the total reached number is at most

\[
                         2^r(r-q+1)4^{r-q}2^d.                     \tag{6.3}
\]

Division by (3.7) gives the upper bound in (0.8).

If `2^q/binom(r,q)=o(1)`, the lower bound is

\[
                         (1+o(1)){2^q\over\binom rq}.              \tag{6.4}
\]

The two bounds differ by at most the polynomial factor `r-q+1`.  For
`q=o(r)`,

\[
 \log\binom rq
 =q\log(r/q)+q
  +O\left({q^2\over r}+\log q\right),                            \tag{6.5}
\]

which proves (0.9).  In particular, if `q=A sqrt(m)+O(1)` and
`r/q -> infinity`,

\[
 \log\rho_{r,q}
 \le -A\sqrt m\log\left({r\over A\sqrt m}\right)
      +O_A(\sqrt m+\log r),                                      \tag{6.6}
\]

and the reached fraction tends to zero.

## 7. Arbitrary cycle orders still face a packet count

Every packet owner is one directed start and supplies only one lower
target at depth `q`.  Thus an arbitrary exact cycle factor reaches at most
`8^r2^d` distinct targets.  Comparing with (3.7) proves (0.10).

For `q=o(r)`,

\[
 \log\rho^{\rm arbitrary}_{r,q}
 \le -q\log(r/q)+(\log8-1)q
    +O\left({q^2\over r}+\log q\right).                            \tag{7.1}
\]

This again tends to minus infinity when `r/q -> infinity`.  This count is
factor-independent but packet-sector-specific; it is not an ambient
coefficient-one lower bound.

More generally, suppose a local packet is partitioned into `t` cells and
the distinguished target has one carrier in every cell.  Replacing the
two rectangle cells by those `t` cells in Section 6 gives

\[
                         \rho_{r,q}
                         \le {t^q(r-q+1)\over\binom rq}.            \tag{7.2}
\]

Keeping this bounded below requires

\[
 t\ge
 \exp\left({\log\binom rq-\log(r-q+1)+O(1)\over q}\right)
 =(e-o(1)){r\over q}                                               \tag{7.3}
\]

for `q=o(r)` and `log r=o(q)`.  Since `t` disjoint edge carriers need at least `2t`
middle extensions, every successful local bank in this tensor scheme must
grow at the same scale.

## 8. The global two-sided star invariant

Let an arbitrary exact cycle factor have middle-owner set `mathcal M`.
For a directed start `X`, let `Y` be the owner reached after `q` geodesic
pair flips, and let `L(X),U(X)` be the associated lower and upper shadows.
Coordinatewise,

\[
 \mathbf1_{x\in L(X)}+\mathbf1_{x\in U(X)}
 =\mathbf1_{x\in X}+\mathbf1_{x\in Y}.                            \tag{8.1}
\]

Indeed, if `x` occurs in both endpoints it occurs in both intersection
and union; if it occurs in one endpoint it occurs only in the union; and
if it occurs in neither it occurs in neither.

As `X` ranges over all directed starts, the map `X mapsto Y` is the
`q`th power of the cycle successor permutation and therefore permutes
`mathcal M`.  Summing (8.1) gives

\[
 A^-_{q,x}+A^+_{q,x}
 =2|\{X\in\mathcal M:x\in X\}|=2M_x,                              \tag{8.2}
\]

which is (0.12).

For the complete middle layer on `2m` coordinates,

\[
                         M_x={1\over2}\binom{2m}{m}={W\over2},    \tag{8.3}
\]

so the sum is exactly `W`.  The ideal uniform lower and upper ledgers
also satisfy this identity:

\[
 W{m-q\over2m}+W{m+q\over2m}=W.                                  \tag{8.4}
\]

Thus (8.2) is not a no-go against the balanced target.  It is an exact
coupling condition: a local operation cannot correct a lower coordinate
star without producing the complementary upper-star change.

## 9. Exact boundary and next lemma

The rectangle closes the local existence question:

* nonunique physical carriage occurs in the minimum eight-owner packet;
* alternative exact factors pair the same four source extensions in three
  different ways;
* tensoring gives `2^q` simultaneous carrier cells;
* a full-face syndrome factor turns this into literal multiplicity
  `4^q/h` for every target of one prescribed profile;
* one exact factor has the positive all-profile coverage (0.8).

But bounded branching loses against `binom(r,q)` when `r/q` grows.  The
precise constructive successor is now:

> Build an owner-disjoint local bank of
> `t=Omega(r/q)` carrier directions above each relevant target, distribute
> its target-rooted extension endpoints with multiplicities proportional
> to `8-ell_j` (and, at repeated depth, to
> `binom(8-ell_j,d)`), pair those endpoints integrally, and preserve the
> two-sided star law (8.2).

Neither the old octahedral `Q_3` atlas nor the bounded rectangle tensor
supplies this growing dispersion.
