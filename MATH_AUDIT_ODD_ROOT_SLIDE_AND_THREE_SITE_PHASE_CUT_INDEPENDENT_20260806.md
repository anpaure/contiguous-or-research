# Independent audit: root-slide parity and three-site phase cut

**Date:** 2026-08-06  
**Audited source:**
`MATH_THEOREM_ODD_ROOT_SLIDE_PARITY_AND_THREE_SITE_PHASE_CUT_20260806.md`  
**Method:** direct reindexing and complete hand enumeration of the
three-site layer; no computation or search  
**Verdict:** Theorem 1.1 and Proposition 2.1 PASS.  Corollary 2.2 needs an
explicit global quiet-prefix/protection hypothesis; without it, the final
unconditional no-go sentence is too strong.

**Resolution:** the audited source was subsequently amended to state this
quiet-prefix hypothesis explicitly and to retain only the unconditional
claim that every three-site transporter passes through `111`.  With that
amendment, the source PASSes this audit.

## 1. Root-slide identity

Reindexing gives

\[
 \chi_{j+1}-\chi_j
   =(n-1)t_j-\sum_{q=1}^{n-1}t_{j+q}
   =-R+nt_j.
\]

For odd \(n\), this is \(R-t_j\) modulo two.  At odd \(R\), a crossed
coordinate of value one therefore preserves the shore.  The indexing and
sign in the source are correct.

## 2. Three-site graph

At local mass three and capacity two, deleting \(111\) leaves the six
permutations of \(201\).  Their noncentral adjacent-transfer edges are
exactly

\[
                         201-210-120
\]

and

\[
                         021-012-102.
\]

Thus \(201=20|1\) and \(021=02|1\) lie in different components after
deleting \(111\).  Proposition 2.1 is exact, and every three-site phase
transporter must use \(111\).

## 3. Scope correction

A local boundary state \(11\) is an endpoint of the **row**
\(11-02\), but the global first-nonquiet scan selects that boundary row
only when every earlier scan pair is quiet.  In the clock/zipper aperture,
an earlier active marker can make the scan stop before the boundary.  The
corresponding global state with local pattern \(111\) is then not
automatically in the deleted set \(V(P)\).

Therefore the proof supports the conditional statement:

> if the relevant global \(111\) state is deleted or protected, no
> three-site phase repair exists.

It does not by itself support:

> every boundary-locked dual-phase basis lacks a three-site repair.

That stronger conclusion needs either a quiet-prefix theorem for every
candidate route or an independent reason that all occurrences of the
local \(111\) bottleneck are unavailable.

## 4. Correct remaining target

The unconditional information is still useful: a positive transporter
must either make one globally safe occurrence of \(111\) available, use
at least one more live coordinate, or perform a nonlocal root handoff.
The root-slide identity supplies the scalar parity condition for the last
option but not its physical linkage.
