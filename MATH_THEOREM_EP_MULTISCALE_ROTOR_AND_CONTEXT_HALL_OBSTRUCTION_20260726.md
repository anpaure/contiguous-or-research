# EP\(_A\): multiscale rotor filtration, a one-hole reservoir macro-packet, and the contextual Hall obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Result and exact scope

Put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 H=\lceil A\sqrt m\rceil
 \tag{0.1}
\]

for fixed \(A>0\).  A decorated clipped SCD has one full radius-\(H\)
state over every middle owner and \(\mathrm{EP}_A\) asks that these \(W\)
states have a spanning directed bridge-one path forest with

\[
                         p=o_A(W/H)
 \tag{0.2}
\]

components.

All finite statements below assume \(1\le H<m\), which holds for every
fixed \(A\) once \(m\) is sufficiently large.

This note does not prove or universally refute \(\mathrm{EP}_A\).  It
proves universal multiscale necessities, an exact strict-scale
lower-tag macro-packet and conditional integration theorem, and a
fixed-context Hall obstruction which closes the proposed use of the
existing logarithmic-anchor contextual atlas.

First, let \(R\) be the number of genuine full-radius rotor arcs in a
bridge-one path forest and let \(P_\ell\) be the number of promotion arcs
whose promoted singleton lies \(\ell\) places into the upper half of the
collar.  Then, simultaneously for every \(0\le q\le H\),

\[
 \boxed{
 p+R+\sum_{\ell>q}P_\ell\ge N_q.}
 \tag{0.3}
\]

In particular,

\[
 \boxed{R\ge N_H-p.}
 \tag{0.4}
\]

Under the EP hypothesis (0.2),
\[
 N_H-p=(e^{-A^2}+o_A(1))W.
\]
Thus dense genuine rotor motion somewhere in the full decorated cover is
necessary for every fixed \(A\), not only for \(A<\sqrt{\log2}\).  These
rotors may have lower-tag endpoints; (0.4) does not assert a dense
tag-\(H\)-to-tag-\(H\) backbone for large \(A\).  Promotions alone and a
globally \(O(1)\) average number of top-changing rotors per component are
excluded.

Writing

\[
                         \Delta=p+R-N_H\ge0,
 \tag{0.5}
\]

the same filtration gives

\[
 \boxed{
 H\Delta+\sum_{\ell=1}^H\ell P_\ell
 \ge \sum_{q=0}^{H-1}N_q-HN_H.}
 \tag{0.6}
\]

The right side is

\[
 \left[
  \int_0^A e^{-t^2}\,dt-Ae^{-A^2}+o_A(1)
 \right]W\sqrt m,
 \tag{0.7}
\]

and the bracket is positive for every \(A>0\).  Consequently a
near-minimal carrier threading, \(\Delta=o(W)\), requires a positive
density of promotions using literal \(\Theta(H)\)-deep collar slots.  This
is a deep-lookahead requirement; one such promotion is still a single
bridge edge, so no temporal-duration conclusion is inferred from (0.6)
alone.

There is, however, an exact temporal conclusion in the near-minimal rotor
branch.  The same defect satisfies
\[
 \Delta=\sum_U(a_U-1),
\]
where \(a_U\) is the number of promotion components in full-top fibre
\(U\).  If \(\Delta=o(W/H)\), almost every fibre is one promotion path;
after those paths are contracted, the genuine rotor quotient has \(p\)
paths of average length \(\omega(H)\).  This is the required long
exterior-moving normal form, but not its construction.

The two laws above do not create a local payload obstruction.  There is
an exact promotion ring of length \(m+H\) in one full-top fibre which
carries one tag-\(H\) anchor and \(m+H-1\) arbitrarily tagged lower chains
as pairwise mask-disjoint symmetric chains.  Prescribed cuts of such rings
have literal exterior-moving rotor cross-splices, and an explicit port
scaffold supplies \(2(m-H)=\Theta(m)\) cyclically compatible crossing
rotors with all port chains mask-disjoint.  The natural full rings do have
the exact staircase collision of Proposition 3.9, but all their interior
collisions are covered by one distinguished chain per ring.  Deleting
those chains gives an explicit \(\Theta(m^2)\)-state partial-SCD
macro-packet with \(\Theta(m)\) paths, component density
\(O(1/m)=o(1/H)\), and optional distributed exterior rotor switches.
What is not proved is a global owner-disjoint selection of these
macro-packets, jointly with the top rotor backbone, with the exact tag
census.

Second, let \(C\) be the fixed trace-visible anchor of the contextual
atlas, \(|C|=d\), and let a perfect matching \(M_x\) on the bulk be selected
by each anchor word \(x\subseteq C\).  Every SCD has at least

\[
                         D^-_{C,H}
 \tag{0.8}
\]

tag-\(H\) chains which either move the anchor or abandon the selected
matching's full-pair invariant, where \(D^-_{C,H}\) is the exact
sectorwise Hall deficit defined in (5.8).  For \(d=O(\log m)\),

\[
 \boxed{
 D^-_{C,H}=(\delta_A+o_A(1))W,\qquad
 \delta_A=e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0.}
 \tag{0.9}
\]

Only

\[
                         {dH\over m}N_H
 \tag{0.10}
\]

tag-\(H\) chains can move this fixed anchor.  Hence any proposed
RPE/TCB candidate in which all but \(o(W/H)\) top-tag states are inherited
from this frozen logarithmic-anchor atlas is impossible: it requires
\((\delta_A-o(1))W\) genuinely non-atlas top-tag chains.  A repair relying
only on anchor motion would require

\[
 \boxed{
 d\ge(\Delta_A-o_A(1)){m\over H},\qquad
 \Delta_A=\Phi(A/2)-e^{A^2}\Phi(-3A/2)>0,}
 \tag{0.11}
\]

so a trace-visible moving context must already have order \(\sqrt m\).

The obstruction occurs at the final lower endpoint matching.  Only
tag-\(H\) SCD chains own masks at rank \(m-H\); virtual radius-\(H\)
collars on lower tags and promotion detours cannot replace that actual
boundary partition.

The surviving route is therefore strictly larger than the frozen part of
the existing contextual atlas.  It may use a growing trace-visible
context of size \(\Omega_A(m/H)\), arbitrary-conjugate packets with no one
common anchor Hall set, or a positive-density family of anchor-avoiding
top chains which deliberately breaks the selected full-pair invariant.
In every case it must still be an owner-disjoint, payload-dense rotor
mosaic with an exact recursive common-base selection, together with either
the general lower-tag coalescent or the repaired reservoir-macro packing.
That global route remains open.

### Imported exact inputs and a logical correction

The non-elementary imported inputs are the bridge-one classification,
collar normal form, and exact recursive packet rotor cycles proved in
`ROTOR_MULTI_FRAME_PACKET_RESOLUTION_20260725.md`, together with the
standard uniform lattice central-limit theorem used in
`MATH_THEOREM_CONTEXTUAL_MOVING_FRAME_B4_RIGIDITY_PROVIDER_NOGO_20260726.md`.

The two earlier top-tag targets must be distinguished:

* \(\mathrm{RPE}_A^H\) is an exact mask-disjoint recursive-packet packing,
  boundary partition, and residual lower-tag SCD completion;
* \(\mathrm{TCB}_A\) is an approximate layerwise common-base construction
  with total forced-color, Boolean-completion, and active-boundary loss
  \(o(W/H)\).

They are alternative sufficient top-tag routes, not proved equivalent.
Neither, by itself, integrates the lower tags into the final path cover.

The clipped-BTK no-go stated in the second audited input is not used: it
is false.  Clipping mixes native BTK radii.  Indeed the two clipped BTK
states

\[
 (\{1,\ldots,m-H\};m-H+1,\ldots,m+H;
   \{m+H+1,\ldots,2m\})
\]

and

\[
 (\{1,\ldots,m-H-1\}\cup\{2m\};m-H,\ldots,m+H-1;
   \{m+H,\ldots,2m-1\})
\]

are joined by the rotor with departure \(m-H\) and entry \(2m\), for
every \(1\le H<m\).  Thus no conclusion below depends on native-radius
BTK rigidity.

## 1. Full collars and bridge types

A full radius-\(H\) state is an ordered partition

\[
 \omega=(L;z_1,\ldots,z_{2H};R_0),
 \qquad |L|=|R_0|=m-H.
 \tag{1.1}
\]

Its middle owner is

\[
                         X(\omega)=L+\{z_1,\ldots,z_H\}.
 \tag{1.2}
\]

Every bridge-one arc between distinct owners is of one of the following
two forms.

* A **rotor** chooses \(x\in L\), \(y\in R_0\), and has
  \[
   L'=L-x+y,\qquad
   z'=(x,z_1,\ldots,z_{2H-1}).
   \tag{1.3}
  \]
* A **promotion** chooses \(x\in L\) and \(H<j\le2H\), and has
  \[
   L'=L-x+z_j,\qquad
   z'=(x,z_1,\ldots,\widehat z_j,\ldots,z_{2H}).
   \tag{1.4}
  \]

Promotions with \(j\le H\) preserve the middle owner and therefore cannot
join two distinct vertices of a decorated SCD.  For (1.4), define its
**lookahead** by

\[
                         \ell=j-H\in\{1,\ldots,H\}.
 \tag{1.5}
\]

The full collar top is

\[
                         Q_H(\omega)=L+\{z_1,\ldots,z_{2H}\}.
 \tag{1.6}
\]

Promotion preserves (1.6), while a rotor changes it by one Johnson
exchange.  The next sections refine this observation simultaneously at
every intermediate radius.

## 2. Central truncation is an exact bridge functor

For \(1\le q\le H\), put \(s=H-q\) and define the radius-\(q\) central
truncation

\[
 \tau_q(\omega)=
 \left(
  L+\{z_1,\ldots,z_s\};
  z_{s+1},\ldots,z_{H+q};
  R_0+\{z_{H+q+1},\ldots,z_{2H}\}
 \right).
 \tag{2.1}
\]

The two residual sets in (2.1) have size \(m-q\), and the displayed
central word has length \(2q\).

### Theorem 2.1 (exact truncation of bridge-one arcs)

Under \(\tau_q\):

1. every full rotor becomes a radius-\(q\) rotor;
2. a promotion of lookahead \(\ell\le q\) becomes a radius-\(q\)
   promotion, at upper slot \(q+\ell\);
3. a promotion of lookahead \(\ell>q\) becomes a radius-\(q\) rotor.

Hence central truncation maps every full bridge-one path edge-for-edge to
a radius-\(q\) bridge-one path on the same ordered chain vertices.

#### Proof

For \(1\le q<H\), write

\[
 A=L+\{z_1,\ldots,z_s\},\quad
 c=(z_{s+1},\ldots,z_{H+q}),\quad
 B=R_0+\{z_{H+q+1},\ldots,z_{2H}\}.
 \tag{2.2}
\]

For a full rotor (1.3), direct substitution gives

\[
 A'=A-z_s+y,\qquad
 c'=(z_s,c_1,\ldots,c_{2q-1}),\qquad
 B'=B-y+c_{2q},
 \tag{2.3}
\]

which is exactly a radius-\(q\) rotor.

For a promotion, \(j=H+\ell\).  If \(\ell\le q\), then \(z_j\) lies in
the upper half of \(c\).  Substitution gives the radius-\(q\) promotion
which removes \(z_s\) from \(A\), prepends it to \(c\), and promotes the
letter in slot \(q+\ell\).

If \(\ell>q\), then \(z_j\in B\).  The same substitution gives

\[
 A'=A-z_s+z_j,\qquad
 c'=(z_s,c_1,\ldots,c_{2q-1}),\qquad
 B'=B-z_j+c_{2q},
 \tag{2.4}
\]

which is a radius-\(q\) rotor.  These computations also prove that no
additional cases occur.  At \(q=H\), \(s=0\), the truncation is the
identity and the three conclusions follow directly from the full bridge
classification. \(\square\)

### Corollary 2.2 (high-tag bridges truncate to genuine rotors)

For \(1\le q\le H\), if both endpoint chains of a distinct-owner bridge
have tags at least \(q\), their forced radius-\(q\) truncations are joined by a genuine
radius-\(q\) rotor arc.

#### Proof

By the defining compatibility of a collar extension with its tagged SCD
chain, (2.1) is the chain's actual SCD segment through ranks
\(m-q,\ldots,m+q\) whenever its tag is at least \(q\).  A radius-\(q\)
promotion preserves its rank-\((m+q)\) endpoint.  Two distinct chains of
one SCD cannot contain the same mask at that rank.  Case 2 of Theorem 2.1
is therefore impossible; the other two cases are rotors. \(\square\)

This corollary is a common all-depth constraint.  It cannot be obtained by
choosing separate matching maximizers at each recursive layer.

### Corollary 2.3 (residual-slot law for promotions)

If a distinct-owner promotion of lookahead \(\ell\) joins chains of tags
\(d\) and \(d'\) in one decorated SCD, then

\[
                         \boxed{\ell>\min\{d,d'\}.}
 \tag{2.5}
\]

In particular, a promotion between a tag-\(H\) anchor and a tag-\(d<H\)
chain must use a residual slot

\[
                         j=H+\ell>H+d.
 \tag{2.6}
\]

In the terminology of Propositions 5.4 and 5.6 of
`MATH_ATTACK_EP_PROMOTION_BACKBONE_20260725.md`, this excludes the \(d\)
formal middle-slot predecessor/successor templates from occurring together
with the anchor in one SCD.  An incoming top port collapses to its one
residual tagged template, while an outgoing top port may use only the late
residual-slot templates.

#### Proof

If \(\ell\le\min\{d,d'\}\), apply Theorem 2.1 at \(q=\ell\).  It makes the
edge a radius-\(\ell\) promotion, whereas Corollary 2.2 makes the same
edge a genuine radius-\(\ell\) rotor.  The two bridge types are disjoint:
the former preserves the radius-\(\ell\) top and the latter changes it.
This contradiction proves (2.5), and (2.6) is its top/lower
specialization. \(\square\)

## 3. The multiscale carrier-run theorem

For \(0\le q\le H\), define the upper prefix

\[
 Q_q(\omega)=L+\{z_1,\ldots,z_{H+q}\}
 \in\binom{[2m]}{m+q}.
 \tag{3.1}
\]

### Lemma 3.1 (exact prefix dynamics)

A rotor always changes \(Q_q\).  A promotion of lookahead \(\ell\)
preserves \(Q_q\) if and only if \(\ell\le q\).

#### Proof

For a rotor,

\[
 Q_q(\omega')
 =Q_q(\omega)-z_{H+q}+y,
 \tag{3.2}
\]

and \(y\in R_0\) is outside \(Q_q(\omega)\).

For a promotion, if \(j\le H+q\), the letter \(z_j\) moves from the
first \(H+q\) singleton positions into \(L'\), while \(x\) moves from
\(L\) into the singleton list.  Their union is unchanged.  If
\(j>H+q\), then

\[
 Q_q(\omega')
 =Q_q(\omega)-z_{H+q}+z_j,
 \tag{3.3}
\]

and \(z_j\notin Q_q(\omega)\).  Since \(j=H+\ell\), the criterion is
exactly \(\ell\le q\). \(\square\)

In a clipped SCD, the number of chains whose tag is at least \(q\) is

\[
 \sum_{d=q}^{H-1}(N_d-N_{d+1})+N_H=N_q.
 \tag{3.4}
\]

For each such chain, \(Q_q\) is its actual rank-\((m+q)\) member.  These
\(N_q\) values are pairwise distinct.

### Theorem 3.2 (simultaneous carrier-run inequalities)

Let a spanning directed bridge-one path forest of a decorated SCD have
\(p\) paths, \(R\) rotor arcs, and \(P_\ell\) lookahead-\(\ell\) promotion
arcs.  Then, for every \(0\le q\le H\),

\[
 \boxed{
 p+R+\sum_{\ell=q+1}^{H}P_\ell\ge N_q.}
 \tag{3.5}
\]

Equivalently,

\[
 \boxed{
 \sum_{\ell=1}^{q}P_\ell\le W-N_q.}
 \tag{3.6}
\]

#### Proof

Cut every rotor arc and every promotion arc with \(\ell>q\).  By Lemma
3.1, each remaining directed run has one constant value of \(Q_q\).
There are exactly

\[
                         p+R+\sum_{\ell>q}P_\ell
 \tag{3.7}
\]

runs.  A run contains at most one tag-at-least-\(q\) state, since two such
states would be two distinct SCD chains with the same actual rank-
\((m+q)\) member.  There are \(N_q\) such states, proving (3.5).

Every path-forest arc is either a rotor or a distinct-owner promotion, so

\[
                         R+\sum_{\ell=1}^HP_\ell=W-p.
 \tag{3.8}
\]

Subtracting (3.5) from \(p+(W-p)=W\) proves (3.6). \(\square\)

The endpoint cases are informative.  At \(q=0\), (3.5) is equality because
\(Q_0=X\) is the middle owner.  At \(q=H\), all promotions preserve the
full collar top and

\[
                         R\ge N_H-p.
 \tag{3.9}
\]

This proves (0.4).

### Corollary 3.3 (fragmentation/lookahead potential)

Let \(\Delta=p+R-N_H\).  Then

\[
 \boxed{
 \Delta+\sum_{\ell>q}P_\ell\ge N_q-N_H
 \qquad(0\le q\le H),}
 \tag{3.10}
\]

and

\[
 \boxed{
 H\Delta+\sum_{\ell=1}^H\ell P_\ell
 \ge\sum_{q=0}^{H-1}N_q-HN_H.}
 \tag{3.11}
\]

#### Proof

Equation (3.9) says \(\Delta\ge0\).  Subtract \(N_H\) from (3.5) to get
(3.10), and sum it for \(q=0,\ldots,H-1\).  A lookahead-\(\ell\)
promotion is counted for exactly \(\ell\) values of \(q\). \(\square\)

Uniformly for \(q\le A\sqrt m+O(1)\),

\[
                         {N_q\over W}=e^{-q^2/m+o_A(1)}.
 \tag{3.12}
\]

Consequently (3.11) gives (0.7).  The coefficient

\[
 J(A)=\int_0^A e^{-t^2}\,dt-Ae^{-A^2}
 \tag{3.13}
\]

is positive for \(A>0\), because \(J(0)=0\) and

\[
                         J'(A)=2A^2e^{-A^2}>0.
 \tag{3.14}
\]

More locally, for fixed \(0\le\theta<1\), put
\(q=\lfloor\theta H\rfloor\).  Equation (3.10) yields

\[
 \boxed{
 \Delta+\sum_{\ell>q}P_\ell
 \ge
 \left(e^{-\theta^2A^2}-e^{-A^2}-o_{A,\theta}(1)\right)W.}
 \tag{3.15}
\]

Thus either \(\Delta=\Omega_A(W)\), meaning a linear excess of
top-changing carrier runs, or a positive density of promotions reaches a
literal distance \(\Theta(H)\) into the upper collar.

### Corollary 3.4 (the census-tight promotion coalescent)

Define the nonnegative prefix defects

\[
 \varepsilon_q=(W-N_q)-\sum_{\ell\le q}P_\ell.
 \tag{3.16}
\]

Then

\[
 \varepsilon_0=0,\qquad
 \varepsilon_H=\Delta,\qquad
 P_q=(N_{q-1}-N_q)-\varepsilon_q+\varepsilon_{q-1}.
 \tag{3.17}
\]

After deleting every rotor and every promotion edge of lookahead greater
than \(q\), exactly \(N_q\) of the remaining runs contain one
tag-at-least-\(q\) chain, and exactly

\[
                         \boxed{\varepsilon_q}
 \tag{3.17a}
\]

remaining runs contain no such chain.

If every inequality (3.6) is tight, then

\[
 \boxed{P_q=N_{q-1}-N_q=\gamma_{q-1}.}
 \tag{3.18}
\]

In this zero-defect case there is also a canonical rooted merge
coalescent.  Let \(G_q\) consist of the promotion edges of lookahead at
most \(q\), with every rotor deleted.  Each component of \(G_{q-1}\) has
one root: its unique chain of tag at least \(q-1\).  On adding the
lookahead-\(q\) edges, each new \(G_q\)-component contains exactly one
old root whose tag is at least \(q\); all its other old roots have tag
exactly \(q-1\).  Contract the old components and orient the resulting
tree toward the surviving root.  This gives a bijection

\[
 \boxed{
 \{G_{q-1}\text{-components whose unique root has tag }q-1\}
 \longleftrightarrow
 \{\text{lookahead-}q\text{ promotion edges}\}.}
 \tag{3.18a}
\]

Thus the zero-defect lower-tag structure is a literal nested promotion
coalescent with the exact SCD radius census, not merely a histogram.
What remains nonunique is the geometric realization: (3.18a) does not
force the edge paired to a tag-\((q-1)\) root to be incident with that
root vertex itself, nor does it choose any collar or packet endpoint.

#### Proof

The number of runs after the stated deletions is
\[
 p+R+\sum_{\ell>q}P_\ell
 =W-\sum_{\ell\le q}P_\ell
 =N_q+\varepsilon_q.
\]
The proof of Theorem 3.2 shows that at most one of the \(N_q\) high-tag
chains lies in each run, proving (3.17a).

If every \(\varepsilon_q=0\), the asserted unique roots exist at every
level.  The quotient of \(G_q\) by the \(G_{q-1}\)-components is a forest,
because it is a subquotient of the selected path forest.  Each of its
connected components contains exactly one root which remains high at
level \(q\).  If it contains \(k\) roots which expire at tag \(q-1\), it
has \(k+1\) old component-vertices and therefore exactly \(k\)
lookahead-\(q\) edges.  Orienting toward the surviving root pairs every
expired component with its unique parent edge.  This last orientation is
auxiliary bookkeeping and need not agree with the directed bridge
orientation.  Summing over the new components proves (3.18a). \(\square\)

### Theorem 3.5 (exact carrier quotient and long exterior-moving normal form)

Delete all rotor arcs from the selected path forest.  For each
\(U\in\binom{[2m]}{m+H}\), let \(a_U\) be the number of remaining directed
components contained in the full-top fibre \(Q_H=U\).  Then

\[
 \boxed{
 \sum_U a_U=p+R,\qquad
 \Delta=\sum_U(a_U-1).}
 \tag{3.19}
\]

Contracting each of these promotion components produces a directed path
forest with \(p+R=N_H+\Delta\) vertices, \(R\) genuine exterior-moving
rotor edges, and \(p\) paths.

Consequently, if

\[
 p=o_A(W/H),\qquad \Delta=o_A(W/H),
 \tag{3.20}
\]

then:

1. at most \(\Delta=o_A(W/H)\) top fibres are fragmented;
2. every unfragmented fibre is one promotion path containing all selected
   states assigned to that fibre, including its unique tag-\(H\) anchor;
3. the contracted rotor paths have average vertex length
   \[
       {N_H+\Delta\over p}=\omega_A(H);
       \tag{3.21}
   \]
4. all but \(o_A(W)\) of their vertices, and hence all but \(o_A(W)\)
   tag-\(H\) anchor components, lie on contracted paths having at least
   \(H+1\) vertices, and hence at least \(H\) consecutive exterior-moving
   rotor edges in the contracted quotient.  In the original path they are
   separated only by within-fibre promotion subpaths.

Thus the near-minimal recursive-packet branch really does require
genuinely long exterior-moving splices.  Deep lookahead in (3.15) alone
does not imply temporal length; the quotient conclusion (3.21) does.

#### Proof

At radius \(H\), promotions preserve \(Q_H\) and rotors change it.
Deleting the \(R\) rotor edges from a \(p\)-path forest leaves exactly
\(p+R\) directed path components, each contained in one \(Q_H\)-fibre.
Every fibre is nonempty because its rank-\((m+H)\) mask is the actual top
of one unique tag-\(H\) SCD chain.  Therefore
\[
 \sum_Ua_U=p+R,\qquad
 \sum_U(a_U-1)=p+R-N_H=\Delta.
\]
Contracting the remaining promotion components turns each deleted rotor
back into one edge.  Since contraction occurs inside the original paths,
the quotient is again a directed path forest, with the asserted census.

Each fragmented fibre contributes at least one to the second sum in
(3.19).  This proves items 1 and 2.  Equation (3.21) follows from
\(N_H=(e^{-A^2}+o_A(1))W\) and (3.20).  Finally, the \(p\) quotient paths
having fewer than \(H+1\) vertices contain at most \(Hp=o_A(W)\)
vertices altogether. \(\square\)

### Theorem 3.6 (an exact full-top promotion ring)

Put \(n=m+H\).  Fix \(U\in\binom{[2m]}n\) and a cyclic ordering
\[
                         c_0,c_1,\ldots,c_{n-1}
 \tag{3.22}
\]
of \(U\), with all indices below read modulo \(n\).  Since \(H<m\), one
has \(2H<n\).  Define
\[
 \Omega_i=
 \left(
  U\setminus\{c_i,\ldots,c_{i+2H-1}\};
  c_i,\ldots,c_{i+2H-1};
  [2m]\setminus U
 \right).
 \tag{3.23}
\]

Then the \(\Omega_i\) form a directed lookahead-\(H\) promotion cycle:
\[
                         \boxed{\Omega_i\longrightarrow\Omega_{i-1}.}
 \tag{3.24}
\]

More strongly, assign arbitrary tags
\[
                         0\le d_i\le H
 \tag{3.25}
\]
with at most one \(d_i=H\), and truncate \(\Omega_i\) to tag \(d_i\).
The resulting \(n\) saturated symmetric chains are pairwise mask-disjoint.
At rank \(m+r\), \(-d_i\le r\le d_i\), the \(i\)-th chain owns exactly
\[
 C_i(r)
 =U\setminus
   \{c_{i+H+r},c_{i+H+r+1},\ldots,c_{i+2H-1}\},
 \tag{3.26}
\]
where the deleted cyclic interval has length \(H-r\), and is empty when
\(r=H\).

Consequently one full-top fibre can carry one tag-\(H\) anchor and as many
as \(m+H-1\) arbitrarily tagged lower chains on one literal promotion
cycle.  Cutting an edge gives one promotion path through that whole local
payload.

#### Proof

The lower block in (3.23) has size \(n-2H=m-H\), and the residual block
has size \(2m-n=m-H\).  In \(\Omega_i\), choose departure \(c_{i-1}\)
from the lower block and promote the last singleton \(c_{i+2H-1}\).
Formula (1.4) gives exactly \(\Omega_{i-1}\), proving (3.24).

Central truncation of (3.23) to tag \(d_i\) gives (3.26), so it is a
saturated chain from rank \(m-d_i\) through rank \(m+d_i\), and
\(\Omega_i\) is its radius-\(H\) collar extension.  Two chains can collide
only at the same rank \(m+r\).  If \(r<H\), the deleted interval in
(3.26) is nonempty and has length at most \(2H<n\).  A proper cyclic
interval of a fixed positive length determines its starting index, so
equality of two masks forces \(i=j\).  At \(r=H\), the mask is \(U\), and
at most one selected chain has tag \(H\). \(\square\)

Theorem 3.6 proves that neither the residual-slot law nor the carrier
fragmentation identity gives a local lower-payload capacity obstruction.
The remaining issue is whether many such rings can be selected
owner-disjointly and completed to one SCD.

### Theorem 3.7 (exact exterior-moving ring splice)

Put \(s=m-H\).  Fix an ordered \((2H-1)\)-tuple
\[
                         P=(p_1,\ldots,p_{2H-1}).
 \tag{3.27}
\]
For cyclic indices \(i\in\mathbb Z/k\mathbb Z\), let
\(K_i\subseteq[2m]\setminus P\) have size \(s+1\), let
\[
 x\in\bigcap_iK_i,\qquad a_i\in K_i\setminus\{x\},
 \tag{3.28}
\]
and choose
\[
 y_i\notin P\cup K_i,\qquad
 K_{i+1}=K_i-\{a_i\}+\{y_i\}.
 \tag{3.29}
\]
Write \(U_i=P\cup K_i\), and define the two full collar states
\[
 A_i=(K_i-\{a_i\};\,P,a_i;\,[2m]\setminus U_i),
 \tag{3.30}
\]
\[
 B_i=(K_i-\{x\};\,x,P;\,[2m]\setminus U_i).
 \tag{3.31}
\]
Then
\[
 \boxed{
 A_i\longrightarrow B_i\text{ is a lookahead-}H\text{ promotion},\qquad
 A_i\longrightarrow B_{i+1}\text{ is a rotor}.}
 \tag{3.32}
\]
The rotor has departure \(x\) and exterior entry \(y_i\).

Choose the cyclic order of \(U_i\) to contain the consecutive block
\[
                         (x,p_1,\ldots,p_{2H-1},a_i).
 \tag{3.33}
\]
Then \(A_i\to B_i\) is one edge of the promotion ring in Theorem 3.6.
If \(k\) such promotion rings are pairwise mask-disjoint, deleting the
edges \(A_i\to B_i\) and inserting the rotor edges
\[
                         A_i\longrightarrow B_{i+1}
 \tag{3.34}
\]
fuses the \(k\) rings into one directed cycle without a seam or an
additional state.

There is an exact port-disjointness test independent of the unselected
ring interiors.  Give every \(A_i\)- and \(B_i\)-chain a tag below \(H\).
If the \(K_i\) are pairwise distinct and the \(K_i-\{a_i\}\) are pairwise
distinct, then all \(2k\) port chains are pairwise mask-disjoint.

#### Proof

For \(A_i\to B_i\), use departure \(x\) and promote the last singleton
\(a_i\).  For \(A_i\to B_{i+1}\), use the full rotor formula with
departure \(x\) and entry \(y_i\).  Equations (3.29)--(3.31) give
\[
 K_i-\{a_i,x\}+\{y_i\}=K_{i+1}-\{x\}
\]
for the new lower block, the new word is \((x,P)\), and the new residual
block is
\[
 ([2m]\setminus U_i)-\{y_i\}+\{a_i\}
 =[2m]\setminus U_{i+1}.
\]
This proves (3.32).  The block (3.33) embeds the two states as consecutive
windows of the ring.  After the switch, following the remainder of ring
\(i\) from \(B_i\) to \(A_i\), then (3.34), advances from ring \(i\) to
ring \(i+1\); since this permutation is one \(k\)-cycle, all rings fuse.

For the port audit, let \(P_t=\{p_1,\ldots,p_t\}\), with
\(P_0=\varnothing\).  At every common rank
\(m+r\) of two port chains, their masks have the exact forms
\[
 A_i(r)=(K_i-\{a_i\})\cup P_{H+r},\qquad
 B_i(r)=K_i\cup P_{H+r-1}.
 \tag{3.35}
\]
Here \(1\le H+r\le2H-1\), because the port tags are below \(H\).
Distinct \(K_i-\{a_i\}\) separate the \(A\)-chains, and distinct \(K_i\)
separate the \(B\)-chains.  An \(A\)-mask contains \(p_{H+r}\), whereas a
\(B\)-mask does not, so no cross-type collision is possible. \(\square\)

### Corollary 3.8 (minimal three-way and long port scaffolds)

Within the common-\((x,P)\) model of Theorem 3.7, a mask-disjoint binary
closed splice is impossible.  Indeed, closure forces
\[
 a_2=y_1,\qquad y_2=a_1,\qquad
 K_1-\{a_1\}=K_2-\{a_2\},
 \tag{3.36}
\]
so the two \(A\)-port chains collide already at their middle masks.

For \(s\ge2\), a ternary port scaffold is possible.  Choose a set \(C\)
of size \(s-1\) with \(x\in C\), and distinct \(a,b,c\) outside
\(C\cup P\).  Put
\[
 \begin{array}{lll}
 K_1=C+\{a,b\},&a_1=a,&y_1=c,\\
 K_2=C+\{b,c\},&a_2=b,&y_2=a,\\
 K_3=C+\{c,a\},&a_3=c,&y_3=b.
 \end{array}
 \tag{3.37}
\]
Both port families in Theorem 3.7 are pairwise distinct.

For \(s\ge2\), there is also an explicit \(\Theta(m)\)-long port
scaffold.  Partition
the ground set as
\[
 [2m]=P\mathbin{\dot\cup}\{x\}\mathbin{\dot\cup}
       \{v_0,\ldots,v_{2s-1}\},
\]
cyclically order the \(v\)'s, and set, modulo \(2s\),
\[
 K_i=\{x,v_i,v_{i+1},\ldots,v_{i+s-1}\},\qquad
 a_i=v_i,\qquad y_i=v_{i+s}.
 \tag{3.38}
\]
Then (3.29) holds for \(k=2s=2(m-H)\); the \(K_i\) are distinct cyclic
\(s\)-windows with \(x\) adjoined, and the \(K_i-\{a_i\}\) are distinct
cyclic \((s-1)\)-windows with \(x\) adjoined.  Thus all \(4s\) port chains
are mask-disjoint and all \(2s\) crossing rotors are literal.  The cyclic
ring order
\[
 (x,p_1,\ldots,p_{2H-1},v_i,v_{i+1},\ldots,v_{i+s-1})
\]
contains the required cut block (3.33) in every fibre.

The ternary construction certifies only the ports and crossing rotors.
For the natural long construction the full rings collide, as the next
proposition shows; Theorem 3.10 then repairs every interior collision by
one deletion per ring.

### Proposition 3.9 (the exact staircase collision in the natural long rings)

The interior caveat above is real.  Assume \(H\le s=m-H\), and give the
long scaffold (3.38) the displayed natural cyclic ring orders.  For every
\[
                 1\le t\le\min\{2H-1,s\}
 \tag{3.39}
\]
and every \(i\), the following two formal ring chains have the same mask
at rank \(m+(H-t)\):

* in ring \(i\), the chain whose omitted interval is
  \(\{v_i,\ldots,v_{i+t-1}\}\);
* in ring \(i+t\), the chain whose omitted interval is
  \(\{v_{i+s},\ldots,v_{i+s+t-1}\}\).

Their common mask is
\[
             P\cup\{x,v_{i+t},v_{i+t+1},\ldots,v_{i+s-1}\}.
 \tag{3.40}
\]
The collision is present in a tagged ring selection whenever both chains
have tag at least \(|H-t|\).  At \(t=H\), it occurs at the middle rank and
is therefore tag-independent.  Hence the natural full rings of the long
port scaffold are never mutually mask-disjoint.

#### Proof

At rank \(m+r\), Theorem 3.6 describes a ring mask as its top \(U\) with
a cyclic interval of length \(H-r\) omitted.  Put \(r=H-t\).  Removing
the first \(t\) elements of the \(v\)-window of
\[
 U_i=P\cup\{x,v_i,\ldots,v_{i+s-1}\}
\]
leaves (3.40).  The \(v\)-window of \(U_{i+t}\) runs from \(v_{i+t}\) to
\(v_{i+t+s-1}\); removing its final \(t\) elements, from \(v_{i+s}\) to
\(v_{i+s+t-1}\), leaves the same set.  A tag-\(d\) symmetric chain reaches
rank \(m+r\) exactly when \(d\ge|r|\).  For \(t=H\), \(r=0\), which every
chain reaches. \(\square\)

The displayed collisions in fact exhaust all cross-ring collisions after
the natural orders are fixed.  This gives the following exact repair.

### Theorem 3.10 (one-hole reservoir macro-packet)

Assume
\[
                         s=m-H>2H
 \tag{3.41}
\]
and use the \(2s\) long-scaffold tops and natural cyclic orders from
(3.38).  In ring \(i\), let \(D_i\) be the unique ring state whose last
singleton is \(v_{i+s-1}\), the last coordinate of its \(v\)-tail.  Delete
the entire chain \(D_i\) (equivalently, the window beginning at cyclic
position \(s\)).

Assign arbitrary tags in \(\{0,\ldots,H\}\) to every retained ring state,
subject only to at most one tag \(H\) in each ring.  Then all
\[
                         \boxed{2s(m+H-1)}
 \tag{3.42}
\]
retained truncated symmetric chains are pairwise mask-disjoint, over all
ranks and all \(2s\) rings.  Their full collar states have a directed
bridge-one cover by exactly \(2s\) promotion paths.

The port states \(A_i,B_i\) survive.  If every internal promotion edge
\(A_i\to B_i\) is replaced by the rotor \(A_i\to B_{i+1}\), the switched
macro-packet still has exactly \(2s\) directed paths, now with one literal
exterior-moving rotor in each path.

#### Proof

Write
\[
 Q=(x,p_1,\ldots,p_{2H-1}),\qquad
 T_i=(v_i,v_{i+1},\ldots,v_{i+s-1}),
\]
so the cyclic order of ring \(i\) is \((Q,T_i)\), with \(|Q|=2H<s\).
At a common rank \(m+r\), two ring masks omit cyclic intervals \(I,J\)
of the same length
\[
                         \ell=H-r,\qquad0\le\ell\le2H.
 \tag{3.43}
\]
If \(\ell=0\), the masks are the distinct tops \(U_i\).  Otherwise take
two distinct rings and, after interchanging them if necessary, write the
second index as \(i+t\) with \(1\le t\le s\).  Equality
\[
                         U_i\setminus I=U_{i+t}\setminus J
 \tag{3.44}
\]
forces
\[
 \{v_i,\ldots,v_{i+t-1}\}\subseteq I,\qquad
 \{v_{i+s},\ldots,v_{i+s+t-1}\}\subseteq J.
 \tag{3.45}
\]
Hence \(t\le\ell<s\); in particular \(t<s\).

Because \(\ell\le|Q|<s\), an \(\ell\)-interval containing the first set
in (3.45) has the form
\[
 I=\operatorname {suffix}_a(Q)\cup
   \operatorname {prefix}_b(T_i),
 \qquad a+b=\ell,\quad b\ge t,
 \tag{3.46}
\]
and an \(\ell\)-interval containing the second has the form
\[
 J=\operatorname {suffix}_c(T_{i+t})\cup
   \operatorname {prefix}_d(Q),
 \qquad c+d=\ell,\quad c\ge t.
 \tag{3.47}
\]
Equality in (3.44) on the common \(Q\)-coordinates gives
\[
                         \operatorname {suffix}_a(Q)
                         =\operatorname {prefix}_d(Q).
 \tag{3.48}
\]
Both lengths are at most \(\ell-t<2H=|Q|\).  Since the coordinates of
\(Q\) are distinct, no nonempty proper prefix equals a suffix; thus
\(a=d=0\).  It follows that
\[
 I=\operatorname {prefix}_\ell(T_i),\qquad
 J=\operatorname {suffix}_\ell(T_{i+t}).
 \tag{3.49}
\]
After the two difference sets in (3.45) are removed, equality of the
remaining \(v\)-intervals is impossible when \(\ell>t\): two proper
cyclic intervals of length \(\ell-t\) would have starting indices differing
by \(s-\ell\), forcing \(\ell=s\).  Therefore
\[
                         \boxed{\ell=t.}
 \tag{3.50}
\]

Conversely, (3.49) with \(\ell=t\) is exactly the staircase collision in
Proposition 3.9.  For fixed target ring \(j=i+t\), every interval
\(\operatorname {suffix}_t(T_j)\), \(1\le t\le2H\), is an omitted interval
of the one state \(D_j\): a ring state's omitted intervals at all its
ranks have the same last singleton.  Thus every cross-ring collision
contains one deleted chain.  Theorem 3.6 handles disjointness within a
ring, including the stated tag-\(H\) restriction, proving (3.42).

Deleting one vertex from each directed promotion cycle leaves one directed
promotion path.  Moreover \(A_i\) has last singleton \(v_i\), \(B_i\) has
last singleton \(p_{2H-1}\), and \(D_i\) has last singleton
\(v_{i+s-1}\); hence both ports and their internal edge survive.
Removing \(A_i\to B_i\) splits path \(i\) into a prefix \(L_i\) ending at
\(A_i\) and a suffix \(R_i\) beginning at \(B_i\).  Adding
\(A_i\to B_{i+1}\) concatenates \(L_i\) with \(R_{i+1}\).  These are
exactly \(2s\) directed paths, with no edge returning from an \(R\)-piece
to an \(L\)-piece. \(\square\)

If one retained state in each ring is assigned tag \(H\), the macro-packet
has
\[
 2s(m+H-2)
 \tag{3.51}
\]
lower-tag slots and \(2s\) top-tag slots.  Its component density is
\[
 {2s\over2s(m+H-1)}={1\over m+H-1}=O(1/m)=o_A(1/H).
 \tag{3.52}
\]
Thus a disjoint family of these macro-packets covering \(T\) lower-tag
chains would contribute at most
\[
 {T\over m+H-2}+2(m-H)
\]
components, including one partial terminal macro-packet: fill whole
retained ring paths and at most one contiguous subpath in each remaining
ring.  Tags may be assigned to these slots in any prescribed order.  For
\(T=\Theta_A(W)\), this is \(O_A(W/m)=o_A(W/H)\).

The remaining assertion is global and exact: select such macro-packets
mutually mask-disjoint with the prescribed aggregate tag census and with
a divisibility-safe recursive-packet/TCB backbone on the unused top mass,
treating their \(O(W/m)=o(W/H)\) used anchors as backbone exceptions.
Exact census plus pairwise disjointness then fills the central band by
Corollary 3.11.  This is an RPE-type partial packet route, not the exact
all-boundary RPE statement as originally defined.  Theorem 3.10 proves
the full local collar, bridge, owner, and component ledger, but not that
one-fold global selection theorem.
Its collision proof uses the identical ordered block
\(Q=(x,p_1,\ldots,p_{2H-1})\) in every constituent ring; independently
conjugating those blocks is outside the theorem.

### Corollary 3.11 (strict-scale lower-tag integration)

For fixed \(A\) and all sufficiently large \(m\), suppose there is one
pairwise mask-disjoint family of saturated symmetric chains in the central
band with the following two structures.

1. A mutually mask-disjoint family of full or partial one-hole reservoir
   macro-packets from Theorem 3.10 containing exactly
   \(\gamma_d=N_d-N_{d+1}\) chains of tag \(d\), for every \(d<H\), and
   exactly one tag-\(H\) anchor per nonempty promotion path.  If \(u\) is
   the number of these paths, assume they are filled except for one
   terminal macro, so
   \[
        u\le {W-N_H\over m+H-2}+2(m-H).
        \tag{3.53}
   \]
2. A genuine rotor path cover with \(p_H=o_A(W/H)\) paths on the remaining
   \(N_H-u\) tag-\(H\) chains, mask-disjoint from the first family.

Then the chosen collar states have a spanning bridge-one path cover with
\[
 p\le u+p_H
 \le {W-N_H\over m+H-2}+2(m-H)+p_H
 =o_A(W/H).
 \tag{3.54}
\]
Hence \(\mathrm{EP}_A\) holds for that SCD.

#### Proof

First, the two chain families automatically form a clipped SCD; no
separate central-band completion hypothesis is needed.  Indeed, at either
rank \(m\pm q\), the number of selected chains reaching that rank is
\[
 \sum_{d=q}^{H-1}(N_d-N_{d+1})+N_H=N_q,
\]
exactly the number of masks in the rank.  Pairwise mask-disjointness
therefore makes the selected masks a partition of every band rank.

Now use the \(u\) promotion paths and the \(p_H\) rotor paths without
joining them.  They are vertex-disjoint by hypothesis and together span
all \(W\) chains; every transition is literally bridge one.  Since
\[
 W-N_H=(1-e^{-A^2}+o_A(1))W
\]
and \(H=\Theta_A(\sqrt m)\), (3.53) gives
\(u=O_A(W/m)+O(m)=o_A(W/H)\), proving (3.54). \(\square\)

Corollary 3.11 replaces the old lower-tag two-sided-detour gate by one
precise global selection problem: pack the repaired macro-atoms inside
one pairwise mask-disjoint central-band family with the exact tag census,
while the top recursive-packet/common-base construction tolerates their
\(O(W/m)=o(W/H)\) anchor exceptions.  The exact census then supplies the
clipped-SCD completion automatically.

## 4. Common all-depth rotor support and a fixed-label no-go

Let \(\lambda_q(\mathcal D)\) be the maximum number of edges in a directed
linear forest of the radius-\(q\) rotor graph induced by the chains of tag
at least \(q\), using their forced central truncations.

### Theorem 4.1 (all-depth rotor-forest necessity)

Every bridge-one \(p\)-path cover satisfies

\[
 \boxed{
 \lambda_q(\mathcal D)\ge(2N_q-W-p)_+
 \qquad(1\le q\le H).}
 \tag{4.1}
\]

Moreover, if \(F\) is the selected full path forest and \(t(v)\) is the
tag of its vertex \(v\), then

\[
 \boxed{
 \sum_{uv\in E(F)}\min\{t(u),t(v)\}
 \ge
 \sum_{q=1}^H(2N_q-W-p)_+.}
 \tag{4.2}
\]

#### Proof

On each full path, mark vertices whose tags are at least \(q\).  Their
number is \(N_q\).  At most \(W-N_q\) lower-tag vertices and the \(p\)
path boundaries can separate their runs, so the number of high--high arcs
is at least

\[
                         2N_q-W-p.
 \tag{4.3}
\]

These arcs form a directed linear forest and, by Corollary 2.2, truncate
to genuine radius-\(q\) rotor arcs.  This proves (4.1).

An edge \(uv\) is counted as a high--high edge at exactly the depths
\(1\le q\le\min\{t(u),t(v)\}\).  Summing (4.3) over \(q\) proves (4.2).
\(\square\)

Under the EP-scale hypothesis \(p=o_A(W/H)\), the asymptotic form of
(4.2) is

\[
 \left[
  \int_0^{\min(A,\sqrt{\log2})}(2e^{-t^2}-1)\,dt
  +o_A(1)
 \right]W\sqrt m.
 \tag{4.4}
\]

Thus the recursively retained edges must be common providers across a
whole nested interval of depths.  Independent layerwise common-base
maximizers do not certify (4.2).

There is also a simple exact class obstruction.  For a tag-at-least-\(q\)
chain with forced radius-\(q\) truncation

\[
                         (D_q;c_1,\ldots,c_{2q};R_q),
 \tag{4.5}
\]

write \(Z_q=\{c_1,\ldots,c_{2q}\}\) for its unordered central
\(2q\)-label.

### Proposition 4.2 (independent-label cut)

Let \(\mathcal I\subseteq\binom{[2m]}{2q}\) have the property that no two
distinct members intersect in \(2q-1\) coordinates.  If \(M_q\) tag-at-
least-\(q\) chains have \(Z_q\in\mathcal I\), then every bridge-one path
cover has

\[
 \boxed{p\ge(2M_q-W)_+.}
 \tag{4.6}
\]

#### Proof

A radius-\(q\) rotor shift changes its central label by deleting one
coordinate and adding one, so its two labels intersect in exactly
\(2q-1\) coordinates.  Corollary 2.2 therefore forbids a bridge between
two of the marked states.  On a union of \(p\) paths, \(M_q\) marked
vertices with no marked--marked adjacency require at least \(M_q-p\)
unmarked separators.  Hence \(M_q-p\le W-M_q\), which is (4.6).
\(\square\)

Take \(\mathcal I\) to be the unions of \(q\) edges of one fixed perfect
matching \(P\).  This is an independent family of the required kind.  If
\(E_q\) of the \(N_q\) high-tag chains have labels outside this family,
then

\[
 \boxed{p\ge(2N_q-2E_q-W)_+.}
 \tag{4.7}
\]

At \(q=1\),

\[
 \boxed{
 p\ge {m-1\over m+1}W-2E_1.}
 \tag{4.8}
\]

Therefore \(\mathrm{EP}_A\) requires

\[
                         E_1\ge(1/2-o(1))W
 \tag{4.9}
\]

outside every fixed central pair frame.  Any SCD for which \(E_1=o(W)\)
relative to one fixed matching has a linear path-cover obstruction under
arbitrary radius-\(H\) collar choices.  This conclusion is stronger in scope than a
fixed-frame trace deficit: it uses the full decorated bridge graph.

## 5. The contextual atlas fails the final top-tag Hall matching

Let \(C\subseteq[2m]\) be an even anchor set of size \(d\), put

\[
                         2n=2m-d,
 \tag{5.1}
\]

and, for every \(x\subseteq C\), prescribe a perfect matching \(M_x\) on
the bulk \([2m]\setminus C\).  For a bulk set \(S\), let

\[
                         F_x(S)=\#\{e\in M_x:e\subseteq S\}.
 \tag{5.2}
\]

Consider a tag-\(H\) SCD chain

\[
                         B\subset X\subset T,
 \tag{5.3}
\]

at ranks \(m-H,m,m+H\).  Call it **frozen-context** when

\[
 B\cap C=X\cap C=T\cap C=x,\qquad
 F_x(B)=F_x(X).
 \tag{5.4}
\]

Every top-tag chain inherited from the fixed-anchor contextual atlas has
(5.4): its central collar avoids the anchor and its lower trace preserves
the number of full pairs in the matching selected by that anchor word.

For \(k=m-|x|\), define the exact source and target counts

\[
 S_{k,f}
 =\frac{n!}{f!\,(n-k+f)!\,(k-2f)!}\,2^{k-2f},
 \tag{5.5}
\]

\[
 T_{k-H,f}
 =\frac{n!}{f!\,(n-k+H+f)!\,(k-H-2f)!}\,2^{k-H-2f},
 \tag{5.6}
\]

with an invalid factorial interpreted as zero.  Put

\[
 \mu_{n,k}=\frac{k(k-1)}{2(2n-1)},\qquad
 f_x=\left\lfloor\mu_{n,k}-\frac{3H}{8}\right\rfloor,
 \tag{5.7}
\]

and

\[
 \boxed{
 D^-_{C,H}
 =\sum_{x\subseteq C}
  \left(
   \sum_{f\le f_x}T_{k-H,f}
   -\sum_{f\le f_x}S_{k,f}
  \right)_+.}
 \tag{5.8}
\]

### Theorem 5.1 (exact final-layer context Hall cut)

In every clipped SCD, the number \(E^-\) of tag-\(H\) chains which are not
frozen-context satisfies

\[
                         \boxed{E^-\ge D^-_{C,H}.}
 \tag{5.9}
\]

#### Proof

Every rank-\((m-H)\) target \(B\) is the bottom of one unique tag-\(H\)
chain.  Fix its anchor sector \(x=B\cap C\) and full-pair type
\(f=F_x(B)\).  If its chain is frozen-context, its middle owner \(X\) is a
distinct middle set in the same sector and of the same full-pair type.
There are only \(S_{k,f}\) such possible owners, whereas the number of
bottom targets of that sector and type is \(T_{k-H,f}\).

Therefore, inside the tail \(f\le f_x\), at least

\[
 \left(
  \sum_{f\le f_x}T_{k-H,f}
  -\sum_{f\le f_x}S_{k,f}
 \right)_+
 \tag{5.10}
\]

chains are not frozen-context.  The bottom sectors are disjoint, so
summing (5.10) proves (5.9). \(\square\)

### Lemma 5.2 (Gaussian evaluation)

If \(d=o(m)\), then

\[
 \boxed{
 D^-_{C,H}\ge(\delta_A-o_A(1))W,\qquad
 \delta_A=e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0.}
 \tag{5.11}
\]

For \(d=O(\log m)\), equality holds up to \(o(W)\) for the displayed tail
test.

The proof uses the following standard analytic input, imported rather
than reproved here: the bivariate lattice local central-limit theorem for
the rank/full-pair vector of \(n\) independent matching-pair states,
uniformly when the conditioned rank and the relevant full-pair threshold
differ from their means by \(O_A(\sqrt n)\).  Stirling's formula is used
in the same bounded-standard-deviation window.

#### Proof

Write \(k=n+s\), where \(s=d/2-|x|\).  Under the sector weights
\(\binom{2n}{m-|x|}\), the anchor size is the hypergeometric marginal of a
uniform middle set.  It has mean \(d/2\) and variance \(O(d)\).  Since
\(d=o(m)\), choose \(\varepsilon_m\downarrow0\) so slowly that

\[
                         {d\over\varepsilon_m^2m}\longrightarrow0.
 \tag{5.11a}
\]

Hypergeometric Chebyshev then shows that all but \(o(W)\) sector mass has
\(|s|\le\varepsilon_m\sqrt m\).

On this whole typical band, the bivariate lattice local central-limit
theorem is uniform and gives conditional standard deviation
\(\sqrt n/4+o(\sqrt n)\).  The threshold
in (5.7) is \(-3A/2+o(1)\) standard deviations from the source mean and
\(A/2+o(1)\) standard deviations from the target mean.  Also

\[
 \frac{\binom{2n}{k-H}}{\binom{2n}{k}}
 =e^{-A^2+o(1)}.
 \tag{5.12}
\]

Thus the target-tail demand minus source-tail capacity, divided by the
sector's middle mass, tends to

\[
                         e^{-A^2}\Phi(A/2)-\Phi(-3A/2).
 \tag{5.13}
\]

Discarding the atypical \(o(W)\) sector mass proves the lower bound.  When
\(d=O(\log m)\), the estimate is uniform over every sector and gives the
stated equality for this tail test.  Positivity follows from the
elementary Gaussian Chernoff bound

\[
 \Phi(-z)\le\tfrac12e^{-z^2/2}\qquad(z\ge0),
\]

which, at \(z=3A/2\), gives

\[
 \Phi(-3A/2)<\tfrac12e^{-A^2}
 <e^{-A^2}\Phi(A/2).
 \tag{5.14}
\]

\(\square\)

The Hall weight in Theorem 5.1 is literal and state-independent once the
anchor word has selected \(M_x\).  Correlating choices within this one
prescribed fixed-context state does not alter (5.9).  Independently
conjugated packet anchors do not share this Hall set and remain outside the
theorem.

## 6. Exact anchor incidence and the bounded-context RPE/TCB no-go

For a tag-\(H\) chain (5.3), call it **anchor-touching** if

\[
                         (T\setminus B)\cap C\ne\varnothing.
 \tag{6.1}
\]

### Lemma 6.1 (exact anchor-motion budget)

Every clipped SCD satisfies

\[
 \boxed{
 \sum_{B\subset X\subset T}|(T\setminus B)\cap C|
 ={dH\over m}N_H.}
 \tag{6.2}
\]

In particular, the number of anchor-touching tag-\(H\) chains is at most
\(dHN_H/m\).

#### Proof

Fix \(c\in C\).  The tag-\(H\) tops enumerate every rank-\((m+H)\) mask
once and the bottoms enumerate every rank-\((m-H)\) mask once.  Since
\(B\subset T\), the number of chains with \(c\in T\setminus B\) is

\[
 \begin{aligned}
 &\binom{2m-1}{m+H-1}
 -\binom{2m-1}{m-H-1}\\
 &\hspace{25mm}=
 \left({m+H\over2m}-{m-H\over2m}\right)N_H
 ={H\over m}N_H.
 \end{aligned}
 \tag{6.3}
\]

Sum (6.3) over the \(d\) anchor coordinates.  The final assertion is the
union bound, with multiplicity only strengthening (6.2). \(\square\)

Let \(r_C\) be the number of **anchor-avoiding** tag-\(H\) chains which
abandon the contextual matching invariant in (5.4).

### Theorem 6.2 (bounded-context packet obstruction)

For every clipped SCD,

\[
 \boxed{
 r_C\ge D^-_{C,H}-{dH\over m}N_H.}
 \tag{6.4}
\]

Consequently, if \(d=O(\log m)\),

\[
                         r_C\ge(\delta_A-o_A(1))W.
 \tag{6.5}
\]

The same conclusion holds for every even \(d=o(m/H)\), because then the
anchor-touching term in (6.4) is \(o(W)\).

If all but \(r=o(W/H)\) top-tag states in a proposed
\(\mathrm{RPE}_A^H\) or \(\mathrm{TCB}_A\) construction are inherited
from the logarithmic-anchor contextual atlas, then (6.5) is impossible.

#### Proof

Every non-frozen chain counted by Theorem 5.1 is either anchor-touching or
is counted by \(r_C\).  Lemma 6.1 bounds the first class.  This proves
(6.4), and Lemma 5.2 gives (6.5).  One exceptional top-tag state can
supply at most one additional bottom target, so \(r=o(W/H)\) exceptional
states cannot absorb the linear deficit. \(\square\)

Since

\[
                         {N_H\over W}=e^{-A^2+o_A(1)},
 \tag{6.6}
\]

under the standing hypothesis \(d=o(m)\), a construction relying only on
anchor motion and having
\(r_C=o(W)\) must satisfy

\[
 d\ge
 \left({\delta_A\over e^{-A^2}}-o_A(1)\right){m\over H}
 =(\Delta_A-o_A(1)){m\over H},
 \tag{6.7}
\]

which is (0.11).

This is a final-layer obstruction to the logarithmic-anchor candidate for
the recursive common-base theorem: its last lower endpoint matching has
\(\Omega_A(W)\) disagreement relative to the contextual forced values.  It
is also an obstruction to an RPE packing inherited from that atlas because
only tag-\(H\) SCD chains own rank \(m-H\).  Artificial radius-\(H\) collars
on lower-tag chains cannot substitute for the required actual boundary
partition.  No promotion-fibre assignment, terminal-port matching,
internal list order, or bridge-one reordering changes a tag-\(H\) chain's
actual bottom endpoint.

## 7. Consequences for the promotion-backbone programme

The exact implications are now as follows.

1. **Top-tag packet scale is not the obstruction.**  A recursive
   \(2\ell\)-packet remains an exact rotor cycle, and a divisibility-safe
   packing covering \(N_H-r\) top states gives
   \[
    p_H\le {N_H-r\over2\ell}+r.
   \]
   The obstruction is selecting a one-fold, arbitrary-frame packet family
   satisfying the boundary and recursive common-base matchings.
2. **The present contextual atlas cannot be that selection.**  Equations
   (6.4)--(6.5) force a positive-density replacement of its top-tag chains,
   before residual SCD completion is considered.
3. **Local lower-tag payload and crossing ports are available.**  Theorem
   3.6 packs \(m+H-1\) lower chains around one anchor on a single
   promotion ring.  Theorem 3.7 and Corollary 3.8 give exact crossing
   rotors and a distributed \(2(m-H)\)-port exterior-moving scaffold.  They do
   not by themselves select ring interiors; Proposition 3.9 classifies
   their exact staircase collisions, and Theorem 3.10 removes all of them
   with one chain deletion per ring, at strict \(O(1/m)\) component
   density.  Selection of many such repaired macros in one SCD is open.
4. **Lower tags require a multiscale coalescent.**  Even after an arbitrary-
   frame top backbone is constructed, (3.5)--(3.18) must hold.  In the
   zero-defect regime, the aggregate lookahead histogram equals the SCD
   radius census exactly, and (3.18a) gives a canonical tag-rooted
   component merge at every depth.  It does not identify the physical
   endpoint of the parent edge, and the coarse bounded-load assignment to
   top fibres does not impose this rooted coalescent.
5. **The exact long-splice quotient is known.**  In the
   \(\Delta=o(W/H)\) branch, Theorem 3.5 makes almost every carrier fibre
   one promotion path and contracts them to genuine rotor paths of average
   length \(\omega(H)\).  The missing theorem is the correlated selection
   of those fibre paths with the packet-prescribed entrance and exit
   states.
6. **Shallow-slot detours are insufficient.**  If
   \(\Delta=o(W)\), (3.15) forces linearly many \(\Theta(H)\)-lookahead
   promotions.  If \(\Delta=\Omega(W)\), there are instead linearly many
   excess top-changing rotor runs.  Either branch is payload-dense.  The
   first conclusion concerns collar depth, not the number of consecutive
   bridge edges in a temporal splice.
7. **All depths must use common edges.**  The weighted rotor requirement
   (4.2) is imposed on one path forest.  Separate layerwise Hall matchings
   may meet every marginal and still fail this common-provider inequality.

Thus the exact surviving positive theorem is stronger than coarse
\(\mathrm{TCB}_A\) bookkeeping plus an arbitrary top-fibre assignment:
one must choose a top packet family not overwhelmingly confined to the
frozen logarithmic atlas, together with endpoint matchings and promotion
collars realizing the common truncation forests (4.1) and the
promotion-census filtration (3.6) simultaneously.  Arbitrary-conjugate
packets and positive-density invariant-breaking fixed-anchor packets are
both still allowed.  Corollary 3.11 gives a different exact formulation
of the lower module: it suffices to select the repaired reservoir macros
and the exceptional-tolerant top backbone as one pairwise mask-disjoint
family with the exact tag census.  The central-band SCD and the strict
\(o(W/H)\) component ledger then follow automatically.

## 8. Audited implication boundary

The decisive one-hole collision classification in Theorem 3.10 was
independently rederived twice from the cyclic intervals.  Both audits
confirmed that every cross-ring collision has the deleted suffix-side
chain and that the bottom \(\ell=2H\) case is covered.  They also caught
and corrected the component scope: before the holes, the cross-switch
fuses closed rings into one cycle; after deleting the \(D_i\), the same
switch yields exactly \(2s\) paths, not one cycle.  The statements above
use the corrected form.

Proved here:

1. the exact central-truncation functor for rotor and promotion bridges;
2. the exact residual-slot law \(\ell>\min\{d,d'\}\) for promotions;
3. the simultaneous carrier-run inequalities (3.5)--(3.6);
4. the exact carrier-fragmentation identity and long rotor quotient
   (3.19)--(3.21);
5. the exact \(m+H\)-state promotion ring with arbitrary lower tags;
6. the exact exterior-moving \(k\)-splice, minimal ternary port atom, and
   \(2(m-H)\)-rotor port scaffold, together with the exact natural-ring
   staircase collision, its one-hole-per-ring repair, and the conditional
   strict-scale integration theorem;
7. the dense full-cover rotor bound \(R\ge N_H-p\) for every fixed \(A\),
   without a claim that both endpoints have tag \(H\);
8. the positive long-lookahead potential (3.11)--(3.15);
9. the exact rootless-run interpretation of every prefix defect and the
   census-tight rooted promotion coalescent;
10. the common all-depth rotor-forest requirement (4.1)--(4.4);
11. the independent central-label obstruction (4.6)--(4.9);
12. the exact final-layer contextual Hall cut (5.9);
13. the exact anchor-motion census (6.2); and
14. the resulting no-go for the logarithmic-anchor atlas as an RPE/TCB
    top-tag selector.

Not proved:

1. a universal obstruction to arbitrary-conjugate recursive packets;
2. a one-fold arbitrary-frame solution of \(\mathrm{RPE}_A^H\) or
   \(\mathrm{TCB}_A\);
3. mutually mask-disjoint global selection of the repaired reservoir
   macro-packets jointly with the top backbone and their exact aggregate
   tag census;
4. the general two-sided promotion-fibre detour/coalescent theorem for all
   lower tags (it is unnecessary if Corollary 3.11's hypotheses are
   achieved); or
5. \(\mathrm{EP}_A\) and coefficient one.

The lane is therefore closed for the logarithmic frozen-context atlas.
More generally, (6.7) applies to every \(d=o(m)\) fixed-context candidate
whose anchor-avoiding invariant-breaking class satisfies \(r_C=o(W)\);
without that hypothesis it gives no context-size lower bound.
Bounded-lookahead exterior surgery is excluded in the near-minimal-rotor
branch \(\Delta=o(W)\); the alternative is a linear excess of top-changing
rotor runs.  A surviving route may use a growing context, arbitrary-
conjugate frames, or positive-density invariant-breaking chains, and must
also meet one correlated all-depth common-base selection.  The new macro
route makes its missing gate exact: one global mask-disjoint selection
with the prescribed tag census, jointly compatible with the exceptional-
state top backbone.
