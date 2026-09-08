# Audit: integral strip ports and the literal annulus compiler

Date: 2026-07-26

Audited source:
`MATH_THEOREM_FINE_STRIP_INTEGRAL_PORT_SPARSIFICATION_AND_ANNULUS_MATCHING_GATE_20260726.md`.

## Verdict

The rankwise port construction and the implication

\[
 \text{port matching with nonmiddle leave }o(W)
 \quad\Longrightarrow\quad
 \text{literal central word of length }W+o(W)
\]

are correct, provided the compiler hypothesis

\[
                              H/h=o(1)                 \tag{A.1}
\]

is stated.  The source's opening criterion originally omitted (A.1), even
though Theorem 5.1 used it.  That opening statement has now been patched.

There is no hidden middle leave and no chronology repair.  There is one
important structural qualification: the port hypergraph is generally
**nonuniform**.  Formula (4.1) is an upper bound on its variable edge
sizes, not a common uniformity.  Consequently no uniform-hypergraph
matching theorem follows merely from the displayed degrees and width.
This does not affect the conditional compiler.

## 1. Total unimodularity check

Fix a sign and depth.  The variables are the edges of the bipartite
incidence graph (G_q^\epsilon).  The constraints are

\[
 \sum_{C\ni T}z_{C,T}=D_1,
 \qquad
 \lfloor2h\theta_q\rfloor
 \le \sum_{T\in C}z_{C,T}
 \le \lceil2h\theta_q\rceil,
 \qquad 0\le z\le1.                                \tag{A.2}
\]

The constant vector (z=\theta_q=D_1/D_q) is feasible because target
degree is (D_q) and strip degree is (2h).  After changing the signs of
the rows on one bipartite shore, the non-bound part of the matrix is the
directed node--edge incidence matrix.  Repeating a row with opposite sign
for lower and upper inequalities and adjoining identity rows preserve
total unimodularity.  All right-hand sides are integral.  Hence (A.2) has
a (0)-(1) vertex.

At (q=1), (D_q=D_1) and (	heta_1=1).  Every target equality then
forces all of its incident edge variables to one, so the complete
depth-one incidence graph is retained.  Thus the TU conclusion, including
the claimed floor/ceiling strip degrees and the all-port first shadow, is
valid.

The degree formulae are also consistent:

\[
 2hM=N_qD_q,
 \qquad
 {D_q\over D_1}={N_1\over N_q},
 \qquad
 2hM=WD_0=N_1D_1.                                  \tag{A.3}
\]

Therefore every nonmiddle target has port degree (D_1), every middle
owner has degree (D_0=(N_1/W)D_1), and (x_C=1/D_1) is indeed a
fractional matching.

## 2. Edge-size check

Ranks and signs are disjoint vertex classes, so for each strip

\[
 |e_C^\#|
 =2h+\sum_{q=1}^{H}\sum_{\epsilon\in\{-,+\}}
        d_{P_q^\epsilon}(C).                       \tag{A.4}
\]

Each summand is one of the two adjacent integers bracketing
(2hN_q/N_1).  Hence

\[
 |e_C^\#|
 \le 2h+4h\sum_{q=1}^{H}{N_q\over N_1}+2H
 =O(h\sqrt m+H).                                   \tag{A.5}

This verifies the displayed width.  But the independent TU choices can
give different rounding patterns to different strips, so (A.4) need not
be constant in (C).  The object is a simple nonuniform hypergraph with
bounded edge size.  It may be padded with private vertices if a theorem
requires formal uniformity, but such padding does not manufacture the
regularity or leave estimate required by an almost-perfect matching
theorem.  The annulus matching statement therefore remains a genuine
open gate.

Also, a port matching makes only the **certified** target occurrences
disjoint.  Two chosen strips can overlap through uncertified deep
occurrences.  This is harmless for covering and for the literal compiler,
but it must not be restated as physical disjointness at every depth.

## 3. No hidden middle leave

Let (s) be the number of matching edges and (L^\#) the total number of
unmatched nonmiddle target vertices.  Because every depth-one occurrence
is a port, the matching meets exactly (2hs) distinct targets on each
depth-one side.  Thus, writing (L_1^\pm) for the two depth-one leaves,

\[
 L_1^-=L_1^+=N_1-2hs,
 \qquad
 2(N_1-2hs)\le L^\#.                               \tag{A.6}
\]

Middle vertices in matching edges are disjoint, so exactly (2hs)
middle owners are used.  Their leave is therefore

\[
 \begin{aligned}
 L_0
 &=W-2hs\\
 &=(W-N_1)+(N_1-2hs)\\
 &\le {W\over m+1}+{L^\#\over2}=o(W).              \tag{A.7}
 \end{aligned}

Hence the hypothesis (L^\#=o(W)) automatically controls the otherwise
unstated middle leave.  No assumption that the matching saturates middle
owners is needed.

## 4. Literal chronology and exact length

For one physical strip, the block

\[
 A_0,\ldots,A_{2h-1},A_0,\ldots,A_{2H-1}           \tag{A.8}
\]

has length (2h+2H).  The consecutive-union identity for the (A_i)'s
realizes every physical strip target through depth (H), with every
witness wholly inside (A.8).  Consequently uncertified incidences cause
no difficulty: selecting a strip supplies its entire physical block, not
only its ports.

A matched port target is physically covered.  Therefore actual
nonmiddle holes form a subset of the (L^\#) unmatched port vertices.
Append those actual holes and the (L_0=W-2hs) uncovered middle targets
as singleton letters.  The total length is at most

\[
 \begin{aligned}
 (2h+2H)s+(W-2hs)+L^\#
 &=W+2Hs+L^\#\\
 &\le W+{H\over h}W+o(W)
  =W+o(W),                                         \tag{A.9}
 \end{aligned}

where (2hs\le W) and (A.1) are used.  Concatenating strip blocks cannot
destroy their internal witnesses, and each singleton witnesses itself.
Thus there is no seam or chronology gap.

## 5. Exact proved/open boundary

The following claims survive the audit:

1. exact integral port thinning at every rank and sign;
2. the target and middle degree formulae and the fractional matching;
3. the variable-edge upper bound (O(h\sqrt m+H));
4. automatic (o(W)) middle leave from an (o(W)) nonmiddle leave; and
5. the literal (W+o(W)) compiler under (H/h=o(1)).

What remains unproved is precisely the existence of the required matching
in this nonuniform, nested-flag port hypergraph.  The TU theorem does not
round the fractional hypergraph matching; it only constructs the ports.

