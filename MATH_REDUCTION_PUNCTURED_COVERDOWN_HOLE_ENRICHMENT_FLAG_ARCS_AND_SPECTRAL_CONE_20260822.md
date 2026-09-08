# Punctured cover-down: hole enrichment, nested flag arcs, and the spectral cone boundary

**Date:** 2026-08-22  
**Status:** unconditional reduction and obstruction.  The note proves the
amount of physical hole alignment required by any minimal cover-down, gives
an exact fractional dual, and gives a weaker long-arc sufficient interface
whose promotion cost is still \(o(A)\).  It also identifies exactly what the
Petr--Turek wreath spectrum does and does not supply.  The existence of the
required enriched rows or arcs for the actual nibble residual remains open.

## 1. Literal punctured bank and its holes

Fix \(r\ge2\), and put

\[
 b=2r+1,\qquad
 A=\binom br,\qquad
 L=\binom b{r-1}={r\over r+2}A,\qquad
 B={A\over b}=\operatorname {Cat}_r.              \tag{1.1}
\]

For a permutation \(w=(w_0,\ldots,w_{b-1})\), with indices modulo \(b\),
write

\[
 I_k^w(s)=\{w_s,w_{s+1},\ldots,w_{s+k-1}\}.        \tag{1.2}
\]

The directed punctured configuration \(E(w)\) contains the \(2r\) middle
targets \(I_r^w(s)\), \(s\ne0\), and the \(2r\) lower targets
\(I_{r-1}^w(s)\), \(s\ne0\).  Let \(\mathcal P\) be any matching of these
configurations, put \(p=|\mathcal P|\), and define its lower residual
density \(x\) by

\[
                         2rp=(1-x)L.               \tag{1.3}
\]

For \(1\le q\le H\le r-1\), define the literal hole sets

\[
 \mathcal H_q^-=
 \binom{[b]}{r-q}\setminus
 \{I_{r-q}^w(s):E(w)\in\mathcal P,\ s\ne0\},       \tag{1.4}
\]

\[
 \mathcal H_q^+=
 \binom{[b]}{r+1+q}\setminus
 \{I_{r+1+q}^w(s):E(w)\in\mathcal P,\ s\ne0\},     \tag{1.5}
\]

and write \(h_q^\pm=|\mathcal H_q^\pm|\).  These are sets of distinct
missing targets; repeated occurrences are not counted repeatedly.

Each selected permutation is already a literal full cyclic row.  Restoring
its omitted start adds one occurrence on each shore at every depth.
Therefore, if \(\widetilde h_q^\pm\) are the holes of the full-row bank,

\[
 0\le h_q^\pm-\widetilde h_q^\pm\le p,\qquad
 \sum_{q\le H}
 \bigl(h_q^-+h_q^+-\widetilde h_q^--\widetilde h_q^+\bigr)
 \le2Hp=o(A)                                       \tag{1.6}
\]

whenever \(H=o(b)\), since \(p\le B\).  Thus the punctured and restored
formulations are equivalent at the \(o(A)\) scale.  We retain the literal
punctured holes in Sections 2--5 because those are the targets which a
cover-down must actually repair.

## 2. Capacity forces hole-enriched rows

Put

\[
 Q=\min\left\{H,\left\lfloor{\sqrt{rx}\over4}\right\rfloor\right\}.
                                                               \tag{2.1}
\]

Assume \(rx\ge64\).  For every \(1\le q\le Q\),

\[
 { \binom b{r-q}\over L}
 =\prod_{j=1}^{q-1}{r-j\over r+j+2}
 \ge1-{(q-1)(q+2)\over r}
 \ge1-{x\over8}.                                  \tag{2.2}
\]

Every shore has only \(2rp=(1-x)L\) indexed occurrences.  Hence

\[
 h_q^-\ge {7x\over8}L,\qquad
 h_q^+\ge {7x\over8}L,                             \tag{2.3}
\]

and consequently

\[
 \mathfrak h_Q:=
 \sum_{q=1}^Q(h_q^-+h_q^+)
 \ge {7\over4}xLQ.                                \tag{2.4}
\]

Now let \(C\) be any full cyclic row.  Its score against the *pre-existing*
punctured holes is

\[
\begin{aligned}
 S_Q(C)=\sum_{q=1}^Q\bigl(
 &|\{s\in\mathbb Z_b:I_{r-q}^C(s)\in\mathcal H_q^-\}|\\
 +&|\{s\in\mathbb Z_b:I_{r+1+q}^C(s)\in\mathcal H_q^+\}|
 \bigr).
                                                               \tag{2.5}
\end{aligned}
\]

Thus \(0\le S_Q(C)\le2bQ\).

### Theorem 2.1 (minimum cover-down enrichment)

Let \(\mathcal R\) be a family of \(s\) added physical cyclic rows.  If,
after adjoining them, the aggregate holes through depth \(Q\) are at most
\(\varepsilon A\), then

\[
 \boxed{
 \sum_{C\in\mathcal R}S_Q(C)
 \ge {7\over4}xLQ-\varepsilon A.}                 \tag{2.6}
\]

In particular,

\[
 \boxed{
 \max_{C\in\mathcal R}S_Q(C)
 \ge {{7\over4}xLQ-\varepsilon A\over s}.}         \tag{2.7}
\]

Suppose now that \(x=r^{-\alpha}(1+o(1))\) for fixed
\(0<\alpha<1/3\), that \(Q=\lfloor\sqrt{rx}/4\rfloor\), that
\(\varepsilon=o(1)\), and that

\[
                         s\le KxB                 \tag{2.8}
\]

for a fixed \(K>0\).  Then

\[
 {1\over s}\sum_{C\in\mathcal R}S_Q(C)
 \ge\left({7\over4K}+o(1)\right)bQ.               \tag{2.9}
\]

Thus a \(\Theta(x\operatorname {Cat}_r)\) cover-down cannot be made from
typical rows: its average selected row must place a positive constant
fraction of all its \(2bQ\) shallow-band windows in the actual hole sets.

#### Proof

Every original hole which disappears is a window of at least one added
row.  Counting a target once on the left and with all its possible added
occurrences on the right gives

\[
 \mathfrak h_Q-\varepsilon A
 \le\sum_{C\in\mathcal R}S_Q(C).
\]

Use (2.4) to obtain (2.6), and divide by \(s\) for (2.7).  Under the
asymptotic hypotheses,

\[
 xQ={1+o(1)\over4}\sqrt r\,x^{3/2}\longrightarrow\infty.
\]

Hence \(\varepsilon A=o(xAQ)\).  Substitute \(L/A=1-o(1)\),
\(B=A/b\), and (2.8) into (2.6) to get (2.9).  \(\square\)

This is stronger than the scalar occurrence obstruction.  It says that
having enough new windows is not sufficient: a minimal cover-down must
find rows enriched in the *joint physical hole flag* by a factor of order
\(1/x\).

### Corollary 2.2 (many hole-rich starts)

For a row \(C\), let \(d_C(s)\) be the number of its \(2Q\) lower/upper
targets at start \(s\) which belong to the corresponding hole sets.  If

\[
                         S_Q(C)\ge\eta bQ,\qquad0<\eta\le2,      \tag{2.10}
\]

then at least

\[
                         {\eta\over4-\eta}\,b       \tag{2.11}
\]

starts satisfy

\[
                         d_C(s)\ge{\eta Q\over2}.   \tag{2.12}
\]

#### Proof

Let \(g\) be the number of starts satisfying (2.12).  At a rich start use
the trivial bound \(d_C(s)\le2Q\), and at every other start use
\(d_C(s)<\eta Q/2\).  Then

\[
 \eta bQ\le S_Q(C)
 \le2Qg+{\eta Q\over2}(b-g).
\]

Rearranging gives (2.11).  \(\square\)

Hence the required enrichment is genuinely nested: many starts of a
selected row must simultaneously hit a positive fraction of the depth
levels.

### Proposition 2.3 (uniform rows are short by a factor \(1/x\))

Let \(C\) be a uniformly random oriented cyclic order modulo rotation.
Then exactly

\[
 \boxed{
 \mathbb ES_Q(C)
 =b\sum_{q=1}^Q
 \left(
 {h_q^-\over\binom b{r-q}}+
 {h_q^+\over\binom b{r+1+q}}
 \right).}                                        \tag{2.13}
\]

If, in the best-capacity regime,

\[
                         h_q^-+h_q^+=O(xA)
                         \quad(1\le q\le Q),        \tag{2.14}
\]

then \(\mathbb ES_Q(C)=O(xbQ)\).  Comparison with (2.9) gives the
enrichment factor \(\Omega(1/x)\).

#### Proof

At rank \(k\), a cyclic row has \(b\) distinct proper windows and symmetry
makes each target occur with probability \(b/\binom bk\).  Sum the
indicators over the two shores and all depths.  Under (2.14), equation
(2.2) gives \(\binom b{r-q}=\Theta(A)\), uniformly for \(q\le Q\).
\(\square\)

### 2.4 Why a residual one-rank wreath packing is not yet the cover-down

Suppose one proves a perfect or near-perfect packing of the rank-\((r-1)\)
holes into \(O(xB)\) physical rows.  This certifies only

\[
                         \Theta(xA)                \tag{2.15}
\]

hole hits at depth one.  The unavoidable shallow-band ledger (2.4) is

\[
                         \Theta(xAQ),              \tag{2.16}
\]

and \(Q\to\infty\) in the current range.  The rows used by the one-rank
packing do have deeper windows, but rank-one packing supplies no assertion
that those particular windows lie in the deeper hole sets.  The exact
additional statement needed is precisely

\[
 \sum_{C\in\mathcal R}S_Q(C)=\Omega(xAQ).          \tag{2.17}
\]

Thus a residual wreath packing at one rank is a useful first stage only
when coupled to the hole-enrichment theorem (2.17).  Treating its automatic
deeper windows as covered without proving (2.17) would replace physical
coinstantiation by an unsupported marginal inference.

## 3. The exact positive fractional question

Let \(\Omega\) be the finite set of oriented cyclic orders modulo rotation.
For this section, replace the punctured hole sets by the restored full-bank
hole sets.  Equation (1.6) changes the aggregate by only \(o(A)\).  No
restored base row contains one of these holes, so base rows may be deleted
from \(\Omega\) without changing any incidence below.  Let

\[
 \mathcal H=\bigsqcup_{q=1}^H
             (\mathcal H_q^-\sqcup\mathcal H_q^+)               \tag{3.1}
\]

be the shore-tagged hole universe.  For \(T\in\mathcal H\) and
\(C\in\Omega\), put \(M_{T,C}=1\) when \(T\) is a cyclic window of \(C\)
at its tagged rank, and put \(M_{T,C}=0\) otherwise.

Define the fractional physical cover number

\[
 \tau^*(\mathcal H)=
 \min\left\{\sum_{C\in\Omega}y_C:
 y_C\ge0,\quad
 \sum_CM_{T,C}y_C\ge1\quad(T\in\mathcal H)\right\}.              \tag{3.2}
\]

### Theorem 3.1 (exact row-score dual)

\[
 \boxed{
 \tau^*(\mathcal H)=
 \max\left\{\sum_{T\in\mathcal H}z_T:
 z_T\ge0,\quad
 \sum_TM_{T,C}z_T\le1\quad(C\in\Omega)\right\}.}                 \tag{3.3}
\]

In particular, if

\[
 \Delta(\mathcal H)=
 \max_{C\in\Omega}|\{T\in\mathcal H:M_{T,C}=1\}|,                \tag{3.4}
\]

then

\[
                         \boxed{
 \tau^*(\mathcal H)\ge{|\mathcal H|\over\Delta(\mathcal H)}.}    \tag{3.5}
\]

The weighted version of (3.3) is the exact sharp reduction: a fractional
cover of mass \(O(xB)\) exists if and only if every nonnegative weighting
of the actual holes has a row carrying at least the corresponding
\(\Omega(1/(xB))\) fraction of its total weight.

#### Proof

Equation (3.3) is finite covering-LP duality.  For completeness, weak
duality follows by

\[
 \sum_Tz_T
 \le\sum_Tz_T\sum_CM_{T,C}y_C
 =\sum_Cy_C\sum_TM_{T,C}z_T
 \le\sum_Cy_C.                                     \tag{3.6}
\]

We include the short Farkas proof of equality.  The finite Farkas
alternative says that exactly one of

\[
                         Av=b,\quad v\ge0,
\]

and

\[
                         \xi^{\mathsf T}A\ge0,\quad
                         \xi^{\mathsf T}b<0
\]

holds.  Indeed, the nonnegative cone generated by the finitely many
columns of \(A\) is closed; if it does not contain \(b\), a hyperplane
separating \(b\) from its closest point in that cone gives \(\xi\).

Fix \(\delta>0\).  By the definition of \(\tau^*\), the system

\[
 My-u=\mathbf1,\qquad
 \mathbf1^{\mathsf T}y+v=\tau^*-\delta,\qquad
 y,u,v\ge0                                         \tag{3.7}
\]

is infeasible.  Apply Farkas to its columns.  We obtain a vector
\((-\widehat z,\lambda)\) with

\[
 \widehat z\ge0,\qquad
 M^{\mathsf T}\widehat z\le\lambda\mathbf1,\qquad
 \mathbf1^{\mathsf T}\widehat z>
              \lambda(\tau^*-\delta).              \tag{3.8}
\]

Every hole belongs to some cyclic row.  Hence \(\lambda=0\) in (3.8)
would force \(\widehat z=0\), a contradiction, so \(\lambda>0\).
After division by \(\lambda\), (3.8) is dual-feasible and has value
larger than \(\tau^*-\delta\).  Each dual coordinate is at most one,
because some row contains its target.  Letting \(\delta\downarrow0\)
and taking a convergent subsequence gives a dual vector of value
\(\tau^*\).  Together with (3.6), this proves (3.3).

For (3.5), take \(z_T=1/\Delta(\mathcal H)\) in the dual.  \(\square\)

Applying (3.5) to the first \(Q\) depths and using (2.4) recovers Theorem
2.1 at the fractional level.  More importantly, (3.3) identifies the
missing theorem exactly as a positive-cone statement.  Rank, Gram
eigenvalues, and signed spanning do not control the dual inequalities in
(3.3).

The integral rounding of a positive fractional cover is, however, cheap.

### Theorem 3.2 (logarithmic independent rounding)

Let \(y\) be feasible in (3.2), with total mass \(t\), and let
\(\lambda\ge1\).  There is a family \(\mathcal R\) of distinct cyclic rows
such that

\[
 |\mathcal R|\le4\lambda t,\qquad
 \left|\mathcal H\setminus
       \bigcup_{C\in\mathcal R}
       \{T\in\mathcal H:M_{T,C}=1\}\right|
 \le4|\mathcal H|e^{-\lambda}.                    \tag{3.9}
\]

Consequently, if

\[
 \tau^*(\mathcal H)=O(xB),\qquad
 x=r^{-\alpha}\quad(\alpha>0\text{ fixed}),        \tag{3.10}
\]

then choosing \(\lambda=3\log r\) gives an integral physical cover-down
with

\[
 |\mathcal R|=O(x\log r\,B)=o(B),                  \tag{3.11}
\]

\[
 b|\mathcal R|=O(x\log r\,A)=o(A),                \tag{3.12}
\]

and only \(o(A)\) aggregate holes.  Thus no Baranyai--Katona factor or
target-disjoint rounding theorem is needed after the fractional bound
(3.10) is proved.

#### Proof

Select every row \(C\) independently with probability

\[
                         p_C=\min\{1,\lambda y_C\}.               \tag{3.13}
\]

The expected number selected is at most \(\lambda t\).  Fix a hole \(T\).
If some incident row has \(\lambda y_C\ge1\), that row is selected
certainly.  Otherwise,

\[
\begin{aligned}
 \Pr(T\text{ remains uncovered})
 &=\prod_{C:M_{T,C}=1}(1-\lambda y_C)\\
 &\le\exp\left\{-\lambda
       \sum_{C:M_{T,C}=1}y_C\right\}
 \le e^{-\lambda},                                \tag{3.14}
\end{aligned}
\]

using feasibility of \(y\).  Hence the expected number of uncovered holes
is at most \(|\mathcal H|e^{-\lambda}\).  Markov's inequality and a union
bound show that with positive probability both random quantities are at
most four times their expectations, proving (3.9).

There are at most \(2HA\) shore-tagged holes.  For \(H\le r\) and
\(\lambda=3\log r\), the second bound in (3.9) is \(O(A/r^2)=o(A)\).
Equations (3.11)--(3.12) follow from \(B=A/b\) and
\(x\log r=o(1)\).  \(\square\)

### Corollary 3.3 (residual-biased row sampler)

For \(s>0\), the inequality

\[
                         \tau^*(\mathcal H)\le s                 \tag{3.15}
\]

holds if and only if there is a probability distribution \(\pi\) on
physical cyclic rows such that

\[
 \boxed{
 \Pr_{C\sim\pi}(M_{T,C}=1)\ge {1\over s}
 \qquad(T\in\mathcal H).}                           \tag{3.16}
\]

Thus the exact positive input sufficient for the cover-down is a sampler
which raises every residual target's row-incidence probability from its
uniform scale \(\Theta(1/B)\) to \(\Omega(1/(xB))\).  Once that sampler
exists, \(O(xB\log r)\) independent samples close the physical holes by
Theorem 3.2.

#### Proof

If \(y\) is feasible with total mass \(0<t\le s\), set
\(\pi(C)=y_C/t\).  Every cover constraint gives inclusion probability at
least \(1/t\ge1/s\).  Conversely, \(y_C=s\pi(C)\) is feasible in (3.2).
The empty-hole case is immediate.  \(\square\)

### Proposition 3.4 (normalized co-hole Gram criterion)

For \(T\in\mathcal H\), let

\[
                         D_T=\sum_{C\in\Omega}M_{T,C}             \tag{3.17}
\]

be its row degree, and define

\[
 R_{\mathcal H}(U)=
 \sum_{C:M_{U,C}=1}
 \sum_{T\in\mathcal H}{M_{T,C}\over D_T}
 \qquad(U\in\mathcal H).                           \tag{3.18}
\]

If

\[
 \boxed{
 \min_{U\in\mathcal H}R_{\mathcal H}(U)
 \ge {|\mathcal H|\over s},}                       \tag{3.19}
\]

then \(\tau^*(\mathcal H)\le s\).  In particular, (3.19) with
\(s=O(xB)\) proves the fractional input needed by Theorem 3.2.

#### Proof

Give a row \(C\) weight

\[
                         w_C=\sum_{T\in\mathcal H}{M_{T,C}\over D_T}.
                                                               \tag{3.20}
\]

Double counting gives

\[
                         \sum_Cw_C=|\mathcal H|.                 \tag{3.21}
\]

Thus \(\pi(C)=w_C/|\mathcal H|\) is a probability distribution.  For a
fixed hole \(U\),

\[
 \Pr_{C\sim\pi}(M_{U,C}=1)
 ={R_{\mathcal H}(U)\over|\mathcal H|}
 \ge {1\over s}.                                    \tag{3.22}
\]

Apply Corollary 3.3.  \(\square\)

The vector \(R_{\mathcal H}\) is exactly a degree-normalized block Gram
operator for the restricted row-incidence matrix \(M\).  If the candidate
catalogue is the full cyclic-order catalogue, its blocks are
\(A_kA_\ell^{\mathsf T}/D_\ell\).  This is the precise way in which the
wreath Gram data can help.  Their positive eigenvalues control averaged
\(\ell_2\) behavior of (3.18), but (3.19) is a pointwise lower bound.
Positivity of the eigenvalues alone does not imply it.  At the current
scale \(|\mathcal H|/(xB)=\Theta(bQ)\), so (3.19) asks every hole to see
\(\Theta(bQ)\) normalized co-hole mass among the rows containing it.

## 4. A long-flag-arc bypass

The minimal \(O(xB)\)-row target requires whole-row-scale enrichment.  A
larger but still \(o(B)\) cover-down can use long physical arcs.

For a row \(C\) and a cyclic interval \(J\subseteq\mathbb Z_b\) of
\(L_0\) starts, define its depth-\(H\) flag arc

\[
 \mathcal F_H(C,J)=
 \bigsqcup_{q=1}^H
 \left(
 \{I_{r-q}^C(s):s\in J\}\sqcup
 \{I_{r+1+q}^C(s):s\in J\}
 \right).                                         \tag{4.1}
\]

The two copies are shore-tagged.  The underlying row is a full physical
permutation; \(J\) only records which of its starts are charged to the
cover-down.

### Theorem 4.1 (promotion of covering flag arcs)

Suppose there is a family

\[
 \mathscr A=\{(C_j,J_j):1\le j\le M\}              \tag{4.2}
\]

with distinct underlying rows not already in the restored base bank,
every \(|J_j|=L_0\), and

\[
 \left|
 \mathcal H\setminus
 \bigcup_{j=1}^M\mathcal F_H(C_j,J_j)
 \right|=o(A).                                    \tag{4.3}
\]

If

\[
                         Mb=o(A),                 \tag{4.4}
\]

then adjoining the \(M\) full rows \(C_j\) gives a literal physical
cover-down with aggregate holes \(o(A)\).  At every rank it adds only
\(Mb=o(A)\) total occurrences; in particular the central occurrence
overhead and the relative number of added rows are \(o(A)\) and \(o(B)\),
respectively.  No claim that the duplicate counts summed over all \(H\)
ranks are \(o(A)\) is needed or made.

In particular, if

\[
 M=O\left({xA\over L_0}\right),
 \qquad {xb\over L_0}=o(1),                        \tag{4.5}
\]

then (4.4) holds.  The concrete choice

\[
                         L_0=\lceil b\sqrt x\rceil             \tag{4.6}
\]

turns the target scale in (4.5) into

\[
                         M=O(\sqrt x\,B)=o(B),                  \tag{4.7}
\]

with promotion overhead \(O(\sqrt x\,A)=o(A)\).

#### Proof

Every target in the union in (4.3) occurs in its underlying full row, so
adjoining those rows leaves at most the targets counted in (4.3) missing.
One full row has exactly \(b\) indexed windows at every proper rank.
Thus the added occurrence and worst-case duplicate count at each rank is
at most \(Mb\).  Equations (4.5)--(4.7) are direct substitutions using
\(B=A/b\).  \(\square\)

This theorem avoids any exact wreath-factor assumption.  Its remaining
input is a matching/cover theorem for long residual flag arcs.  It is
strictly weaker than finding \(xB\) almost entirely hole-supported full
rows, while still preserving coefficient one asymptotically.

More generally, for any scale \(y\) with \(x\ll y=o(1)\), taking

\[
                         L_0\asymp {xb\over y}                  \tag{4.8}
\]

reduces the desired promoted row count to \(O(yB)\).  This gives a
continuous tradeoff between the difficult minimal cover-down and the
long-arc interface.

## 5. The exact structure inherited from a physical bank

Restore the omitted starts and consider the full bank of \(p\) rows.  At
rank \(k\), let

\[
 \mu_k(T)=|\{(C,s):C\text{ is a bank row},\
                       I_k^C(s)=T\}|,              \tag{5.1}
\]

\[
 H_k=\{T:\mu_k(T)=0\},\qquad
 e_k(T)=(\mu_k(T)-1)_+.                            \tag{5.2}
\]

Let \(U_k\) be the point-versus-\(k\)-set incidence operator,

\[
                         (U_kf)(a)=\sum_{T\ni a}f(T).            \tag{5.3}
\]

### Theorem 5.1 (hole--duplicate margin identity)

Pointwise on the target layer,

\[
                         1-\mu_k=\mathbf1_{H_k}-e_k.             \tag{5.4}
\]

Consequently,

\[
 \boxed{
 |H_k|-\sum_Te_k(T)=\binom bk-bp,}                 \tag{5.5}
\]

and, for every ground coordinate \(a\),

\[
 \boxed{
 (U_k\mathbf1_{H_k})(a)-(U_ke_k)(a)
 =\binom{b-1}{k-1}-kp.}                            \tag{5.6}
\]

#### Proof

If \(\mu_k(T)=0\), both sides of (5.4) equal one.  If
\(\mu_k(T)\ge1\), both equal \(1-\mu_k(T)\).  Summing gives (5.5), since
the bank has \(bp\) indexed rank-\(k\) windows.

In one cyclic row, a fixed coordinate belongs to exactly \(k\) of the
\(b\) length-\(k\) windows.  Hence

\[
                         U_k\mu_k=kp\,\mathbf1.
\]

Also \(U_k\mathbf1=\binom{b-1}{k-1}\mathbf1\).  Apply \(U_k\) to
(5.4) to obtain (5.6).  \(\square\)

This is the usable nested residual structure presently forced by the
physical bank.  Hole point-margins are balanced only after the
duplicate-excess margins are subtracted.  Thus a theorem controlling only
the cardinalities of the hole sets loses genuine information; a
cover-down may need to repair holes and redistribute duplicate excess
together.

## 6. What the wreath spectrum supplies

Let \(\Omega\) again denote all oriented cyclic orders modulo rotation.
For \(1\le k\le b-1\), let

\[
 A_k:\mathbb R^\Omega\longrightarrow
       \mathbb R^{\binom{[b]}k}
 \quad\text{with}\quad
 (A_ky)_T=\sum_Cy_C\mathbf1\{T\text{ is a }k
 \text{-window of }C\}.                            \tag{6.1}
\]

Every column contains \(b\) targets and has perfect point marginals:

\[
                         U_kA_k
 =k\,\mathbf1\,\mathbf1^{\mathsf T}.               \tag{6.2}
\]

The Petr--Turek Gram matrix at rank \(k\) is \(A_k^{\mathsf T}A_k\), up
to the harmless reversal quotient.  Its positive eigenvalues determine
the Euclidean geometry of the signed image of \(A_k\).

For completeness, the exact signed image can be proved without quoting
the spectrum.  Fix a cyclic order \(C=(1,\ldots,b)\).  For
\(2\le a\le r\), let

\[
 \tau=(1\ 2),\qquad \sigma=(a+1\ a+2),
\]

and put

\[
                         z_a=e_C-e_{\tau C}-e_{\sigma C}
                                  +e_{\tau\sigma C}.             \tag{6.3}
\]

An interval can survive this alternating sum only if its two boundary cuts
separate both swapped adjacent pairs.  The two arcs between those cuts
have lengths \(a\) and \(b-a\).  Therefore

\[
 A_kz_a=0\quad(k\ne a,b-a),                        \tag{6.4}
\]

while \(A_az_a\) is the elementary four-set square

\[
\begin{aligned}
 &e_{K\cup\{2,a+1\}}-e_{K\cup\{1,a+1\}}\\
 &\qquad-e_{K\cup\{2,a+2\}}+e_{K\cup\{1,a+2\}},
 \qquad K=\{3,\ldots,a\}.                          \tag{6.5}
\end{aligned}
\]

Relabelings of (6.5) span \(\ker U_a\): if a function is orthogonal to
all such squares, its exchange difference between two coordinates is
independent of the common \((a-1)\)-set, so the function is a sum of
point weights.  Taking orthogonal complements proves the claim.

It follows that

\[
                         \operatorname {im}A_a
 =\operatorname {span}\{\mathbf1\}\oplus\ker U_a,                \tag{6.6}
\]

and the selectors \(z_a\) act independently at distinct complementary
rank pairs.  Thus every simultaneous discrepancy with the correct point
margins has a signed real row correction.

### Theorem 6.1 (spectral verdict for the residual cover)

The positive wreath eigenvalues and (6.6) settle only the following
question:

> does a prescribed target discrepancy lie in the signed real span of
> cyclic rows?

They do not settle the cover-down question (3.2), which asks for a
**nonnegative** vector of small \(\ell_1\)-mass.  More specifically:

1. the signed deficit \(\mathbf1_{H_k}-e_k\) from (5.4) has the exact
   point margins required by (6.6), whereas the positive hole indicator
   \(\mathbf1_{H_k}\) generally does not;
2. the exact positive obstruction is the row-score dual (3.3), which is
   not bounded by rank or by positivity of the nonzero Gram eigenvalues;
3. an elementary selector (6.3) is never a support-compatible residual
   trade when \(2\le a<r\): the two positive rows \(C,\tau\sigma C\)
   share at least \(b-4\) middle windows, and the same is true of the two
   negative rows.

#### Proof

Items 1 and 2 are (5.4), (6.6), and Theorem 3.1.  For item 3, one adjacent
transposition changes exactly the two middle windows containing one
swapped position but not the other.  Two disjoint adjacent
transpositions therefore change at most four of the \(b\) middle windows.
Thus the two orders in either sign of (6.3) share at least \(b-4>0\)
middle targets and cannot both belong to a target-disjoint residual
packing.  \(\square\)

There is also a completely explicit signed simultaneous correction which
shows why affine feasibility is too weak.  Let \(u\) be the uniform
fractional middle factor on all cyclic orders, of total mass \(B\), and
let \(x_{\mathcal P}\) be the indicator of the restored \(p\)-row bank.
Then

\[
                         y=u-x_{\mathcal P}                       \tag{6.7}
\]

has total signed mass \(B-p\) and makes every rank load perfectly uniform.
But on every selected row its coefficient is \(-1+o(1)\), so its negative
mass is \((1-o(1))p=\Theta(B)\), not \(O(xB)\).  Kernel selectors may
change this signed representative, but the spectrum supplies no theorem
placing one in the nonnegative cone of (3.2).

## 7. Exact remaining cover-down alternatives

The current direct route can now be continued through either of two
precise, non-equivalent interfaces.

### Minimal-row interface

Prove that the actual punctured residual satisfies

\[
                         \tau^*(\mathcal H)=O(xB),                \tag{7.1}
\]

then round a fractional minimizer to \(O(xB)\) distinct physical rows with
only \(o(A)\) additional uncovered targets.  By Theorem 2.1, any such
proof must exploit rows with \(\Omega(bQ)\) shallow hole score and hence
many hole-rich nested starts.  Independent one-rank marginals cannot
supply this.

There is a particularly concrete sufficient form.  Let \(\mathcal C\) be
any finite candidate family of physical rows and put

\[
 d_{\mathcal C}(T)=|\{C\in\mathcal C:M_{T,C}=1\}|.               \tag{7.2}
\]

If, outside an exceptional set of \(o(A)\) aggregate holes,

\[
 d_{\mathcal C}(T)\ge D_0,\qquad
 {|\mathcal C|\over D_0}=O(xB),                   \tag{7.3}
\]

write \(\mathcal H'=\mathcal H\setminus\mathcal E\) for the nonexceptional
holes.  Assigning weight \(1/D_0\) to every candidate row gives

\[
                         \tau^*(\mathcal H')=O(xB).
\]

Theorem 3.2 covers all but \(o(A)\) targets of \(\mathcal H'\); carrying
the already exceptional set \(\mathcal E\) into the uncovered ledger still
leaves only \(o(A)\) aggregate holes.

For the actual stopped punctured process, one may take \(\mathcal C\) to
be the surviving configuration catalogue, with every configuration
promoted to its full cyclic row.  At the first lower rank, (7.3) is an
aggregate lower-degree condition on the residual hypergraph.  At deeper
ranks it is a new external-window degree condition:

\[
 \#\{F\in\mathcal C:T\text{ is a depth-}q
       \text{ window of the row underlying }F\}
 \ge D_0.                                         \tag{7.4}
\]

Thus the exact probabilistic cover-down gate is an all-depth residual
degree floor, not another integral wreath-factor theorem.  Current
maximum-degree control does not imply (7.4).

### Long-arc interface

For some \(L_0\) with

\[
                         xb\ll L_0\le b,            \tag{7.5}
\]

construct \(O(xA/L_0)\) distinct covering flag arcs satisfying (4.3).
Theorem 4.1 promotes them to full rows with \(o(A)\) cost.  Taking
\(L_0=b\sqrt x\) asks for \(O(\sqrt x\,B)\) rows rather than
\(O(xB)\), but remains fully compatible with a coefficient-one
asymptotic.

Neither interface assumes a Baranyai--Katona factor.  The first is a
positive-cone/rounding theorem on the actual residual; the second is a
long nested-arc packing theorem.  Cardinality, the wreath Gram spectrum,
and abstract chain supply alone do not prove either one.
