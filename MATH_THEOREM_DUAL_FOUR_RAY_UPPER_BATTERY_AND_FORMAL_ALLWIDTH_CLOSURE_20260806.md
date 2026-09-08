# A dual four-ray battery exactly cancels the complementary upper current

**Date:** 2026-08-06  
**Method:** literal interval-union classification  
**Status:** unconditional linear-word construction for the upper dual of a
native inverse-pair current.  A saturated anchor choice keeps every dual
pivot at rank `m+1`; its four extra central singleton currents cancel in
two opposite pairs.  Together with the corrected lower battery it gives one
shield-isolated eight-port block whose lower and upper currents are
respectively `-D` and `-bar(D)`.  Cancellation with the native factor move
is a formal disjoint-ledger conclusion unless the native occurrence is
coinstantiated in a host which proves all cross-native/battery intervals
fixed.

## 1. One dual ray

Let the full coordinate ground be `Omega`, with

\[
                         |\Omega|=2m+1,\qquad p=m-2.  \tag{1.1}
\]

Fix active coordinates `a,d`.  Let

\[
                 Q=(q_1,\ldots,q_p),qquad
                 Q_j=\{q_1,\ldots,q_j\},             \tag{1.2}
\]

be disjoint from `{a,d}`.  Put

\[
\begin{aligned}
 R_Q&=\Omega\setminus(Q_p\cup\{a,d\}),\\
 w&\in R_Q,\qquad C_Q=R_Q\setminus\{w\},\\
 P^{\bar a}_Q&=C_Q\cup\{d\},\\
 P^{\bar d}_Q&=C_Q\cup\{a\},\\
 H&=\{a,d\}.
\end{aligned}                                         \tag{1.3}
\]

Consider the linear port

\[
 H,\ P_Q,\ \{w\},\{q_p\},\{q_{p-1}\},\ldots,\{q_1\},\ H.
\tag{1.4}
\]

The two pivot states are `P_Q^(bar a)` and `P_Q^(bar d)`.

### Lemma 1.1 (exact complementary ray)

Changing the pivot from `P_Q^(bar a)` to `P_Q^(bar d)` has complete signed
current

\[
 [C_Q\cup\{a\}]-[C_Q\cup\{d\}]
 +\sum_{j=0}^{p}
 \left(
   [\Omega\setminus(Q_j\cup\{d\})]
   -[\Omega\setminus(Q_j\cup\{a\})]
 \right).                                             \tag{1.5}
\]

The first two terms have rank `m+1`.  Every term in the sum has rank
`2m-j`, hence lies in the strict upper range `m+2,...,2m`.  The port has
zero changed lower current.

#### Proof

An interval containing the pivot and either shield contains both `a,d`,
so its union is independent of the pivot state.  Every changed interval
therefore starts at the pivot.  The pivot-only interval gives the first
two terms of (1.5).  Every longer changed interval contains `w` and then
takes the first `p-j` rail letters for one unique `j`.  In state `bar a`
its value is

\[
\begin{aligned}
 P_Q^{\bar a}\cup\{w,q_p,\ldots,q_{j+1}\}
   &=R_Q\cup\{d,q_p,\ldots,q_{j+1}\}\\
   &=\Omega\setminus(Q_j\cup\{a\}),
\end{aligned}                                         \tag{1.6}
\]

and in state `bar d` it is

\[
                         \Omega\setminus(Q_j\cup\{d\}).
\tag{1.7}
\]

This proves (1.5).  The strict-upper value has rank

\[
                         (2m+1)-(j+1)=2m-j,           \tag{1.8}
\]

whose minimum over `0<=j<=p=m-2` is `m+2`.  Finally,
`|C_Q|=m`, so both pivot-only values have rank `m+1`. \(\square\)

Several dual ports may share adjacent copies of `H`.  Any interval meeting
two ports contains the shared shield and is fixed, even when the two ports
have different sets `R_Q`.

## 2. The four upper rails

Use the native inverse-pair banks

\[
 |X|=p,\qquad X=(x_1,\ldots,x_p),\qquad
 |Y|=p+1,\qquad Y=(y_1,\ldots,y_{p+1}).              \tag{2.1}
\]

For each desired nested rail, take the following growth order `Q` in
Lemma 1.1; the physical chain in the port is its reverse:

\[
\begin{array}{c|c|c|c|c}
\text{rail}&Q=(q_1,\ldots,q_p)&w&C_Q&\text{physical chain}\\ \hline
Y^+&(y_{p+1},y_p,\ldots,y_2)&y_1&X\cup\{b,c\}&
       (y_1,y_2,\ldots,y_p,y_{p+1})\\
Y^-&(y_1,y_2,\ldots,y_p)&y_{p+1}&X\cup\{b,c\}&
       (y_{p+1},y_p,\ldots,y_2,y_1)\\
X^+&(x_p,x_{p-1},\ldots,x_1)&b&Y\cup\{c\}&
       (b,x_1,\ldots,x_{p-1},x_p)\\
X^-&(x_1,x_2,\ldots,x_p)&b&Y\cup\{c\}&
       (b,x_p,\ldots,x_2,x_1).
\end{array}                                           \tag{2.2}
\]

Here `b,c` are the two inactive native labels.  The table includes the
anchor `w` as the first physical chain letter after the pivot.  The
truncation of the two `Y` growth orders to length `p` is load-bearing: the
native current uses `Y_j^+,Y_j^-` only for `0<=j<=p`, not the full
`(p+1)`-set `Y`.

For a signed basis vector, write

\[
                         \overline{[S]}=[\Omega\setminus S]. \tag{2.3}
\]

Let `overline(D_j)` be obtained by complementing every basis set in the
native current `D_j(X,Y;a,d)` without changing its coefficient.

Define upper-battery state `U_0` and `U_1` as follows:

* on `Y^+,X^+`, use `P^(bar d) -> P^(bar a)`;
* on `Y^-,X^-`, use `P^(bar a) -> P^(bar d)`.

### Theorem 2.1 (exact upper-battery cancellation)

At native lower index `j`, the complete upper current of `U_0 -> U_1` is

\[
                         -\overline{\mathcal D_j(X,Y;a,d)}.   \tag{2.4}
\]

The upper battery has zero current in ranks at most `m+1`.

#### Proof

Lemma 1.1 gives, in the displayed port order,

\[
\begin{aligned}
 &\overline{[Y_j^++a]}-\overline{[Y_j^++d]}
  +\overline{[X_j^++a]}-\overline{[X_j^++d]}\\
 &\quad+
  \overline{[Y_j^-+d]}-\overline{[Y_j^-+a]}
  +\overline{[X_j^-+d]}-\overline{[X_j^-+a]}.
\end{aligned}                                         \tag{2.5}
\]

This is the negative of the termwise complement of the native formula.
It remains to cancel the four pivot-only terms from Lemma 1.1.  The
`Y^+` and `Y^-` ports have the same core

\[
                         C_Y=X\cup\{b,c\},             \tag{2.6}
\]

and are traversed in opposite directions, so their currents
`[C_Y+d]-[C_Y+a]` and `[C_Y+a]-[C_Y+d]` cancel.  Likewise the two `X`
ports have the common core

\[
                         C_X=Y\cup\{c\}               \tag{2.7}
\]

and opposite directions, so their pivot-only currents cancel.  Lemma 1.1
then proves both assertions. \(\square\)

## 3. One shield-isolated bi-battery

Concatenate the four corrected lower ports and the four dual upper ports,
sharing one copy of `H={a,d}` at every adjacent boundary.  Then every
interval meeting two ports is fixed.  Hence the current of the eight-port
transition is the direct sum of the port currents:

\[
 \begin{array}{c|c}
 \text{strict lower ranks}&-\mathcal D\\
 \text{central ranks}&0\\
 \text{strict upper ranks}&-\overline{\mathcal D}.
 \end{array}                                          \tag{3.1}
\]

The standalone position count is

\[
                       8p+4+8+9=8(m-2)+21=8m+5.       \tag{3.2}
\]

Here `8p` counts the four lower and four upper rail banks, the additional
`4` counts the upper anchors, `8` counts all pivots, and `9` counts the
shared shields.

### Theorem 3.1 (physical battery-to-battery composition)

Equation (3.1) is the complete changed interval ledger of the single
eight-port linear block.  There are no hidden lower--upper or cross-port
intervals.

#### Proof

Every interval meeting two ports contains their common shield `H` and is
unchanged.  A changed interval lies inside one port.  The lower ports have
changed ranks at most `m-1`.  The upper ports have changed ranks at least
`m+2`, apart from their four rank-`m+1` pivot-only terms, which cancel in
the two equal-core opposite-direction pairs of Theorem 2.1.  Apply the two
four-port theorems and add their disjoint ledgers.
\(\square\)

## 4. Exact composition scope with the native move

The native inverse-pair factor move has lower current `D` and upper current
`bar(D)`.  Therefore its **formal occurrence ledger** plus (3.1) is zero at
every proper width.

This does not by itself prove that the native move and the bi-battery can
be performed inside one linear universal word.  The shields prove isolation
among the eight battery ports and from a fixed exterior.  They do not prove
that an interval meeting both a changed native-factor occurrence and the
battery block is unchanged, nor do they identify the native cyclic-row
occurrences with the physical battery addresses.

### Corollary 4.1 (conditional literal all-width closure)

Suppose a common host supplies:

1. one literal native inverse-pair occurrence with its complete
   occurrence-labelled lower and upper ledgers;
2. the eight-port bi-battery (3.1);
3. physical capacity separation between their named occurrences; and
4. a shielding or coinstantiation identity proving every interval crossing
   between the native region and the battery region invariant.

Then the simultaneous native move and bi-battery transition have zero
complete all-width current.

#### Proof

Under hypotheses 3--4, the total physical current is the sum of the native
and battery ledgers.  Equation (3.1) cancels the native lower and upper
currents separately. \(\square\)

The remaining problem is now a host theorem rather than an upper-current
formula: plant the native slot and the eight ports inside one simple,
resident owner carrier with only `O(1)` extra positions and with the
terminal compiler state preserved.
