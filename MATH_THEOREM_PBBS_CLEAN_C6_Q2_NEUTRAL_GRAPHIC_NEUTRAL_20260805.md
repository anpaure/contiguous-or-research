# The explicit PBBS clean C6 is q2-neutral but graphic-neutral

**Date:** 2026-08-05  
**Method:** pure cyclic-parenthesis algebra and exact cut-and-reconnect
calculus; no computation or search  
**Status:** unconditional for `m>=4`.  The displayed clean C6 preserves the
entire selected q2 multiset, but it does **not** repair the graphic
cycle-hit obstruction.  Its three old edges lie on exactly two completely
selected PBBS components, and the switch replaces them by exactly two
completely selected components.

## 1. The clean C6

Work on `Z/(2m+1)Z`, put

\[
 K=\{1,\ldots,m-2\},\qquad
 (a_0,a_1,a_2)=(m-1,m,m+1),\qquad c=0,
\]

with subscripts modulo three, and define

\[
 R_i=K+a_i,qquad
 P_i=K+a_i+a_{i+1},\qquad
 Q_i=K+a_i+c.
\tag{1.1}
\]

The standard clean-C6 identities are

\[
 P_i\cap Q_i=R_i,qquad
 P_i\cap Q_{i+1}=R_{i+1}.
\tag{1.2}
\]

The old PBBS shore contains the directed factor edges

\[
                         P_i\longrightarrow Q_i,
\tag{1.3}
\]

and the clean switch replaces them by

\[
                         P_i\longrightarrow Q_{i+1}.
\tag{1.4}
\]

At `P_i`, the unchanged incoming q1 row is

\[
\begin{aligned}
 L_0&=\{2,\ldots,m\},\\
 L_1&=\{2,\ldots,m-2,m,m+1\},\\
 L_2&=\{2,\ldots,m-1,m+1\}.
\end{aligned}
\tag{1.5}
\]

Equivalently, `L_i=P_i-{1}`.

Direct forward/reverse cancellation verifies (1.3).  It also shows that
the max-height q1 rule selects every displayed old occurrence `R_i` and
every displayed outside occurrence `L_i`: in each deficit-three word the
current edge is obtained from the unique tallest block (using the
rightmost maximum inside that block).

## 2. Exact q2 effect

Put

\[
 A=\{2,\ldots,m-1\},\quad
 B=\{2,\ldots,m-2,m\},\quad
 C=\{2,\ldots,m-2,m+1\}.
\tag{2.1}
\]

Before the switch, the selected q2 turns at the three `P_i` are

\[
 (R_0\cap L_0,R_1\cap L_1,R_2\cap L_2)=(A,B,C).
\tag{2.2}
\]

After the switch they are

\[
 (R_1\cap L_0,R_2\cap L_1,R_0\cap L_2)=(B,C,A).
\tag{2.3}
\]

At `Q_i`, the incoming new edge is `P_(i-1)Q_i`, whose q1 colour is

\[
                         P_{i-1}\cap Q_i=R_i.
\tag{2.4}
\]

Thus the q1 row at every `Q_i` is pointwise unchanged.  These six endpoints
are all endpoints of changed factor edges.  Consequently (2.2)--(2.4)
prove the exact identity

\[
 \boxed{\text{the multiset of selected q2 turns is unchanged}.}
\tag{2.5}
\]

Transport the section by selecting all three new occurrences of the same
three labels `R_i` and leaving every other choice fixed.  The q1
one-occurrence condition and q2 completeness both survive exactly.  This
is stronger than a no-new-hole assertion: every q2 witness load is
unchanged.

## 3. The three old edges lie on exactly two PBBS components

Let `f` be PBBS, `g=f^2`, and represent a middle state by its unmatched
zero followed by a rooted Dyck word.  The state `P_0` has root zero and
shape

\[
                         1^m0^m.
\tag{3.1}
\]

It therefore lies on the single-soliton `g`-cycle `C_ss`, of length

\[
                         n=2m+1.
\tag{3.2}
\]

The states `P_2` and `P_1` have root zero and respective shapes

\[
 A_1=1^{m-1}010^{m-1},
 \qquad
 B_{m-2}=1^{m-2}0110^{m-1}.
\tag{3.3}
\]

To locate them exactly, define

\[
 A_j=1^{m-1}0^j1,0^{m-j}quad(1\le j\le m-1),
\]

\[
 B_j=1^j0,1^{m-j}0^{m-1}quad(1\le j\le m-2).
\tag{3.4}
\]

For the rooted PBBS map `phi`, direct first-maximum substitution gives

\[
 A_j\xrightarrow{m-1}B_j\xrightarrow{m+1}A_{j+1}
 \quad(1\le j\le m-2),
\]

and

\[
                         A_{m-1}\xrightarrow{m-1}A_1.
\tag{3.5}
\]

Hence the shape cycle has length

\[
                         p=2m-3
\tag{3.6}
\]

and total voltage

\[
 (m-1)^2+(m-2)(m+1)
   =(m-2)(2m+1)+1\equiv1\pmod{2m+1}.
\tag{3.7}
\]

It therefore lifts to one `f`-cycle of length `np`.  Both `n` and `p` are
odd, so the same set is one `g=f^2` component, denoted `C_ts`.  Since
`P_2` has shape `A_1` and `P_1` has shape `B_(m-2)`, the edges
`P_1Q_1` and `P_2Q_2` lie on this same component.  The single-soliton and
two-soliton components are distinct, for example by their different
peak-pruning profiles.

Thus the clean C6 touches exactly

\[
 \boxed{\text{one edge of `C_ss` and two edges of `C_ts`}.}
\tag{3.8}
\]

It is not a three-component merger.

## 4. The two-soliton component is also wholly selected

The following calculation is useful independently of this C6.  Every
outgoing q1 occurrence on `C_ts` is selected by the max-height rule.

For a root-zero state of shape `A_j`, `1<=j<=m-2`, its outgoing q1 row is

\[
 K^A_j=\{1,\ldots,m-2\}\cup\{m+j\}.
\tag{4.1}
\]

Its three forward-Dyck block heights are

\[
 (m-2,0,0)\quad(1\le j\le m-3),
 \qquad
 (m-2,1,0)\quad(j=m-2).
\tag{4.2}
\]

For `A_(m-1)`, the outgoing row is

\[
 \{1,\ldots,m-2,2m-1\}
\]

and the block heights are `(m-2,0,1)`.

For a root-zero state of shape `B_j`, `1<=j<=m-2`, its outgoing row is

\[
 K^B_j=\{1,\ldots,m\}\setminus\{j+1\}.
\tag{4.3}
\]

Its decomposition has one nonempty block of height `m-2` and two empty
blocks.  When `j=m-2`, the maximum occurs twice inside that same block;
the rightmost-maximum rule gives the current edge.

In (4.1) and its `A_(m-1)` endpoint case, that rightmost maximum is
followed by coordinate `m-1`; adjoining `m-1` and `0` gives respectively
the old state and its `g`-successor.  In (4.3), it is followed by
coordinate `m+1`; adjoining `m+1` and `0` again gives the old state and
its successor.  Thus these block comparisons identify the literal current
occurrence, not merely some occurrence with the same row label.

Since `m>=4`, the competing heights `0,1` are strictly smaller than
`m-2`.  Thus every edge in every spatial lift of every shape in (3.4) is
the globally chosen max-height occurrence of its q1 label.  Therefore

\[
                         o_{C_{ts}}(S)=0.
\tag{4.4}
\]

The single-soliton forced-cycle theorem already gives

\[
                         o_{C_{ss}}(S)=0.
\tag{4.5}

## 5. Exact cut-and-reconnect topology

Orient the old edges as `P_i->Q_i`.  On `C_ts`, the directed path from
`Q_1` to `P_2` has length

\[
                         p(m+1).
\tag{5.1}

Indeed, `Q_1` has rooted shape `A_1` with root `-1`, one full shape tour
of `f` raises the root by one, and

\[
 g^{p(m+1)}=f^{p(2m+2)}=f^p
\]

on this `np`-cycle.  The complementary path from `Q_2` to `P_1` has
length

\[
                         pm-2.
\tag{5.2}

Deleting the three old edges gives:

* the `n-1` edge path `Q_0 -> P_0` from `C_ss`;
* the path `Q_1 -> P_2` of (5.1); and
* the path `Q_2 -> P_1` of (5.2).

Installing `P_i->Q_(i+1)` produces exactly two cycles:

\[
 P_0\to Q_1\leadsto P_2\to Q_0\leadsto P_0,
\]

and

\[
                         P_1\to Q_2\leadsto P_1.
\tag{5.3}

Their lengths are respectively

\[
 n+p(m+1)+1=2m^2+m-1,
 \qquad
 pm-1=2m^2-3m-1.
\tag{5.4}

Thus the component count is unchanged: two old cycles become two new
cycles.

More decisively, every old position on both input components was selected,
and all three new q1 occurrences are selected.  Hence both new cycles have
omission count zero:

\[
 \boxed{o_{C'_1}(S')=o_{C'_2}(S')=0.}
\tag{5.5}

## 6. Verdict

The candidate clean C6 is a perfect **q2-transparent** carrier surgery,
but it is not a graphic repair:

\[
 \boxed{
 \text{q1 palette exact, q2 loads exact, component count unchanged,
 and two unhit cycles remain two unhit cycles.}}
\]

It cannot by itself remove the forced-cycle obstruction.  A successful
clean-C6 repair must touch three distinct components with at least one
already-hit donor component, or must be combined with a separate operation
which creates an omission on one of the two output cycles.
