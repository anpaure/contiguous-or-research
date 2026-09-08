# Final audit of the GMM--Middle-Levels depth-one common-refinement theorem

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

Audited source:
MATH_THEOREM_Q1_COMMON_REFINEMENT_GMM_MIDDLE_LEVELS_HALL_20260726.md.

## 0. Verdict

The main theorems are correct after the source's explicit separation of the
coverage and balanced floor/ceiling versions.

* The incidence cut (2.3) is necessary and sufficient for upper-exact,
  lower-hole-free completion of a fixed core.
* It is not sufficient for lower load at most two. The exact balanced
  residual system is (2.3a)--(2.3d), whose determinant-two owner minor is
  genuine.
* A forest core yields at most

  \[
                    d={2W\over m+2}=o(W/H)
  \]

  components precisely under the stated hypothesis \(H=o(m)\).
* The GMM rigid/flexible occurrence criterion and the Middle-Levels
  coverage/balance criteria are correct.
* The qualitative pseudoforest gives no \(o(W/H)\) rate. The separate PBBS
  construction has the stated quantitative rates on
  \(H=o(m/\log ^2m)\), but still lacks exact residual completion.

One notational correction is needed in the PBBS source used in Section 5:
its Theorem 3.1 writes \(N_1-o(W/H)\) after using \(N_j\) for category
sizes. Its proof gives

\[
             N-o(W/H),\qquad N=\binom{2m+1}{m-1}.
\]

This is the interpretation required in the audited note.

No audited claim proves the desired common refinement or constant one.

## 1. Load and point-degree ledgers

On the odd ground,

\[
 W=\binom{2m+1}m=|\mathcal U|,\qquad
 N=\binom{2m+1}{m-1}={m\over m+2}W,\qquad
 d=W-N={2W\over m+2}.
\]

A spanning two-factor has \(W\) edges. Upper injectivity is therefore
upper bijection, while lower injectivity is impossible. Lower coverage
forces

\[
                       \sum_R(\mu(R)-1)=d.
\]

Coverage alone allows a load greater than two. Balanced floor/ceiling means
every load is one or two and exactly \(d\) lower colours are doubled.

For a balanced factor, let \(\mathcal Q\) be the doubled lower family. At a
fixed coordinate \(x\), counting factor-edge endpoints containing \(x\)
gives

\[
 2\binom{2m}{m-1}
 =\binom{2m}{m}+\binom{2m}{m-2}+d_{\mathcal Q}(x).
\]

Hence

\[
                 d_{\mathcal Q}(x)={d(m-1)\over2m+1},
\]

verifying Proposition 1.1. This is necessary, not sufficient.

## 2. Audit of Theorems 2.1--2.3

For an admissible core \(F\), there are \(d\) unused upper colours and
total middle degree deficit \(2d\). Build the network

* from the source to each unused upper set \(U\), capacity two;
* from \(U\) to each middle facet \(X\subset U\), capacity one;
* from \(X\) to the sink, capacity \(\delta_F(X)\).

For \(\mathcal A\subseteq\mathcal X\), one \(U\) can deliver at most
\(\min\{2,d_{\mathcal A}(U)\}\) units into \(\mathcal A\). Thus
max-flow/min-cut gives exactly (2.3). An integral flow chooses two distinct
facets of every unused \(U\); their pair is one Johnson edge of union
\(U\). Conversely every completion gives this flow. No simplicity issue
is hidden: an old edge cannot have an unused union colour, and distinct
upper colours give distinct new edges.

The waste--slack rewrite is algebraically correct. The universal slack is
nonnegative because the regular bipartite incidence graph between ranks
\(m\) and \(m+1\) contains a spanning two-factor.

For balance, selecting the two facets independently is illegal: their pair
determines the lower colour. Equations (2.3a)--(2.3d) correctly impose one
edge for each unused upper colour, lower residual capacity one, and every
middle deficit. The displayed owner minor has determinant two, so this is
not the preceding network flow.

Every completed component either was already a cycle component of \(F\),
or contains a new edge. Hence

\[
                       c(C)\le d+c_{\rm cyc}(F).
\]

Conversely, choosing one occurrence of each lower colour in any coverage
common refinement produces the stated core, and the discarded edges give
the residual flow. Theorems 2.1--2.3 are therefore correct.

Finally,

\[
                       {d\over W/H}={2H\over m+2}.
\]

The claimed little-oh follows exactly from \(H=o(m)\); it would fail at
linear depth.

## 3. GMM rigid-occurrence audit

A contracted GMM tight enumeration is a Hamilton Johnson cycle \(P\) with
all lower colours present. Its occurrence graph has one edge
\((\ell(e),u(e))\) per cycle edge. It is simple because one flag
\(R\subset U\) determines one Johnson edge, and a simple cycle does not
repeat an edge.

The total lower excess is \(d\), so at most \(d\) lower vertices have
degree greater than one. Every degree-one lower vertex forces its unique
upper neighbour in any lower-saturating occurrence matching. These forced
upper neighbours must be distinct. After deleting them, Hall on the at
most \(d\) flexible lower vertices is necessary and sufficient. This
proves Theorem 3.1.

For an upper colour forced by \(r\) degree-one lower colours, at most one
forced occurrence can remain. Summing \(r-1\) proves the edit lower bound
\(\rho(P)\). If a transversal exists, it is a proper edge subset of one
simple Hamilton cycle because \(N<W\), hence a forest. The occurrence
criterion correctly remains separate from the residual cut (2.3), and
from the stronger balanced system.

## 4. Middle-Levels audit

The added lexical-factor component theorem also passes.  The union of the
\(0\)- and \(1\)-lexical perfect matchings is the published spanning
Middle-Levels cycle factor.  Suppressing every upper vertex preserves its
number of components and gives each upper colour exactly once.  The
published component classification indexes its cycles by plane trees with
\(m\) edges.  Forgetting the root is a surjection from rooted ordered plane
trees onto plane trees, so their number is at most
\(\operatorname {Cat}_m\).  Finally

\[
 \binom{2m+1}{m}=(2m+1)\operatorname {Cat}_m.
\]

Thus

\[
 c(Q_{\rm lex})\le\operatorname {Cat}_m
 =\frac{W}{2m+1}=o(W/H)
\]

for \(H=o(m)\).  Its lower-support and lower-fibre-cap conditions remain
additional; the published plane-tree component classification does not
assert them.

Suppressing upper vertices from a Middle-Levels Hamilton cycle gives a
Hamilton cycle on all middle owners. Every suppressed upper set is the
union of its neighbouring facets, so upper colours occur exactly once.

Therefore complete lower support is exactly the coverage criterion.
Choosing one edge of each lower colour leaves a proper subset of a simple
cycle and hence a forest. The deleted \(d\) edges have exactly the unused
upper colours and exactly fill the middle deficits, so they are the
residual flow.

For balance, lower coverage plus \(\mu(R)\le2\) is necessary. It is also
sufficient: precisely \(d\) lower colours occur twice, and after retaining
one occurrence of each colour, the deleted \(d\) edges have pairwise
distinct lower colours. Thus (4.2) is the exact balanced criterion.

## 5. Pseudoforest and PBBS rates

If a two-sided rainbow forest has \(N-k\) edges, then on all \(W\) owners
it has \(d+k\) path or isolated components, misses \(k\) lower colours,
has \(d+k\) unused upper colours, and has total middle deficit \(2(d+k)\).
System (5.3) correctly couples each missing lower colour, one unused upper
colour, and the two endpoints of its lifted flag. It is not a network
system. Adding \(k\) edges to a forest creates at most \(k\) core cycles,
so any later coverage completion has at most \(d+k\) components. Therefore
\(k=o(W/H)\) is the right sufficient rate. The fixed-girth diagonal gives
only \(k=o(W)\).

The singleton-cut warning is legitimate at the level claimed. Fix a middle
owner \(X\). For each \(b\notin X\), choose distinct \(a_b,c_b\in X\) and
the edge with union \(X\cup\{b\}\) and endpoints
\(X-a_b+b,X-c_b+b\). Across distinct \(b\), endpoints and lower colours
are distinct. This \(O(m)\)-edge matching isolates \(X\) while using all
upper cofacets of \(X\), so its singleton residual cut is \(2\le0\).
It is a poisoned near-forest witness, not an extendible exact lower core.

For the PBBS construction,

\[
                       A=\binom{2m-1}{m-1}=\Theta(W).
\]

The discarded upper-collision mass over \(O(\log m)\) phases is

\[
                       O(W\log m/m),
\]

and the interval/cut ledger is

\[
                       O(W\log ^2m/m).
\]

The category tail is smaller. Adding unused owners as isolated vertices
does not change the second asymptotic order. This total component bound is
\(o(W/H)\) under

\[
                       H=o(m/\log ^2m),
\]

which includes every fixed Gaussian window. These rates do not solve the
integral exactification or the residual Hall system.

## 6. Final boundary

The odd-ground coverage problem is correctly reduced to either:

1. a Middle-Levels cycle with complete lower support; or
2. a forest exact lower core satisfying every residual incidence cut.

For exact floor/ceiling balance, replace these respectively by:

1. complete lower support with every lower load at most two; or
2. an integral solution of (2.3a)--(2.3d).

The component target then follows automatically from \(H=o(m)\). What
remains unproved is the integral colour/owner common refinement itself.
