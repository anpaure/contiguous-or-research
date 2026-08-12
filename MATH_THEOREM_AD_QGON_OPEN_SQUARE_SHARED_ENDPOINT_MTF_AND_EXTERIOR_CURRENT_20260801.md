# The open Johnson square is a shared-boundary depth-one MTF role converter, not the fusion move

**Date:** 2026-08-01  
**Lane:** AD, direct q-gon fusion / literal chronology  
**Status:** exact local construction, exact MTF threshold, exact component
ledger, and exact all-width exterior-current formula. The support-four
square removes the q-gon closed doubleton in the immediate three-rank band.
It does not by itself merge components, it has no saturated one-step MTF
lift of depth at least two, and a frozen exterior can leave a linear family
of crossing-window defects.

## 0. Exact verdict

Let \(K\) have rank \(m-2\), and let \(x,y,z,w\) be distinct and outside
\(K\). Put

\[
 A=K+x+z,\qquad B=K+x+y,\qquad
 C=K+y+w,\qquad D=K+z+w.                         \tag{0.1}
\]

The two open-square phases are

\[
 P^+=(B,C,D,A),\qquad
 P^-=(A,D,C,B)=\operatorname{rev}P^+.             \tag{0.2}
\]

The exact answer has four parts.

1. The packet is a literal shared-boundary OR converter. There are source
   words \(W^+,W^-\) with one common boundary cell at both ends whose first
   derivative rows are (0.2) and whose second derivative rows are the same
   three upper colours in reverse order. No middle root or immediate upper
   owner repeats inside a phase.
2. As a one-step move-to-front trajectory, either owner path has an
   \(H\)-saturated lift exactly for \(H=1\). It has none for \(H\ge2\).
   Thus it is an immediate-band role converter, not a growing-depth MTF
   converter.
3. In the simultaneous q-port bank, the four exact states have component
   counts

   \[
                     1\longrightarrow q\longrightarrow q
                       \longrightarrow1.                  \tag{0.3}
   \]

   The middle square reversal has component change zero. The following
   q-gon rethread, not the reversal, fuses the \(q\) port cycles.
4. Reversal preserves the complete internal interval-OR deck. Against a
   fixed exterior, however, its entire all-width current consists of two
   nested rays at each boundary. These currents need not vanish and can
   have linearly many distinct contextual occurrences.

Consequently the square gives the literal role conversion needed by the
q-gon construction, but it is not an unconditional connector between two
arbitrary pre-existing closed q-gon copies. Prospective endpoint planting,
whole-copy reversal, or an additional support-changing connector is still
required.

## 1. Literal shared-boundary source and immediate palettes

Define

\[
 L_0=K+x,\qquad L_1=K+y,\qquad
 L_2=K+w,\qquad L_3=K+z.                         \tag{1.1}
\]

Let \(\mathcal D\) denote the sliding union of adjacent cells. Consider the
two five-cell source words

\[
\begin{aligned}
 W^+&=(L_0,L_1,L_2,L_3,L_0),\\
 W^-&=(L_0,L_3,L_2,L_1,L_0)=\operatorname{rev}W^+ .
\end{aligned}                                             \tag{1.2}
\]

The repeated display of \(L_0\) means two boundary positions of one linear
ear. In a cyclic square they are the same cut cell. Direct calculation gives

\[
 \mathcal D W^+=(B,C,D,A),\qquad
 \mathcal D W^-=(A,D,C,B),                                \tag{1.3}
\]

and

\[
\begin{aligned}
 \mathcal D^2W^+&=(U_1,U_2,U_3),\\
 \mathcal D^2W^-&=(U_3,U_2,U_1),                          \tag{1.4}
\end{aligned}
\]

where

\[
\begin{aligned}
 U_1&=K+x+y+w,\\
 U_2&=K+y+z+w,\\
 U_3&=K+x+z+w.
\end{aligned}                                             \tag{1.5}
\]

### Theorem 1.1 (literal shared-boundary converter)

The four middle roots in (0.1), the three nonseam lower colours
\(L_1,L_2,L_3\), and the three upper colours \(U_1,U_2,U_3\) are
separately distinct. Equations (1.2)--(1.4) are therefore a literal
two-derivative role-conversion ear. Both phases omit exactly the seam pair

\[
                  L_0=K+x,\qquad U_0=K+x+y+z=A\cup B.     \tag{1.6}
\]

In particular, neither phase contains either oriented seam atom
\((L_0,U_0;A,B)\) or \((L_0,U_0;B,A)\); the q-gon closed doubleton is
absent.

#### Proof

Adjacent unions in (1.2) are the four sets in (0.1), and unions of three
adjacent source cells are the sets in (1.5). Distinctness follows from the
active labels \(x,y,z,w\). The cyclic triple \(L_3,L_0,L_1\) would supply
the omitted upper seam value \(U_0\), but it is not an interval of either
open source word. The value \(L_0\) itself occurs at both source boundaries;
what is omitted from the first derivative is the seam adjacency \(A B\),
and hence the immediate pair \((L_0,U_0)\). \(\square\)

This is a literal source-level statement. It is stronger than merely saying
that (0.2) is a Johnson path, but it is weaker than a prescribed complete
last-occurrence-state identification at the two ends.

## 2. Exact MTF threshold

Use the one-step MTF convention of
MATH_ATTACK_AD_ADAPTIVE_MTF_FUSION_AUDIT_20260724.md, Theorem 3.1. A
Johnson walk

\[
 T_{i+1}=T_i-\{p_i\}+\{q_i\}
\]

has an \(H\)-saturated one-step MTF lift if and only if every later reuse
\(q_a=p_b\), \(a<b\), obeys

\[
                              b-a\ge H+1.                  \tag{2.1}
\]

Along \(P^+=(B,C,D,A)\), the departure/arrival pairs are

\[
 (p_0,q_0)=(x,w),\qquad
 (p_1,q_1)=(y,z),\qquad
 (p_2,q_2)=(w,x).                                         \tag{2.2}
\]

The unique arrival which departs later inside the path is

\[
                              q_0=w=p_2,                   \tag{2.3}
\]

at gap two. Along the reverse path they are

\[
 (x,w),\qquad(z,y),\qquad(w,x),                            \tag{2.4}
\]

with the same unique gap.

### Theorem 2.1 (sharp MTF depth)

For \(1\le H\le m/2\), either orientation in (0.2) has an \(H\)-saturated
one-step MTF lift if and only if \(H=1\).

#### Proof

By (2.3), criterion (2.1) is exactly \(2\ge H+1\). This holds for \(H=1\)
and fails for every \(H\ge2\). Equations (2.2) and (2.4) show that the two
orientations have the same obstruction. \(\square\)

Here \(H=1\) means the immediate ranks \(m-1,m,m+1\). The phrase
“depth-two second-order walk” in the depth-two square theorem refers to the
literal lower/root/upper identities (1.3)--(1.4); it must not be read as
\(H=2\) saturation. The coordinate \(w\) has owner trace

\[
                                0,1,1,0,                   \tag{2.5}
\]

which is the same sharp obstruction in run language.

An existential \(H=1\) lift for each orientation does not identify its
complete ordered-partition endpoint states with arbitrary ambient q-gon
states. That endpoint-state equality remains an explicit gluing condition.
For example, immediately traversing \(P^+\) and then \(P^-\) makes the
arrival \(x\) depart on the next edge, a gap-one reuse which violates even
\(H=1\). The q-port closure in the next section avoids this because no
closing edge immediately deletes the newly returned \(x=s\). More
explicitly, after \(R_i^+\) the next direct edge deletes \(z\); after
\(R_i^-\) it deletes \(a_{i+1}\) in \(G_1\) and \(a_i\) in \(G_0\).

## 3. The exact q-port fusion architecture

Let \(S\) have rank \(m-2\), let

\[
 A_i=S+z+a_i,\qquad
 B_i=S+a_i+a_{i+1}\qquad(i\in\mathbb Z_q),                \tag{3.1}
\]

where \(q\ge3\). Choose \(s\in S\) and a fresh \(w\) outside the complete
q-gon support, and put

\[
\begin{aligned}
 C_i&=(S-s)+a_i+a_{i+1}+w,\\
 D_i&=(S-s)+a_i+z+w.                                     \tag{3.2}
\end{aligned}
\]

This is (0.1) with

\[
 K_i=(S-s)+a_i,\qquad x=s,\qquad y=a_{i+1}.               \tag{3.3}
\]

Assume the displayed coordinates exist; on a \(2m\)-point ground it is
enough that \(3\le q\le m\). Define the two open rails

\[
 R_i^+:B_i\to C_i\to D_i\to A_i,\qquad
 R_i^-:A_i\to D_i\to C_i\to B_i.                         \tag{3.4}
\]

Finally define four directed states

\[
\begin{aligned}
 G_0&=\{B_{i-1}\to A_i:i\in\mathbb Z_q\}\cup\bigcup_iR_i^-,\\
 G_1&=\{B_i\to A_i:i\in\mathbb Z_q\}\cup\bigcup_iR_i^-,\\
 G_2&=\{A_i\to B_i:i\in\mathbb Z_q\}\cup\bigcup_iR_i^+,\\
 G_3&=\{A_i\to B_{i-1}:i\in\mathbb Z_q\}\cup\bigcup_iR_i^+.
                                                               \tag{3.5}
\end{aligned}
\]

### Theorem 3.1 (owner-simple q-port role conversion and fusion)

Every state in (3.5) has \(4q\) distinct middle roots and uses the same
\(4q\) lower and \(4q\) upper immediate resources, each exactly once. Its
component counts are

\[
             c(G_0)=1,\qquad c(G_1)=q,\qquad
             c(G_2)=q,\qquad c(G_3)=1,                    \tag{3.6}
\]

and

\[
                        G_2=\operatorname{rev}G_1,\qquad
                        G_3=\operatorname{rev}G_0.         \tag{3.7}
\]

Thus \(G_1\leftrightarrow G_2\) is a literal shared-endpoint role
conversion with component change zero. The q-gon rethread
\(G_2\to G_3\) is the actual fusion and has

\[
                              \Delta c=-(q-1).             \tag{3.8}
\]

#### Proof

Every direct q-gon root contains \(s\) and omits \(w\), while every internal
root \(C_i,D_i\) omits \(s\) and contains \(w\). The active \(a\)-profile
and the presence of \(z\) distinguish all internal roots. The same
prefix/profile argument separates the three rail lower and upper colours
at every port from one another and from the direct seam pair. Equivalently,
this is the \(d=1\) specialization of the resource-disjoint q-port rail
theorem. Hence each state has one copy of every displayed resource.

In \(G_1\) and \(G_2\), each port is one directed \(C_4\), and (3.7) holds
on that cycle. In \(G_3\), following a rail to \(A_i\) and then its direct
edge enters the rail at index \(i-1\). The shift \(i\mapsto i-1\) is one
q-cycle, so all q port cycles fuse. \(G_0\) is its complete reversal.
\(\square\)

This theorem answers the one-copy q-port question, not arbitrary-copy
planting. The four states are alternative selections on one common q-port
root bank; they do not place two physically disjoint q-gon copies
simultaneously. If two pre-existing owner-disjoint paths expose compatible
typed endpoints, identifying the path endpoints and inserting the two new
internal roots can join them without duplicating an owner. At the graph
level this reduces the two charged components to one. But a closed-cycle
fusion needs the complementary connector/current, and literal source
composition still requires matching endpoint MTF states and the q1 ledger.

In particular, \(q=2\) is not obtained by this theorem. The q-gon then
identifies the two \(B\)-roots and returns to the closed-doubleton
degeneracy. A two-component-to-one connector needs a different
support-changing splice or an auxiliary third component.

## 4. Component and fixed-exterior no-go

For a directed path \(Q=(T_0,\ldots,T_r)\), put

\[
                         \partial Q=e_{T_r}-e_{T_0}.       \tag{4.1}
\]

For the two square paths,

\[
               \partial P^+=e_A-e_B,\qquad
               \partial P^-=e_B-e_A,                     \tag{4.2}
\]

so the reversal current is

\[
                     \partial(P^--P^+)=2(e_B-e_A).        \tag{4.3}
\]

### Theorem 4.1 (reversal is not a fusion)

Replacing \(P^+\) by \(P^-\) changes no undirected edge and hence no weak
component. It is a legal balanced replacement only when another module
cancels (4.3). In a directed one-factor, every legal batch of
orientation-only replacements reverses whole components and preserves the
component count and all component lengths.

#### Proof

The two paths have the same three unoriented edges. This proves weak
component invariance and (4.3) proves the balance condition. On one
underlying cycle, record each edge as forward or reversed. Indegree and
outdegree one at a vertex force the signs of its two incident edges to
agree. Connectedness forces all signs on the cycle to agree, so the only
legal choices are no reversal and whole-cycle reversal. \(\square\)

There is a sharper fixed-context statement. Suppose a fixed owner word
contains

\[
                    p,B,C,D,A,q                             \tag{4.4}
\]

and one tries to replace its middle block by

\[
                    p,A,D,C,B,q.                            \tag{4.5}
\]

Assume all four new boundary adjacencies are loopless Johnson edges.
Then \(p,q\) are common Johnson neighbours of \(A,B\). Exact preservation
of the two boundary lower and upper palettes holds if and only if \(p=q\).
In that case (4.4)--(4.5) are opposite orientations of one closed
five-cycle, not a fusion. Moreover, the Johnson common-neighbour
dichotomy says that the two incident edges at \(p\) repeat either their
lower colour or their upper colour. Hence the completion is not a clean
one-copy q1 closure of the bare square.

Indeed, put \(L=K+x\) and \(U=K+x+y+z\). Every common neighbour is either

\[
                 R_a=L+a\quad(a\notin U)                  \tag{4.6}
\]

or

\[
                 T_a=U-a\quad(a\in L).                    \tag{4.7}
\]

For two bottom neighbours \(p=R_a,q=R_b\), the lower boundary palette is
fixed while the signed upper change is

\[
 [L+a+z]-[L+a+y]+[L+b+y]-[L+b+z],                        \tag{4.8}
\]

which vanishes exactly when \(a=b\). For two top neighbours the symmetric
lower calculation gives the same conclusion; a mixed pair has a nonzero
primitive change on both shores. Thus \(p=q\). Equations (4.6)--(4.7)
also show respectively the repeated lower or repeated upper boundary
colour.

Here \(p=q\) is an endpoint identification on a closed cycle. In a literal
linear word it would display the same rank-\(m\) owner at both ends. The
clean direct-seam \(C_4\) closure from Section 3 is not a counterexample:
there the seam edge is reversed together with the three-edge rail, so the
exterior is phase-dependent rather than frozen.

The q-port states avoid this no-go because the direct q-gon atom changes
orientation together with the rail; the exterior is not frozen.

## 5. Internal OR deck and exact exterior current

Put

\[
                  \Omega=K+x+y+z+w.                       \tag{5.1}
\]

For the owner block \(P^+=(B,C,D,A)\), the internal graded interval-union
deck is

\[
\begin{array}{c|c}
\text{width}&\text{multiset}\\ \hline
1&\{A,B,C,D\},\\
2&\{U_1,U_2,U_3\},\\
3&\{\Omega,\Omega\},\\
4&\{\Omega\}.
\end{array}                                                \tag{5.2}
\]

Reversal gives a value-preserving bijection on every interval, so (5.2)
also holds for \(P^-\). The same statement holds at the literal source
level because \(W^-=\operatorname{rev}W^+\).

The source prefix profiles are

\[
\begin{aligned}
 \operatorname{Pref}(W^+)&=(L_0,B,U_1,\Omega,\Omega),\\
 \operatorname{Pref}(W^-)&=(L_0,A,U_3,\Omega,\Omega),      \tag{5.3}
\end{aligned}
\]

and the suffix profiles are exchanged. Thus the common boundary screen
\(L_0\) removes the first possible current; only packet-take sizes two and
three can differ.

Let \(X\) and \(Y\) be fixed exterior source words. For \(j\ge1\), let

\[
 X_j=\bigcup\{\text{last }j\text{ cells of }X\},\qquad
 Y_j=\bigcup\{\text{first }j\text{ cells of }Y\}.          \tag{5.4}
\]

Write \([R]\) for one unit of multiset mass at mask \(R\). At total width
\(\ell\), the signed crossing current
\(\Delta_\ell=\operatorname{Deck}_\ell(XW^-Y)-
\operatorname{Deck}_\ell(XW^+Y)\) is

\[
\begin{aligned}
\Delta_\ell={}&
 [X_{\ell-2}\cup A]-[X_{\ell-2}\cup B]
 +[X_{\ell-3}\cup U_3]-[X_{\ell-3}\cup U_1]\\
&+[Y_{\ell-2}\cup B]-[Y_{\ell-2}\cup A]
 +[Y_{\ell-3}\cup U_1]-[Y_{\ell-3}\cup U_3],             \tag{5.5}
\end{aligned}
\]

where a term is omitted unless its exterior index is at least one and the
corresponding suffix or prefix exists.

### Theorem 5.1 (four-ray exterior theorem)

Equation (5.5) is the complete exterior all-width defect. All intervals
wholly inside the packet, taking only the common first boundary cell,
taking at least four packet cells, or spanning the whole packet cancel
separately. Hence the only possible contextual changes are the four nested
families

\[
\begin{array}{ll}
 X_j\cup B\leftrightarrow X_j\cup A,&
 X_j\cup U_1\leftrightarrow X_j\cup U_3,\\
 A\cup Y_j\leftrightarrow B\cup Y_j,&
 U_3\cup Y_j\leftrightarrow U_1\cup Y_j.
\end{array}                                                \tag{5.6}
\]

For any fixed exterior union \(R\), each of the two individual left ray
pairs, and likewise each reflected right ray pair, collapses pointwise if
and only if

\[
                              \{y,z\}\subseteq R.           \tag{5.7}
\]

#### Proof

An interval crossing only the left boundary contains an exterior suffix
and a packet prefix. Formula (5.3) gives the first line of (5.5). The
right boundary is the reflected calculation. Internal intervals reverse,
and a two-sided crossing interval contains the complete packet union
\(\Omega\), proving completeness.

For the collapse criterion,

\[
 R\cup A=R\cup B
 \quad\Longleftrightarrow\quad
 \{y,z\}\subseteq R,                                      \tag{5.8}
\]

because \(A-B=\{z\}\) and \(B-A=\{y\}\). Since
\(U_3=A+w\) and \(U_1=B+w\), the identical equivalence holds for the upper
ray:

\[
 R\cup U_3=R\cup U_1
 \quad\Longleftrightarrow\quad
 \{y,z\}\subseteq R.                                      \tag{5.9}
\]

The reflected right pairs are the same equalities with signs reversed.
\(\square\)

Thus internal all-width transparency does not imply fixed-exterior
transparency. A clean sufficient global cancellation is equality of the
left-suffix and right-prefix union profiles, so that the two sides of
(5.5) cancel term by term. Whole-copy reversal gives this transport
functorially. With an arbitrary frozen exterior, the four rays can contain
\(O(|X|+|Y|)\) distinct affected interval occurrences.

Condition (5.7) is a pointwise ray-collapse criterion, not a
necessary-and-sufficient characterization of cancellation of the complete
fixed-width current (5.5). At one width, its two left terms use the
different exterior unions \(X_{\ell-2}\) and \(X_{\ell-3}\), and accidental
cross-cancellation may occur.

## 6. What the actual q-gon fusion does to upper decks

The complete reversal pairs \(G_1,G_2\) and \(G_0,G_3\) in (3.7) have
identical componentwise cyclic interval-union decks at every width. This
is the exact all-width statement for the role conversion and for the two
endpoint states.

The topology-changing rethread \(G_2\to G_3\) is different. At \(d=1\)
the first nonzero graded current is at width four. With

\[
\begin{aligned}
 C_i^*&=S+w+z+a_i+a_{i+1},\\
 D_i^*&=S+w+z+a_{i-1}+a_i+a_{i+1},                       \tag{6.1}
\end{aligned}
\]

one has

\[
 \operatorname{Deck}_4(G_3)-\operatorname{Deck}_4(G_2)
       =\sum_{i\in\mathbb Z_q}([D_i^*]-[C_i^*]).          \tag{6.2}
\]

All \(G_2\) internal OR values still have witnesses in \(G_3\), but their
graded multiplicities are not fixed. Therefore the square reversal closes
the internal all-width role-conversion row, while the direct q-gon fusion
still carries an explicit upper occurrence current and any exterior/source
or compiler casualties.

## 7. Exact proved boundary

The support-four reverse path is:

* a literal shared-boundary two-derivative OR ear;
* owner- and q1-simple inside every q-port phase;
* an \(H=1\), and only \(H=1\), saturated MTF-liftable path;
* a component-neutral complete reversal; and
* internally all-width transparent.

It is not:

* an \(H\ge2\) MTF/resident return;
* a two-component fusion or a legal \(q=2\) q-gon;
* a fixed-exterior balanced switch;
* pointwise transparent across arbitrary exterior windows; or
* by itself a common-cap/compiler theorem.

The exact positive direct-fusion architecture is therefore

\[
 \boxed{
  \text{q disjoint direct+return port cycles}
   \xrightarrow{\text{square role conversion }(\Delta c=0)}
  \text{q forward port cycles}
   \xrightarrow{\text{q-gon rethread }(\Delta c=-(q-1))}
  \text{one cycle}.}
\]

For a growing-depth theorem, replace the bare square rail by the
authenticated \(2d+1\)-edge resident return rail. For arbitrary disjoint
whole-copy fusion, one must additionally construct the endpoint joins and
one concrete literal source chronology, or reverse the completed exterior
copies as a whole. Neither conclusion follows from the open square alone.

## 8. Dependencies and independent audit

The proof uses the exact constructions and no finite search:

* MATH_THEOREM_QGON_PROJECTION_COMPOSITION_AND_CLOSED_DOUBLETONGATE_20260801.md;
* MATH_THEOREM_D2_SUPPORT4_ROLE_CONVERTER_AND_PROTECTED_PROJECTIONS_20260801.md;
* MATH_THEOREM_QPORT_RESIDENT_RAIL_ROLE_CONVERTER_20260801.md;
* MATH_THEOREM_THREAD_D_OPEN_C4_ONE_COPY_EULER_FUSION_AND_PARITY_GATE_20260801.md;
* MATH_ATTACK_AD_ADAPTIVE_MTF_FUSION_AUDIT_20260724.md; and
* MATH_THEOREM_AD_RESET_RETURN_RAIL_LINEAR_OPENING_AND_WHOLE_COPY_FUSION_20260801.md.

The decisive MTF gap, component ledger, immediate palettes, and exterior
prefix/suffix identities were independently rederived from the displayed
sets. No statement here promotes owner-endpoint equality to equality of
complete MTF states, and no statement calls the q-gon rethread graded
all-width transparent.
