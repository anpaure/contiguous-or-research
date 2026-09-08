# Audit of the buffered Pascal private-anchor gate

Date: 2026-07-31  
Lane: R, independent theorem audit  
Status: all displayed finite counts and min--max statements below were
rederived from the literal set formulas.  The verdict is a scoped positive
Hall theorem and a scoped negative load theorem, not an all-parameter
contiguous-OR upper bound.

## 1. Sources audited

The audit uses:

* `MATH_THEOREM_BUFFERED_HEXAGON_LLL_REDUCTION_AND_MISSING_LOAD_GATE_20260731.md`;
* `MATH_THEOREM_H2_CATALAN_CORRELATED_C6_PLANTING_AND_REROUTER_CUT_20260731.md`;
* `MATH_THEOREM_CATALAN_SUSPENDED_TRANSPARENT_HEX_ABSORBER_AND_BLOCKERS_20260731.md`;
* `MATH_THEORY_K_ALL_BALANCED_TWO_EXTENSION_HEXAGON_AND_O1_REDUCTION_20260731.md`;
* `MATH_THEOREM_PASCAL_ATTACHMENT_HALL_AND_PRIVATE_ANCHOR_LOAD_OBSTRUCTION_20260731.md`;
* `MATH_THEOREM_R_PASCAL_CHILD_TASK_SOURCE_ANCHOR_HALL_RADO_GATE_20260731.md`; and
* `MATH_THEOREM_R_BUFFERED_C6_WEIGHTED_ANCHOR_AND_TOKEN_LOAD_20260731.md`.

## 2. Valid statements

### 2.1 Haxell is the correct final selector

For task packet lists forming the parts of a graph of maximum external
conflict degree `Delta`, part size at least `2 Delta` is sufficient for an
independent transversal.  Same-list packet intersections are irrelevant.
Accordingly every resource load used to bound `Delta` must be a
**cross-list** load.

### 2.2 The literal Pascal component-attachment graph has load one

Let `V=[2m-1]`.  A component with `X` endpoint `X_R`,
`R in binom(V,m)`, is adjacent to the source

\[
             s_P^x:P+x\subset P+x+y
\]

exactly when `P subset R`.  Every task has `m` neighbours and every source
has degree at most `m` on any distinct endpoint family.  Hence, for every
task set `J`,

\[
                  m|J|\le m|N(J)|.
\]

Hall therefore supplies distinct `P`'s and distinct source incidences for
all `C` components.  The two-shore owner-capacity version is exactly the
Rado cut for the partition matroid on the pairs `{s_P^x,s_P^y}`.

### 2.3 The suspended target catalogue factors linearly by source

For

\[
 A=(D,V=D+p+q),\qquad |D|=n,quad |\Omega|=2n,
\]

the canonical packet parameters `(b,a,c)` factor through the source

\[
  \sigma(A;b,a):D-b+a\subset V-b,qquad
  b\in D,quad a\in\{p,q\}.
\]

There are `2n` distinct sources and exactly `n-2` exterior choices over
each source.  Thus the formal `2n(n-2)` supply is not a quadratic list after
one private source has been fixed.

For a target bank with distinct upper resources, a fixed source belongs to
at most `n-1` target neighbourhoods: its upper endpoint `H` forces
`V=H+b`, and there are `n-1` choices of `b outside H`.  Double counting
therefore proves the guarded congestion bound in the source theorem.  This
is an incidence-routing theorem, not yet the strict private-token theorem.

### 2.4 The exact incidence-C6 token ledger is correct

At a fixed source `C subset C+a`, the six vertex roles have multiplicities

\[
                       m^2,m,1,1,1,m,
\]

and the six incidence roles have the same free-coordinate pattern.  Hence a
restricted anchor family has exact token load

\[
                 \Lambda(r)=m^2N_0(r)+mN_1(r)+N_2(r).
\]

Double counting over the full atlas gives `6m^2` labelled candidates per
incidence token and `3(m+1)m^2` per vertex on either shore.  The independent
small-parameter audit script returns

```text
PASS_EXACT_LOAD_CORRECTION_AND_COUNTEREXAMPLE
```

with payload SHA-256
`2add582c29141154c41905dcb62bccc2cbc43e1da6f7d502c5d05d59b794e2ae`.

### 2.5 The concentrated-endpoint obstruction is exact

For chosen attachment facets `P_i subset R_i`, the suspended packet slot
`P_i+x+c` occurs in `2m` options for fixed `c`.  Hence the external load at
`X_R=R+x` contains

\[
  2m\,\#\{i:P_i\subset R,\ R_i\ne R\}.
\]

If the endpoint family is all `m`-sets of one `(m+s)`-set `W`, every chosen
facet lies in exactly `s` other endpoints.  Double counting gives average
external codegree `s`, so some slot has load at least `2ms`.  Taking

\[
 t=\left\lceil\log_2{m+1\over2}\right\rceil,
 \qquad s=m-1-t
\]

keeps the task family below the Catalan attachment count because its
relative size is at most `2^{-t}<=2/(m+1)`, while the forced load is
`Omega(m^2)`.  This refutes derivation of `O(m)` load from the scalar
component ledger and distinct endpoints alone.  It does not assert that
this endpoint family is forced by PBBS, and pruning may avoid the displayed
slot.

## 3. Required corrections and unsupported implications

1. Before the Section 4 attachments in the balanced-two-extension note,
   all `W_0` vertices of the `A` sector are unused.  Only after attaching
   `C` of them does the unused count become `U_0=W_0-C`.
2. Literal total token load cannot be `O(m)` for a quadratic list: its
   source-fixed tokens already occur in all `Theta(m^2)` alternatives.
   The selector needs source-fixed privacy and `O(m)` **external** load.
3. Two tasks cannot share one cap-one source while retaining quadratic
   lists.  Therefore the relevant source assignment is injective, unless
   physically distinct clones or an exact contraction of the common token
   are supplied.
4. Pairwise endpoint-disjoint anchors do not imply low auxiliary load.  The
   exact owner-star example has external load `m(m-1)`.
5. Passing separate physical, colour, owner, and cap Rado cuts need not give
   a common assignment.  The simultaneous upper/lower codegree constraints
   are nonlaminar and already contain graph matching at `m=3`.
6. A complete alternating cap ticket is not controlled by local C6
   geometry.  A common cap cut vertex gives gammoid rank one for two tasks,
   even when their local packet supports are private.

## 4. Bounded-task salvage and its exact boundary

If a guarded regenerative theorem independently proves at most `H=O(1)`
reachable tasks, then injective source-fixed privacy and per-list noncore
multiplicity at most `kappa m` give external local physical/colour load at
most `(H-1)kappa m`.  With `O(d)` local support this is `O(md)`, the scale
needed before applying Haxell.

This does not close complete cap paths or replacement-witness tickets: a
token used by every packet in two lists still has quadratic external load.
It also cannot presently be invoked recursively.  The estimate

\[
                         |U|\le4\Phi+b_0
\]

is a hypothesis in the buffered theorem.  Existing Pascal identities prove
the coefficient four only for passive two-coordinate descendants of a
declared upper hole.  They do not prove an absolute fresh-task bound for
the one-unit residence tax, exposed cut/seam casualties, or the
common-cap/compiler reset.  Hence absolute `b_0` remains a distinct theorem
gate.

## 5. Final audited boundary

The component-attachment Hall problem is solved.  The private-anchor step
needed by the buffered Haxell route is not solved: the current results do
not simultaneously provide a quadratic packet list, private fixed source
tokens, `O(m)` auxiliary-token load, and private complete cap/witness
tickets.  The weakest live alternatives are:

1. prove a dispersed representative theorem for the full Pascal endpoint
   family together with complete-ticket locality; or
2. prove the absolute guarded exposure bound, then use the bounded-task
   private-source theorem and separately route the finitely many cap and
   witness tickets.

Neither conclusion implies `nu(k)<=B(k)+O(1)` until boundary-equivalent
packet composition and bounded terminal completion are also supplied.

## 6. Compound-seam and dispersed-leave update

### 6.1 Exact scope of the AD seam grouping

For two fixed cyclic chronologies with \(s>0\) changed seams and
\(1\le\ell<N\), the AD identity

\[
                         b_\ell\le\ell s
\]

does prove a disjoint partition of the signed changed-window ledger.
Pairing the \(s\) old and \(s\) new bins is only bookkeeping.  It becomes
one selectable compound task per seam only if the lift authenticates an
old/new seam-event pairing and a nonempty whole two-collar packet menu.
Otherwise the proof-safe count is \(2s\) one-sided groups.  The \(4D\)
bound concerns owner positions in the two window collars, not nonlocal cap,
witness, topology or augmenting-path tickets.

The reachable induction therefore needs the joint literal ledger

\[
 |{\cal T}|\le\lambda\Phi+r_0+q s,\qquad
 s\le a\Phi+s_0,
\]

with \(q=1\) only for owned paired packets and \(q=2\) otherwise.  Existing
Pascal results do not prove this fully guarded statement.  In particular,
the coefficient four is only passive two-coordinate upper-hole inheritance;
fresh residence and common-cap reset mass remain unbounded.  A local
coherent ECO toggle has bounded \(s=6\), but no theorem bounds the number of
required ECO atoms by \(\Phi\) while exporting all guards.

### 6.2 Large leaves can work under a global code

The strong-colour theorem in

`MATH_THEOREM_R_DISPERSED_LARGE_LEAVE_STRONG_COLOUR_HALL_AND_CAP_ENERGY_GATE_20260731.md`

is a genuine way around the assumption \(|{\cal T}|=O(1)\).  Coordinate-sum
colouring modulo a prime \(q>2m-1\) makes every fixed \(h\)-colour anchor
bank satisfy

\[
 d_+,d_-\le h,\qquad d_J\le h(m-1).
\]

If the task graph restricted to that bank passes Hall, matching plus at
most \(h(m-1)\) source-collision deletions per quadratic list gives source
privacy, \(N_1\le h\), and \(N_2\le h(m-1)\).  Complete packets with
\(O(d)\) tokens then have \(\Delta=O(md)\), provided complete cap/witness
tokens obey the same code and topology is precompiled.  Haxell is therefore
independent of the task count.

### 6.3 Cardinality alone is refuted at exactly the DP scale

Let \(t=\lceil\log_2((m+1)/2)\rceil\), choose
\(|W|=2m-1-t=m+s\), and take all \(m\)-subsets of \(W\) as tasks.
Put \(W_m=\binom{2m-1}{m}\).  This family has size
\(\Theta(W_m/m)\), and ordinary task--facet Hall holds.
Nevertheless every injective facet assignment satisfies

\[
 \sum_{R'}d_{\rm ext}(R')=s|{\cal T}|,
 \qquad\max d_{\rm ext}\ge s=m-O(\log m).
\]

Thus one raw one-free token has external load at least \(ms=\Omega(m^2)\).
The DP leave-size row by itself cannot imply the weighted code.

### 6.4 The sparse raw reservoir is positive but target-free

The exact-energy Bernoulli extraction is compatible with this
counterexample.  On the full \((2m+1)\)-coordinate incidence atlas put
\(\widetilde W_m=\binom{2m+1}{m}\).  It chooses its own endpoint-disjoint
anchors and gives

\[
 |A|\ge {\widetilde W_m\over32m},\qquad
 \overline\Delta_A\le16m.
\]

Per-list pruning and Haxell give one compatible raw C6 per anchor for
\(m\ge128\).  This proves Catalan-scale raw local supply.  It does not map
prescribed repair tasks into the reservoir.

The tunable-density audit is stronger.  From exact raw row energy
\(R_m<44m^3\), density \(p=1/(1408m)\) gives at least
\(3\widetilde W_m/5632\) compatible raw packets.  For complete-list size
\(\alpha m^2\) and full-ticket energy \(KD_m m^3\), density
\(\alpha/(64KD_m m)\) conditionally gives
\(\Omega(\widetilde W_m/D_m)\) packets.  Hence even \(D_m=\Theta(m)\)
would retain Catalan-scale supply; the energy and prescribed-task rows,
not the raw span, are the unproved gates.

For complete packets the same extraction is valid only after replacing the
raw energy by the full conflict row

\[
 \sum_{f\ne e}{1\over L}
 |\{(p,q)\in{\cal Q}_e\times{\cal Q}_f:p\sim q\}|
 \le K D_m m^3,
\]

and fixing a topology/private-cap composition skeleton.  A cap-one cut
vertex shared by all choices in two prescribed lists already gives gammoid
rank one and makes that task pair infeasible.  For the average-energy route,
the decisive obstruction is a token shared by \(\omega(D_m m)\) quadratic
menus; then its row exceeds \(O(D_m m^3)\).

### 6.5 Fixed unused cells remove the cap-path load

Fix one trace-guarded compiler matching \(M_0\), already containing every
final old and newborn target, and let \(B\) be its unused cells.  If the
packet deletion lists satisfy

\[
 \left|\bigcup_{i\in J}(D_i\cap B)\right|\ge|J|
 \qquad(J\subseteq{\cal T}),
\]

Hall chooses distinct \(b_i\in D_i\cap B\).  On the globally Cartesian
frozen face--packet choices only delete their assigned \(b_i\), change no
target neighbourhood or trace guard, and never touch another assigned
cell--the same \(M_0\) survives.  Each list then carries one private
unused-cell label with external load zero; there are no cap paths or sink
tickets.

For the raw strong-colour lists, source pruning leaves at least
\(m^2-h(m-1)\) choices.  An exact cross-role check gives nine nonsource
tokens, each of external load at most \(hm\), so

\[
 \Delta_{\rm raw}\le9hm.
\]

Haxell works under \(m^2-h(m-1)\ge18hm\), in particular for
\(m\ge19h\).  A bounded task bank instead has the sufficient greedy row
\(L_m>(H-1)\beta_{\rm loc}md\), now with no compiler term.

Separate anchor Hall and unused-cell Hall do not imply a joint assignment
when cell choices depend on anchors.  The two-task option rows

\[
 \{(a_1,b_1),(a_2,b_2)\},\qquad
 \{(a_1,b_2),(a_2,b_1)\}
\]

have complete Hall projections but every pair repeats an anchor or a cell.
Thus the exact remaining interface is either Cartesian factorization or a
joint task--anchor--unused-cell hypergraph theorem.

The sharp current alternatives are therefore:

1. prove colour-selective Hall plus Cartesian fixed-unused Hall and
   protected witness/topology codes for the actual DP leave; or
2. prove a task-covering full-energy sparse extraction after the compiler
   energy has been removed by the same frozen unused-bank interface.

Both are strictly stronger than a leave cardinality estimate.
