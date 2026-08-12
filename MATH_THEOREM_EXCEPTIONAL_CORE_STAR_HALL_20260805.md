# Exceptional-core Hall for the slack owner levels

**Date:** 2026-08-05  
**Method:** degree cleanup, one incidence double count, and Chernoff tails;
no computation or search  
**Status:** unconditional deterministic Hall lemma plus a quantitative
probabilistic corollary.  At every owner level `j>=2`, it is unnecessary to
verify all Hall cuts.  It suffices to control two one-dimensional tails:
low left-list degrees and incidence mass on abnormally high right degrees.
If both tails are \(\exp(-\Omega(d))\), all slack levels together discard
`o(H/d)` copies.  Establishing those two tails for the recursively produced
skeleton process remains the live probabilistic input.

## 1. A general exceptional-core lemma

Let `G=(L,R;E)` be a finite bipartite graph.  Fix numbers `a>0` and
`0<eta<1/10`.  Define

\[
 L_{\rm low}=\{v\in L:d(v)<(1-\eta)a\},                    \tag{1.1}
\]

and

\[
 R_{\rm high}=\{w\in R:d(w)>(1-2\eta)a\}.                  \tag{1.2}
\]

Put

\[
 b=|L_{\rm low}|,
 \qquad
 B=e(L,R_{\rm high})=
      \sum_{w\in R_{\rm high}}d(w).                         \tag{1.3}
\]

### Theorem 1.1 (exceptional-core Hall)

The graph `G` has a matching which leaves unmatched at most

\[
 \boxed{
                         b+{B\over\eta a}}                   \tag{1.4}
\]

vertices of `L`.

#### Proof

Delete `L_low` and `R_high`.  For a remaining left vertex `v`, let `ell(v)`
be the number of its incident edges deleted with `R_high`.  Since

\[
                         \sum_{v\in L-L_{\rm low}}\ell(v)\le B,             \tag{1.5}
\]

fewer than `B/(eta a)` remaining left vertices have
`ell(v)>eta a`.  Delete those vertices as well.

In the residual graph every left degree is at least

\[
                         (1-\eta)a-\eta a=(1-2\eta)a,        \tag{1.6}
\]

whereas every right degree is at most `(1-2eta)a`.  For any residual
left set `X`, double counting its incident edges gives

\[
 (1-2\eta)a|X|
     \le e(X,N(X))
     \le (1-2\eta)a|N(X)|.                                  \tag{1.7}
\]

Thus `|N(X)|>=|X|` for every `X`, and Hall's theorem saturates the residual
left shore.  Only the vertices deleted in the two cleanup steps remain
unmatched, proving (1.4).  \(\square\)

The lemma is deliberately insensitive to the number of Hall cuts and to the
maximum degree before cleanup.

## 2. Application to one backward owner level

At owner level `j`, each copy `i` has a rank-`r-1` skeleton

\[
                         K_i=T_{j+1}^i-\{b_{j+1}^i\}.         \tag{2.1}
\]

Its raw menu is the upper star

\[
                         \mathcal U(K_i)
             =\{K_i\cup\{x\}:x\notin K_i\},                 \tag{2.2}
\]

punctured by the already used owner bank and by at most `d-j` forbidden
coordinates belonging to its future queue and terminal flag.

Distinct skeleton stars have the exact intersection law

\[
 |\mathcal U(K)\cap\mathcal U(K')|
   =\begin{cases}
      1,&|K\cap K'|=r-2,\\
      0,&|K\cap K'|<r-2.
    \end{cases}                                             \tag{2.3}
\]

Identical skeletons are the only source of a large common list.

Let `G_j` be the actual level graph after deleting all owners already used
at levels above `j`.  Its nominal product-residual left-degree scale is

\[
                         a_j={j+1\over d+1}(q-d)              \tag{2.4}
\]

and hence \(a_j=\Theta((j+1)d)\).  Applying
Theorem 1.1 with `a=a_j` gives the following exact criterion.

### Corollary 2.1 (two-tail level certificate)

If

\[
 \begin{aligned}
 b_j&=|\{i:d_{G_j}(i)<(1-\eta)a_j\}|,\\
 B_j&=\sum_{T:\ d_{G_j}(T)>(1-2\eta)a_j}d_{G_j}(T),
                                                               \tag{2.5}
 \end{aligned}
\]

then level `j` can be installed after discarding at most

\[
                         b_j+{B_j\over\eta a_j}              \tag{2.6}
\]

copies.

No separate family of Hall inequalities remains.

## 3. Identical-skeleton classes are explicitly visible

Let `m_K` copies have one common skeleton `K`.  Suppose every copy deletes
at most `f` points from the raw star \(\mathcal U(K)\) before the common used
owner bank is removed.  Across all copies, the number of missing
copy--owner incidences is at most `m_K f`.

### Lemma 3.1 (large class forces a high-degree tail)

At least `q-2f` owners of \(\mathcal U(K)\) are adjacent to at least `m_K/2`
members of the class, where `q=k-r+1`.

#### Proof

If more than `2f` star owners each missed more than `m_K/2` class
incidences, the number of missing incidences would exceed
`2f(m_K/2)=m_Kf`.  \(\square\)

Consequently, before common-bank deletions, a class with

\[
                         m_K>2(1-2\eta)a_j.                 \tag{3.1}


places at least

\[
                         (q-2f)m_K/2                         \tag{3.2}

incidences into the high-right-degree tail.  Thus (2.5) automatically
detects an excessive identical-skeleton class.  A separate multiplicity cap
is useful operationally, but it is not a hidden third Hall condition.

## 4. Quantitative all-level cleanup

Let `H` be the number of surviving copy tasks at the beginning of the
backward construction.  Suppose that, for every `2<=j<=d-2`, the level
process satisfies

\[
 \begin{aligned}
 b_j&\le H\exp(-c(j+1)d),\\
 B_j&\le H a_j\exp(-c(j+1)d)                                \tag{4.1}
 \end{aligned}
\]

for one absolute `c>0` and the fixed `eta` above.

### Theorem 4.1 (all slack levels cost `o(H/d)`)

All levels `d-2,d-3,...,2` can then be installed after discarding a total of

\[
 \begin{aligned}
 \sum_{j=2}^{d-2}
   \left(b_j+{B_j\over\eta a_j}\right)
 &\le C_\eta H\sum_{j=2}^{\infty}e^{-c(j+1)d}\\
 &=O(H e^{-3cd})
  =o(H/d).                                                  \tag{4.2}
 \end{aligned}
\]

#### Proof

Apply Corollary 2.1 at every level and sum (2.6).  The displayed geometric
series proves (4.2).  \(\square\)

Since one discarded copy loses `d` duplicate lower positions, (4.2) costs
`o(H)=o(W/d)`, strictly below the available separator scale.

## 5. Where the exponential tails come from

This section records a sufficient probabilistic input; it is not asserted
for the physical recursive process without proof.

Assume at one level that the available owner bank is a uniform or Bernoulli
sample of density

\[
                         p_j={j+1\over d+1}+O(1/d^2),         \tag{5.1}
\]

independent of each fixed raw star.  A left list of size `q-O(d)` then has
mean

\[
                         (q-O(d))p_j=\Theta((j+1)d).          \tag{5.2}
\]

The hypergeometric Chernoff bound gives

\[
 Pr\bigl(d_{G_j}(i)<(1-\eta)E d_{G_j}(i)\bigr)
                         \le e^{-c_\eta(j+1)d}.              \tag{5.3}
\]

Therefore the **expected number**, not the probability of no exception, has
the correct size:

\[
                         E b_j\le H e^{-c_\eta(j+1)d}.       \tag{5.4}
\]

No union bound over the exponentially many jobs is needed; the exceptional
jobs are simply discarded.

For the right tail, let `s_T` be the number of current skeleton copies whose
raw stars contain owner `T`.  If the recursively generated skeleton process
has the size-biased tail

\[
 \sum_{T:s_T>(1-3\eta)a_j}s_T
                         \le H a_j e^{-c(j+1)d},             \tag{5.5}
\]

and the bank sampling does not increase degrees, then (4.1) follows after a
constant adjustment of `eta`.  Equation (5.5) is the exact remaining
right-tail tracking row.  It includes identical-skeleton classes through
Lemma 3.1.

Thus the probabilistic proof target for all slack levels is only:

* product-like thinning of each individual upper star, and
* an exponential size-biased tail for the number of skeleton stars through
  one owner.

These are scalar degree-distribution statements.  They are strictly weaker
than hereditary near-regularity of the complete growing-rank macro
hypergraph.

### Lemma 5.1 (cylinder spread implies the right tail)

For every current copy, retain the occurrence-labelled pair `(U,b)`, where
`U=T_(j+1)` is its current owner and `b=b_(j+1)` is the coordinate deleted
when its skeleton is formed.  Owners `U` are pairwise distinct.  Suppose
their joint law satisfies the cylinder estimate

\[
 \Pr\bigl((U_1,b_1),\ldots,(U_m,b_m)
             \hbox{ are all selected}\bigr)
 \le\left({1+\varepsilon\over dr}\right)^m               \tag{5.6}
\]

for every compatible collection with distinct owners, where
`epsilon=o(1)`.

Then, for every fixed rank-`r` owner `T`, its raw skeleton-star degree `s_T`
satisfies

\[
 E(s_T)_m\le\mu^m,
 \qquad
 \mu=(1+\varepsilon){q\over d}=\Theta(d).                  \tag{5.7}
\]

Consequently, with

\[
                         \psi(x)=x\log x-x+1,                \tag{5.8}
\]

for every integer `L>mu+1`,

\[
 \Pr(s_T\ge L)\le
       \exp\!\left[-\mu\psi\!\left({L\over\mu}\right)\right]
                                                               \tag{5.9}
\]

and

\[
 E\bigl[s_T\mathbf1_{\{s_T\ge L\}}\bigr]
 \le \mu\exp\!\left[-\mu\psi\!\left({L-1\over\mu}\right)\right].
                                                               \tag{5.10}
\]

#### Proof

The skeleton of `(U,b)` lies in the upper star of `T` precisely when

\[
                         U-\{b\}\subset T.                  \tag{5.11}
\]

There are exactly `rq` occurrence-labelled pairs satisfying (5.10): choose
one of the `r` facets of `T`, then choose the added coordinate in the
`q`-element complement of that facet.  A factorial-moment expansion of
`s_T` sums (5.6) over compatible ordered collections of such pairs.  Terms
repeating one owner are zero, so

\[
 E(s_T)_m\le(rq)^m
      \left({1+\varepsilon\over dr}\right)^m=\mu^m.         \tag{5.12}
\]

The factorial-moment bound implies, coefficientwise for `z>=0`,

\[
 E(1+z)^{s_T}
   =\sum_{m\ge0}{E(s_T)_m\over m!}z^m
   \le e^{\mu z}.                                           \tag{5.13}
\]

Chernoff's argument with `1+z=e^theta`, optimized at
`e^theta=L/mu`, proves (5.9).  Differentiating the coefficientwise series
in (5.13) gives

\[
 E\bigl[s_Te^{\theta(s_T-1)}\bigr]
       \le\mu e^{\mu(e^\theta-1)}.                          \tag{5.14}
\]

On `s_T>=L`, multiply by `e^{-theta(L-1)}` and optimize at
`e^theta=(L-1)/mu`; this proves (5.10).  \(\square\)

Take `L=(1-3eta)a_j`.  Since

\[
                         {a_j\over\mu}=j+1+o(1),             \tag{5.15}
\]

the right side of (5.10) is `d exp(-Omega((j+1)d))` uniformly
for `j>=2`.  Summing over the `W` possible owners and absorbing the
polynomial factor `d` into the exponential yields (5.5), and hence (4.1),
in expectation.  As with the left exceptions, one chooses an outcome no
worse than a constant multiple of its expectation; no all-owner union bound
is needed.

The cylinder hypothesis is exact for the ideal uniform model.  If `H`
distinct owners are sampled uniformly and each receives a uniform marked
coordinate, then for distinct prescribed owners

\[
 { (H)_m\over(W)_m}\,r^{-m}
       \le\left({1+o(1)\over dr}\right)^m,                  \tag{5.16}
\]

because `H/W=(1+o(1))/d`.  The remaining recursive task is therefore to
choose the level matchings from a distribution which preserves (5.6), or a
weaker factorial-moment bound sufficient for (5.7).

## 6. Remaining bottom band

Theorem 4.1 applies only to `j>=2`.  Levels `0,1` are retained as one fixed
3-uniform bottom-band matching, as established in

`MATH_THEOREM_BOTTOM_OWNER_BAND_FIXED_RANK_REDUCTION_20260805.md`.

The proof programme is therefore:

1. establish (5.5) inductively while choosing the slack-level matchings;
2. discard the exponentially small exceptional cores using Theorem 4.1;
3. solve the fixed 3-uniform bottom band; and
4. apply the terminal `Sym(h)` switches for topology.
