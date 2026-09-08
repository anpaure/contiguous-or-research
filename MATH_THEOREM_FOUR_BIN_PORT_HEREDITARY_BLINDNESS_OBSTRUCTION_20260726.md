# Four-bin port substitutions do not destroy hereditary excursion blindness

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Verdict

The proposed induction is false.

A rooted \(D_s\)-port substitution can change an early distinguished child
target, but that change does not propagate monotonically to all larger
depths. There are two exact obstructions.

1. **Swallowing blindness.** If a larger window contains both fixed ports
   of the substituted path, then its local intersection is empty because
   the ports are complementary. Its target is independent of every
   internal path choice.

2. **Matched-scale collar repayment.** The smallest nontrivial port
   rectangle, at semilength two, permutes four singleton bins while
   preserving its bare matched-scale affected histogram:

   \[
                   e_1+e_4+e_3+e_2=e_2+e_3+e_1+e_4.      \tag{0.1}
   \]

   Its residual-cap defect is therefore identical before and after the
   substitution for every background load on this bare target universe.
   Slot-dependent exterior collars need not preserve this equality; they
   are exactly the surviving parent-aligned variant isolated below.

In rooted middle-levels path-factor form, a local interval satisfies

\[
 \boxed{\displaystyle
 \bigcap_{t=i}^{j}X_t=(P\setminus A_j)\cup B_i.}           \tag{0.2}
\]

Thus a first-edge or four-bin label controls only selected intervals.
General crossing windows depend on the entire deletion and insertion flags
\(A_j,B_i\), while swallowing windows forget the flags completely.

The correct constant-one successor must be depth-adaptive: at every parent
it must route the **full** affected-window histograms into the current
residual capacities. Early four-bin dispersion alone cannot support such
an induction.

## 1. Rooted path-factor normal form

Let \(|J|=2s\), let \(D_s\subseteq\binom Js\) be the inherited Dyck port
family, and let \(\infty\notin J\). A \(D_s\)-port exact local factor is
equivalently a partition of the middle-levels inclusion graph into paths

\[
 P=X_0\subset Y_0\supset X_1\subset\cdots\subset
 Y_{s-1}\supset X_s=J\setminus P,\qquad P\in D_s.         \tag{1.1}
\]

The \(X\)-states partition \(\binom Js\), and the \(Y\)-states partition
\(\binom J{s+1}\). The \(X\)-projection is a length-\(s\) Johnson
geodesic between complementary endpoints. Hence there are unique orders

\[
 (a_1,\ldots,a_s)\text{ of }P,\qquad
 (b_1,\ldots,b_s)\text{ of }J\setminus P                 \tag{1.2}
\]

such that, with

\[
 A_t=\{a_1,\ldots,a_t\},\qquad B_t=\{b_1,\ldots,b_t\},
\]

one has

\[
                         X_t=(P\setminus A_t)\cup B_t.     \tag{1.3}
\]

### Lemma 1.1 (exact interval flags)

For \(0\le i\le j\le s\),

\[
 \boxed{\displaystyle
 \bigcap_{t=i}^{j}X_t=(P\setminus A_j)\cup B_i,}           \tag{1.4}
\]

and

\[
 \boxed{\displaystyle
 \bigcup_{t=i}^{j}X_t=(P\setminus A_i)\cup B_j.}           \tag{1.5}
\]

#### Proof

A coordinate of \(P\) occurs throughout precisely when it has not been
deleted by time \(j\), and a coordinate of \(J\setminus P\) occurs
throughout precisely when it was inserted by time \(i\). This proves
(1.4); the union statement is dual. \(\square\)

The distinguished right-child interval is only the special case

\[
 \bigcap_{t=1}^{s}X_t=\{b_1\},\qquad
 \bigcup_{t=1}^{s}X_t=J\setminus\{a_1\}.                \tag{1.6}
\]

It records the first directed Johnson edge, not the later flags.

## 2. Exact crossing collars and the blind windows

Install (1.1) in an aligned ambient parent. On a local state the ambient
middle set has the form

\[
                              E_t\;\dot\cup\;X_t,          \tag{2.1}
\]

where \(E_t\) uses coordinates outside \(J\). Let an ambient rooted window
\(W\) meet the local slab in the interval \([i,j]\), and put

\[
                              C_W=\bigcap_{t\in W}E_t.     \tag{2.2}
\]

Because the coordinate blocks are disjoint, its target is literally

\[
 \boxed{\displaystyle
 T_G(P,W)=C_W\;\dot\cup\;
       \bigl((P\setminus A_j^G(P))\cup B_i^G(P)\bigr).}    \tag{2.3}
\]

This formula includes both ambient collars. They are fixed by the outer
row and must not be replaced by a private cyclic completion of \(G\).

The three relevant types are:

* left-crossing windows, \(i=0<j<s\), with local target
  \(P\setminus A_j\);
* right-crossing windows, \(0<i<j=s\), with local target \(B_i\);
* swallowing windows, \(i=0,j=s\), with empty local target.

### Theorem 2.1 (hereditary swallowing blindness)

If an ambient window contains both ports \(X_0=P\) and
\(X_s=J\setminus P\), then

\[
                              T_G(P,W)=C_W              \tag{2.4}
\]

for every \(D_s\)-port factor \(G\). Thus no internal substitution changes
that lower target. The complementary upper target is fixed as well.

#### Proof

The local intersection is contained in

\[
                 X_0\cap X_s=P\cap(J\setminus P)=\varnothing.
\]

Equivalently, put \(i=0,j=s\) in (1.4). Port substitution fixes both
endpoints. \(\square\)

This gives blind windows at every larger scale. A new ancestor-level
substitution may change such a window, but the early substitution cannot
do so by hereditary propagation.

## 3. The smallest four-bin obstruction

Semilength one has a unique port factor. At semilength two, put
\(J=[4]\) and \(D_2=\{12,13\}\). The canonical paths are

\[
\begin{array}{c|ccc}
12&12&14&34\\
13&13&23&24
\end{array}                                               \tag{3.1}
\]

and the noncanonical port rectangle is

\[
\begin{array}{c|ccc}
12&12&23&34\\
13&13&14&24.
\end{array}                                               \tag{3.2}
\]

Both tables partition \(\binom{[4]}2\), and both have adjacent-union
palette \(\{123,124,134,234\}\), so both are exact port factors.

At depth one, the two affected consecutive-state windows in each row have
singleton targets

\[
\begin{array}{c|cc}
 &X_0\cap X_1&X_1\cap X_2\\ \hline
\text{old }12&1&4\\
\text{old }13&3&2
\end{array}
\qquad
\begin{array}{c|cc}
 &X_0\cap X_1&X_1\cap X_2\\ \hline
\text{new }12&2&3\\
\text{new }13&1&4.
\end{array}                                               \tag{3.3}
\]

### Theorem 3.1 (four-bin collar repayment)

The bare matched-scale affected profiles are identical:

\[
                        u_{\rm old}=u_{\rm new}
                        =e_1+e_2+e_3+e_4.               \tag{3.4}
\]

The distinguished second windows do change,

\[
                              (4,2)\longmapsto(3,4),      \tag{3.5}
\]

but the first, boundary-crossing windows make the compensating change

\[
                              (1,3)\longmapsto(2,1).      \tag{3.6}
\]

#### Proof

This is the literal census (3.3). If one common exterior set is adjoined
to all four slots, the same injection is applied to both sides, so equality
persists. For genuinely slot-dependent collars the four injections differ,
and no such conclusion follows. \(\square\)

The cancellation is universal at a singleton target rank, where there are
no nonempty exterior collars.

### Lemma 3.2 (singleton affected-profile rigidity)

Suppose two exact ambient middle factors differ only on a fixed collection
of rooted depth-\((m-1)\) slots. If \(u,u'\) are the singleton histograms
of those slots, then \(u=u'\).

#### Proof

Every exact factor satisfies the point-margin identity

\[
             \sum_{S\ni x}\mu_{m-1}(S)=\operatorname {Cat}_m.       \tag{3.7}
\]

At this depth \(S\) is a singleton, so the complete labelled histogram is
the same for every exact factor. Subtract the common histogram of all
unchanged slots. \(\square\)

Thus (3.4) is the smallest instance of a general exact-factor invariant,
not an accidental symmetry of the rectangle.

## 4. Residual cap

For one parent \(C\) and depth \(q\), let \(\mathcal I_{C,q}\) contain
all windows meeting an interior state, including both crossing collars.
If \(G_0\) is the old local factor, define

\[
 u_G(S)=#\{I\in\mathcal I_{C,q}:T_G(I)=S\},\qquad
 \beta(S)=\mu_q^F(S)-u_{G_0}(S).                         \tag{4.1}
\]

Then \(\beta\ge0\) and, after installing \(G\),

\[
                          \mu_q^{F[C\leftarrow G]}=\beta+u_G.       \tag{4.2}
\]

Put \(c_\beta(S)=(p-\beta(S))_+\).

### Theorem 4.1 (literal residual-cap identity)

\[
 \boxed{\displaystyle
 K_q(F[C\leftarrow G])
 =K_p(\beta)+\sum_S\bigl(u_G(S)-c_\beta(S)\bigr)_+.}      \tag{4.3}
\]

#### Proof

If \(\beta(S)\ge p\), the contribution is
\((\beta(S)-p)+u_G(S)\) and \(c_\beta(S)=0\). If
\(\beta(S)<p\), it is
\((u_G(S)-(p-\beta(S)))_+\). Sum over \(S\). \(\square\)

For the bare four-bin rectangle, or after adjoining one common collar,
(3.4) gives

\[
 \sum_S\bigl(u_{\rm new}(S)-c_\beta(S)\bigr)_+
 =
 \sum_S\bigl(u_{\rm old}(S)-c_\beta(S)\bigr)_+            \tag{4.4}
\]

for every background \(\beta\) on that target universe. There is no cap
descent at the first matched scale, even if (3.5) looks favourable in
isolation. With slot-dependent carriers one must recompute \(u_G\) from
(2.3); (3.4) is then not available.

At larger depths \(u_{\rm new}=u_{\rm old}\) need not persist, because
targets are no longer singletons. But no favourable inequality follows
from the early bins: (2.3) contains all later flag prefixes and
carrier-resolved collars, while Theorem 2.1 supplies a fixed blind core.

## 5. Consequence for constant one

An induction

\[
 \text{early four-bin split}
 \Longrightarrow
 \text{all larger-depth fibres remain split}              \tag{5.1}
\]

cannot hold:

* swallowing windows erase the whole local choice;
* one-sided crossing windows see later flag prefixes, not just the first
  edge;
* at the first uncollared matched scale, point margins force exact
  repayment;
* a moved occurrence is useful only when its destination has residual
  capacity in (4.3).

The strongest valid recursive statement is state-adaptive. At every
ancestor and every protected depth, one must choose a single integral
\(D\)-port path factor whose **full** profiles \(u_G\), computed over all
crossing starts by (2.3), fit the current capacities \(c_\beta\). Earlier
choices may be retained as boundary data, but they do not discharge the
ancestor profile inequality.

Equivalently, the missing constant-one lemma is:

> For each current parent state and all protected depths simultaneously,
> find one integral rooted middle-levels path factor whose
> carrier-resolved full affected-window histograms have total residual-cap
> defect \(o(W)\), while retaining every target whose only old witness lies
> in the replaced packet.

This is strictly stronger than hereditary four-bin dispersion. The
smallest formal obstruction is already (3.1)--(3.4).

## 6. Final statement

\[
 \boxed{\text{Early four-bin \(D\)-port substitutions do not destroy
 hereditary excursion blindness.}}                       \tag{6.1}
\]

They are genuine exact local moves and can split selected child targets.
But windows swallowing their two fixed ports remain blind at every larger
depth, and the first bare matched-scale census is exactly invariant.
Constant one therefore requires fresh ancestor-level, carrier-resolved
full-profile routing, not an induction from early bins.
