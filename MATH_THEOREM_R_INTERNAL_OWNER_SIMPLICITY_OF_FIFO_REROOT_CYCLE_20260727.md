# Internal owner simplicity of a reduced FIFO re-root cycle

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or web input is used.

## 0. Exact result

Let

\[
L=2m,\qquad k=m-H,\qquad \ell=m+H,
\]

and assume

\[
1\le r\le H,\qquad 2H<m,\qquad \gcd(\ell,r)=1.
\tag{0.1}
\]

On the ordered state

\[
\Sigma=(Q=(q_0,\ldots,q_{H-1});
        P=(p_0,\ldots,p_{m-1});
        E=(e_0,\ldots,e_{k-1}))
\]

use the exact maps

\[
\begin{aligned}
O\Sigma={}&(q_1,\ldots,q_{H-1},p_0;\,
             p_1,\ldots,p_{m-1},q_0;\,
             E),\\
S\Sigma={}&(q_1,\ldots,q_{H-1},e_0;\,
             p_1,\ldots,p_{m-1},q_0;\,
             e_1,\ldots,e_{k-1},p_0)
\end{aligned}
\]

and put

\[
F_r=S O^{r-1}.
\tag{0.2}
\]

Because \(\gcd(\ell,r)=1\), the ordered slots form one \(L\)-cycle
under \(F_r\). For a block index \(b\in\mathbb Z/L\mathbb Z\) and a
within-block phase \(0\le j<r\), let \(\mathcal P_{b,j}\) be the
middle-owner set at the state

\[
O^jF_r^b\Sigma.
\tag{0.3}
\]

The terminal state at phase \(r\) is the next block's phase-zero state
and is not counted again.

### Theorem 0.1 (all principal owners in one closed macro cycle are distinct)

Under (0.1),

\[
\boxed{
\mathcal P_{b,j}=\mathcal P_{b',j'}
\quad\Longleftrightarrow\quad
b=b'\pmod {2m}\ \hbox{ and }\ j=j'.
}
\tag{0.4}
\]

Consequently one closed \(F_r\)-cycle contains exactly

\[
\boxed{2mr}
\tag{0.5}
\]

pairwise distinct middle-owner \(m\)-subsets. In particular, the
unresolved owner-simple packing gate has no within-cycle multiplicity
loss for the calibrated choice \(r=\rho\), whenever
\(\gcd(m+H,\rho)=1\) and \(m\) is sufficiently large.

The theorem does not assert that owner sets belonging to two different
coordinate orders are disjoint. That cross-cycle matching condition,
root disjointness, ordered queue compatibility, and all prefix-target
capacities remain separate requirements.

## 1. The exact slot chart

Use the cyclic top-slot order

\[
u_0=Q_0,\quad
u_1,\ldots,u_m=P_{m-1},\ldots,P_0,\quad
u_{m+1},\ldots,u_{\ell-1}=Q_{H-1},\ldots,Q_1.
\tag{1.1}
\]

The map \(O\) sends \(u_i\) to \(u_{i+1}\). Relative to top rotation
by \(r\), the map \(F_r\) replaces the arrow

\[
u_{m-r+1}\longrightarrow u_{m+1}
\]

by the path through the \(E\)-slots. Since \(r\) is invertible modulo
\(\ell\), define

\[
v_t=u_{m+1+rt}\qquad(0\le t<\ell),
\tag{1.2}
\]

with the subscript on \(u\) read modulo \(\ell\). Then an exact
\(F_r\)-cycle chart \(\phi:\mathbb Z/L\mathbb Z\to\{\hbox{ordered
slots}\}\) is

\[
\phi(t)=v_t\quad(0\le t<\ell),
\qquad
\phi(\ell+s)=E_{k-1-s}\quad(0\le s<k).
\tag{1.3}
\]

Indeed, the last top slot in (1.2) is

\[
v_{\ell-1}=u_{m+1-r}=u_{m-r+1},
\]

and hence

\[
v_{\ell-1}\to E_{k-1}\to\cdots\to E_0\to v_0.
\]

Thus

\[
F_r\phi(x)=\phi(x+1).
\tag{1.4}
\]

For set calculations below, identify each coordinate label with the
unique chart position of the slot which contains it in the initial
state \(\Sigma\). This is a bijective relabelling and therefore
preserves equality and distinctness of owner sets.

Put

\[
T=\{0,\ldots,\ell-1\},
\qquad
J=\{\ell,\ldots,L-1\}.
\tag{1.5}
\]

The interval \(J\) is precisely the exterior-root slot set and has
length \(k=m-H\).

## 2. The phase patterns

Let \(a\in\mathbb Z/\ell\mathbb Z\) be the inverse of \(r\):

\[
ar\equiv1\pmod\ell.
\tag{2.1}
\]

At phase zero, the top slots outside \(P\) are the \(Q\)-slots, namely
the cyclic \(H\)-interval

\[
u_{m+1},u_{m+2},\ldots,u_{\ell-1},u_0.
\]

Therefore the top-slot complement of the phase-\(j\) owner
\(O^{-j}P\) is

\[
\{u_{m+1-j+s}:0\le s<H\}.
\tag{2.2}
\]

In the \(F_r\)-chart (1.2), this is the set

\[
G_j
=\{a(s-j)\pmod\ell:0\le s<H\}
\subseteq T.
\tag{2.3}
\]

Thus the initial-slot labels forming the phase-\(j\) owner and its
complement are, respectively,

\[
A_j=T\setminus G_j,
\qquad
C_j=J\cup G_j.
\tag{2.4}
\]

Since applying \(F_r^b\) moves labels forward by \(b\) in the chart,
the labels present in \(P\) after (0.3) are those whose initial slots
lie in

\[
A_j-b.
\tag{2.5}
\]

Equivalently,

\[
\mathcal P_{b,j}^{\,c}
=\phi(C_j-b).
\tag{2.6}
\]

The two boundary facts decisive below are

\[
0\in G_j,
\qquad
\ell-1\notin G_j
\qquad(0\le j<r).
\tag{2.7}
\]

For the first, choose \(s=j\) in (2.3); this is allowed because
\(j<r\le H\). For the second, membership of \(\ell-1\) would give

\[
s-j\equiv-r\pmod\ell
\tag{2.8}
\]

for some \(0\le s<H\). But

\[
-(r-1)\le s-j\le H-1.
\]

The representative \(-r\) is below this interval, while the other
representative \(\ell-r\) is above it because
\(\ell-r\ge m>H-1\). Hence (2.8) is impossible.

The set \(G_j\), viewed back in the \(u\)-chart, is one nonempty proper
cyclic interval of length \(H<\ell\). It consequently has trivial
stabilizer under top-slot rotation. Indeed, such an interval has a
unique directed boundary edge from its complement into the interval,
which every stabilizing rotation must fix.

## 3. Proof of Theorem 0.1

Suppose

\[
\mathcal P_{b,j}=\mathcal P_{b',j'}.
\]

By (2.6), with

\[
\delta=b-b'\pmod L,
\]

we have

\[
C_j=C_{j'}+\delta.
\tag{3.1}
\]

Let \(d\in[0,m]\) be the least cyclic magnitude of \(\delta\). Since
both \(G_j\) and \(G_{j'}\) have size \(H\), (3.1) implies

\[
|J\mathbin\triangle(J+\delta)|\le2H.
\tag{3.2}
\]

The set \(J\) is a cyclic interval of length \(k=m-H<L/2\). For a
translation of least magnitude \(d\le L/2=m\),

\[
|J\mathbin\triangle(J+\delta)|=2\min\{d,k\}.
\tag{3.3}
\]

Since \(k>H\) by (0.1), equations (3.2)--(3.3) force

\[
d\le H.
\tag{3.4}
\]

Assume first that \(\delta=d\) with \(1\le d\le H\). In the chart
\(\mathbb Z/L\mathbb Z\),

\[
J\setminus(J+d)=\{\ell,\ldots,\ell+d-1\}.
\tag{3.5}
\]

Every point of (3.5) belongs to the left side of (3.1) and not to the
translated copy \(J+d\). It must therefore belong to \(G_{j'}+d\).
Subtracting \(d\) gives

\[
\{\ell-d,\ldots,\ell-1\}\subseteq G_{j'}.
\tag{3.6}
\]

In particular \(\ell-1\in G_{j'}\), contradicting (2.7).

Assume next that \(\delta=-d\) with \(1\le d\le H\). Now

\[
(J-d)\setminus J=\{\ell-d,\ldots,\ell-1\}.
\tag{3.7}
\]

These points occur on the right side of (3.1) but lie outside \(J\),
so equality forces them to lie in \(G_j\). Again
\(\ell-1\in G_j\), contradicting (2.7).

Thus \(d=0\), so \(b=b'\pmod L\). Equation (3.1) then gives
\(G_j=G_{j'}\). By (2.2), these are two rotations by \(-j\) and
\(-j'\) of the same proper cyclic \(H\)-interval in the \(u\)-chart.
Its rotational stabilizer is trivial, so

\[
j\equiv j'\pmod\ell.
\]

Because \(0\le j,j'<r<\ell\), this means \(j=j'\). The converse in
(0.4) is immediate. This proves Theorem 0.1. \(\square\)

## 4. Exact stabilizer and packing consequences

The proof yields three exact statements, not merely the count (0.5).

1. For each fixed phase \(j\), the full owner pattern \(A_j\) has
   trivial stabilizer under the \(F_r\)-cycle translation group
   \(\mathbb Z/L\mathbb Z\).

2. No two distinct phase patterns \(A_j,A_{j'}\),
   \(0\le j,j'<r\), are translates of one another under that group.

3. Hence a genuine closed ordered \(F_r\)-cycle is a legitimate
   hyperedge with exactly \(2m\) distinct root vertices and exactly
   \(2mr\) distinct middle-owner vertices. The latter rank is not a
   formal multiplicity count.

At the reduced scale \(r=\rho\sim\log m\), this resolves internal owner
simplicity completely. A near-perfect packing theorem must still select
different coordinate-order cycles whose two vertex sets are jointly
disjoint (up to the intended small leaves). Low codegree in the root
projection alone does not imply this joint matching statement, but no
extra within-edge owner collision has to be charged.
