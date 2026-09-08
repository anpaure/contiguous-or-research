# Independent audit: PBBS all-depth corridor and fixed-band literal words

Date: 2026-07-26

## Verdict

The following statements survive an independent index-by-index audit.

1. The global-maximum mark lemma (Theorem 4.1 of
   `MATH_ATTACK_AD15_DIRECT_PBBS_ALLQ_EROSION_AUDIT_20260725.md`) is
   correct, including shared physical coordinates.
2. Conditional only on the standard PBBS one-flip unmatched-zero rule and
   the deficit-three arrow criterion, its all-depth consequence is correct:
   for each
   \(S\in\binom{[2m+1]}{m-q}\) there is a forward \(q\)-edge
   \(g=f^2\) path whose full intersection is exactly \(S\), and the number
   of such forward oriented starts is at most
   \(\binom{2q+1}{q}\).
3. The five-rank literal word bound
   \[
      |Q_2|\le W+4\operatorname{Cat}_m
   \]
   is correct for \(m\ge2\), and covers ranks
   \(m-1,m,m+1,m+2,m+3\).
4. The seven-rank literal word bound
   \[
      |Q_3|\le W+6\operatorname{Cat}_m
        +21(2m+1)(m-1)
   \]
   is correct for \(m\ge3\), provided the imported exact PBBS gap-five
   classification is retained. It covers ranks
   \(m-2,m-1,m,m+1,m+2,m+3,m+4\).

These are upper bounds, not exact word lengths.  They are fixed-depth
results.  They neither produce wreath rows nor settle a growing central
band.

Two nearby claims should not be imported.

* From \(K_P\le W/(2m+1)\) one gets average projected component length
  **at least** \(2m+1\), not equality.  Equality would require
  \(K_P=W/(2m+1)\), which is not proved.
* For \(m\ge3\), complete first-shadow support with loads in
  \(\{1,2,3\}\) does not put
  balanced overload at its integrality floor.  If \(a_j\) is the number
  of load-\(j\) targets, then
  \[
     a_2+2a_3=W-N_1={2W\over m+2},
     \qquad O_1=a_3\le {W\over m+2}.
  \]
  The true balanced floor is \(O_1=0\), attained exactly when \(a_3=0\).

## 1. Global-maximum corridor

Let \(z_i\) be the number of expanded \(A\)-symbols in the open gap
from \(C_i\) to \(C_{i+1}\).  Shared coordinates are expanded as
\(C_x,A_x\), so the \(A_x\)-copy belongs to the gap *after* \(C_x\),
and still
\[
   \sum_{i\in\mathbb Z_d}z_i=d.
\]
Set \(h(i+1)-h(i)=z_i-1\), and choose \(i\) at a global maximum.
Then \(z_{i-1}\ge1\), so the last \(A\)-symbol in that gap gives a
genuine boundary \(A_0,C_0\).  For the forward-numbered \(C_j\),
\[
 x_j=\sum_{s=0}^{j-1}z_{i+s},\qquad
 x_j-j=h(i+j)-h(i)\le0.
\]
For the backwards-numbered \(A_j\), maximality also gives
\[
 \sum_{s=1}^{L}z_{i-s}
 =d-\sum_{s=0}^{d-L-1}z_{i+s}\ge L.
\]
Taking \(L=j+1\) shows that the \(j\)-th preceding \(A\)-symbol is
reached after crossing at most \(j\) \(C\)-symbols, hence \(y_j\le j\).
This proves both inequalities with no generic-position assumption.

## 2. Corridor-to-ladder indexing

Put \(d=2q+1\), number the forward marks by
\[
 F_0=A_0,F_1,\ldots,F_{d-1},\qquad A_h=F_{d-h}\quad(h\ge1),
\]
and define
\[
 P_t=\{C_0,\ldots,C_{q-t-1}\}
       \cup\{A_0,\ldots,A_{t-1}\},
 \qquad B_t=S\cup P_t.
\]
For the transition \(t\to t+1\), let \(r=q-t-1\).  Its common
rank-\((m-1)\) core is
\[
 K_t=S\cup\{C_0,\ldots,C_{r-1}\}
       \cup\{A_0,\ldots,A_{t-1}\}.
\]

The forward one-flip calculation is consistent.  The first \(r\)
\(C\)-flips delete \(F_1,\ldots,F_{2r}\).  The next \(t\)
\(A\)-flips delete
\[
 F_0,F_{d-1},\ldots,F_{d-t+1}
 \quad\hbox{and}\quad
 F_{2r+1},\ldots,F_{2r+t}.
\]
Because \(d=2q+1\) and \(r=q-t-1\), precisely
\[
 U_+(K_t)=\{A_t,A_{t+1},A_{t+2}\}
\]
remain.  The inequality \(x_r\le r\) puts \(C_r\) before the first
surviving forward mark; therefore its strict predecessor in this triple is
\(A_t\).  Reversing the circle gives
\[
 U_-(K_t)=\{C_r,C_{r+1},C_{r+2}\},
\]
with \(C_r\) the strict reverse successor of \(A_t\).  The exact
deficit-three rule then yields
\[
       g(K_t\cup\{C_r\})=K_t\cup\{A_t\}.
\]

The shared-coordinate check is also correct.  If \(C_j=A_h\), the local
order \(C_x,A_x\) gives
\[
       x_j=d-h-1=2q-h,
\]
so \(x_j\le j\) implies \(j+h\ge2q\).  A duplicate inside one
\(P_t\) would require \(j+h\le q-2\), and a coordinate in every
\(P_t\) would require \(j+h\le q-1\).  Both are impossible.  Hence
\(|P_t|=q\) and \(\bigcap_tP_t=\varnothing\), proving
\(\bigcap_tB_t=S\).

For the multiplicity cap, any correct \(q\)-edge path has exactly \(q\)
deletions and its \(q\) initial extras must all disappear.  Thus the
deleted labels are exactly those initial extras.  Reverse unmatched-zero
monotonicity puts them in the \((2q+1)\)-set \(U_-(S)\).  Their
\(q\)-subset determines the initial state, and the forward map \(g\)
then determines the path.  This proves the cap for the single canonical
orientation.  Counting both directions would require saying so separately.

## 3. Five ranks

On a complement-projected step-two cycle let \(X_i\) have rank \(m+1\)
and define
\[
      D_i=X_i\cap X_{i+1}\cap X_{i+2}.
\]
No gap-three return implies every proper positive \(X\)-run has length at
least three.  Coordinatewise erosion and dilation therefore give
\[
\begin{aligned}
D_i&=X_i\cap X_{i+1}\cap X_{i+2},\\
D_i\cup D_{i+1}&=X_{i+1}\cap X_{i+2},\\
D_i\cup D_{i+1}\cup D_{i+2}&=X_{i+2},\\
D_i\cup\cdots\cup D_{i+3}&=X_{i+2}\cup X_{i+3},\\
D_i\cup\cdots\cup D_{i+4}&=X_{i+2}\cup X_{i+3}\cup X_{i+4}.
\end{aligned}
\]
Restoring old PBBS indices identifies these with, respectively, an
opposite-parity first shadow, an exact middle owner, its complement, the
complement of a first shadow, and the complement of a correct second
shadow.  Their ranks are exactly
\(m-1,m,m+1,m+2,m+3\), and the imported first- and second-shadow
theorems give complete support.

The unextended cycle portions have \(W\) letters in total.  Four copied
prefix letters expose every certified window crossing a cycle seam, and
there are at most \(B=W/(2m+1)\) projected cycles.  This proves
\(|Q_2|\le W+4B\).

## 4. Seven ranks and the number 21

For four-fold erosion put
\[
      D_i=X_i\cap X_{i+1}\cap X_{i+2}\cap X_{i+3}.
\]
This is the intersection of three consecutive opposite-parity PBBS
states, so the pointwise depth-two theorem gives \(|D_i|=m-2\).  Thus
the emitted letters are nonzero for \(m\ge3\).

If a coordinate has no positive \(X\)-run of length three, ordinary
four-fold erosion/dilation gives seven target identities, with window
lengths one through seven.  A length-three run is erased from every
\(D_i\).  It spoils no first-line identity (that line merely defines
\(D_i\)), and spoils at most
\[
      1,2,3,4,5,6
\]
windows on the remaining six lines.  The total is exactly the safe upper
bound \(21\).  Appending the intended right-hand-side target for every
spoiled occurrence is therefore a valid literal repair, even when several
short runs spoil the same target.

The PBBS return dictionary identifies positive complement-projected runs
of length three bijectively with consecutive omitted-label returns of gap
five.  For \(m\ge3\), gap five is shorter than the circumference, so the
equality-particle passage argument applies without a wraparound exception.
The defect-one quotient roots are exactly
\[
       (10)^a1(10)^b0,qquad a\ge0,quad b\ge1,quad a+b=m-1.
\]
There are \(m-1\) such roots and \(2m+1\) spatial phases, giving
\((2m+1)(m-1)\) physical starts.  This validates the repair term in the
stated range \(m\ge3\).  (The same formula should not be extrapolated to
the wraparound case \(m=2\); the seven-rank theorem does not do so.)

Six copied prefix letters expose all length-seven atom windows.  The seven
right-hand-side target systems are the lower second, lower first, middle,
upper middle, upper first, upper second, and correct upper third systems.
The all-depth corridor supplies the correct third system; every occurrence
whose erosion identity is spoiled was included in the literal repairs.
Therefore
\[
 |Q_3|\le W+6B+21(2m+1)(m-1)
        =W+O(W/m)
\]
is valid as an asymptotic upper bound.

## 5. Exact scope

The all-depth theorem is a **support** theorem: for every target it finds
at least one rank-correct PBBS window.  It does not assert that all windows
at that depth have the correct rank, and its exponential pointwise cap is
not an aggregate Gaussian-window collision estimate.  The five- and
seven-rank words work because their finite families of wrong erosion
windows can be controlled explicitly.  For growing \(H\), neither the
Catalan short-residence packing estimate nor the linear crossing-mask seam
chart is proved.
