# Independent audit of the selected-boundary obstruction note

## Artifact and verdict

Audited artifact:

`SELECTED_BOUNDARY_GRAPH_OBSTRUCTION_20260724.md`

SHA-256 after the one correction described below:

```text
5349f2fa9eb8f7f6b7ca3b43c01ab73c3a8221c275e5da5d09198a07a3fac4ea
```

Reference definitions were checked against
`MULTIDEPTH_SAFE_SPLICE_THEOREM_20260724.md`, SHA-256

```text
3438c99d862c92b68ba6a463bc1fc19551c26d9753541582e9e3c37568beaf8e
```

**Verdict: valid after one necessary local hypothesis correction.**  The
directed-flag law, the exact `A_1` ledger, both zero-arc constructions, the
random-cut first moment, the pointwise removal-word theorem, and the
setwise-to-pointwise induction are correct under their stated separation
and injectivity hypotheses.  They establish an obstruction/reduction, not
the full constant-one construction.

## 1. Correction found during the audit

The original version of Theorem 2.1 did not explicitly require its two
directed occurrences to come from distinct selected undirected edges.  In
that version there is a genuine degenerate counterexample.  Take `M=L` and
let the target head be `L+c`.  Then

```text
(L+a) intersect (L+c) = L,
(L+a) union     (L+c) = L+a+c,
```

so the mixed flag identities hold, although `c` is not in `L` and (2.2)
does not hold.  This includes the repeated-occurrence case when `c=b`.

The theorem now explicitly assumes distinct selected undirected edges,
hence `L!=M` by global lower rainbowness.  Its proof now retains both
algebraic cases and excludes `M=L` using that premise.  This premise is
automatic for the cross-component arcs to which the theorem and ledger
are applied.

As a finite sanity check, exhaustive enumeration gave:

```text
m=2: 48 mismatches without L!=M, 0 with L!=M
m=3: 540 mismatches without L!=M, 0 with L!=M
```

No other correction was required.

## 2. Directed depth-one law and exact arc ledger

Write the source tail and target head as

```text
A = L+a,
B = M+c.
```

The equality `A intersect B=L` implies

```text
B=L+d
```

for a unique `d` outside `L union {a}`.  Since `c` is not in `M`, either
`c=d` and `M=L`, or `c in L` and

```text
M=L-c+d.
```

The corrected distinct-edge premise excludes the first alternative.  In
the second alternative the upper equality is automatic:

```text
M+a+c = L+a+d = A union B.
```

This proves both directions of (2.2).  If source and target components are
vertex-disjoint, `d=b` would make the target head `L+d` equal the source's
old head `L+b`; hence `d!=b` is indeed automatic.

For a fixed target flag `(M,c)` removing `a`, solve (2.2) for the source
lower colour:

```text
L=M-d+c,  d in M.
```

Different `d` give different `L`, and global lower rainbowness makes the
projection from a selected directed occurrence to `L` injective.  Thus

```text
sum_a sum_(M,c in F_a) |{d in M : M-d+c in S_a}|
```

counts every ordered compatible occurrence pair exactly once.  Removing
pairs whose occurrences are in the same current component gives exactly
the cross-component quantity `A_1`; there is no missing factor of two.

## 3. The two zero-arc obstructions

For fixed `a!=x`, the family indexed by

```text
L in binom([2m] minus {a,x},m-1)
```

has endpoints `L+a` and `L+x`.  Same-side endpoint equality forces equal
`L`; cross-side equality is impossible because one side contains `a` and
omits `x`, while the other does the reverse.  Hence the selected Johnson
edges are vertex-disjoint.  Their lower and upper colours are injective.

Every directed occurrence removing `a` inserts `x`, while every possible
source lower colour omits `x`; Theorem 2.1 therefore forbids every such
arc.  The argument with `a,x` exchanged handles the reverse orientations.
The exact size and ratios are

```text
binom(2m-2,m-1),
binom(2m-2,m-1) / binom(2m,m) = m/[2(2m-1)] -> 1/4,
binom(2m-2,m-1) / binom(2m-1,m-1) = m/(2m-1) -> 1/2.
```

For Proposition 3.2, the antipodal law
`z_(t+ell)=pi(z_t)` makes every transition pair exactly
`{z_t,pi(z_t)}`.  A directed occurrence removing `a` therefore inserts
`pi(a)`, while its lower colour omits both.  The target label required by
Theorem 2.1 can never lie in a source lower colour.  This proves the
zero-arc claim for every subfamily; restricting to vertex-disjoint or
rainbow members cannot create an arc.  The proposition correctly makes no
near-perfect-matching claim for the fixed-`pi` family.

## 4. Random-cut normalization

A `2ell`-edge undirected cycle has `4ell` directed cut occurrences.  An
ordered compatible occurrence arc specifies one occurrence on each of two
distinct cycles.  Independent uniform directed cuts select that ordered
pair with probability

```text
1/(4ell)^2 = 1/(16ell^2).
```

Summing the occurrence-arc indicators proves (4.1).  The formula is an
exact first moment only; the note correctly does not infer a long path
forest without cycle-level degree and codegree control.

## 5. Pointwise multidepth compatibility

The proof uses the following standard consequence of transition
separation.  On a separated path segment,

```text
intersection = starting set minus all removals,
union        = ending set plus all removals.
```

All displayed removal sets are disjoint from the relevant starting or
ending set, so equality of shadows is equivalent to equality of those
removal sets; no insertion data are missing.

For a lower crossing window `(q,r)`, the source-prefix removals are common
to the old and cross paths.  Cancelling them gives exactly

```text
{r_*, r^j_0, ..., r^j_(q-r-1)}
  = {r^i_-1, r^i_0, ..., r^i_(q-r-1)}.                 (L)
```

For an upper crossing window, use the common target endpoint and cancel
the common post-cut target removals.  This gives exactly

```text
{r^i_-r, ..., r^i_-2, r_*}
  = {r^j_-r, ..., r^j_-1}.                             (U)
```

In (L), `r=q` gives `r_*=r^i_-1`; then `r=1` and
`q=2,...,H` successively give equality at indices `0,...,H-2`.  In (U),
`r=1,...,H` successively gives `r_*=r^j_-1` and equality at indices
`-2,...,-H`.  These are precisely the `2H-1` common removal coordinates

```text
-H,-H+1,...,-1,0,...,H-2.
```

Conversely, substituting that word equality into (L) and (U) proves every
pointwise identity.  The actual cross edge and the old/spliced separation
hypotheses are essential and are present in the theorem's setup.

## 6. Setwise signatures

Corollary 5.2 is also correct; equality of unordered signatures does not
introduce a hidden permutation freedom.

At depth one, the singleton signatures give both cut-removal equalities.
Assume the removal word is already matched through depth `q-1`.  At lower
depth `q`, the cross windows with `r>=2` use target post-cut removal indices
only through `q-3`; hence those `q-1` windows already equal the old source
windows with the same `r`.  Internal injectivity makes them `q-1` distinct
members of the old `q`-set.  Set equality forces the sole remaining
`r=1` windows to agree, yielding equality at index `q-2`.

Dually, at upper depth `q`, the windows with `r<=q-1` use only already
matched negative indices.  They agree pointwise and exhaust `q-1`
distinct old windows.  The remaining `r=q` equality yields equality at
index `-q`.

This induction uses internal injectivity at every old and cross signature;
without it the statement would not follow.  Corollary 5.2 states this
hypothesis explicitly, and the strong seam condition supplies it in the
intended cyclic-strip application.

## 7. Scope conclusion

The note proves that the ownership/rainbow marginals alone do not force a
selected boundary forest and that exact multidepth inheritance forces a
common transition word.  It leaves open the advertised soft-gain route.
Nothing in the audited artifact proves the full asymptotic coefficient-one
theorem or the finite shortest-array objective by itself.
