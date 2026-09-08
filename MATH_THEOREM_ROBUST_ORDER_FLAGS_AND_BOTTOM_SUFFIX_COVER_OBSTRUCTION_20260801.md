# Robust ordered flags and the exact bottom-suffix cover obstruction

**Date:** 2026-08-01  
**Status:** unconditional local construction and unconditional menu-size
obstruction. This gives linear robust portal degree on any bounded prepared
set of roots. A single order, or any bounded order menu, cannot be a named
lower-exact flag factor. It does not prove the remaining selector theorem or
the additive-constant conjecture.

## 0. Verdict

Write the odd dimension as \(k=2m+1\), and let rooted flags have depth
\(d\). Order the coordinates globally and, at every rank-\(m\) root, put
its first \(d-1\) elements in the singleton positive-age classes.

For any fixed \(h\) prepared roots, the order can be chosen so that each
prepared root has at least

\[
                         m+1-(h-1)d-b                         \tag{0.1}
\]

legal turns after any \(b\) additional foreign resource rows are forbidden.
The portal-list pair-codegree is one. Hence this family gives linear robust
degree on the prepared roots whenever \(h=O(1)\) and \(b=O(d)\).

The obstruction is equally exact. Put \(s=m-d+1\). For one global order,
the bottom suffix \(C_0\) can equal an \(s\)-set \(S\) if and only if the
first \(d-1\) global coordinates avoid \(S\). Therefore a menu of \(t\)
global orders can even support every rank-\(s\) target only if

\[
 t\ge
 { \binom{2m+1}{d-1} \over \binom{m+d}{d-1}}
 =2^{d-1}\exp\!\left(-O\!\left({d^2\over m}\right)\right).       \tag{0.2}
\]

Thus robust portal degree is easy in one ordered flag, but named lower
support forces an exponentially large-in-\(d\) order menu. The missing row
is correlated selection of one flag from that menu at every root while
retaining exact lower targets and owner/turn Hall.

## 1. Rooted all-high order flags

Fix a total order \(\prec\) on \([2m+1]\). For a rank-\(m\) root \(p\),
write its elements as

\[
                         z_1\prec z_2\prec\cdots\prec z_m.       \tag{1.1}
\]

Define

\[
\begin{aligned}
 C^p_{d-j}&=\{z_j\} &&(1\le j\le d-1),\\
 C^p_0&=\{z_d,z_{d+1},\ldots,z_m\}.                             \tag{1.2}
\end{aligned}
\]

The corresponding owner type is
\((m-d+1,1,\ldots,1,1)\), where the final singleton is supplied by
the owner attachment.

A predecessor root \(p\), head root \(q\), and owner \(o\) form a legal turn
when

\[
 o=p\cup q,\qquad o-q\subseteq C^p_{d-1},\qquad
 C^q_{i+1}\subseteq C^p_i\quad(0\le i<d-1).                    \tag{1.3}
\]

### Theorem 1.1 (ordered-shift turn)

Let \(\beta\notin p\) satisfy \(z_d\prec\beta\), and put

\[
 q=p-\{z_1\}+\{\beta\},\qquad o=p\cup\{\beta\}.                  \tag{1.4}
\]

Then \((p,q,o)\) is legal for the frozen order flags. Different choices of
\(\beta\) give different head roots and owners. The candidate list at \(p\)
therefore has pair-codegree one against every foreign resource row.

#### Proof

The first \(d-1\) elements of \(q\) are \(z_2,\ldots,z_d\).
Furthermore \(o-q=\{z_1\}=C^p_{d-1}\). For \(2\le j\le d-1\),
the singleton \(C^q_j\) equals \(C^p_{j-1}\), while
\(C^q_1=\{z_d\}\subseteq C^p_0\). These are exactly (1.3).

The owner determines \(\beta=o-p\), and the head determines the unique
exchange \(\beta=q-p\). Thus a fixed foreign owner or head row occurs in at
most one candidate; a foreign tail row occurs in none. \(\square\)

## 2. Simultaneous robust degree on bounded prepared roots

### Theorem 2.1 (bounded prepared order)

Let \(p_1,\ldots,p_h\) be rank-\(m\) roots. For each \(i\), choose an
arbitrary \(d\)-set \(Q_i\subseteq p_i\). There is a total order placing
\[
                              Q:=\bigcup_{i=1}^h Q_i             \tag{2.1}
\]
before every coordinate outside \(Q\). Under its flags (1.2), root \(p_i\)
has at least

\[
                              m+1-(h-1)d                        \tag{2.2}
\]

legal turns. After forbidding any \(b\) foreign resource rows, none equal
to \(p_i\), at least

\[
                              m+1-(h-1)d-b                      \tag{2.3}
\]

turns remain.

#### Proof

The first \(d\) elements of \(p_i\) lie in \(Q\), since
\(Q_i\subseteq Q\cap p_i\). Every coordinate outside \(Q\) is therefore
after \(z_d(p_i)\). The complement of \(p_i\) has size \(m+1\), and

\[
                         |Q-p_i|\le\sum_{j\ne i}|Q_j|
                                      \le(h-1)d.                 \tag{2.4}
\]

Theorem 1.1 proves (2.2). Its pair-codegree-one conclusion says each
foreign resource row deletes at most one candidate, proving (2.3).
\(\square\)

### Corollary 2.2 (prepared portal lists)

If \(h=O(1)\), \(d=O(\sqrt m)\), and the fixed packet/anchor bank has
\(b=O(hd)\) resources, every prepared root has
\(m-O(hd)=\Omega(m)\) legal portal turns and cross-list conflict degree at
most \(3(h-1)\).

Hence the LLL packet selection of the balanced-turn note is automatic for
these prepared ordered flags. This conclusion is local: it says nothing
about named lower-target exactness of the full flag table.

## 3. Exact bottom-suffix support of one order

The bottom suffix has rank \(s=m-d+1\):

\[
                              C^q_0=q-\{z_1,\ldots,z_{d-1}\}.    \tag{3.1}
\]

For an \(s\)-set \(S\), let \(j_\prec(S)\) be the position of its first
element in the global order.

### Theorem 3.1 (one-order support formula)

The number of roots \(q\) for which \(C^q_0=S\) is

\[
                 \binom{j_\prec(S)-1}{d-1}.                     \tag{3.2}
\]

In particular, \(S\) occurs under \(\prec\) exactly when the first \(d-1\)
global coordinates are disjoint from \(S\).

#### Proof

If \(C^q_0=S\), then \(q=S\mathbin{\dot\cup}H\), where \(H\) consists of
the first \(d-1\) elements of \(q\). Every member of \(H\) precedes every
member of \(S\). Conversely every \((d-1)\)-subset of the
\(j_\prec(S)-1\) coordinates preceding \(\min_\prec S\) gives one such
root. This proves (3.2) and its positivity criterion. \(\square\)

A single order is therefore maximally nonuniform: every \(s\)-set
containing the first global coordinate has zero candidates.

## 4. Exponential order-menu lower bound

Let \(\Pi\) be a family of total orders, and let \(H_\pi\) be the first
\(d-1\) coordinates of \(\pi\).

### Theorem 4.1 (order-menu covering bound)

If every rank-\(s=m-d+1\) target occurs as \(C_0\) in at least one flag
from \(\Pi\), then every \((m+d)\)-subset of \([2m+1]\) contains some
\(H_\pi\). Consequently

\[
 |\Pi|\ge
 { \binom{2m+1}{m+d} \over \binom{2m-d+2}{m+1}}
 =
 { \binom{2m+1}{d-1} \over \binom{m+d}{d-1}}.                   \tag{4.1}
\]

For \(d=o(m)\),

\[
 |\Pi|\ge
 2^{d-1}\exp\!\left(-O\!\left({d^2\over m}\right)\right).       \tag{4.2}
\]

In the problem range \(d=\Theta(\sqrt m)\), this is
\(\exp(\Theta(\sqrt m))\).

#### Proof

By Theorem 3.1, \(S\) is available from \(\pi\) exactly when
\(H_\pi\subseteq[2m+1]-S\). The complement has size \(m+d\), so the
\(H_\pi\) blocks must cover all \((m+d)\)-sets by containment.

One fixed \((d-1)\)-block lies in
\(\binom{2m-d+2}{m+1}\) such large sets. Counting large sets proves the
first ratio; double counting gives the second. Finally,

\[
 { \binom{2m+1}{d-1} \over \binom{m+d}{d-1}}
 =\prod_{i=0}^{d-2}{2m+1-i\over m+d-i}
 =2^{d-1}\exp\!\left(-O\!\left({d^2\over m}\right)\right).
\]

\(\square\)

### Corollary 4.2

No bounded, polynomial-in-\(d\), or polynomial-in-\(m\) menu of global-order
all-high flags can even support every bottom-rank target when
\(d=\Theta(\sqrt m)\).

This is a support obstruction, before multiplicity, owner matching,
chronology, upper shadows, or the compiler.

## 5. Exact remaining selector theorem

Theorems 2.1 and 4.1 expose the quantifier conflict.

* One suitably prepared order gives linear robust portal degree at all
  \(O(1)\) named task roots.
* Named lower support across every target requires an order menu of size at
  least \(\exp(\Theta(d))\).

The weakest remaining statement along this route is:

> **Protected multi-order flag selector.** From an order family whose
> initial \((d-1)\)-blocks cover every \((m+d)\)-set, choose one order flag
> at every root so that every named lower target has its required
> multiplicity, the chosen owner/turn support satisfies Hall, and the
> \(O(1)\) protected roots all use one prepared order from Theorem 2.1.

If this selector leaves residual fractional turn deficiency \(C\), then
Corollary 12.1 of the balanced-turn note gives the terminal bound
\(B(k)+C\), modulo any separately declared fixed physical charge.

No theorem presently proves this selector. The exponential menu lower bound
shows why a bounded prepared-order bank cannot do so; it does not rule out a
large-menu matching or absorption proof.

