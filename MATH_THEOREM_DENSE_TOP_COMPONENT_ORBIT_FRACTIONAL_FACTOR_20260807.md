# Every exact dense-top component has a four-palette orbit factor

**Date:** 2026-08-07  
**Method:** orbit averaging under the full symmetric group  
**Status:** unconditional fractional theorem.  It saturates the complete
rank-\((m-d-1)\) top layer while respecting owner and both immediate-palette
capacities.  For the block queue, independent fractional thinning also
selects a target-once *designated subfamily* in each sparse suffix row, but
does not remove the other physical cells.  Consequently it is not a literal
occurrence-exact SCD factor.  It does not round the orbit factor integrally,
join components, or provide the missing saturated SCD ranks.

## 1. A local component with four simple palettes

Put

\[
 n=2m+1,\qquad q=d+1,\qquad \rho=m-q=m-d-1.
\tag{1.1}
\]

Let \(C\) be a cyclic literal component of length \(L\).  Assume that its
four resource lists are simple:

\[
 \mathcal T(C)\subseteq {[n]\choose \rho},\qquad
 \mathcal O(C)\subseteq {[n]\choose m},
\tag{1.2}
\]

and

\[
 \mathcal Q^-(C)\subseteq {[n]\choose m-1},\qquad
 \mathcal Q^+(C)\subseteq {[n]\choose m+1},
\tag{1.3}
\]

with all four sets having cardinality \(L\).  Here \(\mathcal T\) is the
top-target list, \(\mathcal O\) the central-owner list, and
\(\mathcal Q^-,\mathcal Q^+\) the immediate lower and upper owner palettes.

The weight-\(q\) block queue constructed in
`MATH_THEOREM_DENSE_TOP_ROW_DELAYED_ATOM_BLOCK_QUEUE_NORMAL_FORM_20260807.md`
has these properties with \(L=q(q+1)\).  The theorem below is deliberately
stated for any component with the same four simple resource lists.

Let \(\mathfrak C\) be the set of distinct images of \(C\) under
\(\operatorname{Sym}([n])\).  Regard every image as a four-partite
hyperedge containing its \(L\) resources in each of the four coloured
parts.

## 2. Exact orbit loads

### Theorem 2.1 (four-palette orbit factor)

There is a nonnegative constant weight on \(\mathfrak C\) for which every
rank-\(\rho\) top target has total load exactly one, while the load of every
resource in a rank-\(a\) auxiliary part is

\[
 \boxed{
   \frac{\binom n\rho}{\binom na}}
 \qquad (a\in\{m-1,m,m+1\}).
 }
\tag{2.1}
\]

In particular all three auxiliary loads are below one for
\(q\ge2\).  Thus the complete top layer has an exact fractional component
factor with simultaneous owner, lower-\(q1\), and upper-\(q1\) capacities.

#### Proof

Write \(M=|\mathfrak C|\) and \(N_a=\binom na\).  The full symmetric group
is transitive on every rank layer.  Double-counting incidences between
orbit components and rank-\(a\) resources shows that every resource of that
rank has orbit degree

\[
 D_a=\frac{ML}{N_a}.
\tag{2.2}
\]

Give every component the common weight

\[
 w=\frac1{D_\rho}=\frac{N_\rho}{ML}.
\tag{2.3}
\]

Every top target then has load one.  A rank-\(a\) resource has load

\[
 D_aw=\frac{N_\rho}{N_a},
\]

which is (2.1).  Since

\[
 \rho=m-q<m-1<m<m+1=\frac{n+1}{2},
\]

the binomial coefficients strictly increase through rank \(m\), while
\(N_m=N_{m+1}\).  Both are strictly larger than \(N_\rho\), so all
auxiliary loads are below one. \(\square\)

### Corollary 2.2 (no four-palette fractional separator)

No nonnegative linear price on top targets, owners, and the two immediate
palettes can separate the local-component polytope from complete top
saturation.  Any obstruction to a complete top factor is integral,
topological, or caused by a resource not present in (1.2)--(1.3).

This is an exact statement, not an asymptotic one.

## 3. Designated sparse-row witnesses, and the literal mass obstruction

For the weight-\(q\) block queue, a suffix of \(j\) literal atoms has rank

\[
 r_j=m-(q-j)q,\qquad 1\le j\le q-1.
\tag{3.1}
\]

At every fixed \(j\), the component has \(L\) distinct rank-\(r_j\)
targets.  Notice that

\[
 r_1<r_2<\cdots<r_{q-1}=\rho.
\tag{3.2}
\]

### Theorem 3.1 (simultaneous designated sparse-row saturation)

In the relaxation which permits physical cells to remain undesignated, the
orbit factor of Theorem 2.1 can be marked fractionally so that every
target in every rank layer

\[
 {[n]\choose r_1},\ldots,{[n]\choose r_{q-1}}
\tag{3.3}
\]

has marked load exactly one.  These markings use different physical suffix
depths, and hence do not compete with one another as designated witnesses.

#### Proof

Before marking, the total orbit-factor mass of rank-\(r_j\) occurrences is
\(N_\rho\): every component has one such occurrence for each of its \(L\)
top occurrences.  Symmetry makes the load on each rank-\(r_j\) target

\[
 \frac{N_\rho}{N_{r_j}}.
\tag{3.4}
\]

By (3.2) and strict increase of the lower binomial layers,
\(N_{r_j}\le N_\rho\).  Retain the common fraction

\[
 \frac{N_{r_j}}{N_\rho}
\tag{3.5}
\]

of the rank-\(r_j\) occurrence mass.  The resulting load is one on every
target of that rank.  Each \(j\) uses a different interval length, so these
fractional marks are distinct physical cells. \(\square\)

This thinning is not a literal exact factor.  Top saturation fixes the
total component weight by

\[
 L\sum_{C'\in\mathfrak C}x_{C'}=N_\rho.
\tag{3.6}
\]

The same full components then contain exactly \(N_\rho\) physical cells
at every depth \(j\).  Literal occurrence-once saturation of rank
\(r_j\) would instead require

\[
 L\sum_{C'\in\mathfrak C}x_{C'}=N_{r_j}.
\tag{3.7}
\]

For \(j<q-1\), one has \(N_{r_j}<N_\rho\), so (3.6)--(3.7) are
incompatible.  At least \(N_\rho-N_{r_j}\) cells in that row must remain
unassigned or repeat a value.  The theorem therefore closes a witness-
selection marginal only; it does not close the physical short-cell ledger.

## 4. Exact remaining gate

The theorem removes the four central palette marginals for the dense top
row.  It simultaneously exposes a genuine lower-cell obstruction for a
positive-density use of the uniform queue.  The remaining global statement
is not another four-palette Hall inequality:

> Select integral component images, or replace them by one connected
> chronology, so that every top target occurs once, no owner or immediate
> palette resource is repeated, the missing saturated SCD ranks are
> installed in the same literal history, and component fusion preserves
> arbitrary-width upper witnesses and the terminal compiler.

Orbit averaging does not imply such an integral factor.  In particular,
the component uniformity grows with \(d\), and an appeal to a
fixed-uniformity nibble theorem would not be proof-safe.  The value of the
present result is the exact boundary: any future no-go or construction must
use integral correlation, component topology, the absent SCD ranks, or a
deeper guarded resource.  It cannot come from the four central palette
marginals.
