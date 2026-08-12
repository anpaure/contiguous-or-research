# Cross-half parity matchings and logarithmic-block packet near-tilings

Date: 2026-07-26

## 0. Outcome

Let `A,B` be disjoint `d`-sets.  On the `k`-subsets of `A union B`, let
`G_(d,k)` contain exactly the Johnson edges which exchange one coordinate
of `A` with one coordinate of `B`.  Its bipartition is the parity of
`|X cap A|`.

The parity matching question has a complete positive answer.

### Theorem 0.1

For every `d` and `0<=k<=2d`, `G_(d,k)` has a matching saturating its
smaller parity shore.  If `k` is odd the matching is perfect.  If
`k=2j` is even, it leaves exactly

\[
                         \binom dj                         \tag{0.1}
\]

vertices unmatched, all on the parity shore `|X cap A|=j mod 2`.

This realizes exactly the absolute parity imbalance

\[
 \left|[x^k](1-x^2)^d\right|
 =\begin{cases}
 0,&k\text{ odd},\\
 \binom d{k/2},&k\text{ even}.
 \end{cases}                                             \tag{0.2}
\]

Tensoring these local matchings gives the requested owner construction.
Partition `[2m]` into blocks `D_i=A_i dotcup B_i` of size `2d`, with a
residual set of size less than `2d`.  For suitable

\[
 d=\Theta(\log m)\text{ odd},
 \qquad \sqrt m\ll H=o(r),
 \qquad r=o(m/\log m),                                  \tag{0.3}
\]

where `r` is a power of two, there is a deterministic owner-disjoint
near-tiling of the middle layer by physical `Q_r` packets such that every
active axis exchanges one coordinate across one of the fixed halves
`A_i|B_i`.  Its owner leave is

\[
                         2^{m+o(m)}=o(W/H),
 \qquad W=\binom{2m}m.                                  \tag{0.4}
\]

This is an owner theorem, not `CPM`.  A crucial design distinction remains.

* If the same local bijection `A_i to B_i` is used at every local rank,
  all packet axes lie in one global perfect matching.  The old fixed-frame
  Gaussian obstruction survives unchanged.
* One may instead vary the bijection with the local rank so that the union
  of allowed axes in each `2d`-block is `K_(d,d)`.  Then there is no common
  coordinate component finer than the logarithmic block.  The exact
  surviving invariant is full-block count for lower windows (empty-block
  count for upper windows).  Because `d to infinity`, this invariant is
  too sparse to reproduce a positive-mass Gaussian Hall cut: its
  source-target standardized shift is `O_A(sqrt(d)2^(-d))=o(1)`.

No other all-depth capacity theorem is proved here.  Thus the parity
matching and owner near-tiling are complete, while simultaneous colored
target coverage remains open.

## 1. Exact parity imbalance

Let

\[
 E_{d,k}=\#\{X:|X|=k,\ |X\cap A|\text{ even}\},
\]

and define `O_(d,k)` analogously.  Then

\[
\begin{aligned}
 E_{d,k}-O_{d,k}
 &=\sum_a(-1)^a\binom da\binom d{k-a}\\
 &=[x^k](1-x)^d(1+x)^d\\
 &=[x^k](1-x^2)^d.                                    \tag{1.1}
\end{aligned}
\]

Consequently the shores are equal for odd `k`, while for `k=2j`

\[
                         E_{d,2j}-O_{d,2j}
                         =(-1)^j\binom dj.             \tag{1.2}
\]

## 2. A matching with exactly the forced leave

Fix a bijection

\[
                         \pi:A\longrightarrow B       \tag{2.1}
\]

and an order on its `d` pairs `{a,pi(a)}`.  For a `k`-set `X`, call a
pair

* empty if neither endpoint lies in `X`;
* full if both endpoints lie in `X`; and
* split if exactly one endpoint lies in `X`.

The empty/full/split status vector partitions the whole local layer into
orientation cubes.  A status class with `s` split pairs is a `Q_s`.

If `s>=1`, toggle the first split pair in the fixed pair order.  The first
split pair remains the first split pair after the toggle, so this is a
fixed-point-free involution of the status class.  Its two endpoints differ
by exchanging one `A` coordinate with one `B` coordinate, hence form an
edge of `G_(d,k)`.  It also reverses the parity of `|X cap A|`.

Thus every status class with a split pair is perfectly matched.  A class
with no split pair is a singleton, necessarily with even `k=2j`; it is a
union of exactly `j` full pairs.  There are `binom(d,j)` such vertices,
and every one has

\[
                         |X\cap A|=j.                  \tag{2.2}
\]

They lie on precisely the majority shore specified by (1.2).  This proves
Theorem 0.1.  The cases `k=0,2d` are included: the smaller shore is empty
and the unique vertex is the forced unmatched singleton.

Summed over every local rank, the unmatched local states are exactly the
unions of the `d` fixed pairs.  Therefore their total number is

\[
                         2^d,                          \tag{2.3}
\]

while the matched local states number `4^d-2^d`.

## 3. The global packet near-tiling

Write

\[
 [2m]=R_0\mathbin{\dot\cup}
       D_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}D_c,
 \qquad
 D_i=A_i\mathbin{\dot\cup}B_i,
 \qquad |A_i|=|B_i|=d,                                \tag{3.1}
\]

where

\[
                         c=\left\lfloor{m\over d}\right\rfloor,
 \qquad |R_0|=2m-2dc<2d.                              \tag{3.2}
\]

For every block `i` and local rank `k`, choose a bijection

\[
                         \pi_{i,k}:A_i\longrightarrow B_i              \tag{3.3}
\]

and use the matching from Section 2.  Call a local subset *eligible* if
it is matched.  Every eligible local state belongs to one unique local
edge, and that edge crosses `A_i|B_i`.

For a middle owner `X`, let `E(X)` be its eligible block set.  If
`|E(X)|>=r`, choose its first `r` eligible blocks.  Freeze the exact local
state outside those blocks and vary each active local state along its
unique matched edge.  This gives a physical `Q_r` packet.

Eligibility and the first-`r` index set are unchanged by every active
toggle.  Hence two such packets which meet have the same active indices
and the same frozen exterior, and are equal.  The packets therefore
partition every middle owner with at least `r` eligible blocks.

Every active direction is one of the cross-half edges from Section 2, so
all `r` axes of every retained packet cross a fixed local half boundary.

## 4. Owner-leave estimate

Ignore the global rank condition.  The residual coordinates contribute at
most `2^|R_0|`.  Choose `e<r` eligible blocks; each has
`4^d-2^d` states, and each ineligible block has `2^d` states.  Therefore

\[
\begin{aligned}
 L_r
 &\le2^{|R_0|}\sum_{e<r}\binom ce
          (4^d-2^d)^e(2^d)^{c-e}\\
 &=2^{|R_0|+dc}
   \sum_{e<r}\binom ce(2^d-1)^e.                      \tag{4.1}
\end{aligned}
\]

Since `2m=2dc+|R_0|`,

\[
                         |R_0|+dc=m+{|R_0|\over2}\le m+d.     \tag{4.2}
\]

If

\[
                         r=o(c),
 \qquad
                         r\bigl(d+\log(c/r)\bigr)=o(m),        \tag{4.3}
\]

then

\[
 \log_2\sum_{e<r}\binom ce(2^d-1)^e=o(m).             \tag{4.4}
\]

Thus

\[
                         L_r\le2^{m+o(m)}.             \tag{4.5}
\]

As `W=2^(2m-o(m))`, this is exponentially `o(W/H)` for every polynomial
height `H`.

For example, take `d` to be the nearest odd integer above
`C log_2 m` for any fixed `C>0`, choose a
power of two `r` with

\[
                         \sqrt m\,\omega(m)\ll r\ll {m\over\log m},
 \tag{4.6}
\]

and then choose

\[
                         \sqrt m\,\omega(m)\le H=o(r).          \tag{4.7}
\]

The verified nonlinear `Q_r` compiler may be installed in every retained
packet and works simultaneously through every `q<=H`.

## 5. Avoiding the hidden fixed frame

If `pi_(i,k)` is independent of `k`, then all active axes over all packet
owners lie in the single global perfect matching

\[
                         \bigcup_i\pi_i                \tag{5.1}
\]

(plus an arbitrary matching on the residual coordinates).  The
construction is then only the deterministic fixed-frame packet tiling in
different notation, and the known Gaussian Hall deficit applies.

This is avoidable at the owner level.  Label both halves of a block by
`Z/dZ`, take `d` odd, and put

\[
                         \pi_{i,k}(a_j)=b_{j+k\pmod d}.          \tag{5.2}
\]

As `k` ranges over `1,...,2d-1`, these bijections contain every cyclic
shift.  Moreover every residue occurs at an odd local rank: offset zero
occurs at `k=d`, and for a nonzero offset one of `k` and `k+d` is odd.
At an odd local rank, any prescribed `pi_(i,k)`-pair occurs as the sole
split pair of a suitable status class, so it is actually used by the
matching from Section 2.  Therefore the used-edge union is `K_(d,d)`.
Hence the common coordinate union graph in one macroblock is connected
and there is no common coordinate component finer than `D_i`.

This variation is compatible with the packet partition: toggling a local
edge preserves its local rank `k`, so both endpoints use the same
`pi_(i,k)` and the same local matching.

It does not prove colored target coverage.  In particular, status
statistics relative to the rank-dependent pairings, or another
multitype Hall cut, still require a separate audit.

## 6. The surviving macroblock invariant is asymptotically weak

Every active direction stays inside one macroblock `D_i`.  Therefore the
number of full macroblocks is invariant between a middle source and its
lower intersection; dually, empty macroblocks are invariant on the upper
side.

This is the exact analogue of the quartet invariant, but its Gaussian
strength disappears when `d to infinity`.  Put

\[
                         b=2d,
 \qquad c={2m\over b}+O(1).
\]

At the middle source rank, the expected number of full macroblocks is

\[
                         \lambda_X=c2^{-b}.            \tag{6.1}
\]

At lower rank `m-q`, with `q=A sqrt(m)` and
`p=1/2-A/(2sqrt(m))+O(m^(-1))`, it is

\[
\begin{aligned}
 \lambda_T
 &=cp^b\\
 &=\lambda_X\exp\left(-{Ab\over\sqrt m}
                 +o\left({b\over\sqrt m}\right)\right).
                                                               \tag{6.2}
\end{aligned}
\]

The shift in units of the natural standard deviation is therefore at
most

\[
 {\lambda_X-\lambda_T\over\sqrt{\lambda_X}}
 =O_A\left({b\sqrt{c2^{-b}}\over\sqrt m}\right)
 =O_A\left(\sqrt b\,2^{-b/2}\right)
 =O_A\left(\sqrt d\,2^{-d}\right)=o(1).               \tag{6.3}
\]

If `lambda_X` tends to zero, both source and target have no full block
with probability `1-o(1)`; if it is bounded or diverges, (6.3) says their
central full-block profiles are contiguous.  Since the total source to
target layer ratio tends to `e^(A^2)>1`, this invariant does not yield a
positive-mass target profile with fewer middle sources.

Thus the specific full-block Gaussian obstruction which forced dense
crossing at block size four does not survive at logarithmic block size.
This does not exclude a different rank-dependent status or chronology
cut.

## 7. Exact frontier

Proved:

1. `G_(d,k)` has a matching saturating its smaller parity shore, with
   exactly the forced leave (0.1).
2. The tensor construction gives an exponentially accurate owner
   near-tiling by `Q_r` packets.
3. Every packet axis crosses its prescribed logarithmic-block half.
4. Rank-dependent cyclic-shift pairings eliminate a common fixed frame
   below the macroblock scale.
5. The surviving full/empty macroblock invariant is too weak to reproduce
   the positive-mass quartet Hall cut.

Open:

1. a simultaneous target-capacity theorem for the rank-dependent local
   matching mosaic;
2. a common all-depth selection of local matching resolutions and packet
   compilers with `o(W)` aggregate target holes; and
3. `CPM` itself.
