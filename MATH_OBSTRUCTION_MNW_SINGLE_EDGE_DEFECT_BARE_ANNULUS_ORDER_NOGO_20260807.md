# The MNW one-edge boundary defect cannot be absorbed by the bare annulus

**Date:** 2026-08-07  
**Method:** exact fused-cycle ledger and alternating-face order; no
computation or search  
**Status:** unconditional no-go for the unaugmented `01 -> 10` carry of the
first fused B8 cycle.  It does not rule out an augmented module containing
a destination-boundary switch or another phase-creating circuit.

## 1. The first two B8 hexagons fuse to one alternating `C_8`

Use the base owners

\[
\begin{aligned}
 O_a&=10001101,& O_b&=10001011,& O_c&=11001001,\\
 O_2&=10000111,& O_3&=11000011,
\end{aligned}
\]

and colours

\[
 A=10001111,quad B=11001011,quad
 C=11001101,quad D=11000111.
\]

The first B8 hexagon is

\[
 O_a-A-O_b-B-O_c-C-O_a,
\]

and the second is

\[
 O_b-A-O_2-D-O_3-B-O_b.
\]

They share the two-edge path `A-O_b-B`.  Their sequential symmetric
difference is the simple cycle

\[
 \boxed{
 C_{01}=O_a-A-O_2-D-O_3-B-O_c-C-O_a.}
\tag{1.1}
\]

In the canonical source factor its edge-status word, starting with
`O_aA`, is

\[
                         10101010.                 \tag{1.2}
\]

Thus `C_{01}` is literally alternating.  Toggling it has the same net
incidence current as applying B8 hexagons `H_0,H_1` in order.

## 2. The gamma--alpha state has exactly one boundary discrepancy

Put the cycle in source context `01` and destination context `10`.  The
one-prefix boundary audit proves:

1. the complete source copy is canonical;
2. at the destination owner `10 O_c`, mirror gamma has exactly the
   required cycle phase;
3. at `10 O_a`, the required selected incidence `10 O_a--10 A` is absent,
   while the other cycle incidence `10 O_a--10 C` has its required
   unselected status; and
4. no other edge of (1.1) has a boundary-phase defect.

Consequently the source and destination copies have identical statuses on
the seven edges other than

\[
                         e_*=O_aA,                  \tag{2.1}
\]

and opposite statuses on `e_*`.

The leaf endpoint-transfer hexagon is exactly the transport face
`H_(e_*)`.  In ten-bit notation its three boundary/rail owners are

\[
 01O_a=0110001101,qquad
 10O_a=1010001101,qquad
 00A=0010001111,
\]

and its three colours are

\[
 01A=0110001111,qquad
 10A=1010001111,qquad
 11O_a=1110001101.
\]

The exact status audit proves that this face is alternating in the
gamma--alpha factor.

## 3. A transport face needs opposite boundary statuses

For any edge `e=OQ` of a base incidence cycle, its one-step transport face
has cyclic order

\[
 01O-01Q-00Q-10Q-10O-11O-01O.                    \tag{3.1}
\]

The two boundary incidences `01O--01Q` and `10O--10Q` occur three edges
apart.  Hence they must have opposite statuses in every alternating
realization of (3.1).  In particular, no choice of the four rail phases
can make the face alternating when its two boundary incidences have equal
status.

Therefore, in the state of Section 2, `H_(e_*)` is the only transport face
of (1.1) that can possibly be alternating.

## Theorem 3.1 (singleton-defect bare-annulus no-go)

Starting from the exact gamma--alpha boundary state, there is no ordering
which toggles

\[
 C_{01}quad\text{and every transport face }H_e
 \quad(e\in E(C_{01}))                              \tag{3.2}
\]

exactly once, with every toggled cycle alternating at the moment it is
used.

### Proof

Before the first relevant move, only two members of (3.2) can be
alternating: the source cycle `C_{01}` and the exceptional transport face
`H_(e_*)`.

* If `H_(e_*)` is used first, it flips the source incidence on `e_*` and
  no other source-cycle edge.  The source cycle then differs from the
  alternating word (1.2) in exactly one position, so it is not alternating.
  Every other transport face still has equal boundary statuses, because
  `H_(e_*)` touches no other boundary incidence.  Hence no unused member of
  (3.2) is available.

* If `C_{01}` is used first, it flips every source boundary incidence.
  The two copies of `e_*`, which were opposite, become equal.  Toggling
  transport faces attached to other edges never changes either copy of
  `e_*`.  Consequently `H_(e_*)` can never become alternating during the
  remainder of a sequence that uses only the still-unused members of
  (3.2).

Both possible first moves prevent completion.  \(\square\)

The proof uses only the boundary entries of the faces.  It is independent
of how the auxiliary rail incidences are chosen and therefore cannot be
repaired by a different complementary rail phase.

## 4. Exact consequence for the finite ordered-two-SDR target

The standard carry of one simple cycle is the source switch plus all its
transport faces.  Theorem 3.1 proves that the first fused B8 cycle cannot
be carried in that bare form from the inherited gamma--alpha state.

Accordingly, an occurrence-labelled static pattern consisting only of

\[
 \text{the inherited gamma--alpha phase}
 +\text{the B8 source faces}
 +\text{their bare transport faces}                 \tag{4.1}
\]

has no legal alternating face order.  No ordered two-SDR can certify a
face order that does not exist.

This sharpens the finite-module statement: a valid ten-prefix-bit module
must contain at least one additional phase-changing operation affecting
the defective fused cycle.  Three possible augmentations remain:

1. toggle an appropriate destination-boundary cycle and compensate its
   extra current later;
2. add a circuit which changes one further source or destination boundary
   incidence, converting the singleton discrepancy into a sweepable phase;
3. replace the bare annulus by a genuinely two-phase ordered-SDR module in
   which the source and destination cycles live in different factor
   phases.

The direct positive-H0 route is an example of the first option.  Its later
q2 casualties show that the compensation must be chosen jointly rather
than appended from the currently known local repairs.

## 5. Scope

This theorem does not disprove the finite connector-faithful module.  It
disproves only the unaugmented module implicit in the phrase “interleave
the leaf face with the standard source-plus-annulus sweep.”  The exact
remaining finite object is now:

> an **augmented two-phase ordered two-SDR** containing the gamma--alpha
> boundary, one additional phase creator for the fused `H_0/H_1` cycle,
> the B8 transport bank, and the inherited connector/socket marks.

Before a positive module claim, that extra phase creator must be included
explicitly in the occurrence-labelled `P_0,P_1,N,omega` ledger.

