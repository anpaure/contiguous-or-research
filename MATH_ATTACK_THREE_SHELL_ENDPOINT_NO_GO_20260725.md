# Exact rank-\(2t\) no-go for internally confined shell modules

Date: 2026-07-25

## 0. Verdict

Put

\[
Q_t=[0,t]^3,\qquad
\mathcal S_{t,k}=Q_t\setminus Q_{t-k}
\quad(1\le k\le t),
\]

and let \(W_t\) be the width of \(Q_t\). A word *internally covers*
\(\mathcal S_{t,k}\) if every target in that shell is the
coordinatewise maximum of a nonempty contiguous interval lying in the
word.

The confined three-shell gate is impossible for the strongest elementary
reason: the shell itself has an upper-rank antichain twice as large as
its recursive width ledger. For \(t\ge9\),

\[
\boxed{
\left|\mathcal S_{t,3}\cap\{x+y+z=2t\}\right|=9t-27.}
\tag{0.1}
\]

Consequently every word internally covering \(\mathcal S_{t,3}\) has
length at least \(9t-27\). On the other hand,

\[
W_t-W_{t-3}=
\begin{cases}
\dfrac{9t}{2}-2,&t\ \text{even},\\[2mm]
\dfrac{9t-5}{2},&t\ \text{odd}.
\end{cases}
\tag{0.2}
\]

Thus the exact parity comparisons are

\[
\boxed{
9t-27=
\begin{cases}
2(W_t-W_{t-3})-23,&t\ \text{even},\\
2(W_t-W_{t-3})-22,&t\ \text{odd}.
\end{cases}}
\tag{0.3}
\]

No internally complete three-shell module can have length
\(W_t-W_{t-3}+o(t)\); it needs twice that ledger at leading order.

More generally, for \(t\ge3k\),

\[
\boxed{
\left|\mathcal S_{t,k}\cap\{x+y+z=2t\}\right|
=\binom{t+2}{2}-\binom{t-3k+2}{2}
=\frac{3k}{2}(2t+3-3k).}
\tag{0.4}
\]

This exact formula closes every internally confined shell scheme of
uniformly sublinear thickness. If the shell modules are
occurrence-disjoint, their total length is

\[
\left(\frac32-o(1)\right)R^2
=(2-o(1))W_R.
\tag{0.5}
\]

If their physical hulls overlap, a near-width global word requires total
cross-window overlap incidence at least

\[
\left(\frac34-o(1)\right)R^2.
\tag{0.6}
\]

Accordingly the next live shell statement must use either a
macroscopically thick window or a fusion that shares a quadratic number
of physical module incidences (or witnesses that are not confined to
individual shell hulls).

---

## 1. Antichains force distinct word starts

### Lemma 1.1

Let a word internally cover a target family \(F\) in a product order.
If \(A\subseteq F\) is an antichain, then the word has length at least
\(|A|\).

### Proof

Choose one interval witness \(I_a=[\ell_a,r_a]\) for every \(a\in A\).
Two distinct witnesses cannot have the same left endpoint. Indeed, two
intervals with one common left endpoint are nested, and coordinatewise
maxima of nested intervals are comparable. Their two maxima would
therefore be comparable members of \(A\), a contradiction.

Hence the \(|A|\) witnesses have \(|A|\) distinct physical left
endpoints, so the word has at least \(|A|\) positions. \(\square\)

The same proof works with right endpoints. No assumption on shell order,
roots, portals, private providers, or the letters outside the selected
witnesses is used.

---

## 2. Exact shell antichain

### Theorem 2.1

For \(1\le k\le t\), the rank-\(2t\) part of
\(\mathcal S_{t,k}\) has size

\[
A(t,k)=
\begin{cases}
\displaystyle
\binom{t+2}{2}-\binom{t-3k+2}{2}
=\dfrac{3k}{2}(2t+3-3k),&t\ge3k,\\[4mm]
\displaystyle
\binom{t+2}{2},&t<3k.
\end{cases}
\tag{2.1}
\]

Every word internally covering \(\mathcal S_{t,k}\) consequently has
length at least \(A(t,k)\).

### Proof

The rank-\(2t\) size of \(Q_t\) equals its rank-\(t\) size by the
coordinatewise involution

\[
(x,y,z)\longmapsto(t-x,t-y,t-z).
\]

The upper bounds are inactive for nonnegative triples of sum \(t\), so

\[
|Q_t\cap\{x+y+z=2t\}|=\binom{t+2}{2}.
\tag{2.2}
\]

The maximum rank in \(Q_{t-k}\) is \(3(t-k)\). If \(t<3k\), then
\(2t>3(t-k)\), so the inner cube contributes no point of rank \(2t\).

Suppose \(t\ge3k\). The complement involution inside \(Q_{t-k}\) sends
rank \(2t\) to rank

\[
3(t-k)-2t=t-3k.
\]

This rank is nonnegative and is at most \(t-k\), so again the coordinate
upper bounds are inactive. The inner contribution is therefore

\[
|Q_{t-k}\cap\{x+y+z=2t\}|=\binom{t-3k+2}{2}.
\tag{2.3}
\]

Subtracting (2.3) from (2.2) proves the first expression in (2.1).
The binomial difference simplifies as

\[
\binom{t+2}{2}-\binom{t-3k+2}{2}
=\frac{3k}{2}(2t+3-3k).
\]

All targets counted in (2.1) have the same coordinate-sum rank, so they
form an antichain. Lemma 1.1 proves the word-length conclusion.
\(\square\)

### Three-shell specialization

For \(k=3\), (2.1) reads

\[
A(t,3)=
\begin{cases}
9t-27,&t\ge9,\\
\binom{t+2}{2},&3\le t<9.
\end{cases}
\tag{2.4}
\]

The exact equal-cube widths are

\[
W_{2s}=3s^2+3s+1,\qquad
W_{2s+1}=3(s+1)^2.
\tag{2.5}
\]

Substituting \(t-3\) into the opposite-parity formula in (2.5) gives
(0.2), and then direct subtraction gives (0.3). Equivalently, the excess
over one three-shell width ledger is

\[
A(t,3)-(W_t-W_{t-3})=
\begin{cases}
\dfrac{9t}{2}-25,&t\ \text{even},\\[2mm]
\dfrac{9t-49}{2},&t\ \text{odd}.
\end{cases}
\tag{2.6}
\]

This is a positive linear toll with leading coefficient \(9/2\).

### Sublinear-thickness comparison

The width formula can be written

\[
W_t=\frac34t^2+\frac32t+c_t,\qquad
c_t=
\begin{cases}
1,&t\ \text{even},\\
\frac34,&t\ \text{odd}.
\end{cases}
\tag{2.7}
\]

Hence

\[
W_t-W_{t-k}
=\frac32kt-\frac34k^2+\frac32k+(c_t-c_{t-k}).
\tag{2.8}
\]

On the range \(t\ge3k\), (0.4) is

\[
A(t,k)=3kt-\frac92k^2+\frac92k.
\tag{2.9}
\]

If \(k=o(t)\), division of (2.9) by (2.8) gives

\[
\boxed{
A(t,k)=(2-o(1))(W_t-W_{t-k}).}
\tag{2.10}
\]

Thus allowing the confined window thickness to tend to infinity does
not help while it remains sublinear in the outer radius.

---

## 3. Exact disjoint three-shell recurrence sum

Fix \(r\in\{0,1,2\}\), write \(R=r+3m\), and put

\[
t_j=r+3j\qquad(1\le j\le m).
\]

Suppose a global construction uses occurrence-disjoint word blocks
\(H_j\), with \(H_j\) internally covering
\(\mathcal S_{t_j,3}\). Lemma 1.1 and (2.4) give

\[
\sum_{j=1}^m|H_j|\ge\sum_{j=1}^m A(t_j,3).
\tag{3.1}
\]

For all \(t\ge3\),

\[
A(t,3)=9t-27+\delta_t,
\]

where

\[
\delta_3=10,\quad
\delta_4=6,\quad
\delta_5=3,\quad
\delta_6=1,
\qquad
\delta_t=0\quad(t\ge7).
\tag{3.2}
\]

Consequently, for \(m\ge2\) when \(r=0\),

\[
\boxed{
\sum_{j=1}^m A(t_j,3)
=\frac{27}{2}m^2+
\left(9r-\frac{27}{2}\right)m+c_r,}
\tag{3.3}
\]

with

\[
c_0=11,\qquad c_1=6,\qquad c_2=3.
\tag{3.4}
\]

Indeed,

\[
\sum_{j=1}^m(9t_j-27)
=9mr+\frac{27}{2}m(m+1)-27m
=\frac{27}{2}m^2+
\left(9r-\frac{27}{2}\right)m,
\]

and the corrections met in the three residue classes are respectively
\(\delta_3+\delta_6=11\), \(\delta_4=6\), and \(\delta_5=3\).

Since \(R=r+3m\), (3.3) is equivalently

\[
\sum_{j=1}^m A(t_j,3)
=\frac32R^2-\frac92R+e_r,
\qquad
(e_0,e_1,e_2)=(11,9,6).
\tag{3.5}
\]

If the base block internally covers \(Q_r\), its exact minimum lengths
are \(0,4,10\) for \(r=0,1,2\). Therefore every disjoint three-shell
recursion has the exact lower bounds

\[
\boxed{
N_R\ge\frac32R^2-\frac92R+d_r,\qquad
(d_0,d_1,d_2)=(11,13,16),}
\tag{3.6}
\]

apart from the harmless case \(r=0,m=1\), where the direct bound is
\(N_3\ge10\).

In particular,

\[
N_R\ge\left(\frac32-o(1)\right)R^2
=(2-o(1))W_R.
\tag{3.7}
\]

Thus every occurrence-disjoint internally complete three-shell
recursion is trapped at the same leading factor two as the known global
triangular-shell benchmark.

---

## 4. Exact overlap-incidence ledger

The module hulls need not be disjoint for the antichain theorem to
apply. Let \(H_j\) be contiguous subwords of one global word, each
internally covering \(\mathcal S_{t_j,3}\). For a physical word position
\(p\), put

\[
\mu(p)=\#\{j:p\in H_j\},
\]

and define

\[
\mathcal Q
=\sum_{p:\,\mu(p)>0}(\mu(p)-1)
=\sum_j|H_j|-\left|\bigcup_jH_j\right|.
\tag{4.1}
\]

Because the global word has at least \(|\bigcup_jH_j|\) positions,
(3.5) gives the exact hull-incidence lower bound

\[
\boxed{
N_R\ge
\frac32R^2-\frac92R+e_r-\mathcal Q.}
\tag{4.2}
\]

Since \(W_R=(3/4)R^2+O(R)\), any such system with

\[
N_R=W_R+o(R^2)
\]

must satisfy

\[
\boxed{
\mathcal Q\ge\left(\frac34-o(1)\right)R^2.}
\tag{4.3}
\]

Thus an \(o(R^2)\)-overlap correction cannot rescue internally complete
three-shell hulls. A surviving reset-free fusion theorem must identify
quadratic physical sharing, not merely \(o(t)\) seam overlaps.

---

## 5. Variable sublinear shell thickness

The fixed thickness is not essential. Let

\[
0\le t_0<t_1<\cdots<t_m=R,\qquad
k_j=t_j-t_{j-1}.
\]

Assume \(t_j\ge3k_j\) and let a module \(H_j\) internally cover
\(\mathcal S_{t_j,k_j}\). Summing (0.4) gives

\[
\begin{aligned}
\sum_{j=1}^m A(t_j,k_j)
&=\sum_j\left(
3k_jt_j-\frac92k_j^2+\frac92k_j
\right)\\
&=\boxed{
\frac32(R^2-t_0^2)
-3\sum_jk_j^2+\frac92(R-t_0).}
\end{aligned}
\tag{5.1}
\]

For the second equality, use

\[
2k_jt_j-k_j^2=t_j^2-t_{j-1}^2
\]

and telescope.

Now consider a sequence of such schemes with

\[
t_0=o(R),\qquad
K_R:=\max_j k_j=o(R).
\tag{5.2}
\]

Then

\[
\sum_jk_j^2\le K_R\sum_jk_j
=K_R(R-t_0)=o(R^2).
\tag{5.3}
\]

Equations (5.1)--(5.3) imply

\[
\sum_j A(t_j,k_j)
=\left(\frac32-o(1)\right)R^2.
\tag{5.4}
\]

In particular, (5.2) follows from the usual uniformly sublinear
condition

\[
t_0=o(R),\qquad
\max_j\frac{k_j}{t_j}=o(1);
\]

that condition also ensures \(t_j\ge3k_j\) for all sufficiently large
schemes. Therefore every occurrence-disjoint internally confined
\(k=o(t)\) shell scheme satisfies

\[
\boxed{N_R\ge(2-o(1))W_R.}
\tag{5.5}
\]

For overlapping hulls define \(\mathcal Q\) as in (4.1). The same union
identity gives

\[
N_R\ge
\frac32(R^2-t_0^2)
-3\sum_jk_j^2+\frac92(R-t_0)-\mathcal Q.
\tag{5.6}
\]

Under (5.2), a near-width global word again requires

\[
\boxed{\mathcal Q\ge\left(\frac34-o(1)\right)R^2.}
\tag{5.7}
\]

This is the exact surviving statement: sublinear internally confined
shells cannot beat factor two without quadratic cross-window physical
fusion.

---

## 6. Architecture-free endpoint-reuse gate

There is a corresponding necessary ledger even when witnesses are
allowed to cross every proposed shell boundary. Use the fixed
three-shell partition from Section 3, and in an arbitrary universal word
choose one witness for every target in each rank-\(2t_j\) antichain.

For a physical position \(p\), let \(\lambda(p)\) be the number of shell
antichains whose selected family contains a witness starting at \(p\).
Within one shell antichain the starts are distinct by Lemma 1.1. Hence

\[
\sum_p\lambda(p)=\sum_jA(t_j,3)
=\frac32R^2-\frac92R+e_r.
\tag{6.1}
\]

Define the cross-shell left-start reuse

\[
\mathcal R_L=\sum_{p:\,\lambda(p)>0}(\lambda(p)-1).
\tag{6.2}
\]

At most \(N_R\) physical starts are used, so (6.1) gives the exact bound

\[
\boxed{
\mathcal R_L\ge
\frac32R^2-\frac92R+e_r-N_R.}
\tag{6.3}
\]

Repeating the same argument with right endpoints gives an independent
quantity \(\mathcal R_R\) satisfying the identical bound. Therefore
every near-width universal word obeys

\[
\boxed{
\mathcal R_L,\mathcal R_R
\ge\left(\frac34-o(1)\right)R^2.}
\tag{6.4}
\]

This conclusion assumes neither internal hulls nor a recursive word
order. It pinpoints what an unrestricted reset-free surface braid must
do: a quadratic mass of both endpoint families must be shared across
different radius windows. The theorem does not rule out such nested
cross-shell reuse.

No computation or finite search is used.
