# Minimum upper-safe aligned folded-C8 face: exact graded gate

Date: 2026-08-01  
Lane: H2, regenerative split/history audit  
Status: exact scoped computation and elementary screen lemma.  This note does
not retract the full graded four-relabelled-octagon relation.  It audits one
quotient-folded physical path face and two proposed host realizations.

## 0. Verdict

Among all folded Hamilton openings which

1. retain all sixteen local upper support values, and
2. put each phase pair of directed-ray bases at the same source address,

the exact minimum maximal-source graded distance is

\[
                    \|D(S_0)-D(S_1)\|_1=22d+44.       \tag{0.1}
\]

There are four symmetry-equivalent minimizers.  The canonical row has

\[
               p=4d+10,\qquad q=5d+10,                \tag{0.2}
\]

while the independently reported row `p=4d+13,q=5d+13` is another one of
the same four minima.  Thus `+10` versus `+13` was a choice of symmetric
representative, not a numerical discrepancy.

Let `G_0,G_1` be the two-host ray words and combine them in the opposite
phase.  Then

\[
\begin{aligned}
 \|D(G_1)-D(G_0)\|_1&=4d-4,\\
 \|D(S_0)+D(G_1)-D(S_1)-D(G_0)\|_1&=18d+48.           \tag{0.3}
\end{aligned}
\]

The second line has positive and negative mass `9d+24`, supported on
`4d+11` graded keys on each side.  On either sign, the total coefficient
weights by width are

\[
 1,2,\underbrace{3,\ldots,3}_{3d+6\text{ widths}},2,1
 \quad\hbox{at widths}\quad 2d+4,\ldots,5d+13.        \tag{0.4}
\]

The exact key refinement of (0.4) is:

- width `2d+4`: `[1]`;
- width `2d+5`: `[1,1]`;
- widths `2d+6,...,3d+5`: `[1,2]`;
- widths `3d+6,...,5d+11`: `[3]`;
- widths `5d+12,5d+13`: `[2]`, `[1]`.

Across both signs, the absolute-coefficient histogram is

\[
       1^{,2d+8}\;2^{,2d+2}\;3^{,4d+12}.          \tag{0.5}
\]

Consequently the opposite two-host gadget cancels the exclusive **set
support** rays but does not cancel their graded address history.

## 1. Literal canonical row

Suppress a common core.  The ray bases at (0.2) are

\[
\begin{array}{ll}
 L_0=za_3f_1,&L_1=za_1f_1,\\
 R_0=za_1f_d,&R_1=za_3f_d,
\end{array}                                             \tag{1.1}
\]

and the phase-common corridor between them is

\[
       zf_1f_2,\ zf_2f_3,\ldots,\ zf_{d-1}f_d.        \tag{1.2}
\]

The exact common caps are

\[
             X_L=za_1a_3f_1,\qquad X_R=za_1a_3f_d.    \tag{1.3}
\]

In the audit's literal integer encoding, the common opened edge is

\[
 \{z,a_2,10,12,\ldots,d+11\}
 \longleftrightarrow
 \{z,a_2,11,12,\ldots,d+11\}.                          \tag{1.4}
\]

The unique inclusion-minimal one-letter active screen which equalizes both
the prefix and suffix chains is

\[
                         H=\{a_1,a_3\}.                \tag{1.5}
\]

Both labels in (1.5) are forced: the old/new left bases differ by
`a3/a1`, and the right bases differ by `a1/a3`.

The opposite ray gadget is

\[
 G_e=(X_L,L_e,zf_2,zf_3,\ldots,zf_{d-1},R_e,X_R).      \tag{1.6}
\]

Its set-deck identities are exact:

\[
\begin{aligned}
 \operatorname{Deck}(S_0)\setminus\operatorname{Deck}(S_1)
   &=\operatorname{Deck}(G_0)\setminus\operatorname{Deck}(G_1),\\
 \operatorname{Deck}(S_1)\setminus\operatorname{Deck}(S_0)
   &=\operatorname{Deck}(G_1)\setminus\operatorname{Deck}(G_0),
\end{aligned}                                           \tag{1.7}
\]

so the two direct-sum support unions agree.  Equations (0.3)--(0.5) are the
remaining multiplicity/address residue.

## 2. Common screens cannot change this residue

The following elementary statement is independent of the C8 construction.

**Screen lemma.**  Let `W,W'` be two words and let the same exterior screen
letter `H` be placed at both ends.  If

\[
 H\cup\operatorname{prefix}_j(W)
   =H\cup\operatorname{prefix}_j(W'),\qquad
 H\cup\operatorname{suffix}_j(W)
   =H\cup\operatorname{suffix}_j(W')                    \tag{2.1}
\]

pointwise, then

\[
 D(H|W|H)-D(H|W'|H)=D(W)-D(W').                        \tag{2.2}
\]

Indeed, the internal intervals give the right-hand side.  Every newly
left-crossing interval cancels by the prefix equality, every newly
right-crossing interval cancels by the suffix equality, and the one interval
crossing both screens cancels by either terminal equality.

For `S0|G1` versus `S1|G0`, and also in the reverse block order, (2.1) holds
with `H={a1,a3}` or `H={z,a1,a3}`.  Equation (2.2) proves that the graded
distance remains exactly `18d+48`.  Thus a common pointwise prefix/suffix
screen is context-safe but cannot pay this history debt.

## 3. Direct in-place wrap is a different construction

At the two source addresses (0.2), form the literal in-place wrap

\[
\begin{array}{c|cc}
 &p&q\\ \hline
 \text{old}&(L_0,L_1)&(R_1,R_0)\\
 \text{new}&(L_1,L_0)&(R_0,R_1).
\end{array}                                             \tag{3.1}
\]

This is not the direct sum of Section 1: every later source address shifts,
and new intervals cross the inserted letters.  Its exact ungraded support
residue in each direction is

\[
       2\quad(d=2),\qquad 8(d-2)\quad(d\ge3),           \tag{3.2}
\]

giving the observed `2/2` and `8/8` at `d=2,3`.  Its graded distance is

\[
 \|D(W_0)-D(W_1)\|_1=
 \begin{cases}
 82,&d=2,\\
 4d^2+28d+6,&d\ge3.
 \end{cases}                                            \tag{3.3}
\]

Adding the common screen (1.5) at both ends makes prefix and suffix chains
pointwise equal but changes neither (3.2) nor (3.3).  Hence the direct-wrap
support counts do not contradict (0.3): they measure another word pair.

## 4. Comparison with the canonical unsafe aligned row

The previously frozen aligned row at

\[
                         4d+12,\ 5d+12                \tag{4.1}
\]

retains only fifteen upper support values.  Its three exact distances are

\[
                   10d+12,\qquad4d-4,\qquad6d+16,      \tag{4.2}
\]

and the last residue has one positive and one negative unit at every width
`2d+5,...,5d+12`.  The corrected tradeoff is therefore:

- aligned and small residue: upper-unsafe, (4.2);
- upper-safe and same-address: source `22d+44`, residual `18d+48`;
- upper-safe with the previously recorded minimum `10d+20`: ray addresses
  are phase-displaced, so it is not a same-address host row.

## 5. Regenerative scope

The original four-relabelled C8 macro relation still has full graded OR
equality and action `4g8`.  Folding to simple owners, opening a Hamilton
path, and taking maximal erosion are extra physical operations; the
relations audited here are their resulting source interfaces.

This audit proves no bounded-`chi` regenerative reset.  It proves the sharper
conditional statement that common exterior screening contributes **zero**
graded correction to this face, while the surviving direct-sum debt is
linear in `d`.  A positive bounded-sidecar theorem must therefore use at
least one feature absent here: a phase-sensitive collar, address-changing
transport, overlap/quotient identification of graded keys, or another
upper-strict physical weave.  It is not enough to recycle common screens
around the present two hosts.

## 6. Replay

Run

```text
PYTHONPATH=scratch python3 \
  scratch/audit_h2_c8_folded_upper_safe_aligned_graded_gate_20260801.py \
  --write
```

The replay enumerates every folded candidate for `2<=d<=12`, proves the
four-minimizer reconciliation, checks the literal anchors/corridor/cut,
verifies (0.1)--(0.5), checks both direct-sum block orders and both common
screens, replays (3.1)--(3.3), and rechecks the unsafe control (4.2).
