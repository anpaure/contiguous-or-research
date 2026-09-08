# Finite grid-chain certificates inflate to asymptotic staircase chains

2026-09-08. Pure constructive proof; no computation. Full root and independent
appendix-a audits PASS, including the arbitrary-comparability extension
below. The lemma converts a finite chain partition into an actual chain
partition after uniformly enlarging every coordinate interval. Unit
macro steps give saturated chains after inflation, but the compiler
also permits the increasing chains obtained from general macro jumps.
The lemma does not require the finite poset to be Sperner.

## 1. A cube can be traversed between any two prescribed coordinate faces

Use integer coordinates `0,...,m-1`. For any two coordinate indices
`a,b` in `{1,...,d}`, the cube `[m]^d` has a partition into exactly
`m^(d-1)` nonempty increasing saturated paths with the following properties:

- their initial points are precisely the points on the face `x_a=0`;
- their final points are precisely the points on the face `x_b=m-1`.

Each point on either face occurs once as the corresponding endpoint.

If `a=b`, take the straight paths parallel to that coordinate. If `a!=b`,
fix all other coordinates and partition the `(a,b)` square into the
following `m` paths, for `j=0,...,m-1`:

    (0,j),(1,j),...,(m-1-j,j),
                 (m-1-j,j+1),...,(m-1-j,m-1).       (1)

The first segment includes its turning point and the second does not.
A point `(x,y)` belongs to exactly the path

    j=min(y,m-1-x).

Thus (1) is a literal partition. Its starts are `(0,j)`, and its ends
are `(m-1-j,m-1)`. Tensoring with the fixed other coordinates proves
the assertion. The intersection of the two specified faces causes no
problem: the path at their corner is a singleton. The case `m=1` is
also a singleton in every fixed slice.

## 2. Inflation of one saturated macro chain

Let `P` be any finite subset of an integer product grid. Suppose it has
a partition into `R` chains, each of whose successive points differ
by increasing ONE coordinate by ONE. This is the required meaning of
"saturated grid chain"; an arbitrary comparability-chain partition is
not being assumed to have this property.

For a positive integer `m`, replace each macro point `x` by its cell

    B_x={m*x+y : y in {0,...,m-1}^d},

and write `P[m]` for the disjoint union of these cells. Then

    P[m] has a partition into exactly R*m^(d-1)
    increasing saturated chains, with |P|*m^d members.             (2)

**Proof.** First take one macro chain `x^(1),...,x^(L)`. A transition
to the next macro point uses one coordinate direction. In each cell
prescribe its entry face to be the minimum face in the preceding
transition direction, and its exit face to be the maximum face in the
following transition direction. At the first and last cells, the
unconstrained entry or exit direction can be chosen arbitrarily. For
a one-cell macro chain choose the same direction for both faces.

Apply Section 1 inside each cell. For consecutive macro cells whose
transition is in direction `a`, every point on the first cell's exit
face pairs uniquely with the point on the next cell's entry face having
the same remaining coordinates. Their actual coordinates differ by
exactly one in direction `a`. Join the corresponding paths through
this cover edge.

All exit points and entry points are used once, so the joins form a
bijection of the `m^(d-1)` paths between consecutive cells. They create
neither branches nor identifications. After all joins there are exactly
`m^(d-1)` chains, and they partition all `L*m^d` points of the macro
chain's cells. Singleton paths at face intersections simply connect an
incoming edge to an outgoing edge at that point. Different macro chains
have disjoint cells; applying the construction to each proves (2).

Every asserted chain comparison holds in the ambient coordinate order.
The result therefore remains valid when increasing coordinates index
ascending set chains on disjoint supports. Square.

**Extension to arbitrary macro comparabilities.** Formula (2) remains
valid if each macro chain is merely strictly increasing componentwise.
Its inflated chains need not be saturated at the joins. For a jump
`x<y`, choose any coordinate `a` with `y_a>x_a`, prescribe the exit and
entry faces in direction `a`, and match all other residual coordinates
as before. The joined points differ by

    m*(y_a-x_a)-(m-1)>=1        in coordinate a,
    m*(y_i-x_i)>=0             in every coordinate i!=a.

They are therefore strictly comparable in the required direction.
All within-cell partitions, endpoint bijections and disjointness
arguments are unchanged. Thus any explicit finite chain partition can
be inflated; unit grid steps are needed only for the stronger saturation
assertion, not for the word compiler or the chain-count bound.

## 3. Application to one displaced threshold in the fourteen-row bank

Fix a finite positive integer `s0`, put `a=2*s0`, and choose an integer
cut `u` with `1<=u<a`. For `p=1,...,4`, let `P_p(s0,u)` be the four-axis
staircase on `{0,...,a-1}^4` whose threshold bits are nonincreasing,
whose cut in position `p` is `u`, and whose other three cuts are `s0`.
Let

    Q_p(s0,u)=P_p(s0,u) x {0,...,a-1}.                (3)

Suppose actual finite saturated-grid-chain partitions of these four
five-dimensional posets have been supplied, with chain counts `W_p`.
Apply (2) with `d=5`. Inflating every cell by `m` gives EXACTLY the
staircase with axis lengths `2*s0*m`, displaced cut `u*m`, other cuts
`s0*m`, and additional chain length `2*s0*m`. It has a literal partition
into `W_p*m^4` chains.

The ordinary opposite four-axis staircase has the accepted hook
partition into `(s0*m)^3` chains, with `5*(s0*m)^4` members. Write
`Delta=u-s0`. Splitting the displaced staircase into its five disjoint
threshold boxes gives exactly

    |P_p(s0,u)|=5*s0^4+(2*p-5)*Delta*s0^3,
    |Q_p(s0,u)|=2*s0*|P_p(s0,u)|.                  (4)

Indeed `p` boxes use the low length `u`, and `5-p` boxes use the high
length `2*s0-u`, with the other three lengths equal to `s0`.

Absorb the ninth equal coordinate into the shore containing the displaced
principal axis. This choice can be made separately in each paired row.
The paired principal charge of row position `p`, after inflation, is

    [ s0^3*|Q_p(s0,u)| + 5*s0^4*W_p ] * m^8.       (5)

This uses the actual chain partitions: membership times the opposite
chain count, plus opposite membership times this chain count. It is an
upper charge, not a rank-polynomial lower bound.

For coordinate zero of the fixed fourteen-row bank, its position counts
are `(n_1,n_2,n_3,n_4)=(4,1,7,2)`. They satisfy

    sum_p n_p=14,       sum_p n_p*(2*p-5)=0.

Consequently the total of (5) is

    [ 140*s0^8 + 5*s0^4*(4*W_1+W_2+7*W_3+2*W_4) ] * m^8.         (6)

The existing equal-cut charge is `280*s0^8*m^8`. Thus the finite,
integer sufficient criterion for a STRICT principal improvement is

    4*W_1+W_2+7*W_3+2*W_4 < 28*s0^4.             (7)

Coverage remains the same fourteen-row threshold-cover argument: the
displaced coordinate has the SAME cut in every occurrence, so its
low/high bit is consistently defined across the bank. Assigning the
extra ninth coordinate to either shore does not change this coverage.

## 4. Scope of a successful finite certificate

A supplied partition meeting (7) would prove an asymptotic principal
charge improvement for these equal-length nine-axis products, by a
literal construction. No asymptotic Sperner or normalized-matching
theorem would be needed. The finite partition should record all its
chains, or a matching whose successor edges are checked to be strict
componentwise comparisons. Unit grid-cover edges additionally certify
saturation. The inflation then requires no additional search.

A full coefficient improvement for the original unequal-chain compiler
still requires its length-dependent switching and probability ledger.
This note does not supply that ledger, assert that (7) has been met, or
turn a matching lower bound into a chain partition. In particular, a
maximum-rank count without a supplied chain partition is insufficient.

Padding all axes to a convenient multiple may be handled separately;
it is not needed for the exact identity at lengths `2*s0*m` above.
