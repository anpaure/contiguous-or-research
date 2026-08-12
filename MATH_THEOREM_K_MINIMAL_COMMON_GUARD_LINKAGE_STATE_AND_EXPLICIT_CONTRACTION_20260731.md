# Minimal common-guard linkage state and explicit compiler contraction

Date: 2026-07-31  
Lane: K, common-cap/compiler  
Status: exact relational theorem and quantitative conditional contraction;
uniform Boolean/Pascal bank supply remains open

## 0. Main result

Assume a child chronology has already passed literal replay, residence,
every declared upper-shadow test, sockets, and prepins.  Fix one literal
guard word \(Q\), and let \(H_Q\) be its common-cap-safe target--cell graph.
Transport a partial matching into \(H_Q\).  Let \(U\) be the exposed target
sources, let \(F\) be the free cell sinks, and orient the alternating graph
in the usual way.

There are three exact levels of exported state.

1. For one already specified source set \(U\), the single number
   \(r(U)\), the maximum number of disjoint augmenting paths from \(U\) to
   \(F\), is sufficient and necessary.
2. If a future context may expose any subset of a fixed boundary source
   bank \(B\), the coarsest exact relational state is the strict-gammoid
   rank function
   \[
                   r(A)\qquad(A\subseteq B).
   \tag{0.1}
   \]
3. If both entry and exit terminals may vary under later gluing, one must
   export the pairing-resolved disjoint-linkage relation.  A fixed-sink
   gammoid rank is then insufficient.

If inheritance exposes at most

\[
                         |U|\le\lambda V+b_0
\tag{0.2}
\]

sources from an old compiler defect \(V\), and a commonly guarded bank
satisfies

\[
                         r(A)\ge\eta|A|-\gamma
 \qquad(A\subseteq U),                                \tag{0.3}
\]

then the new defect obeys

\[
 V'\le (1-\eta)(\lambda V+b_0)+\gamma
     =\rho V+\beta,                                   \tag{0.4}
\]

with the explicit constants

\[
 \boxed{\rho=(1-\eta)\lambda,\qquad
        \beta=(1-\eta)b_0+\gamma.}                    \tag{0.5}
\]

Thus strict contraction is exactly the numerical condition

\[
                         (1-\eta)\lambda<1.           \tag{0.6}
\]

For \(\lambda\ge1\), this says

\[
                         \eta>1-\lambda^{-1}.         \tag{0.7}
\]

This is the smallest exact common-cap boundary relation on the fixed-sink
face and the requested quantitative regenerative invariant.  It is
conditional on common-guard alternating-linkage supply; bounded switch
support alone does not imply (0.3).

## 1. Alternating compiler graph

Let \(H=(L,R;E)\) be one fixed common-guard graph.  Every edge of \(H\) is
simultaneously realized by the same literal guard word, so every matching
in \(H\) is a partial literal compiler.

Let \(M_0\subseteq E\) be a transported partial matching.  Put

\[
 U=L\setminus V(M_0),\qquad F=R\setminus V(M_0).
\tag{1.1}
\]

Orient

\[
 E\setminus M_0:L\longrightarrow R,
 \qquad
 M_0:R\longrightarrow L.                             \tag{1.2}
\]

For \(A\subseteq U\), let

\[
 r(A)=\max\{|\mathcal P|:
   \mathcal P\text{ is a family of vertex-disjoint directed paths
   from distinct vertices of }A\text{ to }F\}.         \tag{1.3}
\]

The linkable subsets of \(U\) form the strict gammoid presented by the
vertex-split version of this digraph; \(r\) is its rank function.

### Lemma 1.1 (defect from one rank value)

If \(u=|U|\), then the final Hall defect is

\[
                              V'=u-r(U).               \tag{1.4}
\]

#### Proof

The directed paths are precisely vertex-disjoint \(M_0\)-augmenting paths.
Symmetric difference with a maximum matching proves that their maximum
number is \(\nu(H)-|M_0|\).  Therefore

\[
 |L|-\nu(H)
 =(|L|-|M_0|)-(\nu(H)-|M_0|)
 =u-r(U).
\]

\(\square\)

For a single final instance, only \(r(U)\) is needed.  The larger rank table
is required because recursion does not know in advance which boundary
subset a later physical exchange will expose.

## 2. Coarsest state on the fixed-sink face

Fix a boundary source set \(B\) and the free sink bank \(F\).  A
**selection context** chooses a subset \(A\subseteq B\) to expose and adds
no other interior route.  Two guarded interiors are selection-equivalent
when every such context produces the same maximum repair count.

### Theorem 2.1 (fixed-sink minimality)

Two guarded interiors are selection-equivalent if and only if their rank
functions \(r(A)\), \(A\subseteq B\), agree.  Consequently every exact
exported state for all selection contexts must determine the entire rank
function, and the rank function itself is sufficient.

#### Proof

If the rank functions agree, the maximum repair count in the context
exposing \(A\) is \(r(A)\) in both interiors.

Conversely, if the rank functions differ, choose a set \(A\) on which they
differ and expose exactly \(A\).  That selection context obtains different
maximum repair counts, so the interiors are distinguishable.  \(\square\)

This is a coarseness statement about exact context behavior, not a lower
bound on bit encoding.  Gammoid identities or a compact network
representation may encode the table more economically.

### Why fixed-sink rank is not enough for arbitrary gluing

Suppose a block has entry terminals \(a,b\) and exit terminals \(c,d\).
One interior has disjoint paths \(a\to c,b\to d\); another has
\(a\to d,b\to c\).  With the undifferentiated fixed sink bank
\(\{c,d\}\), the two source rank functions agree.  A context retaining only
exit \(c\) distinguishes them.

For variable entry and exit sets, define

\[
 \Lambda(A,C,\pi)=1
\]

when the block contains pairwise vertex-disjoint directed paths realizing
the partial bijection \(\pi:A\to C\).  The set of all such triples is the
pairing-resolved linkage relation.

### Theorem 2.2 (variable-boundary minimality)

The pairing-resolved linkage relation is sufficient for exact tree-like
composition of guarded blocks.  Under contexts allowed to demand any
boundary pairing, every exact exported state must determine this relation.

#### Proof

Restriction of a global disjoint linkage to a block produces one recorded
partial pairing.  Compatible child pairings glue uniquely; rejecting reused
boundary vertices and wrong orientations, and discarding any closed
internal cycle (equivalently choosing the subpattern without it), gives
exact composition.

If two blocks differ on a partial pairing \(\pi\), attach disjoint exterior
private paths which accept precisely the endpoints and pairings prescribed
by \(\pi\).  The block realizing \(\pi\) completes those routes, while the
other does not.  Hence any exact state for all such contexts must
distinguish them.  \(\square\)

When outside matching only asks for an unpaired source set against one fixed
sink bank, Theorem 2.1 is the genuinely smaller state and should be used.

## 3. A source-to-port bank and Rado's formula

Often one does not expose a source directly in the global alternating
network.  Instead, each source \(u\in U\) has an allowed menu \(P_u\) of
entry ports.  Let \(\mathcal M\) be the strict gammoid on the union of those
ports, with rank \(r_{\mathcal M}\) given by disjoint linkage to the fixed
free sink bank.  Local source-to-port spokes are required to be
source-private; all global vertex conflicts are included in
\(\mathcal M\).

### Theorem 3.1 (exact partial Rado linkage)

The maximum number \(q\) of exposed sources which can choose distinct
representative ports and link disjointly to the sink bank is

\[
 q=\min_{X\subseteq U}
 \left(
 |U|-|X|+
 r_{\mathcal M}\!\left(\bigcup_{u\in X}P_u\right)
 \right).
\tag{3.1}
\]

Consequently the exact residual target defect of this bank is

\[
 |U|-q
 =\max_{X\subseteq U}
 \left(
 |X|-
 r_{\mathcal M}\!\left(\bigcup_{u\in X}P_u\right)
 \right).
\tag{3.1a}
\]

Thus residual defect at most \(D\) is equivalent to the weakest cut system

\[
 r_{\mathcal M}\!\left(\bigcup_{u\in X}P_u\right)
 \ge |X|-D
 \qquad(X\subseteq U).
\tag{3.1b}
\]

If the guard itself is not fixed, the exact quantifier order is
\(\exists Q\,\forall X\); choosing a different guard for each cut or
uniting several guarded graphs is invalid.

In particular, if

\[
 r_{\mathcal M}\!\left(\bigcup_{u\in X}P_u\right)
 \ge\eta|X|-\gamma
 \qquad(X\subseteq U),                                \tag{3.2}
\]

then

\[
                              q\ge\eta|U|-\gamma.       \tag{3.3}
\]

#### Proof

Formula (3.1) is the deficient form of Rado's independent-transversal
theorem.  It can also be obtained by adding one source vertex with arcs to
its menu and applying vertex-capacitated max-flow/min-cut.

Substitute (3.2) into (3.1):

\[
 q\ge\min_X\bigl(|U|-(1-\eta)|X|-\gamma\bigr)
   =\eta|U|-\gamma,
\]

because \(0\le\eta\le1\) and the minimum occurs at \(X=U\).
\(\square\)

For singleton menus \(P_u=\{u\}\), this is the rank condition (0.3).
For an orthogonal actuator bank, the gammoid reduces further to ordinary
Hall on source--actuator choices.  The gammoid statement is strictly more
general because it permits globally long alternating reroutes.

## 4. The sharp contraction-pressure summary

The full rank function is needed for exact arbitrary future contexts.  For
one desired repair fraction \(\eta\), it has a canonical scalar summary:

\[
 \Gamma_\eta(D,B,F)
   =\max_{A\subseteq B}\bigl(\eta|A|-r(A)\bigr),
 \qquad 0\le\eta\le1.                                 \tag{4.1}
\]

Thus

\[
 \Gamma_\eta\le\gamma
 \quad\Longleftrightarrow\quad
 r(A)\ge\eta|A|-\gamma
 \quad(A\subseteq B).                                 \tag{4.2}
\]

Unlike raw scalar Hall defect, \(\Gamma_\eta\) is hereditary over every
boundary subset.

Use the vertex-split unit-capacity network presenting the strict gammoid.
For a vertex set \(P\) on the source side of a cut, let
\(\operatorname{cap}(P)\) be the internal cut capacity separating the
boundary sources in \(P\) from the fixed sink bank.  The source arcs have
unit capacity.

### Theorem 4.1 (exact min-cut form)

\[
 \boxed{
 \Gamma_\eta
 =\max_P\bigl(
       \eta|B\cap P|-\operatorname{cap}(P)
       \bigr).}
\tag{4.3}
\]

#### Proof

Max-flow/min-cut with a unit arc from a supersource to each \(a\in A\)
gives

\[
 r(A)=\min_P
 \bigl(|A\setminus P|+\operatorname{cap}(P)\bigr).
\]

Therefore

\[
\begin{aligned}
 \Gamma_\eta
 &=\max_{A,P}
 \bigl(\eta|A|-|A\setminus P|-\operatorname{cap}(P)\bigr).
\end{aligned}
\]

For fixed \(P\), a source in \(P\) contributes \(\eta\), while a source
outside \(P\) contributes \(\eta-1\le0\).  The maximizing choice is
\(A=B\cap P\), with arbitrary indifferent outside sources only when
\(\eta=1\).  This proves (4.3).  \(\square\)

### Corollary 4.2 (bounded-perturbation stability)

Deleting \(q\) unit-capacity vertices/arcs from a protected common-guard
bank increases \(\Gamma_\eta\) by at most \(q\); adding resources cannot
increase it:

\[
                         \Gamma'_\eta\le\Gamma_\eta+q.
\tag{4.4}
\]

#### Proof

Every cut capacity decreases by at most \(q\).  Apply (4.3).  \(\square\)

This is the sharp stable scalar invariant requested for contraction.  It is
not an exact substitute for the full rank function when later gluing must
distinguish source subsets or pairings.

## 5. Explicit regenerative constants

Let \(V\) be the old exact common-cap defect.  After Pascal inheritance,
physical transport, target births, and deletion of invalidated old matched
cells, suppose the transported partial compiler exposes \(u\) sources with

\[
                              u\le\lambda V+b_0.        \tag{5.1}
\]

All terms in \(b_0\) are literal: boundary births, bounded halo casualties,
and other declared additive exposure.  The coefficient \(\lambda\) is the
maximum multiplicity with which an old exposed target can generate child
sources before repair.

Assume one final common guard exists and its alternating bank satisfies
(0.3), equivalently \(\Gamma_\eta\le\gamma\).  Lemma 1.1 gives

\[
\begin{aligned}
 V'
   &=u-r(U)\\
   &\le(1-\eta)u+\gamma\\
   &\le(1-\eta)\lambda V+(1-\eta)b_0+\gamma.
\end{aligned}
\tag{5.2}
\]

This proves (0.4)--(0.5).

### Corollary 5.1 (bounded-halo specialization)

If inheritance creates no multiplicative branching and at most \(b_0\)
extra exposed sources, then \(\lambda=1\) and

\[
 \rho=1-\eta,\qquad
 \beta=(1-\eta)b_0+\gamma.                            \tag{5.3}
\]

Any fixed \(\eta>0\) contracts the inherited defect.

### Corollary 5.2 (relative halo loss)

If an interior batch invalidates at most

\[
                         \ell\le\alpha V+\ell_0
\tag{5.4}
\]

old matched cells and creates at most \(b\) newly residual targets, then
\(\lambda=1+\alpha\), \(b_0=\ell_0+b\), and

\[
 \rho=(1-\eta)(1+\alpha),\qquad
 \beta=(1-\eta)(\ell_0+b)+\gamma.                     \tag{5.5}
\]

Strict contraction requires

\[
                         \eta>\frac{\alpha}{1+\alpha}. \tag{5.6}
\]

### Corollary 5.3 (uniform additive constant)

If \(\rho<1\), put

\[
 E=\max\left\{V_0,\frac{\beta}{1-\rho}\right\}.        \tag{5.7}
\]

Then every reachable compiler defect is at most \(E\).  On a physically
accepted length-\(B(k)+c\) scaffold, append its unmatched target masks.
The compiler contribution to the terminal word is at most
\(\lceil E\rceil\), giving

\[
                         \nu(k)\le B(k)+c+\lceil E\rceil
\tag{5.8}
\]

when all noncompiler target rows are exact.  Separately bounded terminal
middle/upper charges are added once, not inherited automatically.

### Corollary 5.4 (typed self-healing bank)

Split the exposed source set into inherited sources \(U_0\), with
\(|U_0|\le V\), and sources \(U_1\) newly exposed by the physical exchange,
with

\[
                         |U_1|\le\alpha V+b_0.
\tag{5.9}
\]

Suppose one common guard satisfies the typed hereditary rank inequality

\[
 r(A)\ge
 \eta_0|A\cap U_0|+\eta_1|A\cap U_1|-\gamma
 \qquad(A\subseteq U_0\cup U_1).
\tag{5.10}
\]

Then

\[
 V'\le
 \left((1-\eta_0)+(1-\eta_1)\alpha\right)V
 (1-\eta_1)b_0+\gamma.
\tag{5.11}
\]

Hence

\[
 \rho=(1-\eta_0)+(1-\eta_1)\alpha,\qquad
 \beta=(1-\eta_1)b_0+\gamma.
\tag{5.12}
\]

In particular, a bank which exactly self-heals all newly created halo
sources (\(\eta_1=1\)) and repairs an \(\eta_0\)-fraction of inherited Hall
sources has

\[
                         \rho=1-\eta_0,\qquad
                         \beta=\gamma.
\tag{5.13}
\]

This typed form is the cleanest target for guarded switch monoids: local
damage is absorbed completely, while a distributed bank performs the
genuine global contraction.

## 6. Necessity of an extensive or reset bank

If a physical exchange introduces at most \(h\) new or
neighborhood-changed cell columns on a reversible common-guard face, it can
increase matching rank by at most \(h\).  Hence

\[
                              V'\ge V-h.               \tag{6.1}
\]

Combining (5.1) with \(V'\le\rho V+\beta\) gives

\[
                              h\ge(1-\rho)V-\beta.      \tag{6.2}
\]

Thus a fixed-support atom cannot provide a uniform positive repair fraction
for unbounded \(V\).  A valid construction must use one of:

1. an extensive parallel bank with \(\Omega(V)\) independent linkage rank;
2. a global quotient/orbit flow whose lift supplies that rank; or
3. a reset leaving only \(O(1)\) exceptional sources.

This is a theorem about matching rank.  It does not forbid a long
augmenting path triggered by one local change from repairing one unit.

## 7. Guard requirement and exact scope

All paths in Sections 1--4 lie in one final \(H_Q\).  This is what makes
their simultaneous symmetric-difference matching a literal compiler.
Running the same linkage calculation in the marginal graph is unsound:
different paths may require incompatible cap letters, and a pairwise-legal
collection may complete a forbidden triple.

When no common guard has yet been fixed, the exported relation must include
the feasible guard assignment together with the linkage signature.  Rank
at most three of the fixed-socket obstruction clutter does not make the
unguarded relation a gammoid and does not bound LLL dependency.

The current K17 OPTIMAL28 zipper is outside the hypothesis.  Its replay and
ranks 10--12 fail before \(H_Q\) exists.  The theorem becomes applicable
only to a fully replayed, upper-certified complement rethread.

## 8. Exact remaining all-dimensional lemma

The common-cap part of a \(B(k)+O(1)\) proof is reduced to:

> After every accepted Pascal/RSB physical transition, construct one common
> guard and an alternating linkage bank with exposure inheritance
> \(u\le\lambda V+b_0\) and hereditary rank
> \(r(A)\ge\eta|A|-\gamma\), where
> \((1-\eta)\lambda<1\) and \(b_0,\gamma\) are absolute.

The exported fixed-sink state is exactly the strict-gammoid rank function
on the live boundary sources.  If the recursive glue varies exits or
requires path pairings, replace it by the pairing-resolved linkage
relation.  No scalar slack or bounded-support claim remains in this gate.
