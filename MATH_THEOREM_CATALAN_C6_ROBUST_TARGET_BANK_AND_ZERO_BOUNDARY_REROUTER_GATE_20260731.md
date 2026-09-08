# C6 target banks: exact robust-completion interface and the zero-boundary rerouter obstruction

Date: 2026-07-31  
Status: exact conditional absorption theorem, exact sparse-cycle transport
invariant, and a literal Boolean `n=3` obstruction.  No robust all-`n`
target-bank construction is claimed.

## 0. Verdict

The suspended fixed-four `C6` and the linear resource-disjoint prepacking
theorem do not yet form a robust absorber.  The missing correlation can be
stated exactly.

After the forced unused-slot baseline is removed, a side matching `M` has a
leave in the two outer classes and the literal-slot class.  A target bank
works for `M` precisely when some matching `J` of target atoms covers that
complete typed leave and the old halves of compatible `2 -> 3` packets are
installed in `M`.
Replacing those old halves by the new halves is then exact.  Contracted
graphic independence, the root-star base row, and a literal downstream
compiler certificate are the remaining independent guards.

Sparse Boolean `ell <-> ell` cycles have a narrower role.  They have zero
boundary on both outer palettes.  They may permute lower--upper pairings and
change literal owner-slot leave by

```text
                         P(C)-Q(C),                       (0.1)
```

but they cannot change either outer leave set.  Consequently they can solve
the **pairing/slot fibre after outer Hall has been met**; they cannot steer an
arbitrary Delcourt--Postle leave into a prechosen outer target reservoir.

This distinction already has a literal Boolean obstruction.  In the
parameter-three fixed-four hex, one phase is a three-atom resource-disjoint
target matching.  Deleting one atom of the other phase leaves a legal cross
atom whose lower and upper resources are not paired by the target matching.
The induced one-by-one target graph has no edge.  Every zero-outer-boundary
rerouter preserves this failure.

Thus the correct next object is not a larger disjoint packet packing.  It is
an **overlapping, matching-indexed C6 atlas** whose target graph is robust on
the actual family of DP outer leaves, together with a sparse-cycle slot
transport system and installed old phases.  The theorem below gives the
exact interface such an atlas must satisfy.

## 1. Normalized side host and exact target completion

Fix an admissible common basis `Q`.  Delete the forced affine unused-slot
baseline, so that the active four-uniform host has typed resource classes

```text
                         D, U, S                         (1.1)
```

of orders `P,P,2P`.  A side atom uses one lower colour, one upper colour,
and two distinct literal owner slots.  On an ordered-four-transversal face
the two slots may additionally be assigned tail/head roles, but this role
split is not needed below.

For a host matching `M`, write

```text
 Lambda_R(M)=R \ res_R(M),       R in {D,U,S},            (1.2)
 Lambda(M)=disjoint union_R Lambda_R(M).                 (1.3)
```

If `|M|=P-h`, the two outer leaves have order `h` and the slot leave has
order `2h`.

### Lemma 1.1 (dummy target completion)

Let `M` be a host matching of order `P-h`, and let `J` be a matching of `h`
host atoms disjoint from `M`.  The following are equivalent.

1. `res(J)=Lambda(M)`.
2. `M union J` is a perfect matching of the normalized typed host.

In particular, saying that the leave is a disjoint union of target atoms is
already an exact four-uniform perfect-matching statement.  It is not a
consequence of the scalar equality of the typed leave sizes.

#### Proof

Every resource is used at most once by `M union J`.  The union has `P`
atoms, so it consumes `P,P,2P` resources of the three types.  It is perfect
exactly when `J` uses each resource omitted by `M`.  This is (1). `square`

Let `T` be a catalogue of legal target atoms.  Its projection to the two
outer shores is the bipartite graph

```text
 G_T subseteq D x U.                                     (1.4)
```

For fixed outer leave sets `D_0,U_0`, a necessary condition for target
completion is

```text
 |N_(G_T[D_0,U_0])(X)| >= |X|       for every X subseteq D_0.  (1.5)
```

This outer Hall row is not sufficient in general: the chosen edges must
also admit pairwise-disjoint slot pairs equal to the literal slot leave.

There is one useful exact face on which it is sufficient.  Call a target
catalogue **slot-separable on `(D_0,U_0)`** when there are injections

```text
 sigma^-:D_0 -> S,          sigma^+:U_0 -> S              (1.6)
```

with disjoint images, and the available target over `du` is exactly

```text
             tau(du)=(d,u,sigma^-(d),sigma^+(u)).        (1.7)
```

If the slot leave is

```text
 sigma^-(D_0) disjoint union sigma^+(U_0),               (1.8)
```

then target completions are in bijection with perfect matchings of
`G_T[D_0,U_0]`.  Hence (1.5) is necessary and sufficient on this face.
Outside it, the exact target row is the four-uniform matching condition of
Lemma 1.1; replacing it by outer Hall is unsound.

## 2. What a sparse Boolean cycle can transport

Use the notation of the sparse-cycle theorem.  For `ell>=5` and
`n>=2ell-2`, its two phases are

```text
 C^0={(D_i,V_i;H_i,P_i):i in Z_ell},
 C^1={(D_(i+1),V_i;H_i,Q_i):i in Z_ell}.                (2.1)
```

All `3ell` owners `H_i,P_i,Q_i` are distinct.

### Theorem 2.1 (zero outer boundary and exact slot displacement)

For either orientation of (2.1),

```text
 partial_D(C^1-C^0)=0,       partial_U(C^1-C^0)=0,       (2.2)
 partial_S(C^1-C^0)=chi_Q-chi_P.                         (2.3)
```

Suppose `C^0 subseteq M` and

```text
                  M'=(M-C^0) union C^1                 (2.4)
```

is a legal host matching.  Then

```text
 Lambda_D(M')=Lambda_D(M),
 Lambda_U(M')=Lambda_U(M),                               (2.5)
 chi_(Lambda_S(M'))=chi_(Lambda_S(M))+chi_P-chi_Q.       (2.6)
```

For a serializable sequence `C_1,...,C_r`, (2.5) remains exact and the
right side of (2.6) is the corresponding signed sum.

#### Proof

Both phases use every `D_i` and every `V_i` once.  Their common slot bank is
`{H_i}`, while the old-only and new-only banks are respectively `{P_i}` and
`{Q_i}`.  This proves (2.2)--(2.3).  A leave is total supply minus consumed
supply, giving (2.5)--(2.6).  Additivity proves the last assertion. `square`

Thus a target matching `J` can be reached from `M` through a declared
old-to-new sparse-cycle sequence only if

```text
 res_D(J)=Lambda_D(M),       res_U(J)=Lambda_U(M),       (2.7)

 chi_(res_S(J))-chi_(Lambda_S(M))
       =sum_j (chi_(P(C_j))-chi_(Q(C_j))).              (2.8)
```

Equation (2.8) is the exact slot-alignment equation.  It is only a lattice
condition until the cycles are ordered so that each old phase is present,
each new phase is free, and every protected graphic/compiler guard passes.

### Corollary 2.2 (single-site retargeting is impossible)

Let `R` be one fixed off phase.  Suppose two gain-one macros have on phases
`A` and `A'` with

```text
 inc(A)-inc(R)=inc(t),
 inc(A')-inc(R)=inc(t'),                                  (2.9)
```

and `A'` is obtained from `A` by any sequence of count-neutral sparse-cycle
rerouters.  Then `t` and `t'` have the same lower colour and the same upper
colour.  They may differ only in their slot realization.

#### Proof

Project (2.9) to the two outer resource groups and subtract.  Every
rerouter has zero outer boundary by Theorem 2.1, so
`partial_(D,U) inc(t)=partial_(D,U) inc(t')`.  A target atom has one resource
on each outer shore, proving equality of both. `square`

This rules out the most direct robustly-matchable-graph interpretation: one
fixed C6 site cannot be joined to several different outer targets merely by
attaching zero-boundary rerouters.  Outer flexibility must be supplied by
different native gain-one packets or by a correlated multi-site macro whose
**total** target outer multiset is fixed.  Sparse cycles then transport the
pairing and slots inside that fixed multiset.

### Lemma 2.3 (batch pairing transport)

Let `J_0,J_1` be two outer-perfect target matchings on the same lower and
upper vertex sets.  Their symmetric difference is a disjoint union of
alternating cycles.  Suppose every nontrivial component has half-length
`ell` with `5<=ell<=(n+2)/2`, is literally a sparse Boolean cycle of (2.1),
and the owner banks belonging to distinct components are disjoint.  Then
the component switches commute and transport `J_0` to `J_1`, preserving the
two outer palettes exactly.  Their total slot displacement is the sum in
(2.8).

This is a positive pairing theorem, not a target-inclusion theorem.  The
hypothesis that each abstract alternating cycle has the literal Boolean
form (2.1) is essential; high girth alone does not provide that lift.

## 3. Exact guarded target-bank completion

The next theorem packages the smallest sufficient interface.  It is useful
because every row is finite and literal once `Q`, the DP body, and the
catalogues are fixed.

### Theorem 3.1 (rerouted C6 target-bank absorption)

Let `M` be a normalized fixed-`Q` side matching of order `P-h`.  Let `Z` be
a protected old-atom bank and `F_fix` a fixed physical scaffold.  Assume the
following data.

1. **Serializable neutral transport.**  There is a sequence of legal sparse
   cycle switches taking `M` to a matching `M_hat` of the same order.  Every
   prefix retains `Z`, respects all literal slot capacities, and remains on
   every protected compiler face which is required prefixwise.
2. **Exact target matching.**  There is a matching `J={t_1,...,t_h}` of C6
   target atoms such that

   ```text
                         res(J)=Lambda(M_hat).           (3.1)
   ```

   Equivalently `M_hat union J` is perfect.  On a slot-separable target face
   this row is exactly outer Hall (1.5), together with the slot displacement
   equation (2.8).
3. **Installed C6 off phases.**  For every `t_i` there is a native suspended
   C6 packet `(R_i,A_i)` satisfying

   ```text
   |R_i|=2, |A_i|=3,
   inc(A_i)-inc(R_i)=inc(t_i),
   R_i subseteq M_hat,       R_i cap Z=empty.            (3.2)
   ```

   The `R_i` are pairwise disjoint, and

   ```text
   M_plus=(M_hat-union_i R_i) union union_i A_i          (3.3)
   ```

   is a host matching.  This last clause includes all cross-packet palette
   and literal-slot conflicts; local C6 legality alone does not imply it.
4. **Contracted graphic and root guards.**  Put

   ```text
   F_0=F_fix union phi(M_hat-union_i R_i).                (3.4)
   ```

   `F_0` is a forest.  After contracting its components, the edges in
   `phi(union_i A_i)` are loopless and graphic-independent.  If every final
   component must have exactly one named root, every component of `F_0`
   initially has at most one root and, after adjoining a root-star edge for
   each root-bearing component, the selected quotient edges form a spanning
   tree with those fixed star edges.
5. **Compiler cap guard.**  The terminal state (3.3) has one literal
   target-to-cell SDR/maximal-envelope certificate.  If intermediate packet
   states are semantically visible, every pulled-back minimal compiler
   blocker also satisfies the protected-ear self-breaking/deadline order.

Then `M_plus` is an exact size-`P` fixed-`Q` host matching, retains every
protected atom, is a physical forest with the declared root state, and has
the declared downstream compiler cap.

#### Proof

By (3.1)--(3.2),

```text
 inc(M_plus)
   =inc(M_hat)-sum_i inc(R_i)+sum_i inc(A_i)
   =inc(M_hat)+sum_i inc(t_i)
   =1_(D union U union S).                              (3.5)
```

The host-matching clause in row 3 therefore makes `M_plus` perfect.  Its
order is

```text
                 P-h-2h+3h=P.                           (3.6)
```

No protected old atom is removed.  Contracting a forest preserves the
equivalence between graphic independence in the quotient and absence of a
cycle after expansion, proving the forest assertion.  The root-star base
condition is equivalent to exactly one root in every expanded component.
The final compiler assertion is row 5. `square`

Once (3.5) gives an outer-perfect slot matching and row 4 gives a forest,
the **local Boolean two-step common cap is automatic**.  Row 5 is still
needed for the downstream same-cell/maximal-envelope compiler.  A protected
pointwise cap is also not automatic: the fixed-four C6 changes its cap map
on the edited lower colours.

### Corollary 3.2 (robust target-bank template)

Let `mathcal M` be a declared family of possible DP output matchings.  A
target catalogue is a zero-defect robust bank for `mathcal M` if rows 1--5
of Theorem 3.1 can be supplied for every `M in mathcal M`.  It is enough to
verify the following static factorization.

1. Every pair of outer leaves occurring in `mathcal M` satisfies the robust
   Hall inequalities (1.5) in a declared target graph.
2. Every Hall matching has a slot lift reachable by the exact signed
   displacement equation (2.8) through a serializable sparse-cycle atlas.
3. Every reached target matching has a simultaneous, matching-indexed
   choice of installed C6 packets satisfying rows 3--5.

Under these hypotheses every DP output in `mathcal M` closes exactly.

The adjective **matching-indexed** is load-bearing.  Alternatives incident
with one target colour may overlap, because they are never selected
together; options belonging to disjoint selected target edges must be
compatible.  A pairwise-disjoint list of already selected packets is only
one matching of the target graph and has no such robustness.

### 3.3 The natural JMS-shaped macro encoding

After the old phases in row 3 have genuinely been installed, there is a
useful exact contraction with the formal Joos--Mubayi--Smith profile

```text
                         p=1, q=3, r=3.                (3.7)
```

Let `mathsf P` be the lower target resources and let `mathsf Q` contain the
upper and two literal-slot resources of ordinary atoms.  An ordinary side
atom is then an `H_1` edge with one `mathsf P` resource and three
`mathsf Q` resources.  Here `H_1` is taken in the residual host obtained by
deleting every resource already occupied by the common installed off bank;
otherwise the contraction is not faithful.  For an installed packet with target

```text
                         t=(d,u,s^-,s^+),               (3.8)
```

make three formal duplicates `u_tilde,s^-_tilde,s^+_tilde` in a disjoint
part `mathsf R`.  Contracting the already-present two-atom off phase to one
completion choice gives the macro

```text
              {d,u_tilde,s^-_tilde,s^+_tilde},          (3.9)
```

an `H_2` edge with one `mathsf P` resource and three `mathsf R` resources.
Mixed conflicts must forbid a duplicate together with any ordinary atom or
other macro using the actual resource it represents.  Expanding a selected
macro means replacing its installed off phase by its three-atom on phase.

This contraction is exact as a finite selection encoding under three
literal hypotheses:

1. every macro's off phase is already installed in one common matching;
2. ordinary choices avoid that installed bank, and all actual-resource
   collisions represented by the formal duplicates are forbidden; and
3. expansion passes rows 4--5 of Theorem 3.1.

Unselected macros leave their off phases untouched.  Selecting (3.9)
deletes exactly its own off phase and inserts its on phase.  Sharing the
`mathsf P` vertex forbids an ordinary atom from using the same lower target;
the mixed duplicate conflicts do the analogous job for its actual upper and
two slots.  Under the three hypotheses, expansion is therefore a literal
host matching operation.

It is not a way to plant an off phase: a conflict system can forbid a
choice, but cannot impose the positive implication that selecting (3.9)
also selected its two missing old atoms.  Nor does the formal profile prove
the robust outer Hall row.  Theorem 2.1 still says that every sparse
rerouter preserves the outer leave.

The separate exact applicability audit

```text
MATH_THEOREM_CATALAN_JMS_TRIPARTITE_C6_MACRO_EXPONENT_NOGO_20260731.md
```

shows that the global Catalan host violates the simultaneous JMS size and
codegree exponent requirements, and that a disjoint planted packet bank has
completion degree one rather than the required local spread.  Thus (3.7)
is a correct **conditional macro encoding**, not an application of the JMS
black box.

## 4. A literal Boolean obstruction to a disjoint target bank

Take the fixed-four suspension with `n=3`.  Let `|H|=2` and choose four
points `a,b,c,z` outside `H`.  Put, cyclically,

```text
 D_i=H+r_i,
 V_i=H+r_i+r_(i+1)+z,
 X_i=H+r_i+z,
 Y_i=H+r_i+r_(i+1).                                  (4.1)
```

The two phases are

```text
 E^0={(D_i,V_i;X_i,Y_i):i in Z_3},
 E^1={(D_i,V_(i-1);X_i,Y_(i-1)):i in Z_3}.            (4.2)
```

They use the same twelve typed resources.  Regard `E^0` as a prepacked
resource-disjoint target bank.  Its outer graph is the matching

```text
                         D_i -- V_i.                    (4.3)
```

Now put

```text
 t=(D_0,V_2;X_0,Y_2),          M=E^1-{t}.              (4.4)
```

Within the twelve-resource hex host, `M` is a two-atom matching and its
leave is exactly the legal atom `t`.  But

```text
             G_(E^0)[{D_0},{V_2}] has no edge.          (4.5)
```

Hence no subset of the prepacked bank covers this leave.  By Theorem 2.1,
no sequence of zero-outer-boundary sparse rerouters can change the singleton
outer leave `{D_0},{V_2}`.  This is a literal Boolean target-bank failure,
not an abstract prime-field obstruction.

This fixture is an unpunctured local host statement.  It remains a literal
fixed-`Q` obstruction for any admissible `Q` retaining its three displayed
lower colours, but the audit does not assert that condition for every
parameter-three common basis or that this particular two-atom body is a DP
colour class.

More generally, let `T={t_i}` be any pairwise-resource-disjoint target atom
bank.  Its lower and upper resources define a partial bijection `pi`.  A
balanced outer leave `(D_0,U_0)` can be covered by a subset of `T` if and
only if

```text
                    D_0 subseteq dom(pi),
                    U_0=pi(D_0),                         (4.6)
```

plus the analogous literal slot equality.  Thus a disjoint bank is robust
only for synchronized leaves of its own partial bijection.  The linear
prepacking theorem proves capacity for many private packets, but not the
overlapping alternatives required by (1.5).

### 4.1 Common-installed branching also fails locally

There is a stronger obstruction to the most literal overlapping-bank
architecture.  Say that two target options have a **common installed
realization** when both two-atom off phases lie in one host matching and
that matching is disjoint from every resource of both target atoms.  The
last clause is necessary: selecting either option removes only its own off
phase, so the unselected option's off phase must not block the selected
target.

### Proposition 4.1 (no common-installed lower branching at `n=3`)

In the unpunctured parameter-three fixed-four host, two distinct target
atoms with the same lower colour have no common installed realization by
native suspended C6 packets.  Consequently any target graph whose complete
option menu is preinstalled in one common off matching has lower degree at
most one.

#### Proof

Fix the lower set `D` and write its three outside points as `x,y,z`.  Two
distinct target uppers may be written

```text
                  V_y=[6]-{y},       V_z=[6]-{z}.       (4.7)
```

They share the target-complement point `x`.  A packet through target
`(D,V_c)` chooses `b in D` and orients the two points of `V_c-D` as
`(a,s)`.  Its two off uppers are

```text
                         [6]-{b},     [6]-{a}.           (4.8)
```

To keep both target uppers in (4.7) free, the second upper in (4.8) can be
neither of them.  Hence both packets are forced to take `a=x`.  Their
second off atoms then have the common upper `[6]-{x}` and respective lower
sets

```text
                  (D-{b_y})+y,       (D-{b_z})+z.       (4.9)
```

The atoms in (4.9) are distinct for every choice of `b_y,b_z`, but share
one upper resource.  They cannot coexist in a host matching. `square`

The exhaustive audit lists all `60` target atoms and their `6` native
packets (`360` packets total).  Across all `60` pairs of distinct targets
sharing a lower colour it tests `2,160` packet pairs.  Exactly `1,080`
pairs have mutually disjoint off phases if target resources are ignored,
but **zero** are also disjoint from both target atoms.  The target-free
clause is therefore load-bearing.

Proposition 4.1 closes only the strong architecture in which every offered
alternative is planted simultaneously.  It does not exclude choosing the
target matching jointly with the DP body and planting only the selected
off phases; that weaker matching-indexed correlated construction remains
the live route in Corollary 3.2.

## 5. Consequences for the two-scale programme

The exact division of labour is now:

* **DP/body steering:** produce an outer leave in a family on which a target
  graph has robust Hall.  Neither full-colour deficiency identities nor
  common-basis one-point marginals prove this.
* **Native gain:** provide matching-indexed suspended-C6 packets whose old
  phases are installed.  Count-neutral rerouters cannot replace this row.
* **Pairing and slot transport:** use sparse Boolean cycles only inside a
  fixed lower/upper leave fibre, solving (2.8) with a legal serialization.
* **Physical completion:** test the contracted graphic/root row after the
  old packet halves are deleted.
* **Cap completion:** use automatic local Boolean cap only after exact outer
  saturation and a forest are proved; export a separate literal certificate
  for the downstream compiler.

Uniform common-basis marginal survival remains useful after a robust atlas
has been built.  If each target option has constant declared risk and the
target template remains robust after the resulting `O(P/n)` option/site
failures, the existing weighted marginal theorem selects a common basis on
which Corollary 3.2 applies.  Marginals do not build the robust target graph,
do not install its off phases, and do not imply the slot-displacement or
graphic rows.

The first honest all-parameter target is therefore:

> Construct, before choosing `Q`, an overlapping Boolean target graph with
> constant-risk C6 menus and a declared DP outer-leave family satisfying
> robust Hall; after `Q`, prove that every selected Hall matching has an
> installed packet realization and lies in the guarded sparse-cycle slot
> orbit of the body.

The literal obstruction in Section 4 shows why replacing “overlapping
target graph” by “linear disjoint packet bank” is false.

## 6. Independent audit

Run

```text
python3 scratch/audit_catalan_c6_robust_target_bank_gate_20260731.py
```

The dependency-free audit:

* reconstructs the complete parameter-three fixed-four hex;
* verifies both phase matchings and exact twelve-resource equality;
* verifies that deleting the cross atom in (4.4) leaves exactly that atom;
* exhausts all target-bank subsets and the legal singleton outer pairs,
  obtaining three diagonal successes and three cross failures;
* exhausts all `360` native parameter-three packets and verifies the
  common-installed branching count `1080/2160` off-compatible but
  `0/2160` target-free; 
* checks that the full phase exchange has zero outer boundary; and
* reconstructs the canonical `n=8,ell=5` sparse switch, verifying zero outer
  boundary and the exact `P-Q` slot-leave displacement.

It writes

```text
scratch/catalan_c6_robust_target_bank_gate_20260731.audit.json.
```

The audit does not construct a DP-aligned target graph, installed old-phase
bank, contracted rooted forest, or downstream compiler certificate.  Those
are exactly the scopes excluded above.
