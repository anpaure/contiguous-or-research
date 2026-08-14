# Hostile audit of the minimal marked-C6 resident reset quotient

**Date:** 2026-08-14  
**Audited theorem:**
`MATH_THEOREM_D5_MINIMAL_MARKED_C6_RESIDENT_RESET_QUOTIENT_20260814.md`  
**Audited SHA-256:**
`1fc6116577918d2749cfcfb42dbc0965927538253a5a7c62930d3ba7273ecde4`  
**Verdict:** **PASS** for the closed local 18-owner C6 router, the
self-contained 24-owner fixed-tail box, q1 simplicity, exact two-shore q2
zero current, internal residence, the stated two-move collar criterion, and
architecture-relative minimality.  It does not prove prescribed D5 terminal
linkage or simultaneous planting.

## 1. Rank-five spectator boundary

The spectator supply inequality is sharp but valid.  After reserving the
router marker `h`, there are `2r-2` available coordinates.  A spectator core
of size `r-2` and five exterior labels require

\[
                         (r-2)+5=r+3\le2r-2,          \tag{1.1}
\]

which is equivalent to `r>=5`.

At the endpoint `r=5`, the router ground can be written

\[
 \{h,x_1,x_2,y_1,y_2,z,a_0,a_1,a_2\}.               \tag{1.2}
\]

One literal spectator choice is

\[
\begin{aligned}
 K'&=\{a_2,y_1,y_2\},&x'_1&=a_2,&x'_2&=y_1,\\
 (y'_1,y'_2,z',s_0,s_1)&=(x_1,x_2,z,a_0,a_1).        \tag{1.3}
\end{aligned}
\]

The core and exterior in `(1.3)` are disjoint and all omit `h`.  Every
router owner and every lower, upper, lower-q2, and upper-q2 resource contains
`h`; every spectator resource omits it.  Hence the typed banks are disjoint
even at equality in `(1.1)`.  The H100 replay includes `r=5` and obtains the
claimed 24 distinct resources on each q1 and q2 row.

## 2. Full q2 deck audit

For one old router port, the six lower triple intersections are

\[
\begin{array}{lll}
 (K-x_1)+a_i,&(K-x_1-x_2)+a_i+a_{i+1},&
 (K-x_1-x_2)+y_1+a_i,\\
 (K-x_1-x_2)+y_2+a_i,&(K-x_1-x_2)+z+a_i,&
 (K-x_2)+a_i.
\end{array}                                           \tag{2.1}
\]

The theorem's pre-freeze draft incorrectly wrote the fifth value with only
`x_2` missing.  Direct intersection shows that both `x_1,x_2` are missing;
the frozen theorem contains `(2.1)`.  This repair does not affect the current
identity or the executable replay.

In `(2.1)`, the missing subset of `{x_1,x_2}` first distinguishes the two
end values from the middle four.  Within a clock class, the extra symbol
`a_(i+1),y_1,y_2,z` distinguishes the position, and `a_i` or the adjacent
active pair distinguishes the port.  Thus all 18 lower-q2 router values are
distinct.

The six upper triple unions are

\[
\begin{array}{lll}
 K+z+y_1+a_i+a_{i+1},&K+y_1+y_2+a_i+a_{i+1},&
 (K-x_1)+z+y_1+y_2+a_i+a_{i+1},\\
 (K-x_2)+z+y_1+y_2+a_i+a_{i+1},&K+z+y_1+y_2+a_i,&
 K+z+y_2+a_i+a_{i+1}.
\end{array}                                           \tag{2.2}
\]

The full clock profile distinguishes the six positions, after which the
active singleton or pair distinguishes the port.  Hence all 18 values in
`(2.2)` are distinct.  The spectator contributes six further distinct
values on each shore, separated by absence of `h`.

Only the two triple windows adjacent to each C6 seam change.  The lower
values agree at the same port:

\[
 Q_{i,1}\cap A_i\cap B_i
  =Q_{i,1}\cap A_i\cap B_{i-1},\qquad
 A_i\cap B_i\cap P_{i,1}
  =A_i\cap B_{i-1}\cap P_{i-1,1}.                    \tag{2.3}
\]

The two upper values replace active pair `{a_i,a_(i+1)}` by
`{a_(i-1),a_i}` and therefore cancel by cyclic reindexing.  All other
windows and the spectator are copied.  Thus both complete q2 occurrence
currents are exactly zero.

## 3. Residence and the collar quantifier

The six transition supports on an old port are

\[
\begin{array}{c}
 \{z,a_{i+1}\},\ \{x_1,y_1\},\ \{x_2,y_2\},\\
 \{z,a_{i+1}\},\ \{x_1,y_1\},\ \{x_2,y_2\}.
\end{array}                                           \tag{3.1}
\]

The switched C6 seam merely replaces the first pool by
`{z,a_(i-1)}` on the corresponding outgoing rail.  Any three consecutive
support pools are pairwise disjoint.  This proves owner run/gap minima
`(3,3)` and immediate-upper minima `(4,2)` in both phases.

Cutting `P_(i,2)Q_(i,0)` is phase-common and lies three transitions from the
changed seam.  At its two sides the internal support pools are
`{x_2,y_2}` and `{x_1,y_1}`.  A q2 collar crossing the graft can contain up
to two exterior moves, not only one.  The pre-freeze one-move guard was
therefore insufficient.  The frozen theorem correctly requires the first
two and last two exterior supports to avoid all four clock labels.

Together with q2 biresidence of the exterior, that condition checks the only
mixed triples explicitly:

\[
 \{x_2,y_2\},S_1,S_2
       \qquad\hbox{and}\qquad
 T_2,T_1,\{x_1,y_1\}.                                \tag{3.2}
\]

Every pair in each triple is disjoint.  Thus owner and immediate-upper q2
residence survives both grafts.  Since the cut, two internal stubs, and
exterior are identical in the two phases, every q2 window crossing a graft
is also copied occurrence-for-occurrence.  This proves exactly the stated
collar criterion.  It does not assert that the frozen D5 occurrences already
satisfy it.

## 4. Minimality scope

A simple Johnson-cycle component cannot have every coordinate constant:
that would make all owner sets identical.  It therefore has a nonconstant
coordinate.  Q2 biresidence gives that coordinate a positive cyclic run and
a zero cyclic run, each of length at least three, so the component has at
least six owners.

If the old first-return map is identity on three distinct router ports, no
two can lie on the same directed component: on a component with two marked
ports, first marked return sends one to the other.  Hence the router needs at
least three six-owner components, or 18 owners.  If the tail is a fourth
physical fixed-return port in a self-contained box, it is a fourth component
and raises the lower bound to 24.  The construction attains both bounds.

The 24 bound does not apply when a tail wire is borrowed from an ambient
protected factor or represented only formally; then the proved sharp local
count is the 18-owner router.  Nor does the theorem claim minimality among
models with repeated owner occurrences, noncyclic boundary fragments, or a
different notion of full port return.

## 5. D5 terminal audit and scope

Suppressing the auxiliary port turns `(b u c)` into `(b c)` and the
spectator fixes `a`, so the internal D5 reset action is exact.

The tapped rank-seven formulas also pass.  In the adjacent type, marks at
`A_0,A_2,A_1` and the tail `K+z+f_0` have signature

\[
                           (1,1,1,6,9).               \tag{5.1}
\]

In the hard type, marks at

\[
 A_0,\quad A_2,\quad Q_{1,1},qquad
 T=(K-x_2)+z+a_0+a_1                                \tag{5.2}
\]

have signature `(1,1,2,5,9)`.  Although `Q_(1,1)` is at a different phase,
there is exactly one mark on each old router component.  Traversing the new
18-cycle gives `B -> U -> C -> B`, so the marked quotient is still the
required head transposition.

The two displayed spectator parameter sets root their first owner exactly
at the corresponding `T`.  Direct q1/q2 comparison is disjoint from the
router at rank seven.  Adding one common owner coordinate plus one unused
ground coordinate per rank preserves every distinction, proving the lift to
all larger ranks.  Since the D5 signatures determine the Venn cells, this
settles **individual typed coordinate compatibility** for both the 48 and
164 row classes.  A separate serial resident cable is therefore unnecessary
in the tapped architecture.

This does not identify all `a,b,c` occurrences simultaneously inside the
frozen D5 factor.  In particular, it does not yet prove:

1. a simultaneous choice of the hidden `u` and clock labels for all 212
   reset rows;
2. clock-disjoint terminal connectors satisfying Section 3; or
3. one common owner/lower/upper host containing all boxes.

Those are the surviving occurrence-linkage and coinstantiation rows.  The
theorem is a strict improvement over the C8 route at the internal-current
layer: it has zero lower as well as upper q2 current and needs no heptagonal
backups.

## 6. H100 certificate

The frozen replay checks every rank `5<=r<=40`, including literal Johnson
incidence, simple cycles, containment in the declared ground, both return
maps, all q1 and q2 simplicity/equality rows, the seam identities, and both
run/gap minima.

```text
verifier SHA-256
bfc51de922d507ae86de1f88cafb919c3f34a0addc0f5b2e2adf518626f06336

H100 output SHA-256
24cd3b64a40f3c942a1961c00633c18adfc5ee104b87d58a5dc3c21cbcbef994
```

All execution and hashing occurred on H100.
