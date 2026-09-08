# K17 c7be U-shore internal single-reversal opposite-core no-go

Date: 2026-07-31  
Status: solver-free exhaustive theorem for one fixed parent and one exact rethread class

## 1. Scope

Let `T` be the authenticated c7be K16 rank-eight chronology

```text
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
SHA c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906
```

and put

\[
 q_e=T_e\mathbin\lor T_{e+1}\qquad(0\le e<12869).
\]

Every rank-nine mask occurs among the `q_e`.  A U-shore occurrence
transversal chooses exactly one occurrence of every one of these 11,440
colours and orders the chosen colours by their physical edge positions.

This note considers exactly the chronologies obtained by reversing one
**internal** inclusive vertex block `[l,r]`, where

\[
 1\le l<r\le12868,
\]

subject to both new boundary joins being Johnson edges and all 11,440 q1
colours remaining present.  Prefix reversals, suffix reversals, two-block
rethreads, split/interleaved moves, and arbitrary parent chronologies are not
part of this theorem.

## 2. Exact incremental quotient

For a reversal `[l,r]`, every internal old edge survives with transformed
position

\[
 e\longmapsto l+r-1-e\qquad(l\le e<r).
\]

Only old edge positions `l-1` and `r` are deleted.  They are replaced at the
same positions by

\[
 T_{l-1}\lor T_r,\qquad T_l\lor T_{r+1}.
\]

Thus Johnson legality and full q1-palette preservation are decided from two
literal seam joins and a four-colour multiplicity delta.  No full K17 SAT or
compiler model is involved.

## 3. Exact interval formula

Fix an old-coordinate upper target `X`.  For every raw edge interval `I`, let
`sel(c,e)` mean that occurrence `e` is the unique selected occurrence of q1
colour `c`.  The interval witnesses `X` exactly when

1. every selected colour in `I` is a submask of `X`; and
2. for every bit of `X`, some selected submask colour in `I` carries it.

Equivalently its exact selector formula is

\[
 \bigwedge_{\substack{e\in I\\q_e\not\subseteq X}}
     \neg\operatorname{sel}(q_e,e)
 \quad\wedge\quad
 \bigwedge_{b\in X}
 \bigvee_{\substack{e\in I\\q_e\subseteq X\\b\in q_e}}
     \operatorname{sel}(q_e,e).                 \tag{3.1}
\]

Intervals containing the sole occurrence of a bad colour are impossible.
Those immutable bad events split the stream into exact independent candidate
gaps.  Every genuine witness trims to its first and last selected good event,
so enumerating pairs of good raw endpoints inside these gaps is complete.
Equal formulas are merged.  If formula `B` has a superset of the blockers of
`A` and each carrier row of `A` is implied by a carrier row of `B`, then
`B => A`, so `B` is safely deleted from the witness disjunction.

Crucially, (3.1) is rebuilt from the rethreaded occurrence domains for every
candidate.  No forced literal from the unrethreaded c7be chronology is
transported by assumption.

## 4. Two opposite-occurrence cores

The source control regenerates the two exact disjoint pairs

| targets | shared q1 colour | forced source occurrences |
|---|---:|---:|
| `0x0ff5`, `0x1bf5` | `0x0bf5` | `10616`, `9176` |
| `0x1def`, `0x3de7` | `0x1ce7` | `12799`, `12814` |

In each row, simultaneous coverage is impossible when the displayed forced
occurrences remain the only compatible witnesses, because a transversal
selects the shared colour exactly once.

For each rethread the audit regenerates all exact formulas for these four
targets and tests exact-one compatibility.  A target with no formula is an
even stronger individual obstruction.

## 5. Exhaustive result

There are exactly 19,856 nontrivial internal reversals satisfying both
Johnson seam tests and the complete-palette test.  Their exact classification
is

| outcome | count |
|---|---:|
| both opposite-pair obstructions persist | 19,779 |
| only the `0x0bf5` pair persists | 60 |
| only the `0x1ce7` pair persists | 17 |
| both pairs become compatible | 0 |

The classes partition all 19,856 candidates.

### Theorem 5.1

No internal single-block reversal in the scope of Section 1 admits a U-shore
occurrence transversal covering every old-coordinate target of ranks at least
ten.

### Proof

The quotient of Section 2 exhausts the class.  For every retained chronology,
the exact formula enumeration of Section 3 shows that at least one of the two
opposite-occurrence pairs in Section 4 remains incompatible.  The four class
counts in Section 5 sum to 19,856, and the compatible class is empty.
Therefore every U shore misses at least one required strict-upper target.
\(\square\)

## 6. Audit and hashes

```text
scratch/audit_k17_u_single_reversal_quotient_20260731.py
SHA 43521afdc3c3ef0afb3e2ae321282a6a1b2098f998c8ec01d114d22f1babd15c

scratch/k17_u_single_reversal_quotient_20260731.audit.json
SHA bc1d4dbc871b30907b277d47817c2b9f74b671d201176da77134cb22ef051229
payload e44b3421119f8823631ee8cf89ee0bdf529124137129b44dae43ddf4c8f7ab78

candidate-row SHA
37ac0075b6104d78cfdac88104b6353db8637319a3c23b4c5746bb355f7941f1
```

The audit replays byte-identically and calls no SAT, BDD, DP, or external
solver.

## 7. Nonclaims

This is a source-relative upper-U obstruction.  It is not a K17 no-go.  It
does not decide one-ended reversals, two-block rethreads, interleavings, a
different rank-eight parent, a depth-three K17 middle schedule, or the lower
common-cap compiler.
