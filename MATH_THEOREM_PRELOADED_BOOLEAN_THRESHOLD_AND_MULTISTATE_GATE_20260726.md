# Preloaded Boolean cells: sharp threshold, bounded contingency, and the multistate gate

Date: 2026-07-26

Method: pure mathematics only.

> **Canonical-overlay qualification.**  The contingency theorem below is
> conditional on independently selectable packet blocks.  It does not apply
> to the canonical two-endpoint coordinate overlay: its four root families
> form one Klein-four ownership component, and a legal shore choice merely
> permutes \((C_s,C_{s-1},C_{s-1},C_{s-2})\).  Moreover the dense strict-
> interior \(D_4\) fringe packets, although independently legal and
> asymptotically covering, preserve the two-endpoint target cell.  The exact
> proof is in
> `MATH_THEOREM_V4_COMPONENT_AND_D4_FRINGE_INDIVISIBILITY_20260726.md`.
> Thus Theorem 2.2 is a tool for a future boundary-active non-coordinate
> packet system, not a solution for either presently known library.

## 0. Outcome

Put \(C_t=\operatorname {Cat}_t\), let \(s\) be the first relevant
Catalan scale, and write

\[
                 \theta={C_s\over p}.
\tag{0.1}
\]

For the two-endpoint Boolean orbit, the complete canonical population is
not \(C_s\).  It is

\[
 \boxed{M_s=C_s+2C_{s-1}+C_{s-2}.}
\tag{0.2}
\]

If

\[
 \rho_s={M_s\over C_s}
 ={5s(5s-7)\over4(2s-1)(2s-3)},
\tag{0.3}
\]

then \(\rho_s\to25/16\).  Four cells of cap \(p\) are statewise possible
only if

\[
 \boxed{
 \theta\le\theta_{4,s}:={4\over\rho_s}
 ={16(2s-1)(2s-3)\over5s(5s-7)}
 ={64\over25}+O(s^{-1}).}
\tag{0.4}
\]

This is only the zero-background bound.  If the four physical targets have
unaffected loads \(\beta_{00},\ldots,\beta_{11}\), their true capacities
are

\[
                         c_{ab}=(p-\beta_{ab})_+,
\tag{0.5}
\]

and the necessary condition is

\[
                         M_s\le\sum_{a,b}c_{ab}.
\tag{0.6}
\]

Thus (0.4) must never be used without the physical carrier/background
ledger.

Below the threshold, the abstract balanced-contingency problem has a
strong deterministic solution.  Suppose the left and right legal packet
choices are constant on blocks of two partitions of the complete
\(M_s\)-occurrence multiset, every nonexceptional block has size at most
\(B\), and \(R\) occurrences are exceptional.  Then legal binary choices
can be made so that every Boolean cell has size at most

\[
 \boxed{{M_s\over4}+{5B+3R\over4}.}
\tag{0.7}
\]

Consequently four zero-background cells are sufficient whenever

\[
                         4p-M_s\ge5B+3R.
\tag{0.8}
\]

With true backgrounds, the sufficient condition is

\[
              {M_s+5B+3R\over4}lemin_{a,b}c_{ab}.
\tag{0.9}
\]

For the fourteen-row \(D_4\) packet size, \(B=14\), the deterministic
contingency cost is only seventy tokens, apart from the exceptional set.
The estimate does not prove that the actual packet systems cover all
principal and collar occurrences, commute at the two boundaries, or land
in separated physical carriers.  Those are precisely the remaining legal
geometry hypotheses.

Above (0.4), four cells are impossible even with zero background.  The
minimum number of cap-\(p\) cells is

\[
 \boxed{k_s(\theta)=\left\lceil\rho_s\theta\right\rceil.}
\tag{0.10}
\]

Asymptotically this requires five, six, or seven cells in the three ranges

\[
\begin{array}{c|c}
64/25<\theta\le16/5&5\\
16/5<\theta\le96/25&6\\
96/25<\theta<4&7.
\end{array}
\tag{0.11}
\]

There is a concrete partial multistate input.  Let

\[
 H_4=\langle(2\ 3),(4\ 5),(6\ 7)\rangle.
\tag{0.12}
\]

At the fixed port \(P=1256\), the reanchored \(H_4\)-orbits of both the
canonical \(D_4\) factor and the new pair-transfer factor realize the four
first-insertion labels

\[
                              \{3,4,7,8\}.
\tag{0.13}
\]

Thus one endpoint has a literal four-state port-valid local menu.  With a
second independent binary endpoint in a disjoint physical coordinate
block, it gives eight nominal cells, enough for every value in (0.11).
What is not proved is a balanced eight-cell action on the complete
\(M_s\) occurrence family.  The factor state is chosen for a whole packet,
so the four labels in (0.13) cannot be assigned independently occurrence by
occurrence.

The exact remaining split is therefore:

* for \(\theta\le\theta_{4,s}\), verify full occurrence coverage,
  two-boundary legal commutation, and carrier separation, then apply
  (0.7)--(0.9);
* for \(\theta>\theta_{4,s}\), construct a multistate parent-aligned packet
  system whose complete carrier-resolved profile occupies at least
  \(k_s(\theta)\) residual cells.  The fixed-port menu (0.13) is a finite
  seed, not yet that packet system.

## 1. Exact preload and the four-cell obstruction

The principal two-boundary fibre contributes \(C_s\) occurrences.  Fixing
the left endpoint atom leaves an arbitrary semilength-\((s-1)\) Dyck
filling, and so contributes \(C_{s-1}\); the right endpoint contributes a
second copy.  Fixing both endpoint atoms leaves semilength \(s-2\), giving
\(C_{s-2}\).  This proves (0.2).

The exact Catalan ratios are

\[
 {C_{s-1}\over C_s}={s+1\over2(2s-1)},
 \qquad
 {C_{s-2}\over C_s}={s(s+1)\over4(2s-1)(2s-3)}.
\tag{1.1}
\]

Therefore

\[
\begin{aligned}
 \rho_s
 &=1+{s+1\over2s-1}
       +{s(s+1)\over4(2s-1)(2s-3)}\\
 &={5s(5s-7)\over4(2s-1)(2s-3)},
\end{aligned}
\tag{1.2}
\]

which proves (0.3).  Every legal two-bit state merely redistributes the
same \(M_s\) occurrences among its four physical cells.  Hence
\(M_s>4p\) is a statewise obstruction, proving (0.4).

If unaffected loads are present, at most \(c_{ab}\) new occurrences fit in
cell \((a,b)\).  Summing gives (0.6).  Notice that even
\(M_s\le4p\) can be useless when the background consumes capacity in one
or more of the four carrier cells.

## 2. A bounded-error two-partition contingency theorem

Let \(\Omega\) be a multiset of \(N\) occurrences.  Let \(\mathcal P\)
and \(\mathcal Q\) be partitions of \(\Omega\), and suppose every block has
size at most \(B\).  A legal left bit is one sign \(x_P\in\{-1,1\}\) per
\(P\in\mathcal P\), while a legal right bit is one sign
\(y_Q\in\{-1,1\}\) per \(Q\in\mathcal Q\).  Put

\[
 X=\sum_{\omega}x_{P(\omega)},\qquad
 Y=\sum_{\omega}y_{Q(\omega)},\qquad
 Z=\sum_{\omega}x_{P(\omega)}y_{Q(\omega)}.
\tag{2.1}
\]

The four cell sizes are

\[
 n_{\epsilon,\eta}
 ={N+\epsilon X+\eta Y+\epsilon\eta Z\over4}.
\tag{2.2}
\]

### Lemma 2.1 (fixed-dimensional extreme-point signing)

Let \(v_1,\ldots,v_t\in\mathbb R^d\) satisfy
\(\|v_i\|_\infty\le B\).  There are signs
\(\sigma_i\in\{-1,1\}\) such that

\[
                 \left\|\sum_i\sigma_iv_i\right\|_\infty
                              \le dB.
\tag{2.3}
\]

#### Proof

Consider the nonempty polytope

\[
 \mathcal K=\{z\in[-1,1]^t:\sum_i z_iv_i=0\}.
\]

At an extreme point of \(\mathcal K\), at most
\(\operatorname {rank}\{v_i\}\le d\) coordinates lie strictly between
\(-1\) and \(1\); otherwise a nonzero perturbation supported on the
fractional coordinates would remain in the kernel and contradict
extremality.  Round every fractional coordinate to its nearer sign.  Each
rounding displacement is at most one, so the error in every vector
coordinate is at most \(dB\). \(\square\)

### Theorem 2.2 (constant-error four-cell signing)

There are legal block signs for which

\[
                         |X|\le B,qquad
                         |Y|\le2B,qquad |Z|\le2B.
\tag{2.4}
\]

Consequently

\[
 \boxed{
                    \max_{\epsilon,\eta}n_{\epsilon,\eta}
                         \le {N\over4}+{5B\over4}.}
\tag{2.5}
\]

#### Proof

Apply Lemma 2.1 in dimension one to the scalars \(|P|\),
\(P\in\mathcal P\).  This chooses \(x_P\) with \(|X|\le B\).

For every \(Q\in\mathcal Q\), define

\[
 v_Q=\left(|Q|,\sum_{\omega\in Q}x_{P(\omega)}\right).
\tag{2.6}
\]

Both coordinates of \(v_Q\) have absolute value at most \(|Q|\le B\).
Apply Lemma 2.1 in dimension two to obtain signs \(y_Q\) for which the two
coordinates of \(\sum_Qy_Qv_Q\) have absolute value at most \(2B\).
Those two coordinates are precisely \(Y,Z\).  Formula (2.2) now gives
(2.5). \(\square\)

This improves the square-root error obtained from independent random
signs to an error depending only on the maximum packet size.

### Corollary 2.3 (exceptions)

If \(R\) occurrences are removed, the two partitions on the remaining
occurrences have blocks of size at most \(B\), and the exceptions are then
placed adversarially, every cell has size at most

\[
                         {N\over4}+{5B+3R\over4}.
\tag{2.7}
\]

#### Proof

Apply (2.5) to \(N-R\) occurrences and place all \(R\) exceptions in one
cell:

\[
 {N-R\over4}+{5B\over4}+R
 ={N\over4}+{5B+3R\over4}.
\]

This proves the claim. \(\square\)

Taking \(N=M_s\) proves (0.7)--(0.9), provided the two packet partitions
are literal independently selectable exact-factor partitions of the whole
preloaded occurrence multiset.

## 3. What “legal” still requires

The signs in Theorem 2.2 are legal factor choices only under all of the
following hypotheses.

1. **Full coverage.**  Every principal, one-sided-collar, and double-collar
   occurrence counted by \(M_s\) belongs to one left packet block and one
   right packet block, apart from the declared \(R\) exceptions.
2. **Packet legality.**  Either shore of every block is a complete exact
   port-valid replacement.
3. **Cross-boundary commutation.**  Every chosen set of left shores and
   right shores composes to one exact factor.  Separate exactness of the
   two packet systems does not imply this when their ownership supports
   overlap.
4. **Literal target map.**  The two states act through disjoint surviving
   boundary-coordinate pairs, so the four sign cells map injectively to
   four physical targets.
5. **Full residual capacities.**  The \(c_{ab}\) in (0.5) include every
   occurrence from all other contexts and depths already landing on those
   physical targets.

Thus Theorem 2.2 closes the abstract contingency problem, including its
integrality, but not these geometric hypotheses.  In particular, applying
it only to the principal \(C_s\) fibre would repeat the preload error which
led to the false four-cell range.

## 4. Cross-context separation

Suppose context \(C\) has common core \(K_C\) and four targets

\[
 T_C^{ab}=K_C\cup\{x_C^a,y_C^b\},
 \qquad a,b\in\{0,1\},
\tag{4.1}
\]

where the two active coordinate pairs are disjoint from each other and
from \(K_C\).

### Lemma 4.1 (exact collision localization)

If \(T_C^{ab}=T_D^{a'b'}\) for two contexts, then

\[
 K_C\setminus K_D\subseteq\{x_D^{a'},y_D^{b'}\},
 \qquad
 K_D\setminus K_C\subseteq\{x_C^a,y_C^b\}.
\tag{4.2}
\]

In particular

\[
                         |K_C\triangle K_D|\le4.
\tag{4.3}
\]

#### Proof

Every element of \(K_C\setminus K_D\) belongs to the common target but not
to \(K_D\), so it must be one of the two active labels contributed by
context \(D\).  The reverse containment is symmetric. \(\square\)

### Corollary 4.2 (core-code separation)

Any atlas satisfying

\[
                         |K_C\triangle K_D|>4
                         \qquad(C\ne D)
\tag{4.4}
\]

has pairwise disjoint four-cell target sets.  More generally, a private
marker contained in all four targets of one context and in no target of
another also gives separation.

For constant-weight cores of size \(k\) in an \(n\)-coordinate universe,
the number of other cores at symmetric-difference distance at most four is
at most

\[
 \boxed{
 D_{n,k}=\sum_{i=0}^2\binom{k}{i}\binom{n-k}{i}.}
\tag{4.5}
\]

Hence the collision graph has a greedily selectable independent atlas of
size at least \(|\mathscr C|/D_{n,k}\).

This is a rigorous separator, but \(D_{n,k}\) is polynomial rather than
\(1+o(1)\).  Selecting only one independent atlas can therefore lose a
polynomial factor and does not by itself close coefficient one.  A complete
argument must either provide private context markers, process all collision
colours with an adaptive residual-capacity theorem, or show that the actual
aligned core family has a much smaller weighted collision degree.

## 5. Above the four-cell threshold

No signing or matching theorem can place \(M_s\) tokens into fewer than
\(k_s(\theta)\) cap-\(p\) cells.  Formula (0.10) follows by pigeonhole.
Using \(\rho_s\to25/16\) gives (0.11).  In particular a binary choice at
each of two endpoints is structurally insufficient as soon as
\(\theta>\theta_{4,s}\).

There are two minimal ways to reach the required state counts:

* a ternary endpoint times a binary endpoint gives six cells, sufficient
  only while \(M_s\le6p\);
* a four-state endpoint times a binary endpoint gives eight cells,
  sufficient throughout the full early-scale range \(\theta<4\).

The second option has a finite \(D_4/H_4\) seed.

### Proposition 5.1 (a four-state fixed-port menu)

Let \(P=1256\).  For \(h\in H_4\), root the coordinate-conjugate factor
\(hF\) at \(P\); its path is \(h\) applied to the path of \(F\) rooted at
\(h^{-1}P\).  The corresponding first-insertion labels are

\[
\begin{array}{c|c|c|c}
h&h^{-1}P&b_1^{hF}(P)&b_1^{hG}(P)\\ \hline
1&1256&4&7\\
(6\ 7)&1257&4&3\\
(4\ 5)&1246&8&3\\
(4\ 5)(6\ 7)&1247&7&3\\
(2\ 3)&1356&3&3\\
(2\ 3)(6\ 7)&1357&3&4\\
(2\ 3)(4\ 5)&1346&3&8\\
(2\ 3)(4\ 5)(6\ 7)&1347&3&8.
\end{array}
\tag{5.1}
\]

Both columns have support

\[
                              \{3,4,7,8\}.
\tag{5.2}
\]

Every row of (5.1) is a legal \(D_4\)-port factor state, because \(H_4\)
preserves the Dyck port family and coordinate conjugation preserves both
exact ownership ledgers.  This proves (0.13). \(\square\)

The four labels in (5.2) lie in four different pair classes
\(E_1,E_2,E_3,E_0\).  Thus this is not merely an orientation within one
two-cell orbit.  If a second phase-disjoint endpoint bit is embedded into a
disjoint physical coordinate block, the marked occurrence has eight
distinct formal labels.

The limitation is global coupling.  Choosing one \(h\) fixes the paths of
all fourteen ports simultaneously.  Table (5.1) proves four states for one
port, not balanced four-state marginals for all \(M_s\) occurrences.  The
needed theorem above (0.4) is therefore a multicolour analogue of Theorem
2.2 with factor-state blocks and the complete carrier preload included.

## 6. Decision

The preload reconciliation changes the early-scale program as follows.

1. Four cells are numerically meaningful only up to the exact threshold
   (0.4), and only after replacing \(p\) by the true capacities (0.5).
2. Below that threshold, bounded two-partition packet systems have no
   serious discrepancy obstruction: Theorem 2.2 gives constant packet-size
   error.  The unresolved work is full legal coverage and physical carrier
   separation.
3. Core-distance greater than four is an exact cross-context separator, but
   the generic greedy subatlas loses a polynomial factor.  A dense marked or
   weighted separator is still needed.
4. Above the threshold, four cells are statewise impossible.  The
   \(D_4/H_4\) orbit supplies a genuine four-state fixed-port seed and hence
   a nominal eight-cell boundary product.  Turning it into a complete
   balanced parent-aligned library remains open.

This isolates the next theorem sharply: construct the carrier-resolved
factor-state partitions realizing either the legal four-cell hypothesis of
Section 3 below threshold or the eight-cell \(D_4/H_4\) product above it,
with the actual residual capacities rather than uniform empty bins.
