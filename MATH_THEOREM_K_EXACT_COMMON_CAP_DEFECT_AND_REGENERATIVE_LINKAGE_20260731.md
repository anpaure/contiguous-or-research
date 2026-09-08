# Exact common-cap defect and regenerative linkage under interior exchanges

Date: 2026-07-31  
Lane: K, common-cap/compiler  
Status: unconditional abstract theorem and sharp local obstruction; the
Boolean/Pascal regenerative-bank existence hypothesis remains open

## 0. Verdict

There is an exact common-cap defect which is weaker than a perfect compiler
and strong enough to give an additive-constant word theorem.  It is not
scalar slot slack.  Once the proposed chronology has passed literal replay,
residence, every declared upper-shadow row, and all fixed socket/prepin
tests, put

\[
 V_*(Z)=\min_Q\bigl(|\mathcal T|-\nu(H_Q)\bigr),
\tag{0.1}
\]

where \(Q\) ranges over literal middle-realizing guard words and \(H_Q\)
is the target--cell graph retained by \(Q\).  Then \(V_*(Z)\) is exactly
the minimum number of target masks omitted by a partial literal common-cap
compiler.  Equivalently,

\[
 V_*(Z)=
 \min_Q\max_{X\subseteq\mathcal T}
 \bigl(|X|-|N_{H_Q}(X)|\bigr).
\tag{0.2}
\]

Thus \(V_*=0\) is equivalent to an exact common-cap compiler, while a
length-\(B(k)\) physical scaffold with \(V_*=v\) gives a word of length at
most \(B(k)+v\) by appending the \(v\) omitted masks.

For a fixed guard transition through an interior exchange, the exact
regenerative condition is cutwise.  If \(K^-\) and \(K^+\) are respectively
the old and new nontransported cell banks, then a target cut \(X\) changes
by

\[
 d'(X)=d(X)+|N_{K^-}(X)|-|N_{K^+}(X)|,
 \qquad d(X)=|X|-|N_{H_Q}(X)|.
\tag{0.3}
\]

Consequently \(V'\le R\) if and only if

\[
 |N_{K^+}(X)|-|N_{K^-}(X)|\ge d(X)-R
 \quad\hbox{for every }X\subseteq\mathcal T.
\tag{0.4}
\]

The equivalent operational statement is an alternating-linkage theorem.
If an old maximum partial compiler loses \(\ell\) matched cells in the
exchange and the new guarded graph contains \(\kappa\) vertex-disjoint
augmenting paths, then

\[
                         V'=V+\ell-\kappa.
\tag{0.5}
\]

Hence the desired recurrence

\[
                         V'\le \rho V+\beta
\tag{0.6}
\]

holds exactly when

\[
              \kappa\ge(1-\rho)V+\ell-\beta.
\tag{0.7}
\]

This identifies the lossless recursive state: the transported guard/host
signature together with the boundary gammoid or pairing-resolved linkage
relation.  The scalar \(V\) alone is a terminal potential, not a complete
composition state.

A bounded interior exchange gives only an additive Lipschitz bound.  It
cannot contract an unbounded \(V\) by a fixed factor.  A genuine
\(\rho<1\) theorem needs an extensive, commonly guarded augmentor bank
touching \(\Omega(V)\) independent matching resources, or a global reset.

The present K17 nonflat zipper does not yet define a live instance of
(0.1): it has 2392 replay defects, 3568 failed rows, and upper holes
1900/911/128 before common-cap Hall.  Its scalar slack 3293 has no compiler
consequence.

## 1. The upstream physical gate

Let \(Z\) be a proposed derivative chronology and let \(E(Z)\) be its
maximal envelope.  Fix all physical data used before the lower compiler:

1. the literal inverse/replay equations and nonempty letters;
2. the required residence threshold;
3. the declared protected upper and long-interval witnesses;
4. every socket choice, boundary letter, and prepin; and
5. the direct target occurrences which are to remain outside the short-cell
   compiler.

Call \(Z\) **upstream accepted** when all these tests pass.  Nothing below
is evaluated before that event.  Formally, put \(V_*(Z)=+\infty\), or leave
it undefined, when \(Z\) is not upstream accepted.

This ordering is essential.  Capping an envelope only removes coordinate
bits.  It cannot create a missing replay host or restore an absent upper
interval.  Hall in a graph built before replay therefore proves nothing
about a physical word.

After upstream acceptance, let \(\mathcal T\) be the fixed family of target
parts assigned to the terminal compiler.  It is convenient under switches
to use a fixed target universe.  A target already served by a protected
direct or long occurrence receives a private unconditional service column.
A target which must be supplied by a short physical interval uses an actual
singleton/pair cell.  If direct-service status changes under a switch, the
corresponding private columns simply belong to \(K^-\) or \(K^+\) below.

Let \(G_Z=(\mathcal T,\mathcal C_Z;E_Z)\) be the sound marginal
target--cell graph after those choices.  A **guard word** is a nonempty
set word \(Q=(Q_p)\) satisfying

\[
 Q_p\subseteq E_p(Z)
 \quad\hbox{and}\quad
 \bigvee_{p\in I_i}Q_p=T_i
 \quad\hbox{for every fixed carrier row }(T_i,I_i).
\tag{1.1}
\]

Retain every unconditional service column and precisely the short-cell
incidences which \(Q\) realizes:

\[
 H_Q=\left\{(S,C)\in G_Z:
               \bigvee_{p\in C}Q_p=S\right\}
       \cup\{\hbox{unconditional service incidences}\}.
\tag{1.2}
\]

Every matching in \(H_Q\) is simultaneously literal: the same word \(Q\)
realizes all selected short cells and all fixed carrier rows.  Thus \(H_Q\)
is a Cartesian, common-cap-safe graph, not merely a marginal candidate
graph.

## 2. The exact defect

For a guard \(Q\), define

\[
 V_Q(Z)=|\mathcal T|-\nu(H_Q).
\tag{2.1}
\]

Hall deficiency gives the equivalent formula

\[
 V_Q(Z)=\max_{X\subseteq\mathcal T}
              \bigl(|X|-|N_{H_Q}(X)|\bigr).
\tag{2.2}
\]

The empty cut makes the maximum nonnegative.  If \(\sigma_G(X)\) is the
marginal surplus and \(\lambda_Q(X)\) is the neighborhood deleted by guard
pruning,

\[
 \sigma_G(X)=|N_{G_Z}(X)|-|X|,
 \qquad
 \lambda_Q(X)=|N_{G_Z}(X)\setminus N_{H_Q}(X)|,
\]

then

\[
 V_Q(Z)=\max_X\bigl(\lambda_Q(X)-\sigma_G(X)\bigr).
\tag{2.3}
\]

Finally put

\[
                         V_*(Z)=\min_Q V_Q(Z).
\tag{2.4}
\]

### Theorem 2.1 (minimum omitted-target theorem)

\(V_*(Z)\) is exactly the minimum number of target parts which must be
omitted by a literal partial common-cap compiler on the accepted scaffold
\(Z\).  In particular,

\[
 V_*(Z)=0
 \quad\Longleftrightarrow\quad
 Z\hbox{ has an exact common-cap compiler}.
\tag{2.5}
\]

#### Proof

For a fixed \(Q\), take a maximum matching in \(H_Q\).  The word \(Q\)
realizes all its selected physical cells simultaneously, so it serves
exactly \(\nu(H_Q)\) distinct target parts and omits \(V_Q\).

Conversely, a literal partial compiler supplies its own physical cap word
\(Q\).  Every selected target--cell incidence belongs to \(H_Q\), and the
selected cells are distinct, so those incidences form a matching in
\(H_Q\).  Its number of omitted target parts is at least \(V_Q\), hence at
least \(V_*\).  Taking the minimum over literal partial compilers proves the
claim.  \(\square\)

### Corollary 2.2 (weakest deficient-Hall condition)

For an integer \(d\ge0\), a partial literal compiler omitting at most \(d\)
target parts exists if and only if some guard word \(Q\) satisfies

\[
 |N_{H_Q}(X)|\ge |X|-d
 \qquad(X\subseteq\mathcal T).
\tag{2.6}
\]

Thus (2.6), existentially over literal guards, is the weakest Hall
condition for a \(d\)-defect common cap.  Positive scalar cell surplus,
minimum degree, bounded conflict rank, and ordinary Hall in \(G_Z\) are all
strictly weaker and are not substitutes.

### Corollary 2.3 (terminal completion)

If the accepted scaffold has length \(B(k)+c\), appending the \(V_*(Z)\)
omitted target masks as singleton letters gives

\[
                         \nu(k)\le B(k)+c+V_*(Z),
\tag{2.7}
\]

provided all targets outside \(\mathcal T\) were already certified
upstream.

## 3. Exact transport across an interior exchange

Let an interior exchange carry an upstream-accepted \(Z\) to another
upstream-accepted \(Z'\).  This hypothesis includes the signed-fragment run
and upper-provider monoid tests; it is not inferred from Hall.  Fix a guard
transition \(Q\to Q'\) which agrees under the natural translation/reflection
on every retained fragment interior.

First use the fixed target-universe convention of Section 1.  After
identifying transported physical cells, decompose

\[
 H_Q=H_0\mathbin{\dot\cup}K^- ,
 \qquad
 H_{Q'}=H_0\mathbin{\dot\cup}K^+ ,
\tag{3.1}
\]

where the dot denotes disjoint right-vertex banks.  Thus \(H_0\) is the
exact transported guarded graph and \(K^\pm\) contain every nontransported
old/new cell or private service column.

For \(X\subseteq\mathcal T\), write

\[
 d_Q(X)=|X|-|N_{H_Q}(X)|.
\tag{3.2}
\]

### Theorem 3.1 (exact cut transport)

For every target cut \(X\),

\[
 d_{Q'}(X)=d_Q(X)
       +|N_{K^-}(X)|-|N_{K^+}(X)|.
\tag{3.3}
\]

Consequently, for every real \(R\ge0\),

\[
 V_{Q'}(Z')\le R
\tag{3.4}
\]

if and only if

\[
 |N_{K^+}(X)|-|N_{K^-}(X)|
       \ge d_Q(X)-R
 \qquad(X\subseteq\mathcal T).
\tag{3.5}
\]

#### Proof

The right banks in (3.1) are disjoint, so

\[
 |N_{H_Q}(X)|=|N_{H_0}(X)|+|N_{K^-}(X)|
\]

and the analogous identity holds with \(Q',K^+\).  Subtraction gives
(3.3).  Taking the maximum over \(X\) and applying (2.2) gives
(3.4)--(3.5).  \(\square\)

Taking \(R=\rho V_Q+\beta\) in (3.5) is the exact cutwise regenerative
condition for this specified guard transition.  If the declared successor
relation permits an old optimal guard and a new guard to be chosen jointly,
existence of such a transition proves

\[
                         V_*(Z')\le\rho V_*(Z)+\beta.
\tag{3.6}
\]

Without that guard-connectivity hypothesis, the numerical inequality
(3.6) need not provide a transported recursive certificate: its two
minimizing guards may lie in different transition components.

If one works directly with changing residual target sets instead of private
service columns, every newly residual target is an additional exposed
source below.  A safe coarse bound simply adds their number to the old
defect.  The fixed-universe convention is exact and avoids that extra
notation.

## 4. The alternating-linkage form

Let \(M\) be a maximum matching in \(H_Q\), so \(M\) leaves \(V_Q\) target
parts exposed.  Transport its stable edges through the switch and delete
the \(\ell\) matched incidences whose right cells lie in \(K^-\).  The result
is a matching \(M_0\subseteq H_{Q'}\) with

\[
       |\mathcal T|-|M_0|=V_Q+\ell.
\tag{4.1}
\]

Orient every nonmatching edge of \(H_{Q'}\) from target to cell and every
edge of \(M_0\) from cell to target.  Let \(\kappa\) be the maximum number
of vertex-disjoint directed paths from exposed targets to exposed cells.

### Theorem 4.1 (exact regenerative linkage)

\[
                         V_{Q'}=V_Q+\ell-\kappa.
\tag{4.2}
\]

In particular,

\[
 V_{Q'}\le\rho V_Q+\beta
 \quad\Longleftrightarrow\quad
 \kappa\ge(1-\rho)V_Q+\ell-\beta.
\tag{4.3}
\]

#### Proof

The directed paths are precisely vertex-disjoint \(M_0\)-augmenting paths.
Their maximum number is \(\nu(H_{Q'})-|M_0|\), by the symmetric-difference
decomposition of \(M_0\) with a maximum matching.  Therefore

\[
 V_{Q'}=|\mathcal T|-\nu(H_{Q'})
       =|\mathcal T|-|M_0|-\kappa,
\]

and (4.1) proves (4.2).  Rearrangement gives (4.3).  \(\square\)

The cut form (3.5) and linkage form (4.3) are max-flow/min-cut duals.  A
recursive block must export enough of this relation to answer every subset
of boundary sources which a later block may expose.  With a fixed sink
bank this is the boundary gammoid rank function

\[
 r(A)=\max\{\hbox{vertex-disjoint alternating paths from }A
                  \hbox{ to free cells}\}.
\tag{4.4}
\]

If the sink bank also varies, the lossless state is the pairing-resolved
source--sink linkage relation.  Together with the literal guard/host
signature, this is an exact stable state of bounded width.  The paths may
be globally long; bounded boundary width does not imply locality.

## 5. A finite boundary-pressure table

The cut condition can be compressed when only a bounded cell bank is new.
Let \(H_0\) be the transported exterior guarded graph and let \(L\) be the
new local graph on a right-cell set \(C\) disjoint from \(H_0\).  Assume
that \(H_0\cup L\) is realized by one guard word.  Equivalently, if one uses
the obstruction-clutter formulation, all cross-halo unary/pair/triple
guards must already have passed.

For \(Y\subseteq C\), define

\[
 \Pi_L(Y)=
 \max_{\substack{X\subseteq\mathcal T\\N_L(X)=Y}}
       \bigl(|X|-|N_{H_0}(X)|\bigr),
\tag{5.1}
\]

with the maximum over an empty family equal to \(-\infty\).

### Theorem 5.1 (lossless boundary pressure)

\[
 \operatorname{def}(H_0\cup L)
 =\max_{Y\subseteq C}\bigl(\Pi_L(Y)-|Y|\bigr).
\tag{5.2}
\]

Hence \(\operatorname{def}(H_0\cup L)\le R\) if and only if

\[
                         \Pi_L(Y)\le |Y|+R
 \qquad(Y\subseteq C).
\tag{5.3}
\]

#### Proof

For each \(X\), the exterior and local right banks are disjoint, so

\[
 |X|-|N_{H_0\cup L}(X)|
 =|X|-|N_{H_0}(X)|-|N_L(X)|.
\]

Group target cuts by the value \(Y=N_L(X)\), maximize first inside each
group, and then over \(Y\subseteq C\).  This is (5.2), and (5.3) follows.
\(\square\)

The \(2^{|C|}\)-entry pressure table is an exact finite cutwise criterion,
not a scalar capacity estimate.  Its entries still depend on global
exterior neighborhoods.  Under recursive composition they are supplied by
the boundary linkage state of Section 4.

## 6. What bounded switch support does and does not prove

Suppose a depth-two interior exchange changes \(s\) derivative rows and an
old guard attaining \(V_*\) has an accepted transported guard on the new
side.  Let

\[
                         J=I+\{0,1,2\}
\tag{6.1}
\]

be the affected envelope positions in the chosen indexing convention.
Every singleton or adjacent-pair cell meeting \(J\) is exceptional.  The
union generated by one changed row contains at most three singleton and
four adjacent-pair cells, so subadditivity gives at most \(7s\) such cells.
If \(b\) old cut-crossing cells do not transport into this bank, then

\[
                         c_\sigma\le7s+b.
\tag{6.2}
\]

If residual target sets rather than private service columns are used, at
most \(q_\sigma\le s\) newly residual direct colours must also be exposed.
Transporting an old optimum and doing no augmentation gives

\[
 V'_*\le V_*+c_\sigma+q_\sigma.
\tag{6.3}
\]

When the inverse transition transports every admissible new guard back to
the old face, it gives the corresponding reverse inequality.  Under the
standard \(t\)-cut convention \(s\le2t\), \(b\le t\), the safe coarse
one-way bound is

\[
                         V'_*\le V_*+17t.
\tag{6.4}
\]

The exact \(c_\sigma+q_\sigma\) value, not 17t, is authoritative.

### Corollary 6.1 (bounded-local contraction obstruction)

Fix a reversible guard-transition face as in (3.1), suppose every admissible
new guard lies in that face, and retag every new or neighborhood-changed
right column into \(K^+\), with \(|K^+|\le h\).  Then

\[
                         V'_*\ge V_*-h.
\tag{6.5}
\]

Therefore a recurrence \(V'_*\le\rho V_*+\beta\), with fixed
\(\rho<1\), requires

\[
                         h\ge(1-\rho)V_*-\beta.
\tag{6.6}
\]

In particular, one bounded-support switch cannot contract an unbounded
compiler defect by a dimension-independent factor.

#### Proof

Adding one right vertex increases matching rank by at most one.  Deleting
old cells can only worsen the new deficiency.  Hence \(h\) new cells reduce
deficiency by at most \(h\), proving (6.5); combine it with the asserted
upper recurrence to obtain (6.6).  \(\square\)

This closes the purely local contraction architecture.  It does not close
an extensive packet bank: a parallel batch with \(\Omega(V_*)\) independent
new matching resources may satisfy (4.3).

## 7. Two useful reset certificates

### 7.1 A guarded augmentor bank

Start from a maximum partial compiler with \(V\) exposed targets.  Suppose
a commonly guarded, pairwise-orthogonal bank of net-unit augmentors is
available.  Join an exposed target to an augmentor when the latter supplies
one cap-safe alternating path for that target, and suppose simultaneous
selection along a matching gives vertex-disjoint augmenting paths.

If, for absolute constants \(\eta>0,\beta\ge0\),

\[
 |N_{\mathcal A}(X)|\ge\eta|X|-\beta
 \qquad(X\subseteq U),
\tag{7.1}
\]

then deficient Hall gives a matching of size at least
\(\eta V-\beta\).  Applying its augmentors in parallel yields

\[
                         V'\le(1-\eta)V+\beta.
\tag{7.2}
\]

Thus \(\rho=1-\eta\).  This is a concrete sufficient Boolean/Pascal target:
the hard part is the common guard and orthogonality, not the algebra.

### 7.2 Fractional retention with margin

Let a marginal guarded bank carry fractional matching weights with target
mass one and cell load at most \(1-\varepsilon\).  After a physical switch
and guard pruning, suppose all but an exceptional target set \(O\),
\(|O|\le\beta\), retain incident mass at least \(1-\eta\), where
\(\eta\le\varepsilon\).

For every nonexceptional target \(S\), divide its retained weights by its
retained mass.  Cell load becomes at most

\[
                    \frac{1-\varepsilon}{1-\eta}\le1.
\]

This is a fractional matching saturating \(\mathcal T\setminus O\).
Integrality of the bipartite matching polytope gives an integral guarded
matching saturating those targets, hence

\[
                              V'_*\le\beta.
\tag{7.3}
\]

This is the reset case \(\rho=0\).  It is a normalized candidate-pressure
criterion, not total slack.  An orbit flow, quotient matching, or a
matching-first nibble may prove its hypotheses.  Generic independent-target
LLL does not: bounded blocker rank alone neither bounds dependency nor
removes the known collision tax.

## 8. The universal-safe obstruction profile

Sometimes one wants to run an ordinary matching algorithm without fixing a
whole guard word first.  After sockets are frozen, let \(G\) be the marginal
candidate graph and let \(\mathfrak F\) be the exact family of
matching-compatible minimal common-cap blockers.  In the fixed depth-two
architecture these have rank at most three.  For \(F\in\mathfrak F\), force
the candidates in \(F\), delete their target and cell endpoints, and call
the residual ordinary graph \(G_F\).  Put

\[
 \delta_F=(|\mathcal T|-|F|)-\nu(G_F),
 \qquad
 \delta_\varnothing=|\mathcal T|-\nu(G).
\tag{8.1}
\]

### Theorem 8.1 (weakest arbitrary-matching safety test)

For an integer \(d\ge0\), the following are equivalent:

1. an ordinary matching omitting at most \(d\) targets exists, and every
   such matching is common-cap safe;
2.
   \[
   \delta_\varnothing\le d,
   \qquad
   \delta_F\ge d+1\quad(F\in\mathfrak F).
   \tag{8.2}
   \]

#### Proof

\(\delta_F\) is exactly the minimum number of unmatched targets among
ordinary matchings containing \(F\).  Therefore an unsafe matching with at
most \(d\) omissions exists exactly when some minimal blocker \(F\) has
\(\delta_F\le d\).  The first inequality in (8.2) is exactly existence of an
ordinary matching with at most \(d\) omissions.  \(\square\)

This is not weaker than (2.6): it guarantees safety of **every** sufficiently
large ordinary matching, whereas (2.6) asks only for one guarded matching.
It is useful because every \(\delta_F\) has a proof-producing deficient-Hall
cut.

If an exchange changes at most \(h\) right columns, then for every blocker
persisting on both sides

\[
 |\delta'_F-\delta_F|\le h.
\tag{8.3}
\]

Thus, writing \(v=\delta_\varnothing\) and
\(\mu=\min_F\delta_F\), the margin

\[
                         \mu-v\ge2h+1
\tag{8.4}
\]

survives one exchange after all newly created halo blockers are checked.
This is a robust sufficient window, not a replacement for the exact
linkage state.

## 9. Constant-additive consequence

Consider one compatible odd/even regenerative spine whose accepted physical
scaffolds have base length \(B(k)\).  Suppose that after every completed
physical transition there is a guard transition satisfying

\[
                         V_{n+1}\le\rho V_n+\beta,
 \qquad 0\le\rho<1,
\tag{9.1}
\]

with constants independent of dimension.  Put

\[
 E=\max\left\{V_0,\frac{\beta}{1-\rho}\right\}.
\tag{9.2}
\]

Then \(V_n\le E\) for all \(n\).  Corollary 2.3 gives

\[
                         \boxed{\nu(k)\le B(k)+\lceil E\rceil}.
\tag{9.3}
\]

If the scaffold itself has bounded excess \(c\), or there are separately
declared bounded terminal middle/upper charges, add those once to the right
side.  They are not carried into the next stage unless the recursive state
explicitly exports them.  This is the compiler-row specialization of the
bounded-defect regenerative-spine theorem.

For \(\beta=0\), integrality and \(\rho<1\) force eventual \(V_n=0\).  Exact
equality still requires all other physical and terminal charges to vanish.

## 10. Sharp remaining theorem

The exact missing common-cap statement is now the following.

> **Guarded bulk-regeneration lemma.**  After a Boolean/Pascal physical
> rethread has passed replay, residence, protected upper shadows, sockets,
> and prepins, its interior switch packet admits one transported guard and
> an augmentor bank satisfying either the cut condition (3.5), the linkage
> condition (4.3), or the pressure table (5.3), with uniform
> \(\rho<1,\beta=O(1)\).

The guarded switch monoids prove exact physical transport and bound the
exceptional halo.  They do not prove this augmenting supply.  Conversely,
an abstract matching expansion theorem applied before replay or without a
common guard is outside the hypothesis.

For the authenticated K17 OPTIMAL28 zipper, the theorem cannot yet be
tested: physical replay and ranks 10--12 fail upstream.  A successful
complement rethread must first pass those rows.  Only its final literal
chronology may be converted into \(H_Q\), \(V_*\), and the boundary linkage
state.

## 11. Relation to the existing reductions

This note supplies the previously opaque compiler coordinate in
MATH_THEOREM_REGENERATIVE_GUARDED_SWITCH_CONTRACTION_AND_CONSTANT_ADDITIVE_20260731.md:
its exact value is \(d_{\rm cap}=V_*\).  The affine bounded-spine implication
itself is already proved in
MATH_THEOREM_BOUNDED_DEFECT_REGENERATIVE_SPINE_AND_EXPLICIT_O1_CONSTANT_20260731.md.

The five-row physical transport used here is the one proved in
MATH_THEOREM_K17_TWO_BANK_SWITCH_MONOIDS_AND_GUARDED_REPAIR_HALL_20260731.md.
The fixed-guard deficient-Hall identity refines
MATH_THEOREM_R_COMMON_CAP_GUARD_PRUNING_ROBUST_HALL_LIFT_20260731.md.
The lossless recursive linkage state is the compiler specialization of
MATH_THEOREM_CATALAN_BOUNDARY_LINKAGE_GAMMOID_STATE_20260731.md.
No new physical switch or K17 carrier is asserted.
