# The fixed-prefix `k=14` cross-seam completion

## 1. Result

Let `P` be the certified 3,434-entry word
`k14_pinnable_factor_missing260.txt`.  There is an appended word `W` of
length 242 such that `P || W` covers every nonzero 14-bit mask.  The explicit
word is `k14_append_242.txt`, and the concatenation is
`k14_completed_3676.txt`.

Therefore

\[
 \nu(14)\le 3676,\qquad N(14)\le 3677.
\]

This improves the preceding bounds 3677 and 3678 by one.  It does **not**
prove that 3676 is globally shortest, or even that 242 is the shortest suffix
for this fixed prefix.

## 2. The exact old suffix-OR chain

Number the old positions from 1 through 3434.  Reading backward from the
seam, the distinct suffix OR values begin as follows.

| old start | suffix OR | rank |
|---:|---:|---:|
| 3434 | 12329 | 5 |
| 3433 | 12393 | 6 |
| 3432 | 12409 | 7 |
| 3431 | 12411 | 8 |
| 3430 | 12415 | 9 |
| 3429, 3428, 3427 | 12671 | 10 |
| at most 3426 | rank at least 11 | at least 11 |

Consequently a crossing witness for one of the missing rank-9 or rank-10
targets can start only in this terminal zone.  Direct containment against the
certified missing family gives an even sharper table.

| suffix | compatible missing rank-9 targets | compatible hard rank-10 targets |
|---:|---:|---|
| 12329 | 18 | 13439, 13757 |
| 12393 | 7 | 13439 |
| 12409 | only 12923 | 13439 |
| 12411 | only 12923 | 13439 |
| 12415 | none | 13439 |
| 12671 | none | none |

Here the hard upper family is

\[
\{7676,8015,13287,13439,13757,14285,15334,15346\}.
\]

This table is the complete finite interface between the old prefix and any
new suffix for these 260 omissions.

## 3. The seam splice

The first three new entries are

\[
 1095,\quad 8014,\quad 15694.
\]

They give four decisive witnesses:

\[
\begin{aligned}
12329\mathbin{\mathrm{OR}}1095&=13423,\\
12409\mathbin{\mathrm{OR}}1095&=13439,\\
1095\mathbin{\mathrm{OR}}8014&=8015,\\
8014\mathbin{\mathrm{OR}}15694&=16206.
\end{aligned}
\]

Thus the same new entry 1095 uses two members of the old suffix chain to
replace both the missing rank-9 literal 13423 and the former rank-10 edge
13423--48.  Its new right neighbor 8014 simultaneously replaces the old
literal 8015.  This is exactly the one-entry saving that a standalone
completion cannot obtain.

The complete 242-entry word is obtained mechanically from the old certified
243-entry completion `k14_completion_best.txt`:

1. delete old one-based positions 81, 82, 152, 153, and 243, whose values are
   respectively 8014, 15694, 13423, 48, and 8015;
2. prepend `1095 8014 15694`;
3. append the literal 13757.

The count is

\[
243-5+3+1=242.
\]

The moved adjacent pair 8014,15694 retains the witness for 16206.  The edge
48,13725 formerly represented 13757; its replacement literal represents the
same target.  All other targets retain append-only witnesses.  In fact,
enumerating the 29,403 intervals of `k14_append_242.txt` alone shows that it
covers 258 of the 260 old omissions and misses exactly 13423 and 13439.  The
two displayed old/new intervals cover precisely those remaining masks.

## 4. Exact witness indices

In the completed length-3676 word, the five altered witnesses are:

| target | rank | zero-based interval | one-based interval | mode |
|---:|---:|---:|---:|---|
| 13423 | 9 | [3433,3434] | [3434,3435] | cross-seam |
| 13439 | 10 | [3431,3434] | [3432,3435] | cross-seam |
| 8015 | 10 | [3434,3435] | [3435,3436] | appended |
| 16206 | 10 | [3435,3436] | [3436,3437] | appended |
| 13757 | 10 | [3675,3675] | [3676,3676] | appended |

The same records occur in `k14_append_242_seam_certificate.txt`.

## 5. A fixed-prefix lower bound: 241 entries are necessary

The seam analysis also strengthens the trivial rank-9 endpoint bound.  Any
suffix completing this particular prefix has length at least 241.

Choose one witness for each of the 238 missing rank-9 targets.  Since none
occurred in the prefix, their right endpoints are 238 distinct new positions.
Write the appended length as

\[
q=238+t.
\]

Only four old starts can support a missing rank-9 witness: 3431 through 3434.
Moreover starts 3431 and 3432 can support only the same target 12923, so at
most three selected rank-9 witnesses can start in the old prefix.  Call their
number `x`; then

\[
x\le3.
\]

The eight hard rank-10 witnesses have distinct right endpoints.  The target
15346 contains no missing rank-9 target, so its right endpoint cannot be
shared with a selected rank-9 witness.  Each of the other seven hard targets
contains exactly one missing rank-9 target.  If such a hard witness shares
its right endpoint with its unique lower witness, it cannot also share the
left endpoint with that same witness, because then the two physical intervals
would be identical.

If `t=1`, 15346 consumes the only unused new right endpoint.  Hence the other
seven hard targets all share their right endpoints with their lower bases,
and all eight hard targets require lower-free left endpoints.  There are only
`1+x` lower-free new starts.  Among old starts, at most two *distinct* hard
targets can occur at all, namely 13439 and 13757.  Thus there are at most

\[
(1+x)+2\le6
\]

available lower-free left endpoints, fewer than eight.  Hence `t=1` is
impossible.

If `t=2`, after 15346 uses one free right endpoint, at most one of the seven
unique-base targets can use the other.  Therefore at least six of those seven
share right endpoints with their bases.  Together with 15346, at least seven
hard witnesses require lower-free left endpoints.  The crude capacity is

\[
(2+x)+2\le7.
\]

Equality would require `x=3` and both old-compatible hard targets.  But 13757
can use only old start 3434, so that start would have to remain lower-free.
With start 3434 unavailable, three old rank-9 starts would have to be selected
from 3431, 3432, and 3433.  Starts 3431 and 3432 can both produce only 12923,
and selected equal-rank targets must be distinct.  Hence at most two can be
selected, contradicting `x=3`.

The case `t=0` is already impossible because 15346 has no free new right
endpoint.  Therefore

\[
q\ge241.
\]

Combining this with the construction gives the exact current fixed-prefix
window

\[
241\le q_{\min}(P)\le242.
\]

Whether a 241-entry suffix exists remains open.  The proof above already
forces any such suffix to use at least one genuinely crossing rank-9 witness;
more detailed equality cases are the natural next finite problem.

### The complete seam branching for `q=241`

The endpoint proof gives a compact exact reduction of that last case.  Let
`x` again be the number of selected rank-9 witnesses whose left endpoint is
old.  Let `f` be the number of the seven unique-base hard targets whose right
endpoint is one of the three new right endpoints not occupied by rank-9
witnesses.  Since 15346 necessarily uses one of those three endpoints,

\[
f\le2.
\]

The other `7-f` unique-base targets share their right endpoints with their
sole lower bases.  They cannot also share the left endpoints with the same
base witnesses.  Together with 15346, at least

\[
8-f
\]

hard witnesses therefore require lower-free left endpoints.  There are
`3+x` such new starts and at most two usable old starts, one for 13439 and one
for 13757.  Hence `x=0` is impossible.  More precisely, if `h` denotes the
number of those two old hard starts actually available, the only endpoint
profiles are

| `x` | necessary `(f,h)` profiles |
|---:|---|
| 1 | exactly `(2,2)` |
| 2 | `f=2,h>=1` or `f=1,h=2` |
| 3 | `f=2`, or `f=1,h=1`; `f=0` is impossible |

For `x=3`, the old lower starts are forced to be 3434, 3433, and exactly one
of 3431 and 3432.  Thus start 3434 is unavailable to 13757, so at most the
13439 old hard start remains; this is the reason `f=0` drops out of the last
row.

The nonnesting order gives an additional finite cutoff.  The old-start
rank-9 witnesses are the first `x` witnesses in left-endpoint order, while
their selected right endpoints are the first `x` elements of a 238-subset of
241 new positions.  Their new right endpoints are therefore at most

\[
4,5,6
\]

respectively.  Only the first six prefix OR states of a proposed suffix are
relevant to all old-start rank-9 witnesses.

Write the usable old suffixes in increasing-old-start order as

\[
12411,\ 12409,\ 12393,\ 12329.
\]

For two old-start witnesses, exact bit containment leaves only 27 ordered
target pairs.  Their counts by the selected suffix pair are:

| first suffix | second suffix | possible ordered target pairs |
|---:|---:|---:|
| 12411 | 12409 | 0 |
| 12411 | 12393 | 2 |
| 12411 | 12329 | 9 |
| 12409 | 12393 | 2 |
| 12409 | 12329 | 6 |
| 12393 | 12329 | 8 |

For three witnesses there are only six ordered triples.  The first suffix is
12411 or 12409 and the first target is always 12923.  For either first-suffix
choice, the remaining possibilities are

```text
12923, 12911, 13103
12923, 13163, 13103
12923, 13163, 15147
```

The corresponding minimal nested appended-prefix OR requirements are

```text
first:   512  (for suffix 12411), or 514 (for suffix 12409)
second:  518  (target 12911), or 770 (target 13163)
third:   774  (target 13103), or 2818 (target 15147)
```

These lists follow from the exact criterion for two consecutive seam events.
If old suffixes `C > C'` are assigned targets `S,S'`, a nested pair of prefix
OR masks exists exactly when

\[
S\setminus C\subseteq S'.
\]

One may take the first prefix requirement as `S\C` and the second as its
union with `S'\C'`.  Iterating the same test gives the six triples above.

Thus the unresolved 241 case is no longer a raw 241-by-14 search at the seam.
It consists of the endpoint profiles in the first table, 27 two-crossing
branches or six three-crossing branches, and a monotone chain of at most six
explicit 14-bit prefix states, followed by the residual append-only interval
assignment.  This is the appropriate exact finite target for a subsequent
proof or solver.

## 6. Independent verification and prefix identity

The completed file has exactly 3,676 integers.  Its first 3,434 integers are,
term for term, the unchanged sequence in
`k14_pinnable_factor_missing260.txt`; its remaining 242 integers are exactly
`k14_append_242.txt`.  Whitespace normalization is immaterial.  A direct
integer-sequence comparison passes for both parts.

Two independent remote verifiers pass:

* exhaustive enumeration of all physical intervals:
  `length=3676 covered=16383 required=16383`;
* the distinct-suffix-OR recurrence:
  `length=3676 covered=16383/16383 missing=0`.

The corresponding outputs are
`k14_completed_3676_exhaustive.log` and
`k14_completed_3676_suffix.log`.

SHA-256 values:

| artifact | SHA-256 |
|---|---|
| old prefix | `4c71a5e59985ff8d78a4ae80845defd21cebfe240c16ad4604b57e9b9cb999ad` |
| `k14_append_242.txt` | `41d7028668cde93d6f9347ae881b352dfbc3de446845324a185b21414099d8a8` |
| `k14_completed_3676.txt` | `df86beff2854227f215a8720a7959489c689d3d3d5747e9847a2ff9fd3aeac94` |
| `k14_append_242_seam_certificate.txt` | `f7e362a9248ae1aaf32036bd47904e246342fd5c7b231584d04be4d6e5b5b38d` |
| exhaustive log | `49e044c4d1be8a144bec80026ac4ceef41002fe7b1c133a64dd97952ed8ceed5` |
| suffix-recurrence log | `c8565cc9d1f594bcbe479cd8844535eb3dcfbe6a5d865285225c0cb34c59ea13` |
