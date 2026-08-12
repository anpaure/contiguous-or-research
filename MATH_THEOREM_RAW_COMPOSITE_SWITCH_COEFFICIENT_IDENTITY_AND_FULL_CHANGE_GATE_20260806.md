# Raw composite-switch coefficient identity and the full-change gate

**Date:** 2026-08-06  
**Method:** exact covariance-orbit symmetrization and earliest-blocker
coarea; no computation or search  
**Status:** **TYPE-UNSAFE LINEAGE -- DO NOT CITE Sections 3--7.**  Section 2
records a scalar first-kill coefficient identity, but Sections 3--7 apply
the resource-layer resolvent `R` to the scalar `(K_T f)(A)`.  That operation
is undefined.  Consequently `(FSW)` is not the Bellman residual and the
claimed reduction to `(FSW)` is withdrawn.  The proof-safe replacement is
`MATH_AUDIT_RAW_COMPOSITE_SWITCH_RESOLVENT_TYPE_ERROR_AND_BILINEAR_REPAIR_20260806.md`.

## 1. Literal stopped covariance index

For one resource type `T`, the joint-Lyapunov quadratic face is

\[
 \mathcal B_{T,i}(f)
 =\sum_{A\in\mathfrak A_i}\mu_i(A)(K_Tf)(A)^2,
\tag{1.1}
\]

where a composite index is either

\[
 A=(Q,E,F)
 \quad\hbox{or}\quad
 A=(v,E,F,h),
\tag{1.2}
\]

and `mu_i(A)` is the corresponding pair- or root-future coefficient in
(5.1) of the joint-Lyapunov note.  Availability of `A` means that all of
its literal host edges and named roots are live.

A coordinate transposition acts on the whole occurrence-labelled index:

\[
 \tau A=(\tau Q,\tau E,\tau F)
 \quad\hbox{or}\quad
 (\tau v,\tau E,\tau F,h).
\tag{1.3}
\]

In particular, one must not keep `Q` fixed while transposing `E,F`.

### Lemma 1.1 (equal live composite coefficients)

If both `A` and `tau A` are live at state `i`, then

\[
 \boxed{\mu_i(\tau A)=\mu_i(A).}
\tag{1.4}
\]

If both hypothetically survive the next deterministic density update, then
their next coefficients are equal as well.

#### Proof

The base host is a complete coordinate orbit.  Coordinate transposition
preserves the base weights of `E,F`, every non-slot and slot count, the
intersection and union cardinalities relative to the transported root,
and the deterministic densities.  These are all factors in `mu_i`.
\(\square\)

This is the exact coefficient equality available before stopping.  It is
an equality for the composite coefficient; there is no additional
independent `a_C/X` factor unless a separate literal formula for the
covariance operator supplies one.

## 2. Exact first-kill coefficient

Let `G` be accepted at transition `i`, and suppose

\[
 A,\tau A\in\mathfrak A_i,qquad
 A\text{ survives }G,qquad \tau A\text{ is killed by }G.
\tag{2.1}
\]

Let `mu_i^+(A;G)` be the coefficient which `A` would have after the
deterministic update if it survived.  The future-fugacity drift identities
`(FP6)` and (2.5) of the joint-Lyapunov note give this coefficient exactly;
by Lemma 1.1,

\[
                    \mu_i^+(A;G)=\mu_i^+(\tau A;G).
\tag{2.2}
\]

The expected coefficient of this boundary birth is

\[
 \boxed{
 {a_G(i)\over X(i)}\mu_i^+(A;G).}
\tag{2.3}
\]

The counterfactual next potential would contain the `tau A` term with
coefficient `mu_i^+(tau A;G)`.  Transition (2.1) deletes it.  Therefore the
negative first-kill coefficient is exactly (2.3).  It does not merely
dominate it up to a density or time factor.

The earliest-blocker partition makes (2.3) unique: every oriented pair
`(A,tau A)` has at most one boundary birth.  Hence no occupation-time sum
and no comparison with the law of the first blocker occurs.

This proves the raw coefficient statement requested in the adaptive
Bellman note.  It does not prove the analogous statement after multiplying
transitions by an arbitrary terminal-event Doob ratio.

## 3. Polarization and the full changed set

Put

\[
 u=(K_Tf)(A),\qquad v=(K_Tf)(\tau A).
\tag{3.1}
\]

The oriented covariance boundary is proportional to
`[u^2-v^2]_+`.  With the positive-semidefinite resolvent norm, the vector
version is

\[
 [\|u\|_R^2-\|v\|_R^2]_+
 \le \|v\|_R^2+2\|u-v\|_R^2.
\tag{3.2}
\]

The first term is paid with the exact coefficient (2.3) by the killed
`tau A` term.  What remains is the switch energy

\[
                         \mathcal E_T(A,\tau;f)
       =\|K_Tf(A)-K_Tf(\tau A)\|_R^2.
\tag{3.3}
\]

Let `D_T(A,tau)` be **all** non-slot resource occurrences changed by the
coordinate transposition.  Then

\[
 K_Tf(A)-K_Tf(\tau A)
 =\sum_{(x,y)\in D_T(A,\tau)}\epsilon_{x,y}(f_x-f_y),
\tag{3.4}
\]

and every `(x,y)` is one Johnson edge.  The set in (3.4) has size `O(d)`.
It cannot be replaced by the subset of endpoints met by `G`.

## 4. What `(ROc)` and `(FE3)` already pay

Let

\[
 J_T(A,\tau;G)
 =\{(x,y)\in D_T(A,\tau):
       G\text{ contains exactly the killed-side endpoint}\}.
\tag{4.1}
\]

It is nonempty on (2.1).  The earliest-blocker map chooses a unique first
such incidence after fixing an ordering of the finitely many occurrence
roles.

Expand (3.3).  The following subterms have the established static
normalizations.

1. A diagonal term supported on the first blocker incidence is a rooted
   one-entry tuple.  The exact switch resistance removes the inverse
   Johnson gap, and `(ROc)` pays its coefficient.
2. If two changed incidences are both met by the same blocker, choosing
   their unordered pair gives exactly a summand counted by
   `binom(j(G;E,F),2)` in `(FE3.3)`.  The coefficient is (2.3), and the
   density sum is the kernel `K_(p_*)(j)`.  Thus this subface injects
   termwise into `(FE3)`.
3. The slot-only version remains in the already separate slot ledger.

These assertions use no independence between two hits; both hits determine
the same transposition and are kept in the same `(FE3)` tuple.

## 5. The exact residual inequality

Write

\[
 Z_J=\sum_{e\in J_T}z_e,qquad
 Z_U=\sum_{e\in D_T\setminus J_T}z_e.
\tag{5.1}
\]

The terms not covered by Section 4 are

\[
 \boxed{
 \mathcal U_T(A,\tau,G;f)
 =2\langle Z_J,RZ_U\rangle+\|Z_U\|_R^2.}
\tag{5.2}
\]

They involve one or two changed occurrences which the earliest blocker did
not meet.  They are not literally indexed by two members of
`G cap(E union F)`, so `(FE3.3)` does not contain them termwise as currently
stated.

The remaining raw switch theorem is exactly

\[
 \boxed{
 \begin{aligned}
 \mathbb E\sum_{i<T}{1\over {k\choose2}}
 \sum_\tau\sum_{A\in\partial_\tau^+\mathfrak A_i}
 {a_{G_i}(i)\over X(i)}\mu_i^+(A;G_i)
 [\mathcal U_T(A,\tau,G_i;f_i)]_+
 =O(M/d^4).
 \end{aligned}}
\tag{FSW}
\]

Sum over the finitely many resource types and the marked entry patterns in
`(FSW)`.  The exact coefficient and all blocker-hit terms have already
been removed.

A sufficient strengthening is a coefficient-preserving map which assigns
every unhit changed occurrence to the first blocker incidence with total
multiplicity `O(d)`, because `(FE3)` has a spare factor `1/d`.  Such a map
must use the literal FIFO/track geometry: an abstract involution does not
provide it.

## 6. Why equal coefficients alone do not prove `(FSW)`

Take a two-dimensional Hilbert space with `R=I`.  Let one switch have
changed vectors `z_0,z_1`, where the blocker sees only `z_0`, and choose

\[
                         \|z_0\|=1,qquad \|z_1\|=L.
\tag{6.1}
\]

Give the switch mates equal weights and let the unique blocker always kill
the same mate.  There is one boundary birth and the coefficient identity
(2.3) is exact.  The blocker-hit diagonal is `1` and there is no
two-blocker-hit term, while (5.2) is `Theta(L^2)`.  Letting `L` grow shows
that equal weights, one birth, `(ROc)` on the hit incidence, and `(FE3)` on
two hit incidences do not imply `(FSW)` in an abstract regular host.

The actual FIFO host has extra relations among `z_0,z_1`; those relations
may prove `(FSW)`, but they must be used explicitly.

## 7. Consequence and scope

If `(FSW)` is proved, the raw one-sided Bellman value has scale
`O(M/d^4)`.  The already proved stopped-transfer chain then yields

\[
                 \mathbb E(B_0+B_1)=O(M/d^2),
\tag{7.1}
\]

and the annealed quarantine--Haxell theorem finishes the stochastic bottom
selection without `(JCYL)`.

At present `(FSW)` is not proved.  The gain of this note is exact: the
future-fugacity/earliest-blocker **coefficient** is no longer open.  The
only remaining switch row is a literal full-change FIFO energy estimate,
not a comparison with a first-kill law.
