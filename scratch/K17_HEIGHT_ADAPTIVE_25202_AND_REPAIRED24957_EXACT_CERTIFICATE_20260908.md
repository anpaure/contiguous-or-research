# Fixed height-adaptive PBBS construction: a universal 24,957-letter word

Date: 2026-09-08. Independent exact finite construction and verification.

Status: one bounded deterministic h100 execution passed. It materialized a
25,202-letter universal height-adaptive word and a shorter 24,829-letter
partial word. The latter has exactly 128 missing targets; appending those
targets as individual letters gives a universal word of length 24,957.
All letters are nonzero. Every one of its 131,071 targets has an ordinary,
nonwrapping interval witness that was rechecked by a separate range-OR
implementation.

Together with the established endpoint lower bound, this proves

    24,313 <= nu(17) <= 24,957.

The user proposed the height-adaptive recipe and reported a 24,969-letter
word obtained from 140 missing targets. That particular word was not
supplied or independently checked here. The present 24,957-letter word is
the independently materialized result of the single explicit convention
below. It is not a verification of the user's different 140-hole inventory,
and it is not asserted optimal.

## 1. Exact canonical map, component order, and cut convention

Coordinates are numbered 1 through 17, and coordinate x is bit x-1.
Let FULL=131071. Enumerate every rank-eight lower owner A. Find its unique
unmatched zero u by requiring that the sixteen coordinates cyclically
following u form a nonnegative balanced Dyck word. Define

    f(A)=FULL xor A xor (1<<u),   g=f^2.

This is precisely the original canonical map used in
`audit_k17_pbbs_cycle_upper_cut_inventory_20260908.py`. Decompose g into
cycles. Start each lower cycle at its smallest integer mask, traverse in
the forward g direction, and order all cycles by their initial masks.
No alternate cut, orientation, or cycle ordering is tested.

The run has 146 cycles containing all 24,310 lower owners. On each cycle
the maximum height h of its rooted Dyck word is invariant; this was checked
at every state. The component-height histogram is

| h | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Number of cycles | 1 | 29 | 46 | 40 | 21 | 7 | 1 | 1 |

Thus the sum of component heights is exactly 519.

## 2. The two literal height-adaptive openings

For a lower cycle (A_i) of length L, let X_i=FULL xor A_i be its rank-nine
upper owners. With all indices cyclic, form the source period

    D_i=intersection_(j=0)^h X_(i+j),  0<=i<L.

Every D_i was checked nonempty. In every component, every proper positive
coordinate residence is strictly larger than h. Independently of that run
check, literal period unions verify at every i that

    union_(j=0)^h D_(i+j)=X_(i+h).

The longer opening emits the period followed by its first 2h-1 letters.
Concatenate these blocks in the fixed component order. Its exact length is

    24,310 + sum_cycles(2h-1) = 24,310+1,038-146 = 25,202.

The shorter opening emits each period followed by its first h letters.
Concatenating in exactly the same order gives

    24,310 + sum_cycles h = 24,829.

The first word covers every nonempty target. The second covers 130,943 of
the 131,071 targets, including all targets of ranks one through nine and
thirteen through seventeen. Its exact missing-rank census is

| Missing rank | 10 | 11 | 12 | Total |
|---:|---:|---:|---:|---:|
| Number missing | 65 | 49 | 14 | 128 |

The certificate contains every one of the 128 missing masks, not only this
census. Append them as singleton *letters* in increasing integer-mask order
(these letters themselves are rank-ten, eleven, or twelve subsets). Each
formerly missing target now has its own length-one interval. Every old
witness remains within the unchanged prefix. Hence the resulting length
24,829+128=24,957 word is universal. A full independent target scan and
range-OR replay confirm this direct repair argument.

Opening cuts change which cyclic witnesses survive inside a block, and
the component order changes which targets are supplied by intervals crossing
block boundaries. Therefore these choices can affect the actual hole census
of the concatenated shorter word. Our 128-hole result under the stated
fixed convention does not contradict a 140-hole result for a differently
opened or ordered word. The user's exact 140-hole word was not available
to compare. No search was used to reduce the hole count to 128.

## 3. Literal words, checksums, and exhaustive verification

The three materialized words have these independently recorded checksums:

| Word | Length | Distinct targets | Missing | SHA-256 |
|---|---:|---:|---:|---|
| `k17_height_theorem25202.word` | 25,202 | 131,071 | 0 | `b491a5b1a7b8f2b21edc9ac46b8d031b1bc3895f668a9a025ec1115eee79d982` |
| `k17_height_trimmed24829.word` | 24,829 | 130,943 | 128 | `a0449903fb7e1161494d58187d8589654aa22dc5c1cf0fd18e9798bbed533450` |
| `k17_height_repaired24957.word` | 24,957 | 131,071 | 0 | `dc7c7af32feb73c91fd14e00c6a046de6d753af4d2fc632f71960dcdbdd820db` |

For each word, the checker maintains every distinct suffix OR at each
endpoint, retaining a literal start/end witness for every target. There are
at most seventeen distinct suffix ORs at an endpoint, so this covers all
ordinary interval unions without scanning every pair of endpoints.

It then builds a separate segment tree directly from the literal word and
independently re-evaluates the interval OR for every recorded target. Every
witness has in-range zero-based inclusive endpoints; no wraparound is used.
The all-target tests compare against every integer mask from 1 through
131071. No coverage premise comes from the unverified construction search
for the earlier 25,374-letter word or from a presumed asymptotic result.

This execution also checks the finite strict-residence and erosion
identities for every actual component in dimension seventeen. The proposed
all-dimension height-adaptive theorem is being audited in separate proof
notes; the literal universal-word certificate here does not depend on
assuming that proposed general theorem.

## 4. Exact integer checks of the two proposed thresholds

For

    W=binom(2r+1,r),
    e_r=(2^(2r+2)-3W)/((2r+1)W),

the same bounded h100 process evaluated the exact integer sign of

    q*(2^(2r+2)-3W) - (2r+1)W

for (r,q)=(283,10),(284,10),(31115,100),(31116,100).
It also computed rational enclosures with denominator 10^20 by exact
integer division. The resulting lower endpoints are listed below; in
each row the upper endpoint is exactly the lower endpoint plus 10^-20.

| r | Rational lower endpoint | Exact comparison |
|---:|---:|:---|
| 283 | 0.10011665992129646015 | e_r>1/10 |
| 284 | 0.09994935560479428639 | e_r<1/10 |
| 31115 | 0.01000007366975609665 | e_r>1/100 |
| 31116 | 0.00999991375155981379 | e_r<1/100 |

Thus the requested adjacent threshold inequalities pass, in fact strictly
on both sides. These four comparisons alone do not prove monotonicity
of e_r or a minimal threshold across every earlier r; such a global claim
requires the separate general argument. No floating-point computation
was used for these comparisons or enclosures.

## 5. Complete artifacts and execution limits

The exact script is

    scratch/verify_k17_height_adaptive_fixed_construction_20260908.py.

All outputs are copied to

    scratch/k17_height_adaptive_20260908/.

The three word names are in Section 3. For each word its full target map
is stored in the corresponding `*_target_witnesses.json`. The principal
`height_adaptive_fixed_certificate.json` records the three coverage reports,
all missing masks, height census, SHA-256 hashes, and the exact threshold
comparison signs and rational enclosures.
`height_adaptive_canonical_cycles.json` stores every lower cycle, height,
minimum positive residence, source period, and its offsets in both openings.
Together these files specify the entire finite construction and all witnesses.

The single process ran only on h100 in

    /home/amodo/exact-b-k17-height-adaptive-20260908/.

It had limits of 120 CPU seconds, 150 wall seconds, and 2 GiB address space.
It returned PASS. No alternative cuts, ordering search, repair selection,
or further mathematical run was performed. Appending every missing mask
was the prescribed deterministic repair, with no removal of redundant
repairs or attempt to improve the resulting 24,957 length.
