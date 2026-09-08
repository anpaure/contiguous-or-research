# Independent audit: clocked singleton-arm product-cell compiler

**Date:** 2026-08-13  
**Verdict:** **PASS.**  The base-rank and freshness hypotheses identified in the
first audit are present in the frozen source below.  
**Frozen source:** MATH_THEOREM_CLOCKED_SINGLETON_ARM_PRODUCT_CELL_COMPILER_AND_ATOM_COUNT_GATE_20260813.md  
**Source SHA-256:** dee9cf183d3f8b193903e985db4e57bae76598d2b9754df15e17f569186efff9

This was a proof-level audit.  No search or solver was used.

## 1. Owner, lower, upper, and residence rows

The payload run has length \(L\le q-2\), so every cyclic interval of
\(q-1\) source positions contains at least one guard.  Every such interval therefore
contains all of \(F=K\dot\cup E\).  Its toggle part is a proper cyclic interval in the
\(N=q+2\) distinct toggle labels.

It follows literally that widths \(q-1,q,q+1\) have ranks \(R-1,R,R+1\)
and are separately simple.  Shifting the \(q\)-window deletes its oldest toggle and
inserts the next, so the owner row is a simple Johnson cycle.  A toggle belongs to
exactly the \(q\) consecutive owner windows containing its unique source address; its
positive run therefore has length exactly \(q\).  Core coordinates are permanent in the
owner row.  The theorem correctly claims positive residence only: every toggle has a
zero gap of length two.

Intervals wholly inside the payload arm contain no \(E\)-emission and have the exact
value \(K\) plus their consecutive payload toggles.  Theorem 1.1 passes.

## 2. Product rectangle indexing

The left increments are ordered

\[
c_{i_0+A-1},c_{i_0+A-2},\ldots,c_{i_0+1}
\]

and the right increments in the opposite direction

\[
d_{j_0+1},d_{j_0+2},\ldots,d_{j_0+B-1}.
\]

For \(i,j\ge1\), the interval from \(c_{i_0+i}\) through \(d_{j_0+j}\)
contains exactly the left increments \(c_{i_0+1},\ldots,c_{i_0+i}\) and
the right increments \(d_{j_0+1},\ldots,d_{j_0+j}\).  Its width is \(i+j\)
and its union with the base is exactly
\(C_{i_0+i}\cup D_{j_0+j}\).

For a left-axis cell, take the left subarm from \(c_{i_0+i}\) down through
\(c_{i_0+1}\); for a right-axis cell, take the right subarm from
\(d_{j_0+1}\) through \(d_{j_0+j}\).  Their widths are respectively \(i\)
and \(j\), and their values are correct.  The base has no toggle occurrence and is
properly excluded.  Thus the ordering, axis cases, values, and widths in Corollary 2.1
all pass.

## 3. Repaired parameter conditions

Corollary 2.1 now assumes

\[
 |K|=|C_{i_0}|+|D_{j_0}|\le R-q.                         \tag{A.1}
\]

Otherwise the guard core required by Theorem 1.1 would have size
\(|E|=R-q-|K|<0\), and the clocked rail does not exist.

It also says explicitly that \(E\) and the guard-toggle set \(Y\) are chosen
from the complement of \(K\cup X\).  Once (A.1) holds, this choice is possible under
the stated \(R+2\le k\), because the complete packet support has exactly

\[
 |K|+|E|+|X|+|Y|=(R-q)+(q+2)=R+2
\]

coordinates.  No stronger ambient-capacity assumption is needed.

With (A.1), every nonbase product target has rank at most

\[
 |K|+(A+B-2)\le (R-q)+(q-2)=R-2,
\]

so it is indeed a strict-lower target.

The patched conditions close the only defect in the first audit.

## 4. Atom-count scope

Each closed atom uses exactly \(q+2\) source addresses and has exactly \(q+2\)
middle-owner windows.  Thus (3.1) is the correct raw packet charge and (3.2) is a
necessary coefficient-one budget before global overlap/fusion.  Paying an uncovered
base with a singleton address can itself create additional middle windows, so the note
correctly labels (3.2) necessary rather than sufficient.

The two repairs for arms of length \(q-1\) are proof-safe reductions: either remove one
outer cell/increment, or place the sole in-arm guard emission at the terminal phase and
assign only cells avoiding it.  Their exact weighted recurrence is correctly left open.

The theorem proves no asymptotic atom-count bound, packet factor, global resource
disjointness, or fusion.  Its scope is exact.

## 5. Remote census replay

The frozen script `analyze_clocked_product_scd_atom_count.py` was rerun on H100 for
all six displayed values \(k=201,301,401,561,641,721\).  Its `source/W`,
`bases/W`, and `one-clock-per-atom/W` outputs agree with every row of Table (5.1)
to all seven printed decimal places.  In particular, the private one-clock-per-atom
charge is above one in every displayed case.  This is a finite exact census, not an
asymptotic lower bound, exactly as the source states.
