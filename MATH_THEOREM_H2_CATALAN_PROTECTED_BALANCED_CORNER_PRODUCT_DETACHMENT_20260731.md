# Protected balanced corners in product SCDs

Date: 2026-07-31  
Status: exact product-intrusion identity and all-\(a\ge2\) protected-SCD
construction; protected CLM positive at \(a=3,4\), negative at \(a=1,2\);
no all-\(a\) CLM or integral collar braid

## 0. Verdict

Fix \(A\in\binom{C}{a}\), \(|C|=2a\), and product an SCD of \(B_C\) with
one of \(B_R\), \(|R|=2b\). Making \(\{A\}\) a singleton collar chain
protects only the on-chain middle role. The exact condition protecting the
opposite role is

\[
 \boxed{A\text{ is isolated in the collar central graph.}}
 \tag{0.1}
\]

If an edge incident with \(A\) is owned by a radius-\(\rho\) collar chain,
it creates exactly

\[
 Q_b(\rho)=\binom{2b}{b}-\binom{2b}{b-\rho}
 \tag{0.2}
\]

product edges entering the child middle sector. Thus (0.1) is necessary and
sufficient for detaching the exact child central graph.

Protected SCDs exist for every \(a\ge2\), by products of explicit protected
\(B_4\) and \(B_6\) bases; \(a=1\) is impossible. The stronger protected
Catalan linear matching (CLM) is impossible for \(a=1,2\), exists for
\(a=3,4\), and is open for every \(a\ge5\).

Protection is not an integral collar braid. The protected \(B_6\)
path-forest SCD times the ordinary \(B_2\) SCD has zero child crossing but
three degree-three central vertices.

All statements are central, on ranks \(m-1,m,m+1\). Residence, deeper
shadows, sockets, voltage, and the common-cap compiler are separate.

## 1. Exact product intrusion

For a positive-radius collar chain \(D\), write its central flag and
opposite middle corner as

\[
 L_D<T_D<U_D,\qquad H_D=L_D\cup(U_D\setminus T_D),
 \tag{1.1}
\]

put \(e_D=\{T_D,H_D\}\), and let

\[
 \rho(D)=a-|\min D|.
 \tag{1.2}
\]

If \(\{A\}\) is a singleton chain, then \(A\) owns no central edge and

\[
 d_{J_C}(A)=|\{D:H_D=A\}|.
 \tag{1.3}
\]

Call \(A\) protected when it is a singleton and (1.3) is zero. This is
strictly stronger than the singleton condition of
MATH_THEOREM_CATALAN_BALANCED_SUBCUBE_PRODUCT_SCD_OUTER_COMPLETION_20260731.md:
that theorem excludes child traces among nonchild on-chain owners, while
protection also excludes them among opposite corners.

Let

\[
 {\cal X}_A=\{A\cup X:X\in\binom{R}{b}\},
 \tag{1.4}
\]

and let \(I_A\) count product central edges with exactly one endpoint in
\({\cal X}_A\).

### Theorem 1.1 (radius-weighted intrusion identity)

For \(b\ge1\),

\[
 \boxed{
 I_A=\sum_{D:e_D\ni A}Q_b(\rho(D)),\qquad
 Q_b(r)=\binom{2b}{b}-\binom{2b}{b-r}.}
 \tag{1.5}
\]

The second binomial is zero when \(b-r<0\). Hence \(I_A=0\) if and only if
\(A\) is protected.

### Proof

Pair collar chain \(c_0<\cdots<c_{2\rho}\) with core chain
\(d_0<\cdots<d_{2s}\).

If \(\rho<s\), every central product triple moves in the core factor. A
non-singleton collar chain does not contain \(A\), while the singleton box
has both edge endpoints in (1.4). If \(\rho=s>0\), the central triple is
at the grid bend. An endpoint in (1.4) would put \(A\) inside a
positive-radius collar chain. Equal zero radii give no edge.

Suppose \(\rho>s\). After the harmless abstract factor swap in the product
formula, product child \(h\in\{0,\ldots,2s\}\) has central collar index

\[
 j=s+\rho-h.
 \tag{1.6}
\]

An opposite collar corner can equal the rank-\(a\) set \(A\) only when
\(j=\rho\), or \(h=s\). That unique child uses precisely the collar edge
\(e_D\). Thus an incident radius-\(\rho\) edge contributes once for every
core chain of radius \(s<\rho\).

Every SCD of \(B_{2b}\) has

\[
 \binom{2b}{b-s}-\binom{2b}{b-s-1}
 \tag{1.7}
\]

radius-\(s\) chains. Summing (1.7) for \(s<\rho\) telescopes to
\(Q_b(\rho)\). Distinct boxes give distinct flags, and
\(Q_b(\rho)\ge Q_b(1)=\operatorname{Cat}_b>0\). \(\square\)

### Corollary 1.2 (detachable child)

For protected \(A\),

\[
 J_{C\times R}=J_R[A]\ \dot\cup\ J_{\rm comp},
 \tag{1.8}
\]

where \(J_R[A]\) is the literal child central graph. Child lower and upper
colours are matched internally; all other lower and upper colours are
matched in the complement.

If the whole product central graph is also a linear forest, endpoint
rerooting separately on the components in (1.8) gives an integral central
four-resource complement braid, including both outer trace collars, without
using child middle resources.

### Proof

The singleton product boxes are exactly the child chains. Theorem 1.1
excludes every other edge from their middle sector. Outer separation is the
product-SCD outer-completion theorem cited above. Components of a linear
forest remain linear forests, and endpoint rerooting makes both middle
roles injective. \(\square\)

The swapped-length grid formula in the cited audit is correct: it swaps the
abstract grid factors and then shifts the original core mask. The audit
below exercises both length orders.

## 2. Protected SCDs for all \(a\ge2\)

### Lemma 2.1 (bases)

The following \(B_4\) SCD protects \(A=12\):

\[
\begin{aligned}
 &\varnothing<1<13<134<1234,\\
 &2<24<234,\qquad3<23<123,\qquad4<14<124,\\
 &12,\qquad34.
\end{aligned}
\tag{2.1}
\]

Its central graph is the cycle

\[
 13-14-24-23-13
 \tag{2.2}
\]

plus isolates \(12,34\). It is protected but not a CLM.

The frozen \(B_6\) certificate protects \(A=000111\). It has chain-length
histogram \(1^5,3^9,5^5,7^1\), and its central graph is a five-path forest
of orders

\[
 13,3,2,1,1.
 \tag{2.3}
\]

Its twenty chains are recorded literally in
scratch/catalan_protected_balanced_corner_smallcases_20260731.audit.json.

### Lemma 2.2 (product closure)

If SCDs protect \(A_1,A_2\), their boundary-peeling product protects
\(A_1\cup A_2\).

### Proof

The singleton chains product to \(\{A_1\cup A_2\}\). With unequal factor
radii, the central diamond moves only in the larger factor; hitting
\(A_1\cup A_2\) would make that factor edge hit its protected set. With
equal positive radii, the diamond straddles the bend; hitting
\(A_1\cup A_2\) would put each \(A_i\) in a positive-radius factor chain.
Both are impossible. Equal zero radii give no edge. \(\square\)

### Theorem 2.3 (protected-SCD existence)

A protected SCD exists for every \(a\ge2\), and none exists for \(a=1\).

### Proof

The unique \(B_2\) central edge hits both middle sets. Lemma 2.1 supplies
parameters two and three. Every integer at least two is a sum of twos and
threes, so Lemma 2.2 gives the general construction. Coordinate transitivity
moves the protected set to any prescribed \(A\in\binom{[2a]}a\).
\(\square\)

This is not a CLM induction: the \(B_4\) base contains (2.2), and even
products of path-forest bases may branch.

## 3. Protected CLMs and the braid obstruction

A protected CLM is a perfect lower/upper diamond matching whose Johnson
lift is a spanning linear forest and in which \(A\) is isolated.

### Proposition 3.1 (exact bottom status)

For fixed \(A\), exhaustive protected-CLM counts are

\[
\begin{array}{c|ccc}
a&1&2&3\\ \hline
\#&0&0&18444.
\end{array}
\tag{3.1}
\]

At \(a=4\), a separate literal fixture has 56 diamond edges, exact outer
palettes, maximum degree two, no cycle, and 14 paths of orders

\[
 1,2,2,2,2,3,3,3,3,4,4,4,8,29.
 \tag{3.2}
\]

It protects \(A=00001111\).

The \(a=1\) zero is immediate. At \(a=2\), represent a perfect outer
matching by the derangement \(\pi\in S_4\) matching lower singleton \(i\)
to the upper triple omitting \(\pi(i)\). Protecting a two-set \(A\) forces
\(\pi(A)=A\) and \(\pi(A^c)=A^c\), hence two within-block transpositions.
The central graph is (2.2) plus \(A,A^c\), so it is cyclic.

Therefore a protected CLM does not exist for every \(a\). Existence for
every \(a\ge5\) is open.

### Proposition 3.2 (separation is not a braid)

Product the protected \(B_6\) path-forest SCD with the ordinary \(B_2\)
SCD. The child sector has no crossing edge, but the rank-four central degree
profile is

\[
 1^{31},\qquad2^{36},\qquad3^3.
 \tag{3.3}
\]

The degree-three vertices in the frozen labelling are

    01001110  01010101  01100101

Thus

\[
 \text{protected collar CLM + child CLM}
 \not\Longrightarrow \text{product CLM}.
 \tag{3.4}
\]

## 4. Relation to independent-boundary absorbers

Protection is a deterministic zero-crossing condition: it freezes one
recursive child and removes every opposite-middle collision with it.
Independent-boundary absorbers instead supply switchable endpoint pairs and
must choose disjoint interiors matching an admissible leave.

Identity (1.5) quantifies the bridge. An unprotected radius-\(\rho\) edge
creates \(Q_b(\rho)\) rigid child-middle intrusions that an absorber repair
must reroute. Protection empties this boundary bank but supplies neither an
independently selectable diamond menu nor a bounded-degree leave template.
Proposition 3.2 shows why it cannot replace reserve packing.

The weakest exact product target is:

1. a protected collar singleton for child detachment;
2. a whole product central graph that is a linear forest for the integral
   central complement braid; and
3. separate leave, residence, shadow, socket, and compiler conditions.

Only item 1 is constructed for every collar parameter.

## 5. Audit and scope

The independent audit

    scratch/audit_h2_catalan_protected_balanced_corner_product_20260731.py

authenticates the exhaustive \(a=1,2,3\) census, verifies the \(B_4,B_6\)
bases, constructs protected products for \(a=2,\ldots,8\), checks (1.5)
in fifteen product cases using both chain-length orders, and replays the
three degree-three vertices of Proposition 3.2.

Companion exact artifacts are:

    scratch/audit_catalan_protected_balanced_corner_smallcases_20260731.py
    scratch/catalan_protected_balanced_corner_smallcases_20260731.audit.json
    scratch/audit_catalan_protected_a4_clm_fixture_20260731.py
    scratch/catalan_protected_a4_clm_fixture_20260731.audit.json

No protected CLM for every \(a\ge5\), integral collar braid from isolation
alone, or full contiguous-OR construction is claimed.
