# Separated lower-turn stars have a one-step full-port linkage

> **Superseded as the main cap route.**  The stronger theorem
> `MATH_THEOREM_BOUNDED_TURN_STARS_ONE_STEP_FULL_PORT_LINKAGE_20260804.md`
> removes pairwise source separation and handles arbitrary distinct turns
> for `p<=floor((m+2)/4)`.  The present theorem remains a correct sharper
> bound (`p<=floor(m/2)`) on the separated face.

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional Boolean-incidence theorem.  It constructs the raw
full owner-port linkage required by the near-full owner-gammoid wedge
theorem when the protected lower turns are pairwise nonadjacent.  It does
not prove that the current regenerative cap materializes the required
terminal occurrences or that its source turns can always be chosen with
this separation.

## 0. Setting

Fix `m>=3` and put

\[
 n=2m-1,
 \qquad \mathcal L=\binom{[n]}{m-1},
 \qquad \mathcal U=\binom{[n]}m,
 \qquad \mathcal V=\binom{[n]}{m+1}.
\]

Let

\[
 L_1,\ldots,L_p\in\mathcal L,
 \qquad 1\le p\le\lfloor m/2\rfloor,
\tag{0.1}
\]

and assume that the lower turns are pairwise nonadjacent in the Johnson
graph:

\[
 |L_i\setminus L_j|=|L_j\setminus L_i|\ge2
 \qquad(i\ne j).
\tag{0.2}
\]

For each source put

\[
 C_i=[n]\setminus L_i,
 \qquad |C_i|=m,
\]

and let its complete owner star be

\[
 P_i=\{L_i+a:a\in C_i\}\subseteq\mathcal U.
\tag{0.3}
\]

The candidate one-step terminal from owner `L_i+a` through a second
coordinate `b` is

\[
 V_i(a,b)=L_i\cup\{a,b\}\in\mathcal V.
\tag{0.4}
\]

Thus the candidate terminals at source `i` are naturally the edges of the
complete graph on vertex set `C_i`.

## 1. Two exact intersection facts

### Lemma 1.1 (owner stars are disjoint)

Under (0.2),

\[
 \boxed{P_i\cap P_j=\varnothing\qquad(i\ne j).}
\tag{1.1}
\]

#### Proof

If an owner `U` belonged to both stars, then

\[
 L_i\cup L_j\subseteq U,
 \qquad |U|=m.
\]

Writing `d=|L_i\setminus L_j|`, the union has rank `m-1+d`.  Hence
`d\le1`, contrary to (0.2).  \(\square\)

### Lemma 1.2 (two terminal clouds meet at most once)

For `i\ne j`, the two terminal families

\[
 \mathcal V_i=\{V\in\mathcal V:L_i\subset V\},
 \qquad
 \mathcal V_j=\{V\in\mathcal V:L_j\subset V\}
\]

have intersection of size at most one.

More precisely, with `d=|L_i\setminus L_j|`, the intersection is empty
for `d>2`, and for `d=2` it consists of the single terminal
`L_i\cup L_j`.

#### Proof

Any common terminal contains `L_i\cup L_j`, whose rank is `m-1+d`, while
the terminal rank is `m+1`.  Thus `d\le2`.  Assumption (0.2) leaves only
`d=2`, when the union itself already has rank `m+1` and is the unique
possible terminal.  \(\square\)

## 2. Full-port linkage theorem

### Theorem 2.1

There are injections

\[
 \phi_i:P_i\longrightarrow\mathcal V_i
 \qquad(1\le i\le p)
\tag{2.1}
\]

such that

1. `U\subset\phi_i(U)` for every `U\in P_i`;
2. all `pm` terminal values in the images of the `\phi_i` are distinct.

Consequently the rank-`m` to rank-`(m+1)` Boolean incidence graph contains
`pm` pairwise vertex-disjoint one-edge paths linking every owner in

\[
 P_0=P_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}P_p
\tag{2.2}
\]

to a distinct terminal.

#### Proof

Construct the maps in the order `i=1,\ldots,p`.  Suppose the earlier
terminal images have already been chosen and are globally distinct.

On vertex set `C_i`, identify an unordered pair `{a,b}` with the terminal
`V_i(a,b)`.  By Lemma 1.2, the entire terminal cloud of any one earlier
source intersects `\mathcal V_i` in at most one value.  Therefore at most
`i-1` edges of the complete graph `K_{C_i}` are forbidden by all earlier
terminal choices.

Delete those forbidden edges and call the residual graph `H_i`.  It has

\[
 \delta(H_i)\ge m-1-(i-1)=m-i\ge {m\over2},
\tag{2.3}
\]

because `i\le p\le\lfloor m/2\rfloor`.  By Dirac's theorem, `H_i` has a
Hamilton cycle.  Orient that cycle cyclically.  For every `a\in C_i`, let
`b(a)` be its successor and define

\[
 \phi_i(L_i+a)=L_i\cup\{a,b(a)\}.
\tag{2.4}
\]

Every selected terminal contains its owner.  The oriented Hamilton cycle
uses every cycle edge exactly once, so the `m` terminals selected for this
source are distinct.  They avoid every earlier selected terminal by the
definition of `H_i`.  This completes the induction.

Lemma 1.1 makes all starting owner ports distinct, while (2.1)--(2.4) make
all endpoints distinct.  The one-edge incidence paths therefore have
pairwise disjoint vertex sets.  \(\square\)

## 3. Gammoid consequence after priced deletions

Let `Gamma_0` be the strict gammoid on the owner-port set `P_0` whose sinks
are the terminal occurrences used in Theorem 2.1 and whose paths are the
displayed one-edge incidences.  Then

\[
 \boxed{r_{\Gamma_0}(P_0)=|P_0|=pm.}
\tag{3.1}
\]

Delete a physical capacity bank `F`, and let `h_F` be the number of these
pairwise disjoint paths meeting `F`.  In the residual typed-suffix gammoid
`Gamma_F`, deleting the hit paths and retaining all unhit ones gives

\[
 \boxed{
 |P_0|-r_{\Gamma_F}(P_0)\le h_F\le |F|.
 }
\tag{3.2}
\]

The final inequality uses vertex-disjointness: one deleted unit-capacity
vertex lies on at most one displayed path.

### Corollary 3.1 (near-full protected-wedge activation)

Assume additionally that:

1. the owner and terminal values above are materialized as distinct typed
   occurrences in one cap/guard/phase state;
2. all required source and prefix resources survive;
3. every displayed terminal is legal for its owner port; and
4. the deletion bank meets at most `m-p` displayed paths.

Then

\[
 |P_0|-r_{\Gamma_F}(P_0)\le m-p.
\]

For `p\le m-1`, the near-full owner-gammoid theorem therefore selects one
globally owner/q1-terminal-distinct protected wedge at each source and
routes all `p` claims in the same state.

This is a zero-defect conclusion.  The only cap-specific premise left in
this corollary is materialization and deletion pricing; the raw full-port
linkage itself is no longer an assumption.

## 4. Sharp scope

The separation hypothesis is used twice and cannot simply be omitted from
this proof:

* adjacent lower turns have a common owner, so their complete owner stars
  are not disjoint;
* adjacent terminal clouds can share `m-1` values rather than one, so the
  deleted-edge bound in (2.3) fails.

The restriction `p\le m/2` is sufficient, not claimed necessary.  It is
the exact range in which the crude global bound of `i-1` deleted edges
forces Dirac's minimum-degree condition.  The intended regenerative use
has bounded `p`, so this range holds for all sufficiently large `m`.

The theorem is a value-level Boolean-incidence construction.  It does not
assert that the current reference cap contains one physical occurrence of
every selected value, that all terminal types agree, or that the required
source turns can already be planted pairwise nonadjacently.  Those are the
remaining occurrence and regeneration rows.

## 5. Dependencies

The only external combinatorial input is Dirac's Hamilton-cycle theorem.
The gammoid corollary uses:

* `MATH_THEOREM_NEAR_FULL_OWNER_GAMMOID_PROTECTED_WEDGE_BYPASS_20260804.md`;
* `MATH_THEOREM_CAP_AWARE_PROTECTED_WEDGE_ACTIVATION_AND_EXACT_MENU_THRESHOLD_20260804.md`.
