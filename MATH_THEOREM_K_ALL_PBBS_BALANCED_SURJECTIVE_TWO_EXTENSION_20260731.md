# PBBS gives balanced surjective two-extensions in every odd dimension

Date: 2026-07-31.

Status: unconditional theorem, obtained by complementing the independently
audited centered-PBBS factor. It closes the bare depth-one extension problem.
It does not supply residence, deeper decks, boundedly many components, or a
lossless opening.

## 1. Closed-form construction

Put

\[
 n=2m+1,\qquad
 \mathcal L=\binom{[n]}m,\qquad
 \mathcal M=\binom{[n]}{m+1},\qquad
 \mathcal U=\binom{[n]}{m+2}.
\]

For \(C\in\mathcal L\), let \(z_+(C)\) and \(z_-(C)\) be the surviving
zeros in the forward cyclic 10 matching and reverse cyclic 01 matching.
Define

\[
 F(C)=\{z_+(C),z_-(C)\},\qquad
 \Sigma(C)=C\cup F(C).                                  \tag{1.1}
\]

### Theorem 1.1

For every \(m\ge1\), the two entries of \(F(C)\) are distinct and:

\[
 \#\{a\in T:a\in F(T\setminus\{a\})\}=2
       \qquad(T\in\mathcal M),                           \tag{1.2}
\]

while

\[
 1\le |\Sigma^{-1}(U)|\le3
       \qquad(U\in\mathcal U).                           \tag{1.3}
\]

Thus \(F\) is a balanced surjective two-extension map. Equivalently,

\[
 \bigl\{\{C+z_+(C),C+z_-(C)\}:C\in\mathcal L\bigr\}      \tag{1.4}
\]

is a spanning Johnson 2-factor on \(\mathcal M\), uses every lower
rank-\(m\) colour exactly once, and covers every upper rank-\((m+2)\)
colour with load at most three. The construction is cyclic-equivariant.
With the audited periodic-BBS site-homomesy theorem, the contracted Johnson
factor has at most \(\operatorname{Cat}_m\) components.

### Proof

Let \(p\) be the canonical cyclic-parenthesis/PBBS permutation on
\(\mathcal L\). Its forward and inverse formulae are

\[
 p(C)=C^c\setminus\{z_+(C)\},\qquad
 p^{-1}(C)=C^c\setminus\{z_-(C)\}.                       \tag{1.5}
\]

The audited centered-PBBS theorem says that

\[
 e_C=\{p^{-1}(C),p(C)\}                                  \tag{1.6}
\]

is a simple spanning 2-factor on the rank-\(m\) layer. Its union colour is
\(C^c\), once for each \(C\), and its intersection colour

\[
 \chi(C)=p^{-1}(C)\cap p(C)                              \tag{1.7}
\]

satisfies the PBBS angle bound

\[
 1\le\#\{C:\chi(C)=S\}\le3
       \qquad\left(S\in\binom{[n]}{m-1}\right).          \tag{1.8}
\]

Complement the endpoints of (1.6). By (1.5), they become

\[
 (p(C))^c=C+z_+(C),\qquad
 (p^{-1}(C))^c=C+z_-(C).                                \tag{1.9}
\]

They are distinct because the centered factor is simple. Complementation is
a vertex bijection, so (1.9) is again a spanning 2-factor. Its intersection
is

\[
 (p(C)\cup p^{-1}(C))^c=C,                              \tag{1.10}
\]

and its union is

\[
 (p(C)\cap p^{-1}(C))^c=\chi(C)^c=\Sigma(C).            \tag{1.11}
\]

Equation (1.10) proves exact lower colours and hence (1.2). Complementation
bijects the rank-\((m-1)\) and rank-\((m+2)\) layers, so (1.8) and (1.11)
prove (1.3). Cyclic matching commutes with rotation, proving equivariance.

For the component count, let the PBBS orbit lengths be
\(P_i=(2m+1)\ell_i\), as supplied by site homomesy. The contracted
step-two Johnson factor has \(\gcd(2,P_i)=\gcd(2,\ell_i)\) components on
orbit \(i\). Since \(\gcd(2,\ell_i)\le\ell_i\) and

\[
 \sum_i\ell_i=\frac{\binom{2m+1}m}{2m+1}
              =\operatorname{Cat}_m,
\]

the claimed sharp bound follows.
\(\square\)

Here “factor” means the contracted Johnson graph (1.4), with
\(|\mathcal M|=\binom{2m+1}{m+1}=W\) owner vertices. Subdividing every
Johnson edge by its unique lower colour produces the alternating
\(\mathcal L\)-\(\mathcal M\) incidence factor on \(2W\) vertices. It has
the same number of components and exactly twice each component length, so
the component bound is unchanged; one must not divide the \(2W\)-vertex
count by \(2m+1\) without also accounting for that doubling.

For \(m=1\), one may also verify the construction directly: each singleton
chooses the other two points and (1.4) is the triangle on rank two.

## 2. Consequences and scope

The bare balanced-surjective problem is therefore closed for every odd
\(n\), prime or composite. In particular, prime-only quotient search is not
needed for this gate. The current \(k=17\) factor is valuable because of its
additional decorations, not because depth-one existence was missing:

* PBBS already has upper load at most three (the current decorated \(k=17\)
  map has maximum load five);
* PBBS has \(O(W/k)\), rather than \(O(1)\), components;
* its short positive residence runs are not controlled;
* a protected opening and exact lower compiler are not supplied.

The PBBS input is actually stronger than the immediate-shadow statement:
it already supplies every correct-window shadow on both sides.

### Theorem 2.1 (all-depth PBBS flag support)

Orient a cycle of \(g=p^2\), write its consecutive rank-\(m\) states as
\((B_i)\), and put

\[
 T_i=p(B_i)^c=B_i\cup B_{i+1}.                         \tag{2.1}
\]

Then \((T_i)\) is a component of the rank-\((m+1)\) carrier and

\[
 T_i\cap T_{i+1}=B_{i+1}.                              \tag{2.2}
\]

Across all PBBS components, for every \(1\le q\le m\) and every
\(S\in\binom{[n]}{m-q}\), some directed \(q\)-edge PBBS path satisfies

\[
 \bigcap_{a=0}^{q}B_{i+a}=S.                            \tag{2.3}
\]

That same occurrence gives the lower carrier window

\[
 \bigcap_{a=-1}^{q}T_{i+a}=S,                           \tag{2.4}
\]

and, on the complementary component, the upper carrier window

\[
 \bigcup_{a=0}^{q}B_{i+a}^c=S^c.                        \tag{2.5}
\]

The two complementary correct-window loads agree occurrencewise and lie
between \(1\) and \(\binom{2q+1}{q}\).

#### Proof

Equation (2.1) follows because \(B_i\) and \(B_{i+1}=p^2(B_i)\) are the two
distinct \(m\)-subsets disjoint from \(p(B_i)\); (2.2) follows immediately.
The audited all-depth PBBS corridor theorem supplies (2.3). Intersecting
the adjacent identities (2.2) gives (2.4), while De Morgan's law gives
(2.5). The occurrence map is the same in both formulae, preserving the
load. \(\square\)

Consequently **all shadow-surjectivity constraints, at every depth, are
already unconditional for odd \(k\)**. The odd-\(k\) construction problem
reduces to precisely the following three compatible-decoration gates:

1. **Residence:** rethread or modify the factor so every positive coordinate
   run needed by the depth-\(d(k)\) erosion has length at least \(d(k)+1\).
2. **Protected opening:** cut and concatenate its at most
   \(\operatorname{Cat}_m\) components without losing more shadow witnesses
   than the available boundary/seam halo can absorb.
3. **Integral compiler:** choose one common depth-\(d(k)\) preimage word and
   an integral SDR for all lower targets.

Connectivity is not a fourth independent gate; it belongs to protected
opening. Nor is any further upper/lower coverage theorem needed before
residence: PBBS has already paid for the complete flag tower.

The cyclic action is free on \(\mathcal L\) and \(\mathcal M\). If a set were
fixed by a nonidentity rotation, it would be a union of rotation orbits of
some common length \(s>1\) dividing \(2m+1\), so \(s\) would divide its
cardinality. This contradicts
\(\gcd(2m+1,m)=\gcd(2m+1,m+1)=1\). Hence the quotient has exactly
\(\operatorname{Cat}_m\) lower and middle orbits even when \(2m+1\) is
composite. Upper orbits can have stabilizers; equivariant surjectivity does
not require them to be free.

Dependencies:

* MATH_AUDIT_PBBS_FIRST_SHADOW_THEOREM_20260726.md, Theorem 7.1 and
  angle bound (0.1);
* PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md, only for the optional
  component bound.
* THREAD_A_COMPOSITE_ODD_PBBS_TWO_MATCHING_SHADOW_FACTOR_20260729.md,
  Theorem 2.2, for the all-depth transport in Theorem 2.1.

## 3. Hexagons span the binary incidence cycle space

Let \(I(n,q)\) be the inclusion graph between ranks \(q\) and \(q+1\).
For \(S\in\binom{[n]}{q-1}\) and distinct \(a,b,c\notin S\), let
\(H(S;a,b,c)\) be the incidence hexagon

\[
 S+a,\ S+a+b,\ S+b,\ S+b+c,\ S+c,\ S+c+a,\ S+a.       \tag{3.1}
\]

### Theorem 3.1

The cycle space of \(I(n,q)\) over \(\mathbb F_2\) is generated by the
hexagons (3.1).

### Proof

The boundary cases \(q=0,n-1\) are stars. For \(1\le q\le n-2\), induct on
\(n\). Separate sets according to whether they contain the last point \(z\).
The graph is the union of \(I(n-1,q)\), \(I(n-1,q-1)\), and the matching

\[
 M_A:A\longleftrightarrow A+z,\qquad
 A\in\binom{[n-1]}q.                                    \tag{3.2}
\]

For a binary cycle \(Z\), let \(R\) be the set of \(A\)'s whose matching
edge \(M_A\) occurs in \(Z\). The set \(R\) has even size. Since
\(J(n-1,q)\) is connected, choose a binary \(T\)-join \(Q\) with odd-degree
set \(R\).

For every edge \(A=S+a,\ B=S+b\) of \(Q\), the hexagon \(H(S;a,b,z)\)
consists of \(M_A,M_B\), the two-edge \(A\)-to-\(B\) path in \(I(n-1,q)\),
and its counterpart in \(I(n-1,q-1)\). Add these hexagons to \(Z\).
Matching edge \(M_A\) changes with parity \(\deg_Q(A)\), so all matching
edges cancel. The remainder is a cycle in each smaller inclusion graph,
and induction finishes. \(\square\)

Therefore the symmetric difference of any two balanced factors is
algebraically a sum of incidence hexagons. This is not yet legal Markov
connectivity: the decomposition need not order the toggles so that every
intermediate hexagon is alternating selected/unselected. That nonnegative
plateau-connectivity problem is the real remaining hexagon gate.
