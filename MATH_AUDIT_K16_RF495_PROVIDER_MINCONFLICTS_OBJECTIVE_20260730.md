# K16 repeat-free 4/9/5 provider-choice min-conflicts objective

This note audits the objective used by
`scratch/search_k16_provider_choice_minconflicts_20260730.cpp`.  It is a
witness-only search over the authenticated seed5-by-seed5 atlas.  A timeout
has status `UNKNOWN` and has no negative mathematical meaning.

## Exact quotient

The two fixed bodies leave 70 residual targets.  For each target `T` and each
of the 70 contiguous editable-cell supports `Q`, the physical atlas has one
or more fixed ORs `F`.  The atlas audit proves that this class has a unique
greatest member `F*(T,Q)`.  Replacing a row `(T,F,Q)` by `(T,F*,Q)` preserves
feasibility: `F subset F* subset T`, so any cells realizing the former also
realize the latter.  Conversely `(T,F*,Q)` is itself a physical interval.
Thus the exact quotient has `70*70=4900` choices.

## Maximal-intersection state

Choose one support `Q_T` for every residual target.  The selected row imposes
`x_p subset T` for each `p in Q_T`.  Hence every realization is bounded by

```
U_p = intersection { T : p in Q_T },
```

where an empty intersection is the full 16-bit mask.  Every physical cell
must be nonempty.  For a selected provider, define

```
D_T = T \ F*(T,Q_T).
```

The selected family is realizable exactly when

```
U_p != 0                                        for every editable p,
D_T subseteq OR { U_p : p in Q_T }              for every residual T.
```

Necessity is immediate.  For sufficiency take `x_p=U_p`.  Every participating
`U_p` is a submask of `T`, while the displayed demand condition supplies all
bits not already in the fixed OR, so the corresponding literal interval OR
is exactly `T`.  This also proves maximality: if any assignment realizes the
chosen providers, the componentwise maximal assignment does as well.

## Score and delta interpretation

For bit `b` and editable position `p`, let

```
c[b,p] = #{ T : b notin T and p in Q_T }.
```

Then `b in U_p` exactly when `c[b,p]=0`.  The hard score is the exact sum of

1. the number of positions `p` for which all sixteen `c[b,p]` are positive;
2. for every selected target, the number of demanded bits `b in D_T` for
   which `c[b,p]>0` at every `p in Q_T`.

Changing one target choice from `Q` to `Q'` changes `c[b,p]` only for
`b notin T` and `p in Q symmetric-difference Q'`.  In particular, a support
bit is created only at a `1->0` blocker transition and destroyed only at a
`0->1` transition.  This is the dependency graph used by the ejection-chain
and ruin/refill moves; no Boolean-cell SAT variables are present.

The implementation additionally scans all 70 physical providers of every
residual target under the maximal cells.  This physical score is used as a
tie guide and as the acceptance gate.  A candidate is written only when all
18 cells are nonzero and every residual target has some exact physical
provider.  It is then inserted into the frozen 12,873-cell word and replayed
over all 65,535 nonempty masks in C++.  The H100 runner invokes the separate
`scratch/verify_exact_or_word.py` afterward.  It does **not** require a flat
middle derivative row: the authenticated repeat-free marked-parent fibre has
one fixed child jump, and literal universality at the proved length `B(16)` is
the sufficient and necessary acceptance statement.  The verifier still
records middle-row exactness as a diagnostic field.

## Authenticated seed5 inputs

At staging time the bound inputs were:

```
residual_witness_incidence.tsv  a3ca5b14a5e6286cbcb96e6ca3c827979a525f697eabf6f0704c4fcde982113c
lead_score3.cells               6f90ca3f682ad1565977d53f0d3a30496ae01f38a7816f411375e5f6b415745c
lead_score3.word                9771f928d2a405308eabbbc780a2f810f77d8faef4f10d56cbb4e50381f518d6
```

The frozen seed4 S4 fibre is not searched here: it is already excluded by
the fixed-ghost/deadline theorem in handoff item 2015.  This lane is scoped
only to the repeat-free seed5 self-pair 4/9/5 fibre in item 2016.
