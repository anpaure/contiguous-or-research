# Audit of the role-recycling and complete-bipartite proposals

## Verdict

**THE LOCAL JOIN IDENTITIES PASS, BUT THE PROPOSED SUBCUBIC
LINEARIZATION FAILS AS STATED.**

The pivot blocks, the three-provider identities, and the displayed linked
bands are useful upper-shadow constructions.  The complete-bipartite normal
form is also exact as a parametrization of the relevant middle points.

However, identifying an arm role and a height role with the same alphabet
cell removes label multiplicity, not physical adjacency multiplicity.  If
all left and right stars of the proposed complete bipartite graphs are kept
in their prescribed orders, they force a cubic number of cuts or repeated
edge occurrences.  For the family in the proposal the exact lower bound is

\[
 \sum_{d=0}^{m-1}
 \bigl((d+1)(m-d)-\max\{d+1,m-d\}\bigr)
   =\frac{m^3}{6}+O(m^2).
\]

Thus the stated `o(m^3)` bipartite-star linearization lemma is impossible.
The complete-bipartite normal form is valuable because it exposes this
ordering obstruction sharply; it does not eliminate it.

There are two further scope gaps.

1. Several claimed role identifications are equalities of raw middle-point
   labels but do not lie in the domain of the alleged destination arm band.
2. A forest of band junctions does not itself imply pin survival.  One still
   needs an actually assigned, sign-correct negative parent for every linked
   negative hull, together with clean root separators and global containment
   compatibility.

No new unconditional asymptotic bound follows from the proposal.

## 1. Claims that pass

### 1.1 Pivot blocks

For

\[
 \mathcal B_j=(P_0,\ldots,P_{j-1},
 E_{j,j-1},\ldots,E_{j,0},P_{j+1},\ldots,P_R),
\]

the assignment

\[
 j=\max\{u,x+1\}
\]

does represent every rectangle `[u,r]x[0,x]`.

* If `x<u`, the interval from `E_(u,x)` to `P_r` works.
* If `x>=u`, the interval from `P_u` to `P_r` in block `x+1`
  works.

The total length is `(3R^2+R)/2`.  Every positive-height cell occurs once,
and all excess is caused by repeating the complete peak chain in every
block.  This is a clean common-chain-superposition formulation.

### 1.2 Central-square providers

With

\[
 E(c,r,x)=(c+r,m-c-x,x,m-r),
 \qquad Q(c,u,r,x)=(c+r,m-c,x,m-u),
\]

the identity

\[
 Q(c,u,r,x)=A(c,u,r)\vee B(c,u)\vee H(c,u,x)
\]

is correct on the stated domain, where

\[
 A(c,u,r)=E(c,r,u),\quad
 B(c,u)=E(c-u+1,u,u-1),\quad
 H(c,u,x)=E(c-x,x+u+1,x).
\]

The three parameter maps are injective.  The linked word consisting of a
descending `A` arm, the core `B`, and an ascending `H` arm represents every
advertised upper target.  These are genuine coordinatewise-maximum
identities in a word of middle points.

### 1.3 Raw complete-bipartite parametrization

Every cell in the relevant triangular middle surface has the unique form

\[
 e_{v,u}^{(d)}=E(d-v,u+v+1,v),
 \qquad 0\le v\le d,\quad 0\le u<m-d.
\]

For fixed `d` these labels are the edges of `K_(d+1,m-d)`, and

\[
 \sum_{d=0}^{m-1}(d+1)(m-d)=\binom{m+2}{3}.
\]

The raw equality

\[
 H(c,u,x)=A(c-x,x,x+u+1)
\]

is also correct.  What fails is the inference that every such raw role is
an active primary arm in one of the proposed valid bands; see Section 3.

### 1.4 The later `L/C/W` atlas

The displayed lower-triangle, diagonal-provider, and low-threshold words
give exact upper-join witnesses after the minor endpoint repair `v<=r` in
the diagonal theorem.  The case `v=r` is needed for targets with `x=r-1`
and the same coordinate check proves it.

These local words do not by themselves provide the physical common cores
or coordinate pins required by the global Boolean factor.

## 2. Exact complete-star ordering barrier

Consider one `K_(a,b)` with edge labels `e_(i,j)`.  Suppose every left star
must occur in its prescribed order and every right star must occur in its
prescribed order.

The left stars demand

\[
 a(b-1)
\]

directed adjacent transitions.  The right stars demand

\[
 b(a-1).
\]

The two sets of transitions are disjoint: two distinct edges of a complete
bipartite graph share at most one endpoint.  Hence there are

\[
 R=2ab-a-b
\]

distinct required transitions on `N=ab` labels.

Let `p` be the number of repeated edge occurrences and let `c` be the
number of required star adjacencies that are cut or abandoned.  The basic
transition count gives

\[
 p+c\ge R-(N-1)=(a-1)(b-1).
\]

There is an exact strengthening.  Orient the two star orders consistently;
after reversing one coordinate, their union is the directed grid
`P_a x P_b`.  Break a candidate word at every nonrequired transition.  The
remaining useful runs are directed chains covering all `ab` grid vertices.
The grid width is `min(a,b)`, so at least that many useful runs are needed.
Therefore

\[
 \boxed{p+c\ge R-N+\min(a,b)=ab-\max(a,b).}
\]

This is sharp.  If `a<=b`, concatenate the `a` complete left stars.  This
uses no repeated labels and cuts exactly all `b(a-1)=ab-b` right-star
adjacencies.  The symmetric construction handles `b<a`.

For the family `a=d+1`, `b=m-d`, summing gives

\[
 p+c\ge
 \begin{cases}
 \dfrac{h(h-1)(4h+1)}3,&m=2h,\\[2mm]
 \dfrac{h(h+1)(4h-1)}3,&m=2h+1,
 \end{cases}
 =\dfrac{m^3}{6}+O(m^2).
\]

Even the weaker transition count sums to

\[
 \sum_{d=0}^{m-1}d(m-d-1)=\binom m3.
\]

Consequently no Euler tour, ordinary edge ordering, or forest splicing can
retain both complete star foliations with `o(m^3)` total repeats and cuts.

### Scope of the barrier

This theorem refutes the complete-star lemma exactly as stated.  It does not
rule out a substantially weaker construction that retains only carefully
chosen truncated star segments, reassigns targets to different provider
systems, or uses intervals whose internal labels simultaneously replace
many demanded star adjacencies.  Any such rescue must specify the reduced
adjacency family and reprove coverage and pins; it cannot invoke the full
`K_(d+1,m-d)` star system.

## 3. Domain failure in the claimed role recycling

Equality of two raw `E` labels is not enough: the destination occurrence
must lie in the domain of a path that is actually present.

For the first central-square bands, the right side of

\[
 H(c,u,x)=A(c-x,x,x+u+1)
\]

is an active central-square `A` arm only when the new arm parameter `x`
satisfies the destination band's threshold condition.  In the first
formulation that requires `x<=c-x`; in the later diagonal formulation it
requires `x<=c-x+1`.  Neither is automatic.  For example, with `m>=8`,

\[
 H(4,1,3)=A(1,3,5)
\]

is a valid raw label identity, but the purported destination arm has
`3>1+1` and is absent from the stated diagonal-band family.

The same issue occurs in the later identity

\[
 D_{c;u,t}=A_{c-u+1;t,u+t-1}.
\]

The destination diagonal arm requires

\[
 t\le(c-u+1)+1=c-u+2,
\]

while the source permits `t` as large as `m-c`.  For instance,
`D_(4;2,6)=A_(3;6,7)` is a valid label when `m>=12`, but the destination
arm is in none of the stated `C`, `L`, or `W` path domains.

Likewise, the low-threshold equality

\[
 E(0,u,t)=A_{0;t+1,u}
\]

usually has `t+1>1`, outside the `c=0` diagonal-arm domain.  The `W` arms at
threshold zero have height zero, so they do not supply this missing role.

Thus the global assertion that every nonprimary `D`, `L`, or `H` occurrence
is already a primary `A` occurrence elsewhere is false.  The raw provider
maps remain injective, which is useful inventory information, but the
proposed path identification is not available on the full domain.

## 4. Pin survival remains conditional

Acyclicity of a band-junction graph does not imply pin survival.  On three
positions prescribe

\[
 I_X=[1,2],\ X=\{a\},\qquad
 I_Y=[2,3],\ Y=\{c\},\qquad
 I_S=[1,3],\ S=\{a,b,c\}.
\]

For coordinate `b`, the two negative intervals form a one-edge tree but
cover `[1,3]`.  Hence the positive interval `I_S` has no legal `b` pin.
Their hull is the positive interval itself, not an assigned negative
parent.

A valid merge-forest argument must explicitly supply, for every coordinate,

* an actually assigned negative parent containing every linked negative
  hull;
* clean separators between distinct negative roots; and
* global containment compatibility with all positive intervals.

The proposal states this sign-correct-parent condition in one place but
does not construct it, and the assertion that the required parents are
already selected band intervals is unproved.  The local upper-join words do
not manufacture physical lower cores or pins.

## 5. Corrected research target

The useful new information is:

1. the pivot theorem isolates a single repeated common chain;
2. the provider maps show that raw middle-point capacity is sufficient;
3. the complete-bipartite parametrization makes the transverse ordering
   conflict explicit; and
4. the local `L/C/W` words cover all advertised upper targets.

The next viable theorem cannot demand both complete star foliations.  It
must instead do at least one of the following:

* select a sparse subfamily of star adjacencies whose total ordering deficit
  is `o(m^3)` while retaining all targets;
* reassign many targets to intervals not following either complete star;
* let additional middle labels replace whole batches of transverse
  adjacencies without being charged once per cut; or
* prove a different factor construction with explicit sign-correct pins.

Until such a theorem is supplied, the justified asymptotic upper constant
does not improve.
