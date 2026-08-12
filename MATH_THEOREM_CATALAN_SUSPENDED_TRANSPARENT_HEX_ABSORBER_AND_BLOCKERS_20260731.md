# A suspended transparent hex is an exact gain-one absorber, but not a uniform protected absorber

Date: 2026-07-31  
Status: exact dimension-uniform local identity and exact catalogue blockers.
This produces a planted four-resource absorber in every dimension.  It does
**not** prove that an arbitrary fixed-`Q` near-forest contains the off phase,
that the auxiliary colours survive puncturing, or that an `o(P)` leave can be
packed by these gadgets while preserving a downstream common cap.

## 0. Verdict

The decoration-transparent `ML(7)` incidence hex does embed uniformly in the
capacity-slot geometry.  In side parameter `n>=3`, every formal diamond atom
has exactly

\[
                           2n(n-2)                         \tag{0.1}
\]

distinct suspended-hex phase pairs through it.  Each pair is a literal
gain-one switch

\[
                  \{​\text{two off atoms}​\}
                    \longrightarrow
                  \{​\text{three on atoms}​\},           \tag{0.2}
\]

in which the on state covers exactly the four resources left free by the
off state.  Both physical projections are three-edge forests, and the six
physical slot resources agree exactly between the full old and new phases.

This is genuinely different from the refuted assertion that an arbitrary
bichromatic outer `C6` is an independently switchable Kempe circuit.  It is
a **predesigned consumptive packet** and must be planted in its off phase.

There are also two exact limitations.

1. All suspended-hex absorbers for one target meet an `n`-element owner
   transversal.  Protecting the residual slots of those owners blocks the
   entire catalogue.
2. Every orientation changes a pointwise lower-to-upper cap assignment.
   A frozen common-cap representative map can therefore block every member
   of the catalogue.

Consequently no uniform random-packing conclusion follows for an arbitrary
puncture `Q` and arbitrary protected forest.  The correct remaining theorem
would be a local-availability or resource-private packing statement, not a
pure enumeration of formal hexes.

## 1. Capacity-slot notation

Work on a ground set containing a set `K` of size `n-1` and four distinct
elements

\[
                              a,b,c,s\notin K.                    \tag{1.1}
\]

In the standard ground set of size `2n`, the other `n-3` coordinates are
spectators.  This is the dimension-uniform suspension of the six-coordinate
local pattern; equivalently one fixes an outside `(n-3)`-set.

Put

\[
\begin{array}{lll}
 D_a=K+a,&D_b=K+b,&D_c=K+c,\\
 U_{abs}=K+a+b+s,&U_{acs}=K+a+c+s,&U_{bcs}=K+b+c+s,
\end{array}                                                       \tag{1.2}
\]

and name the six rank-`(n+1)` owners

\[
 X_{ab},X_{ac},X_{bc},X_{as},X_{bs},X_{cs},\qquad
 X_{uv}=K+u+v.                                                     \tag{1.3}
\]

Choose one literal available slot `xi_uv` at every owner `X_uv`.  An atom
below records its lower colour, upper colour, and its two literal owner-slot
resources.

Define the old phase

\[
\begin{array}{lll}
 e_a=(D_a,U_{acs};\xi_{ac},\xi_{as}),&
 e_b=(D_b,U_{abs};\xi_{ab},\xi_{bs}),&
 e_c=(D_c,U_{bcs};\xi_{bc},\xi_{cs}),
\end{array}                                                       \tag{1.4}
\]

and the new phase

\[
\begin{array}{lll}
 f_a=(D_a,U_{abs};\xi_{ab},\xi_{as}),&
 f_b=(D_b,U_{bcs};\xi_{bc},\xi_{bs}),&
 f_c=(D_c,U_{acs};\xi_{ac},\xi_{cs}).
\end{array}                                                       \tag{1.5}
\]

Every listed containment is valid.  The three lower colours, three upper
colours, and six owners are pairwise distinct within their types.

## 2. Exact suspended-hex identity

### Theorem 2.1 (literal four-resource equality)

Both (1.4) and (1.5) are matchings in the four-uniform capacity-slot host,
and

\[
                         e_a+e_b+e_c=f_a+f_b+f_c                 \tag{2.1}
\]

as multisets of lower, upper, and literal slot resources.  Their physical
projections are three disjoint edges.

#### Proof

Both phases use exactly the lower bank

\[
                         \{D_a,D_b,D_c\},                         \tag{2.2}
\]

the upper bank

\[
                         \{U_{abs},U_{acs},U_{bcs}\},             \tag{2.3}
\]

and the six literal slots

\[
       \{\xi_{ab},\xi_{ac},\xi_{bc},\xi_{as},\xi_{bs},\xi_{cs}\}.
                                                                    \tag{2.4}
\]

Every resource occurs once.  The six owners in (1.3) are distinct and each
occurs once in either phase, so each physical projection is a matching of
three edges and in particular a forest. `square`

### Corollary 2.2 (gain-one state)

Designate `e_b` as the target atom and put

\[
                 A^{\rm off}=\{e_a,e_c\},\qquad
                 A^{\rm on}=\{f_a,f_b,f_c\}.                    \tag{2.5}
\]

Then the off state is disjoint from every resource of `e_b`, and

\[
   \operatorname {res}(A^{\rm on})
    =\operatorname {res}(A^{\rm off})\mathbin{\dot\cup}
      \operatorname {res}(e_b).                                  \tag{2.6}
\]

Thus (2.5) is a protected gain-one ear whenever its off phase has been
planted and the six named slots are legal.

This statement includes topology: every subset state of this one packet is
a forest.  It includes no downstream common-cap claim beyond the literal
resources displayed in (2.6).

## 3. Every formal target has a quadratic catalogue

Let

\[
        A=(D,V;(D+p,i),(D+q,j)),\qquad
        V=D+p+q,\quad |D|=n.                                    \tag{3.1}
\]

be a formal host atom, including its prescribed literal slots.  Choose

\[
       b\in D,qquad K=D-b,qquad c\notin V,                     \tag{3.2}
\]

and orient `(a,s)` as either `(p,q)` or `(q,p)`.  Use the prescribed target
slots for `xi_ab,xi_bs`, in the corresponding order, and use the canonical
slot `1` at the four auxiliary owners.  Slot `1` exists at ordinary owners
and at capacity-one anchors alike.

### Theorem 3.1 (exact formal count)

On a ground set of size `2n`, (3.2) and the two orientations give exactly

\[
                              2n(n-2)                             \tag{3.3}
\]

distinct old/new phase pairs whose designated atom is `A`.

#### Proof

There are `n` choices of `b`, exactly `n-2` choices of `c` outside the
rank-`(n+2)` set `V`, and two orientations.  Substitution in (1.2)--(1.5)
gives `e_b=A`.  The lower bank recovers `b` and `c`, while the incidence of
the two target-complement elements with the auxiliary upper colours recovers
the orientation, so different parameters give different phase pairs.
`square`

This is the exact count of the canonical slot-`1` embeddings.  Ordinary
owners may provide further literal slot lifts; they are not included in
(3.3).

This is a count in the **unpunctured formal host**.  A fixed common basis `Q`
may delete either auxiliary lower colour `D_a` or `D_c`; anchor capacities
may remove a required slot; and an already chosen target matching need not
contain the two off atoms.  Therefore (3.3) is not an absorber-supply theorem
for an arbitrary post-nibble leave.

## 4. The exact `ML(7)` fixture is the base pattern

The transparent switch recorded in the positive `ML(7)` fixture is

\[
 (30,156),(54,150),(60,180)
 \longrightarrow
 (30,150),(54,180),(60,156).                                    \tag{4.1}
\]

Take

\[
 K=\{2,4\},\qquad(a,b,c,s)=(1,3,5,7).                            \tag{4.2}
\]

Intersections and unions of the three old edges in (4.1) are respectively
`D_b,U_abs`, `D_a,U_acs`, and `D_c,U_bcs`; the new edges are exactly
`f_a,f_c,f_b`.  Hence (4.1) is Theorem 2.1 literally, with two unused
spectator coordinates in the displayed `J(8,4)` realization.

The suspension fixes the local six-coordinate pattern and adds the outside
core/spectators.  Rank and containment, not an accidental small-dimensional
symmetry, prove the identity.

## 5. A biclique cannot replace the hex

The natural affine `TD(4,5)`/`K_(5,5)` refactorization fails for a separate
and exact reason.

### Lemma 5.1 (complete-containment owner collapse)

Let `mathcal D` contain at least two distinct rank-`n` sets and `mathcal V`
at least two distinct rank-`(n+2)` sets.  If

\[
                         D\subset V
       \qquad(D\in\mathcal D, V\in\mathcal V),                 \tag{5.1}
\]

then

\[
        H:=\bigcup_{D\in\mathcal D}D
          =\bigcap_{V\in\mathcal V}V,qquad |H|=n+1.             \tag{5.2}
\]

Moreover every diamond `(D,V)` in the complete incidence rectangle has
`H` as one of its two physical owners.

#### Proof

Two distinct rank-`n` sets have union of size at least `n+1`.  That union is
contained in the intersection of two distinct rank-`(n+2)` sets, whose size
is at most `n+1`.  Hence both have size exactly `n+1`.  Enlarging the union
over all lower sets or shrinking the intersection over all upper sets cannot
change this common set, proving (5.2).  Since

\[
                              D\subset H\subset V,
\]

and the ranks rise by one at each inclusion, `H` is one of the two owners of
the diamond `(D,V)`. `square`

If the owner capacity is `c(H)<=2`, any physical-slot matching uses at most
two atoms from this complete rectangle (at most one when `H` is an anchor).
Thus a five-atom affine `K_(5,5)` phase cannot embed directly in the physical
slot host.

The hypotheses requiring two **distinct** sets on both shores are necessary:
with one lower set the union may have rank `n`, and with one upper set the
intersection may have rank `n+2`.  For `n=0` two distinct lower sets do not
exist; otherwise no additional edge case occurs.

The suspended hex avoids this collapse.  Its lower--upper incidence graph is

\[
                            K_{3,3}\setminus M,                    \tag{5.3}
\]

the six-cycle obtained by deleting the three noncontainments

\[
     D_a\not\subset U_{bcs},\quad
     D_b\not\subset U_{acs},\quad
     D_c\not\subset U_{abs}.                                    \tag{5.4}
\]

There is no common owner: the six owners in (1.3) are all different.  This
is exactly why the hex can use three physical atoms per phase while the full
biclique cannot.

## 6. Exact catalogue blockers

### Proposition 6.1 (an `n`-owner transversal)

For the target (3.1), define

\[
                         \mathcal W_A=\{V-b:b\in D\}.             \tag{6.1}
\]

Every suspended-hex packet through `A` uses a slot of one owner in
`mathcal W_A`; more precisely, the packet selected by `b` uses

\[
                         X_{as}=V-b.                              \tag{6.2}
\]

Hence the owner projection of the whole `2n(n-2)`-packet catalogue has a
transversal of size `n`.

#### Proof

With `K=D-b` and `{a,s}={p,q}`,

\[
                         X_{as}=K+a+s=D-b+p+q=V-b.                \tag{6.3}
\]

This owner occurs in both phases. `square`

Thus, if every residual slot at the owners in `mathcal W_A` is already used
or protected, no packet in this catalogue is admissible.  This is a sharp
scope obstruction to an absorber theorem quantified over an arbitrary
protected bank.  It is not a claim that every near-forest actually saturates
this transversal.

### Proposition 6.2 (pointwise-cap change)

In either orientation, the auxiliary lower colour

\[
                         D_a=D-b+a                                \tag{6.4}

is paired in the off phase with `U_acs` and in the on phase with the target
upper colour `U_abs=V`.  Therefore a protected pointwise common-cap map on
all candidate colours `D-b+p` and `D-b+q` can block every orientation.

This does not obstruct a merely existential common cap which is recomputed
after all packets.  It does show that the local identity does not preserve a
preselected cap representative coordinate by coordinate.

## 7. Packing verdict and the correct next statement

The exact identity supplies a useful **planted** absorber template.  It does
not by itself absorb the leave of an arbitrary Delcourt--Postle colour class:

1. both off atoms must already lie in the target matching;
2. both auxiliary lower colours must survive the fixed puncture;
3. all six literal slots must be legal and compatible with protection;
4. packets chosen for different targets must be resource-private; and
5. the switched state must retain or regenerate the downstream common cap.

Proposition 6.1 shows that these hypotheses cannot be removed by citing the
quadratic formal count (3.3).  A random packing argument needs, at minimum,
a pointwise availability/dispersion hypothesis for the packet catalogues and
a Hall or matching theorem for resource-private choices.  No such hypothesis
holds uniformly for every protected bank.

There is nevertheless a useful unconditional **prepacking** statement.  It
shows that resource privacy costs a constant fraction of `P`, not a Catalan
factor.

### Theorem 7.1 (linear unpunctured packet bank)

Use slot `1` at every owner; this slot exists whether or not that owner later
becomes a capacity-one anchor.  In the unpunctured host there is a
pairwise-resource-disjoint family of suspended-hex packet supports of size

\[
             T>{PN\over18N+36P}
               ={n+2\over54n}P>{P\over54},                       \tag{7.1}
\]

where the unpunctured lower shore has

\[
 M=\binom{2n}{n}=P+C,
 \qquad {N\over P}={n+2\over n-1}.                               \tag{7.2}
\]

After a common-basis puncture the surviving lower and upper shores both
have order `P`.

In particular `T=Theta(P)=Theta(n C)`, not merely `O(C)`, where
`C=Theta(P/n)` is the Catalan puncture scale.

#### Proof

Take the full `Sym(2n)` orbit `mathcal O` of one literal-slot packet support.
Every support has exactly three lower resources, three upper resources, and
six slot-`1` owner resources.  Transitivity and double counting give the
three resource degrees

\[
 d_D={3|\mathcal O|\over M},\qquad
 d_U={3|\mathcal O|\over P},\qquad
 d_S={6|\mathcal O|\over N}.                                    \tag{7.3}
\]

The intersection graph on packet supports therefore has maximum degree at
most

\[
 3(d_D-1)+3(d_U-1)+6(d_S-1)
 ={9|\mathcal O|\over M}+{9|\mathcal O|\over P}
   +{36|\mathcal O|\over N}-12
 \le {18|\mathcal O|\over P}+{36|\mathcal O|\over N}-12.       \tag{7.4}
\]

A greedy independent set has order at least `|mathcal O|/(Delta+1)`, which
is strictly larger than the first expression in (7.1).  Resource-disjoint
supports give simultaneously disjoint off and on states. `square`

The constant `1/54` is only the crude greedy guarantee.  Elementary resource
counting gives `T<=P/3` from the upper shore (`T<=M/3` from the unpunctured
lower shore) and, if owner vertices rather than literal slots are required
to be private, `T<=N/6`.
All these bounds are linear in `P`; there is no Catalan-scale resource
obstruction.

### Corollary 7.2 (uniform-marginal survival)

Let a packet bank of order `T` be fixed before the synchronized common basis
is chosen.  Under the exact uniform-marginal distribution on common bases,
a fixed lower colour is punctured with probability at most

\[
                   p={C\over N}={2(2n+1)\over n(n+2)}.            \tag{7.5}
\]

Each suspended hex has three lower colours.  Hence

\[
             \mathbb E[\text{invalid packets}]\le3pT=O(T/n),    \tag{7.6}
\]

with no independence assumption.  Some synchronized common basis therefore
retains at least `(1-3p)T` packets.  Slot `1` survives even at an anchor, so a
fully resource-disjoint bank has no additional anchor-capacity loss.

For a coupled two-shore packet the same union bound uses six puncture risks.
This quantifier swap still does **not** ensure the selected common basis has
the separate `rho=0`, attachment, trace, or downstream common-cap property.
Nor does it align the planted target resources with the leave of the later
near-forest.  Moreover every packet held in its off state deliberately leaves
one lower and one upper outer resource unmatched, so a near-perfect starting
forest should plant only an `o(P)` subbank unless most packets are already
activated.  The result is a linear raw catalogue from which such a subbank
may be selected, not an exact cover-down.

The strongest honest next lemma is therefore:

> **Aligned suspended-hex packing lemma.**  Construct the near-forest and its
> leave together with planted off phases so that every leave atom has many
> admissible packet choices outside all protected owner transversals, the
> packet-choice hypergraph has a near-perfect resource-private matching, and
> the aggregate switch leaves a feasible common cap.

This is more structured than a generic bichromatic-`C6` reservoir and weaker
than an arbitrary-postprocessing absorber theorem.  The local six-port
identity is now exact; correlated planting and common-cap regeneration are
the remaining gates.

## 8. Distinction from the sparse `5 <-> 5` rerouter

The independently frozen construction

```text
MATH_THEOREM_CATALAN_SPARSE_FIVE_CYCLE_PHYSICAL_SWITCH_20260731.md
scratch/audit_catalan_sparse_five_cycle_physical_switch_20260731.py
```

has also been replayed.  For `n>=8`, it uses five lower colours `D_i`, five
upper colours `V_i`, and the two alternating phases of their sparse
lower--upper `C10`.  Its fifteen owners `H_i,P_i,Q_i` are all distinct.  Each
phase is five disjoint physical edges, and both outer palettes agree exactly.

The roles are different:

* the suspended `C6` is a planted **gain-one absorber**, replacing two atoms
  by three while filling four previously free resources;
* the sparse `C10` is a **count-neutral rerouter**, replacing five atoms by
  five and preserving both outer palettes.

For the `C10`, the five `H_i` slots are common to both phases, while the five
`P_i` slots are replaced by the five `Q_i` slots.  Thus it is a protected
constant-support kernel switch only when the `Q_i` residual slots are free
and the changed pointwise cap pairing and quotient-graphic topology are
accepted.  Its internal forests do not imply that their union with an
exterior protected forest remains acyclic.

## 9. Independent audit

The script

```text
scratch/audit_catalan_suspended_transparent_hex_absorber_20260731.py
```

checks the literal `ML(7)` switch and, for every `3<=n<=10`, enumerates all
`2n(n-2)` formal embeddings through a canonical target.  It verifies ranks,
containments, exact four-resource equality, gain one, physical-forest
topology, distinctness of all parameterized phase pairs, and the universal
owner transversal.  It additionally reconstructs the sparse `C10` for
`8<=n<=12`, independently checking all fifteen owners, both outer palettes,
and the `5+5+5` common/old-only/new-only slot profile.  Its output is

```text
scratch/catalan_suspended_transparent_hex_absorber_20260731.audit.json
```

with status `PASS`.  The audit explicitly excludes puncture survival,
protected-slot availability, common-cap preservation, and global packing.
