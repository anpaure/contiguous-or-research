# A three-auxiliary-owner diamond removes both forced context-seam tickets

**Date:** 2026-08-13  
**Status:** unconditional owner/immediate-palette seam replacement.  The
same patch works in both rail-square states and hence preserves the
telescoped owner current.  The bare patch is not yet a depth-resident
literal source gadget; a clocked lift is isolated in Section 5.

## 1. The bad seam

Fix an `(R-1)`-context `G` and distinct labels `x,p` outside `G`.  Put

\[
                             U=G\cup\{x,p\}.           \tag{1.1}
\]

At an internal vertex of an adjacent-transposition context path, either
aggregate shore contains the two endpoint owners

\[
                             X=G\cup\{x\},qquad
                             P=G\cup\{p\}.             \tag{1.2}
\]

The retained common-deck owners on the outer sides have the form

\[
                             K_a=G\cup\{a\},qquad
                             K_b=G\cup\{b\},            \tag{1.3}
\]

and those on the inner sides have the form

\[
                             I=U\setminus\{r\},qquad
                             I'=U\setminus\{s\}.        \tag{1.4}
\]

Here `r,s in G`, while `a,b` lie outside `U`.  The unpatched rail union
uses `G` twice as an immediate-lower ticket and `U` twice as an
immediate-upper ticket.

Assume that `r,s,t` are three distinct points of `G`, and choose

\[
 y\notin G\cup\{x,p,a,b\},                            \tag{1.5}
\]

with `a,b,y` pairwise distinct.  This is available whenever `|G|>=3`
and at least five labels lie outside `G`.

## 2. Three auxiliary owners

Define

\[
 \begin{aligned}
 Z_x&=(G\setminus\{t\})\cup\{x,y\},\\
 Z_p&=(G\setminus\{t\})\cup\{p,y\},\\
 Z_a&=(G\setminus\{s\})\cup\{x,a\}.
 \end{aligned}                                       \tag{2.1}
\]

All have rank `R`.  Replace the two bad rail fragments by the two Johnson
paths

\[
 I-X-Z_x-Z_p-P-K_b,                                  \tag{2.2}
\]

and

\[
 K_a-Z_a-I'.                                         \tag{2.3}
\]

The four boundary owners `I,I',K_a,K_b` keep their one exterior edge.
They acquire one patch edge; `X,P,Z_x,Z_p,Z_a` have patch degree two.
Consequently (2.2)--(2.3), together with the retained exterior, is a
degree-two owner/lower-incidence object.

## 3. Exact ticket table

For a Johnson edge `AB`, write

\[
                         L(A,B)=A\cap B,qquad
                         V(A,B)=A\cup B.              \tag{3.1}
\]

The seven patch edges have the following literal tickets.

| edge | lower ticket | upper ticket |
|---|---|---|
| `I-X` | `(G-r)+x` | `G+x+p=U` |
| `X-Z_x` | `(G-t)+x` | `G+x+y` |
| `Z_x-Z_p` | `(G-t)+y` | `(G-t)+x+p+y` |
| `Z_p-P` | `(G-t)+p` | `G+p+y` |
| `P-K_b` | `G` | `G+p+b` |
| `K_a-Z_a` | `(G-s)+a` | `G+x+a` |
| `Z_a-I'` | `(G-s)+x` | `(G-s)+x+p+a` |

Here `G-r` means `G setminus {r}`, and similarly for `s,t`.

> **Theorem 3.1 (three-owner seam diamond).**  Under (1.5), all nine
> owners in (1.2)--(1.4) and (2.1) are distinct.  Every row of the table
> is a Johnson edge; its seven lower tickets are pairwise distinct and
> its seven upper tickets are pairwise distinct.  In particular the old
> lower ticket `G` and old upper ticket `U` are each used exactly once.

### Proof

Each consecutive pair in (2.2)--(2.3) differs by the exchange shown in
the table, so it is a Johnson edge.  Owner distinctness follows from the
signature consisting of the subset missing from `G` and the labels added
outside `G`:

* `X,P,K_a,K_b` miss no point of `G` and add respectively `x,p,a,b`;
* `I,I'` miss respectively `r,s` and add `x,p`;
* `Z_x,Z_p` miss `t` and add respectively `x,y` and `p,y`;
* `Z_a` misses `s` and adds `x,a`.

The hypotheses make these signatures distinct.

For the lower tickets, first separate by the number and identity of labels
outside `G`.  The only repeated outside signature is `+x`; the three
corresponding rows miss `r,t,s`, which are distinct.  The two tickets
missing `t` but not having outside signature `+x` add `y` and `p`, so they
are distinct.  The tickets `G` and `(G-s)+a` are then separated from all
others.  Hence the lower row is simple.

For the upper tickets which contain all of `G`, their added pairs are

\[
 \{x,p\},\ \{x,y\},\ \{p,y\},\ \{p,b\},\ \{x,a\},   \tag{3.2}
\]

and are distinct.  The remaining two tickets miss respectively `t,s`
and add the distinct triples `{x,p,y}` and `{x,p,a}`.  They cannot equal
one another or a full-`G` ticket.  This proves upper simplicity and the
last assertion.  `square`

## 4. Two-state and current compatibility

At an internal context, both shores of the telescoped path-square current
contain the same **set** `{X,P}`: the two owners merely exchange which
incident rail supplies them.  The four owners `I,I',K_a,K_b` belong to
the unchanged decks of the rail squares and are also common to both
states.

Install the same three auxiliary owners and the same paths (2.2)--(2.3)
in both states.  The patch therefore contributes zero signed owner
current and zero signed immediate-palette current.  It physically replaces
the multiplicity-two tickets `G,U` by the seven-entry simple table in
each state.  In particular, applying this local operation does not alter
the endpoint telescope

\[
       \delta_{xp}(G_0)-\delta_{xp}(G_t).             \tag{4.1}
\]

This is a literal common-reserve seam repair at the owner and immediate
palette levels, not merely a signed cancellation.

Global use still requires choosing `r,s,t,y` so that the nine owners and
fourteen tickets also avoid every other seam and the protected exterior.
The local theorem makes no unsupported polynomial-forbidden-bank claim.

## 5. Exact residence defect and a canonical clocked middle bridge

The bare diamond cannot be inserted directly into the depth-`d` source
architecture when `q=d+1>2`.  The fresh point `y` has owner trace

\[
                         0\,1\,1\,0                  \tag{5.1}
\]

on the subpath `X-Z_x-Z_p-P`; absent exterior occurrences do not lengthen
its positive run.  Thus its positive run has length two.

There is, however, an explicit resident replacement of the single edge
`Z_x-Z_p`.  Choose

\[
 W=\{w_0,\ldots,w_{q-1}\}
   \subseteq G\setminus\{r,s,t\},                   \tag{5.2}
\]

and a fresh disjoint set

\[
 W'=\{v_0,\ldots,v_{q-1}\}.                          \tag{5.3}
\]

On the cyclic order

\[
 w_0,\ldots,w_{q-1},v_0,\ldots,v_{q-1},              \tag{5.4}
\]

let `D_j` be its cyclic `q`-window, so `D_0=W`, `D_q=W'`, and
`D_(2q)=W`.  Put

\[
 J=(G\setminus(\{t\}\cup W))\cup\{y\}.              \tag{5.5}
\]

Then the sequence

\[
 \begin{split}
 &J\cup\{x\}\cup D_0,ldots,J\cup\{x\}\cup D_q,\\
 &J\cup\{p\}\cup D_q,ldots,J\cup\{p\}\cup D_{2q}
 \end{split}                                         \tag{5.6}
\]

starts at `Z_x`, ends at `Z_p`, and is a simple Johnson path.  Its
immediate lower and upper tickets are simple: the two phases are separated
by `x/p`, the midpoint edge by containing neither/both, and within one
phase the clock tickets are proper cyclic `(q-1)`- and `(q+1)`-intervals.

Every clock point has both binary runs at least `q` relative to the
boundary state `D_0=W`; `x` and `p` have runs `q+1`, `y` and the set `J`
are constant on the bridge, and `t` has a zero run longer than `q`.
Thus (5.6) repairs the intrinsic run-two defect of (5.1).

This clocked middle bridge is an exact local owner/palette/residence
module.  It is not yet a complete source theorem for the whole seam.  A
full lift must additionally verify the inherited residence halos at
`I,I',K_a,K_b`, give a simultaneous source-letter realization of the
rewired owner components, retain the all-width ticket current, and pack
the fresh clock signatures across all commodities.  Those are the exact
remaining interfaces; they are not consequences of the seven-edge table.

## 6. Consequence

The degree invariant for complete path squares is not a terminal local
obstruction.  New owners do remove it:

\[
 \boxed{\text{three auxiliary owners}
        \Longrightarrow
        \text{one-use }G\text{ and }G+x+p
        \text{ with simple immediate palettes}.}
\]

The result narrows the next Gate-A construction to a protected packing and
source-lift theorem for this explicit finite seam table (or its clocked
version).  Merely cycling the old squares is impossible, while a new
compound seam is locally feasible.
