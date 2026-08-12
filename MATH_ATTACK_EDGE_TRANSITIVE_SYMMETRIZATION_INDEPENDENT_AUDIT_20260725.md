# Independent audit: edge-transitive symmetrization and the actual coefficient-one threshold

Date: 2026-07-25

Method: pure mathematics only.

## Verdict

The edge-transitive weighted identity is correct, including arbitrary
residual supports encoded by zero weights.  Its converse is also exact:
for one edge orbit, the worst weighted matching cut is attained by the
constant weight and equals \(|E|/\nu\).

For \(n=2m+1\), the middle-only wreath orbit has matching number exactly
\(\binom nm/n\) by the Mütze--Standke--Wiechert odd-graph cycle factor.
Thus every weighted residual cut of the middle-only orbit is solved
losslessly.

This does not transfer to an augmented multirank wreath/geodesic edge.
Adding protected lower and upper interval vertices changes the matching
problem.  The known middle factor is only a perfect matching after those
vertices are projected away.

There is one correction.  The condition

\[
 \nu=T-o(T/Q)
\]

is exactly equivalent to a \(1+o(1/Q)\) **weighted-cut** estimate, but it
is stronger than the direct literal-repair condition needed for
coefficient one.  Since the exact augmented edge size is
\(K=\Theta(g\sqrt m)\) (or \(\Theta(M\sqrt m)\) for a full trajectory)
and \(W=(1+o(1))Tg\), a single augmented matching followed by literal
repair only requires

\[
 \boxed{T-\nu=o(T/\sqrt m).}
\]

The stronger \(o(T/Q)\) condition is sufficient and may be needed by a
particular all-residual colour-extraction argument, but it is not the
necessary converse for coefficient one itself when
\(Q/\sqrt m\to\infty\).

## 1. General identity

Let a finite group act transitively on the edge multiset of a finite
hypergraph \(H\).  Fix a maximum matching \(M_0\), \(|M_0|=\nu\).  For
uniform \(g\) in the group, every labelled edge belongs to \(gM_0\) with
probability \(\nu/|E|\).  Hence for every \(y\ge0\),

\[
 \mathbb E y(gM_0)=\frac\nu{|E|}y(E).
\]

Some translate attains its expectation, so

\[
 \max_{M\text{ matching}}y(M)
 \ge\frac\nu{|E|}y(E).
\]

Taking \(y\equiv1\) proves equality in the worst ratio:

\[
 \boxed{
 \sup_{y\ge0}\frac{y(E)}{\max_My(M)}=\frac{|E|}{\nu}.}
\]

If \(R\subseteq E\) is an arbitrary residual catalogue, extend a weight
on \(R\) by zero to \(E\).  Intersecting the translated matching with
\(R\) proves the same lower bound.  No invariance of \(R\) is needed.

This is a statement with the **full-orbit denominator** \(|E|/\nu\).  It
does not say that every residual hypergraph is itself edge-transitive or
that its matching ratio equals its own unweighted ratio.

## 2. Fixed design degree

Suppose each edge contains \(k_i\) vertices from a transitive stratum
\(V_i\).  Then

\[
 D_i=|E|k_i/|V_i|,
 \qquad
 D=\max_iD_i,
 \qquad
 T_*=|E|/D=\min_i|V_i|/k_i.
\]

The uniform vector \(x_e=1/D\) is a fractional matching of value \(T_*\).
Its exact cut ratio is

\[
 \sup_{y\ge0}
 \frac{\sum_ex_ey_e}{\max_My(M)}
 =\frac{T_*}{\nu}.
\]

Therefore the assertion that every weighted residual cut loses at most a
factor \(1+\varepsilon\) is equivalent, within this one orbit, to

\[
 \nu\ge T_*/(1+\varepsilon).
\]

The necessity converse is just the constant weighting on the full orbit.

## 3. Exact odd middle wreath specialization

Let \(n=2m+1\), \(V=\binom{[n]}m\), and let one template edge be the
\(n\) cyclic \(m\)-intervals of one cyclic order.  Its full
\(S_n\)-orbit is the middle wreath hypergraph.  Here

\[
 k=n,
 \qquad
 T_*=\frac1n\binom nm.
\]

Every shortest \(n\)-cycle in the odd graph is such a wreath, and the
MSW \(C_n\)-factor partitions all middle vertices into wreaths.  Hence

\[
 \nu=T_*.
\]

The edge-transitive identity then solves the fractional/weighted
middle-only residual problem exactly.

If the edge is augmented by lower and upper intervals, this argument
stops.  An MSW middle factor can repeat the same lower interval in many
of its wreaths, so it need not be a matching in the augmented vertex
system.  Conversely, the matching number of the augmented orbit can be
strictly smaller without contradicting the exact matching number of its
middle projection.

Thus the augmented theorem remains a genuine simultaneous multirank
packing statement.

## 4. Correct gap ledger for direct coefficient one

Let the augmented orbit have tag capacity \(T\), and suppose every edge
contains \(k_i\) resources in stratum \(i\).  Put

\[
 K=\sum_i k_i,
 \qquad
 b_i=|V_i|-Tk_i\ge0.
\]

Take a matching of size \(\nu=T-L\).  Since its edges are disjoint, the
number of uncovered vertices in stratum \(i\) is exactly

\[
 |V_i|-\nu k_i=b_i+Lk_i.
\]

Therefore total literal repair is

\[
 \boxed{
 \sum_i b_i+LK.}
\]

The calibrated scalar floor/cap ledger gives \(\sum_i b_i=o(W)\).  For
the geodesic chunk,

\[
 K=\Theta(g\sqrt m),
 \qquad
 W=(1+o(1))Tg.
\]

Thus the exact remaining repair is \(o(W)\) whenever

\[
 L=o(W/K)=o(T/\sqrt m).
\]

The same computation with a full trajectory replaces \(g\) by \(M\).

By contrast,

\[
 L=o(T/Q)
\]

is equivalent to asking the orbit cut itself to be
\(1+o(1/Q)\).  Since \(Q=\sqrt m\,\omega(m)\) in the coefficient-one
scales, this is stronger by the growing factor \(\omega(m)\).  It is a
valid sufficient target, not the exact necessary matching gap for the
direct one-matching construction.

## 5. Final status

What symmetrization removes:

* all nonnegative edge weights;
* arbitrary residual supports;
* stabilizer/divisibility bookkeeping inside one fixed orbit.

What it does not remove:

* the unweighted matching-number problem of the augmented orbit;
* compatibility of all protected ranks in one integral edge family;
* unions of several distinct schedule/priority orbits.

The sharp direct target for one calibrated augmented orbit is therefore

\[
 \boxed{\nu=T-o(T/\sqrt m),}
\]

while \(\nu=T-o(T/Q)\) is a stronger weighted-cut target.
