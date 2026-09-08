# Gate C: exact coherent-tour orbit moments and the product-regeneration barrier

**Status (2026-09-05).**  Every assertion below is proved.  This note does
not prove the completed-tour selector.  It gives the exact one- and
two-target laws of a uniformly relabelled completed tour at every band
offset, specializes them to explicit middle-layer intersection moments,
and proves that Bernoulli-product regeneration of whole tours becomes
impossible after deleting only `Theta(log(b)/b)` of the middle layer.
Thus a successful near-factor argument must preserve a highly correlated
residual or use a global resolution/absorber; a product-residual nibble
cannot reach positive coverage.

Throughout, `b>=5` is odd,

\[
 n=2b,\qquad W={2b\choose b},\qquad q=b(b-1),\qquad m=b^2.
 \tag{0.1}
\]

Partition the ground set as

\[
 \Omega=\mathbb Z_b\times\mathbb F_2,
 \qquad P_j=\{j^0,j^1\}.                                \tag{0.2}
\]

Here is a complete definition of the zero-state completed word `w`.  At
packet `s in {0,...,b-1}`, start with the FIFO pair queue

\[
 P_s,P_{s+1},\ldots,P_{s-1}                              \tag{0.3}
\]

(indices modulo `b`).  For `k=1,...,b-1`, emit the member of
`P_(s+k)` opposite to its currently selected member and eject the queue
front `P_(s+k-1)`.  The special front `P_s` retains its selected member;
every later ejected front changes its selected member to the opposite one
emitted at the preceding step.  At the last step emit the retained selected
member of `P_s`, eject `P_(s-1)`, and perform that pair's change.  Initially
select `j^0` in every pair.  Every coordinate is nonspecial in `b-1`
packets, hence is flipped an even number of times; the state and queue close
after `b` packets.  The `b^2` emitted labels form the cyclic word `w`.

We record the gap proof because it is what makes every support below
literal.  Number output positions from one.  The occurrence of pair
`P_j` in packet `s` is at

\[
 t_s(j)=s(b-1)+j+b\mathbf1_{\{s\ge j\}}.                \tag{0.4}
\]

Successive occurrences of `P_j` have gap `b-1`, except from packet
`j-1` to packet `j`, where the gap is `2b-1`.  The two members of the
pair alternate at every nonspecial packet, while the member at the special
packet is retained.  Separating the two label subsequences therefore gives

\[
\begin{array}{c|c}
\text{successive equal-label gap}&\text{number over the whole word}\\ \hline
2b-2&b(b-2)\\
2b-1&b\\
4b-3&b.
\end{array}                                             \tag{0.5}
\]

In particular every cyclic interval of at most `2b-2` positions contains
distinct ground labels.

For an integer `h` with `2<=b+h<=2b-3`, put

\[
 \mathcal S_h=\bigl\{\{w_i,w_{i+1},\ldots,w_{i+b+h-1}\}:
                  i\in\mathbb Z_m\bigr\},
 \qquad N_h={2b\choose b+h},                            \tag{0.6}
\]

where repetitions among the displayed window sets are identified.  The
gap theorem makes every displayed window a genuine set.  Its distinct
support size is

\[
 \boxed{
 d_h:=|\mathcal S_h|=
 \begin{cases}
 b(b+h+1),&h<0,\\
 b^2,&h\ge0.
 \end{cases}}                                           \tag{0.7}
\]

Here is the support count.  Write \(\ell=b+h\).  If
\(2\le\ell\le b-2\), a window which stays inside one packet has
\(\ell\) consecutive pair indices.  For each of the \(b\) such cyclic
pair intervals, direct substitution in (0.4) shows that all its
noncrossing starts give exactly the two complementary transversal choices.
There are therefore \(2b\) distinct noncrossing targets.  A window which
crosses a packet seam uses, for some \(1\le r\le\ell-1\), the last \(r\)
indices of packet \(s\) and the first \(\ell-r\) indices of packet \(s+1\):

\[
 \{s-r+1,\ldots,s\}\ \cup\
 \{s+2,\ldots,s+\ell-r+1\}.                            \tag{0.8}
\]

Its pair support together with the emitted bits recovers \((s,r)\);
these \(b(\ell-1)\) targets are distinct and none has a consecutive pair
support.  Hence there are \(2b+b(\ell-1)=b(\ell+1)\) targets.  At
\(\ell=b-1\), and throughout \(b-1\le\ell\le2b-3\), equality of two
window sets forces equality of their two successive pair-occupancy
boundaries and then equality of their starts.  Thus all \(b^2\) starts
are distinct.  This proves (0.7), including agreement of its two formulas
at \(h=-1\).

We sample a uniformly relabelled tour by taking a uniform
`pi in S_(2b)` and replacing every target `A` by `pi A`.  This retains
parameter multiplicities and therefore avoids any unproved assertion
about the setwise stabilizer of a tour support.

## 1. Complete one- and two-target orbit laws

For one rank, define the ordered internal Johnson census

\[
 M_{h,r}=|\{(A,B)\in\mathcal S_h^2:A\ne B,
                       |A\setminus B|=r\}|,
 \qquad
 v_{h,r}={b+h\choose r}{b-h\choose r}.                 \tag{1.1}
\]

### Theorem 1.1 (same-rank law)

For a fixed `(b+h)`-set `A`,

\[
 \Pr(A\in\pi\mathcal S_h)={d_h\over N_h}.             \tag{1.2}
\]

For fixed distinct `(b+h)`-sets `A,B` at Johnson distance `r`,

\[
 \boxed{
 \Pr(A,B\in\pi\mathcal S_h)
 ={M_{h,r}\over N_hv_{h,r}}.}                          \tag{1.3}
\]

#### Proof

The symmetric group is transitive on the rank-`b+h` layer, and on its
ordered pairs at every fixed Johnson distance.  One support contributes
`d_h` one-target incidences and `M_{h,r}` ordered distance-`r`
incidences.  The ambient numbers are respectively `N_h` and
`N_hv_{h,r}`.  Double counting the relabellings proves (1.2)--(1.3).
\(\square\)

There is an equally exact mixed-rank version.  For offsets `h,k`, put

\[
 M_{h,k,x}=|\{(A,B)\in\mathcal S_h\times\mathcal S_k:
                         |A\cap B|=x\}|,                \tag{1.4}
\]

\[
 v_{h,k,x}={b+h\choose x}{b-h\choose b+k-x}.           \tag{1.5}
\]

For a fixed rank-`b+h` target `A`, the latter is the number of
rank-`b+k` targets `B` with intersection size `x`.  The same double count
therefore gives

\[
 \boxed{
 \Pr(A\in\pi\mathcal S_h,\ B\in\pi\mathcal S_k)
 ={M_{h,k,x}\over N_hv_{h,k,x}}.}                       \tag{1.6}
\]

Equations (1.3) and (1.6) are the complete two-target laws.  No scalar
codegree estimate loses information: inserting the finite within-word
censuses gives every covariance of the relabelled support indicators.

## 2. Exact intersection and hole moments

Let `pi,sigma` be independent uniform relabellings and set

\[
 Y_h=|\pi\mathcal S_h\cap\sigma\mathcal S_h|.           \tag{2.1}
\]

### Corollary 2.1 (two-tour intersection moments)

\[
 \boxed{\mathbb EY_h={d_h^2\over N_h},}                 \tag{2.2}
\]

\[
 \boxed{
 \mathbb E(Y_h)_2={1\over N_h}
       \sum_{r\ge1}{M_{h,r}^2\over v_{h,r}}.}           \tag{2.3}
\]

#### Proof

For (2.2), sum the square of (1.2) over the `N_h` targets.  For (2.3),
sum the square of (1.3) over the `N_hv_{h,r}` ordered ambient pairs at
each positive distance. \(\square\)

Now take `t` independent uniformly relabelled tours and let `X_h` be the
number of rank-`b+h` targets missed by all their supports.  Then

\[
 \boxed{
 \mathbb EX_h=N_h\left(1-{d_h\over N_h}\right)^t,}      \tag{2.4}
\]

and

\[
 \boxed{
 \mathbb E(X_h)_2=N_h\sum_{r\ge1}v_{h,r}
 \left(1-{2d_h\over N_h}
       +{M_{h,r}\over N_hv_{h,r}}\right)^t.}            \tag{2.5}
\]

Indeed one tour misses a fixed ordered pair at distance `r` with the
probability inside parentheses.  This proves (2.5) after summing over all
ordered pairs.  More generally, (1.6) gives the exact mixed-offset moment

\[
 \mathbb E(X_hX_k)=N_h\sum_xv_{h,k,x}
 \left(1-{d_h\over N_h}-{d_k\over N_k}
       +{M_{h,k,x}\over N_hv_{h,k,x}}\right)^t
 \quad(h\ne k).                                        \tag{2.6}
\]

Thus the all-offset second-moment problem is exactly finite: its only
inputs are the intersection censuses of one completed word.

## 3. Explicit central specialization

We first derive the central census directly from the construction.  If the
empty and doubled pair indices are respectively \(t\) and \(i\), the
internal target is

\[
 T_{t,i}=P_i\cup
 \{j^{\chi_{t,i}(j)}:j\notin\{t,i\}\},\qquad
 \chi_{t,i}(j)=t+\mathbf1_{\{(j-i)(t-i)>0\}}\pmod2.       \tag{3.0}
\]

Here indices in the indicator use representatives in
\(\{0,\ldots,b-1\}\).  Before packet \(t\), coordinate \(j\) has
selected bit \(t+\mathbf1_{\{j<t\}}\); precisely the open directed interval
from \(t\) to \(i\) is then flipped before \(P_i\) is doubled, proving
(3.0).

Substitution gives the following exhaustive ordered-pair audit.  The two
target indices are \((t,i)\) and \((u,j)\).

\[
\begin{array}{c|c|c}
\text{index relation}&\text{distance}&\text{number}\\ \hline
(t,i)=(u,j)&0&b(b-1)\\
t=u,\ i\ne j&1\le r\le b-2&2b(b-1-r)\\
i=j,\ t\ne u&1&b(b-1)(b-3)/2\\
i=j,\ t\ne u&b-2&b(b-1)^2/2\\
(u,j)=(i,t)&r\in\{2,4,\ldots,b-1\}&2b\\
\text{exactly one crossed role}&2\le r\le b-1&2b(b-1)\\
|\{t,i,u,j\}|=4&2\le r\le b-2&
b\{b^2-4b+3+4\lfloor r/2\rfloor\}.
\end{array}                                               \tag{3.0a}
\]

For the only nonimmediate last row, fix \(t=0\), put the other three
indices at \(1\le x<y<z\le b-1\), and denote their roles by \(I,U,J\)
(first doubled, second empty, second doubled).  For the six role orders
\(IUJ,IJU,UIJ,UJI,JIU,JUI\), formula (3.0), when \(U\) is even, gives

\[
 z-x,\ b+x-y-1,\ 1-y+z,\ 1-y+z,\ b+x-y-1,\ b+x-z.       \tag{3.0b}
\]

When \(U\) is odd, it gives the respective complements to \(b\).
Solving each linear difference for fixed \(r\), then pairing cases
\(1/6\), \(2/5\), and \(3/4\), gives
\(b^2-4b+3+4\lfloor r/2\rfloor\) choices for fixed \(t\).
The five nonidentity relation classes in (3.0a) have totals

\[
 q(b-2),\quad q(b-2),\quad q,\quad2q(b-2),\quad
 q(b-2)(b-3),
\]

which sum to \(q(q-1)\); hence the table is exhaustive.  Summing it by
distance gives (3.1).

Let `mathcal K` be the `q` distinct **internal** middle targets of one
tour.  Its ordered distance census is

\[
\begin{aligned}
 M_0&=b(b-1),&M_1&={b(b^2-5)\over2},\\
 M_r&=b(b^2+1)&&(2\le r\le b-3,\ r\ {\rm even}),\\
 M_r&=b(b^2-3)&&(3\le r\le b-4,\ r\ {\rm odd}),\\
 M_{b-2}&={b(b+1)(3b-5)\over2},&M_{b-1}&=2b^2,
 \qquad M_b=0 .                                        \tag{3.1}
\end{aligned}
\]

Applying (2.2)--(2.3), with `d_h` replaced by `q`, gives for two
independent internal supports

\[
 \boxed{
 \mathbb E|\pi\mathcal K\cap\sigma\mathcal K|
 ={q^2\over W},\qquad
 \mathbb E\bigl(|\pi\mathcal K\cap\sigma\mathcal K|\bigr)_2
 ={b^4/4+O(b^3)\over W}.}                              \tag{3.2}
\]

The main term in the second expression is the distance-one term:

\[
 {1\over W}{M_1^2\over {b\choose1}^2}
 ={(b^2-5)^2\over4W}.                                  \tag{3.3}
\]

For `2<=r<=b-2`, use `M_r=O(b^3)` and
`binom(b,r)>=binom(b,2)`; their total contribution is `O(b^3/W)`.
The remaining endpoint contributes `O(b^2/W)`, proving (3.2).

For the full completed middle support `mathcal S_0`, the census is

\[
\begin{aligned}
 M^+_1&={b(b^2+4b-1)\over2},\\
 M^+_r&=b(b+1)^2&&(2\le r\le b-3,\ r\ {\rm even}),\\
 M^+_r&=b(b^2+2b-1)&&(3\le r\le b-4,\ r\ {\rm odd}),\\
 M^+_{b-2}&={b(b+1)(3b-1)\over2},&M^+_{b-1}&=4b^2.
                                                               \tag{3.4}
\end{aligned}
\]

To verify (3.4) without importing another result, the added boundary
transversals are

\[
 B_t=\{j^{\,t+\mathbf1_{\{j<t\}}\bmod2}:j\in\mathbb Z_b\}. \tag{3.4a}
\]

Direct comparison with (3.0) shows that ordered boundary--boundary pairs
number \(2b\) at each positive even distance and zero at odd distance.  In
one direction, boundary--internal pairs number \(b(b+1)\) at every odd
distance \(1,\ldots,b-2\), and \(b(b-1)\) at every even distance
\(2,\ldots,b-1\).  Adding both cross directions and these boundary pairs
to (3.1) gives exactly (3.4).

The same argument gives

\[
 \boxed{
 \mathbb E|\pi\mathcal S_0\cap\sigma\mathcal S_0|
 ={b^4\over W},\qquad
 \mathbb E\bigl(|\pi\mathcal S_0\cap\sigma\mathcal S_0|\bigr)_2
 ={b^4/4+O(b^3)\over W}.}                              \tag{3.5}
\]

At the live band width

\[
 H=\left\lceil\sqrt{2b\log(2b)}\right\rceil,           \tag{3.6}
\]

the standard product expansion gives, uniformly for `|h|<=H`,

\[
 {N_h\over W}=
 \exp\left\{-{h^2\over b}+O\left({|h|\over b}
                    +{|h|^3\over b^2}\right)\right\}.  \tag{3.7}
\]

In particular `min_{|h|<=H} N_h=Wb^{-2+o(1)}`.  Since
`d_h<=b^2`, (2.2) and a union bound imply

\[
 \Pr\bigl(\exists |h|\le H:
       \pi\mathcal S_h\cap\sigma\mathcal S_h\ne\varnothing\bigr)
 \le\sum_{|h|\le H}{d_h^2\over N_h}
 \le {b^{6+o(1)}H\over W}=o(1).                        \tag{3.8}
\]

So two random tours are simultaneously disjoint at every band rank with
probability `1-o(1)`.  This local fact does not scale to the required
number of tours.  For

\[
 t=\left\lfloor {W\over q}\right\rfloor,
\]

the expected total number of internal-middle intersection incidences over
all unordered pairs of sampled tours is

\[
 {t\choose2}{q^2\over W}=\left({1\over2}+o(1)\right)W.  \tag{3.9}
\]

Thus exponentially rare two-tour collisions accumulate at linear order
on the near-factor scale.  Pairwise rarity cannot justify independent
rounding or an alteration that samples only the correct number of tours.

## 4. Sharp product-thinning extinction

Consider the parameter-labelled hypergraph whose vertices are middle
targets and whose edges are the internal supports `pi mathcal K`.  Its
exact labelled root degree is

\[
 \boxed{D_{\rm lab}=(b-1)(b!)^2.}                       \tag{4.1}
\]

Indeed there are `(2b)!/b` parameter labels, every label contains `q`
targets, and division of the resulting incidence count by `W` gives
(4.1).  If `mu_b` parameter labels represent each simple support, its
simple degree is `D_lab/mu_b<=D_lab`; no value of `mu_b` is needed below.

Retain every middle target independently with probability `rho`.  Let
`Z_rho` be the number of retained targets which lie in at least one whole
internal tour support contained in the residual.  Counting surviving
rooted edge incidences gives

\[
 \mathbb EZ_\rho\le W D_{\rm lab}\rho^q.                \tag{4.2}
\]

Consequently, if

\[
 D_{\rm lab}\rho^{q-1}=o(1),                            \tag{4.3}
\]

then `Z_rho=o_p(W rho)`.  Since the residual itself has
`(1+o(1))W rho` vertices with high probability, almost every retained
vertex is isolated in the induced tour hypergraph.

There is also a global version.  The number of simple internal supports is
at most the number `(2b)!/b` of parameter labels, so if `Y_rho` counts
whole supports contained in the product residual, then

\[
 \mathbb EY_\rho\le{(2b)!\over b}\rho^q.                \tag{4.3a}
\]

Stirling's formula gives

\[
 \log D_{\rm lab}=2b\log b-2b+O(\log b),               \tag{4.4}
\]

and hence the first-moment survival threshold is

\[
 \boxed{
 \rho_*=D_{\rm lab}^{-1/(q-1)}
 =\exp\left\{-{2\log b-2\over b}
              +O\left({\log b\over b^2}\right)\right\}.} \tag{4.5}
\]

For every fixed `epsilon>0`, take

\[
 \rho=\exp\left\{-{(2+\epsilon)\log b\over b}\right\}.
                                                               \tag{4.6}
\]

Then

\[
 \log(D_{\rm lab}\rho^{q-1})
 =-\epsilon b\log b-2b+O(\log b),                     \tag{4.7}
\]

so (4.3) holds superpolynomially strongly.  Moreover,

\[
 \log\mathbb EY_\rho
 \le 2b\log(2b)-(2+\epsilon)(b-1)\log b
 =-\epsilon b\log b+O(b),                              \tag{4.7a}
\]

and hence with high probability the residual contains **no** whole tour
at all.  Yet

\[
 1-\rho={(2+\epsilon)\log b\over b}
        +O\left({\log^2b\over b^2}\right)=o(1).        \tag{4.8}
\]

Therefore an independently thinned residual loses essentially every
whole-tour option after only `Theta(log(b)/b)` of its vertices have been
removed.  This proves a quantitative obstruction to product-regeneration,
including any whole-tour nibble argument whose essential induction
hypothesis is that the residual behaves like Bernoulli thinning.

It is not an obstruction to the desired theorem itself.  A residual left
by a deliberately correlated tour matching need not resemble a product
set; an explicit resolution, a global switching/absorbing construction,
or a matching-correlated regeneration theorem can evade (4.2).  The
calculation shows exactly why such correlation is indispensable.
