# Explicit antipodal tag cycles with injective half-distance shadows

2026-09-07. Root construction; pure proof, no computation.
The permutation, cycle-length, geodesic and shadow claims below passed
an independent root-agent audit. No publication-priority claim is made.

For every power of two d>=1 there is an explicit permutation F_d of
the binary cube {0,1}^d with the following properties:

1. Every step changes one bit; every cycle has length exactly 2d.
2. F_d^d(x)=bar(x), so every d consecutive steps are a geodesic to
   the bitwise complement.
3. For d>=2 and 1<=s<=d/2, both endpoint-shadow maps in Section 3
   are injective on all 2^d starting tags.

This is an abstract finite tag object, not an OR word covering the full
Boolean lattice. In particular the covered middle family below consists
only of transversals of d fixed coordinate pairs.

## 1. Recursive permutation

Let F_1 flip its one bit. If F_d is defined, write a 2d-bit word as
(x,y), with x,y in {0,1}^d, and set

    F_(2d)(x,y) =
       (F_d(x), y)   if |x|+|y| is even,
       (x, F_d(y))   if |x|+|y| is odd.                 (1)

Here |x| is Hamming weight. Each step flips one bit and hence reverses
total parity. The inverse is unique: at an odd-parity output apply
F_d^(-1) to its first half; at an even-parity output apply it to its
second half.

Directly,

    F_(2d)^(2t)(x,y)=(F_d^t(x),F_d^t(y)).              (2)

For 2t+1 steps, the two exponents are (t+1,t) for even input parity
and (t,t+1) for odd input parity. Equation (2) gives

    F_(2d)^(2d)(x,y)=(bar(x),bar(y)),
    F_(2d)^(4d)(x,y)=(x,y).                           (3)

Inductively every cycle length divides 4d but not 2d. Since 2d is a
power of two, the only such divisor is 4d itself. This proves the
cycle-length claim in dimension 2d; dimension one is immediate.

A path of exactly d one-bit steps from x to bar(x) must change every
coordinate once. Thus every segment of length at most d in these
cycles is geodesic. The same holds starting at any cycle position.

## 2. Ternary erasure patterns

For 0<=s<=d define E_(d,s)(x) in {0,1,*}^d by putting a star in each
coordinate changed between x and F_d^s(x), and the original bit x_i
in each unchanged coordinate. Geodesicity gives exactly s stars.

The map E_(d,0) is the identity. We prove by induction, beginning at
d=2, that E_(d,s) is injective for all 1<=s<=d/2.

In dimension two, F_2 has the cycle

    00 -> 10 -> 11 -> 01 -> 00.

Its four one-step erasure patterns are (*,0), (1,*), (*,1), (0,*),
which are distinct.

Now consider dimension 2d, d>=2. For s=2t, equation (2) gives

    E_(2d,2t)(x,y)=(E_(d,t)(x),E_(d,t)(y)).

If s<=d, then t<=d/2, so the two halves are separately invertible by
the induction hypothesis, including t=0.

For s=2t+1, the pattern is either

    (E_(d,t+1)(x),E_(d,t)(y))

or the version with exponents interchanged. Its two star counts are
(t+1,t) or (t,t+1), so the pattern identifies which case occurred.
Since 2t+1<=d and d is even, t+1<=d/2. Both halfwords are therefore
recovered uniquely by induction. This proves the claim through the
inclusive endpoint s=d/2 in every allowed dimension.

## 3. Injective intersections and unions of paired-coordinate tags

Introduce 2d distinct coordinates u_(i,0),u_(i,1), 1<=i<=d. For a
binary word x define its d-element transversal

    T_x={u_(i,x_i):1<=i<=d}.

For 1<=s<=d/2,

    x -> T_x intersect T_(F_d^s(x)),
    x -> T_x union T_(F_d^s(x))                       (4)

are injective. Indeed the intersection has neither coordinate from a
starred pair and the original singleton from an unstarred pair. The
union has both coordinates from a starred pair and the original
singleton from an unstarred pair. Either set therefore recovers
E_(d,s)(x), and Section 2 recovers x.

Thus there are exactly 2^d distinct lower tags of rank d-s and 2^d
distinct upper tags of rank d+s at each such distance. A common phase
offset causes no difficulty because F_d^a is a permutation. This
does NOT make different offsets disjoint: their full image families
are identical after reindexing the starting tag.

## 4. Interpretation as short cyclic permutation rows

Each F_d cycle has length 2d. Record the newly arrived paired coordinate
at every one-bit step. During its first d steps every pair is toggled
once, and the next d steps toggle the same coordinates in the same
order because F_d commutes with complement (complement equals F_d^d).
Thus its 2d recorded letters are a permutation of all 2d coordinates.

Its cyclic d-letter windows give the transversal states of that cycle,
up to a uniform index shift. Over all cycles, every transversal occurs
once. Intersections of two transversal windows s steps apart are their
common (d-s)-letter windows, and their unions are the (d+s)-letter
windows along that geodesic arc. Section 3 therefore gives distinct
windows, across this whole row family, at every length in

    d-floor(d/2),...,d+floor(d/2).

There are only 2^d windows at each length; these do not exhaust all
subsets of that size from a 2d-set. This is not a universal-cycle
theorem for the whole middle layer.

## 5. Construction scope

The recursion supplies an explicit geodesic routing through all binary
tags with no search or existence oracle. It can be considered as a tag
schedule on a separate long body of geodesic middle states.

There is NO claim here that this schedule preserves the target support
of the fixed-coordinate-order schedule for d>2. That comparison can
lose old tags. A different predecessor, forwarding even tags and
reversing odd tags along F_d, has now passed separate endpoint-role
and literal-source audits in the higher-tag phase trade in worktree7796.
That theorem does not change the scope of this abstract cycle construction.
Nor does this note prove candidate packing, global freshness, iteration,
or coefficient one.
