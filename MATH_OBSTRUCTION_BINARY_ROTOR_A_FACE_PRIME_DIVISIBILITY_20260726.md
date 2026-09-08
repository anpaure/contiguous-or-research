# Binary-rotor LP dual, prime-divisibility obstruction, and the exact mixed-face boundary

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or external
input is used.

## 0. Outcome

Let

\[
n=2m+1,\qquad W=\binom{n}{m},\qquad D=m!(m+1)!,
\]

and let \(A\) and \(B\) be the left rotations of respectively the first
\(n-1=2m\) positions and all \(n\) positions of a permutation state.
This note audits the nonsymmetric binary-rotor LP in
MATH_THEOREM_ANTI_DIHEDRAL_NESTED_UCYCLE_GAUSSIAN_RETHREADING_20260726.md.

There are four exact conclusions.

1. The real owner--flow--two-sided-prefix LP has the explicit Farkas dual
   in Theorem 2.1. It has no Farkas obstruction: the uniform circulation
   satisfies every prefix inequality. At depth
   \(q=A_0\sqrt m+O(1)\), its exact target multiplicity is
   \(\exp(A_0^2+o_{A_0}(1))\).

2. If flow is deleted, there is an integral one-state-per-owner
   transversal satisfying both prefix systems at all depths. Any symmetric
   chain decomposition supplies one.

3. Circulation nevertheless has a genuine integral gap. On the \(A\)-only
   support face the uniform fractional point remains feasible at every
   depth, but for every odd prime \(m=p\) there is no Boolean
   owner-transversal circulation: an integral \(A\)-circulation is a union
   of \(2p\)-orbits, whereas

   \[
   \binom{2p+1}{p}\equiv2\pmod p.
   \]

4. This obstruction is only to the pure face. Any Boolean circulation
   with \(C=o(W/m)\) components must use

   \[
   a\ge \frac{W}{2m+1}-o(W/m),\qquad
   b\ge \frac{W}{2m}-o(W/m)                 \tag{0.1}
   \]

   \(A\)-arcs and \(B\)-arcs, respectively. Thus a viable rounding must
   live genuinely inside the mixed face.

No full mixed-system obstruction and no coefficient-one theorem is
claimed.

## 1. Exact primal system

For \(\pi=(x_1,\ldots,x_n)\in S_n\), write

\[
X(\pi)=\{x_1,\ldots,x_m\}.
\]

For \(0\le q\le H\le m-1\), put

\[
L_q(\pi)=\{x_1,\ldots,x_{m-q}\},\qquad
U_q(\pi)=\{x_1,\ldots,x_{m+1+q}\}.          \tag{1.1}
\]

Let \(z_{\pi,g}\ge0\), \(g\in\{A,B\}\), be the mass on
\(\pi\to g\pi\). The constraints are

\[
\sum_{\pi:X(\pi)=X}\sum_gz_{\pi,g}=1
\quad\left(X\in\binom{[n]}m\right),         \tag{1.2}
\]

\[
\sum_gz_{\pi,g}-\sum_gz_{g^{-1}\pi,g}=0
\quad(\pi\in S_n),                          \tag{1.3}
\]

\[
\sum_{\pi:L_q(\pi)=S}\sum_gz_{\pi,g}\ge1
\quad\left(S\in\binom{[n]}{m-q}\right),     \tag{1.4}
\]

\[
\sum_{\pi:U_q(\pi)=T}\sum_gz_{\pi,g}\ge1
\quad\left(T\in\binom{[n]}{m+1+q}\right).   \tag{1.5}
\]

For Boolean \(z\), (1.2)--(1.3) select one state over every middle owner
and make the selected arcs a disjoint union of directed rotor cycles.

## 2. Complete Farkas dual and Gaussian margin

Give (1.2) free variables \(\alpha_X\), (1.3) free potentials
\(\phi_\pi\), and (1.4)--(1.5) nonnegative variables
\(\lambda^-_{q,S},\lambda^+_{q,T}\). Define

\[
w(\pi)=\sum_{q=0}^H
\left(\lambda^-_{q,L_q(\pi)}+\lambda^+_{q,U_q(\pi)}\right). \tag{2.1}
\]

### Theorem 2.1 (Farkas alternative)

The real system (1.2)--(1.5) is feasible if and only if every dual tuple
satisfying

\[
\boxed{\alpha_{X(\pi)}+\phi_\pi-\phi_{g\pi}\ge w(\pi)
\quad(\pi\in S_n,\ g\in\{A,B\})}            \tag{2.2}
\]

also satisfies

\[
\boxed{\sum_X\alpha_X\ge
\sum_{q=0}^H\left(\sum_S\lambda^-_{q,S}
+\sum_T\lambda^+_{q,T}\right).}             \tag{2.3}
\]

#### Proof

Multiply (2.2) by \(z_{\pi,g}\) and sum. Equation (1.2) turns the owner
term into \(\sum_X\alpha_X\), and (1.3) cancels the potential terms.
The cover inequalities give (2.3). Conversely, this is the standard
Farkas alternative for the equalities (1.2)--(1.3), inequalities
(1.4)--(1.5), and \(z\ge0\). \(\square\)

There are exactly

\[
D=m!(m+1)!                                  \tag{2.4}
\]

states above each owner. A fixed lower or upper target at paired depth
\(q\) is the prefix set of exactly

\[
(m-q)!(m+1+q)!                              \tag{2.5}
\]

states.

Give every \(A\)-arc weight \(1/D\) and every \(B\)-arc weight zero.
Since \(A\) permutes \(S_n\), this is a circulation, and each owner has
mass one. Every paired target at depth \(q\) has load

\[
\rho_q=
\frac{(m-q)!(m+1+q)!}{m!(m+1)!}
=\frac{W}{\binom n{m-q}}
=\prod_{j=0}^{q-1}\frac{m+2+j}{m-j}.        \tag{2.6}
\]

Thus \(\rho_0=1\) and \(\rho_q>1\) for \(q>0\). The same statement holds
on the \(B\)-only face and for every common convex mixture.

For fixed \(A_0<\infty\), uniformly for \(q\le A_0\sqrt m\),

\[
\boxed{\log\rho_q=\frac{q(q+1)}m+O_{A_0}(m^{-1/2}).} \tag{2.7}
\]

Indeed

\[
\log\frac{m+2+j}{m-j}
=\log\left(1+\frac{2j+2}{m-j}\right);
\]

the sum of the linear terms is
\(q(q+1)/m+O(q^3/m^2)\), and the sum of their squares is
\(O(q^3/m^2)\). Hence

\[
q=A_0\sqrt m+O(1)\quad\Longrightarrow\quad
\rho_q=e^{A_0^2+o_{A_0}(1)}.                \tag{2.8}
\]

Multiplying (2.2) by the uniform \(A\)-circulation proves the stronger
dual inequality

\[
\boxed{\sum_X\alpha_X\ge
\sum_{q=0}^H\rho_q
\left(\sum_S\lambda^-_{q,S}+\sum_T\lambda^+_{q,T}\right).} \tag{2.9}
\]

Therefore no real Farkas separator exists, even on the \(A\)-only face.
At depth one the exact extra margin is

\[
\rho_1-1=\frac2m,                            \tag{2.10}
\]

while a positive Gaussian depth has constant margin. Any obstruction
must use integrality.

## 3. Integral static resolution of both prefix systems

### Theorem 3.1 (symmetric-chain state transversal)

For every \(0\le H\le m-1\), there is
\(\mathcal T\subset S_n\) containing exactly one state over each middle
owner and satisfying both cover systems (1.4)--(1.5).

#### Proof

Fix a symmetric-chain decomposition of \(2^{[n]}\). Every chain is

\[
C_a\subset C_{a+1}\subset\cdots\subset C_{n-a},
\qquad |C_r|=r,\qquad a\le m.               \tag{3.1}
\]

It contains a unique rank-\(m\) set \(X_C=C_m\), and the chains are in
bijection with the middle sets.

Order the elements of \(C_a\) arbitrarily in positions \(1,\ldots,a\).
For \(a<r\le m\), put the unique element of
\(C_r\setminus C_{r-1}\) in position \(r\). Do the same for
\(m<r\le n-a\), and order the remaining \(a\) elements arbitrarily at
the end. The resulting permutation \(\pi_C\) satisfies

\[
X(\pi_C)=X_C,\qquad
\{(\pi_C)_1,\ldots,(\pi_C)_r\}=C_r
\quad(a\le r\le n-a).                       \tag{3.2}
\]

Put \(\mathcal T=\{\pi_C:C\text{ a chain}\}\). A target of rank
\(r=m-q\) belongs to a chain beginning at some \(a\le r\), so the
corresponding state has that target as its lower prefix. A target of rank
\(n-r=m+1+q\) lies on a chain beginning at \(a\le r\), and that chain
ends at \(n-a\ge n-r\), so its state has the target as its upper prefix.
Both signs and all depths are therefore covered. \(\square\)

For a fixed transversal \(\mathcal T\), circulation has an exact Hall
form. Make left and right copies of \(\mathcal T\), and join \(\pi\) on
the left to \(g\pi\) on the right when \(g\pi\in\mathcal T\). It supports
a rotor circulation exactly when

\[
\boxed{|N_{\mathcal T}(Q)|\ge|Q|
\quad(Q\subseteq\mathcal T).}               \tag{3.3}
\]

Theorem 3.1 does not assert (3.3). It proves that the missing obstruction
must couple chronology to prefix resolution; owner capacity and the two
prefix signs alone are integrally feasible.

## 4. Integral obstruction on the \(A\)-only face

### Theorem 4.1 (prime-divisibility obstruction)

Let \(m=p\) be an odd prime. There is no Boolean solution of
(1.2)--(1.3) supported only on \(A\)-arcs. Consequently there is no such
solution with the prefix constraints, for any \(H\), even though the
uniform \(A\)-only fractional point satisfies all of them.

#### Proof

On this face put \(y_\pi=z_{\pi,A}\in\{0,1\}\). Flow conservation is

\[
y_\pi=y_{A^{-1}\pi}.                         \tag{4.1}
\]

Thus the selected state set is a union of \(A\)-orbits. The rotation
\(A\) has order \(2p\), and its action on permutation states is free:
if \(A^d\pi=\pi\), the \(2p\) distinct entries in the rotated positions
force \(2p\mid d\). Every orbit has exactly \(2p\) states.

The owner equations select exactly one state above each of the \(W\)
owners, so the selected set has size

\[
W=\binom{2p+1}{p}.                           \tag{4.2}
\]

Lucas' congruence in base \(p\) gives

\[
\binom{2p+1}{p}\equiv\binom21\binom10
\equiv2\pmod p.                             \tag{4.3}
\]

Hence \(p\nmid W\), contradicting divisibility of a union of
\(2p\)-orbits by \(p\). \(\square\)

This applies in particular to \(H=\lceil A_0\sqrt p\rceil\) once \(p\)
is large. It is a genuine integer-hull cut: on this prime subsequence
every Boolean circulation satisfies

\[
\boxed{\sum_{\pi}z_{\pi,B}\ge1,}             \tag{4.4}
\]

whereas the feasible uniform \(A\)-only fractional point has left side
zero.

There is also a weak mixed parity law. The position permutation \(A\) is
odd and \(B\) is even. The generator word around every selected state
cycle is the identity, so each cycle has an even number of \(A\)-arcs.
If \(a,b\) are the total selected \(A,B\) counts, then

\[
a\equiv0\pmod2,\qquad b\equiv W\pmod2.       \tag{4.5}
\]

This does not give a growing lower bound on \(b\).

## 5. Few components force genuine two-rotor mixing

### Proposition 5.1 (mixed-rotor lower bounds)

Let a Boolean owner-transversal circulation have \(C\) support cycles
and \(a,b\) selected \(A,B\)-arcs. Then

\[
\boxed{a+C\ge\frac Wn,\qquad
b+C\ge\frac W{n-1}.}                        \tag{5.1}
\]

#### Proof

Delete all \(A\)-arcs. A support cycle containing \(k>0\) \(A\)-arcs
breaks into \(k\) directed \(B\)-paths; a pure \(B\)-cycle contributes
one \(B\)-orbit. Since \(B\) has free order \(n\), each path or orbit has
at most \(n\) selected states. There are at most \(a+C\) pieces, whence
\(W\le n(a+C)\).

Deleting all \(B\)-arcs and using the free order-\((n-1)\) action of
\(A\) gives \(W\le(n-1)(b+C)\). \(\square\)

Thus \(C=o(W/m)\) gives exactly (0.1). For comparison, the total excess
over one in either depth-one prefix system is

\[
W-\binom n{m-1}
=W\left(1-\frac m{m+2}\right)
=\frac{2W}{m+2},                             \tag{5.2}
\]

asymptotic to four times \(W/(2m)\). Consequently the mandatory mixed
arc count and scalar depth-one surplus do not contradict each other. A
full obstruction would have to show that mixed rotor arcs consume
structured surplus in at least one sign; plain counting cannot do so.

## 6. Proved boundary

The following are proved:

* the full real Farkas system is feasible, with the exact Gaussian
  multiplicities (2.6)--(2.9);
* both nested prefix systems have an exact integral owner resolution
  before chronology;
* chronology has a genuine integrality gap on the pure \(A\)-face for
  every odd prime \(m\);
* every few-component solution uses \(\Theta(W/m)\) arcs of both rotors.

The remaining problem is an integral transversal satisfying the
cycle-cover Hall inequalities (3.3) and both prefix systems while the
transversal itself may vary. The prime obstruction does not extend to
that mixed face, and this note makes no constant-one claim.
