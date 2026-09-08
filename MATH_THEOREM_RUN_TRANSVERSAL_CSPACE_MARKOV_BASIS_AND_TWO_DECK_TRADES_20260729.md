# Run-transversal `c`-space, its legal move lattice, and simultaneous two-deck trades

Date: 2026-07-29

Status: exact normal form; exact erosion tower through residence depth `d`; complete
same-run-order legal-displacement criterion; complete Markov basis inside each
endpoint-permutation chamber; rigorous disconnection of the bounded separate
endpoint-swap graph; exact middle/q1 simultaneous-trade criterion; line-by-line
audit of the frozen `anneal3.cpp`; tiny exhaustive calibration at `k=3,5,7`;
and an exact support-at-most-three `k=15` boundary atlas.  No compiler/Hall
conclusion and no `k=15` existence claim is made.

## 1. Main conclusions

Let

\[
 k=2m+1,\qquad r=m+1,\qquad
 W=\binom{k}{r}=kN,
\]

fix a depth `0<=d<r` as in the compiler regime, and let a unit-voltage
trace `c in {0,1}^W` define

\[
 T_i=\{x\in\mathbb Z_k:c_{i-xN}=1\}.
 \tag{1.1}
\]

The exact structural conclusions are as follows.

1. Rank `r` and Johnson adjacency are equivalent to class weight `r`
   together with one `c`-run start and one `c`-run end in every residue
   modulo `N`.  Under boundary transversality, the `N` rank equations reduce
   to the one total-weight equation `|c|=rN`.

2. A run-transversal word has exactly `N` one-runs.  If every run has length
   at least `d+1`, then every lower intersection row through depth `d` has
   the pointwise expected rank.  More strongly, these rows form a nested
   tower of strict equivariant Johnson walks, and consecutive erosion rows
   are related by the literal derivative identity

   \[
   \mathcal D P^{(q+1)}=P^{(q)}.
   \tag{1.2}
   \]

3. The abbreviated description “two endpoint permutations plus a
   run-length composition” is incomplete.  The exact data also contain the
   gap lifts, cyclic phase, and congruence compatibility.  Once the start and
   end residue permutations are fixed, the legal states form a product of
   two integer simplices.  Its complete Markov basis consists of `N`-block
   transfers of run surplus and `N`-block transfers of gap surplus.

4. Across permutation chambers, a legal move is exactly a coupled start/end
   boundary displacement satisfying four explicit conditions.  Separate
   start and end transpositions span the unconstrained permutation lattice,
   but they are not a Markov basis under the positivity bounds.  Simultaneous
   alternating circulations can be genuinely necessary.

5. The active `anneal3.cpp` loop samples only separate `endSwap` and
   `startSwap`.  It preserves a nontrivial endpoint barycentre and therefore
   splits the indexed state graph into phase sectors.  It also fails to
   validate three seed preconditions on which its preservation claims rely.

6. At a middle/q1-perfect seed, a useful perturbation must lie in the
   simultaneous kernel of the middle-necklace deck and the adjacent-
   intersection-necklace deck.  The exact localized signed equations are
   given in Section 8.  A one-column non-inert trade can only be a phase
   diamond.  Middle-orbit reassignment needs at least two columns, and every
   support-two instance is a coupled rectangle.  These are conditional
   normal forms, not existence assertions.

7. For the audited resident `k=15` seed, the exact atlas of every nonzero
   same-run-order displacement supported on at most three run slots contains
   46,928 legal states and no middle-perfect state.  Thus its perfect-face
   boundary girth is at least four.  This is seed-specific and supplies no
   bounded Markov basis.

The last item is the correct next move target.  Generic run-state connectivity
does not imply that the perfect middle/q1 face is connected, and neither
statement implies compiler/Hall compatibility.

## 2. Exact seam equations and run-transversal normal form

All indices below are cyclic.  Define the start and end indicators

\[
 A_p=c_p(1-c_{p-1}),\qquad B_p=c_p(1-c_{p+1}),
 \tag{2.1}
\]

and the residue loads

\[
 h_j=\sum_{p\equiv j\pmod N}c_p,\quad
 a_j=\sum_{p\equiv j\pmod N}A_p,\quad
 b_j=\sum_{p\equiv j\pmod N}B_p.
 \tag{2.2}
\]

### Theorem 2.1 (exact seam identity)

For `i congruent to j mod N`, one has

\[
 |T_i\setminus T_{i-1}|=a_j,
 \qquad
 |T_{i-1}\setminus T_i|=b_{j-1},
 \tag{2.3}
\]

and hence

\[
 h_j-h_{j-1}=a_j-b_{j-1},
 \qquad
 |T_i\mathbin\triangle T_{i-1}|=a_j+b_{j-1}.
 \tag{2.4}
\]

#### Proof

Coordinate `x` enters between `T_(i-1)` and `T_i` precisely when

\[
 c_{i-1-xN}=0,\qquad c_{i-xN}=1.
\]

As `x` ranges over `Z_k`, the second positions are exactly the `k` positions
in residue class `j`.  This counts `a_j`.  The exit statement is the same
argument for a `1 to 0` boundary whose last one lies in residue `j-1`.
Subtracting the two ranks and adding the two disjoint differences gives
(2.4).  ∎

### Corollary 2.2 (normal form)

Assume `h_j=r` for every `j`.  Then every seam is a Johnson edge if and only
if

\[
 a_j=b_j=1\qquad(j\in\mathbb Z_N).
 \tag{2.5}
\]

Conversely, (2.5) makes all `h_j` equal, so inside the boundary-transversal
class the rank equations are equivalent to

\[
 \sum_pc_p=rN.
 \tag{2.6}
\]

In particular, there are exactly `N` cyclic one-runs.

#### Proof

Equal adjacent ranks make the two quantities in (2.3) equal.  A Johnson
edge has symmetric difference two, so both are one.  Conversely (2.5) makes
(2.3) a one-delete/one-insert seam.  Equation (2.4) makes every `h_j`
equal, and their sum is `|c|`; (2.6) therefore makes the common value `r`.
Finally, the number of cyclic runs is the total number of starts, namely
`sum_j a_j=N`.  ∎

The strict voltage identity is

\[
 T_{i+N}=T_i+1.
 \tag{2.7}
\]

The rotation actions on ranks `r` and `r-1` are free because
`gcd(k,r)=gcd(k,r-1)=1`.  Thus middle Hamiltonicity is exactly the
pairwise inequivalence of `T_0,...,T_(N-1)` under rotation, while exact q1
is the separate pairwise inequivalence of their adjacent intersections.
Neither follows from (2.5).

## 3. Exact run/gap bijection

Anchor at the unique run start congruent to zero modulo `N`, and let its lift
be

\[
 S_0=\eta N,\qquad \eta\in\mathbb Z_k.
\]

List the runs chronologically.  Write

\[
 S_i\le E_i<S_{i+1},\qquad
 \ell_i=E_i-S_i+1,\qquad
 g_i=S_{i+1}-E_i-1,
 \tag{3.1}
\]

with `S_N=S_0+W`.  Put

\[
 \pi_i=S_i\pmod N,\qquad \rho_i=E_i\pmod N.
 \tag{3.2}
\]

### Theorem 3.1 (exact data)

A rooted residence-legal rank-`r` Johnson trace is equivalent to the data

\[
 \eta\in\mathbb Z_k,\quad
 \ell_i\ge h:=d+1,\quad g_i\ge1,
 \tag{3.3}
\]

\[
 \sum_i\ell_i=rN,\qquad
 \sum_i g_i=(k-r)N,
 \tag{3.4}
\]

where both `pi` and `rho` are permutations of `Z_N` and `pi_0=0`.
These data reconstruct `c` uniquely, and maximal-run decomposition recovers
the data uniquely.

For a fixed pair `(pi,rho)`, let `L_i` be the least integer at least `h`
congruent to

\[
 \rho_i-\pi_i+1\pmod N,
\]

and let `G_i` be the least positive integer congruent to

\[
 \pi_{i+1}-\rho_i-1\pmod N.
\]

Then every state in this chamber has the unique form

\[
 \ell_i=L_i+Np_i,\qquad g_i=G_i+Nq_i,\qquad p_i,q_i\ge0,
 \tag{3.5}
\]

where

\[
 \sum_ip_i=P:=\frac{rN-\sum_iL_i}{N},
 \qquad
 \sum_iq_i=Q:=\frac{(k-r)N-\sum_iG_i}{N}.
 \tag{3.6}
\]

The chamber is nonempty if and only if `P,Q` are nonnegative integers.

#### Proof

Equations (3.1) immediately give the two congruences defining `L_i,G_i`.
The lower bounds make the residual lifts nonnegative.  Conversely, (3.5)
gives

\[
 S_{i+1}\equiv
 \pi_i+(\rho_i-\pi_i+1)+(\pi_{i+1}-\rho_i-1)
 \equiv\pi_{i+1}\pmod N.
\]

The total equations close the lift after `W` positions.  Filling every
`[S_i,E_i]` with ones and every following gap with zeros constructs the
word.  Positive gaps make these exactly its maximal runs.  Corollary 2.2
then supplies the rank and Johnson assertions.  ∎

This proves the flaw in the shorter “two permutations plus a length
composition” parametrization: the gap vector and its lift equations cannot
be omitted.  For example, at `k=7,N=5,h=3`, the same endpoint permutations
and run lengths

\[
 \pi=(0,4,3,2,1),\quad \rho=(2,1,0,4,3),\quad
 \ell=(3,3,3,3,8)
\]

admit both

\[
 g=(1,1,1,1,11)
 \quad\hbox{and}\quad
 g=(1,1,1,6,6).
\]

Also, not every permutation pair is feasible: `pi=rho=(0,1,2,3,4)`
forces every run length to be `1 mod 5`, so residence forces each to be at
least six, contradicting total run mass twenty.

## 4. Exact erosion and derivative tower through depth `d`

Use the past-window convention requested for the compiler envelope:

\[
 P_i^{(q)}=\bigcap_{t=0}^{q}T_{i-t},
 \qquad 0\le q\le d.
 \tag{4.1}
\]

Its scalar trace is

\[
 p_u^{(q)}=\prod_{t=0}^{q}c_{u-t}.
 \tag{4.2}
\]

### Theorem 4.1 (self-similar lower tower)

For every `q<=d`:

1. a `c`-run `[S_i,E_i]` becomes `[S_i+q,E_i]`;
2. the eroded word has exactly `N` runs, start residues shifted uniformly by
   `q`, and the same end residues;
3. every class sum is `r-q`;
4. `P^(q)` is a strict equivariant Johnson walk of pointwise rank `r-q`;
5. if `q<d` and `(D F)_i=F_i union F_(i+1)`, then

   \[
   \boxed{\mathcal D P^{(q+1)}=P^{(q)}}.
   \tag{4.3}
   \]

#### Proof

Since every original run has length at least `d+1`, (4.2) erodes exactly
its first `q` positions and never deletes a whole run.  The new run length is
`ell_i-q`, so its total one-mass is

\[
 \sum_i(\ell_i-q)=rN-qN=(r-q)N.
\]

Uniformly shifting every start residue and leaving every end residue fixed
preserves both transversals.  Corollary 2.2 therefore gives class weight
`r-q`, Johnson adjacency, and equivariance.

For (4.3), a run of `p^(q+1)` is `[S_i+q+1,E_i]`.  Its occurrence at
position `u+1` supplies `[S_i+q,E_i-1]` in the `u` trace.  The union with
`[S_i+q+1,E_i]` is exactly `[S_i+q,E_i]`.  The eroded gaps remain nonempty,
so no two runs merge.  ∎

Equivalently, adjacent Johnson steps give the pointwise lower bound
`|P_i^(q)|>=r-q`, while summing all windows over all coordinate traces gives
the average exactly `r-q`; equality is therefore forced everywhere.

For future windows `intersection_(t=0)^q T_(i+t)`, starts remain fixed and
ends shift back by `q`.  The rank and Johnson conclusions are identical.
The convention must be fixed before saying which endpoint shifts.

The theorem proves exact ranks and nested chronology.  It does not prove
distinctness of any erosion row, target coverage, or compiler ports.

## 5. Complete legal boundary-displacement theorem

Fix one chronological labeling of the runs.  Let another same-order state
have

\[
 S_i'=S_i+u_i,\qquad E_i'=E_i+v_i,
 \tag{5.1}
\]

where `u,v in Z^N` and cyclically `u_N=u_0`.

### Theorem 5.1 (necessary and sufficient legal move)

The displacement `(u,v)` carries one legal rank-`r`, residence-`h` state
to another if and only if

\[
 \ell_i+v_i-u_i\ge h,
 \tag{5.2}
\]

\[
 g_i+u_{i+1}-v_i\ge1,
 \tag{5.3}
\]

\[
 \sum_i(v_i-u_i)=0,
 \tag{5.4}
\]

and both residue lists

\[
 (S_i+u_i\bmod N)_i,\qquad(E_i+v_i\bmod N)_i
 \tag{5.5}
\]

are permutations of `Z_N`.

Conversely, every same-run-order legal trade is uniquely of this form after
the cyclic run labels and integer lifts are aligned.

#### Proof

Equations (5.2) and (5.3) are exactly the new run and gap lower bounds.
Equation (5.4) preserves total one-mass, because

\[
 \sum_i\ell_i'=\sum_i\ell_i+\sum_i(v_i-u_i).
\]

Condition (5.5) is exactly start/end transversality.  The inequalities keep
the chronological order strict, and Corollary 2.2 turns transversality plus
the preserved total mass into all class sums and all Johnson seams.  The
converse follows by taking the literal differences of aligned boundary
lifts.  ∎

This is the complete legal move normal form.  It includes:

- an end exchange: `u=0`, `v_a=delta`, `v_b=-delta`;
- a start exchange: `v=0`, `u_a=-delta`, `u_b=delta`;
- an `N`-unit endpoint transfer;
- a whole-run slide: `u_a=v_a=plus or minus N`;
- and genuinely coupled, multi-run alternating circulations.

Every move satisfying (5.2)--(5.5) also preserves all structural conclusions
of Theorem 4.1 through depth `d`.

## 6. Chamber Markov basis and connectivity boundary

Fix `(pi,rho,eta)`.  By Theorem 3.1 its state set is

\[
 \{p\in\mathbb Z_{\ge0}^N:\sum p_i=P\}
 \times
 \{q\in\mathbb Z_{\ge0}^N:\sum q_i=Q\}.
 \tag{6.1}
\]

### Theorem 6.1 (complete within-chamber Markov basis)

The moves

\[
 p\longmapsto p+e_a-e_b\quad(p_b>0),
 \tag{6.2}
\]

and

\[
 q\longmapsto q+e_a-e_b\quad(q_b>0)
 \tag{6.3}
\]

form a complete legal Markov basis in every nonempty chamber.

#### Proof

Each move transfers one `N`-block of run or gap surplus and remains in the
nonnegative simplex.  Repeatedly transfer every surplus unit whose coordinate
differs from a chosen target.  This connects any two weak compositions of
the same total.  The two factors in (6.1) are independent.  ∎

In physical boundary coordinates, (6.2)--(6.3) can shift a whole contiguous
block of runs by `N`; they are nonlocal moves even though they are unit moves
in chamber coordinates.

Across chambers, differences of the two permutation matrices decompose into
even alternating cycles.  Without (5.2)--(5.3), transpositions generate this
permutation lattice.  Under the inequalities, however, start and end cycles
may have to be executed simultaneously.  The exact legal moves are precisely
the displacements satisfying (5.2)--(5.5); their primitive alternating-
circulation decomposition is the natural search target.  No uniform
cross-chamber Graver basis or support bound is proved here.

Thus there are two precise connectivity statements:

- the graph using **all** legal displacements (5.2)--(5.5) is connected
  after aligning cyclic run order, indeed any two states differ by one such
  displacement;
- the graph generated by separate bounded start/end swaps need not be
  connected.

### Counterexample 6.2 (separate moves are not a Markov basis)

This is a small explicit abstract run fiber, not a central-layer instance.
Take

\[
 N=3,\quad k=5,\quad r=h=2.
\]

The two legal states

\[
 \ell=(2,2,2),\quad g=(3,3,3),\qquad c=(11000)^3,
\]

and

\[
 \ell=(2,2,2),\quad g=(2,2,5),\qquad
 c'=110011001100000
\]

have class sums two and both endpoint transversals.  Every run is tight, so
every separate nonzero start or end exchange would shrink a run below `h`.
There is no run-surplus donor, while pure gap `N`-transfers and `N`-slides
cannot change the gap residues.  Nevertheless the coupled displacement

\[
 u=v=(0,-1,-2)
\]

maps the first state to the second while leaving all run lengths unchanged.
This proves that simultaneous start/end circulation is genuinely necessary.

## 7. Exact `anneal3.cpp` audit

The final inspected source is the frozen copy

```text
scratch/anneal3_sha83d5_audit.cpp
SHA-256 83d5c1b79f07bbf3927aa8a22f21b61533edcd0481b7bb8af24d2adffb40cf20
```

The live external file changed during the audit from SHA-256
`b3cbd4d9...` (391 lines) to the frozen hash above (428 lines).  All line
claims below refer to the latter.

### 7.1 Correct move vectors

Let `u_i` now denote a standard basis vector indexed by runs.  The active
end move has

\[
 \delta=[E_b-E_a]_N,
\]

\[
 \Delta E=\delta(u_a-u_b),\quad \Delta S=0,
\]

\[
 \Delta\ell=\delta(u_a-u_b),\quad
 \Delta g=\delta(-u_a+u_b).
 \tag{7.1}
\]

The active start move has

\[
 \delta=[S_a-S_b]_N,
\]

\[
 \Delta S=\delta(-u_a+u_b),\quad \Delta E=0,
\]

\[
 \Delta\ell=\delta(u_a-u_b),\quad
 \Delta g=\delta(-u_{a-1}+u_{b-1}).
 \tag{7.2}
\]

The donor-length and recipient-gap guards are exactly the inequalities
needed to preserve `ell>=D+1` and `g>=1`.  The flipped-in and flipped-out
positions have the same residue multiset, so every class sum is preserved.
The two endpoint residues are exchanged.  Conditional on a valid seed, these
moves are structurally sound.

In the unconstrained algebraic lattice, applying the same ordered exchange
twice produces the corresponding `plus or minus N` transfer, so the defined
`transferEnd` adds no lattice direction.  The two successive swaps are both
legal only when the direct transfer's full `N`-block donor/gap guards hold.
The direct move can still matter as an energy proposal.  It is not sampled by
the loop, and no slide exists despite the header comment.

### 7.2 Exact missing invariant

For lifted starts and ends define

\[
 \Phi_S=\frac{\sum_iS_i-\binom N2}{N}\pmod k,
 \qquad
 \Phi_E=\frac{\sum_iE_i-\binom N2}{N}\pmod k.
 \tag{7.3}
\]

These are integral because both residue rows are permutations.  Moreover

\[
 \Phi_E-\Phi_S=r-1\pmod k.
 \tag{7.4}
\]

Every sampled swap preserves `sum S_i` and `sum E_i` separately, hence fixes
both phases.  A general legal displacement changes both by

\[
 \frac{\sum_i u_i}{N}=\frac{\sum_i v_i}{N}\pmod k.
\]

A legal `N`-slide or a global chronology rotation supplies the missing
direction.  Thus the literal indexed swap graph has at least `k` phase
sectors.  Quotienting global rotation removes this particular obstruction,
but not the positivity obstruction of Counterexample 6.2.

### 7.3 Missing seed validation

The parser checks the number of runs and whether every endpoint residue is
represented.  It does not check:

- that input entries are binary;
- that total weight is `rN`, equivalently that the common class sum is `r`;
- that every pre-existing run has length at least `D+1`.

Two exact accepted-seed counterexamples at `k=5` are:

```text
1111011110
```

which has two transversal runs of lengths four and four but class sum four
instead of three, and

```text
0001101111
```

which has correct total/class sums and transversal endpoints but run lengths
two and four instead of minimum three.  The latter defect can make a rejected
repair unrollable: the inverse move correctly refuses to recreate the illegal
length-two donor and the program aborts.  An early zero-energy exit can also
emit an invalid seed.

The inactive `transferEnd(a,b)` additionally needs `a!=b`.  On the retained
`k=15` NAND seed, `transferEnd(0,0)` passes both numerical guards, applies
noncancelling bit flips, cancels only its metadata updates, and corrupts the
run representation.

### 7.4 Objective and incremental counters

For `k=15`, the incremental `tau` bit map, affected-window interval, and
popcount-separated shared counters are correct for the objective actually
implemented.  That objective uses weights

\[
 (12,12,8,3),
\]

not the stale `(300,300,5,5)` in the header.  Upper unions are scored only
at widths two through eight.  Hence energy zero is a mathematically
sufficient certificate for full existential upper coverage: every upper
orbit already has a witness of one of those widths.  It is stronger than
necessary and can reject a valid carrier whose first witness is wider.  Every
retained candidate still needs the independent exact upper oracle as
fail-closed verification of the counters and artifact.

There are also minor out-of-scope defects for a null seed path, unrestricted
`K`, and rank-zero q2 counting at `k=3`.

## 8. The useful move: simultaneous middle/q1 deck trades

Let

\[
 \mu_j=[T_j]_\rho,\qquad
 X_j=T_j\cap T_{j+1},\qquad
 \lambda_j=[X_j]_\rho,
 \tag{8.1}
\]

where `T_N=rho T_0`.  Assume both `mu` and `lambda` are bijections.  For a
second structurally legal trace `c'`, put

\[
 A=\{j:T'_j\ne T_j\},
 \qquad
 \partial A=A\cup(A-1).
 \tag{8.2}
\]

### Theorem 8.1 (localized two-deck kernel)

The new trace is again middle/q1 perfect if and only if

\[
 \boxed{
 \sum_{j\in A}
   (\mathbf e_{\mu'_j}-\mathbf e_{\mu_j})=0}
 \tag{8.3}
\]

and

\[
 \boxed{
 \sum_{j\in\partial A}
   (\mathbf f_{\lambda'_j}-\mathbf f_{\lambda_j})=0.}
 \tag{8.4}
\]

#### Proof

Middle columns outside `A` are literally unchanged.  Adjacent intersections
outside `partial A` have two unchanged endpoints and are also literally
unchanged.  Since each old global count vector is the all-ones vector,
the two localized signed differences vanish exactly when both new global
count vectors are again all ones.  ∎

Equivalently, the old and new position-to-color perfect matchings differ by
even alternating cycles in each deck.  Since the two relevant rotation
actions are free, there are unique phases and transport permutations with

\[
 T'_j=\rho^{a_j}T_{\sigma_M(j)},
 \qquad
 X'_j=\rho^{b_j}X_{\sigma_Q(j)}.
 \tag{8.5}
\]

They are not independent.  They obey the literal coupling equation

\[
 \boxed{
 \rho^{b_j}X_{\sigma_Q(j)}
 =
 \rho^{a_j}T_{\sigma_M(j)}
 \cap
 \rho^{a_{j+1}+\varepsilon_j}T_{\sigma_M(j+1)},}
 \tag{8.6}
\]

where `epsilon_(N-1)=1` and all other `epsilon_j=0`.  A legal run-boundary
move must satisfy (5.2)--(5.5) in addition to this two-deck equation.
At the helical boundary, the convention is `a_N=a_0` and
`sigma_M(N)=sigma_M(0)` before applying the displayed unit twist.

### 8.1 Literal finite criterion

Set

\[
 t_{j,x}=c_{j-xN},\qquad
 \Delta_{j,x}=c'_{j-xN}-c_{j-xN}.
\]

Class preservation is

\[
 \sum_x\Delta_{j,x}=0.
 \tag{8.7}
\]

The exact start-boundary difference in class `j` is

\[
 \sum_{p\equiv j}
 \left[
 \Delta_p(1-c_{p-1})-c_p\Delta_{p-1}
 -\Delta_p\Delta_{p-1}
 \right],
 \tag{8.8}
\]

and the end-boundary formula is the same expression with `p-1` replaced by
`p+1`.  Structural legality requires both to vanish, together with binaryness
and the run inequalities.  The exact q1 bit difference is

\[
 \Delta X_{j,x}
 =\Delta_{j,x}t_{j+1,x}
  +t_{j,x}\Delta_{j+1,x}
  +\Delta_{j,x}\Delta_{j+1,x}.
 \tag{8.9}
\]

Canonicalize `t+Delta` and `X+Delta X`, then impose (8.3)--(8.4).  This is a
complete finite test in trace variables, not a heuristic energy condition.

### 8.2 Primitive sizes and the first useful atlas

For a same-run-order displacement `(u,v)`, let `c^(u,v)` be the word whose
lifted one-runs are

\[
 [S_i+u_i,E_i+v_i],
\]

and set

\[
 \Delta^{u,v}_p=c^{u,v}_p-c_p,
 \qquad
 A(u,v)=\{j:\Delta^{u,v}_{j-xN}\ne0\text{ for some }x\in\mathbb Z_k\}.
 \tag{8.10a}
\]

Thus (5.2)--(5.5) are the complete structural test on `(u,v)`, while
(8.3)--(8.4), evaluated using (8.9), are the complete simultaneous-deck
test.  Call a simultaneous trade **deck-inert** if every `mu_j` and every
`lambda_j` remains at the same position; otherwise call it **non-inert**.

### Theorem 8.2 (smallest non-inert simultaneous trades)

Assume `N>1` and the seed is middle/q1 perfect.

1. A structurally legal displacement with `A(u,v)={a}` is a simultaneous
   trade if and only if

   \[
    \mu'_a=\mu_a,
    \qquad
    \{\lambda'_{a-1},\lambda'_a\}
      =\{\lambda_{a-1},\lambda_a\}
    \tag{8.10b}
   \]

   as multisets.  It is non-inert if and only if the two q1 colors are
   transposed.  This is the one-column **phase diamond**.

2. Suppose `A(u,v)={a,b}` and the trade reassigns a middle color.  Then it is
   a simultaneous trade if and only if

   \[
    \mu'_a=\mu_b,
    \qquad
    \mu'_b=\mu_a,
    \qquad
    \{\lambda'_j:j\in\partial\{a,b\}\}
      =\{\lambda_j:j\in\partial\{a,b\}\}
    \tag{8.10c}
   \]

   as multisets.  Its middle matching overlay is exactly one alternating
   four-cycle.  This is the two-column **rectangle**; its q1 overlay is the
   cycle decomposition induced on the at most four halo positions.

Consequently support one can be non-inert only via a phase diamond.
Middle-orbit reassignment requires at least two columns, and every
support-two reassigning trade is exactly a coupled rectangle.  Thus one and
two are the smallest arities not ruled out by deck balance alone.  Existence
is seed-dependent: the theorem is a characterization, not an assertion that
either object occurs in a globally legal run embedding.

#### Proof

If only column `a` changes, (8.3) reduces to `mu'_a=mu_a`; the only q1
positions that can change are `a-1,a`, so (8.4) is precisely the two-element
multiset equality in (8.10b).  Since the old q1 deck is a permutation, these
two colors are distinct; their only nonidentity recycling is their
transposition.

If exactly `a,b` change, middle balance says

\[
 \{\mu'_a,\mu'_b\}=\{\mu_a,\mu_b\}.
\]

The colors `mu_a,mu_b` are distinct.  A middle-reassigning solution is
therefore forced to transpose them, and the overlay of the old and new
position-to-color matchings is one alternating four-cycle.  The changed q1
positions are exactly contained in `partial{a,b}`; applying (8.4) gives the
last multiset equality in (8.10c).  The converses follow directly from
Theorem 8.1.  ∎

A nonempty support of a permutation difference cannot have size one.  Hence:

- a middle-orbit-reassigning trade needs at least two changed middle colors;
- its degree-two primitive is a coupled matching-overlay four-cycle, namely
  a two-color transposition whose entire affected q1 halo also satisfies
  (8.4) and (8.6);
- if the seed has no legal singleton phase reroute of any type and no legal
  two-column simultaneous trade of any type, then the first possible trade
  has at least three changed literal columns and must be sought as a coupled
  alternating circulation, not as an independent endpoint swap.

There is an important qualification.  If `A={a}`, middle balance forces only

\[
 \mu'_a=\mu_a.
\]

The literal middle representative can change phase.  The two incident q1
colors must then either remain pointwise fixed or transpose.  This is locally
sharp at `k=9`:

\[
 L=107,\quad T=79,\quad R=93,\quad T^*=121=\rho^3T.
\]

Both `L-T-R` and `L-T^*-R` are Johnson paths, and their q1 orbit colors are

\[
 (75,77)\longmapsto(77,75).
\]

Thus no universal theorem can demand three changed columns.  Residence and
global run embedding are additional gates for this local diamond.

For a family of proposed swaps whose q1 halos `A union (A-1)` are pairwise
disjoint and whose literal boundary effects commute, define each signed
signature to be the pair of vectors in (8.3)--(8.4).  Their union is a
simultaneous trade exactly when the signatures sum to zero and the combined
boundary displacement satisfies (5.2)--(5.5).  In that disjoint-halo atlas,
two swaps work exactly when their signatures are opposites and their physical
supports are compatible; absence of a zero singleton and an opposite pair
forces arity at least three.  For overlapping halos, the quadratic term in
(8.9) prevents baseline-signature additivity, so the combined move must be
evaluated directly by (8.3)--(8.9).

This is the proof-level replacement for tuning the two-run annealer.

### 8.3 Exact specialization to one active endpoint swap

Extend the helical rows to integer indices, so that

\[
 T_{J+N}=\rho T_J.
 \tag{8.10}
\]

An active start or end swap of distance `delta` acts on one lifted
consecutive interval `I` in `Z` of size `delta<N`.  There are two fixed
coordinate labels `x,y` in this lifted frame such that, with
`theta=(x y)`,

\[
 T'_J=\theta T_J\quad(J\in I).
 \tag{8.11}
\]

Residue classes outside the image of `I` modulo `N` are unchanged.  Formula
(8.11) must not be read as a fixed transposition on all canonical
representatives.  If `J=j+qN` with `0<=j<N`, then equivariance gives

\[
 T'_j=\rho^{-q}\theta\rho^q T_j.
 \tag{8.12}
\]

Likewise, on the translated lift `I+qN` the acting transposition is
`rho^q theta rho^(-q)`.  This conjugation is essential when `I` crosses the
chosen helical cut.

Indeed, in each affected lifted residue the move removes the bit belonging
to one endpoint lift and inserts the bit belonging to the other; the two
lift differences are constant multiples of `N` along the whole interval.
For every internal lifted edge `J,J+1` in `I`, both endpoints are acted on by
the same transposition and hence

\[
 X'_J=\theta X_J.
 \tag{8.13}
\]

Only the two lifted boundary intersections of the halo `I union (I-1)` are
mixed.  Passing from `J=j+qN` to the canonical row `j` rotates both the old
and new lifted sets by `rho^(-q)`, so it preserves their respective necklace
colors.  Hence a single active swap at a perfect seed remains in the joint
fiber if and only if the middle-orbit multiset on the lifted interval `I`
and the q1-orbit multiset on its lifted halo `I union (I-1)` are each
recycled exactly.  This is the specialized form of (8.3)--(8.4) used in the
exact `k=15` one-neighbor census below.

## 9. Tiny exact calibrations

The lightweight scripts enumerate only `k=3,5,7`.

| `k` | `(r,W,N,d)` | indexed legal words | middle+q1 perfect | indexed active-swap components |
|---:|---:|---:|---:|---:|
| 3 | `(2,3,1,1)` | 3 | 3 | `3 x 1` |
| 5 | `(3,10,2,2)` | 5 | 0 | `5 x 1` |
| 7 | `(4,35,5,2)` | 6,797 | 70 | `7 x 971` |

At `k=7`, direct indexed enumeration gives seven active-swap components of
size 971.  Separately, quotienting physical rotation gives 195 legal run/gap
states, and the quotient active-swap graph is connected on those 195 states.
Thus, in this tiny computation, the indexed components agree with the seven
barycentre/phase sectors.  This identification is a result of the direct
indexed census, not a consequence of quotient connectivity alone, and it
does not prove quotient connectivity at general `k`.

The 70 perfect `k=7` words form two physical-rotation orbits.  Among all
2,415 pairs, the actual changed-column support histogram is

\[
 3^{35},\qquad4^{105},\qquad5^{2275}.
\]

There is no support-one or support-two pair and no perfect-to-perfect single
active-swap edge.  A minimum witness is

```text
c  =11111110011110001110000111011100000
c' =11011100001110001111001111111000001
```

with changed literal quotient columns `{1,2,4}`.  It transposes two middle
orbit colors and changes all five q1 positions as a three-cycle plus a
two-cycle.  Its anchored data are

\[
 (\eta;\ell;g)
 =(0;(7,4,3,3,3);(2,3,4,1,5))
\]

and

\[
 (2;(3,4,7,3,3);(3,2,5,1,4)).
\]

This is an exact finite example of the coupled trade architecture, not a
general support lower bound.

By Theorem 4.1, all 6,805 indexed legal `k=3,5,7` states satisfy the
erosion-rank, boundary-transversal, Johnson, and derivative identities through
their full depth `d`.  The frozen tiny scripts reproduce the state/deck/move
counts above; they do not separately re-evaluate the analytic erosion proof.

## 10. Exact `k=15` one-swap closure and the 4.499-billion portfolio

The retained summary

```text
scratch/k15_runtrans_swap_portfolio_20260729.audit.json
SHA-256 7af9cd35f7ba26888c0eb705cc0c1e88ae40da8f3f597fa417289340e948c8d6
```

reports 4,499,000,000 attempted proposals over twelve H100 runs with no
energy below 661.  Its arithmetic and frozen source hash are internally
consistent.  By itself it is evidence of severe stagnation, not an exhaustive
local-minimum certificate: the summary contains no legal-neighbor census or
minimum-delta histogram.

A subsequent deterministic, solver-free census now closes that precise
one-step question.  On the pinned seed of SHA-256

```text
3eac66853812e5dfc9189b7e9ac3ae1eaabb2acdf83fe660d2f74348a4d14265
```

it enumerates all 1,805 distinct legal active proposals: 907 end swaps and
898 start swaps.  The seed has

\[
 (\operatorname{miss}_{M},\operatorname{miss}_{q1},
   \operatorname{miss}_{q2},\operatorname{miss}_{U})=(0,0,47,95),
 \qquad E=661.
\]

Every neighbor has a middle-orbit hole.  Exactly two retain the q1 deck, but
each has one middle hole.  Thus there are zero joint-fiber neighbors.  There
are also zero equal-energy or improving neighbors; the unique best score is

\[
 (1,1,46,93),\qquad E=671,
\]

from `startSwap(recipient=165,donor=76,delta=1)`.  Therefore this pinned seed
is an exact strict one-step local minimum for the frozen active neighborhood
and objective.  By Section 8.3, every one of its 1,805 single-swap middle
recycling equations fails; two nevertheless pass the q1 recycling equation.

The proof artifacts are

```text
scratch/audit_k15_runtrans_single_swap_neighbors_20260729.py
708b1258eb18497a283ad1ce072697a44e59d283589181a943183d7a90702ecb

scratch/k15_runtrans_single_swap_neighbors_20260729.audit.json
5b4f5e8f6848087dc743106e73a88763ba0fd368b0956348af330d7cd4ec79ee
```

The exact census takes about 2.7 seconds locally.  By itself it proves
nothing about two or more swaps, the full legal displacement graph, the
existence of a wider simultaneous trade, or compiler/Hall.  Those moves must
be tested by (5.2)--(5.5) and (8.3)--(8.9), not by the annealer's scalar
energy alone.

### 10.1 Complete coupled support-three closure

A subsequent H100-CPU audit enumerates the complete same-run-order boundary
atlas with

\[
 |\{i:(u_i,v_i)\ne(0,0)\}|\le3.
\]

The authoritative fixture-oriented gauge has 46,928 structurally legal
nonzero states: 1,045 coupled two-run rectangles, 8,115 one-sided three-run
cycles, 35,963 coupled three-run overlays, and the 1,805 one-sided
transpositions above.  Every one fails the middle-necklace permutation;
exactly two one-sided transpositions retain q1, and no state is joint-perfect.
Therefore the pinned seed's same-order perfect-face boundary girth is at
least four.  This is seed-specific: an exact `k=7` joint-perfect rectangle
exists.

The companion theorem
`MATH_THEOREM_COUPLED_RUN_SUPPORT_THREE_TWO_DECK_GIRTH_20260729.md` proves
completeness using endpoint-residue permutations and the fixture's
sub-`N` component collars.  It also incorporates the exact event-stream
translation

\[
 \ell'_i=\ell_i+v_i-u_i,
 \qquad
 g'_i=g_i+u_{i+1}-v_i,
\]

and the coefficient-exact short-zero potential.  The verified MMM shear is
a larger-support two-deck-kernel move with `Delta Z_7=-12` quotient units and
upper holes `95 -> 94`, but its mandatory terminal rank-five protected-port
zeros worsen `165 -> 180`.  Full compiler Hall is not invoked because both
states retain 47 lower-q2 holes.

## 11. Compiler/Hall boundary

Theorem 4.1 materially strengthens the structural compiler input:
`P^(d)` is automatically a rank-`r-d` equivariant Johnson walk, and the whole
lower tower is reconstructed by repeated derivative.  Any legal move from
Section 5 preserves these rank and adjacency identities.

Nothing here proves that the rows are orbit-bijective, cover the needed q2 or
deeper targets, preserve arbitrary-width upper coverage, or keep one-core
ports and physical Hall.  Even a simultaneous middle/q1 trade can change the
depth-`d` occurrence labels and endpoint-conditioned pins.  The compiler
target must therefore be scored only after the structural and two-deck gates:

\[
 \text{legal run circulation}
 \longrightarrow
 \text{middle/q1 two-deck kernel}
 \longrightarrow
 \text{deeper shadows and exact upper oracle}
 \longrightarrow
 \text{one-core/physical Hall and cut audit}.
\]

At the audited `k=15` seed, legal rectangles and all coupled arity-three
run-boundary circulations are now closed by Section 10.1.  The next
constructive object is a support-at-least-four zero-signature circulation, or
a composition of extensive MMM/gluing shears that improves the event
potential without damaging the protected compiler gate.  Generic run-state
mixing is not the target.

## 12. Frozen artifacts

```text
scratch/anneal3_sha83d5_audit.cpp
83d5c1b79f07bbf3927aa8a22f21b61533edcd0481b7bb8af24d2adffb40cf20

scratch/anneal3_sha83d5_move_audit_20260729.md
15040cceedd2f9a09461de1e1a81e42c494745128ca4999685479e0778564631

scratch/audit_run_gap_markov_tiny.py
a12eb2364bde8106462e78a110c7a1c7dc095bcdf435966bc1b84ad86c450307

scratch/audit_k7_perfect_run_trades.py
67a0fcf12e4322c7ae8f2e882cd1b8576a31448719611a11092a12db07b119a3

scratch/k15_runtrans_swap_portfolio_20260729.audit.json
7af9cd35f7ba26888c0eb705cc0c1e88ae40da8f3f597fa417289340e948c8d6

scratch/audit_k15_runtrans_single_swap_neighbors_20260729.py
708b1258eb18497a283ad1ce072697a44e59d283589181a943183d7a90702ecb

scratch/k15_runtrans_single_swap_neighbors_20260729.audit.json
5b4f5e8f6848087dc743106e73a88763ba0fd368b0956348af330d7cd4ec79ee

scratch/k15_runtrans_seed_3eac_20260729.cw
7dd31950ffd69eea819d5ea413feb66f1d32bc1d88fe206a2b11faf26c1fd332

scratch/audit_k15_coupled_run_support3_atlas_20260729.cpp
d4ed720fc3171e336c0de2b63df1d3260362dbc44ad94773b0ea9a60ae08bc78

scratch/k15_coupled_run_support3_atlas_20260729.tsv
c19b9085487bc22d49623d89a651d040b4e198828b70d7a68dba6694a683a9cc

scratch/k15_coupled_run_support3_atlas_20260729.summary.txt
e5b89413798880c4ab365a3b3c7d0126e57fc710f554eb0b3cc26653c06e2ed7
```

The retained seed is token-identical to the pinned `/private/tmp` seed; its
byte hash differs only because the retained copy has a final newline.  The
scripts are theorem aids for the displayed tiny calibrations and exact
boundary atlases.  The complete support-three census ran only on H100 CPU;
no local heavy search or SAT computation was run for this report.
