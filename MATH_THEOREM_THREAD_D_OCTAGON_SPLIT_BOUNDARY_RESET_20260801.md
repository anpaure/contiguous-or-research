# Two exterior split letters close the octagon boundary signature

Date: 2026-08-01  
Lane: Thread D / H2, octagon terminal boundary repair  
Status: exact source-word OR and typed-boundary theorem.  The two exterior
hosts are explicit, but their ambient owner, deadline, prescribed-cap and
full protected-bank cross-phase matching admissibility remain hypotheses.

**Full-deck scope correction.**  “Preserves every old interval” below means
that each phase embeds its own unsplit intervals by full-block lifting.  It
does not mean that the two expanded phase decks are equal.  Their exact sharp
directed differences are `4d+1` and `6d-3`; see
`MATH_THEOREM_THREAD_D_OCTAGON_FULL_SOURCE_DECK_AND_COMPILER_GATE_20260801.md`.
Thus this note proves the two typed boundary tasks and its conditional reset,
not contextual transparency of the complete source block.

## 0. Result

The resident quaternary-octagon tensor has four typed endpoint occurrences:
one phase-exclusive prefix and one phase-exclusive suffix value in each
phase.  As **untyped masks**, all four values already occur in both source
interval decks.  What is missing is their occurrence at the correct packet
boundary.  This distinction is decisive.

No refinement of any number of tensor-internal source letters can create
the missing typed prefix or suffix.  The obstruction is the order of first
and last active-label occurrences and survives arbitrary replacement blocks,
not only binary splits.

There is nevertheless an exact constant repair using two old exterior host
letters

\[
                         X_L=\{a_0,a_1\},
             \qquad      X_R=\{a_1,a_2\}.                \tag{0.1}
\]

Split and orient them as

\[
\begin{array}{c|cc}
 &X_L\text{ (far,near)}&X_R\text{ (near,far)}\\ \hline
 \epsilon=0&(a_0,a_1)&(a_2,a_1)\\
 \epsilon=1&(a_1,a_0)&(a_1,a_2).
\end{array}                                               \tag{0.2}
\]

The packet-near halves create exactly the missing prefix and suffix typed
occurrences.  Refinement adds two source positions, preserves every old
interval OR by full-block lifting, and uses the same two host caps in both
phases.

Moreover the two marked boundaries admit a local full reset.  On phase
reversal, the two targets previously supplied by side cells become native
packet-boundary occurrences.  Contract both old splits and reverse their
orientations to supply the two newly missing targets.  Subject to physical
boundary-owner/deadline/common-cap legality, matching-safe contraction, and
one simultaneous post-phase-replacement matching for the entire protected
occurrence bank, the construction carries exactly two marked boundaries and
therefore has

\[
                              \Phi\le2                     \tag{0.3}
\]

at every terminal phase; it does not accumulate.  Without those physical
and matching hypotheses, including cross-phase transport, the split-letter
theorem gives only
`Phi'<=Phi+2`.

## 1. Exact tensor boundary data

Let `T^epsilon` be the owner path of the resident octagon tensor, let
`Q^epsilon` be either its maximal depth-`d` inverse or the sharp thinned
inverse, and put

\[
                         N=|Q^\epsilon|=9d+23.            \tag{1.1}
\]

Write the filler bank as `F` and retain any fixed core `K`.  The four typed
owner-path boundary values are

\[
\begin{aligned}
 \Pi_0&=K\cup F\cup\{z,a_0,a_2,a_3\},&
 \Pi_1&=K\cup F\cup\{z,a_1,a_2,a_3\},\\
 \Sigma_0&=K\cup F\cup\{z,a_0,a_1,a_3\},&
 \Sigma_1&=\Pi_0.                                      \tag{1.2}
\end{aligned}
\]

Phase `epsilon` has native typed occurrences `Pi_epsilon` on the left and
`Sigma_epsilon` on the right; it lacks the opposite typed pair.  These are
statements about the **owner-word boundary profile**.  They must not be
confused with ordinary membership in the source-word interval deck.

The source words have two phase-common literal interval unions

\[
\begin{aligned}
 R_L&=\bigcup_{p=0}^{2d+3}Q_p^\epsilon
     =K\cup F\cup\{z,a_2,a_3\},\\
 R_R&=\bigcup_{p=7d+19}^{9d+22}Q_p^\epsilon
     =K\cup F\cup\{z,a_0,a_3\}.                        \tag{1.3}
\end{aligned}
\]

Equation (1.3) is a literal **source-interval** identity in both phases.
It is the bridge from the owner boundary signature to split-letter side
cells.

## 2. Why internal refinements cannot work

Each mask in (1.2) has rank `r+3`, whereas every literal letter in an exact
depth-`d` source is contained in a rank-`r` owner and therefore has rank at
most `r`.  Thus none of the four typed debts is singleton-hosted by an
internal source letter.  The stronger obstruction below also excludes every
multi-piece endpoint-ray refinement of those letters.

Both maximal and sharp-thinned inverse words have the exact occurrence
orders

\[
\begin{array}{c|cc}
 &\min a_0&\min a_1\\ \hline
 Q^0&3d+5&4d+9\\
 Q^1&4d+9&3d+5
\end{array}
\qquad
\begin{array}{c|cc}
 &\max a_1&\max a_2\\ \hline
 Q^0&6d+17&5d+13\\
 Q^1&5d+13&6d+17.
\end{array}                                               \tag{2.1}
\]

### Theorem 2.1 (arbitrary internal block-refinement no-go)

Replace any family of tensor-internal source letters by arbitrary consecutive
nonempty blocks having the same unions.  Then:

* phase zero has no refined packet prefix with value `Pi_1`;
* phase one has no refined packet prefix with value `Pi_0`;
* phase zero has no refined packet suffix with value `Sigma_1`; and
* phase one has no refined packet suffix with value `Sigma_0`.

This holds for every number and arity of internal refinements.

#### Proof

A refined prefix contains every old block before its final old position in
full.  In phase zero, the first source block containing `a_0` precedes the
first block containing `a_1`.  Hence every refined prefix containing the
required `a_1` already contains forbidden `a_0`, so it cannot equal
`Pi_1`.  The phase-one argument is the swapped first-occurrence row of
(2.1).

Dually, a refined suffix contains every old block after its first old
position in full.  In phase zero the last `a_1` block lies after the last
`a_2` block, so every suffix containing required `a_2` also contains
forbidden `a_1`; it cannot equal `Sigma_1`.  The phase-one row is again
the swap.  \(\square\)

All four set values nevertheless occur as ordinary internal source
intervals in both phases.  Thus an untyped target census reports no defect;
only the typed boundary audit detects Theorem 2.1.

## 3. Two exterior binary splits

Start from the unsplit extended source word

\[
                         X_L\mid Q^\epsilon\mid X_R.      \tag{3.1}
\]

Use the phase-oriented replacements (0.2).  Every piece is nonempty and
each two-piece block has the original union in (0.1).

### Theorem 3.1 (exact two-side-cell repair)

In phase `epsilon`, the two packet-near side cells have values

\[
\begin{aligned}
 \{a_{1-\epsilon}\}\cup
       \bigcup_{p=0}^{2d+3}Q_p^\epsilon
     &=\Pi_{1-\epsilon},\\
 \bigcup_{p=7d+19}^{9d+22}Q_p^\epsilon
       \cup\{a_{2-\epsilon}\}
     &=\Sigma_{1-\epsilon}.                            \tag{3.2}
\end{aligned}
\]

Thus both missing typed occurrences are supplied.  Every old source
interval has a distinct full-block lift with exactly the same OR.  The
refinement charge is exactly two positions relative to (3.1), and the two
terminal phases have equal length.

One common cap family supports both orientations: use `X_L` at both
expanded left positions, `X_R` at both expanded right positions, and the
existing packet common caps internally.

#### Proof

Substitute (1.3) into (3.2).  For phase zero the near labels are `a_1` and
`a_2`, giving `Pi_1,Sigma_1`; for phase one they are `a_0` and `a_1`, giving
`Pi_0,Sigma_0`.  Simultaneous block contraction preserves every old OR and
is injective on old intervals.  The length and cap statements follow
directly from the two binary blocks.  \(\square\)

The two old host letters in (0.1) are assumptions about the exterior source
word.  If they must themselves be planted, the charge relative to the bare
tensor is four rather than two.  The `+2` theorem is the exact refinement
charge once the two hosts exist.

The full-block lift in Theorem 3.1 is within-phase.  In particular, it does
not supply a phase-zero-only interval value after switching to phase one (or
vice versa); that obligation belongs to Theorem 4.1, item 3, and its exact
occurrence-labelled Hall formulation in the full-deck note.

## 4. Native return and the reset state

The side target pair used in phase `epsilon` is exactly the native boundary
pair in phase `1-epsilon`.  This makes the split state regenerative rather
than cumulative.

### Theorem 4.1 (conditional full reset)

Assume all of the following.

1. Both oriented refinements (0.2) satisfy the ambient boundary owner,
   q1, residence, deadline and prescribed common-cap rows.
2. Every inherited target-cell assignment uses an admissible full-block
   lift, and simultaneous contraction of the two marked blocks satisfies
   the exact contraction Hall condition.
3. After replacing the contracted packet `Q^epsilon` by
   `Q^(1-epsilon)`, the entire protected occurrence bank together with the
   two old side tasks has one simultaneous matching to opposite-phase
   native/full-block cells, with native
   `Pi_(1-epsilon),Sigma_(1-epsilon)` available.
4. The reverse split cells are available for
   `Pi_epsilon,Sigma_epsilon`.

Then one may contract both marked blocks, switch the packet phase, and
re-split the same two hosts in the opposite orientations.  All inherited
targets survive, the old side targets move to native cells, and the two new
side cells cover the newly missing targets.  Consequently the
essential-boundary state for this typed bank obeys

\[
                         \Phi'\le2                       \tag{4.1}
\]

whenever the carried state uses the two displayed boundaries; equivalently
the local recurrence has full reclaim `g=Phi=2` and fresh refinement cost
`r=2`.

#### Proof

The contraction criterion and its Hall refinement preserve the inherited
matching until phase replacement.  Item 3 is the additional cross-phase
transport and moves the two disappearing side tasks to their native cells.
Item 4 and Theorem 3.1 supply the opposite pair after the reverse split.
Exactly the same two physical host boundaries remain marked.  \(\square\)

Item 3 is essential.  In the sharp inverse at `d=1`, the mask
`{z,a_3,f_0}=Q^0_26` has a contraction-safe singleton witness in phase zero
but is absent from both the contracted and expanded phase-one interval decks.
Thus within-phase full-block transport and contraction Hall alone do not
transport an arbitrary protected bank through phase replacement.

If the two displayed side cells are the only admissible typed witnesses,
both boundaries are essential and equality holds in (4.1).  An ambient
alternate witness can only lower `Phi`.

Without items 1--4, the OR identities alone do not imply reset.  In
particular, a fixed-depth owner compiler may reject the two extra positions,
a transported cell may miss its deadline, contraction may coalesce two
protected matching cells, or the opposite source phase may omit a protected
mask altogether.  In that case the only unconditional ledger is

\[
                         \Phi'\le\Phi+2,                  \tag{4.2}
\]

and the general essential-boundary accumulation obstruction remains live.

## 5. Audit

Run

```text
python3 scratch/audit_threadD_octagon_split_boundary_reset_20260801.py
```

The audit checks `1<=d<=12`, maximal and sharp-thinned inverse occurrence
orders, the typed internal-refinement no-go, ordinary interval-deck
membership of all four masks, the two source-interval identities (1.3),
both oriented exterior splits, simultaneous full-block transport, common
caps, and the conditional `+2/Phi=2` ledger.  It does not audit an ambient
owner/deadline host or item 3's cross-phase matching.

The frozen output is

```text
scratch/threadD_octagon_split_boundary_reset_20260801.audit.json
```

and reports

```text
PASS_THREADD_OCTAGON_SPLIT_BOUNDARY_RESET
payload_sha256=16878689e600ecd3ff068b143c069d8648b5639cb59b5a8134efbd9810e1a003
```
