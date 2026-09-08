# The third overlap moment is a two-path polymer term

**Date:** 2026-08-21  
**Status:** analytic fixed-order moment theorem; no growing-order polymer
summation or adaptive-nibble theorem is claimed

## 1. Setup

Put `b=2r+1`, and let `C_r` be the directed punctured-configuration
hypergraph.  Thus a word retains its `2r` rank-`r` cyclic windows and its
`2r` rank-`(r-1)` cyclic windows at starts different from zero.  Write

\[
 D_M=2r\,r!(r+1)!
\]

for the middle-target degree.  Fix one configuration `e`, and for every
configuration `F` put

\[
 t_F=|e\cap F|,\qquad
 M_3(e):=\sum_F {t_F\choose3}
        =\sum_{T\in{e\choose3}}\deg(T).                 \tag{1.1}
\]

Inside `e`, let `Gamma_e` be the union of

1. the alternating path of lower--middle containment pairs; and
2. the path of disjoint middle--middle pairs.

These are exactly the two pair types whose codegree is `Theta(D_M/r)`.
Every other pair inside `e` has codegree `O(D_M/r^2)`.

## 2. Exact three-arc formula

For an ordered triple of distinct targets `T=(A_1,A_2,A_3)`, let
`k_i=|A_i|`, and for `epsilon in {0,1}^3` put

\[
 n_\epsilon(T)=
 |\{x\in[b]:({\bf1}_{x\in A_1},{\bf1}_{x\in A_2},
                    {\bf1}_{x\in A_3})=\epsilon\}|.     \tag{2.1}
\]

Let `p_k(n)` be the number of ordered triples of retained cyclic starts
whose positional arcs of lengths `k_1,k_2,k_3` have Venn-cell vector `n`.

### Lemma 2.1 (Venn signature count)

For every triple `T`,

\[
             \deg(T)=p_{\bf k}({\bf n}(T))
                      \prod_{\epsilon\in\{0,1\}^3}n_\epsilon(T)! .
                                                               \tag{2.2}
\]

#### Proof

Fix the three retained starts.  A word realizes the prescribed targets at
those starts exactly when, for every membership vector `epsilon`, it maps
the `n_epsilon` ground labels in that Venn cell bijectively to the
positional coordinates having the same membership vector.  This gives
`product n_epsilon!` words.  Conversely, the three nonempty proper target
sets have unique cyclic starts in a word, so no word is counted at two
start triples.  Summing over positional signatures proves (2.2). `square`

## 3. The connected three-target contribution

The graph `Gamma_e[T]` has at most two edges.  If it has two, then it is a
length-two path.  Directly applying (2.2) gives the following complete
inventory.  Here `ell` is the number of lower targets.

\[
\begin{array}{c|c|c|c}
\ell&\text{number of target triples}&\text{triple codegree(s)}
 &\text{total divided by }D_M\\ \hline
0&(r-1)\text{ of each of two orientations}
 &4(r-1)r!(r-1)!
 &\displaystyle {4(r-1)^2\over r^2(r+1)}\\[2mm]
1&(4r-2),(4r-4),(2r-1)
 &2(4r-3)r!(r-1)!,\ 2(4r-3)r!(r-1)!,\
   2(2r-1)r!(r-1)!
 &\displaystyle {36r^2-52r+19\over r^2(r+1)}\\[2mm]
2&2r-1
 &2(2r-1)(r+1)!(r-2)!
 &\displaystyle {(2r-1)^2\over r^2(r-1)}.
\end{array}                                                \tag{3.1}
\]

For example, the three `ell=1` rows are respectively a middle target
joined to one contained lower target and one disjoint middle target, the
reflected version, and a lower target contained in two middle targets.
The `ell=2` row is the dual containment path.  The `ell=0` rows are the two
orientations of a length-two segment in the middle disjointness path.

Consequently the total two-skeleton-edge contribution is

\[
 {44\over r}+O(r^{-2}).                                  \tag{3.2}
\]

## 4. The disconnected three-arc tail

### Lemma 4.1 (three-arc endpoint tail)

The total codegree of triples spanning at most one edge of `Gamma_e` is

\[
 \sum_{\substack{T\in{e\choose3}\\
                  |E(\Gamma_e[T])|\le1}}\deg(T)
                  =O(D_M/r^2).                           \tag{4.1}
\]

#### Proof

Represent each target by the two boundary positions of its base cyclic
arc.  Fixing the cyclic weak order of the at most six boundaries leaves at
most two free gap variables; there are only constantly many weak orders
for each of the four layer multisets `MMM,MML,MLL,LLL`.  Formula (2.2)
then turns every case into a product of reciprocal binomial or multinomial
coefficients.  The only boundary terms of order `D_M/r` are precisely the
six length-two skeleton paths already listed in (3.1).

After those terms are removed, the endpoint sums have the following
orders.  The rows are the number `ell` of lower targets and the columns are
the number of skeleton edges.

\[
\begin{array}{c|ccc}
\ell&0&1&2\\ \hline
0&O(r^{-3})&O(r^{-2})&\text{the first row of (3.1)}\\
1&O(r^{-2})&O(r^{-2})&\text{the second row of (3.1)}\\
2&O(r^{-2})&O(r^{-2})&\text{the third row of (3.1)}\\
3&O(r^{-2})&0&0.
\end{array}                                               \tag{4.2}
\]

All entries in (4.2) are normalized by `D_M`.  To bound the tails, merge
adjacent Venn cells and repeatedly use

\[
 {u!v!\over(u+v)!}={1\over{u+v\choose u}},\qquad
 \sum_{j=1}^{n-1}{1\over{n\choose j}}=O(n^{-1}),          \tag{4.3}
\]

together with its two-gap multinomial analogue, whose sum is `O(n^-2)`.
There are constantly many endpoint weak orders, so the bounds are uniform.
This proves (4.2), and summing its seven non-skeleton entries proves
(4.1). `square`

## 5. Third factorial moment

### Theorem 5.1

Uniformly over directed punctured configurations,

\[
 \boxed{\qquad
 {M_3(e)\over D_M}={44\over r}+O(r^{-2}).
 \qquad}                                                  \tag{5.1}
\]

#### Proof

Coordinate relabelling makes `M_3(e)` independent of `e`.  The triples
with two skeleton edges contribute (3.1), hence (3.2).  Lemma 4.1 bounds
all remaining triples by `O(D_M/r^2)`. `square`

This is the first higher-overlap analogue of the pair identity
`M_2(e)=S(e)=(12+O(1/r))D_M`.  It shows that the first nontrivial polymer
correction loses a full factor `1/r`; it does not control moments whose
order grows with `r`.

## 6. Reproducibility and scope

The standard-library exact counter

`scratch/research_punctured_configuration_third_moment_20260821.py`

uses (2.2), not permutation enumeration.  It matches the independent full
intersection histograms through `r=5` and evaluates the exact moment
through `r=25`.  The values of `r M_3/D_M` at `r=5,10,15,20,25` are

\[
 76.2374,\quad57.2639,\quad52.6243,\quad50.4613,\quad49.1778,
\]

consistent with the limit `44` and the analytic endpoint estimate above.
The computation is a regression check; Theorem 5.1 rests on the Venn-cell
count and endpoint bounds.
