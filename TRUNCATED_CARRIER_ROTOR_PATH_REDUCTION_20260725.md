# Truncated carrier-rotor paths at the crossing scale

## 0. Outcome

The full cyclic top packet is more rigid than the hard-band transfer needs.
Let

\[
k=2m,\qquad W=\binom{2m}{m},\qquad
N_q=\binom{2m}{m-q}.
\]

Choose the first crossing height \(H\) with

\[
\frac{W}{N_H}\ge M:=m+H,
\]

so

\[
H=(1+o(1))\sqrt{m\log m},\qquad
MN_H=W-o(W),\qquad HN_H=o(W).
\]

Let

\[
Q=\left\lceil\sqrt{m(\log\log m+\gamma(m))}\right\rceil,
\qquad
\gamma\to\infty,\qquad \gamma=o(\log\log m).
\]

Then \(Q=o(H)\).  The ranks deeper than \(Q\) can already be handled by
the sparse full-packet reservoir.  Consequently the primary construction
may use **radius-\(Q\) rotor paths inside an \(M\)-carrier**, rather than a
full radius-\(H\) cyclic packet.

This strictly enlarges the available atom family while preserving the
width-scale word ledger.  It gives a new sufficient theorem, but the final
integral path selection remains open.

## 1. The induced carrier rotor

Fix a carrier

\[
U\in\binom{[2m]}M.
\]

A carrier quotient-state is

\[
\omega=(L;z_1,\ldots,z_{2Q};R_U),                    \tag{1.1}
\]

where

\[
|L|=m-Q,\qquad |R_U|=H-Q,
\]

and

\[
L,\{z_1\},\ldots,\{z_{2Q}\},R_U
\]

partition \(U\).  In the full ordered-partition state on \([2m]\), these
data specify the exact prefix

\[
L,\{z_1\},\ldots,\{z_{2Q}\}
\]

and only the union of the unresolved tail blocks, namely

\[
R=R_U\cup([2m]\setminus U).
\]

For \(x\in L\) and \(y\in R_U\), append the nonempty mask

\[
L-x+y.
\]

The exact MTF recurrence gives a successor whose displayed prefix and tail
union are

\[
\mathcal R_{x,y}(\omega)
=
(L-x+y;\ x,z_1,\ldots,z_{2Q-1};\ R_U-y+z_{2Q}).       \tag{1.2}
\]

The internal tail partition need not remain one block and is not part of
the quotient-state.  The recurrence depends only on its union, so paths
compose exactly and the carrier remains fixed.  Every quotient-state has

\[
(m-Q)(H-Q)                                             \tag{1.3}
\]

successors and the same number of predecessors.

The number of carrier states is

\[
|\Omega_Q(U)|
=\frac{M!}{(m-Q)!(H-Q)!}.                              \tag{1.4}
\]

The same slot-cycle argument as for the equal-sided rotor proves strong
connectivity whenever \(m-Q\ge2\) and \(H-Q\ge2\).  Indeed a move is the
slot cycle

\[
(a_i,q_1,\ldots,q_{2Q},b_j),
\]

and, modulo internal permutations of the \(a\)- and \(b\)-slots, two such
cycles generate a transposition between an \(a\)-slot and \(q_1\).  Its
conjugates and the internal symmetric groups generate all slot
permutations.  Regular weak connectivity then implies strong connectivity.

## 2. Exact flag column

The state (1.1) exposes the saturated chain

\[
L\subset L+z_1\subset\cdots\subset L+z_1+\cdots+z_{2Q}.
\]

Its middle owner is

\[
X(\omega)=L+z_1+\cdots+z_Q.                            \tag{2.1}
\]

For \(0\le q\le Q\), define

\[
L_q(\omega)=L+z_1+\cdots+z_{Q-q},                     \tag{2.2}
\]

\[
U_q(\omega)=L+z_1+\cdots+z_{Q+q}.                     \tag{2.3}
\]

These have ranks \(m-q\) and \(m+q\), respectively.

Under (1.2), the middle owner changes by

\[
X' = X-z_Q+y.                                          \tag{2.4}
\]

Conditioned on a uniform carrier state with owner \(X\), and then on a
uniform rotor edge, the next owner is uniform among the \(mH\) Johnson
neighbors of \(X\) inside \(U\): for

\[
Y=X-a+b,qquad a\in X,\ b\in U\setminus X,
\]

one has exactly

\[
\Pr(X'=Y\mid X)=\frac1m\frac1H.                       \tag{2.5}
\]

Indeed \(z_Q\) is uniform in \(X\), while the chosen \(y\) is uniform in
\(U\setminus X\).  Likewise, conditioned on \(X\), the lower deletion
flag and upper addition flag are uniform ordered flags inside \(X\) and
\(U\setminus X\).

This is much more flexible than a cyclic packet: after a state is fixed,
there are \((m-Q)(H-Q)\) legal continuations rather than one.

## 3. Literal word for one path

Let

\[
\omega_0,\omega_1,\ldots,\omega_{s-1}
\]

be a directed carrier-rotor path.  Initialize \(\omega_0\) by taking the
unresolved tail as one block and writing the resulting blocks in reverse
state order:

\[
R,\{z_{2Q}\},\ldots,\{z_1\},L.
\]

This costs \(2Q+2\) nonempty entries.  For each subsequent rotor edge,
append the new core mask \(L-x+y\).  The resulting literal nonzero word has
length

\[
s+2Q+1,                                                \tag{3.1}
\]

and, at its \(s\) state endpoints, exposes every flag (2.2)--(2.3).

Take one path with

\[
s=M
\]

states in every carrier \(U\in\binom{[2m]}M\).  The total primary length is

\[
MN_H+(2Q+1)N_H
=W-o(W)+O(QW/m)
=W+o(W).                                               \tag{3.2}
\]

No cyclic closure, full-depth pin, or radius-\(H\) initialization is used.

## 4. Exact occurrence loads

Choose the start state uniformly in \(\Omega_Q(U)\), and at every step
choose a uniform rotor successor.  By regularity, every time marginal is
uniform on \(\Omega_Q(U)\).

For any controlled rank \(r=m\pm q\), \(0\le q\le Q\), the rank-\(r\)
member of a uniform state is uniform in \(\binom Ur\).  Hence a fixed
target \(S\in\binom{[2m]}r\) has expected total primary multiplicity

\[
\binom{2m-r}{M-r}\frac{M}{\binom Mr}
=\frac{MN_H}{\binom{2m}r}.                             \tag{4.1}
\]

Thus the family has the exact symmetric occurrence-mass load

\[
\lambda_r^{\rm prim}=\frac{T}{N_r},
\qquad T:=MN_H=W-o(W),                                 \tag{4.2}
\]

at every hard rank, with the entire nested flag column kept intact.

Equation (4.2) counts phase occurrences.  It is not by itself an ordinary
support-incidence fractional cover, because one path may revisit a target.
The open theorem below asks for support coverage and therefore includes
control of these self-collisions.

The occurrence owner load is \(T/W=1-o(1)\).  Independent stationary paths
still leave at least \((e^{-1}-o(1))W\) middle owners uncovered.  The
integrality problem is
to choose one actual length-\(M\) path per carrier so that the union of
owners and hard flags loses only \(o(W)\) targets in total.

## 5. Outer reservoir and tails

Use the already audited full cyclic-packet reservoir for the ranks

\[
Q<q\le H.
\]

Put

\[
\varepsilon=e^{-\gamma/2},\qquad
R_{\rm res}=\left\lceil\varepsilon W/M\right\rceil.
\]

For \(Q<q<H\), a fixed rank-\((m\pm q)\) target is hit by a uniform full
packet with probability \(M/N_q\).  Therefore the expected number of
targets missed by all reservoir packets at these proper packet ranks is at
most

\[
\sum_{q=Q+1}^{H-1}N_q
\left(1-\frac{M}{N_q}\right)^{R_{\rm res}}
=o(W),                                                 \tag{5.1}
\]

because

\[
\varepsilon\frac{W}{N_Q}
\ge \log m\,e^{\gamma/2-o(1)}.
\]

At upper depth \(H\), all \(M\) phases of a full packet expose the same
carrier \(U\), so the hit probability is \(1/N_H\), not \(M/N_H\).  Append
all rank-\((m+H)\) carriers literally; this costs

\[
N_H=O(W/m)=o(W).                                       \tag{5.2}
\]

The reservoir's literal cost is

\[
R_{\rm res}(M+O(H))=o(W).                              \tag{5.3}
\]

Finally, the two tails beyond the crossing height have total literal cost

\[
2\sum_{q>H}N_q=O(W/H)=o(W).                            \tag{5.4}
\]

## 6. Exact sufficient theorem

### Truncated carrier-rotor path theorem (open)

For the parameters above, choose one directed path of \(M\) states in
\(\Omega_Q(U)\) for every carrier \(U\in\binom{[2m]}M\), so that

\[
\sum_{q=0}^{Q}
\left(
N_q-\left|\{L_q(\omega):\omega\text{ selected}\}\right|
+N_q-\left|\{U_q(\omega):\omega\text{ selected}\}\right|
\right)
=o(W),                                                 \tag{TRP}
\]

with the duplicated \(q=0\) term counted only once.

Then

\[
\nu(2m)\le W+o(W).
\]

#### Proof

Compile the primary paths by Section 3.  Append the reservoir of Section 5,
then append the remaining missing hard-band masks and the two outer tails
literally.  Equations (3.2), (5.1)--(5.4), and (TRP) give total length
\(W+o(W)\).  Every entry is nonempty, and concatenation preserves all
internal witnesses.  \(\square\)

The standard one-bit lift transfers the conclusion to odd dimensions.

## 7. What changed, and what did not

The cyclic crossing-packet theorem chooses one cyclic order per carrier.
Such a packet has only two orientations after its owner family is fixed.
The truncated carrier rotor instead uses the entire strongly connected
state graph (1.1)--(1.3), with \((m-Q)(H-Q)\) legal choices at every step.
Every cyclic hard-band packet is a special case, so (TRP) is a strictly
weaker selection target.

Independent choices still have Poisson-scale holes and do not prove (TRP).
The remaining theorem is still correlated and integral.  The gain is that
the primary atom no longer carries the unused depths \(Q<q\le H\), and the
dynamic choice space is no longer frozen by one cyclic order.

The automorphism-overlay use of this dynamic choice space is audited in
`MATH_ATTACK_TRUNCATED_CARRIER_ROTOR_ACD_20260725.md`. The exact delayed
owner law forces

\[
x_t=X_{t+Q}\setminus X_{t+Q+1}.
\]

Moreover every nonendpoint flag is an intersection or union of a
consecutive owner path. Consequently two lifts of the same owner sequence
have only \(O(q)\) discrepancy at depth \(q\), hence only \(O(Q^2)\) over
the truncated band. Thus the large rotor outdegree does not by itself give
macroscopic shallow descent. A successful overlay component must globally
rethread \(\Theta(M)\) owner-successor arcs per active carrier at depth one;
the resulting two-factor rotor rethreading lemma remains open.

The independent audit, including the tail-union interpretation, endpoint
repair, exact trajectory embedding, and ABKV obstruction, is recorded in
`TRUNCATED_CARRIER_ROTOR_PATH_REDUCTION_CROSS_AUDIT_20260725.md`.
