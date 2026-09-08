# Two-step root-socket ages and a corrected local replacement

Date: 2026-09-09. Status: exact pure-proof history classification.
No computation, matching run, source preparation or global construction.

The proposed replacement 011D00 -> 110D00 is never residence-three legal
in a strict canonical-Phi factor. Its deleted third old bit has age
exactly2. A different explicit replacement, deleting the first one of D,
has a guaranteed age-at-least3 deletion and distinct heads. This resolves
the local edge question, not the surrounding matching or history supply.

## 1. Setup and the question left by the first obstruction

Retain [the all-root first-entrance obstruction](Q3_ALL_ROOT_ENTRANCE_BANK_FORCES_ONE_STEP_RUNS_20260909.md).
Let r>=1, D be Dyck of semilength r-1, and put

    U=011D00,       Z=111D00.

The last two positions are the new a,b, in that physical order. The first
three old positions are u,x,y. Child Phi(U)=Z. In a strict incoming-
matching factor, returning from an upper to its own Phi preimage is
forbidden. A coordinate's age counts consecutive lower states containing
it, including the current state.

Every nonself arrival at U inserts x. Its preceding lower state is exactly

    S_z=U+z-x,                                        (1.1)

where z is either a zero position of D or the new a or b. Adding u to U
would instead use Z and have U itself as Phi preimage. The second old bit
x is therefore always age1 at U. The previously proposed head110D00
deletes y; it requires analysis of one further predecessor.

## 2. Exhaustive second-inverse classification

For a predecessor of S_z consider an upper S_z+w with w outside S_z.
The possible w are precisely x, u, and all other choices from the zero
positions of D together with a,b, excluding z itself.

If w=x, this is U+z and its Phi preimage is S_z, a forbidden self edge.
For the other cases, the inverse Phi deletes the up-step after the LAST
global prefix minimum of the complete child upper word. The full table is

| Cases | Last minimum | Bit removed by inverse Phi |
|---|---|---|
| w=u and z is an old D-zero or a | height0 at old x | y |
| w is neither u nor x | height-2 at old x | y |
| z=b and w=u | height0 at new a | b=z |

Here the empty prefix is included when taking a minimum. These three
cases exhaust all nonself second predecessors.

For the first row, the initial old bits are101, with heights1,0,1.
An old zero flip leaves the subsequent old heights at least1 and the
appended00 ends at heights2,1; adding a instead gives appended heights2,1
as well. Hence the last minimum is at x, followed by the up-step y.

For the second row, the initial old bits remain001, with heights-1,-2,-1.
The two added coordinates z,w are distinct and lie later, in D or at
a,b. Subsequent old heights stay at least-1. If both are old, the appended
heights are2,1; if one is old and the other is a or b they are respectively
2,1 or0,1; if both are new they are0,1. None revisits -2, so the last
minimum is again at x and the removed bit is y.

In the exception z=b,w=u, the initial old bits are101, the old walk ends
at height1 and is otherwise strictly above its height0 at x. The new
suffix01 visits height0 again at a and then height1 at b. Thus the last
minimum is at a and inverse Phi removes b=z.

The exceptional predecessor omits z. Its transition to S_z inserts z,
and the very next transition S_z->U deletes z. It necessarily closes a
positive lower run of length1 and is excluded by residence at least2,
regardless of any earlier history.

## 3. Exact ages and the complete local outgoing list

Consequently every residence-two incoming history at U has the form

    R=U+z+w-x-y -> S_z=U+z-x -> U,                     (3.1)

with the exceptional case excluded. Its insertions are y,x and its
deletions w,z. Therefore at U:

    age(x)=1,       age(y)=2,
    age(t)>=3 for EVERY one-position t of D.           (3.2)

The D-ones were present in all three states R,S_z,U. This proves their
age bounds without any prescribed parent history.

It follows that U->110D00, which deletes y, closes a run of length2 and
cannot occur in a residence-three factor. At the fixed upper Z, deleting
u is the forbidden self successor and deleting x closes a one-state run.
Thus the COMPLETE residence-three outgoing list at U is

    U -> 111(D with one of its ones changed to zero)00. (3.3)

Every deletion in (3.3) has age at least3. This asserts local legality
given a residence-three incoming history, not the existence of such a
history within a global factor. If r=1, D is empty and the list is empty:
there is no residence-three strict canonical-Phi full factor on these
five child coordinates. No claim about general OR words follows.

For clarity, the exact boundary condition for the three transitions
R->S_z->U->Y in the ordinary rows of Section2 is as follows. At R require
age(w)>=3 and age(z)>=2. Then deleting w is legal; deleting z at S_z is
legal after its extra state; and any D-one can be deleted at U. These
conditions are also necessary for the first two transitions. All other
completed runs are already part of the supplied history at R. The
exception cannot be repaired by changing those initial ages.

## 4. Explicit distinct corrected heads

For r>=2 write D=1R_tail, since every nonempty Dyck word begins with one.
Choose the first D-one in (3.3). The corrected head is

    Y_D=1110R_tail00.                                 (4.1)

These heads are distinct for distinct D. Their old nonempty prefixes
are all strictly positive, so they belong to the old head bank Phi(I)
occupied by the prescribed first entrances. Their new00 sector and the
source U are literal, not independently rerooted.

The failed proposed heads are110D00=1101R_tail00. They start with110,
whereas every eligible head in (3.3) starts with111. Thus freeing exactly
the failed110D heads cannot permit any of the critical U sockets to
continue with residence3. If all those omissions are kept, at least
Cat_(r-1) ADDITIONAL distinct root-entrance heads must be freed, by
injectivity of the matching across the Cat_(r-1) critical uppers.

If one chooses the replacement set anew, this argument does NOT increase
the general necessary count beyond Cat_(r-1): it strengthens the required
TYPE of freed heads. The explicit injection (4.1) supplies that many
distinct local incidence choices. It does not give an optimal reopening
count or a residual perfect matching.

## 5. An explicit conditional three-step connector

Taking z=a and w=b in (3.1) gives the particularly simple literal path

    000D11 -> 001D10 -> 011D00 -> 1110R_tail00.         (5.1)

The inserted coordinates are y,x,u. The deleted coordinates are b,a,
and the first D-one. Every insertion is the actual canonical Phi choice,
as can be read from the first minima -3,-2,-1 of the successive sources.
At the first state it suffices to have b-age at least3 and a-age at least2;
all D-ones merely need their automatic age at least1. These input ages
make all three closed runs in (5.1) legal at residence3.

This connector exhibits a concrete valid continuation under explicit
input ages. Supplying those incoming11 histories, keeping all chosen
paths globally disjoint, reallocating the displaced upper incidences,
and checking ages at the new00 outputs remain unproved. No claimed
matching, spanning factor, all-rank OR coverage or exact-budget opening
is hidden in (5.1).

## 6. Attribution and review

The first-socket obstruction and inverse matching are retained results.
Root proposed testing the110D replacement. The induction agent derived
the exhaustive two-step table, its exceptional one-state run, the forced
ages1/2, and corrected1110 heads. Root independently checked these
conclusions. The finite-frontier agent independently read the full proof
and passed all inverse cases, the exceptional one-state run, the complete
outgoing menu, the r=1 boundary, and the explicit connector's input-age
conditions. This is internal independent proof review, not external
certification. No mathematical execution occurred.
