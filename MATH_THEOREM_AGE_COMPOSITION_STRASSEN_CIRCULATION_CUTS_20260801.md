# Exact Strassen cuts for age-composition circulation

Date: 2026-08-01

Status: unconditional finite reduction.  Combined with
`MATH_AUDIT_AGE_COMPOSITION_QUOTIENT_LITERAL_LIFT_AND_PHYSICAL_SCOPE_20260801.md`,
this removes the edge-flow variables from the symmetric rank-only
fractional marked-trace gate.  It does not prove that the triangular target
vector is feasible, and it does not retain one-copy owner, topology,
root/pin, upper-witness, or common-cap data.

## 1. Prefix and shifted age vectors

Let

\[
 \mathcal C_{r,d}=\{c=(c_0,\ldots,c_d):c_0>0,\ c_i\ge0,
                         \ \sum_i c_i=r\}.
\]

Put

\[
 P(c)=(c_0,\ldots,c_{d-1}),\qquad
 Q(c)=(c_1,\ldots,c_d).
\]

The age-composition graph has an arc `c -> c'` precisely when

\[
                         Q(c')\le P(c)                \tag{1.1}
\]

coordinatewise.

For a probability distribution `pi` on `C_(r,d)`, write `P_*pi` and
`Q_*pi` for the two induced laws on nonnegative integer `d`-vectors.

## Theorem 1 (age-circulation/Strassen equivalence)

There is a nonnegative circulation `f` on the age-composition graph with

\[
 \sum_{c'}f(c,c')=\sum_{c'}f(c',c)=\pi(c)             \tag{1.2}
\]

if and only if

\[
                         Q_*\pi\preceq_{\rm st}P_*\pi \tag{1.3}
\]

in the coordinatewise product order.

Equivalently, for every upward-closed set
`U subseteq Z_(>=0)^d`,

\[
 \boxed{
   \Pr_{c\sim\pi}[Q(c)\in U]
      \le
   \Pr_{c\sim\pi}[P(c)\in U].}                       \tag{1.4}
\]

The equivalent down-set form is

\[
   \Pr[P(c)\in D]\le\Pr[Q(c)\in D]                  \tag{1.5}
\]

for every downward-closed `D`.

### Proof

If `f` exists, sample an arc `(C,C')` with law `f`.  Both endpoint
marginals are `pi`, and (1.1) gives

\[
                         Q(C')\le P(C).
\]

Thus `f` supplies a monotone coupling of `Q_*pi` below `P_*pi`, proving
(1.3).

Conversely, finite-poset Strassen (equivalently fractional Hall on the
bipartite graph `x<=y`) turns (1.3) into a coupling `(X,Y)` with

\[
 X\sim Q_*\pi,\qquad Y\sim P_*\pi,\qquad X\le Y.
\]

The map `Q` determines its composition uniquely, because

\[
 c_0=r-\sum_{i=1}^d c_i,
\]

and the map `P` also determines its composition uniquely, because

\[
 c_d=r-\sum_{i=0}^{d-1}c_i.
\]

Therefore the coupling lifts uniquely to a coupling `(C',C)` with both
composition marginals `pi` and with `Q(C')<=P(C)`.  Orient its mass from
`C` to `C'`; this is the required `f`.  The upper-set inequalities are the
standard finite Strassen/Hall dual.  `square`

## 2. Exact edge-free formulation of the marked fractional gate

For a type `c`, let

\[
 R(c)=\{c_0+\cdots+c_{j-1}:1\le j\le d\}\cap[1,r-1].
\]

The symmetric rank-only fractional vector `q` belongs to
`ST_(k,r,d)` if and only if there are a probability distribution `pi` and
mark variables `m_s(c)` satisfying

\[
 0\le m_s(c)\le\pi(c){\bf1}_{s\in R(c)},\qquad
 \sum_c m_s(c)=q_s,                                  \tag{2.1}
\]

together with every Strassen cut (1.4).  Eliminating the independent mark
variables gives

\[
 q_s\le\sum_{c:s\in R(c)}\pi(c)                      \tag{2.2}
\]

plus (1.4).

Thus the remaining unit-descent problem is a distribution-design problem,
not an edge-enumeration problem: construct one `pi` which simultaneously
dominates all requested suffix-rank capacities and satisfies the product-
order shift cuts.

## 3. Two exact circulation families

The theorem recovers two useful sufficient families.

1. If `c_0>=c_1>=...>=c_d`, then `Q(c)<=P(c)`, so the point mass at `c`
   is feasible.  This is the stationary self-loop family.
2. If every component of `c` is positive, put

   \[
        \rho(c)=(c_d,c_0,c_1,\ldots,c_{d-1}).
   \]

   Then `Q(rho(c))=P(c)`.  Uniform mass on the cyclic rotation orbit of
   `c` is therefore a circulation.  At the literal level this is the clock
   which refreshes exactly the oldest age class at every step.

The second family shows why nonmonotone individual types need not be an
obstruction: their age debt may circulate around a rotation orbit.

## 4. A necessary warning for the proposed unit-descent proof

The local condition

\[
                         g_{i+1}\ge g_i-1             \tag{4.1}
\]

on one marked deficit profile does not by itself imply circulation.
For example, take `d=2`, any `r>=4`, and a fully marked profile with gaps
`(2,1)`.
It satisfies (4.1), but it fixes an age type with

\[
                         c_2=2>c_1=1.
\]

If every row had this same fully marked type, no unmarked suffix can be
inserted and the point mass violates (1.4) (already the increasing event
`{x_2>=2}` separates `Q_*pi` from `P_*pi`).

This does not refute the systematic residue family: its global column
multiplicities contain additional structure absent from the example.  It
does prove that a valid unit-descent argument must use that global
structure and establish the Strassen cuts (or an explicit monotone
coupling), rather than invoke the one-row gap law alone.

## 5. Physical scope

The theorem is exact only at the same level as the audited age quotient.
It does not encode:

* one selected trace per named owner;
* connected/rooted literal Euler support;
* Johnson adjacency or Catalan owner topology;
* lower/upper q1 rainbows or arbitrary-width upper witnesses;
* residence after opening and joining components;
* occurrence-labelled guarded common-cap matching; or
* bounded regeneration.

Those remain separate integral/physical gates even if the systematic
triangular vector is proved to satisfy (1.4) and (2.2).
