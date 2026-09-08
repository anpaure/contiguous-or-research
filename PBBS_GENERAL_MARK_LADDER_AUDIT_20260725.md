# Audit of the proposed general PBBS mark ladder

Date: 2026-07-25

Method: exact unmatched-zero calculus. No search or computation is used.

## 0. Verdict

The proposed implication

\[
 A_0\longrightarrow C_0
 \quad\Longrightarrow\quad
 g(S\cup P_i)=S\cup P_{i+1}\quad(0\le i<q)
\]

is **false for an arbitrary \(A\to C\) boundary**. The first obstruction
is already present at \(q=2\), and there is a direct \(q=3\)
counterexample.

The valid clean-label rule says that flipping a zero keeps the old
forward marks immediately preceding that zero and the old reverse marks
immediately succeeding it. What fails is the next inference: after
flipping \(C_0\), the next reverse mark \(C_1\) need not be preceded by
the originally chosen \(A_0\) among the *surviving* forward marks. Some
forward marks lying in the physical arc \((C_0,C_1)\) can survive. Thus
the boundary \(A_0\to C_0\) need not peel to \(A_0\to C_1\).

This does **not** refute the strengthened construction in
PBBS_Q3_DEFICIT7_COMPLETE_SUPPORT_20260725.md. That construction chooses
the boundary after a global maximum of a gap potential. Its inequalities

\[
 x_j\le j,\qquad y_j\le j
\]

do force every required surviving boundary. Sections 6--8 below give an
independent audit of that repair. The resulting conclusions are:

1. the arbitrary-transition ladder is false;
2. Lemma 6.2 (global-maximum corridor) is correct;
3. Theorem 6.1 (corridor \(\Rightarrow\) \(q\)-edge PBBS ladder) is
   correct;
4. hence the updated complete-support theorem is not affected by the
   counterexamples in Sections 3--4.

## 1. The valid clean-label rule

Let a cyclic binary word have zero excess \(d\ge3\), so its forward and
reverse parenthesis matchings each leave \(d\) unmatched zeros. If a
zero \(u\) is changed to one, the new word has zero excess \(d-2\).

### Lemma 1.1

After changing \(u\) to one:

1. the forward unmatched zeros are the \(d-2\) old forward marks
   immediately preceding \(u\) in physical circular order;
2. the reverse unmatched zeros are the \(d-2\) old reverse marks
   immediately succeeding \(u\) in physical circular order.

Here the predecessor/successor is strict if \(u\) itself is a mark.

#### Proof

Cut the old word at its forward unmatched zeros and write it as

\[
 0_{a_0}D_0\,0_{a_1}D_1\cdots0_{a_{d-1}}D_{d-1},
\]

where every \(D_j\) is Dyck. If \(u=a_j\), changing it to one consumes
\(a_j\) and the next forward unmatched zero. If \(u\) is a down-step in
some \(D_j\), the changed block has final height two, and those two units
consume the first two forward unmatched zeros after \(u\). In either
case precisely the two forward marks at or immediately after \(u\)
disappear. The remaining \(d-2\) marks are exactly the strict
predecessors asserted above. Reversing the physical circle proves the
reverse statement. \(\square\)

The lemma is not the source of the failure.

## 2. Where the proposed peeling induction breaks

Suppose the combined mark word, with a shared coordinate displayed in
local order \(C,A\), has a transition

\[
 A_0\longrightarrow C_0.
\]

After flipping \(C_0\), Lemma 1.1 leaves the \(d-2\) forward marks
immediately preceding \(C_0\), and the \(d-2\) reverse marks immediately
succeeding \(C_0\). It does **not** follow that \(A_0\) is immediately
followed by \(C_1\) in the new combined mark word. Indeed, if at least
three old forward marks lie in the physical arc \((C_0,C_1)\), then all
but the first two of them survive and occur before \(C_1\).

This invalidates the claimed induction

\[
 A_0\to C_0
 \Longrightarrow A_0\to C_1
 \Longrightarrow A_0\to C_2\longrightarrow\cdots.
\]

The same issue occurs in the opposite direction when the proposed
ladder begins flipping \(A\)-marks.

## 3. A direct \(q=3\) counterexample

Take \(q=3\), \(m=10\), and \(n=21\). Let \(S\) be the rank-seven set
whose cyclic binary word is

\[
 \boxed{
 0_a\,1\,0_z\,
 0_{b_1}0_{b_2}0_{b_3}0_{b_4}0_{b_5}0_{b_6}\,
 1^6\,
 0_{c_1}0_{c_2}0_{c_3}0_{c_4}0_{c_5}0_{c_6}.}
\tag{3.1}
\]

It has seven ones and fourteen zeros, hence zero excess seven as
required for a rank-\((m-3)\) target.

Forward matching leaves exactly

\[
 U_+(S)=\{a,b_1,b_2,b_3,b_4,b_5,b_6\}.
\tag{3.2}
\]

Indeed, the displayed word has the forward Dyck decomposition

\[
 0_a(10_z)\,0_{b_1}\,0_{b_2}\,0_{b_3}\,0_{b_4}\,0_{b_5}\,
 0_{b_6}(1^60^6).
\]

Reverse matching pairs \(a\) with the first displayed one and pairs
\(b_6,b_5,\ldots,b_1\) with the later six ones. Hence

\[
 U_-(S)=\{z,c_1,c_2,c_3,c_4,c_5,c_6\}.
\tag{3.3}
\]

The combined mark word therefore contains the genuine consecutive
transition

\[
 A_a\longrightarrow C_z.
\tag{3.4}
\]

Choose it as the proposed \(A_0\to C_0\). With the prescribed indexing,

\[
 A_0=a,\quad A_1=b_6,\quad A_2=b_5,
\]

\[
 C_0=z,\quad C_1=c_1,\quad C_2=c_2.
\tag{3.5}
\]

The first claimed ladder edge is therefore

\[
 S\cup\{c_2,c_1,z\}
 \stackrel{?}{\longmapsto}
 S\cup\{c_1,z,a\}.
\tag{3.6}
\]

Put

\[
 R=S\cup\{z,c_1\}.
\]

This is a rank-\((m-1)\) core. Apply Lemma 1.1 twice. After flipping
\(z\), the forward and reverse marks are

\[
 \{a,b_6,b_5,b_4,b_3\},
 \qquad
 \{c_1,c_2,c_3,c_4,c_5\}.
\]

After then flipping \(c_1\), the marks of \(R\) are

\[
 U_+(R)=\{b_6,b_5,b_4\},
 \qquad
 U_-(R)=\{c_2,c_3,c_4\}.
\tag{3.7}
\]

In their surviving combined order, \(A_{b_6}\) is immediately followed
by \(C_{c_2}\). The exact deficit-three PBBS rule consequently gives

\[
 \boxed{
 g\bigl(R\cup\{c_2\}\bigr)=R\cup\{b_6\}.}
\tag{3.8}
\]

For completeness, the deficit-three rule follows because
\(r_+(R\cup\{c_2\})=b_6\) and
\(r_-(R\cup\{b_6\})=c_2\). Hence

\[
 f(R\cup\{c_2\})
 =[n]\setminus(R\cup\{b_6,c_2\})
 =f^{-1}(R\cup\{b_6\}),
\]

and applying \(f\) proves (3.8).

Since \(a\ne b_6\), equations (3.6)--(3.8) give the claimed failure:

\[
 \boxed{
 g\bigl(S\cup\{c_2,c_1,z\}\bigr)
 =S\cup\{c_1,z,b_6\}
 \ne S\cup\{c_1,z,a\}.}
\tag{3.9}
\]

Thus the first edge of the proposed \(q=3\) ladder can already be wrong.

## 4. The same obstruction already occurs at \(q=2\)

Take \(m=7,n=15\), and use the rank-five word

\[
 0_a\,1\,0_z\,
 0_{b_1}0_{b_2}0_{b_3}0_{b_4}\,
 1^4\,
 0_{c_1}0_{c_2}0_{c_3}0_{c_4}.
\tag{4.1}
\]

Its forward marks are \(a,b_1,b_2,b_3,b_4\), its reverse marks are
\(z,c_1,c_2,c_3,c_4\), and \(A_a\to C_z\) is consecutive. The proposed
first edge is

\[
 S\cup\{c_1,z\}
 \stackrel{?}{\longmapsto}
 S\cup\{z,a\}.
\]

But the core \(R=S\cup\{z\}\) has forward marks
\(a,b_4,b_3\) and reverse marks \(c_1,c_2,c_3\). Its surviving boundary
at \(c_1\) is \(A_{b_4}\to C_{c_1}\), so

\[
 \boxed{
 g(S\cup\{c_1,z\})=S\cup\{z,b_4\}\ne S\cup\{z,a\}.}
\tag{4.2}
\]

This does not contradict the separate theorem that every depth-two
target has some PBBS three-state witness. It only shows that an arbitrary
combined \(A\to C\) transition does not supply the advertised fixed-label
ladder. In (4.1), the later transition \(A_{b_4}\to C_{c_1}\) is the
well-positioned one.

## 5. The corrected exact gate

For the proposed windows \(P_i\), define their rank-\((m-1)\) common
cores

\[
 R_i=(S\cup P_i)\cap(S\cup P_{i+1})
 \qquad(0\le i<q).
\tag{5.1}
\]

Let

\[
 x_i=C_{q-1-i},\qquad y_i=A_i
\]

be respectively the deleted and inserted coordinates at step \(i\).
Then the exact PBBS criterion is

\[
 \boxed{
 g(R_i\cup\{x_i\})=R_i\cup\{y_i\}
 \iff
 \begin{cases}
 r_+(R_i\cup\{x_i\})=y_i,\\
 r_-(R_i\cup\{y_i\})=x_i.
 \end{cases}}
\tag{5.2}
\]

Equivalently, in the deficit-three mark data of \(R_i\), the surviving
forward mark \(A_{y_i}\) must immediately precede the surviving reverse
mark \(C_{x_i}\). The original single adjacency \(A_0\to C_0\) verifies
none of these later \(q\) conditions by itself.

Therefore a repaired all-depth theorem has to prove one of the following
genuinely stronger assertions:

1. every deficit-\((2q+1)\) word has a transition whose induced fixed
   labels satisfy all \(q\) conditions (5.2); or
2. a dynamically relabelled construction always produces a length-\(q\)
   path in the fibre over \(S\); or
3. a different PBBS argument supplies the required path.

The original arbitrary-cut argument proved none of them. The updated
global-maximum corridor lemma proves the first assertion; this is audited
next. The obstruction above is therefore an obstruction to the naive
selection rule, not to the strengthened all-depth theorem.

## 6. Audit of the global-maximum corridor lemma

Let the expanded mark word contain \(d=2q+1\) symbols of each type.
Index its \(C\)-symbols cyclically. Put

\[
 z_i=\#\{\text{\(A\)-symbols strictly between \(C_i\) and \(C_{i+1}\)}\}.
\tag{6.1}
\]

Then \(\sum_i z_i=d\). Define a periodic potential by

\[
 H(i+1)-H(i)=z_i-1.
\tag{6.2}
\]

Choose \(i\) at a global maximum of \(H\). Since

\[
 H(i)-H(i-1)=z_{i-1}-1\ge0,
\]

the gap immediately before \(C_i\) contains an \(A\)-symbol. Its final
\(A\)-symbol, called \(A_0\), is immediately followed by
\(C_0:=C_i\).

For \(j\ge1\), the number \(x_j\) of \(A\)-symbols strictly between
\(C_0\) and \(C_j=C_{i+j}\) is

\[
 x_j=\sum_{h=0}^{j-1}z_{i+h}.
\]

Maximality gives

\[
 x_j-j=H(i+j)-H(i)\le0,
\]

so

\[
 \boxed{x_j\le j.}
\tag{6.3}
\]

For the reverse inequality, the \(L\) gaps ending at the selected gap
contain

\[
\begin{aligned}
\sum_{h=1}^{L}z_{i-h}
&=d-\sum_{h=0}^{d-L-1}z_{i+h}\\
&\ge d-(d-L)=L.
\end{aligned}
\tag{6.4}
\]

Take \(L=j+1\). The current gap and the preceding \(j\) gaps contain at
least \(j+1\) \(A\)-symbols. Starting from the final \(A\)-symbol in the
current gap, the \(j\)-th preceding \(A\)-symbol is therefore reached
after crossing at most \(j\) \(C\)-symbols. Hence

\[
 \boxed{y_j\le j.}
\tag{6.5}
\]

This proves Lemma 6.2, including both orientations. The argument remains
valid when an \(A\)- and \(C\)-symbol share a physical coordinate,
because the expanded local order \(C,A\) assigns that \(A\)-symbol to
the gap following its \(C\)-copy.

## 7. Audit of the corridor-to-ladder theorem

Assume now only the weaker corridor bounds

\[
 x_j\le2j,\qquad y_j\le2j
 \quad(1\le j\le q-1).
\tag{7.1}
\]

At the selected boundary index the \(A\)-marks forward as

\[
 F_0=A_0,F_1,\ldots,F_{d-1},
\qquad A_h=F_{d-h}\quad(\bmod d),
\tag{7.2}
\]

and index the \(C\)-marks forward as \(C_0,C_1,\ldots,C_{d-1}\).

Fix \(0\le t<q\) and put

\[
 r=q-t-1,
\]

\[
 K_t=S\cup\{C_0,\ldots,C_{r-1}\}
          \cup\{A_0,\ldots,A_{t-1}\}.
\tag{7.3}
\]

This is the proposed common rank-\((m-1)\) core.
The coordinate-distinctness check in Section 8 is independent of the
mark-elimination calculation and may formally be read first; it ensures
that every displayed flip below changes a zero to one.

### 7.1 Forward marks

Flip \(C_0,C_1,\ldots,C_{r-1}\) in order. After the first \(j\) flips,
the removed forward marks are exactly

\[
 F_1,F_2,\ldots,F_{2j}.
\tag{7.4}
\]

Indeed, \(x_j\le2j\) says that every \(A\)-mark strictly between
\(C_0\) and \(C_j\) is among those already removed. Thus the first two
current forward marks at or after \(C_j\) are
\(F_{2j+1},F_{2j+2}\), and Lemma 1.1 removes precisely those two.

After the \(r\) \(C\)-flips, the forward marks are

\[
 F_0,F_{2r+1},F_{2r+2},\ldots,F_{d-1}.
\tag{7.5}
\]

Now flip \(A_0,A_1,\ldots,A_{t-1}\). Each is a current forward mark:
the flip removes that mark itself at the high-index end and the next
current mark at the low-index end. Since

\[
 d-2r=2t+3,
\]

the three final forward marks are exactly

\[
 \boxed{U_+(K_t)=\{A_t,A_{t+1},A_{t+2}\}.}
\tag{7.6}
\]

The bound \(x_r\le2r\) places \(C_r\) before all three surviving marks
in the forward traversal from \(C_0\). They occur in the order
\(A_{t+2},A_{t+1},A_t\), so the strict forward predecessor of \(C_r\)
is \(A_t\).

### 7.2 Reverse marks

Analyze the same final set in the opposite flip order. First flip
\(A_0,\ldots,A_{t-1}\). The inequalities \(y_j\le2j\) show inductively
that these flips remove the last \(2t\) \(C\)-marks. Then flip the
current reverse marks \(C_0,\ldots,C_{r-1}\). Each removes itself and
the final current reverse mark. Since again \(d-2t-2r=3\), this leaves

\[
 \boxed{U_-(K_t)=\{C_r,C_{r+1},C_{r+2}\}.}
\tag{7.7}
\]

The bound \(y_t\le2t\) puts \(A_t\) after all removed preceding
\(C\)-marks and before the first surviving one. Therefore the strict
reverse successor of \(A_t\) is \(C_r\).

The deficit-three law now gives

\[
 \boxed{
 g(K_t\cup\{C_r\})=K_t\cup\{A_t\}.}
\tag{7.8}
\]

This proves every arrow in the proposed \(q\)-edge path.

## 8. Coordinate coincidences and the common intersection

It remains to check that shared \(A/C\) coordinates do not collapse a
state or survive in every state. Suppose \(C_j=A_h\). Because the local
expanded order is \(C_j,A_h\), for the relevant indices
\(0\le j,h\le q-1\) one has

\[
 x_j=d-h-1.
\tag{8.1}
\]

If \(j+h\le q-1\), then

\[
 x_j=2q-h\ge q+j+1>2j,
\]

contradicting the corridor inequality. Thus

\[
 \boxed{C_j=A_h\ \Longrightarrow\ j+h\ge q}
\tag{8.2}
\]

throughout the selected index ranges.

Coordinates \(C_j\) and \(A_h\) occur together in some \(P_t\) only
when \(j+h\le q-2\), so (8.2) proves that every \(P_t\) has \(q\)
distinct coordinates. Their two ranges of appearances cover all
\(t=0,\ldots,q\) only when \(j+h\le q-1\), again excluded by (8.2).
Hence no extra coordinate survives all \(q+1\) states, and

\[
 \boxed{\bigcap_{t=0}^{q}(S\cup P_t)=S.}
\tag{8.3}
\]

The endpoint case \(j=0\) is harmless: a shared \(A\)-copy immediately
after \(C_0\) is \(A_{d-1}\), outside the selected range
\(A_0,\ldots,A_{q-1}\).

Therefore the global-maximum cut supplies a valid corridor and the
corridor supplies the complete PBBS ladder. The arbitrary-cut
counterexamples remain correct but do not invalidate Theorems 6.1--6.3
of the updated note.
