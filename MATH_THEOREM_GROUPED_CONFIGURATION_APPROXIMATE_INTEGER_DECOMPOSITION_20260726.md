# Approximate integer decomposition for grouped packet configurations

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let \(\mathfrak F\) be the owner fibres. Fibre \(f\) has a finite library
of whole packet/compiler columns

\[
                         {\cal A}_f=\{a_{f,\omega}:
                                      \omega\in\Omega_f\}.        \tag{0.1}
\]

Every option is already a legal whole-fibre chronology. One must choose
exactly one column from every \({\cal A}_f\).

Ordinary total unimodularity is false: the augmented column matrices
contain determinant-two minors. Exact normality is therefore not inferred.
Nevertheless, the grouped problem has a rank-controlled approximate
integer decomposition theorem which is sufficient on the Gaussian profile
quotient.

Let \(\rho\) be any common all-depth quotient of the literal target ledger,
including both signs, and let

\[
                              D=\operatorname{rank}\rho A         \tag{0.2}
\]

be the rank of its configuration rows after removing the fibre-sum rows.
Put

\[
                              M=\max_f|V_f|,\qquad
                              C=2H                                \tag{0.3}
\]

for the largest owner-fibre mass and the number of signed depth colours.

### Main theorem

If a common fractional choice has quotient load \(b\), then there is an
integral choice of one whole column per fibre whose quotient load
\(\widehat b\) satisfies

\[
 \boxed{\|\widehat b-b\|_1\le2CDM=4HDM.}                           \tag{0.4}
\]

The proof uses a basic feasible representation, not TU, Graver bounds, or
independent rounding. At most \(D\) fibres remain fractional at a basic
point; all other fibres already choose one whole column.

For the independently randomized rank-matching Gaussian profile quotient,

\[
                         D=2^{o(m)},\qquad M\le2^m,\qquad
                         H=m^{O(1)},                              \tag{0.5}
\]

and

\[
                         W=\binom{2m}m=2^{2m-o(m)}.                \tag{0.6}
\]

Consequently

\[
                              4HDM=2^{m+o(m)}=o(W).                \tag{0.7}
\]

Thus the grouped **profile** configuration problem has approximate integer
decomposition: every common fractional profile point can be rounded to
whole packet/compiler columns with \(o(W)\) total profile discrepancy.
All lower and upper depths are rounded simultaneously because they are
rows of the same vector \(a_{f,\omega}\).

This result also localizes every determinant-two or parity defect to at
most \(D\) fibres, of total owner mass at most \(DM=o(W)\). Hence no stable
linear parity obstruction exists in the Gaussian profile quotient.

The theorem does not yet round the full literal target ledger. There its
effective rank can be \(\Theta(HW)\), and (0.4) becomes useless. A stable
literal obstruction would have to consist of
\(\Omega(W/M)\) independent parity or odd-set constraints, or a real
Hall functional with \(\Omega(W)\) deficit. No such family is presently
proved.

## 1. Exact grouped system

Let

\[
 x_{f,\omega}\ge0,\qquad
 \sum_{\omega\in\Omega_f}x_{f,\omega}=1                           \tag{1.1}
\]

be the product of fibre simplices. Write \(A\) for the matrix whose column
\((f,\omega)\) is the common signed all-depth configuration vector
\(a_{f,\omega}\). Thus

\[
                              Ax=b                                \tag{1.2}
\]

fixes one fractional load vector in the intersection of the Minkowski sum
\(\sum_f\operatorname{conv}{\cal A}_f\) with the desired quota polytope.

For every colour \(c=(\sigma,q)\), every option contributes exactly one
target occurrence per owner:

\[
                         \sum_Ta_{f,\omega}^{c}(T)=|V_f|.         \tag{1.3}
\]

Therefore, after any quotient \(\rho\) obtained by aggregating target
coordinates, one column has total nonnegative mass \(|V_f|\) in every
colour. In the concatenated \(\ell^1\) norm,

\[
                         \|\rho a_{f,\omega}\|_1=C|V_f|.          \tag{1.4}
\]

The same identity holds for every convex combination of the columns of
one fibre.

The integral Minkowski sum is

\[
                         {\cal P}_{\mathbb Z}
                           =\sum_f{\cal A}_f.                      \tag{1.5}
\]

Exact normality would assert much more than needed: it would require
appropriate lattice points in the convex Minkowski sum to lie in (1.5).
The theorem below instead bounds their distance from (1.5).

## 2. Rank-controlled approximate integer decomposition

### Theorem 2.1 (grouped basic-point rounding)

Let \(A_f\subseteq\mathbb Z_{\ge0}^D\) be finite nonempty configuration
sets, and suppose every \(a\in A_f\) has the same \(\ell^1\)-mass
\(m_f\). If

\[
                         b\in\sum_f\operatorname{conv}A_f,        \tag{2.1}
\]

then there are \(a_f\in A_f\) such that

\[
                         \left\|\sum_fa_f-b\right\|_1
                              \le2D\max_fm_f.                     \tag{2.2}
\]

More precisely, all nonintegrality can be confined to at most
\(\operatorname{rank}A\le D\) fibres, and the right side can be replaced
by twice the sum of their masses.

#### Proof

Choose a representation

\[
                         b=\sum_{f,\omega}
                              x_{f,\omega}a_{f,\omega}             \tag{2.3}
\]

in the product of simplices, and take an extreme point of the polytope
defined by (1.1) and (2.3). Let \(r=\operatorname{rank}A\), after
restriction to the affine span left by the fibre-sum equations.

There are \(|\mathfrak F|+r\) independent equality rows. Hence a basic
feasible solution has at most \(|\mathfrak F|+r\) positive variables.
Every fibre has at least one positive variable. A fibre with more than
one positive variable has at least two. If \(s\) fibres are fractional,
the number of positive variables is at least

\[
                              |\mathfrak F|+s.                    \tag{2.4}
\]

Therefore \(s\le r\le D\).

Every fibre with exactly one positive variable is already integral,
because its variables sum to one. In each of the at most \(D\) fractional
fibres, choose an arbitrary column \(a_f\). If

\[
                         \bar a_f=\sum_\omega
                                x_{f,\omega}a_{f,\omega},          \tag{2.5}
\]

then

\[
                         \|a_f-\bar a_f\|_1
                         \le\|a_f\|_1+\|\bar a_f\|_1=2m_f.        \tag{2.6}
\]

Summing (2.6) proves (2.2). \(\square\)

### Corollary 2.2 (common all-depth packet rounding)

Apply Theorem 2.1 to the quotient columns
\(\rho a_{f,\omega}\). Then one legal whole packet/compiler option can be
chosen in every owner fibre and

\[
                         \|\rho L-\rho L^*\|_1
                              \le2C\sum_{f\in{\cal R}}|V_f|
                              \le2CDM,                            \tag{2.7}
\]

where \({\cal R}\) is a set of at most \(D\) exceptional fibres.

Every chosen column retains its entire certified chronology. No depthwise
splicing or independent lower/upper rounding occurs.

## 3. Gaussian profile scale

For the independent-rank-matching atlas, use the common profile quotient
whose rows record:

* the signed depth \(q\le H\);
* the macro-rank and half-rank histogram class;
* the Gaussian carrier/status bins; and
* the floor/ceiling profile-reset totals.

The bin widths and tail cutoffs may tend to zero and infinity slowly. The
number of rows is

\[
                         D\le H\exp(\operatorname{polylog}m)
                              =2^{o(m)}.                           \tag{3.1}
\]

An owner fibre is contained in one product status cube. Its owner mass is
at most the number of orientations of the \(N=m-O(d)\) nonresidual
matching pairs:

\[
                              |V_f|\le2^N\le2^m.                   \tag{3.2}
\]

Combining (3.1)--(3.2) proves (0.7). Hence the positive Gaussian profile
flow, once chosen commonly across all \(q\le H\), has a whole-column
integral rounding with \(o(W)\) profile discrepancy.

This is an approximate integer decomposition theorem for the precise
Minkowski sum appearing in the selector-conditioned configuration LP. It
does not assume its semigroup is normal.

## 4. Relation to determinant-two minors

A determinant-two minor certifies failure of TU and can create an exact
index-two hole. It does not by itself create a stable \(o(W)\)-rounding
obstruction.

At a basic representation, every exact congruence defect is supported on
the at most \(D\) fractional fibres. One may:

1. round those fibres arbitrarily and charge at most \(2CDM\);
2. omit them as an owner reserve of mass at most \(DM\); or
3. retain them for a final parity absorber.

On the profile scale all three costs are \(o(W)\). Thus a replicated
triangle minor can obstruct exact equality, but it yields a linear
discrepancy only if the number of independent triangle residues is at
least

\[
                              \Omega(W/M).                         \tag{4.1}
\]

The profile quotient has lattice rank \(D=o(W/M)\), so such a family
cannot exist there.

This also explains why a Graver-basis bound is unnecessary for approximate
rounding. Graver moves matter if one insists on reaching an exact lattice
point while retaining every fibre. The basic-point theorem already
concentrates every failure of exact integrality into an \(o(W)\) reserve.

## 5. Exact absorber criterion

The preceding theorem leaves an explicit exact-completion problem on the
reserve \({\cal R}\). Fix provisional reserve columns
\(a_f^0\), and define its difference configuration

\[
 {\cal D}_{\cal R}
   =\left\{\sum_{f\in{\cal R}}
       (a_{f,\omega_f}-a_f^0):
       \omega_f\in\Omega_f\right\}.                                \tag{5.1}
\]

Let

\[
 {\cal L}_{\cal R}
   =\sum_{f\in{\cal R}}
      \left\langle
        a_{f,\omega}-a_{f,\omega'}:
        \omega,\omega'\in\Omega_f
      \right\rangle_{\mathbb Z}                                  \tag{5.2}
\]

be its difference lattice. If the rounded core leaves residual \(r\), an
exact completion exists precisely when

\[
                              -r\in{\cal D}_{\cal R}.              \tag{5.3}
\]

Lattice membership

\[
                              -r\in{\cal L}_{\cal R}               \tag{5.4}
\]

is only necessary. A Graver or normality theorem for the reserve must also
prove positivity, namely (5.3).

An absorber sufficient for exact completion is therefore a reserve for
which:

1. all permitted residuals satisfy the lattice congruences (5.4);
2. the reserve zonotope contains those residuals with a fixed interior
   margin; and
3. the reserve semigroup is normal in that interior region.

The determinant-two minors affect item 1 by one parity bit. Replicating a
cell twice removes that one saturation defect, but does not prove item 3.

For coefficient one, exact completion of the reserve is unnecessary if
its full signed all-depth mass is \(o(W)\); arbitrary rounding already
gives (0.4).

## 6. Dependent rounding and Graver moves

Independent choice of one option per fibre has order-one target
fluctuations and need not give \(o(W)\) literal holes. Theorem 2.1 is
different: it first fixes the entire fractional load vector and then takes
a basic representation of that same point. This uses global dependence
between fibres and preserves the load exactly outside at most \(D\)
groups.

Standard dependent rounding may reduce the discrepancy contributed by
the exceptional groups, but it cannot improve the structural bound
\(s\le D\) without additional column relations. Conversely, the full
Graver basis connects two integral points in the same exact fibre, but
does not produce an integral point near a fractional one if the relevant
semigroup class is empty.

Thus the correct order is:

\[
\boxed{
\text{fractional profile point}
\ \longrightarrow\
\text{basic representation}
\ \longrightarrow\
\text{at most \(D\) reserve fibres}
\ \longrightarrow\
\text{round or absorb}.}                                           \tag{6.1}
\]

## 7. Stable parity and odd-set obstructions

Let \(\chi:\mathbb Z^D\to\mathbb Z/2\mathbb Z\) be a parity functional.
If \(\chi(a_{f,\omega})\) is independent of \(\omega\) for every fibre,
then every integral selection has the fixed residue

\[
                         \chi\left(\sum_fa_f\right)
                          =\sum_f\chi(a_f).                         \tag{7.1}
\]

This can obstruct one exact balanced quota vector. But changing one target
load repairs one parity bit, so one such invariant costs \(O(1)\), not
\(\Omega(W)\).

A stable obstruction to (0.4) requires either:

1. \(\Omega(W/M)\) independent parity functionals whose repairs require
   disjoint fibre mass;
2. an odd-set inequality violated by \(cW\); or
3. a semigroup hole at \(\ell^1\)-distance \(cW\) from every integral
   configuration.

The Gaussian profile quotient has only \(D=o(W/M)\) independent row
directions, so none of these can be supported there. The full literal
target ledger may have enough independent directions, and the theorem
does not rule out such an obstruction below profile resolution.

No stable literal parity or odd-set family is currently exhibited by the
packet columns. A determinant-two minor without an isolating face or
independent replication is not such a family.

## 8. Precise surviving gate

The grouped integrality question now splits cleanly.

### Closed

Given a common all-depth fractional point in the positive Gaussian profile
flow, one can choose one whole packet/compiler column per owner fibre with
\(o(W)\) aggregate profile discrepancy. TU and exact normality are not
needed.

### Still open

To obtain literal target holes \(o(W)\), one needs one of:

1. a refinement of the quotient whose effective row rank \(D_{\rm eff}\)
   still satisfies

   \[
                              HD_{\rm eff}M=o(W);                  \tag{8.1}
   \]

2. a within-profile absorber which redistributes the \(o(W)\) profile
   error among literal targets;
3. a proof that the literal column semigroup is normal away from an
   \(o(W)\) boundary; or
4. a stable literal parity/odd-set obstruction of the form in Section 7.

The full literal row count is \(\Theta(HW)\), so Theorem 2.1 alone does not
finish this step. Packet/chronology grouping is integralized at the
Gaussian profile scale; literal within-profile balancing is the sole
remaining integrality gate.
