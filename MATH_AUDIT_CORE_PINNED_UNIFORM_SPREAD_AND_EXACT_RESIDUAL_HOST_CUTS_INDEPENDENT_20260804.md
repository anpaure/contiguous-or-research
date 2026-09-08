# Independent audit: core-pinned spread, residual factor cuts, and pull-host cuts

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_CORE_PINNED_UNIFORM_SPREAD_AND_EXACT_RESIDUAL_HOST_CUTS_20260804.md`  
**Method:** line-by-line deductive replay; pure mathematics; no computation,
search, sampling, or solver  
**Verdict:** **INDEPENDENT GO after three explicit repairs.**  The pinned
spread and spanning protected-two-factor statements are valid for all
sufficiently large `m`.  The pull-host statement is exact only in the
declared fixed, tree-compatible last-ring host containing the opposite-half
spanning pull tree.  It does not place the protected two-factor in that
host, connect its cycles, prove global residence, or preserve unprotected
upper witnesses.

The three repairs made during this audit were:

1. the deterministic cyclic-interval top bank was made literally pinned by
   putting `q` last in every `K`-order (and keeping the ring-deletion label
   first on the three ring paths); this removes a possible hidden
   substitution of the earlier unpinned bank;
2. the sixth-moment sum was given an explicit uniform middle/upper-tail
   split, rather than an informal appeal to a central range; and
3. the pull-host theorem now explicitly assumes that its fixed host contains
   `R_q^0 union {g}` and records why `R_q^0` avoids the forced-off bank.

## 1. The pinned hybrid bank is literal

The ordinary cyclic-interval top path deletes the first `m-2` coordinates
of its ordered `(m-1)`-set `K`.  Choosing `q` as the last coordinate makes
`q` persist in every top owner and hence in every immediate lower and upper
colour.  On the three paths carrying the ring hinges, the prescribed
ring-deletion coordinate and `q` are distinct, so they may be put first and
last simultaneously.  The first protected adjacency is therefore unchanged.

The pinned shortened noninterval paths and pinned high-tail paths already
contain `q` in every resource.  Exact external trace separates the top paths
from the noninterval paths and separates distinct private paths.  Thus the
hybrid bank is one genuinely core-pinned bank; no estimate below is imported
from a second unpinned realization.  Its incidence size remains
`O(m 2^m)`.

## 2. Owner-star marginal and union bound

Fix a rank-`m` owner `U` containing `q`, put `S=U cap E`, and let `|S|=e`.
For an external deletion `a in S`, the facet `U-{a}` has trace `S-{a}` of
size `e-1`.  Its required part in `K-{q}` has size `m-e-1`.  A pinned
shortened path of this trace has `e-2` distinct immediate lower colours,
and every one of the

\[
 \binom{m-2}{m-e-1}=\binom{m-2}{e-1}
\]

possible core parts is symmetric.  Hence the marginal (1.3) is exact:

\[
 \Pr(U-\{a\}\in Z_P)
   ={e-2\over\binom{m-2}{e-1}}.
\]

Different `a` give different external traces, whose low-path orders are
independent.  Owners with this value of `e` number

\[
 \binom me\binom{m-2}{e-1}.
\]

The union bound over triples of cross-trace hits therefore gives exactly
(1.4).  The ratio

\[
 {\binom me\over\binom{m-2}{e-1}}
 ={m(m-1)\over e(m-e)}
\]

is correct.  For fixed `4<=e<=8` the summand is `O(m^(2-e))`.  On
`9<=e<=m/4`, its polynomial numerator is `O(m^6)` and the denominator is at
least `binom(m-2,8)`, so the whole range is `O(1/m)`.  On
`m/4<e<=m-d-1`, unimodality gives the denominator lower bound

\[
 \min\left\{\binom{m-2}{\lfloor m/4\rfloor-1},
             \binom{m-2}{d}\right\}=\omega(m^8),
\]

whereas the summed numerator is `O(m^8/d)`.  Thus (1.7) follows.  One
common low-path choice has at most two randomized cross-trace facets under
every owner.

The remaining pre-high owner load is deterministic and is unchanged by the
pin.  Deleting a coordinate of `K-{q}` stays in one exact trace and the
same-trace adjacency bound gives at most two hits.  Deleting `q` cannot hit
the protected lower palette.  The cyclic top/ring contribution gives at
most three cross-trace facets.  Hence the pre-high total is at most seven.

## 3. Pinned lower-star and endpoint tails

If a lower vertex `x` avoids `q`, the only pinned owner above it is `x+q`.
Owner simplicity bounds both relevant private loads by one, so such a vertex
is never a critical star.

Now suppose `q in x`, put `S=x cap E`, and set

\[
 D=(K-\{q\})-x,qquad |S|=|D|=s.
\]

A random private path meeting this star has trace `S+z`, with at most
`m-s` choices of `z`.  Its required core part is the fixed set
`(K-{q})-D`.  The path has `s+1` owner positions and two endpoints, giving
the valid means

\[
 \mu_\ell(s)\le{(m-s)(s+1)\over\binom{m-2}s},
 \qquad
 \mu_e(s)\le{2(m-s)\over\binom{m-2}s}.
\]

Distinct contributing paths again have distinct independently ordered
traces, and one path contributes at most one unit to either load.  There
are

\[
 N_s=\binom ms\binom{m-2}s
\]

lower vertices on this pinned level.  The standard bound
`Pr(X>=6)<=(e mu/6)^6` yields (1.9).

For completeness, the sum is uniform, not merely pointwise.  With
`B_s=binom(m-2,s)`, the exact ratio

\[
 {\binom ms\over B_s}
 ={m(m-1)\over(m-s)(m-s-1)}
\]

shows that every term with `4<=s<=m/2` is `O(m^-4)` after using
`B_s>=binom(m-2,4)`; summing costs `O(m^-3)`.  For
`m/2<s<=m-d-3`, one has `B_s>=binom(m-2,d+1)=m^omega(1)`, which uniformly
dominates the polynomial numerator.  The two fixed indices `s=2,3`
contribute `O(m^-2)` and less.  Therefore the total is `o(1)`.

The owner-star bad-event sum and both lower-star bad-event sums are each
`o(1)`, so their union is below one.  This proves genuine simultaneous
co-selection, not three incompatible existential choices.  The random
contribution is at most five, the possible own trace costs at most one, and
the fixed cyclic top/ring bank costs at most four singleton units.  The
pre-high caps ten follow.

## 4. The high-tail greedy co-selection remains valid

One monotone high path adds at most two protected facets below a fixed owner
and at most one unit to either lower-star load.  Declaring an owner critical
at load eight and a lower star critical at load ten therefore enforces final
caps nine and ten.

The exact identity

\[
 \sum_U z_U=m|Z_P|=O(m^2 2^m)
\]

shows that the critical-owner facet bank has only `2^(m+o(m))` resources.
Summed singleton and endpoint load is at most a polynomial multiple of the
already selected bank, so the two lower-star critical banks have the same
size scale.  All their relevant resources contain `q`; resources avoiding
`q` have zero probability under the conditioned high-path law.

The three conditioned owner/lower/upper denominators are respectively
central binomial layers of an `(N-1)`-set and are uniformly
`2^(2m-o(m))`.  The number of high traces is `2^o(m)`.  Adding all three
critical banks to the original resource-collision bank leaves the usual
per-step failure probability `2^(-m+o(m))<1`.  Recomputing critical sets
after each step proves the three final caps for the same completed bank.

## 5. Optional co-small and residual small cuts

The owner cap gives `g_U=m-z_U>=m-9`.  The exact optional-core ledger would
therefore give at least `m-10` selected facets below every owner in its
positive witness family.  The sharp partial-shadow theorem forces

\[
 |B^-|\ge\binom{2m-21}{m-11}+1=2^{2m-o(m)},
\]

contradicting the protected near-shadow localization
`|B^-|=O(m^2 2^m)`.  This uses the same pinned bank just constructed.

For a minimal residual deficient shore, irreducibility removes every
degree-two protected lower vertex, Johnson uncrossing gives a connected
component, and the co-small alternative has just been excluded.  On the
remaining shore every lower demand is two, so the exact Hall inequality is

\[
 2|A|\le\sum_U\min\{2-d_P(U),a_U\}. \tag{SC}
\]

Subtracting this capacity from the unprotected capacity gives (2.3): an
internal owner loses `min(2,a_U)`, while an endpoint owner loses one exactly
when `a_U>=2`.

The pinned hybrid is still an incidence-lift path bank with at most `2m`
deterministic top endpoints.  The independent small-cut theorem uses only
the two spread-ten bounds, that endpoint count, the owner-star cap nine,
and this path-forest structure.  All are now established simultaneously.
Its partial-shadow and Kruskal--Katona argument therefore applies without
changing the bank.  The residual integral `b`-matching gives a spanning
two-factor containing the protected reservoir.

This conclusion is a factor statement only.  A spanning two-factor may
have many cycles and supplies neither a chronology nor a residence theorem.

## 6. The pull-host cut is a separate conditional theorem

Fix the tree-compatible host `H` containing the opposite-half spanning pull
tree `R_q^0` and the coherent ring pull `g`.  Accessibility and phase
consistency determine the forced-on set `A_D` and the forced-off set `B_D`.
With `J=A_D union {g}`, a last-`g` tree must contain `J`, so `J` must be
graphic-independent.  In a multigraph this is exactly

\[
 |J cap E_H(X)|\le |X|-1
 \qquad(|X|\ge2), \tag{PH}
\]

after loops are excluded and parallel occurrence labels are retained.

Conversely, if `(PH)` holds, contract the components of `J`.  The image of
the spanning tree `R_q^0` is connected.  Every complete pull support in
`R_q^0` lies in the `q=0` half, while `D` and the complete ring state lie in
the `q=1` half.  Thus `R_q^0 cap B_D=emptyset`, and a subset of `R_q^0`
extends `J` to an allowed spanning tree.  Holding out `g` and then toggling
it gives the claimed two-cycle/one-cycle last-ring pair.

This verifies `(PH)` only inside this fixed host and last-ring scheme.  It
is not the same cut as `(SC)`:

* `(SC)` is a capacitated Hall cut on lower-shore subsets of `ML_m`;
* `(PH)` is a graphic-independence cut on occurrence-labelled pull edges.

The two-factor obtained from `(SC)` is not proved to be a state in `H`, and
no implication from `(SC)` to `(PH)` is valid.

## 7. Residence and upper-witness scope

Every completion pull from `R_q^0` changes only edges whose endpoints avoid
`q`.  It therefore freezes, but does not improve, the complete induced
`q=1` path system after the forced labels are installed.  Any short positive
`q`-run already present remains short.  For other coordinates even this
wall invariant is absent.

Likewise, vertex-disjoint pull support does not preserve remote occurrence
addresses or interval order.  The protected bank supplies selected
three-ring damage witnesses, but ambient upper completeness and invariance
of every selected exterior witness remain separate hypotheses.

Accordingly the audited source proves exactly:

1. one genuinely pinned complete reservoir with all three spread caps;
2. one spanning protected two-factor containing that bank; and
3. the conditional fixed-host criterion `(PH)`.

It does **not** prove accessibility, phase consistency, `(PH)` for a
constructed host state, connectedness of the Hall-completed factor, global
residence, ambient upper completeness, or terminal lower compilation.

