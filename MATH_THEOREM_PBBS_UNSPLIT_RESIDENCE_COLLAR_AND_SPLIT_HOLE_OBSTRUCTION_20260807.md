# The unsplit promotion hinge has an exact biresident rail collar; the split staircase cannot occur at positive density at length (B)

**Date:** 2026-08-07  
**Status:** unconditional local collar theorem and sharp global scale
obstruction.  Splitting the predecessor bank makes both q1 colours literal
but creates one unavoidable missing fixed-depth central endpoint.  At
length (B=W+d), at most (d) such holes exist.  Hence the split
staircase cannot serve the (H=\Theta(W)) rephased flags.  The unsplit
hinge instead embeds in a flat simple biresident rail with exactly one
lower-q1 sidecar and no upper sidecar.

## 1. The split staircase has one unavoidable central hole

Put (D=d+1).  In the split source of Theorem 6.1 of the hinge note, the
length-(D) interval ending at the promoted endpoint is

\[
 [-d-1,-1]
\]

and has value

\[
 I_-=M\cup\{u\}\cup C,
 \qquad |I_-|=m-1.
\tag{1.1}
\]

Every shorter interval ending there is contained in (I_-).  The rank-
(m) predecessor

\[
 T_-=I_-\cup\{b^-\}
\]

uses the length-((D+1)) interval ([-d-2,-1]).

### Proposition 1.1 (sharp fixed-depth obstruction)

No extension outside the displayed split block can make the promoted
endpoint carry a rank-(m) interval of length at most (D) while retaining
the interval table of Theorem 6.1.

#### Proof

Every interval ending at the endpoint and having length at most (D) lies
inside ([-d-1,-1]), whose union is the rank-((m-1)) set (I_-).
Letters outside the block do not meet any such interval.  \(\square\)

Thus the split refinement is compatible only with a variable-length or
incidental duplicate occurrence.  It cannot be one row of an everywhere
flat fixed-depth owner chronology.

## 2. Exact endpoint-hole budget at (B=W+d)

The local obstruction becomes decisive globally.

### Theorem 2.1 (at most (d) split central holes)

Let a word have length (B=W+d), and select one witnessing interval for
each of the (W=\binom{k}{m}) rank-(m) targets.  Then:

1. every selected interval has length at most (D=d+1); and
2. their right endpoints are pairwise distinct.

Consequently at most (d) physical endpoints carry no selected rank-(m)
witness.  Any occurrence-disjoint family of split promotion staircases has
size at most (d).

#### Proof

The selected-interval lower-bound argument at length (W+d) gives the
length bound.  If two selected intervals have the same right endpoint,
one contains the other.  Their unions are therefore comparable.  Distinct
rank-(m) targets are incomparable, so the two selected intervals cannot
witness different targets.  Hence the (W) chosen intervals use (W)
distinct right endpoints among the (W+d) positions.

By Proposition 1.1, the promoted endpoint of every split staircase is not
one of those selected endpoints.  Distinct upper-flag occurrences require
distinct promoted endpoints, proving the last assertion.  \(\square\)

The adaptive-phase bank has

\[
 \frac HW\longrightarrow
 \theta=4\sum_{a\ge1}e^{-4\pi a^2}>0.
\tag{2.1}
\]

Since (d=\Theta(\sqrt k)) while (W) is exponential,

\[
 H/d\longrightarrow\infty.
\tag{2.2}
\]

Therefore the split, sidecar-free staircase can handle only a vanishing
fraction of the required rephased flags in an exact-(B) construction.
The mass route must return to the unsplit flat hinge and route its one q1
sidecar.

## 3. Explicit unsplit rail collar

Use the unsplit hinge data

\[
 B^-=C\mathbin{\dot\cup}\{b^-\},
 \qquad
 B=C\mathbin{\dot\cup}\{b\},
 \qquad |C|=d.
\tag{3.1}
\]

Partition

\[
 M=K\mathbin{\dot\cup}\{a_1,\ldots,a_{d-1}\},
\tag{3.2}
\]

which is possible under the hinge hypothesis (|M|\ge d-1), and put

\[
 G=K\mathbin{\dot\cup}C,
 \qquad |G|=m-d-1=m-D.
\tag{3.3}
\]

Choose a cyclic order of (N=2D) distinct toggle labels containing the
consecutive segment

\[
 b^-,u,a_1,\ldots,a_{d-1},b,v.
\tag{3.4}
\]

At all ordinary positions with toggle (x), use the source letter

\[
 G\cup\{x\}.
\tag{3.5}
\]

On the displayed segment replace those ordinary letters by

\[
 C\cup\{b^-\},\quad
 K\cup\{u\},\quad
 K\cup\{a_1\},\ldots,K\cup\{a_{d-1}\},\quad
 C\cup\{b\},\quad
 K\cup\{v\}.
\tag{3.6}
\]

These replacements preserve the toggle label of every position but
fragment the permanent core (G=K\cup C).  The redundant copies of (K)
in the (u)- and (v)-letters do not change any displayed hinge value;
they make the collar uniform in the boundary case (d=2).

### Theorem 3.1 (biresident unsplit collar)

For the cyclic source word (3.5)--(3.6):

1. every length-(D) source interval has union

   \[
   G\cup\{\text{its (D) consecutive toggles}\};
   \tag{3.7}
   \]

2. these values are distinct rank-(m) owners forming a simple Johnson
   cycle;
3. both set-theoretic immediate palettes are simple;
4. every noncore coordinate has one owner run and one owner gap, both of
   length (D), while every coordinate of (G) is permanent;
5. the middle three owners and the saturated suffix flag are exactly the
   unsplit promotion hinge; and
6. every proper upper interval is literal and simple.  The only lower-q1
   value not equal to its native shared length-(d) source interval is
   (I_-) on the predecessor hinge edge.

#### Proof

Any length-(D) interval not wholly contained in the exceptional segment
contains an ordinary letter (3.5), hence contains all of (G).  There are
exactly three length-(D) intervals wholly inside the exceptional segment.
Their core fragments are respectively

\[
 C,K;\qquad K,C;\qquad K,C,
\]

so each also has union (G).  Every source position contains its own
distinct toggle and no other noncore toggle.  This proves (3.7).

Sliding a (D)-window deletes one toggle and inserts the next.  Distinct
proper cyclic toggle intervals recover their endpoints, proving owner
simplicity and Johnson adjacency.  Intersections and unions of consecutive
owners are (G) plus (D-1) and (D+1) consecutive toggles, proving
both palette statements.

Each toggle occurs at one source position and therefore in exactly the
next (D) owners.  Since (N=2D), its complementary gap also has length
(D).  Equation (3.7) makes (G) permanent in the owner row.

On the exceptional segment, the interval unions are

\[
 M,quad M+u,quad M+C+b,quad M+C+u+b,
\]

at the required suffix depths, and the three owner windows are precisely
(T_-,T_0,T_+).  Thus the hinge survives literally.

Every interval of length at least (D) contains a length-(D) subinterval
and hence all of (G); its value is (G) plus its proper cyclic toggle
interval, so all proper upper values are literal and simple.  Finally, on
the predecessor edge the shared length-(d) source interval is (U=M+u),
whereas the owner intersection is (I_-=M+C+u).  Every other immediate
edge either contains an ordinary full-(G) letter in its shared interval
or is the successor hinge edge, whose shared interval is (Y).  Hence no
other lower-q1 sidecar occurs.  \(\square\)

### Corollary 3.2 (exact local sidecar budget)

The unsplit promotion hinge admits a literal cyclic residence collar with

\[
 \boxed{
 \text{one named lower-q1 sidecar and zero upper sidecars}.}
\tag{3.8}
\]

All owner and upper occurrence rows of the collar are flat, simple and
biresident.

## 4. Global boundary of the collar

Theorem 3.1 is a local template, not a positive-density packing theorem.
One isolated collar occupies (2D=\Theta(d)) physical positions.  Taking
(H=\Theta(W)) disjoint copies would require

\[
 \Theta(Hd)=\Theta(Wd)
\]

positions, far beyond a length-(W+O(d)) word.  A global construction must
interlace many hinges in one shared owner chronology and reuse the ambient
rail state.  The theorem proves that residence and upper sidecars are not
the local obstruction; it does not prove this interlacing.

The surviving mass-scale statement is therefore:

> Plant (H) unsplit hinges in one flat resident owner factor and match
> their (H) predecessor sidecars (I_-) to distinct legal lower-q1
> occurrences, while retaining the common upper/compiler rows.

The ideal reset count and the local collar do not imply that matching.
But the split alternative is now ruled out at scale by Theorem 2.1, so q1
sidecar routing is the unique proof-safe continuation of this promotion
route.
