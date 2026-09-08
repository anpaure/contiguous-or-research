# Two-scale common-radius promotion inside a full product SCD

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

There is an exact noncentral two-scale sector substantially larger than the
balanced-child-center sector.

Take four coordinate-disjoint Boolean blocks, fix an arbitrary SCD in each
block, decompose the first two child chains and the last two child chains by
the usual rectangle SCD, and then decompose the two resulting carrier chains
once more. Whenever the two second-scale carriers have the same radius
\(R\), their square product has a canonical promotion path

\[
 z_{R,0}\longrightarrow z_{R,1}\longrightarrow\cdots
 \longrightarrow z_{R,2R}
\]

such that, exactly and with literal child-edge labels,

\[
 \boxed{G_t(z_{R,j})=z_{R,j+t}\quad(j+t\le2R),\qquad
 G_1(G_tz_{R,j})=G_{t+1}z_{R,j}\quad(j+t<2R)}
 \tag{0.1}
\]

The head has residual radius
\(2R-j-t\), so every domain condition is exact.

This is not a partial fractional object. It is a collection of whole
symmetric chains inside one full recursively constructed SCD of the entire
four-block product. Different child-chain tuples and different carrier
radii use disjoint vertices.

For four copies of \(B_{2s}\), the number of selected middle owners is

\[
 \Theta\!\left(\frac{1}{\sqrt{s}}\binom{8s}{4s}\right).
 \tag{0.2}
\]

The older balanced-child-center sector has size
\(\Theta(s^{-3/2}\binom{8s}{4s})\), so (0.2) is larger by a factor
\(\Theta(s)\). The selected induced forced graph has one path per common
carrier radius and only an \(O(s^{-1/2})\) fraction of abstract internal
reset seams. For
\(H=o(\sqrt{s})\), a \(1-o(1)\) fraction of the selected owners have
radius at least \(H\).

The sector still has density \(o(1)\). Moreover, the reset edges obtained by
closing its paths abstractly have not been made literal Johnson edges. A
specific \(B_4\)-by-\(B_4\) calculation shows that simply applying the same
rectangle recursion to unequal carriers fails the depth-two power equation.
Thus this note proves a genuine larger positive sector, not a full-carrier
cyclic SCD.

## 1. The rectangle SCD

Let

\[
 C=(c_0<c_1<\cdots<c_{2a}),\qquad
 D=(d_0<d_1<\cdots<d_{2b})
\]

be saturated symmetric chains on disjoint coordinate sets, with \(a\ge b\).
For \(0\le k\le2b\), put

\[
\begin{aligned}
 L_k(C,D)=\;&(c_0,d_k)<(c_1,d_k)<\cdots<(c_{2a-k},d_k)\\
 &<(c_{2a-k},d_{k+1})<\cdots<(c_{2a-k},d_{2b}).
\end{aligned}
\tag{1.1}
\]

### Lemma 1.1 (exact rectangle decomposition)

The chains \(L_k(C,D)\), \(0\le k\le2b\), partition \(C\times D\).
The chain \(L_k\) begins in relative rank \(k\), ends in relative rank
\(2a+2b-k\), and has radius

\[
                         a+b-k.                       \tag{1.2}
\]

Consequently the carrier radii in \(C\times D\) are, each once,

\[
                         |a-b|,|a-b|+1,\ldots,a+b.    \tag{1.3}
\]

#### Proof

A grid point \((c_i,d_j)\) below the line \(i+j=2a\) lies on the horizontal
part of \(L_j\). A point above that line lies on the vertical part of
\(L_{2a-i}\). A point on the line is the horizontal endpoint, hence the
turn, of \(L_j=L_{2a-i}\). These alternatives are mutually exclusive, so
(1.1) partitions the rectangle.

The endpoint ranks are \(k\) and
\((2a-k)+2b=2a+2b-k\). This proves symmetry and (1.2); varying \(k\)
gives (1.3). \(\square\)

## 2. The exact common-radius rotor

Now take four child chains \(C_1,C_2,C_3,C_4\), of arbitrary radii
\(a,b,c,d\). Apply Lemma 1.1 to \(C_1\times C_2\) and to
\(C_3\times C_4\). There is one first-pair carrier \(A_R\) of radius
\(R\) for every

\[
 |a-b|\le R\le a+b,
\]

and one second-pair carrier \(B_R\) for every

\[
 |c-d|\le R\le c+d.
\]

Define

\[
 R_- =\max(|a-b|,|c-d|),\qquad
 R_+ =\min(a+b,c+d).                                  \tag{2.1}
\]

For every integer \(R\in[R_-,R_+]\), the product
\(A_R\times B_R\) is a square product of two chains of radius \(R\).
Apply (1.1) again. For \(0\le j\le2R\), its chain has center

\[
 z_{R,j}=\bigl(A_R[2R-j],B_R[j]\bigr),                \tag{2.2}
\]

where brackets denote position from the lower endpoint. Its radius is

\[
                         \rho(z_{R,j})=2R-j.           \tag{2.3}
\]

### Theorem 2.1 (power-consistent two-scale sector)

For every \(0\le t\le2R-j\), the depth-\(t\) opposite corner of the
chain centered at \(z_{R,j}\) is

\[
                         G_t(z_{R,j})=z_{R,j+t}.       \tag{2.4}
\]

In particular, for \(0\le t<2R-j\),

\[
 G_1(G_tz_{R,j})=G_{t+1}z_{R,j},\qquad
 \rho(G_tz_{R,j})=\rho(z_{R,j})-t.                   \tag{2.5}
\]

Both deletion and insertion labels agree literally, not merely by child
type.

#### Proof

The center (2.2) is the turn of the square chain. Its first \(t\) lower
edges are the edges of \(A_R\) descending from positions
\(2R-j\) to \(2R-j-t\). Its first \(t\) upper edges are the edges of
\(B_R\) ascending from positions \(j\) to \(j+t\). Taking the opposite
corner therefore changes the two carrier positions to

\[
                         (2R-j-t,j+t),
\]

which is exactly the center \(z_{R,j+t}\). At that center the remaining
lower and upper words are the literal tails of the two words just displayed.
This proves (2.4)--(2.5), including the flag identities. \(\square\)

To obtain one full SCD, not merely the displayed sector, perform the final
rectangle decomposition on every product \(A_R\times B_S\), using either
orientation when \(R\ne S\), and use Theorem 2.1 on the diagonal products
\(R=S\). All these products are vertex-disjoint and exhaust the four-chain
box. Thus Theorem 2.1 sits integrally inside one full SCD.

## 3. Exact counts and reset ledger

For fixed child radii \((a,b,c,d)\), the selected number of middle owners is

\[
\begin{aligned}
 S(a,b,c,d)
   &=\sum_{R=R_-}^{R_+}(2R+1)\\
   &=(R_++1)^2-R_-^2                                      \tag{3.1}
\end{aligned}
\]

when \(R_-\le R_+\), and is zero otherwise.

For each common \(R\), the forced map is the single path

\[
 z_{R,0}\to z_{R,1}\to\cdots\to z_{R,2R}.             \tag{3.2}
\]

Only its final owner has radius zero. If the selected sector is considered
in isolation, closing (3.2) abstractly therefore costs one reset. The exact
internal reset fraction within this child tuple is

\[
 \frac{R_+-R_-+1}{S(a,b,c,d)}
 =\frac{1}{R_-+R_++1}.                                \tag{3.3}
\]

No Johnson adjacency is claimed for the edge
\(z_{R,2R}\to z_{R,0}\). Nor is it proved that an off-diagonal carrier
owner has no forced edge entering the selected sector. Thus (3.3) is an
induced-sector path count, not a global permutation-completion theorem.
For \(R=0\), the path is one singleton; (3.3) counts its formal abstract
self-closure as one nonforced component. It does not assert a literal
positive-length seam.

Merely swapping the two top carriers does not fuse this path to fresh
owners. In the swapped frame its centers are

\[
 z'_{R,j}=\bigl(A_R[j],B_R[2R-j]\bigr)=z_{R,2R-j}.    \tag{3.3a}
\]

Thus the swapped path is exactly (3.2) in reverse; at \(z_{R,2R}\) its
first step returns to \(z_{R,2R-1}\). A useful changing-frame seam needs a
third carrier context or a non-coordinate internal-diamond move.

The number of displayed owners of radius at least \(H\) is

\[
 \sum_{R=R_-}^{R_+}(2R-H+1)_+.                         \tag{3.4}
\]

More explicitly, put

\[
 L_H=\max\!\left(R_-,\left\lceil\frac H2\right\rceil\right).
\]

Then the exact selected active count and component count for one child
tuple are

\[
 \boxed{
 S_H(a,b,c,d)=
 \begin{cases}
 (R_+-L_H+1)(R_++L_H-H+1),&L_H\le R_+,\\
 0,&L_H>R_+,
 \end{cases}}                                         \tag{3.5}
\]

and the untruncated full-sector path count is

\[
 \boxed{K(a,b,c,d)=(R_+-R_-+1)_+.}                   \tag{3.6}
\]

After retaining only owners of radius at least \(H\), the exact number of
nonempty active path components is instead

\[
 \boxed{K_H(a,b,c,d)=(R_+-L_H+1)_+.}                 \tag{3.6a}
\]

For four copies of \(B_{2s}\), the corresponding exact totals inside the
one full hierarchical SCD are

\[
 \boxed{
 |\mathcal P_{s,H}|=
 \sum_{a,b,c,d=0}^{s}
 A_s(a)A_s(b)A_s(c)A_s(d)S_H(a,b,c,d),}               \tag{3.7}
\]

and

\[
 \boxed{
 K_s=
 \sum_{a,b,c,d=0}^{s}
 A_s(a)A_s(b)A_s(c)A_s(d)K(a,b,c,d).}                 \tag{3.8}
\]

These are integral counts. Every nonterminal edge counted in (3.7) is a
top-scale cross-pair move: its deletion lies on \(A_R\), while its insertion
lies on the coordinate-disjoint carrier \(B_R\). Thus the construction
uses dense cross-quartet motion within its selected sector, rather than
trying to hide all noncentral motion in the reset set.

In the equal-child-radius case \(a=b=c=d=R_0\), retaining the particular
equal first-pair indices gives the simpler sub-sector count

\[
 (2R_0+1)^2.                                          \tag{3.9}
\]

For this sub-sector, if \(H=2h\), (3.4) equals

\[
                         (2R_0-h+1)^2,                 \tag{3.10}
\]

and if \(H=2h+1\), it equals

\[
                         (2R_0-h)(2R_0-h+1).           \tag{3.11}
\]

The ambient four-chain middle layer in that case has exact size

\[
 [z^{4R_0}](1+z+\cdots+z^{2R_0})^4
 =\frac{16R_0^3+24R_0^2+14R_0+3}{3}.                 \tag{3.12}
\]

Thus (3.9) has density

\[
                         \frac{3}{4R_0}+O(R_0^{-2}).   \tag{3.13}
\]

## 4. Boolean aggregation

Fix any SCD of \(B_{2s}\). The number of its chains of radius \(r\) is
forced by the rank census:

\[
 A_s(r)=\binom{2s}{s-r}-\binom{2s}{s-r-1}
       =\frac{2r+1}{s+r+1}\binom{2s}{s-r}.            \tag{4.1}
\]

Put \(W_s=\binom{2s}s\). For every fixed
\(0<\alpha<\beta<3\alpha\), uniform Stirling estimates on
\(\alpha\sqrt{s}\le r\le\beta\sqrt{s}\) give

\[
 \sum_{\alpha\sqrt{s}\le r\le\beta\sqrt{s}}A_s(r)
                         =\Theta(W_s).                 \tag{4.2}
\]

If all four child radii lie in this band, then

\[
 R_-\le(\beta-\alpha)\sqrt{s},\qquad
 R_+\ge2\alpha\sqrt{s}.                              \tag{4.3}
\]

The interval in (4.3) has length \(\Theta(\sqrt{s})\) and contains a
subinterval of length \(\Theta(\sqrt{s})\) on which
\(R=\Theta(\sqrt{s})\). Consequently (3.1) is \(\Theta(s)\). Equations
(4.2)--(4.3) therefore give the lower bound

\[
                         \Omega(sW_s^4)                \tag{4.4}
\]

selected owners.

Conversely, (3.1) is at most \((a+b+1)^2\). Under the chain-radius
distribution \(A_s(r)/W_s\), the second moment of \(r\) is \(O(s)\),
directly from (4.1) and the usual central-binomial tail bound. Hence the
total selected count is \(O(sW_s^4)\). Finally,

\[
 W_s^4=\Theta\!\left(s^{-3/2}\binom{8s}{4s}\right),   \tag{4.5}
\]

so (4.4)--(4.5) prove

\[
 \boxed{
 |\mathcal P_s|=
 \Theta\!\left(s^{-1/2}\binom{8s}{4s}\right).}       \tag{4.6}
\]

The same band gives \(K(a,b,c,d)=\Theta(\sqrt{s})\), while generally
\(K(a,b,c,d)=O(a+b+c+d+1)\). The first moment of the chain-radius
distribution is \(O(\sqrt{s})\), so the exact sum (3.8) satisfies

\[
 \boxed{
 K_s=\Theta(\sqrt{s}\,W_s^4)
    =\Theta\!\left(s^{-1}\binom{8s}{4s}\right).}      \tag{4.7}
\]

There is also a census-only upper audit. The terminal vertices of distinct
selected paths are distinct radius-zero chains of the full SCD of
\(B_{8s}\). Hence, exactly,

\[
 K_s\le A_{4s}(0)=\frac{1}{4s+1}\binom{8s}{4s}.       \tag{4.7a}
\]

Thus the induced reset count is \(o(\binom{8s}{4s})\) and is an
\(O(s^{-1/2})\) fraction of the selected sector. Deleting all owners of
selected radius below \(H\) costs at most \(HK_s\), because each of the
\(K_s\) paths loses at most \(H\) terminal owners. Hence

\[
 |\mathcal P_{s,H}|=|\mathcal P_s|-O(HK_s)
                   =\bigl(1-O(H/\sqrt{s})\bigr)|\mathcal P_s|, \tag{4.8}
\]

uniformly for \(H=o(\sqrt{s})\).

## 5. The first unequal-carrier failure

The diagonal condition \(R=S\) in Theorem 2.1 is exactly the condition that
the second-scale middle point be a carrier turn.

### Proposition 5.1 (corner-equality invariant)

Let \(A,B\) have radii \(R\ge S\), and give \(A\times B\) the rectangle
SCD (1.1). Every chain turn has relative rank \(2R\), whereas every middle
center has relative rank \(R+S\). Therefore a middle center is a turn if
and only if

\[
                         R=S.                          \tag{5.1}
\]

When \(R>S\), the predecessor and successor at every middle center both
come from the long carrier \(A\). Consequently any unequal-carrier
extension must solve an internal, off-centre diamond problem inside
\(A\); changing only which of the two top carriers is called first does
not create a cross-carrier corner.

For four equal Boolean blocks, any uniformly bounded library of fixed
physical pair partitions
has only \(O(s^{-1/2})\) common-radius owner density: apply the upper bound
in Section 4 to each pairing and take a finite union. Thus bounded
height-dependent re-pairing cannot make the corner construction dense. A
denser two-scale recursion needs either a growing frame library or a genuine
one-sided internal-diamond interface.

#### Proof

In (1.1), the horizontal leg ends at grid rank
\((2R-k)+k=2R\), independently of \(k\). Symmetry puts the center at rank
\(R+S\). Equality is equivalent to \(R=S\). If \(R>S\), the center occurs
strictly before the turn, so both adjacent edges lie on the \(A\)-leg.
The density statement is the union bound applied to (4.6). \(\square\)

The following literal calculation shows that the required internal
interface is not automatic in the quartet seed. Use the displayed
\(B_4\) SCD chains

\[
 \varnothing<1<14<124<1234,
 \qquad
 2'<1'2'<1'2'3'.                                     \tag{5.2}
\]

For self-containment, the first chain belongs to the full SCD

\[
\begin{array}{c}
 \varnothing<1<14<124<1234,\\
 2<12<123,\quad3<23<234,\quad4<34<134,\\
 13,\quad24,
\end{array}                                           \tag{5.2a}
\]

and the primed block carries an independent primed copy.

They have radii two and one. In their rectangle product, the \(k=0\)
chain has middle center

\[
                         X=(124,2').                   \tag{5.3}
\]

Its first two lower deletions in the long child are \(2,4\), while its
first upper insertion is \(3\). Therefore

\[
                         G_1X=(134,2').                \tag{5.4}
\]

The state \(134\) lies at the top of the radius-one chain

\[
                         4<34<134.                    \tag{5.5}
\]

Pairing (5.5) with the second chain in (5.2), and orienting the equal square
with (5.5) first, the head's first lower deletion is \(1\), whereas the
source's second lower deletion is \(4\).
Thus

\[
 \boxed{\delta_1(G_1X)=1\ne4=\delta_2(X),
        \qquad G_1^2X\ne G_2X.}                       \tag{5.6}
\]

Explicitly, the next upper label is \(1'\), and

\[
                         G_1^2X=(34,1'2'),\qquad
                         G_2X=(13,1'2').               \tag{5.7}
\]

This is the exact one-sided-tail obstruction exposed by unequal carriers:
an off-centre parent diamond can use the predecessor and successor from
one child, after which the new child's long one-sided flag need not be the
tail of the old one. Ordinary child coherence through the minimum of its
two endpoint distances does not control this amplified one-sided demand.

Equation (5.6) rules out the naive unequal-carrier extension of this
recursion in this orientation. Reversing the equal-square orientation puts
the same head at the center of the radius-zero top chain, which violates the
required residual radius two even earlier. It is not a theorem against
every contextual re-pairing.

## 6. Exact implication boundary

Proved here:

1. One full four-block product SCD contains the integral common-radius
   sector of Theorem 2.1.
2. Every selected owner satisfies the exact power equation and the literal
   lower/upper flag-tail identities at every available depth.
3. In four Boolean blocks of size \(2s\), the sector has size
   \(\Theta(s^{-1/2}\binom{8s}{4s})\), with an
   \(O(s^{-1/2})\) induced abstract reset fraction and exact component
   count (3.8).
4. For \(H=o(\sqrt{s})\), almost every owner in that band is protected
   through depth \(H\).
5. The explicit unequal \(B_4\)-carrier product fails already at depth two.

Not proved here:

1. The selected sector has vanishing density, so it does not cover
   \(W-o(W)\) middle owners.
2. The abstract path-closing resets in (3.3) are not literal Johnson edges.
3. No completion is given which makes the off-diagonal carrier products
   \(A_R\times B_S\), \(R\ne S\), power-consistent.
4. A height-dependent atlas with a genuinely growing family of re-pairings
   may evade (5.5). Such an atlas must supply the missing one-sided flag
   tails, preserve all rank resources once, and then solve the literal reset
   matching.

The common-radius construction is therefore a rigorous larger positive
sector and an exact test case for a future moving-frame recursion. It does
not establish constant one.
