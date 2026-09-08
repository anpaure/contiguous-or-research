# Ferrers nested flags are exactly an equitable chain problem on a punctured half lattice

**Date:** 2026-08-07  
**Status:** unconditional equivalence and literature boundary.  This note
does not prove the sharp nested-flag theorem.  It identifies that theorem
with an exact minimum-chain balancing problem and records why the currently
proved uniform-chain results do not apply at the required coefficient.

## 1. Setup

Fix (k) and a middle rank (R), and put

\[
 \mathcal O=\binom{[k]}R,\qquad
 W=|\mathcal O|,\qquad
 \mathcal L=\{S\subseteq[k]:1\le |S|<R\},\qquad
 \Lambda=|\mathcal L|.
\tag{1.1}
\]

Fix a depth (d) and a boundary profile

\[
 b=(b_1,\ldots,b_{R-1}),\qquad
 0\le b_s\le\binom ks,
\tag{1.2}
\]

with

\[
 N_b:=\sum_{s=1}^{R-1}\left(\binom ks-b_s\right)\le dW.
\tag{1.3}
\]

For named boundary families

\[
 \mathcal B_s\subseteq\binom{[k]}s,qquad |\mathcal B_s|=b_s,
\tag{1.4}
\]

write

\[
 P(\mathcal B)
 :=\mathcal O\ \cup\
 \left(\mathcal L\setminus\bigcup_s\mathcal B_s\right),
\tag{1.5}
\]

ordered by inclusion.  This is the lower Boolean half, including its owner
shore, punctured by the named Ferrers boundary.

The exact capacity-(d) containment-flow theorem proves that the boundary
families and a residual assignment to at most (d) slots per owner can
always be chosen under (1.3).  It does not make the targets assigned to one
owner comparable.  The next theorem identifies precisely what is missing.

## 2. Exact punctured-half equivalence

### Theorem 2.1 (Ferrers punctured-half chain equivalence)

The following are equivalent.

1. There are boundary families (1.4) and chains

   \[
    C_T\subseteq 2^T\setminus\{\varnothing,T\},
    \qquad T\in\mathcal O,
   \tag{2.1}
   \]

   which partition the residual lower targets and satisfy
   (|C_T|\le d) for every (T).

2. For some boundary families (1.4), the punctured poset
   (P(\mathcal B)) has a partition into exactly (W) chains, each of
   size at most (d+1).

3. There are boundary families (1.4), a partition

   \[
    \mathcal L\setminus\bigcup_s\mathcal B_s
      =A_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}A_d,
   \tag{2.2}
   \]

   and inclusion injections

   \[
    A_1\hookrightarrow\mathcal O,
    \qquad A_{i+1}\hookrightarrow A_i\quad(1\le i<d).
   \tag{2.3}
   \]

For fixed boundary families and fixed slices, (2.3) is equivalent to the
ordinary Hall inequalities on the (d) adjacent inclusion graphs.

#### Proof

Given (1), append (T) to (C_T).  The resulting (W) chains partition
(P(\mathcal B)) and have size at most (d+1), proving (2).

Conversely, every chain meets the rank-(R) shore in at most one element.
A partition of (P(\mathcal B)) into (W) chains must therefore place its
(W) owners in distinct chains.  Removing the owner from each chain gives
(1).

The equivalence of (1) and (3) is the right-aligned ladder construction:
place a target in (A_i) when it is the (i)-th target below its owner.
Consecutive members of a chain give (2.3).  Conversely, orient all the
injections toward smaller slice index.  Their components are vertex-disjoint
inclusion paths ending at distinct owners.  Hall's theorem gives the last
assertion.  \(\square\)

### Proposition 2.2 (the number of chains and the anchors are already free)

For every choice of boundary families, the width of (P(\mathcal B)) is
exactly (W).  Hence Dilworth already gives a partition into (W) chains;
the only missing condition in Theorem 2.1(2) is the maximum chain size.

#### Proof

The owner shore is an antichain of size (W), so the width is at least
(W).  The poset is an induced subposet of the Boolean lattice, whose width
is (W) by Sperner's theorem, so its width is at most (W).  Dilworth gives
a (W)-chain partition.  As in the proof of Theorem 2.1, every such
partition has one distinct owner in each chain.  \(\square\)

Thus neither the chain count nor distinct owner containment is the static
obstruction.  The obstruction is **equitable balancing inside a minimum
chain decomposition**.

### Corollary 2.3 (equitable chromatic form)

Let \(G_{\mathcal B}\) be the incomparability graph of
\(P(\mathcal B)\). Then

\[
 \chi(G_{\mathcal B})=\omega(G_{\mathcal B})=W.
\tag{2.4}
\]

Theorem 2.1 is equivalent to choosing the prescribed rank-profiled
punctures so that \(G_{\mathcal B}\) has a proper \(W\)-colouring with
every colour class of size at most \(d+1\). In the positive-boundary face
of Corollary 3.1, every colour class must have size exactly \(d+1\).

#### Proof

Independent sets of an incomparability graph are precisely poset chains.
Proposition 2.2 gives both the chromatic number and clique number, and
Theorem 2.1 gives the bounded-colour-class statement. \(\square\)

Thus the static gate is also an exact equitable colouring problem at the
chromatic number of a perfect graph. Perfectness supplies the number of
colours, but not equitable class sizes.

## 3. The optimal boundary is an exact equal-chain problem

Let (d=d(k)) be the optimal deadline and put

\[
 h=(\Lambda-dW)_+.
\tag{3.1}
\]

The triangular lower-bound ledger gives

\[
 0\le h\le\binom{d+1}{2}=O(k),
\tag{3.2}
\]

and the optimal Ferrers boundary has total size

\[
 \sum_s b_s=h.
\tag{3.3}
\]

Let

\[
 D=\left\lceil\frac\Lambda W\right\rceil.
\tag{3.4}
\]

The established deadline arithmetic gives (d\le D\le d+1).  More
precisely,

\[
 h=0\Longrightarrow D=d,
 \qquad
 h>0\Longrightarrow D=d+1.
\tag{3.5}
\]

### Corollary 3.1 (equal-chain and ceiling-optimal faces)

For the optimal Ferrers profile:

* If (h>0), then

  \[
   |P(\mathcal B)|=W+(\Lambda-h)=(d+1)W.
  \tag{3.6}
  \]

  Hence Theorem 2.1 is equivalent to choosing the named boundary so that
  (P(\mathcal B)) has a partition into (W) chains **all of size exactly
  (d+1)**.

* If (h=0), put (sigma=dW-\Lambda).  Then

  \[
   |P(\varnothing)|=(d+1)W-\sigma,
   \qquad 0\le\sigma<W,
  \tag{3.7}
  \]

  and (d+1=\lceil |P(\varnothing)|/W\rceil).  Theorem 2.1 is therefore
  equivalent to a minimum (W)-chain decomposition attaining the smallest
  possible maximum chain size.

#### Proof

Equation (3.6) follows from (h=\Lambda-dW).  A (W)-chain partition with
maximum (d+1) has total capacity ((d+1)W), so equality in total size
forces every chain to use all (d+1) positions.

If (h=0), then (D=d), so
(d-1<\Lambda/W\le d).  This gives (0\le\sigma<W) and (3.7).  Any
partition into (W) chains has maximum at least the ceiling of its average,
namely (d+1), so the requested maximum is optimal.  \(\square\)

This is sharper than saying merely that the residual targets fit into
(dW) slots.  In the positive-boundary dimensions, the desired object is
literally an equal-chain decomposition of a rank-profiled punctured Boolean
half.

## 4. The exact new chain statement

The remaining static theorem can be stated without any OR-word language.

> **Ferrers-profiled equitable half-chain conjecture (FEHC).**  For the
> optimal deadline (d(k)) and an admissible triangular Ferrers profile
> (b), one can choose exactly (b_s) deleted elements from every rank
> (s<R) so that the punctured poset (P(\mathcal B)) has a minimum
> (W)-chain decomposition of maximum (d+1).

Equivalently, by Theorem 2.1, one can choose (d) globally correlated
rank-interleaved slices whose adjacent inclusion graphs all satisfy Hall.

FEHC is the sharp static nested-flag row.  It is weaker than physical OR
serialization: it supplies no ordering of the (W) owner flags satisfying
the coordinate-age countdown law, no upper interval language, and no common
cap.

It is also more specialized than the full Füredi conjecture: the poset is a
half lattice with only (O(k)) rank-profiled punctures, and the punctures
may be chosen.  But it is not a known consequence of Füredi's conjecture.
An arbitrary equitable full-lattice chain partition need not be
rank-symmetric, so one chain may place most of its mass below the middle.
Nor does it provide the prescribed ranks of the (h) deleted boundary
elements.

The directly sufficient classical-looking strengthening would be a
**rank-symmetric equitable** minimum-chain decomposition with a
profile-controlled middle cut.  That strengthening is itself unproved.

## 5. Why the currently proved chain theorems do not apply

### 5.1 Tomon's rank-symmetric decomposition

Tomon's rank-symmetric theorem gives a minimum (W)-chain decomposition of
the full Boolean lattice with every chain of size (O(\sqrt{k})).  In the
explicit form already audited in this repository, restriction below the
middle gives owner chains of depth at most

\[
 \frac{13}{2}\sqrt{k}+1
   =\bigl(13\sqrt{2/\pi}+o(1)\bigr)d,
\tag{5.1}
\]

and hence depth at most (11d) for large (k).  This proves constant-factor
chainization, not coefficient one.

### 5.2 Tomon's equal-(c) partition theorem

The published sufficient hypothesis is

\[
 k>500c^2.
\tag{5.2}
\]

At the required half-chain scale (c=d+O(1)),

\[
 \frac{500c^2}{k}\longrightarrow\frac{500\pi}{8}>196,
\tag{5.3}
\]

so the hypothesis fails by a fixed factor.  At the corresponding
full-lattice scale (c=2d+O(1)), the limiting factor exceeds (785).
Moreover, the theorem concerns the full Boolean lattice and does not supply
the prescribed Ferrers punctures or owner slices.

### 5.3 Sudakov--Tomon--Wagner

The proved STW upper-half construction gives (W) chains for which all but
an (o(1)) proportion have asymptotically average size.  Its restriction
does yield an anchored depth-(d) factor covering all but

\[
 O\!\left(\Lambda k^{-1/16+o(1)}\right)
\tag{5.4}
\]

lower targets.  This is asymptotically sharp, but the exceptional bank is
still exponential in (k), whereas the optimal Ferrers boundary has only
(O(k)) targets.  Thus it does not prove FEHC or an (O(1))-defect version.

The conjectural exact upper-half uniform partition would imply the
unpunctured cap-(D) statement.  By (3.5), this is the desired cap (d) in
the zero-boundary dimensions.  In the positive-boundary dimensions it gives
only cap (d+1) before puncturing; lowering that cap by one while deleting
the prescribed (h=O(k)) rank-profiled targets is exactly the new FEHC
refinement.

### 5.4 Füredi's conjecture

Füredi's equal-chain conjecture remains open.  It asks for a minimum
(W)-chain decomposition of the full Boolean lattice with chain sizes
differing by at most one.  Even that statement, without rank symmetry or a
controlled middle cut, does not immediately imply FEHC.  What is proved is
only asymptotic uniformity for almost all chains, not an all-chain additive
bound.

### 5.5 The 2026 chain-cover result is a different problem

The 2026 paper *Chain Covers in the Boolean Lattice* studies the least
number of chains whose union meets every strict (r)-term chain.  It does
not partition the vertices into (W) chains of prescribed or bounded size,
so its chain-cover estimates do not apply to FEHC.

## 6. Sharp verdict

The Ferrers capacity theorem and Proposition 2.2 together remove all of the
following as possible static obstructions:

* total capacity;
* ordinary containment Hall;
* the number (W) of owner chains;
* distinct owner anchors;
* and the exact boundary rank totals.

What remains is exactly

\[
 \boxed{
 \text{choose the named Ferrers punctures so that a width-}W
 \text{ Boolean-half poset has an equitable minimum chain partition}.}
\tag{6.1}
\]

No currently proved exact equal-chain theorem applies at
(d\sim\sqrt{\pi k/8}).  The best general static conclusions presently
available are:

* coefficient-one depth with an exponentially large (o(\Lambda)) leave;
* or zero leave with depth (2d+O(1)) (and, from the rank-symmetric theorem,
  another explicit constant-factor bound).

Even a proof of FEHC would close only the owner-local nested flags.  The
move-to-front countdown coupling of consecutive owners remains a separate
integral serialization theorem.

## References

* I. Tomon, *On a conjecture of Füredi*, European J. Combin. 49 (2015),
  1--12, DOI `10.1016/j.ejc.2015.02.026`.
* I. Tomon, *Improved bounds on the partitioning of the Boolean lattice into
  chains of equal size*, Discrete Math. 339 (2016), 333--343, DOI
  `10.1016/j.disc.2015.08.025`.
* I. Tomon, *Decompositions of the Boolean lattice into rank-symmetric
  chains*, Electron. J. Combin. 23(2) (2016), P2.53, arXiv:1509.07346.
* B. Sudakov, I. Tomon and A. Z. Wagner, *Uniform chain decompositions and
  applications*, Random Structures & Algorithms 60 (2022), 261--286,
  arXiv:1911.09533.
* Z. L. Nagy and B. Patkós, *Chain Covers in the Boolean Lattice*,
  arXiv:2606.29385 (2026); a different covering problem, as noted above.
