# Audit of the domino double-segment half-exponent obstruction

Date: 2026-07-27

## 0. Verdict

Put

\[
 n=2m,\qquad R=2r+1=m-q_0,
 \qquad h=m-2r=q_0+1.
\]

At the Gaussian annulus (h=\Theta(\sqrt m)).  The proposed uniform
close-neighbour estimate

\[
 \#\{G:|F\cap G|\ge K-s\}
 \le \exp(O(m))n^{cs},\qquad c<\frac12,                 \tag{0.1}
\]

is false for (s=o(m)).  The globally aligned double-segment family in
`MATH_OBSTRUCTION_GLOBALLY_ALIGNED_DOUBLE_SEGMENT_DOMINO_ENTROPY_20260727.md`
has been independently checked.  Its bad-cell count

\[
 2(\ell-1)+\min\{\ell-1,h\}+4                         \tag{0.2}
\]

is correct, and its presentation-to-simple-support multiplicity is at
most (2m).  Taking \(\ell=m/\sqrt{\log m}\) gives list exponent
(1/2-o(1)), with an entropy term of order
(m\sqrt{\log m}), so the prefactor \(\exp(O(m))\) cannot absorb it.

The local star-to-top charge of three missing targets per deferred mate
remains correct.  What fails is additivity: two modified segments at
displacement (r) have remote defect fronts separated by only
(h=m-2r), so their local collars overlap almost completely when
(h=o(\ell)).

## 1. Construction and support count

Fix the cyclic word of unordered dominoes

\[
 B_0,B_1,\ldots,B_{m-1}
\]

of a simple twin packet (F).  Let

\[
 I=\{0,1,\ldots,\ell-1\},
 \qquad J=I+r,
\]

where

\[
 1\ll\ell,\qquad \ell+h<r.                             \tag{1.1}
\]

The segments are disjoint.  On each segment independently, repartition
its (2\ell) coordinate labels into an ordered list of \(\ell\)
unordered pairs.  One segment has

\[
 N_\ell=\frac{(2\ell)!}{2^\ell}                         \tag{1.2}
\]

such ordered repartitions, so there are (N_\ell^2) paired cyclic
words before quotienting.

A simple twin support recovers its unordered domino partition and the
unoriented cyclic order of the dominoes.  Since the words in (1.2)
already use unordered pairs, internal domino flips create no additional
multiplicity.  Two displayed words defining the same simple support can
differ only by one element of the global dihedral group (D_m), of size
(2m).  Hence the number of distinct simple supports is at least

\[
 \boxed{
 \frac1{2m}\left(\frac{(2\ell)!}{2^\ell}\right)^2.}     \tag{1.3}
\]

This also covers a dihedral symmetry interchanging the two modified
segments: it is already one of the at most (2m) global symmetries.

Here is the recovery argument, included to make the quotient accounting
literal.  The star quartets are intrinsically the four-cliques whose
members have a common ((R-1))-intersection; the exact clique
classification says that these are precisely the canonical lower cells.
Intersecting their four members therefore recovers the unordered family
of cores

\[
 A_i=B_i\cup\cdots\cup B_{i+r-1}.
\]

Because (2r=m-h<m), one has (r<m/2).  For two distinct cores put
(d=\min\{|i-j|,m-|i-j|\}).  Then

\[
 |A_i\mathbin\triangle A_j|=
 \begin{cases}
 4d,&1\le d\le r,\\
 4r,&r\le d\le m-r.
 \end{cases}                                           \tag{1.4}
\]

(At (d=r) the two formulas agree.)  Thus symmetric difference four
occurs exactly for cyclically consecutive cores.  The graph on the
recovered cores defined by this relation is the original (m)-cycle, so
its order is determined up to rotation and reflection.  After choosing
one of those (2m) dihedral presentations,

\[
 B_i=A_i\setminus A_{i+1},
 \qquad B_{i+r}=A_{i+1}\setminus A_i,                 \tag{1.5}
\]

which recovers every unordered domino.  This proves, rather than assumes,
the multiplicity bound used in (1.3).

## 2. Exact bad-core union

For a segment (Q) of domino positions, an (r)-block core can change
only if its block-index interval meets (Q) nontrivially without
containing all of (Q).  Put

\[
 L=\{1,2,\ldots,\ell-1\}.
\]

For (I), the two partial-intersection fronts are

\[
 L\cup(L-r).                                            \tag{2.1}
\]

Indeed (L) consists of starts whose left endpoint cuts (I), while
(L-r) consists of starts whose right endpoint cuts (I).  Translating
the segment by (r) gives

\[
 (L+r)\cup L                                            \tag{2.2}
\]

for (J).  Thus the full set of possibly changed core starts is

\[
 L\cup(L-r)\cup(L+r).                                   \tag{2.3}
\]

Condition (1.1) makes (L) disjoint from both remote bands.  Moreover

\[
 2r=m-h
 \quad\Longrightarrow\quad
 L+r\equiv(L-r)-h\pmod m.                               \tag{2.4}
\]

The union of two cyclic intervals of length \(\ell-1\) whose relative
shift is (h) has size

\[
 (\ell-1)+\min\{\ell-1,h\}.
\]

Adding the disjoint middle band proves the exact count

\[
 \boxed{
 |L\cup(L-r)\cup(L+r)|
 =2(\ell-1)+\min\{\ell-1,h\}.}                         \tag{2.5}
\]

The word “exact” here refers to the union of starts at which a core is
allowed to change.  A special repartition may accidentally preserve an
additional core, which only increases its overlap with (F) and does
not weaken the obstruction.

## 3. Boundary exceptions

For (I), a cell whose core is not in (2.1) can still change through a
boundary domino only at the two starts

\[
 \ell\quad\text{and}\quad-r.
\]

To see this, the left boundary condition (i-1\in I) gives
(i\in L\cup\{\ell\}), and the right boundary condition (i+r\in I)
gives (i\in(L-r)\cup\{-r\}).  The points in the two (L)-bands were
already counted.  Translating by (r), segment (J) contributes at
most the two further starts

\[
 \ell+r\quad\text{and}\quad0.
\]

Thus there are at most four boundary-only exceptions.  Every other cell
has the same core union—it contains all or none of each modified label
set—and the same two boundary dominoes.  It is therefore literally the
same complete four-target cell in (F) and (G).

If (b_\ell) is the number of cells which may change, then

\[
 \boxed{
 b_\ell\le
 2(\ell-1)+\min\{\ell-1,h\}+4.}                        \tag{3.1}
\]

Since the four-target cells of (F) are disjoint,

\[
 |F\setminus G|\le4b_\ell
 \le s_\ell:=8\ell+4\min\{\ell-1,h\}+8.             \tag{3.2}
\]

No assumption about partial coincidences inside a changed cell is used;
such coincidences again improve the overlap.

## 4. Half-exponent calculation

Stirling's formula applied to (1.3) gives

\[
 \log|\mathcal F_\ell|
 =4\ell\log\ell+O(\ell+\log m).                        \tag{4.1}
\]

When (h=o(\ell)=o(m)), (3.2) gives

\[
 s_\ell=8\ell+4h+8,                                    \tag{4.2}
\]

and hence

\[
 \frac{\log|\mathcal F_\ell|}{s_\ell\log n}
 =\frac12-o(1).                                        \tag{4.3}
\]

Take

\[
 \ell=\frac{m}{\sqrt{\log m}}.
\]

Then (h=o(\ell)), (s_\ell=o(m)), and

\[
 \log|\mathcal F_\ell|
 =(4+o(1))m\sqrt{\log m}.                              \tag{4.4}
\]

For every fixed (c<1/2), the logarithm of the right side of (0.1) is

\[
 O(m)+c(8+o(1))m\sqrt{\log m},                         \tag{4.5}
\]

which is smaller than (4.4) for all sufficiently large (m).  This
rigorously refutes (0.1).

### 4.1 Exact consequence at the terminal scale

The same construction gives a useful statement even when one restricts
attention to

\[
 s_A=\left\lceil {A m\over\log m}\right\rceil
\]

for a fixed positive constant (A).  Choose

\[
 \ell=\left\lfloor {s_A-4h-8\over8}\right\rfloor.
\]

Indeed, in the regime (h<\ell), (3.1) gives
(4b_\ell\le8\ell+4h+8).  Thus every member of the
double-segment family has defect at most (s_A), while
(h=O(\sqrt m)) gives

\[
 \ell={A m\over8\log m}+o\!\left({m\over\log m}\right).
\]

Equation (4.1) therefore yields the explicit lower estimate

\[
 \boxed{
 \log |B_{s_A}(F)|
 \ge {A\over2}m
      -{A\over2}{m\log\log m\over\log m}
      -O_A\!\left({m\over\log m}\right).}
 \tag{4.6}
\]

Indeed, substitute
(\log\ell=\log m-\log\log m+\log(A/8)+o(1)) into
(4\ell\log\ell+O(\ell+\log m)); the subtraction of (4h+O(1))
from the defect budget changes the logarithm by only
(O_A(h\log m)=o(m)).

Consequently, if a terminal-scale estimate has the explicit form

\[
 |B_{s_A}(F)|\le
 \exp(C_*m+o(m))\,n^{c s_A},                           \tag{4.7}
\]

then necessarily

\[
 \boxed{C_*\ge(1/2-c)A.}                              \tag{4.8}
\]

Thus a separate bound for one prescribed (A) is not formally refuted if
its exponential constant is allowed to depend on (A).  But the usual
macro-thinning plan needs one (C_*) uniform in (A) and then chooses (A)
large compared with it.  Equation (4.8) proves that this particular
choice-of-(A) escape cannot work using raw overlap alone.

## 5. Relation to the star-to-top collar

A single cross-shore star-to-top edge fixes its top carrier but leaves
two endpoint mate labels.  Its immediate two-star collar can be chosen
to have six noncommon targets, giving the sharp local ratio

\[
 \frac{6\text{ missing targets}}{2\text{ free labels}}=3.
\]

For one independently repartitioned segment, its two moving core fronts
are disjoint and the corresponding local charges are essentially
additive.  For the pair (I,I+r), the four nominal fronts reduce to

\[
 L,\quad L-r,\quad L+r,
\]

and the last two differ by only (h).  Thus when \(\ell\gg h\), two
families of local collars charge the same remote targets on all but an
(O(h)) fringe.  The effective global cost drops to approximately two
missing targets per free coordinate label, exactly the critical
(1/2) exponent.

Therefore the three-target deferred-mate theorem is correct locally but
cannot be summed without an overlap correction.  A finite local
high-order cutoff or a pointwise common-event bound does not remove this
arithmetic front collision.

## 6. Exact surviving statement

The following static lane is closed negatively:

> There is no uniform (c<1/2) close-neighbour list bound depending only
> on (s=|F\setminus G|), even after complete-cell global alignment and
> even in the simple-support quotient.

For one prescribed (A), the obstruction does not determine the optimal
additive constant at the terminal scale (s=A m/\log m).  It does,
however, force the lower bound (4.8), and therefore rules out a constant
uniform in (A) that could later be beaten merely by taking (A) larger.
The exact remaining alternatives are therefore:

1. prove a terminal-scale list bound with its additive constant exposed;
2. quarantine the paired (r)-separated segments as one cluster, so the
   common remote front is charged only once; or
3. use trajectory information which forbids the two independent
   repartitions from surviving simultaneously.

No near-factor or coefficient-one conclusion is claimed.
