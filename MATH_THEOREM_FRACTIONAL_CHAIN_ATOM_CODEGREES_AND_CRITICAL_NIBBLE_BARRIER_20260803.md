# Fractional owner-chain atoms: exact flag codegrees and the critical nibble barrier

**Date:** 2026-08-03  
**Status:** unconditional weighted-codegree theorem and scope obstruction.  No
computation is used.  This note does **not** disprove structured chain
rounding and does not prove `gamma_d(k)=o(W)`.

## 0. Outcome

Put `k=2r`,

\[
 W={2r\choose r},\qquad
 p_s={{2r\choose s}\over W}\quad(1\le s<r),
\]

and let `d` be the optimal depth from the lower-bound ledger.  Consider the
symmetric fractional owner-chain construction used in Theorem 1.2 of
`MATH_THEOREM_DENSE_FERRERS_UNIT_SCALE_CHAIN_DELETION_BARRIER_20260803.md`.
It first chooses a random rank set

\[
 R\subseteq[r-1],\qquad q_s=\Pr(s\in R),
\]

then, independently for each owner `T in binom([2r],r)`, chooses a uniform
ordering of `T` and takes the initial sets at the ranks in `R`.  Write

\[
 \eta_{s_1,\ldots,s_j}
   =\Pr(\{s_1,\ldots,s_j\}\subseteq R).
\]

This note proves the exact weighted degrees and every flag codegree of this
law.  In particular, on any `o(W)`-defect law,

\[
 \boxed{\rho_2\ge {1-o(1)\over r}},
 \tag{0.1}
\]

where `rho_2` is the maximum pair codegree divided by the smaller incident
degree, over supported positive-degree vertices.  Let `K` be the maximum
cardinality of a supported atom, including its owner vertex.  Then some
supported atom has at least

\[
 K-1\ge {\sqrt\pi\over2}\sqrt r-o(\sqrt r)
 \tag{0.2}
\]

real target vertices.  Consequently

\[
 \boxed{K^2\rho_2\ge {\pi\over4}-o(1).}
 \tag{0.3}
\]

Thus the most direct growing-uniformity nibble is on a genuinely critical
surface, not in a regime where `K^2 rho_2=o(1)`.

The obstruction survives after deleting any top-rank collar of width
`a=o(sqrt(r))` **while retaining the same symmetric uniform-order law on the
residual rank classes**.  To make even the elementary forced adjacent-rank
correlation disappear in that residual law, a necessary collar width is

\[
 a\ge(\sqrt{\log2}-o(1))\sqrt r
   =\left(2\sqrt{{\log2}\over\pi}-o(1)\right)d,
 \tag{0.4}
\]

and the last coefficient is approximately `0.9394`.  A constant or slowly
growing collar is therefore quantitatively irrelevant.  Equation (0.4) is
only a necessary threshold: prechainizing such a macroscopic collar and
extending it compatibly are not proved here.

## 1. The weighted atom hypergraph

The vertex set has two types:

* one owner vertex `o_T` for every `T in binom([2r],r)`;
* one target vertex for every nonempty `S subset [2r]` of rank below `r`.

An atom contains `o_T` and the initial subsets of a permutation of `T` at
the ranks in `R`.  Give the atoms the probability weights described above,
with total atom weight one at every owner.  Let `d_x(A)` denote the total
weight of atoms containing every vertex in `A`.

### Theorem 1.1 (exact degrees)

For `|S|=s<r`,

\[
 d_x(o_T)=1,
 \qquad
 d_x(S)=
 { {2r-s\choose r-s}q_s\over {r\choose s}}
 ={q_s\over p_s}.
 \tag{1.1}
\]

Moreover,

\[
 d_x(o_T,S)=
 \begin{cases}
 q_s/{r\choose s},&S\subset T,\\
 0,&S\not\subset T.
 \end{cases}
 \tag{1.2}
\]

#### Proof

For a fixed owner containing `S`, a uniform ordering has `S` as its initial
`s`-set with probability `1/binom(r,s)`, and rank `s` is retained with
probability `q_s`.  There are `binom(2r-s,r-s)` owners containing `S`.
The standard identity

\[
 {{2r-s\choose r-s}\over {r\choose s}}
 ={W\over {2r\choose s}}={1\over p_s}
\]

gives (1.1); the same one-owner calculation gives (1.2).  `square`

### Theorem 1.2 (all target-flag codegrees)

Let `S_1,...,S_j` have distinct ranks

\[
 1\le s_1<\cdots<s_j<r.
\]

Their codegree is zero unless they form a flag

\[
 S_1\subset S_2\subset\cdots\subset S_j.
\]

For a flag,

\[
 \boxed{
 d_x(S_1,\ldots,S_j)=
 { {2r-s_j\choose r-s_j}\eta_{s_1,\ldots,s_j}
  \over
   {r\choose s_j}{s_j\choose s_{j-1}}\cdots{s_2\choose s_1}}
 }
 \tag{1.3}
\]

and, if an owner is also prescribed,

\[
 d_x(o_T,S_1,\ldots,S_j)=
 \begin{cases}
 \displaystyle{eta_{s_1,\ldots,s_j}\over
   {r\choose s_j}{s_j\choose s_{j-1}}\cdots{s_2\choose s_1}},
       &S_j\subset T,\\[3mm]
 0,&S_j\not\subset T.
 \end{cases}
 \tag{1.4}
\]

#### Proof

An initial-set family from one ordering is a flag, proving the zero case.
For a fixed owner containing `S_j`, the number of relative orderings of its
coordinates which realize the prescribed flag gives probability

\[
 {1\over
   {r\choose s_j}{s_j\choose s_{j-1}}\cdots{s_2\choose s_1}}.
\]

Multiply by the joint rank probability `eta` and, for (1.3), by the number
`binom(2r-s_j,r-s_j)` of possible owners.  `square`

For two comparable targets `S subset U`, of ranks `s<t`, (1.3) gives the
particularly transparent normalizations

\[
 {d_x(S,U)\over d_x(U)}
 ={\eta_{s,t}\over q_t{t\choose s}},
 \qquad
 {d_x(S,U)\over d_x(S)}
 ={\eta_{s,t}\over q_s{2r-s\choose t-s}}.
 \tag{1.5}
\]

Equations (1.1)--(1.5) are the complete weighted codegree ledger: a
nonzero collection consists of at most one owner and one target flag.

## 2. The forced critical pair

Suppose the weighted law misses total target mass `o(W)`.  Since the total
load missing from rank `s` is

\[
 W(p_s-q_s),
\]

we have

\[
 \sum_{s<r}(p_s-q_s)=o(1).
 \tag{2.1}
\]

In the scalar-optimal fractional law the left side is even at most
`binom(d+1,2)/W`, but (2.1) is all that is needed.

The top two strict-lower rank ratios are

\[
 p_{r-1}={r\over r+1},
 \qquad
 p_{r-2}={r(r-1)\over(r+1)(r+2)}.
 \tag{2.2}
\]

Hence `q_(r-1)=1-O(1/r)-o(1)` and the same holds at rank `r-2`.
For any two events,

\[
 \eta_{r-2,r-1}
 \ge q_{r-2}+q_{r-1}-1=1-O(1/r)-o(1).
 \tag{2.3}
\]

Take any flag `S subset U` of these two ranks.  The first identity in
(1.5) yields

\[
 {d_x(S,U)\over d_x(U)}
 ={\eta_{r-2,r-1}\over q_{r-1}(r-1)}
 ={1-o(1)\over r}.
 \tag{2.4}
\]

This proves (0.1).  Notice that it is forced by the target marginals; no
choice of the dependence structure of `R` can reduce it.

Also

\[
 \mathbb E|R|=\sum_{s<r}q_s
 ={\Lambda\over W}-o(1)
 =\left({\sqrt\pi\over2}+o(1)\right)\sqrt r.
 \tag{2.5}
\]

The last asymptotic follows from

\[
 { {2r\choose r-j}\over {2r\choose r}}
 =\exp\left(-{j^2\over r}
       +O\left({j\over r}+{j^3\over r^2}\right)\right)
 \tag{2.6}
\]

and a Gaussian Riemann sum.  Some supported atom has at least the average
number of target vertices, proving (0.2), and (0.3) follows from (2.4).

## 3. Why a small deleted symmetric collar does not help

Delete, without proving a compatible physical prechainization, the top `a`
strict-lower ranks

\[
 r-a,\ldots,r-1
\]

from the atom matching and retain the same exchangeable owner-chain law,
or a symmetrized residual law for which the uniform-order flag formulas
(1.3)--(1.5) remain valid.  Suppose the residual construction still misses
only `o(W)` targets.  Its two highest ranks are

\[
 s=r-a-2,\qquad t=r-a-1.
\]

If `a=o(sqrt(r))`, (2.6) gives `p_s,p_t=1-o(1)`.  Therefore the same
inclusion--exclusion and (1.5) argument gives

\[
 \rho_2\ge{1-o(1)\over r}.
 \tag{3.1}
\]

The residual expected atom size is

\[
 \sum_{u\le r-a-1}q_u
 =\left({\sqrt\pi\over2}+o(1)\right)\sqrt r
 \tag{3.2}
\]

for `a=o(sqrt(r))`, so (0.3) is unchanged.

More generally put `a=(c+o(1))sqrt(r)`.  The two highest residual
marginals converge to `exp(-c^2)`.  Their joint occurrence is forced by
the marginals to be at least

\[
 (2e^{-c^2}-1)_+-o(1).
 \tag{3.3}
\]

Thus a necessary condition even to make this elementary forced codegree
lower bound vanish is `c>=sqrt(log 2)`.  Since

\[
 d=\left({\sqrt\pi\over2}+o(1)\right)\sqrt r,
\]

this is precisely (0.4).  The conclusion is deliberately one-way.  It does
not apply to an arbitrary fixed named prechainization that conditions or
changes the residual ordering law.  At or beyond that threshold, other
codegrees and the extension compatibility of a prechainized collar remain
open.

## 4. Exact boundary of the black-box nibble route

The quantitative growing-uniformity theorem most often used in the current
research record is Theorem 3.9 of Alon--Bollobas--Kim--Vu, *Economical
covers with geometric applications*.  For a `K`-uniform nearly
`D`-regular hypergraph with maximum pair codegree `C`, its growing-rank
hypothesis includes

\[
 e^{2K}C=o(D/\log D),
 \tag{4.1}
\]

and its matching residual contains the factor

\[
 K\left({C\log(1+C)\over D}\right)^{1/(K-1)}.
 \tag{4.2}
\]

Primary source:
<https://web.math.princeton.edu/~nalon/PDFS/abkv4.pdf>.

In any regular-uniform blow-up which preserves the saturated weighted
degrees and codegrees above, `C/D>=(1-o(1))/r` and
`K>=Theta(sqrt(r))`.  Consequently the left side of (4.1), divided by
`D/log D`, is at least

\[
 {e^{2K}\log D\over(1+o(1))r},
\]

which diverges.  Moreover (4.2) is not an `o(r^(-1/2))` uncovered
fraction at this scale.  Thus this theorem cannot be applied diagonally to
the full chain atoms.

This statement has two scope qualifications.

1. The atom hypergraph is naturally nonuniform.  Passing to a
   regular-uniform blow-up is already a favorable extra assumption; the
   ABKV theorem does not apply directly to the raw nonuniform law.
2. Failure of (4.1) is **not** a nonexistence theorem.  A specialized
   process may exploit that all nonzero higher codegrees are flags, the
   exact formulas (1.3)--(1.4), Boolean exchanges, or absorption.

Even a qualitative fixed-uniformity Pippenger theorem would be
insufficient: it only promises `o(Lambda)=o(sqrt(r)W)` missed target
vertices, whereas `gamma_d(k)=o(W)` requires relative leave
`o(r^(-1/2))`.  Since an atom carries `Theta(sqrt(r))` targets, it also
requires all but `o(W/sqrt(r))` of the owner capacity to be used.

## 5. The precise missing matching theorem

The static route now requires the following object-specific assertion.

> **Critical Boolean flag-matching theorem.**  For the owner-plus-flag
> atom law above, with the exact degree and all-flag codegree profile
> (1.1)--(1.4), there is an integral atom matching covering all but `o(W)`
> named targets (equivalently, using all but `o(W/sqrt(r))` of the required
> owner capacity).

This theorem must work on the critical surface

\[
 K=Theta(\sqrt r),\qquad \rho_2=Theta(1/r),
 \qquad K^2\rho_2=Theta(1),
\]

and must obtain a leave one factor `sqrt(r)` sharper than a qualitative
almost-perfect matching theorem.  Therefore a proof must use the laminar
flag geometry or an explicit Boolean switching/absorption system, not only
maximum degree, maximum pair codegree, and edge size.

Even if this critical flag-matching theorem is proved, it closes only the
static parameter `gamma_d(k)=o(W)`.  The sliding suffix cocycle, literal
interval closure, Euler serialization, upper coverage, and regeneration
remain separate physical gates.
