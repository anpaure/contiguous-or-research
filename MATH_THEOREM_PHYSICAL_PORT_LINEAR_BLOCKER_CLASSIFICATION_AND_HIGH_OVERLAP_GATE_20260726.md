# Physical ports: linear blockers are negligible and the exact high-overlap gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, solver, or web input is
used.

## 0. Outcome

Use the target-regular physical port hypergraph \(\mathcal H^\#\) of
`MATH_THEOREM_PHYSICAL_PORT_EKR_HIGH_COVER_REDUCTION_20260726.md`.  Put

\[
 D=D_1,
 \qquad
 K=\max_C|e_C^\#|=O(h\sqrt m+H)=m^{O(1)},          \tag{0.1}
\]

and retain the proved estimates

\[
 \Delta_2(\mathcal H^\#)\le(4+o(1))D/m             \tag{0.2}
\]

and, for \(v\notin e_E^\#\),

\[
 |\{C:v\in e_C^\#,\ e_C^\#\cap e_E^\#\ne\varnothing\}|
 \le2\widehat\rho_mD.                              \tag{0.3}
\]

This note gives four audited conclusions.

1. A literal high-cover physical linear space is impossible at the
   relevant scale.  If an intersecting strip family has target-cover
   number greater than \(s\) and every two strips share at most \(s\)
   selected targets, then

   \[
   \boxed{|\mathcal F|\le K^{s+1}.}                \tag{0.4}
   \]

   For \(s=1\), the sharp bound is \(K^2-K+1\).  Since

   \[
   \log D=(2h+o(h))\log m,                          \tag{0.5}
   \]

   (0.4) is \(o(D/m^A)\) for every fixed \(A\) whenever \(s=o(h)\).
   In particular it disposes of the entire high-cover threshold isolated
   in the preceding note, both at the default and optimized strip scales,
   **provided the family is genuinely linear or, more generally,
   \(s\)-linear**.

2. The physical cyclic pair kernel gives a uniform large-overlap bound.
   If

   \[
   \mathcal N_s(E)=
   \{C\ne E:|e_C^\#\cap e_E^\#|\ge s\},            \tag{0.6}
   \]

   then

   \[
   \boxed{
   |\mathcal N_s(E)|
   \le K^2\left[
     4hD\left({C\sqrt s\over m-H}\right)^{c\sqrt s}
     +C_1m\right].}                                \tag{0.7}
   \]

   Hence, for every \(s\to\infty\) with \(s=m^{\Omega(1)}\) and
   \(s=o(m)\),

   \[
   |\mathcal N_s(E)|=D\exp[-\Omega(\sqrt s\log(m/s))]
                    +D^{o(1)}.                     \tag{0.8}
   \]

3. There is an exact cover-number supersaturation inequality.  For a
   non-star intersecting family \(\mathcal F\), let \(J_s(\mathcal F)\)
   join two strips when they share more than \(s\) targets.  Then

   \[
   \boxed{
   e(J_s(\mathcal F))
   \ge {|\mathcal F|\over2}
       \left({|\mathcal F|\over A_s}-1\right),
   \qquad
   A_s=\max\{K^{s+1},\,2s\widehat\rho_mD\}.}      \tag{0.9}
   \]

   Thus a dangerous high-cover clique is forced to contain many
   genuinely repeated physical intersections.  At \(s=1\), a family of
   size \(cD/\sqrt m\) forces

   \[
   e(J_1)=
   \Omega\left({D\over m\widehat\rho_m}\right).    \tag{0.10}
   \]

   This is \(D/m^{1/6+o(1)}\) at the default scale and
   \(D/\operatorname{polylog}m\) at the optimized scale.

4. Every graph-like or pair-bundle physical blocker is harmless even for
   the full weighted fractional-colouring problem.  If the conflicts of a
   weighted support are represented by a loopless multigraph on target
   vertices, with every physical strip assigned to a contained target
   pair, then

   \[
   \boxed{\chi_f'\le D+2\Delta_2
          =D+O(D/m).}                              \tag{0.11}
   \]

   Thus neither a literal projective plane nor an odd graph blow-up made
   from physical target-pair bundles can obstruct
   \((1+o(m^{-1/2}))D\).

These results correct the terminology of the preceding reduction.  The
remaining object is not a linear-space blocker.  It would have to be a
**nonlinear high-overlap blocker**: an intrinsically rank-at-least-three,
weighted configuration whose repeated intersections cannot be resolved
by target pairs.

The note does not prove that no such object exists.  The exact surviving
inequality is stated in Section 6.  No physical counterexample to it is
constructed here.

## 1. The scale audit

The common nonmiddle target degree is

\[
 D={ (m+1)!(m-1)!\over2(m-h)!^2}.                  \tag{1.1}
\]

Since \(h=o(m)\), the two factorial quotients in (1.1) contain altogether
\(2h\) factors, each \(m(1+o(1))\).  Therefore

\[
 \log D=(2h+o(h))\log m.                            \tag{1.2}
\]

On the other hand \(K=m^{O(1)}\), so

\[
 K^{s+1}=\exp[O(s\log m)].                          \tag{1.3}
\]

Consequently

\[
 s=o(h)\quad\Longrightarrow\quad
 K^{s+1}=D^{o(1)}=o(D/m^A)                          \tag{1.4}
\]

for every fixed \(A\).

At the default scale \(h=m^{2/3+o(1)}\), the unresolved cover threshold
in the preceding note is \(m^{1/3-o(1)}=o(h)\).  At the optimized scale

\[
 h=\sqrt m\log m\,L_m,\qquad L_m=m^{o(1)},\quad L_m\to\infty,
\]

that threshold is at most

\[
 s_0={\sqrt m\over(\log m)L_m}m^{-o(1)}=o(h).       \tag{1.5}
\]

Thus the polynomial-versus-exponential separation in (1.4) has ample
room at precisely the alleged high-cover scale.

## 2. Bounded-overlap high-cover families

The following theorem is abstract, but its strength here comes from
(1.4).

### Theorem 2.1 (adaptive bounded-overlap theorem)

Let \(\mathcal F\) be an intersecting family of sets of size at most
\(K\).  Suppose

\[
 \tau(\mathcal F)>s,
 \qquad
 |E\cap F|\le s\quad(E\ne F\in\mathcal F).         \tag{2.1}
\]

Then

\[
                         |\mathcal F|\le K^{s+1}.   \tag{2.2}
\]

#### Proof

Run the adaptive witness tree of Proposition 4.1 in the preceding note to
depth \(s+1\).  At a node labelled by a target set \(A\), with
\(|A|\le s\), the cover inequality \(\tau(\mathcal F)>s\) supplies a
witness edge \(E_A\in\mathcal F\) disjoint from \(A\).  Partition the
current branch by one chosen target of its intersection with \(E_A\), and
append that target to \(A\).  Every level has branching factor at most
\(K\), so there are at most \(K^{s+1}\) leaves.

Every member of a leaf branch contains its leaf label, which has
\(s+1\) distinct targets.  Two different members of that branch would
therefore have intersection at least \(s+1\), contrary to (2.1).  Hence
each leaf branch has at most one member.  This proves (2.2). \(\square\)

### Corollary 2.2 (literal linear spaces)

If every two members of \(\mathcal F\) meet in exactly one target and
\(\tau(\mathcal F)>1\), then

\[
                         |\mathcal F|\le K^2-K+1.   \tag{2.3}
\]

In particular, every literal physical projective plane, at every cover
number and every possible order, has size \(D^{o(1)}\), and hence

\[
                         |\mathcal F|=o(D/\sqrt m). \tag{2.4}
\]

#### Proof

The sharper count is the standard one-line argument.  Fix
\(E_0\in\mathcal F\).  For every \(v\in E_0\), choose a member \(F_v\)
avoiding \(v\).  Distinct members of the \(v\)-pencil must meet \(F_v\)
in distinct targets, so that pencil has size at most \(K\).  The
\(|E_0|\le K\) pencils partition \(\mathcal F\setminus\{E_0\}\), after
removing \(E_0\) once from each, and give
\(|\mathcal F|-1\le K(K-1)\).  Now apply (1.4). \(\square\)

Corollary 2.2 is stronger than the multistar projective-plane exclusion in
the preceding note for a *literal* linear space.  The multistar argument
was needed only because a blow-up can make two physical strips share many
targets.  Such a blow-up is no longer linear.

## 3. Large physical intersections are rare around one strip

### Theorem 3.1 (large-overlap neighbourhood)

For every selected physical edge \(e_E^\#\) and every \(2\le s\le K\),
(0.7) holds.

#### Proof

Let \(C\in\mathcal N_s(E)\), and choose any \(s\) distinct common targets

\[
                         \mathcal A\subseteq e_C^\#\cap e_E^\#.
\]

These are raw band targets of the one physical strip \(E\).  Lemma 3.2
of the preceding note gives \(S,T\in\mathcal A\) with

\[
 |S\setminus T|+|T\setminus S|\ge c\sqrt s.        \tag{3.1}
\]

The selected pair estimate used in Lemma 3.3 there gives

\[
 d^\#(S,T)
 \le4hD\left({C\sqrt s\over m-H}\right)^{c\sqrt s}+C_1m.       \tag{3.2}
\]

There are fewer than \(K^2\) possible unordered pairs \(\{S,T\}\) in
\(e_E^\#\).  Every member of \(\mathcal N_s(E)\) contains at least one
pair satisfying (3.1), so the union bound over those pairs proves (0.7).
Taking logarithms in the first term and using (1.2) in the additive term
gives (0.8). \(\square\)

The estimate is much stronger than maximum pair codegree once \(s\) grows.
It does not by itself finish EKR: the right side of (0.8), though an
arbitrarily small polynomial fraction of \(D\), is still exponentially
large, and a high-overlap graph can have complicated components.

## 4. Exact nonlinear-overlap supersaturation

Let \(\mathcal F\) be a non-star intersecting strip family.  For every
target \(v\), some \(E_v\in\mathcal F\) avoids \(v\).  Equation (0.3)
therefore gives

\[
 d_{\mathcal F}(v)\le2\widehat\rho_mD.             \tag{4.1}
\]

For an integer \(s\ge1\), let \(J_s=J_s(\mathcal F)\) have vertex set
\(\mathcal F\), joining \(C,E\) when

\[
                         |e_C^\#\cap e_E^\#|>s.    \tag{4.2}
\]

### Theorem 4.1 (cover/overlap supersaturation)

Equations (0.9) and (0.10) hold.

#### Proof

Let \(\mathcal I\) be an independent set of \(J_s\).  If
\(\tau(\mathcal I)>s\), Theorem 2.1 gives

\[
                         |\mathcal I|\le K^{s+1}.   \tag{4.3}
\]

If \(\tau(\mathcal I)\le s\), cover \(\mathcal I\) by at most \(s\)
targets and use (4.1):

\[
                         |\mathcal I|
                         \le2s\widehat\rho_mD.      \tag{4.4}
\]

Thus \(\alpha(J_s)\le A_s\).  Every graph on \(f\) vertices with
independence number at most \(A\) has at least

\[
 {f\over2}\left({f\over A}-1\right)                \tag{4.5}
\]

edges, by the usual Turan bound applied to the complement.  Substituting
\(f=|\mathcal F|\) and \(A=A_s\) proves (0.9).

For \(s=1\), (1.4) makes \(K^2\) negligible compared with
\(2\widehat\rho_mD\), so \(A_1=(2+o(1))\widehat\rho_mD\).  If
\(f\ge cD/\sqrt m\), then

\[
 {f\over A_1}\asymp{1\over\widehat\rho_m\sqrt m}\longrightarrow\infty.
\]

Equation (4.5) consequently gives

\[
 e(J_1)=\Omega\left({f^2\over\widehat\rho_mD}\right)
       =\Omega\left({D\over m\widehat\rho_m}\right),
\]

which is (0.10). \(\square\)

Theorem 4.1 is the requested rigorous supersaturation statement.  It
shows exactly why the remaining family is not a linear-space design:
at the dangerous scale it has an exponentially large population of pairs
sharing at least two literal targets.

## 5. Pair-bundle blockers reduce to multigraphs

The next theorem treats non-clique weighted obstructions as well, but only
when all conflicts have a coherent target-pair representation.

### Definition 5.1 (pair-core representation)

A strip subfamily \(\mathcal Q\) has a pair-core representation if one can
assign to every \(C\in\mathcal Q\) an unordered pair

\[
                         \pi(C)=\{u_C,v_C\}
                         \subseteq e_C^\#            \tag{5.1}
\]

such that two members of \(\mathcal Q\) conflict if and only if their
assigned pairs share an endpoint.

Thus \(\mathcal Q\) is the edge multiset of a loopless multigraph on the
target vertices.  Its maximum degree is at most \(D\), and (0.2) bounds
its maximum edge multiplicity by

\[
                         \mu\le(4+o(1))D/m.          \tag{5.2}
\]

### Theorem 5.2 (pair-core fractional colouring)

Every pair-core represented subfamily satisfies

\[
                         \chi_f'(\mathcal Q)
                         \le D+2\mu.                \tag{5.3}
\]

In particular, (0.11) holds.

#### Proof

For a loopless multigraph \(G\), the fractional edge-chromatic number is

\[
 \chi_f'(G)=
 \max\left\{\Delta(G),
       \max_{\substack{U\subseteq V(G)\\|U|\text{ odd},\ |U|\ge3}}
       {2|E(G[U])|\over|U|-1}\right\}.             \tag{5.4}
\]

This is the fractional matching-polytope theorem.  Put \(r=|U|\).  The
degree and multiplicity bounds give

\[
 {2|E(G[U])|\over r-1}
 \le\min\left\{D{r\over r-1},\ \mu r\right\}.      \tag{5.5}
\]

If \(r\le D/\mu\), the second quantity is at most \(D\).  If
\(r>D/\mu\), then, for \(D/\mu\ge2\),

\[
 D{r\over r-1}
 =D+{D\over r-1}
 \le D+{D\over D/\mu-1}
 \le D+2\mu.                                       \tag{5.6}
\]

Taking the maximum in (5.4) proves (5.3).  Now use (5.2). \(\square\)

This includes all odd-set obstructions obtained by replacing the edges of
an ordinary graph by bundles of physical strips through target pairs.
The pair kernel forces bundle multiplicity \(O(D/m)\), and the worst odd
cut then has only \(O(D/m)\) excess.  Hence a physical obstruction at
precision \(D/\sqrt m\) cannot be assembled from pair bundles.

### Corollary 5.3 (pair-core resolution criterion)

For a nonnegative strip weight \(y\), write

\[
 \nu_y=\max_{M\text{ matching}}\sum_{C\in M}y_C.
\]

Suppose that every \(y\) admits a subfamily \(\mathcal Q_y\) with a
pair-core representation and

\[
 \sum_{C\notin\mathcal Q_y}y_C
 =o(D/\sqrt m)\,\nu_y.                             \tag{5.7}
\]

Then

\[
 \chi_f'(\mathcal H^\#)
 \le D+o(D/\sqrt m).                               \tag{5.8}
\]

#### Proof

Theorem 5.2, in its weighted LP-dual form, gives

\[
 \sum_{C\in\mathcal Q_y}y_C
 \le(D+O(D/m))
    \max_{M\text{ matching}}
       \sum_{C\in M\cap\mathcal Q_y}y_C
 \le(D+O(D/m))\nu_y.
\]

Add (5.7).  Since \(D/m=o(D/\sqrt m)\), the result is precisely the
dual inequality defining (5.8). \(\square\)

## 6. The exact surviving weighted gate

The preceding theorems dispose of three candidate blockers:

1. literal linear spaces, by Corollary 2.2;
2. every bounded-overlap high-cover family with overlap threshold
   \(s=o(h)\), by Theorem 2.1; and
3. every graph-like weighted odd-set construction, by Theorem 5.2.

For cliques, Theorem 4.1 says that the sole remaining possibility is a
nonlinear family with the high-overlap supersaturation (0.9).  A
sufficient physical anti-clustering statement would be the following.

> **Nonlinear-overlap dissipation.**  Uniformly for non-star intersecting
> \(\mathcal F\) with \(|\mathcal F|\ge D/\sqrt m\), there is some
> \(s=o(h)\) for which
> \[
> e(J_s(\mathcal F))
> <{|\mathcal F|\over2}
>   \left({|\mathcal F|\over
>    \max\{K^{s+1},2s\widehat\rho_mD\}}-1\right).   \tag{6.1}
> \]

Theorem 4.1 shows that (6.1) is impossible for such a clique.  Therefore
proving (6.1) from the cyclic pair kernel would refute every high-cover
clique.  The one-edge estimate (0.7) is not yet enough: substituting its
maximum-degree consequence into (6.1) loses an exponential factor.

Even complete clique exclusion is not formally equivalent to the desired
fractional edge-colouring theorem.  The exact weighted gate is

\[
 \boxed{
 \sum_C y_C
 \le\left(D+o(D/\sqrt m)\right)
       \max_{M\text{ matching}}\sum_{C\in M}y_C
 \quad(y_C\ge0).}                                  \tag{6.2}
\]

Theorem 5.2 proves (6.2) for every pair-core support.  Thus any violation
of (6.2) must simultaneously be

* weighted and non-clique or a nonlinear high-cover clique;
* not representable by target pairs; and
* supported on repeated intersections satisfying the supersaturation
  lower bound (0.9).

No such physical configuration is presently exhibited.  Conversely, the
pair kernel and cover number alone have not yet yielded the weighted
anti-clustering needed for (6.2).  This is the precise surviving physical
gate; it is strictly narrower than the “high-cover linear-space blocker”
left in the preceding note.

## 7. Audited boundary

Proved:

1. all literal and bounded-overlap linear-space blockers at the relevant
   cover scale are \(o(D/\sqrt m)\);
2. the uniform physical large-overlap neighbourhood estimate (0.7);
3. the exact nonlinear-overlap supersaturation inequality (0.9); and
4. the full weighted \(D+O(D/m)\) bound for pair-core obstructions and
   the sufficient pair-core resolution criterion (5.7).

Not proved:

1. nonlinear-overlap dissipation for arbitrary physical strip families;
2. the weighted inequality (6.2) outside pair-core supports; or
3. \(\chi_f'(\mathcal H^\#)=(1+o(m^{-1/2}))D\).

No physical obstruction at the forbidden scale is constructed.  Any such
obstruction must use genuinely higher-order intersection holonomy rather
than a projective plane, a literal linear space, or an odd graph of target
pairs.
