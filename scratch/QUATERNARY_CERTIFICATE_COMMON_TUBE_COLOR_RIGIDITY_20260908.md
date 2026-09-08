# The actual charge-1248 tube catalogue has no nonconstant common lane color

2026-09-08. Pure finite proof; no mathematical computation or search.
Author: appendix_a. Root full analytical audit and direct-route full
independent source/proof audit passed.

This note concerns the specific denominator-15 quaternary certificate
in `q4d6_fractional_template_20260906_c52e9.py`, using the standard
tube partitions from Sections 2–3 of
`QARY_TUBE_AMPLIFICATION_AND_FINITE_GATE_20260906_c52e9.md`.
It strengthens the archived universal-common-selector warning to this
actual finite catalogue. It does NOT exclude separate Latin colors on
left and right lanes, arbitrary correlated edge selections, or a new
chain repartition.

## 1. Regular edge selection has the proposed charge identity

For one template C×D with shore dimensions r,s and r+s=6, the standard
tube families have m^(r-1) left lanes and m^(s-1) right lanes. Their
memberships sum to |C|m^r and |D|m^s, respectively.

Suppose a selected bipartite graph gives every left lane the same
degree p·m^(s-1) and every right lane degree p·m^(r-1), with these
degrees integral. Its exact principal charge is

    p·m^(s-1) sum_left |F| + p·m^(r-1) sum_right |G|
              = p(|C|+|D|)m^5.                         (1)

Thus the proposed degree-regular selection really does scale charge
by p, despite unequal lane lengths. This calculation does not assert
that the selected pairs cover any particular fine point or the
required fraction of each macrocell.

Develop the fourteen certificate seeds under all six-coordinate
permutations and simultaneous reflection. The indexed group has size
1440. A developed copy of seed i has prescribed weight n_i/21600,
where n_i is its listed numerator. If compatible regular selections
at these fractions existed and covered every fine target, (1) would
give charge 1248m^5. The missing issue is compatibility, not the
charge identity.

## 2. Exact common-color rigidity for this catalogue

Let Omega=[4m]^6. A common lane color means a function

    chi: Omega -> K

to any set K which is constant on EVERY candidate fine rectangle
in the standard tube family of EVERY developed seed. It may depend
arbitrarily on both the macrocell and the microcoordinates; no
linearity, periodicity or symmetry is assumed.

**Theorem.** Every such chi is constant on Omega.

The first certificate seed consists of the full saturated chains

    C: 000 100 110 111 211 221 222 232 233 333,
    D: 000 001 002 003 013 023 033 133 233 333.            (2)

In their initial macrocell, both tube routings go straight through:
the initial incoming and outgoing axes are the first path axes,
as prescribed by the standard tube construction. The first shore
therefore consists of all parallel fine lines in its first axis,
and the second shore of all parallel lines in its first axis.
Their products are all two-dimensional coordinate planes in the
zero macrocell [m]^6, with the other four coordinates fixed.

The coordinate-permutation developments of (2) realize every choice
of two distinct active axes. Constancy on these planes forces chi
constant on [m]^6: any coordinate step lies on one such plane, and
any two points of the microcube can be connected by coordinate steps.
Call the resulting color c.

Every fine lane in a tube partition has a nonempty piece in every
macro vertex of its defining chain. Every fine pair of any developed
copy of (2) consequently meets the zero macrocell: these two full
chains contain their minimum even after reflection and reversal.
Its color must be c. Hence chi=c on the complete blown-up support
of every developed copy of (2).

To propagate this to the other seeds, only their displayed first
point before development is needed. The following table lists its
two shore states and number k of one-valued coordinates; all its
other coordinates are zero. Seed numbers are one-based in the
certificate source.

| Seed | Left state | Right state | k |
|---:|---|---|---:|
| 1 | 000 | 000 | 0 |
| 2 | 000 | 000 | 0 |
| 3 | 110 | 011 | 4 |
| 4 | 00 | 0111 | 3 |
| 5 | 00 | 0111 | 3 |
| 6 | 000 | 001 | 1 |
| 7 | 000 | 001 | 1 |
| 8 | 010 | 001 | 2 |
| 9 | 010 | 001 | 2 |
| 10 | 100 | 001 | 2 |
| 11 | 00 | 0001 | 1 |
| 12 | 011 | 011 | 4 |
| 13 | 000 | 011 | 2 |
| 14 | 010 | 000 | 1 |

The first seed itself contains representatives of all five relevant
histograms (6-k,k,0,0), k=0,...,4, namely

    (000,000), (000,001), (100,001),
    (110,001), (111,001).                              (3)

Coordinate permutations cover every point of each such histogram;
the reflected developments cover their reflected histograms as well.
Consequently the distinguished point of EVERY developed seed lies
in an already c-colored macrocell. This remains true after reflection:
the distinguished point may cease to be the first chain point, but
is still one of its macro vertices.

Every candidate fine rectangle of that developed seed has a
nonempty piece in the distinguished macrocell. It must therefore
have color c on its entirety. This propagates chi=c to the full
developed catalogue. Its union covers [4]^6, since the verified
fractional certificate has positive coverage of every macro target;
the complete tube families cover their blown-up supports. Thus
chi=c on Omega, proving the theorem.

## 3. Scope of the obstruction

This excludes a nonconstant shared phase function that would make
all candidate tube rectangles monochromatic, including a phase
function adapted to the actual quaternary catalogue and allowed to
change from one macrocell to another. The argument does not rely
on a universal pool of all possible coordinate-plane rectangles.

It does NOT cover a Latin subgraph rule of the form

    select (F,G) according to separate left/right lane colors,

because those colors need not induce one consistent function chi
on all fine targets. Nor does it exclude choosing a smaller subset
of monochromatic candidates after a color function is chosen; the
theorem's hypothesis concerns every candidate in the specified
catalogue. The regular-degree identity (1) by itself provides no
common color and remains valid.

The separate concrete counterexample in
`CORRELATED_FRACTIONAL_TUBE_SELECTION_CYCLIC_OBSTRUCTION_20260908.md`
does allow arbitrary row-dependent whole-pair selections in its
own binary three-axis instance. Neither result supplies an
impossibility proof or a compatible integral realization for the
specific charge-1248 quaternary bank. That selected-pair or
repartitioned-chain construction remains open.
