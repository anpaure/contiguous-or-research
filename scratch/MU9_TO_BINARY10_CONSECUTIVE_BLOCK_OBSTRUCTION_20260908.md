# The cyclic mu(9) certificate does not complete the consecutive-block lift

2026-09-08. Cover-selectors derivation and one bounded h100 screen.
The variable-block obstruction and its reversal-invariant formulation
have passed direct-route's independent analytic audit. The stronger
three-hole argument below is due to that independent audit. No solver
or cyclic partition search was run for this note. Root integration audit
also passed. Subsequent local changes of the source cycle are separate
constructions and are not excluded by this result.

## 1. Literal source and row reconstruction

Use the parent pair envelope from
MATH_CERTIFICATE_CYCLIC_MU9_WIDTH126_20260907.md. Its seed is

    (3,18,130,258,264,72,96,36,33,48,24,272,144,192),

and A_(14t+i)=rho^(5t)(seed_i), for 0<=t<9, where rho rotates the
nine coordinate bits once. All indices are cyclic modulo126. The final
universal word replaces the first3 by1 in every developed seed; every
OR of at least two consecutive letters is unchanged. Put

    S_t=A_t union A_(t+1) union A_(t+2),
    U_t=A_t union ... union A_(t+3),
    V_t=A_t union ... union A_(t+4).

The S and U sequences are the exact126-element rank-four and rank-five
decks on {0,...,8}. All V_t have rank six. Introduce pivot z=9.

For a block of p successive S targets, starting at s, use a balanced
prefix row with pivot at left position p, 1<=p<=5:

    left=(a_1,...,a_(p-1),z,c_1,...,c_(5-p)),
    right=(b_1,...,b_5).

Let

    a_j=S_(s+j) minus S_(s+j-1),
    d_j=S_(s+j-1) minus S_(s+j),       1<=j<p,
    b_5=U_(s-1) minus S_s,
    K=intersection_(j=0)^(p-1) S_(s+j).

Every displayed difference must be a singleton. Row realizability also
requires the d_j to be distinct original S_s elements, the a_j to be
distinct and outside U_(s-1), and |K|=5-p. Then, and only then, the row
is reconstructed as

    right=(an ordering of K,d_(p-1),...,d_1,b_5),
    {c_1,...,c_(5-p)}={0,...,8} minus
                                  (U_(s-1) union {a_1,...,a_(p-1)}).

There are exactly ((5-p)!)^2 free row orders. Singleton differences
alone are insufficient: an entering coordinate may resurrect b_5.

For p=3 these formulas are exactly the proposed four-choice row:
b_4=S_s minus S_(s+1), b_3=S_(s+1) minus S_(s+2), and b_1,b_2=K.
Its no-z rank-four targets are S_s,S_(s+1),S_(s+2); its no-z rank-five
targets are U_(s-1),U_s,U_(s+1). This verifies the proposed derivation
with the necessary all-coordinate distinctness condition included.

More generally a valid block supplies exactly p no-z rank-four targets,
p no-z rank-five targets, and p-1 no-z rank-six targets. They are

    S_s,...,S_(s+p-1),
    U_(s-1),...,U_(s+p-2),
    V_(s-1),...,V_(s+p-3),                           (1)

respectively. To see the last line, a no-z rank-six target uses j left
coordinates and 6-j right coordinates, with 1<=j<p. It is the union
of the two consecutive assigned U targets U_(s+j-2),U_(s+j-1), hence
V_(s+j-2). Free permutations of K and the c's change none of (1).

## 2. One bounded necessary-condition screen

The independent script generated the parent envelope, checked that all
interval ORs of lengths2,...,126 agree with the final certificate, and
checked every block and every available four-way row order at each
fixed triple alignment. All execution was through ssh h100, hostname
arboghast; runtime was0.2620014562 seconds, with a10-second CPU cap.

| Triple offset e | Valid blocks out of42 | Actual row orders checked | Fixed no-z rank-six targets covered |
|---|---:|---:|---:|
| 0 |33|132|59 of84|
| 1 |33|132|59 of84|
| 2 |33|132|59 of84|

Even ignoring row realizability, the selected V positions cover only
65 of84 targets for each alignment. The invalid block starts have
residues6,10,13 modulo14. For example at s=6,

    S_6=101, S_7=53, S_8=57, U_5=109,

so a_2=3=b_5 as coordinate labels. This is a genuine shore collision.

The same small screen checked local realizability of all630 pairs(s,p),
without enumerating their free orders or selecting a partition. The
numbers of valid starts for p=1,2,3,4,5 are

    126,126,99,63,36.

The V target multiplicity inventory is54 targets occurring once,
18 occurring twice, and12 occurring three times. Thus126 occurrences
cover all84 rank-six targets. The full report is
MU9_BINARY10_PREFIX_BLOCK_SCREEN_20260908.json; the script is
screen_mu9_binary10_prefix_blocks_20260908.py, both in this directory.
The remote report remains at
/tmp/mu9_binary10_block_screen_20260908_cover_selectors/report.json.

## 3. Exact variable-block boundary problem

Partition the126 cyclic S positions into42 consecutive blocks with
lengths p in{1,...,5}. The first two lines of (1) automatically retain
the complete no-z S and U decks. There are84 retained V positions,
since sum(p-1)=126-42. Each block ending at the next boundary b drops
the single V position b-2. Thus the dropped positions form a cyclic
set D of42 indices whose consecutive cyclic gaps are the block lengths,
and in particular are at most5.

A necessary boundary CSP, before any free row-order choices, is:

1. Every selected block(s,p) satisfies the local row conditions above.
2. Its boundaries give a cyclic partition with42 blocks.
3. For every rank-six target v, exactly multiplicity(v)-1 of its V
   occurrences lie in D; equivalently one occurrence remains.

The first condition is irrelevant to the obstruction below: conditions
2-3 are already incompatible on this specific cyclic certificate.

Were these boundary conditions feasible, the remaining finite row CSP
would select one of ((5-p)!)^2 orders per block and require exact
coverage of the z-present ranks4,5,6. Removing z, these are respectively
all84 triples, all126 four-sets, and all126 five-sets on nine coordinates.
Every other rank would still need its literal full-cover check. This is
an exact finite prefix-row problem, not an inference from cyclic coverage.

## 4. A finite certificate forbids every such full rank-six lift

The first14 V masks, obtained directly from the literal seed, are

    (411,474,490,366,365,125,125,317,441,504,504,497,249,249).

Their canonical nine-rotation representatives are respectively

    (111,187,175,183,219,125,125,123,119,63,63,63,95,95).

All these orbits have size9 except219, which has size3. Consequently
the V positions14t+i with i in{0,1,2,3,7,8} are globally unique target
occurrences. The positions14t+4 are precisely ALL occurrences of the
three targets

    {219,365,438}.                                    (2)

Each target in (2) occurs three times. No other seed position belongs
to this rotation orbit.

Suppose all rank-six targets were retained. The four consecutive
unique occurrences14t,...,14t+3 cannot be dropped. Because consecutive
drops are at distance at most5, the two neighboring positions14t-1
and14t+4 must BOTH be drops: the nearest drops on either side already
have distance at least5, and equality is the only permitted possibility.
Thus every occurrence in (2) is dropped, a contradiction.

This proof is invariant under rotation, coordinate relabeling, and
reversal of the cyclic word. Reversing the word permutes the V indices
and reverses the cyclic drop order; consecutive drop distances still
are at most5. Both neighboring drops of a four-position forbidden run
must be used, so reversal does not escape the argument.

## 5. Stronger statement: at least three rank-six holes

No assumption that all globally unique targets survive is necessary
for the following stronger conclusion:

    EVERY consecutive-block lift on this cycle has at least THREE
    distinct missing no-z rank-six targets.           (3)

For each of the three periodic targets in (2), consider two cases.
If all its occurrences are dropped, charge that missing target itself.
Otherwise choose a retained occurrence x=14t+4. Every interval of five
consecutive V positions contains a drop, because drop gaps are at most5.
Since x is retained, some position in{x-4,x-3,x-2,x-1} is dropped.
That position is a globally unique occurrence, so its target is missing.

The charged holes are distinct. Charges that are periodic targets are
different from all unique targets. For two different retained periodic
targets, the chosen t values are different; the preceding four-position
runs are disjoint and consist of globally distinct unique targets.
This constructs three distinct holes and proves (3), in either orientation.

Thus this particular variable-block escape cannot produce an exact,
one-hole, or two-hole macro cover. This does not rule out an unrelated
42-row prefix bank, a different cyclic source, nonconsecutive grouping,
or an additional structured repair beyond this block construction.

## 6. Additional full-cube scope guard

With pivot fixed at p=3 in every row, no row supplies a z-present target
of rank1 or2, or a no-z target of rank8 or9. These are20 structurally
missing targets, independent of the critical-deck failures above.

Variable positions can avoid that particular defect, but a complete bank
must have n_1>=1 and n_5>=1, where n_p counts rows with pivot position p.
Rank-two and complementary rank-eight capacity also require

    2n_1+n_2>=9,       n_4+2n_5>=9.

Every42-row balanced prefix bank has exactly210 rank-four occurrences,
252 rank-five occurrences, and210 rank-six occurrences. These equal the
full ten-dimensional rank sizes. Therefore ALL three critical ranks
must be exact decks, with no repetitions or missing targets, in any
full42-row construction. The no-z S/U/V conditions alone would not
have established this.

All coverage claims here concern the designated36 prefix-union targets
of each macro row. They do not silently add the full complements of
those targets as a different macro coverage convention.
