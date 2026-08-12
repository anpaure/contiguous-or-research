# PBBS proximity: the distinct-label cut lower bound and its return-interval dual

Date: 2026-07-27

## 1. Omitted-label words

Let \(F\) be a spanning 2-factor of the odd graph \(KG(2m+1,m)\).  For an
oriented factor edge \(A_iA_{i+1}\), let

\[
 g_i=[2m+1]\setminus(A_i\cup A_{i+1})
\]

be its unique omitted coordinate.  Every point-balanced component of length
\(\ell(2m+1)\) has each coordinate exactly \(\ell\) times in its cyclic
omitted-label word.  Indeed, the cyclic incidence identity gives

\[
 2\deg_x(C)=|C|-\#\{i:g_i=x\},
\]

and point balance gives \(\deg_x(C)=m\ell\).

For a wreath, \(\ell=1\), so its edge labels are a permutation of all
\(2m+1\) coordinates.

## 2. A necessary condition for retained PBBS edges

Fix the canonical PBBS factor \(F\), and let \(G\) be any exact wreath
factor.  The common-edge graph

\[
 R=(V,E(F)\cap E(G))
\]

is a disjoint union of paths and cycles.  Each component of \(R\) lies inside
one wreath of \(G\).

### Lemma 2.1 (distinct-label runs)

Every path component of \(R\) has pairwise distinct omitted labels.

#### Proof

A common edge has the same endpoints, hence the same unique omitted label,
in both factors.  The containing wreath of \(G\) uses every coordinate label
exactly once.  No subpath of that wreath can repeat a label. \(\square\)

Define \(\kappa(F)\) to be the minimum number of positions deleted from all
cyclic PBBS label words so that every residual linear run has distinct
labels.  A component which is already one label-simple \(n\)-cycle is allowed
to remain cyclic and contributes zero; it is already a wreath.

### Corollary 2.2 (proximity lower bound)

For every exact wreath factor \(G\),

\[
 \boxed{|E(F)\setminus E(G)|\ge\kappa(F).}
\]

This is only a necessary condition: distinct-label PBBS paths may still have
incompatible endpoints or fail to pack into wreaths.

## 3. Consecutive-return interval duality

In one cyclic label word, join each occurrence of a coordinate to the next
*distinct* cyclic occurrence of the same coordinate.  (A coordinate occurring
once creates no constraint.) Regard the positions from the first occurrence
through the next as a closed circular arc.  Let
\(\mathcal R\) be this family of consecutive-return arcs.

### Proposition 3.1

A position set \(D\) leaves only distinct-label residual runs if and only if
\(D\) meets every arc of \(\mathcal R\).  Consequently the minimum cut number
is the transversal number \(\tau(\mathcal R)\).

#### Proof

If one consecutive-return arc avoids \(D\), its two equal endpoint labels
remain in the same residual run.  Conversely, if a residual run contains two
equal labels, two consecutive cyclic occurrences of that label lie inside
the run, and their return arc avoids \(D\). \(\square\)

Let \(\nu(\mathcal R)\) be the maximum number of pairwise disjoint return
arcs.  Circular-arc piercing gives

\[
 \boxed{\nu(\mathcal R)\le\tau(\mathcal R)le\nu(\mathcal R)+1.}
 \tag{3.1}
\]

For the upper bound, choose one point of the circle, use it to hit every arc
containing it, cut the circle there, and apply interval packing--covering
duality to the remaining line intervals.  Summing componentwise introduces
at most the number of PBBS components as additive slack.

Thus \(\kappa(F_{\rm PBBS})\) is, up to one cut per component, exactly the
all-return packing parameter.  This connects the static nearest-factor
problem to the PBBS return-packing machinery without replacing it by an
occupancy heuristic.

## 4. Exact finite values

The exact dynamic program in
`scratch/audit_pbbs_distinct_label_cuts.py` gives

\[
\begin{array}{c|rrrrrrr}
m&2&3&4&5&6&7&8\\ \hline
C_m&2&5&14&42&132&429&1430\\
\kappa(F_{\rm PBBS})&0&4&16&56&184&632&2257\\
\kappa/C_m&0&0.800&1.143&1.333&1.394&1.473&1.578.
\end{array}
\]

These values do not prove boundedness, but they rule out a finite trend
toward the \(\sqrt m\)- or \(m\)-scale at the first informative dimensions.
At \(m=5\), the lower bound 56 remains far below the best currently verified
factor distance 267, so endpoint compatibility and global exact cover—not
label repetition alone—account for most of the observed gap.

## 5. Sharpened sufficient route

A useful intermediate theorem would be

\[
 \boxed{\kappa(F_{\rm PBBS})=O(C_m).}
 \tag{5.1}
\]

By Proposition 3.1, it is equivalent up to the PBBS component count to an
\(O(C_m)\) packing bound for *all* consecutive coordinate-return arcs.  It
would partition PBBS into \(O(C_m)\) label-simple physical paths.  The next,
strictly stronger step is to group those paths into \(C_m\) endpoint-compatible
wreath packets while maintaining \(o(W)\) signed annular extraction loss.

Statement (5.1) alone does not prove the theorem, but it is a concrete
Catalan-scale bridge between the existing PBBS return estimates and the
nearest-wreath exact-cover formulation.
