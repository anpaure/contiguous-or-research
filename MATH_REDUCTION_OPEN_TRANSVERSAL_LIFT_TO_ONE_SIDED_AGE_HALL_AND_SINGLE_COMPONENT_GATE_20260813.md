# Opening the transversal lift reduces resident completion to one age-Hall gate

**Date:** 2026-08-13  
**Status:** unconditional exact reduction.  One incidence cut is the minimum needed
to let the saturated transversal component join the complement.  After that cut, one
parity is a protected perfect matching which always extends globally; the other parity
is one forced successor path.  Positive-`q`-resident completion is then equivalent to
one explicit capped-age Hall system.  This note does not prove that Hall system.

## 1. The incidence lift and its unique cut ticket

Use the notation of
`MATH_THEOREM_PAIR_CELL_TRANSVERSAL_LIFT_EXTENDS_TO_EXACT_OWNER_LOWER_FACTOR_20260813.md`.
Put

\[
                         e=2^{r-1}.
\]

Index the long-run lifted owner cycle so that

\[
                         D_{t-1}\cap D_t=L_t
                    \qquad(t\in\mathbb Z_e).              \tag{1.1}
\]

Its alternating incidence cycle is

\[
 L_0,D_0,L_1,D_1,\ldots,L_{e-1},D_{e-1},L_0.             \tag{1.2}
\]

Delete the single incidence \(L_0D_{e-1}\).  The result is the alternating path

\[
 \mathcal P^-:quad
 L_0,D_0,L_1,D_1,\ldots,L_{e-1},D_{e-1}.                 \tag{1.3}
\]

Every internal vertex of \(\mathcal P^-\) still has protected degree two.  Its only
degree-one vertices are the lower colour \(L_0\) and owner \(D_{e-1}\).

### Proposition 1.1 (exact deficit)

In any spanning incidence two-factor containing \(\mathcal P^-\), exactly one new
incidence must enter \(L_0\), and exactly one new incidence must enter
\(D_{e-1}\).  Every other protected lower and owner vertex is saturated.

After completion no lower colour is omitted: \(L_0\) is still used twice, but its
second endpoint is transported from \(D_{e-1}\) to an exterior owner.  Thus the cut
creates one unassigned **incidence ticket**, not one missing lower colour.

If the two exposed vertices are joined by one alternating path through every exterior
lower and owner vertex, its union with \(\mathcal P^-\) is one spanning incidence
cycle.  More generally, an arbitrary completion may leave exterior cycles.

#### Proof

This is the degree ledger of (1.3).  Both shores of the exterior have equal size
\(W-e\); after including the two degree-one protected endpoints, their residual degree
sums are equal.  Alternating closure gives the component statements.  \(\square\)

Keeping the whole incidence cycle instead would saturate every one of its vertices and
make it a closed component of every extension.  Hence at least one incidence cut is
necessary for fusion, and Proposition 1.1 shows that one is topologically sufficient.

## 2. Canonical parity split

Colour one parity of (1.3) by

\[
                         F_0=\{L_tD_t:0\le t<e\}.          \tag{2.1}
\]

This is a perfect matching from the protected lower set
\(Z=\{L_t\}\) to the protected owner set \(Y=\{D_t\}\).  The other protected
incidences are

\[
                         F_1^-=
 \{L_tD_{t-1}:1\le t<e\}.                                \tag{2.2}
\]

Orient the eventual owner factor so that its first incidence matching maps

\[
                         M_0(D_t)=L_t.                     \tag{2.3}
\]

Then (2.2) is precisely the forced successor path

\[
 Q:quad D_{e-1}\longrightarrow D_{e-2}longrightarrow
       \cdots\longrightarrow D_0.                         \tag{2.4}
\]

It has tail and head sets

\[
 Z_Q=Y-\{D_0\},\qquad H_Q=Y-\{D_{e-1}\}.                 \tag{2.5}
\]

Thus \(D_{e-1}\) is the unique protected owner needing an exterior predecessor and
\(D_0\) the unique protected owner needing an exterior successor.

### Proposition 2.1 (the first phase always extends)

For all sufficiently large \(r\), \(F_0\) extends to a perfect incidence matching
\(M_0\) of the whole middle-levels graph.

Moreover, given any base perfect matching \(H_0\), one may choose \(M_0\supseteq F_0\)
with

\[
                         |M_0\triangle H_0|
                          =r^{O(1)}2^r=o(W).                \tag{2.6}
\]

#### Proof

The endpoint sets of \(F_0\) are exactly \(Z,Y\), so the exposure bounds of the
transversal-lift theorem give both all-occurrence exposures at most two.  The protected
matching theorem gives existence.  The one-matching relative insertion theorem in
`MATH_THEOREM_EXPOSURE_TWO_EXPONENTIAL_MATCHING_INSERTION_HAS_SUBMIDDLE_DAMAGE_20260813.md`
gives (2.6).  This uses only its valid single-matching theorem, not the independent
two-colour corollary.  \(\square\)

## 3. Positive residence is the source-relevant condition

Put \(q=d+1\).  For an oriented owner chronology, give each present coordinate its
positive age, capped at \(q\).  A transition may delete only a coordinate of capped
age \(q\); an inserted coordinate receives age one; every persistent coordinate has
its age increased by one and capped at \(q\).

This one-sided condition is exactly equivalent to every finite positive owner run
having length at least \(q\).  It is also exactly what the nonempty maximal depth-\(d\)
antecedent needs to reconstruct all owner windows.  No zero-gap floor is needed for
that inversion.  If a later interface requires full biresidence, the signed two-sided
collar condition must be added separately.

The lifted cycle is `q`-biresident whenever the underlying cube transition directions
have separation at least \(q+1\).  Cutting it preserves every internal run.  It exports
only clipped age requirements at the entrance \(D_{e-1}\) and exit \(D_0\).

## 4. Exact age-Hall completion

Fix any global extension \(M_0\supseteq F_0\).  For an owner \(T\), write

\[
                         M_0(T)=T-\{x_T\}.                  \tag{4.1}
\]

Fix a capped positive-age assignment \(a_T(z)\in[q]\) for every \(z\in T\).
On the protected owners it must equal the deterministic ages along (2.4), with the
chosen clipped entrance ages, so that every arc of \(Q\) obeys the age recurrence.

Define the directed bipartite successor graph \(D^+_{M_0,a}\) on tail and head copies
of the owner layer.  Retain

\[
 T\longrightarrow T_y=T-\{x_T\}+\{y\},\qquad y\notin T,  \tag{4.2}
\]

exactly when

\[
 a_T(x_T)=q,qquad a_{T_y}(y)=1,                           \tag{4.3}
\]

and

\[
 a_{T_y}(z)=\min\{q,a_T(z)+1\}
                  \qquad(z\in T\cap T_y).                 \tag{4.4}
\]

### Theorem 4.1 (exact chronological gate)

For the fixed pair \((M_0,a)\), there is a simple spanning owner/lower factor
containing \(\mathcal P^-\), having first incidence phase \(M_0\), and having every
positive coordinate run of length at least \(q\), if and only if

\[
 Q\subseteq D^+_{M_0,a}                                  \tag{4.5}
\]

and

\[
 \boxed{
 |N_{D^+_{M_0,a}}(S)-H_Q|\ge |S|
       \quad(S\subseteq\mathcal O-Z_Q).}                  \tag{4.6}
\]

When these conditions hold, the completion is integral.  It has one global owner
component exactly when the selected successor permutation is a single directed cycle;
equivalently, add the standard subtour inequalities to the matching system.

#### Proof

This is Hall's theorem after deleting the forced tails and heads (2.5).  Every selected
successor uses the lower colour \(M_0(T)\), so the first and successor incidence
matchings are edge-disjoint and together use every lower and owner vertex twice.
Equations (4.3)--(4.4) make each inserted coordinate start at age one, each persistent
coordinate age deterministically, and each deletion occur only at age \(q\).  Hence
every finite positive run is long enough.  Conversely any such oriented factor records
an age assignment satisfying (4.3)--(4.4), and deleting its forced path gives the
residual perfect matching required by (4.6).  The component assertion is the usual
successor-permutation characterization.  \(\square\)

## 5. What ordinary protected Ore does not prove

The protected-Ore extension theorem for the closed lift proves incidence feasibility,
but it cannot imply (4.6): it has no age variables and no ordered transition history.
Applied after the single cut, it may simply restore the deleted incidence
\(L_0D_{e-1}\), reclosing the lift as its original saturated component.  Even a
completion forbidden from restoring that edge need not respect the capped-age
recurrence or be connected.

Therefore the precise next theorem is

\[
 \boxed{
 \text{choose }M_0\supseteq F_0\text{ and a compatible age state }a
 \text{ for which (4.6) holds, with bounded subtour defect}.}
\]

The first-phase matching is already solved by Proposition 2.1.  The unresolved content
is entirely the joint age-Hall/chronology row, not owner/lower incidence saturation.
