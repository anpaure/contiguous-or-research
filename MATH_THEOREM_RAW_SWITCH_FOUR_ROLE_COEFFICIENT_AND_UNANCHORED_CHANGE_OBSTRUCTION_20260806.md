# Raw switch four-role coefficient and the first-kill collapse

> **UNVERIFIED CANDIDATE -- DO NOT CITE AS A THEOREM.**  This draft assumes
> that the stopped covariance candidate carries an independent factor
> `a_C/X`.  The parent notation also admits the materially different
> interpretation in which the switched object is the composite
> `A=(Q,E,F)` and its whole coefficient is `mu_A=c_iR_i`.  Until the literal
> formula for `B_(T,i)` is expanded, Sections 2--6 do not establish the
> claimed normalization.  The proof-safe coefficient identity and exact
> remaining gate are recorded in
> `MATH_THEOREM_RAW_COMPOSITE_SWITCH_COEFFICIENT_IDENTITY_AND_FULL_CHANGE_GATE_20260806.md`.

**Date:** 2026-08-06  
**Method:** exact one-step rate symmetrization, earliest-boundary coarea,
future-fugacity domination, and a full changed-resource polarization; no
computation or search  
**Status:** candidate proof of the raw switch-coefficient row, pending an
independent audit of the final normalization.  Unlike the retracted first
draft, it separates the four roles and retains every changed resource.

This note continues
`MATH_THEOREM_ADAPTIVE_JOHNSON_BELLMAN_VALUE_AND_EQUIVARIANT_HIDING_OBSTRUCTION_20260806.md`.
Its purpose is only the raw selected-relation estimate; no
separator-cylinder `h`-transform is used.

## 1. The four roles

Four logically different objects occur in one stopped switch term.

1. `C,tau C` are the coordinate-transposed **covariance candidates**.
2. `E,F` are the two host edges obtained when the actual root/profile
   vector is squared.  They carry a common root `Q` and coefficient
   `c_i(Q,E,F)` from `(FP2)`.
3. `G` is the accepted edge which first makes exactly one of `C,tau C`
   unavailable.

No identification among `C,E,F,G` is made.

Let `A_i` be the available candidate set.  At a transition at which

\[
 C\in A_i,\quad \tau C\in A_i,\quad
 C\cap G=\varnothing,\quad \tau C\cap G\ne\varnothing,
\tag{1.1}
\]

the oriented switch boundary is born with survivor `C` and killed mate
`tau C`.  The earliest-blocker partition proves that every oriented switch
pair has at most one such birth.

Every switch form below carries the uniform-transposition normalization

\[
                  \kappa_k={1\over {k\choose2}}.
\tag{1.1a}
\]

This factor is essential: one killed candidate can be the mate of many
switch pairs, but averaging over `tau` gives total multiplicity one.

The coordinate orbit gives, while both candidates are live,

\[
 \boxed{
 \omega_C=\omega_{\tau C},\qquad
 a_C(i)=a_{\tau C}(i).}
\tag{1.2}
\]

If the whole covariance term is conjugated, its root is transported from
`Q` to `tau Q`; we never assume `tau Q=Q`.  In the actual-vector expansion
below, the two endpoint shores are instead bounded separately and the sum
already ranges over every literal `Q,E,F`.  Thus no stopped-state
equivariance of a fixed root is used.

## 2. Exact bare-to-future coefficient comparison

For the square pair `E,F`, let

\[
 \widetilde c_i^+(Q,E,F)=\xi_{E,i}^+\xi_{F,i}^+
\tag{2.1}
\]

be the bare product after deterministic rescaling, with both edges
hypothetically retained.  By `(FP6)`, the corresponding next
future-fugacity coefficient is

\[
 c_i^+(Q,E,F)=c_i(Q,E,F)R_i(E,F;Q).
\tag{2.2}
\]

Since every remaining future-density ratio is at least one,

\[
 \boxed{\widetilde c_i^+(Q,E,F)\le c_i(Q,E,F)R_i(E,F;Q).}
\tag{2.3}
\]

The covariance-candidate coefficient immediately after a transition by
`G`, under the hypothetical survival of `C`, is

\[
                    \gamma_i^+(C;G)={a_C^+(i;G)\over X^+(i;G)}.
\tag{2.4}
\]

Put `gamma_i(C)=a_C(i)/X(i)`.  The one-step rate reconstruction retained in
the parent drift formulas gives, uniformly over a legal `G` and
`p>=c/d`,

\[
             \gamma_i^+(C;G)\le(1+o(1))\gamma_i(C).
\tag{2.4a}
\]

The same estimate holds for `tau C`; when both are hypothetically retained,
their two post-transition coefficients are equal.

Thus the true expected bare coefficient of a boundary term born through
`G` is at most

\[
 \kappa_k {a_G(i)\over X(i)}\,\gamma_i^+(C;G)\,
 c_i(Q,E,F)R_i(E,F;Q).
\tag{2.5}
\]

This is the only use of future fugacity in the comparison.  It dominates
the actual post-rescaling square coefficient, rather than an arbitrary
cylinder survival martingale.

## 3. Sum out the actual blocker, not the killed mate

Fix the pre-transition state, `C,tau`, and the future pair `Q,E,F`.  Sum
(2.5) over the possible accepted edges `G` which produce this boundary
birth.  Since these are a subset of all available transitions,

\[
 \sum_{G:\,(1.1)}{a_G(i)\over X(i)}\le1.
\tag{3.1}
\]

By (1.2), (2.4a), and (3.1),

\[
 \boxed{
 \kappa_k\sum_\tau\sum_{G:\,(1.1)}
 {a_G(i)\over X(i)}\gamma_i^+(C;G)c_iR_i
 \le (1+o(1))\kappa_k\sum_\tau\gamma_i(C)c_iR_i.}
\tag{3.2}
\]

This is the four-to-three collapse.  The actual earliest blocker `G`
disappears.  On the `C` endpoint shore, `C` becomes the third edge in the
static first-entry ledger.  On the opposite shore, use (1.2) to replace
its coefficient by that of `tau C`, which becomes the third edge there.
For a fixed third edge, summing `kappa_k` over the transpositions gives
one.  Since a switch boundary is born only once, summing (3.2) over birth
times is bounded by the all-time third-edge ledger; no occupation factor is
introduced.

Equivalently, the elementary symmetric product

\[
 {a_Ga_C\over X^2}={a_Ca_G\over X^2}
\tag{3.3}
\]

allows the relation to be oriented toward its killed covariance candidate.
This is valid only in the raw law.  It would not survive an arbitrary
terminal-event `h`-transform.

## 4. Retain the full changed-resource set

For a fixed resource type `T`, let `W_T(C)` be the multiset of its
occurrences in the candidate word.  Put

\[
 \mathscr D_T(C,\tau)=
 \{(y,\tau y):y\in W_T(C),\ \tau y\ne y\}.
\tag{4.1}
\]

This is the full changed set.  It has size `O(d)`.  Only a subset of its
`tau C` endpoints is met by the actual blocker `G`, but no other changed
occurrence is discarded.

For the current profile `f`, covariance of the template gives

\[
 K_Cf-K_{\tau C}f
   =\sum_{(y,x)\in\mathscr D_T(C,\tau)}
          \epsilon_{y,x}(f_y-f_x),
\tag{4.2}
\]

with fixed signs/multiplicities determined by the occurrence roles.  Every
`(y,x)` is a Johnson edge.  The full resolvent energy expands as

\[
 \begin{aligned}
 \|K_Cf-K_{\tau C}f\|_R^2
 ={}&\sum_{e\in\mathscr D}\|z_e\|_R^2\\
 &+2\sum_{\{e,e'\}\subseteq\mathscr D}
                   \langle z_e,Rz_{e'}\rangle .
 \end{aligned}
\tag{4.3}
\]

There is no replacement of `mathscr D` by the blocker-hit subset.

The oriented covariance boundary itself is a difference of two equal-
coefficient squares.  For every positive-semidefinite `R`,

\[
 [\|u\|_R^2-\|v\|_R^2]_+
 \le \|v\|_R^2+2\|u-v\|_R^2.
\tag{4.4}
\]

The killed-mate diagonal pays the first term.  The second term is (4.3).
By the exact Johnson-switch resistance identity, each diagonal summand in
(4.3) loses the inverse-gap factor.

## 5. Why every changed occurrence is visible to a third-edge ledger

Split (4.2) according to its two endpoint shores:

\[
 K_Cf-K_{\tau C}f=Z_C-Z_{\tau C},
\tag{5.1}
\]

where every literal occurrence in `Z_C` belongs to `C`, and every literal
occurrence in `Z_(tau C)` belongs to `tau C`.  Then

\[
 \boxed{
 \|Z_C-Z_{\tau C}\|_R^2
 \le2\|Z_C\|_R^2+2\|Z_{\tau C}\|_R^2.}
\tag{5.2}
\]

This two-shore split prevents a false `O(d)` loss from cross-side pairs.
It retains the full changed set, but does not require one third edge to
contain both endpoints of a changed Johnson edge.

After expanding the actual profile square, an occurrence contributes only
when it lies in `E union F`.  For `H in {C,tau C}`, put

\[
 j_T(H;E,F)=|W_T(H)\cap(E\cup F)|
\tag{5.3}
\]

with literal occurrence multiplicities, and let `j` be the sum over the
non-slot types.  On the `H` shore, the number of contributing diagonal
terms is at most `j`, and the number of correlated pairs is at most
`binom(j,2)`.

After (3.2), `H` is exactly the third edge on its own shore.  Therefore:

* the diagonal, one-entry terms are the rooted-overlap first-entry tuples
  with third edge `H`; they are contained in the `(ROc)` enumeration;
* the correlated terms are indexed by an unordered pair of distinct
  resources in `H cap(E union F)`, and hence inject into the summands of
  `(FE3.3)` with third edge `H`.

This retains all unhit changed occurrences.  The actual blocker is
irrelevant after (3.2).  In particular,

\[
 {\#\{\text{contributing occurrences on shore }H\}\choose2}
 \le {j(H;E,F)\choose2}.
\tag{5.4}
\]

The first-entry coefficient uses (2.3); its complete-host sum is the
rooted overlap polynomial.  Quantitatively `(ROc)` gives
`C/(pd^2)`, so the literal occurrence sum remains inside its proved rooted
normalization at `p>=c/d`.  For the correlated part, the time/density
summation of the third-edge coefficient is bounded, using the already
proved global-rate reconstruction, by

\[
 \omega_E\omega_F\omega_H
 p_*^{-m(E,F;Q)}
 {j(H;E,F)\choose2}K_{p_*}(j),
\tag{5.5}
\]

which is the corresponding `(FE3.3)` summand.  Proposition `(FE3)` has the
needed spare factor `1/d`.  Slot-only changed entries remain in the
separate slot ledger.

The same argument is root-covariant for a marked cluster: transport its
root by `tau`, apply the size-two/three rooted normalization, and use the
marked first-two-hit theorem (7.3).

## 6. Raw consequence

The preceding calculation closes the missing **raw coefficient** row:

1. the actual blocker is summed out by (3.1);
2. equal live coefficients replace the survivor by the killed mate;
3. future fugacity dominates the bare post-rescaling `E,F` coefficient;
4. each endpoint candidate is the third edge for the changed occurrences
   on its own shore, with the `kappa_k` average removing transposition
   multiplicity;
5. one-entry and correlated terms are respectively subsets of `(ROc)` and
   `(FE3)`.

Consequently the one-sided raw Bellman transfer has initial/injection scale

\[
                         O(M/d^4),
\tag{6.1}
\]

and the stopped chain in the parent notes yields

\[
 \boxed{\mathbb E(B_0+B_1)=O(M/d^2).}
\tag{6.2}
\]

Combined with the annealed quarantine--Haxell composition, this is the
stochastic bottom estimate needed by the current architecture.

## 7. Scope

This proof uses the raw transition probabilities in (3.1).  It does not
prove `(JCYL)` for a terminally tilted law.  It also does not prove the
separate terminal component-joining theorem, the PBBS payload bridge, or
the odd occurrence-labelled reservoir.

The normalization in (5.3), including the occurrence multiplicities of
the candidate covariance word, is the load-bearing row for independent
audit.  No conclusion in Section 6 should be cited if that row fails.
