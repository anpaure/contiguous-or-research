# The canonical \(K_5\) pentagon does not portal the alternating PBBS component

Date: 2026-07-27

Method: exact endpoint-table analysis; no computational search.

## 1. The pentagon is a valid fixed-core sigma trade

Fix a rank-four core \(R\) and five cyclically ordered outside coordinates

\[
Q=(q_0,q_1,q_2,q_3,q_4).
\]

Write \(z_{i\mid jk}\) for the diamond whose lower row is \(R+i\) and whose
endpoint pair is \(\{j,k\}\). Define

\[
P(Q)=\{z_{q_i\mid q_{i+1}q_{i+2}}:i\in\mathbb Z_5\},
\qquad
N(Q)=\{z_{q_{i+2}\mid q_iq_{i+1}}:i\in\mathbb Z_5\}.
\tag{1.1}
\]

The two sides have identical marginals:

- each root in \(Q\) occurs once on each side;
- the upper triple belonging to index \(i\) is
  \(\{q_i,q_{i+1},q_{i+2}\}\) on both sides;
- the endpoint-pair multiset on each side is the five edges of the cyclic
  pentagon on \(Q\).

Hence \(P(Q)-N(Q)\) lies in the fixed-core sigma-trade kernel.

After reindexing, the negative-side condition is

\[
N(Q)=\{z_{q_j\mid q_{j-2}q_{j-1}}:j\in\mathbb Z_5\}.
\tag{1.2}
\]

Reversing the cyclic order of \(Q\) interchanges (1.1) and (1.2). Therefore
it is enough in every executability audit to test the forward rule

\[
\epsilon_R(q_i)=\{q_{i+1},q_{i+2}\}.
\tag{1.3}
\]

## 2. No initial pentagon contains the alternating chord

Let

\[
Z=\{1,3,5,7,9\},
\qquad R_x=Z\setminus\{x\}.
\]

The row \(Z=R_x+x\) has endpoint pair

\[
\epsilon_{R_x}(x)=\{0,10\}.
\tag{2.1}
\]

If (1.3) contains this diamond, rotate \(Q\) so that \(q_0=x\). Up to
reversing the two endpoints, there are only two possibilities:

\[
Q=(x,0,10,a,b)
\quad\text{or}\quad
Q=(x,10,0,a,b).
\tag{2.2}
\]

For \(x\in\{3,5,7\}\), exact cyclic reduction gives

\[
\epsilon_{R_x}(0)=\epsilon_{R_x}(10)=\{x-1,x+1\}.
\tag{2.3}
\]

In the first order in (2.2), equation (1.3) requires
\(\epsilon_{R_x}(0)=\{10,a\}\), contradicting (2.3). In the second order it
requires \(\epsilon_{R_x}(10)=\{0,a\}\), again contradicting (2.3).

At the boundary \(x=1\), with \(R=\{3,5,7,9\}\), the relevant endpoint
entries are

\[
\epsilon_R(0)=\{1,2\},
\qquad
\epsilon_R(10)=\{0,2\}.
\tag{2.4}
\]

For \(Q=(1,0,10,a,b)\), the root \(0\) would require pair \(\{10,a\}\),
impossible by (2.4). For \(Q=(1,10,0,a,b)\), the root \(10\) forces
\(a=2\), after which the root \(0\) forces \(b=1\), repeating the root
\(q_0=1\). Thus no five-element \(Q\) exists. The case \(x=9\) is the
reflection.

By the reversal observation following (1.2), the same argument excludes
both sides of the pentagon trade. Therefore:

### Theorem 2.1

No executable side of the canonical \(K_5\) pentagon trade in the initial
PBBS factor contains a chord of the alternating component.

## 3. No pentagon portal appears after the boundary \(K_4\)

For the unique boundary core

\[
R=\{3,5,7,9\},
\]

the \(K_4\) reversal changes the four endpoint entries to

\[
\begin{array}{c|cccc}
u&1&10&0&2\\ \hline
\epsilon'_R(u)&\{0,2\}&\{1,2\}&\{1,10\}&\{0,10\}.
\end{array}
\tag{3.1}
\]

The transported alternating route uses the chords

\[
R+2:\{0,10\},
\qquad
R+10:\{1,2\}.
\tag{3.2}
\]

First suppose a forward pentagon contains the chord at root \(2\). Its
cyclic order must begin with one of

\[
(2,0,10,a,b),\qquad (2,10,0,a,b).
\tag{3.3}
\]

In the first case, the root \(0\) and (3.1) force \(a=1\); then the root
\(10\) forces \(b=2\), repeating the initial root. In the second case, the
root \(10\) would need an endpoint \(0\), absent from
\(\epsilon'_R(10)=\{1,2\}\).

Now suppose it contains the chord at root \(10\). Its order must begin with

\[
(10,1,2,a,b),\qquad (10,2,1,a,b).
\tag{3.4}
\]

In the first case, the root \(1\) forces \(a=0\), and then the root \(2\)
forces \(b=10\), repeating the initial root. In the second case, the root
\(2\) would need endpoint \(1\), absent from
\(\epsilon'_R(2)=\{0,10\}\).

Again reversal excludes the opposite side of the trade. Hence:

### Theorem 3.1

After either boundary \(K_4\) transport, no executable side of the canonical
\(K_5\) pentagon trade contains either transported chord on the alternating
route.

## 4. Consequence and scope

The canonical five-diamond circulation is a genuine new support pattern,
but it does not supply the missing PBBS portal:

\[
\boxed{\text{initial alternating route}
\ \xrightarrow{\ K_5\ }\ \text{impossible},\qquad
\text{boundary \(K_4\) transport}
\ \xrightarrow{\ K_5\ }\ \text{impossible}.}
\]

This closes the most symmetric \(K_5\) candidate. It does not classify the
entire \(K_5\) circuit lattice and therefore does not prove that every
one-common-core portal needs \(K_6\). Nor does it rule out a changing-core
two-alpha commutator. Those remain the two smallest unresolved categories.
