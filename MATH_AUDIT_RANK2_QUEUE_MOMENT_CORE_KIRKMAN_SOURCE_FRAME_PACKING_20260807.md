# Independent audit of the moment-core Kirkman source-frame packing

**Date:** 2026-08-07  
**Audited theorem:**  
MATH_THEOREM_RANK2_QUEUE_MOMENT_CORE_KIRKMAN_SOURCE_FRAME_PACKING_20260807.md  
**Audited theorem SHA-256:**  
\[
\texttt{73869bb631325a36eafaadded4644b7e2662cc846db700647b1c3c188e2a2627}.
\]
**Verdict:** **PASS**. The theorem gives an unconditional
rank-\(s\)-target-disjoint legal-frame supply. It does not recouple those
frames to an owner-disjoint queue-ring packing.

## 1. Moment-colour code

For a prime \(n<Q<2n\), colouring a \(c\)-set \(K\) by its first two
power sums in \(\mathbb F_Q\) gives a class of size at least
\(Q^{-2}{n\choose c}\).

If two members differ at Johnson distance one, first-moment equality
forces the exchanged elements to be equal. If they differ at distance
two, equality of the first two moments gives equal sums and equal
products of the two exchanged pairs. Since \(Q\) is odd, the two pairs
are the roots of the same quadratic and hence are identical. Thus
distinct same-colour cores have Johnson distance at least three.

A rank-\((c+2)\) set containing two \(c\)-cores would put those cores at
Johnson distance at most two. Therefore the complete \(+2\) shadows of
the selected cores are pairwise disjoint.

## 2. Kirkman decomposition and frame loss

For one core \(K\), let \(U=[n]\setminus K\), \(N=|U|\), and take
\(N'\le N\), \(N'\equiv3\pmod6\), with \(N-N'\le5\). A resolvable
Steiner triple system on \(U'\) has \((N'-1)/2\) parallel classes, each
partitioning \(U'\) into disjoint triples.

Grouping each parallel class into batches of \(p\) triples makes every
batch a legal source frame. Fewer than \(p\) triples are lost per class,
so discarded triples account for \(O(pN)\) pairs. The \(O(1)\) omitted
vertices account for \(O(N)\) pairs. Since \(p=o(N)\), the retained
inventories cover

\[
 (1-o(1)){N\choose2}
\]

members of the core's \(+2\) shadow. Steiner pair uniqueness makes all
inventories for that core disjoint, including inventories from different
parallel classes. Moment-code shadow disjointness makes inventories for
different selected cores disjoint as well.

## 3. Global constant

The covered target count is at least

\[
 (1-o(1))Q^{-2}{n\choose c}{n-c\choose2}.
\]

Using \(s=c+2\),

\[
 {n\choose c}{n-c\choose2}
 ={n\choose s}{s\choose2}.
\]

Since \(s/n\to1/2\) and \(Q<2n\),

\[
 \frac{{s\choose2}}{Q^2}\ge\frac1{32}-o(1).
\]

This proves both the target-density bound and, after dividing by the
exact inventory size \(3p\), the frame-count bound.

At triangular depth, \(d^2/m\to\pi/4\) and \(s=m-2d\). Hence

\[
 \frac{{2m+1\choose m-2d}}{{2m+1\choose m}}
 \longrightarrow e^{-\pi}.
\]

Thus the covered source-target count is
\((e^{-\pi}/32-o(1))W\). This is strictly larger than the required
\(\theta W\), where
\(\theta=4\sum_{a\ge1}e^{-4\pi a^2}<10^{-4}\).

## 4. Literal correspondence

Each batch contains \(p\) pairwise disjoint triples. Ordering them as
phases and cyclically rotating the omitted element in each triple gives
a genuine \(3p\)-position rank-two queue ring with permanent core \(K\).
The three source letters contributed by a triple are exactly its three
pairs adjoined to \(K\), so the abstract Kirkman pair packing is
literally the source inventory of the queue frame.

The theorem proves:

1. legal literal rank-two source frames;
2. pairwise disjoint rank-\(s\) inventories;
3. at least \((1/32-o(1)){n\choose s}\) covered rank-\(s\) targets;
4. target capacity exceeding the PBBS reset demand by a fixed factor.

It does not prove:

1. disjointness of the owner fibres of different selected frames;
2. a common choice of one owner-cycle translate per frame;
3. cross-frame q1 or deeper-target disjointness;
4. physical fusion or the residual compiler.

Accordingly, the exact remaining hinge is the stated owner--source frame
recoupling problem, not either marginal supply.

## 5. Recoupling configuration hypergraph

Write

\[
 \mathcal A=\{q\mathbf1+P_j:q\in\mathbb F_3,\ 0\le j<p\}
\]

for the standard \(3p\)-state ring in one full owner fibre
\(\mathbb F_3^p\). In its natural cyclic order, successive states differ
in one coordinate. No other pair differs in one coordinate: within one
\(q\)-level only consecutive prefixes can be adjacent, and between
different \(q\)-levels the only Hamming-one pairs are the two wrap joins.
Thus the induced distance-one graph is exactly \(C_{3p}\).

If a nonzero translation stabilizes \(\mathcal A\), it induces a
fixed-point-free order-three automorphism of \(C_{3p}\). The only
order-three cycle automorphisms are rotations by \(p\) and \(2p\)
positions. In the displayed parametrization these are translations by
\(\mathbf1\) and \(2\mathbf1\). Therefore

\[
 \operatorname{Stab}(\mathcal A)=\langle\mathbf1\rangle
\]

and there are exactly \(3^{p-1}\) distinct translates.

For a fixed owner state \(X\), the translates containing \(X\) are
uniform by translation symmetry. Double-counting ring--state incidences
gives

\[
 \frac{3^{p-1}\cdot3p}{3^p}=p
\]

such rings. Hence the configuration-hypergraph degrees

\[
 d(F)=3^{p-1},\qquad d(X)=p\,d_{\rm fib}(X)
\]

are exact.

Adding one private frame vertex to every translated-ring edge enforces at
most one chosen ring per frame; its \(3p\) owner vertices enforce global
owner disjointness. Since Theorem 0.1 already makes distinct frame
inventories source-target-disjoint, a matching of size \(H\) is exactly a
choice of \(H\) target-disjoint frames and one owner-disjoint translate in
each. Thus the matching inequality in (5.7) is an exact reformulation of
the remaining owner--source recoupling gate.

## 6. Exact scope

Sections 0--5 of the audited theorem are valid. The configuration
hypergraph is a reduction, not a proof of the required matching. Its
unequal frame and owner degree rows remain uncontrolled.
