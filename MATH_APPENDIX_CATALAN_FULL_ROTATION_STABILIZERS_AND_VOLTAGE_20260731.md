# Appendix: full-rotation stabilizers, orbit degrees, and voltage diagnostics

Date: 2026-07-31  
Status: exact obstruction and diagnostic theorems for the full rotation
group; not a constructive all-\(m\) ansatz

## A.1 Scope and constructive reference

Put

\[
q=2m-1,\qquad
\Omega=\mathbb Z_q\sqcup\{\infty\},
\qquad G=\mathbb Z_q,
\]

with \(G\) acting by translation on the finite coordinates and fixing
\(\infty\).

This appendix records the exact information that remains useful when one
temporarily inspects the **full** rotation group: shortened subset orbits,
local orbit multiplicities in quotient matchings, the missing three-adic
Catalan factor, and regular voltage-cycle formulas.  Full \(G\)-symmetry is
only an obstruction/diagnostic coordinate when \(3\mid q\).

The constructive symmetry scale is instead

\[
H=\left\langle3^{v_3(q)}\right\rangle
\cong\mathbb Z_{q/3^{v_3(q)}},
\]

as proved in
`MATH_THEOREM_CATALAN_THREE_PRIMARY_QUOTIENT_REDUCTION_20260731.md`
(SHA-256
`f3d81e2fbf86c8db930c413f3d34752bb1b79b00b4abfb08b7c9da55161a56b1`).
The \(H\)-path-forest and unit-voltage construction theorem is not repeated
here.

## A.2 Exact full-rotation subset stabilizers

### Lemma A.2.1 (stabilizer divisibility)

If \(S\subseteq\Omega\) has stabilizer of order \(d\) in \(G\), then

\[
d\mid |S\cap\mathbb Z_q|.                              \tag{A.1}
\]

Indeed, the stabilizer acts freely on \(\mathbb Z_q\), so the finite part
of \(S\) is a union of its \(d\)-element cosets.

### Theorem A.2.2 (the only shortened orbits near the middle)

The full translation action has the following exact classification.

1. Every rank-\(m\) subset of \(\Omega\) is free.
2. Every rank-\((m-1)\) subset avoiding \(\infty\) is free.
3. A rank-\((m-1)\) subset containing \(\infty\) is free unless
   \(3\mid q\).  When \(3\mid q\), the nonfree sets are exactly

   \[
   \{\infty\}\cup A,qquad
   A\text{ a union of }(m-2)/3
   \text{ cosets of the order-three subgroup}.          \tag{A.2}
   \]

   Their stabilizer has order exactly three.
4. Every rank-\((m+1)\) subset containing \(\infty\) is free.  When
   \(3\mid q\), the nonfree rank-\((m+1)\) sets are exactly the sets
   avoiding \(\infty\) which are unions of \((m+1)/3\) cosets of the
   order-three subgroup.  Again the stabilizer has order exactly three.

For a rank-\(m\) set, the possible finite-part sizes are \(m,m-1\), and

\[
\gcd(q,m)=\gcd(q,m-1)=1.
\]

For the two outer ranks, the only additional finite-part sizes are
\(m-2,m+1\), and

\[
\gcd(q,m-2)=\gcd(q,m+1)=\gcd(q,3).                     \tag{A.3}
\]

Lemma A.2.1 therefore leaves only the stated order-three stabilizer.
Conversely, every displayed union of order-three cosets is fixed by that
subgroup.  Equation (A.3) excludes a larger stabilizer, proving exactness.

### Exact counts

When \(3\mid q\), put

\[
E_m=\binom{q/3}{(m-2)/3}
   =\binom{q/3}{(m+1)/3}.                               \tag{A.4}
\]

There are exactly \(E_m\) exceptional physical sets on each outer rank.
Every such orbit has size \(q/3\), so the number of exceptional quotient
orbits on either shore is

\[
\frac{3E_m}{q}.                                         \tag{A.5}
\]

Consequently the number of full-rotation orbits at rank \(m-1\), and also
at rank \(m+1\), is

\[
\begin{cases}
\displaystyle \frac1q\binom{2m}{m-1},&3\nmid q,\\[6pt]
\displaystyle \frac1q\left(\binom{2m}{m-1}+2E_m\right),&3\mid q.
\end{cases}                                             \tag{A.6}
\]

The middle rank is free and has \(q^{-1}\binom{2m}{m}\) quotient states.

## A.3 Orbit-degree matching lemma

Let a finite group act on an occurrence-labelled multipartite hypergraph.
Suppose an edge \(e\) is incident with a shore vertex \(x\), and write

\[
h_e=|\operatorname{Stab}(e)|,
\qquad h_x=|\operatorname{Stab}(x)|.
\]

Because the edge is occurrence-labelled,
\(\operatorname{Stab}(e)\leq\operatorname{Stab}(x)\).

### Lemma A.3.1 (local orbit multiplicity)

Selecting the whole orbit of \(e\) contributes exactly

\[
\frac{h_x}{h_e}                                         \tag{A.7}
\]

incident physical edges at every vertex in the orbit of \(x\).

Choose representatives with \(e\ni x\).  A translate \(ge\) is incident
with \(x\) precisely for \(g\in\operatorname{Stab}(x)\).  Two such
translates are the same edge precisely when their translating elements
differ by \(\operatorname{Stab}(e)\).  The number of distinct incident
translates is therefore the index in (A.7).

### Corollary A.3.2 (stabilizer-compatible quotient matching)

An invariant physical perfect matching may select the orbit of \(e\) only
if

\[
h_e=h_x
\]

at every endpoint of \(e\).  After deleting all incompatible edge orbits,
invariant physical perfect matchings are in bijection with ordinary perfect
matchings of the orbit **multihypergraph**.  Parallel quotient edges must be
retained because they can represent different physical incidences or
voltages.

Necessity follows because every selected orbit contributes a positive
integer to the physical degree, while a perfect matching requires degree
one.  Under stabilizer equality, one selected quotient edge covers every
physical vertex in each of its incident vertex orbits once; hence quotient
and physical perfect matchings lift and project bijectively.

For a Catalan repair triple whose omitted coordinate has rank \(m\), the
edge stabilizer is trivial by Theorem A.2.2.  A free edge orbit incident
with an exceptional outer colour therefore contributes degree three at
that colour, not degree one.  This is the exact local reason a fully
\(G\)-invariant exact lower/upper transversal fails when it must cover the
shortened states.

The smallest literal example is \(m=5,q=9\):

\[
\{\infty,0,3,6\}
\]

has stabilizer \(\{0,3,6\}\), orbit size three, and incidence multiplier
three against any free edge orbit.

## A.4 Catalan divisibility and the missing three-power

Let

\[
K=\operatorname{Cat}_m=\frac1{m+1}\binom{2m}{m}.
\]

Any fully \(G\)-invariant repair matching of size \(K\) whose edge orbits
are free requires

\[
q\mid K.                                                 \tag{A.8}
\]

The same divisibility is necessary for a fully \(G\)-invariant spanning
common-transversal path forest: it has \(K\) components, and the odd-order
path-stabilizer argument puts those components in free \(q\)-orbits.  These
are only full-symmetry obstructions, not unrestricted no-go statements.

The Catalan recurrence gives

\[
(m+1)K=2q\operatorname{Cat}_{m-1}.                      \tag{A.9}
\]

Since

\[
\gcd(q,m+1)=\gcd(q,3),
\]

every prime-power divisor of \(q\) other than its three-primary part
already divides \(K\).  In fact, if \(3\mid q\), equation (A.9) also gives

\[
q/3\mid K.                                               \tag{A.10}
\]

For \(v_3(q)\ge2\), this uses
\(v_3(m+1)=1\), obtained from
\(m+1=(q+3)/2\); for \(v_3(q)=1\), (A.10) is just the prime-to-three
part.

Thus the only possible missing factor in (A.8) is one power from the
three-primary demand.  More exactly,

\[
q\mid K
\quad\Longleftrightarrow\quad
v_3(K)\ge v_3(q).                                       \tag{A.11}
\]

Kummer's theorem makes this a digit test:

\[
v_3(K)=c_3(m,m)-v_3(m+1),                               \tag{A.12}
\]

where \(c_3(m,m)\) is the number of carries in the base-three addition
\(m+m\).  Equations (A.11)--(A.12) decide the full-orbit scalar obstruction
without constructing a core.

Examples:

* \(m=5\): \(q=9\), \(K=42\), and \(v_3(K)=1<2\), so a 42-edge union of
  free full-rotation orbits is impossible.
* \(m=8\): \(q=15\), \(K=1430\), and \(v_3(K)=0<1\), so full
  \(\mathbb Z_{15}\)-equivariance is again impossible.  The constructive
  scale is the clean subgroup \(H\cong\mathbb Z_5\) with three sectors.

Passing (A.11) is not sufficient: quotient Hall, physical path topology,
outer-shore compatibility, and voltage remain independent gates.

## A.5 General regular voltage-cycle formulas

This section applies only to a regular free \(\mathbb Z_n\)-cover.  Choose
a section of the vertex orbits and assign each directed quotient edge its
translation voltage.  Changing the section adds a coboundary; the sum
around any directed quotient circuit is gauge invariant.

Suppose the quotient graph is a disjoint union of directed cycles
\(Q_1,\ldots,Q_t\).  Let \(\ell_i\) be the number of quotient vertices of
\(Q_i\), and let \(v_i\in\mathbb Z_n\) be its total voltage.

### Theorem A.5.1 (cycle count and length)

The physical lift above \(Q_i\) consists of exactly

\[
g_i=\gcd(n,v_i)                                          \tag{A.13}
\]

cycles, each of length

\[
\frac{n\ell_i}{g_i}.                                    \tag{A.14}
\]

Hence the entire lift has

\[
\sum_{i=1}^t\gcd(n,v_i)                                 \tag{A.15}
\]

cycle components.  It is one Hamilton cycle exactly when the quotient is
one cycle and its voltage is a unit modulo \(n\).

After one quotient revolution, a fibre phase \(a\) becomes \(a+v_i\).
Translation by \(v_i\) on \(\mathbb Z_n\) has \(g_i\) phase orbits, each of
length \(n/g_i\), proving (A.13)--(A.15).

### Corollary A.5.2 (rotation advance)

If a rooted oriented quotient cycle has length \(\ell\) and unit voltage
\(v\), then translation by the group generator advances the lifted cycle by

\[
\ell v^{-1}\pmod{n\ell}.                                \tag{A.16}
\]

Indeed, one quotient revolution advances \(\ell\) physical positions and
adds fibre voltage \(v\).  Exactly \(v^{-1}\) revolutions add fibre phase
one.  Reversing the cycle negates the oriented voltage and advance.

For composite \(n\), nonzero voltage is not enough: a nonzero nonunit
voltage produces \(\gcd(n,v)>1\) physical cycles.  This defect is gauge
invariant.

## A.6 Graph-of-groups warning

Ordinary voltage graphs and ordinary orbit multihypergraphs silently assume
free, regular fibres.  When a quotient object itself contains a shortened
outer state, the correct local object is a graph/orbifold of groups, or
equivalently a quotient carrying vertex and edge stabilizers.  Formula
(A.7) supplies the missing local index.

This warning concerns the colour/matching quotient that uses the shortened
state.  It does not prevent the rank-\(m\) physical Johnson graph from being
a regular cover, because the middle rank is free.  Nor does it obstruct the
clean \(H\)-quotient: \(H\) acts freely on all three relevant shores.

## A.7 Audit and scope

The finite audit exhausts the three relevant subset ranks for
\(2\le m\le8\), checks the Catalan/Kummer criterion, checks 203 cyclic-coset
instances of (A.7), and checks 2400 voltage-cycle instances through group
order 24 and quotient length eight.  It also replays the literal
\(m=5,q=9\) multiplier-three example.

```text
python3 scratch/audit_catalan_full_rotation_stabilizers_voltage_appendix_20260731.py
```

Output:

```text
scratch/catalan_full_rotation_stabilizers_voltage_appendix_20260731.audit.json
```

This appendix proves no all-\(m\) repair construction and no unrestricted
Catalan no-go.  It should be used to reject over-symmetric full-rotation
models and to interpret nonfree quotient states before moving to the clean
\(H\)-scale.
