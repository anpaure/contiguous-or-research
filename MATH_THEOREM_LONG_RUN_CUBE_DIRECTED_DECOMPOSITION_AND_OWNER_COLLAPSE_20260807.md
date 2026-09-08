# Directed cube decomposition closes the direction gate, but the current owner map has an exact factor-two collapse

**Date:** 2026-08-07  
**Method:** symmetric directed Hamilton decomposition, followed by an exact
owner-fibre count  
**Status:** unconditional reduction and obstruction.  The unguarded
outgoing-direction gate is a theorem of Stong for every cube dimension
different from three.  This does **not** supply long-run cycles.  Moreover,
even an orthogonal long-run directed decomposition cannot be inserted as one
simple-owner fixed-frame factor in the construction of
`MATH_THEOREM_LONG_RUN_CUBE_DENSE_TOP_COMPONENT_20260807.md`: the two
orientations of every cube edge induce the same set-valued owner, so every
owner occurs twice.

## 1. The fixed frame

Fix disjoint sets

\[
 K,\qquad H_1,\ldots,H_h,\qquad P_i=\{a_i,b_i\}\quad(i\in[h]),
\]

with the sizes used in the long-run cube component.  For
\(z\in\{0,1\}^h\), let \(V(z)\) select one point of each pair \(P_i\).
The complete structured target bank on this frame is

\[
 \Sigma(F)=\{S(z,i):z\in\{0,1\}^h,\ i\in[h]\},
\]

where

\[
 S(z,i)=K\cup\bigcup_{j\ne i}H_j\cup V(z).
\tag{1.1}
\]

The missing bank recovers \(i\), and the payload recovers \(z\).  Hence

\[
 |\Sigma(F)|=h2^h.
\tag{1.2}
\]

Given an oriented Hamilton cycle \(C\) of \(Q_h\), write \(\tau_C(z)\)
for the direction of the edge leaving \(z\).  The component selected by
\(C\) is

\[
 \Sigma(C)=\{S(z,\tau_C(z)):z\in\{0,1\}^h\}.
\tag{1.3}
\]

## 2. Exact directed-decomposition equivalence

### Theorem 2.1

Let \(C_1,\ldots,C_h\) be directed Hamilton cycles of \(Q_h\).  The
following are equivalent.

1. For every vertex \(z\),
   \[
   \{\tau_{C_a}(z):a\in[h]\}=[h].
   \tag{2.1}
   \]
2. The directed cycles partition the arcs of the symmetric directed cube
   \(\overleftrightarrow{Q_h}\).
3. The target components \(\Sigma(C_a)\) partition the complete fixed-frame
   target bank \(\Sigma(F)\).

#### Proof

There are exactly \(h\) arcs leaving each vertex, one in each direction.
Every directed Hamilton cycle uses one outgoing arc there.  Thus (2.1) is
equivalent, vertex by vertex, to using every outgoing arc once.  This is
equivalent to a partition of all directed arcs, proving `1 iff 2`.
Equation (1.1) makes \((z,i)\mapsto S(z,i)\) injective, so the same
pointwise statement is exactly `2 iff 3`. \(\square\)

The bipartite matching version is also exact.  Split every directed cycle
at the parity bipartition of \(Q_h\).  Its even-to-odd arcs form a perfect
matching \(A_a\), its odd-to-even arcs form a perfect matching \(B_a\), and
\(A_a\cup B_a\) is Hamilton.  Consequently Theorem 2.1 is equivalent to
two one-factorizations

\[
 \{A_1,\ldots,A_h\},\qquad \{B_1,\ldots,B_h\}
\]

such that \(A_a\cup B_a\) is Hamilton for every \(a\).

## 3. The unguarded direction gate is already known

Stong proved that

\[
 \boxed{
 \overleftrightarrow{Q_h}\text{ decomposes into }h
 \text{ directed Hamilton cycles for every }h\ne3.
 }
\tag{3.1}
\]

Thus, in the asymptotic range \(h\ge4\), the outgoing-direction condition
of Theorem 2.1 is not an open problem.

The exception \(h=3\) is genuine.  It is irrelevant to the present
triangular regime, where \(h\to\infty\).

What (3.1) does **not** assert is a lower bound on same-direction transition
separation.  The long-run component needs every selected Hamilton cycle to
have

\[
 \operatorname{mrl}(C_a)\ge d+1.
\tag{3.2}
\]

Goddyn--Gvozdjak prove the existence of one Hamilton cycle in \(Q_h\) with
minimum run length at least \(h-O(\log h)\).  Their theorem does not make
\(h\) such cycles arc-disjoint, and Stong's theorem does not make its
cycles long-run.  Hence the simultaneous strengthening `(3.1)+(3.2)` is
still open from the cited results.

There is a basic necessary count.  If \(c_{a,i}\) is the number of
direction-\(i\) transitions in \(C_a\), then

\[
 c_{a,i}\le \left\lfloor\frac{2^h}{d+1}\right\rfloor,
 \qquad
 \sum_{a=1}^h c_{a,i}=2^h.
\tag{3.3}
\]

In particular \(d+1\le h\), consistent with the frame parameters but
showing that the desired family lies close to the extremal run-length
regime.

## 4. The owner map forgets orientation

For consecutive cube vertices \(u,v\), the owner in the long-run component
is

\[
 \boxed{
 O(uv)=K\cup\bigcup_{i=1}^hH_i\cup\bigl(V(u)\cup V(v)\bigr).
 }
\tag{4.1}
\]

This depends only on the unordered edge \(\{u,v\}\), not on its
orientation and not on the missing-bank label attached at either endpoint.

### Theorem 4.1 (factor-two owner collapse)

The fixed frame has exactly

\[
 h2^{h-1}
\tag{4.2}
\]

distinct owners of the form (4.1).  Any family of long-run cube components
whose owners are globally simple contains at most \(h/2\) components and
covers at most

\[
 h2^{h-1}=\frac12|\Sigma(F)|
\tag{4.3}
\]

fixed-frame targets.

In particular, a directed Hamilton decomposition from Theorem 2.1 uses
every owner in (4.1) exactly twice.

#### Proof

Distinct undirected cube edges have distinct coordinate-set payload unions,
so (4.1) injects the edge set of \(Q_h\) into the owner layer.  Since

\[
 |E(Q_h)|=h2^{h-1},
\]

this proves (4.2).

One Hamilton component uses \(2^h\) cube edges and hence \(2^h\) owners.
Global owner simplicity therefore forces the underlying undirected edge
sets of different components to be disjoint.  At most
\(|E(Q_h)|/2^h=h/2\) such components exist, and they contain at most the
number (4.3) of targets.

Finally, a directed decomposition uses both directed arcs above every
undirected edge.  Formula (4.1) identifies those two arcs, so every owner is
used exactly twice. \(\square\)

This is independent of run length.  Therefore proving the orthogonal
long-run directed-cube theorem would solve the fixed-frame **target**
partition, but would still fail the simple-owner gate exactly by a factor
of two.

## 5. The correct fixed-frame half-factor

Assume \(h\) is even.  An undirected Hamilton decomposition

\[
 E(Q_h)=E(D_1)\mathbin{\dot\cup}\cdots
        \mathbin{\dot\cup}E(D_{h/2})
\tag{5.1}
\]

uses every frame owner exactly once.  Orient each \(D_a\) arbitrarily.  At
each vertex, the \(h\) incident cube directions are partitioned into
\(h/2\) two-element pairs, one pair from each \(D_a\); the chosen
orientation selects one direction from each pair.  Consequently the
oriented components cover exactly \(h/2\) distinct target labels at every
payload vertex, hence exactly half of \(\Sigma(F)\).

Reversing all the orientations covers the complementary half, but repeats
the same owners.  This is another direct view of Theorem 4.1.

For the residence-aware construction the relevant unresolved local theorem
is therefore not the directed statement in isolation, but:

> **Long-run undirected half-factor.**  Find an undirected Hamilton
> decomposition of \(Q_h\) in which every cycle has minimum run length at
> least \(d+1\).

Even this theorem supplies only one owner-valid half of a fixed frame.  The
other targets must be represented through different frames or a different
owner geometry.

## 6. The exact global recoupling problem

Let

\[
 \mathcal T=\binom{[n]}{m-d-1},
 \qquad
 \mathcal O=\binom{[n]}m.
\]

Define a **half-frame packet** to consist of a labelled frame, a long-run
undirected Hamilton decomposition, and one orientation of each of its
cycles.  It contains

\[
 R=h2^{h-1}
\tag{6.1}
\]

distinct targets and the same number of distinct owners.  The remaining
top-factor problem is a two-resource exact packing problem:

* partition \(\mathcal T\) by target sets of half-frame packets;
* keep all packet owner sets disjoint in \(\mathcal O\);
* then couple the result to the delayed atoms, lower flags, and the other
  owner sectors.

This formulation permits the second half of one geometric frame to be
covered using different frame representations of the same global targets.
It avoids the impossible demand that one fixed frame carry both
orientations of every cube edge.

There is no scalar obstruction.  Let \(\mathcal P\) be any nonempty
\(S_n\)-invariant family of half-frame packets.  By transitivity, a fixed
target lies in \(d_T\) packets and a fixed owner lies in \(d_O\) packets.
Double counting gives

\[
 |\mathcal P|R=|\mathcal T|d_T=|\mathcal O|d_O.
\]

Weighting every packet by \(1/d_T\) gives target load one and owner load

\[
 \frac{d_O}{d_T}=\frac{|\mathcal T|}{|\mathcal O|}<1.
\tag{6.2}
\]

Thus the global half-frame hypergraph has a symmetric fractional packing
with exact target marginals and spare owner capacity.  What remains is
integral rounding with growing packet size

\[
 R=h2^{h-1}=\exp(\Theta(\sqrt m)),
\]

plus the other physical rows.  No cited Hamilton-decomposition theorem
performs this rounding.

### Theorem 6.1 (whole-cube divisibility obstruction)

An exact factor of \(\mathcal T\) cannot consist solely of whole long-run
cube components in the triangular regime.  This remains true if arbitrary
cube dimensions satisfying the residence requirement are mixed.

#### Proof

A whole Hamilton component on an \(s\)-cube contains exactly \(2^s\)
targets.  The required minimum run length is \(d+1\), while the elementary
cyclic transition count gives

\[
 \operatorname{mrl}(C)\le s.
\]

Thus every admissible cube dimension satisfies \(s\ge d+1\), and every
whole component size is divisible by \(2^{d+1}\).  Any union of such
components consequently has cardinality divisible by \(2^{d+1}\).

On the other hand, Kummer's theorem gives

\[
 v_2\binom nr
 =\#\{\text{binary carries in }r+(n-r)\}.
\tag{6.3}
\]

The number of binary columns is at most
\(\lfloor\log_2 n\rfloor+1\), so

\[
 v_2\binom nr\le \lfloor\log_2 n\rfloor+1.
\tag{6.4}
\]

But \(d=\Theta(\sqrt n)\).  Therefore, for all sufficiently large \(n\),

\[
 v_2|\mathcal T|<d+1,
\]

and \(2^{d+1}\nmid|\mathcal T|\).  Exact partition by whole admissible
cube components is impossible. \(\square\)

The same argument applies a fortiori to complete half-frame packets: a
packet of cube dimension \(s\) has size \(s2^{s-1}\), whose 2-adic
valuation is at least \(s-1\ge d\), whereas (6.4) is \(o(d)\).

This is a scalar **integral** obstruction despite the fractional point
(6.2).  Therefore the global construction necessarily needs at least one
of the following:

* truncated or opened cube packets with non-power-of-two target counts;
* a second non-cube packet family whose size lattice removes the 2-adic
  obstruction;
* or a correlated splice in which the unit of decomposition is not a
  whole cube Hamilton component.

The remainder cannot be dismissed as a bounded divisibility correction:
modulo \(2^{d+1}\), it may be exponentially large in \(d\).  A successful
opening theorem must therefore control physical boundary state rather than
pay for the remainder by appending its targets.

## 7. Correct frontier

The cube-frame situation is now separated into three statements.

1. **Outgoing-direction resolution:** proved by Stong for \(h\ne3\).
2. **Simultaneous long-run resolution:** not supplied by Stong or by the
   one-cycle Goddyn--Gvozdjak theorem.
3. **Simple-owner global factorization:** a full directed fixed-frame
   resolution is impossible in the present set-valued owner geometry;
   one must use owner-valid half-frames and recouple globally, or change the
   owner geometry so that orientation becomes visible.
4. **Whole-packet divisibility:** even globally varying the frames cannot
   partition the target layer using only complete admissible cube
   components; Kummer's theorem forces a non-cube or opened-packet sector.

The exact new obstruction is

\[
 \boxed{
 |\Sigma(F)|=h2^h,
 \qquad
 |\{\text{available frame owners}\}|=h2^{h-1}.
 }
\]

## References

* R. Stong, *Hamilton decompositions of directed cubes and products*,
  Discrete Mathematics **306** (2006), 2186--2204,
  DOI `10.1016/j.disc.2005.09.021`.
* L. Goddyn and P. Gvozdjak, *Binary Gray Codes with Long Bit Runs*,
  Electronic Journal of Combinatorics **10** (2003), R27.
