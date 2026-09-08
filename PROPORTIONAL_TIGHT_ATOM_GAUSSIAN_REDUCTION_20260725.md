# Proportional tight atoms at Gaussian depth

Date: 2026-07-25

This note records a new exact reduction.  It does not prove the remaining
matching lemma.

## 1. Parameters and proportional starts

Put

\[
 n=2m+1,\qquad W=\binom nm,
 \]

and choose

\[
 H=\lceil\alpha\sqrt{m\log m}\rceil,
 \qquad \frac1{\sqrt2}<\alpha<\frac{\sqrt3}{2},
 \qquad b=\lfloor m^{3/4}\rfloor.
\]

For \(-H\le q\le H+1\), write

\[
 N_q=\binom n{m+q}.
\]

Let \(p=\lfloor W/b\rfloor\), and put

\[
 b_q=\left\lfloor\frac{N_q}{p}\right\rfloor.
 \tag{1.1}
\]

Then \(b_0=b+O(1)\), every \(b_q\ge1\) for the displayed range and all
large \(m\), and

\[
 0\le N_q-pb_q<p.                                  \tag{1.2}
\]

Indeed, uniformly in the band,

\[
 \frac{N_q}{W}=\exp(-q^2/m+o(1)),
\]

so the smallest \(b_q\) is
\(m^{3/4-\alpha^2+o(1)}\to\infty\).

For each \(q\), choose any set \(I_q\subseteq\{0,\ldots,b-1\}\) of
\(b_q\) start positions.  An injective word

\[
 x=(x_0,\ldots,x_{m+b+H-1})
\]

defines the designated targets

\[
 A_{i,q}(x)=\{x_i,\ldots,x_{i+m+q-1}\},
 \qquad i\in I_q.                                  \tag{1.3}
\]

For all large \(m\), \(b+H<m\), so two distinct starts of the same
length give distinct target sets in an injective word.  Hence every atom
contains exactly \(b_q\) vertices in part \(q\).

Let \(\mathcal P_{m;b,H}\) be the resulting multipartite
**multihypergraph**, with part \(\binom{[n]}{m+q}\) at depth \(q\), and
one labelled hyperedge for every injective word.  Thus two words which
give the same designated set system are retained as parallel edges.  A
matching in this multihypergraph is, after forgetting labels, a matching
of distinct designated set systems, since parallel copies intersect in
all their vertices.  Its edge size is

\[
 \kappa=\sum_{q=-H}^{H+1}b_q
 =(1+o(1))\frac bW\sum_qN_q
 =\Theta(b\sqrt m).                                \tag{1.4}
\]

By coordinate transitivity, if \(E\) is the number of atom edges, every
vertex in part \(q\) has degree

\[
 d_q=\frac{b_qE}{N_q}
 =\left(1+O\left(\frac p{N_q}\right)\right)\frac Ep
 =(1+o(1))\frac Ep.                                \tag{1.5}
\]

Thus proportional starts remove the exponential degree imbalance between
Gaussian-depth ranks without clones or independently chosen quota vectors.

## 2. Exact literal consequence of a quantitative matching

### Theorem 2.1

If \(\mathcal P_{m;b,H}\) has a matching of size

\[
 p-t,\qquad t=o(p/\sqrt m),                         \tag{2.1}
\]

then

\[
 \nu(2m+1)\le W+o(W).                               \tag{2.2}
\]

#### Proof

For one selected atom emit the base windows

\[
 E_j(x)=\{x_j,\ldots,x_{j+m-H-1}\},
 \qquad 0\le j<b+2H+1.
\]

They are nonempty, and for every designated target (1.3),

\[
 E_i\cup E_{i+1}\cup\cdots\cup E_{i+q+H}
 =A_{i,q}(x).                                      \tag{2.3}
\]

The selected-atom word therefore has length

\[
 (p-t)(b+2H+1)\le W+O(HW/b)=W+o(W).                \tag{2.4}
\]

In part \(q\), the matching certifies \((p-t)b_q\) distinct targets.
The total literal repair over the band is at most

\[
 \begin{aligned}
 \sum_q\bigl(N_q-(p-t)b_q\bigr)
 &\le (2H+2)p+t\sum_qb_q\\
 &=O(HW/b)+O(tb\sqrt m)=o(W),                       \tag{2.5}
 \end{aligned}
\]

by (1.2), (1.4), and (2.1).

Finally, append every nonempty mask in the two literal binomial tails.
Their total size is at most

\[
 O\left(W\sqrt m\,e^{-H^2/m}\right)
 =Wm^{1/2-\alpha^2+o(1)}=o(W),                     \tag{2.6}
\]

because \(\alpha^2>1/2\).  Appending them proves (2.2). \(\square\)

Applied for every \(m\), (2.2) also gives the even-dimensional result by
the standard trimmed lift \(\nu(2m+2)\le2\nu(2m+1)\) and the exact identity
\(W(2m+2)=2W(2m+1)\).

The required matching accuracy is only polynomial:
an \(o(m^{-1/2})\) relative edge leave.

## 3. A rank-free local overlap estimate

The usual maximum-codegree bound loses the nested-column structure.  The
following stronger row-sum estimate does not.

For a labelled slot \(P=[i,i+r-1]\) and a second slot
\(Q=[j,j+s-1]\), put

\[
 a=|P\setminus Q|,\qquad c=|Q\setminus P|.
\]

Conditioned on the coordinate set in \(P\) being a prescribed \(r\)-set
\(A\), a prescribed \(s\)-set \(B\) can occupy \(Q\) only when
\(|A\cap B|=|P\cap Q|\), and then the exact probability is

\[
 \frac1{\binom r a\binom{n-r}c}.                  \tag{3.1}
\]

All slots above share a common position interval of length
\(m-H-b+1\), so \(a,c\le b+2H=o(m)\).  For fixed \((a,c)\), at most
\(a+c+1\) position intervals \(Q\) have those two differences: either one
interval contains the other, when the total inward displacement can split
between the two ends, or neither contains the other, when there are at most
two orientations.  In the latter case \(a,c\ge1\), so
\(2\le a+c+1\).

Consequently, uniformly in the initial slot \(P\),

\[
 \boxed{
 \sum_{Q\ne P}
 \frac1{\binom r{|P\setminus Q|}
          \binom{n-r}{|Q\setminus P|}}
 =O(1/m).}                                           \tag{3.2}
\]

To verify the last estimate, sum first over \(a,c\).  The terms with
\(a+c=1\) are \(O(1/m)\).  For \(a+c\ge2\), use
\(\binom r a\ge(r/a)^a\) and the analogous inequality for \(c\).
The series \(\sum_{a\ge1}(a/r)^a\) is \(O(1/r)\) uniformly for
\(a=o(r)\), and similarly on the complement side; the extra polynomial
factor \(a+c+1\) does not change the bound.

There is one extra multiplicity which must be included when passing from
labelled slots to intrinsic codegrees.  We give the full argument.

Let \(\mathcal S\) be the family of designated position intervals.  For
\(P\in\mathcal S\), define

\[
 M_P(a,c)=\#\{Q\in\mathcal S\setminus\{P\}:
 |P\setminus Q|=a,\ |Q\setminus P|=c\}.
\]

The interval count above gives

\[
 M_P(a,c)\le a+c+1.                                \tag{3.3}
\]

Fix a labelled atom \(e\), a vertex \(v\in e\), and the unique slot
\(P_0\) of \(e\) occupied by \(v\).  (Slots of one rank in an injective
word give distinct sets.)  For a vertex \(w\in e\setminus\{v\}\), put

\[
 a_w=|v\setminus w|,\qquad c_w=|w\setminus v|.
\]

By (3.3), at most \(a+c+1\) vertices \(w\in e\) have
\((a_w,c_w)=(a,c)\).  Now condition a uniformly random labelled atom
containing \(v\) on the slot \(P\) occupied by \(v\).  The target \(w\)
can occur only in a slot \(Q\) with differences \((a_w,c_w)\); there are
at most \(a_w+c_w+1\) such slots.  The corresponding events are disjoint,
and (3.1) therefore gives

\[
 \Pr(w\hbox{ occurs}\mid v\hbox{ occurs in }P)
 \le
 \frac{a_w+c_w+1}
 {\binom r{a_w}\binom{n-r}{c_w}}.                 \tag{3.4}
\]

Consequently, uniformly in \(P,P_0,e\),

\[
 \sum_{w\in e\setminus\{v\}}
 \Pr(w\hbox{ occurs}\mid v\hbox{ occurs in }P)
 \le
 \sum_{a+c\ge1}
 \frac{(a+c+1)^2}{\binom r a\binom{n-r}c}
 =O(1/m).                                         \tag{3.5}
\]

For completeness, the last series estimate is uniform here.  Both
\(r\) and \(n-r\) are at least \(m-H\), whereas
\(a,c\le b+2H=o(m)\).  Using
\(\binom Rj\ge(R/j)^j\), the one-variable series

\[
 \sum_{1\le j\le b+2H}\frac{(j+1)^2}{\binom{m-H}j}
\]

is dominated by its \(j=1\) term (successive terms have ratio \(o(1)\))
and hence is \(O(1/m)\).  The two-variable sum in (3.5) is bounded by a
constant times the product of the corresponding one-variable series,
with the \((0,0)\) term removed, and is also \(O(1/m)\).

Finally average (3.5) over the possible slots occupied by \(v\).  This
proves the intrinsic atom estimate

\[
 \boxed{
 \max_{v,e\ni v}
 \sum_{w\in e\setminus\{v\}}
 \frac{\deg(v,w)}{\deg(v)}=O(1/m),}                \tag{3.6}
\]

for the labelled multihypergraph.  Notice that the square in (3.5) is
essential: one factor counts vertices of the test edge with a given
intersection type, and the other counts slots in which such a vertex can
reappear.  Parallel word descriptions are already built into the labelled
degrees, so no assumption of constant representation multiplicity is
being made.

Thus the strong codegrees are confined to one nested interval column and
have total normalized mass \(O(1/m)\), even though
\(\kappa=\Theta(b\sqrt m)\).

## 4. Exact remaining lemma

The constant-one theorem follows from the following rank-sensitive nibble.

> **Proportional tight-atom matching lemma.**  With the parameters above,
> the nearly regular hypergraph \(\mathcal P_{m;b,H}\), which satisfies
> (3.6), has a matching of size \(p-o(p/\sqrt m)\).

This statement is stronger than a fixed-uniformity Pippenger theorem in its
allowed rank, but it uses substantially more information than maximum
codegree: the total conditional overlap of every atom column is \(O(1/m)\).
Proving this lemma would give the full literal constant-one bound directly
through Theorem 2.1, without exact wreath factors, quota clones, or a
separate pin-survival theorem.

## 5. Audit of the remaining matching step

The local estimate (3.6) is genuine, but it does **not** by itself put the
problem within the range of a conventional vertexwise Rödl nibble.  Here
is a quantitative reason.

Let

\[
 L=m+b+H
\]

be the length of the injective word.  The number of labelled atoms is at
most

\[
 E\le n^L=\exp(O(m\log m)),                        \tag{5.1}
\]

whereas

\[
 \kappa=\Theta(b\sqrt m)=\Theta(m^{5/4}).          \tag{5.2}
\]

Suppose, as in the usual independent-residual heuristic for a nibble,
that every target vertex is retained independently with probability
\(z\).  A fixed atom survives with probability \(z^\kappa\), and hence

\[
 \mathbb E[\#\hbox{ surviving atoms}]=Ez^\kappa.  \tag{5.3}
\]

At the leave density required by Theorem 2.1, \(z=m^{-1/2}\), equations
(5.1)--(5.3) give

\[
 \log(Ez^\kappa)
 \le O(m\log m)-\tfrac12\Theta(m^{5/4})\log m
 \longrightarrow-\infty.                         \tag{5.4}
\]

In fact the independent residual loses all atoms after deleting only an
\(O(m^{-1/4}\log m)\) fraction of the vertices: the threshold
\(Ez^\kappa\asymp1\) has

\[
 -\log z=O(m^{-1/4}\log m).                       \tag{5.5}
\]

Thus a proof of the matching lemma must keep the residual target sets
highly correlated along whole interval columns.  Rank-free random greedy,
even supplemented by (3.6), cannot be justified by the standard
``approximately independent leftover'' analysis.

There are two further bookkeeping points.

1.  The degree error in (1.5) is only

    \[
    O(1/b_{\min})
    =m^{-(3/4-\alpha^2)+o(1)},                    \tag{5.6}
    \]

    which can be much larger than the requested \(m^{-1/2}\) edge leave.
    This is not a fractional obstruction: assigning weight \(p/E\) to
    every labelled atom is a fractional matching of total weight exactly
    \(p\), since every vertex in part \(q\) receives load
    \(pb_q/N_q\le1\).  It does mean that a quantitative theorem stated
    only in terms of unweighted near-regularity is insufficient.

2.  Parallel word labels are useful for the exact conditional calculation
    in Section 3, but they do not create new matching choices.  Any
    eventual proof has to exploit the interval geometry, not the enormous
    labelled degree.

Accordingly, the audited open gate is more precise than a generic
rank-sensitive nibble:

> **Column-correlated matching gate.**  Round the uniform fractional
> matching of weight \(p\) to an integral matching with edge loss
> \(o(p/\sqrt m)\), while preserving correlations of all
> \(\Theta(b\sqrt m)\) nested slots of each atom.

No proof of this gate is supplied here.  Equations (5.4)--(5.5) rule out
the most direct independent-residual implementation, but they do not
constitute a counterexample to the atom-specific matching statement.
