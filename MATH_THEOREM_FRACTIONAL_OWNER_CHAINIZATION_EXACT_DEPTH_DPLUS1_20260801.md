# Exact fractional owner-chainization at depth `D<=d+1`

Date: 2026-08-01  
Status: unconditional all-`k` fractional theorem.  It strengthens the ideal
containment SDR from independent slots to nested owner chains, but it does
not round those chains integrally or serialize them as one OR chronology.

## 0. Statement

Put

\[
 r=\lceil k/2\rceil,\qquad W=\binom{k}{r},\qquad
 \Lambda=\sum_{s=1}^{r-1}\binom{k}{s},\qquad
 D=\left\lceil\frac{\Lambda}{W}\right\rceil .       \tag{0.1}
\]

An **owner-chain atom** is a pair `(T,C)`, where

\[
 T\in\binom{[k]}r
\]

and `C` is an inclusion chain of nonempty strict subsets of `T`, of length
at most `D`.

There are nonnegative weights `z_(T,C)` such that

\[
 \sum_C z_{T,C}=1\quad\hbox{for every owner }T,       \tag{0.2}
\]

and

\[
 \sum_{T,C:\,S\in C}z_{T,C}=1
 \quad\hbox{for every }S\subseteq[k],\ 1\le |S|<r. \tag{0.3}
\]

Thus the complete strict lower ideal has an exact fractional decomposition
into one chain of length at most `D` per middle owner.  Since the ideal-slot
theorem gives `d<=D<=d+1`, fractional nestedness costs at most the same one
extra row as unrestricted containment matching.

With chains restricted to length at most `d`, there is a fractional packing
whose total uncovered target mass is exactly

\[
                   h=(\Lambda-dW)_+.                 \tag{0.4}
\]

Hence neither containment nor nested owner-chain structure creates any
additional fractional loss beyond scalar capacity.

## 1. Rank marginals

For `1<=s<r`, define

\[
                         p_s=\frac{\binom{k}{s}}W.    \tag{1.1}
\]

Since the middle layer is largest,

\[
 0\le p_s\le1,\qquad \sum_{s=1}^{r-1}p_s
       =\frac{\Lambda}{W}\le D.                     \tag{1.2}
\]

The vector `p` therefore belongs to the independence polytope of the
uniform matroid `U_(D,r-1)`.  By integrality of that polytope, there is a
probability distribution on rank sets

\[
 R\subseteq\{1,\ldots,r-1\},\qquad |R|\le D,         \tag{1.3}
\]

such that

\[
                         \Pr(s\in R)=p_s             \tag{1.4}
\]

for every `s`.

## 2. The symmetric fractional chains

Fix an owner `T`.  Draw `R` from (1.3), and independently draw a uniform
ordering

\[
                         \pi=(t_1,\ldots,t_r)
\]

of the elements of `T`.  Set

\[
 C(T,R,\pi)=
 \bigl\{\{t_1,\ldots,t_s\}:s\in R\bigr\}.            \tag{2.1}
\]

This is an inclusion chain of length at most `D`.  Let `z_(T,C)` be the
probability that (2.1) equals `C`, aggregating equal chains.  Equation
(0.2) is immediate.

Fix a lower target `S` of rank `s`.  For an owner `T` containing `S`, the
rank-`s` member of a uniform maximal chain in `T` is uniform over
`binom(r,s)` choices.  Therefore

\[
 \Pr\bigl(S\in C(T,R,\pi)\bigr)=\frac{p_s}{\binom rs}.\tag{2.2}
\]

There are `binom(k-s,r-s)` owners containing `S`.  Consequently its total
weight is

\[
 \binom{k-s}{r-s}\frac{p_s}{\binom rs}
 =\binom{k-s}{r-s}\frac{\binom{k}{s}}{W\binom rs}
 =1,                                                   \tag{2.3}
\]

using

\[
 \binom{k}{s}\binom{k-s}{r-s}=W\binom rs.             \tag{2.4}
\]

This proves (0.3).

## 3. Sharp fractional deficiency at depth `d`

Write `rho=Lambda/W`.  If `rho<=d`, the preceding construction already
uses chains of expected rank-set vector in the `U_(d,r-1)` polytope and is
exact.

If `rho>d`, choose numbers

\[
 0\le q_s\le p_s,\qquad \sum_s q_s=d;                 \tag{3.1}
\]

for example `q_s=(d/rho)p_s`.  Repeat the construction with rank marginals
`q_s`.  Every owner still contributes one chain of length at most `d`, and
every rank-`s` target receives weight `q_s/p_s<=1`.  The total covered
target mass is

\[
 \sum_s\binom{k}{s}\frac{q_s}{p_s}
 =W\sum_s q_s=dW.                                     \tag{3.2}
\]

Thus the uncovered mass is `Lambda-dW=h`.  No depth-`d` fractional packing
can do better because its `W` owner chains contain at most `dW` target
positions.  This proves (0.4).

## 4. Exact remaining gate

The weights above are not an integral choice of one chain for each owner.
Independent sampling creates both repeated and uncovered lower targets.
Even an integral owner-chain factor would still need a common endpoint
ordering whose suffix ORs are those chains and whose central/upper language
and residence remain valid.

The logical frontier is therefore

\[
 \text{fractional owner chains (proved)}
 \longrightarrow
 \text{integral owner-chain factor}
 \longrightarrow
 \text{one serialized OR chronology}.                \tag{4.1}
\]

This theorem rules out a fractional chainization obstruction.  It does not
claim an equitable Boolean-lattice chain partition, a hypergraph rounding
theorem, or a universal word.
