# The canonical product-hook SCD has a linear clustered interior-phase overload

**Status (2026-08-21).** Every statement below is proved.  The standard
hook symmetric-chain decomposition of each product of two local Boolean
symmetric chains does give simultaneous nested targets at every upper
offset, and every post-middle word has at most one switch.  Nevertheless it
cannot be inserted into the clustered schedules with `o(W_b)` alteration.
For every

\[
 \sqrt b\le q\le 2\sqrt b,
 \qquad W_b={2b\choose b},
\]

the hooks put `Omega(W_b)` rank-`(b+q)` targets in the interior clustered
phase colors, while all such colors together have capacity only
`O(W_b/sqrt b)`.  Thus even the abstract occurrence-token relaxation forces
`Omega(W_b)` deletions or non-hook reroutings at one such offset, and the
summed unchanged-hook deficit on this offset window is
`Omega(sqrt b W_b)`.

There are two useful side ledgers.  Deleting all equal-bottom chain
rectangles throughout a DCC band costs `(3/4+o(1))W_b`, so that loss is not
aggregate-negligible.  By contrast, deleting hook targets whose middle
source is outside the genuine central payload interval costs `o(W_b)` in
total.

This is a barrier only to the **canonical hook lift** (and to any repair that
changes only `o(W_b)` of its offset-`q` incidences).  It is not a no-go for a
different product-SCD, adaptive within-rectangle paths, the proved
equal-bottom flow relaxation, or a general coherent order-bank
construction.  Tight-cycle-factor existence is not used in the obstruction;
physical interpretation of the stated clustered token capacities remains
conditional on the same growing-rank factor hypothesis as the product
route.

## 1. Local chains and the canonical hooks

Let `b=2h+1` be odd.  Fix symmetric-chain decompositions of the Boolean
lattices on disjoint `b`-sets `A,B`.  Put

\[
 c_d={b\choose d}-{b\choose d-1},
 \qquad 0\le d\le h,                               \tag{1.1}
\]

with `binom(b,-1)=0`.  There are exactly `c_d` local chains with bottom
rank `d`.

Pair an `A`-chain of bottom `a` and edge-length `p=b-2a` with a `B`-chain
of bottom `c` and edge-length `s=b-2c`.  Index their product grid by
`(i,j) in [0,p] times [0,s]`.  The global rank of `(i,j)` is
`a+c+i+j`, and its middle diagonal is

\[
 i+j=K,
 \qquad K=b-a-c={p+s\over2}.                       \tag{1.2}
\]

If `a>=c`, so `p<=s`, use the vertical-then-horizontal hooks

\[
 C_k:(k,0),(k,1),\ldots,(k,s-k),
      (k+1,s-k),\ldots,(p,s-k),
 \quad 0\le k\le p.                               \tag{1.3}
\]

If `a<c`, transpose this construction:

\[
 C_k:(0,k),(1,k),\ldots,(p-k,k),
      (p-k,k+1),\ldots,(p-k,s),
 \quad 0\le k\le s.                               \tag{1.4}
\]

The equality case is oriented by (1.3).  Other choices on equal-bottom
rectangles do not affect the obstruction below.

### Lemma 1.1 (exact hook geometry)

The chains (1.3), respectively (1.4), partition the whole product grid.
Every chain starts at relative rank `k`, ends at relative rank `p+s-k`, and
hence is symmetric.  It has one middle vertex of global rank `b`.

If `a>=c`, the middle source on `C_k` has local `A`-rank

\[
 r=a+k                                                   \tag{1.5}
\]

and the complete word above the middle is

\[
 B^{a-c}A^{b-2a-k}.                                  \tag{1.6}
\]

If `a<c`, the middle source has local `A`-rank

\[
 r=b-c-k                                               \tag{1.7}
\]

and the complete word above the middle is

\[
 A^{c-a}B^{b-2c-k}.                                  \tag{1.8}
\]

#### Proof

For (1.3), a cell `(i,j)` with `j<=s-i` lies on the vertical part of the
unique hook `C_i`; if `j>s-i`, it lies on the horizontal part of the unique
hook `C_(s-j)`.  This proves partition and uniqueness.  The endpoint ranks
are `k` and `p+s-k`.  Because `p<=s`, the middle point is
`(k,K-k)`.  From there the hook takes `s-K=a-c` vertical `B`-steps and then
`p-k=b-2a-k` horizontal `A`-steps, proving (1.5)--(1.6).  Transposing the
same argument proves (1.4) and (1.7)--(1.8).  \(\square\)

Thus, for a central source split `r` and `q<=min(r,b-r)`, every length-`q`
hook prefix is individually a subword of a cyclic clustered word
`A^rB^(b-r)`.  The issue is not individual prefix embeddability; it is the
multiplicity of the required phase colors.

## 2. Exact offset and color ledger

For `q>=1`, define

\[
 N_{a,c}^{(q)}=
 \left[
 b-2\max(a,c)+1-\bigl(q-|a-c|\bigr)_+
 \right]_+ .                                      \tag{2.1}
\]

This is the exact number of hooks in the rectangle which reach rank
`b+q`.  Let `z` denote the number of `A`-steps among the first `q`
post-middle steps.  Lemma 1.1 gives the rectangle-constant color

\[
 z_q(a,c)=
 \begin{cases}
  (q-a+c)_+,&a\ge c,\\
  \min(q,c-a),&a<c.
 \end{cases}                                      \tag{2.2}
\]

Indeed, for `a>=c` the active indices are

\[
 0\le k\le\min(b-2a,b-a-c-q),                     \tag{2.3}
\]

and for `a<c` the analogous bound is
`0<=k<=min(b-2c,b-a-c-q)`.  Counting these indices gives (2.1), and
(1.6)--(1.8) give (2.2).

Let `H_(r,q,z)` be the number of canonical hook targets at offset `q`,
color `z`, whose middle source has split `r`.  The exact profile ledger is

\[
\begin{aligned}
H_{r,q,z}
={}&\sum_{\substack{a\ge c;
 a\le r\le\min(b-a,b-c-q)\\
 z=(q-a+c)_+}}c_ac_c\\
&+\sum_{\substack{a<c;
 \max(c,a+q)\le r\le b-c\\
 z=\min(q,c-a)}}c_ac_c .                           \tag{2.4}
\end{aligned}
\]

Summing over source profiles gives the following simpler global ledger:

\[
\begin{aligned}
 H_{q,0}
  &=\sum_{\substack{a>c\\a-c\ge q}}
       c_ac_cN_{a,c}^{(q)},\\
 H_{q,q}
  &=\sum_d c_d^2N_{d,d}^{(q)}
    +\sum_{\substack{a<c\\c-a\ge q}}
       c_ac_cN_{a,c}^{(q)},                        \tag{2.5}\\
 H_{q,z}
  &=\sum_{\substack{a<c\\c-a=z}}
       c_ac_cN_{a,c}^{(q)}
    +\sum_{\substack{a<c\\c-a=q-z}}
       c_ac_cN_{a,c}^{(q)},
       \qquad 1\le z\le q-1.
\end{aligned}
\]

The second sum in the last line is the transposed `a>c` contribution.  In
particular, the exact total interior-color demand is

\[
 \boxed{
 H_q^{\rm int}
 =2\sum_{\substack{0\le a<c\le h\\c-a<q}}
      c_ac_cN_{a,c}^{(q)}.}                        \tag{2.6}
\]

Because the product hooks form a symmetric-chain decomposition of the
whole `2b`-cube,

\[
 \sum_{z=0}^qH_{q,z}={2b\choose b+q}.              \tag{2.7}
\]

Equations (2.1)--(2.7) are identities, not asymptotic estimates.

## 3. The clustered interior capacity

At source split `r`, put

\[
 L_r={b\choose r}^2.
\]

For `q<=min(r,b-r)`, a cyclic length-`q` segment of the clustered phase
word `A^rB^(b-r)` has exactly `z` letters of type `A` at two phase origins
when `1<=z<=q-1`.  Hence the occurrence-token capacity of every interior
color is

\[
 Q_{r,q,z}={2\over b}L_r,
 \qquad 1\le z\le q-1.                             \tag{3.1}
\]

Consequently, on any genuine central payload interval `I` on which
`q<=min(r,b-r)`, all interior colors together have capacity at most

\[
 \boxed{
 Q_q^{\rm int}(I)
 ={2(q-1)\over b}\sum_{r\in I}L_r
 \le {2(q-1)\over b}W_b.}                          \tag{3.2}
\]

The equality `sum_r binom(b,r)^2=binom(2b,b)` is Vandermonde's identity.

### Theorem 3.1 (linear interior-phase overload)

For a source-rank interval `I`, write

\[
 H_q^{\rm int}(I)=
 \sum_{r\in I}\sum_{z=1}^{q-1}H_{r,q,z}.           \tag{3.2a}
\]

There is an absolute constant `eta>0` such that, for every sufficiently
large odd `b` and every integer

\[
 \lceil\sqrt b\rceil\le q\le\lfloor2\sqrt b\rfloor,
\]

the canonical product hooks satisfy

\[
 H_q^{\rm int}\ge\eta W_b.                         \tag{3.3}
\]

whereas

\[
 Q_q^{\rm int}(I)=O(W_b/\sqrt b).                  \tag{3.4}
\]

If `H/sqrt b -> infinity` and the genuine payload interval is
`I=[H+2,b-H-2]`, the stronger restricted statement

\[
 H_q^{\rm int}(I)\ge\eta W_b                       \tag{3.4a}
\]

holds: all hook targets used in the proof of (3.3) have their middle source
in `I`.

#### Proof

Write a bottom rank as `h-k`.  Uniformly for `2sqrt b<=k<=6sqrt b`,

\[
 c_{h-k}
 ={b\choose h-k}{2k+2\over h+k+2}
 \ge \gamma\,{k\over b}{b\choose h}               \tag{3.5}
\]

for an absolute `gamma>0`.  To see this without invoking a local limit
theorem, write

\[
 {{b\choose h-k}\over{b\choose h}}
 =\prod_{j=0}^{k-1}{h-j\over h+j+2}.
\]

For `k<=6sqrt b`, `log(1-x)>=-2x` applied to the factors gives a positive
absolute lower bound for this product; the rational factor in (3.5) is at
least a constant times `k/b`.

For the chosen `q`, take integers

\[
 2q\le j\le {9q\over4},
 \qquad {5q\over2}\le i\le {11q\over4},            \tag{3.6}
\]

and set `a=h-i`, `c=h-j`.  Rounding the four endpoints inward changes only
absolute constants.  There are `Omega(q^2)` such pairs, and they satisfy

\[
 0<c-a=i-j<q,
 \qquad
 N_{a,c}^{(q)}=i+j+2-q\ge3q.                       \tag{3.7}
\]

Each is therefore an interior-color term of (2.6).  Equations
(3.5)--(3.7) give

\[
 H_q^{\rm int}
 \ge \gamma_1 {q^5\over b^2}{b\choose h}^2
 \ge \gamma_2\sqrt b\,{b\choose h}^2.             \tag{3.8}
\]

The standard Stirling bounds yield

\[
 \sqrt b\,{b\choose h}^2=\Theta\left({2b\choose b}\right), \tag{3.9}
\]

which proves (3.3).  Equation (3.4) follows immediately from (3.2).

For the displayed pairs, an active `a<c` hook has source splits

\[
 h-i+q\le r\le h+j+1.
\]

They are within `O(sqrt b)` of the center, hence lie in `I` when
`H/sqrt b -> infinity`.  \(\square\)

### Corollary 3.2 (the canonical hook lift fails at linear scale)

At every offset in Theorem 3.1, any injection of unchanged hook paths into
clustered occurrence tokens must delete or reroute at least

\[
 H_q^{\rm int}(I)-Q_q^{\rm int}(I)=\Omega(W_b)     \tag{3.10}
\]

target incidences.  Moreover

\[
 \sum_{q=\lceil\sqrt b\rceil}^{\lfloor2\sqrt b\rfloor}
 \bigl(H_q^{\rm int}(I)-Q_q^{\rm int}(I)\bigr)_+
 =\Omega(\sqrt b\,W_b).                           \tag{3.11}
\]

#### Proof

The number of `A`-steps in a hook prefix is intrinsic, so an unchanged path
of interior color must consume an interior token.  Sum the necessary
capacity inequalities over `r` and `1<=z<=q-1`, then use Theorem 3.1.
There are `Theta(sqrt b)` offsets in the displayed interval, and the bound
is uniform.  \(\square\)

Thus the one-switch shape is not by itself sufficient.  The clustered word
has only two origins for each interior color, whereas a positive fraction of
the canonical hooks switch within `q=Theta(sqrt b)` steps.

## 4. Equal-bottom and payload-boundary ledgers

The exact number of offset-`q` targets in equal-bottom rectangles is

\[
 E_{b,q}=\sum_{d=0}^h c_d^2[b-2d-q+1]_+.           \tag{4.1}
\]

The hook SCD includes these targets.  If instead they are all discarded,
their full aggregate cost is

\[
\begin{aligned}
 \sum_{q\ge1}E_{b,q}
 &= {1\over2}\sum_{d=0}^h
       c_d^2(b-2d)(b-2d+1)\\
 &=\left({3\over4}+o(1)\right)W_b.                \tag{4.2}
\end{aligned}
\]

The same asymptotic holds with the sum truncated at any
`H` satisfying `H/sqrt b -> infinity` and `H=o(b^(2/3))`.

For completeness, put `d=h-k`.  Uniformly on `k=O(b^(1/2+o(1)))`,

\[
 {c_{h-k}\over{b\choose h}}
 ={4k\over b}e^{-2k^2/b}(1+o(1))                  \tag{4.3}
\]

away from the negligible `k=o(sqrt b)` endpoint in the associated Riemann
sum.  Since `b-2d=2k+1`, (4.2) follows from

\[
 32\int_0^\infty x^4e^{-4x^2}\,dx
 ={3\sqrt\pi\over8},
 \qquad
 {{b\choose h}^2\sqrt b\over W_b}\longrightarrow{2\over\sqrt\pi}. \tag{4.4}
\]

The Gaussian product bound used in (3.5), with a matching upper bound,
makes the range `k>H/2` negligible when `H/sqrt b -> infinity`; this proves
the truncated assertion.

Finally, each middle source vertex has at most one hook descendant at every
offset.  Therefore deleting every target whose middle source split is
outside

\[
 I=[H+2,b-H-2]
\]

costs at most

\[
 H\sum_{r\notin I}{b\choose r}^2=o(W_b)            \tag{4.5}
\]

over all `1<=q<=H`, because `H=o(b)` and the omitted local binomial layers
have entropy `o(b)`.  Hence payload boundaries are harmless, while
equal-bottom deletion and the canonical-hook interior overload are not.

## 5. Exact remaining scope

The canonical hooks solve simultaneous nestedness and labelled target
simplicity before token assignment: they form an actual symmetric-chain
decomposition of the product grid.  Theorem 3.1 shows that their switch-time
distribution is macroscopically incompatible with the clustered phase
palette.  This obstruction occurs before cyclic-order labels, factor-order
coinstantiation, seams, or cross-offset physical reuse enter.

It leaves open constructions that redistribute switch times across product
rectangles, use nonconstant matchings, mix several product-SCDs, or exploit
the integral equal-bottom shift flow together with unequal-bottom
augmentations.  Any successful clustered construction must change a linear
number of the canonical hook incidences around `q=Theta(sqrt b)`; merely
choosing phase origins for the existing hooks cannot work.
