# Reserve completion for H's deterministic all-depth-rainbow catalogue

Date: 2026-07-25

Pure mathematics only.

Let

\[
n=2m,\qquad
W=\binom{2m}{m},\qquad
M=m+H,\qquad
N=\binom{2m}{M},
\tag{0.1}
\]

at the calibrated crossing. Thus

\[
H\sim\sqrt{m\log m},\qquad
MN=W-o(W),\qquad
HN=o(W),
\tag{0.2}
\]

and the truncated radius satisfies \(Q=o(H)\).

This note applies the \(O(Q)\)-cost rotor reserve ledger to the
deterministic gap-permutation catalogue in
MATH_ATTACK_H_DETERMINISTIC_CARRIER_ROTOR_TRAJECTORIES_20260725.md.

## 0. Verdict

The catalogue has exactly the rowwise capacity needed for a much weaker
exceptional-carrier threshold than the one in its original common-path
gate.

Let

\[
R_q=\binom{2m}{m-q}=\binom{2m}{m+q},
\tag{0.3}
\]

and let

\[
c_0=M,\qquad
c_q=\min\left\{
M,\left\lfloor\frac{R_q}{N}\right\rfloor
\right\}
\quad(1\le q\le Q)
\tag{0.4}
\]

be H's claimed-phase counts. Put

\[
\delta_0=W-MN,\qquad
\delta_q=R_q-c_qN\quad(q\ge1).
\tag{0.5}
\]

If a common catalogue matching is found on \(N-R\) carrier tags, then at
every signed protected rank its target holes satisfy

\[
\boxed{
h_0\le\delta_0+MR,
\qquad
h_{q,\pm}\le\delta_q+c_qR.
}
\tag{0.6}
\]

Since \(\max_q\delta_q=o(W)\), the rowwise necessary condition for an
\(o(W)\) reserve is met as soon as

\[
\boxed{R=o(N).}
\tag{0.7}
\]

This is far weaker than the earlier threshold

\[
R=o(W/m^{3/2})=o(N/\sqrt m),
\tag{0.8}
\]

which arose from patching every exceptional claimed slot separately.

The improvement is real but conditional. A reserve top carries

\[
L_Q=\Theta(M/Q)
\tag{0.9}
\]

localized cells at \(O(M)\) total cost, and \(R\) reserve tops can
therefore carry

\[
S=O(RM/Q)
\tag{0.10}
\]

cells at total cost \(O(RM)\). For \(R=o(N)\), this is \(o(W)\).
The cell occurrence capacities are large enough, row by row and in
aggregate, to absorb the leave in (0.6).

What is not proved is the required integral joint cover. The following
facts from H's catalogue do not establish it:

* exact all-depth rainbowness inside each trajectory;
* the tag-saturating fractional point;
* integral Hall at every rank separately;
* an owner-only matching.

The weakest sufficient statement is a **tagged flagged-reserve theorem**:
after choosing one base trajectory on every exceptional tag, the remaining
holes must be coverable by \(S=o(W/Q)\) localized cells hosted on those
tags, plus \(E=o(W)\) literal exceptions.

Thus a two-stage owner matching plus flagged reserve succeeds only if the
second stage includes this joint tagged certificate. The currently proved
owner matching and separate-rank Hall statements do not imply it.

## 1. The deterministic catalogue data

Every catalogue trajectory on a carrier \(U\) has \(M\) state endpoints
and is internally injective at every rank \(m\pm q\), \(0\le q\le Q\).
In the decorated catalogue it claims the first \(c_q\) phases in one common
priority order at both signed depth-\(q\) rows.

The common priority is important. The claimed sets for larger depths are
nested phase restrictions of the claimed sets at smaller depths; they are
not \(2Q+1\) unrelated row objects.

Let

\[
K_Q=M+2\sum_{q=1}^Q c_q
\tag{1.1}
\]

be the number of claimed target slots in one decorated trajectory. The
catalogue calculation gives

\[
\boxed{
K_Q=(\sqrt\pi+o(1))m^{3/2}.
}
\tag{1.2}
\]

The total calibrated scalar floor leave is

\[
\boxed{
\delta_\Sigma
:=\delta_0+2\sum_{q=1}^Q\delta_q
=o(W).
}
\tag{1.3}
\]

More precisely:

* at a noncapped depth, \(0\le\delta_q<N=O(W/m)\);
* at a capped depth, \(c_q=M\) and
  \[
  0\le\delta_q\le W-MN=O(WH/m)=o(W).
  \tag{1.4}
  \]

Hence

\[
\boxed{\max_{0\le q\le Q}\delta_q=o(W).}
\tag{1.5}
\]

## 2. A partial common matching

Let \(\mathcal C\) be a set of \(N-R\) carrier tags. Suppose one decorated
catalogue trajectory is selected for each \(U\in\mathcal C\), and all
claimed target slots of the selected trajectories are mutually disjoint.
No path is yet selected on the reserve-tag family

\[
\mathcal R=\binom{[2m]}M\setminus\mathcal C,
\qquad |\mathcal R|=R.
\tag{2.1}
\]

### Proposition 2.1 (exact guaranteed row leave)

The protected row holes after the common matching satisfy

\[
h_0\le W-M(N-R)=\delta_0+MR,
\tag{2.2}
\]

and, for \(1\le q\le Q\),

\[
\boxed{
h_{q,\pm}
\le R_q-c_q(N-R)
=\delta_q+c_qR.
}
\tag{2.3}
\]

#### Proof

Each selected trajectory contributes \(M\) distinct claimed owners and
\(c_q\) distinct claims at each signed depth \(q\). The common matching
makes those claims distinct across trajectories. Thus the core covers
exactly \(M(N-R)\) claimed owners and \(c_q(N-R)\) claimed targets in
each signed row. Unclaimed phases can only improve coverage. Subtracting
these guaranteed supports from the row sizes proves the result.
\(\square\)

### Corollary 2.2 (weak rowwise exceptional-tag scale)

If

\[
R=o(N),
\tag{2.4}
\]

then

\[
\max\left\{
h_0,\max_{q,\pm}h_{q,\pm}
\right\}=o(W).
\tag{2.5}
\]

#### Proof

Use \(c_q\le M\), \(MN=W-o(W)\), and (1.5):

\[
\delta_q+c_qR\le o(W)+MR=o(W).
\]

\(\square\)

The aggregate guarantee is

\[
\boxed{
h_\Sigma
\le\delta_\Sigma+RK_Q.
}
\tag{2.6}
\]

Literal repair of all these holes requires

\[
RK_Q=o(W),
\tag{2.7}
\]

which is exactly the old scale

\[
R=o(W/m^{3/2}).
\tag{2.8}
\]

The rotor reserve seeks to replace the aggregate condition (2.7) by the
rowwise scale (2.4) plus an integral vertical-cover theorem.

Equivalently, after charging the unavoidable catalogue floors
\(\delta_\Sigma=o(W)\) literally, the exceptional-tag leave is

\[
\boxed{
\bar h_0:=(h_0-\delta_0)_+\le MR,
\qquad
\bar h_{q,\pm}:=(h_{q,\pm}-\delta_q)_+\le c_qR.
}
\tag{2.9}
\]

These are the exact rank budgets which the flagged reserve must pack
vertically. Their maximum is \(O(MR)\), while their sum is at most
\(RK_Q\).

## 3. H-specific word ledger

Compile one length-\(M\), radius-\(Q\) rotor trajectory on every carrier
tag. The \(N-R\) core trajectories and the \(R\) reserve base
trajectories together cost

\[
\boxed{
(M+2Q+1)N
=MN+(2Q+1)N
=W+o(W).
}
\tag{3.1}
\]

This point is sharper than the generic reserve ledger. The reserve base
trajectories do not create a new \(MR\) word term: one trajectory on every
carrier was already part of the calibrated primary budget. The value
\(MR\) appears only in the owner-hole estimate (2.2).

A localized four-order cell is a union of at most four radius-\(Q\)
promotion chunks and at most \(4Q+4\) state endpoints. Its exact upper
cost is

\[
\boxed{
c_Q=(4Q+4)+4(2Q+1)=12Q+8.
}
\tag{3.2}
\]

Let \(S\) cells be added and let \(E\) protected targets remain for
individual literal repair after the final positive diagonal choices.
Then the complete length, before the already audited \(q>Q\) reservoir
and tails, is

\[
(M+2Q+1)N+(12Q+8)S+E.
\tag{3.3}
\]

### Theorem 3.1 (H-catalogue reserve completion)

Starting from a partial common matching on \(N-R\) tags, suppose one can
choose:

1. one base catalogue trajectory on every reserve tag;
2. \(S\) localized rotor cells hosted on reserve tags, with one positive
   diagonal selected in every cell;
3. a final literal exception set of size \(E\);

so that all protected targets are covered. If

\[
\boxed{
QS=o(W),\qquad E=o(W),
}
\tag{3.4}
\]

then the full construction has length \(W+o(W)\).

#### Proof

Equation (3.1) pays for all base trajectories. Equation (3.2) pays for
every state and reset in the cells. The exception set costs \(E\).
Every selected object is positive and integral. The standard outer
reservoir and tails cost \(o(W)\). Equation (3.4) completes the ledger.
\(\square\)

No scalar hypothesis on \(R\) is needed in the word identity (3.1).
The useful regime \(R=o(N)\) enters because it gives rowwise \(o(W)\)
leave and because arbitrary reserve base paths need not repair the
middle holes in (2.2).

## 4. Tagged reserve capacity

Use the safe bank size

\[
L_Q
=\left\lfloor
\frac{M}{2(12Q+8)}
\right\rfloor
=\Theta(M/Q).
\tag{4.1}
\]

At most \(L_Q\) cells on one reserve tag cost at most \(M/2\) and expose
at most

\[
(4Q+4)L_Q<M/4
\tag{4.2}
\]

additional state endpoints at any fixed rank.

Thus \(R\) reserve tags can carry

\[
S\le RL_Q=\Theta(RM/Q)
\tag{4.3}
\]

cells at total cell cost

\[
O(QS)=O(RM).
\tag{4.4}
\]

If \(R=o(N)\), then

\[
RM=o(MN)=o(W),
\qquad
S=o(W/Q).
\tag{4.5}
\]

### Row and aggregate occurrence capacity

One reserve base path supplies \(M\) state flags in each protected row.
One cell supplies at most \(4Q+4\) state flags in each protected row.
Consequently a banked reserve has per-row occurrence capacity at most

\[
B_QR,
\qquad
B_Q:=M+(4Q+4)L_Q<\frac54M.
\tag{4.6}
\]

The inequality is an upper-capacity audit, not a coverage theorem.
Its order is

\[
B_QR=\Theta(MR),
\tag{4.7}
\]

which matches the worst row deficit \(c_qR\le MR\) in (2.3).

Across all protected ranks, the cell bank has at most

\[
(2Q+1)(4Q+4)RL_Q
=O(RMQ)
\tag{4.8}
\]

flag occurrences. Since

\[
RK_Q=\Theta(Rm^{3/2})
\tag{4.9}
\]

and

\[
MQ
=m^{3/2}\sqrt{\log\log m+\gamma}\,(1+o(1)),
\tag{4.10}
\]

the total occurrence capacity also dominates the exceptional claimed-slot
count by a growing factor. Thus there is no remaining scalar capacity
obstruction at \(R=o(N)\).

The problem is incidence, not volume: the needed holes must occur in the
actual positive configurations of cells hosted by the available tags.

## 5. Exact carrier-tag conditions

### 5.1 A necessary row-host Hall inequality

Fix a protected rank \(k\) and a family
\(\mathcal A\subseteq\mathcal H_k\) of holes. A target \(A\) exposed by
a rotor state in carrier \(U\) must satisfy

\[
A\subseteq U.
\tag{5.1}
\]

Let

\[
N_{\mathcal R}(\mathcal A)
=\left\{
U\in\mathcal R:
\text{some }A\in\mathcal A\text{ satisfies }A\subseteq U
\right\}.
\tag{5.2}
\]

If at most \(L_Q\) cells are used per reserve tag and only \(E\) targets
are patched literally, then necessarily

\[
\boxed{
|\mathcal A|
\le
B_Q|N_{\mathcal R}(\mathcal A)|+E
\quad
\text{for every }\mathcal A\subseteq\mathcal H_k.
}
\tag{5.3}
\]

This is only a necessary row-capacity condition. It ignores trajectory
chronology and the requirement that all ranks be covered by the same
positive configurations.

### 5.2 Exact Hall for a proposed cell multiset

A rank-\(k\) octahedral cell has coordinate support \(F\) of size \(k+2\)
and is hostable in \(U\) exactly when

\[
F\subseteq U.
\tag{5.4}
\]

For a proposed integral cell multiset \(\mathcal D\), join a cell to its
containing reserve tags. There is an assignment using at most \(L_Q\)
cells per tag if and only if

\[
\boxed{
|\mathcal A|
\le
L_Q|N_{\mathcal R}^{\rm cell}(\mathcal A)|
\quad
\text{for every submultiset }
\mathcal A\subseteq\mathcal D.
}
\tag{5.5}
\]

This capacitated Hall condition is necessary and sufficient for hosting
the proposed cells. It does not construct their signed decomposition or
prove that their positive sides cover the holes.

## 6. The weakest tagged leave

The exact residual object is a tagged joint cover, not a list of row
counts.

### Definition 6.1 (H-tagged reserve functional)

For a partial common catalogue matching \(\mathscr M\) with reserve tags
\(\mathcal R\), define

\[
\operatorname{HRCov}_Q(\mathscr M,\mathcal R)
\tag{6.1}
\]

to be the minimum of

\[
(12Q+8)S+E
\tag{6.2}
\]

over:

1. one base all-depth-rainbow catalogue trajectory on every
   \(U\in\mathcal R\);
2. \(S\) positive localized cells hosted on \(\mathcal R\), at most
   \(L_Q\) per tag;
3. \(E\) literal target patches;
4. final choices which, together with the core, cover every protected
   target.

The base trajectories are not charged in (6.2), because their cost is
already included in the all-\(N\)-tag identity (3.1). All other objects
are integral and all coverage is evaluated after the final choices.

### Theorem 6.2 (weakest H-catalogue completion gate)

A partial common matching completes at coefficient one whenever

\[
\boxed{
\operatorname{HRCov}_Q(\mathscr M,\mathcal R)=o(W).
}
\tag{6.3}
\]

For a banked localized absorber, the explicit sufficient scale is

\[
\boxed{
R=o(N),\qquad
S=O(RM/Q)=o(W/Q),\qquad
E=o(W),
}
\tag{6.4}
\]

provided the final joint cover and Hall condition (5.5) hold.

#### Proof

The first statement is Theorem 3.1 with the minimum in Definition 6.1.
For the explicit scale, (4.5) gives \(QS=o(W)\), and (3.4) applies.
\(\square\)

The numerical conditions in (6.4) are not a replacement for the joint
cover. They merely show that such a cover, if constructed, fits the
coefficient-one ledger.

In rank-and-tag language, the weakest explicit certificate has four
parts:

\[
\boxed{
\begin{gathered}
\bar h_0\le MR,\qquad
\bar h_{q,\pm}\le c_qR,\\
S=o(W/Q),\qquad E=o(W),\\
|\mathcal A|
\le L_Q|N_{\mathcal R}^{\rm cell}(\mathcal A)|
\quad(\mathcal A\subseteq\mathcal D),\\
\text{the final positive configurations cover all holes outside }E.
\end{gathered}
}
\tag{6.5}
\]

For \(R=o(N)\), the first line is rowwise \(o(W)\) and the catalogue
floors are already absorbable into \(E\). The last line is the genuinely
cross-rank condition which no scalar inequality replaces.

## 7. Comparison with the original exceptional-carrier gate

The original catalogue argument filled \(R\) exceptional carriers
arbitrarily and charged every possibly colliding claimed target. Its
exceptional contribution was

\[
RK_Q,
\tag{7.1}
\]

so it required

\[
R=o(W/K_Q)=o(W/m^{3/2}).
\tag{7.2}
\]

The reserve ledger separates this into row and joint-cover questions.

* Rowwise, a partial common matching has leave at most
  \(\delta_q+c_qR=o(W)\) for every rank as soon as \(R=o(N)\).
* A bank of \(O(M/Q)\) cells per reserve tag has word cost \(O(M)\) per
  tag and enough occurrence volume to address \(O(M)\) holes per row.
* Therefore the largest exceptional-tag scale certified solely by the
  partial-matching row bound is
  \[
  \boxed{R=o(N)=o(W/m).}
  \tag{7.3}
  \]

This improves the permitted number of exceptional tags by a factor of
order \(\sqrt m\).

The improvement can be realized only if the \(RK_Q\) row slots share
the same \(O(RM/Q)\) localized cells. If the rows are repaired
independently, one needs on the order of

\[
\sum_q\frac{c_qR}{Q}
=\Theta(RK_Q/Q)
\tag{7.4}
\]

cells, whose word cost is \(\Theta(RK_Q)\). This returns exactly to the
old threshold (7.2).

Hence **vertical sharing is the entire gain**.

## 8. Does owner matching plus a flagged reserve meet the gate?

There are two different meanings of the proposed two-stage construction.

### 8.1 Owner-only first stage

Suppose the first stage chooses trajectories whose middle owners are
disjoint or have \(o(W)\) collisions, but imposes no condition on their
nonmiddle flags.

This does not meet the reserve gate. Internal all-depth rainbowness says
that one trajectory has no repeated flag in a row. It does not prevent
the same flag from occurring in many different carriers. An owner
matching determines vertices of the Johnson chronology; it does not
give a near-transversal of its consecutive intersections and unions.

In particular, the owner condition alone does not prove

\[
h_{q,\pm}=o(W)
\tag{8.1}
\]

for even one \(q\ge1\). If (8.1) fails linearly at one rank, the one-row
lower bound forces \(\Omega(W)\) reserve cost. H's exact fractional loads
and separate-rank Hall theorem do not change this: they concern the whole
catalogue, not the residual catalogue after a particular owner matching.

Therefore:

\[
\boxed{
\text{owner matching alone + a sparse flagged reserve is not proved
sufficient.}
}
\tag{8.2}
\]

### 8.2 Partial common claimed-target matching

Suppose instead that the first stage is a genuine common catalogue
matching on \(N-R\) tags. Then Proposition 2.1 supplies all rowwise bounds,
and \(R=o(N)\) passes every scalar reserve test.

The remaining flagged-reserve assertion is:

> Choose base trajectories and at most \(O(M/Q)\) localized cells on each
> reserve tag so that their positive flag columns cover all but \(o(W)\)
> of the residual holes jointly across every \(q\le Q\).

This assertion is sufficient by Theorem 6.2 and strictly weaker than
extending the exact common matching to every reserve tag: it permits
localized overlays, duplicate flags, and \(o(W)\) final exceptions.

It is not implied by the catalogue results currently proved. Separate-rank
Hall gives unrelated target assignments at different ranks. A trajectory
or localized cell must realize one chronological, vertically coupled
column. This is the missing theorem.

Thus the precise status is

\[
\boxed{
\begin{array}{c}
\text{partial common matching on }N-o(N)\text{ tags}\\
+\ \text{tagged flagged-reserve theorem}
\end{array}
\Longrightarrow
\text{coefficient one},
}
\tag{8.3}
\]

while

\[
\boxed{
\text{owner-only matching}
+\ \text{separate-rank Hall}
\not\Longrightarrow
\text{the tagged reserve certificate presently.}
}
\tag{8.4}
\]

## 9. Optional signed correction audits

If the flagged reserve is formulated as an exact signed correction
\(z_k\), rather than pure positive coverage, then \(S\) cells must satisfy

\[
A_1z_k=0,
\tag{9.1}
\]

\[
S\ge
\frac12\sum_kW_1^J((z_k)_+,(z_k)_-),
\tag{9.2}
\]

and

\[
S\ge
\frac14\sum_k\|A_2z_k\|_1.
\tag{9.3}
\]

At the H-catalogue scale, a banked reserve therefore requires

\[
\sum_kW_1^J((z_k)_+,(z_k)_-)
=O(RM/Q)=o(W/Q),
\tag{9.4}
\]

\[
\sum_k\|A_2z_k\|_1
=O(RM/Q)=o(W/Q).
\tag{9.5}
\]

These are necessary diagnostics. They are not sufficient without an
integral positive decomposition and the tagged Hall condition (5.5).
For pure coverage, none of these signed invariants is required.

## 10. Exact obstructions

Any proposed two-stage proof is stopped by one of the following explicit
failures.

1. **Row leave.** If some protected rank has \(\Omega(W)\) holes after
   the owner/core stage, an \(o(W)\) rotor reserve cannot repair it.
2. **Tag concentration.** If for some rank and hole family
   \(\mathcal A\),
   \[
   |\mathcal A|-B_Q|N_{\mathcal R}(\mathcal A)|
   =\Omega(W),
   \tag{10.1}
   \]
   then (5.3) forces \(E=\Omega(W)\).
3. **No vertical packing.** If every joint cover needs
   \(S=\Omega(W/Q)\) cells, their literal cost is \(\Omega(W)\).
4. **Signed transport.** In a signed formulation, either (9.2) or (9.3)
   can force \(S=\Omega(W/Q)\).

The partial common matching with \(R=o(N)\) automatically avoids the first
obstruction by Proposition 2.1. It does not automatically avoid the other
three.

## 11. Final calibrated target

The strongest weakened catalogue theorem which the \(O(Q)\)-cost reserve
can use is:

> Select a common claimed-target matching on \(N-R\) carrier tags, where
> \(R=o(N)\). On the remaining tags, choose one deterministic
> all-depth-rainbow base trajectory per tag and at most \(O(M/Q)\)
> hosted localized cells per tag, so that the final aggregate protected
> holes are \(o(W)\).

The final aggregate condition here is measured after the vertically shared
reserve configurations, not before them. Under this statement,

\[
(M+2Q+1)N+O(RM)+o(W)
=W+o(W).
\tag{11.1}
\]

This theorem would relax H's old exceptional-tag requirement from
\(o(N/\sqrt m)\) to \(o(N)\).

It remains open. The presently proved two-stage owner matching plus
separate flagged Hall does not meet it, because neither result supplies
the required common chronological reserve columns.
