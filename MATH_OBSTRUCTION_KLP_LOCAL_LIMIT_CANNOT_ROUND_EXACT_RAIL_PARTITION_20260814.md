# The KLP local-limit theorem cannot round the exact rail partition at its natural scale

**Date:** 2026-08-14  
**Status:** unconditional theorem-interface obstruction.  It concerns a
direct invocation of the Kuperberg--Lovett--Peled subset theorem on the
complete catalogue of legal pure-rail components.  It does not obstruct a
new sparse-coordinate formulation, a multi-stage absorption proof, or a
specialized local-limit theorem whose bound depends on component rank rather
than the dimension of the full named-resource space.

## 1. The proposed invocation

Put

\[
 W=\binom{k}{R},\qquad q=d+1.
\]

Let \(\mathcal B\) be a finite parameterized catalogue containing every
legal nonmaximal pure rail used by the full owner-lattice theorem.  Parallel
parameterizations may be retained.  For every named owner
\(A\in\binom{[k]}R\), define the incidence function

\[
 f_A(Q)=\mathbf 1_{\{A\text{ is an owner of }Q\}},
 \qquad Q\in\mathcal B.                              \tag{1.1}
\]

Let

\[
 V_{\rm own}=\operatorname {span}_{\mathbb Q}
       \{f_A:A\in\tbinom{[k]}R\}\subseteq\mathbb Q^{\mathcal B}.
                                                               \tag{1.2}
\]

A direct KLP proposal chooses a subset \(\mathcal T\subseteq\mathcal B\)
whose average agrees with the catalogue average on this space (and,
possibly, on additional lower, upper, phase, or cap functions).  With the
normalization chosen so that each owner has load one, \(\mathcal T\) would
be an exact owner partition.

## 2. The named-owner space has full dimension

### Lemma 2.1

Under the central hypotheses of
`MATH_THEOREM_PURE_RAIL_FULL_OWNER_LATTICE_AND_DESIGNS_II_DIAGONAL_BARRIER_20260812.md`,

\[
                     \dim V_{\rm own}=W.             \tag{2.1}
\]

#### Proof

Let \(M\) be the \(W\times|\mathcal B|\) owner-incidence matrix, whose
column at \(Q\) is the named-owner vector of that rail.  The cited full
owner-lattice theorem proves that the integer column lattice of \(M\) is
all of \(\mathbb Z^W\).  In particular \(M\) has row rank \(W\) over
\(\mathbb Q\).  Its rows are exactly the functions (1.1), proving (2.1).
\(\square\)

Adding decorated target functions can only increase the dimension.  On the
same complete catalogue, treating the two incident owner facets as one
internal alternating configuration does not change (2.1): exact named-owner
coverage still contains these \(W\) independent rows.  A genuinely restricted
configuration catalogue requires a new row-rank calculation and is covered by
the restriction caveat below.

## 3. The KLP size hypothesis is on the wrong side of the owner count

The Kuperberg--Lovett--Peled main theorem states that, with its divisibility,
bounded integer bases, transitive symmetry, and constant-function hypotheses,
a subset of size \(s\) is guaranteed only when

\[
 \min(s,|\mathcal B|-s)
 \ge Cc_2c_3^2\dim(V)^6
       \log(2c_3\dim(V))^6,                         \tag{3.1}
\]

where \(C>0\) is absolute and \(c_2,c_3\ge1\).

Every nonempty legal rail in the present catalogue has at least two owners;
in the port-rich catalogue it has at least \(2q+2\).  Consequently an exact
owner partition has

\[
 s\le \frac W2,
 \qquad\text{and in the port-rich case}\qquad
 s\le\frac{W}{2q+2}.                                \tag{3.2}
\]

### Theorem 3.1 (direct KLP invocation is quantitatively impossible)

For all sufficiently large \(W\), no exact owner partition can satisfy the
KLP lower bound (3.1) on the full named-owner incidence space.

#### Proof

By Lemma 2.1, every KLP space \(V\) on this complete catalogue which
contains the named-owner incidence space \(V_{\rm own}\) has
\(\dim(V)\ge W\).  Since \(c_2,c_3\ge1\), the right side of (3.1) is at
least

\[
 C W^6\log(2W)^6.                                   \tag{3.3}
\]

The left side is at most \(s\le W/2\) by (3.2).  Inequalities (3.2) and
(3.3) are incompatible once \(W\) is large. \(\square\)

This conclusion is independent of how favorable the local rail codegrees
are and independent of the value of the KLP local-decoding constant
\(c_3\).  Even the impossible optimistic value \(c_3=1\) leaves a sixth
power of a space whose dimension already exceeds the number of selected
components by a factor \(\Omega(q)\).

A deliberately restricted catalogue can have a smaller row rank; this note
does not rule out that route. Such a restriction must separately prove
named eligibility and exact coverage—uniform point roles are insufficient—and
cannot import the complete-catalogue rank calculation into its own incidence
space.

## 4. Why optional marks and type mixing do not repair the invocation

Optional lower or upper marks are valuable for lattice generation: changing
one designation can create a short signed unit in a target coordinate.  But
they append constraint rows and cannot reduce the independent owner block
(2.1).  They therefore make (3.1) no easier.

Mixing consecutive periods inside the complete catalogue removes scalar
divisibility obstructions, but the natural ground-coordinate symmetry then
has several component-type orbits and therefore does not by itself verify the
theorem's transitivity hypothesis.  There could in principle be a larger
abstract symmetry group of the function space, so orbit count alone is not a
transitivity obstruction.  This issue is immaterial to Theorem 3.1: even
granting transitivity for free does not fix the size contradiction, because
every exact mixed-period partition still selects fewer than \(W/2\)
components while retaining the \(W\)-dimensional owner system.

## 5. Exact surviving routes

The obstruction rules out only the most direct local-central-limit shortcut:

\[
 \text{all rail copies as }\mathcal B
 \quad+\quad
 \text{all named resources as }V
 \quad\Longrightarrow\quad
 \text{invoke KLP once}.
\]

It leaves three structurally different possibilities.

1. **Nibble plus absorption.**  Use the small external configuration
   codegrees to obtain a structured leave, then absorb it by explicit
   positive rail trades.
2. **Compressed regenerative state.**  Prove that a much smaller family of
   constraints implies all named equations through a hereditary compiler;
   the compression must be a theorem, since point roles alone are known not
   to imply named coverage.
3. **A specialized exact theorem.**  Prove a local-limit or design result
   whose quantitative cost depends on the local configuration rank and
   extendability, rather than on the sixth power of the full named-resource
   dimension.

Thus full signed lattice saturation is still useful for an absorber, but it
does not place the natural exact partition inside the quantitative range of
the existing KLP theorem.

## Reference

G. Kuperberg, S. Lovett, and R. Peled, *Probabilistic existence of regular
combinatorial structures*, Geom. Funct. Anal. 27 (2017), Theorem 2.4
(arXiv:1302.4295).
