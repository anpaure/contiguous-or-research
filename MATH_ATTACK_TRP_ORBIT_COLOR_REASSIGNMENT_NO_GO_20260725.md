# TRP orbit-color reassignment: an exact run theorem and a transition-diversity cut

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad
 T=M\binom{2m}{M},\qquad
 D=(m-Q)(H-Q),
\tag{0.1}
\]

and let \(\mathcal B\) be one integral ambient
floor/ceiling-balanced top-rooted full-flag resolution, with exactly
\(M\) columns at every rank-\(M\) top.  Resolve its columns to
radius-\(Q\) rotor states.  Let \(G=S_{2m}\), and regard the relabelled
families \(g\mathcal B\), indexed by \(g\in G\), as distinct colors.

The fully symmetrized occurrence multiset has \(h\) copies of every
exact rotor state.  The symmetrized double-resolution theorem factors it
by taking \(h\) copies of any legal successor permutation of the exact
state space.  This note solves the color-reassignment problem on every
such factor, up to an immaterial additive term.

Let \(E=E(\mathcal B)\) be the number of ordered pairs of columns of
\(\mathcal B\) whose resolved states form a legal rotor edge.  If
\(R_{\min}\) is the least possible total number of cyclic monochromatic
runs after arbitrary typewise reassignment of the exact color
occurrences, then

\[
 \boxed{
 |\mathscr S|(h-J)
 \le R_{\min}\le
 |\mathscr S|(h-J)+\kappa J,}
 \qquad
 \boxed{\frac Jh=\frac{E}{TD}.}
\tag{0.2}
\]

Here \(\mathscr S\) is the global exact state space, \(\kappa\) is the
number of cycles of the chosen state successor permutation, and
\(J\) is the number of colors allowed simultaneously at the two ends
of any fixed legal rotor edge.  Since every top contains only \(M\)
selected states,

\[
 E\le T(M-1),\qquad
 \frac Jh\le\frac{M-1}{(m-Q)(H-Q)}.
\tag{0.3}
\]

Consequently, whenever

\[
 H=o(m),\qquad Q=o(m),\qquad H-Q\longrightarrow\infty,
\tag{0.4}
\]

one has, uniformly over the balanced resolution and over the legal state
successor permutation,

\[
 \boxed{R_{\min}=(1-o(1))|G|T.}
\tag{0.5}
\]

At the calibrated first crossing, \(T=(1-o(1))W\).  If also
\(Q\to\infty\), (0.5) is incompatible with the required

\[
 R=o(|G|W/Q).
\tag{0.6}
\]

Thus low-run color reassignment of the copied state-cycle factor is
rigorously closed: almost every dynamic edge must change color.  This
obstruction applies to every ambient-balanced \(\mathcal B\), not just
to the earlier anticycle table.

There is one precise escape.  A more general color-blind rotor
circulation can avoid the obstruction only by using
\(\Omega(H-Q)\) distinct successor types per exact source state on
average.  In particular, no convex combination of \(o(H-Q)\) fixed
state successor permutations can have the desired run count.  Such a
broad-support circulation is no longer a recoloring of the copied-cycle
factor; it is the original joint Hall/transport construction in another
form.

No coefficient-one conclusion is claimed.

## 1. States, colors, and distinctness

For a top \(U\in\binom{[2m]}M\), a radius-\(Q\) state is

\[
 s=(U;L;z_1,\ldots,z_{2Q};R),
 \qquad |L|=m-Q,\quad |R|=H-Q,
\tag{1.1}
\]

where the displayed parts partition \(U\).  A legal update chooses
\(x\in L\) and \(y\in R\) and sends this state to

\[
 (U;L-x+y;x,z_1,\ldots,z_{2Q-1};R-y+z_{2Q}).
\tag{1.2}
\]

Thus every state has exactly \(D=(m-Q)(H-Q)\) legal successors.
Write \(\mathscr S\) for the state space over all tops.

The middle load of \(\mathcal B\) is at most one, because
\(T/W\le1\) at the calibrated crossing.  Two columns with the same
resolved state have the same middle flag.  Hence all \(T\) resolved
states selected by \(\mathcal B\) are distinct.  The same is true in
every color \(g\mathcal B\).

For \(s\in\mathscr S\), define its set of allowed indexed colors by

\[
 \mathcal C(s)=\{g\in G:s\text{ is selected by }g\mathcal B\}.
\tag{1.3}
\]

Even if two relabellings happen to give the same unlabelled resolution,
their elements of \(G\) are retained as distinct colors.

The stabilizer of one exact state has order

\[
 K=(m-H)!(m-Q)!(H-Q)!.
\tag{1.4}
\]

For each of the \(T\) indexed columns of \(\mathcal B\), exactly \(K\)
permutations send its resolved state to a prescribed \(s\).  Distinctness
then gives

\[
 \boxed{|\mathcal C(s)|=h:=TK.}
\tag{1.5}
\]

Also, by orbit--stabilizer,

\[
 |\mathscr S|K=|G|,
 \qquad
 |\mathscr S|h=|G|T.
\tag{1.6}
\]

## 2. Exact common-color count on a rotor edge

Let

\[
 E=\#\{(c,d)\in\mathcal B^2:\rho(c)\longrightarrow\rho(d)\},
\tag{2.1}
\]

where columns are indexed and the arrow is the legal rotor relation.
There are no diagonal terms, since a legal rotor update cannot fix a
state with distinct queue entries.

### Lemma 2.1 (one edge orbit and its stabilizer)

The action of \(G\) is transitive on directed legal rotor edges.  The
stabilizer of such an edge has order \(K/D\).

#### Proof

A directed edge is a state together with a choice \((x,y)\in L\times R\).
After mapping its source state to any other source state, permutations of
the unordered \(L\)- and \(R\)-blocks map \((x,y)\) to any prescribed
choice \((x',y')\).  Hence all directed rotor edges form one orbit.

An edge stabilizer fixes the ordered queue pointwise, fixes the chosen
\(x\) and \(y\), and may permute independently the ambient complement of
the top, \(L\setminus\{x\}\), and \(R\setminus\{y\}\).  Its order is

\[
 (m-H)!(m-Q-1)!(H-Q-1)!=\frac KD.
\]

Conversely all these permutations fix both endpoints, so this is the
full stabilizer. \(\square\)

### Lemma 2.2 (exact adjacent-color overlap)

For every legal edge \(s\to t\),

\[
 \boxed{
 |\mathcal C(s)\cap\mathcal C(t)|
 =J:=\frac{EK}{D},
 \qquad
 \frac Jh=\frac{E}{TD}.}
\tag{2.2}
\]

#### Proof

Count triples \((g,c,d)\) for which \(c,d\) are columns of
\(\mathcal B\) and

\[
 g\rho(c)=s,\qquad g\rho(d)=t.
\tag{2.3}
\]

Only the \(E\) legal ordered pairs can occur.  For each such pair, the
permutations satisfying (2.3) form a coset of the directed-edge
stabilizer, and hence number \(K/D\).  The triple count is therefore
\(EK/D\).

For fixed \(g\), distinctness of the resolved states in \(g\mathcal B\)
shows that there is at most one pair \((c,d)\) in (2.3).  Thus the triple
count is exactly the number of indexed colors containing both endpoints.
This proves the first identity.  Divide by \(h=TK\) for the second.
\(\square\)

The count also proves automatically that \(EK/D\) is an integer.

### Lemma 2.3 (universal sparsity)

One has

\[
 E\le T(M-1).
\tag{2.4}
\]

#### Proof

Rotor edges preserve the top.  At each top, \(\mathcal B\) selects
exactly \(M\) distinct states.  For each selected source there are at
most \(M-1\) other selected states which could be its target.  Summing
over the \(T\) sources gives (2.4). \(\square\)

Combining Lemmas 2.2 and 2.3 gives (0.3).  Notice that no property of the
floor/ceiling quotas beyond distinct middle ownership was used.

## 3. The fixed-cycle recoloring theorem

Let \(\phi\) be any permutation of \(\mathscr S\) such that
\(s\to\phi(s)\) is legal for every state.  Take \(h\) labelled copies
of every cycle of \(\phi\).  A **typewise exact recoloring** is a family
of bijections

\[
 \chi_s:[h]\longrightarrow\mathcal C(s)
 \qquad(s\in\mathscr S).
\tag{3.1}
\]

Thus every full-column occurrence in every color is used exactly once.
In particular each color retains its original \(M\) columns at every top
and all its original ambient floor/ceiling quotas.

On the copied directed cycles, let \(R(\chi)\) be the total number of
maximal cyclic constant-color runs, with an entirely monochromatic cycle
counted as one run.  Put \(R_{\min}=\min_\chi R(\chi)\), and let
\(\kappa\) be the number of cycles of \(\phi\).

### Theorem 3.1 (exact run sandwich)

\[
 \boxed{
 |\mathscr S|(h-J)
 \le R_{\min}
 \le |\mathscr S|(h-J)+\kappa J.}
\tag{3.2}
\]

#### Proof: lower bound

Fix a state edge \(s\to t=\phi(s)\).  Its \(h\) copied edges can be
monochromatic only in colors belonging to
\(\mathcal C(s)\cap\mathcal C(t)\).  Each such color occurs only once at
each endpoint, so at most \(J\) of the copied edges can be monochromatic.
At least \(h-J\) change color.  Summing over all \(|\mathscr S|\) state
edges gives at least \(|\mathscr S|(h-J)\) color-change edges.

On a nonmonochromatic directed cycle, the number of cyclic color runs is
exactly its number of color-change edges.  A monochromatic cycle has no
change edge and one run.  Hence total runs are at least total change
edges, proving the lower bound.

#### Proof: upper bound

Work independently on each state cycle

\[
 s_1\to s_2\to\cdots\to s_\ell\to s_1.
\]

Cut it between \(s_\ell\) and \(s_1\), and choose \(\chi_{s_1}\)
arbitrarily.  Having chosen \(\chi_{s_i}\), assign every color in
\(\mathcal C(s_i)\cap\mathcal C(s_{i+1})\) to the same copy at
\(s_{i+1}\).  These are \(J\) distinct colors on \(J\) distinct
copies.  Bijection between the remaining \(h-J\) colors and copies
completes \(\chi_{s_{i+1}}\).  Thus each of the \(\ell-1\) uncut
boundaries has exactly \(h-J\) color changes.

Along one cut-open copy, the number of linear constant-color intervals
is one plus its number of changes at the uncut boundaries.  Passing back
to the cyclic word cannot increase this number.  The total number of
cyclic runs over the \(h\) copies is therefore at most

\[
 h+(\ell-1)(h-J)
 =\ell(h-J)+J.
\]

Summing over all cycles gives

\[
 |\mathscr S|(h-J)+\kappa J,
\]

as required. \(\square\)

The lower and upper bounds differ by only \(\kappa J\).  In particular,
using \(\kappa\le|\mathscr S|\), (1.6), and Lemma 2.2,

\[
 1-\frac{E}{TD}
 \le
 \frac{R_{\min}}{|G|T}
 \le1.
\tag{3.3}
\]

By Lemma 2.3,

\[
 \frac{E}{TD}
 \le
 \frac{m+H-1}{(m-Q)(H-Q)}
 =\frac{1+o(1)}{H-Q}
\tag{3.4}
\]

under (0.4).  This proves (0.5).

At the calibrated first crossing \(T=(1-o(1))W\).  Therefore, if
\(Q\to\infty\),

\[
 \frac{R_{\min}}{|G|W/Q}\ge(1-o(1))Q\longrightarrow\infty.
\tag{3.5}
\]

This contradicts the low-total-run target (0.6), by a factor tending to
infinity.

## 4. Arbitrary rotor circulations require broad transition support

The preceding no-go concerns \(h\) copied cycles of one state
permutation.  We now state the exact condition which any more general
color-blind cycle factor must evade.

Let \(n_{s,t}\) be nonnegative integers on legal state edges, with

\[
 \sum_{t:s\to t}n_{s,t}=h,
 \qquad
 \sum_{s:s\to t}n_{s,t}=h.
\tag{4.1}
\]

Thus \(n\) is an integral stationary circulation on the uniform
\(h\)-fold state multicover and factors into occurrence-level rotor
cycles.  Put

\[
 d_s=\#\{t:n_{s,t}>0\}.
\tag{4.2}
\]

### Theorem 4.1 (edge-capacity and transition-diversity cut)

Under every typewise exact recoloring of this circulation, the number
\(X\) of color-change edges, and hence its run count \(R\), satisfy

\[
 \boxed{
 R\ge X\ge
 |\mathscr S|h-\sum_{s\to t}\min\{n_{s,t},J\}}
\tag{4.3}
\]

and consequently

\[
 \boxed{
 R\ge X\ge
 \sum_{s\in\mathscr S}(h-Jd_s)_+.}
\tag{4.4}
\]

If \(E>0\), then

\[
 \boxed{
 \frac1{|\mathscr S|}\sum_s d_s
 \ge
 \frac{TD}{E}
 \left(1-\frac{R}{|G|T}\right).}
\tag{4.5}
\]

#### Proof

On the \(n_{s,t}\) occurrences of one edge type, a monochromatic edge
can use only one of the \(J\) common colors, and each common color occurs
only once at either endpoint.  Hence at most
\(\min\{n_{s,t},J\}\) such edges are monochromatic.  There are
\(|\mathscr S|h\) edges in total, proving (4.3).  At one source,

\[
 \sum_{t:n_{s,t}>0}\min\{n_{s,t},J\}\le Jd_s.
\]

Since a source contributes a nonnegative number of changes, summing the
positive parts gives (4.4).

Finally the total number of monochromatic edges is at least
\(|\mathscr S|h-R\), because \(R\ge X\).  It is at most
\(J\sum_s d_s\).  Therefore

\[
 J\sum_s d_s\ge|\mathscr S|h-R.
\]

Use \(h/J=TD/E\) and \(|\mathscr S|h=|G|T\) to obtain (4.5).
\(\square\)

In particular, if \(R=o(|G|W/Q)\), calibrated \(T=(1-o(1))W\) gives

\[
 \frac1{|\mathscr S|}\sum_s d_s
 \ge(1-o(1))\frac{TD}{E}
 \ge(1-o(1))\frac{D}{M-1}.
\tag{4.6}
\]

Under (0.4), the final quantity is

\[
 \frac{D}{M-1}=(1+o(1))(H-Q).
\tag{4.7}
\]

Thus a low-run factor must use \((1-o(1))(H-Q)\) distinct legal
successor types per source on average.  If a circulation is a sum of
\(L\) state successor permutations, then \(d_s\le L\) for every source;
hence every construction with \(L=o(H-Q)\) is excluded.

## 5. The exact Hall-deficiency cut for an arbitrary circulation

There is a second, complementary obstruction which no choice of
color-blind circulation can evade.  Let \(S_{\mathcal B}\subset
\mathscr S\) be the selected state set of \(\mathcal B\).  In the
bipartite graph with a source and target copy of this set, retain just the
legal rotor edges.  Let \(\mu(\mathcal B)\) be its maximum matching size
and put

\[
 \delta(\mathcal B)=T-\mu(\mathcal B).
\tag{5.1}
\]

By the deficiency form of Hall's theorem,

\[
 \delta(\mathcal B)
 =\max_{A\subseteq S_{\mathcal B}}
 \bigl(|A|-|N^+(A)\cap S_{\mathcal B}|\bigr).
\tag{5.2}
\]

### Proposition 5.1 (colorwise deficiency charge)

For every integral uniform rotor circulation and every typewise exact
recoloring,

\[
 \boxed{R\ge |G|\,\delta(\mathcal B).}
\tag{5.3}
\]

#### Proof

Fix a color \(g\).  Its monochromatic rotor edges have distinct source
vertices and distinct target vertices, because the ambient circulation
has indegree and outdegree one at every occurrence.  They therefore form
a matching in the legal bipartite graph induced by the selected states
of \(g\mathcal B\).  Relabelling preserves its maximum matching size,
so there are at most \(\mu(\mathcal B)\) monochromatic outgoing edges of
color \(g\).  At least \(T-\mu(\mathcal B)=\delta(\mathcal B)\) of its
outgoing edges change color.  Sum over the \(|G|\) indexed colors and use
\(R\ge X\). \(\square\)

Thus any successful recoloring necessarily has

\[
 \delta(\mathcal B)=o(W/Q).
\tag{5.4}
\]

This is weaker than exact successor Hall, but it is the exact scale
needed by the run ledger.

## 6. Proved boundary

The following route is now rigorously closed.

1. Start with an arbitrary ambient floor/ceiling-balanced resolution.
2. Symmetrize it over all coordinate permutations.
3. Factor the uniform state multicover as \(h\) copies of one legal
   state successor permutation.
4. Reassign the exact color occurrences while preserving every color's
   original columns and quotas.

Theorem 3.1 shows that the optimal reassignment still has
\((1-o(1))|G|W\) runs, rather than \(o(|G|W/Q)\).

The obstruction is not merely pairwise propagation inside one proposed
balanced color.  It is an orbit-capacity identity: an adjacent pair of
exact states shares only the fraction \(E/(TD)=O(1/(H-Q))\) of its
allowed colors.  The interval alignment construction in Theorem 3.1
also shows that this lower bound is asymptotically sharp for every fixed
copied-cycle factor.

The only surviving options within exact-state-preserving color transport
are:

* directly construct \(\mathcal B\) with
  \(\delta(\mathcal B)=o(W/Q)\), preferably exact successor Hall; or
* replace the copied-cycle factor by a genuinely broad-support joint
  circulation using \(\Omega(H-Q)\) successor types per state and align
  it simultaneously with the colors.

Allowing a color to acquire state types which were not present in its
original relabelled resolution, while preserving only its rank quotas,
is a different joint quota-flow problem.  The allowed-color sets
\(\mathcal C(s)\) then change, so the no-go above does not address that
larger construction.  No such construction is proved here.
