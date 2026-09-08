# Equal three-box surface braids and endpoint obstructions

Date: 2026-07-25

## 0. Verdict

Write

\[
Q_R=[0,R]^3,\qquad
W_R=w_3(R,R,R)
=\left\lceil\frac{3(R+1)^2}{4}\right\rceil,
\]

and

\[
g_3(R,R,R)=W_R+D_R.
\]

A word covers \(T\in Q_R\setminus\{0\}\) when one nonempty contiguous
factor has coordinatewise maximum exactly \(T\). All occurrences and all
witnesses in this report are in this literal sense.

No literal word of length \(W_R+o(R^2)\) was found here. The best explicit
unrestricted construction remains the reset-free triangular-shell word

\[
|{\cal T}_R|
=\frac{3R(R+1)}2+R-1
=2W_R-\left\lfloor\frac R2\right\rfloor-3
\qquad(R\ge2).
\tag{0.1}
\]

The new work gives four exact conclusions.

1. **Architecture-free endpoint obstruction.**

   \[
   \boxed{
   D_R\ge\left(\frac23-o(1)\right)R.
   }
   \tag{0.2}
   \]

   Exact parity formulas appear in Theorem 3.1. This is the strongest
   unrestricted conclusion obtained here, but it is only linear and does
   not disprove \(D_R=o(R^2)\).

2. **The existing rank-band endpoint dual is exhausted.** Every
   consecutive-rank-band certificate using the two endpoint partitions,
   one coordinate-cover capacity, and an arbitrary positive transverse
   linear potential gives at most

   \[
   \boxed{
   272\,\frac{(R+1)^2}{R}+1=O(R)
   }
   \tag{0.3}
   \]

   excess. Its limiting cubic coefficient is strictly negative for every
   macroscopically thick band and vanishes only at the collapsed middle
   scale \(A/R,B/R\to3/2\). A quadratic cube obstruction needs a
   nonlinear potential, a nonconsecutive or non-rank target region, or a
   new coupling of the endpoint orders.

3. **All-positive and two-coordinate-positive recursion fail at
   coefficient one.** If a recursive word retains an
   occurrence-for-occurrence copy of a previous word shifted into
   \([1,R-1]^3\), then at least \(4R\) new occurrences are forced, whereas

   \[
   W_R-W_{R-2}=3R.
   \]

   Iteration gives excess \((1/4+o(1))R^2\).

   A two-coordinate-positive lift also fails. The exact minimum word for
   the union of its two excluded zero faces is

   \[
   4R-1,
   \]

   attained by a doubled-axis corridor. It gives the same
   \((1/4+o(1))R^2\) recursive excess. Thus only a one-coordinate-positive
   lift, preserving zero in two fixed coordinates, survives this
   obstruction.

4. **One- and two-shell confined recursion is impossible.** A contiguous
   module internally covering the outer \(k\) max shells has length at
   least

   \[
   L_k(t)=
   \left\lceil
   \frac{\sqrt{1+8((t+1)^3-(t-k+1)^3)}-1}{2}
   \right\rceil.
   \tag{0.4}
   \]

   For \(k=1,2\), this exceeds the width increment at leading order.
   Three shells are the first fixed window not excluded by interval
   counting. A second, independent nested-pivot theorem rules out the
   natural shared-arm two-shell surface braid with excess
   \((1/2+o(1))R^2\).

Thus the explicit construction problem remains open. The surviving
construction routes are:

- a three-or-more-shell module with cross-window witnesses;
- an asymmetric lift preserving zero in at least two fixed coordinates;
  or
- a genuinely global braid with positive-density degree-three or
  high-multiplicity arm reuse.

No reduction to another theorem is repeated here. Every positive word and
every obstruction below is literal and integral.

---

## 1. Exact width and the explicit benchmark word

The equal-cube width is

\[
W_R=
\begin{cases}
3s^2+3s+1,&R=2s,\\[1mm]
3(s+1)^2,&R=2s+1.
\end{cases}
\tag{1.1}
\]

Indeed, if \(m_k\) denotes the rank-\(k\) coefficient of
\((1+x+\cdots+x^R)^3\), with \(m_{-1}=0\), then, up to the middle rank,

\[
m_k-m_{k-1}=
\begin{cases}
k+1,&0\le k\le R,\\
3R-2k+1,&R<k\le\lceil3R/2\rceil.
\end{cases}
\tag{1.1a}
\]

This follows by taking first differences in the one-term
inclusion--exclusion formula

\[
m_k=\binom{k+2}{2}
-3\binom{k-R+1}{2}
\qquad(R<k<2R+2),
\]

with the second term omitted for \(k\le R\). Rank symmetry and (1.1a)
locate the maximum at rank \(3s\) for \(R=2s\), and at the two ranks
\(3s+1,3s+2\) for \(R=2s+1\). Substitution gives (1.1).

For completeness, a product of chains has a symmetric-chain
decomposition. Inductively, take one old symmetric chain at a time and
decompose its product with the new chain by the successive boundary
chains of the resulting rectangle. Every resulting chain is symmetric
about the middle rank of the full product. Hence the width equals the
largest rank size, proving the claimed identity for \(W_R\).

### Theorem 1.1 (triangular-shell word)

For \(t\ge1\), put

\[
A_t=(t,0,0),\qquad B_t=(0,t,0),\qquad C_t=(0,0,t),
\]

and define

\[
\begin{split}
{\cal C}_t={}&
(t,0,0),(t-1,1,0),\ldots,(0,t,0),\\
&(0,t-1,1),\ldots,(0,0,t),\\
&(1,0,t-1),\ldots,(t,0,0).
\end{split}
\tag{1.2}
\]

For \(R\ge2\), concatenate \({\cal C}_1,\ldots,{\cal C}_R\) and replace the
first block by

\[
B_1,C_1,A_1.
\tag{1.3}
\]

The resulting word \({\cal T}_R\) covers every nonzero target of \(Q_R\)
and has the length in (0.1).

#### Literal witnesses

Take \(T=(x,y,z)\ne0\), put \(t=\max(x,y,z)\), and break ties in the
following order. If \(t=1\), check the shortened block directly: its six
nonempty interval maxima are

\[
(0,1,0),(0,0,1),(1,0,0),(0,1,1),(1,0,1),(1,1,1).
\]

The remaining max-one target \((1,1,0)\) is the singleton displayed in
\({\cal C}_2\). Hence assume \(t\ge2\).

- If \(y=t\), use

  \[
  [(x,t-x,0),\ldots,B_t,\ldots,(0,t-z,z)].
  \tag{1.4}
  \]

  Its maximum is exactly \((x,t,z)\).

- If \(y<t\) and \(z=t\), use

  \[
  [(0,y,t-y),\ldots,C_t,\ldots,(x,0,t-x)].
  \tag{1.5}
  \]

  Its maximum is exactly \((x,y,t)\).

- Otherwise \(x=t\) and \(y,z<t\). For \(t\ge2\), begin in the final side
  of \({\cal C}_{t-1}\) at

  \[
  (t-1-z,0,z),
  \]

  cross the seam from the terminal \(A_{t-1}\) to the initial \(A_t\),
  and end at

  \[
  (t-y,y,0).
  \tag{1.6}
  \]

  This interval has maximum exactly \((t,y,z)\).

\[
|{\cal T}_R|
=3+\sum_{t=2}^R(3t+1)
=\frac{3R(R+1)}2+R-1.
\]

\(\square\)

No new unrestricted word found here improves the leading coefficient
\(3/2\) in (0.1). The remaining sections explain why the most direct
surface and recursive modifications fail.

---

## 2. Endpoint queue for a middle antichain

The next lemma is independent of every shell order.

### Lemma 2.1 (ordered middle endpoints)

Let a word of length \(N\) represent \(M\) distinct targets in one rank.
Choose one witness

\[
I_i=[\ell_i,r_i]
\]

for each target and order them by increasing left endpoint. Then both
endpoint orders are strict and identical. Writing \(E=N-M\),

\[
\ell_i=i+\alpha_i,\qquad r_i=i+\beta_i,
\tag{2.1}
\]

where

\[
0\le\alpha_1\le\cdots\le\alpha_M\le E,
\]

\[
0\le\beta_1\le\cdots\le\beta_M\le E,
\qquad \beta_i\ge\alpha_i.
\tag{2.2}
\]

In particular every middle witness has span

\[
d_i=r_i-\ell_i=\beta_i-\alpha_i\le E.
\tag{2.3}
\]

#### Proof

Equal left endpoints would make the two intervals nested, hence their
distinct equal-rank maxima comparable. If
\(\ell_i<\ell_j\) but \(r_i\ge r_j\), then
\(I_j\subseteq I_i\), giving the same contradiction. Thus both endpoint
sequences are strictly increasing. An increasing \(M\)-tuple in
\(\{1,\ldots,M+E\}\) has the form (2.1)--(2.2). \(\square\)

### Lemma 2.2 (rank-capped starts)

Let the selected rank be \(h\), and let \(L_{<h}\) be the number of
nonzero targets of ranks below \(h\). Then

\[
\boxed{
L_{<h}\le(M+h-1)(N-M).
}
\tag{2.4}
\]

#### Proof

Choose one witness for every lower target and group these witnesses by
their physical left endpoint.

At a selected start \(\ell_i\), a lower witness must end before \(r_i\).
Otherwise it contains \(I_i\), and its maximum dominates the rank-\(h\)
target. There are at most \(d_i\) possible endpoints.

There are exactly \(E=N-M\) unselected starts. At one fixed start,
maxima obtained by increasing the right endpoint form a chain. A strict
chain of nonzero targets below rank \(h\) has at most \(h-1\) members.
Therefore

\[
L_{<h}
\le\sum_{i=1}^M d_i+(h-1)E
\le(M+h-1)E.
\]

\(\square\)

---

## 3. New architecture-free equal-cube obstruction

### Theorem 3.1 (exact middle-endpoint lower bound)

For \(R=2s\), \(s\ge1\),

\[
\boxed{
D_{2s}\ge
\left\lceil
\frac{8s^3+9s^2+3s-2}
{6s^2+12s}
\right\rceil.
}
\tag{3.1}
\]

For \(R=2s+1\), \(s\ge0\),

\[
\boxed{
D_{2s+1}\ge
\left\lceil
\frac{4(s+1)^3-1}
{3s^2+9s+4}
\right\rceil.
}
\tag{3.2}
\]

Consequently,

\[
\boxed{
D_R\ge\left(\frac23-o(1)\right)R.
}
\tag{3.3}
\]

#### Proof

Suppose first \(R=2s\). The unique middle rank is \(h=3s\), of size

\[
M=W_R=3s^2+3s+1.
\]

Rank symmetry gives the exact number of nonzero targets below it:

\[
\begin{split}
L_{<h}
&=\frac{(2s+1)^3-W_R}{2}-1\\
&=\frac{8s^3+9s^2+3s-2}{2}.
\end{split}
\tag{3.4}
\]

Since

\[
M+h-1=3s^2+6s,
\]

Lemma 2.2 gives (3.1).

Now let \(R=2s+1\). The two middle layers have ranks \(3s+1,3s+2\)
and common size

\[
M=W_R=3(s+1)^2.
\]

Choose the upper middle layer, \(h=3s+2\). Exactly half of the cube lies
strictly below it, including its lower middle partner. After deleting the
global zero,

\[
L_{<h}=4(s+1)^3-1.
\tag{3.5}
\]

Moreover

\[
M+h-1=3s^2+9s+4.
\]

Lemma 2.2 proves (3.2). The leading terms in (3.1)--(3.2) give (3.3).
\(\square\)

This is architecture-free, but it remains compatible with
\(D_R=o(R^2)\). The trivial span estimate \(d_i\le D_R\) is sharp for an
abstract endpoint queue, so a quadratic obstruction must use additional
literal geometry.

### Corollary 3.2 (exact endpoint-rigidity slack)

For any universal word of length \(W_R+D\), use the middle layer chosen
in Theorem 3.1 and write

\[
\Delta_R(D)=(M+h-1)D-L_{<h}.
\tag{3.6}
\]

For the endpoint coordinates in Lemma 2.1,

\[
\boxed{
\sum_{i=1}^{M}\bigl(\alpha_i+D-\beta_i\bigr)
\le \Delta_R(D).
}
\tag{3.7}
\]

Consequently, for every real \(u>0\),

\[
\boxed{
\#\{i:\alpha_i\ge u\}
+\#\{i:\beta_i\le D-u\}
\le\frac{\Delta_R(D)}{u}.
}
\tag{3.8}
\]

In particular, if

\[
D_R=\left(\frac23+o(1)\right)R,
\]

then, for every fixed \(\varepsilon>0\), all but \(o(W_R)\) selected
middle witnesses satisfy

\[
\alpha_i<\varepsilon R,\qquad
\beta_i>D_R-\varepsilon R,\qquad
d_i>D_R-2\varepsilon R.
\tag{3.9}
\]

#### Proof

The proof of Lemma 2.2 gives the stronger intermediate inequality

\[
\sum_i d_i\ge L_{<h}-(h-1)D.
\]

Since \(d_i=\beta_i-\alpha_i\),

\[
\sum_i(\alpha_i+D-\beta_i)
=MD-\sum_i d_i
\le(M+h-1)D-L_{<h}.
\]

This is (3.7), and Markov counting gives (3.8). Under the preceding
hypothesis \(D_R=(2/3+o(1))R\), the exact parity formulas in Theorem 3.1
give
\(\Delta_R(D_R)=o(R^3)\). Take \(u=\varepsilon R\) in (3.8), use
\(W_R=\Theta(R^2)\), and then use
\(d_i=\beta_i-\alpha_i\). \(\square\)

Thus a word attaining the linear endpoint bound is forced into an almost
translated endpoint queue: almost every middle interval starts within
\(o(R)\) of its earliest possible slot and ends within \(o(R)\) of its
latest one. This rigidity is still insufficient by itself to contradict
literal cube maxima.

---

## 4. Exact weighted rank-band endpoint dual

The preceding theorem uses only one maximum layer. We next audit the full
consecutive-band endpoint-potential mechanism.

Fix

\[
1\le A\le B\le3R.
\]

Let \(L_t\) be rank \(t\) of \(Q_R\), put

\[
m_t=|L_t|,\qquad
T_{A,B}=\sum_{t=A}^B m_t,
\tag{4.1}
\]

and let

\[
K_{A,B}
=\#\{(x,y)\in[0,R]^2:
[x+y,x+y+R]\cap[A,B]\ne\varnothing\}.
\tag{4.2}
\]

Every vertical \(z\)-column meets the band in an interval, so the exact
number of vertical cover edges inside the band is

\[
T_{A,B}-K_{A,B}.
\tag{4.3}
\]

Take a positive transverse linear potential

\[
\phi(x,y,z)=\alpha x+\beta y.
\]

After dividing by \(\min(\alpha,\beta)\), assume

\[
\min(\alpha,\beta)=1,\qquad c=\alpha+\beta\ge2.
\tag{4.4}
\]

Coordinate symmetry on each rank gives

\[
\sum_{X\in L_t}\phi(X)=\frac{ct}{3}m_t.
\tag{4.5}
\]

### Theorem 4.1 (exact weighted band certificate)

Every universal word of length \(W_R+D\) satisfies

\[
\boxed{
2(B-A+cR)D\ge{\cal N}_c(A,B),
}
\tag{4.6}
\]

where

\[
\boxed{
\begin{split}
{\cal N}_c(A,B)
={}&3T_{A,B}+K_{A,B}-2m_A+2(cR-1)m_B\\
&+\frac{2c}{3}(A m_A-Bm_B)
-2(B-A+cR)W_R.
\end{split}
}
\tag{4.7}
\]

Thus this band and potential certify the lower bound

\[
D\ge E_c(A,B),
\]

where

\[
E_c(A,B)=
\max\left\{
0,\
\left\lceil
\frac{{\cal N}_c(A,B)}{2(B-A+cR)}
\right\rceil
\right\}.
\tag{4.8}
\]

#### Proof

Choose one witness for every target in the band and partition the targets
by common left endpoint and, independently, by common right endpoint.
Every class is a target chain, and each partition has at most \(W_R+D\)
classes.

Consider one endpoint partition with \(C\) classes and put \(J=B-A\).
Between ranks \(t,t+1\), at least

\[
m_t+m_{t+1}-C
\]

classes meet both layers. Such a class uses a genuine cover edge. Summing
over all transitions, the partition uses at least

\[
2T_{A,B}-m_A-m_B-JC
\tag{4.9}
\]

band covers.

Every nonvertical cover raises \(\phi\) by at least \(1\). Exactly \(m_A\)
chains begin at the bottom boundary and \(m_B\) chains end at the top
boundary.
Internal starts have nonnegative potential and each internal end has
potential at most \(cR\). Telescoping \(\phi\) therefore bounds the number
of nonvertical covers in (4.9) by

\[
\frac{cB}{3}m_B-\frac{cA}{3}m_A+cR(C-m_B).
\tag{4.10}
\]

Consequently this endpoint partition uses at least

\[
\begin{split}
2T_{A,B}-m_A+(cR-1)m_B
+\frac c3(A m_A-Bm_B)
-(J+cR)C
\end{split}
\tag{4.11}
\]

vertical covers.

A vertical edge cannot occur in both endpoint partitions. Otherwise its
two targets would lie in one common left class and one common right class,
forcing two different maxima to have the same physical interval.

Apply (4.11) to both partitions, use

\[
C_L+C_R\le2(W_R+D),
\]

and compare their combined demand with the exact capacity (4.3).
Rearrangement gives (4.6)--(4.7). \(\square\)

---

## 5. The positive-linear rank-band dual cannot be quadratic

Theorem 4.1 is exact, but its entire certificate family is asymptotically
silent at quadratic scale.

### Theorem 5.1 (finite uniform ceiling)

For every

\[
R\ge1,\qquad1\le A\le B\le3R,\qquad c\ge2,
\]

\[
\boxed{
{\cal N}_c(A,B)\le(144c+800)(R+1)^2.
}
\tag{5.1}
\]

Consequently

\[
\boxed{
E_c(A,B)
\le
\left\lceil
272\,\frac{(R+1)^2}{R}
\right\rceil.
}
\tag{5.2}
\]

The bound is uniform even when the potential coefficients depend on
\(R\).

#### Proof

Put

\[
C=3R-B,\qquad A+C\le3R,
\]

and define

\[
q_R(k)=\sum_{t<k}m_t.
\]

Rank complementation gives

\[
T_{A,B}=(R+1)^3-q_R(A)-q_R(C),\qquad m_B=m_C.
\tag{5.3}
\]

Define

\[
H_{c,R}(k)
=-3q_R(k)
+\left(\frac{2ck}{3}-2\right)m_k
+2kW_R.
\tag{5.4}
\]

Substitution in (4.7) gives the exact identity

\[
\boxed{
{\cal N}_c(A,B)
=3(R+1)^3-2(c+3)RW_R+K_{A,B}
+H_{c,R}(A)+H_{c,R}(C).
}
\tag{5.5}
\]

For \(0\le x\le3\), put

\[
f(x)=
\frac12\sum_{j=0}^3(-1)^j\binom3j(x-j)_+^2,
\]

\[
F(x)=
\frac16\sum_{j=0}^3(-1)^j\binom3j(x-j)_+^3,
\tag{5.6}
\]

and

\[
h_c(x)
=-3F(x)+\frac{2c}{3}x f(x)+\frac32x.
\tag{5.7}
\]

The continuous cube rank density satisfies

\[
0\le f(x)\le\frac34.
\tag{5.8}
\]

The exact inclusion-exclusion formulas are

\[
m_k
=\sum_{j=0}^3(-1)^j\binom3j
B_2(k-j(R+1)),
\]

\[
q_R(k)
=\sum_{j=0}^3(-1)^j\binom3j
B_3(k-j(R+1)),
\tag{5.9}
\]

where

\[
B_2(n)=
\begin{cases}
\binom{n+2}{2},&n\ge0,\\
0,&n<0,
\end{cases}
\]

\[
B_3(n)=
\begin{cases}
\binom{n+2}{3},&n\ge1,\\
0,&n\le0.
\end{cases}
\]

For \(y=k-jR\), direct expansion gives

\[
\left|
B_2(y-j)-\frac12(y_+)^2
\right|
\le\frac92(R+1),
\]

\[
\left|
B_3(y-j)-\frac16(y_+)^3
\right|
\le16(R+1)^2.
\tag{5.10}
\]

Here the constants are literal. When \(y-j\ge0\),

\[
B_2(y-j)-\frac{y^2}{2}
=\frac{3-2j}{2}y+\frac{j^2-3j+2}{2};
\]

for \(0\le j\le3\), the two coefficients have absolute values at most
\(3/2\) and \(1\). In the active range \(0\le y\le3R\), this is at most
\((9/2)R+1\), and the finitely truncated cases \(0<y<j\), or \(y\le0\),
are smaller. Similarly,

\[
\begin{split}
6B_3(y-j)-y^3
={}&3(1-j)y^2+(3j^2-6j+2)y\\
&{}-j^3+3j^2-2j
\end{split}
\]

whenever \(y-j\ge1\). The three displayed coefficients have absolute
values at most \(6,11,6\); with \(0\le y\le3R\), the result is at most
\(9R^2+(11/2)R+1\), below \(16(R+1)^2\). The truncated cases again have
\(0<y\le3\). This proves (5.10) without an asymptotic convention.

Summing the eight inclusion-exclusion coefficients yields

\[
\boxed{
|m_k-R^2f(k/R)|\le36(R+1),
}
\]

\[
\boxed{
|q_R(k)-R^3F(k/R)|\le128(R+1)^2.
}
\tag{5.11}
\]

Also

\[
0\le W_R-\frac34R^2\le\frac32(R+1).
\tag{5.12}
\]

Equations (5.11)--(5.12), \(k\le3R\), and
\(m_k\le(R+1)^2\) imply

\[
\boxed{
\left|
H_{c,R}(k)-R^3h_c(k/R)
\right|
\le(72c+395)(R+1)^2.
}
\tag{5.13}
\]

It remains to control the cubic term. For \(c=2\), the affine function

\[
\ell_2(x)=\frac x4+\frac{15}{8}
\]

majorizes \(h_2(x)\) on \([0,3]\). On the three polynomial pieces the
differences are

\[
\ell_2-h_2
=\frac{15}{8}-\frac54x-\frac16x^3
\qquad(0\le x\le1),
\]

\[
\ell_2-h_2
=\frac{(2x-3)^2(2x+9)}{24}
\qquad(1\le x\le2),
\tag{5.14}
\]

and, with \(t=3-x\),

\[
\ell_2-h_2
=\frac98+\frac54t-2t^2+\frac16t^3
\qquad(0\le t\le1).
\]

These are nonnegative, with equality only at \(x=3/2\). For \(c\ge2\),
(5.8) gives

\[
h_c(x)
=h_2(x)+\frac{2(c-2)}3x f(x)
\le
\left(\frac c2-\frac34\right)x+\frac{15}{8}.
\tag{5.15}
\]

For clarity, on the first interval the first difference in (5.14) is
strictly decreasing and has endpoint value \(11/24\). On the last
interval its derivative changes from positive to negative at most once,
so its minimum is at an endpoint; those values are \(9/8\) and \(13/24\).
The middle factorization is manifestly nonnegative. Also

\[
f(x)=
\begin{cases}
x^2/2,&0\le x\le1,\\
-x^2+3x-3/2,&1\le x\le2,
\end{cases}
\]

with the third piece obtained by symmetry, proving \(f\le3/4\) and hence
(5.15).

Because \(A+C\le3R\),

\[
R^3h_c(A/R)+R^3h_c(C/R)
\le\frac32(c+1)R^3.
\tag{5.16}
\]

Finally,

\[
3(R+1)^3-2(c+3)RW_R
\le-\frac32(c+1)R^3+9R^2+9R+3,
\]

and \(K_{A,B}\le(R+1)^2\). Substitute (5.13) and (5.16) into
(5.5). The cubic terms cancel and give

\[
{\cal N}_c(A,B)
\le
2(72c+395)(R+1)^2
+10(R+1)^2,
\]

which is (5.1). Since

\[
2(B-A+cR)\ge2cR
\]

and

\[
\frac{144c+800}{2c}
=72+\frac{400}{c}\le272,
\]

(5.2) follows. \(\square\)

### 5.2 Sharp asymptotic diagnosis

For fixed \(c\), if

\[
\frac AR\to a,\qquad\frac BR\to b,
\]

then

\[
\lim_{R\to\infty}\frac{{\cal N}_c(A,B)}{R^3}
=h_c(a)+h_c(3-b)-\frac32(c+1)\le0.
\tag{5.17}
\]

Equality occurs only at

\[
a=b=\frac32,
\]

the collapsed middle band. Every genuinely macroscopic band has a
strictly negative cubic numerator.

The scope is exact. This eliminates only the two endpoint partitions,
one coordinate-edge capacity, consecutive rank bands, and positive
transverse linear potentials. It does not eliminate nonlinear potentials,
nonconsecutive or non-rank target regions, or constraints coupling the
two endpoint orders beyond cover-edge exclusion.

---

## 6. Central recursive shelling has an exact support toll

The following obstruction does not assume that old witnesses survive an
insertion step.

### Lemma 6.1 (proper-support OR word)

Let a finite word over the nonempty subsets of \(\{1,2,3\}\) have every
nonempty proper subset as the union of a contiguous factor. Then its
length is at least \(4\). This is sharp.

#### Proof

The three singleton targets force occurrences labelled
\(\{1\},\{2\},\{3\}\). If these were the only three positions, only the
two adjacent singleton pairs could occur as two-letter unions. The
interval joining the nonadjacent singleton labels has union
\(\{1,2,3\}\), so one two-element target is missing.

The word

\[
\{1\},\{2\},\{3\},\{1\}
\]

covers all three singletons and all three two-element subsets. \(\square\)

### Theorem 6.2 (all-positive core toll)

Let a literal universal word for \(Q_R\) have its occurrences partitioned
into a distinguished core \({\cal C}\) and an off-core set \({\cal E}\).
Assume every core letter is strictly positive in all three coordinates.
Then

\[
\boxed{|{\cal E}|\ge4R.}
\tag{6.1}
\]

#### Proof

For \(1\le h\le R\), let \({\cal E}_h\) be the off-core occurrences of
height

\[
\|v\|_\infty=h
\]

in inherited word order. Label such an occurrence by

\[
\sigma_h(v)=\{j:v_j=h\},
\tag{6.2}
\]

a nonempty subset of \(\{1,2,3\}\).

Fix a nonempty proper subset \(S\) and the target

\[
T_{h,S}=h\,{\bf1}_S.
\tag{6.3}
\]

Every letter in a witness for \(T_{h,S}\) has coordinate zero outside
\(S\). Since \(S\) is proper, no all-positive core letter lies in that
witness.

Retain from the witness only its height-\(h\) occurrences. They form a
nonempty contiguous factor of \({\cal E}_h\): every height-\(h\)
off-core occurrence physically between the first and last retained
positions was also in the original interval. Their \(\sigma_h\)-label
union is exactly \(S\). It is contained in \(S\) because every witness
letter is at most \(T_{h,S}\), and it contains \(S\) because every target
coordinate equal to \(h\) must be attained.

Lemma 6.1 gives \(|{\cal E}_h|\ge4\). The height classes are disjoint, so
\(|{\cal E}|\ge4R\). \(\square\)

### Corollary 6.3 (central two-level recursion no-go)

Suppose a recursive word at scale \(R\) retains, as a distinguished
subsequence, an occurrence-for-occurrence copy of the previous
\([0,R-2]^3\) word shifted by \((1,1,1)\), and all other occurrences are
new. Then

\[
\boxed{N_R\ge N_{R-2}+4R.}
\tag{6.4}
\]

No preservation of the old selected witnesses is assumed.

The exact width increment is

\[
\boxed{W_R-W_{R-2}=3R.}
\tag{6.5}
\]

Taking \(N_0=0\) and \(N_1\ge4\), iteration gives

\[
\boxed{
N_{2s}\ge4s(s+1)=R^2+2R,
}
\tag{6.6}
\]

\[
\boxed{
N_{2s+1}\ge4(s+1)^2=(R+1)^2.
}
\tag{6.7}
\]

Consequently,

\[
N_{2s}-W_{2s}
\ge s^2+s-1
=\frac{R^2}{4}+\frac R2-1,
\tag{6.8}
\]

\[
N_{2s+1}-W_{2s+1}
\ge(s+1)^2
=\frac{(R+1)^2}{4}.
\tag{6.9}
\]

This central recursion has asymptotic ratio at least \(4/3\).

#### Proof

The shifted old letters form an all-positive core, so Theorem 6.2 gives
(6.4). The width formulas (1.1) give (6.5), and summing the recurrence
gives (6.6)--(6.9). No additional \(+1\) for the translated local origin
follows from this support argument.
\(\square\)

### 6.4 Exact asymmetric escape

Suppose every core letter is strictly positive in every coordinate of a
fixed nonempty set \(J\subseteq\{1,2,3\}\), with no restriction on its
other coordinates. The same proof uses targets \(S\) with
\(J\nsubseteq S\). The exact support-word toll per height is

\[
\mu(J)=|J|+1.
\tag{6.10}
\]

For \(|J|=1\), a two-letter word on the other two singleton labels is
sharp. For \(J=\{1,2\}\), the word

\[
\{1\},\{3\},\{2\}
\]

is sharp for

\[
\{1\},\{2\},\{3\},\{1,3\},\{2,3\}.
\]

For \(|J|=3\), Lemma 6.1 applies. Thus a two-coordinate-positive lift has
support toll \(3R\), exactly the width increment (6.5). The lower bounds
are sharp at the support-word level: singleton targets give the matching
lower bounds for \(|J|=1,2\), and the displayed words attain them.

Literal values impose one more constraint. For \(J=\{1,2\}\), equality
at a fixed height forces the three labels, in inherited order, to be

\[
\{1\},\{3\},\{2\}
\quad\hbox{or}\quad
\{2\},\{3\},\{1\}.
\tag{6.11}
\]

Indeed the three singleton targets force the three singleton labels, and
the targets \(\{1,3\}\), \(\{2,3\}\) force \(\{3\}\) to lie between the
other two. Thus the support projection alone says that an all-positive
lift must preserve zero somewhere, and a two-coordinate-positive lift
must realize the deterministic corridor order (6.11) on every
support-saturated height. The exact two-face theorem in Section 8
strengthens this: even that two-coordinate lift costs \(4R-1\) per step.
The surviving recursive pattern may be positive in at most one fixed
coordinate.

### Lemma 6.5 (literal structure at support saturation)

Assume every core occurrence is positive in coordinates \(1,2\), and
there are exactly \(3R\) off-core occurrences. Then, for every
\(1\le h\le R\), the three height-\(h\) off-core letters are exactly

\[
h e_1,\qquad h e_3,\qquad h e_2
\]

in one of the two inherited orders in (6.11). Moreover, the three
occurrences lie in one common component of the word after all core
occurrences are deleted.

#### Proof

The support proof gives at least three off-core occurrences at every
height. Equality in the total therefore gives exactly three at every
height, and (6.11) gives their labels. A witness of the singleton target
\(h e_j\) must contain the exact letter \(h e_j\). Since the corresponding
height-\(h\) label is unique, the three letters are the asserted pure
axis pins.

The witness of \(h(e_1+e_3)\) contains the \(e_1,e_3\) pins and no core
occurrence, because every core letter is positive in coordinate \(2\).
Likewise the witness of \(h(e_2+e_3)\) joins the \(e_2,e_3\) pins while
avoiding the core. Hence no core occurrence separates either adjacent
pair in (6.11), and all three pins lie in one core-free component.
\(\square\)

---

## 7. Confined shell modules: interval-count obstruction

For \(t\ge k\ge1\), define the outer \(k\) max shells

\[
{\cal S}_{t,k}
=[0,t]^3\setminus[0,t-k]^3.
\tag{7.1}
\]

Their exact target count is

\[
A_k(t)=|{\cal S}_{t,k}|
=(t+1)^3-(t-k+1)^3.
\tag{7.2}
\]

### Theorem 7.1 (module interval count)

If one contiguous word module of length \(n\) internally witnesses every
target in \({\cal S}_{t,k}\), then

\[
\boxed{
n\ge
L_k(t):=
\left\lceil
\frac{\sqrt{1+8A_k(t)}-1}{2}
\right\rceil.
}
\tag{7.3}
\]

#### Proof

Select one internal interval for every target. Different targets require
different intervals because one interval has one coordinatewise maximum.
A word of length \(n\) has exactly \(n(n+1)/2\) nonempty intervals.
Therefore

\[
\frac{n(n+1)}2\ge A_k(t),
\]

which is equivalent to (7.3). \(\square\)

For one shell,

\[
A_1(t)=3t^2+3t+1,
\qquad
L_1(t)=(\sqrt6+o(1))t.
\tag{7.4}
\]

Separately confined one-shell modules consequently have total length

\[
\left(\frac{\sqrt6}{2}+o(1)\right)R^2,
\]

strictly exceeding \(W_R=(3/4+o(1))R^2\).

For two shells,

\[
A_2(t)=6t^2+2,
\]

\[
\boxed{
L_2(t)
=\left\lceil
\frac{\sqrt{48t^2+17}-1}{2}
\right\rceil
=(\sqrt{12}+o(1))t.
}
\tag{7.5}
\]

The exact width identity

\[
W_t-W_{t-2}=3t
\tag{7.6}
\]

has a precise portal-ledger consequence. In a **two-shell width-ledger
architecture**, require for each even \(t\) a contiguous hull \(H_t\)
inside which all selected witnesses for \({\cal S}_{t,2}\) lie, and
designate at most \(3t\) positions of \(H_t\) as the native allocation
for that pair. Count every other position of \(H_t\) as one foreign
incidence for that pair. Theorem 7.1 then gives at least

\[
L_2(t)-3t
=(\sqrt{12}-3)t+O(1)
\tag{7.7}
\]

foreign portal positions into its contiguous witness hull.

For \(R=2s\), summing over \(t=2,4,\ldots,2s\) gives the quadratic
portal-incidence requirement

\[
\boxed{
\sum_{j=1}^s\bigl(L_2(2j)-6j\bigr)
=\left(\frac{\sqrt{12}-3}{4}+o(1)\right)R^2.
}
\tag{7.8}
\]

This is an incidence statement, not necessarily quadratic physical
support: the same physical position may be foreign in many hulls. If the
native allocations total \(W_R+o(R^2)\) instead of obeying the
pair-by-pair cap \(3t\), the right side of (7.8) loses only \(o(R^2)\).
Without a declared native allocation and witness hull, (7.7)--(7.8) make
no claim about an arbitrary global word.

For fixed \(k\),

\[
L_k(t)=(\sqrt{6k}+o(1))t,
\tag{7.9}
\]

whereas the \(k\)-level width increment is

\[
\left(\frac{3k}{2}+o(1)\right)t.
\]

The interval count exceeds the width ledger exactly for \(k=1,2\).
Three shells are the first fixed local window not excluded:

\[
\frac{\sqrt{18}}{3}=\sqrt2<\frac32.
\tag{7.10}
\]

Thus, within fixed-window confined or width-ledger recursion, a
construction must use at least three-shell windows or permit quadratic
cross-window portal incidence.

---

## 8. Literal corridor and arm-duplication obstructions

The interval count does not see which side of a portal supplies a
coordinate. The next results do.

### Theorem 8.1 (opposed common-root corridor)

Let a universal word for \(Q_R\) have a distinguished core whose letters
are positive in coordinates \(1,2\), and let \({\cal E}\) be the set of
all other occurrences. Designate one occurrence

\[
X_R=(R,0,0),\qquad Y_R=(0,R,0).
\]

Assume that, for every \(1\le z\le R\),

- a selected witness of \((R,0,z)\) contains the same designated
  occurrence \(X_R\); and
- a selected witness of \((0,R,z)\) contains the same designated
  occurrence \(Y_R\).

Then

\[
\boxed{|{\cal E}|\ge4R-1.}
\tag{8.1}
\]

#### Proof

The \(2R\) axis targets

\[
(i,0,0),\quad(0,i,0)\qquad(1\le i\le R)
\]

force \(2R\) distinct pure axis-pin occurrences. They are off-core.

For every \(z\), choose from the first selected witness an occurrence
\(P_z\) whose third coordinate is exactly \(z\), and from the second an
occurrence \(Q_z\) with third coordinate \(z\). The \(P_z\)'s are
distinct, as are the \(Q_z\)'s. They are off-core and are distinct from
the \(2R\) axis pins because their third coordinate is positive.

It remains to show

\[
|\{P_z\}\cap\{Q_z\}|\le1.
\tag{8.2}
\]

Suppose in physical word order that \(X_R<Y_R\). A common provider must
lie strictly between them: if it were to the right of \(Y_R\), the
\((R,0,z)\)-witness would contain \(Y_R\), and if it were to the left of
\(X_R\), the \((0,R,z)\)-witness would contain \(X_R\).

Now suppose two common providers have third coordinates \(z<w\). The
\((R,0,z)\)-interval forces the \(z\)-provider to occur before the
\(w\)-provider; otherwise the latter lies between \(X_R\) and the former
and raises the third maximum above \(z\). But the
\((0,R,z)\)-interval forces the reverse order, since it runs from its
provider toward \(Y_R\). This is impossible. The case \(Y_R<X_R\) is
symmetric. Hence (8.2) holds, and the exact count is

\[
2R+(R+R-1)=4R-1.
\]

\(\square\)

The common-root hypothesis is substantial: a target-dependent mixed
letter \((R,0,z')\) can replace the pure root in some witnesses. The
theorem is therefore a corridor obstruction, not an unrestricted
four-\(R\) toll.

### Theorem 8.2 (root-portal product tradeoff)

Let a word, not necessarily universal outside the listed targets, have a
distinguished core positive in coordinates \(1,2\), with off-core set
\({\cal E}\). Assume it covers all \(2R\) nonzero \(x\)- and \(y\)-axis
targets. Fix arbitrary \(1\le r,s\le R\) and assume it also covers
\((r,0,z)\), \((0,s,z)\) for every \(1\le z\le R\). Select one witness
of each \((r,0,z)\), designate within it an \(x\)-root occurrence
\(X_z^{(r)}\) whose first coordinate is \(r\), and designate a
\(z\)-provider \(P_z^{(r)}\) whose third coordinate is \(z\). Do the
same for \((0,s,z)\), obtaining a \(y\)-root \(Y_z^{(s)}\) and provider
\(Q_z^{(s)}\). Put

\[
a_r=\#\{X_z^{(r)}:1\le z\le R\},\qquad
b_s=\#\{Y_z^{(s)}:1\le z\le R\},
\tag{8.3}
\]

where the braces count distinct physical occurrences. Then

\[
\boxed{|{\cal E}|\ge4R-a_rb_s.}
\tag{8.4}
\]

In particular, if

\[
|{\cal E}|\le3R+e,
\]

then

\[
\boxed{a_rb_s\ge R-e.}
\tag{8.5}
\]

Thus a two-face corridor with \(|{\cal E}|=3R+o(R)\) would have to use,
for every row pair \(r,s\), at least
\((1-o(1))\sqrt R\) distinct row-root portals on one of the two rows.

#### Proof

As in Theorem 8.1, the \(x\)- and \(y\)-axis targets force \(2R\)
off-core pure pins, while the \(R\) occurrences \(P_z^{(r)}\) are
distinct, the \(R\) occurrences \(Q_z^{(s)}\) are distinct, and all
providers are off-core and distinct from those pins.

If one physical occurrence is both \(P_z^{(r)}\) and \(Q_w^{(s)}\), then
its third coordinate gives \(z=w\). Charge this common provider to the
ordered physical root pair \((X_z^{(r)},Y_z^{(s)})\). For one fixed root
pair, at most one common provider can be charged: the proof of (8.2),
with those two roots in place of \(X_R,Y_R\), gives the same
opposite-order contradiction. There are at most \(a_rb_s\) root pairs.
Therefore

\[
|\{P_z^{(r)}\}\cap\{Q_z^{(s)}\}|\le a_rb_s,
\]

and the union of the two provider families has size at least
\(2R-a_rb_s\).
Adding the \(2R\) pure \(x\)- and \(y\)-axis pins proves (8.4).
Rearrangement gives (8.5). \(\square\)

This is a literal portal tradeoff, not merely a support projection. For
one fixed row pair it still permits \(\sqrt R=o(R)\) portals. Applying it
simultaneously to all row pairs closes that escape.

### Theorem 8.3 (exact two-face wedge)

Let

\[
{\cal F}_R=
\{(x,0,z):0\le x,z\le R\}
\cup
\{(0,y,z):0\le y,z\le R\}
\setminus\{0\}.
\tag{8.6}
\]

The minimum length of a literal word covering every target in
\({\cal F}_R\) is exactly

\[
\boxed{g({\cal F}_R)=4R-1.}
\tag{8.7}
\]

#### Proof: lower bound

For each \(1\le r\le R\), select witnesses of
\((r,0,z)\), \(1\le z\le R\), and let \(a_r\) be the number of distinct
physical occurrences designated to attain first coordinate \(r\) in
those witnesses. Define \(b_s\) analogously from witnesses of
\((0,s,z)\). Put

\[
a=\min_r a_r,\qquad b=\min_s b_s.
\]

Root occurrences belonging to different \(r\)'s are distinct; the
\(x\)-root and \(y\)-root families are disjoint; and all are distinct
from the \(R\) pure \(z\)-axis pins forced by the targets \((0,0,z)\).
Therefore a word of length \(N\) covering \({\cal F}_R\) satisfies

\[
N\ge R+\sum_{r=1}^R a_r+\sum_{s=1}^R b_s
\ge R(1+a+b).
\tag{8.8}
\]

If \(a+b\ge3\), then \(N\ge4R\). Otherwise \(a=b=1\). Choose rows
\(r,s\) attaining these minima and apply Theorem 8.2 with empty core:

\[
N\ge4R-a_rb_s=4R-1.
\]

This proves the lower bound in every case.

#### Proof: matching word and literal intervals

Write

\[
X_i=(i,0,0),\qquad
Y_i=(0,i,0),\qquad
Z_i=(0,0,i).
\]

The word

\[
X_R,X_{R-1},\ldots,X_1,\;
Z_1,Z_2,\ldots,Z_R,\;
Z_{R-1},\ldots,Z_1,\;
Y_1,Y_2,\ldots,Y_R
\tag{8.9}
\]

has length \(4R-1\), with the second \(Z\)-run empty when \(R=1\). The
target \((x,0,z)\), with \(x,z>0\), is witnessed
from \(X_x\) to the first \(Z_z\): the intervening \(X\)-values decrease
and the \(Z\)-values increase. The target \((0,y,z)\), with \(y,z>0\),
is witnessed from the second \(Z_z\) to \(Y_y\), using the central
\(Z_R\) when \(z=R\): the intervening \(Z\)-values decrease and the
\(Y\)-values increase. Axis targets are singleton occurrences. Every
displayed interval therefore has exactly the required maximum.
\(\square\)

### Corollary 8.4 (two-coordinate recursive lifts fail quadratically)

Let a universal word have a distinguished core positive in coordinates
\(1,2\), and let \({\cal E}\) be its off-core occurrences. Then

\[
\boxed{|{\cal E}|\ge4R-1.}
\tag{8.10}
\]

Consequently, every occurrence-for-occurrence recursive lift whose
retained core is positive in two fixed coordinates satisfies

\[
\boxed{N_R\ge N_{R-2}+4R-1.}
\tag{8.11}
\]

#### Proof

Every target of \({\cal F}_R\) has zero in coordinate \(1\) or \(2\), so
none of its witnesses contains a core occurrence. Delete the core
positions from the word. Each selected wedge witness remains a
contiguous factor inside one core-free component, and concatenating
those components cannot destroy it. Thus the inherited off-core word
covers \({\cal F}_R\), and Theorem 8.3 proves (8.10). Taking the retained
copy as core proves (8.11). \(\square\)

With \(N_0\ge0\), \(N_1\ge4\), iteration gives

\[
\boxed{
N_{2s}\ge4s^2+3s,\qquad
N_{2s+1}\ge4s^2+7s+4.
}
\tag{8.12}
\]

Hence

\[
N_{2s}-W_{2s}\ge s^2-1,\qquad
N_{2s+1}-W_{2s+1}\ge s^2+s+1.
\tag{8.13}
\]

Both parities have excess \((1/4+o(1))R^2\). A recursive lift capable of
the conjectured scale must therefore keep zero in at least two fixed
coordinates; positivity in only one fixed coordinate is the first
support pattern not excluded here.

### Theorem 8.5 (catalogued nested-pivot duplication)

Fix \(t\ge2\) and define the three open inner-edge catalogues

\[
\begin{split}
E_{xy}&=\{(t-i,i,0):1\le i\le t-1\},\\
E_{yz}&=\{(0,t-i,i):1\le i\le t-1\},\\
E_{zx}&=\{(i,0,t-i):1\le i\le t-1\}.
\end{split}
\tag{8.14}
\]

Consider one word module with distinguished occurrences of every
catalogue point, the three inner hubs

\[
(t,0,0),\quad(0,t,0),\quad(0,0,t),
\]

and the three outer hubs

\[
q_x=(t+1,0,0),\quad
q_y=(0,t+1,0),\quad
q_z=(0,0,t+1).
\]

Write \(p_x=(t,0,0)\), \(p_y=(0,t,0)\), \(p_z=(0,0,t)\). At \(q_x\),
call \(E_{xy},E_{zx}\) the incident catalogues and call \(p_x\) its inner
hub; define the incident pair and inner hub cyclically at \(q_y,q_z\).
Assume the following literal certificate rule. For every outer hub \(q\),
its matching inner hub \(p\), and every pair \(L,R\) from its two
incident catalogues:

1. a selected witness of the shell-\(t\) lower target
   \(p\vee L\vee R\) avoids the
   distinguished occurrence \(q\) and contains occurrences of the exact
   types \(L,R\); and
2. a selected witness of the upper target \(q\vee L\vee R\) contains
   that occurrence \(q\) strictly between occurrences of the exact
   types \(L,R\).

Catalogue types are private exact types: one physical occurrence is
charged to at most one catalogue point. Then the module has length

\[
\boxed{n_t\ge5t+1.}
\tag{8.15}
\]

#### Proof

Fix one outer hub \(q\) and call its incident catalogues \(L,R\). Let
\(D_L\) be the set of \(L\)-types having occurrences on both sides of
\(q\), and define \(D_R\) similarly.

For a pair \(L_i,R_j\), its lower certificate lies wholly on one side of
\(q\), so its selected type occurrences lie on the same side. Its upper
certificate puts selected occurrences of those same types on opposite
sides. If \(L_i\notin D_L\) and \(R_j\notin D_R\), each type has a fixed
side, which would have to be simultaneously equal and unequal. Hence

\[
D_L\cup D_R
\]

is a vertex cover of the complete bipartite graph on \(L,R\). Every
vertex cover of a complete bipartite graph contains one whole part: if
some \(L_i\) is omitted, every \(R_j\) must be present. Therefore, at
each outer hub, one entire incident edge catalogue is duplicated across
that hub.

The three outer hubs impose the three edges of a triangle on the family
vertices \(E_{xy},E_{yz},E_{zx}\). Meeting all three constraints requires
at least two whole catalogues to be duplicated. The exact occurrence
ledger is therefore

\[
3(t-1)+3+3+2(t-1)=5t+1:
\]

one occurrence for each open-edge type, three inner hubs, three outer
hubs, and two full catalogues of additional occurrences. \(\square\)

### Corollary 8.6 (pair-confined nested-pivot iteration)

Let \(R=2s\). Suppose the global word is a concatenation of
occurrence-disjoint modules for the shell pairs

\[
(1,2),(3,4),\ldots,(2s-1,2s),
\]

and the module with inner level \(t=2k-1\ge3\) satisfies Theorem 8.5.
For \(t=1\), require its six distinct inner and outer axis hubs. Then

\[
\boxed{
N_R\ge\sum_{k=1}^{s}\bigl(5(2k-1)+1\bigr)
=5s^2+s.
}
\tag{8.16}
\]

Consequently,

\[
\boxed{
N_R-W_R\ge2s^2-2s-1
=\frac{R^2}{2}-R-1.
}
\tag{8.17}
\]

Equivalently, a \(t,t+1\) module pays the baseline

\[
W_{t+1}-W_{t-1}=3(t+1)
\]

plus the duplication toll \(2(t-1)\). The architecture has limiting
ratio at least \(5/3\).

The scope is strict. The theorem assumes a common straddled outer hub
for every pair in the restricted grid, private exact catalogue types,
and pair-confined occurrence accounting. It does not cover one-sided
upper witnesses, target-dependent hub occurrences, multipin letters,
cross-pair sharing, or abandonment of the inner-edge catalogue.

### Theorem 8.7 (private rooted-face arm ledger)

Let \(P\) be a universal word for \(Q_R\). For every coordinate
\(c\in\{1,2,3\}\) and \(1\le t\le R\), designate one root-pin occurrence
\(a_{c,t}\) whose letter is \(t e_c\). Assume that, for every ordered
\(d\ne c\) and every \(1\le u<t\), a chosen witness

\[
I_{c,t;d,u}\quad\hbox{of}\quad t e_c+u e_d
\]

contains the common root \(a_{c,t}\) and designates an arm-provider
occurrence \(q_{c,t;d,u}\), distinct from every root pin, whose
\(d\)-coordinate is exactly \(u\). Finally assume that one physical
arm-provider occurrence is designated for at most two quadruples
\((c,t;d,u)\). Then

\[
\boxed{
|P|\ge3R+\frac{3R(R-1)}2
=\frac{3R(R+1)}2.
}
\tag{8.18}
\]

Restricted to two consecutive levels \(t-1,t\), \(t\ge2\), let
\(N_{\rm pair}\) denote the number of distinct root and provider
occurrences charged to demands on those two levels. The same ledger gives

\[
\boxed{N_{\rm pair}\ge6t-3.}
\tag{8.19}
\]

#### Proof

At level \(t\) there are

\[
3\cdot2\cdot(t-1)=6(t-1)
\]

ordered arm demands. Summing over \(t\) gives \(3R(R-1)\). Reuse degree
two forces at least \(3R(R-1)/2\) provider positions. The \(3R\) root
pins are distinct and private from them, proving (8.18). For levels
\(t-1,t\), the provider count is

\[
\frac{6(t-2)+6(t-1)}2=6t-9;
\]

adding the six roots gives (8.19). \(\square\)

The triangular-shell word does not satisfy all three hypotheses
simultaneously. Choosing private within-shell open-edge providers makes
the \(xy\)- and \(xz\)-arms rooted at \(A_t\) use the initial and terminal
copies of \(A_t\), so common-root fails. Choosing instead the cross-shell
seam (1.6) so that both arms use the initial \(A_t\) makes the
\(u=t-1\) \(z\)-provider equal the previous root \(C_{t-1}\), so
provider-root privacy fails. The degree-two catalogue condition itself
is compatible. Hence the theorem does not apply: common roots, provider
privacy, and degree two are hypotheses, not consequences of
universality. Without privacy the additive \(3R\) is unavailable, and
without the degree bound this count gives no quadratic conclusion.

---

## 9. Surviving construction gates

No theorem above disproves

\[
g_3(R,R,R)=W_R+o(R^2).
\]

They leave three precise construction gates.

### 9.1 Asymmetric one-coordinate lift -- **UNPROVED**

Seek words \(U_R\) in which a contiguous factor is

\[
U_{R-2}+(1,0,0)
\]

and the prefix and suffix outside that factor have total length

\[
3R+e_R,\qquad e_R=o(R).
\tag{9.1}
\]

The retained factor literally preserves all translated witnesses whose
targets lie in

\[
[1,R-1]\times[0,R-2]\times[0,R-2].
\]

The sole exception is the translated local origin \((1,0,0)\), because
the old word is not required to witness \(0\). The construction must
give an explicit seam or outside witness for \((1,0,0)\), as well as
explicit intervals for every target complementary to the displayed
inner box.

The forced zero face \(x=0\) has an exact \(2R\)-letter word. With

\[
Y_i=(0,i,0),\qquad Z_i=(0,0,i),
\]

use

\[
Y_R,Y_{R-1},\ldots,Y_1,Z_1,Z_2,\ldots,Z_R.
\tag{9.2}
\]

The interval from \(Y_y\) to \(Z_z\) has maximum \((0,y,z)\); singleton
intervals give the axes. Conversely, the \(R\) pure \(y\)-axis pins and
\(R\) pure \(z\)-axis pins are forced, so \(2R\) is exact. Thus the
one-coordinate lift has \(R+o(R)\) positions beyond its mandatory zero
face with which to braid the upper face \(x=R\), the two top
\(y\)-levels, the two top \(z\)-levels, and all seams. No theorem in this
report excludes that ledger.

If such words exist uniformly with (9.1), then

\[
|U_R|\le |U_{R-2}|+3R+o(R)
\]

and the exact identity \(W_R-W_{R-2}=3R\), followed by summation on each
parity class, gives

\[
|U_R|=W_R+o(R^2).
\]

The unresolved certificate problem is not the interior factor; it is a
single literal ordering that extends (9.2) through the remaining
boundary slabs without inserting a forbidden maximum into any zero-face
interval. This is the sharp asymmetric construction gate left by the
two-face obstruction.

### 9.2 Three-shell module -- **UNPROVED**

For \(t\ge3\), the first confined window with interval-count slack has
thickness three.
Its exact width budget is

\[
W_t-W_{t-3}=
\begin{cases}
\dfrac{9t}{2}-2,&t\ \hbox{even},\\[2mm]
\dfrac{9t-5}{2},&t\ \hbox{odd},
\end{cases}
\tag{9.3}
\]

whereas Theorem 7.1 asks only

\[
L_3(t)=(\sqrt{18}+o(1))t.
\]

The leading slack is

\[
\left(\frac92-\sqrt{18}\right)t.
\]

A successful module must order its surface corridors so that every
selected interval stays inside the target box, and must give seam
witnesses for targets whose three coordinate maxima are supplied in
different sublayers. The exact catalogued/private nested common pivot is
excluded by Theorem 8.5. An internally complete two-shell submodule
already spends
\((\sqrt{12}-3)t+o(t)\) beyond its two-shell width share, so the third
shell would have to recover that deficit through cross-sublayer sharing;
Sections 7--8 do not rule this out inside the total three-shell budget.
No literal three-shell ordering was found.

### 9.3 Global high-reuse braid -- **UNPROVED**

To beat the rooted-face count at leading order, a braid must abandon at
least one of its three hypotheses: common pure roots, root-provider
privacy, or reuse degree at most two. The nested-pivot count likewise
forces target-dependent hubs, multipin providers, cross-window sharing,
or abandonment of its exact edge catalogue. These are exact design
requirements, not proof that such a braid exists.

On the obstruction side, Sections 4--5 show exactly what an endpoint
dual must add: a nonlinear potential, a nonconsecutive or non-rank
target region, or a constraint coupling the left and right endpoint
orders. Merely changing positive linear weights cannot produce a
quadratic excess.

---

## 10. Audit ledger

The following statements are unrestricted:

- the literal triangular-shell construction and its exact length
  (Theorem 1.1);
- the architecture-free endpoint lower bound and rigidity
  (Theorem 3.1 and Corollary 3.2);
- the exact weighted rank-band inequality and the uniform \(O(R)\)
  ceiling on that entire positive-linear dual family
  (Theorems 4.1 and 5.1);
- the exact \(4R-1\) word length for the union of two coordinate-zero
  faces (Theorem 8.3).

The following statements are conditional on the architectures written
in their hypotheses:

- the all-positive or two-coordinate-positive retained-core recurrences;
- the confined-shell and width-ledger portal counts;
- the common-root and root-portal corridor bounds, nested-pivot
  catalogue, and rooted-face arm ledgers.

The three construction gates in Section 9 are explicitly unproved. No
finite search, computation, or external source is used anywhere in this
report. The triangular-shell witnesses, endpoint inequalities,
rank-band constants, support tolls, shell counts, and duplication
arguments were each rederived and independently audited after the first
draft.
