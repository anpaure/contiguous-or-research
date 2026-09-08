# An actual twenty-target unbalanced patch saves one unit locally

2026-09-08. Author: appendix_a. Pure proofs and literal file inspection;
no mathematical execution, enumeration, or new search. Root and direct-route
full analytical audits passed, including the corrected reflected fiber
weights and the Section6 baseline-fit accounting.
No full-cube improvement is claimed.

## 1. Literal charge-nine patch and balanced lower bound ten

Use one coordinate for the chain

    C=(0,1,2,3)

and its complementary five coordinates for

    D=(11111,21111,22111,22211,22221).                (1)

Both are strict saturated chains. Their product T has twenty distinct
quaternary-six targets and actual charge 4+5=9.

The lower-middle projection

    y_7(x)=(1/3)*#{a:sum_(i!=a)x_i=7}

is valid for every balanced 3+3 row, by the elementary deletion test:
each of the three deleted coordinates on a fixed shore state fixes
at most one counterpart rank. It is NOT valid for unrestricted splits.

For (1), deleting the one-coordinate shore contributes four tests,
because exactly D's third state has rank seven. At its five successive
states, deletions on the other shore contribute 5,5,5,5,4 tests.
For example, D_k has k twos and 5-k ones; the required C coordinate
is 7-(5+k)+D_k(a), and is retained precisely when it lies in 0,...,3.
Therefore

    sum_(x in T)y_7(x)=(4+5+5+5+5+4)/3=28/3>9.      (2)

Every bank of balanced rows covering T, even if it covers additional
targets and overlaps, consequently has integer charge at least ten.
Thus (1) is an ACTUAL cheaper unbalanced cover of a concrete point
family, not just a column with a favorable rank count. Its coordinate
permutations and reflection give equivalent local patch primitives.

This does not produce a trade in an existing full cover: the critical
residual of removed rows must still be contained in the replacement
union. Covering T more cheaply does not imply that those removed rows
can be discarded or shortened.

The target contains the rank-eight point (3,1,1,1,1,1), and explicitly
joins its full first-coordinate fiber to a five-state monotone progression
through the binary-valued interior of the other coordinates. This is
the local geometry to test against an actual baseline residual.

## 2. What the projection counterexample does and does not say

Reflection gives the analogous failure for deletion rank eight.
The reflection average of the two projections has row load 17/2
on T, below nine; (1) does not refute that averaged weight.
Its total cube weight is 1240, since the central five-coordinate
quaternary ranks each have size

    [t^7](1+t+t^2+t^3)^5 = binom(11,4)-5binom(7,4)=155.

The existing exact unrestricted optimum 1248 remains valid. In
particular, a proof that the single-rank ternary projection extends
unchanged to all q-ary support splits is impossible.

## 3. Exact cost relative to the existing optimal dual

The saved universal quaternary dual in
`qary_dual_verify_20260906_c52e9.cpp` has the following compact expression.
Let R=sum x_i and n_j=#{i:x_i=j}. Its value is

    R=7:  (n_0-1)_+/2;
    R=8:  (12+n_3-2n_0^2)_+/12;
    R=9:  (n_1+n_2)/12;
    R=10: (12+n_0-2n_3^2)_+/12;
    R=11: (n_3-1)_+/2;
    otherwise zero.                               (3)

This formula is an algebraic rewriting of the saved histogram table.
For example, at rank ten the identity n_2+2n_3-n_0=4 lists the possible
histograms; their table numerators are (12+n_0-2n_3^2)_+. Rank eleven
similarly gives 6(n_3-1)_+, and reflection handles ranks seven and eight.
The central table is n_1+n_2. This rewriting is not a new analytic
proof of the universal row inequality: that premise remains the
already verified exact all-chain certificate.

The twelve-scaled dual loads of T's five successive D fibers are

    13,17,28,28,17.

The reflected histogram (0,4,2,0) has scaled weight twelve, because
its canonical representative is (0,2,4,0). It occurs once in each
of the second and third fibers and is included in the displayed loads.
Thus T has optimal-dual load 103/12 and row slack 5/12. It is close
to, but not tight for, the true optimal dual. A full cover of charge
at most1260 can contain at most twenty-eight such row occurrences:
the total row slack plus weighted overcoverage budget is only
1260-1248=12. This is a restriction on how often the primitive can
be used, not a prohibition on using it.

## 4. Existing baseline scope before attempting an embedding

The five inflated binary rows give eighty paired rows of charge1280.
For each ordered triple their four actual shore chains are

    A=000 100 200 300 310 320 330 331 332 333,
    B=001 101 201 301 311 321 322 323,
    C'=010 110 210 220 230 231 232 233,
    D'=011 111 211 221 222 223.

Their lengths are10,8,8,6. Each binary row pairs all sixteen combinations,
at charge256. The ordered shore splits are

    012|345, 124|350, 143|520, 041|235, 423|501.

The archived finite fourteen-seed pool had no 1+5 primitive of type (1).
However, the later result
`Q4_ALTERNATIVE_SPLIT_TWO_RECTANGLE_REDUCTION_20260907.md`
already checks arbitrary replacement support pairs and proves support
rigidity for every two-row residual not excluded by the dual. Its
combination with the separately reported original-slot cost checks closes
two-to-two improvements of that saved baseline. The private-core theorem
in `Q4_PAIR_COALESCENCE_CERTIFICATE_20260907.md` also rules out every
many-to-one improvement. The new local primitive does not evade either
statement merely by having an unbalanced split.

A useful embedding therefore needs a genuinely larger residual trade
or coordinated chain recombination. No such embedding has yet been
proved in this note, and no old integer search was retried.

## 5. The five shortest rows cannot finance any repair saving

In every baseline binary row the shortest paired rectangle is D'×D',
where

    D'=(011,111,211,221,222,223).

Index these six states by 0,...,5. The only nonzero entries above
the diagonal of its twelve-scaled optimal-dual weight matrix are

    (0,4):10, (0,5):4, (1,3):12, (1,4):6,
    (1,5):10, (2,3):6, (2,4):12.

The only nonzero diagonal entries are (2,2):12 and (3,3):12.
Reflection across the matrix diagonal supplies the remaining entries.
Thus its dual mass is

    (2*(10+4+12+6+10+6+12)+12+12)/12=12,

equal to its actual charge.

The threshold-bit ranks of D''s six states, for the cut at two, are
0,0,1,2,3,3. Every positive matrix entry above has total threshold
rank two, three, or four. The five-row binary template covers those
three ranks exactly once: its total occurrences there are15,20,15,
equal to the corresponding Boolean layer sizes. Within each such
binary row, the four explicit shore chains partition its staircase.
Consequently EVERY positive-dual target in a D'×D' row is globally
private to that one physical baseline row.

Remove any subset of the five shortest rows while keeping all other
baseline rows. The resulting required residual contains the entire
positive-dual mass of every removed row, without overlap between them.
Its mass is therefore at least twelve times the number of removed
rows, exactly their old total charge. The universal dual implies
that ANY replacement cover has at least that charge, regardless of
its support splits, number of rows, skips, or extra covered points.

Thus coordinated trimming or replacement confined to these five
rows cannot improve the baseline. The charge-nine primitive remains
valid, but an improving embedding must also remove or modify rows
with positive credit in the exact Section5 ledger of
`Q4_ALTERNATIVE_SPLIT_TWO_RECTANGLE_REDUCTION_20260907.md`.
This is a local obstruction to the proposed shortest-core trade,
not a lower bound1280 for arbitrary full covers.

## 6. The patch's heavy target raises the minimum trade neighborhood

This section uses the existing exact private-credit census and matching
from Section5 of
`Q4_ALTERNATIVE_SPLIT_TWO_RECTANGLE_REDUCTION_20260907.md`;
it does not re-enumerate or re-price baseline rows. Write all dual
quantities in twelve-scaled units. For removed rows J, that result gives

    available credit C(J)=6n_6+16n_16+19n_19-13e,

where e counts completely removed owner pairs in an eight-edge matching.
The largest credit among k removed rows is

    T(k)=19k                         for0<=k<=8,
    T(k)=152+16(k-8)                 for8<=k<=18.

A saving of b in an actual repair leaves at most C(J)-12b units
for new-row slack, weighted repetitions inside the residual, and
new incidences on points still covered by retained rows.

Every coordinate permutation of patch (1), with free axis a, contains

    x_a^+=(3 at a, one at every other coordinate).

Its optimal dual weight is13/12. The threshold mask of this target is
the singleton {a}, so its old owners are exactly the binary rows with
a first on one of their shores. The five first-axis pairs are

    {0,3}, {1,3}, {1,5}, {0,2}, {4,5},

forming the path2--0--3--1--5--4. In each owner the actual shore
states are B's311 and D''s111. Thus an internal path axis has two
owners, while a=2 or4 has one owner.

These owners have precisely the credits in the saved ledger. Each
B/D row has raw scaled slack six: row14 is a literal B/D row, and
its credit19 minus its one shared positive target of weight13 is six;
coordinate symmetry gives the same raw slack to every B/D row.
Such a row contains only one target of the displayed x_a^+ form and
no reflected target x_b^-=(0 at b, twos elsewhere). Consequently the
two-owner case is one of the matched credit19 pairs; the unique
owner has credit six.

For reflected patches the same argument uses the five last-axis pairs

    {2,5}, {4,0}, {3,0}, {1,5}, {3,1},

forming the path2--5--1--3--0--4. The conclusion is identical.

The four internal first-axis heavy targets and four internal last-axis
reflected heavy targets yield eight disjoint owner pairs. Each already
contributes weight thirteen, so they exhaust the saved eight-edge
positive-overlap matching. Thus the unique-owner B/D rows have no
other positive shared target, justifying their credit six directly.

If even one old owner of the patch's heavy target remains, that target
lies outside the repair residual. The new patch therefore incurs at
least thirteen units of extra incidence as well as its own five units
of row slack: a total unavoidable expenditure of eighteen units.
If all old owners are removed, that extra incidence is avoided, but
the removed set must contain either a whole matched pair or a credit-six
row. This reduces the maximum possible available credit.

In particular:

* Six removed rows have C(J)<=114. Saving nine to reach1271 leaves
  at most six units, too little for eighteen. Removing every heavy-target
  owner instead gives C(J)<=6*19-13=101, or6+5*19=101, below the
  108 units needed even before paying new-row slack. Thus NO six-row
  trade reaching1271 can contain any coordinate-permuted or reflected
  copy of (1).
* Fourteen removed rows have C(J)<=248. Saving twenty to reach1260
  leaves at most eight units, again below eighteen. If all owners are
  removed, the maximum is238: a whole matching pair has marginal
  credits19 and6, replacing a marginal16 by6 in the optimal selection;
  a required unique-owner credit-six row has the same effect.
  This is below the required240. Thus NO fourteen-row trade reaching1260
  can contain such a patch.

Therefore use of this primitive raises those necessary neighborhood
sizes to at least seven and fifteen, respectively. At seven rows and
target1271 it leaves at most seven scaled units for every other new-row
slack and excess incidence: either133-108-18=7 with an old owner
retained, or120-108-5=7 after all owners are removed.

For example, the old targeted six-row set
{14,15,26,27,46,47} would need at least a seventh modified row to
use the primitive in a saving-nine repair. Adding row29 completes
the heavy-target owner pair(14,29) and gives a concrete seven-row
neighborhood consistent with this necessary budget. It does NOT give
replacement chains or prove that the residual can be covered at the
budget. No model on this neighborhood was run.

The obstruction concerns embedding this particular useful local patch
into the fixed baseline. It neither excludes larger coordinated trades
nor proves integral optimality1280. A literal improving trade remains
unconstructed.
