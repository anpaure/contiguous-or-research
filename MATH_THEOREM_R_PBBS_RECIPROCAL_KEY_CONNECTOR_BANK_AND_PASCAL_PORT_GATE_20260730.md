# PBBS reciprocal-key connector banks and the Pascal port gate

Date: 2026-07-30  
Lane: R, pure mathematics  
Status: unconditional endpoint reduction for protected wedge rays; exact
`b=2` reciprocal-key theorem; exact `b=3` keyed-ear theorem inside the
canonical extreme-ray reuse architecture; conditional PBBS connector-bank
corollary; exact Pascal trace transducers and a scoped canonical-ribbon
obstruction.  No unconditional PBBS port-bank existence theorem and no
lower compiler are claimed.

## 0. Result and scope

Items 2028--2029 left the upper opening problem at the full suffix--prefix
trace conditions `(E1-port_2)` and `(E1-port_3)`.  For the protected
wedge-flank casualties those conditions have a much smaller sufficient
subclass.

Every possible fixed-width casualty at a chosen wedge flank is an extreme
geodesic ray

\[
                 w,u_1,u_2,\ldots,u_q.              \tag{0.1}
\]

The singleton

\[
                 \{\kappa\}=w\setminus u_1          \tag{0.2}
\]

never reappears on that ray.  Replacing the deleted endpoint `w` by a new
Johnson neighbour `v` of `u_1` preserves **every** eligible ray target if
and only if

\[
                         \kappa\in v.                \tag{0.3}
\]

Thus:

* two nonempty component chains are repaired by canonical endpoint
  replacement at one seam precisely when their two keys are exchanged
  across that seam;
* three components are repaired, in this extreme-ray subclass, by two
  keyed seams of which one is reciprocal.

This is a genuine positive connector theorem.  It is not equivalent to the
whole trace grid: a nonextreme suffix--prefix interval can sometimes repair
a target even when (0.3) fails.  The key condition is the weakest
depth-uniform condition depending only on the replacement endpoint in the
canonical operation which reuses the old extreme ray and replaces its one
cut-side vertex.

Protected fixed-width PBBS geometry proves (0.1)--(0.3), but it does not
prove that suitable endpoints from different components are adjacent or
exchange keys.  That remaining statement is isolated below as the
reciprocal-key PBBS port-bank lemma.

## 1. Signed protected wedge ports

Let `C` be a simple cycle in `J(k,r)`.  Let `w-u_1` be one flank of a wedge,
and orient that flank away from the wedge centre so that the corresponding
outward ray is

\[
       I_q=(u_0,u_1,\ldots,u_q),\qquad u_0=w.         \tag{1.1}
\]

For the left flank this may use the reverse orientation of the original
directed cycle.  Union labels do not depend on that reversal.  Put

\[
       U_q=\bigcup_{i=1}^{q}u_i,qquad
       Y_q=\bigcup_{i=0}^{q}u_i,qquad
       \{\kappa\}=w\setminus u_1.                    \tag{1.2}
\]

Because `w,u_1` are distinct Johnson neighbours, `kappa` is a singleton.
After cutting `w-u_1`, the retained component has endpoints `w,u_1`.  We
call `u_1` the **service endpoint**, `w` its deleted mate, and `kappa` its
**departure key**.  The signed data

\[
                         p=(w,u_1,\kappa)             \tag{1.3}
\]

are a protected wedge port.  A final path may reverse the retained
fragment; this changes which end of the displayed interval is read first,
but not its union.

By the outward-ray theorem, under fixed-width support every rank-`(r+q)`
target `Y` for which this flank lies in the component kernel `K_C(Y)` is
exactly `Y_q` for the applicable orientation.  In particular, every actual
old-lost target assigned to this supporting component is on the ray list
(1.2), because losing all component witnesses puts the selected cut edge
in that kernel.  The list may contain depths which are not actual
casualties; repairing all eligible depths is only stronger.

Call the port **active** when at least one old-lost target is assigned to
its ray list.  An inactive port imposes no service condition.

All nonreturn assertions in this report are restricted to the maximal
geodesic ray horizon under discussion.  The cycle eventually returns to
`w`, so no claim is made that `kappa` is absent from the rest of the cycle.

## 2. The departure-key lemma

### Theorem 2.1 (geodesic key nonreturn)

Suppose

\[
                         |Y_q|=r+q.                  \tag{2.1}
\]

Then every transition in (1.1) inserts a coordinate not present in any
earlier vertex of the interval.  In particular,

\[
             \kappa\notin U_q,qquad
             Y_q=U_q\mathbin{\dot\cup}\{\kappa\}.  \tag{2.2}
\]

#### Proof

The first vertex has rank `r`.  Each of the `q` Johnson transitions can
increase the running union rank by at most one.  Equality (2.1) says that
the total increase is exactly `q`; hence every transition increases it by
one.  The coordinate `kappa` belongs to the first vertex `w` and is absent
from `u_1`.  If it first reappeared in some later `u_i`, that transition
would insert a coordinate already present in the running union and would
fail to increase its rank, a contradiction.

All elements of `w` other than `kappa` lie in `u_1`, because `w` and `u_1`
are Johnson neighbours.  Thus `w` contributes to `Y_q` exactly the one
coordinate `kappa` beyond `U_q`, proving (2.2).  QED.

### Theorem 2.2 (exact endpoint replacement)

Let `v` be any rank-`r` set.  The replacement interval

\[
                         v,u_1,\ldots,u_q             \tag{2.3}
\]

has union `Y_q` if and only if

\[
                         \kappa\in v\subseteq Y_q.   \tag{2.4}
\]

If `v` is Johnson-adjacent to `u_1`, this is equivalent simply to

\[
                         \boxed{\kappa\in v}.        \tag{2.5}
\]

The same one endpoint therefore repairs every geodesic depth in the ray
list simultaneously.

#### Proof

By Theorem 2.1, the old target is `U_q dot-union {kappa}`.  The new union is
`U_q union v`; equality holds exactly when `v` adds the missing key and
adds nothing outside `Y_q`, which is (2.4).

Now assume `v` is a Johnson neighbour of `u_1`.  Since `kappa` is absent
from `u_1`, condition `kappa in v` forces it to be the unique coordinate of
`v setminus u_1`.  Hence

\[
                  v=u_1-\{a\}+\{\kappa\}
                    \subseteq u_1\cup\{\kappa\}
                    \subseteq Y_q,                  \tag{2.6}
\]

so the subset condition is automatic.  Conversely (2.4) includes the key
condition.  Neither (2.5) nor its proof depends on `q`, proving the final
assertion.  QED.

### Remark 2.3 (why this is stronger than insertion-order control)

The general theorem of item 2029 compares two complete first-insertion
traces and their first forbidden coordinates.  The present theorem uses
the protected-ray fact that the old witness crosses the cut at an extreme
edge.  It keeps all `q` states on the retained side and changes only `w`.
The entire chain consequently collapses to the one-bit condition (2.5).
This collapse is unavailable for an arbitrary cut-crossing target or an
arbitrary nonextreme seam host.

## 3. Two components: reciprocal key exchange

Take protected ports

\[
        p_i=(w_i,u_i,\kappa_i),\qquad i=1,2,         \tag{3.1}
\]

on two distinct components.  Orient the retained fragments so that the
new seam is `u_1-u_2`: near the seam, the first fragment is read toward
`u_1` and the second away from `u_2`.  Thus the ray of component 1 appears
in reverse order ending `...u_1,u_2`, while that of component 2 appears as
`u_1,u_2,...`.  Both are literal intervals of the same final path.

### Theorem 3.1 (`PRK_2`, reciprocal-key connector)

Assume `u_1-u_2` is a strict Johnson seam and that the two assigned ray
lists exhaust the actual old-lost targets.  The seam canonically rehosts
every assigned ray casualty if and only if

\[
 \begin{aligned}
  p_1\text{ active}&\Longrightarrow\kappa_1\in u_2,\\
  p_2\text{ active}&\Longrightarrow\kappa_2\in u_1.
 \end{aligned}                                      \tag{3.2}
\]

If both ports are active, (3.2) is equivalent to the reciprocal-key
identity

\[
                    \boxed{
                    u_2=u_1-\{\kappa_2\}+\{\kappa_1\}.}          \tag{3.3}
\]

If the two openings and the new seam also pass the exact residence and
erosion tests, then this one connector repairs every active assigned
protected-ray casualty chain.  Under the fixed-width/outward-ray
classification it implies `(E1-port_2)` and gives zero protected upper
spill.

#### Proof

For the first active component the partner endpoint replacing `w_1` is
`u_2`; Theorem 2.2 gives the first implication in (3.2).  For the second
active component the replacement of `w_2` is `u_1`, giving the second.

When both are active, `kappa_1` is absent from `u_1` and `kappa_2` is absent
from `u_2`.  Conditions (3.2) and Johnson adjacency force

\[
       u_2\setminus u_1=\{\kappa_1\},\qquad
       u_1\setminus u_2=\{\kappa_2\},               \tag{3.4}
\]

which is (3.3).  The converse is immediate.  Literal fixed-width intervals
are supplied by Theorem 2.2.  The protected outward-ray theorem says that
every old-lost target assigned to either cut is on the corresponding ray
list, so all such targets are restored.  Residence, erosion and the lower
compiler are independent clauses and are not inferred from (3.2).  QED.

### Definition 3.2 (PBBS reciprocal-key bank)

For a protected PBBS factor, let its signed port bank contain every chosen
wedge-flank state together with its service endpoint, key, component,
orientation and exact residence collar.  Its reciprocal graph joins ports
on distinct components when (3.3) is a legal residence-safe seam.

The PBBS-specific hypothesis `KPB_2` is that the bank has a legal seam
satisfying the active implications (3.2); it is a reciprocal-graph edge
when both chains are active and a one-way keyed edge when exactly one is.
Theorem 3.1 proves

\[
                         KPB_2\Longrightarrow E1\text{-port}_2. \tag{3.5}
\]

This is the weakest endpoint-only hypothesis for the canonical
extreme-ray replacement: (2.5) is necessary as well as sufficient for
each side.  It is a stronger sufficient condition than unrestricted
`E1-port_2`, which may use a nonextreme cell of the full seam grid.

### Remark 3.3 (the key test is not necessary for the full grid)

The distinction persists in the genuine odd-middle graph `J(9,5)`, with a
wedge flank and a nested q2/q3 ray.  Take

```text
other wedge neighbour: 13789
old ray:                12789,23789,34789,45789
partner trace:                24789,14789,15789.
```

The equal wedge unions are

\[
 13789\cup12789=12789\cup23789=123789.              \tag{3.6}
\]

The port key is `1`, which is absent from the partner endpoint `24789`.
Thus canonical endpoint replacement fails.  Nevertheless the new seam
`23789-24789` is Johnson and the two noncanonical seam intervals give

\[
\begin{aligned}
 23789\cup24789\cup14789&=1234789,\\
 23789\cup24789\cup14789\cup15789&=12345789,
\end{aligned}                                       \tag{3.7}
\]

exactly the old q2 and q3 ray targets.  The q3 target is proper of rank
eight.  Thus `PRK_2` is exact only for endpoint replacement and is merely
sufficient for unrestricted `(E1-port_2)`, even for a protected-looking
nested ray trace.  This is a local trace germ, not a spanning cycle-factor
counterexample; it does not assert that the cut kills all other witnesses.

## 4. Three components: a keyed ear

Take three protected ports.  One concrete orientation has
the endpoint order

\[
          w_1\;\cdots\;u_1
          \mid
          u_2\;\cdots\;w_2
          \mid
          u_3\;\cdots\;w_3.                         \tag{4.1}
\]

The first seam can replace `w_1` and `w_2` simultaneously.  The second can
replace `w_3` by the boundary endpoint `w_2`.

### Theorem 4.1 (`PRK_3`, keyed-ear connector)

Suppose the three assigned ray lists exhaust the actual old-lost targets,
both seams are Johnson, and the active-key conditions hold:

\[
\begin{aligned}
 &u_1\sim u_2,\qquad w_2\sim u_3,                   \tag{4.2}\\
 &p_1\text{ active}\Longrightarrow\kappa_1\in u_2,\\
 &p_2\text{ active}\Longrightarrow\kappa_2\in u_1,\\
 &p_3\text{ active}\Longrightarrow\kappa_3\in w_2. \tag{4.3}
\end{aligned}
\]

Then the two seams in (4.1) repair every geodesic protected-ray target of
all three active port chains.  If all three are active, the first seam is
reciprocal and repairs ports 1 and 2, while the second is a one-way keyed
ear which repairs port 3.  The reversed pattern, in which the reciprocal
seam is incident with component 3, is equally valid.

If every chain is nonempty, then within the **canonical extreme-ray reuse
architecture** this shape is also necessary, up to reversal: each outer
component forces its one-way key condition, and the middle component must
use one of its two incident seams, making that seam reciprocal with the
outer component already serviced there.

Consequently a legal residence-safe keyed-ear path implies
`(E1-port_3)` and zero protected upper spill.

#### Proof

Apply Theorem 2.2 to each active port: port 1 has replacement endpoint
`u_2`, port 2 has replacement endpoint `u_1`, and port 3 has replacement
endpoint `w_2`.  Conditions (4.2)--(4.3) are exactly the resulting key
tests.

For the converse in the stated subclass, an outer component has only one
new seam and its canonical reused ray changes only the deleted mate.  Its
adjacent foreign endpoint must therefore contain its key by Theorem 2.2.
The service endpoint of the middle signed port lies at one of the two
seams.  If its chain is nonempty and is canonically reused, the foreign
endpoint at that seam must contain the middle key.  The outer port at the
same seam has already forced the opposite key condition, so this seam is
reciprocal.  The other seam is the one-way keyed ear.  QED.

### Definition 4.2 (PBBS keyed-ear bank)

The PBBS-specific hypothesis `KPB_3` is the existence of three signed
ports and an order satisfying (4.1)--(4.3), with both seams passing every
physical Johnson, residence and erosion test.  The theorem gives

\[
                         KPB_3\Longrightarrow E1\text{-port}_3. \tag{4.4}
\]

This is a deterministic label theorem, not the scalar inequality
`q(b-1)>=b`.  It also keeps the common physical chronology: the three
witness families are intervals of the one path (4.1), not independently
chosen rankwise rows.

## 5. What protected PBBS geometry proves

The combination of fixed-width PBBS support and the protected outward-ray
theorem proves all of the following without a new hypothesis:

1. every old-lost target assigned to a wedge-flank cut has the extreme form
   (1.1);
2. its departure key is one singleton independent of depth;
3. a legal partner endpoint containing the key repairs the entire ray list;
4. for `b=2` and `b=3`, `KPB_2` and `KPB_3` are sufficient connector-bank
   conditions.

It does **not** prove cross-component key incidence.  Neither all-depth
support, cyclic residence, component fullness nor the existence of many
Johnson endpoint pairs says that another component supplies a seam endpoint
containing the prescribed key.  The exact remaining PBBS statement is:

> **UNPROVED: protected reciprocal-port existence lemma.**  The
> residence-safe PBBS
> wedge-port graph contains an active-keyed edge (reciprocal when both
> chains are active) for a two-component opening, and contains an
> active-keyed spanning path (a keyed ear when all three chains are active)
> for a three-component opening.

This is strictly smaller than asking for all suffix--prefix grids: a port
is described by two rank-`r` endpoints, one key, its component and its
residence collar.  It is nonetheless a new existence theorem and is not a
consequence of the currently audited PBBS support theorem.

## 6. Pascal transport: exact trace law

### Proposition 6.0 (the transport which is automatic)

Coordinate relabelling and adjoining one fixed common core to every state
preserve `PRK_2` and `PRK_3` exactly.  More precisely, for a permutation
`pi` and a fixed set `K` disjoint from its image, replace every state `S` by

\[
                         K\cup\pi(S).                \tag{6.0}
\]

The transformed key is `pi(kappa)`, Johnson adjacency and every key
containment are unchanged, and every ray union acquires the same common
core `K`.

#### Proof

Relabelling commutes with differences and unions.  Adding the same disjoint
core changes every rank and intersection rank by `|K|`, hence preserves
Johnson adjacency.  It adds no departure or arrival event, and
`pi(kappa) in K union pi(v)` is equivalent to `kappa in v`.  Apply Theorems
2.2, 3.1 and 4.1.  QED.

This gives a genuine suspension of a connector certificate, but does not
create new owners or prove that the suspended ports belong to a spanning
PBBS factor.  The nontrivial Pascal facet and union operators behave
differently.

The Pascal operators do not preserve first-entry data automatically.  Let

\[
                         Z_0,Z_1,\ldots              \tag{6.1}
\]

be a seam-facing endpoint trace and put

\[
               \tau_Z(x)=\min\{j:x\in Z_j\},        \tag{6.2}
\]

with value infinity if `x` never appears.  Define

\[
       (\partial Z)_j=Z_j\cap Z_{j+1},\qquad
       (\nabla Z)_j=Z_j\cup Z_{j+1}.                 \tag{6.3}
\]

### Proposition 6.1 (Pascal endpoint transducers)

For every coordinate `x`,

\[
 \tau_{\nabla Z}(x)=\max\{\tau_Z(x)-1,0\},          \tag{6.4}
\]

where infinity remains infinity, while

\[
 \tau_{\partial Z}(x)
   =\min\{j:x\in Z_j\text{ and }x\in Z_{j+1}\}.     \tag{6.5}
\]

A fixed common tag has insertion time zero, and a relabelling composes
`tau` with the inverse permutation.

#### Proof

A coordinate belongs to `Z_j union Z_(j+1)` exactly when it has appeared by
one of those two positions; its first union occurrence is therefore one
position before its first old occurrence, clipped at zero.  Membership in
an intersection is exactly simultaneous membership at the two adjacent
positions, proving (6.5).  The tag and relabelling assertions are
immediate.  QED.

The union law is a scalar shift.  The facet law is not: a coordinate in
`Z_0 setminus Z_1` is delayed until its next adjacent `11` occurrence,
possibly forever.  Thus a parent port satisfying the item-2029 quadrant
criterion need not have a child port.  A physical Pascal induction must
carry the ordered endpoint membership words, or equivalently recompute the
transformed insertion times, rather than transport only a signed shadow
ledger.

### Proposition 6.2 (small legal facet-port counterexample)

In `J(9,5)`, take the physical left and right fragments

```text
P = (12789,12389,12348,12345),
Q = (12346,12368,12689,16789).
```

The parent seam `12345-12346` is Johnson and its endpoint union is
`123456`.  Add a new coordinate `z` and replace the left trace by the
facet trace, in the physical orientation toward the seam,

```text
z+partial(P) = (z1289,z1238,z1234).
```

The child seam `z1234-12346` remains Johnson.  Nevertheless the target

\[
                         z123456                    \tag{6.6}
\]

has no child seam-grid host.  At fixed depth two the two diagonal cells
are both

\[
                         z123468.                   \tag{6.7}
\]

The desired coordinate `5` is the facet departure at the old endpoint and
never returns on either displayed trace.

#### Proof

The intersections of consecutive `P` states are `1289,1238,1234`.  Direct
set comparison gives both Johnson seams and (6.7).  No displayed child
state contains coordinate `5`.  Therefore
no larger suffix--prefix union can equal (6.6) either.  QED.

This is a local legal trace counterexample, not a spanning PBBS factor.  It
proves that Pascal facet/copy transport plus parent and child seam legality
does not imply `E1-port`.

## 7. A conditional Pascal source and its canonical obstruction

### Lemma 7.1 (abstract swapped-key siblings)

Suppose two protected ports on distinct components have compatible
openings and have service endpoints and keys

\[
 u_1=U\cup\{b\},\quad \kappa_1=a,qquad
 u_2=U\cup\{a\},\quad \kappa_2=b,                  \tag{7.1}
\]

where `a,b` are absent from `U`.  Then `u_1-u_2` is Johnson and is a
reciprocal-key seam.  If its physical residence collar passes, the two
ports satisfy the reciprocal-key clause of `KPB_2`; if their assigned ray
lists also exhaust the actual casualties, they satisfy full `KPB_2`.

#### Proof

The endpoints differ by exchanging `a,b`, and each contains the other
port's key.  Apply Theorem 3.1.  QED.

The four-sector Pascal diamond contains the abstract sibling states

\[
             X_i=\{x\}\cup T_i,qquad
             Y_i=\{y\}\cup T_i,                    \tag{7.2}
\]

which have precisely the swapped-tag endpoint form.  The missing issue is
not their algebra; it is their simultaneous selection as distinct
protected wedge ports in resident components.

### Proposition 7.2 (canonical resident-ribbon sibling obstruction)

In the standard unrelabeled four-sector Catalan-leave ribbon, the selected
edge `Y_i-X_i` occurs only for a leave gap `g=1`.  The two new coordinates
then have a positive run of length `g+1=2`.  More generally depth-`d`
residence requires every leave gap to satisfy `g>=d`.  Hence for every
`d>=2`, the resident face of the canonical ribbon contains no selected
`X_i-Y_i` sibling edge and therefore no reciprocal bank obtained directly
from the selected swapped-tag sibling edges.

#### Proof

For consecutive leaves `j<k`, the exact selected ribbon is

\[
 A_j,
 Y_{j+1},\ldots,Y_k,
 U_{k-1},\ldots,U_{j+1},
 X_{j+1},\ldots,X_k,
 A_k.                                                \tag{7.3}
\]

When `g=k-j>=2`, the nonempty `U` arm separates the `Y` and `X` arms, so no
selected sibling transition occurs.  When `g=1`, the `U` arm is empty and
the selected transition is `Y_(j+1)-X_(j+1)`.  The exact ribbon run law is
`g+1`; depth-`d` residence requires run length at least `d+1`, equivalently
`g>=d`.  Thus `g=1` is excluded for `d>=2`.  QED.

This proposition excludes only the direct canonical sibling supply.  It
does not exclude a root-dependent relabelling, a nonlocal Pascal rethread,
a protected triangle port using old-coordinate keys, or another PBBS port
bank.  Such a construction must explicitly prove selected wedge status,
cross-component key exchange and the seam no-return comparisons.

The exact positive Pascal target is therefore the **UNPROVED protected
phase-aligned port lemma**: a noncanonical braid must produce distinct resident signed
ports with swapped keys, or a keyed-ear triple, while transporting the
literal fixed-width witnesses and compiler sockets.  Current Pascal
interior identities and endpoint Hall theorems do not supply this clause.

## 8. Checks against the known carriers and counterexamples

### 8.1 `k=11,13,15`

* `k=11` has one physical component.  Its opening loses no proper upper
  target, so it does not test `KPB_2` or `KPB_3`.
* `k=13` has two components, but every proper upper target retains an
  interior witness after the chosen splice.  Its upper `E1-port_2` condition
  is vacuous.  The larger atlas contains `24960` directed candidates,
  `6032` preserving all upper targets, and `1092` also passing residence;
  this shows that legality alone is not the selection theorem.
* `k=15` has exactly two proper fragment casualties,

  \[
                  20089=\mathtt{0x4e79}
                     \subset
                  28537=\mathtt{0x6f79}.            \tag{8.1}
  \]

  The seam endpoints union to the first, and the four-state seam interval
  at indices `6387,...,6390` realizes the second as the one-sided trace cell
  `S_2 union R_0`.  Thus it is a genuine positive general `b=2` seam-grid
  calibration.  It is not evidence for canonical key replacement: the old
  q1 union at the left cut is

  \[
          19065\cup26745=27257\ne
          19065\cup18041=20089,                    \tag{8.2}
  \]

  and the frozen reports do **not** certify that either selected cut is a
  wedge flank or that `28537` is an assigned protected outward ray.  It is
  therefore not an authenticated reciprocal-key certificate.
  Of the `3960` residence-safe Johnson seams in the complete atlas, exactly
  `60` are unrestricted-upper-complete; all `1290` colour-recycling seams
  fail.  Again, an existential port theorem is necessary.

No authenticated `k=11,13,15` certificate tests a nonvacuous `b=3`
protected keyed-ear condition.  The frozen router types are `BB`, `BB`, and
`AA`; they are not one inherited Pascal sibling-port template.

### 8.2 The odd-middle `J(9,5)` systems

The path germ from item 2029 has identical insertion order `8,9,7` on its
two sides but strands desired coordinates behind forbidden insertions.  It
shows that a common insertion order is not a substitute for target-relative
coherence.  It is not itself a protected wedge-cycle port system.

For the three-cycle example of item 2029, suppress the common coordinates
`8,9`.  The three closure-flank ports are

\[
              (u,\kappa)=(124,3),(125,6),(136,4).   \tag{8.3}
\]

Only `124-125` is a Johnson pair, and neither endpoint contains the other
port's key.  Hence the fixed ports have no reciprocal edge and no keyed-ear
path.  The example's cuts fail the separate depth-two safety condition, so
this is only a sharp test of the connector algebra, not a PBBS-spanning
counterexample.

In the two-cycle `J(9,5)` system, the second component carries coordinate
`7` on every vertex while `7` is absent from the first locked target.  A
foreign endpoint from that component cannot be a valid one-way replacement;
in particular it cannot be both Johnson-adjacent to the first service
endpoint and contain the required new key without introducing the poison
coordinate.  That system has q2-safe cuts and actual q3 casualties but no
legal connector for its fixed ports.  It still does not refute a different
cut in a spanning PBBS factor.

## 9. Exact implication for the word theorem

Let `T` be the final physical owner path obtained from two or three
protected components.  Suppose:

1. fixed-width all-depth support and the protected outward-ray
   classification hold before opening;
2. `KPB_2` or `KPB_3` supplies the cuts, order, orientations and
   residence-safe physical seams;
3. all retained component-interior witnesses and all boundary conditions
   required by the owner theorem pass; and
4. the final common lower compiler `COMP_d(T)` is feasible.

Then every proper old-lost upper target is restored by a literal seam
interval, so the upper trace defect `tau_b` of item 2029 is zero.  Hence

\[
                 \nu(k)\le B(k)+\lambda_d(T),       \tag{9.1}
\]

where `lambda_d(T)` is the exact remaining common-compiler deletion number.
If the full compiler is feasible without deletions, then

\[
                         \nu(k)=B(k).                \tag{9.2}
\]

The reciprocal-key theorem has no lower-repair capacity by itself.  It does
not turn scalar deadline slack into ports, does not choose compiler pins,
and does not transport a compiler through Pascal.  Those are independent
conjuncts.

## 10. Audited boundary

The decisive mathematical step is Theorem 2.2.  Its quantifiers are
pointwise in the component, port and geodesic depth; no independence,
counting, probability or finite search is used.  The `b=2` and `b=3`
conclusions use the same literal final path for every depth.

An independent adversarial audit checked the finite geodesic horizon,
active versus empty chains, the component-kernel quantifier, both path
orientations, the canonical-only converses, the odd-middle noncanonical
countergerm, the `k=15` q1 mismatch, and the Pascal leave-gap scope.  The
theorem passed after those qualifications were incorporated.

The proved boundary is:

1. protected ray geometry reduces canonical rehosting to one key bit;
2. `PRK_2` and `PRK_3` rigorously imply `E1-port_2` and `E1-port_3`;
3. the standard resident Pascal ribbon does not contain the most direct
   selected swapped-tag sibling bank at depth at least two;
4. Pascal facet transport can destroy a legal trace host, as Proposition
   6.2 shows;
5. the smallest remaining positive theorem is cross-component existence of
   a resident reciprocal PBBS port or keyed ear, possibly created by a
   noncanonical phase-aligned Pascal braid.

No claim is made that the current PBBS factor has that bank in every rank,
that the canonical Pascal braid can be repaired locally, or that the lower
compiler follows from the endpoint keys.
