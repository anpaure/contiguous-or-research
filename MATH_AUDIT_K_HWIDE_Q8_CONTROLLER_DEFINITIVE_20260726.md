# Definitive adversarial audit of the \(H\)-wide \(Q_8\) carousel controller

Date: 2026-07-26

Method: pure mathematics only.

This note supersedes the earlier preliminary local audit wherever their
scopes differ.

Primary source:

\[
\texttt{MATH\_THEOREM\_HWIDE\_COMPILER\_CONTROLLER\_FOR\_Q8\_CAROUSEL\_20260726.md}.
\]

Compared against:

\[
\texttt{MATH\_ATTACK\_K\_Q8\_OWNER\_CAROUSEL\_CPM\_EMSF\_BOUNDARY\_20260726.md},
\]

\[
\texttt{MATH\_OBSTRUCTION\_Q8\_CAROUSEL\_LITERAL\_TURNAROUND\_SEAM\_20260726.md},
\]

and the literal compiler theorem cited by the source.

## 0. Verdict

The apparent \(H^2\) versus \(H\) conflict is not a contradiction.

The old \(H^2\) quarantine bound charged every window meeting an
undecoded seam.  The raw turnaround obstruction additionally exhibited
actual \(q\)-element fibres when an increasing and a decreasing payload
run were separated by only a bounded collar.  In the new word

\[
                         \Pi=B\Sigma A,\qquad
                         \Pi\Pi=B\Sigma A\,B\Sigma A,          \tag{0.1}
\]

the two opposite payload runs are separated by the entire controller word
\(AB\), of length \(2n=\Theta(H)\), and by the next \(Q_8\) direction.
No window of length \(q\le H\) reaches both payload sides.  The central
turnaround windows are genuine controller intervals and are decoded by the
proved compiler.  Thus the old raw fibre is absent.

The source theorem is nevertheless not correct verbatim.

1. The phrase “every turnaround window lies in \(AB\)” must be restricted
   to windows containing the central \(A|B\) cut.  Windows at
   \(\rho_7|A\) and \(B|w_0\) are mixed controller/core windows.
2. A meet or union cannot recover an unknown traversal orientation: an
   interval and its reversal have the same target.  Compiler injectivity
   holds separately for each fixed orientation, which is sufficient.
3. There are fourteen homogeneous two-payload \(Q_8\) seams, not sixteen.
   The two \(w_0\) occurrences have a controller collar.
4. Four frozen tag pairs were omitted from the ambient coordinate budget.
5. The inherited parity-indexed frame ledger needs even payload lengths,
   or an explicit phase reset.
6. The displayed local family is a sparse union of \(2D\)-owner cycles,
   not a full packet and not a near-spanning ambient factor.

After those corrections the local geometric theorem is valid.  In fact,
under the source theorem’s stated *full split-pair Johnson interface* and
its injective tagged \((C,Y)\)-registry, the local signed trace maps are
stronger than claimed:

\[
                  \boxed{E_q^-=E_q^+=0\qquad(1\le q\le H).}   \tag{0.2}
\]

Consequently the published

\[
 64HM={32H\over D}G                                      \tag{0.3}
\]

is a valid but vacuous local upper bound.  If one deliberately drops
support recovery on the core coordinates and retains only the controller
decoder, the exact interface census gives the corrected safe fallback

\[
 \sum_{q\le H}(E_q^-+E_q^+)
 \le32HM={16H\over D}G,                                 \tag{0.4}
\]

under the cross-macro separation hypotheses stated below.  Thus
same-oriented seams contribute \(O(1)\), not \(O(q)\), collision excess at
one depth.

Neither (0.2), (0.3), nor (0.4) proves coefficient one.  The fixed-atlas
family to which (0.2) applies has exponentially negligible owner mass.
Extending it to \(W-o(W)\) owners requires translated or incompatible
atlases, precisely where cross-macro target equality is uncontrolled.

## 1. Exact controller scale

Let \(n=4\cdot2^t\) be least with

\[
                         n\ge2(H+1),                         \tag{1.1}
\]

and put \(r=2n\).  Then

\[
 2(H+1)\le n<4(H+1),\qquad
 4(H+1)\le r<8(H+1).                                    \tag{1.2}
\]

The compiler factor is on \(Q_r\), with first-half word

\[
                         \kappa=BA,\qquad |A|=|B|=n.          \tag{1.3}
\]

Its proved literal split-pair range is

\[
                         \ell\le {n\over2}-1.                 \tag{1.4}
\]

Equation (1.1) gives \(H\le n/2-1\), including the endpoint \(q=H\).
The compiler therefore applies to every protected controller interval,
for each sign, each physical start phase, and each fixed traversal
orientation.

## 2. Exact turnaround statement

Consider one central cut

\[
                         A=(a_1,\ldots,a_n)\mid
                         B=(b_1,\ldots,b_n).                  \tag{2.1}
\]

A forward \(q\)-edge interval containing the cut vertex uses

\[
                         a\text{ edges of }A,\qquad
                         b\text{ edges of }B,\qquad a+b=q.    \tag{2.2}
\]

There are exactly \(q+1\) endpoint-inclusive intervals, corresponding to
\(a=0,\ldots,q\), and \(q-1\) proper straddlers with \(a,b\ge1\).
All lie in \(AB\) because \(q\le H<n\).  Since

\[
                         \kappa\kappa=BABA,                   \tag{2.3}
\]

they are ordinary consecutive controller intervals.  Restricting either
signed literal target to the controller pairs gives exactly the compiler
trace, so these intervals are injectively decoded.

The same proof holds at the other \(A|B\) cut and in the reverse
orientation, considered as its own fixed domain.

The source wording needs one correction.  The controller does not contain
every interval touching the *enlarged* payload turnaround.  The neighbouring
interfaces are

\[
                         \rho_7|A,\qquad B|w_0.                \tag{2.4}
\]

Those are mixed windows handled in Section 3.  What is true, and is exactly
what removes the old fibre, is:

\[
\boxed{\begin{gathered}
\text{every interval containing the central copy cut lies in }AB,\\
\text{no interval of length at most }H\text{ reaches both payload sides.}
\end{gathered}}                                             \tag{2.5}
\]

Indeed any interval reaching both sides must traverse all \(2n\)
controller edges and the intervening \(w_0\), hence has length at least
\(2n+1>H\).

## 3. Mixed controller/core decoding

Fix one traversal orientation.  A protected interval at \(B|\Sigma\) or
\(\Sigma|A\) containing \(d\ge1\) controller moves restricts on the
controller pairs to a literal trace of \(d\) consecutive controller
directions.  Repetition of the frozen controller state during the core
moves does not alter its intersection or union.

In the split-pair interface, the controller restriction has size

\[
                         r-d\quad\text{for the lower sign},\qquad
                         r+d\quad\text{for the upper sign}.   \tag{3.1}
\]

Thus \(d\) is visible.  Compiler injectivity recovers the controller
interval start and its factor cycle \(Y\).  It does not and need not recover
an unknown traversal orientation.  The frozen four-bit tag recovers the
\(Q_8\) base cycle \(C\).  With at most one macro registered for each
tagged pair \((C,Y)\), the macro and then the full start are unique.

A core-only interval has controller size \(r\) and cannot collide with a
mixed interval.  This supplies the cross-class separation omitted from the
source proof.

## 4. Exact interface census

One full macrocycle has:

1. two central \(A|B\) turnarounds;
2. four controller/core boundaries, \(B|\Sigma\) and \(\Sigma|A\) in
   each half;
3. fourteen homogeneous two-payload seams
   \(w_1,\ldots,w_7\), twice; and
4. two one-sided \(w_0\) occurrences at \(B|\Sigma\).

There are sixteen \(Q_8\) edges in total.  At depth \(q\le H\le L\), each
edge belongs to exactly \(q\) directed \(q\)-windows, and the seam collars
are disjoint.  Hence exactly

\[
                         16q                              \tag{4.1}
\]

directed windows meet a \(Q_8\) edge, and no protected window meets two
such edges.

At a homogeneous increasing seam, write

\[
                         a+b=q-1.                           \tag{4.2}
\]

In raw orientation-bit notation the left lower frontier and right upper
frontier are

\[
                         1^{L-a}0^a,\qquad
                         1^b0^{L-b}.                        \tag{4.3}
\]

Thus the lower sign determines \(a\), the upper sign determines \(b\), and
either sign determines the split because \(q\) is fixed.  Complementation
gives the decreasing case.  In the literal split-pair notation, the zeros
in the moved part of the lower frontier mean “no endpoint,” while the ones
in the moved part of the upper frontier mean “both endpoints”; the same
parameter recovery is even more explicit.

At each \(w_0\), exactly \(q-1\) of the \(q\) windows contain controller
moves and are decoded by Section 3.  The remaining one starts at \(w_0\).

Therefore the same-oriented seams are split-rainbow; the \(O(q)\)
quarantine count is not an \(O(q)\) collision count.

If support recovery is removed from the core, a conservative count allows
at most one adjacent nonseam collision per sign at each homogeneous seam,
and at most one per sign for each \(w_0\).  Hence

\[
                         E_q^-+E_q^+
 \le14\cdot2+2\cdot2=32.                              \tag{4.4}
\]

Summing and using \(G=2DM\) gives (0.4).  The source constant 64 is a
looser one-orientation estimate obtained from its unrefined
sixteen-seam, two-boundary-cases-per-sign count.  Reverse traversal does
not create a second EMSF target catalogue.

## 5. Strong split-pair trace theorem

We now prove (0.2), which is the exact conclusion under the source’s actual
all-split-pair implementation.

### Theorem 5.1 (fixed-atlas local trace injectivity)

Fix one common split-pair atlas.  Give the sixteen \(Q_8\) base cycles
distinct four-bit frozen tags.  Let the controller cycles be the cycles of
one certified compiler factor, and use at most one macro for every tagged
pair \((C,Y)\).  Then, for each fixed traversal orientation, each sign, and
every \(1\le q\le H\), the literal trace map on all starts of the declared
macro family is injective.

#### Proof

For a signed target \(T\), inspect every active split pair.

* An untouched pair contributes exactly one endpoint.
* A pair moved once contributes no endpoint to a lower target and both
  endpoints to an upper target.

Since \(q\le H<D\), no direction repeats in one protected interval.
Therefore \(T\) recovers the exact moved-direction set \(J\), and it
recovers the start orientations on \(J^c\).

The frozen tag recovers \(C\).  Put \(d=|J\cap R|\), where \(R\) is the
controller block.

If \(d=0\), the target contains one endpoint from every controller pair,
so it contains the complete controller owner.  The controller factor
partitions \(Q_r\); this owner determines its unique cycle \(Y\).

If \(d>0\), the controller moves form one consecutive interval of \(Y\).
They cannot be separated by the long core at length \(q\le H\), and the
central \(A|B\) case is consecutive by (2.3).  The controller restriction
is its certified \(d\)-trace, so the compiler theorem recovers \(Y\) and
the controller interval start.

The injective \((C,Y)\)-registry now determines the macro.

Inside that macro the direction word is \(\Pi\Pi\), with \(\Pi\) a
permutation of its \(D\) directions.  Two cyclic \(q\)-intervals with the
same support have starts congruent modulo \(D\).  The only second occurrence
is the antipodal start \(D\) steps later.  Its orientations on every pair
of \(J^c\) are complementary.  Because \(q<D\), the set \(J^c\) is
nonempty, and the literal target distinguishes the antipodal occurrences.
Thus the starts agree. \(\square\)

This theorem includes turnaround, mixed, homogeneous-seam, \(w_0\), and
payload-internal intervals.  There is no inherited payload collision in
this fixed registered family.  The number 64 is consequently safe but
nonsharp:

\[
                         E_q^-=E_q^+=0.                     \tag{5.1}
\]

This zero statement does not survive an unproved change of atlas or a
registry which reuses \((C,Y)\) with independent payload contexts.

## 6. Isometry and exact owner support

The first-half word is

\[
                         \Pi=B\Sigma A,                      \tag{6.1}
\]

and contains exactly once:

* all \(r\) controller directions;
* all eight \(Q_8\) directions; and
* all \(8L\) payload directions.

The blocks are disjoint, so \(\Pi\) is a permutation of

\[
                         D=r+8+8L                            \tag{6.2}
\]

directions.  Hence \(\Pi\Pi\) is a simple isometric \(C_{2D}\).
Under the split-pair realization it is literally a cyclic \(D\)-strip in
the middle Johnson layer.

Distinct macros whose \(Q_8\) cycles or controller cycles are disjoint
have disjoint owner supports.  Their union is an exact factor of that
declared support.  This proves local compilation, not a factor of the full
\(Q_D\) packet.

## 7. Correct ambient coordinate and parity budget

The active blocks use \(D\) split pairs.  The four frozen tags use four
additional split pairs.  Thus literal embedding in
\(\binom{[2m]}m\) requires

\[
                         D+4\le m.                          \tag{7.1}
\]

The source choice

\[
                         L=\left\lfloor{m-r-8\over8}\right\rfloor
\]

ensures only \(D\le m\) and can violate (7.1).

To reserve the tags and inherit the parity-indexed frame ledger without a
separate reset, take

\[
                         L=
 2\left\lfloor{m-r-12\over16}\right\rfloor.            \tag{7.2}
\]

Writing \(m-r-12=16t+s\), \(0\le s\le15\), gives

\[
                         D=m-4-s,\qquad
                         m-19\le D\le m-4.             \tag{7.3}
\]

Hence \(L\) is even, \(D+4\le m\), \(L\sim m/8\),
\(D\sim m\), and \(H\le L\) for all sufficiently large \(m\) whenever
\(H=o(m)\).

Raw doubled-permutation isometry does not require even \(L\).  Evenness is
needed only for the inherited parity-indexed \(Q_8\) frame ledger; an
explicit phase reset would be an alternative.

Thus \(D=\Theta(m)\) is compatible with disjoint active coordinates, tags,
middle rank, and strict EMSF half-length \(D<m\), after the \(O(1)\)
correction (7.2).

## 8. How much owner mass is actually supplied?

The local theorem supplies at most one macro for each \(Q_8\) cycle and
controller cycle.  There are sixteen \(Q_8\) cycles and

\[
                         {2^r\over2r}
\]

controller cycles.  Hence

\[
 M\le16{2^r\over2r}={8\,2^r\over r},\qquad
 G=2DM\le {16D\,2^r\over r}.                         \tag{8.1}
\]

Since \(r=O(H)=o(m)\),

\[
                         G=2^{o(m)},                         \tag{8.2}
\]

whereas

\[
                         W=\binom{2m}m=2^{2m-o(m)}.           \tag{8.3}
\]

Thus the exact family to which Theorem 5.1 applies has exponentially
vanishing owner density.

Even allowing every middle owner in one fixed split-pair chart gives at
most

\[
 2^{D+4}
 \binom{2m-2D-8}{m-D-4}
 =2^{m+O(1)}=o(W)                                     \tag{8.4}
\]

at root scale \(D=m-O(1)\).  A near-spanning construction must use many
translated completions or different pair atlases.  The common support
decoder and frozen tags do not by themselves separate targets across those
copies.

Accordingly the sentence “an outer packing on \(G=W-o(W)\) would have the
same seam bound” is conditional on a substantial new cross-copy theorem;
it is not a consequence of the local controller construction.

## 9. Global geometric compilation

The named local theorem proves only a factor of its declared sparse union.
There is, however, a separate algebraic packet completion available when
\(D=2^s\): for any permutation word \(\Pi\), a syndrome map

\[
 \phi:\mathbb F_2^D\longrightarrow\mathbb F_2^{s+1}
\]

can be chosen so that the \(2D\) prefixes of \(\Pi\Pi\) have all distinct
syndromes.  Translates by \(\ker\phi\) then give

\[
                         Q_D=
 \dot\bigcup_{k\in\ker\phi}(C_\Pi+k),\qquad
 |\ker\phi|={2^D\over2D}.                              \tag{9.1}
\]

Thus the cycles are geometrically compilable into a full \(Q_D\) factor,
but this is an additional syndrome theorem, not proved in the named local
source.  The power-of-two choice is not generally simultaneous with the
root formula \(D=m-4-s\) in (7.3); one must choose a different
\(\Theta(m)\) power-of-two scale, as in the separate global theorem, or
restrict the ambient subsequence.  Conjugating the entire template by each
endpoint-swap translation preserves owner equations and raw isometry.

Two qualifications remain.

1. If equal payload blocks force odd \(L\), the inherited phase ledger still
   needs a reset.  One exact repair is to choose eight even payload lengths
   with the same total: take a common even baseline and add two directions
   to four blocks.  All lengths remain \(\Theta(D)\), every collar remains
   longer than \(H\), and \(\Pi\) is still a permutation.
2. The syndrome translates use conjugated controller/payload contexts.
   The fixed-registry proof of \(E=0\) does not compare targets from
   different translates.  The global owner factor therefore does not imply
   the EMSF target-hole condition.

Any further claim that rank-twisted \(Q_D\) packets cover \(W-o(W)\) owners
belongs to the separate global-packing theorem and is not established by
the local controller theorem audited here.

## 10. Corrected theorem

### Theorem 10.1 (verified \(H\)-wide local controller)

Let \(n,r,H,L,D\) satisfy (1.1)--(1.4), \(H\le L\), and let all active
directions use disjoint physical split pairs.  Reserve four further split
pairs for the base-cycle tags.  Fix one traversal orientation, tag the
sixteen \(Q_8\) cycles distinctly, and register at most one macro for each
pair \((C,Y)\).

Then:

1. every word \(\Pi\Pi\) is a literal isometric \(C_{2D}\);
2. the declared macros are owner-disjoint and factor their declared union;
3. every lower and upper trace map is injective through every
   \(1\le q\le H\);
4. the two central turnarounds, four mixed boundaries, fourteen homogeneous
   seams, and two \(w_0\) occurrences contribute exactly zero local
   collision excess; and
5. with the root-scale choice (7.2), all coordinates fit and
   \(m-19\le D\le m-4\).

If the core is instead read through a raw interface without support
recovery, items 3--4 are replaced by the safe bound

\[
 \sum_{q\le H}(E_q^-+E_q^+)
 \le32HM={16H\over D}G.                               \tag{10.1}
\]

No near-spanning owner packing, cross-atlas target estimate, CPM option, or
EMSF target-hole theorem follows from Theorem 10.1.

## 11. Exact implication boundary

The verified conclusions are:

* \(AB\) decodes every interval containing either central copy cut through
  \(q=H\);
* no protected interval reaches both oppositely oriented payload runs;
* same-oriented \(Q_8\) seams are split-rainbow, not \(q\)-to-one;
* \(D=\Theta(m)\) and exact isometry are compatible after reserving tags and
  correcting parity; and
* full \(Q_D\) geometric factorization is possible only after invoking the
  separate syndrome completion.

Scoped only to the named local theorem, the unproved gate includes both
owner completion and target coverage.  If the separate syndrome and
rank-twisted owner-packing theorems are invoked, the owner part is supplied
and the remaining gate is the second line below:

\[
\boxed{\begin{gathered}
\text{pack or complete these macros on }W-o(W)\text{ owners (if not supplied separately), and}\\
\text{prove }o(W)\text{ total target overlap across the resulting}\\
\text{translated/conjugated atlases simultaneously for all }q\le H.
\end{gathered}}                                             \tag{11.1}
\]

This is a grouped cross-macro target problem, not a remaining local
\(H^2\) turnaround problem.
