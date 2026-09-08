# Orientation words compress the q4 k17 post-owner lift fibres to at most 512 classes per reflected footprint

**Date:** 2026-08-14

**Status:** exact symbolic reduction.  It gives a complete finite interface
for extracting the non-literal lifts above a selected reflected owner
footprint and for coupling their lower, upper, and directed rank-seven
tickets.  It does not assert that any off-diagonal fibre is nonempty, that
the resulting multiple-choice master is feasible, or that signature-level
choices have simultaneous resource-disjoint physical representatives.

## 0. Outcome

Let `rho` be reflection on the 1,430 rank-nine translation necklaces.  A
usable nonself reflected q4 pair meets ten nonfixed reflection orbits, one
owner necklace in each orbit on either shore.  Its reduced footprint is a
ten-set `M` of the 680 nonfixed owner rows.

Choose once and for all one reference necklace `a_r` above every nonfixed
row `r`, with the other necklace equal to `rho(a_r)`.  A rail witness `w`
above `M` determines an orientation word

```text
 eps_w(r)=0  if E(w) contains a_r,
 eps_w(r)=1  if E(w) contains rho(a_r).                       (0.1)
```

Here `E(w)` is the unordered oriented deck of ten rank-nine necklaces,
not merely its ten reduced rows.

The reduction has five conclusions.

1. For witnesses with the same reduced footprint,

   ```text
                         E(u)=E(v) iff eps_u=eps_v.             (0.2)
   ```

   Moreover `eps_(rho w)=1-eps_w`.  Hence an unordered reflected footprint
   has at most `2^10/2=512` complement classes of oriented lift fibres,
   equivalently 512 normalized fibres after fixing one anchor bit.
2. The two rails `u+rho(v)` cover both owner necklaces above every row of
   `M` exactly once if and only if `u,v` belong to the same oriented fibre.
   Equality of the reduced row mask alone is insufficient.
3. Fixing one row of `M` to its reference necklace reduces the exact fibre
   key to the other nine bits.  The already proved anchored raw
   parameterization, followed by an exact footprint filter, enumerates
   every one of these fibres.  No all-row rail atlas is required.
4. If `s(w)` is an additive typed-ticket signature, the complete two-sided
   ledger menu over one oriented fibre `W` is the Minkowski menu

   ```text
                   {s(u)+rho s(v):u,v in W}.                   (0.3)
   ```

   Relative to one base witness it has an exact affine difference form.
   If a literal base rail is frozen, the menu becomes one-sided.  The two
   cases must not be conflated.
5. Rank-seven phase data are directed cyclic words.  Cyclic rotation may
   be replaced by an explicit phase variable, but reversal may not be
   quotiented without a separate reversed-chronology certificate.

## 1. Exact orientation-word classification

Let `pi` map a nonfixed owner necklace to its reflection-pair row.  A
quotient-simple rail `w` is **pair-usable** when

```text
                    E(w) intersect rho(E(w)) = empty.          (1.1)
```

Then `M(w)=pi(E(w))` has size ten and `E(w)` contains exactly one of
`a_r,rho(a_r)` for every `r in M(w)`.  Thus `(0.1)` is well defined.

### Theorem 1.1 (exact oriented fibre key)

For pair-usable witnesses `u,v` with `M(u)=M(v)=M`, equality of their
oriented owner decks is equivalent to equality of their orientation words.
Reflection complements every bit.

#### Proof

On one row `r`, the pair `{a_r,rho(a_r)}` has two distinct members.
The bit in `(0.1)` selects exactly one of them.  Equality of all ten bits
is therefore equivalent row by row to equality of the two ten-necklace
decks.  Reflection exchanges the two members on every row and hence
complements all ten bits.  \(\square\)

### Theorem 1.2 (owner-exact cross lift)

Let `u,v` have the same reduced footprint `M`.  The deck of
`u+rho(v)` covers the two owner necklaces above every row of `M` once each
if and only if `eps_u=eps_v`.

#### Proof

Above a row `r`, the first rail uses bit `eps_u(r)` and the reflected second
rail uses bit `1-eps_v(r)`.  These are the two different bits exactly when
`eps_u(r)=eps_v(r)`.  Applying this independently on all ten rows proves
the claim.  \(\square\)

Thus the exact oriented fibre is

```text
             W(M,eps)={w:M(w)=M and eps_w=eps}.                (1.2)
```

The complementary words `eps` and `1-eps` describe the two orientations
of the same unordered reflected footprint.  Complementation has no fixed
binary word, so there are exactly `2^9=512` possible complement classes
before realizability is imposed.  This is an upper bound; many classes may
be empty.

There is also an exact option symmetry:

```text
       (u,v,eps) -> (rho(v),rho(u),1-eps)                      (1.3)
```

does not change the unordered physical pair `{u,rho(v)}`.  A catalogue may
therefore choose the lexicographically smaller of `eps,1-eps` and transform
the two witnesses by `(1.3)` when necessary.

## 2. Complete selected-footprint extraction

Fix a selected footprint `M` and a row `r_0 in M`.  Choose a physical
rank-nine subset `A subset Z_17` representing the reference necklace
`a_(r_0)`.  Enumerate the anchored pure-rail parameters

```text
 C subset A, |C|=5;
 (s_0,s_1,s_2,s_3) an order of A-C;
 (s_4,...,s_9) an ordered six-subset of Z_17-A.                (2.1)
```

They have raw cardinality

```text
                   C(9,5) 4! P(8,6)=60,963,840.               (2.2)
```

Construct

```text
             O_i=C union {s_i,s_(i+1),s_(i+2),s_(i+3)}.       (2.3)
```

Retain exactly the quotient-simple, pair-usable witnesses with reduced
footprint `M`.  Partition them by their remaining nine orientation bits;
the anchor bit is zero.

### Theorem 2.1 (anchored completeness for all lift fibres over `M`)

The retained catalogue contains every pair-usable rail above `M`, modulo
reflection of the whole rail and the global translation/cyclic-start
normalization already built into `(2.1)`.

#### Proof

Take any pair-usable witness `w` above `M`.  Exactly one owner of `w` lies
above `r_0`.  If its necklace is `rho(a_(r_0))`, reflect the whole witness;
the resulting occurrence lies in necklace `a_(r_0)`.  The rank-nine
translation action is free, so there is a unique translation taking that
occurrence to the chosen physical representative `A`; rotate starts so it
is `O_0`.  Its core is then a unique five-subset of `A`, its first four
support labels are `A-C` in their cyclic order, and its remaining six
support labels are an ordered six-subset of `Z_17-A`.
These are exactly the parameters `(2.1)`.  The literal filters recover its
footprint and orientation word.  \(\square\)

Consequently a completed owner certificate needs only 54 selected-mask
extractions, not a broad catalogue over all 680 target rows.  The theorem
is about completeness, not runtime or the number of signatures in a fibre.

## 3. Exact additive menu and the baseline distinction

Let `A_8,A_10,A_7` be the free abelian occurrence groups on the rank-eight,
rank-ten, and rank-seven translation orbits.  For a rail `w` put

```text
 l_8(w)=sum_i [O_i intersect O_(i+1)] in A_8,
 u_10(w)=sum_i [O_i union O_(i+1)] in A_10,
 l_7(w)=sum_i [O_i intersect O_(i+1) intersect O_(i+2)] in A_7,
 s(w)=(l_8(w),u_10(w),l_7(w)).                                (3.1)
```

Reflection acts linearly on every occurrence group.  By Theorem 1.2 an
owner-exact option over `W=W(M,eps)` has additive typed contribution

```text
                         T(u,v)=s(u)+rho s(v).                 (3.2)
```

Thus it is enough at the ledger stage to retain one physical witness for
every distinct value of `s(w)` in `W`; all other copies have identical
linear columns.  If `w_0 in W` and

```text
                         D_W={s(w)-s(w_0):w in W},              (3.3)
```

then the complete two-sided menu is exactly

```text
       s(w_0)+rho s(w_0) + D_W + rho D_W.                     (3.4)
```

Both occurrences of `D_W` in `(3.4)` are finite sets, so `+` means a
Minkowski sum, not an integer span.

### One-sided fixed-base menu

Suppose the owner certificate freezes a literal pair
`u_0+rho(u_0)` and permits only the reflected mate to be replaced.  The
exact menu is

```text
                       {s(u_0)+rho s(v):v in W},               (3.5)
```

and its current relative to the frozen literal pair is

```text
                            rho(s(v)-s(u_0)).                  (3.6)
```

This is the setting in which a one-sided `Delta` column is sufficient.

### Two-sided free-base menu

If the owner master selects only the reduced footprint and leaves both
physical shores free, `(3.4)` is required.  Rewriting one option as

```text
 T(u,v)=[s(u)+rho s(u)] + rho(s(v)-s(u))                      (3.7)
```

shows the obstruction to a difference-only catalogue: its literal
baseline depends on `u`.  Retaining only `rho(s(v)-s(u))` can identify
options having different absolute lower, upper, or rank-seven loads.

The lattice

```text
 L_W=span_Z D_W,
 s(w_0)+rho s(w_0)+L_W+rho L_W                               (3.8)
```

is a useful necessary relaxation of the exact menu.  Membership in
`(3.8)` is not sufficient unless saturation of the finite Minkowski menu
is separately proved.

## 4. Directed rank-seven phase data

The additive vector `l_7(w)` forgets where its ten occurrences lie.  For
the canonical rank-seven schedule retain instead the directed cyclic word

```text
 q(w)=(q_0,...,q_9),
 q_i=[O_i intersect O_(i+1) intersect O_(i+2)].                (4.1)
```

A cyclic rotation of the support order rotates `(4.1)` and changes no
additive deck.  It may therefore be canonicalized under the directed
`C_10` action while exposing an explicit phase `delta in Z_10`.  On the
pure period-ten face the canonical unmarked positions are

```text
                         {delta,delta+3}.                      (4.2)
```

Reflection acts entrywise:

```text
                         q(rho w)=rho(q(w)).                   (4.3)
```

An owner-exact pair option must retain the two constituent words
`q(u),rho(q(v))` separately, because the two rails receive independent
phase choices.

Reversal is different from rotation.  It reverses the directed chronology
of `(4.1)`.  The frozen 72-state schedule theorem is directed and does not
claim reversal closure.  Hence reversal may be used to identify owner or
unordered ticket decks, but it may not be removed from a phase-decorated
menu without a literal reversed-state certificate.

## 5. Exact post-owner multiple-choice interface

Fix an exact owner scaffold with its 35 self columns and 54 nonself
reflected footprints.  For every nonself footprint choose one option

```text
 (eps,u,v,delta_u,delta_v),
 u,v in W(M,eps),  delta_u,delta_v in Z_10.                    (5.1)
```

On phase-decorated options the complementary symmetry is explicitly

```text
 (eps,u,v,delta_u,delta_v)
   -> (1-eps,rho(v),rho(u),delta_v,delta_u).                  (5.2)
```

Thus the two phases swap together with the two physical shores.  This
symmetry removes duplicate descriptions.  Self columns retain their own
literal lift and phase menus.  Owner exactness is automatic from
Theorem 1.2.  The next exact typed rows are:

```text
 total immediate-lower load on every rank-eight orbit = 1;
 1 <= total immediate-upper load on every rank-ten orbit <= 2;
 total L3_load(A)-unmarked_phase(A) = 1 for every rank-seven orbit A;
 total L3_load(A) <= 2 for every rank-seven orbit A.           (5.3)
```

For one constituent rail with word `q` and phase `delta`, its unmarked
contribution in `(5.3)` is at positions `delta,delta+3`.  Equations `(5.3)`
therefore mark every singleton rank-seven occurrence and exactly one of the
two occurrences of every doubled orbit.  Coupling the chosen phases to the
already frozen directed state cycles supplies the canonical pure-face
rank-seven schedule; it does not follow from `l_7` alone.

One may omit the rank-ten row if only the lower/L3 gate is being tested,
but doing so is a declared relaxation of the joint typed master.

## 6. Multiplicity and physical-resource boundary

Signature deduplication is exact for the linear ledger rows because equal
signatures give equal columns.  It is not a physical packing theorem.
For the phase-decorated master, deduplication must use the augmented
`(s,q,resource decoration)` rather than `s` alone.  For every retained
augmented signature the extractor must also keep

```text
 one literal (core,ordered support) witness;
 the complete witness multiplicity or a regenerating key;
 every resource/collar/chronology decoration needed by the later master.
                                                                    (6.1)
```

After a signature-level solution is found, choosing simultaneous physical
representatives is a separate SDR/conflict problem.  A fibre of size one
offers only the literal pair.  Two different signatures can have no
resource-disjoint representatives, while repeated physical witnesses with
one signature can be essential for avoiding collisions elsewhere.

The present theorem proves only:

* the exact orientation key and the 512 normalized-fibre bound;
* complete extraction from one anchored selected row;
* the exact one-sided and two-sided additive menus; and
* the directed phase interface.

It does not prove lower/upper/L3 feasibility, signature saturation,
simultaneous resource disjointness, collar residence, component fusion, or
the later actuator compilation.
