# Audit of fixed-width wedge facet-seam repair and the two-component socket

Date: 2026-07-30  
Lane: AD  
Audited source:
`MATH_THEOREM_ROOT_FIXED_WIDTH_WEDGE_SEAM_RAY_ABSORPTION_20260730.md`  
Status: local theorem PASS.  The union identity is valid at every depth and
through cyclic index wrap.  The corrected source now distinguishes a cyclic
socket merge from a final linear word.  On the retained factors the cyclic
two-socket condition fails at both `k=13` and `k=15`; nevertheless the
`k=13` factor has 52 exact distinguished-safe big-to-small linear socket
chains.  The `k=15` 45-cycle is wedge-free, so this theorem does not
instantiate there.

## 1. Local statement

Let a directed Johnson cycle have a wedge at `A_i`:

\[
 U=A_{i-1}\cup A_i=A_i\cup A_{i+1}.                \tag{1.1}
\]

Cut the right flank `A_i A_(i+1)`.  In the opened orientation put

\[
 E=A_i,\qquad S=A_{i+1}.                            \tag{1.2}
\]

Suppose the preceding opened path ends in an `r`-set `B` satisfying

\[
 B\cup S=U=E\cup S.                                \tag{1.3}
\]

Because `B` and `S` are distinct facets of the `(r+1)`-set `U`, the new
seam `B--S` is a Johnson edge.

### Theorem 1.1 (simultaneous fixed-width seam repair)

Let

\[
 E,S,A_{i+2},\ldots,A_{i+q}                        \tag{1.4}
\]

be a fixed-width `q`-edge witness, so its union has rank `r+q`.  Then the
new contiguous interval

\[
 B,S,A_{i+2},\ldots,A_{i+q}                        \tag{1.5}
\]

has exactly the same union.  Every selected fixed-width witness crossing
the cut has form (1.4); witnesses avoiding the cut remain internal.

#### Proof

A fixed-width witness crossing the right flank cannot also cross the left
flank.  Traversing both wedge transitions repeats the wedge coordinate, so
at most `q-1` fresh coordinates are introduced and the union rank is at
most `r+q-1`.  Among directed `q`-edge intervals containing the right flank
but not its predecessor, the only one starts at `E`; this remains true when
the numerical indices wrap modulo the cycle length.  Finally,

\[
\begin{aligned}
B\cup S\cup A_{i+2}\cup\cdots\cup A_{i+q}
 &=U\cup A_{i+2}\cup\cdots\cup A_{i+q}\\
 &=E\cup S\cup A_{i+2}\cup\cdots\cup A_{i+q}.
\end{aligned}                                      \tag{1.6}
\]

No step depends on `q=2`.  A fixed-width witness automatically has
`q<N`; otherwise it would revisit the initial cycle vertex and the closing
transition could not introduce a fresh coordinate. QED.

The left-flank version is obtained by reversing the component and uses the
outgoing seam after that opened path.

## 2. Exact directed socket graph

An oriented right-flank option is a triple

\[
 o=(C,i,\epsilon),\qquad \epsilon\in\{+1,-1\},     \tag{2.1}
\]

where `A_i` is a wedge center in the orientation `epsilon`.  Define

\[
 E(o)=A_i,\quad S(o)=A_{i+\epsilon},\quad
 U(o)=A_{i-\epsilon}\cup A_i=A_i\cup A_{i+\epsilon}. \tag{2.2}
\]

There is a directed socket arc

\[
                   o\longrightarrow p
 \quad\Longleftrightarrow\quad
                   E(o)\cup S(p)=U(p).              \tag{2.3}
\]

The seam represented by (2.3) repairs every selected fixed-width witness
crossing the cut of the destination option `p`.

### Proposition 2.1 (two-component mutual-socket condition)

Two oriented options `o_1,o_2`, one from each component, form a directed
facet-socket 2-cycle if and only if

\[
 o_1\to o_2\quad\hbox{and}\quad o_2\to o_1.        \tag{2.4}
\]

Such a 2-cycle produces an upper-tower-preserving cyclic chronology by
Theorem 1.1.  The converse is asserted only inside this mutual facet-socket
construction: alternative old or seam witnesses may make a nonsocket splice
upper-safe.  Cutting either new seam to obtain a
linear word can again lose witnesses; (2.4) alone is not a final-word
certificate.

When the two components are vertex-disjoint, (2.4) has the simpler exact
form

\[
                            U(o_1)=U(o_2).           \tag{2.5}
\]

Indeed, the socket equations put the two distinct `r`-sets
`E(o_1),E(o_2)` inside both `(r+1)`-sets `U(o_1),U(o_2)`.  Their union has
size at least `r+1` and lies in the intersection of the two wedge unions,
forcing equality.  Conversely, if the wedge unions agree, component
disjointness makes every cross-component pair of their facets distinct, so
both socket equations hold.

### Proposition 2.2 (two-component linear sufficient condition)

Put component 1 first and component 2 second.  The following selected-tower
condition is sufficient:

1. `o_1 -> o_2`;
2. every target assigned to component 1 has a fixed-width occurrence whose
   edge span avoids the physical cut of `o_1`;
3. every other target is assigned a fixed-width occurrence on component 2.

Then component-1 witnesses remain internal and Theorem 1.1 repairs every
crossing component-2 witness at the single seam.

Condition 2 has a direct finite form.  Let

\[
 K^{\rm fw}_{1,q}(Y)
  =\bigcap\{\text{edge span}(I):I\text{ is a q-edge witness of }Y
                  \text{ on }C_1\}.                \tag{2.6}
\]

Assign every target occurring on `C_2` to `C_2`.  For targets absent from
`C_2`, condition 2 for this assignment scheme holds exactly when the cut of
`o_1` avoids

\[
 \bigcup_{q,Y\notin C_2}K^{\rm fw}_{1,q}(Y).        \tag{2.7}
\]

This is a fixed-width kernel test, not the false unrestricted rank-two
criterion.  Accidental additional seam witnesses could make the final word
safe even when this sufficient selected-witness test fails.

## 3. Exact `k=13` check

The authenticated middle path splits at index 1547 into cyclic components
of lengths

\[
                         1547+169.                  \tag{3.1}
\]

They have 104 and 13 wedges.  Allowing both orientations gives 208 and 26
right-flank options.  Their numbers of distinct wedge unions are 78 and 13,
with zero shared union.  In accordance with (2.5), the exact socket graph
has

\[
\begin{array}{c|r}
\text{arc family}&\text{count}\\ \hline
C_{1547}\to C_{169}&104\\
C_{169}\to C_{1547}&0\\
\text{reciprocal pairs}&0.
\end{array}                                         \tag{3.2}
\]

Thus there is no two-component cyclic **mutual-socket** splice of form
(2.4).  This is not a no-go for arbitrary upper-safe cyclic splices.

The factor is fixed-width complete at every depth `q=1,...,6`.  Assigning a
target to the small component whenever it occurs there gives the following
distinguished-big ledger:

\[
\begin{array}{c|r|r|r}
q&\#\text{targets}&\#\text{absent on small}&
 \#\text{nonempty }K^{\rm fw}_{\rm big,q}\\ \hline
1&1287&1144&858\\
2&715&598&273\\
3&286&195&13\\
4&78&39&0\\
5&13&0&0\\
6&1&1&0.
\end{array}                                         \tag{3.3}
\]

The union (2.7) contains 1014 physical big-cycle edges.  Exactly 52 of the
104 oriented big-to-small socket arcs avoid it.  They use 26 distinct
oriented big source options; each has two admissible orientations of the
small destination.  For example, the reverse-oriented big wedge centered
at index 29, cutting physical edge 28, sockets to the small wedge centered
at index 88 in either orientation.

Every factor target was explicitly present at its required fixed width,
and the seam equality was replayed for all depths on every socket arc:

\[
                         104\cdot6=624              \tag{3.4}
\]

union checks, with zero failures including modular wrap.  Therefore the
`k=13` factor has 52 exact **upper-tower-complete linear socket chains**.
An independent implementation also materialized all 52 length-1716
chronologies and replayed every fixed-width layer `q=1,...,6`, with zero
holes.
This is only the upper chronology.  It does not itself certify seam
residence, the two lost lower colours, COMP_3 Hall, or a literal word.

These are not a relabeling of the retained successful `k=13` opening: its
two cut neighborhoods are nonwedges,

```text
2455|2515 = 0x9d7 != 0x9db = 2515|2395,
2675|2167 = 0xa77 != 0x977 = 2167|2391.
```

The new 52 rows therefore require their own residence and lower-compiler
audit before any literal-word claim.

## 4. Exact `k=15` check

The authenticated factor has component lengths

\[
                         6390+45.                   \tag{4.1}
\]

The large component has 330 wedges and hence 660 oriented right-flank
options.  The 45-cycle has zero wedges and zero such options.  Consequently

\[
 \#(C_{6390}\to C_{45})=
 \#(C_{45}\to C_{6390})=
 \#\text{reciprocal pairs}=0.                       \tag{4.2}
\]

The corresponding distinct-wedge-union counts are 330 and zero.

The factor is nevertheless fixed-width complete at depths `q=1,...,7`.
Equation (4.2) means only that the all-components-wedge socket theorem does
not instantiate on this factor.  It does not rule out an arbitrary cut on
the 45-cycle, an old-witness-safe cut, a wider collar, or the already known
non-socket seam constructions.

## 5. Scope and remaining interface

The audited local theorem eliminates higher-depth SPILL exactly once an
appropriate facet socket exists.  It does not prove:

* a wedge on every component;
* a reciprocal socket cycle;
* a distinguished-safe first cut in every factor;
* residence across the new seam;
* lower-colour endpoint eligibility or the lower Hall compiler.

For the concrete `k=13` factor the upper part of the linear condition is
now fully certified by (3.2)--(3.4).  For the concrete `k=15` factor the
wedge premise fails on the small component, so a hybrid arbitrary-cut/ray
absorber or another seam theorem is still required.

## 6. Reproducer

The common independent replay is

```text
scratch/audit_ad_wedge_spill_ray_socket_20260730.py
  2029e7df58204133df291f9f10f6b7b4792c2ac9140edc7126080b1c7f954b7e
scratch/ad_wedge_spill_ray_socket_20260730.audit.json
  e6298b23401c077834d7139832c2c21f61fa4dee1a6092f5f85f4c76483cf6a1
payload
  efc5eae904742e1b13705c6ed62c0e868732d95efe6f9e9d1693cbd706284d59
```

It verifies factor identities, equivariant gauges, fixed-width coverage,
socket arcs, distinguished kernels, and all seam union equations.  No SAT,
web access, exhaustive subset search, or sustained local computation was
used.

The audited root theorem version has SHA
`8c771e7c4197c445ceabb002c8baa087c5baa88c2a9496f86a13ac6bea0d1241`.
