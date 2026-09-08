# Width-three pruning: the exact EKR pair-star conclusion and its sharp limit

Date: 2026-07-25

Method: pure mathematics only.  No computation, solver, or web input is
used.

## 0. Verdict

Replace the protected three-antichain conflict by the conflict which deletes
one member of every pair sharing four pairwise incomparable protected
targets.  The proposed scale is numerically correct.  Under the same
protected-anchor census as in the width-two argument,

\[
 {\Delta _4+1\over A}\le m^{-5+o(1)}.               \tag{0.1}
\]

With

\[
 L=Qm^{2/3}\log m,\qquad Q=m^{1/2+o(1)},            \tag{0.2}
\]

isolated pruning has nominal retained degree

\[
 \mu={A\over L(\Delta _4+1)}=m^{23/6-o(1)}.         \tag{0.3}
\]

For protected edge rank

\[
 K\le(2Q+1)g=m^{1+o(1)},                            \tag{0.4}
\]

one in fact has

\[
 {K^2\over\mu}=m^{-11/6+o(1)},\qquad
 {K^3\over\mu}=m^{-5/6+o(1)},\qquad
 {K^4\over\mu}=m^{1/6+o(1)}.                       \tag{0.5}
\]

Thus the new scale crosses the cubic EKR threshold, but not a quartic one.

There is an exact positive conclusion.  Let \({\cal F}\) be any
pairwise target-intersecting family of protected supports of size at most
\(K\).  Then either all its members contain one common target, or
\({\cal F}\) is covered by at most \(K^2\) pair-stars.  More quantitatively,
for every threshold \(b\), all but at most \(K^2b\) members are covered by
at most \(K^2\) pair-stars having more than \(b\) members.  Taking \(b=K\)
gives

\[
 \boxed{
 {\cal F}\subseteq {\cal S}(v)
 \quad\hbox{or}\quad
 {\cal F}={\cal R}\cup
       \bigcup_{p\in{\cal P}}{\cal F}(p),
 \quad |{\cal P}|\le K^2,\quad |{\cal R}|\le K^3=o(\mu).}
                                                               \tag{0.6}
\]

The theorem is weighted and does not use width three.  Hence it certainly
applies after four-antichain pruning.

This is also the strongest conclusion of this kind available from edge
rank and intersection width alone.  A blown-up projective plane, with all
of its core targets placed on one chain, has pairwise intersection width
one, no common target, and

\[
 |{\cal F}|=\Theta(K^2\Delta _2),                   \tag{0.7}
\]

where \(\Delta _2\) is its maximum pair-star size.  With
\(\Delta _2=K\), it has \(\Theta(K^3)\) members, proving the cubic residual
sharp up to constants.  With the copies calibrated so that target and tag
degrees equal \(\mu\), it contains a clique of size \(\Theta(q\mu)\), for
an arbitrarily growing projective-plane order \(q\), although
\(\mu\gg K^2\).  This construction can be embedded in the Boolean protected
band and still has width one.

Therefore four-antichain pruning proves the useful structural statement
(0.6), but it does **not** prove a coefficient-one matching or colouring.
One still needs a geodesic-specific inequality controlling the total mass
of the pair-stars in the canonical cover, or the full matching-polytope
cut.  Width at most three supplies neither.

## 1. The four-antichain bad ratio

Write \(n=m-g=(1-o(1))m\).  Four incomparable cells in one monotone grid,
listed in increasing first coordinate and decreasing second coordinate,
have three positive successive gaps on each axis:

\[
 \alpha _1,\alpha _2,\alpha _3\ge1,
 \qquad
 \beta _1,\beta _2,\beta _3\ge1.                   \tag{1.1}
\]

Condition on one protected anchor.  The same stabilizer count used for the
three-antichain conflict bounds the relative degree of a competitor with
these six prescribed disjoint coordinate blocks by

\[
 {m^{o(1)}\over
  \binom n{\alpha _1,\alpha _2,\alpha _3}
  \binom n{\beta _1,\beta _2,\beta _3}}.            \tag{1.2}
\]

Here the \(m^{o(1)}\) is the protected-anchor load
\(\max_{q\le Q}\lambda_q\).  No full-grid rank is used.

For completeness, put

\[
 S_3(n,g)=
 \sum_{\substack{a,b,c\ge1\\a+b+c\le2g}}
 {1\over\binom n{a,b,c}}.                           \tag{1.3}
\]

Because \(g=o(n)\), throughout this sum every remaining ambient size is
\((1-o(1))n\).  The elementary estimate

\[
 \sum_{r=1}^{2g}{1\over\binom Nr}=O(N^{-1})         \tag{1.4}
\]

holds uniformly for \(N=(1-o(1))n\): the term \(r=1\) is \(1/N\), while
the remaining \(O(g)\) terms are at most
\(\binom N2^{-1}=O(N^{-2})\).  Using

\[
 \binom n{a,b,c}
 =\binom na\binom{n-a}b\binom{n-a-b}c               \tag{1.5}
\]

and applying (1.4) successively gives

\[
 S_3(n,g)=O(n^{-3}).                                 \tag{1.6}
\]

There are \(O(gQ)\) choices of the first protected cell and its signed
row data; after that, the six gaps determine the rectangle shape up to a
constant multiplicity.  Summing (1.2) by (1.6) on the two axes yields

\[
 {\Delta _4+1\over A}
 \le m^{o(1)}gQ S_3(n,g)^2
 \le m^{o(1)}{gQ\over m^6}
 =m^{-5+o(1)},                                      \tag{1.7}
\]

because \(gQ=m^{1+o(1)}\).  This proves (0.1) within exactly the same
protected-orbit hypotheses as the earlier three-antichain census.

Now (0.2) gives

\[
 L=m^{7/6+o(1)},qquad
 \mu={m^{5-o(1)}\over L}=m^{23/6-o(1)},             \tag{1.8}
\]

which is (0.3).  The suggested relative accuracy
\(\delta=m^{-2/3}\) is numerically compatible with simultaneous binomial
concentration, since

\[
 \delta^2\mu=m^{5/2-o(1)}\gg m,
 \qquad L^{-1}=m^{-7/6+o(1)}=o(\delta).             \tag{1.9}
\]

Equation (1.9) is an arithmetic audit, not a substitute for hereditary
residual propagation through later bites.  The EKR statements below need
only the retained degree scale, not such propagation.

## 2. Exact target-star/pair-star theorem

Let \({\cal F}\) be a finite family of labelled sets, each of cardinality
at most \(K\), and suppose

\[
 E\cap F\ne\varnothing\qquad(E,F\in{\cal F}).       \tag{2.1}
\]

Labels are allowed so the statement applies unchanged after denominator
clearing.  For a target \(x\) and a target pair \(p=\{x,y\}\), write

\[
 {\cal F}(x)=\{E\in{\cal F}:x\in E\},
 \qquad
 {\cal F}(p)=\{E\in{\cal F}:p\subseteq E\}.         \tag{2.2}
\]

### Theorem 2.1 (canonical pair-star cover)

At least one of the following conclusions holds.

1. There is a target \(x\) with \({\cal F}={\cal F}(x)\).
2. There is a collection \({\cal P}\) of at most \(K^2\) target pairs such
   that
   \[
    {\cal F}\subseteq\bigcup_{p\in{\cal P}}{\cal F}(p). \tag{2.3}
   \]

The second conclusion holds whenever \(\bigcap_{E\in{\cal F}}E\) is
empty.

#### Proof

Fix \(A\in{\cal F}\).  If the total intersection is nonempty, the first
conclusion holds.  Otherwise, for every \(x\in A\), choose
\(B_x\in{\cal F}\) with \(x\notin B_x\), and put

\[
 {\cal P}=\{\{x,y\}:x\in A,\ y\in B_x\}.            \tag{2.4}
\]

Then \(|{\cal P}|\le\sum_{x\in A}|B_x|\le K^2\).
Given \(E\in{\cal F}\), choose \(x\in E\cap A\).  Since
\(E\cap B_x\ne\varnothing\), choose \(y\in E\cap B_x\).  The choice of
\(B_x\) gives \(y\ne x\), and hence
\(\{x,y\}\subseteq E\).  Thus \(E\) lies in the pair-star indexed by
\(\{x,y\}\in{\cal P}\).  This proves (2.3). \(\square\)

The assertion is independent of every order placed on the target set.  In
particular, width at most three does not strengthen its proof.

In particular, if

\[
 \Delta _2({\cal F})=
 \max_{x\ne y}|{\cal F}(\{x,y\})|,
\]

then every no-common-target intersecting family satisfies the exact
rank--codegree bound

\[
 \boxed{|{\cal F}|\le K^2\Delta _2({\cal F}).}      \tag{2.4a}
\]

The projective-plane blow-up in Section 3 shows that the factor \(K^2\)
has the correct order even when every pairwise intersection has width one.

### Theorem 2.2 (weighted threshold form)

Give the members of \({\cal F}\) arbitrary weights \(w_E\ge0\), and write

\[
 w({\cal A})=\sum_{E\in{\cal A}}w_E.                \tag{2.5}
\]

If \({\cal F}\) has empty total intersection, then for every \(b\ge0\)
there is a set \({\cal P}_b\) of at most \(K^2\) pairs such that

\[
 w({\cal F}(p))>b\quad(p\in{\cal P}_b),             \tag{2.6}
\]

and

\[
 \boxed{
 w\left({\cal F}\setminus
       \bigcup_{p\in{\cal P}_b}{\cal F}(p)\right)
 \le K^2b.}                                         \tag{2.7}
\]

#### Proof

Use the canonical collection \({\cal P}\) from Theorem 2.1 and retain in
\({\cal P}_b\) just the pairs whose pair-star has weight greater than
\(b\).  Every member left outside their union is covered by at least one
of the remaining, light pairs in \({\cal P}\).  Therefore its total
weight is at most

\[
 \sum_{\substack{p\in{\cal P}\\w({\cal F}(p))\le b}}
 w({\cal F}(p))
 \le |{\cal P}|b\le K^2b.                           \tag{2.8}
\]

Multiple counting only makes the upper bound larger. \(\square\)

Taking unit weights and \(b=K\) proves (0.6).  At the new pruning scale,

\[
 |{\cal R}|\le K^3=m^{3+o(1)}
 =m^{-5/6+o(1)}\mu=o(\mu),                          \tag{2.9}
\]

and \(|{\cal P}_K|\le K^2=o(\mu)\).  Equivalently, every
\(\Omega(\mu)\)-sized intersecting family with no common target contains
a pair-star of size at least

\[
 {|{\cal F}|\over K^2}.                             \tag{2.10}
\]

This is the precise EKR gain supplied by \(\mu\gg K^3\).  Merely saying
\(\mu\gg K^2\) misses the useful cubic residual in (2.9).

There is a terminological trap here.  Every intersecting family is already
covered by the at most \(K\) target-stars centred at the members of one
fixed edge.  Also, a pair-star is contained in either of its endpoint
target-stars.  Thus an unqualified ``small target-star/pair-star cover''
is automatic and has no colouring content.  The nontrivial statement is
the one-target-star alternative followed by the heavy-pair decomposition
(2.7).

## 3. Sharpness: a width-one projective-plane blow-up

Let \(\Pi\) be a projective plane of prime-power order \(q\).  It has

\[
 v=q^2+q+1                                           \tag{3.1}
\]

points and the same number of lines; every line has \(q+1\) points, every
point lies on \(q+1\) lines, and two lines meet in exactly one point.
Place all \(v\) point-targets in one total chain.

Fix integers \(K\ge q+2\) and \(R\ge1\).  For every line \(\ell\) and
every \(i\in[R]\), make a distinct support

\[
 E_{\ell,i}=\ell\mathbin{\dot\cup}P_{\ell,i},
 \qquad |P_{\ell,i}|=K-q-1,                         \tag{3.2}
\]

where all padding sets are private and mutually disjoint.  Let
\({\cal F}=\{E_{\ell,i}\}\).

### Proposition 3.1 (sharp EKR obstruction)

The family \({\cal F}\) has all of the following properties.

1. It is pairwise intersecting and has no common target.
2. Every two supports have intersection-poset width one.
3. Its maximum pair-star size is
   \[
    \Delta _2({\cal F})=R.                          \tag{3.3}
   \]
4. Its size is
   \[
    |{\cal F}|=R(q^2+q+1).                          \tag{3.4}
   \]

#### Proof

Two supports belonging to different lines share the unique projective
point at which those lines meet.  Two supports belonging to the same line
share exactly the \(q+1\) point-targets of that line.  Those targets all
lie on the chosen total chain, so both kinds of intersection have width
one.  No point lies on every projective line, and padding is private, so
the total intersection is empty.  A pair of distinct projective points
determines a unique line and is contained in its \(R\) copies; every pair
involving padding lies in at most one support.  This proves (3.3), and
(3.4) is immediate. \(\square\)

Choose \(q=\Theta(K)\).  Then

\[
 |{\cal F}|=\Theta(K^2\Delta _2({\cal F})),          \tag{3.5}
\]

so the \(K^2\) factor in Theorem 2.1 and the consequent bound
\(K^2b\) in Theorem 2.2 cannot be replaced by \(o(K^2)\) under a
width-three hypothesis.  In particular, taking \(R=K\) gives a width-one
family of size \(\Theta(K^3)\) in which every pair-star has size at most
\(K\).  This proves that the residual order in (2.9) is sharp.

## 4. Degree-calibrated failure of coefficient one

The preceding example can satisfy the degree lower-bound scale as well.
Put

\[
 \mu=R(q+1).                                        \tag{4.1}
\]

Each projective point then has degree exactly \(\mu\) in \({\cal F}\).
Give every core support \(E_{\ell,i}\) its own tag.  Above that tag add
\(\mu-1\) filler supports, each having \(K\) globally private protected
targets.  The resulting tagged hypergraph \({\cal H}\) has

\[
 d_{\cal H}(\tau)=\mu\quad\hbox{for every tag},
 \qquad
 d_{\cal H}(x)\le\mu\quad\hbox{for every target}.   \tag{4.2}
\]

Every protected claim set has size \(K\), and every pairwise protected
intersection still has width at most one.  The core supports use distinct
tags and are pairwise target-intersecting, hence form a clique of size

\[
 |{\cal F}|=Rv
 =\mu\,{q^2+q+1\over q+1}
 =\mu\left(q+{1\over q+1}\right).                  \tag{4.3}
\]

Consequently

\[
 \chi'({\cal H})\ge |{\cal F}|
 =\left(q+{1\over q+1}\right)\mu,                  \tag{4.4}
\]

although the maximum tag/target degree is \(\mu\).  Taking \(R\) so that
\(\mu\gg K^2\) does not change a single intersection property.

The minimum number of target-stars and pair-stars needed to cover the core
clique is exactly \(q+1\).  Indeed, a target-star covers at most
\(R(q+1)=\mu\) core supports, and a pair-star covers at most \(R\), so
fewer than

\[
 \left\lceil {Rv\over\mu}\right\rceil=q+1           \tag{4.5}
\]

such stars cannot cover \({\cal F}\).  Conversely, the \(q+1\) point
targets on any one projective line meet every line of \(\Pi\), so their
target-stars cover all core supports.  Thus even the optimal mixed cover
has unbounded size.

### Boolean-band realization of the obstruction data

This counterexample need not use an abstract target order.  In the
truncated regime choose a power of two \(q\) with

\[
 q=\Theta(\sqrt Q)=m^{1/4+o(1)},
 \qquad q^2+q+1\le2Q+1.                             \tag{4.6}
\]

Map the projective points injectively to consecutive members of one
maximal Boolean chain at ranks in \([m-Q,m+Q]\).  There are exponentially
many other Boolean targets in the band, so all polynomially many padding
and filler targets can be chosen distinct.  Take \(K=m^{1+o(1)}\) and
choose \(R\) so that

\[
 R(q+1)=m^{23/6-o(1)}.                              \tag{4.7}
\]

Then the construction has the proposed \(K\), \(\mu\), and protected
Boolean ranks, survives four-antichain pruning with room to spare, and its
clique ratio in (4.4) tends to infinity.

This is an incidence counterexample to deductions from width, rank, and
degree alone.  It is not a claim that arbitrary projective-plane supports
are realizable by return-free geodesic chunks.  Precisely that missing
geodesic incidence information must be used by any positive theorem.

## 5. The exact remaining geodesic gate

For the canonical witnesses \(A\) and \(B_x\) in Theorem 2.1, every
non-star intersecting family obeys the sharper, nonuniform bound

\[
 w({\cal F})
 \le
 \sum_{x\in A}\sum_{y\in B_x}w({\cal F}(x,y)).      \tag{5.1}
\]

Thus a sufficient geodesic EKR gate is the joint pair-load estimate

\[
 \boxed{
 \sup_{A,(B_x)}
 \sum_{x\in A}\sum_{y\in B_x}w({\cal H}(x,y))
 =o(\mu),}                                          \tag{5.2}
\]

with the supremum restricted to legal intersecting witness systems.
A cruder sufficient condition is

\[
 \max_{x\ne y}w({\cal H}(x,y))
 =o(\mu/K^2),                                       \tag{5.3}
\]

but (5.3) is likely too strong for adjacent nested targets.  Formula
(5.2) is the correct place to exploit the exact grid-intersection shapes,
phase chronology, and cover-neighbour sparsity; multiplying a worst
pair-codegree by \(K^2\) discards that information.

Even (5.2) controls only clique-type intersecting obstructions.  A full
coefficient-one decomposition must also exclude weighted odd systems and
the other matching-polytope cuts identified in the width-two multicover
audit.  Four-antichain pruning improves the available degree and gives the
sharp structural reduction (0.6), but it does not by itself close either
gate.
