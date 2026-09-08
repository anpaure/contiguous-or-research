# Exact fractional chain factor for the optimal triangular lower-cell profile

Date: 2026-08-01  
Status: unconditional all-`k` fractional theorem.  It matches the exact
`W+d` short-cell geometry.  It does not give an integral chain factor or a
serialized OR word.

## 0. Statement

Put

\[
 r=\lceil k/2\rceil,\qquad W=\binom kr,\qquad
 \Lambda=\sum_{s=1}^{r-1}\binom ks,
\]

and let

\[
 d=\min\left\{q:qW+\binom{q+1}{2}\ge\Lambda\right\}.
\]

There is an exact fractional chain decomposition of the strict lower ideal
with the following resources:

* one anchored chain of length at most `d` for each rank-`r` owner `T`; and
* `d` boundary chains of respective capacities `1,2,...,d`, generated
  jointly by one length-`d` singleton source prefix.

More precisely, there are probability distributions on those chain atoms
such that every owner and every boundary-chain address selects one chain
with total weight one, while every strict-lower target receives total weight
exactly one.

Thus the exact Ferrers capacity

\[
                        dW+\binom{d+1}{2}
\]

has no fractional containment or nested-chain obstruction.  The remaining
gap is integral selection of the atoms and their sliding-OR serialization.

## 1. The boundary deficit bank

Write

\[
                  h=(\Lambda-dW)_+.
\]

By definition of `d`,

\[
                  0\le h\le\binom{d+1}{2}.
\]

Consider the triangular board

\[
 \mathcal F_d=\{(i,s):1\le i\le d,\ 1\le s\le i\}.
\]

Choose any `h` cells of this board.  For each boundary address `i`, put

\[
 R_i=\{s:(i,s)\text{ was chosen}\},
\]

and for each rank `s` put

\[
 b_s=|\{i:s\in R_i\}|.
\]

Then

\[
 |R_i|\le i,\qquad \sum_s b_s=h,
 \qquad 0\le b_s\le d.
\]

All selected ranks satisfy `1<=s<=d<=r-1`.  Also

\[
 b_s\le d\le k\le\binom ks,
\]

so the rank deficits below are nonnegative.

## 2. The anchored owner chains

Set

\[
 p_s=\frac{\binom ks}{W},\qquad
 q_s=p_s-\frac{b_s}{W}.
\]

Then `0<=q_s<=1`, and

\[
 \sum_s q_s=
 \begin{cases}
   d,&\Lambda>dW,\\
   \Lambda/W\le d,&\Lambda\le dW.
 \end{cases}
\]

Hence `q=(q_s)` lies in the independence polytope of the uniform matroid
`U_(d,r-1)`.  Choose a random rank set `R` of size at most `d` with

\[
                         \Pr(s\in R)=q_s.
\]

For each owner `T`, independently choose a uniform ordering of its `r`
elements and retain the initial subsets at the ranks in `R`.  This is a
nested chain below `T` of length at most `d`.

For a fixed target `S` of rank `s`, its total weight in the owner chains is

\[
 \binom{k-s}{r-s}\frac{q_s}{\binom rs}
 =\frac{q_s}{p_s}
 =1-\frac{b_s}{\binom ks}.
\]

## 3. The boundary chains have one common source prefix

Choose one uniform ordering `pi=(pi_1,...,pi_k)` of the whole ground set and
put

\[
                         A_i=\{\pi_i\}\qquad(1\le i\le d).
\]

At boundary endpoint `i`, and for every `s in R_i`, retain the literal
suffix union

\[
             A_{i-s+1}\cup\cdots\cup A_i
               =\{\pi_{i-s+1},\ldots,\pi_i\}.        \tag{3.1}
\]

Because `R_i subseteq {1,...,i}`, these are legal cells and form a chain of
length at most `i`.  All `d` boundary chains arise from the **same** source
prefix, so their complete suffix-OR table already obeys the sliding cocycle.

A fixed rank-`s` target occurs in (3.1) with probability
`1/binom(k,s)`, since a fixed block of `s` positions in a uniform permutation
is a uniform `s`-subset.  Its total boundary weight is therefore

\[
                         \frac{b_s}{\binom ks}.
\]

Adding this to the owner contribution gives total target weight exactly one.
This proves the theorem.

## 4. Correct frontier

The sharper implication chain is

\[
 \boxed{
 \begin{array}{c}
 \text{optimal triangular fractional chains (proved)}\\
 \Downarrow\\
 \text{integral triangular chain factor (open)}\\
 \Downarrow\\
 \text{sliding-OR cocycle and upper/common-Q serialization (open).}
 \end{array}}
\]

The common singleton prefix strengthens the earlier independent-chain
formulation: no separate boundary-chain serialization theorem is needed at
the fractional level.  What is still missing is coupling the terminal
boundary state `(A_1,...,A_d)` to the first selected owner trace and then
rounding the complete coloured trace system integrally.

An anchored `D=ceil(Lambda/W)` factor is a clean sufficient subclass, but it
is stronger than the actual `B(k)` lower-cell geometry because it gives one
extra slot to every owner.  The physical optimum instead has only the
triangular boundary bank above.  Future sharp rounding statements should be
formulated for this triangular atom system, not solely for anchored
`D`-chains.
