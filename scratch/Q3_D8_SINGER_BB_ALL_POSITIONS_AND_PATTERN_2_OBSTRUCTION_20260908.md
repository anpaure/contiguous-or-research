# All B/B placements miss 223; the pure pattern-2 obstruction

2026-09-08. Pure proof by ternary_lift, independently derived and audited
by root. No computation is a premise. The original fixed endpoint is
00112244 / 33776655 with its Singer translates and upper complements.
Infinity is global coordinate 0; cyclic labels 0,...,6 correspond to
global (1,2,4,3,6,7,5). All cyclic arithmetic is modulo seven.

## 1. No B/B placement can supply necklace 223

Use a short B/B representative with block orders (A,B,C,D)/(E,F,G,H),
meaning the literal words AABBCCDD / EEFFGGHH. Develop its fourteen-row
bundle under Singer and complementation. Require that its one-one
critical flags be distinct and avoid the fixed endpoint flags.

The endpoint-covered infinity-zero triple signatures and infinity-two
pair signatures, with the unique cyclic one normalized to zero, are

    F = {123,126,135,146,234,245,456},
    P = {16,35,25,26,45,56}.

If infinity occupies an interior block, the complementary-partition
proof in Q3_D8_SINGER_ONE_ONE_PROVIDER_FLAG_OBSTRUCTION_20260908.md
already shows that the bundle cannot supply infinity-one necklace 223.

For an endpoint block, exchange shores and complement if necessary to
put infinity at A. Its sole infinity-one critical flag has two-triple
EFG. Suppose its necklace is 223. Translate so that EFG = {0,2,4}.
The next flag (infinity,E,F;G) requires the pair {E,F}-G to avoid P.
Choosing G=2 or G=4 gives 25 or 35, respectively. Therefore

    G=0, {E,F}={2,4}.

The flag (infinity,E,F;B) now requires {2,4}-B to avoid P. Among the
remaining cyclic axes B in {1,3,5,6}, choices 3 and 6 give 16 and 35.
Thus B is 1 or 5. The flag (infinity,B,E;F) rules out B=1: its pair is
45 when (E,F)=(2,4), and 26 when (E,F)=(4,2). Hence B=5.

The three remaining axes C,D,H are {1,3,6}. The complemented critical
flag (CDH;B) then has normalized triple

    {1,3,6}-5 = {1,3,5},

which belongs to F. This contradicts endpoint avoidance. The endpoint
case is impossible too.

Consequently NO infinity position in a B/B bundle can supply the
223 infinity-one orbit while avoiding the original endpoint flags.
This strengthens the earlier interior-only statement. It is specific
to these endpoint words, and does not assert the same for other
endpoint decks.

## 2. Pure exclusion of amended provider pattern 2

Pattern 2 uses BB with infinity at an endpoint, BL with infinity on
an interior L axis, and BU with infinity at B's second block. These
are the literal profiles in
Q3_D8_SINGER_BB_BL_BU_AMENDED_PROFILE_LEDGER_20260908.md. The target
is an exact partition of the original endpoint's 26 residual
one-one critical flag orbits. Higher profiles supply no such flags.

The pure BU B-B endpoint/parity lemma in Sections 5--6 of that note
forces its odd complementary rank-four class to be 133. Its single
infinity-one flag has type 133,124,or142, and therefore cannot supply
223. The distinction between its odd class and its own infinity-one
class is essential here.

Orient BL so its fixed axis is F, writing

    AABBCCDD / EFEFGHGH,  F=infinity.

Its two odd complementary rank-four classes are the necklaces of AEG
and DGH. Quotient degree parity, using the endpoint's class 115 and
BU's class 133, forces these two classes to be {115,133}. BL has two
infinity-one flags, with two-triples ABE and DGH. The latter cannot
have type 115, already supplied by the endpoint. Thus DGH has type
133. The disjoint triples ABE and DGH cover six of the seven cyclic
axes. In the complete complementary-three-set necklace graph, a
133 triple can pair only with 124,142,or133, never 223. This is the
ten-partition table in Section 7 of the earlier one-one-provider note.
Hence BL cannot supply 223 either.

Section 1 excludes BB, and the preceding paragraphs exclude BL and
BU. The residual infinity-one 223 orbit is uncovered. Pattern 2 is
therefore impossible by a pure endpoint-only argument: no seed
central restriction, positive-weight cap, or finite catalogue is
needed. A literal missing target is

    (1,2,0,0,2,0,2,0).

The separately completed finite inventory agrees with this theorem:
Q3_D8_SINGER_BB_BL_BU_PROVIDER_INVENTORY_RESULT_20260908.md.
