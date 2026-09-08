# Why fixed-depth shadows do not bootstrap by ordinary staging or products

This note audits three natural attempts to upgrade the fixed-depth theorem in
`FIXED_DEPTH_SHADOWS.md` to a band of half-width

\[
        H=\sqrt{m\,\omega(m)},\qquad \omega(m)\longrightarrow\infty.
\]

The conclusions are negative, but exact.  A fixed-depth construction cannot
be amplified by concatenating independently certified stages, by taking a
Cartesian tensor power, or by traversing independently the diagonal middle
rows of product SCD rectangles.  All three mechanisms lose a macroscopic
amount before the required scale is reached.

The third obstruction has a useful representation-theoretic interpretation:
the Clebsch--Gordan radius imbalance between two independently chosen SCD
chains is of order the square root of the block dimension.  A successful
product theorem must transfer this radius between different chain rectangles;
it cannot process each rectangle independently.

None of the results below rules out a genuinely interlaced multiscale braid.
They do show that such a braid is a new growing-depth theorem, rather than a
formal consequence of the existing fixed-depth theorem.

## 1. Endpoint capacity rules out concatenated fixed-depth stages

Let a word be split into modules, and require every selected witness to lie
inside one module.  Suppose a module is certified for at most `R` ranks.  An
endpoint in that module supplies a chain of suffix ORs, and hence at most one
mask of any fixed rank.  Therefore a module of length `L` certifies at most
`RL` masks across its designated ranks.

### Proposition 1 (stage-capacity bound)

Let `n=2m`.  Suppose internally witnessed modules together cover every mask
of ranks

\[
             m-\lfloor c\sqrt m\rfloor,\ldots,
             m+\lfloor c\sqrt m\rfloor                 \tag{1.1}
\]

for some fixed `c>0`, and every module is assigned at most `2J+1` of these
ranks.  If their total length is `L`, then

\[
             L=\Omega_c\!\left(\frac{W_m\sqrt m}{J+1}\right),
             \qquad W_m=\binom{2m}{m}.                 \tag{1.2}
\]

#### Proof

For every `|q|<=c sqrt(m)`, the local central-binomial estimate gives

\[
       \binom{2m}{m+q}\ge c_0(c)W_m.                   \tag{1.3}
\]

Thus (1.1) contains `Theta_c(W_m sqrt(m))` distinct target masks.  As noted
above, one endpoint certifies at most one target in each designated rank, so
all modules together certify at most `(2J+1)L` targets.  Comparing the two
counts proves (1.2).  QED.

In particular, if `J=o(sqrt(m))`, independently appending fixed-depth
modules costs `omega(W_m)`.  A viable multiscale construction must reuse the
same endpoints at many depths; it cannot append one fixed-depth certificate
per scale.

## 2. Cartesian tensor powers have a local-imbalance barrier

Partition `[2st]` into `t` blocks of size `2s`.  Call a target **locally
eligible** when its restriction to every block has rank in

\[
                        [s-J,s+J].                     \tag{2.1}
\]

Any literal Cartesian product of local depth-`J` gadgets can directly handle
only locally eligible targets.  The following count shows why additive depth
amplification does not follow.

Put

\[
 p_{s,J}=2^{-2s}\sum_{|u|\le J}\binom{2s}{s+u}.        \tag{2.2}
\]

### Proposition 2 (tensor eligibility bound)

Among the global middle sets of `[2st]`, the fraction that are locally
eligible is at most

\[
          O(\sqrt{st})\,p_{s,J}^{\,t}.                \tag{2.3}
\]

Moreover, for every `t>=2`, the fraction whose restriction to even the first
block satisfies (2.1) is

\[
                  O\!\left(\frac{J+1}{\sqrt s}\right).\tag{2.4}
\]

#### Proof

Take `t` independent uniformly random subsets of the `2s`-blocks, and
condition their total rank to be `st`.  This conditional distribution is
uniform on the global middle layer.  The unconditioned probability that all
blocks satisfy (2.1) is `p_(s,J)^t`, while

\[
 \Pr\{\operatorname {Bin}(2st,1/2)=st\}=\Theta((st)^{-1/2}).
\]

Dividing gives (2.3).

For (2.4), the rank of the first block in a uniformly random global middle
set has the hypergeometric distribution

\[
 \Pr\{R=r\}
 =\frac{\binom{2s}{r}\binom{2s(t-1)}{st-r}}
        {\binom{2st}{st}}.                              \tag{2.5}
\]

Its variance is `Theta(s)` uniformly for `t>=2`, and the maximum atom of
this log-concave distribution is `O(s^(-1/2))` by the usual consecutive-ratio
bound (or Stirling's formula).  Summing `2J+1` atoms proves (2.4).  QED.

Consequences:

* if `s->infinity` and `J=o(sqrt(s))`, even one block excludes
  `1-o(1)` of the global middle layer;
* if `s,J` are fixed with `J<s` and `t->infinity`, then `p_(s,J)<1`, so
  (2.3) tends exponentially to zero; and
* tensoring many copies so that a formal depth `tJ` becomes much larger than
  `sqrt(st)` does not help: almost every target uses an off-band local state.

Thus a block product can work only after it already controls local
fluctuations on at least their natural `sqrt(s)` scale (and, for many blocks,
on the corresponding maximum-fluctuation scale).  This is the growing-depth
problem again, not a bootstrap from fixed `J`.

## 3. Exact audit of the natural SCD product row

The preceding entropy count concerns literal products of local bands.  There
is a more sophisticated possibility: take full SCDs in the two factors and
use the rank convolution.  Its simplest middle row can be audited exactly.

Split \([4s]=X\mathbin{\dot\cup}Y\), with \(|X|=|Y|=2s\).  Let
\(\mathcal C_X\) and \(\mathcal C_Y\) be arbitrary symmetric-chain
decompositions.  Index a chain of radius `a` as

\[
 C_{-a}\subset C_{-a+1}\subset\cdots\subset C_a,
 \qquad |C_i|=s+i.                                  \tag{3.1}
\]

The number of radius-`a` chains is forced:

\[
 v_a=\binom{2s}{s-a}-\binom{2s}{s-a-1}
     =\binom{2s}{s-a}\frac{2a+1}{s+a+1}.            \tag{3.2}
\]

For chains `C,D` of radii `a,b`, put `r=min(a,b)`.  Their global middle
members are exactly

\[
              T_i=C_i\cup D_{-i},\qquad -r\le i\le r.\tag{3.3}
\]

They form a Johnson path in either monotone order.  These diagonal paths,
over all ordered chain pairs `(C,D)`, partition the complete middle layer of
`B_(4s)`.

### Theorem 3 (product-rectangle shadow theorem)

The consecutive intersections and unions internal to the diagonal path
(3.3) are exactly the cells

\[
             C_u\cup D_v,\qquad |u|,|v|\le r.         \tag{3.4}
\]

Consequently the number of cells in the rectangle \(C\times D\) not supplied
by internal diagonal windows is

\[
 (2a+1)(2b+1)-(2r+1)^2
       =2(2r+1)|a-b|.                                \tag{3.5}
\]

No internal window belonging to another chain rectangle can supply one of
these missing cells.

#### Proof

Order (3.3) by increasing `i`.  For `i<=j`, nesting in the two factor chains
gives

\[
 \bigcap_{x=i}^{j}T_x=C_i\cup D_{-j},
 \qquad
 \bigcup_{x=i}^{j}T_x=C_j\cup D_{-i}.                \tag{3.6}
\]

If `u+v<=0`, take `i=u,j=-v` in the intersection formula.  If `u+v>=0`,
take `i=-v,j=u` in the union formula.  This proves that every cell in (3.4)
occurs.  Formula (3.6) also proves that no other cell of the rectangle occurs.
Subtracting its `(2r+1)^2` central cells from the rectangle size proves
(3.5).

Finally, restricting an intersection or union of middle sets to `X` gives
an intersection or union of members of one chain `C`, hence another member
of `C`; similarly on `Y`.  Since the two factor SCDs partition their Boolean
lattices, every resulting mask belongs to a unique chain rectangle.  A
window internal to a different rectangle therefore cannot duplicate a
missing cell here.  QED.

Summing (3.5), the exact number of Boolean masks missed by all internal
diagonal windows is

\[
 \boxed{
 E_s=2\sum_{a,b=0}^{s}v_av_b(2\min(a,b)+1)|a-b|.
 }                                                       \tag{3.7}
\]

This is the Clebsch--Gordan imbalance term.  The product of radius-`a` and
radius-`b` chains decomposes into `2min(a,b)+1` global chains, and every one
of those chains carries the common residual radius `|a-b|` which the
diagonal traversal cannot resolve internally.

For a deliberately generous comparison, say that a rectangle receives a
**\(J\)-halo** if, when \(a\le b\), it is credited with every cell whose
\(C\)-index lies in \([-a,a]\) and whose \(D\)-index lies in
\([-a-J,a+J]\cap[-b,b]\), and symmetrically when \(b<a\).  This credits
arbitrary extra structure in the first \(J\) levels of each residual tail,
without charging any entries for it.

### Proposition 4 (the imbalance is macroscopic)

There are absolute constants `c,C>0` such that, for all sufficiently large
`s`,

\[
        E_s\ge c\,2^{4s}
        =\Theta\!\left(\binom{4s}{2s}\sqrt s\right),
                                                               \tag{3.8}
\]

and at least `c 2^(4s)` of these missing masks have ranks in

\[
                     [\,2s-C\sqrt s,\;2s+C\sqrt s\,]. \tag{3.9}
\]

The conclusion is unchanged if each rectangle is optimistically granted a
halo of `J=o(sqrt(s))` cells in the longer-chain direction.

#### Proof

Choose a uniform subset of a `2s`-element factor and let `A` be the radius of
the SCD chain containing it.  From (3.2),

\[
 \Pr\{A=a\}=\frac{v_a(2a+1)}{2^{2s}}
 =\frac{\binom{2s}{s-a}}{2^{2s}}
   \frac{(2a+1)^2}{s+a+1}.                         \tag{3.10}
\]

Uniform local Stirling estimates show that `A/sqrt(s)` converges to the
nondegenerate density

\[
                    \frac{4x^2}{\sqrt\pi}e^{-x^2},
                    \qquad x>0.                     \tag{3.11}
\]

Take two independent factor subsets.  With probability bounded below, their
chain radii lie in two disjoint intervals

\[
 A\in[\alpha\sqrt s,\beta\sqrt s],\qquad
 B\in[\gamma\sqrt s,\delta\sqrt s],
 \quad 0<\alpha<\beta<\gamma<\delta.                \tag{3.12}
\]

Conditional on radii `a<b`, a uniform cell of the chain rectangle lies
outside the central square with probability

\[
       1-\frac{(2a+1)^2}{(2a+1)(2b+1)}
       =1-\frac{2a+1}{2b+1},                         \tag{3.13}
\]

which is bounded below on (3.12).  This proves that a positive fraction of
all `2^(4s)` Boolean masks are counted in (3.7), giving (3.8).

The rank of a uniform subset of `[4s]` has standard deviation `sqrt(s)`.
Choose `C` so large that the binomial mass outside (3.9) is smaller than half
the constant just obtained.  This proves (3.9).

If a halo of width `J` is granted, the two intervals in (3.12) still have
radius gap at least `(gamma-beta)sqrt(s)>J`.  After slightly shortening the
longer-chain tails, (3.13) remains bounded below.  Hence the same argument
works for every `J=o(sqrt(s))`.  QED.

The desired band half-width `sqrt(2s omega(s))` contains (3.9).  Thus an
independent diagonal treatment of SCD rectangles leaves
`Omega(W_(4s)sqrt(s))`, not `o(W_(4s))`, central-band masks to repair.

## 4. The seam ledger is already fatal at growing depth

There are exactly

\[
             P_s=\left(\sum_a v_a\right)^2
                =\binom{2s}{s}^{\!2}                 \tag{4.1}
\]

diagonal blocks.  Since

\[
 \frac{P_s}{\binom{4s}{2s}}
       =\left(\sqrt{\frac{2}{\pi}}+o(1)\right)s^{-1/2},\tag{4.2}
\]

their mean length is only `Theta(sqrt(s))`.

If independent blocks are cut and each seam is padded by `d` entries to
preserve all length-`d+1` windows or the delay-`d` run condition, the padding
alone is

\[
 dP_s=\left(\sqrt{\frac{2}{\pi}}+o(1)\right)
          \frac d{\sqrt s}\binom{4s}{2s}.             \tag{4.3}
\]

For `d=sqrt(s omega(s))`, this is `Theta(sqrt(omega) W)`, not `o(W)`.
Therefore even a hypothetical repair of the radius imbalance inside each
rectangle would not suffice.  The diagonal blocks must themselves be spliced
into paths of average length `omega(d)`, with no physical reset at almost all
rectangle boundaries.

## 5. Consequence: what a genuine bootstrap must prove

The fixed-depth theorem can still be an ingredient, but not a black box.  A
successful multiscale theorem must simultaneously do all of the following.

1. Reuse essentially the same `W` endpoints at `Theta(sqrt(m) omega(1))`
   depths; Proposition 1 forbids independent stages.
2. Permit locally off-centre restrictions and transfer rank between
   coordinate blocks; Proposition 2 forbids a literal tensor of local bands.
3. Route the Clebsch--Gordan residual radii `|a-b|` between different product
   rectangles; Theorem 3 and Proposition 4 forbid independent diagonal
   rectangles.
4. Globalize almost all rectangle seams into long compatible paths; (4.3)
   forbids per-rectangle padding.

This identifies the missing object precisely: a **non-Cartesian
radius-transfer braid** whose cross-rectangle windows partition the residual
tails in (3.5), while its components have length
`omega(sqrt(m) omega(1))`.

Constructing such a braid would be a genuinely new growing-depth theorem.
The existence of fixed-depth block matchings, by itself, supplies neither the
radius transfers nor the seam compatibility.  Thus there is no rigorous
bootstrap from the current fixed-`J` theorem through the ordinary product or
staged mechanisms audited here.
