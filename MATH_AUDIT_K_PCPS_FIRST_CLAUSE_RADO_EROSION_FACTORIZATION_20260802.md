# Independent audit: PCPS first-clause Rado--erosion factorization

**Date:** 2026-08-02  
**Lane:** K, protected Catalan--pivot existence  
**Audited file:**
`MATH_THEOREM_K_PCPS_FIRST_CLAUSE_RADO_EROSION_FACTORIZATION_20260802.md`  
**Verdict:** **PASS after scope corrections.**  The product theorem is exact
for one completely frozen chronology, occurrence support, witness/pin/cap
system, global address quotient, and accepting non-set history state.  It is
not an existence proof for that prospective data.

## 1. Exact product equivalence

For every source address `j`, any feasible letter is contained in its cap
and in every target row whose interval uses `j`.  Hence it is contained in

\[
 \widehat E_j=C_j\cap\bigcap_{H\ni j}R_H.
\]

Conversely, assigning `A_j=widehat E_j` cannot introduce an element outside
any `R_H`; the covering inequality

\[
                 R_H\subseteq\bigcup_{j\in H}\widehat E_j
\]

gives the reverse containment.  Pins and nonemptiness are exactly the two
remaining pointwise conditions.  Thus (2.1) is necessary and sufficient and
`widehat E` is the unique pointwise maximum source word.

For the occurrence side, `S` is an incidence matching.  Therefore its rooted
arcs have distinct tails and heads.  After contracting the forced forest
`F`, choosing one edge from every residual upper-colour class while retaining
acyclicity is precisely a matroid transversal.  Rado gives

\[
 r_{M_{\rm gr}/F}(E(X))\ge |X|
\]

for every residual colour set `X`.  Since `F` is a forest,

\[
 r_{M_{\rm gr}/F}(E(X))=|E(X)|-\kappa(F\cup E(X)),
\]

which verifies (2.3)--(2.4).

The factorization is independent only because all rows are frozen before
either choice and marking `Q_0` activates no new source constraint.  If a
chosen representative itself activates a cap, pin, history, or witness row,
the theorem is inapplicable until that alternative is incorporated into the
fixed state or treated jointly.  Boolean closure also does not prove
residence or history acceptance; those are fixed guards supplied by `PCS`.

## 2. Rooted path and one-cycle faces

If `lambda(S)` is a forest, every `F union E(X)` is independent.  Because
the colour classes are disjoint, Rado reduces exactly to `E_R` nonempty for
every residual colour.

If `lambda(S)` is one spanning cycle, a rank loss occurs only when
`F union E(X)` is the whole cycle.  Then

\[
 |E(X)|=W-|F|,\qquad |X|\le U-|F|,
\]

so `|E(X)|-1>=|X|` follows from `W-U=Cat_m>=1`.  This proves the cycle
corollary; the original informal “Catalan excess pays” sentence is now
backed by the exact inequality.

## 3. Endpoint phase audit

An unrooted lower-rainbow owner path is not by itself a rooted path support.
Let its owners be `T_0,...,T_(W-1)`, put
`X_i=T_i cap T_(i+1)`, and let `o` be the unique unused lower root.  In the
terminal phase required by Corollary 3.1,

\[
 o\subset T_{W-1},\qquad
 M_0(X_i)=T_i,\qquad M_0(o)=T_{W-1},
\]

and the successor support is

\[
                  S=\{X_iT_{i+1}:0\le i<W-1\}.
\]

Its rooted arcs are

\[
 X_0\to X_1\to\cdots\to X_{W-2}\to o,
\]

and the `i`th upper colour is exactly `T_i union T_(i+1)`.  Therefore upper
selection is automatic only if every one of the `U` immediate-upper colours
actually occurs among those adjacent unions.  The protected pivot successor
incidences must be contained in this same support.  The opposite endpoint
has the reversed formula, but Corollary 3.1 now fixes the terminal phase and
does not silently switch phases.

The containment `o subset T_(W-1)` is load-bearing: without containment the
unrooted path does not recover a perfect incidence phase.

## 4. Source length, erosion and the pivot rows

The full depth row has `N=W+1` cells: `W` owners and one controlled boundary
ticket.  A depth-`d` antecedent has `N+d=W+d+1` source letters.  Thus this is
exactly the `B+1` convention when `B=W+d`; no `W+1`/`B+1` off-by-one remains.

Every `d+1` consecutive Johnson owners have intersection rank at least
`m-d`.  A terminal window containing `o` starts with `m-1` elements, incurs
no loss on the containment step into `T_(W-1)`, and crosses at most `d-1`
owner transitions, again leaving at least `m-d`.  Hence maximal envelopes
are nonempty for `m>d`.  For the uncapped row, coverage by those maximal
envelopes is exactly the clipped full-row residence condition.

For the split-core collar, `n=3d+1` depth cells require `n+d=4d+1` source
letters.  Once its internal equations are replayed, only the first and last
`d` source letters can meet external target rows, and only the `d` external
depth cells on either side can lose coverage.  The resulting set-valued
interface has at most `2d+2d=4d` rows.  Named-pin injectivity, the global
address quotient, and history acceptance remain additional literal guards;
the row count does not imply them.

## 5. PCS implication and the full immediate-upper shore

After correction, `PCS(m,d)` in the certified literal-pivot range
`m>=3d+1` fixes:

1. the terminal rooted phase and lower-rainbow Hamilton owner path;
2. an eligible rooted incidence for every colour in the full
   rank-`m+1` shore;
3. residence and the bounded pivot interface;
4. witnesses for strictly higher upper ranks; and
5. the preword/star-deletion Boolean closure.

Rows in `mathcal H` certify interval-OR occurrences.  They cannot replace an
absent rooted incidence in `S`, hence cannot supply a missing `Q_0` colour.
With that distinction, path support reduces Rado to individual colour
nonemptiness, (2.1) gives the source word, and the fixed history guard gives
the claimed global replay.  Thus `PCS` implies the stated rooted protected
host.  Conversely, only a `PCPS` certificate in the corrected prepared-
scaffold formulation is asserted to restrict to these rows.

## 6. K17 scope

Here `m=9`, `d=3`,

\[
 W={17\choose9}=24310,qquad U={17\choose10}=19448,
\]

and the source length on this sufficient face is `W+d+1=24314=B(17)+1`.

The independently certified three-hole model covers `19409/19412`
necessary non-`D` colours and misses `32058,103907,109870`.  Its literal
full rank-ten leave is `25=3+22`.

The independently authenticated `transport3_2.best.model` (model SHA
`be00a9d0b2470cd334a0b51476185c2ef61c99d28ce61b12f2ff32c26bcac213`;
audit JSON SHA
`b4401058201ed6cb40c0f3a16640d737da8ddd684ecc980f2e475ea6e2957f95`)
has only the non-`D` hole `32058`, but its full literal rank-ten leave is
still `23=1+22`, with rank-11/12/13 holes `1532/286/7` and `5584` short
positive runs.

The authenticated successor closes all `19412` non-`D` colours, but still
has literal holes `22/1533/286/7` at ranks 10--13 and `5586` short positive
runs.  The 22 rank-ten boundary/`D` colours belong to the same full
immediate-upper shore and require rooted support incidences; they cannot be
reclassified as Boolean-window-only rows.  Therefore none of these finite
models proves the required `W-1`-incidence rooted path support, any complete
`PCS` host, or a K17 word.

## 7. Final scope

Proved after correction:

- exact fixed-data Boolean/Rado product equivalence;
- the graphic deficiency formula;
- the rooted path and one-cycle collapse;
- the explicit endpoint phase;
- the uncapped envelope/residence corollary;
- the `W+d+1=B+1` and bounded `4d` interface counts; and
- the conditional implication `PCS ->` rooted upper-exact source-replayed
  host.

Still open:

- construction of `PCS(m,d)`;
- the complete full-shore K17 support and source chronology;
- terminal common-cap/lower compiler and regeneration; and
- any all-dimensional `B+1`, equality, or K17-word conclusion.
