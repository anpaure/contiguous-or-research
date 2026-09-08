# Gate C: the endpoint-resource obstruction for earliest-empty phase packets

**Status (2026-08-23).**  Every assertion below is proved.  This note studies
only the middle-core matching problem.  It does not address ordered packet
joins or off-middle windows.

The conclusion is a sharp scope restriction on the proposed priority
construction.  If a phase packet with omitted pair `P_j` is required to keep
all of its `b-1` internal cores in the first-empty stratum for `P_j`, then its
two endpoint cores must come from a thin part of that stratum: each can double
at most two earlier pairs.  Consequently, at priority depth

\[
 r=j-1=C\log(b-1),
\]

no matching of such whole packets covers a positive fraction when

\[
 C>{1\over\log(3/2)}=2.466303462\ldots .
\]

This rules out whole-packet near-factorization at sufficiently deep
logarithmic priority levels.  It does **not** rule out stopping after an
arbitrarily slowly diverging number of pairs, which is enough to leave
`o(1)` middle density.

## 1. The stratum and its exact doubled-pair profile

Assume `b>=3` and put

\[
 m=b-1>=2,
\]

and remove the proposed omitted pair `P_j` from the `2b`-point ground set.
The remaining ground set `R` has size `2m`.  Among its `m` original pairs,
distinguish the `r=j-1` earlier pairs

\[
 P_1,\ldots,P_r,
\]

and put `n=m-r`.  Define

\[
 \mathcal S_{m,r}
 =\left\{C\in{R\choose m+1}:C\cap P_h\ne\varnothing
                  \text{ for }1\le h\le r\right\}.       \tag{1.1}
\]

Thus `S_(m,r)` is exactly the first-empty stratum for `P_j`, after `P_j`
itself has been deleted.  For `C in S_(m,r)`, let

\[
 d(C)=|\{h\le r:P_h\subseteq C\}|                         \tag{1.2}
\]

be the number of earlier pairs doubled by `C`, and write

\[
 N_d=|\{C\in\mathcal S_{m,r}:d(C)=d\}|,
 \qquad N=|\mathcal S_{m,r}|.                              \tag{1.3}
\]

### Proposition 1.1 (exact profile)

For every `0<=d<=min(r,n+1)`, with the usual convention that an invalid
binomial coefficient is zero,

\[
 \boxed{
 N_d={r\choose d}2^{r-d}{2n\choose n+1-d}.}                \tag{1.4}
\]

Consequently

\[
 N=[z^{m+1}](2z+z^2)^r(1+z)^{2n}.                          \tag{1.5}
\]

#### Proof

Choose the `d` earlier pairs which are doubled.  From each of the other
`r-d` earlier pairs choose one of its two elements.  This uses `r+d`
elements, so the unrestricted `2n` coordinates must supply

\[
 (m+1)-(r+d)=n+1-d
\]

elements.  This proves (1.4), and summing the same choices gives (1.5).
\(\square\)

The same count has a useful Motzkin description.  For every remaining
original pair put

\[
 \sigma_h(C)=|C\cap P_h|-1\in\{-1,0,1\}.
\]

Then `sum_h sigma_h(C)=1`; a zero step has two colours, and the first `r`
steps are forbidden to equal `-1`.  Formula (1.5) is the corresponding
two-coloured Motzkin enumerator.

### Proposition 1.2 (binomial local limit)

Uniformly for `r=o(sqrt(m))`,

\[
 {N_d\over N}
 ={r\choose d}\left({1\over3}\right)^d
                 \left({2\over3}\right)^{r-d}
   \exp\!\left(O\left({r^2\over m}\right)\right)          \tag{1.6}
\]

for every admissible `d`.  In particular,

\[
 \boxed{
 {N_0+N_1+N_2\over N}
 =\left({2\over3}\right)^r
   \left(1+{r\over2}+{r(r-1)\over8}\right)
   \exp\!\left(O\left({r^2\over m}\right)\right).}       \tag{1.7}
\]

#### Proof

For `0<=d<=r=o(sqrt(m))`, consecutive-factor cancellation gives

\[
 {2n\choose n+1-d}
 ={2n\choose n+1}\exp\!\left(O\left({(d+1)^2\over n}\right)\right)
 ={2n\choose n+1}\exp\!\left(O\left({r^2\over m}\right)\right), \tag{1.8}
\]

uniformly in `d`; here `n=m-r=(1-o(1))m`.  Insert (1.8) in (1.4) and sum
over `d`.  Since

\[
 \sum_d{r\choose d}2^{r-d}=3^r,
\]

division gives (1.6).  The first three binomial probabilities are

\[
 \left({2\over3}\right)^r,
 \quad {r\over2}\left({2\over3}\right)^r,
 \quad {r(r-1)\over8}\left({2\over3}\right)^r,
\]

which proves (1.7). \(\square\)

For context, if `W=binom(2b,b)`, prescribing that `P_j` is empty and that
the previous `r` pairs are nonempty gives, by the same fixed-slice estimate,

\[
 {N\over W}={1\over4}\left({3\over4}\right)^r
             \exp\!\left(O\left({r^2\over b}\right)\right). \tag{1.9}
\]

Likewise, the residual after the first `L=o(sqrt(b))` pairs has density

\[
 \left({3\over4}\right)^L
 \exp\!\left(O\left({L^2\over b}\right)\right).            \tag{1.10}
\]

Indeed, if a fixed pattern on `ell=o(sqrt(b))` coordinates has weight `s`,
then its probability in a uniform member of `binom([2b],b)` is

\[
 { {2b-\ell\choose b-s}\over {2b\choose b}}
 =2^{-\ell}\exp\!\left(O\left({\ell^2\over b}\right)\right), \tag{1.11}
\]

uniformly in `s`; this follows by expanding the `ell` falling-factorial
ratios.  Sum (1.11) over the `3^L` allowed patterns to obtain (1.10), or
over the `3^r` patterns together with the forced-empty pattern on `P_j`
to obtain (1.9).

## 2. Every safe packet consumes rare endpoint cores

A phase packet on `R` has ordered partitions

\[
 X=(x_1,\ldots,x_m),\qquad Y=(y_1,\ldots,y_m)
\]

and internal cores

\[
 C_i=\{x_i,\ldots,x_m\}\cup\{y_1,\ldots,y_i\},
 \qquad1\le i\le m.                                    \tag{2.1}
\]

Call it **`r`-safe** when every `C_i` belongs to `S_(m,r)`.

### Lemma 2.1 (position cap)

For every `r`-safe phase packet and every `1<=i<=m`,

\[
 \boxed{d(C_i)\le1+\min\{i,m+1-i\}.}                    \tag{2.2}
\]

In particular,

\[
                         d(C_1),d(C_m)\le2.             \tag{2.3}
\]

#### Proof

Fix one earlier pair `P`.  Its two elements occupy two of the `2m` slots
`x_1,...,x_m,y_1,...,y_m`.

* If both lie in `X`, safety at `C_m`, which contains only `x_m` from
  `X`, forces one of them to be `x_m`.  Hence at most one doubled earlier
  pair can be of `XX` type.
* If both lie in `Y`, safety at `C_1` similarly forces one of them to be
  `y_1`.  Hence at most one doubled earlier pair can be of `YY` type.
* If their slots are `x_a,y_c`, then the pair is absent precisely for
  `a<i<c`.  Thus safety is equivalent to `c<=a+1`, and the pair is doubled
  at `C_i` only if `c<=i<=a`.

Put `p=m-i+1` and `q=i`, the numbers of active `X` and `Y` slots in
`C_i`.  Let `alpha,beta in {0,1}` indicate whether a doubled `XX`,
respectively `YY`, earlier pair is present.  Such pairs consume two active
slots on their respective sides.  Every doubled split pair uses one further
active slot on each side, so their number is at most

\[
 \min\{p-2\alpha,q-2\beta\}.
\]

If `p<=q`, the total doubled count is at most

\[
 \alpha+\beta+p-2\alpha=p-\alpha+\beta\le p+1.
\]

If `q<=p`, it is at most `q+alpha-beta<=q+1`.  This is (2.2), and (2.3)
follows at `i=1,m`. \(\square\)

The full position cap yields a hierarchy of resource inequalities.  If
`2t<=m`, the first and last `t` cores of every safe packet all satisfy
`d<=t+1`.  Thus a matching `M` of safe packets obeys

\[
 \boxed{2t|\mathcal M|\le\sum_{d=0}^{t+1}N_d.}           \tag{2.4}
\]

The endpoint case `t=1` is already asymptotically sharp enough for the
priority-depth obstruction.

### Lemma 2.2 (there is no local extension obstruction at slow depth)

Every `C in S_(m,r)` satisfying

\[
                         r+d(C)\le m-1                 \tag{2.5}
\]

lies in an `r`-safe phase packet.  In particular, every vertex has a safe
packet extension whenever `2r<=m-1`.

#### Proof

Put `d=d(C)` and place `C` at packet position `i=d+1`.  Split every earlier
pair between one `X` slot and one `Y` slot.  For the `d` doubled pairs, use
distinct `Y` positions `1,...,d` and distinct `X` positions
`i,...,i+d-1`.  Both elements are then active at position `i`, and the
`Y` position precedes the `X` position.

For the remaining `r-d` earlier pairs, let `c` be the member belonging to
`C`.  In any order, use the consecutive position pairs

\[
 (x_t,y_{t+1}),\qquad t=i+d,i+d+1,\ldots,i+r-1,        \tag{2.6}
\]

putting `c` in `x_t` and the unselected member in `y_(t+1)`.  Such a pair
is met at every core: it switches directly from its `X` member to its `Y`
member without an empty intermediate index.  Condition (2.5) says that
the last `X` position in (2.6) is at most `m-1`, so all displayed slots
exist and are distinct.

At position `i`, the constrained labels active in these slots are exactly
the `r+d` constrained labels of `C`.  The number of unused active slots is

\[
                         m+1-r-d,
\]

exactly the number of unconstrained labels in `C`.  Fill them bijectively,
and fill the remaining inactive slots with the unconstrained labels outside
`C`.  The resulting ordered `X,Y` define a phase packet, its `i`-th core is
`C`, and every earlier pair is met throughout. \(\square\)

Thus the logarithmic obstruction below is a global endpoint-resource
obstruction, not a vanishing-degree phenomenon.

## 3. Maximum whole-packet cover fraction

Let `theta_(m,r)` be the maximum fraction of `S_(m,r)` covered by a
matching of `r`-safe whole phase packets.  Each packet contains exactly
`m` internal cores.

### Theorem 3.1 (endpoint-resource cover cap)

For all `m,r`,

\[
 \boxed{
 \theta_{m,r}\le
 \min\left\{1,{m\over2}{N_0+N_1+N_2\over N}\right\}.}   \tag{3.1}
\]

Uniformly for `r=o(sqrt(m))`, this becomes

\[
 \boxed{
 \theta_{m,r}\le
 \min\left\{1,
 {m\over2}\left({2\over3}\right)^r
 \left(1+{r\over2}+{r(r-1)\over8}\right)
 \exp\!\left(O\left({r^2\over m}\right)\right)
 \right\}.}                                             \tag{3.2}
\]

#### Proof

Distinct packets in a matching have disjoint internal cores.  By (2.3),
the two endpoint cores of every retained packet are two distinct members
of the `d<=2` subfamily.  Hence

\[
 2|\mathcal M|\le N_0+N_1+N_2.
\]

The matching covers `m|M|` vertices, proving (3.1).  Equation (3.2) is
(1.7). \(\square\)

### Corollary 3.2 (sharp logarithmic constant from the endpoint cap)

Let `r=C log m` for a fixed constant `C>0`.  Then

\[
 \boxed{
 \theta_{m,r}\le
 m^{1-C\log(3/2)+o(1)}.}                               \tag{3.3}
\]

Therefore

\[
 C>{1\over\log(3/2)}=2.466303462\ldots
 \quad\Longrightarrow\quad
 \theta_{m,r}=o(1).                                    \tag{3.4}
\]

More quantitatively, for every fixed `epsilon>0`,

\[
 r\ge {\log m+(2+\epsilon)\log\log m\over\log(3/2)}
 \quad\Longrightarrow\quad
 \theta_{m,r}=o(1),                                    \tag{3.5}
\]

provided `r=o(sqrt(m))`.

#### Proof

For `r=C log m`, the quadratic factor in (3.2) contributes only
`m^(o(1))`, as does `exp(O(r^2/m))`.  Also

\[
 (2/3)^r=m^{-C\log(3/2)}.
\]

This proves (3.3)--(3.4).  Under (3.5), the main factor in (3.2) is at
most

\[
 O\!\left(mr^2(2/3)^r\right)
 =O\!\left((\log m)^{-\epsilon}\right),
\]

and the exponential error tends to one. \(\square\)

## 4. Exact scope

The obstruction concerns **whole** packets whose complete internal core
lies in one first-empty stratum.  It gives no obstruction at
`r=o(log m)`.  In particular, one may take `r` to infinity as slowly as
desired; (1.10) then makes the unassigned residual `o(W)`, while the right
side of (3.2) need not be small.  Thus this theorem narrows, but does not
close, the earliest-empty route.

There is also a weaker exact decomposition that explains where the whole-
packet condition enters.  Fix any complete punctured Catalan factor of
`binom(R,m+1)` into `m`-core phase packets.  In one packet, a fixed earlier
pair is absent on one (possibly empty) interval of indices: a suffix for
`XX`, a prefix for `YY`, and `{a+1,...,c-1}` for slots `x_a,y_c`.
Therefore intersecting every packet with `S_(m,r)` partitions the stratum
into literal packet subpaths, at most `r+1` per original packet.  These
subpaths are not whole packets, and reassembling them while preserving FIFO
ports and all-offset cleanliness is precisely the missing step.
