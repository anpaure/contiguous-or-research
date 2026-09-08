# A boundary four-cycle breaks the raw punctured factorial-moment hierarchy

**Date:** 2026-08-21  
**Status:** exact analytic obstruction with an independent H100 Venn audit

Let `b=2r+1`, with `r>=3`, and let the identity punctured configuration be

\[
 E=\{M_i,L_i:1\le i\le b-1\},
 \quad
 M_i=\{i,\ldots,i+r-1\},
 \quad
 L_i=\{i,\ldots,i+r-2\},                              \tag{0.1}
\]

where indices are modulo `b`.  If `D_M=2r r!(r+1)!` is the degree of a
middle target and

\[
 M_4(E)=\sum_F {|E\cap F|\choose4},                    \tag{0.2}
\]

then

\[
 \boxed{\qquad
 {M_4(E)\over D_M}\ge
 {4(r-1)^2\over r^2(r+1)}=\Theta(r^{-1}).
 \qquad}                                               \tag{0.3}
\]

Consequently there is no absolute constant `C` for which

\[
 M_s(E)\le D_M C^s r^{2-s}                             \tag{0.4}
\]

holds uniformly even at `s=4`.  In particular, a raw factorial-moment
hierarchy at the scale `C^s r^(2-s)` cannot be the input to FIFO
regeneration.  Connected/cycle-renormalized weights would have to remove
the family below.

## 1. The canonical cycle family

For

\[
 s\in\mathbb Z_b\setminus\{0,r,-1\},
\]

put

\[
 T_s=\{M_s,M_{s+1},M_{s+r+1},L_{s+1}\}\subset E.       \tag{1.1}
\]

The three exclusions are exactly those which would give one of the three
distinct starts `s,s+1,s+r+1` the deleted value zero.  Thus there are

\[
                         b-3=2(r-1)                    \tag{1.2}
\]

members of this family.  They are distinct because `L_(s+1)` determines
`s`.

Represent a length-`k` cyclic interval starting at `i` by its boundary
edge `{i,i+k}` on the cut-position circle.  The four boundary edges of
`T_s` are

\[
\begin{array}{c|c}
M_s&\{s,s+r\}\\
M_{s+1}&\{s+1,s+r+1\}\\
M_{s+r+1}&\{s+r+1,s\}\\
L_{s+1}&\{s+1,s+r\}.
\end{array}                                             \tag{1.3}
\]

Hence the boundary multigraph `H_(T_s)` is literally the four-cycle on
the cuts

\[
                         s, s+r, s+1, s+r+1.          \tag{1.4}
\]

In the notation `t=|T|`, `q=|V(H_T)|`, `c=c(H_T)`, and
`beta=t-q+c`, this gives

\[
                         (t,q,c,\beta)=(4,4,1,1).       \tag{1.5}
\]

It is also a four-cycle in the high-codegree skeleton: `L_(s+1)` is
contained in `M_s,M_(s+1)`, while `M_(s+r+1)` is disjoint from those same
two middle targets.  There are no other skeleton edges on these four
vertices.

## 2. Exact codegree

Write

\[
 A=M_s,\quad B=M_{s+1},\quad C=M_{s+r+1},\quad D=L_{s+1}.
\]

Their set relations are

\[
                         D=A\cap B,
 \qquad C=[b]\setminus(A\cup B).                       \tag{2.1}
\]

Thus their labelled Venn cells have the four nonzero sizes

\[
                         1, 1, r, r-1.               \tag{2.2}
\]

We now count their possible retained positional placements in a second
punctured word.  Two length-`r` cyclic intervals with intersection the
length-`r-1` interval `D` must have adjacent starts.  Choose the start `a`
of the earlier interval and choose which of the labelled targets `A,B` is
earlier.  Then the four starts are forced to be

\[
                         a, a+1, a+r+1, a+1.          \tag{2.3}
\]

for the two middle intervals, `C`, and `D`, respectively.  For either of
the two orientations, exactly the three values

\[
                         a=0,quad a=-1,quad a=-r-1
\]

use the deleted positional start zero.  Therefore the exact number of
retained placements is

\[
                         2(b-3)=4(r-1).                 \tag{2.4}
\]

For each placement, the Venn-cell labelling formula gives
`r!(r-1)!` words.  Directed-deck injectivity and within-layer simplicity
make this count multiplicity-free.  Consequently

\[
\begin{aligned}
 \deg(T_s)
   &=4(r-1)r!(r-1)!,\\
 {\deg(T_s)\over D_M}
   &={2(r-1)\over r^2(r+1)}.                           \tag{2.5}
\end{aligned}
\]

Summing (2.5) over the `2(r-1)` distinct sets in (1.2) proves (0.3).

## 3. What fails in the boundary-tree ansatz

For this family,

\[
 (q-2)+\beta=3,                                        \tag{3.1}
\]

but the actual normalized codegree has only two powers of `r` in (2.5).
The independent boundary cycle does not force an additional unit of
factorial split mass.  Its full cyclic embedding retains a free rotation;
after puncturing, `4(r-1)` placements remain and return one power of `r`.

This does not contradict the corrected three-target boundary estimate.
For example, the formerly problematic disconnected-skeleton `MLL` triple
has `(q,c,beta)=(5,2,0)` and exact normalized codegree
`4/[r^2(r+1)]`, agreeing with exponent `t+c-2=3`.  The first failure is the
boundary cycle above.

## 4. H100 audit

The standard-library exact counter

`scratch/research_punctured_boundary_graph_four_cycles_20260821.py`

constructs the full high-codegree skeleton, enumerates every induced
four-cycle, computes `H_T`, and independently evaluates its Venn-factorial
codegree.  On H100 it found exactly `2(r-1)` cycles and no other cycle type
at `r=5,8`.  In both cases every cycle had `(q,c,beta)=(4,1,1)` and the
codegree in (2.5).  Source SHA-256:

```text
53b17fd5cc95c0c507d4d92e04b7c52697cd632fde2bf8c99364626c82004649
```

The computation is a regression audit.  Equations (1.1)--(2.5) are the
uniform proof.
