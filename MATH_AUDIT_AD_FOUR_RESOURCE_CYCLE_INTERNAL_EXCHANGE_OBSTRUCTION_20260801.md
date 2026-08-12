# Adversarial audit of the four-resource cycle-internal obstruction

Date: 2026-08-01  
Audited source:
`MATH_THEOREM_AD_FOUR_RESOURCE_CYCLE_INTERNAL_EXCHANGE_OBSTRUCTION_20260801.md`  
Verdict: **PASS with two terminology/scope corrections.**  The restricted
fibre theorem and the Johnson-moat nonlocal near-factor theorem are sound.
Both corrections listed in Section 4 have been applied to the audited
source.

## 1. Restricted fibre: PASS

For `O_I={e_i:i in I}`, exact tail and head equality confines every new
endpoint to the full middle bank `{T_i}`.  The induced-cycle property then
forces every legal new atom to use one adjacent pair `T_i,T_(i+1)`, whose
intersection and union are uniquely `L_i,U_i`.  Exact lower and upper
equality therefore leaves exactly the two orientations `e_i,bar e_i` for
each `i in I`.

Writing `r_i=1` for reversal gives the exact tail equation

\[
 1_I(i)r_i=1_I(i-1)r_{i-1}.
\]

These quantities are constant around the cyclic index set.  If `I` is
proper, one is zero and all are zero.  If `I` is the full cycle, all are
zero or all are one.  Thus Theorem 3.1 has no missing disconnected-`I`
case and no hidden lower/upper cross-pairing.

The quantifier in Corollary 3.2 is also correct: for an integer support
bound `s`, `ell=max{4,s+1}` satisfies `ell<=m+2` whenever
`m>=max{2,s-1}`, and every support of order at most `s` is proper.

## 2. Delcourt--Postle deletion and count: PASS

The closed Johnson moat around four protected middle vertices has
`O(m^2)` physical vertices.  Deleting both typed middle copies and the
eight protected outer resources removes `O(m^2)` host resources.  Each has
degree at most

\[
 D=m(m+1),
\]

so at most `O(m^2D)=O(D^2)` of the `ND` host atoms are removed.

Delcourt--Postle Corollary 1.17 requires a maximum-degree bound, not
approximate regularity or a minimum-degree bound.  Passing to the residual
host cannot increase any host degree, pair-codegree, configuration degree
or mixed codegree.  Therefore the largest fixed-`g` colour class has size

\[
 {ND-O(D^2)\over D(1+D^{-\alpha_g})}=N-o(N).
\]

After deletion of the moat resources its physical cycles still all have
length greater than `g`.  Removing one atom per remaining cycle costs at
most `N/(g+1)`.  The usual stepwise fixed-`g` diagonal proves the claimed
`N-o(N)` linear forest.  No illicit growing-`g` invocation occurs.

## 3. Lower/upper splitting across the moat: PASS

No Johnson edge joins a protected middle vertex to a residual forest
vertex, so exact tail/head equality splits every new phase physically into
protected and forest parts.

This split also respects both outer shores.  Every rank-`m` superset of a
protected lower colour `L_i` is equal or Johnson-adjacent to either protected
endpoint above `L_i`, hence belongs to the closed moat.  Dually, every
rank-`m` facet of a protected upper colour `U_i` is equal or
Johnson-adjacent to a protected endpoint below `U_i`.  Therefore no atom
whose endpoints lie in the residual forest bank can use `L_i` or `U_i`.
Conversely, an atom on protected endpoints has the forced protected
intersection and union.  The cycle subphase consequently inherits exactly
the four **typed subbanks** contributed by `O cap C_4`, and Theorem 3.1
applies.

## 4. Required corrections

1. In Section 5, the `m=2` cycle `C_4` is an exact outer-complete
   four-resource factor (equivalently an exact transversal of the four
   partition shores), but it is **not** an ordered four-transversal under
   the authoritative five-matroid definition in
   `MATH_THEOREM_CATALAN_FOUR_TRANSVERSAL_MATROID_AND_TURN_AUGMENTATION_20260731.md`:
   that term includes graphic independence.  `C_4` is graphically
   dependent.  Replace “exact outer-complete ordered four-transversal” by
   “exact outer-complete four-resource factor.”

2. In Theorem 4.1's proof, replace “the cycle part ... has exactly the four
   typed resources removed from `C_4`” by “the cycle part has exactly the
   lower, upper, tail and head subbanks contributed by `O cap C_4`.”  The
   old support may meet a proper subset of the four protected atoms.
   Likewise “partial four-transversal” is best written “partial
   four-resource matching” unless the project explicitly adopts a
   graphic-free local convention.

These are scope/terminology corrections only; neither changes the two
decisive proofs.

## 5. Replay

The dependency-free replay was rerun successfully.  It reports identity on
all `2^ell` proper/full subsets plus one additional full-reversal state for
each `4<=ell<=10`, and confirms outer completeness at `m=2,ell=4`:

```text
PASS_AD_FOUR_RESOURCE_CYCLE_INTERNAL_OBSTRUCTION
payload_sha256=dad12307db4a0b61d024bc463edf24c0c45d47e1889d17c8591749c53082798c
```

No handoff or research-index file was edited by this audit.
