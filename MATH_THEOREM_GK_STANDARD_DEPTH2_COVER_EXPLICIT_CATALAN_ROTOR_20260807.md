# An explicit Catalan rotor gives the optimal standard GK depth-two cover

**Date:** 2026-08-07  
**Status:** unconditional all-parameter **abstract root-selector** theorem.
It proves the formerly open nonsink-to-nonprimitive Hall statement by an
explicit bijection.  It does not prove that consecutive selected root
hinges fuse to one alternating physical factor: cancellation of their
shared fixed edge leaves a `00` phase pair.  A phase-repair/higher-circuit
lemma and the protected upper/compiler tickets remain open.

## 1. The Catalan rotor

Write `D_j` for the Dyck words of semilength `j`.  Define a map

\[
                         \theta:{\cal D}_j\longrightarrow{\cal D}_j
                                                               \tag{1.1}
\]

as follows.  Put `theta(empty)=empty`.  If `E` is nonempty, use its
first-return decomposition

\[
                         E=1A0N,                       \tag{1.2}
\]

where `A,N` are Dyck words, and set

\[
                         \theta(E)=A1N0.               \tag{1.3}
\]

## Lemma 1.1

`theta` is a bijection of `D_j`.  Its inverse is obtained by writing a
nonempty word uniquely as

\[
                         E'=A1N0,                      \tag{1.4}
\]

where `1N0` is the last primitive component, and putting

\[
                         \theta^{-1}(E')=1A0N.         \tag{1.5}
\]

### Proof

In (1.2), `A` and `N` are Dyck, so `A1N0` is Dyck.  Conversely every
nonempty Dyck word has a unique last primitive component `1N0`; the
preceding word `A` is Dyck.  Equations (1.3) and (1.5) are visibly inverse.
\(\square\)

This elementary rotor is the only auxiliary bijection needed below.

## 2. Canonical decomposition of a nonsink root

Fix `m>=2`.  A depth-two nonsink is a Dyck word whose first primitive has
semilength at least two.  It has a unique decomposition

\[
                         U=1PC0B,                      \tag{2.1}
\]

where

* `P,B` are Dyck words;
* `C` is the last primitive component of the nonempty interior of the
  first primitive of `U`.

Write

\[
                         C=1E0.                        \tag{2.2}
\]

Define

\[
             \Phi(U)=(1P0)\,(1\theta(E)0)\,B.          \tag{2.3}
\]

The displayed first two factors are primitive, so `Phi(U)` is
nonprimitive.

## 3. Every rotor edge is one legal depth-two flip

## Lemma 3.1

For every nonsink `U`, the pair

\[
                         U\longrightarrow\Phi(U)       \tag{3.1}
\]

is a legal arc of the standard depth-two orientation.

### Proof

If `E` is empty, then `C=10`.  Choose for `b` the opener of this final
interior primitive and for `x` its closing downstep.  In the local word

\[
                         1P\,10\,0B
\]

the flip changes the displayed `10` to `01`, giving

\[
                         (1P0)\,10\,B,
\]

which is (2.3).

Now let `E` be nonempty and write its first-return decomposition as

\[
                         E=1A0N.                       \tag{3.2}
\]

Then

\[
                         U=1P\,1\,1A0N0\,0B.           \tag{3.3}
\]

Choose `b` to be the first displayed opener of `C`, and choose `x` to be
the displayed downstep closing the first primitive `1A0` of `E`.  The
opener `b` goes from height one to height two and `x` lies in its
excursion.  Changing `b` down and `x` up gives

\[
 \begin{aligned}
             1P\,0\,1A1N0\,0B
              &=(1P0)\,(1(A1N0)0)\,B\\
              &=(1P0)\,(1\theta(E)0)\,B.
 \end{aligned}                                        \tag{3.4}
\]

This is exactly `Phi(U)`.  Thus (3.1) is a legal depth-two arc in both
cases. \(\square\)

## 4. Exact perfect matching

## Theorem 4.1 (standard-cover matching)

The map `Phi` is a bijection

\[
 \boxed{
 \{\text{nonsink roots in }{\cal D}_m\}
 \longleftrightarrow
 \{\text{nonprimitive roots in }{\cal D}_m\}
 }
                                                               \tag{4.1}
\]

and every matched pair is a standard depth-two arc.  Consequently the
standard nonsink-to-nonprimitive bipartite graph has a perfect matching
for every `m>=2`.

### Proof

Only bijectivity remains after Lemma 3.1.  Let `V` be nonprimitive.  Split
off its first primitive and then the first primitive of the remaining
nonempty suffix.  This gives a unique decomposition

\[
                         V=(1P0)(1E'0)B,               \tag{4.2}
\]

with `P,E',B` Dyck.  Put

\[
                         E=\theta^{-1}(E'),\qquad
                         C=1E0,
\]

and reconstruct

\[
                         U=1PC0B.                      \tag{4.3}
\]

Its first primitive has nonempty interior `PC`, whose last primitive is
exactly `C`, so `U` is a nonsink and its canonical decomposition is
(4.3).  Equation (2.3) gives `Phi(U)=V`.  Every step of the reconstruction
is unique, proving bijectivity. \(\square\)

## 5. Optimal directed path cover

Select the arcs `U -> Phi(U)` for all nonsink roots.  Every nonsink has
selected outdegree one, and Theorem 4.1 gives every nonprimitive root
selected indegree one.  The depth-two orientation is acyclic, so the
selected graph is a spanning directed path cover.

Its starts are exactly the primitive roots and its ends are exactly the
sink roots `10A`.  Both banks have size `Cat_{m-1}`.  Therefore:

## Corollary 5.1

For every `m>=2`, the standard depth-two orientation has a spanning path
cover with exactly

\[
                         \boxed{\operatorname{Cat}_{m-1}}              \tag{5.1}
\]

components.  This is optimal because every directed path must end at one
of the `Cat_{m-1}` sinks.

## 6. Resource injectivity and the remaining phase gate

Each source uses only one socket `(U,b)`, and the targets `Phi(U)` are
distinct.  The global socket-colour theorem therefore makes the hinge
colours `a(U,b)` and `B_y(U,b)` private, while the target facets
`B_x=X_{Phi(U)}` are private as well.  Thus there is no residual ordinary
Hall or lower-colour collision in the standard bank.

This is an abstract path cover, not yet a literal alternating factor.
When two selected root circuits meet at an internal root, their common
fixed edge cancels and the two surviving cross edges both have status
zero.  Hence the bare symmetric difference is nonalternating; serially
toggling the two circuits fails for the same reason.  The correction is
recorded in
`MATH_CORRECTION_GK_ROOT_PATH_C6_SYMMETRIC_DIFFERENCE_NONALTERNATING_20260807.md`.

The theorem closes the **ordinary optimal-cover Hall** hypothesis.  It
does not close the later physical rows:

1. a phase-repair or higher alternating circuit must lift the selected
   root paths to a literal degree-two factor;
2. any escape/helper packet must be planted without making degree three;
   and
3. the resulting physical factor must coexist with the protected
   residence, arbitrary-upper and terminal-compiler tickets.

The former open base Hall theorem is therefore no longer part of the
all-dimensional frontier.
