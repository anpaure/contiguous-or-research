# Collision-path phase selection for a repaired ECO shadow

Date: 2026-07-31
Status: exact abstract phase criterion; sharp union-bound threshold; exact
asymmetric/symmetric local-lemma sufficient conditions; no claim that the
raw canonical ECO carrier has an owner-aligned decoration

## 0. Scope and verdict

Fix one coordinate rotation of the coherent ECO family. Its physical-port,
lower-owner-repeat and upper-owner-repeat collision graphs are the same path
forest. Choosing one alternating parity class on each nontrivial path
therefore gives a bank of atoms with pairwise-disjoint six-port supports and
with no repeated forced owner on either shore.

If a preliminary repair changes any port occurrence or forced owner, this
collision forest must be reverified. The theorem applies unchanged to the
recomputed forest, but the canonical ECO path law cannot simply be imported
through an arbitrary rethread.

The useful multiplicity of a binary component adjacency is not its raw
number of ECO witnesses. Witnesses in one parity class of one collision
path make only one independent phase offer. A witness on each parity of the
same path makes the adjacency automatic. After this contraction, the exact
phase problem is a CNF on one bit per nontrivial collision path.

For a fixed target spanning tree with \(q\) edges, if every edge has at least
\(r\) independent phase offers, then

\[
                              q<2^r                 \tag{0.1}
\]

guarantees a collision-free phase containing the whole binary tree. More
generally the exact union-bound condition is

\[
                 \sum_{e\in E(T)}2^{-\tau(e)}<1,    \tag{0.2}
\]

with automatically covered edges contributing zero. Condition (0.1) is
sharp using multiplicities alone: at equality \(q=2^r\), a disjoint union of
\(r\) collision paths can realize all \(2^r\) complementary bad phase
assignments, so that every global phase misses a different tree edge.

Sparse sharing of phase bits gives the stronger Lovasz-local-lemma
criterion in Section 4.

This is only a binary-shadow selection theorem. It does not turn
two-section connectivity into a literal component merge. The selected
atoms must still form a common physical cube and be component-faithful (or
an incidence hypertree with a proved unit expansion). Nor does parity
injectivity imply leaf-forest owner alignment, residual gap Hall, private
occurrence routing, residence or the compiler. In particular the raw
canonical \(m=5\) ECO counterexample lies upstream: it has no upper
transversal even though its minimal ECO ports and forced faces are already
disjoint. The correct use is

\[
 \text{repair/rethread}\to\text{phase-select ECO shadow}
 \to\text{owner-align/Hall}\to\text{route}.          \tag{0.3}
\]

## 1. Path phases and faithful binary witnesses

Let \(\mathcal X\) be a path forest on a finite atom set \(\mathcal A\).
For every nontrivial path component \(P_i\), fix its alternating
bipartition

\[
                         P_i=P_i^0\sqcup P_i^1.      \tag{1.1}
\]

An isolated atom is selected deterministically; selecting the empty side of
an isolated path would only discard a conflict-free atom. Let
\(\mathcal A_{\rm iso}\) be the isolated atoms. For a phase vector
\(\sigma\in\{0,1\}^{I}\), define

\[
       \mathcal A(\sigma)=\mathcal A_{\rm iso}
                  \cup\bigcup_{i\in I}P_i^{\sigma_i}.               \tag{1.2}
\]

Because each parity class is independent and different path components do
not meet, \(\mathcal A(\sigma)\) is collision-free.

Let \(V\) be the set of old factor components. To every atom \(a\), assign
a set \(Q(a)\subseteq\binom V2\) of certified binary shadows. The
meaning of \(xy\in Q(a)\) is only that this atom is an admissible witness for
the abstract component adjacency \(xy\) after the preliminary repair. Put

\[
 G_\sigma=\left(V,\ \bigcup_{a\in\mathcal A(\sigma)}Q(a)\right).    \tag{1.3}
\]

Fix a spanning tree \(T\) on \(V\). For \(e\in E(T)\), let

\[
                         W_e=\{a:e\in Q(a)\}.        \tag{1.4}
\]

For a nontrivial collision path \(P_i\), define its allowable phase set

\[
 A_{e,i}=\{b\in\{0,1\}:W_e\cap P_i^b\ne\varnothing\}.              \tag{1.5}
\]

Call \(e\) automatic if either
\(W_e\cap\mathcal A_{\rm iso}\ne\varnothing\), or
\(A_{e,i}=\{0,1\}\) for some \(i\). If \(e\) is not automatic, put

\[
 J_e=\{i:|A_{e,i}|=1\},\qquad
 \tau(e)=|J_e|,                                      \tag{1.6}
\]

and write \(b_{e,i}\) for the unique element of \(A_{e,i}\). For an
automatic edge set \(\tau(e)=\infty\) and interpret \(2^{-\infty}=0\).
The number \(\tau(e)\) is the phase multiplicity. Repeated atoms in the
same \(P_i^b\) count once, not with their raw multiplicity.

## 2. Exact phase CNF

### Theorem 2.1 (exact phase criterion)

There exists a phase \(\sigma\) for which \(T\subseteq G_\sigma\) if and
only if the CNF

\[
 \Phi_T=\bigwedge_{\substack{e\in E(T)\\e\ {\rm not\ automatic}}}
              \left(\ \bigvee_{i\in J_e}[\sigma_i=b_{e,i}]\right)   \tag{2.1}
\]

is satisfiable. An empty clause, equivalently a nonautomatic edge with
\(\tau(e)=0\), is an exact obstruction.

#### Proof

An automatic edge has a selected witness under every phase. Otherwise,
the only paths that can supply \(e\) are the paths in \(J_e\), and path
\(i\) supplies it exactly when \(\sigma_i=b_{e,i}\). Thus \(e\) belongs to
\(G_\sigma\) exactly when its clause in (2.1) is true. Taking the
conjunction over the tree edges proves the equivalence. \(\square\)

Under independent fair phase bits, let \(B_e\) be the event that a
nonautomatic tree edge is absent. The theorem gives the exact cylinder
event

\[
 B_e=\bigcap_{i\in J_e}\{\sigma_i=1-b_{e,i}\},
 \qquad
 \Pr(B_e)=2^{-\tau(e)}.                              \tag{2.2}
\]

This identity is the reason phase multiplicity, rather than atom count, is
the correct probabilistic parameter.

## 3. Union-bound selection and its sharpness

### Theorem 3.1 (inhomogeneous phase-union theorem)

If

\[
          \sum_{\substack{e\in E(T)\\e\ {\rm not\ automatic}}}
                            2^{-\tau(e)}<1,           \tag{3.1}
\]

then some phase \(\sigma\) satisfies \(T\subseteq G_\sigma\). Hence the
chosen collision-free atom bank has a connected binary shadow.

#### Proof

By (2.2) and the union bound,

\[
 \Pr\!\left(\bigcup_e B_e\right)
       \le\sum_e2^{-\tau(e)}<1.
\]

Therefore a phase outside every bad event exists. Theorem 2.1 gives all
edges of \(T\), and (1.2) gives collision-freeness. \(\square\)

### Corollary 3.2 (uniform multiplicity)

If \(q=|E(T)|\) and every nonautomatic tree edge has phase multiplicity at
least \(r\), then \(q<2^r\) is sufficient. Equivalently, it is enough that

\[
                 r\ge\left\lceil\log_2(q+1)\right\rceil.            \tag{3.2}
\]

The proof is constructive without search over all phases. Starting from
the conditional expectation

\[
              \mathbf E\!\left[\sum_e{\bf1}_{B_e}\right]<1,
\]

expose the phase bits one at a time and choose the value which does not
increase this conditional expectation. At the end its value is a
nonnegative integer smaller than one, hence zero.

### Corollary 3.3 (biased phase form)

Let the phase bits be independent with
\(\Pr(\sigma_i=1)=p_i\), where \(0<p_i<1\). For a nonautomatic edge put

\[
 q_{e,i}=
 \begin{cases}
   p_i,&1-b_{e,i}=1,\\
   1-p_i,&1-b_{e,i}=0 .
 \end{cases}                                         \tag{3.3}
\]

Then

\[
                    \Pr(B_e)=\prod_{i\in J_e}q_{e,i}.               \tag{3.4}
\]

Consequently

\[
                 \sum_e\prod_{i\in J_e}q_{e,i}<1                   \tag{3.5}
\]

is sufficient. The asymmetric local lemma in Section 4 also remains valid
with \(2^{-\tau(e)}\) replaced by the product in (3.4).

#### Proof

The coordinates in (2.2) are independent, and \(q_{e,i}\) is exactly the
probability of its required bad value. The union-bound and local-lemma
proofs are otherwise unchanged. \(\square\)

### Proposition 3.4 (the threshold is sharp from multiplicity alone)

For every \(r\ge1\), there is a path-forest witness system and a target
tree with \(q=2^r\) edges such that every edge has phase multiplicity exactly
\(r\), but no phase contains the target tree.

#### Proof

Label the target-tree edges \(e_\omega\) by
\(\omega\in\{0,1\}^r\). Make \(r\) mutually disjoint collision paths
\(P_1,\ldots,P_r\), each with \(2^r\) vertices in alternating parity. On
path \(P_i\), biject the parity-\(b\) vertices with the strings satisfying
\(1-\omega_i=b\); the two sets both have size \(2^{r-1}\). Let the vertex
labelled \((i,\omega)\) witness only the strict binary edge \(e_\omega\).

Thus \(e_\omega\) has one witness on each of the \(r\) distinct paths, of
parity \(1-\omega_i\), and so \(\tau(e_\omega)=r\). Under phase
\(\sigma\), this edge is absent exactly when
\(\sigma_i=\omega_i\) for every \(i\), that is, exactly when
\(\sigma=\omega\). Hence every one of the \(2^r\) phases misses its
correspondingly labelled tree edge. \(\square\)

The first member \(r=1\) is the smallest obstruction in which every
required edge has at least one witness. There are three
component vertices, two target-tree edges, and one two-vertex collision
path. Its parity-zero atom witnesses the first edge and its parity-one atom
witnesses the second. Either phase loses one required edge. This is the
CNF \((\sigma)\wedge(\neg\sigma)\), and (3.1) is tight with sum one.

## 4. Sparse-dependency local lemma

The union bound ignores that different tree edges may depend on disjoint
sets of collision paths. On the nonautomatic tree edges, define the
standard variable-dependency graph

\[
 e\sim f\quad\Longleftrightarrow\quad J_e\cap J_f\ne\varnothing.    \tag{4.1}
\]

Let \(\Gamma(e)\) be the neighbours of \(e\).

### Theorem 4.1 (asymmetric phase LLL)

If numbers \(x_e\in(0,1)\) exist such that, for every nonautomatic tree
edge,

\[
 2^{-\tau(e)}\le x_e\prod_{f\in\Gamma(e)}(1-x_f),                  \tag{4.2}
\]

then a phase \(\sigma\) with \(T\subseteq G_\sigma\) exists.

#### Proof

The bad event \(B_e\) is determined only by the independent phase bits in
\(J_e\). It is therefore independent of the sigma-algebra generated by all
bad events outside \(\Gamma(e)\cup\{e\}\). Equation (2.2) and the
asymmetric Lovasz local lemma give positive probability that no \(B_e\)
occurs. Apply Theorem 2.1. \(\square\)

### Corollary 4.2 (symmetric and incidence forms)

Let

\[
 \Delta=\max_e|\Gamma(e)|,\qquad
 r=\min_e\tau(e).                                    \tag{4.3}
\]

Then it suffices that

\[
                  {\rm e}(\Delta+1)\le2^r.           \tag{4.4}
\]

More explicitly, if

\[
             \lambda_i=|\{e:i\in J_e\}|,             \tag{4.5}
\]

then

\[
 |\Gamma(e)|\le\sum_{i\in J_e}(\lambda_i-1).         \tag{4.6}
\]

Thus (4.4) remains valid with

\[
       \Delta\ \hbox{replaced by}\
       D=\max_e\sum_{i\in J_e}(\lambda_i-1).         \tag{4.7}
\]

#### Proof

The symmetric local lemma with \(p=2^{-r}\) gives (4.4). Every event
dependent on \(B_e\) shares at least one \(i\in J_e\); path bit \(i\) is
used by at most \(\lambda_i-1\) other events. Summing, possibly counting
one neighbour more than once, gives (4.6). \(\square\)

Failure of (4.2) or (4.4) is not an impossibility certificate. The exact
criterion remains satisfiability of (2.1). Proposition 3.4 is a genuine
obstruction because its bad cylinders cover the whole phase cube.

## 5. Optional cut form when the spanning tree is not fixed

One need not prescribe \(T\). For one representative \(S\) of every
nontrivial bipartition of \(V\), let \(W_S\) be the atoms having a certified
binary shadow crossing \((S,V\setminus S)\), and define
\(\tau(S)\) exactly as in (1.5)--(1.6). If

\[
       \sum_{\varnothing\ne S\subsetneq V\,/\,S\sim V\setminus S}
                         2^{-\tau(S)}<1,              \tag{5.1}
\]

then some selected shadow crosses every cut and is connected, hence
contains a spanning tree. The same dependency-graph LLL applies to the cut
events. This cut form is logically weaker than demanding every edge of one
preassigned tree, but it has \(2^{|V|-1}-1\) bad events rather than
\(|V|-1\), so it is useful only when cut witness multiplicities are much
larger.

The proof is identical to Theorems 2.1 and 3.1, followed by the elementary
cut characterization of connected graphs.

## 6. Component-faithfulness and the exact handoff boundary

The probabilistic argument sees only the labelled graph \(G_\sigma\). To
convert the selected shadow into literal simultaneous ECO toggles, one must
add one of the following exact physical hypotheses.

1. **Strict binary common cube.** Choose one selected witness for every
   edge of a spanning tree. The chosen atoms have component support exactly
   the two endpoints, form one subset-closed literal common cube, and for
   every subset their physical toggles induce exactly the corresponding
   forest partition.
2. **Faithful incidence hypertree.** Group the selected binary shadows by
   ECO atom, choose at most \(|S_a|-1\) independent unit edges inside each
   component support \(S_a\), and prove that the atom--component incidence
   graph is a tree and that every subset realizes its incidence-forest
   partition.

Without one of these clauses, a connected two-section is not enough. One
ternary atom may contribute several clique edges but only two component-rank
units; two hyperedges may have a Berge cycle; and physically disjoint cuts
on the same old cycle may reconnect with the wrong interleaving. These are
component-faithfulness failures, not phase-selection failures.

Likewise, selecting one parity on the common ECO collision path forest
proves only that the six ports and the two forced-owner triples are
injective. It does not prove that the forced owner edges belong to one
leaf-forest matching. Owner alignment is the later residual-Hall test, and
node-private or laminar occurrence routing is later still.

Consequently the all-\(n\) positive target supplied by this note is precise:

> After a controlled palette/deeper-shadow repair, exhibit a component-
> faithful binary tree (or incidence hypertree) whose every required binary
> unit has enough independent fixed-rotation ECO phase witnesses to satisfy
> (3.1) or (4.2). Then choose the collision-free phase, and only afterward
> solve owner-aligned residual Hall and private/laminar occurrence routing.

The canonical raw \(m=5\) counterexample cannot be bypassed by this lemma:
its missing \(3+3\) period-three turn colours prevent the required repaired
owner/upper witness atlas from existing in the first place.

## 7. Dependencies

* MATH_THEOREM_CATALAN_COHERENT_ECO_HEX_SUPPLY_20260731.md
* MATH_THEOREM_CATALAN_RAW_ECO_OWNER_ALIGNMENT_M5_COUNTEREXAMPLE_20260731.md
* MATH_THEOREM_CATALAN_ECO_OCCURRENCE_CONFLICT_PATH_AND_ROUTER_GATE_20260731.md
* MATH_THEOREM_AD_ECO_OWNER_ROUTED_HYPERTREE_GATE_20260731.md
