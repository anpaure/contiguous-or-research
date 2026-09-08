# Crossing collars around a clean \(C_8\): telescoping and the row-congestion obstruction

Date: 2026-07-26

Method: pure mathematics only.

## 0. Result

The proposed \(\Theta(\sqrt s)\)-stage crossing-collar amplifier does not
work at positive Catalan density under bounded row congestion.

There are two separate obstructions.

First, one clean suffix \(C_8\) router is not itself a common-exterior
physical packet.  Its four port displacements are

\[
                         (1,1,1,2),
\tag{0.1}
\]

and its actual variable row lengths require exterior motions

\[
                         (1,3,0,1).
\tag{0.2}
\]

Thus one common moving exterior cannot make its four strands geodesic.
Any physical successor must use row-dependent exterior motion or add
further switches which change the endpoint action.

Second, suppose this metric problem is somehow solved and all ambient
\(X/Y\) collars are owned exactly.  Let \(S(\mathcal A)\) be the set of
global root rows changed by one fully assembled packet \(\mathcal A\).
At one serviced depth, let \(n_s\) be the maximum number of pointed
windows on one changed row which can differ between the final packet and
the baseline.  For a bounded-width rank-\(s\) composition,

\[
                         n_s\le2s+1
\tag{0.3}
\]

in the unextended local cylinder normalization.  If
\(\Theta(\sqrt s)\) stages each add only \(O(1)\) collar positions, then
\[
                         n_s\le2s+O(\sqrt s)=(2+o(1))s.
\]
More generally \(n_s=O(s)\) whenever the complete physical collar span
is \(O(s)\).

The full carrier, including every crossing collar and every mixed window,
satisfies the statewise occurrence bound

\[
 \boxed{
 M^{\rm full}(\mathcal A)
 \le n_s\,|S(\mathcal A)|.}
\tag{0.4}
\]

The number of intermediate stages does not appear.  If
\(\mathcal A\) is built from \(k\) nested or serial stages on the same
four router strands, then

\[
 \boxed{
 M^{\rm full}(\mathcal A)\le4n_s=O(s),}
\tag{0.5}
\]

even when \(k=\Theta(\sqrt s)\).  Intermediate collar contributions
cancel telescopically; a pointed final window is one occurrence, not one
new unit for every stage which met it.

Now use the dense abstract suffix bank

\[
                         |\mathscr R_s|=C_{s-3}
                         =\left({1\over64}+O(s^{-1})\right)C_s.
\tag{0.6}
\]

For each router \(a\in\mathscr R_s\), let \(S_a\) be the global row
support of its proposed physical amplifier.  Suppose the packet supports
have row congestion at most \(\Delta_s\):

\[
                         \#\{a:P\in S_a\}\le\Delta_s
                         \qquad(P\in D_s).
\tag{0.7}
\]

Then

\[
 \sum_{a\in\mathscr R_s}|S_a|\le\Delta_sC_s,
\tag{0.8}
\]

and (0.4) gives the average full-carrier bound

\[
 \boxed{
 {1\over C_{s-3}}\sum_{a\in\mathscr R_s}
 M^{\rm full}(\mathcal A_a)
 \le
 n_s\Delta_s{C_s\over C_{s-3}}
 =(128+o(1))\Delta_s s.}
\tag{0.9}
\]

The hard Catalan overshoot requires average per-router stage mass

\[
 \left({14\sqrt\pi\over\Gamma\kappa}+o(1)\right)s^{3/2}
\tag{0.10}
\]

in the exact growing-\(D_s\) ledger.  Comparing (0.9) and (0.10) yields

\[
 \boxed{
 \Delta_s\ge
 \left({7\sqrt\pi\over64\Gamma\kappa}+o(1)\right)\sqrt s
 ={0.19386\ldots\over\Gamma\kappa}\sqrt s\,(1+o(1)).}
\tag{0.11}
\]

Consequently:

1. disjoint amplifiers, \(\Delta_s=1\), have average
   \(M^{\rm full}=O(s)\);
2. every bounded-congestion family has average \(O(s)\);
3. every family with \(\Delta_s=o(\sqrt s)\) has
   \(M^{\rm full}=o(s^{3/2})\); and
4. attaching \(\Theta(\sqrt s)\) private carrier rows to every one of
   \(C_{s-3}\) routers is impossible: it demands
   \(\Theta(C_s\sqrt s)\) row incidences from a \(C_s\)-row fibre.

At this stage the only remaining scalar possibility is a high-congestion
joint packet with \(\Delta_s=\Omega(\sqrt s)\), or a larger combined
footprint whose parent-context density is recomputed from scratch. The
high-congestion case is closed by
MATH_THEOREM_C8_HIGH_CONGESTION_OVERLAY_DICHOTOMY_20260726.md: after
target cancellation, router-coupled reuse forces
\(\Xi=\Omega(\sqrt s)\), while decoupled reuse is physical background
and cannot be multiplied by router count.

This is an occurrence and ownership invariant, not an entropy argument.
It proves the requested \(O(s)\) bound for nested same-strand compositions
and the \(o(s^{3/2})\) bound for every positive-density bounded-width
composition of sub-\(\sqrt s\) row congestion.

## 1. Geodesic exterior motion is rowwise

Let \(J\) have size \(2s\).  A candidate physical stage on row \(P\) has
endpoints

\[
 A_P=O^L_P\cup P,\qquad
 B_P=O^R_P\cup(J\setminus\tau(P)),
\tag{1.1}
\]

where the exteriors have the same size and are disjoint from \(J\).  Put

\[
                         e_P=|O^L_P\setminus O^R_P|.
\tag{1.2}
\]

The exact Johnson distance is

\[
 d_J(A_P,B_P)=e_P+|P\cap\tau(P)|.
\tag{1.3}
\]

Every segment of a minimum wreath is geodesic.  Therefore an \(s\)-step
stage requires

\[
 \boxed{
 e_P=|P\setminus\tau(P)|.}
\tag{1.4}
\]

For the suffix \(C_8\), order the four local roots as

\[
 R_0=A110100B,\quad R_1=A111000B,\quad
 R_2=A110010B,\quad R_3=A101100B.
\tag{1.5}
\]

The endpoint action is

\[
 R_0\mapsto R_3,\quad R_1\mapsto R_0,\quad
 R_2\mapsto R_1,\quad R_3\mapsto R_2,
\tag{1.6}
\]

and direct comparison gives (0.1).  Hence no common value of \(e_P\)
satisfies (1.4).

The toggled abstract paths have semilengths

\[
                         s,\quad s+2,\quad s-1,\quad s-1.
\tag{1.7}
\]

For a path of actual length \(q_P\), geodesicity instead requires

\[
 e_P=q_P-|P\cap\tau(P)|,
\tag{1.8}
\]

which gives (0.2).  Thus even the variable-length abstract rows cannot
share one moving exterior.

Suppose several exterior-moving stages are placed successively on one
global row.  A literal connector requires

\[
 O^R_{j,P}=O^L_{j+1,\tau_j(P)}
\tag{1.9}
\]

after transporting the row label.  This equality is part of the seam
ledger; merely naming the two exteriors by the same abstract chart does
not establish it.

Moreover, a minimum Johnson path exchanges every initially present
coordinate exactly once and every initially absent coordinate exactly
once.  Therefore the deletion menus

\[
 (O^L_{j,P}\setminus O^R_{j,P})
 \mathbin{\dot\cup}
 (P_j\cap\tau_j(P_j))
\tag{1.10}
\]

of disjoint geodesic stages on one row are pairwise disjoint after
transport to the global coordinate frame.  Exterior motion cannot pay
for the same local mismatch repeatedly on one minimum wreath.

Equations (1.9)--(1.10) are necessary metric conditions.  They do not by
themselves prove ambient \(X/Y\) ownership.

## 2. Exact \(X/Y\) collar cocycle

Let a proposed packet be assembled through intermediate ambient path
collections

\[
                         F_0,F_1,\ldots,F_k.
\tag{2.1}
\]

All ledgers below are written in one common incoming frame.  Let
\(\mathbf X(F)\) and \(\mathbf Y(F)\) denote the complete multisets of
ambient middle states and ambient adjacent-union colours used by \(F\),
including every exterior coordinate present at each intermediate colour.
Define the stage defects

\[
\begin{aligned}
 \varepsilon^X_j&=\mathbf X(F_j)-\mathbf X(F_{j-1}),\\
 \varepsilon^Y_j&=\mathbf Y(F_j)-\mathbf Y(F_{j-1}).
\end{aligned}
\tag{2.2}
\]

Then, target by target,

\[
 \boxed{
 \sum_{j=1}^k\varepsilon^X_j
   =\mathbf X(F_k)-\mathbf X(F_0),\qquad
 \sum_{j=1}^k\varepsilon^Y_j
   =\mathbf Y(F_k)-\mathbf Y(F_0).}
\tag{2.3}
\]

If the stages carry transported monodromies, the same formula is

\[
 \varepsilon^{X/Y}_{\rm tot}
 =\sum_{j=1}^k(g_{j-1})_*\varepsilon^{X/Y}_j,
\tag{2.4}
\]

where \(g_{j-1}\) is the cumulative literal chart before stage \(j\).
An exact packet requires

\[
                         \varepsilon^X_{\rm tot}
                         =\varepsilon^Y_{\rm tot}=0.
\tag{2.5}
\]

Equations (2.3)--(2.5) are the complete collar additivity law.  In
particular:

* an intermediate collar cancels only when the outgoing occurrence of
  one stage is literally the same ambient state or colour as the incoming
  occurrence of the next stage;
* if the exteriors are merely equinumerous or abstractly isomorphic,
  there is no cancellation;
* after literal identification, the two copies occur with opposite signs
  and cancel targetwise; and
* only unmatched outer collars remain in the final \(X/Y\) defect.

Thus \(k\) nested collars do not create \(k\) independent ownership
budgets.  Their signed internal boundaries telescope.

The same law holds if some \(F_j\) is only an open path ledger rather than
an exact factor: its nonzero defect is retained in (2.4) and must be
cancelled by later transported defects.  Setting it to zero because a
local \(b\)-factor owns an abstract shore would omit the moving-exterior
ambient colours.

## 3. Exact carrier decomposition

Fix a serviced depth \(q\).  For an ambient cyclic row word \(\Pi\), let

\[
 \mu_q(\Pi)=\sum_h e_{I_\Pi(h,m-q)}
\tag{3.1}
\]

be its pointed-window target histogram.  For a path collection \(F\), sum
this over all its rows.

The stagewise carrier differences telescope exactly:

\[
 \boxed{
 \sum_{j=1}^k
 \bigl(\mu_q(F_j)-\mu_q(F_{j-1})\bigr)
 =\mu_q(F_k)-\mu_q(F_0).}
\tag{3.2}
\]

This formula includes all crossing collars because \(\mu_q(F_j)\) is
computed from the complete ambient row words.

There is a second useful description.  For a final pointed window
\(\omega=(P,h)\), let \(J(\omega)\subseteq[k]\) be the set of stage
supports it meets.  Partitioning occurrences gives

\[
 \boxed{
 \Delta_q
 =\sum_{\varnothing\ne I\subseteq[k]}\Xi_{I,q},}
\tag{3.3}
\]

where \(\Xi_{I,q}\) is the signed sum over windows with \(J(\omega)=I\).
This is a disjoint partition of pointed occurrences, not
inclusion--exclusion.

The singleton terms are isolated-stage carriers.  Terms with
\(|I|\ge2\) are mixed crossing-collar tensors.  They are not additional
copies of every singleton carrier.  Equations (3.2)--(3.3) imply:

* for influence-separated stages, the singleton carriers add;
* for nested or overlapping stages, the mixed terms must be computed
  jointly;
* counting one mixed window once for every stage it meets is invalid; and
* intermediate stage gains may cancel even when their unsigned masses
  are large.

This is the exact additivity/cancellation theorem requested for the full
carrier.

## 4. The pointed-occurrence invariant

Let \(S(F_k,F_0)\) be the set of global rows whose final cyclic word
differs from the baseline.  For one such row \(P\), put

\[
 \Delta_{q,P}=\mu_q(\Pi_P^k)-\mu_q(\Pi_P^0).
\tag{4.1}
\]

Both histograms have the same number of pointed occurrences.  Hence

\[
 {1\over2}\|\Delta_{q,P}\|_1
 \le
 \#\{\text{pointed starts on row }P
       \text{ whose target changed}\}.
\tag{4.2}
\]

For a complete rank-\(s\) local cylinder there are \(2s+1\) cyclic
starts, so

\[
                         {1\over2}\|\Delta_{q,P}\|_1\le2s+1.
\tag{4.3}
\]

If the packet is embedded in a larger row but its complete changed
position set has total cyclic span \(L_s\), a window can change only when
one of its two boundaries cuts that span.  Consequently

\[
                         {1\over2}\|\Delta_{q,P}\|_1\le2L_s.
\tag{4.4}
\]

Thus (4.3) remains \(O(s)\) for every bounded-width composition with
\(L_s=O(s)\).  A packet whose collar reaches a much larger span must use
that larger span in both its occurrence ledger and its parent-context
count; it cannot retain the old size-\(s\) Catalan placement density.

Summing (4.2) over the changed rows proves

\[
 {1\over2}\|\Delta_q\|_1
 \le n_s|S(F_k,F_0)|.
\tag{4.5}
\]

Actual cap descent is at most the positive mass
\(\|\Delta_q\|_1/2\), proving (0.4).

Notice that (4.5) concerns the final-minus-baseline packet.  It is
independent of the number of intermediate stages.  Applying the triangle
inequality to every stage separately gives a weaker bound and can
overcount the same pointed occurrence \(k\) times.

For one clean \(C_8\) whose completed collars change only its four
transported strands, (4.3) proves (0.5).

## 5. Positive-density packing

The dense suffix catalogue has

\[
                         A_s=C_{s-3}
\tag{5.1}
\]

abstract clean routers on the \(C_s\) root rows.  Suppose a physical
amplifier \(\mathcal A_a\) has been assigned to every router
\(a\in\mathscr R_s\), and let \(S_a\) be its final changed-row support.

If every root row belongs to at most \(\Delta_s\) supports, double counting
the incidence set

\[
                         \{(a,P):P\in S_a\}
\tag{5.2}
\]

gives (0.8).  Combining with (0.4) gives

\[
\begin{aligned}
 {1\over A_s}\sum_a M^{\rm full}(\mathcal A_a)
 &\le {n_s\over A_s}\sum_a|S_a|\\
 &\le n_s\Delta_s{C_s\over C_{s-3}}.
\end{aligned}
\tag{5.3}
\]

Using

\[
 {C_s\over C_{s-3}}
 ={8(2s-1)(2s-3)(2s-5)\over s(s-1)(s+1)}
 =64+O(s^{-1})
\tag{5.4}
\]

and \(n_s\le(2+o(1))s\) for the proposed
\(\Theta(\sqrt s)\) bounded-width composition proves (0.9).

Now recall the exact hard-overshoot threshold for the dense \(C_8\) bank:

\[
 \overline M_s^{\rm req}
 =
 \left({14\sqrt\pi\over\Gamma\kappa}+o(1)\right)s^{3/2}.
\tag{5.5}
\]

Comparison of (5.3)--(5.5) yields

\[
 \Delta_s
 \ge
 {14\sqrt\pi\over128\Gamma\kappa}\sqrt s\,(1+o(1))
 ={7\sqrt\pi\over64\Gamma\kappa}\sqrt s\,(1+o(1)),
\tag{5.6}
\]

which is (0.11).

This proves the disjoint/nested dichotomy.

* If the \(\Theta(\sqrt s)\) stages are nested on the same bounded set of
  rows, (4.5) gives only \(O(s)\) mass.
* If they use \(\Theta(\sqrt s)\) private rows per router, (5.2) forces
  \(\Theta(C_s\sqrt s)\) total row incidences, contradicting bounded
  congestion.
* If the same payload rows are shared among
  \(\Theta(\sqrt s)\) routers, then
  \(\Delta_s=\Theta(\sqrt s)\).  The proposed bank is one high-overlap
  joint atom; its gains cannot be multiplied router by router.

## 6. Scope of the obstruction

The theorem does not construct an exterior-moving packet.  It assumes
one only to prove an upper bound on what any bounded-width completion
could contribute.

It also does not assert \(M^{\rm full}=O(s)\) for an arbitrary
high-congestion or macroscopic-span construction. After the full-overlay
argument cited above, the exact alternatives left open are:

1. a packet whose physical collar span is \(\omega(s)\), with its smaller
   combined-footprint parent density recomputed exactly; or
2. a different dense parent placement not governed by the literal
   \(N_{R,s}\) ledger.

For the requested \(\Theta(\sqrt s)\) composition around one clean
\(C_8\), every bounded-row-support nested construction has
\(M^{\rm full}=O(s)\), every positive-density bounded-congestion bank has
average \(o(s^{3/2})\) whenever \(\Delta_s=o(\sqrt s)\), and every
bounded-span high-congestion joint completion either has
\(\Xi=\Omega(\sqrt s)\) or loses the claimed multiplicity after
decoupling/cancellation. This rules out the proposed bounded-span clean
amplifier family.
