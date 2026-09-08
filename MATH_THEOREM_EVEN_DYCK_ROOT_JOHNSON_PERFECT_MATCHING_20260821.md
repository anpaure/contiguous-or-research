# Even Dyck roots have a constructive Johnson perfect matching

**Status:** theorem-grade corollary of the Ruskey--Proskurowski adjacent-
transposition Gray path.  The source-verified input is a Hamilton **path**;
no Hamilton-cycle claim is needed or made.

## 1. Conventions

For an integer `r>=1`, let

\[
 \mathcal D_r=\left\{x\in\{0,1\}^{2r}:
 |x|_1=r,\quad
 \sum_{j=1}^t(2x_j-1)\geq0\quad(1\leq t\leq2r)
 \right\}.                                      \tag{1.1}
\]

Thus `1` is an opening step and `0` is a closing step.  Equivalently, every
prefix has at least as many `1`s as `0`s.  Put

\[
 S(x):=\{j\in[2r]:x_j=1\},\qquad
 \mathscr D_r:=\{S(x):x\in\mathcal D_r\}.        \tag{1.2}
\]

Let

\[
 G_r:=J(2r,r)[\mathscr D_r]                       \tag{1.3}
\]

be the graph induced by the Dyck `r`-subsets in the Johnson graph.  Thus two
vertices are adjacent in `G_r` precisely when their symmetric difference has
size two.

## 2. The cited Gray-path input

Ruskey and Proskurowski use exactly the convention (1.1): their `T(n)` is the
set of bitstrings with `n` ones and `n` zeros in which no prefix has more
zeros than ones.  Their adjacent-transposition result is:

> The elements of `T(n)` admit a listing in which every two successive
> bitstrings differ by transposing two adjacent bits if and only if `n` is
> even or `n<5`.  In the affirmative cases they give a constant-average-time
> generation algorithm.

For the present theorem only the even case is used.  In graph language, the
listing is a Hamilton path in the graph on `\mathcal D_r` whose edges are
adjacent swaps `10<->01`.  Neither the paper's abstract nor the standard
definition of a Gray-code *listing* asserts a closing edge from the last word
to the first.  No such cyclic assertion is used below.

The primary citation is F. Ruskey and A. Proskurowski, *Generating Binary
Trees by Transpositions*, **Journal of Algorithms 11** (1990), 68--84,
[doi:10.1016/0196-6774(90)90030-I](https://doi.org/10.1016/0196-6774(90)90030-I).
The publisher abstract states both the definition of `T(n)`, the sharp
even-or-small existence condition, and the constant-average-time algorithm.
For a modern explicit cross-check of the conventions and the word “listing,”
see T. Mütze, *Combinatorial Gray Codes---an Updated Survey*, Section 4.4,
[doi:10.37236/11023](https://doi.org/10.37236/11023).

## 3. Perfect-matching corollary

### Theorem 3.1

For every positive even integer `r`, the induced Johnson graph `G_r` has a
perfect matching.  Moreover, such a matching is constructive from the
Ruskey--Proskurowski adjacent-transposition generator.

#### Proof

Let

\[
 x^{(1)},x^{(2)},\ldots,x^{(C_r)}                 \tag{3.1}
\]

be the Ruskey--Proskurowski listing of `\mathcal D_r`, where

\[
 C_r=|\mathcal D_r|=\frac1{r+1}\binom{2r}{r}.     \tag{3.2}
\]

Two distinct binary words related by transposing adjacent positions must
have `10` in those positions in one word and `01` in the other.  Hence, for
each `i<C_r`, the sets `S(x^(i))` and `S(x^(i+1))` differ by removing one of
two consecutive coordinates and inserting the other.  In particular,

\[
 |S(x^{(i)})\mathbin\triangle S(x^{(i+1)})|=2,    \tag{3.3}
\]

so (3.1) maps under (1.2) to a Hamilton path in `G_r`.

It remains only to check that this path has an even number of vertices.  If
`r` is even, then `r+1` is odd and

\[
 \binom{2r}{r}=2\binom{2r-1}{r-1}.                \tag{3.4}
\]

Because the odd number `r+1` divides the left side of (3.4), it also divides
`\binom{2r-1}{r-1}`.  Consequently

\[
 C_r=2\,\frac{\binom{2r-1}{r-1}}{r+1}             \tag{3.5}
\]

is even.  Therefore

\[
 \mathcal M_r:=\bigl\{
   \{S(x^{(2j-1)}),S(x^{(2j)})\}:1\leq j\leq C_r/2
 \bigr\}                                         \tag{3.6}
\]

is a family of Johnson edges, is pairwise vertex-disjoint, and covers every
vertex of `G_r`.  It is a perfect matching. `square`

### Constructive form

Run the Ruskey--Proskurowski adjacent-transposition generator and buffer one
word.  Pair output words 1 and 2, then 3 and 4, and so on.  In the transition
representation used by Gray-code generators, this preserves their constant
average generation time; explicitly materializing every length-`2r` word of
course costs `Theta(r)` output time per word.

## 4. Scope checks

1. A Hamilton **cycle** is unnecessary: (3.6) uses only the edges in
   positions `(1,2),(3,4),...` of the Hamilton path and never uses a
   last-to-first edge.
2. The exceptional odd cases `r=1,3` do have adjacent-transposition Gray
   paths by the cited theorem, but `C_1=1` and `C_3=5` are odd, so consecutive
   pairing cannot be perfect.
3. For odd `r>=5`, nonexistence of an adjacent-transposition Hamilton path
   does **not** imply nonexistence of a perfect matching in `G_r`; that is a
   different and weaker graph property.
4. The older unrestricted-transposition recursion recorded elsewhere in this
   workspace is not the input used here.  The present reduction specifically
   uses the adjacent-transposition theorem, although any Hamilton path in
   `G_r` would suffice.

## 5. Finite audit

The independent standard-library checker
`scratch/audit_even_dyck_johnson_perfect_matching_20260821.py` enumerates the
Dyck words, constructs the adjacent-swap graph, checks that every such edge is
a Johnson edge, and computes exact bipartite maximum matchings for small
semilengths.  This is a regression audit only; Theorem 3.1 is the analytic
corollary above and is not inferred from finite computation.

An H100 CPU replay (`arboghast`, Python 3.12.3) checked every `1<=r<=10`.
For even `r=2,4,6,8,10`, it found respectively

\[
 (|V|,\nu)=(2,1),(14,7),(132,66),(1430,715),(16796,8398),
\]

and verified that each computed maximum matching is perfect.  It ended
`PASS`.  Checker
SHA-256:

```text
980c3a056beeb7d9f38a8dcea789efac5d7504c57fcf447bbd709c02c626c48d
```
