# A fresh-block hotspot defeats local companion sampling

**Date:** 2026-08-05  
**Method:** a fixed marked-owner kernel, random path packing inside its
roles, and a first-moment collision deletion; no computation or search  
**Status:** unconditional sharp obstruction.  The spectral fresh-path
packing theorem, even together with a uniform local companion choice and
pre-reserved-bank orbit survival, does not imply `(CE)`.  A near-complete
fresh-path packing may contain `Theta(N_*/d^2)` pairwise vertex-disjoint
blocks for which one fixed marked level-two owner is a legal companion.
Independent uniform local choices then hit that occurrence with probability
`Theta(d^-2)`, a factor `Theta(d)` above the required one-point intensity
`Theta(d^-3)`.  A spread lower packing, a hotspot deletion theorem, or a
joint dependent rounding is genuinely necessary.

## 1. A common marked owner

Work in the central range

\[
                         t=r-d,
 \qquad d\to\infty,
 \qquad d^2=O(r),
 \qquad r=\Theta(k).
\tag{1.1}
\]

Put

\[
                         \ell=d-2.
\tag{1.2}
\]

Fix a rank-`r` owner `T` and a coordinate `z in T`.  For every

\[
 P\in{T\choose r-d+2},
 \qquad z\in P,                                           \tag{1.3}
\]

the marked occurrence `(T,z)` can be a level-two copy with common kernel
`P`: its private tail is the unique set `T-P` of size `ell`.

The number of such kernels is

\[
                         D_*={r-1\choose\ell}.              \tag{1.4}
\]

## 2. A random fresh path through one kernel

For a fixed `P` in (1.3), choose

* `b_1` uniformly in `P-{z}`;
* an ordered `d`-tuple `A=(a_1,...,a_d)` from
  `P-{z,b_1}`;
* `C=P-(A union {b_1,z})`, so `|C|=t-d`; and
* an ordered `(d-3)`-tuple `(b_3,...,b_(d-1))` outside `T`.

Put `b_2=z` and define

\[
 S_j=C\cup\{a_{j+1},\ldots,a_d\}
          \cup\{b_1,\ldots,b_j\},
 \qquad 0\le j<d.                                        \tag{2.1}
\]

The event labels are all distinct, so (2.1) is a fresh `d`-vertex Johnson
path.  Its duplicate-macro kernel is exactly `P`, its common second mark is
`z`, and `(T,z)` is one of its legal prospective marked level-two owners.

The stabilizer of `(T,z)` makes each path role uniform on one explicit
stratum.  The two smallest strata are

\[
 \begin{aligned}
 \mathcal U_0&=\mathcal U_1
   =\{S\in{T\choose t}:z\notin S\},\\
 |\mathcal U_0|&={r-1\choose t}={r-1\choose d-1}.
 \end{aligned}                                            \tag{2.2}
\]

Role two is uniform on the `t`-subsets of `T` containing `z`, of size

\[
                         {r-1\choose d}.                    \tag{2.3}
\]

For `j>=3`, put `u=j-2`.  Role `j` is uniform on the sets having exactly
`u` points outside `T` and containing `z`; its stratum has size

\[
                         N_j={k-r\choose u}{r-1\choose d+u}.
\tag{2.4}

Since `0<=u<=d-3` and `2d=o(r)`, binomial unimodality gives, for all
sufficiently large parameters,

\[
                         N_j\ge {r-1\choose d-1}.           \tag{2.5}
\]

Finally,

\[
 { {r-1\choose d-1}\over D_*}
 ={r-d+1\over d-1}=\Theta(d).                              \tag{2.6}
\]

## 3. A large vertex-disjoint hotspot family

### Theorem 3.1

There is a family `mathcal G` of pairwise lower-vertex-disjoint fresh paths
of the form (2.1), with distinct kernels, such that

\[
 \boxed{
                         |\mathcal G|=\Theta(D_*/d^2).}      \tag{3.1}
\]

Every path in `mathcal G` has common second mark `z` and admits `(T,z)` as
a marked level-two occurrence.

#### Proof

Take

\[
                         L=\lfloor D_*/d^2\rfloor           \tag{3.2}
\]

independent samples from Section 2, including independent uniform kernels
from (1.3).

The expected number of pairs with the same kernel is at most

\[
                         {L\choose2}/D_*=O(L/d^2).          \tag{3.3}
\]

For two independently sampled paths, a collision between their roles zero
and one has probability at most

\[
                         {4\over {r-1\choose d-1}}.         \tag{3.4}
\]

Role two has a different `z`-status and contributes at most the reciprocal
of (2.3).  Roles `j>=3` with different `j` have different numbers of points
outside `T`, while equal roles contribute at most `1/N_j`.  Equations
(2.2)--(2.5) therefore give

\[
 \Pr(\text{two sampled paths share a lower vertex})
 \le {d+2\over {r-1\choose d-1}}.                          \tag{3.5}
\]

Using (2.6), the expected number of colliding path pairs is

\[
 {L\choose2}{d+2\over {r-1\choose d-1}}
                         =O(L/d^2).                         \tag{3.6}
\]

Choose a realization no worse than twice the sum of (3.3) and (3.6).
Delete one path from every duplicate-kernel or lower-vertex collision.
Only `O(L/d^2)=o(L)` paths are deleted, proving (3.1).  \(\square\)

### Corollary 3.2 (the hotspot fits inside a near-complete packing)

The family `mathcal G` extends to a fresh-path packing leaving fewer than
`30M/d` lower vertices uncovered, where `M=binom(k,t)`.

#### Proof

The hotspot uses

\[
                         d|\mathcal G|=O(D_*/d)             \tag{3.7}
\]

lower vertices.  Since

\[
                         \log D_*=\Theta(d\log d),
 \qquad
                         \log M=\Theta(d^2),                \tag{3.8}
\]

this is `o(M/d)`.  Starting with `mathcal G`, greedily add fresh paths
until none remains.  Lemma 2.1 of
`MATH_THEOREM_FRESH_JOHNSON_PATH_PACKING_AND_ALL_ORDER_RESIDUAL_20260805.md`
says that every uncovered family of size at least `30M/d` contains another
fresh path.  Hence the final uncovered family is smaller than `30M/d`.
\(\square\)

Thus the existing near-complete packing theorem permits the hotspot; it
does not impose endpoint-kernel spread.

## 4. Uniform local companion sampling violates the cylinder

Fix `h in {2,3}`.  For one hotspot path, choose the `h` private level-two
tails uniformly among pairwise disjoint `ell`-sets in the available queue
pool.  Choose the terminal labels outside `T`.

After removing `C,A,B` and the `h` terminal labels, the tail pool has size

\[
                         q-h,
 \qquad q=k-r+1.                                           \tag{4.1}
\]

It contains the distinguished tail `T-P`.  By symmetry of the uniform
`h`-matching of tails, the probability that this distinguished tail is one
of the `h` copies equals

\[
                         p_*={h\over {q-h\choose\ell}}.     \tag{4.2}
\]

The central ratios and (1.4) give

\[
                         {D_*\over {q-h\choose\ell}}
                              =\Theta(1).                   \tag{4.3}
\]

Make the local choices independently over the paths in `mathcal G`.  The
number proposing the fixed marked occurrence `(T,z)` has mean

\[
 |\mathcal G|p_*=\Theta(d^{-2}).                            \tag{4.4}
\]

Since this mean tends to zero, the probability that exactly one hotspot
macro proposes `(T,z)` is also

\[
                         \Theta(d^{-2}).                    \tag{4.5}
\]

This remains true if a collision rule retains the unique proposal and
deletes every macro whenever two or more propose the same owner.

But the required marked one-point scale is

\[
                         \eta_*={H\over Wr}
                           =(1+o(1)){1\over r(d+1)}
                           =\Theta(d^{-3}).                 \tag{4.6}
\]

Therefore (4.5) exceeds (4.6) by a factor `Theta(d)`.

## 5. Banks do not remove the obstruction

The two pre-reserved banks occupy only `O(W/d)` owners.  After a bank pair
is fixed, choose `T` outside their union; there are still
`(1-O(1/d))W` choices.  The hotspot construction then takes place in its
unreserved local roles.  Alternatively, if `T` is fixed before the uniform
bank draw, it survives with probability `1-O(1/d)`.

Hence the simultaneous local-orbit survival theorem for random banks is
fully consistent with the obstruction.  Every individual orbit is large;
too many lower blocks are allowed to point at the same marked owner.

## 6. Exact conclusion

The following implication is false:

\[
 \boxed{
 \text{near-complete fresh block packing}
 +\text{uniform surviving local companion choices}
 \Longrightarrow (CE).}
\tag{6.1}
\]

The failure already occurs at the one-point root factor, before shared
`b_1` marks are exposed.  Therefore the missing integral theorem must do at
least one of the following:

1. construct the fresh lower packing with a uniform endpoint-kernel load;
2. delete every hotspot with total loss `O(H/d)` and prove this globally;
3. select lower blocks and owner companions jointly by a spread dependent
   rounding; or
4. use an acceptance-aware nibble which proves the local marked cluster
   rows on every residual.

The complete-orbit companion count remains correct and exponentially
strong.  What fails is the quantifier from an arbitrary integral lower
packing to that orbit law.

