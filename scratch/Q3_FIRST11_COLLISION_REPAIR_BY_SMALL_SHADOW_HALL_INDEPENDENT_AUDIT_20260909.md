# Residence-three entrance collisions admit distinct facet choices

Date: 2026-09-09. Status: independent pure-proof audit PASS. No mathematical
execution, matching computation, or buffer construction was performed.

## Exact statement and assumptions

Let n=2r+1 with r>=7. Fix a cyclic middle-level carrier whose lower states
are all r-subsets exactly once, whose outgoing upper matching is the
canonical first-minimum Phi, and whose incoming matching is a permutation.
Assume every positive lower-coordinate run has length at least three.
Choose the first old coordinate u as root, and append two new coordinates
a,b after all old coordinates in the order used by Phi.

At every root port L, put

    U=Phi(L)=L+u,    P=sigma(L)=U-d,    C_L=P-u=L-d.

Here d belongs to L, and the root ports are precisely the words 0 followed
by a Dyck word of semilength r. There are Cat_r such ports. The parent
successors P are distinct, so the sets C_L form a DISTINCT family of
(r-1)-sets.

Assume the entrance begins with the actual parent predecessor history
with a held present and b absent. There is a simultaneous choice

    e_L in C_L

such that every entrance

    L+a  ->  U  ->  P+b  ->  (P-e_L)+a+b                 (1)

uses the canonical child Phi at every step, completes no positive run of
length below three, and has a distinct final 11-state. The previously
injective 00- and 01-state maps are unchanged.

This is a statement about the first three steps of all entrances. It
does not construct any subsequent buffer paths, exits, global child
cycle, or literal universal word.

## Why every second old deletion is allowed at q=3

The inserted coordinates in (1) are u,b,a; its deleted coordinates are
a,d,e_L. The initial a-run has the required length from the held-a
predecessor history. The parent d-run already has length at least three
at L, and d also survives the next state U before being removed.

For ANY e in C_L=L-d, the coordinate e occurs in the three consecutive
states L+a, U, P+b. It therefore has age at least three when removed at
the third step, even if its age at L was only one. This is the new
freedom: e need not equal the next prescribed parent deletion.

The freshly added root u survives all three new states. The new b-run
and the returning a-run remain open at the end of this partial path;
their later deletion times are not supplied by this lemma.

The child Phi additions do not depend on e. To see this directly, encode
membership by +1 and nonmembership by -1. For a root port, the old walk
of L is -1 followed by a Dyck excursion, so its first global minimum is
at u. Appending the new bits 10 preserves that first minimum. Thus Phi
adds u to L+a. The old walk of U stays at least 1 and ends at 1;
appending 00 makes its first negative minimum occur at b, so Phi adds b.
Deleting d from U makes the old walk of P stay at least -1 and end at
-1. Appending 01 creates its first minimum -2 at a, so Phi adds a to
P+b. Any deletion e in C_L then gives the last state in (1).

## The exact Hall condition

We use the existing small-family consequence of the Lovasz form of
Kruskal--Katona: a family A of k-sets with

    |A| <= binom(2k-1,k)

has lower shadow of size at least |A|. For a nonempty A, write
|A|=binom(x,k), x>=k. Then x<=2k-1 and

    |partial A| >= binom(x,k-1)
                 = |A| k/(x-k+1) >= |A|.

The empty case is immediate. Applying this bound to every subfamily is
Hall's condition for distinct lower-facet representatives. This same
argument is already recorded in
[Catalan cap-two compression, Section 1](../MATH_THEOREM_CATALAN_CAP_TWO_COMPRESSION_20260731.md)
and [full-orbit escape, Lemma 5.1](../MATH_ATTACK_N_FULL_ORBIT_ESCAPE_AND_Q1_CYCLE_20260725.md).
The shadow theorem or Hall argument itself is not new here.

For k=r-1, the required size comparison is

    Cat_r / binom(2r-3,r-1) = 4(2r-1)/(r(r+1)) <= 1.

Indeed, the final inequality is r^2-7r+4>=0, which holds for every
integer r>=7. Every subfamily of {C_L} therefore has enough distinct
(r-2)-subsets. Hall gives an injection

    C_L -> F_L subset C_L,    |F_L|=r-2.

Write F_L=C_L-e_L. The final old facet in (1) is u+F_L, so these facets
and their corresponding child 11-states are distinct. The 00-states U
remain distinct by the parent outgoing matching, and the 01-states P+b
remain distinct by the parent incoming permutation. Different sectors
have different membership in a,b, so they cannot collide with each other.

## Relation to the fixed19 diagnostic

The [fixed prescribed-parent diagnostic](K19_FIXED_ROOT_PRESCRIBED_PARENT_SECTOR_PORT_CERTIFICATE_20260909.md)
found 375 double collisions among the 4,862 first11 states obtained by
forcing e to be the next parent deletion. The theorem above removes that
particular collision requirement by allowing any age-legal e. It gives
existence of a simultaneous injection without changing the preceding
00/01 states. It neither materializes that injection nor controls the
remaining internal buffer paths, their intersections, or upper-target
coverage. The diagnostic and its narrow negative conclusion remain valid.

## Five-step closure into a disjoint excursion bank

The first11 choices above also admit a uniform two-step closure, without
another matching. This strengthens the three-step statement: no internal
buffer search is needed for these five-step excursions. Global spanning,
coverage, and attachment to an untouched parent trajectory remain open.

For an old (r-1)-set K, let J(K) add the coordinate where its old-coordinate
walk first attains its global minimum. If that minimum is m, then m<=-3.
Flipping that step from -1 to +1 leaves the earlier walk unchanged and
raises all later heights by two. Its new minimum is exactly m+1, attained
immediately BEFORE the changed step, and no later prefix attains it.
Consequently the changed coordinate is recovered immediately after the
LAST minimum of J(K). Thus J is injective, and

    minimum(J(K)) <= -2.                                 (2)

Empty prefixes are included in this minimum convention. The old total
-3 guarantees that the first minimum is not the empty prefix.

Let the distinct Hall-selected first11 old facets be K_L=P-e_L; all
contain u. Define

    K'_L=J(K_L)-u,    O_L=J(K'_L).

Since J only adds a coordinate, J(K_L) contains u. Therefore K'_L are
distinct and all omit u, whereas every K_L contains u. The sets O_L
are distinct by injectivity of J. They have minimum at most -2 by (2),
whereas every initial root port L=0D has minimum -1. Hence no O_L is
an initial root port. In fact O_L also omits u: otherwise
O_L=K'_L+u=J(K_L), and injectivity would force K'_L=K_L, contradicting
their different membership in u.

The complete path for port L has these six child lower states:

    X0 = L+a,
    X1 = U,
    X2 = P+b,
    X3 = K_L+a+b,
    X4 = K'_L+a+b,
    X5 = O_L+a.                                         (3)

The first three transitions are those already proved. In either 11-state,
the old walk ends at -3 and appending 11 only raises its height. Thus
canonical child Phi adds exactly the coordinate prescribed by old J.
The fourth transition adds J(K_L)-K_L and deletes u; the fifth adds
J(K'_L)-K'_L and deletes b. These insertions are old coordinates and
therefore differ from the deleted new b; the fourth insertion differs
from u because u was already present. Both are legitimate middle-level
steps.

All six state banks in (3) are pairwise disjoint. The new-bit sectors
separate 00,01,10,11. Within sector10, the input and output banks are
separated by the minimum criterion (2). Within sector11, the first and
second banks are separated by membership in u. Each individual bank
is injective, using the parent matchings, Hall, and J as above. Hence
the paths are pairwise vertex-disjoint, including their endpoints. The
canonical child Phi is itself an injective middle-level matching, so
the five upper-owner banks are also injective and mutually disjoint.

The additional residence checks are exact. The root u is present in
X1,X2,X3, then absent from X4 and X5; its completed new run has length
three. The coordinate b is present in X2,X3,X4 and is removed at X5,
also completing a run of length three. The returning a is present in
X3,X4,X5, so its age at the exit is three. All earlier completed runs
retain the history-based checks preceding (2). The newly added old
coordinates may have ages only two or one at X5; this proof does not
authorize arbitrary deletions when attaching another path afterward.

This is a bank of disjoint local excursions, with residence certified
relative to the stated parent entrance histories. It is not a spanning
child cycle. Its output10 states O_L+a avoid the INPUT root-port bank,
but could coincide with other 10 states of an untouched parent copy.
Likewise the bank theorem does not allocate remaining child states,
prove age-compatible gluing, or preserve a complete interval-target
family. None of those conclusions follows from this local injectivity.

This extension was checked purely; no matching, buffer, or word
construction was executed.
