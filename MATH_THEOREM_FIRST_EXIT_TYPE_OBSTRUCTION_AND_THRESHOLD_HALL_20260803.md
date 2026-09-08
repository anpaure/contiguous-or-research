# First-exit times do not force typed acceptance; the threshold face has an exact Hall formula

**Date:** 2026-08-03  
**Status:** unconditional order-type obstruction, exact nonimplication of
convex acceptance from first-exit geometry, and exact conditional threshold-
Hall theorem.  No computation is used.  The theorem does not construct the
missing canonical type converter.

## 0. Result

Use the first-exit paired bank of
`MATH_THEOREM_FIRST_EXIT_PAIRED_BANK_SINGLE_HALL_AND_TWO_WRAP_RESET_20260803.md`.
Its seam `i` supplies the same-phase nested terminal pair

\[
 (w_i,v_i),\qquad
 \operatorname{OR}(w_i)=R_i,\qquad
 \operatorname{OR}(v_i)=V_i,\qquad
 R_i\subset V_i,\qquad |V_i-R_i|=1.                    
\tag{0.1}
\]

The canonical zero-block cross tickets have a different order type.  For
`1<=j<d`, one cross edge has values

\[
\begin{aligned}
 P_0(j)&=B_3\cup F[1,j],\\
 S_1(j+1)&=B_3\cup F[j+1,d],
\end{aligned}
\qquad B_3=K\cup\{z,a_3\},                            
\tag{0.2}
\]

and the other has the same form with the base
`B_1=K\cup\{z,a_1\}`.  In both cases the two values are incomparable:

\[
 P_0(j)\setminus S_1(j+1)=F[1,j]\ne\varnothing,
\quad
 S_1(j+1)\setminus P_0(j)=F[j+1,d]\ne\varnothing .  
\tag{0.3}
\]

Therefore there is no coordinatewise value-preserving occurrence lift, in
either orientation, from a nondegenerate canonical cross ticket to a
first-exit pair.  More generally, no Boolean coordinate relabelling can be
such a lift, because relabellings preserve comparability.  The first-exit
bank replaces terminal **capacity**, but it does not natively realize the
canonical cross-ray occurrence type.

The occurrence phases give a second independent obstruction: a canonical
cross edge uses one coordinate from each of the two opposite phase rays,
whereas `(w_i,v_i)` is one same-phase nested pair.  A phase-preserving direct
lift is therefore impossible even after forgetting the Boolean values.
On the literal direct-lift face the acceptance graph has no edges, so the
canonical bank of `2(d-1)` logical cross tickets has deficiency

\[
                              2d-2,                    
\tag{0.3a}
\]

not `O(1)`.  A protected value-and-phase converter is indispensable.

There is also no interval, convex, or laminar acceptance graph forced by
the numbers `(h_i)` alone.  The terminal common-cap theorem permits
occurrence-labelled structural zeros only after a complete cap state is
fixed.  Without an additional rule tying those zeros to `h_i`, any
bipartite subgraph of ticket-by-seam incidences is consistent with the
stated abstract acceptance interface.  In particular, every ticket may be
nonloop while all tickets share one accepted seam, producing deficiency
`|I|-1`.

The strongest automatic simplification begins only after a genuine type
converter is supplied.  Suppose it has the **threshold form**: every ticket
`x` has an integer requirement `a_x>=2`, and after one complete
cap/background state and one fixed q1 phase it accepts exactly the available
seams satisfying

\[
                              h_i\ge a_x.               
\tag{0.4}
\]

Let `Z` be the unavailable wrap/background seam set.  Put

\[
 A(t)=|\{x:a_x\ge t\}|,
 \qquad
 H_Z(t)=|\{i\notin Z:h_i\ge t\}|.                     
\tag{0.5}
\]

Then the exact terminal deficiency is

\[
 \boxed{
 \delta_{\rm threshold}
 =\max_{t\ge2}\bigl(A(t)-H_Z(t)\bigr)_+.}
\tag{0.6}
\]

Thus the converter changes the exponential all-subset Hall problem into a
one-dimensional Ferrers ledger.

If the constant runs of the upper word `(R_i)` have lengths
`L_1,...,L_J`, the available uncut histogram is exactly

\[
 H(t)=\sum_{j=1}^{J}(L_j-t+2)_+ .                     
\tag{0.7}
\]

For an upper-surjective complete central owner row,

\[
 H(2)=W,qquad
 H(t)\le H(3)=W-J
 \le W-{2r-1\choose r+1}={2W\over r+1}\qquad(t\ge3).
\tag{0.8}
\]

For an arbitrary unavailable set `Z`, deletion alone gives

\[
                    H(t)-|Z|\le H_Z(t)\le H(t).        
\tag{0.9}
\]

For the particular cut supplied by the two-wrap theorem, let `Z_wrap` be
its two unavailable wrap seams.  If there are no further background
deletions, then

\[
              H(t)-2\le H_{Z_{\rm wrap}}(t)\le H(t).
\tag{0.10}
\]

With additional background deletions, (0.9), not (0.10), is the automatic
bound.

Equations (0.6)--(0.10) are the complete first-exit-time contribution to the
typed Hall gate.  No lower bound on `H(3)` follows from upper surjectivity:
repeated upper values may occur in separated one-edge runs.  Hence even the
threshold face requires a converter whose demand histogram fits the actual
run histogram; first-exit supply alone does not guarantee it.

## 1. Literal order-type obstruction

### Theorem 1.1

Let `(X,Y)` be either canonical cross pair in (0.2), with `1<=j<d`.
Let `(R,V)` be any first-exit pair in (0.1).  There is no permutation
`pi` of the Boolean ground coordinates for which either

\[
                         (\pi(X),\pi(Y))=(R,V)
\tag{1.1}
\]

or

\[
                         (\pi(X),\pi(Y))=(V,R).          
\tag{1.2}
\]

In particular, no full-block transport or other coordinatewise
value-preserving occurrence map identifies the two ticket types.

### Proof

Equation (0.3) makes `X,Y` incomparable.  A coordinate permutation is an
automorphism of the Boolean lattice and preserves inclusion and
incomparability.  Equation (0.1) makes `R,V` comparable in either ordering.
Thus neither (1.1) nor (1.2) is possible. `square`

This theorem is deliberately scoped to value-preserving lifts.  It does
not exclude a larger packet which changes the two values along protected
routes and proves that the resulting terminal roles still implement the
original compiler ticket.  Such a packet is exactly the missing type-
conversion theorem; it cannot be replaced by renaming coordinates or
terminal sockets.

The phase statement is equally direct.  The two canonical coordinates have
phase tags `(0,1)` (or `(1,0)`), while both first-exit terminals belong to
one fixed phase bundle.  A map retaining occurrence phase cannot identify
those records.  Therefore, with literal value and phase preservation, every
canonical ticket is a structural zero and the deficiency is the full
ticket count (0.3a).

## 2. No acceptance convexity follows from geometry alone

Fix the literal first-exit bundles and a logical ticket set `I`.  The
terminal common-cap theorem forms its graph only after a complete state
fixes the ticket, phase, occurrence address, flag, endpoint class, guard,
background reservation, and terminal type.

### Proposition 2.1 (acceptance-graph universality at the abstract interface)

Let `G subseteq I times Z_W` be any bipartite graph.  At the level of the
abstract terminal interface, there is a formally admissible
occurrence-labelled filter whose accepted first-exit graph is exactly `G`:
retain the complete bundle at seam `i` in ticket `x`'s menu precisely when
`xi in E(G)`.

Consequently no interval, convex, laminar, or Hall-expansion property of
the acceptance graph is a logical consequence of the simple Johnson row,
upper surjectivity, or the first-exit numbers.

### Proof

Occurrence labels are part of the port record, and arbitrary forbidden
incidences outside the structural-zero set remain explicit inputs to the
terminal Rado/gammoid theorem.  Filtering the complete deterministic bundle
records by the edge set of `G` changes none of their interval identities or
capacities.  It changes only whether the fixed terminal type of ticket `x`
accepts seam `i`.  Therefore the resulting acceptance graph is `G`.
`square`

This is a nonimplication theorem, not a claim that every artificial filter
is physically realizable or arises from the intended canonical compiler.
Its point is exact: a positive convexity theorem must use a stated property
of the canonical type converter.  It cannot be deduced from first-exit
geometry alone.

For example, take `m` tickets and let every ticket accept the same one seam.
Every ticket has a nonempty menu, but the exact Hall deficiency is `m-1`.
This is the first-exit realization of the common-unit-suffix bottleneck in
the terminal common-cap theorem.

## 3. Threshold converters give a Ferrers graph

Assume now the additional threshold hypothesis (0.4).  For `t>=2`, define

\[
 I_t=\{x:a_x\ge t\},
 \qquad E_t=\{i\notin Z:h_i\ge t\}.                   
\tag{3.1}
\]

The seam sets are nested:

\[
 E_2\supseteq E_3\supseteq\cdots\supseteq E_{r+1}.
\tag{3.2}
\]

### Theorem 3.1 (exact threshold Hall deficiency)

Equation (0.6) holds.

### Proof

Ticket `x` has neighborhood `E_(a_x)`.  These neighborhoods are nested.
The empty ticket family contributes deficiency zero.  For a nonempty ticket
family `X`, put

\[
                         t=\min_{x\in X}a_x.
\]

Then

\[
 N(X)=E_t,
 \qquad X\subseteq I_t,
\]

so

\[
 |X|-|N(X)|\le |I_t|-|E_t|=A(t)-H_Z(t).
\]

Conversely, when `t` is an attained ticket requirement, choosing `X=I_t`
gives

\[
 N(I_t)=E_t.
\]

If no ticket has requirement exactly `t`, then `A(t)=A(t+1)` while
`H_Z(t)>=H_Z(t+1)`, so the candidate at `t` is no larger than the next
candidate.  Iterating reaches an attained requirement or the empty set.
Thus the maximum over all `t>=2` is attained at an actual requirement and
equals the maximum Hall deficiency. `square`

Equivalently, sort the ticket requirements and seam exit distances in
decreasing order.  A perfect matching exists exactly when the `j`th ticket
requirement is at most the `j`th seam distance for every `j`.

### Corollary 3.2

If every converted ticket has requirement two and

\[
                         |I|\le W-|Z|,
\]

then the first-exit bank services every ticket.  In particular, when `Z`
is exactly the two-seam wrap set supplied by Theorem 4.1 of the paired-bank
theorem, the opening services any such bank of at most `W-2` tickets with
zero deficiency.  Extra background-unavailable seams must also be included
in `|Z|`.

This is the largest unconditional positive face visible from exit times:
all seams satisfy `h_i>=2`.  Requirements at least three depend on repeated
upper runs and have only the Catalan-scale supply in (0.8).

## 4. Exact exit-distance histogram

In a constant upper run of length `L`, the first-exit distances, from the
beginning to the end of the run, are

\[
                         L+1,L,\ldots,2.               
\tag{4.1}
\]

Therefore the number at least `t` contributed by that run is
`(L-t+2)_+`, proving (0.7).

At `t=3`, one run contributes `L-1`, so

\[
                         H(3)=\sum_j(L_j-1)=W-J.       
\tag{4.2}
\]

For `t>=3`, (0.7) gives `H(t)<=H(3)`.  Upper surjectivity gives at least
`binom(2r-1,r+1)` runs, one for every upper value, which proves (0.8).
Deleting an arbitrary set `Z` changes every histogram count by between zero
and `|Z|`, proving (0.9).  Applying this to the selected two-wrap set, of
cardinality exactly two, proves (0.10).  No two-seam lower bound is asserted
after additional background deletions.

Notice the direction of (0.8): it is an upper bound on long-exit supply,
not a lower bound.  The Catalan surplus controls the total possible
plateau bank but does not force any consecutive repetition of an upper
value.

## 5. Exact surviving type theorem

The first-exit bank can replace the canonical two-cross occurrence system
only after proving a converter with all of the following properties in one
complete state:

1. a non-value-preserving but compiler-correct route from each incomparable
   canonical cross pair to an accepted nested-upper pair;
2. occurrence and phase labels retained through that conversion;
3. compatibility with the transported background and every cap/guard row;
4. either requirement two for every converted ticket, or threshold
   requirements satisfying every inequality in (0.6); and
5. the same converted interface regenerated in the next Pascal child.

Under those hypotheses, Theorem 3.1 replaces the two-system Rado
intersection by one scalar Ferrers ledger.  Without item 1 the **direct
value-preserving** canonical acceptance graph is empty by Theorem 1.1;
without items 2--3 the
graph is not the physical graph; and without item 4 no Hall conclusion
follows from first-exit times.

Thus the remaining gate is no longer ambiguous:

\[
 \boxed{
 \text{canonical incomparable cross type}
 \xrightarrow{\text{protected type converter}}
 \text{nested first-exit type with threshold-Hall control}.}
\]
