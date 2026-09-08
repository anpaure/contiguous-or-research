# A scale-matched obstruction to parameter-only growing-rank nibble iteration

**Status (2026-08-21).**  Everything in this note is proved.  The construction
shows that exact regularity, `r Delta_2/Delta=o(1)`, and even an `o(1)` squared
local codegree kernel do **not** by themselves force an almost-perfect matching
when the rank grows.  The example can be written in the same one-slot-plus-target
shape as the central slot hypergraph and can be tuned to the same numerical
scales

\[
 r=\Theta(n\log n),\qquad
 {\Delta_2\over\Delta}=O\!\left({\log n\over n^2}\right),\qquad
 \Xi=O\!\left({\log^2 n\over n}\right).
\]

Nevertheless every matching covers only `O(1/n)` of its vertices.

This is **not** a counterexample to the Johnson-distance free-history palette.
The construction below has a latent target-position partition which that palette
does not visibly have.  Its precise consequence is narrower and important: the
maximum codegree, the one-bite lemma, and the squared-kernel estimate extracted
from the central exact profile cannot, without an additional global mixing or
anti-partition input, justify the desired iteration.

The absolute degree is not a hidden escape from the example.  Replacing every
edge by an arbitrary common number of parallel copies makes the degree as large
as desired while leaving all normalized codegrees, every `Xi_H(v)`, and the
matching number unchanged.

## 1. Statement

For an `r`-uniform `D`-regular multihypergraph `H`, put

\[
 \delta(H)={\Delta_2(H)\over D},\qquad
 \Xi_H(v)=\sum_{w\ne v}
 \left({\operatorname{codeg}_H(v,w)\over D}\right)^2.       \tag{1.1}
\]

Parallel edge copies are counted separately in degrees and codegrees.

### Theorem 1.1 (equipartition obstruction)

Let `D>=4` and let `r` satisfy

\[
 r\ge 64\log(2eDr).                                      \tag{1.2}
\]

There are arbitrarily large integers `L` and an `r`-partite, `r`-uniform,
`D`-regular multihypergraph `H` with `L` vertices in every part such that

\[
 \Delta_2(H)\le2,\qquad
 \max_v\Xi_H(v)\le {2(r-1)\over D},                      \tag{1.3}
\]

but

\[
 {r\nu(H)\over |V(H)|}
 \le {32\log(2eDr)\over r}.                             \tag{1.4}
\]

Thus, along any sequence with `r/D -> 0` and
`log(Dr)/r -> 0`, one has

\[
 r\delta(H)=o(1),\qquad \max_v\Xi_H(v)=o(1),             \tag{1.5}
\]

while a maximum matching covers only `o(|V(H)|)` vertices.

The first vertex part may be called the **slot part** and the union of the
remaining `r-1` parts the **target set**.  Every edge then contains exactly one
slot and `r-1` targets, every slot and target has the same degree `D`, and still
(1.3)--(1.4) hold.

### Corollary 1.2 (arbitrary degree inflation)

For every positive integer `lambda`, replace each edge of the hypergraph in
Theorem 1.1 by `lambda` labeled parallel copies.  The resulting hypergraph is
`lambda D`-regular and has

\[
 {\Delta_2\over\Delta}\le {2\lambda\over\lambda D}
 ={2\over D},\qquad
 \Xi(v)\le {2(r-1)\over D}.                            \tag{1.6}
\]

Its matching number is exactly the original matching number, because parallel
copies cannot occur together in a matching.  Hence the absolute degree may be
polynomial, exponential, or superexponential in `r` without changing any
conclusion of Theorem 1.1.

## 2. Random equipartitions

Fix `D,r`.  Let `L` tend to infinity and put

\[
 M=LD.
\]

On a set `X` of size `M`, independently choose `r` uniformly random
equipartitions

\[
 \mathcal P_i=\{B_{i,1},\ldots,B_{i,L}\},\qquad i\in[r],  \tag{2.1}
\]

each consisting of `L` blocks of size `D`.

We need two simultaneous properties:

1. blocks from distinct partitions have intersection at most two;
2. there is no large set meeting every block of every partition in at most one
   point.

Both occur together with positive probability for all sufficiently large `L`.

### Lemma 2.1 (all cross-intersections are at most two)

If `M/(r^2D^4) -> infinity`, then with probability `1-o(1)`,

\[
 |B\cap C|\le2                                      \tag{2.2}
\]

for every `B in P_i`, `C in P_j`, and `i ne j`.

#### Proof

For fixed blocks `B,C` from two independently chosen partitions, each is a
uniform `D`-subset of `X`, independently of the other.  Hence

\[
 \Pr(|B\cap C|\ge3)
 \le \mathbb E { |B\cap C|\choose3}
 ={ {D\choose3}^2\over {M\choose3}}.                    \tag{2.3}
\]

There are `binom(r,2)L^2` unordered choices of two partitions and one block
from each.  The expected number of violations of (2.2) is therefore at most

\[
 {r\choose2}L^2 { {D\choose3}^2\over {M\choose3}}
 =O\!\left({r^2D^4\over M}\right)=o(1).                 \tag{2.4}
\]

Markov's inequality proves the claim.  \(\square\)

Call `S subseteq X` a **common partial transversal** if

\[
 |S\cap B|\le1
 \quad\hbox{for every }B\in\mathcal P_i\hbox{ and every }i\in[r].
                                                               \tag{2.5}
\]

### Lemma 2.2 (no large common partial transversal)

Put

\[
 Q=\log(2eDr),\qquad c={16Q\over r}.                    \tag{2.6}
\]

Under (1.2), for all sufficiently large `L`, with probability `1-o(1)` there
is no common partial transversal of size

\[
 s=\lceil cL\rceil.                                    \tag{2.7}
\]

#### Proof

Fix an `s`-set `S`.  In one uniform equipartition, expose the block positions
of its points in an arbitrary order.  The probability that they occupy distinct
blocks is exactly

\[
 p_s={ (L)_sD^s\over (M)_s}
 =\prod_{j=0}^{s-1}{1-j/L\over1-j/M}.                  \tag{2.8}
\]

Since (1.2) gives `c<=1/4`, for large `L` we have `s<=L/2`.  Using
`log(1-x)<=-x` and `-log(1-y)<=2y` for `0<=y<=1/2`, and recalling `M=LD`
and `D>=4`,

\[
 \begin{aligned}
 \log p_s
 &\le -{s(s-1)\over2L}+{s(s-1)\over M}\\
 &\le -{s(s-1)\over4L}.                               \tag{2.9}
 \end{aligned}
\]

The partitions are independent.  If `Z_s` counts common partial transversals
of size `s`, then

\[
 \mathbb E Z_s
 \le {M\choose s}\exp\!\left(-{rs(s-1)\over4L}\right)
 \le \left({eM\over s}\right)^s
      \exp\!\left(-{rs(s-1)\over4L}\right).            \tag{2.10}
\]

For sufficiently large `L`, (2.7) gives `s-1>=cL/2`, while

\[
 \log {eM\over s}
 \le\log {eD\over c}
 \le\log(eDr)<Q.                                      \tag{2.11}
\]

Also `rc/8=2Q`.  Inserting these estimates into (2.10) yields

\[
 \mathbb E Z_s\le e^{-sQ}=o(1).                        \tag{2.12}
\]

Another application of Markov's inequality proves the lemma.  \(\square\)

Choose `L` so large that `M/(r^2D^4)` is arbitrarily large and the failure
probabilities in Lemmas 2.1 and 2.2 have sum below one.  Hence deterministic
equipartitions satisfying both conclusions exist.  This also proves the
"arbitrarily large `L`" clause in Theorem 1.1.

## 3. The block-incidence hypergraph

Fix equipartitions with the two properties above.  Define `H` by

\[
 V(H)=\{(i,B):i\in[r],\ B\in\mathcal P_i\}.             \tag{3.1}
\]

For every `x in X`, let `B_i(x)` be the unique block of `P_i` containing
`x`, and add the edge

\[
 e_x=\{(i,B_i(x)):i\in[r]\}.                            \tag{3.2}
\]

The point `x` labels this edge, so equal sets in (3.2), if any, remain distinct
parallel copies.

Every edge has one vertex in each of the `r` parts.  Every vertex `(i,B)` lies
in exactly the `D` edges indexed by the points of `B`.  Thus `H` is exactly
`r`-uniform and `D`-regular, with

\[
 |V(H)|=rL.                                             \tag{3.3}
\]

Vertices in the same part have codegree zero.  For `i ne j`,

\[
 \operatorname{codeg}_H((i,B),(j,C))=|B\cap C|\le2.    \tag{3.4}
\]

This proves the maximum-codegree assertion in (1.3).

For a fixed vertex `v=(i,B)`, use `t^2<=2t` for `t in {0,1,2}` and the fact
that the blocks of each `P_j` partition `X`.  Then

\[
 \begin{aligned}
 \Xi_H(v)
 &=\sum_{j\ne i}\sum_{C\in\mathcal P_j}
       \left({|B\cap C|\over D}\right)^2\\
 &\le {2\over D^2}\sum_{j\ne i}\sum_{C\in\mathcal P_j}|B\cap C|\\
 &={2(r-1)\over D}.                                    \tag{3.5}
 \end{aligned}
\]

This proves the kernel assertion in (1.3).

Finally, a set of edges `{e_x:x in S}` is a matching precisely when no block
of any partition contains two points of `S`; equivalently, precisely when `S`
is a common partial transversal.  Lemma 2.2 therefore gives `nu(H)<s`.  For
large `L`,

\[
 {r\nu(H)\over|V(H)|}={\nu(H)\over L}
 <{s\over L}\le2c={32Q\over r},                        \tag{3.6}
\]

which is (1.4) and completes the proof of Theorem 1.1.  \(\square\)

## 4. Exact comparison with the central asymptotic scale

Let the new asymptotic parameter be `n` and take, after harmless integer
rounding,

\[
 r=\Theta(n\log n),\qquad D=\Theta(n^2/\log n).         \tag{4.1}
\]

Condition (1.2) holds.  The constructed hypergraphs satisfy

\[
 {\Delta_2\over\Delta}\le {2\over D}
 =O\!\left({\log n\over n^2}\right),                  \tag{4.2}
\]

\[
 r{\Delta_2\over\Delta}
 =O\!\left({\log^2 n\over n}\right)=o(1),             \tag{4.3}
\]

and

\[
 \max_v\Xi_H(v)
 =O\!\left({\log^2 n\over n}\right)=o(1).             \tag{4.4}
\]

These are the same asymptotic scales as the free-history central slot
hypergraph.  In particular, the uniform isolated-edge one-bite calculation is
asymptotically ideal here.  On the other hand, (1.4) gives

\[
 {r\nu(H)\over|V(H)|}=O(1/n),                           \tag{4.5}
\]

so a maximum matching leaves a `1-O(1/n)` fraction of all vertices uncovered.
By Corollary 1.2, the actual degree can simultaneously be inflated past the raw
degree of the free-history palette, with (4.2)--(4.5) unchanged.

## 5. What this settles, and what it does not

The construction proves the following negative conclusion.

> There is no growing-rank matching theorem whose only hypotheses are near or
> exact regularity, `r Delta_2/Delta=o(1)`, and `max_v Xi(v)=o(1)`, even for
> balanced `r`-partite hypergraphs with one designated slot part.  Consequently
> the central one-bite lemma cannot be iterated solely from those numerical
> parameters.

The obstruction is global.  The `r` vertex parts encode `r` simultaneous
equipartitions, and a matching is a common partial transversal.  Pairwise block
intersections are tiny, but the simultaneous transversal number is tiny too.
This information is invisible to every one-vertex and two-vertex statistic in
(1.3).

The result does **not** show that the actual free-history palette lacks a
near-factor.  Its targets live in one Johnson layer and its codegrees have an
exact distance profile, whereas the target side above retains a latent
`(r-1)`-part partition.  A positive central theorem must exploit some additional
global feature specific to that palette.  Examples of a logically sufficient
kind of new input would be a residual-set expansion theorem, an anti-partition
or common-transversal theorem, or direct multi-round degree tracking that uses
more than the maximum and squared pair-codegree summaries.  Establishing such
an input remains open.
