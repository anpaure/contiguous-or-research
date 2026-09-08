## I.1A Phase-packet banks and the ordered-lift gate

This section is independent of the coherent-tour coset construction below.
Keep the notation of I.1, assume \(b\ge5\) is odd, and put \(m=b-1\).

A labelled phase packet consists of distinct \(u,v\in\Omega\) and ordered
disjoint \(m\)-tuples

\[
 X=(x_1,\ldots,x_m),\qquad Y=(y_1,\ldots,y_m)
\]

whose entries partition \(\Omega-\{u,v\}\).  In the cyclic singleton word

\[
 z=(u,x_1,\ldots,x_m,y_1,\ldots,y_m)                 \tag{I.Q.1}
\]

on \(\Omega-\{v\}\), its distinguished middle targets are the \(b+1\)
length-\(b\) arcs

\[
 C_0=\{u\}\cup X,\qquad
 C_i=\{x_i,\ldots,x_m\}\cup\{y_1,\ldots,y_i\} (1\le i\le m),
 \qquad C_b=\{u\}\cup Y.                              \tag{I.Q.2}
\]

They are distinct.  Indeed they are proper arcs of one odd cycle with
distinct labels; equality of two arcs would give equal boundary edges and
hence either equal starts or complementary arcs; the latter have different
sizes \(b\) and \(b-1\).  Every cyclic arc of length at most \(2b-2\) is clean,
so one packet is locally clean through the full band because
\(b+H\le2b-2\).  Linearizing every packet separately would, however, charge
\(\Theta(b)\) letters per packet, and joining boundary sets or even boundary
queues does not by itself control longer windows across the joins.  Both
ordered chaining and all-offset cross-join cleanliness remain in the gate
below.  There are

\[
                    (2b)(2b-1)(2b-2)!=(2b)!           \tag{I.Q.3}
\]

labelled packets.

### Theorem I.Q.1 (exact packet profile) [I]

Every middle target has labelled packet degree

\[
                         D_{\rm pkt}=(b+1)(b!)^2.       \tag{I.Q.4}
\]

If two middle targets are at Johnson distance \(d\), their labelled
codegree is

\[
 \lambda_d=
 \begin{cases}
 \displaystyle {2(b+1-d)(b!)^2\over\binom bd^2},&1\le d\le b-2,\\[6pt]
 \displaystyle {6(b!)^2\over b^2},&d=b-1,\\
 0,&d=b.
 \end{cases}                                           \tag{I.Q.5}
\]

Consequently

\[
                    \boxed{{\Delta_2\over D_{\rm pkt}}
                    ={2\over b(b+1)}.}                 \tag{I.Q.6}
\]

#### Proof

Fix a middle target \(C\) and its position \(i\in\{0,\ldots,b\}\).  At
an endpoint, choose \(u\in C\), order the other \(b-1\) members, choose
\(v\notin C\), and order the other \(b-1\) outside members.  This gives
\(b^2((b-1)!)^2=(b!)^2\) labels.  At an internal position, split and order
the \(i\) entered and \(b-i\) surviving members of \(C\), in
\(\binom bi i!(b-i)!=b!\) ways; the complementary labels fill their
\(b\) ordered roles in \(b!\) ways.  Summing over positions proves
(I.Q.4).

For two distinct positions at ordinary separation \(d\), their targets
have Johnson distance \(d\).  The only exception is the endpoint pair
\(0,b\), whose intersection is \(\{u\}\), so its distance is \(b-1\).
For a fixed ordered position pair and a fixed first target, its stabilizer
is transitive on the \(\binom bd^2\) targets at distance \(d\).  The
contribution to a fixed ordered target pair is therefore
\((b!)^2/\binom bd^2\).  There are \(2(b+1-d)\) ordered position pairs at
separation \(d\), while distance \(b-1\) receives four pairs at separation
\(b-1\) and two endpoint pairs.  This proves (I.Q.5).  Since
\(\binom bd\ge b\) for \(1\le d\le b-1\), the first line is maximized at
\(d=1\); the exceptional normalized value \(6/[b^2(b+1)]\) is no larger.
This proves (I.Q.6). \(\square\)

### Theorem I.Q.2 (integral hypercube bank and adjacent loads) [I]

Fix \(u,v\), and partition \(R=\Omega-\{u,v\}\) into ordered pairs

\[
 P_i=\{a_i^0,a_i^1\},\qquad1\le i\le m.
\]

For \(x\in\mathbb F_2^m\), let
\(V(x)=\{a_i^{x_i}:1\le i\le m\}\), and put
\(p_i=e_1+\cdots+e_i\), \(p_0=0\).  For every even-weight \(x\), take the
packet

\[
 X=(a_1^{x_1},\ldots,a_m^{x_m}),\qquad
 Y=(a_1^{1-x_1},\ldots,a_m^{1-x_m}).                  \tag{I.Q.7}
\]

Let \(\mathcal B(P)\) be the \((m+1)\)-sets in \(R\) which double one
pair and split all the others.  These \(2^{m-1}\) packets satisfy:

1. their internal middle targets \(C_1,\ldots,C_m\) partition
   \(\mathcal B(P)\), so \(|\mathcal B(P)|=m2^{m-1}\);
2. every transversal \(V(z)\) occurs exactly \(m/2\) times among the
   same-start rank-\(m=b-1\) targets;
3. every boundary \(\{u\}\cup V(z)\) with even \(z\) occurs twice; and
4. at rank \(m+2=b+1\), every internal target which doubles consecutive
   pairs \(P_i,P_{i+1}\) and splits the others occurs twice, while every
   final target containing \(u\), doubling \(P_m\), and splitting the
   others occurs once.

#### Proof

The internal target at step \(i\) is the union of the two transversals at
the ends of the direction-\(i\) cube edge

\[
                  \{x+p_{i-1},x+p_i\}.                  \tag{I.Q.8}
\]

For fixed \(i\), translation by \(p_{i-1}\) sends the even shore
bijectively to one endpoint of every direction-\(i\) edge.  Varying \(i\)
partitions \(\mathcal B(P)\), proving part 1.

The rank-\(m\) target at that start is \(V(x+p_{i-1})\).  A fixed
\(V(z)\) occurs precisely when \(x=z+p_{i-1}\) is even, equivalently
\(|z|\equiv i-1\pmod2\).  Exactly \(m/2\) indices have either parity,
proving part 2.  The packet boundaries are
\(\{u\}\cup V(x)\) and \(\{u\}\cup V(\bar x)\).  Since \(m\) is even,
both indices are even; each boundary is supplied by \(x=z\) and
\(x=\bar z\), proving part 3.

For \(i<m\), the upper target is

\[
 \{a_1^{1-x_1},\ldots,a_{i-1}^{1-x_{i-1}}\}
 \cup P_i\cup P_{i+1}
 \cup\{a_{i+2}^{x_{i+2}},\ldots,a_m^{x_m}\}.          \tag{I.Q.9}
\]

It fixes every bit except \(x_i,x_{i+1}\), of whose four completions
exactly two are even.  At \(i=m\), the upper target is
\(\{u\}\cup P_m\cup\{a_1^{1-x_1},\ldots,a_{m-1}^{1-x_{m-1}}\}\);
its split choices and parity determine \(x_m\) uniquely.  This proves
part 4. \(\square\)

The bank decomposition also recovers exact fractional loads.  A fixed
\(C\in\binom R{m+1}\) belongs to \(\mathcal B(P)\) for

\[
 \rho_m=\binom{m+1}2(m-1)!={(m+1)!\over2}              \tag{I.Q.10}
\]

pairings: choose its doubled pair and biject its other elements with
\(R-C\).  Weight \(1/\rho_m\) on every integral bank therefore gives
middle load one.  A fixed \(m\)-set is a transversal of \(m!\) pairings
and has multiplicity \(m/2\) in each, so its lower load is exactly

\[
                         {m!\,(m/2)\over(m+1)!/2}
                         ={m\over m+1}.                \tag{I.Q.11}
\]

### Set-level chaining and the fixed-order obstruction [I]

Pair all of \(\Omega\) as \(P_1,\ldots,P_b\).  For special pair \(P_j\),
take \(u=a_j^0,v=a_j^1\) and the bank on the other pairs.  The internal
targets of the \(b2^{b-2}\) packets partition the defect-one stratum

\[
                 |\mathcal S_1(P)|=b(b-1)2^{b-2}.       \tag{I.Q.12}
\]

Indeed a defect-one target has a unique empty pair; Theorem I.Q.2 then
places it exactly once in the corresponding special-pair bank.

Encode a boundary transversal by an even set \(S\subseteq[b]\).  For
\(j\notin S\), its packet boundary edge is

\[
                         T_j(S)=[b]-(S\cup\{j\}).       \tag{I.Q.13}
\]

The unordered pair \(\{|S|,b-1-|S|\}\) is invariant.  Conversely, if
\(j\notin S\) and \(k\in S\), then

\[
                         T_kT_j(S)=(S-\{k\})\cup\{j\}. \tag{I.Q.14}
\]

Thus two moves make every exchange: there is one connected component for
each unordered weight pair, hence only \(O(b)\) components.  Each edge is
supplied twice, so every component is Eulerian.  This is chaining of
boundary sets, not of ordered FIFO queues.

Quantitatively, fix one cyclic order \(\rho\) of the coordinate pairs and
form a coherent \(b\)-packet cycle from an initial state
\(x\in\mathbb F_2^b\): at each stage keep the special pair, flip every
other pair in the inherited FIFO order, and advance the special pair.  The
target with empty pair \(j\) and doubled pair \(i\) has split bits

\[
               (x+f_{\rho,j,i})|_{[b]-\{j,i\}},         \tag{I.Q.15}
\]

where \(f_{\rho,j,i}\) depends only on the order and positions.  The
formula follows because every prescribed FIFO step adds a fixed coordinate
flip to \(x\).  The empty/doubled signature recovers \((j,i)\).  Hence two
distinct cycles of the same order share an internal middle target exactly
when their initial states differ on at most two coordinates: equality is
equivalent to the difference being supported on some \(\{j,i\}\), and any
support of size at most two is contained in such a pair.  A disjoint family is
therefore a binary code of minimum distance at least three.  Its radius-one
Hamming balls are disjoint, so it has at most \(2^b/(b+1)\) states and
covers at most the following fraction.  Each cycle has one target for each
ordered \(j\ne i\), hence \(b(b-1)\) targets, whereas (I.Q.12) requires
\(2^{b-2}\) such cycles:

\[
                  {2^b/(b+1)\over2^{b-2}}={4\over b+1}=o(1) \tag{I.Q.16}
\]

of \(\mathcal S_1(P)\).  Even before cross-order collisions, a near-factor
therefore needs \(\Omega(b)\) cyclic orders.  The unordered Euler statement
does not remove this ordered-queue obstruction.

### Gate \(C_{\rm Q}\) [O]

Across pairings and within-packet orders, select and, on only \(o(W)\)
core starts, switch or delete phase packets so that their ordered boundaries
form physical \(H\)-fragments with

\[
 M=W-o(W),\qquad gt=o(W),\qquad
 \sum_{s=b-H}^{b+H}
 \left[\binom{2b}s-|\mathcal I_s|\right]=o(W),          \tag{I.Q.17}
\]

and with globally distinct retained middle cores.  Equivalently, the
ordered lift must use \(o(W/b)\) fragment trails and give literal coverage
through every offset \(1\le q\le H\), not only the adjacent loads proved
above.  This gate is not implied by Gate \(C_{\rm F}\) in Section I.6: the
two constructions have different integral blocks and different selector
obstructions.  If (I.Q.17) holds, it is exactly the antecedent (I.6), so
Theorem I.1 proves \(\nu(2b)=(1+o(1))W\), and the bounded top-bit splices
give the full coefficient-one asymptotic. \([\mathrm C]\)
