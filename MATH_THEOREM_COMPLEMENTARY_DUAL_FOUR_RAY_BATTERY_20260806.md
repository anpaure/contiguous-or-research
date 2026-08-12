# Superseded draft: complementary dual four-ray battery

> **DO NOT CITE.**  This draft was independently audited and replaced by
> `MATH_THEOREM_DUAL_FOUR_RAY_UPPER_BATTERY_AND_FORMAL_ALLWIDTH_CLOSURE_20260806.md`
> (with audit
> `MATH_AUDIT_DUAL_FOUR_RAY_UPPER_BATTERY_20260806.md`).  The replacement
> has the corrected `8m+5` shared-shield count and the exact conditional
> native-composition scope.  The calculations below are retained only as
> derivational lineage.

**Date:** 2026-08-06  
**Method:** literal interval-union calculation  
**Status:** unconditional word-level current theorem.  A rank-saturated
version uses no letter larger than the native rank-`(m+1)` owner shore.
Together with the proper-lower battery in
`MATH_THEOREM_FOUR_RAY_SHIELDED_BATTERY_CANCELS_INVERSE_CURRENT_20260806.md`,
it cancels the complete lower and upper interval currents of one native
inverse-pair move.  It does not yet prove that the eight ray blocks coexist
inside a simple resident owner carrier with only bounded extra positions.

## 1. A complementary one-sided ray port

Let the coordinate ground be `Omega`, let `a,d` be distinct coordinates,
and let

\[
                 Z=(z_1,\ldots,z_t)
\tag{1.1}
\]

be an ordered list disjoint from `{a,d}`.  Put

\[
 R=\Omega\setminus (Z\cup\{a,d\}),\qquad
 K=R\cup\{a,d\},                                    \tag{1.2}
\]

and define the two large pivot letters

\[
 P_a=R\cup\{d\}=\Omega\setminus(Z\cup\{a\}),\qquad
 P_d=R\cup\{a\}=\Omega\setminus(Z\cup\{d\}).       \tag{1.3}
\]

Here the subscript records the endpoint omitted by the pivot.  Consider the
shielded word block

\[
       K,\ P_e,\ \{z_t\},\{z_{t-1}\},\ldots,\{z_1\},\ K,
              \qquad e\in\{a,d\}.                   \tag{1.4}
\]

For `0<=j<=t`, write `Z_j={z_1,...,z_j}`.

### Lemma 1.1 (exact complementary ray current)

Changing the pivot state from `P_a` to `P_d` changes the complete interval
multiset by

\[
 \boxed{
   \sum_{j=0}^{t}
       \left([\Omega\setminus(Z_j\cup\{d\})]
             -[\Omega\setminus(Z_j\cup\{a\})]\right).}
                                                               \tag{1.5}
\]

Every changed value has rank between `|Omega|-t-1` and `|Omega|-1`.

#### Proof

An interval avoiding the pivot is fixed.  An interval containing either
shield contains `K`, and `K` contains both pivot letters `P_a,P_d`; hence
that interval is also fixed.  The remaining intervals start at the pivot
and end after `ell` letters of the reversed chain, for `0<=ell<=t`.

Set `j=t-ell`.  In state `e` their value is

\[
 P_e\cup\{z_t,\ldots,z_{j+1}\}
     =\Omega\setminus(Z_j\cup\{e\}).                 \tag{1.6}
\]

Subtracting the `a` state from the `d` state proves (1.5).  The rank in
(1.6) is `|Omega|-j-1`, giving the displayed range.  \(\square\)

The large pivot in (1.3) is useful for seeing the complement identity, but
it is one rank too large for a central owner carrier.  The following
refinement removes that defect.

### Lemma 1.2 (rank-saturated complementary port)

Choose one anchor `w in R`, put `C=R minus {w}`, and define

\[
 Q_a=C\cup\{d\},\qquad Q_d=C\cup\{a\},\qquad H=\{a,d\}.             \tag{1.7}
\]

In the block

\[
       H,\ Q_e,\ \{w\},\ \{z_t\},\ldots,\{z_1\},\ H,              \tag{1.8}
\]

the transition `e=a -> e=d` has complete current

\[
 [C\cup\{a\}]-[C\cup\{d\}]
 +\sum_{j=0}^{t}
   \left([\Omega\setminus(Z_j\cup\{d\})]
        -[\Omega\setminus(Z_j\cup\{a\})]\right).                   \tag{1.9}
\]

The first two terms are the singleton-pivot current.  Every other changed
value is a complementary ray value from (1.5).

#### Proof

The two pivot letters have common part `C` and symmetric difference
`{a,d}`.  Hence an interval containing either adjacent `H` has the same
union in both states.  A changed interval avoiding the shields starts at
the pivot.  The length-one interval gives the first two terms of (1.9).
After the anchor and `t-j` reversed rail letters its value is

\[
 Q_e\cup\{w,z_t,\ldots,z_{j+1}\}
  =R\cup\bigl(Z\setminus Z_j\bigr)\cup
     \bigl(\{a,d\}\setminus\{e\}\bigr)
  =\Omega\setminus(Z_j\cup\{e\}).                              \tag{1.10}
\]

These are all changed intervals.  \(\square\)

Several saturated ports may share the same `H` between them.  Every
cross-port interval then contains `H` for each changed pivot it meets, so
it is fixed.

## 2. The four dual ports

Use the native inverse-pair notation

\[
 |\Omega|=2m+1,\qquad p=m-2,\qquad |X|=p,\quad |Y|=p+1,            \tag{2.1}
\]

where `X,Y,{a,b,c,d}` partition `Omega`.  Only `a,d` enter the current.
For `0<=j<=p`, let `X_j^-,X_j^+` and `Y_j^-,Y_j^+` be the prefix and suffix
profiles appearing in the native current

\[
\begin{aligned}
 \mathcal D_j(X,Y;a,d)={}&
 [Y_j^++d]+[Y_j^-+a]-[Y_j^++a]-[Y_j^-+d]\\
 &+[X_j^-+a]+[X_j^++d]-[X_j^-+d]-[X_j^++a].          \tag{2.2}
\end{aligned}
\]

The four profile chains, in their increasing orders, are

\[
\begin{array}{c|c}
Y^+&(y_{p+1},y_p,\ldots,y_2)\\
Y^-&(y_1,y_2,\ldots,y_p)\\
X^+&(x_p,x_{p-1},\ldots,x_1)\\
X^-&(x_1,x_2,\ldots,x_p).
\end{array}                                             \tag{2.3}
\]

For each row of (2.3), build the saturated complementary port of Lemma 1.2.
Thus the literal singleton chain after the anchor is the **reverse** of the
row shown in (2.3).  Choose anchors

\[
\begin{array}{c|c|c}
\text{port}&w&C=\Omega\setminus(Z\cup\{a,d,w\})\\ \hline
Y^+&y_1&X\cup\{b,c\}\\
Y^-&y_{p+1}&X\cup\{b,c\}\\
X^+&b&Y\cup\{c\}\\
X^-&b&Y\cup\{c\}.
\end{array}                                                     \tag{2.4}
\]

The anchors are outside their respective full profile chains, as required.
Crucially, the two `Y` ports have the same central pivot core, and the two
`X` ports have the same central pivot core.

Let dual state `U_0` use endpoint state `d` on the `Y^+,X^+` ports and
endpoint state `a` on the `Y^-,X^-` ports.  Let `U_1` swap all four endpoint
states.  Recall from (1.3) that endpoint state `e` means pivot letter `P_e`.

### Theorem 2.1 (exact upper-current cancellation)

The complete changed **upper** interval current of `U_0 -> U_1` is

\[
                         -\overline{\mathcal D_j(X,Y;a,d)}       \tag{2.5}
\]

at every complementary upper rank `2m-j`, `0<=j<=p`.  It is zero in every
rank at most `m+1`.

The aggregate current at rank `m+1` is zero, and the current is zero at
every smaller rank.  Here the bar sends each basis vector `[S]` to
`[Omega minus S]`, retaining its coefficient.

#### Proof

For any increasing profile chain `Z_j`, Lemma 1.1 says that the endpoint
transition `a -> d` contributes

\[
       [\overline{Z_j+d}]-[\overline{Z_j+a}],         \tag{2.6}
\]

while `d -> a` contributes its negative.  In `U_0 -> U_1`, the `Y^+,X^+`
ports make `d -> a`, and the `Y^-,X^-` ports make `a -> d`.  Adding the four
currents gives

\[
\begin{aligned}
 &[\overline{Y_j^++a}]-[\overline{Y_j^++d}]
  +[\overline{X_j^++a}]-[\overline{X_j^++d}]\\
 &\quad+[\overline{Y_j^-+d}]-[\overline{Y_j^-+a}]
  +[\overline{X_j^-+d}]-[\overline{X_j^-+a}],
\end{aligned}                                           \tag{2.7}
\]

which is exactly `-bar(D_j)`.

It remains to audit the singleton pivots from Lemma 1.2.  The `Y^+` port
changes `d -> a` and contributes

\[
 [X\cup\{b,c,d\}]-[X\cup\{b,c,a\}],
\]

while the `Y^-` port changes `a -> d` and contributes its negative.  The
same cancellation occurs between `X^+` and `X^-`, with common core
`Y union {c}`.  Hence the total rank-`(m+1)` singleton current is zero.

Every profile chain in (2.3) has length `p`.  Lemma 1.1 therefore puts
every changed value in ranks

\[
 (2m+1)-p-1=m+2,\ldots,2m.                            \tag{2.8}
\]

Hence the dual battery creates no proper-lower or middle-root current, and
its only owner-shore current cancels internally.  Cross-port intervals are
fixed by the common `H` shields.  Every saturated pivot has rank `m+1`,
every anchor/rail letter has rank one, and every shield has rank two, so no
letter exceeds the owner rank.  \(\square\)

## 3. Complete all-width cancellation

Let `B_0 -> B_1` be the lower four-ray battery transition of the companion
theorem, and let `U_0 -> U_1` be the dual transition above.  Place the two
gadgets in disjoint word intervals, retaining their terminal shields.  Any
interval meeting both gadgets contains a terminal shield for every changed
pivot it contains and is therefore state-independent.

### Corollary 3.1 (formal eight-port complete-current absorber)

Assume the native occurrence and the two battery occurrences are composed
in a host for which every interval meeting two different changed gadgets is
state-independent.  This is automatic between battery ports by their
shields; isolation from the native factor occurrence is part of the
physical host hypothesis.

Perform simultaneously:

1. one native inverse-pair move;
2. `B_0 -> B_1`; and
3. `U_0 -> U_1`.

Then the signed interval-union current is zero at every nontrivial rank.
The native central rank-`m` and rank-`m+1` palettes are already exact, the
lower battery cancels `D_j` in ranks `1,...,m-1`, and the dual battery
cancels `bar(D_j)` in ranks `m+2,...,2m`.

The combined transition is involutive.  Reusing the same native slot with
the same eight pivot positions back and forth therefore accumulates no
interval-palette debt.

#### Proof

The proper-lower assertion is Theorem 2.1 of the lower-battery note.  The
proper-upper assertion is Theorem 2.1 above.  Their rank supports are
disjoint.  The native inverse-pair theorem gives exact equality on the two
central shores.  Shield isolation excludes every cross-gadget contribution.
Adding the three signed currents gives zero rank by rank.  \(\square\)

## 4. Position count and exact remaining host theorem

Each dual port has one pivot, one anchor, and `p` rail letters.  Four such
interiors and five shared `H` shields give

\[
                         4(p+2)+5=4m+5               \tag{4.1}
\]

standalone dual positions.  Together the lower and upper batteries use
`8m+6` standalone positions.  This is **not** an additive-constant bound:
the eight length-`p` rail segments must be realized by existing chronology
support rather than appended as new support.

The remaining statement is now purely a host/coinstantiation theorem:

> **Prepared eight-ray host.**  In one near-optimal owner chronology, plant
> the four lower rays, four complementary upper rays, their bounded pivot
> and shield interface, and one native changing slot, with the rail letters
> replacing existing `O(m)` support.  Preserve simple central ownership,
> q1 palettes, residence, and one background compiler basis outside `O(1)`
> occurrence labels.

Under this host theorem, the combined battery gives a reusable zero-current
state transition.  The bounded terminal-omission theorem then turns any
`O(1)` residual logical bank into `B(k)+O(1)`.  Thus all-width current
arithmetic is no longer the missing row; owner-safe host coinstantiation and
background occurrence transport are.
