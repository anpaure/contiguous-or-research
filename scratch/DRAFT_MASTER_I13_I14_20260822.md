### I.13 The all-pairing coherent-tour orbit

Retain odd \(b\ge5\), let \(|\Omega|=2b\), and put
\(\mathcal V={\Omega\choose b}\), \(W=|\mathcal V|\). Pair the symbols as
\(P_j=\{a_j^0,a_j^1\}\), \(j\in\mathbb Z_b\), in a directed cyclic order.
Initially select \(a_j^0\) from every pair. At stage \(t\), keep the selected
member of the special pair \(P_t\), flip the selected member of every other
pair in cyclic FIFO order, and rotate the pair queue once. Every coordinate
is flipped \(b-1\) times, so the \(b\) packets form a closed tour.

For \(t\ne i\), the internal middle window with empty pair \(P_t\) and
doubled pair \(P_i\) is

\[
 T_{t,i}=P_i\cup
 \{a_h^{\chi_{t,i}(h)}:h\notin\{t,i\}\},\qquad
 \chi_{t,i}(h)=t+\mathbf1_{(h-i)(t-i)>0}\pmod2.             \tag{I.99}
\]

Here \(0,\ldots,b-1\) are integer representatives. Indeed, before stage
\(t\) the selected bit at \(h\) is
\(t+\mathbf1_{h<t}\pmod2\), and the coordinates strictly between \(t\) and
\(i\) in the directed order have then been flipped once more. Each target
has the recoverable signature “empty \(P_t\), doubled \(P_i\),” so

\[
 K=\{T_{t,i}:t\ne i\},\qquad |K|=q=b(b-1).                 \tag{I.100}
\]

A parameter label consists of a perfect pairing, a rooted directed cyclic
listing of its pairs, and an initial bit state, modulo the free \(b\) phase
shifts. Hence

\[
 |\mathcal E_{\rm lab}|=
 { (2b)!\over2^bb!}\,{b!2^b\over b}={(2b)!\over b}.         \tag{I.101}
\]

We retain labels temporarily, so parallel supports are allowed.

For \(0\le d\le b\), let
\(M_d=|\{(A,B)\in K^2:|A\setminus B|=d\}|\). Substitution in (I.99)
gives the following disjoint, exhaustive relation census for the two labels
\((t,i),(u,j)\):

\[
\begin{array}{c|c|c}
\text{relation}&d&\text{ordered pairs}\\ \hline
(t,i)=(u,j)&0&b(b-1)\\
t=u,\ i\ne j&1\le d\le b-2&2b(b-1-d)\\
i=j,\ t\ne u&1&b(b-1)(b-3)/2\\
i=j,\ t\ne u&b-2&b(b-1)^2/2\\
(u,j)=(i,t)&d\in\{2,4,\ldots,b-1\}&2b\\
\text{exactly one of }t=j,\ i=u&2\le d\le b-1&2b(b-1)\\
|\{t,i,u,j\}|=4&2\le d\le b-2&
b\{b^2-4b+3+4\lfloor d/2\rfloor\}.
\end{array}                                                \tag{I.102}
\]

Here is a direct audit. With a common empty coordinate, the doubled
coordinates at positions \(r,s\in[1,b-1]\) have distance \(|r-s|\), giving
the second row. With a common doubled coordinate, the two parity cases in
(I.99) give only \(1,b-2\), with the displayed totals. Reversing the two
roles gives every positive even distance; one crossed role gives every
distance \(2,\ldots,b-1\), with respectively \(2\) and \(2(b-1)\) choices
per fixed first empty coordinate. In the four-distinct case fix \(t=0\),
write the other positions \(1\le x<y<z\le b-1\), and order their roles as
\(IUJ,IJU,UIJ,UJI,JIU,JUI\), where \(I,U,J\) are first-double,
second-empty, second-double. Formula (I.99) gives respectively

\[
 z-x,\ b+x-y-1,\ 1-y+z,\ 1-y+z,\ b+x-y-1,\ b+x-z
\]

when the \(U\)-position is even, and their complements to \(b\) when it is
odd. Solving each linear difference for \(d\), then pairing the first with
last, second with fifth, and third with fourth, cancels the endpoint floors
and gives \(b^2-4b+3+4\lfloor d/2\rfloor\) for fixed \(t\). Restoring \(b\)
choices of \(t\) proves the last row. The five nonidentity relation totals
are \(q(b-2),q(b-2),q,2q(b-2),q(b-2)(b-3)\), whose sum is \(q(q-1)\).

Summing (I.102) by distance gives

\[
\boxed{\begin{aligned}
 M_0&=b(b-1),&M_1&={b(b^2-5)\over2},\\
 M_d&=b(b^2+1)&& (2\le d\le b-3,\ d\ {\rm even}),\\
 M_d&=b(b^2-3)&& (3\le d\le b-4,\ d\ {\rm odd}),\\
 M_{b-2}&={b(b+1)(3b-5)\over2},&M_{b-1}&=2b^2,\quad M_b=0.
\end{aligned}}                                             \tag{I.103}
\]

Empty ranges are omitted. The formulas sum to \(q^2\).

The symmetric group is transitive on middle vertices and on ordered middle
pairs at each Johnson distance. Incidence counting therefore gives

\[
 D_{\rm lab}={|\mathcal E_{\rm lab}|q\over W}=(b-1)(b!)^2,
 \qquad {\lambda_d^{\rm lab}\over D_{\rm lab}}
 ={M_d\over b(b-1){b\choose d}^2}.                         \tag{I.104}
\]

For \(2\le d\le b-2\), use
\(M_d\le M_{b-2}\) and \({b\choose d}\ge {b\choose2}\); the resulting
upper bound
\[
 {2(b+1)(3b-5)\over b^2(b-1)^3}
\]
is smaller than the \(d=1\) value because their cross-multiplied difference
is \(b^4-2b^3-16b^2+18b+15>0\) for \(b\ge5\) (it is positive at \(5\),
and its derivative is then increasing and positive). The \(d=b-1\) value is
\(2/[b(b-1)]\), tying only when \(b=5\). Hence

\[
 \boxed{{\Delta_2\over D_{\rm lab}}=
 {b^2-5\over2b^2(b-1)}={1\over2b}+O(b^{-2}).}               \tag{I.105}
\]

Reversal of the cyclic FIFO word preserves its support, so labels are not
simple. All supports form one \(S_{2b}\)-orbit. If their common label
multiplicity is \(\mu_b\), collapsing parallels divides every degree and
codegree by \(\mu_b\), leaving (I.104)--(I.105) unchanged:

\[
 D_{\rm simp}={(b-1)(b!)^2\over\mu_b},\qquad
 \lambda_{d,\rm simp}={\lambda_d^{\rm lab}\over\mu_b}.     \tag{I.106}
\]

We use only \(\mu_b\ge2\); no assertion \(\mu_b=2\) is needed.

Write one packet's consecutive middle windows as
\(C_0,\ldots,C_b\). At each internal window define the literal adjacent
tokens

\[
 L_i=C_{i-1}\cap C_i,\qquad U_i=C_i\cup C_{i+1}\quad(1\le i<b). \tag{I.107}
\]

Within a tour the \(q\) lower tokens are distinct: their empty pair fixes
the packet, and inside it they are the vertices of an antipodal cube path.
The upper tokens are distinct: an internal one is identified by its empty
pair and two consecutive doubled pairs, while the packet-end type has no
empty pair and one doubled pair. Orbit incidence counting gives

\[
 D_-=D_+={|\mathcal E_{\rm lab}|q\over{2b\choose b-1}}
 =(b-1)(b-1)!(b+1)!,\qquad
 {D_-\over D_{\rm lab}}={D_+\over D_{\rm lab}}={b+1\over b}. \tag{I.108}
\]

Thus \(1/D_{\rm lab}\) is an exact fractional middle factor with adjacent
load \((b+1)/b\); weight \(1/D_-\) factors both adjacent ranks and has middle
load \(b/(b+1)\). This is not an integral augmented matching.

There is no density-only recursion. For fixed \(a\in\Omega\), neither
\(\{C:a\in C\}\) nor its complement contains a tour: at \(a\)'s special
packet every internal target omits its pair, while at another special packet
one internal target doubles that pair.

Adding the \(b\) packet-boundary transversals gives \(b^2\) distinct closed-
cycle windows. Boundary and internal windows are disjoint by their pair
signatures, and different boundary states differ by parity between their
stages. More explicitly, relative to boundary stage zero, boundary stage
\(u\) has distance \(u\) for even \(u\), and \(b-u\) for odd \(u\).
Thus boundary--boundary pairs number \(2b\) at every positive even distance.
For a fixed boundary at stage zero, (I.99) gives the following distance to
\(T_{t,i}\):
\[
\begin{array}{c|cc}
&t<i&t>i\\ \hline
t\ {\rm even}&i&b-i-1\\
t\ {\rm odd}&b-i&i+1.
\end{array}
\]
Counting the allowed \(t\ne i\) in these four cells gives \(b+1\) internal
targets at each odd distance and \(b-1\) at each positive even distance.
After the \(b\) boundary choices, the boundary--internal counts in either
ordered direction are therefore \(b(b+1)\) and \(b(b-1)\), respectively.
Adding these counts to (I.103) gives

\[
\boxed{\begin{aligned}
 M_0^+&=b^2,&M_1^+&={b(b^2+4b-1)\over2},\\
 M_d^+&=b(b+1)^2&&(2\le d\le b-3,\ d\ {\rm even}),\\
 M_d^+&=b(b^2+2b-1)&&(3\le d\le b-4,\ d\ {\rm odd}),\\
 M_{b-2}^+&={b(b+1)(3b-1)\over2},&M_{b-1}^+&=4b^2,\quad M_b^+=0.
\end{aligned}}                                             \tag{I.109}
\]

Its degree is \(b(b!)^2\), and the same comparison as above gives

\[
 \boxed{{\Delta_2^+\over D^+}={b^2+4b-1\over2b^3}
 ={1\over2b}+O(b^{-2}).}                                  \tag{I.110}
\]

Indeed, for \(2\le d\le b-2\), use
\(M_d^+\le M_{b-2}^+\) and
\({b\choose d}\ge {b\choose2}\). The resulting normalized value is at most
\(2(b+1)(3b-1)/[b^3(b-1)^2]\), smaller than (I.110) because
\(b^4+2b^3-20b^2-2b+3>0\) for \(b\ge5\). At \(d=b-1\) the value
is \(4/b^2\), also smaller since \(b^2-4b-1>0\).

Consequently a matching covering \((1-o(1))W\) middle vertices would use at
most \(W/[b(b-1)]\) closed tours. Linearizing them and concatenating costs
at most \(O(b+H)\) unusable starts per join, hence

\[
 O\!\left({(b+H)W\over b(b-1)}\right)=o(W)\qquad(H=o(b)).  \tag{I.111}
\]

It would close middle coverage and FIFO seam cost, but not collisions among
adjacent tokens from different tours or literal coverage at offsets
\(2,\ldots,H\). Also, \(q=b(b-1)\to\infty\); Appendix C.6 proves that
regularity plus (I.105) alone cannot imply the required matching.

### I.14 The ordered Greene--Kleitman factor contains no coherent tour

For a three-rank flag \(L\subset C\subset U\), with sizes \(b-1,b,b+1\),
define its directed symbol arc

\[
 p=C\setminus L\longrightarrow q=U\setminus C.             \tag{I.112}
\]

For literal consecutive windows this is the previous entrant followed by
the next entrant. In the normalized coherent tour above, let \(Q_s\) be the
selected boundary queue beginning with special pair \(P_s\). Before stage
\(s\), the selected bit at pair \(j\) is

\[
 \eta_s(j)=s+\mathbf1_{j<s}\pmod2,\qquad
 Q_s=(a_s^{\eta_s(s)},a_{s+1}^{\eta_s(s+1)},\ldots,
      a_{s+b-1}^{\eta_s(s+b-1)}).                          \tag{I.113}
\]

Pair subscripts are modulo \(b\). The \(b-1\) internal flags of a packet are
precisely the consecutive arcs of its ending queue; over all stages these
ending queues are \(Q_0,\ldots,Q_{b-1}\) in cyclically shifted order. For
\(0\le j<b-1\), the
pair-coordinate adjacency \(j\to j+1\) occurs in every \(Q_s\) except
\(Q_{j+1}\); in the retained occurrences its bits agree,
\(h=(b-1)/2\) times in each bit. The wrap \((b-1)\to0\) occurs except in
\(Q_0\), with each opposite-bit orientation \(h\) times. Thus every
coherent tour projects exactly to \(h\) copies of

\[
 \boxed{a_0^0\to a_1^0\to\cdots\to a_{b-1}^0\to
 a_0^1\to a_1^1\to\cdots\to a_{b-1}^1\to a_0^0.}          \tag{I.114}
\]

Hence, for any disjoint flag family \(\mathscr F\), a retained subfamily
partitioned into \(T\) whole tours has indegree and outdegree \(hT\) at every
symbol. If \(R=b(b-1)T\) flags are retained, every nontrivial directed cut
has at least \(R/(2b)\) arcs in each direction, counted with multiplicity,
and

\[
 |\mathscr F|-R\ge {1\over2}\sum_{v\in\Omega}|d^+(v)-d^-(v)|, \tag{I.115}
\]

where \(d^\pm\) are the original arc degrees of \(\mathscr F\), because
deleting one arc changes total absolute imbalance by at most two.
These are necessary, not sufficient: middle-set and packet incidences must
also agree.

Now fix any total order on \(\Omega\) and form its ordered Greene--Kleitman
SCD. Scan the membership word left to right and pair each zero with the
latest unpaired one to its left. Once pairs are fixed, the unpaired
coordinates are zeros followed by ones. At a central flag
\(L\subset C\subset U\), the edge \(L\to C\) flips the leftmost unpaired
one of \(C\), whereas \(C\to U\) flips its rightmost unpaired zero.
Therefore

\[
                         q(L,C,U)<p(L,C,U),                 \tag{I.116}
\]

so every GK flag arc points strictly backward and their arc multigraph is a
DAG. Exactly

\[
 N={2b\choose b-1}={b\over b+1}{2b\choose b}               \tag{I.117}
\]

chains cross all three ranks: every rank-\((b-1)\) set lies on one symmetric
chain; its bottom is at most \(b-1\), so symmetry puts its top at least
\(b+1\). These flags are disjoint in all three ranks. Equations (I.114) and
(I.116) prove that not one coherent tour is contained in any ordered or
relabelled GK factor.

If exceptional replacement flags are allowed, every Hamilton cycle in
(I.114) has a nondecreasing arc, appearing \(h\) times. Therefore \(T\)
disjoint tours require at least \(hT\) exceptional flags, or

\[
 \boxed{\#\{\text{exceptional flags}\}\ge {R\over2b}.}     \tag{I.118}
\]

This is only \(o(R)\), so it does not rule out a non-GK SCD, a different
three-rank flag factor, or a vanishing-fraction trade. It proves precisely
that Appendix D's ordered GK flag column cannot be grouped wholesale into
physical coherent tours; its abstract retirement theorem remains valid.

The non-GK caveat is genuine: on \(\{0,1,2,3\}\), the chains
\[
 \varnothing\subset0\subset03\subset023\subset0123,\quad
 1\subset01\subset013,\quad2\subset12\subset012,\quad
 3\subset23\subset123,\quad02,\quad13
\]
partition the Boolean lattice into symmetric chains, and their four middle
flags have arcs \(3\to2,0\to3,1\to0,2\to1\), a Hamilton cycle. This
even-\(b=2\) example is only a scope witness, not an odd-\(b\) construction.
