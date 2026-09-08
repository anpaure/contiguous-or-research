# Joint face incidence in quartet wreath partitions

## 0. Status and conclusion

This note studies a genuinely joint source--target event.  Let `X` be a
middle set in `binom([2m],m)` and let `S subset X` have size `m-q`.  A
quartet wreath cell containing `X` has `S` as the intersection of a
physical `q`-face exactly when every coordinate of `X\S` lies on a
different free frame pair.

For a uniformly random quartet decomposition and independent uniform
three-frame choices in the rank sector of `X`, the induced frame at `X` is
an exactly uniform perfect matching of `[2m]`.  Consequently the exact
face-incidence probability is

\[
 p_m(q)=\prod_{i=0}^{q-1}{m-i\over 2(m-i)-1}
       ={(m)_q(2m-2q-1)!!\over(2m-1)!!}.             \tag{0.1}
\]

Uniformly for `q=o(m)`,

\[
 p_m(q)=(1+o(1))2^{-q}.                              \tag{0.2}
\]

The upper-face probability is identical.  Thus the one-pair incidence has
no additional `exp(-Theta(q^2/m))` loss after averaging over frames.
That Gaussian factor is nevertheless real inside a typical
dimension-`m/2` cell.  It disappears from (0.2) because incidence
size-biases the source toward cells of mean dimension
`m/2+q/2+O(1)`.

This exact law has a negative catalog consequence.  Every deterministic
quartet wreath partition has the same dimension histogram, and therefore
covers exactly a `p_m(q)` fraction of all depth-`q` nested pairs.  Any
catalog covering every pair must have at least

\[
 p_m(q)^{-1}=(1+o(1))2^q                             \tag{0.3}
\]

members.  Conversely, `O(m2^H)` independent catalog members cover every
lower and upper nested pair through `H=o(m)`, with linear multiplicity at
the deepest level.  Hence a polynomial catalog is possible through
`H=O(log m)` but impossible when `H/log m` tends to infinity.  At the
central-band depth, an `exp(Theta(H))` reservoir is unavoidable.

An admissible cube face is **not** yet a consecutive cycle window.  This
note supplies neither a cycle factor nor an order in which the required
directions occur.

## 1. The random wreath experiment

When `m=2g`, partition `[2m]` uniformly into `g` unordered quartets.  In
each quartet choose one of its three perfect matchings independently and
uniformly.  When `m=2g+1`, use `g` quartets and one leftover pair; the
leftover pair is itself a matching edge.

For the complete wreath construction the local frame vector is sampled
independently for every admissible source rank sector.  For one fixed
source `X`, only the vector assigned to its sector is relevant.

### Lemma 1 (the induced frame is uniform)

At every fixed source sector, the union `P` of the chosen local matching
edges is a uniformly random perfect matching of `[2m]`.

### Proof

Suppose first that `m=2g`.  Fix a perfect matching `P` with `m` edges.
A quartet decomposition and its local resolutions induce `P` precisely
when the `m` edges of `P` are grouped into `g` unordered pairs.  The number
of such groupings is

\[
 {m!\over 2^g g!},                                  \tag{1.1}
\]

independent of `P`.

For `m=2g+1`, first choose which of the `m` edges of `P` is the leftover
pair, then group the other `2g` edges into `g` unordered pairs.  The count
is again independent of `P`.  Uniformity follows in both cases.  QED.

For a matching `P` and middle set `X`, call a matching edge **split** when
it has one endpoint in `X` and one in `X^c`.  The cell containing `X` has
exactly those split edges as its free physical directions.

Let

\[
 D=X\setminus S,\qquad |D|=q.                       \tag{1.2}
\]

The lower incidence event is

\[
 A^-(X,D)=\{P(D)\subseteq X^c\}.                    \tag{1.3}
\]

If it holds, the `q` matching edges incident with `D` are automatically
distinct.  Flipping arbitrary subfamilies of them gives a physical
`q`-cube whose vertex intersection is `S`.

For `E subset X^c`, `|E|=q`, the upper event is

\[
 A^+(X,E)=\{P(E)\subseteq X\}.                      \tag{1.4}
\]

The corresponding face has vertex union `X union E`.

## 2. Exact one-pair incidence

### Theorem 2 (joint source--target law)

For every fixed `D subset X` of size `q`,

\[
 \Pr A^-(X,D)=p_m(q)
 ={(m)_q(2m-2q-1)!!\over(2m-1)!!}
 =\prod_{i=0}^{q-1}{m-i\over2(m-i)-1}.              \tag{2.1}
\]

The same formula holds for every fixed upper demand
`E subset X^c` of size `q`.

### Proof

Match the labelled elements of `D` injectively to `q` elements of `X^c`.
There are `(m)_q` choices.  The remaining `2m-2q` vertices admit
`(2m-2q-1)!!` arbitrary perfect matchings.  Divide by the total
`(2m-1)!!`.  Complementation proves the upper statement.  QED.

The useful uniform form of (2.1) is

\[
 \log(2^q p_m(q))
 ={1\over2}\log{m\over m-q}+O\left({1\over m-q}\right).  \tag{2.2}
\]

In particular (0.2) holds uniformly for `q=o(m)`.

## 3. Where the `exp(-q^2/m)` factor went

Write `d_P(X)` for the number of split matching edges at `X`.  Conditional
on `P` and `X`, exactly

\[
 \binom{d_P(X)}q                                     \tag{3.1}
\]

of the `binom(m,q)` lower targets are admissible faces.  If `d>=cm` and
`q=o(m)`, direct expansion gives

\[
 \log {\binom dq\over\binom mq}
 =q\log{d\over m}
  -{q(q-1)\over2}\left({1\over d}-{1\over m}\right)
  +O\left({q^3\over m^2}\right).                   \tag{3.2}
\]

Thus a cell of dimension `d=m/2+O(1)` has face density

\[
 2^{-q}\exp\left(-{q(q-1)\over2m}
                  +O(q/m+q^3/m^2)\right).          \tag{3.3}
\]

This is the expected `exp(-Theta(q^2/m))` depletion.

There is no contradiction with (2.2).  Conditional on `A^-(X,D)`, remove
the `q` forced cross edges.  The remaining matching is uniform on two
equal sides of size `m-q`.  Therefore

\[
 d_P(X)\mid A^-(X,D)\ \buildrel d\over=
 q+D_{m-q},                                         \tag{3.4}
\]

where `D_n` is the number of cross edges in a uniform matching of two
labelled `n`-sets.  Since

\[
 \mathbb E D_n={n^2\over2n-1},                      \tag{3.5}
\]

we get

\[
 \mathbb E[d_P(X)\mid A^-(X,D)]
 ={m\over2}+{q\over2}+O(1).                         \tag{3.6}
\]

At depths above `sqrt(m)`, successful incidences are therefore
exponentially tilted toward atypically large cells.  The rarity of those
cells and their excess number of faces cancel in the exact factorial
moment

\[
 \mathbb E_P\binom{d_P(X)}q=\binom mq p_m(q).        \tag{3.7}
\]

Equation (3.3) is the correct cellwise scale; equation (2.2) is the correct
unconditional nested-pair scale.

## 4. Exact same-source codegrees

Let `D_1,D_2 subset X`, with sizes `a,b`, and put
`c=|D_1 intersection D_2|` and `u=a+b-c`.

### Theorem 3 (two lower faces)

\[
 \Pr(A^-(X,D_1)\cap A^-(X,D_2))=p_m(u).             \tag{4.1}
\]

The identical formula holds for two upper demands in `X^c`.  Consequently

\[
 {\Pr(A_1\cap A_2)\over\Pr(A_1)\Pr(A_2)}
 =2^c\exp(o(1))                                     \tag{4.2}
\]

uniformly when `a+b=o(m)`.  In particular, overlapping demands have the
unavoidable shared-coordinate factor `2^c`.

If `D_1,D_2` are disjoint, an exact sequential form is

\[
 p_m(a+b)=p_m(a)p_{m-a}(b),                         \tag{4.3}
\]

and hence

\[
 {p_m(a+b)\over p_m(a)p_m(b)}
 =\exp\left(O\left({ab\over(m-a-b)^2}\right)\right). \tag{4.4}
\]

Disjoint lower demands are therefore asymptotically independent throughout
`a+b=o(m)`.

### Proof

Both events hold exactly when every element of `D_1 union D_2` is matched
outside `X`; apply Theorem 2.  For disjoint demands, expose the `a` forced
cross edges first.  They leave two equal sides of size `m-a`, proving
(4.3).  Equations (2.2) and (4.3) give the estimates.  QED.

## 5. Lower--upper codegrees

Let `D subset X`, `E subset X^c`, with `|D|=a`, `|E|=b`.  Direct edges
between `D` and `E` satisfy one lower and one upper demand simultaneously,
so this codegree has a different scale.

Let `R` have the hypergeometric law

\[
 \Pr(R=h)={\binom bh\binom{m-b}{a-h}\over\binom ma}. \tag{5.1}
\]

### Theorem 4 (opposite-side codegree)

\[
 \Pr(A^-(X,D)\cap A^+(X,E))
 =p_m(a)\,\mathbb E\,p_{m-a}(b-R).                  \tag{5.2}
\]

Equivalently it is

\[
 {1\over(2m-1)!!}
 \sum_h \binom ah\binom bhh!
 (m-b)_{a-h}(m-a)_{b-h}
 (2m-2a-2b+2h-1)!!.                                \tag{5.3}
\]

Uniformly for `a+b=o(m)`,

\[
 {\Pr(A^-\cap A^+)\over p_m(a)p_m(b)}
 =(1+o(1))\mathbb E2^R.                             \tag{5.4}
\]

Moreover

\[
 \exp\left((\log2){ab\over m}\right)
 \le \mathbb E2^R
 \le \left(1+{b\over m}\right)^a
 \le \exp\left({ab\over m}\right).               \tag{5.5}
\]

Thus the normalized lower--upper codegree has the genuine scale

\[
 \exp(\Theta(ab/m)).                                \tag{5.6}
\]

For `a=b=q`, this is `exp(Theta(q^2/m))`.  It is a positive correlation,
not an incidence loss.

### Proof

First impose the lower event.  Its `a` outside mates form a uniform
`a`-subset of `X^c`; `R` counts how many lie in `E`.  Those `R` upper
demands are already satisfied.  After deleting the exposed edges, a
uniform matching remains on two sides of size `m-a`, giving (5.2).
Classifying by the number `h` of direct `D--E` edges gives (5.3).

Write `p_n(s)=2^{-s}r_n(s)`.  Equation (2.2) gives
`r_n(s)=exp(O(s/(n-s)))`, so (5.4) follows uniformly when `a+b=o(m)`.
Jensen gives the first bound in (5.5).  Sampling without replacement is
negatively associated, so its exponential moment is at most that of `a`
independent Bernoulli variables of mean `b/m`; this gives the second bound.
QED.

The factor `exp(Theta(q^2/m))` must be retained in any codegree or nibble
analysis involving lower and upper targets simultaneously.

## 6. Arbitrary two-source codegrees

For two distinct sources, a single scalar such as their Johnson distance
does not determine the wreath codegree.  Whether the two sources have the
same complete quartet-rank vector determines whether they share or use
independent local frame variables.

There is nevertheless an exact local formula.  Fix a quartet decomposition
`Qcal`.  For source--demand pair `(X_s,D_s)`, `s=1,2`, let

\[
 A_s(Q)=\{P\text{ one of the three matchings of }Q:
          P(D_s\cap Q)\subseteq Q\setminus X_s\},   \tag{6.1}
\]

and put `alpha_s(Q)=|A_s(Q)|/3`.  If the complete rank vectors
`t(X_1)` and `t(X_2)` differ, the conditional codegree is

\[
 \prod_{Q\in Qcal}\alpha_1(Q)\alpha_2(Q).           \tag{6.2}
\]

If the rank vectors agree, the two sources use the same sector frame and
the conditional codegree is

\[
 \prod_{Q\in Qcal}{|A_1(Q)\cap A_2(Q)|\over3}.      \tag{6.3}
\]

Average (6.2)--(6.3) over the uniform quartet decomposition.  This is an
exact finite codegree formula for arbitrary lower pairs.  Upper or mixed
pairs are obtained by reversing the required side of each demanded
coordinate.  For odd `m`, multiply the local product by the deterministic
feasibility indicator on the leftover pair.  The formula depends only on
the nine coordinate types

\[
 (D_s,\ X_s\setminus D_s,\ X_s^c),\qquad s=1,2,    \tag{6.4}
\]

and can be evaluated by a finite coefficient extraction or dynamic
program.  It also shows why one-set marginal independence cannot simply be
asserted for two sources.

## 7. Exact incidence budget of one wreath partition

Let `eta` be any deterministic wreath frame function and let
`d_eta(X)` be the dimension of the cell containing `X`.  The exact
dimension-histogram theorem gives

\[
 \#\{X:d_eta(X)=d\}
 =\binom md2^d\binom{m-d}{(m-d)/2}.                 \tag{7.1}
\]

It is independent of `eta`.  Therefore the number of admissible lower
depth-`q` incidences in one complete wreath partition is

\[
 \sum_X\binom{d_eta(X)}q
 =W\binom mq p_m(q).                                \tag{7.2}
\]

The same identity holds on the upper side.  Since there are
`W binom(m,q)` nested pairs on either side, every wreath partition has
average multiplicity exactly `p_m(q)`.

There is an exact two-sided version.  Let

\[
 J_m(a,b)=\Pr(A^-(X,D)\cap A^+(X,E))                \tag{7.3}
\]

be the quantity in Theorem 4.  A dimension-`d` cell admits
`binom(d,a)binom(d,b)` ordered lower--upper demand pairs: the two chosen
direction sets may overlap, in which case a direct matching edge satisfies
both demands.  Hence

\[
 \sum_X\binom{d_eta(X)}a\binom{d_eta(X)}b
 =W\binom ma\binom mb J_m(a,b).                     \tag{7.4}
\]

### Corollary 5 (catalog lower bound)

If a catalog of `K` deterministic wreath partitions covers every lower
depth-`q` nested pair at least `L` times, then

\[
 K\ge {L\over p_m(q)}=(1+o(1))L2^q.                \tag{7.5}
\]

for `q=o(m)`.  The same is true for upper pairs.  If instead every ordered
combined lower--upper demand of sizes `a,b` must occur at least `L` times,
then

\[
 K\ge {L\over J_m(a,b)}.                            \tag{7.6}
\]

For `a=b=q=o(m)`, Theorem 4 places this combined lower bound between
`L2^{2q}exp(-q^2/m+o(1))` and
`L2^{2q}exp(-(log2)q^2/m+o(1))`.

In particular, no constant catalog covers all depths tending to infinity,
and no polynomial catalog covers a depth `q` with `q/log m` tending to
infinity.

## 8. A matching random-catalog upper bound

Take `K` independent complete random wreath partitions.  For any fixed
nested pair at depth `q`, its number `Z` of admissible frames is exactly

\[
 Z\sim\operatorname{Bin}(K,p_m(q)).                 \tag{8.1}
\]

There are

\[
 2W\sum_{q=0}^H\binom mq                            \tag{8.2}
\]

lower and upper pairs through depth `H`.  If `H=o(m)`, the logarithm of
(8.2) is `(2 log 2+o(1))m`.  Chernoff and a union bound therefore prove:

### Theorem 6 (uniform random catalog)

For every fixed `epsilon>0` and `H=o(m)`, there exists a catalog of

\[
 K=O_\epsilon\left({m\over p_m(H)}\right)
   =O_\epsilon(m2^H)                                \tag{8.3}
\]

wreath partitions such that every lower and upper nested pair at every
`q<=H` belongs to at least

\[
 (1-\epsilon)Kp_m(q)                                \tag{8.4}
\]

admissible cube faces.

At `q=H`, this is `Omega(m)` admissible catalog members.  Equations
(7.5) and (8.3) determine the catalog scale up to a polynomial factor.
The catalog is subexponential for every `H=o(m)`, but it is far larger than
polynomial at the intended central-band depths.

The same union bound for **combined** lower--upper demands uses

\[
 K=O\left({m\over
       \min_{a,b\le H}J_m(a,b)}\right).              \tag{8.5}
\]

By choosing canonical demand sets nested as their sizes increase, the
events show that `J_m(a,b)` is nonincreasing in each argument.  Hence the
minimum in (8.5) is `J_m(H,H)`.  At equal deepest demands its governing scale is
`m2^{2H}exp(-Theta(H^2/m))`.  This is where the Gaussian-scale correction
survives in the catalog incidence ledger.

## 9. The remaining gap to an OR construction

The event in Theorem 2 says that the required `q` independent physical
directions exist in the source cell.  It gives a `2^q`-vertex face, and any
chosen ordering of its directions gives a geodesic `q`-step path whose
lower intersection or upper union is the desired target.

It does **not** say that:

* a selected cycle factor contains that path consecutively;
* different targets receive distinct cycle windows;
* one catalog member can be selected for each middle source while keeping
  a disjoint partition;
* lower and upper assignments survive their
  `exp(Theta(q^2/m))` mixed codegrees; or
* the number of seams and omitted targets is `o(W)`.

The next theorem cannot be another one-set diffusion statement.  It must
route nested-pair incidences from an `exp(Theta(H))` wreath reservoir into
ordered, disjoint cycle windows, or find a structured replacement whose
incidence budget beats the universal `2^{-q}` face fraction.
