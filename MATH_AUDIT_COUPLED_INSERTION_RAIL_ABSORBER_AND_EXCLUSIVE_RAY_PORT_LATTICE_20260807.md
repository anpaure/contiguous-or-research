# Audit of the coupled-insertion absorber and exact lattice of its exclusive rays

**Date:** 2026-08-07  
**Audited file:** MATH_THEOREM_COUPLED_INSERTION_COMPACT_TWO_SIZE_RAIL_ABSORBER_20260807.md  
**Verdict:** PASS.  The insertion current, common reserve, and
\(2\ell-1\) exclusive-value count are exact.  The nested port system has
a full zero-sum *coordinate* lattice on its movable ray labels, but its
named sets form Johnson geodesics.  Consequently arbitrary small named
leaves do not embed in one ray merely from lattice compatibility.

## 1. Exact insertion current

Let the old directed cut be \(a\to b\), and insert \(z\) between them.
For a width \(1\le\ell<n\), an old cyclic \(\ell\)-interval changes if
and only if it contains the cut edge.  Exactly \(\ell-1\) old intervals
do.  Exactly \(\ell\) new intervals contain \(z\).  Therefore

\[
\boxed{
|\mathcal I_\ell(\tau)\cap\mathcal I_\ell(\tau^z)|=n-\ell+1,
\quad
|\mathcal I_\ell(\tau)\setminus\mathcal I_\ell(\tau^z)|=\ell-1,
\quad
|\mathcal I_\ell(\tau^z)\setminus\mathcal I_\ell(\tau)|=\ell.}
\tag{1.1}
\]

This also covers the boundary cases \(\ell=1\) and \(\ell=n-1\).

In the coupled absorber, the \(D+x\) shore uses long-minus-short and the
\(D+y\) shore uses short-minus-long.  Their signatures are disjoint.
Hence at every common proper width:

* common values:
  \[
  2(n-\ell+1)=2(M-\ell-1);
  \]
* plus-only values:
  \[
  \ell+(\ell-1)=2\ell-1;
  \]
* minus-only values:
  \[
  (\ell-1)+\ell=2\ell-1.
  \]

Each state has

\[
2(M-\ell-1)+(2\ell-1)=2M-3
\]

values, as required.  At owner width \(q=d+1\), the exclusive footprint
is exactly \(2q-1=2d+1\) per side.

The coordinate current also passes directly.  On the \(x\)-shore,
long-minus-short is

\[
\mathbf1_{D+x}+\ell\mathbf e_z,
\]

and on the \(y\)-shore short-minus-long is

\[
-\mathbf1_{D+y}-\ell\mathbf e_z.
\]

Their sum is

\[
\boxed{\mathbf e_x-\mathbf e_y.}
\tag{1.2}
\]

Thus the compact coupling preserves the positive unit residue proved by
the uncoupled four-carousel macro.

## 2. Exact normal forms of the two exclusive rays

Write the labels immediately before the cut as

\[
\lambda_1=a,\lambda_2,\lambda_3,\ldots
\]

in reverse temporal order, and those immediately after the cut as

\[
\rho_1=b,\rho_2,\rho_3,\ldots
\]

in forward temporal order.  Put

\[
L_i=\{\lambda_1,\ldots,\lambda_i\},
\qquad
R_j=\{\rho_1,\ldots,\rho_j\},
\qquad L_0=R_0=\varnothing.
\]

### Proposition 2.1 (new-ray normal form)

The \(\ell\) new-only intervals are exactly

\[
\boxed{
N_i^\ell=\{z\}\cup L_i\cup R_{\ell-1-i},
\qquad 0\le i\le\ell-1.}
\tag{2.1}
\]

They form a Johnson geodesic:

\[
|N_i^\ell\cap N_j^\ell|=\ell-|i-j|,
\qquad
d_J(N_i^\ell,N_j^\ell)=|i-j|.
\tag{2.2}
\]

Their common intersection is \(\{z\}\), and their union has size
\(2\ell-1\).

### Proposition 2.2 (old-ray normal form)

For \(\ell\ge2\), the \(\ell-1\) old-only cut-crossing intervals are

\[
\boxed{
O_i^\ell=L_{i+1}\cup R_{\ell-1-i},
\qquad 0\le i\le\ell-2.}
\tag{2.3}
\]

They also form a Johnson geodesic:

\[
|O_i^\ell\cap O_j^\ell|=\ell-|i-j|,
\qquad
d_J(O_i^\ell,O_j^\ell)=|i-j|.
\tag{2.4}
\]

Their common intersection is \(\{a,b\}\), and their union has size
\(2\ell-2\).

Both propositions follow by counting how many labels a window takes from
the two sides of the insertion point.  Adjoining the signature core
\(D+x\) or \(D+y\) preserves every identity.

## 3. Exact named-leave embedding criterion

### Theorem 3.1 (one-width ray criterion)

A labelled family \(\mathcal L\) of \(\ell\)-sets embeds into a subset of
one new exclusive ray if and only if there exist:

* a label \(z\);
* two disjoint ordered rays
  \((\lambda_1,\ldots,\lambda_{\ell-1})\) and
  \((\rho_1,\ldots,\rho_{\ell-1})\), disjoint from \(z\); and
* an injective map \(j:\mathcal L\to\{0,\ldots,\ell-1\}\)

such that

\[
S=\{z\}\cup L_{j(S)}\cup R_{\ell-1-j(S)}
\qquad(S\in\mathcal L).
\tag{3.1}
\]

Likewise, \(\mathcal L\) embeds into an old exclusive ray if and only if
there are two ordered rays and an injection into
\(\{0,\ldots,\ell-2\}\) such that

\[
S=L_{j(S)+1}\cup R_{\ell-1-j(S)}.
\tag{3.2}
\]

For the coupled absorber, a width-\(\ell\) named leave embeds exactly when
it can be partitioned into:

1. a new-ray family of size at most \(\ell\) on one signature shore; and
2. an old-ray family of size at most \(\ell-1\) on the other signature
   shore,

with the common \(D,x,y,z\) labels and the two independently chosen cuts
consistent with the requested signatures.  The opposite absorber state
interchanges the two roles.

This is an exact criterion, not merely a count.

### Multiwidth consistency

Across several widths, the same ordered \(\lambda\)- and \(\rho\)-rays
must work in (3.1)--(3.2), using their initial segments.  Thus independent
one-width embeddings do not automatically compose.  The full
lower/owner/upper leave must admit one common two-ray word on each
signature shore.

## 4. The exclusive-ray coordinate lattice

At a fixed width, consecutive new ports satisfy

\[
\mathbf1_{N_{i+1}^\ell}-\mathbf1_{N_i^\ell}
=\mathbf e_{\lambda_{i+1}}
-\mathbf e_{\rho_{\ell-1-i}}
\qquad(0\le i\le\ell-2).
\tag{4.1}
\]

Consecutive old ports satisfy

\[
\mathbf1_{O_{i+1}^\ell}-\mathbf1_{O_i^\ell}
=\mathbf e_{\lambda_{i+2}}
-\mathbf e_{\rho_{\ell-1-i}}
\qquad(0\le i\le\ell-3).
\tag{4.2}
\]

### Theorem 4.1 (all-width new-ray lattice)

Fix \(h\ge2\).  The lattice generated by (4.1) over all
\(2\le\ell\le h\) is

\[
\boxed{
\left\{v\in
\mathbb Z^{\{\lambda_1,\ldots,\lambda_{h-1},
\rho_1,\ldots,\rho_{h-1}\}}:
\sum_u v_u=0\right\}.}
\tag{4.3}
\]

The coordinate \(z\) is fixed.

#### Proof

The generators are edge differences of the bipartite graph with edges

\[
\lambda_j\rho_t
\qquad(j,t\ge1,\ j+t\le h).
\]

This graph is connected: every \(\lambda_j\) is adjacent to \(\rho_1\),
and every \(\rho_t\) is adjacent to \(\lambda_1\).  The oriented edge
vectors of a connected graph generate its full zero-sum integer lattice.
\(\square\)

### Theorem 4.2 (all-width old-ray lattice)

Fix \(h\ge3\).  The lattice generated by (4.2) over all
\(3\le\ell\le h\) is the full zero-sum lattice on

\[
\boxed{
\{\lambda_2,\ldots,\lambda_{h-1},
\rho_2,\ldots,\rho_{h-1}\}.}
\tag{4.4}
\]

The cut labels \(a=\lambda_1,b=\rho_1\) are fixed.

#### Proof

The generator graph has edges

\[
\lambda_j\rho_t
\qquad(j,t\ge2,\ j+t\le h+1).
\]

It is connected by the same \(\lambda_2,\rho_2\) star argument.
\(\square\)

Thus the nested rays have no further coordinate gcd obstruction on their
movable labels.  Their limitation is named-set geometry, not their linear
lattice.

## 5. A sharp small named obstruction

Lattice compatibility does not imply one-ray embeddability.  At a fixed
width, choose a \((\ell-1)\)-set \(H\) and three fresh labels \(r,s,t\).
The three \(\ell\)-sets

\[
H\cup\{r\},
\qquad H\cup\{s\},
\qquad H\cup\{t\}
\tag{5.1}
\]

are pairwise at Johnson distance one.  Three distinct points of an integer
line cannot be pairwise at distance one.  By (2.2)--(2.4), this family is
not a subset of one new or old exclusive ray, even though it has only
three members and an extremely large common intersection.

After adjoining a fixed signature core, the same obstruction holds on the
owner shore.  Therefore:

\[
\boxed{
\text{an arbitrary small named leave is not automatically absorbable by
one compact insertion ray.}}
\tag{5.2}
\]

This is scoped to a fixed signature/ray assignment; a larger absorber may
split the leave across several rays or introduce intermediate reserve
owners.

### Proposition 5.1 (singleton universality)

Let \(S\subseteq[k]\) have rank \(c+\ell\), where
\(1\le\ell<M-2\).  Then \(S\) can be made one new-exclusive
width-\(\ell\) port of a coupled insertion absorber.

#### Proof

Choose distinct \(x,z\in S\), choose

\[
D\subseteq S\setminus\{x,z\},\qquad |D|=c-1,
\]

and choose \(y\notin S\).  Then

\[
S=(D\cup\{x\})\cup P,
\qquad |P|=\ell,\quad z\in P.
\]

Arrange the labels of \(P-\{z\}\) on the two sides of the insertion cut
and fill the remaining toggle positions arbitrarily.  Formula (2.1)
then makes \(S\) a new-exclusive port. \(\square\)

Consequently every bounded named leave can be assigned one target per
absorber.  This avoids the three-leaf geodesic obstruction at the price
of reserving \(2\ell-2\) additional entering ports and \(2\ell-1\)
departing ports for each absorbed width-\(\ell\) target.  It is therefore
a valid local route for an \(O(1)\)-sized terminal leave, but it still
requires a globally disjoint reserve and compatible coordinate-current
orientations.

## 6. Iterative-absorption implication

The coupled insertion theorem supplies exactly the right positive local
shape:

* \(O(d)\) exclusive owners instead of \(\Theta(k)\);
* coherent nested ports at every width;
* full zero-sum coordinate lattices on the movable ray labels; and
* literal two-ray adjacent-transposition moves.

It does not yet supply universality for named leaves.  A proof-ready next
lemma may take either of two forms:

1. **geodesic leave decomposition:** every sufficiently small admissible
   leave can be partitioned into \(O(1)\) families satisfying Theorem 3.1
   simultaneously at all protected widths; or
2. **reserve closure:** a preselected reserve of intermediate owners makes
   the safe-order graph connect every admissible leave to a union of such
   geodesic families.

The three-leaf obstruction (5.1) shows that no theorem based only on leave
size, coordinate moments, or the count \(2\ell-1\) can suffice.

This audit does not prove the global leave decomposition, common-cap
compatibility, \(\nu(k)\le B(k)+O(1)\), or exact equality.
