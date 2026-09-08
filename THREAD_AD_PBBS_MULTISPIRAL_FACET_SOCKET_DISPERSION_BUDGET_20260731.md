# PBBS/multi-spiral facet-socket incidence and the wedge-budget obstruction

Date: 2026-07-31  
Lane: AD, general mathematics  
Status: exact incidence and counting theorems; conditional interface only.
No PBBS socket-expansion theorem is claimed.

## 1. Setting

Let \(F\) be a spanning directed cycle factor of \(J(k,r)\), with simple
components \(C_1,\ldots,C_b\) of length at least three.  The components are
vertex-disjoint.  For a
wedge centre \(A\in C_d\), write its two neighbours as \(L_A,R_A\) and put

\[
 U_A=L_A\cup A=A\cup R_A,\qquad |U_A|=r+1.       \tag{1.1}
\]

Let \(Z_d\) be the set of wedge centres in \(C_d\).  A signed opening at
\(A\) chooses either \(L_A\) or \(R_A\) as its service/start facet.  Thus
each wedge centre gives two opening vertices.  The endpoint of either
opening is \(A\).

All multiplicities below are in this signed option graph.  If the two
orientations at a centre are identified, the corresponding multiplicity is
the unsigned facet-incidence count rather than four times that count.

For distinct component colours \(c,d\), define the directed facet-incidence
number

\[
 I_{cd}=\#\{(B,A)\in Z_c\times Z_d:B\subset U_A\}. \tag{1.2}
\]

This is directed: in general \(I_{cd}\ne I_{dc}\).

Residence, lower-q1 colour restitution, and the lower compiler are not part
of this note.

## 2. Exact socket multiplicity

### Theorem 2.1 (four arcs per cross-component facet incidence)

Let \(c\ne d\).  The number of directed facet-socket arcs from signed
openings of \(C_c\) to signed openings of \(C_d\) is exactly

\[
                         4I_{cd}.                   \tag{2.1}
\]

For a fixed destination wedge centre \(A\), the number of possible
predecessor wedge centres on other components is

\[
 p(A)=\left|\left(\binom{U_A}{r}\cap
                    \bigcup_{c\ne d}Z_c\right)\right|\le r-2. \tag{2.2}
\]

Consequently

\[
 \sum_{c\ne d}I_{cd}\le (r-2)|Z_d|.               \tag{2.3}
\]

#### Proof

Take \((B,A)\) counted by \(I_{cd}\).  Both service facets
\(L_A,R_A\) belong to \(C_d\), whereas \(B\in C_c\); hence \(B\) is
distinct from either service facet.  Since \(B\) and the selected service
facet are two distinct \(r\)-facets of the same \((r+1)\)-set \(U_A\),
their union is \(U_A\).  This is exactly the facet-socket equation.
There are two source orientations at \(B\) and two destination orientations
at \(A\), giving four arcs.  Conversely, the socket equation forces the
source endpoint \(B\) to be an \(r\)-facet of \(U_A\), so every arc arises
this way.

The three distinct facets \(A,L_A,R_A\) of \(U_A\) all lie in \(C_d\).
Only the other \((r+1)-3=r-2\) facets can be vertices of other components.
This proves (2.2), and summing it over \(A\in Z_d\) proves (2.3).  \(\square\)

If \(s(B)\in\{0,1,2\}\) is the number of signed openings at \(B\) whose
cut carries a declared safe-root label, then the number of safe-root arcs
from \(C_c\) to \(C_d\) is exactly

\[
 2\sum_{\substack{B\in Z_c,\ A\in Z_d\\B\subset U_A}}s(B).       \tag{2.4}
\]

The factor two in (2.4) is the free choice of destination orientation.

### Corollary 2.2 (equivariant orbit compression)

Let \(k=2m+1\), \(r=m+1\), and let cyclic coordinate rotation preserve
both \(C_c\) and \(C_d\) setwise.  Then

\[
                         k\mid I_{cd}.              \tag{2.5}
\]

Writing \(I_{cd}=k j_{cd}\), the integer \(j_{cd}\) is the true quotient
socket multiplicity.  The \(4k\) physical arcs supplied by one quotient
incidence all join the same ordered pair of component colours and therefore
do not by themselves give colourful expansion.

#### Proof

Rotation acts on the incidence pairs in (1.2).  Its action is free because
it is free on rank-\(r\) subsets: if a nonidentity rotation fixed an
\(r\)-set, then \(r\) would be divisible by a nontrivial divisor of \(k\),
contrary to \(\gcd(2m+1,m+1)=1\).  Every orbit of incidence pairs therefore
has size \(k\).  \(\square\)

For the authenticated \(k=13\) factor, (2.1) reads

\[
 I_{\rm big,small}=26=2k,qquad I_{\rm small,big}=0,
\]

and hence gives the measured \(104\) versus \(0\) socket arcs.  The
distinguished-safe restriction leaves \(52\) arcs.  This is two quotient
incidences in one direction, not a dense two-colour graph.

## 3. The q1 overload bounds the number of wedge openings

For every directed factor edge \(A_iA_{i+1}\), call
\(A_i\cup A_{i+1}\) its q1 colour.  For a colour \(U\), let \(\mu_U\)
be its number of edge occurrences.

### Lemma 3.1 (adjacent-repeat budget)

Assume every rank-\((r+1)\) colour occurs and no factor component has a
constant q1-colour word.  If \(D=\sum_d|Z_d|\) is the total number of
wedge centres, then

\[
                    D\le \binom{k}{r}-\binom{k}{r+1}.              \tag{3.1}
\]

#### Proof

For a fixed colour \(U\), decompose its occurrences in the cyclic edge
words into maximal runs.  The nonconstant-component hypothesis makes every
such run a proper linear run.  A run of length \(a\) contains exactly
\(a-1\) adjacent equal pairs.  Since \(\mu_U\ge1\), the number of wedges
with colour \(U\) is at most \(\mu_U-1\).  Sum over all
\(\binom{k}{r+1}\) colours and use \(\sum_U\mu_U=\binom{k}{r}\).  \(\square\)

Without the nonconstant-component hypothesis, if \(M\) is the number of
q1-monochromatic physical components, the safe replacement is
\[
 D\le \binom{k}{r}-\binom{k}{r+1}+M.                \tag{3.1a}
\]
Indeed, for a fixed colour the circular-run correction beyond
\(\mu_U-1\) is at most one, and the number of colours needing that
correction is at most \(M\).  The hypothesis is automatic for a component
invariant under the full cyclic coordinate rotation: a constant colour
\(U\) would satisfy \(\rho U=U\), impossible for a nonempty proper subset.

At odd middle rank, put

\[
 W=\binom{2m+1}{m+1}=(2m+1)\operatorname{Cat}_m.
\]

Then (3.1) becomes the exact overload bound

\[
                    D\le {2W\over m+2}.             \tag{3.2}
\]

### Theorem 3.2 (stabilizer-weighted wedge obstruction)

Let the cyclic group act on the components of a q1-complete factor, and
assume no component is q1-monochromatic.  Let \(h_d\) be the order of the
setwise stabilizer of component \(C_d\).  If \(C_d\) contains a wedge,
then it contains at least \(h_d\) wedge centres.  Hence

\[
 \boxed{\displaystyle
   \sum_{d:\,Z_d\ne\varnothing}h_d\le {2W\over m+2}.}             \tag{3.3}
\]

In particular, if every component is a unit-voltage multi-spiral component
and therefore invariant under all \(k=2m+1\) rotations, the number
\(b_{\rm wedge}\) of components on which a wedge opening is possible obeys

\[
 \boxed{\displaystyle
 b_{\rm wedge}\le {D\over k}\le
 {2\operatorname{Cat}_m\over m+2}.}                 \tag{3.4}
\]

#### Proof

The stabilizer carries any wedge centre to a wedge centre in the same
component.  Its orbit has size \(h_d\), again because rotation is free on
rank-\(r\) subsets.  Sum these disjoint componentwise lower bounds and use
(3.2).  A unit-voltage quotient cycle lifts to one physical component
preserved by the full rotation group, so \(h_d=k\), giving (3.4).  \(\square\)

### Corollary 3.3 (arbitrary voltage)

Retain q1 completeness and the absence of q1-monochromatic physical
components.  Suppose an equivariant quotient cycle has voltage \(v_\nu\)
and put
\[
 g_\nu=\gcd(k,v_\nu).
\]
It lifts to \(g_\nu\) physical components, each with stabilizer order
\(k/g_\nu\).  Here **wedge-bearing quotient cycle** means that its physical
lift contains a wedge; a bare repeat in a quotient word is not being used
across a voltage wrap.  If it is wedge-bearing, all of its physical
components are wedge-bearing and together contain at least \(k\) wedge
centres.  Therefore the number of such quotient cycles is at most
\[
                     {D\over k}\le
                     {2\operatorname{Cat}_m\over m+2}.             \tag{3.5}
\]

This does not give the same bound on the number of physical components:
one wedge-bearing quotient cycle may lift to as many as \(k\) physical
components.  Thus the voltage/stabilizer distribution is part of the
missing PBBS theorem.

#### Proof

The cyclic group acts transitively on the \(g_\nu\) lifts, and each lift has
stabilizer order \(k/g_\nu\).  Apply Theorem 3.2 to the \(g_\nu\)
components.  Their stabilizer weights sum to \(k\).  \(\square\)

### Consequence 3.4

An all-components wedge-socket path is impossible for a unit-voltage
multi-spiral factor with

\[
                         b>{2\operatorname{Cat}_m\over m+2}.       \tag{3.6}
\]

In particular, if \(b=\Theta(\operatorname{Cat}_m)\), the proportion of
components which can even supply a wedge opening is \(O(1/m)\).  Thus a
Catalan-component unit-voltage multi-spiral cannot satisfy the desired
socket existence quantifier.  It first needs a premerge down to
\(O(\operatorname{Cat}_m/m)\) components, or a seam theorem permitting
nonwedge cuts.

This is a counting obstruction to the proposed architecture, not an
obstruction to coefficient one: opening Catalan-many components by other
collars still has asymptotically cheap topology in the existing ledger.

## 4. Why a Dirac condition is too strong

Assume \(m\ge2\) and again that all \(b\) components have unit voltage.
Put

\[
 t_d={|Z_d|\over k},\qquad t=\sum_dt_d.
\]

Let \(\overline G\) be the directed component projection with
\(c\to d\) when \(j_{cd}>0\).  From (2.3),

\[
 \deg^-_{\overline G}(d)\le\sum_{c\ne d}j_{cd}
       \le(r-2)t_d.                                  \tag{4.1}
\]

Also, by (3.2),

\[
                         t\le {2\operatorname{Cat}_m\over m+2}.   \tag{4.2}
\]

The total number of directed component arcs, and even the total quotient
incidence multiplicity, consequently obey

\[
 |A(\overline G)|
 \le\sum_{c\ne d}j_{cd}
 \le(r-2)t
 \le {2(m-1)\over m+2}\operatorname{Cat}_m
 <2\operatorname{Cat}_m.                              \tag{4.2a}
\]

Therefore any half-indegree hypothesis
\(\deg^-_{\overline G}(d)\ge b/2\) for every component forces

\[
 {b^2\over2(r-2)}\le t\le {2\operatorname{Cat}_m\over m+2},
\]
and, since \(r=m+1\),

\[
 \boxed{\displaystyle
 b^2\le {4(m-1)\over m+2}\operatorname{Cat}_m
       <4\operatorname{Cat}_m.}                     \tag{4.3}
\]

Thus a directed-Dirac route cannot apply when
\(b\gg\sqrt{\operatorname{Cat}_m}\).  At the maximal feasible wedge scale
\(b=\Theta(\operatorname{Cat}_m/m)\), however, the total
quotient-incidence capacity is \(O(mb)\).  A sparse rotation-extension
expander of degree
\(O(m)\) is numerically possible.  What is absent is a theorem placing the
incidences among component colours and, more strongly, making the incoming
and outgoing incidences use one common wedge centre on every intermediate
component.

## 5. The exact missing PBBS dispersion statement

The relevant graph is not merely the component projection.  It is the
coloured wedge-centre digraph

\[
 B\longrightarrow A\quad\Longleftrightarrow\quad B\subset U_A,qquad
 B,A\text{ on different components}.                \tag{5.1}
\]

A colourful socket path is a directed path in (5.1) containing exactly one
wedge centre of every component colour, with a safe signed opening at its
first centre.  Using only the component projection can be unsound: the
incoming incidence and the outgoing incidence at an intermediate colour
may require two different wedge centres.

In the invariant/unit-voltage case, for a proposed safe root colour
\(c_0\), even root reachability already
requires the cut inequalities

\[
 \sum_{c\notin X,\ d\in X}j_{cd}>0
 \quad\text{for every nonempty }X\subseteq[b]\setminus\{c_0\}.    \tag{5.2}
\]

A rooted Hamilton path also implies the Hall inequalities

\[
 |N^-(X)|\ge|X|
 \quad\text{for every }X\subseteq[b]\setminus\{c_0\},             \tag{5.3}
\]

but (5.3) alone only gives a predecessor matching and may leave directed
cycles.  A positive theorem needs a centre-compatible rotation/exchange
condition which merges those cycles while retaining the safe root.

The currently audited PBBS fixed-width theorem proves neither (5.2),
(5.3), nor centre compatibility.  The exact finite factors demonstrate the
gap:

* at \(k=13\), the quotient socket incidence is \(2\) in the big-to-small
  direction and zero in reverse; nevertheless a safe big root yields 52
  distinguished two-component chains;
* at \(k=15\), the invariant components have \(t=(22,0)\).  The length-45
  component is wedge-free, so the all-components wedge graph has no vertex
  of that colour despite complete fixed-width support at every depth.

The multi-spiral run/lifetime equations and residence bounds do not repair
this gap: the authenticated length-45 component is simultaneously a
unit-voltage multi-spiral component, biresident, and wedge-free.

Accordingly the sharp remaining asymptotic lemma is a **quotient
facet-dispersion/rotation lemma** after sufficient component premerging:
it must place the integers \(j_{cd}\), supply a safe root, and ensure that
successive incidences share one physical wedge centre in each intermediate
component.  All-depth PBBS shadow support controls witness labels, not this
incidence distribution.
