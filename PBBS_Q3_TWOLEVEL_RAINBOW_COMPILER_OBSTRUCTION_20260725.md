# A depth-three compiler obstruction with two complete rainbow shadows

Date: 2026-07-25

Method: exact mathematics only.

## 0. Outcome

The star obstruction admits a second exact suspension. For every
\(R\ge5\) there is a cyclic rank-four Johnson walk with \(S=2R\) owners
such that

* every depth-one lower intersection is distinct;
* every depth-two lower intersection is distinct and floor-correct;
* the repeated depth-three intersections are floor-correct; and
* every arbitrary nonzero contiguous-OR word covering the lower data
  through depth three has

\[
 \boxed{L\ge S+\frac{S}{24}.}                     \tag{0.1}
\]

This reaches the first residence length not automatically excluded by the
canonical PBBS gap theorem: PBBS has no projected positive runs of length
one or two, but it does have length-three runs coming from gap-five omitted
labels. Thus neither first-shadow nor two-level lower rainbowness is a
black-box substitute for the missing PBBS-specific global rethreading.

## 1. Explicit rank-four walk

Use distinct coordinates

\[
 b_0,\ldots,b_{R-1},p_0,\ldots,p_{R-1},
\]

with subscripts modulo \(R\). Put

\[
\begin{aligned}
 A_t&=\{b_t,b_{t+1},b_{t+2},p_{t+1}\},\\
 D_t&=\{b_{t+1},b_{t+2},p_{t+1},p_{t+2}\}.
\end{aligned}                                      \tag{1.1}
\]

Take the cyclic owner sequence

\[
 A_0,D_0,A_1,D_1,\ldots,A_{R-1},D_{R-1}.          \tag{1.2}
\]

Consecutive owners are Johnson adjacent.

### Depth one

\[
\begin{aligned}
 A_t\cap D_t
   &=\{b_{t+1},b_{t+2},p_{t+1}\},\\
 D_t\cap A_{t+1}
   &=\{b_{t+1},b_{t+2},p_{t+2}\}.
\end{aligned}                                      \tag{1.3}
\]

All \(2R\) displayed triples are pairwise distinct.

### Depth two

\[
\begin{aligned}
 A_t\cap D_t\cap A_{t+1}
   &=\{b_{t+1},b_{t+2}\}=:X_{t+1},\\
 D_t\cap A_{t+1}\cap D_{t+1}
   &=\{b_{t+2},p_{t+2}\}=:Y_{t+2}.
\end{aligned}                                      \tag{1.4}
\]

The \(2R\) pairs \(X_t,Y_t\) are pairwise distinct. Their rank is
\(4-2=2\), so all are floor-correct.

### Depth three

\[
\begin{aligned}
 A_t\cap D_t\cap A_{t+1}\cap D_{t+1}
   &=\{b_{t+2}\},\\
 D_t\cap A_{t+1}\cap D_{t+1}\cap A_{t+2}
   &=\{b_{t+2}\}.
\end{aligned}                                      \tag{1.5}
\]

These have the floor-correct rank \(4-3=1\).

## 2. The old hard target family is still present

The depth-three singletons in (1.5), the depth-two pairs in (1.4), and
the depth-one triples in (1.3) are precisely the three layers in the
arbitrary-word H1 star obstruction:

\[
\begin{array}{c|c}
\text{star target}&\text{rank-four realization}\\ \hline
\{b_t\}&\text{depth-three lower target},\\
X_t,Y_t&\text{depth-two lower target},\\
U_t^-,U_t^+&\text{depth-one lower target}.
\end{array}                                        \tag{2.1}
\]

The canonicalization and mandatory-order proof from that obstruction
therefore applies without change. Any word covering the complete
depth-three target family covers this hard subfamily, and hence

\[
 L\ge2R+\frac{R}{12}
   =S+\frac{S}{24}.                                \tag{2.2}
\]

Notice that (2.2) does not even need the rank-four owners or any upper
unions. Adding those requirements cannot reduce the minimum length.

## 3. Fixed-core and odd-graph lifts

Adjoin a fixed core of size \(k-4\) to reach every rank \(k\ge4\).
Projection back to the active coordinates preserves the lower bound.

For the complement-projected PBBS rank, take \(k=m+1\), so the fixed core
has size \(m-3\). The example fits in \([2m+1]\) when

\[
 2R+(m-3)\le2m+1,
\]

allowing \(S=2R=\Theta(m)\). Because the depth-one lower colours (1.3)
are distinct rank-\(m\) sets, alternating them with the complements of
the lifted owners gives a simple integral odd-graph cycle. Again, this is
local odd-graph compatibility, not membership in the canonical PBBS
factor.

## 4. Exact implication for coefficient one

The canonical PBBS gap theorem removes projected positive residences of
length one and two, so it automatically avoids the unsuspended and
once-suspended shortest-run obstructions. Gap-five returns produce
residence length three, and the twice-suspended construction proves that
at this first permitted depth even two complete rainbow lower layers do
not force an \(S+O(1)\) arbitrary-word compiler.

Therefore the surviving coefficient-one theorem must use information not
contained in

* Johnson adjacency,
* exact odd-graph incidence,
* distinct first shadows, or
* distinct second shadows.

It must exploit the canonical PBBS quotient/phase chronology, a global
residence packing estimate, or a genuine cross-packet carrier rethreading.
