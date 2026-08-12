# Symmetric promotion-hinge orbit: exact degrees, the Aharoni--Haxell countercut, and the cycle-scaffold gate

**Date:** 2026-08-07  
**Status:** unconditional orbit arithmetic and exact negative scope theorem.
The flat three-owner hinge has a highly symmetric, low-codegree ideal
orbit, but target-disjointness of the flags alone does not imply a joint
hinge matching. The one-longer split hinge has only \(d\) available
endpoint holes at length \(W+d\); at length \(W+d+1\) that hole obstruction
disappears, but the packet trades its lower sidecar for an upper sidecar.
Independent flat-hinge sidecars eventually exceed the entire q1 duplicate
budget. A sidecar cycle cancels only a signed target-support ledger: it
still consumes one owner-edge q1 duplicate per hinge.

## 1. Orbit normal form

Use

\[
 n=2m+1,\qquad q=d+1,\qquad a=m-d-2.
\tag{1.1}
\]

Write

\[
 B^-=C\mathbin{\dot\cup}\{x\},\qquad
 B=C\mathbin{\dot\cup}\{y\},
\qquad |C|=d,
\tag{1.2}
\]

and take

\[
 M,\ C,\ \{u,x,y,v\}
\tag{1.3}
\]

pairwise disjoint, with \(|M|=a\). Put

\[
 R=M\mathbin{\dot\cup}C,\qquad |R|=m-2.
\tag{1.4}
\]

The set-valued resources of the flat hinge are

\[
\begin{array}{c|c}
\text{resource}&\text{value}\\ \hline
\text{flag bottom/top}&M,\quad U=M+u\\
\text{owners}&T_-=R+u+x,\quad T_0=R+u+y,\quad T_+=R+y+v\\
\text{lower/coatom}&I_-=R+u,\quad Y=R+y\\
\text{upper}&J_-=R+u+x+y,\quad J_+=R+u+y+v .
\end{array}
\tag{1.5}
\]

All three owners, both lower values, and both upper values are distinct.
The internal ordered source partition of \(M\) is suppressed below. If a
full saturated flag chain is fixed, it fixes those internal letters. If it
is not fixed, every orbit count is multiplied by the corresponding common
number of ordered covers of \(M\), without changing any normalized load.

Put

\[
 c_0=\binom{m-2}{d},\qquad N=m+d+2.
\tag{1.6}
\]

## 2. Exact one-point degrees

### Theorem 2.1 (orbit and typed resource degrees)

The number of labelled flat-hinge embeddings is

\[
 \boxed{
 E=\binom n{m-2}c_0(m+3)_4
   =\frac{n!}{a!\,d!\,(m-1)!}.}
\tag{2.1}
\]

For one fixed flag \(f=(M,u)\), the number of completions is

\[
 \boxed{
 D_F=\binom Nd(m+2)_3.}
\tag{2.2}
\]

For one fixed resource value in one specified slot, the degrees are

\[
 \boxed{
 D_O=c_0(m)_2(m+1)_2}
\tag{2.3}
\]

for each of \(T_-,T_0,T_+\),

\[
 \boxed{
 D_L=c_0(m-1)(m+2)_3}
\tag{2.4}
\]

for each of \(I_-,Y\), and

\[
 \boxed{D_U=D_O}
\tag{2.5}
\]

for each of \(J_-,J_+\).

In particular the predecessor sidecar \(I_-\) and successor coatom \(Y\)
have the same exact orbit degree.

#### Proof

Choose \(R\), then \(M\subset R\), then the ordered labels
\((u,x,y,v)\) outside \(R\), giving (2.1).

For a fixed \((M,u)\), choose \(C\) from the \(N\) coordinates outside
\(M+u\), then choose the ordered distinct labels \(x,y,v\) outside
\(M+C+u\), giving (2.2).

For a fixed owner in a specified slot, choose the two ordered active labels
inside it, choose \(M\) inside the remaining rank-\((m-2)\) base, and
choose the two ordered exterior labels. This gives (2.3). For a fixed
lower value, choose its distinguished active label, split the remaining
rank-\((m-2)\) base into \(M,C\), and choose three ordered exterior labels,
giving (2.4). For a fixed upper value, choose its three ordered active
labels, split the base, and choose the remaining exterior label; the result
simplifies to (2.5). \(\square\)

If resource slots are forgotten, a fixed rank-\(m\) owner has degree at
most \(3D_O\), a fixed rank-\((m-1)\) lower value at most \(2D_L\), and a
fixed rank-\((m+1)\) upper value at most \(2D_U\).

## 3. Exact principal pair-codegrees

The following table uses typed slots and assumes the displayed pair has the
required Johnson distance. Incompatible pairs have codegree zero.

\[
\begin{array}{c|c}
\text{fixed typed pair}&\text{codegree}\\ \hline
(T_-,T_0)\text{ or }(T_0,T_+)&c_0(m)_2\\
(T_-,T_+)&4c_0\\
(I_-,Y)&c_0(m+1)_2\\
(J_-,J_+)&c_0(m)_2\\
(f,I_-)&(m+2)_3 .
\end{array}
\tag{3.1}
\]

The largest pair-codegree between two nonflag resource vertices occurs for
a nested lower--owner pair, for example \(I_-\subset T_-\) or
\(I_-\subset T_0\):

\[
 \boxed{
 \lambda_{\max}
 =c_0(m-1)(m+1)_2.}
\tag{3.2}
\]

Consequently

\[
 \frac{\lambda_{\max}}{D_L}=\frac1{m+2},
\qquad
 \frac{\lambda_{\max}}{D_O}=\frac1m.
\tag{3.3}
\]

Thus the symmetric orbit has worst normalized resource codegree
\(O(m^{-1})\). Same-rank pair codegrees are \(O(m^{-2})\) after
normalization.

#### Proof

For an adjacent owner pair, its intersection and two exchanged labels are
fixed. Choose the distinguished label inside the intersection, split the
remaining base into \(M,C\), and choose the one remaining exterior label.
This gives \(c_0(m)_2\). The nonadjacent owner pair fixes the base and
leaves two orders on each two-element difference, giving \(4c_0\).

For \(I_-,Y\), their intersection is \(R\), their two active labels are
fixed, and \(x,v\) are an ordered exterior pair, giving
\(c_0(m+1)_2\). The upper pair is analogous. For \((f,I_-)\), the set
\(C=I_-\setminus U\) is fixed and only \(x,y,v\) remain.

Finally, a nested lower--owner pair leaves the distinguished label
\(u\) at \(m-1\) positions, the split \(R=M\dot\cup C\), and two ordered
exterior labels. Every other typed resource pair fixes at least as many
active labels, proving (3.2). \(\square\)

## 4. What target-disjointness gives, and what it does not

Let \(\mathcal X\) be a target-disjoint flag bank: its \(M\)-targets and
\(U\)-targets are both distinct. Set

\[
 \Delta_*=\binom{m-1}{d}(m+2)_3.
\tag{4.1}
\]

For one fixed sidecar value \(I\), at most
\(\binom{m-1}{d}\) flags of \(\mathcal X\) have \(U_f\subset I\), and
each such flag has exactly \((m+2)_3\) completions with sidecar \(I\).
The corresponding bounds for one typed coatom, owner, or upper value are
no larger than \(\Delta_*\). After forgetting slots, every resource value
has load at most \(3\Delta_*\).

Moreover,

\[
 \boxed{
 \rho_H:=\frac{D_F}{\Delta_*}
 =\frac{\binom{m+d+2}{d}}{\binom{m-1}{d}}
 \longrightarrow e^{\pi/4}.}
\tag{4.2}
\]

Represent one hinge completion by the seven resource vertices in (1.5):
three owners, two lower values, and two upper values. A maximal-matching
argument in the union of the colour classes gives only

\[
 \nu\ge\frac{|\mathcal X|D_F}{7\cdot3\Delta_*}
 =\frac{\rho_H}{21}|\mathcal X|.
\tag{4.3}
\]

The graph/hypergraph Aharoni--Haxell criterion would require

\[
 \nu>7(|\mathcal X|-1).
\tag{4.4}
\]

Thus the symmetric degree table cannot certify Aharoni--Haxell:
the degree-ratio route would require \(\rho_H>147\), whereas
\(\rho_H\to e^{\pi/4}=2.19328\ldots\).

This is a failure of that sufficient estimate, not yet a no-go for the
small rephased bank. There is, however, an exact large-bank countercut.

### Theorem 4.1 (target-disjointness alone is insufficient)

For all sufficiently large optimal parameters, there is a target-disjoint
flag bank of size greater than \(W/3\). No such bank has a
resource-disjoint flat-hinge embedding.

#### Proof

The inclusion graph from rank \(a\) to rank \(a+1\) has a matching
saturating the smaller rank-\(a\) shore. Hence there is a target-disjoint
flag bank of size

\[
 \binom na.
\]

The local central limit ratio is

\[
 \frac{\binom n{m-d-2}}{\binom nm}
 \longrightarrow e^{-\pi/4}>\frac13.
\tag{4.5}
\]

Every flat hinge consumes three distinct rank-\(m\) owners. Since there
are only \(W=\binom nm\) owners, a resource-disjoint hinge bank has size at
most \(W/3\). \(\square\)

The same bank also gives an exact countercut to a universal
Aharoni--Haxell assertion: for
\(|\mathcal X|>W/21+1\), the owner shore gives
\(\nu\le W/3<7(|\mathcal X|-1)\).

The actual adaptive rephased bank has density about
\(1.3949\cdot10^{-5}W\), so it lies far below this owner-capacity cut.
Its ideal joint matching remains open; target-disjointness by itself is
not the missing theorem.

### Marginal Rado rows do pass separately

The sidecar marginal alone is not obstructed. A flag top
\(U_f\) may choose any rank-\((m-1)\) superset \(I_f\). The Boolean
inclusion graph from rank \(m-d-1\) to rank \(m-1\) has normalized
matching, so every target-disjoint \(U\)-bank has a matching to distinct
sidecars. Independently, the complete prospective coatom--owner family has
the previously proved ideal rainbow matching when its degree ratio exceeds
two.

These are two different Rado/Hall projections. They do not use the same
\(C=I_f\setminus U_f\), nor do they select the two outer owners and upper
colours. Theorem 4.1 proves that no theorem may infer their common
intersection from target-disjointness alone. For the actual small bank, the
remaining ideal statement is precisely a common-base/common-transversal
problem across these marginal rows.

## 5. Split versus flat capacity

The one-longer split hinge makes its predecessor lower-q1 colour literal,
but its length-\((d+1)\) window at the split endpoint has rank \(m-1\).
At exact length \(W+d\), the endpoint-hole theorem therefore permits at
most

\[
 \boxed{d}
\tag{5.1}
\]

distinct split hinges. A \(\Theta(W)\)-sized promotion bank at exact
length \(W+d\) cannot use that realization.

This bound must not be transported to length \(W+d+1\). There a selected
middle witness may have length \(d+2\), so the split predecessor owner can
occupy the formerly missing endpoint. However, its predecessor upper colour
\(J_-\) spans \(d+3\) source positions, while selected rank-\((m+1)\)
witnesses at length \(W+d+1\) have length at most \(d+2\). Thus

\[
 \boxed{
 \text{flat at }B+1:\ 1\text{ lower sidecar, }0\text{ upper};
 \qquad
 \text{split at }B+1:\ 0\text{ lower, }1\text{ upper}.}
\tag{5.1a}
\]

The split is a sidecar transfer, not a complete local closure.

The flat hinge preserves the rank-\(m\) row but exports one q1 sidecar.
For a linear one-copy owner path, the total number of q1 edge occurrences
in excess of the complete rank-\((m-1)\) palette is

\[
\begin{aligned}
 S_{q1}
 &=(W-1)-\binom n{m-1}\\
 &=\boxed{\frac{2W}{m+2}-1}.
\end{aligned}
\tag{5.2}
\]

For a cyclic owner factor the final \(-1\) is absent. Hence

\[
 S_{q1}=\Theta(W/m).
\tag{5.3}
\]

If the promoted bank has \(H\sim\eta W\) for a fixed
\(\eta>0\), then

\[
 \frac{S_{q1}}H\sim\frac{2}{\eta m}\longrightarrow0.
\tag{5.4}
\]

Thus independent payment of one q1 sidecar per flat hinge also fails
asymptotically. Moreover, a cycle of flat hinges does not evade this
one-copy palette count: every cycle coatom \(Q_i\) colours two owner edges,
so a cycle bank of \(H\) hinges has duplicate excess \(H\). Therefore

\[
 \boxed{H\le \frac{2W}{m+2}+O(1)}
\tag{5.5}
\]

whenever the global owner row requires a one-copy lower-q1 palette.
Cycle cancellation still proves named target support, but not zero
occurrence-level palette cost.

## 6. Three-cycle cancellation scaffold

The smallest nonduplicating cancellation packet has length three. Choose

\[
 R\in\binom{[n]}{m-2}
\]

and ordered distinct labels \(x,y,z\notin R\). Put

\[
 Q_x=R+x,\qquad Q_y=R+y,\qquad Q_z=R+z.
\tag{6.1}
\]

The directed cycle

\[
 Q_x\longrightarrow Q_y\longrightarrow Q_z\longrightarrow Q_x
\tag{6.2}
\]

has distinct middle-owner union colours

\[
 R+x+y,\qquad R+y+z,\qquad R+z+x.
\tag{6.3}
\]

At vertex \(x\), any flag \((M_x,x)\) with
\(M_x\in\binom R a\) is eligible, and similarly at \(y,z\). Put again
\(c_0=\binom{m-2}{d}\).

The number of oriented scaffolds is

\[
 \binom n{m-2}(m+3)_3.
\tag{6.4}
\]

A fixed flag has, in one specified cycle slot, degree

\[
 \boxed{
 D_\triangle=\binom{m+d+2}{d}(m+2)_2.}
\tag{6.5}
\]

If the three selected \(M\)-targets must be distinct, one complete
flagged triangle has orbit size

\[
 \boxed{
 E_\triangle
 =\binom n{m-2}(m+3)_3(c_0)_3,}
\tag{6.6}
\]

and a fixed flag has untyped degree

\[
 \boxed{
 3\binom{m+d+2}{d}(m+2)_2(c_0-1)_2.}
\tag{6.7}
\]

For two fixed distinct flags \(f=(M,u)\), \(g=(M',u')\), assigned to two
specified slots, write \(s=|M\cup M'|\). Their codegree is zero unless

\[
 u,u'\notin M\cup M',\qquad s\le m-2.
\tag{6.8}
\]

When (6.8) holds it is

\[
 \boxed{
 \binom{n-s-2}{m-2-s}(m+1).}
\tag{6.9}
\]

The worst case for distinct \(M,M'\) is \(s=a+1\), giving

\[
 \binom{m+d}{d-1}(m+1).
\tag{6.10}
\]

In the full flagged-triangle hypergraph, the corresponding worst pair
codegree is

\[
 6\binom{m+d}{d-1}(m+1)(c_0-2),
\tag{6.10a}
\]

because the two flags may occupy any ordered pair of cycle slots and the
third \(M\)-target may be any of the other \(c_0-2\) subsets of \(R\).
Relative to the flag degree (6.7), this is exactly

\[
 \boxed{
 \frac{2d}
 {(m+d+2)(m+d+1)(c_0-1)}.}
\tag{6.10b}
\]

Thus the symmetric triangle orbit itself has ample degree and extremely
small compatible-pair codegree. Compatibility, however, is not automatic.

### Theorem 6.1 (far-core countercut to cycle cancellation)

If a flagged-coatom arc \(i\to j\) exists, then necessarily

\[
 |M_j\setminus M_i|\le d+1.
\tag{6.11}
\]

Consequently there are target-disjoint flag banks whose flagged-coatom
digraph has no arcs and hence no sidecar-cancelling cycle cover.

#### Proof

For an arc \(i\to j\), the rank-\((m-2)\) set

\[
 Q_i\setminus\{u_i\}
\]

contains \(M_i\), so it has only \(d\) positions outside \(M_i\).
The next coatom is obtained by adjoining one label:

\[
 Q_j=(Q_i\setminus\{u_i\})\cup\{b\}.
\]

Since \(M_j\subset Q_j\), at most \(d+1\) members of \(M_j\) lie outside
\(M_i\), proving (6.11).

Choose three rank-\(a\) sets \(M_i\) with every ordered difference larger
than \(d+1\), and choose distinct \(u_i\) outside their union. This is
possible for all sufficiently large parameters. Match each \(M_i\) to
\(U_i=M_i+u_i\). The flags are target-disjoint, but (6.11) excludes every
arc between distinct flags. \(\square\)

Therefore the exact positive input for cycle cancellation is not
target-disjointness. It is a near-diagonal decomposition of the flag bank
into compatible triples or longer cycles, together with rainbow edge-union
colours.

## 7. Two scope gates after algebraic cycle cancellation

Cycle cancellation is exact for **named target coverage**, but it does not
make the owner-edge lower palette rainbow. Every cycle vertex \(Q_i\)
appears on two set-theoretic owner edges: once as a predecessor colour and
once as a successor colour. Thus a global theorem which requires every
rank-\((m-1)\) owner-edge colour exactly once must obey (5.5), fuse away one
of the two edges, or move to an architecture where the immediate palette is
not a one-copy owner-edge row.

There is also a physical endpoint constraint. If hinge \(i\to j\) has
flag endpoint \(e_i\), its successor source letter must contain \(u_j\).
The penultimate suffix interval of flag \(j\) omits \(u_j\). Hence

\[
 \boxed{\delta(e_i,e_j)\ge d}
\tag{7.1}
\]

in directed cyclic distance. Three synchronized triangle endpoints
therefore require cyclic span at least \(\lceil3d/2\rceil\). This does not
force additive cost per triangle in one large shared chronology, but it
rules out constant-span local concatenation.

After endpoint placement, literal coexistence is exactly the
coordinatewise cover-free condition: for every coordinate, each prescribed
positive interval must contain an owner-allowed position outside the union
of all prescribed negative intervals for that coordinate. The orbit
degrees do not imply this condition.

## 8. Final boundary

The symmetric orbit proves that the local hinge is not scarce:
all one-point degrees are large and all normalized pair-codegrees are
\(O(1/m)\). It does not prove the global factor.

The proof-safe alternatives from these packets are now:

1. **flat, externally routed:** prove a joint seven-resource matching for
   the actual small flag bank and separately route its sidecars;
2. **flat, cycle-cancelled:** prove a near-diagonal flagged-coatom cycle
   packing satisfying (6.11), then either fuse one duplicate edge per
   hinge or abandon the one-copy q1 edge-palette invariant;
3. **split:** usable only for \(O(d)\) exceptional flags at exact length
   \(W+d\); at \(W+d+1\) it exports one upper sidecar per hinge.

None of the three, without an additional fusion or palette trade, supplies
a positive-density promotion bank with a complete one-copy immediate
palette.
