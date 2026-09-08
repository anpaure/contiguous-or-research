# Uniform flag apertures make all named-target Hall cuts scalar

**Date:** 2026-08-03  
**Status:** unconditional matching theorem for a complete uniform flag
atlas.  It proves that, on this face, rank transportation is sufficient for
an integral matching of every named Boolean target.  It does not prove that
a one-copy Johnson carrier supplies such an atlas.

## 0. Outcome

Let the target shore contain every set in a chosen collection of Boolean
ranks.  A physical aperture has a mandatory core \(K\), an envelope \(E\),
and may carry precisely the targets

\[
                              K\subseteq S\subseteq E.              \tag{0.1}
\]

Suppose that for each aperture type \(t=(a_t,b_t)\), every flag

\[
                    K\subseteq E,\qquad |K|=a_t,quad |E|=b_t       \tag{0.2}
\]

occurs with one common integral multiplicity \(\mu_t\).  Then all
exponentially many named-target Hall inequalities collapse exactly to a
transportation problem on the rank indices.

Write

\[
 M_t=\mu_t {k\choose a_t}{k-a_t\choose b_t-a_t}                    \tag{0.3}
\]

for the number of type-\(t\) slots.  If nonnegative numbers
\(\lambda_{t,s}\) satisfy

\[
 \sum_t\lambda_{t,s}=1                                                \tag{0.4}
\]

for every demanded rank \(s\), with \(\lambda_{t,s}=0\) unless
\(a_t\le s\le b_t\), and

\[
                 \sum_s\lambda_{t,s}{k\choose s}\le M_t
                 \qquad(t),                                         \tag{0.5}
\]

then there is an **integral** matching assigning every named target to a
distinct compatible aperture slot.  Conversely, every such matching gives
an integral rank transportation satisfying (0.4)--(0.5).  Thus the two
systems are equivalent.

The proof is one symmetric fractional matching followed by ordinary
bipartite integrality.  The key identity is

\[
 {k\choose s}{s\choose a}{k-s\choose b-s}
 =
 {k\choose a}{k-a\choose b-a}{b-a\choose s-a}.                    \tag{0.6}
\]

This theorem explains why the stationary pull clock has no fractional
named-target separator.  It also identifies the exact missing integral
design: a real one-copy carrier must supply a sufficiently uniform family
of its **actual** collar/envelope apertures.  Uniform rank marginals alone,
or an average over different carriers, is not the hypothesis.

## 1. Complete flag-slot model

Fix a ground set \([k]\) and a demanded rank set

\[
                         \mathcal R\subseteq\{0,1,\ldots,k\}.
\]

Usually rank zero is omitted.  For every type \(t\) fix integers

\[
                         0\le a_t\le b_t\le k
\]

and a multiplicity \(\mu_t\in\mathbb Z_{\ge0}\).  The type-\(t\) slot
shore is

\[
 \mathcal C_t=
 \{(K,E,\ell):K\subseteq E\subseteq[k],\ |K|=a_t,\ |E|=b_t,
                       1\le\ell\le\mu_t\}.                         \tag{1.1}
\]

Slots with different copy labels are distinct physical resources.  Put
\(\mathcal C=\dot\bigcup_t\mathcal C_t\), and join a target
\(S\in\binom{[k]}s\), \(s\in\mathcal R\), to \((K,E,\ell)\) exactly when

\[
                              K\subseteq S\subseteq E.              \tag{1.2}
\]

No other guards or capacities are hidden in this graph.  If an actual
physical model has further structural zeros, those edges must be deleted
and the theorem no longer applies without a separate orbit/Hall argument.

## 2. Exact rank-transportation theorem

### Theorem 2.1 (uniform flag matching)

The graph in Section 1 has a matching saturating every demanded target if
and only if the rank-transportation system (0.4)--(0.5) is feasible.

#### Proof

Necessity is immediate from a matching.  Let \(n_{t,s}\) count matched
rank-\(s\) targets using type \(t\), and put

\[
                  \lambda_{t,s}={n_{t,s}\over {k\choose s}}.
\]

Every target is matched once, giving (0.4), and no type uses more than its
\(M_t\) slots, giving (0.5).

For sufficiency, fix a feasible \(\lambda\).  A rank-\(s\) target \(S\)
has exactly

\[
             \mu_t {s\choose a_t}{k-s\choose b_t-s}                 \tag{2.1}
\]

compatible type-\(t\) slots.  Send from \(S\) to each of them the
fractional weight

\[
 {\lambda_{t,s}\over
   \mu_t {s\choose a_t}{k-s\choose b_t-s}}.                         \tag{2.2}
\]

Terms with zero denominator have \(\lambda_{t,s}=0\) and are omitted.
Summing (2.2) over the compatible type-\(t\) slots gives
\(\lambda_{t,s}\); summing over \(t\) gives one unit out of every target.

Fix a slot \((K,E,\ell)\) of type \(t=(a,b)\).  It is compatible with
exactly

\[
                             {b-a\choose s-a}                         \tag{2.3}
\]

rank-\(s\) targets.  Its load from that rank is therefore

\[
 {b-a\choose s-a}
 {\lambda_{t,s}\over
  \mu_t {s\choose a}{k-s\choose b-s}}.
\]

Identity (0.6) turns this into

\[
                    {\lambda_{t,s}{k\choose s}\over M_t}.           \tag{2.4}
\]

Summing (2.4) over \(s\) and using (0.5) gives load at most one on every
slot.  We have constructed a fractional matching saturating the entire
target shore.

The bipartite matching polytope is integral.  Hence there is an integral
matching saturating every demanded target. \(\square\)

### Corollary 2.2 (one-type criterion)

For one flag type \((a,b)\) of multiplicity \(\mu\), every target in ranks
\(\mathcal R\subseteq[a,b]\) can be matched whenever

\[
                  \sum_{s\in\mathcal R}{k\choose s}
                  \le
                  \mu{k\choose a}{k-a\choose b-a}.                  \tag{2.5}
\]

Thus on a complete uniform flag atlas, total slot count is the only Hall
condition.

### Corollary 2.3 (rank-flow formulation)

Create a source node of supply \({k\choose s}\) for every demanded rank
\(s\), a type node of capacity \(M_t\), and an arc \(s\to t\) exactly when
\(a_t\le s\le b_t\).  Then the full named-target matching exists exactly
when this small rank network routes all source supply.

This is merely (0.4)--(0.5) after putting

\[
                             x_{s,t}=\lambda_{t,s}{k\choose s}.
\]

The rank network has integral capacities, so its feasible flow may itself
be taken integral.  Theorem 2.1 then lifts it to an ordinary physical
matching.

## 3. Relation to rotor apertures

For a fixed depth-\(d\) carrier, the exact physical aperture of a
\(q\)-cell \(c=(j,q)\) is

\[
                       K_c\subseteq S\subseteq E_c,                 \tag{3.1}
\]

where \(K_c\) is its mandatory two-sided collar and \(E_c\) its maximal
erosion envelope.  Theorem 2.1 applies literally if, after all protected
reservations, the actual slots decompose into complete uniform flag copies
as in (1.1), with \((a_t,b_t)=(|K_c|,|E_c|)\), and no edge depends on data
outside that flag.

It does **not** follow from any of the following weaker statements.

1. The histogram of \((|K_c|,|E_c|)\) is correct.
2. Every target has at least one individually compatible slot.
3. The flag distribution is uniform only in expectation over several
   carriers.
4. A cyclic quotient forgets short orbits, phase, addresses, or a twisted
   seam.
5. The target-to-slot matching ignores simultaneous-pin interval closure.

The last point is separate: Theorem 2.1 assigns targets to individually
compatible slots.  The simultaneous-pin theorem must still verify that the
chosen cell intervals do not collectively erase every supplier of a
required owner coordinate or a positive selected target coordinate.

Consequently a proof of integral coloured-rotor fusion may be split into
three exact rows:

\[
 \boxed{
 \begin{array}{c}
 \text{construct a one-copy carrier with a complete or controlled flag atlas},\\
 \text{solve the small rank transportation},\\
 \text{enforce the simultaneous interval-closure constraints}.
 \end{array}}
\]

The second row is solved by this note.  The first and third are genuine
physical chronology questions.

## 4. Orbit-balanced extension

Full symmetric uniformity is stronger than necessary.  If a group
preserves the addressed target-slot graph, the exact orbit-transportation
theorem may be applied instead: every target and slot orbit becomes a
weighted quotient vertex, and the physical matching number equals the
quotient transportation optimum.  Theorem 2.1 is the special case in which
the full symmetric group is transitive on every flag type and every target
rank, so the orbit program collapses further to the rank network of
Corollary 2.3.

For a free cyclic action the matching deficiency is a multiple of the orbit
order.  Therefore any independently proved defect bound smaller than that
order forces exact saturation on the free-orbit part.  Periodic target
orbits and fixed boundary resources must be handled separately.
