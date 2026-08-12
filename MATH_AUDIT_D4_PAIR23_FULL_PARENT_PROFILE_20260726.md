# The complete `D_4` pair bridge: parent profile, compensation, and cap descent

Date: 2026-07-26

Method: pure mathematics only.

## 0. Result

Let \(F\) be the canonical MSW \(D_4\)-port factor and let \(G\) be the
explicit complete port factor in
`MATH_THEOREM_D4_PAIR23_PORT_FACTOR_20260726.md`.  Write

\[
 E_0=\{1,8\},\qquad E_1=\{2,3\},\qquad
 E_2=\{4,5\},\qquad E_3=\{6,7\}.
\tag{0.1}
\]

The reported first-insertion profile is correct:

\[
             (5,5,2,2)\longrightarrow(5,5,1,3),
\tag{0.2}
\]

so that one unit moves from \(E_2\) to \(E_3\).  It is not, however, the
full six-start parent profile.  The exact six-start histograms are

\[
\boxed{
\begin{aligned}
 u_F&=(9,9,12,12,12,12,9,9),\\
 u_G&=(9,11,9,12,12,9,13,9),
\end{aligned}}
\tag{0.3}
\]

on coordinates \(1,\ldots,8\), with zero mass at \(9=\infty\).  Hence

\[
 \boxed{u_G-u_F=2e_2-3e_3-3e_6+4e_7.}
\tag{0.4}
\]

On pair classes this is the pure transfer

\[
 \boxed{
 (18,21,24,21)\longrightarrow(18,20,24,22),
 \qquad -e_{E_1}+e_{E_3}.}
\tag{0.5}
\]

Thus the new primitive survives the four crossing collars.  More exactly,
the first-insertion start moves one unit \(E_2\to E_3\), the other five
parent starts move one unit \(E_1\to E_2\), and their composition is the
new bridge \(E_1\to E_3\).

There is nevertheless exact compensation in the isolated nine-coordinate
factor.  The other three cyclic starts have histograms

\[
\boxed{
\begin{aligned}
 v_F&=(5,5,2,2,2,2,5,5,14),\\
 v_G&=(5,3,5,2,2,5,1,5,14),
\end{aligned}}
\tag{0.6}
\]

and

\[
                         v_G-v_F=-(u_G-u_F).
\tag{0.7}
\]

Consequently

\[
             u_F+v_F=u_G+v_G=14\sum_{x=1}^9e_x.
\tag{0.8}
\]

The previous singleton-rigidity argument applied (0.8) incorrectly to
\(u\) alone.  Exactness fixes \(u+v\); it does not fix \(u\), because the
complementary starts \(v\) change.

This also identifies the missing hypothesis in the parent residual-capacity
note.  For an arbitrary complete port factor, the displayed \(2r=6\) starts
are not the entire changed profile: the complementary starts may change
through the first-deletion and last-insertion ledgers.  The literal
decomposition \(\mu=\beta+u_G\) with one factor-independent \(\beta\) is
valid only after either

1. enlarging \(u_G\) to include every such complementary occurrence, or
2. restricting the library so that its complementary histogram \(v_G\) is
   fixed.

Port transversality alone supplies neither condition.

At the isolated cap \(p=9\), the bridge gives no residual-cap descent:
every changed load is at least nine, so every admissible capacity
\(c\le9\) sees the same hinge value.  In a higher or mixed context the two
opposite profiles can acquire different exterior carriers.  If their
physical images are separated, (0.4) survives and has a sharp six-unit
residual descent for a suitable residual-capacity vector.  If the two
images coincide, (0.7) cancels it.  The exact survival criterion is the
push-forward equality in Theorem 6.1 below; the local pair-total table alone
does not decide an arbitrary outer context.

## 1. Six parent starts and three complementary starts

Let a rooted size-four path have deletion and insertion orders

\[
 a_1,a_2,a_3,a_4,qquad b_1,b_2,b_3,b_4,
\tag{1.1}
\]

so that

\[
 X_t=(P\setminus\{a_1,\ldots,a_t\})
        \cup\{b_1,\ldots,b_t\},\qquad0\le t\le4.
\tag{1.2}
\]

The cyclic lower-state order comes from

\[
              (a_1,a_2,a_3,a_4,b_1,b_2,b_3,b_4,9).
\tag{1.3}
\]

At depth three, the six starts whose four-state windows meet an open parent
state have singleton targets

\[
                         a_2,a_3,a_4,b_1,b_2,b_3.
\tag{1.4}
\]

The three complementary starts have targets

\[
                              b_4,9,a_1.
\tag{1.5}
\]

For a fourteen-row factor \(H\), let \(A_H(x)\) count rows with
\(a_1=x\), and let \(B_H(x)\) count rows with \(b_4=x\).  Equations
(1.4)--(1.5) give

\[
\boxed{
 u_H(x)=14-A_H(x)-B_H(x),\qquad
 v_H=A_H+B_H+14e_9.}
\tag{1.6}
\]

In particular

\[
                         u_H+v_H=14\sum_{x=1}^9e_x.
\tag{1.7}
\]

Identity (1.7), not constancy of \(u_H\), is the singleton consequence of
exactness.

## 2. The canonical profile

The MSW flip recursion gives

\[
 A_F=5e_1+5e_2+2e_4+2e_6,
\qquad
 B_F=2e_3+2e_5+5e_7+5e_8.
\tag{2.1}
\]

Substitution into (1.6) yields

\[
 u_F=9e_1+9e_2+12e_3+12e_4+12e_5+12e_6+9e_7+9e_8,
\tag{2.2}
\]

and

\[
 v_F=5e_1+5e_2+2e_3+2e_4+2e_5+2e_6
              +5e_7+5e_8+14e_9.
\tag{2.3}
\]

These are the two lines of (0.3) and (0.6) belonging to \(F\).

## 3. The new factor profile

Read the first deletion \(a_1=X_0\setminus X_1\) and the last insertion
\(b_4=X_4\setminus X_3\) from the fourteen displayed paths of \(G\).  The
rowwise values are

\[
\begin{array}{c|cccccccccccccc}
P&1234&1235&1236&1237&1245&1246&1247&1256&1257&1345&1346&1347&1356&1357\\ \hline
a_1&4&2&3&3&1&1&1&2&1&3&6&3&1&3\\
b_4&7&4&8&5&8&5&6&8&6&8&2&6&8&6.
\end{array}
\tag{3.1}
\]

Therefore

\[
\begin{aligned}
 A_G&=5e_1+2e_2+5e_3+e_4+e_6,\\
 B_G&=e_2+e_4+2e_5+4e_6+e_7+5e_8.
\end{aligned}
\tag{3.2}
\]

Equation (1.6) now gives

\[
 u_G=9e_1+11e_2+9e_3+12e_4+12e_5+9e_6+13e_7+9e_8,
\tag{3.3}
\]

and

\[
 v_G=5e_1+3e_2+5e_3+2e_4+2e_5+5e_6
              +e_7+5e_8+14e_9.
\tag{3.4}
\]

Subtracting (2.2)--(2.3) proves (0.4) and (0.7).  Notice that all four
vectors have the required masses

\[
                |u_F|=|u_G|=84,qquad |v_F|=|v_G|=42.
\tag{3.5}
\]

## 4. Exact pair-class decomposition of the crossing effect

Let \(\Pi\) send a singleton histogram to its four pair totals on
\(E_0,E_1,E_2,E_3\).  The first-insertion start has old and new profiles

\[
\begin{aligned}
 q_F^+&=5e_8+5e_2+2e_4+2e_6,\\
 q_G^+&=5e_8+e_2+4e_3+e_4+e_6+2e_7.
\end{aligned}
\tag{4.1}
\]

Thus

\[
 \Pi(q_G^+-q_F^+)=-e_{E_2}+e_{E_3}.
\tag{4.2}
\]

Subtracting this one start from the six-start result (0.5) gives

\[
 \boxed{
 \Pi\bigl((u_G-q_G^+)-(u_F-q_F^+)\bigr)
                    =-e_{E_1}+e_{E_2}.}
\tag{4.3}
\]

Hence the five other parent starts do not cancel the reported bridge.
They concatenate with it:

\[
                  E_1\longrightarrow E_2
                      \longrightarrow E_3.
\tag{4.4}
\]

If one wants the four crossing starts separately from both intrinsic
starts, the last-deletion profiles are

\[
\begin{aligned}
 q_F^-&=5e_1+2e_3+2e_5+5e_7,\\
 q_G^-&=5e_1+2e_2+4e_5+3e_6.
\end{aligned}
\tag{4.5}
\]

Therefore

\[
 \Pi(q_G^--q_F^-)=2e_{E_2}-2e_{E_3},
\tag{4.6}
\]

and the four crossing starts alone have

\[
 \boxed{
 \Pi\Delta_{\rm cross}=-e_{E_1}-e_{E_2}+2e_{E_3}.}
\tag{4.7}
\]

Equations (4.2), (4.6), and (4.7) sum to (0.5).  Thus the crossing collars
reinforce the destination \(E_3\); the isolated cancellation occurs only
after the complementary three cyclic starts (1.5) are restored.

## 5. Residual-capacity calculation

Fix the old complementary background and write \(c_x=(p-\beta_x)_+\).
On the six-start profile the exact residual-defect change is

\[
\boxed{
\begin{aligned}
 E_\beta(G)-E_\beta(F)
={}&(11-c_2)_+-(9-c_2)_+\\
 &+(9-c_3)_+-(12-c_3)_+\\
 &+(9-c_6)_+-(12-c_6)_+\\
 &+(13-c_7)_+-(9-c_7)_+.
\end{aligned}}
\tag{5.1}
\]

At the isolated scale \(p=9\), every \(c_x\le9\).  Each load appearing in
(5.1) is at least nine, so every hinge is linear and the right side is

\[
             (11-9)+(9-12)+(9-12)+(13-9)=0.
\tag{5.2}
\]

Thus there is no local cap descent, despite the nonzero profile.

The total variation bound is sharp:

\[
              \frac12\|u_G-u_F\|_1
                     ={2+3+3+4\over2}=6.
\tag{5.3}
\]

For any ambient cap \(p\ge13\), take on this physical six-start support

\[
                             c=u_G.
\tag{5.4}
\]

Then

\[
                         E_c(G)=0,qquad E_c(F)=6.
\tag{5.5}
\]

Equivalently the dual weight supported on the two decreased cells,

\[
                         \alpha=e_3+e_6,
\tag{5.6}
\]

satisfies

\[
             \langle\alpha,u_G\rangle
               -\langle\alpha,u_F\rangle=-6.
\tag{5.7}
\]

This is genuine residual-cap descent for the six-start atom.  It becomes
descent for the complete higher-context replacement precisely when the
compensating starts are sent to other physical cells with enough residual
capacity.

## 6. Mixed and higher contexts

An outer common context sends each **indexed** local target occurrence to a
physical target by adjoining its exterior carrier and applying the inherited
affine coordinate injection.  Let

\[
 \widehat d_6,\widehat d_3
\tag{6.1}
\]

be the signed old-to-new ledgers in the free abelian groups on the indexed
occurrences of, respectively, the six starts (1.4) and the three starts
(1.5).  Let

\[
 \mathsf P_C,\mathsf Q_C
\tag{6.2}
\]

be their occurrencewise physical push-forward maps.  If \(\operatorname
{agg}\) forgets the occurrence index and retains only the local target,
then (0.4) and (0.7) say

\[
 \operatorname {agg}(\widehat d_6)=d,
 \qquad
 \operatorname {agg}(\widehat d_3)=-d,
 \qquad
 d=2e_2-3e_3-3e_6+4e_7.
\tag{6.3}
\]

### Theorem 6.1 (exact survival criterion)

The complete physical histogram change of the lifted bridge is

\[
 \boxed{
 \Delta_C=\mathsf P_C\widehat d_6
              +\mathsf Q_C\widehat d_3.}
\tag{6.4}
\]

Consequently:

1. the bridge cancels exactly if and only if the right side of (6.4)
   vanishes;
2. if each sector is transported by one fixed-carrier affine injection,
   say \(\phi_6,\phi_3\), then

   \[
        \Delta_C=(\phi_6)_*d-(\phi_3)_*d;
   \tag{6.5}
   \]

3. if, in addition, the two images in (6.5) are disjoint, then
   \(\Delta_C\ne0\) and
   \(\frac12\|\Delta_C\|_1=12\);
4. in that support-disjoint case, assigning the transported new six-start
   load as capacity on the \(\phi_6\)-image and coordinatewise maximum
   old/new capacity on the **changed cells** of the \(\phi_3\)-image gives
   six units of genuine cap descent; unchanged cells may have arbitrary
   common overflow.

#### Proof

Context lifting is occurrencewise and linear, so the two indexed signed
ledgers add as in (6.4).  This proves the first assertion.  Under a common
carrier injection inside each sector, aggregation commutes with push-forward;
(6.3) then gives (6.5).  Such an injection is one-to-one on local targets,
so each image has positive mass six and negative mass six by (5.3).  If the
two images are disjoint, neither can cancel the other and their sum has
positive mass twelve.  Finally (5.4)--(5.5) give six units of descent on the
first image.  Giving every changed cell of the second image capacity at
least the coordinatewise maximum of its old and new loads makes its hinge
contribution zero in both states; unchanged cells contribute the same hinge
value in both states. \(\square\)

The theorem is deliberately carrier-sensitive.  A common coordinate
relabeling and common carrier applied uniformly to all nine starts has
\((\phi_6)_*d=(\phi_3)_*d\) and preserves the isolated cancellation.  A
mixed context which tags the two sectors by distinct fixed exterior carriers
separates the supports and exposes the bridge.  Between these extremes,
row- and offset-dependent carriers must be evaluated using the indexed
formula (6.4); the aggregated vector \(d\), and a fortiori its pair totals,
cannot replace that calculation.

The residual capacities used in Theorem 6.1 are legitimate vectors
\(0\le c\le p\) once \(p\ge13\).  The theorem proves that the primitive is
cap-productive in principle.  It does not prove that the particular
background arising in the canonical coefficient-one construction supplies
those capacities.  That remaining statement is a joint carrier-profile
theorem, not a finite-factor existence question.

## 7. Audit decision

The new complete port factor changes the answer in three ways.

1. The earlier assertion \(u_G=u_F\) on the six parent starts is false.
   Singleton exactness was applied to the wrong subhistogram.
2. The reported \(E_2\to E_3\) first-insertion transfer survives the
   crossing collars and becomes the stronger six-start bridge
   \(E_1\to E_3\).
3. The isolated nine-coordinate factor still has zero total singleton
   change and zero cap descent, because an opposite three-start profile is
   present.  Higher contexts can turn the bridge into genuine cap descent
   exactly when they physically separate that compensating profile, as
   quantified by (6.4)--(6.5).

Thus this is a genuine new primitive, but not yet an unconditional
coefficient-one absorber.  Its remaining gate is the explicit
carrier-resolved lift, followed by the actual residual-capacity test.
Any use of the former \(2r\)-slot residual identity must first add the
complementary profile or prove it invariant for the chosen library.
