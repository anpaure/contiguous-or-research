# Audit of the cross-SCD sparse-top collar attachment theorem

**Date:** 2026-08-03  
**Status:** independent pure-mathematical audit; PASS.  No finite search or
solver computation is used.

The audited theorem is

```text
a4d954e2d35e6a17e24099a3b6d28b9731f6f7d47d5a14533dad9e29ca62359e
  MATH_THEOREM_CROSS_SCD_SPARSE_TOP_COLLAR_ATTACHMENT_20260803.md
```

## 1. General two-slab criterion

If a residual flag `F` is joined to a collar flag `D`, the two concatenate
to one inclusion flag exactly under the asserted order relation

\[
                         \operatorname{top}(F)
                         \subset\operatorname{bot}(D).
\]

The load is additive, so the edge condition
`|F|+|D|<=d` is exact.  Distinct matched collar flags have their already
distinct owners.  Therefore a legal simultaneous attachment is precisely a
matching saturating the residual-flag shore.  Hall gives the stated
all-subset condition, and the displayed rank is the standard transversal-
matroid rank formula.  No owner or capacity row is lost after the collar
bank has been fixed.

## 2. SCD chunk census

In an SCD of `B_(2r)`, a chain which contains any set below rank `r` passes
through every intermediate rank up to `r`.  Therefore:

1. for a residual rank block with top `s_j<r`, every nonempty chunk contains
   one rank-`s_j` top, and every rank-`s_j` set indexes exactly one chunk;
2. every collar chunk on ranks `t,...,r-1` ends at one rank-`r-1` set, and
   every rank-`r-1` set indexes exactly one such chunk; and
3. collar chunks meeting rank `t` are indexed by all rank-`t` sets and have
   exactly `r-t=a` members.

These statements remain true when the residual and collar chunks come from
different SCDs.  Thus the theorem's left and right matching shores have the
claimed complete-layer indexing.

## 3. Uniform containment Hall proof

A residual chunk whose top has rank `s` has

\[
                         {2r-s\choose t-s}
\]

rank-`t` socket neighbours.  Sending unit mass uniformly over them gives
unit load at the residual chunk.  A fixed socket contains `binom(t,s)`
rank-`s` tops, so its incoming load from one block is

\[
 {\binom ts\over\binom{2r-s}{t-s}}
 ={\binom{2r}s\over\binom{2r}t}
 ={p_s\over p_t}.                                      \tag{3.1}
\]

The sparse-top hypothesis makes the sum of (3.1) at most one.  This is a
fractional matching saturating every named residual chunk.  Integrality of
the bipartite matching polytope supplies an integral matching and therefore
proves all Hall cuts—not merely the total count.

## 4. Load and owner checks

Every matched socket contributes exactly `a` collar targets, while its
residual chunk contributes at most `h=d-a`.  Hence every combined load is at
most `d`.  Unmatched collar chunks start above rank `t` and are shorter.

Every completed flag has a distinct rank-`r-1` top.  The inclusion graph
from rank `r-1` to rank `r` has degrees `r+1` and `r`.  Edge counting gives

\[
                         (r+1)|X|\le r|N(X)|,
\]

so Hall injects all flag tops into rank-`r` owners.  Containment is
transitive, and every finite flag inside an owner extends to prefixes of an
owner ordering.  Thus the theorem is fully named, not merely a rank-pattern
statement.

## 5. Adjacent-band corollary

For the one block `{t-h,...,t-1}`, its top is `t-1`, its size is `h`, and

\[
                              p_{t-1}\le p_t
\]

because the Boolean rank sizes increase below the middle.  Hence it meets
the sparse-top hypothesis.  With `t=r-a` and `h=d-a`, the first selected
rank is `r-d`, and the total selected band has exactly `d` ranks.  The
corollary is therefore arithmetically and combinatorially exact.

## 6. Scope relative to the uniform-chain problem

The theorem does not partition the full Boolean lattice or even the full
strict lower ideal.  It allows unselected ranks, controls a maximum flag
load rather than floor/ceiling equality, and uses only one residual chunk
per rank-`t` socket.  Consequently it does not imply Füredi's uniform-chain
conjecture.

The density condition can fail when enough residual blocks are included to
cover the whole ideal.  The single-SCD linear-deletion barrier is therefore
untouched.  Full named chainization still requires multisocket attachment,
serial cross-chain splicing, or a collar decomposition chosen jointly with
the residual chunks.

The proof-safe new implication is exactly

\[
 \sum_jp_{s_j}\le p_t,quad |B_j|\le d-(r-t)
 \quad\Longrightarrow\quad
 \text{an exact named depth-}d\text{ residual--collar flag factor}.
\]
