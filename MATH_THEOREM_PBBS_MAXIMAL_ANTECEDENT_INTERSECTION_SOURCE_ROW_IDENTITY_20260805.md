# Maximal-antecedent row identity: the top `d` lower fan layers are literal source cells

**Date:** 2026-08-05  
**Method:** coordinate-run intervals; no computation or search  
**Status:** unconditional for a cyclic `d`-resident owner trace.  Every
intersection of at most `d+1` consecutive owners is exactly one contiguous
source union in the maximal antecedent.  Hence any exact owner-intersection
fan through depths `1,...,d` lifts occurrence-injectively to ordinary source
cells.  This removes target-to-cell matching for those layers.  It does not
by itself protect the cells against later deletions made to realize deeper
targets, and it does not supply a typed suffix router.

## 1. Set-up

Let

\[
                         T=(T_i)_{i\in{\mathbb Z}_W}             \tag{1.1}
\]

be a cyclic set trace, with `0<=d<W`.  Assume every cyclic coordinate-presence component
is either the whole cycle or has length at least `d+1`.  Define its maximal
depth-`d` antecedent by

\[
                         P_p=\bigcap_{t=0}^{d}T_{p-t},
                         \qquad p\in{\mathbb Z}_W.              \tag{1.2}
\]

All indices below are cyclic.  A nonconstant positive run containing the
segment under discussion may be unwrapped to an ordinary integer interval;
the constant-coordinate case is immediate.

## 2. Exact row identity

### Theorem 2.1 (intersection-to-source row identity)

For every `0<=q<=d` and every `i`,

\[
 \boxed{
 \bigcap_{j=0}^{q}T_{i+j}
   =\bigcup_{h=q}^{d}P_{i+h}.}                                \tag{2.1}
\]

In particular, at `q=0`,

\[
                         \bigcup_{h=0}^{d}P_{i+h}=T_i,          \tag{2.2}
\]

so `D^dP=T`.

#### Proof

Fix a coordinate `x`.

If `x in P_(i+h)` for some `q<=h<=d`, then `x` belongs to every owner in

\[
                         [i+h-d,i+h].                          \tag{2.3}
\]

Because `h<=d` and `h>=q`, this interval contains `[i,i+q]`.  Hence `x`
lies in the left side of (2.1).

Conversely, suppose `x` lies in every owner `T_i,...,T_(i+q)`.  Unwrap the
positive run of `x` containing this segment as `[a,b]`.  Thus

\[
                         a\le i,
                         \qquad b\ge i+q,
                         \qquad b-a\ge d.                      \tag{2.4}
\]

Choose

\[
                         h=\max\{q,a-i+d\}.                    \tag{2.5}
\]

The inequalities `a<=i` and `q<=d` give `h<=d`.  Also `q<=b-i`, while
`a-i+d<=b-i` follows from `b-a>=d`; hence `h<=b-i`.  Therefore

\[
                         [i+h-d,i+h]\subseteq[a,b].            \tag{2.6}
\]

Thus `x in P_(i+h)` for some `h in [q,d]`, proving the reverse inclusion.
`square`

### Corollary 2.2 (Johnson ranks)

Suppose in addition that `T` is a simple rank-`r` Johnson trace.  Then for
`0<=q<=d`,

\[
 \left|\bigcap_{j=0}^{q}T_{i+j}\right|=r-q.                   \tag{2.7}
\]

#### Proof

Each of the `q` Johnson transitions deletes one coordinate.  Those deleted
coordinates are distinct: deleting the same coordinate twice would require
reinserting it between the two deletions, producing a positive run of at
most `q<=d` owners.  Likewise, a coordinate inserted inside the segment
cannot be deleted again inside it.  Hence precisely `q` distinct coordinates
of `T_i` are absent from the total intersection. `square`

## 3. Occurrence-injective lift of the top lower fan

For `0<=q<=d`, define the source interval

\[
                         J(i,q)=[i+q,i+d].                     \tag{3.1}
\]

Theorem 2.1 says

\[
                         \bigcup_{p\in J(i,q)}P_p
                         =\bigcap_{j=0}^{q}T_{i+j}.            \tag{3.2}
\]

The pair `(i,q)` is determined by the cyclic interval `J(i,q)`: its terminal
index is `i+d` and its length is `d-q+1`.  Therefore distinct selected fan
occurrences give distinct physical source intervals.  More generally,
distinct exact target values could not share one physical interval because
that interval has a single union value.

### Corollary 3.1 (top-`d` source-cell SDR)

Assume the owner trace carries an occurrence-injective intersection fan:
for every target `S` of rank `r-q`, where `1<=q<=d`, choose one pair `(i,q)`
with

\[
                         S=\bigcap_{j=0}^{q}T_{i+j}.            \tag{3.3}
\]

Then

\[
                         S\longmapsto J(i,q)                   \tag{3.4}
\]

is an occurrence-injective ordinary source compiler for all ranks

\[
                         r-d,r-d+1,\ldots,r-1                  \tag{3.5}
\]

inside the single maximal antecedent `P`.

Thus, once the rigid all-depth owner-intersection bank has been fixed, no
target-to-cell Hall theorem is needed for its first `d` strict-lower rows.

## 4. Exact remaining boundary

The result removes one gate but not three others.

1. **Deeper targets.**  Owner intersections of depth `q>d` do not fit in a
   depth-`d` source window by (3.1).  Targets of rank below `r-d` still need
   fresh short source occurrences or a separate compiler mechanism.
2. **Cross-pin protection.**  If the final antecedent is obtained by deleting
   coordinates from `P`, the cells (3.1) remain valid only when the deeper
   target pins leave at least one occurrence of every positive coordinate in
   each designated interval.  In the exact fixed-atlas criterion these are
   the positive-hit cuts

   \[
    Q_x\cap J(i,q)\ne\varnothing
    \quad\left(x\in\bigcap_{j=0}^{q}T_{i+j}\right).            \tag{4.1}
   \]

   The top-layer targets create no self-conflict: if `x` is absent from their
   target value, then `x` is already absent from every maximal-envelope letter
   in `J(i,q)`.  Only pins belonging to other selected target intervals can
   erase a designated positive witness.
3. **Typed routes.**  A literal interval (3.1) is an ordinary compiler cell.
   If it must also reach a shared typed sink bank, the residual gammoid/Rado
   cut remains.

For a linear opening, the same proof applies to every untruncated interior
window.  Boundary owners require the separately priced opening collar; no
cyclic-to-linear boundary claim is made here.

## 5. Consequence for the rigid-rotation route

Combining the rigid all-depth fan theorem with Corollary 3.1 changes the
strict-lower ledger as follows:

1. ranks `r-d,...,r-1` have explicit, mutually compatible cells in the
   maximal antecedent;
2. only ranks below `r-d`, together with preservation of (4.1), remain in
   the ordinary fresh-atlas problem;
3. after canonical literal occurrences are fixed, any extra shared cap is
   exactly the full-port linkage cut, not a target-to-cell matching cut.

This is a strict reduction of the compiler problem.  It is not yet a proof
of a complete terminal antecedent, bounded cyclic opening, deeper compiler,
or typed full-port router.

## 6. Dependencies and scope

The rigid named fan and owner-path occurrence banks are in

`MATH_THEOREM_PBBS_RIGID_ROTATION_E1_FAN_COMPLETE_SUPPORT_REPAIR_20260805.md`

and

`MATH_THEOREM_PBBS_RIGID_ROTATION_OWNER_PATH_SDR_AND_SOURCE_LIFT_BOUNDARY_20260805.md`.

The exact positive-hit cuts referred to in (4.1) are in

`THREAD_A_UNRESTRICTED_COMP_TWO_BOUNDARY_LAMINAR_HALL_THEOREM_20260729.md`

and are restated in

`MATH_THEOREM_PBBS_RIGID_ROTATION_FIXED_ANTECEDENT_COMPILER_AND_EXACT_CAP_CUT_20260805.md`.

No computation, finite search, or probabilistic assumption is used.
