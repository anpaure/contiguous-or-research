# Audit of the global-maximum PBBS all-depth ladder

Date: 2026-07-25

No computation, finite search, or external input is used.

## 0. Verdict

The global-maximum selection lemma and the all-depth ladder obtained from
that selected boundary are **valid**.  The counterexamples based on an
arbitrary expanded-word boundary do not apply: the proof needs the prefix
inequalities at the selected boundary, and those inequalities are exactly
what the global-maximum cut supplies.

More precisely:

1. Candidate Lemma 6.2 of
   `PBBS_Q3_DEFICIT7_COMPLETE_SUPPORT_20260725.md` is correct, including
   both the forward and backward inequalities and all shared-coordinate
   conventions.
2. Candidate Lemma 6.1 is correct.  Its printed clean-label induction is
   compressed, but the missing induction is supplied below.  In fact its
   stated bounds \(x_j,y_j\le 2j\) suffice; the global-maximum boundary gives
   the stronger bounds \(x_j,y_j\le j\).
3. Consequently the support assertion in Candidate 6.3 is a theorem:
   every rank-\((m-q)\) target is the intersection of a directed
   \(q\)-edge PBBS \(g=f^2\) path, for every \(1\le q\le m\).
4. This proves complete correct-rank support, not a growing-depth residence,
   collision, or literal-word estimate.  It therefore does not by itself
   prove the constant-one conjecture.

The only repairs needed in the source are expository: prove label
distinctness before calling \(K_t\) a rank-\((m-1)\) core, state the two
clean-label induction orders explicitly, and treat the possible shared
endpoint when identifying the strict predecessor/successor.

## 1. Clean-label rule

Let a cyclic binary word have zero excess \(e\ge3\), with forward unmatched
zeros \(F_0,\ldots,F_{e-1}\) in physical forward order.  If a zero \(u\) is
changed to one, its new forward unmatched zeros are the \(e-2\) old marks
immediately preceding \(u\), cyclically.  Equivalently, the first two old
forward marks at or strictly after \(u\) disappear.  If \(u\) itself is an
old mark, it and the next mark disappear.

The reverse analogue says that the new reverse unmatched zeros are the
\(e-2\) old reverse marks immediately succeeding \(u\).  Thus the first two
reverse marks at or strictly before \(u\) disappear.

This is the standard unmatched-zero decomposition: cut at the forward
unmatched zeros, so that the intervening blocks are Dyck words.  Changing a
zero in a Dyck block to one creates two units of surplus, which consume the
first two following unmatched zeros; changing an unmatched zero consumes
that mark and its successor.  Reversing the circle gives the reverse rule.
The rule applies after every flip, so it may be iterated.

## 2. The global-maximum cut

Let an expanded circular word have \(d\) symbols of each kind, with the
forced local order \(C_x,A_x\) at a shared physical coordinate.  Index the
\(C\)-symbols cyclically and put

\[
 z_i=\#\{A\text{-symbols strictly between }C_i\text{ and }C_{i+1}\}.
\]

Then \(\sum_i z_i=d\).  Define the periodic potential

\[
 H(i+1)-H(i)=z_i-1.
\]

Choose \(i\) at a global maximum of \(H\).  Since

\[
 H(i)-H(i-1)=z_{i-1}-1\ge0,
\]

the preceding gap is nonempty.  Let \(A_0\) be its final \(A\)-symbol and
put \(C_0=C_i\).  These are consecutive expanded-word symbols.  They are
different physical coordinates: if a coordinate is shared, its local order
is \(C,A\), never \(A,C\).

For \(1\le j\le d-1\), if \(C_j=C_{i+j}\), then

\[
 x_j=\sum_{h=0}^{j-1}z_{i+h}
     =j+H(i+j)-H(i)\le j.                 \tag{2.1}
\]

For the backward inequality, the current gap and the preceding \(j\) gaps
contain

\[
 \sum_{h=1}^{j+1}z_{i-h}
 =d-\sum_{h=0}^{d-j-2}z_{i+h}\ge j+1.     \tag{2.2}
\]

Starting at the final \(A\)-symbol in the current gap, the \(j\)-th previous
\(A\)-symbol is therefore reached after crossing at most \(j\)
\(C\)-symbols.  This is \(y_j\le j\).  The argument remains exact when an
endpoint is shared: in backward traversal one reaches the local \(A_x\)
before the local \(C_x\), as required by the convention \(C_x,A_x\).

This proves Candidate Lemma 6.2.

## 3. Shared-coordinate audit

Fix \(q\ge1\), put \(d=2q+1\), and use a boundary satisfying

\[
 x_j\le2j,\qquad y_j\le2j\quad(1\le j\le q-1).       \tag{3.1}
\]

The global-maximum cut satisfies the stronger version of (3.1).

Number forward marks from \(A_0\) by

\[
 F_0=A_0,F_1,\ldots,F_{d-1},
 \qquad A_h=F_{d-h}\pmod d.
\]

If \(C_j\) and \(A_h\) are copies of the same physical coordinate, the
local order \(C_j,A_h\) gives the exact identity

\[
 x_j=d-h-1.                                           \tag{3.2}
\]

If \(j+h\le q-1\), then

\[
 x_j=2q-h\ge q+j+1>2j,
\]

contrary to (3.1).  Hence no such collision exists.  In particular:

- every displayed set \(P_t\) has exactly \(q\) physical coordinates;
- every common core below has exactly \(q-1\) extras;
- the deleted coordinate \(C_r\) differs from the inserted coordinate
  \(A_t\), since \(r+t=q-1\).

Moreover, a coordinate \(C_j=A_h\) lies in every \(P_t\) exactly when the
two index intervals

\[
 t\le q-j-1,qquad t\ge h+1

\]

cover every integer \(0\le t\le q\), equivalently when
\(j+h\le q-1\).  Equation (3.2) excludes this.  Therefore

\[
 \bigcap_{t=0}^{q}P_t=\varnothing.                   \tag{3.3}
\]

This verifies both within-state distinctness and empty common extras; they
are separate conclusions and neither is lost at a shared coordinate.

## 4. Every forward arrow

Put

\[
 P_t=\{C_0,\ldots,C_{q-t-1}\}
       \cup\{A_0,\ldots,A_{t-1}\},
 \qquad 0\le t\le q.
\]

Fix \(0\le t<q\) and put \(r=q-t-1\).  The common core of the two proposed
states is

\[
 K_t=S\cup\{C_0,\ldots,C_{r-1}\}
          \cup\{A_0,\ldots,A_{t-1}\}.               \tag{4.1}
\]

It has rank \(m-1\) by Section 3.

Process \(C_0,C_1,\ldots,C_{r-1}\) in this order.  We claim that after the
first \(j\) flips the removed original forward marks are exactly

\[
 F_1,F_2,\ldots,F_{2j}.                            \tag{4.2}
\]

For \(j=0\) this is empty.  Before flipping \(C_j\), the old forward marks
strictly in the arc from \(C_0\) to \(C_j\) are
\(F_1,\ldots,F_{x_j}\), and (3.1) puts all of them in (4.2).  If \(C_j\)
is shared with a forward mark, that mark is \(F_{x_j+1}\); it is either
already removed or is the first current mark at \(C_j\).  Thus the first
two current forward marks at or after \(C_j\) are precisely
\(F_{2j+1},F_{2j+2}\).  The clean-label rule removes them, proving (4.2)
inductively.

After the \(r\) flips, the surviving forward marks are

\[
 F_0,F_{2r+1},F_{2r+2},\ldots,F_{d-1}.               \tag{4.3}
\]

Now flip \(A_0,A_1,\ldots,A_{t-1}\).  These are cyclically consecutive
current forward marks.  At each step the chosen current mark and the next
low-index current mark disappear.  Since

\[
 d-2r=2t+3,
\]

the three final forward marks are

\[
 U_+(K_t)=
 \{F_{d-t-2},F_{d-t-1},F_{d-t}\}
 =\{A_{t+2},A_{t+1},A_t\}.                          \tag{4.4}
\]

Indices are cyclic, so (4.4) also covers \(t=0\).

It remains to locate \(C_r\), not merely to count marks.  All old forward
marks strictly between \(C_0\) and \(C_r\) have index at most
\(x_r\le2r\), hence are absent from (4.4).  If \(C_r\) is shared with the
first surviving mark, the forced local order is \(C_r,A_{t+2}\), so that
mark lies after, not before, \(C_r\).  Therefore the strict predecessor of
\(C_r\) in (4.4) is exactly \(A_t\).  This also holds for \(r=0\), directly
from the original boundary.

## 5. Every reverse arrow

The reverse calculation must be performed in the opposite flip order.
First flip \(A_0,A_1,\ldots,A_{t-1}\).  Using \(y_j\le2j\) and the reverse
clean-label rule, induction gives removal of the tail reverse marks

\[
 C_{d-2t},C_{d-2t+1},\ldots,C_{d-1}.                 \tag{5.1}
\]

Indeed, all reverse marks strictly between \(A_j\) and \(A_0\) have
already disappeared before \(A_j\) is flipped; a shared reverse copy is
either already absent or is the last current mark at that coordinate.
The flip therefore removes the next pair at the high-index end.

Next flip the current reverse marks \(C_0,C_1,\ldots,C_{r-1}\).  Each flip
removes the chosen low-index mark and the current high-index mark.  Since
\(r+t=q-1\), exactly three reverse marks remain:

\[
 U_-(K_t)=\{C_r,C_{r+1},C_{r+2}\}.                  \tag{5.2}
\]

The same arc argument, now using \(y_t\le2t\), shows that the strict
successor of \(A_t\) in (5.2) is \(C_r\).  A possible shared endpoint is
ordered \(C,A\), so it cannot reverse this strict-successor conclusion;
Section 3 already excludes \(C_r=A_t\).

For a rank-\((m-1)\) core \(K\), the exact deficit-three PBBS criterion is

\[
 K\cup\{x\}\longrightarrow K\cup\{y\}
 \iff
 \begin{cases}
 y\text{ is the strict forward predecessor of }x,\\
 x\text{ is the strict reverse successor of }y.
 \end{cases}                                        \tag{5.3}
\]

Equations (4.4), (5.2), and the two location statements give

\[
 g(K_t\cup\{C_r\})=K_t\cup\{A_t\}                 \tag{5.4}
\]

for every \(0\le t<q\).  Thus all \(q\) arrows, including the endpoint
arrows \(t=0,q-1\), are genuine directed \(g=f^2\) transitions.

## 6. Audited theorem and exact scope

Combining Sections 2--5 yields the following unconditional statement.

### Theorem

Let \(n=2m+1\), let \(g=f^2\) be the canonical PBBS step-two
permutation, and let \(1\le q\le m\).  For every

\[
 S\in\binom{[n]}{m-q}
\]

there are consecutive directed PBBS states

\[
 B_0\longrightarrow B_1\longrightarrow\cdots\longrightarrow B_q
\]

such that

\[
 \bigcap_{t=0}^{q}B_t=S.
\]

Consequently every target in rank \(m-q\) has a correct-rank PBBS
occurrence.  Together with the independently proved correct-fibre cap, this
also gives

\[
 1\le\mu_{P,q}^{\mathrm{corr}}(S)
 \le\binom{2q+1}{q}.
\]

The proof is uniform at \(q=1\) (the corridor system is empty) and at
\(q=m\) (\(S=\varnothing\)); no finite exceptional case is used.

The theorem is a support theorem only.  The cap grows exponentially in
\(q\), and the argument supplies no bound on short physical residence,
wrong-rank windows, high collision mass, or the cost of concatenating
growing-depth witnesses.  Those are logically separate from the audited
global-maximum ladder.
