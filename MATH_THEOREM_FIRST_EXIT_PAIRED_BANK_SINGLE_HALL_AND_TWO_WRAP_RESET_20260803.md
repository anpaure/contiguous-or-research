# First-exit paired banks reduce to one Hall graph and admit a two-ticket linear opening

**Date:** 2026-08-03  
**Status:** unconditional occurrence and opening theorem; exact conditional
replacement of the two-cross socket premise.  No computation is used.  The
result does not prove terminal type acceptance, transported-background
admissibility, or the Pascal overlay which absorbs inherited source
positions.

## 0. Outcome

Let the ground set have size `2r-1`, and let

\[
 T_0,T_1,\ldots,T_{W-1},
 qquad W={2r-1\choose r},
\tag{0.1}
\]

be a cyclic simple Johnson row containing every rank-`r` owner once.  Let
it have one cyclic literal depth-`d` source realization

\[
                         T_i=\bigcup_{h=i}^{i+d}A_h,
 \qquad A_h\ne\varnothing,
\tag{0.2}
\]

and put `R_i=T_i union T_(i+1)`.  Assume the immediate-upper row is
surjective:

\[
 \{R_i:i\in\mathbb Z_W\}={ [2r-1]\choose r+1}.
\tag{0.3}
\]

Repetitions are permitted and forced.  Define the first-exit distance

\[
 h_i=\min\{h\ge2:T_{i+h}\not\subseteq R_i\}.
\tag{0.4}
\]

The first-exit theorem gives `2<=h_i<=r+1` and two terminal occurrences

\[
 w_i=[i,i+d+h_i-1]_W,
 \qquad
 v_i=[i,i+d+h_i]_W,                                   
\tag{0.5}
\]

with values

\[
 \operatorname{OR}(w_i)=R_i,
 \qquad
 \operatorname{OR}(v_i)=V_i,
 \qquad |V_i|=r+2.
\tag{0.6}
\]

Combine this with the native q1 interval diamond.  Every seam `i` then has
one complete deterministic route bundle from its q1 lower port to the
**paired** terminals `(w_i,v_i)`.  In either q1 phase the `W` bundles are
pairwise occurrence-disjoint.  Hence, after a complete cap/guard/background
state is fixed, the two-coordinate terminal problem on these bundles is
not an intersection of two marginal gammoids: it is one ordinary bipartite
matching between logical tickets and accepted seam bundles.

The cyclic bank also has a bounded linear opening.  Open the source cycle
and repeat only the first `d` source letters, as in the standard
length-`W+d` owner realization.  There is a choice of cut for which exactly

\[
                              \boxed{2}                 
\tag{0.7}
\]

of the `W` first-exit paired bundles fail to fit in the linear word.  This
is sharp: every such opening loses at least two.

The reason is a new run ledger.  If the maximal constant runs in the
cyclic upper word `(R_i)` have lengths `L_1,...,L_J`, then

\[
 \sum_i h_i
 =2W+\sum_{j=1}^{J}{L_j(L_j-1)\over2}
 \le 2W+{r\over2}\left(W-{2r-1\choose r+1}\right)
 <3W.
\tag{0.8}
\]

Double-counting route losses over all opening cuts now proves (0.7).

Consequently, on the exact dual-role type face, the first-exit bank
**does replace** the former two-cross-socket capacity premise and exports
only two wrap tickets.  It does **not** replace the typed acceptance
premise.  The values available at seam `i` are specifically

\[
                         (R_i,V_i)
 \quad\text{of ranks}\quad(r+1,r+2),                  
\tag{0.9}
\]

and a canonical ray ticket which does not accept that occurrence/type pair
has no edge to bundle `i`.  The exact remaining gate is the Hall condition
in Section 3, together with background transport and the same-parity
overlay.

## 1. Complete first-exit bundles

Put

\[
 p_i=[i+1,i+d]_W,
 \qquad o_i=[i,i+d]_W,
 \qquad o_{i+1}=[i+1,i+d+1]_W,
\tag{1.1}
\]

and for `1<=t<=h_i` put

\[
                         z_{i,t}=[i,i+d+t]_W .          
\tag{1.2}
\]

Thus `z_(i,1)=q_i`, `z_(i,h_i-1)=w_i`, and
`z_(i,h_i)=v_i`.  The two phase bundles are

\[
\begin{aligned}
 \mathcal B_i^0&=(p_i,o_i,z_{i,1},\ldots,z_{i,h_i}),\\
 \mathcal B_i^1&=(p_i,o_{i+1},z_{i,1},\ldots,z_{i,h_i}).
\end{aligned}
\tag{1.3}
\]

Their values are respectively

\[
 P_i,T_i,
 \underbrace{R_i,\ldots,R_i}_{h_i-1\text{ occurrences}},V_i
\tag{1.4}
\]

and

\[
 P_i,T_{i+1},
 \underbrace{R_i,\ldots,R_i}_{h_i-1\text{ occurrences}},V_i.
\tag{1.5}
\]

The first two steps are the physical Boolean q1 diamond.  The middle steps
are nested interval occurrences with the same value `R_i`; the last step is
the first strict exit `R_i subset V_i`.  Thus (1.3) is a complete
occurrence-labelled route record.  A terminal model may retain every
plateau occurrence as a finite vertex or contract the plateau into one
canonical same-value relocation block.  Both representations have the
same endpoint capacities.

### Theorem 1.1 (bundle disjointness)

Assume `d+r+2<W`.  In either fixed phase, the bundles in (1.3) are pairwise
disjoint in every finite interval-address coordinate.  Their terminal pairs
`(w_i,v_i)` are two distinct coordinates, and all `2W` terminal addresses
are distinct.

### Proof

The port family has interval length `d`; the owner family has length
`d+1`; and every `z_(i,t)` has length `d+t+1>=d+2`.  Hence different
levels of (1.3) cannot collide.  Within the `z` family, the oriented cyclic
start is `i` and the length determines `t`.  Since all lengths are strictly
below `W`, an interval address determines both.  Therefore
`z_(i,t)=z_(j,u)` implies `i=j,t=u`.

The ports are injective in `i`; the phase-zero owners are injective; and in
phase one the translation `i mapsto i+1` is a permutation.  This proves
bundle disjointness.  The terminal statement is the case
`t=h_i-1,h_i`, also proved directly in the first-exit theorem. `square`

Overlap of constituent source positions is irrelevant: physical cells are
interval addresses.  If an auxiliary model node-prices every intermediate
**interval occurrence**, Theorem 1.1 still gives no cross-bundle collision
because the complete interval route records are indexed by distinct starts.
If instead it node-prices the underlying singleton source positions, the
routes may collide heavily.  That is the stronger boundary-source model,
not native OR-word capacity.

## 2. The constant-run identity

Decompose the cyclic word

\[
                         R_0,R_1,\ldots,R_{W-1}
\]

into maximal constant runs of lengths `L_1,...,L_J`.

### Lemma 2.1 (first exit equals remaining run plus one)

If `i` is in position `q`, numbered from zero, of a constant run of length
`L`, then

\[
                         h_i=L-q+1.                    
\tag{2.1}
\]

Consequently

\[
 \sum_i h_i
 =\sum_{j=1}^{J}{L_j(L_j+3)\over2}
 =2W+\sum_{j=1}^{J}{L_j(L_j-1)\over2}.                
\tag{2.2}
\]

### Proof

For `0<=t<h_i-1`, both consecutive owners
`T_(i+t),T_(i+t+1)` are rank-`r` facets of the same rank-`(r+1)` set
`R_i`.  Since they are distinct, their union is `R_i`, so

\[
                         R_{i+t}=R_i.
\]

At `t=h_i-1`, the second owner is the first one outside `R_i`, so the
upper value changes.  Thus exactly `h_i-1` consecutive upper edges starting
at `i` have label `R_i`, proving (2.1).  Summing
`L+1,L,...,2` over one run gives `L(L+3)/2`; sum over runs. `square`

### Lemma 2.2 (Catalan run bound)

Under upper surjectivity (0.3), equation (0.8) holds.

### Proof

A run of `L` equal upper labels uses `L+1` distinct owner facets of one
rank-`(r+1)` set.  There are only `r+1` facets, so

\[
                              L\le r.                  
\tag{2.3}
\]

Every one of the

\[
                         U={2r-1\choose r+1}
\]

upper values labels at least one run, so `J>=U`.  Hence

\[
\begin{aligned}
 \sum_j{L_j(L_j-1)\over2}
 &\le {r\over2}\sum_j(L_j-1)\\
 &= {r\over2}(W-J)\\
 &\le {r\over2}(W-U).
\end{aligned}
\tag{2.4}
\]

Finally

\[
 {U\over W}={r-1\over r+1},
 \qquad W-U={2W\over r+1}.
\tag{2.5}
\]

Substitute (2.5) into (2.2)--(2.4):

\[
 {1\over W}\sum_i h_i
 \le2+{r\over r+1}<3.
\tag{2.6}
\]

This proves (0.8). `square`

The argument needs surjectivity, not upper injectivity.  Repeated upper
values are completely allowed; their total run excess is paid by the
forced Catalan multiplicity surplus.

## 3. Exact acceptance graph

Fix one complete cap, endpoint, deadline, residence, occurrence, and
transported-background state `c`.  Let `I` be its logical terminal tickets.
For a chosen q1 phase, define a bipartite graph

\[
                         H_c\subseteq I\times\mathbb Z_W
\tag{3.1}
\]

by joining ticket `x` to seam `i` precisely when:

1. the complete route `mathcal B_i^epsilon` is legal after the fixed
   background reservation;
2. the two physical occurrence coordinates `(w_i,v_i)` are both admissible;
3. ticket `x` accepts their complete paired type, including the values
   `(R_i,V_i)` and every fixed flag/guard; and
4. assigning both roles to that one complete bundle creates no unrecorded
   cross-ticket resource.

Let `Z` be any set of seam indices unavailable at the chosen linear
opening.

### Theorem 3.1 (one-Hall reduction)

The maximum number of tickets serviceable by the first-exit paired bank is
the maximum matching size in

\[
                         H_c-Z.
\]

Its exact deficiency is

\[
 \boxed{
 \delta_{\rm exit}(c,Z)
 =\max_{X\subseteq I}
   \bigl(|X|-|N_{H_c}(X)\setminus Z|\bigr)_+.}
\tag{3.2}

### Proof

One accepted edge `x i` selects the complete deterministic bundle at seam
`i`, including both terminal coordinates.  By Theorem 1.1, bundles with
distinct seam indices are capacity-disjoint in the native interval
coordinates.  The complete state in the definition of `H_c` has already
priced every other shared resource.  Therefore a set of tickets is jointly
serviceable exactly when it has distinct neighboring seam indices.  This
is a bipartite matching, and (3.2) is Hall deficiency. `square`

This is the precise replacement for the old two-cross-socket premise.  It
simultaneously resolves both occurrence coordinates and their product
closure.  It does not make `H_c` complete.  In particular, a rank, value,
flag, or cap mismatch deletes the corresponding edge before Hall is tested.

## 4. Exactly two wrap losses

Choose a cut `c` of the cyclic source order.  Write

\[
                         t_c(i)=(i-c)\bmod W
 \quad\text{in }\{0,\ldots,W-1\}.                    
\tag{4.1}
\]

The standard linear owner word consists of this one revolution followed by
the first `d` source letters, and has length `W+d`.  Bundle `i` fits in the
linear word exactly when its longest interval `v_i` fits, namely

\[
                         t_c(i)+h_i\le W-1.            
\tag{4.2}
\]

Put

\[
 Z_c=\{i:t_c(i)+h_i\ge W\},
 \qquad \ell(c)=|Z_c|.                                 
\tag{4.3}
\]

### Theorem 4.1 (two-ticket opening)

Under the hypotheses of Section 0, some cut `c` has

\[
                         \ell(c)=2.                    
\tag{4.4}
\]

### Proof

For a fixed ticket `i`, as `c` runs over all `W` cuts, `t_c(i)` runs once
through `0,...,W-1`.  Exactly `h_i` of these values satisfy (4.3).  Double
counting gives

\[
 {1\over W}\sum_c\ell(c)={1\over W}\sum_i h_i<3       
\tag{4.5}
\]

by Lemma 2.2.  Hence some integer `ell(c)` is at most two.

For every cut, the tickets starting at relative positions `W-1` and `W-2`
belong to `Z_c`, because every `h_i>=2`.  Thus `ell(c)>=2`.  The minimizing
cut therefore has equality. `square`

The conclusion is stronger than the generic first-exit bound
`ell(c)<=r+1`.  Without upper surjectivity, (2.4) is unavailable and the
first-exit theorem alone does not give a constant opening loss.

There is also an exact width distinction.  The immediate q1 upper interval
`q_i=[i,i+d+1]` loses only the single start at relative position `W-1` in
the standard `W+d` opening.  The paired first-exit bank includes
`v_i=[i,i+d+h_i]` with `h_i>=2`, and therefore loses at least the last two
starts.  Thus a one-wrap statement is correct for the q1 bank alone but not
for the full paired bank; Theorem 4.1 gives the sharp replacement `2` under
upper surjectivity.

## 5. Same-parity reset consequence and its exact premise

The one-terminal recurrence of
`MATH_THEOREM_AD_ODD_PASCAL_TRIANGULAR_ONE_TERMINAL_HOST_RECURRENCE_20260801.md`
uses a clause demanding two occurrence-exact cross-ray systems in one
physical split.  On a child satisfying Sections 0--4, that clause may be
replaced proof-safely by:

> **First-exit paired-bank clause.**  Fix one complete child cap/background
> state `c`, choose the two-ticket opening of Theorem 4.1, and prove the
> Hall bound `delta_exit(c,Z_c)<=e_m`.  Every selected edge represents the
> complete two-coordinate bundle, not two separately combined marginal
> paths.

No fresh source split and no additional `W`-socket bank is required.  The
first-exit terminals are already intervals of the child baseline.  If an
explicit Pascal overlay absorbs all but `kappa_m` inherited charged source
positions into the child baseline, while the other defect terms retain the
notation of the old recurrence, the same bookkeeping proof gives

\[
 \boxed{
 C_{m+1}
 \le
 \kappa_m+2e_m+\rho_m+\beta_m+u_m.}
\tag{5.1}
\]

Here:

* `e_m` is the logical-ticket Hall deficiency (3.2), including the two
  unavailable wrap bundles; the coefficient two is the unconditional
  repair bound obtained by appending the two declared target values of
  each omitted two-coordinate ticket;
* `rho_m` is trace/component reset cost outside the paired bank;
* `beta_m` is transported lower/background casualty count;
* `u_m` is uncovered upper-target count; and
* `kappa_m<=C_m` is the inherited terminal-position charge which the
  independently proved overlay failed to absorb.

If the ticket semantics separately proves that one appended literal cell
repairs an omitted logical ticket, the coefficient of `e_m` may be reduced
from two to one.  That identification is not assumed here.

Equation (5.1) is a conditional bookkeeping theorem, not a consequence of
the cyclic bank alone.  If one proves a genuine reset with `kappa_m=0` and
uniformly bounded `e_m+rho_m+beta_m+u_m`, then the exported state is bounded
independently of the parent.  In the ideal complete-acceptance case for a
diagonal `W`-ticket system, `e_m=2` solely from the wrap cut.

The new bank does not prove `kappa_m=0`.  In particular, the scalar Pascal
recurrence and existence of the intervals `(w_i,v_i)` do not supply the
order-preserving overlay map, the integral residual forest, or admissible
full-block transport.  These remain the exact nonterminal rows of the
same-parity regeneration theorem.

## 6. Proof-safe answer to the socket question

The answer is a dichotomy.

### What is replaced

On the native interval-address face, after one cap state is fixed, the
first-exit construction gives:

* two distinct terminal occurrence coordinates per accepted seam;
* pairwise-disjoint complete two-coordinate bundles;
* automatic product closure inside each deterministic bundle;
* no new physical positions; and
* an opening with exactly two unavailable seams under upper surjectivity.

Thus a second abstract `W`-socket bank, two separate marginal Rado proofs,
and a later product-closure inference are unnecessary.  They are replaced
by the single Hall graph (3.1).

### What is not replaced

The construction supplies only the paired type `(R_i,V_i)` in the fixed
state.  It does not prove:

1. that the canonical two-cross ray ticket accepts this pair;
2. that the selected upper occurrences remain available after the
   transported background is fixed;
3. that the child Pascal construction is a simple upper-surjective q1
   diagonal;
4. that inherited charged source positions contract into the child
   baseline; or
5. lower compilation, residence, the residual forest, or arbitrary-width
   upper preservation.

Therefore the two-cross **capacity premise** is removed, while the
coinstantiated type/background/overlay premise remains the exact gate.
