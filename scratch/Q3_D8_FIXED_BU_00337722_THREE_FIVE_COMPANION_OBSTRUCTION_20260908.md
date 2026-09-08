# The fixed BU223 provider has no exact two-primitive completion

2026-09-08. Pure hand proof, with no mathematical execution. Ternary_lift
independently audited the general primitive tables and the actual BU
supplier. Root independently checked the three final assignments below;
full-file audit and the complete loop-classification dependency now
passed root's independent check. Appendix_a supplies the separate
complete endpoint-disjoint loop classification used in Section2.

The scope is the ORIGINAL29-row Singer skeleton, the FIXED G-closed BU
row C=00337722, U=46146155, and exactly two G-closed3+5 primitives of
the literal form in Section1. Their one-one critical targets must cover
the26 residual C7 orbits exactly; every other completion profile must
have no one-one targets. The theorem does not exclude another BU
embedding, other primitive words, or a ledger permitting one-one repeats.
The actual BU partial bank remains valid.

## 1. Notation, actual rows, and forced parity

Infinity is global coordinate0. Cyclic labels0,...,6 correspond to
global coordinates(1,2,4,3,6,7,5); arithmetic on cyclic labels is modulo7.
G means C7 together with global complementation. A flag(T;o) is the
rank7 target with twos on T, one at o, and zero elsewhere. Rank9 flags
are reflected to rank7 notation. Cyclic triples are normalized by
subtracting their unique cyclic one when infinity has value0.

The3+5 primitive has words and retained ranks

    AABBCC:       0,...,6;
    DEDEFFGHGH:   2,...,8.

Its one-one flags are

    lower:    (DEF;G),(DEF;A),(ADE;F),(ADE;B),(ABD;E);
    reflected upper:
              (BCH;G),(CGH;B),(CGH;F),(FGH;C),(FGH;E).

Its odd upper vertices in the Boolean flag graph are DEFG and EFGH.
All tables and flags are proved in
`Q3_D8_THREE_FIVE_TIGHT_PRIMITIVE_FIXED_AXIS_AND_PROVIDER_QUOTAS_20260908.md`.

The original endpoint forbids infinity-zero normalized triples

    {123,126,135,146,234,245,456},

infinity-two normalized pairs

    {16,35,25,26,45,56},

and the infinity-one necklace115. The other four infinity-one necklaces
are124,142,133,223, each required exactly once by this provider ledger.

The fixed BU row has cyclic roles

    (A,B,C,D,E,F,G,H)=(infinity,3,5,1,2,4,0,6).

Its literal positive-target audit is in
`Q3_D8_BU_INFINITY_FIRST_223_ZERO_EXCESS_PROVIDER_20260908.md`.
It supplies infinity-one223. Its odd upper vertices are the
infinity-containing necklace124 and the infinity-free endpoint odd
orbit Hc, whose cyclic complement has necklace115.

The exact fixed-axis count table forces the two primitives to have
infinity respectively on A/C and E/F/G. The first therefore has both
odd vertices infinity-free, and the second both infinity-containing.
The endpoint's required odd vertices are H=infinity+012 and Hc.
Since BU already supplies Hc, the first primitive's two odd vertices
must be the SAME Singer orbit, cancelling modulo2. On the infinity
side, the second primitive must have DISTINCT odd necklaces115 and124.
This retains the quotient-loop possibility rather than discarding it.

## 2. The required three-shore loop fixes the remaining one-one deck

Appendix_a's endpoint-disjoint loop classification normalizes infinity
to A by reversal and D=0 by a Singer translate. The loop condition gives

    {B,C}={d,2d}, H=3d, d nonzero.

After testing the literal endpoint flag restrictions and intrinsic
one-one repetitions, its unique survivor is

    P0: (A,B,C,D,E,F,G,H)=(infinity,4,1,0,3,2,6,5),
    global words006622 /1313445757,
    retained ranks0,...,6 /2,...,8.

This is uniqueness within the stated literal loop family, modulo the
Singer translations and reversal already included in G. The complete
small case proof is a separate dependency, not an inferred consequence
of the existence of P0.

That complete proof is
`Q3_D8_THREE_FIVE_INFINITY_A_LOOP_CLASSIFICATION_AND_LITERAL_EXTENSION_20260908.md`.
Root independently audited every step-size exclusion and every entry
of its five-assignment table: PASS. The dependency is discharged.

P0 has one-one signatures

    infinity0: 134,256,124,346,145,236;
    infinity1: necklace142;
    infinity2: 15,36,14.

Thus any second primitive must supply infinity-one necklaces124 and133,
and must avoid P0's infinity-zero signature346. The argument below uses
only these facts, the odd115/124 requirement, and the original endpoint
pair restrictions. It does not require central-target restrictions.

## 3. Infinity F cannot have odd necklaces115 and124

For infinity F, the odd cyclic triples are DEG and EGH. Reversal
exchanges D with H and E with G, while keeping F fixed, so orient the
first triple DEG to have necklace115. Translate it to{0,1,2}.

The critical infinity-two flag(DEF;G) has normalized pair DE-G.
If G=1 this pair is16; if G=2 it is56. Both are forbidden, so G=0.
There are only two orders for D,E:

| D | E | H forced by EGH necklace124 | GH-E |
| --- | --- | --- | --- |
| 2 | 1 | 3 | 26 |
| 1 | 2 | 6 | 45 |

The final column is the infinity-two flag(FGH;E). Both26 and45 are
endpoint-forbidden. Infinity F is therefore impossible even without
the new BU or P0 target restrictions.

## 4. Infinity G leaves three assignments, all repeating346

Reversal exchanges infinity E and G, so the remaining case is G.
Its odd cyclic triples are DEF and EFH; DEF is also one of its two
infinity-one flags. Since the second primitive must supply124 and133,
DEF cannot be the odd115 triple. Consequently

    DEF has necklace124, EFH has necklace115,
    BCH has necklace133.

Translate EFH to{0,1,2}. The pair FH-E from(FGH;E) forces E=0:
E=1 gives16 and E=2 gives56. Then{F,H}={1,2}.
The pair FH-C from(FGH;C) rules out C=3 and4 by56 and45 respectively,
so C is5 or6.

The condition DEF=124 gives exactly

    (F,H,D)=(1,2,3) or(2,1,6).

Indeed, with E=0,F=1 only D=3 gives the oriented cyclic necklace124;
with E=0,F=2 only D=6 does. Requiring BCH=133 now leaves the following
complete table:

| D | E | F | H | A | B | C | DEF-A |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 0 | 1 | 2 | 4 | 6 | 5 | 346 |
| 3 | 0 | 1 | 2 | 4 | 5 | 6 | 346 |
| 6 | 0 | 2 | 1 | 3 | 4 | 5 | 346 |

For the first two rows, DEF=013 and013-4=346. In the third,
DEF=026 and026-3=346. This last column is the actual infinity-zero
flag(DEF;A), and P0 already covers precisely that Singer target orbit.
Every possible second primitive therefore violates exact one-one
coverage.

## 5. Scope of the exclusion

Using the separately proved and independently audited loop classification,
the fixed BU row00337722/46146155 admits no exact two-primitive
completion in the stated literal G-closed provider ledger. Sections3
and4 are independently inspectable endpoint/flag arguments; no solver,
candidate catalogue, or numerical test is a premise.

Another BU embedding can change the required odd vertices and the
remaining target deck. This note leaves that possibility open.
