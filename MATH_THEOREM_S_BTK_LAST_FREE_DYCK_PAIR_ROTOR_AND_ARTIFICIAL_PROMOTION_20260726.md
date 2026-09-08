# The BTK last-free Dyck pair: native rotors, the exact fibre obstruction, and artificial promotions

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 E=[2m],\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},
\]

with the convention \(N_{m+1}=0\), and fix \(1\le H<m\).  Use the BTK convention in which a matched pair
has the form \(0D1\), with \(D\) a Dyck word.  Suppose a BTK source
signature has native radius \(r+1\), with free positions

\[
 u_1<\cdots<u_{2r}<a<b,
\]

and pair the last two free positions \(a,b\) across their fully matched
intervening substring.  The resulting target signature has native radius
\(r\), fixes \(a\) out and \(b\) in, and retains free positions
\(u_1,\ldots,u_{2r}\).

The exact conclusions are as follows.

1. If \(r\ge H\), the forced native radius-\(H\) clippings form a genuine
   rotor.  The departure is
   \[
                         x=u_{r+1-H},
   \]
   not \(u_{r-H}\), and the exterior entry is exactly \(b\).

2. Taking this arc for every source is **not target-injective**.  A target
   has as many preimages as there are primitive Dyck factors in its final
   fully matched suffix.  At native target radius \(r\), the unrestricted
   family has \(\gamma_{r+1}=N_{r+1}-N_{r+2}\) arcs.  Summed over
   \(r\ge H\), it has \(N_{H+1}\) arcs counted with their distinct
   sources, but repeated targets occur.

3. There is a sharp canonical repair.  Retain precisely the sources whose
   last free position is \(b=2m\), equivalently unpair the last primitive
   factor of the target's final Dyck suffix.  These arcs form a
   vertex-disjoint matching of exact size
   \[
     \boxed{
     R_H=\binom{2m-1}{m-H-1}
         ={m-H\over2m}N_H.}
   \]
   This is the largest target-injective subfamily of last-two-free arcs.
   It contains the adjacent-suffix matching of size
   \(\binom{2m-2}{m-H-1}\), strictly when \(H\le m-2\).
   In particular, if \(H=o(m)\), then \(R_H=(1/2+o(1))N_H\); if
   \(H=A\sqrt m+O(1)\), then
   \(R_H=(e^{-A^2}/2+o(1))W\).

4. If \(r=d<H\), no flag-coherent artificial radius-\(H\) collars on
   this paired source and target give a rotor in either orientation.  In
   particular, \(b\) lies inside the source collar at slot \(H+d+1\), so
   it cannot be the exterior entry.

5. The low-radius pair is nevertheless bridge-one.  For every coherent
   source extension, and every choice of departure in its lower block,
   there is a unique coherent target extension for which the transition
   is the late promotion deleting \(b\) from slot
   \[
                         j=H+d+1.
   \]
   The exact number of such extension-level promotion arcs for one paired
   signature is
   \[
     \boxed{
      \bigl((m-d-1)_{H-d-1}\bigr)^2(m-H).}
   \]

6. Canonically imposing \(b=2m\) at every radius pairs all BTK chains:
   after choosing the collars in item 5 on the low-radius pairs, it gives
   a bridge-one perfect matching of the \(W\) BTK chains.  It contains
   exactly \(R_H\) native rotors and \(W/2-R_H\) artificial-collar
   promotions.

7. More generally, every directed path in the last-two-free contraction
   digraph has one recursively coherent radius-\(H\) lift.  Nevertheless,
   on the BTK chains of native radius at least \(q\), the exact minimum
   number of components in any path forest using only these contractions
   is
   \[
     \boxed{P_q=\binom{2m-1}{m-q}
                 ={m+q\over2m}N_q.}
   \]
   Thus at \(q=H\) this is an acceptable \(O(W/m)=o(W/H)\) top-tail
   forest, but at \(q=q_0=m^{1/4}+O(1)\) it is
   \((1/2+o(1))W\).  Artificial collars do not repair this integral
   owner-fibre obstruction.

The all-radius matching in item 6 is real and exact, but has \(W/2\)
two-vertex paths.  Item 7 strengthens this: even allowing every possible
last-two-free contraction and choosing the paths optimally still leaves
the displayed half-census obstruction near the centre.  Iterating
genuinely different, non-monotone operations while preserving one common
collar choice remains a separate problem.

## 1. Signature and Dyck normal form

A BTK chain signature of radius \(s\) has \(2s\) free stars.  Its fixed
coordinates are partitioned into noncrossing matched zero--one pairs.
Equivalently it has the unique form

\[
 D_0*D_1*\cdots *D_{2s},
\tag{1.1}
\]

where every \(D_i\) is a (possibly empty) Dyck word.  The coordinates
fixed to one form the fixed-in set \(I\), and those fixed to zero form
the fixed-out set \(O\).

For the source in the outcome, refine (1.1) around the last two stars as

\[
 D_0*\cdots *D_{2r}*D_{2r+1}*D_{2r+2}.
\tag{1.2}
\]

The final two stars occupy \(a,b\).  Replacing the displayed final
\(*D_{2r+1}*\) by

\[
                         0D_{2r+1}1
\tag{1.3}
\]

creates one more matched pair without changing any old pair.  Thus the
target is a valid BTK signature, has free positions
\(u_1,\ldots,u_{2r}\), fixed-in set \(I+\{b\}\), and fixed-out set
\(O+\{a\}\).  This proves validity without assuming that \(a,b\) are
adjacent or that \(b=2m\).

## 2. The exact native clipped rotor

Define one ordered list

\[
 v_i=u_i\ (1\le i\le2r),\qquad
 v_{2r+1}=a,\qquad v_{2r+2}=b.
\tag{2.1}
\]

Assume \(r\ge H\).  The source has radius \(r+1\), so its forced
radius-\(H\) clipping is

\[
 \begin{aligned}
 L_+&=I+\{v_1,\ldots,v_{r+1-H}\},\\
 Z_+&=(v_{r+2-H},\ldots,v_{r+H+1}),\\
 R_+&=O+\{v_{r+H+2},\ldots,v_{2r+2}\}.
 \end{aligned}
\tag{2.2}
\]

Because \(r\ge H\), the displayed lower set ends among the \(u_i\)'s,
and \(b=v_{2r+2}\) always belongs to \(R_+\).  The target has radius
\(r\), hence its forced clipping is

\[
 \begin{aligned}
 L_0&=I+\{b\}+\{u_1,\ldots,u_{r-H}\},\\
 Z_0&=(u_{r-H+1},\ldots,u_{r+H}),\\
 R_0&=O+\{a\}+\{u_{r+H+1},\ldots,u_{2r}\}.
 \end{aligned}
\tag{2.3}
\]

### Theorem 2.1 (native last-free-pair rotor)

The full rotor with

\[
                         x=u_{r+1-H},\qquad y=b
\tag{2.4}
\]

sends (2.2) exactly to (2.3).

#### Proof

The full rotor law is

\[
 (L;z_1,\ldots,z_{2H};R)
 \longmapsto
 (L-x+y;\ x,z_1,\ldots,z_{2H-1};\ R-y+z_{2H}).
\tag{2.5}
\]

Here \(x=v_{r+1-H}\) is the last newly free coordinate in \(L_+\), and
the first coordinate of \(Z_+\) is \(v_{r+2-H}\).  Therefore the new
lower block and collar are

\[
 I+\{b\}+\{u_1,\ldots,u_{r-H}\}
\tag{2.6}
\]

and

\[
 (u_{r+1-H},u_{r+2-H},\ldots,u_{r+H}),
\tag{2.7}
\]

which are \(L_0,Z_0\).

If \(r>H\), the last old collar coordinate is
\(v_{r+H+1}=u_{r+H+1}\), and (2.5) changes the residual block into

\[
 O+\{a\}+\{u_{r+H+1},\ldots,u_{2r}\}.
\]

If \(r=H\), the last old collar coordinate is instead
\(v_{2r+1}=a\), while \(R_+=O+\{b\}\); the same formula gives
\(R_0=O+\{a\}\).  Thus the endpoint case is included and every part of
the successor is exactly (2.3). \(\square\)

## 3. The unrestricted map is not injective

Fix a target signature of radius \(r\), and let \(D\) be the fully
matched Dyck suffix after its last free star (the whole signature when
\(r=0\)).  Write its unique primitive factorization as

\[
                         D=P_1P_2\cdots P_k,
\tag{3.1}
\]

where every \(P_i=0Q_i1\) is nonempty and primitive.

### Proposition 3.1 (exact preimage fibre)

The target has exactly \(k\) preimages under last-two-free pairing, one
for each primitive factor in (3.1).

#### Proof

Unpairing the outer zero and one of \(P_i\) leaves its interior \(Q_i\)
fully matched.  All earlier target stars precede these two new stars, and
all material after the second new star is still fully matched.  Thus the
two new stars are the last two free positions of a valid source
signature.  The construction is different for distinct primitive
factors.

Conversely, in any source preimage the new matched pair \(a,b\) encloses
a fully matched word, and the material after \(b\) is fully matched.
Hence \(0D_{ab}1\) is one primitive factor of the target's final Dyck
suffix.  This recovers one of the factors in (3.1), proving exhaustivity.
\(\square\)

For example, the target signature

\[
                         **0101
\tag{3.2}
\]

has the two distinct source preimages

\[
                         ****01,qquad **01**.
\tag{3.3}
\]

Thus the unrestricted last-two-free construction is not a matching.

Let

\[
 \gamma_r=N_r-N_{r+1}
 ={2r+1\over m+r+1}N_r
\tag{3.4}
\]

be the number of BTK chains of native radius \(r\).  Every source of
radius \(r+1\) gives one arc, so the number of raw arcs from radius
\(r+1\) to radius \(r\) is exactly \(\gamma_{r+1}\).  Hence

\[
 \sum_{r=H}^{m-1}\gamma_{r+1}=N_{H+1}.
\tag{3.5}
\]

Equation (3.5) counts distinct sources and directed arcs, not distinct
targets.

## 4. A sharp canonical injective family

Take the last primitive factor in (3.1).  Its closing one is coordinate
\(2m\).  Equivalently, on the source side retain exactly signatures whose
last free position is

\[
                         b=2m.
\tag{4.1}
\]

This choice is unique for every target with nonempty final Dyck suffix.
The sources have coordinate \(2m\) free, whereas the targets have it fixed
in, so the two endpoint classes are disjoint.

### Theorem 4.1 (sharp canonical native matching)

At target radius \(r\), the canonical family has

\[
 A_r={r+1\over m}N_{r+1}
\tag{4.2}
\]

vertex-disjoint arcs.  Over every \(r\ge H\), it has

\[
 \boxed{
 \sum_{r=H}^{m-1}A_r
 =\binom{2m-1}{m-H-1}
 ={m-H\over2m}N_H.}
\tag{4.3}
\]

No target-injective subfamily of the unrestricted last-two-free arcs can
have more arcs.

#### Proof

Let \(C(z)=1+zC(z)^2\) be the Catalan generating function.  A radius-
\(r\) signature is a sequence of \(2r+1\) Dyck gaps with total semilength
\(m-r\).  Requiring its final gap to be nonempty gives

\[
 \begin{aligned}
 A_r
 &=[z^{m-r}]C(z)^{2r}(C(z)-1)\\
 &=[z^{m-r-1}]C(z)^{2r+2}\\
 &={2r+2\over2m}\binom{2m}{m-r-1}
 ={r+1\over m}N_{r+1},
 \end{aligned}
\tag{4.4}
\]

using the standard Lagrange coefficient

\[
 [z^j]C(z)^p={p\over2j+p}\binom{2j+p}{j}.
\tag{4.5}
\]

Put \(d=r+1\).  The elementary identity

\[
 {d\over m}\binom{2m}{m-d}
 =\binom{2m-1}{m-d}-\binom{2m-1}{m-d-1}
\tag{4.6}
\]

telescopes from \(d=H+1\) through \(m\), proving the first equality in
(4.3).  The second is the usual adjacent-layer binomial ratio.

By Proposition 3.1, all unrestricted arcs into one target form one fibre.
An injective subfamily can use at most one member of each nonempty fibre,
and there are exactly \(A_r\) such fibres.  The last-primitive choice uses
one in every fibre, so it is sharp.  Its sources and targets are disjoint,
as observed above, and hence its arcs form a vertex-disjoint matching.
\(\square\)

If the unmatched native tag-\(H\) chains are made singletons, this
matching gives the exact top-tail path count

\[
 N_H-R_H={m+H\over2m}N_H.
\tag{4.7}
\]

Thus it is still a positive fraction of \(N_H\).  It is insufficient at
fixed Gaussian depth \(H=A\sqrt m\), but at any critical scale with
\(H=o(m)\) and \(N_H=O(W/m)\) it is already
\(O(W/m)=o(W/H)\).  This latter observation
concerns only the top-tail class; it supplies no common lower-tag
integration.

## 5. Exact artificial-collar analysis below the cutoff

Now let the target native radius be

\[
                         d<H,
\]

and put \(s=H-d\).  The paired source has native radius \(d+1\).
Write its fixed-in and fixed-out sets as \(I,O\); both have size
\(m-d-1\).  Let

\[
                         U=(u_1,\ldots,u_{2d}).
\]

Every flag-coherent radius-\(H\) extension of the source has the form

\[
 \omega_+(A,B)=
 (I\setminus A;\ A,U,a,b,B;\ O\setminus B),
\tag{5.1}
\]

where \(A\) and \(B\) are ordered \((s-1)\)-tuples from \(I\) and
\(O\), respectively.  Every flag-coherent extension of the target has
the form

\[
 \omega_0(C,D)=
 ((I+\{b\})\setminus C;\ C,U,D;\
  (O+\{a\})\setminus D),
\tag{5.2}
\]

where \(C\) is an ordered \(s\)-tuple from \(I+\{b\}\), and \(D\) is
an ordered \(s\)-tuple from \(O+\{a\}\).  Equations (5.1)--(5.2)
exhaust all coherent artificial collars.

### Theorem 5.1 (no artificial rotor, but an exact late promotion)

For \(d<H\):

1. no choices in (5.1)--(5.2) give a rotor from \(\omega_+\) to
   \(\omega_0\), or from \(\omega_0\) to \(\omega_+\);
2. choose arbitrary ordered tuples \(A,B\) as in (5.1) and any
   \(x\in I\setminus A\), and set
   \[
                    C=(x,A),\qquad D=(a,B).
   \tag{5.3}
   \]
   Then the promotion from \(\omega_+(A,B)\) with departure \(x\) which
   omits \(b\) sends it exactly to \(\omega_0(C,D)\);
3. these are all forward promotions between the paired source and target
   extensions.

The omitted slot is exactly

\[
                         j=H+d+1.
\tag{5.4}
\]

#### Proof

In the source collar (5.1), the coordinate \(b\) occupies slot

\[
 (s-1)+2d+2=H+d+1\le2H.
\tag{5.5}
\]

Thus \(b\) is not in the source residual block and cannot be the exterior
entry used in Theorem 2.1.

Suppose first that a rotor sends (5.1) to (5.2).  If \(s\ge2\), its new
collar has the exact form

\[
                         (x,A,U,a,b,B^-),
\tag{5.6}
\]

where \(B^-\) deletes the last entry of \(B\).  But the part of the
target collar after \(U\) is \(D\subseteq O+\{a\}\), and cannot contain
\(b\).  If \(s=1\), collar equality forces \(C=(x)\), \(D=(a)\); lower
block equality then forces the rotor entry to be \(b\), which is not in
the source residual block \(O\).  Hence no forward rotor exists.

For a reverse rotor and \(d\ge1\), the coordinate \(u_1\) occurs at
position \(s+1\) in the target collar and hence at position \(s+2\) after
the rotor prepends its departure.  It must occur at position \(s\) in the
source collar (5.1), impossible because all coordinates are distinct.  If
\(d=0\) and \(H=s\ge2\), the source requires \(a\) at collar position
\(H\), whereas that position of a reverse-rotor successor lies in
\(C\subseteq I+\{b\}\).  For \(d=0,H=1\), its first collar coordinate
would have to be the departure \(a\), but
\(a\notin I+\{b\}\).  Thus no reverse rotor exists either.

Now apply the full promotion law

\[
 (L;z_1,\ldots,z_{2H};R)
 \longmapsto
 (L-x+z_j;\ x,z_1,\ldots,\widehat z_j,\ldots,z_{2H};R)
\tag{5.7}
\]

to (5.1), with \(z_j=b\).  It gives

\[
 (I\setminus(A+\{x\})+\{b\};\ x,A,U,a,B;\ O\setminus B),
\tag{5.8}
\]

which is exactly (5.2) under (5.3).

Conversely, a forward promotion preserves the residual block.  Equality
with (5.2) forces \(a\) to be used in the target upper artificial tuple,
and every member of \(B\) to follow it.  The source coordinate \(b\)
cannot remain after \(U\), because the target's post-\(U\) tuple lies in
\(O+\{a\}\); it must therefore be the omitted coordinate.  The remaining
collar order then forces exactly \(C=(x,A)\), \(D=(a,B)\).  This proves
exhaustivity and (5.4). \(\square\)

There are

\[
 (m-d-1)_{s-1}^2
\]

choices of \((A,B)\).  After either tuple is chosen, the source lower
block has \(m-H\) coordinates available for \(x\).  Thus the exact number
of extension-level arcs in Theorem 5.1 is

\[
 \bigl((m-d-1)_{H-d-1}\bigr)^2(m-H).
\tag{5.9}
\]

Here \((t)_j=t(t-1)\cdots(t-j+1)\), with \((t)_0=1\).

## 6. The canonical all-radius perfect bridge matching

At coordinate \(2m\), a BTK signature has only two possibilities:

* it is free; or
* it is the closing one of a matched pair.

It cannot be a fixed-out zero, since there is no later coordinate with
which that zero could be matched.  If it is free, pair it with the
preceding free coordinate.  If it is fixed in, unpair the outer endpoints
of the last primitive factor of the final Dyck suffix.  These operations
are inverse.  Hence the canonical \(b=2m\) rule is a bijection between the
two classes of BTK chains.

The number in either class is

\[
 \sum_{d=1}^{m}{d\over m}N_d
 =\binom{2m-1}{m-1}
 ={W\over2}.
\tag{6.1}
\]

### Corollary 6.1 (perfect bridge matching with exact type split)

For every \(1\le H<m\), one can choose one flag-coherent radius-\(H\)
collar on every BTK chain so that the canonical \(b=2m\) pairs form a
directed bridge-one perfect matching.  Its exact transition census is

\[
 \boxed{
 \#\text{native rotors}
 =R_H=\binom{2m-1}{m-H-1},}
\tag{6.2}
\]

\[
 \boxed{
 \#\text{artificial-collar promotions}
 ={W\over2}-R_H.}
\tag{6.3}
\]

#### Proof

For a pair whose target radius is at least \(H\), use the forced native
clippings and Theorem 2.1.  Summing their exact counts gives (4.3).  For a
pair whose target radius is below \(H\), choose any \(A,B,x\) allowed by
Theorem 5.1 and give its target the induced collar (5.3).  The canonical
pairs are vertex-disjoint, so these collar choices never compete for one
chain.  Theorem 5.1 supplies the remaining bridge arcs.  Equation (6.1)
then gives (6.3). \(\square\)

## 7. Recursive lift and the exact last-pair path obstruction

Fix \(0\le q\le m\), and let \(\mathcal B_{\ge q}\) be the standard BTK
signatures of native radius at least \(q\).  Hence

\[
                         |\mathcal B_{\ge q}|=N_q.
\tag{7.1}
\]

For every signature of positive radius, let \(f(C)\) be obtained by
pairing its last two free positions.  Direct every available edge as
\(C\to f(C)\).  The native radius decreases by one on every edge.

### Theorem 7.1 (exact optimal contraction forest)

Among all directed path forests on \(\mathcal B_{\ge q}\) using only
last-two-free contraction edges, the maximum number of edges is

\[
 \boxed{
 E_q=\binom{2m-1}{m-q-1}
     ={m-q\over2m}N_q.}
\tag{7.2}
\]

Consequently the exact minimum number of path components is

\[
 \boxed{
 P_q=N_q-E_q
     =\binom{2m-1}{m-q}
     ={m+q\over2m}N_q.}
\tag{7.3}
\]

Both extrema are attained integrally.

#### Proof

At target radius \(r\), Proposition 3.1 says that the image of \(f\)
consists exactly of signatures whose final Dyck gap is nonempty.  Section
4 counted these targets:

\[
                         A_r={r+1\over m}N_{r+1}.
\tag{7.4}
\]

A path forest can use at most one incoming edge at each target.  Hence it
has at most

\[
 \sum_{r=q}^{m-1}A_r
 =\binom{2m-1}{m-q-1}
\tag{7.5}
\]

edges, by the same telescoping identity (4.6).  Conversely, choose one
preimage of every target in the image of \(f\), for example by unpairing
the last primitive factor of its final Dyck gap.  Distinct targets have
distinct chosen sources because \(f\) is a function.  Thus every vertex
has indegree and outdegree at most one.  Radius strictly decreases, so
there is no directed cycle.  The selected graph is therefore a path
forest with exactly (7.5) edges.  A forest with \(N_q\) vertices and
\(E_q\) edges has \(N_q-E_q\) components.  Pascal's identity and the
adjacent binomial ratios give (7.3). \(\square\)

The raw count \(N_{H+1}\) in (3.5) is therefore not a usable
path-forest edge count.  It counts every source arc before the repeated
target fibres are resolved.  The exact usable maximum on the top tail is

\[
                         E_H=R_H,
\tag{7.6}
\]

only \((1/2+o(1))N_H\) when \(H=o(m)\).

### Theorem 7.2 (recursive collar composability)

Every path forest attaining Theorem 7.1, and indeed every selected
subforest of the last-two-free contraction digraph, admits one coherent
radius-\(H\) state on each of its BTK chains such that every selected
edge is a literal bridge-one transition.  Edges whose target radius is at
least \(H\) are the native rotors of Theorem 2.1; all lower edges are the
promotions of Theorem 5.1.

#### Proof

On the part of a path with native radii at least \(H\), each chain has
its forced clipped state, so consecutive rotors compose automatically.
Consider the first edge whose target radius is \(d<H\).  If
\(d=H-1\), its source has radius \(H\); in (5.1) the lists \(A,B\) are
empty, so that source state is exactly its forced clipping.

For the induction, suppose the step from radius \(d+1\) to radius \(d\)
uses the source lists \(A,B\), each of length \(H-d-1\), and departure
\(x\).  By Theorem 5.1 its target collar is

\[
                         (x,A;\ U;\ a,B).
\tag{7.7}
\]

When this radius-\(d\) target is used as the source of the next
contraction, its last two free coordinates are the last two entries of
\(U\).  Its required artificial lists have length \(H-d\).  Set

\[
                         A'=(x,A),\qquad B'=(a,B).
\tag{7.8}
\]

The new fixed-in set is \(I+\{b\}\), the new fixed-out set is
\(O+\{a\}\), and (7.8) makes both residual blocks and the entire ordered
collar identical to the preceding target state.  The next lower block
has size exactly \(m-H>0\), so a new departure can always be chosen.
This induction continues through target radius zero if required.

Different forest components use distinct BTK chains.  Truncating every
artificial state at its native tag recovers exactly that BTK chain, so
the original SCD's mask partition gives owner simplicity across
components.  Hence the lift is integral and literal. \(\square\)

For the one-baseline scale

\[
 q_0=\lceil m^{1/4}\rceil,
 \qquad H=\lfloor\sqrt{m\log m}\rfloor,
\tag{7.9}
\]

equation (7.3) gives

\[
 P_{q_0}=\left({1\over2}+o(1)\right)W,
\tag{7.10}
\]

whereas

\[
 P_H={m+H\over2m}N_H=O(W/m)=o(W/H).
\tag{7.11}
\]

Thus the stronger rule completely suffices for the retained top-tail
component scale, and its artificial collars are recursively compatible.
It cannot fuse the full retained BTK census: the exact failure is the
terminal-Dyck target capacity (7.2), not the bridge law.

## 8. Exact scope

Proved here:

1. validity of pairing the last two free BTK positions across an arbitrary
   fully matched substring;
2. the exact native clipped rotor, including the departure index, entry,
   endpoint case, and all three state parts;
3. the primitive-suffix fibre formula and a concrete failure of
   injectivity;
4. the sharp canonical injective count (4.3);
5. impossibility of an artificial rotor below the cutoff;
6. the exact replacement by a late promotion and its full extension
   count; and
7. the canonical all-radius perfect bridge matching;
8. recursive collar composability along arbitrary selected contraction
   paths; and
9. the exact optimal edge and component counts for the entire
   last-two-free contraction digraph.

Not proved here:

1. a path cover of all retained radii with \(o(W/H)\) components;
2. compatibility of two or more different canonical coordinate matchings
   with one common collar choice;
3. a long alternating forest obtained by composing these matchings; or
4. the constant-one theorem.

The corrected use of the lemma is therefore exact: the last-free rule
supplies a large native rotor matching, recursively coherent artificial
promotions below \(H\), and an optimal integral contraction forest.  Its
terminal-Dyck image has only half the required central owner capacity, so
it cannot by itself supply the long rotor paths needed for coefficient
one.
