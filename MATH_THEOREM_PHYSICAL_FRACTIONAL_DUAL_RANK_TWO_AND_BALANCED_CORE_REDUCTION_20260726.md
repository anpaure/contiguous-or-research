# Physical fractional duals: rank-two odd sets are harmless and the remaining obstruction is a growing branching tangle

Date: 2026-07-26

## 0. Outcome

Let \(\mathcal H^\#\) be the exact target-regular selected physical-port
hypergraph from
`MATH_THEOREM_LOCALIZED_FLAG_BOUNDARY_ADAPTIVE_KERNEL_HIGH_COVER_EKR_20260726.md`.
Write

\[
 D=D_1,
 \qquad
 \mu=\Delta _2(\mathcal H^\#)
 \le (4+o(1)){D\over m}.
\tag{0.1}
\]

The localized theorem proves that every non-star pairwise-intersecting
support has weighted mass \(o(D/\sqrt m)\) times its largest edge weight.
That is exactly the clique part of the fractional-colouring dual, but it
does not imply the full dual: a fractional-chromatic obstruction need not
be a clique.

This note makes the residual precise and proves three new facts.

1. The implication “large stars plus small non-star cliques imply
   coefficient one” is false abstractly.  The first missing object is an
   odd strong cycle (the \(C_5\) dual is the smallest non-clique example).
2. Every **rank-two faithful** physical support nevertheless satisfies

   \[
     \chi_f'\le D+O(D/m)=D+o(D/\sqrt m).
   \tag{0.2}
   \]

   Thus all ordinary odd-set/multigraph obstructions, of every order and
   with arbitrary weights, are harmless at the required precision.
3. A fixed physical incidence gadget whose columns each prescribe at
   least two targets has total size \(O(D/m)\).  Together with the proved
   physical Hilton--Milner theorem and the all-order projective-plane
   exclusion, this rules out every single bounded target-labelled
   odd-cycle gadget and every standard projective-plane multistar.

Consequently the unresolved fractional dual is not a single hidden
triangle, ordinary multigraph odd set, or projective plane.  It must be a
**growing, distributed,
non-clique, rank-at-least-three strong-cycle tangle**.  Two exact
sufficient formulations are given below: a weighted odd-cycle
transversal and a weighted two-anchor compression.  They are strictly
more precise than the previous phrase “arbitrary non-clique support”.

## 1. The exact dual and why EKR alone cannot finish it

Let \(L(\mathcal H^\#)\) be the conflict graph on physical strips: two
vertices are adjacent exactly when their selected target sets intersect.
The fractional edge-chromatic number is

\[
 \chi_f'(\mathcal H^\#)
 =\max\left\{
       \sum_C y_C:
       y_C\ge0,
       \ \sum_{C\in M}y_C\le1
       \text{ for every matching }M
      \right\}.
\tag{1.1}
\]

The weighted Hilton--Milner theorem settles (1.1) when the support of
\(y\) is a clique of \(L(\mathcal H^\#)\): a star has at most \(D\)
members, while a non-star clique has weighted mass \(o(D/\sqrt m)\)
times its largest weight.

There is no general clique decomposition of (1.1).  On an abstract
\(5\)-cycle, the vector \(y_v=1/2\) is feasible in (1.1), has total
\(5/2\), and every clique has size at most two.  Hence even perfect
control of all pairwise-intersecting supports does not control arbitrary
dual supports.

The physical incidence matrix is not balanced either.  It contains the
already audited determinant-two minor

\[
 \begin{pmatrix}
  1&0&1\\
  1&1&0\\
  0&1&1
 \end{pmatrix},
\tag{1.2}
\]

so exact total unimodularity or an exact star decomposition is unavailable.
What matters is that the physical multiplicity of each prescribed target
pair is only \(O(D/m)\).

## 2. Balanced cores and a weighted odd-cycle-transversal criterion

A **strong cycle** in a hypergraph is a cyclic sequence

\[
 T_0,C_0,T_1,C_1,\ldots,T_{\ell-1},C_{\ell-1},T_0
\tag{2.1}
\]

of distinct targets and distinct hyperedges such that, within the selected
rows \(T_i\) and columns \(C_i\), column \(C_i\) contains exactly
\(T_i,T_{i+1}\).  A hypergraph is balanced when it has no odd strong
cycle.  We use the classical balanced-hypergraph edge-colouring theorem:

\[
 \mathcal B\text{ balanced}
 \quad\Longrightarrow\quad
 \chi'(\mathcal B)=\Delta(\mathcal B).
\tag{2.2}
\]

### Theorem 2.1 (weighted odd-cycle-transversal reduction)

Suppose that for every feasible vector \(y\) in (1.1), with support
\(\mathcal F\), there is \(X\subseteq\mathcal F\) such that

\[
 y(X)=o(D/\sqrt m)
\tag{2.3}
\]

and every odd strong cycle of the incidence hypergraph induced by
\(\mathcal F\) contains a column in \(X\).  Then

\[
 \boxed{\chi_f'(\mathcal H^\#)=D+o(D/\sqrt m).}
\tag{2.4}
\]

#### Proof

The induced hypergraph on \(\mathcal F\setminus X\) is balanced, so its
edges admit a proper colouring with at most \(D\) colours by (2.2).  Each
colour class is a matching.  Applying the dual constraints (1.1) to the
colour classes and averaging gives

\[
 y(\mathcal F\setminus X)\le D.
\]

Add (2.3), then maximize over feasible \(y\).  The reverse inequality
\(\chi_f'\ge D\) follows from a target star of degree \(D\). \(\square\)

Theorem 2.1 is support-dependent: one need not find one global deletion
set that balances the entire catalogue.  It is enough to hit the odd
strong cycles carrying one putative dual certificate, at cost measured
in the same dual weight.

The physical Hilton--Milner theorem can pay for one non-star intersecting
piece of \(X\), since every feasible dual has \(\max_Cy_C\le1\).  It
cannot pay for an unbounded union of such pieces without a new aggregate
argument.  This is the precise limitation of “decompose into non-star
cliques”.

## 3. Rank-two faithful supports

Call \(\mathcal F\subseteq E(\mathcal H^\#)\) **two-anchor faithful** if
there is a map

\[
 a:\mathcal F\longrightarrow {V(\mathcal H^\#)\choose2}
\tag{3.1}
\]

such that \(a(C)\subseteq e_C^\#\) for every \(C\), and, for distinct
\(C,C'\in\mathcal F\),

\[
 e_C^\#\cap e_{C'}^\#\ne\varnothing
 \quad\Longleftrightarrow\quad
 a(C)\cap a(C')\ne\varnothing.
\tag{3.2}
\]

Thus all conflicts in the support are faithfully routed through two
anchor targets per strip.

### Theorem 3.1 (rank-two physical fractional colouring)

Every two-anchor faithful physical support satisfies

\[
 \boxed{
 \chi_f'\bigl(\mathcal H^\#[\mathcal F]\bigr)
 \le D+O(D/m)
 =D+o(D/\sqrt m).}
\tag{3.3}
\]

The conclusion is for arbitrary nonnegative weights, not merely the
unweighted support.

#### Proof

Make a multigraph \(G\) on the physical target set by replacing every
strip \(C\in\mathcal F\) by one graph edge with endpoints \(a(C)\).
Equation (3.2) identifies the conflict graph of \(\mathcal F\) with the
line graph of \(G\).  Moreover

\[
 \Delta(G)\le D,
 \qquad
 \mu(G)\le\Delta_2(\mathcal H^\#)=:\mu
 \le(4+o(1)){D\over m},
\tag{3.4}
\]

where \(\mu(G)\) is the largest parallel-edge multiplicity.

Edmonds' fractional edge-colouring formula gives

\[
 \chi_f'(G)
 =\max\left\{
  \Delta(G),
  \max_{\substack{U\subseteq V(G)\\|U|\ge3\ \mathrm{odd}}}
       {2|E_G(U)|\over |U|-1}
       \right\}.
\tag{3.5}
\]

Put \(s=|U|\).  The multiplicity and degree estimates imply

\[
 {2|E_G(U)|\over s-1}
 \le\min\left\{\mu s,{Ds\over s-1}\right\}.
\tag{3.6}
\]

If \(s\le m/8\), the first term in (3.6) is at most
\((1/2+o(1))D\).  If \(s>m/8\), the second is at most

\[
 D+{D\over s-1}=D+O(D/m).
\tag{3.7}
\]

Substitution in (3.5) proves (3.3).  Since fractional chromatic number
already has the all-weights dual formulation, no separate rounding or
uniform-weight argument is being used. \(\square\)

This closes every ordinary odd-set obstruction.  In particular, a long
odd cycle, a dense odd multigraph, and an arbitrary superposition of
multigraph odd sets cannot be the missing physical dual as long as their
conflicts are faithfully represented by two anchors.

## 4. Fixed physical gadgets and standard projective planes

### Lemma 4.1 (fixed incidence-pattern bound)

Fix a finite \(0\)-\(1\) matrix \(P\) with \(s\) columns, each of column
weight at least two.  Fix distinct physical targets for its rows.  The
number of physical port strips realizing any one prescribed column of
\(P\) is at most \(\mu\), and the union of all strips realizing its
columns has size at most

\[
 s\mu=O_P(D/m)=o(D/\sqrt m).
\tag{4.1}
\]

#### Proof

Choose two of the prescribed one-entries in each column.  Every strip
realizing that column lies in the corresponding physical pair-link,
which has size at most \(\mu\).  Sum over the \(s\) columns and use
(0.1). \(\square\)

Thus one target-labelled copy of the determinant-two triangle (1.2), one
fixed odd strong cycle, or one other bounded incidence gadget may occur
physically but is too small by a factor \(\sqrt m\) to affect the compiler
precision.  The same argument permits one pattern with
\(s=o(\sqrt m)\) columns.  A distributed union of many overlapping copies
is not covered by this count; that is part of the tangle isolated below.

For projective planes there is an even stronger result already proved in
the physical EKR work.  A standard multistar realization of the lines is
pairwise intersecting and non-star, so the localized weighted
Hilton--Milner theorem makes it \(o(D/\sqrt m)\); the metric packing
argument in Corollary 3.4 of
`MATH_THEOREM_PHYSICAL_PORT_EKR_HIGH_COVER_REDUCTION_20260726.md`
does this at every growing order.  Therefore neither a bounded Fano
gadget nor a growing standard projective-plane multistar is the missing
dual.

## 5. The exact remaining branching obstruction

The two proved mechanisms cover opposite extremal shapes:

* a pairwise-intersecting support is either contained in a star or has
  total mass \(o(D/\sqrt m)\) at dual normalization;
* supports whose conflicts route through two anchors have fractional
  chromatic index \(D+O(D/m)\).

What they do not cover is a support in which many strips participate
essentially through three or more collision targets and in which the
resulting odd strong cycles overlap in a non-clique way.

The following is an exact sufficient compression statement.

### Theorem 5.1 (weighted two-anchor compression criterion)

Suppose that for every feasible dual vector \(y\) in (1.1) there is a
set \(X\) with

\[
 y(X)=o(D/\sqrt m)
\tag{5.1}
\]

such that \(\operatorname {supp}(y)\setminus X\) is two-anchor faithful.
Then (2.4) holds.

#### Proof

Restrict \(y\) to the two-anchor faithful part.  It remains feasible for
the matching dual of that induced support, so Theorem 3.1 bounds its mass
by \(D+O(D/m)\).  Add (5.1) and maximize over \(y\). \(\square\)

Failure of both Theorems 2.1 and 5.1 has a concrete meaning.  There must
exist a feasible dual \(y\) of excess \(\Omega(D/\sqrt m)\) such that,
after deleting every set of \(y\)-mass \(o(D/\sqrt m)\),

1. odd strong cycles remain;
2. their conflicts cannot be routed through two target anchors per strip;
3. no pairwise-intersecting non-star part carries significant mass; and
4. no fixed incidence pattern or standard projective-plane multistar
   carries significant mass.

Equivalently, the obstruction must be a growing distributed
**three-branching strong-cycle tangle**.  This is the minimal physical
non-clique gate left by the verified EKR theorem.

## 6. What the flag chronology has and has not proved

The cyclic flag chronology is used essentially in (0.1): it supplies the
selected physical pair kernel

\[
 \Delta_2\le(4+o(1))D/m,
\tag{6.1}
\]

which is what closes all rank-two odd sets in Theorem 3.1 and every
bounded gadget in Lemma 4.1.  The localized Boolean-envelope chronology
then closes all non-star cliques, including all standard physical
projective-plane multistars.

The chronology has **not** yet supplied a weighted odd-cycle transversal
or a two-anchor compression for an arbitrary dual support.  The crossing
minor (1.2) shows that an exact statement of that kind cannot hold with
zero exceptional mass.  The correct next theorem is one of the two
quantitative statements

\[
 \boxed{
 \begin{array}{ll}
 \text{(WOT)}&
 \text{hit all odd strong cycles of every dual support at }y\text{-cost }
 o(D/\sqrt m),\\[1mm]
 \text{(W2A)}&
 \text{delete }y\text{-cost }o(D/\sqrt m)\text{ and route every remaining
 conflict through two anchors.}
 \end{array}}
\tag{6.2}
\]

Either theorem, combined with the results already in the workspace,
proves the required coefficient-one fractional edge-colouring.  Neither
follows from EKR alone.  The old vague “non-clique fractional dual” gate
should therefore be replaced by the growing three-branching tangle in
Section 5, with (WOT)/(W2A) as two exact sufficient targets.
