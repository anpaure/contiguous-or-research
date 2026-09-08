# Antipodal cyclic-interval blocks: exact spread and the diagonal nibble gap

## 1. Outcome

Put

\[
 n=2m+1,\qquad W=\binom n m,\qquad
 N_q=\binom n{m-q},\qquad \rho_q=N_q/W.
\]

There are two different hypergraphs which must not be conflated.

* In the unquotiented vertically resolved hypergraph, complementary masks are
  exact or near twins.  Its maximum relative codegree is therefore bounded
  away from zero at every shallow depth.  A raw Pippenger--Rödl invocation is
  impossible.
* After quotienting each complementary pair to one **antipodal atom**, a
  canonical typed cyclic-order hypergraph has an exact fractional perfect
  matching, maximum relative pair-codegree exactly `2/(m+1)`, and a stronger
  edge--link overlap bound `O(H/n)`.  Thus the projective-plane obstruction is
  genuinely absent after quotienting.

The second statement is positive, but it still does not yield the desired
OR construction from an available black-box nibble.  The atom set through
depth `H >> sqrt(n)` has `Theta(W sqrt(n))` vertices, while literal repair is
allowed to cost only `o(W)`.  Hence the matching must leave an
`o(n^(-1/2))` fraction, not merely an `o(1)` fraction.  The audited
growing-uniformity theorems do not give that rate in this diagonal regime.

This note gives the exact calculations.

## 2. The raw complement obstruction

For a cyclic order `pi`, write

\[
 L_q(j)=I_\pi(j,m-q),\qquad
 U_q(j)=I_\pi(j,m+1+q).
\]

Suppose one block activates a set `A_q subseteq Z_n` of starts at depth `q`,
with `|A_q|=t_q`.  The complement identity is

\[
 [n]\setminus L_q(j)=U_q(j+m-q).                       \tag{2.1}
\]

Consequently the block contains at least

\[
 |A_q\cap(A_q-(m-q))|\ge (2t_q-n)_+                  \tag{2.2}
\]

complementary lower--upper pairs.

Consider any coordinate-symmetric weighted family of such blocks.  Let
`D_q` be the common degree of a depth-`q` target and let `lambda_q` be the
codegree of `S` and its complement.  If every block has the same `t_q`, then
double counting complementary-pair incidences gives

\[
 \boxed{\frac{\lambda_q}{D_q}
     \ge \frac{(2t_q-n)_+}{t_q}.}                     \tag{2.3}
\]

The identical inequality with `t_q` replaced by its weighted average follows
for variable profiles, because `x -> (2x-n)_+` is convex.

In a rank-balanced family the average is

\[
 \overline t_q=n\rho_q+o(n).
\]

Moreover

\[
 \rho_q=\prod_{i=0}^{q-1}\frac{m-i}{m+2+i}
        =1-O(q^2/n)
\]

uniformly for `q=o(sqrt(n))`.  Hence

\[
 \frac{\lambda_q}{D_q}=1-O(q^2/n)                   \tag{2.4}
\]

as a lower bound in the shallow range.  At depth zero it equals one exactly.
For `q=1`, (2.3) gives the explicit lower bound `1-2/m`.

Thus the raw maximum relative codegree is not `Theta(1/n)`; it is nearly
one.  Equivalently, either a complementary pair is an exact twin pair, or an
edge containing `S^c` but not `S` destroys a `1-O(q^2/n)` fraction of the
link of `S`.  This also disproves an `o(1)` maximum edge--link overlap bound
before antipodal quotienting.

## 3. The antipodal typed-order hypergraph

For `0<=q<=H`, let the depth-`q` atom set be

\[
 \mathcal V_q={[S]=\{S,[n]\setminus S\}:|S|=m-q\}.
\]

It has size `N_q`.  For an unoriented cyclic order `pi` and a type
`d in {0,...,H}`, define

\[
 e(\pi,d)=
 \{[I_\pi(j,m-q)]:0\le q\le d,\ j\in\mathbb Z_n\}.   \tag{3.1}
\]

Thus

\[
 |e(\pi,d)|=n(d+1).                                  \tag{3.2}
\]

Give type `d` weight

\[
 p_d=\rho_d-\rho_{d+1}\quad(d<H),\qquad p_H=\rho_H.  \tag{3.3}
\]

The tail identity is

\[
 \sum_{d=q}^H p_d=\rho_q.                            \tag{3.4}
\]

### Theorem 1 (exact common fractional degree)

Every atom in every depth has the same weighted degree

\[
 \boxed{D_*=\frac{n!}{2W}.}                           \tag{3.5}
\]

#### Proof

There are `(n-1)!/2` unoriented cyclic orders.  A fixed `s`-set is an
interval in exactly

\[
 \frac{s!(n-s)!}{2}=\frac{n!}{2\binom ns}
\]

of them.  For `s=m-q`, multiply this by the type tail `rho_q=N_q/W`.
The result is (3.5), independent of `q`.  QED.

The mean atom rank of an edge under (3.3) is

\[
 \overline R_H
 =n\sum_{q=0}^H\rho_q.                               \tag{3.6}
\]

If `H/sqrt(n)->infinity`, then

\[
 \sum_{q=0}^H\rho_q
   =(1+o(1))\frac{2^{n-1}}W
   =\left(\sqrt{\frac\pi8}+o(1)\right)\sqrt n,
\]

and therefore

\[
 \overline R_H
   =\left(\sqrt{\frac\pi8}+o(1)\right)n^{3/2}.        \tag{3.7}
\]

## 4. Exact pair probabilities and codegree

Fix sets `S,T` of sizes `s,r<=m`, and put

\[
 a=|S\cap T|,\qquad b=|T\setminus S|,\qquad c=n-s.
\]

For a uniform cyclic order conditioned on `S` being an interval, the exact
probability that `T` is also an interval is

\[
 P_S(T)=
 \begin{cases}
  1,&T=S,\\
  \dfrac{s-r+1}{\binom sr},&T\subsetneq S,\\
  \dfrac{2}{\binom c{r-s}},&S\subsetneq T,\\
  \dfrac{c-r+1}{\binom cr},&S\cap T=\varnothing,\\
  \dfrac{2}{\binom sa\binom cb},&
       0<a<s,\ b>0.
 \end{cases}                                             \tag{4.1}
\]

To prove (4.1), condition on the two linear blocks `S` and `S^c` in the
cyclic order.  A proper subinterval of `S` has `s-r+1` possible positions; a
proper superinterval extends through either endpoint of `S`; a disjoint
interval is an internal interval of the complementary block; and a crossing
interval chooses one of the two `S|S^c` boundaries.  The internal orders of
all Venn atoms are arbitrary, giving the displayed binomial denominators.

For two atoms at depths `q_S,q_T`, condition on the deeper atom.  The type
tail in their common weighted codegree is then exactly the type tail in the
degree of that deeper atom.  Hence their relative weighted codegree is the
corresponding value in (4.1).

### Corollary 2 (exact maximum pair-codegree)

For distinct antipodal atoms in the band,

\[
 \boxed{\frac{\Delta_2}{D_*}=\frac2{m+1}.}             \tag{4.2}
\]

The maximum is attained by two disjoint `m`-sets.  Indeed, after conditioning
on the smaller of `S,T`, the proper-containment cases are at most
`2/(m+1)`, the disjoint case is maximized when the complementary block has
one unused point, and the crossing case is at most
`2/(s(n-s))`.

There is also an exact higher-codegree spine.  Let

\[
 S_0\subset S_1\subset\cdots\subset S_a,
 \qquad |S_i|=s+i,
\]

be a prescribed saturated flag in the band, with `S_0` the deepest atom.
Then

\[
 \boxed{
 \frac{\deg_w([S_0],\ldots,[S_a])}{D_*}
   =\frac{2^a}{(n-s)_a}.}                              \tag{4.3}
\]

Conditioned on `S_0` being an interval, each prescribed new element must be
the left or right endpoint of the unused complementary block.  This gives
two choices at each step and proves (4.3).  Thus the large pair-codegree does
collapse by another factor `Theta(1/n)` along every additional prescribed
chain step.  Formula (4.3) is a useful full-codegree input, but by itself it
is not a growing-rank matching theorem.

## 5. A quotient edge--link spread theorem

For an edge `e` and an atom `v notin e`, define the normalized link-overlap
mass

\[
 \Lambda(e,v)=\frac1{D_*}\sum_{u\in e}\deg_w(u,v).     \tag{5.1}
\]

It upper-bounds the probability that a random weighted edge through `v`
meets `e`.

### Lemma 3 (one fixed rank)

Let `s,r in [m-H,m]`, where `H=o(n)`.  Fix an `s`-set `S` and a cyclic
order `sigma`.  Among the `n` atoms represented by the `r`-intervals of
`sigma`, omit `[S]` if it occurs.  Then

\[
 \sum_T P_S(T)=O(1/n),                                 \tag{5.2}
\]

uniformly in `S,r,s`.

#### Proof

Decompose the `r`-intervals `T` into four classes.

* If `T proper-subset S`, the number of such intervals is at most
  `s-r+1`.  Their total contribution is at most
  \[
    \frac{(s-r+1)^2}{\binom sr}=O(1/n).
  \]
  (For difference one this is `Theta(1/n)`; for every larger difference it
  is `O(1/n^2)`.)
* If `S proper-subset T`, there are at most `r-s+1`, and their contribution
  is at most
  \[
    \frac{2(r-s+1)}{\binom{n-s}{r-s}}=O(1/n).
  \]
* If `S` and `T` are disjoint, there are at most `n-s-r+1`, and their
  contribution is at most
  \[
   \frac{(n-s-r+1)^2}{\binom{n-s}{r}}=O(1/n).
  \]
* Every remaining interval crosses a boundary of `S`.  Each has probability
  at most `2/(s(n-s))=O(1/n^2)` by (4.1), and there are at most `n` of them.

The three interval-count bounds follow by decomposing `S` or `S^c` into
cyclic runs: the number of length-`r` all-one windows in a word with `s`
ones is at most `s-r+1`.  Since all relevant size differences are `o(n)`,
the displayed binomial ratios have the stated uniform bounds.  QED.

### Theorem 4 (maximum quotient link-overlap)

For the typed-order hypergraph through depth `H=o(n)`,

\[
 \boxed{max_{e,\,v\notin e}\Lambda(e,v)=O(H/n)=o(1).} \tag{5.3}
\]

#### Proof

At any one depth, enlarge the retained atoms of `e` to all `n` intervals of
its cyclic order.  For a random weighted edge through `v`, the conditional
type requirement and the retention of another atom can only decrease the
underlying conditional interval probability.  Lemma 3 therefore bounds the
contribution of that depth by `O(1/n)`.  Sum over at most `H+1` depths.
QED.

Thus antipodal quotienting does more than repair the maximum codegree: it
also removes the standard projective-plane pathology.  In a projective
plane every line through an outside point meets a fixed line, so the analogue
of (5.3) equals one.

## 6. Why this still does not close the nibble

The number of antipodal atoms in the certified band is

\[
 V_H=\sum_{q=0}^H N_q
    =W\sum_{q=0}^H\rho_q
    =\left(\sqrt{\frac\pi8}+o(1)\right)W\sqrt n       \tag{6.1}
\]

when `H/sqrt(n)->infinity`.  If a matching leaves `Q` atom vertices, literal
repair costs `2Q`.  Therefore the condition sufficient for
`nu(n)=W+o(W)` is

\[
 \boxed{Q=o(W),\qquad\text{equivalently}\qquad
        Q/V_H=o(n^{-1/2}).}                            \tag{6.2}
\]

An ordinary statement that leaves `o(V_H)` vertices is not enough.

If (6.2) holds, concatenate the cyclic erosion block for every selected
`(pi,d)`.  Its principal length is `n` and its repeated prefix costs `O(d)`.
There are `(1+o(1))W/n` selected blocks and `d<=H=o(n)`, so the physical
length is `W+o(W)`.  Append the two members of every missing atom and then
the already proved `o(W)` outer-tail word.  This proves the claimed
sufficiency.

The audited black boxes do not yield (6.2).

* The edge rank is growing, with weighted mean `Theta(n^(3/2))` by (3.7).
  Classical Pippenger--Rödl/Pippenger--Spencer statements fix the rank.
* The exact pair ratio is `Theta(1/n)`.  Quantitative criteria of the form
  `Delta_2=o(D/(R log V_H))` fail by a polynomial factor.
* In full-codegree nibble formulations whose usable parameter is bounded by
  `B<=sqrt(D/Delta_2)`, (4.2) gives only `B=O(sqrt(n))`.  Even the nominal
  scale `B^(-1+o(1))` is `n^(-1/2+o(1))`, before the theorem's logarithmic
  loss and before its fixed-rank hierarchy.  The required error in (6.2) is
  strictly `o(n^(-1/2))`.

The spread estimate (5.3) is a real extra structural input, and it rules out
the usual projective-plane counterexample.  What is still missing is a
**diagonal spread-nibble/absorption theorem** which uses (4.3) and (5.3),
handles edge rank `Theta(n^(3/2))`, preserves the type tails, and returns the
absolute leftover `o(W)`.  No theorem audited in the current handoff has all
four properties.

Hence the precise conclusion is:

\[
 \text{raw resolved-order nibble: impossible without quotienting;}\qquad
 \text{antipodal quotient: numerically viable but not yet rounded.}
\]
