# Long trace switches: common-core augmenting linkages

Date: 2026-07-31  
Status: exact augmenting theorem for arbitrary alternating-circuit switches;
complete classification of the eleven repairing \(C_{10}\)'s in the audited
\({\rm ML}(7)\) fixture; smallest counterexample to old-witness-only descent

## 1. Scope

Let \(C\) and \(C'\) be middle-levels Hamilton cycles related by one
Hamilton-safe alternating-circuit switch, and let
\({\cal G}_C,{\cal G}_{C'}\) be their augmented trace graphs. Both graphs
are balanced bipartite graphs of shore size

\[
 N=\binom{2m-1}{m-1}+\binom{2m-1}{m-2}.
\]

This note concerns only the fixed-middle-levels-cycle sufficient subclass.
It does not make an arbitrary Catalan linear matching
middle-levels-resolvable.

## 2. The right object is the common graph

Put

\[
 H={\cal G}_C\cap{\cal G}_{C'},\qquad
 A=E({\cal G}_{C'})\setminus E(H).                   \tag{2.1}
\]

Thus all deletions caused by the physical switch have already been charged
inside \(H\), while \(A\) consists of the genuinely new augmented edges.

### Theorem 2.1 (common-core augmenting-linkage theorem)

Let \(M\) be a maximum matching of \(H\), of size \(N-r\). Then
\({\cal G}_{C'}\) has a perfect matching if and only if it contains
\(r\) pairwise vertex-disjoint \(M\)-alternating augmenting paths whose
endpoints are precisely the \(2r\) vertices exposed by \(M\).

More generally, \(t\) pairwise vertex-disjoint augmenting paths give

\[
             \operatorname {def}({\cal G}_{C'})\le r-t.           \tag{2.2}
\]

Hence, if the old deficiency is \(d>0\), the switch strictly improves it
whenever \(t>r-d\).

#### Proof

Toggling pairwise vertex-disjoint \(M\)-augmenting paths preserves the
matching property and increases its size by one per path, proving (2.2)
and sufficiency.

Conversely, suppose \(P\) is a perfect matching of
\({\cal G}_{C'}\). In \(M\mathbin\triangle P\), every vertex exposed by
\(M\) has degree one and its incident edge belongs to \(P\); every other
nonisolated vertex has degree two. The symmetric difference therefore
decomposes into alternating cycles and exactly \(r\) alternating paths.
Each path has one exposed endpoint on each shore and begins and ends with a
\(P\)-edge, so all \(r\) are \(M\)-augmenting and together cover all
exposed vertices. \(\square\)

This is an exact augmenting-path theorem for a long or compound physical
switch. It differs from applying Berge augmentation directly to the old
graph: the deletions must first be absorbed into the common graph \(H\).

### Corollary 2.2 (exact no-new-witness cut)

For \(X\) in the left shore, put

\[
 \rho_H(X)=|X|-|N_H(X)|.
\]

The switch gives a perfect augmented matching if and only if

\[
 \boxed{\quad
 |N_A(X)\setminus N_H(X)|\ge \rho_H(X)
 \quad\text{for every }X.
 \quad}                                                \tag{2.3}
\]

#### Proof

The new neighbour set is
\(N_{{\cal G}_{C'}}(X)=N_H(X)\cup N_A(X)\). Substitution in Hall's
inequality gives (2.3). \(\square\)

Formula (2.3), or equivalently Theorem 2.1, is the exact structural
condition which lowers every relevant Hall cut without creating another
one. Checking only maximum witnesses of the **old** graph cannot work:
deleted edges can expose a new witness which was not tight before the
switch.

## 3. The eleven repairing \(C_{10}\)'s

Use the \({\rm ML}(7)\) Hamilton cycle from
MATH_THEOREM_CATALAN_TRACE_SWITCH_DEFICIENCY_AND_SHORT_FLIP_LOCAL_MINIMUM_20260731.md.
Its augmented graph has shore size \(56\), matching size \(55\), and
deficiency one.

Every one of the \(94\) Hamilton-safe alternating \(C_{10}\)'s in this
fixture changes exactly fifteen augmented edges: five cycle-incidence
edges, five upper-turn edges and five lower-turn occurrence edges. Thus
its common graph has \(125\) of the old \(140\) edges.

There are \(94\) Hamilton-safe alternating \(C_{10}\)'s. Exactly eleven
repair the augmented deficiency. Their circuit vertices, common-graph
deficiency \(r\), and one audited family of \(r\) augmenting-path lengths
are:

\[
\begin{array}{c|c|c}
\text{circuit in cyclic order}&r&\text{path lengths}\\ \hline
7,15,13,77,76,108,100,102,38,39&5&3,7,9,9,9\\
13,29,28,92,84,116,52,53,37,45&5&3,3,3,9,15\\
13,15,14,46,38,102,100,108,76,77&6&3,3,3,7,9,9\\
7,39,37,45,41,43,35,99,67,71&5&3,3,11,15,15\\
26,30,28,60,52,54,38,46,42,58&6&1,3,7,7,9,11\\
35,39,38,54,52,60,44,45,41,43&4&7,9,9,11\\
35,39,38,54,50,58,56,57,41,43&4&3,5,7,9\\
35,39,37,101,97,113,49,57,41,43&5&1,3,3,13,19\\
37,45,41,43,42,46,38,54,52,53&4&3,3,9,13\\
13,29,28,92,84,85,21,53,37,45&3&3,3,3\\
7,15,13,77,76,78,70,102,38,39&4&3,7,9,9
\end{array}                                           \tag{3.1}
\]

Thus the common deficiencies have histogram

\[
                         3^1\,4^4\,5^4\,6^2.          \tag{3.2}
\]

The repair is genuinely correlated. No repairing circuit leaves an old
near-perfect matching intact: deleting its fifteen augmented edges lowers
the common matching rank by between two and five additional units. The
new edges then supply a complete linkage of three to six disjoint
augmenting paths. The \(C_{10}\) is therefore not one hidden unit move; it
is a synchronized deletion-and-rerouting packet.

## 4. Old maximum witnesses are not a potential

Fix any maximum matching \(M\) of the old augmented graph. It exposes one
left vertex \(u\) and one right vertex \(v\). There is an exact description
of every old maximum Hall witness \(X\):

1. \(u\in X\);
2. no member of \(X\) is adjacent to \(v\); and
3. whenever \(x\in X\) and \(xy\) is an old edge with \(y\) matched by
   \(M\), the mate \(M(y)\) also lies in \(X\).

#### Proof

If \(u\notin X\), the matching injects \(X\) into \(N(X)\), so \(X\) is
not deficient. For a deficiency-one set containing \(u\), the
\(|X|-1\) matched images of \(X\setminus\{u\}\) already fill \(N(X)\).
The unmatched right vertex cannot occur, and the mate of every neighbour
must return to \(X\), or the neighbourhood would gain an extra vertex.
Conversely these three conditions make the matched images exactly
\(N(X)\), of size \(|X|-1\). \(\square\)

This turns optimization over all old maximum witnesses into one
maximum-weight closure/min-cut calculation: left vertices have weight
\(+1\), new right neighbours weight \(-1\), and the implications in item 3
are infinite-capacity arcs.

### Theorem 4.1 (smallest new-witness counterexample)

In the same \({\rm ML}(7)\) fixture, toggle the Hamilton-safe alternating
hexagon

\[
                  26,30,28,60,56,58.                 \tag{4.1}
\]

The maximum, over **every** old maximum Hall witness \(X\), of

\[
                  |X|-|N_{{\cal G}_{C'}}(X)|
\]

is zero. Thus the switch strictly repairs every old maximum witness.
Nevertheless the new augmented graph still has deficiency one. A new
component-Hall witness consists of three consecutive lower positions with
middle masks

\[
                         \{98,38,22\}.                \tag{4.2}
\]

It uses only upper colour \(118\), while its collar traps lower colours
\(\{6,18,34\}\), and hence has violation

\[
                         3-1-1=1.                    \tag{4.3}
\]

Both turn maps remain surjective. Therefore even

> strictly lower every old maximum Hall witness

is not an augmenting theorem: preventing newly exposed cuts is essential.
This counterexample has the minimum circuit length because the
middle-levels graph has no \(C_4\), and the minimum dimension because every
\({\rm ML}(5)\) Hamilton cycle has zero augmented deficiency.

The phenomenon is common rather than exceptional. Among the \(83\)
nonrepairing Hamilton-safe \(C_{10}\)'s, \(26\) repair every old maximum
witness but create a new positive witness. The common-core criterion (2.3)
detects all of them.

## 5. Consequence

Long switches do admit an exact augmenting-path theorem, but it lives in the
common augmented graph, not in the physical circuit alone and not in the
old deficiency witness lattice. For recursive work, a proposed packet is
certified by either:

1. a complete augmenting linkage relative to a maximum matching of the
   common graph; or
2. the equivalent common-core Hall inequalities (2.3).

This is polynomial and exact for a supplied switch. It is not an all-\(m\)
existence theorem for such switches. Transparent gluing, the direct ordered
four-transversal route, and arbitrary Catalan linear matchings remain
separate.

## 6. Reproducible audit

Run

    python3 scratch/audit_catalan_trace_long_switch_augmenting_linkage_20260731.py

The audit reconstructs all \(94\) Hamilton-safe alternating \(C_{10}\)'s,
the eleven repairs, every common matching deficiency and augmenting linkage,
the closure/min-cut optimization over every old maximum witness, and the
new \(C_6\) witness (4.2)--(4.3).
