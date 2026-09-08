# Outer moving-frame packet flow: an exact symmetric fractional cover and the blossom obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

The local parity/trace compiler of
\(\texttt{MATH\_ATTACK\_S\_PARITY\_COMPLETE\_MAPPING\_TRACE\_ENTROPY\_CUT\_20260726.md}\)
is taken as proved.  The remaining variables choose physical packet frames,
three-shore \(B_4\) resolutions, and one legal all-depth packet state.
The packet partition is the rotation-equivariant selector of
\(\texttt{MATH\_THEOREM\_W\_ROTATION\_EQUIVARIANT\_STATUS\_NECKLACE\_PACKETS\_20260726.md}\);
the legal local frame changes are the common-owner three-shore resolutions
of
\(\texttt{MATH\_THEOREM\_CONTEXTUAL\_THREE\_SHORE\_DENSE\_RECOUPLER\_20260726.md}\).

There is an exact master transportation formulation in which:

1. every middle owner has total packet load one;
2. every signed target at every \(q\le H\) has demand one;
3. one packet variable simultaneously determines all signs and depths; and
4. the three-shore cells of one associator resolution cannot be weighted
   independently.

If one legal rotation-equivariant atlas covers \(G\) of the

\[
                         W=\binom{2m}{m}                         \tag{0.1}
\]

middle owners, then averaging all its coordinate conjugates under
\(\Gamma=S_{2m}\), with normalization \(W/G\), gives an exact fractional
owner cover.  At either sign and every depth \(q\), every target has the
same occurrence load

\[
 \boxed{
 \lambda_q={W\over N_q}\ge1,\qquad
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.}               \tag{0.2}
\]

The same averaged packet weights work simultaneously for all
\(0\le q\le H\).  By accepting the common fraction \(N_q/W\) of every
depth-\(q\) occurrence and sending the surplus to a dump node, one obtains
target equality, not merely a covering inequality.  Thus every signed
target has an \(S_{2m}\)-averaged fractional exact cover.

This closes the fractional Hall question for the full moving-frame
catalogue.  It does not round the catalogue integrally.

The natural occupancy-profile refinement is not a network or
totally-unimodular system.  When the global perfect matching is
disaggregated into edge marginals \(y_e\), its degree equations contain
the submatrix

\[
 B_\triangle=
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},
 \qquad
 |\det B_\triangle|=2.                               \tag{0.3}
\]

On six coordinates, putting weight \(1/2\) on every edge of two disjoint
triangles satisfies all degree-one equations but is not a convex
combination of perfect matchings.  It violates the exact odd-set inequality

\[
 y(E(U))\le {|U|-1\over2},
 \quad\text{equivalently}\quad y(\delta(U))\ge1
 \qquad(|U|\text{ odd}).                             \tag{0.4}
\]

The three \(B_4\) shores are precisely the three perfect matchings on a
four-set, and their local recouplings are even alternating switches.  They
do not enforce the global inequalities (0.4).  Hence profile
transportation without blossom rows is a strict relaxation, while adding
the blossom rows destroys the proposed TU/network proof.

This is an integrality-method obstruction, not an outer Hall obstruction:
the symmetric fractional point is already a convex combination of whole
matchings and obeys every blossom inequality.  The surviving theorem is
to round the common all-depth master point while retaining whole matching,
whole associator-resolution, and whole packet columns.

## 1. Legal moving-frame packet columns

Put

\[
 \Omega=[2m],\qquad
 {\cal M}=\binom{\Omega}{m},\qquad
 {\cal T}_q^-=\binom{\Omega}{m-q},\qquad
 {\cal T}_q^+=\binom{\Omega}{m+q}.                  \tag{1.1}
\]

A physical frame consists of a perfect matching of \(\Omega\), a cyclic
order of its matched pairs, and all bounded \(B_4\) carrier blocks used by
the three-shore associator.  The rotation-equivariant status selector
partitions its retained owners into packet carriers.  On every carrier, a
legal option contains:

1. one complete three-shore resolution on every connected \(24\)-owner
   associator support;
2. the associated packet frame and coordinate conjugate; and
3. one instance of the proved local parity/trace compiler in every
   resulting cell.

The word *complete* is essential.  Six local cells on one shore partition
one common \(24\)-owner support.  They are not six independent owner
supplies.

Let \({\cal A}\) be the catalogue of all legal packet options over all
coordinate frames.  For \(a\in{\cal A}\), write \(P(a)\subseteq{\cal M}\)
for its owner set and

\[
 \tau_{a,q}^{\epsilon}:P(a)\longrightarrow{\cal T}_q^\epsilon
 \qquad(\epsilon\in\{-,+\},\ 0\le q\le H)            \tag{1.2}
\]

for its literal signed trace map.  The local theorem makes (1.2)
injective for every fixed \(a,q,\epsilon\).  Define the incidence
coefficients

\[
\begin{aligned}
 B_{X,a}&={\bf1}_{\{X\in P(a)\}},\\
 A_{q,T,a}^{\epsilon}
 &={\bf1}_{\{T\in\tau_{a,q}^{\epsilon}(P(a))\}} .
\end{aligned}                                        \tag{1.3}
\]

Thus

\[
 \sum_XB_{X,a}=|P(a)|,\qquad
 \sum_TA_{q,T,a}^{\epsilon}=|P(a)|                  \tag{1.4}
\]

for every signed depth.  One and the same column \(a\) supplies every row
in (1.3); there are no depthwise packet copies.

## 2. The common all-depth master LP

The fractional moving-frame cover is

\[
\begin{aligned}
 \sum_{a\in{\cal A}}B_{X,a}x_a&=1
                  &&(X\in{\cal M}),\\
 \sum_{a\in{\cal A}}A_{q,T,a}^{\epsilon}x_a&\ge1
                  &&(q\le H,\ \epsilon,\ T\in{\cal T}_q^\epsilon),\\
 x_a&\ge0.
\end{aligned}                                        \tag{2.1}
\]

An integral solution has \(x_a\in\{0,1\}\).  Its first line says that the
chosen packet options are owner-disjoint and cover every owner exactly
once.  Because every option is a whole legal factor, this line also
preserves whole cycles and associator resolution legality.

For a literal transportation form, introduce accepted-occurrence variables
\(f_{q,T,a}^{\epsilon}\) and dump variables
\(d_{q,T,a}^{\epsilon}\):

\[
\begin{aligned}
 f_{q,T,a}^{\epsilon}+d_{q,T,a}^{\epsilon}
 &=A_{q,T,a}^{\epsilon}x_a,\\
 \sum_a f_{q,T,a}^{\epsilon}&=1
                  &&(q,\epsilon,T),\\
 f_{q,T,a}^{\epsilon},d_{q,T,a}^{\epsilon}&\ge0.
\end{aligned}                                        \tag{2.2}
\]

The variables \(f,d\) only audit which fractional occurrences are needed
to meet unit demand.  They do not alter the packet option.  In particular,
allowing separate \(f\)'s at different depths does not make a separate
depthwise construction choice: all capacities in (2.2) come from the same
\(x_a\).

Equations (2.1)--(2.2) are the exact source-allocation/transport model.
The owner equations are equalities, target demands are singleton
equalities after dumping, and all physical nonlinearities are confined to
the legal column catalogue \({\cal A}\).

There is a necessary surplus which should not be mistaken for a defect.
Summing (1.4) against any solution of the owner equations gives, at every
signed depth,

\[
 \sum_T\sum_aA_{q,T,a}^{\epsilon}x_a
 =\sum_a|P(a)|x_a
 =W.                                                  \tag{2.3}
\]

For \(q>0\), one has \(N_q<W\).  Therefore the raw target loads cannot all
equal one under exact middle ownership.  The mathematically correct
meaning of an exact fractional target cover is unit accepted demand plus
the forced surplus \(W-N_q\) in the dump variables of (2.2).

## 3. The \(S_{2m}\)-averaged fractional exact cover

Fix one legal base atlas

\[
 {\cal F}_0=\{a_1,\ldots,a_s\}\subseteq{\cal A}       \tag{3.1}
\]

whose packet owner sets are disjoint and whose union

\[
 {\cal G}_0=\dot\bigcup_{j=1}^sP(a_j)                \tag{3.2}
\]

has size \(G\).  The rotation-equivariant necklace theorem gives
\(G=W-e^{-\Omega(m)}W\) in its permitted range, but only \(G>0\) is
needed below.  The local compiler gives exactly one occurrence per retained
owner at each signed depth.

Every \(\sigma\in\Gamma=S_{2m}\) conjugates (3.1) to another legal atlas.
Give every conjugated base column the weight

\[
                         \alpha={W\over G|\Gamma|},               \tag{3.3}
\]

aggregating weights when two named columns coincide.

### Theorem 3.1 (common symmetric fractional cover)

The weights (3.3) satisfy the owner equalities in (2.1).  For both signs
and every \(0\le q\le H\), every target \(T\in{\cal T}_q^\epsilon\) has
load exactly \(W/N_q\).

#### Proof

The action of \(\Gamma\) is transitive on \({\cal M}\).  Double-count the
pairs

\[
 (\sigma,X_0),\qquad \sigma\in\Gamma,\quad
 X_0\in{\cal G}_0,\quad \sigma X_0=X.                \tag{3.4}
\]

For every fixed \(X\in{\cal M}\), their number is
\(|\Gamma|G/W\).  Multiplication by (3.3) gives owner load one.

Fix \(q,\epsilon\).  Across the base atlas there are exactly \(G\)
signed occurrences, one for every retained owner.  The group is
transitive on the \(N_q\) targets of the relevant rank.  Double-counting
the conjugates of these \(G\) occurrences shows that every fixed target
appears

\[
                         {|\Gamma|G\over N_q}        \tag{3.5}
\]

times in the full conjugate list, with multiplicity.  The local
injectivity makes the packet incidence in (1.3) binary; coincidences
between different packets are correctly counted as distinct source
occurrences.  Multiplication by (3.3) gives \(W/N_q\).
\(\square\)

Since the middle binomial coefficient is maximal,

\[
                         N_q\le W.                   \tag{3.6}
\]

Thus (3.3) is feasible for the cover inequalities at all depths
simultaneously.  To obtain the exact transportation equality (2.2), put

\[
\begin{aligned}
 f_{q,T,a}^{\epsilon}
 &={N_q\over W}A_{q,T,a}^{\epsilon}x_a,\\
 d_{q,T,a}^{\epsilon}
 &=\left(1-{N_q\over W}\right)
   A_{q,T,a}^{\epsilon}x_a .
\end{aligned}                                        \tag{3.7}
\]

Theorem 3.1 makes every target acceptance sum one.  Formula (3.7) again
uses the same \(x_a\) for every \(q\); only the surplus bookkeeping varies.

### Corollary 3.2 (fractional outer Hall is closed)

The complete moving-frame packet catalogue has zero fractional uncovered
mass simultaneously at every protected signed depth.  Therefore any
remaining linear deficit for a fixed matching, fixed suffix, fixed
necklace arc, or fixed occupancy frame is not invariant under the full
\(S_{2m}\)-moving catalogue.

This statement depends on averaging legal whole atlases.  Averaging
ownerwise frame labels which do not assemble into packet factors would not
prove it.

## 4. Occupancy-profile aggregation

Let

\[
                         \Omega=C_1\dot\cup\cdots\dot\cup C_b             \tag{4.1}
\]

be any fixed coordinate-block partition, and define the occupancy profile

\[
 \kappa(S)=\bigl(|S\cap C_1|,\ldots,|S\cap C_b|\bigr).             \tag{4.2}
\]

For a legal column \(a\), define its exact profile transport census

\[
 C_{a,q}^{\epsilon}(u,v)
 =\#\{X\in P(a):
       \kappa(X)=u,\ 
       \kappa(\tau_{a,q}^{\epsilon}(X))=v\}.          \tag{4.3}
\]

It obeys the source conservation law

\[
 \sum_v C_{a,q}^{\epsilon}(u,v)
 =\#\{X\in P(a):\kappa(X)=u\}                        \tag{4.4}
\]

for every signed depth.  Aggregating (2.1) gives the necessary profile
transport inequalities

\[
\begin{aligned}
 \sum_a x_a\#\{X\in P(a):\kappa(X)=u\}
 &=\#\{X\in{\cal M}:\kappa(X)=u\},\\
 \sum_{a,u}x_aC_{a,q}^{\epsilon}(u,v)
 &\ge\#\{T\in{\cal T}_q^\epsilon:\kappa(T)=v\}.
\end{aligned}                                        \tag{4.5}
\]

The variables \(x_a\) remain common across all \(q,\epsilon\).  Thus
(4.5) is a coupled multicommodity transportation system: one hypercolumn
simultaneously carries one transport table for every signed depth.  It is
not the direct sum of the depthwise bipartite flow matrices.

For the symmetric point of Theorem 3.1, every literal target has the same
load, so every profile demand in (4.5) has the same surplus factor
\(W/N_q\).  Profile aggregation therefore creates no new fractional cut.
It can only discard literal Hall information.

## 5. Why the natural profile refinement is not TU

To seek a network formulation, one naturally disaggregates a physical
frame into its selected matching edges.  Let \(y_e\) be the marginal of
edge \(e\in\binom{\Omega}{2}\).  Every whole perfect matching column
satisfies

\[
                         \sum_{e\ni v}y_e=1
                         \qquad(v\in\Omega).          \tag{5.1}
\]

The unsigned vertex-edge incidence matrix in (5.1) is a submatrix of the
edge-disaggregated profile formulation.  On vertices \(1,2,3\) and edge
columns \(12,23,31\), it is, up to column order, \(B_\triangle\) from
(0.3).  Hence:

### Theorem 5.1 (non-TU minor)

Every edge-disaggregated occupancy-profile formulation retaining the
matching degree rows (5.1) contains a square submatrix of determinant
\(\pm2\).  Its constraint matrix is not totally unimodular and cannot be
a directed network matrix.

Adding further occupancy or target rows cannot repair total
unimodularity, because the same square submatrix remains.  One can avoid
the displayed minor only by keeping whole perfect matchings as
Dantzig--Wolfe columns or by using a genuinely different extended
formulation.

## 6. The exact odd-set obstruction

The determinant has a literal fractional witness.  On six coordinates,
put

\[
 y_{12}=y_{23}=y_{31}
 =y_{45}=y_{56}=y_{64}={1\over2},                   \tag{6.1}
\]

and put all other edge marginals equal to zero.  Every vertex has incident
sum one, so (5.1) holds.

No perfect matching lies in the support of (6.1), because each of the two
support components has odd order.  More invariantly, every perfect
matching \(M\) and every odd set \(U\subseteq\Omega\) obey

\[
 |M\cap\delta(U)|\equiv |U|\pmod2,
 \qquad |M\cap\delta(U)|\ge1.                        \tag{6.2}
\]

Taking convex combinations gives the blossom inequalities

\[
 y(\delta(U))\ge1,
 \qquad
 y(E(U))\le {|U|-1\over2}.                           \tag{6.3}
\]

For \(U=\{1,2,3\}\), the vector (6.1) has

\[
 y(\delta(U))=0,\qquad y(E(U))={3\over2}>1.          \tag{6.4}
\]

Thus degree conservation and ordinary source-target transportation are
not sufficient for a moving physical frame.

### B4 interpretation

On a four-set \(\{a,b,c,d\}\), the three local shores are

\[
 ab\mid cd,\qquad ac\mid bd,\qquad ad\mid bc.        \tag{6.5}
\]

They are exactly the three perfect matchings of that four-set.  A
three-shore associator replaces one by another through an even alternating
four-coordinate recoupling.  Such moves preserve (6.2) for every odd
coordinate set.  Consequently:

1. the local three-shore simplex is integral;
2. overlapping \(B_4\) recouplings do not turn the global degree polytope
   into a network polytope; and
3. a profile LP which records local shore proportions but omits (6.3)
   admits frame marginals which no common integral matching can realize.

This is the precise odd-set obstruction promised by the TU audit.  It is
not removed by refining owner and target occupancies.  A refinement can
exclude (6.1) only by adding rows which imply the relevant blossom
inequality.  Since the old determinant-two submatrix remains, that
augmented matrix is still not TU.

## 7. Exact boundary and remaining outer theorem

The following statements are proved.

1. The all-frame, all-shore master LP (2.1) has a common all-depth
   \(S_{2m}\)-averaged fractional solution.
2. The solution is a convex combination of legal whole atlases, so it
   satisfies all perfect-matching odd-set inequalities automatically.
3. The natural occupancy-profile/edge transportation relaxation is
   non-TU and strictly larger than the convex hull of physical frames.
4. Independent depthwise rounding is invalid because every packet column
   fixes all \(q,\epsilon\) simultaneously.

Therefore the blossom witness does **not** prove that an integral outer
cover is impossible.  It proves that ordinary network flow, TU rounding,
or a degree-only dependent rounding theorem cannot establish it.

The exact remaining statement is:

> **Common all-depth moving-frame rounding theorem.**  Round the symmetric
> point of Theorem 3.1 to owner-disjoint legal whole packet columns so that,
> with one common packet option at every depth,
> \[
>  \sum_{q=1}^{H}\sum_{\epsilon\in\{-,+\}}
>  \sum_{T\in{\cal T}_q^\epsilon}
>  \left(1-\sum_aA_{q,T,a}^{\epsilon}x_a\right)_+
>  =o(W).
> \tag{7.1}
> \]
> The rounding must preserve whole perfect matchings, all blossom
> constraints, whole connected \(B_4\)-associator resolutions, and the
> local compiler cycles.

Equivalently, one needs a discrepancy or absorption theorem for the
whole-column master matrix, not another depthwise transportation theorem.
The \(S_{2m}\)-average supplies the exact fractional starting point; the
determinant-two triangle identifies the first unavoidable integrality
constraint.
