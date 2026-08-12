# Triangular one-copy rotor obstruction audit

**Date:** 2026-08-02  
**Lane:** A, integral coloured rotor fusion  
**Status:** exact scope audit.  The known quotient holes do not obstruct the
canonical large-
\(k\) triangular Boolean profile.  The smallest obstruction on the literal
central slice is the \(k=4\) state-parity example, and its exact open-route
repair cost is one.  No one-copy rounding theorem is proved here.

## 1. The target and the transfer question

Put

\[
 r=\lceil k/2\rceil,\qquad W=\binom{k}{r},\qquad
 \Lambda=\sum_{s=1}^{r-1}\binom{k}{s},
\]

and let \(d\) be the least integer with

\[
 dW+\binom{d+1}{2}\geq\Lambda.
\]

For the left-filled Ferrers boundary write \(b_s\) for the number of
boundary cells of rank \(s\), and

\[
 n_s=\binom{k}{s}-b_s,qquad q_s=n_s/W.                 \tag{1.1}
\]

The desired integral lower object chooses one literal trace for every one
of the \(W\) rank-\(r\) owners and covers each of the \(n_s\) residual
named rank-\(s\) targets once.  It may use a bounded rooted sidecar and is
then required to have only boundedly many Euler components (ideally one).

An obstruction proved after additionally freezing an age-type multiset, a
particular pull-block histogram, or one same-owner package transfers to this
target only if those extra data are forced by (1.1).  They are not part of
the triangular target itself.

## 2. Exact audit of the recorded obstructions

### Theorem 2.1 (parameter and quantifier separation)

The four recorded rotor obstructions have the following exact scope.

1. The pull-block integer hole with

   \[
   (c,d,W)=(2,2,3),\qquad (N_1,N_2)=(1,1),
   \]

   is not a canonical triangular instance.  Since \(c=r-d-1\), it would
   require \(r=5\), hence central \(k\in\{9,10\}\), where the Boolean owner
   counts are respectively \(126\) and \(252\), not three.

2. The saturated marked-age hole

   \[
   (r,d,W)=(7,3,2),\qquad n_1=\cdots=n_6=1             \tag{2.1}
   \]

   is not a canonical triangular instance.  Central rank \(r=7\) forces
   \(k\in\{13,14\}\), and then \(W\in\{1716,3432\}\).  Moreover its
   normalized profile is the constant vector \(q_s=1/2\), whereas the
   canonical profile has \(q_1\leq14/1716<1/2\).

3. The forced-rotation necklace theorem assumes the complete uniform
   multiset of all positive \((d+1)\)-part compositions of \(r\), one copy
   of each.  The triangular equations prescribe the rank histogram (1.1),
   owners, and eventually named targets; they do not prescribe that type
   multiset.  Consequently the necklace count and its occurrence-edit floor
   are conditional lower bounds for that frozen decomposition, not cuts of
   the triangular one-copy polytope.

4. The primitive package

   \[
   (1,2,1)\longleftrightarrow(2,1,1)                  \tag{2.2}
   \]

   has no two-state *same-owner* labelled lift.  This proves that a formal
   primitive aggregate generator need not lift package by package.  It does
   not forbid a global lift which rethreads occurrences from different
   packages and assigns different owners.

5. At \(k=10\), the nonintegrality

   \[
   W x_{1,1}=605/29                                   \tag{2.3}
   \]

   really belongs to the canonical symmetric pull decomposition.  It
   forbids retaining that exact block-start histogram.  It does not forbid
   the triangular target: `answers/k10.word` is a verified alternative
   integral architecture.

6. The reversible-menu parity family with \(r=2,d=1\) is on the central
   slice only for \(k=3,4\).  Its extension to all even \(k>4\) is a valid
   generic no-go but is not the central-rank triangular family.  The
   determinant-two one-owner fibre and the incomplete star family are
   likewise matrix/method obstructions, not complete canonical instances.

#### Proof

Items 1 and 2 are the displayed substitutions into
\(r=\lceil k/2\rceil\) and \(W=\binom{k}{r}\).  Item 3 follows because the
proof of forced rotation sums coordinate inequalities over the *uniform
positive-composition multiset*; changing the integer type multiplicities
changes those coordinate sums and permits positive slack.  Item 4 is
exactly the disjoint-cell contradiction in the primitive-lift theorem, whose
hypothesis keeps one owner and two prescribed states.  Item 5 is only a
Parikh equation for one chosen fractional decomposition; its converse would
incorrectly assert uniqueness of that decomposition.  The verified
`k=10` certificate supplies a literal counterexample to such a converse.
Item 6 follows from \(2=\lceil k/2\rceil\), which gives \(k\in\{3,4\}\).
\(\square\)

### Corollary 2.2 (aggregate large-\(k\) obstructions are already cleared)

For every \(k\geq31\), the canonical vector (1.1), in its alpha/role
coordinates, belongs exactly to the integer uniform-rotor semigroup.
Therefore no obstruction living solely in the aggregate age-signature
semigroup or its first-moment lattice can rule out the canonical target in
that range.

This corollary uses the independently audited two-buffer conductor theorem.
It says nothing about a primitive labelled lift: owner colours, named target
colours, literal state balance, and connectivity are absent from that
semigroup.

## 3. The canonical saturated profile is off the rigid rotation face

The first-moment theorem gives an additional target-specific separation
whenever the owner bank is saturated:

\[
                         \sum_{s=1}^{r-1} n_s=dW.       \tag{3.1}
\]

Then every chosen owner occurrence must mark all \(d\) of its distinct
proper suffix ranks.

### Theorem 3.1 (exact covariance certificate)

Assume (3.1), \(r\geq3\), and the canonical monotonicity

\[
                         q_1\leq\cdots\leq q_{r-1}.
\]

Let

\[
                         F=\sum_{s=1}^{r-1}s n_s.
\]

Then

\[
 \boxed{
 2F-rdW={2W\over r-1}
       \sum_{1\leq i<j\leq r-1}(j-i)(q_j-q_i)>0.}      \tag{3.2}
\]

Consequently no integral realization of the canonical saturated histogram
can lie wholly on the zero-slack forced-rotation face.  At least one
positive-slack age transition is necessary.

#### Proof

For \(n=r-1\), direct expansion gives the covariance identity

\[
 \sum_{i<j}(j-i)(q_j-q_i)
 =n\sum_i i q_i-\Big(\sum_i i\Big)\Big(\sum_iq_i\Big).
\]

Use \(\sum_iq_i=d\), \(\sum_i i=nr/2\), and multiply by
\(2W/n\) to obtain (3.2).  Every summand is nonnegative.  The inequality is
strict because the canonical vector is not constant: for \(k\geq5\),

\[
 n_1\leq k<\binom{k}{r-1}-d\leq n_{r-1}.
\]

The finite saturated cases also satisfy this inequality directly.  Finally,
the first-moment gradient identity says equality
\(2F=rdW\) holds exactly when every used transition is a block rotation.
Thus strict (3.2) excludes that face. \(\square\)

This is only a rigidity exclusion, not a fusion theorem.  The positive
first-moment excess permits slack but does not by itself construct the
owner-coloured transitions which spend it.

## 4. The smallest actual central obstruction costs exactly one

The parity obstruction does meet the triangular central slice at
\((k,r,d)=(4,2,1)\).  It is also completely absorbed at additive cost one.

### Theorem 4.1 (literal \(k=4\) calibration)

There is no owner-once balanced circuit or unbridged open trail using the
six pair owners of \([4]\).  There is, however, an owner-once, singleton-
target-exact connected open chronology after adding exactly one unmarked
route edge.

#### Proof

One trace per pair owner is an orientation of \(K_4\).  Every vertex has
odd underlying degree three, so all four divergences are odd.  A circuit
has no nonzero divergence and an open trail has only two boundary vertices;
neither is possible without a route edge.

Use the six owner arcs

\[
 0\to1,quad1\to2,quad2\to0,quad3\to0,quad
 1\to3,quad2\to3.                                    \tag{4.1}
\]

Their divergence vector is \((-1,+1,+1,-1)\).  Add the unmarked route arc
\(0\to1\).  The new divergence is \((0,0,+1,-1)\), and the support is
connected, so it has an Euler trail from \(2\) to \(3\).  Mark the heads of
the four distinct selected owner arcs

\[
 2\to0,quad0\to1,quad1\to2,quad1\to3;              \tag{4.2}
\]

these are respectively the four singleton targets.  Hence all owners and
all residual lower targets are exact.  The parity lower bound and this
construction prove that the route cost is exactly one. \(\square\)

For \(k=3\), the pair-owner graph is \(K_3\), whose directed 3-cycle is
already balanced and singleton-target exact.  Thus \(k=4\) is the smallest
complete central Boolean parity obstruction.  It refutes a theorem claiming
zero-sidecar rounding uniformly for every dimension; it does **not** refute
\(B(k)+O(1)\).

## 5. Exact remaining obstruction class

After this audit, a genuine obstruction to the large-\(k\) triangular
one-copy target must survive the complete Boolean fibres.  In particular it
must be one of the following, with the boundary bank already included:

1. a character or state-cut certificate for the complete one-copy
   Minkowski sum of all owner option sets;
2. an owner--named-target Hall cut after literal representative widths are
   retained;
3. an unbounded minimum state discrepancy or component/overlap cost over
   every such exact selector; or
4. a common-cap/upper/residence obstruction carried by every lower-exact
   selector.

The recorded holes establish none of these for the canonical large-\(k\)
instance.  Conversely, their failure to transfer is not a positive
rounding theorem.  The live lower gate remains a Boolean-specific common
owner/target/state selection followed by coloured cycle fusion or a bounded
absorber.

## 6. Independent audit

The lightweight exact replay

```text
scratch/audit_a_triangular_rotor_obstruction_scope_20260802.py
```

checks the two parameter mismatches, exhausts all \(2^6\) orientations of
\(K_4\), verifies the zero-sidecar no-go and one-sidecar witness (4.1), and
checks its exact singleton-head marking.  It is evidence for the finite
calibrations; the displayed arguments prove the general statements.
