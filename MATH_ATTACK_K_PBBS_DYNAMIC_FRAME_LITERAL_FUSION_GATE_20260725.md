# Lane K: the corrected dynamic-frame literal fusion gate

Date: 2026-07-25

Pure mathematics only. No computation, finite search, solver, or external
input is used.

## 0. Verdict

Put

\[
 N=2r+1,\qquad B=\operatorname {Cat}_r,\qquad W=NB,
 \qquad H\le A\sqrt r
\]

for fixed \(A\).  The proposed fusion of all primitive or all
terminal-maximum roots cannot be constructed from the sector iteration in
`PBBS_ZERO_WINDING_CONVERSE_AND_RPA_COUNTEREXAMPLE_20260725.md`.
That iteration is false.  The exact block rotation

\[
 D=P1R0S\quad\Longmapsto\quad \tau D=S1P0R                 \tag{0.1}
\]

may change the canonical first-deepest spine after one round.  In
particular, terminality \(S=\varnothing\) is not an invariant frame and
does not identify two equal physical ports.

There are two rigorous conclusions.

1.  The largest class on which the advertised static \(h\)-round sector
    itinerary is actually canonical is stretched-exponentially sparse.
    Even the old \(O(H^2)\) literal repair at every spatial lift of every
    root in that class has total cost \(o_A(W)\).  No shared fusion is
    needed there.

2.  Outside that protected class, the existing PBBS, row-coherent, and
    MTF theorems do not furnish a legal fusion.  A true short return has a
    dynamically changing sequence

    \[
       D_j=P_j1R_j0S_j,\qquad D_{j+1}=S_j1P_j0R_j,          \tag{0.2}
    \]

    and any literal chart must use the whole sequence.  One sufficient
    conditional fallback is a **deck-shared dynamic-frame braid**: it must
    retain the existing \(N\)-fold baseline owner mass, add only \(O_A(H)\)
    letters for an entire quotient block (or return carrier), and preserve
    all selected correct lower and upper PBBS masks crossing the braid.
    No theorem presently quoted in this lane supplies that chart.

There is also a sharp worst-case volume correction.  On a dyadic residence
band \(\ell\in[H/2,H]\), edge volume alone guarantees \(o(W)\) for an
independent physical-cut chart when its per-interval cost is \(o(H)\), not
merely \(o(H^2)\).  This is not a lower bound on the number of actual PBBS
intervals.  An \(O(H)\) chart is volume-sufficient if its cost is paid once
per quotient trace while all \(N\) spatial lifts are fused together.

Thus this report neither proves nor uses the assertion that \(RP_A\) is
false.  It identifies the exact literal theorem which would bypass
residence packing after the erroneous static-sector premise is removed.

## 1. The exact protected static-sector class

Write the first-deepest-spine decomposition of a height-\(h\) Dyck root as

\[
 D=A_0\,1A_1\,1\cdots1A_{h-1}\,1\,0B_{h-1}0\cdots0B_1\,0B_0. \tag{1.1}
\]

If the displayed spine remains canonical, one formal application of
(0.1) sends the sectors to

\[
 A'_0=B_0,\quad A'_i=A_{i-1}\ (i\ge1),\qquad
 B'_i=B_{i+1},\quad B'_{h-1}=\varnothing.            \tag{1.2}
\]

The exact protection theorem proved in
`MATH_ATTACK_K_CORRECTED_TERMINAL_SECTOR_FUSION_OBSTRUCTION_20260725.md`
is

\[
 \boxed{
 \text{(1.2) is canonical through rounds }0,\ldots,h
 \iff
 A_k=\varnothing\ \forall k,
 \quad \operatorname {ht}(B_k)\le k\ \forall k.}   \tag{1.3}
\]

The necessity is literal.  A nonempty \(A_k\), after
\(h-1-k\) formal shifts, lies in the \(A_{h-1}\)-sector and reaches
height \(h\) before the displayed spine.  If
\(\operatorname {ht}(B_k)\ge k+1\), then at round \(h\) it lies at
depth \(h-1-k\) and again reaches height \(h\) first.  Conversely, under
(1.3), every transported \(B_k\) which precedes the spine has total height
at most \(j-1<h\) at round \(j\), so the itinerary stays canonical.

On this class the standard computation is legitimate and gives

\[
 d(D_j)=2|B_j|+1\quad(0\le j<h),\qquad
 \delta(D_j)=h+2\sum_{t<j}|B_t|\quad(0\le j\le h). \tag{1.4}
\]

and hence

\[
 \delta(D_j)-\sum_{t<j}d(D_t)=h-j.                 \tag{1.5}
\]

Thus there is a first zero-winding return of gap \(2h+1\).

Let \(\mathcal S_r\) be the union of the protected class over all heights.
The same report proves, for an absolute \(c>0\),

\[
 |\mathcal S_r|\le r4^r e^{-c r^{1/3}}
 =o\!\left(\operatorname {Cat}_r/r^K\right)        \tag{1.6}
\]

for every fixed \(K\).  Indeed, (1.3) forces an initial run of \(h\)
up-steps, giving \(4^r2^{-h}\), while height at most \(h\) gives

\[
 4^r\exp\!\left(-\frac{\pi^2r}{(h+2)^2}\right).
\]

Splitting at \(h=r^{1/3}/2\) and summing over \(h\) proves (1.6).
Consequently

\[
 N(H^2+2H)|\mathcal S_r|=o_A(NB)=o_A(W).           \tag{1.7}
\]

The charge in (1.7) is a literal *incremental* charge inside any complete
cut-repair construction.  Add one cut for each protected lifted interval
to whatever scheme handles the remaining short returns, append every
selected correct lower or upper target whose intended depth-\(q\le H\)
witness that cut destroys, and pay the usual endpoint collar.  There are at
most \(H(H+1)\) signed crossing masks and at most \(2H\) collar letters per
lift; every appended target is an actual nonempty Boolean set.  Repetitions
only lower the required number, so (1.7) is a valid integral upper bound on
the protected family's contribution.

This does not by itself produce a valid global erosion word: unprotected
short runs may remain and must still be cut, fused, or otherwise serviced.
It proves that the protected static-sector family can be removed from the
cost obstruction at \(o(W)\), conditional only on completing the treatment
of the remaining returns.

## 2. Exact physical failure of terminality as a port condition

The primitive terminal root

\[
 D_0=1110011000,\qquad N=11,                       \tag{2.1}
\]

has the exact orbit

\[
\begin{array}{c|c|c}
D_j&\delta(D_j)&d(D_j)\\ \hline
1110011000&3&1\\
1110001100&3&5\\
1100111000&7&1
\end{array}
\qquad D_3=D_0.                                    \tag{2.2}
\]

After three even-time moves the spatial root is \(u-7\), and the next odd
move adds \(3\).  The alleged height-three endpoint label is therefore

\[
 u-7+3=u-4\not\equiv u\pmod {11}.                  \tag{2.3}
\]

Thus a chart which glues the two static-sector endpoints identifies two
different physical coordinates.  It is not a PBBS return repair and cannot
preserve the claimed lower or upper flag.  This is a factor-consistency
failure, not an asymptotic loss.

The first actual return in this example has gap \(13\).  Hence even the
primitive/terminal predicate neither determines the return time nor
provides the labelled ports needed by a literal MTF connector.

## 3. What a genuine zero-winding return does provide

Suppose now that a true zero-winding return has \(s\) even-time steps and
write its exact frames as in (0.2).  Put

\[
 d_j=|S_j|+1,\qquad \delta_j=|P_j|+1,\qquad
 L_j=\sum_{t<j}d_t.                                \tag{3.1}
\]

The zero-winding equation is \(L_s=\delta_s\).  The audited dynamic
staircase theorem in
`MATH_ATTACK_O_RP_A_ZERO_WINDING_PREFIX_CODE_20260725.md` gives

\[
 \delta_j-L_j\ge s-j>0\quad(j<s),                 \tag{3.2}
\]

and the literal identity

\[
 \boxed{
 P_s1=(S_{s-1}1)(S_{s-2}1)\cdots(S_01),
 \qquad \operatorname {ht}(S_j)\le j.}             \tag{3.3}
\]

There is also a dual sequence of Dyck words \(T_j\) with

\[
 S_j1P_j=P_{j+1}1\overline {T_j}.                  \tag{3.4}
\]

Equations (3.3)--(3.4) are the correct replacements for the false static
sector rotation.  They certify the return and retain every frame change.
They do **not** themselves give a literal contiguous-OR word: their bits
are coordinate-incidence bits inside PBBS middle states, not successive
set-letters of an OR word.  Turning (3.4) into a word braid requires a
separate ordered-state realization theorem.

## 4. Exact MTF cost inside the established priority-cylinder class

This section records why the existing MTF theorem does not silently supply
the required realization.

Here \(m:=r+1\) denotes the rank of a complement-projected PBBS owner, not
the semilength parameter from Sections 0--3.  The priority-prefix proof is
an ordered-partition argument and extends verbatim from the even
\(J(2m,m)\) notation of its source to the \(N=2r+1\) ground set: the owner
side has \(r+1\) coordinates, the complementary side has \(r\), and both
have at least \(H\) available coordinates in the present range.  Only the
chronological lower prefix is used below; any upper queue is endogenous.

A marked rank-\(m\) owner with a depth-\(H\) singleton queue has state

\[
 \Pi=(B,\{x_{H-1}\},\ldots,\{x_0\},\mathcal R),
 \qquad |B|=m-H.                                   \tag{4.1}
\]

Its lower deletion queue is \((x_0,\ldots,x_{H-1})\).  Suppose the next
owner is

\[
 Y=X-\{x_0\}+\{a\}.                               \tag{4.2}
\]

If the next queue is

\[
 (x_1,\ldots,x_j,a,x_{j+1},\ldots,x_{H-1}),        \tag{4.3}
\]

then the audited priority transition writes

\[
 \{a\},\{x_{j+1}\},\ldots,\{x_{H-1}\},B          \tag{4.4}
\]

and has \(H-j\) extra letters beyond the one new owner position.

Moreover this cost is exact only for the prescribed chronological lower
prefix in the one-update, core-leading singleton normal form.  It is not a
distance lower bound to an arbitrary saturated MTF state over the same
target owner: a different base/tail decomposition can be reached in one
letter.  Subject to the prescribed target prefix, a one-letter update from
(4.1) to a different marked owner
can only be a nonqueued transition

\[
 Q(Y)=(x_1,\ldots,x_{H-1},b),\qquad b\in B.         \tag{4.5}
\]

Indeed, after one MTF update the old base can leave at most one residual
singleton before the surviving old queue blocks.  If no residual block is
left, the middle owner is unchanged; if one is left while a genuinely new
singleton is inserted, it must be the \(b\) in (4.5).  An arrival inserted
strictly inside the new queue therefore needs the intervening positions in
(4.4).

This is precisely the scope of the sharp priority-prefix portal theorem in
`MATH_ATTACK_AE_HYBRID_PRIORITY_ROTOR_FUSION_20260725.md`.  It does not
exclude an interlaced braid whose marked endpoint uses a different refined
prefix and later recovers the desired masks by other intervals.

For a PBBS positive run of residence \(s+1\), the arriving coordinate
departs again after \(s\) later transition slots.  In the canonical
next-departure queue its priority position is at most \(s\): at most one
coordinate which was contemporaneous with the arrival can make its first
departure in each intervening slot.  Later arrivals are not counted in
this priority statistic.  Thus independent priority repair costs at least

\[
 (H-s)_+.                                          \tag{4.6}
\]

Summed over omitted-label gap multiplicities \(M_s\), a universal lower
bound on the independent chronological priority excess is the PBBS
rank-excess energy

\[
 E_H=\sum_s(H-s)_+M_s.                             \tag{4.7}
\]

This is an architecture statement.  A genuinely interlaced braid may use
the intermediate positions in (4.4) as distinct owners from other strands;
that is precisely the fusion still missing.  Merely invoking the priority
connector independently repeats the same middle owner in those positions
and pays at least (4.7).

The row-coherent theorem does not change this conclusion.  It proves that
one paired cut hits the synchronized positive and zero defects on the two
PBBS parity rows.  It then independently recanonicalizes the resulting
endpoints.  It supplies neither a cross-fragment owner ordering nor a
conversion of the repeated portal positions in (4.4) into fresh middle
owners.

## 5. The worst-case residence-band cost scale

Consider edge-disjoint physical residence intervals whose residence
lengths lie in

\[
 H/2\le\ell\le H.                                  \tag{5.1}
\]

Each uses at least \(H/2\) projected transition edges.  Since the full
projected PBBS factor has \(W\) edges, their number is at most

\[
 {2W\over H}.                                      \tag{5.2}
\]

This order is compatible with the alleged Gaussian obstruction and cannot
be improved from edge volume alone.  If an independent physical chart
costs \(\beta_H\) new letters per selected interval, its worst-case bill is

\[
 O\!\left({\beta_HW\over H}\right).               \tag{5.3}
\]

Therefore the scale which guarantees little-oh is

\[
 \boxed{\beta_H=o(H).}                             \tag{5.4}
\]

The condition \(\beta_H=o(H^2)\) is insufficient.  Even
\(\beta_H=H\) yields only an \(O(W)\) bound on this band.

This is a worst-case volume normalization, not an unconditional necessity
theorem for the actual PBBS.  It becomes necessary for a mechanism which
must service \(\Theta(W/H)\) intervals separately.  Since \(RP_A\) remains
open, no such lower bound on the number of top-band physical intervals is
assumed here.  The proved statement is that \(\beta_H=o(H)\) uniformly
guarantees \(o(W)\) from edge volume alone, whereas \(o(H^2)\) does not.

There is a different, viable accounting if all \(N\) spatial lifts of one
quotient trace are braided together.  The quotient has \(B\) directed
edges.  A quotient-edge-disjoint family satisfying (5.1) has at most
\(2B/H\) traces.  A chart with connector overhead \(O_A(H)\) **per whole
deck bundle**, independent of \(N\), then costs only

\[
 O_A(H)\,{2B\over H}=O_A(B)=o(W).                  \tag{5.5}
\]

This is the precise attraction of a deck-shared braid.  Its \(N\) lifted
owners are part of the existing baseline \(W\) positions; they may be
reordered, but they cannot be re-emitted as \(N\) new connector letters.

## 6. A sufficient conditional dynamic-frame deck-braid fallback

Here is a conditional theorem which would compose literally with the
audited all-depth PBBS support result.  It is one fallback, not the unique
remaining theorem.  The block form deliberately includes all intersecting
returns; a chart only for a selected edge-disjoint packing would not by
itself repair the unselected crossing intervals.

> **Dynamic-frame PBBS deck braid, \(\mathrm{DFB}(H)\).**  Partition every
> directed \(\tau\)-quotient cycle into consecutive blocks of between
> \(H\) and \(2H-1\) quotient edges, except that one terminal block may
> have fewer than \(H\) edges.  First fix one global support-complete family
> \(\mathscr W_H\) of correct PBBS windows: every lower and upper target
> through depth \(H\) has at least one chosen correct witness.  Assign each
> chosen window, and each true return of residence at most \(H\), to the
> unique carrier block containing its first quotient edge.  A carrier may
> inspect the next \(H\) quotient edges as a read-only collar; every collar
> baseline position remains emitted and owned only by its home block.  For
> each block use all \(N\) spatial lifts and the exact frame sequence (0.2)
> for every return assigned to it, to replace the lifted baseline pieces by
> literal nonzero set-word pieces such that:
>
> 1. every baseline middle owner is marked exactly once overall;
> 2. every witness in \(\mathscr W_H\), including those meeting or crossing
>    a block boundary, is a contiguous OR interval in every required lift;
> 3. the pieces concatenate with the untouched PBBS pieces without an
>    independent reset at each spatial lift;
> 4. every assigned true return is serviced in every spatial lift,
>    including returns which overlap one another inside a block or cross
>    its right boundary;
> 5. the connector overhead, including carrier, collar, and boundary
>    composition costs, is \(O_A(H)\) per quotient block, independent of
>    \(N\); and
> 6. distinct block charts use disjoint home baseline owner positions;
>    collars are context rather than duplicate owner emissions, and the
>    charts compose into one integral global word.

There are at most \(B/H+c_\tau\) blocks, where \(c_\tau\le B\) is the
number of quotient cycles.  Thus item 5, which explicitly includes every
carrier and collar cost, gives total overhead

\[
 O_A\!\left(H(B/H+c_\tau)\right)=O_A(B+HB)=o(W).    \tag{6.1}
\]

Indeed \((B+HB)/W=(1+H)/N=O_A(r^{-1/2})\).  This
summation is valid only because item 5 charges the complete block chart,
including its assigned witnesses and read-only collar composition; no
additional per-return or per-lift toll may be added afterward.

Together with the all-depth support theorem and the standard outer-rank
tail, \(\mathrm{DFB}(H)\) would yield the desired direct PBBS central word.

The quantifier “true PBBS return” in \(\mathrm{DFB}(H)\) is essential.
Replacing it by “primitive” or “terminal maximum” makes item 2 ill-defined:
equation (2.3) shows that the advertised two ports can carry different
labels.  Likewise, independently conjugating a local factor for each
overlapping deck bundle violates item 1; the same middle owner can then be
used by several exact factors.  A legal proof must give one global owner
assignment or prove disjointness before any conjugate charts are combined.

No existing result establishes items 2--4.  The staircase identities
(3.3)--(3.4) provide audited extra dynamic data only for the zero-winding
subfamily.  A positive-winding return still has the universal exact frame
recursion (0.2), but no analogue of (3.3)--(3.4) is asserted here.  The MTF
theorem of Section 4 gives an exact realization only after one already has
a low-weight ordered path cover.  This conditional fallback therefore asks
for the stronger implication

\[
 \boxed{
 \text{all true PBBS dynamic frames, with staircase data at zero winding}
 \Longrightarrow
 \text{deck-shared low-weight ordered MTF braid}.}  \tag{6.2}
\]

## 7. Exact proved and conditional boundary

The following are proved.

1. The full static sector itinerary has the exact protected class (1.3).
2. That class is sparse enough for direct quadratic literal repair to cost
   \(o_A(W)\).
3. Primitive or terminal-maximum roots outside it need not have the claimed
   ports; (2.1)--(2.3) give an exact labelled counterexample.
4. Every true zero-winding return has the dynamic staircase
   (3.2)--(3.4).
5. Within the prescribed chronological refined prefix, independent
   priority-cylinder repair pays the exact portal positions of (4.4), and
   one-letter owner advancement cannot absorb an internal priority
   insertion in that normal form.
6. The edge-volume-uniform physical cost target on the top residence band
   is \(o(H)\) per cut, while \(O(H)\) per whole quotient deck bundle is
   sufficient under the stated deck-sharing accounting.

The following are not proved.

1. \(RP_A\) or its negation.
2. A shared literal fusion for all true short-return frames.
3. \(\mathrm{DFB}(H)\), or any other theorem converting the full dynamic
   return frames into a global owner-injective MTF trajectory.
4. Constant one.

The requested primitive/terminal-sector braid therefore has no valid
literal input.  One rigorously formulated fallback is the conditional
dynamic-frame deck braid (6.2), with exact factor ownership, signed
crossing-mask preservation, and \(O(H)\) overhead per entire quotient
bundle.  It is not the exact or sole remaining theorem while \(RP_A\)
itself remains open.
