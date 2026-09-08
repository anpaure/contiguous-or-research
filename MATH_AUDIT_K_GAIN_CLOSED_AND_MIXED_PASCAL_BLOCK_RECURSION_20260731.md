# Independent audit of the gain-closed and mixed-partner Pascal block recursion

Date: 2026-07-31  
Status: **PASS after one decisive global correction and one topology-scope correction**

## 1. Verdict

The local Pascal-square, partner, three-facet pivot, and parallel-cut
monodromy formulas in
`MATH_THEOREM_K_GAIN_CLOSED_PASCAL_BLOCK_RECURSION_20260731.md` are exact.
The initially proposed gain-closed existence route, however, is empty in
every nondegenerate dimension.  Exact gain closure seals a proper
alternating subcycle inside the central Hamilton cycle.  The theorem note
now records this correction as Theorem 2.3.

The correct nonvacuous replacement is a mixed retained/gain partner bank.
If

\[
 \mathcal R\mathbin{\dot\cup}\mathcal Y=\mathcal U,
 \qquad |\mathcal X|=|\mathcal Y|=|\mathcal P|=K,
\]

where \(\mathcal X\) is the direct-label bank, \(\mathcal Y\) is the
gain bank, and \(\mathcal P\to\mathcal X\) is the selected port matching,
then

\[
 t:=|\mathcal X\setminus\mathcal Y|
   =|\mathcal X\cap\mathcal R|
\]

is exactly the number of balanced alternating intervals cut out by
\(\mathcal P\cup\mathcal X\) in the central cycle.  Exactly \(t\) direct
labels require retained partners; the other \(K-t\) receive automatic gain
partners.  Necessarily \(t\ge1\).

This is a structural obstruction and a sharp replacement invariant, not a
counting heuristic.  It does not obstruct larger nonlocal switches or a
mixed construction satisfying the retained-partner incidence conditions.

## 2. Closed-subcycle theorem

Let \(C_0\) be a simple alternating Hamilton cycle with bipartition
\(L\mathbin{\dot\cup}U\), where \(|L|=|U|=A\).  Let

\[
 \mathcal P=\{r_i:i\in[K]\}\subset L,
 \qquad
 \mathcal X=\{x_i:i\in[K]\}\subset U
\]

be distinct banks, and suppose that \(r_ix_i\in E(C_0)\).  Write \(y_i\)
for the other neighbour of \(r_i\).

### Theorem 2.1 (closed alternating-subcycle obstruction)

If \(\{y_i:i\in[K]\}=\mathcal X\) as a multiplicity-one identity, then
\(\mathcal P\cup\mathcal X\) is a union of entire components of \(C_0\).
If \(C_0\) is one cycle and \(K>0\), this forces \(K=A\).

#### Proof

Every \(r_i\) has both neighbours \(x_i,y_i\) in \(\mathcal X\).  The
\(2K\) incidences from \(\mathcal P\) therefore lie in
\(C_0[\mathcal P\cup\mathcal X]\).  Conversely, every
\(x\in\mathcal X\) occurs once in the selected bank and once in the gain
bank.  The two corresponding ports are distinct, since equality would make
the two neighbours of one port equal.  Hence every \(x\in\mathcal X\) also
has both neighbours in \(\mathcal P\).  The induced subgraph is two-regular
and has no boundary edge.  It is consequently a union of full cycle
components.  Connectedness of \(C_0\) forces it to be all of \(C_0\), so
\(|\mathcal P|=|\mathcal X|=A\).  \(\square\)

For the Pascal split,

\[
 A=\binom{2m-1}{m-1},\quad
 B=\binom{2m-1}{m-2}>0,\quad
 K=A-B,
\]

so \(0<K<A\) for every \(m\ge2\).  Thus the exact gain identity is
impossible before the no-\(z\) palette, fragment topology, floor profile,
or repair orientation is tested.

## 3. Exact mixed-partner interval law

Assume instead that the gains form a distinct bank \(\mathcal Y\), not
necessarily equal to \(\mathcal X\).  Put

\[
 t=|\mathcal X\setminus\mathcal Y|
  =|\mathcal Y\setminus\mathcal X|.
\]

### Theorem 3.1 (interval and boundary identity)

The induced graph

\[
 H=C_0[\mathcal P\mathbin{\dot\cup}\mathcal X]
\]

is a disjoint union of exactly \(t\) balanced alternating paths.  Moreover,

\[
 |V(H)|=2K,\qquad |E(H)|=2K-t,\qquad
 |\delta_{C_0}(V(H))|=2t.                         \tag{3.1}
\]

Every component has one endpoint in
\(\mathcal X\setminus\mathcal Y\) and one port endpoint whose gain lies
in \(\mathcal Y\setminus\mathcal X\).  In particular \(t\ge1\).

#### Proof

The \(K\) selected edges \(r_ix_i\) form a perfect matching of \(H\).
A second edge at \(r_i\) lies in \(H\) exactly when
\(y_i\in\mathcal X\).  There are
\(|\mathcal X\cap\mathcal Y|=K-t\) such edges, so (3.1)'s first two
equalities follow.  Since \(K<A\), the vertex set is a proper nonempty
subset of one simple cycle; its induced subgraph is therefore a forest.
Consequently

\[
 c(H)=|V(H)|-|E(H)|=t.
\]

The selected matching restricts to a perfect matching on each component,
so every path is balanced and has endpoints on opposite shores.  A direct
vertex has degree one exactly when its label is absent from the gain bank;
a port has degree one exactly when its gain leaves the direct bank.  These
are the stated endpoint types.  Each path contributes two boundary edges,
giving the last identity in (3.1).  \(\square\)

Under the exact tagged palette

\[
 \mathcal R\mathbin{\dot\cup}\mathcal Y=\mathcal U,
\]

we have

\[
 \mathcal X\setminus\mathcal Y=\mathcal X\cap\mathcal R.
\]

Hence exactly \(t\) direct labels have retained distinguished partners,
and exactly \(K-t\) have gain partners.  The forbidden gain-closed case is
\(t=0\); the fully rooted retained-partner case is \(t=K\).  The smallest
possible mixed recursion state is \(t=1\): one balanced selected/gain path
with one retained-label end and one escaping-gain end.

## 4. Partner dichotomy and literal contiguity

For a selected square write

\[
 d_i=r_is_i,\qquad x_i=r_i\cup s_i,
\]

so its new direct occurrence is

\[
 D_i=x_i0-s_i1.
\]

The exact tagged palette gives the following exhaustive dichotomy.

1. If \(x_i\in\mathcal Y\), there is a unique \(j\) with
   \(y_j=x_i\).  The distinguished gain occurrence is
   \(E_j=x_i0-r_j1\), so it automatically shares \(x_i0\) with \(D_i\).
   One must still exclude \(r_j=s_i\); otherwise the direct and gain
   occurrences coincide in projection and the full enumeration contains
   the isolated triangle
   \(x_i0-s_i0-s_i1-x_i0\).
2. If \(x_i\notin\mathcal Y\), then
   \(x_i\in\mathcal R\).  Its unique distinguished occurrence is a
   retained tagged-child edge.  It cannot meet \(x_i0\), and is contiguous
   with \(D_i\) if and only if it is incident with \(s_i1\).

Thus the interval law by itself does **not** supply the \(t\) retained
incidences.  Those incidences are precisely the additional physical state
an induction must carry.  With them, the nondegeneracy condition in the
gain cases, distinct ports, squarefree direct labels, and connected
fragment monodromy, the cap-two conclusion has no further hidden local
condition.  Injectivity of the \(s_i\) is not needed for upper cap-two;
it is needed for the lower full floor profile.

## 5. Three-facet pivots: two different formulas

The gain and retained categories have different physical pivots.  They
must not be merged into one formula.

For a gain partner \(y_j=x_i\),

\[
 X_i=x_i,\qquad h_i=r_j,\qquad \alpha_i=s_i,\qquad
 U_i=z+x_i,\qquad d_i=z+(r_j\cap s_i).              \tag{5.1}
\]

For a retained partner \(s_i1-c_i1\), where
\(s_i\cup c_i=x_i\),

\[
 X_i=z+s_i,\qquad h_i=z+(s_i\cap c_i),\qquad
 \alpha_i=s_i,\qquad U_i=z+x_i,\qquad d_i=c_i.      \tag{5.2}
\]

Both follow from

\[
 d_i=(h_i\cap\alpha_i)
       \cup\bigl(U_i\setminus(h_i\cup\alpha_i)\bigr).
\]

The \(z\)-parities in (5.1)--(5.2) separate the two categories **within
each individual repair shore**.  Distinctness is nevertheless still
required within each category.  In addition, the complete duplicate bank
\(\{d_i\}\) must be disjoint from the complete hole bank \(\{h_i\}\): a
gain \(d_i\), which contains \(z\), can collide with a retained \(h_j\),
and a retained \(d_i\) can collide with a gain \(h_j\).  Uniform cyclic
sign remains a separate directed-repair condition.  Neither the central
interval forest nor the common-colour forest proves
pivot-unitriangularity of the full alternative-host atlas.

## 6. Physical degree two and fragment topology

Within the mixed master, distinct ports make the vertical edges distinct,
and distinct direct labels \(x_i\) make the new cross edges
\(x_i0-s_i1\) distinct.  Each switch then preserves degree two.  Deleting
the selected parent edges, contracting the resulting fragments, and
retaining the \(2K\) new connections gives an exact component-preserving
fragment graph.  Connectedness of that graph is equivalent to one output
cycle.

There is one scope correction to the stand-alone topology statement.  If
the squarefree direct-label hypothesis is dropped, distinct ports alone do
not guarantee a simple physical output.  Two child direct edges
\(r_1-s,r_2-s\) can have the same union \(x\); switching both adds the
same cross edge \(x0-s1\) twice.  Degree two survives only in the
transition multigraph.  Therefore Section 4's general statement must
either retain pairwise distinct \((x_i,s_i)\) (in particular distinct
\(x_i\)), or explicitly speak about a multigraph.  The stated mixed master
already assumes distinct \(x_i\), so its application is sound.

## 7. Successor permutation and parity

In the parallel-oriented subfibre, let \(\alpha\) and \(\beta\) be the
cyclic successor permutations of the selected cuts in the two parent
cycles.  Starting at \(x_i0\), one traverses the new direct edge, the
forward \(C_1\)-fragment, the vertical edge, and the backward
\(C_0\)-fragment, returning at

\[
 \pi(i)=\alpha^{-1}\beta(i).
\]

Thus components are exactly the cycles of \(\pi\).  Since both
\(\alpha\) and \(\beta\) are \(K\)-cycles,
\(\operatorname {sgn}(\pi)=+1\).  If the output is connected, \(\pi\)
is a \(K\)-cycle, forcing \(K\) odd.

This calculation is correct but its scope is strict: “parallel at every
port” is stronger than “all repair blocks have one directed sign.”  A
twisted signed-port bank is not governed by the unsigned permutation
\(\alpha^{-1}\beta\), so the result is not an even-\(K\) obstruction to
arbitrary uniform directed repair.  It is also logically independent of
gain closure; after Theorem 2.1, the gain-closed Hamilton fibre itself is
empty.

## 8. Small-fixture scope

The authenticated fixture audit supports, but does not enlarge, the
theorem scope.

* At \(m=2\), the census is complete over the six rooted saturating cycles
  and their 24 common-refinement decorations.  For every split coordinate
  passing the crossing-count test, the two direct rows have the same sole
  vertical candidate, so the inverse-square matching rank is \(1<2\).
  This closes those one-coordinate, all-direct-square fibres only.
* At \(m=3\), the positive and mixed results are complete only within the
  explicitly listed cycle fibres.  Their maximum single-coordinate direct
  crossing count is \(3<5\).  They are not a census over every
  \(m=3\) common refinement.
* The vendored GMM \(m=3\) cycle has no common transversal in its audited
  host/orientation fibre.  That is not a global \(m=3\) no-go.

None of these finite statements rules out multi-coordinate or nonlocal
rethreading.  The closed-subcycle theorem is uniform in \(m\), but only for
the exact gain-closed one-coordinate square architecture.

## 9. Final audited boundary

Proved and nonvacuous:

* the mixed \(t\)-interval/boundary law;
* the exact gain-versus-retained partner dichotomy;
* literal cap-two sufficiency after the \(t\) retained incidences,
  gain nondegeneracy, simple square support, and connected monodromy;
* the category-specific pivot identities; and
* parallel-cut successor monodromy and its scoped even-\(K\) obstruction.

Proved impossible:

* exact gain closure \(t=0\) on a proper subset of one central alternating
  Hamilton cycle.

Still open:

* an all-dimensional mixed construction, especially the minimal
  \(t=1\) retained-anchor recursion;
* connected twisted monodromy in every dimension;
* distinct pivots with one directed sign; and
* leaf peeling of the full occurrence-labelled repair atlas.

## 10. Bound inputs

The audited source snapshot and finite calibration are bound by SHA-256:

* `MATH_THEOREM_K_GAIN_CLOSED_PASCAL_BLOCK_RECURSION_20260731.md` --
  `2290522c1318f1269fded06f458a5acf8d605607f635bf4937c9767e174a4cde`;
* `MATH_AUDIT_K_GMM_BLOCK_CONTIGUITY_SMALL_FIXTURES_20260731.md` --
  `81a03d4d67173d490b402c4718c8d858a35291e188a9626eaa371c38b50dfeed`;
* `scratch/audit_k_gmm_block_contiguity_m2_m3_20260731.py` --
  `b91a1f0bba0c9fc639b310355e4860d39419cba5b99a5833abb0f379e7ad58c2`;
* `scratch/k_gmm_block_contiguity_m2_m3_20260731.audit.json` --
  `638a00fd583984473d07ffd635769cd4f7d277d9f6a3579e20759313d49744f6`.
