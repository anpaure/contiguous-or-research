# Independent audit of the k=16 length-12,875 two-cell completion

## Verdict

**PASS.**  The file `answers/k16_upper12875.word` is exactly the authenticated
length-12,873 partial word followed, in order, by

\[
x=0x0200,\qquad y=0x287d.
\]

Its SHA-256 is
`d4690a0d11f1d8e69765ec988d9fbcbac63d354ebd6ab07aa8081b577a9ac0c9`.
An independent suffix-OR recurrence covers all 65,535 nonempty masks.
Consequently

\[
12873\leq \nu(16)\leq 12875.
\]

No length-12,873 word is claimed.

## Authenticated inputs

The prefix `scratch/k16_12873_repaired_partial.word` has length 12,873 and
SHA-256
`0a70a67eced48a82883a698c6fd25688a27c52faf19e3fa11bbbd9a78581bea6`.
Its missing set, recomputed from the raw masks, is exactly

\[
T=\{0x287d,0xce61,0xce63\}.
\]

Tokenwise comparison, rather than only hash comparison, gives

\[
\texttt{answers/k16\_upper12875.word}=P\mathbin\Vert(0x0200,0x287d).
\]

## Independent recurrence

For a word `w_0,...,w_j`, let `E_j` be the set of distinct ORs of suffixes
ending at `j`.  The audit computes

\[
E_0=\{w_0\},\qquad
E_j=\{w_j\}\cup\{s\lor w_j:s\in E_{j-1}\},
\]

and marks every member of every `E_j`.  This is logically equivalent to
enumerating all contiguous intervals, but it is a separate linear-size
implementation; at most 12 distinct suffix states occurred at any endpoint.
It returned zero missing nonempty masks for the 12,875-cell word.  The
repository's quadratic verifier independently reports
`PASS k=16 length=12875 covered=65535/65535` with `--allow-nonoptimal`.

## Exact append contributions

The audit of the five relevant words is:

| word | exact missing set |
|---|---|
| `P` | `{0x287d,0xce61,0xce63}` |
| `P,x` | `{0x287d}` |
| `P,y` | `{0xce61,0xce63}` |
| `P,x,y` | empty |
| `P,y,x` | `{0xce61,0xce63}` |

Thus `x` supplies exactly the two old high holes and `y` supplies exactly the
remaining old hole.  All witnesses of the three old holes in the completed
word are the following zero-based intervals:

\[
\begin{array}{c|c|l}
\text{target}&\text{interval}&\text{letters}\cr
0x287d &[12874,12874]&0x287d\cr
0xce61 &[12871,12873]&0x8c61\lor0xcc41\lor0x0200\cr
0xce63 &[12870,12873]&0x8c62\lor0x8c61\lor0xcc41\lor0x0200.
\end{array}
\]

All three displayed targets have exactly the witness lists shown above; in
particular, the singleton `0x287d` witness is unique.

## Exact minimality for this append operation

Both appended cells are irredundant: deleting `x` leaves the two high holes,
and deleting `y` leaves `0x287d`.  Their order is also essential for this
pair: `P,y,x` still misses both high holes.

More strongly, **no single nonzero cell appended to this fixed prefix `P` can
complete it.**  Every nonempty suffix of `P` contains its last cell
`0xcc41`, which has bits outside `0x287d`.  Hence a new interval ending in an
appended cell can equal `0x287d` only when the interval is the new singleton,
forcing that cell to equal `0x287d`.  But `0x287d` has bits outside each of
`0xce61` and `0xce63`, so no interval containing it can equal either high
target.  Therefore two cells are append-minimal for this exact prefix.

This statement does **not** rule out one internal insertion, a simultaneous
edit plus one insertion, or a different length-12,873 basin.

## Reproducer

The fail-closed independent checker is
`scratch/audit_r_k16_upper12875_append2_independent_20260730.py`.
