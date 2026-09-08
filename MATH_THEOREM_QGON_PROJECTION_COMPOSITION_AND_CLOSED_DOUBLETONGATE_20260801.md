# The Boolean q-gon has the reset permutation algebra, but naive same-port composition is a closed doubleton

Date: 2026-08-01

Status: exact all-`q` resource, projection and topology audit; exact
orientation correction; and exact literal same-port obstruction.  The
abstract reflected reverse followed by the forward q-gon has the opened
reset signature `(sigma,sigma^2)`.  Its naive literal realization selects
opposite orientations of the same intermediate edges and repeats their
owners.  An intervening role-conversion packet or disjoint-copy connector
is still required.

## 1. Boolean q-gon

Let `q>=3`, let `S` have rank `m-2`, and choose distinct labels

\[
                       z,a_0,\ldots,a_{q-1}\notin S.
\]

Read indices modulo `q` and put

\[
\begin{aligned}
 L_i&=S+a_i, &U_i&=S+z+a_i+a_{i+1},\\
 A_i&=S+z+a_i, &B_i&=S+a_i+a_{i+1}.
\end{aligned}                                             \tag{1.1}
\]

Define

\[
 O_i=(L_i,U_i,A_i,B_i),\qquad
 N_i=(L_i,U_{i-1},A_i,B_{i-1}).                           \tag{1.2}
\]

Exactly as in the quaternary octagon,

\[
 A_i\cap B_i=L_i,\quad A_i\cup B_i=U_i,
\]

and

\[
 A_i\cap B_{i-1}=L_i,\quad A_i\cup B_{i-1}=U_{i-1}.      \tag{1.3}
\]

Thus `O={O_i}` and `N={N_i}` have the same complete lower, upper,
tail and head resource sets.  Their physical projections are

\[
             O:A_i\to B_i,\qquad N:A_i\to B_{i-1}.         \tag{1.4}
\]

The required coordinate supply is `|S|+q+1=m+q-1`; on a `2m`-point
ground this displayed family exists for `q<=m+1`.

## 2. Exact projection permutations

Use the head-column convention: the attachment permutation records which
owner is assigned to each head, and the predecessor permutation records
which tail is assigned to each head.  Put

\[
                         \sigma(i)=i+1\pmod q.               \tag{2.1}
\]

For the forward toggle (1.4), head `B_i` retains owner `U_i`, while its
tail changes from `A_i` to `A_(i+1)`.  Therefore

\[
                         F=(\alpha_F,\pi_F)=(1,\sigma).      \tag{2.2}
\]

Literally reverse the same atoms.  The old and new edges are

\[
              B_i\to A_i,\qquad B_{i-1}\to A_i.             \tag{2.3}
\]

At head `A_i`, both its owner and its predecessor tail change from index
`i` to index `i-1`.  Hence the literal reverse is

\[
                         R=(\sigma^{-1},\sigma^{-1}),        \tag{2.4}
\]

not `(sigma,sigma)` under the same indexing.

Let `kappa(i)=-i`.  Since

\[
                  \kappa\sigma^{-1}\kappa^{-1}=\sigma,
\]

reflecting the reverse block's port labels gives the abstract action

\[
                         R^{\rm ref}=(\sigma,\sigma).        \tag{2.5}
\]

Consequently, at the level of port permutations alone,

\[
             R^{\rm ref}\ hbox{ followed by }F
                    =(\sigma,\sigma^2).                     \tag{2.6}

This is exactly the closed rolling-reset signature: the head--owner
attachment shifts by one, while the predecessor assignment shifts by two.

## 3. Literal same-port obstruction

Equation (2.6) is not yet a physical two-switch history.  Implement the
reflection by taking the forward block labels

\[
                       a_i^F=a_{-i}^R.                       \tag{3.1}
\]

Then

\[
 A_i^F=A_{-i}^R,qquad
 B_i^F=B_{-i-1}^R,qquad
 U_i^F=U_{-i-1}^R.                                         \tag{3.2}
\]

The old forward edge is therefore

\[
 A_i^F\to B_i^F=A_{-i}^R\to B_{-i-1}^R,                   \tag{3.3}
\]

whereas the terminal new edge of the reverse block on the same two roots is

\[
 B_{-i-1}^R\to A_{-i}^R.                                  \tag{3.4}
\]

Both have owner `U_i^F=U^R_(-i-1)`.

### Theorem 3.1 (closed-doubleton gate)

The reflected same-port realization of (2.6) is not a literal serial
composition inside one owner-injective factor.  At every intermediate port
it identifies the forward block's required old atom with the **opposite
orientation** of the reverse block's selected new atom.  Selecting both
creates a directed two-cycle and repeats its unique owner; selecting only
the reverse atom does not provide the old state required to apply the
forward toggle.

Thus (2.6) is a correct endpoint-permutation identity but not, without an
additional lift, a legal Boolean switch composition.

The obstruction can be evaded only by at least one of:

1. an intervening owner-changing role-conversion packet;
2. disjoint physical copies joined by an external same-port connector with
   separately balanced owner/lower resources; or
3. a larger atomic circuit in which the opposite intermediate orientations
   are overwritten rather than simultaneously selected and whose literal
   reachability is proved.

## 4. Exact q-cycle fusion

Assume the `q` old edges `A_i->B_i` lie on `q` distinct directed cycles.
Deleting them leaves directed fragments

\[
                         B_i\leadsto A_i.                    \tag{4.1}
\]

The new edges concatenate them as

\[
 B_0\leadsto A_0\to B_{-1}\leadsto A_{-1}\to
 B_{-2}\leadsto\cdots\to B_0.                             \tag{4.2}
\]

Since `i -> i-1` is one q-cycle, all `q` fragments form one directed
cycle.  Hence the toggle performs

\[
                              q\longmapsto1,
\]

reducing the cycle count by exactly `q-1`, while preserving all four
resource palettes.  This topology theorem is correct for every `q>=3`.

As with the ternary fusion theorem, it is conditional on literal packet
supply with the old edges on distinct components.  It does not remove the
same-port wiring obstruction in Section 3.

## 5. Reset verdict

The q-gon identifies the right abstract algebra:

\[
          (1,\sigma)\cdot(\sigma,\sigma)
                       =(\sigma,\sigma^2).
\]

But the reflected reverse and forward blocks meet on closed doubletons.
Therefore the next construction target is not another permutation
calculation.  It is a literal role-conversion splice which carries the
same port index through the reflection while changing the owner occurrence,
and which preserves suffix rows, arbitrary-width OR current, residence and
the common cap.
