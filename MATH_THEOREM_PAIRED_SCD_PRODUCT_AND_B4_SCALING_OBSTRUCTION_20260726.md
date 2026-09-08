# Paired SCDs: exact product obstruction and the bounded-\(B_4\) scaling tax

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web input
is used.

## 0. Outcome

Let a **paired SCD** of \(B_{2m}\) mean two symmetric-chain
decompositions which agree at every nonmiddle rank and whose nontrivial
chains use opposite corners of each common central diamond, with the
radius-zero middle singleton chains common to both decompositions.
Equivalently,
if \(\mathcal A\) is the set of positive-radius middle members of the
first SCD and

\[
 g(X)=X-\alpha(X)+\beta(X),
\]

then \(g:\mathcal A\to\mathcal A\) must be a permutation.

The complement-symmetric \(B_4\) seed does not propagate through the
ordinary product-SCD recursion.  The failure is not special to BTK and is
not merely a monotone-potential argument.

1. In the standard rectangular product of arbitrary SCDs of
   \(B_{2a}\) and \(B_{2b}\), every pair of child chains having the
   same positive radius contributes a forced directed path of central
   alternate-corner moves ending at a radius-zero global singleton.
   Consequently the product SCD is never one member of a paired SCD when
   \(a,b\ge1\).
2. The exact number of these forced escapes is at least

   \[
    E_{a,b}=\sum_{r=1}^{\min(a,b)}c_{a,r}c_{b,r},
    \qquad
    c_{a,r}=\binom{2a}{a-r}-\binom{2a}{a-r-1}.
   \]

   For a \(B_4\) outer factor this is

   \[
    E_{2,m-2}=3c_{m-2,1}+c_{m-2,2}
             =\left(\frac78+o(1)\right)\frac{W_m}{m},
   \]

   where the second term is omitted when \(m<4\) and
   \(W_m=\binom{2m}{m}\).
3. More generally, even a nonstandard product construction whose central
   map is a permutation must use many cross-box diamonds.  For child-chain
   boxes \(C\times D\), the exact lower bound is

   \[
    E_{\mathrm{cross}}\ge
    W_aW_b-\mathrm{Cat}_a\mathrm{Cat}_b.
   \]

   With a fixed \(B_4\) outer factor this becomes

   \[
    E_{\mathrm{cross}}\ge
    \frac{m(3m-4)}{2(2m-1)(2m-3)}W_m
    >\frac38W_m.
   \]

   Thus no common-box product, and no construction adding only \(o(W_m)\)
   cross-box seam edges to its middle-line forests, can scale the bounded
   seed.  A successful use of the seed must be a genuinely
   context-dependent construction on growing packets, with a
   positive density of central diamonds leaving their original product
   boxes.
4. Whole even packet cycles also have an exact residue obstruction.  If a
   construction uses only cycles of a common length \(L\), then
   \(L\mid N_1\), where

   \[
    N_1=\binom{2m}{m-1},\qquad
    \nu_2(N_1)=s_2(m)+\nu_2(m)-\nu_2(m+1).
   \]

   In particular \(N_1\) is odd for \(m=2^t-1\).  Hence a library
   consisting only of the \(C_4\) seed, or only of even Hamming packet
   cycles, cannot be an all-\(m\) exact construction without an explicit
   odd boundary component.

These are product and packet-scaling obstructions, not a no-go for paired
SCDs themselves.  The surviving route is a growing, cross-box resolver.
Its exact central target is a doubly-rainbow Johnson 2-factor, and it must
also admit radius-compatible lower and upper half-chain covers.

## 1. Central diamonds and the exact gluing normal form

Write

\[
 \mathcal L=\binom{[2m]}{m-1},\qquad
 \mathcal M=\binom{[2m]}m,\qquad
 \mathcal U=\binom{[2m]}{m+1}.
\]

A Johnson edge \(e={X,Y}\) in \(\mathcal M\) has lower and
upper colours

\[
 L(e)=X\cap Y\in\mathcal L,\qquad
 U(e)=X\cup Y\in\mathcal U.
 \tag{1.1}
\]

Call a 2-factor \(\Gamma\) on \(A\subseteq\mathcal M\)
**doubly rainbow** if both colour maps

\[
 L:E(\Gamma)\to\mathcal L,\qquad
 U:E(\Gamma)\to\mathcal U
 \tag{1.2}
\]

are bijections.  Necessarily

\[
 |A|=|E(\Gamma)|=N_1:=\binom{2m}{m-1},\qquad
 |\mathcal M\setminus A|=\frac{W_m}{m+1}=\mathrm{Cat}_m.
 \tag{1.3}
\]

The following records the additional data needed to turn the central object
into two full SCDs.

### Proposition 1.1 (doubly-rainbow gluing criterion)

Fix a doubly-rainbow 2-factor \(\Gamma\) on \(A\), and orient each
of its cycles.  Suppose:

* the ranks \(0,\ldots,m-1\) are partitioned into saturated lower
  paths, one ending at each \(R\in\mathcal L\);
* the ranks \(m+1,\ldots,2m\) are partitioned into saturated upper
  paths, one starting at each \(U\in\mathcal U\);
* whenever an oriented edge \(e:X\to Y\) has colours
  \(R=L(e)\) and \(U=U(e)\), the lower path ending at \(R\)
  starts at rank \(m-q\) if and only if the upper path starting at
  \(U\) ends at rank \(m+q\).

Then concatenating

\[
 (\text{lower path to }R),\ X,
 (\text{upper path from }U)
 \tag{1.4}
\]

for the first SCD, and replacing \(X\) by \(Y\) for the second,
gives a paired SCD.  Add every member of \(\mathcal M\setminus A\)
as a common singleton chain.

Conversely, deleting the middle rank from a paired SCD produces exactly
these data.

#### Proof

Because \(R=X\cap Y\) and \(U=X\cup Y\), both
\(R\subset X\subset U\) and \(R\subset Y\subset U\) are
saturated two-step segments.  The radius condition makes each concatenated
chain symmetric.  Double rainbowness uses every lower and upper endpoint
once.  In the oriented 2-factor every member of \(A\) is the tail of
one edge and the head of one edge, so each SCD uses every member of
\(A\) once at the middle rank.  The common singleton chains complete
that rank.

For the converse, orient each diamond edge from the middle member used by
the first SCD to the opposite corner used by the second.  Every
\((m-1)\)-set and every \((m+1)\)-set occurs in one common
nontrivial chain, proving both rainbow bijections.  Deleting the middle
members leaves the asserted lower and upper paths, and symmetry gives the
radius equality. \(\square\)

Thus a doubly-rainbow 2-factor is necessary but not sufficient by itself:
the radius-compatible half-chain gluing is a separate exact condition.

## 2. The standard product of two SCDs

Let \(\mathscr C\) and \(\mathscr D\) be arbitrary SCDs of
Boolean lattices on disjoint coordinate sets of sizes \(2a\) and
\(2b\).  A child chain of radius \(r\) has \(2r+1\) members;
write it as

\[
 C=(c_0\subset c_1\subset\cdots\subset c_{2r}).
\]

Every pair \(C\in\mathscr C,D\in\mathscr D\) gives the
chain box

\[
 C\times D=\{c_i\cup d_j:0\le i\le2r,\ 0\le j\le2s\}.
 \tag{2.1}
\]

For \(r\le s\), the standard rectangular SCD consists of the
\(2r+1\) L-shaped chains indexed by \(k=0,\ldots,2r\):

\[
 (c_0,d_k),(c_1,d_k),\ldots,(c_{2r-k},d_k),
 (c_{2r-k},d_{k+1}),\ldots,(c_{2r-k},d_{2s}).
 \tag{2.2}
\]

Each begins at local rank \(k\) and ends at local rank
\(2r+2s-k\), so it is symmetric.  Reversing the roles of the two
axes gives the other standard orientation.

The number of radius-\(r\) child chains in any SCD of \(B_{2a}\)
is forced by the rank census:

\[
 c_{a,r}=\binom{2a}{a-r}-\binom{2a}{a-r-1}
 =\binom{2a}{a-r}\frac{2r+1}{a+r+1}.
 \tag{2.3}
\]

Here and below a binomial coefficient with a negative lower index is zero.

### Theorem 2.1 (equal-radius escape obstruction)

Let \(a,b\ge1\).  Form the standard product SCD by applying (2.2)
inside every child-chain box.  Its central alternate-corner map does not
map its positive-radius middle set into itself.  More precisely, it has at
least

\[
 E_{a,b}=\sum_{r=1}^{\min(a,b)}c_{a,r}c_{b,r}
 \tag{2.4}
\]

directed diamond edges whose head is a radius-zero middle singleton.
Consequently this product SCD cannot be one member of a paired SCD.

#### Proof

Take a child-chain box with equal positive radii \(r=s\).  Its middle
line is

\[
 Z_k=(c_{2r-k},d_k),\qquad 0\le k\le2r.
 \tag{2.5}
\]

In (2.2), \(Z_k\) is the middle member of the \(k\)-th product
chain.  For \(k<2r\), its central predecessor and successor are

\[
 (c_{2r-k-1},d_k)\subset Z_k\subset(c_{2r-k},d_{k+1}).
 \tag{2.6}
\]

The opposite corner is therefore

\[
 g(Z_k)=(c_{2r-k-1},d_{k+1})=Z_{k+1}.
 \tag{2.7}
\]

The last product chain, indexed by \(k=2r\), consists only of
\(Z_{2r}=(c_0,d_{2r})\), so \(Z_{2r}\) is a radius-zero global
singleton.  Equation (2.7) gives

\[
 g(Z_{2r-1})=Z_{2r}\notin\mathcal A.
 \tag{2.8}
\]

Using the opposite standard L orientation merely reverses the path and
makes the other endpoint the singleton; there is still one escape.

There are exactly \(c_{a,r}c_{b,r}\) boxes of common radius \(r\),
and boxes are disjoint.  Summing (2.8) proves (2.4).  Since closure of
\(g\) on \(\mathcal A\) is necessary for a paired SCD, the
last assertion follows. \(\square\)

This theorem permits arbitrary child SCDs.  Only the standard rectangular
composition is used.  Thus replacing BTK by the nonmonotone \(B_4\)
seed does not repair ordinary product recursion.

### Corollary 2.2 (exact \(B_4\)-outer defect)

Use the cyclic \(B_4\) SCD as one child and an arbitrary SCD of
\(B_{2m-4}\) as the other.  For \(m\ge3\), the standard product has
at least

\[
 E_{2,m-2}=3c_{m-2,1}+\mathbf1_{\{m\ge4\}}c_{m-2,2}
 \tag{2.9}
\]

escapes into global singleton centers.  As \(m\to\infty\),

\[
 E_{2,m-2}=\left(\frac78+o(1)\right)\frac{W_m}{m}.
 \tag{2.10}
\]

#### Proof

The \(B_4\) seed has three radius-one chains and one radius-two chain,
so (2.9) is (2.4).  For fixed \(r\), (2.3) and the elementary adjacent
central-binomial ratios give

\[
 c_{b,r}=\left(\frac{2r+1}{b}+O(b^{-2})\right)\binom{2b}b.
 \tag{2.11}
\]

Hence the right side of (2.9) is

\[
 \left(\frac{3\cdot3+5}{m}+O(m^{-2})\right)
 \binom{2m-4}{m-2}.
\]

Finally

\[
 \binom{2m-4}{m-2}=\left(\frac1{16}+O(m^{-1})\right)W_m,
\]

which gives (2.10). \(\square\)

The defect is of the same order as the entire singleton reservoir
\(\mathrm{Cat}_m\sim W_m/m\).  An outer resolver may still repair
it, but the repair is an additional theorem; it is not inherited from the
\(B_4\) seed.

## 3. The common-box and sparse-seam obstructions

The preceding obstruction used the standard L decomposition.  The next
one applies to every central construction that tries to remain inside the
same two-chain boxes.

For a box (2.1), its global middle members satisfy

\[
 i+j=r+s.
 \tag{3.1}
\]

They form a path under Johnson adjacency: consecutive vertices change
\(i,j\) to \(i+1,j-1\).  Call this the **middle line** of the box.

### Theorem 3.1 (common product-box no-go)

There do not exist paired SCDs of \(B_{2(a+b)}\), with
\(a,b\ge1\), such that both decompositions are subordinate to one
common partition into child-chain boxes \(C\times D\).

#### Proof

Take a common central diamond.  Its rank-\(m-1\) and
rank-\(m+1\) members lie in one box.  If both SCD chains remain in that
box, then both middle corners lie on its middle line.  Thus every internal
diamond edge is an edge of a path.

The paired-SCD condition says that these edges form a 2-factor on the
positive-radius middle members.  Each component of a 2-factor contains a
cycle, whereas a disjoint union of middle lines is a forest.  Since
\(N_1>0\), the 2-factor is nonempty, a contradiction. \(\square\)

Thus some central chains of the second SCD must jump between the chain
boxes of the first.  The required number of jumps is also exact.

### Theorem 3.2 (cross-box edge tax)

Fix arbitrary child SCDs of \(B_{2a}\) and \(B_{2b}\), and let a
**full** first global SCD, including all of its already assigned middle
members, be subordinate to their chain boxes: every whole chain of this
SCD is contained in one box.  Suppose its alternate-corner map is a
permutation of its positive-radius middle set.  Then its diamond 2-factor
has at least

\[
 B_{a,b}=W_aW_b-\mathrm{Cat}_a\mathrm{Cat}_b
 \tag{3.2}
\]

edges whose endpoints lie in different child-chain boxes.

#### Proof

Subordination of the first SCD does not assert that its opposite corners
stay in their boxes.  If the two central steps of one chain use the same
child axis, the opposite Boolean corner ordinarily lies in a different
child-chain box.  Those are precisely the cross-box edges counted below.

What subordination does fix is the first SCD's owner census in each box.

In a box whose child radii are \(r,s\), the middle line has
\(2\min(r,s)+1\) vertices.  The number of positive-radius global
chain centers in that box is

\[
 v_{r,s}=2\min(r,s)+1-\mathbf1_{\{r=s\}}.
 \tag{3.3}
\]

Indeed, the number of singleton global chains is the difference between
the middle-line size and the size of the adjacent rank.  This difference is
one when \(r=s\) and zero otherwise.  Therefore \(v_{r,s}>0\) unless
\(r=s=0\).

Fix a box containing \(v>0\) positive centers.  Internal diamond edges
form a simple subgraph of its middle-line path, so there are at most
\(v-1\) of them.  In the global diamond 2-factor the sum of degrees of
these \(v\) vertices is \(2v\).  Hence at least

\[
 2v-2(v-1)=2
\]

edge incidences leave the box.  Summing over nonempty boxes and dividing by
two shows that the number of cross-box edges is at least the number of
nonempty boxes.

There are \(W_a\) child chains in the first SCD and \(W_b\) in the
second.  Exactly \(\mathrm{Cat}_a\) and
\(\mathrm{Cat}_b\) of them have radius zero.  Thus precisely
\(W_aW_b-\mathrm{Cat}_a\mathrm{Cat}_b\) boxes are nonempty in the
sense above. \(\square\)

### Corollary 3.3 (positive-density tax for a fixed \(B_4\) factor)

For \(a=2\), \(b=m-2\), Theorem 3.2 gives

\[
\begin{aligned}
 E_{\mathrm{cross}}
 &\ge 6\binom{2m-4}{m-2}-2\mathrm{Cat}_{m-2} \\
 &=\frac{m(3m-4)}{2(2m-1)(2m-3)}W_m
  >\frac38W_m.
\end{aligned}
 \tag{3.4}
\]

#### Proof

Use \(W_2=6\), \(\mathrm{Cat}_2=2\), and
\(\mathrm{Cat}_{m-2}=W_{m-2}/(m-1)\).  Also

\[
 \frac{W_{m-2}}{W_m}
 =\frac{m(m-1)}{4(2m-1)(2m-3)}.
\]

Substitution gives the equality in (3.4).  Its excess over \(3/8\) has
positive numerator \(8m-9\). \(\square\)

This separates two phenomena.  The standard product has only
\(\Theta(W_m/m)\) forced escapes into singleton centers, but any
successful permutation-valued central map organized over the fixed
\(B_4\)-by-spectator chain boxes **as a full first SCD** must have
\(\Theta(W_m)\)
cross-box edges.  Repairing the former does not construct the latter.

Theorem 3.2 does not apply to a weaker datum consisting only of lower and
upper half-chain skeletons with their middle owners still unassigned.  In
that weaker problem the Catalan singleton leave may be relocated among
boxes, so the local values \(v_{r,s}\) are not yet forced.  Such a global
owner reassignment is one of the surviving outer-resolver routes.

### Corollary 3.4 (bounded packet-seam principle)

Let a candidate central 2-factor be partitioned into \(B\) nonempty
packets.  Suppose the graph of allowed internal diamond edges in every
packet is a forest.  Then at least \(B\) selected diamond edges cross
between packets.  If every packet has at most \(K\) positive owners,
then

\[
 E_{\mathrm{cross}}\ge B\ge\frac{N_1}{K}.
 \tag{3.5}
\]

#### Proof

The degree count in Theorem 3.2 applies verbatim to each forest packet.
The size bound gives \(BK\ge N_1\). \(\square\)

Therefore a fixed bounded seed plus only \(o(W_m)\) interpacket seams
cannot work.  The packet size must tend to infinity, or the internal
allowed graph must itself acquire cycles.  This is the precise point at
which first-eligible or other context-dependent growing packets become
necessary.

## 4. Exact packet residues and component control

The positive-radius owner count is fixed, not asymptotic:

\[
 N_1=\binom{2m}{m-1}=\frac{m}{m+1}W_m.
 \tag{4.1}
\]

### Proposition 4.1 (whole-cycle divisibility)

If a proposed paired-SCD central factor is a disjoint union of cycles all
having one common length \(L\), then \(L\mid N_1\).  More generally,
the greatest common divisor of all permitted component lengths must divide
\(N_1\).

For every \(m\ge1\),

\[
 \nu_2(N_1)=s_2(m)+\nu_2(m)-\nu_2(m+1),
 \tag{4.2}
\]

where \(s_2(m)\) is the number of ones in the binary expansion of
\(m\).  In particular, if \(m=2^t-1\), then \(N_1\) is odd.

#### Proof

The divisibility assertion follows by summing the component lengths.
The classical carry count for the central binomial coefficient gives

\[
 \nu_2\binom{2m}m=s_2(m).
\]

Using \(N_1=\binom{2m}m\,m/(m+1)\) yields (4.2).  For
\(m=2^t-1\), its right side is \(t-t=0\). \(\square\)

Thus whole \(C_4\) packets already fail at \(m=3,7,15,\ldots\).
Likewise a Hamming packet factor made only of \(C_{4r}\)'s requires

\[
 2+\nu_2(r)\le\nu_2(N_1).
 \tag{4.3}
\]

This is a boundary-residue obstruction, not an asymptotic density
obstruction: an explicitly constructed odd component could repair it.  It
does show that an all-\(m\) theorem cannot simply retain a union of whole
even packets and omit the rest.

There is also an independent component requirement.  If all central cycles
have length at most \(L\), then their number is at least

\[
 \frac{N_1}{L}.
 \tag{4.4}
\]

Consequently repeated \(C_4\) seeds have \(\Theta(W_m)\)
components.  A packet factor with cycles of length \(4r\) has
\(N_1/(4r)\) components apart from its boundary resolver; it reaches
\(o(W_m/H)\) only when \(r/H\to\infty\).  This explains why a
bounded seed must be fused into genuinely growing cycles even before any
higher-shadow condition is considered.

## 5. Audited implication boundary

The exact conclusions are:

* **Disproved:** ordinary standard product/ordinal SCD recursion, even when
  one child is the complement-symmetric cyclic \(B_4\) seed.
* **Disproved:** a pair of SCDs both subordinate to one common system of
  two-chain product boxes.
* **Disproved:** scaling a fixed bounded forest-like seed using only
  \(o(W_m)\) cross-context seams.
* **Necessary:** a positive-density cross-box central resolver for a fixed
  \(B_4\) outer factor when the first full SCD retains the product-box
  owner census; a growing packet size for sparse seam count; and an explicit
  boundary component to handle the all-\(m\) residue.
* **Still open:** a context-dependent growing resolver which simultaneously
  makes the central alternate map a permutation, makes both Johnson colour
  maps bijective, and supplies radius-compatible lower/upper half-chain
  covers, at any parameter not eliminated by an independent global parity
  obstruction.

The cross-box density bound deliberately does not cover a construction
which starts only from product half-chain skeletons and globally reassigns
the Catalan singleton set before forming either full SCD.

If that last object exists at a given parameter and has \(o(W_m/H)\)
cycles, Proposition 1.1 gives a paired SCD there with the needed component
control.  None of the product obstructions above rules out such a
non-product construction at the parity-admissible parameters.
