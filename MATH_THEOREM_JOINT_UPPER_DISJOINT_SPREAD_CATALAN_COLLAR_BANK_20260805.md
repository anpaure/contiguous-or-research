# A joint upper-disjoint and low-star-spread Catalan collar bank

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional prospective bank theorem.  For all sufficiently
large middle dimensions at the deadline scale, there is an exact
parity-appropriate Catalan bank of balanced pivot collars which is
simultaneously owner/endpoint-disjoint, upper-`q1`-target-disjoint, and
`O(1/s)`-spread in every low containment star.  This proves the
intersection left open between Theorems 2.3 and 2.4 of
`MATH_THEOREM_PIVOT_GLUING_UPPER_Q1_CAPACITY_AND_BALANCED_SEAM_COLLAR_20260805.md`.
It does not construct the protected trace factor on the complementary
owners.

## 1. Parameters and the balanced-collar resource sets

Let

\[
       k\in\{2r,2r-1\},\qquad W={k\choose r},
       \qquad h\ge2,\qquad s=h+1.
\tag{1.1}
\]

A generalized balanced collar is the object in equations (2.2),
(2.14)--(2.16) of the pivot-gluing note.  It has two resource sets:

* an owner resource set
  \[
       E_O=\{P,M_0,\ldots,M_h,N\},\qquad |E_O|=s+2;
  \tag{1.2}
  \]
* a set of distinct new upper-`q1` resources
  \[
       E_U=\{U_1,\ldots,U_h,U_*\},\qquad |E_U|=s.
  \tag{1.3}
  \]

The repeated left seam occurrence of `U_1` is the unique internal repeat
of one collar; it is represented only once in the resource set (1.3).

Put

\[
 c=\begin{cases}
       W/(r+1),&k=2r,\\
       W/(2r-1),&k=2r-1,
    \end{cases}
 \qquad b=c-1.
\tag{1.4}
\]

Thus `b` is the exact number of collars needed to join the standard
parity-appropriate Catalan component count.

## 2. A large doubly-disjoint bank

The greedy proof of Theorem 2.4 in the pivot-gluing note can be run much
longer than the Catalan count.  We record the quantitative form needed for
thinning.

### Lemma 2.1 (large owner-and-upper-disjoint bank)

Let `F` be an independently prescribed forbidden owner bank.  Assume

\[
       r\ge32s,
       \qquad |F|\le {W\over64s}.                    \tag{2.1}
\]

Then there are

\[
                         M=\left\lfloor{W\over16s}\right\rfloor
\tag{2.2}
\]

balanced collars outside `F` whose owner resource sets are pairwise
disjoint and whose new upper-`q1` resource sets are pairwise disjoint.

#### Proof

Use the bipartite containment graph between the rank-`r` owner shore and
the rank-`r+1` upper shore.  First delete `F`.  After each collar, delete
its `s+2` owner vertices and its `s` upper vertices.

For `k=2r`, the shore degrees are `r` and `r+1`, and the initial edge count
is `Wr`.  One collar deletes at most

\[
 D_e=(s+2)r+s(r+1)=2r(s+1)+s                    \tag{2.3}
\]

incidences.  Before the `M`-th collar the residual graph therefore has
strictly more than

\[
 W\left(r-{r\over64s}-{D_e\over16s}\right)
 =W\left({7r\over8}-{9r\over64s}-{1\over16}\right)
 >2W(s+3)                                           \tag{2.4}
\]

edges.  The last inequality follows from `r>=32s` and `s>=3`.

For `k=2r-1`, the shore degrees are `r-1` and `r+1`, the initial edge
count is `W(r-1)`, and one collar deletes at most

\[
 D_o=(s+2)(r-1)+s(r+1)=2r(s+1)-2.                  \tag{2.5}
\]

The residual graph has strictly more than

\[
 W\left(r-1-{r\over64s}-{D_o\over16s}\right)
 =W\left({7r\over8}-{9r\over64s}-1+{1\over8s}\right)
 >2W(s+3).                                           \tag{2.6}
\]

Both residual shores together contain fewer than `2W` vertices.  Equations
(2.4) and (2.6) therefore imply that the residual graph has a nonempty
subgraph of minimum degree greater than `s+3`: repeatedly delete vertices
of degree at most `s+3`; if all vertices disappeared, at most
`(s+3)|V|<2W(s+3)` edges could have been deleted.

The constructive argument in Theorem 2.4 applies inside any such
minimum-degree subgraph.  It produces a generalized balanced collar whose
`s+2` owners and `s` new upper resources all lie in the residual graph.
Deleting those resources and iterating proves (2.2).  \(\square\)

## 3. Exact-size thinning with weighted star control

The next lemma is stated separately because it is useful whenever a large
resource-disjoint bank is available.

### Lemma 3.1 (weighted exact-size thinning)

Let `B_1,...,B_M` be pairwise disjoint subsets of a finite set, with

\[
                         |B_i|\le t.                 \tag{3.1}
\]

Let `mathcal A` be a family of test sets, put

\[
                         L=\min_{A\in\mathcal A}|A|,
\tag{3.2}
\]

and choose exactly `b` of the `M` blocks uniformly, where

\[
                         p={b\over M}.               \tag{3.3}
\]

For every fixed test set `A`, if `X_A` is the number of selected elements
lying in `A`, then

\[
 \Pr\{X_A>2p|A|\}
       \le \exp\left(-{3p|A|\over8t}\right).         \tag{3.4}
\]

Consequently, if

\[
       {3pL\over8t}-\log|\mathcal A|\longrightarrow+\infty,
\tag{3.5}
\]

there is an exact `b`-block subfamily satisfying

\[
              \left|A\cap\bigcup_{i\text{ selected}}B_i\right|
                    \le2p|A|                         \tag{3.6}
\]

simultaneously for every `A in mathcal A`.

#### Proof

For fixed `A`, write

\[
                  w_i=|B_i\cap A|.
\tag{3.7}
\]

Disjointness gives

\[
       0\le w_i\le t,
       \qquad \sum_iw_i\le|A|,
       \qquad \sum_iw_i^2\le t|A|.                 \tag{3.8}
\]

Sampling `b` population values without replacement is dominated in convex
order by sampling `b` values independently with replacement (Hoeffding's
sampling comparison theorem).  Let `Y_1,...,Y_b` be the latter independent
sample.  Then

\[
 \mathbb E\sum_jY_j=p\sum_iw_i\le p|A|,
 \qquad
 \sum_j\operatorname{Var}(Y_j)
       \le {b\over M}\sum_iw_i^2\le pt|A|.          \tag{3.9}
\]

Each centered summand has absolute upper bound `t`.  More explicitly,
Hoeffding's convex-order comparison gives domination of every positive
exponential moment, so the usual exponential-moment proof of Bernstein's
inequality for the independent sum applies unchanged to the
without-replacement sum.  Since both sums have the same mean, at most
`p|A|`, the event `X_A>2p|A|` has centered deviation greater than
`p|A|`.  Bernstein's bound therefore gives

\[
 \begin{aligned}
 \Pr\{X_A>2p|A|\}
 &\le
 \exp\left(
   -{p^2|A|^2\over2(pt|A|+tp|A|/3)}
      \right)\\
 &=\exp\left(-{3p|A|\over8t}\right),
 \end{aligned}
\]

which is (3.4).  A union bound proves (3.6) under (3.5).  \(\square\)

## 4. The joint Catalan bank

For every lower set `S` of rank at most `r-h-1`, let

\[
 \mathcal O(S)=\{T\in{[k]\choose r}:S\subseteq T\} \tag{4.1}
\]

be its owner-containment star.  The smallest such star has size

\[
             L_*={k-r+h+1\choose h+1}.               \tag{4.2}
\]

### Theorem 4.1 (joint upper-disjoint spread Catalan bank)

Let `F` be any independently prescribed owner bank.  Assume

\[
 r\ge32s,
 \qquad {W\over16s}\ge2,
 \qquad c\ge2,
 \qquad |F|\le {W\over64s},                         \tag{4.3}
\]

and

\[
 {L_*/r\over
  1+\log\left|
   \{S\subseteq[k]:|S|\le r-h-1\}
            \right|}
       \longrightarrow+\infty.
\tag{4.4}
\]

Then there is a family of exactly `b=c-1` generalized balanced collars,
all avoiding `F`, such that:

1. all `s+2` owner resources of different collars are pairwise distinct;
2. all `s` new upper-`q1` resources of different collars are pairwise
   distinct; and
3. for every `S` with `|S|<=r-h-1`, the complete protected owner bank
   `V_B` satisfies
   \[
   |V_B\cap\mathcal O(S)|
       \le
       \begin{cases}
        \displaystyle {64s\over r+1}|\mathcal O(S)|,&k=2r,\\[6pt]
        \displaystyle {64s\over2r-1}|\mathcal O(S)|,&k=2r-1.
       \end{cases}                                  \tag{4.5}
   \]

#### Proof

Take the `M`-collar bank of Lemma 2.1 and sample exactly `b` of its collars.
The sample is possible because, using `floor(x)>=x/2` for `x>=2`,

\[
 M\ge {W\over32s}.                                  \tag{4.6}
\]

In the even case, `b<W/(r+1)<=W/(32s)`, and in the odd case
`b<W/(2r-1)<W/(32s)`, so `b<=M`.

Put `p=b/M` and `t=s+2<=2s`.  Since `c>=2`, `c-1>=c/2`.  Hence

\[
 {p\over t}\ge
 \begin{cases}
  \displaystyle {4\over r+1},&k=2r,\\[5pt]
  \displaystyle {4\over2r-1},&k=2r-1.
 \end{cases}                                        \tag{4.7}
\]

Indeed, for example in the even case,

\[
 p={c-1\over M}
    \ge {W/[2(r+1)]\over W/(16s)}={8s\over r+1},
\]

and division by `t<=2s` gives (4.7).  The odd calculation is identical.

Apply Lemma 3.1 to the pairwise disjoint owner sets `E_O` of the large
bank, and to all tests (4.1).  Equations (4.4) and (4.7) imply (3.5), so
one exact `b`-collar subbank satisfies

\[
                         |V_B\cap\mathcal O(S)|
                                  \le2p|\mathcal O(S)|. \tag{4.8}
\]

On the other hand, (4.6) and `b<c` give

\[
 p\le
 \begin{cases}
  \displaystyle {32s\over r+1},&k=2r,\\[5pt]
  \displaystyle {32s\over2r-1},&k=2r-1.
 \end{cases}                                        \tag{4.9}
\]

Equations (4.8)--(4.9) prove (4.5).  Owner and upper-resource
disjointness are inherited from the large bank.  \(\square\)

### Corollary 4.2 (deadline-scale intersection theorem)

Take

\[
 h=d(k)+1,\qquad s=d(k)+2,\qquad k=2r+O(1).
\tag{4.10}
\]

Then

\[
             {s^2\over r}\longrightarrow{\pi\over4},
\tag{4.11}
\]

so (4.3) holds for every sufficiently large `k`.  Moreover

\[
 \log L_*=\Theta(\sqrt r\log r),
 \qquad
 \log|\mathcal A|=O(r),
\tag{4.12}
\]

and hence (4.4) holds.  Therefore, for every sufficiently large middle
dimension, there is an exact parity-appropriate Catalan bank of balanced
collars which is simultaneously:

* owner- and endpoint-owner-disjoint;
* globally upper-`q1`-target-disjoint; and
* `O(1/s)=O(r^{-1/2})`-spread in every containment star rooted at rank at
  most `r-h-1`.

In particular, the complementary owner layer retains

\[
              (1-O(r^{-1/2}))|\mathcal O(S)|          \tag{4.13}
\]

owners above every such lower target `S`.

The same conclusion holds while avoiding any independently prescribed
`o(W/s)` owner bank; quantitatively the remaining owners above `S` number
at least

\[
 |\mathcal O(S)|-|F\cap\mathcal O(S)|
                  -O(s/r)|\mathcal O(S)|.            \tag{4.14}
\]

#### Proof

The deadline asymptotic (4.11) is the established binomial-tail estimate.
Equation (4.12) follows from (4.2), while there are at most `2^k` tests.
Apply Theorem 4.1.  \(\square\)

## 5. Scope

This note proves the previously missing intersection of the two bank
marginals:

\[
 \boxed{
 \text{exact Catalan size}
 +\text{ owner/endpoint disjointness}
 +\text{ upper-`q1` disjointness}
 +\text{ low-star spread}.}
\tag{5.1}
\]

The proof needs no growing-uniformity nibble and no codegree estimate.  Its
two stages are:

1. greedy construction of a larger `Theta(W/s)` doubly-disjoint bank;
2. exact hypergeometric thinning to the required `Theta(W/s^2)` bank.

It does **not** prove:

1. disjointness of all natural lower suffix-deck targets of different
   collars;
2. the punctured prescribed-end ordered-four-transversal on the complement;
3. a compatible resident literal trace factor;
4. the arbitrary-width upper deck; or
5. `nu(k)<=B(k)+O(1)` or exact equality in all dimensions.
