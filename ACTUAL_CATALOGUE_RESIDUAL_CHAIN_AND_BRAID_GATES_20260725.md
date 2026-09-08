# Actual deterministic-catalogue residuals: chain expansion, donor strings, and braid path Hall

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

This note continues the tagged flagged-reserve chain-Hall audit, but now
uses the partial-matching process which is actually proved for the
deterministic gap-permutation catalogue.

There are four conclusions.

1. The present catalogue theory proves one owner-scale common-priority
   bite, not a near-complete common matching.  The residual after that one
   bite still has middle-layer width \(W-o(W)\), so it is not yet in the
   sparse-reserve regime.
2. The exact priority-deadline defect has useful vertical structure.  If
   \[
   \delta(P)=\max_{q\le Q}(B_q(P)-\bar d_q)_+,
   \]
   then deleting \(\delta(P)\) phase columns is necessary and sufficient
   for priority feasibility.  Each deleted phase is one complete nested
   flag chain, so the deleted claimed strings have chain width at most
   \(\delta(P)\).  In one rigorous owner-scale bite their total width is
   \(o(W/Q)\).
3. This does **not** bound the width of the actual complement hole set.
   The deleted strings are duplicate or withheld claims and are therefore
   a structured donor family.  The missing targets created by the lost
   distinct-claim count may be located anywhere else in the row.  A
   donor-to-hole transport theorem or a lower-uniformity theorem is still
   required.
4. Two exact positive gates are isolated:
   - a two-step cross-shadow matching condition which gives
     \(\operatorname{width}({\cal H})=o(W)\);
   - a rotor-successor Hall condition which groups the resulting hosted
     state-columns into \(O(B/Q)\) genuine chunks, where \(B\) is their
     number.

Together these give a precise strengthened residual condition under which
the flagged reserve closes at \(o(W)\) cost.  Neither condition follows
from the currently recorded PDRC recurrence, common-priority deadlines,
or separate-rank Hall.

## 1. What the actual partial-matching process proves

Use

\[
W=\binom{2m}{m},\qquad M=m+H,\qquad
N=\binom{2m}{M},\qquad MN=W-o(W).
\tag{1.1}
\]

The owner-scale theorem in
MATH_ATTACK_LADDER_PRIORITY_OWNER_SCALE_NIBBLE_20260725.md selects, in one
round,

\[
\Theta(N/M)
\tag{1.2}
\]

carrier trajectories whose owners and all nested claimed targets are
mutually disjoint.  The claim counts use the harmlessly lowered values
\(\bar c_q=M-\bar d_q\).

This matches only an \(O(1/M)\) fraction of the carrier tags.  The number
of middle owners covered is \(O(W/M)\), so the actual residual hole poset
after the proved bite contains

\[
W-O(W/M)=W-o(W)
\tag{1.3}
\]

middle sets.  These form an antichain.  Thus the one unconditional bite
has residual width \(W-o(W)\).

The later-round statement in that note is conditional on PDRC.  PDRC
controls weighted path degrees, pathwise deadline slack, and upper bounds
on normalized owner and target loads.  It contains no lower bound on how a
prescribed family of currently unused targets is hit.  Therefore even a
proof of PDRC iteration down to \(R=o(N)\) would not, as presently stated,
imply a cross-rank width bound for the complement holes.

## 2. The exact priority donor theorem

Fix one base path \(P\).  For each phase \(t\), let \(r(t)\) be its first
blocked depth, and put

\[
B_q(P)=\#\{t:r(t)\le q\}.
\tag{2.1}
\]

The allowed reverse-priority deadlines are \(\bar d_q=M-\bar c_q\).

### Proposition 2.1 (minimum deleted phase columns)

Put

\[
\boxed{
\delta(P)=\max_{q\le Q}(B_q(P)-\bar d_q)_+.}
\tag{2.2}
\]

Then \(\delta(P)\) is exactly the minimum number of whole phase columns
which must be removed so that the remaining phase jobs admit a legal
common priority order.

#### Proof

If \(s\) columns are removed, every prefix count can fall by at most \(s\).
The deadline Hall inequalities force

\[
s\ge B_q(P)-\bar d_q
\]

for every \(q\), proving the lower bound.

For the upper bound, remove the \(\delta(P)\) phases with smallest
first-block depths.  At every depth \(q\), the new prefix count is

\[
\max\{B_q(P)-\delta(P),0\}\le\bar d_q.
\]

The exact deadline Hall theorem supplies a legal priority. \(\square\)

On a return-free geodesic grid, the physical flags at phase \(t\) are

\[
L_q(t)=G_{t+q,t},\qquad U_q(t)=G_{t-q,t}.
\tag{2.3}
\]

The lower and upper strings concatenate through the owner:

\[
L_Q(t)\subset\cdots\subset L_1(t)\subset X_t
\subset U_1(t)\subset\cdots\subset U_Q(t).
\tag{2.4}
\]

### Corollary 2.2 (structured donor width)

For a family of paths, put

\[
D=\sum_P\delta(P).
\tag{2.5}
\]

The claims withheld by the minimum phase-column deletions have an
inclusion-chain cover, and hence antichain width, at most

\[
\boxed{D.}
\tag{2.6}
\]

For the rigorous owner-scale bite,

\[
\mathbb E D
\le
\mathbb E\sum_{P\ {\rm active}}B_Q(P)
=O\left(\frac{N\Lambda_Q}{M}\right)
=O\left(\frac{N\lambda_Q}{Q}\right)
=o(W/Q),
\tag{2.7}
\]

where

\[
\Lambda_Q=\Theta\left(\frac mQ\lambda_Q\right),
\qquad \lambda_Q=m^{o(1)}.
\tag{2.8}
\]

Hence some one-bite outcome has a withheld donor family of chain width
\(o(W/Q)\).

## 3. Why donor width is not hole width

The distinction is elementary but essential.

### Proposition 3.1 (support location is absent from the collision ledger)

Let \(V\) be one target row, let \(T\) be the total number of claimed
occurrences, and let \(D_{\rm row}\) be the number of lost distinct claims
caused by duplicates or priority withholding.  Knowing the complete
locations of the duplicated or withheld claims does not determine the
complement hole family.

More precisely, subject only to

\[
|{\cal H}|=|V|-T+D_{\rm row},
\tag{3.1}
\]

the hole family \({\cal H}\subseteq V\) may be prescribed independently
of the locations on which the \(D_{\rm row}\) excess occurrences are
stacked.

#### Proof

Choose any support \(C=V\setminus{\cal H}\) of the required cardinality.
Put one occurrence on every member of \(C\).  The remaining

\[
T-|C|=D_{\rm row}
\]

occurrences may be added, with repetition, on any prescribed members of
\(C\).  The duplicate locations and hole locations are disjoint and
otherwise independent. \(\square\)

Applied simultaneously to the protected rows, Proposition 3.1 says that
the nested family in Corollary 2.2 is a donor/counterterm family.  It is
not a positive cover of the actual missing targets.  In particular the
weighted-level antichain from
TAGGED_FLAGGED_RESERVE_CHAIN_HALL_AUDIT_20260725.md remains compatible
with the scalar row identities even when every duplicate donor string is
perfectly nested.

There are only two valid ways to exploit (2.6).

1. Prove an integral signed rotor transport which moves the donor strings
   onto the actual holes at total cell cost \(o(W)\).
2. Prove a lower-uniformity or cross-shadow theorem which directly controls
   the location and inclusion width of the complement holes.

Simply compiling the donor strings again covers targets which were already
covered and does not repair the complement.

## 4. A concrete cross-shadow condition forcing low width

Index the protected hole rows by

\[
{\cal H}_i\subseteq\binom{[2m]}{m+i},
\qquad -Q\le i\le Q.
\tag{4.1}
\]

For \(i\le-2\), let \(\varepsilon_i^-\) be the Hall deficiency of the
two-rank inclusion graph from \({\cal H}_i\) to \({\cal H}_{i+2}\):

\[
\varepsilon_i^-
=
\max_{{\cal A}\subseteq{\cal H}_i}
\left(
|{\cal A}|
-
|N_{{\cal H}_{i+2}}^+({\cal A})|
\right)_+.
\tag{4.2}
\]

For \(i\ge2\), let \(\varepsilon_i^+\) be the Hall deficiency of the
reverse inclusion graph which assigns every upper target to a contained
target two ranks closer to the middle:

\[
\varepsilon_i^+
=
\max_{{\cal A}\subseteq{\cal H}_i}
\left(
|{\cal A}|
-
|N_{{\cal H}_{i-2}}^-({\cal A})|
\right)_+.
\tag{4.3}
\]

### Theorem 4.1 (two-step shadow chain cover)

The residual hole poset has a chain cover of size at most

\[
\boxed{
h_{-1}+h_0+h_1
+
\sum_{i\le-2}\varepsilon_i^-
+
\sum_{i\ge2}\varepsilon_i^+.}
\tag{4.4}
\]

Consequently, if

\[
h_{-1}+h_0+h_1=o(W)
\tag{4.5}
\]

and

\[
\sum_{i\le-2}\varepsilon_i^-
+
\sum_{i\ge2}\varepsilon_i^+
=o(W),
\tag{4.6}
\]

then

\[
\boxed{\operatorname{width}({\cal H})=o(W).}
\tag{4.7}
\]

#### Proof

By deficient Hall, for every \(i\le-2\) there is an inclusion matching
from \({\cal H}_i\) into \({\cal H}_{i+2}\) which leaves at most
\(\varepsilon_i^-\) members of \({\cal H}_i\) unmatched.  Direct these
edges toward the middle.

For every \(i\ge2\), there is a matching assigning all but
\(\varepsilon_i^+\) members of \({\cal H}_i\) to distinct contained
members of \({\cal H}_{i-2}\).  Direct these edges away from the middle,
from the contained set to its containing set.

At every hole vertex there is at most one incoming and at most one outgoing
edge.  Strict inclusion prevents cycles.  The components are inclusion
chains.  Counting vertices minus selected edges gives (4.4): all
noncentral row sizes cancel, leaving only the three roots \(-1,0,1\) and
the matching deficiencies. \(\square\)

### Why a two-step condition is natural

Write

\[
\epsilon=R/N.
\tag{4.8}
\]

The exceptional row ledger has density of order \(\epsilon\) in every
shallow row.  If \(\epsilon\le1/m\), then

\[
RK_Q=O(\epsilon W\sqrt m)=o(W),
\tag{4.9}
\]

so literal repair already suffices.  In the only range where vertical
sharing is needed, \(\epsilon>1/m\), one target has
\(\Theta(m^2)\) two-rank supersets or subsets near the middle.  A
random-like residual would therefore have expected two-step residual
degree

\[
\Theta(\epsilon m^2)\ge\Theta(m).
\tag{4.10}
\]

This is the natural expansion scale for (4.2)--(4.3).  The statement is
only motivational: PDRC supplies neither the required lower degrees nor
the Hall cuts.

### Theorem 4.2 (the proved one-bite residual has small two-step deficiency)

Let \(t=O(N/M)\) be the number of trajectories selected by the rigorous
owner-scale bite, and let \({\cal C}_i\) be their distinct claimed targets
in row \(m+i\).  Put

\[
{\cal H}_i=\binom{[2m]}{m+i}\setminus{\cal C}_i.
\tag{4.11}
\]

Then

\[
\boxed{
\sum_{i\le-2}\varepsilon_i^-
+
\sum_{i\ge2}\varepsilon_i^+
\le 2(Q-1)Mt
=O(QN)=o(W).}
\tag{4.12}
\]

#### Proof

The complete two-rank inclusion graph from rank \(m+i\) to rank
\(m+i+2\), for \(i\le-2\), has a matching saturating the farther-from-the-
middle layer.  This follows from the normalized matching property of the
Boolean lattice.  Fix one such injection.

Restrict it to \({\cal H}_i\).  A lower hole fails to map into
\({\cal H}_{i+2}\) only when its fixed image lies in
\({\cal C}_{i+2}\).  Hence

\[
\varepsilon_i^-\le|{\cal C}_{i+2}|\le Mt.
\tag{4.13}
\]

The complementary argument on the upper side gives

\[
\varepsilon_i^+\le|{\cal C}_{i-2}|\le Mt.
\tag{4.14}
\]

There are \(Q-1\) indices on each side.  Summation proves the first
inequality in (4.12).  Since \(t=O(N/M)\), the sum is \(O(QN)\), and

\[
\frac{QN}{W}=O(Q/M)=o(1).
\]

\(\square\)

This is a theorem about the actual bite, not a random-residual heuristic.
It also shows why it does not yet close the reserve: the three central
hole rows in (4.4) still have total size \(\Theta(W)\) after only one
bite.

## 4.3 A catalogue-specific fractional overload criterion

There is another exact route to low width which uses the residual legal
path catalogue directly.

Suppose \(R\) carrier tags remain.  Let \(x_P\ge0\) be weights on legal
residual decorated trajectories such that

\[
\sum_{P\text{ above }U}x_P=1
\qquad(U\text{ an unmatched tag}).
\tag{4.15}
\]

Every claimed target of every path is required to lie in the current hole
family \({\cal H}\).  Define the fractional target load

\[
\ell(S)=\sum_{P:S\text{ is claimed by }P}x_P.
\tag{4.16}
\]

Put

\[
\Delta_-=\sum_{S\in{\cal H}}(1-\ell(S))_+,
\qquad
\Delta_+=\sum_{S\in{\cal H}}(\ell(S)-1)_+.
\tag{4.17}
\]

### Theorem 4.3 (fractional residual overload controls width)

For the actual common-priority trajectory catalogue,

\[
\boxed{
\operatorname{width}({\cal H})\le MR+\Delta_-.}
\tag{4.18}
\]

If every trajectory has the same claimed size

\[
K_Q=M+2\sum_{q=1}^Qc_q
\tag{4.19}
\]

and the designated residual hole count is

\[
|{\cal H}|=RK_Q+\delta_\Sigma,
\tag{4.20}
\]

then

\[
\boxed{\Delta_-=\delta_\Sigma+\Delta_+.}
\tag{4.21}
\]

Consequently

\[
\boxed{
\Delta_+=o(W)
\quad\Longrightarrow\quad
\operatorname{width}({\cal H})=o(W)}
\tag{4.22}
\]

whenever \(R=o(N)\).

#### Proof

The claims of one decorated trajectory are the union of its \(M\) phase
columns.  Each phase column is an inclusion chain.  Hence every antichain
\({\cal A}\subseteq{\cal H}\) meets the claims of one trajectory in at
most \(M\) targets.  Therefore

\[
\sum_{S\in{\cal A}}\ell(S)
=\sum_Px_P|P\cap{\cal A}|
\le M\sum_Px_P
=MR.
\tag{4.23}
\]

It follows that

\[
|{\cal A}|
\le
\sum_{S\in{\cal A}}\ell(S)
+
\sum_{S\in{\cal A}}(1-\ell(S))_+
\le MR+\Delta_-.
\]

Maximize over antichains to obtain (4.18).

Tag saturation and (4.19) give

\[
\sum_{S\in{\cal H}}\ell(S)=RK_Q.
\tag{4.24}
\]

Subtracting (4.24) from (4.20), and separating positive and negative
parts of \(1-\ell(S)\), gives (4.21).  Finally
\(\delta_\Sigma=o(W)\), \(RM=o(W)\), and (4.18)--(4.21) prove (4.22).
\(\square\)

Theorem 4.3 pinpoints the quantitative strengthening needed from PDRC.
An exact capacity-one residual fractional point, \(\ell(S)\le1\), gives
\(\Delta_+=0\) and closes the width gate immediately.  A pointwise estimate
\(\ell(S)\le1+\zeta_m\) is enough only when

\[
\zeta_m|{\cal H}|=o(W).
\tag{4.25}
\]

Since \(|{\cal H}|\) may be of order
\((R/N)W\sqrt m\), an unspecified \(1+o(1)\) target-load upper bound is
not sufficient.  The required rate is

\[
\zeta_m(R/N)\sqrt m=o(1).
\tag{4.26}
\]

In particular, the weighted-level obstruction from the abstract reserve
audit cannot occur as the whole residual of a capacity-one fractional
catalogue: its width is \(\Theta(W)\), whereas (4.18) would bound the width
by \(MR+o(W)\).  This is the exact sense in which an **actual**
capacity-controlled residual is stronger than the row ledger.  What is
missing is a proof that the iterative catalogue really retains such a
fractional point with the quantitative overload in (4.22).

## 5. Exact horizontal rotor path Hall

Theorem 4.1 produces inclusion chains.  Extending each chain to a saturated
protected flag segment gives a set \(\Omega\) of full rotor state-columns.
This vertical step does not ensure efficient concatenation.

Assign every \(\omega\in\Omega\) to a carrier containing it.  Give the
states an acyclic phase order, and form the directed graph \(D_\Omega\) in
which

\[
\omega\longrightarrow\omega'
\tag{5.1}
\]

when the two states have the same carrier, \(\omega'\) is one legal rotor
successor of \(\omega\), and the phase order increases.  Let \(B_\Omega\)
be the bipartite graph on left and right copies of \(\Omega\) induced by
(5.1).

### Theorem 5.1 (rotor path-cover Hall)

The minimum number \(p(\Omega)\) of directed rotor chunks whose state sets
partition \(\Omega\) is

\[
\boxed{
p(\Omega)
=|\Omega|-\nu(B_\Omega)
=
\max_{{\cal A}\subseteq\Omega}
\left(
|{\cal A}|-|N^+_\Omega({\cal A})|
\right),}
\tag{5.2}
\]

where \(\nu\) is maximum matching size.

#### Proof

A matching chooses at most one successor and at most one predecessor of
every state.  Acyclicity makes the selected components directed paths.
A matching of size \(\nu\) gives \(|\Omega|-\nu\) paths.  Conversely every
path cover with \(p\) paths uses \(|\Omega|-p\) successor edges and hence
gives a matching of that size.  The last equality is the deficiency form
of Hall's theorem. \(\square\)

Compiling a path cover has exact length

\[
|\Omega|+(2Q+1)p(\Omega).
\tag{5.3}
\]

Therefore, if

\[
|\Omega|=B=o(W)
\tag{5.4}
\]

and

\[
\boxed{p(\Omega)=O(B/Q)+o(W/Q),}
\tag{5.5}
\]

then the complete positive reserve costs \(o(W)\).

For \(B=O(RM)\), condition (5.5) asks for

\[
p(\Omega)=O(RM/Q)+o(W/Q),
\tag{5.6}
\]

the desired number of \(O(Q)\)-phase braid blocks.

Condition (5.5) is automatic if the chosen columns can be placed in legal
rotor segments of average length \(\Omega(Q)\).  This is the exact
phase-provenance condition that common priority would have to preserve.
Carrier hosting of each chain separately is not enough.

### Proposition 5.2 (vertical expansion does not imply rotor expansion)

There are saturated-chain covers with perfect vertical rank balance whose
rotor-successor graph is empty at every positive radius.  In particular,
the standard BTK/Greene--Kleitman symmetric chain decomposition has

\[
p_d=c_d
\tag{5.7}
\]

at every radius \(d\ge1\), where \(c_d\) is its number of radius-\(d\)
chains.

Thus even zero vertical Hall deficiency does not imply (5.5).  This is the
exact obstruction proved in
BTK_SCD_ROTOR_PATH_COVER_AUDIT_20260725.md.  It does not rule out a
different phase-compatible completion of the same hole chains, but it
shows that the horizontal Hall condition cannot be omitted or inferred
from Dilworth alone.

## 6. The sharpened positive reserve gate

### Theorem 6.1 (cross-shadow plus braid-Hall completion)

Suppose a partial deterministic-catalogue matching leaves \(R=o(N)\)
carrier tags and protected holes \({\cal H}\).  Assume:

1. after \(E_0=o(W)\) literal exceptions,
   \[
   h_{-1}+h_0+h_1
   +\sum_{i\le-2}\varepsilon_i^-
   +\sum_{i\ge2}\varepsilon_i^+
   =B=O(RM)+o(W);
   \tag{6.1}
   \]
2. the resulting chain cover extends to hosted rotor states
   \(\Omega\) with \(|\Omega|\le B\);
3. those states satisfy
   \[
   p(\Omega)=O(B/Q)+o(W/Q).
   \tag{6.2}
   \]

Then the protected residual has a positive literal completion of length

\[
O(B)+o(W)=o(W).
\tag{6.3}
\]

Consequently the calibrated primary word, outer reservoir, and tails give
coefficient one.

#### Proof

Theorem 4.1 gives at most \(B\) inclusion chains.  Extend them to
\(\Omega\).  Theorem 5.1 compiles that set at cost

\[
|\Omega|+(2Q+1)p(\Omega)=O(B)+o(W).
\]

Since \(R=o(N)\), \(RM=o(NM)=o(W)\), so \(B=o(W)\).  Add the
\(E_0=o(W)\) exceptions and the audited outer pieces. \(\square\)

Theorem 6.1 is stronger than separate-rank Hall but weaker than extending
the original common matching exactly.  Duplicate flags, skipped ranks
inside a chain, and \(o(W)\) literal exceptions are allowed.

## 7. What the actual process must add

The actual priority-ladder process controls:

- internal all-depth rainbowness of each selected trajectory;
- exact priority deadline feasibility;
- an owner-scale first bite;
- upper normalized loads under conditional PDRC;
- a vertically nested withheld donor family of width \(D\).

It does not control:

- lower inclusion degrees of the actual complement hole rows;
- the two-step Hall deficiencies (4.2)--(4.3);
- antichain width of the complement holes;
- phase provenance or rotor-successor deficiency (5.2);
- signed donor-to-hole transport.

A sufficient strengthened residual condition is:

> **PDRC plus cross-shadow plus braid.**  Iterate PDRC while also
> maintaining total two-step residual-shadow deficiency \(o(W)\); at a
> stopping time \(R=o(N)\), choose the deficient chain cover with
> phase-compatible completions whose rotor path-cover number is
> \(O(RM/Q)+o(W/Q)\).

No near-complete process with these properties is proved.

## 8. Actual obstruction status

There is currently no unconditional near-complete deterministic-catalogue
matching at \(R=o(N)\), so there is no actual residual at that scale from
which either low width or a catalogue-realizable weighted-antichain
counterexample can be deduced.

Two rigorous facts delimit the question.

1. The only unconditional actual bite has width \(W-o(W)\), by (1.3).
2. At the hypothetical sparse stopping scale, the row ledger and the
   target-load upper bounds do not exclude the weighted antichain cut of
   the preceding reserve audit.  Common priority constrains the selected
   edge and its donor strings, not the complement location.  It remains
   possible that the stronger weighted-degree flatness clause of PDRC,
   together with an additional argument not presently recorded, excludes
   that cut; no such implication is proved here.

Constructing an actual sparse residual containing that weighted antichain
would require a near-perfect common matching which systematically avoids
it.  Proving such a matching is itself comparable to the unresolved
common-matching theorem.  No such actual counterexample is claimed.

The positive target is now

\[
\boxed{
\text{small two-step shadow deficiency}
\quad+\quad
\text{small rotor-successor deficiency}.}
\tag{8.1}
\]

The first turns rowwise holes into \(O(RM)\) vertical chains.  The second
turns those chains into \(O(RM/Q)\) legal braid blocks.  Both must be
proved for the actual partial-matching residual.
