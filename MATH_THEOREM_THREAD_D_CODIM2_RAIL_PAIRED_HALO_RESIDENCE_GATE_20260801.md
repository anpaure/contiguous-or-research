# The codimension-two boundary current has a six-edge algebraic circuit, but residence forces growing halos

Date: 2026-08-01  
Lane: Thread D, independent referee audit of the aligned coatom birail  
Status: exact boundary-current circuit, exact common-cap pairing, and a
dimension-growing residence lower bound.  No source-word embedding is
claimed.

## 0. Verdict

Let `D` have size `r+2`, let

\[
             a,b,h,x,y,t\in D
\]

be distinct, and let `tau=(a b)`.  Write `T(E)=D\setminus E` for the
rank-`r` owner whose omitted pair is `E`.  In the coatom link of
`MATH_THEOREM_THREAD_D_C8_ALIGNED_SINGLECUT_COATOM_LINK_20260801.md`, for
`d>=4` these labels are

\[
 a=a_1,\quad b=a_3,\quad h=f_{d+1},\quad x=f_2,
 \quad y=f_{d-1},\quad t=f_0.                         \tag{0.1}
\]

The two direct rail boundaries have the exact signed lower current

\[
 [L_b]+[R_a]-[L_a]-[R_b],                            \tag{0.2}
\]

where

\[
\begin{array}{ll}
L_a=D\setminus\{a,h,x\},&L_b=D\setminus\{b,h,x\},\\
R_b=D\setminus\{b,t,y\},&R_a=D\setminus\{a,t,y\}.
\end{array}                                           \tag{0.3}
\]

There is an exact owner-level cancellation circuit.  Replace the two direct
seams by the omitted-pair paths

\[
\begin{array}{c|c|c}
 &\text{minus phase}&\text{plus phase}\\ \hline
\text{left}&ah-ax-bx-hx&bh-bx-ax-hx,\\
\text{right}&yt-ay-by-bt&yt-by-ay-at.
\end{array}                                           \tag{0.4}
\]

All eight displayed owner rows on each phase are simple.  The lower palette
is phase-independent separately on each halo.  The upper palettes are not
phase-independent separately, but their two defects cancel between the left
and right halos.  Thus (0.4) is a literal six-edge, two-shore boundary
circuit.

It is **not resident**.  In the left halo, coordinate `h` has an internal
positive owner run of length two; in the right halo, `t` does.  More
generally, every simple `tau`-related left halo from `ah` to `hx` whose lower
palette is phase-independent has an internal positive `h`-run.  At
depth `d` that run must contain at least `d+1` owner rows, so the halo has at
least `d+2` edges.  The same holds on the right.  In the separated literal
left/right profiles, a resident paired circuit therefore has at least

\[
                             2d+4                    \tag{0.5}
\]

edges, not six.

There are two additional physical gaps.

* The circuit has repeated upper q1 colours (`D\setminus{x}` twice on the
  left and `D\setminus{y}` twice on the right).  Cross-phase equality is not
  a strict-rainbow or incumbent-safety certificate.
* An omitted-pair owner path is not a source word.  No literal inverse,
  occurrence addresses, or pointwise source caps are supplied.  Subdividing
  the two old seam edges by a resident pair would add at least `2d+2` owner
  and source positions.  Equal phase lengths do not make this charge zero.

Consequently the paired halo proves the correct algebraic boundary current,
but refutes the proposed bounded resident realization in this direct class.
The exact escape is a nonlocal equal-length rethread/contraction which
exports a literal inverse and uses the two forced side-paired caps below.

## 1. Omitted-pair calculus

Two distinct owners `T(E),T(F)` are Johnson adjacent precisely when
`|E\cap F|=1`.  For such an edge,

\[
 T(E)\cap T(F)=D\setminus(E\cup F),\qquad
 T(E)\cup T(F)=D\setminus(E\cap F).                  \tag{1.1}
\]

Thus a path of omitted pairs records its lower q1 colour by the union triple
and its upper q1 colour by the common singleton.  This calculus is literal:
equal cardinality or isomorphic labels do not identify colours.

For the direct left and right seams the minus phase supplies `L_a,R_b` and
the plus phase supplies `L_b,R_a`.  This is exactly (0.2).

### Proposition 1.1 (two companion occurrences and forced target-cap pairing)

Suppose one wants both phases to contain all four colours in (0.3), and one
physical companion cell can serve at most one lower-q1 colour.  Then at
least two companion cells are necessary.  If corresponding cells in the two
phases must lie in a common cap of rank at most `r`, their phase pairing is
forced:

\[
             (L_a,L_b)\text{ at the left cap},\qquad
             (R_a,R_b)\text{ at the right cap}.       \tag{1.2}
\]

Indeed,

\[
 L_a\cup L_b=D\setminus\{h,x\},\qquad
 R_a\cup R_b=D\setminus\{t,y\},                       \tag{1.3}
\]

both of rank `r`.  The crossed unions are `D\setminus{a}` and
`D\setminus{b}`, both of rank `r+1`.  Hence the left/right caps in (1.3)
are the only rank-`r` pairing.

This is only a necessary occurrence ledger.  It does not manufacture the
two source cells.  The two rank-`r` sets in (1.3) are the rail endpoint
owners `T(hx),T(ty)`.  They are **interval-value caps**, not the much smaller
planted source letters `X_L,X_R`.  Thus Proposition 1.1 does not say that the
seven-host menu already contains the required companion occurrences.

## 2. Exact six-edge circuit

For the left minus path in (0.4), the lower omitted triples are

\[
               ahx,\quad abx,\quad bhx,               \tag{2.1}
\]

and `tau` reverses this list.  Its upper omitted singletons are

\[
                        a,x,x,                         \tag{2.2}
\]

while the plus list is `b,x,x`.

For the right minus path, the lower omitted triples are

\[
               aty,\quad aby,\quad bty,               \tag{2.3}
\]

again reversed by `tau`.  Its upper omitted singletons are `y,y,b`, while
the plus list is `y,y,a`.  Therefore

\[
 \{a,x,x,y,y,b\}=\{b,x,x,y,y,a\},                    \tag{2.4}
\]

and the complete upper multiset is phase-independent.

The qualification "complete" is important.  A single halo is not upper
neutral.  Also, (2.2)--(2.4) exhibit two repeated upper colours in each
phase.  The circuit is an exact signed/multiset circuit, not a two-sided
rainbow circuit.

Relative to the two direct seams, (0.4) replaces two edges by six and adds
the four internal owners

\[
                      ax,bx,ay,by.                     \tag{2.5}
\]

These are distinct, but their availability in an ambient owner factor is a
separate address condition.

## 3. Minimal algebraic length in the separated halo class

Assume the left path uses only `{a,b,h,x}` and the right path only
`{a,b,y,t}`.  Their lower triple supports are disjoint because the two
alphabets intersect in only `{a,b}` and every lower colour omits three
distinct labels.  Hence global lower cancellation forces lower cancellation
on each halo separately.

### Lemma 3.1 (one and two edges do not suffice)

There is no simple `tau`-related path of one or two edges from `ah` to `hx`
with a phase-independent lower multiset.

For one edge the two omitted triples are `ahx` and `bhx`.  For two edges,
an intermediate pair adjacent to both endpoints is either `ax` or `hu`.
The first choice gives two copies of `ahx` versus two copies of `bhx`.  In
the second choice the triple containing `x` forces `u=tau(u)`, after which
the other triple still distinguishes `a` from `b`.  Thus neither works.

The path in (0.4) shows that three edges suffice.  By the symmetric right
argument, six total edges are minimum in this separated, nonresident
algebraic class.

Allowing a halo to borrow the other side's labels invalidates the disjoint
support step.  No total-six minimality statement is asserted for that larger
nonlocal class.

## 4. Residence forces a growing halo

The preceding finite minimality is not the physical bound.

### Theorem 4.1 (star-parity residence lower bound)

Let

\[
                 E_0=ah,E_1,\ldots,E_ell=hx           \tag{4.1}
\]

be a simple omitted-pair path, and let the other phase be its `tau` image.
If the two lower-colour multisets are equal, then some internal `E_i` does
not contain `h`.  Consequently the owner path has an internal positive
`h`-run.  If it is depth-`d` resident, then

\[
                              ell\ge d+2.               \tag{4.2}
\]

#### Proof

Suppose every `E_i` contains `h`.  Write `E_i={h,u_i}`.  Simplicity makes
`u_0=a,u_1,...,u_ell=x` a simple label path.  Removing the common `h` from
each lower omitted triple identifies the lower palette with the edge set of
this label path.  Phase equality says this edge set is `tau`-invariant, so
the degrees of `a` and `b` are equal.  But `a` is one endpoint and has
degree one, whereas `b` is either absent (degree zero) or internal (degree
two), since the other endpoint is the fixed label `x`.  Contradiction.

Hence some internal omitted pair avoids `h`, so the corresponding owner
contains `h`.  Since both endpoint pairs contain `h`, the maximal positive
`h`-run containing this row is wholly internal.  Residence makes its length
at least `d+1`.  It needs an omitted-`h` owner on each side, so the path has
at least `d+3` vertices and `d+2` edges.  \(\square\)

Apply the theorem with `t` on the right.  Under separated lower supports,
both halos must be neutral separately, giving (0.5).

For the explicit three-edge paths the bad runs are visible without the
theorem:

\[
 \begin{array}{c|c|c}
 \text{halo}&\text{coordinate}&\text{positive-owner positions}\\ \hline
 \text{left}&h&1,2\\
 \text{right}&t&1,2.
 \end{array}                                           \tag{4.3}
\]

They are bounded by zeros at both path ends.  No exterior collar can extend
these runs.

## 5. Source, common-cap and equal-length quantifiers

The owner universe `D` is not a legal rank-`r` source cap: it has rank
`r+2`.  Moreover, at an active internal address the two phase owners
`T(ax),T(bx)` have union `D\setminus{x}` of rank `r+1`.  Thus even a
pointwise common *owner* cap of rank `r` is impossible there.  A source cap
may be smaller, but proving it requires literal source rows.

For a proposed owner chronology `T_0,...,T_m`, put

\[
 E_p=\bigcap_{\max(0,p-d)\le j\le\min(m,p)}T_j.        \tag{5.1}
\]

The maximal inverse test is

\[
                   T_j=\bigcup_{p=j}^{j+d}E_p          \tag{5.2}
\]

for every row, with the actual exterior chronology included.  A physical
two-phase embedding additionally needs source rows `A^0,A^1` satisfying

\[
 D^dA^epsilon=T^epsilon,\qquad
 A_p^0\cup A_p^1\subseteq C_p                         \tag{5.3}
\]

at fixed addresses, plus occurrence freshness and all crossing-interval
checks.  Equations (0.4) do not imply (5.2) or (5.3).

The same distinction controls length.  Both phases in (0.4) have six
edges, but the old two-boundary scaffold has two.  Direct subdivision adds
four positions.  Any resident subdivision has at least `2d+4` edges and
therefore adds at least `2d+2` positions.  Zero net charge requires a
different equal-length segment rethread or that many certified contractions;
it does not follow from phase equality.

This reconciles the result with the audited seven-host menu.  That menu has
pointwise common source caps and, once planted, a fixed `+7` bank which does
not grow under repeated phase changes.  It has no native zero-length
planting in the sharp four-block word.  The paired halo neither removes the
initial `+7` nor supplies a new zero-length planting: its bounded version is
nonresident, while every resident direct subdivision has the growing charge
above.

The telescoping theorem in
`MATH_THEOREM_ALIGNED_BIRAIL_TELESCOPING_AND_PROSPECTIVE_FIXED_BANK_20260801.md`
does not alter this conclusion.  It cancels signed lower actions only for a
prospectively prepared sequence with the same literal bases and profiles.
It supplies neither the occurrence cells in (5.3) nor the compensating
length contractions.

## 6. Exact surviving gate

The direct paired halo settles the boundary algebra but not the physical
macro.  A positive theorem must exhibit all of the following jointly:

1. a nonlocal resident left/right circuit (or a circuit whose short runs are
   removed by an equal-length interior rethread);
2. the two side-paired rank-`r` common caps from (1.3), at literal source
   addresses;
3. strict or incumbent-safe lower and upper occurrences, including payment
   for the repeated upper colours in (2.2)--(2.4);
4. a maximal-inverse certificate (5.2) in the full exterior chronology; and
5. zero net positions via an equal-length replacement or protected
   contraction Hall.

The smallest counterexample to omitting these rows is already (0.4): it is
simple and exactly phase-neutral in both q1 multisets, yet it is nonresident,
not upper-rainbow, and has positive length charge.

## 7. Audit

Run

```text
python3 scratch/audit_threadD_codim2_rail_paired_halo_residence_20260801.py --write
```

The dependency-free replay checks the omitted-pair calculus, the exact
lower and upper multisets in both phases, owner simplicity, the duplicated
upper colours, the two forced common-cap pairings, the complete one/two-edge
left and right no-go, and the explicit internal length-two residence defects
for `2<=d<=16`.

Frozen replay:

```text
scratch/audit_threadD_codim2_rail_paired_halo_residence_20260801.py
  SHA-256 6c83d1cf83e7056635ceb9f7648b91ea14beb1cf1f000d44db9bcf0c4e93bea8
scratch/threadD_codim2_rail_paired_halo_residence_20260801.audit.json
  SHA-256 cb5a09aff7188fb6c74f232e8a091b9b864a6af0520c60516794367e40c69997
  payload c938afea65b30a6d3e9222a1ddac905f23bc2017b231e597d4a1dfb2760dfe40
```
