# Mixed coordinate pairings: fractional balancing and the true rounding barrier

This note strengthens Proposition 9 of `CUBE_SHADOW_TILING.md`.  Mixing a
polynomial number of coordinate perfect matchings is enough to remove the
fixed-pair type bias not merely target by target, but simultaneously at the
level of the full typed fractional matching.  The proof uses an exact
size-bias identity.

What remains is genuinely integral.  The resulting typed hypergraph has an
almost perfect fractional matching and weighted pair-codegree
`Theta(1/m)`, but its edges have growing size at least `omega(m)`.  Those two
statistics alone cannot imply an almost-perfect matching: projective planes
give counterexamples in precisely this range.  Thus the next theorem must use
the necklace/chain geometry of the blocks, not another black-box invocation
of Pippenger's theorem.

Throughout, put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 \rho_q=N_q/W.
\tag{0.1}
\]

Let `ell=o(m)` be the half-length of a partial pair-flip block, and let
`h<ell` be the largest certified shadow depth.  After the width-order tail
construction in `TRUNCATED_TAIL_CONSTRUCTION.md`, the application may take

\[
 h=\sqrt m\,c_m,\quad c_m\longrightarrow\infty,\qquad
 \ell/h\longrightarrow\infty,\quad \ell=o(m),\quad
 c_m=o(\sqrt{\log m}).
\tag{0.2}
\]

Use the certification probabilities

\[
 p_0=1-\rho_1,\quad
 p_d=\rho_d-\rho_{d+1}\ (1\le d<h),\quad
 p_h=\rho_h.
\tag{0.3}
\]

Then `sum_(d>=q) p_d=rho_q`.

## 1. The block family inside one coordinate matching

Fix a perfect matching `P` of the `2m` ground coordinates.  A middle mask
has `f` full pairs, `f` empty pairs and

\[
                         s=m-2f
\tag{1.1}
\]

split pairs.  All partial blocks compatible with `P` stay in one such
orientation-cube stratum.

### Lemma 1 (middle degree in a stratum)

The number of geometric partial `2ell`-cycles through a prescribed middle
vertex in an `s`-dimensional orientation stratum is

\[
                         g_s=\frac{(s)_{\ell}}2.
\tag{1.2}
\]

#### Proof

Choose the `ell` active split pairs and then a geometric standard cycle on
their orientation cube through the prescribed vertex.  There are
`binom(s,ell)` active sets.  On `Q_ell`, a fixed vertex belongs to
`ell!/2` geometric standard cycles (an ordering of the directions, modulo
reversal).  Their product is (1.2).  QED.

Now fix a lower target `S` of rank `m-q`.  Relative to `P`, suppose it has

\[
 f\text{ full pairs},\qquad f+q\text{ empty pairs},\qquad
 r=m-2f-q\text{ split pairs}.
\tag{1.3}
\]

Its source orientation stratum has `s=r+q=m-2f` split pairs.

### Lemma 2 (exact normalized shadow degree)

The number of compatible partial blocks whose depth-`q` lower row contains
`S` is

\[
 h_{f,q}=2^{q-1}(f+q)_{q}(s-q)_{\ell-q}.
\tag{1.4}
\]

Consequently,

\[
 \boxed{\frac{h_{f,q}}{g_s}
   =\lambda_{f,q}:=
     \frac{2^q(f+q)_q}{s_q}
   =\frac{2^q\binom{f+q}{q}}{\binom{s}{q}}.}
\tag{1.5}
\]

The same formula holds for an upper target of rank `m+q`.

#### Proof

Choose the `q` empty pairs which become the free directions of the target
face, and choose the other `ell-q` active pairs among its split pairs.  A
fixed `q`-face of `Q_ell` lies in

\[
                       2^{q-1}q!(\ell-q)!
\]

geometric standard cycles: double-count the `2ell` depth-`q` windows over
all `2^(ell-2)(ell-1)!` geometric cycles.  Multiplying these three factors
gives (1.4).  Division by (1.2) gives (1.5).  The upper statement is the
complement-dual calculation.  QED.

Thus the correct weight for every compatible block in an `s`-stratum is
`1/g_s`.  With this normalization, one coordinate matching gives weighted
middle degree exactly one in every stratum and weighted target degree
exactly `lambda_(f,q)`.

## 2. The exact size-bias identity

Let `P` now be a uniformly random perfect matching.  For a fixed rank
`m-q` target, the probability that its type is `f` is

\[
 \pi_{q}(f)=\frac{T_{f,q}}{N_q},
\qquad
 T_{f,q}=
 \frac{m!}{f!(f+q)!(m-2f-q)!}2^{m-2f-q}.
\tag{2.1}
\]

For a fixed middle mask, the corresponding type law is

\[
 \pi_0(f)=\frac{V_f}{W},
\qquad
 V_f=\frac{m!}{f!f!(m-2f)!}2^{m-2f}.
\tag{2.2}
\]

Equation (1.5) is equivalently `lambda_(f,q)=V_f/T_(f,q)`.  Hence:

### Theorem 3 (size-bias cancellation)

For every `f` and every `q<ell`,

\[
 \boxed{\pi_q(f)\lambda_{f,q}
       =\rho_q^{-1}\pi_0(f).}
\tag{2.3}
\]

In particular,

\[
              \mathbb E_{\mathcal P}\lambda_{F,q}=\rho_q^{-1}.
\tag{2.4}
\]

More strongly, for every set `B` of pair types,

\[
 \mathbb E_{\mathcal P}
   [\lambda_{F,q}{\bf1}_{F\in B}]
 =\rho_q^{-1}\Pr_{\pi_0}(F\in B).
\tag{2.5}
\]

This identity is the reason a mixed reservoir can be truncated without
destroying rank balance.  Under the target law, the rare pair types carrying
large `lambda` are exactly the ordinary middle types after size biasing.

## 3. Polynomial truncation

Let `mu_0=E_(pi_0)F=m(m-1)/(2(2m-1))`.  Exposing a random perfect matching
through a random paired permutation gives the subgaussian estimate

\[
 \Pr_{\pi_0}(|F-\mu_0|>u)
       \le 2\exp(-c u^2/m)
\tag{3.1}
\]

for an absolute `c>0`.  (A transposition changes `F` by at most two, so the
standard bounded-differences inequality for random permutations applies.)

Fix constants `A,C>0` and put

\[
 \mathcal B=\{f:|f-\mu_0|\le A\sqrt{m\log m}\},
 \qquad \tau=\Pr_{\pi_0}(F\notin\mathcal B).
\tag{3.2}
\]

Then `tau<=2m^(-cA^2)`.  If `q<=C sqrt(m log m)` and `f in B`, a direct
expansion of (1.5) gives

\[
 \log\lambda_{f,q}
 =O\!\left(\frac{q(|f-m/4|+q+1)}m\right)
 =O_{A,C}(\log m).
\tag{3.3}
\]

Thus

\[
                       \lambda_{f,q}\le m^{K(A,C)}
\tag{3.4}
\]

uniformly in the full required central band.  For `ell=o(m)`, every balanced
stratum has `s>=ell` for all sufficiently large `m`.

## 4. A polynomial reservoir theorem

For a perfect matching `P`, retain all compatible partial blocks lying in a
balanced stratum.  For every retained block `B` in an `s`-stratum and every
certification label `d`, give its typed edge the provisional weight

\[
                    \frac{p_d}{g_s}.
\tag{4.1}
\]

Sample independent uniform perfect matchings

\[
                   \mathcal P_1,\ldots,\mathcal P_J.
\tag{4.2}
\]

Scale every weight in (4.1) by `1/[J(1-tau)]`.

### Theorem 4 (polynomial mixed-pair fractional reservoir)

For every fixed `A,C` and every fixed `a>0`, and uniformly for every
`h<=C sqrt(m log m)`, there is

\[
                         J=m^{O_{A,C,a}(1)}
\tag{4.3}
\]

and a deterministic choice of the matchings (4.2) such that simultaneously:

1. every middle and every lower/upper target through the certified depth
   `h` has weighted degree `1+O(m^(-a))`;
2. the weighted codegree of every two distinct target vertices is at most
   `2/(m-h)+O(m^(-a))` when only depths through `h` are certified.

Thus a polynomial family of coordinate matchings supports an approximate
version of the exact typed fractional matching from
`PARTIAL_BLOCK_MULTISCALE.md`.

#### Proof: degrees

For a fixed middle mask, one matching contributes either zero or one before
the factor `1/[J(1-tau)]`; its expectation is `1-tau`.

For a fixed depth-`q` target, summing the labels `d>=q` contributes the factor
`rho_q`.  Its contribution from one matching is therefore

\[
             \rho_q\lambda_{F,q}{\bf1}_{F\in\mathcal B},
\tag{4.4}
\]

whose expectation is `1-tau` by (2.5).  It is bounded by a fixed polynomial
in `m` by (3.4).

Bernstein's inequality now gives failure probability

\[
       \exp[-m^{\Omega(1)}]
\]

for any prescribed target after taking the exponent in (4.3) sufficiently
large.  Increase it once more so that the failure probability is at most
`exp(-m^2)`.  There are fewer than `4^m` target vertices, so a union bound
proves item 1.

#### Proof: codegrees

Average the balanced, normalized block measure over all coordinate
matchings.  It is invariant under `S_(2m)`, because the condition
`f in B` is preserved by simultaneous relabelling.  Every middle vertex has
expected weighted degree `1-tau`.  Transitivity on geometric partial blocks
therefore forces the averaged weight of every block to be exactly
`(1-tau)/D`, where `D` is its middle degree in the unrestricted geometric
block family.  After division by `1-tau`, the average is exactly the uniform
geometric-block measure, with type weight `p_d/D`.

For two masks of ranks `m+a` and `m+b`, condition on a block containing the
first.  If the masks are nested and `b-a=t>0`, precisely `t+1` cyclic
intervals of length `ell+b` contain the fixed interval of length `ell+a`.
Therefore the conditional co-occurrence ratio is

\[
                        \frac{t+1}{\binom{m-a}{t}}.
\tag{4.5}
\]

The reverse-nested formula is

\[
                        \frac{t+1}{\binom{m+a}{t}}.
\tag{4.6}
\]

For equal ranks and Johnson distance `t`, the ratio is

\[
               \frac{2}{\binom{m+a}{t}\binom{m-a}{t}}
\tag{4.7}
\]

away from the irrelevant antipodal endpoint.

For a rigorous bound in every remaining case, fix the first mask `A` of rank
`m+a` and write

\[
 v=|A\setminus B|,\qquad u=|B\setminus A|.
\]

After the `S_(2m)`-average, the stabilizer of `A` is transitive on the

\[
 \binom{m+a}{v}\binom{m-a}{u}
\]

masks `B` with these two differences.  A geometric block containing `A`
has at most `2ell` vertices at the rank of `B`.  If the pair is nonnested,
then `u,v>=1`.  Co-occurrence in one partial block also forces
`u,v<=ell+2h=o(m)`; otherwise the ratio is zero.  Thus neither binomial
coefficient below is at an endpoint, and the conditional ratio is at most

\[
 \frac{2\ell}
      {\binom{m+a}{v}\binom{m-a}{u}}
 \le \frac{2\ell}{(m-h)^2}
 \le \frac2{m-h}                                      \tag{4.8}
\]

for all sufficiently large `m`, because `ell=o(m)`.  In the nested formulas
(4.5)--(4.6), `(t+1)/binom(n,t)` is maximized at `t=1` throughout the present
band, with `n>=m-h` and every co-occurring `t<=ell+2h=o(m)`.  The equal-rank
formula (4.7) is smaller still.  Hence every conditional ratio is bounded by
the adjacent-nesting envelope

\[
                         \frac2{m-h}.
\tag{4.9}
\]

If the two vertices first occur at depths `q_1,q_2`, the certification tail
for their pair is `rho_(max(q_1,q_2))`; after conditioning on either vertex
it is multiplied by a ratio at most one.  Thus (4.9) is also the maximum
weighted pair-codegree.

Thus the expected scaled pair contribution is already at most
`2/(m-h)`.  Each one-matching contribution is bounded by the same
polynomial as in (3.4).  A second Bernstein/union-bound argument, now over
fewer than `16^m` vertex pairs, proves item 2.  QED.

Theorem 4 strictly strengthens Proposition 9 of `CUBE_SHADOW_TILING.md`.
That proposition supplied one favourable matching for each target.  Theorem
4 supplies a single polynomial reservoir carrying the complete rank-balanced
fractional solution and its small weighted codegrees.

## 5. Why this still does not round by a standard nibble

The support in Theorem 4 may be sparsified further to a nearly regular
finite hypergraph of any prescribed polynomial degree `Delta`, with

\[
 \Delta_2=O(\Delta/m),
 \qquad
 |e(B,d)|=2\ell(1+2d).
\tag{5.1}
\]

The average typed edge size is

\[
 \bar r
 =2\ell\left(1+2\sum_{q\le h}\rho_q\right)
 =(2\sqrt\pi+o(1))\ell\sqrt m.
\tag{5.2}
\]

With `ell/h->infinity` and `h=sqrt(m) omega(1)`, one has

\[
                         \bar r=m\,\omega(1).
\tag{5.3}
\]

Classical Pippenger--Spencer and modern pseudorandom/conflict-free matching
theorems take the edge bound as fixed.  Their quantitative dependence also
does not survive (5.3).  For example, in the Ehard--Glock--Joos theorem the
error exponent is `epsilon=beta/(50r^2)`.  Writing

\[
       \Delta/m=\Delta^{1-\beta}
       \quad\Longrightarrow\quad
       \beta=\frac{\log m}{\log\Delta},
\]

gives

\[
       \Delta^{-\epsilon}
       =m^{-1/(50r^2)}=1-o(1),
\tag{5.4}
\]

regardless of how large `Delta` is.  It cannot even prove a vanishing
relative defect, let alone the required `o(W)` absolute defect among
`Theta(W sqrt(m))` typed vertices.

This is not merely a weakness in one proof.  Weighted degree one and
pair-codegree `O(1/m)` do not imply a large matching when the edge size
exceeds `m`.  A projective plane of order `r-1` is `r`-uniform and
`r`-regular, has relative pair-codegree `1/r`, and has matching number one
because every two lines meet.  Taking `r>=m` satisfies the same numerical
pair-codegree bound as (5.1) while being maximally far from matchable.

Therefore any valid rounding theorem for the present hypergraph must use
structure absent from a projective plane.  Here that structure is:

* every typed edge is a disjoint union of `2ell` nested symmetric-chain
  segments;
* its middle members form an induced pair-flip cycle;
* its rows are cyclic-interval shadows of one common active order; and
* the reservoir is a mixture of resolvable orientation-cube geometries.

## 6. Exact successor theorem

The mixed-coordinate-pairing route has now been reduced to the following
purely integral statement.

> **Necklace-bundle rounding theorem.**  In the polynomial reservoir of
> Theorem 4, select pairwise disjoint typed block edges so that the total
> number of uncovered typed vertices is `o(W)`, not merely
> `o(W sqrt(m))`.  The selection must retain Poisson-scale statistics of the
> uncertified physical windows at depths above `h`.

No density, local type, divisibility, fractional-Hall, or pair-codegree
obstruction remains.  Conversely, Theorem 4 by itself is not an integral
construction: a proof of the necklace-bundle rounding theorem (or an
equivalent wreath-resolved SCD theorem) is still necessary.

The most promising way to lower the effective uniformity is to first build a
symmetric-chain decomposition, regard each whole chain segment as one atomic
vertex, and then match `2ell` such atoms into compatible necklaces.  That
would leave an `R=2ell`-uniform bundling problem instead of an
`Theta(ell sqrt(m))`-uniform mask problem.  It is exactly the
wreath-resolved-SCD reformulation in `PARTIAL_BLOCK_MULTISCALE.md`.
