# The marker-58 factor: protected incidence circuits, exact cap gain, and the graphic merge gate

**Date:** 2026-08-02  
**Lane:** A, marker-reservoir owner/q1 extension  
**Status:** exact structural theorem and finite local-move reduction.  No SAT
or broad enumeration is used.  The note does not assert that the frozen
factor contains a cap-positive merging circuit.

## 1. Frozen input and conclusion

Let

\[
 {\cal L}={ [17]\choose 8},\qquad
 {\cal M}={ [17]\choose 9},\qquad
 {\cal U}={ [17]\choose10}.
\]

The frozen file
`scratch/k17_marker58_q1_extension_20260802/marker58_q1_factor.tsv`
is an owner two-factor on all `24,310` vertices of \({\cal M}\), with one
edge of each lower colour in \({\cal L}\).  It contains `986` protected
four-edge paths, hence `3,944` protected factor edges.  Its exact audited
statistics are

\[
 1179\text{ components},\qquad
 13307\text{ distinct rank-ten caps},\qquad
 6141\text{ missing caps}.                              \tag{1.1}
\]

The `3,944` protected edges use `986` distinct caps four times each, hence
force exactly `2,958` repeat units.  The `20,366` residual edges must cover
the other `18,462` caps, so an upper-exact completion is allowed `1,904`
residual repeats.  The incumbent has `8,045`; its excess

\[
                         8045-1904=6141                 \tag{1.1a}
\]

is exactly the hole count.  Every protected-avoiding cap gain below acts on
this residual ledger; the marker repeats themselves are immutable.

There is an exact, much simpler representation of this object.  Subdivide
the factor edge of lower colour \(C\) by the vertex \(C\).  The result is a
degree-two subgraph of the bipartite containment graph

\[
 G=({\cal L},{\cal M};E),\qquad
 E=\{(C,T):C\subset T\}.                                \tag{1.2}
\]

This representation gives four rigorous conclusions.

1. Ignoring caps and connectivity, protected palette-exact factors are
   common bases of two partition matroids, equivalently integral bipartite
   \(b\)-flows.  Their exact feasibility has the cut criterion (3.3).
2. The exchange graph of all such protected factors is connected by
   protected-avoiding alternating incidence circuits.
3. For every circuit, cap gain and component merger have the exact local
   formulae (5.3) and (6.1).  Thus a move is simultaneously useful if and
   only if both displayed quantities are positive.
4. A simple `C6` can merge either three components to one or, for a
   different physically legal retained-path pairing, two components to one.
   The exact port-involution formula (7.6) decides the topology; there is no
   parity no-go.  The active simple-`C8` bank remains a second
   proof-complete finite face.  Its old cap values are pairwise distinct, as
   are its new cap values, so its cap score reduces to the singleton-load
   test (7.5).  At `k=17` it has at most `1,750,320` members before
   protection and score filters.

Cap coverage and connectedness are not another ordinary matroid
intersection.  Cap choice is quadratic at every lower vertex, and a
connected degree-two factor adds graphic/subtour constraints.  Section 8
gives the precise obstruction and an exact fixed-witness contraction that
does remain a bipartite flow.

## 2. Bijection between incidence factors and lower-rainbow owner factors

Let \(I\subseteq E(G)\) satisfy

\[
 d_I(C)=2\quad(C\in{\cal L}),\qquad
 d_I(T)=2\quad(T\in{\cal M}).                             \tag{2.1}
\]

For every \(C\), write its two selected owner neighbours as
\(T_C^0,T_C^1\).  They are distinct rank-nine supersets of \(C\), so

\[
 T_C^0\cap T_C^1=C,\qquad |T_C^0\triangle T_C^1|=2.      \tag{2.2}
\]

Join \(T_C^0\) and \(T_C^1\) by an owner edge labelled \(C\).

### Theorem 2.1 (exact subdivision bijection)

Equation (2.1) is in bijection with spanning owner two-factors having every
rank-eight lower colour exactly once.  Under this bijection:

* connected components agree, because (1.2) merely subdivides every owner
  edge once; and
* the cap carried at \(C\) is

\[
                 U_I(C)=T_C^0\cup T_C^1\in{\cal U}.       \tag{2.3}
\]

#### Proof

The construction above gives one lower-labelled edge at every \(C\), and
the second equation of (2.1) gives owner degree two.  Conversely, subdivide
each labelled owner edge at its unique intersection \(C\).  Adjacency makes
the two incidences legal, and lower-colour injectivity makes every \(C\)
occur once.  These operations are inverse.  Subdivision preserves
components, and (2.3) is the definition of the upper colour. \(\square\)

Let \({\cal P}\) be the protected owner-edge bank.  Retaining an edge of
colour \(C\) means forcing **both** incidences at \(C\).  In particular, an
exchange which retains every protected path cannot touch a protected lower
vertex at all.

## 3. The exact common-base and cut formulation

Force the incidences belonging to \({\cal P}\).  Delete every forbidden
incidence and reduce each residual vertex demand to

\[
 b(v)=2-d_{\cal P}(v).                                    \tag{3.1}
\]

Thus a protected lower vertex has demand zero, an internal protected owner
may have demand zero, a protected endpoint owner has demand one, and an
untouched vertex has demand two.  Let \(G_{\cal P}\) be the remaining
allowed bipartite graph.

On its incidence ground set, the inequalities

\[
 |J\cap\delta(C)|\le b(C),\qquad
 |J\cap\delta(T)|\le b(T)                                 \tag{3.2}
\]

define two partition matroids.  A full residual completion is a common
independent set of size \(B=\sum_Cb(C)=\sum_Tb(T)\), hence a common base of
the contracted partition matroids.

### Theorem 3.1 (protected factor min--max)

A protected palette-exact owner factor exists if and only if the two total
demands agree and, for every \(A\subseteq{\cal L}\) and
\(D\subseteq{\cal M}\),

\[
 b(A)\le b(D)+|E_{G_{\cal P}}(A,{\cal M}\setminus D)|.    \tag{3.3}
\]

The polytope (3.2) with the exact degree equations is integral.

#### Proof

Use the network with arcs `source -> C` of capacity \(b(C)\), incidence
arcs \(C\to T\) of capacity one, and arcs `T -> sink` of capacity
\(b(T)\).  A cut whose source side contains \(A\) and \(D\) has capacity

\[
 b({\cal L}\setminus A)+|E(A,{\cal M}\setminus D)|+b(D).
\]

It has capacity at least \(B=b({\cal L})\) exactly when (3.3) holds.
Max-flow/min-cut proves feasibility, and integral capacities give an
integral completion.  This is also the two-partition-matroid intersection
min--max in this special bipartite form. \(\square\)

The frozen factor is already a positive certificate for (3.3).  The point
of the theorem is that later forced incidence banks can be audited without
rebuilding an unrelated owner-edge model.

## 4. The complete protected exchange graph

Let \({\cal F}_{\cal P}\) be the set of all completions in Theorem 3.1.
Join two completions when their symmetric difference is one alternating
incidence circuit in \(G_{\cal P}\).

### Theorem 4.1 (alternating-circuit connectivity)

The exchange graph on \({\cal F}_{\cal P}\) is connected.  More precisely,
if \(I,I'\in{\cal F}_{\cal P}\), then \(I\triangle I'\) decomposes into
red--blue alternating even circuits, and the circuits can be toggled in a
sign-compatible order from \(I\) to \(I'\).  Every intermediate state is a
protected palette-exact owner factor.

#### Proof

Colour \(I\setminus I'\) red and \(I'\setminus I\) blue.  At every lower
and owner vertex the red and blue degrees agree, because both factors have
the same exact degree vector.  The resulting balanced two-coloured graph
decomposes into alternating even circuits.  On one circuit, remove its red
edges and add its blue edges.  Every incident degree is unchanged.  The
decomposition is sign-compatible, so a red edge is removed only once and a
blue edge is added only once; all intermediate incidence variables remain
zero or one.  Forced incidences lie in \(I\cap I'\), hence no circuit uses
them. \(\square\)

This is a completeness theorem for exchange **generation**, not a descent
theorem: a path to a better endpoint need not make the cap or component
objective monotone at every circuit.

## 5. Exact cap delta of one circuit

Let \(Q=(Q^-,Q^+)\) be a simple alternating circuit applicable to \(I\).
At every touched lower vertex \(C\), it replaces one selected owner
\(T_C^-\) by \(T_C^+\), while the other selected owner \(R_C\) is retained.
Define

\[
 U_C^-=R_C\cup T_C^-,\qquad U_C^+=R_C\cup T_C^+.         \tag{5.1}
\]

Let \(o_Q(U)\) and \(n_Q(U)\) be the multiplicities of \(U\) among the old
and new values in (5.1), and let

\[
 \ell_I(U)=|\{C:U_I(C)=U\}|.                              \tag{5.2}
\]

### Theorem 5.1 (local cap ledger)

For \(I'=I-Q^-+Q^+\),

\[
 \ell_{I'}(U)=\ell_I(U)-o_Q(U)+n_Q(U),                    \tag{5.3}
\]

and the change in the number of distinct caps is exactly

\[
 \Delta_{\rm cap}(Q)=
 \sum_{U\in{\cal U}}
 \left({\bf1}_{\ell_I(U)-o_Q(U)+n_Q(U)>0}
       -{\bf1}_{\ell_I(U)>0}\right).                     \tag{5.4}
\]

Thus only the cap loads on the touched old/new values are needed.

#### Proof

Only the selected pair at a touched lower vertex changes.  Summing those
literal deletions and insertions gives (5.3), and taking supports gives
(5.4). \(\square\)

## 6. Exact component delta

Put \(I_0=I-Q^-\).  Contract every connected component of \(I_0\), retaining
loops, and let \(H^-\) and \(H^+\) be the quotient multigraphs formed by the
old and new circuit incidences.

### Theorem 6.1 (graphic-rank merge criterion)

If \(I'=I-Q^-+Q^+\), then

\[
 \kappa(I)-\kappa(I')
   =r_{\rm gr}(I')-r_{\rm gr}(I)
   =r_{\rm gr}(H^+)-r_{\rm gr}(H^-).                     \tag{6.1}
\]

Consequently \(Q\) simultaneously increases distinct cap coverage and
merges components exactly when

\[
                       \Delta_{\rm cap}(Q)>0,
 \qquad r_{\rm gr}(H^+)>r_{\rm gr}(H^-).                 \tag{6.2}
\]

#### Proof

Both incidence factors span the same vertex set, so graphic rank is
\(|V|-\kappa\).  Contracting the common edge set \(I_0\) preserves the rank
difference.  Theorem 2.1 identifies these incidence components with the
owner-factor components. \(\square\)

Formula (6.1), rather than the number of touched old components by itself,
is the proof-safe topology test.

## 7. The complete short-circuit faces

The containment graph (1.2) has no `C4`.  Its shortest circuits are simple
`C6`s.  Every simple `C6` has a rank-seven core:

\[
 C_i=S+a_i,\qquad T_i=S+a_i+a_{i+1}\quad(i\in\mathbb Z/3). \tag{7.1}
\]

The other Johnson-triangle type has all three lower vertices under one
rank-nine owner and therefore does not give a simple incidence cycle.
This is a two-shore incidence `C6`, not the four-resource-neutral Boolean
hex: it preserves lower and owner degrees and is deliberately allowed to
change rank-ten caps.

### Lemma 7.1 (the active `C6` cap and fusion identity)

Suppose the incidences \((C_i,T_i)\) are selected and mutable, while
\((C_i,T_{i-1})\) are unselected and mutable.  Let \(R_i\) be the other
selected owner at \(C_i\).  Then toggling the six incidences preserves every
lower and owner degree.  Its three old direct caps are pairwise distinct,
as are its three new direct caps.  If the three removed owner edges
\(R_iT_i\) lie on three distinct factor components, the toggle merges those
three components into one.

#### Proof

Degree preservation is the alternating-cycle identity.  Write
\(R_i=S+a_i+r_i\).  Activity forces \(r_i\) to avoid the other two petals:
one is the removed owner and one is the advertised unselected owner.  An
old cap is \(S+\{a_i,a_{i+1},r_i\}\).  Equality of two old caps would force
one exterior \(r_i\) to be the third petal, a contradiction; reversal gives
the new claim.  After removing one edge from each of three cycles, the new
cyclic endpoint pairing concatenates the three resulting paths into one
cycle. \(\square\)

For one rank-seven core there are ten possible first petals and at most two
selected continuations at each of the next two steps.  Every active directed
`C6` is counted by its three cyclic roots.  Hence the complete active
simple-`C6` face has the universal bound

\[
 \left\lfloor { {17\choose7}\,10\,2^2\over3}\right\rfloor
                         =259306.                          \tag{7.2}
\]

The opposite-incidence anti-join and protected-incidence rejection only
shrink this number.  Theorem 5.1 scores cap gain using three old/new values,
and Theorem 6.1 scores every component pattern.  Thus active `C6`s are the
first finite face to test for simultaneous cap gain and **three-to-one**
component fusion.  They can also realize a two-to-one fusion; the exact
condition is the port formula below, not component multiplicity alone.

### The complete simple-`C8` face

A simple alternating incidence `C8` touches four lower vertices.  The exact
classification has the star form

\[
 C_i=S+a_i,\quad |S|=7,                                 \tag{7.3}
\]

or the octahedral form

\[
 C_i=S+a_i+a_{i+1},\quad |S|=6,                         \tag{7.4}
\]

with four distinct cyclic petals.  In either form, the old selected owner
at \(C_i\) is \(T_i=C_i\cup C_{i+1}\), the new owner is
\(T_{i-1}\), and \(R_i\) is the retained selected owner.

### Lemma 7.2 (within-phase `C8` cap simplicity)

For an active simple `C8`, the four old caps
\(R_i\cup T_i\) are pairwise distinct, and the four new caps
\(R_i\cup T_{i-1}\) are pairwise distinct.

#### Proof

In the star case write \(R_i=S+a_i+r_i\).  Activity forces
\(r_i\notin\{a_{i-1},a_{i+1}\}\): one forbidden choice repeats the removed
incidence and the other makes the advertised added incidence already
selected.  An old cap is
\(S+\{a_i,a_{i+1},r_i\}\).  Equality for adjacent indices forces one of the
forbidden choices; equality for opposite indices would put four distinct
petals in a three-element set.  The new phase is the same argument with the
cyclic order reversed.

In the octahedral case write \(R_i=C_i+r_i\).  Activity forces \(r_i\) to
lie outside all four petals, since the two petals outside \(C_i\) are
exactly the removed and added choices.  An old cap consists of \(S\), three
consecutive petals, and this exterior \(r_i\).  Two such caps cannot agree:
their distinct three-petal parts would force an exterior \(r_i\) to be the
missing petal.  Again reversal proves the new statement. \(\square\)

Let \(O_Q,N_Q\) be the resulting four-element old and new cap sets.  Lemma
7.2 simplifies (5.4) to

\[
 \Delta_{\rm cap}(Q)=
 |\{U\in N_Q\setminus O_Q:\ell_I(U)=0\}|
 -|\{U\in O_Q\setminus N_Q:\ell_I(U)=1\}|.              \tag{7.5}
\]

Thus a missing new cap is a literal gain and an old cap costs coverage only
when the circuit removes its last global occurrence.  Internal cap
cardinality alone is not a score: both phases always contribute four
distinct local values.  In particular one `C8` gains at most four caps, so
an all-`C8` repair of the present `6,141` holes requires at least
\(\lceil6141/4\rceil=1536\) successful toggles, regardless of regeneration.

### Lemma 7.3 (exact cut-port involution formula)

For a length-\(2s\) incidence circuit, name the lower and owner ports of
the removed incidences \(c_i,t_i\).  The old and new incidence matchings on
the ports are

\[
 \rho=\prod_i(t_i\ c_i),\qquad
 \beta=\prod_i(c_i\ t_{i+1}),
\]

with the cyclic direction changed if the opposite phase is used.  Delete
the old incidences.  Every retained path pairs two ports; let \(\alpha\) be
the resulting fixed-point-free involution.  If \(c(\pi)\) denotes the
number of cycles of a permutation, including fixed points, then the numbers
of touched components before and after the toggle are exactly

\[
 k^-=\frac{c(\alpha\rho)}2,\qquad
 k^+=\frac{c(\alpha\beta)}2.                              \tag{7.6}
\]

In particular a `C6` can merge two components into one.  One literal port
certificate is

\[
\begin{aligned}
 \rho&=(t_0c_0)(t_1c_1)(t_2c_2),\\
 \beta&=(c_0t_1)(c_1t_2)(c_2t_0),\\
 \alpha&=(t_0c_0)(t_1t_2)(c_1c_2),
\end{aligned}
\qquad
 \frac{c(\alpha\rho)}2=2,
 \quad
 \frac{c(\alpha\beta)}2=1.                              \tag{7.6a}
\]

The same-shore pairs in \(\alpha\) are physically legal: an even retained
bipartite path has endpoints on the same shore.  They occur when two
removed incidences have opposite factor parity on one old component.

#### Proof

The retained paths form the matching \(\alpha\) on the port set.  Restoring
one phase adds the matching \(\rho\) or \(\beta\).  The union of two perfect
matchings is a disjoint union of alternating cycles.  Each such alternating
cycle gives two cycles of the product of the two involutions, so its number
of components is half the number of product cycles.  This proves (7.6).
Direct multiplication gives (7.6a). \(\square\)

When the three removed `C6` incidences lie on three distinct old
components, \(\alpha=\rho\), and (7.6) recovers the valid three-to-one
sufficient case of Lemma 7.1.  For a `C8`, the aligned `3+1` occurrence
order of
`MATH_THEOREM_A_K17_ACTIVE_31C8_SPARSE_TRANSITION_JOIN_AND_PREFERENCE_20260802.md`,
has \(k^-=2,k^+=1\).  Both statements are instances of the same formula.

### Theorem 7.4 (finite simultaneous-improvement theorem)

Generate every active simple `C8` in the frozen marker factor, reject a key
if any removed incidence belongs to a protected marker edge, and evaluate
(7.5) and (6.1).  This emits every protected simple-`C8` exchange which
simultaneously increases distinct rank-ten cap coverage and merges owner
components, exactly once.

Before any protection, cap, or topology filter, there are at most

\[
 388960\text{ star keys}+1361360\text{ octahedral keys}
       =\boxed{1750320}                                   \tag{7.7}
\]

at `k=17`.

#### Proof

The cited active-`C8` theorem proves that (7.3)--(7.4), with its transition
joins and opposite-incidence anti-join, enumerate all active simple `C8`s
once and prove (7.7) from incidence degree two alone.  Protection is exactly
avoidance of the forced removed incidences.  Lemma 7.2 and Theorem 5.1 give
the complete cap test, while Theorem 6.1 gives the complete topology test.
No other datum enters the declared finite face. \(\square\)

The theorem licenses reuse of the **generator and identities**, not reuse
of any old factor's census or verdict.  The marker factor needs its own
light catalogue/replay.  It also does not preserve residence, ranks 11--17,
or a compiler state.

## 8. What remains matroidal, and what does not

For a lower vertex \(C\), choosing its cap \(U=C+a+b\) chooses the unique
pair of owner incidences

\[
                   (C,C+a),\qquad(C,C+b).                 \tag{8.1}
\]

Introduce a pair variable \(p_{C,\{A,B\}}\) for every two owner supersets
of \(C\).  The exact upper-aware factor model is

\[
\begin{aligned}
 &\sum_{\{A,B\}}p_{C,\{A,B\}}=1 &&(C\in{\cal L}),\\
 &\sum_{C,\{A,B\}:T\in\{A,B\}}p_{C,\{A,B\}}=2
       &&(T\in{\cal M}),\\
 &y_U\le
   \sum_{C,\{A,B\}:A\cup B=U}p_{C,\{A,B\}},
       &&(U\in{\cal U}),                                \tag{8.2}
\end{aligned}
\]

with the protected pair variables fixed to one.  Maximizing
\(\sum_Uy_U\) is exactly maximum distinct-cap coverage.  Connectivity of
the owner factor is exactly the subtour family

\[
 \sum_{C,\{A,B\}:|\{A,B\}\cap S|=1}p_{C,\{A,B\}}\ge2
 \quad(\varnothing\ne S\subsetneq{\cal M}).              \tag{8.3}
\]

Equations (8.2)--(8.3) are an exact finite model, but not ordinary weighted
intersection of the two partition matroids in Section 3.

First, one cap indicator is not additive on incidence edges.  Fix four
possible owner extensions \(a,b,c,d\) of one \(C\).  Every affine pair
score \(f(x,y)=\alpha+w_x+w_y\) obeys the rectangle identity

\[
                         f(a,b)+f(c,d)=f(a,c)+f(b,d).
\]

The indicator of the cap \(C+a+b\) has values `1,0,0,0` on the four
pairs `ab,cd,ac,bd`, and violates this identity.  Thus no linear
incidence-edge weight, even with a lower-vertex constant, realizes one
cap-coverage row.

Second, the natural owner-degree-at-most-two system on physical owner edges
is not a matroid.  Take three owners \(V_a=C+a,V_b=C+b,V_c=C+c\).  The
triangle on them is a feasible three-edge set saturating all three owners.
For each \(V_i\), choose two Johnson neighbours \(W_{i,1},W_{i,2}\), all six
distinct and outside the triangle; at `k=17` this is obtained by six
distinct swaps \(x_j\in C\) to the six coordinates outside
\(C\cup\{a,b,c\}\).  The six pendant edges form another degree-at-most-two
set.  None can be added to the three-edge triangle, violating matroid
augmentation.  This refutes the obvious partition-matroid treatment of the
pair variables; it does not claim that no larger extended formulation can
exist.

There is, however, an exact protected-witness face which stays matroidal.
Choose one current provider lower vertex for every cap that must be retained,
and force both of its incidences.  For a missing cap \(U\), choose one
\(C\subset U\) of rank eight and additionally force the unique pair (8.1).

### Theorem 8.1 (fixed-witness one-cap insertion)

For a fixed compatible witness bank and a fixed candidate \(C\subset U\),
there exists a palette-exact factor retaining every witness and covering
\(U\) if and only if the contracted demands satisfy (3.3).  Therefore a
lossless insertion of \(U\) exists on this fixed-witness face if and only if
at least one of its `45` rank-eight facets passes that cut test.

#### Proof

The forced provider pairs preserve their advertised caps.  The pair (8.1)
provides \(U\).  After contracting all forced incidences, nothing remains
except the protected bipartite degree-completion problem of Theorem 3.1.
There are \({10\choose2}=45\) possible rank-eight \(C\subset U\). \(\square\)

This is a sufficient lossless cap-insertion theorem with an exact min--max,
not a necessary theorem for unrestricted cap improvement: a successful
exchange may move the chosen witnesses themselves.

## 9. Exact boundary

The following statements are proved here.

* Protected owner/q1 factors form one alternating-circuit-connected
  bipartite \(b\)-factor fibre.
* Cap and component deltas of a proposed circuit are local and exact.
* The active simple-`C8` join is a complete finite face for simultaneous
  cap improvement and component merger, with the universal bound (7.7).
* A fixed cap-witness bank plus one desired cap reduces exactly to the Hall
  cuts (3.3).

The note does **not** prove that the frozen marker factor has a circuit with
both positive deltas, that all `6,141` cap holes can be repaired, or that
the resulting factor is connected.  It does not address source/buffer
binding, residence, ranks 11--17, or common-cap/compiler feasibility.  The
separately running upper-aware Boolean-diamond solve is neither duplicated
nor used as evidence.

## 10. Frozen provenance

The finite input data used only for (1.1) have the following SHA-256 values:

```text
0eab1f3cb25d0704e86e614850b95dec7a14e5b3c12b69254e2a90b2af0bf09e  marker58_q1_factor.tsv
6e1598c481ff41cde4fc99159acf0737bd30ba9585c4261fe213fff2b29060c6  marker58_q1_factor.audit.json
518a96832053a78595ae8284d4b27b2a90e266876968ff18e07b5247e3491b5d  marker58_q1_factor.independent_ad.audit.json
7afd27dc3489b20654216642b45ab84bbd0ce69ac95cee98fb4bed495db9786a  marker58_q1_upper_core.independent.audit.json
```

All files are under
`scratch/k17_marker58_q1_extension_20260802/`.  Theorems 2.1--8.1 are
symbolic and do not depend on a solver transcript.
