# Second-shadow support is closed; long residence and protected rethreading are the real gate

**Date:** 2026-08-13  
**Status:** synthesis of unconditional all-parameter theorems; no claim of
the final `B(k)+O(1)` bound

## 0. Revised verdict

The canonical MSW wreath factor still misses a linear number of
second-shadow targets, so its cyclic orders do not solve the proposed
long-aperture deck.  Nevertheless, the abstract second-shadow **existence**
gate on odd ground is now closed by a different, explicit factor.

For `n=2r-1`, the standard Greene--Kleitman SCD and its set-complement
partner produce a spanning Johnson `2`-factor on rank `r` such that

* every rank-`r-1` intersection colour occurs exactly once;
* every rank-`r+1` union colour occurs between one and three times; and
* the factor has at most `Cat_(r-1)` components.

This factor is exactly the already audited centered PBBS factor in dual
coordinates.  Thus no new arithmetic or incidence theorem is needed for
immediate lower/upper support.  The remaining obstruction is chronological:
the factor has positive coordinate runs of length exactly three, so it has
no flat growing-aperture antecedent once `q>=4`.

The honest surviving target is therefore

\[
 \boxed{\text{PBBS all-width flag bank}
 \quad+\quad
 \text{protected `q`-safe rethreading}.}
\tag{0.1}
\]

## 1. Exact support factor

Put

\[
 \mathcal L={ [2r-1]\choose r-1},\quad
 \mathcal M={ [2r-1]\choose r},\quad
 \mathcal U={ [2r-1]\choose r+1}.
\]

For `L in \mathcal L`, let `a(L)` and `b(L)` be its rank-`r` successors
in the standard GK SCD and its set-complement SCD.  The theorem frozen in

```text
MATH_THEOREM_STANDARD_COMPLEMENT_SCD_IS_PBBS_BALANCED_SURJECTIVE_TWO_EXTENSION_20260813.md
```

identifies

\[
 \{a(L),b(L)\}=\{p(L)^c,p^{-1}(L)^c\},
\tag{1.1}
\]

where `p` is the PBBS permutation on `\mathcal L`.  Hence

\[
 a(L)\cap b(L)=L,
\qquad
 a(L)\cup b(L)=\bigl(p^{-1}(L)\cap p(L)\bigr)^c.
\tag{1.2}
\]

The PBBS angle theorem gives every rank-`r-2` angle between one and three
preimages.  Complementing proves every `U in \mathcal U` occurs between
one and three times in `(1.2)`.  The two endpoint maps are bijections, so
the owner graph is `2`-regular.  Its successor is conjugate to `p^{-2}`;
the PBBS orbit divisibility theorem gives at most `Cat_(r-1)` components.

This is an all-parameter integral statement.  It is stronger than the
needed support clause and eliminates an occurrence-lattice concern at the
three central ranks.

## 2. Why it does not finish the long-aperture theorem

Write the complement-centered PBBS owners as `X_t`, with step-two
successor.  Consecutive occurrences of one omitted label at PBBS gap
`g=2s+1` create a positive owner run of length `(g+1)/2`.  The exact PBBS
return census contains

\[
 (2r-1)(r-2)
\tag{2.1}
\]

gap-five returns (putting `m=r-1` in the established formula
`(2m+1)(m-1)`).  Therefore the owner chronology contains proper positive
runs of length exactly three.

A cyclic trace has a flat `q`-antecedent exactly when every proper positive
coordinate run has length at least `q`.  Thus this factor cannot be used
unchanged for any `q>=4`, in particular not for the target
`q=d+1 asymp sqrt(r)`.

This failure is invariant under rotation, reversal, and component
rephasing.  It is not cured by merely joining the components: a legal
fusion theorem must simultaneously remove every short return and avoid
creating new ones.

## 3. The all-width flag bank already exists

The residence failure must not be mistaken for a higher-shadow failure.
The PBBS all-depth fan theorem says that for every required width `w`, every
rank-`r+w` target has at least one designated union occurrence on the same
step-two owner factor.  For `w>=2`, the correct-rank multiplicity is bounded
between

\[
 1\quad\hbox{and}\quad {2w-1\choose w-1}.
\tag{3.1}
\]

Thus PBBS supplies an explicit occurrence-labelled all-width flag bank.
Some targets may have a unique designated occurrence, so arbitrary cutting
or switching is unsafe: it can delete the last witness.

## 4. Exact replacement theorem still needed

Let `q=d+1`.  A sufficient theorem is:

### Protected PBBS `q`-safe flag rethreading

Rethread the exact PBBS owner multiset into cycles or paths so that:

1. every owner is used exactly once;
2. every proper positive coordinate run has length at least `q`;
3. every required all-width target retains a designated PBBS fan
   occurrence, or gains a certified replacement occurrence;
4. every seam and fusion switch respects the same run bound and the
   protected phase/socket/history tickets.

If these four clauses hold, the maximal flat source is obtained by erosion:

\[
 P_i=\bigcap_{h=0}^{q-1}X_{i+h}.
\tag{4.1}
\]

No coordinate inserted within a block of `q-1` transitions can be deleted
again inside that block, so `(4.1)` has the required fixed rank.  Every
retained width-`w` PBBS owner union then becomes a literal union of
`q+w-1` consecutive source letters.  This formally supplies the flat
carrier and the complete upper deck.

The theorem is stronger than:

* component fusion alone;
* a transversal of short PBBS returns alone;
* support-surjectivity alone; or
* an unprotected alternating `C_6/C_8` switch bank.

### 4.1 The exact immediate-upper deletion budget

There is already a sharp necessary condition for any rethreading which
cuts the PBBS cycles into directed pieces and leaves the interiors of those
pieces unchanged.  Let `E` be the PBBS edge set, let

\[
 \sigma:E\longrightarrow { [2r-1]\choose r+1}
\tag{4.2}
\]

be the immediate-upper colour, and put
`mu(U)=|sigma^(-1)(U)|`.  The PBBS angle theorem gives
`1<=mu(U)<=3`.  A cut set `D subseteq E` retains at least one literal PBBS
witness of every immediate-upper target if and only if

\[
 |D\cap\sigma^{-1}(U)|\le \mu(U)-1
 \qquad\hbox{for every }U.                         \tag{4.3}
\]

In particular, the total capacity of all upper fibres is exactly

\[
 \sum_U(\mu(U)-1)
 =|E|-{2r-1\choose r+1}
 ={2\over r+1}{2r-1\choose r-1}
 =\operatorname {Cat}_r.                           \tag{4.4}
\]

For a proper positive coordinate run, call the run together with its
insertion and removal transition edges its **collar**.  If a run has
length less than `q` and `D` misses its collar, then the entire pattern
`0,1,...,1,0` remains internal to one unchanged directed piece.  No
permutation of the pieces can lengthen it.  Consequently every such
piece-preserving `q`-safe rethreading must satisfy both

\[
 \boxed{
 \begin{array}{l}
 D\text{ meets every PBBS positive-run collar of length }<q,\\
 |D\cap\sigma^{-1}(U)|\le\mu(U)-1\quad\text{for every }U.
 \end{array}}                                      \tag{4.5}
\]

Thus even the immediate-upper transport problem is a capacitated circular-
interval transversal with total colour capacity `Cat_r`.  The usual
uncoloured return-packing bound does not prove `(4.5)`, and `(4.5)` is only
necessary: the new seams must themselves be `q`-safe.  The all-width flag
bank imposes further window-crossing constraints, so it cannot weaken this
gate.

## 5. Relation to the MSW route

The two explicit factors now have complementary exact strengths.

\[
\begin{array}{c|c|c}
 &\text{MSW wreath factor}&\text{PBBS/GK-complement factor}\\ \hline
\text{owner integrality}&\text{exact}&\text{exact}\\
\text{flat growing residence}&\text{exact}&\text{fails at }q=4\\
\text{immediate lower support}&\text{exact}&\text{exact}\\
\text{immediate upper support}&\text{canonical linear defect}&\text{complete, load }1..3\\
\text{all-width upper bank}&\text{not proved}&\text{complete}\\
\text{components}&\operatorname {Cat}_{r-1}&\le\operatorname {Cat}_{r-1}
\end{array}
\tag{5.1}
\]

Accordingly, proving that the specific MSW orders cover their second shadow
is no longer the only way forward.  The sharper alternatives are:

1. transport the PBBS flagged all-width bank into a rethreaded resident
   chronology; or
2. rethread the MSW resident owners while importing PBBS-designated
   witnesses and preserving them occurrence by occurrence.

Either is a joint protected chronology theorem, not a new marginal count.

## 6. Scope corrections from the selector experiments

The cyclic-unmatched three-choice diamond catalogue gives a beautiful
directed-triangle normal form and finite linear forests through `r=7`, but
it cannot be the all-parameter replacement.  Its exact plane-tree degree
law implies a capacity deficit for every `r>=14` even before acyclicity.

Allowing every adjacent lexical diamond gives positive simultaneous
lower/tail/head-injective acyclic selectors through `r=7` in remote SAT
audits.  This remains finite evidence.  It is now secondary to `(0.1)`,
because the PBBS/GK-complement theorem closes the support rows for all
parameters without solving a new selector problem.

## 7. Updated frontier

The central long-aperture question should now be stated as follows:

\[
 \boxed{
 \begin{array}{c}
 \text{Can the exact PBBS owner multiset be rethreaded into a flat}\
 \text{growing-residence chronology while retaining one protected}\
 \text{designated occurrence of every required all-width target?}
 \end{array}}
\tag{7.1}
\]

An affirmative answer, coupled to the already isolated socket and common-cap
gates, is the substantive route toward `B(k)+O(1)`.  A negative answer would
need an invariant of protected rethreading, not another missing-shadow
example in the canonical MSW factor.
