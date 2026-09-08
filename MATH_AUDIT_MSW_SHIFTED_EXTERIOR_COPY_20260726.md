# The one-phase-shifted rectangle is not an independent exact move

Date: 2026-07-26

## 0. Verdict

The second self-depth neutral arm of the recursive MSW rectangle is
preloaded on the opposite, one-phase-shifted boundary window.  It is
natural to try to add the corresponding shifted-exterior rectangle.  For
the certified two-row rectangle this does not create a second move.

* Swapping only one exterior phase preserves the two row paths but fails
  the adjacent-union ownership ledger.
* Exact ownership forces the two exterior phases to be swapped together.
* That two-end swap produces, as an unordered row family, exactly the same
  factor as the already certified middle-phase swap.

Thus the shifted copy is either illegal or inert.  It cannot turn the
one persistent neutral arm into two without a genuinely larger packet.

## 1. Complete local classification

Suppress the common spectator set `Q`.  The two canonical traces are

\[
 A=(12,14,34),
 \qquad
 B=(13,23,24).                                           \tag{1.1}
\]

At each of the three phases choose whether to keep the two states in their
rows or swap them.  Let

\[
                         b=(b_0,b_1,b_2)\in\{0,1\}^3    \tag{1.2}
\]

record these choices.  The middle-state ownership ledger is preserved for
every `b`, because each phase merely permutes its two states.  All eight
choices also give Johnson edges within each row.  Exact odd-graph
ownership additionally requires the multiset of the four adjacent unions
to remain

\[
                         \{123,124,134,234\}.            \tag{1.3}
\]

### Lemma 1.1 (three-phase rectangle classification)

The adjacent-union ledger (1.3) is preserved if and only if

\[
                         b_0=b_2.                        \tag{1.4}
\]

Consequently the only ledger-preserving phase patterns are

\[
                         000,\quad010,\quad101,\quad111. \tag{1.5}
\]

Moreover `000` and `111` give the same unordered row family, while `010`
and `101` give the same unordered row family.

#### Proof

If only the first phase is swapped, the new adjacent-union multiset is

\[
                         \{123,134,134,234\},            \tag{1.6}
\]

so `124` is lost and `134` is repeated.  Swapping only the last phase is
the reflected failure.  Swapping the middle phase does preserve (1.3):

\[
 (12,23,34),
 \qquad
 (13,14,24).                                             \tag{1.7}
\]

Swapping both exterior phases also preserves (1.3):

\[
 (13,14,24),
 \qquad
 (12,23,34),                                             \tag{1.8}
\]

which is exactly the same unordered pair as (1.7).  Complementing all
three phase bits merely exchanges the two row names.  These observations
give (1.4)--(1.5) and exhaust the eight choices.  Adjoining the common
spectator set `Q` to every state does not change any conclusion.
\(\square\)

## 2. Consequence for the shifted-preload proposal

At the matched depth the certified middle swap `010` has occurrence-level
moves

\[
                         2\longrightarrow4,
 \qquad                  4\longrightarrow3.             \tag{2.1}
\]

The preload at `3` comes from the opposite boundary window.  Aligning a
move with that window requires changing an exterior phase.  Lemma 1.1
shows the exact alternatives.

1. Change one exterior phase only: the adjacent-union ledger fails, so the
   rows do not form an exact local replacement.
2. Change both exterior phases: the resulting unordered row family is
   already the `010` factor, so no independent switch bit and no new
   target action are obtained.
3. In an open slab with individually fixed boundary ports, the exterior
   phases cannot be changed at all; only `010` remains.

Therefore the one-phase offset diagnosed in the persistent-suffix audit
cannot be repaired by an adjacent copy of the same two-row rectangle.  A
repair must use auxiliary rows or a parent-boundary-changing packet whose
ledger is not the two-row table (1.1).  This is consistent with the
canonical two-boundary/Klein-four audit: coordinate endpoint copies only
permute the Catalan cell vector and do not split it.

## 3. Scope

This is a complete no-go for shifted copies of the **same two-row
rectangle**.  It does not rule out:

* the known four-row complete-wreath associator packet;
* a larger packet which repairs the lost adjacent-union colour using
  auxiliary rows;
* a nonlocal atom which changes the parent ports coherently.

Those are precisely the mechanisms that would have to be tested next if
one wants a second persistent neutral arm.
