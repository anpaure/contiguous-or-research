# Minimal-aperture rigidity and the `q`-reset pass; the serpentine wreath fails at its wrap

**Date:** 2026-08-13  
**Audited source:**
`/Users/amir.nuriyev/.codex/attachments/1ec502a8-a89e-4fdd-abba-f8aa5ccef83f/pasted-text.txt`  
**Status:** Theorems 1 and 2 pass.  Proposition 3 fails as written.

## 1. Minimal-aperture rigidity

Let

\[
 H_t=F\mathbin{\dot\cup}J_t,\qquad |J_t|=q,
\]

be a closed Johnson walk, where `F` is fixed and contains every constantly
positive coordinate.  Suppose every nonconstant positive run has length at
least `q`.

Each Johnson transition inserts exactly one coordinate absent just before
the transition, hence begins exactly one positive run.  Conversely every
nonconstant positive run begins at such an insertion.  There are therefore
exactly `ell` positive runs, counted with multiplicity, while

\[
 \sum_{\rho}|\rho|=\sum_t|J_t|=q\ell.
\]

Since every summand on the left is at least `q`, all have length exactly
`q`.  If `x_s` is the entry at transition `s`, then

\[
 J_t=\{x_{t-q+1},\ldots,x_t\}.                     \tag{1}
\]

This remains valid when a physical label enters several times in one
closed walk: (1) is a statement about entry events, and the `q` simultaneous
labels are distinct because `J_t` is a set of size `q`.

For a legal pure rail, the entry word is a cyclic order of `m` distinct
toggle points.  If `m>=q+2`, the union of adjacent owners is

\[
 U_t=F\cup\{x_{t-q+1},\ldots,x_{t+1}\}.            \tag{2}
\]

These are cyclic intervals of length `q+1<m` in a distinct-label cyclic
order.  Two such intervals cannot have the same underlying set.  This also
covers the boundary case `m=q+2`, where the intervals are co-singletons,
and `m=2q`.

It follows that equality of the literal width-two union currents of two
edge subsets on one rail forces equality edge by edge.  For a compound
bank, every changed edge must be paired with a changed edge, necessarily
on another rail, having the same literal rank-`R+1` union.  Thus

\[
 \chi_U(E_0)=\chi_U(E_1)\qquad
 (U\in{[k]\choose R+1})                            \tag{3}
\]

is a genuine character of the actual closed-rail columns.  Its precise
scope is important: it rules out a nontrivial zero-all-width switch
supported on one minimal-aperture pure rail.  It is not by itself a global
positive-semigroup obstruction, because equal-`U` edges on different cores
may cancel.

## 2. The shielded `q`-reset

For disjoint ordered `q`-sets

\[
 \alpha=(a_1,\ldots,a_q),\qquad Z=(z_1,\ldots,z_q),
\]

the owners

\[
 X_t=F\cup\{a_{t+1},\ldots,a_q,z_1,\ldots,z_t\},
 \qquad0\le t\le q,                                \tag{4}
\]

form a simple Johnson path.  The immediate lower and upper sets displayed
in the candidate are correct and pairwise distinct.  For every interval,

\[
 \bigcup_{j=s}^{t}X_j
 =F\cup\{a_{s+1},\ldots,a_q,z_1,\ldots,z_t\}.       \tag{5}
\]

If a predecessor `K` obeys `K union X_0=U`, then every `a_i` is already in
`U`, so the crossing-prefix formula

\[
 K\cup X_0\cup\cdots\cup X_t
 =U\cup\{z_1,\ldots,z_t\}                          \tag{6}
\]

is independent of the ordering of `alpha`.

The path (4) is exactly the consecutive-window segment of the toggle word

\[
 a_1\cdots a_qz_1\cdots z_q.
\]

Extend this to a cyclic order of `m>=2q` distinct toggles.  Each toggle has
one positive run of length exactly `q` and one zero gap of length
`m-q>=q`.  Hence the reset satisfies both positive and dual residence.
Owner and palette injectivity also hold at `m=2q`.  Theorem 2 is therefore
proof-safe.

The later zero-current braid equations remain conditional equations; the
reset theorem does not solve them.

## 3. Exact failure of the serpentine wrap

Proposition 3 puts

\[
 c_i=-i\pmod{2q},\qquad i\in\mathbb Z_q,
\]

and claims that the filler windows agree on every transition

\[
 (i,\varepsilon,q-1)\longrightarrow
 (i+1,1-\varepsilon,0).                            \tag{7}
\]

For a nonwrap transition, `c_(i+1)=c_i-1` modulo `2q`, and the claim is
correct.  At the wrap `i=q-1 -> 0`, however,

\[
 c_{q-1}=q+1,\qquad c_0=0.
\]

The old filler start in (7) is

\[
 c_{q-1}+\varepsilon q+q-1
 \equiv \varepsilon q\pmod{2q},
\]

whereas the new filler start is

\[
 c_0+(1-\varepsilon)q
 \equiv(1-\varepsilon)q\pmod{2q}.                 \tag{8}
\]

The two values in (8) differ by `q` for both choices of `epsilon`.  Since
the filler windows have length `q-1` on a `2q`-cycle, these two windows are
disjoint.  The wrap transition changes the base Johnson coordinate and
all `2(q-1)` filler incidences, so it is not a Johnson edge.

This is not a removable indexing typo within the proposed ansatz.  Equality
of fillers on (7) forces

\[
 c_{i+1}=c_i-1\pmod{2q}
\]

at every base transition.  After `q` transitions it would force
`c_0=c_0-q (mod 2q)`, impossible.  Therefore the claimed cyclic serpentine
wreath and all conclusions depending on it are unproved.  A repair needs
an additional reset seam, a doubled base period, or a different filler
monodromy, followed by new residence and all-width audits.

## 4. Proof-safe boundary

The attachment contributes two valid results:

1. minimal-aperture resident pure rails are literal shift registers and
   have an injective width-two union map; and
2. a terminal phase can be flushed through a literal resident `q`-step
   reset.

It does not supply the promised aperture-`q+2` all-width actuator, because
the proposed serpentine cycle is not a Johnson walk at its wrap.  Any use
of the reset in an actuator also remains conditional on solving the stated
phase-refined braid equations.
