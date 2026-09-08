# The Kneser near-core: an exact critical-rate rounding reduction and a rectangle-switch obstruction

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Put

\[
 \Omega=[2m],\qquad
 \mathcal L=\binom{\Omega}{m-1},\qquad
 \mathcal M=\binom{\Omega}{m},
\]

\[
 W=|\mathcal M|=\binom{2m}{m},\qquad
 N=|\mathcal L|=\binom{2m}{m-1},\qquad
 D=W-N={W\over m+1}=\operatorname {Cat}_m .                  \tag{0.1}
\]

The Mersenne parity obstruction to an exact Kneser 1-factor disappears
asymptotically, but the required near-core does **not** follow from an
ordinary near-perfect matching theorem.  There is an exact four-uniform
rounding formulation in which the necessary residual is already at the
critical scale

\[
                         D=\Theta(W/m).                         \tag{0.2}
\]

More precisely, let

\[
 \mathcal P=\mathcal M/(X\sim X^c)                             \tag{0.3}
\]

be the set of complementary middle-owner pairs, and give every
\(P\in\mathcal P\) two clones \(P^0,P^1\).  There is a canonical
four-uniform hypergraph \(\mathfrak K_m\) on

\[
                  \mathcal L\ \dot\cup\ (\mathcal P\times\{0,1\})
                                                                    \tag{0.4}
\]

with the following properties.

1. A matching of \(\mathfrak K_m\) projects to a simple Kneser matching
   whose Johnson lift has degree at most two at every middle owner.
2. The exact symmetric fractional point has value \(N/2\), saturates
   every Kneser vertex, and leaves exactly \(D\) units of owner-clone
   slack.  This is the fractional optimum.
3. If an integral matching leaves \(u\) Kneser vertices uncovered, it
   can be completed to a simple Kneser edge cover \(Q\) satisfying

   \[
      |Q|\le {N\over2}+{u\over2},                              \tag{0.5}
   \]

   and the canonical Johnson lift has degree outside \(\{0,2\}\) at
   at most

   \[
                          2D+6u                                \tag{0.6}
   \]

   middle owners.

Consequently the requested owner statement follows from the sharply
quantified assertion

\[
 \boxed{\text{there is a matching of \(\mathfrak K_m\) with
              \(u=O(D)\).}}                                   \tag{CR}
\]

The component statement has one additional, equally explicit gate.  If
the degree-at-most-two lift of that matching has \(c=O(D)\) cycle
components, then after completion the total number of nontrivial
components is \(O(D)\).  For

\[
                         H=\sqrt m\,\omega,qquad \omega=\log\log m,
                                                                    \tag{0.7}
\]

this is

\[
                       O(D)=o(W/H).                              \tag{0.8}
\]

Thus \((\mathrm {CR})\), together with \(c=O(D)\), is a sufficient
integral theorem for the requested asymptotic Kneser near-core, in every
dimension including the Mersenne dimensions.

This note does not prove \((\mathrm {CR})\).  It does prove that the two
suggested soft mechanisms do not supply it:

* independent rounding of the exact symmetric point leaves
  \((1-3e^{-2}+o(1))W\) bad middle owners in expectation and a positive
  fraction of Kneser vertices uncovered;
* the elementary alternating Kneser rectangle switch changes four
  complementary owner-pair loads by \(-1,-1,+1,+1\).  Starting from an
  exact \(0/2\) lift, every nondegenerate rectangle switch creates at
  least eight bad middle owners.  Hence the exact \(0/2\) locus has no
  edges in the elementary rectangle-switch graph.

The surviving problem is therefore a critical-rate **correlated**
rounding, followed by balanced multi-rectangle switches.  An
unparameterized \(o(W)\) nibble and isolated alternating rectangles are
provably insufficient.  No quantitative obstruction to the existence of
the near-core itself is obtained here.

## 1. Complementary owner-pairs are the correct capacity resources

Let \(e=\{R,S\}\) be an edge of \(KG(2m,m-1)\).  Write its two-point
leave as

\[
                     \Omega\setminus(R\cup S)=\{a,b\}.          \tag{1.1}
\]

The canonical Johnson lift of \(e\) consists of

\[
 \{R+a,R+b\},\qquad \{S+a,S+b\}.                               \tag{1.2}
\]

Its four middle owners form two complementary pairs

\[
 P_a(e)=[R+a]=\{R+a,S+b\},\qquad
 P_b(e)=[R+b]=\{R+b,S+a\}.                                    \tag{1.3}
\]

Here \([X]=\{X,X^c\}\).  Notice that one lifted Kneser edge contributes
degree one at both owners in each of the two resources \(P_a(e),P_b(e)\).
It is therefore wrong to clone \(X\) and \(X^c\) independently: those
two clone coordinates would have codegree of order \(m^2\).  Quotienting
by complementation first removes that artificial high codegree.

### Definition 1.1 (the complement-pair clone hypergraph)

The vertex set of \(\mathfrak K_m\) is (0.4).  For every Kneser edge
\(e=\{R,S\}\) and every \((\alpha,\beta)\in\{0,1\}^2\), insert

\[
             \{R,S,P_a(e)^\alpha,P_b(e)^\beta\}.               \tag{1.4}
\]

The unordered names \(a,b\) merely interchange the last two entries, so
the four-edge fibre over \(e\) is canonical.

### Lemma 1.2 (literal meaning of an auxiliary matching)

Let \(\mathcal F\) be a matching in \(\mathfrak K_m\), and let \(Q_0\)
be its set of projected Kneser edges.  Then

1. \(Q_0\) is a simple Kneser matching;
2. for every \(P=[X]\in\mathcal P\),

   \[
      d_{H(Q_0)}(X)=d_{H(Q_0)}(X^c)
       =\#\{\alpha:P^\alpha\text{ is used by }\mathcal F\}
       \in\{0,1,2\}.                                         \tag{1.5}
   \]

#### Proof

Two auxiliary edges whose Kneser projections meet share their common
\(\mathcal L\)-vertex, so their projections cannot both occur in a
matching.  Two lifts of the same Kneser edge share both lower vertices,
so the projection is simple.  By (1.3), a projected edge contributes
degree one at \(X\) exactly when its auxiliary lift uses one of the two
clones of \([X]\).  A matching uses each clone at most once, proving
(1.5). \(\square\)

## 2. Exact degrees, codegrees, and the symmetric optimum

Let

\[
                         \Delta=\binom{m+1}{2}                  \tag{2.1}
\]

be the degree of \(KG(2m,m-1)\).

### Lemma 2.1 (degree ledger)

The two vertex types of \(\mathfrak K_m\) have degrees

\[
 d_{\mathcal L}=4\Delta=2m(m+1),\qquad
 d_{\mathcal P^\ast}=2m^2.                                   \tag{2.2}
\]

Moreover

\[
                         \Delta_2(\mathfrak K_m)\le2m.          \tag{2.3}
\]

For \(m\ge3\), the nonzero pair-codegrees are bounded more precisely by

\[
\begin{array}{c|c}
\text{pair type}&\text{codegree}\ \\ \hline
R,S\in\mathcal L&4\quad\text{if }R\cap S=\varnothing,\\
R\in\mathcal L,\ P^\alpha&2m\quad\text{when }R\subset X
   \text{ or }R\subset X^c,\\
P^\alpha,Q^\beta, P\ne Q&\le1.
\end{array}                                                     \tag{2.4}
\]

#### Proof

A fixed \(R\in\mathcal L\) has \(\Delta\) Kneser neighbours, and every
Kneser edge has four clone lifts.  This gives \(4\Delta\).

Fix \(P=[X]\).  Formula (2.0f) of the Kneser normal form shows that
exactly \(m^2\) Kneser edges have \(P\) among their two owner-pair
resources.  Once the clone \(P^\alpha\) is fixed, the clone of the other
owner-pair has two choices.  Hence its degree is \(2m^2\).

An adjacent pair \(R,S\) lies in the four lifts of its unique Kneser
edge.  If \(R=X-x\), a Kneser neighbour \(S\) produces the pair \([X]\)
exactly when \(x\) is in the two-point leave.  Equivalently,
\(S\subset X^c\), giving \(m\) choices for \(S\) and two choices for the
other clone.  The case \(R\subset X^c\) is identical.  Finally, two
distinct owner-pairs occur together only when suitable representatives
are Johnson-adjacent; the intersection and union then determine the
Kneser edge.  For \(m\ge3\) the two possible complement orientations
cannot both be adjacent.  This proves (2.3)--(2.4). \(\square\)

Thus the relative codegree is at the critical order

\[
 {\Delta_2(\mathfrak K_m)\over\Delta(\mathfrak K_m)}
                         ={1\over m+1}.                         \tag{2.5}
\]

### Theorem 2.2 (exact symmetric fractional optimum)

Give every auxiliary edge the weight

\[
                 w={1\over4\Delta}={1\over2m(m+1)}.            \tag{2.6}
\]

Then every \(R\in\mathcal L\) has fractional load one and every owner
clone has fractional load

\[
                         {m\over m+1}.                          \tag{2.7}
\]

The total fractional matching weight is exactly \(N/2\), which is the
fractional matching optimum.  The total unused owner-clone capacity is
exactly

\[
  W\left(1-{m\over m+1}\right)=D.                              \tag{2.8}
\]

#### Proof

Equations (2.2) and (2.6) give the two asserted loads.  There are
\(4(N\Delta/2)=2N\Delta\) auxiliary edges, so their total weight is
\(N/2\).  Every auxiliary edge uses two vertices of \(\mathcal L\),
whose total capacity is \(N\); hence no fractional matching can have
weight greater than \(N/2\).  Finally there are
\(2|\mathcal P|=W\) owner clones, and (2.7) gives (2.8). \(\square\)

This is precisely the fractional point

\[
 z_{R,S}={1\over\Delta},\qquad a_X={m\over m+1}                \tag{2.9}
\]

from the Kneser normal form: the four clone lifts split the Kneser-edge
weight equally.  In particular, the Catalan discrepancy \(D\) is not an
artifact of rounding.  It is the exact slack forced by the unequal sizes
of the two resource shores.

## 3. The critical-rate completion theorem

### Theorem 3.1 (from an auxiliary matching to a literal edge cover)

Let \(\mathcal F\) be a matching of \(\mathfrak K_m\) of size

\[
                         k={N-u\over2};                         \tag{3.1}
\]

thus exactly \(u\) Kneser vertices are uncovered.  There is a simple
edge cover \(Q\subseteq KG(2m,m-1)\), containing the projection \(Q_0\)
of \(\mathcal F\), such that

\[
                  |Q|\le {N\over2}+{u\over2}.                  \tag{3.2}
\]

Furthermore, if

\[
 \mathcal B(Q)=\{X\in\mathcal M:d_{H(Q)}(X)\notin\{0,2\}\},   \tag{3.3}
\]

then

\[
                         |\mathcal B(Q)|\le2D+6u.              \tag{3.4}
\]

#### Proof

Process the uncovered Kneser vertices.  Whenever an uncovered vertex
\(R\) remains, add one incident Kneser edge.  No edge of \(Q_0\) is
incident with \(R\), and an edge added earlier would already cover it,
so the new edge is not a duplicate.  Each step covers at least one
previously uncovered vertex, and hence at most \(u\) edges are added.
This gives a simple edge cover and

\[
 |Q|\le {N-u\over2}+u={N\over2}+{u\over2}.                    \tag{3.5}
\]

The matching \(\mathcal F\) uses \(2k=N-u\) of the \(W\) owner clones.
It therefore leaves exactly

\[
                         W-(N-u)=D+u                            \tag{3.6}
\]

owner clones unused.  If a complementary owner-pair has degree one in
\(H(Q_0)\), exactly one of its two clones is unused.  Thus at most
\(D+u\) complementary pairs, or at most \(2(D+u)\) individual middle
owners, have degree one in \(H(Q_0)\).

Every added Kneser edge touches exactly two complementary owner-pairs,
hence four individual middle owners.  Put all owners touched by an added
edge into the exceptional set.  Outside that set the degree is unchanged
from \(H(Q_0)\), and (1.5) makes it zero or two.  Since at most \(u\)
edges were added,

\[
 |\mathcal B(Q)|\le2(D+u)+4u=2D+6u,                            \tag{3.7}
\]

as required. \(\square\)

### Corollary 3.2 (the exact owner-rate gate)

If \(u=O(D)\), then

\[
 |Q|={N\over2}+O(W/m),\qquad
 |\mathcal B(Q)|=O(W/m)=o(W/H)                                \tag{3.8}
\]

for every \(H=o(m)\), in particular for (0.7).

The parity of \(N\) is irrelevant: when \(N\) is odd, \(u\) is odd and
may be as small as one.  Thus this completion theorem applies without
change at Mersenne \(m\).

### Proposition 3.3 (the separate component gate)

Let \(c\) be the number of cycle components of \(H(Q_0)\).  The number
of its path components is at most \(D+u\).  The completed lift \(H(Q)\)
has at most

\[
                           c+D+3u                              \tag{3.9}
\]

nontrivial components.  Consequently \(c=O(D)\) and \(u=O(D)\) imply
\(O(D)=o(W/H)\) components.

#### Proof

By Lemma 1.2, \(H(Q_0)\) has maximum degree two.  Its degree-one middle
owners occur in complementary pairs and number at most \(2(D+u)\), by
(3.6).  Every path component has two degree-one endpoints, so there are
at most \(D+u\) path components.  Adding one Kneser edge adds two
Johnson edges and can introduce at most two new nontrivial components.
At most \(u\) Kneser edges are added, proving (3.9). \(\square\)

The natural sufficient cycle condition is therefore not merely
``girth tends to infinity''.  Since the lift has \(\Theta(W)\) edges,
excluding all cycles of length below \(L\) gives only \(O(W/L)\) cycle
components.  To deduce \(o(W/H)\) in this way one needs

\[
                            L/H\longrightarrow\infty,          \tag{3.10}
\]

a growing conflict range.  A fixed-girth diagonal with no explicit rate
does not establish (3.10).

## 4. Why the usual near-perfect theorem misses the needed scale

The maximum degree scale of \(\mathfrak K_m\) is

\[
                    \mathcal D=2m(m+1)=\Theta(m^2),             \tag{4.1}
\]

while (CR) asks for relative uncovered mass

\[
 {u\over N}=O(1/m)=O(\mathcal D^{-1/2}).                       \tag{4.2}
\]

By (2.5), this is also the order of the largest relative codegree.  The
problem is therefore at the first non-negligible dependency scale, not
inside the qualitative \(o(1)\) regime.

A fixed-uniformity near-perfect matching theorem applied to Lemma 2.1
does give

\[
                            u=o(W),                              \tag{4.3}
\]

but (4.3) does not imply (4.2).  For example, an admissible qualitative
error \(W/\log m\) is \(o(W)\) and is nevertheless larger than \(D\) by
a factor asymptotic to \(m/\log m\).  The completion in Theorem 3.1
would then have too many edges and too many bad owners.  Likewise, a
fixed-conflict theorem yielding only an unspecified power
\(\mathcal D^{-\alpha}\) proves (4.2) only if its explicit exponent is at
least \(1/2\), including its endpoint constants.  No such estimate is
contained in the qualitative nibble input.

This is an exact rate obstruction to that proof route.  It is not an
integrality-gap lower bound for \(\mathfrak K_m\).

## 5. Diffuse rounding of the symmetric point has linear loss

The symmetric point also explains why independent rounding cannot be
the missing quantitative argument.

### Proposition 5.1 (Poisson owner obstruction for independent rounding)

Select every Kneser edge independently with probability

\[
                              p={1\over\Delta}.                 \tag{5.1}
\]

For a fixed middle owner \(X\), its lifted degree is exactly

\[
 d_{H(Q)}(X)\sim\operatorname {Bin}(m^2,1/\Delta).             \tag{5.2}
\]

Consequently

\[
 \Pr\bigl(d_{H(Q)}(X)\in\{0,2\}\bigr)
   =(1-p)^{m^2}+\binom{m^2}{2}p^2(1-p)^{m^2-2}
   =3e^{-2}+o(1).                                               \tag{5.3}
\]

The expected number of bad middle owners is therefore

\[
                       (1-3e^{-2}+o(1))W.                       \tag{5.4}
\]

Moreover, for every \(R\in\mathcal L\),

\[
 d_Q(R)\sim\operatorname {Bin}(\Delta,1/\Delta),qquad
 \Pr(d_Q(R)=0)=e^{-1}+o(1),                                    \tag{5.5}
\]

so a positive fraction of lower targets is uncovered in expectation.

#### Proof

The \(m^2\) pairs

\[
                 \{X-x,X^c-y\},\qquad(x,y)\in X\times X^c,    \tag{5.6}
\]

are distinct Kneser edges, giving (5.2).  Since
\(m^2/\Delta=2m/(m+1)\to2\), the two binomial probabilities in
(5.3) tend to \(e^{-2}\) and \(2e^{-2}\).  Kneser regularity gives
(5.5). \(\square\)

Thus the symmetric point must be rounded by a highly polarized dependent
law: almost every owner-pair must receive either both clones or neither,
while almost every Kneser vertex must receive exactly one selected edge.
Correct marginals alone do not begin to enforce this correlation.

## 6. Exact effect of an alternating rectangle switch

Alternating-cycle switches remain the complete reconfiguration space for
Kneser matchings.  The smallest such switch, however, has a rigid owner
signature.

Let

\[
 \Omega=C\ \dot\cup\ D_0\ \dot\cup\{u,v,s,t\},qquad
 |C|=|D_0|=m-2,                                                 \tag{6.1}
\]

and consider the old matching edges

\[
 e_1=\{C+u,D_0+s\},\qquad e_2=\{C+v,D_0+t\},                  \tag{6.2}
\]

and the other parity class of their Kneser 4-cycle,

\[
 e_3=\{C+u,D_0+t\},\qquad e_4=\{C+v,D_0+s\}.                  \tag{6.3}
\]

Define the five complementary owner-pairs

\[
\begin{aligned}
 A&=[C+u+v],\\
 B&=[C+u+t],& E&=[C+v+s],\\
 F&=[C+u+s],& G&=[C+v+t].
\end{aligned}                                                  \tag{6.4}
\]

For \(m\ge3\), these five pairs are distinct.

### Theorem 6.1 (rectangle transport identity)

Replacing \(e_1,e_2\) by \(e_3,e_4\) preserves the load at \(A\) and
changes the other owner-pair loads by

\[
                   -\mathbf e_B-\mathbf e_E
                    +\mathbf e_F+\mathbf e_G.                  \tag{6.5}
\]

Equivalently, on individual middle-owner degrees the same signed change
occurs simultaneously at both members of every pair in (6.5).

#### Proof

The two-point leaves in (6.2) are \(\{v,t\}\) and \(\{u,s\}\).
Equations (1.3) therefore give the owner-pair multisets

\[
                         \{A,B\},\qquad\{A,E\}.                \tag{6.6}
\]

The leaves in (6.3) are \(\{v,s\}\) and \(\{u,t\}\), giving

\[
                         \{A,F\},\qquad\{A,G\}.               \tag{6.7}
\]

Subtracting (6.6) from (6.7) proves (6.5). \(\square\)

### Corollary 6.2 (elementary-switch freeze of the exact locus)

Suppose before the switch every middle-owner degree belongs to
\(\{0,2\}\).  After any nondegenerate switch (6.2)--(6.3), all four
complementary pairs \(B,E,F,G\) have odd degree.  Hence at least eight
middle owners leave the \(0/2\) locus.

In particular, the graph whose vertices are exact \(0/2\) Kneser
matchings and whose edges are single alternating rectangle switches has
no edges.

#### Proof

The selected old edges show that the pre-switch loads at \(B,E\) are
positive.  Under the \(0/2\) hypothesis they are two, and (6.5) changes
them to one.  The pre-switch loads at \(F,G\) are zero or two, and
(6.5) changes them to one or three.  Distinctness in (6.4) gives eight
bad individual owners. \(\square\)

This does not obstruct a balanced composition of rectangles: later
switches may cancel all four signed defects.  It does show exactly what a
successful switch proof must contain.  One must construct a circulation
of rectangle signatures (6.5), not greedily join owner cycles by isolated
4-cycle flips.  If the intermediate states are also required to keep an
\(o(W/H)\) exceptional set, those circulations must be scheduled with the
same small active boundary.

The same statement has an exact form for an arbitrary alternating cycle.
Let \(C\) be an even cycle of the Kneser graph, with old and new parity
classes \(C^-\) and \(C^+\).  For every complementary owner-pair \(P\),
put

\[
 \delta_C(P)=
   |\{e\in C^+:P\in\{P_a(e),P_b(e)\}\}|
  -|\{e\in C^-:P\in\{P_a(e),P_b(e)\}\}|.                     \tag{6.8}
\]

### Proposition 6.3 (parity boundary of a general alternating switch)

Switching \(C^-\) to \(C^+\) changes both individual owner degrees in
\(P\) by exactly \(\delta_C(P)\).  In particular:

1. an exact \(0/2\) lift can be carried to another exact \(0/2\) lift
   only if

   \[
                         \delta_C(P)\equiv0\pmod2
                         \quad(P\in\mathcal P);                \tag{6.9}
   \]

2. if the initial load of \(P\) is zero, then an exact-to-exact switch
   has \(\delta_C(P)\in\{0,2\}\), while if its initial load is two, then
   \(\delta_C(P)\in\{0,-2\}\);
3. more generally, if the lifts before and after the switch are exact
   outside exceptional owner-pair sets \(B^-\) and \(B^+\), then the odd
   boundary

   \[
      \partial_{\mathcal P}C
       =\{P:\delta_C(P)\text{ is odd}\}                        \tag{6.10}
   \]

   is contained in \(B^-\cup B^+\).

#### Proof

Every old Kneser edge incident with the resource \(P\) removes one from
the degrees of both owners in \(P\), and every new edge adds one.  This
is (6.8).  The difference of two numbers in \(\{0,2\}\) is even and has
the sign restrictions in assertion 2.  If both endpoint degrees are even
outside \(B^-\cup B^+\), their difference is even there, proving
assertion 3. \(\square\)

For the rectangle of Theorem 6.1, the parity boundary is exactly
\(\{B,E,F,G\}\).  Thus a route staying inside the exact locus cannot use
individual rectangles at all.  It must use longer alternating cycles, or
compose rectangles so that their four-point parity boundaries cancel.
This is the precise balanced-switch condition left by the normal form.

## 7. Exact remaining theorem

The requested near-core follows from the following self-contained
statement.

> **Critical Kneser rounding-and-routing theorem.**  There is a matching
> \(\mathcal F\) in \(\mathfrak K_m\) which leaves \(O(D)\) vertices of
> \(\mathcal L\) uncovered and whose projected Johnson lift has
> \(O(D)\) cycle components.

Indeed, Theorem 3.1 and Proposition 3.3 then give a simple Kneser edge
cover \(Q\) with

\[
 |Q|={N\over2}+O(W/m),\qquad
 |\mathcal B(Q)|=O(W/m),\qquad
 \operatorname {comp}(H(Q))=O(W/m).                            \tag{7.1}
\]

For \(H=\sqrt m\log\log m\), both latter quantities are \(o(W/H)\).

The exact symmetric point proves that this theorem has no fractional
capacity obstruction.  Proposition 5.1 rules out diffuse independent
rounding, and Corollary 6.2 rules out an exact-locus walk by elementary
rectangles.  What remains is a genuinely dependent critical-scale
rounding, or an explicit dual/odd-set obstruction to that rounding, plus
a balanced multi-rectangle circulation controlling the cycle count.

No such integral theorem or obstruction is proved here; consequently no
literal near-core construction is claimed.

## 8. Subsequent exact switch progress

The single-rectangle freeze in Corollary 6.2 is not a freeze of the full
alternating-switch space.  The subsequent note
MATH_THEOREM_KNESER_ZERO_SIGNATURE_HEXAGON_AND_CRITICAL_AUGMENTER_20260726.md
proves two exact families.

1.  For every two distinct lower vertices \(R,S\), with
    \(t=|R\cap S|\), there is a \((2t+1)\)-edge alternating path replacing
    \(t\) old edges by \(t+1\) new ones whose owner signature is exactly

    \[
                 \mathbf e_{[R+h]}+\mathbf e_{[S+h]}
    \]

    for any chosen \(h\notin R\cup S\).  Thus it is an auxiliary-matching
    augmenter whenever all old edges are present and the two terminal
    owner pairs each have a free clone.
2.  There is an explicit six-coordinate alternating Kneser hexagon whose
    two parity classes have exactly the same owner-resource multiset.  It
    is therefore a zero-signature \(3\)-for-\(3\) switch, and it can splice
    three quotient owner cycles without changing any degree.

For fixed \(R\), the exact number of oriented depth-\(t\) augmenter
templates is

\[
                    (m-1)_t(m+1)_{t+2}.                       \tag{8.1}
\]

After normalization by \(\Delta^t\), this is
\((1+o(1))2^tm^2\) for \(t=o(\sqrt m)\).  Hence logarithmic length
\(t=\log_2m+O(1)\) is exactly the first scale at which the diffuse
augmenter inventory remains visible at a Catalan-size leave.  The new
residual is a correlation-robust supersaturation theorem for those
logarithmic augmenters, plus availability of the zero-signature hexagons;
the local directions themselves are no longer missing.
