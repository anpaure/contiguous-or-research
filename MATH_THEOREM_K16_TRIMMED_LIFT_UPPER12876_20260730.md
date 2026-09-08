# K16 trimmed lift: a verified upper bound of 12,876

Date: 2026-07-30  
Status: **proved construction and independent exhaustive replay**

## The construction

Let (A=(a_1,\ldots,a_n)) be any universal nonzero word on (k)
coordinates, and let (z) be a new coordinate.  Define

\[
 A^+=A,\ \{z\},\ (\{z\}\cup a_1),\ldots,
                 (\{z\}\cup a_{n-1}).
\]

Then (A^+) is universal on (k+1) coordinates and has length (2n).
Indeed, targets not containing (z) occur in the first copy.  The singleton
\(\{z\}\) occurs at the middle cell.  If (a_i\vee\cdots\vee a_j=S)
and (j<n), its lifted copy gives \(\{z\}\cup S\).  If (j=n), the
first-copy suffix (a_i,\ldots,a_n) followed by \(\{z\}\) gives the same
target.  Thus

\[
                         \nu(k+1)\le 2\nu(k).
\]

Applying this to the authenticated optimal (k=15) word of length (6438)
gives

\[
                         \boxed{\nu(16)\le12876}.
\]

Together with the monotone-deadline lower bound,

\[
                         \boxed{12873\le\nu(16)\le12876}.
\]

The previously displayed upper bound `12909` in the handoff was stale; the
trimmed-lift recurrence was already proved earlier in the research log but
had not been propagated to the current K16 headline.

## Artifacts

The retained literal word is

```text
answers/k16_upper12876.word
SHA-256 9d0214f6c7cea45a1f26d031687ecada9ac34500e925dcfc127bdf1514b624c8
```

Two independent replay paths enumerate all (65,535) nonzero targets:

```text
scratch/audit_k16_trimmed_lift_upper12876_20260730.py
SHA-256 0ff37384b35dfc694845ad4774ba2054eccfba61bd958a954916b32703e56925

scratch/k16_trimmed_lift_upper12876_20260730.audit.json
SHA-256 bccf5314b737c9343e7aa2c41bab2cfd250e9e6e9256d650f02d577093e39bf3

python3 verify_word.py --k 16 --allow-nonoptimal answers/k16_upper12876.word
```

The audit constructs the word from the pinned (k=15) source hash rather
than trusting the retained output, then enumerates contiguous ORs from
scratch.  It reports `65535/65535` covered.

## Scope

This proves only the upper bound.  The word has three more cells than the
conjectured optimum, and its derivative rows are not a flat central carrier.
The remaining finite problem is now a three-cell compression, possibly with
simultaneous replacement/rethreading; it is not merely three monotone
deletions.

## Subsequent fixed-boundary obstruction

`MATH_THEOREM_R_K16_TRIMMED_LIFT_FIXED_BASE_HIGH_SHORE_COMPRESSION_NOGO_20260730.md`
sharpens the scope of that compression problem.  If the authenticated first
copy `A` and the following singleton `{z}` are retained consecutively, then
**no** arbitrary 6,434-cell suffix `H` makes `A|{z}|H` universal.  The proof
uses equality in the rank-seven interval-antichain bound and is stronger than
the earlier 3,218-cell support floor.  Therefore a length-12,873 construction
must also alter the first copy or the singleton boundary, or use an
interleaved multi-sector chronology.  This is an architecture-specific no-go,
not a global improvement of the lower bound `12873`.
