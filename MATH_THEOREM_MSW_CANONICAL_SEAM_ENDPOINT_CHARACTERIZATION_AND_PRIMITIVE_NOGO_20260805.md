# Canonical MSW seam endpoints: exact characterization and the primitive-component no-go

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, finite search, or solver  
**Status:** unconditional characterization on the **first-upper-repeat
face** `P union M_0=M_0 union M_1`.  It proves that independent path
reversal cannot upgrade the canonical MSW protected-stem theorem on that
restricted face.  It is not a no-go for a free-repeat seam
`P=M_0-q+p` with arbitrary `p notin M_0`; that broader interface is treated
in `MATH_THEOREM_MSW_FREE_REPEAT_COLLAR_AND_ENDPOINT_GRAPH_20260805.md`.

## Scope correction (2026-08-05)

The upper multiplicity budget does not force the added seam to repeat the
first stem colour `U_1`.  In an already upper-exact forest, every Johnson
seam has a rank-`(r+1)` union which already has one provider and therefore
costs exactly one excess occurrence.  The no-go below remains correct for
the historically used choice `p=rho_1`, but it must not be cited against
the broader free-repeat collar.

## 0. Outcome

Let `x` be a Dyck word of semilength `r`, and let `P(x)` be its canonical
Mütze--Standke--Wiechert complementary geodesic in the rank-`r` layer of the
`2r`-cube.  Its endpoints are `x` and `bar(x)`.  Fix a stem length

\[
                         s=h+1\le r,\qquad h<r.        \tag{0.1}
\]

The previous protected-stem theorem allows us to orient `P(x)` from either
endpoint and use its first `s` Johnson edges as a generalized balanced
collar stem.  To turn the `Cat_r` path components into the collar-adapted
spanning path, the repeated left seam must have the form

\[
                   P\longrightarrow M_0,
        \qquad P\cup M_0=M_0\cup M_1,                \tag{0.2}
\]

where `P` is the terminal endpoint of another MSW component and the deleted
label belongs to the stem core.

This note characterizes every possible `P` **under the additional equation
`P union M_0=U_1`**.

Write the primitive-factor decomposition

\[
                         x=w_1w_2\cdots w_t.           \tag{0.3}
\]

If the stem starts at the Dyck endpoint `x`, its endpoint predecessors are
exactly the words obtained by moving the closing downstep of `w_1` to a
surviving upstep in `w_2\cdots w_t`.  If the stem starts at the anti-Dyck
endpoint `bar(x)`, its endpoint predecessors are exactly the anti-Dyck words
obtained by the reflected operation: move the opening upstep of `w_t` to a
surviving downstep in `w_1\cdots w_{t-1}`.

For a nonprimitive `x`, each orientation has at least

\[
                              r-h>0                   \tag{0.4}
\]

candidates before any further endpoint collision is imposed.

For a primitive word `x=1u0`, however, both candidate sets are empty unless

\[
                         x=1(10)^{r-1}0.               \tag{0.5}
\]

The exceptional height-two word has one candidate in each orientation.
Thus

\[
 \boxed{
   \operatorname {Cat}_{r-1}-1
   \text{ canonical MSW components have no legal repeated-seam
   predecessor in either orientation}. }             \tag{0.6}
\]

This is a positive-density obstruction:

\[
 {\operatorname {Cat}_{r-1}-1\over\operatorname {Cat}_r}
      ={r+1\over4r-2}-o(1)\longrightarrow {1\over4}. \tag{0.6a}
\]

For `r>=4`, the number in (0.6) exceeds one.  In a directed spanning path
of components only its first component may have no predecessor.  Therefore:

\[
 \boxed{
 \begin{gathered}
 \text{The canonical MSW path factor, even with independent reversal of
 every path,}\\
 \text{cannot be collar-adapted on the first-upper-repeat face with }
 \operatorname {Cat}_r-1\\
 \text{initial collars for }r\ge4.
 \end{gathered}}                                      \tag{0.7}
\]

This does not contradict the unconditional protected-stem theorem.  All
canonical components have long geodesic stems; a positive fraction of them
simply cannot receive the specialized seam which repeats `U_1`.

The corrected next target must change one of three things:

1. rethread or replace the canonical endpoint pairing on the primitive
   components;
2. permit a longer stateful left interface instead of one repeated edge; or
3. use a noncanonical complementary-geodesic factor whose endpoint
   transversal has at most one seam-isolated component.

## 1. Dyck-height notation and MSW boundary flips

For a balanced binary word `a=a_1\cdots a_{2r}`, put

\[
 H_a(j)=\sum_{i=1}^{j}(2a_i-1).                       \tag{1.1}
\]

Thus `a` is Dyck exactly when `H_a(j)>=0` for every `j`, and it is
anti-Dyck exactly when `H_a(j)<=0` for every `j`.

Write the first-return decomposition

\[
                         x=1u0v,\qquad d=|u|+2.        \tag{1.2}
\]

The MSW flip recursion begins with coordinate `d`.  Consequently the first
upper owner on the orientation from `x` is

\[
                             U=x\cup\{d\}.             \tag{1.3}
\]

Every rank-`r` owner giving the repeated union in (0.2) is

\[
                             P_q=U\setminus\{q\},      \tag{1.4}
\]

where `q` is a `1`-position of `x`.  For the generalized balanced collar,
`q` must additionally survive in the core after the first `h` Johnson
exchanges.

At the other endpoint, let `p` be the initial position of the last
primitive factor `w_t` in (0.3).  The last entry of the MSW flip sequence
is `p`: this follows immediately by iterating the suffix term in

\[
 \pi(1u0v)=
   (d,\ d-\pi(\mu u),\ 1,\ d+\pi(v)).                \tag{1.5}
\]

Thus, when the path is reversed from `bar(x)`, its first upper owner is

\[
                         U'=\bar x\cup\{p\}.           \tag{1.6}
\]

Its repeated-union candidates are

\[
                         P'_q=U'\setminus\{q\},        \tag{1.7}
\]

where `q` is a `1`-position of `bar(x)`, equivalently a downstep of `x`.

## 2. Forward endpoint characterization

### Theorem 2.1

Assume `v` in (1.2) is nonempty.  Then `P_q` in (1.4) is an endpoint of an
MSW path if and only if

\[
                  q>d\quad\text{and}\quad x_q=1.      \tag{2.1}
\]

In that case `P_q` itself is a Dyck word.  If `v` is empty, an endpoint
candidate exists if and only if (0.5) holds, and then the unique candidate
is `q=1`; `P_1` is anti-Dyck.

#### Proof

Changing the closing downstep at `d` into an upstep raises the height by two
from `d` onward.  Deleting the upstep at `q` lowers it by two from `q`
onward.

If `q>d`, the height is unchanged before `d`, raised by two on
`[d,q-1]`, and unchanged after `q`.  Hence `P_q` is Dyck.

If `q<d`, then at the position `d-1` the primitive prefix has height one.
The deletion at `q` has already acted and the insertion at `d` has not, so

\[
                         H_{P_q}(d-1)=-1.              \tag{2.2}
\]

Thus `P_q` is not Dyck.  Unless `q=1`, it still begins in `1`, so it is not
anti-Dyck either.

If `q=1`, then before `d` its heights are `H_x-2`, while from `d` onward
they are again `H_x`.  For a nonempty Dyck suffix `v`, the latter heights
are positive somewhere, so `P_1` cannot be anti-Dyck.  If `v` is empty,
anti-Dyckness is equivalent to

\[
                         H_x(j)\le2\quad(1\le j<2r).   \tag{2.3}
\]

A primitive Dyck word has height at most two exactly when it is
`1(10)^(r-1)0`.  This proves the theorem. `square`

### Corollary 2.2 (the core restriction costs no existence)

Suppose `v` has semilength `r-a>0`, so the first primitive factor has
semilength `a`.  After the first `h<r` Johnson exchanges, the number of
forward candidates (2.1) which remain in the stem core is exactly

\[
 \begin{cases}
   r-a,&h<a,\\
   r-h,&h\ge a.
 \end{cases}                                          \tag{2.4}
\]

In particular it is at least `r-h`.

#### Proof

The recursion (1.5) processes all `2a` coordinates of the first primitive
factor before it processes the suffix `v`.  The first `a` Johnson exchanges
therefore delete only upsteps of the first factor.  If `h>a`, exactly
`h-a` of the `r-a` suffix upsteps have subsequently been deleted.  Formula
(2.4) follows. `square`

## 3. Reverse endpoint characterization

### Theorem 3.1

Suppose (0.3) has at least two primitive factors, and let `p` be the first
position of `w_t`.  Then `P'_q` in (1.7) is an endpoint of an MSW path if
and only if

\[
                  q<p\quad\text{and}\quad x_q=0.      \tag{3.1}
\]

In that case `P'_q` is anti-Dyck.  If `x` is primitive, an endpoint
candidate exists if and only if (0.5) holds, and then the unique candidate
is `q=2r`; `P'_{2r}` is Dyck.

#### Proof

The starting word `bar(x)` is anti-Dyck.  Inserting at `p` raises its
height by two from `p` onward, while deleting a `1` of `bar(x)` at `q`
lowers it by two from `q` onward.

If `q<p`, the height is unchanged before `q`, lowered by two on
`[q,p-1]`, and unchanged after `p`.  Hence `P'_q` is anti-Dyck.

If the last primitive is not the whole word and `q>p`, the word still
begins in zero, so an endpoint would have to be anti-Dyck.  But at the first
position `p` of the last primitive, `H_x(p)=1`; before the deletion at `q`
we have

\[
                         H_{P'_q}(p)=-1+2=1,           \tag{3.2}
\]

which is impossible.

If `x` is primitive then `p=1`.  Every candidate has `q>1`, so `P'_q`
begins in one and could only be Dyck.  After deletion at any `q<2r`, its
height is `-H_x(q)<0`, since a primitive Dyck path is strictly positive
before its final step.  Hence `q=2r` is forced.  Before that last deletion,
Dyckness is exactly the bound `H_x<=2`, which is equivalent to (0.5).
This proves the theorem. `square`

### Corollary 3.2 (reverse core survival)

If the last primitive factor has semilength `b<r`, then after the first
`h<r` exchanges of the reversed path the number of candidates (3.1)
remaining in the stem core is

\[
 \begin{cases}
   r-b,&h<b,\\
   r-h,&h\ge b.
 \end{cases}                                          \tag{3.3}
\]

In particular it is at least `r-h`.

#### Proof

The last `2b` entries of (1.5) are precisely the flip block of the last
primitive factor.  Reversing the path processes that block first.  The
deleted coordinates from the anti-Dyck endpoint are the downsteps of `x`.
The same count as in Corollary 2.2, with prefix and suffix interchanged,
gives (3.3). `square`

## 4. The primitive obstruction

There are `Cat_(r-1)` primitive Dyck words of semilength `r`, because

\[
                         u\longmapsto1u0              \tag{4.1}
\]

is a bijection from `D_(r-1)` to the primitive words in `D_r`.  Exactly one
of them has height at most two, namely (0.5).  Theorems 2.1 and 3.1 prove
that every other primitive component has no endpoint predecessor for either
orientation.  This proves (0.6).

Now orient the `C` components arbitrarily and suppose the formal repeated
seams form a directed spanning path on the component set.  Exactly one
component is first and has no incoming seam; every other component must
have an endpoint predecessor of the form characterized above.  Hence at
most one seam-isolated primitive component is permissible.  For `r>=4`,

\[
                    \operatorname {Cat}_{r-1}-1>1,    \tag{4.2}
\]

contradicting (0.6).  This proves (0.7).

At `r=3`, the obstruction count equals one, so this argument alone does not
rule out a collar-adapted order.  No positive assertion for that finite
case is needed here.

### Corollary 4.1 (repair inside the first-upper-repeat face is Catalan-scale)

Suppose a new upper-exact `C`-path forest retains the canonical initial stem
on `C-1` MSW components but is allowed to change the terminal endpoint set.
If seams constrained to repeat `U_1` form the required component spanning path, then at
least

\[
                   \operatorname {Cat}_{r-1}-2        \tag{4.3}
\]

terminal endpoint occurrences must be owners outside the canonical MSW
endpoint set.

#### Proof

Among the `Cat_(r-1)-1` bad primitive components, at most one can be the
unique component on which no stem is prescribed.  Every remaining bad
component is a stem target and must receive an incoming repeated seam.
Theorems 2.1 and 3.1 say that none of its candidate predecessor owners is a
canonical endpoint.  Different incoming seams consume different terminal
endpoint occurrences.  Hence at least `Cat_(r-1)-2` new terminal occurrences
are necessary. `square`

Since `Cat_(r-1)/Cat_r -> 1/4`, a repair which stays on this restricted
repeat face cannot be an `O(1)` endpoint perturbation or a bounded collection
of local endpoint exceptions.  Free-repeat seams are outside the corollary.

## 5. Orientation-state law

The endpoint characterization has a second useful consequence.  Regard
orientation from `x` to `bar(x)` as sign `+` and the reverse orientation as
sign `-`.

* A forward target (`+`) receives a predecessor `P_q` which is Dyck.  To
  make that Dyck endpoint terminal, its predecessor component must have
  sign `-`.
* A reverse target (`-`) receives a predecessor `P'_q` which is anti-Dyck.
  To make that endpoint terminal, its predecessor component must have sign
  `+`.

Thus every ordinary repeated seam, i.e. every seam whose target is
nonprimitive, changes sign:

\[
                              -\longrightarrow+,
                 \qquad      +\longrightarrow-.       \tag{5.1}
\]

The unique height-two primitive component (0.5) is exceptional.  Its
forward candidate is anti-Dyck and its reverse candidate is Dyck, so a seam
entering that one component may preserve rather than change sign.  Hence a
hypothetical spanning seam path would alternate signs except at at most one
position; in particular the two orientation counts could differ by at most
two.  Independent path reversal supplies this binary choice, but it cannot
repair the primitive zero-neighbourhoods.

## 6. Residence and spread scope

Reversing a canonical MSW path preserves the following local facts:

1. every chosen stem is a Johnson geodesic;
2. its owners and upper colours remain disjoint from those of every other
   canonical path;
3. every active coordinate changes membership at most once inside the
   stem.

It merely exchanges the first-primitive and last-primitive boundary
profiles.  Equations (2.4) and (3.3) show that, on every nonprimitive path,
the core retains at least `r-h` endpoint-seam choices in either orientation.
This is ample local aperture when `h=Theta(sqrt(r))`.

However reversal creates no aperture at all on the
`Cat_(r-1)-1` bad primitive components.  Therefore no low-star spread or
residence averaging over the two orientations can imply the required
spanning seam order: the obstruction is a literal empty neighbourhood, not
a concentration failure.

The local one-change property also does not by itself prove the global
residence gate.  Prefix and suffix runs clipped by the formal seams still
need the external collar inequalities.  The theorem here concerns only the
owner/upper-q1 endpoint interface.

## 7. Corrected frontier

The unconditional MSW/MNW theorem supplies the entire Catalan bank of long,
owner-disjoint, upper-disjoint stems.  The present theorem proves only that
its canonical endpoint transversal cannot supply the seams if each seam is
forced to repeat its target stem's first upper colour.

On that restricted face, the Hall graph has `Cat_(r-1)-1` isolated target
components, so endpoint repair is necessary.  On the broader free-repeat
face the isolated vertices disappear; its correct frontier is the
bi-core-safe signed Gray-code problem in the companion note.
