# Repaired promotion rings: deterministic root transversals, large meshes, and the nonadditive augmentation gate

Date: 2026-07-26

Scope: constant-one owner packing only.  This note uses, without repeating
their codegree calculations,

* `MATH_THEOREM_REPAIRED_RING_EKR_AND_NONSTAR_CLIQUES_20260726.md`; and
* `MATH_THEOREM_REPAIRED_RING_SMALL_MESH_DENSITY_20260726.md`.

The convention is the one-hole repaired catalogue: an edge has one root
and \(M-1\) owners, where

\[
 M=m+H,\qquad H=(1+o(1))\sqrt{m\log m}.
\tag{0.1}
\]

Formal orientations are retained.  Thus every root star has size

\[
 D=M!.
\tag{0.2}
\]

## 0. Outcome

The EKR and small-mesh inputs do not yet prove a matching missing
\(o(N_H)\) roots.  They do, however, force every deterministic obstruction
far beyond the previously visible \(\Omega(m)\) scale.

Put

\[
 \sigma_R:=H(M-1)m!H!,\qquad
 L_R:={D\over\sigma_R}
      ={\binom MH\over H(M-1)}.
\tag{0.3}
\]

Here \(\sigma_R\) is the maximum number of options in one root star
blocked by one edge from a different root.  Consequently

\[
 L_R=\exp\big((1+o(1))H\log(m/H)\big)=m^{\Theta(H)}.
\tag{0.4}
\]

This note proves four deterministic statements.

1. **Robust partial-star Hall theorem.**  Let
   \(\mathcal F_i\) be arbitrary subfamilies of \(a\) distinct root
   stars.  If, after increasing-size ordering,

   \[
                |\mathcal F_i|>(i-1)\sigma_R
                \qquad(1\le i\le a),                \tag{0.5}
   \]

   then the \(\mathcal F_i\) have pairwise-disjoint representatives.  In
   particular, if \(a\sigma_R\le D\) and

   \[
                       \sum_i|\mathcal F_i|>(a-1)D, \tag{0.6}
   \]

   they have a full rooted transversal.

2. **Support theorem for every cardinality mesh.**  If
   \(\mathcal B\) is any subcatalogue with

   \[
      \nu(\mathcal B)=r,\qquad |\mathcal B|>rD,      \tag{0.7}
   \]

   and its edges use \(a\) roots, then

   \[
        r>\left({1\over8}+o(1)\right)m,
        \qquad
        a>\sqrt{L_R}.                                \tag{0.8}
   \]

   Thus the first possible unweighted mesh is simultaneously
   \(\Omega(m)\) in matching number and
   \(m^{\Theta(H)}\) in root support.  No clique, finite odd gadget,
   polynomial star mesh, or localized cardinality certificate survives.

3. **Full-root Hall circuits are even larger.**  If a root set
   \(\mathcal C\) is inclusion-minimal with no disjoint choice of one full
   repaired ring per root, then

   \[
       |\mathcal C|>L_R,
       \qquad
       \nu\!\left(\bigcup_{A\in\mathcal C}\mathcal S(A)\right)
          =|\mathcal C|-1.                            \tag{0.9}
   \]

   Hence a failure of a perfect rooted matching cannot have a bounded,
   polynomial, or merely Gaussian-scale Hall certificate.

4. **Exact remaining deterministic gate.**  The preceding circuit bound
   is not additive in the deficiency.  A closed alternating component with
   one unmatched root must be large, but the two theorems do not rule out
   one enormous component containing a positive fraction of all unmatched
   roots.  To obtain the desired leave it is sufficient to prove the
   deficiency-linear strengthening

   \[
             |\mathcal C|\ge L(m)\operatorname{def}(\mathcal C),
             \qquad L(m)\longrightarrow\infty,       \tag{0.10}
   \]

   for every blocker-closed alternating component.  Then the unmatched
   roots are at most \(N_H/L(m)=o(N_H)\).

No physical family satisfying (0.7) is constructed.  The attempted
\(\Omega(m)\) star and odd-cycle meshes fail: full root stars have robust
transversals through the much larger scale \(L_R\), and partial meshes
must have the diffuse profile in Section 5.  Thus the present result is a
positive obstruction theorem, not the requested near-perfect matching.

## 1. Root parts and the cross-blocking constant

For a root \(A\), write \(\mathcal S(A)\) for its full star.  The root-link
lemma in the EKR note states that, for every edge \(e\notin\mathcal S(A)\),

\[
 |\{f\in\mathcal S(A):f\cap e\ne\varnothing\}|
 \le \sum_{x\in e}d(A,x)
 \le \sigma_R.                                      \tag{1.1}
\]

The first inequality is only a union bound, so (1.1) remains valid for
every subfamily \(\mathcal F\subseteq\mathcal S(A)\): one foreign edge
deletes at most \(\sigma_R\) members of \(\mathcal F\).

The ratio in (0.3) follows from

\[
 {D\over\sigma_R}
 ={M!\over H(M-1)m!H!}
 ={\binom MH\over H(M-1)}.                           \tag{1.2}
\]

Since \(H=o(m)\), Stirling's formula gives (0.4).

## 2. A robust deterministic root-transversal theorem

### Lemma 2.1 (ordered greedy transversal)

Let \(A_1,\ldots,A_a\) be distinct roots and let
\(\mathcal F_i\subseteq\mathcal S(A_i)\).  Relabel them so that

\[
 |\mathcal F_1|\le|\mathcal F_2|\le\cdots\le|\mathcal F_a|.
\tag{2.1}
\]

If (0.5) holds, there are pairwise-disjoint edges
\(e_i\in\mathcal F_i\).

#### Proof

Choose the edges in the order (2.1).  Before choosing \(e_i\), there are
\(i-1\) selected foreign-root edges.  By (1.1), together they forbid at
most \((i-1)\sigma_R\) members of \(\mathcal F_i\).  The strict inequality
in (0.5) leaves an available member. \(\square\)

### Theorem 2.2 (total-mass robust Hall criterion)

Suppose \(a\sigma_R\le D\).  If the subfamilies in Lemma 2.1 satisfy

\[
                         \sum_{i=1}^a|\mathcal F_i|>(a-1)D,
\tag{2.2}
\]

then they have a full rooted transversal.

#### Proof

Use the order (2.1).  If (0.5) fails, let \(i\) be an index with

\[
                         |\mathcal F_i|\le(i-1)\sigma_R.
\tag{2.3}
\]

Then the first \(i\) families have size at most the right side of (2.3),
and every remaining family has size at most \(D\).  Hence

\[
\begin{aligned}
 \sum_{j=1}^a|\mathcal F_j|
 &\le i(i-1)\sigma_R+(a-i)D\\
 &\le(a-1)D,
\end{aligned}                                        \tag{2.4}
\]

because

\[
 (a-1)D-\big(i(i-1)\sigma_R+(a-i)D\big)
  =(i-1)(D-i\sigma_R)\ge0.
\]

This contradicts (2.2).  Thus (0.5) holds and Lemma 2.1 applies.
\(\square\)

For full root stars, Theorem 2.2 is stronger than the elementary
owner-count transversal: every root set of size \(a\) satisfying

\[
                         (a-1)\sigma_R<D             \tag{2.5}
\]

has a full repaired-ring matching.

## 3. Root support of an arbitrary density obstruction

Let \(\mathcal B\) be a subcatalogue.  For every root in its support put

\[
 \mathcal F_A=\mathcal B\cap\mathcal S(A),\qquad
 f_A=|\mathcal F_A|.
\tag{3.1}
\]

The root parts are disjoint and \(f_A\le D\).

### Theorem 3.1 (large root support)

Assume (0.7), and let \(a\) be the number of nonempty root parts.  Then

\[
                         a^2\sigma_R>D.               \tag{3.2}
\]

#### Proof

Call a root part **large** if

\[
                         f_A>a\sigma_R,               \tag{3.3}
\]

and let \(h\) be the number of large parts.  Lemma 2.1, in any order,
gives a matching with one edge from every large part.  Hence \(h\le r\).

In fact \(h\ne r\).  If equality held, choose one edge first from any
nonempty small part; such a part exists because \(a>r\), the latter being
forced by \(|\mathcal B|>rD\).  Then greedily choose from all \(r\) large
parts.  Before every such choice there are at most \(r<a\) selected
foreign edges, so fewer than \(a\sigma_R\) members are forbidden.  This
constructs a matching of size \(r+1\), a contradiction.  Therefore

\[
                         h\le r-1.                    \tag{3.4}
\]

The large parts contribute at most \((r-1)D\), while all small parts
together contribute at most \(a^2\sigma_R\).  Thus

\[
 |\mathcal B|\le(r-1)D+a^2\sigma_R.                  \tag{3.5}
\]

If (3.2) failed, (3.5) would give \(|\mathcal B|\le rD\), contrary to
(0.7). \(\square\)

Combining (3.2) with (1.2) gives

\[
 \boxed{
 a>\sqrt{L_R}
   =\left({\binom MH\over H(M-1)}\right)^{1/2}
   =\exp\big((1/2+o(1))H\log(m/H)\big).}             \tag{3.6}
\]

The small-mesh density theorem independently gives

\[
 \boxed{r>\left({1\over8}+o(1)\right)m.}             \tag{3.7}
\]

Equations (3.6)--(3.7) prove (0.8).  Notice that they control different
features: (3.7) is an owner-link/matching-number statement, while (3.6) is
a root-part/cross-blocking statement.

## 4. Full-root Hall circuits

Call a root set \(\mathcal C\) **dependent** if its full stars do not have
a transversal.  It is a **root circuit** if it is dependent and every
proper subset is independent.

### Theorem 4.1 (root-circuit lower bound)

Every root circuit satisfies

\[
                         |\mathcal C|>L_R.            \tag{4.1}
\]

Moreover, with

\[
 \mathcal B_{\mathcal C}
   =\bigcup_{A\in\mathcal C}\mathcal S(A),           \tag{4.2}
\]

one has

\[
 |\mathcal B_{\mathcal C}|=|\mathcal C|D,
 \qquad
 \nu(\mathcal B_{\mathcal C})=|\mathcal C|-1.       \tag{4.3}
\]

#### Proof

If \((|\mathcal C|-1)\sigma_R<D\), Lemma 2.1 applied to the full stars
would give a transversal, contrary to dependence.  This proves (4.1).

Delete any one root from \(\mathcal C\).  Minimality supplies a matching
of size \(|\mathcal C|-1\), while dependence forbids size
\(|\mathcal C|\).  The root parts in (4.2) are disjoint and each has size
\(D\), proving (4.3). \(\square\)

Thus a failure of a perfect rooted factor does produce a genuine
cardinality mesh, but the first possible certificate has matching number

\[
 |\mathcal C|-1
  >{\binom MH\over H(M-1)}-1
  =m^{\Theta(H)},                                    \tag{4.4}
\]

not merely \(\Theta(m)\).  No such physical circuit is presently known.

## 5. The sharp profile of a first small-mesh obstruction

It is useful to record what equality in the small-mesh proof would force.
Choose a cardinality obstruction \(\mathcal B\) with minimum possible
matching number \(r\), and let \(F=\{e_1,\ldots,e_r\}\) be a maximum
matching.  Put

\[
                         C=\bigcup_{i=1}^r e_i,       \tag{5.1}
\]

so \(|C|=rM\) and \(C\) is a vertex cover of \(\mathcal B\).

Let

\[
 s=\max_{v, e\not\ni v}\sum_{x\in e}d(v,x)
   =\left({8+o(1)\over m^2}\right)D                 \tag{5.2}
\]

be the small-mesh constant.

### Proposition 5.1 (flat-mesh necessity)

Every vertex satisfies

\[
                         d_{\mathcal B}(v)\le rs,    \tag{5.3}
\]

while the matching cover satisfies

\[
 {1\over rM}\sum_{v\in C}d_{\mathcal B}(v)
    \ge {|\mathcal B|\over rM}
    >{D\over M}.                                    \tag{5.4}
\]

Consequently \(rs>D/M\), which is (3.7).  If

\[
                         r=\left({1\over8}+o(1)\right)m,
\tag{5.5}
\]

then (5.3)--(5.4) are asymptotically equal: almost all of the available
incidence capacity on the \(\Theta(m^2)\) vertices of \(C\) must be used
at scale \(D/m\).  In addition,

\[
 \sum_{e\in\mathcal B}(|e\cap C|-1)
   =\sum_{v\in C}d_{\mathcal B}(v)-|\mathcal B|      \tag{5.6}
\]

must be lower order at a sharp threshold.  Thus a first obstruction is a
diffuse, nearly one-hit incidence mesh, not a union of large stars or
nonstar cliques.

#### Proof

If (5.3) failed at \(v\), let
\(\mathcal B'=\{e\in\mathcal B:v\notin e\}\).  A matching of size \(r\)
in \(\mathcal B'\) would force every edge of \(\mathcal B\) through \(v\)
to meet its union and hence, by the definition of \(s\), would give
\(d_{\mathcal B}(v)\le rs\).  Therefore
\(\nu(\mathcal B')\le r-1\).  Minimality of \(r\) gives
\(|\mathcal B'|\le(r-1)D\), and the ambient degree bound gives
\(d_{\mathcal B}(v)\le D\); together they contradict
\(|\mathcal B|>rD\).  This proves (5.3).

Every edge of \(\mathcal B\) meets \(C\), proving the first inequality in
(5.4) by incidence counting.  Equations (5.2)--(5.4) imply
\(rs>D/M\).  Under (5.5), their upper and lower endpoints differ by
\(o(D/m)\).  Formula (5.6) is the exact excess-incidence identity.
\(\square\)

The proposition does not assert that such a mesh exists.  It identifies
the first profile not eliminated by the two supplied theorems.

## 6. Alternating augmentation uses a different rank function

Fix a matching \(Q\).  For a catalogue edge \(e\), let

\[
 \beta_Q(e)=\{f\in Q:e\cap f\ne\varnothing\}         \tag{6.1}
\]

be its blocker set.  An augmentation is a matching \(P\) of new edges
such that

\[
                         |P|>|\beta_Q(P)|,            \tag{6.2}
\]

where \(\beta_Q(P)=\bigcup_{e\in P}\beta_Q(e)\), and the roots gained by
\(P\) include the desired unmatched roots.  Replacing
\(\beta_Q(P)\) by \(P\) then increases the rooted matching.

The small-mesh theorem controls \(|P|\) as an ordinary matching inside a
subcatalogue.  It does **not** control the blocker expansion
\(|\beta_Q(P)|\).  These are different parameters:

* many disjoint new rings can all meet one old ring at different owner
  vertices, in which case ordinary matching is large and blocker expansion
  is one; and
* a family with excellent EKR behavior can still send every one of its
  disjoint choices to different old blockers.

Thus a Berge-path search based only on ordinary matching number has no
valid termination theorem here.  A successful deterministic proof needs a
two-shore statement involving the matching \(Q\) and the candidate family
simultaneously.

## 7. Blocker-closed components and the sufficient additive theorem

Let \(R(Q)\) be the roots used by \(Q\).  A root set \(\mathcal C\) is
**blocker-closed relative to \(Q\)** if every matching edge in \(Q\) which
meets a candidate edge rooted in \(\mathcal C\) also has its root in
\(\mathcal C\).  Put

\[
 q(\mathcal C)=|\mathcal C\setminus R(Q)|.           \tag{7.1}
\]

The current matching has \(|\mathcal C|-q(\mathcal C)\) edges rooted in
such a component.  If it is nonaugmentable, blocker closure implies

\[
 \nu\!\left(\bigcup_{A\in\mathcal C}\mathcal S(A)\right)
    \le |\mathcal C|-q(\mathcal C).                  \tag{7.2}
\]

Indeed, a larger matching inside the full root subcatalogue would meet no
member of \(Q\) rooted outside \(\mathcal C\), and would replace the
current edges inside \(\mathcal C\).

For \(q(\mathcal C)>0\), (7.2) makes the full-star union a cardinality
mesh.  Theorem 4.1 proves only the one-unit conclusion

\[
                         |\mathcal C|>L_R.            \tag{7.3}
\]

It supplies no factor \(q(\mathcal C)\).

### Deficiency-linear repaired-ring mesh theorem (DLM)

There is a function \(L(m)\to\infty\) such that every blocker-closed,
nonaugmentable component satisfies

\[
                         |\mathcal C|\ge L(m)q(\mathcal C).   \tag{7.4}
\]

### Theorem 7.1 (DLM implies the owner near-factor)

Suppose the unmatched roots of every maximum matching can be covered by
root-disjoint blocker-closed components satisfying DLM.  Then the matching
misses \(o(N_H)\) roots.  Consequently the repaired-ring owner leave is
\(o(W)\).

#### Proof

Let the components be \(\mathcal C_1,\ldots,\mathcal C_t\).  Their
deficiencies sum to the number \(s\) of unmatched roots.  By (7.4) and
root disjointness,

\[
 L(m)s
 \le\sum_i|\mathcal C_i|
 \le N_H.
\tag{7.5}
\]

Hence \(s\le N_H/L(m)=o(N_H)\).  The exact owner ledger from the
packing-side audit then gives \(o(W)\) holes. \(\square\)

The supplied EKR and small-mesh theorems prove neither root-disjoint
component coverage nor the linear dependence on \(q\) in (7.4).  This is
not a cosmetic strengthening: rooted disjoint-representative systems form
a hereditary independence system, but no exchange axiom or submodular rank
function has been proved.  Large one-unit circuits can overlap densely and
carry a macroscopic total deficiency.

## 8. Edge-colouring formulation

A proper colouring of all catalogue edges with \(D+o(D)\) colours would
also solve the problem: since there are \(N_HD\) root-edge incidences, one
colour class would contain

\[
                         {N_HD\over D+o(D)}=N_H-o(N_H)
\tag{8.1}
\]

edges.  It would therefore miss only \(o(N_H)\) roots.

The EKR theorem proves that the largest line-graph cliques are the root
stars of size \(D\), and the small-mesh theorem eliminates all unweighted
matching-polytope obstructions of matching number \(o(m)\).  Those facts
do not yield an edge colouring: a colour-exchange fan is governed by the
same blocker sets (6.1), and a failed fan may be one large, diffuse mesh of
the form in Proposition 5.1.  Controlling it is again DLM, or a stronger
weighted two-shore analogue.

Thus the augmenting-path and edge-colouring routes meet at exactly the same
deterministic gate; neither is blocked by a local odd cycle, and neither is
closed by ordinary EKR alone.

## 9. Final boundary

Unconditional:

\[
\begin{array}{ll}
\text{nonstar clique size}&\le(8/m+o(1/m))D,\\
\text{cardinality-mesh matching number}&>(1/8+o(1))m,\\
\text{cardinality-mesh root support}&>\sqrt{L_R},\\
\text{full-root Hall-circuit size}&>L_R,
\end{array}                                           \tag{9.1}
\]

where

\[
                         L_R=m^{\Theta(H)}.           \tag{9.2}
\]

Still open:

1. a physical cardinality obstruction at any scale;
2. an additive lower bound \(|\mathcal C|\gg q(\mathcal C)\) for closed
   alternating components;
3. a deterministic matching missing \(o(N_H)\) roots; and
4. a \(D+o(D)\) edge colouring.

Therefore the supplied repaired-ring EKR and small-mesh theorems rule out
not only fixed gadgets but every localized unweighted density certificate.
They do not by themselves rule out a localized blocker obstruction, because
ordinary matching number and blocker expansion differ as in Section 6.
The remaining alternative is exact: either prove deficiency-linear blocker
expansion, which gives the coefficient-one owner near-factor, or construct
a genuinely global, diffuse, blocker-closed mesh carrying nonadditive
deficiency.  No such physical mesh is currently exhibited.
