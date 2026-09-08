# Exact Hall theorem and antichain obstruction for H's flagged reserve

Date: 2026-07-25

Pure mathematics only.

This note starts from:

* MATH_ATTACK_H_DETERMINISTIC_CARRIER_ROTOR_TRAJECTORIES_20260725.md;
* MATH_ATTACK_H_RAINBOW_CATALOGUE_RESERVE_COMPLETION_20260725.md.

Put

\[
n=2m,\qquad
W=\binom{2m}{m},\qquad
M=m+H,\qquad
N=\binom{2m}{M},
\tag{0.1}
\]

at the calibrated crossing. Thus

\[
MN=W-o(W),\qquad
N=(1+o(1))W/m,\qquad
Q=o(H),\qquad Q/\sqrt m\to\infty.
\tag{0.2}
\]

## 0. Outcome

There is a sharp exact Hall theorem for **one-state** flagged reserve
cells, proved directly from H's gap/phase catalogue. It is an ordinary
capacitated Dilworth theorem because arbitrary carrier labellings make
every saturated central flag chain available as one catalogue phase.

There is also a precise obstruction to closing the desired
\(R=o(N)\) reserve theorem from H's presently proved data.

1. If the residual hole poset is \(\mathcal H\), then it can be covered by
   at most \(b\) one-state cells on each reserve tag if and only if, for
   every \(\mathcal A\subseteq\mathcal H\),
   \[
   \boxed{
   |\mathcal A|
   \le
   |\Gamma^+(\mathcal A)|
   +b|\Gamma_{\mathcal R}(\mathcal A)|.
   }
   \tag{0.3}
   \]
   Here \(\Gamma^+(\mathcal A)\) is the set of residual holes strictly
   containing a member of \(\mathcal A\), and
   \(\Gamma_{\mathcal R}(\mathcal A)\) is the set of reserve tops
   containing a member of \(\mathcal A\).

2. The resulting literal cost is at most
   \[
   (2Q+2)bR.
   \tag{0.4}
   \]
   Hence this theorem closes coefficient one whenever
   \[
   bRQ=o(W).
   \tag{0.5}
   \]

3. H's natural exceptional-tag row leave is of order \(MR\) per shallow
   rank. One-state cells with coefficient-safe capacity
   \(b=O(M/Q)\) provide only \(O(MR/Q)\) columns per row. Thus (0.3)
   generally fails by a factor \(Q\). The desired relaxation to
   \(R=o(N)\) must batch \(\Theta(Q)\) state columns into each
   \(O(Q)\)-cost local rotor cell.

4. For these multi-state local cells, no ordinary row Hall condition is
   sufficient. Every state column is a chain in the Boolean lattice.
   Therefore every antichain \(\mathcal A\) of residual holes satisfies
   the mandatory cross-rank capacity cut
   \[
   \boxed{
   |\mathcal A|
   \le
   B_Q|N_{\mathcal R}(\mathcal A)|+E,
   \qquad
   B_Q=M+(4Q+4)L_Q,
   }
   \tag{0.6}
   \]
   where \(L_Q\) is the number of cells allowed per reserve tag and
   \(E\) is the literal exception budget.

5. In particular, every coefficient-safe flagged reserve with
   \(R=o(N)\), \(QS=o(W)\), and \(E=o(W)\) requires
   \[
   \boxed{\operatorname{width}(\mathcal H)=o(W).}
   \tag{0.7}
   \]
   H's rowwise estimates do not imply (0.7).

6. This failure is sharp at the level of the proved information. There
   are rank profiles obeying
   \[
   h_{q,+}\le \delta_q+c_qR
   \tag{0.8}
   \]
   with \(R=o(N)\), yet whose holes contain an antichain of size
   \(\Theta(W)\). An explicit profile is given in Section 7.

Consequently the flagged reserve theorem is not closed. The exact missing
input is now narrower:

> Select the partial common catalogue matching so that its actual residual
> hole poset has \(o(W)\) antichain width and admits an integral cover by
> \(o(W/Q)\) legal \(O(Q)\)-phase blocks on the reserve tags.

The catalogue's exact fractional loads, separate-rank Hall inequalities,
and internal all-depth rainbowness do not prove this phase-block cover.

## 1. Local completeness of the gap catalogue

Let

\[
\mathcal K_Q=\{m-Q,\ldots,m+Q\}.
\tag{1.1}
\]

A saturated central flag chain in a carrier \(U\) is

\[
C_{m-Q}\subset C_{m-Q+1}\subset\cdots\subset C_{m+Q},
\qquad |C_k|=k,
\tag{1.2}
\]

with every \(C_k\subseteq U\).

### Lemma 1.1 (every flag chain is a catalogue phase)

For every carrier \(U\), every saturated chain (1.2), and every prescribed
phase \(t\in\mathbb Z_M\), there is a deterministic exact-rainbow
gap-permutation trajectory in H's catalogue whose phase-\(t\) flag column
is exactly (1.2).

#### Proof

Use the ordinary admissible gap schedule

\[
\rho(c)=c+H.
\tag{1.3}
\]

If the initially named nonempty schedule subcatalogue does not contain
this schedule, adjoin it. This only enlarges the deterministic catalogue;
the relabelling symmetry, exact-rainbow property, and all degree statements
used here are preserved.

Its gaps satisfy

\[
Q<H<M/2-Q
\tag{1.4}
\]

for all sufficiently large \(m\), so H's simultaneous-rainbow theorem
applies.

Write

\[
C_{m-Q+i}=C_{m-Q}+\{a_1,\ldots,a_i\}
\qquad(1\le i\le2Q).
\tag{1.5}
\]

At phase \(t\), the quotient state of the gap trajectory has one unordered
core block of size \(m-Q\), then \(2Q\) ordered singleton positions, then
an unresolved carrier tail of size \(H-Q\). Assign the labels
\(C_{m-Q}\) to the core positions and assign \(a_i\) to singleton
position \(i\). Assign the remaining elements of \(U\) arbitrarily to the
tail positions.

All bijective labellings of the carrier phases belong to H's catalogue.
The quotient flag formula then gives

\[
L+\{a_1,\ldots,a_i\}=C_{m-Q+i}
\]

at every central rank. Thus the phase column is (1.2). \(\square\)

### Corollary 1.2 (every residual chain is one state)

Let \(\mathcal C\) be any chain of residual holes under inclusion. If its
maximum member is contained in a reserve top \(U\), then \(\mathcal C\)
extends to a saturated chain (1.2) inside \(U\), and one catalogue phase
exposes every member of \(\mathcal C\).

#### Proof

Nested sets can be completed between their ranks by adding one coordinate
at a time. Extend below the minimum down to rank \(m-Q\), and extend above
the maximum to rank \(m+Q\). The latter is possible because

\[
m+Q\le m+H=|U|.
\]

Apply Lemma 1.1. \(\square\)

The literal radius-\(Q\) compilation of this one phase costs

\[
2Q+2.
\tag{1.6}
\]

This is a positive integral object; no signed rectangle or fractional
rounding is involved.

## 2. Exact hosted-chain Hall theorem

Let

\[
\mathcal H
=\bigcup_{k\in\mathcal K_Q}\mathcal H_k
\tag{2.1}
\]

be the protected holes after the core partial matching, ordered by strict
set inclusion. Let \(\mathcal R\) be the reserve-top family,
\(|\mathcal R|=R\).

For \(\mathcal A\subseteq\mathcal H\), define

\[
\Gamma^+(\mathcal A)
=\left\{
X\in\mathcal H:
\text{some }A\in\mathcal A\text{ satisfies }A\subsetneq X
\right\},
\tag{2.2}
\]

and

\[
\Gamma_{\mathcal R}(\mathcal A)
=\left\{
U\in\mathcal R:
\text{some }A\in\mathcal A\text{ satisfies }A\subseteq U
\right\}.
\tag{2.3}
\]

### Theorem 2.1 (capacitated hosted Dilworth-Hall)

Fix an integer \(b\ge0\). The residual hole poset \(\mathcal H\) can be
partitioned into chains and those chains assigned to reserve tops, at most
\(b\) chains per top, if and only if

\[
\boxed{
|\mathcal A|
\le
|\Gamma^+(\mathcal A)|
+b|\Gamma_{\mathcal R}(\mathcal A)|
\quad
\text{for every }\mathcal A\subseteq\mathcal H.
}
\tag{2.4}
\]

Every such chain cover is realized by at most \(bR\) one-state
exact-rainbow catalogue cells.

#### Proof

Construct a bipartite graph. Its right vertex class is a copy
\(\mathcal H_R\) of the hole set. Its left class consists of:

* a copy \(\mathcal H_L\) of the hole set;
* \(b\) clones of every reserve top \(U\in\mathcal R\).

Join \(X_L\) to \(A_R\) when \(A\subsetneq X\). Join a clone of \(U\) to
\(A_R\) when \(A\subseteq U\).

Hall's condition for a matching saturating every right vertex is exactly
(2.4).

Assume such a matching. Direct an edge from \(X\) to \(A\) whenever
\(X_L\) is matched to \(A_R\). Every hole has at most one predecessor
and at most one successor. Strict inclusion forbids directed cycles.
Thus the hole set is partitioned into descending chains. The maximum
member of each chain is matched from one reserve-top clone, which assigns
the chain to a containing top. At most \(b\) chains are assigned to one
top.

Conversely, from a hosted chain cover, match every nonmaximum chain member
from its immediate predecessor and match each chain maximum from one clone
of its host. This saturates the right class.

Corollary 1.2 realizes every hosted chain by one catalogue phase.
\(\square\)

### Corollary 2.2 (coefficient-safe one-state reserve)

If (2.4) holds and

\[
bRQ=o(W),
\tag{2.5}
\]

then the protected holes can be repaired at literal cost \(o(W)\).

#### Proof

There are at most \(bR\) one-state chunks, each of length \(2Q+2\).
Their total cost is at most

\[
(2Q+2)bR=o(W).
\]

\(\square\)

This is the sharp ordinary Hall theorem obtainable from the catalogue's
phase completeness.

## 3. Why the exact Hall theorem is not enough

For H's decorated catalogue, put

\[
c_0=M,\qquad
c_q=\min\left\{
M,\left\lfloor\frac{R_q}{N}\right\rfloor
\right\}.
\tag{3.1}
\]

A common matching on \(N-R\) tags guarantees exceptional row leave

\[
\bar h_0\le MR,\qquad
\bar h_{q,\pm}\le c_qR.
\tag{3.2}
\]

At shallow ranks \(q=O(\sqrt m)\),

\[
c_q=\Theta(M).
\tag{3.3}
\]

One chain contains at most one hole from a fixed rank. Therefore a
hosted-chain cover of a worst-case residual satisfying (3.2) may require

\[
bR\ge\max_{q,\pm}\bar h_{q,\pm}=\Theta(MR),
\tag{3.4}
\]

or \(b=\Theta(M)\). The one-state literal cost is then

\[
\Theta(QMR).
\tag{3.5}
\]

For the desired full range \(R=o(N)\), (3.5) need not be \(o(W)\).

Coefficient safety forces approximately

\[
b=O(M/Q),
\tag{3.6}
\]

which supplies only \(O(MR/Q)\) chain columns per row. Thus one-state
cells lose a factor \(Q\).

The purpose of a localized multi-state cell is exactly to recover this
factor: it contains \(O(Q)\) state columns but still costs \(O(Q)\), because
the states share resets along a few legal rotor chunks.

## 4. The exact multi-state cell criterion

Let \(\mathfrak P(U)\) be H's deterministic exact-rainbow trajectory
catalogue on reserve top \(U\). Let \(\mathfrak G_Q(U)\) be the catalogue
of positive localized rotor-cell configurations hosted on \(U\). Every
\(G\in\mathfrak G_Q(U)\):

* is a union of at most four legal radius-\(Q\) chunks;
* has at most \(4Q+4\) state endpoints;
* has literal cost at most \(12Q+8\).

For a trajectory or cell configuration \(B\), let

\[
F(B)\subseteq\bigcup_{k\in\mathcal K_Q}\binom{[2m]}k
\tag{4.1}
\]

be its protected flag support.

Fix a partial common matching \(\mathscr M\), and let
\(\mathcal H\) be its holes. The following finite integral system is the
exact flagged-reserve criterion for this architecture.

Choose variables

\[
z_{U,P}\in\{0,1\}
\quad(U\in\mathcal R,\ P\in\mathfrak P(U)),
\tag{4.2}
\]

\[
x_{U,G}\in\mathbb Z_{\ge0}
\quad(U\in\mathcal R,\ G\in\mathfrak G_Q(U)),
\tag{4.3}
\]

and

\[
y_A\in\{0,1\}
\quad(A\in\mathcal H),
\tag{4.4}
\]

subject to

\[
\sum_{P\in\mathfrak P(U)}z_{U,P}=1
\quad(U\in\mathcal R),
\tag{4.5}
\]

\[
\sum_{G\in\mathfrak G_Q(U)}x_{U,G}\le L_U
\quad(U\in\mathcal R),
\tag{4.6}
\]

\[
\sum_{\substack{U,P\\A\in F(P)}}z_{U,P}
+
\sum_{\substack{U,G\\A\in F(G)}}x_{U,G}
+y_A
\ge1
\quad(A\in\mathcal H),
\tag{4.7}
\]

\[
\sum_{U,G}x_{U,G}\le S,
\qquad
\sum_{A\in\mathcal H}y_A\le E.
\tag{4.8}
\]

### Theorem 4.1 (exact integral block-cover gate)

The partial common matching is repairable by one reserve base trajectory
per tag, at most \(L_U\) local cells on tag \(U\), at most \(S\) cells
globally, and at most \(E\) literal patches if and only if
(4.2)--(4.8) has an integral solution.

If

\[
QS=o(W),\qquad E=o(W),
\tag{4.9}
\]

then such a solution proves coefficient one.

#### Proof

The variables list exactly the positive objects deployed by the
architecture. Constraint (4.5) chooses one reserve base path per tag.
Constraint (4.6) is the tag capacity. Constraint (4.7) is exact final
coverage; it gives no fractional credit. Constraint (4.8) is the global
cell and exception ledger.

Conversely, every physical flagged reserve supplies these variables.
The all-\(N\)-tag base trajectories cost \(W+o(W)\). The cells cost at
most \((12Q+8)S=o(W)\), and the patches cost \(E=o(W)\).
\(\square\)

System (4.2)--(4.8) is an integral block-cover problem, not an ordinary
bipartite matching. The shared selection of all \(O(Q)\) phase columns in
one cell is precisely what gains the factor \(Q\). Splitting those columns
into independent slots destroys that gain by charging a separate reset to
each slot.

### Exact host Hall for a proposed cell multiset

If an untagged integral cell multiset \(\mathcal D\) has already been
constructed, a cell with coordinate support \(F\) is adjacent to reserve
tag \(U\) exactly when \(F\subseteq U\). It can be assigned with capacities
\((L_U)\) if and only if

\[
\boxed{
|\mathcal A|
\le
\sum_{U\in N_{\mathcal R}^{\rm cell}(\mathcal A)}L_U
\quad
\text{for every submultiset }
\mathcal A\subseteq\mathcal D.
}
\tag{4.10}
\]

This is the sharp capacitated Hall theorem for **hosting proposed cells**.
It does not construct \(\mathcal D\) or prove (4.7).

## 5. A mandatory cross-rank Hall cut

Every phase state exposes one saturated chain across the protected ranks.
Therefore one state column meets an antichain in at most one target.

Let \(\mathcal A\subseteq\mathcal H\) be an antichain. Define its reserve
tag neighborhood by

\[
N_{\mathcal R}(\mathcal A)
=\left\{
U\in\mathcal R:
\text{some }A\in\mathcal A\text{ satisfies }A\subseteq U
\right\}.
\tag{5.1}
\]

### Proposition 5.1 (tagged antichain capacity)

Every solution of (4.2)--(4.8) satisfies

\[
\boxed{
|\mathcal A|
\le
\sum_{U\in N_{\mathcal R}(\mathcal A)}
\left(M+(4Q+4)L_U\right)
+E.
}
\tag{5.2}
\]

If \(L_U\le L_Q\) for every tag, where

\[
L_Q
=\left\lfloor
\frac{M}{2(12Q+8)}
\right\rfloor,
\tag{5.3}
\]

then

\[
\boxed{
|\mathcal A|
\le
B_Q|N_{\mathcal R}(\mathcal A)|+E,
\qquad
B_Q:=M+(4Q+4)L_Q<\frac54M.
}
\tag{5.4}
\]

#### Proof

A reserve base trajectory on \(U\) has \(M\) phase columns, each meeting
\(\mathcal A\) at most once. A local cell has at most \(4Q+4\) phase
columns, each again meeting \(\mathcal A\) at most once. Objects on a tag
outside \(N_{\mathcal R}(\mathcal A)\) meet no member of
\(\mathcal A\). At most \(E\) members are patched literally. Summing these
capacities proves (5.2).

The definition (5.3) gives

\[
(4Q+4)L_Q
\le
\frac{(4Q+4)M}{24Q+16}
<\frac M4,
\]

which proves (5.4). \(\square\)

### Corollary 5.2 (width obstruction)

If

\[
R=o(N),\qquad
\sum_U L_U=O(RM/Q),\qquad
E=o(W),
\tag{5.5}
\]

then every coefficient-safe flagged reserve requires

\[
\boxed{\operatorname{width}(\mathcal H)=o(W).}
\tag{5.6}
\]

#### Proof

For every antichain \(\mathcal A\),

\[
|\mathcal A|
\le MR+(4Q+4)\sum_UL_U+E
=O(MR)+E=o(W).
\]

Take the maximum over antichains. \(\square\)

This cut is cross-rank. Applying Hall separately in every row cannot see
it.

## 6. The catalogue results do not imply the width bound

For a partial common matching on \(N-R\) tags, H's proved row estimate is

\[
h_0\le\delta_0+MR,
\qquad
h_{q,\pm}\le\delta_q+c_qR,
\tag{6.1}
\]

where

\[
\delta_0+2\sum_{q=1}^Q\delta_q=o(W).
\tag{6.2}
\]

After charging the \(\delta\)-terms literally, the only information is

\[
\bar h_0\le MR,\qquad
\bar h_{q,\pm}\le c_qR.
\tag{6.3}
\]

These inequalities control horizontal slices of the residual poset.
They do not control its antichains across different ranks.

There is one additional piece of genuine phase structure. For a decorated
trajectory \(P\), let

\[
d(t)=\max\{q:t\le c_q\}.
\tag{6.4}
\]

The claims made at phase \(t\) form the saturated symmetric chain segment

\[
L_{d(t)}(t)\subset\cdots\subset L_0(t)=U_0(t)
\subset\cdots\subset U_{d(t)}(t).
\tag{6.5}
\]

Because a partial common matching has no repeated claimed target, all
these phase-chain segments are vertex-disjoint across all selected
trajectories. Thus the actual hole poset is the complement of a tagged
packing of disjoint symmetric chain segments. This is stronger than
(6.1)--(6.3).

No theorem in the current catalogue note shows that the complement of
such a packing has width \(o(W)\), nor that it extends using the omitted
carrier tags. The explicit construction below is therefore an obstruction
to the row-count and separate-Hall data; it is not claimed to be the
complement of an actually selected catalogue chain packing.

The next construction proves that this is not a merely formal concern.

## 7. An explicit admissible-profile antichain

Assume first that \(m\) is even; floors change nothing asymptotically.
Partition the coordinate set as

\[
[2m]=A\sqcup B,\qquad |A|=|B|=m.
\tag{7.1}
\]

Fix a sufficiently small absolute constant \(a>0\), and for

\[
0\le j\le a\sqrt m
\tag{7.2}
\]

define the upper-rank family

\[
\mathcal A_j
=\left\{
S\in\binom{[2m]}{m+j}:
|S\cap A|=\frac m2-j
\right\}.
\tag{7.3}
\]

### Lemma 7.1 (the union is an antichain)

\[
\mathcal A^*
:=\bigcup_{0\le j\le a\sqrt m}\mathcal A_j
\tag{7.4}
\]

is an antichain.

#### Proof

Members in one \(\mathcal A_j\) have equal size. If \(i<j\),
\(S\in\mathcal A_i\), and \(T\in\mathcal A_j\), then

\[
|S\cap A|=\frac m2-i
>
\frac m2-j=|T\cap A|.
\]

Thus \(S\not\subseteq T\). The reverse inclusion is impossible because
\(|T|>|S|\). \(\square\)

### Lemma 7.2 (linear total size)

Uniformly for \(0\le j\le a\sqrt m\),

\[
|\mathcal A_j|
=
\binom m{m/2-j}
\binom m{m/2+2j}
=\Theta_a(W/\sqrt m).
\tag{7.5}
\]

Consequently

\[
\boxed{|\mathcal A^*|=\Theta_a(W).}
\tag{7.6}
\]

#### Proof

For deviations \(O(\sqrt m)\), the uniform central Stirling estimate gives

\[
\binom m{m/2+s}
=\Theta_a(2^m/\sqrt m).
\]

Multiplying the two factors in (7.5) gives
\(\Theta_a(4^m/m)=\Theta_a(W/\sqrt m)\). There are
\(\Theta(\sqrt m)\) values of \(j\). \(\square\)

Now take

\[
R^*=\left\lfloor\frac{N}{m^{1/4}}\right\rfloor.
\tag{7.7}
\]

Then

\[
R^*=o(N).
\tag{7.8}
\]

For \(j\le a\sqrt m\), the catalogue estimate gives

\[
\frac{R_j}{N}
=(1+o(1))M e^{-j^2/m}
=\Theta_a(M),
\tag{7.9}
\]

and hence

\[
c_j=\Theta_a(M).
\tag{7.10}
\]

Therefore

\[
c_jR^*
=\Theta_a\left(\frac{MN}{m^{1/4}}\right)
=\Theta_a(W/m^{1/4}).
\tag{7.11}
\]

Since

\[
W/\sqrt m=o(W/m^{1/4}),
\tag{7.12}
\]

every slice \(\mathcal A_j\) fits inside the permitted exceptional row
budget \(c_jR^*\) for all sufficiently large \(m\).

### Proposition 7.3 (row budgets permit a fatal antichain)

The rank profile

\[
\mathcal H_{m+j}=\mathcal A_j
\quad(0\le j\le a\sqrt m),
\qquad
\mathcal H_k=\varnothing
\quad\text{otherwise},
\tag{7.13}
\]

obeys H's exceptional row bounds with \(R=R^*=o(N)\), but

\[
\operatorname{width}(\mathcal H)=\Theta(W).
\tag{7.14}
\]

Consequently it cannot be repaired by any reserve satisfying

\[
R=o(N),\qquad
QS=o(W),\qquad
E=o(W),
\tag{7.15}
\]

when every \(O(Q)\)-cost cell contains \(O(Q)\) state columns.

#### Proof

The row bounds follow from (7.11)--(7.12); adding the nonnegative floor
terms \(\delta_j\) only enlarges the allowance. Lemmas 7.1--7.2 give
(7.14).

The reserve base paths have \(MR=o(W)\) state columns. The \(S\) local
cells have \(O(QS)=o(W)\) state columns. Each state column meets the
antichain at most once, and \(E=o(W)\) individual patches do not close the
linear gap. \(\square\)

For odd \(m\), replace all half-integers by floors and ceilings. The same
Stirling estimates and strict monotonicity of the chosen \(A\)-intersection
counts give the result.

### Scope of the obstruction

Proposition 7.3 constructs a hole **profile** compatible with every
row-count estimate currently proved for a partial common matching. It does
not assert that this profile is realized by an actual catalogue matching.
In particular, it does not prove that the complement of the profile can be
packed by the disjoint phase-chain segments (6.5).

Its precise implication is:

> H's scalar leave, exact fractional point, internal rainbowness, and
> separate-rank Hall inequalities cannot by themselves prove the flagged
> reserve theorem. A new structural statement about the actual residual
> poset is necessary.

This is an obstruction to the present proof data, not a disproof of the
desired carefully selected partial matching.

## 8. What the gap/phase structure does and does not prove

The gap/phase structure proves:

1. every individual saturated flag column is locally available
   (Lemma 1.1);
2. every hosted residual chain can be repaired by one positive state
   (Corollary 1.2);
3. the exact hosted one-state problem is governed by Hall condition (2.4);
4. each multi-state local cell has \(O(Q)\) columns and \(O(Q)\) literal
   cost.

It does not prove:

1. that the residual holes of a partial common matching have width
   \(o(W)\);
2. that a Dilworth chain cover can be ordered into \(O(Q)\)-long legal
   rotor phase blocks;
3. that those blocks can be assigned to \(R=o(N)\) reserve tags with
   \(O(M/Q)\) blocks per tag;
4. that the positive sides of localized rectangle cells contain the
   required blocks.

The first missing statement is necessary by Corollary 5.2. The other
three are additional phase-packing constraints even after the width
obstruction is removed.

## 9. The sharp flagged-reserve target

The strongest theorem supported by the exact ledger is now:

### Flagged reserve phase-block theorem (open)

Choose a partial common deterministic catalogue matching on \(N-R\)
carrier tags, with

\[
R=o(N).
\tag{9.1}
\]

For its actual residual hole set \(\mathcal H\), find an integral solution
of (4.2)--(4.8) with

\[
\sum_U L_U=O(RM/Q),
\qquad
S=O(RM/Q),
\qquad
E=o(W).
\tag{9.2}
\]

Equivalently, cover the residual by one reserve base trajectory per tag,
\(O(M/Q)\) legal \(O(Q)\)-phase cells per tag, and \(o(W)\) literal
exceptions.

If this theorem holds, then

\[
(M+2Q+1)N+(12Q+8)S+E
=W+o(W),
\tag{9.3}
\]

and coefficient one follows.

Every proof must establish at least the tagged antichain cut (5.2). The
catalogue's current rowwise Hall theorem does not.

## 10. Final status

The exact ordinary Hall theorem is closed: (2.4) is necessary and
sufficient for hosted one-state flag columns, and it follows directly from
the gap catalogue's phase completeness.

The desired \(R=o(N)\) result needs the factor-\(Q\) batching supplied by
multi-state local cells. That problem is the integral block-cover system
(4.2)--(4.8). It has the mandatory cross-rank cut (5.2), and the row data
currently proved for H's partial matching allow a \(\Theta(W)\) antichain
violating that cut.

Therefore the two-stage flagged reserve theorem is not proved. The precise
next lemma is not another marginal Hall estimate. It is a structural
residual theorem:

\[
\boxed{
\begin{array}{c}
\text{choose the partial common matching so that}\\
\operatorname{width}(\mathcal H)=o(W)
\text{ and }\mathcal H
\text{ has an }o(W/Q)\text{-cell phase-block cover.}
\end{array}
}
\tag{10.1}
\]

Without this, local \(O(Q)\)-cost rotor cells cannot close the
constant-one proof.
