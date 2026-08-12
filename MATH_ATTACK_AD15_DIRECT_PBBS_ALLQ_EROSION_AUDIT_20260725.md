# AD15: direct PBBS all-depth corridor and literal erosion audit

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\operatorname{Cat}_m=\frac{W}{2m+1}.
\tag{0.1}
\]

Let \(f\) be the canonical parenthesis/PBBS permutation of the
rank-\(m\) sets and put \(g=f^2\). On every oriented \(f\)-component
write \(A_i=f^i(A_0)\), with indices understood cyclically.

The audit has four conclusions.

1. The corrected deficit-five \(q=2\) theorem is correct. Its proof needs
   two local clarifications, and its exact floor-one quantitative range is
   \(m\ge8\).

2. The separate deficit-seven \(q=3\) theorem is correct for \(m\ge3\).
   Its shared-coordinate paragraph should be replaced by the exact index
   calculation in Section 3 below.

3. The quarantined global-maximum corridor survives. For every
   \(1\le q\le m\) and every
   \(S\in\binom{[n]}{m-q}\), there is an oriented \(q\)-edge \(g\)-path

   \[
   B_0\longrightarrow B_1\longrightarrow\cdots\longrightarrow B_q
   \]

   with

   \[
   \bigcap_{t=0}^qB_t=S,
   \qquad
   1\le\mu_{P,q}^{\rm corr}(S)
       \le\binom{2q+1}{q}.
   \tag{0.2}
   \]

4. The claimed reduction of coefficient one **solely** to Catalan
   residence packing does not follow. Complete support holds on the uncut
   PBBS cycles. A residence cut can destroy \(q\) selected correct masks
   at each sign and depth \(q\). The strongest unconditional literal
   erosion transfer proved here is

   \[
   \boxed{
   L_H\le
   W+2Hc_2(P_m)+2(H^2+2H)\nu_H(P_m),}
   \tag{0.3}
   \]

   where \(c_2(P_m)\) is the number of complement-projected step-two
   cycles and \(\nu_H(P_m)\) is the maximum packing of short positive
   residence intervals. Therefore

   \[
   \nu_H(P_m)=O(B)
   \]

   yields \(L_H=W+o(W)\) only for \(H=o(\sqrt m)\), not in the required
   Gaussian-above window.

The exact additional theorem is an \(O(H)\)-letter literal seam chart per
active residence cut which preserves all correct-rank crossing masks.
With that theorem, and only then, Catalan residence packing would be the
sole PBBS-specific constant-one gate.

## 1. The unmatched-zero update used in all three audits

Use \(1\) for an up-step and \(0\) for a down-step. If a cyclic binary
word has positive zero deficit, forward matching leaves an odd set of
forward-unmatched zeros. Reverse matching gives the reverse-unmatched
zeros.

### Lemma 1.1 (one-flip deletion rule)

Let the current forward-unmatched zeros be listed in physical cyclic order.
Change one zero \(u\) to a one.

- If \(u\) is not currently forward-unmatched, the first two currently
  unmatched zeros strictly after \(u\) cease to be unmatched.
- If \(u\) is currently forward-unmatched, then \(u\) and the next
  currently unmatched zero cease to be unmatched.

The reverse rule is obtained by reversing the physical circle.

#### Proof

Cut the word at its forward-unmatched zeros:

\[
 0_{a_0}D_0\,0_{a_1}D_1\cdots0_{a_{d-1}}D_{d-1},
\tag{1.1}
\]

where every \(D_i\) is Dyck. If \(u=a_i\), the new up-step at \(u\)
matches \(a_{i+1}\), so precisely \(a_i,a_{i+1}\) disappear from the
unmatched list. If \(u\) is inside \(D_i\), changing its down-step to an
up-step creates two units of forward excess. Those two units consume the
next two unmatched zeros, \(a_{i+1},a_{i+2}\). No earlier matching is
altered outside the intervening Dyck suffix. This proves the forward rule;
physical reversal proves the reverse rule. \(\square\)

For a deficit-three rank-\((m-1)\) core \(K\), write \(P=U_+(K)\) and
\(Q=U_-(K)\). For distinct \(x,y\in[n]\setminus K\), the standard strict
predecessor/successor form is

\[
 g(K\cup\{x\})=K\cup\{y\}
 \quad\Longleftrightarrow\quad
 y=\operatorname{pv}_{P}(x),\quad
 x=\operatorname{nx}_{Q}(y).
\tag{1.2}
\]

Every later arrow audit uses (1.2), not an abstract adjacency claim.

## 2. Independent audit of the corrected \(q=2\) theorem

Fix \(m\ge2\) and

\[
 S\in\binom{[n]}{m-2}.
\]

Define

\[
 \mu_{P,2}(S)
 =\#\left\{i:
 \bigcap_{h=0}^{2}A_{i+2h}=S
 \right\},
\tag{2.0}
\]

where \(i\) ranges over oriented starting states of the canonical factor.

Its word has five forward-unmatched and five reverse-unmatched zeros. Form
the expanded circular word with symbols \(A_x\) at forward marks and
\(C_x\) at reverse marks, using the local order

\[
 C_x,A_x
\tag{2.1}
\]

at a shared coordinate.

For a zero \(u\notin S\), the deficit-three core \(C_u=S\cup\{u\}\)
has forward set equal to the three old \(A\)-marks immediately preceding
\(u\), and reverse set equal to the three old \(C\)-marks immediately
following \(u\). This is exactly Lemma 1.1.

Write the expanded word in runs

\[
 A^{\alpha_0}C^{\gamma_0}\cdots
 A^{\alpha_{t-1}}C^{\gamma_{t-1}},
 \qquad
 \sum_i\alpha_i=\sum_i\gamma_i=5.
\tag{2.2}
\]

At an \(A_c,C_b\) boundary let \(x\) be the number of \(A\)-marks
encountered strictly after \(C_b\) and before the next \(C\)-symbol.
Let \(y\) be the number of \(C\)-marks encountered when moving backward
strictly after \(A_c\) and before the preceding \(A\)-symbol. The
five-by-five run argument does prove that some boundary has

\[
 x\le2,\qquad y\le2.
\tag{2.3}
\]

If \(a\) is the next \(C\)-mark after \(C_b\), and \(d\) is the
previous \(A\)-mark before \(A_c\), then (2.3) and (1.2) give

\[
 S\cup\{a,b\}\longrightarrow
 S\cup\{b,c\}\longrightarrow
 S\cup\{c,d\}.
\tag{2.4}
\]

There are two proof details which must be stated explicitly.

First, in the deficit-five fibre an outgoing edge from
\(S\cup\{b,c\}\) could a priori retain \(b\) rather than \(c\). That
alternative would leave \(S\cup\{b\}\) in all three states, giving a
three-state intersection of rank at least \(m-1\). The pointwise
no-gap-three theorem says that every such intersection has rank exactly
\(m-2\), so the alternative is impossible. This is the missing
orientation justification in the exact multiplicity formula.

Second, \(a\ne b\), \(b\ne c\), and \(c\ne d\) are immediate from the
strict next/previous definitions and the forced shared order. The two
nonlocal equalities are also excluded. If \(a=c\), then \(C_c\)
would be both the predecessor and successor of \(C_b\) in the five-element
cyclic \(C\)-order: it lies immediately before \(A_c,C_b\), yet by
definition it would also be the next \(C\)-mark after \(C_b\). This is
impossible with five distinct \(C\)-marks. The reverse argument excludes
\(d=b\) in the five-element \(A\)-order. Hence
\(\{a,b\}\cap\{b,c\}\cap\{c,d\}=\varnothing\), and the common
intersection in (2.4) is exactly \(S\).

We obtain the audited theorem

\[
 \boxed{
 1\le\mu_{P,2}(S)\le10.}
\tag{2.5}
\]

For the cap, \(a\in U_-(C_b)\subset U_-(S)\) and
\(b\in U_-(C_c)\subset U_-(S)\). Thus the two deleted initial extras are
distinct members of \(U_-(S)\); their two-set determines the initial state
and hence the oriented deterministic path.

The exact floor-one range is

\[
 \frac{W}{\binom{2m+1}{m-2}}
 =\frac{(m+2)(m+3)}{m(m-1)}<2
 \quad\Longleftrightarrow\quad m\ge8.
\tag{2.6}
\]

For \(m\ge8\), with

\[
 R_2=W-\binom{2m+1}{m-2},
\]

define

\[
\begin{aligned}
 O_2(P_m)
 &=\min_{\substack{J\subseteq\binom{[n]}{m-2}\\|J|=R_2}}
   \sum_S\bigl(\mu_{P,2}(S)-1-\mathbf1_J(S)\bigr)_+,\\
 Q_2(P_m)
 &=\sum_S\binom{\mu_{P,2}(S)-1}{2}.
\end{aligned}
\tag{2.6a}
\]

Then the standard balanced overload and ordinary corrected collision energy
satisfy

\[
 O_2(P_m)\le R_2<12B,
 \qquad
 Q_2(P_m)\le4R_2<48B.
\tag{2.7}
\]

The source report's duplicate equation tags are editorial only.

The shorter proof printed in Section 15 of
PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md chooses an arbitrary
\(A\to C\) boundary and is not valid. The theorem statement is rescued by
the corrected five-by-five selection above; downstream uses must import
this corrected theorem rather than that stale proof.

## 3. Independent audit of the separate \(q=3\) theorem

Assume \(m\ge3\) and fix

\[
 S\in\binom{[n]}{m-3}.
\]

There are seven marks of each type. At a chosen boundary \(A_c,C_b\),
number the forward \(A\)-marks

\[
 F_0=c,F_1,\ldots,F_6,
\]

and the forward \(C\)-marks

\[
 G_0=b,G_1=a_1,G_2=a_2,\ldots,G_6.
\]

Thus \(F_6=d_1\) and \(F_5=d_2\). The four good-boundary inequalities
are

\[
 k\le2,\quad \ell\le4,\quad k'\le2,\quad \ell'\le4.
\tag{3.1}
\]

For the shared-coordinate audit below, put

\[
 C_j:=G_j,\qquad
 A_0:=F_0,\quad A_1:=F_6,\quad A_2:=F_5,
\tag{3.1a}
\]

and let \(x_j\) count the \(A\)-marks strictly between \(C_0,C_j\).
Then \(x_1=k\) and \(x_2=\ell\).

Under (3.1), applying Lemma 1.1 gives the following exact table for the
three common rank-\((m-1)\) cores:

\[
\begin{array}{c|c|c}
K_0=S\cup\{G_0,G_1\}
 &U_+(K_0)=\{F_0,F_5,F_6\}
 &U_-(K_0)=\{G_2,G_3,G_4\}\\
K_1=S\cup\{G_0,F_0\}
 &U_+(K_1)=\{F_4,F_5,F_6\}
 &U_-(K_1)=\{G_1,G_2,G_3\}\\
K_2=S\cup\{F_0,F_6\}
 &U_+(K_2)=\{F_3,F_4,F_5\}
 &U_-(K_2)=\{G_0,G_1,G_2\}.
\end{array}
\tag{3.2}
\]

The inequalities in (3.1) give precisely the strict
predecessor/successor pairs in (1.2), hence

\[
\begin{aligned}
S\cup\{a_2,a_1,b\}&\longrightarrow S\cup\{a_1,b,c\},\\
S\cup\{a_1,b,c\}&\longrightarrow S\cup\{b,c,d_1\},\\
S\cup\{b,c,d_1\}&\longrightarrow S\cup\{c,d_1,d_2\}.
\end{aligned}
\tag{3.3}
\]

The seven-by-seven run table and each of its cases
\(t=1,2,3,\ge4\) are correct, so a good boundary always exists.

The shared-coordinate check should be written as follows. For selected
indices \(0\le j,h\le2\), if \(C_j=A_h\), then the forced local order
\(C_x,A_x\) gives

\[
 x_j=6-h.
\tag{3.4}
\]

The bounds \(x_1\le2,x_2\le4\) exclude every harmful selected
coincidence. The only permitted selected equality is

\[
 C_2=A_2.
\]

It occurs only in the first and last triples of (3.3), and in neither
middle triple. It therefore neither collapses a state nor enters the
four-way intersection. Consequently

\[
\begin{aligned}
 \mu_{P,3}^{\rm corr}(S)
 &=\#\left\{i:
 \bigcap_{h=0}^{3}A_{i+2h}=S\right\},\\
 b_3
 &=\#\left\{i:
 \left|\bigcap_{h=0}^{3}A_{i+2h}\right|>m-3\right\}.
\end{aligned}
\tag{3.4a}
\]

The first count is over oriented starting states. We have

\[
 \boxed{
 1\le\mu_{P,3}^{\rm corr}(S)\le35.}
\tag{3.5}
\]

The cap is obtained exactly as at depth two: the three distinct initial
extras which are later deleted lie in the seven-element set \(U_-(S)\),
and their three-subset determines the oriented path.

The global-maximum construction below specializes at \(q=3\) to the same
four formal triples in (3.3), but with the stronger inequalities

\[
 x_1\le1,\quad x_2\le2,\quad y_1\le1,\quad y_2\le2.
\]

It therefore excludes even the harmless equality \(C_2=A_2\). The
separate seven-by-seven theorem permits that equality but does not require
it.

Depth three has complete correct support, not pointwise correct rank.
Gap-five windows of excess one remain. Complete support nevertheless gives

\[
 b_3\le W-\binom{2m+1}{m-3}<24B
\tag{3.6}
\]

and

\[
 \sum_S\binom{\mu_{P,3}^{\rm corr}(S)-1}{2}<396B.
\tag{3.7}
\]

These are fixed-depth statements only.

## 4. The global-maximum two-sided corridor

The following statement was quarantined in the source reports. It passes.

### Theorem 4.1 (global-maximum corridor)

Let a circular word contain \(d\) symbols \(A\) and \(d\) symbols
\(C\), with shared physical coordinates expanded in the order
\(C_x,A_x\). There is an \(A_0,C_0\) boundary such that, after numbering
the \(C\)'s forward and the \(A\)'s backward from that boundary,

\[
 x_j\le j,\qquad y_j\le j
 \qquad(1\le j\le d-1),
\tag{4.1}
\]

where \(x_j\) counts \(A\)-symbols strictly between \(C_0,C_j\), and
\(y_j\) is the reverse-dual count. Put \(x_0=y_0=0\).

#### Proof

Index the \(C\)-symbols cyclically and let \(z_i\) be the number of
\(A\)-symbols strictly between \(C_i,C_{i+1}\). Then

\[
 \sum_{i\in\mathbb Z_d}z_i=d.
\]

Define a periodic potential by

\[
 h(i+1)-h(i)=z_i-1.
\tag{4.2}
\]

Choose \(i\) at a global maximum. Since

\[
 h(i)-h(i-1)=z_{i-1}-1\ge0,
\]

the gap before \(C_i\) contains an \(A\)-symbol; its last \(A\)-symbol
is \(A_0\). For \(j\ge1\), maximality gives

\[
 x_j-j
 =\sum_{s=0}^{j-1}(z_{i+s}-1)
 =h(i+j)-h(i)\le0.
\tag{4.3}
\]

For the backward inequality, the \(L\) gaps ending at \(C_i\) contain

\[
 \sum_{s=1}^{L}z_{i-s}
 =d-\sum_{s=0}^{d-L-1}z_{i+s}\ge L.
\tag{4.4}
\]

With \(L=j+1\), the current gap and the preceding \(j\) gaps contain at
least \(j+1\) \(A\)-symbols. Starting at the final \(A\)-symbol in the
current gap, the \(j\)-th previous \(A\)-symbol is reached after crossing
at most \(j\) \(C\)-symbols. Hence \(y_j\le j\). \(\square\)

For \(j=d-1\), equation (4.4) uses \(L=d\); its complementary forward
sum is the empty sum.

## 5. Complete correct PBBS support at every depth

### Theorem 5.1 (all-depth PBBS corridor theorem)

For every \(m\ge1\), every \(1\le q\le m\), and every

\[
 S\in\binom{[2m+1]}{m-q},
\]

there is a canonically oriented \(q\)-edge \(g=f^2\) path

\[
 B_0\longrightarrow B_1\longrightarrow\cdots\longrightarrow B_q
\tag{5.1}
\]

such that

\[
 \boxed{\bigcap_{t=0}^{q}B_t=S.}
\tag{5.2}
\]

Moreover

\[
 \boxed{
 1\le\mu_{P,q}^{\rm corr}(S)
 \le\binom{2q+1}{q}.}
\tag{5.3}
\]

#### Proof

The word of \(S\) has

\[
 d=2q+1
\]

forward-unmatched and \(d\) reverse-unmatched zeros. Apply Theorem 4.1 to
its expanded mark word. Number the \(C\)'s forward and the \(A\)'s
backward from the chosen boundary. Define

\[
 P_t=
 \{C_0,\ldots,C_{q-t-1}\}
 \cup
 \{A_0,\ldots,A_{t-1}\},
 \qquad0\le t\le q,
\tag{5.4}
\]

with empty ranges omitted, and put \(B_t=S\cup P_t\).

Fix \(0\le t<q\), put \(r=q-t-1\), and define the proposed common core

\[
 K_t=S\cup\{C_0,\ldots,C_{r-1}\}
          \cup\{A_0,\ldots,A_{t-1}\}.
\tag{5.5}
\]

List the original forward marks as

\[
 F_0=A_0,F_1,\ldots,F_{d-1},
 \qquad
 A_0=F_0,\quad A_j=F_{d-j}\quad(1\le j\le d-1).
\tag{5.6}
\]

Before processing any flips, audit physical label collisions. If
\(C_j=A_h\), the local order \(C_x,A_x\) gives

\[
 x_j=d-h-1=2q-h.
\tag{5.6a}
\]

Together with \(x_j\le j\), this implies

\[
 j+h\ge2q.
\tag{5.6b}
\]

In particular, no selected \(C_j\), \(j<r\), equals a selected \(A_h\),
\(h<t\). Also the forward indices of the selected \(A\)-marks lie outside
\(F_1,\ldots,F_{2r}\): \(A_0=F_0\), while
\(A_h=F_{d-h}\) for \(1\le h<t\) and \(d-h>2r\). Thus the selected
\(A\)-marks really do survive the preceding \(C\)-flips.

Process the flips \(C_0,\ldots,C_{r-1}\). Before \(C_j\) is flipped,
all original forward marks strictly between \(C_0\) and \(C_j\) lie
among \(F_1,\ldots,F_j\), because \(x_j\le j\). By induction and Lemma
1.1, the first \(j\) flips have removed

\[
 F_1,\ldots,F_{2j}.
\]

Thus the \(C_j\)-flip removes the next two surviving marks
\(F_{2j+1},F_{2j+2}\). After all \(r\) flips, the removed forward marks
are \(F_1,\ldots,F_{2r}\).

The selected marks \(A_0,\ldots,A_{t-1}\) still survive. Processing them
in that order removes the selected cyclic tail

\[
 F_0,F_{d-1},\ldots,F_{d-t+1}
\]

and the next surviving marks

\[
 F_{2r+1},\ldots,F_{2r+t}.
\]

Since \(d=2q+1\) and \(r=q-t-1\), precisely three forward marks remain:

\[
 U_+(K_t)=\{A_t,A_{t+1},A_{t+2}\}.
\tag{5.7}
\]

The inequality \(x_r\le r\le2r\) places \(C_r\) after the removed
forward block and before the first surviving forward mark. Hence its
strict predecessor in (5.7) is \(A_t\).

Apply the identical calculation to the physically reversed word, with
the roles of \(A,C\) interchanged. It gives

\[
 U_-(K_t)=\{C_r,C_{r+1},C_{r+2}\},
\tag{5.8}
\]

and the strict successor of \(A_t\) in this triple is \(C_r\). Equation
(1.2) therefore yields

\[
 g(K_t\cup\{C_r\})=K_t\cup\{A_t\},
\tag{5.9}
\]

which is the \(t\)-th arrow in (5.1).

A duplicated coordinate inside one \(P_t\) would require

\[
 j\le q-t-1,\qquad h\le t-1,
\]

and hence \(j+h\le q-2\), contradicting (5.6b). A shared coordinate
could belong to every \(P_t\) only if \(j+h\le q-1\), again impossible.
Thus every \(|P_t|=q\) and

\[
 \bigcap_{t=0}^qP_t=\varnothing.
\]

This proves (5.2).

For the cap, every one of the \(q\) initial extras above \(S\) is present
in \(B_0\) but absent from the full intersection, so each must be deleted
at least once. There are exactly \(q\) deletion events along a \(q\)-edge
path. Hence those events delete the \(q\) distinct initial extras and no
inserted label. Parenthesis monotonicity puts the deleted labels in the
\((2q+1)\)-set \(U_-(S)\). Their \(q\)-subset determines the initial
state and hence the oriented deterministic path, proving (5.3).
\(\square\)

Theorem 5.1 promotes the quarantined all-depth support statement. It does
not say that every PBBS window has correct rank, nor does its exponential
cap give a Gaussian collision estimate.

## 6. Consecutive projected masks and the covered band

Let \((A_i)\) be indexed in the original \(f\)-order and fix one
\(g=f^2\) orbit. An even-length \(f\)-component gives two parity orbits,
whereas an odd-length component gives one \(g\)-orbit traversed by the
step-two indexing. Write

\[
 X_j=[n]\setminus A_{\epsilon+2j}.
\tag{6.1}
\]

These are rank-\((m+1)\) owners on a directed Johnson cycle. For every
\(q\ge0\),

\[
 \bigcup_{h=0}^{q}X_{j+h}
 =[n]\setminus\bigcap_{h=0}^{q}A_{\epsilon+2j+2h},
\tag{6.2}
\]

and

\[
 \bigcap_{h=0}^{q+1}X_{j+h}
 =\bigcap_{h=0}^{q}A_{\epsilon+2j+1+2h}.
\tag{6.3}
\]

Equation (6.3) follows by intersecting the adjacent identities

\[
 X_j\cap X_{j+1}=A_{\epsilon+2j+1}.
\]

Theorem 5.1 applied over all \(g\)-orbits therefore shows that the correct
consecutive projected masks cover every set in the ranks

\[
 \boxed{m-H+1,m-H+2,\ldots,m+H+1}
\tag{6.4}
\]

when projected depths through \(H\) are retained. Explicitly, upper rank
\(m+1+q\) comes from a union of \(q+1\) projected owners for
\(0\le q\le H\), while lower rank \(m-q\) comes from an intersection of
\(q+2\) projected owners for \(0\le q\le H-1\). Lower rank \(m-H\)
would require \(H+2\) projected owners and is intentionally outside this
radius-\(H\) erosion.

We also import the standard PBBS component-length ledger. Every
\(f\)-component has length \(\ell(2m+1)\). If \(\ell\) is odd, its
\(g\)-orbit has that length; if \(\ell\) is even, it splits into two
orbits of length \(\ell(2m+1)/2\). Consequently every projected
\(g\)-cycle has length at least \(2m+1\). In particular, for \(H\le m\)
all residence intervals considered below are proper circular intervals,
and a cut belongs to exactly \(q\) cyclic windows of \(q+1\) owners.

## 7. Exact literal erosion on a cut path

### Lemma 7.1 (path erosion/dilation identities)

Let

\[
 X_0,X_1,\ldots,X_{\ell-1}\in\binom{[n]}{m+1}
\]

be a directed Johnson path. Assume every internally bounded positive
coordinate run has at least \(H+1\) vertices, where \(1\le H\le m\).
Extend the path constantly by

\[
 \widetilde X_i=X_0\ (i<0),\qquad
 \widetilde X_i=X_{\ell-1}\ (i\ge\ell).
\tag{7.1}
\]

For \(-H\le i\le\ell-1\), put

\[
 D_i=\bigcap_{h=0}^{H}\widetilde X_{i+h}.
\tag{7.2}
\]

Then every \(D_i\) is nonempty, and the word

\[
 D_{-H},D_{-H+1},\ldots,D_{\ell-1}
\tag{7.3}
\]

has length exactly \(\ell+H\). For every
\(0\le a\le b\le\ell-1\) with \(b-a\le H\), it contains literal
intervals satisfying

\[
 \boxed{
 \bigcup_{i=b-H}^{a}D_i
 =\bigcap_{t=a}^{b}X_t,}
\tag{7.4}
\]

and

\[
 \boxed{
 \bigcup_{i=a-H}^{b}D_i
 =\bigcup_{t=a}^{b}X_t.}
\tag{7.5}
\]

#### Proof

Fix a coordinate \(x\). Its one-set in the constant extension is a union
of intervals, each either unbounded or of length at least \(H+1\). Also

\[
 x\in D_i
 \quad\Longleftrightarrow\quad
 [i,i+H]\text{ lies inside one such one-interval}.
\tag{7.6}
\]

An interval of ones contains \([a,b]\) if and only if it contains an
\((H+1)\)-window starting somewhere in \([b-H,a]\). This proves (7.4).
It meets \([a,b]\) if and only if it contains an \((H+1)\)-window starting
somewhere in \([a-H,b]\). This proves (7.5).

For each \(i\), over the \(H\) Johnson transitions starting at the first
owner \(\widetilde X_i\) of that erosion window, at most \(H\) of its
coordinates can be removed. Hence

\[
 |D_i|\ge m+1-H\ge1,
\]

including at the constant endpoints. Thus all letters are nonzero.
\(\square\)

There is a cyclic version. If a projected cycle has no positive residence
run of length at most \(H\), define the \(D_i\)'s cyclically and emit one
cycle followed by its first \(2H\) letters. The same coordinatewise proof
shows that every cyclic intersection/union mask of the depths in (6.4) is
literal. The exact length is \(\ell+2H\).

## 8. Residence cuts and the strongest unconditional transfer

For a projected cycle \(C\), let \(\mathcal I_H(C)\) be its circular
positive residence intervals of length at most \(H\), including their
insertion and removal transition edges. Let \(\nu_H(C)\) be the maximum
number of pairwise edge-disjoint members and let \(\tau_H(C)\) be the
minimum edge transversal. The circular interval theorem gives

\[
 \nu_H(C)\le\tau_H(C)\le\nu_H(C)+1.
\tag{8.1}
\]

Call \(C\) active when \(\mathcal I_H(C)\ne\varnothing\). On an active
cycle, cutting a transversal of size

\[
 J_C=\tau_H(C)\le\nu_H(C)+1\le2\nu_H(C)
\tag{8.2}
\]

produces \(J_C\) paths satisfying Lemma 7.1. Indeed, an internally bounded
positive run of length at most \(H\) in a fragment would give an unhit
member of \(\mathcal I_H(C)\).

Complete support was proved on the uncut cycles. Before cutting, select one
correct occurrence for every target in (6.4). A cut edge lies in at most
\(q\) cyclic intervals of \(q+1\) consecutive projected owners. Hence,
over all depths, one cut can destroy at most

\[
 \sum_{q=1}^{H}q+\sum_{q=1}^{H}q
 =H(H+1)
\tag{8.3}
\]

selected correct masks: the first sum is for the lower intersections and
the second for the upper unions. Append every genuinely lost selected
target as one literal set-letter. This is integral, preserves nonzero
letters, and requires no factor mixing.

### Theorem 8.1 (exact unconditional PBBS erosion/cut transfer)

Let

\[
 c_2(P_m)=\#\{\text{complement-projected step-two cycles}\},
 \qquad
 \nu_H(P_m)=\sum_C\nu_H(C).
\]

For every \(1\le H\le m\), there is a nonzero literal contiguous-OR word
covering all ranks in (6.4), of length at most

\[
 \boxed{
 L_H\le
 W+2Hc_2(P_m)+2(H^2+2H)\nu_H(P_m).}
\tag{8.4}
\]

#### Proof

On every inactive cycle of length \(\ell\), use the cyclic erosion word of
length \(\ell+2H\). On every active cycle, the path words from Lemma 7.1
have total length

\[
 \ell+HJ_C.
\]

Literal completion of the selected masks destroyed by its cuts costs at
most

\[
 H(H+1)J_C.
\]

Thus the active-cycle overhead is at most

\[
 (H^2+2H)J_C
 \le2(H^2+2H)\nu_H(C).
\]

Sum over cycles. Their unextended lengths total exactly \(W\), and the
number of inactive cycles is at most \(c_2(P_m)\). This proves (8.4).
All words and repair letters are concatenated only after they have been
constructed literally, so no fractional or cross-factor step occurs.
\(\square\)

The standard PBBS cycle ledger gives

\[
 c_2(P_m)\le B.
\tag{8.5}
\]

Consequently a Catalan packing estimate

\[
 \nu_H(P_m)\le K B
\tag{8.6}
\]

implies only

\[
 \frac{L_H-W}{W}
 \le
 \frac{2H+2K(H^2+2H)}{2m+1}.
\tag{8.7}
\]

This is \(o(1)\) when \(H=o(\sqrt m)\). At
\(H=A\sqrt m\) it has a nonvanishing \(O_K(A^2)\) term, and for
\(H=\sqrt m\,\omega(m)\) it diverges. Thus (8.6) alone does not prove
coefficient one.

## 9. Why endpoint recanonicalization does not supply the missing seam

The failure in Section 8 is not repaired by simply declaring arbitrary
dummy departures at every cut.

### Proposition 9.1 (short-run terminal incompatibility)

Let a coordinate \(x\) be inserted at transition \(p\), remain present
for \(\ell=q-p\) owners, and be removed at transition \(q\). Cut at the
removal edge and suppose

\[
 \ell\le H-1.
\]

Any terminal natural-departure radius-\(H\) state which preserves the lost
depth-one facet across that cut must use \(x\) as its first terminal dummy
departure. Such a state cannot be propagated backwards through the
insertion transition.

#### Proof

The lost facet is \(X_q\setminus\{x\}\), so preserving it as the first
terminal lower flag forces the first dummy departure to be \(x\). At the
owner \(X_p\) immediately before insertion, the radius-\(H\) future
departure queue contains every departure through transition
\(p+H-1\). Since

\[
 q=p+\ell\le p+H-1,
\]

that queue contains \(x\). But \(x\notin X_p\), contradicting the defining
lower-queue condition that every future departure coordinate belong to the
current owner. \(\square\)

PBBS gap-five returns have projected positive residence three, so this
incompatibility occurs for every \(H\ge4\). Proposition 9.1 rules out only
naive independent endpoint recanonicalization. It is not a no-go theorem
for a genuinely new literal seam chart.

## 10. The exact missing seam theorem and the conditional coefficient-one implication

The needed statement is now isolated without hidden synchronization.

> **PBBS crossing-mask seam theorem \(\mathrm{CMS}(H)\).** There is an
> absolute constant \(C\) such that, for every active projected PBBS cycle
> and every nonempty transversal \(D_C\) of its residence intervals of
> length at most \(H\),
> the cycle can be replaced by one nonzero literal word of length
> \[
> \ell+CHJ_C,\qquad J_C:=|D_C|\ge1,
> \]
> which exposes every correct-rank consecutive lower intersection and
> upper union of depth at most \(H\), including all masks crossing the
> selected cuts. Inactive cycles retain their cyclic erosion word of
> length \(\ell+2H\).

Nearby cuts must be handled jointly; an independent endpoint flag choice
is not enough by Proposition 9.1.

### Theorem 10.1 (conditional reduction to Catalan residence packing)

Assume \(\mathrm{CMS}(H)\) and

\[
 \nu_H(P_m)=O(B)
\tag{10.1}
\]

uniformly for some \(H=H(m)\) with

\[
 H=o(m),\qquad
 \frac{m}{H}\exp\!\left(-\frac{H^2}{m+H}\right)\longrightarrow0.
\tag{10.2}
\]

Then there is a nonzero universal contiguous-OR word of length

\[
 (1+o(1))W.
\tag{10.3}
\]

#### Proof

The circular packing theorem gives

\[
 \sum_{C\ {\rm active}}J_C
 \le2\nu_H(P_m)=O(B),
\]

while the number of inactive cycles is at most \(c_2(P_m)\le B\).

The seam theorem and Theorem 5.1 therefore give one literal word covering
the central band (6.4), of length

\[
 W+O(HB)=W+o(W)
\]

because \(HB/W=H/(2m+1)=o(1)\).

For the outer ranks, use the elementary adjacent-binomial ratio. Uniformly
for \(H=o(m)\),

\[
 \frac{\binom{2m+1}{m-H}}{W}
 \le \exp\!\left(-\frac{H^2}{m+H}\right),
\tag{10.4}
\]

and the subsequent tail decreases geometrically with ratio at most

\[
 \frac{m-H}{m+H+2}.
\]

Hence the total number of nonempty sets outside (6.4) is

\[
 O\!\left(
 W\frac{m}{H}
 e^{-H^2/(m+H)}
 \right)=o(W)
\tag{10.5}
\]

under (10.2), after choosing for example
\(H=\lceil\sqrt m\log m\rceil\). Append those outer targets literally.
This proves (10.3). \(\square\)

The argument above proves (10.3) in odd dimension \(2m+1\). It gives all
dimensions by the standard one-coordinate lift. For even dimension
\(2m\), apply the odd-dimensional result on \([2m-1]\), concatenate its
word \(w=(E_i)\) with

\[
 w^\star=(E_i\cup\{\star\}),
\]

and append the one-letter word \(\{\star\}\). The first copy covers every
nonempty target avoiding \(\star\), the second covers
\(T\cup\{\star\}\) for every nonempty \(T\subseteq[2m-1]\), and the last
letter covers the singleton. Since

\[
 2\binom{2m-1}{m-1}=\binom{2m}{m},
\]

the resulting length is \((1+o(1))\binom{2m}{m}\).

Thus Theorem 5.1 closes the all-depth support gate, but the direct
constant-one PBBS route still has two logically separate inputs:

1. Catalan residence packing;
2. the literal crossing-mask seam theorem.

It is incorrect to list only the first until \(\mathrm{CMS}(H)\) is proved.

## 11. Exact proved and unproved boundary

### Proved

1. Corrected complete \(q=2\) support and cap ten.
2. Separate complete correct \(q=3\) support and cap thirty-five.
3. The global-maximum two-sided corridor.
4. Complete correct PBBS support at every depth, with cap
   \(\binom{2q+1}{q}\).
5. Exact projected lower/upper band identities.
6. Literal path erosion with exact length \(\ell+H\).
7. The unconditional transfer (8.4), including every seam and literal
   repair.
8. The short-run obstruction to naive endpoint recanonicalization.
9. Conditional coefficient one from \(\mathrm{CMS}(H)\) plus Catalan
   residence packing.

### Unproved

1. Catalan residence packing in the required growing window.
2. The \(O(H)\)-per-cut crossing-mask seam theorem \(\mathrm{CMS}(H)\).
3. Constant one.
