# Exact layer-saturated obstruction to local-parameter retired-chain rounding

**Status (2026-08-21).**  Every assertion below is proved.  The construction
has the exact Boolean upper-layer cardinalities, a fractional retired-chain
matching which saturates every target, maximum vertex load one, and maximum
fractional pair load at most `2/b`.  Nevertheless every integral matching
loses `Omega(sqrt(b) W_b)` target occurrences.  Thus the one-vertex and
two-vertex estimates of the affine retirement lift cannot, by themselves,
imply the required `o(W_b)` integral rounding theorem.

This is a parameter-only obstruction, not a counterexample to the affine
Boolean-chain hypergraph.  Its paths are chains in a common abstract graded
order, but the order is not the Boolean containment order and the construction
does not have the affine orbit identities.  Any positive affine rounding
theorem must use such additional global structure.

## 1. Statement

Let

\[
 W_b={2b\choose b},\qquad M_q={2b\choose b+q},
 \qquad H=\Theta(\sqrt{b\log b}).                    \tag{1.1}
\]

A retired-chain hypergraph has parts

\[
 \mathcal O\,\dot\cup\,\mathcal U\,\dot\cup\,
 \mathcal T_1\,\dot\cup\cdots\dot\cup\,\mathcal T_H, \tag{1.2}
\]

and an edge of retirement time `ell` contains one token, one source, and one
target from each of `T_1,...,T_ell`.  Its target value is `ell`.  For a
fractional matching `theta`, its fractional target value is

\[
 \operatorname{val}(\theta)=\sum_e |e\cap\mathcal T|\theta(e). \tag{1.3}
\]

For an integral matching `\mathcal M`, use the same notation with unit edge
weights:

\[
 \operatorname{val}(\mathcal M)
 =\sum_{e\in\mathcal M}|e\cap\mathcal T|.            \tag{1.3a}
\]

### Theorem 1.1 (local loads do not round growing retired chains)

For all sufficiently large `b` there is a finite retired-chain hypergraph
`H_b` with

\[
 |\mathcal O|=|\mathcal U|=W_b,
 \qquad |\mathcal T_q|=M_q\quad(1\le q\le H),        \tag{1.4}
\]

and a fractional matching `theta_b` such that

1. every target has load exactly one, every nonisolated token and source has
   load exactly one, and all remaining tokens and sources have load zero;
2. every pair of distinct vertices has fractional pair load at most `2/b`;
3. the fractional target deficit is exactly zero:

   \[
    \operatorname{val}(\theta_b)=\sum_{q=1}^H M_q;  \tag{1.5}
   \]

4. every integral matching `\mathcal M` satisfies

   \[
    \sum_{q=1}^H M_q-\operatorname{val}(\mathcal M)
       =\Omega(\sqrt b\,W_b).                        \tag{1.6}
   \]

The hypergraph may be made simple by coalescing parallel edges and adding
their fractional weights.  Also, if every vertex in `O` is declared below
every vertex in `U`, every vertex in `U` below every vertex in `T_1`, and
every vertex in `T_q` below every vertex in `T_(q+1)`, then every hyperedge
is a chain in this single graded poset.

In particular there is no theorem deducing an `o(W_b)` integral target loss
only from the part sizes (1.4), vertex loads at most one, pair loads `O(1/b)`,
and the nested partite format.

## 2. The bad balanced gadget

We use the following specialization of the common-partial-transversal
construction.

### Lemma 2.1 (balanced equipartition gadget)

Let `D>=4`, let `r>=64 log(2eDr)`, and let `L` be sufficiently large in
terms of `D,r`.  There is an `r`-partite, `r`-uniform multihypergraph `G`
with `L` vertices in every part such that

\[
 d_G(v)=D,\qquad \Delta_2(G)\le2,                  \tag{2.1}
\]

and

\[
 \nu(G)\le {32\log(2eDr)\over r}\,L.              \tag{2.2}
\]

For the values of `L` used in Theorem 1.1, the phrase "sufficiently large"
holds uniformly.

#### Proof

Put `X=[LD]`.  Independently choose `r` uniform equipartitions `P_i` of `X`
into `L` blocks of size `D`.  A vertex is a pair `(i,B)` with `B in P_i`,
and every `x in X` gives the edge consisting of the `r` blocks which contain
`x`.  Hence (2.1) holds except possibly for the codegree assertion.

For blocks in two distinct partitions,

\[
 \Pr(|B\cap C|\ge3)
 \le {{D\choose3}^2\over {LD\choose3}}.             \tag{2.3}
\]

A union bound over at most `binom(r,2)L^2` block pairs shows that the expected
number of codegree violations is

\[
 O\!\left({r^2D^3\over L}\right).                  \tag{2.4}
\]

This tends to zero for the stated regime.

A matching is exactly a common partial transversal: a set `S subset X`
meeting every block of every partition at most once.  Put

\[
 Q=\log(2eDr),\qquad c={16Q\over r},\qquad
 s=\lceil cL\rceil.                                  \tag{2.5}
\]

The rank assumption gives `c<=1/4`.  For a fixed `s`-set, its probability of
meeting every block of one equipartition at most once is

\[
 p_s={(L)_sD^s\over(LD)_s},                          \tag{2.6}
\]

and, for sufficiently large `L`,

\[
 \log p_s\le-{s(s-1)\over4L}.                       \tag{2.7}
\]

The expected number of common partial transversals of size `s` is therefore
at most

\[
 {LD\choose s}\exp\!\left(-{rs(s-1)\over4L}\right)
 \le e^{-Qs}=o(1).                                  \tag{2.8}
\]

Indeed, `s-1>=cL/2`, `log(eLD/s)<Q`, and `rc/8=2Q`.
With positive probability (2.4) has no violation and (2.8) has no such
transversal.  Then `nu(G)<s`, and `s/L<=2c` for large `L`, proving (2.2).
\(\square\)

Give every edge of `G` weight `1/D`.  Every vertex then has load one, every
pair has load at most `2/D`, and the total fractional edge mass is `L`.
Parallel edges can be coalesced by summing their weights.  Their multiplicity
is at most `Delta_2(G)<=2` (look at any two of their vertices), so the pair
bound is preserved; all vertex loads and the matching number are unchanged.

## 3. Cohort decomposition with the exact layer sizes

Set `M_(H+1)=0` and define the retirement cohorts

\[
 d_\ell=M_\ell-M_{\ell+1}\qquad(1\le\ell\le H).     \tag{3.1}
\]

They are positive integers and telescope as

\[
 \sum_{\ell=q}^H d_\ell=M_q,
 \qquad \sum_{\ell=1}^H d_\ell=M_1.                \tag{3.2}
\]

Put

\[
 Q_b=\log(2eb(H+2)),\qquad R=\lceil128Q_b\rceil.    \tag{3.3}
\]

For every `ell>=R`, apply Lemma 2.1 with

\[
 D=b,\qquad r=\ell+2,\qquad L=d_\ell.               \tag{3.4}
\]

The parts are named one token cohort, one source cohort, and target cohorts
at ranks `1,...,ell`.  Since `ell+2>=128Q_b`, the hypothesis of the lemma
holds and its matching bound strengthens to

\[
 \nu(G_\ell)\le {1\over4}d_\ell.                   \tag{3.5}
\]

Moreover all `d_ell` are exponentially large.  For `ell<H`, explicitly,

\[
 d_\ell=M_\ell{2\ell+1\over b+\ell+1},             \tag{3.6}
\]

while `d_H=M_H`; and `M_H=W_b b^{-O(1)}` because
`H^2/b=Theta(log b)`.  Thus the uniform
largeness required in Lemma 2.1 follows, including the estimate
`(ell+2)^2b^3/d_ell=o(1)` from (2.4).
In particular `d_ell>=b` for every `1<=ell<=H` once `b` is sufficiently
large.

For `ell<R`, use instead the complete `(ell+2)`-partite hypergraph with
`d_ell` vertices per part and give every edge weight

\[
 d_\ell^{-(\ell+1)}.                                \tag{3.7}
\]

It has total fractional mass `d_ell`, vertex loads one, pair loads
`1/d_ell<=1/b`, and an integral perfect matching.  These short cohorts are
included only to realize the exact layer ledger; they create no obstruction.

Take the disjoint union over all cohorts.  By (3.2), target part `T_q` has
exactly `M_q` vertices, all of load one.  There are `M_1` active token and
source vertices; add `W_b-M_1` isolated vertices to each of those two parts.
This proves (1.4), assertions 1 and 2, and

\[
 \operatorname{val}(\theta_b)
 =\sum_{\ell=1}^H\ell d_\ell
 =\sum_{q=1}^HM_q,                                  \tag{3.8}
\]

which proves assertion 3.

## 4. The integral loss

Because different cohorts have disjoint vertices, every integral matching
has target value at most

\[
 \sum_{\ell<R}\ell d_\ell
 +\sum_{\ell\ge R}\ell\nu(G_\ell).                 \tag{4.1}
\]

By (3.5), its deficit from (3.8) is at least

\[
 {3\over4}\sum_{\ell\ge R}\ell d_\ell.            \tag{4.2}
\]

The full layer mass has the standard central lower bound

\[
 \sum_{q=1}^H M_q=\Omega(\sqrt b\,W_b).             \tag{4.3}
\]

For example, uniformly for `q<=sqrt(b)/4`, the product formula

\[
 {M_q\over W_b}=\prod_{j=0}^{q-1}{b-j\over b+j+1}  \tag{4.4}
\]

is bounded below by an absolute positive constant, and this range lies below
`H` for all large `b`.  On the other hand,

\[
 \sum_{\ell<R}\ell d_\ell
 \le R\sum_{\ell<R}d_\ell
 \le RW_b=O(W_b\log b).                             \tag{4.5}
\]

Subtracting (4.5) from (4.3) gives

\[
 \sum_{\ell\ge R}\ell d_\ell
 =\Omega(\sqrt b\,W_b).                             \tag{4.6}
\]

Equations (4.2) and (4.6) prove (1.6).  \(\square\)

## 5. Exact consequence for the affine program

The fractional affine retirement theorem provides precisely the local
statistics defeated here: vertex loads at most one and pair loads `O(1/b)`
in rank at most `H+2`.  Even exact target saturation and the exact target
layer histogram do not rescue a parameter-only rounding argument.

The obstruction does **not** say that the affine point fails to round.  It
isolates the missing input.  A successful theorem must use a genuinely global
property absent from the equipartition gadgets, such as Boolean-shadow
expansion for every residual family, an affine-orbit anti-partition theorem,
or a direct common-order construction.  Reusing a fixed-rank nibble estimate
with the displayed pair bound cannot prove the coefficient-one result.
