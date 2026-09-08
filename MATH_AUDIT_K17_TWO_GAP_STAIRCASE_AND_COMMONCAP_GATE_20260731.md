# Independent audit of the K17 two-gap and common-cap theorem

Date: 2026-07-31  
Verdict: **PASS after scoped corrections**

Audited theorem:

```text
MATH_THEOREM_K17_TWO_GAP_STAIRCASE_OBSTRUCTION_AND_COMMONCAP_GATE_20260731.md
SHA256 2474febd5088da979aac1ade854f582bbf098b6acf4d1080feb8d9f0925c6e10
```

## 1. Symbolic two-gap audit

For a length-two run beginning at `s`, the following absent row has index
`s+2`.  If `s+3 <= alpha_1`, no start threshold has activated there, so the
run forces `tau_2 >= s`.  If `s+3 <= alpha_2`, at most one threshold has
activated, so it forces `tau_3 >= s`.  Substitution in the exact loss
identity and deletion of nonnegative terms gives

\[
\operatorname {Loss}\ge
2W-(\alpha_1-R_2(\alpha_1))-(\alpha_2-R_2(\alpha_2))
\ge2W-2G_2.
\]

The activation offset `s+3`, the final `+2` in the cyclic gap bound, and
the ceiling

\[
\left\lceil\frac{2(24310)-7401}{2}\right\rceil=20610
\]

are all correct.  The proof does not need a no-singleton hypothesis.

## 2. Independent literal replay

An independent run extractor, not importing the theorem's audit script,
replayed the authenticated cycle SHA

```text
39cc3abe6a8991dc101a585123989deab863030060c00d3e0a2a60cd73252de6.
```

It found

```text
total cyclic runs                  24310
length-two runs                     1063
length-three runs                   1829
minimum run length                     2
maximum run2 deleted by one cut        2
maximum short runs deleted by a cut    3
D1,D3,D4                         420,586,617
```

A separate all-cut event sweep gave

```text
max G2                              422
cuts attaining max                23889
cut-list digest       26c24e8b488485a0...
```

Thus the robust bound is `Loss >= 47444`, while the exact correlated bound
is `Loss >= 47776`; both exceed `Delta_17=7401`.

Fresh stdout from

```text
scratch/audit_k17_parent_cycle_nonflat_schedule_gap_20260731.py
```

is byte-identical to

```text
scratch/k17_parent_cycle_nonflat_schedule_gap_20260731.audit.json.
```

Their SHAs are respectively

```text
6af01349ffdd3789379d56f24f960f7db6bd4c79a6a9ff28c0d8fe322f028263
174ef8be813183584755d10c1691d47082cc450144d51a13631419f730656c90
```

and the internal JSON payload SHA recomputes to

```text
b577061f54f5d6f9fff9abcca57433cd2310bdb6edf57176584d449220e51d4f.
```

## 3. Residence and occurrence scope

The three quantifier classes are correctly separated.

1. The exact `G2` values concern all cyclic openings of one fixed owner
   order only.
2. The `605` wholly internal collars concern every permutation/reversal and
   port-flow completion of one fixed macro family, under a flat compiler.
3. The `165` empty clauses and exact optimum `180` concern every rank-six
   occurrence transversal of the fixed parent, again under the flat
   parent-induced architecture.

The odd-diamond identity is correctly scoped to nonconstant runs of length
at least two; singleton runs disappear and an all-one coordinate is the
exceptional cyclic case.  The current parent has minimum run four, so its
`1425` minimum runs become the `1425` child length-three packets.  The exact
residence optimum `180=12*15` and its independently verified `bound179`
DRAT certificate agree with the source theorem.

The occurrence-coherence ledger is also correct:

\[
\min\{\text{deleted upper-unique providers}\}
=\sum_Z(u_Z-1)^+.
\]

The current and octahedral marginal debts are `505` and `405`; the latter's
separate marginal residence optimum is `150`.  The theorem correctly makes
no assertion that `405` and `150` are attained by one transversal.

## 4. Common-cap audit

The maximal-cap equivalence is exact only with the final protected equation

\[
\bigcup_{p\in M_0(S)}Q_p(M)=S.
\]

That equation is present.  A preliminary protected-pin replay under the
precap does not suffice because residual assignments may later delete its
witness bits.

The five conflict families--cell collision, empty position, middle-bit,
protected-bit, and selected-lower-bit blockers--are jointly exhaustive.
The integral Hall system plus every minimal conflict cut is therefore
necessary and sufficient for the fixed fibre.

The rank scope is stated correctly.  For an unrestricted arbitrary-start
atlas the bounds are

```text
empty position       <= min(|bar E_p|, c_p)
middle blocker       <= |I_i|
protected blocker    <= |M_0(S)|
lower blocker        <= 1+|J|
```

and the empty-position bound is at most `17` globally, or `9` at a
rank-nine-row-covered position.  The sharper `6/4/3/4` depth-only profile
requires a separately proved length-at-most-three cell subatlas.  Thus the
note does not infer a generic LLL or total-unimodularity theorem from depth
alone.

Finally, the guarded-Hall theorem is constructive: its position guards and
literal hosts make every saturating matching common-cap safe.  The phrase
“pairwise matching-compatible” is explicitly local--distinct target parts
and distinct cells--and introduces no circular global extendibility
assumption.

## 5. Final implication boundary

The audited conclusion is exactly:

* this fixed cyclic order has no optimal monotone arbitrary-start/deadline
  staircase;
* this fixed parent has no flat occurrence-transversal child;
* a future chronology must export residence margin or compensation,
  occurrence/provider coherence, exact upper service, and one common-cap
  compiler.

It is not a global `K17` obstruction and proves no all-dimensional upper
bound.
