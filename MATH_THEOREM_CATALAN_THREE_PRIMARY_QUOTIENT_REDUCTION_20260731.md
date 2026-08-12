# The exact three-primary cyclic quotient for directed Catalan repair

Date: 2026-07-31  
Status: proved arithmetic, freeness, quotient-matching and voltage reduction;
existence of the required quotient fixture remains open in general

## 1. Arithmetic and the maximal clean rotation group

Put

\[
q=2m-1,\qquad
K=\operatorname{Cat}_m,\qquad
N=mK,\qquad
M=(m+1)K=\binom{2m}{m}.
\]

Write

\[
s=3^{v_3(q)},\qquad h=q/s,
\]

and identify the ground set with

\[
\Omega=\mathbb Z_q\sqcup\{\infty\}.
\]

Let \(H=\langle s\rangle\le\mathbb Z_q\), so \(H\cong\mathbb Z_h\).

### Theorem 1 (three-primary divisibility and freeness)

For every \(m\ge2\):

1. \(h\mid K\), and hence \(h\mid M,N,K\);
2. \(H\) acts freely on each of
   \[
   \binom{\Omega}{m-1},\qquad
   \binom{\Omega}{m},\qquad
   \binom{\Omega}{m+1};
   \]
3. if \(3\nmid q\), then \(h=q\), so the full rotation group is clean;
4. if \(3\mid q\), then the full \(\mathbb Z_q\)-action has short orbits on
   both outer ranks \(m-1\) and \(m+1\).

#### Proof

The Catalan identity

\[
(m^2-1)\operatorname{Cat}_m
   =2q\binom{q-1}{m-2}                                      \tag{1}
\]

follows by rewriting
\(\operatorname{Cat}_m=(m+1)^{-1}\binom{q+1}{m}\).  Since

\[
\gcd(q,m^2-1)=\gcd(q,3)
\]

and \(h\) is coprime to \(3\), equation (1) gives \(h\mid K\).

For freeness, a subset of \(\mathbb Z_q\) fixed by an element of order
\(d>1\) is a union of \(d\)-cycles, so its cardinality is divisible by
\(d\).  A rank-\(r\) subset of \(\Omega\) has finite part of size \(r\) or
\(r-1\).  For \(r\in\{m-1,m,m+1\}\), those possible sizes are

\[
m-2,\ m-1,\ m,\ m+1.
\]

Every common divisor of \(h\) with one of these four numbers is one:
\[
\gcd(q,m)=\gcd(q,m-1)=1,\qquad
\gcd(q,m-2)=\gcd(q,m+1)=\gcd(q,3),
\]
and \(3\nmid h\).  Thus no nonidentity element of \(H\) fixes a relevant
set.

If \(3\mid q\), write \(q=6a+3\), so \(m=3a+2\).  The order-three subgroup
of \(\mathbb Z_q\) partitions the finite coordinates into triples.  A union
of \(a\) such triples, together with \(\infty\), has rank \(m-1\) and a
nontrivial stabilizer.  A union of \(a+1\) triples has rank \(m+1\) and a
nontrivial stabilizer.  Choosing consecutive triple-orbits makes the
stabilizer exactly order three when a literal example is desired. \(\square\)

Thus the canonical symmetry scale is not “prime versus composite.”  It is
the \(3\)-free part of \(2m-1\).  The remaining
\(s=3^{v_3(2m-1)}\) cosets are the unavoidable braid sectors.

## 2. Why full rotation is impossible when \(3\mid q\)

### Theorem 2 (short-orbit obstruction)

Assume \(3\mid q\).  There is no fully \(\mathbb Z_q\)-invariant exact
lower-rainbow Johnson edge set, and hence no fully invariant directed
Catalan repair fixture in diamond normal form.

#### Proof

Every rank-\(m\) middle set has a free \(\mathbb Z_q\)-orbit: its finite
part has size \(m\) or \(m-1\), both coprime to \(q\).  Since \(q\) is odd,
an undirected Johnson edge also has a free orbit.  Indeed, an element
stabilizing the unordered endpoint pair cannot swap its endpoints with
order two; it therefore fixes each endpoint, which is impossible.

By Theorem 1 there is a rank-\((m-1)\) colour orbit with stabilizer of
order three and hence orbit size at most \(q/3\).  A free orbit of Johnson
edges whose lower colour lies in this colour orbit hits every colour in it
three times (or a larger multiple if the stabilizer is larger).  A union of
full edge-orbits therefore cannot hit that colour orbit exactly once.
Exact lower rainbow is impossible.  Directed repair in diamond normal form
contains such an exact lower transversal, so it is impossible as well.
\(\square\)

This is an obstruction only to *full equivariance*.  It is not an
obstruction to the word conjecture.  It prescribes the repair: retain
\(H\cong\mathbb Z_h\) symmetry and braid the \(s\) cosets.

## 3. Exact quotient matching theorem

Let a directed-repair hypergraph be \(H\)-invariant, with \(H\) acting
freely on all three shores and on its hyperedges.  Its quotient is the
three-partite multihypergraph whose vertices and edges are the corresponding
\(H\)-orbits.

### Theorem 3 (equivariant matching equivalence)

An \(H\)-invariant perfect matching exists upstairs if and only if the
quotient multihypergraph has a perfect matching.

#### Proof

An invariant matching is a disjoint union of edge-orbits.  Because the
action is free on each shore, one selected edge-orbit covers every vertex
of each incident vertex-orbit exactly once.  It therefore projects to one
quotient edge, and the selected quotient edges cover every quotient vertex
once.

Conversely, lift every edge of a quotient perfect matching to its full
\(H\)-orbit.  Freeness implies that each incident vertex-orbit is covered
once, and disjointness in the quotient prevents collisions between lifted
orbits.  The lift is an invariant perfect matching. \(\square\)

The theorem applies directly at the \(h\)-fold symmetry scale of Theorem 1.
It reduces the exact three-dimensional repair gate by the factor \(h\);
parallel quotient hyperedges must be retained because they encode different
voltages or physical endpoint choices.

## 4. Exact physical path-forest and voltage criterion

Suppose an \(H\)-invariant two-sided-rainbow spanning forest \(F\) on the
rank-\(m\) middle sets is the lift of a quotient forest \(\bar F\).

### Theorem 4 (quotient path forest and connected closure)

Assume:

1. \(\bar F\) is a spanning forest with exactly \(K/h\) path components;
2. every quotient path lifts to \(h\) disjoint physical paths;
3. \(K/h\) closure-edge orbits join the quotient path endpoints into one
   quotient cycle \(\bar P\); and
4. the total voltage \(v\in\mathbb Z_h\) around \(\bar P\) satisfies
   \(\gcd(v,h)=1\).

Then the lifted forest consists of exactly \(K\) physical paths, and the
lifted closure is one Hamilton cycle on all \(M\) middle sets.  If
\(\gcd(v,h)=g>1\), the closure has exactly \(g\) cycles.

#### Proof

A voltage assignment on a tree is gauged to zero, so each quotient path
lifts to \(h\) disjoint copies.  This gives \(K\) paths.  Adding the closure
orbits makes every lifted vertex degree two.  Traversing the quotient cycle
once changes the fibre coordinate by \(v\).  Its orbit on \(\mathbb Z_h\)
has size \(h/\gcd(v,h)\), so the lift has \(\gcd(v,h)\) components. \(\square\)

For the authenticated \(m=4\) fixture, \(q=h=7\), \(K/h=2\), the quotient
forest has path orders \(3\) and \(7\), and the closure voltage is \(2\).
This is exactly the construction audited in
'MATH_THEOREM_CATALAN_M4_Z7_QUOTIENT_REPAIR_CORE_20260731.md'.

## 5. Consequences for the construction program

The all-\(m\) problem separates into two precise regimes.

* If \(3\nmid(2m-1)\), a fully cyclic quotient construction is
  arithmetically admissible.  One needs a quotient repair matching, a
  quotient \(K/h\)-path forest, and a unit voltage.
* If \(3\mid(2m-1)\), searching for full \(\mathbb Z_{2m-1}\)-equivariance
  is provably overconstrained.  The correct target is
  \(\mathbb Z_h\)-equivariance plus an \(s\)-sector braid.

Here “\(s\)-sector braid” means a symmetry-breaking construction on the
residual action \(\mathbb Z_q/H\cong\mathbb Z_s\) of the \(H\)-quotient.
It does not mean \(s\) independent or equal-sized packets.  Middle and
edge \(H\)-orbits have residual orbit size \(s\), whereas the exceptional
outer-colour \(H\)-orbits have size \(s/3\); a residual-invariant edge
choice retains the same three-to-one obstruction.  Thus the quotient
matching must generally couple and break the residual phases.

In particular, for \(m=8\) (the \(k=16\) word problem),

\[
q=15,\qquad h=5,\qquad s=3.
\]

The repeated failure of full-\(\mathbb Z_{15}\) quotient lanes is therefore
structural.  A three-sector \(\mathbb Z_5\)-equivariant braid is the maximal
clean cyclic architecture.

This theorem does not construct the quotient forest or the sector braid.
It proves the correct symmetry scale and removes all larger cyclic groups
from consideration.
