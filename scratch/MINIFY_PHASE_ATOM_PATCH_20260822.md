# Phase-atom repair for minified Section 4.4

## Patch target

In `scratch/MASTER_HANDOFF_MINIFIED_DRAFT_20260822.md`, replace lines
714--718 (from “A phase atom” through “is injective”) by the following.

## Proposed replacement

Write \(b=2h+1\). Split \(\Omega=A\mathbin{\dot\cup}B\), with both
shores of size \(b\), and fix directed cyclic orders
\(\alpha=(\alpha_i)_{i\in\mathbb Z_b}\) on \(A\) and
\(\beta=(\beta_j)_{j\in\mathbb Z_b}\) on \(B\). For roots
\(i_0,j_0\in\mathbb Z_b\), define a bi-infinite singleton word by
\[
 w_{qb+2u}=\beta_{j_0+q(h+1)+u}\quad(0\le u\le h),
 \qquad
 w_{qb+2u+1}=\alpha_{i_0+qh+u}\quad(0\le u<h),            \tag{4.11a}
\]
where \(q\in\mathbb Z\) and all subscripts are modulo \(b\). Thus every
type period is \(B,A,B,A,\ldots,B,A,B\). Roots differing by a multiple of
\((h,h+1)\) give a rotation by a multiple of \(b\); equivalently the phase
is their coset in
\(\mathbb Z_b^2/\langle(h,h+1)\rangle\). The word is \(b^2\)-periodic by
(4.11a). Its least period is \(b^2\): the shore-type word has least period
\(b\) (there is one cyclic \(BB\) boundary), while a shift by \(kb\)
advances the \(A\)-stream by \(kh\); since \(\gcd(h,b)=1\), return forces
\(b\mid k\).

For a cyclic start \(t\), put
\[
 C_t=\{w_t,w_{t+1},\ldots,w_{t+b-1}\}.
\]
It consists of \(h\) consecutive entries of \(\alpha\) and \(h+1\)
consecutive entries of \(\beta\). Let \(p_t=(x_t,y_t)\in\mathbb Z_b^2\)
be the two interval starts. Sliding the window one place advances exactly
one of \(x_t,y_t\), because the leaving and entering letters have the same
shore. Hence
\[
 p_{t+b}=p_t+(h,h+1),\qquad x_{t+1}+y_{t+1}=x_t+y_t+1\pmod b.             \tag{4.11b}
\]
For a fixed residue \(r\in\{0,\ldots,b-1\}\), the pairs
\(p_{r+qb}=p_r+q(h,h+1)=p_r+q(h,-h)\), \(q\in\mathbb Z_b\), run once
through the diagonal \(x+y=x_r+y_r\), since \(h\) is invertible modulo
\(b\). As \(r\) varies, (4.11b) gives all \(b\) diagonals. Thus the
\(b^2\) starts give every pair in \(\mathbb Z_b^2\) exactly once. Proper
directed cyclic intervals have distinct starts, and the shores are
disjoint, so the \(b^2\) sets \(C_t\) are pairwise distinct.

Finally, successive \(A\)-events are separated by at least two positions.
Successive \(B\)-events have gap two except for one gap one in each block
of \(h+1\) such gaps. A fixed coordinate reappears only after \(b\) events
of its shore. Its return gap is therefore at least \(2b\) on \(A\); on
\(B\), any \(b=2h+1\) consecutive event-gaps contain at most
\(\lceil b/(h+1)\rceil=2\) short gaps, so the return gap is at least
\(2b-2\). Since the shores are disjoint, no block of at most \(2b-2\)
consecutive letters contains a repeated coordinate. This proves the two
phase-atom properties used below.

## Dependency audit

- The proof needs only odd \(b\ge3\), the labelled disjoint split
  \(\Omega=A\mathbin{\dot\cup}B\), and cyclic-order indices modulo \(b\).
  These data were implicit in minified lines 714--717 and are explicit in
  the replacement.
- “Cyclic window” must mean the set of letters at consecutive starts modulo
  \(b^2\), and “injective” must mean that those positions carry pairwise
  distinct ground coordinates. The replacement defines \(C_t\) locally.
  The draft's later general definitions of singleton words and clean
  windows are at lines 5703--5718; no forward reference is now needed for
  this lemma.
- The quotient phase is not needed for distinctness or the recurrence-gap
  bound. It is needed only if the omitted old-master enumeration and
  symmetric-family claims for *phase-refined labelled atoms* are restored.
  Those claims also require coordinate-relabeling invariance and the atom
  counts, neither of which Section 4.4 uses.
- The later linearization uses the lemma with \(g=b+H\le2b-2\). Thus its
  cleanliness depends on the already displayed inequality \(H\le b-2\),
  but the atom lemma itself does not depend on the probabilistic choice of
  \(H\).

## Recovered source

- Full source heading: `MASTER_HANDOFF.md`, `### I.2 Phase-refined product
  atoms`, line 14508.
- Construction and phase quotient: lines 14510--14525, especially (I.3).
- Period, distinct-window argument, and recurrence-gap conclusion: lines
  14527--14539, especially (I.4).
- Minified insertion site: `scratch/MASTER_HANDOFF_MINIFIED_DRAFT_20260822.md`,
  `### 4.4 A direct literal fragment compiler [C]`, lines 710--718.

The displayed formula (4.11a) merely expands the old source's “repeatedly
emit” instruction; (4.11b) expands its diagonal-orbit sentence. No later
atom-counting or FIFO statement is imported.
