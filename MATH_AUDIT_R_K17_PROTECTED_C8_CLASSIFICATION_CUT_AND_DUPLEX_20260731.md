# Adversarial audit: protected C8 classification, K17 release cut, and staggered duplex

Date: 2026-07-31  
Audited notes:

* `MATH_THEOREM_R_PROTECTED_C8_SPLICE_AND_K17_FOUR_INCIDENCE_FLOOR_20260731.md`;
* `MATH_THEOREM_R_K17_STAGE2_FOUR_INCIDENCE_CUT_DUAL_AND_DUPLEX_GATE_20260731.md`.

Status: the mathematical cores are valid.  Two scope phrases required
narrowing, and the staggered-duplex theorem required explicit endpoint
anchoring before it could be called a transport from a prescribed source to
a prescribed final factor.  Those corrections have been applied to the
current theorem files.  No correction yields a K17 equality proof.

## 1. C8 support classification: valid

Write the incidence C8 as

\[
 C_0-T_0-C_1-T_1-C_2-T_2-C_3-T_3-C_0,
 \qquad T_i=C_i\cup C_{i+1}.
\]

The opposite lower vertices have Johnson distance one or two.

* At distance one, a common-neighbour in the star clique repeats the same
  consecutive upper row and violates simplicity.  Both intermediate
  neighbours must therefore lie in the common top clique.  In lower-row
  notation this is exactly the note's star form
  \(C_i=S+a_i\).
* At distance two, the intermediate common neighbours select complementary
  choices from the two two-element differences; a noncomplementary choice
  repeats a consecutive union.  This is exactly the octahedral-square form
  \(C_i=S+a_i+a_{i+1}\).

The classification is complete.  Its names differ from the equivalent
upper-row classification (“Boolean square” and “top square”), but the set
systems are the same.

## 2. The three load-neutral forms: valid

In the star form the other selected owner is
\(R_i=S+a_i+x_i\).  Alternation excludes \(x_i=a_{i-1},a_{i+1}\), so
\(x_i\) is either the antipodal petal \(a_{i+2}\) or an exterior point.
For one exterior point \(e\), the old and new target indices differ by a
one-step cyclic shift.  Therefore the occurrence set
\(I_e=\{i:x_i=e\}\) must satisfy \(I_e=I_e-1\), whose only solutions are
empty and all four indices.  If no exterior occurs, every row is antipodal.
This gives exactly the two star forms in the note.

In the octahedral form both missing petals are the two circuit neighbours,
so every \(x_i\) is exterior.  The same shift argument forces one common
exterior in all four rows.  There is no fourth mixed form.

In the antipodal form

\[
                         R_i=R_{i+2}.
\]

Thus \(C_i-R_i-C_{i+2}\) is an old factor path, and the two corresponding
deleted incidences lie in one component.  The conclusion that a
load-neutral four-component-clean C8 must be common-exterior is valid.

## 3. Topology: valid with the stated cleanliness hypothesis

Deleting one selected incidence from each of \(\ell\) distinct factor
cycles gives \(\ell\) paths with endpoint pairs \((C_i,T_i)\).  The new
incidences \(T_iC_{i+1}\) concatenate them into one cycle.  Hence the
component change is exactly \(1-\ell\); a clean C8 changes it by \(-3\).

Without distinct old components, only the port-matching formula is exact:
pair the cut endpoints by their retained paths and compare its cycle count
after superposition with the old and new incidence pairings.  Neither note
uses the clean formula outside its hypothesis.

## 4. Witness reserve: correct only for one switch

A simple \(C_{2\ell}\) toggle deletes exactly \(\ell\) incidences.  If one
target has \(\ell+1\) pairwise incidence-edge-disjoint witness spans, each
deleted incidence can meet at most one member of that family, so at least one
span survives.  The `5` for C8 and `ell+1` in Corollary 4.3 are exact.

This is a **single-switch** reserve.  It must not be promoted to a sequence
of C8s or a C8/C6 bank unless either

1. the union of all future deleted incidences still has size below the
   reserve; or
2. a surviving occurrence is reselected after each switch and is protected
   from every later deletion.

PBBS all-depth support alone supplies neither condition.

## 5. Stage-2 release-cut signs: valid

Let \(K\) be the prescribed service-plus-protection bank and release one
edge \(e=(u,v)\).  For

\[
 \Delta_K(A,B)=a_K(A)-c_K(B)-e_{G\setminus K}(A,L\setminus B),
\]

the four endpoint cases give

\[
\begin{array}{c|c|c}
u\in A&v\in B&\Delta\text{ change}\\ \hline
1&1&0\\
1&0&0\\
0&1&-1\\
0&0&0.
\end{array}
\]

Thus only an incidence entering \(B\) from \(U\setminus A\) repairs the
cut, exactly as Lemma 2.2 states.

For the displayed K17 sets, an independent direct recount gives

\[
                  a_K(A)=4,\qquad c_K(B)=0,
             \qquad e_{G\setminus K}(A,L\setminus B)=2.
\]

The two available crossing incidences are

\[
       (109258,76490),\qquad(73379,72355).
\]

There are twenty protected incidences in
\(P\cap E(U\setminus A,B)\).  Every endpoint containing all fixed service
incidences must omit at least two members of this **twenty-edge set**.
The max-retention factor happens to omit

\[
                    (7847,7843),\qquad(109506,109250)
\]

from this set, plus two incidences outside it.  The cut does not prove that
these two named incidences are individually unavoidable.

### Applied wording correction

The original opening phrase “at least two specified entering incidences must
first be released” was too strong if “specified” meant a fixed pair or if “first” meant
a strict temporal order.  The exact statement is:

> By the first state which contains all 3,676 fixed service incidences, at
> least two incidences from the explicit twenty-edge set
> \(P\cap E(U\setminus A,B)\) must already be absent (they may be released
> earlier or simultaneously).

The current theorem note and later corollary use this correct setwise meaning.

## 6. Four-incidence floor: implication valid, dual scope correctly limited

The maximum-retention result reports an exact optimum of 13,596 among 13,600
optional protected incidences.  The supplied factor independently replays as
a balanced factor containing all 3,676 fixed service incidences and losing
four protected incidences.  The current artifact does not contain the
transportation dual multipliers, so the solver-free cut above proves only a
two-unit floor; the four-unit lower bound relies on the authenticated exact
`OPTIMAL` status.  Both notes state this limitation.

At an optimum \(H\), a move remaining in the fixed-service face which adds
\(a\) missing protected incidences and deletes \(b\) retained protected
incidences has final defect \(4-a+b\ge4\), hence \(b\ge a\).  This argument
is correct.

### Applied wording correction

The corresponding sentence in the C8 note's opening verdict now has the same
face qualifier.  A circuit starting at the optimum but allowed to delete a
fixed service incidence is not constrained by the 13,596 optimum.  It should
read:

> Every circuit move whose endpoint still contains all fixed service
> incidences and which installs \(a\) currently absent protected incidences
> must delete at least \(a\) other protected incidences.

The formal Theorem 6.1 also has the correct fixed-face scope.

## 7. Alternative service witnesses: valid at target level only

The four displayed strings for rows 814, 1024, 1325 and 1352 have rank nine,
successive Hamming distance two, and OR respectively

\[
                  15fb3,\quad17d1e,\quad1b7ae,\quad1bbc3.
\]

They occur consecutively in the reported largest component.  Therefore all
four affected service **targets** survive, and together with the 1,834
fully retained advertised spans all 1,838 service targets are covered.
This does not certify the four original occurrence identities, their
external residence collars, or any of the 6,499 unrelated old targets.  The
second note states these restrictions correctly.

## 8. Staggered duplex: bridge theorem valid; endpoint quantifiers need stating

For each stage \(i\), the local degree bounds plus all capacitated Hall cuts
are necessary and sufficient for a balanced bridge factor containing

\[
             S^i\cup\operatorname{supp}(Q^i)
                   \cup\operatorname{supp}(Q^{i+1}).
\]

These conditions are stagewise independent, so satisfying them for every
\(i\) produces all bridge factors.  Consecutive bridge factors share
\(\operatorname{supp}(Q^i)\); their symmetric difference therefore has an
alternating-circuit decomposition disjoint from that support.  The
make-before-break handoff argument is valid.

Two quantifiers must remain explicit.

1. The circuit ordering/residence condition is universal over **every
   intermediate toggle state**, including cyclic closing seams and the two
   bridge endpoints.  Existence of the bridge factors alone gives no such
   ordering.
2. The displayed theorem constructs the chain among
   \(F^0,\ldots,F^{m-1}\).  To obtain transport from a prescribed source
   \(F_{\rm src}\) and to a prescribed final factor \(F_{\rm dst}\), one
   must additionally require

   \[
      \operatorname{supp}(Q^0)\subseteq F_{\rm src}\cap F^0,
      \qquad
      \operatorname{supp}(Q^m)\subseteq F^{m-1}\cap F_{\rm dst},
   \]

   and residence-safe circuit orders for these two endpoint transitions (or
   identify the source/final factors with the first/last bridge factors).

The current statement is exact as a **bridge-factor existence theorem** and
now includes these endpoint clauses.  They must be invoked before citing it
as a complete transport from the frozen PBBS source to a required connected
endpoint.

For non-reversal-closed residence or directed compiler pins, each guard must
also carry its orientation state.  Mere undirected incidence support keeps
the OR witness but does not determine the directed collar.  The note's final
residence hypothesis can carry this information; it is not automatic from
the Hall cuts.

## 9. Final verdict

Valid without correction:

* both C8 geometries;
* the three load-neutral forms and exclusion of the antipodal clean merger;
* the \(1-\ell\) clean topology law;
* the single-switch \(\ell+1\) witness reserve;
* the release-cancellation sign and explicit deficit-two cut;
* the fixed-face four-debt inequality, at the authenticated optimum scope;
* the four alternative service intervals; and
* the stagewise Hall equivalence and common-guard circuit decomposition.

Corrections/guardrails:

* “two specified releases” means at least two from an explicit twenty-edge
  entering set, not one forced pair;
* debt monotonicity applies only while the endpoint remains in the fixed
  service face;
* the reserve count is not cumulative over a switch bank; and
* a full staggered transport needs source/final anchoring and residence-safe
  orders for every intermediate state.

These corrections leave the strategic conclusion unchanged: the frozen
Stage-2 occurrence section cannot be monotone-installed, while a
target-reselected, residence-safe staggered duplex remains open.
