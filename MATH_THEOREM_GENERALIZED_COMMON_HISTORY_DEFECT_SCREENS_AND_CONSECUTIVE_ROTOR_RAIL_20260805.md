# Generalized common-history defect screens and a consecutive rotor rail

**Date:** 2026-08-05  
**Method:** literal sliding-window algebra and a reverse-order source-splice
argument; no computation or search  
**Status:** unconditional local/source theorem.  Redundant core coordinates
in the two screens remove the scalar obstruction to decorating a long run of
consecutive clean C6 edges.  An explicit `(d+1)`-age-class rotor realizes
every local packet simultaneously and supports a reverse-order serial
lower-deck proof.  Embedding this rotor corridor in the actual PBBS sibling
rail, and protecting arbitrary upper targets/common-cap routes, remain open.

## 1. A generalized clean-C6 history

Use the clean-C6 normal form

\[
 P_i=K+a_i+a_{i+1},\qquad Q_i=K+a_i+c,             \tag{1.1}
\]

where `|K|=r-2` and `a_0,a_1,a_2,c` are distinct outside `K`.

Choose any defect set

\[
                         D\subseteq K,
 \qquad H=K\setminus D,                            \tag{1.2}
\]

and any nonempty source letters `C_1,...,C_d` with

\[
                         \bigcup_{s=1}^d C_s=H.     \tag{1.3}
\]

They need not be disjoint.  Put

\[
 X_i=D\cup\{c,a_i\},\qquad
 Y_i=D\cup\{a_{i-1},a_i\}.                        \tag{1.4}
\]

The fragment `(X_i,C_1,...,C_d,Y_i)` has owner pair

\[
 Q_i=H\cup D\cup\{c,a_i\},
 \qquad
 P_{i-1}=H\cup D\cup\{a_{i-1},a_i\}.             \tag{1.5}
\]

Replacing `Y_i` by `Y_(i+1)` changes the second owner to `P_i`, exactly as
in the minimal ring.

### Theorem 1.1 (defect-screen transparency)

The generalized head rethread preserves:

1. the owner multiset and both immediate palettes;
2. the complete occurrence-labelled strict-lower interval-OR deck;
3. every lower derivative row through depth `d`; and
4. every occurrence-labelled strict-lower compiler matching.

It has zero source-length charge and positive cyclic residence at least
`d+1`.

#### Proof

The owner identities are (1.5).  The two screens share `D` in every role,
and the history union is `H`, so their owner/palette set algebra is the same
as after replacing `D union H` by `K`.

An interval meeting both screens contains `D`, every `C_s`, and the left
active pair.  Hence it contains

\[
 D\cup H\cup\{c,a_i\}=Q_i,
\]

a rank-`r` owner.  Every strict-lower interval is therefore one-sided.  The
left side is fixed, the complete right screen/context pair is permuted, and
the common history is literal.  This gives the same occurrence bijection as
the minimal theorem.  Compiler transport follows by moving its selected
cells through that bijection.  Finally every source occurrence belongs to
`d+1` cyclic owner windows, and the source-letter multiset is merely
permuted.  \(\square\)

The PBBS common-deletion coordinate used for selected q2 neutrality is
independent of the defect-screen choice.

## 2. Exact colored sliding equations

Consider a source rail `(A_t)` and a consecutive family of desired clean
edge roles indexed by `t`.  At role `t`, let

\[
 K_t,quad D_t\subseteq K_t,quad
 \ell_t=\{u_t,v_t\},\quad r_t=\{u_t,w_t\}          \tag{2.1}
\]

be respectively the clean core, defect, left active pair, and right active
pair.  The active pairs share `u_t`, and their other labels are distinct and
outside `K_t`.

### Theorem 2.1 (necessary and sufficient rail equations)

The distinguished roles have simultaneous generalized histories in one
depth-`d` source rail if and only if

\[
 A_t=D_t\cup\ell_t,                                \tag{2.2}
\]

\[
 A_{t+d+1}=D_t\cup r_t,                            \tag{2.3}
\]

and

\[
 \bigcup_{s=1}^{d}A_{t+s}=K_t\setminus D_t         \tag{2.4}
\]

for every indexed role `t`.

Equivalently, successive roles must satisfy the screen-consistency equation

\[
 D_t\cup\ell_t=D_{t-d-1}\cup r_{t-d-1}            \tag{2.5}
\]

whenever both sides are indexed, together with (2.4).

#### Proof

Equations (2.2)--(2.4) are exactly the left screen, right screen, and common
history required by Theorem 1.1, so they are necessary.  Conversely, copy
the history word `(A_(t+1),...,A_(t+d))` into the other two clean-C6 roles
and use their corresponding defect screens.  Equations (2.2)--(2.4) invoke
Theorem 1.1 at every role.  Equation (2.5) is simply (2.2) at time `t`
compared with (2.3) at time `t-d-1`.  \(\square\)

This is the exact nonminimal escape from the two-set screen obstruction.  It
is a colored sliding-window/payload problem, not an aggregate capacity
inequality.

## 3. An explicit periodic age-class solution

Choose pairwise disjoint nonempty sets

\[
                         G_0,G_1,\ldots,G_d,         \tag{3.1}
\]

and a distinguished coordinate `g_p in G_p` for each phase.  Put

\[
                         G=\bigcup_{p=0}^{d}G_p.     \tag{3.2}
\]

Let `(x_t)` be a label stream disjoint from `G` such that every `d+2`
consecutive labels are distinct.  Define

\[
 p(t)=t\pmod{d+1},
 \qquad
 A_t=G_{p(t)}\cup\{x_t\}.                         \tag{3.3}
\]

Its depth-`d` owner row is

\[
 T_t=G\cup\{x_t,x_{t+1},\ldots,x_{t+d}\}.         \tag{3.4}
\]

Set

\[
                         r=|G|+d+1.                \tag{3.5}
\]

Then the `T_t` are rank-`r` owners and

\[
 T_{t+1}=T_t-\{x_t\}+\{x_{t+d+1}\}.              \tag{3.6}
\]

For edge `t`, put `p=p(t)` and define

\[
 D_t=G_p\setminus\{g_p\},                         \tag{3.7}
\]

\[
 K_t=(G\setminus\{g_p\})
       \cup\{x_{t+1},\ldots,x_{t+d}\},            \tag{3.8}
\]

\[
 \ell_t=\{g_p,x_t\},
 \qquad r_t=\{g_p,x_{t+d+1}\}.                   \tag{3.9}
\]

### Theorem 3.1 (rotating-defect rotor)

Equations (2.2)--(2.4) hold for every `t`.  Hence every consecutive edge of
the rotor rail admits a simultaneous generalized clean-C6 history.

#### Proof

Equations (2.2) and (2.3) follow immediately from
`p(t+d+1)=p(t)`.  The intervening phases `p(t+1),...,p(t+d)` are exactly
all phases other than `p(t)`.  Thus

\[
\begin{aligned}
 \bigcup_{s=1}^{d}A_{t+s}
 &= (G\setminus G_p)
    \cup\{x_{t+1},\ldots,x_{t+d}\}\\
 &=K_t\setminus D_t.
\end{aligned}                                      \tag{3.10}
\]

Also

\[
 |K_t|=(|G|-1)+d=r-2,
\]

so it is exactly a clean-C6 core.  \(\square\)

To complete a literal clean C6 around the distinguished rotor edge, choose
one additional active label outside `K_t union ell_t union r_t`; the other
two roles then use the same history and defect.  This is the only extra
local ground-set requirement.

### Corollary 3.2 (residence interpretation)

Every `G` coordinate is present in every owner.  A clock coordinate `x_t`
has an owner run of exactly `d+1` along the displayed corridor.  Thus the
rotor is the canonical `(d+1)`-age-class solution: defects are the phase
blocks carried by the two screens, and the other `d` phase blocks form the
history.

## 4. Reverse-order composition on one sibling rail

The local histories overlap, so simultaneous planting is not by itself a
composition proof.  The following order resolves that issue.

Consider packets indexed `t=0,...,E-1` on one common child source path.
Assume:

1. packet `t` uses the literal common-child fragment
   `(A_t,...,A_(t+d+1))`;
2. in the chosen orientation, its source rethread changes only the complete
   right screen/context beginning at `A_(t+d+1)` and fixes the prefix through
   `A_(t+d)`;
3. its other two clean-C6 role supports do not meet those of another packet,
   apart from the already authenticated directed q2 halo overlaps; and
4. every packet is q2-neutral in isolation.

### Theorem 4.1 (descending serial lift)

Apply the packets in the order

\[
                         E-1,E-2,\ldots,0.          \tag{4.1}
\]

Then every packet is still literally available when used.  The final move
preserves the complete strict-lower occurrence deck, every lower derivative
row, and every transported strict-lower compiler matching.  Together with
the directed-halo theorem, q1 and q2 are exact as well.

#### Proof

Before packet `t` is applied, only packets `u>t` have acted.  Their changed
right boundaries begin at positions

\[
                         A_{u+d+1},qquad u+d+1\ge t+d+2.
\]

Hence the entire fragment `A_t,...,A_(t+d+1)` remains literal.  Changes to
its later right context are harmless because Theorem 1.1 permits arbitrary
contexts and moves the complete current right pair.  The other role supports
are private by item 3.  Thus packet `t` is legal.

Each step has a strict-lower occurrence bijection, so composing those
bijections gives exact final lower transport.  The q1/q2 statement is the
directed-halo telescoping theorem under items 3--4.  \(\square\)

For a cyclic sibling contour, choose a cut outside the packet run or provide
the usual endpoint collar; no wraparound claim is implicit.

## 5. Exact PBBS corridor gate

The rotor theorem does not say that an arbitrary PBBS factor rail has form
(3.4).  It identifies the exact sufficient physical pattern:

> a fixed core `G` of size `r-d-1`, together with a clock stream whose
> successive noncore coordinates have lifetime exactly `d+1` and whose
> consecutive `(d+1)`-sets give the owner rail.

Equivalently, along the corridor the deletion at transition `t` must be
`x_t` and the insertion must be `x_(t+d+1)`.  This is a fixed-core,
minimum-lifetime rotor corridor.

The open PBBS statement is now concrete: choose the rotations/ports of each
cool-lex sibling family so that its common-child owner segment is such a
corridor (or prove a more general solution of (2.2)--(2.5)).

## 6. Scope

Proved:

1. the generalized defect-screen local packet;
2. exact necessary/sufficient colored sliding equations;
3. one periodic solution avoiding the `r-2<=2d` obstruction;
4. positive residence and a literal long consecutive pre-switch rail; and
5. exact descending serial lower/q1/q2 composition under the stated support
   orientation.

Not proved:

1. existence of the rotor corridor in every required PBBS sibling family;
2. simultaneous packing of the other two roles throughout the global tree;
3. arbitrary-width upper protection for the whole rail;
4. zero-gap residence or endpoint closure;
5. a typed/shared common-cap router; or
6. `nu(k)=B(k)+O(1)`.
