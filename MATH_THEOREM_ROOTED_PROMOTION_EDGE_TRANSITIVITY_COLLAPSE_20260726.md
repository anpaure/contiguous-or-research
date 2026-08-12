# Rooted promotion rings: edge transitivity collapses the arbitrary dual

Date: 2026-07-26

Method: pure mathematics. No probabilistic or matching black box is used.

## 0. Result

Let \(\mathcal G_0\) be the rooted middle promotion-ring catalogue at a
packing-side critical height. Its vertices are

\[
 \mathcal A=\binom{[2m]}{m-H}
 \quad\text{and}\quad
 \mathcal X=\binom{[2m]}m,
\]

and an edge is a pair \((A,\pi)\), consisting of the root marker \(A\)
and all \(M=m+H\) middle windows of an oriented cyclic order \(\pi\) on
\(A^c\). Write

\[
 N=|\mathcal A|=N_H,
 \qquad R=(M-1)!,
\]

so that every root has degree \(R\) and

\[
 |E(\mathcal G_0)|=NR.
\]

Let \(\nu(\mathcal G_0)\) be its ordinary matching number and
\(\chi_f'(\mathcal G_0)\) its fractional edge-chromatic number. Then

\[
 \boxed{\chi_f'(\mathcal G_0)={NR\over\nu(\mathcal G_0)}.}
 \tag{0.1}
\]

Consequently

\[
 \boxed{
 \chi_f'(\mathcal G_0)\le R+o(R/\sqrt m)
 \iff
 \nu(\mathcal G_0)=N-o(N/\sqrt m).}
 \tag{0.2}
\]

Thus the rooted arbitrary-weight representative inequality is not a
second theorem beyond owner packing. For the full rooted middle
catalogue it is exactly equivalent, with the same error, to one
unweighted near-\(\mathcal A\)-perfect matching.

This collapses the fibre-dense arbitrary-dual lane at the middle rank.
It does not prove the matching estimate in (0.2), and it does not apply
without a separate symmetry audit to a fixed-frame or fixed-tag residual
catalogue.

The same identity applies to the covering-side one-hole catalogue
\(\mathcal R^-\), whose edge is a top together with \(M-1\) cyclic
middle windows and a marked deleted phase.  That catalogue is also
edge-transitive, and therefore

\[
 \boxed{\chi_f'(\mathcal R^-)
 ={N_HM!\over\nu(\mathcal R^-)}.}
 \tag{0.3}
\]

In particular, every arbitrary-weight statement for the full one-hole
catalogue again collapses exactly to its unweighted maximum matching.
The fractional matching value \(W/(M-1)\) does not by itself determine
the integral \(\nu(\mathcal R^-)\).

## 1. Edge-transitive fractional colouring identity

### Lemma 1.1

Let \(\mathcal H=(V,E)\) be a finite hypergraph and suppose a group
\(G\le\operatorname{Aut}(\mathcal H)\) acts transitively on \(E\). Then

\[
 \boxed{\chi_f'(\mathcal H)={|E|\over\nu(\mathcal H)}.}
 \tag{1.1}
\]

#### Proof

Let \((\lambda_Q)\) be any fractional edge colouring, indexed by
matchings \(Q\), so

\[
 \lambda_Q\ge0,
 \qquad
 \sum_{Q\ni e}\lambda_Q\ge1\quad(e\in E).
\]

Sum these inequalities over all edges. Since every matching has size at
most \(\nu(\mathcal H)\),

\[
 |E|
 \le \sum_Q\lambda_Q|Q|
 \le \nu(\mathcal H)\sum_Q\lambda_Q.
\]

Hence \(\chi_f'(\mathcal H)\ge |E|/\nu(\mathcal H)\).

For the reverse inequality, fix a maximum matching \(Q_0\). Average its
images \(gQ_0\), \(g\in G\). Edge transitivity and orbit--stabilizer
give, for every fixed \(e\in E\),

\[
 {1\over|G|}\sum_{g\in G}\mathbf1_{\{e\in gQ_0\}}
 ={\nu(\mathcal H)\over|E|}.
\]

Assign weight \(|E|/(|G|\nu(\mathcal H))\) to every image \(gQ_0\),
with multiplicity. Every edge receives total weight one, while the total
colour weight is \(|E|/\nu(\mathcal H)\). This proves (1.1). \(\square\)

### Corollary 1.2 (all weights and all subcatalogues)

For every \(E'\subseteq E\) and every nonnegative edge weight \(w\),

\[
 \nu_w(\mathcal H[E'])
 \ge {\nu(\mathcal H)\over |E|}\,w(E').
 \tag{1.2}
\]

Indeed, extend \(w\) by zero outside \(E'\), average \(w(gQ_0)\) over
\(g\in G\), and intersect the maximizing image with \(E'\). Thus the
full-catalogue unweighted matching number also controls every weighted
residual with no additional loss.

## 2. Application to rooted promotion rings

The symmetric group \(S_{2m}\) acts on \(\mathcal G_0\) by relabelling
the ground coordinates. Given two rooted frames \((A,\pi)\) and
\((A',\pi')\), a bijection sending the cyclic list \(\pi\) to \(\pi'\)
also sends \(A\) to \(A'\). Hence this action is transitive on catalogue
edges. Lemma 1.1 and \(|E|=NR\) give (0.1).

Put

\[
 \nu(\mathcal G_0)=N-\ell.
\]

Then exactly

\[
 \chi_f'(\mathcal G_0)
 ={NR\over N-\ell}
 ={R\over1-\ell/N}.
 \tag{2.1}
\]

If \(\ell=o(N/\sqrt m)\), equation (2.1) is
\(R+o(R/\sqrt m)\). Conversely, if the latter chromatic estimate holds,
then

\[
 {1\over1-\ell/N}=1+o(m^{-1/2}),
\]

which forces \(\ell=o(N/\sqrt m)\). This proves (0.2).

## 3. Exact implication boundary

Proved here:

1. the general edge-transitive identity (1.1);
2. the residual weighted transfer (1.2);
3. edge transitivity of the full rooted middle promotion catalogue; and
4. exact equivalence (0.2) between its arbitrary-dual estimate and its
   unweighted matching estimate; and
5. the one-hole identity (0.3).

Still open:

1. the near-\(\mathcal A\)-perfect matching in (0.2);
2. a growing-uniformity nibble or absorber proving it; and
3. the stronger nested-rank tagged resolution required by the
   coefficient-one theorem.

The practical consequence is that weighted odd meshes cannot be a
strictly stronger obstruction at the full middle-catalogue level: any
such obstruction must already lower the ordinary maximum matching.
