# Weighted tube widths do not improve the saved bank by deletion or separate staircase repair

2026-09-08. Pure geometry and inspection of existing literal data; no
mathematical program, search, or new certificate execution. This note
uses Sections1–6 of
`QARY_TUBE_AMPLIFICATION_AND_FINITE_GATE_20260906_c52e9.md` and the saved
private-core certificate. It proves scoped obstructions to concrete
coverage-preserving modifications, not a lower bound for all weighted
templates. Root read and independently checked the complete geometric
arguments, bounds, and certificate scope: analytical audit PASS. The
literal-bank inspection is recorded in Section1; existing finite
certificates were used as previously audited, without reexecution.

## 1. The weighted coefficient and the existing literal banks

For a three-coordinate macrochain C, the exact tube-width coefficient
rho(C) is1 if any consecutive step changes only one coordinate. Otherwise
rho(C)=1-1/(4L), where L is the longest identical two-coordinate-change
run measured in cells, with L=1 if there is no such run. In particular

    3/4 <= rho(C) <= 1.

A jump of size two or three in only one coordinate still gives rho=1.
Merely inserting some multi-coordinate jumps is insufficient: every
remaining step must change at least two coordinates to obtain rho<1.

The literal first two states of all160 shores in the saved integral
`q4int_final1280_witness_20260906_f7a91.json` were inspected. Every pair
differs by a unit step in exactly one coordinate. Consequently every
shore has rho=1, and its actual weighted charge remains

    Mhat=sum_rows(|C|rho(D)+|D|rho(C))=1280.         (1)

Thus the refined width compiler gives the old(5/4)beta7 coefficient
for this bank, not a record improvement.

The same applies to both explicit quaternary fractional certificates:
the14-type denominator15 certificate and the15-type balanced denominator119
certificate. Every three-coordinate chain there has at least six states.
Indeed any chain in[4]^3 with no one-coordinate step has at most five
states, since each step increases rank by at least two but the total rank
span is at most nine. Hence all their three-shore rho factors are1 too.
Their weighted charge is still1248, and their multiplicities remain
fractional; they cannot be inserted into the literal integral compiler.

For comparison, the saved ternary fractional certificate has one
singleton-by-singleton row. Its weighted charge changes from306 to611/2;
all other listed three-shores have a one-coordinate step. This is only
the value of that fractional certificate, not a weighted optimum or an
integral cover. Even its normalized value611/486 exceeds5/4.

## 2. Pure macro-state deletion is impossible in the saved80-row bank

For a saved row Ri=Ci x Di, let Pi be its globally private target set.
The exact existing certificate
`Q4_PAIR_COALESCENCE_CERTIFICATE_20260907.md`, Section3, proves

    projection_left(Pi)=Ci, projection_right(Pi)=Di,

and that Pi has conflict graph K3,3 on the original support split.
This is a previously checked finite certificate; it was not rerun here.

Suppose each saved row is replaced by subchains Ci' subset Ci and
Di' subset Di, without adding new coverage outside those old rows.
Every point of Pi must still be covered by row i: it belonged to no
other old row, and shrinking the others cannot add it. Projecting gives
Ci'=Ci and Di'=Di. This holds simultaneously for all80 rows, not only
for one isolated deletion.

The same private-core property rules out a weighted saving by one
containing replacement rectangle. It forces the old support split and
both entire old chains into that rectangle. Their old unit-step pair
has no intermediate grid point, so it remains a consecutive
one-coordinate step in every containing chain. Its rho remains1.
The saved many-to-one obstruction therefore still applies under the
weighted objective.

This does not exclude replacement by several new rectangles sharing
different parts of the old private targets. It does show that creating
jumps by deleting allegedly redundant states from the present rows is
not a legal coverage-preserving move.

## 3. Splitting a chain while keeping all pairings does not help

There is an exact coverage-preserving way to create jumps: partition a
chain C into nonempty subchains C1,...,Ck, and pair every piece with the
unchanged D. It covers C x D exactly. But for k>=2 and a three-coordinate
C with rho(C)=1, its weighted charge is

    |C|rho(D)+|D|sum_i rho(Ci)
      >= |C|rho(D)+(3k/4)|D|
      >= old weighted charge+|D|/2.               (2)

Allowing overlapping subchains cannot improve this bound, since total
membership only increases. Thus this particular guaranteed-coverage
method for producing multi-coordinate jumps is strictly worse. It must
not be confused with a replacement that also changes the right-hand
pairings and redistributes targets among different old rows.

## 4. Exact obstruction to arbitrary separate repair of each binary ancestor

There is a stronger obstruction for the canonical1280 bank obtained by
inflating the five binary six-axis rows. This canonical construction is
the explicit one in `q4d6_fractional_template_20260906_c52e9.py` under
`check_integral_baseline`; it is distinguished here from any later
equal-cost incumbent changes.

Let X_m be one of its three-axis staircase shores after inflation to
alphabet[4m]. It is the union of the four disjoint cubes of side2m
whose binary addresses are000,100,110,111. Thus

    |X_m|=32m^3.                                  (3)

Its first two cubes contain the entire box[4m] x[2m] x[2m]. The points

    (4m-2-y-z, y, z), 0<=y,z<2m,

form an antichain of size4m^2 in this box. The usual staircase hook
partition gives4m^2 chains, so the exact width of X_m is4m^2. Only the
explicit antichain lower bound is needed below.

For any finite shore sets X,Y and antichains A subset X,B subset Y,
assign to points of X x Y the weight

    w(x,y)=1_A(x)+1_B(y),

and assign zero elsewhere. Any strict chain-pair row C x D on that
fixed support split has total weight at most|D|+|C|: each projected
chain meets its corresponding antichain at most once. This remains
true if the row contains extra points outside X x Y. Therefore every
such cover of X x Y has principal charge at least

    |A||Y|+|B||X|.                                (4)

Take X,Y to be the two staircase shores of one binary ancestor and use
the displayed size4m^2 antichains. Equations(3)–(4) give the exact bound

    principal charge >=256m^5.                    (5)

The standard construction attains it. Consequently no arbitrary new
chain partition, nonsaturated stitching, or altered pairing on that
same support split can improve this ancestor while still covering its
entire X_m x Y_m. In particular it cannot do so by optimizing rho factors:
the actual fine-grid antichain-product bound already charges all of
those widths.

If the five ancestors are repaired separately and every replacement row
is charged to its own ancestor, their total is at least1280m^5. This
includes every independent macro-shore repartition followed by the
improved tube compiler. It is an exact geometric obstruction, not a
failure of a width search or a flat fractional lower certificate.

The word "separately" is essential. A row jointly serving two ancestor
families, a changed support split, or an assignment that ceases to cover
each whole ancestor individually is outside this bound. Deduplicating
rows across ancestors is also such a joint modification and is not
excluded by summing(5).

## 5. Bounded conclusion

No actual record improvement follows from weighting the known integral
bank. The concrete moves audited here are closed: deleting old states,
splitting one shore while retaining all its pairings, and independently
recompiling each full canonical binary ancestor. The last obstruction
holds at every fine scale and permits arbitrary nonsaturated replacement
chains on the fixed split.

A successful weighted template would have to prove a genuinely joint
coverage change beyond these moves, with its private targets and all
other targets assigned to actual new rows. No such construction is
asserted, and no fractional multiplicity has been treated as integral.
