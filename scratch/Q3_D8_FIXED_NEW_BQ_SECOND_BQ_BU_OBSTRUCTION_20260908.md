# The fixed new BQ has no second-BQ plus BU completion in the old ledger

2026-09-08. Pure derivation by ternary_lift; independent audit pending.
No computation, candidate enumeration, or source preparation occurred.
This closes a particular companion plan, not the new BQ construction.

## 1. Scope and required odd classes

Retain the original verified skeleton and the literal new BQ bundle
55116677 / 33220404, with B=AABBCCDD, Q=AABBCDCD. Its zero-excess
43-row, charge620 partial bank is proved in
Q3_D8_SINGER_NEW_BQ_223_ZERO_EXCESS_PROVIDER_20260908.md.
Consider completing the fixed bank with exactly

    one more BQ + BU + TT + NN + five NZ,

all generic fourteen-row cropped bundles, for final charge2384.
The new BQ has odd complementary rank-four class223, and the endpoint
has class115. A BQ has exactly one odd complementary pair; the BU
parity lemma requires its two odd vertices to form a complementary
pair in the quotient. Therefore the second BQ and BU odd classes
must be115 and223, one each.

The already supplied infinity-one necklaces are115,223,142. The
remaining two are124 and133. The endpoint's forbidden infinity-zero
triples and infinity-two pairs are

    F={123,126,135,146,234,245,456},
    P={16,35,25,26,45,56}.

The fixed new BQ also forbids triples136,256,236,134,235 and
pairs15,14,34. Exact one-one coverage permits no repetition.

## 2. A geometric exclusion for certain second-BQ positions

Use literal BQ=AABBCCDD / EEFFGHGH.

If infinity is B-B, normalize G=0. The infinity-one triple AEF and
the odd-class triple CDH partition the six other cyclic axes. Both
also occur as infinity-zero flags with unique one G. The four
complementary partitions avoiding F have necklace pairs
(124,142),(133,124),(142,133),(133,133). Hence the BQ odd class
cannot be115 or223.

If infinity is Q-G, its odd class is its infinity-one triple AEF.
An odd class115 or223 would repeat an already supplied necklace.

For infinity B-C or Q-F, BQ has two infinity-one flags and must
supply124 and133. Their two-triples are necessarily the partition
125/346 in one order, after normalizing the unused cyclic axis to
zero. The following hand tables exclude either required odd class.

For infinity B-C, put F=0, U=ABE, V=DGH. The odd-class triple is
BDH. The listed (B,G) are all choices yielding115 or223; D,H are
the unused elements of V.

| U / V | Odd class | Possible (B,G) | Exclusion |
| --- | --- | --- | --- |
| 125 / 346 | 115 | (2,6),(5,3),(5,6) | B=5 gives (AE0)-B=234; B=2,G=6 gives (AE0)-G=126 |
| 125 / 346 | 223 | (1,3),(1,4),(2,3) | B=1 gives (AE0)-B=146; B=2,G=3 gives (AE0)-G=245 |
| 346 / 125 | 115 | (3,5) | (AE0)-B=134, supplied by the fixed BQ |
| 346 / 125 | 223 | (3,2) | (AE0)-B=134, supplied by the fixed BQ |

For infinity Q-F, put C=0, U=ABE, V=DGH. The odd-class triple is
AEG. Again all choices yielding115 or223 are listed.

| U / V | Odd class | Possible (B,G) | Exclusion |
| --- | --- | --- | --- |
| 125 / 346 | 115 | (5,3) | AE-B=34, supplied by the fixed BQ |
| 125 / 346 | 223 | (2,3) | AE-G=25 |
| 346 / 125 | 115 | (3,5),(6,2),(6,5) | B=6 gives AE-B=45; B=3,G=5 gives AE-G=16 |
| 346 / 125 | 223 | (3,1),(3,2),(4,1) | (3,1) gives AE-G=35; B=4 gives AE-B=26; (3,2) gives GH-D=14 or34, both supplied by the fixed BQ |

Every exclusion is a literal one-one flag of BQ. Thus a second BQ
at B-B, B-C, Q-F, or Q-G cannot have either required odd class.

## 3. The fixed-axis quotas force those excluded positions

For BQ, the one-one vector has infinity-zero count5. Its
infinity-one count k and endpoint indicator e are:

| Infinity axis | k | Gap | e |
| --- | ---: | ---: | ---: |
| B-A | 0 | 1 | 1 |
| B-B | 1 | 1 | 0 |
| B-C | 2 | 1 | 0 |
| B-D | 1 | 1 | 1 |
| Q-E | 1 | 1 | 1 |
| Q-F | 2 | 1 | 0 |
| Q-G | 2 | 2 | 0 |
| Q-H | 1 | 2 | 1 |

The fixed first BQ has k=2, gap2, indicator0. The remaining
one-one quota therefore requires BU infinity-zero count3 and

    k_secondBQ + j_BU = 2.

For BU this permits only infinity B-A,B-B,B-D,U-E,U-G,U-H.
Write t=1 for U-E/U-G and0 otherwise, and e_U for its endpoint
indicator. The existing TT/NN/NZ central-four quota gives
d+a=1+t+i in the notation of the amended ledger. Consequently
the ten-bundle total satisfies

    sum gap = 19 + gap_secondBQ + t + z,
    sum epsilon = 3 + e + e_U + t.

The critical extra cannot have infinity0, which would require
sum epsilon2. For infinity1 all e,e_U,t vanish. The only BU
position is B-B, whose odd class is133, contradicting Section1.

For infinity2, e+e_U+t=1. BU B-B is again excluded by odd class133.
U-E has e_U+t=2 and is impossible. U-G has t=1 and j=2, so it
would require a second BQ with k=0 and e=0; the table has none.
BU B-A or U-H has j=1,e_U=1, forcing second BQ to B-B. BU B-D
has j=0,e_U=1, forcing second BQ to B-C,Q-F,orQ-G. Section2
excludes all these positions.

This proves the stated fixed-bank completion impossible, subject to
independent audit of the hand tables. It does not invalidate the
literal zero-excess223 provider, nor exclude a different provider
mix, different higher profiles, or an additional repair budget.
