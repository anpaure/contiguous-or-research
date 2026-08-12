# Audit of the three attached exploratory notes

Date: 2026-07-25

This audit records only statements relevant to the coefficient-one target

\[
 \nu(k)\le(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\]

The three attachments are exploratory narratives rather than proofs.  They
do not close a current gate.  Two reformulations are useful; several proposed
reductions are either already known or too strong.

## 1. Exact Johnson-path formulation of a wreath factor

Put \(n=2m+1\), and let

\[
 X_j=I_\pi(j,m),\qquad j\in\mathbb Z_n.
\]

Then \((X_j)_j\) is an \(n\)-cycle in \(J(n,m)\).  For every
\(0\le q<m\),

\[
 \bigcap_{a=0}^{q}X_{j+a}=I_\pi(j+q,m-q),
 \tag{1.1}
\]

and

\[
 \bigcup_{a=0}^{q}X_{j+a}=I_\pi(j,m+q).
 \tag{1.2}
\]

Consequently an exact middle wreath factor has complete lower depth-\(q\)
shadow precisely when, for every
\(T\in\binom{[n]}{m-q}\), one factor cycle contains a consecutive
\((q+1)\)-vertex path wholly inside the up-set of \(T\).  Since the
intersection in (1.1) has exactly \(m-q\) elements, containment is enough
to force equality.

This is a clean equivalent formulation of the vertical gate.  It may be fed
directly into the mixed-frame rotor/SCD construction.

Complementation has the shifted identity

\[
 \binom{[n]}{m+q}\longleftrightarrow
 \binom{[n]}{m-(q-1)}.
 \tag{1.3}
\]

Thus lower depth \(q-1\) controls upper depth \(q\).  There is an index
shift; lower and upper depths with the same numerical \(q\) are not direct
complements.

## 2. The near-Ucycle reduction is not established

The notes repeatedly restrict to singleton entries and then identify the
middle states with FIFO windows.  Under that restriction, a leading-order
construction would indeed be a near-universal cycle for central subsets.
But a general OR word has ordered-partition states, and a depth-preserving
middle transition may replace a whole terminal block, not one singleton.
No argument in the attachments proves that the nonsingleton transitions can
be removed with \(o(W)\) cost.

This restriction is especially unsafe because the proved facet-braid word
and the fixed-core/rotor modules achieve their leading-order savings with
nonsingleton letters.  Therefore

\[
 \text{coefficient one}\Longrightarrow
 \text{central near-Ucycle}
\]

is not an available reduction.  A near-Ucycle remains a sufficient special
case, but it is at least as hard as an additional central universal-cycle
problem and should not replace the current OR-word gate.

## 3. Affine and translation-equivariant ideas

The AP wreath observations are correct but quantitatively negligible.  For
prime \(n\), the multiplier rows have exactly rainbow shadows on one affine
orbit, but only \(O(n^2)\) targets per rank, versus
\(\Theta(W)\) required targets.  The stronger audited statement is in
`MATH_ATTACK_AP_AGL_SHADOW_LEDGER_20260725.md`:

* no exact \(AGL(1,n)\)-invariant middle factor exists for prime
  \(n\ge7\);
* high-stabilizer targets have negligible total mass;
* the uniform affine fractional resolution is perfectly balanced but is
  only annealed and gives no good integral constituent.

Hence exact equivariance is obstructed, while an almost-equivariant
large-orbit core remains only a matching proposal.

## 4. Random wreaths and generic nibble arguments

The Poisson computation in the attachments agrees with the audited barrier:
for any fixed-density independent family, depths \(q=O(\sqrt m)\) contribute
\(\Theta(W\sqrt m)\) misses.  This does not prove impossibility of a
designed factor; it proves that an i.i.d.-like factor cannot work.

The growing-edge economical-cover proposal also does not cross the current
barrier.  Encoding all shallow rows of one atom gives growing uniformity,
and the nested adjacent-rank codegree is already \(\Omega(D/m)\).  The
isolated-reset ABKV architecture is rigorously capped at
\(o(\sqrt{\log m})\) depth.  The attachments do not supply a stronger
rounding theorem.

## 5. Product and repair suggestions

The fixed-dimensional product-box suggestions are closed by the existing
endpoint duals on positive-measure dominance sectors.  The incomplete
two-rate product/Ucycle calculation in the first attachment does not define
a valid OR word or prove distinctness of its middle windows.

Similarly, missed masks from different ranks cannot in general be repaired
at the cost of the maximum one-rank defect.  Such a saving requires a proved
common chain/word realization.  Endpoint throughput gives only one new mask
per rank per appended endpoint, and no cross-rank repair construction is
provided in the notes.

## 6. What the attachments add to the live program

The useful surviving statement is (1.1): the wreath vertical problem is an
exact consecutive-path hitting problem in Johnson up-sets.  Combined with
the new recursive orientation-cube factor, it suggests the following
precise mixed-frame target:

> Partition almost all middle owners into long pair-flip rotor cycles,
> allowing the coordinate pairing to vary between cycles, so that for every
> fixed \(A\) and every \(q\le A\sqrt m\), almost every rank-\(m-q\)
> up-set contains one consecutive \((q+1)\)-vertex segment, while the total
> cycle-cut toll is \(o(W)\).

The recursive cube factor already makes every such path shadow injective
inside one chosen orientation cube.  The unresolved mathematics is the
integral multi-frame ownership selection across cubes.  None of the three
attachments proves that selection.

