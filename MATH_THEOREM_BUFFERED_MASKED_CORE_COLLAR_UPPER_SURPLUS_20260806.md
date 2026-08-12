# A buffered masked-core collar fits the exact upper-surplus ledger

## Status

The local mixed-period masked-core port protects roots, owners, and the
immediate upper row, but a growing family of such ports can disturb longer
one-seam upper witnesses.  This note enlarges the common collar by only
`Theta(sqrt(h))` source positions on each side and proves that every
remaining nonextreme upper layer has enough **scalar duplicate surplus**
to pay its complete worst-case one-seam debt.

Put

\[
 t_0=\left\lceil\sqrt{3h-2}\right\rceil,
 \qquad P=h+t_0.                                      \tag{0.1}
\]

The collar protects every crossing source width through `P`, hence every
upper rank through `q+t_0`, exactly.  If `m` masked `C6` ports are used,
the number `D_t` of distinct rank-`(q+t)` targets whose retained witness
can be destroyed satisfies the sharp raw bound

\[
 D_t\le
 \min\left\{
   \binom{2q-1}{q+t},\;
   3m\min\{h+t-1,,2(t-t_0)_+\}
 \right\}.                                            \tag{0.2}
\]

For every

\[
                         t_0+1\le t\le q-h-1,          \tag{0.3}
\]

this is at most the exact duplicate surplus

\[
 \boxed{
 D_t\le
 W-\binom{2q-1}{q+t},
 \qquad W=\binom{2q-1}{q}.}                           \tag{0.4}
\]

The top remainder excluded from (0.3) is exactly the family of complements
of size at most `h-1`.  It has subexponential size at critical width.  Its
multi-seam part is confined further to complements of size at most two.

Equation (0.4) is a cardinality theorem, not an occurrence-level repair.
It does not imply that the duplicate tickets have the right target values,
phases, lower guards, or common-cap resources.  The final provider graph
must still satisfy Hall.  No computation or search is used.

## 1. Parameters and feasibility

Let

\[
 n=2q-1,qquad s=q-h,qquad h\ge3,                     \tag{1.1}
\]

and use the two near-maximal periods

\[
 \ell_-=q+h-3,qquad \ell_+=q+h-2.                    \tag{1.2}
\]

Assume

\[
                         q\ge h+2t_0+1.                \tag{1.3}
\]

Then

\[
 2P-2=2h+2t_0-2\le q+h-3=\ell_-.                    \tag{1.4}
\]

Thus a collar of `P-1` source positions on each side fits in either
period.  Condition (1.3) is automatic for all sufficiently large critical
parameters `h=Theta(sqrt(q))`.

Choose pairwise disjoint sets

\[
 H,\quad \{a_0,a_1,a_2\},\quad
 \mathcal R=\{\rho_1,\ldots,\rho_{P-1}\},\quad
 \mathcal L=\{\lambda_1,\ldots,\lambda_{P-2}\},\quad
 \mathcal D,                                           \tag{1.5}
\]

with

\[
 |H|=s-1=q-h-1,qquad
 |\mathcal D|=q+h-2P=q-h-2t_0.                         \tag{1.6}
\]

The sizes in (1.5) sum to

\[
 (q-h-1)+3+(P-1)+(P-2)+(q+h-2P)=2q-1=n.              \tag{1.7}
\]

Give `mathcal D` a fixed order.  For a ring of period `ell_t` in
`{ell_-,ell_+}`, let `mathcal D_t` be its initial segment of size

\[
             |\mathcal D_t|=\ell_t-(2P-2).            \tag{1.8}
\]

For the long period this is all of `mathcal D`; for the short period it
omits exactly its final element.  Define

\[
 \begin{aligned}
 K_t&=H\cup\{a_t\},\\
 F_t&=\mathcal R\cup\mathcal D_t\cup\mathcal L
             \cup\{a_{t+1}\}.
 \end{aligned}                                         \tag{1.9}
\]

The unused set contains `a_(t+2)` and, for the short period, the final
element of `mathcal D`.  Hence its size is respectively one or two, as
required.

Order the moving labels from the opened cut as

\[
 \rho_1,\ldots,\rho_{P-1},\quad
 \mathcal D_t,\quad
 \lambda_{P-2},\ldots,\lambda_1,\quad a_{t+1}.        \tag{1.10}
\]

The count is `(P-1)+|mathcal D_t|+(P-2)+1=ell_t`.
Thus (1.3) proves both ground-set and period feasibility literally.

## 2. Exact buffered tensor

For `1<=i,j<=P-1`, the cumulative left and right profiles at cut `t` are

\[
 \begin{aligned}
 L_i^t&=H\cup\{a_t,a_{t+1}\}
       \cup\{\lambda_1,\ldots,\lambda_{i-1}\},\\
 R_j^t&=H\cup\{a_t\}
       \cup\{\rho_1,\ldots,\rho_j\}.
 \end{aligned}                                         \tag{2.1}
\]

Reconnect `left(t)` to `right(t+1)`.  Exactly as in the masked-core
identity,

\[
 \boxed{
 L_i^t\cup R_j^{t+1}=L_i^t\cup R_j^t}                 \tag{2.2}
\]

at every displayed address.  The common rank is

\[
                         q-h+i+j.                       \tag{2.3}
\]

Every crossing interval of width `w<=P` has a split `w=i+j` with
`1<=i,j<=P-1`, and is therefore transported pointwise.  In particular,
the rows of ranks

\[
                         q-1,q,q+1,\ldots,q+t_0        \tag{2.4}
\]

are exact at all three cuts.

All these widths are proper widths below either period.  The active
signatures `{a_t}` and `{a_t,a_(t+1)}`, together with the two ordered
prefix lengths, prove one-copy simplicity exactly as for the unbuffered
masked port.

The residence proof is also unchanged.  Common collar and remote labels
occur at a fixed offset from the beginning or end whenever they are used;
successive occurrences are separated by at least `ell_->=2h`.  Label
`a_t` is the terminal mover of block `t-1`, core throughout block `t`, and
unused in block `t+1`.  Its source-positive block has length
`ell_t+1`, and its owner run and gap are at least `h`.  Hence every one-port
mixed-period realization is biresident at deadline `h-1`.

## 3. Exact unprotected split count

Fix a crossing source width `w`.  There are `w-1` positive splits

\[
                         w=i+j,qquad i,j\ge1.          \tag{3.1}
\]

The buffered tensor protects a split exactly when

\[
                         i,j\le P-1.                   \tag{3.2}
\]

Thus the number of unprotected old crossing occurrences at one cut is

\[
 d_P(w)=
 \begin{cases}
 0,&w\le P,\\
 2(w-P),&P<w<2P-1,\\
 w-1,&w\ge2P-1.
 \end{cases}                                           \tag{3.3}
\]

Equivalently,

\[
                         d_P(w)=\min\{w-1,2(w-P)_+\}.  \tag{3.4}
\]

Indeed, in the middle range the protected indices are

\[
              w-P+1\le i\le P-1,                      \tag{3.5}
\]

of which there are `2P-w-1`; subtracting from `w-1` gives (3.3).

Suppose a connector system uses `m` masked ports.  Each port changes
three arcs.  Choose one retained witness for every upper target before
the ports are applied, and let `D_t` be the number of distinct
rank-`(q+t)` targets whose chosen witness is destroyed.  For

\[
                         w=h+t<\ell_-,                  \tag{3.6}
\]

one retained interval meets at most one opened arc in its input ring.
Even under serial reuse, summing over the three current arcs of every port
is safe.  Therefore

\[
 D_t\le
 \min\left\{
   \binom n{q+t},\;3m,d_P(h+t)
 \right\}.                                            \tag{3.7}
\]

This proves (0.2).  The second term may count the same target several
times; such collisions only improve (3.7).

Let `c` be the number of scheduled rings before joining.  A three-way
port reduces the component count by two, so

\[
                         m\le\left\lfloor{c-1\over2}\right\rfloor.
                                                               \tag{3.8}
\]

Since every period is at least `ell_-` and their sum is `W`,

\[
                         c\le {W\over q+h-3}.           \tag{3.9}
\]

Combining (3.4), (3.7)--(3.9) gives the safe coarse estimate

\[
 {D_t\over W}
 \le {3(h+t-1)\over2(q+h-3)}.                         \tag{3.10}
\]

The sharp estimate replaces `h+t-1` in (3.10) by
`d_P(h+t)`.

## 4. Exact binomial-surplus domination

Put

\[
 U_t=\binom{2q-1}{q+t},
 \qquad R_t={U_t\over W}.                              \tag{4.1}
\]

Then

\[
 R_t=\prod_{j=1}^t{q-j\over q+j}
    =\prod_{j=1}^t\left(1+{2j\over q-j}\right)^{-1}. \tag{4.2}
\]

Since a product of positive `(1+b_j)` is at least
`1+sum_j b_j`,

\[
 R_t\le {q\over q+t(t+1)},
 \qquad
 1-R_t\ge {t(t+1)\over q+t(t+1)}.                     \tag{4.3}
\]

### Theorem 4.1 (every nonextreme layer has enough scalar surplus)

For every `t` in (0.3),

\[
                         D_t\le W-U_t.                 \tag{4.4}
\]

#### Proof

By (0.1), `t>=t_0+1` implies

\[
 (t-1)^2\ge3h-2,
\]

and hence

\[
                         t(t+1)\ge3(h+t-1).             \tag{4.5}
\]

There are two cases.

If `R_t<=1/2`, the first term in (3.7) gives

\[
                         D_t\le U_t\le W-U_t.           \tag{4.6}
\]

If `R_t>1/2`, equation (4.3) forces `t(t+1)<q`.  Therefore

\[
 1-R_t
 \ge {t(t+1)\over2q}
 \ge {3(h+t-1)\over2q}
 \ge {3(h+t-1)\over2(q+h-3)}.                         \tag{4.7}
\]

The final term dominates `D_t/W` by (3.10), proving (4.4).
The upper limit `t<=q-h-1` ensures `h+t<=q-1<ell_-`, which is precisely
the one-seam range used in (3.6). \(\square\)

For `1<=t<=t_0`, equation (2.2) gives `D_t=0`.  Thus every upper layer
through rank `2q-h-1` is either transported exactly or has aggregate debt
at most its exact binomial duplicate surplus.

## 5. The extreme top remainder

The omitted indices are

\[
                         q-h\le t\le q-1.              \tag{5.1}
\]

Writing

\[
                         j=(2q-1)-(q+t)=q-1-t,          \tag{5.2}
\]

their targets are exactly

\[
 \mathcal E_h
   =\{R-X:X\subseteq R,\ |X|\le h-1\}.               \tag{5.3}
\]

Hence

\[
                         |\mathcal E_h|
             =\sum_{j=0}^{h-1}\binom{2q-1}{j}.        \tag{5.4}
\]

For `h=O(sqrt(q))`,

\[
 |\mathcal E_h|
 \le h\left({e(2q-1)\over h-1}\right)^{h-1}
 =\exp(O(h\log(q/h)))
 =\exp(o(q)).                                          \tag{5.5}
\]

In particular it is `o(W/q^A)` for every fixed `A`.

There is a sharper geometric split.  A complete period-`ell_+` block has
support `R-{z}`, while a complete period-`ell_-` block has support
`R-{z_1,z_2}`.  Any interval meeting two or more block seams contains a
whole intermediate block, so its complement has size at most two.  Thus
the entire multi-seam alphabet is

\[
 \mathcal E_{\le2}
   =\{R-X:|X|\le2\},
 \qquad
 |\mathcal E_{\le2}|=1+(2q-1)+\binom{2q-1}{2}.        \tag{5.6}
\]

The genuinely unresolved extreme one-seam remainder is consequently

\[
 \boxed{
 \mathcal E_h-\mathcal E_{\le2},
 \qquad
 \left|\mathcal E_h-\mathcal E_{\le2}\right|
   =\sum_{j=3}^{h-1}\binom{2q-1}{j}.}                 \tag{5.7}
\]

It is subexponential but not bounded.  It therefore cannot simply be
appended in an additive-constant proof.

## 6. Exact Hall scope

At source width `h+t`, an upper-complete ring factor has `W` physical
occurrences on `U_t` named targets, so its total duplicate excess is

\[
                         W-U_t.                         \tag{6.1}
\]

Theorem 4.1 proves that this aggregate excess is at least the worst-case
number of destroyed target values.  It does **not** provide a matching
from those values to usable duplicate occurrences.

Let `mathcal D_t` be the actual destroyed-target set and let
`mathcal P_t` be a capacity-faithful bank of duplicate physical tickets.
A right ticket records its donor target, occurrence, phase, side, lower
guards, cap state, and every resource consumed by its use.  Join
`U in mathcal D_t` to `p in mathcal P_t` when `p` can serve or be
reconfigured to serve `U` while retaining one protected occurrence of its
donor.  The exact remaining condition is

\[
 \boxed{
 |N(X)|\ge|X|\qquad\text{for every }X\subseteq\mathcal D_t.}            \tag{6.2}
\]

If nominal tickets share an unencoded resource, they must first be merged
into complete resource packets or treated by the corresponding
matching-with-conflicts theorem.  Neither (0.4) nor the subexponential
bound (5.5) implies (6.2).

Accordingly, the buffered collar closes the exact **scalar** upper-current
gate for every nonextreme rank.  What remains is provider Hall for those
layers, plus a protected occurrence bank for the explicit extreme family
(5.7), correlated with the one-copy masked-ring cover-down.

