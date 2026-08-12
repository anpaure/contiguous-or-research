# Audit of cap-aware protected-wedge activation and the exact menu threshold

**Date:** 2026-08-04  
**Method:** independent line-by-line pure-mathematical replay; no computation,
search, or solver  
**Audited theorem:** MATH_THEOREM_CAP_AWARE_PROTECTED_WEDGE_ACTIVATION_AND_EXACT_MENU_THRESHOLD_20260804.md  
**Audited SHA-256:** ae4ce45555394121fcf1e7df7840c86a0786b840dedcf96ca414ef9d33c7f188

## 0. Verdict

**GO at the theorem's stated conditional scope.**

The proof correctly establishes:

1. the exact cross-menu conflict profile: one coordinate star, one
   singleton, or the empty set;
2. the exact maximum

   \[
   B_q(m)={m\choose2}-{m-q\choose2}
   \]

   of candidates forbidden in one full wedge menu by a valid protected
   prefix of \(q\) wedges;
3. the active-menu packing threshold

   \[
   |W_i^c|>B_{p-1}(m);
   \]

4. pairwise nonconsecutiveness of the selected factor turns;
5. automatic private routing from one common-state active direct branch per
   selected wedge; and
6. the directed-support and \(L_0L_1\) sufficient conditions.

The note correctly does **not** claim that the current Pascal/common-cap
construction supplies these active menus or completion-stable branch
certificates.

## 1. Cross-menu conflict replay

Fix \(w=(L;\{a,b\})\), with owners \(L+a,L+b\) and terminal
\(Z=L+a+b\).  For another rank-\((m-1)\) turn \(L'\ne L\):

* \(L'\subset L+a\) iff \(L'=L-x+a\) for one \(x\in L\).  The wedges at
  \(L'\) using owner \(L+a\) are exactly the \(m-1\) pairs containing
  extension coordinate \(x\).
* The analogous condition for \(L+b\) is \(L'=L-x+b\).
* Those two owner conditions cannot hold simultaneously because the first
  \(L'\) contains \(a\notin L+b\), while the second contains
  \(b\notin L+a\).
* \(L'\subset Z\) iff \(L'\) is obtained by deleting two elements of \(Z\).
  Deleting \(a,b\) gives the excluded \(L\).  Deleting one of \(a,b\) and
  one old element gives an owner-star case, and the terminal pair already
  belongs to that star.  Deleting two old elements gives one terminal-only
  pair.

Therefore the exact alternatives in Lemma 1.1 are exhaustive and mutually
exclusive.  In particular, the previous \(2m-1\) bound was valid but loose;
the exact single-other-menu maximum is \(m-1\).

## 2. Union bound replay

At a fixed lower turn, identify wedges with edges of \(K_m\).  If \(t\) of
the \(q\) prior wedges induce coordinate stars, their union has at most

\[
 B_t(m)={m\choose2}-{m-t\choose2}
\]

edges.  The remaining \(q-t\) prior wedges add at most one edge each.  For
\(q\le m-1\),

\[
 B_{s+1}(m)-B_s(m)=m-s-1\ge1
\]

for \(s\le q-1\), hence

\[
 B_t(m)+(q-t)\le B_q(m).
\]

This proves the upper bound.

For sharpness, the theorem chooses

\[
 L_j=L_0-x_j+c_j,\qquad
 w_j=(L_j;\{x_j,e\}),
\]

with all \(x_j\) distinct inside \(L_0\), and all \(c_j,e\) distinct
outside it.  The requirements use \(q\) internal and \(q+1\) external
coordinates, both available exactly when \(q\le m-1\).  The owner lists

\[
 L_0+c_j,\qquad L_0-x_j+c_j+e
\]

and terminals \(L_0+c_j+e\) are pairwise distinct.  Thus the prefix is a
valid protected bank.  Its conflicts at \(L_0\) are the \(q\) distinct
stars at \(c_j\), whose union has exactly \(B_q(m)\) edges.

Hence \(B_q(m)\) is an attained one-step deletion maximum, not merely an
upper estimate.

## 3. Greedy threshold replay

After \(i-1\) selected wedges, at most \(B_{i-1}(m)\) candidates are
forbidden in the next active menu.  Therefore

\[
 |W_i^c|>B_{i-1}(m)
\]

leaves an active candidate.  The uniform floor

\[
 |W_i^c|>B_{p-1}(m)
\]

implies every sequential row because \(B_q(m)\) is increasing for
\(q\le m-1\).

Substituting \(q=p-1\) gives

\[
 B_{p-1}(m)
 ={m\choose2}-{m-p+1\choose2}
 ={(p-1)(2m-p)\over2}.
\]

The protected-factor edge budget \(2p+|P_*|\le m-2\) automatically places
the proof within \(p-1<m\), so no out-of-range use of the union formula
occurs in the intended application.

## 4. Factor and routing replay

The selected wedge bank has:

* distinct lower vertices;
* lower degree two;
* \(2p\) distinct upper owners, hence upper degree one inside the bank; and
* \(p\) distinct terminal values.

Together with the theorem's explicit degree-compatibility and edge-budget
premises, the small protected-factor theorem applies.

Two consecutive lower turns in an oriented factor share their intervening
upper owner.  Since no two selected wedges share an owner, selected turns
cannot be consecutive.  Thus they form an independent set in every factor
cycle.

After one active side is chosen at each selected turn, routes have distinct
sources, distinct selected owners, and distinct terminals.  Their arcs have
empty interiors, and the three occurrence layers are disjoint.  Hence the
routes are pairwise vertex-disjoint.  This is also exactly the independent-
turn special case of the previously proved monotone-side criterion.

The proof requires the explicit value-to-capacity injectivity and
completion-stability premises.  It does not infer them from Boolean value
distinctness alone.

## 5. Active-side support replay

Let \(e_i\) be the number of active directed branches and \(b_i\) the
number of unordered pairs carrying both directions.  Each singly oriented
pair contributes one to \(e_i\), each bidirected pair contributes two, and
each active unordered wedge contributes one.  Therefore

\[
 |W_i^c|=e_i-b_i\ge\lceil e_i/2\rceil.
\]

If \(L_{0,i}\) active owners each have at least \(L_{1,i}\) active direct
partners, then \(e_i\ge L_{0,i}L_{1,i}\).  Consequently

\[
 L_{0,i}L_{1,i}>2B_{p-1}(m)=(p-1)(2m-p)
\]

implies the active-menu threshold.  With \(L_{0,i}=m\), it is enough that

\[
 L_{1,i}>{(p-1)(2m-p)\over m}<2(p-1).
\]

No multiplication of counts from different cap states is used.

## 6. Gammoid separation replay

The common-owner example is valid.  For

\[
 L_i=U-x_i
\]

and active branches

\[
 L_i\to U\to U+b\qquad(b\notin U),
\]

every source has \(m-1\) active wedges, but every branch uses the same unit
owner \(U\).  Thus two claims cannot coexist.  At \(p=2\), this attains
exactly \(B_1(m)=m-1\), proving that strict inequality is necessary in the
cardinality-only one-step statement.

The example has suffix-gammoid rank one, so it does not refute a full Rado
cut theorem.  It proves the narrower and correct claim: individual branch
activity and large marginal wedge counts do not imply joint cap routing.

Conversely, gammoid rank measures linkability of already named ports and
does not count canonical partner incidences.  A rank-\(m\) port bank with
one direct typed terminal per port can contribute at most \(m\) active
wedges, which does not exceed \(B_{p-1}(m)\) once \(p\ge3\) and \(m\ge3\).
Therefore the menu theorem cannot be deduced from rank alone.

## 7. Scope exclusions confirmed

The theorem does not establish:

* existence of one cap state meeting the active-menu threshold;
* persistence of prospective branches through factor completion;
* a two-coordinate source/terminal product;
* Hamiltonization or upper decoration;
* residence, regeneration, or the terminal common compiler.

Its exact remaining premise is a common-state active-side support estimate,
preferably either

\[
 e_i-b_i>B_{p-1}(m)
\]

or

\[
 L_{0,i}L_{1,i}>(p-1)(2m-p).
\]

This is a strictly smaller target than the former demand that both diamond
degrees be \(\Theta(m)\).

## 8. Dependency hashes checked

| dependency | SHA-256 |
|---|---|
| protected wedge packing | 7727963a32eda4aad2b556ec0141dd02ca2c38e80daa563e97e36601cd3332fd |
| fixed-factor activation law | f190f4904a2c18a012e5dd3fd78eb97953b6ce9f8c68318452294f4961a1b794 |
| state-first Boolean diamond router | 19611e47ec7c121e6869f27930c1cbd9b74ddc3cfadaba9a6b50588d99ea30d1 |
| private regular-factor router | 2d64e2cb36b65706133ae1e68c6bdda80d433ccd428259860382a301538096d0 |
