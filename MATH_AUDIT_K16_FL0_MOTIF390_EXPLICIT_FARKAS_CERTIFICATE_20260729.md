# K16 FL0 motif 390: explicit solver-free Farkas certificate

Date: 2026-07-29

## 1. Statement and normalization

Fix the detector-zero endpoint $Q$ and resident endpoint $R$ from the
guarded motif-390 core.  For a blue edge in $Q\setminus R$, let $b_i\ge 0$
denote its deletion variable; for a red edge in $R\setminus Q$, let
$r_j\ge 0$ denote its insertion variable.  The actual model makes these
variables Boolean, but the proof below uses only nonnegativity.

At a middle vertex $v$, orient the hard degree equation as

\[
 D_v:\qquad \sum_{j:v\in r_j}r_j-\sum_{i:v\in b_i}b_i=0.
\]

Every guarded palette row used below has base load one.  Orient it as either

\[
 b_i-r_j\le 0
\]

when a red replacement provider exists, or as $b_i\le0$ when none exists.
Put

\[
 a=b_{11795},\qquad x=r_{11806}.
\]

Here $a$ deletes the internal motif edge $(57902,57998)$, and $x$ adds
$(57902,61990)$.

**Theorem.**  The seventeen guarded palette rows in the forced-$a$ core,
together with only eight hard degree equations, imply

\[
 b_{11795}+r_{10793}+r_{12168}+r_{9710}+r_{9960}
 +r_{8352}+r_{5685}\le0.                              \tag{F}
\]

Consequently $b_{11795}=0$ in every nonnegative real solution.  Thus the
branch $b_{11795}=1$ is already infeasible in the LP relaxation; no Boolean
integrality, parity argument, or case split is needed.

## 2. Tail block (T)

At vertex (61990), add

\[
\begin{aligned}
D_{61990}:&\quad r_{9710}+x-b_{9796}-b_{12319}=0,\\
U_{62118}:&\quad b_{9796}\le0,\\
L_{61988}:&\quad b_{12319}-r_{12345}\le0.
\end{aligned}
\]

The result is

\[
 r_{9710}+x-r_{12345}\le0.                              \tag{T1}
\]

At vertex (64036), add

\[
\begin{aligned}
D_{64036}:&\quad r_{10025}+r_{12345}-b_{12455}-b_{12456}=0,\\
U_{65060}:&\quad b_{12456}\le0,\\
U_{64044}:&\quad b_{12455}-r_{9993}\le0,
\end{aligned}
\]

obtaining

\[
 r_{10025}+r_{12345}-r_{9993}\le0.                     \tag{T2}
\]

At vertex (47660), add

\[
\begin{aligned}
D_{47660}:&\quad r_{9960}+r_{9993}-b_{10030}-b_{10117}=0,\\
U_{47676}:&\quad b_{10030}-r_{9991}\le0,\\
L_{47652}:&\quad b_{10117}-r_{10025}\le0,
\end{aligned}
\]

obtaining

\[
 r_{9960}+r_{9993}-r_{9991}-r_{10025}\le0.             \tag{T3}
\]

At vertex (47644), add

\[
\begin{aligned}
D_{47644}:&\quad r_{8352}+r_{9991}-b_{3328}-b_{9749}=0,\\
U_{47772}:&\quad b_{3328}\le0,\\
U_{47645}:&\quad b_{9749}\le0,
\end{aligned}
\]

obtaining

\[
 r_{8352}+r_{9991}\le0.                                \tag{T4}
\]

Adding (T1)--(T4) cancels
$r_{12345},r_{9993},r_{9991},r_{10025}$ and gives the exact tail facet

\[
 \boxed{x+r_{9710}+r_{9960}+r_{8352}\le0.}              \tag{T}
\]

This linear implication cycle is why ordinary unit propagation can stop at
a fixpoint even though the branch is infeasible.

## 3. Middle block (M)

At vertex (59942), add

\[
\begin{aligned}
D_{59942}:&\quad r_{10798}+r_{12168}-b_{11579}-b_{11827}=0,\\
U_{64038}:&\quad b_{11579}\le0,\\
L_{57894}:&\quad b_{11827}-x\le0,
\end{aligned}
\]

to get

\[
 r_{10798}+r_{12168}-x\le0.                             \tag{M1}
\]

At vertex (59918), add

\[
\begin{aligned}
L_{57870}:&\quad a-r_{11797}\le0,\\
D_{59918}:&\quad r_{10793}+r_{11797}-b_{12126}-b_{12127}=0,\\
U_{59950}:&\quad b_{12126}-r_{10798}\le0,\\
L_{59406}:&\quad b_{12127}-r_{12057}\le0,
\end{aligned}
\]

to get

\[
 a+r_{10793}-r_{10798}-r_{12057}\le0.                  \tag{M2}
\]

Adding (M1) and (M2) cancels $r_{10798}$:

\[
 \boxed{a+r_{10793}+r_{12168}-x-r_{12057}\le0.}         \tag{M}
\]

## 4. End block (E)

At vertex (59422), add

\[
\begin{aligned}
D_{59422}:&\quad r_{10650}+r_{12057}-b_{10718}-b_{12037}=0,\\
L_{51230}:&\quad b_{10718}-r_{10650}\le0,\\
U_{59486}:&\quad b_{12037}-r_{5686}\le0,
\end{aligned}
\]

to get

\[
 r_{12057}-r_{5686}\le0.                               \tag{E1}
\]

At vertex (26718), add

\[
\begin{aligned}
D_{26718}:&\quad r_{5685}+r_{5686}-b_{4006}-b_{5891}=0,\\
L_{18526}:&\quad b_{4006}\le0,\\
U_{27742}:&\quad b_{5891}\le0,
\end{aligned}
\]

to get

\[
 r_{5685}+r_{5686}\le0.                                \tag{E2}
\]

Adding (E1) and (E2) cancels $r_{5686}$:

\[
 \boxed{r_{12057}+r_{5685}\le0.}                       \tag{E}
\]

## 5. Final cancellation and exact support

Adding (T), (M), and (E) cancels $x$ and $r_{12057}$ and gives (F).
All seven terms in (F) are nonnegative, so each is zero and in particular
$b_{11795}=0$.

The palette rows used are exactly

\[
\begin{aligned}
L:&\quad 18526,47652,51230,57870,57894,59406,61988,\\
U:&\quad 27742,47645,47676,47772,59486,59950,62118,
64038,64044,65060.
\end{aligned}
\]

The only degree sockets used are

\[
47644,61990,64036,47660,59918,59942,26718,59422.
\]

Their union contains 33 signed variable edges on 40 physical vertices,
including the branch edge $b_{11795}$.  The forced-branch artifact records
that these seventeen palette assumptions are deletion-minimal relative to
the full hard degree system: deleting any one gives `OPTIMAL`, with no
`UNKNOWN` replay.  That is a solver-backed assumption-minimality statement;
the displayed Farkas sum itself is solver-free.  No global minimality claim
is made for the eight degree sockets or the 33-edge physical support.

## 6. The other two motif branches

The same tail block immediately gives the incoming-boundary branch.  Row

\[
U_{61998}:\quad b_{11796}-x\le0
\]

together with (T) implies $b_{11796}=0$.

The outgoing-boundary branch is even shorter.  Adding

\[
\begin{aligned}
U_{58254}:&\quad b_{11821}-r_{10338}\le0,\\
D_{58126}:&\quad r_{10338}+r_{11867}-b_{9815}-b_{11849}=0,\\
U_{62222}:&\quad b_{9815}-r_{11867}\le0,\\
L_{57614}:&\quad b_{11849}\le0
\end{aligned}
\]

gives $b_{11821}\le0$.  Hence all three motif-390 deletion variables are
zero in the LP relaxation, contradicting

\[
b_{11795}+b_{11796}+b_{11821}\ge1.
\]

Thus the full 22-row guarded core also has a literal linear Farkas
certificate.

## 7. Catalogue-expansion boundary

For the internal-edge branch, an enlarged catalogue invalidates this exact
certificate only if it changes at least one of the seventeen normalized
palette inequalities or adds eligible incidence to at least one of the eight
degree sockets above.  This is a necessary proof-escape condition, not a
sufficient physical repair: every new provider must still belong to a
degree-balanced alternating circulation and preserve every other palette
and residence requirement.

## 8. Frozen provenance

```text
guarded 22-row core
2f8031fff879faf42b80a169aee2f0a0f5a2484987c5fe625c20fc5bf945c238
scratch/k16_failedlit0_guarded_q1_motif_core_20260729.json

forced b11795 branch core
ab08cc116e5aa284f0c2cce34ceb3d9bc2ebfcca0208025317d40241752677a5
scratch/k16_failedlit0_b11795_q1_core_20260729.json

detector-zero endpoint
17bd05a0bb0da228e580d65bdec27ce04589072baecb8575e0623fc4ea4343b8
scratch/k16_q1_endpoint_resume1_failedlit0_20260729.json

resident endpoint
d28491b708d5a83e8abcde20fda8ad523cd58f9c662f46ae2d9c2507ba73e951
scratch/k16_pbbs_oriented_noaa_softq1_resume1_20260729.json
```
