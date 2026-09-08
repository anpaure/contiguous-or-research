# Thirteen universal ports close the native MSW common-history arborescence

**Date:** 2026-08-14  
**Status:** unconditional symbolic theorem after independent hostile audit;
see
`MATH_AUDIT_THIRTEEN_UNIVERSAL_PORTS_COMMON_HISTORY_ARBORESCENCE_20260814.md`.  
**Inputs:**
`MATH_THEOREM_MSW_HIGHEST_VALLEY_FOUR_PACKET_MONOTONE_CONNECTIVITY_20260813.md`
and
`MATH_THEOREM_COALESCED_MULTIINCIDENCE_COMMON_HISTORY_EULER_FUSION_20260814.md`

## 0. Statement

Let

\[
 n=2m+1,\qquad 1\le d<m,
\]

and suppose

\[
 \boxed{n\ge 13(d+1).}                              \tag{0.1}
\]

In particular, (0.1) implies \(m\ge3d+1\), so the highest-valley
four-packet theorem is available.

For every nonmountain Dyck root, choose a highest valley and then the
case-selected area-increasing parent used in the residue proof: `01` when
\(L=Q=0\), `001` when \(L>0,Q=0\), `011` when \(L=0,Q>0\), and `0011`
when \(L,Q>0\). Then all chosen
edges admit a simultaneous coalesced separated-port realization in their
canonical MSW orientations. Consequently all native tight MSW component
source circuits fuse into one cyclic source word, with zero added source
positions, preserving the complete occurrence-labelled literal source deck
through width \(d+1\).

In particular, the complete rank-\(R\) owner ledger and every strict-lower
compiler cell supported on a source interval of width at most \(d\) survive
the fusion exactly.

The proof uses thirteen fixed starts, independent of the Dyck root and of
the chosen parent edge. No recursive boundary state, Proskurowski--Ruskey
path, packet-universal parent cut, or finite CSP is needed.

## 1. Six moved tight positions give twelve bad cut positions

Fix one case-selected highest-valley packet edge. In the notation of the
four-packet theorem, let \(\pi\) be its old-to-new flip-position
permutation. For the four selected cases, the numbers of nonfixed flip
positions are respectively at most

\[
 4,\quad 5,\quad 5,\quad 6.                         \tag{1.1}
\]

Here the bounds for `001` and `011` use respectively \(Q=0\) and \(L=0\),
exactly as stated in the packet theorem. They are not bounds for those packet
types outside their selected residue cases.

The sole direct-`0011` exception is
\((L,Q,O)=(d,d,d-1)\), where \(m=3d+1\) and \(n=6d+3\). It cannot occur
under (0.1), because \(6d+3<13(d+1)\). Hence every selected edge in the
present parameter range has the claimed direct packet.

Context transport only translates or reverses this permutation and inserts
fixed positions. Hence, globally,

\[
 |\operatorname{supp}(\pi-\mathrm{id})|\le 6.       \tag{1.2}
\]

Let

\[
 s=m+1-d,
 \qquad
 \iota(z)=2^{-1}z\pmod n,
\]

and define

\[
 C_e=\iota(\operatorname{supp}(\pi-\mathrm{id})),
 \qquad
 \mathcal B_e=C_e\cup(C_e-(s-1)).                  \tag{1.3}
\]

Here (1.3) is indexed in the two endpoints' **global canonical source
orientations**, not in a separately reoriented local packet.  Explicitly,
write their canonical flip orders as \(\rho_u,\rho_v\), with

\[
 \rho_v(r)=\rho_u(\pi(r)),
 \qquad
 w^u_j=\rho_u(2j),\quad w^v_j=\rho_v(2j).
\]

If \(q_j\) is the old tight position occupying new tight position \(j\),
then

\[
 q_j=\iota(\pi(2j)),
 \qquad
 w^v_j=w^u_{q_j}.                                  \tag{1.4}
\]

Thus the affected **source starts** are exactly
\(C_e=\operatorname{supp}(q-\mathrm{id})\).  No endpoint-dependent
rotation or reflection is made after this calculation.  The dihedral
context transport has already been absorbed into the actual global
permutation \(\pi\); it preserves the support bound but may move the bad
positions themselves.

The direct-cut lemma from the four-packet theorem says that a cyclic start
\(a\) is a same-start direct common-history cut whenever

\[
 I_a:=\{a,a+1,\ldots,a+d-1\}
 \quad\hbox{satisfies}\quad
 I_a\cap\mathcal B_e=\varnothing.                  \tag{1.5}
\]

Indeed, avoidance of \(C_e\) fixes the first endpoint source positions
\(a+j\), while avoidance of \(C_e-(s-1)\) fixes the second endpoint source
positions \(a+s-1+j\).  Hence the *same numerical source start* \(a\) in
the two canonical endpoint rows gives

\[
 F_j(u,a)=F_j(v,a)\qquad(0\le j<d).                 \tag{1.6}
\]

By (1.2),

\[
 \boxed{|\mathcal B_e|\le 12.}                     \tag{1.7}
\]

This bound is uniform in the root, context, packet type, and exterior
semilength.

## 2. A fixed thirteen-port hitting argument

Put

\[
 a_t=t(d+1)\pmod n,
 \qquad 0\le t\le 12,                              \tag{2.1}
\]

and let \(I_t=I_{a_t}\). Condition (0.1) says that the thirteen intervals
\(I_t\) are pairwise disjoint on the cyclic position circle and that every
two consecutive intervals have at least one unused position between them,
including across the cyclic wrap.

### Lemma 2.1 (one universal port is direct for every packet edge)

For every selected packet edge \(e\), at least one of the thirteen starts
\(a_t\) is a same-start direct common-history cut.

#### Proof

If all thirteen starts were bad, every disjoint interval \(I_t\) would
contain at least one point of \(\mathcal B_e\). The witnesses would be
distinct, so \(|\mathcal B_e|\ge13\), contradicting (1.7). Thus some
\(I_t\) avoids \(\mathcal B_e\), and (1.5) gives the direct cut. \(\square\)

Assign each selected edge to one such start, for example the least possible
\(t\). An edge assigned to \(a_t\) has, at its two endpoints \(u,v\),

\[
 F_j(u,a_t)=F_j(v,a_t)\qquad(0\le j<d).             \tag{2.2}
\]

Use this common forced word as its literal edge history.

## 3. Unlimited incidences coalesce at each of the thirteen starts

Fix a row \(v\) and a start \(a_t\). Every selected edge incident with
\(v\) and assigned to \(a_t\) requests the same word

\[
 (F_j(v,a_t))_{0\le j<d}.                           \tag{3.1}
\]

Therefore all such incidences form one jointly feasible port class. The
multiway union/intersection test is automatic: at every offset its forced
union is exactly \(F_j(v,a_t)\), and this lies in the maximal letter of
every incidence at that same row-start.

Equality is also transitively consistent across the component graph. Along
an edge, (2.2) identifies the two endpoint words; at a reused row-start,
(3.1) identifies all incident edge words. Thus every generated history
class has one literal word. More explicitly, an edge is assigned one fixed
index \(t\) at both endpoints, and coalescence only joins incidences with
the same \(t\).  The thirteen residues \(a_t\) are distinct modulo \(n\),
because \(0\le a_t\le12(d+1)<n\).  Hence equality across an edge and
equality inside a row port both preserve \(t\), so \(t\) is constant on
every transitive history class.  In particular, no generated class can
force equality between two distinct starts.  At each row its word is
\((F_j(v,a_t))_{j<d}\), while every direct edge identifies its two endpoint
words. This also verifies the full multiway condition: the forced union is
this common word and it lies in every endpoint maximal letter.

The only distinct physical starts used at a row belong to

\[
 \{a_0,a_1,\ldots,a_{12}\}.                        \tag{3.2}
\]

They have cyclic distance at least \(d+1\), so their length-\(d\) source
blocks are disjoint and separated by an unaltered source position. This is
exactly the separated-port hypothesis of the coalesced common-history Euler
theorem. Notice that the degree of the row in the selected component graph
is irrelevant: arbitrarily many incidences may reuse one physical start.

## 4. Proof of the theorem

The highest-valley four-packet theorem and the preceding case rule give every
nonmountain root a parent of strictly larger area. Iterating these choices yields an arborescence to
the mountain root. In particular, the selected component graph is connected.

Orient every native MSW row canonically. By Lemma 2.1, assign every
arborescence edge one of the thirteen direct starts. Section 3 verifies one
global row orientation, joint feasibility of every coalesced class,
transitive history consistency, and separation of every pair of distinct
classes. The coalesced multi-incidence common-history Euler theorem now fuses
all component source circuits into one cyclic source word with no added
positions.

That theorem preserves every occurrence-labelled de Bruijn edge and hence
the complete literal source deck through width \(d+1\). The owner row is the
width-\(d+1\) deck, while every strict-lower compiler cell in scope uses
width at most \(d\). Both ledgers therefore survive exactly. \(\square\)

## 5. Target-regime consequence and exact scope

The deadline regime has \(d=O(\sqrt m)\). Hence (0.1) holds for every
sufficiently large \(m\). The native MSW common-history chronology gate is
therefore closed asymptotically by a constant thirteen-port alphabet.

This theorem does **not** assert preservation or creation of proper-upper
source intervals of width greater than \(d+1\). The independently audited
absolute upper-portal obstruction shows that common-history fusion alone
cannot do so. An owner-changing upper actuator remains necessary. The theorem
also does not supply the terminal opening cap or compile unrelated protected
ticket banks. Its exact contribution is the global owner/strict-lower source
serialization that had previously been left as the all-parameter
coalesced-port CSP.
