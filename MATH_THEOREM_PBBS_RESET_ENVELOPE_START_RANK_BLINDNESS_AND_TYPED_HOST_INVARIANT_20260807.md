# The SCD start-rank ledger does not determine reset envelopes; the exact missing datum is occurrence typing

**Date:** 2026-08-07  
**Method:** maximal PBBS antecedents, symmetry, and occurrence-labelled
rainbow matching  
**Status:** unconditional scope theorem and exact residual invariant.  The
ordinary SCD start-rank census determines reset *counts* but not the safe
coordinate set of any reset occurrence.  Consequently it cannot imply the
rephased-upper host theorem without one additional occurrence-labelled
typing row.

## 1. What the envelope actually is

Fix a literal rank-(m) PBBS owner chronology

\[
 T=(T_i)_{i\in\mathbb Z_W},
 \qquad |T_i|=m,
\]

and deadline (d).  The maximal source envelope at physical source
position (p) is

\[
 \boxed{P_p=\bigcap_{h=0}^{d}T_{p-h}.}
\tag{1.1}
\]

If the already assigned lower targets whose source intervals contain
(p) are (S\) with intervals (I_S), then the coordinatewise maximal
safe letter is

\[
 \boxed{
 C_p=P_p\cap\bigcap_{S:p\in I_S}S.}
\tag{1.2}
\]

Thus (C_p), not the scalar fact that (p) is called a reset, is the
actual owner envelope available to a new literal use of that position.
The forced endpoint labels of the Johnson trace lie in (C_p) whenever
the pinned-envelope test is feasible, so (C_p\ne\varnothing); no large
rank or exterior aperture follows from nonemptiness.

## 2. Start rank is blind to (1.2)

The adaptive SCD ledger records the number of chains beginning at each
rank and the lengths of their fragmented pieces.  In particular it
determines the scalar quantities

\[
 P,\qquad F,\qquad S=g-P,
\tag{2.1}
\]

and it identifies which chain remainders are rephased.  It does not record
any of the following occurrence data:

1. the physical source position (p);
2. the ordered owner window (T_{p-d},\ldots,T_p);
3. its intersection (P_p);
4. the target intervals passing through (p); or
5. their intersection with (P_p).

### Theorem 2.1 (start-rank blindness)

There is no function of the SCD start-rank ledger and a reset occurrence's
start-rank class which returns its labelled safe set (C_p).  In
particular, no lower bound on the typed degree of an upper flag into the
reset bank follows from the scalar ledger alone.

#### Proof

The start-rank ledger is invariant under every permutation of the ground
coordinates.  Apply a coordinate permutation (sigma) to a literal PBBS
history.  Its SCD ranks, piece lengths, remainders, and reset counts are
unchanged, whereas (1.1)--(1.2) give

\[
 P_p\longmapsto\sigma(P_p),
 \qquad C_p\longmapsto\sigma(C_p).
\tag{2.2}
\]

Since a feasible source letter is nonempty and in the central regime is
not the full ground set, its orbit contains more than one labelled set.
The invariant ledger cannot distinguish these outcomes.  Hence it cannot
recover (C_p).

More strongly, the degree conclusion fails even if one ignores which
reset occurrence receives which set.  Fix an upper flag

\[
 f=(M,u),\qquad |M|=m-d-2,quad U=M\cup\{u\}.
\]

A successor host must contain (M) and have entering label (u).  A
scalar reset bank of the prescribed size can be labelled entirely by
central edges with entering labels different from (u), because the
complementary central-edge supply is exponentially larger than the reset
count.  It then has flag degree zero while retaining exactly the same
start-rank census.  Therefore the ledger alone implies neither a positive
degree nor a Hall/rainbow cut.  \(\square\)

The obstruction is not a missing asymptotic count.  It is a missing
correlation between absolute coordinate labels, owner order, and physical
occurrences.

## 3. The complete ideal successor universe

Write (n=2m+1) and (t=m-d).  For a rephased upper flag

\[
 M\in{[n]\choose t-2},
 \qquad U=M\cup\{u\}\in{[n]\choose t-1},
\]

an ideal immediate-successor central edge is obtained from

\[
 B\in{[n]\setminus U\choose d+1},
 \qquad Y=M\cup B,
 \qquad T=U\cup B=Y\cup\{u\}.
\tag{3.1}
\]

For target-disjoint flags the coloured union has exact colour degree

\[
 D={m+d+2\choose d+1}
\tag{3.2}
\]

and maximum host-vertex load

\[
 \Delta={m\choose d+1}.
\tag{3.3}
\]

Consequently

\[
 \frac D\Delta\longrightarrow e^{\pi/4}=2.19328\ldots>2.
\tag{3.4}
\]

The graph form of Aharoni--Haxell uses the sufficient cut

\[
 \nu\!\left(\bigcup_{f\in X}\mathcal G_f\right)
 >2(|X|-1).
\tag{3.5}
\]

Kőnig's theorem and (3.2)--(3.4) therefore prove a disjoint ideal host
for every target-disjoint flag bank for all sufficiently large optimal
parameters.  The factor (2) in (3.5) is essential; a factor-one rainbow
criterion is not valid here.

## 4. The weakest occurrence-labelled typing invariant

Choose the upper endpoint positions (e_f) so that the three position
sets

\[
 \{e_f\},\qquad\{e_f+1\},\qquad\{e_f-d\}
\tag{4.1}
\]

are pairwise disjoint.  The sparse-circulant scheduling lemma supplies
such a choice with enormous room.  Put

\[
 q_f=e_f+1,\qquad p_f=e_f-d.
\]

The exact additional datum needed from the literal PBBS chart is:

* the successor safe set (C_{q_f}) and its phase/state type;
* the lag safe set (C_{p_f}) and its phase/state type; and
* the list of central coatom--owner edges physically legal at (q_f).

Before an owner occurrence is frozen, one may formally define the
prospective typed successor colour class

\[
 \mathcal G_f^{\rm typ}
 =\left\{
 (Y,T):
 \begin{array}{l}
 B\in{C_{q_f}\setminus U_f\choose d+1},\\
 \text{there is }K\subseteq M_f\cap C_{q_f}
       \text{ with }A_{q_f}=B\cup K,\\
 Y=M_f\cup B,\\
 T=Y\cup\{u_f\},\\
 (q_f,A_{q_f},B,Y,T)\text{ has the required phase/state type, and}\\
 \text{installing }A_{q_f}\text{ preserves every mandatory-core and}\\
 \text{coordinatewise positive-hit cut}
 \end{array}
 \right\}.
\tag{4.2}
\]

Here the PBBS suffix indexing is

\[
 M_f=Z_{e_f,d-1},\quad U_f=Z_{e_f,d},\quad
 Y=Z_{e_f+1,d},\quad T=Z_{e_f+1,d+1}.
\tag{4.2a}
\]

Thus \(Y\) is a depth-\(d\) coatom, not a source letter.  The new source
letter has exterior

\[
 B=A_{q_f}\setminus U_f,
\]

and may contain a filler \(K\subseteq M_f\).  Distinct legal fillers for
one \(B\) induce the same central edge and count only once.

The lag position is legal for (f) exactly when

\[
 \boxed{|C_{p_f}\setminus U_f|\ge d+1}
\tag{4.3}
\]

with the required phase/state compatibility.  The actual lag letter may
then use any (L_f\in{C_{p_f}\setminus U_f\choose d+1}); its value need
not be distinct from another lag letter because the physical positions
are already distinct.

### Scope correction 4.1 (prospective, not frozen-history)

Once the literal history and its owner \(T_{q_f}\) are fixed, (1.4)
forces

\[
 B=T_{q_f}\setminus U_f,
 \qquad Y=T_{q_f}\setminus\{u_f\}.
\tag{4.4}
\]

Thus a frozen occurrence offers zero or one host edge for a flag.  Varying
\(B\) in (4.2) also varies \(T\), so it changes the owner history from
which \(C_{q_f}\) was computed.  Consequently (4.2) is a valid family only
inside a joint prospective factor model in which each edge carries its own
compatible history realization.

If those candidate-dependent histories are product-closed at the scheduled
positions, the lag apertures (4.3) together with a rainbow matching in
\((\mathcal G_f^{\rm typ})_f\) are sufficient.  They are not an
if-and-only-if criterion after the history is frozen.  The exact
frozen-history object is the occurrence-labelled matching of Section 7.
The fibre-one proof is recorded separately in
MATH_THEOREM_PBBS_FROZEN_OCCURRENCE_FIBRE_ONE_AND_PROSPECTIVE_HOST_QUANTIFIER_20260807.md.

If flags are not assigned to successor and lag slots in advance, combine
the flag, successor occurrence, lag occurrence, coatom, and owner into one
occurrence-labelled hyperedge.  A matching saturating the flag shore is
then the exact unfrozen criterion.  Separate Hall matchings for the two
slot shores are not sufficient unless their common phase/state choices
are product-closed.

## 5. A useful strong typing invariant

The prospective rainbow condition above may be certified pointwise in the
uncontracted ideal universe.
Define

\[
 q_*(m,d)=\min\left\{q:{q\choose d+1}
 \ge2{m\choose d+1}\right\}.
\tag{5.1}
\]

If every successor occurrence obeys

\[
 \boxed{
 |C_{q_f}\setminus U_f|\ge q_*(m,d),}
\tag{5.2}
\]

and every displayed exterior \(B\) has at least one filler
\(K\subseteq M_f\cap C_{q_f}\) whose actual source letter \(B\cup K\)
has the required phase/state type and is certified literal-safe for the
mandatory-core and positive-hit cuts, then
each colour has at least (2\Delta) edges.  Every nonempty colour
subfamily (X) therefore has matching number at least (2|X|), by
Kőnig's theorem, and satisfies (3.5).

This implication is formally correct but **vacuous for a frozen literal
successor occurrence**.  Indeed, (1.1)--(1.2) put \(C_{q_f}\) inside every
rank-\(m\) owner window containing \(q_f\), so \(|C_{q_f}|\le m\).  Hence

\[
 |C_{q_f}\setminus U_f|\le m,
 \qquad
 |\mathcal G_f^{\rm typ}|\le {m\choose d+1}=\Delta.
\tag{5.4}
\]

On the other hand \(q_*(m,d)>m\), because
\(\binom{q}{d+1}\) is strictly increasing in \(q\) and the defining
right side is twice its value at \(q=m\).  Thus (5.2) cannot hold for a
pre-existing literal envelope.  The complete-ideal degree argument is
useful only before the host and its physical occurrence are chosen jointly;
it is not a pointwise certificate for a frozen schedule.

At the optimal deadline,

\[
 q_*(m,d)=m+
 \left(\frac{4\log2}{\pi}+o(1)\right)d,
\tag{5.3}
\]

so the complete ideal exterior (m+d+2) is above the threshold.  This is a
sufficient criterion only in the uncontracted ideal host universe.  By
(5.4) it is unavailable on a frozen literal occurrence.  The exact usable
fixed-schedule invariant remains Theorem 4.1.

## 6. Consequence for the adaptive-phase programme

The following rows are now separated cleanly.

1. **Scalar endpoint supply:** proved; adaptive rephasing removes the
   theta reset deficit without extra positions.
2. **Abstract positional supply:** proved; upper, successor, and lag
   positions can be separated.
3. **Complete Boolean host supply:** proved asymptotically by (3.2)--(3.5).
4. **Literal occurrence typing:** open; the SCD start-rank ledger gives no
   information about (1.2), hence cannot establish Theorem 4.1.

Therefore the next all-(k) theorem is not another reset count.  It is an
owner-compatible construction which exposes, on the selected ordinary
reset occurrences, either:

\[
 \boxed{
 \text{the exact typed rainbow condition of Theorem 4.1,}}
\]

while preserving common history, residence, upper coverage, and the
terminal compiler.  The alternative is to choose flags, hosts, and
occurrences jointly in the unfrozen hypergraph; (5.2) is not a realizable
pointwise shortcut.

This note does not prove that occurrence-typing theorem, the adaptive
merged PBBS chart theorem, \(\nu(k)\le B(k)+O(1)\), or exact equality.
