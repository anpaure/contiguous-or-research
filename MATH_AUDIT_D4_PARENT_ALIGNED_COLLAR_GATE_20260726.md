# Parent-aligned `D_4` bridge: exact collar ledger and the remaining cap gate

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let $F$ be the canonical MSW $D_4$-port factor and let $G$ be the
fourteen-row factor in
`MATH_THEOREM_D4_PAIR23_PORT_FACTOR_20260726.md`.  Put

\[
 E_0=\{1,8\},\quad E_1=\{2,3\},\quad
 E_2=\{4,5\},\quad E_3=\{6,7\}.
\tag{0.1}
\]

The new first-insertion pair totals are indeed

\[
                 (5,5,2,2)\longrightarrow(5,5,1,3).
\tag{0.2}
\]

This is not erased by the other five starts of the open matched parent.
The complete six-start change is

\[
 \boxed{d=2e_2-3e_3-3e_6+4e_7,\qquad
        \Pi d=-e_{E_1}+e_{E_3}.}
\tag{0.3}
\]

Thus the distinguished move $E_2\to E_3$ and the five-start collar move
$E_1\to E_2$ concatenate to $E_1\to E_3$.  This is a genuine
parent-boundary signal.

There is, however, exact singleton compensation in the complete local
nine-cycle.  The three attachment starts $b_4,9,a_1$ contribute $-d$.
Consequently the full singleton histogram is unchanged.  At the isolated
cap $p=9$, even the six-start atom has zero hinge descent for every
residual-capacity vector.

The cancellation is not universal at higher target sizes.  Summing all
nine cyclic starts, the local signed interval profiles are nonzero exactly
at lengths

\[
                         \ell=2,3,6,7,
\tag{0.4}
\]

with positive masses $(19,22,22,19)$, respectively.  Hence the new factor
is not collar-null in all higher contexts.  But nonzero transport is not a
cap-descent theorem.  Its sign depends on the actual exterior carriers and
the actual residual capacities.

There is also a precise hidden issue in an aggregate-carrier formulation.
In a general outer context, different rows and different cyclic starts can
receive different exterior carriers.  One may not first sum their local
directions to $d$ or to \(\Delta_{\ell,j}\) and then push that aggregate
through one carrier map.  The exact lift is row- and start-resolved; it is
formula (6.3) below.  Therefore neither pair totals nor support separation
of two abstract aggregate vectors proves a legal PCap absorber.

The surviving route is consequently narrow but real:

1. use the established anchored port-context substitution, which makes the
   replacement exactly legal in every common aligned context;
2. compute its row-resolved carrier tensor in the chosen ancestor context;
3. prove that tensor has favourable sign against the canonical residual
   capacities.

The present $D_4$ certificate settles step 1, because its endpoints are
$P,[8]\setminus P$ row by row and its complete $X/Y$ ledgers are exact.
It does not settle step 3.

## 1. Exact chronology

For a rooted row write

\[
 X_t=(P\setminus\{a_1,\ldots,a_t\})
       \cup\{b_1,\ldots,b_t\},\qquad 0\le t\le4,
\tag{1.1}
\]

and use the cyclic coordinate word

\[
 q=(a_1,a_2,a_3,a_4,b_1,b_2,b_3,b_4,9).
\tag{1.2}
\]

At protected depth three, the six starts meeting the open parent have
singleton targets

\[
                  a_2,a_3,a_4,b_1,b_2,b_3,
\tag{1.3}
\]

while the three complementary attachment starts have targets

\[
                              b_4,9,a_1.
\tag{1.4}
\]

The first-insertion statistic in (0.2) is only the fourth entry $b_1$
of (1.3).  It is neither the six-start parent statistic nor the complete
nine-start statistic.

Let

\[
 \delta_j=\sum_{P\in\mathcal D_4}
       \bigl(e_{q_G(P)_j}-e_{q_F(P)_j}\bigr),
       \qquad 1\le j\le9.
\tag{1.5}
\]

Literal reading of the two fourteen-row word tables gives

\[
\begin{array}{c|l}
j&\delta_j\\ \hline
1&-3e_2+5e_3-e_4-e_6\\
2& 2e_2-3e_3-3e_4+2e_5-e_6+3e_7\\
3&-e_2+4e_4-4e_5-e_6+2e_7\\
4& 2e_2-2e_3+2e_5+3e_6-5e_7\\
5&-4e_2+4e_3-e_4-e_6+2e_7\\
6& 3e_2-e_3-2e_4\\
7&-e_3+2e_4-3e_6+2e_7\\
8& e_2-2e_3+e_4+4e_6-4e_7\\
9&0.
\end{array}
\tag{1.6}
\]

Position five is $b_1$.  Thus

\[
 \delta_5=4(e_3-e_2)-e_4-e_6+2e_7,
 \qquad \Pi\delta_5=-e_{E_2}+e_{E_3},
\tag{1.7}
\]

which recovers (0.2).

## 2. Six-start survival and three-start repayment

Summing exactly the open-parent positions in (1.3) gives

\[
 \boxed{
 \sum_{j=2}^{7}\delta_j
       =2e_2-3e_3-3e_6+4e_7=d.}
\tag{2.1}
\]

After removing the marked start,

\[
 \Pi\left(\sum_{j=2}^{7}\delta_j-\delta_5\right)
                         =-e_{E_1}+e_{E_2}.
\tag{2.2}
\]

This proves the chronology

\[
             E_1\xrightarrow{\text{five other starts}}E_2
                 \xrightarrow{b_1}E_3.
\tag{2.3}
\]

The attachment positions repay the result exactly:

\[
 \boxed{
 \delta_8+\delta_9+\delta_1
       =-2e_2+3e_3+3e_6-4e_7=-d.}
\tag{2.4}
\]

Therefore

\[
                              \sum_{j=1}^{9}\delta_j=0.
\tag{2.5}
\]

This is the correct form of singleton rigidity.  Exactness fixes the sum
of the open-parent and attachment histograms.  It does not fix either
summand.  The strict-hole erasure theorem applies to the full matched
window and is reflected in the cancellation (2.5); it does not assert
that the six-start subprofile (2.1) vanishes.  The factor $G$ keeps the
complementary interface states fixed but changes the internal first/last
exchange symbols $(a_1,b_4)$, and therefore changes crossing-collar
targets seen by an ancestor.

## 3. Exact six-start loads and the isolated cap

The canonical and new open-parent histograms are

\[
\begin{aligned}
 u_F&=9e_1+9e_2+12e_3+12e_4+12e_5+12e_6+9e_7+9e_8,\\
 u_G&=9e_1+11e_2+9e_3+12e_4+12e_5+9e_6+13e_7+9e_8.
\end{aligned}
\tag{3.1}
\]

Thus $u_G-u_F=d$.  If $c_x=(p-\beta_x)_+$ is the residual capacity,
the exact six-start hinge change is

\[
\begin{aligned}
 \Delta K={}&(11-c_2)_+-(9-c_2)_+
 +(9-c_3)_+-(12-c_3)_+\\
 &+(9-c_6)_+-(12-c_6)_+
 +(13-c_7)_+-(9-c_7)_+.
\end{aligned}
\tag{3.2}
\]

At the isolated scale $p=9$, one has $c_x\le9$.  Every hinge in
(3.2) is then on its linear branch, and

\[
                         \Delta K=2-3-3+4=0.
\tag{3.3}
\]

Restoring the attachment starts makes the stronger statement that the
complete singleton histogram is identical, so its cap contribution is
identical for every capacity vector, not only for $p=9$.

The variation of the open atom is

\[
                         \frac12\lVert d\rVert_1=6.
\tag{3.4}
\]

This is potential transport, not automatic descent.  A favourable
capacity can expose all six units, and the opposite capacity can reverse
their sign.  The canonical coefficient-one background must therefore be
inserted before any unit of (3.4) is credited.

## 4. The complete cyclic interval audit

For $1\le\ell\le8$, $j\in\mathbb Z_9$, and a row $P$, put

\[
 I_{\ell,j}(q)=\{q_j,q_{j+1},\ldots,q_{j+\ell-1}\}
\tag{4.1}
\]

with cyclic indices, and define

\[
 \Delta_{\ell,j}
 =\sum_{P\in\mathcal D_4}
   \left(e_{I_{\ell,j}(q_G(P))}
         -e_{I_{\ell,j}(q_F(P))}\right),
 \qquad
 \Delta_\ell=\sum_{j\in\mathbb Z_9}\Delta_{\ell,j}.
\tag{4.2}
\]

The exact aggregate ledger is

\[
\begin{array}{c|cccccccc}
\ell&1&2&3&4&5&6&7&8\\ \hline
\lVert\Delta_\ell\rVert_1/2&0&19&22&0&0&22&19&0.
\end{array}
\tag{4.3}
\]

The four zeroes have structural proofs:

* $\Delta_1=0$ because every row word is a permutation of the same nine
  coordinates, and $\Delta_8=0$ by complementation;
* $\Delta_4=0$ because the cyclic four-windows are exactly the vertices
  of the two exact $C_9$-factors, and $\Delta_5=0$ by complementation.

The length-two profile is already nonzero.  For example, direct adjacency
counting in the displayed words gives

\[
                       \Delta_2(\{1,4\})=+2,
 \qquad                 \Delta_2(\{1,2\})=-1.
\tag{4.4}
\]

Indeed $\{1,4\}$ is cyclically adjacent in two old words and four new
words, while $\{1,2\}$ is adjacent in five old words and four new words.
The complete length-two profile has positive and negative mass $19$.
The length-three profile has positive and negative mass $22$, and the
length-seven and length-six profiles are their complement images.

Consequently (2.5) is a singleton cancellation, not a full
higher-context erasure.  An aligned outer window whose local intersection
has length two, three, six, or seven can see the replacement.

## 5. Why nonzero profile is not yet cap descent

For any physical signed profile $D$ and old load $u$, the cap change is

\[
 K_c(u+D)-K_c(u)
       =\sum_T\bigl[(u(T)+D(T)-c(T))_+
                    -(u(T)-c(T))_+\bigr].
\tag{5.1}
\]

If $D$ has zero total mass and positive mass $M$, then

\[
                              -M\le\Delta K\le M.
\tag{5.2}
\]

Both signs are possible as the residual capacities vary.  Thus (4.3)
only supplies possible transports of sizes $19$ and $22$; it supplies
no state-independent negative sign.  A PCap conclusion requires the
actual canonical background $u-c$, target by target.

This also explains why the isolated singleton calculation gives zero.
There all changed entries in (3.2) lie on the same linear branch, so the
zero total of $d$ forces cancellation.  Merely separating the formal
positive and negative support in a later context does not prove that the
negative support is overloaded while the positive support has spare
capacity.

## 6. The exact row-resolved context formula

The local aggregate profiles must not be pushed through a carrier map
unless that map is common to every term being aggregated.  Define the
row-level signed atom

\[
 d_{P,\ell,j}
  =e_{I_{\ell,j}(q_G(P))}
      -e_{I_{\ell,j}(q_F(P))}.
\tag{6.1}
\]

For each affected occurrence
$\omega=(P,\ell,j)$, let $O_\omega$ be its exterior intersection and
let $\iota_\omega$ be its inherited injection of the local labels.  Its
physical push-forward is

\[
 \Phi_\omega(e_S)=e_{O_\omega\cup\iota_\omega(S)}.
\tag{6.2}
\]

The complete physical change in an outer context is exactly

\[
 \boxed{
             D_C=\sum_{\omega}\Phi_\omega
                         d_{P,\ell,j}.}
\tag{6.3}
\]

Formula (6.3) follows occurrence by occurrence and has no hidden
uniformity assumption.  The aggregated formula

\[
                  \Phi\Delta_{\ell,j}
       =\Phi\sum_Pd_{P,\ell,j}
\tag{6.4}
\]

is valid only when the same $\Phi$ applies to every one of the fourteen
rows at that $(\ell,j)$.  Likewise, a formula of the form

\[
                         \mathsf P_Cd-\mathsf Q_Cd
\tag{6.5}
\]

is valid only when the six open starts share the relevant push-forward
and the three attachment starts share another.  General parent contexts
need not have either property.  Different offsets usually adjoin different
exterior collars, and row-dependent routing can refine them further.

This is the hidden aggregation issue.  Support-disjointness asserted only
after forming $d$ is not enough: it may describe no realizable aligned
context.  The legal object to test for support collisions and cap sign is
$D_C$ in (6.3).

## 7. Exact parent-aligned legality; only the cap gate remains

The factor $G$ preserves the state ports

\[
                         X_0=P,\qquad X_4=[8]\setminus P,
\tag{7.1}
\]

and its complete local state and adjacent-union ledgers agree with those
of $F$.  These are exactly the hypotheses of the anchored
port-transversal context-substitution theorem.  Therefore $F\rightsquigarrow
G$ is a legal exact replacement in every common aligned one-hole tree
context.

### Theorem 7.1 (authoritative aligned-interface statement)

Let $C[\ ]$ be any aligned rooted port context to which the corrected
context-substitution theorem applies.  Replace the fourteen canonical
rank-four fragments in $C[F]$ by the fourteen fragments of $G$, matching
the row rooted at $P$ to the row rooted at the same $P$.  Then $C[G]$ is a
literal integral exact factor, every ambient row retains its prescribed
two ports, and both ambient ownership ledgers are unchanged.  No separate
$D_5$ completion or boundary-gluing lemma is required.

#### Proof

For every root $P$, the two local attachment states are identically

\[
                         P,\qquad [8]\setminus P
\]

on the two packet shores.  Hence every edge from the unchanged outer
context to the local fragment has the same endpoint before and after the
replacement.  Inside the fragment, the complete $X$-multisets agree and
the complete adjacent-union $Y$-multisets agree.  After adjoining fixed
context coordinates, or complementing the appropriate ledger in a
primitive wrap, these equalities remain equalities.  They are precisely
the two ambient ownership equations.  Thus the replacement glues, owns
every middle vertex once, and keeps the named complementary ports.  This
is the aligned context-substitution theorem specialized to the displayed
$D_4$ certificate. \(\square\)

The symbols $a_1$ and $b_4$ are the first deletion and last insertion
*inside* the local geodesic.  They determine crossing-window targets, but
they are not the outer interface states.  Changing them does not break
the incident outer edges: the actual entrance and exit states remain
$P$ and $[8]\setminus P$.  Equality of the complete $X$ ledger preserves
all local middle owners, and equality of the complete $Y$ ledger preserves
all owners containing the distinguished interface coordinate.  Hence the
ambient ownership equations remain exact.

Phase-disjoint aligned substitutions may be chosen independently.  Nested
or overlapping substitutions may still have coupled *profile choices* and
must be grouped into a joint atom for a simultaneous cap calculation, but
this is not a defect in the legality of either substitution.

Thus the corrected decision is:

* **strictly internal substitutions:** erased at the next full matched
  parent, by complementary-port intersection;
* **the complete $D_4$ singleton profile:** collar-cancelled after all
  nine starts are included;
* **higher interval profiles:** genuinely nonzero at lengths
  $2,3,6,7$, hence not algebraically erased;
* **exact aligned-context legality:** proved by the anchored substitution
  theorem from the fixed endpoints and complete $X/Y$ ledgers;
* **coefficient-one cap descent:** still unproved, because row-resolved
  carrier separation and the true residual-capacity sign remain to be
  established.

The $D_4$ bridge is therefore a valid boundary primitive, but it is not
yet a Catalan conveyor or a hereditary PCap absorber.

## 8. Corrections to the current surrounding notes

Two nearby formulations should not be used without these qualifications.

First,
`MATH_THEOREM_D4_PAIR_TRANSFER_PARENT_PROFILE_COLLAR_AUDIT_20260726.md`
asserts that the two six-start profiles are both the canonical vector
$u_F$.  Equations (1.6), (2.1), and (3.1) above directly refute that
assertion.  Its singleton-rigidity lemma was applied after declaring the
three attachment starts unchanged, but the explicit $G$ table changes
$a_1$ and $b_4$.  Exactness fixes the nine-start sum, not the six-start
summand.

That note also says that the $D_4$ table does not construct a legal
parent-aligned extension.  This is too pessimistic.  The rooted-context
functor supplies such extensions directly: fixed complementary endpoint
states plus the two exact ledgers are the complete interface certificate.
What remains absent is not an exact completion but a favourable
carrier-resolved PCap inequality.

Second, the aggregate context formula in Section 6 of
`MATH_THEOREM_D4_PAIR23_PORT_FACTOR_20260726.md` is correct under its
stated common-carrier hypothesis: for fixed $(\ell,j)$, all fourteen rows
must have the same exterior carrier and injection.  Its extension to a
"general ambient window family" requires grouping only occurrences with
identical carrier maps; if a group does not contain all fourteen roots,
one must use the row atoms (6.1), not the already-summed
$\Delta_{\ell,j}$.  Formula (6.3) is the safe general statement.

Finally, the statement that the first matched singleton scale cancels is
correct for the complete nine-start local factor.  It is false for the
six open-parent starts alone.  Keeping this scope distinction prevents
both errors: crediting the marked $E_2\to E_3$ move as free descent, and
discarding the genuine boundary signal (0.3) as though it had already
vanished.
