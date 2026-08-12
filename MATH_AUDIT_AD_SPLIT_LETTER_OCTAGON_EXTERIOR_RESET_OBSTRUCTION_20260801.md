# Adversarial audit of the octagon's internal split obstruction and two-host exterior reset

Date: 2026-08-01  
Lane: AD, exterior OR guards / split-letter contraction  
Status: exact internal/exterior scope audit.  Source-level common caps are
checked; physical common-cap compilation and global host construction are
excluded.

## 0. Verdict

The conditional split-host theorem in
MATH_THEOREM_AD_SPLIT_LETTER_OCTAGON_EXTERIOR_POLARITY_AND_RESET_GATE_20260801.md
is sound: \(H\) actual source splits preserve the full retained-phase OR deck
and expose an arbitrary side-cell task bank exactly when the occurrence-to-
side-cell equality graph has a matching.

Its antecedent fails on the current resident coatom tensor **internally**, but
is realized by the explicit exterior hosts
`X_L={a_0,a_1}`, `X_R={a_1,a_2}`.

1. All four unscreened typed exterior debts reverse a strict first- or
   last-occurrence order. No block refinement of any exact source antecedent
   realizes the required boundary prefix or suffix.
2. None of the four masks is contained in one actual source letter or in an
   adjacent source union. One maximal erosion letter has active size at most
   two; an adjacent union has active size at most three, while each debt has
   active size four.
3. The local two-sided tensor rectangle needs no repair because both phases
   have the same total union.
4. The nonlocal donor-swap rectangle cannot be repaired by any number of
   pure refinements in the private-label fixture: an \(a_1\)-bearing old
   block remains strictly interior to every candidate interval.
5. Old split boundaries reset only under one **simultaneous** contraction-
   safe Hall reassignment. Individual reset witnesses or pairwise
   nonconflict are insufficient because contraction can coalesce cells.
6. The two exterior hosts have exact phase-opposite ray identities and add
   two positions while preserving the full old OR deck. Their old side
   targets become native after phase reversal. Therefore they reset with
   `Phi<=2` provided a simultaneous matching transports the entire protected
   bank through contraction **and phase replacement**, and all physical
   boundary rows pass; absent those hypotheses only `Phi'<=Phi+2` follows.

Thus the split pivot gives zero-loss \(O(1)\) birth only after an actual-host
identity is proved. The present tensor supplies no internal host, but its
prepared exterior pair repairs the four polarities two at a time. Reset is
positive and nonaccumulating only at the stated conditional scope.

## 1. Exact refinement-order invariant

Let \(A=(A_0,\ldots,A_{N-1})\). Replace \(A_i\) by a consecutive nonempty
block \(B_{i,1},\ldots,B_{i,r_i}\) with

\[
                 \bigcup_{j=1}^{r_i}B_{i,j}=A_i.        \tag{1.1}
\]

### Lemma 1.1 (prefix and suffix normal form)

Every prefix union of the refinement is

\[
 A_0\cup\cdots\cup A_{i-1}\cup
 B_{i,1}\cup\cdots\cup B_{i,t}                         \tag{1.2}
\]

for one \(i,t\). The suffix statement is the reversal. Consequently:

\[
\begin{aligned}
 f_A(x)<f_A(y)&\Longrightarrow
  \text{every refined prefix containing \(y\) contains \(x\)},\\
 \ell_A(x)<\ell_A(y)&\Longrightarrow
  \text{every refined suffix containing \(x\) contains \(y\)}.
\end{aligned}                                          \tag{1.3}
\]

#### Proof

Only the terminal old block of a prefix can be partial; all earlier blocks
are complete. This proves (1.2) and the first implication. Reverse the word
for the second. \(\square\)

The lemma permits refinement of a tie inside one old letter. It forbids
reversal of events at distinct old positions.

Now let \(E=(E_0,\ldots,E_{L+d-1})\) satisfy

\[
                    T_i=\bigcup_{p=i}^{i+d}E_p.         \tag{1.4}
\]

If \(\alpha_T(x)>0\) and \(\beta_T(x)<L-1\) are the first and last owner
indices containing \(x\), then every exact antecedent satisfies

\[
                 f_E(x)=\alpha_T(x)+d,\qquad
                 \ell_E(x)=\beta_T(x).                 \tag{1.5}
\]

Indeed, the windows at \(\alpha_T(x)-1,\alpha_T(x)\) differ only by adding
source position \(\alpha_T(x)+d\), while the windows at
\(\beta_T(x),\beta_T(x)+1\) differ only by deleting source position
\(\beta_T(x)\).

## 2. The four tensor debts

The active path orders are

\[
\begin{aligned}
 W^0&=(B_2,A_2,A_0,B_0,B_1,A_1,A_3,B_3),\\
 W^1&=(B_2,A_3,A_1,B_0,B_1,A_2,A_0,B_3).              \tag{2.1}
\end{aligned}
\]

The phase-exclusive boundary masks are

\[
\begin{aligned}
 \Pi_0&=K\cup\Phi\cup\{z,a_0,a_2,a_3\},&
 \Pi_1&=K\cup\Phi\cup\{z,a_1,a_2,a_3\},\\
 \Sigma_0&=K\cup\Phi\cup\{z,a_0,a_1,a_3\},&
 \Sigma_1&=K\cup\Phi\cup\{z,a_0,a_2,a_3\}.             \tag{2.2}
\end{aligned}
\]

### Theorem 2.1 (arbitrary-inverse polarity obstruction)

For every \(d\ge1\):

* no refinement of a phase-one exact antecedent has \(\Pi_0\) as a boundary
  prefix or \(\Sigma_0\) as a boundary suffix;
* no refinement of a phase-zero exact antecedent has \(\Pi_1\) as a boundary
  prefix or \(\Sigma_1\) as a boundary suffix.

#### Proof

In phase one, \(a_1\) first occurs before \(a_0\). Equations (1.3)--(1.5)
force every refined prefix reaching \(a_0\) to contain \(a_1\), whereas
\(\Pi_0\) omits it. Phase zero reverses these first occurrences, excluding
\(\Pi_1\).

In phase one, the last \(a_1\) occurs before the last \(a_2\). Every suffix
reaching \(a_1\) therefore contains \(a_2\), whereas \(\Sigma_0\) omits it.
Phase zero reverses these last occurrences, excluding \(\Sigma_1\).
\(\square\)

Adding a private marker on the exterior shore makes this an occurrence
obstruction: any witness containing the marker must enter the tensor as a
prefix or suffix. The unmarked mask may still have an unrelated internal
witness in the common internal deck.

The sharper source positions are

\[
\begin{array}{c|cc|cc}
 &f(a_0)&f(a_1)&\ell(a_1)&\ell(a_2)\\ \hline
 \text{phase 1}&4d+9&3d+5&5d+13&6d+17,
\end{array}                                             \tag{2.3}
\]

with \(a_0,a_1\) and \(a_1,a_2\) exchanged in phase zero. These follow by
combining the owner indices in the main theorem with (1.5).

### Proposition 2.2 (dominating-letter faces also fail)

After active projection, the maximal erosion alternates the eight size-two
active path vertices \(V_i\) with their size-one intersections
\(V_i\cap V_{i+1}\). For \(d\ge2\), every intersection occurs between its
two vertex states, so every adjacent active union has size at most two. For
\(d=1\), three intersection states have zero multiplicity; the adjacent
vertices are Johnson adjacent and their union has size three.

Every exact source letter is contained in the corresponding maximal erosion
letter. Hence one exact letter has active size at most two and an adjacent
union at most three for all exact antecedents. Every mask in (2.2) has active
size four. The one-letter and adjacent-union host criteria both fail.

The exterior screening criterion is weaker than pointwise profile equality.
For example a left exterior suffix containing either \(a_0\) or \(a_1\)
already gives another phase-one prefix witness for the old phase-zero target.
The obstruction concerns exterior states omitting both polarity labels.

### Proposition 2.3 (the exterior two-host identities pass)

Let

\[
 X_L=\{a_0,a_1\},\quad X_R=\{a_1,a_2\},
\]

and let the phase-common source corridors be

\[
 R_L=K\cup\Phi\cup\{z,a_2,a_3\},\qquad
 R_R=K\cup\Phi\cup\{z,a_0,a_3\}.                    \tag{2.4}
\]

In phase zero orient the two splits as `(a_0|a_1)` and `(a_2|a_1)`;
in phase one use `(a_1|a_0)` and `(a_1|a_2)`.  Then the packet-near cells
are exactly

\[
 \{a_{1-\epsilon}\}\cup R_L=\Pi_{1-\epsilon},
 \qquad
 R_R\cup\{a_{2-\epsilon}\}=\Sigma_{1-\epsilon}.       \tag{2.5}
\]

Both blocks retain their old unions, so simultaneous full-block lift
preserves every old interval OR injectively.  The exact refinement charge is
two positions.  Assigning cap `X_L` to both left pieces and `X_R` to both
right pieces is phase independent.

This does not contradict Propositions 2.1--2.2: those propositions concern
the tensor-internal inverse, while these are prepared exterior letters.  If
the hosts themselves are absent from the ambient word, planting plus
refining them costs four positions relative to the bare tensor.

## 3. Generic product rectangles need growing split support

Split \(H\) old positions into binary blocks \((Z_p,T_p)\). Apart from
full-block lifts, the exact side-cell normal form has:

* one right-facing chain beginning at \(T_p\) and one left-facing chain
  ending at \(Z_p\), hence \(2H\) nested chains; and
* one double-partial cell
  \[
       T_p\cup A_{p+1}\cup\cdots\cup A_{q-1}\cup Z_q
                                                               \tag{3.1}
  \]
  for each \(p<q\), hence \(\binom H2\) additional points.

The singleton halves are the first members of the corresponding one-sided
chains, so they add no further chain class.

### Proposition 3.1 (side-cell width bound)

Let \({\cal U}\) be target masks absent from the old OR deck and realized
after \(H\) binary splits. Then

\[
 \operatorname{width}({\cal U})
       \le 2H+\binom H2={H(H+3)\over2}.                 \tag{3.2}
\]

If \({\cal U}\) contains the antidiagonal of a product
\([0,r]\times[0,r]\), then

\[
 H\ge\left\lceil{\sqrt{8r+17}-3\over2}\right\rceil
   =\Omega(\sqrt r).                                   \tag{3.3}
\]

#### Proof

Every target absent from the old deck must use a side cell. A nested ray
meets an antichain in at most one mask, and each double-partial cell supplies
at most one. This proves (3.2). The \(r+1\) masks with \(i+j=r\) in the
product are incomparable; solving \(H(H+3)/2\ge r+1\) gives (3.3).
\(\square\)

The old-deck qualification is essential. Every rectangle entry already in
the old deck is transported automatically by a full-block lift and consumes
no side-cell width. The bound applies to the residual family after deleting
all targets with unaffected old witnesses. It is necessary, not sufficient:
the surviving rays and points must still have the exact values and pass
Hall.

## 4. Why the donor rectangle does not contract

The local full-span tensor relation is already identical in both phases,
because their total union is common. It needs no split ticket.

The donor-swap rectangle is different. In the private-label fixture from the
earlier exterior audit, the new order is

\[
                         P_2\quad B_1\quad P_1,          \tag{4.1}
\]

where \(a_1\in B_1\), while selected old targets use one private label from
each donor bank and omit \(a_1\).

### Lemma 4.1 (interior-poison invariant)

Suppose a target needs labels whose only occurrences lie on opposite sides
of one old interior block \(C\), and \(C\) contains a label omitted by the
target. No block refinement of the word realizes that target.

#### Proof

Every interval containing both private labels contains every piece of the
strictly interior block. Their union is the old block \(C\), including the
forbidden label. \(\square\)

This proves a no-go for every number of pure splits in the frozen donor
order. An unaffected duplicate or a non-block rethread is not excluded.

## 5. Exact reset and the needed scope correction

Let \(V\) refine \(A\), and contract a chosen family \({\cal R}\) of old
split blocks. For a refined interval \(J\), let
\(\operatorname{cl}_{\cal R}(J)\) be its smallest full-block closure.

### Lemma 5.1 (closure dominance)

A witness \(J\) of target \(S\) survives through its contraction closure iff

\[
 \operatorname{OR}_V(J)=S,\qquad
 \operatorname{OR}_V(\operatorname{cl}_{\cal R}(J))=S. \tag{5.1}
\]

Only the omitted pieces at the two endpoint blocks are added. For binary
splits \(X_p=Z_p\cup T_p\), the exact tests are

\[
\begin{array}{c|c}
\text{side cell}&\text{closure-safe iff}\\ \hline
[T_p,\ldots]&Z_p\subseteq S,\\
[\ldots,Z_q]&T_q\subseteq S,\\
[T_p,\ldots,Z_q]&Z_p\cup T_q\subseteq S.
\end{array}                                             \tag{5.2}
\]

Full-block lifts are always safe.

Define the reset deficit

\[
 \delta_{\cal R}(J)=
 \operatorname{OR}_V(\operatorname{cl}_{\cal R}(J))
       \setminus\operatorname{OR}_V(J).                 \tag{5.3}
\]

Thus (5.1) is exactly \(\delta_{\cal R}(J)=\varnothing\). If a target is
absent from the contracted old deck, every one of its side witnesses has
nonempty deficit; otherwise its closure would already be an old cell of the
same value. Therefore every genuinely new tensor debt, if an actual split
host existed, would be non-self-resetting at birth.

For occurrence-labelled targets, individual safe witnesses are not enough.
Reset is equivalent to a matching from protected target occurrences to
distinct contracted cells of the required value, after deleting deadline-
or residence-inadmissible edges.

This qualifies recurrence (5.1) of the main polarity theorem. The phrase
“\(g\) independently certified resettable” must mean:

> one simultaneous contraction of those \(g\) boundaries admits a saturating
> matching jointly with the new task bank and all protected occurrence rows.

If it means merely that each boundary can be contracted separately, the
recurrence is false: different safe refined cells may coalesce to one
contracted cell.

Under the simultaneous meaning, if \(\Phi\) old boundaries remain, \(g\)
are reset in one certified contraction, and \(r\) fresh boundaries are
created, then

\[
                         \Phi'\le \Phi-g+r.             \tag{5.4}
\]

Old rays transported by full-block lifts contribute no essential reset
debt. A genuinely new side-cell-only target generally does; it can reset
only after an alternate witness is supplied. Therefore old boundaries do
not automatically reset, and \(O(1)\) essential births per transition can
accumulate linearly.

For the two exterior hosts of Proposition 2.3, the required alternate values
are present natively after phase reversal: the old side pair
`Pi_(1-epsilon),Sigma_(1-epsilon)` is the new phase's native pair.  Therefore
the recurrence has `g=2,r=2`, and hence `Phi'<=2`, provided all of the
following are checked together:

* both split orientations are legal at the physical Johnson boundary and
  satisfy q1, residence, deadline and common-cap rows;
* the two old blocks can be contracted simultaneously while a single Hall
  matching retains every inherited/protected occurrence;
* after replacing the packet phase, one simultaneous matching places the
  entire protected bank and the disappearing side targets in opposite-phase
  native/full-block cells; and
* the reverse-split cells are free for the newly missing pair.

The literal OR identities prove none of these ambient conditions.  At
the source-word level the reset mechanism is exact; at the physical compiler
level it remains conditional.

The cross-phase matching is genuinely additional.  At `d=1` in the sharp
inverse, `S={z,a_3,f_0}=Q^0_26` is safe under both exterior contractions but
is absent from both the contracted and expanded phase-one interval decks.
Thus contraction Hall alone cannot justify reset.

## 6. Proved boundary

If the exterior debts are actual side-cell rays or rectangles of \(O(1)\)
source splits, the split-host theorem preserves the full retained-phase OR
deck at \(O(1)\) added length.  The octagon's two prepared exterior hosts do
exactly this at refinement charge two.  If all old side-cell-only occurrences
also have the displayed simultaneous contraction-safe and cross-phase Hall
reassignment, the same two boundaries reset under phase reversal rather than
accumulate.

The current tensor fails the actual-host premise only **internally** for all
four unscreened typed debts.  The frozen donor rectangle still fails it even
with unboundedly many pure splits.  Common-cap containment for the two host
pieces is exact, but physical owner, q1, residence, deadline and matching
compilation remain separate.
