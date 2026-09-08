# PBBS \(q\)-fans: complete support, the exact \(q=2\) row, and unbounded Gaussian multiplicity

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, web
input, or asymptotic heuristic is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad
 \mathcal M=\binom{[n]}m,\qquad
 W=|\mathcal M|,\qquad
 B=\frac{W}{2m+1}=\operatorname {Cat}_m.
 \tag{0.1}
\]

Let \(f\) be the canonical cyclic-parenthesis/PBBS permutation of
\(\mathcal M\), and put \(g=f^2\).  The natural lower \(q\)-fan based at
\(A\in\mathcal M\) is the step-two orbit segment

\[
 \mathcal F_q(A)=(A,gA,\ldots,g^qA),
 \qquad
 \Theta_q^-(A)=\bigcap_{t=0}^qg^tA.                 \tag{0.2}
\]

Its upper companion is

\[
 \Theta_q^+(A)=\bigcup_{t=0}^qg^tA.                 \tag{0.3}
\]

At \(q=1\), if \(X=f(A)\), then

\[
 \Theta_1^-(A)=f^{-1}(X)\cap f(X),
 \]

so (0.2) is exactly the PBBS angle, not a new surrogate.

The following statements are proved.

1. **Complete lower support at every depth.**  For every
   \(1\le q\le m\) and every
   \(S\in\binom{[n]}{m-q}\), there is a directed \(q\)-edge \(g\)-fan
   whose intersection is exactly \(S\).

2. **Exact multiplicity cap.**  If \(\mu_q^-(S)\) counts correct-rank
   based lower fans with target \(S\), then

   \[
   \boxed{
   1\le\mu_q^-(S)\le\binom{2q+1}{q}.}                \tag{0.4}
   \]

3. **Complete upper support.**  For every \(1\le q\le m\),

   \[
   \boxed{
   \mu_q^+(U)=\mu_{q-1}^-(U^c),}                     \tag{0.5}
   \]

   where only correct-rank fans are counted.  Hence every
   \((m+q)\)-set occurs and

   \[
   1\le\mu_q^+(U)\le\binom{2q-1}{q-1}.               \tag{0.6}
   \]

4. **The complete \(q=2\) row.**  Every based lower \(2\)-fan has rank
   exactly \(m-2\), and

   \[
   1\le\mu_2^-(S)\le10.                              \tag{0.7}
   \]

   Every based upper \(2\)-fan has rank exactly \(m+2\), and

   \[
   1\le\mu_2^+(U)\le3.                               \tag{0.8}
   \]

   For \(m\ge8\), their floor-one collision energies obey

   \[
   \boxed{Q_2^-<48B,\qquad Q_2^+<2B.}                \tag{0.9}
   \]

5. **Uniform bounded multiplicity is false at growing depth.**  For every
   fixed \(A>0\), there are \(m_j\to\infty\), depths
   \(q_j\to\infty\) with \(q_j\le A\sqrt {m_j}\), and targets \(S_j\)
   such that

   \[
   \boxed{\mu_{q_j}^-(S_j)\ge2q_j+1.}                \tag{0.10}
   \]

   This lower bound is forced by a target stabilizer and is exact at the
   symmetry level: the order of any rotational stabilizer of an
   \((m-q)\)-target divides \(2q+1\).

Thus the PBBS angle theorem has a genuine all-depth support analogue, and
the entire two-sided \(q=2\) row is Catalan-cheap.  A bound independent of
\(q\) is impossible in a Gaussian window.  The present general cap is
polynomial in \(m\) for \(q=O(\log m)\), but is
\(\exp(O_A(\sqrt m))\) at \(q\le A\sqrt m\).  Whether the latter can be
replaced by \(m^{O_A(1)}\), or whether a superpolynomial load family exists,
remains open.

## 1. PBBS chronology and fan targets

Represent an \(m\)-set by its cyclic binary word, with \(1\) an opening
step and \(0\) a closing step.  Cyclic forward matching leaves one
unmatched zero \(r_+(A)\), and

\[
 f(A)=A^c\setminus\{r_+(A)\}.                        \tag{1.1}
\]

Reverse matching leaves \(r_-(A)\), with

\[
 f^{-1}(A)=A^c\setminus\{r_-(A)\}.                   \tag{1.2}
\]

On an \(f\)-orbit write \(A_i=f^i(A_0)\), and let

\[
 \lambda_i=[n]\setminus(A_i\cup A_{i+1})
\]

be the omitted coordinate on its Kneser edge.  Applying (1.1) twice gives

\[
 \boxed{
 A_{i+2}=A_i-\{\lambda_{i+1}\}+\{\lambda_i\}.}       \tag{1.3}
\]

Thus \(g=f^2\) is a directed Johnson permutation.  In a based \(q\)-fan,
an original coordinate leaves the intersection exactly at its first
deletion.  Therefore

\[
 \Theta_q^-(A_i)
 =A_i\setminus
 \{\lambda_{i+2t+1}:
   \lambda_{i+2t+1}\in A_i,\ 0\le t<q\}.             \tag{1.4}
\]

In particular, the fan has correct lower rank \(m-q\) exactly when the
\(q\) effective deleted labels are distinct original coordinates.

There is an exact cross-shore identity.  Formula (1.1) gives

\[
 A_{j+1}=[n]\setminus(A_j\cup A_{j+2}).
\]

Intersecting this identity for \(j=i,i+2,\ldots,i+2q-2\) yields

\[
 \boxed{
 [n]\setminus\bigcup_{t=0}^qA_{i+2t}
 =\bigcap_{t=0}^{q-1}A_{i+2t+1}.}                   \tag{1.5}
\]

The right side is a lower \((q-1)\)-fan on the opposite parity.  Taking
complements proves (0.5), including multiplicities and wrong-rank
correspondence.

## 2. Unmatched-mark lemmas

Fix \(S\in\binom{[n]}{m-q}\), and put

\[
 d=n-2|S|=2q+1.                                      \tag{2.1}
\]

Forward and reverse matching of the word of \(S\) each leave \(d\)
unmatched zeros.  Mark the forward survivors by \(A\) and the reverse
survivors by \(C\).  If one coordinate is a survivor in both matchings,
replace its physical mark by the two consecutive symbols

\[
 C_x,A_x.                                            \tag{2.2}
\]

### Lemma 2.1 (clean-label deletion)

If a zero \(x\) in a word of positive odd deficit \(d\) is changed to one,
then:

- the new forward-unmatched set consists of the \(d-2\) old forward
  marks immediately preceding \(x\);
- the new reverse-unmatched set consists of the \(d-2\) old reverse
  marks immediately succeeding \(x\).

The statement remains valid when \(x\) is itself an old mark, using the
local order (2.2).

#### Proof

Cut the word at its forward-unmatched zeros:

\[
 0_{a_0}D_0\,0_{a_1}D_1\cdots0_{a_{d-1}}D_{d-1},
\]

where every \(D_i\) is Dyck.  If \(x=a_i\), changing it to one consumes
\(a_i\) and \(a_{i+1}\).  If \(x\) lies inside \(D_i\), the flip creates
two units of forward excess, which consume \(a_{i+1},a_{i+2}\).
Precisely the \(d-2\) old marks preceding \(x\) remain.  Reversing the
physical circle proves the reverse statement. \(\square\)

We also need the exact deficit-three transition law.

### Lemma 2.2 (one-edge criterion)

Let \(K\in\binom{[n]}{m-1}\), and let \(P=U_+(K)\) and
\(Q=U_-(K)\) be its three forward and three reverse unmatched zeros.
For distinct \(x,y\notin K\),

\[
 \boxed{
 g(K\cup\{x\})=K\cup\{y\}
 \iff
 y=\operatorname{pv}_{P}(x),\quad
 x=\operatorname{nx}_{Q}(y),}                       \tag{2.3}
\]

where \(\operatorname{pv}\) is strict cyclic predecessor and
\(\operatorname{nx}\) strict cyclic successor.

#### Proof

The forward and inverse PBBS formulas give

\[
\begin{aligned}
 f(K\cup\{x\})
 &=K^c\setminus\{x,r_+(K\cup\{x\})\},\\
 f^{-1}(K\cup\{y\})
 &=K^c\setminus\{y,r_-(K\cup\{y\})\}.
\end{aligned}
\]

Lemma 2.1 in deficit three says

\[
 r_+(K\cup\{x\})=\operatorname{pv}_{P}(x),\qquad
 r_-(K\cup\{y\})=\operatorname{nx}_{Q}(y).
\]

The two displayed complements are equal exactly when their omitted
two-sets are equal.  Since neither unmatched zero equals the flipped
coordinate, equality is precisely (2.3). \(\square\)

### Lemma 2.3 (global-maximum boundary)

In the expanded circular word with \(d\) \(A\)-marks and \(d\)
\(C\)-marks, there is a consecutive boundary \(A_0,C_0\) such that,
after numbering \(C_0,C_1,\ldots\) forward and
\(A_0,A_1,\ldots\) backward,

\[
 x_j\le j,\qquad y_j\le j
 \qquad(1\le j\le d-1),                              \tag{2.4}
\]

where \(x_j\) is the number of \(A\)-marks strictly between \(C_0,C_j\),
and \(y_j\) is the reverse-dual count.

#### Proof

Index the \(C\)-marks cyclically and let \(z_i\) be the number of
\(A\)-marks strictly between \(C_i,C_{i+1}\).  Then
\(\sum_i z_i=d\).  Define a periodic potential by

\[
 H(i+1)-H(i)=z_i-1.
\]

Choose \(i\) at a global maximum.  The gap immediately preceding \(C_i\)
is nonempty; take its final \(A\)-mark as \(A_0\), and put \(C_0=C_i\).
Then

\[
 x_j-j
 =\sum_{s=0}^{j-1}(z_{i+s}-1)
 =H(i+j)-H(i)\le0.
\]

The current gap and the preceding \(j\) gaps contain

\[
 d-\sum_{s=0}^{d-j-2}z_{i+s}\ge j+1
\]

\(A\)-marks.  Starting from the last \(A\)-mark in the current gap, the
\(j\)-th preceding \(A\)-mark is therefore reached after crossing at most
\(j\) \(C\)-marks.  Hence \(y_j\le j\). \(\square\)

One collision identity will be used repeatedly.  If the physical
coordinate carrying \(C_j\) also carries \(A_h\), then the forced local
order (2.2) gives

\[
 x_j=d-h-1=2q-h.                                     \tag{2.5}
\]

Together with (2.4), this implies

\[
 \boxed{C_j=A_h\Longrightarrow j+h\ge2q.}            \tag{2.6}
\]

## 3. The exact \(q=2\) theorem

We first prove that every based lower \(2\)-fan has the correct rank.

Normalize a middle state as \(0_rD\), where \(r\) is its forward-unmatched
zero and \(D\) is a Dyck word.  Let \(H\) be the height of \(D\).  Define:

- \(p_+(D)\): the first up-step reaching height \(H\);
- \(p_-(D)\): the initial up-step of the last primitive Dyck factor of
  height \(H\);
- \(v(D)\): the down-step following the rightmost occurrence of height
  \(H\).

### Lemma 3.1 (two distinguished deletions)

\[
\begin{aligned}
 g(A)&=(A\cup\{r\})\setminus\{p_+(D)\},\\
 g^{-1}(A)&=(A\cup\{v(D)\})\setminus\{p_-(D)\},
\end{aligned}                                                \tag{3.1}
\]

and, for \(m\ge2\),

\[
 p_+(D)\ne p_-(D).                                  \tag{3.2}
\]

#### Proof

Write \(D=P\,1_{p_+}Q\), where the displayed step first reaches the
maximum.  After one PBBS update, root at \(p_+\).  Complementation turns
the suffix into

\[
 0_{p_+}\,\overline Q\,0_r\,\overline P.
\]

The height inequalities defining the first maximum say that the suffix
after \(0_{p_+}\) is Dyck.  Hence \(p_+\) is the next forward-unmatched
zero, and applying \(f\) again gives the first formula in (3.1).

For the inverse formula, write \(D=P\,0_vQ\), where \(P\) ends at the
rightmost maximum.  Reverse matching leaves the displayed down-step
\(v(D)\).  Rooting \(f^{-1}(A)\) there gives

\[
 0_v\,\overline Q\,1_r\,\overline P.
\]

The suffix \(E=\overline Q\,1_r\,\overline P\) is Dyck:
\(\overline Q\) rises from zero to \(H-1\), the step \(1_r\) reaches
\(H\), and the height along \(\overline P\) is \(H-h_P\ge0\).
Let \(C_1\cdots C_s\) be the primitive factorization of \(D\), and let
\(C_j\) be the last factor of height \(H\).  Write \(P=LR\), where
\(L=C_1\cdots C_{j-1}\) and \(R\) is the nonempty prefix of \(C_j\)
ending immediately before \(v\).  The part \(\overline Q\) never reaches
height \(H\).  After \(1_r\), height \(H\) is reached exactly at ends of
complete factors in \(P\), the last such end being \(L\); the next symbol
is the complement of the initial up-step of \(C_j\), namely the zero
\(p_-(D)\).  Thus it is the next reverse-unmatched zero, proving the
second formula.

If the first and last tallest primitive factors differ, the two positions
are distinct.  If they agree and \(H\ge2\), \(p_-\) reaches height one
while \(p_+\) reaches height \(H\).  If \(H=1\), then
\(D=(10)^m\); for \(m\ge2\), its first and last primitive factors differ.
This proves (3.2). \(\square\)

Consequently

\[
 g^{-1}(A)\cap A\cap g(A)
 =A\setminus\{p_-(D),p_+(D)\}
\]

has rank \(m-2\).  Re-centering shows that every based fan
\((A,gA,g^2A)\) has correct lower rank.  By (1.5), every based upper
\(2\)-fan also has correct rank.

We now prove target coverage directly.  Fix
\(S\in\binom{[n]}{m-2}\), so \(d=5\).  Choose the boundary of Lemma 2.3
and put

\[
\begin{aligned}
 B_0&=S\cup\{C_0,C_1\},\\
 B_1&=S\cup\{C_0,A_0\},\\
 B_2&=S\cup\{A_0,A_1\}.                              \tag{3.3}
\end{aligned}
\]

Equation (2.6) shows that all selected \(A\)- and \(C\)-coordinates are
distinct where required, and that their common extra intersection is
empty.

For \(K_0=S\cup\{C_0\}\), Lemma 2.1 and \(x_1,y_1\le1\) give

\[
 U_+(K_0)=\{A_0,A_1,A_2\},\qquad
 U_-(K_0)=\{C_1,C_2,C_3\}.                          \tag{3.4}
\]

The strict predecessor of \(C_1\) in the first triple is \(A_0\), and
the strict successor of \(A_0\) in the second is \(C_1\).  Lemma 2.2
therefore gives \(g(B_0)=B_1\).

Likewise, for \(K_1=S\cup\{A_0\}\),

\[
 U_+(K_1)=\{A_1,A_2,A_3\},\qquad
 U_-(K_1)=\{C_0,C_1,C_2\},                          \tag{3.5}
\]

and Lemma 2.2 gives \(g(B_1)=B_2\).  Hence

\[
 B_0\cap B_1\cap B_2=S,
\]

proving complete lower \(q=2\) support.

For the multiplicity cap, consider any correct \(2\)-fan with target
\(S\).  At each arrow its deleted label belongs to the reverse-unmatched
triple of the rank-\((m-1)\) overlap core.  Repeated use of Lemma 2.1
puts both deleted initial extras in the five-set \(U_-(S)\).  They are
distinct, and their unordered pair determines the initial state and hence
the deterministic fan.  Thus

\[
 1\le\mu_2^-(S)\le\binom52=10.                       \tag{3.6}
\]

The constant ten is sharp under the stated \(m\ge2\) quantifier: when
\(m=2\), the only target is \(S=\varnothing\), every one of the
\(\binom52=10\) based fans has rank zero, and hence
\(\mu_2^-(\varnothing)=10\).
This also rules out a tempting boundary-only classification of all fans.
For the empty five-coordinate word the expanded mark circle has only five
\(A\)-to-\(C\) global-maximum boundaries, but there are ten occurrences.
The global-maximum ladder is a support construction, not a normal form for
all occurrences.

Equation (1.5) identifies upper \(2\)-fan loads with lower angle loads,
so the depth-one angle theorem gives

\[
 1\le\mu_2^+(U)\le3.                                \tag{3.7}
\]

Finally let

\[
 N_2^-=\binom{2m+1}{m-2},\qquad
 N_2^+=\binom{2m+1}{m+2}
      =\binom{2m+1}{m-1}.
\]

For \(m\ge8\), both balanced floors are one.  Put

\[
 Q_2^\pm=\sum_T\binom{\mu_2^\pm(T)-1}{2}.            \tag{3.8}
\]

Since every lower target occurs and every load is at most ten,

\[
\begin{aligned}
 Q_2^-
 &\le4\sum_S(\mu_2^-(S)-1)\\
 &=4(W-N_2^-)\\
 &=\frac{24(m+1)}{(m+2)(m+3)}W
 <48B.                                               \tag{3.9}
\end{aligned}
\]

For the upper row, loads lie in \(\{1,2,3\}\).  If \(a_j\) is the number
of load-\(j\) targets, then

\[
 a_2+2a_3=W-N_2^+=\frac{2W}{m+2}.
\]

Therefore

\[
 Q_2^+=a_3\le\frac{W}{m+2}<2B.                      \tag{3.10}
\]

This proves (0.7)--(0.9) with exact constants.

## 4. Complete support at arbitrary depth

Fix \(1\le q\le m\), set \(d=2q+1\), and choose the global-maximum
boundary from Lemma 2.3.  Define

\[
 P_t=
 \{C_0,\ldots,C_{q-t-1}\}
 \cup
 \{A_0,\ldots,A_{t-1}\},
 \qquad0\le t\le q,                                  \tag{4.1}
\]

with empty ranges omitted, and put \(B_t=S\cup P_t\).

Equation (2.6) first shows that every \(P_t\) has \(q\) distinct physical
coordinates.  A shared coordinate \(C_j=A_h\) could lie in every \(P_t\)
only if \(j+h\le q-1\), again contradicting (2.6).  Hence

\[
 |B_t|=m,\qquad \bigcap_{t=0}^qB_t=S.                \tag{4.2}
\]

It remains to prove the arrows.  Fix \(0\le t<q\), put
\(r=q-t-1\), and let

\[
 K_t=
 S\cup\{C_0,\ldots,C_{r-1}\}
  \cup\{A_0,\ldots,A_{t-1}\}.                       \tag{4.3}
\]

Then \(B_t=K_t\cup\{C_r\}\) and
\(B_{t+1}=K_t\cup\{A_t\}\).

Number the original forward marks by

\[
 F_0=A_0,F_1,\ldots,F_{d-1},
 \qquad A_h=F_{d-h}\quad(h\ge1).                    \tag{4.4}
\]

Process the flips \(C_0,\ldots,C_{r-1}\).  Before \(C_j\) is flipped,
all original forward marks between \(C_0\) and \(C_j\) have indices at
most \(x_j\le j\).  Induction with Lemma 2.1 therefore removes exactly

\[
 F_1,\ldots,F_{2r}.                                  \tag{4.5}
\]

The selected marks used next really survive this stage.  One has
\(A_0=F_0\), while for \(1\le h<t\),

\[
 A_h=F_{d-h},\qquad
 d-h=2q+1-h>2q-2t-2=2r.
\]

Now process \(A_0,\ldots,A_{t-1}\).  They remove the selected cyclic
tail

\[
 F_0,F_{d-1},\ldots,F_{d-t+1}
\]

and, respectively, the next surviving low-index marks

\[
 F_{2r+1},\ldots,F_{2r+t}.
\]

This is another direct induction from Lemma 2.1: at each stage the chosen
\(A_j\) is a current forward mark, so it and the first current mark after
it disappear.  Since \(d-2r=2t+3\), exactly

\[
 U_+(K_t)=\{A_t,A_{t+1},A_{t+2}\}                   \tag{4.6}
\]

remain.  The same induction in the reversed physical circle gives

\[
 U_-(K_t)=\{C_r,C_{r+1},C_{r+2}\}.                  \tag{4.7}
\]

The inequalities \(x_r\le r\), \(y_t\le t\), together with the local
order \(C,A\) at a shared mark, show that \(A_t\) is the strict forward
predecessor of \(C_r\) in (4.6), while \(C_r\) is the strict reverse
successor of \(A_t\) in (4.7).  Lemma 2.2 now gives

\[
 g(B_t)=B_{t+1}.                                     \tag{4.8}
\]

Thus (4.1) is a genuine directed PBBS fan and (4.2) proves complete
support for every \(q\).

For the cap, take any correct fan with target \(S\).  Its \(q\) initial
extras must all be deleted during its \(q\) arrows; hence they are
distinct and no deletion is spent on an inserted label.  At each arrow,
Lemma 2.2 and repeated clean-label contraction put the deleted label in
the original \((2q+1)\)-set \(U_-(S)\): each overlap core is obtained
from \(S\) by \(q-1\) zero-to-one flips, and Lemma 2.1 only deletes
members from the reverse-unmatched set, so
\(U_-(K_t)\subseteq U_-(S)\).  The \(q\)-subset of initial
extras determines the initial state, and \(g\) determines the whole fan.
Therefore

\[
 \mu_q^-(S)\le\binom{2q+1}{q}.                       \tag{4.9}
\]

Together with support this proves (0.4).  Equation (1.5) then proves
(0.5)--(0.6).

## 5. Rotational multiplicity and a Gaussian counterfamily

Identify the coordinate circle with \(\mathbb Z_n\).  The PBBS map is
rotation-equivariant.

### Lemma 5.1 (target stabilizer divisibility)

Let \(S\in\binom{[n]}{m-q}\), and let its rotational stabilizer have order
\(h\).  Then

\[
 \boxed{h\mid(2q+1).}                                \tag{5.1}
\]

Moreover every stabilizer orbit on the set of based correct occurrences
of \(S\) has size exactly \(h\).  In particular,

\[
 \boxed{h\mid\mu_q^-(S).}                            \tag{5.2}
\]

#### Proof

The stabilizer subgroup of order \(h\) acts freely on the \(n\)
coordinates, with every coordinate orbit of size \(h\).  Hence

\[
 h\mid n,\qquad h\mid|S|=m-q.
\]

It follows that

\[
 h\mid n-2(m-q)=2q+1,
\]

proving (5.1).

If a nonidentity stabilizer element of order \(d\mid h\) fixed an
occurrence's initial \(m\)-set, then \(d\mid m\).  But \(d\mid n=2m+1\),
so \(\gcd(d,m)=1\), forcing \(d=1\).  Thus the stabilizer acts freely on
the occurrence roots.  Rotation equivariance preserves the target and
the fan, proving (5.2). \(\square\)

### Theorem 5.2 (unbounded multiplicity inside every Gaussian window)

Fix \(A>0\).  There are infinitely many \(m,q,S\) with

\[
 q\to\infty,\qquad q\le A\sqrt m,\qquad
 \mu_q^-(S)\ge2q+1.                                  \tag{5.3}
\]

#### Proof

Choose odd integers \(h\to\infty\), put

\[
 q=\frac{h-1}{2},
\]

and choose an odd integer \(p\ge3\) satisfying

\[
 \frac{(h-1)^2}{4}
 \le A^2\,\frac{hp-1}{2}.                            \tag{5.4}
\]

Set

\[
 n=hp,\qquad m=\frac{hp-1}{2}.
\]

Choose a primitive binary block \(R\subset\mathbb Z_p\) of size
\((p-1)/2\), for example one proper consecutive interval.  Such an
interval has trivial stabilizer: any stabilizer order would divide both
\(p\) and \((p-1)/2\), whose greatest common divisor is one.  Repeat it
in all \(h\) blocks:

\[
 S=\{tp+r:t\in\mathbb Z_h,\ r\in R\}
 \subset\mathbb Z_{hp}.                              \tag{5.5}
\]

Then

\[
 |S|=\frac{h(p-1)}2=m-q.                             \tag{5.6}
\]

The word of \(S\) has minimal rotational period \(p\), so its stabilizer
has order exactly \(h=2q+1\).  The complete-support theorem supplies at
least one correct occurrence.  Lemma 5.1 turns its stabilizer orbit into
\(h\) distinct occurrences, whence

\[
 \mu_q^-(S)\ge h=2q+1.
\]

Inequality (5.4) is precisely \(q\le A\sqrt m\). \(\square\)

If \(p\) is chosen as the least admissible odd integer in (5.4), then
\(p/h\to(2A^2)^{-1}\) and in fact \(q/\sqrt m\to A\).  Thus the
unbounded family can be placed at any prescribed positive Gaussian ratio,
not merely somewhere below it.

A particularly transparent subfamily takes \(p=h\).  Then

\[
 m=\frac{h^2-1}{2},\qquad
 q=\frac{h-1}{2},\qquad
 \frac q{\sqrt m}\longrightarrow\frac1{\sqrt2},
\]

and the target is an \(h\)-fold repetition of a primitive half-density
block.

The stabilizer mechanism cannot itself force more than linear growth:
Lemma 5.1 gives \(h\le2q+1\), and Theorem 5.2 attains equality.

For the square subfamily \(p=h\), the target necklace has exactly \(h\)
distinct rotations and every one has load at least \(h\).  Moreover

\[
 \log\frac{W}{\binom{2m+1}{m-q}}
 =\frac{q(q+1)}m+O\!\left(\frac{q^3}{m^2}\right)
 =\frac12+O(q^{-1}).
\]

Thus the correct-window histogram has floor one for all sufficiently large
\(q\): complete support makes its total mass at least the target count,
while its total mass is at most \(W<2\binom{2m+1}{m-q}\).  Its
floor-one energy therefore has the exact lower bound

\[
 \sum_T\binom{\mu_q^-(T)-1}{2}
 \ge h\binom{h-1}{2}
 =\frac{h(h-1)(h-2)}2
 =(\sqrt2+o(1))m^{3/2}.                              \tag{5.7}
\]

This is a genuine spike obstruction to bounded pointwise load, but it is
still \(o(B)\).  Hence it does not by itself obstruct a Catalan-scale
global collision theorem.

## 6. Exact asymptotic boundary

Stirling's formula gives

\[
 \binom{2q+1}{q}
 =\left(\frac{2}{\sqrt{\pi q}}+o(q^{-1/2})\right)4^q.
 \tag{6.1}
\]

Consequently:

- for fixed \(q\), every lower fan multiplicity is bounded by a constant
  depending only on \(q\);
- for \(q\le c\log m\),

  \[
  \mu_q^-(S)\le2\cdot4^q\le2m^{c\log4};
  \]

- for \(q\le A\sqrt m\), the proved cap is only

  \[
  \mu_q^-(S)\le
  \exp\!\bigl((\log4)A\sqrt m+O(\log m)\bigr);
  \]

- no \(O_A(1)\) cap is possible in that window, by Theorem 5.2.

The exact surviving multiplicity problem is:

> Determine whether
> \[
> \max_{q\le A\sqrt m}\max_S\mu_q^-(S)
> \le m^{O_A(1)},
> \]
> or construct a target family with superpolynomial correct-fan load.

This question is separate from support, which is completely solved, and
from wrong-rank residence: for \(q\ge3\), PBBS can have other based fans
whose intersections have rank larger than \(m-q\).

For constant-one, the positive content is exact: all lower and upper fan
targets exist, and the complete \(q=2\) collision cost is \(O(B)\).  The
negative content is equally exact: a bounded all-depth multiplicity theorem
is false, and the current exponential cap is insufficient for the Gaussian
floor-completion ledger.
