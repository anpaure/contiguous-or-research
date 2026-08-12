# Exact orbit recoloring: run factorization and the sparse-edge cut

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Let \(G=S_{2m}\), let \(\mathcal B\) be an ambient
floor/ceiling-balanced top-rooted full-flag resolution, and let

\[
 T=M\binom{2m}{M},\qquad M=m+H.
\tag{0.1}
\]

Assume the calibrated regime \(T\le W=\binom{2m}{m}\); when asymptotic
estimates are invoked below, assume also \(T=(1-o(1))W\), \(Q=o(H)\),
and \(H=o(m)\).

For completeness, the usual least-crossing calibration implies the stated
estimate with an explicit error.  If

\[
 \lambda_h=\frac{W}{\binom{2m}{m-h}}
\]

and \(H\) is least with \(\lambda_H\ge M=m+H\), then
\(\lambda_{H-1}<M-1\) and

\[
 \frac{\lambda_H}{\lambda_{H-1}}
 =\frac{m+H}{m-H+1}.
\]

Therefore

\[
 1\ge\frac TW=\frac M{\lambda_H}
 >\frac{m-H+1}{M-1}
 =1-O(H/m),
\tag{0.1a}
\]

which proves \(T=(1-O(H/m))W\) whenever \(H=o(m)\).

For a top \(U\), let \(p_U^*(\mathcal B)\) be the minimum number of
legal radius-\(Q\) rotor paths needed to cover the \(M\) columns of
\(\mathcal B\) rooted at \(U\), and put

\[
 P(\mathcal B)=\sum_U p_U^*(\mathcal B).
\tag{0.2}
\]

This note proves the exact recoloring theorem

\[
 \boxed{R_{\min}(G\mathcal B)=|G|P(\mathcal B).}
\tag{0.3}
\]

Here \(R_{\min}\) is the minimum total number of maximal constant-color
runs over every legal successor permutation of the fully symmetrized
column multiset, while each color retains exactly the columns of one
coordinate image \(g\mathcal B\).

There is an equally exact version allowing arbitrary reassignment of
colors subject only to the ambient rank quotas.  The full coordinate
orbit of **every** indexed \(T\)-column family is the same universal
full-flag multiset.  If \(\mathfrak B\) denotes all ambient
floor/ceiling-balanced resolutions, then

\[
 \boxed{
 R_{\min}^{\rm quota}
 =|G|\min_{\mathcal A\in\mathfrak B}P(\mathcal A).}
\tag{0.4}
\]

Consequently a quota-preserving recoloring with

\[
 R=o(|G|W/Q)
\tag{0.5}
\]

exists if and only if there is already one ambient balanced resolution
\(\mathcal A\) with

\[
 P(\mathcal A)=o(W/Q).
\tag{0.6}
\]

Thus symmetrization causes no additional integral loss, but recoloring
cannot bypass the original one-resolution path-factor gate.

A second theorem explains why the sparse cycle factor used in the first
double-resolution proof is maximally hostile to recoloring.  If
\(E(\mathcal B)\) is the number of ordered legal pairs already present in
\(\mathcal B\), then the two endpoints of any fixed ambient rotor edge
coexist in exactly an \(E/(TD)\) fraction of their orbit colors, where

\[
 D=(m-Q)(H-Q).
\tag{0.7}
\]

In fact middle-owner injectivity gives the sharper bound

\[
 E\le T(H-Q),
\tag{0.8}
\]

so this fraction is at most \(1/(m-Q)\).  Any symmetrized transition
factor whose outgoing support per state is \(o(m-Q)\) must therefore
change color on \((1-o(1))|G|W\) edges.  The exact completion behind
(0.3) succeeds only by rebuilding the transition support from the
per-color path matchings.

No coefficient-one conclusion is claimed: (0.6) remains open.

## 1. Occurrence path count at one top

Resolve every full flag column to its quotient state

\[
 \omega=(L;z_1,\ldots,z_{2Q};R),
 \qquad |L|=m-Q,\quad |R|=H-Q.
\tag{1.1}
\]

At one top \(U\), split the \(M\) indexed column occurrences into a left
and a right copy and join two occurrences when their resolved states form
a legal rotor edge.  A partial matching \(P\) becomes, after identifying
the two copies of every occurrence, a directed graph whose components are
paths, cycles, and isolated vertices.  Let \(c(P)\) be its number of
cycle components.

The number of components after cutting one edge in every cycle is exactly

\[
 p(P)=M-|P|+c(P).
\tag{1.2}
\]

Indeed every path or isolated component has one more vertex than edge,
whereas every cycle has equally many.  Cutting one edge from each cycle
changes neither the right side of (1.2) nor the number of resulting path
components.  Therefore

\[
 p_U^*(\mathcal B)
 =\min_P\{M-|P|+c(P)\}
\tag{1.3}
\]

is exactly the minimum legal occurrence-path-cover number at \(U\).
Repeated resolved states, if any, remain distinct indexed occurrences.

## 2. Orbiting minimizing partial matchings

Choose at every top \(U\) a partial matching \(P_U\) attaining (1.3).
For every color \(g\in G\), place the relabelled matching \(gP_U\) on
the columns of \(g\mathcal B\) over the top \(gU\).  Their union
\(P_0\) is a legal partial matching of the complete colored orbit
multiset.  Its monochromatic component count is exactly

\[
 |G|\sum_U p_U^*(\mathcal B)=|G|P(\mathcal B).
\tag{2.1}
\]

It remains to match its unused left and right occurrences.  Put

\[
 r=\sum_U(M-|P_U|).
\tag{2.2}
\]

This is both the number of unused left occurrences and the number of
unused right occurrences in the base family.

Let

\[
 K=(m-H)!(m-Q)!(H-Q)!
\tag{2.3}
\]

be the stabilizer size of one exact ambient quotient state.  Fix such a
state \(s\).  Every indexed unused base occurrence is sent to \(s\) by
exactly \(K\) coordinate permutations.  Counting occurrences with their
indices, whether or not two resolved states coincide, gives

\[
 \boxed{
 \#\{\text{unused left occurrences of type }s\}
 =\#\{\text{unused right occurrences of type }s\}=rK.}
\tag{2.4}
\]

Thus the two residual marginals are not merely equinumerous: they are
identical and uniform on exact quotient states.

### Lemma 2.1 (uniform residual completion)

The residual occurrences admit an integral legal perfect matching.

#### Proof

At a fixed top, the bipartite rotor graph on exact state types is
\(D\)-regular, with \(D\) as in (0.7).  Hence Hall's theorem gives one
perfect matching of its state types.  Take \(rK\) labelled copies of this
matching.  Equation (2.4) permits independent typewise bijections from
its left and right copies to the actual residual occurrences.  Doing this
at every top gives the required integral matching. \(\square\)

Add this residual matching to \(P_0\), obtaining a legal successor
permutation \(\Sigma\) of every colored occurrence.  A residual edge
whose endpoints have different colors does not alter the monochromatic
subgraphs.  A residual edge whose endpoints have the same color can only
join two monochromatic path components or close one path into a cycle; it
cannot increase their number.  Therefore

\[
 R(\Sigma)\le |G|P(\mathcal B).
\tag{2.5}
\]

## 3. The reverse component inequality

Consider any legal successor permutation \(\Sigma\) of the same colored
orbit multiset.  Fix a color \(g\) and a top \(V\).  Retain only those
successor edges whose two endpoints both have color \(g\).  They form a
partial legal matching \(P_{g,V}\) on the \(M\) occurrences of that
table.

Every maximal constant-color run of \(\Sigma\) is one path component of
some \(P_{g,U}\).  If a complete successor cycle is monochromatic, it is
one cycle component and counts as one run.  Hence the total run count is
exactly the sum of the component counts

\[
 R(\Sigma)
 =\sum_{g\in G}\sum_V
  \bigl(M-|P_{g,V}|+c(P_{g,V})\bigr).
\tag{3.1}
\]

By (1.3), the inner summand is at least
\(p_{g^{-1}V}^*(\mathcal B)\).  Since \(V\mapsto g^{-1}V\) permutes the
top layer, summing gives

\[
 R(\Sigma)\ge|G|P(\mathcal B).
\tag{3.2}
\]

Combining (2.5) and (3.2) proves (0.3).  Notice that the residual
completion is exact at the occurrence level; it uses no rational scaling
beyond the coordinate orbit already present.

## 4. The universal full-flag orbit

A full top-rooted column through ranks \(m-H,\ldots,M\) consists of:

* its bottom set of size \(m-H\);
* an ordered list of the \(2H\) labels added on the way to its top; and
* the ambient complement of that top, also of size \(m-H\).

The coordinate group \(G\) is transitive on these full columns.  The
stabilizer of one column has size

\[
 J=((m-H)!)^2,
\tag{4.1}
\]

because only the bottom and ambient-complement labels may be permuted.

### Lemma 4.1 (orbit independence of the resolution)

The full coordinate orbit of any indexed family of exactly \(T\) full
columns contains every full-column type with multiplicity exactly

\[
 \boxed{TJ.}
\tag{4.2}
\]

#### Proof

Fix one indexed column \(c\) and one target full-column type \(f\).  The
permutations sending \(c\) to \(f\) form a coset of the stabilizer of
\(f\), so there are exactly \(J\).  Sum over the \(T\) indexed columns.
\(\square\)

Call the multiset in Lemma 4.1 the universal \(T\)-column orbit
\(\mathscr F_T\).  It is independent of the starting resolution, even
before quotienting the columns to radius \(Q\).

Now color \(\mathscr F_T\) by \(|G|\) colors, each required to form an
ambient floor/ceiling-balanced resolution in \(\mathfrak B\), and choose
any legal successor permutation.  Applying Section 3 separately to its
color classes gives

\[
 R\ge\sum_{g\in G}P(\mathcal A_g)
 \ge |G|\min_{\mathcal A\in\mathfrak B}P(\mathcal A).
\tag{4.3}
\]

Conversely, take a minimizing \(\mathcal A_\star\in\mathfrak B\).  Its
full coordinate orbit is \(\mathscr F_T\) by Lemma 4.1, and Sections
2--3 give a coloring and successor permutation with exactly

\[
 |G|P(\mathcal A_\star)
\]

runs.  This proves (0.4).  Since the family is finite, the minimum is
attained.

Equations (0.5)--(0.6) are now immediate.  A low-run quota-preserving
recoloring and a low-path-count ambient balanced resolution are not two
different routes; they are exactly the same finite optimization after
orbiting.

## 5. Exact color overlap on one rotor edge

The preceding theorem allows the transition factor to be rebuilt.  We
now audit the more restrictive idea of keeping a sparse projected rotor
factor and merely reassigning its existing orbit colors.

The balanced resolution has distinct middle owners because its middle
load is at most one.  Hence its resolved state occurrences are distinct.
Let

\[
 E=E(\mathcal B)
 :=\#\{(c,d):c,d\in\mathcal B,\ \rho(c)\to\rho(d)\}
\tag{5.1}
\]

be its number of ordered legal pairs.  Rotor edges preserve tops, and
there are only \(M\) selected columns at one top, so

\[
 E\le T(M-1).
\tag{5.2}
\]

There is a substantially sharper bound.  The middle owner of

\[
 \omega=(L;z_1,\ldots,z_{2Q};R)
\]

is

\[
 X(\omega)=L\cup\{z_1,\ldots,z_Q\}.
\tag{5.2a}
\]

If \(\omega\to\eta\) uses \(x\in L\) and \(y\in R\), then

\[
 X(\eta)
 =(L-x+y)\cup\{x,z_1,\ldots,z_{Q-1}\}
 =X(\omega)-z_Q+y.
\tag{5.2b}
\]

For fixed \(\omega\), different selected targets therefore have different
values of \(y\): two targets with the same \(y\) would have the same
middle owner, whereas every middle owner occurs at most once in
\(\mathcal B\).  Hence the selected outdegree of every base state is at
most \(|R|=H-Q\), and

\[
 \boxed{E\le T(H-Q).}
\tag{5.2c}
\]

The stabilizer of a directed rotor edge has size

\[
 K_{\rm e}
 =(m-H)!(m-Q-1)!(H-Q-1)!
 =\frac KD.
\tag{5.3}
\]

Indeed the state stabilizer may permute its \(L\)- and \(R\)-blocks; an
edge additionally fixes the chosen departure \(x\in L\) and arrival
\(y\in R\).  The group \(G\) is transitive on directed rotor edges.

Fix an ambient edge \(e=(s,t)\).  For each ordered legal base pair
\((c,d)\), exactly \(K/D\) permutations send
\((\rho(c),\rho(d))\) to \((s,t)\).  Conversely every color containing
both \(s\) and \(t\) determines its unique preimage pair, because the
base states are distinct.  Thus

\[
 \boxed{
 J_e:=\#\{g:s,t\in g\mathcal B\}=\frac{EK}{D}.}
\tag{5.4}
\]

Every state belongs to exactly

\[
 h=TK
\tag{5.5}
\]

orbit colors, and therefore

\[
 \boxed{
 \frac{J_e}{h}=\frac{E}{TD}
 \le \frac{H-Q}{(m-Q)(H-Q)}
 =\frac1{m-Q}.}
\tag{5.6}
\]

At the calibrated scales \(Q=o(m)\),

\[
 \frac{J_e}{h}\le\frac1{m-Q}=(1+o(1))\frac1m=o(1).
\tag{5.7}
\]

This uniform overlap count is independent of the chosen ambient edge.

## 6. Sparse projected support forces almost all edges to switch

Consider any legal successor permutation of the orbit occurrences whose
projection, at a state \(s\), uses only \(\kappa_s\) distinct successor
state types.  There are \(h\) outgoing occurrence edges above \(s\).
For each projected edge type, at most \(J_e=EK/D\) of those edges can be
monochromatic, because only that many colors contain both endpoints.
Consequently the number \(X\) of color-change edges satisfies the exact
cut

\[
 \boxed{
 X\ge\sum_{s\in\mathscr S}
       \left(h-\kappa_s\frac{EK}{D}\right)_+.}
\tag{6.1}
\]

In particular, if

\[
 \max_s\kappa_s=o(m-Q),
\tag{6.2}
\]

then (5.2c) gives

\[
 X\ge(1-o(1))|\mathscr S|h
 =(1-o(1))|G|T.
\tag{6.3}
\]

The number of constant-color runs is at least \(X\): on a
nonmonochromatic directed cycle the run count equals the number of color
changes, while a monochromatic cycle only adds one run.  Since
\(T=W-o(W)\), (6.3) yields

\[
 R\ge(1-o(1))|G|W,
\tag{6.4}
\]

far above the target \(o(|G|W/Q)\).

The original double-resolution factor takes \(h\) copies of one fixed
successor permutation of the exact state types, so \(\kappa_s=1\) and is
covered by (6.2).  More exactly, it satisfies

\[
 R\ge X\ge |G|T\left(1-\frac1{m-Q}\right).
\tag{6.5}
\]

Thus its cycle colors cannot be repaired by a label-only local flow.  The
completion in Section 2 escapes (6.1) by changing the projected transition
factor itself and using the unmatched uniform reservoir.

There is also a necessary support scale for *any* projected factor.  Put

\[
 \overline\kappa
 =\frac1{|\mathscr S|}\sum_{s\in\mathscr S}\kappa_s.
\tag{6.6}
\]

Dropping the positive parts in (6.1) and using
\(|\mathscr S|h=|G|T\) gives

\[
 R\ge X
 \ge |G|T\left(1-\overline\kappa\frac{E}{TD}\right).
\tag{6.7}
\]

Since \(T/W=1-o(1)\), the target
\(R=o(|G|W/Q)\) can hold only if

\[
 \overline\kappa\frac{E}{TD}\ge1-o(1/Q).
\tag{6.8}
\]

If \(E=0\), (6.7) already gives \(R\ge |G|T\), so the target is
impossible.  If \(E>0\), consequently

\[
 \boxed{
 \overline\kappa
 \ge \frac{TD}{E}\bigl(1-o(1/Q)\bigr)
 \ge (m-Q)\bigl(1-o(1/Q)\bigr).}
\tag{6.9}
\]

Thus a successful label-only flow cannot be a bounded-phase or even an
\(o(m)\)-phase perturbation.  It must spread the outgoing copies of an
average exact state over essentially \(m-Q\) different successor state
types.  This support requirement is independent of the anticycle example
and holds for every ambient balanced base resolution.

## 7. Exact surviving gate

The recoloring lane is now exhausted in the following precise sense.

* For fixed orbit colors, its optimum run count is exactly
  \(|G|P(\mathcal B)\).
* If all color labels may be reassigned while retaining the ambient
  floor/ceiling quotas, the optimum is exactly
  \(|G|\min_{\mathcal A\in\mathfrak B}P(\mathcal A)\).
* Keeping the sparse projected rotor factor and changing labels only is
  impossible at the required scale by (6.1)--(6.4).

Therefore a coefficient-one proof through this architecture must produce
an ambient balanced resolution \(\mathcal A\) with

\[
 \boxed{\sum_U p_U^*(\mathcal A)=o(W/Q).}
\tag{7.1}
\]

Successor Hall at every top supplies cycle covers but does not alone bound
the number of cycles; the whole-transversal cycle-cylinder condition from
`MATH_ATTACK_TRP_WHOLE_TRANSVERSAL_STATIONARY_ROTOR_COUPLING_20260725.md`
is one sufficient strengthening.  No orbit recoloring theorem can replace
(7.1), because (0.4) shows that doing so would already construct the
required one-resolution factor.
