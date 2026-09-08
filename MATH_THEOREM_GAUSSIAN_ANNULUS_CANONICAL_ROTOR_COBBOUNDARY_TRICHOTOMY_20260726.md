# Gaussian annulus rotor strips: exact canonical coboundary, zero frustration, and the linear type defect

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad
 W=\binom{2m+1}{m},
 \qquad
 H=\lceil A\sqrt m\rceil,
 \tag{0.1}
\]

where \(A>0\) is fixed.  This note combines three exact inputs:

* the in-place strongly safe cyclic-strip OR compiler from
  `MATH_ATTACK_PBBS_GAUSSIAN_ANNULUS_NONLINEAR_LOW_SWITCH_20260726.md`;
* the two-shore signed packet theorem from
  `MATH_THEOREM_FINE_STRIP_CONJUGATE_PACKET_MULTICHOICE_GATE_20260726.md`;
  and
* the anti-dihedral two-rotor classification from
  `MATH_OBSTRUCTION_ANTI_DIHEDRAL_NESTED_UCYCLE_PERIOD_N_COCYCLE_20260726.md`.

The requested canonical-rotor decision is rigorous.

1. **The canonical target signs are an exact coboundary.**  For the
   canonical fixed-pair strip factor and simultaneous endpoint reflection,
   every overlay packet is one physical strip on each shore.  Every
   two-occurrence target gives the two literals

   \[
    (P,0),\qquad(P,1),
   \]

   and hence a label-zero loop.  Thus

   \[
    \boxed{\tau(G)=0.}
    \tag{0.2}
   \]

   The explicit packet potential is the constant zero function.  There is
   not merely no \(\Omega(W)\) packing of frustrated cycles: there is no
   frustrated cycle at all.

2. **Coboundary is not the full annulus condition.**  At every Gaussian
   depth \(q/\sqrt m\to a>0\), any two shores whose physical transitions
   remain in one fixed coordinate pairing satisfy

   \[
    \boxed{
    \mathfrak B_{2,q}^-\ge
      2D_{m,q}^{\rm odd}
      =(2\delta(a)+o(1))W,}
    \tag{0.3}
   \]

   where \(\mathfrak B_{2,q}^-\) is the two-copy occurrence imbalance and

   \[
    \delta(a)=e^{-a^2}\Phi(a/2)-\Phi(-3a/2)>0.
    \tag{0.4}
   \]

   Hence the canonical pair realizes the exact third possibility omitted
   by the proposed dichotomy:

   \[
    \boxed{
    \text{perfect signed coboundary}quad+quad
    \Omega_A(W)\text{ pair/type imbalance}.}
    \tag{0.5}
   \]

   A signed-cycle theorem alone therefore cannot close the annulus.

3. **Exact anti-dihedral symmetry cannot supply a nonlinear repair.**  In
   the two-rotor state graph, anti-dihedral phase symmetry forces every
   selected transition to be the full-rotation \(B\)-move; all nonlinear
   \(A\)-moves vanish.  Every component is one length-\(n\) wreath.  This
   collapse does not itself make the typed OR collar expensive:

   \[
    W+2H{W\over n}=W+o_A(W).
    \tag{0.6}
   \]

   Its failure is instead (0.3): the same-frame wreath chronology has a
   positive Gaussian target deficit.

4. **Mixed-frame soft switches are quantitatively compulsory.**  If an
   owner-exact strongly safe chronology has \(s\) transitions outside one
   fixed pairing, then

   \[
    h_q^-\ge D_{m,q}^{\rm odd}-qs.
    \tag{0.7}
   \]

   Consequently \(h_q^-=o(W)\) at any fixed Gaussian depth forces

   \[
    \boxed{s\ge(\delta(a)+o(1)){W\over q}
          =\Omega_a(W/\sqrt m).}
    \tag{0.8}
   \]

   These switches must be soft edges inside the final chronology.  Paying
   an additive \(H\)-collar at each would cost \(\Theta(W)\), which is
   expressly forbidden in the in-place lane.

Thus the canonical rotor has the desired physical signed-coboundary
identity, but this does not produce an annulus compiler.  The exact
remaining mixed-frame theorem must establish all three conditions

\[
 \mathfrak B_2=o(W),
 \qquad
 \tau(G)=o(W),
 \qquad
 c=o(W/H),
 \tag{0.9}
\]

for an owner-exact strongly safe rethreading with at least
\(\Omega(W/\sqrt m)\) frame-changing soft transitions.  Here \(c\) is the
number of final cyclic components.  Neither exact reflection nor an
additive seam chart supplies this object.

No coefficient-one conclusion is claimed.

## 1. The signed packet complex

Let two exact strip factors be overlaid on their common middle-owner
support.  Connected owner-support components are packets \(P\), and a
binary variable

\[
 x_P\in\mathbb F_2
 \tag{1.1}
\]

chooses one of the two shores on the whole packet.

Suppose a target \(T\) has exactly two catalogue occurrences

\[
 (P,a),\qquad(Q,b),
 \qquad a,b\in\mathbb F_2,
 \tag{1.2}
\]

where occurrence \((P,a)\) is retained precisely when \(x_P=a\).  Define

\[
 s_T=1\oplus a\oplus b.
 \tag{1.3}
\]

### Lemma 1.1 (exact-one equation)

The selected load of \(T\) is exactly one if and only if

\[
 \boxed{x_P\oplus x_Q=s_T.}
 \tag{1.4}
\]

#### Proof

The truth indicator for the first occurrence is

\[
 1\oplus x_P\oplus a,
\]

and similarly for the second.  Exactly one is true precisely when their
XOR is one.  Rearranging gives (1.4). \(\square\)

The regular two-occurrence targets therefore form a signed multigraph
\(G\) on the packets.  Its sign cochain is

\[
 s\in C^1(G;\mathbb F_2).
\]

It is a coboundary if

\[
 s=\delta x,
 \qquad
 (\delta x)(PQ)=x_P\oplus x_Q.
 \tag{1.5}
\]

Equivalently, every signed cycle has XOR zero.  The frustration index is

\[
 \tau(G)=\min_x|\{e:s_e\ne(\delta x)_e\}|.
 \tag{1.6}
\]

If \(k\) edge-disjoint frustrated cycles are present, every balancing
edge deletion meets each of them, so

\[
 \tau(G)\ge k.
 \tag{1.7}
\]

The converse need not hold without a bounded-length or bounded-congestion
cycle decomposition; this is why frustration index and a packing of
frustrated cycles must not be interchanged silently.

Define the two-copy imbalance at a target family \(\mathcal T\) by

\[
 \mathfrak B_2=\sum_{T\in\mathcal T}|r_T-2|,
 \tag{1.8}
\]

where \(r_T\) is its total catalogue occurrence count on the two shores.
The exact packet theorem gives the combined gate

\[
 \boxed{\mathfrak B_2+\tau(G)=o(W).}
 \tag{1.9}
\]

Coboundary controls only the integral choice among regular two-copy
targets.  It says nothing about targets absent from that regular graph.

## 2. The canonical physical cyclic-strip identity

Pair the first \(2m\) physical coordinates as

\[
 \mathcal P=\{\{a_1,b_1\},\ldots,\{a_m,b_m\}\}
 \tag{2.1}
\]

and retain the distinguished odd coordinate.  Let \(\mathcal F\) be the
canonical fixed-pair dyadic strip factor on the good owner cells.  Put

\[
 \rho=\prod_{i=1}^m(a_i\ b_i).
 \tag{2.2}
\]

On every active orientation cube, \(\rho\) complements all orientation
bits.  The canonical direction cycle is invariant under this half-turn,
and the same cycle factor is installed in every inactive spectator face.
Thus

\[
 \boxed{\rho\mathcal F=\mathcal F.}
 \tag{2.3}
\]

This is an equality of physical strip factors, not merely equality of
their owner histograms.

### Theorem 2.1 (canonical strip signs are a coboundary)

Use the same integral port system on the two labelled copies
\((\mathcal F,\rho\mathcal F)\).  Every overlay packet contains one copy
of a physical strip on each shore.  Every two-occurrence target produces
a label-zero loop, and hence

\[
 \boxed{s=0=\delta0,qquad\tau(G)=0.}
 \tag{2.4}
\]

#### Proof

Distinct strips of \(\mathcal F\) have disjoint owner supports.  By (2.3),
the two copies of one strip have identical support, so they form one
packet and no packet contains a different strip.

If \(T\) has total occurrence count two, it occurs on exactly one physical
strip and hence has literals

\[
 (P,0),\qquad(P,1).
\]

Equation (1.3) gives the loop sign

\[
 1\oplus0\oplus1=0.
\]

Every edge is therefore a zero loop, which is the coboundary of the
constant potential. \(\square\)

### Corollary 2.2 (the requested frustration branch is false canonically)

The canonical reflected rotor has no frustrated cycle.  In particular it
cannot have \(\Omega(W)\) edge-disjoint frustrated cycles.

This conclusion is statewise.  It does not rely on averaging shores,
discarding exceptional targets, or choosing a favorable packet potential.

## 3. Reflection transports, rather than cancels, frustration

The preceding zero-loop identity is special to the setwise-fixed
canonical factor.  There is nevertheless an exact statement for every
anti-automorphic packet pair.

Suppose reflection sends packets by \(P\mapsto\sigma P\) and occurrence
literals by

\[
 (P,a)\longmapsto(\sigma P,a\oplus\eta_P).
 \tag{3.1}
\]

Then the upper target corresponding to a lower edge \(PQ\) has sign

\[
 s^+_{\theta T}
 =s^-_T\oplus\eta_P\oplus\eta_Q.
 \tag{3.2}
\]

### Theorem 3.1 (switching-isomorphic signs)

The lower and upper signed graphs are switching-isomorphic.  In
particular,

\[
 \boxed{\tau(G^+)=\tau(G^-).}
 \tag{3.3}
\]

For every packet assignment \(x\), if

\[
 (Jx)_P=x_{\sigma P}\oplus\eta_P,
\]

then

\[
 F_+(x)=F_-(Jx),
 \qquad
 F_-(x)+F_+(x)\ge2\tau(G^-).
 \tag{3.4}
\]

#### Proof

Equation (3.2) differs from the lower sign by the vertex coboundary
\(\delta\eta\), followed by the packet permutation \(\sigma\).  Switching
and graph isomorphism preserve every cycle sign and the frustration index.
Substitution of \(Jx\) into the lower equations gives the first identity
in (3.4); the second follows by minimizing each summand. \(\square\)

Thus anti-dihedral reflection never makes lower and upper frustration
cancel.  It either copies one coboundary to the other sign, as in the
canonical case, or copies the same obstruction.

## 4. The fixed-pair Gaussian deficit survives exact coboundary

For a lower rank-\((m-q)\) target, let \(\varepsilon\in\{0,1\}\) record
whether it contains the distinguished coordinate, and let \(f\) be its
number of full pairs in (2.1).  Write

\[
 T_{f,q}^{\varepsilon}
 ={m!\,2^{m-2f-q-\varepsilon}\over
 f!(f+q+\varepsilon)!(m-2f-q-\varepsilon)!},
 \tag{4.1}
\]

\[
 V_f^{\varepsilon}
 ={m!\,2^{m-2f-\varepsilon}\over
 f!(f+\varepsilon)!(m-2f-\varepsilon)!}.
 \tag{4.2}
\]

These are respectively the target count and compatible middle-source
count in type \((\varepsilon,f)\).  Every in-frame transition preserves
this type.

Put

\[
 D_{m,q}^{\rm odd}
 =\sum_{\varepsilon,f}
   (T_{f,q}^{\varepsilon}-V_f^{\varepsilon})_+.
 \tag{4.3}
\]

### Theorem 4.1 (two-shore imbalance cut)

For any two strip factors whose transitions remain in the same pairing
frame, and for arbitrary selected port subsets,

\[
 \boxed{
 \mathfrak B_{2,q}^-
 =\sum_T|r_T-2|
 \ge2D_{m,q}^{\rm odd}.}
 \tag{4.4}
\]

#### Proof

Fix a deficient type \((\varepsilon,f)\).  One shore has at most
\(V_f^\varepsilon\) source owners of that type and hence at most that many
selected occurrences ending in its target orbit.  Two shores have at most
\(2V_f^\varepsilon\).  Therefore

\[
 \begin{aligned}
 \sum_{T\text{ of type }(\varepsilon,f)}|r_T-2|
 &\ge
 \left|\sum_T(r_T-2)\right|\\
 &\ge2T_{f,q}^\varepsilon-2V_f^\varepsilon.
 \end{aligned}
\]

Sum over the deficient types. \(\square\)

If \(q/\sqrt m\to a>0\), the exact local central-limit ratio gives

\[
 {D_{m,q}^{\rm odd}\over W}
 \longrightarrow
 \delta(a)=e^{-a^2}\Phi(a/2)-\Phi(-3a/2)>0.
 \tag{4.5}
\]

Combining (2.4), (4.4), and (4.5) proves (0.3)--(0.5).

There is a one-shore form which directly audits a physical cyclic-strip
compiler.  Every in-frame owner chronology has at least

\[
 \boxed{h_q^-\ge D_{m,q}^{\rm odd}}
 \tag{4.6}
\]

missing lower targets at depth \(q\).  Thus its typed erosion word cannot
cover the whole Gaussian layer solely by its physical strip flags, even
though its packet signs have zero frustration.

This is a target-capacity statement for the cyclic-strip atlas.  It is not
a universal lower bound for every arbitrary OR word: a noncanonical master
overlay may create witnesses which are not physical same-frame strip
windows.  Such an overlay is precisely a new construction, not a
consequence of the canonical coboundary.

## 5. Anti-dihedral Ucycle rigidity and the OR-collar audit

Let \(A\) rotate the first \(n-1\) entries of a permutation state and
let \(B\) rotate all \(n\) entries.  Both moves project to the same
Johnson successor; they differ only in the tail state.

### Theorem 5.1 (anti-dihedral rotor face)

If a sliding component is carried anti-dihedrally to its rank-reversed
component, then its emitted symbol word has period \(n\), one period is a
permutation of the coordinates, and its rotor control word contains only
\(B\)-moves.

#### Proof

Comparing two consecutive anti-dihedral identities with the unique target
exchange gives

\[
 s_{i+n}=s_i.
 \tag{5.1}
\]

Distinct middle windows force the component length to divide \(n\) and
to exceed \(m\).  Every proper divisor of the odd number \(n=2m+1\) is
at most \(n/3<m+1\), so the length is exactly \(n\).  Window injectivity
then makes its period a permutation.

At every state, the next emitted coordinate is therefore the unique
missing coordinate, which is exactly the \(B\)-move. \(\square\)

Consequently an exact anti-dihedral middle factor is a union of

\[
 C={W\over n}
 \tag{5.2}
\]

wreaths.  A singleton-window linearization pays

\[
 W+C(m+H)=\left({3\over2}+o_A(1)\right)W,
 \tag{5.3}
\]

but that is not the relevant cost for the rotor OR compiler.  The strongly
safe erosion compiler pays only

\[
 \boxed{
 W+2HC
 =W+{2H\over n}W
 =W+o_A(W).}
 \tag{5.4}
\]

Thus it would be incorrect to cite the anti-dihedral component collapse as
an additive-seam obstruction to the typed OR lane.  The exact obstruction
is the missing-target term (4.6), which remains \(\Omega_A(W)\).

## 6. Mixed-frame soft-switch threshold

Call a transition exceptional when it does not exchange the two endpoints
of one pair in (2.1).  Suppose an owner-exact strongly \(H\)-safe
chronology contains \(s\) exceptional transition occurrences.

### Theorem 6.1 (stability of the type cut)

For every \(q\le H\),

\[
 \boxed{
 h_q^-\ge D_{m,q}^{\rm odd}-qs.}
 \tag{6.1}
\]

#### Proof

A cyclic depth-\(q\) window is exceptional only if it contains one of the
\(s\) frame-changing transitions.  Each transition belongs to exactly
\(q\) cyclic \(q\)-windows, so there are at most \(qs\) exceptional
windows.  Every remaining window stays in the fixed frame, and the
type-capacity proof of (4.6) applies unchanged.  Each exceptional window
can supply at most one formerly missing target.  Subtracting \(qs\) gives
(6.1). \(\square\)

At \(q=a\sqrt m+O(1)\), equations (4.5) and (6.1) imply

\[
 h_q^-=o(W)
 \quad\Longrightarrow\quad
 s\ge(\delta(a)+o(1)){W\over q}
   =\Omega_a(W/\sqrt m).
 \tag{6.2}
\]

This is exactly the soft-switch scale found by the annulus seam-fan
census.  If each switch were opened as a separate hard component or paid
an \(H\)-letter repair block, then

\[
 Hs=\Omega_A(W).
 \tag{6.3}
\]

Therefore these transitions must be absorbed inside a few final cyclic
strips; no additive seam accounting is coefficient-compatible.

## 7. Why approximate anti-dihedral defects do not imply frustration

Let \(\mathcal B\) be the phase set on which a proposed long component
fails its anti-dihedral relation.  The exact period comparison gives

\[
 |\mathcal B|\ge{\ell\over4m}
 \tag{7.1}
\]

on a component of length \(\ell>n\).  Moreover every interval of
\(2m+3\) phases meets \(\mathcal B\).  Hence, through a Gaussian window,
the number of defect-meeting phase--depth incidences is

\[
 \Omega_A(\ell).
 \tag{7.2}
\]

These are chronology defects, not signed-cycle periods.  There is no valid
implication

\[
 \text{defect-meeting traces }\Longrightarrow
 \text{frustrated signed cycles}.
 \tag{7.3}
\]

The canonical factor itself is the sharp countercalibration: its signed
graph has \(\tau=0\), while its Gaussian occurrence/type defect is linear.
Thus neither (7.1) nor (7.2) can be converted into an
\(\Omega(W)\) frustrated-cycle packing without an additional physical
identity which maps phase defects injectively into nonzero cycle periods.

## 8. Exact in-place annulus gate

Let a mixed-frame owner chronology have \(c\) final strongly safe cyclic
components.  The erosion compiler contributes

\[
 W+2Hc.
 \tag{8.1}
\]

For a support-matched two-shore catalogue, let \(\mathfrak B_2\) include
all exceptional non-two-copy target mass through the desired annulus, and
let \(G\) be its regular signed graph.  The signed packet theorem and the
literal compiler give the sufficient ledger

\[
 \boxed{
 L\le W+2Hc+\mathfrak B_2+\tau(G)+o(W).}
 \tag{8.2}
\]

No term is charged per soft switch.  The switches are actual internal
edges of the final cycles.  Therefore

\[
 c=o(W/H),
 \qquad
 \mathfrak B_2=o(W),
 \qquad
 \tau(G)=o(W)
 \tag{8.3}
\]

are the precise in-place conditions.  The canonical reflected rotor
satisfies the last condition exactly and violates the middle condition by
\(\Omega_A(W)\).  A generic reflected mixed pair has equal lower and upper
frustration by Theorem 3.1, so the two signs cannot cancel one another.

The remaining physical theorem is now narrower than a generic annulus
matching problem:

> Construct an owner-exact, strongly safe, mixed-frame cyclic-strip
> rethreading with \(c=o(W/H)\), at least
> \(\Omega_A(W/\sqrt m)\) internal frame-changing transitions, two-copy
> imbalance \(o(W)\), and a target sign cochain equal to a packet
> coboundary off \(o(W)\) regular targets.

Alternatively, for a specified mixed-frame canonical candidate, prove
either \(\mathfrak B_2=\Omega(W)\) or \(\tau(G)=\Omega(W)\).  A packing of
\(\Omega(W)\) edge-disjoint frustrated cycles would imply the second
alternative by (1.7), but the canonical same-frame rotor has zero such
cycles and is obstructed by the first alternative instead.

## 9. Audited boundary

Proved here:

1. the exact signed cochain and frustration formulation;
2. the physical canonical-strip identity \(s=\delta0\);
3. absence of every frustrated cycle in the canonical reflected rotor;
4. the exact same-frame two-copy imbalance cut;
5. its positive Gaussian limit;
6. the anti-dihedral \(B\)-only/wreath classification;
7. the distinction between the expensive singleton compiler and the
   economical erosion compiler;
8. the \(\Omega(W/\sqrt m)\) mixed-frame soft-switch necessity; and
9. the no-additive-seam ledger (8.2).

Not proved:

1. a mixed-frame rethreading satisfying (8.3);
2. an all-but-\(o(W)\) coboundary theorem for such a mixed rethreading;
3. an \(\Omega(W)\) frustrated-cycle packing for a specified mixed-frame
   candidate; or
4. coefficient one.

The requested canonical dichotomy is therefore decided but insufficient:
the canonical signs are a perfect coboundary, so the frustrated-cycle
branch is false, while a separate \(\Omega_A(W)\) type/occurrence defect
prevents the direct same-frame annulus compiler.
