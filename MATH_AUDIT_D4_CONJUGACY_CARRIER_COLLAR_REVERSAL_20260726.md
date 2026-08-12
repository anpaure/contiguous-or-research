# Audit of the full `D_4` conjugacy carrier tensor and the reflected-reversal gate

Date: 2026-07-26

Method: pure mathematics only.  The only finite input is the fourteen-word
table in `MATH_THEOREM_D4_PAIR23_PORT_FACTOR_20260726.md`.  All assertions
below follow by relabelling, reversal, and the displayed exact ledgers.

## 0. Verdict

Put

\[
 H=\langle(2\ 3),(4\ 5),(6\ 7)\rangle\cong C_2^3,
 \qquad R(i)=9-i\quad(1\le i\le8),
 \tag{0.1}
\]

and extend `R` by fixing the anchor `9`.  The correct port-preserving
reversal is the **contravariant reflected reversal**

\[
 \widetilde X_t=R(X_{4-t}),
 \qquad \mu(P)=R([8]\setminus P).
 \tag{0.2}
\]

It gives a legal `D_4`-ported exact factor after the root is reindexed by
`mu`.  Together with `H` it gives sixteen legal factor states.  Bare cyclic
reversal is legal only at the opposite oriented endpoint; the tempting
root-fixed block reversal is not exact.

For every local interval length `ell` and start `j` (zero based, modulo
nine), the complete carrier profile of the sixteen states is obtained from
the original profile by the exact formulas

\[
\boxed{
 U^{h,+}_{\ell,j}=h_*U_{\ell,j},\qquad
 U^{h,-}_{\ell,j}=(hR)_*U_{\ell,\,8-j-\ell}.}
 \tag{0.3}
\]

Thus reflected reversal does not add a free marked coordinate while leaving
the collar fixed: it reflects **every** collar offset at the same time.

At singleton length the marked `b_1` motion is repaid by the other eight
starts in the abstract local ledger.  This repayment survives physically
only when those starts have the same exterior carrier and local embedding.
At lengths two, three, six, and seven even the all-start aggregate need not
cancel.  Hence there is no state-independent overload sign.

The full rootwise first-boundary support is

\[
 \boxed{
 T(P)=
 \begin{cases}
 \{8\},&P\in\{1234,1235\},\\
 [8]\setminus P,&P\in D_4\setminus\{1234,1235\}.
 \end{cases}}
 \tag{0.4}
\]

Consequently the proposed root-uniform four-state boundary packet is false.
If either member of a two-boundary occurrence has root `1234` or `1235`,
then even independently chosen left and right library factors give at most
`1 times 4=4` marked joint cells, not eight.  Full collar tensors may
distinguish more global factor states, but they do not create four
first-boundary owners at the locked root.

This audit validates the carrier formulas and support obstruction in
`MATH_THEOREM_D4_CONJUGACY_TARGET_POLYTOPE_AND_SUPPORT_OBSTRUCTION_20260726.md`,
subject to the physical-carrier qualification in Section 6 below.  The
companion report
`MATH_THEOREM_D4_CONJUGACY_ROOT_SUPPORT_20260726.md` has been corrected to
use the same contravariant reflected reversal and agrees with (0.4).

## 1. The only legal reanchored reversal

Let a row of the factor be

\[
 X_0=P,X_1,X_2,X_3,X_4=[8]\setminus P,
 \qquad Y_t=X_t\cup X_{t+1}.
 \tag{1.1}
\]

Define the reflected reverse row by (0.2).  Its first and last states are

\[
 \widetilde X_0=R([8]\setminus P)=\mu(P),
 \qquad
 \widetilde X_4=R(P)=[8]\setminus\mu(P).
 \tag{1.2}
\]

Moreover

\[
 \widetilde X_t\cup\widetilde X_{t+1}
   =R(Y_{3-t}).
 \tag{1.3}
\]

Thus the seventy lower states and fifty-six union states are merely
permuted.  Exactness and the prescribed `D_4` ports are preserved because
`mu=CR` preserves `D_4`.

If

\[
 q(P)=(a_1,a_2,a_3,a_4,b_1,b_2,b_3,b_4,9),
 \tag{1.4}
\]

then the row rooted at `mu(P)` has word

\[
 q^\dagger(\mu(P))
  =(Rb_4,Rb_3,Rb_2,Rb_1,Ra_4,Ra_3,Ra_2,Ra_1,9).
 \tag{1.5}
\]

In particular its first insertion is `Ra_4`, not a freely selectable
version of the old `b_1`.

There are two useful warnings.

1. Reversing the cyclic word without `R` preserves the underlying
   unoriented wreath, but the displayed Dyck port moves to the opposite
   endpoint.  It is not another state at the same oriented boundary.
2. The root-fixed block reversal
   \(\widehat X_t=[8]\setminus X_{4-t}\) is not exact.  Indeed the rows
   `1234` and `1235` contain respectively the consecutive pairs
   `1238,1368` and `1358,1378`, both with intersection `138`.  After
   complement reversal both corresponding union colours are
   \([8]\setminus138=24567\), so the upper ledger repeats a colour.

This proves that (0.2), rather than either naive reversal, is the relevant
sixteen-state ported library.

## 2. Exact offset reflection

For a cyclic word `q` define

\[
 I_{\ell,j}(q)=\{q_j,q_{j+1},\ldots,q_{j+\ell-1}\},
 \qquad
 U^F_{\ell,j}=\sum_{P\in D_4}e_{I_{\ell,j}(q_F(P))}.
 \tag{2.1}
\]

The position map in (1.5) is

\[
 k\longmapsto7-k\pmod9.
 \tag{2.2}
\]

Therefore the image of the length-`ell` interval starting at `j` is the
`R`-image of the forward interval whose first position is

\[
 j^\dagger=8-j-\ell\pmod9.
 \tag{2.3}
\]

This proves

\[
 U^{F^\dagger}_{\ell,j}=R_*U^F_{\ell,j^\dagger}.
 \tag{2.4}
\]

Changing the root variable under `h` then proves (0.3).  More generally,
for any two library states `(h,epsilon)` and `(k,eta)`, their literal
signed carrier difference is

\[
 D^{(h,\epsilon),(k,\eta)}_{\ell,j}
 =U^{h,\epsilon}_{\ell,j}-U^{k,\eta}_{\ell,j}.
 \tag{2.5}
\]

This absolute formula is the safe one.  If `Delta` denotes the old
`G-MSW` signed table, then

\[
 \Delta^{h,+}_{\ell,j}=h_*\Delta_{\ell,j},\qquad
 \Delta^{h,-}_{\ell,j}=(hR)_*\Delta_{\ell,j^\dagger}
 \tag{2.6}
\]

only when the canonical comparison factor is transformed by the **same**
`(h,epsilon)`.  Against one fixed untransformed canonical factor an extra
canonical-orbit term remains.  Hence a transformed signed table must not be
used as though every conjugate were a one-column perturbation of the same
fixed background.

## 3. Full sixteen-state collision table

Let

\[
 m_{\ell,j}=\max_S U^G_{\ell,j}(S).
 \tag{3.1}
\]

The forward values are the exact table in
`MATH_THEOREM_D4_H4_ORBIT_AND_CARRIER_CAPACITY_20260726.md`.  Relabelling by
`h` does not change a maximum, and (2.4) gives

\[
 M_{\ell,j}:=\max_{L\in\mathcal L}\max_S U^L_{\ell,j}(S)
  =\max\{m_{\ell,j},m_{\ell,j^\dagger}\}.
 \tag{3.2}
\]

Thus the exact maximum single-factor collision table over all sixteen
states is

\[
\begin{array}{c|rrrrrrrrr}
\ell\backslash j&0&1&2&3&4&5&6&7&8\\ \hline
1&5&4&5&5&5&5&4&5&14\\
2&2&2&2&5&2&2&2&5&5\\
3&1&1&2&2&1&1&2&2&2\\
4&1&1&1&1&1&1&1&1&1\\
5&1&1&1&1&1&1&1&1&1\\
6&2&2&2&1&1&2&2&1&1\\
7&5&5&2&2&2&5&2&2&2\\
8&14&5&4&5&5&5&5&4&5.
\end{array}
\tag{3.3}
\]

Compared with the forward eight-state table, reflected reversal increases
only `(ell,j)=(1,5)` and `(8,6)`, from three to five.  Apart from the
constant profiles `(1,8)` and `(8,0)`, every local profile in every legal
conjugate has collision multiplicity at most five.

This is a local packet statement.  After an ambient push-forward it remains
valid if the local labelling is injective and the fourteen rows share the
same exterior carrier.  Overlapping atoms or row-dependent carriers require
their joint physical ledger and cannot be bounded by adding (3.3) blindly.

## 4. Exact marked menus and the locked orbit

The reflected reverse has

\[
 b_1^{G^\dagger}(P)=R a_4^G(\mu(P)).
 \tag{4.1}
\]

Reading `b_1` and `a_4` from the fourteen words and then taking the `H`
orbits gives

\[
\begin{array}{c|c|c|c}
P&T^+(P)&T^-(P)&T(P)\\ \hline
1234&\{8\}&\{8\}&\{8\}\\
1235&\{8\}&\{8\}&\{8\}\\
1236&\{7,8\}&\{4,5\}&\{4,5,7,8\}\\
1237&\{6,8\}&\{4,5\}&\{4,5,6,8\}\\
1245&\{3,6,7\}&\{3,8\}&\{3,6,7,8\}\\
1345&\{2,6,7\}&\{2,8\}&\{2,6,7,8\}\\
1246&\{3,5,7,8\}&\{3,5,7,8\}&\{3,5,7,8\}\\
1247&\{3,5,6,8\}&\{3,5,6,8\}&\{3,5,6,8\}\\
1256&\{3,4,7,8\}&\{3,4,7,8\}&\{3,4,7,8\}\\
1257&\{3,4,6,8\}&\{3,4,6,8\}&\{3,4,6,8\}\\
1346&\{2,5,7,8\}&\{2,5,7,8\}&\{2,5,7,8\}\\
1347&\{2,5,6,8\}&\{2,5,6,8\}&\{2,5,6,8\}\\
1356&\{2,4,7,8\}&\{2,4,7,8\}&\{2,4,7,8\}\\
1357&\{2,4,6,8\}&\{2,4,6,8\}&\{2,4,6,8\}.
\end{array}
\tag{4.2}
\]

For the eight roots containing one member of each swappable pair, `H` acts
freely, so one representative calculation proves the last eight lines.
The other lines follow from their two-point orbits and stabilizers.  The
last column is exactly (0.4).

The locked rows have a transparent structural proof.  Both `1234` and
`1235` have `b_1=8` in `G`, have `a_4=1`, and are fixed by `mu`; `H` fixes
both endpoint labels `1,8`.  Hence both the forward and reflected cosets
have first insertion `8` there.  This is a port-owner invariant, not an
artifact of one orientation.

## 5. Marked motion and collar repayment

Every row word is a permutation of `[9]`.  Therefore, for every legal
factor state `L`,

\[
 \sum_{j\in\mathbb Z_9}U^L_{1,j}
   =14\sum_{x=1}^9 e_{\{x\}},
 \qquad
 \sum_jU^L_{8,j}
   =14\sum_{x=1}^9e_{[9]\setminus\{x\}}.
 \tag{5.1}
\]

Exact lower-state and union ownership similarly give

\[
 \sum_jU^L_{4,j}=\sum_{S\in\binom{[9]}4}e_S,
 \qquad
 \sum_jU^L_{5,j}=\sum_{S\in\binom{[9]}5}e_S.
 \tag{5.2}
\]

Subtracting the identities for any two states gives

\[
 \sum_jD_{\ell,j}=0
 \qquad(\ell=1,4,5,8).
 \tag{5.3}
\]

In particular, at singleton length and marked start `j=4`,

\[
                 \sum_{j\ne4}D_{1,j}=-D_{1,4}.        \tag{5.4}
\]

This is the precise sense in which the marked first-boundary multiplicity
is repaid by its collar.  It is an equality of the **complete local start
ledger**, not a pointwise equality at the marked target and not an overload
descent theorem.

The original `G-MSW` table shows that the all-start differences at lengths
two and three have positive masses `19` and `22`; lengths seven and six are
their complements.  Thus no analogue of (5.3) exists at those lengths.
Even at lengths one, four, five, and eight the start-resolved columns can be
nonzero; only their sum is forced to vanish.

## 6. Physical carrier criterion

Let the ambient occurrence attached to start `j` have exterior carrier
`O_j` and local injection `iota_j`.  Write

\[
 \Phi_j(e_S)=e_{O_j\cup\iota_j(S)}.
 \tag{6.1}
\]

The physical signed collar is exactly

\[
                         \mathcal D_\ell=\sum_j\Phi_j(D_{\ell,j}).
 \tag{6.2}
\]

If all `Phi_j` are the same map, (5.3) implies physical cancellation for
`ell=1,4,5,8`.  Without this common-carrier hypothesis, the exact repayment
condition is instead the vector identity

\[
             \sum_{j\ne4}\Phi_j(D_{1,j})
                     =-\Phi_4(D_{1,4}),              \tag{6.3}
\]

which need not follow from (5.4).  If the images of the carrier slices are
disjoint, no cross-slice cancellation is possible at all.

This is the needed qualification to Section 6 of the target-polytope
report.  Its sentence that marked motion is “repaid across the complete
start ledger” is correct locally; it is not automatically true after the
different collar starts are embedded in an outer factor.  Likewise,
start-resolved disturbances occur at all lengths, although only lengths
two, three, six, and seven can have a nonzero all-start aggregate.

## 7. Two-boundary cell obstruction

For two fixed port roots `P,Q`, define the common-state marked map

\[
 \Theta_{P,Q}(h,\epsilon)
   =\bigl(b_1^{hG^\epsilon}(P),b_1^{hG^\epsilon}(Q)\bigr),
 \qquad (h,\epsilon)\in H\times\{+,-\}.
 \tag{7.1}
\]

One root-scale factor choice gives one point of this image; the two row
coordinates cannot be selected independently.  Even if the two boundaries
are placed in disjoint packets so that their factor choices really are
independent, the largest possible marked product menu is

\[
                         T(P)\times T(Q).              \tag{7.2}
\]

If `P` or `Q` lies in `A={1234,1235}`, (0.4) gives

\[
 |T(P)\times T(Q)|\le1\cdot4=4.                      \tag{7.3}
\]

The same upper bound holds for the common-state image (7.1).  Hence this
library cannot supply eight marked joint cells with the requested
all-root quantifier.

If both roots lie outside `A` and two factor copies are independently
selectable on disjoint coordinate blocks, then (0.4) does give sixteen
distinct marked pairs after a fixed injective physical embedding.  If one
common factor state controls both boundaries, four-state marginals alone
do **not** imply eight joint cells: the exact number is the cardinality of
the correlated image (7.1), and the whole collar state is the corresponding
vertex of (0.3), not merely its two marked labels.

Thus there are two separate surviving gates even after excluding `A`:

1. prove that the two boundary factor choices are independently legal, or
   compute the common-state image (7.1) for the actual boundary-root pair;
2. route the complete physical collar (6.2) with a favourable cap sign.

Neither follows from the four-point row supports.

## 8. Correct boundary of the finite result

The finite library has a real positive feature: twelve of the fourteen
ports have their entire four-element complement as the marked menu, and
every nonconstant local collar profile has single-factor collision at most
five.  But the exact obstruction is equally sharp:

* `1234` and `1235` are permanently owned by target `8` at the first
  boundary under the full legal symmetry library;
* a factor choice selects one complete tensor vertex (0.3) for every root
  and every collar start;
* marked repayment is only a common-carrier local identity;
* no root-uniform eight-cell or floor-corrected descent theorem follows.

An all-root construction must add a genuinely new exact factor which
unlocks the orbit `{1234,1235}`, or prove that every charged occurrence in
the intended root-scale atlas avoids that orbit.  Even then, a joint
carrier/cap argument remains necessary.
