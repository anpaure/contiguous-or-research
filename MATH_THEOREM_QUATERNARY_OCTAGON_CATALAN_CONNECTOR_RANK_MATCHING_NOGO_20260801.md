# Quaternary octagons are local rank surgeries, not Catalan connectors

Date: 2026-08-01  
Lane: fixed-`H` upper-decorated host / Catalan connector gate  
Status: exact residual rank-matching criterion and explicit finite method
no-go.  No all-dimensional upper-complete host theorem is claimed.

## 0. Outcome

The quaternary endpoint absorber from
`MATH_THEOREM_AD_ENDPOINT_PATH_BANK_QUATERNARY_OCTAGON_20260801.md`
does not close the `H=1` upper-decorated bounded-component gate when it is
inserted into the Catalan decomposition of
`MATH_THEOREM_UPPER_DECORATED_NEAR_FACTOR_CATALAN_CONNECTOR_DECOMPOSITION_20260801.md`.
There are two exact reasons.

1. A quaternary `4 <-> 4` exchange preserves the complete upper-colour
   multiplicity vector.  It therefore cannot repair any upper hole in the
   q1 factor supplied by
   `MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`.
2. An exchange confined to a rooted Catalan forest preserves its size.
   If the result is still a forest, it still has exactly `C` components.
   Thus it supplies none of the `C-O(1)` additional connector-rank units.

The octagon becomes useful only after a suitable upper-complete matching
completion has already been supplied.  Under its prepared one-cycle plus
one-path hypothesis, one toggle gives one relative graphic-rank gain.  A
global proof would still have to supply an augmenting octagon at every
required stage; neither of the three input theorems does this.

The exact remaining connector condition has a compact form.  After fixing
a rooted Catalan forest `Q0`, its `C` path components each expose one tail
port and one head port.  On the residual `C`-by-`C` incidence graph one must
find a perfect matching `F` whose links have contracted graphic rank at
least `C-s`.  Equivalently, the directed cycle cover induced by `F` on the
Catalan components has at most `s` cycles.  For `s=1`, the residual port
graph must have a perfect matching which is one directed Hamilton cycle.

This condition is not forced even qualitatively by the existence of the
Catalan decomposition.  The frozen upper-surjective `m=4` factor used in
the Catalan replay has component lengths `3,11,21` and the documented
`Q0,Q1` certificate, but an exhaustive census finds **no quaternary
octagon support at all**, on either side of the identity, under any of the
eight independent orientations of its three components.

## 1. Catalan residual ports

Fix a perfect matching `M0` of the middle-levels incidence graph `ML_m`
between

\[
 {\cal L}={[2m-1]\choose m-1},\qquad
 {\cal M}={[2m-1]\choose m}.
\]

Put

\[
 W={2m-1\choose m},\qquad
 U={2m-1\choose m+1},\qquad
 C=W-U={2W\over m+1}=\operatorname{Cat}_m.              \tag{1.1}
\]

For `e=LV in ML_m-M0`, retain the rooted link notation

\[
 \operatorname{up}(e)=M_0(L)\cup V,
 \qquad
 \lambda(e)=L\longrightarrow M_0^{-1}(V).               \tag{1.2}
\]

Let `Q0` be a rooted Catalan forest: it is a matching of size `U`, its
upper map is a bijection onto the rank-`m+1` layer, and its links are
graphic-independent.  Its link forest has exactly `C` components.  Since
the links are a directed partial permutation, each component is a directed
path, with isolated vertices allowed.  Consequently every component has
exactly one lower vertex unused as a link tail and exactly one lower vertex
unused as a link head.

Let \(X\subset {\cal L}\) and \(Y\subset {\cal M}\) be the two shores left
unmatched by `Q0`.  Both have size `C`, and put

\[
              B_0=(ML_m-M_0)[X,Y].                       \tag{1.3}
\]

Write \({\cal C}(Q_0)\) for the set of the `C` link components.  Every
residual edge `e=LV in B0` induces a labelled contracted link

\[
 \bar\lambda(e)=
 \bigl[\operatorname{comp}_{Q_0}(L),
       \operatorname{comp}_{Q_0}(M_0^{-1}(V))\bigr]       \tag{1.4}
\]

on \({\cal C}(Q_0)\).  Loops and parallel edges are retained.  Let
`r_barG` denote graphic rank in this contracted labelled multigraph.

## 2. Exact high-rank perfect-matching criterion

### Theorem 2.1 (residual rank-matching equivalence)

Fix `1<=s<=C`.  The following are equivalent.

1. There is a matching `Q1 subset B0` of size `C-s` such that
   `bar lambda(Q1)` is graphic-independent and, after deleting the
   endpoints of `Q1`, the remaining graph `B0` has a perfect matching on
   its `s` vertices per shore.
2. There is a perfect matching `F` of `B0` such that
   \[
                         r_{\bar G}(F)\ge C-s.             \tag{2.1}
   \]
3. There is a perfect matching `F` of `B0` for which
   `M0 union (Q0 union F)` is an upper-surjective q1 factor with at most
   `s` components.

For every perfect matching `F` of `B0`, the component count is exactly

\[
 c\bigl(M_0\cup(Q_0\cup F)\bigr)
                  =C-r_{\bar G}(F).                       \tag{2.2}
\]

#### Proof

Assume 1, and let `R` be the residual `s`-edge perfect matching.  Then
`F=Q1 union R` is a perfect matching of `B0`.  Since `bar lambda(Q1)` is an
independent set of size `C-s`, monotonicity gives (2.1).

Conversely, assume 2.  Choose from `F` a graphic-independent subset `Q1`
of size `C-s`.  Because `F` is a matching, so is `Q1`.  Removing `Q1`
from `F` leaves `s` edges which perfectly match the shores left after the
endpoints of `Q1` are deleted.  This gives 1.

The forest `lambda(Q0)` has rank `U`.  Contracting it shows

\[
 r_{\rm gr}\bigl(\lambda(Q_0\cup F)\bigr)
                      =U+r_{\bar G}(F).                   \tag{2.3}
\]

The links of the full second matching `Q0 union F` form a permutation on
the `W` lower vertices, so the components of the q1 factor are its
permutation cycles.  Therefore

\[
 c=W-r_{\rm gr}\bigl(\lambda(Q_0\cup F)\bigr)
   =W-U-r_{\bar G}(F)=C-r_{\bar G}(F),                   \tag{2.4}
\]

which proves (2.2) and the equivalence of 2 and 3.  Upper surjectivity is
already supplied by `Q0`.  \(\square\)

### Corollary 2.2 (component-port cycle cover)

Every perfect matching `F` of `B0` gives each Catalan path component one
outgoing residual link and one incoming residual link.  Hence its
contracted directed links form a cycle cover of the `C` components, and

\[
 r_{\bar G}(F)=C-#\{\hbox{cycles of the component-port cover}\}.         \tag{2.5}
\]

In particular:

* an `s=1` certificate is exactly a perfect matching of `B0` whose
  component-port cover is one directed Hamilton cycle;
* an `s=O(1)` certificate is exactly a perfect matching whose port cover
  has `O(1)` cycles.

Thus ordinary Hall on `B0` proves only the existence of a cycle cover.  It
does not control the number of cycles.  The remaining condition is a
**high-graphic-rank perfect matching**, not an ordinary residual Hall row.

### Protected version

For the terminal plus phase of one quaternary collar, choose the two
incidence matchings so that `M0` contains the first shore `P0` and the
second shore is `P1`.  The plus octagon and its private return rail project
to a path forest, and their upper colours are distinct.  Hence `P1` is an
admissible forced seed for `Q0`.  What is not proved is that this seed
extends to a rooted Catalan forest of size `U` or that the resulting
residual graph has a perfect matching satisfying (2.1).

If some protected second-shore set `S` is instead left for the connector
stage, the exact modification is to require `F superset S`, require
`bar lambda(S)` independent, and require rank at least `C-s-|S|` after
contracting `bar lambda(S)`.  For the one-collar plus forest there is no
need for this complication: all of `P1` may be rooted in `Q0`.

## 3. Why the octagon does not discharge Theorem 2.1

### Proposition 3.1 (cardinality and palette no-go)

Let \(O\leftrightarrow N\) be a quaternary Boolean-octagon exchange.

1. The lower, upper, tail and head multisets of `O` and `N` agree.  In
   particular, toggling an arbitrary ambient factor preserves its complete
   upper-colour multiplicity vector, not merely upper surjectivity.
2. Suppose `O subset Q0` and put `Q0'=(Q0-O) union N`.  If `Q0'` is again a
   rooted Catalan forest, then
   \[
       |Q_0'|=U,\qquad r_{\rm gr}(\lambda(Q_0'))=U,
       \qquad c(\lambda(Q_0'))=W-U=C.                    \tag{3.1}
   \]
   Thus the exchange contributes no connector-rank unit.
3. In the prepared topology of the endpoint-absorber theorem, where one
   old edge lies on a cycle and three ordered old edges lie on one separate
   path, the proved relative rank change is exactly
   \[
                         r_K(N)-r_K(O)=1.                 \tag{3.2}
   \]
   This statement presupposes the ambient remainder `K` and the required
   ordered support.  It does not construct either one.

#### Proof

Part 1 is the four-resource identity.  For part 2, the exchange preserves
cardinality, and every forest has rank equal to its number of edges.  Thus
any forest result has rank `U` and exactly `W-U=C` spanning components.
Part 3 is the one-cycle plus one-path concatenation theorem: those two
components become one path while all other components are unchanged.
\(\square\)

There are two consequences for the proposed `H=1` insertion.

* Starting from the protected q1 factor theorem cannot work: that factor
  may have upper holes, and every octagon toggle preserves those holes.
* Starting from `Q0` cannot work by internal toggles: the missing rank is
  `C-s`, while every valid rooted transversal still has rank `U`.

One may instead first complete `Q0` by a perfect matching `F`, open a root
component through the protected path, and try to absorb the other cycles
sequentially.  This gives a valid conditional strategy, but it needs the
following new statement:

> **Quaternary augmentation accessibility.**  Whenever the current
> upper-surjective protected factor has more than `s` cycles, some
> unprotected cycle edge and three suitably ordered edges of the current
> root path form a legal quaternary support whose toggle merges that cycle
> into the root path.

The octagon theorem proves what one such support does.  It does not prove
accessibility, and its polynomial completion menu for a fixed target does
not show that the other three old atoms occur in the current matching or
in the required path order.

## 4. A Catalan connector certificate with zero octagons

### Theorem 4.1 (finite method no-go at `m=4`)

Index the rank-three subsets of `[7]` lexicographically and take the two
rank-three/rank-four perfect matchings

```text
M0 = 71,15,23,51,99,29,85,53,101,57,45,77,113,89,105,46,30,39,
     86,27,43,75,54,83,106,92,108,78,60,116,102,58,90,120,114

M1 = 39,43,83,99,75,77,23,45,85,27,57,105,53,113,101,15,86,102,
     71,30,58,78,51,90,114,29,46,108,54,92,116,60,89,106,120
```

where each number is the bit mask of the rank-four endpoint.  Then:

1. `M0 union M1` is upper-surjective and has lower-shore cycle lengths
   `3,11,21`;
2. cuts at indices `0,1,24` give the documented upper-transparent
   Catalan decomposition
   \[
       |Q_0|=21,\quad c(Q_0)=14,\quad |Q_1|=11,
       \quad |R|=3;                                      \tag{4.1}
   \]
3. the full residual perfect matching `F=M1-Q0` has size `14` and
   contracted graphic rank `11`, so
   \[
                         14-r_{\bar G}(F)=3,              \tag{4.2}
   \]
   replaying Theorem 2.1 exactly; and
4. the factor contains no quaternary Boolean-octagon side under any
   independent orientation of its three components.

#### Exhaustive census

For each of the `2^3=8` component orientations, the replay separately
enumerates both sides `O` and `N` of the octagon identity.  On `[7]`, an
indexed parameterization consists of

\[
 S\in{[7]\choose2},\qquad z\notin S,
 \qquad (a_0,a_1,a_2,a_3)
       \text{ an ordering of }[7]-(S\cup\{z\}).           \tag{4.3}
\]

There are

\[
                 {7\choose2}\,5\,4!=2520                \tag{4.4}
\]

parameterizations per side and orientation, and therefore `40320` checks
in total.  For `O`, the replay asks for all four oriented atoms

\[
 (S+a_i, S+z+a_i+a_{i+1}, S+z+a_i, S+a_i+a_{i+1}),   \tag{4.5}
\]

and for `N` it replaces `a_(i+1)` by `a_(i-1)` in the head and upper
ports.  Every one of the `40320` checks fails.  Reversing the cyclic
`a`-order also identifies the two sides, so the separate `O` and `N`
counts cross-check the same zero-support conclusion.

This is a no-go for the inference

\[
 \boxed{\text{Catalan forest + connector certificate}
        \Longrightarrow\text{available quaternary rank augmentation}.} \tag{4.6}
\]

It is not a counterexample to the existence of a different upper-complete
`H=1` host, nor to an accessibility theorem with additional hypotheses.

## 5. Exact remaining `H=1` statement

Let \(P=P_0\mathbin{\dot\cup}P_1\) be the incidence lift of one fixed
terminal plus quaternary collar, and let `M0` contain `P0`.  The exact
Catalan-certificate route to an upper-complete factor with at most
`s=O(1)` components is:

1. find a rooted Catalan forest `Q0` containing `P1`; and
2. in its residual graph `B0`, find a perfect matching `F` satisfying
   \[
                         r_{\bar G}(F)\ge C-s.             \tag{5.1}
   \]

The first row is a rooted common-independence problem on incidence edges:

* one left-shore partition constraint;
* one middle-shore partition constraint;
* the upper-colour partition matroid, used as a basis of size `U`; and
* the graphic link matroid.

The second row is a perfect matching--the common basis of the two residual
shore partition matroids--with near-spanning rank in the contracted graphic
matroid.  Equivalently, it is the component-port cycle-cover condition of
Corollary 2.2.

Neither row follows from ordinary Ore--Ryser or Hall, and neither is proved
by a quaternary exchange.  An octagon-based proof must replace row 2 by an
equally substantive global accessibility theorem and must still supply an
initial upper-surjective completion.  Thus the three input theorems do not
prove the desired all-dimensional `H=1` host.

As in the Catalan decomposition theorem, (5.1) is an exact sufficient
certificate.  A converse from an arbitrary bounded-component decorated
factor is exact after upper-transparent cuts; without transparency it has
only `O(s)` named upper casualties, which is sufficient for the
additive-constant application but is not literal exact upper completeness
of the opened forest.

## 6. Independent replay

Run

```text
python3 scratch/audit_quaternary_octagon_catalan_connector_rank_matching_nogo_20260801.py
```

Expected status:

```text
PASS_QUATERNARY_OCTAGON_CATALAN_CONNECTOR_RANK_MATCHING_NOGO
```

The replay independently checks the two matchings and every incidence,
upper surjectivity, the `3,11,21` cycle census, the safe cuts, the
`Q0,Q1,R` decomposition, the residual contracted rank identity, and all
`40320` oriented `O/N` octagon parameterizations.

Frozen hashes:

```text
script SHA-256  9c4ffa8d4a274c66356c5908aec8d2979a7f92416efa15f8ee71f6a1a1dcbad3
JSON SHA-256    fa25b6c51397d3df8cf81b960fcd2171c16ac3c42f7ae62da6e98ffd48a92043
payload SHA-256 dbde77353f25de9eeba9044e42ad5361a61c54c9cea7eb3073d12d7fbff87b05
```
