# The exact synchronized outer-carrier cell and its critical unit mode

Date: 2026-07-25  
Method: pure mathematics only; no computation or search

## 0. Result

The one-block localization formerly proposed for the outer-carrier
reconstruction is false by Proposition 4.2 of
`MATH_ATTACK_QST_TWO_SEAM_TRANSFER_KERNEL_20260725.md`.  This note derives
the transfer object which survives that counterexample.

The common outer carrier has two simultaneous block parsings.  After the
heights inside the current forward and dual blocks are synchronized, a
full cell of unmatched height (q) has the exact endpoint resolvent

\[
 \mathbf G_q(x)=\frac1{F_{q+1}(x^2)}
 \begin{pmatrix}
  F_q(x^2)&x^q\\
  x^q&F_q(x^2)
 \end{pmatrix}.                                      \tag{0.1}
\]

Consuming the unique separator at the chosen endpoint multiplies this
matrix by (x).  At the critical point,

\[
 \boxed{
 \mathbf P_q:=\frac12\mathbf G_q(1/2)
 =\frac1{q+2}
 \begin{pmatrix}q+1&1\\1&q+1\end{pmatrix}.}          \tag{0.2}
\]

Thus

\[
 \lambda_+(q)=1,
 \qquad
 \lambda_-(q)=\frac q{q+2}.                         \tag{0.3}
\]

The synchronized transfer is critical, not subcritical.  More precisely,
the total critical source-to-sink mass of the **marked** full-cell killed
automaton is

\[
 \boxed{\Theta(s).}                                  \tag{0.4}
\]

Both bounds in (0.4) are uniform and elementary.  The lower bound is
carried by an explicit family which completes several forward blocks,
crosses once from the forward to the dual boundary, and then completes all
remaining dual blocks.  Each central source has order-one total mass, and
there are order (s) central sources.  The upper bound follows because
every critical cell matrix is stochastic and every separator decreases one
of the two block indices.

The source does not supply a hidden reciprocal-height factor.  If the
outer carrier starts in (\overline T_h), then after its first displayed
zero the synchronized height is (q=h+1).  The exact critical mass of the
arbitrary legal prefix of (T_h), including that zero, is

\[
 \boxed{\frac{s-2h}{s-h+1},}                         \tag{0.5}
\]

whenever (0\le h\le(s-2)/2).  It is bounded away from zero on every
fixed subinterval (h\le(1/2-\varepsilon)s).  The factor (1/(h+3))
arises only after imposing the false one-block *first-hit* condition.  In
the correct spanning parser, the only reciprocal-height factor is the
off-diagonal crossing entry (1/(q+2)) in (0.2); charging another such
factor at the source double counts the same crossing restriction.

Consequently the exact two-dimensional synchronized capped-carrier
relaxation cannot prove an (o(s)) outer-carrier series.  A proof of

\[
 \mathcal Z_s^+(x)\preceq
 K^\times_{s,t_s,u_s}(x)\Psi_s(x),
 \qquad \Psi_s(1/2)=o(s),                            \tag{0.6}
\]

must use an additional PBBS chronology restriction which removes the
unit mode (0.3), or must show that actual boundary vectors have vanishing
projection onto the explicit corner family.  Height caps, literal equality
of the shared carrier, and unique separator parsing do not suffice.

This is a no-go for the synchronized capped relaxation, not a construction
of a Catalan-dense family of genuine PBBS returns.  The word "marked" is
essential: one formal dual tuple may admit more than one candidate start
cut.  An actual return supplies one distinguished outer-carrier cut, so
the marked relaxation is a valid upper language, but its lower-bound words
need not be distinct actual roots.

## 1. Rank accounting with the outer carrier counted once

Retain the exact zero-winding notation

\[
 \mathcal A=(\overline T_{s-1}0)\cdots(\overline T_00),
 \qquad
 \mathcal C=(0S_s)(0S_{s-1})\cdots(0S_1),            \tag{1.1}
\]

and

\[
 \mathcal A=R_sO,
 \qquad
 \mathcal C=OR_0.                                   \tag{1.2}
\]

Let (e_j=|T_j|+1).  The exact dual staircase gives

\[
 \sum_{j=0}^{s-1}e_j=M_0-M_s=\delta(D_0),            \tag{1.3}
\]

because (M_0=\delta(D_0)) and (M_s=0).  Therefore

\[
 |\mathcal A|=\delta(D_0).                           \tag{1.4}
\]

Since (D_0=P_01R_00),

\[
 |R_0|=2m-\delta(D_0)-1.                             \tag{1.5}
\]

It follows that

\[
 \boxed{|\mathcal A R_0|=2m-1.}                     \tag{1.6}
\]

The tuple of dual blocks changes the last separator of every
(\overline T_j0) to (1) and thereby reconstructs (P_01); appending
the last zero reconstructs (D_0).  Thus one separator together with

\[
 W:=\mathcal A R_0=R_sOR_0=R_s\mathcal C             \tag{1.7}
\]

is a length-preserving encoding of the root data.  In particular, the
shared outer carrier (O) occurs exactly once in (1.7).  All transfer
matrices below count literal bits of (W) once.

There is a useful lifted-path interpretation.  Read (W) from height
(2s-1).  Before the block (\overline T_j), the height is (s+j).
The cap

\[
 \operatorname{ht}(T_j)\le s-1-j                    \tag{1.8}
\]

keeps this complemented excursion above

\[
 s+j-(s-1-j)=2j+1>0.                                \tag{1.9}
\]

After the (s) dual separators the height is (s-1).  The word (R_0),
shifted down by one from its native terminal corridor, stays in
([0,s-1]) and ends at zero.  Hence (W) is a nonnegative walk from
(2s-1) to zero.  This verifies (1.6) at the level of net height as well
as length.

## 2. The exact synchronized state and lattice domain

Inside the overlap (O), suppose the forward parser is in (S_p) and
the dual parser is in (\overline T_j), where

\[
 1\le p\le s,
 \qquad 0\le j\le s-1.                              \tag{2.1}
\]

In the lifted path, (S_p) is based at height (p-1), whereas
(\overline T_j) is based at height (s+j).  Let

\[
 c=\text{height in }S_p,
 \qquad
 t=\text{height in }T_j.                            \tag{2.2}
\]

Literal equality of the two carrier readings gives

\[
 p-1+c=s+j-t.
\]

Equivalently,

\[
 \boxed{t+c=q,
 \qquad q:=s+j-p+1.}                                \tag{2.3}
\]

Within a cell, a literal zero is an up-step for (T_j) and a down-step
for (S_p), while a literal one is the reverse.  Thus (t) performs a
nearest-neighbour walk and (t+c=q) is invariant until a separator is
consumed.

The two height caps give the exact interval

\[
 \boxed{
 \max(0,q-p)\le t\le\min(q,s-1-j).}                 \tag{2.4}
\]

The dual boundary is (t=0).  The forward boundary is (c=0), or
(t=q).  Both boundaries are present precisely in a **full cell**:

\[
 \boxed{1\le q\le\min(p,s-1-j).}                   \tag{2.5}
\]

At the dual boundary, consuming the dual separator sends

\[
 (p,j,q)\longmapsto(p,j-1,q-1).                    \tag{2.6}
\]

At the forward boundary, consuming the forward separator sends

\[
 (p,j,q)\longmapsto(p-1,j,q+1).                    \tag{2.7}
\]

Equations (2.3), (2.6), and (2.7) show that the exact block-level state
is two-dimensional: one may retain ((j,q)), since
(p=s+j-q+1).  The coordinate (q) is the unmatched height and (j) is
the current dual-block index.  Truncated cells use the interval (2.4),
so they can only kill paths relative to the full-cell relaxation.

Both moves strictly decrease (p+j).  The synchronized transfer is
therefore a finite acyclic killed automaton even though each cell contains
an arbitrary finite-path Green kernel.

## 3. Exact full-cell transfer and Perron calculation

Let (F_0=F_1=1) and (F_{r+1}=F_r-zF_{r-1}).  In a full cell, the
resolvent of the path (0,1,\ldots,q), restricted to its two endpoints,
is

\[
 \mathbf G_q(x)
 =\begin{pmatrix}
  ((I-xA)^{-1})_{0,0}&((I-xA)^{-1})_{0,q}\\
  ((I-xA)^{-1})_{q,0}&((I-xA)^{-1})_{q,q}
 \end{pmatrix}
 =\frac1{F_{q+1}(x^2)}
 \begin{pmatrix}
  F_q(x^2)&x^q\\x^q&F_q(x^2)
 \end{pmatrix}.                                    \tag{3.1}
\]

The diagonal entry is the bounded-height Dyck series (C_q); the
off-diagonal entry is the endpoint corridor series (G_q).  This proves
(3.1) either by Cramer's rule or by the unique continuant minors.

Exactly one separator is consumed after choosing the exit endpoint, so
the cell transition is (x\mathbf G_q(x)).  At (x=1/2),

\[
 F_q(1/4)=\frac{q+1}{2^q},
 \qquad
 F_{q+1}(1/4)=\frac{q+2}{2^{q+1}}.                 \tag{3.2}
\]

Substitution gives (0.2).  In particular,

\[
 \mathbf P_q\binom11=\binom11,
 \qquad
 \mathbf P_q\binom1{-1}=\frac q{q+2}\binom1{-1}. \tag{3.3}
\]

The entries have the direct interpretation

\[
 a_q:=\frac{q+1}{q+2}
 \quad\text{(exit on the same side)},
 \qquad
 b_q:=\frac1{q+2}
 \quad\text{(cross to the other side)}.            \tag{3.4}
\]

Their sum is one.  Thus the full-cell critical automaton is a persistent
walk: the chosen side is retained with probability (a_q), is switched
with probability (b_q), and (q) changes by (+1) after a forward
exit and by (-1) after a dual exit.

This calculation locates the precise reciprocal-height factor.  It is
the off-diagonal entry (b_q), not an additional source factor.

## 4. Exact source coupling

The overlap begins with the forward separator before (S_s).  Suppose
this bit lies in (\overline T_h).  Immediately after it, the forward
height is (c=0).  Equation (2.3), with (p=s,j=h), gives

\[
 q=h+1,
 \qquad t=h+1.                                      \tag{4.1}
\]

Before the displayed zero, the prefix of (T_h) is an arbitrary walk
from zero to (h), confined to

\[
 0\le t\le H,
 \qquad H=s-1-h.                                    \tag{4.2}
\]

It is not a first-passage path.  Its exact resolvent entry is

\[
 B_{H,h}(x)=\frac{x^hF_{H-h}(x^2)}{F_{H+1}(x^2)}.  \tag{4.3}
\]

The displayed zero contributes one further factor (x).  At the critical
point,

\[
 \begin{aligned}
 xB_{H,h}(x)\big|_{x=1/2}
 &=\frac{s-2h}{s-h+1}.                              \tag{4.4}
 \end{aligned}
\]

Indeed, substitute (H=s-1-h) into (4.3) and use (3.2).  For every fixed
(\varepsilon>0), (4.4) is bounded below by a positive
(c_\varepsilon) whenever

\[
 0\le h\le(1/2-\varepsilon)s.                      \tag{4.5}
\]

The false one-block parsing replaced (4.3) by a first-passage kernel and
thereby manufactured (1/(h+3)).  Proposition 4.2 shows why that
replacement is illegal.  Formula (4.4) is the floor- and separator-correct
source calculation.

At the cell endpoint itself, the forward source vector is
(e_F=(0,1)^T) (up to ordering).  Its projection onto the invariant vector
((1,1)^T/\sqrt2) is exactly (1/\sqrt2).  The terminal dual vector has
the same projection.  Thus neither endpoint is orthogonal to the unit
mode.

The external source normalization does not alter this conclusion.  The
complete dual blocks before the cut have caps

\[
 0,1,\ldots,s-h-2.
\]

Including their separators, their exact critical mass is

\[
 \prod_{a=0}^{s-h-2}\frac12C_a(1/4)
 =\frac1{s-h}.                                      \tag{4.6}
\]

Indeed the (a=0) term is (1/2), and the remaining terms telescope.
Thus the full source prefix has mass

\[
 \frac1{s-h}\frac{s-2h}{s-h+1}.                   \tag{4.7}
\]

On every central range used below, this is a bounded nonzero multiple of
the ordinary first-passage mass

\[
 A_{s-h-1}(1/2)=\frac1{s-h}.                       \tag{4.8}
\]

There is an equally exact sink calculation.  Suppose the dual parser has
just consumed the final (T_0)-separator and the surviving forward state
is in (S_p) at height (L).  The compatible suffix first completes
(S_p) from height (L) to zero and then contains the blocks

\[
 (0S_{p-1})\cdots(0S_1).
\]

Its generating function is

\[
 \mathsf K_{p,L}^{\rm sink}(x)
 =\frac{x^LF_{p-L}(x^2)}{F_{p+1}(x^2)}
   \prod_{a=1}^{p-1}xC_a(x^2).                    \tag{4.9}
\]

Therefore

\[
 \boxed{
 \mathsf K_{p,L}^{\rm sink}(1/2)
 =\frac{4(p-L+1)}{(p+1)(p+2)}.}                   \tag{4.10}
\]

For the corner paths below, (p=s-L) and (L\in[s/10,s/8]).  Hence

\[
 \frac{\mathsf K_{p,L}^{\rm sink}(1/2)}
 {G_{s-1}(1/2)}
 =\frac{2(s+1)(p-L+1)}{(p+1)(p+2)}                \tag{4.11}
\]

is bounded above and below by positive absolute constants.  Thus, after
the ordinary external first-passage and terminal-corridor kernels are
factored out, both synchronized boundary vectors still couple to the unit
mode at order one.

## 5. A critical corner family

We now prove the lower bound in (0.4).  Start at

\[
 p=s,
 \qquad j=h,
 \qquad q_0=h+1,
 \qquad\text{on the forward side}.                 \tag{5.1}
\]

Fix (L\ge0).  Take (L) same-side forward exits, then one
forward-to-dual crossing, then (h) same-side dual exits.  After the
first (L) exits,

\[
 Q=h+1+L.                                           \tag{5.2}
\]

The crossing itself completes the dual block (T_h) and decreases the
dual index to (h-1).  The final (h) dual exits complete
(T_{h-1},\ldots,T_0).  Hence the path reaches the physical dual sink
after the last dual separator.

Its exact critical weight is

\[
 \begin{aligned}
 w_{h,L}
 &=\left(\prod_{q=h+1}^{h+L}a_q\right)
   b_{h+1+L}
   \left(\prod_{q=L+1}^{h+L}a_q\right)\\
 &=\boxed{
 \frac{(h+2)(L+2)}
 {(h+L+2)^2(h+L+3)}.}                              \tag{5.3}
\end{aligned}
\]

The first product is interpreted as one when (L=0); shifting either
endpoint by one changes only an absolute factor.  The displayed form
follows from

\[
 \prod_{q=a}^{b}\frac{q+1}{q+2}=\frac{a+1}{b+2}.   \tag{5.4}
\]

For definiteness, take

\[
 \frac{s}{10}\le h\le\frac{s}{8},
 \qquad
 \frac{s}{10}\le L\le\frac{s}{8}.                \tag{5.5}
\]

Every visited cell is full.  During the forward part this follows from

\[
 h+1+L\le s-1-h,
 \qquad
 h+1+L\le s-L.                                     \tag{5.6}
\]

During the dual part, (q) decreases while the dual cap increases and
(p=s-L) remains fixed, so (2.5) continues to hold.  Equations (5.3) and
(5.5) give

\[
 \frac{c}{s}\le w_{h,L}\le\frac{C}{s}.             \tag{5.7}
\]

For every fixed (h) in (5.5), summing over the (\Theta(s)) admissible
values of (L) gives source-to-dual-sink mass at least an absolute
constant.  There are (\Theta(s)) such values of (h).  Therefore

\[
 \boxed{\mathcal G_s^{F\to D}\ge c s.}             \tag{5.8}
\]

This family has a literal interpretation: it completes (L) successive
forward blocks while remaining in (T_h), crosses once through the current
full cell, and then completes all remaining dual blocks while remaining in
one forward block.  It therefore includes separator-spanning carriers and
counts their common literal word only once.

## 6. Matching upper bound

At criticality every full-cell matrix is stochastic.  A truncated cell is
obtained by killing some finite-path states or one endpoint, so its row
sums are at most one.  Moreover, every separator transition decreases
(p+j).  Hence the automaton is acyclic and, from a fixed source, the total
weight of all paths stopped on first arrival at any sink is at most one.

There are at most (s) possible source blocks (h).  Consequently

\[
 \boxed{\mathcal G_s^{F\to D}\le s.}               \tag{6.1}
\]

Combining (5.8) and (6.1) proves (0.4).

If the exact prefix factor (4.4) is included, the lower bound is unchanged
up to an absolute constant on the range (5.5).  Thus the source completion
does not suppress the corner family.

## 7. Consequence for OCR

The four-strip one-crossing kernel removes a critical factor of order
(s) from the unrestricted terminal corridor.  To close zero winding,
the residual outer-carrier transfer in (0.6) must have mass (o(s)).

The exact marked synchronized capped-carrier parser derived above has mass
(\Theta(s)).  Its failure is not an artefact of duplicating (O): the
rank identity (1.6) counts (O) once, and every cell matrix counts each
shared literal bit once.  Nor is it an artefact of a loose spectral bound:
the invariant eigenvalue in (0.3) is exactly one, and the source and sink
vectors have nonzero invariant projections.

Therefore a successful OCR theorem must impose a genuinely additional
PBBS condition.  One precise sufficient statement is:

> **Anti-corner chronology lemma (unproved).**  After the external four
> one-crossing pieces are fixed, the total critical mass of actual PBBS
> carrier paths which, on a central range of source blocks, follow the
> forward-corner/one-crossing/dual-corner itinerary of Section 5 is
> (o(s)).

Equivalently, actual chronology must either kill a (1-o(1)) fraction of
the invariant-mode mass, or make its physical boundary vector have
vanishing projection onto that mode.  The scalar height caps, shared-word
collision, and separator chronology proved so far do neither.

No coefficient-one conclusion is claimed.
