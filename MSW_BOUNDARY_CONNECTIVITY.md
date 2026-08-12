# Boundary connectivity of the MSW path factor

## 1. The theorem

For a Dyck word `x in D_m`, let `P_m(x)` be its MSW path.  Let `s_1` swap
the first two coordinates, and join roots `x,y` when some vertex of `P_m(x)`
is carried by `s_1` into `P_m(y)`.  Denote this quotient graph by
`Gamma_m^partial`.

### Theorem 1

\[
                 \Gamma_m^\partial\text{ is connected for all }m. \tag{1.1}
\]

The proof uses the spanning flippability hypergraph of
Mütze--Nummenpalo--Walczak (MNW).  Its new ingredient is an exact
decomposition of arbitrary MNW contexts into three operations that preserve
capped boundary connectivity:

1. append a Dyck suffix;
2. prepend a Dyck prefix;
3. add one non-mirrored outer primitive, \(J(x)=1x0\).

The third operation moves the apparent mirror-wrap difficulty entirely to
the finite base patterns.  Both orientations of those patterns have explicit
common-hub certificates.  The full context proof is given in
`MSW_CAP_CONTEXT_DECOMPOSITION.md`; Sections 2--3 below record the owner
identities used in it.

## 2. Exact owner recursion

Write

\[
                 \mu(w)=\overline{\operatorname{rev}(w)}.
\]

Let `o(z)` be the unique Dyck root whose MSW path contains the middle-level
word `z`.  MNW equation (8) gives three mutually exclusive cases:

\[
\begin{array}{rcll}
 z&=&1u0v, &u,v\in\mathcal D,
 \qquad o(z)=z,\\[2mm]
 z&=&1a1v, &\mu(a)\in\mathcal B, v\in\mathcal D,
 \qquad o(z)=1\mu(o(\mu(a)))0v,\\[2mm]
 z&=&0\overline u1a, &u\in\mathcal D, a\in\mathcal B,
 \qquad o(z)=1u0o(a).
\end{array}                                               \tag{2.1}
\]

For Dyck words `P,Q`,

\[
 \rho(PQ)=\rho(P)\mathbin\Vert(|P|+\rho(Q)),             \tag{2.2}
\]

and hence

\[
 P(PQ)=P(P)Q\ \mathbin\Vert\
       \overline P\bigl(P(Q)\setminus\{Q\}\bigr).       \tag{2.3}
\]

One immediate owner identity is

\[
                         o(zV)=o(z)V                       \tag{2.4}
\]

for every Dyck suffix `V`.

There is also the cap owner rule

\[
                 01z\in P(10x)
 \quad\Longleftrightarrow\quad z\in P(x).                \tag{2.5}
\]

Thus a nontrivial boundary incidence from a capped root has the form

\[
 01z\in P(10x),\qquad 10z\in P(h).                        \tag{2.6}
\]

## 3. The two proved context functors

### 3.1. Suffixes

If (2.6) holds, then by (2.3)--(2.4)

\[
 01zV\in P(10xV),\qquad 10zV\in P(hV).                   \tag{3.1}
\]

Thus `x -> xV` and `h -> hV` preserve every incidence and every connected
capped support.

### 3.2. Prefixes

Let `U` be nonempty Dyck, and write its last-primitive decomposition as

\[
                         U=V(1W0).
\]

For `b in {0,1}`, put

\[
                 \theta_b(U)=VbW0.                       \tag{3.2}
\]

For a Dyck root `h=1bR`, define

\[
                 \mathsf H_U(h)=11\theta_b(U)R.           \tag{3.3}
\]

The prefix-context theorem proved in
`MSW_PREFIX_CONTEXT_FUNCTOR.md` states

\[
 10z\in P(h)
 \quad\Longrightarrow\quad
 10\overline U z\in P(\mathsf H_U(h)).                   \tag{3.4}
\]

The final part of `P(Ux)` is `bar(U)P(x)`.  Hence (2.6) maps to

\[
 01\overline U z\in P(10Ux),\qquad
 10\overline U z\in P(\mathsf H_U(h)).                   \tag{3.5}
\]

Therefore `x -> Ux` preserves every connected capped support.  This is a
genuine left-context theorem; it does **not** follow from naively commuting
the blocks `10` and `bar(U)`.

## 4. The capped MNW theorem

Mütze--Nummenpalo--Walczak define a family \(\Psi_m\) of flippable tuples on
\(\mathcal D_m\).  The following is proved in
`MSW_CAP_CONTEXT_DECOMPOSITION.md`.

### Theorem 2 (capped MNW supports)

For every \(\psi\in\Psi_m\), the capped support

\[
                         10\operatorname{supp}(\psi)      \tag{4.1}
\]

is connected in \(\Gamma_{m+1}^{\partial}\).

Here is the structural reason.  If a context cut \(uv\) in a Dyck word has
height \(d\), there are unique Dyck excursions \(A_i,B_i\) with

\[
 u=A_0\mathbin\Vert1A_1\mathbin\Vert\cdots\mathbin\Vert1A_d,\qquad
 v=B_d\mathbin\Vert0B_{d-1}\mathbin\Vert\cdots\mathbin\Vert0B_0. \tag{4.2}
\]

Starting from the correctly oriented base support
\(A_d\mu^d(S)B_d\), repeatedly apply

\[
                 X\longmapsto A_i\mathbin\Vert J(X)\mathbin\Vert B_i,
 \qquad J(x)=1x0.                                      \tag{4.3}
\]

The result is exactly \(u\mu^d(S)v\), and
\(d\equiv |u|\pmod2\), which is precisely the parity convention in the
definition of \(\Psi\).  Dyck prefixes and suffixes preserve capped edges by
Section 3.  Literal path reversal proves that \(J\) preserves them: if

\[
 z\in P(x),\qquad10z\in P(h),
\]

then

\[
 1\bar z1\in P(J(x)),\qquad10(1\bar z1)\in P(J(h)).    \tag{4.4}
\]

Finally, the four MNW base-pattern families
\(\alpha(w),\beta,\gamma,\delta\), and their mirrors, have the explicit
common-hub certificates listed and proved in Section 5 of
`MSW_CAP_CONTEXT_DECOMPOSITION.md`.  This proves Theorem 2 without assuming
that mirror-wrapping acts functorially on individual owner paths (it does
not).

MNW Lemma 10 proves that the support hypergraph of \(\Psi_m\) has a spanning
tree.  Apply Theorem 2 to every hyperedge of such a tree.
Intersecting hyperedges have an intersecting capped root, so their connected
images glue.  Consequently

\[
                         10\mathcal D_m                  \tag{4.5}
\]

lies in one component of \(\Gamma_{m+1}^{\partial}\).

It then remains to attach roots not beginning in `10`.  Write such a root
as

\[
                         x=1u0v,\qquad u\ne\epsilon.    \tag{4.6}
\]

The last vertex of the middle piece of `P(x)` is

\[
                         1\overline u\,1v.               \tag{4.7}
\]

Since `u` is nonempty Dyck, `bar(u)` starts in zero.  Swapping the first two
coordinates of (4.7) produces a word beginning in `01`.  By (2.5), its
owner root begins in `10`.  Thus every root in (4.6) has an edge into the
component (4.5), proving (1.1) whenever \(m\ge3\).  The cases
\(\Gamma_1^\partial,\Gamma_2^\partial,\Gamma_3^\partial\) follow directly
from their one, two, and five MSW paths, respectively.  This completes the
proof of Theorem 1.

## 5. Exact component law

The suffix-local induction in `MSW_COMPONENT_HIERARCHY_REDUCTION.md`, now
using Theorem 1, gives

\[
 \#\{\text{components of size }
       \operatorname{Cat}_j+\operatorname{Cat}_{j+1}\}
   =\operatorname{Cat}_{m-j-2},
 \qquad 0\le j\le m-2.                                  \tag{6.1}
\]

The component indexed by `R in D_(m-j-2)` is

\[
 \{AR:A=1u0,\ u\in\mathcal D_{j+1}\}
 \ \dot\cup\
 \{AR:A=10\,1v0,\ v\in\mathcal D_j\}.                 \tag{6.2}
\]

Thus the Catalan hierarchy is an all-dimensional theorem, not a pattern
extrapolated from finite data.
