# The proposed Singer central-line repair still forces too much overlap

2026-09-08. Pure audit by ternary_lift; no computation. The charge
and endpoint repair arithmetic is valid, but complement closure
forces an additional all-ones overlap that rules out the stated
2384 scheme. This concerns arbitrary copied-partner bijections,
not only translations in F_2^3.

## 1. The proposed actual rows

Let a Singer permutation S fix coordinate 0 and cycle the other
seven coordinates. A lower endpoint row uses shore ranks 0,...,7
on both four-coordinate chains, so its charge is 16. Require its
two copied shore words to start with a repeated axis, with one
first axis at coordinate 0 and the other nonzero. Developing under
S gives seven rows. The fixed first axis supplies both axis targets
at coordinate 0; the other first axis cycles through all seven
nonzero coordinates. The zero-zero cell supplies the global minimum.
The complemented seven-row upper orbit repairs all coaxes and the
global maximum. Their combined charge is 14*16=224.

Add 154 ordinary short rows, of charge 154*14=2156. The regular
balanced rows then have charge 2380. Finally add the literal line

    (0,1,2) on coordinate 0
      times the singleton all-ones vector on the other seven.

Its charge is 3+1=4. It covers exactly (0,1,1,1,1,1,1,1), the
all-ones point, and (2,1,1,1,1,1,1,1). These are the three central
S-fixed targets. The other six S-fixed cube targets are the bottom
and top corners and the coordinate-0 axes and coaxes, already
covered by the endpoint repair. Total charge is indeed 2384.

## 2. The critical occurrence ledger

Rank seven has 1016 points: one fixed point A_0, with its zero at
coordinate 0, and 145 seven-point S-orbits. The lower endpoint
orbit contributes 7*8=56 rank-seven occurrences, the upper orbit
7*6=42, and the short rows 154*6=924. Thus the regular bank has
1022 occurrences, or 146 units of seven.

If the regular bank avoids A_0, it has only one repeated unit among
the 145 nonfixed target orbits. The central line covers A_0 once.
By complement symmetry the same statement holds at rank nine.

A copied all-opening short row covers two seven-one targets: the
zero lies at the last-opened coordinate of either shore. If 0 is
not last-opened on its shore, both zeros are nonzero. Its seven-row
Singer orbit therefore covers the single nonfixed seven-one target
orbit twice. One such orbit already consumes the entire allowed
critical repetition. This observation is a necessary constraint,
not a claim that its other critical targets are eligible.

## 3. Every self-complementary seven-row short orbit is all-opening

Every ordinary short row has six distinct rank-seven targets. Its
Singer orbit cannot have size one: an S-invariant six-point set
could contain only fixed points, whereas rank seven has only one
S-fixed point. Hence every short row has a seven-row Singer orbit.

Suppose global value complementation preserves this orbit. Write
complement(R)=S^k R. Complementation commutes with S and is an
involution, so R=S^(2k)R. Since the orbit has size seven, k=0.
Thus R itself is complement invariant.

Projecting onto either of its given shores shows that each cropped
shore chain is complement invariant. The omitted rank-zero and
rank-eight states are fixed by the shore, so restoring them makes
the full chain complement invariant as well. Its step word must
therefore be a palindrome. Each of the four axes occurs twice;
each occurs once in the first half and once in the second. The
first four steps are all distinct. Both chains are all-opening and
the row contains the all-ones point.

This argument does not allow an extra non-all-opening self7 orbit.
All such self7 orbits necessarily have the same all-opening profile.

## 4. Complement parity forces at least fourteen all-ones rows

A Singer- and complement-closed short bank is a union of self7
orbits and distinct complementary pairs of Singer orbits, of size14.
Writing its row count as 7s+14g=154 gives s+2g=22, so s is even.

The endpoint repair words start with a repeated axis. Since partners
are copies, neither repaired orbit covers a seven-one target. The
central line supplies only the fixed seven-one target A_0. The
nonfixed seven-one targets must therefore be covered by short rows.
For copied partners, any row covering such a target has the
all-opening profile on both shores, hence contains all ones.

If the covering row belongs to a generic14 orbit pair, all fourteen
rows have that profile and contain all ones. If it belongs to a
self7 orbit, the even value of s forces at least one further self7
orbit, which is also all-opening by Section 3. Again at least
fourteen regular rows contain all ones. The central line raises
the all-ones load to at least fifteen.

In particular, the proposed 154-short-row decomposition into two
self7 orbits and ten generic14 bundles has this unavoidable problem,
even if exactly one self7 orbit was intended to be all-opening.

## 5. The exact projection waste contradiction

Use the balanced-row projection weight

    y(x) = (1/4) * #{a : sum_{i != a} x_i = 7},
    sum_x y(x)=2358.

Every saturated balanced row retaining ranks 1,...,7 on both shores
has y-charge equal to its actual charge, including the one-sided
endpoint rows here. The central line has y-charge

    1/4 + 2 + 1/4 = 5/2,

while its actual charge is 4. This distinction is necessary because
the balanced-row dual bound is not a uniform bound for unbalanced
line rows. For this specific proposed bank the exact identity is

    actual charge = sum_x y(x)*load(x) + 3/2.

If the bank covered the whole cube and had all-ones load at least
fifteen, the fourteen excess all-ones occurrences alone would have
weight 28. Its charge would be at least

    2358 + 28 + 3/2 = 2387.5,

strictly exceeding 2384. Equivalently, charge 2384 permits only
24.5 weighted duplicate load after the line's 1.5 charge deficit,
whereas all ones already consumes 28.

The actual endpoint restoration and the central line are valid.
The obstruction is to the stated Singer/complement-closed copied
short-bank ledger. Breaking complement closure, changing the row
budget, or using genuinely different shore profiles changes the
premises; none of those changes is constructed or tested here.
