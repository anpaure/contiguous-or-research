# The planted mixed-screen schedule is lower-shadow optimal

Date: 2026-08-01  
Status: exact local classification for the authoritative twelve-owner ECO
connector.  This is a packet-fibre theorem, not a global lower bound on the
terminal compiler deletion number.

## 0. Result

Among the sixteen mixed lower/upper screen schedules which give the two ECO
phases common simple immediate screen palettes, the minimum possible local
lower-intersection support exchange is

\[
          2\text{ old-only and }2\text{ new-only values}          \tag{0.1}
\]

at every depth `2 <= q <= d`.  Exactly three schedules attain (0.1):

```text
{1,3,5,7},
{0,2,4,5,6,8,10},
{0,2,3,4,5,6,8,10}.
```

The **superseded** first-block endpoint rotation used in the original
Section 8.5 required transition `0` to remain a lower screen.  On that
restricted face, the canonical schedule

\[
                              \{1,3,5,7\}                        \tag{0.2}
\]

is the **unique** minimizer.  The corrected endpoint planting instead uses a
different first-block order and an upper screen at transition zero; it is
proved and audited separately in
`MATH_THEOREM_COATOM_ENDPOINT_PLANTING_FIXED_SLOT_HALL_CORRECTION_20260801.md`.
This note does not classify the deeper lower action after that reordered
first block.  Its uniqueness statement applies only to the old lower-rooted
planting face, not to all endpoint-compatible coatom tensors.

This does not prove a global compiler defect of `2(d-1)`: an exchanged local
value may have another witness outside the packet.  It proves that schedule
tuning inside this exact packet fibre cannot make the local lower exposure
bounded independently of `d`.

## 1. Symbolic calculation

Put `n=d+2`.  A depth-`q` lower value is the intersection of `q+1`
consecutive tensor owners.  For `2 <= q <= d`, such a window has length at
most `d+1<n`, so it crosses at most one screen.

Windows contained in one coatom block agree because the two phases have the
same active-owner set.  Windows through a lower screen depend only on its
active intersection colour; the legal-schedule definition makes those
colours common.  At an upper screen, every window using owners on both sides
again has the active intersection colour.  Only the two one-sided endpoint
windows can differ.

Their filler profiles are

\[
 P_q=\{f_1,\ldots,f_{n-q-1}\},\qquad
 S_q=\{f_q,\ldots,f_{n-2}\}.                                  \tag{1.1}
\]

For `q>=2`, `P_q` and `S_q` are distinct.  Neither can coincide with a
lower-screen profile because an upper screen additionally omits both extreme
fillers.  Consequently the old-only count for a schedule `E` is exactly

\[
 \left|\{V_j:j\in E\}_{old}\setminus
              \{V_j:j\in E\}_{new}\right|
 +
 \left|\{V_{j+1}:j\in E\}_{old}\setminus
              \{V_{j+1}:j\in E\}_{new}\right|,                 \tag{1.2}
\]

and the new-only count is the reverse difference.  Formula (1.2) is
independent of `d` and `q`.  Exhausting the `2^11` active schedules and
retaining the sixteen legal ones gives only `(2,2)` or `(4,4)`, with `(2,2)`
precisely for the three schedules in Section 0.

At `q=1`, the two filler profiles merge and additional collisions are
possible.  The canonical schedule has exact immediate palettes, as already
proved by the authoritative tensor theorem.

## 2. Consequence for the additive-constant route

For the canonical standard filler order, the local packet is already optimal
in its screen-choice coordinate.  The remaining useful structure is not a
smaller loss count but the form of the losses: the canonical `(2,2)` exchange
is a pair of synchronized nested prefix/suffix filler chains.  The later flag
lattice theorem now gives their exact saturated span.  The corrected
upper-rooted endpoint rotation is a separate physical-host fibre.

## 3. Replay

The dependency-free replay enumerates all `2^11` schedules, recovers the
sixteen legal schedules, checks the symbolic endpoint formula, and literally
replays every `2 <= d <= 32` and `1 <= q <= d`:

```text
scratch/audit_mixed_screen_lower_damage_optimality_20260801.py
  e0f86afcba8f4607b7e5dc64ee2f3782123e110d4a4dd5cfbdb48b0ab9b90a87
scratch/mixed_screen_lower_damage_optimality_20260801.audit.json
  30b54df679e214bdb1c167a41c5695824a3403199e0db9be6938c597a738007f
```

It reports

```text
PASS_MIXED_SCREEN_LOWER_DAMAGE_OPTIMALITY
```

with canonical payload SHA-256

```text
85401f530d0d3f11f68b7c24136f1111fd7e208f2ae1c4265071411698eb9aa8
```
