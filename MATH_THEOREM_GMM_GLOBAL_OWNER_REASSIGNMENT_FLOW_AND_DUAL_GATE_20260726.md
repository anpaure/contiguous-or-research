# GMM global band reassignment: the exact owner-coloured circulation and its dual gates

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

The direct excursion obstruction

\[
                         G+R=A_H-W
\]

does not survive arbitrary global reassignment as a linear invariant:
an inserted occurrence of owner \(X\) may replace the original occurrence
of \(X\), and incoming and outgoing ports from two different occurrences
of \(X\) may be spliced.  The surviving problem is an integral
owner-coloured circulation.

This note gives its exact formulation.

Let \(\Gamma_{\rm GMM,H}\) be the catalogue of all legal \(H\)-memory
columns obtainable from retained or inserted occurrences of the fixed GMM
band enumeration, after all allowed equal-owner port reassignments.  A
column

\[
                         \gamma=(X_0,X_1,\ldots,X_H)             \tag{0.1}
\]

is included only when:

1. every consecutive pair is a licensed Johnson transition of the
   retained/inserted band catalogue;
2. the \(2H\) exchange labels are pairwise distinct;
3. every provenance or port constraint of the chosen reassignment model
   is respected; and
4. \(X_0\) is the owner consumed by the column.

Put

\[
 \operatorname{pre}\gamma=(X_0,\ldots,X_{H-1}),\qquad
 \operatorname{suf}\gamma=(X_1,\ldots,X_H).         \tag{0.2}
\]

There is a coefficient-one globally reassigned \(H\)-safe owner
circulation if and only if the integer system

\[
 \boxed{
                         Az=\mathbf1,\qquad
                         Qz=\mathbf1,\qquad
                         Mz=0,\qquad
                         z\in\mathbb Z_{\ge0}^{\Gamma_{\rm GMM,H}}}
                                                               \tag{0.3}
\]

is feasible, where \(A\) records the root owner \(X_0\), \(Q\) records
the retained/inserted occurrence slot consumed by the column, and \(M\)
is the pre-minus-suffix memory incidence matrix.  Thus \(Az=\mathbf1\)
and \(Qz=\mathbf1\) are the two shores of the global reassignment
matching.

For any solution \(z\), let \(\kappa(z)\) be the number of weakly
connected components of its memory-state support.  Free splicing at equal
memory states gives exactly

\[
 \boxed{
 \min\{\text{owner cycles realizing }z\}=\kappa(z).}            \tag{0.4}
\]

Thus the requested cycle theorem is precisely

\[
 \boxed{
 \text{find an integral solution of (0.3) with }
                         \kappa(z)=O(W/m).}          \tag{0.5}
\]

The shallow shadows are also exact linear images before support is taken.
If \(S_{q,\epsilon,T;\gamma}\) records the lower or upper target emitted
by \(\gamma\), then

\[
 L_{q,\epsilon}(T;z)
 =\sum_\gamma S_{q,\epsilon,T;\gamma}z_\gamma,
\qquad
 \mathfrak H(z)
 =\sum_{q,\epsilon,T}
       \bigl(1-L_{q,\epsilon}(T;z)\bigr)_+.          \tag{0.6}
\]

The full surviving target is therefore

\[
 \boxed{
 Az=\mathbf1,\quad Qz=\mathbf1,\quad Mz=0,\quad
 \kappa(z)=O(W/m),\quad
 \mathfrak H(z)=o(W),\quad z\text{ integral}.}      \tag{0.7}
\]

There are two exact dual obstruction forms.  The second becomes an
if-and-only-if Hall system after restricting the target weights to
\([0,1]\); see Theorem 4.2.

### Feasibility dual

The real relaxation of (0.3) is infeasible if and only if there are owner
weights \(u_X\), occurrence-slot weights \(v_r\), and memory-state
potentials \(\phi_\sigma\) such that

\[
 \boxed{
 u_{X_0}+v_{r(\gamma)}
          +\phi_{\operatorname{pre}\gamma}
          -\phi_{\operatorname{suf}\gamma}\ge0
 \quad(\gamma\in\Gamma_{\rm GMM,H}),\qquad
 \sum_Xu_X+\sum_rv_r<0.}                            \tag{0.8}
\]

### Literal shadow dual

Let \(y_{q,\epsilon,T}\ge0\).  If \(u,v,\phi\) satisfy

\[
 \boxed{
 \sum_{q,\epsilon}
   y_{q,\epsilon,T_{q,\epsilon}(\gamma)}
 \le
 u_{X_0}+v_{r(\gamma)}
          +\phi_{\operatorname{pre}\gamma}
          -\phi_{\operatorname{suf}\gamma}
 \quad(\gamma\in\Gamma_{\rm GMM,H}),}               \tag{0.9}
\]

then every integral or fractional owner circulation obeys

\[
 \sum_{q,\epsilon,T:
       L_{q,\epsilon}(T;z)=0}y_{q,\epsilon,T}
 \ge
 \sum_{q,\epsilon,T}y_{q,\epsilon,T}
       -\sum_Xu_X-\sum_rv_r.                        \tag{0.10}
\]

Thus a gap \(\Omega(W)\) on the right of (0.10) is a literal
positive-density obstruction, valid against every global reassignment.

No feasible integral solution of (0.7), and no potentials satisfying
(0.8) or (0.9) with a linear gap, are presently derived from GMM
tightness.  This is not merely a missing marginal calculation:
\([A;Q;M]\) is a coloured-circulation matrix and need not be totally
unimodular.  Even if (0.8) has no witness, the integer semigroup in (0.3)
may have an alternating integrality obstruction.

The rigorous advance is therefore an exact reduction and theorem of
alternatives.  The previous \(G+R\) identity rules out local contraction;
the global variant survives exactly as (0.7).

## 1. Band-derived occurrence ports

Fix one tight enumeration of

\[
                         \bigcup_{j=0}^{H}\binom{[p]}{m-j}.
\]

Expand every distance-two tight transition into two labelled cube flips.
Every retained rank-\(m\) visit and every synthetic rank-\(m\) visit
obtained by pairing a deletion with an insertion has:

* an owner label \(X\in\binom{[p]}m\);
* an incoming physical port;
* an outgoing physical port;
* a finite left exchange history; and
* a finite right exchange history.

Several occurrence copies may have the same owner label.  Global
reassignment is allowed to take the incoming port from one occurrence of
\(X\) and the outgoing port from another, provided their histories are
compatible through depth \(H\).  This is the precise freedom absent from
direct excursion contraction.

Fix a retention/insertion ledger with exactly \(W\) occurrence slots
\(\mathcal R\).  If the construction is also allowed to choose the
ledger, the full problem is the disjoint union of the systems below over
all admissible ledgers.  Any shared retention/insertion choice must be
fixed before forming one catalogue, or represented by additional exact
packing rows; it cannot be replaced by independent per-column choices.
A column
\(\gamma\) records the unique slot

\[
                         r(\gamma)\in\mathcal R
\]

which it assigns to its root owner.

An admissible column (0.1) records one complete compatible splice.  If the
model has an indivisible provenance group, shared lower occurrence, or
shared insertion choice, that whole choice must be included in the column
definition.  Splitting such a choice into independent arcs enlarges the
catalogue and invalidates any positive theorem.

The catalogue is finite.  It may contain many columns rooted at one
owner or using one slot, but a coefficient-one reassignment must select
exactly one in every owner fibre and exactly one in every slot fibre.

## 2. Owner and memory matrices

Let \(\Sigma_{H-1}\) be the set of **decorated** length-\(H\) memory
states

\[
 \sigma=(X_0,\ldots,X_{H-1};\eta),
\]

where the displayed owner word is safe and \(\eta\) contains exactly the
incoming/outgoing port identities, occurrence provenance, and partial
exchange history that must agree when two columns are concatenated.  We
suppress \(\eta\) in formulas.  Thus equality of two memory states means
physical port compatibility, not merely equality of their owner tuples.
The prefix and suffix in (0.2) include these decorations.

Define

\[
 A_{X,\gamma}=\mathbf1_{\{X_0=X\}},                \tag{2.1}
\]

\[
 Q_{r,\gamma}=\mathbf1_{\{r(\gamma)=r\}},           \tag{2.2}
\]

\[
 M_{\sigma,\gamma}
 =\mathbf1_{\{\operatorname{pre}\gamma=\sigma\}}
  -\mathbf1_{\{\operatorname{suf}\gamma=\sigma\}}. \tag{2.3}
\]

Because every column has one root, an integral nonnegative solution of
\(Az=\mathbf1\) is automatically zero-one inside every owner fibre.
The equation \(Qz=\mathbf1\) is the exact occurrence-slot bijection.

### Theorem 2.1 (global reassignment/circulation equivalence)

The following are equivalent.

1. There is a global reassignment of the retained and inserted band
   occurrence ports into an exact \(H\)-safe successor on all \(W\)
   middle owners.
2. The integer system (0.3) is feasible.

#### Proof

A global successor chooses one outgoing \(H\)-column at every owner, so
its column vector satisfies \(Az=\mathbf1\).  It assigns every retained
or inserted slot once, giving \(Qz=\mathbf1\).  Consecutive selected
columns overlap in their last and first \(H\) owners.  Therefore every
memory state is entered and left equally often, which is \(Mz=0\).

Conversely, regard every selected column as a directed edge from its
prefix memory state to its suffix memory state.  Equation \(Mz=0\) makes
this finite directed multigraph Eulerian.  Decompose each weak component
into an Euler circuit.  Consecutive edges of an Euler circuit have equal
suffix and prefix states, so their owner words concatenate consistently.
Every resulting \(H\)-window is one selected admissible column and is
therefore physical and safe.  Finally \(Az=\mathbf1\) makes every middle
owner the root of exactly one selected window, while \(Qz=\mathbf1\)
makes the reassignment use every chosen occurrence slot once.  Thus the
concatenated cycles realize the required bijection. \(\square\)

This proof is occurrence-sensitive.  If two equal owner labels have
different histories, they may be spliced only when a column certifies the
combined prefix and suffix.

## 3. Exact cycle count under equal-state splicing

Let \(D_z\) be the directed multigraph on memory states formed by the
selected columns.  It is Eulerian.

### Theorem 3.1 (minimum cycle count)

Among all equal-state pairings of the selected incoming and outgoing
column occurrences, the minimum number of owner cycles is exactly the
number \(\kappa(z)\) of weak components of \(D_z\).

#### Proof

No chronology can cross two different weak components of \(D_z\), so at
least one cycle is required per component.  Every nontrivial weak
component of an Eulerian directed multigraph has an Euler circuit using
all its edges.  An isolated state supporting loops likewise has one
Euler circuit.  Choosing one Euler circuit per component attains
\(\kappa(z)\). \(\square\)

Consequently cycle count is not an additional local port statistic.  It
is a support-connectivity property of the selected circulation.

A simple statewise lower obstruction follows.  Let
\(\mathcal C_1,\ldots,\mathcal C_r\) be the weak components of the full
catalogue state graph, and let

\[
 \mathcal O_j
 =\{X:\text{some column rooted at \(X\) lies in }\mathcal C_j\}.
\]

Also put

\[
 \mathcal R_j
 =\{r:\text{some column using occurrence slot \(r\) lies in }
             \mathcal C_j\}.
\]

Every solution has

\[
 \kappa(z)\ge
 \min\left\{|J|:
       \bigcup_{j\in J}\mathcal O_j
       =\binom{[p]}m,\quad
       \bigcup_{j\in J}\mathcal R_j
       =\mathcal R\right\}.                        \tag{3.1}
\]

Thus a catalogue-component cover number
\(\omega(W/m)\) is an explicit cycle obstruction.  GMM tightness alone
does not determine the sets \(\mathcal O_j\).

## 4. Exact shallow traces

For an admissible column
\(\gamma=(X_0,\ldots,X_H)\), put

\[
 T_{q,-}(\gamma)=\bigcap_{i=0}^{q}X_i,\qquad
 T_{q,+}(\gamma)=\bigcup_{i=0}^{q}X_i.              \tag{4.1}
\]

Safety gives their exact ranks.  Define

\[
 S_{q,\epsilon,T;\gamma}
 =\mathbf1_{\{T_{q,\epsilon}(\gamma)=T\}}.          \tag{4.2}
\]

Every selected root emits exactly one target at every typed depth, so

\[
                         \sum_TL_{q,\epsilon}(T;z)=W.           \tag{4.3}
\]

The missing objective is (0.6).  It depends on the support of the load,
not merely its total or first moments.

### Theorem 4.1 (weighted shadow-potential obstruction)

Assume (0.9).  Then (0.10) holds for every real nonnegative solution of
\(Az=\mathbf1,Qz=\mathbf1,Mz=0\), and hence for every integral global
reassignment.

#### Proof

Multiply (0.9) by \(z_\gamma\) and sum.  The memory potentials telescope:

\[
\begin{aligned}
 \sum_\gamma z_\gamma
   \sum_{q,\epsilon}
      y_{q,\epsilon,T_{q,\epsilon}(\gamma)}
 &\le
 \sum_Xu_X\sum_{\gamma:X_0=X}z_\gamma\\
 &\quad+\sum_rv_r\sum_{\gamma:r(\gamma)=r}z_\gamma\\
 &\quad+
 \sum_\sigma\phi_\sigma(Mz)_\sigma\\
 &=\sum_Xu_X+\sum_rv_r.
\end{aligned}                                      \tag{4.4}
\]

The left side counts weighted target occurrences.  The total weight of
the distinct covered target support is no larger.  Subtracting it from
the total target weight proves (0.10). \(\square\)

This is a whole-column, all-depth dual.  A weight supported only at
depth two is permitted; so are correlated weights on complete lower and
upper flag profiles.

### Theorem 4.2 (exact fractional all-order Hall criterion)

Let

\[
 \mathcal P=
 \{z\ge0:Az=\mathbf1,\ Qz=\mathbf1,\ Mz=0\},       \tag{4.5}
\]

and fix an allowed aggregate hole budget \(E\).  For
\(0\le y_{q,\epsilon,T}\le1\), write

\[
 w_y(\gamma)=
 \sum_{q,\epsilon}
 y_{q,\epsilon,T_{q,\epsilon}(\gamma)}.            \tag{4.6}
\]

Assume \(\mathcal P\ne\varnothing\).  Then the following are equivalent.

1. Some \(z\in\mathcal P\) has \(\mathfrak H(z)\le E\).
2. For every \(y\in[0,1]^{\mathcal T}\),
   \[
     \max_{z\in\mathcal P}\sum_\gamma w_y(\gamma)z_\gamma
       \ge \sum_{q,\epsilon,T}y_{q,\epsilon,T}-E.  \tag{4.7}
   \]
3. For every \(y\in[0,1]^{\mathcal T}\),
   \[
   \min_{u,v,\phi}
     \left(\sum_Xu_X+\sum_rv_r\right)
       \ge \sum_{q,\epsilon,T}y_{q,\epsilon,T}-E,  \tag{4.8}
   \]
   where the minimum is over
   \[
   w_y(\gamma)\le
       u_{X_0}+v_{r(\gamma)}
       +\phi_{\operatorname{pre}\gamma}
       -\phi_{\operatorname{suf}\gamma}
       \quad(\gamma\in\Gamma_{\rm GMM,H}).        \tag{4.9}
   \]

#### Proof

For a scalar \(x\),

\[
                         (1-x)_+=\max_{0\le y\le1}y(1-x).
\]

Therefore

\[
 \mathfrak H(z)
 =\max_{y\in[0,1]^{\mathcal T}}
   \left(\sum_Ty_T-\sum_\gamma w_y(\gamma)z_\gamma\right).    \tag{4.10}
\]

The polytope \(\mathcal P\) is compact, because \(Az=\mathbf1\) and
every column has one owner root imply \(\sum_\gamma z_\gamma=W\).
Finite-dimensional minimax now interchanges \(\min_{z\in\mathcal P}\)
and \(\max_y\) in (4.10), proving the equivalence of 1 and 2.  For fixed
\(y\), the maximum in (4.7) is a linear program.  Its dual is precisely
the minimum (4.8) subject to (4.9).  Strong LP duality proves the last
equivalence. \(\square\)

Thus a literal fractional shadow obstruction at budget \(E\) is exactly
a target weight \(y\in[0,1]^{\mathcal T}\) and feasible potentials in
(4.9) whose objective is strictly below \(\sum_Ty_T-E\).  A deficit
\(cW\) rules out \(o(W)\) holes.  Theorem 4.1 is the directly usable
certificate form, while Theorem 4.2 proves that no other fractional
shadow cut is missing.

For integral \(z\), (4.7)--(4.9) remain necessary but need not be
sufficient: an alternating or projective-plane-type configuration can
have a fractional cover and no integral owner/slot resolution.

## 5. Farkas alternative for the real circulation

Let

\[
 C=\begin{bmatrix}A\\Q\\M\end{bmatrix},
 \qquad
 b=\begin{bmatrix}\mathbf1\\\mathbf1\\0\end{bmatrix}.
\]

Farkas' lemma gives:

### Theorem 5.1 (exact fractional alternative)

Exactly one of the following holds.

1. There is \(z\ge0\) with \(Cz=b\).
2. There are \(u,v,\phi\) satisfying (0.8).

#### Proof

The alternative to \(Cz=b,z\ge0\) is a row vector
\((u,v,\phi)\) with

\[
                         (u,v,\phi)^TC\ge0,\qquad
                         (u,v,\phi)^Tb<0.
\]

Written columnwise, these are exactly the two inequalities in (0.8).
\(\square\)

The theorem is only fractional.  Integral feasibility is the semigroup
membership statement

\[
 \begin{bmatrix}\mathbf1\\\mathbf1\\0\end{bmatrix}
 \in
 \sum_{X\in\binom{[p]}m}
 \left\{
  \begin{bmatrix}e_X\\e_{r(\gamma)}\\
  e_{\operatorname{pre}\gamma}
   -e_{\operatorname{suf}\gamma}
  \end{bmatrix}:
  \gamma\in\Gamma_{\rm GMM,H},\ X_0=X
 \right\}.                                         \tag{5.1}
\]

The summands are finite configuration sets, not matroid bases.  Therefore
absence of a Farkas witness does not prove an integral state.

### Theorem 5.2 (integral character obstruction)

Fix an integer \(k\ge2\).  Suppose there are residues

\[
 \alpha_X,\ \beta_r,\ \psi_\sigma\in\mathbb Z/k\mathbb Z
\]

such that every admissible column satisfies

\[
 \alpha_{X_0}+\beta_{r(\gamma)}
 +\psi_{\operatorname{pre}\gamma}
 -\psi_{\operatorname{suf}\gamma}=0\pmod k,        \tag{5.2}
\]

but

\[
 \sum_X\alpha_X+\sum_r\beta_r\ne0\pmod k.         \tag{5.3}
\]

Then (0.3) has no integral solution.

#### Proof

Multiply (5.2) by the integers \(z_\gamma\) and sum.  The memory terms
cancel by \(Mz=0\), while the owner and slot equations leave the residue
in (5.3), a contradiction. \(\square\)

This is the first exact integral discrepancy invisible to Farkas
potentials.  More general semigroup holes need not be detected by a
single finite character, but every parity or determinant obstruction
appears in this form after passing to the lattice quotient generated by
the catalogue columns.

### Exact cut formulation of the cycle target

For completeness, the nonlinear-looking condition
\(\kappa(z)\le K\) has an exact mixed-integer cut formulation.  Introduce
root variables \(a_X\in\{0,1\}\).  Since an admissible column has owner
successor \(X_1\), impose

\[
 \sum_Xa_X\le K,                                  \tag{5.4}
\]

and, for every nonempty \(S\subseteq\binom{[p]}m\),

\[
 \sum_{X\in S}a_X+
 \sum_{\gamma:X_0\in S,\ X_1\notin S}z_\gamma
 \ge1.                                             \tag{5.5}
\]

For an integral solution of (0.3), the selected owner arcs
\(X_0\to X_1\) form a permutation.  Indeed, summing the memory-balance
rows over states whose first owner is \(X\) gives

\[
 \sum_{\gamma:X_0=X}z_\gamma
 -\sum_{\gamma:X_1=X}z_\gamma=0;                   \tag{5.6}
\]

the first sum is one by \(Az=\mathbf1\), so every owner also has
indegree one.  If (5.5) holds, taking \(S\) to be
one complete permutation cycle shows that the cycle contains a marked
root.  Conversely, if every cycle contains a marked root, every nonempty
\(S\) either contains a root or is a proper subset of one of its
intersected cycles and has a selected arc leaving it.  Hence (5.4)--(5.5)
are equivalent to at most \(K\) chronology cycles.

Likewise introduce \(d_{q,\epsilon,T}\ge0\) and impose

\[
 d_{q,\epsilon,T}
 +\sum_\gamma S_{q,\epsilon,T;\gamma}z_\gamma\ge1,
 \qquad
 \sum_{q,\epsilon,T}d_{q,\epsilon,T}\le E.         \tag{5.7}
\]

For integral \(z\), the least possible \(d\) is exactly the missing
indicator in (0.6).  Equations (0.3), (5.4)--(5.5), and (5.7) are
therefore an exact integer matching/flow formulation of the global
variant, with
\(K=O(W/m)\) and \(E=o(W)\).

## 6. Why the old contraction identity is no longer a dual

For direct excursion-by-excursion contraction, every internal geodesic
occurrence was added while every original rank-\(m\) occurrence was kept.
This forced the scalar defect

\[
                         G+R=A_H-W.
\]

Global reassignment changes the ledger.  If a synthetic occurrence has
owner \(X\), it may consume the unique root row \(A_X\) and the original
occurrence of \(X\) may be omitted.  Hence \(G\) is no longer an added
owner count.  Likewise, incoming history from one occurrence and outgoing
history from another may remove a local return.

Algebraically, the scalar \(G+R\) is not a linear functional constant on
the columns of (0.3).  It therefore yields neither potentials (0.8) nor
weights (0.9).  Any attempt to reuse it after global reassignment would
silently count both the retained and displaced occurrence of the same
owner.

What remains invariant is only:

* one selected root per physical owner;
* zero total memory boundary;
* the literal target images of the selected columns; and
* the support connectivity controlling cycles.

These are exactly the rows retained in (0.7).

## 7. What would constitute a construction

A positive proof may proceed in three exact stages.

1. **Fractional circulation.**  Construct \(z^{\rm frac}\ge0\) satisfying
   \(Az=\mathbf1,Qz=\mathbf1,Mz=0\), preferably with target loads at
   least one outside \(o(W)\) tokens.
2. **Integralization.**  Prove normality or an integer-decomposition
   theorem for the owner-coloured circulation semigroup (5.1), preserving
   the target reserve.
3. **Support joining.**  Choose the integral point so its state support
   has \(O(W/m)\) weak components.  Theorem 3.1 then supplies the required
   chronology cycles with no further owner cost.

Neither the vertical rank counts of the band nor the original cyclic
tight enumeration proves Stage 1: the former omit memory balance, while
the latter repeats or omits owner roots after synthetic insertion.

## 8. Certified boundary

Proved:

1. the exact owner-coloured \(H\)-memory circulation formulation (0.3);
2. its equivalence with global occurrence reassignment;
3. the exact minimum cycle formula (0.4);
4. the complete shallow-shadow functional (0.6);
5. the exact real Farkas alternative (0.8);
6. the whole-column literal shadow dual (0.9)--(0.10);
7. the exact all-order fractional Hall criterion (4.7)--(4.9);
8. the integral character obstruction (5.2)--(5.3);
9. the exact subtour-cut and hole-budget formulation (5.4)--(5.5) and
   (5.7); and
10. the reason the former \(G+R\) obstruction does not survive global
   reassignment.

Not proved:

1. a real feasible circulation;
2. an integral circulation;
3. a dual certificate with \(\Omega(W)\) gap;
4. \(O(W/m)\) support components;
5. \(o(W)\) shallow holes; or
6. coefficient one.

The global GMM variant is therefore neither constructed nor refuted.  It
has been reduced to the exact integral system (0.7); any further claim
must exhibit either its columns or one of the dual certificates above.
