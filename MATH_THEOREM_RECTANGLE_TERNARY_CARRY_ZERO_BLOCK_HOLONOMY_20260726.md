# Tensor rectangles plus the phase-dense ternary carry: zero block holonomy and the residual physical Hall cut

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web input
is used.

## 0. Verdict

The eight-owner rectangle gives a genuine two-carrier kernel inside one
packet, and the phase-dense ternary carry gives genuine state-dependent
shore choices.  These two facts do not compose into state-dependent orders
of the tensor packets.

The obstruction is an exact semiconjugacy.  Colour every physical edge by
the tensor packet in which its coordinates lie.  A rectangle shore switch
replaces an edge by another edge of the same packet colour.  The carry uses
only phase-aligned rectangle switches.  Consequently its block-colour word
is

\[
                 1,2,\ldots,t
        \quad\hbox{repeated four times per macroperiod},          \tag{0.1}
\]

in every binary, syndrome, and ternary state.  In particular, the
base-three odometer has trivial image in the permutation group of the
packet indices.  It changes the local carrier inside a port, but it never
changes the order of the ports.

This gives an all-target Hall cut which does not assume one common order for
all cycles.  It allows every rectangle shore at every port, every ternary
predicate, every syndrome translate, every component choice, and every
correlation among those choices.  It uses only the invariant quotient word
(0.1) and the canonical first-\(t\)-eligible-packet rule.

For a bare six-coordinate rectangle packet, the exact reached fractions at
signed depth \(q\le t\), \(q=o(m)\), are bounded by

\[
 \boxed{
 {R_q^-\over \binom{2m}{m-q}}
 \le C m^{5/2}(q+1)
       \left({3(m+q)\over7m-q}\right)^q,}             \tag{0.2}
\]

\[
 \boxed{
 {R_q^+\over \binom{2m}{m-q}}
 \le C m^{5/2}(q+1)
       \left({2(m+q)\over3m+q}\right)^q.}             \tag{0.3}
\]

Here \(R_q^\pm\) is the number of distinct literal targets reached from the
good canonical macrocells.  The exponentially small bad-owner leave may add
at most its cardinality to either image.

For the 24-owner local support used by the audited ternary carry, both signs
instead obey

\[
 \boxed{
 {R_{q,H}^\pm\over \binom{2m}{m-q}}
 \le C m^{5/2}(q+1)
       \left({5(m+q)\over8m+2q}\right)^q.}            \tag{0.4}
\]

Thus at every fixed Gaussian depth \(q=A\sqrt m+O(1)\), the right sides of
(0.2)--(0.4) are exponentially small in \(\sqrt m\).  Since

\[
 {\binom{2m}{m-q}\over\binom{2m}{m}}
       =e^{-A^2+o(1)},                                \tag{0.5}
\]

each sign has \((e^{-A^2}-o(1))W\) holes.  At
\(q=\lceil20\log m\rceil\), (0.4) already gives \(W-o(W)\) holes in
each sign.

Within the proposed single-atlas H composition, the exact missing primitive
is therefore not another rectangle shore or a denser carry predicate.  It
is a **ported block-transposition trade**: an
exact phase-compatible owner trade whose two shores assign different packet
colours to at least one common phase.  Such a trade necessarily overlaps
two tensor packets.  It is absent from the disjoint rectangle tensor and
from the proved ternary-carry generator library.

## 1. The eight-owner rectangle and its packet colour

Let

\[
 P=\{u,v\},\qquad A=\{a,b,c,d\},
\]

and let

\[
 \mathcal R=P\times A
 =\{\{p,x\}:p\in P,\ x\in A\}.                       \tag{1.1}
\]

For a perfect matching \(M\) of \(A\), the two sets

\[
 Q(P,E)=\{\{p,x\}:p\in P,\ x\in E\},\qquad E\in M, \tag{1.2}
\]

are two disjoint physical squares partitioning \(\mathcal R\).  The three
matchings

\[
 ab\mid cd,\qquad ac\mid bd,\qquad ad\mid bc          \tag{1.3}
\]

are the three rectangle shores.  Notice the following elementary but
decisive fact: every edge of every shore has both endpoints in the same
six-coordinate support \(P\dot\cup A\).

There is one phase-compatibility qualification.

### Lemma 1.1 (two-shore phase compatibility and the three-shore obstruction)

Any two distinct shores in (1.3) have a common owner colouring by
\(\mathbb Z_4\) which is cyclic on every square of both factors.  No such
colouring exists simultaneously for all three shores.

#### Proof

For two distinct matchings, their union on \(A\) is a four-cycle.  Write it
as \(x_0x_1x_2x_3x_0\), and define

\[
 \begin{array}{c|cc}
       &x_0,x_2&x_1,x_3\\ \hline
 u&0&1\\
 v&3&2
 \end{array}.                                                    \tag{1.4}
\]

For every edge between an even and an odd vertex of this four-cycle, the
corresponding physical square has cyclic colours \(0,1,2,3\), up to
rotation or reversal.  The edges of each of the two matchings are among
these four edges, proving common compatibility.

For the negative assertion, suppose all three shores have a common cyclic
colouring.  Put \(a_x=c(u,x)\) and \(b_x=c(v,x)\).  Every pair \(xy\) is
an edge of one of the three perfect matchings.  On its square, diagonally
opposite vertices have colours differing by two, so

\[
                         b_x=a_y+2\pmod4              \tag{1.5}
\]

for all distinct \(x,y\in A\).  Fixing \(x\) makes the three values
\(a_y\), \(y\ne x\), equal.  Varying \(x\) makes all four \(a_y\) equal,
contradicting adjacency of \((u,x)\) and \((u,y)\) on the square belonging
to the matching containing \(xy\). \(\square\)

Thus phase compatibility permits an H-style construction to use either
member of a chosen pair of rectangle shores with one common phase map; this
does not by itself construct the carry state bijection.  Simultaneously
invoking all three shores would require an additional phase-extension
gadget.  The support Hall bounds below deliberately allow all three and are
therefore valid a fortiori for every phase-compatible two-shore carry.

Tensor \(t\) copies on disjoint supports \(B_1,\ldots,B_t\).  Colour an
edge by \(i\) when its two endpoints differ only in \(B_i\).  Every edge in
every product rectangle shore has one well-defined colour, and changing the
shore in copy \(i\) preserves that colour.

The word *cross-sector* in the rectangle theorem refers to the ambient
macroprofile sectors occupied by the six coordinates.  It does not change
this packet-colour statement: the union of those coordinates is still the
one support \(B_i\).  A physical edge always changes one packet.  What is
absent from the tensor library is a trade whose ownership component
correlates the *phase assignments* of edges from two different supports
\(B_i,B_j\).  Such a trade is exactly a new cross-packet primitive.

## 2. Zero block holonomy of every H-compatible rectangle carry

We isolate the structural input of the phase-dense carry.

Let \(\Omega\) be a common owner support with a phase map

\[
                         \vartheta:\Omega\longrightarrow\mathbb Z_{4t}.
                                                                    \tag{2.1}
\]

In the static tensor factor, an outgoing edge from phase \(j\) has packet
colour

\[
                         \gamma(j)=1+(j\bmod t).       \tag{2.2}
\]

The first and third passages use one local rectangle direction, and the
second and fourth passages use the other.  Thus (2.2) records only the
packet, not the fine direction inside it.

Call a successor switch **H-compatible** if it has the two properties used
by the exact carry construction:

1. it matches owners with the same phase; and
2. at phase \(j\), it replaces the old local matching by a rectangle-shore
   matching supported in \(B_{\gamma(j)}\).

The ternary predicate may depend arbitrarily on every state label.  No
independence or sparsity is assumed.

### Theorem 2.1 (zero block holonomy)

Every successor permutation obtained from the static tensor factor by an
arbitrary family of H-compatible switches satisfies

\[
 \vartheta(\Phi x)=\vartheta(x)+1\pmod {4t},          \tag{2.3}
\]

and the edge \(x\Phi x\) has colour

\[
                         \gamma(\vartheta(x)).        \tag{2.4}
\]

Consequently every orbit, in every ternary state, has the same packet word
(0.1).  The induced monodromy on \([t]\) is the identity.

#### Proof

The common phase colouring is precisely the legality condition for an
H-compatible switch.  Both old and new outgoing matches at a phase-\(j\)
owner end at phase \(j+1\), which proves (2.3).  By definition, both matches
are supported in \(B_{\gamma(j)}\), proving (2.4).

These statements are pointwise.  Performing any number of switches, with
the choice at one port depending on all binary, syndrome, and ternary
labels, cannot change either statement.  Iterating (2.3)--(2.4) gives
(0.1) on every orbit.  After one macroperiod a ternary carry may change the
fine state, but the next macroperiod again starts with packet \(1\) and has
the same word.  Hence the induced permutation of packet labels is the
identity. \(\square\)

### Corollary 2.2 (no phase-dependent touched-set orders)

For every \(q\le t\), the packet colours in a \(q\)-edge window are \(q\)
distinct cyclically consecutive elements of \([t]\).  The collection of
such colour sets is independent of the ternary state.

#### Proof

Every length-\(t\) segment of (0.1) contains each packet colour once.  A
shorter segment is a cyclic interval in that order.  Theorem 2.1 makes the
word state-independent. \(\square\)

This is stronger than saying that one displayed Hamming factor has a common
order.  It says that all state-dependent factors generated by the exact
carry switches have the same quotient order, even when their fine physical
edges and their long connected components differ.

## 3. A general first-eligible-word Hall lemma

Partition the physical coordinates into an ordered list of bounded packets,
apart from a bounded remainder.  Let \(\mathcal E\) be a local middle-owner
alphabet, and let

\[
 \mathcal C^-={X\cap Y:X,Y\in\mathcal E, |X\triangle Y|=2\},
\qquad
 \mathcal C^+=\{X\cup Y:X,Y\in\mathcal E, |X\triangle Y|=2\}.    \tag{3.1}
\]

Alphabets of different local ranks are disjoint.  Call a middle owner
eligible in a packet when its restriction belongs to \(\mathcal E\), and
form its canonical macrocell from the first \(t\) eligible packets.

Suppose a successor factor has the following two properties:

1. every transition changes one selected packet along an edge internal to
   \(\mathcal E\); and
2. every \(q\le t\) window touches a cyclic interval of \(q\) selected
   packet indices.

For a signed target, erase all local packet types except

\[
 E:\ S\vert_B\in\mathcal E,
 \qquad
 C:\ S\vert_B\in\mathcal C^\pm.                    \tag{3.2}
\]

### Lemma 3.1 (two-run support condition)

Every signed depth-\(q\) target emitted from a good canonical macrocell has,
in its suppressed \(E/C\) word, either one \(C\)-run of length at least
\(q\), or two \(C\)-runs whose total length is at least \(q\).

#### Proof

Let \(i_1<\cdots<i_t\) be the first eligible list of the starting owner.
Touched selected packets become \(C\)-packets in the target; untouched
selected packets remain \(E\)-packets.

For a nonwrapping cyclic interval, no target \(E\)-packet can lie between
two successive touched selected packets.  It is unchanged in the starting
owner and hence would have appeared in its eligible list between them.
After neutral packets are erased, the \(q\) touched packets therefore lie
in one \(C\)-run.

If the interval wraps across the end of the selected list, split it into
its terminal and initial pieces.  The same argument puts each piece in one
\(C\)-run, and their lengths sum to \(q\). \(\square\)

Let a product Bernoulli law make the packet letters independent, and put

\[
 p_E=\Pr(E),\qquad p_C=\Pr(C),\qquad
                         \rho={p_C\over p_E+p_C}.     \tag{3.3}
\]

If there are \(n=O(m)\) complete packets, Lemma 3.1 and a union bound give

\[
 \Pr(\hbox{the support condition})
 \le n^2(q+1)\rho^q.                                 \tag{3.4}
\]

Indeed, choose the starts of the one or two disjoint runs and a split
\(q=a+(q-a)\).  The next prescribed \(q\) nonneutral letters must all be
\(C\), an event of probability \(\rho^q\).  Cases with one empty part
include the one-run event.

Choose the coordinate density so that the total-set-size conditioning event
has mean exactly \(m\pm q\).  For \(q=o(m)\), its probability is at least
\(c/\sqrt m\), with an absolute \(c>0\).  Conditioning (3.4) on that event
therefore proves the slice bound

\[
 {R_q^\pm\over\binom{2m}{m-q}}
 \le C m^{5/2}(q+1)\rho^q.                          \tag{3.5}
\]

No independence after slice conditioning is used.

The good-owner estimate has the required scale.  Under the
Bernoulli-\(1/2\) law, eligibility indicators of disjoint complete packets
are independent with fixed positive means: \(1/8\) for the six-coordinate
rectangle and \(3/32\) for the eight-coordinate H support.  If \(t=o(m)\),
a Chernoff bound makes the probability of fewer than \(t\) eligible packets
\(e^{-\Omega(m)}\).  Conditioning on middle rank costs only a factor
\(O(\sqrt m)\).  Hence in either atlas the bad middle owners have
cardinality

\[
                         u=e^{-\Omega(m)}W.            \tag{3.5a}
\]

The complement of the support event is an explicit Hall witness.  Give
weight one to every target outside that event and zero to every other
target.  Every good component has zero incidence with this weight.  If
\(u\) bad owners are allowed to emit arbitrary targets, the target-side
deficiency is at least

\[
                         N_q-R_q^\pm-u.               \tag{3.6}
\]

Thus (3.6) applies to integral component choices, fractional mixtures, and
arbitrary correlations among the carry states.

We will use the exact layer ratio

\[
 {N_q\over W}
 =\prod_{j=0}^{q-1}{m-j\over m+j+1}.                 \tag{3.7}
\]

For \(q=o(m^{2/3})\), Taylor expansion term by term gives

\[
 \log {N_q\over W}
 =-{q^2\over m}
   +O\!\left({q\over m}+{q^3\over m^2}\right).       \tag{3.8}
\]

Indeed, the linear part is
\(-m^{-1}\sum_{j=0}^{q-1}(2j+1)=-q^2/m\), and the sum
of all quadratic and higher remainders has the displayed size.  Thus
\(N_q/W=e^{-A^2+o(1)}\) at \(q=A\sqrt m+O(1)\), and
\(N_q/W=1-o(1)\) at \(q=O(\log m)\).

## 4. Exact constants for the six-coordinate rectangle atlas

Use \(\mathcal E=\mathcal R\) from (1.1).  Its members have local rank two
and

\[
                         |\mathcal E|=8.              \tag{4.1}
\]

Two adjacent members either keep the \(P\)-coordinate and exchange the
\(A\)-coordinate, or keep the \(A\)-coordinate and exchange the
\(P\)-coordinate.  Therefore

\[
 \mathcal C^-=\{\{x\}:x\in P\dot\cup A\},
 \qquad |\mathcal C^-|=6,                            \tag{4.2}
\]

while

\[
 \begin{aligned}
 \mathcal C^+
 ={}&\{\{p,x,y\}:p\in P,\ \{x,y\}\in\tbinom A2\}\;\dot\cup\\
    &\{P\cup\{x\}:x\in A\},
 \end{aligned}
 \qquad |\mathcal C^+|=12+4=16.                     \tag{4.3}
\]

These are maximal alphabets over all three rectangle shores, so allowing a
state-dependent choice among the shores cannot enlarge them.

For a lower target use coordinate density

\[
                         p_-={m-q\over2m}.
\]

Then

\[
 p_E=8p_-^2(1-p_-)^4,qquad
 p_C=6p_-(1-p_-)^5,                                  \tag{4.4}
\]

and hence

\[
 \rho_q^-={6(1-p_-)\over8p_-+6(1-p_-)}
          ={3(m+q)\over7m-q}.                        \tag{4.5}
\]

For an upper target use \(p_+=(m+q)/(2m)\).  Equations (4.1), (4.3) give

\[
 p_E=8p_+^2(1-p_+)^4,qquad
 p_C=16p_+^3(1-p_+)^3,                               \tag{4.6}
\]

and therefore

\[
 \rho_q^+={16p_+\over8(1-p_+)+16p_+}
          ={2(m+q)\over3m+q}.                        \tag{4.7}
\]

Substitution of (4.5), (4.7) in (3.5) proves (0.2)--(0.3).

At \(q=A\sqrt m+O(1)\),

\[
 \rho_q^-={3\over7}+O_A(m^{-1/2}),\qquad
 \rho_q^+={2\over3}+O_A(m^{-1/2}),                  \tag{4.8}
\]

so even the larger upper reached fraction is

\[
 \exp\{-A\log(3/2)\sqrt m+O_A(\log m)\}=o(1).       \tag{4.9}
\]

At \(q=\lceil20\log m\rceil\), both (0.2) and (0.3) are \(o(1)\),
while (3.8) gives \(N_q/W=1-o(1)\).  Thus the bare rectangle atlas also
has \(W-o(W)\) holes in each sign at one depth in the protected band.

This calculation already permits all local carrier nonuniqueness supplied
by the rectangle kernel.

## 5. Exact constants for the 24-state ternary-carry support

In the physical eight-coordinate support of the audited carry, put

\[
 \mathcal V=
 \left\{X\cup Y:
 X\in\binom{\{a,b,c,d\}}2,
 Y\in\{uw,ux,vw,vx\}\right\}.                       \tag{5.1}
\]

Thus \(|\mathcal V|=24\), at local rank four.  The union over all physical
one-swap frames has exact lower and upper boundary sizes

\[
                         |\mathcal C^-|=|\mathcal C^+|=40.        \tag{5.2}
\]

For completeness, a lower boundary member has either one special
coordinate and one complete reservoir orientation, giving
\(4\cdot4=16\) choices, or a special two-set and one reservoir coordinate,
giving \(6\cdot4=24\) choices.  Complementation gives the upper count.

At lower density \(p_-=(m-q)/(2m)\),

\[
 p_E=24p_-^4(1-p_-)^4,qquad
 p_C=40p_-^3(1-p_-)^5.                               \tag{5.3}
\]

At upper density \(p_+=(m+q)/(2m)\), the powers are respectively
\((4,4)\) and \((5,3)\).  Both signs give the same suppressed density

\[
                         \rho_{q,H}
 ={5(m+q)\over8m+2q}.                                \tag{5.4}
\]

Equation (3.5) now proves (0.4).  This maximal boundary already includes
every legal within-block rectangle frame.  Hence inserting the
cross-sector carrier kernel at H's local ports cannot enlarge the quotient
support used in the Hall cut.

At \(q=A\sqrt m+O(1)\),

\[
 \rho_{q,H}={5\over8}+O_A(m^{-1/2}),                 \tag{5.5}
\]

so the reached fraction is

\[
 \exp\{-A\log(8/5)\sqrt m+O_A(\log m)\}=o(1).       \tag{5.6}
\]

If \(q=\lceil20\log m\rceil\), then eventually
\(\rho_{q,H}<2/3\), while \(N_q/W=1-o(1)\).  Equations (3.5)--(3.6)
give \(W-o(W)\) holes for each sign.

## 6. Multiple phase states do not count as transverse order atlases

Theorem 2.1 says that all \(3^t\) ternary states lie over the same packet
word.  They are therefore one atlas for the Hall witness, not \(3^t\)
transverse atlases.

If one supplies \(L\) genuinely different coordinate blockings or packet
orders, a union bound multiplies (0.4) by at most \(L\).  Thus positive
density coverage at \(q=A\sqrt m+O(1)\) requires

\[
                         L\ge
 \exp\{(A\log(8/5)-o_A(1))\sqrt m\}                  \tag{6.1}
\]

for the 24-state H support.  For the bare rectangle atlas, simultaneous
lower coverage requires the stronger necessary count

\[
                         L\ge
 \exp\{(A\log(7/3)-o_A(1))\sqrt m\}.                 \tag{6.2}
\]

These are only necessary support counts.  Even that many atlases would
still need an exact owner cover satisfying their target Hall inequalities.

## 7. The exact surviving constructive lemma

Define the **block-order projection** of a phase-compatible factor to be
the packet colour of each common phase.  Every generator in the tensor
rectangle plus ternary-carry library has identity block monodromy by
Theorem 2.1.

The first operation not ruled out here is the following.

> **Ported adjacent-block transposition lemma (open).**  On a common owner
> support meeting two rectangle packets \(B_i,B_{i+1}\), construct two
> exact phase-compatible cycle factors such that at two common phases their
> packet-colour words are respectively
> \(\cdots,i,i+1,\cdots\) and
> \(\cdots,i+1,i,\cdots\), while all collars needed for cyclic
> \(H\)-geodesicity agree.

Such a factor cannot be a disjoint tensor of one-packet rectangle trades:
packet colour is preserved separately by every tensor generator.  A
nontrivial block transposition requires an overlap component containing
edges from both packets.

Once this primitive exists, its block-order projection can generate
state-dependent permutations, and the run Hall witness above need no longer
apply.  Without it, denser ternary phases only move vertically inside the
same forbidden quotient column.  Thus the H branch is rigorously exhausted
at the precise point where cross-block order holonomy, rather than local
carrier multiplicity, is required.

## 8. Scope audit

1. The proof does not use the old fixed-common-order carrier count.  It
   allows arbitrary state-dependent local shores and derives a physical
   target-side Hall witness from a quotient semiconjugacy.
2. Cross-sector macroprofile recoupling inside one rectangle is fully
   allowed.  Only crossing two disjoint tensor-packet supports would leave
   the theorem's scope.
3. The local alphabets in Sections 4 and 5 are unions over every possible
   physical one-swap frame, so no omitted rectangle shore can evade the
   probability calculation.
4. Slice conditioning is exact: independence is used only before
   conditioning, and the conditioning event has probability
   \(\Omega(m^{-1/2})\).
5. The bad-owner leave is charged one possible new target per owner; it is
   never treated as if it obeyed the run condition.
6. No coefficient-one conclusion is claimed.  The theorem closes only the
   exact phase-dense H composition with disjoint tensor rectangles and
   identifies the first generator needed to escape it.
