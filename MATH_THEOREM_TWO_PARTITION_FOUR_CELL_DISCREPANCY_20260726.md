# Two-partition four-cell discrepancy and the exact early-scale interface

Date: 2026-07-26

Method: pure mathematics only.

## 0. Result

Let \(\Omega\) be a multiset of \(d\) protected occurrences.  Suppose
that a left boundary choice is constant on the blocks of a partition
\(\mathcal P\) of \(\Omega\), while a right boundary choice is constant
on the blocks of a second partition \(\mathcal Q\).  If every block of
both partitions has size at most \(B\), then the two families of binary
choices can be made so that all four joint cells have size at most

\[
                 \boxed{\frac d4+\frac34\sqrt{Bd}.}       \tag{0.1}
\]

More generally, if an exceptional multiset of size \(R\) is removed
before forming the two bounded-block partitions, then every cell has size
at most

\[
       \boxed{\frac d4+\frac{3R}{4}+\frac34\sqrt{Bd}.}   \tag{0.2}
\]

Consequently, put

\[
 s=\min\{t:\operatorname {Cat}_t\ge p\},\qquad
 d=\operatorname {Cat}_s.
\]

Since

\[
 \frac{\operatorname {Cat}_s}{\operatorname {Cat}_{s-1}}
       =4-\frac6{s+1}
 \quad\hbox{and}\quad \operatorname {Cat}_{s-1}<p,
\]

one has the strict scalar slack

\[
                    p-\frac d4>\frac{3p}{2(s+1)}.       \tag{0.3}
\]

Thus four-cell cap \(p\) follows whenever

\[
                   R=o(p/s),\qquad B=o(p/s^2).          \tag{0.4}
\]

In particular, bounded packet size and an exponentially small exceptional
part have far more than enough discrepancy room.  If the two dense
size-four fringe-packet systems from
`MATH_THEOREM_D4_PAIR23_PORT_FACTOR_20260726.md` really induce two
independent boundary bits on the **entire relevant occurrence multiset**,
then their packet size \(B=14\) closes the balanced-contingency part of
the early-scale gate.

There is, however, an exact scalar qualification.  The complete natural
four-cell orbit contains not only the principal \(C_s\) fibre but also
the two one-sided collars and the double collar.  Its mass is

\[
 M_s=C_s+2C_{s-1}+C_{s-2},                              \tag{0.5}
\]

and

\[
 {M_s\over C_s}
 ={5s(5s-7)\over4(2s-1)(2s-3)}
 \longrightarrow {25\over16}.                           \tag{0.6}
\]

Therefore four physical cells of capacity \(p\) are possible only when

\[
 {C_s\over p}
 \le {4\over M_s/C_s}
 ={16(2s-1)(2s-3)\over5s(5s-7)}
 ={64\over25}+O(s^{-1}).                                \tag{0.7}
\]

For larger Catalan overshoot, no four-cell signing theorem can help: a
multi-state boundary library producing more physical cells is necessary.

The italicized interface is essential.  The theorem below does not assert
that one marked row in a fourteen-row local factor gives a bit to all
fourteen occurrences, nor does it omit the canonical collar/background
mass.  Those are the remaining geometric checks.

## 1. Exact cell formula

For every block \(P\in\mathcal P\), choose a sign
\(x_P\in\{-1,+1\}\), and for every block \(Q\in\mathcal Q\), choose a
sign \(y_Q\in\{-1,+1\}\).  Put

\[
\begin{aligned}
 X&=\sum_{\omega\in\Omega}x_{P(\omega)},\\
 Y&=\sum_{\omega\in\Omega}y_{Q(\omega)},\\
 Z&=\sum_{\omega\in\Omega}x_{P(\omega)}y_{Q(\omega)}.
\end{aligned}                                           \tag{1.1}
\]

For \(\epsilon,\eta\in\{-1,+1\}\), let

\[
 n_{\epsilon,\eta}
 =|\{\omega:x_{P(\omega)}=\epsilon,
              y_{Q(\omega)}=\eta\}|.                  \tag{1.2}
\]

Then the indicator identity

\[
 \mathbf1_{\{x=\epsilon,y=\eta\}}
 ={(1+\epsilon x)(1+\eta y)\over4}
\]

gives

\[
 \boxed{
 n_{\epsilon,\eta}
 ={d+\epsilon X+\eta Y+\epsilon\eta Z\over4}.}         \tag{1.3}
\]

Thus the four-cell problem is exactly the simultaneous discrepancy
problem for the two linear marginals \(X,Y\) and the bilinear correlation
\(Z\).

## 2. The second-moment lemma

For \(P\in\mathcal P,Q\in\mathcal Q\), write

\[
                         w_{P,Q}=|P\cap Q|.             \tag{2.1}
\]

### Theorem 2.1 (two-partition signing)

There are signs \((x_P),(y_Q)\) for which

\[
 X^2+Y^2+Z^2
 \le d\left(max_P|P|+\max_Q|Q|+max_{P,Q}w_{P,Q}\right).  \tag{2.2}
\]

In particular, if all blocks have size at most \(B\), then

\[
                         X^2+Y^2+Z^2\le3Bd.             \tag{2.3}
\]

#### Proof

Choose all signs independently and uniformly.  Independence and zero
means give

\[
 \mathbb E X^2=\sum_{P\in\mathcal P}|P|^2
       \le d\max_P|P|,                                  \tag{2.4}
\]

and similarly

\[
 \mathbb E Y^2\le d\max_Q|Q|.                           \tag{2.5}
\]

Moreover

\[
                         Z=\sum_{P,Q}w_{P,Q}x_Py_Q.
\]

In the expansion of \(\mathbb EZ^2\), a cross term survives only when
both its \(P\)-indices and its \(Q\)-indices agree.  Hence

\[
 \mathbb EZ^2=\sum_{P,Q}w_{P,Q}^2
       \le d\max_{P,Q}w_{P,Q}.                          \tag{2.6}
\]

Adding (2.4)--(2.6), some deterministic signing is no worse than the
expectation.  This proves (2.2), and (2.3) follows because
\(w_{P,Q}\le\min\{|P|,|Q|\}\). \(\square\)

By Cauchy--Schwarz and (2.3),

\[
 |X|+|Y|+|Z|
 \le\sqrt3\sqrt{X^2+Y^2+Z^2}
 \le3\sqrt{Bd}.                                        \tag{2.7}
\]

Equations (1.3) and (2.7) prove (0.1).

## 3. Exceptional occurrences

Let \(\Omega_0\subseteq\Omega\) have size \(R\), and apply Theorem 2.1
to \(\Omega\setminus\Omega_0\), of size \(d-R\).  Its largest cell has
size at most

\[
                 {d-R\over4}+{3\over4}\sqrt{B(d-R)}.
\]

Place all exceptional occurrences adversarially in one cell.  The largest
resulting cell is at most

\[
 {d-R\over4}+{3\over4}\sqrt{B(d-R)}+R
 \le {d\over4}+{3R\over4}+{3\over4}\sqrt{Bd},          \tag{3.1}
\]

which proves (0.2).

## 4. Catalan slack

Minimality of \(s\) gives \(\operatorname {Cat}_{s-1}<p\).  The exact
Catalan quotient is

\[
 {\operatorname {Cat}_s\over\operatorname {Cat}_{s-1}}
 ={2(2s-1)\over s+1}=4-{6\over s+1}.                   \tag{4.1}
\]

Therefore

\[
 {d\over4}<\left(1-{3\over2(s+1)}\right)p,
\]

which is (0.3).  Since \(s=\Theta(\log p)\), conditions (0.4) make both
error terms in (0.2) equal to \(o(p/s)\).  For sufficiently large \(p\),
(0.2) is then strictly below \(p\).

## 5. Exact geometric hypotheses still to verify

The discrepancy theorem closes the numerical contingency problem only
after the following four facts have been established for one common
protected target family.

1. **Occurrence coverage.**  Every occurrence being charged to the four
   cells receives one left packet label and one right packet label.  A
   packet which moves only one distinguished row does not label the other
   thirteen rows.
2. **Independent exact legality.**  Any chosen set of left packet states
   and any chosen set of right packet states must compose to one exact
   middle factor.  This follows for influence-separated port substitutions,
   but not from two independently valid overlay partitions alone.
3. **Literal four-target action.**  The two bits must act through two
   disjoint surviving coordinate pairs, so that the four cells in (1.2)
   push to four distinct physical targets.  The rows `1256` and `1345`
   in the explicit \(D_4\) factor provide one literal local witness, not
   yet a witness for every occurrence.
4. **Complete residual mass.**  The multiset \(\Omega\) must include all
   canonical collar and background occurrences which land in the same
   four physical targets.  Balancing only the hereditary fibre can still
   leave total load above \(p\).

Accordingly, no abstract discrepancy or integrality difficulty remains
once these four carrier-resolved hypotheses hold.  The open theorem is a
geometric packet-realization theorem supplying them simultaneously across
the parent atlas and all serviced depths.

## 6. Exact preload calculation

The four Boolean cells are indexed by the presence or absence of the
distinguished left and right `10` boundary atoms.  The unrestricted
interior filling contributes \(C_s\) occurrences to the principal cell.
Fixing the left boundary atom leaves an arbitrary Dyck filling of
semilength \(s-1\), and the same is true on the right, giving two copies
of \(C_{s-1}\).  Fixing both atoms leaves semilength \(s-2\), giving
\(C_{s-2}\).  This proves (0.5).

The exact Catalan ratios are

\[
 {C_{s-1}\over C_s}={s+1\over2(2s-1)},\qquad
 {C_{s-2}\over C_s}={s(s+1)\over4(2s-1)(2s-3)}.        \tag{6.1}
\]

Substitution into \(1+2C_{s-1}/C_s+C_{s-2}/C_s\)
gives (0.6).  Since the sum of the four cell loads is invariant under
the two boundary permutations, \(M_s>4p\) is a statewise obstruction.
This proves (0.7), independently of discrepancy or packet legality.

## 7. Multi-state extension

The obstruction (0.7) motivates more than two legal states at one
boundary.  The discrepancy part extends without difficulty.

### Theorem 7.1 (two-partition multi-state signing)

Let the blocks of \(\mathcal P\) be independently assignable any of
\(u\ge2\) labels and the blocks of \(\mathcal Q\) any of \(v\ge2\)
labels.  If both partitions have block size at most \(B\), then there is
an assignment for which every one of the \(uv\) joint cells has size at
most

\[
 \boxed{
 {d\over uv}
 +\sqrt{Bd\left(1+{1\over u}+{1\over v}\right)}.}       \tag{7.1}
\]

#### Proof

Assign every block an independent uniform label.  Let \(n_{ab}\) be the
joint cell counts and put

\[
                  \mathcal S=\sum_{a=1}^u\sum_{b=1}^v
                     \left(n_{ab}-{d\over uv}\right)^2. \tag{7.2}
\]

Expanding \(\sum n_{ab}^2\) counts ordered pairs of occurrences which
receive the same joint label.  A pair in different \(\mathcal P\)- and
different \(\mathcal Q\)-blocks has probability \(1/(uv)\), exactly the
baseline in (7.2).  A pair sharing only its \(\mathcal P\)-block has
excess probability at most \(1/v\); one sharing only its
\(\mathcal Q\)-block has excess at most \(1/u\); and one sharing both has
excess at most one.  The number of ordered pairs sharing a block of either
partition, or one intersection block, is at most \(Bd\).  Therefore

\[
              \mathbb E\mathcal S
              \le Bd\left(1+{1\over u}+{1\over v}\right). \tag{7.3}
\]

Some assignment satisfies the same inequality.  Each individual squared
deviation is at most \(\mathcal S\), which proves (7.1). \(\square\)

For the complete early-scale preload \(M_s\), the worst possible Catalan
overshoot gives

\[
                    {M_s\over p}< {25\over4}+o(1).       \tag{7.4}
\]

Thus eight genuinely distinct joint cells would have constant scalar
slack uniformly over the entire overshoot interval.  For example a
four-state left boundary and a binary right boundary would be sufficient
numerically, with bounded packets giving only \(O(\sqrt p)\) discrepancy.
The unresolved issue is wholly geometric: a factor-level library must
give all charged occurrences those states, not merely give one selected
row four possible marked targets.
