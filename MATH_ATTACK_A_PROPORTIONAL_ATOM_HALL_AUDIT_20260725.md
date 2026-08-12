# Proportional tight atoms: exact Boolean Hall solution and physical-row boundary

Date: 2026-07-25

This note audits `PROPORTIONAL_TIGHT_ATOM_GAUSSIAN_REDUCTION_20260725.md`
and isolates the first exact Hall collar.  Its positive conclusion is that
the whole proportional floor profile has an **exact**, zero-leave solution
in the Boolean inclusion poset.  Consequently neither quota mismatch nor
Boolean shadow expansion is the remaining obstruction.  What is not proved
is that the resulting chains can be grouped into the common injective tight
rows which are the hyperedges of the proportional-atom hypergraph.

Throughout,

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 N_q=\binom{n}{m+q},
\]

\[
 b=\lfloor m^{3/4}\rfloor,\qquad
 p=\left\lfloor\frac Wb\right\rfloor,\qquad
 b_q=\left\lfloor\frac{N_q}{p}\right\rfloor .
\tag{0.1}
\]

## 1. Audit of the proportional atom

All of the following claims in the Gaussian reduction are valid.

1. Division of \(W\) by \(b\) gives \(W=pb+r\), with \(0\le r<b<p\)
   for all sufficiently large \(m\).  Hence in fact

   \[
   b_0=b_1=\left\lfloor\frac Wp\right\rfloor=b.
   \tag{1.1}
   \]

2. Uniformly for \(|q|\le H+1\),

   \[
   \log\frac{N_q}{W}=-\frac{q^2}{m}+o(1)
   \tag{1.2}
   \]

   with the harmless linear-in-\(q\) correction absorbed in \(o(1)\).
   Thus \(b_q=m^{3/4-\alpha^2+o(1)}\) at the edge of the band and tends
   to infinity because \(\alpha^2<3/4\).

3. The longest required position is \(m+b+H-1\), so the word has
   \(m+b+H\le n\) distinct coordinates for all sufficiently large \(m\).
   At a fixed rank, two different start positions give different sets:
   the leftmost coordinate in the earlier interval is absent from the
   later interval.  Hence every labelled atom really has

   \[
   \kappa=\sum_{q=-H}^{H+1}b_q=\Theta(b\sqrt m)
   \tag{1.3}
   \]

   distinct vertices.

4. If \(E\) is the number of labelled injective words, coordinate
   transitivity and incidence counting give the exact degree

   \[
   d_q=\frac{b_qE}{N_q}.
   \tag{1.4}
   \]

   Since \(N_q=p(b_q+\theta_q)\), \(0\le\theta_q<1\), this is

   \[
   d_q=\frac Ep\left(1+O(1/b_q)\right).
   \tag{1.5}
   \]

5. The literal identity

   \[
   \bigcup_{j=0}^{q+H}
   \{x_{i+j},\ldots,x_{i+j+m-H-1}\}
   =\{x_i,\ldots,x_{i+m+q-1}\}
   \tag{1.6}
   \]

   is exact.  Consequently a matching of size
   \(p-o(p/\sqrt m)\) has the length and repair bounds asserted in
   Theorem 2.1 of the source note.  No boundary term was omitted.

## 2. Audit of the local overlap sum

Let \(P,Q\) be two designated position intervals, let \(|P|=r\), and put

\[
 a=|P\setminus Q|,\qquad c=|Q\setminus P|.
\]

Conditioned on the unordered coordinate set in \(P\) being a prescribed
\(r\)-set \(A\), the set in \(P\cap Q\) is a uniformly random
\((r-a)\)-subset of \(A\), independently of the uniformly random
\(c\)-subset used on \(Q\setminus P\).  Therefore, for a prescribed set
\(B\), the exact conditional probability is

\[
 \frac{1}{\binom r a\binom{n-r}c}
\tag{2.1}
\]

when \(|A\cap B|=r-a\), and zero otherwise.

For fixed \((a,c)\), there are at most \(a+c+1\) possible intervals
\(Q\).  If one interval contains the other, the unused length can split
between its two ends in at most \(a+1\) or \(c+1\) ways.  Otherwise there
are at most the two crossing orientations, which are also bounded by
\(a+c+1\).  The common position core excludes disjoint intervals.

For \(R\ge m-H\) and \(J\le b+2H=o(R)\),

\[
 \sum_{j=1}^{J}\frac{(j+1)^4}{\binom Rj}=O(1/R).
\tag{2.2}
\]

Indeed the \(j=1\) term is \(O(1/R)\), and the ratio of successive
terms is \(O(j/R)=o(1)\) uniformly after increasing the implicit constant
to handle the first boundedly many terms.  Using
\((a+c+1)^2\le 2(a+1)^2(c+1)^2\), (2.2) gives

\[
 \sum_{a+c\ge1}
 \frac{(a+c+1)^2}{\binom r a\binom{n-r}c}=O(1/m).
\tag{2.3}
\]

For a fixed test atom \(e\), a fixed \(v\in e\), and a fixed
intersection type \((a,c)\), at most \(a+c+1\) vertices of \(e\) have
that type relative to \(v\).  In a random labelled atom containing \(v\)
in a specified slot, the same bound counts the slots in which one such
vertex can reappear.  These events are disjoint because equal-length
distinct intervals in an injective word give distinct sets.  Averaging
over the equally likely slots of \(v\) proves exactly

\[
 \boxed{
 \max_{v,e\ni v}\sum_{w\in e\setminus\{v\}}
 \frac{\deg(v,w)}{\deg(v)}=O(1/m).}
\tag{2.4}
\]

Thus the square in the source proof is correct, and passing to the labelled
multihypergraph introduces no missing representation factor.

As a consequence, for an independent uniformly random labelled atom \(F\),

\[
 \mathbb E\binom{|F\cap e|}{2}
 =O\left(\frac{\kappa}{mp}\right).
\tag{2.5}
\]

This follows by multiplying (2.4) by
\(\Pr(v\in F)=d(v)/E=(1+o(1))/p\), summing over \(v\in e\), and dividing
the ordered-pair sum by two.

## 3. The first exact proportional Hall collar

Put \(V_q=\binom{[n]}{m+q}\).  Consider the upper transition
\(V_q\to V_{q+1}\), with \(q\ge0\), in the Boolean inclusion graph.
Suppose \(s\) prospective bundles currently occupy a family

\[
 \mathcal U\subseteq V_q,\qquad |\mathcal U|=s b_q.
\]

Exactly \(s b_{q+1}\) of these vertices must continue to distinct vertices
of \(V_{q+1}\).  Write

\[
 \Delta_q=b_q-b_{q+1}\ge0.
\]

### Proposition 3.1 (exact collar)

Such a continuation exists if and only if, for every
\(\mathcal X\subseteq\mathcal U\),

\[
 \boxed{
 |\partial^+\mathcal X|
 \ge |\mathcal X|-s\Delta_q.}
\tag{3.1}
\]

#### Proof

In any bipartite graph, the maximum matching size from a left vertex set
\(\mathcal U\) is

\[
 |\mathcal U|-max_{\mathcal X\subseteq\mathcal U}
       \bigl(|\mathcal X|-|N(\mathcal X)|\bigr).
\tag{3.2}
\]

Requiring this to be at least
\(s b_{q+1}=s b_q-s\Delta_q\) is exactly (3.1). \(\square\)

The lower transition from rank \(m-d\) to rank \(m-d-1\) has the symmetric
criterion

\[
 |\partial^-\mathcal X|
 \ge |\mathcal X|-s(b_{-d}-b_{-(d+1)}).
\tag{3.3}
\]

These are the first literal floor-corrected Hall cuts.  Replacing their
right sides by a proportional real quantity would lose the exact collar.

## 4. Exact zero-leave solution of all Boolean collars

Define

\[
 a_d=b_{-d}-b_{-(d+1)}\quad(0\le d<H),
 \qquad a_H=b_{-H}.
\tag{4.1}
\]

Then

\[
 b_q=\sum_{d\ge\max\{-q,q-1\}}a_d.
\tag{4.2}
\]

An abstract proportional bundle consists of \(a_d\) saturated symmetric
chain segments from rank \(m-d\) through rank \(m+d+1\), for every
\(0\le d\le H\).  Unlike an atom, it is not required that these segments
come from different starts in one coordinate word.

### Theorem 4.1 (exact proportional Boolean bundle packing)

There are exactly \(p\) pairwise vertex-disjoint abstract proportional
bundles.  They occupy exactly \(p b_q\) vertices of every rank \(V_q\).
In particular, they leave precisely

\[
 R_q=N_q-pb_q<p
\tag{4.3}
\]

vertices at rank \(q\), and they satisfy every upper and lower Hall collar
(3.1)--(3.3) simultaneously with no bundle loss.

#### Proof

We use only the standard symmetric-chain decomposition of the Boolean
lattice.  For completeness, its existence follows inductively.  If

\[
 A_r\subset A_{r+1}\subset\cdots\subset A_s,
 \qquad r+s=n-1,
\]

is a symmetric chain in \(B_{n-1}\), it produces in \(B_n\) the chains

\[
 A_r\subset\cdots\subset A_s\subset A_s\cup\{n\}
\]

and, when nonempty,

\[
 A_r\cup\{n\}\subset\cdots\subset A_{s-1}\cup\{n\}.
\]

Both new endpoint-rank sums equal \(n\), and these chains partition the
two copies of \(B_{n-1}\).

Fix such a decomposition \(\mathscr C\) of \(B_{2m+1}\).  Let
\(\mathscr C_{\ge d}\) be the set of its chains meeting rank \(m-d\).
These families are nested, and

\[
 |\mathscr C_{\ge d}|=N_{-d},
\tag{4.4}
\]

because every chain meeting the rank does so in exactly one vertex.

We construct nested chain families

\[
 K_H\subseteq K_{H-1}\subseteq\cdots\subseteq K_0,
 \qquad K_d\subseteq\mathscr C_{\ge d},
\tag{4.5}
\]

with

\[
 |K_d|=p b_{-d}.
\tag{4.6}
\]

Choose \(K_H\) arbitrarily.  Having chosen \(K_{d+1}\), extend it inside
\(\mathscr C_{\ge d}\) to size \(p b_{-d}\).  This is possible because

\[
 |K_{d+1}|=p b_{-(d+1)}\le p b_{-d}\le N_{-d}
 =|\mathscr C_{\ge d}|.
\]

Assign truncation radius \(d<H\) to the chains in
\(K_d\setminus K_{d+1}\), and radius \(H\) to those in \(K_H\).  The
number assigned radius \(d\) is exactly \(p a_d\).  On each such Boolean
chain retain only the symmetric segment from rank \(m-d\) to rank
\(m+d+1\).  All retained segments remain vertex-disjoint.

For each \(d\), partition the \(p a_d\) radius-\(d\) segments into \(p\)
groups of size \(a_d\), and combine one group of every radius into each
of \(p\) bundles.  Formula (4.2) gives exactly \(p b_q\) occupied vertices
at rank \(q\).  Following the selected symmetric chains furnishes all the
simultaneous inclusion matchings, so Proposition 3.1 and its lower analogue
give every asserted Hall inequality. \(\square\)

### Quantitative consequence

The requested accuracy \(p-o(p/\sqrt m)\) loses nothing at the level of
Boolean shadows: Theorem 4.1 attains \(p\).  All floor remainders are
absorbed exactly by the unused rank sets (4.3).

## 5. Why this does not prove the atom matching

For a true proportional atom, the \(a_d\) chain segments assigned to one
bundle must have central sets

\[
 T_i=\{x_i,\ldots,x_{i+m-1}\}
\]

in one support-separated Johnson path, and every truncated flag must obey

\[
 A_{i,-d}=\bigcap_{j=0}^dT_{i-j},
 \qquad
 A_{i,d}=\bigcup_{j=0}^dT_{i+j}.
\tag{5.1}
\]

The grouping step in Theorem 4.1 supplies none of these common-word
identities.  Conversely, the overlap estimate (2.4) controls only the
second-order incidence of two already physical atoms.  It does not turn an
arbitrary collection of Boolean chains into the interval system (5.1), and
it is not a Hall sufficiency theorem for a growing-rank hypergraph matching.

This distinction is already visible at the middle rank.  A physical atom
uses \(b\) middle sets forming one injective tight-window Johnson segment.
An abstract bundle merely uses \(b\) unrelated middle vertices.  The
saturating Johnson cycle supplies a near-spanning general Johnson order,
but a general Johnson order need not satisfy the departure/arrival FIFO law
of an injective tight row.  Thus the q=1 saturating-cycle theorem does not
perform the missing recoding.

The exact proved/conditional boundary is therefore:

\[
 \boxed{
 \begin{array}{c}
 \text{all proportional floor counts and all Boolean Hall collars}\cr
 \text{are simultaneously feasible for }p\text{ bundles}
 \end{array}}
\tag{5.2}
\]

but

\[
 \boxed{
 \text{common physical tight-row bundling with loss }o(p/\sqrt m)
 \text{ remains unproved}.}
\tag{5.3}
\]

## 6. Adversarial audit

1. **No hidden maximal-radius assumption.**  The chains assigned radius
   \(d\) in Theorem 4.1 may be longer chains truncated at \(d\).  Therefore
   the number \(N_{-d}-N_{-(d+1)}\) of maximal SCD chains of exact radius
   \(d\) is not a capacity obstruction.

2. **The two sides use the same chain.**  The lower and upper flags were
   not matched independently.  Each comes from one symmetric chain, so
   the common nesting required at the abstract level is literal.

3. **Floors remain exact.**  The construction uses \(p b_q\), not
   \(pN_q/W\), at every rank.  The remainder is exactly \(R_q\).

4. **The theorem is not an atom theorem.**  Calling the abstract bundles
   hyperedges of the original multihypergraph would be invalid.  The shared
   coordinate word is an additional high-order compatibility constraint.

5. **Scope of the local row sum.**  Equation (2.4) is verified for the
   labelled multihypergraph.  It does not by itself imply a near-\(D\)
   edge-coloring or an integral matching, because those conclusions require
   a growing-rank structured-rounding theorem not contained in the source
   note.

No algebraic correction to the Gaussian reduction or to its \(O(1/m)\)
local-overlap calculation was found.  The substantive correction is one of
logical placement: Boolean Hall is now completely solved by Theorem 4.1;
the remaining lemma must explicitly retain the common physical row law.
