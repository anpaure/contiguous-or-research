# Sparse-top SCD flag rounding and the single-SCD refinement barrier

**Date:** 2026-08-03  
**Status:** unconditional exact named-target theorem for the entire
noncontiguous residual ideal in all sufficiently large dimensions, plus a
linear obstruction to every construction which only splits one fixed SCD.
No computation is used.  The central collar attachment remains open.

## 0. Outcome

Put

\[
             k=2r,\qquad W={2r\choose r},\qquad
             p_s={{2r\choose s}\over W}.
\]

Let `d=d(2r)` be the optimal lower-bound depth, so

\[
                     {d\over\sqrt r}\longrightarrow
                     \alpha={\sqrt\pi\over2}.                 \tag{0.1}
\]

Fix any symmetric chain decomposition `S` of the Boolean lattice
`B_(2r)`.  The first theorem below gives a simple sufficient condition for
turning rank blocks in `S` into exact named-target flags on distinct
rank-`r` owners:

\[
 \boxed{\quad
      |B_j|\le d\text{ for every rank block},
      \qquad\sum_jp_{\max B_j}\le1.
      \quad}                                                \tag{0.2}
\]

The proof uses only one ordinary bipartite matching.  Every block--SCD
intersection is already a named inclusion chain.  Its top set is used as
an anchor, and the uniform containment flow assigns all anchors to distinct
middle owners.  Hence ownerwise prefix nesting is literal, not recovered
from rank marginals afterward.

Take

\[
                   a=\left\lceil {7\over8}\sqrt r\right\rceil,
                   \qquad u=r-a-1.                           \tag{0.3}
\]

Partition the residual ranks `1,...,u` by parity into blocks of `d`
successive ranks of that parity.  Their top ranks are

\[
                  u-2jd,qquad u-1-2jdqquad(j\ge0),         \tag{0.4}
\]

while positive.  In the following sum, terms with a nonpositive rank index
are omitted.  Then, for all sufficiently large `r`,

\[
   \sum_{j\ge0}\bigl(p_{u-2jd}+p_{u-1-2jd}\bigr)<1.         \tag{0.5}
\]

Consequently every named target of every residual rank `s<=u` admits an
exact partition into ownerwise flags such that

* every owner is used at most once;
* every flag has at most `d` targets;
* no flag contains two adjacent residual ranks; and
* every flag extends to the prefixes of one ordering of its assigned owner.

Arbitrary prescribed boundary families `B_s` may then be deleted from the
flags, giving exact multiplicities

\[
                         {2r\choose s}-|B_s|.                 \tag{0.6}
\]

Thus the named-target integrality gate is closed with **zero defect on the
whole residual ideal below the collar**.  This is stronger than merely
rounding its rank law.  What remains is to attach these exact residual flags
to an exact collar chainization while respecting the residual capacity and
bottom-containment rows of each owner.

The second theorem explains why that attachment needs genuine cross-chain
splicing.  If every output flag is required to stay inside one chain of one
fixed SCD, then any depth-`d` construction using at most `W` flags omits

\[
                              \Omega(W)                       \tag{0.7}
\]

strict-lower targets.  This holds even before the nonadjacent-rank
restriction is imposed.  Therefore splitting or chopping a single SCD
cannot prove an `o(W)` leave.

## 1. A general sparse-top block theorem

Let `J subseteq {1,...,r-1}` be partitioned into nonempty rank blocks

\[
                              J=B_1\dot\cup\cdots\dot\cup B_t,
\]

and put `s_j=max B_j`.

For a chain `C` of the fixed SCD, let

\[
                         C[B_j]=\{X\in C:|X|\in B_j\}.
\]

Discard empty intersections.

### Theorem 1.1 (sparse-top exact flag rounding)

Suppose

\[
                       |B_j|\le d\quad(j\in[t]),
                       \qquad \sum_{j=1}^t p_{s_j}\le1.     \tag{1.1}
\]

Then all named targets whose ranks lie in `J` can be partitioned into
inclusion flags and assigned injectively to rank-`r` owners so that:

1. every flag is one `C[B_j]` and has at most `d` targets;
2. its assigned owner contains every target in the flag; and
3. its targets are prefixes of one ordering of that owner.

If every block `B_j` has no two adjacent ranks, neither does any flag.

#### Proof

A symmetric chain is saturated.  Consequently, if it meets any rank in
`B_j`, then it also meets `s_j=max B_j<r`; it contains exactly one set of
that rank, and this set is the maximum of `C[B_j]`.  Conversely every
rank-`s_j` set belongs to one SCD chain and produces one nonempty chunk.
Hence the chunks with block label `j` are canonically indexed by the
complete layer

\[
                             { [2r]\choose s_j}.             \tag{1.2}
\]

Make a bipartite graph whose left vertices are all chunks and whose right
vertices are the rank-`r` owners.  Join a chunk with top `S` to every owner
`T` containing `S`.  A top of rank `s` has degree

\[
                             D_s={2r-s\choose r-s}.           \tag{1.3}
\]

Give every incident edge of such a chunk weight `1/D_s`.  The chunk load
is one.  A fixed owner contains `binom(r,s_j)` possible tops of rank `s_j`,
so its total load is

\[
 \sum_j{{r\choose s_j}\over {2r-s_j\choose r-s_j}}
 =\sum_j{{2r\choose s_j}\over {2r\choose r}}
 =\sum_jp_{s_j}\le1.                                    \tag{1.4}
\]

Thus (1.4) is a fractional matching saturating every chunk and respecting
unit owner capacities.  The bipartite matching polytope is integral (or,
equivalently, the fractional matching itself proves every Hall inequality),
so there is an integral matching saturating all chunks.

Every target in a chunk is contained in its top, hence in the assigned
owner.  A finite inclusion chain

\[
                         X_1\subset\cdots\subset X_h\subset T
\]

extends to an ordering of `T`: list first the elements of `X_1`, then the
successive differences, and finally the unused elements of `T`.  Its
prefixes at ranks `|X_i|` are exactly the `X_i`.  This proves all claims.
\(\square\)

### Corollary 1.2 (boundary deletion)

After Theorem 1.1, for each `s in J` delete any prescribed named family
`B_s` from rank `s`.  The remaining targets stay partitioned into flags on
the same owners, and their rank multiplicities are exactly
`binom(2r,s)-|B_s|`.

If a deleted target was the top used in the containment-matching proof,
keep the already assigned owner and ordering.  The deleted set may be
remembered as a proof-only containment certificate, but it is not a target,
not a marked prefix, and consumes no flag or owner capacity.  Equivalently,
the highest surviving target is itself contained in the same owner and is
a prefix of the retained ordering.  Empty flags are discarded, releasing
their owners.  Thus deletion can only decrease loads and cannot weaken
nesting or owner injectivity.

## 2. The parity-block residual construction

Use `a,u` from (0.3).  For every `j>=0`, define, omitting nonpositive
ranks,

\[
\begin{aligned}
 B_{0,j}&=\{u-2(jd+h):0\le h<d\},\\
 B_{1,j}&=\{u-1-2(jd+h):0\le h<d\}.
\end{aligned}                                             \tag{2.1}
\]

These sets partition `1,...,u`.  Every block has size at most `d` and lies
in one parity class.  Its top is one of the ranks in (0.4).  It remains to
prove (0.5).

### Lemma 2.1 (strict sparse-top inequality)

For the blocks (2.1), equation (0.5) holds for all sufficiently large `r`.

#### Proof

For `j=O(sqrt(r))`, the local central-binomial ratio gives, uniformly on
every fixed scaled window,

\[
 { {2r\choose r-j}\over {2r\choose r}}
                         =\exp(-j^2/r+o(1)).                 \tag{2.2}
\]

The general bound

\[
 { {2r\choose r-j}\over {2r\choose r}}
 \le \exp\left(-{j^2\over r+j}\right)
 \le \exp\left(-{j^2\over2r}\right)                      \tag{2.3}
\]

supplies a summable domination after using (0.1).  Therefore dominated
convergence for the series in (0.5) gives

\[
 \lim_{r\to\infty}
 \sum_{j\ge0}\bigl(p_{u-2jd}+p_{u-1-2jd}\bigr)
 =2\sum_{j\ge0}
      \exp\left[-\left({7\over8}+\sqrt\pi j\right)^2\right].
                                                               \tag{2.4}
\]

The last series is strictly below one.  Indeed its `j=0` term is below
`15/16`: the first four terms of the exponential series give

\[
 e^{49/64}>1+{49\over64}+{1\over2}\left({49\over64}\right)^2
       +{1\over6}\left({49\over64}\right)^3>{32\over15}.  \tag{2.5}
\]

For `j>=1`, use `sqrt(pi)>7/4`.  The first squared exponent is larger than
`(21/8)^2=441/64`, and consecutive squared exponents differ by more than
`49/4`.  Hence

\[
 2\sum_{j\ge1}e^{-(7/8+\sqrt\pi j)^2}
 <{2e^{-441/64}\over1-e^{-49/4}}<{1\over16}.              \tag{2.6}
\]

For the final elementary inequality, `e>8/3` implies
`e^{-49/4}<1/16` and `e^{441/64}>2^6>512/15`.
Equations (2.5)--(2.6) prove that the limit in (2.4) is below one.  The
strict inequality persists for all sufficiently large `r`. \(\square\)

### Theorem 2.2 (exact residual named-target flags)

For all sufficiently large `r`, all nonempty targets of ranks

\[
                         1\le s\le r-a-1
\]

have an exact ownerwise flag realization with at most `d` targets per
owner and no adjacent selected ranks.  It uses at most `W` owners.  After
arbitrary boundary deletion it realizes the exact residual inventory
(0.6).

#### Proof

Apply Theorem 1.1 to (2.1), using Lemma 2.1, and then Corollary 1.2.
\(\square\)

This theorem is fully labelled: every Boolean target occurs at its literal
set value, not merely with the correct rank count.  It also produces one
common owner ordering per nonempty flag.  Its patterns need not have the
equitable size histogram of the abstract rank-pattern theorem; only the
load cap, exact rank inventory, and nonadjacency are asserted.

## 3. A fixed-SCD refinement cannot have `o(W)` defect

Every SCD of `B_(2r)` has

\[
                 {2r\choose j}-{2r\choose j-1}              \tag{3.1}
\]

chains starting at rank `j` (with the second binomial read as zero at
`j=0`).  For `j>=1`, such a chain contains

\[
                              L_j=r-j                       \tag{3.2}
\]

nonempty strict-lower targets.  The unique chain starting at rank zero has
only `r-1` such targets, because the empty set is not a target.  This
one-chain correction is retained explicitly below.

Call a flag construction **one-SCD-refining** if every output flag is
contained in one chain of one fixed SCD.  Different flags may use the same
SCD chain, and their assigned owners may be arbitrary; targets from two
different SCD chains are never placed in one output flag.

### Theorem 3.1 (linear deletion barrier)

Let a one-SCD-refining construction use at most `W` flags, each containing
at most `d=d(2r)` targets.  Then it omits at least

\[
                              c_0W                             \tag{3.3}
\]

strict-lower targets for some absolute `c_0>0` and all sufficiently large
`r`.  The conclusion remains true if adjacent residual ranks are allowed.

#### Proof

If every nonempty strict-lower target were retained, the minimum number of
depth-`d` flags needed inside the separate SCD chains would be

\[
                           Q_r=\sum_C\left\lceil{L_C\over d}\right\rceil.
                                                               \tag{3.4}
\]

If the empty set were temporarily counted on the unique root chain, then
`L_C=r-j` for every chain starting at rank `j`.  Using
`ceil(L/d)=sum_(h>=0)1_{L>hd}` and telescoping (3.1) gives the corresponding
count

\[
 \widetilde Q_r=\sum_{h\ge0}{2r\choose r-hd-1}.             \tag{3.5}
\]

Removing the empty set changes the root-chain summand by at most one.
Therefore, for some `theta_r in {0,1}`,

\[
 Q_r=\widetilde Q_r-\theta_r,
 \qquad
 {Q_r\over W}
 ={1\over W}\sum_{h\ge0}{2r\choose r-hd-1}+O(W^{-1}).
                                                               \tag{3.6}
\]

The same central-binomial limit and domination as in Lemma 2.1 give

\[
 \lim_{r\to\infty}{Q_r\over W}
 =\sum_{h\ge0}e^{-\pi h^2/4}
 >1+e^{-\pi/4}>1.                                      \tag{3.7}
\]

Hence `Q_r>=(1+2c_0)W` for some absolute `c_0>0` and all sufficiently
large `r`.

Deleting one target from one SCD chain reduces
`ceil(L/d)` by at most one.  Therefore deleting `z` targets can reduce the
minimum required flag count by at most `z`.  If the remaining targets fit
in at most `W` flags, then

\[
                         W\ge Q_r-z,
\]

so `z>=Q_r-W>=2c_0W`, proving (3.3) after weakening the constant.
No nonadjacency assumption was used. \(\square\)

The barrier is specifically against refinement of one frozen SCD.  It does
not obstruct alternating splices between different SCD chains, assignment
of a chain fragment below a different owner, or the sparse-top construction
of Section 1; those are exactly the mechanisms an `o(W)` full construction
must exploit.

## 4. What is now closed and what remains

The exact integer rank-pattern theorem left two named-target questions:
residual chainization and joint collar attachment.  Theorem 2.2 closes the
first with zero defect below a `(7/8+o(1))sqrt(r)` collar.  In particular,
the favorable nonadjacent rank law is not merely fractionally clockable:
its complete residual named target set has an explicit exact integral flag
factor.

The unresolved condition is still correlated.  If a collar path ending at
owner `T` has bottom `B_T` and length `ell_T`, a residual flag assigned to
that owner must satisfy

\[
             \max F_T\subseteq B_T,
             \qquad |F_T|+\ell_T\le d.                     \tag{4.1}
\]

The matching in Theorem 1.1 sees only the owner `T`, not a selected collar
bottom or its remaining capacity.  Independently chainizing the collar and
then superposing the residual matching therefore remains invalid.

The exact next pure-mathematical target is a **capacitated cross-SCD
attachment theorem**: choose the sparse-top owner matching and the collar
chain decomposition jointly so that (4.1) holds, leaving `o(W)` or no
targets.  Theorem 3.1 proves that this theorem must use cross-chain splices;
chopping one canonical Greene--Kleitman SCD cannot suffice.
