# The Cartesian Boolean-hex fan cannot supply three private rolling-reset return corridors

Date: 2026-08-01

Status: exact projection and resource no-go, plus the sharp bounded-bank
positive remainder.  The result concerns private support-three corridors
built from the displayed Cartesian ternary-hex fan.  It does not rule out a
coupled multi-hex macro, a longer nonlocal corridor, or a different
owner-changing primitive.

## 0. Outcome

The quadratic Cartesian fan is a local rerouter over one oriented Johnson
atom.  It is not a universal three-return corridor matrix.

There are two successive structural zeros.

1. In its displayed orientation, the ternary hex fixes both outer incidence
   projections pointwise.  It changes only the physical tail--head matching.
   Hence it has zero head--owner attachment boundary and cannot realize the
   rolling reset's return of type `A`.
2. The two predecessor-parity returns have opposite orientations on the
   same adjacent endpoint roots.  Their target atoms share the unique lower
   colour `L=E intersect F` and upper colour `U=E union F`.  Every phase of
   every Cartesian-fan packet through either target uses `L` and `U`.
   Therefore two private target-centred hex corridors cannot coexist in one
   four-resource matching, regardless of the quadratic fan parameters.

Thus no bank of three private support-three Cartesian-hex corridors can
supply the reset signature

\[
                       \mathsf A+\mathsf P_0+\mathsf P_1.    \tag{0.1}
\]

This failure occurs before residence, arbitrary-width upper witnesses,
compiler hazards, or phase-common residual minors are considered.

There is a sharp positive remainder.  For any fixed bank of pairwise
resource-disjoint oriented seam atoms, one Cartesian fan corridor per atom
can be planted prospectively by the existing quadratic-versus-linear greedy
theorem.  What fails is promoting one such corridor to three independent
corridors at one reset.

## 1. The two frozen outer projections

Use the Boolean-hex notation

\[
\begin{array}{lll}
 o_1=(L_a,U_b,A,B),&o_2=(L_c,U_a,C,D),
     &e=(L_b,U_c,E,F),\\
 n_1=(L_a,U_c,A,F),&n_2=(L_c,U_b,C,B),
     &n_3=(L_b,U_a,E,D).
\end{array}                                                \tag{1.1}
\]

Put `O={o_1,o_2,e}` and `N={n_1,n_2,n_3}`.  For an ordered atom
`x=(L,U,T,H)`, define the three projections

\[
 \pi_-(x)=(L,T),\qquad
 \pi_0(x)=(T,H),\qquad
 \pi_+(x)=(H,U).                                      \tag{1.2}
\]

Here `pi_-` is the lower--tail incidence, `pi_0` is the physical or
predecessor tail--head edge, and `pi_+` is the head--owner attachment.

### Theorem 1.1 (outer-projection rigidity)

The displayed ternary switch satisfies

\[
 \begin{aligned}
  \pi_-(O)=\pi_-(N)
    &=\{(L_a,A),(L_c,C),(L_b,E)\},\\
  \pi_+(O)=\pi_+(N)
    &=\{(B,U_b),(D,U_a),(F,U_c)\}.
 \end{aligned}                                            \tag{1.3}
\]

Its only nontrivial projection is

\[
 \pi_0(O)=\{AB,CD,EF\},\qquad
 \pi_0(N)=\{AF,CB,ED\},                                \tag{1.4}
\]

whose union is the alternating physical `C6`.

#### Proof

Read the three pairs in each projection directly from (1.1).  In `pi_-`,
each lower colour retains its tail.  In `pi_+`, each head retains its upper
owner; only the order of the three displayed atoms changes.  Formula (1.4)
is the ordinary ternary-hex identity. \(\square\)

### Corollary 1.2 (attachment structural zero)

Any disjoint union of displayed-orientation Cartesian hex switches has
zero boundary in the head--owner attachment matching.  It cannot close the
nonzero attachment path exported by an opened bidirectional reset.

This is stronger than a shortage of fan entries: all `(m-1)^2` entries in
the fan of one target have the same zero attachment current.

Reversing every directed atom removes this particular zero by exchanging
the typed tail and head roles.  The next obstruction applies even when such
reversed hexes are admitted.

## 2. The opposite parity targets share their outer colours

Let the opened reset have adjacent endpoint roots

\[
                         E=T_0,\qquad F=T_{N-1}.             \tag{2.1}
\]

Because they are a Johnson pair, their outer colours are uniquely

\[
                         L=E\cap F,\qquad U=E\cup F.         \tag{2.2}
\]

The two direct predecessor orientations are the atoms

\[
 e^\rightarrow=(L,U,E,F),\qquad
 e^\leftarrow=(L,U,F,E).                                  \tag{2.3}
\]

They are the two typed orientations of one physical edge.

### Lemma 2.1 (endpoint uniqueness for a one-hex ear)

Let a ternary-hex cycle be opened by deleting one old atom, and suppose the
resulting five-edge alternating physical ear has endpoints `E,F`.  Then the
deleted target atom is one of (2.3), and its lower and upper resources are
the sets in (2.2).

#### Proof

Opening the alternating `C6` at one edge makes the endpoints exactly the
tail and head of the deleted atom.  A legal ordered Boolean diamond on the
adjacent middle sets `E,F` has intersection `E intersect F` and union
`E union F`, which are unique. \(\square\)

### Theorem 2.2 (two-parity private-fan no-go)

No two private ternary-hex corridors, one centred on
\(e^\rightarrow\) and one centred on \(e^\leftarrow\), can coexist in a
four-resource matching.

#### Proof

For a target atom `e`, both full packet phases `O` and `N` use exactly the
four typed target resources of `e`, together with eight non-target
resources.  Hence every phase of every fan option through
\(e^\rightarrow\) uses the lower resource `L` and upper resource `U`.  The
same is true through \(e^\leftarrow\).  Lower and upper resources have
capacity one, so the two packet
states conflict on both shores.  The fan parameters `(b,c)` change only
the eight non-target resources and cannot remove this collision.
\(\square\)

### Corollary 2.3 (three private corridors are impossible)

At most one of the two parity returns can be represented by a private
target-centred one-hex ear.  Together with Corollary 1.2, the displayed
Cartesian fan cannot furnish the three-return reset signature (0.1).

The conclusion persists if one corridor uses a reversed-orientation hex:
reversal swaps the typed tail/head copies, but it does not change the common
lower and upper resources `L,U`.

## 3. What the quadratic fan does prove

Let

\[
                  e_1,\ldots,e_H                            \tag{3.1}
\]

be a fixed collection of pairwise four-resource-disjoint oriented target
atoms, with `H` fixed.  The Cartesian fan of each target has `(m-1)^2`
options, and any fixed non-target typed resource occurs in at most `m-1`
options.

### Theorem 3.1 (one private corridor per reset target)

If

\[
                            m-1>16(H-1),                     \tag{3.2}
\]

one may choose one Cartesian-hex option per `e_i` so that their complete
twelve-resource supports are pairwise disjoint.  In either cycle phase,
the union is a four-resource matching, and switching any subset preserves
the complete four-resource signature.

#### Proof

This is the bounded prospective-bank theorem for the Cartesian fan.  Each
previous target tuple and each previous selected support excludes at most a
linear number of the quadratic options, and (3.2) leaves an option at every
greedy step.  Resource equality of the two packet phases makes every subset
switch exact. \(\square\)

Thus fixed-bank planting is not the issue.  The reset's three demands fail
the theorem's first hypothesis: their target tuples are not pairwise
resource-disjoint, and the attachment demand is not represented by a
displayed-orientation fan current at all.

## 4. Later obstructions, after the central no-go

Even one central support-three packet has further OR-word gates.

1. At depth three, every forward-oriented native flag lift has the same
   first deletion coordinate on its three tails.  Two simple reset rings
   can host at most two of these flags, so three rings are necessary.
2. The known two-ring root embedding changes an arbitrary-width upper
   target in a private boundary context.  Four-resource, suffix and rail
   neutrality do not imply exterior OR transparency.
3. A shortest resident return rail exists and is internally upper-explicit,
   but its old and new phases have different clipped boundary-run records
   and different socket pairings.  It is not a strong unary
   bi-contractible slot without a joint interface.

These facts are not used in Theorem 2.2.  They show that overcoming the
outer-resource collision would still not finish the protected host.

## 5. Exact escape target

The next construction cannot be a direct sum of three private
target-centred Cartesian fans.  It must contain at least one of the
following genuinely new features.

1. An owner-changing primitive with nonzero `pi_+` boundary.
2. A coupled macro in which both parity returns share the unique `L,U`
   target resources internally rather than claiming two private copies.
3. A longer nonlocal typed corridor whose endpoint current is assembled
   from several gain/loss ears and whose intermediate outer currents cancel.
4. A support-six opposite-current pair with one joint phase-common
   component quotient and one joint compiler relocation certificate.

The cleanest theorem target is therefore:

> **Coupled rolling-reset return macro.**  Construct one occurrence-labelled
> two-phase packet, not three private packets, whose projected symmetric
> difference is exactly one head--owner return and the two signed
> predecessor returns, whose total lower/upper resources are simple, and
> whose two contracted residual hosts coincide.

The quadratic fan can supply local rerouting choices inside such a macro,
but it cannot supply its boundary algebra by itself.
