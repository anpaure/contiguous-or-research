# Rational protected-strip multicover: heat-bath audit and the exact fractional gate

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Consider the rational protected-strip multicover after denominators have
been cleared.  Each chunk contains one tag and at most \(K\) protected
targets.  Every tag has degree \(D\), while every protected target has
degree at most \((1+\xi)D\), where \(\xi=o(1)\).

There are three distinct conclusions.

1. The hypotheses stated only as degree balance, pairwise intersection
   width at most two, and normalized exponential intersection excess
   \(m^{o(1)}\) do **not** imply a \((1+o(1))D\) edge colouring.  The
   doubled-triangle obstruction in
   `RATIONAL_MULTICOVER_EDGE_COLORING_OBSTRUCTION_20260725.md` has
   chromatic and fractional chromatic index at least \(3D/2\).
2. The stronger fixed-shape span-codegree estimate already proved for the
   catalogue does **not** exclude this obstruction.  That estimate is only
   for competitors on distinct tags.  The doubled triangle puts every
   repeated two-target intersection inside one tag, while different tags
   meet in only one target.  In the actual parameter range,
   \[
     K=m^{1+o(1)},\qquad D\ge m^{5/2-o(1)},\qquad
     K^2/D=m^{-1/2+o(1)}.
   \]
   The doubled triangle can be chosen in exactly this numerical range, so
   neither fact removes the displayed obstruction.
3. The exact first gate is fractional, not integral.  If the fractional
   chromatic index is at most \((1+\eta)D\), then a further common rational
   scaling has an exact integral decomposition into at most
   \((1+\eta)D\) matchings per copy.  One matching contains at least
   \(T/(1+\eta)\) chunks, where \(T\) is the number of tags.  Thus
   \(\eta=o(1)\) gives the required near-factor.  No theorem for the
   original, unscaled multicover follows from this rational argument.

A direct local hard-core or Dobrushin heat bath does not prove the missing
fractional inequality.  At activity of order \(D^{-1}\), its calibrated
conflict load is of order \(K\); at the smaller activity \((KD)^{-1}\)
where a local cluster expansion can start, the tag occupancy is only of
order \(K^{-1}\).  The desired near-factor therefore requires a global
matching-cover mechanism.

## 1. Abstract multicover and its two chromatic indices

Let \({\cal T}\) be a set of \(T\) tags and \({\cal V}\) the protected
target set.  Let \({\cal H}\) be a finite multihypergraph.  An occurrence
edge has the form

\[
 e=\{\tau(e)\}\cup C(e),\qquad
 \tau(e)\in{\cal T},\quad C(e)\subseteq{\cal V},
 \quad |C(e)|\le K.
 \tag{1.1}
\]

Assume

\[
 d(\tau)=D\quad(\tau\in{\cal T}),
 \qquad d(v)\le(1+\xi)D\quad(v\in{\cal V}).
 \tag{1.2}
\]

In particular,

\[
 |E({\cal H})|=TD.
 \tag{1.3}
\]

A colour class is a matching: it contains at most one edge at every tag
and at every protected target.  Let \(\chi'({\cal H})\) be the integral
chromatic index.

Let \({\cal M}\) be the finite family of all matchings.  The fractional
chromatic index is

\[
 \chi_f'({\cal H})
 =\min\left\{
       \sum_{M\in{\cal M}}y_M:
       y_M\ge0,\quad
       \sum_{M\ni e}y_M\ge1\ (e\in E({\cal H}))
     \right\}.
 \tag{1.4}
\]

Parallel occurrences are kept distinct in (1.4).  A matching contains at
most one of several parallel copies, as it must.

### Proposition 1.1 (exact weighted matching-cover cut)

For every \(q\ge0\), the inequality

\[
 \chi_f'({\cal H})\le q
 \tag{1.5}
\]

holds if and only if, for every nonnegative occurrence weight
\(a:E({\cal H})\to\mathbb R_{\ge0}\),

\[
 \boxed{
   \sum_e a_e
   \le q\max_{M\in{\cal M}}\sum_{e\in M}a_e.}
 \tag{1.6}
\]

#### Proof

The dual of (1.4) is

\[
 \max\left\{
       \sum_e z_e:
       z_e\ge0,\quad
       \sum_{e\in M}z_e\le1\ (M\in{\cal M})
     \right\}.
 \tag{1.7}
\]

Finite-dimensional linear-programming duality applies.  If (1.6) holds
and \(z\) is feasible in (1.7), then \(\sum_ez_e\le q\).  Conversely, if
(1.6) fails for \(a\), divide \(a\) by
\(\max_M\sum_{e\in M}a_e\); the denominator is positive unless \(a=0\).
The resulting vector is feasible in (1.7) and has objective value greater
than \(q\).  This proves the equivalence. \(\square\)

Thus point-degree feasibility is only the subfamily of (1.6) obtained from
star-supported weights.  It does not give the full matching-cover cut.

## 2. Rational fractional colourings factor integrally after scaling

### Theorem 2.1 (exact scaled factorization)

Suppose

\[
 \chi_f'({\cal H})\le q
 \tag{2.1}
\]

with rational \(q\).  There is an integer \(L\ge1\) such that the
multihypergraph \(L{\cal H}\), obtained by replacing every occurrence by
\(L\) labelled copies, has a proper edge colouring with at most \(qL\)
colours.

#### Proof

The polytope in (1.4) is rational and finite, so it has a rational optimum
\((y_M)\).  Give the empty matching the additional weight
\(q-\sum_My_M\), so that \(\sum_My_M=q\).  Choose \(L\) clearing every
denominator of the \(y_M\) and of \(q\).  Make \(Ly_M\) labelled slots of
type \(M\).

For each occurrence edge \(e\), the number of slots whose matching type
contains \(e\) is

\[
 \sum_{M\ni e}Ly_M\ge L.
\]

Assign the \(L\) labelled copies of \(e\) injectively to any \(L\) of
these slots, and delete \(e\) from all its other slots.  These assignments
can be made separately for different \(e\): deleting members of a
matching cannot destroy the matching property.  Every slot is therefore
a matching, and every labelled edge copy occurs in exactly one slot.  The
number of slots is \(qL\). \(\square\)

### Corollary 2.2 (exact near-factor accounting)

If

\[
 \chi_f'({\cal H})\le(1+\eta)D,
 \tag{2.2}
\]

then some colour in the scaled factorization contains at least

\[
 \boxed{|M|\ge {T\over1+\eta}.}
 \tag{2.3}
\]

It leaves at most

\[
 \boxed{T-|M|\le {\eta\over1+\eta}T}
 \tag{2.4}
\]

tags uncovered.

#### Proof

The scaled multicover has \(LTD\) occurrence edges and at most
\((1+\eta)DL\) colour classes.  Their average cardinality is at least
\(T/(1+\eta)\).  A largest class satisfies (2.3), and (2.4) follows.
\(\square\)

For a chunk length \(g\) with \(gT=(1+o(1))W\), (2.4) has physical cost

\[
 g(T-|M|)\le(1+o(1)){\eta\over1+\eta}W.
 \tag{2.5}
\]

If each selected legal chunk has an \(O(Q)\) initialization and
\(Q=o(g)\), all chunk initializations cost

\[
 O(QT)=O(QW/g)=o(W).
 \tag{2.6}
\]

Hence \(\eta=o(1)\) is exactly sufficient for the coefficient ledger.
This is only a scaled factorization.  To colour the original occurrence
multicover itself one still needs a growing-\(K\) integrality-gap theorem,
for example

\[
 \chi'({\cal H})\le\chi_f'({\cal H})+o(D),
 \tag{2.7}
\]

uniformly in the present parameter range.  Nothing in Theorem 2.1 proves
(2.7).

## 3. Why the summary hypotheses do not imply the fractional cut

The construction in
`RATIONAL_MULTICOVER_EDGE_COLORING_OBSTRUCTION_20260725.md` has, for even
\(D\), \(D/2\) copies of each of the three core types

\[
 ab,\qquad bc,\qquad ca,
 \tag{3.1}
\]

with private padding to any prescribed \(K\).  The \(3D/2\) core edges
are pairwise intersecting, so every matching contains at most one of them.
Putting weight one on those edges in (1.6) gives

\[
 {3D\over2}\le q.
 \tag{3.2}
\]

Thus \(\chi_f'\ge3D/2\), before integral rounding is considered.  The
example has target degree at most \(D\), pairwise intersections of size at
most two, and centered normalized exponential excess at most
\(\tfrac12(w-1)^2\).  For \(w\le C\log m\), this is \(m^{o(1)}\).

Consequently neither entropy compression nor a heat bath can prove
(2.2) from only the user-listed summary hypotheses: the desired statement
is false even fractionally.

## 4. The genuine span bound does not exclude the doubled triangle

The actual protected-strip catalogue has a stronger input.  If a fixed
width-two intersection shape has meet--join span \(t\ge1\), its relative
degree among **different-tag** competitors is at most

\[
 \boxed{
 m^{o(1)}{t+1\over\binom{m-g}{t}}.}
 \tag{4.1}
\]

This is Lemma 3.1(3.4) of
`PROTECTED_STRIP_WIDTH_TWO_PRUNING_AND_DUAL_GATE_20260725.md`, equivalently
Lemma 11.2 of
`MATH_ATTACK_H_CATALOGUE_OVERLAP_HIERARCHY_20260725.md`.

The tag restriction is essential.  In the doubled triangle, the \(D/2\)
chunks containing the core pair \(\{a_j,b_j\}\) all have the same tag
\(\tau_{ab}\).  They are absent from the sum in the actual span-codegree
theorem.  A chunk on \(\tau_{ab}\) meets chunks on either distinct tag
\(\tau_{bc}\) or \(\tau_{ca}\) in exactly one core target.  Such a
singleton intersection has no nontrivial two-target shape and contributes
zero to the centered exponential excess.  Thus (4.1) is satisfied
vacuously by every cross-tag nontrivial shape in this example.

If (4.1) were additionally assumed for same-tag competitors, then the
relative codegree \(1/2\) of \(\{a_j,b_j\}\) would indeed contradict its
\(m^{-1+o(1)}\) right-hand side.  That is not the theorem currently proved,
and same-tag intersections were intentionally omitted because a matching
already uses at most one chunk from a tag.

The retained catalogue also has

\[
 D\ge m^{5/2-o(1)}.
 \tag{4.2}
\]

Its protected chunk size obeys

\[
 K\le(2Q+1)g=m^{1+o(1)},
 \tag{4.3}
\]

and therefore

\[
 \boxed{K^2/D=m^{-1/2+o(1)}=o(1).}
 \tag{4.4}
\]

Here \(D\) in (4.2)--(4.4) is the retained support-degree scale.  A later
common replication may make the occurrence degree arbitrarily large and
does not strengthen (4.4); normalized codegrees and the support have not
changed.

The doubled triangle works for arbitrary \(K\ge2\) by private padding and
arbitrary even \(D\).  It may therefore be instantiated with (4.2)--(4.4).
Consequently the cross-tag form of (4.1), even together with (4.4), does
not verify (1.6).  The obstruction is an odd matching-cover cut assembled
from three tag fibres; it is invisible to every repeated-intersection
statistic currently listed.

## 5. Local heat-bath scale

Give every occurrence edge a common hard-core activity \(\lambda\).  The
standard local cluster-expansion or Dobrushin load at an edge \(e\) contains

\[
 L(e):=\sum_{f\ne e:f\cap e\ne\varnothing}
          {\lambda\over1+\lambda}.
 \tag{5.1}
\]

Using (1.2),

\[
 L(e)\le {\lambda\over1+\lambda}
          \left(D-1+\sum_{v\in C(e)}(d(v)-1)\right)
 \le(1+o(1))\lambda(K+1)D
 \tag{5.2}
\]

when \(\lambda=o(1)\).  In a calibrated near-regular target reservoir,
the actual distinct-neighbour load is \(\Theta(\lambda KD)\) for all but
an \(o(1)\) fraction of edges, provided the calibrated incidence is not
concentrated inside single tags.  Precisely, write

\[
 d_\tau(v)=|\{e:\tau(e)=\tau,\ v\in C(e)\}|.
\]

Assume \(|C(e)|=K\), \(|{\cal V}|=(1+o(1))KT\),
\(\sum_vd(v)=KTD\), and

\[
 \max_{\tau,v}d_\tau(v)\le\zeta D,
 \qquad \zeta=o(1).
 \tag{5.2a}
\]

Then Cauchy--Schwarz and (5.2a) give

\[
 {1\over TD}\sum_e
   \sum_{\substack{f:\tau(f)\ne\tau(e)}}
       |C(e)\cap C(f)|
 ={1\over TD}\sum_v
   \left(d(v)^2-\sum_\tau d_\tau(v)^2\right)
 \ge(1-o(1))KD.
 \tag{5.3}
\]

For \(j_{ef}=|C(e)\cap C(f)|\), put

\[
 S_e^\times=\sum_{f:\tau(f)\ne\tau(e)}j_{ef},\qquad
 N_e^\times=|\{f:\tau(f)\ne\tau(e),\ j_{ef}\ge1\}|.
\]

The centered moment at \(w=2\) gives

\[
\begin{aligned}
 S_e^\times-N_e^\times
 &=\sum_{\substack{f:\tau(f)\ne\tau(e)\\j_{ef}\ge2}}(j_{ef}-1)\\
 &\le\sum_{f:\tau(f)\ne\tau(e)}(2^{j_{ef}}-1-j_{ef})
 \le D\mathfrak M_2(e)=Dm^{o(1)}.
 \tag{5.3a}
\end{aligned}
\]

Since \(K=m^{1+o(1)}\), the final error is \(o(KD)\).  The target-degree
ceiling gives \(S_e^\times\le(1+o(1))KD\), while (5.3) says that its edge
average is at least \((1-o(1))KD\).  Hence all but an \(o(1)\) fraction
of edges have

\[
 N_e^\times=(1-o(1))KD.
 \tag{5.3b}
\]

For those edges, (5.1) is \(\Theta(\lambda KD)\) when \(\lambda=o(1)\).

At one tag, even after deleting all non-tag conflicts, the hard-core
occupancy is

\[
 {D\lambda\over1+D\lambda}.
 \tag{5.4}
\]

Indeed, after conditioning on all choices outside the tag, the total
weight of the \(D\) alternatives at the tag is at most \(D\lambda\) times
the weight of leaving that tag empty.  Additional target conflicts can
only decrease (5.4).  Thus occupancy
\(1-o(1)\) requires \(D\lambda\to\infty\).  But then (5.3) makes the
typical local load at least

\[
 (1-o(1))K(D\lambda)\longrightarrow\infty.
 \tag{5.5}
\]

Already at \(\lambda=c/D\), (5.4) is only \(c/(1+c)\) and the load is
\(\Theta(cK)\).  At the cluster-safe scale
\(\lambda=\Theta((KD)^{-1})\), tag occupancy is only \(\Theta(K^{-1})\).

Therefore a one-phase local hard-core expansion cannot simultaneously
have a bounded influence sum and near-unit tag occupancy when
\(K\to\infty\).  The exponential intersection moment controls repeated
neighbours and high common cores; it does not remove the linear contribution
\(\sum_{v\in C(e)}d(v)\), which is exactly the term in (5.2)--(5.3).

## 6. Exact surviving theorem

The coefficient-safe positive statement now has two logically separate
parts.

1. **Fractional protected-strip matching-cover theorem.**  Prove, using
   an additional global legality/chronology property not contained in the
   present cross-tag span hierarchy, that for some \(\eta_m=o(1)\),
   \[
     \sum_ea_e
     \le(1+\eta_m)D
       \max_{M\text{ matching}}\sum_{e\in M}a_e
     \quad\text{for every }a\ge0.
     \tag{6.1}
   \]
   By Proposition 1.1 and Corollary 2.2, this alone gives a genuine legal
   near-factor after a common rational scaling, with physical leave
   \(O(\eta_mW)=o(W)\).
2. **Unscaled growing-\(K\) integrality theorem.**  If colouring the given
   cleared multicover itself is required, prove (2.7) with an error
   \(o(D)\), uniformly under
   \[
      K=m^{1+o(1)},\quad K^2/D=m^{-1/2+o(1)},
   \]
   and the complete fixed-span codegree hierarchy.

The first item is unavoidable; the doubled-triangle example shows that no
integral rounding theorem can repair its failure.  The second item should
not be attacked before the first has been verified.  No coefficient-one
conclusion is claimed here.
