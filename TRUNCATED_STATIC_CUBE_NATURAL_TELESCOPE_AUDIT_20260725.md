# The natural two-step connector telescope does not close

## 0. Verdict

Put (n=2Q).  Consider the bit ((i,j)) in the rectangular static cube.
In the route (A_j\to B_j), its source collar has the marked pair at
positions (r,r+1).  After the two literal cyclic steps from (B_j) to
(C_j), the same pair has the opposite orientation at positions
(r+2,r+3).  It is natural to hope that the source-flush traces of the
routes

\[
 A_j\longrightarrow B_j,
 \qquad
 C_j\longrightarrow A_{j+1}
\]

cancel above rank (r+2).

They cannot.  At every prefix length

\[
 r+3\le h\le 2Q-1
\]

their active-pair projections have disjoint supports, independently of all
buffer choices, even if the buffer rule itself changes with the bit.
Quantitatively,

\[
 \boxed{
 \sum_{h=r+3}^{2Q-1}
 \|D_h(A_j)+D_h(C_j)\|_2^2
 \ge 8(2Q-r-3).}
 \tag{0.1}
\]

The obstruction is an exact two-label boundary flux.  The ordinary flush
base for (A_j) contains the two labels which leave the back of the old
collar during the two cyclic steps.  The corresponding base for (C_j)
contains instead the two labels at the next column cut.  These four labels
are distinct.  The ordinary bases are independent of the chosen flush
buffers, so no buffer coupling repairs the mismatch.

There is a different, partial telescope after reindexing by phase.  The
source states (C_j) and (A_{j+1}) are at the same phase and lie on the
opposite sides of the same column exchange \(\beta_{j+1}\).  Their ordinary
and special flush bases can be coupled exactly whenever their collar orders
agree away from the row being updated.  But doing this simultaneously for
all row directions is impossible.  In the most favorable common-column
case, the uncancelled terms are one elementary two-row rectangle in each of
the two row-update directions for every pair of row swaps at every port.
These rectangles have disjoint supports
as the phase advances.  Thus the natural cross-port telescope leaves

\[
 \boxed{4(t-1)p(p-1)=\Theta(tQ^2)=\Theta(MQ)}
 \tag{0.2}
\]

total squared row-update trace per carrier, rather than (O(M)).

This does not rule out a genuinely different multi-template or
multi-carrier coboundary.  It does rule out the direct idea that the two
cyclic steps make the (A_j)-source connector cancel the (C_j)-source
connector, and it rules out the phase-reindexed version under the natural
common-column coupling.

## 1. Positional form of a cyclic quotient state

Let \(\rho=(\rho_k)_{k\in\mathbb Z_M}\) be a cyclic order.  At phase (s),
the radius-(Q) quotient state is

\[
 K_s=\{\rho_{s+Q},\ldots,\rho_{s+m-1}\},
 \tag{1.1}
\]

\[
 z_a=\rho_{s+Q-a},\qquad 1\le a\le 2Q,
 \tag{1.2}
\]

with the remaining labels in the tail.  The phase-(s) to phase-(s+1)
cyclic rotor move chooses

\[
 x=\rho_{s+Q},\qquad y=\rho_{s+m}.
 \tag{1.3}
\]

Equations (1.1)--(1.3) follow directly from the rotor recurrence and also
verify it.

At port (j), put (s=2j).  The (i)-th row pair occupies the fixed
positional cut (a_i,a_i+1), and

\[
 q=a_i-s+1,
 \qquad
 r=Q-q=Q-a_i+s-1.
 \tag{1.4}
\]

Thus its two labels occur at collar positions (r,r+1), in reverse
positional order.

Write the column-(j) cut labels as

\[
 a=\rho_{s+m-1},\qquad b=\rho_{s+m},
 \tag{1.5}
\]

and the next column-cut labels as

\[
 a'=\rho_{s+m+1},\qquad b'=\rho_{s+m+2}.
 \tag{1.6}
\]

The route (A_j\to B_j) exchanges (a) out of the core and (b) into
the core.

Let (g=\prod_k\alpha_k) be the product of all row transpositions.  The
frame of (B_j) is (g\beta\rho).  Its next two cyclic moves choose

\[
 x_1=\rho_{s+Q},\quad y_1=a,
 \qquad
 x_2=\rho_{s+Q+1},\quad y_2=b'.
 \tag{1.7}
\]

Indeed \(\beta_j\) sends the label at position (s+m-1) to position
(s+m), while \(\beta_{j+1}\) sends the label at position (s+m+2) to
position (s+m+1).  Hence the core of (C_j) is

\[
 K(C_j)=K_s-\{\rho_{s+Q},\rho_{s+Q+1}\}+\{b,b'\},
 \tag{1.8}
\]

and the route (C_j\to A_{j+1}) uses tail input (a').  Its collar is

\[
 (\rho_{s+Q+1},\rho_{s+Q},gz_1,\ldots,gz_{n-2}).
 \tag{1.9}
\]

All labels in (1.5)--(1.7), together with (z_{n-1},z_n), are distinct in
the calibrated regime (Q<H-1).

## 2. Ordinary flush bases cannot match after two steps

For a generic source state ((P;w_1,\ldots,w_n;R)), a source
transposition at collar boundary (r), and tail input (b_0), the ordinary
flush term at prefix (h=r+d), (d\ge1), has transposition base

\[
 \mathcal K_h(P,w,b_0;r)
 =P+\{b_0\}+\{w_1,\ldots,w_{r-1}\}
  +\{w_{n-d+2},\ldots,w_n\}.
 \tag{2.1}
\]

This is the base called (K_h) in the one-route connector audit.  Crucially,
it contains no flush-buffer labels in a distinguished way: all buffer
deletions have cancelled against the buffer prefix.

For (A_j\to B_j), equation (2.1) gives, for (d=h-r\ge3),

\[
 \mathcal K^A_h
 =K_s+\{b\}+Z_{<r}+Z_{n-d+2:n}.
 \tag{2.2}
\]

For (C_j\to A_{j+1}), the boundary is (r+2), so its flush index is
(d-2).  Equations (1.8)--(1.9) give

\[
 \mathcal K^C_h
 =K_s+\{b,b',a'\}+gZ_{<r}+gZ_{n-d+2:n-2}.
 \tag{2.3}
\]

In particular,

\[
 z_n=\rho_{s-Q}\in\mathcal K^A_h,
 \qquad
 z_n\notin\mathcal K^C_h.
 \tag{2.4}
\]

The second assertion holds because the old collar contribution in (2.3)
stops at (z_{n-2}), while (z_n) is neither in (K_s) nor one of
(b,b',a').  Therefore

\[
 \boxed{\mathcal K^A_h\ne\mathcal K^C_h}
 \qquad(r+3\le h\le n-1).
 \tag{2.5}
\]

No buffer choice appears in this proof.

## 3. Why a special-state cross-match cannot rescue it

For a base (B) containing neither row label (u,v), write

\[
 T_B=e_{B+u}-e_{B+v}.
 \tag{3.1}
\]

The vectors (T_B) for distinct bases are orthogonal and have squared norm
two.

If (A_j) has the unswapped orientation and (C_j) the swapped
orientation, the sum of their source-flush differences at a fixed
(r+3\le h\le n-1) is, up to an overall sign,

\[
 -T_{\mathcal K^A_h}+T_{\mathcal J^A_h}
 +T_{\mathcal K^C_h}-T_{\mathcal J^C_h}.
 \tag{3.2}
\]

For each individual route and every (h<n),

\[
 \mathcal K^A_h\ne\mathcal J^A_h,
 \qquad
 \mathcal K^C_h\ne\mathcal J^C_h.
 \tag{3.3}
\]

This is the exact (z_{r+2})-separator from the one-route audit, applied at
boundaries (r) and (r+2).

If (3.2) were zero, orthogonality would force equality of the positive and
negative base multisets.  In view of (3.3), the only possible matching is

\[
 \mathcal J^A_h=\mathcal J^C_h,
 \qquad
 \mathcal K^A_h=\mathcal K^C_h.
 \tag{3.4}
\]

Equation (2.5) excludes (3.4).  This already gives squared norm at least
four per rank under a common buffer coupling.

There is a stronger buffer-independent projection.  At a fixed high
prefix, project onto masks containing exactly one of the active row labels
(u,v).  During the entire flush/reload skeleton, only the ordinary boundary
state and the one core--tail split state contribute to this projection.  If
the two bit values use unrelated legal buffer lists, their one-route
difference is

\[
 -e_{\mathcal K+u}+e_{\mathcal K+v}
 +e_{\mathcal J_1+u}-e_{\mathcal J_0+v}
 \tag{3.5}
\]

up to an overall sign.  Both (\mathcal J_0) and (\mathcal J_1) differ from
(\mathcal K) by the same fixed collar separator used in (3.3), and a
mask containing (u) but not (v) cannot equal one containing (v) but
not (u).  Thus the four masks in (3.5) are distinct and the one-route
squared norm is exactly four.

For the (A_j)-source route, all four masks contain the two old trailing
collar labels (\rho_{s-Q},\rho_{s-Q+1}) and omit the next-column labels
(a',b').  For the (C_j)-source route the opposite invariant holds.  The
two four-mask supports are therefore disjoint, giving squared norm eight
per rank and proving (0.1).

Target-reload traces are confined to (h\le r) for the first route and
(h\le r+2) for the second.  The two cyclic intermediate states differ
only at the moving adjacent boundary (r+1).  Hence none of those terms
affects (0.1).

## 4. The phase-reindexed partial telescope

There is a more favorable pairing.  At phase (s=2j), compare the two
routes on opposite sides of the *same* column exchange:

\[
 C_{j-1}\longrightarrow A_j,
 \qquad
 A_j\longrightarrow B_j.
 \tag{4.1}
\]

Abstractly, their source states are

\[
 (K-a+b;\widetilde z;R-b+a),
 \qquad
 (K;z;R),
 \tag{4.2}
\]

and their respective tail inputs are (a) and (b).  Choose the same
flush buffers from (K-\{a\}) for both routes.  Then the unordered part of
every ordinary base agrees because

\[
 (K-a+b)+a=K+b,
 \tag{4.3}
\]

and the unordered part of every special base agrees for the same reason,
even after deleting the common buffer prefix.

Let (x^{j-1},x^j\in\{0,1\}^p) be the adjacent column signatures and put

\[
 D_j=\{i:x^j_i=x^{j-1}_i\}.
 \tag{4.4}
\]

The collar signature of (C_{j-1}) is (1-x^{j-1}), whereas that of
(A_j) is (x^j).  Hence for a row (i\in D_j) the two source traces have
opposite orientation, which is the sign required for cancellation.  For
(i\notin D_j) they have the same orientation and add rather than cancel.

The row cuts are (a_k=a_0+2k).  For fixed (i), the ordinary bases agree at
every rank except when
the moving suffix cuts one earlier row pair (k<i).  That happens exactly
at

\[
 h_{ik}=2Q+1+2(k-i).
 \tag{4.5}
\]

The special base has a symmetric phenomenon.  Its fixed suffix contains
every earlier row pair completely.  After all common buffers have
re-entered, however, its moving prefix can cut one later row pair (k>i).
This happens exactly at

\[
 h_{ik}=2Q+1+2(i-k).
 \tag{4.6}
\]

Therefore, for (i\in D_j), the full high-rank residual of (4.1) is exactly
one elementary ((\alpha_i,\alpha_k))-rectangle for every

\[
 k\ne i,\qquad k\in D_j.
 \tag{4.7}
\]

Each such rectangle has squared norm four.  The two possible row pairs at
the same distance from (i) occur in the same rank but have distinct
four-mask supports.  In positional coordinates, after removing both row
pairs, their bases are respectively

\[
 \{\rho_\ell:s-Q\le\ell\le a_k-1\}
 \cup\{\rho_\ell:a_i+2\le\ell\le s+m\},\qquad k<i,
 \tag{4.8a}
\]

and

\[
 \{\rho_\ell:s-Q\le\ell\le a_i-1\}
 \cup\{\rho_\ell:a_k+2\le\ell\le s+m\},\qquad k>i.
 \tag{4.8b}
\]

For equidistant (k)'s, the first rectangle contains both labels of the
later pair while the second contains only its selected label, so their
supports cannot meet.  Summing over (i\in D_j) gives the exact contribution

\[
 \boxed{4|D_j|(|D_j|-1)}
 \tag{4.8}
\]

from the opposite-orientation rows.

For (i\notin D_j), all nonexceptional ranks have equal ordinary and
special bases but equal signs, so the two route traces double.  There are
(\Omega(Q)) such ranks.  More precisely, a changed row has at least

\[
 (n-r_i-1)-(p-1)\ge p
\]

nonexceptional high ranks, using (r_i\le Q-2t-3) and
(2p\le Q-4t).  At each of them the doubled source trace has squared norm
sixteen.  If (d=|D_j|), the local aggregate over all row directions is
therefore at least

\[
 4d(d-1)+16p(p-d)\ge4p(p-1).
 \tag{4.9}
\]

Thus making (D_j) small does not help: it replaces the rectangles in
(4.8) by (\Omega(Q)) same-sign cost for every row outside (D_j).  The
local lower bound is minimized at (d=p).

## 5. No telescope across ports in the favorable common-column case

Take the most favorable choice

\[
 x^0=x^1=\cdots=x^{t-1}.
 \tag{5.1}
\]

Then (D_j=[p]) at every internal phase, so every row has the correct
opposite sign.  The matched parts of the special and ordinary bases cancel.
Equation (4.8) leaves exactly

\[
 4p(p-1)
 \tag{5.2}
\]

squared trace per internal port.

These residual rectangles cannot cancel between different ports.  To see
this, fix an unordered pair (i<k).  The special-base residual in row
direction (i) and the ordinary-base residual in row direction (k) are the
same elementary four-mask rectangle (they are counted separately in the
covariance trace).  Its underlying base after removing both row-pair labels
is, at phase (s=2j),

\[
 \mathcal B_{s,i,k}
 =\{\rho_ell:s-Q\le\ell\le a_i-1\}
  \cup
  \{\rho_ell:a_k+2\le\ell\le s+m\}.
 \tag{5.3}
\]

When the phase advances from (s) to (s+2), this set loses the two
left-boundary labels

\[
 \rho_{s-Q},\rho_{s-Q+1}
\]

and gains the two right-boundary labels

\[
 \rho_{s+m+1},\rho_{s+m+2}.
\]

None of these is a row-pair label.  Thus no mask in the four-point
((i,k))-rectangle at phase (s) equals a mask in the corresponding
rectangle at another phase.  The supports are disjoint.  Summing (5.2)
over (t-1) internal phases proves (0.2).

The initial (A_0\to B_0) source trace is unpaired and only increases the
cost.

## 6. Remaining logical possibility

The calculation above treats the two canonical pairings:

1. same bit before and after its two cyclic steps; and
2. opposite sides of the same column exchange after reindexing by phase.

The first has the buffer-independent boundary-flux obstruction (0.1).  The
second cancels only at the price of the pairwise row rectangles (4.7),
whose supports do not telescope in the favorable common-column case.

A successor would therefore need a genuinely noncanonical construction:
different route templates whose ordinary boundary fluxes cross-match, or
a multi-carrier signed design which cancels the pairwise row rectangles
without cancelling the marked rank-isolating rectangles.  No such identity
is present in the flush-and-reload compiler.

## 7. Successor outside the flush-and-reload phase family

There is now an exact noncanonical four-template identity, recorded in
MATH_ATTACK_FOUR_TEMPLATE_ROTOR_COBBOUNDARY_20260725.md.  It does not try
to match phase-shifted flush bases.

Instead, one two-step arrival diamond gives a vertical flag string indexed
by a saturated base chain.  Subtracting the strings for two chains that
differ by one adjacent increment cancels every rank except one and leaves
an elementary rectangle there.  Two carrier tags turn the signed
four-column identity into a positive switch with one path per carrier and
no added word length.

Thus Sections 1--6 remain a no-go for the natural rectangular-cube
telescope, but they are not a no-go for all rotor coboundaries.  The new
open gate is packing \(\Theta(M)\) synchronized paired diamonds per carrier
pair while preserving a global near-cover.
