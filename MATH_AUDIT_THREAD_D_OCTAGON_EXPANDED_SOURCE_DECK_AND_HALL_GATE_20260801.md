# Full expanded octagon decks: exact phase difference and the surviving Hall gate

Date: 2026-08-01  
Lane: Thread D, terminal octagon compiler audit  
Status: exact all-`d` interval-deck classification for `d>=2`, with a
separate finite replay through `d=12`.  This note scopes, but does not alter,
the typed two-boundary `+2` theorem.

## 0. Verdict

Let `Q^0,Q^1` be the sharp source inverses of the resident quaternary
octagon, and split the two exterior hosts as in
`MATH_THEOREM_THREAD_D_OCTAGON_SPLIT_BOUNDARY_RESET_20260801.md`.  Denote the
expanded words by `Qhat^0,Qhat^1` and their ordinary consecutive-interval OR
decks by `D_0,D_1`.

The decks are not equal.  For every `d>=2`,

\[
 |D_0\setminus D_1|=4d+1,
 \qquad
 |D_1\setminus D_0|=6d-3.                         \tag{0.1}
\]

Thus the observed sequence

\[
 (9,9),(13,15),(17,21),\ldots,(41,57)
\]

at `d=2,3,4,...,10` is exact, not a census artefact.  The depth-one sharp
inverse is exceptional and gives `(7,7)`.

The two host splits create seven new **set values** in each phase, but only
three of the seven are phase-exclusive.  The other phase-exclusive values
were already native in the unsplit sharp packet.  More precisely,

\[
\begin{array}{c|cc}
 &\text{old-native exclusive}&\text{split-new exclusive}\\ \hline
 \epsilon=0&4d-2&3\\
 \epsilon=1&6d-6&3.
\end{array}                                             \tag{0.2}
\]

The advertised `Pi/Sigma` repair is different: those four typed boundary
tasks use three set values which already occur in **both** old interval
decks.  Splitting creates their required boundary occurrences, not new
untyped masks.  Consequently the native-return argument really does reset
the two typed boundary tasks, but it does not reset the complete source
deck.

The remaining compiler condition is an occurrence-labelled protected-witness
Hall condition.  Every phase-exclusive local witness used by the terminal
compiler must either have a surviving common/exterior alternate witness or
belong to a jointly saturable reserve bank.  Equation (0.1) is not by itself
a compiler deficiency lower bound, because any of these masks may be
irrelevant or redundantly witnessed elsewhere.

## 1. Exact phase-only families

Write the filler bank as

\[
 F=\{f_0,f_1,\ldots,f_{d+1}\},
 \qquad
 F_{i:j}=\{f_i,f_{i+1},\ldots,f_j\}.
\]

Put

\[
\begin{aligned}
 \mathcal P={}&\{F_{1:t}:1\le t\le d-1\},\\
 \mathcal G={}&\{F_{t:d}:2\le t\le d\}\\
 &{}\cup\{F_{t:d+1}:3\le t\le d\}\\
 &{}\cup\{\{f_0\}\cup F_{t:d+1}:3\le t\le d\},\\
 \mathcal H={}&\{F_{2:t}:3\le t\le d+1\}\\
 &{}\cup\{F_{1:t}:3\le t\le d+1\}.
                                                               \tag{1.1}
\end{aligned}
\]

Then

\[
 |\mathcal P|=d-1,
 \qquad |\mathcal G|=3d-5,
 \qquad |\mathcal H|=2d-2.                    \tag{1.2}
\]

Here and below an active signature in the left column is to be unioned with
every filler set in the right column.  The exact phase-zero-only deck is:

\[
\begin{array}{c|c|c}
\text{active signature}&\text{filler family}&\text{number}\\ \hline
 \{z,a_1\}&\mathcal P&d-1\\
 \{z,a_3\}&\mathcal G&3d-5\\
 \{a_3\}&\{F_{0:1},F_{0:2}\}&2\\
 \{a_1\}&\{F_{2:d+1},F_{1:d+1}\}&2\\
 \{a_1,a_2,a_3\}&\{F\setminus\{f_0\},F\}&2\\
 \{a_0,a_2,a_3\}&\{F\setminus\{f_{d+1}\}\}&1.
                                                        \tag{1.3}
\end{array}
\]

The exact phase-one-only deck is:

\[
\begin{array}{c|c|c}
\text{active signature}&\text{filler family}&\text{number}\\ \hline
 \{z,a_1\}&\mathcal G&3d-5\\
 \{z,a_3\}&\mathcal P&d-1\\
 \{a_1\}&\{F_{0:1},F_{0:2}\}&2\\
 \{a_3\}&\mathcal H&2d-2\\
 \{a_0,a_1,a_3\}&\{F\setminus\{f_{d+1}\},F\}&2\\
 \{a_0,a_2,a_3\}&\{F\setminus\{f_0\}\}&1.
                                                        \tag{1.4}
\end{array}
\]

All rows in each table are disjoint because their active signatures are
different.  Summing (1.3) and (1.4) gives (0.1).  The total deck sizes are,
also exactly,

\[
 |D_0|={11d^2+59d+108\over2},
 \qquad
 |D_1|={11d^2+63d+100\over2}.                \tag{1.5}
\]

### Proof of the classification

In the sharp inverse, the filler projection is phase-independent at every
position.  Only the active projection changes, and it changes at the eight
affine positions displayed in the literal-octagon theorem.  Partition the
two interval endpoints by those eight positions and by the coatom-block
boundaries.  Inside one endpoint rectangle the active union is constant,
while the filler union changes monotonically with the two endpoint offsets.

For the two signatures containing `z`, the noncommon endpoint rectangles
give respectively the single initial ray `P` and the three terminal rays
`G`; phase reversal exchanges the two active labels.  Intervals ending in
the two screen collars give the two constant `a_3` and `a_1` rows in
(1.3).  Reversing the same endpoint rectangles gives the two initial rays
`H` in the phase-one `a_3` row.  The only endpoint rectangles meeting an
exterior split have full filler bank or omit exactly `f_0` or `f_(d+1)`;
these are the last two rows of each table.  All remaining endpoint
rectangles have the same active and filler union in both phases.

This exhausts the endpoint partition and proves (1.3)--(1.4).  Counting all
common rectangles as well gives (1.5).  The accompanying audit constructs
the literal words and checks the displayed families set-for-set, rather than
checking only their cardinalities.  \(\square\)

## 2. What the two split rays do and do not repair

Let `Qbar^epsilon` be the old word with the two exterior hosts left unsplit,
and define

\[
 S_\epsilon=\mathcal D(Qhat^\epsilon)
                 \setminus\mathcal D(Qbar^\epsilon).
\]

Direct block algebra gives

\[
 |S_0|=|S_1|=7.                                      \tag{2.1}
\]

Exactly three members of each `S_epsilon` are phase-exclusive.  They are

\[
\begin{aligned}
 J_0={}&\{
 \{a_0,a_2,a_3\}\cup(F\setminus\{f_{d+1}\}),
 \{a_1,a_2,a_3\}\cup(F\setminus\{f_0\}),
 \{a_1,a_2,a_3\}\cup F\},\\
 J_1={}&\{
 \{a_0,a_1,a_3\}\cup(F\setminus\{f_{d+1}\}),
 \{a_0,a_2,a_3\}\cup(F\setminus\{f_0\}),
 \{a_0,a_1,a_3\}\cup F\}.
                                                        \tag{2.2}
\end{aligned}
\]

Deleting the last two rows of (1.3) or (1.4), as appropriate, leaves the
old-native banks of sizes `4d-2` and `6d-6`.  Hence (0.2) is an exact
disjoint decomposition.

In contrast, the typed packet values `Pi_0,Pi_1,Sigma_0,Sigma_1` are in both
old untyped decks.  Their split-ray occurrences therefore do not appear in
(2.2).  This is why the two statements

* “the two typed boundary tasks reset after native phase return”, and
* “the full expanded interval deck resets”,

are not equivalent.  The first is the proved `Phi<=2` statement.  The
second is false locally: every member of `D_epsilon\D_(1-epsilon)` is absent
from both the opposite unsplit packet deck and its split-ray additions.

The linear banks are nevertheless highly structured.  Apart from a
constant number of masks, they are the nested rays `P,G,H`, so a future
exterior host theorem may exploit a constant-width convex/laminar graph.
There is currently no such physical host theorem.

## 3. Exact remaining compiler gate

The right object is an occurrence graph, not the set census (0.1).
Fix a terminal phase `epsilon` and an inherited compiler matching.  Delete
the local interval occurrences which disappear on changing to phase
`1-epsilon`.  Let `B_epsilon` be the matched hard rows thereby exposed after
removing rows which already have a protected common witness.  Let
`C_epsilon` be the still-free exterior or common-lift cells, filtered by all
of the actual requirements:

* owner and deadline legality;
* trace and residence-frontier guards;
* the prescribed common cap;
* noncollision with the unaffected inherited matching; and
* matching-safe contraction of both split hosts.

Join a row to a cell precisely when that cell is a literal admissible
replacement occurrence.  Then the lost rows can be transported with no
terminal deficiency if and only if

\[
 |N(X)|\ge |X|
 \qquad\text{for every }X\subseteq B_\epsilon.          \tag{3.1}
\]

This is just Hall, but (1.3)--(1.4) identify the complete local bank on
which it must be checked.  If the same cell assignment must survive both
phases, use the intersection of the two phase-admissibility graphs before
applying (3.1).  If phase-dependent assignments are allowed, apply (3.1)
separately in the two phases.  Soft lower rows contribute the usual exact
matching deficiency after all hard typed rows are saturated.

Thus the smallest unresolved statement is:

> **Protected occurrence reserve.**  After reserving the inherited
> matching, the phase-only rows actually used from (1.3)--(1.4) admit a
> saturating matching into phase-common/exterior cells, compatibly with the
> two split-host contractions.

Without this reserve theorem, the typed `Phi=2` reset cannot be promoted to
a complete common-compiler reset.  Conversely, (3.1) plus the already
proved two-boundary reset is sufficient locally.  No claim is made that all
`4d+1` or `6d-3` masks become hard rows in a global compiler.

## 4. Audit

Run

```text
PYTHONPATH=scratch python3 \
  scratch/audit_threadD_octagon_expanded_source_deck_difference_20260801.py
```

The replay checks `d=1,...,12`; for every `d>=2` it verifies (1.3) and
(1.4) as exact sets, the deck-size formulas (1.5), the `7=4+3` split ledger,
and the absence of opposite-phase local witnesses.  It records the
depth-one exceptional counts separately.  The frozen output is

```text
scratch/threadD_octagon_expanded_source_deck_difference_20260801.audit.json
```

Dependencies:

* `MATH_THEOREM_THREAD_D_QUATERNARY_OCTAGON_COATOM_PATH_COMMONCAP_20260801.md`;
* `MATH_THEOREM_THREAD_D_OCTAGON_SPLIT_BOUNDARY_RESET_20260801.md`;
* `scratch/audit_threadD_octagon_split_boundary_reset_20260801.py`.

