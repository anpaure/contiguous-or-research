# Exact bounded Hamming switches: an exponential order bank and its Gaussian obstruction

## 0. Scope and conclusion

Let \(h=2^r\), \(r\ge 3\), and put

\[
 G=\mathbb F_2^h/\langle\mathbf 1\rangle,
 \qquad g_i=\bar e_i,
 \qquad \sum_{i=1}^h g_i=0.
\]

An isometric \(2h\)-cycle in \(Q_h\), folded by antipodes, is a
rainbow \(h\)-cycle in \(G\): its direction word uses every \(g_i\)
exactly once.  This note proves the following two facts.
Throughout, a cyclic word is oriented and is taken modulo rotation,
but not modulo reversal.  Reversal has no effect on the interval-support
obstruction proved below.

1. Starting from a parallel quotient-Hamming tiling, there is an exact
   bank of switches, each involving at most eight rainbow tiles, which
   produces a vertex factor containing \(2^{h/8}\) distinct cyclic
   direction words, all with the same multiplicity.
2. This exponential diversity is nevertheless useless for Gaussian
   \(q\)-covering.  A fixed four-to-one direction class has two members
   in every consecutive eight-position packet.  Consequently every
   supported \(q\)-set \(S\) satisfies

   \[
                 \bigl||S\cap I|-q/4\bigr|\le 4.
   \]

   For \(q\to\infty\), \(q\le A\sqrt h\), the proportion of all
   \(q\)-sets satisfying this is at most
   \(18e^{A^2}/\sqrt q\).  Thus this bounded, positive-density switch
   bank covers only \(o(1)\), rather than \(1-o(1)\), of the direction
   \(q\)-sets at Gaussian depth.

The second statement is an obstruction only to the constructed
port-preserving packet orbit.  It is not an invariant of every possible
switch out of a Hamming factor.  It pinpoints the missing operation:
one must transport direction mass between separated packets or change
the packet frame at growing scales.

## 1. The general quotient-Hamming packet switch

Let

\[
             L:G\longrightarrow Y:=\mathbb F_2^r
\]

be onto, and set \(K=\ker L\).  Thus

\[
        \dim K=h-1-r,
        \qquad |K|=2^{h-1-r}=\frac{2^{h-1}}h.
                                                        \tag{1.1}
\]

A rainbow tile \(T\subseteq G\) is called an \(L\)-transversal if
\(L|_T:T\to Y\) is a bijection.  Write its unique section as

\[
                         s_T:Y\longrightarrow T.
\]

Every \(L\)-transversal gives a parallel Hamming factor:

\[
                         G=\bigsqcup_{k\in K}(k+T).     \tag{1.2}
\]

Indeed, for each \(y\in Y\), the points \(k+s_T(y)\), \(k\in K\),
are exactly the fibre \(L^{-1}(y)\).

### Lemma 1.1 (exact common-subgroup switch)

Let \(T,T'\) be two \(L\)-transversal rainbow tiles, and put

\[
 B(T,T')=
 \left\langle s_T(y)+s_{T'}(y):y\in Y\right\rangle\le K.          \tag{1.3}
\]

Then

\[
                         B(T,T')+T=B(T,T')+T'.          \tag{1.4}
\]

Consequently, for every \(a\in K\), the \(|B(T,T')|\) tiles

\[
                         \{a+b+T:b\in B(T,T')\}
\]

may be replaced exactly by

\[
                         \{a+b+T':b\in B(T,T')\}.
\]

#### Proof

For a fixed \(y\), (1.3) gives

\[
              B+s_T(y)=B+s_{T'}(y).
\]

Taking the disjoint union over \(y\in Y\) proves (1.4).  Translating by
\(a\) proves the switch assertion.  Every tile on both sides remains a
literal rainbow tile; no fractional matching is used. \(\square\)

There is a useful bound on the packet size.  View \(L(T)\) and \(L(T')\)
as labeled Hamilton cycles on the common vertex set \(Y\).  A common
edge is called label-preserving if it carries the same direction \(g_i\)
in both tiles.

### Lemma 1.2 (common-edge component bound)

Suppose deleting \(m\) edges from the labeled cycle \(L(T)\) leaves
only label-preserving common edges of \(L(T)\) and \(L(T')\).  After a
translation of \(T'\) by an element of \(K\),

\[
                         \dim B(T,T')\le m-1.           \tag{1.5}
\]

#### Proof

Put \(d(y)=s_T(y)+s_{T'}(y)\in K\).  If \(yz\) is a label-preserving
common edge carrying \(g_i\), then

\[
 s_T(y)+s_T(z)=g_i=s_{T'}(y)+s_{T'}(z),
\]

so \(d(y)=d(z)\).  The graph obtained from one cycle by deleting \(m\)
edges has at most \(m\) components.  Hence \(d\) takes at most \(m\)
values.  Translating (T') makes one value zero, and the other at most
\(m-1\) values span \(B(T,T')\). \(\square\)

Thus a labeled alternating trade which replaces four old cycle edges
has packet mass at most \(2^3=8\).

## 2. A three-dimensional two-state port gadget

Let \(a,b,c\) be the standard basis of \(\mathbb F_2^3\).  The two
words

\[
                 P^0=(a,c,b,c,a,c,b),
 \qquad          P^1=(b,c,a,c,b,c,a)                  \tag{2.1}
\]

give Hamilton paths from \(0\) to \(c\).  Their vertex sequences are

\[
\begin{aligned}
 P^0:&\quad
 0,a,a+c,a+b+c,a+b,b,b+c,c,\\
 P^1:&\quad
 0,b,b+c,a+b+c,a+b,a,a+c,c.
\end{aligned}                                                   \tag{2.2}
\]

Both use two \(a\)-directions, two \(b\)-directions and three
\(c\)-directions.  Give the three common \(c\)-edges

\[
 \{a,a+c\},\qquad
 \{a+b,a+b+c\},\qquad
 \{b,b+c\}                                             \tag{2.3}
\]

the same three actual direction labels in both paths.  Assign the two
actual \(a\)-labels and the two actual \(b\)-labels bijectively to the
remaining edges of the corresponding type.  The two paths then use the
same seven actual directions, have the same ports, and differ in exactly
four old labeled edges.

## 3. Concatenating (h/8) independent gadgets

Put

\[
                         M=2^{r-3}=h/8.                \tag{3.1}
\]

Write

\[
                         Y=\mathbb F_2^3\times Z,
 \qquad                 Z=\mathbb F_2^{r-3}.
\]

For \(r\ge5\), take a cyclic Gray order
\(z_0,z_1,\ldots,z_{M-1}\) of \(Z\).  For \(r=4\), use
\(z_0=0,z_1=1\), with the sole high direction used on both closing
connections.  For \(r=3\), there is one fibre and the edge from \(c\)
back to \(0\) closes it.

For \(r\ge4\), traverse the fibre
\(\mathbb F_2^3\times\{z_j\}\) from \(0\) to \(c\) when \(j\) is even,
and from \(c\) to \(0\) when \(j\) is odd.  Between consecutive fibres,
use the unique high-coordinate edge from the ending port in fibre \(j\)
to the same port in fibre \(j+1\).  Since \(M\) is even, the closing
ports also agree.  This is a Hamilton cycle on \(Y\).

In each fibre choose independently \(P^0\) or \(P^1\), reversing the
chosen path in the odd fibres.  For

\[
                         \omega\in\mathbb F_2^M
\]

write \(C_\omega\) for the resulting Hamilton cycle.  All \(C_\omega\)
have the same transition-direction multiset.

Assign the \(h\) actual directions \(g_1,\ldots,g_h\) bijectively to the
edges of \(C_0\), respecting the transition types.  In a switched fibre
use the relabeling described after (2.3); all directions outside that
fibre keep their labels.  Since the transition labels around \(C_0\)
xor to zero, the assignment

\[
                         g_i\longmapsto L(g_i)
\]

extends uniquely to a linear map \(L:G\to Y\): the only relation among
the \(g_i\) is \(\sum_i g_i=0\).  It is onto because the transition
types span \(Y\).  Every \(C_\omega\) therefore lifts to an
\(L\)-transversal rainbow tile \(T_\omega\).
Choose these lifts coherently: start every syndrome cycle at the common
first fibre port and take its initial prefix in \(G\) to be \(0\).

For the switch in fibre \(j\), let

\[
 B_j=\left\langle
       s_{T_0}(y)+s_{T_{e_j}}(y):y\in Y
     \right\rangle\le K.                              \tag{3.2}
\]

The two cycles differ in four old labeled edges.  The three internal
common components are (2.3), while the rest of the global cycle joins
the two ports into a fourth component.  Lemma 1.2 gives

\[
                         \dim B_j\le3.                 \tag{3.3}
\]

Moreover the two gadget states use exactly the same actual direction
set.  Hence, after leaving the fibre, their prefix sums agree again.
Thus there are functions \(d_j:Y\to B_j\), supported in the interior of
fibre \(j\), such that

\[
 s_{T_\omega}(y)=
 \begin{cases}
  s_{T_0}(y)+\omega_jd_j(y),&y\text{ lies in fibre }j,\\
  s_{T_0}(y),&y\text{ is on no switched fibre interior}.
 \end{cases}                                          \tag{3.4}
\]

Only one line of (3.4) can be active at a given \(y\).

## 4. Exact context-dependent ownership

Set

\[
                         B=B_1+\cdots+B_M.
\]

By (3.3),

\[
                         \dim B\le3M=3h/8.             \tag{4.1}
\]

Let \(B^\perp\le K^*\) be its annihilator.  From (1.1),

\[
 \dim B^\perp
 \ge h-1-r-3h/8
 \ge h/8=M,                                           \tag{4.2}
\]

where the last inequality is equivalent to \(h/2\ge r+1\), valid for
all \(h=2^r\), \(r\ge3\).  Choose linearly independent

\[
                         \lambda_1,\ldots,\lambda_M\in B^\perp.
                                                                    \tag{4.3}
\]

For \(k\in K\), define

\[
 \omega(k)=\bigl(\lambda_1(k),\ldots,\lambda_M(k)\bigr),
 \qquad
                         \mathcal T_k=k+T_{\omega(k)}. \tag{4.4}
\]

### Theorem 4.1 (exponential exact switch factor)

The tiles \(\{\mathcal T_k:k\in K\}\) partition \(G\).  Their lifts are
a vertex \(2\)-factor of \(Q_h\) into isometric \(2h\)-cycles.  Every one
of the \(2^M=2^{h/8}\) cyclic order words occurs exactly

\[
                         2^{\dim K-M}                  \tag{4.5}
\]

times.

#### Proof

Fix \(y\in Y\).  If \(y\) is in the interior of fibre \(j\), the point
of \(\mathcal T_k\) above \(y\) is

\[
 s_{T_0}(y)+
 \Phi_y(k),
 \qquad
 \Phi_y(k)=k+\lambda_j(k)d_j(y).                      \tag{4.6}
\]

Because \(d_j(y)\in B_j\le B\) and \(\lambda_j\in B^\perp\),

\[
                         \lambda_j(d_j(y))=0.
\]

Therefore \(\Phi_y\) is an involution:

\[
 \Phi_y(\Phi_y(k))=k.
\]

At all other vertices, \(\Phi_y\) is the identity.  Hence, for every
syndrome \(y\), the tiles contain every point of \(L^{-1}(y)\) exactly
once.  They partition \(G\).

Each \(T_\omega\) uses every actual direction exactly once, so its lift
is an isometric \(2h\)-cycle.  Finally, the independent functionals in
(4.3) make \(k\mapsto\omega(k)\) onto, with every fibre of size
\(2^{\dim K-M}\).  The connector direction following each fibre is a
fixed unique actual label.  Aligning that label in two cyclic words
aligns the corresponding fibre boundary, and the two labeled port paths
inside a fibre are different.  Thus different \(\omega\)'s give
different cyclic words.  This proves (4.5). \(\square\)

This factor is reachable from the parallel Hamming factor by literal
packets of mass at most eight.  At stage \(j\), the previous choice bits
are constant on every \(B_j\)-coset because every \(\lambda_i\) annihilates
\(B_j\).  On each coset for which \(\lambda_j=1\), apply Lemma 1.1 to
replace the \(T_\omega\)-packet by the \(T_{\omega+e_j}\)-packet.

## 5. The fixed-packet invariant

Let

\[
                         I=\{i:L(g_i)=a\}.
\]

Every seven-edge fibre path in (2.1) contains exactly two directions
from \(I\), while no high connector lies in \(I\).  Therefore

\[
                         |I|=2M=h/4.                  \tag{5.1}
\]

The cyclic direction word of every factor cycle is a concatenation of
\(M\) eight-position packets: one seven-edge fibre followed by its high
connector.  Every complete packet contains exactly two members of \(I\).

### Lemma 5.1 (window discrepancy invariant)

For every cyclic interval \(W\) of \(q<h\) direction positions in any
word occurring in Theorem 4.1,

\[
                         \bigl||W\cap I|-q/4\bigr|\le4.             \tag{5.2}
\]

#### Proof

The interval contains some number \(f\) of complete packets and at most
two proper boundary fragments.  If the fragments have total length
\(b\), then \(0\le b\le14\),

\[
                         q=8f+b,
 \qquad                  |W\cap I|=2f+x,
\]

where \(0\le x\le4\).  Hence

\[
 \left||W\cap I|-\frac q4\right|
 =\left|x-\frac b4\right|\le4. \(\square\)
\]

## 6. Gaussian anti-concentration

Choose \(S\) uniformly from \(\binom{[h]}q\), and put \(X=|S\cap I|\).
By (5.1), \(X\) is hypergeometric with success density \(1/4\):

\[
 \Pr(X=k)=
 \binom qk\frac{(h/4)_k(3h/4)_{q-k}}{(h)_q}.           \tag{6.1}
\]

Here \((u)_v=u(u-1)\cdots(u-v+1)\).  Since

\[
 \frac{(h/4)_k(3h/4)_{q-k}}{(h)_q}
 \le
 \frac{(1/4)^k(3/4)^{q-k}}
      {\prod_{j=0}^{q-1}(1-j/h)},                     \tag{6.2}
\]

and, for \(q\le h/2\),

\[
 \left(\prod_{j=0}^{q-1}(1-j/h)\right)^{-1}
 \le
 \exp\left(\frac{q(q-1)}h\right),                    \tag{6.3}
\]

(6.1) is at most \(e^{q(q-1)/h}\) times the corresponding
\({\rm Bin}(q,1/4)\) mass.

For \(q\ge64\) and \(|k-q/4|\le4\), elementary Stirling inequalities
give

\[
 \binom qk(1/4)^k(3/4)^{q-k}\le\frac2{\sqrt q}.        \tag{6.4}
\]

Indeed \(k/q\in[3/16,5/16]\), and the usual entropy form of the
Stirling bound is

\[
 \binom qk p^k(1-p)^{q-k}
 \le
 \frac{e^{1/(12q)}}{\sqrt{2\pi qx(1-x)}}
 e^{-qD(x\|p)},
 \qquad x=k/q, p=1/4,
\]

which is stronger than (6.4) on that interval.

### Theorem 6.1 (Gaussian failure of the bounded switch bank)

Fix \(A>0\).  If \(64\le q\le A\sqrt h\) and \(q\le h/2\), then the
proportion of \(q\)-subsets which occur as cyclic intervals in at least
one cycle of the factor in Theorem 4.1 is at most

\[
                         \frac{18e^{A^2}}{\sqrt q}.     \tag{6.5}
\]

In particular, whenever \(q\to\infty\) and \(q\le A\sqrt h\), this
proportion tends to zero.

#### Proof

Lemma 5.1 is necessary for occurrence.  There are at most nine integer
values \(k\) with \(|k-q/4|\le4\).  Equations (6.1)--(6.4), and
\(q(q-1)/h\le A^2\), bound each such probability by
\(2e^{A^2}/\sqrt q\).  Summing proves (6.5). \(\square\)

## 7. Exact boundary

The construction proves that neither factor integrality nor a shortage
of bounded exact switches is the obstruction: there are \(h/8\)
independent switch coordinates, every local packet has at most eight
cycles, and exponentially many cyclic orders coexist in one literal
factor.

What fails is global direction transport.  Every switch preserves the
direction multiset of each fixed seven-edge port gadget, hence preserves
the two-per-eight packet ledger (5.2).  Any proposed Gaussian-depth
construction based on this bank must add at least one of the following,
none of which is proved here:

* nonlocal switches which exchange directions between separated
  packets;
* overlapping packet frames at growing scales;
* a multi-kernel tiling in which the syndrome class \(I\) itself changes
  between independently assignable factor blocks.

Accordingly, this note supplies a scalable exact switch family and a
sharp invariant for its entire port-preserving orbit, but not the
requested approximate \(q\)-covering factor.
