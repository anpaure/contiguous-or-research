# Rational multicover edge-colouring obstruction

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

The following data do **not** imply a \((1+o(1))D\) edge-colouring:

1. every chunk contains one tag and exactly \(K\) protected targets;
2. every tag has degree exactly \(D\);
3. every protected target has degree at most \(D+o(D)\);
4. every two distinct chunks have protected intersection of width at most
   two; and
5. the normalized exponential intersection moment is \(m^{o(1)}\), even
   uniformly for every \(1\leq w\leq C\log m\).

There is an explicit family satisfying stronger versions of all five
conditions whose chromatic index is at least \(3D/2\).  The construction
works for every even \(D\) and every \(K\geq2\); in particular it survives
the intended regime

\[
 K=m^{1+o(1)},\qquad D=m^{5/2-o(1)}.
\]

It also has the exact rational capacity-feasible point \(x_e=1/D\).
Thus the obstruction occurs between the vertex-capacity polytope and the
matching polytope, before any entropy-compression or heat-bath rounding
argument can begin.

The missing local statistic is at least the maximum two-vertex codegree
\(\Delta_2=o(D)\).  The exact fractional global gate is the weighted
matching-cover inequality

\[
 \sum_e y_e\leq(1+o(1))D
       \max_{M\text{ a matching}}\sum_{e\in M}y_e
 \qquad(y_e\geq0).
 \tag{0.1}
\]

Its unweighted special case is the matching-density cut

\[
 |F|\leq(1+o(1))D\,\nu(F)
 \tag{0.2}
\]

for every substantial subfamily \(F\), where \(\nu(F)\) is its maximum
matching size.  Neither width two nor an \(m^{o(1)}\) exponential moment
implies this cut.

This is an abstract incidence obstruction to the stated hypotheses.  It
does not assert that the configuration is realizable by the full Boolean
geodesic chronology.  If the word `legal' is intended to include an
additional geometric axiom excluding the construction, that axiom must be
used explicitly; it is not a consequence of the five numerical properties
above.

## 1. The doubled-triangle multicover

Fix an even integer \(D\), put

\[
 n=D/2,
\]

and fix any \(K\geq2\).  One block has three tag vertices

\[
 \tau_{ab},\quad \tau_{bc},\quad \tau_{ca}
\]

and two disjoint copies, indexed by \(j\in\{0,1\}\), of three protected
core targets

\[
 a_j,b_j,c_j.
\]

For every \(j\), every type

\[
 xy\in\{ab,bc,ca\},
\]

and every \(r\in[n]\), introduce a private set

\[
 P_{j,xy,r}
\]

of \(K-2\) targets.  All these private sets are mutually disjoint and
are disjoint from all core targets.  Define the chunk

\[
 e_{j,xy,r}
 =\{\tau_{xy}\}\cup\{x_j,y_j\}\cup P_{j,xy,r}.
 \tag{1.1}
\]

Thus every edge consists of one tag and exactly \(K\) protected targets.
Take any number of mutually disjoint blocks.  This gives arbitrarily many
tags; adding at most two disjoint trivial tag fibres handles a prescribed
tag count not divisible by three without changing any asymptotic
conclusion.

## 2. Exact degree and intersection audit

### Proposition 2.1 (degrees)

Every tag has degree exactly \(D\), every core target has degree exactly
\(D\), and every private target has degree one.

#### Proof

For a fixed type \(xy\), its tag is used by \(n\) chunks in each of the
two copies.  Hence

\[
 d(\tau_{xy})=2n=D.
\]

In one copy, for example, \(a_j\) occurs in the \(n\) chunks of type
\(ab\) and the \(n\) chunks of type \(ca\), so its degree is \(2n=D\).
The same calculation applies to \(b_j,c_j\).  Every private target was
assigned to one edge only. \(\square\)

### Proposition 2.2 (protected intersections)

For distinct chunks \(e,f\),

\[
 |C(e)\cap C(f)|\in\{0,1,2\},
 \tag{2.1}
\]

where \(C(e)\) denotes the protected-target part of \(e\).  In particular,
every protected pair intersection has width at most two in every partial
order on the protected targets.

#### Proof

Private targets never recur.  Chunks in different copies have disjoint
protected targets.  In one copy, chunks of the same type share exactly
their two core targets, while chunks of different types share the unique
core target common to their two types.  This proves (2.1).  A family of
at most two elements has width at most two. \(\square\)

### Proposition 2.3 (a strong exponential-moment bound)

For \(w\geq1\), define the uncentred overlapping moment

\[
 \Phi_w(e)
 :=\frac1D
   \sum_{\substack{f\ne e\\C(e)\cap C(f)\ne\varnothing}}
       w^{|C(e)\cap C(f)|}.
 \tag{2.2}
\]

Then uniformly in \(e\),

\[
 \boxed{\Phi_w(e)
 \leq \frac12w^2+w.}
 \tag{2.3}
\]

The centred exponential excess

\[
 \Psi_w(e)
 :=\frac1D\sum_{f\ne e}
 \bigl(
  w^{|C(e)\cap C(f)|}-1
  -(w-1)|C(e)\cap C(f)|
 \bigr)
 \tag{2.4}
\]

satisfies the sharper bound

\[
 \boxed{\Psi_w(e)\leq\frac12(w-1)^2.}
 \tag{2.5}
\]

Consequently both quantities are \(m^{o(1)}\), uniformly for
\(1\leq w\leq C\log m\), independently of \(K\) and \(D\).

#### Proof

Fix a chunk of type \(ab\) in one copy.  It meets the other \(n-1\)
chunks of type \(ab\) in two protected targets.  It meets the \(n\)
chunks of type \(bc\) and the \(n\) chunks of type \(ca\) in one target.
It has no other protected intersections.  Therefore

\[
 \Phi_w(e)
 =\frac{(n-1)w^2+2nw}{D}
 \leq\frac12w^2+w,
\]

which proves (2.3).  The summand in (2.4) is zero for an intersection of
size zero or one, and for an intersection of size two it equals

\[
 w^2-1-2(w-1)=(w-1)^2.
\]

Thus

\[
 \Psi_w(e)=\frac{n-1}{D}(w-1)^2
 \leq\frac12(w-1)^2.
\]

Finally, every fixed power of \(\log m\) is \(m^{o(1)}\). \(\square\)

Even if tag intersections are inserted into the uncentred moment, the
same example obeys

\[
 \frac1D\sum_{f\ne e,\ e\cap f\ne\varnothing}w^{|e\cap f|}
 \leq\frac12w^3+\frac32w,
 \tag{2.6}
\]

because the \(n-1\) same-type chunks in the same copy share the tag and
two core targets, while all remaining intersecting chunks share only one
incidence vertex.  Hence this stronger convention is also \(m^{o(1)}\)
on the logarithmic window.

## 3. Exact chromatic and near-factor obstruction

### Theorem 3.1 (chromatic index at least \(3D/2\))

The hypergraph constructed above satisfies

\[
 \boxed{\chi'(\mathcal H)\geq\frac32D.}
 \tag{3.1}
\]

More strongly, if one block is covered by \(C\) matchings, at least

\[
 \boxed{3D-2C}
 \tag{3.2}
\]

of its chunks remain uncovered.

#### Proof

Within either fixed copy, all \(3n=3D/2\) chunks are pairwise
intersecting: chunks of one type share two core targets, and chunks of
different types share one.  Thus a matching contains at most one chunk
from each copy, and at most two chunks from the whole doubled block.
Consequently \(C\) matchings cover at most \(2C\) of its \(3D\) chunks,
which proves (3.2).  Taking a complete edge-colouring gives
\(3D\leq2\chi'(\mathcal H)\), proving (3.1). \(\square\)

In particular, if \(C=(1+\varepsilon_D)D\) with
\(\varepsilon_D\to0\), then every block leaves at least

\[
 (1-2\varepsilon_D)D
 \tag{3.3}
\]

chunks.  Since a block has \(3D\) chunks, the uncovered proportion is at
least

\[
 \frac13-o(1).
 \tag{3.4}
\]

Thus allowing near-factors and a global \(o(1)\) leave does not evade the
obstruction.

## 4. The rational point exists exactly

### Proposition 4.1 (capacity-feasible rational multicover)

Put

\[
 x_e=1/D
 \qquad(e\in E(\mathcal H)).
 \tag{4.1}
\]

Then every tag has total incident weight one, every core target has total
incident weight one, and every private target has total incident weight
\(1/D\).

#### Proof

This follows immediately from Proposition 2.1. \(\square\)

Nevertheless (4.1) is not in the matching polytope.  In one doubled block
its total edge weight is

\[
 3D\cdot\frac1D=3,
\]

whereas every integral matching has size at most two.  Thus the violated
matching-polytope inequality is exactly

\[
 \sum_{e\text{ in the block}}x_e\leq2.
 \tag{4.2}
\]

This explains why a heat bath preserving only tag and target one-point
marginals cannot prove the desired decomposition: those marginals admit
an exact stationary rational state lying a fixed distance outside the
convex hull of legal matchings.

## 5. The missing cut and the role of codegrees

For a hypergraph \(\mathcal H\), define the unweighted density parameter

\[
 \Gamma(\mathcal H)
 :=\max_{\varnothing\ne F\subseteq E(\mathcal H)}
       \frac{|F|}{\nu(F)},
 \tag{5.1}
\]

where \(\nu(F)\) is the maximum number of pairwise disjoint edges in
\(F\).

### Lemma 5.1 (unavoidable matching-density cut)

If \(C\) matchings cover all but \(L\) edges of \(\mathcal H\), then for
every \(F\subseteq E(\mathcal H)\),

\[
 \boxed{L\geq |F|-C\nu(F).}
 \tag{5.2}
\]

In particular, an edge-colouring requires

\[
 \chi'(\mathcal H)\geq\Gamma(\mathcal H).
 \tag{5.3}
\]

#### Proof

Each of the \(C\) matchings contains at most \(\nu(F)\) edges of \(F\).
They therefore cover at most \(C\nu(F)\) members of \(F\).  The remaining
members of \(F\) are among the global leave. \(\square\)

For one doubled block, \(|F|=3D\) and \(\nu(F)=2\), so

\[
 \Gamma(\mathcal H)\geq3D/2.
\]

The exact fractional parameter is the weighted version

\[
 \Gamma^*(\mathcal H)
 :=\sup_{\substack{y\geq0\\y\ne0}}
 \frac{\sum_e y_e}
      {\max_{M\text{ a matching}}\sum_{e\in M}y_e}.
 \tag{5.4}
\]

Finite linear-programming duality identifies \(\Gamma^*(\mathcal H)\)
with the fractional edge-chromatic number: the primal covers every edge
by nonnegative weights on matchings, and the dual maximizes \(\sum_e y_e\)
subject to \(\sum_{e\in M}y_e\leq1\) for every matching \(M\).  Thus
\(\Gamma^*(\mathcal H)\leq(1+o(1))D\) is an unavoidable gate even for a
fractional decomposition into near-factors.  Taking \(y\) to be the
indicator of one doubled block gives

\[
 \Gamma^*(\mathcal H)\geq3D/2.
 \tag{5.5}
\]

The same obstruction is already visible locally in the two-vertex
codegree:

\[
 d(a_j,b_j)=d(b_j,c_j)=d(c_j,a_j)=D/2.
 \tag{5.6}
\]

Thus a prospective growing-rank nibble theorem must at least exclude
\(\Delta_2=\Theta(D)\), including both target--target and, when tags are
part of the incidence hypergraph, tag--target links.

The stated exponential estimate does not do this.  Indeed, if
\(x,y\in C(e)\), then the centred excess obeys

\[
 \Psi_w(e)
 \geq
 \frac{d(x,y)-1}{D}(w-1)^2.
 \tag{5.7}
\]

Therefore a bound \(\Psi_w(e)\leq M_m\) yields only

\[
 \frac{d(x,y)}D
 \leq\frac1D+\frac{M_m}{(w-1)^2}.
 \tag{5.8}
\]

When \(M_m=m^{o(1)}\) and \(w=O(\log m)\), the right side need not tend
to zero.  To deduce \(\Delta_2=o(D)\) from this statistic one needs, for
some \(w=w_m>1\), the quantitatively stronger condition

\[
 \boxed{M_m=o((w_m-1)^2),}
 \tag{5.9}
\]

or else an explicit codegree hypothesis.

Even \(\Delta_2=o(D)\) should not be advertised here as a proved
sufficient condition for growing \(K\).  The exact fractional global
condition is \(\Gamma^*(\mathcal H)\leq(1+o(1))D\); (5.2) is its
unweighted necessary shadow.  A complete positive theorem would need to prove
both:

1. every substantial catalogue subfamily satisfies the near-\(D\)
   matching-density inequalities; and
2. the remaining local dependency parameters are strong enough, with
   their dependence on \(K\) made explicit, to round the matching-polytope
   point into \((1+o(1))D\) integral matchings.

The current width-two and \(m^{o(1)}\)-moment hypotheses prove neither
item.

## 6. Exact boundary for the PBBS lane

The abstract heat-gap/edge-colouring reduction is false under the stated
incidence summaries.  There are two logically valid continuations.

1. **Geometric exclusion.**  Prove from the actual common-priority
   geodesic chronology that no weighted family can realize the
   doubled-triangle cut, quantitatively establishing (0.1).  A
   shape-by-shape relative-degree bound strong enough
   to imply \(\Delta_2=o(D)\) is one necessary local input, but the global
   matching-density cut must still be checked.

2. **Strengthened rounding theorem.**  Add the matching-polytope cut and
   explicit vanishing link codegrees as hypotheses, then prove a
   growing-\(K\) colouring theorem.  Any entropy-compression estimate must
   display its dependence on \(K\); a bare \(m^{o(1)}\) moment cannot be
   substituted for that dependence.

No \((1+o(1))D\) colouring, and hence no coefficient-one conclusion, is
claimed in this note.
