# Gate C: an explicit Catalan phase-packet subfactor

**Status (updated 2026-08-23).**  Every theorem below is proved.  The first
two Catalan banks construct a matching in the full phase-packet hypergraph
of size

\[
             C_{b-1}+C_{b-2}-1,
\]

where \(C_j=(j+1)^{-1}{2j\choose j}\).  Since a perfect packet factor
would have \(C_b\) edges, the construction covers

\[
 {C_{b-1}+C_{b-2}-1\over C_b}
 = {5\over16}+O(b^{-1})
\]

of the middle layer.  Section 8 adds two shifted primitive banks and
strengthens this to

\[
             C_{b-1}+3C_{b-2}-2
             =\left({7\over16}+O(b^{-1})\right)C_b.
\]

This is an explicit positive-density integral subfactor; it is not an
asymptotically perfect matching.  The construction also identifies why
simply stacking complete fixed-puncture Catalan banks cannot complete the
factor.

The only imported terminology is the definition of a phase packet; it is
restated in Section 1.  The minimum-change Chung--Feller lemma needed in the
proof is stated, constructed, and justified in Section 2.  Its underlying
map is the one introduced by M\"utze, Standke, and Wiechert, *European
Journal of Combinatorics* 69 (2018), 260--275.

## 1. Phase packets

Let \(b\ge3\), let \(|\Omega|=2b\), and put \(k=b-1\).  A labelled phase
packet is determined by distinct \(r,v\in\Omega\) and ordered disjoint
\(k\)-tuples

\[
 X=(x_1,\ldots,x_k),\qquad Y=(y_1,\ldots,y_k)
\]

which partition \(\Omega\setminus\{r,v\}\).  Its \(b+1=k+2\) middle
vertices, in their physical order, are

\[
 \{r\}\cup X,\quad
 \{x_i,\ldots,x_k\}\cup\{y_1,\ldots,y_i\} (1\le i\le k),\quad
 \{r\}\cup Y.                                      \tag{1.1}
\]

Thus the first move removes \(r\), the last move restores \(r\), and the
coordinate \(v\) never occurs.

## 2. The minimum-change Chung--Feller path factor

Identify a subset of \([2k]\) with its zero--one word, with a one an up-step
and a zero a down-step.  A down-step is *below height zero* when its endpoint
has negative height, equivalently when its starting height is at most zero.
Let \(D^e_{2k}\) be the balanced words having exactly \(e\) such down-steps.
Thus \(D^0_{2k}\) is the set of Dyck words and \(D^k_{2k}\) its set of
complements.

For a lattice word \(w\), let \(d_c(w)\), respectively \(u_c(w)\), be the
number of down-steps, respectively up-steps, starting at height \(c\).  A
step *touches* height \(c\) when one of its endpoints has that height.
For a balanced word \(x\notin D^k_{2k}\), define \(g(x)\) by changing to an
up-step the \((d_0(x)+1)\)-st down-step, from left to right, which touches
height zero.  The word \(g(x)\) has \(k+1\) ones.  For any word \(y\) with
\(k+1\) ones, define \(h(y)\) by changing to a down-step the \(u_1(y)\)-th
up-step which touches height one.  Put

\[
                         f=h\circ g.                  \tag{2.1}
\]

For \(x\in D^0_{2k}\), set

\[
 S_i(x)=\operatorname{supp}(f^i(x))\quad(0\le i\le k),
 \qquad
 T_i(x)=\operatorname{supp}(g(f^i(x)))\quad(0\le i<k). \tag{2.2}
\]

Write \(a_i\) for the coordinate added by \(g\) at step \(i\), and
\(d_i\) for the coordinate removed by \(h\).  Then

\[
 S_{i+1}=S_i-\{d_i\}+\{a_i\},qquad
 T_i=S_i\cup\{a_i\}=S_{i+1}\cup\{d_i\}.              \tag{2.3}
\]

### Lemma 2.1 (minimum-change path factor)

The paths

\[
 S_0(x),T_0(x),S_1(x),\ldots,T_{k-1}(x),S_k(x),
 \qquad x\in D^0_{2k},                               \tag{2.4}
\]

have the following properties.

1. For each \(0\le e\le k\), \(f^e\) is a bijection from
   \(D^0_{2k}\) to \(D^e_{2k}\).
2. For every \(x\in D^0_{2k}\),
   \[
        S_k(x)=[2k]\setminus S_0(x),                  \tag{2.5}
   \]
   and \((a_0,d_0,a_1,d_1,\ldots,a_{k-1},d_{k-1})\)
   is a permutation of \([2k]\).  The \(a_i\)'s are the zeros of \(x\)
   and the \(d_i\)'s are its ones.
3. The sets \(T_i(x)\), over all \(x\in D^0_{2k}\) and \(0\le i<k\),
   partition \({[2k]\choose k+1}\).
4. If \(x=1u0\) is primitive, where \(u\in D^0_{2k-2}\), then
   \[
                         a_0=2k,qquad d_{k-1}=1.      \tag{2.6}
   \]

#### Proof

We include the elementary bookkeeping because all four conclusions are
used below.  Define \(h'(y)\) by changing the
\((u_1(y)+1)\)-st up-step of \(y\) touching height one to a down-step.
Every word with \(k+1\) up-steps has this step.  If \(y=g(x)\), a height
scan on the two sides of the changed step gives

\[
 \#\{\text{touching up-steps of }y\text{ weakly before the changed step}\}
 =u_1(y)+1.
\]

The same scan, read backwards, shows that the changed step in \(h'(y)\)
is the \((d_0(h'(y))+1)\)-st touching down-step.  Hence
\(h'g=\mathrm{id}\) and \(gh'=\mathrm{id}\):

\[
 g:L_{2k,k}\setminus D^k_{2k}\longleftrightarrow
   L_{2k,k+1}:h'
\]

is a bijection.  Similarly, define \(g'(z)\) by changing the
\(d_0(z)\)-th down-step touching height zero to an up-step.  The identical
scan with the index shifted by one gives

\[
 h:L_{2k,k+1}\longleftrightarrow
   L_{2k,k}\setminus D^0_{2k}:g'.
\]

In particular, both \(g\) and \(h\) are injective on the domains used by
\(f\).

Let the coordinates changed by \(f\) be \(a<j\), where \(j\) is changed
from down to up by \(g\), and \(a\) from up to down by \(h\).  There is no
up-step touching height one strictly between \(a\) and \(j\); this follows
from the two consecutive ranks in the preceding inverse scan.  Therefore
the middle segment is lowered by two without producing a second new flaw,
and the step at \(j\) produces exactly one new flaw.  Thus

\[
                         f(D^e_{2k})\subseteq D^{e+1}_{2k}. \tag{2.7}
\]

The injections in (2.7), together with complement symmetry
\(|D^0_{2k}|=|D^k_{2k}|\), force equality at every stage.  This proves
part 1 and also gives

\[
 |D^e_{2k}|={1\over k+1}{2k\choose k}=C_k.            \tag{2.8}
\]

For completeness, the standard recovery invariant is as follows.  In
\(w=f^e(x)\), mark every up-step below height zero, and mark every down-step
which is below height \(-1\) or is among the first \(d_0(w)\) down-steps
touching height zero.  The same inverse scan used above shows inductively
that the newly added coordinate is a new mark of the first kind, the newly
removed coordinate is a new mark of the second kind, and no old mark is
lost.  Moreover, these are exactly the coordinates on which \(w\) differs
from \(x\).  There are \(e\) marks of each kind.  At \(e=k\) every
coordinate is marked, proving (2.5) and part 2.

The pairs \((x,i)\) with \(x\in D^0_{2k}\) and \(0\le i<k\) map under
\((x,i)\mapsto f^i(x)\) bijectively onto all balanced words except
\(D^k_{2k}\).  The inverse scan says that \(g\) maps this set bijectively
onto all words with \(k+1\) ones.  This proves part 3.

Finally, the flip order has the following first-return recursion.  If
\(x=1u0v\), where the displayed zero is the first return to height zero,
then direct application of the two selectors gives

\[
 \pi(x)=\bigl(|u|+2, |u|+2-\pi(\overline{\operatorname{rev}}u),
                    1, |u|+2+\pi(v)\bigr),            \tag{2.9}
\]

where \(\pi=(a_0,d_0,\ldots,a_{k-1},d_{k-1})\), operations on a sequence
are entrywise, and empty terms are omitted.  This identity follows by
induction on the two Dyck subwords: the selectors first enter the closing
step of the first component, traverse its interior in reversed-complemented
order, remove its opening step, and then traverse \(v\).  When \(v\) is
empty, (2.9) begins with \(2k\) and ends with \(1\), which is (2.6).
\(\square\)

## 3. A complete punctured Catalan bank

Fix distinct \(p,q\in\Omega\), linearly order
\(R=\Omega\setminus\{p,q\}\), and identify \(R\) with \([2k]\).
For every \(x\in D^0_{2k}\), define

\[
 \mathcal P_x=
 \bigl(\{p\}\cup S_0(x),\ T_0(x),\ldots,T_{k-1}(x),\
       \{p\}\cup S_k(x)\bigr).                       \tag{3.1}
\]

### Proposition 3.1

The \(C_k=C_{b-1}\) sequences in (3.1) are pairwise vertex-disjoint
phase packets.

#### Proof

By Lemma 2.1(2), the removals \((d_0,\ldots,d_{k-1})\) order \(S_0\),
and the additions \((a_0,\ldots,a_{k-1})\) order its complement.  Equations
(2.3) show that (3.1) is precisely (1.1) with

\[
 r=p,\quad v=q,\quad X=(d_0,\ldots,d_{k-1}),\quad
 Y=(a_0,\ldots,a_{k-1}).                              \tag{3.2}
\]

Lemma 2.1(3) says that the internal vertices partition
\({R\choose k+1}\).  The two endpoints range respectively over
\(\{p\}\cup D^0_{2k}\) and \(\{p\}\cup D^k_{2k}\); these two families
are disjoint and each has no point in common with an internal vertex.
\(\square\)

This already covers the fraction

\[
 {C_{b-1}\over C_b}={b+1\over4b-2}={1\over4}+O(b^{-1}) \tag{3.3}
\]

of the middle layer.

## 4. A disjoint dual primitive bank

For \(x\in D^0_{2k}\), put

\[
                         Z_i(x)=R\setminus T_i(x).     \tag{4.1}
\]

Now restrict to primitive Dyck words

\[
                         x=1u0,qquad u\in D^0_{2k-2}, \tag{4.2}
\]

and omit the single word

\[
                         x_*=1(10)^{k-1}0.             \tag{4.3}
\]

For such an \(x\), define

\[
 U(x)=S_0(x)-\{1\}+\{2k\}=0u1                       \tag{4.4}
\]

and the sequence

\[
 \mathcal Q_x=
 \bigl(\{p\}\cup(R\setminus U(x)),
       \{p,q\}\cup Z_0(x),\ldots,\{p,q\}\cup Z_{k-1}(x),
       \{q\}\cup S_0(x)\bigr).                      \tag{4.5}
\]

### Proposition 4.1

The \(C_{k-1}-1=C_{b-2}-1\) sequences in (4.5) are pairwise
vertex-disjoint phase packets, and they are disjoint from every packet in
Proposition 3.1.

#### Proof

For primitive \(x\), Lemma 2.1(4) gives \(a_0=2k\) and
\(d_{k-1}=1\).  Complementing (2.3) gives

\[
 Z_{i+1}=Z_i-\{a_{i+1}\}+\{d_i\}\quad(0\le i<k-1),\qquad
 Z_0=\{a_1,\ldots,a_{k-1}\},\quad
 Z_{k-1}=\{d_0,\ldots,d_{k-2}\}.                     \tag{4.6}
\]

Thus (4.5) is (1.1) with

\[
 \begin{aligned}
 r&=d_{k-1}=1,& v&=a_0=2k,\\
 X&=(a_1,\ldots,a_{k-1},p),&
 Y&=(q,d_0,\ldots,d_{k-2}).
 \end{aligned}                                        \tag{4.7}
\]

In particular it is a genuine phase packet.

The internal vertices of distinct \(\mathcal Q_x\)'s are distinct because
the \(T_i(x)\)'s are globally distinct by Lemma 2.1(3).  Their final
vertices \(\{q\}\cup S_0(x)\) are distinct.  Their first vertices are
distinct because \(U(x)=0u1\) remembers \(u\).

It remains only to check cross-collisions.  An internal \(\mathcal P\)
vertex avoids \(p,q\), an endpoint \(\mathcal P\) vertex contains \(p\)
but not \(q\), an internal \(\mathcal Q\) vertex contains both, and the
final \(\mathcal Q\) vertex contains \(q\) but not \(p\).  The sole
possible collision is therefore between the first vertex of
\(\mathcal Q_x\) and a \(\mathcal P\) endpoint.

The word \(U(x)=0u1\) is never Dyck.  It is anti-Dyck exactly when the
Dyck word \(u\) never rises above height one, which forces
\(u=(10)^{k-1}\).  That is precisely the omitted word (4.3).  For every
retained \(x\), neither \(U(x)\) nor its complement belongs to
\(D^0_{2k}\cup D^k_{2k}\).  Proposition 3.1 shows that no collision is
possible.  Finally, there are \(C_{k-1}\) primitive words (4.2), and one
was omitted. \(\square\)

## 5. The explicit matching theorem

### Theorem 5.1 (Catalan phase-packet subfactor)

For every \(b\ge3\), the full phase-packet hypergraph on
\({\Omega\choose b}\) contains an explicit matching of size

\[
                         \boxed{C_{b-1}+C_{b-2}-1}.     \tag{5.1}
\]

It covers the fraction

\[
 \boxed{
 {C_{b-1}+C_{b-2}-1\over C_b}
 ={b+1\over2(2b-1)}
  +{b(b+1)\over4(2b-1)(2b-3)}-{1\over C_b}
 ={5\over16}+O(b^{-1}).}                              \tag{5.2}
\]

#### Proof

Take the union of the matchings in Propositions 3.1 and 4.1.  Their
disjointness and size give (5.1).  Every phase packet has \(b+1\) vertices
and

\[
                         {2b\choose b}=(b+1)C_b.       \tag{5.3}
\]

The two consecutive Catalan ratios give (5.2). \(\square\)

## 6. Exact scope and the remaining matching gate

This theorem does not prove an asymptotically perfect matching.  It does,
however, close two possible misunderstandings.

1. The phase-packet hypergraph has a large integral matching for an
   explicit structural reason; its known fractional matching is not the
   only positive evidence.
2. Distinct complete fixed-puncture Catalan banks cannot simply be stacked.
   The internal support of the bank for \(\{p,q\}\) is the whole slice
   \({\Omega\setminus\{p,q\}\choose b}\).  If \(b\ge4\), the internal
   supports for any two puncture pairs intersect, because one can choose a
   \(b\)-set outside their union of at most four points.  Thus any extension
   beyond (5.1) must switch or thin the Catalan paths; taking several full
   conjugate banks is impossible.

The exact open problem remains to construct a matching of
\((1-o(1))C_b\) phase packets, or to prove an obstruction to that
statement.  Even such a matching would solve only middle-core ownership;
the ordered cross-join and all-offset coverage requirements remain separate
physical gates.

## 7. Exact small cases

The accompanying verifier contains complete exact factors at \(b=3\) and
\(b=5\).  Here are the certificates themselves.  For \(b=3\), take
\(\Omega=\{0,1,\ldots,5\}\) and the following five labels:

\[
\begin{array}{c|c|c|c}
r&v&X&Y\\ \hline
3&2&04&51\\
5&3&01&24\\
1&4&03&52\\
5&1&02&34\\
2&5&04&13
\end{array}
\]

Their expansions by (1.1) partition all \({6\choose3}=20\) middle
vertices.  For \(b=5\), take \(\Omega=\{0,1,\ldots,9\}\), set

\[
                    p=8,\qquad q=9,\qquad R=(0,1,\ldots,7),
\]

and take the 18 packets from Theorem 5.1 in this labeling.  Adjoin the
following 24 residual packet labels.  Each row is \((r,v;X;Y)\) in the
notation of (1.1):

\[
\begin{array}{c|c|c|c}
r&v&X&Y\\ \hline
3&7&6518&0924\\5&2&7380&4916\\3&0&7925&8461\\
4&2&5318&9076\\8&7&0169&5234\\4&6&1738&0295\\
4&5&3096&2178\\4&1&3782&9065\\8&4&0659&7123\\
4&6&8152&3907\\1&4&7095&3826\\7&2&4860&9351\\
6&4&5218&7930\\6&1&3845&0972\\8&0&3142&9576\\
8&0&6124&9735\\0&1&8276&9354\\3&5&1079&2486\\
0&3&8517&9462\\0&2&4519&3678\\2&3&5496&7810\\
2&5&3691&0748\\2&1&5087&4936\\6&2&3149&7850
\end{array}                                             \tag{7.1}
\]

In both tables, concatenated digits denote ordered tuples; for example,
`6518` means \((6,5,1,8)\), not the integer 6518.  Direct expansion of
(1.1) shows that these 24 packets
partition the 144 vertices left by the Catalan subfactor.  The verifier
checks this expansion against all \({10\choose5}=252\) middle vertices.
Thus the phase-packet hypergraph has a perfect matching for \(b=3,5\).
The certificate is finite evidence only; no induction from it is claimed.

## 8. Two shifted primitive banks

The construction above can be enlarged without any probabilistic deletion.
Continue to write

\[
 R=(1,2,\ldots,2k),\qquad k=b-1,
\]

and retain the distinguished coordinates \(p,q\).  For a primitive Dyck
root \(x=1u0\), where \(u\in D^0_{2k-2}\), form the primal packet (3.1) on
each of the following two ordered punctured grounds:

\[
 R_0=(2,3,\ldots,2k,q),\qquad
 R_1=(3,4,\ldots,2k,1,q).                         \tag{8.1}
\]

In both cases the repeated coordinate is \(p\).  The omitted coordinate is
respectively \(1\) and \(2\).  Call the resulting packets
\(\mathcal A_x\) and \(\mathcal B_x\).  Retain every \(\mathcal A_x\), and
retain every \(\mathcal B_x\) except the packet whose root is

\[
                         x_*=1(10)^{k-1}0.           \tag{8.2}
\]

### Proposition 8.1 (shifted-bank disjointness)

The \(C_{k-1}\) packets \(\mathcal A_x\) and the \(C_{k-1}-1\) retained
packets \(\mathcal B_x\) are mutually vertex-disjoint.  They are also
disjoint from every packet in Propositions 3.1 and 4.1.

#### Proof

Each family by itself is a subfamily of the complete punctured bank in
Proposition 3.1, transported to the corresponding ordered ground in (8.1).
Thus its members are genuine phase packets and are pairwise disjoint within
that family.  Lemma 2.1(4) says that the last coordinate \(q\) of either
ground is the first added coordinate.  It remains in every upper vertex.
The first coordinate of either ground is the last removed coordinate and
also remains in every upper vertex.

We now compare the four banks.  Encode subsets of \(R\) by binary words in
the displayed base order.  Relative to membership in \((p,q)\), the primal
bank of Proposition 3.1 has type \(00\) internally and type \(10\) at both
ends.  The dual bank of Proposition 4.1 has types \(10,11,01\) at its first
end, internally, and at its last end.  Both shifted banks have types
\(10,01,11\) in those three locations.  Consequently only locations of the
same displayed type can collide.

For \(x=1u0\), the first \(\mathcal A_x\) endpoint has base word

\[
                              01u.                   \tag{8.3}
\]

It is not Dyck because its first step is down.  It is not anti-Dyck either:
after the initial \(01\) the height is zero, and the nonempty Dyck word
\(u\) immediately rises above zero.  Hence (8.3) is not a primal endpoint.
A dual first endpoint has word \(1\bar v0\), so it cannot equal (8.3).

Every internal \(\mathcal A_x\) vertex contains \(q\) and omits coordinate
\(1\).  A dual last endpoint is \(q\) together with a primitive Dyck root
\(1v0\), and therefore contains coordinate \(1\).  These vertices cannot
collide.  After removing \(p,q\), the last \(\mathcal A_x\) endpoint has
base word

\[
                              00\bar u.               \tag{8.4}
\]

If it were a dual internal vertex, its complement \(11u\) in \(R\) would
be one of the upper sets \(T_i(y)\) belonging to a primitive root \(y\).
But

\[
                         T_0(10u)=11u:                \tag{8.5}
\]

the word \(10u\) is Dyck, and the selector \(g\) changes its second step
from zero to one.  Lemma 2.1(3) gives a unique owner to every upper set, and
\(10u\) is nonprimitive.  Thus (8.4) cannot collide with a dual internal
vertex.  This proves that the entire \(\mathcal A\)-bank is disjoint from
the first two banks.

Let \(u^-\) be \(u\) with its final zero deleted.  The first
\(\mathcal B_x\) endpoint has base word

\[
                              001u^-.                 \tag{8.6}
\]

It cannot be Dyck and cannot equal a dual first endpoint, which starts with
one.  It is anti-Dyck precisely when \(u\) never rises above height one.
Indeed the initial \(00\) lowers the height to \(-2\), the next one raises
it to \(-1\), and the remaining prefixes are the proper prefixes of \(u\).
A Dyck word has maximum height at most one exactly when it is
\((10)^{k-1}\).  Hence the sole collision with a primal endpoint is the
packet (8.2), which was deleted.

Every internal \(\mathcal B_x\) vertex omits coordinate \(2\), whereas a
dual last endpoint has primitive root \(1v0\) and therefore begins with
\(11\).  The two cannot collide.  After removing \(p,q\), the last
\(\mathcal B_x\) endpoint begins with \(1\), whereas every dual internal
vertex omits coordinate \(1\): by Lemma 2.1(4), coordinate \(1\) is the
last removed coordinate and hence belongs to every \(T_i\), so it belongs
to no complement \(Z_i\).  Thus the retained \(\mathcal B\)-bank is
disjoint from the first two banks.

Finally, an internal \(\mathcal A_x\) vertex contains coordinate \(2\),
the first coordinate of \(R_0\), while every internal
\(\mathcal B_y\) vertex omits coordinate \(2\).  Their first endpoints
begin respectively with \(01\) and \(00\), and, after deleting \(p,q\),
their last endpoints begin respectively with \(0\) and \(1\).  Therefore
the two shifted banks are disjoint from one another. \(\square\)

### Theorem 8.2 (four-Catalan-bank subfactor)

For every \(b\ge3\), the phase-packet hypergraph on
\({\Omega\choose b}\) has an explicit matching of size

\[
                 \boxed{C_{b-1}+3C_{b-2}-2}.          \tag{8.7}
\]

It covers the fraction

\[
 \boxed{
 {C_{b-1}+3C_{b-2}-2\over C_b}
 ={b+1\over2(2b-1)}
  +{3b(b+1)\over4(2b-1)(2b-3)}-{2\over C_b}
 ={7\over16}+O(b^{-1}).}                              \tag{8.8}
\]

#### Proof

Take the union of the banks in Propositions 3.1, 4.1, and 8.1.  Their
sizes are respectively

\[
                         C_{b-1},\quad C_{b-2}-1,\quad
                         C_{b-2},\quad C_{b-2}-1.
\]

Proposition 8.1 proves disjointness, hence (8.7).  Divide by the perfect
factor size \(C_b\) from (5.3) and use the two consecutive Catalan ratios
to obtain (8.8). \(\square\)

The checker
`scratch/verify_gate_c_phase_packet_four_banks_20260823.py` constructs and
validates all four banks for every \(3\le b\le10\).  It verifies each
packet against its explicit \((r,v;X;Y)\) label and checks global vertex
disjointness and the count (8.7).
