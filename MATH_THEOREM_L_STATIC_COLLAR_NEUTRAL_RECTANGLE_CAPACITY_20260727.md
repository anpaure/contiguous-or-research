# Static collar-neutral rectangle banks have only \(O(H)\) capacity per top

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
 \qquad N=\binom{2m}{M},\qquad W=\binom{2m}{m},
\tag{0.1}
\]

and assume \(H\ge3\), \(d\ge2H+3\), \(H=o(m)\), and the calibrated
common-core relation

\[
                         MN=(1+o(1))W.
\tag{0.2}
\]

The two-top construction in
`MATH_THEOREM_NONCLOSED_BOUNDARY_RECTANGLE_LIFT_AND_DENSE_RECYCLING_GATE_20260727.md`
realizes a standard hypersimplex rectangle by one middle unit transfer
at each of two tops, while its aggregate trace derivative vanishes at
every nonmiddle protected length. The remaining question was whether
many such rectangles could be installed on the same tops as independent
literal toggles.

They cannot occur at the required density.

> **Static installation-capacity theorem.** Consider a bank of \(R\)
> collar-neutral hypersimplex-rectangle toggles. Suppose that
>
> 1. every one of the \(2^R\) toggle shores is represented by exactly
>    one literal length-\(d\) tight path at every top;
> 2. every toggle has two fixed middle-nonneutral incident tops and acts
>    at each by one fixed middle unit transfer (middle-neutral helper
>    changes are allowed);
> 3. the local middle effects of the toggles add on every Boolean shore;
>    and
> 4. the aggregate trace at every protected nonmiddle length is the same
>    on all Boolean shores.
>
> If \(r_U\) is the number of toggles incident with a top \(U\), then
>
> \[
>                         \boxed{r_U\le2H+2.}
> \tag{0.3}
> \]
>
> Consequently
>
> \[
>             \boxed{R\le(H+1)N,\qquad
>             \sum_U r_U\le(2H+2)N=o(W).}
> \tag{0.4}
> \]

Thus a common-core top does not have

\[
                         \Theta(m)
\]

independently composable collar-neutral rectangle slots. Its conformal
Boolean installation capacity is at most \(2H+2=O(H)=o(m)\). This is
not an abstract rank statement: it uses the nonnegativity of every
literal Boolean shore.

The explicit master-order state requires \((1-o(1))W\) middle unit
transfers before it can reach any load of collision energy \(o(W)\).
Even applying every toggle in a static bank once supplies only
\(O(HN)=o(W)\) local unit transfers. Hence a static independent bank,
including one with perfect aggregate cancellation of every nonmiddle
trace, cannot close the master-order gate.

What remains possible is genuinely **state-dependent sequential
recycling**: after using some rectangles, change the local path charts,
expose new endpoint-band owners, and install new rectangles. The theorem
does not bound the cumulative number of transfers along such a
reinstalled trajectory. It rules out precisely the hoped-for
\(\Theta(m)\)-dimensional static Boolean bank per top.

## 1. Literal decks and the relevant notion of capacity

For an injective word

\[
                     \pi=(\pi_1,\ldots,\pi_{d+H-1})
\tag{1.1}
\]

on a fixed top \(U\), write

\[
 J_i(\pi)=\{\pi_i,\ldots,\pi_{i+H-1}\},\qquad
 \mathcal B_U(\pi)=\sum_{i=1}^d e_{U\setminus J_i(\pi)}.
\tag{1.2}
\]

The middle owners in (1.2) are distinct. A **local middle unit edge**
from \(\pi\) to \(\pi'\) means

\[
              \mathcal B_U(\pi')-\mathcal B_U(\pi)
                         =e_Y-e_X
\tag{1.3}
\]

for two distinct \(m\)-set owners \(X,Y\subset U\).

We make the independent-composability condition explicit. A static
rectangle bank is indexed by \([R]\). For every \(S\subseteq[R]\) and
every top \(U\), it supplies one path \(\pi_U(S)\). Toggle \(j\) has two
fixed middle-nonneutral incident tops. It may also change helper paths
whose middle decks stay fixed. For an incident pair \((U,j)\), there is
a fixed unit vector

\[
                         z_{Uj}=e_{Y_{Uj}}-e_{X_{Uj}}
\tag{1.4}
\]

such that

\[
 \mathcal B_U(\pi_U(S))
 =\mathcal B_U(\pi_U(\varnothing))
   +\sum_{j\in S:\,j\sim U}z_{Uj}
 \qquad(S\subseteq[R]).
\tag{1.5}
\]

At the two incident tops, the two vectors in (1.4) sum to the standard
four-term rectangle

\[
 e_{R_0\cup\{a,z\}}+e_{R_0\cup\{b,z'\}}
 -e_{R_0\cup\{a,z'\}}-e_{R_0\cup\{b,z\}}.
\tag{1.6}
\]

The all-depth collar condition is

\[
 \sum_U\mathcal D_h(U,\pi_U(S))
 \quad\hbox{is independent of \(S\) for every protected \(h\ne H\)}.
\tag{1.7}
\]

Condition (1.5), rather than ordinary linear independence in the signed
catalogue, is the physical content of an installed independent bank.
It says that any subset of the advertised toggles can actually be
selected while retaining one path per top. A state-dependent protocol
whose support or local action changes after earlier toggles is not a
static Boolean bank and is intentionally outside the definition.

## 2. Chronology confines every local source to \(2H+2\) phases

Define the endpoint band

\[
 I_{\partial}
 =\{1,\ldots,H+1\}\cup\{d-H,\ldots,d\}.
\tag{2.1}
\]

The two intervals are disjoint under \(d\ge2H+3\), and therefore

\[
                            |I_{\partial}|=2H+2.
\tag{2.2}
\]

### Lemma 2.1 (local unit-edge chronology)

If two literal paths on the same top satisfy (1.3), then the removed
owner \(X\) occurs in the initial path at a phase \(i\in I_{\partial}\).

#### Proof

Complementation inside the fixed top turns (1.3) into two \(H\)-window
decks with symmetric difference two. For one injective word, the graph
on its windows in which two windows are adjacent when their intersection
has size \(H-1\) is intrinsically the path \(P_d\): two windows have
intersection size

\[
                         \max\{0,H-|i-j|\}.
\tag{2.3}
\]

After deleting the one noncommon window from each deck, the two common
subpaths align, up to one global reversal. If the missing phase is
\(i\), the two components have sizes \(i-1\) and \(d-i\); when both are
nonempty, the two endpoints facing the gap are intrinsically identified
as the cross-component pair of largest intersection, namely \(H-2\).
Thus, after the possible reversal, the common windows have the same
index \(j\ne i\) in both words.

For every transition \(t\notin\{i-1,i\}\), consecutive common windows
recover both the leaving and entering letters:

\[
 \{\pi_t\}=J_t\setminus J_{t+1},\qquad
 \{\pi_{t+H}\}=J_{t+1}\setminus J_t.
\tag{2.4}
\]

If \(H+2\le i\le d-H-1\), these identities determine even the four
positions not fixed directly beside the gap. They are recovered from
the transitions

\[
 \begin{array}{c|c}
 \text{position}&\text{recovering transition}\\ \hline
 i-1&i-H-1\ \text{(entering)},\\
 i&i-H\ \text{(entering)},\\
 i+H-1&i+H-1\ \text{(leaving)},\\
 i+H&i+H\ \text{(leaving)}.
 \end{array}
\tag{2.5}
\]

All four transitions lie in
\(\{1,\ldots,d-1\}\setminus\{i-1,i\}\).
The two words are then identical, including their allegedly different
\(i\)-th windows, a contradiction. Hence \(i\in I_{\partial}\).
\(\square\)

This is the one-top content of
\`MATH_THEOREM_BOUNDARY_SWAP_CLOSED_CATALYST_CHRONOLOGY_OBSTRUCTION_20260727.md\`;
no restoration assumption is needed here because (1.3) already states
the complete endpoint difference on the fixed top.

## 3. Conformal Boolean directions must have different sources

The second ingredient is elementary but decisive. It is the point at
which signed lattice generation ceases to be relevant.

### Lemma 3.1 (source injection)

Let \(B\) be a \(0\)-\(1\) vector and let

\[
                         z_j=e_{Y_j}-e_{X_j}
\tag{3.1}
\]

be nonzero unit transfers. Suppose

\[
                         B+\sum_{j\in S}z_j\ge0
\tag{3.2}
\]

coordinatewise for every subset \(S\). Then the sources \(X_j\) are
pairwise distinct.

#### Proof

For the singleton shore \(S=\{j\}\), the source \(X_j\) has coefficient
one in \(B\), and \(Y_j\ne X_j\). If \(X_j=X_k=X\) for \(j\ne k\), then
on the two-toggle shore \(S=\{j,k\}\) the coefficient of \(X\) is

\[
                             1-1-1=-1,
\]

because neither target equals its own common source. This contradicts
(3.2). \(\square\)

The argument still works if targets and sources of *different* toggles
form chains or cycles. The only forbidden coincidence needed below is
two negative units charged to the same base occurrence.

## 4. Proof of the installation-capacity theorem

Fix a top \(U\), and put

\[
                         B_U=\mathcal B_U(\pi_U(\varnothing)).
\tag{4.1}
\]

For every incident toggle \(j\), compare the empty shore with the
singleton shore \(\{j\}\). Equation (1.5) gives the unit edge

\[
 \mathcal B_U(\pi_U(\{j\}))-B_U
                         =e_{Y_{Uj}}-e_{X_{Uj}}.
\tag{4.2}
\]

Lemma 2.1 assigns its source \(X_{Uj}\) to a phase in
\(I_{\partial}\). Equation (1.5) on all subset shores and the literal
nonnegativity of those decks let us apply Lemma 3.1. Thus distinct
incident toggles have distinct source owners. Since the base path has
exactly one owner at every phase, the map

\[
        j\longmapsto X_{Uj}\longmapsto
        \text{its phase in }I_{\partial}
\tag{4.3}
\]

is injective. Equations (2.2) and (4.3) prove

\[
                             r_U\le2H+2.
\tag{4.4}
\]

Every rectangle has two incident tops, so double counting gives

\[
                  2R=\sum_Ur_U\le(2H+2)N,
\tag{4.5}
\]

which proves the first assertion in (0.4). Finally, (0.2) and \(H=o(m)\)
give

\[
 { (2H+2)N\over W}
 ={2H+2\over M}(1+o(1))=o(1).
\tag{4.6}
\]

This proves the theorem. Notice that the nonmiddle cancellation
condition (1.7) was not used. The upper bound therefore remains valid
even if an ideal collar router supplies exact aggregate cancellation
for free.

## 5. Consequence for the master-order state

Let \(K\) be the master-order middle load from
`MATH_THEOREM_PSI_TWO_BASE_EXCHANGE_FLATNESS_AND_ISOLATED_HIGH_STATE_20260727.md`.
The support estimate audited in the nonclosed-rectangle note says that
for every nonnegative integer load \(L\) of the same total mass with

\[
                         \Psi(L)=o(W),
\tag{5.1}
\]

one has

\[
                         {1\over2}\|K-L\|_1=(1-o(1))W.
\tag{5.2}
\]

A local unit edge moves one unit of middle mass and changes the load in
\(L^1\) by two. Thus any boundary-swap route from \(K\) to \(L\) needs
\((1-o(1))W\) local unit edges. A static bank contains only

\[
                   \sum_Ur_U\le(2H+2)N=o(W)
\tag{5.3}
\]

such installed local actions, even before compatibility with the
current master-order shore is imposed. Therefore it cannot reach (5.1).

Equivalently, the required average local-action capacity is

\[
                         \Theta(W/N)=\Theta(m)
\tag{5.4}
\]

per top, while static literal composability supplies at most \(O(H)\).
At the tuned height this loses the factor

\[
                         \Theta(m/H)\to\infty.
\tag{5.5}
\]

## 6. Independent audit of the decisive step

The decisive implication is

\[
 \text{literal Boolean composability}
 \quad\Longrightarrow\quad
 \text{at most one toggle per endpoint-band source occurrence}.
\tag{6.1}
\]

Here is a second audit which does not use the rectangle-lattice
generation argument or any nonmiddle trace identity.

First check the signs of the literal two-top rectangle. With the notation
of (1.6), its two local derivatives are

\[
 e_{R_0\cup\{b,z'\}}-e_{R_0\cup\{a,z'\}},
 \qquad
 e_{R_0\cup\{a,z\}}-e_{R_0\cup\{b,z\}}.
\tag{6.2}
\]

Their sum is exactly (1.6), and each has one negative source occurrence.
Thus counting local unit edges, rather than four-term signed lattice
vectors, is the correct incidence ledger.

Fix \(U\) and expose only the empty shore, all singleton shores, and all
two-toggle shores. From a singleton shore, the negative coordinate of
the local difference identifies an actual owner occurrence in the empty
shore. The one-window chronology proof places that occurrence in
\(I_{\partial}\). If two singleton shores select the same occurrence,
then the corresponding two-toggle shore deletes that one occurrence
twice. No target term can repair the coefficient: for either singleton
difference its target is distinct from its own source, and the two
sources have been assumed equal. The two-toggle middle vector therefore
has coefficient \(-1\) at that owner and cannot be the deck of a literal
path. Hence the singleton-to-source map is injective, and its codomain
has exactly \(2H+2\) members.

This audit also checks four possible loopholes.

1. **Opposite rectangle orientations.** Reorienting a bit merely
   interchanges which endpoint shore is called empty; it still has one
   negative source on the chosen empty shore.
2. **Source-target chains.** A target of one toggle may equal the source
   of another. That does not permit two toggles with the same source and
   does not affect the injection used in (6.1).
3. **Aggregate collar cancellation.** Cancellation between different
   tops changes no coefficient in the one-top middle deck, so it cannot
   repair the negative local coefficient.
4. **Unordered deck or word reversal.** Lemma 2.1 recovers the intrinsic
   window path from intersections and already quotients by global
   reversal; no chosen indexing is being smuggled into the phase count.

Only a state-dependent escape remains: after applying a toggle, abandon
the fixed Boolean chart and use the new path as the base of a newly
installed bank. That is sequential recycling, not an omitted shore of
the static bank.

## 7. Exact boundary

Proved:

1. a per-top conformal Boolean capacity bound \(r_U\le2H+2\) for fixed
   two-top unit-transfer rectangle toggles;
2. a global bound \(R\le(H+1)N\) on independently composable
   collar-neutral hypersimplex rectangles;
3. the stronger fact that at most \(o(W)\) local middle unit actions are
   available in any such bank, even if all nonmiddle trace cancellation
   is granted; and
4. failure of every static independent rectangle bank to bridge the
   master-order distance to a load with \(\Psi=o(W)\).

Not proved:

1. the exact maximum below the upper bound \(2H+2\);
2. a sequential top-reuse bound after the local chart is reinstalled;
3. impossibility of a state-dependent open catalyst flow which exposes
   fresh endpoint owners after each batch;
4. a lower bound for general macros whose local action is not a fixed
   unit transfer on two fixed tops; or
5. coefficient one.

The installation gate is therefore no longer a question of finding
\(\Theta(m)\) simultaneous independent toggles per top: chronology and
conformal nonnegativity rule that out. The remaining positive route must
be an adaptive dense-recycling theorem rather than a static
hypersimplex-rectangle bank.
