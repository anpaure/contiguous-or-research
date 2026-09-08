# Independent audit: small-port Boolean one-step private router

**Date:** 2026-08-04  
**Theorem audited:**
`MATH_THEOREM_SMALL_PORT_BOOLEAN_ONE_STEP_PRIVATE_ROUTER_20260804.md`  
**Original SHA-256:**
`be0ad31552f612f221b0a3143ce72da3caf85583ca27d7b1778324d3fee418b1`  
**Corrected SHA-256:**
`5012824ff43f6baa6093eba21e18f460c598c75d103acd9ac56a5a628e3e808c`  
**Method:** independent symbolic replay.  No computation, solver, or finite
enumeration.

## 0. Verdict

**PASS after one occurrence-lift clarification.**

The Boolean Hall theorem, including the endpoint inequality for all small
`L,p`, is correct as written.  The one-step occurrence lift is also correct
after distinguishing forbidden Boolean sink values from occupied physical
sink vertices and requiring each port neighbourhood to be type-legal for
every gain incident with that port.

The theorem file was corrected only at that interface.  No combinatorial
inequality or conclusion changed.

The result is unconditional for a fixed bank satisfying its hypotheses.  It
does not prove that a parent-derived common-cap state has distinct Boolean
port values, `Theta(k)` common typed extensions, or an injective physical
reservation of those extension values.

## 1. Pair-overlap replay

Let `p,p'` be distinct rank-`s` sets.  A common rank-`(s+1)` extension must
contain `p union p'`.  Since equal-rank distinct sets have
`|p union p'|>=s+1`, there are two cases.

* If `|p union p'|=s+1`, the only possible common extension is
  `p union p'`.
* If `|p union p'|>s+1`, no common extension exists.

Restricting full upper shadows to typed menus cannot enlarge an
intersection.  Therefore

\[
                         |N(p)\cap N(p')|\le1.        \tag{1.1}
\]

Lemma 1.1 is exact.

## 2. Bonferroni replay

For a sink `y` lying in exactly `r` of the sets `N(p)`, its contribution to

\[
 \sum_p|N(p)|-\sum_{p<p'}|N(p)\cap N(p')|            \tag{2.1}
\]

is

\[
                         r-{r\choose2}.              \tag{2.2}
\]

This is at most one for every integer `r>=1`, while a point outside the
union contributes zero.  Summing pointwise proves the first Bonferroni lower
bound

\[
 \left|\bigcup_{p\in X}N(p)\right|
 \ge\sum_{p\in X}|N(p)|
     -\sum_{\{p,p'\}\in{X\choose2}}|N(p)\cap N(p')|. \tag{2.3}
\]

Using degree at least `L` and (1.1) gives

\[
                         |N(X)|\ge xL-{x\choose2}.   \tag{2.4}
\]

No assumption on triple intersections is missing; they only make the
two-term lower bound weaker.

## 3. Hall endpoint inequality, including small parameters

After deleting an arbitrary forbidden **value** bank of size `f`, (2.4)
gives

\[
 |N(X)-F|-|X|
 \ge g(x):=x(L-1)-{x\choose2}-f.                    \tag{3.1}
\]

As a real quadratic,

\[
 g(x)=-{x^2\over2}+\left(L-{1\over2}\right)x-f      \tag{3.2}
\]

is concave.  Hence its minimum on `[1,p]` is at an endpoint.

At `x=1`,

\[
                         g(1)=L-1-f\ge0.             \tag{3.3}
\]

At `x=p`, use `f<=L-1`:

\[
 \begin{aligned}
 g(p)
 &\ge p(L-1)-{p\choose2}-(L-1)\\
 &=(p-1)\left(L-1-{p\over2}\right).                 \tag{3.4}
 \end{aligned}
\]

The small cases and the general case are:

* `P` empty: Hall is vacuous.
* `p=1`: (3.3) is the required inequality.
* `L=1`: the hypotheses force `p<=1` and `f=0`, so the preceding case
  applies.
* `L>=2` and `2<=p<=L`:
  
  \[
  L-1-{p\over2}\ge L-1-{L\over2}={L\over2}-1\ge0.   \tag{3.5}
  \]

Thus every Hall cut is nonnegative.  The injection of Theorem 2.1 follows.
The conditions are sufficient, not asserted necessary; the theorem's
sharpness remark correctly notes only that `f<L` cannot be weakened in
complete generality.

## 4. Required occurrence-lift correction

The original theorem used `F` in two incompatible types:

* Theorem 2.1 has
  
  \[
                       F\subseteq{[k]\choose s+1},  \tag{4.1}
  \]
  
  a bank of Boolean sink **values**.
* Original Section 3 said that `F` contained occupied physical sink
  **vertices**.

Moreover, one suffix selected for port `p` may be used by any gain adjacent
to `p` after max-flow integrality.  Its terminal type must therefore be
accepted by every such gain, not merely by one nominal port incidence.

The corrected theorem now fixes an injective physical reservation

\[
 r:\mathcal Y-F\longrightarrow T,
 \qquad \mathcal Y=\bigcup_{p\in P}N(p),             \tag{4.2}
\]

at the level of stated hypotheses: different reserved values have distinct
unit-capacity sink vertices.  Every value with no available occurrence, or
whose reserved occurrence is consumed by compensation, a prefix, or a
protected bank, is inserted into the forbidden **value** set `F`.  It also
requires that `r(Y)` have a terminal type accepted by every gain incident
with every port `p` for which `Y in N(p)`.

With these corrections, an injective Boolean matching `phi` lifts to the
literal suffix family

\[
                         p\longrightarrow r(\phi(p)).              \tag{4.3}
\]

The sinks are distinct because both `phi` and `r` are injective.  The ports
are distinct physical occurrences by hypothesis.  Each suffix is one
step and has no additional shared unit-capacity interior, so the family is
pairwise vertex-disjoint away from its distinct endpoints.  This proves the
literal lift exactly within the corrected scope.

The cardinality condition `|F|<=L-1` must, of course, be checked **after**
all unavailable or occupied reserved values have been added.  The theorem
does not infer that bound from aggregate physical sink count.

## 5. Factor-flow replay

Let `B=(G,P;E)` be left `h`-regular and right degree at most `h`.  For every
incidence `gp`, concatenate its private prefix with the unique suffix of
`p`, and send `1/h` units.

* Gain `g` has `h` incidences, so emits one unit.
* A private prefix interior has load `1/h`.
* A port and its suffix have load
  
  \[
                         {\deg_B(p)\over h}\le1.      \tag{5.1}
  \]
* Reserved sinks are pairwise distinct.
* Prefix/suffix privacy accounts for every remaining unit capacity.

This is a feasible flow of value `|G|` in the node-split residual network.
Integral max flow saturates every unit gain-source arc and terminates at
distinct sink arcs.  Because `N(p)` is common type-legal for all gains
adjacent to `p`, an integral path may choose any displayed incidence
without changing terminal legality.  Corollary 3.1 is correct.

Without the common-type condition, single-commodity integrality could send
a gain to a sink legal only for another gain.  Without the injective
reservation (4.2), distinct Boolean values would not prove distinct
physical capacities.  The corrected theorem explicitly retains both
premises.

## 6. Middle-level specialization

For an `m`-set in a `(2m+1)`-element ground set there are exactly

\[
                         (2m+1)-m=m+1               \tag{6.1}
\]

one-coordinate upper extensions.  If typing forbids at most `c`, the
common degree lower bound may be taken as

\[
                         L=m+1-c.                   \tag{6.2}
\]

The displayed conditions `|P|<=m+1-c` and `|F|<=m-c` are exactly
Theorem 2.1's `|P|<=L`, `|F|<=L-1`.  For a nonempty interface they also
force `L>=1`; the empty interface is trivial.

If `B` is left 2-regular and its right shore is the active support, then

\[
 |P|\le |E(B)|=2|G|.                                \tag{6.3}
\]

Hence `|G|<=(m+1-c)/2` implies the required port bound.  A fixed `c`, an
`O(sqrt m)` gain bank, and an `O(sqrt m)` forbidden **value** bank satisfy
all these inequalities eventually.  Corollary 3.2 is correct, conditional
on the physical reservation and common-type premises audited in Section 4.

## 7. Asymptotic endpoint

If

\[
 |P|\le C_1d(k),\qquad |F|\le C_2d(k),\qquad
 L\ge\eta k,\qquad d(k)=\Theta(\sqrt{k}),            \tag{7.1}
\]

then

\[
 {|P|\over L}=O(k^{-1/2}),
 \qquad
 {|F|+1\over L}=O(k^{-1/2}).                         \tag{7.2}
\]

Both ratios are below one for all sufficiently large `k`, proving
`|P|<=L` and `|F|<=L-1`.  The asymptotic corollary is valid.

Its scope is local and conditional: `L>=eta k` counts common type-legal
extensions with distinct reserved physical occurrences after the complete
cap state and fixed prefixes are materialized.  Raw Boolean upper-shadow
degree does not itself prove that occurrence-level premise.

## 8. Final audit boundary

The corrected result proves:

\[
 \boxed{\begin{array}{c}
 \text{small distinct Boolean port bank}
 +\text{linear common typed degree}\\
 +\text{injective private occurrence reservation}
 \Longrightarrow\text{full simultaneous suffix router}.
 \end{array}}                                        \tag{8.1}
\]

It does not construct the ports, the prefix factor, the cap state, or the
occurrence reservation, and it does not apply to duplicate-valued ports or
multi-step suffixes with shared interiors.
