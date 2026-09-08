# Audit of the swapped-stratum endpoint law at the fixed-`M_0` phase interface

Date: 2026-08-01  
Lane: two swapped controlled-leave strata / rooted phase compatibility  
Status: the endpoint-cocycle calculation passes after replacing the
unrooted packet by a phase-compatible packet with the same excess vector.
Local planted incidence rows and typed cross-stratum resource conditions
are exact.  Extension of the planted rows to one perfect `M_0`, the exit
square-SDR, and the residual physical forest are not proved.

## 0. Audit verdict

Put

\[
 C=\operatorname {Cat}_m,\qquad c=\operatorname {Cat}_{m-1},
 \qquad I=C-2c.
\]

The singleton-coordinate conclusion of
`MATH_THEOREM_TWO_STRATUM_PACKET_COORDINATE_COCYCLE_FEASIBILITY_20260801.md`
is correct, but its abstract owner-slot packet is not by itself a
fixed-`M_0` certificate.  There is a literal correction: a canonical
C-phase packet has exactly the same signed coordinate excess.  The two
swapped strata therefore still give

\[
 E_\alpha=C+s_\alpha,\qquad E_\beta=C+s_\beta,
 \qquad E_t=C\quad(t\notin\{\alpha,\beta\}),       \tag{0.1}
\]

and hence

\[
 h=E-2c\mathbf1.                                    \tag{0.2}
\]

Moreover, the abstract hole family can be chosen before the Kneser
circulation and the circulation can then avoid its one-special-coordinate
members.  Thus the endpoint vector and literal lower-hole avoidance are
jointly feasible for all sufficiently large `m`.

What remains open is not a scalar endpoint row.  It is the conjunction of

1. extending a Catalan-size partial incidence matching to one perfect
   `M_0`, or realizing the same bank inside one SCD;
2. choosing the exit labels with all typed target and owner resources
   disjoint; and
3. constructing the residual physical forest and later compiler state.

## 1. The phase-compatible packet has the same excess

Let

\[
 \Omega=G\mathbin{\dot\cup}\{a,z\},\qquad |G|=2m-3,
 \qquad r=m-2.
\]

Take disjoint `S,J in binom(G,r)` and put

\[
 L=G-J=S+u                                             \tag{1.1}
\]

for the unique point `u` outside `S union J`.  Choose `b in J` and put

\[
 U=L+b,\qquad V=S+b.                                  \tag{1.2}
\]

The mixed-head auxiliary provider and its corrected replacement are

\[
\boxed{
 (azL,aS;\ aL,azS)
 \quad\longmapsto\quad
 (aU,aS;\ aL,aV)
 \ +\
 (azL,zS;\ azS,zL). }                                \tag{1.3}
\]

This is the tight one-to-two augmenter with lower `aS`, added letters
`u,b,z`, and deleted letter `a`.  It is in C-phase when the planted
incidence rows are

\[
                         M_0(aS)=aL,qquad
                         M_0(zS)=azS,qquad
                         M_0(L)=zL.                  \tag{1.4}
\]

The first two rows orient the old and target diamonds; the third orients
the rerouted auxiliary diamond.  Thus (1.3), unlike a raw owner-slot
identity, is a literal rooted packet under (1.4).

Reserve both slots at the old physical endpoints `aL,azS`, one slot at
the new endpoints `aV,zL`, and the displayed two upper and two lower
resources.  The signed change in the forced lower-hole vector is

\[
\begin{aligned}
 \delta_{a,z}(S,L)
 &=2\chi_{aL}+2\chi_{azS}+\chi_{aV}+\chi_{zL}\\
 &\quad-\chi_{aS}-\chi_{zS}-\chi_{azL}-\chi_{aU}\\
 &=2\chi_{\{a\}}+\chi_{\{z\}}+\chi_S+\chi_L.       \tag{1.5}
\end{aligned}
\]

Indeed the ordinary-coordinate part is

\[
 3\chi_L+2\chi_S+\chi_V-2\chi_S-\chi_L-\chi_U
 =\chi_L+\chi_S,                                    \tag{1.6}
\]

because `U=L+b` and `V=S+b`.  Equation (1.5) is exactly the
excess vector used by the abstract two-stratum theorem.

## 2. Exact local common-`M_0` rows and the extension gate

Let `P=P_alpha dotcup P_beta` be a `C`-vertex directed Kneser
circulation.  For `S in P`, let `J(S)` be its successor and set
`L(S)=G-J(S)`.  Distinct circulation vertices give distinct `S` and
distinct `L`.

For the `(alpha,beta)` stratum plant

\[
 \alpha S\mapsto\alpha L,qquad
 \beta S\mapsto\alpha\beta S,qquad
 L\mapsto\beta L.                                  \tag{2.1}
\]

For the swapped `(beta,alpha)` stratum plant

\[
 \beta S\mapsto\beta L,qquad
 \alpha S\mapsto\alpha\beta S,qquad
 L\mapsto\alpha L.                                 \tag{2.2}
\]

Across all selected indices these `3C` rows form a partial incidence
matching.  Its domain and image sets are independent of the stratum labels:

\[
 \mathcal D_P=
 \{\alpha S,\beta S,L(S):S\in P\},\qquad
 \mathcal I_P=
 \{\alpha L(S),\beta L(S),\alpha\beta S:S\in P\}. \tag{2.3}
\]

Every map is injective, coordinate signatures separate the three banks,
and all displayed containments are literal.  This proves local planted
phase compatibility.  It does **not** prove that the partial matching
extends to a perfect incidence matching.

Let `B_m` be the rank-`(m-1)` to rank-`m` Boolean incidence graph.  The
exact remaining common-`M_0` condition is

\[
 \boxed{
 |N_{B_m}(X)\setminus\mathcal I_P|\ge |X|
 \quad\text{for every }X\subseteq
 {\Omega\choose m-1}\setminus\mathcal D_P.}        \tag{2.4}
\]

By Hall, (2.4) is necessary and sufficient for the `3C` planted rows to
extend to one perfect `M_0`.  No assertion that (2.4) always holds is made.

There is a stronger sufficient SCD face.  If all selected `S<L(S)` are
central edges of one SCD, then on every long chain the four-row matching
is identical under swapping `alpha,beta`; the canonical packet uses
D-phase.  On each short chain either of the two three-cycle orientations
(2.1)--(2.2) may be chosen according to its stratum label.  This explicitly
gives one common `M_0`.  The abstract Kneser circulation theorem does not
prove that its prescribed edges lie in such an SCD, so this sufficient
face does not remove (2.4) in general.

## 3. Exact cross-stratum resource conditions

Choose `b(S) in J(S)` and put

\[
 U_S=L(S)+b(S),\qquad V_S=S+b(S).                  \tag{3.1}
\]

The physical owner banks are

\[
\begin{array}{c|cccc}
\text{stratum}&\text{old 1}&\text{old 2}&\text{new 1}&\text{new 2}\\ \hline
(\alpha,\beta)&\alpha L&\alpha\beta S&\alpha V&\beta L\\
(\beta,\alpha)&\beta L&\alpha\beta S&\beta V&\alpha L.
\end{array}                                        \tag{3.2}
\]

The lower banks are `alpha S,beta S`; the auxiliary upper bank is
`alpha beta L`; and the target upper banks are respectively `alpha U`
and `beta U`.  Consequently the following stronger-than-necessary
conditions are sufficient for complete typed resource disjointness:

\[
\begin{array}{ll}
 U_S\text{ is injective inside each stratum},&
 V_S\text{ is injective inside each stratum},\\
 \{V_S:S\in P\}\cap\{L(S):S\in P\}=\varnothing.&  \tag{3.3}
\end{array}
\]

Under (3.3), all same-signature owner collisions, including the two
cross-stratum collisions `alpha V=alpha L` and `beta V=beta L`, are
excluded.  Different target strata are separated by `alpha,beta`.
The physical replacement edges are then a matching, so the two
union--find guards pass automatically in an isolated halo.

Condition (3.3) is a coloured square-SDR.  Raw list size `m-2` does not
prove it for an arbitrary circulation.  A spread circulation with bounded
induced collision degree admits the same local-lemma proof as the
one-stratum phase atlas, but constructing such a circulation jointly with
(2.4) remains open.

## 4. Endpoint counts and the exact hole family

Assign

\[
 s_\alpha=|P_\alpha|,qquad s_\beta=|P_\beta|,
 \qquad s_\alpha+s_\beta=C,                         \tag{4.1}
\]

with

\[
                         I\le s_\alpha,s_\beta\le2c. \tag{4.2}
\]

Along the Kneser circulation, `L(S)=G-J(S)` gives

\[
 \sum_{S\in P}(\chi_S+\chi_{L(S)})=C\mathbf1_G.    \tag{4.3}
\]

Equations (1.5) and (4.3) prove

\[
\begin{aligned}
 E_\alpha&=C+s_\alpha,&
 h_\alpha&=C+s_\alpha-2c,\\
 E_\beta&=C+s_\beta,&
 h_\beta&=C+s_\beta-2c,\\
 E_t&=C,&h_t&=I\quad(t\in G).                      \tag{4.4}
\end{aligned}
\]

Put

\[
 n_2=2I,qquad n_\alpha=s_\alpha-I,qquad
 n_\beta=s_\beta-I.                               \tag{4.5}
\]

An exact typed hole family is equivalent to simple families

\[
 \mathcal B\subseteq{G\choose m-3},\qquad
 \mathcal A_\alpha,\mathcal A_\beta
       \subseteq{G\choose m-2}                     \tag{4.6}
\]

of orders `n_2,n_alpha,n_beta` satisfying

\[
 \deg_{\mathcal B}(t)+\deg_{\mathcal A_\alpha}(t)
 +\deg_{\mathcal A_\beta}(t)=I
 \quad(t\in G).                                    \tag{4.7}
\]

The holes are

\[
 \alpha\beta\mathcal B\ \dot\cup\
 \alpha\mathcal A_\alpha\ \dot\cup\
 \beta\mathcal A_\beta.                           \tag{4.8}
\]

The balanced-family argument in the source theorem proves (4.6)--(4.7)
without packet-avoidance constraints.

## 5. Hole avoidance and circulation can be ordered positively

Choose the families in (4.6) first and put

\[
 \mathcal F=\mathcal A_\alpha\cup\mathcal A_\beta.
\]

Their total prescribed size is

\[
 |\mathcal A_\alpha|+|\mathcal A_\beta|
 =4c-C={6c\over m+1}.                              \tag{5.1}
\]

Let `N=binom(2m-3,m-2)=(m/2)c` be the order of the odd Kneser graph.
For all sufficiently large `m`, it has a `C`-vertex disjoint cycle union
avoiding `mathcal F`.

Indeed, a cycle-cover matching has at least `N/3` edges.  Removing all
edges incident to `mathcal F` loses at most `|mathcal F|` edges, while

\[
                         {N\over3}-|\mathcal F|>{C\over2}        \tag{5.2}
\]

for all sufficiently large `m`.  If `C` is even, take `C/2` surviving
edges as directed two-cycles.  If `C` is odd, first take a coordinate
translate of the standard odd cycle of length `2m-3` which avoids
`mathcal F`; one exists because its expected intersection with
`mathcal F` is

\[
 { (2m-3)|\mathcal F|\over N}<1                   \tag{5.3}
\]

for all sufficiently large `m`.  Delete its vertices and fill the
remaining even order with surviving matching edges.  The polynomial-size
loss in (5.3) is negligible compared with (5.2).

For the resulting circulation `P`, we have

\[
 P\cap(\mathcal A_\alpha\cup\mathcal A_\beta)=\varnothing.     \tag{5.4}
\]

The packet lower bank is exactly
`{alpha S,beta S:S in P}`.  Hence (5.4) makes every hole in (4.8)
distinct from every reserved lower resource.  This proves joint
endpoint-degree feasibility and literal lower-hole avoidance.  It does not
address the incidence-extension or exit-resource gates.

## 6. Proof-safe final scope

The following claims are proved:

* the corrected packet (1.3) is a legal tight augmenter;
* its signed excess is exactly the abstract vector (1.5);
* the two swapped packet labels produce a resource-disjoint `3C`-row
  partial incidence matching;
* (2.4) is the exact common-`M_0` extension criterion;
* (3.3) is a sufficient typed cross-stratum exit condition; and
* for all sufficiently large `m`, the exact hole family and a `C`-vertex
  Kneser circulation can be chosen with disjoint lower resources.

The note does **not** prove (2.4), the square-SDR (3.3), an SCD containing
the prescribed circulation, residual upper/slot saturation, graphic
connectivity, residence, or a compiler theorem.  In particular it does not
turn the coordinate-feasible two-stratum theorem into a completed
upper-exact rooted forest.
