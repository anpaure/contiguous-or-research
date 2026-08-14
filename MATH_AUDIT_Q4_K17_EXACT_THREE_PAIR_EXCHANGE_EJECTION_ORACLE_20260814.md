# Hostile audit: exact q4 k17 three-pair ejection-signature oracle

**Date:** 2026-08-14

**Verdict:** **PASS** as a finite-pool algebra/pruning theorem.  It makes no
claim about the current owner pool.

## 1. Source

```text
MATH_REDUCTION_Q4_K17_EXACT_THREE_PAIR_EXCHANGE_EJECTION_SIGNATURE_ORACLE_20260814.md
sha256 202c2ee6efe5e5dcb5eb698a092e5de44f40acfe83c015a709d0920d3439ba63
```

## 2. Score identity

Square energy is quadratic.  Summing three individual signed changes adds
exactly `2<d_i,d_j>` for each of the three pairs and no third-order term.
Expanding `d_i=1_(N_i)-1_(P_i)` gives the source constant `c_R`, one score
`h_R(N_i)` per incoming mask, and the three incoming-overlap terms.  This
remains true when a row occurs in all three outgoing or incoming masks.

## 3. Distinct-candidate pruning

The face bound uses the three smallest scores at distinct candidate
indices.  For a prescribed candidate `N`, `mu_2(N)` excludes `N` and uses
two other distinct indices.  For a pair `N,M`, `mu_1(N,M)` excludes both.
Thus none of the cuts silently reuses one minimum candidate two or three
times.

Every discarded term is a nonnegative overlap or is replaced by an exact
exclusion minimum.  Therefore the face, candidate, pair, and third-candidate
cuts are all necessary conditions for negativity.  Ordering candidates as
`N<M<L` tests every legal incoming triple once.  A negative triple forces
all three candidate cuts, forces its canonical first pair through the pair
cut, and forces its third member through the strict final threshold.  The
ejection scan is complete.

## 4. Replay

```text
scratch/verify_q4_k17_exact_three_pair_exchange_ejection_oracle_20260814.py
sha256 610ce65f446e9974e3e16fe3aec1db5d198e2d0aad644afff4b0b3d082dbbc1a

scratch/verify_q4_k17_exact_three_pair_exchange_ejection_oracle_20260814.h100.out
sha256 89716cadfc61692412d94d4e793f9f1148013339c84f90c65f525d6141539310
status PASS
```

The H100 verifier exhausts 448 scalar identities and 131,040 synthetic
three-exchange scores.  Its random suite has 35,690 negative triples and
checks that the retained scan finds exactly that set; its exact-cover suite
has twenty nonvacuous dead faces.  All exclusion minima use distinct
candidate indices.

## 5. Scope

Only three reflected-pair replacements are covered.  The 35 self lifts are
fixed.  Mixed group-constrained triples, missing pair columns, neutral
pivots, and exchanges of depth at least four remain outside the theorem.
