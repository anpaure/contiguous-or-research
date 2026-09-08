# Independent audit: hybrid clipped-resident common-core reservoir

**Date:** 2026-08-04  
**Verdict:** **FINAL GO**, with two notational/quantifier corrections made
before freezing.  The theorem proves an unconditional asymptotic protected
path bank with internal positive residence and pairwise-disjoint owner,
immediate-lower, and immediate-upper resources.  It does **not** prove a
spanning-factor extension, global cyclic residence, endpoint-collar
compatibility, component distribution, or common-cap feasibility.

No search, solver, sampled experiment, or H100 computation was used in this
audit.

## 1. Frozen inputs

| role | file | SHA-256 |
|---|---|---|
| audited theorem | `MATH_THEOREM_COMMON_CORE_HYBRID_CLIPPED_RESIDENT_WITNESS_RESERVOIR_20260804.md` | `f9cd82ff39c3fb6979bd2c70e92223af6f7bb171d4ede422a023b7d2c6809314` |
| frozen reservoir dependency | `MATH_THEOREM_COMMON_CORE_UPPER_DAMAGE_AND_DISJOINT_WITNESS_RESERVOIR_20260804.md` | `3aaaf6388256954b2579581353f3c1e456198d6f7a4ebd0a9de951945695f983` |

## 2. Corrections made before the verdict

The mathematical construction survived unchanged.  Two proof-presentation
issues were corrected.

1. The old symbol `B_m` minimized the three binomial coefficients for one
   target-dependent value `N=2m-h-1`, but was subsequently used uniformly
   over all `1<=h<=d`.  It is now the genuinely uniform quantity

   \[
   \underline B_m=
   \min_{1\le h\le d}\min_{r\in\{m-1,m,m+1\}}
   {2m-h-1\choose r}.
   \]

2. The asymptotic quantifier `d=O(sqrt(m))` is now explicit: for every fixed
   `C`, the conclusion holds for all sufficiently large `m` whenever
   `1<=d<=C sqrt(m)`, with the threshold allowed to depend on `C`.

The audit also added the direct clipped-residence check after the canonical
ring rethread.  This strengthens the exposition but is not needed for the
pre-rethread packing theorem.

## 3. Low paths: rank, union, simplicity, and residence

Fix a noninterval trace `T` of size `q` in the low range and put
`h=m-q>=d+1`.  The `q` windows

\[
 W_j=\{k_j,\ldots,k_{j+h-1}\},\qquad 0\le j\le q-1,
\]

do not wrap because their final index is

\[
 (q-1)+(h-1)=m-2=|K|-1.
\]

Therefore `V_j=T union W_j` has rank `q+h=m`, and

\[
V_j\setminus V_{j+1}=\{k_j\},\qquad
V_{j+1}\setminus V_j=\{k_{j+h}\}.
\]

The immediate lower and upper colours are respectively

\[
 T\cup\{k_{j+1},\ldots,k_{j+h-1}\},
 \qquad
 T\cup\{k_j,\ldots,k_{j+h}\},
\]

of ranks `m-1` and `m+1`.  Their starting positions distinguish them.  The
span of all windows has length `h+q-1=m-1`, so their union is all of `K`
and the path union is exactly `K union T`.

For a fixed `k_s`, its occurrence indices are

\[
[s-h+1,s]\cap[0,q-1].
\]

If this run meets neither endpoint of the path, neither clipping operation
is active and its length is exactly `h>=d+1`.  Every coordinate of `T`
occurs throughout.  This proves precisely the stated **positive
`d`-clipped residence**, with endpoint runs exported rather than silently
claimed to be globally resident.

For a two-owner path, every nonempty positive run meets at least one of its
two endpoints, so the clipped condition is automatic.  In the actual
full-size damage family, a noninterval `q=2` trace is absent anyway: a
two-set containing a cyclic hinge edge equals that edge and is a cyclic
interval.

All resources on one low path have exact external trace `T`.  Distinct
noninterval traces therefore separate different low paths in all three
ranks, and no low resource equals a top-bank resource, whose external trace
is cyclic-interval.

## 4. High monotone geodesics

For `q=m-h`, `1<=h<=d`, one has

\[
N=|K\cup T|=2m-h-1=(h+1)+2(q-1).
\]

Thus the partition `Z=C dotcup X dotcup Y` has the asserted sizes.  Each

\[
A_t=C\cup\{x_{t+1},\ldots,x_{q-1}\}
       \cup\{y_1,\ldots,y_t\}
\]

has rank `(h+1)+(q-1)=m`, and the transition `A_t -> A_(t+1)` deletes
`x_(t+1)` and inserts `y_(t+1)`.  The path is simple because
`|A_t cap Y|=t`.  Its union is `C union X union Y=Z`.

Every `x` has one initial positive run, every `y` one terminal positive run,
and every element of `C` occurs throughout.  Hence no coordinate has an
internal positive run; the path is clipped-resident for every `d`.

## 5. Exact hitting probabilities

Choosing `C` uniformly and then uniformly ordering `Z setminus C` is
invariant under the full symmetric group of `Z`.  At each fixed owner
position, this makes `A_t` uniform on `binom(Z,m)`.  Since the `q` owner
positions are pairwise distinct,

\[
 \Pr(O\text{ is used})={q\over{N\choose m}}.
\]

At edge `t`, the lower colour contains exactly `t` members of the selected
set `Y`, while the upper colour contains exactly `t+1`; therefore the
`q-1` colours in either palette are pairwise distinct.  Symmetry makes each
fixed edge-position marginal uniform on the appropriate rank, and summing
the disjoint events gives

\[
 \Pr(L\text{ is used})={q-1\over{N\choose m-1}},\qquad
 \Pr(U\text{ is used})={q-1\over{N\choose m+1}}.
\]

These are exact probabilities, not merely upper bounds.  Resources not
contained in the target ground set `Z` have probability zero.

## 6. Uniform entropy and target counts

The number of high traces is at most

\[
H_d=\sum_{h=1}^d {m\choose h}
\le(d+1)(em/d)^d=2^{o(m)}
\]

uniformly for `d<=C sqrt(m)`.

For `N_h=2m-h-1`, `r in {m-1,m,m+1}`, and `p=r/N_h`, the index `r` is a
mode of `Bin(N_h,p)`.  Consequently its probability is at least
`1/(N_h+1)`, which gives

\[
{N_h\choose r}\ge {2^{N_h H_2(p)}\over N_h+1}.
\]

Writing `p=1/2+t` gives `|t|<=(h+3)/(2N_h)`.  The inequality

\[
H_2(1/2+t)\ge1-6t^2\qquad(|t|\le1/4)
\]

is valid: the difference is even, vanishes with derivative zero at the
origin, and has second derivative

\[
12-{1\over\ln 2\,(1/4-t^2)}>0
\]

throughout `|t|<=1/4`.  Since `h<=d`, both the linear loss `h` and the
quadratic entropy loss are maximized safely by `d`.  This verifies the
uniform bound

\[
\underline B_m\ge {1\over2m}
2^{2m-d-1-3(d+3)^2/(2(2m-d-1))}=2^{2m-o(m)}.
\]

## 7. Sequential greedy packing

Before any high path is selected, the number of forbidden resources at
each of the three ranks is at most

\[
m^2+m2^m+O(m)+mH_d.
\]

For all sufficiently large `m` this is bounded by

\[
R_m=4m(2^m+H_d).
\]

The same bound remains valid at every sequential step because `H_d`
already counts every possible earlier high target.  For the current target,
the exact hit probabilities and a union bound give

\[
\Pr(\text{some collision})
\le {3mR_m\over\underline B_m}
=2^{-m+o(m)}<1.
\]

Thus a legal high geodesic exists at every step.  Induction yields a
simultaneous bank.  The forbidden set contains all prior owners, immediate
lower colours, and immediate upper colours, so the conclusion is genuinely
pairwise disjoint in all three resource ranks.  It also contains the full
top and low banks and any separately specified `O(m)` hinge bank.

## 8. Interaction with the ring hinges

In the canonical full-size realization, each hinge is already the first
edge of its top path, so it is retained rather than separately duplicated.
Every low private resource is disjoint from the top bank by its noninterval
external trace.  Every high private resource is chosen to avoid the top
bank by the greedy construction.  Hence the ring rethread changes no
private path.

For a transported top path beginning `L_i,R_(i+1)`, the coordinate `b`
occurs only at the first endpoint, the other `K` coordinates occur in
initial runs, `a_i` occurs throughout, and the remaining external
coordinates occur in terminal runs.  Thus the rethread preserves clipped
residence as well as the prefix-union witnesses proved in the frozen
dependency.

## 9. Fail-closed scope

The verified conclusion is local and asymptotic.  It supplies a
pairwise-resource-disjoint, internally positive-resident witness path for
every possible common-core upper-damage target, uniformly for
`d<=C sqrt(m)` and sufficiently large `m`.

It does **not** establish any of the following:

- a spanning two-factor containing the bank;
- the protected weighted Ore--Ryser inequalities;
- that endpoint runs close into globally legal cyclic residence runs;
- compatible endpoint collars;
- that the distinguished hinges lie on separate factor components;
- a forest complement, connected carrier, or common cap;
- the all-dimensional `B(k)+O(1)` theorem by itself.

Subject to exactly this scope, the theorem is **FINAL GO**.
