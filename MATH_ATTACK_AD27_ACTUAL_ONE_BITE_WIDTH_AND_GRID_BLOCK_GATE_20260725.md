# Actual one-bite holes: exact shadow loss and the grid-block cone gate

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

Put

\[
W=\binom{2m}{m},\qquad R_q=\binom{2m}{m-q}=R_{-q},
\qquad 0\le q\le Q.
\]

Consider a genuine owner-scale bite selecting \(k\) internally rainbow
trajectories whose claimed targets are mutually distinct. Let \(L\) be
the number of owner phases per trajectory and \(P\) the number of
catalogue tags. Thus \((L,P)=(M,N)\) in the full carrier catalogue and
\((L,P)=(g,T)\) in the geodesic-chunk catalogue. Write

\[
u_0=kL,\qquad u_{-q}=u_q=kc_q
\]

for the exact numbers of covered targets, and

\[
\mathcal H_d=\binom{[2m]}{m+d}\setminus\mathcal C_d
\]

for the actual complement holes.

The proved conclusions are:

1. The actual residual width obeys

   \[
   \boxed{
   W-u_0\le\operatorname{width}(\mathcal H)
   \le\left\lfloor W-\frac{u_0}{m+1}\right\rfloor.}
   \tag{0.1}
   \]

   Hence one owner-scale bite still leaves width \(W-o(W)\).

2. Suppose

   \[
   c_0=L\le W/P,\qquad c_q\le R_q/P.
   \tag{0.2}
   \]

   The total adjacent-rank Hall deficiency of the actual holes on both
   sides of the middle is at most

   \[
   \boxed{E_1\le\frac{2k}{P}\sum_{q=1}^Q R_q,}
   \tag{0.3}
   \]

   and the total two-step deficiency is at most

   \[
   \boxed{E_2\le\frac{2k}{P}\sum_{q=2}^Q R_q.}
   \tag{0.4}
   \]

   At owner-bite scale \(k/P=O(1/m)\), both are
   \(O(W/\sqrt m)=o(W)\). These are actual-hole estimates, not bounds on
   withheld donor strings.

3. Two consecutive saturated rotor columns satisfy the exact cone law

   \[
   \boxed{
   C'_{-Q}=C_{-Q}-x+y,\qquad
   C'_d=C_{d-1}+y\quad(-Q<d\le Q),}
   \tag{0.5}
   \]

   with one common arrival token \(y\). This law is also sufficient.
   Therefore \(r\) residual inclusion chains fit in one literal
   \(r\)-phase block exactly when they possess saturated extensions
   satisfying (0.5) successively. The compiled length is \(r+2Q+1\).

4. Shadow condensation does not imply (0.5). If two consecutive columns
   have prescribed distinct sets \(S,T\) at one common rank, then

   \[
   \boxed{d_J(S,T)=1,}
   \tag{0.6}
   \]

   and this condition is sufficient for the two singleton constraints.
   In a geodesic grid, prescribed middle owners in one run must form a
   monotone Johnson geodesic:

   \[
   d_J(X_s,X_t)=|s-t|.
   \tag{0.7}
   \]

Thus the vertical actual-hole gate is favorable in one bite, but the
factor-\(Q\) batching gate is exactly an integral geodesic low-run
coloring with common cone tokens. It remains unproved.

## 1. Exact actual-hole width sandwich

### Theorem 1.1

For every covered family having exactly \(u_0\) covered middle sets,
(0.1) holds.

### Proof

The \(W-u_0\) uncovered middle sets form an antichain, proving the lower
bound.

Let \(\mathcal A\subseteq\mathcal H\) be an antichain, and put

\[
a_0=\left|\mathcal A\cap\binom{[2m]}m\right|,
\qquad a_*=|\mathcal A|-a_0.
\]

LYM gives

\[
\frac{a_0}{W}
+\sum_{d\ne0}
 \frac{|\mathcal A\cap\binom{[2m]}{m+d}|}
      {\binom{2m}{m+d}}
\le1.
\]

Every off-middle protected row has size at most

\[
R_1=\binom{2m}{m-1}=\frac{m}{m+1}W.
\]

Consequently

\[
\frac{a_0}{W}+\frac{a_*}{R_1}\le1,
\]

and hence

\[
|\mathcal A|
\le R_1+\left(1-\frac{R_1}{W}\right)a_0.
\]

The right side increases with \(a_0\), while \(a_0\le W-u_0\).
Substituting \(R_1/W=m/(m+1)\) gives

\[
|\mathcal A|\le W-\frac{u_0}{m+1}.
\]

Taking the integer floor proves the theorem. \(\square\)

For the full-trajectory bite, truncate if necessary so that \(k\le N/M\).
Then

\[
u_0=kM\le N=(1+o(1))W/m.
\]

The guaranteed nontrivial bite has \(u_0=\Theta(N)\), so the universal
sandwich becomes

\[
W-\Theta(W/m)
\le\operatorname{width}(\mathcal H)
\le W-\Theta(W/m^2).
\]

Closing this interval requires information about the location of the
covered owners inside Boolean shadows.

## 2. Actual adjacent and two-step shadow loss

We use the normalized matching property of Boolean levels: if
\(\mathcal A\subseteq\binom{[2m]}r\) and \(r<m\), then

\[
\frac{|N^+(\mathcal A)|}{\binom{2m}{r+1}}
\ge
\frac{|\mathcal A|}{\binom{2m}r}.
\tag{2.1}
\]

Iterating gives its two-step version.

### Lemma 2.1 (target deletion)

Let \(V\to V'\) be a normalized-matching inclusion graph with
\(\rho=|V'|/|V|>1\). After deleting \(u\) vertices from \(V'\), the Hall
deficiency from any surviving subfamily of \(V\) into the surviving
\(V'\) is at most

\[
\boxed{\lfloor u/\rho\rfloor.}
\tag{2.2}
\]

### Proof

A family of size \(a\) has at least \(\lceil\rho a\rceil\) neighbors
before deletion and at least

\[
\max\{0,\lceil\rho a\rceil-u\}
\]

after deletion. If \(\rho a\le u\), its deficiency is at most
\(a\le u/\rho\). If \(\rho a>u\), its deficiency is at most

\[
a-(\rho a-u)=u-(\rho-1)a\le u/\rho.
\]

The deficiency is integral. \(\square\)

For \(1\le q\le Q\), define

\[
\varepsilon_{q,1}^-
=\max_{\mathcal A\subseteq\mathcal H_{-q}}
\left(
|\mathcal A|-
|N^+_{\mathcal H_{-(q-1)}}(\mathcal A)|
\right)_+,
\]

and define \(\varepsilon_{q,1}^+\) dually. For \(q\ge2\), define
\(\varepsilon_{q,2}^{\pm}\) with two-rank shadows.

### Theorem 2.2 (exact one-bite deficiencies)

\[
\varepsilon_{q,1}^-+\varepsilon_{q,1}^+
\le
2\left\lfloor
u_{q-1}\frac{R_q}{R_{q-1}}
\right\rfloor,
\tag{2.3}
\]

and

\[
\varepsilon_{q,2}^-+\varepsilon_{q,2}^+
\le
2\left\lfloor
u_{q-2}\frac{R_q}{R_{q-2}}
\right\rfloor.
\tag{2.4}
\]

Under (0.2), these imply (0.3)--(0.4).

### Proof

The inclusion graph from rank \(m-q\) to rank \(m-q+1\) has normalized
ratio \(R_{q-1}/R_q\). Exactly \(u_{q-1}\) vertices were removed from its
target row. Lemma 2.1 proves the lower half of (2.3), and complementation
proves the upper half. The two-step graph proves (2.4).

For \(q\ge2\),

\[
u_{q-1}\frac{R_q}{R_{q-1}}
=kc_{q-1}\frac{R_q}{R_{q-1}}
\le\frac{kR_q}{P}.
\]

At \(q=1\), use \(u_0=kL\) and \(L\le W/P\). Summing proves (0.3).
The same calculation with \(q-2\) proves (0.4). \(\square\)

The exact central ratio satisfies

\[
\frac{R_q}{W}
=\prod_{i=1}^q\frac{m-i+1}{m+i}
\le
\exp\left(-\frac{q^2}{m+Q}\right)
\qquad(q\le Q).
\tag{2.5}
\]

Indeed, apply \(\log(1-x)\le-x\) and
\(\sum_{i=1}^q(2i-1)=q^2\). Therefore

\[
\sum_{q=1}^Q R_q
\le
W\sum_{q\ge1}e^{-q^2/(m+Q)}
\le
\frac{\sqrt\pi}{2}W\sqrt{m+Q}.
\tag{2.6}
\]

If \(k/P\le C/m\), then

\[
E_1,E_2
\le(C\sqrt\pi+o(1))\frac{W}{\sqrt m}.
\tag{2.7}
\]

Matching adjacent residual rows toward the middle gives an actual
inclusion-chain cover with at most

\[
|\mathcal H_0|+E_1
\le
W-u_0+\frac{2k}{P}\sum_{q=1}^Q R_q
\tag{2.8}
\]

components. This is genuine structural information about the complement,
but it is still of order \(W\) after one bite.

### Proposition 2.3 (low-run deadline realization on one grid)

Fix one cyclically ordered trajectory. Let \(B\) be the number of phases
having a finite first-block depth, and suppose the deadline inequalities
\(B_q\le d_q\) hold. There is a legal priority assignment for which, at
every depth \(q\), both the claimed phase set and its complement have at
most

\[
\boxed{2B+1}
\tag{2.9}
\]

cyclic phase runs.

### Proof

By deadline Hall, assign the \(B\) blocked phases injectively to legal
slots, each no later than its deadline. Fill the remaining slots, in
increasing slot order, with the unblocked phases in their physical cyclic
order.

For a fixed \(q\), the unblocked phases appearing in the first \(d_q\)
slots form an initial segment of the cyclic order after the \(B\) blocked
points are deleted. In the original cycle, this is one cyclic interval
with at most \(B\) points removed, hence has at most \(B+1\) runs. The
blocked phases in those slots add at most \(B\) singleton runs. Thus the
low-priority set has at most \(2B+1\) runs. Its cyclic complement, the
claimed phase set, has the same number of boundary pairs and hence no more
runs. \(\square\)

This proposition describes the physical incidence pattern of the claims
made by the bite. It does **not** identify the unclaimed raw cells of that
grid with the global actual holes: another trajectory may contain the same
raw cell, and a missing distinct claim can occur elsewhere. Therefore
(2.9) is useful horizontal structure, but it cannot replace Theorem 2.2
or be counted as a donor-to-hole transport theorem.

## 3. Exact rotor cone identity

Write a quotient state as

\[
\omega=(L;z_1,\ldots,z_{2Q};R),
\qquad |L|=m-Q,\quad |R|=H-Q.
\]

Its protected saturated column is

\[
F_d(\omega)
=L\cup\{z_1,\ldots,z_{Q+d}\},
\qquad -Q\le d\le Q.
\tag{3.1}
\]

A legal update with \(x\in L\), \(y\in R\) is

\[
\omega'
=(L-x+y;x,z_1,\ldots,z_{2Q-1};R-y+z_{2Q}).
\tag{3.2}
\]

### Theorem 3.1 (cone law and converse)

The columns \(C_d=F_d(\omega)\) and \(C'_d=F_d(\omega')\) satisfy (0.5).
Conversely, suppose two saturated chains satisfy (0.5) for

\[
x\in C_{-Q},\qquad y\notin C_Q,
\]

and both lie in a common \(M\)-set \(U\). They are the columns of two
consecutive legal quotient-rotor states in \(U\).

### Proof

The new bottom core is \(C_{-Q}-x+y\). For \(d>-Q\),

\[
\begin{aligned}
F_d(\omega')
&=L-x+y+\{x,z_1,\ldots,z_{Q+d-1}\}\\
&=L+\{z_1,\ldots,z_{Q+d-1}\}+y\\
&=F_{d-1}(\omega)+y.
\end{aligned}
\]

Conversely, recover the collar from the singleton increments of the first
chain, take core \(C_{-Q}\), and tail \(U\setminus C_Q\). The assumptions
put \(x\) in the core and \(y\) in the tail. Update (3.2) then gives the
second chain exactly. \(\square\)

### Corollary 3.2 (exact literal block criterion)

Inclusion chains

\[
\mathscr D_0,\ldots,\mathscr D_{r-1}
\]

of actual holes occupy the successive columns of one radius-\(Q\) rotor
block if and only if they have saturated extensions \(C^t\supseteq
\mathscr D_t\) in a common top satisfying (0.5) successively. When this
holds, the audited rotor compiler gives exact literal length

\[
\boxed{r+2Q+1.}
\tag{3.3}
\]

Thus \(r=\Theta(Q)\) is precisely the desired \(O(Q)\)-cost batching.

## 4. Grid-strip geometry

For a buffered geodesic let

\[
G_{i,j}
=C\cup\{a_{i+1},\ldots,a_g\}
 \cup\{b_1,\ldots,b_j\}.
\tag{4.1}
\]

At phase \(t\), the signed-depth-\(d\) flag is

\[
\boxed{F_d(t)=G_{t-d,t}.}
\tag{4.2}
\]

Thus

\[
F_d(t+1)=F_d(t)-a_{t-d+1}+b_{t+1},
\tag{4.3}
\]

and

\[
F_d(t+1)=F_{d-1}(t)+b_{t+1}.
\tag{4.4}
\]

The middle owners are

\[
X_t=G_{t,t}
=C\cup\{a_{t+1},\ldots,a_g\}
 \cup\{b_1,\ldots,b_t\},
\]

so

\[
X_{t+1}=X_t-a_{t+1}+b_{t+1},
\qquad
d_J(X_s,X_t)=|t-s|.
\tag{4.5}
\]

The product-grid increments also obey

\[
G_{i,j+1}\setminus G_{i,j}=\{b_{j+1}\}
\quad\text{independently of }i,
\tag{4.6}
\]

\[
G_{i-1,j}\setminus G_{i,j}=\{a_i\}
\quad\text{independently of }j.
\tag{4.7}
\]

Equations (4.6)--(4.7), with one common bottom cell, the displayed rank
increments, and pairwise distinct \(a\)- and \(b\)-edge labels, are
sufficient to label a filled rectangle as a two-chain grid. Every
elementary square must therefore be a commuting Boolean diamond with
equal labels on opposite parallel edges. Separate SCD chains do not
impose these cross-chain identities.

## 5. Exact diagonal embedding of one parity chain

### Theorem 5.1

Let

\[
S_0\subset S_1\subset\cdots\subset S_{r-1},
\qquad |S_s|=m+d_0+2s,
\]

where

\[
-Q\le d_0,\qquad d_0+2(r-1)\le Q.
\]

For all sufficiently large \(m\), this chain is exposed at \(r\)
consecutive phases of one buffered geodesic rotor chunk. One may take

\[
g=2Q+r-1\le3Q,\qquad t_s=Q+s,
\]

and arrange

\[
\boxed{S_s=F_{d_0+2s}(t_s).}
\tag{5.1}
\]

The literal word length is \(r+2Q+1\le3Q+2\).

### Proof

Put

\[
i_s=t_s-(d_0+2s)=Q-d_0-s,
\qquad j_s=t_s=Q+s.
\]

Then

\[
(i_{s+1},j_{s+1})=(i_s-1,j_s+1)
\]

and

\[
G_{i_{s+1},j_{s+1}}
=G_{i_s,j_s}\cup\{a_{i_s},b_{j_s+1}\}.
\tag{5.2}
\]

Orient the two elements of \(S_{s+1}\setminus S_s\) as
\(a_{i_s}\) and \(b_{j_s+1}\). Partition \(S_0\) among

\[
C,\qquad \{a_{i_0+1},\ldots,a_g\},
\qquad \{b_1,\ldots,b_Q\}.
\]

The required count is

\[
(m-g)+(g-i_0)+Q=m+d_0=|S_0|.
\]

The labels already assigned are exactly the \(m+d_0\) elements of \(S_0\)
and the \(2(r-1)\) elements of \(S_{r-1}\setminus S_0\). Thus they are
exactly all \(m+d_0+2(r-1)=m+d_{r-1}\) elements of \(S_{r-1}\).
There remain

\[
M-|S_{r-1}|=H-d_{r-1}
\]

slots inside the carrier, while

\[
|[2m]\setminus S_{r-1}|=m-d_{r-1}\ge H-d_{r-1}.
\]

Fill all remaining \(a\)- and \(b\)-positions and \(R\) from this
complement. The block sizes are

\[
|C|=m-g,\qquad |R|=H-g.
\]

Since \(Q=o(H)\), we have \(g\le3Q<H\) eventually. Hence

\[
U=C\mathbin{\dot\cup}\{a_1,\ldots,a_g\}
 \mathbin{\dot\cup}\{b_1,\ldots,b_g\}
 \mathbin{\dot\cup}R
\]

is an \(M\)-carrier. Equations (5.1)--(5.2) now follow inductively.
The choice \(g=r+2Q-1\) supplies the two \(Q\)-phase buffers. \(\square\)

This construction uses one phase for each member of one inclusion chain.
One saturated state column could already cover that chain. Thus it does
not provide the desired factor-\(Q\) batching of \(Q\) different chain
components; it only audits the horizontal formula exactly.

## 6. Sharp local incompatibility

### Proposition 6.1 (same-rank singleton criterion)

For distinct

\[
S,T\in\binom{[2m]}{m+d},
\]

there are consecutive rotor columns having rank-\(m+d\) flags \(S,T\)
if and only if \(d_J(S,T)=1\).

### Proof

For \(d>-Q\), write

\[
C_d=C_{d-1}+z,\qquad C'_d=C_{d-1}+y
\]

using (0.5). Since \(y\notin C_d\),

\[
T=S-z+y,
\]

so \(d_J(S,T)=1\). At \(d=-Q\), the bottom identity in (0.5) gives the
same result.

Conversely, write \(T=S-z+y\). Choose a saturated chain through \(S\)
whose increment into rank \(m+d\) is \(z\) when \(d>-Q\); for
\(d=-Q\), put \(x=z\) in the bottom core. Extend above \(S\) without
using \(y\), choose an \(M\)-carrier containing the top and \(y\), and
apply Theorem 3.1. \(\square\)

Consequently, if residual chains containing prescribed middle owners
\(X_0,\ldots,X_{r-1}\) occupy one geodesic block, then

\[
d_J(X_s,X_t)=|s-t|.
\]

Pairwise same-rank Johnson adjacency is still not sufficient for a full
block: all ranks must use the common arrival tokens in (0.5), equivalently
the equal opposite-edge labels in (4.6)--(4.7).

## 7. Proved/conditional boundary

The following are proved:

1. the actual one-bite width sandwich (0.1);
2. actual adjacent and two-step deficiency \(O(W/\sqrt m)\);
3. the necessary-and-sufficient cone criterion for a literal block;
4. monotone Johnson-geodesic owner necessity in a grid block.

The missing theorem is:

> Choose the actual-hole deficient-Hall chain cover so that its components
> split into \(O(B/Q)\) cone-compatible runs, where \(B\) is the number of
> chain components at the relevant sparse residual scale.

The one-bite shadow estimate supplies vertical chains but does not supply
this horizontal geodesic low-run coloring. This is the precise surviving
gate.
