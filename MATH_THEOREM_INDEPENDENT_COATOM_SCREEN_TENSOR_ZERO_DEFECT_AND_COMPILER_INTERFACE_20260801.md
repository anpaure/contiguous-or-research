# Coatom-screen tensors: a zero-owner-defect ECO macro and its exact fixed-basis compiler gate

Date: 2026-08-01  
Status: unconditional local macro theorem; exact conditional compiler theorem  
Scope: the `B(k)+O(1)` transparent-packet route, not a complete Pascal induction

## 0. Outcome

The four repeated-screen owner defects in the first coatom-screen tensor are
not intrinsic.  Every transition has a second useful rank-preserving common
Johnson neighbour.  Replacing one occurrence in each of the four repeated
screen pairs according to any of the three patterns

\[
                         0110,\qquad1011,\qquad1100                 \tag{0.1}
\]

produces an exact macro with all of the following properties, uniformly for
every depth `d>=1`:

* all `12d+35` rank-`r` owners are distinct;
* the old and new owner sets are equal;
* the full ordered prefix/suffix OR signatures are equal;
* the distinct-value internal interval-OR decks are equal;
* every internal coordinate run has length at least `d+1`; and
* the clipped residence boundary states are equal.

Thus the four owner defects require **zero** exported state.  There is no
need to route them through the lower compiler.

The remaining U5 condition does not become automatic.  Fix a trace-guarded
compiler bank `H`, let `rho*` be the worst reachable residence frontier, and
let `D_mac` be the cells whose guarded incidences are not invariant under the
two macro phases.  A fixed matching survives exactly when it can avoid

\[
                         D^*=D(\rho^*)\cup D_{mac}.                 \tag{0.2}
\]

Equivalently,

\[
 \delta_H(D^*)=
   \max_{X\subseteq\mathcal L}
      \left(|X|-|N_H(X)\setminus D^*|\right)=0.                   \tag{0.3}
\]

A bounded value of (0.3), together with a literal bounded terminal repair,
is sufficient for `B(k)+O(1)`.  The tensor theorem proves that no additional
`+4` owner term belongs in this deficiency.  It does not prove (0.3) for the
actual Pascal compiler host.

## 1. The tensor

Take one of the three literal Johnson connector rows with equal internal OR
support in
`MATH_THEOREM_INDEPENDENT_ECO_SIXSEAM_SIGNATURE_CONNECTOR_AND_FRAGMENT_LIFT_20260731.md`.
Write its old and new active words as

\[
                  W^\epsilon=(V_0^\epsilon,\ldots,V_{11}^\epsilon),
                  \qquad\epsilon\in\{0,1\},                       \tag{1.1}
\]

where every `V_j` is a distinct rank-three subset of the six active
coordinates, consecutive owners are Johnson adjacent, and the two words
have the same first owner, last owner, and owner set.

Put

\[
            n=d+2,qquad F=\{f_0,\ldots,f_{n-1}\},
            \qquad C_t=F-\{f_t\}.                                \tag{1.2}
\]

Let `K` be disjoint from the active and filler coordinates, with

\[
                             |K|=r-d-4.                            \tag{1.3}
\]

For every active owner use the coatom block

\[
       B_j=\bigl(K\cup V_j\cup C_0,\ldots,
                   K\cup V_j\cup C_{n-1}\bigr).                  \tag{1.4}
\]

Every displayed set has rank `r`.

For a transition `V_j -> V_(j+1)`, put

\[
 I_j=V_j\cap V_{j+1},\quad
 x_j=V_j-V_{j+1},\quad y_j=V_{j+1}-V_j.                           \tag{1.5}
\]

Both differences are singletons.  Two useful screens between the terminal
letter of `B_j` and the initial letter of `B_(j+1)` are

\[
\begin{aligned}
 S_j^\cap&=K\cup I_j\cup F,\\
 S_j^\cup&=K\cup(V_j\cup V_{j+1})
                 \cup(F-\{f_0,f_{n-1}\}).                       \tag{1.6}
\end{aligned}
\]

### Lemma 1.1 (both screens are literal Johnson bridges)

Both screens in (1.6) have rank `r` and are Johnson adjacent to

\[
                K\cup V_j\cup C_{n-1}
        \quad\hbox{and}\quad K\cup V_{j+1}\cup C_0.              \tag{1.7}
\]

#### Proof

The intersection screen has `|K|+2+n=r` elements.  Relative to the left
endpoint it removes `x_j` and inserts `f_(n-1)`; relative to the right it
removes `f_0` and inserts `y_j`.

The union screen has `|K|+4+(n-2)=r` elements.  Relative to the left endpoint
it removes `f_0` and inserts `y_j`; relative to the right it removes
`f_(n-1)` and inserts `x_j`.  Every comparison is one deletion and one
insertion.  \(\square\)

The original tensor uses `S_j^cap` at all eleven transitions and has length

\[
                           12n+11=12d+35.                          \tag{1.8}
\]

Its blocks are all distinct.  Its only repetitions are four screen values,
each occurring twice, so its owner duplicate excess is exactly four.

## 2. Cross-screen repair

Order the four repeated intersection-screen pairs by the first occurrence of
their common value.  A bit vector `eta in {0,1}^4` chooses, in each pair,
which occurrence of `S^cap` is replaced by `S^cup`.  Make the same bit-vector
choice in the old and new active words.

In zero-based transition indices, the three resulting fixed sets of
union-screen positions are respectively

\[
             \{1,3,5,7\},\qquad \{2,5,8,10\},\qquad
             \{3,4,7,10\}.                                      \tag{2.0}
\]

Thus the repair rule depends on neither the connector row nor `d`.

### Theorem 2.1 (zero-defect tensor macro)

For each of the three connector rows and every `d>=1`, every choice

\[
                         \eta\in\{0110,1011,1100\}                 \tag{2.1}
\]

has the following exact properties.

1. Both phases are length-`12d+35` rank-`r` Johnson paths with the same
   endpoints.
2. Every owner in either phase is distinct.
3. The old and new owner sets are equal.
4. Their ordered prefix and suffix OR chains agree pointwise.
5. Their sets of distinct internal interval OR values agree.
6. Every internal positive coordinate run has length at least `d+1`, and
   the leading/trailing positive-run lengths clipped at `d+1`, boundary bits,
   and whole-fragment flags agree between phases.

Hence the repaired tensor is simultaneously owner-transparent,
upper-transparent, and residence-neutral.

#### Proof

Item 1 follows from Lemma 1.1.  The remaining proof separates active and
filler coordinates.

The twelve active block labels are the same set in both phases.  For the
three patterns (2.1), equivalently the fixed transition sets (2.0), the
finite six-coordinate screen table has the same
set of labelled intersection/union screens in both phases, with no repeated
screen and no collision with a block.  The table is independent of `d` and
is exhaustively reproduced by the audit.  This proves items 2--3.

The filler word is positionwise identical in the two phases: block position
`t` carries `C_t`, an intersection screen carries `F`, and a union screen
carries `F-{f_0,f_(n-1)}`.  The selected screen-type vector is the same at
every macro position in both phases.  The finite active table also has equal
ordered prefix/suffix OR chains.  Repeating each block label exactly `n`
times only repeats the same plateaux, proving item 4.

For item 5, classify an interval by its filler union.  Two distinct coatoms
already unite to `F`.  Therefore a filler union smaller than `F` occurs only
in one of four forms:

* one block letter, with filler part `C_t`;
* one union screen, with filler part `F-{f_0,f_(n-1)}`;
* the last block letter followed by a union screen, with filler part
  `C_(n-1)`; or
* a union screen followed by the first next-block letter, with filler part
  `C_0`.

The block-owner set and union-screen active-label set agree by items 2--3,
so these four exceptional deck classes agree.  Every other interval has
filler union `F`; its active OR belongs to the finite full-filler interval
table, which is identical for the two active words for exactly the three
patterns in (2.1).  This proves equality of the distinct-value internal-deck
supports.  Interval multiplicities are neither asserted nor needed by the
compressed-deck replacement theorem.  Notice that this
case split is independent of the number of middle filler coordinates, so
the finite table proves every `n>=3`, not merely the audited sample.

Finally, one filler coordinate is absent once in each coatom block.  Between
successive absences its positive run has length at least `n-1=d+1`; a union
screen can remove `f_0` or `f_(n-1)` but lowers the connecting run only to
the same value `n-1`.  Every active coordinate present in a block occurs for
`n=d+2` consecutive positions, and a screen occurrence touches an adjacent
present block, so it creates no shorter isolated run.  The finite active
boundary table and the identical filler boundary word give the same clipped
boundary state.  This proves item 6.  \(\square\)

The proof is finite in the active coordinates and symbolic in `d`.  The
audit additionally checks all three rows and all three patterns directly for
`1<=d<=12`.

## 3. What happened to the four owner defects

The unrepaired tensor has four duplicate excess units.  Since its length is
fixed, these are also four missing distinct owner slots relative to an exact
owner transversal.  They are rank-`r` obligations.

An unused compiler cell belongs to the lower target--cell system.  Assigning
such a cell does not by itself create a missing rank-`r` owner.  Therefore:

### Proposition 3.1 (type separation)

The four raw repeated-screen defects cannot be discharged merely by choosing
four cells in the unused basis of a lower compiler matching.  Such a routing
is valid only after one supplies four literal bank-transparent **owner-repair
packets** whose output includes those owner targets and whose compiler effect
is the named cell deletion.

If these packets exist, they are four ordinary task vertices in the joint
unused-basis Hall graph.  Without them, the lower-cell matching and the owner
ledger are different resource types.

#### Proof

Every incidence of the lower compiler caps a proper-prefix physical interval
to a target below rank `r`; preserving or deleting an unused incidence does
not add a new rank-`r` row to the owner chronology.  The transparent-packet
composition theorem changes this only when the packet certificate explicitly
contains the owner repair.  \(\square\)

Theorem 2.1 is stronger: it supplies a local owner repair with no compiler
effect and no sidecar.  The four task vertices never arise.

## 4. Exact U5 integration

Fix a forced-core-contracted compiler bank `H=(L,C;E)`.  Let `rho*` be the
componentwise maximum of every residence frontier in the bounded reachable
macro state family.  Declare a cell *certified invariant* when all retained
target--cell incidences at that cell and all of their trace guards are
literally the same in both macro phases.  Let

\[
 D_{mac}=\{c\in C:c\text{ is not certified invariant under the macro}\}.
                                                                    \tag{4.1}
\]

If the packet explicitly deletes a zero-or-one additional cell `b`, include
it in `D_mac`.  This definition is literal: it includes every compiler
incidence changed by the internal phase switch, not merely cells at the four
screens.

### Theorem 4.1 (fixed-worst-frontier compiler criterion)

Assume that the retained bank outside `D_mac` is trace guarded for both
phases.  Then one matching `M_0` in that retained bank is an exact common
compiler for every repaired tensor phase and every reachable frontier if and
only if the restricted target--cell graph obeys

\[
 \boxed{
 \delta_H\bigl(D(\rho^*)\cup D_{mac}\bigr)
 =\max_{X\subseteq\mathcal L}
   \left(|X|-|N_H(X)\setminus(D(\rho^*)\cup D_{mac})|\right)=0.}  \tag{4.2}
\]

When (4.2) holds, Hopcroft--Karp constructs `M_0`; relative to any old
matching, the symmetric difference gives the exact disjoint alternating
paths which clear all used cells in the forbidden bank.

#### Proof

Theorem 2.1 makes the residence frontier common to both phases and removes
every owner sidecar.  By the certified-invariance hypothesis, every
incidence and guard outside `D_mac` is invariant.  The fixed-unused-basis
frontier theorem says that
one matching avoids every reachable prefix exactly when it avoids the
componentwise worst ideal, and its Hall deficiency is (4.2).  Trace guarding
then makes the unchanged matching a literal common cap in every phase.
The alternating-path statement is the prefix-clearing linkage theorem.
\(\square\)

### Corollary 4.2 (bounded exported compiler state)

If the left side of (4.2) is at most an absolute constant `c`, and the
regenerative terminal sidecar literally repairs any `c` omitted compiler
obligations, then the tensor contributes `O(1)` exported state.  The owner
contribution is zero; all exported obligations come from U5.

This is the sharpest conclusion currently justified.  Neither the tensor
audit nor scalar unused-cell surplus proves (4.2).  In particular,
`D_mac` can contain more than the four screen positions because changing an
owner chronology can change every short cell crossing the macro.

## 5. Consequence for the additive-constant route

The local macro side has improved materially:

\[
 \boxed{\text{four owner defects }\longrightarrow
        \text{three exact zero-defect screen patterns}.}          \tag{5.1}
\]

The remaining construction theorem is now purely the fixed-bank compiler
and abundance interface:

1. embed a positive-density/bounded reachable family of the repaired tensor
   macros on one subset-closed topology skeleton;
2. construct a trace-guarded bank invariant outside a declared `D_mac`;
3. prove (4.2), or a uniform absolute deficiency plus literal repair; and
4. regenerate the same bounded state.

No rank-`r` owner repair has to be carried across the induction.  This removes
one exact four-token state from the proposed recursion, but it does not by
itself prove `nu(k)<=B(k)+O(1)`.

## 6. Audit

Run

```bash
python3 scratch/audit_coatom_screen_tensor_compiler_20260801.py
```

It reads the authenticated six-seam connector catalogue and checks all three
positive connector rows, every `1<=d<=12`, and all sixteen choices of one
cross screen in each repeated pair.  In every row and depth, exactly the
three patterns in (0.1), at the fixed transition sets (2.0), simultaneously
have distinct/equal owner sets, equal signatures, equal distinct-value
internal OR decks, Johnson adjacency, legal internal runs, and equal clipped
boundary states.

The audit also retains the original full-screen tensor, whose duplicate
excess is exactly four in every row and depth.

This note proves the symbolic extension to every `d` by the filler-union
classification in Theorem 2.1.  The audit does not construct `H`, `D_mac`,
or a terminal compiler repair.
