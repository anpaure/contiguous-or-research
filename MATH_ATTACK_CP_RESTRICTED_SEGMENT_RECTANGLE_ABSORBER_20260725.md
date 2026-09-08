# Restricted-segment rectangle absorbers over calibrated top packets

Date: 2026-07-25

Pure mathematics only.  This note audits the proposed repair of the fatal
full-packet \(0/2\) rectangle deployment.

## 0. Verdict

Let

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_H=\binom{2m}{m-H},\qquad M=m+H,
\]

where \(H\) is calibrated by

\[
 \frac{W}{N_H}\ge M
\]

at the first crossing.  Thus

\[
 H\sim\sqrt{m\log m},\qquad
 MN_H=W-o(W),\qquad HN_H=o(W).
\tag{0.1}
\]

The audit has one positive and one negative conclusion.

### Positive conclusion

The restricted-segment rectangle is exact.

Fix a cyclic order \(C\) on one top \(U\), and two disjoint adjacent
position swaps \(\tau,\sigma\), whose boundary separation is \(a\).
Let

\[
 C_{ij}=\tau^i\sigma^j C.
\]

There are two cyclic phase intervals \(P_0,P_1\subseteq\mathbb Z_M\) such
that

\[
 P_0\cup P_1=\mathbb Z_M,\qquad
 |P_0\cap P_1|=O(Q),
\tag{0.2}
\]

and, simultaneously for every controlled length

\[
 k\in[m-Q,m+Q],
\tag{0.3}
\]

the two segment configurations

\[
 \mathcal S_0=(C_{00}|P_0)\sqcup(C_{11}|P_1),
\qquad
 \mathcal S_1=(C_{10}|P_0)\sqcup(C_{01}|P_1)
\tag{0.4}
\]

have incidence difference equal to the full four-order selector

\[
 A_k(C_{00}+C_{11}-C_{10}-C_{01}).
\tag{0.5}
\]

Consequently (0.5) vanishes at every length except

\[
 k=a,\qquad k=M-a.
\tag{0.6}
\]

At length \(a\) it is one coefficient-one octahedron.  Therefore

* \(a=m-q\) isolates lower depth \(q\), with the forced companion length
  \(H+q\) outside the hard band;
* \(a=m+q\) isolates upper depth \(q\), with companion length \(H-q\);
* the middle and all other band ranks are preserved.

The usable upper range is \(q\le H-2\), because two disjoint adjacent
pairs require \(2\le a\le M-2\).  The final two upper ranks contain only
\(o(W)\) masks and may be patched literally.

If the original one-packet-per-top family is an owner near-transversal,
replacing a base packet by either configuration in (0.4) changes or adds
only \(O(Q)\) middle-owner occurrences.  Over all tops the total owner
damage is

\[
 O(QN_H)=O(WQ/m)=o(W)
\tag{0.7}
\]

whenever \(Q=o(m)\).  Two segment resets per top still cost \(o(W)\).

### Negative conclusion

This gadget is only a final absorber.

For a fixed pair of segment orders, (0.4) gives the two diagonals of one
rectangle.  After the switch, applying the same rectangle returns to the
first diagonal.  The two orders differ at exactly the same two adjacent
position pairs, so—without adding another strand or a nonlocal
re-pairing—there is no sequence of new rank selectors inside that
two-segment pair.

Thus one installed pair supplies one octahedral correction, of
\(\ell_1\)-size four.  One pair on every top has total correction capacity

\[
 O(N_H)=O(W/m)=o(W).
\tag{0.8}
\]

It cannot repair the \(\Theta(W)\) holes left by independent packet
selection, and it cannot in general repair an arbitrary \(o(W)\) residual
larger than \(O(W/m)\).

The correct programme is therefore:

1. prove an owner-only near-perfect packet matching;
2. obtain bulk vertical coverage by a correlated packet selection or a
   genuinely nonlocal multi-top/multi-strand trade;
3. use restricted-segment rectangles only for the final
   \(O(N_H)\)-scale, zero-margin residual.

Algebraically there is no parity obstruction: the signed rank-\(a\)
rectangle lattice is exactly the integral zero point-margin lattice.
Positivity and availability, not the lattice, are the remaining gates.

## 1. Phase notation for a promotion packet

Fix a top \(U\), \(|U|=M\), and an oriented cyclic order

\[
 C=(c_i:i\in\mathbb Z_M).
\]

For \(1\le k<M\), let

\[
 I_k(C;t)=\{c_t,c_{t+1},\ldots,c_{t+k-1}\}
\tag{1.1}
\]

be its cyclic length-\(k\) interval with interval start \(t\).

Index packet states by the start \(s\) of their middle \(m\)-interval.
The rank-\(k\) flag of that state is

\[
 I_k(C;s+m-k).
\tag{1.2}
\]

Indeed, for \(k=m-q\) the lower interval starts \(q\) positions after the
middle start, and for \(k=m+q\) the upper interval starts \(q\) positions
before it.  Thus the literal rank-\(k\) incidence of a promotion segment
with **state-phase set** \(P\) is

\[
 \widehat A_{k,P}(C)
 =\sum_{s\in P}e_{I_k(C;s+m-k)}.
\tag{1.3}
\]

When \(P\) is a cyclic interval of phases, the states at those phases form
a literal promotion path: they are a consecutive segment of the promotion
cycle of the calibrated top-packet construction.

### 1.1 Why the full-packet \(0/2\) version is fatal

Let \(C\) and \(\tau\sigma C\) be the two full packets on one diagonal of
a selector rectangle.  One adjacent swap changes at most two middle
windows, so two swaps give

\[
 |\mathcal O(C;\mathbb Z_M)
   \cap\mathcal O(\tau\sigma C;\mathbb Z_M)|
 \ge M-4.
\tag{1.4}
\]

Suppose packet multiplicities are strictly \(0\) or \(2\), with total
packet count \(N_H\).  There are \(N_H/2\) doubled tops.  The total number
of middle occurrences is \(MN_H\), while the internal coincidences in the
doubled pairs already force occurrence excess at least

\[
 (M-4)\frac{N_H}{2}.
\]

Therefore the number of distinct covered owners is at most

\[
 MN_H-(M-4)\frac{N_H}{2}
 =\frac{M+4}{2}N_H
 =\left(\frac12+o(1)\right)W.
\tag{1.5}
\]

More generally, allow multiplicities \(0,1,2\), still with total
\(N_H\), and suppose \(t\) tops carry a full diagonal pair.  Then exactly
\(t\) tops are omitted.  If \(n_X\) is the global occurrence multiplicity
of owner \(X\), the global occurrence excess is

\[
 \sum_X(n_X-1)_+.
\]

For each \(X\), the number of doubled-top pairs in which both packets own
\(X\) is at most \(\lfloor n_X/2\rfloor\le(n_X-1)_+\).  Summing (1.4)
over the \(t\) disjoint packet pairs gives

\[
 \boxed{
 \#\{\text{middle holes}\}
 \ge W-MN_H+t(M-4).}
\tag{1.6}
\]

Thus \(o(W)\) middle holes force \(t=o(N_H)\).  Omitting top masks is cheap,
but concentrating two *full* packets on a top amplifies the loss by the
packet length \(M\).  The restricted-segment construction below removes
this amplification by assigning complementary phase sets to the two close
orders.

## 2. Exact affected phases of one adjacent swap

Suppose \(\tau\) swaps the entries in adjacent positions \(b,b+1\) of
\(C\).

### Lemma 2.1 (two affected starts)

For a fixed proper length \(k\), the only phase starts at which the
underlying interval set changes under \(\tau\) are

\[
 \boxed{\mathcal B_k^{\rm int}(b)=\{b-k+1,\ b+1\}.}
\tag{2.1}
\]

#### Proof

A position interval changes as a set precisely when it contains exactly
one of the two swapped positions.  Since those positions are adjacent,
there are exactly two such cyclic intervals: the interval ending at \(b\),
whose start is \(b-k+1\), and the interval beginning at \(b+1\).
\(\square\)

By the literal phase shift (1.2), the corresponding **state phases** are

\[
 \boxed{
 \mathcal B_k^{\rm st}(b)
 =\{b-m+1,\ b-m+k+1\}.}
\tag{2.2}
\]

For the controlled band (0.3), put

\[
 \mathcal B_Q^{\rm st}(b)
 =\bigcup_{k=m-Q}^{m+Q}\mathcal B_k^{\rm st}(b).
\tag{2.3}
\]

Then

\[
 \mathcal B_Q^{\rm st}(b)
 =\{b-m+1\}\cup
   \{b-Q+1,\ldots,b+Q+1\},
\tag{2.4}
\]

so

\[
 |\mathcal B_Q^{\rm st}(b)|\le2Q+2.
\tag{2.5}
\]

The two pieces in (2.4) are the two **phase-boundary neighborhoods**.
They should not be confused with a neighborhood of the swapped labels in
the cyclic word.  One affected state phase is shifted by approximately
\(m\).

For \(Q=o(H)\), the two neighborhoods are disjoint and separated by arcs
of lengths \(H-O(Q)\) and \(m-O(Q)\).  Choose cyclic phase intervals
\(P_0,P_1\) which cover the phase circle and overlap in small
neighborhoods containing both pieces.  Then

\[
 P_0\cup P_1=\mathbb Z_M,\qquad
 \mathcal B_Q^{\rm st}(b)\subseteq P_0\cap P_1,\qquad
 |P_0\cap P_1|=O(Q).
\tag{2.6}
\]

Indeed, enlarge the two pieces of \(\mathcal B_Q^{\rm st}(b)\) to
disjoint cyclic intervals \(B_0,B_1\) of total size \(O(Q)\).  Their
complement has two cyclic gap intervals \(G_0,G_1\).  Taking

\[
 P_0=B_0\cup G_0\cup B_1,
 \qquad
 P_1=B_1\cup G_1\cup B_0
\tag{2.7}
\]

with the unions read in their cyclic order makes both \(P_i\) cyclic
intervals, gives \(P_0\cup P_1=\mathbb Z_M\), and gives
\(P_0\cap P_1=B_0\cup B_1\).

The same construction works whenever the displayed neighborhoods can be
covered by the two endpoint overlaps with total size \(O(Q)\).  The clean
uniform regime used below is \(Q=o(H)\).

## 3. The exact truncated rectangle identity

Let \(\tau\) and \(\sigma\) swap two disjoint adjacent position pairs of
\(C\).  They commute as coordinate transpositions.  Put

\[
 C_{ij}=\tau^i\sigma^jC,
\qquad
 z_C=C_{00}+C_{11}-C_{10}-C_{01}.
\tag{3.1}
\]

Use phase sets \(P_0,P_1\) satisfying

\[
 P_0\cup P_1=\mathbb Z_M.
\tag{3.2}
\]

Define the signed segment difference

\[
 \Delta_k
 =\widehat A_{k,P_0}(C_{00})+\widehat A_{k,P_1}(C_{11})
  -\widehat A_{k,P_0}(C_{10})-\widehat A_{k,P_1}(C_{01}).
\tag{3.3}
\]

### Theorem 3.1 (restricted segments recover the full selector)

If

\[
 \mathcal B_k^{\rm st}(b)\subseteq P_0\cap P_1,
\tag{3.4}
\]

where \(b,b+1\) are the positions swapped by \(\tau\), then

\[
 \boxed{\Delta_k=A_kz_C.}
\tag{3.5}
\]

Consequently, (2.6) gives (3.5) simultaneously for every controlled
length in (0.3).

#### Proof

At phase \(s\), put

\[
 \delta_s
 =e_{I_k(C_{00};s+m-k)}-e_{I_k(C_{10};s+m-k)},
\tag{3.6}
\]

\[
 \delta_s^\sigma
 =e_{I_k(C_{11};s+m-k)}-e_{I_k(C_{01};s+m-k)}.
\tag{3.7}
\]

Both differences vanish unless

\[
 s\in\mathcal B_k^{\rm st}(b),
\tag{3.8}
\]

because \(\sigma\) does not change the two positions on which \(\tau\)
acts.  Equation (3.3) is

\[
 \Delta_k
 =\sum_{s\in P_0}\delta_s
  +\sum_{s\in P_1}\delta_s^\sigma.
\tag{3.9}
\]

Under (3.4), every possibly nonzero term occurs in both phase sets.
Therefore

\[
 \Delta_k
 =\sum_{s\in\mathbb Z_M}
   (\delta_s+\delta_s^\sigma)
 =A_kz_C.
\]

This proves (3.5).  \(\square\)

Only the affected starts of the swap used to pass from one diagonal to the
other must lie in the overlap.  It is harmless, but unnecessary, to include
the affected starts of both \(\tau\) and \(\sigma\).

### Proposition 3.2 (the exact leakage counterterm)

Without (3.4), one has

\[
 \boxed{
 \Delta_k-A_kz_C
 =-\sum_{s\notin P_0}\delta_s
  -\sum_{s\notin P_1}\delta_s^\sigma.}
\tag{3.10}
\]

Only starts in \(\mathcal B_k^{\rm st}(b)\) can contribute.  Thus omission of one
affected start leaves one uncancelled single-swap incidence difference.

#### Proof

Subtract the full sums in the last line of the proof of Theorem 3.1 from
(3.9).  \(\square\)

Equation (3.10) is the precise counterterm to the informal assertion that
overlap merely near the label positions is sufficient.  The shifted start
\(b-k+1\) must also be protected.

## 4. Rank isolation

Rotate and relabel so that

\[
 C=(a,b,k_1,\ldots,k_{a-2},c,d,\ldots),
\tag{4.1}
\]

where

\[
 \tau=(a\ b),\qquad \sigma=(c\ d),
\]

and put

\[
 K=\{k_1,\ldots,k_{a-2}\}.
\]

The two swapped position boundaries have cyclic separations \(a\) and
\(M-a\).

### Theorem 4.1 (two-length selector)

For every \(1\le k<M\),

\[
 A_kz_C=0
 \qquad
 \text{unless }k\in\{a,M-a\}.
\tag{4.2}
\]

At length \(a\),

\[
 \boxed{
 A_az_C
 =e_{K\cup\{b,c\}}
  -e_{K\cup\{a,c\}}
  -e_{K\cup\{b,d\}}
  +e_{K\cup\{a,d\}}.}
\tag{4.3}
\]

At length \(M-a\), the image is the within-\(U\) complementary copy of
(4.3).

#### Proof

For a target coefficient to survive the alternating sum over
\(\tau,\sigma\), the target must contain exactly one element from
\(\{a,b\}\) and exactly one from \(\{c,d\}\).  If it is a cyclic interval,
its two boundary cuts must separate both adjacent pairs.  The two possible
arcs between those cuts have lengths \(a\) and \(M-a\), proving (4.2).

At length \(a\), the interval contains \(K\) and one endpoint from each
swapped pair.  The four choices and their alternating signs give (4.3).
Complementation of every interval inside \(U\) proves the final assertion.
\(\square\)

For \(1\le q\le Q\), take

\[
 a=m-q.
\tag{4.4}
\]

Then

\[
 M-a=H+q.
\tag{4.5}
\]

At calibrated depth, \(2H<m\) for all large \(m\), so (4.5) lies below the
hard band while (4.4) is lower depth \(q\).

For upper depth, take

\[
 a=m+q,\qquad M-a=H-q.
\tag{4.6}
\]

This is a valid nonzero selector for \(q\le H-2\).  Thus the middle length
\(m\) and every other hard-band length cancel exactly.

## 5. Exact owner-overlap audit

For a phase set \(P\), write

\[
 \mathcal O(C;P)=\{I_m(C;s):s\in P\}.
\tag{5.1}
\]

Within one order these owners are distinct.

Let

\[
 D=\tau\sigma C.
\]

Let \(b_\tau,b_\sigma\) be the first positions of the two swapped adjacent
pairs.  The length-\(m\) windows of \(C\) and \(D\) can differ only at

\[
 E=\mathcal B_m^{\rm st}(b_\tau)
   \cup\mathcal B_m^{\rm st}(b_\sigma),
\qquad |E|\le4.
\tag{5.2}
\]

### Proposition 5.1 (two segment supports are almost disjoint)

If \(P_0\cup P_1=\mathbb Z_M\) and \(B=P_0\cap P_1\), then

\[
 \boxed{
 |\mathcal O(C;P_0)\cap\mathcal O(D;P_1)|
 \le |B|+8.}
\tag{5.3}
\]

Consequently the \(M+|B|\) selected states in

\[
 (C|P_0)\sqcup(D|P_1)
\]

have at least \(M-8\) distinct middle owners, and their occurrence excess
over distinct owners is at most

\[
 |B|+8=O(Q).
\tag{5.4}
\]

#### Proof

Suppose

\[
 I_m(C;s)=I_m(D;t).
\tag{5.5}
\]

If \(s,t\notin E\), then

\[
 I_m(D;t)=I_m(C;t).
\]

Distinct cyclic starts of \(C\) give distinct length-\(m\) intervals, so
(5.5) forces \(s=t\).  A selected common owner of this type therefore has

\[
 s=t\in P_0\cap P_1=B.
\]

Every remaining common owner uses an exceptional phase on at least one
side.  Each side has at most \(|E|\le4\) exceptional owners, giving at most
eight further common owners.  This proves (5.3).  Inclusion-exclusion now
gives (5.4).  \(\square\)

There is a stronger comparison with the original full packet.

### Proposition 5.2 (small perturbation of a base packet)

Let \(\mu_m(\mathcal S_0)\) be the middle-owner occurrence histogram of the
first configuration in (0.4).  Then

\[
 \boxed{
 \|\mu_m(\mathcal S_0)-A_m(C)\|_1\le |B|+8.}
\tag{5.6}
\]

Moreover

\[
 \mu_m(\mathcal S_1)=\mu_m(\mathcal S_0).
\tag{5.7}
\]

#### Proof

On \(P_0\setminus P_1\), the first configuration uses the base order
\(C\).  On \(P_1\setminus P_0\), replacing \(C\) by \(D=\tau\sigma C\)
changes a middle owner only at the at most four exceptional starts in
(5.2), contributing at most eight to the \(\ell_1\)-difference.  Every
overlap phase contributes one additional occurrence, accounting for
\(|B|\).  This proves (5.6).

The controlled range includes \(k=m\), and \(a\ne m,M-a\).  Theorems
3.1 and 4.1 therefore give zero middle-incidence difference between the
two configurations, proving (5.7).  \(\square\)

Suppose a base family \(\{C_U\}\), one packet per top, has only \(o(W)\)
middle holes and occurrence excess.  Apply the segment construction at
every top with \(|B_U|=O(Q)\).  Propositions 5.1--5.2 show that either
diagonal configuration still has only

\[
 o(W)+O(QN_H)=o(W)
\tag{5.8}
\]

middle damage when \(Q=o(m)\).

The number of selected states is

\[
 \sum_U(M+|B_U|)
 =MN_H+O(QN_H)
 =W+o(W).
\tag{5.9}
\]

There are two promotion segments per top.  Even charging \(2H\) to
initialize each segment, the reset toll is

\[
 4HN_H=o(W).
\tag{5.10}
\]

Thus the segment repair is fully compatible with coefficient-one length
bookkeeping, conditional on the owner near-transversal.

## 6. The exact rank-\(a\) lattice and cone

Let \(V\) be a finite ground set of size \(v\), and let

\[
 \mathbb Z^{\binom Vr}
\]

be the integer vectors on its rank-\(r\) masks.  Define the point-margin
map

\[
 U_{V,r}f
 =\left(\sum_{S\ni x}f(S):x\in V\right).
\tag{6.1}
\]

For \(|K|=r-2\) and distinct \(a,b,c,d\notin K\), define the octahedron

\[
 \omega(K;a,b,c,d)
 =e_{Kbc}-e_{Kac}-e_{Kbd}+e_{Kad}.
\tag{6.2}
\]

### Theorem 6.1 (integral saturation)

For \(2\le r\le v-2\),

\[
 \boxed{
 \left\langle\omega(K;a,b,c,d)\right\rangle_{\mathbb Z}
 =\ker_{\mathbb Z}U_{V,r}.}
\tag{6.3}
\]

There is no further parity, congruence, or Smith-index invariant.

#### Proof

Every octahedron has zero point margins, so the left side lies in the
right.

Work over an arbitrary field.  If a function \(g\) on the \(r\)-sets
annihilates every octahedron, then for fixed distinct \(a,b\), the
difference

\[
 g(T+a)-g(T+b)
\tag{6.4}
\]

is independent of the \((r-1)\)-set \(T\) avoiding \(a,b\).  Indeed,
octahedral identities equate (6.4) along every edge of the connected
Johnson graph

\[
 J(V\setminus\{a,b\},r-1).
\]

Write the common difference as \(d_{a,b}\).  The cocycle identity

\[
 d_{a,b}+d_{b,c}=d_{a,c}
\]

gives scalars \(\alpha_x\) such that

\[
 d_{a,b}=\alpha_a-\alpha_b.
\]

Johnson connectivity then gives

\[
 g(S)=c+\sum_{x\in S}\alpha_x.
\tag{6.5}
\]

The parameters in (6.5) have one-dimensional kernel, so the annihilator
has dimension \(v\) over every field.  Hence the octahedra have rank
\(\binom vr-v\) over every field.

Over \(\mathbb Q\), the point-incidence matrix has row rank \(v\), so
\(\ker_{\mathbb Z}U_{V,r}\) also has rank \(\binom vr-v\).  This kernel is
primitive because its quotient is isomorphic to a subgroup of
\(\mathbb Z^v\).  If the octahedral lattice had nontrivial finite index in
it, reduction modulo a prime divisor of that index would lower the
octahedral rank, contradicting the field calculation.  This proves
(6.3).  \(\square\)

Every octahedron in (6.2) is the length-\(r\) image of a coefficient-one
segment rectangle: arrange the four displayed labels as the two adjacent
pairs, place \(K\) on the appropriate arc, and fill the remaining cyclic
positions arbitrarily.

For the global ground set \([2m]\), every octahedron support has size
\(r+2\).  When \(r\le M-2\), it fits inside some top \(U\) of size \(M\).
Therefore the global images of all top-local segment rectangles generate

\[
 \boxed{\ker_{\mathbb Z}U_{[2m],r}.}
\tag{6.6}
\]

The exact invariants are:

1. zero point margins at the isolated rank;
2. zero change in packet count at every top;
3. the forced within-top complementary image at length \(M-r\);
4. zero middle incidence whenever \(r,M-r\ne m\).

Because reversing the orientation of a rectangle changes the sign of its
octahedron, the nonnegative cone generated by all **oriented signed move
directions** is the full real subspace

\[
 \ker_{\mathbb R}U_{[2m],r}.
\tag{6.7}
\]

This statement is algebraic.  At a fixed nonnegative packet
configuration, only rectangles whose negative diagonal is actually
present are feasible.  That availability cone can be much smaller than
(6.7).

## 7. Positivity and the one-bit limitation

Each configuration in (0.4) is a nonnegative union of two literal promotion
segments.  Thus the local rectangle is positivity-feasible: one may choose
either diagonal without introducing a negative packet coefficient.

This does not make the whole lattice (6.6) positively reachable from one
owner near-transversal.

### Proposition 7.1 (one segment pair is one selector bit)

Assume the two swapped adjacent position pairs are disjoint and separated
from one another.  Within the four corner orders

\[
 C_{00},C_{10},C_{01},C_{11},
\]

the only two-packet diagonals are

\[
 \{C_{00},C_{11}\},
\qquad
 \{C_{10},C_{01}\}.
\tag{7.1}
\]

Switching (7.1) once reaches the other diagonal; switching the same
rectangle again returns.  It does not expose a selector at a new boundary
separation or a new rank.

#### Proof

Outside the four swapped positions, all four cyclic words agree.  The two
bits record the orientations of the two adjacent pairs.  Two opposite
corners differ at both pairs; the even and odd parity classes are exactly
the two diagonals in (7.1).  The rectangle switch toggles one bit in both
orders, exchanging those two classes.  The positions of disagreement, and
hence their boundary separation, do not change.  \(\square\)

For oriented packet paths there is no rotation/reversal ambiguity in this
statement.  Passing to unoriented interval incidence only identifies
duplicate columns and does not create another correction direction.

### Corollary 7.2 (capacity of one absorber per top)

Install at most one two-segment rectangle pair at each top.  Across all
tops, every choice of diagonals changes at most

\[
 4N_H=O(W/m)
\tag{7.2}
\]

rank-target incidence units relative to a fixed choice, summed in
\(\ell_1\) over the selected isolated cells.

In particular this family cannot correct a rank residual with
\(\ell_1\)-mass \(\omega(W/m)\).

#### Proof

One selector image is the four-entry octahedron (4.3), whose
\(\ell_1\)-norm is four.  There are at most \(N_H\) installed bits.
\(\square\)

If the tops are divided among \(2Q\) lower/upper ranks, (7.2) is the total
capacity across all of them, not the capacity at each rank.

This is the exact reason the gadget is a final absorber.  The signed lattice
is saturated only when arbitrarily many selector cells are available.
One owner-preserving bit per top supplies merely an
\(O(W/m)\)-sized zonotope inside that lattice.

## 8. What remains

The repaired route separates into three gates.

### Gate A: owner-only packet near-factor

Choose one base cyclic order \(C_U\) per top so that the \(M\) middle
interval packets cover \(W-o(W)\) distinct owners.  This remains the
top-tagged owner-packet matching problem.  Scalar Hall feasibility and the
symmetric fractional point do not round the cyclic bundles.

### Gate B: bulk vertical preparation

Starting from the owner near-factor, arrange that the aggregate vertical
residual to be repaired is at most \(O(N_H)\), with zero point margins
rank by rank.  Independent packet choices do not do this: they leave
\(\Theta(W)\) holes at every near-middle row of mean load about one.

This gate needs a correlated packet choice, a nonlocal multi-top trade, or
a richer restricted-segment construction with many genuinely independent
strands.  It cannot be replaced by repeated toggling of the same
two-segment pair.

### Gate C: final segment absorption

Given an \(O(N_H)\)-size zero-margin residual which decomposes into
available octahedra attached to distinct tops, choose the corresponding
diagonal bits.  Theorem 6.1 removes every abstract lattice and parity
obstruction, but a support-aware matching is still required to assign the
needed octahedra to the actually available top orders.

The local mechanism is therefore valid and useful.  It converts one
owner-near-transversal packet into two promotion paths with only \(O(Q)\)
extra owner occurrences, and gives an exact rank-isolated positive switch.
What it does not give is the owner near-factor, a supply of
\(\Theta(W)\) independent correction cells, or a theorem assigning the
available cells to a prescribed residual.

## 9. Audit ledger

### Proved

1. The exact two-start formula (2.1) for one adjacent swap.
2. Existence of complementary phase segments with \(O(Q)\) overlap in the
   clean regime \(Q=o(H)\).
3. Exact equality between truncated and full selector incidence under the
   affected-start containment condition.
4. The exact leakage counterterm (3.10) when containment fails.
5. Two-length support \(a,M-a\) and the coefficient-one octahedron.
6. Lower/upper rank isolation throughout the usable hard band.
7. \(O(Q)\) middle-owner occurrence damage per top.
8. \(W+o(W)\) state count and \(o(W)\) two-segment reset toll.
9. Integral generation of the entire zero point-margin lattice.
10. Absence of parity or finite-index obstructions.
11. Positivity of each individual segment rectangle.
12. The one-bit and \(O(N_H)\) total correction-capacity bounds.

### Still open

1. The owner-only near-perfect packet matching.
2. Bulk vertical preparation reducing every relevant residual to
   \(O(N_H)\) total.
3. A support-aware assignment of the final octahedra to available tops.
4. Any nonlocal multi-top or multi-strand absorber which supplies bulk
   correction while retaining \(W-o(W)\) distinct middle owners.
