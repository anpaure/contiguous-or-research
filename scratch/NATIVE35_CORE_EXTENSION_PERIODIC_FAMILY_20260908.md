# A native35-period family with arbitrarily large core

2026-09-08. Pure constructive deduction from the independently verified
user-supplied35-period. No mathematical program was run.

For every s>=9 there is an explicit35-period on k=s+8 coordinates with
the generalized eight-arm P_i/Q_i ports, rank-(s-1) triple windows, and
rank-s four-windows. Its eight rotated copies graft to an explicit
280-period with280 distinct targets in each of those two ranks.
This is a native periodic realization, not a reset followed by isolated
ports. It covers its stated target family, not the full k-cube.

## 1. Base certificate and the explicit operation

Let W_0,...,W_34 be the user's35-period in
USER_NATIVE35_GRAFT280_AND_ROOTED291_INDEPENDENT_CERTIFICATE_20260908.md.
Its alphabet is [17], with

    C0={1,2,3,4,5}, u=6, v=7, w=8,
    a_i=9+i (0<=i<8), Z={17}.

The verified first two letters are W_0=C0 union {a_0} and
W_1={a_0,a_1}. Its35 cyclic triple unions and35 cyclic four-window
unions are distinct sets of ranks8 and9, respectively.

For s>=9, add the disjoint core coordinates

    B={18,...,s+8},       C=C0 union B.

Thus |B|=s-9 and |C|=s-4. The empty B is allowed at s=9.
Define the new literal period by the exact rule

    V_j=W_j union B   when j!=1,
    V_1=W_1.

Every new letter is nonempty. This rule is a finite, explicit
construction for every stated dimension.

## 2. Flat ranks and uniqueness survive exactly

Only one position of the35-period omits B. Every cyclic interval of
length at least two therefore contains B. In particular, for each start,

    OR of three V letters = B union OR of the three W letters,
    OR of four V letters  = B union OR of the four W letters.

Because B is disjoint from the old alphabet, their ranks are
8+|B|=s-1 and9+|B|=s. Adding the same disjoint B is injective on sets.
All35 triple targets and all35 middle owners remain distinct.

No repeated middle target is introduced and no additional positions
are used.

## 3. The exact generalized recency ports

Let rho rotate the eight arms and fix all other coordinates, including B.
Define V^(i)=rho^i(V). In its canonical periodic history, the states
after positions0 and1 are exactly

    P_i=(C union {a_i} | {u} | {v} | {w} |
             {a_(i+1)} | ... | {a_(i-1)} | Z),

    Q_i=({a_i,a_(i+1)} | C | {u} | {v} | {w} |
             {a_(i+2)} | ... | {a_(i-1)} | Z).

All arm indices are modulo eight. To prove this, the old coordinate
last-occurrence classes are unchanged. Each coordinate of B last occurs
at position0 when P_i is read, so it joins the first C0 block there.
The arm-pair letter at position1 omits B; thus B stays together with
C0 in the second block of Q_i. This is precisely the required enlarged C.

Every coordinate occurs in each period, so these are actual cyclic
recency states, determined by one traversal. No initial-state convention
or uncharged history is being supplied.

The source prefix ranks are s-3,s-2,s-1,s followed by successive
single-arm additions. The destination begins with ranks2,s-2,s-1,s.
In particular the middle rank still occurs at the fourth recency block.

## 4. An actual eight-to-one graft

The same exact transition identity holds with the enlarged core:

    T_{ {a_(i-1),a_i} }(P_i)=Q_(i-1).

Use the literal joined period formed by concatenating, for
i=7,6,...,0,

    V^(i)_1,V^(i)_2,...,V^(i)_34,V^(i)_0.

It is the old certified280-period with B adjoined at every position
except the initial arm-pair letter of each35-letter block.
The omitted positions are35 apart, including across the cyclic closure.
Thus every triple and every four-window gains exactly B from the old
joined period. All280 rank-(s-1) triple targets and all280 rank-s
four-window owners are distinct.

Alternatively, the legal rerouting retains all old state occurrences
after their indicated core enlargement. Since the joined period visits
every coordinate, those legal recency states are the actual periodic
ones. Hence its complete cyclic target inventory is the union of the
eight input inventories, with no initialization charge.

## 5. Scope of this positive family

This gives q=8 for every s>=9 in dimension k=s+8. It lies within the
requested condition q<=k-s+1, since8<=9. The leftover block has size one.
It supplies an infinite family of explicit native recurrent blocks,
extending the single s=9 example without breaking its port locations
or short-window distinctness.

It does not yet provide arbitrary q, an empty leftover block, or a
complete partition of the middle and facet layers by such modules.
In particular it does not solve the forced suffix problem for the
native291/311 prefix or the full-cube exact-equality goal.
